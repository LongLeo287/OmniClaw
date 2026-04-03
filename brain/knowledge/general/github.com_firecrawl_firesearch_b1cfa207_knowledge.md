---
id: github.com-firecrawl-firesearch-b1cfa207-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:50.038653
---

# KNOWLEDGE EXTRACT: github.com_firecrawl_firesearch_b1cfa207
> **Extracted on:** 2026-04-01 12:51:44
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007522071/github.com_firecrawl_firesearch_b1cfa207

---

## File: `.gitignore`
```
# See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

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

# misc
.DS_Store
*.pem

# debug
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.pnpm-debug.log*

# env files (can opt-in for committing if needed)
.env*

# vercel
.vercel

# typescript
*.tsbuildinfo
next-env.d.ts
```

## File: `README.md`
```markdown
# Firesearch - AI-Powered Deep Research Tool

<div align="center">
  <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2F2YWo4amdieGVnOXR3aGM5ZnBlcDZvbnRjNW1vNmtpeWNhc3VtbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Jw7Q08ll8Vh0BoApI8/giphy.gif" alt="Firesearch Demo" width="100%" />
</div>

Comprehensive web research powered by [Firecrawl](https://www.firecrawl.dev/) and [LangGraph](https://www.langchain.com/langgraph)

## Technologies

- **Firecrawl**: Multi-source web content extraction
- **OpenAI GPT-4o**: Search planning and follow-up generation
- **Next.js 15**: Modern React framework with App Router

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fmendableai%2Ffiresearch&env=FIRECRAWL_API_KEY,OPENAI_API_KEY&envDescription=API%20keys%20required%20for%20Firesearch&envLink=https%3A%2F%2Fgithub.com%2Fmendableai%2Ffiresearch%23required-api-keys)

## Setup

### Required API Keys

| Service | Purpose | Get Key |
|---------|---------|---------|
| Firecrawl | Web scraping and content extraction | [firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys) |
| OpenAI | Search planning and summarization | [platform.openai.com/api-keys](https://platform.openai.com/api-keys) |

### Quick Start

1. Clone this repository
2. Create a `.env.local` file with your API keys:
   ```
   FIRECRAWL_API_KEY=your_firecrawl_key
   OPENAI_API_KEY=your_openai_key
   ```
3. Install dependencies: `npm install` or `yarn install`
4. Run the development server: `npm run dev` or `yarn dev`

## How It Works

### Architecture Overview

```mermaid
flowchart TB
    Query["'Compare Samsung Galaxy S25<br/>and iPhone 16'"]:::query
    
    Query --> Break
    
    Break["🔍 Break into Sub-Questions"]:::primary
    
    subgraph SubQ["🌐 Search Queries"]
        S1["iPhone 16 Pro specs features"]:::search
        S2["Samsung Galaxy S25 Ultra specs"]:::search
        S3["iPhone 16 vs Galaxy S25 comparison"]:::search
    end
    
    Break --> SubQ
    
    subgraph FC["🔥 Firecrawl API Calls"]
        FC1["Firecrawl /search API<br/>Query 1"]:::firecrawl
        FC2["Firecrawl /search API<br/>Query 2"]:::firecrawl
        FC3["Firecrawl /search API<br/>Query 3"]:::firecrawl
    end
    
    S1 --> FC1
    S2 --> FC2
    S3 --> FC3
    
    subgraph Sources["📄 Sources Found"]
        R1["Apple.com ✓<br/>The Verge ✓<br/>CNET ✓"]:::source
        R2["GSMArena ✓<br/>TechRadar ✓<br/>Samsung.com ✓"]:::source
        R3["AndroidAuth ✓<br/>TomsGuide ✓"]:::source
    end
    
    FC1 --> R1
    FC2 --> R2
    FC3 --> R3
    
    subgraph Valid["✅ Answer Validation"]
        V1["iPhone 16 specs ✓ (0.95)"]:::good
        V2["S25 specs ✓ (0.9)"]:::good
        V3["S25 price ❌ (0.3)"]:::bad
    end
    
    Sources --> Valid
    
    Valid --> Retry
    
    Retry{"Need info:<br/>S25 pricing?"}:::check
    
    subgraph Strat["🧠 Alternative Strategy"]
        Original["Original: 'Galaxy S25 price'<br/>❌ No specific pricing found"]:::bad
        NewTerms["Try: 'Galaxy S25 MSRP cost'<br/>'Samsung S25 pricing leak'<br/>'S25 vs S24 price comparison'"]:::strategy
    end
    
    Retry -->|Yes| Strat
    
    subgraph Retry2["🔄 Retry Searches"]
        Alt1["Galaxy S25 MSRP retail"]:::search
        Alt2["Samsung S25 pricing leak"]:::search
        Alt3["S25 vs S24 price comparison"]:::search
    end
    
    Strat --> Retry2
    
    subgraph FC2G["🔥 Retry API Calls"]
        FC4["Firecrawl /search API<br/>Alt Query 1"]:::firecrawl
        FC5["Firecrawl /search API<br/>Alt Query 2"]:::firecrawl
        FC6["Firecrawl /search API<br/>Alt Query 3"]:::firecrawl
    end
    
    Alt1 --> FC4
    Alt2 --> FC5
    Alt3 --> FC6
    
    Results2["SamMobile ✓ ($899 leak)<br/>9to5Google ✓ ($100 more)<br/>PhoneArena ✓ ($899)"]:::source
    
    FC4 --> Results2
    FC5 --> Results2
    FC6 --> Results2
    
    Final["All answers found ✓<br/>S25 price: $899"]:::good
    
    Results2 --> Final
    
    Synthesis["LLM synthesizes response"]:::synthesis
    
    Final --> Synthesis
    
    FollowUp["Generate follow-up questions"]:::primary
    
    Synthesis --> FollowUp
    
    Citations["List citations [1-10]"]:::primary
    
    FollowUp --> Citations
    
    Answer["Complete response delivered"]:::answer
    
    Citations --> Answer
    
    %% No path - skip retry and go straight to synthesis
    Retry -->|No| Synthesis
    
    classDef query fill:#ff8c42,stroke:#ff6b1a,stroke-width:3px,color:#fff
    classDef subq fill:#ffd4b3,stroke:#ff6b1a,stroke-width:1px,color:#333
    classDef search fill:#ff8c42,stroke:#ff6b1a,stroke-width:2px,color:#fff
    classDef source fill:#3a4a5c,stroke:#2c3a47,stroke-width:2px,color:#fff
    classDef check fill:#ffeb3b,stroke:#fbc02d,stroke-width:2px,color:#333
    classDef good fill:#4caf50,stroke:#388e3c,stroke-width:2px,color:#fff
    classDef bad fill:#f44336,stroke:#d32f2f,stroke-width:2px,color:#fff
    classDef strategy fill:#9c27b0,stroke:#7b1fa2,stroke-width:2px,color:#fff
    classDef synthesis fill:#ff8c42,stroke:#ff6b1a,stroke-width:3px,color:#fff
    classDef answer fill:#3a4a5c,stroke:#2c3a47,stroke-width:3px,color:#fff
    classDef firecrawl fill:#ff6b1a,stroke:#ff4500,stroke-width:3px,color:#fff
    classDef label fill:none,stroke:none,color:#666,font-weight:bold
```

### Process Flow

1. **Break Down** - Complex queries split into focused sub-questions
2. **Search** - Multiple searches via Firecrawl API for comprehensive coverage
3. **Extract** - Markdown content extracted from web sources
4. **Validate** - Check if sources actually answer the questions (0.7+ confidence)
5. **Retry** - Alternative search terms for unanswered questions (max 2 attempts)
6. **Synthesize** - GPT-4o combines findings into cited answer

### Key Features

- **Smart Search** - Breaks complex queries into multiple focused searches
- **Answer Validation** - Verifies sources contain actual answers (0.7+ confidence)
- **Auto-Retry** - Alternative search terms for unanswered questions
- **Real-time Progress** - Live updates as searches complete
- **Full Citations** - Every fact linked to its source
- **Context Memory** - Follow-up questions maintain conversation context

### Configuration

Customize search behavior by modifying [`lib/config.ts`](lib/config.ts):

```typescript
export const SEARCH_CONFIG = {
  // Search Settings
  MAX_SEARCH_QUERIES: 12,        // Maximum number of search queries to generate
  MAX_SOURCES_PER_SEARCH: 4,     // Maximum sources to return per search query
  MAX_SOURCES_TO_SCRAPE: 3,      // Maximum sources to scrape for additional content
  
  // Content Processing
  MIN_CONTENT_LENGTH: 100,       // Minimum content length to consider valid
  SUMMARY_CHAR_LIMIT: 100,       // Character limit for source summaries
  
  // Retry Logic
  MAX_RETRIES: 2,                // Maximum retry attempts for failed operations
  MAX_SEARCH_ATTEMPTS: 2,        // Maximum attempts to find answers via search
  MIN_ANSWER_CONFIDENCE: 0.7,    // Minimum confidence (0-1) that a question was answered
  
  // Timeouts
  SCRAPE_TIMEOUT: 15000,         // Timeout for scraping operations (ms)
} as const;
```

### Firecrawl API Integration

Firesearch leverages Firecrawl's powerful `/search` endpoint:

#### `/search` - Web Search with Content
- **Purpose**: Finds relevant URLs AND extracts markdown content in one call
- **Usage**: Each decomposed query is sent to find 6-8 relevant sources with content
- **Response**: Returns URLs with titles, snippets, AND full markdown content
- **Key Feature**: The `scrapeOptions` parameter enables content extraction during search
- **Example**:
  ```
  POST /search
  {
    "query": "iPhone 16 specs pricing",
    "limit": 8,
    "scrapeOptions": {
      "formats": ["markdown"]
    }
  }
  ```

### Search Strategies

When initial results are insufficient, the system automatically tries:
- **Broaden Keywords**: Removes specific terms for wider results
- **Narrow Focus**: Adds specific terms to target missing aspects
- **Synonyms**: Uses alternative terms and phrases
- **Rephrase**: Completely reformulates the query
- **Decompose**: Breaks complex queries into sub-questions
- **Academic**: Adds scholarly terms for research-oriented results
- **Practical**: Focuses on tutorials and how-to guides

## Example Queries

- "Who are the founders of Firecrawl?"
- "When did NVIDIA release the RTX 4080 Super?"
- "Compare the latest iPhone, Samsung Galaxy, and Google Pixel flagship features"

## License

MIT License
```

## File: `components.json`
```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "",
    "css": "app/globals.css",
    "baseColor": "neutral",
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

## File: `next.config.ts`
```typescript
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'www.google.com',
        pathname: '/s2/favicons**',
      },
    ],
  },
};

export default nextConfig;
```

## File: `package.json`
```json
{
  "name": "firecrawl-template",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev --turbopack",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "benchmark": "tsx eval/benchmark-runner.ts",
    "benchmark:quick": "tsx eval/benchmark-runner.ts factual_queries",
    "test:firecrawl": "tsx eval/test-firecrawl-simple.ts"
  },
  "dependencies": {
    "@ai-sdk/google": "^1.2.18",
    "@ai-sdk/openai": "^1.3.22",
    "@fal-ai/client": "^1.4.0",
    "@langchain/core": "^0.3.57",
    "@langchain/langgraph": "^0.2.74",
    "@langchain/openai": "^0.5.11",
    "@mendable/firecrawl-js": "^1.25.1",
    "@radix-ui/react-dialog": "^1.1.13",
    "@radix-ui/react-label": "^2.1.6",
    "@radix-ui/react-popover": "^1.1.13",
    "@radix-ui/react-scroll-area": "^1.2.8",
    "@radix-ui/react-select": "^2.2.4",
    "@radix-ui/react-separator": "^1.1.6",
    "@radix-ui/react-slot": "^1.2.2",
    "@radix-ui/react-switch": "^1.2.4",
    "@radix-ui/react-tabs": "^1.1.11",
    "@radix-ui/react-tooltip": "^1.2.6",
    "@types/uuid": "^10.0.0",
    "@upstash/ratelimit": "^2.0.5",
    "@upstash/redis": "^1.34.9",
    "ai": "^4.3.16",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "lucide-react": "^0.511.0",
    "next": "15.3.2",
    "next-themes": "^0.4.6",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "sonner": "^2.0.3",
    "tailwind-merge": "^3.3.0",
    "tailwindcss-animate": "^1.0.7",
    "uuid": "^11.1.0",
    "vaul": "^1.1.2"
  },
  "devDependencies": {
    "@eslint/eslintrc": "^3",
    "@shadcn/ui": "^0.0.4",
    "@tailwindcss/postcss": "^4",
    "@types/node": "^20",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "eslint": "^9",
    "eslint-config-next": "15.3.2",
    "tailwindcss": "^4",
    "tw-animate-css": "^1.3.0",
    "typescript": "^5"
  }
}
```

## File: `postcss.config.mjs`
```
const config = {
  plugins: ["@tailwindcss/postcss"],
};

export default config;
```

## File: `tailwind.config.ts`
```typescript
import type { Config } from "tailwindcss";
import defaultTheme from "tailwindcss/defaultTheme";

export default {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    container: {
      center: true,
      padding: "2rem",
      screens: {
        "2xl": "1400px",
      },
    },
    extend: {
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        },
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        },
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
        },
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
      fontFamily: {
        sans: ["var(--font-inter)", ...defaultTheme.fontFamily.sans],
        mono: defaultTheme.fontFamily.mono,
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
} satisfies Config; 
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

## File: `vercel.json`
```json
{
  "functions": {
    "app/api/*/route.ts": {
      "maxDuration": 300
    },
    "app/firesearch/search.tsx": {
      "maxDuration": 300
    }
  }
}
```

## File: `app/chat.tsx`
```tsx
'use client';

import { useState, useEffect, useRef } from 'react';
import { search } from './search';
import { readStreamableValue } from 'ai/rsc';
import { SearchDisplay } from './search-display';
import { SearchEvent, Source } from '@/lib/langgraph-search-engine';
import { MarkdownRenderer } from './markdown-renderer';
import { CitationTooltip } from './citation-tooltip';
import Image from 'next/image';
import { getFaviconUrl, getDefaultFavicon, markFaviconFailed } from '@/lib/favicon-utils';
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { toast } from "sonner";

const SUGGESTED_QUERIES = [
  "Who are the founders of Firecrawl?",
  "When did NVIDIA release the RTX 4080 Super?",
  "Compare the latest iPhone 16 and Samsung Galaxy S25",
  "Compare Claude 4 to OpenAI's o3"
];

// Helper component for sources list
function SourcesList({ sources }: { sources: Source[] }) {
  const [showSourcesPanel, setShowSourcesPanel] = useState(false);
  const [expandedSourceIndex, setExpandedSourceIndex] = useState<number | null>(null);
  
  return (
    <>
      {/* Sources button with favicon preview */}
      <div className="mt-6 flex items-center gap-3">
        <div className="flex -space-x-2">
          {(() => {
            // Get unique domains
            const uniqueDomains = new Map<string, Source>();
            sources.forEach(source => {
              try {
                const domain = new URL(source.url).hostname;
                if (!uniqueDomains.has(domain)) {
                  uniqueDomains.set(domain, source);
                }
              } catch {}
            });
            const uniqueSources = Array.from(uniqueDomains.values());
            
            return (
              <>
                {uniqueSources.slice(0, 5).map((source, i) => (
                  <Image 
                    key={i}
                    src={getFaviconUrl(source.url)} 
                    alt=""
                    width={24}
                    height={24}
                    className="w-6 h-6 rounded-full border-2 border-white dark:border-gray-900 bg-white"
                    style={{ zIndex: 5 - i }}
                    onError={(e) => {
                      const img = e.target as HTMLImageElement;
                      img.src = getDefaultFavicon(24);
                      markFaviconFailed(source.url);
                    }}
                  />
                ))}
                {uniqueSources.length > 5 && (
                  <div className="w-6 h-6 rounded-full border-2 border-white dark:border-gray-900 bg-gray-200 dark:bg-gray-700 flex items-center justify-center">
                    <span className="text-[10px] font-medium text-gray-600 dark:text-gray-300">+{uniqueSources.length - 5}</span>
                  </div>
                )}
              </>
            );
          })()}
        </div>
        <button
          onClick={() => setShowSourcesPanel(true)}
          className="text-sm text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-200 flex items-center gap-2"
        >
          <span>View {sources.length} sources & page contents</span>
          <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
          </svg>
        </button>
      </div>

      {/* Click-away overlay */}
      {showSourcesPanel && (
        <div 
          className="fixed inset-0 z-30"
          onClick={() => setShowSourcesPanel(false)}
        />
      )}
      
      {/* Sources Panel */}
      <div className={`fixed inset-y-0 right-0 w-96 bg-white dark:bg-gray-900 border-l border-gray-200 dark:border-gray-700 transform transition-transform duration-300 ease-in-out ${
        showSourcesPanel ? 'translate-x-0' : 'translate-x-full'
      } z-40 overflow-y-auto scrollbar-hide`}>
        <div className="p-6">
          <div className="flex items-center justify-between mb-6">
            <h3 className="text-lg font-semibold">Sources ({sources.length})</h3>
            <button
              onClick={() => setShowSourcesPanel(false)}
              className="p-2 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg transition-colors"
            >
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
          
          <div className="space-y-2">
            {sources.map((source, i) => (
              <div key={i} className="border border-gray-200 dark:border-gray-700 rounded-lg overflow-hidden transition-colors">
                <div 
                  className={`p-3 hover:bg-gray-50 dark:hover:bg-gray-800 cursor-pointer ${expandedSourceIndex === i ? '' : 'rounded-lg'}`}
                  onClick={() => setExpandedSourceIndex(expandedSourceIndex === i ? null : i)}
                >
                  <div className="flex items-start gap-3">
                    <span className="text-sm font-medium text-orange-600 mt-0.5">[{i + 1}]</span>
                    <Image 
                      src={getFaviconUrl(source.url)} 
                      alt=""
                      width={20}
                      height={20}
                      className="w-5 h-5 mt-0.5 flex-shrink-0"
                      onError={(e) => {
                        const img = e.target as HTMLImageElement;
                        img.src = getDefaultFavicon(20);
                        markFaviconFailed(source.url);
                      }}
                    />
                    <div className="flex-1 min-w-0">
                      <a 
                        href={source.url} 
                        target="_blank" 
                        rel="noopener noreferrer"
                        className="font-medium text-sm text-gray-900 dark:text-gray-100 hover:text-orange-600 dark:hover:text-orange-400 line-clamp-2"
                        onClick={(e) => e.stopPropagation()}
                      >
                        {source.title}
                      </a>
                      <p className="text-xs text-gray-500 dark:text-gray-400 mt-1 truncate">
                        {new URL(source.url).hostname}
                      </p>
                    </div>
                    <svg 
                      className={`w-4 h-4 text-gray-400 transition-transform ${expandedSourceIndex === i ? 'rotate-180' : ''}`} 
                      fill="none" 
                      stroke="currentColor" 
                      viewBox="0 0 24 24"
                    >
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                    </svg>
                  </div>
                </div>
                
                {expandedSourceIndex === i && source.content && (
                  <div className="border-t border-gray-200 dark:border-gray-700">
                    <div className="px-4 py-2 border-b border-gray-100 dark:border-gray-800 bg-gray-50 dark:bg-gray-800/50">
                      <span className="text-xs text-gray-500 dark:text-gray-400">
                        {source.content.length.toLocaleString()} characters
                      </span>
                    </div>
                    <div className="p-4 max-h-96 overflow-y-auto scrollbar-hide">
                      <div className="prose prose-sm dark:prose-invert max-w-none">
                        <MarkdownRenderer content={source.content} />
                      </div>
                    </div>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      </div>
    </>
  );
}

export function Chat() {
  const [messages, setMessages] = useState<Array<{
    id: string;
    role: 'user' | 'assistant';
    content: string | React.ReactNode;
    isSearch?: boolean;
    searchResults?: string; // Store search results for context
  }>>([]);
  const [input, setInput] = useState('');
  const [isSearching, setIsSearching] = useState(false);
  const [showSuggestions, setShowSuggestions] = useState(false);
  const [hasShownSuggestions, setHasShownSuggestions] = useState(false);
  const [firecrawlApiKey, setFirecrawlApiKey] = useState<string>('');
  const [hasApiKey, setHasApiKey] = useState<boolean>(false);
  const [showApiKeyModal, setShowApiKeyModal] = useState<boolean>(false);
  const [, setIsCheckingEnv] = useState<boolean>(true);
  const [pendingQuery, setPendingQuery] = useState<string>('');
  const messagesContainerRef = useRef<HTMLDivElement>(null);

  const handleSelectSuggestion = (suggestion: string) => {
    setInput(suggestion);
    setShowSuggestions(false);
  };

  // Check for environment variables on mount
  useEffect(() => {
    const checkEnvironment = async () => {
      setIsCheckingEnv(true);
      try {
        const response = await fetch('/api/check-env');
        const data = await response.json();
        
        if (data.environmentStatus) {
          // Only check for Firecrawl API key since we can pass it from frontend
          // OpenAI and Anthropic keys must be in environment
          setHasApiKey(data.environmentStatus.FIRECRAWL_API_KEY);
        }
      } catch (error) {
        console.error('Failed to check environment:', error);
        setHasApiKey(false);
      } finally {
        setIsCheckingEnv(false);
      }
    };

    checkEnvironment();
  }, []);

  // Auto-scroll to bottom when messages change
  useEffect(() => {
    if (messagesContainerRef.current) {
      messagesContainerRef.current.scrollTop = messagesContainerRef.current.scrollHeight;
    }
  }, [messages]);

  const saveApiKey = () => {
    if (firecrawlApiKey.trim()) {
      setHasApiKey(true);
      setShowApiKeyModal(false);
      toast.success('API key saved! Starting your search...');
      
      // Continue with the pending query
      if (pendingQuery) {
        performSearch(pendingQuery);
        setPendingQuery('');
      }
    }
  };

  // Listen for follow-up question events
  useEffect(() => {
    const handleFollowUpQuestion = async (event: Event) => {
      const customEvent = event as CustomEvent;
      const question = customEvent.detail.question;
      setInput(question);
      
      // Trigger the search immediately
      setTimeout(() => {
        const form = document.querySelector('form');
        if (form) {
          form.dispatchEvent(new Event('submit', { cancelable: true, bubbles: true }));
        }
      }, 100);
    };

    document.addEventListener('followUpQuestion', handleFollowUpQuestion);
    return () => {
      document.removeEventListener('followUpQuestion', handleFollowUpQuestion);
    };
  }, []);

  const performSearch = async (query: string) => {
    setIsSearching(true);

    // Create assistant message with search display
    const assistantMsgId = (Date.now() + 1).toString();
    const events: SearchEvent[] = [];
    
    setMessages(prev => [...prev, {
      id: assistantMsgId,
      role: 'assistant',
      content: <SearchDisplay events={events} />,
      isSearch: true
    }]);

    try {
      // Build context from previous messages by pairing user queries with assistant responses
      const conversationContext: Array<{ query: string; response: string }> = [];
      
      for (let i = 0; i < messages.length; i++) {
        const msg = messages[i];
        // Find user messages followed by assistant messages with search results
        if (msg.role === 'user' && i + 1 < messages.length) {
          const nextMsg = messages[i + 1];
          if (nextMsg.role === 'assistant' && nextMsg.searchResults) {
            conversationContext.push({
              query: msg.content as string,
              response: nextMsg.searchResults
            });
          }
        }
      }
      
      // Get search stream with context
      // Pass the API key only if user provided one, otherwise let server use env var
      const { stream } = await search(query, conversationContext, firecrawlApiKey || undefined);
      let finalContent = '';
      
      // Read stream and update events
      let streamingStarted = false;
      const resultMsgId = (Date.now() + 2).toString();
      
      for await (const event of readStreamableValue(stream)) {
        if (event) {
          events.push(event);
          
          // Handle content streaming
          if (event.type === 'content-chunk') {
            const content = events
              .filter(e => e.type === 'content-chunk')
              .map(e => e.type === 'content-chunk' ? e.chunk : '')
              .join('');
            
            if (!streamingStarted) {
              streamingStarted = true;
              // Add new message for streaming content
              setMessages(prev => [...prev, {
                id: resultMsgId,
                role: 'assistant',
                content: <MarkdownRenderer content={content} streaming={true} />,
                isSearch: false
              }]);
            } else {
              // Update streaming message
              setMessages(prev => prev.map(msg => 
                msg.id === resultMsgId 
                  ? { ...msg, content: <MarkdownRenderer content={content} streaming={true} /> }
                  : msg
              ));
            }
          }
          
          // Capture final result
          if (event.type === 'final-result') {
            finalContent = event.content;
            
            // Update the streaming message with final content and sources
            setMessages(prev => prev.map(msg => 
              msg.id === resultMsgId 
                ? {
                    ...msg,
                    content: (
                      <div className="space-y-4">
                        <div className="prose prose-sm dark:prose-invert max-w-none">
                          <MarkdownRenderer content={finalContent} />
                        </div>
                        <CitationTooltip sources={event.sources || []} />
                        
                        {/* Follow-up Questions */}
                        {event.followUpQuestions && event.followUpQuestions.length > 0 && (
                          <div className="mt-8 pt-6 border-t border-gray-200 dark:border-gray-700">
                            <h3 className="text-sm font-semibold text-gray-700 dark:text-gray-300 mb-3">
                              Follow-up questions
                            </h3>
                            <div className="space-y-2">
                              {event.followUpQuestions.map((question, index) => (
                                <button
                                  key={index}
                                  onClick={() => {
                                    const evt = new CustomEvent('followUpQuestion', { 
                                      detail: { question },
                                      bubbles: true 
                                    });
                                    document.dispatchEvent(evt);
                                  }}
                                  className="block w-full text-left px-4 py-3 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-orange-300 dark:hover:border-orange-700 hover:bg-orange-50 dark:hover:bg-orange-900/10 transition-colors group"
                                >
                                  <div className="flex items-center justify-between">
                                    <span className="text-sm text-gray-700 dark:text-gray-300 group-hover:text-gray-900 dark:group-hover:text-gray-100">
                                      {question}
                                    </span>
                                    <svg className="w-4 h-4 text-gray-400 group-hover:text-orange-500 flex-shrink-0 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                                    </svg>
                                  </div>
                                </button>
                              ))}
                            </div>
                          </div>
                        )}
                        
                        {/* Sources */}
                        <SourcesList sources={event.sources || []} />
                      </div>
                    ),
                    searchResults: finalContent
                  }
                : msg
            ));
          }
          
          // Update research box with new events
          setMessages(prev => prev.map(msg => 
            msg.id === assistantMsgId 
              ? { ...msg, content: <SearchDisplay events={[...events]} />, searchResults: finalContent }
              : msg
          ));
        }
      }
    } catch (error) {
      console.error('Search error:', error);
      // Remove the search display message
      setMessages(prev => prev.filter(msg => msg.id !== assistantMsgId));
      
      // Show error message to user
      const errorMessage = error instanceof Error ? error.message : 'An error occurred during search';
      setMessages(prev => [...prev, {
        id: Date.now().toString(),
        role: 'assistant',
        content: (
          <div className="p-4 border border-red-200 dark:border-red-800 bg-red-50 dark:bg-red-900/20 rounded-lg">
            <p className="text-red-700 dark:text-red-300 font-medium">Search Error</p>
            <p className="text-red-600 dark:text-red-400 text-sm mt-1">{errorMessage}</p>
            {(errorMessage.includes('API key') || errorMessage.includes('OPENAI_API_KEY')) && (
              <p className="text-red-600 dark:text-red-400 text-sm mt-2">
                Please ensure all required API keys are set in your environment variables:
                <br />• OPENAI_API_KEY (for GPT-4o)
                <br />• ANTHROPIC_API_KEY (optional, for Claude)
                <br />• FIRECRAWL_API_KEY (can be provided via UI)
              </p>
            )}
          </div>
        ),
        isSearch: false
      }]);
    } finally {
      setIsSearching(false);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || isSearching) return;
    setShowSuggestions(false);

    const userMessage = input;
    setInput('');

    // Check if we have API key
    if (!hasApiKey) {
      // Store the query and show modal
      setPendingQuery(userMessage);
      setShowApiKeyModal(true);
      
      // Still add user message to show what they asked
      const userMsgId = Date.now().toString();
      setMessages(prev => [...prev, {
        id: userMsgId,
        role: 'user',
        content: userMessage,
        isSearch: true
      }]);
      return;
    }

    // Add user message
    const userMsgId = Date.now().toString();
    setMessages(prev => [...prev, {
      id: userMsgId,
      role: 'user',
      content: userMessage,
      isSearch: true
    }]);

    // Perform the search
    await performSearch(userMessage);
  };

  return (
    <div className="flex flex-col flex-1">
      {messages.length === 0 ? (
        // Center input when no messages
        <div className="flex-1 flex items-center justify-center px-4 sm:px-6 lg:px-8">
          <div className="w-full max-w-4xl">
            <form onSubmit={handleSubmit}>
              <div className="relative">
                <input
                  type="text"
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  onFocus={() => {
                    if (!hasShownSuggestions && messages.length === 0) {
                      setShowSuggestions(true);
                      setHasShownSuggestions(true);
                    }
                  }}
                  onBlur={() => setTimeout(() => setShowSuggestions(false), 200)}
                  placeholder="Enter query..."
                  className="w-full h-14 rounded-full border border-zinc-200 bg-white pl-6 pr-16 text-base ring-offset-white file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-zinc-500 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-orange-500 focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 dark:border-zinc-800 dark:bg-zinc-950 dark:ring-offset-zinc-950 dark:placeholder:text-zinc-400 dark:focus-visible:ring-orange-400 shadow-sm"
                  disabled={isSearching}
                />
                <button
                  type="submit"
                  disabled={isSearching || !input.trim()}
                  className="absolute right-2 top-2 h-10 w-10 bg-orange-500 hover:bg-orange-600 text-white rounded-full disabled:opacity-50 disabled:cursor-not-allowed transition-colors duration-200 flex items-center justify-center"
                >
                  {isSearching ? (
                    <svg className="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24">
                      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                  ) : (
                    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                    </svg>
                  )}
                </button>
                
                {/* Suggestions dropdown - only show on initial load */}
                {showSuggestions && !input && messages.length === 0 && (
                  <div className="absolute top-full mt-2 w-full bg-white dark:bg-zinc-900 rounded-2xl shadow-lg border border-zinc-200 dark:border-zinc-800 overflow-hidden">
                    <div className="p-2">
                      <p className="text-xs text-gray-500 dark:text-gray-400 px-3 py-2 font-medium">Try searching for:</p>
                      {SUGGESTED_QUERIES.map((suggestion, index) => (
                        <button
                          key={index}
                          type="button"
                          onClick={() => handleSelectSuggestion(suggestion)}
                          className="w-full text-left px-3 py-2.5 hover:bg-gray-50 dark:hover:bg-zinc-800 rounded-lg transition-colors text-sm text-gray-700 dark:text-gray-300"
                        >
                          <div className="flex items-center gap-2">
                            <svg className="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                            </svg>
                            <span className="line-clamp-1">{suggestion}</span>
                          </div>
                        </button>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            </form>
          </div>
        </div>
      ) : (
        <>
          {/* Messages */}
          <div className="flex-1 overflow-auto scrollbar-hide px-4 sm:px-6 lg:px-8 py-6">
            <div className="max-w-4xl mx-auto space-y-6">
              {messages.map(msg => (
                <div
                  key={msg.id}
                  className={`${
                    msg.role === 'user' 
                      ? 'flex justify-end' 
                      : 'w-full'
                  }`}
                >
                  {msg.role === 'user' ? (
                    <div className="max-w-2xl">
                      <span className="inline-block px-5 py-3 rounded-2xl bg-[#FBFAF9] dark:bg-zinc-800 text-[#36322F] dark:text-zinc-100">
                        {msg.content}
                      </span>
                    </div>
                  ) : (
                    <div className="w-full">{msg.content}</div>
                  )}
                </div>
              ))}
            </div>
          </div>

          {/* Input */}
          <div className="bg-white dark:bg-zinc-950 px-4 sm:px-6 lg:px-8 py-6">
            <form onSubmit={handleSubmit} className="max-w-4xl mx-auto">
          <div className="relative">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onFocus={() => {
                if (!hasShownSuggestions) {
                  setShowSuggestions(true);
                  setHasShownSuggestions(true);
                }
              }}
              onBlur={() => setTimeout(() => setShowSuggestions(false), 200)}
              placeholder="Enter query..."
              className="w-full h-14 rounded-full border border-zinc-200 bg-white pl-6 pr-16 text-base ring-offset-white file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-zinc-500 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-orange-500 focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 dark:border-zinc-800 dark:bg-zinc-950 dark:ring-offset-zinc-950 dark:placeholder:text-zinc-400 dark:focus-visible:ring-orange-400 shadow-sm"
              disabled={isSearching}
            />
            
            <button
              type="submit"
              disabled={!input.trim() || isSearching}
              className="absolute right-2 top-1/2 -translate-y-1/2 w-10 h-10 rounded-full bg-orange-500 hover:bg-orange-600 disabled:bg-gray-300 disabled:cursor-not-allowed text-white flex items-center justify-center transition-colors shadow-sm"
            >
              {isSearching ? (
                <svg className="animate-spin h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
              ) : (
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="20"
                  height="20"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <circle cx="11" cy="11" r="8" />
                  <path d="m21 21-4.35-4.35" />
                </svg>
              )}
            </button>
            
            {/* Suggestions dropdown - positioned to show above input */}
            {showSuggestions && !input && (
              <div className="absolute bottom-full mb-2 w-full bg-white dark:bg-zinc-900 rounded-2xl shadow-lg border border-zinc-200 dark:border-zinc-800 overflow-hidden">
                <div className="p-2">
                  <p className="text-xs text-gray-500 dark:text-gray-400 px-3 py-2 font-medium">Try searching for:</p>
                  {SUGGESTED_QUERIES.map((suggestion, index) => (
                    <button
                      key={index}
                      type="button"
                      onClick={() => handleSelectSuggestion(suggestion)}
                      className="w-full text-left px-3 py-2.5 hover:bg-gray-50 dark:hover:bg-zinc-800 rounded-lg transition-colors text-sm text-gray-700 dark:text-gray-300"
                    >
                      <div className="flex items-center gap-2">
                        <svg className="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                        </svg>
                        <span className="line-clamp-1">{suggestion}</span>
                      </div>
                    </button>
                  ))}
                </div>
              </div>
            )}
          </div>
        </form>
      </div>
        </>
      )}

      {/* API Key Modal */}
      <Dialog open={showApiKeyModal} onOpenChange={setShowApiKeyModal}>
        <DialogContent className="sm:max-w-[425px] bg-white dark:bg-gray-950 text-gray-900 dark:text-gray-100">
          <DialogHeader>
            <DialogTitle>Firecrawl API Key Required</DialogTitle>
            <DialogDescription>
              To use Firesearch, you need a Firecrawl API key. You can get one for free.
            </DialogDescription>
          </DialogHeader>
          <div className="grid gap-4 py-4">
            <div className="space-y-2">
              <Button
                onClick={() => window.open('https://www.firecrawl.dev/app/api-keys', '_blank')}
                className="w-full"
                variant="code"
              >
                Get your free API key from Firecrawl →
              </Button>
            </div>
            <div className="space-y-2">
              <label htmlFor="apiKey" className="text-sm font-medium">
                Enter your API key
              </label>
              <Input
                id="apiKey"
                type="password"
                value={firecrawlApiKey}
                onChange={(e) => setFirecrawlApiKey(e.target.value)}
                placeholder="fc-..."
                className="w-full"
              />
            </div>
          </div>
          <div className="flex gap-2 justify-end">
            <Button
              variant="code"
              onClick={() => setShowApiKeyModal(false)}
            >
              Cancel
            </Button>
            <Button 
              variant="orange"
              onClick={saveApiKey}
              disabled={!firecrawlApiKey.trim()}
            >
              Save and Continue
            </Button>
          </div>
        </DialogContent>
      </Dialog>
    </div>
  );
}
```

## File: `app/citation-tooltip.tsx`
```tsx
'use client';

import { useState, useRef, useEffect } from 'react';
import Image from 'next/image';
import { Source } from '@/lib/langgraph-search-engine';
import { getFaviconUrl, getDefaultFavicon, markFaviconFailed } from '@/lib/favicon-utils';

interface CitationTooltipProps {
  sources: Source[];
}

export function CitationTooltip({ sources }: CitationTooltipProps) {
  const [tooltip, setTooltip] = useState<{ x: number; y: number; source: Source } | null>(null);
  const timeoutRef = useRef<NodeJS.Timeout | null>(null);

  useEffect(() => {
    const handleMouseOver = (e: MouseEvent) => {
      const target = e.target as HTMLElement;
      if (target.tagName === 'SUP' && target.className.includes('citation')) {
        const citationText = target.textContent?.match(/\d+/)?.[0];
        if (citationText) {
          const index = parseInt(citationText) - 1;
          const source = sources[index];
          if (source) {
            const rect = target.getBoundingClientRect();
            setTooltip({
              x: rect.left + rect.width / 2,
              y: rect.top,
              source
            });
          }
        }
      }
    };

    const handleMouseOut = (e: MouseEvent) => {
      const target = e.target as HTMLElement;
      if (target.tagName === 'SUP' && target.className.includes('citation')) {
        timeoutRef.current = setTimeout(() => {
          setTooltip(null);
        }, 200);
      }
    };

    document.addEventListener('mouseover', handleMouseOver);
    document.addEventListener('mouseout', handleMouseOut);

    return () => {
      document.removeEventListener('mouseover', handleMouseOver);
      document.removeEventListener('mouseout', handleMouseOut);
      if (timeoutRef.current) clearTimeout(timeoutRef.current);
    };
  }, [sources]);

  if (!tooltip) return null;

  const maxUrlLength = 50;
  const displayUrl = tooltip.source.url.length > maxUrlLength 
    ? tooltip.source.url.substring(0, maxUrlLength) + '...' 
    : tooltip.source.url;

  return (
    <div
      className="fixed z-50 pointer-events-none"
      style={{
        left: tooltip.x,
        top: tooltip.y - 8,
        transform: 'translate(-50%, -100%)'
      }}
      onMouseEnter={() => {
        if (timeoutRef.current) clearTimeout(timeoutRef.current);
      }}
      onMouseLeave={() => setTooltip(null)}
    >
      <div className="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-lg shadow-lg p-3 max-w-sm pointer-events-auto">
        <div className="flex items-start gap-3">
          <Image 
            src={getFaviconUrl(tooltip.source.url)} 
            alt=""
            width={20}
            height={20}
            className="w-5 h-5 mt-0.5 flex-shrink-0"
            onError={(e) => {
              const img = e.target as HTMLImageElement;
              img.src = getDefaultFavicon(20);
              markFaviconFailed(tooltip.source.url);
            }}
          />
          <div className="min-w-0">
            <p className="font-medium text-sm text-gray-900 dark:text-gray-100 break-words">
              {tooltip.source.title}
            </p>
            <p className="text-xs text-gray-500 dark:text-gray-400 mt-1 break-all">
              {displayUrl}
            </p>
          </div>
        </div>
      </div>
      {/* Arrow */}
      <div className="absolute left-1/2 -translate-x-1/2 -bottom-2">
        <div className="w-0 h-0 border-l-[6px] border-l-transparent border-r-[6px] border-r-transparent border-t-[6px] border-t-white dark:border-t-gray-800" />
      </div>
    </div>
  );
}
```

## File: `app/globals.css`
```css
@import "tailwindcss";
@import "tw-animate-css";

@custom-variant dark (&:is(.dark *));

@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --font-sans: var(--font-geist-sans);
  --font-mono: var(--font-geist-mono);
  --color-sidebar-ring: var(--sidebar-ring);
  --color-sidebar-border: var(--sidebar-border);
  --color-sidebar-accent-foreground: var(--sidebar-accent-foreground);
  --color-sidebar-accent: var(--sidebar-accent);
  --color-sidebar-primary-foreground: var(--sidebar-primary-foreground);
  --color-sidebar-primary: var(--sidebar-primary);
  --color-sidebar-foreground: var(--sidebar-foreground);
  --color-sidebar: var(--sidebar);
  --color-chart-5: var(--chart-5);
  --color-chart-4: var(--chart-4);
  --color-chart-3: var(--chart-3);
  --color-chart-2: var(--chart-2);
  --color-chart-1: var(--chart-1);
  --color-ring: var(--ring);
  --color-input: var(--input);
  --color-border: var(--border);
  --color-destructive: var(--destructive);
  --color-accent-foreground: var(--accent-foreground);
  --color-accent: var(--accent);
  --color-muted-foreground: var(--muted-foreground);
  --color-muted: var(--muted);
  --color-secondary-foreground: var(--secondary-foreground);
  --color-secondary: var(--secondary);
  --color-primary-foreground: var(--primary-foreground);
  --color-primary: var(--primary);
  --color-popover-foreground: var(--popover-foreground);
  --color-popover: var(--popover);
  --color-card-foreground: var(--card-foreground);
  --color-card: var(--card);
  --radius-sm: calc(var(--radius) - 4px);
  --radius-md: calc(var(--radius) - 2px);
  --radius-lg: var(--radius);
  --radius-xl: calc(var(--radius) + 4px);
}

@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 0 0% 10%;
    --card: 0 0% 100%;
    --card-foreground: 0 0% 10%;
    --popover: 0 0% 100%;
    --popover-foreground: 0 0% 10%;
    --primary: 350 65% 55%;
    --primary-foreground: 0 0% 100%;
    --secondary: 0 0% 96%;
    --secondary-foreground: 0 0% 10%;
    --muted: 0 0% 96%;
    --muted-foreground: 0 0% 45%;
    --accent: 0 0% 96%;
    --accent-foreground: 0 0% 10%;
    --destructive: 0 85% 60%;
    --destructive-foreground: 0 0% 100%;
    --border: 0 0% 90%;
    --input: 0 0% 90%;
    --ring: 350 65% 55%;
    --radius: 0.5rem;
    
    /* Animation durations and delays */
    --d-1: 150ms;
    --d-2: 300ms;
    --d-3: 500ms;
    --t-1: 200ms;
    --t-2: 400ms;
    --t-3: 600ms;
  }

  .dark {
    --background: 0 0% 5%;
    --foreground: 0 0% 98%;
    --card: 0 0% 5%;
    --card-foreground: 0 0% 98%;
    --popover: 0 0% 5%;
    --popover-foreground: 0 0% 98%;
    --primary: 350 65% 55%;
    --primary-foreground: 0 0% 100%;
    --secondary: 0 0% 12%;
    --secondary-foreground: 0 0% 98%;
    --muted: 0 0% 12%;
    --muted-foreground: 0 0% 63%;
    --accent: 0 0% 12%;
    --accent-foreground: 0 0% 98%;
    --destructive: 0 85% 60%;
    --destructive-foreground: 0 0% 100%;
    --border: 0 0% 20%;
    --input: 0 0% 20%;
    --ring: 350 65% 55%;
  }
}

@layer base {
  * {
    @apply border-border;
  }
  body {
    @apply bg-background text-foreground;
    font-feature-settings: "rlig" 1, "calt" 1;
  }
}

:root {
  --sidebar: hsl(0 0% 98%);
  --sidebar-foreground: hsl(240 5.3% 26.1%);
  --sidebar-primary: hsl(240 5.9% 10%);
  --sidebar-primary-foreground: hsl(0 0% 98%);
  --sidebar-accent: hsl(240 4.8% 95.9%);
  --sidebar-accent-foreground: hsl(240 5.9% 10%);
  --sidebar-border: hsl(220 13% 91%);
  --sidebar-ring: hsl(217.2 91.2% 59.8%);
}

.dark {
  --sidebar: hsl(240 5.9% 10%);
  --sidebar-foreground: hsl(240 4.8% 95.9%);
  --sidebar-primary: hsl(224.3 76.3% 48%);
  --sidebar-primary-foreground: hsl(0 0% 100%);
  --sidebar-accent: hsl(240 3.7% 15.9%);
  --sidebar-accent-foreground: hsl(240 4.8% 95.9%);
  --sidebar-border: hsl(240 3.7% 15.9%);
  --sidebar-ring: hsl(217.2 91.2% 59.8%);
}

@layer base {
  * {
    @apply border-border outline-ring/50;
  }
  body {
    @apply bg-background text-foreground;
  }
}

@keyframes text {
  to {
    background-position: 200% center;
  }
}

.animate-text {
  animation: text 5s ease infinite;
  background-size: 200% auto;
}

@keyframes fade-up {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-up {
  animation-name: fade-up;
  animation-fill-mode: forwards;
}

@keyframes fade-in {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes scale-in {
  from {
    transform: scale(0);
  }
  to {
    transform: scale(1);
  }
}

.animate-fade-in {
  animation: fade-in 0.3s ease-out forwards;
}

.animate-scale-in {
  animation: scale-in 0.2s ease-out;
}

@keyframes slide-down {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-slide-down {
  animation: slide-down 0.3s ease-out;
}

/* Hide scrollbars but keep functionality */
.scrollbar-hide {
  /* Hide scrollbar for Chrome, Safari and Opera */
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}

.scrollbar-hide::-webkit-scrollbar {
  display: none;
}

/* Thinking line animations */
@keyframes thinking-fade {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0;
  }
}

.thinking-transition {
  transition: opacity 300ms ease-in-out;
}
```

## File: `app/layout.tsx`
```tsx
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { cn } from "@/lib/utils";

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Firecrawl",
  description: "A Firecrawl template",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body
        suppressHydrationWarning={true}
        className={cn(
          "min-h-screen bg-background font-sans antialiased",
          inter.variable
        )}
      >
        <main className="">
          {children}
        </main>
      </body>
    </html>
  );
}
```

## File: `app/markdown-renderer.tsx`
```tsx
'use client';

import { memo } from 'react';

interface MarkdownRendererProps {
  content: string;
  streaming?: boolean;
}

export const MarkdownRenderer = memo(function MarkdownRenderer({ 
  content, 
  streaming = false 
}: MarkdownRendererProps) {
  // Simple markdown parsing
  const parseMarkdown = (text: string) => {
    // Handle links [text](url) - must come before citations
    let parsed = text.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer" class="text-orange-600 hover:text-orange-700 underline">$1</a>');
    
    // Handle citations [1], [2], etc.
    parsed = parsed.replace(/\[(\d+)\]/g, '<sup class="citation text-orange-600 cursor-pointer hover:text-orange-700">[$1]</sup>');
    
    // Bold text
    parsed = parsed.replace(/\*\*(.+?)\*\*/g, '<strong class="font-semibold">$1</strong>');
    
    // Italic text  
    parsed = parsed.replace(/\*(.+?)\*/g, '<em>$1</em>');
    
    // Headers (process in order from most specific to least)
    parsed = parsed.replace(/^#### (.+)$/gm, '<h4 class="text-sm font-semibold mt-3 mb-2">$1</h4>');
    parsed = parsed.replace(/^### (.+)$/gm, '<h3 class="text-base font-semibold mt-4 mb-2">$1</h3>');
    parsed = parsed.replace(/^## (.+)$/gm, '<h2 class="text-lg font-semibold mt-5 mb-2">$1</h2>');
    parsed = parsed.replace(/^# (.+)$/gm, '<h1 class="text-xl font-bold mt-6 mb-3">$1</h1>');
    
    // Handle list blocks with better multi-line support
    const listBlocks = parsed.split('\n');
    let inList = false;
    let listType = 'ul';
    const processedLines = [];
    
    for (let i = 0; i < listBlocks.length; i++) {
      const line = listBlocks[i];
      const bulletMatch = line.match(/^- (.+)$/);
      const numberMatch = line.match(/^(\d+)\. (.+)$/);
      const isListItem = bulletMatch || numberMatch;
      const isContinuation = inList && line.match(/^\s+/) && line.trim();
      
      if (isListItem && !inList) {
        listType = bulletMatch ? 'ul' : 'ol';
        processedLines.push(`<${listType} class="space-y-2 my-3 pl-0">`);
        inList = true;
      } else if (!isListItem && !isContinuation && inList && line.trim() === '') {
        // Empty line ends the list
        processedLines.push(`</${listType}>`);
        inList = false;
      }
      
      if (bulletMatch) {
        processedLines.push(`<li class="ml-5 list-disc">${bulletMatch[1]}</li>`);
      } else if (numberMatch) {
        processedLines.push(`<li class="ml-5 list-decimal">${numberMatch[2]}</li>`);
      } else if (isContinuation && inList) {
        // Append continuation to previous list item
        if (processedLines.length > 0 && processedLines[processedLines.length - 1].includes('<li')) {
          const lastLine = processedLines.pop();
          if (lastLine) {
            processedLines.push(lastLine.replace('</li>', ' ' + line.trim() + '</li>'));
          }
        }
      } else {
        processedLines.push(line);
      }
    }
    
    if (inList) {
      processedLines.push(`</${listType}>`);
    }
    
    parsed = processedLines.join('\n');
    
    // Code blocks
    parsed = parsed.replace(/```([\s\S]*?)```/g, '<pre class="bg-gray-100 dark:bg-gray-800 p-3 rounded-lg overflow-x-auto my-3"><code>$1</code></pre>');
    
    // Inline code
    parsed = parsed.replace(/`(.+?)`/g, '<code class="bg-gray-100 dark:bg-gray-800 px-1.5 py-0.5 rounded text-sm font-mono">$1</code>');
    
    // Paragraphs
    parsed = parsed.split('\n\n').map(para => {
      if (para.trim() && !para.includes('<h') && !para.includes('<ul') && !para.includes('<pre')) {
        return `<p class="mb-3">${para}</p>`;
      }
      return para;
    }).join('\n');
    
    // Clean up
    parsed = parsed.replace(/<p class="mb-3"><\/p>/g, '');
    parsed = parsed.replace(/\n/g, ' ');
    
    return parsed;
  };

  return (
    <div className="text-gray-700 dark:text-gray-300">
      <div 
        dangerouslySetInnerHTML={{ __html: parseMarkdown(content) }} 
        className="markdown-content leading-relaxed [&>p]:text-sm [&>ul]:text-sm [&>ol]:text-sm [&_li]:text-sm [&>h1]:text-gray-900 [&>h1]:dark:text-gray-100 [&>h2]:text-gray-900 [&>h2]:dark:text-gray-100 [&>h3]:text-gray-900 [&>h3]:dark:text-gray-100 [&>h4]:text-gray-900 [&>h4]:dark:text-gray-100"
      />
      {streaming && <span className="animate-pulse text-orange-500">▊</span>}
    </div>
  );
});
```

## File: `app/page.tsx`
```tsx
import { Chat } from './chat';
import Image from 'next/image';

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col">
      {/* Header with logo */}
      <header className="px-4 sm:px-6 lg:px-8 py-4">
        <div className="max-w-4xl mx-auto flex items-center justify-between">
          <a
            href="https://firecrawl.dev"
            target="_blank"
            rel="noopener noreferrer"
          >
            <Image
              src="/firecrawl-logo-with-fire.png"
              alt="Firecrawl Logo"
              width={113}
              height={24}
              className="w-[113px] h-auto"
            />
          </a>
          <a
            href="https://github.com/mendableai/firesearch"
            target="_blank"
            rel="noopener noreferrer"
            className="justify-center whitespace-nowrap ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none rounded-[10px] text-sm transition-all duration-200 disabled:cursor-not-allowed disabled:opacity-50 bg-[#36322F] text-[#fff] hover:bg-[#4a4542] disabled:bg-[#8c8885] disabled:hover:bg-[#8c8885] [box-shadow:inset_0px_-2.108433723449707px_0px_0px_#171310,_0px_1.2048193216323853px_6.325301647186279px_0px_rgba(58,_33,_8,_58%)] hover:translate-y-[1px] hover:scale-[0.98] hover:[box-shadow:inset_0px_-1px_0px_0px_#171310,_0px_1px_3px_0px_rgba(58,_33,_8,_40%)] active:translate-y-[2px] active:scale-[0.97] active:[box-shadow:inset_0px_1px_1px_0px_#171310,_0px_1px_2px_0px_rgba(58,_33,_8,_30%)] disabled:shadow-none disabled:hover:translate-y-0 disabled:hover:scale-100 h-10 px-4 py-2 font-medium flex items-center gap-2"
          >
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" className="w-4 h-4">
              <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
            </svg>
            Use this template
          </a>
        </div>
      </header>

      {/* Hero section */}
      <div className="px-4 sm:px-6 lg:px-8 pt-8 pb-6">
        <div className="max-w-4xl mx-auto text-center">
          <h1 className="text-[2.5rem] lg:text-[3.8rem] text-[#36322F] dark:text-white font-semibold tracking-tight leading-[0.9] opacity-0 animate-fade-up [animation-duration:500ms] [animation-delay:200ms] [animation-fill-mode:forwards]">
            <span className="relative px-1 text-transparent bg-clip-text bg-gradient-to-tr from-red-600 to-yellow-500 inline-flex justify-center items-center">
              Firesearch
            </span>
            <span className="block leading-[1.1] opacity-0 animate-fade-up [animation-duration:500ms] [animation-delay:400ms] [animation-fill-mode:forwards]">
              Deep Research
            </span>
          </h1>
          <p className="mt-6 text-lg text-zinc-600 dark:text-zinc-400 opacity-0 animate-fade-up [animation-duration:500ms] [animation-delay:600ms] [animation-fill-mode:forwards]">
            AI-powered search powered by Firecrawl and LangGraph
          </p>
        </div>
      </div>

      {/* Main content wrapper */}
      <div className="flex-1">
        {/* Chat component */}
        <Chat />
      </div>

      {/* Footer */}
      <footer className="px-4 sm:px-6 lg:px-8 py-8 mt-auto">
        <div className="max-w-4xl mx-auto text-center">
          <p className="text-sm text-gray-600 dark:text-gray-400">
            Powered by{' '}
            <a
              href="https://firecrawl.dev"
              target="_blank"
              rel="noopener noreferrer"
              className="text-orange-600 hover:text-orange-700 dark:text-orange-400 dark:hover:text-orange-300 font-medium"
            >
              Firecrawl
            </a>
            {' and '}
            <a
              href="https://www.langchain.com/langgraph"
              target="_blank"
              rel="noopener noreferrer"
              className="text-orange-600 hover:text-orange-700 dark:text-orange-400 dark:hover:text-orange-300 font-medium"
            >
              LangGraph
            </a>
          </p>
        </div>
      </footer>
    </div>
  );
}
```

## File: `app/search-display.tsx`
```tsx
'use client';

import { SearchEvent, SearchStep, SearchPhase } from '@/lib/langgraph-search-engine';
import { useState, useEffect, useRef } from 'react';
import Image from 'next/image';
import { MarkdownRenderer } from './markdown-renderer';
import { getFaviconUrl, getDefaultFavicon, markFaviconFailed } from '@/lib/favicon-utils';

// Component for animated thinking line that cycles through messages
function AnimatedThinkingLine({ messages }: { messages: string[] }) {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isVisible, setIsVisible] = useState(true);
  const [isComplete, setIsComplete] = useState(false);
  
  useEffect(() => {
    if (messages.length <= 1) return;
    
    // Detect if this is a "speed run" (many source names)
    const isSpeedRun = messages.some(msg => msg.includes('Analyzing') && messages.length > 5);
    const cycleDelay = isSpeedRun ? 600 : 2000; // Faster for speed runs
    const fadeDelay = isSpeedRun ? 100 : 300;
    
    const cycleMessages = () => {
      setIsVisible(false);
      setTimeout(() => {
        setCurrentIndex((prev) => {
          const next = prev + 1;
          // Stop at the last message if it's a speed run
          if (isSpeedRun && next >= messages.length - 1) {
            setIsComplete(true);
            return messages.length - 1; // Stay on last message
          }
          return next % messages.length;
        });
        setIsVisible(true);
      }, fadeDelay);
    };
    
    if (!isComplete) {
      const interval = setInterval(cycleMessages, cycleDelay);
      return () => clearInterval(interval);
    }
  }, [messages, isComplete]);
  
  // Extract URL from message if it's an "Analyzing" message
  const currentMessage = messages[currentIndex];
  const analyzingMatch = currentMessage.match(/Analyzing (.+)\.\.\./);
  const currentUrl = analyzingMatch ? analyzingMatch[1] : null;
  
  return (
    <div className="flex items-start gap-3 text-gray-700 dark:text-gray-300">
      <div className="w-5 h-5 mt-0.5 rounded bg-gray-200 dark:bg-gray-700 flex items-center justify-center flex-shrink-0 overflow-hidden">
        {currentUrl ? (
          <Image 
            src={getFaviconUrl(currentUrl)} 
            alt=""
            width={20}
            height={20}
            className={`w-5 h-5 rounded transition-all duration-300 ${isVisible ? 'scale-100 opacity-100' : 'scale-75 opacity-0'}`}
            onError={(e) => {
              const img = e.target as HTMLImageElement;
              img.src = getDefaultFavicon(20);
              markFaviconFailed(currentUrl);
            }}
          />
        ) : (
          <svg className="w-3 h-3 animate-spin" fill="none" viewBox="0 0 24 24">
            <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
            <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
        )}
      </div>
      <span className={`text-sm transition-opacity ${isVisible ? 'opacity-100' : 'opacity-0'}`} style={{ transitionDuration: isVisible ? '150ms' : '150ms' }}>
        {currentMessage}
      </span>
    </div>
  );
}

// Component for found sources group with collapse/expand
function FoundSourcesGroup({ 
  event, 
  sources, 
  defaultExpanded, 
  completedPhases, 
  currentPhase, 
  events 
}: {
  event: SearchEvent;
  sources: {
    url: string;
    title: string;
    stage: 'browsing' | 'extracting' | 'analyzing' | 'complete';
    summary?: string;
  }[];
  defaultExpanded: boolean;
  completedPhases: Set<string>;
  currentPhase: SearchPhase | null;
  events: SearchEvent[];
}) {
  const [isExpanded, setIsExpanded] = useState(defaultExpanded);
  
  // Auto-collapse when a new search starts
  useEffect(() => {
    setIsExpanded(defaultExpanded);
  }, [defaultExpanded]);
  
  return (
    <div className="animate-fade-in">
      <div className="flex items-center justify-between gap-2">
        <div className="flex-1">
          {renderEvent(event, completedPhases, currentPhase, false, events)}
        </div>
        {sources.length > 0 && (
          <button
            onClick={() => setIsExpanded(!isExpanded)}
            className="p-0.5 hover:bg-gray-100 dark:hover:bg-gray-800 rounded transition-colors flex-shrink-0"
            aria-label={isExpanded ? "Collapse sources" : "Expand sources"}
          >
            <svg 
              className={`w-3 h-3 text-gray-400 transition-transform ${isExpanded ? 'rotate-90' : ''}`} 
              fill="none" 
              stroke="currentColor" 
              viewBox="0 0 24 24"
            >
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
            </svg>
          </button>
        )}
      </div>
      <div 
        className={`ml-7 mt-1 overflow-hidden transition-all duration-300 ease-in-out ${
          isExpanded && sources.length > 0 ? 'max-h-96 opacity-100' : 'max-h-0 opacity-0'
        }`}
      >
        <div className="space-y-1">
          {sources.map((source, index) => (
            <div
              key={source.url}
              className="animate-slide-down"
              style={{
                animationDelay: `${index * 50}ms`,
                animationFillMode: 'both'
              }}
            >
              <SourceProcessingLine
                url={source.url}
                stage={source.stage}
                summary={source.summary}
              />
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

// Component for animated source processing line
function SourceProcessingLine({ url, stage, summary }: { 
  url: string; 
  stage: 'browsing' | 'extracting' | 'analyzing' | 'complete';
  summary?: string;
}) {
  // const stages = ['browsing', 'extracting', 'analyzing', 'complete'];
  // const _currentStageIndex = stages.indexOf(stage);
  
  
  const stageLabels = {
    browsing: 'Browsing',
    extracting: 'Extracting',
    analyzing: 'Analyzing',
    complete: 'Complete'
  };
  
  return (
    <div className="group flex items-start gap-2 text-xs py-1 animate-fade-in">
      <Image 
        src={getFaviconUrl(url)} 
        alt=""
        width={16}
        height={16}
        className="w-4 h-4 rounded flex-shrink-0 mt-0.5"
        onError={(e) => {
          const img = e.target as HTMLImageElement;
          img.src = getDefaultFavicon(16);
          markFaviconFailed(url);
        }}
      />
      <div className="flex-1 min-w-0">
        <div className="font-medium text-gray-600 dark:text-gray-400 truncate">
          {new URL(url).hostname}
        </div>
        {stage === 'complete' ? (
          summary ? (
            <div className="text-gray-500 dark:text-gray-500 mt-0.5">
              {summary}
            </div>
          ) : (
            <div className="flex items-center gap-1 mt-0.5">
              <svg className="w-3 h-3 text-green-600 dark:text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
              </svg>
              <span className="text-gray-500 dark:text-gray-500">
                Complete
              </span>
            </div>
          )
        ) : (
          <div className="flex items-center gap-1 mt-0.5">
            <div className="w-1.5 h-1.5 rounded-full bg-orange-500 animate-pulse" />
            <span className="text-gray-500 dark:text-gray-500">
              {stageLabels[stage as keyof typeof stageLabels]}...
            </span>
          </div>
        )}
      </div>
    </div>
  );
}

export function SearchDisplay({ events }: { events: SearchEvent[] }) {
  const [steps, setSteps] = useState<SearchStep[]>([]);
  const [, setStreamedContent] = useState('');
  const [showFinalResult, setShowFinalResult] = useState(false);
  const [startTime, setStartTime] = useState<number | null>(null);
  const [elapsedSeconds, setElapsedSeconds] = useState(0);
  const [completedPhases, setCompletedPhases] = useState<Set<string>>(new Set());
  const [, setSearchQueries] = useState<string[]>([]);
  const [currentPhase, setCurrentPhase] = useState<SearchPhase | null>(null);
  const [scrapedCount, setScrapedCount] = useState(0);
  const [lastEventTime, setLastEventTime] = useState<number>(Date.now());
  const messagesScrollRef = useRef<HTMLDivElement>(null);
  const stepsScrollRef = useRef<HTMLDivElement>(null);
  
  // Track source processing states
  const [sourceStates, setSourceStates] = useState<Map<string, {
    url: string;
    title: string;
    stage: 'browsing' | 'extracting' | 'analyzing' | 'complete';
    summary?: string;
  }>>(new Map());
  
  // Format seconds into mm:ss or just ss
  const formatTime = (seconds: number): string => {
    if (seconds < 60) {
      return `${seconds}s`;
    }
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  };
  
  // Initialize steps and start timer
  useEffect(() => {
    if (steps.length === 0 && events.length > 0) {
      setSteps([
        { id: 'understanding', label: 'Understanding request', status: 'pending' },
        { id: 'planning', label: 'Planning search', status: 'pending' },
        { id: 'searching', label: 'Searching sources', status: 'pending' },
        { id: 'analyzing', label: 'Analyzing content', status: 'pending' },
        { id: 'synthesizing', label: 'Synthesizing answer', status: 'pending' },
        { id: 'complete', label: 'Complete', status: 'pending' }
      ]);
      // Start timer immediately
      setStartTime(Date.now());
    }
  }, [events.length, steps.length]);

  // Update timer every second
  useEffect(() => {
    if (startTime) {
      const interval = setInterval(() => {
        if (!showFinalResult) {
          setElapsedSeconds(Math.floor((Date.now() - startTime) / 1000));
        }
      }, 1000);
      
      return () => clearInterval(interval);
    }
  }, [startTime, showFinalResult]);

  // Update steps based on events - only show current and completed steps
  useEffect(() => {
    // Extract search queries from events
    const searchEvents = events.filter(e => e.type === 'searching');
    const uniqueQueries = [...new Set(searchEvents.map(e => e.type === 'searching' ? e.query : ''))];
    setSearchQueries(uniqueQueries);
    
    const latestPhaseEvent = events.findLast(e => e.type === 'phase-update');
    if (latestPhaseEvent?.type === 'phase-update') {
      setCurrentPhase(latestPhaseEvent.phase);
      
      // Mark previous phases as completed
      const phases: SearchPhase[] = ['understanding', 'planning', 'searching', 'analyzing', 'synthesizing', 'complete'];
      const currentPhaseIndex = phases.indexOf(latestPhaseEvent.phase);
      if (currentPhaseIndex > 0) {
        setCompletedPhases(prev => {
          const newCompleted = new Set(prev);
          for (let i = 0; i < currentPhaseIndex; i++) {
            newCompleted.add(phases[i]);
          }
          return newCompleted;
        });
      }
      
      setSteps(() => {
        const baseSteps = [
          { id: 'understanding', label: 'Understanding request', status: 'pending' },
          { id: 'planning', label: 'Planning search', status: 'pending' },
          { id: 'searching', label: 'Searching sources', status: 'pending' }
        ] as SearchStep[];
        
        // Add dynamic search query steps if we're in or past the searching phase
        if (['searching', 'analyzing', 'synthesizing', 'complete'].includes(latestPhaseEvent.phase) && uniqueQueries.length > 0) {
          uniqueQueries.forEach((query, idx) => {
            const queryLabel = query.length > 25 ? query.substring(0, 25) + '\u2026' : query;
            baseSteps.push({
              id: `search-${idx}`,
              label: queryLabel,
              status: 'pending'
            });
          });
        }
        
        // Add remaining steps
        baseSteps.push(
          { id: 'analyzing', label: 'Analyzing content', status: 'pending' },
          { id: 'synthesizing', label: 'Synthesizing answer', status: 'pending' },
          { id: 'complete', label: 'Complete', status: 'pending' }
        );
        
        // Update status based on current phase
        const phases: SearchPhase[] = ['understanding', 'planning', 'searching', 'analyzing', 'synthesizing', 'complete'];
        const currentPhaseIndex = phases.indexOf(latestPhaseEvent.phase);
        
        baseSteps.forEach((step) => {
          if (step.id.startsWith('search-')) {
            // Check if this specific search is complete by looking for a 'found' event
            const searchIndex = parseInt(step.id.split('-')[1]);
            const searchQuery = uniqueQueries[searchIndex];
            const foundEvent = events.find(e => 
              e.type === 'found' && e.query.toLowerCase().trim() === searchQuery.toLowerCase().trim()
            );
            
            if (foundEvent) {
              step.status = 'completed';
            } else if (currentPhaseIndex >= 2) { // We're in or past searching phase
              step.status = 'active';
            } else {
              step.status = 'pending';
            }
          } else {
            const stepPhaseIndex = phases.indexOf(step.id as SearchPhase);
            if (stepPhaseIndex < currentPhaseIndex) {
              step.status = 'completed';
            } else if (stepPhaseIndex === currentPhaseIndex) {
              step.status = 'active';
            }
          }
        });
        
        return baseSteps;
      });
    }
  }, [events]);

  // Handle streaming content and extract research info
  useEffect(() => {
    const contentChunks = events.filter(e => e.type === 'content-chunk');
    if (contentChunks.length > 0) {
      const content = contentChunks.map(e => e.type === 'content-chunk' ? e.chunk : '').join('');
      setStreamedContent(content);
    }
    
    const finalResult = events.find(e => e.type === 'final-result');
    if (finalResult) {
      setShowFinalResult(true);
    }
    
    // Update last event time
    if (events.length > 0) {
      setLastEventTime(Date.now());
    }
    
    // Count total sources found
    const foundEvents = events.filter(e => e.type === 'found');
    const totalSourcesFound = foundEvents.reduce((acc, event) => {
      return acc + (event.type === 'found' ? event.sources.length : 0);
    }, 0);
    setScrapedCount(totalSourcesFound);
    
    // Update source processing states
    events.forEach(event => {
      if (event.type === 'source-processing') {
        setSourceStates(prev => {
          const newMap = new Map(prev);
          newMap.set(event.url, {
            url: event.url,
            title: event.title,
            stage: event.stage,
            summary: prev.get(event.url)?.summary
          });
          return newMap;
        });
      } else if (event.type === 'source-complete') {
        setSourceStates(prev => {
          const newMap = new Map(prev);
          const existing = prev.get(event.url);
          newMap.set(event.url, {
            url: event.url,
            title: existing?.title || '',
            stage: 'complete',
            summary: event.summary
          });
          return newMap;
        });
      }
    });
  }, [events]);

  // Check if we're stalled (no events for more than 3 seconds)
  const [, setIsStalled] = useState(false);
  useEffect(() => {
    const interval = setInterval(() => {
      const timeSinceLastEvent = Date.now() - lastEventTime;
      setIsStalled(timeSinceLastEvent > 3000 && !showFinalResult && currentPhase === 'searching');
    }, 1000);
    
    return () => clearInterval(interval);
  }, [lastEventTime, showFinalResult, currentPhase]);

  // Auto-scroll messages when new events arrive
  useEffect(() => {
    if (messagesScrollRef.current) {
      messagesScrollRef.current.scrollTop = messagesScrollRef.current.scrollHeight;
    }
  }, [events]);

  // Auto-scroll steps when they update
  useEffect(() => {
    if (stepsScrollRef.current) {
      stepsScrollRef.current.scrollTop = stepsScrollRef.current.scrollHeight;
    }
  }, [steps]);

  const latestResult = events.findLast(e => e.type === 'final-result');
  
  // Show final result if complete - only show the research box, not the content
  if (showFinalResult && latestResult?.type === 'final-result') {
    return (
      <div className="flex h-[500px] border border-gray-200 dark:border-gray-700 rounded-lg overflow-hidden">
        <div className="w-56 border-r border-gray-200 dark:border-gray-700 bg-gray-50 dark:bg-gray-900 flex-shrink-0 flex flex-col">
          {/* Fixed progress header */}
          <div className="p-4 pb-2">
            <div className="border border-gray-200 dark:border-gray-700 rounded-lg p-3 bg-white dark:bg-gray-800">
              <div className="flex items-center justify-between">
                <h4 className="text-[10px] font-semibold text-gray-600 dark:text-gray-400 uppercase tracking-wider">
                  Complete
                </h4>
                <span className="text-xs font-mono text-gray-600 dark:text-gray-400">
                  {formatTime(elapsedSeconds)}
                </span>
              </div>
              <div className="flex items-center justify-between mt-1">
                <span className="text-[10px] text-gray-500 dark:text-gray-500">Sources found</span>
                <span className="text-xs font-mono text-gray-600 dark:text-gray-400">
                  {scrapedCount}
                </span>
              </div>
            </div>
          </div>
          
          {/* Scrollable steps area */}
          <div className="flex-1 overflow-y-auto scrollbar-hide px-4 pb-4">
            <div className="relative border border-gray-200 dark:border-gray-700 rounded-lg p-3 bg-white dark:bg-gray-800">
              <div className="relative pl-6">
                {steps.map((step, index) => (
                  <div key={step.id} className="relative flex items-start gap-2 mb-6">
                    <div className="absolute left-[-24px] flex-shrink-0 mt-0.5">
                      <div className="w-5 h-5 rounded-full bg-orange-500 flex items-center justify-center shadow-sm">
                        <span className="text-white text-xs">✓</span>
                      </div>
                    </div>
                    
                    <div className="flex-1">
                      <p className="text-xs leading-tight text-gray-700 dark:text-gray-300">
                        {step.label}
                      </p>
                    </div>
                    
                    {index < steps.length - 1 && (
                      <div 
                        className="absolute left-[-14px] top-[20px] h-[calc(100%+8px)] w-0.5 bg-orange-500"
                        style={{ opacity: 1 }}
                      />
                    )}
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>

        <div className="flex-1 p-8 overflow-auto scrollbar-hide">
          <div className="max-w-4xl">
            <div className="space-y-3">
              {events.filter(e => e.type !== 'content-chunk' && e.type !== 'final-result').map((event, i) => (
                <div key={i} className="text-sm">
                  {renderEvent(event, completedPhases, currentPhase, false, events)}
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    );
  }

  // Show search progress
  return (
    <div className="flex h-[500px] border border-gray-200 dark:border-gray-700 rounded-lg overflow-hidden">
      {/* Steps sidebar - vertical progress */}
      <div className="w-56 border-r border-gray-200 dark:border-gray-700 bg-gray-50 dark:bg-gray-900 flex-shrink-0 flex flex-col">
        {/* Fixed progress header */}
        <div className="p-4 pb-2">
          <div className="border border-gray-200 dark:border-gray-700 rounded-lg p-3 bg-white dark:bg-gray-800">
            <div className="flex items-center justify-between">
              <h4 className="text-[10px] font-semibold text-gray-600 dark:text-gray-400 uppercase tracking-wider">
                Progress
              </h4>
              <span className="text-xs font-mono text-gray-600 dark:text-gray-400">
                {formatTime(elapsedSeconds)}
              </span>
            </div>
            <div className="flex items-center justify-between mt-1">
              <span className="text-[10px] text-gray-500 dark:text-gray-500">Sources found</span>
              <span className="text-xs font-mono text-gray-600 dark:text-gray-400">
                {scrapedCount}
              </span>
            </div>
          </div>
        </div>
        
        {/* Scrollable steps area */}
        <div className="flex-1 overflow-y-auto scrollbar-hide px-4 pb-4" ref={stepsScrollRef}>
          <div className="relative border border-gray-200 dark:border-gray-700 rounded-lg p-3 bg-white dark:bg-gray-800">
            <div className="relative pl-6">
          {/* Steps */}
          {steps.map((step, index) => (
            <div
              key={step.id}
              className="relative animate-fade-in opacity-0"
              style={{
                animationDelay: `${index * 100}ms`,
                animationFillMode: 'forwards'
              }}
            >
              {/* Step content */}
              <div className="relative flex items-start gap-2 mb-6">
                {/* Checkmark on the left */}
                <div className="absolute left-[-24px] flex-shrink-0 mt-0.5">
                  {step.status === 'completed' ? (
                    <div className="w-5 h-5 rounded-full bg-orange-500 flex items-center justify-center shadow-sm animate-scale-in">
                      <span className="text-white text-xs">✓</span>
                    </div>
                  ) : step.status === 'active' ? (
                    <div className="w-5 h-5 rounded-full bg-orange-400 animate-pulse shadow-sm" />
                  ) : (
                    <div className="w-5 h-5 rounded-full bg-gray-300 dark:bg-gray-600" />
                  )}
                </div>
                
                {/* Label */}
                <div className="flex-1">
                  <p className={`text-xs leading-tight transition-all ${
                    step.status === 'active' 
                      ? 'font-medium text-gray-900 dark:text-gray-100' 
                      : step.status === 'completed'
                      ? 'text-gray-700 dark:text-gray-300'
                      : 'text-gray-500 dark:text-gray-500'
                  }`}>
                    {step.label}
                  </p>
                  {step.status === 'active' && (
                    <p className="text-[10px] text-gray-500 dark:text-gray-400 mt-0.5">
                      Processing...
                    </p>
                  )}
                </div>
              </div>
              
              {/* Connecting line - positioned after content */}
              {index < steps.length - 1 && (
                <div 
                  className={`absolute left-[-14px] top-[20px] h-[calc(100%+8px)] w-0.5 transition-all duration-300 ${
                    index < steps.filter(s => s.status === 'completed').length
                      ? 'bg-orange-500'
                      : 'bg-gray-300 dark:bg-gray-600'
                  }`}
                  style={{ opacity: 1 }}
                />
              )}
            </div>
          ))}
            </div>
          </div>
        </div>
      </div>

      {/* Main content area - takes remaining space */}
      <div className="flex-1 p-8 overflow-y-auto scrollbar-hide" ref={messagesScrollRef}>
        <div className="max-w-4xl">
          <div className="space-y-3">
            {/* Group events with their source processing */}
            {(() => {
              const displayGroups: { event: SearchEvent; sourceProcessing?: unknown[] }[] = [];
              let currentFoundEvent: SearchEvent | null = null;
              let currentSources: unknown[] = [];
              
              events.forEach((event) => {
                if (event.type === 'content-chunk' || event.type === 'final-result') return;
                
                if (event.type === 'found') {
                  // Save any pending sources before starting new group
                  if (currentFoundEvent && currentSources.length > 0) {
                    displayGroups.push({ event: currentFoundEvent, sourceProcessing: [...currentSources] });
                    currentSources = [];
                  }
                  currentFoundEvent = event;
                } else if ((event.type === 'source-processing' || event.type === 'source-complete') && currentFoundEvent) {
                  // Don't accumulate, we'll get the current state from sourceStates map
                } else {
                  // Save any pending found event with its sources
                  if (currentFoundEvent) {
                    displayGroups.push({ event: currentFoundEvent, sourceProcessing: [...currentSources] });
                    currentFoundEvent = null;
                    currentSources = [];
                  }
                  // Add non-found event
                  displayGroups.push({ event });
                }
              });
              
              // Don't forget the last group
              if (currentFoundEvent) {
                displayGroups.push({ event: currentFoundEvent, sourceProcessing: currentSources });
              }
              
              // Track the latest "found" event to know which sources should be expanded
              const latestFoundIndex = displayGroups.findLastIndex(g => g.event.type === 'found');
              
              return displayGroups.map((group, i) => {
                if (group.event.type === 'found') {
                  // Get the URLs from this specific found event
                  const foundUrls = new Set(group.event.sources.map(s => s.url));
                  
                  // Get the current state of sources that match these URLs
                  const sourcesForThisQuery = Array.from(sourceStates.entries())
                    .filter(([url]) => foundUrls.has(url))
                    .map(([, source]) => source);
                  
                  // Only expand sources for the current/latest search
                  const isCurrentSearch = i === latestFoundIndex;
                  
                  return (
                    <FoundSourcesGroup
                      key={i}
                      event={group.event}
                      sources={sourcesForThisQuery}
                      defaultExpanded={isCurrentSearch}
                      completedPhases={completedPhases}
                      currentPhase={currentPhase}
                      events={events}
                    />
                  );
                }
                
                return (
                  <div key={i} className="animate-fade-in">
                    {renderEvent(group.event, completedPhases, currentPhase, false, events)}
                  </div>
                );
              });
            })()}
          </div>
        </div>
      </div>
    </div>
  );
}

function renderEvent(event: SearchEvent, _completedPhases: Set<string>, currentPhase: SearchPhase | null = null, _showLoadingIndicator = false, events: SearchEvent[] = []) { // eslint-disable-line @typescript-eslint/no-unused-vars
  switch (event.type) {
    case 'thinking':
      // Single line animated display
      const messages = event.message.split('|');
      const isAnimated = messages.length > 1;
      
      if (isAnimated) {
        return (
          <AnimatedThinkingLine messages={messages} />
        );
      }
      
      // Check if this is the initial understanding (contains markdown headers)
      const isInitialThinking = event.message.includes('###') || event.message.includes('**');
      
      if (isInitialThinking) {
        return (
          <div className="text-gray-500 dark:text-gray-400 text-sm">
            <MarkdownRenderer content={event.message} />
          </div>
        );
      }
      
      // Check if this is a processing message that should show a spinner
      const isProcessing = event.message.includes('Processing') && event.message.includes('sources');
      const isAnalyzing = event.message.includes('Analyzing content from');
      
      if (isProcessing || isAnalyzing) {
        // Check for single source URL (for individual processing)
        const singleSourceMatch = event.message.match(/\|SOURCE:(.+)$/);
        const singleSourceUrl = singleSourceMatch?.[1];
        const displayMessage = singleSourceUrl ? event.message.replace(/\|SOURCE:.+$/, '') : event.message;
        
        return (
          <div className="flex items-start gap-3 text-gray-700 dark:text-gray-300">
            {singleSourceUrl ? (
              // Show favicon for individual source
              <Image 
                src={getFaviconUrl(singleSourceUrl)} 
                alt=""
                width={20}
                height={20}
                className="w-5 h-5 mt-0.5 rounded flex-shrink-0"
                onError={(e) => {
                  const img = e.target as HTMLImageElement;
                  img.src = getDefaultFavicon(20);
                  markFaviconFailed(singleSourceUrl);
                }}
              />
            ) : (
              // Show spinner for general processing
              <div className="w-5 h-5 mt-0.5 rounded bg-gray-200 dark:bg-gray-700 flex items-center justify-center flex-shrink-0">
                <svg className="w-3 h-3 animate-spin" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
              </div>
            )}
            <span className="text-sm">{displayMessage}</span>
          </div>
        );
      }
      
      return (
        <div className="flex items-start gap-3 text-gray-700 dark:text-gray-300">
          <div className="w-5 h-5 mt-0.5 rounded bg-gray-200 dark:bg-gray-700 flex items-center justify-center flex-shrink-0">
            <svg className="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
            </svg>
          </div>
          <span className="text-sm">{event.message}</span>
        </div>
      );
    
    case 'searching':
      // Check if this search has completed by looking for a matching 'found' event
      const searchingQuery = event.query.toLowerCase().trim();
      const searchCompleted = events.some(e => {
        if (e.type !== 'found') return false;
        const foundQuery = e.query.toLowerCase().trim();
        return foundQuery === searchingQuery;
      });
      
      return (
        <div className="flex items-start gap-3 text-gray-700 dark:text-gray-300">
          <div className="w-5 h-5 mt-0.5 rounded bg-orange-100 dark:bg-orange-900/30 flex items-center justify-center flex-shrink-0">
            {searchCompleted ? (
              <svg className="w-3 h-3 text-orange-600 dark:text-orange-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
              </svg>
            ) : (
              <svg className="w-3 h-3 animate-spin" fill="none" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
            )}
          </div>
          <span className="text-sm">
            Search {event.index} of {event.total}: <span className="font-medium text-gray-900 dark:text-gray-100">&quot;{event.query}&quot;</span>
            {!searchCompleted && <span className="text-xs text-gray-500 dark:text-gray-500 ml-2">Finding sources...</span>}
          </span>
        </div>
      );
    
    case 'found':
      return (
        <div className="text-sm text-gray-700 dark:text-gray-300">
          <div className="flex items-center gap-2">
            <div className="w-5 h-5 rounded bg-green-100 dark:bg-green-900/30 flex items-center justify-center flex-shrink-0">
              <svg className="w-3 h-3 text-green-600 dark:text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
              </svg>
            </div>
            <span>Found <span className="font-bold text-gray-900 dark:text-gray-100">{event.sources.length} sources</span> for &quot;{event.query}&quot;</span>
          </div>
        </div>
      );
    
    case 'scraping':
      return (
        <div className="flex items-start gap-3">
          <Image 
            src={getFaviconUrl(event.url)} 
            alt=""
            width={20}
            height={20}
            className="w-5 h-5 mt-0.5 flex-shrink-0 rounded"
            onError={(e) => {
              const img = e.target as HTMLImageElement;
              img.src = getDefaultFavicon(20);
              markFaviconFailed(event.url);
            }}
          />
          <div className="flex-1">
            <div className="text-sm text-gray-900 dark:text-gray-100">
              Browsing <span className="font-medium text-orange-600 dark:text-orange-400">{new URL(event.url).hostname}</span> for &quot;{event.query}&quot;
            </div>
          </div>
        </div>
      );
    
    case 'phase-update':
      // Check if this phase has been completed (we've moved past it)
      const phases: SearchPhase[] = ['understanding', 'planning', 'searching', 'analyzing', 'synthesizing', 'complete'];
      const eventPhaseIndex = phases.indexOf(event.phase);
      const currentPhaseIndex = currentPhase ? phases.indexOf(currentPhase) : -1;
      const isCompleted = currentPhaseIndex > eventPhaseIndex || event.phase === 'complete';
      
      return (
        <div className="flex items-start gap-3 text-gray-900 dark:text-gray-100 font-medium">
          <div className="w-5 h-5 mt-0.5 rounded bg-gray-100 dark:bg-gray-800 flex items-center justify-center">
            {isCompleted ? (
              <svg className="w-3 h-3 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
              </svg>
            ) : (
              <svg className="w-3 h-3 animate-spin text-gray-600" fill="none" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
            )}
          </div>
          <span className="text-sm">{event.message}</span>
        </div>
      );
    
    case 'error':
      return (
        <div className="flex items-start gap-3 text-red-600 dark:text-red-400">
          <div className="w-5 h-5 mt-0.5 rounded bg-red-100 dark:bg-red-900/30 flex items-center justify-center flex-shrink-0">
            <svg className="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <div className="text-sm">
            <span className="font-medium">Error: </span>
            <span>{event.error}</span>
            {event.errorType && <span className="text-xs ml-2">({event.errorType})</span>}
          </div>
        </div>
      );
    
    case 'source-processing':
    case 'source-complete':
      // This will be handled by the SourceProcessingLine component
      return null;
    
    default:
      return null;
  }
}
```

## File: `app/search.tsx`
```tsx
'use server';

import { createStreamableValue } from 'ai/rsc';
import { FirecrawlClient } from '@/lib/firecrawl';
import { LangGraphSearchEngine as SearchEngine, SearchEvent } from '@/lib/langgraph-search-engine';

export async function search(query: string, context?: { query: string; response: string }[], apiKey?: string) {
  const stream = createStreamableValue<SearchEvent>();
  
  // Create FirecrawlClient with API key if provided
  const firecrawl = new FirecrawlClient(apiKey);
  const searchEngine = new SearchEngine(firecrawl);

  // Run search in background
  (async () => {
    try {
      // Stream events as they happen
      await searchEngine.search(query, (event) => {
        stream.update(event);
      }, context);
      
      stream.done();
    } catch (error) {
      stream.error(error);
    }
  })();

  return { stream: stream.value };
}
```

## File: `app/api/check-env/route.ts`
```typescript
import { NextResponse } from 'next/server';

export async function GET() {
  const environmentStatus = {
    FIRECRAWL_API_KEY: !!process.env.FIRECRAWL_API_KEY,
    OPENAI_API_KEY: !!process.env.OPENAI_API_KEY,
    ANTHROPIC_API_KEY: !!process.env.ANTHROPIC_API_KEY,
  };

  return NextResponse.json({ environmentStatus });
} 
```

## File: `components/ui/button.tsx`
```tsx
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const buttonVariants = cva(
  "inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        destructive:
          "bg-destructive text-destructive-foreground hover:bg-destructive/90",
        outline:
          "border border-input bg-background hover:bg-accent hover:text-accent-foreground",
        secondary:
          "bg-secondary text-secondary-foreground hover:bg-secondary/80",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        link: "text-primary underline-offset-4 hover:underline",
        code: "h-9 px-4 rounded-[10px] text-sm font-medium items-center transition-all duration-200 disabled:cursor-not-allowed disabled:opacity-50 bg-[#36322F] text-[#fff] hover:bg-[#4a4542] disabled:bg-[#8c8885] disabled:hover:bg-[#8c8885] [box-shadow:inset_0px_-2.108433723449707px_0px_0px_#171310,_0px_1.2048193216323853px_6.325301647186279px_0px_rgba(58,_33,_8,_58%)] hover:translate-y-[1px] hover:scale-[0.98] hover:[box-shadow:inset_0px_-1px_0px_0px_#171310,_0px_1px_3px_0px_rgba(58,_33,_8,_40%)] active:translate-y-[2px] active:scale-[0.97] active:[box-shadow:inset_0px_1px_1px_0px_#171310,_0px_1px_2px_0px_rgba(58,_33,_8,_30%)] disabled:shadow-none disabled:hover:translate-y-0 disabled:hover:scale-100",
        orange: "h-9 px-4 rounded-[10px] text-sm font-medium items-center transition-all duration-200 disabled:cursor-not-allowed disabled:opacity-50 bg-orange-500 text-white hover:bg-orange-300 dark:bg-orange-500 dark:hover:bg-orange-300 dark:text-white [box-shadow:inset_0px_-2.108433723449707px_0px_0px_#c2410c,_0px_1.2048193216323853px_6.325301647186279px_0px_rgba(234,_88,_12,_58%)] hover:translate-y-[1px] hover:scale-[0.98] hover:[box-shadow:inset_0px_-1px_0px_0px_#c2410c,_0px_1px_3px_0px_rgba(234,_88,_12,_40%)] active:translate-y-[2px] active:scale-[0.97] active:[box-shadow:inset_0px_1px_1px_0px_#c2410c,_0px_1px_2px_0px_rgba(234,_88,_12,_30%)] disabled:shadow-none disabled:hover:translate-y-0 disabled:hover:scale-100",
      },
      size: {
        default: "h-10 px-4 py-2",
        sm: "h-9 rounded-md px-3",
        lg: "h-11 rounded-md px-8",
        icon: "h-10 w-10",
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

## File: `components/ui/dialog.tsx`
```tsx
"use client"

import * as React from "react"
import * as DialogPrimitive from "@radix-ui/react-dialog"
import { XIcon } from "lucide-react"

import { cn } from "@/lib/utils"

function Dialog({
  ...props
}: React.ComponentProps<typeof DialogPrimitive.Root>) {
  return <DialogPrimitive.Root data-slot="dialog" {...props} />
}

function DialogTrigger({
  ...props
}: React.ComponentProps<typeof DialogPrimitive.Trigger>) {
  return <DialogPrimitive.Trigger data-slot="dialog-trigger" {...props} />
}

function DialogPortal({
  ...props
}: React.ComponentProps<typeof DialogPrimitive.Portal>) {
  return <DialogPrimitive.Portal data-slot="dialog-portal" {...props} />
}

function DialogClose({
  ...props
}: React.ComponentProps<typeof DialogPrimitive.Close>) {
  return <DialogPrimitive.Close data-slot="dialog-close" {...props} />
}

function DialogOverlay({
  className,
  ...props
}: React.ComponentProps<typeof DialogPrimitive.Overlay>) {
  return (
    <DialogPrimitive.Overlay
      data-slot="dialog-overlay"
      className={cn(
        "data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 fixed inset-0 z-50 bg-black/50",
        className
      )}
      {...props}
    />
  )
}

function DialogContent({
  className,
  children,
  ...props
}: React.ComponentProps<typeof DialogPrimitive.Content>) {
  return (
    <DialogPortal data-slot="dialog-portal">
      <DialogOverlay />
      <DialogPrimitive.Content
        data-slot="dialog-content"
        className={cn(
          "bg-background data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 fixed top-[50%] left-[50%] z-50 grid w-full max-w-[calc(100%-2rem)] translate-x-[-50%] translate-y-[-50%] gap-4 rounded-lg border p-6 shadow-lg duration-200 sm:max-w-lg",
          className
        )}
        {...props}
      >
        {children}
        <DialogPrimitive.Close className="ring-offset-background focus:ring-ring data-[state=open]:bg-accent data-[state=open]:text-muted-foreground absolute top-4 right-4 rounded-xs opacity-70 transition-opacity hover:opacity-100 focus:ring-2 focus:ring-offset-2 focus:outline-hidden disabled:pointer-events-none [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4">
          <XIcon />
          <span className="sr-only">Close</span>
        </DialogPrimitive.Close>
      </DialogPrimitive.Content>
    </DialogPortal>
  )
}

function DialogHeader({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="dialog-header"
      className={cn("flex flex-col gap-2 text-center sm:text-left", className)}
      {...props}
    />
  )
}

function DialogFooter({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="dialog-footer"
      className={cn(
        "flex flex-col-reverse gap-2 sm:flex-row sm:justify-end",
        className
      )}
      {...props}
    />
  )
}

function DialogTitle({
  className,
  ...props
}: React.ComponentProps<typeof DialogPrimitive.Title>) {
  return (
    <DialogPrimitive.Title
      data-slot="dialog-title"
      className={cn("text-lg leading-none font-semibold", className)}
      {...props}
    />
  )
}

function DialogDescription({
  className,
  ...props
}: React.ComponentProps<typeof DialogPrimitive.Description>) {
  return (
    <DialogPrimitive.Description
      data-slot="dialog-description"
      className={cn("text-muted-foreground text-sm", className)}
      {...props}
    />
  )
}

export {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogOverlay,
  DialogPortal,
  DialogTitle,
  DialogTrigger,
}
```

## File: `components/ui/input.tsx`
```tsx
import * as React from "react"

import { cn } from "@/lib/utils"

function Input({ className, type, ...props }: React.ComponentProps<"input">) {
  return (
    <input
      type={type}
      data-slot="input"
      className={cn(
        "file:text-foreground placeholder:text-muted-foreground selection:bg-primary selection:text-primary-foreground dark:bg-input/30 border-input flex h-9 w-full min-w-0 rounded-md border bg-transparent px-3 py-1 text-base shadow-xs transition-[color,box-shadow] outline-none file:inline-flex file:h-7 file:border-0 file:bg-transparent file:text-sm file:font-medium disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 md:text-sm",
        "focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px]",
        "aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive",
        className
      )}
      {...props}
    />
  )
}

export { Input }
```

## File: `components/ui/pagination.tsx`
```tsx
import * as React from "react"
import {
  ChevronLeftIcon,
  ChevronRightIcon,
  MoreHorizontalIcon,
} from "lucide-react"

import { cn } from "@/lib/utils"
import { Button, buttonVariants } from "@/components/ui/button"

function Pagination({ className, ...props }: React.ComponentProps<"nav">) {
  return (
    <nav
      role="navigation"
      aria-label="pagination"
      data-slot="pagination"
      className={cn("mx-auto flex w-full justify-center", className)}
      {...props}
    />
  )
}

function PaginationContent({
  className,
  ...props
}: React.ComponentProps<"ul">) {
  return (
    <ul
      data-slot="pagination-content"
      className={cn("flex flex-row items-center gap-1", className)}
      {...props}
    />
  )
}

function PaginationItem({ ...props }: React.ComponentProps<"li">) {
  return <li data-slot="pagination-item" {...props} />
}

type PaginationLinkProps = {
  isActive?: boolean
} & Pick<React.ComponentProps<typeof Button>, "size"> &
  React.ComponentProps<"a">

function PaginationLink({
  className,
  isActive,
  size = "icon",
  ...props
}: PaginationLinkProps) {
  return (
    <a
      aria-current={isActive ? "page" : undefined}
      data-slot="pagination-link"
      data-active={isActive}
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
}

function PaginationPrevious({
  className,
  ...props
}: React.ComponentProps<typeof PaginationLink>) {
  return (
    <PaginationLink
      aria-label="Go to previous page"
      size="default"
      className={cn("gap-1 px-2.5 sm:pl-2.5", className)}
      {...props}
    >
      <ChevronLeftIcon />
      <span className="hidden sm:block">Previous</span>
    </PaginationLink>
  )
}

function PaginationNext({
  className,
  ...props
}: React.ComponentProps<typeof PaginationLink>) {
  return (
    <PaginationLink
      aria-label="Go to next page"
      size="default"
      className={cn("gap-1 px-2.5 sm:pr-2.5", className)}
      {...props}
    >
      <span className="hidden sm:block">Next</span>
      <ChevronRightIcon />
    </PaginationLink>
  )
}

function PaginationEllipsis({
  className,
  ...props
}: React.ComponentProps<"span">) {
  return (
    <span
      aria-hidden
      data-slot="pagination-ellipsis"
      className={cn("flex size-9 items-center justify-center", className)}
      {...props}
    >
      <MoreHorizontalIcon className="size-4" />
      <span className="sr-only">More pages</span>
    </span>
  )
}

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

## File: `components/ui/separator.tsx`
```tsx
"use client"

import * as React from "react"
import * as SeparatorPrimitive from "@radix-ui/react-separator"

import { cn } from "@/lib/utils"

function Separator({
  className,
  orientation = "horizontal",
  decorative = true,
  ...props
}: React.ComponentProps<typeof SeparatorPrimitive.Root>) {
  return (
    <SeparatorPrimitive.Root
      data-slot="separator-root"
      decorative={decorative}
      orientation={orientation}
      className={cn(
        "bg-border shrink-0 data-[orientation=horizontal]:h-px data-[orientation=horizontal]:w-full data-[orientation=vertical]:h-full data-[orientation=vertical]:w-px",
        className
      )}
      {...props}
    />
  )
}

export { Separator }
```

## File: `components/ui/sheet.tsx`
```tsx
"use client"

import * as React from "react"
import * as SheetPrimitive from "@radix-ui/react-dialog"
import { XIcon } from "lucide-react"

import { cn } from "@/lib/utils"

function Sheet({ ...props }: React.ComponentProps<typeof SheetPrimitive.Root>) {
  return <SheetPrimitive.Root data-slot="sheet" {...props} />
}

function SheetTrigger({
  ...props
}: React.ComponentProps<typeof SheetPrimitive.Trigger>) {
  return <SheetPrimitive.Trigger data-slot="sheet-trigger" {...props} />
}

function SheetClose({
  ...props
}: React.ComponentProps<typeof SheetPrimitive.Close>) {
  return <SheetPrimitive.Close data-slot="sheet-close" {...props} />
}

function SheetPortal({
  ...props
}: React.ComponentProps<typeof SheetPrimitive.Portal>) {
  return <SheetPrimitive.Portal data-slot="sheet-portal" {...props} />
}

function SheetOverlay({
  className,
  ...props
}: React.ComponentProps<typeof SheetPrimitive.Overlay>) {
  return (
    <SheetPrimitive.Overlay
      data-slot="sheet-overlay"
      className={cn(
        "data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 fixed inset-0 z-50 bg-black/50",
        className
      )}
      {...props}
    />
  )
}

function SheetContent({
  className,
  children,
  side = "right",
  ...props
}: React.ComponentProps<typeof SheetPrimitive.Content> & {
  side?: "top" | "right" | "bottom" | "left"
}) {
  return (
    <SheetPortal>
      <SheetOverlay />
      <SheetPrimitive.Content
        data-slot="sheet-content"
        className={cn(
          "bg-background data-[state=open]:animate-in data-[state=closed]:animate-out fixed z-50 flex flex-col gap-4 shadow-lg transition ease-in-out data-[state=closed]:duration-300 data-[state=open]:duration-500",
          side === "right" &&
            "data-[state=closed]:slide-out-to-right data-[state=open]:slide-in-from-right inset-y-0 right-0 h-full w-3/4 border-l sm:max-w-sm",
          side === "left" &&
            "data-[state=closed]:slide-out-to-left data-[state=open]:slide-in-from-left inset-y-0 left-0 h-full w-3/4 border-r sm:max-w-sm",
          side === "top" &&
            "data-[state=closed]:slide-out-to-top data-[state=open]:slide-in-from-top inset-x-0 top-0 h-auto border-b",
          side === "bottom" &&
            "data-[state=closed]:slide-out-to-bottom data-[state=open]:slide-in-from-bottom inset-x-0 bottom-0 h-auto border-t",
          className
        )}
        {...props}
      >
        {children}
        <SheetPrimitive.Close className="ring-offset-background focus:ring-ring data-[state=open]:bg-secondary absolute top-4 right-4 rounded-xs opacity-70 transition-opacity hover:opacity-100 focus:ring-2 focus:ring-offset-2 focus:outline-hidden disabled:pointer-events-none">
          <XIcon className="size-4" />
          <span className="sr-only">Close</span>
        </SheetPrimitive.Close>
      </SheetPrimitive.Content>
    </SheetPortal>
  )
}

function SheetHeader({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="sheet-header"
      className={cn("flex flex-col gap-1.5 p-4", className)}
      {...props}
    />
  )
}

function SheetFooter({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="sheet-footer"
      className={cn("mt-auto flex flex-col gap-2 p-4", className)}
      {...props}
    />
  )
}

function SheetTitle({
  className,
  ...props
}: React.ComponentProps<typeof SheetPrimitive.Title>) {
  return (
    <SheetPrimitive.Title
      data-slot="sheet-title"
      className={cn("text-foreground font-semibold", className)}
      {...props}
    />
  )
}

function SheetDescription({
  className,
  ...props
}: React.ComponentProps<typeof SheetPrimitive.Description>) {
  return (
    <SheetPrimitive.Description
      data-slot="sheet-description"
      className={cn("text-muted-foreground text-sm", className)}
      {...props}
    />
  )
}

export {
  Sheet,
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

import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { VariantProps, cva } from "class-variance-authority"
import { PanelLeftIcon } from "lucide-react"

import { useIsMobile } from "@/hooks/use-mobile"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Separator } from "@/components/ui/separator"
import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet"
import { Skeleton } from "@/components/ui/skeleton"
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip"

const SIDEBAR_COOKIE_NAME = "sidebar_state"
const SIDEBAR_COOKIE_MAX_AGE = 60 * 60 * 24 * 7
const SIDEBAR_WIDTH = "16rem"
const SIDEBAR_WIDTH_MOBILE = "18rem"
const SIDEBAR_WIDTH_ICON = "3rem"
const SIDEBAR_KEYBOARD_SHORTCUT = "b"

type SidebarContextProps = {
  state: "expanded" | "collapsed"
  open: boolean
  setOpen: (open: boolean) => void
  openMobile: boolean
  setOpenMobile: (open: boolean) => void
  isMobile: boolean
  toggleSidebar: () => void
}

const SidebarContext = React.createContext<SidebarContextProps | null>(null)

function useSidebar() {
  const context = React.useContext(SidebarContext)
  if (!context) {
    throw new Error("useSidebar must be used within a SidebarProvider.")
  }

  return context
}

function SidebarProvider({
  defaultOpen = true,
  open: openProp,
  onOpenChange: setOpenProp,
  className,
  style,
  children,
  ...props
}: React.ComponentProps<"div"> & {
  defaultOpen?: boolean
  open?: boolean
  onOpenChange?: (open: boolean) => void
}) {
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
      if (
        event.key === SIDEBAR_KEYBOARD_SHORTCUT &&
        (event.metaKey || event.ctrlKey)
      ) {
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

  const contextValue = React.useMemo<SidebarContextProps>(
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
          data-slot="sidebar-wrapper"
          style={
            {
              "--sidebar-width": SIDEBAR_WIDTH,
              "--sidebar-width-icon": SIDEBAR_WIDTH_ICON,
              ...style,
            } as React.CSSProperties
          }
          className={cn(
            "group/sidebar-wrapper has-data-[variant=inset]:bg-sidebar flex min-h-svh w-full",
            className
          )}
          {...props}
        >
          {children}
        </div>
      </TooltipProvider>
    </SidebarContext.Provider>
  )
}

function Sidebar({
  side = "left",
  variant = "sidebar",
  collapsible = "offcanvas",
  className,
  children,
  ...props
}: React.ComponentProps<"div"> & {
  side?: "left" | "right"
  variant?: "sidebar" | "floating" | "inset"
  collapsible?: "offcanvas" | "icon" | "none"
}) {
  const { isMobile, state, openMobile, setOpenMobile } = useSidebar()

  if (collapsible === "none") {
    return (
      <div
        data-slot="sidebar"
        className={cn(
          "bg-sidebar text-sidebar-foreground flex h-full w-(--sidebar-width) flex-col",
          className
        )}
        {...props}
      >
        {children}
      </div>
    )
  }

  if (isMobile) {
    return (
      <Sheet open={openMobile} onOpenChange={setOpenMobile} {...props}>
        <SheetContent
          data-sidebar="sidebar"
          data-slot="sidebar"
          data-mobile="true"
          className="bg-sidebar text-sidebar-foreground w-(--sidebar-width) p-0 [&>button]:hidden"
          style={
            {
              "--sidebar-width": SIDEBAR_WIDTH_MOBILE,
            } as React.CSSProperties
          }
          side={side}
        >
          <SheetHeader className="sr-only">
            <SheetTitle>Sidebar</SheetTitle>
            <SheetDescription>Displays the mobile sidebar.</SheetDescription>
          </SheetHeader>
          <div className="flex h-full w-full flex-col">{children}</div>
        </SheetContent>
      </Sheet>
    )
  }

  return (
    <div
      className="group peer text-sidebar-foreground hidden md:block"
      data-state={state}
      data-collapsible={state === "collapsed" ? collapsible : ""}
      data-variant={variant}
      data-side={side}
      data-slot="sidebar"
    >
      {/* This is what handles the sidebar gap on desktop */}
      <div
        data-slot="sidebar-gap"
        className={cn(
          "relative w-(--sidebar-width) bg-transparent transition-[width] duration-200 ease-linear",
          "group-data-[collapsible=offcanvas]:w-0",
          "group-data-[side=right]:rotate-180",
          variant === "floating" || variant === "inset"
            ? "group-data-[collapsible=icon]:w-[calc(var(--sidebar-width-icon)+(--spacing(4)))]"
            : "group-data-[collapsible=icon]:w-(--sidebar-width-icon)"
        )}
      />
      <div
        data-slot="sidebar-container"
        className={cn(
          "fixed inset-y-0 z-10 hidden h-svh w-(--sidebar-width) transition-[left,right,width] duration-200 ease-linear md:flex",
          side === "left"
            ? "left-0 group-data-[collapsible=offcanvas]:left-[calc(var(--sidebar-width)*-1)]"
            : "right-0 group-data-[collapsible=offcanvas]:right-[calc(var(--sidebar-width)*-1)]",
          // Adjust the padding for floating and inset variants.
          variant === "floating" || variant === "inset"
            ? "p-2 group-data-[collapsible=icon]:w-[calc(var(--sidebar-width-icon)+(--spacing(4))+2px)]"
            : "group-data-[collapsible=icon]:w-(--sidebar-width-icon) group-data-[side=left]:border-r group-data-[side=right]:border-l",
          className
        )}
        {...props}
      >
        <div
          data-sidebar="sidebar"
          data-slot="sidebar-inner"
          className="bg-sidebar group-data-[variant=floating]:border-sidebar-border flex h-full w-full flex-col group-data-[variant=floating]:rounded-lg group-data-[variant=floating]:border group-data-[variant=floating]:shadow-sm"
        >
          {children}
        </div>
      </div>
    </div>
  )
}

function SidebarTrigger({
  className,
  onClick,
  ...props
}: React.ComponentProps<typeof Button>) {
  const { toggleSidebar } = useSidebar()

  return (
    <Button
      data-sidebar="trigger"
      data-slot="sidebar-trigger"
      variant="ghost"
      size="icon"
      className={cn("size-7", className)}
      onClick={(event) => {
        onClick?.(event)
        toggleSidebar()
      }}
      {...props}
    >
      <PanelLeftIcon />
      <span className="sr-only">Toggle Sidebar</span>
    </Button>
  )
}

function SidebarRail({ className, ...props }: React.ComponentProps<"button">) {
  const { toggleSidebar } = useSidebar()

  return (
    <button
      data-sidebar="rail"
      data-slot="sidebar-rail"
      aria-label="Toggle Sidebar"
      tabIndex={-1}
      onClick={toggleSidebar}
      title="Toggle Sidebar"
      className={cn(
        "hover:after:bg-sidebar-border absolute inset-y-0 z-20 hidden w-4 -translate-x-1/2 transition-all ease-linear group-data-[side=left]:-right-4 group-data-[side=right]:left-0 after:absolute after:inset-y-0 after:left-1/2 after:w-[2px] sm:flex",
        "in-data-[side=left]:cursor-w-resize in-data-[side=right]:cursor-e-resize",
        "[[data-side=left][data-state=collapsed]_&]:cursor-e-resize [[data-side=right][data-state=collapsed]_&]:cursor-w-resize",
        "hover:group-data-[collapsible=offcanvas]:bg-sidebar group-data-[collapsible=offcanvas]:translate-x-0 group-data-[collapsible=offcanvas]:after:left-full",
        "[[data-side=left][data-collapsible=offcanvas]_&]:-right-2",
        "[[data-side=right][data-collapsible=offcanvas]_&]:-left-2",
        className
      )}
      {...props}
    />
  )
}

function SidebarInset({ className, ...props }: React.ComponentProps<"main">) {
  return (
    <main
      data-slot="sidebar-inset"
      className={cn(
        "bg-background relative flex w-full flex-1 flex-col",
        "md:peer-data-[variant=inset]:m-2 md:peer-data-[variant=inset]:ml-0 md:peer-data-[variant=inset]:rounded-xl md:peer-data-[variant=inset]:shadow-sm md:peer-data-[variant=inset]:peer-data-[state=collapsed]:ml-2",
        className
      )}
      {...props}
    />
  )
}

function SidebarInput({
  className,
  ...props
}: React.ComponentProps<typeof Input>) {
  return (
    <Input
      data-slot="sidebar-input"
      data-sidebar="input"
      className={cn("bg-background h-8 w-full shadow-none", className)}
      {...props}
    />
  )
}

function SidebarHeader({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="sidebar-header"
      data-sidebar="header"
      className={cn("flex flex-col gap-2 p-2", className)}
      {...props}
    />
  )
}

function SidebarFooter({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="sidebar-footer"
      data-sidebar="footer"
      className={cn("flex flex-col gap-2 p-2", className)}
      {...props}
    />
  )
}

function SidebarSeparator({
  className,
  ...props
}: React.ComponentProps<typeof Separator>) {
  return (
    <Separator
      data-slot="sidebar-separator"
      data-sidebar="separator"
      className={cn("bg-sidebar-border mx-2 w-auto", className)}
      {...props}
    />
  )
}

function SidebarContent({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="sidebar-content"
      data-sidebar="content"
      className={cn(
        "flex min-h-0 flex-1 flex-col gap-2 overflow-auto group-data-[collapsible=icon]:overflow-hidden",
        className
      )}
      {...props}
    />
  )
}

function SidebarGroup({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="sidebar-group"
      data-sidebar="group"
      className={cn("relative flex w-full min-w-0 flex-col p-2", className)}
      {...props}
    />
  )
}

function SidebarGroupLabel({
  className,
  asChild = false,
  ...props
}: React.ComponentProps<"div"> & { asChild?: boolean }) {
  const Comp = asChild ? Slot : "div"

  return (
    <Comp
      data-slot="sidebar-group-label"
      data-sidebar="group-label"
      className={cn(
        "text-sidebar-foreground/70 ring-sidebar-ring flex h-8 shrink-0 items-center rounded-md px-2 text-xs font-medium outline-hidden transition-[margin,opacity] duration-200 ease-linear focus-visible:ring-2 [&>svg]:size-4 [&>svg]:shrink-0",
        "group-data-[collapsible=icon]:-mt-8 group-data-[collapsible=icon]:opacity-0",
        className
      )}
      {...props}
    />
  )
}

function SidebarGroupAction({
  className,
  asChild = false,
  ...props
}: React.ComponentProps<"button"> & { asChild?: boolean }) {
  const Comp = asChild ? Slot : "button"

  return (
    <Comp
      data-slot="sidebar-group-action"
      data-sidebar="group-action"
      className={cn(
        "text-sidebar-foreground ring-sidebar-ring hover:bg-sidebar-accent hover:text-sidebar-accent-foreground absolute top-3.5 right-3 flex aspect-square w-5 items-center justify-center rounded-md p-0 outline-hidden transition-transform focus-visible:ring-2 [&>svg]:size-4 [&>svg]:shrink-0",
        // Increases the hit area of the button on mobile.
        "after:absolute after:-inset-2 md:after:hidden",
        "group-data-[collapsible=icon]:hidden",
        className
      )}
      {...props}
    />
  )
}

function SidebarGroupContent({
  className,
  ...props
}: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="sidebar-group-content"
      data-sidebar="group-content"
      className={cn("w-full text-sm", className)}
      {...props}
    />
  )
}

function SidebarMenu({ className, ...props }: React.ComponentProps<"ul">) {
  return (
    <ul
      data-slot="sidebar-menu"
      data-sidebar="menu"
      className={cn("flex w-full min-w-0 flex-col gap-1", className)}
      {...props}
    />
  )
}

function SidebarMenuItem({ className, ...props }: React.ComponentProps<"li">) {
  return (
    <li
      data-slot="sidebar-menu-item"
      data-sidebar="menu-item"
      className={cn("group/menu-item relative", className)}
      {...props}
    />
  )
}

const sidebarMenuButtonVariants = cva(
  "peer/menu-button flex w-full items-center gap-2 overflow-hidden rounded-md p-2 text-left text-sm outline-hidden ring-sidebar-ring transition-[width,height,padding] hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 active:bg-sidebar-accent active:text-sidebar-accent-foreground disabled:pointer-events-none disabled:opacity-50 group-has-data-[sidebar=menu-action]/menu-item:pr-8 aria-disabled:pointer-events-none aria-disabled:opacity-50 data-[active=true]:bg-sidebar-accent data-[active=true]:font-medium data-[active=true]:text-sidebar-accent-foreground data-[state=open]:hover:bg-sidebar-accent data-[state=open]:hover:text-sidebar-accent-foreground group-data-[collapsible=icon]:size-8! group-data-[collapsible=icon]:p-2! [&>span:last-child]:truncate [&>svg]:size-4 [&>svg]:shrink-0",
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
        lg: "h-12 text-sm group-data-[collapsible=icon]:p-0!",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

function SidebarMenuButton({
  asChild = false,
  isActive = false,
  variant = "default",
  size = "default",
  tooltip,
  className,
  ...props
}: React.ComponentProps<"button"> & {
  asChild?: boolean
  isActive?: boolean
  tooltip?: string | React.ComponentProps<typeof TooltipContent>
} & VariantProps<typeof sidebarMenuButtonVariants>) {
  const Comp = asChild ? Slot : "button"
  const { isMobile, state } = useSidebar()

  const button = (
    <Comp
      data-slot="sidebar-menu-button"
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
      <TooltipContent
        side="right"
        align="center"
        hidden={state !== "collapsed" || isMobile}
        {...tooltip}
      />
    </Tooltip>
  )
}

function SidebarMenuAction({
  className,
  asChild = false,
  showOnHover = false,
  ...props
}: React.ComponentProps<"button"> & {
  asChild?: boolean
  showOnHover?: boolean
}) {
  const Comp = asChild ? Slot : "button"

  return (
    <Comp
      data-slot="sidebar-menu-action"
      data-sidebar="menu-action"
      className={cn(
        "text-sidebar-foreground ring-sidebar-ring hover:bg-sidebar-accent hover:text-sidebar-accent-foreground peer-hover/menu-button:text-sidebar-accent-foreground absolute top-1.5 right-1 flex aspect-square w-5 items-center justify-center rounded-md p-0 outline-hidden transition-transform focus-visible:ring-2 [&>svg]:size-4 [&>svg]:shrink-0",
        // Increases the hit area of the button on mobile.
        "after:absolute after:-inset-2 md:after:hidden",
        "peer-data-[size=sm]/menu-button:top-1",
        "peer-data-[size=default]/menu-button:top-1.5",
        "peer-data-[size=lg]/menu-button:top-2.5",
        "group-data-[collapsible=icon]:hidden",
        showOnHover &&
          "peer-data-[active=true]/menu-button:text-sidebar-accent-foreground group-focus-within/menu-item:opacity-100 group-hover/menu-item:opacity-100 data-[state=open]:opacity-100 md:opacity-0",
        className
      )}
      {...props}
    />
  )
}

function SidebarMenuBadge({
  className,
  ...props
}: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="sidebar-menu-badge"
      data-sidebar="menu-badge"
      className={cn(
        "text-sidebar-foreground pointer-events-none absolute right-1 flex h-5 min-w-5 items-center justify-center rounded-md px-1 text-xs font-medium tabular-nums select-none",
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
}

function SidebarMenuSkeleton({
  className,
  showIcon = false,
  ...props
}: React.ComponentProps<"div"> & {
  showIcon?: boolean
}) {
  // Random width between 50 to 90%.
  const width = React.useMemo(() => {
    return `${Math.floor(Math.random() * 40) + 50}%`
  }, [])

  return (
    <div
      data-slot="sidebar-menu-skeleton"
      data-sidebar="menu-skeleton"
      className={cn("flex h-8 items-center gap-2 rounded-md px-2", className)}
      {...props}
    >
      {showIcon && (
        <Skeleton
          className="size-4 rounded-md"
          data-sidebar="menu-skeleton-icon"
        />
      )}
      <Skeleton
        className="h-4 max-w-(--skeleton-width) flex-1"
        data-sidebar="menu-skeleton-text"
        style={
          {
            "--skeleton-width": width,
          } as React.CSSProperties
        }
      />
    </div>
  )
}

function SidebarMenuSub({ className, ...props }: React.ComponentProps<"ul">) {
  return (
    <ul
      data-slot="sidebar-menu-sub"
      data-sidebar="menu-sub"
      className={cn(
        "border-sidebar-border mx-3.5 flex min-w-0 translate-x-px flex-col gap-1 border-l px-2.5 py-0.5",
        "group-data-[collapsible=icon]:hidden",
        className
      )}
      {...props}
    />
  )
}

function SidebarMenuSubItem({
  className,
  ...props
}: React.ComponentProps<"li">) {
  return (
    <li
      data-slot="sidebar-menu-sub-item"
      data-sidebar="menu-sub-item"
      className={cn("group/menu-sub-item relative", className)}
      {...props}
    />
  )
}

function SidebarMenuSubButton({
  asChild = false,
  size = "md",
  isActive = false,
  className,
  ...props
}: React.ComponentProps<"a"> & {
  asChild?: boolean
  size?: "sm" | "md"
  isActive?: boolean
}) {
  const Comp = asChild ? Slot : "a"

  return (
    <Comp
      data-slot="sidebar-menu-sub-button"
      data-sidebar="menu-sub-button"
      data-size={size}
      data-active={isActive}
      className={cn(
        "text-sidebar-foreground ring-sidebar-ring hover:bg-sidebar-accent hover:text-sidebar-accent-foreground active:bg-sidebar-accent active:text-sidebar-accent-foreground [&>svg]:text-sidebar-accent-foreground flex h-7 min-w-0 -translate-x-px items-center gap-2 overflow-hidden rounded-md px-2 outline-hidden focus-visible:ring-2 disabled:pointer-events-none disabled:opacity-50 aria-disabled:pointer-events-none aria-disabled:opacity-50 [&>span:last-child]:truncate [&>svg]:size-4 [&>svg]:shrink-0",
        "data-[active=true]:bg-sidebar-accent data-[active=true]:text-sidebar-accent-foreground",
        size === "sm" && "text-xs",
        size === "md" && "text-sm",
        "group-data-[collapsible=icon]:hidden",
        className
      )}
      {...props}
    />
  )
}

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

function Skeleton({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="skeleton"
      className={cn("bg-accent animate-pulse rounded-md", className)}
      {...props}
    />
  )
}

export { Skeleton }
```

## File: `components/ui/tooltip.tsx`
```tsx
"use client"

import * as React from "react"
import * as TooltipPrimitive from "@radix-ui/react-tooltip"

import { cn } from "@/lib/utils"

function TooltipProvider({
  delayDuration = 0,
  ...props
}: React.ComponentProps<typeof TooltipPrimitive.Provider>) {
  return (
    <TooltipPrimitive.Provider
      data-slot="tooltip-provider"
      delayDuration={delayDuration}
      {...props}
    />
  )
}

function Tooltip({
  ...props
}: React.ComponentProps<typeof TooltipPrimitive.Root>) {
  return (
    <TooltipProvider>
      <TooltipPrimitive.Root data-slot="tooltip" {...props} />
    </TooltipProvider>
  )
}

function TooltipTrigger({
  ...props
}: React.ComponentProps<typeof TooltipPrimitive.Trigger>) {
  return <TooltipPrimitive.Trigger data-slot="tooltip-trigger" {...props} />
}

function TooltipContent({
  className,
  sideOffset = 0,
  children,
  ...props
}: React.ComponentProps<typeof TooltipPrimitive.Content>) {
  return (
    <TooltipPrimitive.Portal>
      <TooltipPrimitive.Content
        data-slot="tooltip-content"
        sideOffset={sideOffset}
        className={cn(
          "bg-primary text-primary-foreground animate-in fade-in-0 zoom-in-95 data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=closed]:zoom-out-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 z-50 w-fit origin-(--radix-tooltip-content-transform-origin) rounded-md px-3 py-1.5 text-xs text-balance",
          className
        )}
        {...props}
      >
        {children}
        <TooltipPrimitive.Arrow className="bg-primary fill-primary z-50 size-2.5 translate-y-[calc(-50%_-_2px)] rotate-45 rounded-[2px]" />
      </TooltipPrimitive.Content>
    </TooltipPrimitive.Portal>
  )
}

export { Tooltip, TooltipTrigger, TooltipContent, TooltipProvider }
```

## File: `hooks/use-mobile.ts`
```typescript
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

## File: `lib/config.ts`
```typescript
// Search Engine Configuration
export const SEARCH_CONFIG = {
  // Search Settings
  MAX_SEARCH_QUERIES: 4,        // Maximum number of search queries to generate
  MAX_SOURCES_PER_SEARCH: 6,     // Maximum sources to return per search query
  MAX_SOURCES_TO_SCRAPE: 6,      // Maximum sources to scrape for additional content
  
  // Content Processing
  MIN_CONTENT_LENGTH: 100,       // Minimum content length to consider valid
  SUMMARY_CHAR_LIMIT: 100,       // Character limit for source summaries
  CONTEXT_PREVIEW_LENGTH: 500,   // Preview length for previous context
  ANSWER_CHECK_PREVIEW: 2500,    // Content preview length for answer checking
  MAX_SOURCES_TO_CHECK: 10,      // Maximum sources to check for answers
  
  // Retry Logic
  MAX_RETRIES: 2,                // Maximum retry attempts for failed operations
  MAX_SEARCH_ATTEMPTS: 3,        // Maximum attempts to find answers via search
  MIN_ANSWER_CONFIDENCE: 0.3,    // Minimum confidence (0-1) that a question was answered
  EARLY_TERMINATION_CONFIDENCE: 0.8, // Confidence level to skip additional searches
  
  // Timeouts
  SCRAPE_TIMEOUT: 15000,         // Timeout for scraping operations (ms)
  
  // Performance
  SOURCE_ANIMATION_DELAY: 50,    // Delay between source animations (ms) - reduced from 150
  PARALLEL_SUMMARY_GENERATION: true, // Generate summaries in parallel
} as const;

// You can also export individual configs for different components
export const UI_CONFIG = {
  ANIMATION_DURATION: 300,       // Default animation duration (ms)
  SOURCE_FADE_DELAY: 50,         // Delay between source animations (ms)
  MESSAGE_CYCLE_DELAY: 2000,     // Delay for cycling through messages (ms)
} as const;

// Model Configuration
export const MODEL_CONFIG = {
  FAST_MODEL: "gpt-4o-mini",     // Fast model for quick operations
  QUALITY_MODEL: "gpt-4o",       // High-quality model for final synthesis
  TEMPERATURE: 0,                // Model temperature (0 = deterministic)
} as const;
```

## File: `lib/context-processor.ts`
```typescript
import { Source } from './langgraph-search-engine';
import { generateText } from 'ai';
import { openai } from '@ai-sdk/openai';

interface ProcessedSource extends Source {
  relevanceScore: number;
  extractedSections: string[];
  keywords: string[];
  summarized?: boolean;
}

export class ContextProcessor {
  // Configuration
  private readonly MAX_TOTAL_CHARS = 100000;
  private readonly MIN_CHARS_PER_SOURCE = 2000;
  private readonly MAX_CHARS_PER_SOURCE = 15000;
  private readonly CONTEXT_WINDOW_SIZE = 500; // chars before/after keyword match

  /**
   * Process sources for optimal context selection
   */
  async processSources(
    query: string,
    sources: Source[],
    searchQueries: string[],
    onProgress?: (message: string, sourceUrl?: string) => void
  ): Promise<ProcessedSource[]> {
    // Determine summary length based on number of sources
    const summaryLength = this.calculateSummaryLength(sources.length);
    
    // Process sources with GPT-4o-mini summarization
    const processedSources = await Promise.all(
      sources.map(source => this.summarizeSource(source, query, searchQueries, summaryLength, onProgress))
    );

    // Filter out failed sources and sort by relevance
    const validSources = processedSources
      .filter(s => s.relevanceScore > 0)
      .sort((a, b) => b.relevanceScore - a.relevanceScore);

    return validSources;
  }

  /**
   * Extract keywords from query and search queries
   */
  private extractKeywords(query: string, searchQueries: string[]): string[] {
    const allText = [query, ...searchQueries].join(' ').toLowerCase();
    
    // Remove common words
    const stopWords = new Set(['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'been', 'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'must', 'can', 'what', 'when', 'where', 'how', 'why', 'who']);
    
    // Extract words, filter stopwords, and get unique keywords
    const words = allText
      .split(/\W+/)
      .filter(word => word.length > 2 && !stopWords.has(word));
    
    // Also extract quoted phrases
    const quotedPhrases = allText.match(/"([^"]+)"/g)?.map(p => p.replace(/"/g, '')) || [];
    
    return [...new Set([...words, ...quotedPhrases])];
  }

  /**
   * Process a single source to extract relevant sections and calculate relevance
   */
  private async processSource(
    source: Source,
    keywords: string[]
  ): Promise<ProcessedSource> {
    if (!source.content) {
      return {
        ...source,
        relevanceScore: 0,
        extractedSections: [],
        keywords: []
      };
    }

    const content = source.content.toLowerCase();
    const foundKeywords: string[] = [];
    const keywordPositions: { keyword: string; position: number }[] = [];

    // Find all keyword occurrences
    for (const keyword of keywords) {
      let position = content.indexOf(keyword);
      while (position !== -1) {
        keywordPositions.push({ keyword, position });
        if (!foundKeywords.includes(keyword)) {
          foundKeywords.push(keyword);
        }
        position = content.indexOf(keyword, position + 1);
      }
    }

    // Calculate relevance score
    const relevanceScore = this.calculateRelevanceScore(
      foundKeywords.length,
      keywordPositions.length,
      keywords.length,
      source.content.length
    );

    // Extract relevant sections around keywords
    const extractedSections = this.extractRelevantSections(
      source.content,
      keywordPositions
    );

    return {
      ...source,
      relevanceScore,
      extractedSections,
      keywords: foundKeywords
    };
  }

  /**
   * Calculate relevance score based on keyword matches
   */
  private calculateRelevanceScore(
    uniqueKeywordsFound: number,
    totalKeywordMatches: number,
    totalKeywords: number,
    contentLength: number
  ): number {
    // Coverage: what percentage of query keywords were found
    const coverage = totalKeywords > 0 ? uniqueKeywordsFound / totalKeywords : 0;
    
    // Density: keyword matches per 1000 characters
    const density = (totalKeywordMatches / contentLength) * 1000;
    
    // Normalize density (cap at 10 matches per 1000 chars)
    const normalizedDensity = Math.min(density / 10, 1);
    
    // Combined score (coverage is more important)
    return (coverage * 0.7) + (normalizedDensity * 0.3);
  }

  /**
   * Extract relevant sections around keyword matches
   */
  private extractRelevantSections(
    content: string,
    keywordPositions: { keyword: string; position: number }[]
  ): string[] {
    if (keywordPositions.length === 0) {
      // No keywords found, return beginning of content
      return [content.slice(0, this.MIN_CHARS_PER_SOURCE)];
    }

    // Sort positions
    keywordPositions.sort((a, b) => a.position - b.position);

    // Merge overlapping windows
    const windows: { start: number; end: number }[] = [];
    
    for (const { position } of keywordPositions) {
      const start = Math.max(0, position - this.CONTEXT_WINDOW_SIZE);
      const end = Math.min(content.length, position + this.CONTEXT_WINDOW_SIZE);
      
      // Check if this window overlaps with the last one
      if (windows.length > 0 && start <= windows[windows.length - 1].end) {
        // Extend the last window
        windows[windows.length - 1].end = end;
      } else {
        // Add new window
        windows.push({ start, end });
      }
    }

    // Extract sections, ensuring we capture sentence boundaries
    const sections: string[] = [];
    
    for (const window of windows) {
      // Extend to sentence boundaries
      let start = window.start;
      let end = window.end;
      
      // Find previous sentence boundary
      const prevPeriod = content.lastIndexOf('.', start);
      const prevNewline = content.lastIndexOf('\n', start);
      start = Math.max(prevPeriod + 1, prevNewline + 1, 0);
      
      // Find next sentence boundary
      const nextPeriod = content.indexOf('.', end);
      const nextNewline = content.indexOf('\n', end);
      if (nextPeriod !== -1 || nextNewline !== -1) {
        end = Math.min(
          nextPeriod !== -1 ? nextPeriod + 1 : content.length,
          nextNewline !== -1 ? nextNewline : content.length
        );
      }
      
      const section = content.slice(start, end).trim();
      if (section) {
        sections.push(section);
      }
    }

    return sections;
  }

  /**
   * Distribute character budget among sources based on relevance
   */
  private distributeCharacterBudget(
    sources: ProcessedSource[]
  ): ProcessedSource[] {
    // Filter out sources with no relevance
    const relevantSources = sources.filter(s => s.relevanceScore > 0);
    
    if (relevantSources.length === 0) {
      // Fallback: use first few sources
      return sources.slice(0, 5).map(s => ({
        ...s,
        content: s.content?.slice(0, this.MAX_CHARS_PER_SOURCE) || ''
      }));
    }

    // Calculate total relevance
    const totalRelevance = relevantSources.reduce((sum, s) => sum + s.relevanceScore, 0);
    
    // Distribute budget proportionally
    let remainingBudget = this.MAX_TOTAL_CHARS;
    const processedResults: ProcessedSource[] = [];
    
    for (const source of relevantSources) {
      if (remainingBudget <= 0) break;
      
      // Calculate this source's share
      const relevanceRatio = source.relevanceScore / totalRelevance;
      const allocatedChars = Math.floor(relevanceRatio * this.MAX_TOTAL_CHARS);
      
      // Apply min/max constraints
      const targetChars = Math.max(
        this.MIN_CHARS_PER_SOURCE,
        Math.min(allocatedChars, this.MAX_CHARS_PER_SOURCE, remainingBudget)
      );
      
      // Use extracted sections if available, otherwise use full content
      let processedContent: string;
      
      if (source.extractedSections.length > 0) {
        // Combine extracted sections
        processedContent = source.extractedSections.join('\n\n[...]\n\n');
        
        // If still too short, add more content around sections
        if (processedContent.length < targetChars && source.content) {
          const additionalContent = source.content.slice(0, targetChars - processedContent.length);
          processedContent = additionalContent + '\n\n[...]\n\n' + processedContent;
        }
      } else {
        // Use beginning of content
        processedContent = source.content?.slice(0, targetChars) || '';
      }
      
      // Ensure we don't exceed target
      if (processedContent.length > targetChars) {
        processedContent = processedContent.slice(0, targetChars) + '\n[... content truncated]';
      }
      
      remainingBudget -= processedContent.length;
      
      processedResults.push({
        ...source,
        content: processedContent
      });
    }
    
    return processedResults;
  }

  /**
   * Calculate optimal summary length based on source count
   */
  private calculateSummaryLength(sourceCount: number): number {
    if (sourceCount <= 5) return 4000;
    if (sourceCount <= 10) return 3000;
    if (sourceCount <= 20) return 2000;
    if (sourceCount <= 30) return 1500;
    return 1000;
  }

  /**
   * Summarize a single source using GPT-4o-mini
   */
  private async summarizeSource(
    source: Source,
    query: string,
    searchQueries: string[],
    targetLength: number,
    _onProgress?: (message: string, sourceUrl?: string) => void // eslint-disable-line @typescript-eslint/no-unused-vars
  ): Promise<ProcessedSource> {
    // If no content, return empty source
    if (!source.content || source.content.length < 100) {
      return {
        ...source,
        relevanceScore: 0,
        extractedSections: [],
        keywords: [],
        summarized: false
      };
    }

    try {
      // No longer emit individual progress events
      
      // Create a focused prompt for relevance-based summarization
      
      const result = await generateText({
        model: openai('gpt-4o-mini'),
        prompt: `You are a research assistant helping to extract the most relevant information from a webpage.

User's question: "${query}"
Related search queries: ${searchQueries.join(', ')}

Source title: ${source.title}
Source URL: ${source.url}

Content to analyze:
${source.content.slice(0, 15000)} ${source.content.length > 15000 ? '\n[... content truncated]' : ''}

Instructions:
1. Extract ONLY the information that directly relates to the user's question and search queries
2. Focus on specific facts, data, quotes, and concrete details
3. Preserve important numbers, dates, names, and technical details
4. Maintain the original meaning and context
5. If the content has little relevance to the query, just note that briefly
6. Target length: approximately ${targetLength} characters

Provide a focused summary that would help answer the user's question:`,
        temperature: 0.3,
        maxTokens: Math.ceil(targetLength / 3), // Rough token estimation
      });

      const summary = result.text.trim();
      
      // Calculate a simple relevance score based on the summary
      const relevanceScore = this.calculateRelevanceFromSummary(summary, query, searchQueries);

      return {
        ...source,
        content: summary,
        relevanceScore,
        extractedSections: [summary],
        keywords: this.extractKeywords(query, searchQueries),
        summarized: true
      };
    } catch (error) {
      console.warn(`Failed to summarize source ${source.url}:`, error);
      
      // Fallback to keyword extraction method
      const keywords = this.extractKeywords(query, searchQueries);
      const processed = await this.processSource(source, keywords);
      
      // Use distributed budget for fallback
      const fallbackSources = await this.distributeCharacterBudget([processed]);
      return fallbackSources[0] || processed;
    }
  }

  /**
   * Calculate relevance score from summary
   */
  private calculateRelevanceFromSummary(
    summary: string,
    query: string,
    searchQueries: string[]
  ): number {
    // Simple heuristic: longer summaries with more specific content are more relevant
    const summaryLength = summary.length;
    
    // Check if summary indicates low relevance
    const lowRelevancePhrases = [
      'not directly related',
      'no specific information',
      'doesn\'t mention',
      'no relevant content',
      'unrelated to'
    ];
    
    const summaryLower = summary.toLowerCase();
    const hasLowRelevance = lowRelevancePhrases.some(phrase => 
      summaryLower.includes(phrase)
    );
    
    if (hasLowRelevance) {
      return 0.1; // Very low relevance
    }
    
    // Check for high relevance indicators
    const highRelevanceIndicators = [
      'specifically mentions',
      'directly addresses',
      'provides detailed',
      'explains how',
      'data shows',
      'research indicates'
    ];
    
    const hasHighRelevance = highRelevanceIndicators.some(phrase => 
      summaryLower.includes(phrase)
    );
    
    // Calculate score
    let score = Math.min(summaryLength / 2000, 1.0); // Base score from length
    
    if (hasHighRelevance) {
      score = Math.min(score + 0.3, 1.0);
    }
    
    // Check keyword density in summary
    const keywords = this.extractKeywords(query, searchQueries);
    const keywordMatches = keywords.filter(keyword => 
      summaryLower.includes(keyword.toLowerCase())
    ).length;
    
    const keywordScore = keywords.length > 0 
      ? keywordMatches / keywords.length 
      : 0.5;
    
    // Combined score
    return (score * 0.6) + (keywordScore * 0.4);
  }
}
```

## File: `lib/error-handler.ts`
```typescript
import { v4 as uuidv4 } from 'uuid';
import { NextResponse } from 'next/server';

// Define error types for consistent user-facing messages
export enum ErrorType {
  VALIDATION = 'VALIDATION',
  AUTHENTICATION = 'AUTHENTICATION',
  AUTHORIZATION = 'AUTHORIZATION',
  RATE_LIMIT = 'RATE_LIMIT',
  NOT_FOUND = 'NOT_FOUND',
  API_ERROR = 'API_ERROR',
  SERVER_ERROR = 'SERVER_ERROR'
}

// Map error types to appropriate HTTP status codes
const errorStatusCodes: Record<ErrorType, number> = {
  [ErrorType.VALIDATION]: 400,
  [ErrorType.AUTHENTICATION]: 401,
  [ErrorType.AUTHORIZATION]: 403,
  [ErrorType.RATE_LIMIT]: 429,
  [ErrorType.NOT_FOUND]: 404,
  [ErrorType.API_ERROR]: 502,
  [ErrorType.SERVER_ERROR]: 500
};

// Map error types to user-friendly messages
const errorMessages: Record<ErrorType, string> = {
  [ErrorType.VALIDATION]: 'Invalid request data. Please check your input and try again.',
  [ErrorType.AUTHENTICATION]: 'Authentication required. Please provide valid credentials.',
  [ErrorType.AUTHORIZATION]: 'You do not have permission to perform this action.',
  [ErrorType.RATE_LIMIT]: 'Rate limit exceeded. Please try again later.',
  [ErrorType.NOT_FOUND]: 'The requested resource was not found.',
  [ErrorType.API_ERROR]: 'Error communicating with external service. Please try again later.',
  [ErrorType.SERVER_ERROR]: 'An unexpected error occurred. Please try again later.'
};

// Helper function to handle errors in a consistent way
export function handleError(
  error: unknown, 
  errorType: ErrorType = ErrorType.SERVER_ERROR, 
  context: string = 'API',
  additionalInfo: Record<string, unknown> = {}
) {
  // Generate a correlation ID for tracing
  const correlationId = uuidv4();
  
  // Get error message if available
  const errorMessage = error instanceof Error ? error.message : String(error);
  
  // Build the log object with all relevant information
  const logData = {
    timestamp: new Date().toISOString(),
    correlationId,
    context,
    errorType,
    errorMessage,
    stack: error instanceof Error ? error.stack : undefined,
    ...additionalInfo
  };
  
  // Log the full error details for debugging
  if (process.env.NODE_ENV === 'production') {
    // In production, use structured logging
    console.error(JSON.stringify(logData));
  } else {
    // In development, make it more readable
    console.error(`[${logData.context}] Error (${correlationId}):`, error);
    console.error('Additional info:', additionalInfo);
  }
  
  // Return a sanitized error response for the client
  return {
    status: errorStatusCodes[errorType],
    body: {
      error: {
        message: errorMessages[errorType],
        correlationId,
        type: errorType
      }
    }
  };
}

// Helper function specifically for Next.js API routes returning NextResponse
export function handleNextError(
  error: unknown, 
  errorType: ErrorType = ErrorType.SERVER_ERROR, 
  context: string = 'API',
  additionalInfo: Record<string, unknown> = {}
) {
  const { status, body } = handleError(error, errorType, context, additionalInfo);
  return NextResponse.json(body, { status });
}

// Helper function specifically for Edge Runtime API routes
export function handleEdgeError(
  error: unknown, 
  errorType: ErrorType = ErrorType.SERVER_ERROR, 
  context: string = 'API',
  additionalInfo: Record<string, unknown> = {}
) {
  const { status, body } = handleError(error, errorType, context, additionalInfo);
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      'Content-Type': 'application/json'
    }
  });
} 
```

## File: `lib/favicon-utils.ts`
```typescript
// Favicon utilities with error tracking to prevent repeated failures
const failedDomains = new Set<string>();

export function getFaviconUrl(url: string): string {
  try {
    const domain = new URL(url).hostname;
    
    // If we've already seen this domain fail, return fallback immediately
    if (failedDomains.has(domain)) {
      return getDefaultFavicon();
    }
    
    return `https://www.google.com/s2/favicons?domain=${domain}&sz=32`;
  } catch {
    return getDefaultFavicon();
  }
}

export function getDefaultFavicon(size: number = 20): string {
  return `data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" fill="none"%3E%3Crect width="${size}" height="${size}" rx="${size < 20 ? 2 : 4}" fill="%23E5E7EB"/%3E%3C/svg%3E`;
}

export function markFaviconFailed(url: string): void {
  try {
    const domain = new URL(url).hostname;
    failedDomains.add(domain);
  } catch {
    // Invalid URL, ignore
  }
}
```

## File: `lib/firecrawl.ts`
```typescript
/* eslint-disable @typescript-eslint/no-explicit-any */
import FirecrawlApp from '@mendable/firecrawl-js';

export class FirecrawlClient {
  private client: FirecrawlApp;

  constructor(providedApiKey?: string) {
    const apiKey = providedApiKey || process.env.FIRECRAWL_API_KEY;
    if (!apiKey) {
      throw new Error('FIRECRAWL_API_KEY is required - either provide it or set it as an environment variable');
    }
    this.client = new FirecrawlApp({ apiKey });
  }

  async scrapeUrl(url: string, timeoutMs: number = 15000) {
    try {
      // Create a timeout promise
      const timeoutPromise = new Promise((_, reject) => {
        setTimeout(() => reject(new Error('Scraping timeout')), timeoutMs);
      });
      
      // Race the scraping against the timeout
      const scrapePromise = this.client.scrapeUrl(url, {
        formats: ['markdown', 'html'],
      });
      
      const result = await Promise.race([scrapePromise, timeoutPromise]) as any;
      
      if ('success' in result && !result.success) {
        throw new Error(result.error || 'Scrape failed');
      }
      
      return {
        markdown: (result as any).markdown || '',
        html: (result as any).html || '',
        metadata: (result as any).metadata || {},
        success: true,
      };
    } catch (error: any) {
      
      // Handle timeout errors
      if (error?.message === 'Scraping timeout') {
        return {
          markdown: '',
          html: '',
          metadata: {
            error: 'Scraping took too long and was stopped',
            timeout: true,
          },
          success: false,
          error: 'timeout',
        };
      }
      
      // Handle 403 errors gracefully
      if (error?.statusCode === 403 || error?.message?.includes('403')) {
        return {
          markdown: '',
          html: '',
          metadata: {
            error: 'This website is not supported by Firecrawl',
            statusCode: 403,
          },
          success: false,
          error: 'unsupported',
        };
      }
      
      // Return error info for other failures
      return {
        markdown: '',
        html: '',
        metadata: {
          error: error?.message || 'Failed to scrape URL',
          statusCode: error?.statusCode,
        },
        success: false,
        error: 'failed',
      };
    }
  }

  async mapUrl(url: string, options?: { search?: string; limit?: number }) {
    try {
      const result = await this.client.mapUrl(url, {
        search: options?.search,
        limit: options?.limit || 10,
      });
      
      if ('success' in result && !result.success) {
        throw new Error((result as any).error || 'Map failed');
      }
      
      return {
        links: (result as any).links || [],
        metadata: (result as any).metadata || {},
      };
    } catch (error) {
      throw error;
    }
  }

  async search(query: string, options?: { limit?: number; scrapeOptions?: any }) {
    try {
      // Search with scrape - this gets us content immediately!
      const searchParams: any = {
        limit: options?.limit || 10,
      };
      
      // Add scrapeOptions to get content with search results
      if (options?.scrapeOptions !== false) {
        searchParams.scrapeOptions = {
          formats: ['markdown'],
          ...options?.scrapeOptions
        };
      }
      
      
      const result = await this.client.search(query, searchParams);
      
      
      // Handle the actual Firecrawl v1 API response format
      if (result && typeof result === 'object' && 'success' in result) {
        if (!(result as any).success) {
          throw new Error((result as any).error || 'Search failed');
        }
      }
      
      // Extract data - search with scrape returns data with content
      const data = (result as any)?.data || [];
      
      // Transform to include scraped content
      const enrichedData = data.map((item: any) => {
        // Try to extract favicon from metadata or construct default
        let favicon = item.metadata?.favicon || null;
        if (!favicon && item.metadata?.ogImage) {
          favicon = item.metadata.ogImage;
        } else if (!favicon && item.url) {
          // Default favicon URL
          const domain = new URL(item.url).hostname;
          favicon = `https://${domain}/favicon.ico`;
        }
        
        return {
          url: item.url,
          title: item.title || item.metadata?.title || 'Untitled',
          description: item.description || item.metadata?.description || '',
          markdown: item.markdown || '',
          html: item.html || '',
          links: item.links || [],
          screenshot: item.screenshot || null,
          metadata: {
            ...item.metadata,
            favicon: favicon,
            screenshot: item.screenshot
          },
          scraped: true, // Mark as already scraped
          content: item.markdown || '', // For compatibility
          favicon: favicon // Add at top level for easy access
        };
      });
      
      return {
        data: enrichedData,
        results: enrichedData, // For backward compatibility
        metadata: (result as any)?.metadata || {},
      };
    } catch (error) {
      throw error;
    }
  }
}
```

## File: `lib/langgraph-search-engine.ts`
```typescript
import { StateGraph, END, START, Annotation, MemorySaver } from "@langchain/langgraph";
import { ChatOpenAI } from "@langchain/openai";
import { HumanMessage, SystemMessage } from "@langchain/core/messages";
import { FirecrawlClient } from './firecrawl';
import { ContextProcessor } from './context-processor';
import { SEARCH_CONFIG, MODEL_CONFIG } from './config';

// Event types remain the same for frontend compatibility
export type SearchPhase = 
  | 'understanding'
  | 'planning' 
  | 'searching'
  | 'analyzing'
  | 'synthesizing'
  | 'complete'
  | 'error';

export type SearchEvent = 
  | { type: 'phase-update'; phase: SearchPhase; message: string }
  | { type: 'thinking'; message: string }
  | { type: 'searching'; query: string; index: number; total: number }
  | { type: 'found'; sources: Source[]; query: string }
  | { type: 'scraping'; url: string; index: number; total: number; query: string }
  | { type: 'content-chunk'; chunk: string }
  | { type: 'final-result'; content: string; sources: Source[]; followUpQuestions?: string[] }
  | { type: 'error'; error: string; errorType?: ErrorType }
  | { type: 'source-processing'; url: string; title: string; stage: 'browsing' | 'extracting' | 'analyzing' }
  | { type: 'source-complete'; url: string; summary: string };

export type ErrorType = 'search' | 'scrape' | 'llm' | 'unknown';

export interface Source {
  url: string;
  title: string;
  content?: string;
  quality?: number;
  summary?: string;
}

export interface SearchResult {
  url: string;
  title: string;
  content?: string;
  markdown?: string;
}

export interface SearchStep {
  id: SearchPhase | string;
  label: string;
  status: 'pending' | 'active' | 'completed';
  startTime?: number;
}

// Proper LangGraph state using Annotation with reducers
const SearchStateAnnotation = Annotation.Root({
  // Input fields
  query: Annotation<string>({
    reducer: (_, y) => y ?? "",
    default: () => ""
  }),
  context: Annotation<{ query: string; response: string }[] | undefined>({
    reducer: (_, y) => y,
    default: () => undefined
  }),
  
  // Process fields
  understanding: Annotation<string | undefined>({
    reducer: (x, y) => y ?? x,
    default: () => undefined
  }),
  searchQueries: Annotation<string[] | undefined>({
    reducer: (x, y) => y ?? x,
    default: () => undefined
  }),
  currentSearchIndex: Annotation<number>({
    reducer: (x, y) => y ?? x,
    default: () => 0
  }),
  
  // Results fields - with proper array reducers
  sources: Annotation<Source[]>({
    reducer: (existing: Source[], update: Source[] | undefined) => {
      if (!update) return existing;
      // Deduplicate sources by URL
      const sourceMap = new Map<string, Source>();
      [...existing, ...update].forEach(source => {
        sourceMap.set(source.url, source);
      });
      return Array.from(sourceMap.values());
    },
    default: () => []
  }),
  scrapedSources: Annotation<Source[]>({
    reducer: (existing: Source[], update: Source[] | undefined) => {
      if (!update) return existing;
      return [...existing, ...update];
    },
    default: () => []
  }),
  processedSources: Annotation<Source[] | undefined>({
    reducer: (x, y) => y ?? x,
    default: () => undefined
  }),
  finalAnswer: Annotation<string | undefined>({
    reducer: (x, y) => y ?? x,
    default: () => undefined
  }),
  followUpQuestions: Annotation<string[] | undefined>({
    reducer: (x, y) => y ?? x,
    default: () => undefined
  }),
  
  // Answer tracking
  subQueries: Annotation<Array<{
    question: string;
    searchQuery: string;
    answered: boolean;
    answer?: string;
    confidence: number;
    sources: string[];
  }> | undefined>({
    reducer: (x, y) => y ?? x,
    default: () => undefined
  }),
  searchAttempt: Annotation<number>({
    reducer: (x, y) => y ?? x,
    default: () => 0
  }),
  
  // Control fields
  phase: Annotation<SearchPhase>({
    reducer: (x, y) => y ?? x,
    default: () => 'understanding' as SearchPhase
  }),
  error: Annotation<string | undefined>({
    reducer: (x, y) => y ?? x,
    default: () => undefined
  }),
  errorType: Annotation<ErrorType | undefined>({
    reducer: (x, y) => y ?? x,
    default: () => undefined
  }),
  maxRetries: Annotation<number>({
    reducer: (x, y) => y ?? x,
    default: () => SEARCH_CONFIG.MAX_RETRIES
  }),
  retryCount: Annotation<number>({
    reducer: (x, y) => y ?? x,
    default: () => 0
  })
});

type SearchState = typeof SearchStateAnnotation.State;

// Define config type for proper event handling
interface GraphConfig {
  configurable?: {
    eventCallback?: (event: SearchEvent) => void;
    checkpointId?: string;
  };
}

export class LangGraphSearchEngine {
  private firecrawl: FirecrawlClient;
  private contextProcessor: ContextProcessor;
  private graph: ReturnType<typeof this.buildGraph>;
  private llm: ChatOpenAI;
  private streamingLlm: ChatOpenAI;
  private checkpointer?: MemorySaver;

  constructor(firecrawl: FirecrawlClient, options?: { enableCheckpointing?: boolean }) {
    this.firecrawl = firecrawl;
    this.contextProcessor = new ContextProcessor();
    
    const apiKey = process.env.OPENAI_API_KEY;
    if (!apiKey) {
      throw new Error('OPENAI_API_KEY environment variable is not set');
    }
    
    // Initialize LangChain models
    this.llm = new ChatOpenAI({
      modelName: MODEL_CONFIG.FAST_MODEL,
      temperature: MODEL_CONFIG.TEMPERATURE,
      openAIApiKey: apiKey,
    });
    
    this.streamingLlm = new ChatOpenAI({
      modelName: MODEL_CONFIG.QUALITY_MODEL,
      temperature: MODEL_CONFIG.TEMPERATURE,
      streaming: true,
      openAIApiKey: apiKey,
    });

    // Enable checkpointing if requested
    if (options?.enableCheckpointing) {
      this.checkpointer = new MemorySaver();
    }
    
    this.graph = this.buildGraph();
  }

  getInitialSteps(): SearchStep[] {
    return [
      { id: 'understanding', label: 'Understanding request', status: 'pending' },
      { id: 'planning', label: 'Planning search', status: 'pending' },
      { id: 'searching', label: 'Searching sources', status: 'pending' },
      { id: 'analyzing', label: 'Analyzing content', status: 'pending' },
      { id: 'synthesizing', label: 'Synthesizing answer', status: 'pending' },
      { id: 'complete', label: 'Complete', status: 'pending' }
    ];
  }

  private buildGraph() {
    // Create closures for helper methods
    const analyzeQuery = this.analyzeQuery.bind(this);
    const scoreContent = this.scoreContent.bind(this);
    const summarizeContent = this.summarizeContent.bind(this);
    const generateStreamingAnswer = this.generateStreamingAnswer.bind(this);
    const generateFollowUpQuestions = this.generateFollowUpQuestions.bind(this);
    const firecrawl = this.firecrawl;
    const contextProcessor = this.contextProcessor;
    
    const workflow = new StateGraph(SearchStateAnnotation)
      // Understanding node
      .addNode("understand", async (state: SearchState, config?: GraphConfig): Promise<Partial<SearchState>> => {
        const eventCallback = config?.configurable?.eventCallback;
        
        if (eventCallback) {
          eventCallback({
            type: 'phase-update',
            phase: 'understanding',
            message: 'Analyzing your request...'
          });
        }
        
        try {
          const understanding = await analyzeQuery(state.query, state.context);
          
          if (eventCallback) {
            eventCallback({
              type: 'thinking',
              message: understanding
            });
          }
          
          return {
            understanding,
            phase: 'planning' as SearchPhase
          };
        } catch (error) {
          return {
            error: error instanceof Error ? error.message : 'Failed to understand query',
            errorType: 'llm' as ErrorType,
            phase: 'error' as SearchPhase
          };
        }
      })
      
      // Planning node
      .addNode("plan", async (state: SearchState, config?: GraphConfig): Promise<Partial<SearchState>> => {
        const eventCallback = config?.configurable?.eventCallback;
        
        if (eventCallback) {
          eventCallback({
            type: 'phase-update',
            phase: 'planning',
            message: 'Planning search strategy...'
          });
        }
        
        try {
          // Extract sub-queries if not already done
          let subQueries = state.subQueries;
          if (!subQueries) {
            const extractSubQueries = this.extractSubQueries.bind(this);
            const extracted = await extractSubQueries(state.query);
            subQueries = extracted.map(sq => ({
              question: sq.question,
              searchQuery: sq.searchQuery,
              answered: false,
              confidence: 0,
              sources: []
            }));
          }
          
          // Generate search queries for unanswered questions
          const unansweredQueries = subQueries.filter(sq => !sq.answered || sq.confidence < SEARCH_CONFIG.MIN_ANSWER_CONFIDENCE);
          
          if (unansweredQueries.length === 0) {
            // All questions answered, skip to analysis
            return {
              subQueries,
              phase: 'analyzing' as SearchPhase
            };
          }
          
          // Use alternative search queries if this is a retry
          let searchQueries: string[];
          if (state.searchAttempt > 0) {
            const generateAlternativeSearchQueries = this.generateAlternativeSearchQueries.bind(this);
            searchQueries = await generateAlternativeSearchQueries(subQueries, state.searchAttempt);
            
            // Update sub-queries with new search queries
            let alternativeIndex = 0;
            subQueries.forEach(sq => {
              if (!sq.answered || sq.confidence < SEARCH_CONFIG.MIN_ANSWER_CONFIDENCE) {
                if (alternativeIndex < searchQueries.length) {
                  sq.searchQuery = searchQueries[alternativeIndex];
                  alternativeIndex++;
                }
              }
            });
          } else {
            // First attempt - use the search queries from sub-queries
            searchQueries = unansweredQueries.map(sq => sq.searchQuery);
          }
          
          if (eventCallback) {
            if (state.searchAttempt === 0) {
              eventCallback({
                type: 'thinking',
                message: searchQueries.length > 3 
                  ? `I detected ${subQueries.length} different questions. I'll search for each one separately.`
                  : `I'll search for information to answer your question.`
              });
            } else {
              eventCallback({
                type: 'thinking',
                message: `Trying alternative search strategies for: ${unansweredQueries.map(sq => sq.question).join(', ')}`
              });
            }
          }
          
          return {
            searchQueries,
            subQueries,
            currentSearchIndex: 0,
            phase: 'searching' as SearchPhase
          };
        } catch (error) {
          return {
            error: error instanceof Error ? error.message : 'Failed to plan search',
            errorType: 'llm' as ErrorType,
            phase: 'error' as SearchPhase
          };
        }
      })
      
      // Search node (handles one search at a time)
      .addNode("search", async (state: SearchState, config?: GraphConfig): Promise<Partial<SearchState>> => {
        const eventCallback = config?.configurable?.eventCallback;
        const searchQueries = state.searchQueries || [];
        const currentIndex = state.currentSearchIndex || 0;
        
        if (currentIndex === 0 && eventCallback) {
          eventCallback({
            type: 'phase-update',
            phase: 'searching',
            message: 'Searching the web...'
          });
        }
        
        if (currentIndex >= searchQueries.length) {
          return {
            phase: 'scrape' as SearchPhase
          };
        }
        
        const searchQuery = searchQueries[currentIndex];
        
        if (eventCallback) {
          eventCallback({
            type: 'searching',
            query: searchQuery,
            index: currentIndex + 1,
            total: searchQueries.length
          });
        }
        
        try {
          const results = await firecrawl.search(searchQuery, {
            limit: SEARCH_CONFIG.MAX_SOURCES_PER_SEARCH,
            scrapeOptions: {
              formats: ['markdown']
            }
          });
          
          const newSources: Source[] = results.data.map((r: SearchResult) => ({
            url: r.url,
            title: r.title,
            content: r.markdown || r.content || '',
            quality: 0
          }));
          
          if (eventCallback) {
            eventCallback({
              type: 'found',
              sources: newSources,
              query: searchQuery
            });
          }
          
          // Process sources in parallel for better performance
          if (SEARCH_CONFIG.PARALLEL_SUMMARY_GENERATION) {
            await Promise.all(newSources.map(async (source) => {
              if (eventCallback) {
                eventCallback({
                  type: 'source-processing',
                  url: source.url,
                  title: source.title,
                  stage: 'browsing'
                });
              }
              
              // Score the content
              source.quality = scoreContent(source.content || '', state.query);
              
              // Generate summary if content is available
              if (source.content && source.content.length > SEARCH_CONFIG.MIN_CONTENT_LENGTH) {
                const summary = await summarizeContent(source.content, searchQuery);
                
                // Store the summary in the source object
                if (summary && !summary.toLowerCase().includes('no specific')) {
                  source.summary = summary;
                  
                  if (eventCallback) {
                    eventCallback({
                      type: 'source-complete',
                      url: source.url,
                      summary: summary
                    });
                  }
                }
              }
            }));
          } else {
            // Original sequential processing
            for (const source of newSources) {
              if (eventCallback) {
                eventCallback({
                  type: 'source-processing',
                  url: source.url,
                  title: source.title,
                  stage: 'browsing'
                });
              }
              
              // Small delay for animation
              await new Promise(resolve => setTimeout(resolve, SEARCH_CONFIG.SOURCE_ANIMATION_DELAY));
              
              // Score the content
              source.quality = scoreContent(source.content || '', state.query);
              
              // Generate summary if content is available
              if (source.content && source.content.length > SEARCH_CONFIG.MIN_CONTENT_LENGTH) {
                const summary = await summarizeContent(source.content, searchQuery);
                
                // Store the summary in the source object
                if (summary && !summary.toLowerCase().includes('no specific')) {
                  source.summary = summary;
                  
                  if (eventCallback) {
                    eventCallback({
                      type: 'source-complete',
                      url: source.url,
                      summary: summary
                    });
                  }
                }
              }
            }
          }
          
          return {
            sources: newSources,
            currentSearchIndex: currentIndex + 1
          };
        } catch {
          return {
            currentSearchIndex: currentIndex + 1,
            errorType: 'search' as ErrorType
          };
        }
      })
      
      // Scraping node
      .addNode("scrape", async (state: SearchState, config?: GraphConfig): Promise<Partial<SearchState>> => {
        const eventCallback = config?.configurable?.eventCallback;
        const sourcesToScrape = state.sources?.filter(s => 
          !s.content || s.content.length < SEARCH_CONFIG.MIN_CONTENT_LENGTH
        ) || [];
        const newScrapedSources: Source[] = [];
        
        // Sources with content were already processed in search node, just pass them through
        const sourcesWithContent = state.sources?.filter(s => 
          s.content && s.content.length >= SEARCH_CONFIG.MIN_CONTENT_LENGTH
        ) || [];
        newScrapedSources.push(...sourcesWithContent);
        
        // Then scrape sources without content
        for (let i = 0; i < Math.min(sourcesToScrape.length, SEARCH_CONFIG.MAX_SOURCES_TO_SCRAPE); i++) {
          const source = sourcesToScrape[i];
          
          if (eventCallback) {
            eventCallback({
              type: 'scraping',
              url: source.url,
              index: newScrapedSources.length + 1,
              total: sourcesWithContent.length + Math.min(sourcesToScrape.length, SEARCH_CONFIG.MAX_SOURCES_TO_SCRAPE),
              query: state.query
            });
          }
          
          try {
            const scraped = await firecrawl.scrapeUrl(source.url, SEARCH_CONFIG.SCRAPE_TIMEOUT);
            if (scraped.success && scraped.markdown) {
              const enrichedSource = {
                ...source,
                content: scraped.markdown,
                quality: scoreContent(scraped.markdown, state.query)
              };
              newScrapedSources.push(enrichedSource);
              
              // Show processing animation
              if (eventCallback) {
                eventCallback({
                  type: 'source-processing',
                  url: source.url,
                  title: source.title,
                  stage: 'browsing'
                });
              }
              
              await new Promise(resolve => setTimeout(resolve, 150));
              
              const summary = await summarizeContent(scraped.markdown, state.query);
              if (summary) {
                enrichedSource.summary = summary;
                
                if (eventCallback) {
                  eventCallback({
                    type: 'source-complete',
                    url: source.url,
                    summary: summary
                  });
                }
              }
            } else if (scraped.error === 'timeout') {
              if (eventCallback) {
                eventCallback({
                  type: 'thinking',
                  message: `${new URL(source.url).hostname} is taking too long to respond, moving on...`
                });
              }
            }
          } catch {
            if (eventCallback) {
              eventCallback({
                type: 'thinking',
                message: `Couldn't access ${new URL(source.url).hostname}, trying other sources...`
              });
            }
          }
        }
        
        return {
          scrapedSources: newScrapedSources,
          phase: 'analyzing' as SearchPhase
        };
      })
      
      // Analyzing node
      .addNode("analyze", async (state: SearchState, config?: GraphConfig): Promise<Partial<SearchState>> => {
        const eventCallback = config?.configurable?.eventCallback;
        
        if (eventCallback) {
          eventCallback({
            type: 'phase-update',
            phase: 'analyzing',
            message: 'Analyzing gathered information...'
          });
        }
        
        // Combine sources and remove duplicates by URL
        const sourceMap = new Map<string, Source>();
        
        // Add all sources (not just those with long content, since summaries contain key info)
        (state.sources || []).forEach(s => sourceMap.set(s.url, s));
        
        // Add scraped sources (may override with better content)
        (state.scrapedSources || []).forEach(s => sourceMap.set(s.url, s));
        
        const allSources = Array.from(sourceMap.values());
        
        // Check which questions have been answered
        if (state.subQueries) {
          const checkAnswersInSources = this.checkAnswersInSources.bind(this);
          const updatedSubQueries = await checkAnswersInSources(state.subQueries, allSources);
          
          const answeredCount = updatedSubQueries.filter(sq => sq.answered).length;
          const totalQuestions = updatedSubQueries.length;
          const searchAttempt = (state.searchAttempt || 0) + 1;
          
          // Check if we have partial answers with decent confidence
          const partialAnswers = updatedSubQueries.filter(sq => sq.confidence >= 0.3);
          const hasPartialInfo = partialAnswers.length > answeredCount;
          
          if (eventCallback) {
            if (answeredCount === totalQuestions) {
              eventCallback({
                type: 'thinking',
                message: `Found answers to all ${totalQuestions} questions across ${allSources.length} sources`
              });
            } else if (answeredCount > 0) {
              eventCallback({
                type: 'thinking',
                message: `Found answers to ${answeredCount} of ${totalQuestions} questions. Still missing: ${updatedSubQueries.filter(sq => !sq.answered).map(sq => sq.question).join(', ')}`
              });
            } else if (searchAttempt >= SEARCH_CONFIG.MAX_SEARCH_ATTEMPTS) {
              // Only show "could not find" message when we've exhausted all attempts
              eventCallback({
                type: 'thinking',
                message: `Could not find specific answers in ${allSources.length} sources. The information may not be publicly available.`
              });
            } else if (hasPartialInfo && searchAttempt >= 3) {
              // If we have partial info and tried 3+ times, stop searching
              eventCallback({
                type: 'thinking',
                message: `Found partial information. Moving forward with what's available.`
              });
            } else {
              // For intermediate attempts, show a different message
              eventCallback({
                type: 'thinking',
                message: `Searching for more specific information...`
              });
            }
          }
          
          // If we haven't found all answers and haven't exceeded attempts, try again
          // BUT stop if we have partial info and already tried 2+ times
          if (answeredCount < totalQuestions && 
              searchAttempt < SEARCH_CONFIG.MAX_SEARCH_ATTEMPTS &&
              !(hasPartialInfo && searchAttempt >= 2)) {
            return {
              sources: allSources,
              subQueries: updatedSubQueries,
              searchAttempt,
              phase: 'planning' as SearchPhase  // Go back to planning for retry
            };
          }
          
          // Otherwise proceed with what we have
          try {
            const processedSources = await contextProcessor.processSources(
              state.query,
              allSources,
              state.searchQueries || []
            );
            
            return {
              sources: allSources,
              processedSources,
              subQueries: updatedSubQueries,
              searchAttempt,
              phase: 'synthesizing' as SearchPhase
            };
          } catch {
            return {
              sources: allSources,
              processedSources: allSources,
              subQueries: updatedSubQueries,
              searchAttempt,
              phase: 'synthesizing' as SearchPhase
            };
          }
        } else {
          // Fallback for queries without sub-queries
          if (eventCallback && allSources.length > 0) {
            eventCallback({
              type: 'thinking',
              message: `Found ${allSources.length} sources with quality information`
            });
          }
          
          try {
            const processedSources = await contextProcessor.processSources(
              state.query,
              allSources,
              state.searchQueries || []
            );
            
            return {
              sources: allSources,
              processedSources,
              phase: 'synthesizing' as SearchPhase
            };
          } catch {
            return {
              sources: allSources,
              processedSources: allSources,
              phase: 'synthesizing' as SearchPhase
            };
          }
        }
      })
      
      // Synthesizing node with streaming
      .addNode("synthesize", async (state: SearchState, config?: GraphConfig): Promise<Partial<SearchState>> => {
        const eventCallback = config?.configurable?.eventCallback;
        
        if (eventCallback) {
          eventCallback({
            type: 'phase-update',
            phase: 'synthesizing',
            message: 'Creating comprehensive answer...'
          });
        }
        
        try {
          const sourcesToUse = state.processedSources || state.sources || [];
          
          const answer = await generateStreamingAnswer(
            state.query,
            sourcesToUse,
            (chunk) => {
              if (eventCallback) {
                eventCallback({ type: 'content-chunk', chunk });
              }
            },
            state.context
          );
          
          // Generate follow-up questions
          const followUpQuestions = await generateFollowUpQuestions(
            state.query,
            answer,
            sourcesToUse,
            state.context
          );
          
          return {
            finalAnswer: answer,
            followUpQuestions,
            phase: 'complete' as SearchPhase
          };
        } catch (error) {
          return {
            error: error instanceof Error ? error.message : 'Failed to generate answer',
            errorType: 'llm' as ErrorType,
            phase: 'error' as SearchPhase
          };
        }
      })
      
      // Error handling node
      .addNode("handleError", async (state: SearchState, config?: GraphConfig): Promise<Partial<SearchState>> => {
        const eventCallback = config?.configurable?.eventCallback;
        
        if (eventCallback) {
          eventCallback({
            type: 'error',
            error: state.error || 'An unknown error occurred',
            errorType: state.errorType
          });
        }
        
        // Retry logic based on error type
        if ((state.retryCount || 0) < (state.maxRetries || SEARCH_CONFIG.MAX_RETRIES)) {
              
          // Different retry strategies based on error type
          const retryPhase = state.errorType === 'search' ? 'searching' : 'understanding';
          
          return {
            retryCount: (state.retryCount || 0) + 1,
            phase: retryPhase as SearchPhase,
            error: undefined,
            errorType: undefined
          };
        }
        
        return {
          phase: 'error' as SearchPhase
        };
      })
      
      // Complete node
      .addNode("complete", async (state: SearchState, config?: GraphConfig): Promise<Partial<SearchState>> => {
        const eventCallback = config?.configurable?.eventCallback;
        
        if (eventCallback) {
          eventCallback({
            type: 'phase-update',
            phase: 'complete',
            message: 'Search complete!'
          });
          
          eventCallback({
            type: 'final-result',
            content: state.finalAnswer || '',
            sources: state.sources || [],
            followUpQuestions: state.followUpQuestions
          });
        }
        
        return {
          phase: 'complete' as SearchPhase
        };
      });

    // Add edges with proper conditional routing
    workflow
      .addEdge(START, "understand")
      .addConditionalEdges(
        "understand",
        (state: SearchState) => state.phase === 'error' ? "handleError" : "plan",
        {
          handleError: "handleError",
          plan: "plan"
        }
      )
      .addConditionalEdges(
        "plan",
        (state: SearchState) => state.phase === 'error' ? "handleError" : "search",
        {
          handleError: "handleError",
          search: "search"
        }
      )
      .addConditionalEdges(
        "search",
        (state: SearchState) => {
          if (state.phase === 'error') return "handleError";
          if ((state.currentSearchIndex || 0) < (state.searchQueries?.length || 0)) {
            return "search"; // Continue searching
          }
          return "scrape"; // Move to scraping
        },
        {
          handleError: "handleError",
          search: "search",
          scrape: "scrape"
        }
      )
      .addConditionalEdges(
        "scrape",
        (state: SearchState) => state.phase === 'error' ? "handleError" : "analyze",
        {
          handleError: "handleError",
          analyze: "analyze"
        }
      )
      .addConditionalEdges(
        "analyze",
        (state: SearchState) => {
          if (state.phase === 'error') return "handleError";
          if (state.phase === 'planning') return "plan";  // Retry with new searches
          return "synthesize";
        },
        {
          handleError: "handleError",
          plan: "plan",
          synthesize: "synthesize"
        }
      )
      .addConditionalEdges(
        "synthesize",
        (state: SearchState) => state.phase === 'error' ? "handleError" : "complete",
        {
          handleError: "handleError",
          complete: "complete"
        }
      )
      .addConditionalEdges(
        "handleError",
        (state: SearchState) => state.phase === 'error' ? END : "understand",
        {
          [END]: END,
          understand: "understand"
        }
      )
      .addEdge("complete", END);

    // Compile with optional checkpointing
    return workflow.compile(this.checkpointer ? { checkpointer: this.checkpointer } : undefined);
  }

  async search(
    query: string,
    onEvent: (event: SearchEvent) => void,
    context?: { query: string; response: string }[],
    checkpointId?: string
  ): Promise<void> {
    try {
      const initialState: SearchState = {
        query,
        context,
        sources: [],
        scrapedSources: [],
        processedSources: undefined,
        phase: 'understanding',
        currentSearchIndex: 0,
        maxRetries: SEARCH_CONFIG.MAX_RETRIES,
        retryCount: 0,
        understanding: undefined,
        searchQueries: undefined,
        finalAnswer: undefined,
        followUpQuestions: undefined,
        error: undefined,
        errorType: undefined,
        subQueries: undefined,
        searchAttempt: 0
      };

      // Configure with event callback
      const config: GraphConfig = {
        configurable: {
          eventCallback: onEvent,
          ...(checkpointId && this.checkpointer ? { thread_id: checkpointId } : {})
        }
      };

      // Invoke the graph with increased recursion limit
      await this.graph.invoke(initialState, {
        ...config,
        recursionLimit: 35  // Increased from default 25 to handle MAX_SEARCH_ATTEMPTS=5
      });
    } catch (error) {
      onEvent({
        type: 'error',
        error: error instanceof Error ? error.message : 'Search failed',
        errorType: 'unknown'
      });
    }
  }


  // Get current date for context
  private getCurrentDateContext(): string {
    const now = new Date();
    const dateStr = now.toLocaleDateString('en-US', { 
      weekday: 'long', 
      year: 'numeric', 
      month: 'long', 
      day: 'numeric' 
    });
    const year = now.getFullYear();
    const month = now.getMonth() + 1;
    
    return `Today's date is ${dateStr}. The current year is ${year} and it's currently ${month}/${year}.`;
  }

  // Pure helper methods (no side effects)
  private async analyzeQuery(query: string, context?: { query: string; response: string }[]): Promise<string> {
    let contextPrompt = '';
    if (context && context.length > 0) {
      contextPrompt = '\n\nPrevious conversation:\n';
      context.forEach(c => {
        contextPrompt += `User: ${c.query}\nAssistant: ${c.response.substring(0, SEARCH_CONFIG.CONTEXT_PREVIEW_LENGTH)}...\n\n`;
      });
    }
    
    const messages = [
      new SystemMessage(`${this.getCurrentDateContext()}

Analyze this search query and explain what you understand the user is looking for.

Instructions:
- Start with a clear, concise title (e.g., "Researching egg shortage" or "Understanding climate change impacts")
- Then explain in 1-2 sentences what aspects of the topic the user wants to know about
- If this relates to previous questions, acknowledge that connection
- Finally, mention that you'll search for information to help answer their question
- Only mention searching for "latest" information if the query is explicitly about recent events or current trends

Keep it natural and conversational, showing you truly understand their request.`),
      new HumanMessage(`Query: "${query}"${contextPrompt}`)
    ];
    
    const response = await this.llm.invoke(messages);
    return response.content.toString();
  }

  private async checkAnswersInSources(
    subQueries: Array<{ question: string; searchQuery: string; answered: boolean; answer?: string; confidence: number; sources: string[] }>,
    sources: Source[]
  ): Promise<typeof subQueries> {
    if (sources.length === 0) return subQueries;
    
    const messages = [
      new SystemMessage(`Check which questions have been answered by the provided sources.

For each question, determine:
1. If the sources contain a direct answer
2. The confidence level (0.0-1.0) that the question was fully answered
3. A brief answer summary if found

Guidelines:
- For "who" questions about people/founders: Mark as answered (0.8+ confidence) if you find names of specific people
- For "what" questions: Mark as answered (0.8+ confidence) if you find the specific information requested
- For "when" questions: Mark as answered (0.8+ confidence) if you find dates or time periods
- For "how many" questions: Require specific numbers (0.8+ confidence)
- For comparison questions: Require information about all items being compared
- If sources clearly answer the question but lack some minor details, use medium confidence (0.6-0.7)
- If sources mention the topic but don't answer the specific question, use low confidence (< 0.3)

Version number matching:
- "0528" in the question matches "0528", "-0528", "May 28", or "May 28, 2025" in sources
- Example: Question about "DeepSeek R1 0528" is ANSWERED if sources mention:
  - "DeepSeek R1-0528" (exact match)
  - "DeepSeek R1 was updated on May 28" (date match)
  - "DeepSeek's R1 model was updated on May 28, 2025" (date match)
- Hyphens and spaces in version numbers should be ignored when matching
- If the summary mentions the product and a matching date/version, that's a full answer

Special cases:
- If asking about a product/model with a version number (e.g., "ModelX v2.5.1" or "Product 0528"), check BOTH:
  1. If sources mention the EXACT version → mark as answered with high confidence (0.8+)
  2. If sources only mention the base product → mark as answered with medium confidence (0.6+)
- Example: Question "What is ProductX 1234?" 
  - If sources mention "ProductX 1234" specifically → confidence: 0.9
  - If sources only mention "ProductX" → confidence: 0.6
- IMPORTANT: For questions like "What is DeepSeek R1 0528?", if sources contain "DeepSeek R1-0528" or "DeepSeek R1 0528", that's a DIRECT match (confidence 0.9+)
- If multiple sources contradict whether something exists, use low confidence (0.3) but still provide what information was found

Important: Be generous in recognizing answers. If the source clearly provides the information asked for (e.g., "The founders are X, Y, and Z"), mark it as answered with high confidence.

Return ONLY a JSON array, no markdown formatting or code blocks:
[
  {
    "question": "the original question",
    "answered": true/false,
    "confidence": 0.0-1.0,
    "answer": "brief answer if found",
    "sources": ["urls that contain the answer"]
  }
]`),
      new HumanMessage(`Questions to check:
${subQueries.map(sq => sq.question).join('\n')}

Sources:
${sources.slice(0, SEARCH_CONFIG.MAX_SOURCES_TO_CHECK).map(s => {
  let sourceInfo = `URL: ${s.url}\nTitle: ${s.title}\n`;
  
  // Include summary if available (this is the key insight from the search)
  if (s.summary) {
    sourceInfo += `Summary: ${s.summary}\n`;
  }
  
  // Include content preview
  if (s.content) {
    sourceInfo += `Content: ${s.content.slice(0, SEARCH_CONFIG.ANSWER_CHECK_PREVIEW)}\n`;
  }
  
  return sourceInfo;
}).join('\n---\n')}`)
    ];

    try {
      const response = await this.llm.invoke(messages);
      let content = response.content.toString();
      
      // Strip markdown code blocks if present
      content = content.replace(/```json\s*/g, '').replace(/```\s*$/g, '').trim();
      
      const results = JSON.parse(content);
      
      // Update sub-queries with results
      return subQueries.map(sq => {
        const result = results.find((r: { question: string }) => r.question === sq.question);
        if (result && result.confidence > sq.confidence) {
          return {
            ...sq,
            answered: result.confidence >= SEARCH_CONFIG.MIN_ANSWER_CONFIDENCE,
            answer: result.answer,
            confidence: result.confidence,
            sources: [...new Set([...sq.sources, ...(result.sources || [])])]
          };
        }
        return sq;
      });
    } catch (error) {
      console.error('Error checking answers:', error);
      return subQueries;
    }
  }

  private async extractSubQueries(query: string): Promise<Array<{ question: string; searchQuery: string }>> {
    const messages = [
      new SystemMessage(`Extract the individual factual questions from this query. Each question should be something that can be definitively answered.

IMPORTANT: 
- When the user mentions something with a version/number (like "deepseek r1 0528"), include the FULL version in the question
- For the search query, you can simplify slightly but keep key identifiers
- Example: "deepseek r1 0528" → question: "What is DeepSeek R1 0528?", searchQuery: "DeepSeek R1 0528"

Examples:
"Who founded Anthropic and when" → 
[
  {"question": "Who founded Anthropic?", "searchQuery": "Anthropic founders"},
  {"question": "When was Anthropic founded?", "searchQuery": "Anthropic founded date year"}
]

"What is OpenAI's Q3 2024 revenue and who is their VP of Infrastructure" →
[
  {"question": "What was OpenAI's Q3 2024 revenue?", "searchQuery": "OpenAI Q3 2024 revenue earnings"},
  {"question": "Who is OpenAI's VP of Infrastructure?", "searchQuery": "OpenAI VP Infrastructure executive team"}
]

"Tell me about Product A + Model B version 123" →
[
  {"question": "What is Product A?", "searchQuery": "Product A features"},
  {"question": "What is Model B version 123?", "searchQuery": "Model B"}
]

"Who founded Company X, compare Product A and Product B, and tell me about Technology Y + Model Z 1234" →
[
  {"question": "Who founded Company X?", "searchQuery": "Company X founders"},
  {"question": "How do Product A and Product B compare?", "searchQuery": "Product A vs Product B comparison"},
  {"question": "What is Technology Y?", "searchQuery": "Technology Y features"},
  {"question": "What is Model Z 1234?", "searchQuery": "Model Z"}
]

Important: 
- For comparison requests, create a single question/search that covers both items
- If a term looks like it might be a model name with a version/date (like "R1 0528"), treat it as a single entity first, but create a search query that focuses on the main product name
- Keep the number of sub-queries reasonable (aim for 3-5 max)

Return ONLY a JSON array of {question, searchQuery} objects.`),
      new HumanMessage(`Query: "${query}"`)
    ];

    try {
      const response = await this.llm.invoke(messages);
      return JSON.parse(response.content.toString());
    } catch {
      // Fallback: treat as single query
      return [{ question: query, searchQuery: query }];
    }
  }

  // This method was removed as it's not used in the current implementation
  // Search queries are now generated from sub-queries in the plan node

  private async generateAlternativeSearchQueries(
    subQueries: Array<{ question: string; searchQuery: string; answered: boolean; answer?: string; confidence: number; sources: string[] }>,
    previousAttempts: number
  ): Promise<string[]> {
    const unansweredQueries = subQueries.filter(sq => !sq.answered || sq.confidence < SEARCH_CONFIG.MIN_ANSWER_CONFIDENCE);
    
    // If we're on attempt 3 and still searching for the same thing, just give up on that specific query
    if (previousAttempts >= 2) {
      const problematicQueries = unansweredQueries.filter(sq => {
        // Check if the question contains a version number or specific identifier that might not exist
        const hasVersionPattern = /\b\d{3,4}\b|\bv\d+\.\d+|\bversion\s+\d+/i.test(sq.question);
        const hasFailedMultipleTimes = previousAttempts >= 2;
        return hasVersionPattern && hasFailedMultipleTimes;
      });
      
      if (problematicQueries.length > 0) {
        // Return generic searches that might find partial info
        return problematicQueries.map(sq => {
          const baseTerm = sq.question.replace(/0528|specific version/gi, '').trim();
          return baseTerm.substring(0, 50); // Keep it short
        });
      }
    }
    
    const messages = [
      new SystemMessage(`${this.getCurrentDateContext()}

Generate ALTERNATIVE search queries for questions that weren't answered in previous attempts.

Previous search attempts: ${previousAttempts}
Previous queries that didn't find answers:
${unansweredQueries.map(sq => `- Question: "${sq.question}"\n  Previous search: "${sq.searchQuery}"`).join('\n')}

IMPORTANT: If searching for something with a specific version/date that keeps failing (like "R1 0528"), try searching for just the base product without the version.

Generate NEW search queries using these strategies:
1. Try broader or more general terms
2. Try different phrasings or synonyms
3. Remove specific qualifiers (like years or versions) if they're too restrictive
4. Try searching for related concepts that might contain the answer
5. For products that might not exist, search for the company or base product name

Examples of alternative searches:
- Original: "ModelX 2024.05" → Alternative: "ModelX latest version"
- Original: "OpenAI Q3 2024 revenue" → Alternative: "OpenAI financial results 2024"
- Original: "iPhone 15 Pro features" → Alternative: "latest iPhone specifications"

Return one alternative search query per unanswered question, one per line.`),
      new HumanMessage(`Generate alternative searches for these ${unansweredQueries.length} unanswered questions.`)
    ];

    try {
      const response = await this.llm.invoke(messages);
      const result = response.content.toString();
      
      const queries = result
        .split('\n')
        .map(q => q.trim())
        .map(q => q.replace(/^["']|["']$/g, ''))
        .map(q => q.replace(/^\d+\.\s*/, ''))
        .map(q => q.replace(/^[-*#]\s*/, ''))
        .filter(q => q.length > 0)
        .filter(q => !q.match(/^```/))
        .filter(q => q.length > 3);
      
      return queries.slice(0, SEARCH_CONFIG.MAX_SEARCH_QUERIES);
    } catch {
      // Fallback: return original queries with slight modifications
      return unansweredQueries.map(sq => sq.searchQuery + " news reports").slice(0, SEARCH_CONFIG.MAX_SEARCH_QUERIES);
    }
  }

  private scoreContent(content: string, query: string): number {
    const queryWords = query.toLowerCase().split(' ');
    const contentLower = content.toLowerCase();
    
    let score = 0;
    for (const word of queryWords) {
      if (contentLower.includes(word)) score += 0.2;
    }
    
    return Math.min(score, 1);
  }

  private async summarizeContent(content: string, query: string): Promise<string> {
    try {
      const messages = [
        new SystemMessage(`${this.getCurrentDateContext()}

Extract ONE key finding from this content that's SPECIFICALLY relevant to the search query.

CRITICAL: Only summarize information that directly relates to the search query.
- If searching for "Samsung phones", only mention Samsung phone information
- If searching for "Firecrawl founders", only mention founder information
- If no relevant information is found, just return the most relevant fact from the page

Instructions:
- Return just ONE sentence with a specific finding
- Include numbers, dates, or specific details when available
- Keep it under ${SEARCH_CONFIG.SUMMARY_CHAR_LIMIT} characters
- Don't say "No relevant information was found" - find something relevant to the current search`),
        new HumanMessage(`Query: "${query}"\n\nContent: ${content.slice(0, 2000)}`)
      ];
      
      const response = await this.llm.invoke(messages);
      return response.content.toString().trim();
    } catch {
      return '';
    }
  }

  private async generateStreamingAnswer(
    query: string,
    sources: Source[],
    onChunk: (chunk: string) => void,
    context?: { query: string; response: string }[]
  ): Promise<string> {
    const sourcesText = sources
      .map((s, i) => {
        if (!s.content) return `[${i + 1}] ${s.title}\n[No content available]`;
        return `[${i + 1}] ${s.title}\n${s.content}`;
      })
      .join('\n\n');
    
    let contextPrompt = '';
    if (context && context.length > 0) {
      contextPrompt = '\n\nPrevious conversation for context:\n';
      context.forEach(c => {
        contextPrompt += `User: ${c.query}\nAssistant: ${c.response.substring(0, 300)}...\n\n`;
      });
    }
    
    const messages = [
      new SystemMessage(`${this.getCurrentDateContext()}

Answer the user's question based on the provided sources. Provide a clear, comprehensive answer with citations [1], [2], etc. Use markdown formatting for better readability. If this question relates to previous topics discussed, make connections where relevant.`),
      new HumanMessage(`Question: "${query}"${contextPrompt}\n\nBased on these sources:\n${sourcesText}`)
    ];
    
    let fullText = '';
    
    try {
      const stream = await this.streamingLlm.stream(messages);
      
      for await (const chunk of stream) {
        const content = chunk.content;
        if (typeof content === 'string') {
          fullText += content;
          onChunk(content);
        }
      }
    } catch {
      // Fallback to non-streaming if streaming fails
      const response = await this.llm.invoke(messages);
      fullText = response.content.toString();
      onChunk(fullText);
    }
    
    return fullText;
  }

  private async generateFollowUpQuestions(
    originalQuery: string,
    answer: string,
    _sources: Source[],
    context?: { query: string; response: string }[]
  ): Promise<string[]> {
    try {
      let contextPrompt = '';
      if (context && context.length > 0) {
        contextPrompt = '\n\nPrevious conversation topics:\n';
        context.forEach(c => {
          contextPrompt += `- ${c.query}\n`;
        });
        contextPrompt += '\nConsider the full conversation flow when generating follow-ups.\n';
      }
      
      const messages = [
        new SystemMessage(`${this.getCurrentDateContext()}

Based on this search query and answer, generate 3 relevant follow-up questions that the user might want to explore next.

Instructions:
- Generate exactly 3 follow-up questions
- Each question should explore a different aspect or dig deeper into the topic
- Questions should be natural and conversational
- They should build upon the information provided in the answer
- Make them specific and actionable
- Keep each question under 80 characters
- Return only the questions, one per line, no numbering or bullets
- Consider the entire conversation context when generating questions
- Only include time-relevant questions if the original query was about current events or trends

Examples of good follow-up questions:
- "How does this compare to [alternative]?"
- "Can you explain [technical term] in more detail?"
- "What are the practical applications of this?"
- "What are the main benefits and drawbacks?"
- "How is this typically implemented?"`),
        new HumanMessage(`Original query: "${originalQuery}"\n\nAnswer summary: ${answer.length > 1000 ? answer.slice(0, 1000) + '...' : answer}${contextPrompt}`)
      ];
      
      const response = await this.llm.invoke(messages);
      const questions = response.content.toString()
        .split('\n')
        .map(q => q.trim())
        .filter(q => q.length > 0 && q.length < 80)
        .slice(0, 3);
      
      return questions.length > 0 ? questions : [];
    } catch {
      return [];
    }
  }
}
```

## File: `lib/rate-limit.ts`
```typescript
import { Ratelimit } from "@upstash/ratelimit";
import { Redis } from "@upstash/redis";
import { NextRequest } from "next/server";

// Create a new ratelimiter that allows 50 requests per day per IP per endpoint
export const getRateLimiter = (endpoint: string) => {
  // Check if we're in a production environment to apply rate limiting
  // In development, we don't want to be rate limited for testing
  if (process.env.NODE_ENV !== "production" && !process.env.UPSTASH_REDIS_REST_URL) {
    return null;
  }

  // Requires the following environment variables:
  // UPSTASH_REDIS_REST_URL
  // UPSTASH_REDIS_REST_TOKEN
  const redis = Redis.fromEnv();

  return new Ratelimit({
    redis,
    limiter: Ratelimit.fixedWindow(50, "1 d"),
    analytics: true,
    prefix: `ratelimit:${endpoint}`,
  });
};

// Helper function to get the IP from a NextRequest or default to a placeholder
export const getIP = (request: NextRequest): string => {
  const forwarded = request.headers.get("x-forwarded-for");
  const realIp = request.headers.get("x-real-ip");
  
  if (forwarded) {
    return forwarded.split(/, /)[0];
  }
  
  if (realIp) {
    return realIp;
  }
  
  // Default to placeholder IP if none found
  return "127.0.0.1";
};

// Helper function to check if a request is rate limited
export const isRateLimited = async (request: NextRequest, endpoint: string) => {
  const limiter = getRateLimiter(endpoint);
  
  // If no limiter is available (e.g., in development), allow the request
  if (!limiter) {
    return { success: true, limit: 50, remaining: 50 };
  }
  
  // Get the IP from the request
  const ip = getIP(request);
  
  // Check if the IP has exceeded the rate limit
  const result = await limiter.limit(ip);
  
  return {
    success: result.success,
    limit: result.limit,
    remaining: result.remaining,
  };
}; 
```

## File: `lib/utils.ts`
```typescript
import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
```


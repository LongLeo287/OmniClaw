---
id: open-researcher-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:15.590947
---

# KNOWLEDGE EXTRACT: open-researcher
> **Extracted on:** 2026-03-30 13:15:07
> **Source:** open-researcher

---

## File: `.env.local.example`
```
# Open Researcher Environment Variables
# Copy this file to .env.local and fill in your actual API keys

# Required: Anthropic API key for Claude AI functionality
# Get yours at: https://console.anthropic.com/
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Optional: Firecrawl API key for web scraping
# If not provided, you can add it through the UI
# Get yours at: https://www.firecrawl.dev/
FIRECRAWL_API_KEY=your_firecrawl_api_key_here
```

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
!.env.local.example

# vercel
.vercel

# typescript
*.tsbuildinfo
next-env.d.ts
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
  /* config options here */
};

export default nextConfig;
```

## File: `package.json`
```json
{
  "name": "open-research",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev --turbopack",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "@anthropic-ai/sdk": "^0.54.0",
    "@mendable/firecrawl-js": "^1.25.1",
    "@radix-ui/react-dialog": "^1.1.14",
    "@radix-ui/react-slot": "^1.2.3",
    "@radix-ui/react-tooltip": "^1.2.7",
    "ai": "^4.3.16",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "lucide-react": "^0.511.0",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "react-markdown": "^10.1.0",
    "remark-gfm": "^4.0.1",
    "sonner": "^2.0.3",
    "tailwind-merge": "^3.3.0",
    "tailwindcss-animate": "^1.0.7",
    "next": "15.3.4"
  },
  "devDependencies": {
    "typescript": "^5",
    "@types/node": "^20",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "@tailwindcss/postcss": "^4",
    "tailwindcss": "^4",
    "eslint": "^9",
    "eslint-config-next": "15.3.4",
    "@eslint/eslintrc": "^3"
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

## File: `README.md`
```markdown
<h1 align="center">Open Researcher</h1>

<p align="center">
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGJncnpmamlzc3RnMzNpeXNwcGk1Z3kwemd6c2w1ZDdxcGZwdWJwdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hhNLykzY76wu7oGFU0/giphy.gif" alt="Open Researcher Demo" width="100%">
</p>

A powerful AI-powered research tool that combines Firecrawl's web scraping capabilities with advanced AI reasoning to help you search, analyze, and understand web content.

## Features

- **AI-Powered Search**: Intelligently search and analyze web content
- **Real-time Web Scraping**: Powered by Firecrawl for accurate, up-to-date information
- **Thinking Display**: See the AI's reasoning process in real-time
- **Smart Citations**: Automatic source tracking and citation generation
- **Split View Interface**: Side-by-side view of chat and search results

## Prerequisites

- Node.js 18+ and npm
- API Keys (at least one required):
  - `ANTHROPIC_API_KEY` - For AI functionality
  - `FIRECRAWL_API_KEY` - For web scraping (can be added via UI)

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/mendableai/open-researcher
   cd open-researcher
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Set up environment variables**
   ```bash
   cp .env.local.example .env.local
   ```
   
   Edit `.env.local` and add your API keys:
   ```
   ANTHROPIC_API_KEY=your_anthropic_api_key
   FIRECRAWL_API_KEY=your_firecrawl_api_key  # Optional, can be added via UI
   ```

4. **Run the development server**
   ```bash
   npm run dev
   ```

5. **Open your browser**
   Navigate to [http://localhost:3000](http://localhost:3000)

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `ANTHROPIC_API_KEY` | Yes | Claude API key for AI functionality |
| `FIRECRAWL_API_KEY` | No* | Firecrawl API key for web scraping |

*Can be provided through the UI if not set in environment variables

## Getting API Keys

- **Anthropic API Key**: Visit [Anthropic Console](https://console.anthropic.com/)
- **Firecrawl API Key**: Visit [Firecrawl](https://www.firecrawl.dev/)

## Usage

1. **Basic Search**: Enter your query in the chat interface
2. **Web Analysis**: The AI will automatically search and analyze relevant web content
3. **Follow-up Questions**: Ask follow-up questions to dive deeper
4. **View Sources**: Click on citations to see source information

## Project Structure

```
open-research/
├── app/
│   ├── api/              # API routes
│   ├── open-researcher/  # Main application page
│   └── layout.tsx        # Root layout
├── components/           # React components
│   ├── ui/              # UI components
│   └── thinking-chat.tsx # Main chat interface
├── lib/                 # Utility functions
└── public/              # Static assets
```

## Development

```bash
# Run development server
npm run dev

# Build for production
npm run build

# Start production server
npm start

# Run linting
npm run lint
```

## Tech Stack

- **Next.js 15** - React framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **Anthropic Claude** - AI model
- **Firecrawl** - Web scraping
- **Radix UI** - UI components

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Firecrawl](https://www.firecrawl.dev/) for powerful web scraping
- Powered by [Anthropic's Claude](https://www.anthropic.com/) for AI capabilities
- UI components from [Radix UI](https://www.radix-ui.com/) and [shadcn/ui](https://ui.shadcn.com/)
```

## File: `tailwind.config.ts`
```typescript
import type { Config } from "tailwindcss";

const config: Config = {
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
        sans: ["var(--font-inter)", "ui-sans-serif", "system-ui", "sans-serif"],
        mono: ["ui-monospace", "SFMono-Regular", "monospace"],
      },
    },
  },
  plugins: [],
};

export default config; 
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

## File: `app/globals.css`
```css
@import "tailwindcss";

@layer utilities {
  /* Hide scrollbar for Chrome, Safari and Opera */
  .scrollbar-hide::-webkit-scrollbar {
    display: none;
  }
  
  /* Hide scrollbar for IE, Edge and Firefox */
  .scrollbar-hide {
    -ms-overflow-style: none;  /* IE and Edge */
    scrollbar-width: none;  /* Firefox */
  }
}

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
    --radius: 0.5rem;
    --chart-1: 12 76% 61%;
    --chart-2: 173 58% 39%;
    --chart-3: 197 37% 24%;
    --chart-4: 43 74% 66%;
    --chart-5: 27 87% 67%;
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
  }
}

@layer base {
  * {
    border-color: hsl(var(--border));
  }
  body {
    background-color: hsl(var(--background));
    color: hsl(var(--foreground));
  }
  
  /* Fix for Tailwind animations disappearing */
  [class*="animate-"] {
    animation-fill-mode: both;
  }
}

/* Custom animation utilities */
@layer utilities {
  /* CSS Variables for animation */
  :root {
    /* Durations */
    --d-1: 150ms;
    --d-2: 300ms;
    --d-3: 500ms;
    --d-4: 700ms;
    --d-5: 1000ms;
    
    /* Timings (delays) */
    --t-1: 100ms;
    --t-2: 200ms;
    --t-3: 300ms;
    --t-4: 400ms;
    --t-5: 500ms;
  }

  /* Fade up animation */
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
    animation: fade-up 500ms ease-out forwards;
  }

  /* Fade in animation */
  @keyframes fade-in {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }

  .animate-fade-in {
    animation: fade-in 500ms ease-out forwards;
  }

  /* Slide in from right */
  @keyframes slide-in-right {
    from {
      opacity: 0;
      transform: translateX(100px);
    }
    to {
      opacity: 1;
      transform: translateX(0);
    }
  }

  .animate-slide-in-right {
    animation: slide-in-right 500ms ease-out forwards;
  }

  /* Scale in content animation */
  @keyframes scale-in-content {
    from {
      opacity: 0;
      transform: scale(0.95);
    }
    to {
      opacity: 1;
      transform: scale(1);
    }
  }

  .animate-scale-in-content {
    animation: scale-in-content 500ms ease-out forwards;
  }

  /* Slide up animation */
  @keyframes slide-up {
    from {
      opacity: 0;
      transform: translateY(40px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  .animate-slide-up {
    animation: slide-up 700ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
  }

  /* Number transition effect */
  .number-transition {
    transition: all 300ms cubic-bezier(0.4, 0, 0.2, 1);
  }

  /* Scanning animations */
  @keyframes scan {
    from {
      top: 0%;
    }
    to {
      top: 100%;
    }
  }

  .animate-scan {
    animation: scan 3s linear infinite;
  }

  /* Scanner effect for screenshot scanning */
  @keyframes scanner {
    0% {
      top: 0;
    }
    100% {
      top: 100%;
    }
  }

  .scanner-line {
    position: absolute;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(
      to bottom,
      transparent,
      rgba(251, 146, 60, 0.8),
      transparent
    );
    box-shadow: 0 0 10px rgba(251, 146, 60, 0.8);
    animation: scanner 2s linear infinite;
  }

  .scanner-line::before {
    content: '';
    position: absolute;
    left: 0;
    right: 0;
    height: 20px;
    background: linear-gradient(
      to bottom,
      transparent,
      rgba(251, 146, 60, 0.1),
      transparent
    );
    top: -10px;
  }

  /* Synchronized scrolling for long screenshots */
  @keyframes screenshot-scroll {
    0% {
      transform: translateY(0);
    }
    100% {
      transform: translateY(calc(-100% + 100vh));
    }
  }

  .screenshot-scroll-container {
    will-change: transform;
  }

  /* Apply animation only when marked as tall */
  .animate-screenshot-scroll {
    animation: screenshot-scroll 4s linear infinite;
  }
  
  /* Scanner moves fast at 2s, screenshot scrolls very slowly at 20s */
  .scanner-line {
    animation-duration: 2s;
  }
  
  .animate-screenshot-scroll {
    animation-duration: 40s; /* 20x slower than scanner - very slow scrolling */
  }

  /* Animated cursor styles */
  @keyframes cursor-click {
    0% { transform: scale(1); }
    50% { transform: scale(0.8); }
    100% { transform: scale(1); }
  }

  /* Selection pulse animation */
  @keyframes selection-pulse {
    0%, 100% {
      border-color: rgba(251, 146, 60, 1);
      box-shadow: 0 0 0 0 rgba(251, 146, 60, 0.4);
    }
    50% {
      border-color: rgba(251, 146, 60, 0.7);
      box-shadow: 0 0 0 8px rgba(251, 146, 60, 0);
    }
  }

  .animate-selection-pulse {
    animation: selection-pulse 1.5s ease-in-out infinite;
  }

  /* Green selection pulse animation */
  @keyframes selection-pulse-green {
    0%, 100% {
      border-color: rgba(34, 197, 94, 1);
      box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.4);
      background-color: rgba(34, 197, 94, 0.05);
    }
    50% {
      border-color: rgba(34, 197, 94, 0.7);
      box-shadow: 0 0 0 6px rgba(34, 197, 94, 0);
      background-color: rgba(34, 197, 94, 0.1);
    }
  }

  .animate-selection-pulse-green {
    animation: selection-pulse-green 1.5s ease-in-out infinite;
  }

  /* Button press animation */
  @keyframes button-press {
    0% { transform: scale(1); }
    50% { transform: scale(0.8); background-color: rgb(220 38 38); }
    100% { transform: scale(1); background-color: rgb(239 68 68); }
  }

  .animate-button-press {
    animation: button-press 0.3s ease-out;
    animation-delay: 1.5s; /* Wait for cursor to reach button */
  }

  @keyframes scan-vertical {
    0% {
      transform: translateY(-100%);
    }
    50% {
      transform: translateY(100%);
    }
    100% {
      transform: translateY(-100%);
    }
  }

  .animate-scan-vertical {
    animation: scan-vertical 4s ease-in-out infinite;
  }

  @keyframes scan-horizontal {
    0% {
      transform: translateX(-100%);
    }
    50% {
      transform: translateX(100%);
    }
    100% {
      transform: translateX(-100%);
    }
  }

  .animate-scan-horizontal {
    animation: scan-horizontal 3s ease-in-out infinite;
  }

  /* Pulse animation for grid */
  @keyframes grid-pulse {
    0%, 100% {
      opacity: 0.1;
    }
    50% {
      opacity: 0.3;
    }
  }

  .animate-grid-pulse {
    animation: grid-pulse 2s ease-in-out infinite;
  }
}

/* Custom scrollbar styles */
@layer components {
  .custom-scrollbar {
    scrollbar-width: thin;
    scrollbar-color: #d1d5db #f3f4f6;
  }

  .custom-scrollbar::-webkit-scrollbar {
    width: 8px;
    height: 8px;
  }

  .custom-scrollbar::-webkit-scrollbar-track {
    background: #f3f4f6;
    border-radius: 4px;
  }

  .custom-scrollbar::-webkit-scrollbar-thumb {
    background: #d1d5db;
    border-radius: 4px;
  }

  .custom-scrollbar::-webkit-scrollbar-thumb:hover {
    background: #9ca3af;
  }

  .dark .custom-scrollbar {
    scrollbar-color: #4b5563 #1f2937;
  }

  .dark .custom-scrollbar::-webkit-scrollbar-track {
    background: #1f2937;
  }

  .dark .custom-scrollbar::-webkit-scrollbar-thumb {
    background: #4b5563;
  }

  .dark .custom-scrollbar::-webkit-scrollbar-thumb:hover {
    background: #6b7280;
  }
}
```

## File: `app/layout.tsx`
```tsx
import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import { Toaster } from "sonner";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {children}
        <Toaster />
      </body>
    </html>
  );
}
```

## File: `app/page.tsx`
```tsx
import { Metadata } from 'next'
import OpenResearcherContent from './open-researcher/open-researcher-content'

export const metadata: Metadata = {
  title: 'Open Researcher',
  description: 'Firecrawl-powered search, scrape, and agentic reasoning',
}

export default function Home() {
  return <OpenResearcherContent />
}
```

## File: `app/api/check-env/route.ts`
```typescript
import { NextResponse } from 'next/server';

export async function GET() {
  const environmentStatus = {
    FIRECRAWL_API_KEY: !!process.env.FIRECRAWL_API_KEY,
    ANTHROPIC_API_KEY: !!process.env.ANTHROPIC_API_KEY,
    FIRESTARTER_DISABLE_CREATION_DASHBOARD: process.env.FIRESTARTER_DISABLE_CREATION_DASHBOARD === 'true',
  };

  // Add debug info (only in development)
  const debugInfo = process.env.NODE_ENV === 'development' ? {
    anthropicKeyPrefix: process.env.ANTHROPIC_API_KEY ? process.env.ANTHROPIC_API_KEY.substring(0, 10) + '...' : 'NOT SET',
    firecrawlKeyPrefix: process.env.FIRECRAWL_API_KEY ? process.env.FIRECRAWL_API_KEY.substring(0, 10) + '...' : 'NOT SET',
    nodeEnv: process.env.NODE_ENV
  } : {};

  return NextResponse.json({ 
    environmentStatus,
    ...debugInfo
  });
} 
```

## File: `app/api/open-researcher/route.ts`
```typescript
import { NextRequest, NextResponse } from 'next/server'
import { performResearchWithStreaming } from '@/lib/open-researcher-agent'

export async function POST(req: NextRequest) {
  try {
    const { query } = await req.json()

    if (!query) {
      return NextResponse.json({ error: 'Query is required' }, { status: 400 })
    }

    // Check for Anthropic API key in environment
    if (!process.env.ANTHROPIC_API_KEY) {
      // ANTHROPIC_API_KEY is not configured in environment variables
      return NextResponse.json(
        { error: 'ANTHROPIC_API_KEY is not configured. Please add it to your Vercel environment variables.' },
        { status: 500 }
      )
    }

    // Get Firecrawl API key from headers first, then fall back to environment variables
    const firecrawlApiKey = req.headers.get('X-Firecrawl-API-Key') || process.env.FIRECRAWL_API_KEY

    if (!firecrawlApiKey) {
      // FIRECRAWL_API_KEY is not configured
      return NextResponse.json(
        { error: 'FIRECRAWL_API_KEY is not configured. Please add it via the interface.' },
        { status: 500 }
      )
    }
    
    // Set Firecrawl API key as environment variable for the agent to use
    process.env.FIRECRAWL_API_KEY = firecrawlApiKey
    
    // API Keys configured successfully

    // Create a streaming response
    const encoder = new TextEncoder()
    const stream = new ReadableStream({
      async start(controller) {
        try {
          // Perform research with streaming events
          const finalResponse = await performResearchWithStreaming(query, (event) => {
            // Add timestamp to events
            const eventWithTimestamp = { ...event, timestamp: Date.now() }
            
            // Send event as SSE
            const data = `data: ${JSON.stringify({ type: 'event', event: eventWithTimestamp })}\n\n`
            controller.enqueue(encoder.encode(data))
          })

          // Send final response
          if (finalResponse) {
            const responseData = `data: ${JSON.stringify({ type: 'response', content: finalResponse })}\n\n`
            controller.enqueue(encoder.encode(responseData))
          }

          // Send done event
          const doneData = `data: ${JSON.stringify({ type: 'done' })}\n\n`
          controller.enqueue(encoder.encode(doneData))
          controller.close()
        } catch (error) {
          // Research error occurred
          const errorMessage = error instanceof Error ? error.message : 'Unknown error'
          const errorDetails = error instanceof Error && error.stack ? error.stack : ''
          
          // Error details logged internally
          
          // More user-friendly error messages
          let userFriendlyError = errorMessage
          if (errorMessage.includes('Model error')) {
            userFriendlyError = 'The Anthropic claude-opus-4 model is not available. This might be due to regional restrictions or API tier limitations.'
          } else if (errorMessage.includes('Beta feature error')) {
            userFriendlyError = 'The interleaved thinking feature is not enabled for your Anthropic API key. This is a beta feature that may require special access.'
          } else if (errorMessage.includes('Authentication error')) {
            userFriendlyError = 'Invalid Anthropic API key. Please check your environment variables in Vercel.'
          }
          
          const errorData = `data: ${JSON.stringify({ 
            type: 'error', 
            error: userFriendlyError,
            originalError: errorMessage,
            details: process.env.NODE_ENV === 'development' ? errorDetails : undefined
          })}\n\n`
          controller.enqueue(encoder.encode(errorData))
          controller.close()
        }
      }
    })

    return new NextResponse(stream, {
      headers: {
        'Content-Type': 'text/event-stream',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
      },
    })
  } catch (error) {
    // API route error occurred
    const errorMessage = error instanceof Error ? error.message : 'Unknown error'
    
    // Log more details for debugging
    // Full error details logged internally
    
    return NextResponse.json(
      { 
        error: 'Internal server error',
        message: errorMessage,
        hint: 'Check the Vercel function logs for more details'
      },
      { status: 500 }
    )
  }
}
```

## File: `app/api/open-researcher/follow-up/route.ts`
```typescript
import { NextRequest, NextResponse } from 'next/server'
import Anthropic from '@anthropic-ai/sdk'

export async function POST(req: NextRequest) {
  try {
    const { query } = await req.json()

    if (!query) {
      return NextResponse.json({ error: 'Query is required' }, { status: 400 })
    }

    // Check for Anthropic API key
    if (!process.env.ANTHROPIC_API_KEY) {
      return NextResponse.json(
        { error: 'ANTHROPIC_API_KEY is not configured' },
        { status: 500 }
      )
    }

    const anthropic = new Anthropic({
      apiKey: process.env.ANTHROPIC_API_KEY,
    })

    // Generate follow-up questions based on the initial query
    const prompt = `Based on this search query: "${query}"

Generate 5 relevant follow-up questions that would help explore this topic further. The questions should:
1. Be directly related to the original query
2. Explore different aspects or deeper details
3. Be concise and clear

Format the response as a JSON array of strings, like:
["question 1", "question 2", "question 3", "question 4", "question 5"]

Only return the JSON array, nothing else.`

    const response = await anthropic.messages.create({
      model: 'claude-3-haiku-20240307',
      max_tokens: 300,
      temperature: 0.7,
      messages: [
        {
          role: 'user',
          content: prompt
        }
      ]
    })

    const content = response.content[0]
    if (content.type !== 'text') {
      throw new Error('Unexpected response type')
    }

    // Parse the JSON response
    try {
      const questions = JSON.parse(content.text)
      if (!Array.isArray(questions)) {
        throw new Error('Response is not an array')
      }
      
      return NextResponse.json({ questions })
    } catch {
      // Failed to parse follow-up questions
      return NextResponse.json({ questions: [] })
    }

  } catch (error) {
    // Error generating follow-up questions
    return NextResponse.json(
      { error: 'Failed to generate follow-up questions' },
      { status: 500 }
    )
  }
}
```

## File: `app/api/scrape/route.ts`
```typescript
import { NextRequest, NextResponse } from 'next/server';
import FirecrawlApp from '@mendable/firecrawl-js';

interface ScrapeRequestBody {
  url?: string;
  urls?: string[];
  [key: string]: unknown;
}

interface ScrapeResult {
  success: boolean;
  data?: Record<string, unknown>;
  error?: string;
}

interface ApiError extends Error {
  status?: number;
}

export async function POST(request: NextRequest) {
  let apiKey = process.env.FIRECRAWL_API_KEY;
  
  if (!apiKey) {
    const headerApiKey = request.headers.get('X-Firecrawl-API-Key');
    
    if (!headerApiKey) {
      return NextResponse.json({ 
        success: false, 
        error: 'API configuration error. Please try again later or contact support.' 
      }, { status: 500 });
    }
    
    apiKey = headerApiKey;
  }

  try {
    const app = new FirecrawlApp({ apiKey });
    const body = await request.json() as ScrapeRequestBody;
    const { url, urls, ...params } = body;

    let result: ScrapeResult;

    if (url && typeof url === 'string') {
      result = await app.scrapeUrl(url, params) as ScrapeResult;
    } else if (urls && Array.isArray(urls)) {
      result = await app.batchScrapeUrls(urls, params) as ScrapeResult;
    } else {
      return NextResponse.json({ success: false, error: 'Invalid request format. Please check your input and try again.' }, { status: 400 });
    }
    
    return NextResponse.json(result);

  } catch (error: unknown) {
    // Error in /api/scrape endpoint (SDK)
    const err = error as ApiError;
    const errorStatus = typeof err.status === 'number' ? err.status : 500;
    return NextResponse.json({ success: false, error: 'An error occurred while processing your request. Please try again later.' }, { status: errorStatus });
  }
} 
```

## File: `app/open-researcher/open-researcher-content.tsx`
```tsx
'use client'

import { useState, useEffect } from 'react'
import Link from 'next/link'
import { Github, ExternalLink, Loader2 } from 'lucide-react'
import { ThinkingChat } from '@/components/thinking-chat'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from '@/components/ui/dialog'
import { toast } from 'sonner'

export default function OpenResearcherContent() {
  const [hasMessages, setHasMessages] = useState(false)
  const [showApiKeyModal, setShowApiKeyModal] = useState(false)
  const [firecrawlApiKey, setFirecrawlApiKey] = useState('')
  const [isValidatingApiKey, setIsValidatingApiKey] = useState(false)
  const [hasFirecrawlKey, setHasFirecrawlKey] = useState(false)

  useEffect(() => {
    // Check for Firecrawl API key on mount
    fetch('/api/check-env')
      .then(res => res.json())
      .then(data => {
        const hasEnvFirecrawlKey = data.environmentStatus.FIRECRAWL_API_KEY
        setHasFirecrawlKey(hasEnvFirecrawlKey)

        // Check localStorage for saved key if not in env
        if (!hasEnvFirecrawlKey) {
          const savedFirecrawlKey = localStorage.getItem('firecrawl_api_key')
          if (savedFirecrawlKey) {
            setFirecrawlApiKey(savedFirecrawlKey)
            setHasFirecrawlKey(true)
          }
        }
      })
      .catch(() => {
        // Fallback to checking localStorage
        const savedFirecrawlKey = localStorage.getItem('firecrawl_api_key')
        if (savedFirecrawlKey) {
          setFirecrawlApiKey(savedFirecrawlKey)
          setHasFirecrawlKey(true)
        }
      })
  }, [])

  const handleApiKeySubmit = async () => {
    if (!firecrawlApiKey.trim()) {
      toast.error('Please enter a valid Firecrawl API key')
      return
    }

    setIsValidatingApiKey(true)

    try {
      // Test the Firecrawl API key
      const response = await fetch('/api/scrape', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-Firecrawl-API-Key': firecrawlApiKey,
        },
        body: JSON.stringify({ url: 'https://example.com' }),
      })

      if (!response.ok) {
        throw new Error('Invalid Firecrawl API key')
      }

      // Save the API key to localStorage
      localStorage.setItem('firecrawl_api_key', firecrawlApiKey)
      setHasFirecrawlKey(true)
      toast.success('API key saved successfully!')
      setShowApiKeyModal(false)
    } catch {
      toast.error('Invalid API key. Please check and try again.')
    } finally {
      setIsValidatingApiKey(false)
    }
  }

  return (
    <div className="min-h-screen flex flex-col">
      {/* Header */}
      <header className="py-4">
        <div className={`px-4 sm:px-6 lg:px-8 transition-all duration-700 ease-in-out ${hasMessages ? 'max-w-[1400px]' : 'max-w-4xl'
          } mx-auto`}>
          <div className="flex items-center justify-between">
            <Link href="https://firecrawl.dev" target="_blank" rel="noopener noreferrer">
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img
                src="/firecrawl-logo-with-fire.png"
                alt="Firecrawl Logo"
                width={113}
                height={24}
                className="w-[113px] h-auto"
              />
            </Link>
            <Button
              variant="code"
              asChild
            >
              <Link
                href="https://github.com/mendableai/open-researcher"
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center gap-2"
              >
                <Github className="h-4 w-4" />
                Use this template
              </Link>
            </Button>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <div className={`px-4 sm:px-6 lg:px-8 transition-all duration-700 ease-in-out ${hasMessages
          ? 'pt-0 pb-0 opacity-0 max-h-0 overflow-hidden'
          : 'pt-8 pb-2 opacity-100 max-h-96'
        }`}>
        <div className="max-w-4xl mx-auto text-center">
          <h1 className="text-[2.5rem] lg:text-[3.8rem] text-[#36322F] dark:text-white font-semibold tracking-tight leading-[1.1] opacity-0 animate-fade-up [animation-duration:500ms] [animation-delay:200ms] [animation-fill-mode:forwards]">
            <span className="relative px-1 text-transparent bg-clip-text bg-gradient-to-tr from-red-600 to-yellow-500 inline-flex justify-center items-center">
              Open Researcher
            </span>
          </h1>
          <p className="mt-6 text-lg text-zinc-600 dark:text-zinc-400 opacity-0 animate-fade-up [animation-duration:500ms] [animation-delay:600ms] [animation-fill-mode:forwards]">
            Firecrawl-powered search, scrape, and agentic reasoning
          </p>
        </div>
      </div>

      {/* Main Content - Full width split layout */}
      <div className="flex-1 px-4 sm:px-6 lg:px-8">
        <div className="h-full max-w-[1400px] mx-auto">
          <ThinkingChat
            onMessagesChange={setHasMessages}
            hasFirecrawlKey={hasFirecrawlKey}
            onApiKeyRequired={() => setShowApiKeyModal(true)}
          />
        </div>
      </div>

      {/* Footer */}
      <footer className="px-4 sm:px-6 lg:px-8 py-8 mt-auto">
        <div className="max-w-4xl mx-auto text-center">
          <p className="text-sm text-gray-600 dark:text-gray-400">
            Powered by{' '}
            <Link
              href="https://firecrawl.dev"
              className="text-orange-600 hover:text-orange-700 dark:text-orange-400 dark:hover:text-orange-300 font-medium"
              target="_blank"
              rel="noopener noreferrer"
            >
              Firecrawl
            </Link>
          </p>
        </div>
      </footer>

      {/* API Key Modal */}
      <Dialog open={showApiKeyModal} onOpenChange={setShowApiKeyModal}>
        <DialogContent className="sm:max-w-md bg-white dark:bg-zinc-900">
          <DialogHeader>
            <DialogTitle>Firecrawl API Key Required</DialogTitle>
            <DialogDescription>
              This tool requires a Firecrawl API key to search and analyze web content.
            </DialogDescription>
          </DialogHeader>
          <div className="flex flex-col gap-4 py-4">
            <Button
              onClick={() => window.open('https://www.firecrawl.dev', '_blank')}
              variant="code"
              className="flex items-center justify-center gap-2"
            >
              <ExternalLink className="h-4 w-4" />
              Get Firecrawl API Key
            </Button>
            <div className="flex flex-col gap-2">
              <label htmlFor="firecrawl-key" className="text-sm font-medium">
                Firecrawl API Key
              </label>
              <Input
                id="firecrawl-key"
                type="password"
                placeholder="fc-..."
                value={firecrawlApiKey}
                onChange={(e) => setFirecrawlApiKey(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === 'Enter' && !isValidatingApiKey) {
                    handleApiKeySubmit()
                  }
                }}
                disabled={isValidatingApiKey}
              />
            </div>
          </div>
          <DialogFooter>
            <Button
              onClick={handleApiKeySubmit}
              disabled={isValidatingApiKey || !firecrawlApiKey.trim()}
              variant="orange"
              className="w-full"
            >
              {isValidatingApiKey ? (
                <>
                  <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                  Validating...
                </>
              ) : (
                'Submit'
              )}
            </Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>
    </div>
  )
}
```

## File: `app/open-researcher/page.tsx`
```tsx
import { Metadata } from 'next'
import OpenResearcherContent from './open-researcher-content'

export const metadata: Metadata = {
  title: 'Open Researcher',
  description: 'Firecrawl-powered search, scrape, and agentic reasoning',
}

export default function OpenResearcherPage() {
  return <OpenResearcherContent />
}
```

## File: `components/animated-cursor.tsx`
```tsx
'use client'

import { useEffect, useState } from 'react'
import { cn } from '@/lib/utils'

interface AnimatedCursorProps {
  targetX: number
  targetY: number
  containerRef: React.RefObject<HTMLElement>
  onComplete?: () => void
  delay?: number
}

export function AnimatedCursor({ targetX, targetY, containerRef, onComplete, delay = 0 }: AnimatedCursorProps) {
  const [position, setPosition] = useState({ x: 0, y: 0 })
  const [isVisible, setIsVisible] = useState(false)
  const [isClicking, setIsClicking] = useState(false)

  useEffect(() => {
    if (!containerRef.current) return

    const calculatePosition = () => {
      const containerRect = containerRef.current!.getBoundingClientRect()
      // Start from center of the container
      const startX = containerRect.width / 2
      const startY = containerRect.height / 2

      setPosition({ x: startX, y: startY })
      setIsVisible(true)
      
      // Start animation after a brief pause
      setTimeout(() => {
        // Recalculate container position in case it moved
        const updatedContainerRect = containerRef.current!.getBoundingClientRect()
        // Move to target position relative to container
        const finalX = targetX - updatedContainerRect.left
        const finalY = targetY - updatedContainerRect.top
        setPosition({ x: finalX, y: finalY })
        
        // Trigger click animation when cursor reaches target
        setTimeout(() => {
          setIsClicking(true)
          
          // Call onComplete after click animation
          setTimeout(() => {
            onComplete?.()
          }, 300)
        }, 1500) // Duration of cursor movement
      }, 100)
    }

    const timer = setTimeout(calculatePosition, delay)

    return () => clearTimeout(timer)
  }, [targetX, targetY, containerRef, onComplete, delay])

  if (!isVisible) return null

  return (
    <div
      className={cn(
        "absolute z-50 pointer-events-none transition-all duration-[1500ms] ease-out",
        isClicking && "scale-75"
      )}
      style={{
        left: position.x,
        top: position.y,
        transform: 'translate(-2px, -2px)' // Slight offset for cursor tip
      }}
    >
      {/* Large Orange Cursor */}
      <svg
        width="48"
        height="48"
        viewBox="0 0 24 24"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        className={cn(
          "transition-transform duration-300 drop-shadow-lg",
          isClicking && "scale-90"
        )}
      >
        <path
          d="M3 3L21 11.5L12.5 12.5L11.5 21L3 3Z"
          fill="#fb923c"
          stroke="white"
          strokeWidth="1.5"
        />
      </svg>
      
      {/* Click ripple effect */}
      {isClicking && (
        <div className="absolute inset-0 flex items-center justify-center">
          <div className="w-16 h-16 rounded-full border-2 border-orange-400 animate-ping" />
        </div>
      )}
    </div>
  )
}
```

## File: `components/citation-tooltip.tsx`
```tsx
'use client';

import { useState, useRef, useEffect } from 'react';
import Image from 'next/image';

interface Source {
  url: string;
  title: string;
  description?: string;
}

interface CitationTooltipProps {
  sources: Source[];
}

// Helper to get favicon URL
function getFaviconUrl(url: string): string {
  try {
    const domain = new URL(url).hostname;
    return `https://www.google.com/s2/favicons?domain=${domain}&sz=32`;
  } catch {
    return '/favicon.ico';
  }
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
              img.src = 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none"%3E%3Crect width="20" height="20" rx="4" fill="%23E5E7EB"/%3E%3C/svg%3E';
            }}
          />
          <div className="min-w-0">
            <p className="font-medium text-sm text-gray-900 dark:text-gray-100 break-words">
              {tooltip.source.title}
            </p>
            <p className="text-xs text-gray-500 dark:text-gray-400 mt-1 break-all">
              {displayUrl}
            </p>
            {tooltip.source.description && (
              <p className="text-xs text-gray-600 dark:text-gray-300 mt-2 line-clamp-2">
                {tooltip.source.description}
              </p>
            )}
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

## File: `components/markdown-renderer.tsx`
```tsx
'use client';

import { memo } from 'react';
import { CitationTooltip } from '@/components/citation-tooltip';

interface MarkdownRendererProps {
  content: string;
  streaming?: boolean;
  sources?: Array<{ url: string; title: string; description?: string }>;
}

export const MarkdownRenderer = memo(function MarkdownRenderer({ 
  content, 
  streaming = false,
  sources = [] 
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
    
    // Headers
    parsed = parsed.replace(/^### (.+)$/gm, '<h3 class="text-base font-semibold mt-4 mb-2">$1</h3>');
    parsed = parsed.replace(/^## (.+)$/gm, '<h2 class="text-lg font-semibold mt-5 mb-2">$1</h2>');
    parsed = parsed.replace(/^# (.+)$/gm, '<h1 class="text-xl font-bold mt-6 mb-3">$1</h1>');
    
    // Handle list blocks
    const listBlocks = parsed.split('\n');
    let inList = false;
    const processedLines = [];
    
    for (let i = 0; i < listBlocks.length; i++) {
      const line = listBlocks[i];
      const isListItem = line.match(/^- (.+)$/) || line.match(/^(\d+)\. (.+)$/);
      
      if (isListItem && !inList) {
        processedLines.push('<ul class="space-y-1 my-3">');
        inList = true;
      } else if (!isListItem && inList) {
        processedLines.push('</ul>');
        inList = false;
      }
      
      if (line.match(/^- (.+)$/)) {
        processedLines.push(line.replace(/^- (.+)$/, '<li class="ml-5 list-disc">$1</li>'));
      } else if (line.match(/^(\d+)\. (.+)$/)) {
        processedLines.push(line.replace(/^(\d+)\. (.+)$/, '<li class="ml-5 list-decimal">$2</li>'));
      } else {
        processedLines.push(line);
      }
    }
    
    if (inList) {
      processedLines.push('</ul>');
    }
    
    parsed = processedLines.join('\n');
    
    // Code blocks
    parsed = parsed.replace(/```([\s\S]*?)```/g, '<pre class="bg-gray-100 dark:bg-gray-800 p-3 rounded-lg overflow-x-auto my-3"><code>$1</code></pre>');
    
    // Inline code
    parsed = parsed.replace(/`(.+?)`/g, '<code class="bg-gray-100 dark:bg-gray-800 px-1.5 py-0.5 rounded text-sm font-mono">$1</code>');
    
    // Handle tables
    const lines = parsed.split('\n');
    const tableProcessed = [];
    let inTable = false;
    let tableContent = [];
    
    for (let i = 0; i < lines.length; i++) {
      const line = lines[i].trim();
      
      // Check if this line is part of a table
      if (line.includes('|') && !line.startsWith('<')) {
        if (!inTable) {
          inTable = true;
          tableContent = [];
        }
        tableContent.push(line);
      } else {
        // End of table
        if (inTable && tableContent.length > 0) {
          // Process the table
          const tableHtml = processTable(tableContent);
          tableProcessed.push(tableHtml);
          inTable = false;
          tableContent = [];
        }
        tableProcessed.push(lines[i]);
      }
    }
    
    // Handle any remaining table content
    if (inTable && tableContent.length > 0) {
      const tableHtml = processTable(tableContent);
      tableProcessed.push(tableHtml);
    }
    
    parsed = tableProcessed.join('\n');
    
    // Paragraphs
    parsed = parsed.split('\n\n').map(para => {
      if (para.trim() && !para.includes('<h') && !para.includes('<ul') && !para.includes('<pre') && !para.includes('<table')) {
        return `<p class="mb-3">${para}</p>`;
      }
      return para;
    }).join('\n');
    
    // Clean up
    parsed = parsed.replace(/<p class="mb-3"><\/p>/g, '');
    parsed = parsed.replace(/\n/g, ' ');
    
    return parsed;
  };

  // Helper function to process table content
  const processTable = (tableLines: string[]) => {
    if (tableLines.length < 2) return tableLines.join('\n');
    
    let html = '<div class="overflow-x-auto my-4"><table class="w-full divide-y divide-gray-200 dark:divide-gray-700">';
    let isHeader = true;
    
    for (let i = 0; i < tableLines.length; i++) {
      const line = tableLines[i];
      
      // Skip separator lines (|---|---|)
      if (line.match(/^\|?\s*[-:]+\s*\|/)) {
        continue;
      }
      
      // Process cells
      const cells = line.split('|').map(cell => cell.trim()).filter(cell => cell !== '');
      
      if (cells.length > 0) {
        if (isHeader) {
          html += '<thead class="bg-gray-50 dark:bg-gray-800">';
          html += '<tr>';
          cells.forEach(cell => {
            html += `<th class="px-4 py-2 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">${cell}</th>`;
          });
          html += '</tr>';
          html += '</thead>';
          html += '<tbody class="bg-white dark:bg-gray-900 divide-y divide-gray-200 dark:divide-gray-700">';
          isHeader = false;
        } else {
          html += '<tr>';
          cells.forEach(cell => {
            html += `<td class="px-4 py-2 text-sm text-gray-900 dark:text-gray-300">${cell}</td>`;
          });
          html += '</tr>';
        }
      }
    }
    
    html += '</tbody>';
    html += '</table></div>';
    
    return html;
  };

  return (
    <div className="text-sm text-gray-700 dark:text-gray-300">
      <div 
        dangerouslySetInnerHTML={{ __html: parseMarkdown(content) }} 
        className="markdown-content leading-relaxed [&>h1]:text-gray-900 [&>h1]:dark:text-gray-100 [&>h2]:text-gray-900 [&>h2]:dark:text-gray-100 [&>h3]:text-gray-900 [&>h3]:dark:text-gray-100"
      />
      {streaming && <span className="animate-pulse text-orange-500">▊</span>}
      {sources.length > 0 && <CitationTooltip sources={sources} />}
    </div>
  );
});
```

## File: `components/screenshot-preview.tsx`
```tsx
'use client'

import { useState, useEffect } from 'react'
import Image from 'next/image'
import { cn } from '@/lib/utils'
import { 
  Dialog,
  DialogContent,
  DialogTitle,
} from '@/components/ui/dialog'
import { Loader2, Expand, X } from 'lucide-react'

interface ScreenshotPreviewProps {
  url: string
  screenshot: string
  isLoading?: boolean
  className?: string
}

export function ScreenshotPreview({ url, screenshot, isLoading = false, className }: ScreenshotPreviewProps) {
  const [showModal, setShowModal] = useState(false)
  const [imageLoaded, setImageLoaded] = useState(false)
  const [scanProgress, setScanProgress] = useState(0)

  // Preload image before showing
  useEffect(() => {
    if (screenshot && typeof window !== 'undefined') {
      const img = document.createElement('img')
      img.onload = () => {
        // Small delay to ensure smooth animation
        setTimeout(() => setImageLoaded(true), 100)
      }
      img.onerror = () => {
        // Failed to preload screenshot
        setImageLoaded(true)
      }
      img.src = screenshot
    }
  }, [screenshot, url])

  // Animate scan progress when loading
  useEffect(() => {
    if (isLoading && scanProgress < 100) {
      const timer = setTimeout(() => {
        setScanProgress(prev => Math.min(prev + 5, 100))
      }, 100)
      return () => clearTimeout(timer)
    }
  }, [isLoading, scanProgress])

  // Reset scan progress when loading changes
  useEffect(() => {
    if (isLoading) {
      setScanProgress(0)
    }
  }, [isLoading])

  return (
    <>
      <div 
        className={cn(
          "relative group cursor-pointer overflow-hidden rounded-lg border border-gray-200 dark:border-gray-700 bg-gray-100 dark:bg-gray-800",
          "transition-all duration-300 hover:shadow-lg hover:scale-[1.02]",
          className
        )}
        onClick={() => setShowModal(true)}
      >
        {/* Screenshot thumbnail */}
        <div className="relative aspect-video">
          {screenshot && (
            <Image
              src={screenshot}
              alt={`Screenshot of ${url}`}
              fill
              className={cn(
                "object-cover transition-opacity duration-500",
                imageLoaded ? "opacity-100" : "opacity-0"
              )}
              onLoad={() => {}}
              onError={() => { /* Failed to load screenshot */ }}
              sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
            />
          )}
          
          {/* Loading state with scanning animation */}
          {(!imageLoaded || !screenshot) && (
            <div className="absolute inset-0 flex items-center justify-center bg-gray-100 dark:bg-gray-800">
              <Loader2 className="h-6 w-6 animate-spin text-orange-500" />
            </div>
          )}

          {/* Scanning overlay animation - only show after image is loaded */}
          {isLoading && imageLoaded && screenshot && (
            <>
              {/* Scan line effect */}
              <div 
                className="absolute left-0 right-0 h-1 bg-gradient-to-b from-transparent via-orange-500 to-transparent opacity-80 animate-scan"
                style={{
                  top: `${scanProgress}%`,
                  boxShadow: '0 0 20px 5px rgba(251, 146, 60, 0.5)'
                }}
              />
              
              {/* Grid overlay */}
              <div className="absolute inset-0 bg-[url('/grid-pattern.svg')] bg-repeat opacity-20 animate-pulse" />
              
              {/* Corner indicators */}
              <div className="absolute top-2 left-2 w-6 h-6 border-t-2 border-l-2 border-orange-500 animate-pulse" />
              <div className="absolute top-2 right-2 w-6 h-6 border-t-2 border-r-2 border-orange-500 animate-pulse" />
              <div className="absolute bottom-2 left-2 w-6 h-6 border-b-2 border-l-2 border-orange-500 animate-pulse" />
              <div className="absolute bottom-2 right-2 w-6 h-6 border-b-2 border-r-2 border-orange-500 animate-pulse" />
            </>
          )}

          {/* Hover overlay */}
          <div className="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-colors duration-300 flex items-center justify-center">
            <Expand className="h-8 w-8 text-white opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
          </div>
        </div>

        {/* URL label */}
        <div className="p-2 bg-white dark:bg-gray-900 border-t border-gray-200 dark:border-gray-700">
          <p className="text-xs text-gray-600 dark:text-gray-400 truncate">
            {new URL(url).hostname}
          </p>
        </div>
      </div>

      {/* Full-size modal */}
      <Dialog open={showModal} onOpenChange={setShowModal}>
        <DialogContent className="max-w-4xl max-h-[90vh] p-0 overflow-hidden">
          <DialogTitle className="sr-only">Screenshot of {url}</DialogTitle>
          
          {/* Modal header */}
          <div className="flex items-center justify-between p-4 border-b border-gray-200 dark:border-gray-700">
            <div className="flex-1 mr-4">
              <p className="text-sm font-medium text-gray-900 dark:text-white truncate">
                {url}
              </p>
            </div>
            <button
              onClick={() => setShowModal(false)}
              className="p-1 rounded-md hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
            >
              <X className="h-5 w-5 text-gray-500" />
            </button>
          </div>

          {/* Modal body with full screenshot */}
          <div className="relative w-full h-full overflow-auto bg-gray-50 dark:bg-gray-900">
            {screenshot && (
              <div className="relative min-h-[500px]">
                <Image
                  src={screenshot}
                  alt={`Screenshot of ${url}`}
                  width={1200}
                  height={800}
                  className="w-full h-auto"
                  priority
                />
                
                {/* Scanning animation in modal */}
                {isLoading && (
                  <div className="absolute inset-0 pointer-events-none">
                    {/* Animated scan grid */}
                    <div className="absolute inset-0 bg-gradient-to-b from-orange-500/10 via-transparent to-orange-500/10 animate-scan-vertical" />
                    <div className="absolute inset-0 bg-gradient-to-r from-orange-500/10 via-transparent to-orange-500/10 animate-scan-horizontal" />
                    
                    {/* Analyzing text */}
                    <div className="absolute top-4 left-4 bg-black/80 text-white px-3 py-1 rounded-md text-sm font-mono">
                      <span className="animate-pulse">Analyzing page content...</span>
                    </div>
                  </div>
                )}
              </div>
            )}
          </div>
        </DialogContent>
      </Dialog>
    </>
  )
}
```

## File: `components/search-results-display.tsx`
```tsx
'use client'

import { useState, useEffect, useRef } from 'react'
import { Globe, Search, FileText, Image } from 'lucide-react'
import { cn } from '@/lib/utils'
import { AnimatedCursor } from './animated-cursor'

interface SearchResult {
  title: string
  url: string
  description?: string
  markdown?: string
  screenshot?: string
  dateFound?: string
}

interface SearchHistory {
  query: string
  results: SearchResult[]
  screenshots: Array<{ url: string; screenshot?: string }>
  timestamp: number
}

interface SearchResultsDisplayProps {
  query?: string
  results?: SearchResult[]
  isActive?: boolean
  currentUrl?: string
  screenshots?: Array<{ url: string; screenshot?: string }>
  onClose?: () => void
}

export function SearchResultsDisplay({ 
  query = '', 
  results = [], 
  isActive = false,
  currentUrl = '',
  screenshots = [],
  onClose
}: SearchResultsDisplayProps) {
  const [showScreenshot, setShowScreenshot] = useState(false)
  const [currentScreenshot, setCurrentScreenshot] = useState<string | null>(null)
  const [activeResultIndex, setActiveResultIndex] = useState(-1)
  const [viewMode, setViewMode] = useState<'search' | 'screenshots' | 'history'>('search')
  const [selectedScreenshotIndex, setSelectedScreenshotIndex] = useState(0)
  const [isImageTall, setIsImageTall] = useState(false)
  const [isImageLoaded, setIsImageLoaded] = useState(false)
  const [searchHistory, setSearchHistory] = useState<SearchHistory[]>([])
  const [showClosingAnimation, setShowClosingAnimation] = useState(false)
  const [browserClosed, setBrowserClosed] = useState(false)
  const closeButtonRef = useRef<HTMLDivElement>(null)
  const browserContainerRef = useRef<HTMLDivElement>(null)
  const screenshotRef = useRef<HTMLImageElement>(null)
  
  // Save search history when search completes
  useEffect(() => {
    if (!isActive && query && results.length > 0) {
      // Check if this search is already in history (avoid duplicates)
      const existingIndex = searchHistory.findIndex(h => h.query === query)
      if (existingIndex === -1) {
        const newHistory: SearchHistory = {
          query,
          results: [...results],
          screenshots: [...screenshots],
          timestamp: Date.now()
        }
        setSearchHistory(prev => [...prev, newHistory])
      }
      
      // Trigger closing animation after search completes
      setTimeout(() => {
        setShowClosingAnimation(true)
      }, 2000) // Wait 2 seconds after search completes
    }
  }, [isActive, query, results.length, screenshots.length])
  
  // Switch to history view when search completes and we have history
  useEffect(() => {
    if (!isActive && searchHistory.length > 0) {
      setViewMode('history')
    }
  }, [isActive, searchHistory.length])

  // Show screenshot only when actively scraping a specific URL
  useEffect(() => {
    if (isActive && currentUrl && currentUrl !== '' && screenshots.length > 0) {
      // Always use the latest screenshot when scraping
      // This handles cases where the same URL is scraped multiple times
      const latestScreenshot = screenshots[screenshots.length - 1]
      
      // Check if this is the URL being scraped or if it's the latest screenshot
      const currentScreenshotData = screenshots.find(s => s.url === currentUrl) || latestScreenshot
      
      if (currentScreenshotData?.screenshot) {
        // Small delay to ensure smooth transition
        setTimeout(() => {
          // Reset loading state when changing screenshots
          setIsImageLoaded(false)
          setIsImageTall(false)
          // Show the screenshot for the page being scraped
          setCurrentScreenshot(currentScreenshotData.screenshot || null)
          setShowScreenshot(true)
        }, 150)
      } else {
        // No screenshot for current URL, show search results
        setShowScreenshot(false)
      }
    } else {
      // Not scraping a specific URL, show search results
      setShowScreenshot(false)
      setCurrentScreenshot(null)
      setIsImageLoaded(false)
      setIsImageTall(false)
    }
  }, [currentUrl, screenshots, isActive])

  // Highlight results as they're being scraped
  useEffect(() => {
    if (currentUrl && results.length > 0) {
      const index = results.findIndex(r => r.url === currentUrl)
      setActiveResultIndex(index)
    } else {
      setActiveResultIndex(-1)
    }
  }, [currentUrl, results])

  const getUrlBarContent = () => {
    // Prioritize showing scraping URL when actively scraping
    if (currentUrl && isActive) {
      return {
        icon: <FileText className="h-4 w-4" />,
        text: currentUrl,
        action: 'scraping'
      }
    }
    // Show search query when we have results or are searching
    if (query && (results.length > 0 || isActive)) {
      return {
        icon: <Search className="h-4 w-4" />,
        text: `Searching: ${query}`,
        action: 'searching'
      }
    }
    // Default to search if we have a query
    if (query) {
      return {
        icon: <Search className="h-4 w-4" />,
        text: `Searching: ${query}`,
        action: isActive ? 'searching' : 'idle'
      }
    }
    return {
      icon: <Globe className="h-4 w-4" />,
      text: '',
      action: 'idle'
    }
  }

  const urlBar = getUrlBarContent()

  return (
    <div 
      ref={browserContainerRef}
      className={cn(
        "h-full flex flex-col bg-white dark:bg-gray-900 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 shadow-lg transition-all duration-500 relative",
        browserClosed && "opacity-0 scale-95 translate-x-full"
      )}
    >
      {/* Animated cursor - positioned inside the browser container */}
      {showClosingAnimation && closeButtonRef.current && browserContainerRef.current && (
        <AnimatedCursor
          targetX={closeButtonRef.current.getBoundingClientRect().left + closeButtonRef.current.offsetWidth / 2}
          targetY={closeButtonRef.current.getBoundingClientRect().top + closeButtonRef.current.offsetHeight / 2}
          containerRef={browserContainerRef as React.RefObject<HTMLElement>}
          onComplete={() => {
            setBrowserClosed(true)
            setTimeout(() => {
              onClose?.()
            }, 500) // Wait for browser close animation
          }}
          delay={500}
        />
      )}
      
      {/* Fake browser URL bar */}
      <div className="bg-gray-100 dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700 px-4 py-2 flex-shrink-0">
        <div className="flex items-center gap-2">
          <div className="flex items-center gap-1">
            <div 
              ref={closeButtonRef} 
              className={cn(
                "w-3 h-3 rounded-full bg-red-500 hover:bg-red-600 cursor-pointer transition-all duration-300",
                showClosingAnimation && "animate-button-press"
              )}
            />
            <div className="w-3 h-3 rounded-full bg-yellow-500" />
            <div className="w-3 h-3 rounded-full bg-green-500" />
          </div>
          <div className="flex-1 flex items-center gap-2 bg-white dark:bg-gray-700 rounded-md px-3 py-1 min-w-0">
            {urlBar.icon}
            <span className="text-sm text-gray-600 dark:text-gray-300 font-mono truncate flex-1 min-w-0">
              {urlBar.text}
            </span>
            {urlBar.action === 'searching' && (
              <div className="flex items-center gap-1 flex-shrink-0 ml-2">
                <div className="w-2 h-2 bg-blue-500 rounded-full animate-pulse" />
                <span className="text-xs text-blue-500 whitespace-nowrap">Searching...</span>
              </div>
            )}
            {urlBar.action === 'scraping' && (
              <div className="flex items-center gap-1 flex-shrink-0 ml-2">
                <div className="w-2 h-2 bg-orange-500 rounded-full animate-pulse" />
                <span className="text-xs text-orange-500 whitespace-nowrap">Scraping...</span>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Search results display */}
      <div className="flex-1 overflow-hidden relative">
        {(viewMode === 'search' && showScreenshot && currentScreenshot) ? (
          <div className="absolute inset-0 flex">
            <div className="relative flex-1 bg-white dark:bg-gray-900 flex items-center justify-center overflow-hidden">
              {/* Loading state for image */}
              {!isImageLoaded && (
                <div className="absolute inset-0 flex items-center justify-center bg-white dark:bg-gray-900 z-10">
                  <div className="text-center">
                    <div className="w-16 h-16 border-4 border-orange-500 border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
                    <p className="text-gray-600 dark:text-gray-400">Loading page...</p>
                  </div>
                </div>
              )}
              
              {/* Scrolling container for long screenshots */}
              <div className="absolute inset-0 overflow-hidden">
                <div className={cn(
                  "screenshot-scroll-container transition-opacity duration-500",
                  isImageTall && isImageLoaded && "animate-screenshot-scroll",
                  isImageLoaded ? "opacity-100" : "opacity-0"
                )}>
                  <img 
                    ref={screenshotRef}
                    src={currentScreenshot} 
                    alt="Screenshot" 
                    className={cn(
                      "w-full",
                      isImageTall ? "object-cover object-top" : "object-contain h-full"
                    )}
                    onLoad={(e) => {
                      const img = e.target as HTMLImageElement;
                      const containerHeight = img.parentElement?.parentElement?.clientHeight || 0;
                      const imageHeight = img.naturalHeight * (img.clientWidth / img.naturalWidth);
                      setIsImageTall(imageHeight > containerHeight * 1.5); // Image is tall if it's 1.5x the container height
                      
                      // Add a small delay to ensure smooth transition
                      setTimeout(() => {
                        setIsImageLoaded(true);
                      }, 100);
                    }}
                  />
                </div>
                {/* Fade gradients for smooth scrolling effect */}
                {isImageTall && isImageLoaded && (
                  <>
                    <div className="absolute top-0 left-0 right-0 h-16 bg-gradient-to-b from-white dark:from-gray-900 to-transparent pointer-events-none" />
                    <div className="absolute bottom-0 left-0 right-0 h-16 bg-gradient-to-t from-white dark:from-gray-900 to-transparent pointer-events-none" />
                  </>
                )}
              </div>
              {/* Scanner effect overlay - only show when image is loaded */}
              {isImageLoaded && (
                <div className="absolute inset-0 pointer-events-none animate-fade-in">
                  <div className="scanner-line" />
                  {/* Grid overlay effect */}
                  <div className="absolute inset-0" style={{
                  backgroundImage: `repeating-linear-gradient(
                    0deg,
                    transparent,
                    transparent 40px,
                    rgba(251, 146, 60, 0.03) 40px,
                    rgba(251, 146, 60, 0.03) 41px
                  ),
                  repeating-linear-gradient(
                    90deg,
                    transparent,
                    transparent 40px,
                    rgba(251, 146, 60, 0.03) 40px,
                    rgba(251, 146, 60, 0.03) 41px
                  )`
                }} />
                </div>
              )}
              {isImageLoaded && (
                <div className="absolute bottom-6 right-6 bg-white border-2 border-orange-500 text-orange-600 px-5 py-3 rounded-lg shadow-lg flex items-center gap-3 animate-fade-up">
                  <div className="flex gap-1">
                    <div className="w-2 h-2 bg-orange-500 rounded-full animate-pulse" />
                    <div className="w-2 h-2 bg-orange-500 rounded-full animate-pulse" style={{ animationDelay: '0.2s' }} />
                    <div className="w-2 h-2 bg-orange-500 rounded-full animate-pulse" style={{ animationDelay: '0.4s' }} />
                  </div>
                  <span className="text-sm font-bold">Scanning page content</span>
                </div>
              )}
            </div>
          </div>
        ) : viewMode === 'search' && !showScreenshot ? (
          <div className="h-full bg-white dark:bg-gray-900 flex flex-col">
            {/* Google-style search header - always show when we have results */}
            {(query || results.length > 0) && (
              <div className="border-b border-gray-200 dark:border-gray-700 px-3 lg:px-6 py-2 lg:py-3 bg-white dark:bg-gray-900">
                <div className="flex items-center gap-3 lg:gap-8">
                  {/* Firecrawl logo */}
                  <img 
                    src="/firecrawl-logo-with-fire.png" 
                    alt="Firecrawl" 
                    className="h-6 lg:h-8 w-auto flex-shrink-0"
                  />
                  
                  {/* Search box */}
                  <div className="flex-1 max-w-[400px]">
                    <div className="flex items-center bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-600 rounded-full px-3 lg:px-5 py-2 lg:py-2.5 shadow-sm hover:shadow-md transition-shadow">
                      <span className="text-gray-700 dark:text-gray-300 flex-1 text-sm font-normal truncate">
                        <span className="lg:hidden">{query ? (query.length > 30 ? query.substring(0, 30) + '...' : query) : 'Search...'}</span>
                        <span className="hidden lg:inline">{query || 'Search...'}</span>
                      </span>
                      <div className="ml-2 lg:ml-3 p-1 flex-shrink-0">
                        <Search className="h-4 w-4 lg:h-5 lg:w-5 text-blue-600" />
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            )}
            
            {/* Search results in Google style */}
            <div className="flex-1 overflow-y-auto px-6">
              <div className="max-w-[500px] py-4">
                {/* Results count */}
                {query && results.length > 0 && !isActive && (
                  <div className="mb-3 text-sm text-gray-600 dark:text-gray-400">
                    About {results.length} results
                  </div>
                )}

                {/* Search results */}
                <div className="space-y-6">
                {results.map((result, index) => {
                  const hostname = new URL(result.url).hostname
                  const urlPath = result.url.split('/').slice(3).filter(Boolean).join(' › ')
                  
                  return (
                    <div key={index} className="group">
                      {/* Site info - simple text without logo */}
                      <div className="text-sm text-gray-600 dark:text-gray-400 mb-1">
                        <cite className="not-italic">
                          {hostname}
                          {urlPath && <span> › {urlPath}</span>}
                        </cite>
                      </div>

                      {/* Title */}
                      <h3 className="mb-1">
                        <a 
                          href={result.url} 
                          target="_blank" 
                          rel="noopener noreferrer"
                          className="text-xl text-blue-700 dark:text-blue-400 hover:underline visited:text-purple-700 dark:visited:text-purple-400"
                        >
                          {result.title}
                        </a>
                      </h3>

                      {/* Date and description */}
                      <div className="text-sm text-gray-600 dark:text-gray-300 leading-relaxed">
                        {result.dateFound && (
                          <span className="text-gray-500 dark:text-gray-400">{result.dateFound} — </span>
                        )}
                        <span>{result.description}</span>
                      </div>

                      {/* Scraping indicator */}
                      {activeResultIndex === index && (
                        <div className="mt-2 inline-flex items-center gap-2 text-sm text-green-600 dark:text-green-400 border-2 border-dashed border-green-500 rounded px-3 py-1 animate-selection-pulse-green">
                          <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse" />
                          <span>Analyzing this page...</span>
                        </div>
                      )}
                    </div>
                  )
                })}

                {/* No results message */}
                {results.length === 0 && query && !isActive && (
                  <div className="py-8">
                    <p className="text-base text-gray-700 dark:text-gray-300">
                      Your search - <span className="font-medium">{query}</span> - did not match any documents.
                    </p>
                    <div className="mt-4 text-sm text-gray-600 dark:text-gray-400">
                      <p className="font-medium mb-2">Suggestions:</p>
                      <ul className="list-disc list-inside space-y-1">
                        <li>Make sure all words are spelled correctly.</li>
                        <li>Try different keywords.</li>
                        <li>Try more general keywords.</li>
                      </ul>
                    </div>
                  </div>
                )}

                {/* Loading state - removed to go directly to search results */}
                </div>
              </div>
            </div>
          </div>
        ) : viewMode === 'screenshots' && !isActive ? (
          <div className="h-full overflow-hidden flex flex-col">
            {/* Screenshot viewer */}
            <div className="flex-1 bg-white dark:bg-gray-900 overflow-hidden">
              {screenshots.length > 0 && screenshots[selectedScreenshotIndex]?.screenshot ? (
                <img 
                  src={screenshots[selectedScreenshotIndex].screenshot} 
                  alt={`Screenshot from ${screenshots[selectedScreenshotIndex].url}`}
                  className="w-full h-full object-contain"
                />
              ) : (
                <div className="text-gray-500 dark:text-gray-400">
                  <Image className="h-12 w-12 mx-auto mb-4 opacity-50" />
                  <p>No screenshots available</p>
                </div>
              )}
            </div>
            
            {/* Screenshot thumbnails */}
            {screenshots.length > 0 && (
              <div className="border-t border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800 p-4">
                <div className="flex gap-2 overflow-x-auto">
                  {screenshots.map((screenshot, index) => (
                    <button
                      key={index}
                      onClick={() => setSelectedScreenshotIndex(index)}
                      className={cn(
                        "flex-shrink-0 relative rounded-lg overflow-hidden transition-all",
                        selectedScreenshotIndex === index
                          ? "ring-2 ring-orange-500 dark:ring-orange-400"
                          : "opacity-70 hover:opacity-100"
                      )}
                    >
                      <img 
                        src={screenshot.screenshot || ''} 
                        alt={`Thumbnail ${index + 1}`}
                        className="w-24 h-16 object-contain bg-gray-100 dark:bg-gray-800"
                      />
                      <div className="absolute bottom-0 left-0 right-0 bg-black/60 text-white text-xs px-1 py-0.5 truncate">
                        {new URL(screenshot.url).hostname}
                      </div>
                    </button>
                  ))}
                </div>
              </div>
            )}
          </div>
        ) : null}
      </div>
    </div>
  )
}
```

## File: `components/thinking-chat.tsx`
```tsx
'use client'

import { useState, useRef, useEffect } from 'react'
import { ChevronDown, Loader2, Send, Copy } from 'lucide-react'
import { SearchResultsDisplay } from '@/components/search-results-display'
import { MarkdownRenderer } from '@/components/markdown-renderer'
import { CitationTooltip } from '@/components/citation-tooltip'
import { cn } from '@/lib/utils'

// Import the ThinkingEvent type from thinking-display
import type { ThinkingEvent } from '@/components/thinking-display'

interface Message {
  id: string
  role: 'user' | 'assistant'
  content: string
  searchData?: {
    status: 'searching' | 'complete' | 'error'
    events: ThinkingEvent[]
  }
  sources?: Array<{ url: string; title: string; description?: string }>
}

const SUGGESTED_QUERIES = [
  "What are the latest AI breakthroughs in 2025 and how do they compare to previous years?",
  "Find me the 2nd sentence of the 3rd and 5th blog post on firecrawl.dev and analyze their content",
  "Compare the latest features and pricing between Samsung Galaxy S24 Ultra and iPhone 15 Pro Max, including camera specs and AI capabilities"
]

interface ThinkingChatProps {
  onMessagesChange?: (hasMessages: boolean) => void
  hasFirecrawlKey?: boolean
  onApiKeyRequired?: () => void
  onBrowserClose?: () => void
}

export function ThinkingChat({ onMessagesChange, hasFirecrawlKey = false, onApiKeyRequired }: ThinkingChatProps) {
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState('')
  const [isSearching, setIsSearching] = useState(false)
  const [showSuggestions, setShowSuggestions] = useState(false)
  const [isTransitioning, setIsTransitioning] = useState(false)
  const [searchResults, setSearchResults] = useState<Array<{ url: string; title: string; description?: string }>>([])
  const [currentQuery, setCurrentQuery] = useState('')
  const [currentScrapingUrl, setCurrentScrapingUrl] = useState('')
  const [screenshots, setScreenshots] = useState<Array<{ url: string; screenshot?: string }>>([])
  const [showFullWidth, setShowFullWidth] = useState(false)
  const [hasAnimatedSuggestions, setHasAnimatedSuggestions] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)
  const inputRef = useRef<HTMLInputElement>(null)

  // Auto-scroll to bottom when new messages are added
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  // Notify parent when messages change
  useEffect(() => {
    onMessagesChange?.(messages.length > 0)
  }, [messages.length, onMessagesChange])

  // Mark suggestions as animated after first show
  useEffect(() => {
    if (showSuggestions && !hasAnimatedSuggestions) {
      // Set after animations complete
      const timer = setTimeout(() => {
        setHasAnimatedSuggestions(true)
      }, 1000)
      return () => clearTimeout(timer)
    }
  }, [showSuggestions, hasAnimatedSuggestions])

  const handleSearch = async (query: string) => {
    if (!query.trim() || isSearching) return

    // Check if Firecrawl API key is available
    if (!hasFirecrawlKey && !localStorage.getItem('firecrawl_api_key')) {
      onApiKeyRequired?.()
      return
    }

    // Start transition animation
    setIsTransitioning(true)
    
    // Wait for fade animation
    await new Promise(resolve => setTimeout(resolve, 300))

    const userMessage: Message = {
      id: Date.now().toString(),
      role: 'user',
      content: query
    }

    setMessages(prev => [...prev, userMessage])
    setInput('')
    setIsSearching(true)
    setShowSuggestions(false)
    setSearchResults([]) // Clear current search results for this query
    setCurrentScrapingUrl('') // Reset scraping URL
    setScreenshots([]) // Clear screenshots
    setIsTransitioning(false)

    // Create assistant message placeholder
    const assistantMessage: Message = {
      id: (Date.now() + 1).toString(),
      role: 'assistant',
      content: '',
      searchData: {
        status: 'searching',
        events: []
      }
    }

    setMessages(prev => [...prev, assistantMessage])


    try {
      const headers: Record<string, string> = { 'Content-Type': 'application/json' }
      
      // Add Firecrawl API key from localStorage if available
      const firecrawlKey = localStorage.getItem('firecrawl_api_key')
      
      if (firecrawlKey) headers['X-Firecrawl-API-Key'] = firecrawlKey
      
      const response = await fetch('/api/open-researcher', {
        method: 'POST',
        headers,
        body: JSON.stringify({ query })
      })

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({ error: 'Unknown error' }))
        // API Error occurred
        throw new Error(errorData.error || errorData.message || 'Search failed')
      }

      const reader = response.body?.getReader()
      const decoder = new TextDecoder()

      if (!reader) throw new Error('No response stream')

      const events: ThinkingEvent[] = []
      let finalContent = ''

      while (true) {
        const { done, value } = await reader.read()
        if (done) break

        const chunk = decoder.decode(value)
        const lines = chunk.split('\n')

        for (const line of lines) {
          if (line.startsWith('data: ')) {
            try {
              const data = JSON.parse(line.slice(6))
              
              if (data.type === 'event') {
                events.push(data.event)
                
                // Parse search results from tool results
                if (data.event.type === 'tool_result' && data.event.tool === 'web_search') {
                  const resultText = data.event.result
                  const parsedResults = parseSearchResults(resultText)
                  setSearchResults(parsedResults)
                  
                  // Extract screenshots if available
                  if (data.event.screenshots) {
                    setScreenshots(data.event.screenshots)
                  }
                  
                  // Check if results mention scraping is happening
                  if (resultText.includes('(SCRAPED)')) {
                    // Find first scraped URL
                    const scrapedMatch = resultText.match(/URL: (https?:\/\/[^\s]+).*?\(SCRAPED\)/)
                    if (scrapedMatch) {
                      setTimeout(() => {
                        setCurrentScrapingUrl(scrapedMatch[1])
                      }, 1000) // Show search results first, then switch to scraping
                    }
                  }
                }
                
                // Track current scraping URL and handle web_search with scraping
                if (data.event.type === 'tool_call') {
                  if (data.event.tool === 'web_search' || data.event.tool === 'firecrawl_search') {
                    // Update the query in the URL bar immediately
                    const searchQuery = (data.event.parameters as { query?: string })?.query || ''
                    setCurrentQuery(searchQuery)
                    setCurrentScrapingUrl('')  // Clear to show search results
                  } else if (data.event.tool === 'firecrawl_scrape' || data.event.tool === 'deep_scrape') {
                    const sourceUrl = (data.event.parameters as { source_url?: string })?.source_url || ''
                    setCurrentScrapingUrl(sourceUrl)
                  }
                } else if (data.event.type === 'tool_result') {
                  if (data.event.tool === 'deep_scrape' || data.event.tool === 'firecrawl_scrape' || data.event.tool === 'web_search') {
                    // Extract screenshots from results
                    // Always add new screenshots even if URL is the same (for multiple scrapes of same page)
                    if (data.event.screenshots) {
                      setScreenshots(prev => [...prev, ...data.event.screenshots])
                    }
                    
                    // Don't clear scraping URL immediately - let it show the screenshot
                    // Only clear when a new tool call happens
                  }
                }
                
                setMessages(prev => prev.map(msg => 
                  msg.id === assistantMessage.id
                    ? { ...msg, searchData: { status: 'searching', events: [...events] } }
                    : msg
                ))
              } else if (data.type === 'response') {
                finalContent = data.content
              } else if (data.type === 'done') {
                setMessages(prev => prev.map(msg => 
                  msg.id === assistantMessage.id
                    ? { 
                        ...msg, 
                        content: finalContent,
                        searchData: { status: 'complete', events: events },
                        sources: searchResults // Keep the sources from this specific search
                      }
                    : msg
                ))
              }
            } catch (e) {
              // Error parsing SSE data
            }
          }
        }
      }
    } catch (error) {
      // Search error occurred
      
      let errorMessage = 'Sorry, an error occurred while searching. Please try again.'
      
      if (error instanceof Error) {
        if (error.message.includes('ANTHROPIC_API_KEY')) {
          errorMessage = 'The Anthropic API key is not configured. Please contact the site administrator.'
        } else if (error.message.includes('FIRECRAWL_API_KEY')) {
          errorMessage = 'The Firecrawl API key is not configured. Please contact the site administrator.'
        } else if (error.message.includes('model')) {
          errorMessage = 'The required AI model is not available. This feature may not be accessible in your region.'
        } else if (error.message.includes('beta')) {
          errorMessage = 'The interleaved thinking feature requires special API access. Please contact support.'
        } else {
          errorMessage = `Error: ${error.message}`
        }
      }
      
      setMessages(prev => prev.map(msg => 
        msg.id === assistantMessage.id
          ? { ...msg, content: errorMessage }
          : msg
      ))
    } finally {
      setIsSearching(false)
    }
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    handleSearch(input)
  }

  const handleSuggestionClick = (suggestion: string) => {
    setInput(suggestion)
    setShowSuggestions(false)
    inputRef.current?.focus()
  }

  // Parse search results from the tool result text
  const parseSearchResults = (resultText: string) => {
    const results: Array<{ url: string; title: string; description?: string; index?: number; scraped?: boolean; dateFound?: string; markdown?: string }> = []
    const lines = resultText.split('\n')
    let currentResult: { url?: string; title?: string; description?: string; index?: number; scraped?: boolean; dateFound?: string; markdown?: string } | null = null
    
    for (const line of lines) {
      // Match result entries like "[1] Title"
      const titleMatch = line.match(/^\[(\d+)\]\s+(.+)$/)
      if (titleMatch) {
        if (currentResult && currentResult.url && currentResult.title) {
          results.push(currentResult as { url: string; title: string; description?: string })
        }
        currentResult = {
          index: parseInt(titleMatch[1]),
          title: titleMatch[2].replace(' (SCRAPED)', ''),
          scraped: line.includes('(SCRAPED)')
        }
        continue
      }
      
      // Match URL lines
      if (line.startsWith('URL: ') && currentResult) {
        currentResult.url = line.substring(5)
        continue
      }
      
      // Match description lines
      if (line.startsWith('Description: ') && currentResult) {
        currentResult.description = line.substring(13)
        continue
      }
      
      // Match date lines
      if (line.startsWith('Date: ') && currentResult) {
        currentResult.dateFound = line.substring(6)
        continue
      }
      
      // Match content preview
      if (line.startsWith('Content preview: ') && currentResult) {
        currentResult.markdown = line.substring(17)
        continue
      }
    }
    
    // Don't forget the last result
    if (currentResult && currentResult.url && currentResult.title) {
      results.push(currentResult as { url: string; title: string; description?: string })
    }
    
    return results
  }

  const hasMessages = messages.length > 0

  // If no messages, show input below hero section
  if (!hasMessages) {
    return (
      <div className={`w-full max-w-2xl mx-auto mt-4 lg:mt-8 px-4 lg:px-0 transition-all duration-500 ${
        isTransitioning ? 'opacity-0 transform -translate-y-4' : 'opacity-100 transform translate-y-0'
      }`}>
        <div className="space-y-4 lg:space-y-8">
          <form onSubmit={handleSubmit} className="relative">
            <input
              ref={inputRef}
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onFocus={() => setShowSuggestions(true)}
              onBlur={() => setTimeout(() => setShowSuggestions(false), 200)}
              placeholder="Enter query..."
              className="w-full h-12 rounded-full border border-zinc-200 bg-white pl-5 pr-14 text-base text-zinc-900 dark:text-zinc-100 ring-offset-white file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-zinc-500 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-orange-500 focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 dark:border-zinc-800 dark:bg-zinc-950 dark:ring-offset-zinc-950 dark:placeholder:text-zinc-400 dark:focus-visible:ring-orange-400 shadow-sm"
              disabled={isSearching}
            />
            <button
              type="submit"
              disabled={isSearching || !input.trim()}
              className="absolute right-2 top-2 h-8 w-8 bg-orange-500 hover:bg-orange-600 text-white rounded-full disabled:opacity-50 disabled:cursor-not-allowed transition-colors duration-200 flex items-center justify-center"
            >
              {isSearching ? (
                <Loader2 className="h-4 w-4 animate-spin" />
              ) : (
                <Send className="h-4 w-4" />
              )}
            </button>
          </form>

          {showSuggestions && !isSearching && (
            <div className="space-y-2">
              <div className={cn(
                "flex items-center gap-2 text-sm text-gray-600 dark:text-gray-400",
                !hasAnimatedSuggestions && "animate-fade-up"
              )} style={{ 
                animationDelay: !hasAnimatedSuggestions ? '200ms' : '0ms',
                opacity: !hasAnimatedSuggestions ? 0 : 1
              }}>
                <span>Try asking:</span>
                <ChevronDown className={cn(
                  "h-3 w-3",
                  !hasAnimatedSuggestions && "animate-bounce"
                )} style={{ animationDelay: !hasAnimatedSuggestions ? '500ms' : '0ms' }} />
              </div>
              <div className="space-y-2">
                {SUGGESTED_QUERIES.map((suggestion, idx) => (
                  <button
                    key={idx}
                    onClick={() => handleSuggestionClick(suggestion)}
                    className={cn(
                      "w-full text-left p-3 rounded-lg bg-gray-50 hover:bg-gray-100 dark:bg-gray-800 dark:hover:bg-gray-700 transition-all duration-300 text-sm text-gray-700 dark:text-gray-300 hover:shadow-sm",
                      !hasAnimatedSuggestions && "animate-fade-up"
                    )}
                    style={{ 
                      animationDelay: !hasAnimatedSuggestions ? `${300 + idx * 80}ms` : '0ms',
                      opacity: !hasAnimatedSuggestions ? 0 : 1,
                      transform: 'translateZ(0)' // Force GPU acceleration to prevent cutoff
                    }}
                  >
                    {suggestion}
                  </button>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>
    )
  }

  // Split layout when messages exist
  return (
    <div className="flex flex-col-reverse lg:flex-row gap-2 lg:gap-4 h-[calc(100vh-120px)] lg:h-[calc(100vh-200px)] animate-slide-up pt-2 lg:pt-5">
      {/* Chat interface - Bottom on mobile, Left on desktop */}
      <div className={cn(
        "flex flex-col bg-white dark:bg-gray-900 rounded-lg border border-gray-200 dark:border-gray-700 shadow-lg overflow-hidden transition-all duration-700 ease-out",
        showFullWidth ? "h-full w-full" : "h-[45vh] lg:h-full lg:w-1/2" // Full height on mobile when browser closed
      )}>
        {/* Messages area */}
        <div className="flex-1 overflow-y-auto p-2 lg:p-4 space-y-3 lg:space-y-4">
          {messages.map((message) => (
            <div
              key={message.id}
              className={cn(
                "flex animate-fade-in",
                message.role === 'user' ? 'justify-end' : 'justify-start'
              )}
            >
              {message.role === 'user' ? (
                <div className="max-w-[85%] lg:max-w-[80%] bg-orange-500 text-white px-3 lg:px-4 py-2 lg:py-3 rounded-lg shadow-sm text-sm">
                  {message.content}
                </div>
              ) : (
                <div className="max-w-[90%] space-y-3">
                  {/* Show thinking events if available */}
                  {message.searchData?.events && message.searchData.events.length > 0 && (
                    <div className="space-y-2">
                      {message.searchData.events.map((event, idx) => {
                        const colorClass = "bg-gray-50 dark:bg-gray-800/50 border-gray-200 dark:border-gray-700"
                        const textColorClass = "text-gray-700 dark:text-gray-300"
                          
                        if (event.type === 'thinking') {
                          return (
                            <div key={idx} className={`px-3 lg:px-4 py-2 lg:py-3 rounded-lg border ${colorClass} max-w-[90%] lg:max-w-[80%]`}>
                              <div className="flex items-start gap-2">
                                <div className="w-1.5 h-1.5 rounded-full bg-blue-500 mt-1.5 flex-shrink-0" />
                                <div className="flex-1">
                                  <div className={`text-sm font-medium ${textColorClass} mb-1`}>
                                    Thinking Block #{event.number}
                                  </div>
                                  <div className={`text-sm ${textColorClass} whitespace-pre-wrap`}>
                                    {event.content || ''}
                                  </div>
                                </div>
                              </div>
                            </div>
                          )
                        }
                        if (event.type === 'tool_call') {
                          const isWebSearch = event.tool === 'firecrawl_search' || event.tool === 'web_search'
                          const isDeepScrape = event.tool === 'firecrawl_scrape' || event.tool === 'deep_scrape'
                          return (
                            <div key={idx} className={`px-3 lg:px-4 py-2 rounded-lg border ${colorClass} max-w-[90%] lg:max-w-[80%]`}>
                              <div className="flex items-start gap-2">
                                <div className={`w-1.5 h-1.5 rounded-full ${isWebSearch ? 'bg-purple-500' : isDeepScrape ? 'bg-orange-500' : 'bg-gray-500'} mt-1.5 flex-shrink-0`} />
                                <div className="flex-1">
                                  <div className="text-sm">
                                    <span className={`font-medium ${textColorClass}`}>
                                      {isWebSearch ? 'Web Search' : isDeepScrape ? 'Deep Scrape' : event.tool}
                                    </span>
                                  </div>
                                  {(event as { parameters?: { query?: string } }).parameters?.query && (
                                    <div className={`text-sm ${textColorClass} opacity-80 mt-1`}>
                                      &quot;{(event as { parameters?: { query?: string } }).parameters?.query}&quot;
                                    </div>
                                  )}
                                </div>
                              </div>
                            </div>
                          )
                        }
                        if (event.type === 'tool_result' && event.result) {
                          const resultPreview = event.result.substring(0, 100)
                          return (
                            <div key={idx} className={`px-3 lg:px-4 py-2 rounded-lg border ${colorClass} max-w-[90%] lg:max-w-[80%]`}>
                              <div className="flex items-start gap-2">
                                <div className="w-1.5 h-1.5 rounded-full bg-green-500 mt-1.5 flex-shrink-0" />
                                <div className="flex-1">
                                  <div className="flex items-center justify-between text-sm">
                                    <span className={`font-medium ${textColorClass}`}>
                                      Results Received
                                    </span>
                                    <span className={`text-xs ${textColorClass} opacity-80`}>
                                      {event.duration ? `${(event.duration / 1000).toFixed(1)}s` : ''}
                                    </span>
                                  </div>
                                  <div className={`text-xs ${textColorClass} opacity-80 mt-1 line-clamp-2`}>
                                    {resultPreview}...
                                  </div>
                                </div>
                              </div>
                            </div>
                          )
                        }
                        return null
                      })}
                    </div>
                  )}
                  
                  {/* Show final response */}
                  {message.content ? (
                    <div className="bg-gray-100 dark:bg-gray-800 px-4 py-3 rounded-lg">
                      <div className="text-sm text-gray-700 dark:text-gray-300">
                        <MarkdownRenderer 
                          content={message.content} 
                          sources={message.sources || []}
                        />
                        <CitationTooltip sources={message.sources || []} />
                      </div>
                    </div>
                  ) : isSearching && message.searchData?.status === 'searching' ? (
                    <div className="bg-gray-100 dark:bg-gray-800 px-4 py-3 rounded-lg animate-fade-in" style={{ animationDelay: '200ms', opacity: 0 }}>
                      <div className="flex items-center gap-2">
                        <Loader2 className="h-4 w-4 animate-spin text-orange-500" />
                        <span className="text-sm text-gray-600 dark:text-gray-400">
                          Researching...
                        </span>
                      </div>
                    </div>
                  ) : null}
                  
                  {/* Action buttons for completed responses */}
                  {message.role === 'assistant' && message.content && message.searchData?.status === 'complete' && (
                    <div className="mt-3 flex items-center">
                      <button
                        onClick={() => {
                          navigator.clipboard.writeText(message.content)
                        }}
                        className="ml-auto p-1.5 rounded-md hover:bg-gray-100 dark:hover:bg-gray-800 text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-300 transition-colors"
                        title="Copy to clipboard"
                      >
                        <Copy className="h-3.5 w-3.5" />
                      </button>
                    </div>
                  )}
                  
                </div>
              )}
            </div>
          ))}
          <div ref={messagesEndRef} />
        </div>

        {/* Input area with firesearch style */}
        <div className="p-2 lg:p-3 border-t border-gray-200 dark:border-gray-700">
          <form onSubmit={handleSubmit}>
            <div className="relative">
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Enter query..."
                className="w-full h-12 rounded-full border border-zinc-200 bg-white pl-5 pr-14 text-base text-zinc-900 dark:text-zinc-100 ring-offset-white file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-zinc-500 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-orange-500 focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 dark:border-zinc-800 dark:bg-zinc-950 dark:ring-offset-zinc-950 dark:placeholder:text-zinc-400 dark:focus-visible:ring-orange-400 shadow-sm"
                disabled={isSearching}
              />
              <button
                type="submit"
                disabled={isSearching || !input.trim()}
                className="absolute right-2 top-2 h-8 w-8 bg-orange-500 hover:bg-orange-600 text-white rounded-full disabled:opacity-50 disabled:cursor-not-allowed transition-colors duration-200 flex items-center justify-center"
              >
                {isSearching ? (
                  <Loader2 className="h-4 w-4 animate-spin" />
                ) : (
                  <Send className="h-4 w-4" />
                )}
              </button>
            </div>
          </form>
        </div>
      </div>

      {/* Browser/Search Results - Top on mobile, Right on desktop */}
      <div className={cn(
        "transition-all duration-700 ease-out",
        showFullWidth 
          ? "w-0 opacity-0 h-0 overflow-hidden" 
          : "h-[45vh] lg:h-full lg:w-1/2"
      )}>
        <SearchResultsDisplay
          query={currentQuery}
          results={searchResults} // Show only current search results
          isActive={isSearching}
          currentUrl={currentScrapingUrl}
          screenshots={screenshots}
          onClose={() => {
            setShowFullWidth(true)
          }}
        />
      </div>
    </div>
  )
}
```

## File: `components/thinking-display.tsx`
```tsx
'use client'

import { useState, useEffect, useRef } from 'react'
import { 
  Brain, 
  Search, 
  FileText, 
  CheckCircle2, 
  Loader2,
  Sparkles,
  AlertCircle,
  Clock,
  Image as ImageIcon
} from 'lucide-react'
import { cn } from '@/lib/utils'
import { MarkdownRenderer } from '@/app/firesearch/markdown-renderer'
import { ScreenshotPreview } from '@/components/screenshot-preview'
import { SearchResultsDisplay } from '@/components/search-results-display'

export interface ThinkingEvent {
  type: 'start' | 'thinking' | 'tool_call' | 'tool_result' | 'response' | 'summary'
  timestamp?: number
  content?: string
  number?: number
  tool?: string
  parameters?: Record<string, unknown>
  result?: string
  searchResults?: Array<{
    url: string
    title: string
    description: string
    markdown?: string
  }>
  screenshots?: Array<{ url: string; screenshot?: string }>
  duration?: number
  thinkingBlocks?: number
  toolCalls?: number
}

interface ThinkingDisplayProps {
  events: ThinkingEvent[]
  status: 'searching' | 'complete' | 'error'
  response?: string
}

const eventIcons: Record<string, React.ComponentType<{className?: string}>> = {
  start: Sparkles,
  thinking: Brain,
  tool_call: Search,
  tool_result: FileText,
  response: CheckCircle2,
  summary: Sparkles
}

const toolNames: Record<string, string> = {
  web_search: 'Web Search',
  firecrawl_search: 'Web Search',
  deep_scrape: 'Deep Web Scrape',
  firecrawl_scrape: 'Deep Web Scrape',
  analyze_content: 'Content Analysis'
}

const getEventIcon = (event: ThinkingEvent) => {
  const Icon = eventIcons[event.type] || AlertCircle
  return Icon
}

const getEventColor = (event: ThinkingEvent, index: number) => {
  const isOdd = index % 2 === 1
  if (isOdd) {
    return 'text-orange-600 dark:text-orange-400 bg-orange-50 dark:bg-orange-900/10'
  } else {
    return 'text-gray-900 dark:text-gray-100 bg-gray-50 dark:bg-gray-900/10'
  }
}

const getEventTitle = (event: ThinkingEvent) => {
  switch (event.type) {
    case 'start':
      return 'Research Started'
    case 'thinking':
      return `Thinking Block #${event.number || 1}`
    case 'tool_call':
      return toolNames[event.tool || ''] || event.tool || 'Tool Call'
    case 'tool_result':
      return 'Results Received'
    case 'response':
      return 'Generating Response'
    case 'summary':
      return 'Research Complete'
    default:
      return 'Processing'
  }
}

const formatDuration = (ms?: number) => {
  if (!ms) return ''
  return `${(ms / 1000).toFixed(1)}s`
}

export function ThinkingDisplay({ events, status, response }: ThinkingDisplayProps) {
  const [elapsedTime, setElapsedTime] = useState(0)
  const [allScreenshots, setAllScreenshots] = useState<Array<{ url: string; screenshot?: string }>>([])
  const [viewMode, setViewMode] = useState<'timeline' | 'results' | 'screenshots'>('timeline')
  const [searchResults, setSearchResults] = useState<Array<{ url: string; title: string; description: string }>>([])
  const [currentQuery, setCurrentQuery] = useState<string>('')
  const startTime = events[0]?.timestamp || Date.now()
  const scrollRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    if (status === 'searching') {
      const interval = setInterval(() => {
        setElapsedTime(Math.floor((Date.now() - startTime) / 1000))
      }, 1000)
      return () => clearInterval(interval)
    }
  }, [status, startTime])

  // Collect all screenshots and search results from events
  useEffect(() => {
    const screenshots: Array<{ url: string; screenshot?: string }> = []
    const results: Array<{ url: string; title: string; description: string }> = []
    let query = ''
    
    events.forEach(event => {
      if (event.screenshots && event.screenshots.length > 0) {
        screenshots.push(...event.screenshots.filter(s => s.screenshot))
      }
      
      // Extract search query
      if (event.type === 'tool_call' && event.tool === 'web_search' && event.parameters?.query) {
        query = event.parameters.query as string
        setCurrentQuery(query)
      }
      
      // Parse search results from tool_result
      if (event.type === 'tool_result' && event.result) {
        const resultText = event.result
        // Parse search results from the text format
        const lines = resultText.split('\n')
        let currentResult: { url?: string; title?: string; description?: string } | null = null
        
        lines.forEach(line => {
          const urlMatch = line.match(/^\d+\.\s+(.+)$/)
          const titleMatch = line.match(/Title:\s+(.+)$/)
          const descMatch = line.match(/Description:\s+(.+)$/)
          
          if (urlMatch) {
            if (currentResult && currentResult.url && currentResult.title && currentResult.description) {
              results.push({
                url: currentResult.url,
                title: currentResult.title,
                description: currentResult.description
              })
            }
            currentResult = { url: urlMatch[1], title: 'Untitled', description: 'No description available' }
          } else if (titleMatch && currentResult) {
            currentResult.title = titleMatch[1]
          } else if (descMatch && currentResult) {
            currentResult.description = descMatch[1]
          }
        })
        
        if (currentResult) {
          const { url, title, description } = currentResult
          if (url && title && description && title !== 'Untitled' && description !== 'No description available') {
            results.push({ url, title, description })
          }
        }
      }
    })
    
    setAllScreenshots(screenshots)
    setSearchResults(results)
    
    // Only auto-switch to results view when search results are found (not for screenshots)
    if (results.length > 0 && viewMode === 'timeline' && screenshots.length === 0) {
      setViewMode('results')
    }
  }, [events, viewMode])

  // Auto-scroll to bottom when new events arrive
  useEffect(() => {
    if (scrollRef.current && status === 'searching') {
      scrollRef.current.scrollIntoView({ behavior: 'smooth', block: 'end' })
    }
  }, [events, status])

  // Show response if complete
  if (status === 'complete' && response) {
    // Filter out the response event from the process display
    const processEvents = events.filter(e => e.type !== 'response');
    
    return (
      <div className="space-y-6">
        {/* Screenshots Gallery */}
        {allScreenshots.length > 0 && (
          <div className="bg-gray-50 dark:bg-gray-900/50 rounded-lg p-4">
            <h3 className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-3 flex items-center gap-2">
              <ImageIcon className="h-4 w-4" />
              Analyzed Pages ({allScreenshots.length})
            </h3>
            <div className="grid grid-cols-2 md:grid-cols-3 gap-3">
              {allScreenshots.map((screenshot, index) => (
                <div key={`${screenshot.url}-${index}`} style={{ animationDelay: `${index * 100}ms` }}>
                  <ScreenshotPreview
                    url={screenshot.url}
                    screenshot={screenshot.screenshot || ''}
                    className="animate-fade-in"
                  />
                </div>
              ))}
            </div>
          </div>
        )}

        <div className="flex gap-6 min-h-[400px]">
          {/* Left side - Thinking process */}
          <div className="flex-1 pr-4 border-r border-gray-200 dark:border-gray-700 overflow-y-auto max-h-[600px]">
            <div className="sticky top-0 bg-white dark:bg-gray-800 pb-3">
              <div className="flex items-center justify-between">
                <h3 className="text-sm font-medium text-gray-700 dark:text-gray-300">Research Process</h3>
                <div className="flex items-center gap-3 text-xs text-gray-600 dark:text-gray-400">
                  <div className="flex items-center gap-1">
                    <Clock className="h-3 w-3" />
                    <span>{elapsedTime}s</span>
                  </div>
                  <div className="flex items-center gap-1">
                    <Brain className="h-3 w-3" />
                    <span>{events.filter(e => e.type === 'thinking').length} thoughts</span>
                  </div>
                  <div className="flex items-center gap-1">
                    <Search className="h-3 w-3" />
                    <span>{events.filter(e => e.type === 'tool_call').length} searches</span>
                  </div>
                  {allScreenshots.length > 0 && (
                    <div className="flex items-center gap-1">
                      <ImageIcon className="h-3 w-3" />
                      <span>{allScreenshots.length} screenshots</span>
                    </div>
                  )}
                </div>
              </div>
            </div>
          <div className="space-y-2">
            {processEvents.map((event, index) => (
              <ThinkingEvent
                key={index}
                event={event}
                index={index}
                isExpanded={false}
                onToggle={() => {}}
                animationDelay={index * 60}
              />
            ))}
          </div>
        </div>

          {/* Right side - Final response */}
          <div className="flex-1 pl-4 overflow-y-auto max-h-[600px] opacity-0 animate-slide-in-right" style={{ animationDelay: `${processEvents.length * 60 + 200}ms`, animationFillMode: 'forwards' }}>
            <div className="prose prose-sm max-w-none dark:prose-invert">
              <h3 className="text-lg font-semibold mb-4 text-gray-900 dark:text-white">Final Response</h3>
              <MarkdownRenderer content={response} />
            </div>
          </div>
        </div>
      </div>
    )
  }

  // Show live thinking process
  return (
    <div className="space-y-4">
      {/* Live status header */}
      <div className="flex items-center justify-between mb-4 animate-fade-in" style={{ animationDelay: '100ms', opacity: 0 }}>
        <div className="flex items-center gap-3">
          <div className="relative">
            <div className="absolute inset-0 bg-orange-500 rounded-full animate-ping opacity-75" />
            <div className="relative w-2 h-2 bg-orange-500 rounded-full" />
          </div>
          <span className="text-sm font-medium text-gray-900 dark:text-white">
            Researching...
          </span>
        </div>
        <div className="flex items-center gap-2 text-sm text-gray-600 dark:text-gray-400">
          <Clock className="h-4 w-4 animate-pulse" />
          <span className="number-transition">{elapsedTime}s</span>
        </div>
      </div>

      {/* View mode tabs */}
      {(searchResults.length > 0 || allScreenshots.length > 0) && (
        <div className="flex gap-2 mb-4 border-b border-gray-200 dark:border-gray-700">
          <button
            onClick={() => setViewMode('timeline')}
            className={cn(
              "px-4 py-2 text-sm font-medium transition-colors border-b-2",
              viewMode === 'timeline' 
                ? "text-orange-600 border-orange-600" 
                : "text-gray-600 dark:text-gray-400 border-transparent hover:text-gray-900 dark:hover:text-gray-200"
            )}
          >
            Timeline
          </button>
          {searchResults.length > 0 && (
            <button
              onClick={() => setViewMode('results')}
              className={cn(
                "px-4 py-2 text-sm font-medium transition-colors border-b-2",
                viewMode === 'results' 
                  ? "text-orange-600 border-orange-600" 
                  : "text-gray-600 dark:text-gray-400 border-transparent hover:text-gray-900 dark:hover:text-gray-200"
              )}
            >
              Search Results ({searchResults.length})
            </button>
          )}
          {allScreenshots.length > 0 && (
            <button
              onClick={() => setViewMode('screenshots')}
              className={cn(
                "px-4 py-2 text-sm font-medium transition-colors border-b-2",
                viewMode === 'screenshots' 
                  ? "text-orange-600 border-orange-600" 
                  : "text-gray-600 dark:text-gray-400 border-transparent hover:text-gray-900 dark:hover:text-gray-200"
              )}
            >
              Screenshots ({allScreenshots.length})
            </button>
          )}
        </div>
      )}

      {/* Content based on view mode */}
      {viewMode === 'timeline' && (
        <div className="space-y-2">
          {events.map((event, index) => (
            <ThinkingEvent
              key={index}
              event={event}
              index={index}
              isExpanded={false}
              onToggle={() => {}}
              isLast={index === events.length - 1}
              isLive={status === 'searching'}
            animationDelay={index * 80}
          />
        ))}
        <div ref={scrollRef} />
        </div>
      )}

      {/* Search Results View */}
      {viewMode === 'results' && (
        <SearchResultsDisplay 
          results={searchResults} 
          query={currentQuery}
          isActive={status === 'searching'}
          screenshots={allScreenshots}
        />
      )}

      {/* Screenshots View */}
      {viewMode === 'screenshots' && (
        <div className="space-y-4">
          {allScreenshots.map((screenshot, idx) => (
            <ScreenshotPreview
              key={`${screenshot.url}-${idx}`}
              url={screenshot.url}
              screenshot={screenshot.screenshot || ''}
              isLoading={false}
              className="w-full"
            />
          ))}
        </div>
      )}
    </div>
  )
}

interface ThinkingEventProps {
  event: ThinkingEvent
  index: number
  isExpanded: boolean
  onToggle: () => void
  isLast?: boolean
  isLive?: boolean
  animationDelay?: number
}

function ThinkingEvent({ event, index, isLast, isLive, animationDelay = 0 }: ThinkingEventProps) {
  const Icon = getEventIcon(event)
  const colorClass = getEventColor(event, index)
  const title = getEventTitle(event)
  const [isVisible, setIsVisible] = useState(false)

  useEffect(() => {
    // Trigger fade-in animation after component mounts with a staggered delay
    const timer = setTimeout(() => {
      setIsVisible(true)
    }, animationDelay * 0.5) // Faster stagger for smoother experience
    return () => clearTimeout(timer)
  }, [animationDelay])

  const isOdd = index % 2 === 1
  const bgClass = isOdd ? 'bg-gradient-to-r from-orange-50 to-orange-100 dark:from-orange-900/20 dark:to-orange-800/20' : 
                         'bg-gradient-to-r from-gray-50 to-gray-100 dark:from-gray-900/20 dark:to-gray-800/20'

  return (
    <div 
      className={cn(
        "relative flex items-start gap-3 p-3 rounded-lg transition-all duration-700 ease-out",
        bgClass,
        "border border-gray-200 dark:border-gray-700",
        isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-2",
        "hover:shadow-md hover:scale-[1.01] cursor-default"
      )}
    >
      <div className={cn("p-2 rounded-full bg-white dark:bg-gray-800 shadow-sm", colorClass)}>
        <Icon className="h-4 w-4" />
      </div>
      
      <div className="flex-1 min-w-0">
        <div className="flex items-center gap-2">
          <h4 className="text-sm font-medium text-gray-900 dark:text-white">
            {title}
          </h4>
          {event.duration && (
            <span className="text-xs text-gray-500 dark:text-gray-400">
              {formatDuration(event.duration)}
            </span>
          )}
          {isLast && isLive && (
            <Loader2 className="h-3 w-3 text-orange-500 animate-spin" />
          )}
        </div>

        {/* Inline content for all events */}
        {event.type === 'tool_call' && event.parameters && (
          <p className="text-xs text-gray-600 dark:text-gray-400 mt-0.5">
            {(event.parameters.query as string) || (event.parameters.source_url as string)}
          </p>
        )}

        {event.type === 'thinking' && event.content && (
          <p className="text-sm text-gray-500 dark:text-gray-400 mt-0.5 italic whitespace-pre-wrap">
            {event.content}
          </p>
        )}

        {event.type === 'tool_result' && event.result && (
          <p className="text-xs text-gray-500 dark:text-gray-400 mt-0.5">
            {event.result.length > 100 
              ? event.result.substring(0, 100) + '...'
              : event.result}
          </p>
        )}

        {event.type === 'tool_result' && event.screenshots && event.screenshots.length > 0 && (
          <div className="mt-4 space-y-3">
            {event.screenshots.map((screenshot, idx) => (
              screenshot.screenshot && (
                <div key={`${screenshot.url}-${idx}`} className="relative">
                  <ScreenshotPreview
                    url={screenshot.url}
                    screenshot={screenshot.screenshot}
                    isLoading={isLast && isLive}
                    className="w-full"
                  />
                  {isLast && isLive && (
                    <div className="absolute top-2 right-2 bg-black/80 text-white px-3 py-1 rounded-md text-sm font-mono animate-pulse z-10">
                      <span>Analyzing page content...</span>
                    </div>
                  )}
                </div>
              )
            ))}
          </div>
        )}

        {event.type === 'summary' && (
          <p className="text-xs text-gray-600 dark:text-gray-400 mt-0.5">
            {event.thinkingBlocks} thinking blocks, {event.toolCalls} tool calls
          </p>
        )}
      </div>

    </div>
  )
}
```

## File: `components/ui/accordion.tsx`
```tsx
"use client"

import * as React from "react"
import * as AccordionPrimitive from "@radix-ui/react-accordion"
import { ChevronDownIcon } from "lucide-react"

import { cn } from "@/lib/utils"

function Accordion({
  ...props
}: React.ComponentProps<typeof AccordionPrimitive.Root>) {
  return <AccordionPrimitive.Root data-slot="accordion" {...props} />
}

function AccordionItem({
  className,
  ...props
}: React.ComponentProps<typeof AccordionPrimitive.Item>) {
  return (
    <AccordionPrimitive.Item
      data-slot="accordion-item"
      className={cn("border-b last:border-b-0", className)}
      {...props}
    />
  )
}

function AccordionTrigger({
  className,
  children,
  ...props
}: React.ComponentProps<typeof AccordionPrimitive.Trigger>) {
  return (
    <AccordionPrimitive.Header className="flex">
      <AccordionPrimitive.Trigger
        data-slot="accordion-trigger"
        className={cn(
          "focus-visible:border-ring focus-visible:ring-ring/50 flex flex-1 items-start justify-between gap-4 rounded-md py-4 text-left text-sm font-medium transition-all outline-none hover:underline focus-visible:ring-[3px] disabled:pointer-events-none disabled:opacity-50 [&[data-state=open]>svg]:rotate-180",
          className
        )}
        {...props}
      >
        {children}
        <ChevronDownIcon className="text-muted-foreground pointer-events-none size-4 shrink-0 translate-y-0.5 transition-transform duration-200" />
      </AccordionPrimitive.Trigger>
    </AccordionPrimitive.Header>
  )
}

function AccordionContent({
  className,
  children,
  ...props
}: React.ComponentProps<typeof AccordionPrimitive.Content>) {
  return (
    <AccordionPrimitive.Content
      data-slot="accordion-content"
      className="data-[state=closed]:animate-accordion-up data-[state=open]:animate-accordion-down overflow-hidden text-sm"
      {...props}
    >
      <div className={cn("pt-0 pb-4", className)}>{children}</div>
    </AccordionPrimitive.Content>
  )
}

export { Accordion, AccordionItem, AccordionTrigger, AccordionContent }
```

## File: `components/ui/alert-dialog.tsx`
```tsx
"use client"

import * as React from "react"
import * as AlertDialogPrimitive from "@radix-ui/react-alert-dialog"

import { cn } from "@/lib/utils"
import { buttonVariants } from "@/components/ui/button"

function AlertDialog({
  ...props
}: React.ComponentProps<typeof AlertDialogPrimitive.Root>) {
  return <AlertDialogPrimitive.Root data-slot="alert-dialog" {...props} />
}

function AlertDialogTrigger({
  ...props
}: React.ComponentProps<typeof AlertDialogPrimitive.Trigger>) {
  return (
    <AlertDialogPrimitive.Trigger data-slot="alert-dialog-trigger" {...props} />
  )
}

function AlertDialogPortal({
  ...props
}: React.ComponentProps<typeof AlertDialogPrimitive.Portal>) {
  return (
    <AlertDialogPrimitive.Portal data-slot="alert-dialog-portal" {...props} />
  )
}

function AlertDialogOverlay({
  className,
  ...props
}: React.ComponentProps<typeof AlertDialogPrimitive.Overlay>) {
  return (
    <AlertDialogPrimitive.Overlay
      data-slot="alert-dialog-overlay"
      className={cn(
        "data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 fixed inset-0 z-50 bg-black/50",
        className
      )}
      {...props}
    />
  )
}

function AlertDialogContent({
  className,
  ...props
}: React.ComponentProps<typeof AlertDialogPrimitive.Content>) {
  return (
    <AlertDialogPortal>
      <AlertDialogOverlay />
      <AlertDialogPrimitive.Content
        data-slot="alert-dialog-content"
        className={cn(
          "bg-background data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 fixed top-[50%] left-[50%] z-50 grid w-full max-w-[calc(100%-2rem)] translate-x-[-50%] translate-y-[-50%] gap-4 rounded-lg border p-6 shadow-lg duration-200 sm:max-w-lg",
          className
        )}
        {...props}
      />
    </AlertDialogPortal>
  )
}

function AlertDialogHeader({
  className,
  ...props
}: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="alert-dialog-header"
      className={cn("flex flex-col gap-2 text-center sm:text-left", className)}
      {...props}
    />
  )
}

function AlertDialogFooter({
  className,
  ...props
}: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="alert-dialog-footer"
      className={cn(
        "flex flex-col-reverse gap-2 sm:flex-row sm:justify-end",
        className
      )}
      {...props}
    />
  )
}

function AlertDialogTitle({
  className,
  ...props
}: React.ComponentProps<typeof AlertDialogPrimitive.Title>) {
  return (
    <AlertDialogPrimitive.Title
      data-slot="alert-dialog-title"
      className={cn("text-lg font-semibold", className)}
      {...props}
    />
  )
}

function AlertDialogDescription({
  className,
  ...props
}: React.ComponentProps<typeof AlertDialogPrimitive.Description>) {
  return (
    <AlertDialogPrimitive.Description
      data-slot="alert-dialog-description"
      className={cn("text-muted-foreground text-sm", className)}
      {...props}
    />
  )
}

function AlertDialogAction({
  className,
  ...props
}: React.ComponentProps<typeof AlertDialogPrimitive.Action>) {
  return (
    <AlertDialogPrimitive.Action
      className={cn(buttonVariants(), className)}
      {...props}
    />
  )
}

function AlertDialogCancel({
  className,
  ...props
}: React.ComponentProps<typeof AlertDialogPrimitive.Cancel>) {
  return (
    <AlertDialogPrimitive.Cancel
      className={cn(buttonVariants({ variant: "outline" }), className)}
      {...props}
    />
  )
}

export {
  AlertDialog,
  AlertDialogPortal,
  AlertDialogOverlay,
  AlertDialogTrigger,
  AlertDialogContent,
  AlertDialogHeader,
  AlertDialogFooter,
  AlertDialogTitle,
  AlertDialogDescription,
  AlertDialogAction,
  AlertDialogCancel,
}
```

## File: `components/ui/alert.tsx`
```tsx
import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const alertVariants = cva(
  "relative w-full rounded-lg border px-4 py-3 text-sm grid has-[>svg]:grid-cols-[calc(var(--spacing)*4)_1fr] grid-cols-[0_1fr] has-[>svg]:gap-x-3 gap-y-0.5 items-start [&>svg]:size-4 [&>svg]:translate-y-0.5 [&>svg]:text-current",
  {
    variants: {
      variant: {
        default: "bg-card text-card-foreground",
        destructive:
          "text-destructive bg-card [&>svg]:text-current *:data-[slot=alert-description]:text-destructive/90",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

function Alert({
  className,
  variant,
  ...props
}: React.ComponentProps<"div"> & VariantProps<typeof alertVariants>) {
  return (
    <div
      data-slot="alert"
      role="alert"
      className={cn(alertVariants({ variant }), className)}
      {...props}
    />
  )
}

function AlertTitle({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="alert-title"
      className={cn(
        "col-start-2 line-clamp-1 min-h-4 font-medium tracking-tight",
        className
      )}
      {...props}
    />
  )
}

function AlertDescription({
  className,
  ...props
}: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="alert-description"
      className={cn(
        "text-muted-foreground col-start-2 grid justify-items-start gap-1 text-sm [&_p]:leading-relaxed",
        className
      )}
      {...props}
    />
  )
}

export { Alert, AlertTitle, AlertDescription }
```

## File: `components/ui/aspect-ratio.tsx`
```tsx
"use client"

import * as AspectRatioPrimitive from "@radix-ui/react-aspect-ratio"

function AspectRatio({
  ...props
}: React.ComponentProps<typeof AspectRatioPrimitive.Root>) {
  return <AspectRatioPrimitive.Root data-slot="aspect-ratio" {...props} />
}

export { AspectRatio }
```

## File: `components/ui/avatar.tsx`
```tsx
"use client"

import * as React from "react"
import * as AvatarPrimitive from "@radix-ui/react-avatar"

import { cn } from "@/lib/utils"

function Avatar({
  className,
  ...props
}: React.ComponentProps<typeof AvatarPrimitive.Root>) {
  return (
    <AvatarPrimitive.Root
      data-slot="avatar"
      className={cn(
        "relative flex size-8 shrink-0 overflow-hidden rounded-full",
        className
      )}
      {...props}
    />
  )
}

function AvatarImage({
  className,
  ...props
}: React.ComponentProps<typeof AvatarPrimitive.Image>) {
  return (
    <AvatarPrimitive.Image
      data-slot="avatar-image"
      className={cn("aspect-square size-full", className)}
      {...props}
    />
  )
}

function AvatarFallback({
  className,
  ...props
}: React.ComponentProps<typeof AvatarPrimitive.Fallback>) {
  return (
    <AvatarPrimitive.Fallback
      data-slot="avatar-fallback"
      className={cn(
        "bg-muted flex size-full items-center justify-center rounded-full",
        className
      )}
      {...props}
    />
  )
}

export { Avatar, AvatarImage, AvatarFallback }
```

## File: `components/ui/badge.tsx`
```tsx
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const badgeVariants = cva(
  "inline-flex items-center justify-center rounded-md border px-2 py-0.5 text-xs font-medium w-fit whitespace-nowrap shrink-0 [&>svg]:size-3 gap-1 [&>svg]:pointer-events-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive transition-[color,box-shadow] overflow-hidden",
  {
    variants: {
      variant: {
        default:
          "border-transparent bg-primary text-primary-foreground [a&]:hover:bg-primary/90",
        secondary:
          "border-transparent bg-secondary text-secondary-foreground [a&]:hover:bg-secondary/90",
        destructive:
          "border-transparent bg-destructive text-white [a&]:hover:bg-destructive/90 focus-visible:ring-destructive/20 dark:focus-visible:ring-destructive/40 dark:bg-destructive/60",
        outline:
          "text-foreground [a&]:hover:bg-accent [a&]:hover:text-accent-foreground",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

function Badge({
  className,
  variant,
  asChild = false,
  ...props
}: React.ComponentProps<"span"> &
  VariantProps<typeof badgeVariants> & { asChild?: boolean }) {
  const Comp = asChild ? Slot : "span"

  return (
    <Comp
      data-slot="badge"
      className={cn(badgeVariants({ variant }), className)}
      {...props}
    />
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

function Breadcrumb({ ...props }: React.ComponentProps<"nav">) {
  return <nav aria-label="breadcrumb" data-slot="breadcrumb" {...props} />
}

function BreadcrumbList({ className, ...props }: React.ComponentProps<"ol">) {
  return (
    <ol
      data-slot="breadcrumb-list"
      className={cn(
        "text-muted-foreground flex flex-wrap items-center gap-1.5 text-sm break-words sm:gap-2.5",
        className
      )}
      {...props}
    />
  )
}

function BreadcrumbItem({ className, ...props }: React.ComponentProps<"li">) {
  return (
    <li
      data-slot="breadcrumb-item"
      className={cn("inline-flex items-center gap-1.5", className)}
      {...props}
    />
  )
}

function BreadcrumbLink({
  asChild,
  className,
  ...props
}: React.ComponentProps<"a"> & {
  asChild?: boolean
}) {
  const Comp = asChild ? Slot : "a"

  return (
    <Comp
      data-slot="breadcrumb-link"
      className={cn("hover:text-foreground transition-colors", className)}
      {...props}
    />
  )
}

function BreadcrumbPage({ className, ...props }: React.ComponentProps<"span">) {
  return (
    <span
      data-slot="breadcrumb-page"
      role="link"
      aria-disabled="true"
      aria-current="page"
      className={cn("text-foreground font-normal", className)}
      {...props}
    />
  )
}

function BreadcrumbSeparator({
  children,
  className,
  ...props
}: React.ComponentProps<"li">) {
  return (
    <li
      data-slot="breadcrumb-separator"
      role="presentation"
      aria-hidden="true"
      className={cn("[&>svg]:size-3.5", className)}
      {...props}
    >
      {children ?? <ChevronRight />}
    </li>
  )
}

function BreadcrumbEllipsis({
  className,
  ...props
}: React.ComponentProps<"span">) {
  return (
    <span
      data-slot="breadcrumb-ellipsis"
      role="presentation"
      aria-hidden="true"
      className={cn("flex size-9 items-center justify-center", className)}
      {...props}
    >
      <MoreHorizontal className="size-4" />
      <span className="sr-only">More</span>
    </span>
  )
}

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

## File: `components/ui/calendar.tsx`
```tsx
"use client"

import * as React from "react"
import { ChevronLeft, ChevronRight } from "lucide-react"
import { DayPicker } from "react-day-picker"

import { cn } from "@/lib/utils"
import { buttonVariants } from "@/components/ui/button"

function Calendar({
  className,
  classNames,
  showOutsideDays = true,
  ...props
}: React.ComponentProps<typeof DayPicker>) {
  return (
    <DayPicker
      showOutsideDays={showOutsideDays}
      className={cn("p-3", className)}
      classNames={{
        months: "flex flex-col sm:flex-row gap-2",
        month: "flex flex-col gap-4",
        caption: "flex justify-center pt-1 relative items-center w-full",
        caption_label: "text-sm font-medium",
        nav: "flex items-center gap-1",
        nav_button: cn(
          buttonVariants({ variant: "outline" }),
          "size-7 bg-transparent p-0 opacity-50 hover:opacity-100"
        ),
        nav_button_previous: "absolute left-1",
        nav_button_next: "absolute right-1",
        table: "w-full border-collapse space-x-1",
        head_row: "flex",
        head_cell:
          "text-muted-foreground rounded-md w-8 font-normal text-[0.8rem]",
        row: "flex w-full mt-2",
        cell: cn(
          "relative p-0 text-center text-sm focus-within:relative focus-within:z-20 [&:has([aria-selected])]:bg-accent [&:has([aria-selected].day-range-end)]:rounded-r-md",
          props.mode === "range"
            ? "[&:has(>.day-range-end)]:rounded-r-md [&:has(>.day-range-start)]:rounded-l-md first:[&:has([aria-selected])]:rounded-l-md last:[&:has([aria-selected])]:rounded-r-md"
            : "[&:has([aria-selected])]:rounded-md"
        ),
        day: cn(
          buttonVariants({ variant: "ghost" }),
          "size-8 p-0 font-normal aria-selected:opacity-100"
        ),
        day_range_start:
          "day-range-start aria-selected:bg-primary aria-selected:text-primary-foreground",
        day_range_end:
          "day-range-end aria-selected:bg-primary aria-selected:text-primary-foreground",
        day_selected:
          "bg-primary text-primary-foreground hover:bg-primary hover:text-primary-foreground focus:bg-primary focus:text-primary-foreground",
        day_today: "bg-accent text-accent-foreground",
        day_outside:
          "day-outside text-muted-foreground aria-selected:text-muted-foreground",
        day_disabled: "text-muted-foreground opacity-50",
        day_range_middle:
          "aria-selected:bg-accent aria-selected:text-accent-foreground",
        day_hidden: "invisible",
        ...classNames,
      }}
      components={{
        IconLeft: ({ className, ...props }) => (
          <ChevronLeft className={cn("size-4", className)} {...props} />
        ),
        IconRight: ({ className, ...props }) => (
          <ChevronRight className={cn("size-4", className)} {...props} />
        ),
      }}
      {...props}
    />
  )
}

export { Calendar }
```

## File: `components/ui/card.tsx`
```tsx
import * as React from "react"

import { cn } from "@/lib/utils"

function Card({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card"
      className={cn(
        "bg-card text-card-foreground flex flex-col rounded-xl border py-6 shadow-sm",
        className
      )}
      {...props}
    />
  )
}

function CardHeader({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-header"
      className={cn(
        "@container/card-header grid auto-rows-min grid-rows-[auto_auto] items-start gap-1.5 px-6 has-data-[slot=card-action]:grid-cols-[1fr_auto] [.border-b]:pb-6",
        className
      )}
      {...props}
    />
  )
}

function CardTitle({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-title"
      className={cn("leading-none font-semibold", className)}
      {...props}
    />
  )
}

function CardDescription({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-description"
      className={cn("text-muted-foreground text-sm", className)}
      {...props}
    />
  )
}

function CardAction({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-action"
      className={cn(
        "col-start-2 row-span-2 row-start-1 self-start justify-self-end",
        className
      )}
      {...props}
    />
  )
}

function CardContent({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-content"
      className={cn("px-6", className)}
      {...props}
    />
  )
}

function CardFooter({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-footer"
      className={cn("flex items-center px-6 [.border-t]:pt-6", className)}
      {...props}
    />
  )
}

export {
  Card,
  CardHeader,
  CardFooter,
  CardTitle,
  CardAction,
  CardDescription,
  CardContent,
}
```

## File: `components/ui/carousel.tsx`
```tsx
"use client"

import * as React from "react"
import useEmblaCarousel, {
  type UseEmblaCarouselType,
} from "embla-carousel-react"
import { ArrowLeft, ArrowRight } from "lucide-react"

import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"

type CarouselApi = UseEmblaCarouselType[1]
type UseCarouselParameters = Parameters<typeof useEmblaCarousel>
type CarouselOptions = UseCarouselParameters[0]
type CarouselPlugin = UseCarouselParameters[1]

type CarouselProps = {
  opts?: CarouselOptions
  plugins?: CarouselPlugin
  orientation?: "horizontal" | "vertical"
  setApi?: (api: CarouselApi) => void
}

type CarouselContextProps = {
  carouselRef: ReturnType<typeof useEmblaCarousel>[0]
  api: ReturnType<typeof useEmblaCarousel>[1]
  scrollPrev: () => void
  scrollNext: () => void
  canScrollPrev: boolean
  canScrollNext: boolean
} & CarouselProps

const CarouselContext = React.createContext<CarouselContextProps | null>(null)

function useCarousel() {
  const context = React.useContext(CarouselContext)

  if (!context) {
    throw new Error("useCarousel must be used within a <Carousel />")
  }

  return context
}

function Carousel({
  orientation = "horizontal",
  opts,
  setApi,
  plugins,
  className,
  children,
  ...props
}: React.ComponentProps<"div"> & CarouselProps) {
  const [carouselRef, api] = useEmblaCarousel(
    {
      ...opts,
      axis: orientation === "horizontal" ? "x" : "y",
    },
    plugins
  )
  const [canScrollPrev, setCanScrollPrev] = React.useState(false)
  const [canScrollNext, setCanScrollNext] = React.useState(false)

  const onSelect = React.useCallback((api: CarouselApi) => {
    if (!api) return
    setCanScrollPrev(api.canScrollPrev())
    setCanScrollNext(api.canScrollNext())
  }, [])

  const scrollPrev = React.useCallback(() => {
    api?.scrollPrev()
  }, [api])

  const scrollNext = React.useCallback(() => {
    api?.scrollNext()
  }, [api])

  const handleKeyDown = React.useCallback(
    (event: React.KeyboardEvent<HTMLDivElement>) => {
      if (event.key === "ArrowLeft") {
        event.preventDefault()
        scrollPrev()
      } else if (event.key === "ArrowRight") {
        event.preventDefault()
        scrollNext()
      }
    },
    [scrollPrev, scrollNext]
  )

  React.useEffect(() => {
    if (!api || !setApi) return
    setApi(api)
  }, [api, setApi])

  React.useEffect(() => {
    if (!api) return
    onSelect(api)
    api.on("reInit", onSelect)
    api.on("select", onSelect)

    return () => {
      api?.off("select", onSelect)
    }
  }, [api, onSelect])

  return (
    <CarouselContext.Provider
      value={{
        carouselRef,
        api: api,
        opts,
        orientation:
          orientation || (opts?.axis === "y" ? "vertical" : "horizontal"),
        scrollPrev,
        scrollNext,
        canScrollPrev,
        canScrollNext,
      }}
    >
      <div
        onKeyDownCapture={handleKeyDown}
        className={cn("relative", className)}
        role="region"
        aria-roledescription="carousel"
        data-slot="carousel"
        {...props}
      >
        {children}
      </div>
    </CarouselContext.Provider>
  )
}

function CarouselContent({ className, ...props }: React.ComponentProps<"div">) {
  const { carouselRef, orientation } = useCarousel()

  return (
    <div
      ref={carouselRef}
      className="overflow-hidden"
      data-slot="carousel-content"
    >
      <div
        className={cn(
          "flex",
          orientation === "horizontal" ? "-ml-4" : "-mt-4 flex-col",
          className
        )}
        {...props}
      />
    </div>
  )
}

function CarouselItem({ className, ...props }: React.ComponentProps<"div">) {
  const { orientation } = useCarousel()

  return (
    <div
      role="group"
      aria-roledescription="slide"
      data-slot="carousel-item"
      className={cn(
        "min-w-0 shrink-0 grow-0 basis-full",
        orientation === "horizontal" ? "pl-4" : "pt-4",
        className
      )}
      {...props}
    />
  )
}

function CarouselPrevious({
  className,
  variant = "outline",
  size = "icon",
  ...props
}: React.ComponentProps<typeof Button>) {
  const { orientation, scrollPrev, canScrollPrev } = useCarousel()

  return (
    <Button
      data-slot="carousel-previous"
      variant={variant}
      size={size}
      className={cn(
        "absolute size-8 rounded-full",
        orientation === "horizontal"
          ? "top-1/2 -left-12 -translate-y-1/2"
          : "-top-12 left-1/2 -translate-x-1/2 rotate-90",
        className
      )}
      disabled={!canScrollPrev}
      onClick={scrollPrev}
      {...props}
    >
      <ArrowLeft />
      <span className="sr-only">Previous slide</span>
    </Button>
  )
}

function CarouselNext({
  className,
  variant = "outline",
  size = "icon",
  ...props
}: React.ComponentProps<typeof Button>) {
  const { orientation, scrollNext, canScrollNext } = useCarousel()

  return (
    <Button
      data-slot="carousel-next"
      variant={variant}
      size={size}
      className={cn(
        "absolute size-8 rounded-full",
        orientation === "horizontal"
          ? "top-1/2 -right-12 -translate-y-1/2"
          : "-bottom-12 left-1/2 -translate-x-1/2 rotate-90",
        className
      )}
      disabled={!canScrollNext}
      onClick={scrollNext}
      {...props}
    >
      <ArrowRight />
      <span className="sr-only">Next slide</span>
    </Button>
  )
}

export {
  type CarouselApi,
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselPrevious,
  CarouselNext,
}
```

## File: `components/ui/chart.tsx`
```tsx
"use client"

import * as React from "react"
import * as RechartsPrimitive from "recharts"

import { cn } from "@/lib/utils"

// Format: { THEME_NAME: CSS_SELECTOR }
const THEMES = { light: "", dark: ".dark" } as const

export type ChartConfig = {
  [k in string]: {
    label?: React.ReactNode
    icon?: React.ComponentType
  } & (
    | { color?: string; theme?: never }
    | { color?: never; theme: Record<keyof typeof THEMES, string> }
  )
}

type ChartContextProps = {
  config: ChartConfig
}

const ChartContext = React.createContext<ChartContextProps | null>(null)

function useChart() {
  const context = React.useContext(ChartContext)

  if (!context) {
    throw new Error("useChart must be used within a <ChartContainer />")
  }

  return context
}

function ChartContainer({
  id,
  className,
  children,
  config,
  ...props
}: React.ComponentProps<"div"> & {
  config: ChartConfig
  children: React.ComponentProps<
    typeof RechartsPrimitive.ResponsiveContainer
  >["children"]
}) {
  const uniqueId = React.useId()
  const chartId = `chart-${id || uniqueId.replace(/:/g, "")}`

  return (
    <ChartContext.Provider value={{ config }}>
      <div
        data-slot="chart"
        data-chart={chartId}
        className={cn(
          "[&_.recharts-cartesian-axis-tick_text]:fill-muted-foreground [&_.recharts-cartesian-grid_line[stroke='#ccc']]:stroke-border/50 [&_.recharts-curve.recharts-tooltip-cursor]:stroke-border [&_.recharts-polar-grid_[stroke='#ccc']]:stroke-border [&_.recharts-radial-bar-background-sector]:fill-muted [&_.recharts-rectangle.recharts-tooltip-cursor]:fill-muted [&_.recharts-reference-line_[stroke='#ccc']]:stroke-border flex aspect-video justify-center text-xs [&_.recharts-dot[stroke='#fff']]:stroke-transparent [&_.recharts-layer]:outline-hidden [&_.recharts-sector]:outline-hidden [&_.recharts-sector[stroke='#fff']]:stroke-transparent [&_.recharts-surface]:outline-hidden",
          className
        )}
        {...props}
      >
        <ChartStyle id={chartId} config={config} />
        <RechartsPrimitive.ResponsiveContainer>
          {children}
        </RechartsPrimitive.ResponsiveContainer>
      </div>
    </ChartContext.Provider>
  )
}

const ChartStyle = ({ id, config }: { id: string; config: ChartConfig }) => {
  const colorConfig = Object.entries(config).filter(
    ([, config]) => config.theme || config.color
  )

  if (!colorConfig.length) {
    return null
  }

  return (
    <style
      dangerouslySetInnerHTML={{
        __html: Object.entries(THEMES)
          .map(
            ([theme, prefix]) => `
${prefix} [data-chart=${id}] {
${colorConfig
  .map(([key, itemConfig]) => {
    const color =
      itemConfig.theme?.[theme as keyof typeof itemConfig.theme] ||
      itemConfig.color
    return color ? `  --color-${key}: ${color};` : null
  })
  .join("\n")}
}
`
          )
          .join("\n"),
      }}
    />
  )
}

const ChartTooltip = RechartsPrimitive.Tooltip

function ChartTooltipContent({
  active,
  payload,
  className,
  indicator = "dot",
  hideLabel = false,
  hideIndicator = false,
  label,
  labelFormatter,
  labelClassName,
  formatter,
  color,
  nameKey,
  labelKey,
}: React.ComponentProps<typeof RechartsPrimitive.Tooltip> &
  React.ComponentProps<"div"> & {
    hideLabel?: boolean
    hideIndicator?: boolean
    indicator?: "line" | "dot" | "dashed"
    nameKey?: string
    labelKey?: string
  }) {
  const { config } = useChart()

  const tooltipLabel = React.useMemo(() => {
    if (hideLabel || !payload?.length) {
      return null
    }

    const [item] = payload
    const key = `${labelKey || item?.dataKey || item?.name || "value"}`
    const itemConfig = getPayloadConfigFromPayload(config, item, key)
    const value =
      !labelKey && typeof label === "string"
        ? config[label as keyof typeof config]?.label || label
        : itemConfig?.label

    if (labelFormatter) {
      return (
        <div className={cn("font-medium", labelClassName)}>
          {labelFormatter(value, payload)}
        </div>
      )
    }

    if (!value) {
      return null
    }

    return <div className={cn("font-medium", labelClassName)}>{value}</div>
  }, [
    label,
    labelFormatter,
    payload,
    hideLabel,
    labelClassName,
    config,
    labelKey,
  ])

  if (!active || !payload?.length) {
    return null
  }

  const nestLabel = payload.length === 1 && indicator !== "dot"

  return (
    <div
      className={cn(
        "border-border/50 bg-background grid min-w-[8rem] items-start gap-1.5 rounded-lg border px-2.5 py-1.5 text-xs shadow-xl",
        className
      )}
    >
      {!nestLabel ? tooltipLabel : null}
      <div className="grid gap-1.5">
        {payload.map((item, index) => {
          const key = `${nameKey || item.name || item.dataKey || "value"}`
          const itemConfig = getPayloadConfigFromPayload(config, item, key)
          const indicatorColor = color || item.payload.fill || item.color

          return (
            <div
              key={item.dataKey}
              className={cn(
                "[&>svg]:text-muted-foreground flex w-full flex-wrap items-stretch gap-2 [&>svg]:h-2.5 [&>svg]:w-2.5",
                indicator === "dot" && "items-center"
              )}
            >
              {formatter && item?.value !== undefined && item.name ? (
                formatter(item.value, item.name, item, index, item.payload)
              ) : (
                <>
                  {itemConfig?.icon ? (
                    <itemConfig.icon />
                  ) : (
                    !hideIndicator && (
                      <div
                        className={cn(
                          "shrink-0 rounded-[2px] border-(--color-border) bg-(--color-bg)",
                          {
                            "h-2.5 w-2.5": indicator === "dot",
                            "w-1": indicator === "line",
                            "w-0 border-[1.5px] border-dashed bg-transparent":
                              indicator === "dashed",
                            "my-0.5": nestLabel && indicator === "dashed",
                          }
                        )}
                        style={
                          {
                            "--color-bg": indicatorColor,
                            "--color-border": indicatorColor,
                          } as React.CSSProperties
                        }
                      />
                    )
                  )}
                  <div
                    className={cn(
                      "flex flex-1 justify-between leading-none",
                      nestLabel ? "items-end" : "items-center"
                    )}
                  >
                    <div className="grid gap-1.5">
                      {nestLabel ? tooltipLabel : null}
                      <span className="text-muted-foreground">
                        {itemConfig?.label || item.name}
                      </span>
                    </div>
                    {item.value && (
                      <span className="text-foreground font-mono font-medium tabular-nums">
                        {item.value.toLocaleString()}
                      </span>
                    )}
                  </div>
                </>
              )}
            </div>
          )
        })}
      </div>
    </div>
  )
}

const ChartLegend = RechartsPrimitive.Legend

function ChartLegendContent({
  className,
  hideIcon = false,
  payload,
  verticalAlign = "bottom",
  nameKey,
}: React.ComponentProps<"div"> &
  Pick<RechartsPrimitive.LegendProps, "payload" | "verticalAlign"> & {
    hideIcon?: boolean
    nameKey?: string
  }) {
  const { config } = useChart()

  if (!payload?.length) {
    return null
  }

  return (
    <div
      className={cn(
        "flex items-center justify-center gap-4",
        verticalAlign === "top" ? "pb-3" : "pt-3",
        className
      )}
    >
      {payload.map((item) => {
        const key = `${nameKey || item.dataKey || "value"}`
        const itemConfig = getPayloadConfigFromPayload(config, item, key)

        return (
          <div
            key={item.value}
            className={cn(
              "[&>svg]:text-muted-foreground flex items-center gap-1.5 [&>svg]:h-3 [&>svg]:w-3"
            )}
          >
            {itemConfig?.icon && !hideIcon ? (
              <itemConfig.icon />
            ) : (
              <div
                className="h-2 w-2 shrink-0 rounded-[2px]"
                style={{
                  backgroundColor: item.color,
                }}
              />
            )}
            {itemConfig?.label}
          </div>
        )
      })}
    </div>
  )
}

// Helper to extract item config from a payload.
function getPayloadConfigFromPayload(
  config: ChartConfig,
  payload: unknown,
  key: string
) {
  if (typeof payload !== "object" || payload === null) {
    return undefined
  }

  const payloadPayload =
    "payload" in payload &&
    typeof payload.payload === "object" &&
    payload.payload !== null
      ? payload.payload
      : undefined

  let configLabelKey: string = key

  if (
    key in payload &&
    typeof payload[key as keyof typeof payload] === "string"
  ) {
    configLabelKey = payload[key as keyof typeof payload] as string
  } else if (
    payloadPayload &&
    key in payloadPayload &&
    typeof payloadPayload[key as keyof typeof payloadPayload] === "string"
  ) {
    configLabelKey = payloadPayload[
      key as keyof typeof payloadPayload
    ] as string
  }

  return configLabelKey in config
    ? config[configLabelKey]
    : config[key as keyof typeof config]
}

export {
  ChartContainer,
  ChartTooltip,
  ChartTooltipContent,
  ChartLegend,
  ChartLegendContent,
  ChartStyle,
}
```

## File: `components/ui/checkbox.tsx`
```tsx
"use client"

import * as React from "react"
import * as CheckboxPrimitive from "@radix-ui/react-checkbox"
import { CheckIcon } from "lucide-react"

import { cn } from "@/lib/utils"

function Checkbox({
  className,
  ...props
}: React.ComponentProps<typeof CheckboxPrimitive.Root>) {
  return (
    <CheckboxPrimitive.Root
      data-slot="checkbox"
      className={cn(
        "peer border-input dark:bg-input/30 focus-visible:border-ring focus-visible:ring-ring/50 aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive size-4 shrink-0 rounded-[4px] border shadow-xs transition-shadow outline-none focus-visible:ring-[3px] disabled:cursor-not-allowed disabled:opacity-50",
        "data-[state=checked]:bg-zinc-900 data-[state=checked]:text-zinc-50 data-[state=checked]:border-zinc-900",
        "dark:data-[state=checked]:bg-zinc-900 dark:data-[state=checked]:text-zinc-50 dark:data-[state=checked]:border-zinc-900",
        className
      )}
      {...props}
    >
      <CheckboxPrimitive.Indicator
        data-slot="checkbox-indicator"
        className="flex items-center justify-center text-current transition-none"
      >
        <CheckIcon className="size-3.5" />
      </CheckboxPrimitive.Indicator>
    </CheckboxPrimitive.Root>
  )
}

export { Checkbox }
```

## File: `components/ui/collapsible.tsx`
```tsx
"use client"

import * as CollapsiblePrimitive from "@radix-ui/react-collapsible"

function Collapsible({
  ...props
}: React.ComponentProps<typeof CollapsiblePrimitive.Root>) {
  return <CollapsiblePrimitive.Root data-slot="collapsible" {...props} />
}

function CollapsibleTrigger({
  ...props
}: React.ComponentProps<typeof CollapsiblePrimitive.CollapsibleTrigger>) {
  return (
    <CollapsiblePrimitive.CollapsibleTrigger
      data-slot="collapsible-trigger"
      {...props}
    />
  )
}

function CollapsibleContent({
  ...props
}: React.ComponentProps<typeof CollapsiblePrimitive.CollapsibleContent>) {
  return (
    <CollapsiblePrimitive.CollapsibleContent
      data-slot="collapsible-content"
      {...props}
    />
  )
}

export { Collapsible, CollapsibleTrigger, CollapsibleContent }
```

## File: `components/ui/command.tsx`
```tsx
"use client"

import * as React from "react"
import { Command as CommandPrimitive } from "cmdk"
import { SearchIcon } from "lucide-react"

import { cn } from "@/lib/utils"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog"

function Command({
  className,
  ...props
}: React.ComponentProps<typeof CommandPrimitive>) {
  return (
    <CommandPrimitive
      data-slot="command"
      className={cn(
        "bg-popover text-popover-foreground flex h-full w-full flex-col overflow-hidden rounded-md",
        className
      )}
      {...props}
    />
  )
}

function CommandDialog({
  title = "Command Palette",
  description = "Search for a command to run...",
  children,
  ...props
}: React.ComponentProps<typeof Dialog> & {
  title?: string
  description?: string
}) {
  return (
    <Dialog {...props}>
      <DialogHeader className="sr-only">
        <DialogTitle>{title}</DialogTitle>
        <DialogDescription>{description}</DialogDescription>
      </DialogHeader>
      <DialogContent className="overflow-hidden p-0">
        <Command className="[&_[cmdk-group-heading]]:text-muted-foreground **:data-[slot=command-input-wrapper]:h-12 [&_[cmdk-group-heading]]:px-2 [&_[cmdk-group-heading]]:font-medium [&_[cmdk-group]]:px-2 [&_[cmdk-group]:not([hidden])_~[cmdk-group]]:pt-0 [&_[cmdk-input-wrapper]_svg]:h-5 [&_[cmdk-input-wrapper]_svg]:w-5 [&_[cmdk-input]]:h-12 [&_[cmdk-item]]:px-2 [&_[cmdk-item]]:py-3 [&_[cmdk-item]_svg]:h-5 [&_[cmdk-item]_svg]:w-5">
          {children}
        </Command>
      </DialogContent>
    </Dialog>
  )
}

function CommandInput({
  className,
  ...props
}: React.ComponentProps<typeof CommandPrimitive.Input>) {
  return (
    <div
      data-slot="command-input-wrapper"
      className="flex h-9 items-center gap-2 border-b px-3"
    >
      <SearchIcon className="size-4 shrink-0 opacity-50" />
      <CommandPrimitive.Input
        data-slot="command-input"
        className={cn(
          "placeholder:text-muted-foreground flex h-10 w-full rounded-md bg-transparent py-3 text-sm outline-hidden disabled:cursor-not-allowed disabled:opacity-50",
          className
        )}
        {...props}
      />
    </div>
  )
}

function CommandList({
  className,
  ...props
}: React.ComponentProps<typeof CommandPrimitive.List>) {
  return (
    <CommandPrimitive.List
      data-slot="command-list"
      className={cn(
        "max-h-[300px] scroll-py-1 overflow-x-hidden overflow-y-auto",
        className
      )}
      {...props}
    />
  )
}

function CommandEmpty({
  ...props
}: React.ComponentProps<typeof CommandPrimitive.Empty>) {
  return (
    <CommandPrimitive.Empty
      data-slot="command-empty"
      className="py-6 text-center text-sm"
      {...props}
    />
  )
}

function CommandGroup({
  className,
  ...props
}: React.ComponentProps<typeof CommandPrimitive.Group>) {
  return (
    <CommandPrimitive.Group
      data-slot="command-group"
      className={cn(
        "text-foreground [&_[cmdk-group-heading]]:text-muted-foreground overflow-hidden p-1 [&_[cmdk-group-heading]]:px-2 [&_[cmdk-group-heading]]:py-1.5 [&_[cmdk-group-heading]]:text-xs [&_[cmdk-group-heading]]:font-medium",
        className
      )}
      {...props}
    />
  )
}

function CommandSeparator({
  className,
  ...props
}: React.ComponentProps<typeof CommandPrimitive.Separator>) {
  return (
    <CommandPrimitive.Separator
      data-slot="command-separator"
      className={cn("bg-border -mx-1 h-px", className)}
      {...props}
    />
  )
}

function CommandItem({
  className,
  ...props
}: React.ComponentProps<typeof CommandPrimitive.Item>) {
  return (
    <CommandPrimitive.Item
      data-slot="command-item"
      className={cn(
        "data-[selected=true]:bg-accent data-[selected=true]:text-accent-foreground [&_svg:not([class*='text-'])]:text-muted-foreground relative flex cursor-default items-center gap-2 rounded-sm px-2 py-1.5 text-sm outline-hidden select-none data-[disabled=true]:pointer-events-none data-[disabled=true]:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
        className
      )}
      {...props}
    />
  )
}

function CommandShortcut({
  className,
  ...props
}: React.ComponentProps<"span">) {
  return (
    <span
      data-slot="command-shortcut"
      className={cn(
        "text-muted-foreground ml-auto text-xs tracking-widest",
        className
      )}
      {...props}
    />
  )
}

export {
  Command,
  CommandDialog,
  CommandInput,
  CommandList,
  CommandEmpty,
  CommandGroup,
  CommandItem,
  CommandShortcut,
  CommandSeparator,
}
```

## File: `components/ui/context-menu.tsx`
```tsx
"use client"

import * as React from "react"
import * as ContextMenuPrimitive from "@radix-ui/react-context-menu"
import { CheckIcon, ChevronRightIcon, CircleIcon } from "lucide-react"

import { cn } from "@/lib/utils"

function ContextMenu({
  ...props
}: React.ComponentProps<typeof ContextMenuPrimitive.Root>) {
  return <ContextMenuPrimitive.Root data-slot="context-menu" {...props} />
}

function ContextMenuTrigger({
  ...props
}: React.ComponentProps<typeof ContextMenuPrimitive.Trigger>) {
  return (
    <ContextMenuPrimitive.Trigger data-slot="context-menu-trigger" {...props} />
  )
}

function ContextMenuGroup({
  ...props
}: React.ComponentProps<typeof ContextMenuPrimitive.Group>) {
  return (
    <ContextMenuPrimitive.Group data-slot="context-menu-group" {...props} />
  )
}

function ContextMenuPortal({
  ...props
}: React.ComponentProps<typeof ContextMenuPrimitive.Portal>) {
  return (
    <ContextMenuPrimitive.Portal data-slot="context-menu-portal" {...props} />
  )
}

function ContextMenuSub({
  ...props
}: React.ComponentProps<typeof ContextMenuPrimitive.Sub>) {
  return <ContextMenuPrimitive.Sub data-slot="context-menu-sub" {...props} />
}

function ContextMenuRadioGroup({
  ...props
}: React.ComponentProps<typeof ContextMenuPrimitive.RadioGroup>) {
  return (
    <ContextMenuPrimitive.RadioGroup
      data-slot="context-menu-radio-group"
      {...props}
    />
  )
}

function ContextMenuSubTrigger({
  className,
  inset,
  children,
  ...props
}: React.ComponentProps<typeof ContextMenuPrimitive.SubTrigger> & {
  inset?: boolean
}) {
  return (
    <ContextMenuPrimitive.SubTrigger
      data-slot="context-menu-sub-trigger"
      data-inset={inset}
      className={cn(
        "focus:bg-accent focus:text-accent-foreground data-[state=open]:bg-accent data-[state=open]:text-accent-foreground flex cursor-default items-center rounded-sm px-2 py-1.5 text-sm outline-hidden select-none data-[inset]:pl-8 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
        className
      )}
      {...props}
    >
      {children}
      <ChevronRightIcon className="ml-auto" />
    </ContextMenuPrimitive.SubTrigger>
  )
}

function ContextMenuSubContent({
  className,
  ...props
}: React.ComponentProps<typeof ContextMenuPrimitive.SubContent>) {
  return (
    <ContextMenuPrimitive.SubContent
      data-slot="context-menu-sub-content"
      className={cn(
        "bg-popover text-popover-foreground data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 z-50 min-w-[8rem] origin-(--radix-context-menu-content-transform-origin) overflow-hidden rounded-md border p-1 shadow-lg",
        className
      )}
      {...props}
    />
  )
}

function ContextMenuContent({
  className,
  ...props
}: React.ComponentProps<typeof ContextMenuPrimitive.Content>) {
  return (
    <ContextMenuPrimitive.Portal>
      <ContextMenuPrimitive.Content
        data-slot="context-menu-content"
        className={cn(
          "bg-popover text-popover-foreground data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 z-50 max-h-(--radix-context-menu-content-available-height) min-w-[8rem] origin-(--radix-context-menu-content-transform-origin) overflow-x-hidden overflow-y-auto rounded-md border p-1 shadow-md",
          className
        )}
        {...props}
      />
    </ContextMenuPrimitive.Portal>
  )
}

function ContextMenuItem({
  className,
  inset,
  variant = "default",
  ...props
}: React.ComponentProps<typeof ContextMenuPrimitive.Item> & {
  inset?: boolean
  variant?: "default" | "destructive"
}) {
  return (
    <ContextMenuPrimitive.Item
      data-slot="context-menu-item"
      data-inset={inset}
      data-variant={variant}
      className={cn(
        "focus:bg-accent focus:text-accent-foreground data-[variant=destructive]:text-destructive data-[variant=destructive]:focus:bg-destructive/10 dark:data-[variant=destructive]:focus:bg-destructive/20 data-[variant=destructive]:focus:text-destructive data-[variant=destructive]:*:[svg]:!text-destructive [&_svg:not([class*='text-'])]:text-muted-foreground relative flex cursor-default items-center gap-2 rounded-sm px-2 py-1.5 text-sm outline-hidden select-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 data-[inset]:pl-8 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
        className
      )}
      {...props}
    />
  )
}

function ContextMenuCheckboxItem({
  className,
  children,
  checked,
  ...props
}: React.ComponentProps<typeof ContextMenuPrimitive.CheckboxItem>) {
  return (
    <ContextMenuPrimitive.CheckboxItem
      data-slot="context-menu-checkbox-item"
      className={cn(
        "focus:bg-accent focus:text-accent-foreground relative flex cursor-default items-center gap-2 rounded-sm py-1.5 pr-2 pl-8 text-sm outline-hidden select-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
        className
      )}
      checked={checked}
      {...props}
    >
      <span className="pointer-events-none absolute left-2 flex size-3.5 items-center justify-center">
        <ContextMenuPrimitive.ItemIndicator>
          <CheckIcon className="size-4" />
        </ContextMenuPrimitive.ItemIndicator>
      </span>
      {children}
    </ContextMenuPrimitive.CheckboxItem>
  )
}

function ContextMenuRadioItem({
  className,
  children,
  ...props
}: React.ComponentProps<typeof ContextMenuPrimitive.RadioItem>) {
  return (
    <ContextMenuPrimitive.RadioItem
      data-slot="context-menu-radio-item"
      className={cn(
        "focus:bg-accent focus:text-accent-foreground relative flex cursor-default items-center gap-2 rounded-sm py-1.5 pr-2 pl-8 text-sm outline-hidden select-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
        className
      )}
      {...props}
    >
      <span className="pointer-events-none absolute left-2 flex size-3.5 items-center justify-center">
        <ContextMenuPrimitive.ItemIndicator>
          <CircleIcon className="size-2 fill-current" />
        </ContextMenuPrimitive.ItemIndicator>
      </span>
      {children}
    </ContextMenuPrimitive.RadioItem>
  )
}

function ContextMenuLabel({
  className,
  inset,
  ...props
}: React.ComponentProps<typeof ContextMenuPrimitive.Label> & {
  inset?: boolean
}) {
  return (
    <ContextMenuPrimitive.Label
      data-slot="context-menu-label"
      data-inset={inset}
      className={cn(
        "text-foreground px-2 py-1.5 text-sm font-medium data-[inset]:pl-8",
        className
      )}
      {...props}
    />
  )
}

function ContextMenuSeparator({
  className,
  ...props
}: React.ComponentProps<typeof ContextMenuPrimitive.Separator>) {
  return (
    <ContextMenuPrimitive.Separator
      data-slot="context-menu-separator"
      className={cn("bg-border -mx-1 my-1 h-px", className)}
      {...props}
    />
  )
}

function ContextMenuShortcut({
  className,
  ...props
}: React.ComponentProps<"span">) {
  return (
    <span
      data-slot="context-menu-shortcut"
      className={cn(
        "text-muted-foreground ml-auto text-xs tracking-widest",
        className
      )}
      {...props}
    />
  )
}

export {
  ContextMenu,
  ContextMenuTrigger,
  ContextMenuContent,
  ContextMenuItem,
  ContextMenuCheckboxItem,
  ContextMenuRadioItem,
  ContextMenuLabel,
  ContextMenuSeparator,
  ContextMenuShortcut,
  ContextMenuGroup,
  ContextMenuPortal,
  ContextMenuSub,
  ContextMenuSubContent,
  ContextMenuSubTrigger,
  ContextMenuRadioGroup,
}
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

## File: `components/ui/drawer.tsx`
```tsx
"use client"

import * as React from "react"
import { Drawer as DrawerPrimitive } from "vaul"

import { cn } from "@/lib/utils"

function Drawer({
  ...props
}: React.ComponentProps<typeof DrawerPrimitive.Root>) {
  return <DrawerPrimitive.Root data-slot="drawer" {...props} />
}

function DrawerTrigger({
  ...props
}: React.ComponentProps<typeof DrawerPrimitive.Trigger>) {
  return <DrawerPrimitive.Trigger data-slot="drawer-trigger" {...props} />
}

function DrawerPortal({
  ...props
}: React.ComponentProps<typeof DrawerPrimitive.Portal>) {
  return <DrawerPrimitive.Portal data-slot="drawer-portal" {...props} />
}

function DrawerClose({
  ...props
}: React.ComponentProps<typeof DrawerPrimitive.Close>) {
  return <DrawerPrimitive.Close data-slot="drawer-close" {...props} />
}

function DrawerOverlay({
  className,
  ...props
}: React.ComponentProps<typeof DrawerPrimitive.Overlay>) {
  return (
    <DrawerPrimitive.Overlay
      data-slot="drawer-overlay"
      className={cn(
        "data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 fixed inset-0 z-50 bg-black/50",
        className
      )}
      {...props}
    />
  )
}

function DrawerContent({
  className,
  children,
  ...props
}: React.ComponentProps<typeof DrawerPrimitive.Content>) {
  return (
    <DrawerPortal data-slot="drawer-portal">
      <DrawerOverlay />
      <DrawerPrimitive.Content
        data-slot="drawer-content"
        className={cn(
          "group/drawer-content bg-background fixed z-50 flex h-auto flex-col",
          "data-[vaul-drawer-direction=top]:inset-x-0 data-[vaul-drawer-direction=top]:top-0 data-[vaul-drawer-direction=top]:mb-24 data-[vaul-drawer-direction=top]:max-h-[80vh] data-[vaul-drawer-direction=top]:rounded-b-lg data-[vaul-drawer-direction=top]:border-b",
          "data-[vaul-drawer-direction=bottom]:inset-x-0 data-[vaul-drawer-direction=bottom]:bottom-0 data-[vaul-drawer-direction=bottom]:mt-24 data-[vaul-drawer-direction=bottom]:max-h-[80vh] data-[vaul-drawer-direction=bottom]:rounded-t-lg data-[vaul-drawer-direction=bottom]:border-t",
          "data-[vaul-drawer-direction=right]:inset-y-0 data-[vaul-drawer-direction=right]:right-0 data-[vaul-drawer-direction=right]:w-3/4 data-[vaul-drawer-direction=right]:border-l data-[vaul-drawer-direction=right]:sm:max-w-sm",
          "data-[vaul-drawer-direction=left]:inset-y-0 data-[vaul-drawer-direction=left]:left-0 data-[vaul-drawer-direction=left]:w-3/4 data-[vaul-drawer-direction=left]:border-r data-[vaul-drawer-direction=left]:sm:max-w-sm",
          className
        )}
        {...props}
      >
        <div className="bg-muted mx-auto mt-4 hidden h-2 w-[100px] shrink-0 rounded-full group-data-[vaul-drawer-direction=bottom]/drawer-content:block" />
        {children}
      </DrawerPrimitive.Content>
    </DrawerPortal>
  )
}

function DrawerHeader({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="drawer-header"
      className={cn("flex flex-col gap-1.5 p-4", className)}
      {...props}
    />
  )
}

function DrawerFooter({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="drawer-footer"
      className={cn("mt-auto flex flex-col gap-2 p-4", className)}
      {...props}
    />
  )
}

function DrawerTitle({
  className,
  ...props
}: React.ComponentProps<typeof DrawerPrimitive.Title>) {
  return (
    <DrawerPrimitive.Title
      data-slot="drawer-title"
      className={cn("text-foreground font-semibold", className)}
      {...props}
    />
  )
}

function DrawerDescription({
  className,
  ...props
}: React.ComponentProps<typeof DrawerPrimitive.Description>) {
  return (
    <DrawerPrimitive.Description
      data-slot="drawer-description"
      className={cn("text-muted-foreground text-sm", className)}
      {...props}
    />
  )
}

export {
  Drawer,
  DrawerPortal,
  DrawerOverlay,
  DrawerTrigger,
  DrawerClose,
  DrawerContent,
  DrawerHeader,
  DrawerFooter,
  DrawerTitle,
  DrawerDescription,
}
```

## File: `components/ui/dropdown-menu.tsx`
```tsx
"use client"

import * as React from "react"
import * as DropdownMenuPrimitive from "@radix-ui/react-dropdown-menu"
import { CheckIcon, ChevronRightIcon, CircleIcon } from "lucide-react"

import { cn } from "@/lib/utils"

function DropdownMenu({
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Root>) {
  return <DropdownMenuPrimitive.Root data-slot="dropdown-menu" {...props} />
}

function DropdownMenuPortal({
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Portal>) {
  return (
    <DropdownMenuPrimitive.Portal data-slot="dropdown-menu-portal" {...props} />
  )
}

function DropdownMenuTrigger({
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Trigger>) {
  return (
    <DropdownMenuPrimitive.Trigger
      data-slot="dropdown-menu-trigger"
      {...props}
    />
  )
}

function DropdownMenuContent({
  className,
  sideOffset = 4,
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Content>) {
  return (
    <DropdownMenuPrimitive.Portal>
      <DropdownMenuPrimitive.Content
        data-slot="dropdown-menu-content"
        sideOffset={sideOffset}
        className={cn(
          "bg-popover text-popover-foreground data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 z-50 max-h-(--radix-dropdown-menu-content-available-height) min-w-[8rem] origin-(--radix-dropdown-menu-content-transform-origin) overflow-x-hidden overflow-y-auto rounded-md border p-1 shadow-md",
          className
        )}
        {...props}
      />
    </DropdownMenuPrimitive.Portal>
  )
}

function DropdownMenuGroup({
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Group>) {
  return (
    <DropdownMenuPrimitive.Group data-slot="dropdown-menu-group" {...props} />
  )
}

function DropdownMenuItem({
  className,
  inset,
  variant = "default",
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Item> & {
  inset?: boolean
  variant?: "default" | "destructive"
}) {
  return (
    <DropdownMenuPrimitive.Item
      data-slot="dropdown-menu-item"
      data-inset={inset}
      data-variant={variant}
      className={cn(
        "focus:bg-accent focus:text-accent-foreground data-[variant=destructive]:text-destructive data-[variant=destructive]:focus:bg-destructive/10 dark:data-[variant=destructive]:focus:bg-destructive/20 data-[variant=destructive]:focus:text-destructive data-[variant=destructive]:*:[svg]:!text-destructive [&_svg:not([class*='text-'])]:text-muted-foreground relative flex cursor-default items-center gap-2 rounded-sm px-2 py-1.5 text-sm outline-hidden select-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 data-[inset]:pl-8 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
        className
      )}
      {...props}
    />
  )
}

function DropdownMenuCheckboxItem({
  className,
  children,
  checked,
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.CheckboxItem>) {
  return (
    <DropdownMenuPrimitive.CheckboxItem
      data-slot="dropdown-menu-checkbox-item"
      className={cn(
        "focus:bg-accent focus:text-accent-foreground relative flex cursor-default items-center gap-2 rounded-sm py-1.5 pr-2 pl-8 text-sm outline-hidden select-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
        className
      )}
      checked={checked}
      {...props}
    >
      <span className="pointer-events-none absolute left-2 flex size-3.5 items-center justify-center">
        <DropdownMenuPrimitive.ItemIndicator>
          <CheckIcon className="size-4" />
        </DropdownMenuPrimitive.ItemIndicator>
      </span>
      {children}
    </DropdownMenuPrimitive.CheckboxItem>
  )
}

function DropdownMenuRadioGroup({
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.RadioGroup>) {
  return (
    <DropdownMenuPrimitive.RadioGroup
      data-slot="dropdown-menu-radio-group"
      {...props}
    />
  )
}

function DropdownMenuRadioItem({
  className,
  children,
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.RadioItem>) {
  return (
    <DropdownMenuPrimitive.RadioItem
      data-slot="dropdown-menu-radio-item"
      className={cn(
        "focus:bg-accent focus:text-accent-foreground relative flex cursor-default items-center gap-2 rounded-sm py-1.5 pr-2 pl-8 text-sm outline-hidden select-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
        className
      )}
      {...props}
    >
      <span className="pointer-events-none absolute left-2 flex size-3.5 items-center justify-center">
        <DropdownMenuPrimitive.ItemIndicator>
          <CircleIcon className="size-2 fill-current" />
        </DropdownMenuPrimitive.ItemIndicator>
      </span>
      {children}
    </DropdownMenuPrimitive.RadioItem>
  )
}

function DropdownMenuLabel({
  className,
  inset,
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Label> & {
  inset?: boolean
}) {
  return (
    <DropdownMenuPrimitive.Label
      data-slot="dropdown-menu-label"
      data-inset={inset}
      className={cn(
        "px-2 py-1.5 text-sm font-medium data-[inset]:pl-8",
        className
      )}
      {...props}
    />
  )
}

function DropdownMenuSeparator({
  className,
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Separator>) {
  return (
    <DropdownMenuPrimitive.Separator
      data-slot="dropdown-menu-separator"
      className={cn("bg-border -mx-1 my-1 h-px", className)}
      {...props}
    />
  )
}

function DropdownMenuShortcut({
  className,
  ...props
}: React.ComponentProps<"span">) {
  return (
    <span
      data-slot="dropdown-menu-shortcut"
      className={cn(
        "text-muted-foreground ml-auto text-xs tracking-widest",
        className
      )}
      {...props}
    />
  )
}

function DropdownMenuSub({
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Sub>) {
  return <DropdownMenuPrimitive.Sub data-slot="dropdown-menu-sub" {...props} />
}

function DropdownMenuSubTrigger({
  className,
  inset,
  children,
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.SubTrigger> & {
  inset?: boolean
}) {
  return (
    <DropdownMenuPrimitive.SubTrigger
      data-slot="dropdown-menu-sub-trigger"
      data-inset={inset}
      className={cn(
        "focus:bg-accent focus:text-accent-foreground data-[state=open]:bg-accent data-[state=open]:text-accent-foreground flex cursor-default items-center rounded-sm px-2 py-1.5 text-sm outline-hidden select-none data-[inset]:pl-8",
        className
      )}
      {...props}
    >
      {children}
      <ChevronRightIcon className="ml-auto size-4" />
    </DropdownMenuPrimitive.SubTrigger>
  )
}

function DropdownMenuSubContent({
  className,
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.SubContent>) {
  return (
    <DropdownMenuPrimitive.SubContent
      data-slot="dropdown-menu-sub-content"
      className={cn(
        "bg-popover text-popover-foreground data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 z-50 min-w-[8rem] origin-(--radix-dropdown-menu-content-transform-origin) overflow-hidden rounded-md border p-1 shadow-lg",
        className
      )}
      {...props}
    />
  )
}

export {
  DropdownMenu,
  DropdownMenuPortal,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuLabel,
  DropdownMenuItem,
  DropdownMenuCheckboxItem,
  DropdownMenuRadioGroup,
  DropdownMenuRadioItem,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuSub,
  DropdownMenuSubTrigger,
  DropdownMenuSubContent,
}
```

## File: `components/ui/form.tsx`
```tsx
"use client"

import * as React from "react"
import * as LabelPrimitive from "@radix-ui/react-label"
import { Slot } from "@radix-ui/react-slot"
import {
  Controller,
  FormProvider,
  useFormContext,
  useFormState,
  type ControllerProps,
  type FieldPath,
  type FieldValues,
} from "react-hook-form"

import { cn } from "@/lib/utils"
import { Label } from "@/components/ui/label"

const Form = FormProvider

type FormFieldContextValue<
  TFieldValues extends FieldValues = FieldValues,
  TName extends FieldPath<TFieldValues> = FieldPath<TFieldValues>,
> = {
  name: TName
}

const FormFieldContext = React.createContext<FormFieldContextValue>(
  {} as FormFieldContextValue
)

const FormField = <
  TFieldValues extends FieldValues = FieldValues,
  TName extends FieldPath<TFieldValues> = FieldPath<TFieldValues>,
>({
  ...props
}: ControllerProps<TFieldValues, TName>) => {
  return (
    <FormFieldContext.Provider value={{ name: props.name }}>
      <Controller {...props} />
    </FormFieldContext.Provider>
  )
}

const useFormField = () => {
  const fieldContext = React.useContext(FormFieldContext)
  const itemContext = React.useContext(FormItemContext)
  const { getFieldState } = useFormContext()
  const formState = useFormState({ name: fieldContext.name })
  const fieldState = getFieldState(fieldContext.name, formState)

  if (!fieldContext) {
    throw new Error("useFormField should be used within <FormField>")
  }

  const { id } = itemContext

  return {
    id,
    name: fieldContext.name,
    formItemId: `${id}-form-item`,
    formDescriptionId: `${id}-form-item-description`,
    formMessageId: `${id}-form-item-message`,
    ...fieldState,
  }
}

type FormItemContextValue = {
  id: string
}

const FormItemContext = React.createContext<FormItemContextValue>(
  {} as FormItemContextValue
)

function FormItem({ className, ...props }: React.ComponentProps<"div">) {
  const id = React.useId()

  return (
    <FormItemContext.Provider value={{ id }}>
      <div
        data-slot="form-item"
        className={cn("grid gap-2", className)}
        {...props}
      />
    </FormItemContext.Provider>
  )
}

function FormLabel({
  className,
  ...props
}: React.ComponentProps<typeof LabelPrimitive.Root>) {
  const { error, formItemId } = useFormField()

  return (
    <Label
      data-slot="form-label"
      data-error={!!error}
      className={cn("data-[error=true]:text-destructive", className)}
      htmlFor={formItemId}
      {...props}
    />
  )
}

function FormControl({ ...props }: React.ComponentProps<typeof Slot>) {
  const { error, formItemId, formDescriptionId, formMessageId } = useFormField()

  return (
    <Slot
      data-slot="form-control"
      id={formItemId}
      aria-describedby={
        !error
          ? `${formDescriptionId}`
          : `${formDescriptionId} ${formMessageId}`
      }
      aria-invalid={!!error}
      {...props}
    />
  )
}

function FormDescription({ className, ...props }: React.ComponentProps<"p">) {
  const { formDescriptionId } = useFormField()

  return (
    <p
      data-slot="form-description"
      id={formDescriptionId}
      className={cn("text-muted-foreground text-sm", className)}
      {...props}
    />
  )
}

function FormMessage({ className, ...props }: React.ComponentProps<"p">) {
  const { error, formMessageId } = useFormField()
  const body = error ? String(error?.message ?? "") : props.children

  if (!body) {
    return null
  }

  return (
    <p
      data-slot="form-message"
      id={formMessageId}
      className={cn("text-destructive text-sm", className)}
      {...props}
    >
      {body}
    </p>
  )
}

export {
  useFormField,
  Form,
  FormItem,
  FormLabel,
  FormControl,
  FormDescription,
  FormMessage,
  FormField,
}
```

## File: `components/ui/hover-card.tsx`
```tsx
"use client"

import * as React from "react"
import * as HoverCardPrimitive from "@radix-ui/react-hover-card"

import { cn } from "@/lib/utils"

function HoverCard({
  ...props
}: React.ComponentProps<typeof HoverCardPrimitive.Root>) {
  return <HoverCardPrimitive.Root data-slot="hover-card" {...props} />
}

function HoverCardTrigger({
  ...props
}: React.ComponentProps<typeof HoverCardPrimitive.Trigger>) {
  return (
    <HoverCardPrimitive.Trigger data-slot="hover-card-trigger" {...props} />
  )
}

function HoverCardContent({
  className,
  align = "center",
  sideOffset = 4,
  ...props
}: React.ComponentProps<typeof HoverCardPrimitive.Content>) {
  return (
    <HoverCardPrimitive.Portal data-slot="hover-card-portal">
      <HoverCardPrimitive.Content
        data-slot="hover-card-content"
        align={align}
        sideOffset={sideOffset}
        className={cn(
          "bg-popover text-popover-foreground data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 z-50 w-64 origin-(--radix-hover-card-content-transform-origin) rounded-md border p-4 shadow-md outline-hidden",
          className
        )}
        {...props}
      />
    </HoverCardPrimitive.Portal>
  )
}

export { HoverCard, HoverCardTrigger, HoverCardContent }
```

## File: `components/ui/input-otp.tsx`
```tsx
"use client"

import * as React from "react"
import { OTPInput, OTPInputContext } from "input-otp"
import { MinusIcon } from "lucide-react"

import { cn } from "@/lib/utils"

function InputOTP({
  className,
  containerClassName,
  ...props
}: React.ComponentProps<typeof OTPInput> & {
  containerClassName?: string
}) {
  return (
    <OTPInput
      data-slot="input-otp"
      containerClassName={cn(
        "flex items-center gap-2 has-disabled:opacity-50",
        containerClassName
      )}
      className={cn("disabled:cursor-not-allowed", className)}
      {...props}
    />
  )
}

function InputOTPGroup({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="input-otp-group"
      className={cn("flex items-center", className)}
      {...props}
    />
  )
}

function InputOTPSlot({
  index,
  className,
  ...props
}: React.ComponentProps<"div"> & {
  index: number
}) {
  const inputOTPContext = React.useContext(OTPInputContext)
  const { char, hasFakeCaret, isActive } = inputOTPContext?.slots[index] ?? {}

  return (
    <div
      data-slot="input-otp-slot"
      data-active={isActive}
      className={cn(
        "data-[active=true]:border-ring data-[active=true]:ring-ring/50 data-[active=true]:aria-invalid:ring-destructive/20 dark:data-[active=true]:aria-invalid:ring-destructive/40 aria-invalid:border-destructive data-[active=true]:aria-invalid:border-destructive dark:bg-input/30 border-input relative flex h-9 w-9 items-center justify-center border-y border-r text-sm shadow-xs transition-all outline-none first:rounded-l-md first:border-l last:rounded-r-md data-[active=true]:z-10 data-[active=true]:ring-[3px]",
        className
      )}
      {...props}
    >
      {char}
      {hasFakeCaret && (
        <div className="pointer-events-none absolute inset-0 flex items-center justify-center">
          <div className="animate-caret-blink bg-foreground h-4 w-px duration-1000" />
        </div>
      )}
    </div>
  )
}

function InputOTPSeparator({ ...props }: React.ComponentProps<"div">) {
  return (
    <div data-slot="input-otp-separator" role="separator" {...props}>
      <MinusIcon />
    </div>
  )
}

export { InputOTP, InputOTPGroup, InputOTPSlot, InputOTPSeparator }
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
        "focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-1",
        "aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive",
        className
      )}
      {...props}
    />
  )
}

export { Input }
```

## File: `components/ui/label.tsx`
```tsx
"use client"

import * as React from "react"
import * as LabelPrimitive from "@radix-ui/react-label"

import { cn } from "@/lib/utils"

function Label({
  className,
  ...props
}: React.ComponentProps<typeof LabelPrimitive.Root>) {
  return (
    <LabelPrimitive.Root
      data-slot="label"
      className={cn(
        "flex items-center gap-2 text-sm leading-none font-medium select-none group-data-[disabled=true]:pointer-events-none group-data-[disabled=true]:opacity-50 peer-disabled:cursor-not-allowed peer-disabled:opacity-50",
        className
      )}
      {...props}
    />
  )
}

export { Label }
```

## File: `components/ui/logo.tsx`
```tsx
// FirecrawlLogo.tsx
import * as React from "react";
import flame from "../../public/assets/twemoji-fire.svg";   // 1️⃣ add the Twemoji file to src/ (2 KB, CC-BY 4.0)

export default function FirecrawlLogo({
  className = "",
  style,
  ...rest
}: React.SVGProps<SVGSVGElement>) {
  return (
    <svg
      width={2907}
      height={600}
      viewBox="0 0 2907 600"
      xmlns="http://www.w3.org/2000/svg"
      className={`h-auto w-full max-w-md ${className}`}
      style={{ maxHeight: 150, ...style }}
      {...rest}
    >
      <switch>
        <foreignObject
          x="0"
          y="0"
          width="600"
          height="600"
          requiredExtensions="http://www.w3.org/1999/xhtml"
        >
          <div
            style={{ fontSize: 600, lineHeight: 1 }}
          >
            🔥
          </div>
        </foreignObject>

        <image href={flame} x="0" y="0" width="600" height="600" />
      </switch>

      <path
        d="M768.456 483V119.364H993.953V166.594H823.321V277.389H977.796V324.442H823.321V483H768.456ZM1052.16 483V210.273H1105.25V483H1052.16ZM1078.97 168.192C1069.74 168.192 1061.81 165.114 1055.18 158.959C1048.67 152.685 1045.42 145.228 1045.42 136.587C1045.42 127.827 1048.67 120.37 1055.18 114.214C1061.81 107.941 1069.74 104.804 1078.97 104.804C1088.21 104.804 1096.08 107.941 1102.59 114.214C1109.22 120.37 1112.53 127.827 1112.53 136.587C1112.53 145.228 1109.22 152.685 1102.59 158.959C1096.08 165.114 1088.21 168.192 1078.97 168.192ZM1171.68 483V210.273H1222.99V253.597H1225.83C1230.8 238.919 1239.56 227.377 1252.11 218.973C1264.77 210.45 1279.1 206.189 1295.08 206.189C1298.39 206.189 1302.3 206.307 1306.8 206.544C1311.41 206.781 1315.02 207.077 1317.63 207.432V258.213C1315.5 257.621 1311.71 256.97 1306.26 256.26C1300.82 255.431 1295.37 255.017 1289.93 255.017C1277.38 255.017 1266.19 257.68 1256.37 263.007C1246.66 268.215 1238.97 275.495 1233.29 284.847C1227.61 294.08 1224.76 304.615 1224.76 316.452V483H1171.68ZM1466.35 488.504C1439.48 488.504 1416.33 482.763 1396.92 471.281C1377.63 459.681 1362.71 443.405 1352.18 422.453C1341.76 401.383 1336.55 376.703 1336.55 348.412C1336.55 320.476 1341.76 295.855 1352.18 274.548C1362.71 253.241 1377.39 236.61 1396.21 224.655C1415.15 212.699 1437.29 206.722 1462.62 206.722C1478.01 206.722 1492.92 209.267 1507.36 214.357C1521.8 219.446 1534.77 227.437 1546.25 238.327C1557.73 249.217 1566.78 263.362 1573.41 280.763C1580.04 298.045 1583.36 319.056 1583.36 343.795V362.616H1366.56V322.844H1531.33C1531.33 308.876 1528.49 296.506 1522.81 285.734C1517.13 274.844 1509.14 266.262 1498.84 259.989C1488.66 253.715 1476.7 250.578 1462.97 250.578C1448.06 250.578 1435.04 254.248 1423.91 261.587C1412.9 268.807 1404.38 278.277 1398.34 289.996C1392.42 301.596 1389.46 314.203 1389.46 327.815V358.888C1389.46 377.117 1392.66 392.624 1399.05 405.408C1405.56 418.192 1414.62 427.957 1426.22 434.705C1437.82 441.333 1451.37 444.648 1466.88 444.648C1476.94 444.648 1486.11 443.227 1494.4 440.386C1502.69 437.427 1509.85 433.047 1515.89 427.247C1521.92 421.447 1526.54 414.286 1529.73 405.763L1579.98 414.818C1575.96 429.615 1568.74 442.576 1558.32 453.703C1548.02 464.712 1535.06 473.294 1519.44 479.449C1503.93 485.486 1486.23 488.504 1466.35 488.504ZM1752.14 488.504C1725.74 488.504 1703.02 482.527 1683.96 470.571C1665.02 458.497 1650.46 441.866 1640.28 420.678C1630.1 399.489 1625.01 375.223 1625.01 347.879C1625.01 320.18 1630.22 295.737 1640.63 274.548C1651.05 253.241 1665.73 236.61 1684.67 224.655C1703.61 212.699 1725.92 206.722 1751.61 206.722C1772.32 206.722 1790.79 210.569 1807.01 218.263C1823.22 225.839 1836.3 236.492 1846.25 250.223C1856.31 263.954 1862.28 279.993 1864.18 298.341H1812.51C1809.67 285.557 1803.16 274.548 1792.98 265.315C1782.92 256.082 1769.42 251.466 1752.5 251.466C1737.7 251.466 1724.74 255.372 1713.61 263.185C1702.6 270.879 1694.02 281.887 1687.86 296.21C1681.71 310.415 1678.63 327.223 1678.63 346.636C1678.63 366.523 1681.65 383.687 1687.69 398.128C1693.72 412.569 1702.25 423.755 1713.26 431.686C1724.38 439.617 1737.46 443.582 1752.5 443.582C1762.56 443.582 1771.67 441.748 1779.84 438.078C1788.13 434.29 1795.05 428.904 1800.61 421.92C1806.3 414.937 1810.26 406.532 1812.51 396.707H1864.18C1862.28 414.345 1856.54 430.088 1846.96 443.938C1837.37 457.787 1824.52 468.677 1808.43 476.608C1792.45 484.539 1773.68 488.504 1752.14 488.504ZM1915.95 483V210.273H1967.27V253.597H1970.11C1975.08 238.919 1983.84 227.377 1996.39 218.973C2009.05 210.45 2023.37 206.189 2039.35 206.189C2042.67 206.189 2046.58 206.307 2051.07 206.544C2055.69 206.781 2059.3 207.077 2061.9 207.432V258.213C2059.77 257.621 2055.99 256.97 2050.54 256.26C2045.1 255.431 2039.65 255.017 2034.21 255.017C2021.66 255.017 2010.47 257.68 2000.65 263.007C1990.94 268.215 1983.25 275.495 1977.56 284.847C1971.88 294.08 1969.04 304.615 1969.04 316.452V483H1915.95ZM2179.77 489.037C2162.49 489.037 2146.87 485.841 2132.9 479.449C2118.93 472.938 2107.86 463.528 2099.7 451.217C2091.65 438.907 2087.62 423.814 2087.62 405.94C2087.62 390.552 2090.58 377.886 2096.5 367.943C2102.42 358 2110.41 350.128 2120.47 344.328C2130.53 338.528 2141.78 334.148 2154.21 331.189C2166.63 328.23 2179.3 325.981 2192.2 324.442C2208.54 322.548 2221.8 321.009 2231.98 319.825C2242.16 318.523 2249.55 316.452 2254.17 313.611C2258.79 310.77 2261.09 306.153 2261.09 299.761V298.518C2261.09 283.012 2256.71 270.997 2247.96 262.474C2239.31 253.952 2226.41 249.69 2209.25 249.69C2191.37 249.69 2177.29 253.656 2166.99 261.587C2156.81 269.399 2149.77 278.099 2145.86 287.688L2095.97 276.324C2101.89 259.752 2110.53 246.376 2121.89 236.196C2133.37 225.898 2146.57 218.44 2161.49 213.824C2176.4 209.089 2192.08 206.722 2208.54 206.722C2219.43 206.722 2230.97 208.024 2243.16 210.628C2255.47 213.114 2266.95 217.73 2277.61 224.477C2288.38 231.224 2297.2 240.872 2304.06 253.419C2310.93 265.848 2314.36 282.006 2314.36 301.892V483H2262.52V445.713H2260.38C2256.95 452.579 2251.8 459.326 2244.94 465.955C2238.07 472.583 2229.25 478.088 2218.48 482.467C2207.71 486.847 2194.81 489.037 2179.77 489.037ZM2191.31 446.423C2205.99 446.423 2218.54 443.523 2228.96 437.723C2239.49 431.923 2247.48 424.347 2252.93 414.996C2258.49 405.526 2261.27 395.405 2261.27 384.634V349.477C2259.38 351.371 2255.71 353.147 2250.26 354.804C2244.94 356.343 2238.84 357.704 2231.98 358.888C2225.11 359.953 2218.42 360.959 2211.91 361.906C2205.4 362.735 2199.96 363.445 2195.58 364.037C2185.28 365.339 2175.87 367.529 2167.34 370.607C2158.94 373.684 2152.19 378.123 2147.1 383.923C2142.13 389.605 2139.65 397.181 2139.65 406.651C2139.65 419.79 2144.5 429.733 2154.21 436.48C2163.91 443.109 2176.28 446.423 2191.31 446.423ZM2439.2 483L2358.94 210.273H2413.81L2467.25 410.557H2469.92L2523.54 210.273H2578.4L2631.67 409.669H2634.34L2687.42 210.273H2742.29L2662.21 483H2608.06L2552.66 286.089H2548.58L2493.18 483H2439.2ZM2840.76 119.364V483H2787.67V119.364H2840.76Z"
        fill="#36322F"
      />
    </svg>
  );
}
```

## File: `components/ui/menubar.tsx`
```tsx
"use client"

import * as React from "react"
import * as MenubarPrimitive from "@radix-ui/react-menubar"
import { CheckIcon, ChevronRightIcon, CircleIcon } from "lucide-react"

import { cn } from "@/lib/utils"

function Menubar({
  className,
  ...props
}: React.ComponentProps<typeof MenubarPrimitive.Root>) {
  return (
    <MenubarPrimitive.Root
      data-slot="menubar"
      className={cn(
        "bg-background flex h-9 items-center gap-1 rounded-md border p-1 shadow-xs",
        className
      )}
      {...props}
    />
  )
}

function MenubarMenu({
  ...props
}: React.ComponentProps<typeof MenubarPrimitive.Menu>) {
  return <MenubarPrimitive.Menu data-slot="menubar-menu" {...props} />
}

function MenubarGroup({
  ...props
}: React.ComponentProps<typeof MenubarPrimitive.Group>) {
  return <MenubarPrimitive.Group data-slot="menubar-group" {...props} />
}

function MenubarPortal({
  ...props
}: React.ComponentProps<typeof MenubarPrimitive.Portal>) {
  return <MenubarPrimitive.Portal data-slot="menubar-portal" {...props} />
}

function MenubarRadioGroup({
  ...props
}: React.ComponentProps<typeof MenubarPrimitive.RadioGroup>) {
  return (
    <MenubarPrimitive.RadioGroup data-slot="menubar-radio-group" {...props} />
  )
}

function MenubarTrigger({
  className,
  ...props
}: React.ComponentProps<typeof MenubarPrimitive.Trigger>) {
  return (
    <MenubarPrimitive.Trigger
      data-slot="menubar-trigger"
      className={cn(
        "focus:bg-accent focus:text-accent-foreground data-[state=open]:bg-accent data-[state=open]:text-accent-foreground flex items-center rounded-sm px-2 py-1 text-sm font-medium outline-hidden select-none",
        className
      )}
      {...props}
    />
  )
}

function MenubarContent({
  className,
  align = "start",
  alignOffset = -4,
  sideOffset = 8,
  ...props
}: React.ComponentProps<typeof MenubarPrimitive.Content>) {
  return (
    <MenubarPortal>
      <MenubarPrimitive.Content
        data-slot="menubar-content"
        align={align}
        alignOffset={alignOffset}
        sideOffset={sideOffset}
        className={cn(
          "bg-popover text-popover-foreground data-[state=open]:animate-in data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 z-50 min-w-[12rem] origin-(--radix-menubar-content-transform-origin) overflow-hidden rounded-md border p-1 shadow-md",
          className
        )}
        {...props}
      />
    </MenubarPortal>
  )
}

function MenubarItem({
  className,
  inset,
  variant = "default",
  ...props
}: React.ComponentProps<typeof MenubarPrimitive.Item> & {
  inset?: boolean
  variant?: "default" | "destructive"
}) {
  return (
    <MenubarPrimitive.Item
      data-slot="menubar-item"
      data-inset={inset}
      data-variant={variant}
      className={cn(
        "focus:bg-accent focus:text-accent-foreground data-[variant=destructive]:text-destructive data-[variant=destructive]:focus:bg-destructive/10 dark:data-[variant=destructive]:focus:bg-destructive/20 data-[variant=destructive]:focus:text-destructive data-[variant=destructive]:*:[svg]:!text-destructive [&_svg:not([class*='text-'])]:text-muted-foreground relative flex cursor-default items-center gap-2 rounded-sm px-2 py-1.5 text-sm outline-hidden select-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 data-[inset]:pl-8 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
        className
      )}
      {...props}
    />
  )
}

function MenubarCheckboxItem({
  className,
  children,
  checked,
  ...props
}: React.ComponentProps<typeof MenubarPrimitive.CheckboxItem>) {
  return (
    <MenubarPrimitive.CheckboxItem
      data-slot="menubar-checkbox-item"
      className={cn(
        "focus:bg-accent focus:text-accent-foreground relative flex cursor-default items-center gap-2 rounded-xs py-1.5 pr-2 pl-8 text-sm outline-hidden select-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
        className
      )}
      checked={checked}
      {...props}
    >
      <span className="pointer-events-none absolute left-2 flex size-3.5 items-center justify-center">
        <MenubarPrimitive.ItemIndicator>
          <CheckIcon className="size-4" />
        </MenubarPrimitive.ItemIndicator>
      </span>
      {children}
    </MenubarPrimitive.CheckboxItem>
  )
}

function MenubarRadioItem({
  className,
  children,
  ...props
}: React.ComponentProps<typeof MenubarPrimitive.RadioItem>) {
  return (
    <MenubarPrimitive.RadioItem
      data-slot="menubar-radio-item"
      className={cn(
        "focus:bg-accent focus:text-accent-foreground relative flex cursor-default items-center gap-2 rounded-xs py-1.5 pr-2 pl-8 text-sm outline-hidden select-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
        className
      )}
      {...props}
    >
      <span className="pointer-events-none absolute left-2 flex size-3.5 items-center justify-center">
        <MenubarPrimitive.ItemIndicator>
          <CircleIcon className="size-2 fill-current" />
        </MenubarPrimitive.ItemIndicator>
      </span>
      {children}
    </MenubarPrimitive.RadioItem>
  )
}

function MenubarLabel({
  className,
  inset,
  ...props
}: React.ComponentProps<typeof MenubarPrimitive.Label> & {
  inset?: boolean
}) {
  return (
    <MenubarPrimitive.Label
      data-slot="menubar-label"
      data-inset={inset}
      className={cn(
        "px-2 py-1.5 text-sm font-medium data-[inset]:pl-8",
        className
      )}
      {...props}
    />
  )
}

function MenubarSeparator({
  className,
  ...props
}: React.ComponentProps<typeof MenubarPrimitive.Separator>) {
  return (
    <MenubarPrimitive.Separator
      data-slot="menubar-separator"
      className={cn("bg-border -mx-1 my-1 h-px", className)}
      {...props}
    />
  )
}

function MenubarShortcut({
  className,
  ...props
}: React.ComponentProps<"span">) {
  return (
    <span
      data-slot="menubar-shortcut"
      className={cn(
        "text-muted-foreground ml-auto text-xs tracking-widest",
        className
      )}
      {...props}
    />
  )
}

function MenubarSub({
  ...props
}: React.ComponentProps<typeof MenubarPrimitive.Sub>) {
  return <MenubarPrimitive.Sub data-slot="menubar-sub" {...props} />
}

function MenubarSubTrigger({
  className,
  inset,
  children,
  ...props
}: React.ComponentProps<typeof MenubarPrimitive.SubTrigger> & {
  inset?: boolean
}) {
  return (
    <MenubarPrimitive.SubTrigger
      data-slot="menubar-sub-trigger"
      data-inset={inset}
      className={cn(
        "focus:bg-accent focus:text-accent-foreground data-[state=open]:bg-accent data-[state=open]:text-accent-foreground flex cursor-default items-center rounded-sm px-2 py-1.5 text-sm outline-none select-none data-[inset]:pl-8",
        className
      )}
      {...props}
    >
      {children}
      <ChevronRightIcon className="ml-auto h-4 w-4" />
    </MenubarPrimitive.SubTrigger>
  )
}

function MenubarSubContent({
  className,
  ...props
}: React.ComponentProps<typeof MenubarPrimitive.SubContent>) {
  return (
    <MenubarPrimitive.SubContent
      data-slot="menubar-sub-content"
      className={cn(
        "bg-popover text-popover-foreground data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 z-50 min-w-[8rem] origin-(--radix-menubar-content-transform-origin) overflow-hidden rounded-md border p-1 shadow-lg",
        className
      )}
      {...props}
    />
  )
}

export {
  Menubar,
  MenubarPortal,
  MenubarMenu,
  MenubarTrigger,
  MenubarContent,
  MenubarGroup,
  MenubarSeparator,
  MenubarLabel,
  MenubarItem,
  MenubarShortcut,
  MenubarCheckboxItem,
  MenubarRadioGroup,
  MenubarRadioItem,
  MenubarSub,
  MenubarSubTrigger,
  MenubarSubContent,
}
```

## File: `components/ui/navigation-menu.tsx`
```tsx
import * as React from "react"
import * as NavigationMenuPrimitive from "@radix-ui/react-navigation-menu"
import { cva } from "class-variance-authority"
import { ChevronDownIcon } from "lucide-react"

import { cn } from "@/lib/utils"

function NavigationMenu({
  className,
  children,
  viewport = true,
  ...props
}: React.ComponentProps<typeof NavigationMenuPrimitive.Root> & {
  viewport?: boolean
}) {
  return (
    <NavigationMenuPrimitive.Root
      data-slot="navigation-menu"
      data-viewport={viewport}
      className={cn(
        "group/navigation-menu relative flex max-w-max flex-1 items-center justify-center",
        className
      )}
      {...props}
    >
      {children}
      {viewport && <NavigationMenuViewport />}
    </NavigationMenuPrimitive.Root>
  )
}

function NavigationMenuList({
  className,
  ...props
}: React.ComponentProps<typeof NavigationMenuPrimitive.List>) {
  return (
    <NavigationMenuPrimitive.List
      data-slot="navigation-menu-list"
      className={cn(
        "group flex flex-1 list-none items-center justify-center gap-1",
        className
      )}
      {...props}
    />
  )
}

function NavigationMenuItem({
  className,
  ...props
}: React.ComponentProps<typeof NavigationMenuPrimitive.Item>) {
  return (
    <NavigationMenuPrimitive.Item
      data-slot="navigation-menu-item"
      className={cn("relative", className)}
      {...props}
    />
  )
}

const navigationMenuTriggerStyle = cva(
  "group inline-flex h-9 w-max items-center justify-center rounded-md bg-background px-4 py-2 text-sm font-medium hover:bg-accent hover:text-accent-foreground focus:bg-accent focus:text-accent-foreground disabled:pointer-events-none disabled:opacity-50 data-[state=open]:hover:bg-accent data-[state=open]:text-accent-foreground data-[state=open]:focus:bg-accent data-[state=open]:bg-accent/50 focus-visible:ring-ring/50 outline-none transition-[color,box-shadow] focus-visible:ring-[3px] focus-visible:outline-1"
)

function NavigationMenuTrigger({
  className,
  children,
  ...props
}: React.ComponentProps<typeof NavigationMenuPrimitive.Trigger>) {
  return (
    <NavigationMenuPrimitive.Trigger
      data-slot="navigation-menu-trigger"
      className={cn(navigationMenuTriggerStyle(), "group", className)}
      {...props}
    >
      {children}{" "}
      <ChevronDownIcon
        className="relative top-[1px] ml-1 size-3 transition duration-300 group-data-[state=open]:rotate-180"
        aria-hidden="true"
      />
    </NavigationMenuPrimitive.Trigger>
  )
}

function NavigationMenuContent({
  className,
  ...props
}: React.ComponentProps<typeof NavigationMenuPrimitive.Content>) {
  return (
    <NavigationMenuPrimitive.Content
      data-slot="navigation-menu-content"
      className={cn(
        "data-[motion^=from-]:animate-in data-[motion^=to-]:animate-out data-[motion^=from-]:fade-in data-[motion^=to-]:fade-out data-[motion=from-end]:slide-in-from-right-52 data-[motion=from-start]:slide-in-from-left-52 data-[motion=to-end]:slide-out-to-right-52 data-[motion=to-start]:slide-out-to-left-52 top-0 left-0 w-full p-2 pr-2.5 md:absolute md:w-auto",
        "group-data-[viewport=false]/navigation-menu:bg-popover group-data-[viewport=false]/navigation-menu:text-popover-foreground group-data-[viewport=false]/navigation-menu:data-[state=open]:animate-in group-data-[viewport=false]/navigation-menu:data-[state=closed]:animate-out group-data-[viewport=false]/navigation-menu:data-[state=closed]:zoom-out-95 group-data-[viewport=false]/navigation-menu:data-[state=open]:zoom-in-95 group-data-[viewport=false]/navigation-menu:data-[state=open]:fade-in-0 group-data-[viewport=false]/navigation-menu:data-[state=closed]:fade-out-0 group-data-[viewport=false]/navigation-menu:top-full group-data-[viewport=false]/navigation-menu:mt-1.5 group-data-[viewport=false]/navigation-menu:overflow-hidden group-data-[viewport=false]/navigation-menu:rounded-md group-data-[viewport=false]/navigation-menu:border group-data-[viewport=false]/navigation-menu:shadow group-data-[viewport=false]/navigation-menu:duration-200 **:data-[slot=navigation-menu-link]:focus:ring-0 **:data-[slot=navigation-menu-link]:focus:outline-none",
        className
      )}
      {...props}
    />
  )
}

function NavigationMenuViewport({
  className,
  ...props
}: React.ComponentProps<typeof NavigationMenuPrimitive.Viewport>) {
  return (
    <div
      className={cn(
        "absolute top-full left-0 isolate z-50 flex justify-center"
      )}
    >
      <NavigationMenuPrimitive.Viewport
        data-slot="navigation-menu-viewport"
        className={cn(
          "origin-top-center bg-popover text-popover-foreground data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-90 relative mt-1.5 h-[var(--radix-navigation-menu-viewport-height)] w-full overflow-hidden rounded-md border shadow md:w-[var(--radix-navigation-menu-viewport-width)]",
          className
        )}
        {...props}
      />
    </div>
  )
}

function NavigationMenuLink({
  className,
  ...props
}: React.ComponentProps<typeof NavigationMenuPrimitive.Link>) {
  return (
    <NavigationMenuPrimitive.Link
      data-slot="navigation-menu-link"
      className={cn(
        "data-[active=true]:focus:bg-accent data-[active=true]:hover:bg-accent data-[active=true]:bg-accent/50 data-[active=true]:text-accent-foreground hover:bg-accent hover:text-accent-foreground focus:bg-accent focus:text-accent-foreground focus-visible:ring-ring/50 [&_svg:not([class*='text-'])]:text-muted-foreground flex flex-col gap-1 rounded-sm p-2 text-sm transition-all outline-none focus-visible:ring-[3px] focus-visible:outline-1 [&_svg:not([class*='size-'])]:size-4",
        className
      )}
      {...props}
    />
  )
}

function NavigationMenuIndicator({
  className,
  ...props
}: React.ComponentProps<typeof NavigationMenuPrimitive.Indicator>) {
  return (
    <NavigationMenuPrimitive.Indicator
      data-slot="navigation-menu-indicator"
      className={cn(
        "data-[state=visible]:animate-in data-[state=hidden]:animate-out data-[state=hidden]:fade-out data-[state=visible]:fade-in top-full z-[1] flex h-1.5 items-end justify-center overflow-hidden",
        className
      )}
      {...props}
    >
      <div className="bg-border relative top-[60%] h-2 w-2 rotate-45 rounded-tl-sm shadow-md" />
    </NavigationMenuPrimitive.Indicator>
  )
}

export {
  NavigationMenu,
  NavigationMenuList,
  NavigationMenuItem,
  NavigationMenuContent,
  NavigationMenuTrigger,
  NavigationMenuLink,
  NavigationMenuIndicator,
  NavigationMenuViewport,
  navigationMenuTriggerStyle,
}
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

## File: `components/ui/popover.tsx`
```tsx
"use client"

import * as React from "react"
import * as PopoverPrimitive from "@radix-ui/react-popover"

import { cn } from "@/lib/utils"

function Popover({
  ...props
}: React.ComponentProps<typeof PopoverPrimitive.Root>) {
  return <PopoverPrimitive.Root data-slot="popover" {...props} />
}

function PopoverTrigger({
  ...props
}: React.ComponentProps<typeof PopoverPrimitive.Trigger>) {
  return <PopoverPrimitive.Trigger data-slot="popover-trigger" {...props} />
}

function PopoverContent({
  className,
  align = "center",
  sideOffset = 4,
  ...props
}: React.ComponentProps<typeof PopoverPrimitive.Content>) {
  return (
    <PopoverPrimitive.Portal>
      <PopoverPrimitive.Content
        data-slot="popover-content"
        align={align}
        sideOffset={sideOffset}
        className={cn(
          "bg-popover text-popover-foreground data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 z-50 w-72 origin-(--radix-popover-content-transform-origin) rounded-md border p-4 shadow-md outline-hidden",
          className
        )}
        {...props}
      />
    </PopoverPrimitive.Portal>
  )
}

function PopoverAnchor({
  ...props
}: React.ComponentProps<typeof PopoverPrimitive.Anchor>) {
  return <PopoverPrimitive.Anchor data-slot="popover-anchor" {...props} />
}

export { Popover, PopoverTrigger, PopoverContent, PopoverAnchor }
```

## File: `components/ui/progress.tsx`
```tsx
"use client"

import * as React from "react"
import * as ProgressPrimitive from "@radix-ui/react-progress"

import { cn } from "@/lib/utils"

function Progress({
  className,
  value,
  ...props
}: React.ComponentProps<typeof ProgressPrimitive.Root>) {
  return (
    <ProgressPrimitive.Root
      data-slot="progress"
      className={cn(
        "bg-primary/20 relative h-2 w-full overflow-hidden rounded-full",
        className
      )}
      {...props}
    >
      <ProgressPrimitive.Indicator
        data-slot="progress-indicator"
        className="bg-primary h-full w-full flex-1 transition-all"
        style={{ transform: `translateX(-${100 - (value || 0)}%)` }}
      />
    </ProgressPrimitive.Root>
  )
}

export { Progress }
```

## File: `components/ui/radio-group.tsx`
```tsx
"use client"

import * as React from "react"
import * as RadioGroupPrimitive from "@radix-ui/react-radio-group"
import { CircleIcon } from "lucide-react"

import { cn } from "@/lib/utils"

function RadioGroup({
  className,
  ...props
}: React.ComponentProps<typeof RadioGroupPrimitive.Root>) {
  return (
    <RadioGroupPrimitive.Root
      data-slot="radio-group"
      className={cn("grid gap-3", className)}
      {...props}
    />
  )
}

function RadioGroupItem({
  className,
  ...props
}: React.ComponentProps<typeof RadioGroupPrimitive.Item>) {
  return (
    <RadioGroupPrimitive.Item
      data-slot="radio-group-item"
      className={cn(
        "border-input text-primary focus-visible:border-ring focus-visible:ring-ring/50 aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive dark:bg-input/30 aspect-square size-4 shrink-0 rounded-full border shadow-xs transition-[color,box-shadow] outline-none focus-visible:ring-[3px] disabled:cursor-not-allowed disabled:opacity-50",
        className
      )}
      {...props}
    >
      <RadioGroupPrimitive.Indicator
        data-slot="radio-group-indicator"
        className="relative flex items-center justify-center"
      >
        <CircleIcon className="fill-primary absolute top-1/2 left-1/2 size-2 -translate-x-1/2 -translate-y-1/2" />
      </RadioGroupPrimitive.Indicator>
    </RadioGroupPrimitive.Item>
  )
}

export { RadioGroup, RadioGroupItem }
```

## File: `components/ui/resizable.tsx`
```tsx
"use client"

import * as React from "react"
import { GripVerticalIcon } from "lucide-react"
import * as ResizablePrimitive from "react-resizable-panels"

import { cn } from "@/lib/utils"

function ResizablePanelGroup({
  className,
  ...props
}: React.ComponentProps<typeof ResizablePrimitive.PanelGroup>) {
  return (
    <ResizablePrimitive.PanelGroup
      data-slot="resizable-panel-group"
      className={cn(
        "flex h-full w-full data-[panel-group-direction=vertical]:flex-col",
        className
      )}
      {...props}
    />
  )
}

function ResizablePanel({
  ...props
}: React.ComponentProps<typeof ResizablePrimitive.Panel>) {
  return <ResizablePrimitive.Panel data-slot="resizable-panel" {...props} />
}

function ResizableHandle({
  withHandle,
  className,
  ...props
}: React.ComponentProps<typeof ResizablePrimitive.PanelResizeHandle> & {
  withHandle?: boolean
}) {
  return (
    <ResizablePrimitive.PanelResizeHandle
      data-slot="resizable-handle"
      className={cn(
        "bg-border focus-visible:ring-ring relative flex w-px items-center justify-center after:absolute after:inset-y-0 after:left-1/2 after:w-1 after:-translate-x-1/2 focus-visible:ring-1 focus-visible:ring-offset-1 focus-visible:outline-hidden data-[panel-group-direction=vertical]:h-px data-[panel-group-direction=vertical]:w-full data-[panel-group-direction=vertical]:after:left-0 data-[panel-group-direction=vertical]:after:h-1 data-[panel-group-direction=vertical]:after:w-full data-[panel-group-direction=vertical]:after:-translate-y-1/2 data-[panel-group-direction=vertical]:after:translate-x-0 [&[data-panel-group-direction=vertical]>div]:rotate-90",
        className
      )}
      {...props}
    >
      {withHandle && (
        <div className="bg-border z-10 flex h-4 w-3 items-center justify-center rounded-xs border">
          <GripVerticalIcon className="size-2.5" />
        </div>
      )}
    </ResizablePrimitive.PanelResizeHandle>
  )
}

export { ResizablePanelGroup, ResizablePanel, ResizableHandle }
```

## File: `components/ui/scroll-area.tsx`
```tsx
"use client"

import * as React from "react"
import * as ScrollAreaPrimitive from "@radix-ui/react-scroll-area"

import { cn } from "@/lib/utils"

function ScrollArea({
  className,
  children,
  ...props
}: React.ComponentProps<typeof ScrollAreaPrimitive.Root>) {
  return (
    <ScrollAreaPrimitive.Root
      data-slot="scroll-area"
      className={cn("relative", className)}
      {...props}
    >
      <ScrollAreaPrimitive.Viewport
        data-slot="scroll-area-viewport"
        className="focus-visible:ring-ring/50 size-full rounded-[inherit] transition-[color,box-shadow] outline-none focus-visible:ring-[3px] focus-visible:outline-1"
      >
        {children}
      </ScrollAreaPrimitive.Viewport>
      <ScrollBar />
      <ScrollAreaPrimitive.Corner />
    </ScrollAreaPrimitive.Root>
  )
}

function ScrollBar({
  className,
  orientation = "vertical",
  ...props
}: React.ComponentProps<typeof ScrollAreaPrimitive.ScrollAreaScrollbar>) {
  return (
    <ScrollAreaPrimitive.ScrollAreaScrollbar
      data-slot="scroll-area-scrollbar"
      orientation={orientation}
      className={cn(
        "flex touch-none p-px transition-colors select-none",
        orientation === "vertical" &&
          "h-full w-2.5 border-l border-l-transparent",
        orientation === "horizontal" &&
          "h-2.5 flex-col border-t border-t-transparent",
        className
      )}
      {...props}
    >
      <ScrollAreaPrimitive.ScrollAreaThumb
        data-slot="scroll-area-thumb"
        className="bg-border relative flex-1 rounded-full"
      />
    </ScrollAreaPrimitive.ScrollAreaScrollbar>
  )
}

export { ScrollArea, ScrollBar }
```

## File: `components/ui/select.tsx`
```tsx
"use client"

import * as React from "react"
import * as SelectPrimitive from "@radix-ui/react-select"
import { CheckIcon, ChevronDownIcon, ChevronUpIcon } from "lucide-react"

import { cn } from "@/lib/utils"

function Select({
  ...props
}: React.ComponentProps<typeof SelectPrimitive.Root>) {
  return <SelectPrimitive.Root data-slot="select" {...props} />
}

function SelectGroup({
  ...props
}: React.ComponentProps<typeof SelectPrimitive.Group>) {
  return <SelectPrimitive.Group data-slot="select-group" {...props} />
}

function SelectValue({
  ...props
}: React.ComponentProps<typeof SelectPrimitive.Value>) {
  return <SelectPrimitive.Value data-slot="select-value" {...props} />
}

function SelectTrigger({
  className,
  size = "default",
  children,
  ...props
}: React.ComponentProps<typeof SelectPrimitive.Trigger> & {
  size?: "sm" | "default"
}) {
  return (
    <SelectPrimitive.Trigger
      data-slot="select-trigger"
      data-size={size}
      className={cn(
        "border-input data-[placeholder]:text-muted-foreground [&_svg:not([class*='text-'])]:text-muted-foreground focus-visible:border-ring focus-visible:ring-ring/50 aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive dark:bg-input/30 dark:hover:bg-input/50 flex w-fit items-center justify-between gap-2 rounded-md border bg-transparent px-3 py-2 text-sm whitespace-nowrap shadow-xs transition-[color,box-shadow] outline-none focus-visible:ring-[3px] disabled:cursor-not-allowed disabled:opacity-50 data-[size=default]:h-9 data-[size=sm]:h-8 *:data-[slot=select-value]:line-clamp-1 *:data-[slot=select-value]:flex *:data-[slot=select-value]:items-center *:data-[slot=select-value]:gap-2 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
        className
      )}
      {...props}
    >
      {children}
      <SelectPrimitive.Icon asChild>
        <ChevronDownIcon className="size-4 opacity-50" />
      </SelectPrimitive.Icon>
    </SelectPrimitive.Trigger>
  )
}

function SelectContent({
  className,
  children,
  position = "popper",
  ...props
}: React.ComponentProps<typeof SelectPrimitive.Content>) {
  return (
    <SelectPrimitive.Portal>
      <SelectPrimitive.Content
        data-slot="select-content"
        className={cn(
          "bg-popover text-popover-foreground data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 relative z-50 max-h-(--radix-select-content-available-height) min-w-[8rem] origin-(--radix-select-content-transform-origin) overflow-x-hidden overflow-y-auto rounded-md border shadow-md",
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
              "h-[var(--radix-select-trigger-height)] w-full min-w-[var(--radix-select-trigger-width)] scroll-my-1"
          )}
        >
          {children}
        </SelectPrimitive.Viewport>
        <SelectScrollDownButton />
      </SelectPrimitive.Content>
    </SelectPrimitive.Portal>
  )
}

function SelectLabel({
  className,
  ...props
}: React.ComponentProps<typeof SelectPrimitive.Label>) {
  return (
    <SelectPrimitive.Label
      data-slot="select-label"
      className={cn("text-muted-foreground px-2 py-1.5 text-xs", className)}
      {...props}
    />
  )
}

function SelectItem({
  className,
  children,
  ...props
}: React.ComponentProps<typeof SelectPrimitive.Item>) {
  return (
    <SelectPrimitive.Item
      data-slot="select-item"
      className={cn(
        "focus:bg-accent focus:text-accent-foreground [&_svg:not([class*='text-'])]:text-muted-foreground relative flex w-full cursor-default items-center gap-2 rounded-sm py-1.5 pr-8 pl-2 text-sm outline-hidden select-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4 *:[span]:last:flex *:[span]:last:items-center *:[span]:last:gap-2",
        className
      )}
      {...props}
    >
      <span className="absolute right-2 flex size-3.5 items-center justify-center">
        <SelectPrimitive.ItemIndicator>
          <CheckIcon className="size-4" />
        </SelectPrimitive.ItemIndicator>
      </span>
      <SelectPrimitive.ItemText>{children}</SelectPrimitive.ItemText>
    </SelectPrimitive.Item>
  )
}

function SelectSeparator({
  className,
  ...props
}: React.ComponentProps<typeof SelectPrimitive.Separator>) {
  return (
    <SelectPrimitive.Separator
      data-slot="select-separator"
      className={cn("bg-border pointer-events-none -mx-1 my-1 h-px", className)}
      {...props}
    />
  )
}

function SelectScrollUpButton({
  className,
  ...props
}: React.ComponentProps<typeof SelectPrimitive.ScrollUpButton>) {
  return (
    <SelectPrimitive.ScrollUpButton
      data-slot="select-scroll-up-button"
      className={cn(
        "flex cursor-default items-center justify-center py-1",
        className
      )}
      {...props}
    >
      <ChevronUpIcon className="size-4" />
    </SelectPrimitive.ScrollUpButton>
  )
}

function SelectScrollDownButton({
  className,
  ...props
}: React.ComponentProps<typeof SelectPrimitive.ScrollDownButton>) {
  return (
    <SelectPrimitive.ScrollDownButton
      data-slot="select-scroll-down-button"
      className={cn(
        "flex cursor-default items-center justify-center py-1",
        className
      )}
      {...props}
    >
      <ChevronDownIcon className="size-4" />
    </SelectPrimitive.ScrollDownButton>
  )
}

export {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectScrollDownButton,
  SelectScrollUpButton,
  SelectSeparator,
  SelectTrigger,
  SelectValue,
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
import { cva, VariantProps } from "class-variance-authority"
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

## File: `components/ui/slider.tsx`
```tsx
"use client"

import * as React from "react"
import * as SliderPrimitive from "@radix-ui/react-slider"

import { cn } from "@/lib/utils"

function Slider({
  className,
  defaultValue,
  value,
  min = 0,
  max = 100,
  ...props
}: React.ComponentProps<typeof SliderPrimitive.Root>) {
  const _values = React.useMemo(
    () =>
      Array.isArray(value)
        ? value
        : Array.isArray(defaultValue)
          ? defaultValue
          : [min, max],
    [value, defaultValue, min, max]
  )

  return (
    <SliderPrimitive.Root
      data-slot="slider"
      defaultValue={defaultValue}
      value={value}
      min={min}
      max={max}
      className={cn(
        "relative flex w-full touch-none items-center select-none data-[disabled]:opacity-50 data-[orientation=vertical]:h-full data-[orientation=vertical]:min-h-44 data-[orientation=vertical]:w-auto data-[orientation=vertical]:flex-col",
        className
      )}
      {...props}
    >
      <SliderPrimitive.Track
        data-slot="slider-track"
        className={cn(
          "bg-muted relative grow overflow-hidden rounded-full data-[orientation=horizontal]:h-1.5 data-[orientation=horizontal]:w-full data-[orientation=vertical]:h-full data-[orientation=vertical]:w-1.5"
        )}
      >
        <SliderPrimitive.Range
          data-slot="slider-range"
          className={cn(
            "bg-primary absolute data-[orientation=horizontal]:h-full data-[orientation=vertical]:w-full"
          )}
        />
      </SliderPrimitive.Track>
      {Array.from({ length: _values.length }, (_, index) => (
        <SliderPrimitive.Thumb
          data-slot="slider-thumb"
          key={index}
          className="border-primary bg-background ring-ring/50 block size-4 shrink-0 rounded-full border shadow-sm transition-[color,box-shadow] hover:ring-4 focus-visible:ring-4 focus-visible:outline-hidden disabled:pointer-events-none disabled:opacity-50"
        />
      ))}
    </SliderPrimitive.Root>
  )
}

export { Slider }
```

## File: `components/ui/sonner.tsx`
```tsx
"use client"

import { useTheme } from "next-themes"
import { Toaster as Sonner, ToasterProps } from "sonner"

const Toaster = ({ ...props }: ToasterProps) => {
  const { theme = "system" } = useTheme()

  return (
    <Sonner
      theme={theme as ToasterProps["theme"]}
      className="toaster group"
      style={
        {
          "--normal-bg": "var(--popover)",
          "--normal-text": "var(--popover-foreground)",
          "--normal-border": "var(--border)",
        } as React.CSSProperties
      }
      {...props}
    />
  )
}

export { Toaster }
```

## File: `components/ui/switch.tsx`
```tsx
"use client"

import * as React from "react"
import * as SwitchPrimitive from "@radix-ui/react-switch"

import { cn } from "@/lib/utils"

function Switch({
  className,
  ...props
}: React.ComponentProps<typeof SwitchPrimitive.Root>) {
  return (
    <SwitchPrimitive.Root
      data-slot="switch"
      className={cn(
        "peer data-[state=checked]:bg-primary data-[state=unchecked]:bg-input focus-visible:border-ring focus-visible:ring-ring/50 dark:data-[state=unchecked]:bg-input/80 inline-flex h-[1.15rem] w-8 shrink-0 items-center rounded-full border border-transparent shadow-xs transition-all outline-none focus-visible:ring-[3px] disabled:cursor-not-allowed disabled:opacity-50",
        className
      )}
      {...props}
    >
      <SwitchPrimitive.Thumb
        data-slot="switch-thumb"
        className={cn(
          "bg-background dark:data-[state=unchecked]:bg-foreground dark:data-[state=checked]:bg-primary-foreground pointer-events-none block size-4 rounded-full ring-0 transition-transform data-[state=checked]:translate-x-[calc(100%-2px)] data-[state=unchecked]:translate-x-0"
        )}
      />
    </SwitchPrimitive.Root>
  )
}

export { Switch }
```

## File: `components/ui/table.tsx`
```tsx
"use client"

import * as React from "react"

import { cn } from "@/lib/utils"

function Table({ className, ...props }: React.ComponentProps<"table">) {
  return (
    <div
      data-slot="table-container"
      className="relative w-full overflow-x-auto"
    >
      <table
        data-slot="table"
        className={cn("w-full caption-bottom text-sm", className)}
        {...props}
      />
    </div>
  )
}

function TableHeader({ className, ...props }: React.ComponentProps<"thead">) {
  return (
    <thead
      data-slot="table-header"
      className={cn("[&_tr]:border-b", className)}
      {...props}
    />
  )
}

function TableBody({ className, ...props }: React.ComponentProps<"tbody">) {
  return (
    <tbody
      data-slot="table-body"
      className={cn("[&_tr:last-child]:border-0", className)}
      {...props}
    />
  )
}

function TableFooter({ className, ...props }: React.ComponentProps<"tfoot">) {
  return (
    <tfoot
      data-slot="table-footer"
      className={cn(
        "bg-muted/50 border-t font-medium [&>tr]:last:border-b-0",
        className
      )}
      {...props}
    />
  )
}

function TableRow({ className, ...props }: React.ComponentProps<"tr">) {
  return (
    <tr
      data-slot="table-row"
      className={cn(
        "hover:bg-muted/50 data-[state=selected]:bg-muted border-b transition-colors",
        className
      )}
      {...props}
    />
  )
}

function TableHead({ className, ...props }: React.ComponentProps<"th">) {
  return (
    <th
      data-slot="table-head"
      className={cn(
        "text-foreground h-10 px-2 text-left align-middle font-medium whitespace-nowrap [&:has([role=checkbox])]:pr-0 [&>[role=checkbox]]:translate-y-[2px]",
        className
      )}
      {...props}
    />
  )
}

function TableCell({ className, ...props }: React.ComponentProps<"td">) {
  return (
    <td
      data-slot="table-cell"
      className={cn(
        "p-2 align-middle whitespace-nowrap [&:has([role=checkbox])]:pr-0 [&>[role=checkbox]]:translate-y-[2px]",
        className
      )}
      {...props}
    />
  )
}

function TableCaption({
  className,
  ...props
}: React.ComponentProps<"caption">) {
  return (
    <caption
      data-slot="table-caption"
      className={cn("text-muted-foreground mt-4 text-sm", className)}
      {...props}
    />
  )
}

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

## File: `components/ui/tabs.tsx`
```tsx
"use client"

import * as React from "react"
import * as TabsPrimitive from "@radix-ui/react-tabs"

import { cn } from "@/lib/utils"

function Tabs({
  className,
  ...props
}: React.ComponentProps<typeof TabsPrimitive.Root>) {
  return (
    <TabsPrimitive.Root
      data-slot="tabs"
      className={cn("flex flex-col gap-2", className)}
      {...props}
    />
  )
}

function TabsList({
  className,
  ...props
}: React.ComponentProps<typeof TabsPrimitive.List>) {
  return (
    <TabsPrimitive.List
      data-slot="tabs-list"
      className={cn(
        "bg-muted text-muted-foreground inline-flex h-9 w-fit items-center justify-center rounded-lg p-[3px]",
        className
      )}
      {...props}
    />
  )
}

function TabsTrigger({
  className,
  ...props
}: React.ComponentProps<typeof TabsPrimitive.Trigger>) {
  return (
    <TabsPrimitive.Trigger
      data-slot="tabs-trigger"
      className={cn(
        "data-[state=active]:bg-background dark:data-[state=active]:text-foreground focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:outline-ring dark:data-[state=active]:border-input dark:data-[state=active]:bg-input/30 text-foreground dark:text-muted-foreground inline-flex h-[calc(100%-1px)] flex-1 items-center justify-center gap-1.5 rounded-md border border-transparent px-2 py-1 text-sm font-medium whitespace-nowrap transition-[color,box-shadow] focus-visible:ring-[3px] focus-visible:outline-1 disabled:pointer-events-none disabled:opacity-50 data-[state=active]:shadow-sm [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
        className
      )}
      {...props}
    />
  )
}

function TabsContent({
  className,
  ...props
}: React.ComponentProps<typeof TabsPrimitive.Content>) {
  return (
    <TabsPrimitive.Content
      data-slot="tabs-content"
      className={cn("flex-1 outline-none", className)}
      {...props}
    />
  )
}

export { Tabs, TabsList, TabsTrigger, TabsContent }
```

## File: `components/ui/textarea.tsx`
```tsx
import * as React from "react"

import { cn } from "@/lib/utils"

function Textarea({ className, ...props }: React.ComponentProps<"textarea">) {
  return (
    <textarea
      data-slot="textarea"
      className={cn(
        "border-input placeholder:text-muted-foreground focus-visible:border-ring focus-visible:ring-ring/50 aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive dark:bg-input/30 flex field-sizing-content min-h-16 w-full rounded-md border bg-transparent px-3 py-2 text-base shadow-xs transition-[color,box-shadow] outline-none focus-visible:ring-1 disabled:cursor-not-allowed disabled:opacity-50 md:text-sm",
        className
      )}
      {...props}
    />
  )
}

export { Textarea }
```

## File: `components/ui/toggle-group.tsx`
```tsx
"use client"

import * as React from "react"
import * as ToggleGroupPrimitive from "@radix-ui/react-toggle-group"
import { type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"
import { toggleVariants } from "@/components/ui/toggle"

const ToggleGroupContext = React.createContext<
  VariantProps<typeof toggleVariants>
>({
  size: "default",
  variant: "default",
})

function ToggleGroup({
  className,
  variant,
  size,
  children,
  ...props
}: React.ComponentProps<typeof ToggleGroupPrimitive.Root> &
  VariantProps<typeof toggleVariants>) {
  return (
    <ToggleGroupPrimitive.Root
      data-slot="toggle-group"
      data-variant={variant}
      data-size={size}
      className={cn(
        "group/toggle-group flex w-fit items-center rounded-md data-[variant=outline]:shadow-xs",
        className
      )}
      {...props}
    >
      <ToggleGroupContext.Provider value={{ variant, size }}>
        {children}
      </ToggleGroupContext.Provider>
    </ToggleGroupPrimitive.Root>
  )
}

function ToggleGroupItem({
  className,
  children,
  variant,
  size,
  ...props
}: React.ComponentProps<typeof ToggleGroupPrimitive.Item> &
  VariantProps<typeof toggleVariants>) {
  const context = React.useContext(ToggleGroupContext)

  return (
    <ToggleGroupPrimitive.Item
      data-slot="toggle-group-item"
      data-variant={context.variant || variant}
      data-size={context.size || size}
      className={cn(
        toggleVariants({
          variant: context.variant || variant,
          size: context.size || size,
        }),
        "min-w-0 flex-1 shrink-0 rounded-none shadow-none first:rounded-l-md last:rounded-r-md focus:z-10 focus-visible:z-10 data-[variant=outline]:border-l-0 data-[variant=outline]:first:border-l",
        className
      )}
      {...props}
    >
      {children}
    </ToggleGroupPrimitive.Item>
  )
}

export { ToggleGroup, ToggleGroupItem }
```

## File: `components/ui/toggle.tsx`
```tsx
"use client"

import * as React from "react"
import * as TogglePrimitive from "@radix-ui/react-toggle"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const toggleVariants = cva(
  "inline-flex items-center justify-center gap-2 rounded-md text-sm font-medium hover:bg-muted hover:text-muted-foreground disabled:pointer-events-none disabled:opacity-50 data-[state=on]:bg-accent data-[state=on]:text-accent-foreground [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 [&_svg]:shrink-0 focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] outline-none transition-[color,box-shadow] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive whitespace-nowrap",
  {
    variants: {
      variant: {
        default: "bg-transparent",
        outline:
          "border border-input bg-transparent shadow-xs hover:bg-accent hover:text-accent-foreground",
      },
      size: {
        default: "h-9 px-2 min-w-9",
        sm: "h-8 px-1.5 min-w-8",
        lg: "h-10 px-2.5 min-w-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

function Toggle({
  className,
  variant,
  size,
  ...props
}: React.ComponentProps<typeof TogglePrimitive.Root> &
  VariantProps<typeof toggleVariants>) {
  return (
    <TogglePrimitive.Root
      data-slot="toggle"
      className={cn(toggleVariants({ variant, size, className }))}
      {...props}
    />
  )
}

export { Toggle, toggleVariants }
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

## File: `lib/open-researcher-agent.ts`
```typescript
import Anthropic from '@anthropic-ai/sdk';
import FirecrawlApp from '@mendable/firecrawl-js';

// Lazy initialization for Vercel deployment
let anthropic: Anthropic | null = null;
let firecrawl: FirecrawlApp | null = null;

function getAnthropicClient(): Anthropic {
  if (!anthropic) {
    const apiKey = process.env.ANTHROPIC_API_KEY;
    if (!apiKey) {
      // ANTHROPIC_API_KEY is not set in environment variables
      throw new Error('ANTHROPIC_API_KEY environment variable is not set');
    }
    // Initializing Anthropic client
    anthropic = new Anthropic({ apiKey });
  }
  return anthropic;
}

function getFirecrawlClient(): FirecrawlApp {
  if (!firecrawl) {
    const apiKey = process.env.FIRECRAWL_API_KEY;
    if (!apiKey) {
      // FIRECRAWL_API_KEY is not set in environment variables
      throw new Error('FIRECRAWL_API_KEY environment variable is not set');
    }
    // Initializing Firecrawl client
    firecrawl = new FirecrawlApp({ apiKey });
  }
  return firecrawl;
}

// Type definitions
interface ToolDefinition {
  name: string;
  description: string;
  input_schema: {
    type: string;
    properties: Record<string, unknown>;
    required?: string[];
  };
}

interface FirecrawlSearchResult {
  success?: boolean;
  data?: Array<{
    url?: string;
    title?: string;
    description?: string;
    markdown?: string;
    links?: string[];
    screenshot?: string;
    metadata?: {
      title?: string;
      description?: string;
    };
  }>;
  error?: string;
}

interface FirecrawlScrapeResult {
  success?: boolean;
  data?: {
    url?: string;
    markdown?: string;
    links?: string[];
    screenshot?: string;
    metadata?: {
      title?: string;
      description?: string;
    };
  };
  markdown?: string;
  links?: string[];
  screenshot?: string;
  metadata?: {
    title?: string;
    description?: string;
  };
  error?: string;
  statusCode?: number;
  message?: string;
}

// Define our research tools
const tools: ToolDefinition[] = [
  {
    name: "web_search",
    description: "Search the web and optionally scrape content from results. Supports Google search operators (site:, intitle:, etc.). Set scrape_content=true to extract full content. For listing/counting items, the search results preview is often sufficient.",
    input_schema: {
      type: "object",
      properties: {
        query: {
          type: "string",
          description: "Search query"
        },
        limit: {
          type: "number",
          description: "Number of results to return",
          default: 5
        },
        scrape_content: {
          type: "boolean",
          description: "Whether to scrape the content of search results",
          default: false
        },
        tbs: {
          type: "string",
          description: "Time-based search filter (e.g., 'qdr:w' for past week)",
          enum: ["qdr:h", "qdr:d", "qdr:w", "qdr:m", "qdr:y"]
        }
      },
      required: ["query"]
    }
  },
  {
    name: "deep_scrape",
    description: "Scrape a single URL and optionally follow its links for deeper analysis. Best for detailed research or when you need content from multiple linked pages. For simple queries, a single page scrape is usually sufficient.",
    input_schema: {
      type: "object",
      properties: {
        source_url: {
          type: "string",
          description: "The source URL to extract links from"
        },
        link_filter: {
          type: "string",
          description: "Regex pattern to filter which links to scrape (e.g., '/blog/', '/docs/')"
        },
        max_depth: {
          type: "number",
          description: "Maximum depth of links to follow (1 = direct links only)",
          default: 1
        },
        max_links: {
          type: "number",
          description: "Maximum number of links to scrape per level",
          default: 5
        },
        formats: {
          type: "array",
          items: { type: "string" },
          description: "Output formats for scraped content",
          default: ["markdown"]
        }
      },
      required: ["source_url"]
    }
  },
  {
    name: "analyze_content",
    description: "Analyze scraped content to extract specific information, patterns, or insights. Use this to process content you've already fetched rather than fetching more.",
    input_schema: {
      type: "object",
      properties: {
        content: {
          type: "string",
          description: "Content to analyze"
        },
        analysis_type: {
          type: "string",
          enum: ["sentiment", "key_facts", "trends", "summary", "credibility"],
          description: "Type of analysis to perform"
        },
        context: {
          type: "string",
          description: "Additional context for the analysis"
        }
      },
      required: ["content", "analysis_type"]
    }
  }
];

// Execute Firecrawl search with two-step approach
async function executeWebSearch(query: string, limit: number = 5, scrapeContent: boolean = false, tbs?: string): Promise<{ content: string; screenshots: Array<{ url: string; screenshot?: string }> }> {
  // Performing firecrawl search
  
  const screenshots: Array<{ url: string; screenshot?: string }> = [];
  
  try {
    // Step 1: First search without scraping to get metadata
    const searchOptions: { limit: number; scrapeOptions: { formats: string[] }; tbs?: string } = {
      limit,
      scrapeOptions: {
        formats: [] // Empty formats array means no scraping
      }
    };

    if (tbs) {
      searchOptions.tbs = tbs;
    }

    const metadataResults = await getFirecrawlClient().search(query, searchOptions) as FirecrawlSearchResult;
    
    if (!metadataResults.data || metadataResults.data.length === 0) {
      return { content: "No search results found.", screenshots: [] };
    }

    let output = `Found ${metadataResults.data.length} results:\n\n`;
    
    // Display all results with metadata
    for (const [index, result] of metadataResults.data.entries()) {
      output += `[${index + 1}] ${result.title}\n`;
      output += `URL: ${result.url}\n`;
      output += `Description: ${result.description}\n`;
      output += '\n';
    }

    // Step 2: If scraping is requested, decide which URLs to scrape based on metadata
    if (scrapeContent) {
      // Dynamic filtering logic based on query intent and search results
      
      // Analyze query for intent signals
      const querySignals = {
        wantsRecent: /latest|recent|newest|new|today|yesterday|this week|this month/i.test(query),
        wantsBlog: /blog|post|article|news|update|announce/i.test(query),
        wantsDocs: /documentation|docs|api|reference|guide|tutorial|how to/i.test(query),
        hasTimeFilter: !!tbs,
        hasSiteFilter: /site:/i.test(query)
      };
      
      const urlsToScrape = metadataResults.data
        .filter((result, index) => {
          const text = `${result.title} ${result.description} ${result.url}`.toLowerCase();
          
          // Always include top results when no specific filters
          if (!querySignals.wantsRecent && !querySignals.wantsBlog && !querySignals.wantsDocs) {
            return index < Math.min(limit, 5);
          }
          
          // For time-sensitive queries, include all results (they're already filtered by search)
          if (querySignals.wantsRecent || querySignals.hasTimeFilter) {
            return true;
          }
          
          // For content-type specific queries, use smart matching
          if (querySignals.wantsBlog || querySignals.wantsDocs) {
            // Check URL patterns
            try {
              const url = new URL(result.url!);
              const pathLower = url.pathname.toLowerCase();
              
              if (querySignals.wantsBlog && (pathLower.includes('blog') || pathLower.includes('post') || 
                  pathLower.includes('article') || pathLower.includes('news'))) {
                return true;
              }
              
              if (querySignals.wantsDocs && (pathLower.includes('doc') || pathLower.includes('api') || 
                  pathLower.includes('guide') || pathLower.includes('reference'))) {
                return true;
              }
            } catch {}
            
            // Also check title/description for relevant terms
            if (querySignals.wantsBlog && /blog|post|article|published|wrote/i.test(text)) {
              return true;
            }
            
            if (querySignals.wantsDocs && /documentation|api|guide|tutorial|reference/i.test(text)) {
              return true;
            }
          }
          
          // Default: include top results
          return index < 3;
        })
        .map(result => result.url);

      // Scraping URLs

      if (urlsToScrape.length > 0) {
        // Now search again with scraping enabled
        const scrapeOptions: { limit: number; scrapeOptions: { formats: string[] }; tbs?: string } = {
          limit,
          scrapeOptions: {
            formats: ["markdown"]
          }
        };

        if (tbs) {
          scrapeOptions.tbs = tbs;
        }

        const scrapedResults = await getFirecrawlClient().search(query, scrapeOptions) as FirecrawlSearchResult;
        
        // Add scraped content to output
        output += `\n--- SCRAPED CONTENT ---\n\n`;
        
        // Process scraped results
        const scrapedWithMetadata = [];
        
        for (const [index, result] of (scrapedResults.data || []).entries()) {
          // Only include scraped content for our selected URLs
          if (result.url && urlsToScrape.includes(result.url) && result.markdown) {
            // Store screenshot if available
            if (result.screenshot) {
              screenshots.push({ url: result.url, screenshot: result.screenshot });
            }
            
            // Try to extract date from content if query suggests time-sensitivity
            let dateFound = null;
            if (querySignals.wantsRecent || querySignals.wantsBlog) {
              // Look for common date patterns in the content
              const datePatterns = [
                /(\w+ \d{1,2}, \d{4})/g,  // "June 12, 2025"
                /(\d{4}-\d{2}-\d{2})/g,    // "2025-06-12"
                /(\d{1,2}\/\d{1,2}\/\d{4})/g,  // "6/12/2025"
                /(\d{1,2} \w+ \d{4})/g    // "12 June 2025"
              ];
              
              // Check multiple locations for dates
              const searchText = [
                result.markdown.substring(0, 1000), // Check beginning
                result.metadata?.description || '',
                result.metadata?.title || ''
              ].join(' ');
              
              for (const pattern of datePatterns) {
                const matches = searchText.match(pattern);
                if (matches && matches.length > 0) {
                  // Try to parse and validate the date
                  try {
                    const testDate = new Date(matches[0]);
                    if (!isNaN(testDate.getTime()) && testDate.getFullYear() >= 2020) {
                      dateFound = matches[0];
                      break;
                    }
                  } catch {}
                }
              }
            }
            
            scrapedWithMetadata.push({
              ...result,
              index: index + 1,
              dateFound,
              relevanceScore: index // Lower index = higher relevance from search
            });
          }
        }
        
        // Sort results based on query intent
        if (scrapedWithMetadata.length > 0) {
          scrapedWithMetadata.sort((a, b) => {
            // For time-sensitive queries, prioritize by date
            if (querySignals.wantsRecent && (a.dateFound || b.dateFound)) {
              if (!a.dateFound && !b.dateFound) return a.relevanceScore - b.relevanceScore;
              if (!a.dateFound) return 1;
              if (!b.dateFound) return -1;
              
              try {
                const dateA = new Date(a.dateFound);
                const dateB = new Date(b.dateFound);
                return dateB.getTime() - dateA.getTime(); // Newest first
              } catch {
                return a.relevanceScore - b.relevanceScore;
              }
            }
            
            // Otherwise, maintain search relevance order
            return a.relevanceScore - b.relevanceScore;
          });
        }
        
        // Display the results
        for (const result of scrapedWithMetadata) {
          output += `[${result.index}] ${result.title} (SCRAPED)\n`;
          output += `URL: ${result.url}\n`;
          if (result.dateFound) {
            output += `Date: ${result.dateFound}\n`;
          }
          
          // Include first 500 chars of scraped content
          const preview = result.markdown ? result.markdown.substring(0, 500).replace(/\n+/g, ' ') : '';
          output += `Content preview: ${preview}...\n`;
          
          if (result.links && result.links.length > 0) {
            output += `Links found: ${result.links.length} (first 3: ${result.links.slice(0, 3).join(', ')})\n`;
          }
          
          output += '\n';
        }
      }
    }
    
    return { content: output, screenshots };
  } catch (error) {
    // Search error occurred
    return { 
      content: `Error performing search: ${error instanceof Error ? error.message : 'Unknown error'}`,
      screenshots: []
    };
  }
}

// Analyze content with various methods
async function analyzeContent(content: string, analysisType: string, context?: string): Promise<string> {
  // Performing analysis
  
  switch (analysisType) {
    case 'sentiment':
      // Simple sentiment analysis based on keywords
      const positiveWords = ['success', 'growth', 'improve', 'innovation', 'breakthrough', 'leading', 'advanced'];
      const negativeWords = ['challenge', 'risk', 'concern', 'threat', 'decline', 'issue', 'problem'];
      
      const contentLower = content.toLowerCase();
      const positiveMatches = positiveWords.filter(word => contentLower.includes(word));
      const negativeMatches = negativeWords.filter(word => contentLower.includes(word));
      
      const sentiment = positiveMatches.length > negativeMatches.length ? 'Positive' : 
                       negativeMatches.length > positiveMatches.length ? 'Negative' : 'Neutral';
      
      return `Sentiment Analysis:\n` +
             `- Overall: ${sentiment}\n` +
             `- Positive indicators: ${positiveMatches.join(', ') || 'none'}\n` +
             `- Negative indicators: ${negativeMatches.join(', ') || 'none'}\n` +
             `- Context considered: ${context || 'general analysis'}`;

    case 'key_facts':
      // Extract sentences with numbers, percentages, or key terms
      const sentences = content.split(/[.!?]/).filter(s => s.trim());
      const keyFacts = sentences
        .filter(s => /\d+%|\$\d+|\d+ (million|billion)|first|largest|leading/i.test(s))
        .slice(0, 5)
        .map(s => s.trim());
      
      return `Key Facts Extracted:\n${keyFacts.map((fact, i) => `${i + 1}. ${fact}`).join('\n')}`;

    case 'trends':
      // Identify trend indicators
      const trendPatterns = {
        'Growth': /increas|grow|rise|expand|surge/i,
        'Decline': /decreas|fall|drop|declin|reduc/i,
        'Innovation': /new|innovat|breakthrough|cutting-edge|advanced/i,
        'Adoption': /adopt|implement|deploy|integrat|using/i,
      };
      
      const identifiedTrends: string[] = [];
      for (const [trend, pattern] of Object.entries(trendPatterns)) {
        if (pattern.test(content)) {
          identifiedTrends.push(trend);
        }
      }
      
      return `Trend Analysis:\n` +
             `- Identified trends: ${identifiedTrends.join(', ') || 'No clear trends'}\n` +
             `- Market direction: ${identifiedTrends.includes('Growth') ? 'Positive' : 'Mixed'}\n` +
             `- Innovation signals: ${identifiedTrends.includes('Innovation') ? 'Strong' : 'Limited'}`;

    case 'summary':
      // Extract most important sentences
      const allSentences = content.split(/[.!?]/).filter(s => s.trim().length > 20);
      const importantSentences = allSentences
        .filter(s => /announc|launch|report|study|research|found|develop/i.test(s))
        .slice(0, 3);
      
      return `Executive Summary:\n${importantSentences.join('. ')}.`;

    case 'credibility':
      // Assess source credibility indicators
      const credibilityFactors = {
        'Has citations': /according to|study|research|report|survey/i.test(content),
        'Includes data': /\d+%|\$\d+|statistics|data/i.test(content),
        'Official source': /\.gov|\.edu|official|announce/i.test(content),
        'Recent info': /2024|2025|recent|latest|new/i.test(content),
      };
      
      const credibilityScore = Object.values(credibilityFactors).filter(v => v).length;
      
      return `Credibility Assessment:\n` +
             Object.entries(credibilityFactors).map(([factor, present]) => 
               `- ${factor}: ${present ? '✓' : '✗'}`
             ).join('\n') +
             `\n- Credibility score: ${credibilityScore}/4`;

    default:
      return `Analysis type "${analysisType}" completed.`;
  }
}

// Deep scrape functionality
async function executeDeepScrape(
  sourceUrl: string, 
  linkFilter?: string, 
  maxDepth: number = 1, 
  maxLinks: number = 5,
  formats: string[] = ["markdown"]
): Promise<{ content: string; screenshots: Array<{ url: string; screenshot?: string }> }> {
  // Performing firecrawl scrape
  
  const screenshots: Array<{ url: string; screenshot?: string }> = [];
  
  try {
    // First, scrape the source page to get links and screenshot
    
    let sourceResult;
    try {
      sourceResult = await getFirecrawlClient().scrapeUrl(sourceUrl, {
        formats: ['markdown', 'links', 'screenshot@fullPage']
      });
    } catch (scrapeError) {
      // Scrape failed
      return { 
        content: `Failed to scrape URL: ${scrapeError instanceof Error ? scrapeError.message : 'Unknown error'}`,
        screenshots: []
      };
    }

    // Firecrawl v1 returns data at the top level of the response
    const data = (sourceResult as FirecrawlScrapeResult).data || (sourceResult as FirecrawlScrapeResult);
    
    if (!data.markdown) {
      // No content found
      return { 
        content: `Failed to scrape source URL: No content found\n\nTip: Try using web_search with scrape_content=true for better results.`,
        screenshots: []
      };
    }
    
    // Store screenshot if available
    if (data.screenshot) {
      screenshots.push({ url: sourceUrl, screenshot: data.screenshot });
    }

    let output = `Source page scraped successfully\n`;
    output += `Title: ${data.metadata?.title || 'Unknown'}\n\n`;
    
    // Add the main page content
    if (data.markdown) {
      const contentPreview = data.markdown.length > 3000 ? 
        data.markdown.substring(0, 3000) + '...\n[Content truncated]' : 
        data.markdown;
      output += `Page content:\n${contentPreview}\n\n`;
    }
    
    // Only follow links if explicitly requested with a filter
    if (!linkFilter) {
      output += `\nFound ${data.links?.length || 0} links on this page.\n`;
      output += `To follow specific links, use the link_filter parameter (e.g., link_filter: "/blog/[^/]+$" for blog posts).\n`;
      return { content: output, screenshots };
    }

    // Extract and filter links
    const allLinks: string[] = data.links || [];
    let filteredLinks = allLinks;
    
    const filterRegex = new RegExp(linkFilter, 'i');
    filteredLinks = allLinks.filter((link: string) => filterRegex.test(link));
    output += `Filtered to ${filteredLinks.length} links matching pattern "${linkFilter}"\n\n`;

    // Limit the number of links to scrape
    const linksToScrape = filteredLinks.slice(0, maxLinks);
    
    if (linksToScrape.length === 0) {
      output += "No links to scrape after filtering.\n";
      return { content: output, screenshots };
    }

    output += `Following ${linksToScrape.length} links:\n`;
    
    // Scrape each link in parallel
    const scrapePromises = linksToScrape.map(async (link: string) => {
      try {
        const result = await getFirecrawlClient().scrapeUrl(link, { 
          formats: [...formats, 'screenshot@fullPage'] as ("markdown" | "html" | "content" | "rawHtml" | "links" | "screenshot" | "screenshot@fullPage" | "extract" | "json" | "changeTracking")[]
        });
        
        // Handle both response formats
        const resultData = (result as FirecrawlScrapeResult).data || (result as FirecrawlScrapeResult);
        if ((result as FirecrawlScrapeResult).success && resultData.markdown) {
          // Store screenshot if available
          if (resultData.screenshot) {
            screenshots.push({ url: link, screenshot: resultData.screenshot });
          }
          
          return {
            url: link,
            title: resultData.metadata?.title || 'Unknown',
            description: resultData.metadata?.description || '',
            content: resultData.markdown?.substring(0, 500) || '',
            links: resultData.links?.length || 0,
            hasScreenshot: !!resultData.screenshot
          };
        }
        return null;
      } catch {
        // Failed to scrape link
        return null;
      }
    });

    const results = await Promise.all(scrapePromises);
    const successfulScrapes = results.filter(r => r !== null);
    
    output += `\nSuccessfully scraped ${successfulScrapes.length} pages:\n\n`;
    
    for (const [index, result] of successfulScrapes.entries()) {
      if (result) {
        output += `[${index + 1}] ${result.title}\n`;
        output += `URL: ${result.url}\n`;
        output += `Description: ${result.description}\n`;
        output += `Content preview: ${result.content}...\n`;
        if (result.hasScreenshot) {
          output += `Screenshot: ✓ Captured\n`;
        }
        if (maxDepth > 1 && result.links > 0) {
          output += `Sub-links available: ${result.links} (depth ${maxDepth - 1} remaining)\n`;
        }
        output += '\n';
      }
    }
    
    return { content: output, screenshots };
  } catch (error) {
    // Deep scrape error occurred
    return { 
      content: `Error performing deep scrape: ${error instanceof Error ? error.message : 'Unknown error'}`,
      screenshots: []
    };
  }
}

// Execute tool based on name
export async function executeTool(toolName: string, input: Record<string, unknown>): Promise<{ content: string; screenshots?: Array<{ url: string; screenshot?: string }> }> {
  switch (toolName) {
    case 'web_search':
      return await executeWebSearch(
        input.query as string, 
        (input.limit as number) || 5, 
        (input.scrape_content as boolean) || false,
        input.tbs as string | undefined
      );
    case 'deep_scrape':
      return await executeDeepScrape(
        input.source_url as string,
        input.link_filter as string | undefined,
        (input.max_depth as number) || 1,
        (input.max_links as number) || 5,
        (input.formats as string[]) || ['markdown']
      );
    case 'analyze_content':
      return { content: await analyzeContent(input.content as string, input.analysis_type as string, input.context as string | undefined) };
    default:
      return { content: `Unknown tool: ${toolName}` };
  }
}

// Streaming version with callback
export async function performResearchWithStreaming(
  query: string, 
  onEvent: (event: { type: string; [key: string]: unknown }) => void
): Promise<string> {
  // Performing research

  // Send initial event
  onEvent({ type: 'start', query });

  const messages: Array<{ role: string; content: string | Array<{ type: string; [key: string]: unknown }> }> = [{
    role: "user",
    content: query
  }];

  const systemPrompt = `You are a research assistant with access to web search and scraping tools. When asked to find specific blog posts on a website, you should:

1. For blog post requests (e.g., "3rd blog post", "5th blog post"):
   - First navigate to the main blog page to see all posts in order
   - Blog posts are typically ordered newest to oldest
   - Count posts as they appear on the page: 1st = newest/top post, 2nd = second from top, etc.
   - For firecrawl.dev: Use "site:firecrawl.dev/blog" to find all blog posts

2. To find the correct blog post:
   - Search with "site:firecrawl.dev/blog" to get the blog listing
   - If needed, scrape the blog index page to see all posts in order
   - Count carefully from the top to identify the correct post by position
   - Then scrape that specific post to get its content

3. Important: When someone asks for the "5th blog post", they mean the 5th post when counting from the newest (top) down, NOT a post with "5" in the title.

Be thorough and methodical. Always verify you have the correct post by its position in the blog listing.`;

  const requestParams = {
    model: "claude-opus-4-20250514",
    max_tokens: 8000,
    system: systemPrompt,
    thinking: {
      type: "enabled" as const,
      budget_tokens: 20000
    },
    tools: tools,
    messages: messages
  };

  // Create request with interleaved thinking
  let response;
  try {
    // Creating Anthropic message with interleaved thinking
    
    response = await getAnthropicClient().beta.messages.create({
      ...requestParams,
      betas: ["interleaved-thinking-2025-05-14"]
    } as Parameters<Anthropic['beta']['messages']['create']>[0]);
  } catch (error) {
    // Failed to create message with beta API
    
    if (error instanceof Error) {
      // Check for specific error types
      if (error.message.includes('model')) {
        throw new Error(`Model error: The claude-opus-4-20250514 model may not be available in your region or with your API key. Error: ${error.message}`);
      }
      if (error.message.includes('beta')) {
        throw new Error(`Beta feature error: The interleaved-thinking-2025-05-14 beta may not be enabled for your account. Error: ${error.message}`);
      }
      if (error.message.includes('authentication') || error.message.includes('401')) {
        throw new Error(`Authentication error: Please check your ANTHROPIC_API_KEY. Error: ${error.message}`);
      }
      // Include full error details for debugging
      // Error details logged internally
    }
    throw error;
  }

  // Track conversation state
  const assistantContent: Array<{ type: string; [key: string]: unknown }> = [];
  let thinkingCount = 0;
  let toolCallCount = 0;
  let currentMessages = [...messages];
  let finalResponse = '';

  // Process response recursively
  async function processResponse(resp: { content: Array<{ type: string; thinking?: string; text?: string; name?: string; input?: Record<string, unknown>; id?: string }> }) {
    for (const block of resp.content) {
      if (block.type === 'thinking') {
        thinkingCount++;
        const thinkingContent = block.thinking || '';
        
        // Send thinking event
        onEvent({
          type: 'thinking',
          number: thinkingCount,
          content: thinkingContent
        });
        
        assistantContent.push(block);
      } else if (block.type === 'tool_use') {
        toolCallCount++;
        const toolDisplayName = block.name === 'web_search' ? 'firecrawl_search' : 
                                 block.name === 'deep_scrape' ? 'firecrawl_scrape' : 
                                 block.name;
        // Executing tool
        
        // Send tool call event
        onEvent({
          type: 'tool_call',
          number: toolCallCount,
          tool: toolDisplayName,
          parameters: block.input
        });
        
        assistantContent.push(block);

        // Execute the tool
        const startTime = Date.now();
        const toolResult = await executeTool(block.name || '', block.input || {});
        const duration = Date.now() - startTime;
        
        // Tool execution completed
        
        // Send tool result event with screenshots if available
        onEvent({
          type: 'tool_result',
          tool: block.name || '',
          duration,
          result: toolResult.content,
          screenshots: toolResult.screenshots
        });

        // Update messages with tool result
        currentMessages = [
          ...currentMessages,
          {
            role: "assistant",
            content: [...assistantContent]
          },
          {
            role: "user",
            content: [{
              type: "tool_result",
              tool_use_id: block.id,
              content: toolResult.content
            }]
          }
        ];

        // Get next response
        const continuationParams = {
          ...requestParams,
          messages: currentMessages
        };

        let nextResponse;
        try {
          nextResponse = await getAnthropicClient().beta.messages.create({
            ...continuationParams,
            betas: ["interleaved-thinking-2025-05-14"]
          } as Parameters<Anthropic['beta']['messages']['create']>[0]);
        } catch (error) {
          // Failed to continue conversation with beta API
          throw error;
        }

        // Clear assistant content for next iteration
        assistantContent.length = 0;

        // Process continuation recursively
        await processResponse(nextResponse as { content: Array<{ type: string; thinking?: string; text?: string; name?: string; input?: Record<string, unknown>; id?: string }> });
        return;
      } else if (block.type === 'text') {
        const textContent = block.text || '';
        // Processing response
        
        // Send final response event
        onEvent({
          type: 'response',
          content: textContent
        });
        
        finalResponse = textContent;
      }
    }
  }

  await processResponse(response as { content: Array<{ type: string; thinking?: string; text?: string; name?: string; input?: Record<string, unknown>; id?: string }> });

  // Research completed
  
  // Send summary event
  onEvent({
    type: 'summary',
    thinkingBlocks: thinkingCount,
    toolCalls: toolCallCount
  });
  
  return finalResponse;
}

// Main research function with interleaved thinking
export async function performResearch(query: string): Promise<string> {
  // Performing research

  const messages: Array<{ role: string; content: string | Array<{ type: string; [key: string]: unknown }> }> = [{
    role: "user",
    content: query
  }];

  const systemPrompt = `You are a research assistant with access to web search and scraping tools. When asked to find specific blog posts on a website, you should:

1. For blog post requests (e.g., "3rd blog post", "5th blog post"):
   - First navigate to the main blog page to see all posts in order
   - Blog posts are typically ordered newest to oldest
   - Count posts as they appear on the page: 1st = newest/top post, 2nd = second from top, etc.
   - For firecrawl.dev: Use "site:firecrawl.dev/blog" to find all blog posts

2. To find the correct blog post:
   - Search with "site:firecrawl.dev/blog" to get the blog listing
   - If needed, scrape the blog index page to see all posts in order
   - Count carefully from the top to identify the correct post by position
   - Then scrape that specific post to get its content

3. Important: When someone asks for the "5th blog post", they mean the 5th post when counting from the newest (top) down, NOT a post with "5" in the title.

Be thorough and methodical. Always verify you have the correct post by its position in the blog listing.`;

  const requestParams = {
    model: "claude-opus-4-20250514",
    max_tokens: 8000,
    system: systemPrompt,
    thinking: {
      type: "enabled" as const,
      budget_tokens: 20000
    },
    tools: tools,
    messages: messages
  };

  // Create request with interleaved thinking
  let response;
  try {
    // Creating Anthropic message with interleaved thinking
    
    response = await getAnthropicClient().beta.messages.create({
      ...requestParams,
      betas: ["interleaved-thinking-2025-05-14"]
    } as Parameters<Anthropic['beta']['messages']['create']>[0]);
  } catch (error) {
    // Failed to create message with beta API
    
    if (error instanceof Error) {
      // Check for specific error types
      if (error.message.includes('model')) {
        throw new Error(`Model error: The claude-opus-4-20250514 model may not be available in your region or with your API key. Error: ${error.message}`);
      }
      if (error.message.includes('beta')) {
        throw new Error(`Beta feature error: The interleaved-thinking-2025-05-14 beta may not be enabled for your account. Error: ${error.message}`);
      }
      if (error.message.includes('authentication') || error.message.includes('401')) {
        throw new Error(`Authentication error: Please check your ANTHROPIC_API_KEY. Error: ${error.message}`);
      }
      // Include full error details for debugging
      // Error details logged internally
    }
    throw error;
  }

  // Track conversation state
  const assistantContent: Array<{ type: string; [key: string]: unknown }> = [];
  let thinkingCount = 0;
  let toolCallCount = 0;
  let currentMessages = [...messages];
  let finalResponse = '';

  // Process response recursively
  async function processResponse(resp: { content: Array<{ type: string; thinking?: string; text?: string; name?: string; input?: Record<string, unknown>; id?: string }> }) {
    for (const block of resp.content) {
      if (block.type === 'thinking') {
        thinkingCount++;
        const thinkingContent = block.thinking || '';
        assistantContent.push(block);
      } else if (block.type === 'tool_use') {
        toolCallCount++;
        const toolDisplayName = block.name === 'web_search' ? 'firecrawl_search' : 
                                 block.name === 'deep_scrape' ? 'firecrawl_scrape' : 
                                 block.name;
        // Executing tool
        assistantContent.push(block);

        // Execute the tool
        const startTime = Date.now();
        const toolResult = await executeTool(block.name || '', block.input || {});
        const duration = Date.now() - startTime;
        
        // Tool execution completed

        // Update messages with tool result
        currentMessages = [
          ...currentMessages,
          {
            role: "assistant",
            content: [...assistantContent]
          },
          {
            role: "user",
            content: [{
              type: "tool_result",
              tool_use_id: block.id,
              content: toolResult.content
            }]
          }
        ];

        // Get next response
        const continuationParams = {
          ...requestParams,
          messages: currentMessages
        };

        let nextResponse;
        try {
          nextResponse = await getAnthropicClient().beta.messages.create({
            ...continuationParams,
            betas: ["interleaved-thinking-2025-05-14"]
          } as Parameters<Anthropic['beta']['messages']['create']>[0]);
        } catch (error) {
          // Failed to continue conversation with beta API
          throw error;
        }

        // Clear assistant content for next iteration
        assistantContent.length = 0;

        // Process continuation recursively
        await processResponse(nextResponse as { content: Array<{ type: string; thinking?: string; text?: string; name?: string; input?: Record<string, unknown>; id?: string }> });
        return;
      } else if (block.type === 'text') {
        const textContent = block.text || '';
        // Processing response
        finalResponse = textContent;
      }
    }
  }

  await processResponse(response as { content: Array<{ type: string; thinking?: string; text?: string; name?: string; input?: Record<string, unknown>; id?: string }> });

  // Research completed
  
  return finalResponse;
}
```

## File: `lib/utils.ts`
```typescript
import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
```


---
id: github.com-gkamradt-agenttrafficcontrol-c5901f85-k
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:53.732635
---

# KNOWLEDGE EXTRACT: github.com_gkamradt_agenttrafficcontrol_c5901f85
> **Extracted on:** 2026-04-01 16:22:14
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007525075/github.com_gkamradt_agenttrafficcontrol_c5901f85

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

.planning/
.claude/
```

## File: `README.md`
```markdown
# Agent Traffic Control

A minimal Next.js dashboard to monitor and control AI agent traffic. View live at https://agenttrafficcontrol.com.

Best with full screen and sound on.

![Agent Traffic Control](homepage.png)

## Getting Started

```bash
git clone https://github.com/gkamradt/agenttrafficcontrol && cd agenttrafficcontrol
npm install
cp .env.example .env  # add your keys if needed
npm run dev
# Open http://localhost:3000
```

## How It Works

On first load the client establishes a connection to a dedicated Web Worker engine (`workers/engine.ts`). Runtime knobs live in `lib/config.ts` and the engine loads a plan definition from `plans/` to build the initial project graph.

The UI immediately sends intents to the worker (set seed → set plan → start running) and the engine begins ticking at `ENGINE_TICK_HZ`, emitting a full `snapshot` once and `tick` diffs thereafter.

Worker messages flow through a tiny transport (`lib/simBridge.ts`) that batches events, then into a coalescing adapter (`lib/bridgeToStore.ts`) that applies them to a single Zustand store (`lib/store.ts`).

All React components read from this store; controls like `components/ControlBar.tsx` post intents (change plan, start/pause, reseed) back to the engine. The store is the UI’s source of truth; the engine is the simulation’s source of truth.

Includes live streams for ambiance:

- ATC: https://www.youtube.com/watch?v=mOec9Fu3Jz0
- Music: https://www.youtube.com/watch?v=jfKfPfyJRdk

## Architecture

```
          .env + lib/config.ts        plans/
                   │                    │
                   ▼                    ▼
             Web Worker Engine  <─ loads plan
                 (ticks)
                   │  snapshot/tick
                   ▼
             lib/simBridge.ts   (batch)
                   │
                   ▼
          lib/bridgeToStore.ts  (coalesce)
                   │
                   ▼
              lib/store.ts  (Zustand appStore)
                   │
                   ▼
            React components (read state)
                   ▲
                   │ intents (set_plan, set_seed, set_running)
          components/ControlBar.tsx via lib/simClient.ts
```
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
  {
    ignores: [
      "node_modules/**",
      ".next/**",
      "out/**",
      "build/**",
      "next-env.d.ts",
    ],
  },
];

export default eslintConfig;
```

## File: `next.config.ts`
```typescript
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  webpack: (config) => {
    // Add support for importing Web Workers
    config.module.rules.push({
      test: /\.worker\.(js|ts)$/,
      type: 'vault/assets/resource',
      generator: {
        filename: 'static/[hash][ext][query]',
      },
    });
    
    return config;
  },
};

export default nextConfig;
```

## File: `package.json`
```json
{
  "name": "calming-control-room",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "eslint",
    "test": "vitest",
    "test:ui": "vitest --ui",
    "test:run": "vitest run",
    "test:coverage": "vitest run --coverage"
  },
  "dependencies": {
    "@vercel/analytics": "^1.5.0",
    "next": "15.5.2",
    "react": "19.1.0",
    "react-dom": "19.1.0",
    "zustand": "^5.0.8"
  },
  "devDependencies": {
    "@eslint/eslintrc": "^3",
    "@tailwindcss/postcss": "^4",
    "@testing-library/dom": "^10.4.1",
    "@testing-library/jest-dom": "^6.8.0",
    "@testing-library/react": "^16.3.0",
    "@testing-library/user-event": "^14.6.1",
    "@types/node": "^20",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "@vitejs/plugin-react": "^5.0.2",
    "comlink-loader": "^2.0.0",
    "eslint": "^9",
    "eslint-config-next": "15.5.2",
    "jsdom": "^26.1.0",
    "tailwindcss": "^4",
    "typescript": "^5",
    "vitest": "^3.2.4",
    "worker-loader": "^3.0.8"
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

## File: `vitest.config.mts`
```
import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';
import path from 'path';

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    globals: true,
    setupFiles: './vitest.setup.ts',
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './'),
    },
  },
});
```

## File: `vitest.setup.ts`
```typescript
import '@testing-library/jest-dom';
```

## File: `app/globals.css`
```css
@import "tailwindcss";

:root {
  --background: #000000; /* Force full black */
  --foreground: #ededed;
  /* Global theme colors */
  --green-bright: #57ff7a;
  /* UI label variables (used for small section titles/badges) */
  --ui-label-font-size: 0.8rem; /* ~10px, about half of text-lg */
  --ui-label-line-height: 1.15;
  --ui-label-py: 0.125rem; /* 2px */
  --ui-label-px: 0.5rem;   /* 8px */
  --ui-label-bg: #c79325ff; /* Tailwind yellow-300 */
  --ui-label-fg: #000000;
  /* Consistent header row height for section headers */
  --ui-header-row-height: 28px;
  /* Row status colors (easy to tweak) */
  --row-done-bg: #05291dff;        /* emerald-800 */
  --row-done-fg: #047f54ff;        /* emerald-200 */
  --row-inprog-bg: #212107ff;      /* amber-900 */
  --row-inprog-fg: #9aa40aff;      /* amber-300 */
  --row-queued-bg: #0e1d46;      /* blue-800 */
  --row-queued-fg: #8aa9cf;      /* blue-200 */
}

@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  /* Map Tailwind font tokens to Source Code Pro */
  --font-sans: var(--font-jet-brains-mono);
  --font-mono: var(--font-jet-brains-mono);
}

@media (prefers-color-scheme: dark) {
  :root {
    --background: #000000; /* Full black in dark mode too */
    --foreground: #ededed;
  }
}

body {
  background: var(--background);
  color: var(--foreground);
}

/* Reusable small title/label style for consistent height */
.ui-label {
  display: inline-flex;
  align-items: center;
  font-size: var(--ui-label-font-size);
  line-height: var(--ui-label-line-height);
  padding: var(--ui-label-py) var(--ui-label-px);
  background: var(--ui-label-bg);
  color: var(--ui-label-fg);
  font-weight: 700; /* use Bold face we loaded */
}

/* Variant: make it look like a tab sitting on the card border */
.ui-label--tab {
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 0;
  margin-top: -1px; /* overlap the top border for a flush tab look */
}

/* Tighter horizontal padding (≈2px each side) */
.ui-label--tight {
  padding-left: 0.125rem;  /* 2px */
  padding-right: 0.125rem; /* 2px */
}

/* Make the label fill the container height */
.ui-label--fill {
  height: 100%;
}

/* Utility to hide scrollbars while enabling scroll */
.no-scrollbar {
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
}
.no-scrollbar::-webkit-scrollbar {
  display: none; /* Chrome, Safari and Opera */
}

/* Table row status helpers */
.tr-status-done {
  background-color: var(--row-done-bg) !important;
  color: var(--row-done-fg) !important;
}
.tr-status-inprogress {
  background-color: var(--row-inprog-bg) !important;
  color: var(--row-inprog-fg) !important;
}
.tr-status-queued {
  background-color: var(--row-queued-bg) !important;
  color: var(--row-queued-fg) !important;
}
```

## File: `app/layout.tsx`
```tsx
import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import localFont from "next/font/local";
import "./globals.css";
import { Analytics } from "@vercel/analytics/next"

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

// Local font: Source Code Pro Regular (applied globally via Tailwind token mapping)
const sourceCodePro = localFont({
  src: [
    {
      path: "../public/fonts/source-code-pro/SourceCodePro-Regular.ttf",
      weight: "400",
      style: "normal",
    },
    {
      path: "../public/fonts/source-code-pro/SourceCodePro-Bold.ttf",
      weight: "700",
      style: "normal",
    },
  ],
  variable: "--font-source-code-pro",
  display: "swap",
});

// Local font: Source Code Pro Regular (applied globally via Tailwind token mapping)
const jetBrainsMono = localFont({
  src: [
    {
      path: "../public/fonts/jet-brains-mono/JetBrainsMono-Regular.ttf",
      weight: "400",
      style: "normal",
    },
    {
      path: "../public/fonts/jet-brains-mono/JetBrainsMono-Bold.ttf",
      weight: "700",
      style: "normal",
    },
  ],
  variable: "--font-jet-brains-mono",
  display: "swap",
});

export const metadata: Metadata = {
  // Helps Next generate absolute URLs for OG/Twitter images
  metadataBase: new URL(process.env.NEXT_PUBLIC_SITE_URL || "http://localhost:3000"),
  title: "Agent Traffic Control (ATC)",
  description: "Direct the vibe of your agents in the Agent Traffic Control Room",
  openGraph: {
    title: "Agent Traffic Control (ATC)",
    description: "Direct the vibe of your agents in the Agent Traffic Control Room",
    type: "website",
    url: "/",
    siteName: "Agent Traffic Control (ATC)",
    images: [
      {
        url: "/images/ATC_OG.png",
        width: 2048,
        height: 1280,
        alt: "Agent Traffic Control (ATC)",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "Agent Traffic Control (ATC)",
    description: "Direct the vibe of your agents in the Agent Traffic Control Room",
    images: ["/images/ATC_OG.png"],
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      
      <body
        className={`${geistSans.variable} ${geistMono.variable} ${sourceCodePro.variable} ${jetBrainsMono.variable} antialiased font-sans`}
      >
        {children}
        <Analytics />
      </body>
    </html>
  );
}
```

## File: `app/page.test.tsx`
```tsx
import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import Home from './page';

describe('renders-root', () => {
  it('renders the root page and shows sentinel text', () => {
    render(<Home />);
    
    const heading = screen.getByText('Calming Control Room');
    expect(heading).toBeInTheDocument();
  });
});
```

## File: `app/page.tsx`
```tsx
import WorkTable from '../components/WorkTable';
import ControlBar from '../components/ControlBar';
import RadarCanvas from '../components/RadarCanvas';
import GlobalQueue from '../components/GlobalQueue';
import ProjectIdDisplay from '../components/ProjectIdDisplay';
import ProjectDescription from '../components/ProjectDescription';
import OperatorGroups from '../components/OperatorGroups';
import TopOverview from '../components/TopOverview';
import TimelineStatusBar from '../components/TimelineStatusBar';

export default function Home() {
  return (
    <div className="h-screen overflow-hidden bg-black text-white flex flex-col">
      {/* Header */}
      <header className="p-4">
        <h1 className="text-2xl tracking-tighter font-bold text-gray-500 text-spacing-px">AGENT TRAFFIC CONTROL</h1>
        <p className="mt-1 text-[10px] leading-none text-gray-500">
          <a
            href="https://github.com/gkamradt/agenttrafficcontrol"
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-gray-400 italic underline"
          >
            OPEN SOURCE
          </a>
          <span className="px-1">•</span>
          <a
            href="https://x.com/gregkamradt"
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-gray-400 italic underline"
          >
            BY GREG
          </a>
        </p>
      </header>

      {/* Controls row */}
      <div className="border-t border-gray-800" />

      {/* Main layout */}
      <main className="flex-1 overflow-hidden p-4">
        {/* Desktop layout (unchanged) */}
        <div className="hidden lg:grid grid-cols-1 lg:grid-cols-[30%_70%] gap-4 h-full min-h-0">
          {/* LEFT COLUMN: 3 rows -> [Monitoring (auto), Operator Actions (auto), Work/Agent table (1fr = remaining space)] */}
          <section className="min-h-0 overflow-hidden grid grid-rows-[auto_auto_1fr]">
            {/* Monitoring table (top) with three internal rows */}
            <div className="min-h-0 overflow-hidden flex flex-col">

              <div className="flex items-center bg-[#130f04ff]">
                <h2 className="bg-[#c79325] pl-2 pr-2 font-bold text-black">MONITORING TABLE</h2>
              </div>

              <div className="grid grid-cols-[20%_1fr] gap-0 border border-[#352b19ff]" style={{ minHeight: 'auto' }}>
                {/* Column 1: 2 parts wide */}
                <div className="border-r border-[#352b19ff] p-3">
                  <div className="text-xs text-[#d79326ff] mb-1">Project ID</div>
                  <div className="text-sm text-[#a4a4a4ff]"><ProjectIdDisplay /></div>
                </div>
                {/* Column 2: 1 part wide */}
                <div className="p-3">
                  <div className="text-xs text-[#c89225ff] mb-1">Project Description</div>
                  <div className="text-sm text-[#a4a4a4ff]"><ProjectDescription /></div>
                </div>
              </div>
            </div>

            {/* Operator Action Items (middle) */}
            <div className="min-h-0 overflow-hidden border border-[#352b19ff] bg-black border-b-0 flex flex-col">
              <div className="flex items-center border-b-3 border-[#352b19ff]">
                <h2 className="text-lg text-[#d79326ff] pl-2 pr-2">OPERATOR ACTION ITEMS</h2>
              </div>
              <div className="flex-1 min-h-0 overflow-auto">
                <OperatorGroups />
              </div>
            </div>

            {/* Work/Agent table (bottom, 75% height) */}
            <div className="min-h-0 overflow-hidden">
              <WorkTable />
            </div>
          </section>

          {/* RIGHT COLUMN: rows -> [Top (1fr), Radar area (7fr), Master Control Panel (auto)] */}
          <aside className="h-full min-h-0 overflow-hidden grid grid-rows-[1fr_7fr_auto] gap-3">
            {/* Top row (same height as Monitoring row). Keep MetricsBar here. */}
            <div className="min-h-0 overflow-hidden bg-black">
              <TopOverview />
            </div>

            {/* Radar row with Global Q header and 10%/90% split below */}
            <div className="min-h-0 overflow-hidden flex flex-col">
              {/* Full-width header bar with yellow tab, like Monitoring */}
              <div className="flex items-center" style={{ backgroundColor: '#130f04ff' }}>
                <div style={{ width: '8%', backgroundColor: '#c79325' }}>
                  <h2 className="pl-2 pr-2 font-bold text-black">GLOBAL QUEUE</h2>
                </div>
              </div>
              {/* Two-column area: 10% ActionItems | 90% Radar */}
              <div className="min-h-0 overflow-hidden grid" style={{ gridTemplateColumns: '8% 92%' }}>
                {/* Global Queue (left, full radar height) */}
                <div className="border-r border-[#352b19ff] bg-black min-h-0 overflow-hidden">
                  <GlobalQueue />
                </div>
                {/* Radar (right) */}
                <div className="min-h-0 overflow-hidden bg-black">
                  <RadarCanvas />
                </div>
              </div>
            </div>

            {/* Master Control Panel (bottom) */}
            <div className="mt-1">
              <div className="flex items-center bg-[#130f04ff]">
                <h2 className="bg-[#c79325] pl-2 pr-2 font-bold text-black">MASTER CONTROL PANEL</h2>
              </div>
              <div className="border border-gray-800 bg-black">
                <div className="px-2 pt-2">
                  <TimelineStatusBar />
                </div>
                <ControlBar />
              </div>
            </div>
          </aside>
        </div>

        {/* Mobile layout */}
        <div className="block lg:hidden h-full min-h-0 overflow-auto">
          <div className="flex flex-col gap-3 p-1">
            {/* Top line metrics (compact, hide completion chart) */}
            <div className="min-h-0">
              <TopOverview compact hideCompletion />
            </div>

            {/* Radar (no global queue) */}
            <div className="min-h-0">
              <div className="flex items-center bg-[#130f04ff]">
                <h2 className="bg-[#c79325] pl-2 pr-2 font-bold text-black">RADAR</h2>
              </div>
              <div className="border border-[#352b19ff] bg-black" style={{ height: 260 }}>
                <RadarCanvas />
              </div>
            </div>

            {/* Work items table (compact + mini text, capped height with internal scroll) */}
            <div className="min-h-0">
              <div className="flex items-center bg-[#130f04ff]">
                <h2 className="bg-[#c79325] pl-2 pr-2 font-bold text-black">WORK ITEMS</h2>
              </div>
              <div className="min-h-0 overflow-hidden">
                <WorkTable compact mini maxHeight={390} columns={['id','work','tokens','eta']} />
              </div>
            </div>

            {/* Project details (ID + Description) */}
            <div className="min-h-0">
              <div className="flex items-center bg-[#130f04ff]">
                <h2 className="bg-[#c79325] pl-2 pr-2 font-bold text-black">PROJECT</h2>
              </div>
              <div className="grid grid-cols-[35%_1fr] border border-[#352b19ff] bg-black">
                <div className="border-r border-[#352b19ff] p-2">
                  <div className="text-xs text-[#d79326ff] mb-1">Project ID</div>
                  <div className="text-sm text-[#a4a4a4ff]"><ProjectIdDisplay /></div>
                </div>
                <div className="p-2">
                  <div className="text-xs text-[#c89225ff] mb-1">Project Description</div>
                  <div className="text-sm text-[#a4a4a4ff]"><ProjectDescription /></div>
                </div>
              </div>
            </div>

            {/* Master Control Panel */}
            <div className="min-h-0">
              <div className="flex items-center bg-[#130f04ff]">
                <h2 className="bg-[#c79325] pl-2 pr-2 font-bold text-black">MASTER CONTROL PANEL</h2>
              </div>
              <div className="border border-gray-800 bg-black">
                <div className="px-2 pt-2">
                  <TimelineStatusBar />
                </div>
                <ControlBar />
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
```

## File: `app/test-worker.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Worker Test</title>
</head>
<body>
    <h1>Worker Test</h1>
    <div id="status">Loading...</div>
    <div id="tick">Tick: 0</div>
    <button id="toggle">Run/Pause</button>
    
    <script>
        const worker = new Worker('/workers/engine.worker.ts', { type: 'module' });
        let running = false;
        let tickCount = 0;
        
        worker.onmessage = (e) => {
            console.log('Message from worker:', e.data);
            document.getElementById('status').textContent = 'Connected: ' + JSON.stringify(e.data);
            
            if (e.data.type === 'tick') {
                tickCount = e.data.tick_id;
                document.getElementById('tick').textContent = 'Tick: ' + tickCount;
            }
            
            if (e.data.type === 'snapshot') {
                running = e.data.state.running;
            }
        };
        
        document.getElementById('toggle').onclick = () => {
            running = !running;
            worker.postMessage({ type: 'set_running', running });
        };
    </script>
</body>
</html>
```

## File: `components/AudioPlayer.tsx`
```tsx
"use client";

import React, { useEffect, useMemo, useRef, useState, useId } from 'react';
import type { Track } from '@/lib/audio/tracks';

type YouTubePlayer = {
  pauseVideo?: () => void;
  playVideo?: () => void;
  loadVideoById?: (videoId: string) => void;
  cueVideoById?: (videoId: string) => void;
  getPlayerState?: () => number;
};

type YouTubeAPI = {
  Player: new (element: HTMLElement, options: {
    width: number;
    height: number;
    playerVars: Record<string, number>;
    events: {
      onReady: () => void;
      onStateChange: (e: { data: number }) => void;
    };
  }) => YouTubePlayer;
};

type Props = {
  tracks: Track[];
  initialIndex?: number;
  className?: string;
  showSourceLink?: boolean;
};

export default function AudioPlayer({ tracks, initialIndex = 0, className = '', showSourceLink = false }: Props) {
  const validTracks = useMemo(() => tracks.filter(Boolean), [tracks]);
  const [index, setIndex] = useState(Math.min(Math.max(0, initialIndex), Math.max(0, validTracks.length - 1)));
  const [isPlaying, setIsPlaying] = useState(false);
  const ytPlayerRef = useRef<YouTubePlayer | null>(null);
  const ytWrapperRef = useRef<HTMLDivElement | null>(null);
  const rid = useId();
  const ytInnerId = useMemo(() => 'ytp-' + rid.replace(/[:]/g, ''), [rid]);

  const current = validTracks[index];
  const isYouTube = current?.source.type === 'youtube';

  // --- Helpers ---
  const getYouTubeId = (url: string): string | null => {
    try {
      const u = new URL(url);
      if (u.hostname === 'youtu.be') {
        return u.pathname.split('/')[1] || null;
      }
      if (u.hostname.includes('youtube.com')) {
        if (u.pathname === '/watch') return u.searchParams.get('v');
        // e.g., /live/<id> or /embed/<id>
        const parts = u.pathname.split('/').filter(Boolean);
        if (parts.length >= 2 && (parts[0] === 'live' || parts[0] === 'embed')) return parts[1];
      }
    } catch {}
    return null;
  };

  const ensureYouTubeAPI = (): Promise<YouTubeAPI | null> => {
    return new Promise((resolve) => {
      if (typeof window === 'undefined') return resolve(null);
      const w = window as Window & { YT?: YouTubeAPI };
      if (w.YT && w.YT.Player) return resolve(w.YT);
      // Inject script once
      const existing = document.getElementById('yt-iframe-api');
      if (!existing) {
        const s = document.createElement('script');
        s.id = 'yt-iframe-api';
        s.src = 'https://www.youtube.com/iframe_api';
        document.head.appendChild(s);
      }
      const check = () => {
        if (w.YT && w.YT.Player) resolve(w.YT);
        else setTimeout(check, 50);
      };
      check();
    });
  };

  // (local audio removed)

  // Handle YouTube player lifecycle and play/pause sync
  useEffect(() => {
    if (!isYouTube) {
      // Pause YT when leaving a YT track
      if (ytPlayerRef.current) {
        try { ytPlayerRef.current.pauseVideo?.(); } catch {}
      }
      return;
    }

    const src = current && current.source.type === 'youtube' ? current.source.url : '';
    const videoId = src ? getYouTubeId(src) : null;
    if (!videoId) {
      console.warn('AudioPlayer: Could not parse YouTube video ID from', src);
      return;
    }

    let cancelled = false;
    ensureYouTubeAPI().then((YT) => {
      if (cancelled || !YT) return;
      const mountTarget = document.getElementById(ytInnerId) as HTMLElement | null;
      if (!mountTarget) return;
      // Create player if needed
      if (!ytPlayerRef.current) {
        ytPlayerRef.current = new YT.Player(mountTarget, {
          width: 0,
          height: 0,
          playerVars: {
            autoplay: 0,
            controls: 0,
            rel: 0,
            modestbranding: 1,
            playsinline: 1,
          },
          events: {
            onReady: () => {
              // Load or cue based on desired state
              if (isPlaying) {
                ytPlayerRef.current?.loadVideoById?.(videoId);
                // Nudge play in case autoplay fails without a direct gesture
                setTimeout(() => { try { ytPlayerRef.current?.playVideo?.(); } catch {} }, 0);
              } else {
                ytPlayerRef.current?.cueVideoById?.(videoId);
              }
            },
            onStateChange: (e: { data: number }) => {
              // Sync UI with player state
              if (e.data === 1) setIsPlaying(true); // playing
              else if (e.data === 2 || e.data === 0) setIsPlaying(false); // paused or ended
              else if (e.data === 5 && isPlaying) {
                // CUED but we want to play
                try { ytPlayerRef.current?.playVideo?.(); } catch {}
              }
            },
          },
        });
      } else {
        // Reuse player
        try {
          if (isPlaying) {
            ytPlayerRef.current.loadVideoById?.(videoId);
            // Ensure it actually starts
            try { ytPlayerRef.current.playVideo?.(); } catch {}
          } else {
            ytPlayerRef.current.cueVideoById?.(videoId);
          }
        } catch {}
      }
    });

    return () => {
      cancelled = true;
    };
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [index, isYouTube]);

  // React to play/pause toggle for YouTube
  useEffect(() => {
    if (!isYouTube || !ytPlayerRef.current) return;
    try {
      if (isPlaying) ytPlayerRef.current.playVideo?.();
      else ytPlayerRef.current.pauseVideo?.();
    } catch {}
  }, [isPlaying, isYouTube]);

  // If autoplay is blocked or fails, sync UI back to Play after a short check
  useEffect(() => {
    if (!isYouTube || !isPlaying || !ytPlayerRef.current) return;
    const id = setTimeout(() => {
      try {
        const state = ytPlayerRef.current?.getPlayerState?.();
        // 1: PLAYING, 3: BUFFERING
        if (state !== 1 && state !== 3) setIsPlaying(false);
      } catch {}
    }, 800);
    return () => clearTimeout(id);
  }, [index, isYouTube, isPlaying]);

  // If track list updates and index goes out of range
  useEffect(() => {
    if (index >= validTracks.length) setIndex(Math.max(0, validTracks.length - 1));
  }, [validTracks.length, index]);

  const onPrev = () => {
    if (!validTracks.length) return;
    setIndex((i) => {
      const nextIdx = (i - 1 + validTracks.length) % validTracks.length;
      const t = validTracks[nextIdx];
      // Always autoplay when navigating
      setIsPlaying(true);
      // If next is YouTube and player exists, load immediately in this user gesture
      if (t?.source.type === 'youtube' && ytPlayerRef.current) {
        const id = getYouTubeId(t.source.url);
        if (id) {
          try {
            ytPlayerRef.current.loadVideoById?.(id);
            ytPlayerRef.current.playVideo?.();
          } catch {}
        }
      }
      return nextIdx;
    });
  };

  const onToggle = () => {
    if (!current || !isYouTube) return;
    setIsPlaying((p) => !p);
  };

  const onNext = () => {
    if (!validTracks.length) return;
    setIndex((i) => {
      const nextIdx = (i + 1) % validTracks.length;
      const t = validTracks[nextIdx];
      // Always autoplay when navigating
      setIsPlaying(true);
      // If next is YouTube and player exists, load immediately in this user gesture
      if (t?.source.type === 'youtube' && ytPlayerRef.current) {
        const id = getYouTubeId(t.source.url);
        if (id) {
          try {
            ytPlayerRef.current.loadVideoById?.(id);
            ytPlayerRef.current.playVideo?.();
          } catch {}
        }
      }
      return nextIdx;
    });
  };

  // No autoplay on initial mount; start on user gesture

  return (
    <div className={`flex flex-col items-end gap-1 text-sm ${className}`}>
      {/* Hidden YouTube player container for YouTube tracks */}
      <div ref={ytWrapperRef} style={{ width: 0, height: 0, overflow: 'hidden' }} aria-hidden>
        <div id={ytInnerId} />
      </div>

      {/* Title row (full length) with optional source link */}
      <div className="text-gray-300 flex items-center gap-2" title={current?.title || ''}>
        <span>{current ? current.title : 'No track'}</span>
        {showSourceLink && isYouTube && current && current.source.type === 'youtube'}
      </div>

      {/* Controls row (fixed position under title) */}
      <div className="flex items-center gap-2">
        <button
          onClick={onPrev}
          className="px-2 py-1 border border-gray-600 text-gray-200"
          title="Back"
          aria-label="Back"
          disabled={!validTracks.length}
        >⏮</button>
        <button
          onClick={onToggle}
          className="px-2 py-1 border border-gray-600 text-gray-200"
          title={isPlaying ? 'Pause' : 'Play'}
          aria-label={isPlaying ? 'Pause' : 'Play'}
        disabled={!current || !isYouTube}
      >{isPlaying ? '⏸' : '▶'}</button>
        <button
          onClick={onNext}
          className="px-2 py-1 border border-gray-600 text-gray-200"
          title="Next"
          aria-label="Next"
          disabled={!validTracks.length}
        >⏭</button>
      </div>
    </div>
  );
}
```

## File: `components/ControlBar.tsx`
```tsx
"use client";

import React, { useEffect, useState, useSyncExternalStore } from 'react';
import { ensureConnected, postIntent } from '@/lib/simClient';
import AudioPlayer from '@/components/AudioPlayer';
import { tracks, radio } from '@/lib/audio/tracks';
import { PLAN_NAMES, DEFAULT_PLAN_NAME } from '@/plans';
import { appStore } from '@/lib/store';

const LS_PREFIX = 'ccr.';
const LS = {
  plan: LS_PREFIX + 'plan',
  speed: LS_PREFIX + 'speed',
};

export default function ControlBar() {
  const [plan, setPlan] = useState<string>(DEFAULT_PLAN_NAME);
  const pingEnabled = useSyncExternalStore(
    appStore.subscribe,
    () => appStore.getState().pingAudioEnabled,
    () => appStore.getState().pingAudioEnabled,
  );
  // Speed controls temporarily removed for stability
  // No longer exposing running/pause in UI

  useEffect(() => {
    ensureConnected();
    // On first mount, set seed, apply plan, then start running
    try {
      const stored = localStorage.getItem(LS.plan) || DEFAULT_PLAN_NAME;
      setPlan(stored);
      // Reflect selected plan in global UI store for ProjectId/Description
      try { appStore.getState().setPlanName(stored); } catch {}
      const url = new URL(window.location.href);
      const urlSeed = url.searchParams.get('seed');
      const randomSeed = `r${Date.now().toString(36)}${Math.random().toString(36).slice(2, 8)}`;
      postIntent({ type: 'set_seed', seed: urlSeed || randomSeed });
      // Apply plan before starting engine to avoid pause from later set_plan
      postIntent({ type: 'set_plan', plan: stored });
      // Start the engine automatically
      postIntent({ type: 'set_running', running: true });
      // Snapshot to sync UI quickly
      postIntent({ type: 'request_snapshot' });
    } catch {}
  }, []);

  // Persist plan whenever it changes (engine is only updated via Execute or initial mount)
  useEffect(() => {
    // Persist the user's selection, but do NOT update the displayed
    // project id/description until Execute is clicked.
    try { localStorage.setItem(LS.plan, plan); } catch {}
  }, [plan]);
  // Speed persistence removed
  // running state persistence removed

  return (
    <div className="px-2 py-2 flex flex-wrap gap-2 items-center">
      <label className="text-sm text-gray-300">Project</label>
      <select
        value={plan}
        onChange={(e) => setPlan(e.target.value)}
        className="bg-black border border-gray-700 px-2 py-1 text-sm h-8 text-gray-100"
      >
        {PLAN_NAMES.map((p) => (
          <option key={p} value={p}>{p}</option>
        ))}
      </select>
      <button
        onClick={() => {
          // Apply plan and immediately start running
          postIntent({ type: 'set_plan', plan: plan });
          postIntent({ type: 'set_running', running: true });
          postIntent({ type: 'request_snapshot' });
          // Reflect applied plan in the UI after executing
          try { appStore.getState().setPlanName(plan); } catch {}
        }}
        className="text-xs px-2 py-1 border border-gray-600 text-gray-200 h-8"
      >Execute</button>

      {/* Speed controls removed for now */}

      {/* Right-aligned players: Radio + Music + Ping toggle */}
      <div className="ml-auto flex items-end gap-6">
        {/* Radar ping sound toggle with label above (SFX) */}
        <div className="flex flex-col items-end gap-1 text-sm">
          <div className="text-gray-300 select-none">SFX</div>
          <button
            type="button"
            onClick={() => appStore.getState().togglePingAudio()}
            title={pingEnabled ? 'Radar ping sound: ON' : 'Radar ping sound: OFF'}
            className={`h-8 w-8 grid place-items-center border ${pingEnabled ? 'border-green-500/70 text-green-400' : 'border-gray-600 text-gray-300'} bg-black hover:bg-gray-900`}
            aria-pressed={pingEnabled}
            aria-label={pingEnabled ? 'Disable radar ping sound' : 'Enable radar ping sound'}
          >
            {pingEnabled ? (
              // Speaker with waves (on)
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
                <path d="M3 10h3l4-3v10l-4-3H3z" fill="currentColor" stroke="none" />
                <path d="M15 9c1.5 1.5 1.5 4.5 0 6" />
                <path d="M17.5 7c2.5 2.5 2.5 7.5 0 10" />
                <path d="M20 5c3.3 3.3 3.3 10.7 0 14" />
              </svg>
            ) : (
              // Speaker with X (muted)
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
                <path d="M3 10h3l4-3v10l-4-3H3z" fill="currentColor" stroke="none" />
                <path d="M16 8l6 6" />
                <path d="M22 8l-6 6" />
              </svg>
            )}
          </button>
        </div>
        <AudioPlayer tracks={radio} showSourceLink className="text-right" />
        <AudioPlayer tracks={tracks} className="text-right" />
      </div>
    </div>
  );
}
```

## File: `components/GlobalQueue.tsx`
```tsx
"use client";

import React, { useMemo, useSyncExternalStore } from 'react';
import { appStore } from '@/lib/store';
import type { UIState } from '@/lib/store';
import type { WorkItem } from '@/lib/types';
import { SECTORS } from '@/lib/constants';

function useAppSelector<T>(selector: (s: UIState) => T): T {
  return useSyncExternalStore(
    appStore.subscribe,
    () => selector(appStore.getState()),
    () => selector(appStore.getState())
  );
}

type Bucket = {
  active: WorkItem[];
  upNext: WorkItem[];
  queue: WorkItem[];
};

export default function GlobalQueue() {
  const items = useAppSelector((s) => s.items);

  const bySector = useMemo(() => {
    const buckets = new Map<string, Bucket>();
    for (const sec of SECTORS) buckets.set(sec, { active: [], upNext: [], queue: [] });
    for (const it of Object.values(items)) {
      if (it.status === 'done') continue; // drop completed
      const sec = (it.sector || '').toUpperCase();
      if (!buckets.has(sec)) buckets.set(sec, { active: [], upNext: [], queue: [] });
      const b = buckets.get(sec)!;
      if (it.status === 'in_progress') b.active.push(it);
      else if (it.status === 'assigned') b.upNext.push(it);
      else b.queue.push(it); // queued/blocked/default
    }
    // stable sort by id for readability
    for (const b of buckets.values()) {
      b.active.sort((a, z) => a.id.localeCompare(z.id));
      b.upNext.sort((a, z) => a.id.localeCompare(z.id));
      b.queue.sort((a, z) => a.id.localeCompare(z.id));
    }
    return buckets;
  }, [items]);

  return (
    <div className="h-full min-h-0 bg-black">
      {/* 4 equal-height sector panes; scroll inside each */}
      <div className="grid grid-rows-4 h-full min-h-0">
        {SECTORS.map((sec, idx) => {
          const b = bySector.get(sec) || { active: [], upNext: [], queue: [] };
          const nextList = b.upNext.length > 0 ? b.upNext : (b.queue.length > 0 ? [b.queue[0]] : []);
          const remaining = b.upNext.length > 0 ? b.queue : b.queue.slice(1);
          return (
            <section key={sec} className={`min-h-0 overflow-hidden ${idx < SECTORS.length - 1 ? '' : ''}`}> 
              {/* Sector header styled like WorkTable headers */}
              <div className="px-2 pt-1 pb-1 text-[#d79326ff] border-b-1 text-xs font-semibold tracking-tight">
                {sec}
              </div>
              <div className="flex-1 min-h-0 overflow-auto no-scrollbar space-y-1">
                {/* Active */}
                {b.active.length > 0 && (
                  <div className="space-y-1">
                    {b.active.map((it) => (
                      <Row key={`act-${it.id}`} tone="active" label="ACTIVE" it={it} />
                    ))}
                  </div>
                )}

                {/* Up next: prefer assigned; else first queued item */}
                {nextList.length > 0 && (
                  <div className="space-y-1">
                    {nextList.map((it) => (
                      <Row key={`next-${it.id}`} tone="upnext" label="UP NEXT" it={it} />
                    ))}
                  </div>
                )}

                {/* Remaining queue (skip the first if it was promoted) */}
                {remaining.length > 0 ? (
                  <div className="space-y-1">
                    {remaining.map((it) => (
                      <Row key={`q-${it.id}`} tone="queue" label="" it={it} />
                    ))}
                  </div>
                ) : (
                  // Only show "queue empty" when there is truly no next item
                  nextList.length === 0 ? (
                    <div className="text-xs text-gray-500 italic pt-2">Queue empty</div>
                  ) : null
                )}
              </div>
            </section>
          );
        })}
      </div>
    </div>
  );
}

function Row({ it, tone, label }: { it: WorkItem; tone: 'active' | 'upnext' | 'queue'; label: string }) {
  const cls = tone === 'active'
    ? 'bg-[#0a1c0dff] text-[#2e904dff] border-r-2'
    : tone === 'upnext'
    ? 'bg-sky-900 text-sky-300 border-r-2'
    : 'bg-black text-zinc-300';
  return (
    <div className={`flex flex-col gap-0.5 ${cls}`} title={it.desc || ''}>
      {/* Status line (blank for queued) */}
      <div className="px-2 pt-1 text-[10px] tracking-wide h-5 leading-4">{label || ' '}</div>
      {/* ID line */}
      <div className="px-2 pb-1 font-mono text-xs text-gray-400">{it.id}</div>
    </div>
  );
}
```

## File: `components/MetricsBar.test.tsx`
```tsx
import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import MetricsBar from './MetricsBar';
import { appStore } from '@/lib/store';

describe('MetricsBar', () => {
  it('renders metric tiles with formatted values', () => {
    appStore.setState({
      metrics: {
        active_agents: 3,
        total_tokens: 12345,
        total_spend_usd: 12.34,
        live_tps: 56.7,
        live_spend_per_s: 0.12,
        completion_rate: 0.42,
      },
    });

    render(<MetricsBar />);
    expect(screen.getByText('Active Agents')).toBeInTheDocument();
    expect(screen.getByText('3')).toBeInTheDocument();
    expect(screen.getByText('Total Tokens')).toBeInTheDocument();
    expect(screen.getByText('12,345')).toBeInTheDocument();
    expect(screen.getByText('Total Spend')).toBeInTheDocument();
    expect(screen.getByText('$12.34')).toBeInTheDocument();
    expect(screen.getByText('Live TPS')).toBeInTheDocument();
    expect(screen.getByText('56.7')).toBeInTheDocument();
    expect(screen.getByText('Completion')).toBeInTheDocument();
    expect(screen.getByText('42%')).toBeInTheDocument();
  });
});

```

## File: `components/MetricsBar.tsx`
```tsx
"use client";

import React, { useSyncExternalStore } from 'react';
import { appStore } from '@/lib/store';

function useAppMetrics() {
  return useSyncExternalStore(
    appStore.subscribe,
    () => appStore.getState().metrics,
    () => appStore.getState().metrics,
  );
}

function fmtInt(n: number) {
  return new Intl.NumberFormat('en-US', { maximumFractionDigits: 0 }).format(n || 0);
}

function fmtFloat(n: number, frac = 1) {
  const v = Number.isFinite(n) ? n : 0;
  return v.toFixed(frac);
}

function fmtUSD(n: number) {
  const v = Number.isFinite(n) ? n : 0;
  return `$${new Intl.NumberFormat('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 }).format(v)}`;
}

function fmtPct(n: number) {
  const v = Number.isFinite(n) ? n : 0;
  return `${(v * 100).toFixed(0)}%`;
}

export default function MetricsBar() {
  const m = useAppMetrics();

  return (
    <div className="px-4 py-3">
      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3">
        <Metric label="Active Agents" value={fmtInt(m.active_agents)} />
        <Metric label="Total Tokens" value={fmtInt(m.total_tokens)} />
        <Metric label="Total Spend" value={fmtUSD(m.total_spend_usd)} />
        <Metric label="Live TPS" value={fmtFloat(m.live_tps, 1)} />
        <Metric label="Spend / sec" value={fmtUSD(m.live_spend_per_s)} />
        <Metric label="Completion" value={fmtPct(m.completion_rate)} />
      </div>
    </div>
  );
}

function Metric({ label, value }: { label: string; value: string }) {
  return (
    <div className="border border-gray-800 bg-black px-3 py-2">
      <div className="text-xs text-gray-400">{label}</div>
      <div className="text-lg font-semibold text-gray-100">{value}</div>
    </div>
  );
}
```

## File: `components/OperatorGroups.tsx`
```tsx
"use client";

import React, { useMemo, useSyncExternalStore } from 'react';
import { getPlanByName, ALL_PLANS } from '@/plans';
import type { PlanDefinition, WorkGroupDef } from '@/plans/types';
import { appStore } from '@/lib/store';
import { DEFAULT_PLAN_NAME } from '@/plans';

function pickPlan(name: string): PlanDefinition {
  return getPlanByName(name) ?? ALL_PLANS[0];
}

function deriveGroupsFromItems(items: ReturnType<typeof appStore.getState>['items']): WorkGroupDef[] {
  const seen = new Map<string, number>();
  for (const it of Object.values(items)) {
    seen.set(it.group, (seen.get(it.group) || 0) + 1);
  }
  const out: WorkGroupDef[] = [];
  for (const [id, count] of seen) {
    out.push({ id, title: `Group ${id}`, description: `${count} work items.` });
  }
  out.sort((a, b) => a.id.localeCompare(b.id));
  return out;
}

export default function OperatorGroups() {
  // Subscribe to live items so completion updates over time
  const items = useSyncExternalStore(
    appStore.subscribe,
    () => appStore.getState().items,
    () => appStore.getState().items,
  );
  // Subscribe to the applied plan name so Operator Action Items update on Execute
  const planName = useSyncExternalStore(
    appStore.subscribe,
    () => appStore.getState().plan_name || DEFAULT_PLAN_NAME,
    () => appStore.getState().plan_name || DEFAULT_PLAN_NAME,
  );

  const groups = useMemo(() => {
    const plan = pickPlan(planName);
    if (plan.groups && plan.groups.length) return plan.groups;
    return deriveGroupsFromItems(items);
  }, [planName, items]);

  function percentForGroup(groupId: string): number {
    const list = Object.values(items).filter((it) => it.group === groupId);
    if (!list.length) return 0;
    let sumEst = 0;
    let sumElapsed = 0;
    const now = Date.now();
    for (const it of list) {
      const est = Math.max(0, it.estimate_ms || 0);
      if (est <= 0) continue;
      sumEst += est;
      let elapsed = 0;
      if (it.status === 'done') {
        elapsed = est;
      } else if (it.status === 'in_progress') {
        if (typeof it.eta_ms === 'number' && isFinite(it.eta_ms)) {
          elapsed = Math.max(0, Math.min(est, est - it.eta_ms));
        } else if (typeof it.started_at === 'number' && isFinite(it.started_at)) {
          elapsed = Math.max(0, Math.min(est, now - it.started_at));
        }
      }
      sumElapsed += elapsed;
    }
    if (sumEst <= 0) return 0;
    return Math.max(0, Math.min(1, sumElapsed / sumEst));
  }

  return (
    <div className="flex flex-col">
      {groups.map((g) => {
        const pct = percentForGroup(g.id);
        const pctText = `${(pct * 100).toFixed(1)}%`;
        return (
        <div key={g.id}>
          <div
            className="grid gap-0.5 bg-[#0f1d34]"
            style={{ gridTemplateColumns: '64px 1fr', gridTemplateRows: 'auto auto' }}
          >
            {/* Top-left: Group ID */}
            <div className="text-xs p-1 bg-[#021b44ff] text-[#97aed4ff]">{g.id}</div>
            {/* Title to the right of ID */}
            <div className="text-xs p-1 bg-[#021b44ff] text-[#97aed4ff]">{g.title}</div>
            {/* Bottom-left: completion placeholder */}
            <div className="text-xs p-1 bg-[#06142eff]">{pctText}</div>
            {/* Description below the title */}
            <div className="text-xs p-1 bg-[#06142eff]">{g.description}</div>
          </div>
        </div>
        );
      })}
    </div>
  );
}
```

## File: `components/ProjectDescription.tsx`
```tsx
"use client";

import React, { useMemo, useSyncExternalStore } from 'react';
import { getPlanByName, ALL_PLANS, DEFAULT_PLAN_NAME } from '@/plans';
import { appStore } from '@/lib/store';

export default function ProjectDescription() {
  const plan = useSyncExternalStore(
    appStore.subscribe,
    () => appStore.getState().plan_name || DEFAULT_PLAN_NAME,
    () => appStore.getState().plan_name || DEFAULT_PLAN_NAME,
  );

  const desc = useMemo(() => {
    const p = getPlanByName(plan) || ALL_PLANS[0];
    return p.description || 'Agent Traffic Control';
  }, [plan]);

  return <span>{desc}</span>;
}
```

## File: `components/ProjectIdDisplay.tsx`
```tsx
"use client";

import React, { useSyncExternalStore } from 'react';
import { DEFAULT_PLAN_NAME } from '@/plans';
import { appStore } from '@/lib/store';

export default function ProjectIdDisplay() {
  const plan = useSyncExternalStore(
    appStore.subscribe,
    () => appStore.getState().plan_name || DEFAULT_PLAN_NAME,
    () => appStore.getState().plan_name || DEFAULT_PLAN_NAME,
  );
  return <span>{plan}</span>;
}
```

## File: `components/RadarCanvas.tsx`
```tsx
"use client";

import React, { useEffect, useRef } from 'react';
import { RING_COUNT, RADAR_CURVE_AMOUNT, RADAR_MAX_TURNS, RADAR_WOBBLE, RADAR_PULSE_DURATION_MS, RADAR_PULSE_MAX_RADIUS, RADAR_PULSE_WIDTH, RADAR_PULSE_SECONDARY, RADAR_REFRESH_HZ, RADAR_PING_VOLUME, RADAR_PING_AUDIO_PATH } from '@/lib/constants';
import { appStore } from '@/lib/store';
import { createRNG } from '@/lib/rng';

function clampDPR(dpr: number) { return Math.min(2, Math.max(1, dpr || 1)); }

// Story script configuration for typing/deleting animation in the radar message box
type StoryLine = {
  text: string;
  pauseAfterMs?: number;
  // Optional per-line cursor overrides
  cursorChar?: string;
  blinkMs?: number;
};
type CursorConfig = { char: string; blinkMs: number };
type StoryConfig = {
  lines: StoryLine[];
  typingMsPerChar: number;    // speed while typing
  deletingMsPerChar: number;  // speed while deleting
  betweenLinesDelayMs: number; // delay after deleting before next line starts
  startDelayMs?: number;      // initial delay before the story starts
  loop?: boolean;             // loop back to the start after last line
  cursor: CursorConfig;       // default blinking end character
};

// Default story/tutorial script. Tweak text and timings here.
const STORY: StoryConfig = {
  lines: [
    { text: "Initializing agent traffic control..", pauseAfterMs: 3000, cursorChar: '.', blinkMs: 500 },
    { text: "Connecting to ATC radio..", pauseAfterMs: 3200, cursorChar: '.', blinkMs: 300 },
    { text: "Connecting ambient music..", pauseAfterMs: 3200, cursorChar: '.', blinkMs: 600 },
    { text: "Enjoy the vibes of agents working..", pauseAfterMs: 4200, cursorChar: '.', blinkMs: 450 },
    { text: "Play music below; switch between different ATC locations...", pauseAfterMs: 5200, cursorChar: '\\/', blinkMs: 500 },
  ],
  typingMsPerChar: 5,
  deletingMsPerChar: 14,
  betweenLinesDelayMs: 450,
  startDelayMs: 350,
  loop: false,
  cursor: { char: "|", blinkMs: 500 },
};

export default function RadarCanvas() {
  const ref = useRef<HTMLCanvasElement | null>(null);
  // current text to draw in the lower-right message box (updated by story engine)
  const currentTextRef = useRef<string>("");
  // audio element for radar ping
  const pingAudioRef = useRef<HTMLAudioElement | null>(null);
  // Story engine state (kept in refs so we can update from rAF without rerenders)
  const storyCfgRef = useRef<StoryConfig>(STORY);
  const storyLineIdxRef = useRef<number>(0);
  const storyCharIdxRef = useRef<number>(0);
  const storyPhaseRef = useRef<"idle" | "typing" | "pause" | "deleting" | "between">("idle");
  const nextEventAtRef = useRef<number>(0); // timestamp for next char or phase transition
  const lastBlinkAtRef = useRef<number>(0);
  const cursorVisibleRef = useRef<boolean>(true);

  useEffect(() => {
    const canvas = ref.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    // Prepare ping audio element once on mount
    try {
      const a = new Audio(RADAR_PING_AUDIO_PATH);
      a.preload = 'auto';
      a.volume = RADAR_PING_VOLUME;
      // Some browsers require user gesture; we will only play after toggle
      pingAudioRef.current = a;
    } catch {}

    let wCss = 0, hCss = 0, cx = 0, cy = 0, r = 0;
    const isVisibleRef = { current: false } as { current: boolean };

    function resize() {
      if (!canvas || !ctx) return;
      const dpr = clampDPR(window.devicePixelRatio || 1);
      const rect = canvas.getBoundingClientRect();
      wCss = Math.max(200, rect.width);
      hCss = Math.max(200, rect.height);
      // Consider this canvas visible for audio purposes only if it actually has layout space
      isVisibleRef.current = rect.width > 0 && rect.height > 0;
      canvas.width = Math.floor(wCss * dpr);
      canvas.height = Math.floor(hCss * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      drawStatic(wCss, hCss);
      cx = wCss / 2; cy = hCss / 2; r = Math.min(wCss, hCss) * 0.45;
    }

    function drawStatic(w: number, h: number) {
      if (!canvas || !ctx) return;
      ctx.clearRect(0, 0, w, h);
      // Background outside the radar circle: off-black green
      const OUT_BG = '#050c0aff';
      ctx.fillStyle = OUT_BG;
      ctx.fillRect(0, 0, w, h);

      // center + radius
      const cx = w / 2;
      const cy = h / 2;
      const r = Math.min(w, h) * 0.45;

      // Subtle background grid (outside circle): draw across, then cover inside with circle fill
      // Tweak these constants to change dotted appearance
      const GRID_COLOR = 'rgba(60, 120, 90, 0.25)';
      const GRID_STROKE_WIDTH = 1.25; // thickness of the dot/stroke
      const GRID_DOT_LEN = 3;         // length of the drawn segment (dot)
      const GRID_GAP_LEN = 4;         // length of the gap between dots
      ctx.strokeStyle = GRID_COLOR;
      ctx.lineWidth = GRID_STROKE_WIDTH;
      ctx.lineCap = 'round';
      ctx.setLineDash([GRID_DOT_LEN, GRID_GAP_LEN]);
      // Horizontal lines: 4 evenly spaced (skip edges)
      for (let i = 1; i <= 4; i++) {
        const yy = (h * i) / 5;
        ctx.beginPath();
        ctx.moveTo(0, yy);
        ctx.lineTo(w, yy);
        ctx.stroke();
      }
      // Vertical lines: 2 evenly spaced (thirds)
      for (let i = 1; i <= 2; i++) {
        const xx = (w * i) / 3;
        ctx.beginPath();
        ctx.moveTo(xx, 0);
        ctx.lineTo(xx, h);
        ctx.stroke();
      }

      // Reset dashes so rings and crosshair are solid
      ctx.setLineDash([]);
      ctx.lineCap = 'butt';

      // Fill inside the radar circle with pure black to mask grid within
      ctx.beginPath();
      ctx.arc(cx, cy, r, 0, Math.PI * 2);
      ctx.fillStyle = '#000000';
      ctx.fill();

      // Border ticks around the radar (like minute indicators)
      // Controls for width, spacing (count), and height (length)
      const BORDER_TICK_STROKE_WIDTH = 1.5; // line width
      const BORDER_TICK_COUNT = 500;          // spacing: number of ticks around circle
      const BORDER_TICK_LENGTH = Math.max(2.5, r * 0.025); // line height/length
      const BORDER_TICK_OFFSET = 2;          // small outward offset from circle edge
      ctx.strokeStyle = 'rgba(60, 120, 90, 0.25)'; // same as GRID_COLOR
      ctx.lineWidth = BORDER_TICK_STROKE_WIDTH;
      ctx.lineCap = 'butt';
      for (let i = 0; i < BORDER_TICK_COUNT; i++) {
        const a = (i / BORDER_TICK_COUNT) * Math.PI * 2;
        const x0 = cx + Math.cos(a) * (r + BORDER_TICK_OFFSET);
        const y0 = cy + Math.sin(a) * (r + BORDER_TICK_OFFSET);
        const x1 = cx + Math.cos(a) * (r + BORDER_TICK_OFFSET + BORDER_TICK_LENGTH);
        const y1 = cy + Math.sin(a) * (r + BORDER_TICK_OFFSET + BORDER_TICK_LENGTH);
        ctx.beginPath();
        ctx.moveTo(x0, y0);
        ctx.lineTo(x1, y1);
        ctx.stroke();
      }

      // rings
      ctx.strokeStyle = 'rgba(255,255,255,0.08)';
      ctx.lineWidth = 1;
      for (let i = 1; i <= RING_COUNT; i++) {
        const rr = (r * i) / RING_COUNT;
        ctx.beginPath();
        ctx.arc(cx, cy, rr, 0, Math.PI * 2);
        ctx.stroke();
      }

      // tick marks (simple cross)
      ctx.strokeStyle = 'rgba(255,255,255,0.12)';
      ctx.beginPath();
      ctx.moveTo(cx - r, cy); ctx.lineTo(cx + r, cy);
      ctx.moveTo(cx, cy - r); ctx.lineTo(cx, cy + r);
      ctx.stroke();

      // center checkbox glyph
      const box = Math.max(10, r * 0.06);
      ctx.strokeStyle = 'rgba(255,255,255,0.4)';
      ctx.lineWidth = 1.5;
      ctx.strokeRect(cx - box / 2, cy - box / 2, box, box);

      // Lower-right message box (dynamic story text)
      const baseText = (currentTextRef.current || '');
      const effectiveLine = storyCfgRef.current.lines[(storyLineIdxRef.current || 0) % Math.max(1, storyCfgRef.current.lines.length)] || { text: '' };
      const effCursorChar = (effectiveLine.cursorChar ?? storyCfgRef.current.cursor.char) || '';
      const isPause = storyPhaseRef.current === 'pause';
      const textToDraw = baseText.trim().length > 0 ? baseText : '—';
      const measureText = isPause ? textToDraw + effCursorChar : textToDraw;
      const padX = 8, padY = 6;
      const margin = 10;
      const isMobile = (typeof window !== 'undefined' && window.innerWidth <= 640);
      const fontSize = isMobile ? 10 : 12;
      ctx.font = `${fontSize}px ui-monospace, SFMono-Regular, Menlo, monospace`;
      const metrics = ctx.measureText(measureText);
      const maxTextWidth = isMobile ? w - margin * 2 - padX * 2 : Math.max(60, w * 0.5);
      const tw = Math.min(Math.max(metrics.width, 60), maxTextWidth);
      const th = fontSize + 6;
      const boxW = tw + padX * 2;
      const boxH = th + padY * 2;
      const bx = w - boxW - margin;
      const by = h - boxH - margin;
      // box background
      ctx.fillStyle = 'rgba(0, 0, 0, 0.6)';
      ctx.fillRect(bx, by, boxW, boxH);
      // border
      ctx.strokeStyle = 'rgba(255,255,255,0.2)';
      ctx.lineWidth = 1;
      ctx.strokeRect(bx, by, boxW, boxH);
      // text + non-shifting cursor draw
      ctx.fillStyle = '#fff';
      const tx = bx + padX;
      const ty = by + padY + fontSize;
      // draw base text
      ctx.textAlign = 'start';
      ctx.fillText(textToDraw, tx, ty);
      // draw cursor char in-place (invisible when blink-off) so width doesn't shift
      if (isPause && effCursorChar) {
        const baseW = ctx.measureText(textToDraw).width;
        const prevAlpha = ctx.globalAlpha;
        ctx.globalAlpha = cursorVisibleRef.current ? 1 : 0;
        ctx.fillText(effCursorChar, tx + baseW, ty);
        ctx.globalAlpha = prevAlpha;
      }
    }

    // Track previous status per item to detect transitions to 'done'
    const prevItemStatus = new Map<string, string>();
    
    resize();
    // Initialize previous statuses to avoid pulsing existing done items on mount
    {
      const init = appStore.getState();
      for (const it of Object.values(init.items)) prevItemStatus.set(it.id, it.status);
    }
    let obs: ResizeObserver | null = null;
    if (typeof ResizeObserver !== 'undefined') {
      obs = new ResizeObserver(resize);
      obs.observe(canvas);
    } else {
      window.addEventListener('resize', resize);
    }
    // Simple animation loop to draw in-progress agents (throttled to RADAR_REFRESH_HZ)
    let rafId: number | null = null;
    const intervalMs = Math.max(1, Math.floor(1000 / Math.max(1, RADAR_REFRESH_HZ)));
    let lastDrawAt = 0;
    function angleForAgent(agentId: string) {
      // Base starting angle, deterministic per agent
      const rng = createRNG(agentId + ':angle');
      return rng.next() * Math.PI * 2;
    }

    // Smooth easing for spiral growth
    function easeInOutSine(t: number) {
      return 0.5 - 0.5 * Math.cos(Math.PI * Math.max(0, Math.min(1, t)));
    }

    // Compute a curved angle offset for an agent at progress t in [0,1]
    function curvedAngleOffset(agentId: string, t: number) {
      const k = Math.max(0, Math.min(1, RADAR_CURVE_AMOUNT));
      if (k <= 0) return 0;
      const rng = createRNG(agentId + ':curve');
      const spiralDir = rng.bool() ? 1 : -1; // clockwise vs counter-clockwise
      // Random wobble frequencies and phases (few direction changes only)
      const f1 = rng.float(0.6, 1.6); // cycles over [0..1]
      const f2 = rng.float(1.2, 2.4);
      const p1 = rng.float(0, Math.PI * 2);
      const p2 = rng.float(0, Math.PI * 2);
      const maxSpin = (RADAR_MAX_TURNS * 2 * Math.PI) || (0.5 * 2 * Math.PI);
      const e = easeInOutSine(t);
      // Allocate some of the curve budget to monotone spiral, some to wobble
      const wobblePortion = Math.max(0, Math.min(1, RADAR_WOBBLE));
      const spiralPortion = 1 - wobblePortion;
      const spiral = spiralDir * (k * spiralPortion) * maxSpin * e;
      const wobbleAmp = (k * wobblePortion) * maxSpin * 0.6; // keep wobble within 60% of budget
      // Wobble can change directions; envelope keeps it smooth
      const wobble = wobbleAmp * (
        Math.sin(2 * Math.PI * f1 * t + p1) * 0.7 +
        Math.sin(2 * Math.PI * f2 * t + p2) * 0.3
      ) * (0.85 + 0.15 * e);
      let s = spiral + wobble;
      // Never exceed the half-rotation cap
      if (s > maxSpin) s = maxSpin;
      if (s < -maxSpin) s = -maxSpin;
      return s;
    }

    // Position on curved path at progress t in [0,1]
    function pathPoint(agentId: string, t: number) {
      const theta0 = angleForAgent(agentId);
      const theta = theta0 + curvedAngleOffset(agentId, t);
      const rad = r * (1 - t);
      const x = cx + Math.cos(theta) * rad;
      const y = cy + Math.sin(theta) * rad;
      return { x, y, theta, rad };
    }
    // Per-agent trailing stroke segments emitted at the agent's position.
    type TrailSeg = { x: number; y: number; dir: number; created: number };
    const trails = new Map<string, { segs: TrailSeg[]; lastEmit: number; lastX: number; lastY: number }>();
    // Tuning knobs for the trailing stroke style
    const TRAIL_STROKE_LEN = 3;   // pixels: length of each stroke
    const TRAIL_STROKE_WIDTH = 2;  // pixels: width of each stroke
    const TRAIL_GAP_PX = 8;        // pixels: minimum distance moved before emitting next stroke
    
    const MAX_SEGS = 60;           // cap per-agent segments
    const LIFESPAN_MS = 2000;      // ms before a stroke fades out fully

    // Center pulses when agents complete
    type Pulse = { created: number };
    const pulses: Pulse[] = [];
    // Track items we've already emitted a pulse for (by item id)
    const pulsedItems = new Set<string>();
    // Track items that have already produced a sound effect to avoid double audio
    const soundedItems = new Set<string>();
    // Centralized pulse emitter that also plays audio if enabled
    function emitPulse(created: number, itemId?: string, playSound: boolean = true) {
      pulses.push({ created });
      // If radar ping sound is enabled, play the short ping only once per itemId
      try {
        const enable = appStore.getState().pingAudioEnabled;
        if (playSound && enable && pingAudioRef.current && isVisibleRef.current) {
          if (!itemId) {
            // No item id context; play normally
            try { pingAudioRef.current.currentTime = 0; } catch {}
            void pingAudioRef.current.play().catch(() => {});
          } else if (!soundedItems.has(itemId)) {
            soundedItems.add(itemId);
            try { pingAudioRef.current.currentTime = 0; } catch {}
            void pingAudioRef.current.play().catch(() => {});
          }
        }
      } catch {}
    }
    function drawAgents() {
      // Throttle by desired refresh rate
      const nowPerf = performance.now();
      if (nowPerf - lastDrawAt < intervalMs) {
        rafId = window.requestAnimationFrame(drawAgents);
        return;
      }
      lastDrawAt = nowPerf;
      // Guard against missing context (TS + runtime safety)
      if (!canvas || !ctx) return;

      // STORY ENGINE: update message text and cursor by time
      const now = Date.now();
      const cfg = storyCfgRef.current;
      const lines = cfg.lines;
      if (lines.length > 0) {
        if (storyPhaseRef.current === 'idle') {
          // Initialize on first run
          storyLineIdxRef.current = 0;
          storyCharIdxRef.current = 0;
          storyPhaseRef.current = 'typing';
          nextEventAtRef.current = now + (cfg.startDelayMs || 0);
          lastBlinkAtRef.current = now;
          cursorVisibleRef.current = true;
        }
        // Blink management (only visible when paused at end of a line)
        const effBlinkMs = Math.max(
          100,
          (lines[storyLineIdxRef.current]?.blinkMs ?? cfg.cursor.blinkMs)
        );
        if (now - lastBlinkAtRef.current >= effBlinkMs) {
          cursorVisibleRef.current = !cursorVisibleRef.current;
          lastBlinkAtRef.current = now;
        }
        const line = lines[storyLineIdxRef.current];
        const full = line.text;
        // Step the phase machine based on time
        if (now >= nextEventAtRef.current) {
          switch (storyPhaseRef.current) {
            case 'typing': {
              if (storyCharIdxRef.current < full.length) {
                storyCharIdxRef.current += 1;
                nextEventAtRef.current = now + Math.max(1, cfg.typingMsPerChar);
              }
              if (storyCharIdxRef.current >= full.length) {
                storyCharIdxRef.current = full.length;
                storyPhaseRef.current = 'pause';
                const pause = typeof line.pauseAfterMs === 'number' ? line.pauseAfterMs : 1000;
                nextEventAtRef.current = now + Math.max(0, pause);
              }
              break;
            }
            case 'pause': {
              // end of pause: begin deleting (if looping) or stay blinking at end
              if (cfg.loop) {
                storyPhaseRef.current = 'deleting';
                nextEventAtRef.current = now + Math.max(1, cfg.deletingMsPerChar);
              } else {
                // Hold final line with blink; schedule next check
                nextEventAtRef.current = now + 200; // keep engine alive for blink
              }
              break;
            }
            case 'deleting': {
              if (storyCharIdxRef.current > 0) {
                storyCharIdxRef.current -= 1;
                nextEventAtRef.current = now + Math.max(1, cfg.deletingMsPerChar);
              }
              if (storyCharIdxRef.current <= 0) {
                storyCharIdxRef.current = 0;
                storyPhaseRef.current = 'between';
                nextEventAtRef.current = now + Math.max(0, cfg.betweenLinesDelayMs);
              }
              break;
            }
            case 'between': {
              // advance to next line
              storyLineIdxRef.current = (storyLineIdxRef.current + 1) % lines.length;
              storyPhaseRef.current = 'typing';
              nextEventAtRef.current = now + Math.max(1, cfg.typingMsPerChar);
              break;
            }
            default:
              break;
          }
        }
        // Build the current display base string (cursor drawn separately to avoid shifting)
        const base = full.slice(0, Math.max(0, Math.min(full.length, storyCharIdxRef.current)));
        currentTextRef.current = base;
      }
      // Redraw static each frame (simple MVP approach)
      drawStatic(wCss, hCss);
      const state = appStore.getState();
      // 'now' already declared above for story engine
      const c = ctx as CanvasRenderingContext2D;

      // Arrow styling knobs
      const ARROW_CORNER_RADIUS = 1;    // rounded corners on arrow polygon
      const ARROW_SIZE = 1.25;           // overall arrow scale (length & width)
      const ARROW_NOTCH_RATIO = -0.25;   // how deep the rear notch is, relative to length
      // Pull arrow color from global CSS variable --green-bright (fallback to #57ff7a)
      function cssVar(name: string, fallback: string): string {
        try {
          const v = getComputedStyle(document.documentElement).getPropertyValue(name).trim();
          return v || fallback;
        } catch {
          return fallback;
        }
      }
      const ARROW_COLOR_HEX = cssVar('--green-bright', '#57ff7a');
      // Label styling knobs
      const LABEL_OFFSET_Y = 25;        // pixels below arrow in screen space
      const LABEL_PAD_X = 4;
      const LABEL_PAD_Y = 2;
      const LABEL_FONT = '10px ui-monospace, SFMono-Regular, Menlo, monospace';

      function fillRoundedPolygon(p: Array<{x:number;y:number}>, r: number) {
        if (p.length === 0) return;
        c.beginPath();
        c.moveTo(p[0].x, p[0].y);
        for (let i = 0; i < p.length; i++) {
          const p1 = p[(i + 1) % p.length];
          const p2 = p[(i + 2) % p.length];
          c.arcTo(p1.x, p1.y, p2.x, p2.y, r);
        }
        c.closePath();
        c.fill();
      }

      function fmtElapsed(ms: number) {
        const total = Math.max(0, Math.round(ms / 1000));
        const m = Math.floor(total / 60);
        const s = total % 60;
        const mm = m.toString().padStart(2, '0');
        const ss = s.toString().padStart(2, '0');
        return `${mm}:${ss}`;
      }

      function drawLabel(x: number, y: number, idLine: string, timeLine: string, colorTop: string) {
        const rx = x; // anchor right edge at the arrow x
        const ty = y + LABEL_OFFSET_Y;
        c.font = LABEL_FONT;
        const m1 = c.measureText(idLine);
        const m2 = c.measureText(timeLine);
        const tw = Math.ceil(Math.max(m1.width, m2.width));
        const th = 12; // approx line height for 10px font
        const lineGap = 2;
        const totalH = th * 2 + lineGap;
        const bw = tw + LABEL_PAD_X * 2;
        const bh = totalH + LABEL_PAD_Y * 2;
        const bx = rx - bw; // align right edge to rx
        const by = ty - bh / 2;
        // background (no border)
        c.fillStyle = 'rgba(0,0,0,0.6)';
        c.fillRect(bx, by, bw, bh);
        // text lines (right-justified)
        c.textAlign = 'right';
        c.fillStyle = colorTop; // top line (agent id)
        c.fillText(idLine, bx + bw - LABEL_PAD_X, by + LABEL_PAD_Y + th - 3);
        c.fillStyle = 'rgba(220,220,220,0.95)'; // bottom line (duration)
        c.fillText(timeLine, bx + bw - LABEL_PAD_X, by + LABEL_PAD_Y + th - 3 + th + lineGap);
        c.textAlign = 'start';
      }

      // Detect newly completed items (status transition to 'done') and pulse once
      for (const it of Object.values(state.items)) {
        const prev = prevItemStatus.get(it.id);
        if (prev !== 'done' && it.status === 'done' && !pulsedItems.has(it.id)) {
          // Visual pulse for 'done', but do not play sound here
          emitPulse(now, it.id, false);
          pulsedItems.add(it.id);
        }
        prevItemStatus.set(it.id, it.status);
      }

      // Draw and update trailing strokes before drawing arrows so arrows sit on top
      for (const [agentId, trail] of trails) {
        // purge expired
        trail.segs = trail.segs.filter(s => now - s.created <= LIFESPAN_MS);
        c.save();
        c.lineCap = 'round';
        c.lineWidth = TRAIL_STROKE_WIDTH;
        for (const s of trail.segs) {
          const age = now - s.created;
          const t = Math.max(0, Math.min(1, age / LIFESPAN_MS));
          const alpha = (1 - t) * 1.0; // start fully opaque, fade to 0
          const dx = Math.cos(s.dir) * TRAIL_STROKE_LEN;
          const dy = Math.sin(s.dir) * TRAIL_STROKE_LEN;
          c.beginPath();
          // draw segment behind the movement direction
          c.moveTo(s.x - dx, s.y - dy);
          c.lineTo(s.x, s.y);
          c.strokeStyle = ARROW_COLOR_HEX;
          c.globalAlpha = alpha;
          c.stroke();
        }
        if (trail.segs.length === 0) trails.delete(agentId);
        c.restore();
      }
      for (const agent of Object.values(state.agents)) {
        const item = state.items[agent.work_item_id];
        if (!item || item.status !== 'in_progress') continue;
        const est = Math.max(1, item.estimate_ms || 0);
        let t = 0;
        if (typeof item.eta_ms === 'number' && isFinite(item.eta_ms)) {
          t = 1 - Math.max(0, Math.min(1, item.eta_ms / est));
        } else if (typeof item.started_at === 'number') {
          const elapsed = Date.now() - item.started_at;
          t = Math.max(0, Math.min(1, elapsed / est));
        }
        // Position along the curved path
        const { x, y } = pathPoint(agent.id, t);
        // Heading tangent to the path using a small finite difference
        const eps = 0.002;
        const t0 = Math.max(0, Math.min(1, t - eps));
        const t1 = Math.max(0, Math.min(1, t + eps));
        const p0 = pathPoint(agent.id, t0);
        const p1 = pathPoint(agent.id, t1);
        let dir = Math.atan2(p1.y - p0.y, p1.x - p0.x);
        if (!isFinite(dir)) {
          // Fallback towards center if derivative is degenerate
          dir = Math.atan2(cy - y, cx - x);
        }
        const len = ARROW_SIZE * Math.max(8, Math.min(14, r * 0.05));
        const width = ARROW_SIZE * 1.25 * Math.max(5, Math.min(9, r * 0.03));

        // Emit a trailing stroke segment at the current position with agent heading
        let trail = trails.get(agent.id);
        if (!trail) { trail = { segs: [], lastEmit: 0, lastX: x, lastY: y }; trails.set(agent.id, trail); }
        // Ensure a first segment exists to make trails immediately visible
        if (trail.segs.length === 0) {
          trail.segs.push({ x, y, dir, created: now });
          trail.lastEmit = now;
          trail.lastX = x; trail.lastY = y;
        }
        const movedDx = x - trail.lastX; const movedDy = y - trail.lastY;
        const moved = Math.hypot(movedDx, movedDy);
        if (moved >= TRAIL_GAP_PX) {
          // Emit as many evenly spaced segments as needed to cover the distance
          const ux = movedDx / moved;
          const uy = movedDy / moved;
          const count = Math.min(20, Math.floor(moved / TRAIL_GAP_PX));
          for (let i = 1; i <= count; i++) {
            const sx = trail.lastX + ux * TRAIL_GAP_PX * i;
            const sy = trail.lastY + uy * TRAIL_GAP_PX * i;
            trail.segs.push({ x: sx, y: sy, dir, created: now });
          }
          // Advance last anchor by the distance we filled
          const adv = TRAIL_GAP_PX * count;
          trail.lastX = trail.lastX + ux * adv;
          trail.lastY = trail.lastY + uy * adv;
          trail.lastEmit = now;
          if (trail.segs.length > MAX_SEGS) trail.segs.splice(0, trail.segs.length - MAX_SEGS);
        }
        c.save();
        c.translate(x, y);
        c.rotate(dir);
        c.fillStyle = ARROW_COLOR_HEX;
        c.globalAlpha = 0.9;
        // Arrow polygon with rear notch to suggest wings
        const notch = len * ARROW_NOTCH_RATIO;
        const wing = width * 0.6;
        const pts = [
          { x: len, y: 0 },                // nose
          { x: -len * 0.45, y: wing },     // lower wing
          { x: -(len * 0.45 + notch), y: 0 }, // rear notch inward
          { x: -len * 0.45, y: -wing },    // upper wing
        ];
        fillRoundedPolygon(pts, ARROW_CORNER_RADIUS);
        c.restore();

        // Emit a center pulse once when this item effectively arrives near the center
        if (!pulsedItems.has(item.id)) {
          const nearT = t >= 0.985; // slightly looser than 0.995 to avoid frame-miss
          const dx = x - cx, dy = y - cy;
          const nearR = Math.hypot(dx, dy) <= Math.max(2, r * 0.01); // pixel/radius guard
          if (nearT || nearR) {
            // Arrival pulse at center: emit with sound
            emitPulse(now, item.id, true);
            pulsedItems.add(item.id);
          }
        }

        // Label with agent id and elapsed time below arrow (screen space)
        const elapsedMs = Math.round(t * est);
        drawLabel(x, y, agent.id, fmtElapsed(elapsedMs), ARROW_COLOR_HEX);
      }

      // Draw center pulses on top
      if (pulses.length) {
        const maxR = r * Math.max(0, Math.min(1, RADAR_PULSE_MAX_RADIUS));
        const secMul = Math.max(0, Math.min(2, RADAR_PULSE_SECONDARY));
        c.save();
        c.translate(cx, cy);
        const remain: Pulse[] = [];
        for (const p of pulses) {
          const age = now - p.created;
          const dur = Math.max(1, RADAR_PULSE_DURATION_MS);
          const u = Math.max(0, Math.min(1, age / dur));
          const radius = Math.max(0.5, u * maxR);
          const alpha = 1.0 - u; // simple fade out
          c.strokeStyle = ARROW_COLOR_HEX;
          c.globalAlpha = alpha * 0.9;
          c.lineWidth = RADAR_PULSE_WIDTH;
          c.beginPath();
          c.arc(0, 0, radius, 0, Math.PI * 2);
          c.stroke();
          if (secMul > 0) {
            c.globalAlpha = Math.max(0, alpha * 0.6);
            c.beginPath();
            c.arc(0, 0, Math.max(0.5, (u * secMul) * maxR), 0, Math.PI * 2);
            c.stroke();
          }
          if (age < dur) remain.push(p);
        }
        c.restore();
        // retain non-finished pulses
        pulses.length = 0;
        pulses.push(...remain);
      }
      rafId = window.requestAnimationFrame(drawAgents);
    }
    rafId = window.requestAnimationFrame(drawAgents);

    return () => {
      if (obs) obs.disconnect();
      else window.removeEventListener('resize', resize);
      if (rafId) cancelAnimationFrame(rafId);
    };
  }, []);

  return (
    <div className="h-full min-h-0 flex flex-col">
      <div className="flex-1 min-h-0 border border-gray-800 bg-black">
        <canvas ref={ref} style={{ width: '100%', height: '100%', display: 'block' }} />
      </div>
    </div>
  );
}
```

## File: `components/TickIndicator.tsx`
```tsx
"use client";

import { useEffect, useRef, useState } from 'react';
import { createSimBridge, type SimBridge } from '@/lib/simBridge';
import { attachBridgeToStore } from '@/lib/bridgeToStore';
import { appStore } from '@/lib/store';
import { debugLog } from '@/lib/debug';
import { isConnected, setExternalBridge } from '@/lib/simClient';

export default function TickIndicator() {
  const [tick, setTick] = useState(0);
  const [running, setRunning] = useState(false);
  const [wired, setWired] = useState(false);
  const bridgeRef = useRef<SimBridge | null>(null);

  useEffect(() => {
    // If a connection already exists, just subscribe
    if (isConnected()) {
      const unsub = appStore.subscribe((state) => {
        setTick(state.lastTickId ?? 0);
        setRunning(!!state.running);
        debugLog('ui', 'state-update', { tick: state.lastTickId, running: state.running });
      });
      setWired(true);
      return () => unsub?.();
    }

    // Spin up worker and wire bridge on mount (only in browser)
    if (typeof window === 'undefined' || typeof Worker === 'undefined') {
      return; // SSR or non-browser test environment
    }
    let worker: Worker | null = null;
    try {
      worker = new Worker(new URL('../workers/engine.ts', import.meta.url), { type: 'module' });
      debugLog('ui', 'worker-created');
      worker.addEventListener('error', (e: ErrorEvent) => {
        debugLog('ui', 'worker-error', { message: e?.message, filename: e?.filename, lineno: e?.lineno, colno: e?.colno });
      });
      worker.addEventListener('message', (e: MessageEvent) => {
        debugLog('ui', 'worker-native-message', e?.data);
      });
    } catch (e) {
      // Worker not available (tests or older env); bail out
      debugLog('ui', 'worker-create-failed', e);
      return;
    }
    const bridge = createSimBridge(worker);
    debugLog('ui', 'bridge-created');
    bridgeRef!.current = bridge;
    const link = attachBridgeToStore(bridge, appStore);
    setExternalBridge(bridge, worker, link);

    // subscribe to lastTickId
    const unsub = appStore.subscribe((state) => {
      setTick(state.lastTickId ?? 0);
      setRunning(!!state.running);
      debugLog('ui', 'state-update', { tick: state.lastTickId, running: state.running });
    });
    setWired(true);
    // Proactively request a snapshot (handshake)
    bridge.postIntent({ type: 'request_snapshot' });

    return () => {
      unsub?.();
      link.destroy();
      bridge.destroy?.();
      worker?.terminate();
    };
  }, []);

  return (
    <div className="p-4">
      <div className="inline-flex items-center gap-3 bg-black border border-gray-700 px-3 py-2">
        <span className="text-sm text-gray-300">Engine</span>
        <span className="text-xs bg-gray-700 px-2 py-1 text-gray-200">{wired ? 'connected' : 'connecting...'}</span>
        <span className="text-sm font-mono">Tick: {tick}</span>
        <button
          onClick={() => {
            const next = !running;
            // Optimistically reflect new state; worker snapshot will reconcile
            setRunning(next);
            bridgeRef.current?.postIntent({ type: 'set_running', running: next });
            // Nudge a snapshot to ensure fast UI sync if batching delays it
            bridgeRef.current?.postIntent({ type: 'request_snapshot' });
          }}
          className={`text-xs px-2 py-1 border ${running ? 'bg-green-700/30 border-green-600 text-green-200' : 'bg-red-700/30 border-red-600 text-red-200'}`}
        >
          {running ? 'Pause' : 'Run'}
        </button>
      </div>
    </div>
  );
}
```

## File: `components/TimelineStatusBar.tsx`
```tsx
"use client";

import React, { useEffect, useMemo, useState, useSyncExternalStore } from 'react';
import { appStore } from '@/lib/store';
import type { UIState } from '@/lib/store';
import type { WorkItem } from '@/lib/types';

function useAppSelector<T>(selector: (s: UIState) => T): T {
  return useSyncExternalStore(
    appStore.subscribe,
    () => selector(appStore.getState()),
    () => selector(appStore.getState())
  );
}

function fmtHMS(ms: number) {
  if (!Number.isFinite(ms) || ms < 0) return '0:00';
  const totalSec = Math.floor(ms / 1000);
  const h = Math.floor(totalSec / 3600);
  const m = Math.floor((totalSec % 3600) / 60);
  const s = totalSec % 60;
  const mm = m.toString();
  const ss = s.toString().padStart(2, '0');
  if (h > 0) return `${h}:${mm.padStart(2, '0')}:${ss}`;
  return `${mm}:${ss}`;
}

export default function TimelineStatusBar() {
  const items = useAppSelector((s) => s.items);

  // Compute totals and progress across items, plus earliest start and completion
  const { totalEstimateMs, progressMs, hasAnyStarted, earliestStart, projectComplete } = useMemo(() => {
    let total = 0;
    let progressed = 0;
    let anyStarted = false;
    let earliest: number | undefined = undefined;
    let allDone = true;
    const now = Date.now();
    const arr = Object.values(items) as WorkItem[];
    if (arr.length === 0) allDone = false; // empty project is not complete
    for (const it of arr) {
      const est = Math.max(0, it.estimate_ms || 0);
      total += est;
      if (typeof it.started_at === 'number' && isFinite(it.started_at)) {
        if (earliest === undefined || it.started_at < earliest) earliest = it.started_at;
      }
      if (it.status !== 'queued' || (typeof it.started_at === 'number' && isFinite(it.started_at))) anyStarted = true;
      if (it.status !== 'done') allDone = false;
      if (est <= 0) continue;
      if (it.status === 'done') {
        progressed += est;
      } else if (it.status === 'in_progress') {
        if (typeof it.eta_ms === 'number' && isFinite(it.eta_ms)) {
          const elapsed = Math.max(0, Math.min(est, est - it.eta_ms));
          progressed += elapsed;
        } else if (typeof it.started_at === 'number' && isFinite(it.started_at)) {
          const elapsed = Math.max(0, Math.min(est, now - it.started_at));
          progressed += elapsed;
        }
      }
    }
    return { totalEstimateMs: total, progressMs: progressed, hasAnyStarted: anyStarted, earliestStart: earliest, projectComplete: allDone };
  }, [items]);

  const [now, setNow] = useState<number>(() => Date.now());
  const [stoppedAt, setStoppedAt] = useState<number | undefined>(undefined);

  // Determine if any items are currently in progress (agents active)
  // const anyInProgress = useMemo(() => {
  //   for (const it of Object.values(items) as WorkItem[]) {
  //     if (it.status === 'in_progress') return true;
  //   }
  //   return false;
  // }, [items]);

  const hasStarted = hasAnyStarted;
  const isComplete = !!projectComplete;

  // Tick while started and not complete; freeze when complete
  useEffect(() => {
    let id: number | undefined;
    if (hasStarted && !isComplete) {
      setStoppedAt(undefined);
      // Faster tick for smoother progress updates
      id = window.setInterval(() => setNow(Date.now()), 100);
    } else if (isComplete) {
      // capture the moment we detected completion (freeze timer)
      setStoppedAt((prev) => prev ?? Date.now());
    }
    return () => {
      if (id) clearInterval(id);
    };
  }, [hasStarted, isComplete]);

  const denom = totalEstimateMs > 0 ? totalEstimateMs : 1;
  // Progress bar uses aggregate item progress (responds to engine speed)
  const progressed = hasStarted ? Math.max(0, Math.min(denom, progressMs)) : 0;
  const baseProgress = Math.max(0, Math.min(1, progressed / denom));
  const progress = isComplete ? 1 : baseProgress;
  // Timer uses wall-clock since first start, freezes on completion
  const effectiveNow = !isComplete ? now : (stoppedAt ?? now);
  const timerMs = hasStarted && typeof earliestStart === 'number' ? Math.max(0, effectiveNow - earliestStart) : 0;
  const statusLabel = !hasStarted ? 'INITIALIZING' : isComplete ? 'COMPLETE' : 'RUNNING';

  return (
    <div className="w-full bg-black">
      <div className="flex items-center gap-4 px-3 py-2">
        <div className="flex items-center gap-3 min-w-[180px]">
          <LiveBadge />
          <span
            className={`text-xs font-semibold ${statusLabel === 'INITIALIZING' ? 'text-yellow-300' : 'text-[var(--row-done-fg)]'}`}
          >
            {statusLabel}
          </span>
          {hasStarted && (
            <span className="font-mono text-xs text-[var(--row-done-fg)]">{fmtHMS(timerMs)}</span>
          )}
        </div>
        <div className="flex-1">
          <ProgressBar pct={progress} />
        </div>
      </div>
    </div>
  );
}

function ProgressBar({ pct }: { pct: number }) {
  const pc = Math.max(0, Math.min(1, pct));
  const percent = pc * 100;
  return (
    <div className="relative h-3 w-full bg-[#0b0b0b] border border-[#1f2910]">
      {/* filled portion */}
      <div
        className="h-full bg-green-600"
        style={{ width: `${percent}%`, transition: 'width 0.3s linear' }}
      />
      {/* notch at current progress */}
      <div
        className="absolute top-0 h-full border-r-2 border-white/70"
        style={{ left: `calc(${percent}% - 1px)`, transition: 'left 0.3s linear' }}
      />
    </div>
  );
}

function LiveBadge() {
  return (
    <div className="flex items-center gap-2 border border-gray-600/60 rounded px-2 py-0.5 select-none">
      
      <span className="relative flex h-3 w-3 items-center justify-center">
        <span className="absolute inset-0 inline-flex rounded-full bg-red-500 opacity-75 animate-ping"></span>
        <span className="relative inline-flex h-2 w-2 rounded-full bg-red-500 shadow-[0_0_8px_rgba(239,68,68,0.9)]"></span>
      </span>
      <span className="text-[10px] leading-none font-bold tracking-widest text-gray-300">LIVE</span>
    </div>
  );
}
```

## File: `components/TopOverview.tsx`
```tsx
"use client";

import React, { useEffect, useRef, useState, useSyncExternalStore } from 'react';
import { appStore } from '@/lib/store';

function useMetrics() {
  return useSyncExternalStore(
    appStore.subscribe,
    () => appStore.getState().metrics,
    () => appStore.getState().metrics,
  );
}

function fmtInt(n?: number) {
  const v = Number.isFinite(n as number) ? (n as number) : 0;
  return new Intl.NumberFormat('en-US', { maximumFractionDigits: 0 }).format(v);
}
function fmtUSD(n?: number) {
  const v = Number.isFinite(n as number) ? (n as number) : 0;
  return `$${new Intl.NumberFormat('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 }).format(v)}`;
}

export default function TopOverview({ compact = false, hideCompletion = false }: { compact?: boolean; hideCompletion?: boolean }) {
  const m = useMetrics();

  // Completion over time graph state
  const containerRef = useRef<HTMLDivElement | null>(null);
  const [points, setPoints] = useState<Array<{ t: number; v: number }>>([]);
  const startRef = useRef<number>(Date.now());
  const wasCompleteRef = useRef<boolean>(false);

  // Collect points over time; start at 0%
  useEffect(() => {
    // ensure first point at t=0 is 0
    setPoints([{ t: 0, v: 0 }]);
    const id = window.setInterval(() => {
      const state = appStore.getState();
      const arr = Object.values(state.items || {});
      const hasItems = arr.length > 0;
      const allDone = hasItems && arr.every((it) => it.status === 'done');

      const vRaw = state.metrics?.completion_rate || 0;
      const v = Math.max(0, Math.min(1, vRaw));

      // Detect transition: complete -> not complete (new run). Reset series.
      if (wasCompleteRef.current && !allDone) {
        wasCompleteRef.current = false;
        startRef.current = Date.now();
        setPoints([{ t: 0, v: 0 }]);
        return;
      }

      // While complete, freeze series (do not append new points)
      if (allDone) {
        wasCompleteRef.current = true;
        return;
      }

      // If not running, do not advance time/series
      if (!state.running) {
        return;
      }

      // Not complete: append point using current baseline
      const t = (Date.now() - startRef.current) / 1000;
      setPoints((prev) => {
        const next = prev.concat({ t, v });
        // keep last ~600 points to cap memory
        return next.length > 600 ? next.slice(next.length - 600) : next;
      });
    }, 400);
    return () => clearInterval(id);
  }, []);

  // Reset the series when a fresh snapshot is applied (e.g., switching plans)
  useEffect(() => {
    let prevLast = appStore.getState().lastTickId;
    const unsub = appStore.subscribe((s) => {
      const currentLast = s.lastTickId;
      if (prevLast > 0 && currentLast === 0) {
        wasCompleteRef.current = false;
        startRef.current = Date.now();
        setPoints([{ t: 0, v: 0 }]);
      }
      prevLast = currentLast;
    });
    return () => {
      if (typeof unsub === 'function') unsub();
    };
  }, []);

  const gridCols = compact ? '1fr' : '1fr 1fr 1fr';
  const gapPx = compact ? 6 : 8;
  const headerCls = compact
    ? 'text-sm text-[#d79326ff] pl-2 pr-2 bg-[#130f04ff]'
    : 'text-lg text-[#d79326ff] pl-2 pr-2 bg-[#130f04ff]';
  const labelCls = compact ? 'text-xs' : 'text-md';
  const valueCls = compact ? 'text-base' : 'text-xl';

  return (
    <div
      style={{
        display: 'grid',
        gridTemplateColumns: gridCols,
        gap: `${gapPx}px`,
        height: '100%',
        minHeight: 0,
      }}
    >
      {/* Main Metrics card */}
      <div style={{ background: '#000' }}>
        <div className={headerCls}>MAIN METRICS</div>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: gapPx, color: '#cfcfcf', padding: '8px' }}>
          <div style={{ display: 'flex', flexDirection: 'column' }}>
            <div className={labelCls} style={{ color: '#a0a0a0'}}>ACTIVE AGENTS</div>
            <div className={valueCls} style={{ marginTop: 4 }}>{fmtInt(m.active_agents)}</div>
          </div>
          <div style={{ display: 'flex', flexDirection: 'column' }}>
            <div className={labelCls} style={{ color: '#a0a0a0'}}>TOTAL TOKENS</div>
            <div className={valueCls} style={{ marginTop: 4 }}>{fmtInt(m.total_tokens)}</div>
          </div>
          <div style={{ display: 'flex', flexDirection: 'column' }}>
            <div className={labelCls} style={{ color: '#a0a0a0'}}>TOTAL SPEND</div>
            <div className={valueCls} style={{ marginTop: 4 }}>{fmtUSD(m.total_spend_usd)}</div>
          </div>
        </div>
      </div>

      {/* Live Throughput card */}
      <div style={{ background: '#000' }}>
        <div className={headerCls}>LIVE THROUGHPUT</div>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: gapPx, color: '#cfcfcf', padding: '8px' }}>
          <div style={{ display: 'flex', flexDirection: 'column' }}>
            <div className={labelCls} style={{ color: '#a0a0a0'}}>TOKENS / SEC</div>
            <div className={valueCls} style={{ marginTop: 4 }}>{fmtInt(m.live_tps)}</div>
          </div>
          <div style={{ display: 'flex', flexDirection: 'column' }}>
            <div className={labelCls} style={{ color: '#a0a0a0'}}>SPEND / SEC</div>
            <div className={valueCls} style={{ marginTop: 4 }}>{fmtUSD(m.live_spend_per_s)}</div>
          </div>
        </div>
      </div>

      {/* Project Completion Rate card (optionally hidden on mobile) */}
      {hideCompletion ? null : (
        <div style={{ background: '#000', display: 'flex', flexDirection: 'column', minHeight: 0 }}>
          <div className={headerCls}>COMPLETION RATE</div>
          <div style={{ padding: '8px', flex: 1, minHeight: 0, height: compact ? 120 : undefined }}>
            <Chart points={points} containerRef={containerRef} />
          </div>
        </div>
      )}
    </div>
  );
}

function Chart({ points, containerRef }: { points: Array<{ t: number; v: number }>; containerRef: React.RefObject<HTMLDivElement | null> }) {
  const [size, setSize] = useState({ w: 300, h: 120 });
  useEffect(() => {
    const el = containerRef.current;
    if (!el) return;
    const r = new ResizeObserver(() => setSize({ w: el.clientWidth, h: el.clientHeight }));
    r.observe(el);
    setSize({ w: el.clientWidth, h: el.clientHeight });
    return () => r.disconnect();
  }, [containerRef]);
  const pad = 12; // general padding
  const w = Math.max(10, size.w);
  const h = Math.max(10, size.h);
  const span = Math.max(5, points.length ? points[points.length - 1].t : 5);
  // Dynamic Y max scales with current progress so small movements are visible
  const yMax = React.useMemo(() => {
    let m = 0;
    for (const p of points) if (Number.isFinite(p.v) && p.v > m) m = p.v;
    return m;
  }, [points]);
  const yMaxClamp = Math.max(0.0001, yMax);
  const yTopPct = Math.max(1, Math.round(yMaxClamp * 100));
  const d = React.useMemo(() => {
    if (!points.length) return '';
    const coords = points.map(({ t, v }) => {
      const x = pad + (t / span) * Math.max(1, w - pad * 2);
      const vy = Math.max(0, Math.min(1, v / yMaxClamp));
      const y = pad + (1 - vy) * Math.max(1, h - pad * 2);
      return `${x.toFixed(1)},${y.toFixed(1)}`;
    });
    return `M ${coords.join(' L ')}`;
  }, [points, w, h, span, yMaxClamp]);
  return (
    <div ref={containerRef} style={{ position: 'relative', width: '100%', height: '100%' }}>
      <svg width="100%" height="100%" style={{ display: 'block' }}>
        {/* Axes */}
        <line x1={pad} y1={h - pad} x2={w - pad} y2={h - pad} stroke="#555" strokeWidth={1} />
        <line x1={pad} y1={pad} x2={pad} y2={h - pad} stroke="#555" strokeWidth={1} />
        {/* X ticks and moving time label */}
        {(() => {
          const ticks: React.ReactElement[] = [];
          // Choose a friendly tick interval
          const tick = span <= 10 ? 1 : span <= 30 ? 5 : span <= 120 ? 10 : 30;
          for (let t = 0; t <= span + 0.001; t += tick) {
            const x = pad + (t / span) * Math.max(1, w - pad * 2);
            ticks.push(
              <g key={`xt-${t.toFixed(2)}`}>
                {/* Keep ticks and labels inside the chart area to avoid clipping */}
                <line x1={x+10} y1={h} x2={x+10} y2={h - pad } stroke="#555" strokeWidth={1} />
                <text x={x+10} y={h - pad + 10} fill="#777" fontSize={9} textAnchor="middle">{Math.round(t)}s</text>
              </g>
            );
          }
          // Moving time label at right end
          const xr = w - pad;
          return (
            <g key="time-label">
              {ticks}
              <text x={xr} y={h - pad - 16} fill="#aaa" fontSize={10} textAnchor="end">{Math.round(span)}s</text>
            </g>
          );
        })()}
        {/* Axis labels */}
        <text x={w / 2} y={h} textAnchor="middle" fill="#888" fontSize={10}>Duration</text>
        {/* <text x={pad - 4} y={h / 2} fill="#888" fontSize={10} transform={`rotate(-90 ${pad - 4},${h / 2})`} textAnchor="middle">Progress</text> */}
        {/* 0% and dynamic-top markers */}
        <text x={pad + 2} y={h - pad - 2} fill="#666" fontSize={9}>0%</text>
        <text x={pad + 2} y={pad + 9} fill="#666" fontSize={9}>{yTopPct}%</text>
        {/* Path */}
        <path d={d} fill="none" stroke="var(--row-queued-fg)" strokeWidth={2} />
      </svg>
    </div>
  );
}
```

## File: `components/WorkTable.test.tsx`
```tsx
import { describe, it, expect, beforeEach } from 'vitest';
import { render, screen, within } from '@testing-library/react';
import WorkTable from './WorkTable';
import { appStore } from '@/lib/store';

beforeEach(() => {
  appStore.setState({
    items: {
      A1: { id: 'A1', group: 'A', sector: 'Planning', depends_on: [], estimate_ms: 10000, tps_min: 1, tps_max: 2, tps: 1.5, tokens_done: 12, est_tokens: 15, eta_ms: 8000, status: 'queued' },
      B1: { id: 'B1', group: 'B', sector: 'Build', depends_on: ['A1','X1','X2','X3'], estimate_ms: 10000, tps_min: 1, tps_max: 2, tps: 1.2, tokens_done: 3, est_tokens: 15, eta_ms: 6000, status: 'assigned' },
      C1: { id: 'C1', group: 'C', sector: 'Eval', depends_on: ['A1'], estimate_ms: 5000, tps_min: 1, tps_max: 2, tps: 1.7, tokens_done: 5, est_tokens: 8, eta_ms: 2000, status: 'in_progress', agent_id: 'AG1', started_at: Date.now() - 3000 },
    },
  });
});

describe('WorkTable', () => {
  it('renders rows sorted by status then id and truncates deps', () => {
    render(<WorkTable />);
    const rows = screen.getAllByRole('row');
    // rows[0] is header
    const dataRows = rows.slice(1);
    const first = within(dataRows[0]).getByText('A1');
    expect(first).toBeInTheDocument();
    // Check truncation text and new columns render
    expect(screen.getByText(/\+2 more/)).toBeInTheDocument();
    expect(screen.getByText(/Tokens/i)).toBeInTheDocument();
    expect(screen.getByText(/TPS/i)).toBeInTheDocument();
    expect(screen.getByText(/ETA/i)).toBeInTheDocument();
    // A simple spot check for formatted values
    expect(screen.getByText(/12\s*\/\s*15/)).toBeInTheDocument();
  });
});
```

## File: `components/WorkTable.tsx`
```tsx
"use client";

import React, { useMemo, useSyncExternalStore } from 'react';
import type { UIState } from '@/lib/store';
import { appStore } from '@/lib/store';
import type { WorkItem } from '@/lib/types';
import { formatTokensAbbrev } from '@/lib/format';

function useAppSelector<T>(selector: (s: UIState) => T): T {
  return useSyncExternalStore(
    appStore.subscribe,
    () => selector(appStore.getState()),
    () => selector(appStore.getState())
  );
}

const statusOrder: Record<string, number> = {
  in_progress: 0,
  queued: 1,
  assigned: 1,
  blocked: 1,
  done: 2,
};

function fmtETA(ms?: number) {
  if (typeof ms !== 'number' || !isFinite(ms) || ms < 0) return '—';
  const total = Math.round(ms / 1000);
  const h = Math.floor(total / 3600);
  const m = Math.floor((total % 3600) / 60);
  const s = total % 60;
  const mm = m.toString().padStart(2, '0');
  const ss = s.toString().padStart(2, '0');
  return h > 0 ? `${h}:${mm}:${ss}` : `${mm}:${ss}`;
}

type ColumnKey = 'id' | 'agent' | 'sector' | 'work' | 'tokens' | 'tps' | 'eta';

export default function WorkTable({
  compact = false,
  mini = false,
  maxHeight,
  columns,
}: {
  compact?: boolean;
  mini?: boolean;
  maxHeight?: number;
  columns?: ColumnKey[];
}) {
  const items = useAppSelector((s) => s.items);

  const rows = useMemo(() => {
    const list = Object.values(items);
    list.sort((a, b) => {
      const ao = statusOrder[a.status] ?? 99;
      const bo = statusOrder[b.status] ?? 99;
      if (ao !== bo) return ao - bo;
      return a.id.localeCompare(b.id);
    });
    return list;
  }, [items]);

  const widthMap: Record<ColumnKey, number> = compact
    ? { id: 22, agent: 26, sector: 38, work: 150, tokens: 34, tps: 34, eta: 42 }
    : { id: 30, agent: 35, sector: 65, work: 225, tokens: 40, tps: 45, eta: 50 };
  const labelMap: Record<ColumnKey, string> = {
    id: 'ID',
    agent: 'AGENT',
    sector: 'SECTOR',
    work: 'WORK ORDER',
    tokens: 'TOKENS',
    tps: 'TPS',
    eta: 'ETA',
  };
  const renderCell: Record<ColumnKey, (it: WorkItem, cls: string) => React.ReactNode> = {
    id: (it, cls) => (
      <td className={`${cls} font-mono`} style={{ backgroundColor: 'inherit', borderLeft: '4px solid currentColor' }}>{it.id}</td>
    ),
    agent: (it, cls) => (
      <td className={`${cls} font-mono`}>{it.agent_id ?? '—'}</td>
    ),
    sector: (it, cls) => (
      <td className={cls} style={{ backgroundColor: 'inherit' }}>{it.sector}</td>
    ),
    work: (it, cls) => (
      <td className={cls} style={{ backgroundColor: 'inherit', maxWidth: workMaxWidth, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }} title={it.desc || ''}>
        {it.desc || '—'}
      </td>
    ),
    tokens: (it, cls) => (
      <td className={cls} style={{ backgroundColor: 'inherit' }}>{formatTokensAbbrev(it.tokens_done)}</td>
    ),
    tps: (it, cls) => {
      const text = it.status === 'in_progress'
        ? formatTokensAbbrev(it.tps, { tpsMode: true, extraDecimalUnder100: true })
        : '0';
      return (
        <td className={cls} style={{ backgroundColor: 'inherit' }}>{text}</td>
      );
    },
    eta: (it, cls) => (
      <td className={cls} style={{ backgroundColor: 'inherit' }}>{fmtETA(it.eta_ms)}</td>
    ),
  };

  const activeColumns: ColumnKey[] = columns && columns.length
    ? columns
    : ['id', 'agent', 'sector', 'work', 'tokens', 'tps', 'eta'];

  const workMaxWidth = compact ? 200 : 360;
  const tableTextCls = compact ? (mini ? 'text-[11px]' : 'text-xs') : 'text-sm';
  const thPad = compact ? (mini ? 'px-1 py-0.5' : 'px-1 py-1') : 'px-1 py-2';
  const tdPad = compact ? (mini ? 'px-1 py-0.5' : 'px-1 py-0.5') : 'px-2 py-1';

  return (
    <div className="h-full min-h-0 flex flex-col">
      <div className="flex-1 min-h-0 overflow-auto no-scrollbar border border-[#352b19ff] border-t-0" style={{ maxHeight: maxHeight }}>
        <table
              className={`min-w-full ${tableTextCls}`}
              style={{
                tableLayout: 'fixed',
                width: '100%',
                borderCollapse: 'separate',
                borderSpacing: compact ? (mini ? '1px' : '2px') : '4px',
                backgroundColor: '#000',
              }}>
          <colgroup>
            {activeColumns.map((key) => (
              <col key={key} style={{ width: widthMap[key] }} />
            ))}
          </colgroup>
          <thead className="text-[#d79326ff]">
            <tr>
              {activeColumns.map((key) => (
                <th key={key} className={`${thPad} text-left border-b-1`}>{labelMap[key]}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {rows.map((it) => {
              const rowCls =
                it.status === 'done' ? 'tr-status-done' :
                it.status === 'in_progress' ? 'tr-status-inprogress' :
                'tr-status-queued';
              return (
                <tr key={it.id} className={`${rowCls}`}>
                  {activeColumns.map((key) => (
                    <React.Fragment key={`${it.id}:${key}`}>
                      {renderCell[key](it, tdPad)}
                    </React.Fragment>
                  ))}
                </tr>
              );
            })}
            {rows.length === 0 && (
              <tr className="pt-2">
                <td colSpan={activeColumns.length} className="px-3 py-3 text-gray-400">No items loaded yet.</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
```

## File: `lib/bridgeToStore.test.ts`
```typescript
import { describe, it, expect } from 'vitest';
import { attachBridgeToStore } from './bridgeToStore';
import { createAppStore } from './store';
import type { SimMsg } from './simBridge';

class FakeBridge {
  private subs = new Set<(msg: SimMsg) => void>();
  subscribe(handler: (msg: SimMsg) => void) {
    this.subs.add(handler);
    return () => this.subs.delete(handler);
  }
  emit(msg: SimMsg) {
    for (const h of this.subs) h(msg);
  }
}

function wait(ms: number) {
  return new Promise((r) => setTimeout(r, ms));
}

describe('throttle-coalesces-updates', () => {
  it('coalesces many ticks into a single store update per interval', async () => {
    const bridge = new FakeBridge();
    const store = createAppStore();
    let updates = 0;
    const unsubStore = store.subscribe(() => updates++);

    const { destroy } = attachBridgeToStore(bridge, store, { intervalMs: 20 });

    // Emit a burst of ticks
    for (let i = 1; i <= 10; i++) {
      bridge.emit({ type: 'tick', tick_id: i });
    }

    // Wait a bit longer than interval to allow flush
    await wait(30);

    expect(store.getState().lastTickId).toBe(10);
    // Should be 1 or a very small number, not 10
    expect(updates).toBeLessThanOrEqual(2);

    unsubStore();
    destroy();
  });

  it('applies snapshot immediately and resets aggregation', async () => {
    const bridge = new FakeBridge();
    const store = createAppStore();
    const { destroy } = attachBridgeToStore(bridge, store, { intervalMs: 50 });

    bridge.emit({ type: 'tick', tick_id: 1 });
    bridge.emit({
      type: 'snapshot',
      state: {
        items: {},
        agents: {},
        metrics: { active_agents: 0, total_tokens: 0, total_spend_usd: 0, live_tps: 0, live_spend_per_s: 0, completion_rate: 0 },
        seed: 's',
        running: true,
      },
    });

    // Next tick id lower than previous should still apply because snapshot reset
    bridge.emit({ type: 'tick', tick_id: 1 });
    await wait(60);
    expect(store.getState().lastTickId).toBe(1);

    destroy();
  });
});

```

## File: `lib/bridgeToStore.ts`
```typescript
import type { SimMsg } from './simBridge';
import type { UIState } from './store';
import type { WorkItem, Agent, ProjectMetrics } from './types';
import { STORE_FLUSH_INTERVAL_MS } from './config';
import { debugLog } from './debug';

export interface Subscribable<M> {
  subscribe: (handler: (msg: M) => void) => () => void;
}

export interface AttachOptions {
  intervalMs?: number; // default 100ms
}

// Attaches a SimMsg stream to the Zustand store, coalescing diffs
// to reduce render churn. Snapshot applies immediately; ticks merge
// within the interval window and apply as a single reducer call.
export function attachBridgeToStore(
  bridge: Subscribable<SimMsg>,
  store: { getState: () => UIState },
  opts: AttachOptions = {}
) {
  const interval = opts.intervalMs ?? STORE_FLUSH_INTERVAL_MS;
  let unsub: (() => void) | null = null;
  let timer: ReturnType<typeof setTimeout> | null = null;

  // Aggregation state
  let latestTick = 0;
  const itemMap = new Map<string, Partial<WorkItem> & { id: string }>();
  const agentMap = new Map<string, Partial<Agent> & { id: string }>();
  let metricsPatch: Partial<ProjectMetrics> | null = null;
  const agentsRemove = new Set<string>();

  const clearAgg = () => {
    latestTick = 0;
    itemMap.clear();
    agentMap.clear();
    metricsPatch = null;
    agentsRemove.clear();
  };

  const scheduleFlush = () => {
    if (timer != null) return;
    timer = setTimeout(() => {
      timer = null;
      if (latestTick === 0) return; // nothing to apply
      const items = itemMap.size ? Array.from(itemMap.values()) : undefined;
      const agents = agentMap.size ? Array.from(agentMap.values()) : undefined;
      const metrics = metricsPatch ?? undefined;
      const agents_remove = agentsRemove.size ? Array.from(agentsRemove) : undefined;
      debugLog('bridgeToStore', 'applyTick', { tick_id: latestTick, items: items?.length ?? 0, agents: agents?.length ?? 0, metrics: !!metrics, agents_remove: agents_remove?.length ?? 0 });
      store.getState().applyTick({ tick_id: latestTick, items, agents, metrics, agents_remove });
      clearAgg();
    }, Math.max(0, interval));
  };

  const onMsg = (msg: SimMsg) => {
    if (msg.type === 'snapshot') {
      // Apply immediately; reset any pending agg
      clearAgg();
      debugLog('bridgeToStore', 'applySnapshot');
      store.getState().applySnapshot(msg.state);
      return;
    }
    if (msg.type === 'tick') {
      if (msg.tick_id <= latestTick) {
        // already aggregated something newer in this window
        return;
      }
      latestTick = msg.tick_id;
      if (msg.items) {
        for (const patch of msg.items) {
          if (patch.id) itemMap.set(patch.id, { ...(itemMap.get(patch.id) ?? {}), ...patch } as Partial<WorkItem> & { id: string });
        }
      }
      if (msg.agents) {
        for (const patch of msg.agents) {
          if (patch.id) agentMap.set(patch.id, { ...(agentMap.get(patch.id) ?? {}), ...patch } as Partial<Agent> & { id: string });
        }
      }
      if (msg.metrics) metricsPatch = { ...(metricsPatch ?? {}), ...msg.metrics };
      if ('agents_remove' in msg && msg.agents_remove) for (const id of msg.agents_remove) agentsRemove.add(id);
      scheduleFlush();
      return;
    }
    // Other event types can be handled later if needed; ignored for throttling
  };

  unsub = bridge.subscribe(onMsg);

  return {
    destroy() {
      if (unsub) unsub();
      unsub = null;
      if (timer) clearTimeout(timer);
      timer = null;
      clearAgg();
    },
  };
}
```

## File: `lib/config.test.ts`
```typescript
import { describe, it, expect } from 'vitest';
import { BRIDGE_BATCH_MS, STORE_FLUSH_INTERVAL_MS, ENGINE_TICK_HZ, DEFAULT_SEED } from './config';

describe('config defaults', () => {
  it('has sane positive numeric defaults', () => {
    expect(BRIDGE_BATCH_MS).toBeGreaterThan(0);
    expect(STORE_FLUSH_INTERVAL_MS).toBeGreaterThan(0);
    expect(ENGINE_TICK_HZ).toBeGreaterThan(0);
  });

  it('has a default seed string', () => {
    expect(typeof DEFAULT_SEED).toBe('string');
    expect(DEFAULT_SEED.length).toBeGreaterThan(0);
  });
});

```

## File: `lib/config.ts`
```typescript
// Centralized runtime configuration and tuning knobs

// Bridge batching cadence (ms) and store flush cadence (ms) are centralized in constants.
// See constants for guidance on tuning.
export { BRIDGE_BATCH_MS, STORE_FLUSH_INTERVAL_MS } from './constants';

// Engine tick rate is now centralized in constants for simplicity.
export { ENGINE_TICK_HZ } from './constants';

// App defaults
export const DEFAULT_SEED = (process.env.NEXT_PUBLIC_DEFAULT_SEED as string) || 'auto';
export const RUNNING_DEFAULT = ((process.env.NEXT_PUBLIC_RUNNING_DEFAULT as string) ?? 'true') === 'true';

// Debug logging toggle
export const DEBUG_LOGS = ((process.env.NEXT_PUBLIC_DEBUG_LOGS as string) ?? 'true') === 'true';
```

## File: `lib/constants.test.ts`
```typescript
import { describe, it, expect } from 'vitest';
import { COST_PER_TOKEN_USD, MAX_CONCURRENT, V_MIN, V_MAX } from './constants';

describe('constants-sanity', () => {
  it('has valid numeric relationships', () => {
    expect(Number.isFinite(COST_PER_TOKEN_USD)).toBe(true);
    expect(COST_PER_TOKEN_USD).toBeGreaterThan(0);
    expect(MAX_CONCURRENT).toBeGreaterThan(0);
    expect(V_MIN).toBeGreaterThan(0);
    expect(V_MAX).toBeGreaterThan(V_MIN);
  });
});

```

## File: `lib/constants.ts`
```typescript
// Core constants for Calming Control Room (tunable via PRD)

// Cost model (USD per token). Example: $0.002 per 1K tokens => 0.000002 per token
export const COST_PER_TOKEN_USD = 0.00013;

// Concurrency and motion tuning
export const MAX_CONCURRENT = 12;
export const V_MIN = 0.002; // world units/frame
export const V_MAX = 0.010; // world units/frame
export const TRAIL_DECAY = 0.08; // alpha per frame on motion buffer

// Radar visuals
export const RING_COUNT = 5;

// Radar path curvature controls
// - RADAR_CURVE_AMOUNT: 0 = straight lines to center, 1 = max curve (half turn cap)
// - RADAR_MAX_TURNS: maximum rotations (in turns) allowed over full path. 0.5 = half rotation
// - RADAR_WOBBLE: proportion of the curve budget allocated to side-to-side wobble (random per agent)
export const RADAR_CURVE_AMOUNT = 0.6; // main knob to increase/decrease curvature [0..1]
export const RADAR_MAX_TURNS = 0.4;    // cap total spin to half a rotation
export const RADAR_WOBBLE = 0.3;      // 0 = pure spiral, 1 = mostly wobble

// Radar completion pulse controls
// A subtle expanding ring emitted at the center when an agent reaches the target.
export const RADAR_PULSE_MAX_RADIUS = 0.10; // as fraction of radar radius
export const RADAR_PULSE_DURATION_MS = 800; // total life of a pulse
export const RADAR_PULSE_WIDTH = 4;         // stroke width in px
export const RADAR_PULSE_SECONDARY = 0.6;   // second ring offset multiplier (0 to disable)

// Radar ping sound volume
export const RADAR_PING_VOLUME = 0.5;
export const RADAR_PING_AUDIO_PATH = '/audio/sonar_ping_3.mp3';

// Radar render/update cadence (UI only; not engine tick)
// Controls how often agent positions and effects update on the radar.
export const RADAR_REFRESH_HZ = 30; // e.g., 30 Hz; set 60 for smoother motion

// Engine tick rate (Hz). Worker internal loop cadence (not UI render).
export const ENGINE_TICK_HZ = 30;

// TPS dynamics (per-item throughput variability)
// - TPS_ALPHA: smoothing toward the current target per tick (higher = faster moves)
// - TPS_TARGET_HOLD_MS_*: how long to hold a sampled target before choosing a new one
// - TPS_JITTER_FRAC: small per-tick flutter around the held target (as fraction of range)
export const TPS_ALPHA = 0.3;
export const TPS_TARGET_HOLD_MS_MIN = 1600;
export const TPS_TARGET_HOLD_MS_MAX = 3600;
export const TPS_JITTER_FRAC = 0.03;

// Transport batching and store flush cadences (UI data pipeline)
// - BRIDGE_BATCH_MS: Coalesces raw worker messages before applying to the app store.
//   Higher values reduce churn (fewer updates) but can add latency.
// - STORE_FLUSH_INTERVAL_MS: How often coalesced diffs are committed to Zustand.
//   Keep similar to BRIDGE_BATCH_MS unless you want extra smoothing.
export const BRIDGE_BATCH_MS = 50;          // ms: batch worker messages
export const STORE_FLUSH_INTERVAL_MS = 50;  // ms: flush coalesced diffs to store

// Sectors and colors
export const SECTORS = ['PLANNING', 'BUILD', 'EVAL', 'DEPLOY'] as const;
export type Sector = typeof SECTORS[number];
export const SECTOR_COLORS: Record<Sector, string> = {
  PLANNING: '#6EE7B7',
  BUILD: '#93C5FD',
  EVAL: '#FCA5A5',
  DEPLOY: '#FDE68A',
};

// Keep stub flag to satisfy existing import smoke test
export const CONSTANTS_MODULE_LOADED = true;
```

## File: `lib/debug.ts`
```typescript
import { DEBUG_LOGS } from './config';

export function debugLog(tag: string, ...args: unknown[]) {
  if (!DEBUG_LOGS) return;
  console.log(`[${tag}]`, ...args);
}

```

## File: `lib/engine.test.ts`
```typescript
import { describe, it, expect } from 'vitest';
import { buildItemsFromPlan, detectCycles, promoteQueuedToAssigned, computeMetrics } from './engine';
import type { PlanDefinition } from '@/plans/types';
import type { Agent, WorkItem } from './types';

describe('deps-resolver', () => {
  it('promotes items whose deps are satisfied', () => {
    const plan: PlanDefinition = {
      name: 'Test',
      items: [
        { id: 'A', group: 'X', sector: 'Planning', depends_on: [], estimate_ms: 1000, tps_min: 1, tps_max: 2 },
        { id: 'B', group: 'X', sector: 'Build', depends_on: ['A'], estimate_ms: 1000, tps_min: 1, tps_max: 2 },
      ],
    };
    const items = buildItemsFromPlan(plan);
    // Initially A has no deps -> should become assigned
    const first = promoteQueuedToAssigned(items);
    expect(first).toContain('A');
    expect(items['A'].status).toBe('assigned');
    expect(items['B'].status).toBe('queued');

    // Mark A done -> B becomes assigned
    items['A'].status = 'done';
    const second = promoteQueuedToAssigned(items);
    expect(second).toContain('B');
    expect(items['B'].status).toBe('assigned');
  });

  it('metrics-math computes totals and rates', () => {
    const plan: PlanDefinition = {
      name: 'Metrics',
      items: [
        { id: 'A', group: 'G', sector: 'Planning', depends_on: [], estimate_ms: 10000, tps_min: 2, tps_max: 4 },
        { id: 'B', group: 'G', sector: 'Build', depends_on: ['A'], estimate_ms: 5000, tps_min: 5, tps_max: 6 },
      ],
    };
    const items = buildItemsFromPlan(plan);
    // Make A done with tokens and B in_progress with current tps
    items['A'].status = 'done';
    items['A'].tokens_done = 100;
    items['B'].status = 'in_progress';
    items['B'].tps = 5;
    items['B'].tokens_done = 20;
    const agents: Record<string, Agent> = { AG1: { id: 'AG1', work_item_id: 'B', x: 0, y: 0, v: 0, curve_phase: 0 } };
    const m = computeMetrics(items as Record<string, WorkItem>, agents);
    expect(m.active_agents).toBe(1);
    expect(m.total_tokens).toBeCloseTo(120, 5);
    expect(m.live_tps).toBeCloseTo(5, 5);
    // Time-weighted completion across whole plan:
    // A contributes 100% of its 10s, B contributes (20/28) of its 5s
    // => (10s + 5s * 20/28) / (10s + 5s)
    const estTokensB = Math.round(((5 + 6) / 2) * (5000 / 1000));
    const expected = (10000 + 5000 * (20 / estTokensB)) / (10000 + 5000);
    expect(m.completion_rate).toBeCloseTo(expected, 5);
    expect(m.total_spend_usd).toBeGreaterThan(0);
    expect(m.live_spend_per_s).toBeGreaterThan(0);
  });

  it('detects cycles and leaves them queued', () => {
    const plan: PlanDefinition = {
      name: 'Cycle',
      items: [
        { id: 'A', group: 'X', sector: 'Planning', depends_on: ['B'], estimate_ms: 1000, tps_min: 1, tps_max: 2 },
        { id: 'B', group: 'X', sector: 'Build', depends_on: ['A'], estimate_ms: 1000, tps_min: 1, tps_max: 2 },
      ],
    };
    const items = buildItemsFromPlan(plan);
    const cycles = detectCycles(items);
    expect(cycles.length).toBeGreaterThan(0);
    const changed = promoteQueuedToAssigned(items);
    expect(changed.length).toBe(0);
    expect(items['A'].status).toBe('queued');
    expect(items['B'].status).toBe('queued');
  });
});
```

## File: `lib/engine.ts`
```typescript
import type { WorkItem } from './types';
import type { PlanDefinition } from '@/plans/types';
import type { Agent, ProjectMetrics } from './types';
import { COST_PER_TOKEN_USD } from './constants';

export function buildItemsFromPlan(plan: PlanDefinition): Record<string, WorkItem> {
  const items: Record<string, WorkItem> = {};
  for (const p of plan.items) {
    const est_tokens = Math.round(((p.tps_min + p.tps_max) / 2) * (p.estimate_ms / 1000));
    items[p.id] = {
      id: p.id,
      group: p.group,
      sector: p.sector,
      depends_on: [...p.depends_on],
      desc: p.work_desc,
      estimate_ms: p.estimate_ms,
      started_at: undefined,
      eta_ms: p.estimate_ms,
      tps_min: p.tps_min,
      tps_max: p.tps_max,
      tps: p.tps_min,
      tokens_done: 0,
      est_tokens,
      status: 'queued',
      agent_id: undefined,
    };
  }
  return items;
}

// Detect cycles using DFS. Returns list of cycles (each as id array) or empty if none.
export function detectCycles(items: Record<string, WorkItem>): string[][] {
  const graph = new Map<string, string[]>(
    Object.values(items).map((i) => [i.id, i.depends_on])
  );
  const cycles: string[][] = [];
  const visited = new Set<string>();
  const stack: string[] = [];
  const onstack = new Set<string>();

  function dfs(u: string) {
    visited.add(u);
    onstack.add(u);
    stack.push(u);
    for (const v of graph.get(u) || []) {
      if (!visited.has(v)) dfs(v);
      else if (onstack.has(v)) {
        // found a cycle: slice from v to end
        const idx = stack.indexOf(v);
        if (idx >= 0) cycles.push(stack.slice(idx));
      }
    }
    stack.pop();
    onstack.delete(u);
  }

  for (const id of graph.keys()) if (!visited.has(id)) dfs(id);
  // Deduplicate identical cycles (simple heuristic)
  const unique: string[][] = [];
  const seen = new Set<string>();
  for (const c of cycles) {
    const key = c.slice().sort().join('|');
    if (!seen.has(key)) {
      seen.add(key);
      unique.push(c);
    }
  }
  return unique;
}

// Returns true if all dependencies of item id are in status 'done'
export function depsSatisfied(items: Record<string, WorkItem>, id: string): boolean {
  const it = items[id];
  if (!it) return false;
  return it.depends_on.every((d) => items[d] && items[d].status === 'done');
}

// Promote items from queued -> assigned when dependencies are satisfied.
export function promoteQueuedToAssigned(items: Record<string, WorkItem>): string[] {
  const changed: string[] = [];
  for (const it of Object.values(items)) {
    if (it.status === 'queued' && depsSatisfied(items, it.id)) {
      it.status = 'assigned';
      changed.push(it.id);
    }
  }
  return changed;
}

export function countInProgress(items: Record<string, WorkItem>): number {
  let n = 0;
  for (const it of Object.values(items)) if (it.status === 'in_progress') n++;
  return n;
}

export function computeMetrics(items: Record<string, WorkItem>, agents: Record<string, Agent>): ProjectMetrics {
  let total_tokens = 0;
  let live_tps = 0;
  let total_estimate_ms = 0;
  let progressed_ms = 0;
  const now = Date.now();

  for (const it of Object.values(items)) {
    total_tokens += it.tokens_done || 0;
    if (it.status === 'in_progress') live_tps += it.tps || 0;

    const est = Math.max(0, it.estimate_ms || 0);
    total_estimate_ms += est;
    if (est <= 0) continue;

    if (it.status === 'done') {
      progressed_ms += est;
    } else if (it.status === 'in_progress') {
      // Prefer ETA-based progress when available
      if (typeof it.eta_ms === 'number' && isFinite(it.eta_ms)) {
        const elapsed = Math.max(0, Math.min(est, est - it.eta_ms));
        progressed_ms += elapsed;
      } else if (typeof it.started_at === 'number' && isFinite(it.started_at)) {
        const elapsed = Math.max(0, Math.min(est, now - it.started_at));
        progressed_ms += elapsed;
      } else if (typeof it.est_tokens === 'number' && it.est_tokens > 0) {
        const td = Math.max(0, it.tokens_done || 0);
        const frac = Math.max(0, Math.min(1, td / it.est_tokens));
        progressed_ms += frac * est;
      }
    }
  }

  const total_spend_usd = total_tokens * COST_PER_TOKEN_USD;
  const live_spend_per_s = live_tps * COST_PER_TOKEN_USD;
  const completion_rate = total_estimate_ms > 0 ? progressed_ms / total_estimate_ms : 0;

  return {
    active_agents: Object.keys(agents).length,
    total_tokens,
    total_spend_usd,
    live_tps,
    live_spend_per_s,
    completion_rate,
  };
}
```

## File: `lib/format.ts`
```typescript
export type FormatAbbrevOptions = {
  // When formatting tokens/second, show decimals under 1000 instead of integer-only
  tpsMode?: boolean;
  // If true and in tpsMode, show 2 decimals when value < 100
  extraDecimalUnder100?: boolean;
};

export function formatTokensAbbrev(n?: number | null, opts?: FormatAbbrevOptions): string {
  const num = typeof n === 'number' && isFinite(n) ? n : 0;
  const sign = num < 0 ? '-' : '';
  const v = Math.abs(num);

  const fmtInt = (x: number) => new Intl.NumberFormat('en-US', { maximumFractionDigits: 0 }).format(x);

  if (v < 1000) {
    if (opts?.tpsMode) {
      const decimals = opts.extraDecimalUnder100 && v < 100 ? 2 : 1;
      const rounded = Math.round(v * 10 ** decimals) / 10 ** decimals;
      return sign + rounded.toFixed(decimals);
    }
    return sign + fmtInt(v);
  }
  const units: Array<[number, string]> = [
    [1_000_000_000_000, 'T'],
    [1_000_000_000, 'B'],
    [1_000_000, 'M'],
    [1_000, 'k'],
  ];
  for (const [div, suf] of units) {
    if (v >= div) {
      const val = v / div;
      const s = val.toFixed(1); // always show one decimal for consistency (e.g., 25.0k)
      return `${sign}${s}${suf}`;
    }
  }
  return sign + fmtInt(v);
}
```

## File: `lib/imports.test.ts`
```typescript
import { describe, it, expect } from 'vitest';

describe('imports-don\'t-throw', () => {
  it('imports all stub modules without throwing', async () => {
    // Test that each module can be imported
    const { TYPES_MODULE_LOADED } = await import('./types');
    expect(TYPES_MODULE_LOADED).toBe(true);
    
    const { CONSTANTS_MODULE_LOADED } = await import('./constants');
    expect(CONSTANTS_MODULE_LOADED).toBe(true);
    
    const { RNG_MODULE_LOADED } = await import('./rng');
    expect(RNG_MODULE_LOADED).toBe(true);
    
    const { SIMBRIDGE_MODULE_LOADED } = await import('./simBridge');
    expect(SIMBRIDGE_MODULE_LOADED).toBe(true);
    
    // Worker module can't be directly imported in test environment,
    // but we can verify the file exists
    const workerModule = await import('../workers/engine');
    expect(workerModule.ENGINE_WORKER_MODULE_LOADED).toBe(true);
  });
});
```

## File: `lib/rng.test.ts`
```typescript
import { describe, it, expect } from 'vitest';
import { createRNG, seedFromString } from './rng';

describe('rng-determinism', () => {
  it('same numeric seed yields same sequence', () => {
    const a = createRNG(123456);
    const b = createRNG(123456);
    const seqA = Array.from({ length: 5 }, () => a.next());
    const seqB = Array.from({ length: 5 }, () => b.next());
    expect(seqA).toEqual(seqB);
  });

  it('same string seed yields same sequence', () => {
    const a = createRNG('hello');
    const b = createRNG('hello');
    const seqA = Array.from({ length: 5 }, () => a.int(0, 1000));
    const seqB = Array.from({ length: 5 }, () => b.int(0, 1000));
    expect(seqA).toEqual(seqB);
  });

  it('different seed diverges quickly', () => {
    const a = createRNG('hello');
    const b = createRNG('hello2');
    const seqA = Array.from({ length: 5 }, () => a.next());
    const seqB = Array.from({ length: 5 }, () => b.next());
    expect(seqA).not.toEqual(seqB);
  });

  it('seedFromString is stable', () => {
    expect(seedFromString('abc')).toEqual(seedFromString('abc'));
  });
});

```

## File: `lib/rng.ts`
```typescript
// Deterministic RNG utilities (mulberry32 + string seeding)

// Hash a string to a 32-bit unsigned integer (xmur3-like)
export function seedFromString(str: string): number {
  let h = 1779033703 ^ str.length;
  for (let i = 0; i < str.length; i++) {
    h = Math.imul(h ^ str.charCodeAt(i), 3432918353);
    h = (h << 13) | (h >>> 19);
  }
  h = Math.imul(h ^ (h >>> 16), 2246822507);
  h = Math.imul(h ^ (h >>> 13), 3266489909);
  h ^= h >>> 16;
  // Ensure uint32
  return h >>> 0;
}

// mulberry32 PRNG
function mulberry32(seed: number) {
  let a = seed >>> 0;
  return function next() {
    a |= 0;
    a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296; // [0,1)
  };
}

export interface RNG {
  seed: number;
  next: () => number; // float in [0,1)
  float: (min: number, max: number) => number;
  int: (min: number, max: number) => number; // inclusive min/max
  bool: (p?: number) => boolean; // true with probability p (default 0.5)
}

export function createRNG(seed: number | string): RNG {
  const s = typeof seed === 'string' ? seedFromString(seed) : (seed >>> 0);
  const base = mulberry32(s);
  const next = () => base();
  const float = (min: number, max: number) => min + (max - min) * next();
  const int = (min: number, max: number) => Math.floor(float(min, max + 1));
  const bool = (p = 0.5) => next() < p;
  return { seed: s, next, float, int, bool };
}

// Keep stub flag to satisfy existing import smoke test
export const RNG_MODULE_LOADED = true;
```

## File: `lib/simBridge.test.ts`
```typescript
import { describe, it, expect } from 'vitest';
import { createSimBridge, type PortLike, type MessageEventLike, type SimMsg } from './simBridge';

class FakePort implements PortLike {
  private handlers = new Set<(e: MessageEventLike) => void>();
  public sent: unknown[] = [];
  postMessage(msg: unknown): void {
    this.sent.push(msg);
  }
  addEventListener(event: 'message', handler: (e: MessageEventLike) => void): void {
    if (event === 'message') this.handlers.add(handler);
  }
  removeEventListener(event: 'message', handler: (e: MessageEventLike) => void): void {
    if (event === 'message') this.handlers.delete(handler);
  }
  emit(msg: SimMsg) {
    for (const h of this.handlers) h({ data: msg });
  }
}

describe('simBridge', () => {
  it('drops out-of-order tick messages', () => {
    const port = new FakePort();
    const bridge = createSimBridge(port, { batchMs: 0 });
    const seen: number[] = [];
    bridge.subscribe((msg) => {
      if (msg.type === 'tick') seen.push(msg.tick_id);
    });

    port.emit({ type: 'tick', tick_id: 1 });
    port.emit({ type: 'tick', tick_id: 3 });
    port.emit({ type: 'tick', tick_id: 2 }); // should be dropped
    port.emit({ type: 'tick', tick_id: 4 });

    expect(seen).toEqual([1, 3, 4]);
  });

  it('resets ordering on snapshot', () => {
    const port = new FakePort();
    const bridge = createSimBridge(port, { batchMs: 0 });
    const seen: SimMsg[] = [];
    bridge.subscribe((msg) => seen.push(msg));

    port.emit({ type: 'tick', tick_id: 2 });
    port.emit({ type: 'snapshot', state: { items: {}, agents: {}, metrics: { active_agents: 0, total_tokens: 0, total_spend_usd: 0, live_tps: 0, live_spend_per_s: 0, completion_rate: 0 }, seed: 's', running: true } });
    port.emit({ type: 'tick', tick_id: 1 }); // accepted after snapshot

    const ticks = seen.filter((m) => m.type === 'tick') as Extract<SimMsg, { type: 'tick' }>[];
    expect(ticks.map((t) => t.tick_id)).toEqual([2, 1]);
  });
});

```

## File: `lib/simBridge.ts`
```typescript
// simBridge: UI-side transport boundary for simulation messages
// Hides transport (Worker now, WebSocket later) behind a small API.

import type { Agent, AppState, ProjectMetrics, WorkItem } from './types';
import { BRIDGE_BATCH_MS } from './config';
import { debugLog } from './debug';

export type SimMsg =
  | { type: 'snapshot'; state: AppState }
  | { type: 'deps_cleared'; id: string }
  | { type: 'start_item'; id: string; agent: Agent }
  | {
      type: 'tick';
      tick_id: number;
      items?: Partial<WorkItem>[];
      agents?: Partial<Agent>[];
      metrics?: Partial<ProjectMetrics>;
      agents_remove?: string[];
    }
  | { type: 'complete_item'; id: string };

export type SimIntent =
  | { type: 'set_running'; running: boolean }
  | { type: 'set_plan'; plan: string }
  | { type: 'set_seed'; seed: string }
  | { type: 'set_speed'; speed: number }
  | { type: 'request_snapshot' };

// Minimal message event/port interfaces so we don't depend on DOM types in tests
export interface MessageEventLike<T = unknown> { data: T }
export interface PortLike {
  postMessage: (msg: unknown) => void;
  addEventListener: (event: 'message', handler: (e: MessageEventLike) => void) => void;
  removeEventListener: (event: 'message', handler: (e: MessageEventLike) => void) => void;
}

export interface SimBridge {
  subscribe: (handler: (msg: SimMsg) => void) => () => void;
  postIntent: (intent: SimIntent) => void;
  getLastTickId: () => number;
  destroy: () => void;
}

export interface BridgeOptions {
  batchMs?: number; // coalesce outbound notifications to subscribers
}

export function createSimBridge(port: PortLike, opts: BridgeOptions = {}): SimBridge {
  const subscribers = new Set<(msg: SimMsg) => void>();
  let lastTickId = 0;
  const batchMs = opts.batchMs ?? BRIDGE_BATCH_MS;
  const queue: SimMsg[] = [];
  let flushTimer: ReturnType<typeof setTimeout> | null = null;

  const emit = (msg: SimMsg) => {
    for (const fn of subscribers) fn(msg);
  };

  const scheduleFlush = () => {
    if (flushTimer != null) return;
    if (batchMs <= 0) {
      flushNow();
      return;
    }
    flushTimer = setTimeout(flushNow, batchMs);
  };

  const flushNow = () => {
    if (flushTimer) clearTimeout(flushTimer);
    flushTimer = null;
    debugLog('bridge', 'flush', { queued: queue.length });
    while (queue.length) {
      const msg = queue.shift()!;
      if (msg.type === 'tick') {
        if (msg.tick_id <= lastTickId) {
          debugLog('bridge', 'drop-late', { tick_id: msg.tick_id, lastTickId });
          continue; // drop out-of-order or duplicate
        }
        lastTickId = msg.tick_id;
      }
      if (msg.type === 'snapshot') {
        // reset ordering on fresh snapshot
        lastTickId = 0;
      }
      debugLog('bridge', 'emit', { type: msg.type, lastTickId });
      emit(msg);
    }
  };

  const onMessage = (e: MessageEventLike) => {
    const raw = e?.data;
    if (!raw || typeof raw !== 'object' || !('type' in raw)) return;
    const msg = raw as SimMsg;
    if (msg.type === 'tick') {
      // Early drop to keep queue lean
      if (msg.tick_id <= lastTickId) {
        debugLog('bridge', 'drop-early', { tick_id: msg.tick_id, lastTickId });
        return;
      }
    } else if (msg.type === 'snapshot') {
      // Snapshot should be delivered promptly; reset tick ordering
      lastTickId = 0;
    }
    debugLog('bridge', 'queue', { type: msg.type, tick_id: msg.type === 'tick' ? msg.tick_id : undefined, size: queue.length + 1 });
    queue.push(msg);
    scheduleFlush();
  };

  port.addEventListener('message', onMessage);
  debugLog('bridge', 'created', { batchMs });

  return {
    subscribe(handler) {
      subscribers.add(handler);
      return () => subscribers.delete(handler);
    },
    postIntent(intent) {
      port.postMessage(intent);
    },
    getLastTickId() {
      return lastTickId;
    },
    destroy() {
      port.removeEventListener('message', onMessage);
      subscribers.clear();
      queue.length = 0;
      if (flushTimer) clearTimeout(flushTimer);
      flushTimer = null;
    },
  };
}

// Keep stub flag for existing smoke test
export const SIMBRIDGE_MODULE_LOADED = true;
```

## File: `lib/simClient.ts`
```typescript
"use client";

import { createSimBridge, type SimBridge } from '@/lib/simBridge';
import { attachBridgeToStore } from '@/lib/bridgeToStore';
import { appStore } from '@/lib/store';
import { debugLog } from '@/lib/debug';

let _bridge: SimBridge | null = null;
let _worker: Worker | null = null;
let _link: { destroy: () => void } | null = null;

export function isConnected() {
  return !!_bridge;
}

export function ensureConnected() {
  if (_bridge) return _bridge;
  if (typeof window === 'undefined' || typeof Worker === 'undefined') return null;
  try {
    _worker = new Worker(new URL('../workers/engine.ts', import.meta.url), { type: 'module' });
    debugLog('simClient', 'worker-created');
    _worker.addEventListener('error', (e: ErrorEvent) => debugLog('simClient', 'worker-error', e?.message || e));
    _worker.addEventListener('message', (e: MessageEvent) => debugLog('simClient', 'worker-message', e?.data));
    _bridge = createSimBridge(_worker);
    _link = attachBridgeToStore(_bridge, appStore);
    // initial handshake
    _bridge.postIntent({ type: 'request_snapshot' });
    return _bridge;
  } catch (e) {
    debugLog('simClient', 'ensureConnected-failed', e);
    return null;
  }
}

export function setExternalBridge(bridge: SimBridge, worker: Worker, link: { destroy: () => void }) {
  if (_bridge) return; // already connected
  _bridge = bridge; _worker = worker; _link = link;
}

export function postIntent(intent: Parameters<SimBridge['postIntent']>[0]) {
  if (!_bridge) ensureConnected();
  _bridge?.postIntent(intent);
}

export function destroyConnection() {
  _link?.destroy();
  try { _worker?.terminate(); } catch {}
  _link = null; _bridge = null; _worker = null;
}

```

## File: `lib/store.test.ts`
```typescript
import { describe, it, expect } from 'vitest';
import { createAppStore } from './store';
import type { AppState } from './types';

describe('reducers-apply-snapshot-and-diff', () => {
  it('applies snapshot then tick diff and advances lastTickId', () => {
    const store = createAppStore();

    const snapshot: AppState = {
      items: {
        A1: {
          id: 'A1',
          group: 'A',
          sector: 'Planning',
          depends_on: [],
          estimate_ms: 10000,
          tps_min: 5,
          tps_max: 10,
          tps: 6,
          tokens_done: 0,
          est_tokens: 60,
          status: 'queued',
        },
        B1: {
          id: 'B1',
          group: 'B',
          sector: 'Build',
          depends_on: [],
          estimate_ms: 15000,
          tps_min: 7,
          tps_max: 12,
          tps: 8,
          tokens_done: 0,
          est_tokens: 100,
          status: 'assigned',
        },
      },
      agents: {},
      metrics: {
        active_agents: 0,
        total_tokens: 0,
        total_spend_usd: 0,
        live_tps: 0,
        live_spend_per_s: 0,
        completion_rate: 0,
      },
      seed: 's',
      running: true,
    };

    store.getState().applySnapshot(snapshot);

    // Apply a diff: update one item and metrics
    store.getState().applyTick({
      tick_id: 1,
      items: [
        { id: 'A1', status: 'in_progress', tps: 9, started_at: 123, eta_ms: 9000 },
      ],
      metrics: { active_agents: 1, live_tps: 9 },
    });

    const state = store.getState();
    expect(state.lastTickId).toBe(1);
    expect(state.items['A1'].status).toBe('in_progress');
    expect(state.items['A1'].tps).toBe(9);
    expect(state.metrics.active_agents).toBe(1);

    // Out-of-order tick should be ignored
    store.getState().applyTick({ tick_id: 1, metrics: { live_tps: 5 } });
    expect(store.getState().metrics.live_tps).toBe(9);
  });
});

```

## File: `lib/store.ts`
```typescript
import { createStore } from 'zustand/vanilla';
import type { Agent, AppState, ProjectMetrics, WorkItem } from './types';
import { DEFAULT_SEED, RUNNING_DEFAULT } from './config';

type PartialWithId<T extends { id: string }> = Partial<T> & { id: string };

export interface UIState extends AppState {
  lastTickId: number;
  // Currently selected plan name (for UI display)
  plan_name?: string;
  // UI: whether radar ping sound is enabled
  pingAudioEnabled: boolean;
  // Reducers
  applySnapshot: (snapshot: AppState) => void;
  applyTick: (diff: {
    tick_id: number;
    items?: PartialWithId<WorkItem>[];
    agents?: PartialWithId<Agent>[];
    metrics?: Partial<ProjectMetrics>;
    agents_remove?: string[];
  }) => void;
  setPlanName: (name: string) => void;
  setPingAudioEnabled: (enabled: boolean) => void;
  togglePingAudio: () => void;
}

const emptyMetrics: ProjectMetrics = {
  active_agents: 0,
  total_tokens: 0,
  total_spend_usd: 0,
  live_tps: 0,
  live_spend_per_s: 0,
  completion_rate: 0,
};

export function createAppStore(initial?: Partial<AppState>) {
  return createStore<UIState>()((set, get) => ({
    items: initial?.items ?? {},
    agents: initial?.agents ?? {},
    metrics: initial?.metrics ?? emptyMetrics,
    seed: initial?.seed ?? DEFAULT_SEED,
    running: initial?.running ?? RUNNING_DEFAULT,
    lastTickId: 0,
    plan_name: initial && (initial as UIState).plan_name,
    pingAudioEnabled: false,

    applySnapshot(snapshot) {
      set({
        items: snapshot.items ?? {},
        agents: snapshot.agents ?? {},
        metrics: snapshot.metrics ?? emptyMetrics,
        seed: snapshot.seed,
        running: snapshot.running,
        lastTickId: 0, // reset ordering on fresh snapshot
      });
    },

    applyTick(diff) {
      if (diff.tick_id <= get().lastTickId) return; // ignore out-of-order

      set((state) => {
        // Clone maps shallowly before mutating
        const items = { ...state.items } as Record<string, WorkItem>;
        const agents = { ...state.agents } as Record<string, Agent>;

        if (diff.items) {
          for (const patch of diff.items) {
            const id = patch.id;
            const prev = items[id] ?? ({ id } as WorkItem);
            items[id] = { ...prev, ...patch } as WorkItem;
          }
        }

        if (diff.agents) {
          for (const patch of diff.agents) {
            const id = patch.id;
            const prev = agents[id] ?? ({ id } as Agent);
            agents[id] = { ...prev, ...patch } as Agent;
          }
        }

        if (diff.agents_remove && diff.agents_remove.length) {
          for (const id of diff.agents_remove) {
            if (id in agents) delete agents[id];
          }
        }

        const metrics = diff.metrics ? { ...state.metrics, ...diff.metrics } : state.metrics;

        return { items, agents, metrics, lastTickId: diff.tick_id };
      });
    },

    setPlanName(name: string) {
      set({ plan_name: name });
    },

    setPingAudioEnabled(enabled: boolean) {
      set({ pingAudioEnabled: !!enabled });
    },

    togglePingAudio() {
      const cur = get().pingAudioEnabled;
      set({ pingAudioEnabled: !cur });
    },
  }));
}

// App-level singleton store (UI can import this).
export const appStore = createAppStore();
```

## File: `lib/types.ts`
```typescript
// Core TypeScript types for the Calming Control Room

export type Status = 'queued' | 'assigned' | 'in_progress' | 'blocked' | 'done';

export interface WorkItem {
  id: string;            // e.g., "A1", "B3"
  group: string;         // 'A', 'B', ... (for grouping/legend)
  sector: string;        // e.g., 'Planning', 'Build', 'Eval', 'Deploy'
  depends_on: string[];  // list of WorkItem ids
  desc?: string;         // optional human-friendly work order description

  estimate_ms: number;   // target duration for this item (ms)
  started_at?: number;   // epoch ms when entered in_progress
  eta_ms?: number;       // rolling ETA in ms (recomputed)

  tps_min: number;       // tokens/sec lower bound for this item
  tps_max: number;       // tokens/sec upper bound
  tps: number;           // current tokens/sec (dynamic within [min,max])
  tokens_done: number;   // cumulative tokens produced for this item
  est_tokens: number;    // derived from estimate + nominal tps

  status: Status;
  agent_id?: string;     // set when in_progress
}

export interface Agent {
  id: string;            // e.g., 'P1','D2','E3','Q7','X584'
  work_item_id: string;  // current assignment
  // Radar motion state (normalized world coords in [-1,1])
  x: number;
  y: number;             // current position
  v: number;             // scalar speed (units/frame) mapped from tps
  curve_phase: number;   // 0..1 for bezier curvature evolution
}

export interface ProjectMetrics {
  active_agents: number;
  total_tokens: number;    // cumulative across all time
  total_spend_usd: number; // cumulative spend
  live_tps: number;        // sum of in_progress tps
  live_spend_per_s: number;
  completion_rate: number; // done / eligible (0..1)
}

export interface AppState {
  items: Record<string, WorkItem>;
  agents: Record<string, Agent>;
  metrics: ProjectMetrics;
  seed: string;
  running: boolean;
}

// Keep this flag export to satisfy existing stub import tests
export const TYPES_MODULE_LOADED = true;
```

## File: `lib/audio/tracks.ts`
```typescript
export type AudioSource =
  | { type: 'local'; src: string }
  | { type: 'youtube'; url: string };

export type Track = {
  id: string;
  title: string;
  source: AudioSource;
};

// Place your audio files under `public/audio/` and update the mapping below.
// Example local files are placeholders; replace with your own.
export const tracks: Track[] = [
  {
    id: 'work-music-for-serious-grind-stay-aligned',
    title: 'Work Music for Serious Grind | Stay Aligned',
    source: { type: 'youtube', url: 'https://www.youtube.com/watch?v=MYW0TgV67RE&list=RDMYW0TgV67RE&start_radio=1' },
  },
  {
    id: 'lofi-hip-hop-radio',
    title: 'lofi hip hop radio 📚 beats to relax/study to',
    source: { type: 'youtube', url: 'https://www.youtube.com/watch?v=jfKfPfyJRdk' },
  },
  {
    id: 'flight-facilities-clair-de-lune-feat-christine-hoberg',
    title: 'Flight Facilities - Clair De Lune feat. Christine Hoberg',
    source: { type: 'youtube', url: 'https://www.youtube.com/watch?v=Jcu1AHaTchM&list=RDJcu1AHaTchM&start_radio=1' },
  },
  {
    id: 'work-music-for-progress-trust-the-process',
    title: 'Work Music for Progress | Trust the Process',
    source: { type: 'youtube', url: 'https://www.youtube.com/watch?v=Efkc-AMB96c' },
  },
  {
    id: 'work-music-for-ambition-build-the-future',
    title: 'Work Music for Ambition | Build the Future',
    source: { type: 'youtube', url: 'https://www.youtube.com/watch?v=UgT24uQx7-I' },
  },
  {
    id: 'work-music-for-deep-hustle-quiet-but-relentless',
    title: 'Work Music for Deep Hustle | Quiet but Relentless',
    source: { type: 'youtube', url: 'https://www.youtube.com/watch?v=5O-Nmzhkz_4&t=11s' },
  },
  {
    id: 'work-music-for-momentum-let-the-flow-build',
    title: 'Work Music for Momentum | Let the Flow Build',
    source: { type: 'youtube', url: 'https://www.youtube.com/watch?v=rH0iZluJ2fY' },
  },
  {
    id: 'work-music-for-clear-focus-calm-and-clear',
    title: 'Work Music for Clear Focus | Calm and Clear',
    source: { type: 'youtube', url: 'https://www.youtube.com/watch?v=fAxCoB2VUlc' },
  },
  {
    id: 'work-music-for-deep-work-focus-with-progress',
    title: 'Work Music for Deep Work | Focus With Progress',
    source: { type: 'youtube', url: 'https://www.youtube.com/watch?v=WZt8hjTwP20' },
  },
  {
    id: 'flight-facilities-live-at-airfields-sydney-full-concert',
    title: 'Flight Facilities - Live At Airfields, Sydney (Full Concert)',
    source: { type: 'youtube', url: 'https://youtu.be/ts-6KyJUDWY?si=Ib_PS5sd9fwLpzTI' },
  },
];

export const radio: Track[] = [
  {
    id: 'sfo',
    title: 'SFO ATC',
    source: { type: 'youtube', url: 'https://www.youtube.com/watch?v=mOec9Fu3Jz0' },
  },
  {
    id: 'las-vegas',
    title: 'Las Vegas ATC',
    source: { type: 'youtube', url: 'https://www.youtube.com/watch?v=Z_iF0OHUuz8' },
  },
  {
    id: 'jfk',
    title: 'JFK ATC',
    source: { type: 'youtube', url: 'https://www.youtube.com/watch?v=xq_kuLD8T0A' },
  }
]
```

## File: `plans/calm.test.ts`
```typescript
import { describe, it, expect } from 'vitest';
import { calmPlan } from './calm';

describe('calm plan shape', () => {
  it('has 12 unique items and valid deps', () => {
    const ids = new Set(calmPlan.items.map(i => i.id));
    expect(ids.size).toBe(calmPlan.items.length);
    const idList = new Set(calmPlan.items.map(i => i.id));
    for (const item of calmPlan.items) {
      for (const dep of item.depends_on) {
        expect(idList.has(dep)).toBe(true);
      }
      expect(item.tps_min).toBeLessThan(item.tps_max);
      expect(item.estimate_ms).toBeGreaterThan(0);
    }
  });

  it('is acyclic', () => {
    const map = new Map<string, string[]>();
    calmPlan.items.forEach(i => map.set(i.id, i.depends_on));
    const seen = new Set<string>();
    const stack = new Set<string>();
    const visit = (id: string): boolean => {
      if (stack.has(id)) return false; // cycle
      if (seen.has(id)) return true;
      stack.add(id);
      for (const d of map.get(id) || []) if (!visit(d)) return false;
      stack.delete(id);
      seen.add(id);
      return true;
    };
    for (const id of map.keys()) {
      expect(visit(id)).toBe(true);
    }
  });
});

```

## File: `plans/edits.py`
```python
#!/usr/bin/env python3
"""
Randomize timing fields in a plan file.

Defaults:
- estimate_ms: 10,000–30,000
- tps_min:     40–80
- tps_max:     80–120

Usage:
  python3 randomize_plan_fields.py path/to/plan.ts
  python3 randomize_plan_fields.py plan.ts --seed 42         # reproducible
  python3 randomize_plan_fields.py plan.ts --dry-run         # preview to stdout
  python3 randomize_plan_fields.py plan.ts --no-backup       # skip .bak
  # Ranges are overrideable:
  python3 randomize_plan_fields.py plan.ts --ms 9000 32000 --tps-min 30 70 --tps-max 70 140
"""
import argparse, random, re, shutil, sys

KEYS = ("estimate_ms", "tps_min", "tps_max")

def replace_field(text: str, field: str, lo: int, hi: int):
    # Match: estimate_ms: 12345  OR  "estimate_ms": 12345
    pat = re.compile(rf'(?P<prefix>(?:"{field}"|\'{field}\'|{field})\s*:\s*)\d+')
    def repl(m):
        return f"{m.group('prefix')}{random.randint(lo, hi)}"
    return pat.subn(repl, text)

def main():
    ap = argparse.ArgumentParser(description="Randomize estimate_ms, tps_min, tps_max in a plan file.")
    ap.add_argument("path", help="Path to .ts/.json-like plan file")
    ap.add_argument("--ms", dest="ms", nargs=2, type=int, default=(10_000, 30_000),
                    metavar=("LOW", "HIGH"), help="Range for estimate_ms")
    ap.add_argument("--tps-min", dest="tpsmin", nargs=2, type=int, default=(40, 80),
                    metavar=("LOW", "HIGH"), help="Range for tps_min")
    ap.add_argument("--tps-max", dest="tpsmax", nargs=2, type=int, default=(80, 120),
                    metavar=("LOW", "HIGH"), help="Range for tps_max")
    ap.add_argument("--seed", type=int, help="PRNG seed for reproducible outputs")
    ap.add_argument("--dry-run", action="store_true", help="Print result to stdout (don’t write file)")
    ap.add_argument("--no-backup", action="store_true", help="Don’t create .bak backup before writing")
    args = ap.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    try:
        with open(args.path, "r", encoding="utf-8") as f:
            txt = f.read()
    except OSError as e:
        sys.exit(f"Error reading {args.path}: {e}")

    txt, c_ms   = replace_field(txt, "estimate_ms", args.ms[0],    args.ms[1])
    txt, c_min  = replace_field(txt, "tps_min",     args.tpsmin[0], args.tpsmin[1])
    txt, c_max  = replace_field(txt, "tps_max",     args.tpsmax[0], args.tpsmax[1])

    if args.dry_run:
        sys.stdout.write(txt)
        return

    if not args.no_backup:
        try:
            shutil.copy2(args.path, args.path + ".bak")
        except OSError as e:
            sys.exit(f"Error creating backup: {e}")

    try:
        with open(args.path, "w", encoding="utf-8") as f:
            f.write(txt)
    except OSError as e:
        sys.exit(f"Error writing {args.path}: {e}")

    print(f"Updated {args.path}  (estimate_ms:{c_ms}, tps_min:{c_min}, tps_max:{c_max})")

if __name__ == "__main__":
    main()
```

## File: `plans/frantic.ts`
```typescript
import type { PlanDefinition } from './types';

// FRANTIC: A swarm of agents hit the fab at once—ASML + TSMC + NVIDIA joint push for +12.8% OEE.
// Early phase: no deps, maximal parallelism. Later: fan‑in, tighter coupling, and pile‑on.
export const franticPlan: PlanDefinition = {
  name: 'Frantic',
  description:
    'Hectic, all‑at‑once optimization sprint across ASML lithography cells and the TSMC line, with NVIDIA co‑optimization. Objective: +12.8% end‑to‑end efficiency (OEE) without yield regressions.',
  groups: [
    { id: 'P', title: 'Frantic Launch — Parallel Scouts & Knobs', description: 'Spin up dozens of agents immediately. No dependencies. Find knobs, bottlenecks, and quick wins.' },
    { id: 'B', title: 'Litho Line & Process Modules', description: 'Upgrade EUV/DUV stages, materials, and flows. Converge to stable recipes.' },
    { id: 'E', title: 'Metrology, Yield, Reliability', description: 'Measure everything: overlay, CDU, stochastic defects, parametrics. Lock in gains.' },
    { id: 'D', title: 'Rollout & Volume Ramp', description: 'Gate the changes, scale to multiple lines, hold the +12.8% under real load.' },
  ],
  items: [
    // -----------------------------
    // P — FRANTIC PARALLEL (no deps)
    // -----------------------------
    { id: 'P01', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'Map OEE tree: availability, performance, quality. Flag top 20 micro‑losses.' },
    { id: 'P02', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 18000, tps_min: 30, tps_max: 90, work_desc: 'EUV dose stability scout: source power drift & fast feedback hooks.' },
    { id: 'P03', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 22000, tps_min: 30, tps_max: 90, work_desc: 'Track time‑in‑state by tool; extract idle, warmup, recipe changeover.' },
    { id: 'P04', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 17000, tps_min: 30, tps_max: 90, work_desc: 'FOUP logistics blitz: AGV routing, queue discipline, buffer sizing.' },
    { id: 'P05', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 21000, tps_min: 30, tps_max: 90, work_desc: 'Mask shop handshake: write slots, blank quality, pellicle lead times.' },
    { id: 'P06', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 16000, tps_min: 30, tps_max: 90, work_desc: 'OPC/ILT compute surge: cluster sizing; job packing; cache strategy.' },
    { id: 'P07', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'Reticle contamination watch: clean intervals vs. throughput hit.' },
    { id: 'P08', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 19000, tps_min: 30, tps_max: 90, work_desc: 'Stage vibration survey: floor spectra, tool isolators, acoustic cross‑talk.' },
    { id: 'P09', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 24000, tps_min: 30, tps_max: 90, work_desc: 'Resist supply & track uptime: bake plate MTBF, coat/develop takt.' },
    { id: 'P10', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'Scrap pareto: stochastic defects, scumming, particles, overlay outliers.' },
    { id: 'P11', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 18000, tps_min: 30, tps_max: 90, work_desc: 'Recipe changeover tax: lens conditioning and reticle swaps.' },
    { id: 'P12', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 23000, tps_min: 30, tps_max: 90, work_desc: 'Inline metrology latency: sampling plan vs. queue time penalty.' },
    { id: 'P13', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 17000, tps_min: 30, tps_max: 90, work_desc: 'Pellicle transmittance audit; thermal bow risk at high EUV dose.' },
    { id: 'P14', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 21000, tps_min: 30, tps_max: 90, work_desc: 'Lens contamination model: outgassing sources and clean triggers.' },
    { id: 'P15', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 22000, tps_min: 30, tps_max: 90, work_desc: 'TSMC line balance scan: bottleneck hop between litho and etch.' },
    { id: 'P16', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 16000, tps_min: 30, tps_max: 90, work_desc: 'NVIDIA DFM rule refresh: hotspot library & acceptable waivers.' },
    { id: 'P17', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 19000, tps_min: 30, tps_max: 90, work_desc: 'Scribe‑line monitor plan: add overlay & CD sentinels early.' },
    { id: 'P18', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'WIP cap policy variants: Little’s Law sanity across tools.' },
    { id: 'P19', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 18000, tps_min: 30, tps_max: 90, work_desc: 'Reticle heating model: dose vs. pattern density vs. overlay drift.' },
    { id: 'P20', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 21000, tps_min: 30, tps_max: 90, work_desc: 'EUV source warm‑start script to shave morning loss minutes.' },
    { id: 'P21', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 24000, tps_min: 30, tps_max: 90, work_desc: 'Tool matching target: overlay & CDU deltas normalized across twins.' },
    { id: 'P22', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 17000, tps_min: 30, tps_max: 90, work_desc: 'Chamber particle audit: purge rates, door cycles, FOUP seals.' },
    { id: 'P23', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 16000, tps_min: 30, tps_max: 90, work_desc: 'Operator motion study: micro‑delays during reticle swaps.' },
    { id: 'P24', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 19000, tps_min: 30, tps_max: 90, work_desc: 'Downtime taxonomy cleanup: better codes → better actions.' },
    { id: 'P25', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'Photoresist bake optimization: plate temp uniformity scan.' },
    { id: 'P26', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 15000, tps_min: 30, tps_max: 90, work_desc: 'Developer nozzle calibration; rinse sequence variants.' },
    { id: 'P27', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 22000, tps_min: 30, tps_max: 90, work_desc: 'Track‑to‑scanner handshake latencies; handshake retries.' },
    { id: 'P28', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 18000, tps_min: 30, tps_max: 90, work_desc: 'Reticle carrier health check; latch sensors; foam wear.' },
    { id: 'P29', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 21000, tps_min: 30, tps_max: 90, work_desc: 'Overlay feedback loop mapping: controller gains by product.' },
    { id: 'P30', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 23000, tps_min: 30, tps_max: 90, work_desc: 'Pellicle frame warp survey; clamp torque standards.' },
    { id: 'P31', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 16000, tps_min: 30, tps_max: 90, work_desc: 'Mask blank inspection slots; defect spec alignment with OPC.' },
    { id: 'P32', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 24000, tps_min: 30, tps_max: 90, work_desc: 'Throughput model v0: takt by layer; Monte Carlo day plan.' },
    { id: 'P33', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 17000, tps_min: 30, tps_max: 90, work_desc: 'EUV collector reflectivity watch; clean/no‑clean decision rules.' },
    { id: 'P34', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'NVIDIA co‑design channel: ECO queue, hotspot reproducer kits.' },
    { id: 'P35', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 19000, tps_min: 30, tps_max: 90, work_desc: 'Quality firewall: fast binning to quarantine suspect lots.' },

    // -----------------------------
    // B — MODULE UPGRADES (early B items still parallel, then pile‑on)
    // -----------------------------
    { id: 'B01', group: 'B', sector: 'BUILD', depends_on: [], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'Dose control retune: faster PID; guardrail limits.' },
    { id: 'B02', group: 'B', sector: 'BUILD', depends_on: [], estimate_ms: 16000, tps_min: 30, tps_max: 90, work_desc: 'Stage feed‑forward: mark‑to‑mark predictive overlay nudge.' },
    { id: 'B03', group: 'B', sector: 'BUILD', depends_on: [], estimate_ms: 18000, tps_min: 30, tps_max: 90, work_desc: 'Auto‑reticle‑clamp verification and torque logging.' },
    { id: 'B04', group: 'B', sector: 'BUILD', depends_on: [], estimate_ms: 22000, tps_min: 30, tps_max: 90, work_desc: 'Pellicle heater profile to limit bow under high dose.' },
    { id: 'B05', group: 'B', sector: 'BUILD', depends_on: [], estimate_ms: 21000, tps_min: 30, tps_max: 90, work_desc: 'Track recipe presets for rapid product switching.' },
    { id: 'B06', group: 'B', sector: 'BUILD', depends_on: [], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'OPC cache warmups for recurring masks; hash‑based reuse.' },
    { id: 'B07', group: 'B', sector: 'BUILD', depends_on: [], estimate_ms: 17000, tps_min: 30, tps_max: 90, work_desc: 'EUV source warm‑start automation (from P20) hardened.' },
    { id: 'B08', group: 'B', sector: 'BUILD', depends_on: [], estimate_ms: 19000, tps_min: 30, tps_max: 90, work_desc: 'Resist prime nozzle quick‑check; self‑cal scheduler.' },
    { id: 'B09', group: 'B', sector: 'BUILD', depends_on: [], estimate_ms: 23000, tps_min: 30, tps_max: 90, work_desc: 'AGV dispatch rules: short‑cycle boost without starvation.' },
    { id: 'B10', group: 'B', sector: 'BUILD', depends_on: [], estimate_ms: 15000, tps_min: 30, tps_max: 90, work_desc: 'Lens purge routine timings to cut changeover deadtime.' },

    // pile‑on begins — link back to P‑findings
    { id: 'B11', group: 'B', sector: 'BUILD', depends_on: ['P06'], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'OPC/ILT scheduling: preemption policy for critical layers.' },
    { id: 'B12', group: 'B', sector: 'BUILD', depends_on: ['P29'], estimate_ms: 18000, tps_min: 30, tps_max: 90, work_desc: 'Overlay controller gain sweep per product family.' },
    { id: 'B13', group: 'B', sector: 'BUILD', depends_on: ['P21', 'B12'], estimate_ms: 21000, tps_min: 30, tps_max: 90, work_desc: 'Tool matching pass: align twins to golden overlay/CDU.' },
    { id: 'B14', group: 'B', sector: 'BUILD', depends_on: ['P14'], estimate_ms: 22000, tps_min: 30, tps_max: 90, work_desc: 'Lens contam mitigation kit: new purge & bake sequences.' },
    { id: 'B15', group: 'B', sector: 'BUILD', depends_on: ['P25', 'P26'], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'Track temp uniformity fix; cure bake drift.' },
    { id: 'B16', group: 'B', sector: 'BUILD', depends_on: ['P31'], estimate_ms: 16000, tps_min: 30, tps_max: 90, work_desc: 'Mask blank spec check integration before OPC launch.' },
    { id: 'B17', group: 'B', sector: 'BUILD', depends_on: ['P07', 'B03'], estimate_ms: 19000, tps_min: 30, tps_max: 90, work_desc: 'Reticle clean cadence auto‑planner.' },
    { id: 'B18', group: 'B', sector: 'BUILD', depends_on: ['P08'], estimate_ms: 18000, tps_min: 30, tps_max: 90, work_desc: 'Under‑tool acoustic damping panels.' },
    { id: 'B19', group: 'B', sector: 'BUILD', depends_on: ['P27'], estimate_ms: 24000, tps_min: 30, tps_max: 90, work_desc: 'Track‑scanner handshake retry backoff tuning.' },
    { id: 'B20', group: 'B', sector: 'BUILD', depends_on: ['P18', 'P32'], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'WIP caps per cell; throughput optimizer online.' },
    { id: 'B21', group: 'B', sector: 'BUILD', depends_on: ['P33'], estimate_ms: 17000, tps_min: 30, tps_max: 90, work_desc: 'Collector clean decision engine (reflectivity trending).' },
    { id: 'B22', group: 'B', sector: 'BUILD', depends_on: ['P30'], estimate_ms: 21000, tps_min: 30, tps_max: 90, work_desc: 'Pellicle clamp torque SOP & sensorized wrench rollout.' },
    { id: 'B23', group: 'B', sector: 'BUILD', depends_on: ['P22'], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'Door cycle purge & FOUP seal refresh kit.' },
    { id: 'B24', group: 'B', sector: 'BUILD', depends_on: ['P15', 'B20'], estimate_ms: 22000, tps_min: 30, tps_max: 90, work_desc: 'Line rebalance: relieve etch wait after litho speedups.' },
    { id: 'B25', group: 'B', sector: 'BUILD', depends_on: ['P17'], estimate_ms: 16000, tps_min: 30, tps_max: 90, work_desc: 'Scribe‑line monitor masks—spin into next lots.' },
    { id: 'B26', group: 'B', sector: 'BUILD', depends_on: ['P10'], estimate_ms: 18000, tps_min: 30, tps_max: 90, work_desc: 'Stochastic defect guardband tweak; resist/filter updates.' },
    { id: 'B27', group: 'B', sector: 'BUILD', depends_on: ['P34'], estimate_ms: 23000, tps_min: 30, tps_max: 90, work_desc: 'NVIDIA hotspot repro kits shipped to litho cells.' },
    { id: 'B28', group: 'B', sector: 'BUILD', depends_on: ['B21', 'B14'], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'EUV uptime kit install window (collector + purge).' },
    { id: 'B29', group: 'B', sector: 'BUILD', depends_on: ['P12'], estimate_ms: 15000, tps_min: 30, tps_max: 90, work_desc: 'Inline metrology fast path; sampling plan v2.' },
    { id: 'B30', group: 'B', sector: 'BUILD', depends_on: ['P24'], estimate_ms: 16000, tps_min: 30, tps_max: 90, work_desc: 'Downtime code UI revamp; single‑click root cause.' },
    { id: 'B31', group: 'B', sector: 'BUILD', depends_on: ['P23'], estimate_ms: 17000, tps_min: 30, tps_max: 90, work_desc: 'Reticle swap kitting: pre‑staged tools & carriers.' },
    { id: 'B32', group: 'B', sector: 'BUILD', depends_on: ['P28'], estimate_ms: 18000, tps_min: 30, tps_max: 90, work_desc: 'Carrier latch sensor replacement & predictive alerts.' },
    { id: 'B33', group: 'B', sector: 'BUILD', depends_on: ['P02', 'B01'], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'Dose drift auto‑correct per wafer map.' },
    { id: 'B34', group: 'B', sector: 'BUILD', depends_on: ['P19', 'B12'], estimate_ms: 22000, tps_min: 30, tps_max: 90, work_desc: 'Reticle heating compensation in overlay model.' },
    { id: 'B35', group: 'B', sector: 'BUILD', depends_on: ['P05', 'P31'], estimate_ms: 21000, tps_min: 30, tps_max: 90, work_desc: 'Mask shop SLA tweak & auto‑paging for write slot slips.' },
    { id: 'B36', group: 'B', sector: 'BUILD', depends_on: ['B20', 'B24'], estimate_ms: 19000, tps_min: 30, tps_max: 90, work_desc: 'Takt re‑calc after rebalance; redistribute FOUP buffers.' },
    { id: 'B37', group: 'B', sector: 'BUILD', depends_on: ['B06'], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'OPC artifact cache eviction policy tuned for hit‑rate.' },
    { id: 'B38', group: 'B', sector: 'BUILD', depends_on: ['B05', 'P11'], estimate_ms: 16000, tps_min: 30, tps_max: 90, work_desc: 'Changeover recipe packer: minimal lens conditioning.' },
    { id: 'B39', group: 'B', sector: 'BUILD', depends_on: ['B13'], estimate_ms: 23000, tps_min: 30, tps_max: 90, work_desc: 'Golden‑tool ghosting: push matching params to twins.' },
    { id: 'B40', group: 'B', sector: 'BUILD', depends_on: ['B33', 'B29'], estimate_ms: 18000, tps_min: 30, tps_max: 90, work_desc: 'Closed‑loop CDU + dose trim by layer.' },

    // -----------------------------
    // E — METROLOGY / YIELD / RELIABILITY (fan‑in on B)
    // -----------------------------
    { id: 'E01', group: 'E', sector: 'EVAL', depends_on: ['B12', 'B13'], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'Overlay nm regression across tools; post‑matching check.' },
    { id: 'E02', group: 'E', sector: 'EVAL', depends_on: ['B40'], estimate_ms: 18000, tps_min: 30, tps_max: 90, work_desc: 'CDU maps before/after dose trim; guardband impact.' },
    { id: 'E03', group: 'E', sector: 'EVAL', depends_on: ['B26'], estimate_ms: 21000, tps_min: 30, tps_max: 90, work_desc: 'Stochastic defect rate trend; wafer‑level heatmaps.' },
    { id: 'E04', group: 'E', sector: 'EVAL', depends_on: ['B14', 'B21'], estimate_ms: 17000, tps_min: 30, tps_max: 90, work_desc: 'Uptime delta from contam mitigations; MTBF delta.' },
    { id: 'E05', group: 'E', sector: 'EVAL', depends_on: ['B28'], estimate_ms: 22000, tps_min: 30, tps_max: 90, work_desc: 'Collector clean windows vs. OEE; find sweet spot.' },
    { id: 'E06', group: 'E', sector: 'EVAL', depends_on: ['B22'], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'Pellicle clamp torque → overlay drift study.' },
    { id: 'E07', group: 'E', sector: 'EVAL', depends_on: ['B37'], estimate_ms: 24000, tps_min: 30, tps_max: 90, work_desc: 'OPC cache hit‑rate vs. mask turn time & compute cost.' },
    { id: 'E08', group: 'E', sector: 'EVAL', depends_on: ['B36'], estimate_ms: 16000, tps_min: 30, tps_max: 90, work_desc: 'Line balance validation: no new downstream starvation.' },
    { id: 'E09', group: 'E', sector: 'EVAL', depends_on: ['B20'], estimate_ms: 19000, tps_min: 30, tps_max: 90, work_desc: 'WIP cap A/B outcomes: cycle‑time vs. throughput.' },
    { id: 'E10', group: 'E', sector: 'EVAL', depends_on: ['B33'], estimate_ms: 21000, tps_min: 30, tps_max: 90, work_desc: 'Dose auto‑correct stability vs. noise injection.' },
    { id: 'E11', group: 'E', sector: 'EVAL', depends_on: ['B29'], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'Metrology latency cut: feedback timeliness to litho.' },
    { id: 'E12', group: 'E', sector: 'EVAL', depends_on: ['B24'], estimate_ms: 17000, tps_min: 30, tps_max: 90, work_desc: 'Fab‑wide takt audit post‑rebalance.' },
    { id: 'E13', group: 'E', sector: 'EVAL', depends_on: ['B31'], estimate_ms: 19000, tps_min: 30, tps_max: 90, work_desc: 'Reticle swap time variance reduction check.' },
    { id: 'E14', group: 'E', sector: 'EVAL', depends_on: ['B19'], estimate_ms: 16000, tps_min: 30, tps_max: 90, work_desc: 'Handshake retry incidence; wafer delay histogram shift.' },
    { id: 'E15', group: 'E', sector: 'EVAL', depends_on: ['B18'], estimate_ms: 18000, tps_min: 30, tps_max: 90, work_desc: 'Vibration spectral change → overlay & CDU correlation.' },
    { id: 'E16', group: 'E', sector: 'EVAL', depends_on: ['B05', 'B38'], estimate_ms: 23000, tps_min: 30, tps_max: 90, work_desc: 'Changeover overhead drop measured across product mix.' },
    { id: 'E17', group: 'E', sector: 'EVAL', depends_on: ['B25'], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'New scribe‑line monitors sensitivity/false positive rate.' },
    { id: 'E18', group: 'E', sector: 'EVAL', depends_on: ['B35'], estimate_ms: 22000, tps_min: 30, tps_max: 90, work_desc: 'Mask SLA → litho wait time impact; days‑to‑recover.' },
    { id: 'E19', group: 'E', sector: 'EVAL', depends_on: ['B23'], estimate_ms: 15000, tps_min: 30, tps_max: 90, work_desc: 'Particle excursion rate before/after FOUP seal refresh.' },
    { id: 'E20', group: 'E', sector: 'EVAL', depends_on: ['B39'], estimate_ms: 21000, tps_min: 30, tps_max: 90, work_desc: 'Ghosting efficacy: twin drift after push.' },
    { id: 'E21', group: 'E', sector: 'EVAL', depends_on: ['B10'], estimate_ms: 19000, tps_min: 30, tps_max: 90, work_desc: 'Changeover deadtime cut quantified.' },
    { id: 'E22', group: 'E', sector: 'EVAL', depends_on: ['B01', 'B33'], estimate_ms: 18000, tps_min: 30, tps_max: 90, work_desc: 'Dose stability → CDU & yield uplift curve.' },
    { id: 'E23', group: 'E', sector: 'EVAL', depends_on: ['B07'], estimate_ms: 17000, tps_min: 30, tps_max: 90, work_desc: 'Warm‑start success rate; morning startup minutes saved.' },
    { id: 'E24', group: 'E', sector: 'EVAL', depends_on: ['B22', 'B34'], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'Pellicle torque + heating compensation residuals.' },
    { id: 'E25', group: 'E', sector: 'EVAL', depends_on: ['B04'], estimate_ms: 16000, tps_min: 30, tps_max: 90, work_desc: 'Bow under dose test; transmittance change vs. time.' },
    { id: 'E26', group: 'E', sector: 'EVAL', depends_on: ['B08', 'B15'], estimate_ms: 21000, tps_min: 30, tps_max: 90, work_desc: 'Track stability & defectivity metrics post tune.' },
    { id: 'E27', group: 'E', sector: 'EVAL', depends_on: ['B20', 'B36'], estimate_ms: 24000, tps_min: 30, tps_max: 90, work_desc: 'Fab‑level OEE recompute—target +12.8% proof.' },
    { id: 'E28', group: 'E', sector: 'EVAL', depends_on: ['B30'], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'Root‑cause tagging completeness & actionability audit.' },
    { id: 'E29', group: 'E', sector: 'EVAL', depends_on: ['B27'], estimate_ms: 18000, tps_min: 30, tps_max: 90, work_desc: 'NVIDIA hotspot closure stats; ECO loop time.' },
    { id: 'E30', group: 'E', sector: 'EVAL', depends_on: ['B24', 'B36'], estimate_ms: 17000, tps_min: 30, tps_max: 90, work_desc: 'Downstream (etch/met) wait time regression check.' },

    // -----------------------------
    // D — ROLLOUT / VOLUME RAMP
    // -----------------------------
    { id: 'D01', group: 'D', sector: 'DEPLOY', depends_on: ['E27'], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'Go/No‑Go gate for fab‑wide rollout (+12.8% confirmed).' },
    { id: 'D02', group: 'D', sector: 'DEPLOY', depends_on: ['E01', 'E02'], estimate_ms: 18000, tps_min: 30, tps_max: 90, work_desc: 'Overlay/CDU control plan baselined per product.' },
    { id: 'D03', group: 'D', sector: 'DEPLOY', depends_on: ['E11', 'E28'], estimate_ms: 22000, tps_min: 30, tps_max: 90, work_desc: 'New downtime codes + dashboards to ops.' },
    { id: 'D04', group: 'D', sector: 'DEPLOY', depends_on: ['E23'], estimate_ms: 17000, tps_min: 30, tps_max: 90, work_desc: 'Morning warm‑start SOP push; training completed.' },
    { id: 'D05', group: 'D', sector: 'DEPLOY', depends_on: ['E05', 'E24'], estimate_ms: 21000, tps_min: 30, tps_max: 90, work_desc: 'Collector & pellicle maintenance windows codified.' },
    { id: 'D06', group: 'D', sector: 'DEPLOY', depends_on: ['E09', 'E12'], estimate_ms: 19000, tps_min: 30, tps_max: 90, work_desc: 'WIP cap & line balance policies live in scheduler.' },
    { id: 'D07', group: 'D', sector: 'DEPLOY', depends_on: ['E03', 'E26'], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'Defectivity guardbands updated; release notes to QA.' },
    { id: 'D08', group: 'D', sector: 'DEPLOY', depends_on: ['E29'], estimate_ms: 15000, tps_min: 30, tps_max: 90, work_desc: 'NVIDIA ECO fast lane formalized; artifact kits versioned.' },
    { id: 'D09', group: 'D', sector: 'DEPLOY', depends_on: ['E06'], estimate_ms: 16000, tps_min: 30, tps_max: 90, work_desc: 'Pellicle torque tools & logging issued to all shifts.' },
    { id: 'D10', group: 'D', sector: 'DEPLOY', depends_on: ['E14'], estimate_ms: 18000, tps_min: 30, tps_max: 90, work_desc: 'Handshake retry alarm thresholds tuned in MES.' },
    { id: 'D11', group: 'D', sector: 'DEPLOY', depends_on: ['E08'], estimate_ms: 23000, tps_min: 30, tps_max: 90, work_desc: 'Downstream readiness checklists to avoid moving bottlenecks.' },
    { id: 'D12', group: 'D', sector: 'DEPLOY', depends_on: ['E20'], estimate_ms: 21000, tps_min: 30, tps_max: 90, work_desc: 'Golden‑tool push cadence & audit trail.' },
    { id: 'D13', group: 'D', sector: 'DEPLOY', depends_on: ['E27'], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'Public KPI: OEE delta and yield neutrality published internally.' },
    { id: 'D14', group: 'D', sector: 'DEPLOY', depends_on: ['E15'], estimate_ms: 19000, tps_min: 30, tps_max: 90, work_desc: 'Acoustic/vibration mitigations standardized in facility SOP.' },
    { id: 'D15', group: 'D', sector: 'DEPLOY', depends_on: ['E18'], estimate_ms: 24000, tps_min: 30, tps_max: 90, work_desc: 'Mask SLA contract updates; paging & penalties enabled.' },
    { id: 'D16', group: 'D', sector: 'DEPLOY', depends_on: ['E21'], estimate_ms: 17000, tps_min: 30, tps_max: 90, work_desc: 'Changeover playbook laminated at toolside.' },
    { id: 'D17', group: 'D', sector: 'DEPLOY', depends_on: ['E19'], estimate_ms: 16000, tps_min: 30, tps_max: 90, work_desc: 'FOUP seal spare kits stocked; PM calendar set.' },
    { id: 'D18', group: 'D', sector: 'DEPLOY', depends_on: ['E25'], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'Pellicle heating watchpoints integrated into shift checks.' },
    { id: 'D19', group: 'D', sector: 'DEPLOY', depends_on: ['E30', 'E12'], estimate_ms: 22000, tps_min: 30, tps_max: 90, work_desc: 'Cross‑module drumbeat: hold no new queues downstream.' },
    { id: 'D20', group: 'D', sector: 'DEPLOY', depends_on: ['D01', 'D11', 'D19'], estimate_ms: 20000, tps_min: 30, tps_max: 90, work_desc: 'Multi‑line rollout; sustain +12.8% for 30 days; lock and handoff.' },
  ],
};

export default franticPlan;
```

## File: `plans/humanoid.ts`
```typescript
import type { PlanDefinition } from './types';

// Humanoid plan: more items, more parallelism, higher tps variance
export const humanoidPlan: PlanDefinition = {
  name: 'Humanoid',
  description: 'Building a humanoid rock-hauling robot. Get the robot to the top of the mountain and back.',
  groups: [
    {
      id: 'P',
      title: 'Mission Planning',
      description: 'Define mission goals, constraints, terrain routes, budget, and safety architecture for the ascent.',
    },
    {
      id: 'B',
      title: 'Mechanical & Power Build',
      description: 'Exoskeleton fabrication, actuation, power systems, and sensors required to haul rocks uphill.',
    },
    {
      id: 'E',
      title: 'Evaluation & Field Tests',
      description: 'Bench and field validation, calibration, and timed haul cycles under load.',
    },
    {
      id: 'D',
      title: 'Deployment & Operations',
      description: 'Productionization, staging at the mountain base, and operational readiness for repeated hauls.',
    },
  ],
  items: [
    // -----------------------------
    // Planning
    // -----------------------------
    { id: 'PA1', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 17653, tps_min: 54, tps_max: 93, work_desc: 'Define mission goals and safety constraints for rock-hauling humanoid.' },
    { id: 'PA2', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 21949, tps_min: 47, tps_max: 105, work_desc: 'Draft system architecture: gait plan, payload target, torque budget.' },
    { id: 'PB1', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 21030, tps_min: 56, tps_max: 118, work_desc: 'Analyze mountain terrain; compile routes and incline profiles dataset.' },

    { id: 'PA3', group: 'P', sector: 'PLANNING', depends_on: ['PA1'], estimate_ms: 27475, tps_min: 64, tps_max: 96, work_desc: 'Build risk register: avalanche, rockfall, battery thermal runaway.' },
    { id: 'PA4', group: 'P', sector: 'PLANNING', depends_on: ['PA1'], estimate_ms: 19034, tps_min: 70, tps_max: 113, work_desc: 'Define success metrics & telemetry KPIs (time-to-summit, Wh/m, fault rate).' },
    { id: 'PA5', group: 'P', sector: 'PLANNING', depends_on: ['PB1'], estimate_ms: 17207, tps_min: 64, tps_max: 110, work_desc: 'Permits & land access: coordinate with park rangers and trail stewards.' },
    { id: 'PB2', group: 'P', sector: 'PLANNING', depends_on: ['PB1'], estimate_ms: 23239, tps_min: 41, tps_max: 109, work_desc: 'Create synthetic rock-shape/weight dataset via photogrammetry.' },
    { id: 'PB3', group: 'P', sector: 'PLANNING', depends_on: ['PA2'], estimate_ms: 22745, tps_min: 62, tps_max: 102, work_desc: 'BOM & budget; flag long-lead items and alternates.' },
    { id: 'PC1', group: 'P', sector: 'PLANNING', depends_on: ['PA1'], estimate_ms: 27284, tps_min: 40, tps_max: 83, work_desc: 'Define HRI & E‑stop protocols; operator roles and comms.' },
    { id: 'PC2', group: 'P', sector: 'PLANNING', depends_on: ['PA2'], estimate_ms: 23934, tps_min: 41, tps_max: 112, work_desc: 'Gait and terrain sim parameter sweep plan.' },
    { id: 'PD1', group: 'P', sector: 'PLANNING', depends_on: ['PA1'], estimate_ms: 18658, tps_min: 45, tps_max: 82, work_desc: 'Comms plan: base-camp radio net + LTE fallback.' },
    { id: 'PD2', group: 'P', sector: 'PLANNING', depends_on: ['PA2'], estimate_ms: 24768, tps_min: 63, tps_max: 106, work_desc: 'Cold‑weather ops plan: battery warmers, low-temp grease, seal choices.' },
    { id: 'PE1', group: 'P', sector: 'PLANNING', depends_on: ['PC1'], estimate_ms: 28811, tps_min: 53, tps_max: 106, work_desc: 'Operator training script & safety drills.' },
    { id: 'PE2', group: 'P', sector: 'PLANNING', depends_on: ['PA2', 'PB1'], estimate_ms: 20655, tps_min: 67, tps_max: 108, work_desc: 'Test matrix: ascent/descent scenarios and acceptance gates.' },
    { id: 'PF1', group: 'P', sector: 'PLANNING', depends_on: ['PB3'], estimate_ms: 24040, tps_min: 74, tps_max: 97, work_desc: 'Spare parts & field kit list with quantities.' },
    { id: 'PF2', group: 'P', sector: 'PLANNING', depends_on: ['PD1'], estimate_ms: 17851, tps_min: 61, tps_max: 82, work_desc: 'Narrative beats for docu-log; media checklist (for fun).' },

    // -----------------------------
    // Build branches
    // -----------------------------
    { id: 'BA1', group: 'B', sector: 'BUILD', depends_on: ['PA1'], estimate_ms: 26318, tps_min: 46, tps_max: 118, work_desc: 'Fabricate exoskeleton frame; assemble hip/shoulder joint modules.' },
    { id: 'BA2', group: 'B', sector: 'BUILD', depends_on: ['BA1'], estimate_ms: 20017, tps_min: 60, tps_max: 106, work_desc: 'Install actuators and motor drivers; verify stall torque on rig.' },
    { id: 'BB1', group: 'B', sector: 'BUILD', depends_on: ['PB1'], estimate_ms: 26913, tps_min: 60, tps_max: 83, work_desc: 'Prototype power pack and thermal spreaders for high-load climbs.' },
    { id: 'BB2', group: 'B', sector: 'BUILD', depends_on: ['BB1'], estimate_ms: 20458, tps_min: 57, tps_max: 86, work_desc: 'Implement power management firmware and brownout protections.' },
    { id: 'BC1', group: 'B', sector: 'BUILD', depends_on: ['PA2'], estimate_ms: 13732, tps_min: 52, tps_max: 84, work_desc: 'Integrate IMU, LiDAR, and foot force sensors; wire harness.' },

    { id: 'BA3', group: 'B', sector: 'BUILD', depends_on: ['PA2'], estimate_ms: 24002, tps_min: 72, tps_max: 100, work_desc: 'Design gripper and basket clamp for irregular rock shapes.' },
    { id: 'BA4', group: 'B', sector: 'BUILD', depends_on: ['BA1'], estimate_ms: 28106, tps_min: 68, tps_max: 81, work_desc: 'Assemble knee/ankle spring‑dampers; select bushings.' },
    { id: 'BA5', group: 'B', sector: 'BUILD', depends_on: ['BA1'], estimate_ms: 29462, tps_min: 46, tps_max: 88, work_desc: 'Carbon shrouds & seal kit for dust/water ingress.' },
    { id: 'BB3', group: 'B', sector: 'BUILD', depends_on: ['BB1'], estimate_ms: 28442, tps_min: 66, tps_max: 115, work_desc: 'Battery pack rev‑B; cold‑soak performance upgrades.' },
    { id: 'BB4', group: 'B', sector: 'BUILD', depends_on: ['BB1'], estimate_ms: 10395, tps_min: 64, tps_max: 102, work_desc: 'Integrate MPPT charger with foldable solar mats (field topping).' },
    { id: 'BC2', group: 'B', sector: 'BUILD', depends_on: ['BC1'], estimate_ms: 18294, tps_min: 68, tps_max: 118, work_desc: 'EMI shielding/grounding; cable routing & strain relief.' },
    { id: 'BC3', group: 'B', sector: 'BUILD', depends_on: ['BC1'], estimate_ms: 20711, tps_min: 73, tps_max: 86, work_desc: 'Toe force sensors redundant path; analog fallback.' },
    { id: 'BD1', group: 'B', sector: 'BUILD', depends_on: ['BA1'], estimate_ms: 14329, tps_min: 74, tps_max: 119, work_desc: 'Footpad design: cleat vs microspike; quick‑change soles.' },
    { id: 'BD2', group: 'B', sector: 'BUILD', depends_on: ['BA2'], estimate_ms: 21290, tps_min: 72, tps_max: 117, work_desc: 'Winch assist module for 45°+ pitches.' },
    { id: 'BE1', group: 'B', sector: 'BUILD', depends_on: ['BA2', 'BB2'], estimate_ms: 24071, tps_min: 40, tps_max: 117, work_desc: 'Thermal management: heatpipes & ducting around drivers.' },
    { id: 'BE2', group: 'B', sector: 'BUILD', depends_on: ['BC2'], estimate_ms: 25920, tps_min: 43, tps_max: 120, work_desc: 'Conformal coating & potting for electronics.' },
    { id: 'BF1', group: 'B', sector: 'BUILD', depends_on: ['PA2'], estimate_ms: 14601, tps_min: 59, tps_max: 80, work_desc: 'Gait controller v1 (ZMP/SLIP hybrid) with torque limits.' },
    { id: 'BF2', group: 'B', sector: 'BUILD', depends_on: ['BC1'], estimate_ms: 21318, tps_min: 75, tps_max: 85, work_desc: 'Sensor fusion & foot slip estimator (Kalman).' },
    { id: 'BG1', group: 'B', sector: 'BUILD', depends_on: ['BF1'], estimate_ms: 26241, tps_min: 80, tps_max: 120, work_desc: 'Fall detection + safe‑kneel routine.' },
    { id: 'BG2', group: 'B', sector: 'BUILD', depends_on: ['BA3'], estimate_ms: 16792, tps_min: 72, tps_max: 101, work_desc: 'Rock grasp strategy library (pinch, cradle, lash).' },
    { id: 'BH1', group: 'B', sector: 'BUILD', depends_on: ['PB2', 'BC1'], estimate_ms: 18737, tps_min: 79, tps_max: 104, work_desc: 'Vision terrain classifier (scree/slab/talus).' },
    { id: 'BH2', group: 'B', sector: 'BUILD', depends_on: ['BC1'], estimate_ms: 22608, tps_min: 49, tps_max: 100, work_desc: 'LiDAR snow/ice reflectance compensation.' },
    { id: 'BI1', group: 'B', sector: 'BUILD', depends_on: ['PD1', 'BC1'], estimate_ms: 27082, tps_min: 79, tps_max: 84, work_desc: 'Comms stack: mesh radios + LTE fallback.' },
    { id: 'BJ1', group: 'B', sector: 'BUILD', depends_on: ['PC1', 'BI1'], estimate_ms: 15020, tps_min: 55, tps_max: 102, work_desc: 'Teleop dashboard with joystick mapping and overlays.' },
    { id: 'BK1', group: 'B', sector: 'BUILD', depends_on: ['PA4'], estimate_ms: 12831, tps_min: 78, tps_max: 86, work_desc: 'Black‑box logging: circular buffer + SD card.' },
    { id: 'BL1', group: 'B', sector: 'BUILD', depends_on: ['BG1'], estimate_ms: 16503, tps_min: 41, tps_max: 89, work_desc: 'Self‑righting routine & torque‑limited push‑up.' },
    { id: 'BM1', group: 'B', sector: 'BUILD', depends_on: ['BB2'], estimate_ms: 15506, tps_min: 72, tps_max: 91, work_desc: 'Battery hot‑swap latch & interlock.' },
    { id: 'BN1', group: 'B', sector: 'BUILD', depends_on: ['PD2', 'BB2'], estimate_ms: 12096, tps_min: 70, tps_max: 83, work_desc: 'Toe heaters & pack warmers control.' },
    { id: 'BO1', group: 'B', sector: 'BUILD', depends_on: ['BA3'], estimate_ms: 16313, tps_min: 57, tps_max: 102, work_desc: 'Payload basket quick‑release & weight sensor.' },
    { id: 'BP1', group: 'B', sector: 'BUILD', depends_on: ['BA3'], estimate_ms: 24482, tps_min: 53, tps_max: 97, work_desc: 'Arm/hand compliance tuning; underactuated fingers.' },
    { id: 'BQ1', group: 'B', sector: 'BUILD', depends_on: ['PB1', 'BH1'], estimate_ms: 12003, tps_min: 75, tps_max: 119, work_desc: 'Onboard map caching & route planner module.' },
    { id: 'BR1', group: 'B', sector: 'BUILD', depends_on: ['BC1', 'BF1'], estimate_ms: 16859, tps_min: 46, tps_max: 96, work_desc: 'Wind gust compensation using torso IMU.' },
    { id: 'BS1', group: 'B', sector: 'BUILD', depends_on: ['BF1', 'BE1'], estimate_ms: 18287, tps_min: 49, tps_max: 120, work_desc: 'Energy‑optimal gait planner (MPC).' },
    { id: 'BT1', group: 'B', sector: 'BUILD', depends_on: ['BB2'], estimate_ms: 24673, tps_min: 80, tps_max: 120, work_desc: 'Firmware watchdogs & brownout recovery.' },
    { id: 'BU1', group: 'B', sector: 'BUILD', depends_on: ['BK1'], estimate_ms: 13391, tps_min: 49, tps_max: 102, work_desc: 'Diagnostics LCD & beeper; field error codes.' },
    { id: 'BV1', group: 'B', sector: 'BUILD', depends_on: ['BE2'], estimate_ms: 20738, tps_min: 58, tps_max: 120, work_desc: 'Cable management tidy pass; tie-downs & labels.' },
    { id: 'BW1', group: 'B', sector: 'BUILD', depends_on: ['BA5', 'BE2'], estimate_ms: 24676, tps_min: 69, tps_max: 93, work_desc: 'Ingress test tweaks toward IP54.' },
    { id: 'BX1', group: 'B', sector: 'BUILD', depends_on: ['BA2'], estimate_ms: 15691, tps_min: 48, tps_max: 97, work_desc: 'Motor driver autotune under payload.' },
    { id: 'BY1', group: 'B', sector: 'BUILD', depends_on: ['PB1', 'BF1'], estimate_ms: 13462, tps_min: 68, tps_max: 105, work_desc: 'Footstep planner constraints generated from incline profiles.' },
    { id: 'BZ1', group: 'B', sector: 'BUILD', depends_on: ['BD2'], estimate_ms: 16292, tps_min: 52, tps_max: 87, work_desc: 'Emergency rope anchor points (no parachutes, sadly).' },

    // -----------------------------
    // Eval fan-in
    // -----------------------------
    { id: 'EA1', group: 'E', sector: 'EVAL', depends_on: ['BA2', 'BB2'], estimate_ms: 19789, tps_min: 75, tps_max: 92, work_desc: 'Bench test chassis + power under load; measure thermal margins.' },
    { id: 'EA2', group: 'E', sector: 'EVAL', depends_on: ['BC1'], estimate_ms: 22654, tps_min: 62, tps_max: 117, work_desc: 'Calibrate sensors; validate sensor fusion on incline jig.' },
    { id: 'EB1', group: 'E', sector: 'EVAL', depends_on: ['EA1'], estimate_ms: 24857, tps_min: 73, tps_max: 106, work_desc: 'Field simulate ascent on treadmill with weighted rock basket.' },

    { id: 'EA3', group: 'E', sector: 'EVAL', depends_on: ['BA3'], estimate_ms: 11179, tps_min: 44, tps_max: 101, work_desc: 'Run end‑to‑end timed haul cycles; tune gait vs. payload.' },
    { id: 'EA4', group: 'E', sector: 'EVAL', depends_on: ['BF1', 'EA1'], estimate_ms: 21947, tps_min: 43, tps_max: 119, work_desc: 'Gait stability on uneven rocks; perturbation test.' },
    { id: 'EB2', group: 'E', sector: 'EVAL', depends_on: ['BB2', 'BN1'], estimate_ms: 16406, tps_min: 75, tps_max: 89, work_desc: 'Battery endurance with 15 kg payload; cold‑soak −5°C.' },
    { id: 'EC1', group: 'E', sector: 'EVAL', depends_on: ['BI1'], estimate_ms: 29591, tps_min: 54, tps_max: 113, work_desc: 'RF link range & dropout characterization on trail.' },
    { id: 'EC2', group: 'E', sector: 'EVAL', depends_on: ['BJ1', 'BT1'], estimate_ms: 28336, tps_min: 75, tps_max: 112, work_desc: 'E‑stop latency under load; brake hold verification.' },
    { id: 'ED1', group: 'E', sector: 'EVAL', depends_on: ['BD1'], estimate_ms: 26790, tps_min: 50, tps_max: 100, work_desc: 'Sole/tread swap tests across scree, slab, and talus.' },
    { id: 'ED2', group: 'E', sector: 'EVAL', depends_on: ['BD2'], estimate_ms: 22425, tps_min: 44, tps_max: 113, work_desc: 'Winch assist regression on steep treadmill profile.' },
    { id: 'EE1', group: 'E', sector: 'EVAL', depends_on: ['BQ1'], estimate_ms: 11716, tps_min: 68, tps_max: 117, work_desc: 'Route planner A/B vs human guide timings.' },
    { id: 'EE2', group: 'E', sector: 'EVAL', depends_on: ['BE1'], estimate_ms: 12041, tps_min: 61, tps_max: 95, work_desc: 'Thermal derate profile under sun + wind.' },
    { id: 'EF1', group: 'E', sector: 'EVAL', depends_on: ['BL1'], estimate_ms: 27248, tps_min: 71, tps_max: 120, work_desc: 'Self‑righting trials on padded slope.' },
    { id: 'EG1', group: 'E', sector: 'EVAL', depends_on: ['BK1', 'BT1'], estimate_ms: 28317, tps_min: 80, tps_max: 97, work_desc: 'Black‑box log integrity; fault injection.' },
    { id: 'EH1', group: 'E', sector: 'EVAL', depends_on: ['BG2', 'BO1'], estimate_ms: 12889, tps_min: 45, tps_max: 85, work_desc: 'Grasp success rate vs randomized basket loads.' },
    { id: 'EI1', group: 'E', sector: 'EVAL', depends_on: ['BH2'], estimate_ms: 24619, tps_min: 74, tps_max: 113, work_desc: 'Ice reflectance compensation field validation.' },
    { id: 'EJ1', group: 'E', sector: 'EVAL', depends_on: ['BR1'], estimate_ms: 17879, tps_min: 54, tps_max: 95, work_desc: 'High wind fan‑tunnel test; gust rejection.' },
    { id: 'EK1', group: 'E', sector: 'EVAL', depends_on: ['PE1', 'BJ1'], estimate_ms: 21180, tps_min: 69, tps_max: 83, work_desc: 'Operator usability dry‑run; SOP rehearsal.' },
    { id: 'EL1', group: 'E', sector: 'EVAL', depends_on: ['BS1', 'EA3'], estimate_ms: 12727, tps_min: 60, tps_max: 113, work_desc: 'Energy per meter vs spec; regression tracking.' },
    { id: 'EM1', group: 'E', sector: 'EVAL', depends_on: ['EA1', 'EG1'], estimate_ms: 25208, tps_min: 65, tps_max: 105, work_desc: 'Multi‑hour continuous run; MTBF snapshot.' },
    { id: 'EN1', group: 'E', sector: 'EVAL', depends_on: ['BI1', 'BG1', 'BT1'], estimate_ms: 20326, tps_min: 73, tps_max: 119, work_desc: 'Recovery drill: comms blackout → safe kneel → reboot.' },
    { id: 'EO1', group: 'E', sector: 'EVAL', depends_on: ['EA2', 'EB1'], estimate_ms: 18244, tps_min: 64, tps_max: 105, work_desc: 'Sensor calibration drift check after descent.' },
    { id: 'EP1', group: 'E', sector: 'EVAL', depends_on: ['BW1'], estimate_ms: 24650, tps_min: 58, tps_max: 103, work_desc: 'Ingress protection validation with mist+dust.' },
    { id: 'EQ1', group: 'E', sector: 'EVAL', depends_on: ['BN1', 'BB2'], estimate_ms: 25037, tps_min: 57, tps_max: 86, work_desc: 'Cold‑start test at dawn.' },
    { id: 'ER1', group: 'E', sector: 'EVAL', depends_on: ['BJ1', 'BF1'], estimate_ms: 18742, tps_min: 59, tps_max: 91, work_desc: 'Trail courtesy test: pause for hikers, resume smoothly.' },
    { id: 'ES1', group: 'E', sector: 'EVAL', depends_on: ['BZ1'], estimate_ms: 12294, tps_min: 44, tps_max: 119, work_desc: 'Rope anchor static load test.' },
    { id: 'ET1', group: 'E', sector: 'EVAL', depends_on: ['BY1', 'EA3'], estimate_ms: 16205, tps_min: 61, tps_max: 84, work_desc: 'Footstep planner performance vs incline dataset.' },
    { id: 'EU1', group: 'E', sector: 'EVAL', depends_on: ['BD1', 'EA3'], estimate_ms: 21341, tps_min: 61, tps_max: 115, work_desc: 'Snow patch crossing with microspikes.' },
    { id: 'EV1', group: 'E', sector: 'EVAL', depends_on: ['BF1', 'EA3'], estimate_ms: 10545, tps_min: 70, tps_max: 104, work_desc: 'Descending brake tests; toe/heel first policy.' },
    { id: 'EW1', group: 'E', sector: 'EVAL', depends_on: ['BC1', 'EA2'], estimate_ms: 27771, tps_min: 78, tps_max: 98, work_desc: 'IMU bias & LiDAR occlusion scenarios.' },
    { id: 'EX1', group: 'E', sector: 'EVAL', depends_on: ['PF2', 'BA5'], estimate_ms: 23606, tps_min: 65, tps_max: 104, work_desc: 'Media capture dry‑run; camera mounts stable for launch day?' },

    // -----------------------------
    // Deploy
    // -----------------------------
    { id: 'DA1', group: 'D', sector: 'DEPLOY', depends_on: ['EA1'], estimate_ms: 19657, tps_min: 47, tps_max: 107, work_desc: 'Prepare production build: fasteners, harnesses, and protective shells.' },
    { id: 'DA2', group: 'D', sector: 'DEPLOY', depends_on: ['EA2'], estimate_ms: 11452, tps_min: 53, tps_max: 100, work_desc: 'Stage charging dock and on-site tools at mountain base.' },
    { id: 'DB1', group: 'D', sector: 'DEPLOY', depends_on: ['EB1'], estimate_ms: 17742, tps_min: 42, tps_max: 93, work_desc: 'Finalize safety checklist and operator SOP for haul cycles.' },
    { id: 'DA3', group: 'D', sector: 'DEPLOY', depends_on: ['EA3'], estimate_ms: 29450, tps_min: 55, tps_max: 104, work_desc: 'Package, label, and ship final unit to the trailhead.' },

    { id: 'DB2', group: 'D', sector: 'DEPLOY', depends_on: ['PF1', 'DA1'], estimate_ms: 29398, tps_min: 51, tps_max: 82, work_desc: 'Assemble field kit (spares, tools, adhesives).' },
    { id: 'DC1', group: 'D', sector: 'DEPLOY', depends_on: ['DA3'], estimate_ms: 17307, tps_min: 77, tps_max: 112, work_desc: 'Vehicle load‑out and weight balance.' },
    { id: 'DC2', group: 'D', sector: 'DEPLOY', depends_on: ['PD1', 'DA2'], estimate_ms: 27006, tps_min: 64, tps_max: 113, work_desc: 'Scout team brief: routes, weather, comms.' },
    { id: 'DD1', group: 'D', sector: 'DEPLOY', depends_on: ['BB4', 'DA2'], estimate_ms: 12324, tps_min: 51, tps_max: 112, work_desc: 'Basecamp power: generator + solar mats.' },
    { id: 'DD2', group: 'D', sector: 'DEPLOY', depends_on: ['BI1', 'DA2'], estimate_ms: 23252, tps_min: 53, tps_max: 91, work_desc: 'Camp mesh network setup & test.' },
    { id: 'DE1', group: 'D', sector: 'DEPLOY', depends_on: ['EC2', 'EK1'], estimate_ms: 24098, tps_min: 44, tps_max: 97, work_desc: 'Safety officer sign‑off.' },
    { id: 'DF1', group: 'D', sector: 'DEPLOY', depends_on: ['PA5', 'DA3'], estimate_ms: 25026, tps_min: 71, tps_max: 93, work_desc: 'Permit check‑in with rangers.' },
    { id: 'DG1', group: 'D', sector: 'DEPLOY', depends_on: ['DB1', 'EK1'], estimate_ms: 23626, tps_min: 64, tps_max: 109, work_desc: 'Pre‑ascent checklist dry‑run with timer.' },
    { id: 'DH1', group: 'D', sector: 'DEPLOY', depends_on: ['EX1', 'DC2'], estimate_ms: 29506, tps_min: 64, tps_max: 115, work_desc: 'Public launch livestream (optional, for the story).' },
    { id: 'DI1', group: 'D', sector: 'DEPLOY', depends_on: ['EN1', 'DA2'], estimate_ms: 23040, tps_min: 62, tps_max: 112, work_desc: 'Stage rescue kit and med kit at switchback 3.' },
    { id: 'DJ1', group: 'D', sector: 'DEPLOY', depends_on: ['DA3'], estimate_ms: 19765, tps_min: 77, tps_max: 114, work_desc: 'Deploy trail signage: “Robots at work.”' },
    { id: 'DK1', group: 'D', sector: 'DEPLOY', depends_on: ['EA3', 'DA2'], estimate_ms: 27577, tps_min: 74, tps_max: 111, work_desc: 'Base loop dry‑run at mountain; 2× laps.' },
    { id: 'DL1', group: 'D', sector: 'DEPLOY', depends_on: ['DE1', 'DG1', 'DK1'], estimate_ms: 29741, tps_min: 68, tps_max: 107, work_desc: 'Go/No‑Go review.' },
    { id: 'DM1', group: 'D', sector: 'DEPLOY', depends_on: ['DL1', 'DC2'], estimate_ms: 18702, tps_min: 64, tps_max: 104, work_desc: 'Summit attempt: select start window.' },
    { id: 'DN1', group: 'D', sector: 'DEPLOY', depends_on: ['DM1'], estimate_ms: 13920, tps_min: 80, tps_max: 82, work_desc: 'Post‑run teardown & base debrief.' },
    { id: 'DO1', group: 'D', sector: 'DEPLOY', depends_on: ['DN1'], estimate_ms: 21259, tps_min: 72, tps_max: 120, work_desc: 'Data offload + log triage.' },
    { id: 'DP1', group: 'D', sector: 'DEPLOY', depends_on: ['DO1'], estimate_ms: 23544, tps_min: 73, tps_max: 114, work_desc: 'Postmortem write‑up & highlight reel.' },
    { id: 'DQ1', group: 'D', sector: 'DEPLOY', depends_on: ['DC2'], estimate_ms: 20227, tps_min: 72, tps_max: 81, work_desc: 'Procure extra snacks—operator morale matters.' },
    { id: 'DR1', group: 'D', sector: 'DEPLOY', depends_on: ['DN1'], estimate_ms: 23331, tps_min: 57, tps_max: 83, work_desc: 'Battery recycling & disposal compliance.' },
    { id: 'DS1', group: 'D', sector: 'DEPLOY', depends_on: ['DN1'], estimate_ms: 21312, tps_min: 42, tps_max: 94, work_desc: 'Thank‑you notes to rangers and volunteers.' },
  ],
};

export default humanoidPlan;
```

## File: `plans/index.ts`
```typescript
// Import concrete plans so we can build a registry
import { humanoidPlan } from './humanoid';
import { martianHomecomingPlan } from './martianHomecomingPlan';
import { franticPlan } from './frantic';
export { humanoidPlan, martianHomecomingPlan, franticPlan };
export * from './types';

// Central registry to drive UI/worker off plan definitions
import type { PlanDefinition } from './types';

export const ALL_PLANS: readonly PlanDefinition[] = [
  humanoidPlan,
  martianHomecomingPlan,
  franticPlan,
] as const;

export const PLAN_NAMES = ALL_PLANS.map(p => p.name) as readonly string[];

export const PLAN_REGISTRY: Record<string, PlanDefinition> = ALL_PLANS.reduce((acc, p) => {
  acc[p.name] = p;
  return acc;
}, {} as Record<string, PlanDefinition>);

export function getPlanByName(name: string): PlanDefinition | undefined {
  return PLAN_REGISTRY[name];
}

export const DEFAULT_PLAN_NAME: string = 'Humanoid';
```

## File: `plans/martianHomecomingPlan.ts`
```typescript
import type { PlanDefinition } from './types';

// Mars noir: a stranded robot turns dust into delta‑v, writing letters to a lost wife back on Earth.
export const martianHomecomingPlan: PlanDefinition = {
  name: 'Homecoming',
  description:
    "A stranded robot on Mars rebuilds a ship from dust, fuel, and resolve to get back to Earth and his long‑lost wife. Letters to home punctuate a dark, hopeful sci‑fi heist against physics.",
  groups: [
    {
      id: 'P',
      title: 'Survival & Mission Plotting',
      description: 'Hard limits, map the crater, choose a way home, and outline the letter cadence.',
    },
    {
      id: 'B',
      title: 'Resource Extraction & Spaceframe Build',
      description: 'Turn Mars into parts: fuel, hull, avionics, comms, and guidance.',
    },
    {
      id: 'E',
      title: 'Trials & Validation',
      description: 'Burn, freeze, shake, and prove the stack can survive the red planet and the void.',
    },
    {
      id: 'D',
      title: 'Departure & Earth Return',
      description: 'Pad ops, ascent, cruise, entry, reunion.',
    },
  ],
  items: [
    // -----------------------------
    // Planning (P)
    // -----------------------------
    { id: 'PA1', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 23299, tps_min: 60, tps_max: 105, work_desc: 'Wake diagnostics; inventory power, mass, and time. Survival triage.' },
    { id: 'PA2', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 26827, tps_min: 58, tps_max: 96, work_desc: 'Crater survey: hazards, ice hints, basalt beds, and salvage beacons.' },
    { id: 'PA3', group: 'P', sector: 'PLANNING', depends_on: ['PA1'], estimate_ms: 28209, tps_min: 43, tps_max: 97, work_desc: 'Define return objective, delta‑v budget, and success criteria.' },
    { id: 'PA4', group: 'P', sector: 'PLANNING', depends_on: ['PA1'], estimate_ms: 15584, tps_min: 73, tps_max: 114, work_desc: 'Risk register: dust storms, radiation, actuator wear, memory decay.' },
    { id: 'PA5', group: 'P', sector: 'PLANNING', depends_on: ['PA2'], estimate_ms: 21093, tps_min: 51, tps_max: 114, work_desc: 'Resource map: ice veins, hematite, perchlorates, derelict landers.' },
    { id: 'PA6', group: 'P', sector: 'PLANNING', depends_on: ['PA3'], estimate_ms: 12573, tps_min: 66, tps_max: 110, work_desc: 'Fuel path: choose methalox via Sabatier; size reactors and power.' },
    { id: 'PA7', group: 'P', sector: 'PLANNING', depends_on: ['PA5'], estimate_ms: 28435, tps_min: 68, tps_max: 104, work_desc: 'Fabrication roadmap; BOM from in‑situ resources + salvage.' },
    { id: 'PA8', group: 'P', sector: 'PLANNING', depends_on: ['PA6'], estimate_ms: 11416, tps_min: 79, tps_max: 101, work_desc: 'Trajectory sketch; launch windows and corridor constraints.' },

    { id: 'PB1', group: 'P', sector: 'PLANNING', depends_on: ['PA2'], estimate_ms: 11967, tps_min: 64, tps_max: 100, work_desc: 'Hab & dust seals; shelter for long runs and letter writing.' },
    { id: 'PB2', group: 'P', sector: 'PLANNING', depends_on: ['PA5'], estimate_ms: 29614, tps_min: 69, tps_max: 118, work_desc: 'Ice mining plan; desalinate and neutralize perchlorates.' },
    { id: 'PB3', group: 'P', sector: 'PLANNING', depends_on: ['PA4'], estimate_ms: 10133, tps_min: 61, tps_max: 101, work_desc: 'Thermal survival plan: cold‑soak nights, radiator and heaters.' },
    { id: 'PB4', group: 'P', sector: 'PLANNING', depends_on: ['PA5'], estimate_ms: 25404, tps_min: 60, tps_max: 80, work_desc: 'Regolith to parts: kiln, fiber, sinter, and cast workcells.' },
    { id: 'PB5', group: 'P', sector: 'PLANNING', depends_on: ['PA1'], estimate_ms: 18594, tps_min: 56, tps_max: 99, work_desc: 'Salvage rules: what to cannibalize; preserve heritage sites.' },
    { id: 'PB6', group: 'P', sector: 'PLANNING', depends_on: ['PB1'], estimate_ms: 17059, tps_min: 57, tps_max: 84, work_desc: 'Comms stack options: UHF relay, X‑band, optical laser.' },
    { id: 'PB7', group: 'P', sector: 'PLANNING', depends_on: ['PA7'], estimate_ms: 25425, tps_min: 40, tps_max: 110, work_desc: 'Material assays; update regolith composition model.' },
    { id: 'PB8', group: 'P', sector: 'PLANNING', depends_on: ['PA7'], estimate_ms: 11489, tps_min: 73, tps_max: 96, work_desc: 'Tooling list; printable jigs; contingency spares.' },

    { id: 'PC1', group: 'P', sector: 'PLANNING', depends_on: ['PA3', 'PB5'], estimate_ms: 23370, tps_min: 51, tps_max: 88, work_desc: 'Letter beam protocol v0; encryption & error correction.' },
    { id: 'PC2', group: 'P', sector: 'PLANNING', depends_on: ['PC1'], estimate_ms: 18765, tps_min: 80, tps_max: 96, work_desc: 'Storm mode triggers; safe‑kneel & blackout behaviors.' },
    { id: 'PC3', group: 'P', sector: 'PLANNING', depends_on: ['PA8', 'PC1'], estimate_ms: 18068, tps_min: 71, tps_max: 119, work_desc: 'Ephemeris and star catalog ingestion plan.' },
    { id: 'PC4', group: 'P', sector: 'PLANNING', depends_on: ['PB6', 'PC2'], estimate_ms: 22874, tps_min: 62, tps_max: 87, work_desc: 'Noir letter pack: voice, cadence, checksum rituals.' },

    { id: 'PD1', group: 'P', sector: 'PLANNING', depends_on: ['PB2', 'PA8'], estimate_ms: 23177, tps_min: 73, tps_max: 115, work_desc: 'Power plan: solar expansion, MPPT, battery refurb.' },
    { id: 'PD2', group: 'P', sector: 'PLANNING', depends_on: ['PB3', 'PA4'], estimate_ms: 11442, tps_min: 51, tps_max: 88, work_desc: 'Thermal plan: radiators, insulation, cryo losses.' },
    { id: 'PD3', group: 'P', sector: 'PLANNING', depends_on: ['PD1', 'PD2'], estimate_ms: 19727, tps_min: 47, tps_max: 114, work_desc: 'Critical path; fan‑in gates; go/no‑go criteria.' },
    { id: 'PD4', group: 'P', sector: 'PLANNING', depends_on: ['PD3'], estimate_ms: 22660, tps_min: 66, tps_max: 92, work_desc: 'Operator (me) SOPs; checklists for lonely nights.' },

    // -----------------------------
    // Build (B)
    // -----------------------------
    { id: 'BA1', group: 'B', sector: 'BUILD', depends_on: ['PD2', 'PA2'], estimate_ms: 19465, tps_min: 45, tps_max: 107, work_desc: 'CO₂ capture: compressor, filters, frost trap.' },
    { id: 'BA2', group: 'B', sector: 'BUILD', depends_on: ['PD2', 'PB2'], estimate_ms: 27324, tps_min: 69, tps_max: 113, work_desc: 'Electrolyzer assembly; O₂/H₂ split under dust‑proof enclosures.' },
    { id: 'BA3', group: 'B', sector: 'BUILD', depends_on: ['PB2'], estimate_ms: 19739, tps_min: 59, tps_max: 117, work_desc: 'Ice mining rig; drill, melt, desalinate; perchlorate scrub.' },
    { id: 'BA4', group: 'B', sector: 'BUILD', depends_on: ['BA1', 'BA2'], estimate_ms: 23276, tps_min: 60, tps_max: 116, work_desc: 'Sabatier reactor; nickel catalyst micro‑channels; heat coupling.' },
    { id: 'BA5', group: 'B', sector: 'BUILD', depends_on: ['BA4'], estimate_ms: 21319, tps_min: 73, tps_max: 111, work_desc: 'Cryo plant; CH₄ liquefaction and O₂ condensation; dewars.' },
    { id: 'BA6', group: 'B', sector: 'BUILD', depends_on: ['PB4'], estimate_ms: 23593, tps_min: 49, tps_max: 99, work_desc: 'Microwave kiln for regolith sintering; brick and tile line.' },
    { id: 'BA7', group: 'B', sector: 'BUILD', depends_on: ['BA6'], estimate_ms: 13986, tps_min: 56, tps_max: 116, work_desc: 'Basalt fiber extruder; tow winding and spooler.' },
    { id: 'BA8', group: 'B', sector: 'BUILD', depends_on: ['PB7', 'BA6'], estimate_ms: 20309, tps_min: 79, tps_max: 88, work_desc: 'Molten‑oxide electrolysis cell; Fe/Al ingots from dust.' },
    { id: 'BA9', group: 'B', sector: 'BUILD', depends_on: ['BA7', 'BA6'], estimate_ms: 28000, tps_min: 48, tps_max: 80, work_desc: '3D print pressure hull sections with basalt‑regolith composite.' },
    { id: 'BA10', group: 'B', sector: 'BUILD', depends_on: ['BA8'], estimate_ms: 20639, tps_min: 58, tps_max: 108, work_desc: 'Tankage spin‑forming; welds; proof fixtures.' },
    { id: 'BA11', group: 'B', sector: 'BUILD', depends_on: ['BA6'], estimate_ms: 21806, tps_min: 59, tps_max: 107, work_desc: 'Seals & gaskets from sulfur polymer; seat tests.' },
    { id: 'BA12', group: 'B', sector: 'BUILD', depends_on: ['PB5'], estimate_ms: 28342, tps_min: 47, tps_max: 114, work_desc: 'Electronics salvage: power rails, MCUs, RF front‑ends.' },
    { id: 'BA13', group: 'B', sector: 'BUILD', depends_on: ['BA12'], estimate_ms: 15955, tps_min: 60, tps_max: 104, work_desc: 'Star tracker build; baffling; dark‑tent alignment jig.' },
    { id: 'BA14', group: 'B', sector: 'BUILD', depends_on: ['BA13'], estimate_ms: 19700, tps_min: 61, tps_max: 110, work_desc: 'GN&C stack; IMU + sun sensor fusion.' },
    { id: 'BA15', group: 'B', sector: 'BUILD', depends_on: ['PB6', 'BA12'], estimate_ms: 26653, tps_min: 58, tps_max: 102, work_desc: 'Deep‑space comms: X‑band dish & laser head on gimbal.' },
    { id: 'BA16', group: 'B', sector: 'BUILD', depends_on: ['BA15'], estimate_ms: 16524, tps_min: 62, tps_max: 105, work_desc: 'Antenna lens heaters and dust sweepers.' },
    { id: 'BA17', group: 'B', sector: 'BUILD', depends_on: ['BA11', 'BA9'], estimate_ms: 19406, tps_min: 60, tps_max: 93, work_desc: 'Simple airlock; pressure boundary integration.' },
    { id: 'BA18', group: 'B', sector: 'BUILD', depends_on: ['PD2', 'BA9'], estimate_ms: 15395, tps_min: 53, tps_max: 86, work_desc: 'Thermal & compute radiator pack; loop plumbing.' },
    { id: 'BA19', group: 'B', sector: 'BUILD', depends_on: ['BA4', 'BA8'], estimate_ms: 16823, tps_min: 62, tps_max: 115, work_desc: 'Main engine: injector, regen‑cooled nozzle, igniter.' },
    { id: 'BA20', group: 'B', sector: 'BUILD', depends_on: ['BA10', 'BA19'], estimate_ms: 24346, tps_min: 54, tps_max: 114, work_desc: 'Pressure‑fed feed system; high‑pressure plumbing and valves.' },
    { id: 'BA21', group: 'B', sector: 'BUILD', depends_on: ['BA19'], estimate_ms: 10013, tps_min: 64, tps_max: 87, work_desc: 'RCS thrusters and cold‑gas reserve.' },
    { id: 'BA22', group: 'B', sector: 'BUILD', depends_on: ['BA6', 'BA8'], estimate_ms: 24155, tps_min: 61, tps_max: 82, work_desc: 'Landing legs with crush‑core footpads.' },
    { id: 'BA23', group: 'B', sector: 'BUILD', depends_on: ['BA14'], estimate_ms: 28169, tps_min: 72, tps_max: 117, work_desc: 'Autopilot; entry/landing hazard map logic.' },
    { id: 'BA24', group: 'B', sector: 'BUILD', depends_on: ['BA12', 'PD1'], estimate_ms: 16051, tps_min: 44, tps_max: 107, work_desc: 'Battery refurb and solar bus controller.' },
    { id: 'BA25', group: 'B', sector: 'BUILD', depends_on: ['BA24'], estimate_ms: 27421, tps_min: 47, tps_max: 110, work_desc: 'Solar field expansion; MPPT micro‑inverters.' },
    { id: 'BA26', group: 'B', sector: 'BUILD', depends_on: ['PB1', 'PC4'], estimate_ms: 24524, tps_min: 60, tps_max: 120, work_desc: 'Black‑box logger + engraved letter plates (“Noir Log”).' },
    { id: 'BA27', group: 'B', sector: 'BUILD', depends_on: ['BA5'], estimate_ms: 28404, tps_min: 75, tps_max: 110, work_desc: 'Cryo insulation: multilayer blankets and silica aerogel.' },
    { id: 'BA28', group: 'B', sector: 'BUILD', depends_on: ['BA5', 'BA20'], estimate_ms: 15677, tps_min: 53, tps_max: 80, work_desc: 'Fuel/oxidizer plumbing; checks; blow‑down logic.' },
    { id: 'BA29', group: 'B', sector: 'BUILD', depends_on: ['BA12', 'BA14'], estimate_ms: 19282, tps_min: 43, tps_max: 92, work_desc: 'Flight computer; redundant buses; rad shielding (regolith tile).' },
    { id: 'BA30', group: 'B', sector: 'BUILD', depends_on: ['BA9', 'BA26'], estimate_ms: 21889, tps_min: 78, tps_max: 88, work_desc: 'Hull “mailbox” vault for physical letters.' },
    { id: 'BA31', group: 'B', sector: 'BUILD', depends_on: ['BA6', 'BA18'], estimate_ms: 29659, tps_min: 46, tps_max: 92, work_desc: 'Heat shield: phenolic char + aerogel tile stack.' },
    { id: 'BA32', group: 'B', sector: 'BUILD', depends_on: ['BA29'], estimate_ms: 10280, tps_min: 80, tps_max: 108, work_desc: 'Fairing/cover ejectors; spring‑bolt actuation; safing.' },
    { id: 'BA33', group: 'B', sector: 'BUILD', depends_on: ['BA15'], estimate_ms: 12686, tps_min: 65, tps_max: 110, work_desc: 'S‑band proximity transceiver for Earthside beacon lock.' },
    { id: 'BA34', group: 'B', sector: 'BUILD', depends_on: ['BA13', 'PC3'], estimate_ms: 14386, tps_min: 51, tps_max: 85, work_desc: 'Ephemeris uploader and star catalog seed.' },
    { id: 'BA35', group: 'B', sector: 'BUILD', depends_on: ['BA9'], estimate_ms: 16487, tps_min: 46, tps_max: 111, work_desc: 'Mission patch acid‑etched on hull: “FIND AURORA”.' },
    { id: 'BA36', group: 'B', sector: 'BUILD', depends_on: ['PC4', 'BA29'], estimate_ms: 14974, tps_min: 67, tps_max: 113, work_desc: 'Encrypted letter vault; checksums; restore keys.' },
    { id: 'BA37', group: 'B', sector: 'BUILD', depends_on: ['PC2', 'BA22'], estimate_ms: 19167, tps_min: 79, tps_max: 109, work_desc: 'Autonomous storm mode: anchors, tent, low‑profile posture.' },
    { id: 'BA38', group: 'B', sector: 'BUILD', depends_on: ['BA6'], estimate_ms: 29207, tps_min: 58, tps_max: 113, work_desc: 'Ore hauler kit: wheels/tracks for dune crossings.' },
    { id: 'BA39', group: 'B', sector: 'BUILD', depends_on: ['BA3'], estimate_ms: 13978, tps_min: 79, tps_max: 97, work_desc: 'Water purification & storage; perchlorate neutralizer plant.' },
    { id: 'BA40', group: 'B', sector: 'BUILD', depends_on: ['BA4'], estimate_ms: 29140, tps_min: 58, tps_max: 119, work_desc: 'Catalyst regeneration line; spare cartridges.' },
    { id: 'BA41', group: 'B', sector: 'BUILD', depends_on: ['PA8', 'BA34', 'BA29'], estimate_ms: 24838, tps_min: 57, tps_max: 119, work_desc: 'Trajectory & launch‑window solver; corridor constraints.' },

    // -----------------------------
    // Evaluation (E)
    // -----------------------------
    { id: 'EA1', group: 'E', sector: 'EVAL', depends_on: ['BA24', 'BA18'], estimate_ms: 26215, tps_min: 71, tps_max: 86, work_desc: 'Power & thermal endurance across a Martian night.' },
    { id: 'EA2', group: 'E', sector: 'EVAL', depends_on: ['BA2'], estimate_ms: 18471, tps_min: 62, tps_max: 85, work_desc: 'Electrolyzer continuous run; O₂ purity & membrane health.' },
    { id: 'EA3', group: 'E', sector: 'EVAL', depends_on: ['BA4'], estimate_ms: 23498, tps_min: 72, tps_max: 102, work_desc: 'Sabatier yield curve; catalyst life modeling.' },
    { id: 'EA4', group: 'E', sector: 'EVAL', depends_on: ['BA5', 'BA27'], estimate_ms: 28979, tps_min: 62, tps_max: 118, work_desc: 'Cryo boil‑off rate; insulation performance.' },
    { id: 'EA5', group: 'E', sector: 'EVAL', depends_on: ['BA10', 'BA28'], estimate_ms: 11242, tps_min: 62, tps_max: 87, work_desc: 'Tank pressure proof & plumbing leak checks.' },
    { id: 'EA6', group: 'E', sector: 'EVAL', depends_on: ['BA19', 'BA28'], estimate_ms: 22492, tps_min: 40, tps_max: 116, work_desc: 'Engine static fire (short) with instrumentation.' },
    { id: 'EA7', group: 'E', sector: 'EVAL', depends_on: ['EA6'], estimate_ms: 16315, tps_min: 73, tps_max: 104, work_desc: 'Engine static fire (long); thermal margins & ignition repeatability.' },
    { id: 'EA8', group: 'E', sector: 'EVAL', depends_on: ['BA21', 'BA29'], estimate_ms: 19732, tps_min: 77, tps_max: 84, work_desc: 'RCS pulsing; attitude hold & limit cycles.' },
    { id: 'EA9', group: 'E', sector: 'EVAL', depends_on: ['BA29', 'BA34'], estimate_ms: 29890, tps_min: 41, tps_max: 109, work_desc: 'Avionics HIL sim; star‑tracker dark‑tent validation.' },
    { id: 'EA10', group: 'E', sector: 'EVAL', depends_on: ['BA15', 'BA36'], estimate_ms: 20844, tps_min: 74, tps_max: 102, work_desc: 'Earth link budget; letter send dry‑run with checksum audit.' },
    { id: 'EA11', group: 'E', sector: 'EVAL', depends_on: ['BA37'], estimate_ms: 19107, tps_min: 57, tps_max: 100, work_desc: 'Dust storm survival drill; anchor and ride‑out.' },
    { id: 'EA12', group: 'E', sector: 'EVAL', depends_on: ['BA17'], estimate_ms: 14879, tps_min: 78, tps_max: 86, work_desc: 'Hull pressure integrity; airlock seal tests.' },
    { id: 'EA13', group: 'E', sector: 'EVAL', depends_on: ['BA31'], estimate_ms: 14035, tps_min: 65, tps_max: 101, work_desc: 'Heat‑shield char & erosion under arc‑jet surrogate.' },
    { id: 'EA14', group: 'E', sector: 'EVAL', depends_on: ['BA41'], estimate_ms: 22197, tps_min: 47, tps_max: 94, work_desc: 'Trajectory solver validation vs ephemerides; corridor Monte Carlo.' },
    { id: 'EA15', group: 'E', sector: 'EVAL', depends_on: ['BA25'], estimate_ms: 18774, tps_min: 68, tps_max: 98, work_desc: 'Battery endurance; solar field recovery after dusting.' },
    { id: 'EA16', group: 'E', sector: 'EVAL', depends_on: ['BA41', 'BA13'], estimate_ms: 20167, tps_min: 52, tps_max: 114, work_desc: 'Navigation endurance; dead‑reckon vs star‑fix drift.' },
    { id: 'EA17', group: 'E', sector: 'EVAL', depends_on: ['BA26', 'BA29'], estimate_ms: 22919, tps_min: 48, tps_max: 117, work_desc: 'Black‑box integrity & fault injection; letter log immutability.' },
    { id: 'EA18', group: 'E', sector: 'EVAL', depends_on: ['BA9', 'BA18'], estimate_ms: 28678, tps_min: 40, tps_max: 104, work_desc: 'Hull thermal maps; radiator loop performance under sun + wind.' },
    { id: 'EA19', group: 'E', sector: 'EVAL', depends_on: ['BA10'], estimate_ms: 20189, tps_min: 45, tps_max: 117, work_desc: 'Tank slosh and baffle effectiveness; vibration survey.' },
    { id: 'EA20', group: 'E', sector: 'EVAL', depends_on: ['BA29'], estimate_ms: 12616, tps_min: 58, tps_max: 86, work_desc: 'EMI/grounding noise rejection and bus resets.' },

    // -----------------------------
    // Departure & Return (D)
    // -----------------------------
    { id: 'DA1', group: 'D', sector: 'DEPLOY', depends_on: ['EA1', 'EA5'], estimate_ms: 20688, tps_min: 56, tps_max: 85, work_desc: 'Stack vehicle on pad; final bolts torqued and tagged.' },
    { id: 'DA2', group: 'D', sector: 'DEPLOY', depends_on: ['EA4', 'EA5'], estimate_ms: 14942, tps_min: 43, tps_max: 106, work_desc: 'Load cryo; chilldown; umbilicals checkout.' },
    { id: 'DB1', group: 'D', sector: 'DEPLOY', depends_on: ['EA10', 'EA17'], estimate_ms: 10172, tps_min: 57, tps_max: 109, work_desc: 'Final letter to AURORA; engrave plate; transmit checksum.' },
    { id: 'DA3', group: 'D', sector: 'DEPLOY', depends_on: ['EA14', 'DA1'], estimate_ms: 14373, tps_min: 63, tps_max: 83, work_desc: 'Go/No‑Go poll; commit to ignition window.' },
    { id: 'DB2', group: 'D', sector: 'DEPLOY', depends_on: ['DA3', 'DA2'], estimate_ms: 24112, tps_min: 58, tps_max: 116, work_desc: 'Ignition and liftoff; rise above the rust.' },
    { id: 'DC1', group: 'D', sector: 'DEPLOY', depends_on: ['DB2', 'EA14'], estimate_ms: 16742, tps_min: 57, tps_max: 91, work_desc: 'Ascent guidance; pitch program and corridor tracking.' },
    { id: 'DC2', group: 'D', sector: 'DEPLOY', depends_on: ['DC1'], estimate_ms: 20515, tps_min: 57, tps_max: 117, work_desc: 'Mass check; pressure‑fed continuity; continue burn profile.' },
    { id: 'DD1', group: 'D', sector: 'DEPLOY', depends_on: ['DC2', 'BA41'], estimate_ms: 15097, tps_min: 80, tps_max: 96, work_desc: 'Trans‑Earth injection burn; solver‑guided.' },
    { id: 'DD2', group: 'D', sector: 'DEPLOY', depends_on: ['EA10', 'DD1'], estimate_ms: 17212, tps_min: 62, tps_max: 119, work_desc: 'Deep‑space comms check; letters beamed nightly.' },
    { id: 'DE1', group: 'D', sector: 'DEPLOY', depends_on: ['DD1', 'EA9'], estimate_ms: 13787, tps_min: 44, tps_max: 114, work_desc: 'Mid‑course correction #1; star‑tracker alignment.' },
    { id: 'DE2', group: 'D', sector: 'DEPLOY', depends_on: ['DE1'], estimate_ms: 15846, tps_min: 63, tps_max: 89, work_desc: 'Mid‑course correction #2; nav sanity checks.' },
    { id: 'DF1', group: 'D', sector: 'DEPLOY', depends_on: ['BA31', 'EA14'], estimate_ms: 24726, tps_min: 75, tps_max: 106, work_desc: 'Entry interface; bank through corridor per guidance.' },
    { id: 'DF2', group: 'D', sector: 'DEPLOY', depends_on: ['DF1', 'EA8'], estimate_ms: 25899, tps_min: 52, tps_max: 82, work_desc: 'Retro burn and RCS trim; blackout countdown.' },
    { id: 'DG1', group: 'D', sector: 'DEPLOY', depends_on: ['DF2', 'EA17'], estimate_ms: 12180, tps_min: 80, tps_max: 80, work_desc: 'Black‑box final dump; safe‑landing routine.' },
    { id: 'DH1', group: 'D', sector: 'DEPLOY', depends_on: ['DG1', 'BA33'], estimate_ms: 23210, tps_min: 77, tps_max: 91, work_desc: 'Earth beacon acquisition; S‑band handshake.' },
    { id: 'DI1', group: 'D', sector: 'DEPLOY', depends_on: ['DG1'], estimate_ms: 25320, tps_min: 76, tps_max: 120, work_desc: 'Touchdown and cooling; O₂ purge and safing.' },
    { id: 'DJ1', group: 'D', sector: 'DEPLOY', depends_on: ['DH1'], estimate_ms: 20319, tps_min: 43, tps_max: 96, work_desc: 'Unseal vault; find AURORA or leave a trail she can follow.' },
    { id: 'DK1', group: 'D', sector: 'DEPLOY', depends_on: ['DJ1'], estimate_ms: 24914, tps_min: 41, tps_max: 97, work_desc: 'Post‑flight letter: “I made it.”' },
    { id: 'DL1', group: 'D', sector: 'DEPLOY', depends_on: ['DK1', 'DG1'], estimate_ms: 24249, tps_min: 57, tps_max: 109, work_desc: 'Mission postmortem; archive letters, logs, and lessons.' },
  ],
};

export default martianHomecomingPlan;
```

## File: `plans/test.ts`
```typescript
import type { PlanDefinition } from './types';

// Rush plan: more items, more parallelism, higher tps variance
export const testPlan: PlanDefinition = {
  name: 'Test',
  description: 'Test plan',
  groups: [
    {
      id: 'P',
      title: 'Mission Planning',
      description: 'Define mission goals, constraints, terrain routes, budget, and safety architecture for the ascent.',
    },
    {
      id: 'B',
      title: 'Mechanical & Power Build',
      description: 'Exoskeleton fabrication, actuation, power systems, and sensors required to haul rocks uphill.',
    },
    {
      id: 'E',
      title: 'Evaluation & Field Tests',
      description: 'Bench and field validation, calibration, and timed haul cycles under load.',
    },
    {
      id: 'D',
      title: 'Deployment & Operations',
      description: 'Productionization, staging at the mountain base, and operational readiness for repeated hauls.',
    },
  ],
  items: [
    // -----------------------------
    // Planning
    // -----------------------------
    { id: 'PA1', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 20000, tps_min: 1200, tps_max: 2400, work_desc: 'Define mission goals and safety constraints for rock-hauling humanoid.' },
    { id: 'PA2', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 18000, tps_min: 1200, tps_max: 2400, work_desc: 'Draft system architecture: gait plan, payload target, torque budget.' },
    { id: 'PB1', group: 'P', sector: 'PLANNING', depends_on: [], estimate_ms: 16000, tps_min: 1000000, tps_max: 20000000, work_desc: 'Analyze mountain terrain; compile routes and incline profiles dataset.' },

    { id: 'PA3', group: 'P', sector: 'PLANNING', depends_on: ['PA1'], estimate_ms: 16000, tps_min: 12, tps_max: 22, work_desc: 'Build risk register: avalanche, rockfall, battery thermal runaway.' },
    { id: 'PA4', group: 'P', sector: 'PLANNING', depends_on: ['PA1'], estimate_ms: 15000, tps_min: 12, tps_max: 22, work_desc: 'Define success metrics & telemetry KPIs (time-to-summit, Wh/m, fault rate).' },
    { id: 'PA5', group: 'P', sector: 'PLANNING', depends_on: ['PB1'], estimate_ms: 12000, tps_min: 10, tps_max: 20, work_desc: 'Permits & land access: coordinate with park rangers and trail stewards.' },
    { id: 'PB2', group: 'P', sector: 'PLANNING', depends_on: ['PB1'], estimate_ms: 15000, tps_min: 10, tps_max: 20, work_desc: 'Create synthetic rock-shape/weight dataset via photogrammetry.' },
    { id: 'PB3', group: 'P', sector: 'PLANNING', depends_on: ['PA2'], estimate_ms: 14000, tps_min: 10, tps_max: 20, work_desc: 'BOM & budget; flag long-lead items and alternates.' },
    { id: 'PC1', group: 'P', sector: 'PLANNING', depends_on: ['PA1'], estimate_ms: 16000, tps_min: 12, tps_max: 22, work_desc: 'Define HRI & E‑stop protocols; operator roles and comms.' },
    { id: 'PC2', group: 'P', sector: 'PLANNING', depends_on: ['PA2'], estimate_ms: 14000, tps_min: 12, tps_max: 22, work_desc: 'Gait and terrain sim parameter sweep plan.' },
    { id: 'PD1', group: 'P', sector: 'PLANNING', depends_on: ['PA1'], estimate_ms: 13000, tps_min: 10, tps_max: 20, work_desc: 'Comms plan: base-camp radio net + LTE fallback.' },
    { id: 'PD2', group: 'P', sector: 'PLANNING', depends_on: ['PA2'], estimate_ms: 13000, tps_min: 12, tps_max: 22, work_desc: 'Cold‑weather ops plan: battery warmers, low-temp grease, seal choices.' },
    { id: 'PE1', group: 'P', sector: 'PLANNING', depends_on: ['PC1'], estimate_ms: 12000, tps_min: 10, tps_max: 20, work_desc: 'Operator training script & safety drills.' },
    { id: 'PE2', group: 'P', sector: 'PLANNING', depends_on: ['PA2', 'PB1'], estimate_ms: 15000, tps_min: 12, tps_max: 22, work_desc: 'Test matrix: ascent/descent scenarios and acceptance gates.' },
    { id: 'PF1', group: 'P', sector: 'PLANNING', depends_on: ['PB3'], estimate_ms: 12000, tps_min: 10, tps_max: 20, work_desc: 'Spare parts & field kit list with quantities.' },
    { id: 'PF2', group: 'P', sector: 'PLANNING', depends_on: ['PD1'], estimate_ms: 10000, tps_min: 10, tps_max: 20, work_desc: 'Narrative beats for docu-log; media checklist (for fun).' },

    // -----------------------------
    // Build branches
    // -----------------------------
    { id: 'BA1', group: 'B', sector: 'BUILD', depends_on: ['PA1'], estimate_ms: 22000, tps_min: 14, tps_max: 26, work_desc: 'Fabricate exoskeleton frame; assemble hip/shoulder joint modules.' },
    { id: 'BA2', group: 'B', sector: 'BUILD', depends_on: ['BA1'], estimate_ms: 20000, tps_min: 14, tps_max: 24, work_desc: 'Install actuators and motor drivers; verify stall torque on rig.' },
    { id: 'BB1', group: 'B', sector: 'BUILD', depends_on: ['PB1'], estimate_ms: 21000, tps_min: 12, tps_max: 22, work_desc: 'Prototype power pack and thermal spreaders for high-load climbs.' },
    { id: 'BB2', group: 'B', sector: 'BUILD', depends_on: ['BB1'], estimate_ms: 19000, tps_min: 12, tps_max: 22, work_desc: 'Implement power management firmware and brownout protections.' },
    { id: 'BC1', group: 'B', sector: 'BUILD', depends_on: ['PA2'], estimate_ms: 17000, tps_min: 12, tps_max: 20, work_desc: 'Integrate IMU, LiDAR, and foot force sensors; wire harness.' },

    { id: 'BA3', group: 'B', sector: 'BUILD', depends_on: ['PA2'], estimate_ms: 16000, tps_min: 14, tps_max: 24, work_desc: 'Design gripper and basket clamp for irregular rock shapes.' },
    { id: 'BA4', group: 'B', sector: 'BUILD', depends_on: ['BA1'], estimate_ms: 18000, tps_min: 14, tps_max: 26, work_desc: 'Assemble knee/ankle spring‑dampers; select bushings.' },
    { id: 'BA5', group: 'B', sector: 'BUILD', depends_on: ['BA1'], estimate_ms: 15000, tps_min: 12, tps_max: 22, work_desc: 'Carbon shrouds & seal kit for dust/water ingress.' },
    { id: 'BB3', group: 'B', sector: 'BUILD', depends_on: ['BB1'], estimate_ms: 18000, tps_min: 12, tps_max: 22, work_desc: 'Battery pack rev‑B; cold‑soak performance upgrades.' },
    { id: 'BB4', group: 'B', sector: 'BUILD', depends_on: ['BB1'], estimate_ms: 15000, tps_min: 12, tps_max: 22, work_desc: 'Integrate MPPT charger with foldable solar mats (field topping).' },
    { id: 'BC2', group: 'B', sector: 'BUILD', depends_on: ['BC1'], estimate_ms: 16000, tps_min: 12, tps_max: 20, work_desc: 'EMI shielding/grounding; cable routing & strain relief.' },
    { id: 'BC3', group: 'B', sector: 'BUILD', depends_on: ['BC1'], estimate_ms: 15000, tps_min: 12, tps_max: 20, work_desc: 'Toe force sensors redundant path; analog fallback.' },
    { id: 'BD1', group: 'B', sector: 'BUILD', depends_on: ['BA1'], estimate_ms: 17000, tps_min: 14, tps_max: 24, work_desc: 'Footpad design: cleat vs microspike; quick‑change soles.' },
    { id: 'BD2', group: 'B', sector: 'BUILD', depends_on: ['BA2'], estimate_ms: 18000, tps_min: 14, tps_max: 24, work_desc: 'Winch assist module for 45°+ pitches.' },
    { id: 'BE1', group: 'B', sector: 'BUILD', depends_on: ['BA2', 'BB2'], estimate_ms: 19000, tps_min: 14, tps_max: 26, work_desc: 'Thermal management: heatpipes & ducting around drivers.' },
    { id: 'BE2', group: 'B', sector: 'BUILD', depends_on: ['BC2'], estimate_ms: 16000, tps_min: 12, tps_max: 22, work_desc: 'Conformal coating & potting for electronics.' },
    { id: 'BF1', group: 'B', sector: 'BUILD', depends_on: ['PA2'], estimate_ms: 18000, tps_min: 14, tps_max: 26, work_desc: 'Gait controller v1 (ZMP/SLIP hybrid) with torque limits.' },
    { id: 'BF2', group: 'B', sector: 'BUILD', depends_on: ['BC1'], estimate_ms: 17000, tps_min: 12, tps_max: 22, work_desc: 'Sensor fusion & foot slip estimator (Kalman).' },
    { id: 'BG1', group: 'B', sector: 'BUILD', depends_on: ['BF1'], estimate_ms: 16000, tps_min: 12, tps_max: 22, work_desc: 'Fall detection + safe‑kneel routine.' },
    { id: 'BG2', group: 'B', sector: 'BUILD', depends_on: ['BA3'], estimate_ms: 15000, tps_min: 12, tps_max: 22, work_desc: 'Rock grasp strategy library (pinch, cradle, lash).' },
    { id: 'BH1', group: 'B', sector: 'BUILD', depends_on: ['PB2', 'BC1'], estimate_ms: 18000, tps_min: 12, tps_max: 22, work_desc: 'Vision terrain classifier (scree/slab/talus).' },
    { id: 'BH2', group: 'B', sector: 'BUILD', depends_on: ['BC1'], estimate_ms: 15000, tps_min: 12, tps_max: 22, work_desc: 'LiDAR snow/ice reflectance compensation.' },
    { id: 'BI1', group: 'B', sector: 'BUILD', depends_on: ['PD1', 'BC1'], estimate_ms: 14000, tps_min: 12, tps_max: 22, work_desc: 'Comms stack: mesh radios + LTE fallback.' },
    { id: 'BJ1', group: 'B', sector: 'BUILD', depends_on: ['PC1', 'BI1'], estimate_ms: 14000, tps_min: 12, tps_max: 22, work_desc: 'Teleop dashboard with joystick mapping and overlays.' },
    { id: 'BK1', group: 'B', sector: 'BUILD', depends_on: ['PA4'], estimate_ms: 12000, tps_min: 12, tps_max: 22, work_desc: 'Black‑box logging: circular buffer + SD card.' },
    { id: 'BL1', group: 'B', sector: 'BUILD', depends_on: ['BG1'], estimate_ms: 14000, tps_min: 12, tps_max: 22, work_desc: 'Self‑righting routine & torque‑limited push‑up.' },
    { id: 'BM1', group: 'B', sector: 'BUILD', depends_on: ['BB2'], estimate_ms: 13000, tps_min: 12, tps_max: 22, work_desc: 'Battery hot‑swap latch & interlock.' },
    { id: 'BN1', group: 'B', sector: 'BUILD', depends_on: ['PD2', 'BB2'], estimate_ms: 12000, tps_min: 12, tps_max: 22, work_desc: 'Toe heaters & pack warmers control.' },
    { id: 'BO1', group: 'B', sector: 'BUILD', depends_on: ['BA3'], estimate_ms: 12000, tps_min: 12, tps_max: 22, work_desc: 'Payload basket quick‑release & weight sensor.' },
    { id: 'BP1', group: 'B', sector: 'BUILD', depends_on: ['BA3'], estimate_ms: 13000, tps_min: 12, tps_max: 22, work_desc: 'Arm/hand compliance tuning; underactuated fingers.' },
    { id: 'BQ1', group: 'B', sector: 'BUILD', depends_on: ['PB1', 'BH1'], estimate_ms: 15000, tps_min: 12, tps_max: 22, work_desc: 'Onboard map caching & route planner module.' },
    { id: 'BR1', group: 'B', sector: 'BUILD', depends_on: ['BC1', 'BF1'], estimate_ms: 15000, tps_min: 12, tps_max: 22, work_desc: 'Wind gust compensation using torso IMU.' },
    { id: 'BS1', group: 'B', sector: 'BUILD', depends_on: ['BF1', 'BE1'], estimate_ms: 19000, tps_min: 14, tps_max: 26, work_desc: 'Energy‑optimal gait planner (MPC).' },
    { id: 'BT1', group: 'B', sector: 'BUILD', depends_on: ['BB2'], estimate_ms: 13000, tps_min: 12, tps_max: 22, work_desc: 'Firmware watchdogs & brownout recovery.' },
    { id: 'BU1', group: 'B', sector: 'BUILD', depends_on: ['BK1'], estimate_ms: 11000, tps_min: 12, tps_max: 20, work_desc: 'Diagnostics LCD & beeper; field error codes.' },
    { id: 'BV1', group: 'B', sector: 'BUILD', depends_on: ['BE2'], estimate_ms: 9000, tps_min: 12, tps_max: 20, work_desc: 'Cable management tidy pass; tie-downs & labels.' },
    { id: 'BW1', group: 'B', sector: 'BUILD', depends_on: ['BA5', 'BE2'], estimate_ms: 12000, tps_min: 12, tps_max: 20, work_desc: 'Ingress test tweaks toward IP54.' },
    { id: 'BX1', group: 'B', sector: 'BUILD', depends_on: ['BA2'], estimate_ms: 13000, tps_min: 14, tps_max: 24, work_desc: 'Motor driver autotune under payload.' },
    { id: 'BY1', group: 'B', sector: 'BUILD', depends_on: ['PB1', 'BF1'], estimate_ms: 14000, tps_min: 12, tps_max: 22, work_desc: 'Footstep planner constraints generated from incline profiles.' },
    { id: 'BZ1', group: 'B', sector: 'BUILD', depends_on: ['BD2'], estimate_ms: 11000, tps_min: 12, tps_max: 20, work_desc: 'Emergency rope anchor points (no parachutes, sadly).' },

    // -----------------------------
    // Eval fan-in
    // -----------------------------
    { id: 'EA1', group: 'E', sector: 'EVAL', depends_on: ['BA2', 'BB2'], estimate_ms: 15000, tps_min: 8, tps_max: 18, work_desc: 'Bench test chassis + power under load; measure thermal margins.' },
    { id: 'EA2', group: 'E', sector: 'EVAL', depends_on: ['BC1'], estimate_ms: 14000, tps_min: 8, tps_max: 16, work_desc: 'Calibrate sensors; validate sensor fusion on incline jig.' },
    { id: 'EB1', group: 'E', sector: 'EVAL', depends_on: ['EA1'], estimate_ms: 12000, tps_min: 8, tps_max: 16, work_desc: 'Field simulate ascent on treadmill with weighted rock basket.' },

    { id: 'EA3', group: 'E', sector: 'EVAL', depends_on: ['BA3'], estimate_ms: 12000, tps_min: 8, tps_max: 18, work_desc: 'Run end‑to‑end timed haul cycles; tune gait vs. payload.' },
    { id: 'EA4', group: 'E', sector: 'EVAL', depends_on: ['BF1', 'EA1'], estimate_ms: 12000, tps_min: 8, tps_max: 18, work_desc: 'Gait stability on uneven rocks; perturbation test.' },
    { id: 'EB2', group: 'E', sector: 'EVAL', depends_on: ['BB2', 'BN1'], estimate_ms: 12000, tps_min: 8, tps_max: 18, work_desc: 'Battery endurance with 15 kg payload; cold‑soak −5°C.' },
    { id: 'EC1', group: 'E', sector: 'EVAL', depends_on: ['BI1'], estimate_ms: 10000, tps_min: 8, tps_max: 16, work_desc: 'RF link range & dropout characterization on trail.' },
    { id: 'EC2', group: 'E', sector: 'EVAL', depends_on: ['BJ1', 'BT1'], estimate_ms: 11000, tps_min: 8, tps_max: 16, work_desc: 'E‑stop latency under load; brake hold verification.' },
    { id: 'ED1', group: 'E', sector: 'EVAL', depends_on: ['BD1'], estimate_ms: 10000, tps_min: 8, tps_max: 16, work_desc: 'Sole/tread swap tests across scree, slab, and talus.' },
    { id: 'ED2', group: 'E', sector: 'EVAL', depends_on: ['BD2'], estimate_ms: 11000, tps_min: 8, tps_max: 16, work_desc: 'Winch assist regression on steep treadmill profile.' },
    { id: 'EE1', group: 'E', sector: 'EVAL', depends_on: ['BQ1'], estimate_ms: 12000, tps_min: 8, tps_max: 18, work_desc: 'Route planner A/B vs human guide timings.' },
    { id: 'EE2', group: 'E', sector: 'EVAL', depends_on: ['BE1'], estimate_ms: 12000, tps_min: 8, tps_max: 18, work_desc: 'Thermal derate profile under sun + wind.' },
    { id: 'EF1', group: 'E', sector: 'EVAL', depends_on: ['BL1'], estimate_ms: 11000, tps_min: 8, tps_max: 16, work_desc: 'Self‑righting trials on padded slope.' },
    { id: 'EG1', group: 'E', sector: 'EVAL', depends_on: ['BK1', 'BT1'], estimate_ms: 12000, tps_min: 8, tps_max: 16, work_desc: 'Black‑box log integrity; fault injection.' },
    { id: 'EH1', group: 'E', sector: 'EVAL', depends_on: ['BG2', 'BO1'], estimate_ms: 12000, tps_min: 8, tps_max: 18, work_desc: 'Grasp success rate vs randomized basket loads.' },
    { id: 'EI1', group: 'E', sector: 'EVAL', depends_on: ['BH2'], estimate_ms: 10000, tps_min: 8, tps_max: 16, work_desc: 'Ice reflectance compensation field validation.' },
    { id: 'EJ1', group: 'E', sector: 'EVAL', depends_on: ['BR1'], estimate_ms: 11000, tps_min: 8, tps_max: 18, work_desc: 'High wind fan‑tunnel test; gust rejection.' },
    { id: 'EK1', group: 'E', sector: 'EVAL', depends_on: ['PE1', 'BJ1'], estimate_ms: 9000, tps_min: 8, tps_max: 16, work_desc: 'Operator usability dry‑run; SOP rehearsal.' },
    { id: 'EL1', group: 'E', sector: 'EVAL', depends_on: ['BS1', 'EA3'], estimate_ms: 12000, tps_min: 8, tps_max: 18, work_desc: 'Energy per meter vs spec; regression tracking.' },
    { id: 'EM1', group: 'E', sector: 'EVAL', depends_on: ['EA1', 'EG1'], estimate_ms: 15000, tps_min: 8, tps_max: 16, work_desc: 'Multi‑hour continuous run; MTBF snapshot.' },
    { id: 'EN1', group: 'E', sector: 'EVAL', depends_on: ['BI1', 'BG1', 'BT1'], estimate_ms: 12000, tps_min: 8, tps_max: 16, work_desc: 'Recovery drill: comms blackout → safe kneel → reboot.' },
    { id: 'EO1', group: 'E', sector: 'EVAL', depends_on: ['EA2', 'EB1'], estimate_ms: 10000, tps_min: 8, tps_max: 16, work_desc: 'Sensor calibration drift check after descent.' },
    { id: 'EP1', group: 'E', sector: 'EVAL', depends_on: ['BW1'], estimate_ms: 10000, tps_min: 8, tps_max: 16, work_desc: 'Ingress protection validation with mist+dust.' },
    { id: 'EQ1', group: 'E', sector: 'EVAL', depends_on: ['BN1', 'BB2'], estimate_ms: 10000, tps_min: 8, tps_max: 16, work_desc: 'Cold‑start test at dawn.' },
    { id: 'ER1', group: 'E', sector: 'EVAL', depends_on: ['BJ1', 'BF1'], estimate_ms: 9000, tps_min: 8, tps_max: 16, work_desc: 'Trail courtesy test: pause for hikers, resume smoothly.' },
    { id: 'ES1', group: 'E', sector: 'EVAL', depends_on: ['BZ1'], estimate_ms: 9000, tps_min: 8, tps_max: 16, work_desc: 'Rope anchor static load test.' },
    { id: 'ET1', group: 'E', sector: 'EVAL', depends_on: ['BY1', 'EA3'], estimate_ms: 10000, tps_min: 8, tps_max: 16, work_desc: 'Footstep planner performance vs incline dataset.' },
    { id: 'EU1', group: 'E', sector: 'EVAL', depends_on: ['BD1', 'EA3'], estimate_ms: 10000, tps_min: 8, tps_max: 16, work_desc: 'Snow patch crossing with microspikes.' },
    { id: 'EV1', group: 'E', sector: 'EVAL', depends_on: ['BF1', 'EA3'], estimate_ms: 11000, tps_min: 8, tps_max: 16, work_desc: 'Descending brake tests; toe/heel first policy.' },
    { id: 'EW1', group: 'E', sector: 'EVAL', depends_on: ['BC1', 'EA2'], estimate_ms: 11000, tps_min: 8, tps_max: 16, work_desc: 'IMU bias & LiDAR occlusion scenarios.' },
    { id: 'EX1', group: 'E', sector: 'EVAL', depends_on: ['PF2', 'BA5'], estimate_ms: 9000, tps_min: 8, tps_max: 16, work_desc: 'Media capture dry‑run; camera mounts stable for launch day?' },

    // -----------------------------
    // Deploy
    // -----------------------------
    { id: 'DA1', group: 'D', sector: 'DEPLOY', depends_on: ['EA1'], estimate_ms: 12000, tps_min: 8, tps_max: 14, work_desc: 'Prepare production build: fasteners, harnesses, and protective shells.' },
    { id: 'DA2', group: 'D', sector: 'DEPLOY', depends_on: ['EA2'], estimate_ms: 11000, tps_min: 8, tps_max: 14, work_desc: 'Stage charging dock and on-site tools at mountain base.' },
    { id: 'DB1', group: 'D', sector: 'DEPLOY', depends_on: ['EB1'], estimate_ms: 10000, tps_min: 8, tps_max: 14, work_desc: 'Finalize safety checklist and operator SOP for haul cycles.' },
    { id: 'DA3', group: 'D', sector: 'DEPLOY', depends_on: ['EA3'], estimate_ms: 9000, tps_min: 8, tps_max: 14, work_desc: 'Package, label, and ship final unit to the trailhead.' },

    { id: 'DB2', group: 'D', sector: 'DEPLOY', depends_on: ['PF1', 'DA1'], estimate_ms: 10000, tps_min: 8, tps_max: 14, work_desc: 'Assemble field kit (spares, tools, adhesives).' },
    { id: 'DC1', group: 'D', sector: 'DEPLOY', depends_on: ['DA3'], estimate_ms: 9000, tps_min: 8, tps_max: 14, work_desc: 'Vehicle load‑out and weight balance.' },
    { id: 'DC2', group: 'D', sector: 'DEPLOY', depends_on: ['PD1', 'DA2'], estimate_ms: 9000, tps_min: 8, tps_max: 14, work_desc: 'Scout team brief: routes, weather, comms.' },
    { id: 'DD1', group: 'D', sector: 'DEPLOY', depends_on: ['BB4', 'DA2'], estimate_ms: 10000, tps_min: 8, tps_max: 14, work_desc: 'Basecamp power: generator + solar mats.' },
    { id: 'DD2', group: 'D', sector: 'DEPLOY', depends_on: ['BI1', 'DA2'], estimate_ms: 9000, tps_min: 8, tps_max: 14, work_desc: 'Camp mesh network setup & test.' },
    { id: 'DE1', group: 'D', sector: 'DEPLOY', depends_on: ['EC2', 'EK1'], estimate_ms: 9000, tps_min: 8, tps_max: 14, work_desc: 'Safety officer sign‑off.' },
    { id: 'DF1', group: 'D', sector: 'DEPLOY', depends_on: ['PA5', 'DA3'], estimate_ms: 8000, tps_min: 8, tps_max: 14, work_desc: 'Permit check‑in with rangers.' },
    { id: 'DG1', group: 'D', sector: 'DEPLOY', depends_on: ['DB1', 'EK1'], estimate_ms: 9000, tps_min: 8, tps_max: 14, work_desc: 'Pre‑ascent checklist dry‑run with timer.' },
    { id: 'DH1', group: 'D', sector: 'DEPLOY', depends_on: ['EX1', 'DC2'], estimate_ms: 9000, tps_min: 8, tps_max: 14, work_desc: 'Public launch livestream (optional, for the story).' },
    { id: 'DI1', group: 'D', sector: 'DEPLOY', depends_on: ['EN1', 'DA2'], estimate_ms: 9000, tps_min: 8, tps_max: 14, work_desc: 'Stage rescue kit and med kit at switchback 3.' },
    { id: 'DJ1', group: 'D', sector: 'DEPLOY', depends_on: ['DA3'], estimate_ms: 8000, tps_min: 8, tps_max: 14, work_desc: 'Deploy trail signage: “Robots at work.”' },
    { id: 'DK1', group: 'D', sector: 'DEPLOY', depends_on: ['EA3', 'DA2'], estimate_ms: 10000, tps_min: 8, tps_max: 14, work_desc: 'Base loop dry‑run at mountain; 2× laps.' },
    { id: 'DL1', group: 'D', sector: 'DEPLOY', depends_on: ['DE1', 'DG1', 'DK1'], estimate_ms: 8000, tps_min: 8, tps_max: 14, work_desc: 'Go/No‑Go review.' },
    { id: 'DM1', group: 'D', sector: 'DEPLOY', depends_on: ['DL1', 'DC2'], estimate_ms: 9000, tps_min: 8, tps_max: 14, work_desc: 'Summit attempt: select start window.' },
    { id: 'DN1', group: 'D', sector: 'DEPLOY', depends_on: ['DM1'], estimate_ms: 9000, tps_min: 8, tps_max: 14, work_desc: 'Post‑run teardown & base debrief.' },
    { id: 'DO1', group: 'D', sector: 'DEPLOY', depends_on: ['DN1'], estimate_ms: 9000, tps_min: 8, tps_max: 14, work_desc: 'Data offload + log triage.' },
    { id: 'DP1', group: 'D', sector: 'DEPLOY', depends_on: ['DO1'], estimate_ms: 9000, tps_min: 8, tps_max: 14, work_desc: 'Postmortem write‑up & highlight reel.' },
    { id: 'DQ1', group: 'D', sector: 'DEPLOY', depends_on: ['DC2'], estimate_ms: 8000, tps_min: 8, tps_max: 14, work_desc: 'Procure extra snacks—operator morale matters.' },
    { id: 'DR1', group: 'D', sector: 'DEPLOY', depends_on: ['DN1'], estimate_ms: 8000, tps_min: 8, tps_max: 14, work_desc: 'Battery recycling & disposal compliance.' },
    { id: 'DS1', group: 'D', sector: 'DEPLOY', depends_on: ['DN1'], estimate_ms: 8000, tps_min: 8, tps_max: 14, work_desc: 'Thank‑you notes to rangers and volunteers.' },
  ],
};

export default testPlan;
```

## File: `plans/types.ts`
```typescript
// Plan types for defining human-readable project plans
import type { Sector } from '@/lib/constants';

export interface PlanItemSpec {
  id: string;            // e.g., 'A1'
  group: string;         // e.g., 'A', 'B', ...
  sector: Sector;        // 'Planning' | 'Build' | 'Eval' | 'Deploy'
  depends_on: string[];  // upstream item ids
  estimate_ms: number;   // target duration in ms
  tps_min: number;       // lower bound tokens/sec
  tps_max: number;       // upper bound tokens/sec
  // Optional work-order description: human text of what's being done
  work_desc?: string;
}

export interface PlanDefinition {
  name: string;
  description?: string;
  items: PlanItemSpec[];
  groups?: WorkGroupDef[]; // optional grouping metadata for items
}

export interface WorkGroupDef {
  id: string;          // e.g., 'P', 'B', 'E', 'D'
  title: string;       // human title for the group
  description: string; // human description for the group
}
```

## File: `public/fonts/source-code-pro/README.md`
```markdown
Place your font file here:

- Expected path: `public/fonts/source-code-pro/SourceCodePro-Regular.ttf`
- Used via `next/font/local` in `app/layout.tsx`
- Weight: 400, Style: normal

Tip: Prefer `.woff2` for best performance if available.

```

## File: `workers/engine.ts`
```typescript
// Engine worker: minimal handshake loop (snapshot + ticks)
// Exports tiny pure helpers for tests; only starts the loop when actually
// running in a WorkerGlobalScope (not during Vitest/jsdom imports).

import { DEFAULT_SEED, RUNNING_DEFAULT } from '../lib/config';
import { ENGINE_TICK_HZ, TPS_ALPHA, TPS_TARGET_HOLD_MS_MIN, TPS_TARGET_HOLD_MS_MAX, TPS_JITTER_FRAC } from '@/lib/constants';
import { debugLog } from '../lib/debug';
import { buildItemsFromPlan, detectCycles, promoteQueuedToAssigned, countInProgress, computeMetrics } from '@/lib/engine';
import { getPlanByName, ALL_PLANS, DEFAULT_PLAN_NAME } from '@/plans';
import { createRNG } from '@/lib/rng';
import { MAX_CONCURRENT } from '@/lib/constants';
import type { AppState, ProjectMetrics, Agent, WorkItem } from '../lib/types';

export const ENGINE_WORKER_MODULE_LOADED = true;

export type PlanName = string;

export function zeroMetrics(): ProjectMetrics {
  return {
    active_agents: 0,
    total_tokens: 0,
    total_spend_usd: 0,
    live_tps: 0,
    live_spend_per_s: 0,
    completion_rate: 0,
  };
}

export function makeInitialState(seed: string = DEFAULT_SEED): AppState {
  return {
    items: {},
    agents: {},
    metrics: zeroMetrics(),
    seed,
    running: RUNNING_DEFAULT,
  };
}

export function hzToMs(hz: number): number {
  return hz > 0 ? Math.round(1000 / hz) : 1000 / 30;
}

interface Ctx {
  state: AppState;
  tickId: number;
  running: boolean;
  speed: number; // multiplier (1x default)
  plan: PlanName;
  timer: any;
  tickMs: number;
  rng: ReturnType<typeof createRNG>;
  nextStartAt: number; // epoch ms for next start attempt
  agentCounter: number;
  lastTickAt: number;
}

function postSnapshot(ctx: Ctx) {
  debugLog('worker', 'postSnapshot', { running: ctx.running, tickId: ctx.tickId, seed: ctx.state.seed, plan: ctx.plan });
  ;(self as any).postMessage({ type: 'snapshot', state: ctx.state });
}


function expDelayMs(mean: number, rng: ReturnType<typeof createRNG>) {
  const u = Math.max(1e-6, rng.next());
  return -Math.log(1 - u) * mean;
}

function tryStartOne(ctx: Ctx, now: number, diffs: { items: Partial<WorkItem>[]; agents: Partial<Agent>[] }) {
  const inProg = countInProgress(ctx.state.items);
  if (inProg >= MAX_CONCURRENT) return false;

  const assigned = Object.values(ctx.state.items).filter((i) => i.status === 'assigned');
  if (assigned.length === 0) return false;
  // pick random assigned
  const pick = assigned[Math.floor(ctx.rng.next() * assigned.length)];
  const agentId = `AG${++ctx.agentCounter}`;
  const nowMs = now;
  // minimal agent (positions unused yet)
  ctx.state.agents[agentId] = { id: agentId, work_item_id: pick.id, x: 0, y: 0, v: 0.002, curve_phase: 0 } as Agent;
  pick.status = 'in_progress';
  pick.agent_id = agentId;
  pick.started_at = nowMs;
  // include minimal diffs
  diffs.items.push({ id: pick.id, status: 'in_progress', agent_id: agentId, started_at: nowMs });
  diffs.agents.push({ id: agentId, work_item_id: pick.id } as Partial<Agent>);
  debugLog('worker', 'start_item', { id: pick.id, agent: agentId });
  return true;
}

function stepEngine(ctx: Ctx) {
  const now = Date.now();
  const diffs: { items: Partial<WorkItem>[]; agents: Partial<Agent>[]; agents_remove?: string[] } = { items: [], agents: [] };
  // Simulation delta (seconds)
  const dtSec = Math.max(0, (now - ctx.lastTickAt) / 1000);
  ctx.lastTickAt = now;

  // Promote any newly eligible items
  const newlyAssigned = promoteQueuedToAssigned(ctx.state.items);
  for (const id of newlyAssigned) diffs.items.push({ id, status: 'assigned' });

  // Start cadence: Poisson-like with mean 800ms, obey cap
  if (ctx.running && now >= ctx.nextStartAt) {
    if (tryStartOne(ctx, now, diffs)) {
      // schedule next start
      const mean = 800 / ctx.speed;
      ctx.nextStartAt = now + Math.max(50, expDelayMs(mean, ctx.rng));
    } else {
      // nothing to start; check again soon
      ctx.nextStartAt = now + 300;
    }
  }

  // Per-item TPS target state (held targets to create bursty behavior)
  type TpsState = { target: number; nextAt: number };
  // Keep this map across ticks by hoisting to module scope; fall back to a property on ctx
  // to avoid redeclaring across calls in certain bundlers.
  const tpsMap: Map<string, TpsState> = (stepEngine as any)._tpsMap || new Map<string, TpsState>();
  (stepEngine as any)._tpsMap = tpsMap;

  // Update in-progress items
  for (const it of Object.values(ctx.state.items)) {
    if (it.status !== 'in_progress') {
      // cleanup any lingering state when item leaves in_progress
      if ((it.status === 'done' || it.status === 'queued' || it.status === 'assigned') && tpsMap.has(it.id)) tpsMap.delete(it.id);
      continue;
    }

    // Sample/hold target for a burst window
    let st = tpsMap.get(it.id);
    if (!st || now >= st.nextAt) {
      const range = Math.max(0, it.tps_max - it.tps_min);
      const baseTarget = it.tps_min + range * ctx.rng.next();
      // Hold window scaled by speed so faster sims don't feel too stable
      const holdMs = (TPS_TARGET_HOLD_MS_MIN + (TPS_TARGET_HOLD_MS_MAX - TPS_TARGET_HOLD_MS_MIN) * ctx.rng.next()) / Math.max(0.0001, ctx.speed || 1);
      st = { target: baseTarget, nextAt: now + Math.max(100, Math.floor(holdMs)) };
      tpsMap.set(it.id, st);
    }

    // Small flutter around the held target
    const range = Math.max(0, it.tps_max - it.tps_min);
    const jitterAmp = TPS_JITTER_FRAC * range;
    const jitter = (ctx.rng.next() * 2 - 1) * jitterAmp;
    const targetEffective = Math.max(it.tps_min, Math.min(it.tps_max, st.target + jitter));

    // Exponential smoothing toward target to avoid instant jumps
    const prev = Number.isFinite(it.tps as number) ? (it.tps as number) : it.tps_min;
    let tps = (1 - TPS_ALPHA) * prev + TPS_ALPHA * targetEffective;
    if (!Number.isFinite(tps)) tps = it.tps_min;
    tps = Math.max(it.tps_min, Math.min(it.tps_max, tps));
    it.tps = tps;
    // accumulate tokens
    it.tokens_done += tps * dtSec;
    if (!Number.isFinite(it.tokens_done)) it.tokens_done = 0;
    // eta by elapsed time
    const started = it.started_at ?? now;
    // ETA based on real elapsed wall time
    it.eta_ms = Math.max(0, it.estimate_ms - (now - started));
    diffs.items.push({ id: it.id, tps: it.tps, tokens_done: it.tokens_done, eta_ms: it.eta_ms });
    // completion
    if (it.eta_ms <= 0) {
      it.status = 'done';
      // cleanup state on completion
      if (tpsMap.has(it.id)) tpsMap.delete(it.id);
      const agentId = it.agent_id;
      it.agent_id = undefined;
      diffs.items.push({ id: it.id, status: 'done', agent_id: undefined });
      if (agentId && (ctx.state.agents as any)[agentId]) {
        delete (ctx.state.agents as any)[agentId];
        (diffs.agents_remove ||= []).push(agentId);
      }
    }
  }
  return diffs;
}

function postTick(ctx: Ctx) {
  // apply engine step to build diffs
  const diffs = stepEngine(ctx);
  // metrics
  const metrics = computeMetrics(ctx.state.items as any, ctx.state.agents as any);
  ctx.state.metrics = metrics;
  ctx.tickId += 1;
  debugLog('worker', 'postTick', { tickId: ctx.tickId, items: diffs.items.length, agents: diffs.agents.length, agents_remove: diffs.agents_remove?.length ?? 0 });
  (self as any).postMessage({ type: 'tick', tick_id: ctx.tickId, items: diffs.items.length ? diffs.items : undefined, agents: diffs.agents.length ? diffs.agents : undefined, agents_remove: diffs.agents_remove && diffs.agents_remove.length ? diffs.agents_remove : undefined, metrics });
}


function startLoop(ctx: Ctx) {
  if (ctx.timer) return;
  debugLog('worker', 'startLoop', { tickMs: ctx.tickMs });
  ctx.timer = setInterval(() => {
    if (!ctx.running) return;
    postTick(ctx);
  }, ctx.tickMs);
}

function stopLoop(ctx: Ctx) {
  if (!ctx.timer) return;
  debugLog('worker', 'stopLoop');
  clearInterval(ctx.timer);
  ctx.timer = null;
}

function loadPlan(ctx: Ctx, name: PlanName) {
  // Choose plan by name from registry (fallback to first available)
  const planDef = getPlanByName(name) ?? ALL_PLANS[0];
  const items = buildItemsFromPlan(planDef);
  const cycles = detectCycles(items);
  if (cycles.length) debugLog('worker', 'plan-cycles-detected', { count: cycles.length });
  // Promote initial eligible (no deps) to assigned
  promoteQueuedToAssigned(items);
  ctx.state.items = items;
  ctx.plan = name;
}

function handleIntent(ctx: Ctx, intent: any) {
  switch (intent?.type) {
    case 'set_running': {
      ctx.running = !!intent.running;
      ctx.state.running = ctx.running; // keep snapshot state in sync
      debugLog('worker', 'intent:set_running', { running: ctx.running });
      if (ctx.running) startLoop(ctx); else stopLoop(ctx);
      // Echo state so UI reflects running flag
      postSnapshot(ctx);
      return;
    }
    case 'set_seed': {
      ctx.state.seed = String(intent.seed ?? DEFAULT_SEED);
      // Re-seed RNG and reset start scheduling for determinism
      ctx.rng = createRNG(ctx.state.seed);
      ctx.nextStartAt = Date.now();
      ctx.agentCounter = 0;
      debugLog('worker', 'intent:set_seed', { seed: ctx.state.seed });
      postSnapshot(ctx);
      return;
    }
    case 'set_plan': {
      const name = (intent.plan as PlanName) ?? DEFAULT_PLAN_NAME;
      debugLog('worker', 'intent:set_plan', { plan: name });
      // Load items from plan and pause so user can inspect
      loadPlan(ctx, name);
      ctx.running = false;
      ctx.state.running = false;
      stopLoop(ctx);
      postSnapshot(ctx);
      return;
    }
    case 'set_speed': {
      const s = Number(intent.speed);
      ctx.speed = Number.isFinite(s) && s > 0 ? s : 1;
      debugLog('worker', 'intent:set_speed', { speed: ctx.speed });
      return;
    }
    case 'request_snapshot': {
      debugLog('worker', 'intent:request_snapshot');
      postSnapshot(ctx);
      return;
    }
    default:
      return;
  }
}

function makeCtx(): Ctx {
  return {
    state: makeInitialState(DEFAULT_SEED),
    tickId: 0,
    running: RUNNING_DEFAULT,
    speed: 1,
    plan: DEFAULT_PLAN_NAME,
    timer: null,
    tickMs: hzToMs(ENGINE_TICK_HZ),
    rng: createRNG(DEFAULT_SEED),
    nextStartAt: Date.now(),
    agentCounter: 0,
    lastTickAt: Date.now(),
  };
}

// Detect dedicated worker context without relying on instanceof (not available across browsers)
const IS_DEDICATED_WORKER = typeof self !== 'undefined' && typeof (self as any).postMessage === 'function' && typeof (globalThis as any).window === 'undefined';
debugLog('worker', 'bootstrap', { isDedicatedWorker: IS_DEDICATED_WORKER, ENGINE_TICK_HZ });

if (IS_DEDICATED_WORKER) {
  const ctx = makeCtx();
  // Preload default plan so snapshot includes items for inspection
  loadPlan(ctx, DEFAULT_PLAN_NAME);
  // Post initial snapshot immediately so UI can latch onto state
  postSnapshot(ctx);
  // Start ticking if running by default
  if (ctx.running) startLoop(ctx);

  self.addEventListener('message', (event: MessageEvent) => {
    debugLog('worker', 'message', { data: (event as any).data });
    handleIntent(ctx, (event as any).data);
  });
}
```

## File: `workers/engine.worker.test.ts`
```typescript
import { describe, it, expect } from 'vitest';
import { makeInitialState, hzToMs, zeroMetrics } from './engine';

describe('engine-handshake helpers', () => {
  it('makes an initial state with zeros and defaults', () => {
    const s = makeInitialState('seed');
    expect(s.seed).toBe('seed');
    expect(s.items).toEqual({});
    expect(s.agents).toEqual({});
    expect(s.metrics).toEqual(zeroMetrics());
  });

  it('converts Hz to ms reasonably', () => {
    expect(hzToMs(50)).toBeGreaterThan(0);
    expect(hzToMs(25)).toBeCloseTo(40, 0);
  });
});
```


---
id: pattern
type: knowledge
owner: OA_Triage
---
# pattern
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "pattern-craft",
  "author": "Megh",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "postbuild": "next-sitemap",
    "lint": "next lint"
  },
  "dependencies": {
    "@radix-ui/react-slot": "^1.2.4",
    "@radix-ui/react-tabs": "^1.1.13",
    "@vercel/analytics": "^2.0.1",
    "@vercel/speed-insights": "^2.0.0",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "geist": "^1.7.0",
    "lucide-react": "^0.577.0",
    "next": "^16.1.6",
    "next-sitemap": "^4.2.3",
    "next-themes": "^0.4.6",
    "react": "^19.2.4",
    "react-dom": "^19.2.4",
    "react-qr-code": "^2.0.18",
    "sonner": "^2.0.7",
    "tailwind-merge": "^3.5.0"
  },
  "devDependencies": {
    "@eslint/eslintrc": "^3",
    "@tailwindcss/postcss": "^4",
    "@types/node": "^25",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "eslint": "^10",
    "eslint-config-next": "16.1.6",
    "tailwindcss": "^4",
    "tw-animate-css": "^1.4.0",
    "typescript": "^5"
  }
}

```

### File: README.md
```md
<!-- # Pattern Craft -->

> _**For developers, by a developer. Design that slaps⚡**_

<div align="center">
  <img src="./public/images/readme-banner.png" alt="Pattern Craft Banner" />
  <br><br>
  <p align="left">
    <strong>Effortlessly enhance your websites and apps with 100+ modern CSS background patterns and gradient snippets.</strong>
    Instantly copy and paste beautifully crafted, production-ready designs built with modern CSS and Tailwind CSS for seamless integration.<br>
    </br>
    <em>Ideal for developers and designers working with React, Next.js, Vue, Angular, or any modern frontend framework. Made for devs who appreciate great design.</em>
    </br>
  </p>
  <br>
  <p align="center">
    <img src="https://img.shields.io/github/stars/megh-bari/pattern-craft?style=social" alt="GitHub stars" />
<img src="https://img.shields.io/github/forks/megh-bari/pattern-craft?style=social" alt="GitHub forks" />
<img src="https://img.shields.io/github/license/megh-bari/pattern-craft?style=social" alt="License" />
<a href="https://vercel.com/oss">
    <img src="https://img.shields.io/badge/Sponsored%20by-Vercel-000000?style=social&logo=vercel&logoColor=black" alt="Sponsored by Vercel" />
</a>
    
  </p>
</div>

---

> **This project is proudly sponsored by [Vercel](https://vercel.com/oss). Thank you for supporting open source!**

  <!-- <p align="center">
<a href="https://vercel.com/oss">
<img src="https://www.datocms-assets.com/31049/1618983297-powered-by-vercel.svg" alt="Powered by Vercel" height="40">
</a>
</p> -->

<br />
<a href="https://vercel.com/oss">
  <img alt="Vercel OSS Program" src="https://vercel.com/oss/program-badge.svg" />
</a>

## Visit: **[Pattern Craft](https://patterncraft.fun)**

![UI Image](./public/images/readme-img-one.png)
![UI Image](./public/images/readme-img-two.png)
![UI Image](./public/images/readme-img-four.png)
![UI Image](./public/images/readme-img-three.png)

> _**Note: This project does not provide plain HTML or vanilla CSS snippets. All code is optimized for JSX (React/Next.js) and Tailwind CSS.**_  
> [Learn more in this announcement.](https://github.com/megh-bari/pattern-craft/discussions/24)

## Pattern Craft in the Wild!!!

<p align="left"> 
Curious where Pattern Craft is getting featured, shared, talk about or appreciated? 
</br>
Check out this growing list of shoutouts, showcases, and love from the community:  
</br>

⚡[**Where Pattern Craft is Making Noise??**](https://patterncraft.notion.site/Where-Pattern-Craft-is-Making-Noise-23bf940b4137803ea79bf3606acdb317?pvs=74)

</p>

## Features

- **Ready-to-use CSS code** - Copy and paste directly into your projects
- **Live preview** - See patterns in action before implementation
- **Modern design** - Crafted with contemporary CSS techniques and Tailwind CSS
- **Responsive patterns** - Optimized for all screen sizes
- **Zero dependencies** - Pure CSS implementations
- **Pattern categories** - Organized collection for easy browsing
- **Return back to scroll** - Smooth navigation experience
- **Add to favorites** - Save your preferred patterns
- **Customizable snippets** - Easily modify patterns to fit your needs

## Tech Stack

- **Next.js 14** - React framework with App Router
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first CSS framework
- **Vercel** - Deployment and hosting

## Sponsored by <a href="https://vercel.com/oss">Vercel⚡</a>

**This project is proudly powered by <b>Vercel</b>. The platform behind PatternCraft’s blazing-fast deployment and seamless scalability.**<br>

<i>Big thanks to Vercel for supporting open source and keeping this project running smoothly!</i>
<br><br>
<a href="https://vercel.com/oss">
<img src="https://www.datocms-assets.com/31049/1618983297-powered-by-vercel.svg" alt="Powered by Vercel" height="40">
</a>

</p>

## Getting Started

### Prerequisites

- Node.js 18+
- npm, yarn, pnpm, or bun

### Installation

1. Clone the repository:

```bash
git clone https://github.com/megh-bari/pattern-craft.git
cd pattern-craft
```

2. Install dependencies:

```bash
npm install
# or
yarn install
# or
pnpm install
```

3. Run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser

### Build for Production

```bash
npm run build
npm start
```

## How to Use This

1. Visit the live site: **[https://patterncraft.fun](https://pattern-craft.vercel.app/)**
2. Browse through the collection of background patterns and gradients.
3. Click on any pattern to open its preview modal.
4. Copy the CSS/Tailwind-compatible code snippet.
5. Paste it into your project wherever needed — it's responsive, clean, and ready to go!

These snippets work great for:

- Hero sections
- Landing pages
- Cards and sections
- Background art

## Demo

[Watch the demo video](https://github.com/user-attachments/assets/d414c57b-128b-43f2-8534-352bc93eb801)

## Customization

### Manual Pattern Customization

You can easily customize any background pattern by modifying the pattern object structure. Each pattern follows this format:

```typescript
{
  id: "unique-pattern-id",
  name: "Pattern Display Name",
  badge: "New",
  style: {
    background: "#ffffff",
    backgroundImage: `
      // Your CSS background patterns here
      linear-gradient(to right, #f0f0f0 1px, transparent 1px),
      radial-gradient(circle 800px at 100% 200px, #d5c5ff, transparent)
    `,
    backgroundSize: "96px 64px, 100% 100%",
  },
  code: `<div className="min-h-screen w-full bg-white relative">
  {/* Pattern Name Background */}
  <div
    className="absolute inset-0 z-0"
    style={{
      backgroundImage: \`
        // Your background image styles
      \`,
      backgroundSize: "96px 64px, 100% 100%",
    }}
  />
  {/* Your Content/Components */}
</div>`,
}
```

### Customization Tips

**Colors**: Change hex values in `backgroundImage` gradients
**Sizing**: Modify `backgroundSize` values for different scales
**Positioning**: Adjust gradient positions and directions
**Effects**: Add multiple background layers for complex patterns

### Example Customization

```typescript
// Original pattern
backgroundImage: `linear-gradient(to right, #f0f0f0 1px, transparent 1px)`;

// Customized version
backgroundImage: `linear-gradient(to right, #3b82f6 1px, transparent 1px)`; // Blue lines
backgroundSize: "48px 32px"; // Smaller grid
```

## Usage

1. Browse the pattern collection on the website
2. Click on any pattern to see the live preview
3. Use the "Add to Favorites" feature to save patterns you like
4. Copy the generated CSS code
5. Paste it into your project

Each pattern includes:

- Complete CSS styling
- Tailwind-compatible code
- Responsive implementation
- Cross-browser compatibility

## Contributing

> **This project is sponsored by Vercel, which helps us maintain a stable development environment.**

We welcome contributions to expand the pattern collection. To add new patterns:

### Adding New Patterns

1. Fork the repository
2. Create a feature branch:

```bash
git checkout -b feature/new-pattern-name
```

3. Navigate to `src/data/patterns.ts`
4. Add your pattern following the established format:

```typescript
{
  id: "unique-pattern-id",
  name: "Pattern Display Name",
  category: "gradients" | "geometric" | "decorative" | "effects",
  badge: "New", // Optional: "New"
  style: {
    background: "#ffffff",
    backgroundImage: `
      // Your CSS background patterns here
      linear-gradient(to right, #f0f0f0 1px, transparent 1px),
      radial-gradient(circle 800px at 100% 200px, #d5c5ff, transparent)
    `,
    backgroundSize: "96px 64px, 100% 100%",
  },
  code: `<div className="min-h-screen w-full bg-white relative">
  {/* Pattern Name Background */}
  <div
    className="absolute inset-0 z-0"
    style={{
      backgroundImage: \`
        // Your background image styles
      \`,
      backgroundSize: "96px 64px, 100% 100%",
    }}
  />
  {/* Your Content/Components */}
</div>`,
}
```

### Contribution Guidelines

- **Consistency**: Follow the existing pattern structure exactly
- **Naming**: Use descriptive, kebab-case IDs and proper display names
- **Quality**: Ensure patterns are visually appealing and professional
- **Performance**: Optimize for rendering performance
- **Responsiveness**: Test patterns across different screen sizes
- **Uniqueness**: Avoid duplicating existing patterns

### Pattern Categories

Consider these categories when adding patterns:

- **Gradient** - Color transitions and blends
- **Geometric** - Grids, dots, lines, shapes
- **Decorative** - Subtle background textures
- **Effects** - Clean and simple designs

### Testing Your Patterns

1. Test the pattern in the development environment
2. Verify responsive behavior
3. Check browser compatibility (Chrome, Firefox, Safari, Edge)
4. Ensure code validity and formatting

### Pull Request Process

1. Commit your changes with descriptive messages
2. Push to your feature branch
3. Create a pull request with:
   - Clear description of the pattern added
   - Screenshots or preview of the pattern
   - Any special considerations or notes

```bash
git add .
git commit -m "feat: add new geometric grid pattern"
git push origin feature/new-pattern-name
```

## Development

### Project Structure

```
pattern-craft/
src/
├── app/
│   ├── globals.css
│   ├── layout.tsx
│   ├── page.tsx
│   └── not-found.tsx
│
├── components/
│   ├── ui/                # shadcn/ui components
│   │   ├── badge.tsx
│   │   ├── button.tsx
│   │   └── tabs.tsx
│   ├── layout/
│   │   ├── navbar.tsx
│   │   └── footer.tsx
│   ├── patterns/
│   │   ├── pattern-showcase.tsx
│   │   ├── pattern-card.tsx
│   │   ├── pattern-grid.tsx
│   │   └── pattern-empty-state.tsx
│   ├── home/
│   │   ├── hero.tsx
│   │   ├── support-dropdown.tsx
│   │   └── return-to-preview.tsx
│   └── providers/
│       └── theme-provider.tsx
│
├── lib/
│   ├── utils.ts
│   └── constants.ts
│
├── hooks/
│   ├── useTheme.tsx
│   └── useCopy.tsx
│
├── types/
│   ├── pattern.ts
│   └── index.ts
│
├── context/
│   └── favourites-context.tsx
│
└── data/
    ├── patterns.ts        # Pattern used in UI (contribute here)
    └── categories.ts
```

### Code Standards

- Use TypeScript for type safety
- Follow ESLint and Prettier configurations
- Maintain consistent code formatting
- Use semantic commit messages

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Built with Next.js and Tailwind CSS
- Inspired by modern web design patterns
- Community-driven pattern collection

## Support

For questions, issues, or suggestions:

- Open an issue on GitHub
- Check existing issues before creating new ones
- Provide detailed information for bug reports

## Built By

- Twitter(X): [@meghtrix](https://x.com/meghtrix)
- Alternate Twitter(X): [@usepatterncraft](https://x.com/usepatterncraft)
- GitHub: [@megh-bari](https://github.com/megh-bari)

If you like this project, consider giving it a ⭐️ on GitHub and sharing it with others!

>This project is proudly supported by:

<a href="https://vercel.com/oss">
  <img alt="Vercel OSS Program" src="https://vercel.com/oss/program-badge.svg" />
</a>

## Star History

<a href="https://www.star-history.com/#megh-bari/pattern-craft&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=megh-bari/pattern-craft&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=megh-bari/pattern-craft&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=megh-bari/pattern-craft&type=Date" />
 </picture>
</a>

---

> _**Happy coding!**_

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
    "baseColor": "slate",
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

### File: next-sitemap.config.js
```js
/** @type {import('next-sitemap').IConfig} */
module.exports = {
  siteUrl: 'https://patterncraft.fun',
  generateRobotsTxt: true,
  generateIndexSitemap: false,
  exclude: [
    '/api/*',
    '/admin/*',
    '/private/*',
    '/_next/*',
    '/404',
    '/500',
  ],
  changefreq: 'weekly', 
  priority: 0.7,        
  trailingSlash: false,
  sourceMap: false,
};
```

### File: next.config.ts
```ts
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
};

export default nextConfig;

```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2017",
    "lib": [
      "dom",
      "dom.iterable",
      "esnext"
    ],
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
      "@/*": [
        "./src/*"
      ]
    }
  },
  "include": [
    "next-env.d.ts",
    "**/*.ts",
    "**/*.tsx",
    ".next/types/**/*.ts",
    ".next/dev/types/**/*.ts"
  ],
  "exclude": [
    "node_modules"
  ]
}

```

### File: public\robots.txt
```txt
# *
User-agent: *
Allow: /

# Host
Host: https://patterncraft.fun

# Sitemaps
Sitemap: https://patterncraft.fun/sitemap.xml

```

### File: src\app\globals.css
```css
@tailwindcss;
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

:root {
  --radius: 0.625rem;
  --background: oklch(1 0 0);
  --foreground: oklch(0.129 0.042 264.695);
  --card: oklch(1 0 0);
  --card-foreground: oklch(0.129 0.042 264.695);
  --popover: oklch(1 0 0);
  --popover-foreground: oklch(0.129 0.042 264.695);
  --primary: oklch(0.208 0.042 265.755);
  --primary-foreground: oklch(0.984 0.003 247.858);
  --secondary: oklch(0.968 0.007 247.896);
  --secondary-foreground: oklch(0.208 0.042 265.755);
  --muted: oklch(0.968 0.007 247.896);
  --muted-foreground: oklch(0.554 0.046 257.417);
  --accent: oklch(0.968 0.007 247.896);
  --accent-foreground: oklch(0.208 0.042 265.755);
  --destructive: oklch(0.577 0.245 27.325);
  --border: oklch(0.929 0.013 255.508);
  --input: oklch(0.929 0.013 255.508);
  --ring: oklch(0.704 0.04 256.788);
  --chart-1: oklch(0.646 0.222 41.116);
  --chart-2: oklch(0.6 0.118 184.704);
  --chart-3: oklch(0.398 0.07 227.392);
  --chart-4: oklch(0.828 0.189 84.429);
  --chart-5: oklch(0.769 0.188 70.08);
  --sidebar: oklch(0.984 0.003 247.858);
  --sidebar-foreground: oklch(0.129 0.042 264.695);
  --sidebar-primary: oklch(0.208 0.042 265.755);
  --sidebar-primary-foreground: oklch(0.984 0.003 247.858);
  --sidebar-accent: oklch(0.968 0.007 247.896);
  --sidebar-accent-foreground: oklch(0.208 0.042 265.755);
  --sidebar-border: oklch(0.929 0.013 255.508);
  --sidebar-ring: oklch(0.704 0.04 256.788);
}

.dark {
  --background: oklch(0.129 0.042 264.695);
  --foreground: oklch(0.984 0.003 247.858);
  --card: oklch(0.208 0.042 265.755);
  --card-foreground: oklch(0.984 0.003 247.858);
  --popover: oklch(0.208 0.042 265.755);
  --popover-foreground: oklch(0.984 0.003 247.858);
  --primary: oklch(0.929 0.013 255.508);
  --primary-foreground: oklch(0.208 0.042 265.755);
  --secondary: oklch(0.279 0.041 260.031);
  --secondary-foreground: oklch(0.984 0.003 247.858);
  --muted: oklch(0.279 0.041 260.031);
  --muted-foreground: oklch(0.704 0.04 256.788);
  --accent: oklch(0.279 0.041 260.031);
  --accent-foreground: oklch(0.984 0.003 247.858);
  --destructive: oklch(0.704 0.191 22.216);
  --border: oklch(1 0 0 / 10%);
  --input: oklch(1 0 0 / 15%);
  --ring: oklch(0.551 0.027 264.364);
  --chart-1: oklch(0.488 0.243 264.376);
  --chart-2: oklch(0.696 0.17 162.48);
  --chart-3: oklch(0.769 0.188 70.08);
  --chart-4: oklch(0.627 0.265 303.9);
  --chart-5: oklch(0.645 0.246 16.439);
  --sidebar: oklch(0.208 0.042 265.755);
  --sidebar-foreground: oklch(0.984 0.003 247.858);
  --sidebar-primary: oklch(0.488 0.243 264.376);
  --sidebar-primary-foreground: oklch(0.984 0.003 247.858);
  --sidebar-accent: oklch(0.279 0.041 260.031);
  --sidebar-accent-foreground: oklch(0.984 0.003 247.858);
  --sidebar-border: oklch(1 0 0 / 10%);
  --sidebar-ring: oklch(0.551 0.027 264.364);
}

@layer base {
  * {
    @apply border-border outline-ring/50;
  }
  body {
    @apply bg-background text-foreground;
  }
}

html {
  overflow: -moz-scrollbars-none;
  scrollbar-width: none;
  -ms-overflow-style: none;
}

html::-webkit-scrollbar {
  width: 0px;
  background: transparent;
}

body {
  overflow-x: hidden;
}

```

### File: src\data\categories.ts
```ts
import { PATTERN_CATEGORIES } from "@/lib/constants";

export const categories = PATTERN_CATEGORIES;

export type CategoryId = (typeof PATTERN_CATEGORIES)[number]["id"];

```

### File: src\lib\constants.ts
```ts
export const PATTERN_CATEGORIES = [
  { id: "all", label: "All Patterns" },
  { id: "gradients", label: "Gradients" },
  { id: "geometric", label: "Geometric" },
  { id: "decorative", label: "Decorative" },
  { id: "effects", label: "Effects" },
  { id: "favourites", label: "Favourites" },
] as const;

export const THEME_CONFIG = {
  light: "light",
  dark: "dark",
} as const;

export const SUPPORT_CONFIG = {
  UPI_ID: "barimegh21@okaxis",
  PAYEE_NAME: "Megh Bari",
  UPI_MSG: "Keep building cool stuff!",
  BUY_ME_COFFEE_URL: "https://coff.ee/meghdev",
  PAYPAL_URL: "https://www.paypal.com/paypalme/meghbari01",
} as const;

export const APP_CONFIG = {
  GITHUB_URL: "https://github.com/megh-bari/pattern-craft",
  TWITTER_URL: "https://twitter.com/meghtrix",
  CONTRIBUTING_URL: "https://github.com/megh-bari/pattern-craft#contributing",
} as const;

```

### File: src\lib\utils.ts
```ts
/* eslint-disable @typescript-eslint/no-explicit-any */
import { Pattern } from "@/types/pattern";
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export function debounce<T extends any[]>(
  fn: (...args: T) => any,
  timeout: number
) {
  let handle: NodeJS.Timeout;

  return function (...args: T) {
    clearTimeout(handle);
    handle = setTimeout(() => {
      fn(...args);
    }, timeout);
  };
}

export function searchPatterns(
  gridPatterns: Pattern[],
  category: string,
  searchInput: string
) {
  if (searchInput === "") return gridPatterns;

  const loweredInput = searchInput.toLowerCase();

  const inputWords = loweredInput.split(" ").filter(Boolean);

  const filteredPatterns = gridPatterns.filter((pattern) => {
    if (pattern.category === category || category === "all") {
      const patternWords = pattern.name.toLowerCase().split(" ");

      if (inputWords.length === 1 && inputWords[0].length === 1) {
        return patternWords[0].startsWith(inputWords[0]);
      }

      return inputWords.every((inputWord) =>
        patternWords.some((patternWord) => patternWord.startsWith(inputWord))
      );
    } else {
      return false;
    }
  });

  const sortedPatterns = filteredPatterns.sort((a, b) => {
    const aName = a.name.toLowerCase();
    const bName = b.name.toLowerCase();

    const posInA = aName.indexOf(inputWords[0]);
    const posInB = bName.indexOf(inputWords[0]);

    return posInA - posInB;
  });

  return sortedPatterns;
}

```

### File: src\types\index.ts
```ts
export * from "./pattern";

```

### File: src\types\pattern.ts
```ts
import type { CSSProperties } from "react";

export interface Pattern {
  id: string;
  name: string;
  category: "gradients" | "geometric" | "decorative" | "effects";
  description?: string;
  badge?: "New" | " ";
  style: CSSProperties;
  code: string;
}

```


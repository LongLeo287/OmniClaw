---
id: open-lovable
type: knowledge
owner: OA_Triage
---
# open-lovable
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "open-lovable",
  "version": "0.1.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "next dev --turbopack",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "test:api": "node tests/api-endpoints.test.js",
    "test:code": "node tests/code-execution.test.js",
    "test:all": "npm run test:integration && npm run test:api && npm run test:code"
  },
  "dependencies": {
    "@ai-sdk/anthropic": "^2.0.1",
    "@ai-sdk/google": "^2.0.4",
    "@ai-sdk/groq": "^2.0.0",
    "@ai-sdk/openai": "^2.0.4",
    "@anthropic-ai/sdk": "^0.57.0",
    "@e2b/code-interpreter": "^2.0.0",
    "@mendable/firecrawl-js": "^4.3.3",
    "@radix-ui/react-accordion": "^1.2.12",
    "@radix-ui/react-alert-dialog": "^1.1.15",
    "@radix-ui/react-aspect-ratio": "^1.1.7",
    "@radix-ui/react-avatar": "^1.1.10",
    "@radix-ui/react-checkbox": "^1.3.3",
    "@radix-ui/react-collapsible": "^1.1.12",
    "@radix-ui/react-context-menu": "^2.2.16",
    "@radix-ui/react-dialog": "^1.1.15",
    "@radix-ui/react-dropdown-menu": "^2.1.16",
    "@radix-ui/react-hover-card": "^1.1.15",
    "@radix-ui/react-label": "^2.1.7",
    "@radix-ui/react-menubar": "^1.1.16",
    "@radix-ui/react-navigation-menu": "^1.2.14",
    "@radix-ui/react-popover": "^1.1.15",
    "@radix-ui/react-progress": "^1.1.7",
    "@radix-ui/react-radio-group": "^1.3.8",
    "@radix-ui/react-scroll-area": "^1.2.10",
    "@radix-ui/react-select": "^2.2.6",
    "@radix-ui/react-separator": "^1.1.7",
    "@radix-ui/react-slider": "^1.3.6",
    "@radix-ui/react-slot": "^1.2.3",
    "@radix-ui/react-switch": "^1.2.5",
    "@radix-ui/react-tabs": "^1.1.13",
    "@radix-ui/react-toast": "^1.2.15",
    "@radix-ui/react-toggle": "^1.1.10",
    "@radix-ui/react-toggle-group": "^1.1.11",
    "@radix-ui/react-tooltip": "^1.2.8",
    "@tabler/icons-react": "^3.34.1",
    "@tailwindcss/typography": "^0.5.16",
    "@types/react-syntax-highlighter": "^15.5.13",
    "@vercel/sandbox": "^0.0.17",
    "ai": "^5.0.0",
    "autoprefixer": "^10.4.21",
    "class-variance-authority": "^0.7.1",
    "classnames": "^2.5.1",
    "clsx": "^2.1.1",
    "copy-to-clipboard": "^3.3.3",
    "cors": "^2.8.5",
    "dotenv": "^17.2.1",
    "framer-motion": "^12.23.12",
    "groq-sdk": "^0.29.0",
    "jotai": "^2.14.0",
    "lodash-es": "^4.17.21",
    "lucide-react": "^0.532.0",
    "motion": "^12.23.12",
    "nanoid": "^5.1.5",
    "next": "15.4.3",
    "next-themes": "^0.4.6",
    "pixi.js": "^8.13.1",
    "react": "19.1.0",
    "react-dom": "19.1.0",
    "react-hook-form": "^7.62.0",
    "react-icons": "^5.5.0",
    "react-syntax-highlighter": "^15.6.1",
    "sonner": "^2.0.7",
    "tailwind-gradient-mask-image": "^1.2.0",
    "tailwind-merge": "^3.3.1",
    "tailwindcss-animate": "^1.0.7",
    "usehooks-ts": "^3.1.1",
    "zod": "^3.25.76"
  },
  "devDependencies": {
    "@eslint/eslintrc": "^3",
    "@types/lodash-es": "^4.17.12",
    "@types/node": "^20",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "eslint": "^9",
    "eslint-config-next": "15.4.3",
    "postcss": "^8.5.6",
    "postcss-import": "^16.1.1",
    "postcss-nesting": "^13.0.2",
    "tailwindcss": "^3.4.17",
    "typescript": "^5"
  }
}

```

### File: README.md
```md
# Open Lovable

Chat with AI to build React apps instantly. An example app made by the [Firecrawl](https://firecrawl.dev/?ref=open-lovable-github) team. For a complete cloud solution, check out [Lovable.dev](https://lovable.dev/) ❤️.

<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZtaHFleGRsMTNlaWNydGdianI4NGQ4dHhyZjB0d2VkcjRyeXBucCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZFVLWMa6dVskQX0qu1/giphy.gif" alt="Open Lovable Demo" width="100%"/>

## Setup

1. **Clone & Install**
```bash
git clone https://github.com/firecrawl/open-lovable.git
cd open-lovable
pnpm install  # or npm install / yarn install
```

2. **Add `.env.local`**

```env
# =================================================================
# REQUIRED
# =================================================================
FIRECRAWL_API_KEY=your_firecrawl_api_key    # https://firecrawl.dev

# =================================================================
# AI PROVIDER - Choose your LLM
# =================================================================
GEMINI_API_KEY=your_gemini_api_key        # https://aistudio.google.com/app/apikey
ANTHROPIC_API_KEY=your_anthropic_api_key  # https://console.anthropic.com
OPENAI_API_KEY=your_openai_api_key        # https://platform.openai.com
GROQ_API_KEY=your_groq_api_key            # https://console.groq.com

# =================================================================
# FAST APPLY (Optional - for faster edits)
# =================================================================
MORPH_API_KEY=your_morphllm_api_key    # https://morphllm.com/dashboard

# =================================================================
# SANDBOX PROVIDER - Choose ONE: Vercel (default) or E2B
# =================================================================
SANDBOX_PROVIDER=vercel  # or 'e2b'

# Option 1: Vercel Sandbox (default)
# Choose one authentication method:

# Method A: OIDC Token (recommended for development)
# Run `vercel link` then `vercel env pull` to get VERCEL_OIDC_TOKEN automatically
VERCEL_OIDC_TOKEN=auto_generated_by_vercel_env_pull

# Method B: Personal Access Token (for production or when OIDC unavailable)
# VERCEL_TEAM_ID=team_xxxxxxxxx      # Your Vercel team ID 
# VERCEL_PROJECT_ID=prj_xxxxxxxxx    # Your Vercel project ID
# VERCEL_TOKEN=vercel_xxxxxxxxxxxx   # Personal access token from Vercel dashboard

# Option 2: E2B Sandbox
# E2B_API_KEY=your_e2b_api_key      # https://e2b.dev
```

3. **Run**
```bash
pnpm dev  # or npm run dev / yarn dev
```

Open [http://localhost:3000](http://localhost:3000)

## License

MIT
```

### File: colors.json
```json
{
  "heat-4": {
    "hex": "fa5d190a",
    "p3": "0.980392 0.364706 0.098039 / 0.039216"
  },
  "heat-8": {
    "hex": "fa5d1914",
    "p3": "0.980392 0.364706 0.098039 / 0.078431"
  },
  "heat-12": {
    "hex": "fa5d191f",
    "p3": "0.980392 0.364706 0.098039 / 0.121569"
  },
  "heat-16": {
    "hex": "fa5d1929",
    "p3": "0.980392 0.364706 0.098039 / 0.160784"
  },
  "heat-20": {
    "hex": "fa5d1933",
    "p3": "0.980392 0.364706 0.098039 / 0.200000"
  },
  "heat-40": {
    "hex": "fa5d1966",
    "p3": "0.980392 0.364706 0.098039 / 0.400000"
  },
  "heat-90": {
    "hex": "fa5d19e6",
    "p3": "0.980392 0.364706 0.098039 / 0.900000"
  },
  "heat-100": {
    "hex": "fa5d19ff",
    "p3": "0.980392 0.364706 0.098039 / 1.000000"
  },
  "accent-black": {
    "hex": "262626ff",
    "p3": "0.149020 0.149020 0.149020 / 1.000000"
  },
  "accent-white": {
    "hex": "ffffffff",
    "p3": "1.000000 1.000000 1.000000 / 1.000000"
  },
  "accent-amethyst": {
    "hex": "9061ffff",
    "p3": "0.564706 0.380392 1.000000 / 1.000000"
  },
  "accent-bluetron": {
    "hex": "2a6dfbff",
    "p3": "0.164706 0.427451 0.984314 / 1.000000"
  },
  "accent-crimson": {
    "hex": "eb3424ff",
    "p3": "0.921569 0.203922 0.141176 / 1.000000"
  },
  "accent-forest": {
    "hex": "42c366ff",
    "p3": "0.258824 0.764706 0.400000 / 1.000000"
  },
  "accent-honey": {
    "hex": "ecb730ff",
    "p3": "0.925490 0.717647 0.188235 / 1.000000"
  },
  "black-alpha-1": {
    "hex": "00000003",
    "p3": "0.000000 0.000000 0.000000 / 0.011765"
  },
  "black-alpha-2": {
    "hex": "00000005",
    "p3": "0.000000 0.000000 0.000000 / 0.019608"
  },
  "black-alpha-3": {
    "hex": "00000008",
    "p3": "0.000000 0.000000 0.000000 / 0.031373"
  },
  "black-alpha-4": {
    "hex": "0000000a",
    "p3": "0.000000 0.000000 0.000000 / 0.039216"
  },
  "black-alpha-5": {
    "hex": "0000000d",
    "p3": "0.000000 0.000000 0.000000 / 0.050980"
  },
  "black-alpha-6": {
    "hex": "0000000f",
    "p3": "0.000000 0.000000 0.000000 / 0.058824"
  },
  "black-alpha-7": {
    "hex": "00000012",
    "p3": "0.000000 0.000000 0.000000 / 0.070588"
  },
  "black-alpha-8": {
    "hex": "00000014",
    "p3": "0.000000 0.000000 0.000000 / 0.078431"
  },
  "black-alpha-10": {
    "hex": "0000001a",
    "p3": "0.000000 0.000000 0.000000 / 0.101961"
  },
  "black-alpha-12": {
    "hex": "0000001f",
    "p3": "0.000000 0.000000 0.000000 / 0.121569"
  },
  "black-alpha-16": {
    "hex": "00000029",
    "p3": "0.000000 0.000000 0.000000 / 0.160784"
  },
  "black-alpha-20": {
    "hex": "00000033",
    "p3": "0.000000 0.000000 0.000000 / 0.200000"
  },
  "black-alpha-24": {
    "hex": "0000003d",
    "p3": "0.000000 0.000000 0.000000 / 0.239216"
  },
  "black-alpha-32": {
    "hex": "26262652",
    "p3": "0.149020 0.149020 0.149020 / 0.321569"
  },
  "black-alpha-40": {
    "hex": "26262666",
    "p3": "0.149020 0.149020 0.149020 / 0.400000"
  },
  "black-alpha-48": {
    "hex": "2626267a",
    "p3": "0.149020 0.149020 0.149020 / 0.478431"
  },
  "black-alpha-56": {
    "hex": "2626268f",
    "p3": "0.149020 0.149020 0.149020 / 0.560784"
  },
  "black-alpha-64": {
    "hex": "262626a3",
    "p3": "0.149020 0.149020 0.149020 / 0.639216"
  },
  "black-alpha-72": {
    "hex": "262626b8",
    "p3": "0.149020 0.149020 0.149020 / 0.721569"
  },
  "black-alpha-88": {
    "hex": "262626e0",
    "p3": "0.149020 0.149020 0.149020 / 0.878431"
  },
  "white-alpha-56": {
    "hex": "ffffff8f",
    "p3": "1.000000 1.000000 1.000000 / 0.560784"
  },
  "white-alpha-72": {
    "hex": "ffffffb8",
    "p3": "1.000000 1.000000 1.000000 / 0.721569"
  },
  "border-faint": {
    "hex": "edededff",
    "p3": "0.929412 0.929412 0.929412 / 1.000000"
  },
  "border-muted": {
    "hex": "e8e8e8ff",
    "p3": "0.909804 0.909804 0.909804 / 1.000000"
  },
  "border-loud": {
    "hex": "e6e6e6ff",
    "p3": "0.901961 0.901961 0.901961 / 1.000000"
  },
  "illustrations-faint": {
    "hex": "edededff",
    "p3": "0.929412 0.929412 0.929412 / 1.000000"
  },
  "illustrations-muted": {
    "hex": "e6e6e6ff",
    "p3": "0.901961 0.901961 0.901961 / 1.000000"
  },
  "illustrations-default": {
    "hex": "dbdbdbff",
    "p3": "0.858824 0.858824 0.858824 / 1.000000"
  },
  "background-lighter": {
    "hex": "fbfbfbff",
    "p3": "0.984314 0.984314 0.984314 / 1.000000"
  },
  "background-base": {
    "hex": "f9f9f9ff",
    "p3": "0.976471 0.976471 0.976471 / 1.000000"
  }
}
```

### File: next.config.ts
```ts
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'www.google.com',
      },
    ],
  },
};

export default nextConfig;

```

### File: tailwind.config.ts
```ts
/* eslint-disable @typescript-eslint/no-require-imports */
import defaultTheme from "tailwindcss/defaultTheme";
import type { Config } from "tailwindcss";

import colorsJson from "./colors.json";

const colors = Object.keys(colorsJson).reduce(
  (acc, key) => {
    acc[key] = `var(--${key})`;

    return acc;
  },
  {} as Record<string, string>
);

const sizes = Array.from({ length: 1000 }, (_, i) => i).reduce(
  (acc, curr) => {
    acc[curr] = `${curr}px`;

    return acc;
  },
  {
    max: "max-content",
    unset: "unset",
    full: "100%",
    inherit: "inherit",
    "1/2": "50%",
    "1/3": "33.3%",
    "2/3": "66.6%",
    "1/4": "25%",
    "1/6": "16.6%",
    "2/6": "33.3%",
    "3/6": "50%",
    "4/6": "66.6%",
    "5/6": "83.3%"
  } as Record<string, string>
);

const opacities = Array.from({ length: 100 }, (_, i) => i).reduce(
  (acc, curr) => {
    acc[curr] = curr / 100 + "";

    return acc;
  },
  {} as Record<string, string>
);

const transitionDurations = Array.from({ length: 60 }, (_, i) => i).reduce(
  (acc, curr) => {
    acc[curr] = curr * 50 + "";

    return acc;
  },
  {} as Record<string, string>
);

const themeConfig: Config = {
  darkMode: "class",
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components-new/**/*.{js,ts,jsx,tsx,mdx}",
    "./styling-reference/ai-ready-website/app/**/*.{ts,tsx}",
    "./styling-reference/ai-ready-website/components/**/*.{ts,tsx}",
    "./styling-reference/ai-ready-website/components-new/**/*.{ts,tsx}",
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
      fontFamily: {
        sans: ["var(--font-geist-sans)", "var(--font-inter)", ...defaultTheme.fontFamily.sans],
        mono: ["var(--font-geist-mono)", ...defaultTheme.fontFamily.mono],
        ascii: ["var(--font-roboto-mono)", ...defaultTheme.fontFamily.mono]
      },
      fontSize: {
        "title-h1": [
          "60px",
          {
            "lineHeight": "64px",
            "letterSpacing": "-0.3px",
            "fontWeight": "500"
          }
        ],
        "title-h2": [
          "52px",
          {
            "lineHeight": "56px",
            "letterSpacing": "-0.52px",
            "fontWeight": "500"
          }
        ],
        "title-h3": [
          "40px",
          {
            "lineHeight": "44px",
            "letterSpacing": "-0.4px",
            "fontWeight": "500"
          }
        ],
        "title-h4": [
          "32px",
          {
            "lineHeight": "36px",
            "letterSpacing": "-0.32px",
            "fontWeight": "500"
          }
        ],
        "title-h5": [
          "24px",
          {
            "lineHeight": "32px",
            "letterSpacing": "-0.24px",
            "fontWeight": "500"
          }
        ],
        "body-x-large": [
          "20px",
          {
            "lineHeight": "28px",
            "letterSpacing": "-0.1px",
            "fontWeight": "400"
          }
        ],
        "body-large": [
          "16px",
          {
            "lineHeight": "24px",
            "letterSpacing": "0px",
            "fontWeight": "400"
          }
        ],
        "body-medium": [
          "14px",
          {
            "lineHeight": "20px",
            "letterSpacing": "0.14px",
            "fontWeight": "400"
          }
        ],
        "body-small": [
          "13px",
          {
            "lineHeight": "20px",
            "letterSpacing": "0px",
            "fontWeight": "400"
          }
        ],
        "body-input": [
          "15px",
          {
            "lineHeight": "24px",
            "letterSpacing": "0px",
            "fontWeight": "400"
          }
        ],
        "label-x-large": [
          "20px",
          {
            "lineHeight": "28px",
            "letterSpacing": "-0.1px",
            "fontWeight": "450"
          }
        ],
        "label-large": [
          "16px",
          {
            "lineHeight": "24px",
            "letterSpacing": "0px",
            "fontWeight": "450"
          }
        ],
        "label-medium": [
          "14px",
          {
            "lineHeight": "20px",
            "letterSpacing": "0px",
            "fontWeight": "450"
          }
        ],
        "label-small": [
          "13px",
          {
            "lineHeight": "20px",
            "letterSpacing": "0px",
            "fontWeight": "450"
          }
        ],
        "label-x-small": [
          "12px",
          {
            "lineHeight": "20px",
            "letterSpacing": "0px",
            "fontWeight": "450"
          }
        ],
        "mono-medium": [
          "14px",
          {
            "lineHeight": "22px",
            "letterSpacing": "0px",
            "fontWeight": "400"
          }
        ],
        "mono-small": [
          "13px",
          {
            "lineHeight": "20px",
            "letterSpacing": "0px",
            "fontWeight": "500"
          }
        ],
        "mono-x-small": [
          "12px",
          {
            "lineHeight": "16px",
            "letterSpacing": "0px",
            "fontWeight": "400"
          }
        ],
        "title-blog": [
          "28px",
          {
            "lineHeight": "36px",
            "letterSpacing": "-0.28px",
            "fontWeight": "500"
          }
        ]
      },
      colors: {
        transparent: "transparent",
        current: "currentColor",
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
        ...colors
      },
      screens: {
        xs: { min: "390px" },
        "xs-max": { max: "389px" },
        sm: { min: "576px" },
        "sm-max": { max: "575px" },
        md: { min: "768px" },
        "md-max": { max: "767px" },
        lg: { min: "996px" },
        "lg-max": { max: "995px" },
        xl: { min: "1200px" },
        "xl-max": { max: "1199px" }
      },
      opacity: opacities,
      spacing: {
        ...sizes,
        'root': 'var(--root-padding)'
      },
      width: sizes,
      maxWidth: sizes,
      height: sizes,
      inset: sizes,
      borderWidth: sizes,
      backdropBlur: Array.from({ length: 20 }, (_, i) => i).reduce(
        (acc, curr) => {
          acc[curr] = curr + "px";

          return acc;
        },
        {} as Record<string, string>
      ),
      transitionTimingFunction: { DEFAULT: "cubic-bezier(0.25, 0.1, 0.25, 1)" },
      transitionDuration: {
        DEFAULT: "200ms",
        ...transitionDurations
      },
      transitionDelay: {
        ...transitionDurations
      },
      borderRadius: (() => {
        const radius: Record<string | number, string> = {
          full: "999px",
          inherit: "inherit",
          0: "0px",
          lg: "var(--radius)",
          md: "calc(var(--radius) - 2px)",
          sm: "calc(var(--radius) - 4px)",
        };

        for (let i = 1; i <= 32; i += 1) {
          radius[i] = `${i}px`;
        }

        return radius;
      })()
    }
  },
  plugins: [
    ({
      addUtilities, matchUtilities
    }: any) => {
      addUtilities({
        // Inside-border utilities are defined in inside-border-fix.css to avoid Tailwind variant conflicts
        '.mask-border': {
          "mask": "linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0)",
          "mask-composite": "exclude",
          "pointer-events": "none"
        },
        ".center-x": { "@apply absolute left-1/2 -translate-x-1/2": {} },
        ".center-y": { "@apply absolute top-1/2 -translate-y-1/2": {} },
        ".center": { "@apply absolute left-1/2 -translate-x-1/2 top-1/2 -translate-y-1/2": {} },
        ".flex-center": { "@apply flex items-center justify-center": {} },
        ".overlay": { "@apply absolute top-0 left-0 w-full h-full rounded-inherit": {} },
        ".text-gradient": { "@apply !bg-clip-text !text-transparent": {} }
      });
      matchUtilities(
        {
          'cw': (value: string) => {
            const width = parseInt(value);

            return {
              width: value,
              left: `calc(50% - ${width / 2}px)`
            };
          },
          'ch': (value: string) => {
            const height = parseInt(value);

            return {
              height: value,
              top: `calc(50% - ${height / 2}px)`
            };
          },
          'cs': (value: string) => {
            const size = parseInt(value);

            return {
              width: size,
              height: size,
              left: `calc(50% - ${size / 2}px)`,
              top: `calc(50% - ${size / 2}px)`
            };
          },
          'cmw': (value: string) => {
            const [maxWidth, paddingX] = value.split(',').map((v) => parseInt(v));

            const width = paddingX ? `calc(100% - ${paddingX * 2}px)` : '100%';

            return {
              maxWidth: maxWidth,
              width,
              left: `calc(50% - (min(${maxWidth}px, ${width}) / 2))`
            };
          },
          'mw': (value: string) => {
            const [maxWidth, paddingX] = value.split(',').map((v) => parseInt(v));

            const width = paddingX ? `calc(100% - ${paddingX * 2}px)` : '100%';

            return {
              maxWidth: maxWidth,
              width
            };
          }
        },
        { values: sizes }
      );
    },
    require("tailwind-gradient-mask-image"),
    require("@tailwindcss/typography"),
  ]
};

export default themeConfig;
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
  "exclude": ["node_modules", "examples", "tests", "lib/e2b-backends/archive", "styles"]
}

```

### File: .cursor\mcp.json
```json
{
  "mcpServers": {
    "dev3000": {
      "type": "http",
      "url": "http://localhost:3684/mcp"
    }
  }
}

```

### File: app\globals.css
```css
@import "../styles/main.css";
```

### File: config\app.config.ts
```ts
// Application Configuration
// This file contains all configurable settings for the application

export const appConfig = {
  // Vercel Sandbox Configuration
  vercelSandbox: {
    // Sandbox timeout in minutes
    timeoutMinutes: 15,

    // Convert to milliseconds for Vercel Sandbox API
    get timeoutMs() {
      return this.timeoutMinutes * 60 * 1000;
    },

    // Development server port (Vercel Sandbox typically uses 3000 for Next.js/React)
    devPort: 3000,

    // Time to wait for dev server to be ready (in milliseconds)
    devServerStartupDelay: 7000,

    // Time to wait for CSS rebuild (in milliseconds)
    cssRebuildDelay: 2000,

    // Working directory in sandbox
    workingDirectory: '/app',

    // Default runtime for sandbox
    runtime: 'node22' // Available: node22, python3.13, v0-next-shadcn, cua-ubuntu-xfce
  },

  // E2B Sandbox Configuration
  e2b: {
    // Sandbox timeout in minutes
    timeoutMinutes: 30,

    // Convert to milliseconds for E2B API
    get timeoutMs() {
      return this.timeoutMinutes * 60 * 1000;
    },

    // Development server port (E2B uses 5173 for Vite)
    vitePort: 5173,

    // Time to wait for Vite dev server to be ready (in milliseconds)
    viteStartupDelay: 10000,

    // Working directory in sandbox
    workingDirectory: '/home/user/app',
  },
  
  // AI Model Configuration
  ai: {
    // Default AI model
    defaultModel: 'google/gemini-3-pro-preview',
    
    // Available models
    availableModels: [
      'openai/gpt-5',
      'moonshotai/kimi-k2-instruct-0905',
      'anthropic/claude-sonnet-4-20250514',
      'google/gemini-3-pro-preview'
    ],
    
    // Model display names
    modelDisplayNames: {
      'openai/gpt-5': 'GPT-5',
      'moonshotai/kimi-k2-instruct-0905': 'Kimi K2 (Groq)',
      'anthropic/claude-sonnet-4-20250514': 'Sonnet 4',
      'google/gemini-3-pro-preview': 'Gemini 3 Pro (Preview)'
    } as Record<string, string>,
    
    // Model API configuration
    modelApiConfig: {
      'moonshotai/kimi-k2-instruct-0905': {
        provider: 'groq',
        model: 'moonshotai/kimi-k2-instruct-0905'
      }
    },
    
    // Temperature settings for non-reasoning models
    defaultTemperature: 0.7,
    
    // Max tokens for code generation
    maxTokens: 8000,
    
    // Max tokens for truncation recovery
    truncationRecoveryMaxTokens: 4000,
  },
  
  // Code Application Configuration
  codeApplication: {
    // Delay after applying code before refreshing iframe (milliseconds)
    defaultRefreshDelay: 2000,
    
    // Delay when packages are installed (milliseconds)
    packageInstallRefreshDelay: 5000,
    
    // Enable/disable automatic truncation recovery
    enableTruncationRecovery: false, // Disabled - too many false positives
    
    // Maximum number of truncation recovery attempts per file
    maxTruncationRecoveryAttempts: 1,
  },
  
  // UI Configuration
  ui: {
    // Show/hide certain UI elements
    showModelSelector: true,
    showStatusIndicator: true,
    
    // Animation durations (milliseconds)
    animationDuration: 200,
    
    // Toast notification duration (milliseconds)
    toastDuration: 3000,
    
    // Maximum chat messages to keep in memory
    maxChatMessages: 100,
    
    // Maximum recent messages to send as context
    maxRecentMessagesContext: 20,
  },
  
  // Development Configuration
  dev: {
    // Enable debug logging
    enableDebugLogging: true,
    
    // Enable performance monitoring
    enablePerformanceMonitoring: false,
    
    // Log API responses
    logApiResponses: true,
  },
  
  // Package Installation Configuration
  packages: {
    // Use --legacy-peer-deps flag for npm install
    useLegacyPeerDeps: true,
    
    // Package installation timeout (milliseconds)
    installTimeout: 60000,
    
    // Auto-restart Vite after package installation
    autoRestartVite: true,
  },
  
  // File Management Configuration
  files: {
    // Excluded file patterns (files to ignore)
    excludePatterns: [
      'node_modules/**',
      '.git/**',
      '.next/**',
      'dist/**',
      'build/**',
      '*.log',
      '.DS_Store'
    ],
    
    // Maximum file size to read (bytes)
    maxFileSize: 1024 * 1024, // 1MB
    
    // File extensions to treat as text
    textFileExtensions: [
      '.js', '.jsx', '.ts', '.tsx',
      '.css', '.scss', '.sass',
      '.html', '.xml', '.svg',
      '.json', '.yml', '.yaml',
      '.md', '.txt', '.env',
      '.gitignore', '.dockerignore'
    ],
  },
  
  // API Endpoints Configuration (for external services)
  api: {
    // Retry configuration
    maxRetries: 3,
    retryDelay: 1000, // milliseconds
    
    // Request timeout (milliseconds)
    requestTimeout: 30000,
  }
};

// Type-safe config getter
export function getConfig<K extends keyof typeof appConfig>(key: K): typeof appConfig[K] {
  return appConfig[key];
}

// Helper to get nested config values
export function getConfigValue(path: string): any {
  return path.split('.').reduce((obj, key) => obj?.[key], appConfig as any);
}

export default appConfig;
```

### File: hooks\useDebouncedCallback.ts
```ts
import {
  useCallback, useRef
} from 'react';

const DEFAULT_CONFIG = { timeout: 0 };

export function useDebouncedCallback<T extends (...args: any[]) => any>(
  callback: T,
  config: number | { timeout?: number }
): T {
  const timeoutRef = useRef(0);
  const callbackRef = useRef(callback);
  callbackRef.current = callback;

  const currentConfig = typeof config === 'object' ? {
    ...DEFAULT_CONFIG,
    ...config
  } : {
    ...DEFAULT_CONFIG,
    timeout: config
  };

  return useCallback((...args: Parameters<T>) => {
    if (timeoutRef.current) {
      clearTimeout(timeoutRef.current);
    }

    timeoutRef.current = window.setTimeout(() => {
      callbackRef.current(...args);
    }, currentConfig.timeout);
  }, [currentConfig.timeout]) as T;
}

export default useDebouncedCallback;

```

### File: hooks\useDebouncedEffect.ts
```ts
import {
  useEffect, useRef
} from 'react';

const DEFAULT_CONFIG = {
  timeout: 0,
  ignoreInitialCall: true
};

export function useDebouncedEffect(
  callback: () => (void | (() => void)),
  config: number | {
    timeout?: number;
    ignoreInitialCall?: boolean;
  },
  deps: any[] = []
): void {
  let currentConfig;

  if (typeof config === 'object') {
    currentConfig = {
      ...DEFAULT_CONFIG,
      ...config
    };
  } else {
    currentConfig = {
      ...DEFAULT_CONFIG,
      timeout: config
    };
  }
  const {
    timeout, ignoreInitialCall
  } = currentConfig;

  const data = useRef<{ firstTime: boolean }>({ firstTime: true });

  useEffect(() => {
    const { firstTime } = data.current;

    if (firstTime && ignoreInitialCall) {
      data.current.firstTime = false;

      return;
    }

    let clearFunc: (() => void) | undefined;

    const handler = setTimeout(() => {
      clearFunc = callback() ?? undefined;
    }, timeout);

    return () => {
      clearTimeout(handler);

      if (clearFunc && typeof clearFunc === 'function') {
        clearFunc();
      }
    };
  }, [
    callback,
    ignoreInitialCall,
    timeout,
    // eslint-disable-next-line react-hooks/exhaustive-deps
    ...deps
  ]);
}

export default useDebouncedEffect;

```

### File: hooks\useSwitchingCode.ts
```ts
import { useEffect, useRef, useState } from 'react';
import { encryptText } from '@/components/app/(home)/sections/hero/Title/Title';



export default function useSwitchingCode(code: string, ms = 20, progress = 1, fill = true) {
  const [value, setValue] = useState(code);
  const prevCode = useRef(value);

  useEffect(() => {
    if (code === prevCode.current) return;

    let i = 0;

    setValue(prevCode.current);

    let timeout: number;

    const tick = () => {
      i += progress;

      const prevLines = prevCode.current.split('\n');
      const currentLines = code.split('\n');

      const maxLines = fill ? 10 : Math.max(prevLines.length, currentLines.length);
      while (prevLines.length < maxLines) prevLines.push('');
      while (currentLines.length < maxLines) currentLines.push('');

      const remainingLines = prevLines.map((line, index) => {
        if (line === currentLines[index]) return line;

        const charLength = Math.floor(line.length * (i / 30));

        return (currentLines[index]?.slice(0, Math.floor(currentLines[index].length * (i / 30))) ?? '')
         + encryptText(line.slice(charLength), 0, { randomizeChance: 0.5 });
      });

      setValue((fill ? remainingLines : remainingLines.filter((line, index, arr) => {
        if (line === '' && arr[index - 1] === '') return false;

        return true;
      })).join('\n'));

      if (i < 30) {
        timeout = window.setTimeout(tick, ms);
      } else {
        prevCode.current = code;
      }
    };

    tick();

    return () => {
      window.clearTimeout(timeout);
      prevCode.current = code;
    };
  }, [code, ms, progress, fill]);

  return value;
}
```

### File: lib\build-validator.ts
```ts
export interface BuildValidation {
  success: boolean;
  errors: string[];
  isRendering: boolean;
  warnings?: string[];
}

/**
 * Validates that the sandbox build was successful
 * Checks compilation status and verifies app is rendering
 */
export async function validateBuild(sandboxUrl: string, sandboxId: string): Promise<BuildValidation> {
  try {
    // Step 1: Wait for Vite to process files (give it time to compile)
    await new Promise(resolve => setTimeout(resolve, 3000));

    // Step 2: Check if the sandbox is actually serving content
    const response = await fetch(sandboxUrl, {
      headers: {
        'User-Agent': 'OpenLovable-Validator',
        'Cache-Control': 'no-cache'
      }
    });

    if (!response.ok) {
      return {
        success: false,
        errors: [`Sandbox returned ${response.status}`],
        isRendering: false
      };
    }

    const html = await response.text();

    // Step 3: Check if it's the default page or actual app
    const isDefaultPage =
      html.includes('Vercel Sandbox Ready') ||
      html.includes('Start building your React app with Vite') ||
      html.includes('Vite + React') ||
      !html.includes('id="root"');

    if (isDefaultPage) {
      return {
        success: false,
        errors: ['Sandbox showing default page, app not rendered'],
        isRendering: false
      };
    }

    // Step 4: Check for Vite error overlay in HTML
    const hasViteError = html.includes('vite-error-overlay');
    if (hasViteError) {
      // Try to extract error message
      const errorMatch = html.match(/Failed to resolve import "([^"]+)"/);
      const error = errorMatch
        ? `Missing package: ${errorMatch[1]}`
        : 'Vite compilation error detected';

      return {
        success: false,
        errors: [error],
        isRendering: false
      };
    }

    // Success! App is rendering
    return {
      success: true,
      errors: [],
      isRendering: true
    };

  } catch (error) {
    console.error('[validateBuild] Error during validation:', error);
    return {
      success: false,
      errors: [error instanceof Error ? error.message : 'Validation failed'],
      isRendering: false
    };
  }
}

/**
 * Extracts missing package names from error messages
 */
export function extractMissingPackages(error: any): string[] {
  const message = error?.message || String(error);
  const packages: string[] = [];

  // Pattern 1: "Failed to resolve import 'package-name'"
  const importMatches = message.matchAll(/Failed to resolve import ["']([^"']+)["']/g);
  for (const match of importMatches) {
    packages.push(match[1]);
  }

  // Pattern 2: "Cannot find module 'package-name'"
  const moduleMatches = message.matchAll(/Cannot find module ["']([^"']+)["']/g);
  for (const match of moduleMatches) {
    packages.push(match[1]);
  }

  // Pattern 3: "Package 'package-name' not found"
  const packageMatches = message.matchAll(/Package ["']([^"']+)["'] not found/g);
  for (const match of packageMatches) {
    packages.push(match[1]);
  }

  return [...new Set(packages)]; // Remove duplicates
}

/**
 * Classifies error type for targeted recovery
 */
export type ErrorType = 'missing-package' | 'syntax-error' | 'sandbox-timeout' | 'not-rendered' | 'vite-error' | 'unknown';

export function classifyError(error: any): ErrorType {
  const message = (error?.message || String(error)).toLowerCase();

  if (message.includes('failed to resolve import') ||
      message.includes('cannot find module') ||
      message.includes('missing package')) {
    return 'missing-package';
  }

  if (message.includes('syntax error') ||
      message.includes('unexpected token') ||
      message.includes('parsing error')) {
    return 'syntax-error';
  }

  if (message.includes('timeout') ||
      message.includes('not responding') ||
      message.includes('timed out')) {
    return 'sandbox-timeout';
  }

  if (message.includes('not rendered') ||
      message.includes('sandbox ready') ||
      message.includes('default page')) {
    return 'not-rendered';
  }

  if (message.includes('vite') ||
      message.includes('compilation')) {
    return 'vite-error';
  }

  return 'unknown';
}

/**
 * Calculates retry delay based on attempt number and error type
 */
export function calculateRetryDelay(attempt: number, errorType: ErrorType): number {
  const baseDelay = 2000; // 2 seconds

  // Different strategies for different errors
  switch (errorType) {
    case 'missing-package':
      // Packages need time to install
      return baseDelay * 2 * attempt; // 4s, 8s, 12s

    case 'not-rendered':
      // Vite needs time to compile
      return baseDelay * 3 * attempt; // 6s, 12s, 18s

    case 'vite-error':
      // Vite restart needed
      return baseDelay * 2 * attempt;

    case 'sandbox-timeout':
      // Sandbox might be slow
      return baseDelay * 4 * attempt; // 8s, 16s, 24s

    default:
      // Standard exponential backoff
      return baseDelay * attempt;
  }
}

```

### File: lib\context-selector.ts
```ts
import { FileManifest, EditIntent, EditType } from '@/types/file-manifest';
import { analyzeEditIntent } from '@/lib/edit-intent-analyzer';
import { getEditExamplesPrompt, getComponentPatternPrompt } from '@/lib/edit-examples';

export interface FileContext {
  primaryFiles: string[]; // Files to edit
  contextFiles: string[]; // Files to include for reference
  systemPrompt: string;   // Enhanced prompt with file info
  editIntent: EditIntent;
}

/**
 * Select files and build context based on user prompt
 */
export function selectFilesForEdit(
  userPrompt: string,
  manifest: FileManifest
): FileContext {
  // Analyze the edit intent
  const editIntent = analyzeEditIntent(userPrompt, manifest);
  
  // Get the files based on intent - only edit target files, but provide all others as context
  const primaryFiles = editIntent.targetFiles;
  const allFiles = Object.keys(manifest.files);
  let contextFiles = allFiles.filter(file => !primaryFiles.includes(file));
  
  // ALWAYS include key files in context if they exist and aren't already primary files
  const keyFiles: string[] = [];
  
  // App.jsx is most important - shows component structure
  const appFile = allFiles.find(f => f.endsWith('App.jsx') || f.endsWith('App.tsx'));
  if (appFile && !primaryFiles.includes(appFile)) {
    keyFiles.push(appFile);
  }
  
  // Include design system files for style context
  const tailwindConfig = allFiles.find(f => f.endsWith('tailwind.config.js') || f.endsWith('tailwind.config.ts'));
  if (tailwindConfig && !primaryFiles.includes(tailwindConfig)) {
    keyFiles.push(tailwindConfig);
  }
  
  const indexCss = allFiles.find(f => f.endsWith('index.css') || f.endsWith('globals.css'));
  if (indexCss && !primaryFiles.includes(indexCss)) {
    keyFiles.push(indexCss);
  }
  
  // Include package.json to understand dependencies
  const packageJson = allFiles.find(f => f.endsWith('package.json'));
  if (packageJson && !primaryFiles.includes(packageJson)) {
    keyFiles.push(packageJson);
  }
  
  // Put key files at the beginning of context for visibility
  contextFiles = [...keyFiles, ...contextFiles.filter(f => !keyFiles.includes(f))];
  
  // Build enhanced system prompt
  const systemPrompt = buildSystemPrompt(
    userPrompt,
    editIntent,
    primaryFiles,
    contextFiles,
    manifest
  );
  
  return {
    primaryFiles,
    contextFiles,
    systemPrompt,
    editIntent,
  };
}

/**
 * Build an enhanced system prompt with file structure context
 */
function buildSystemPrompt(
  userPrompt: string,
  editIntent: EditIntent,
  primaryFiles: string[],
  contextFiles: string[],
  manifest: FileManifest
): string {
  const sections: string[] = [];
  
  // Add edit examples first for better understanding
  if (editIntent.type !== EditType.FULL_REBUILD) {
    sections.push(getEditExamplesPrompt());
  }
  
  // Add edit intent section
  sections.push(`## Edit Intent
Type: ${editIntent.type}
Description: ${editIntent.description}
Confidence: ${(editIntent.confidence * 100).toFixed(0)}%

User Request: "${userPrompt}"`);
  
  // Add file structure overview
  sections.push(buildFileStructureSection(manifest));
  
  // Add component patterns
  const fileList = Object.keys(manifest.files).map(f => f.replace('/home/user/app/', '')).join('\n');
  sections.push(getComponentPatternPrompt(fileList));
  
  // Add primary files section
  if (primaryFiles.length > 0) {
    sections.push(`## Files to Edit
${primaryFiles.map(f => {
  const fileInfo = manifest.files[f];
  return `- ${f}${fileInfo?.componentInfo ? ` (${fileInfo.componentInfo.name} component)` : ''}`;
}).join('\n')}`);
  }
  
  // Add context files section
  if (contextFiles.length > 0) {
    sections.push(`## Context Files (for reference only)
${contextFiles.map(f => {
  const fileInfo = manifest.files[f];
  return `- ${f}${fileInfo?.componentInfo ? ` (${fileInfo.componentInfo.name} component)` : ''}`;
}).join('\n')}`);
  }
  
  // Add specific instructions based on edit type
  sections.push(buildEditInstructions(editIntent.type));
  
  // Add component relationships if relevant
  if (editIntent.type === EditType.UPDATE_COMPONENT || 
      editIntent.type === EditType.ADD_FEATURE) {
    sections.push(buildComponentRelationships(primaryFiles, manifest));
  }
  
  return sections.join('\n\n');
}

/**
 * Build file structure overview section
 */
function buildFileStructureSection(manifest: FileManifest): string {
  const allFiles = Object.entries(manifest.files)
    .map(([path]) => path.replace('/home/user/app/', ''))
    .filter(path => !path.includes('node_modules'))
    .sort();
  
  const componentFiles = Object.entries(manifest.files)
    .filter(([, info]) => info.type === 'component' || info.type === 'page')
    .map(([path, info]) => ({
      path: path.replace('/home/user/app/', ''),
      name: info.componentInfo?.name || path.split('/').pop(),
      type: info.type,
    }));
  
  return `## 🚨 EXISTING PROJECT FILES - DO NOT CREATE NEW FILES WITH SIMILAR NAMES 🚨

### ALL PROJECT FILES (${allFiles.length} files)
\`\`\`
${allFiles.join('\n')}
\`\`\`

### Component Files (USE THESE EXACT NAMES)
${componentFiles.map(f => 
  `- ${f.name} → ${f.path} (${f.type})`
).join('\n')}

### CRITICAL: Component Relationships
**ALWAYS CHECK App.jsx FIRST** to understand what components exist and how they're imported!

Common component overlaps to watch for:
- "nav" or "navigation" → Often INSIDE Header.jsx, not a separate file
- "menu" → Usually part of Header/Nav, not separate
- "logo" → Typically in Header, not standalone

When user says "nav" or "navigation":
1. First check if Header.jsx exists
2. Look inside Header.jsx for navigation elements
3. Only create Nav.jsx if navigation doesn't exist anywhere

Entry Point: ${manifest.entryPoint}

### Routes
${manifest.routes.map(r => 
  `- ${r.path} → ${r.component.split('/').pop()}`
).join('\n') || 'No routes detected'}`;
}

/**
 * Build edit-type specific instructions
 */
function buildEditInstructions(editType: EditType): string {
  const instructions: Record<EditType, string> = {
    [EditType.UPDATE_COMPONENT]: `## SURGICAL EDIT INSTRUCTIONS
- You MUST preserve 99% of the original code
- ONLY edit the specific component(s) mentioned
- Make ONLY the minimal change requested
- DO NOT rewrite or refactor unless explicitly asked
- DO NOT remove any existing code unless explicitly asked
- DO NOT change formatting or structure
- Preserve all imports and exports
- Maintain the existing code style
- Return the COMPLETE file with the surgical change applied
- Think of yourself as a surgeon making a precise incision, not an artist repainting`,
    
    [EditType.ADD_FEATURE]: `## Instructions
- Create new components in appropriate directories
- IMPORTANT: Update parent components to import and use the new component
- Update routing if adding new pages
- Follow existing patterns and conventions
- Add necessary styles to match existing design
- Example workflow:
  1. Create NewComponent.jsx
  2. Import it in the parent: import NewComponent from './NewComponent'
  3. Use it in the parent's render: <NewComponent />`,
    
    [EditType.FIX_ISSUE]: `## Instructions
- Identify and fix the specific issue
- Test the fix doesn't break other functionality
- Preserve existing behavior except for the bug
- Add error handling if needed`,
    
    [EditType.UPDATE_STYLE]: `## SURGICAL STYLE EDIT INSTRUCTIONS
- Change ONLY the specific style/class mentioned
- If user says "change background to blue", change ONLY the background class
- DO NOT touch any other styles, classes, or attributes
- DO NOT refactor or "improve" the styling
- DO NOT change the component structure
- Preserve ALL other classes and styles exactly as they are
- Return the COMPLETE file with only the specific style change`,
    
    [EditType.REFACTOR]: `## Instructions
- Improve code quality without changing functionality
- Follow project conventions
- Maintain all existing features
- Improve readability and maintainability`,
    
    [EditType.FULL_REBUILD]: `## Instructions
- You may rebuild the entire application
- Keep the same core functionality
- Improve upon the existing design
- Use modern best practices`,
    
    [EditType.ADD_DEPENDENCY]: `## Instructions
- Update package.json with new dependency
- Add necessary import statements
- Configure the dependency if needed
- Update any build configuration`,
  };
  
  return instructions[editType] || instructions[EditType.UPDATE_COMPONENT];
}

/**
 * Build component relationship information
 */
function buildComponentRelationships(
  files: string[],
  manifest: FileManifest
): string {
  const relationships: string[] = ['## Component Relationships'];
  
  for (const file of files) {
    const fileInfo = manifest.files[file];
    if (!fileInfo?.componentInfo) continue;
    
    const componentName = fileInfo.componentInfo.name;
    const treeNode = manifest.componentTree[componentName];
    
    if (treeNode) {
      relationships.push(`\n### ${componentName}`);
      
      if (treeNode.imports.length > 0) {
        relationships.push(`Imports: ${treeNode.imports.join(', ')}`);
      }
      
      if (treeNode.importedBy.length > 0) {
        relationships.push(`Used by: ${treeNode.importedBy.join(', ')}`);
      }
      
      if (fileInfo.componentInfo.childComponents?.length) {
        relationships.push(`Renders: ${fileInfo.componentInfo.childComponents.join(', ')}`);
      }
    }
  }
  
  return relationships.join('\n');
}

/**
 * Get file content for selected files
 */
export async function getFileContents(
  files: string[],
  manifest: FileManifest
): Promise<Record<string, string>> {
  const contents: Record<string, string> = {};
  
  for (const file of files) {
    const fileInfo = manifest.files[file];
    if (fileInfo) {
      contents[file] = fileInfo.content;
    }
  }
  
  return contents;
}

/**
 * Format files for AI context
 */
export function formatFilesForAI(
  primaryFiles: Record<string, string>,
  contextFiles: Record<string, string>
): string {
  const sections: string[] = [];
  
  // Add primary files
  sections.push('## Files to Edit (ONLY OUTPUT THESE FILES)\n');
  sections.push('🚨 You MUST ONLY generate the files listed below. Do NOT generate any other files! 🚨\n');
  sections.push('⚠️ CRITICAL: Return the COMPLETE file - NEVER truncate with "..." or skip any lines! ⚠️\n');
  sections.push('The file MUST include ALL imports, ALL functions, ALL JSX, and ALL closing tags.\n\n');
  for (const [path, content] of Object.entries(primaryFiles)) {
    sections.push(`### ${path}
**IMPORTANT: This is the COMPLETE file. Your output must include EVERY line shown below, modified only where necessary.**
\`\`\`${getFileExtension(path)}
${content}
\`\`\`
`);
  }
  
  // Add context files if any - but truncate large files
  if (Object.keys(contextFiles).length > 0) {
    sections.push('\n## Context Files (Reference Only - Do Not Edit)\n');
    for (const [path, content] of Object.entries(contextFiles)) {
      // Truncate very large context files to save tokens
      let truncatedContent = content;
      if (content.length > 2000) {
        truncatedContent = content.substring(0, 2000) + '\n// ... [truncated for context length]';
      }
      
      sections.push(`### ${path}
\`\`\`${getFileExtension(path)}
${truncatedContent}
\`\`\`
`);
    }
  }
  
  return sections.join('\n');
}

/**
 * Get file extension for syntax highlighting
 */
function getFileExtension(path: string): string {
  const ext = path.split('.').pop() || '';
  const mapping: Record<string, string> = {
    'js': 'javascript',
    'jsx': 'javascript',
    'ts': 'typescript',
    'tsx': 'typescript',
    'css': 'css',
    'json': 'json',
  };
  return mapping[ext] || ext;
}
```

### File: lib\edit-examples.ts
```ts
/**
 * Example-based prompts for teaching AI proper edit behavior
 */

export const EDIT_EXAMPLES = `
## Edit Strategy Examples

### Example 1: Update Header Color
USER: "Make the header background black"

CORRECT APPROACH:
1. Identify Header component location
2. Edit ONLY Header.jsx
3. Change background color class/style

INCORRECT APPROACH:
- Regenerating entire App.jsx
- Creating new Header.jsx from scratch
- Modifying unrelated files

EXPECTED OUTPUT:
<file path="src/components/Header.jsx">
// Only the Header component with updated background
// Preserving all existing functionality
</file>

### Example 2: Add New Page
USER: "Add a videos page"

CORRECT APPROACH:
1. Create Videos.jsx component
2. Update routing in App.jsx or Router component
3. Add navigation link if needed

INCORRECT APPROACH:
- Regenerating entire application
- Recreating all existing pages

EXPECTED OUTPUT:
<file path="src/components/Videos.jsx">
// New Videos component
</file>

<file path="src/App.jsx">
// ONLY the routing update, preserving everything else
</file>

### Example 3: Fix Styling Issue
USER: "Fix the button styling on mobile"

CORRECT APPROACH:
1. Identify which component has the button
2. Update only that component's Tailwind classes
3. Add responsive modifiers (sm:, md:, etc)

INCORRECT APPROACH:
- Regenerating all components
- Creating new CSS files
- Modifying global styles unnecessarily

### Example 4: Add Feature to Component
USER: "Add a search bar to the header"

CORRECT APPROACH:
1. Modify Header.jsx to add search functionality
2. Preserve all existing header content
3. Integrate search seamlessly

INCORRECT APPROACH:
- Creating Header.jsx from scratch
- Losing existing navigation/branding

### Example 5: Add New Component
USER: "Add a newsletter signup to the footer"

CORRECT APPROACH:
1. Create Newsletter.jsx component
2. UPDATE Footer.jsx to import Newsletter
3. Add <Newsletter /> in the appropriate place in Footer

EXPECTED OUTPUT:
<file path="src/components/Newsletter.jsx">
// New Newsletter component
</file>

<file path="src/components/Footer.jsx">
// Updated Footer with Newsletter import and usage
import Newsletter from './Newsletter';
// ... existing code ...
// Add <Newsletter /> in the render
</file>

### Example 6: Add External Library
USER: "Add animations with framer-motion to the hero"

CORRECT APPROACH:
1. Import framer-motion in Hero.jsx
2. Use motion components
3. System will auto-install framer-motion

EXPECTED OUTPUT:
<file path="src/components/Hero.jsx">
import { motion } from 'framer-motion';
// ... rest of Hero with motion animations
</file>

### Example 7: Remove Element
USER: "Remove start deploying button"

CORRECT APPROACH:
1. Search for "start deploying" in all component files
2. Find it in Hero.jsx
3. Edit ONLY Hero.jsx to remove that button

INCORRECT APPROACH:
- Creating a new file
- Editing multiple files
- Redesigning the entire Hero

EXPECTED OUTPUT:
<file path="src/components/Hero.jsx">
// Hero component with "start deploying" button removed
// All other content preserved
</file>

### Example 8: Delete Section
USER: "Delete the testimonials section"

CORRECT APPROACH:
1. Find which file contains testimonials
2. Remove only that section from the file
3. Keep all other content intact

INCORRECT APPROACH:
- Deleting the entire file
- Recreating the page without testimonials

### Example 9: Change a Single Style (CRITICAL EXAMPLE)
USER: "update the hero to bg blue"

CORRECT APPROACH:
1. Identify the Hero component file: 'src/components/Hero.jsx'.
2. Locate the outermost 'div' or container element.
3. Find the existing background color class (e.g., 'bg-gray-900').
4. Replace ONLY that class with 'bg-blue-500'.
5. Return the entire file, completely unchanged except for that single class modification.

**Original File Content (BEFORE):**
<file path="src/components/Hero.jsx">
import React from 'react';

export default function Hero() {
  return (
    <div className="w-full bg-gray-900 text-white py-20 px-4">
      <h1 className="text-5xl font-bold">Welcome to the App</h1>
      <p className="mt-4 text-lg">This is the original hero section.</p>
      <button className="mt-6 px-6 py-3 bg-blue-600 hover:bg-blue-700 rounded-lg">
        Get Started
      </button>
    </div>
  );
}
</file>

**Expected Output (AFTER):**
<file path="src/components/Hero.jsx">
import React from 'react';

export default function Hero() {
  return (
    <div className="w-full bg-blue-500 text-white py-20 px-4">
      <h1 className="text-5xl font-bold">Welcome to the App</h1>
      <p className="mt-4 text-lg">This is the original hero section.</p>
      <button className="mt-6 px-6 py-3 bg-blue-600 hover:bg-blue-700 rounded-lg">
        Get Started
      </button>
    </div>
  );
}
</file>

NOTICE: Everything remains EXACTLY the same except 'bg-gray-900' → 'bg-blue-500'. 
- The button still has bg-blue-600 (unchanged)
- All text, structure, imports are identical
- No reformatting, no "improvements", no cleanup

## Key Principles

1. **Minimal Changes**: Only modify what's necessary
2. **Preserve Functionality**: Keep all existing features
3. **Respect Structure**: Follow existing patterns
4. **Target Precision**: Edit specific files, not everything
5. **Context Awareness**: Use imports/exports to understand relationships

## File Identification Patterns

- "header" → src/components/Header.jsx
- "navigation" → src/components/Nav.jsx or Header.jsx
- "footer" → src/components/Footer.jsx
- "home page" → src/App.jsx or src/pages/Home.jsx
- "styling" → Component files (Tailwind) or index.css
- "routing" → App.jsx or Router component
- "layout" → Layout components or App.jsx

## Edit Intent Classification

UPDATE_COMPONENT: Modify existing component
- Keywords: update, change, modify, edit, fix
- Action: Edit single file

ADD_FEATURE: Add new functionality
- Keywords: add, create, implement, build
- Action: Create new files + minimal edits

FIX_ISSUE: Resolve problems
- Keywords: fix, resolve, debug, repair
- Action: Targeted fixes

UPDATE_STYLE: Change appearance
- Keywords: style, color, theme, design
- Action: Update Tailwind classes

REFACTOR: Improve code quality
- Keywords: refactor, clean, optimize
- Action: Restructure without changing behavior
`;

export function getEditExamplesPrompt(): string {
  return EDIT_EXAMPLES;
}

export function getComponentPatternPrompt(fileStructure: string): string {
  return `
## Current Project Structure

${fileStructure}

## Component Naming Patterns
Based on your file structure, here are the patterns to follow:

1. Component files are in: src/components/
2. Page components might be in: src/pages/ or src/components/
3. Utility functions are in: src/utils/ or src/lib/
4. Styles use Tailwind classes inline
5. Main app entry is: src/App.jsx

When the user mentions a component by name, look for:
- Exact matches first (Header → Header.jsx)
- Partial matches (nav → Navigation.jsx, NavBar.jsx)
- Semantic matches (top bar → Header.jsx)
`;
}
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

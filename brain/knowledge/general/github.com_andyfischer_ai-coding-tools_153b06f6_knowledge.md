---
id: github.com-andyfischer-ai-coding-tools-153b06f6-kn
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:30.235838
---

# KNOWLEDGE EXTRACT: github.com_andyfischer_ai-coding-tools_153b06f6
> **Extracted on:** 2026-04-01 16:10:20
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007524953/github.com_andyfischer_ai-coding-tools_153b06f6

---

## File: `.gitignore`
```
node_modules
.DS_Store
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2025 Andrew Fischer

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

# ai-coding-tools #

Repo with open sourced tools for AI assisted coding.

# Contents #

### [claude-history-tool](https://github.com/andyfischer/ai-coding-tools/tree/main/claude-history-tool#readme) ###

Electron based application that allows you to browse the full history of every Claude Code session.

### candle

This project was moved to a new repo, see: https://github.com/facetlayer/candle

```

## File: `candle/README.md`
```markdown

# Moved

Moved to a seperate Github repo: https://github.com/andyfischer/candle
```

## File: `claude-history-tool/.candle-setup.json`
```json
{
  "services": [
    {
      "name": "tsc",
      "shell": "npm run dev:main",
      "default": true
    },
    {
      "name": "renderer",
      "shell": "npm run dev:renderer"
    },
    {
      "name": "electron",
      "shell": "npm run start"
    },
    {
      "name": "storybook",
      "shell": "npm run storybook"
    }
  ]
}
```

## File: `claude-history-tool/.env.example`
```
# Development Environment Variables
# Copy this file to .env and adjust values as needed

# Application Environment
NODE_ENV=development

# Development Server Ports
RENDERER_PORT=3447
STORYBOOK_PORT=3448

# Electron Window Settings
WINDOW_WIDTH=1200
WINDOW_HEIGHT=800

# Development Features
ENABLE_DEV_TOOLS=true
ENABLE_CONSOLE_LOGS=true

# Database Settings (if needed)
# DB_PATH=./data/claude-history.db

# Debug Settings
DEBUG_LEVEL=info

# API Settings
API_HOSTNAME=https://api.mcp-eval.com
```

## File: `claude-history-tool/.gitignore`
```
dist
.parcel-cache

# Environment variables
.env
.env.local

release
.DS_Store
```

## File: `claude-history-tool/CLAUDE.md`
```markdown

# Overview #

This project implements a Electron based desktop app which browses the user's Claude history
and displays it in a helpful UI.

# Tips

Use the 'candle' MCP to start services and read logs.

Services:

 'tsc' - The Typescript compiler
 'renderer' - The Parcel web renderer running at http://localhost:3447
 'electron' - The Electron dev process
 'storybook' - The Storybook service running at http://localhost:3448
```

## File: `claude-history-tool/README.md`
```markdown
# Claude History tool

A desktop application for browsing and viewing your Claude chat history.

## Download

Download the latest release [here](https://github.com/andyfischer/ai-coding-tools/releases).

## Features

- **Browseable Session History**: View all your Claude conversations organized by project.
- **Full Message Details**: Examine the stored JSON to see extra details about your chats.
- **Full Tool Use**: See the full input & response data for each tool use.
- **Token Costs**: See token cost per message.
- **Analytics**: Presents some basic analytics about your sessions and tool use.

## Data Usage and Privacy notice

The "Claude History" tool does not transmit or upload or share your data in any way.
All the related data remains private and local to your machine.

## Development

To run the code locally:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd claude-history-tool
   ```

2. Install dependencies:
   ```bash
   yarn install
   ```

3. Build the application:
   ```bash
   yarn rebuild
   ```

4. (Optional) Copy `.env.sample` to `.env` and adjust as needed.

### Running in Development Mode

The project uses multiple services that can be managed with the included `candle` MCP tool:

1. **Start TypeScript compiler** (watches for changes):
   ```bash
   yarn dev:main
   ```

2. **Start the renderer development server** (http://localhost:3447):
   ```bash
   yarn dev:renderer
   ```

3. **Start Electron in development mode**:
   ```bash
   yarn dev:electron
   ```

4. **Start Storybook** (http://localhost:3448):
   ```bash
   yarn storybook
   ```

### Testing

Run the test suite:
```bash
yarn test
```

Run tests with UI:
```bash
yarn test:ui
```

## License

MIT License - see package.json for details

## Author

https://andyfischer.dev
```

## File: `claude-history-tool/package.json`
```json
{
  "name": "claude-history-tool",
  "version": "0.9.0",
  "description": "A tool to browse and view Claude chat history",
  "main": "dist/main/main.js",
  "scripts": {
    "build": "npm run build:main && npm run build:renderer",
    "build:main": "webpack --config webpack.main.config.js --mode production",
    "build:renderer": "webpack --config webpack.renderer.config.js --mode production",
    "dev:main": "webpack --config webpack.main.config.js --watch --mode development",
    "dev:renderer": "webpack serve --config webpack.renderer.config.js --mode development",
    "start": "electron .",
    "test": "vitest",
    "test:ui": "vitest --ui",
    "storybook": "storybook dev -p ${STORYBOOK_PORT:-3448}",
    "build-storybook": "storybook build",
    "rebuild": "electron rebuild",
    "postinstall": "electron-builder install-app-deps",
    "dist": "npm run build && electron-builder",
    "dist:mac": "npm run build && electron-builder --mac",
    "dist:win": "npm run build && electron-builder --win",
    "dist:dmg": "npm run build && electron-builder --mac --publish=never",
    "dist:mac-dir": "npm run build && electron-builder --mac dir",
    "dist:all": "npm run build && electron-builder -mw",
    "publish": "npm run build && electron-builder --publish always"
  },
  "keywords": [
    "electron",
    "claude",
    "chat",
    "history"
  ],
  "author": "Andy Fischer",
  "license": "MIT",
  "devDependencies": {
    "@storybook/addon-essentials": "^8.3.0",
    "@storybook/addon-interactions": "^8.3.0",
    "@storybook/addon-links": "^8.3.0",
    "@storybook/blocks": "^8.3.0",
    "@storybook/react": "^8.3.0",
    "@storybook/react-vite": "^8.3.0",
    "@storybook/test": "^8.3.0",
    "@testing-library/dom": "^10.4.0",
    "@testing-library/jest-dom": "^6.5.0",
    "@testing-library/react": "^16.0.1",
    "@testing-library/user-event": "^14.5.2",
    "@types/node": "^22.5.0",
    "@types/react": "^18.3.5",
    "@types/react-dom": "^18.3.0",
    "@vitejs/plugin-react": "^4.3.1",
    "concurrently": "^9.0.1",
    "copy-webpack-plugin": "13.0.0",
    "css-loader": "7.1.2",
    "dotenv": "17.2.0",
    "electron": "^32.0.0",
    "electron-builder": "26.0.12",
    "electron-rebuild": "3.2.9",
    "html-webpack-plugin": "5.6.3",
    "jsdom": "^25.0.0",
    "process": "^0.11.10",
    "sass": "1.89.2",
    "sass-loader": "16.0.5",
    "storybook": "^8.3.0",
    "style-loader": "4.0.0",
    "ts-loader": "9.5.2",
    "typescript": "^5.5.4",
    "vite": "^5.4.0",
    "vitest": "3.2.4",
    "webpack": "5.100.2",
    "webpack-cli": "6.0.1",
    "webpack-dev-server": "5.2.2",
    "webpack-node-externals": "3.0.0"
  },
  "dependencies": {
    "@andyfischer/sqlite-wrapper": "^0.3.1",
    "@tanstack/react-query": "5.83.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-icons": "5.5.0",
    "react-router-dom": "^6.26.0"
  },
  "packageManager": "yarn@1.22.22+sha512.a6b2f7906b721bba3d67d4aff083df04dad64c399707841b7acf00f6b133b7ac24255f2652fa22ae3534329dc6180534e98d17432037ff6fd140556e2bb3137e",
  "build": {
    "appId": "com.andyfischer.claude-history-tool",
    "productName": "Claude History",
    "directories": {
      "output": "release"
    },
    "files": [
      "dist/**/*",
      "node_modules/**/*",
      "package.json"
    ],
    "mac": {
      "icon": "assets/icon.icns",
      "category": "public.app-category.productivity",
      "hardenedRuntime": true,
      "gatekeeperAssess": false,
      "entitlements": "assets/entitlements.mac.plist",
      "entitlementsInherit": "assets/entitlements.mac.plist",
      "target": [
        {
          "target": "dmg",
          "arch": [
            "x64",
            "arm64"
          ]
        }
      ],
      "artifactName": "Claude-History-Tool-Mac-${arch}.${ext}",
      "notarize": true
    },
    "win": {
      "icon": "assets/icon.icns",
      "target": [
        {
          "target": "portable",
          "arch": [
            "x64"
          ]
        },
        {
          "target": "zip",
          "arch": [
            "x64"
          ]
        }
      ],
      "artifactName": "Claude-History-Tool-Windows-${arch}.${ext}"
    },
    "dmg": {
      "icon": "assets/icon.icns",
      "title": "Claude History",
      "contents": [
        {
          "x": 110,
          "y": 150
        },
        {
          "x": 240,
          "y": 150,
          "type": "link",
          "path": "/Applications"
        }
      ]
    }
  }
}
```

## File: `claude-history-tool/publish_release.sh`
```bash
#!/bin/bash

set -e

# Get the version from package.json
VERSION=$(node -p "require('./package.json').version")
TAG_NAME="claude-history-tool-v$VERSION"

echo "Publishing release $TAG_NAME..."

# Check if we're on main branch
BRANCH=$(git branch --show-current)
if [ "$BRANCH" != "main" ]; then
    echo "Error: Must be on main branch to publish release (currently on $BRANCH)"
    exit 1
fi

# Check if working directory is clean
if ! git diff-index --quiet HEAD --; then
    echo "Error: Working directory is not clean. Please commit all changes first."
    exit 1
fi

# Check if tag already exists
if git tag -l | grep -q "$TAG_NAME"; then
    echo "Error: Tag $TAG_NAME already exists"
    exit 1
fi

# Create and push tag
echo "Creating tag $TAG_NAME..."
git tag "$TAG_NAME"

echo "Pushing tag to remote..."
git push origin "$TAG_NAME"

echo "Release $TAG_NAME published successfully!"
echo "GitHub Actions should now build and create the release."
```

## File: `claude-history-tool/tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "module": "ESNext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": false,
    "jsx": "react-jsx"
  },
  "include": [
    "src/renderer/**/*",
    "src/types/**/*"
  ],
  "exclude": [
    "node_modules",
    "dist"
  ]
}
```

## File: `claude-history-tool/tsconfig.main.json`
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "lib": ["ES2020"],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "module": "CommonJS",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": false,
    "skipLibCheck": true,
    "outDir": "dist"
  },
  "include": [
    "src/main/**/*",
    "src/types/**/*"
  ],
  "exclude": [
    "node_modules",
    "dist",
    "src/renderer"
  ]
}
```

## File: `claude-history-tool/vitest.config.ts`
```typescript
import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: ['./src/test/setup.ts'],
    pool: 'forks',
    isolate: true,
  },
});
```

## File: `claude-history-tool/webpack.main.config.js`
```javascript
const path = require('path');
const nodeExternals = require('webpack-node-externals');

module.exports = {
  target: 'electron-main',
  mode: process.env.NODE_ENV || 'development',
  entry: {
    main: './src/main/main.ts',
    preload: './src/main/preload.ts',
  },
  output: {
    path: path.resolve(__dirname, 'dist/main'),
    filename: '[name].js',
  },
  resolve: {
    extensions: ['.ts', '.js'],
  },
  module: {
    rules: [
      {
        test: /\.ts$/,
        use: {
          loader: 'ts-loader',
          options: {
            configFile: 'tsconfig.main.json',
          },
        },
        exclude: /node_modules/,
      },
    ],
  },
  externals: [nodeExternals()],
  node: {
    __dirname: false,
    __filename: false,
  },
  devtool: process.env.NODE_ENV === 'production' ? false : 'source-map',
};
```

## File: `claude-history-tool/webpack.renderer.config.js`
```javascript
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  target: 'electron-renderer',
  mode: process.env.NODE_ENV || 'development',
  entry: './src/renderer/App.tsx',
  output: {
    path: path.resolve(__dirname, 'dist/renderer'),
    filename: 'renderer.js',
    clean: true,
  },
  resolve: {
    extensions: ['.tsx', '.ts', '.js', '.jsx'],
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: {
          loader: 'ts-loader',
          options: {
            configFile: 'tsconfig.json',
          },
        },
        exclude: /node_modules/,
      },
      {
        test: /\.s?css$/,
        use: ['style-loader', 'css-loader', 'sass-loader'],
      },
      {
        test: /\.(png|jpe?g|gif|svg|eot|ttf|woff|woff2)$/i,
        type: 'vault/assets/resource',
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/renderer/index.html',
      filename: 'index.html',
    }),
  ],
  devServer: {
    port: process.env.RENDERER_PORT || 3447,
    hot: true,
    historyApiFallback: true,
  },
  devtool: process.env.NODE_ENV === 'production' ? false : 'source-map',
};
```

## File: `claude-history-tool/assets/entitlements.mac.plist`
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>com.apple.security.cs.allow-jit</key>
    <true/>
    <key>com.apple.security.cs.allow-unsigned-executable-memory</key>
    <true/>
    <key>com.apple.security.cs.disable-library-validation</key>
    <true/>
    <key>com.apple.security.cs.allow-dyld-environment-variables</key>
    <true/>
  </dict>
</plist>
```

## File: `claude-history-tool/src/style.scss`
```scss
// SCSS Variables
// Primary Colors
$color-primary: #2D5CDB;
$color-primary-hover: #1E4CC7;
$color-primary-light: #E8F0FF;

// Neutral Colors
$color-neutral-50: #FAFBFC;
$color-neutral-100: #F5F6F8;
$color-neutral-200: #E8EAED;
$color-neutral-300: #D1D5DB;
$color-neutral-400: #9CA3AF;
$color-neutral-500: #6B7280;
$color-neutral-600: #4B5563;
$color-neutral-700: #374151;
$color-neutral-800: #1F2937;
$color-neutral-900: #111827;

// Semantic Colors
$color-success: #059669;
$color-success-light: #ECFDF5;
$color-warning: #D97706;
$color-warning-light: #FFFBEB;
$color-error: #DC2626;
$color-error-light: #FEF2F2;
$color-info: #2563EB;
$color-info-light: #EFF6FF;

// Typography Colors
$color-text-primary: $color-neutral-900;
$color-text-secondary: $color-neutral-600;
$color-text-tertiary: $color-neutral-500;
$color-text-inverse: #FFFFFF;

// Background Colors
$color-bg-primary: #FFFFFF;
$color-bg-secondary: rgb(250, 249, 245);
$color-bg-tertiary: $color-neutral-100;
$color-bg-overlay: rgba(0, 0, 0, 0.5);

// Border Colors
$color-border-primary: $color-neutral-200;
$color-border-secondary: $color-neutral-300;
$color-border-secondary-light: $color-neutral-200;
$color-border-hover: $color-primary;

// Typography
$font-family-base: 'Lexend Deca', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
$font-family-mono: 'SF Mono', Monaco, 'Cascadia Code', 'Roboto Mono', Consolas, 'Courier New', monospace;

// Font Sizes
$font-size-xs: 0.6875rem; // 11px
$font-size-sm: 0.75rem;   // 12px
$font-size-base: 0.8125rem; // 13px
$font-size-md: 0.875rem;  // 14px
$font-size-lg: 0.9375rem; // 15px
$font-size-xl: 1rem;      // 16px
$font-size-2xl: 1.125rem; // 18px
$font-size-3xl: 1.25rem;  // 20px
$font-size-4xl: 1.5rem;   // 24px

// Line Heights
$line-height-tight: 1.2;
$line-height-normal: 1.4;
$line-height-relaxed: 1.6;

// Font Weights
$font-weight-normal: 400;
$font-weight-medium: 500;
$font-weight-semibold: 600;
$font-weight-bold: 700;

// Spacing
$spacing-xs: 0.25rem;  // 4px
$spacing-sm: 0.5rem;   // 8px
$spacing-md: 0.75rem;  // 12px
$spacing-lg: 1rem;     // 16px
$spacing-xl: 1.25rem;  // 20px
$spacing-2xl: 1.5rem;  // 24px
$spacing-3xl: 2rem;    // 32px
$spacing-4xl: 2.5rem;  // 40px
$spacing-5xl: 3rem;    // 48px

// Border Radius
$radius-sm: 0.25rem;   // 4px
$radius-md: 0.375rem;  // 6px
$radius-lg: 0.5rem;    // 8px
$radius-xl: 0.75rem;   // 12px
$radius-2xl: 1rem;     // 16px

// Shadows
$shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
$shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
$shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
$shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
$shadow-card: 0 2px 8px 0 rgba(0, 0, 0, 0.08), 0 1px 3px 0 rgba(0, 0, 0, 0.05);

// Transitions
$transition-fast: 0.15s ease-in-out;
$transition-normal: 0.2s ease-in-out;
$transition-slow: 0.3s ease-in-out;

// Base Reset and Typography
* {
  box-sizing: border-box;
}

html {
  font-size: 16px;
}

body {
  margin: 0;
  padding: 0;
  font-family: $font-family-base;
  font-size: $font-size-base;
  line-height: $line-height-normal;
  color: $color-text-primary;
  background-color: $color-bg-secondary;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

// Typography Components
h1, h2, h3, h4, h5, h6 {
  margin: 0;
  font-weight: $font-weight-semibold;
  line-height: $line-height-tight;
  color: $color-text-primary;
}

.heading-1 {
  font-size: $font-size-4xl;
  font-weight: $font-weight-bold;
  margin-bottom: $spacing-xl;
}

.heading-2 {
  font-size: $font-size-3xl;
  font-weight: $font-weight-semibold;
  margin-bottom: $spacing-lg;
}

.heading-3 {
  font-size: $font-size-2xl;
  font-weight: $font-weight-semibold;
  margin-bottom: $spacing-md;
}

.heading-4 {
  font-size: $font-size-xl;
  font-weight: $font-weight-medium;
  margin-bottom: $spacing-sm;
}

.text-primary {
  color: $color-text-primary;
}

.text-secondary {
  color: $color-text-secondary;
}

.text-tertiary {
  color: $color-text-tertiary;
}

.text-sm {
  font-size: $font-size-sm;
}

.text-md {
  font-size: $font-size-md;
}

.text-lg {
  font-size: $font-size-lg;
}

.text-mono {
  font-family: $font-family-mono;
}

// Atomic Utility Classes
.p-xs { padding: $spacing-xs; }
.p-sm { padding: $spacing-sm; }
.p-md { padding: $spacing-md; }
.p-lg { padding: $spacing-lg; }
.p-xl { padding: $spacing-xl; }
.p-2xl { padding: $spacing-2xl; }

// Tailwind-like utility classes
.p-1 { padding: 0.25rem; }
.p-2 { padding: 0.5rem; }
.p-3 { padding: 0.75rem; }

.px-xs { padding-left: $spacing-xs; padding-right: $spacing-xs; }
.px-sm { padding-left: $spacing-sm; padding-right: $spacing-sm; }
.px-md { padding-left: $spacing-md; padding-right: $spacing-md; }
.px-lg { padding-left: $spacing-lg; padding-right: $spacing-lg; }
.px-xl { padding-left: $spacing-xl; padding-right: $spacing-xl; }

.py-xs { padding-top: $spacing-xs; padding-bottom: $spacing-xs; }
.py-sm { padding-top: $spacing-sm; padding-bottom: $spacing-sm; }
.py-md { padding-top: $spacing-md; padding-bottom: $spacing-md; }
.py-lg { padding-top: $spacing-lg; padding-bottom: $spacing-lg; }
.py-xl { padding-top: $spacing-xl; padding-bottom: $spacing-xl; }

.m-xs { margin: $spacing-xs; }
.m-sm { margin: $spacing-sm; }
.m-md { margin: $spacing-md; }
.m-lg { margin: $spacing-lg; }
.m-xl { margin: $spacing-xl; }

.m-1 { margin: 0.25rem; }
.m-2 { margin: 0.5rem; }
.m-3 { margin: 0.75rem; }

.mb-xs { margin-bottom: $spacing-xs; }
.mb-sm { margin-bottom: $spacing-sm; }
.mb-md { margin-bottom: $spacing-md; }
.mb-lg { margin-bottom: $spacing-lg; }
.mb-xl { margin-bottom: $spacing-xl; }

.mt-xs { margin-top: $spacing-xs; }
.mt-sm { margin-top: $spacing-sm; }
.mt-md { margin-top: $spacing-md; }
.mt-lg { margin-top: $spacing-lg; }
.mt-xl { margin-top: $spacing-xl; }

// Layout Utilities
.flex { display: flex; }
.flex-col { flex-direction: column; }
.flex-row { flex-direction: row; }
.items-center { align-items: center; }
.items-start { align-items: flex-start; }
.items-end { align-items: flex-end; }
.justify-center { justify-content: center; }
.justify-between { justify-content: space-between; }
.justify-start { justify-content: flex-start; }
.justify-end { justify-content: flex-end; }
.gap-xs { gap: $spacing-xs; }
.gap-sm { gap: $spacing-sm; }
.gap-md { gap: $spacing-md; }
.gap-lg { gap: $spacing-lg; }

.w-full { width: 100%; }
.h-full { height: 100%; }
.h-screen { height: 100vh; }
.flex-1 { flex: 1; }

.overflow-auto { overflow: auto; }
.overflow-hidden { overflow: hidden; }

.cursor-pointer { cursor: pointer; }
.user-select-none { user-select: none; }

// Component Styles

// ChatList Component
.ChatList {
  padding: $spacing-xl;
  height: 100%;
  overflow: auto;
  background-color: $color-bg-secondary;
  
  .ChatList__header {
    margin-top: 0;
    margin-bottom: $spacing-lg;
    color: $color-text-primary;
    font-size: $font-size-2xl;
    font-weight: $font-weight-semibold;
  }
  
  .ChatList__search {
    position: relative;
    margin-bottom: $spacing-xl;
    
    .ChatList__search-input {
      width: 100%;
      padding: $spacing-md $spacing-lg;
      padding-right: 40px;
      border: 1px solid $color-border-primary;
      border-radius: $radius-lg;
      font-size: $font-size-md;
      font-family: $font-family-base;
      background-color: $color-bg-primary;
      color: $color-text-primary;
      transition: all $transition-fast;
      
      &:focus {
        outline: none;
        border-color: $color-primary;
        box-shadow: 0 0 0 3px rgba($color-primary, 0.1);
      }
      
      &::placeholder {
        color: $color-text-tertiary;
      }
    }
    
    .ChatList__search-clear {
      position: absolute;
      right: $spacing-md;
      top: 50%;
      transform: translateY(-50%);
      background: none;
      border: none;
      color: $color-text-tertiary;
      cursor: pointer;
      padding: $spacing-xs;
      border-radius: $radius-sm;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all $transition-fast;
      
      &:hover {
        color: $color-text-secondary;
        background-color: $color-bg-tertiary;
      }
      
      svg {
        width: 16px;
        height: 16px;
      }
    }
  }
  
  .ChatList__empty {
    text-align: center;
    margin-top: $spacing-5xl;
    color: $color-text-secondary;
    font-size: $font-size-md;
  }
  
  .ChatList__project {
    margin-bottom: $spacing-xl;
    
    .ChatList__project-header {
      font-size: $font-size-md;
      color: $color-text-primary;
      margin-bottom: $spacing-md;
      border-bottom: 1px solid $color-border-primary;
      padding-bottom: $spacing-sm;
      cursor: pointer;
      display: flex;
      align-items: center;
      user-select: none;
      transition: all $transition-fast;
      
      &:hover {
        color: $color-primary;
      }
      
      .ChatList__project-arrow {
        margin-right: $spacing-sm;
        font-size: $font-size-xs;
        color: $color-text-tertiary;
        transition: transform $transition-fast;
        
        &--expanded {
          transform: rotate(90deg);
        }
      }
      
      .ChatList__project-name {
        font-weight: $font-weight-medium;
      }
      
      .ChatList__project-count {
        margin-left: $spacing-md;
        font-size: $font-size-xs;
        color: $color-text-tertiary;
        font-weight: $font-weight-normal;
      }
    }
    
    .ChatList__session {
      background-color: $color-bg-primary;
      border: 1px solid $color-border-primary;
      border-radius: $radius-lg;
      padding: $spacing-lg;
      margin-bottom: $spacing-md;
      cursor: pointer;
      transition: all $transition-fast;
      box-shadow: $shadow-card;
      display: block;
      text-decoration: none;
      color: inherit;
      
      &:hover {
        border-color: $color-border-hover;
        box-shadow: $shadow-md;
        text-decoration: none;
        color: inherit;
      }
      
      &:visited {
        color: inherit;
      }
      
      .ChatList__session-content {
        font-size: $font-size-sm;
        color: $color-text-primary;
        margin-bottom: $spacing-sm;
        line-height: $line-height-normal;
      }
      
      .ChatList__session-meta {
        display: flex;
        justify-content: space-between;
        font-size: $font-size-xs;
        color: $color-text-tertiary;
      }
    }
  }
}

// MessageCard Component
.MessageCard {
  margin-bottom: $spacing-lg;
  
  &.message-foreground {
    background-color: $color-bg-primary;
    border: 1px solid $color-border-primary;
    border-radius: $radius-lg;
    padding: $spacing-lg;
    box-shadow: $shadow-card;

    .header {
      margin-bottom: $spacing-md;
    }
  }
  
  &.message-background {
    margin-bottom: $spacing-sm;
    background-color: transparent;
    border: 1px solid $color-border-secondary-light;
    border-radius: $radius-lg;
    padding: $spacing-sm;
    box-shadow: none;
  }
  
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    
    &-left {
      display: flex;
      align-items: center;
      gap: $spacing-md;
    }
  }
  
  .badge {
    padding: $spacing-xs $spacing-sm;
    border-radius: $radius-xl;
    font-size: $font-size-xs;
    font-weight: $font-weight-semibold;
    
    &--user {
      background-color: $color-info-light;
      color: $color-info;
    }
    
    &--assistant {
      background-color: $color-primary-light;
      color: $color-primary;
    }
  }
  
  .timestamp {
    font-size: $font-size-xs;
    color: $color-text-tertiary;
  }
  
  .content {
    white-space: pre-wrap;
    line-height: $line-height-relaxed;
    margin-bottom: $spacing-md;
    font-size: $font-size-md;
  }

  pre {
    background-color: $color-bg-tertiary;
    border-radius: $radius-sm;
    font-family: $font-family-mono;
    font-size: $font-size-xs;
    overflow: auto;
    padding: $spacing-sm;
    margin-top: $spacing-md;
    white-space: pre-wrap;
    word-wrap: break-word;
  }
  
  .MessageCard__tool {
    margin-bottom: $spacing-md;
    
    .MessageCard__tool-use {
      background-color: $color-info-light;
      border: 1px solid $color-info;
      border-radius: $radius-md;
      padding: $spacing-sm;
      margin-bottom: $spacing-xs;
      
      .MessageCard__tool-header {
        font-weight: $font-weight-semibold;
        margin-bottom: $spacing-xs;
        font-size: $font-size-sm;
      }
      
      .MessageCard__tool-id {
        font-size: $font-size-xs;
        color: $color-text-tertiary;
        margin-bottom: $spacing-xs;
      }
      
      .MessageCard__tool-input {
        background-color: $color-bg-tertiary;
        padding: $spacing-sm;
        border-radius: $radius-sm;
        font-family: $font-family-mono;
        font-size: $font-size-xs;
        overflow: auto;
        white-space: pre-wrap;
        word-wrap: break-word;
      }
    }
    
    .MessageCard__tool-result {
      background-color: $color-success-light;
      border: 1px solid $color-success;
      border-radius: $radius-md;
      padding: $spacing-sm;
      margin-bottom: $spacing-xs;
      
      .MessageCard__tool-header {
        font-weight: $font-weight-semibold;
        margin-bottom: $spacing-xs;
        font-size: $font-size-sm;
      }
      
      .MessageCard__tool-output {
        background-color: $color-bg-tertiary;
        padding: $spacing-sm;
        border-radius: $radius-sm;
        font-family: $font-family-mono;
        font-size: $font-size-xs;
        overflow: auto;
        white-space: pre-wrap;
        word-wrap: break-word;
      }
    }
  }
  
  .MessageCard__expand-button {
    display: flex;
    justify-content: flex-start;
    margin-top: $spacing-md;
    padding-top: $spacing-md;
    border-top: 1px solid $color-border-primary;
  }
  
  .MessageCard__usage {
    background-color: $color-bg-tertiary;
    padding: $spacing-sm;
    border-radius: $radius-sm;
    font-size: $font-size-xs;
    color: $color-text-tertiary;
    margin-top: $spacing-md;
  }
}

// Badge Component
.Badge {
  padding: $spacing-xs $spacing-sm;
  border-radius: $radius-xl;
  font-size: $font-size-xs;
  font-weight: $font-weight-semibold;
  display: inline-block;
  
  &--user {
    background-color: $color-info-light;
    color: $color-info;
  }
  
  &--assistant {
    background-color: $color-primary-light;
    color: $color-primary;
  }
  
  &--internal {
    background-color: $color-neutral-200;
    color: $color-neutral-600;
  }
  
  &--hook {
    background-color: $color-warning-light;
    color: $color-warning;
  }
  
  &--tool {
    background-color: $color-success-light;
    color: $color-success;
  }
  
  &--tool-result {
    background-color: $color-success-light;
    color: $color-success;
  }
}

// ChatViewer Component
.ChatViewer {
  height: 100%;
  overflow: auto;
  background-color: $color-bg-secondary;
  
  .ChatViewer__header {
    background-color: $color-bg-primary;
    padding: $spacing-xl;
    border-bottom: 1px solid $color-border-primary;
    margin-bottom: $spacing-xl;
    
    .ChatViewer__title {
      margin: 0;
      margin-bottom: $spacing-md;
      font-size: $font-size-2xl;
      font-weight: $font-weight-semibold;
    }
    
    .ChatViewer__meta {
      font-size: $font-size-sm;
      color: $color-text-secondary;
      
      > div {
        margin-bottom: $spacing-xs;
      }
    }
  }
  
  .ChatViewer__content {
    padding: 0 $spacing-xl $spacing-xl;
  }
  
  .ChatViewer__loading {
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: $color-bg-secondary;
  }
}

// LoadingSpinner Component
.LoadingSpinner {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: $spacing-md;
  
  .LoadingSpinner__spinner {
    border: 2px solid $color-border-primary;
    border-top: 2px solid $color-primary;
    border-radius: 50%;
    animation: spin 1s linear infinite;
  }
  
  .LoadingSpinner__message {
    font-size: $font-size-sm;
    color: $color-text-secondary;
  }
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

// Button Components
.btn {
  padding: $spacing-sm $spacing-lg;
  border: 1px solid $color-border-primary;
  border-radius: $radius-md;
  font-size: $font-size-sm;
  font-weight: $font-weight-medium;
  cursor: pointer;
  transition: all $transition-fast;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  
  &:hover {
    transform: translateY(-1px);
    box-shadow: $shadow-md;
  }
  
  &:active {
    transform: translateY(0);
  }
  
  &--primary {
    background-color: $color-primary;
    color: $color-text-inverse;
    border-color: $color-primary;
    
    &:hover {
      background-color: $color-primary-hover;
      border-color: $color-primary-hover;
    }
  }
  
  &--secondary {
    background-color: $color-bg-primary;
    color: $color-text-primary;
    
    &:hover {
      background-color: $color-bg-tertiary;
    }
  }
  
  &--small {
    padding: $spacing-xs $spacing-sm;
    font-size: $font-size-xs;
  }
}

// Atomic Button Classes
.button {
  border: none;
  border-radius: $radius-sm;
  font-weight: $font-weight-medium;
  cursor: pointer;
  transition: all $transition-fast;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  
  &:hover {
    transform: translateY(-1px);
    box-shadow: $shadow-sm;
  }
  
  &:active {
    transform: translateY(0);
  }
}

.button-primary {
  background-color: $color-primary;
  color: $color-text-inverse;
  
  &:hover {
    background-color: $color-primary-hover;
  }
}

.button-secondary {
  background-color: $color-neutral-300;
  color: $color-text-primary;
  
  &:hover {
    background-color: $color-neutral-400;
  }
}

.button-xs {
  padding: $spacing-xs $spacing-sm;
  font-size: $font-size-xs;
}

// Scrollbar Styling
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: $color-bg-tertiary;
}

::-webkit-scrollbar-thumb {
  background: $color-neutral-400;
  border-radius: $radius-sm;
}

::-webkit-scrollbar-thumb:hover {
  background: $color-neutral-500;
}

// LeftSidebar Component
.left-sidebar {
  width: 60px;
  background-color: #8B4513;
  padding: $spacing-lg $spacing-sm;
  display: flex;
  flex-direction: column;
  gap: $spacing-lg;
  border-right: 1px solid $color-border-primary;
  
  .sidebar-button {
    width: 44px;
    height: 44px;
    background-color: transparent;
    border: none;
    border-radius: $radius-sm;
    color: rgba(255, 255, 255, 0.7);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all $transition-fast;
    
    &:hover {
      background-color: rgba(255, 255, 255, 0.1);
      color: rgba(255, 255, 255, 0.9);
    }
    
    &.active {
      background-color: rgba(255, 255, 255, 0.2);
      color: white;
    }
  }
}

// Modal Component
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: $color-bg-overlay;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  
  .modal-content {
    background-color: $color-bg-primary;
    border-radius: $radius-lg;
    box-shadow: $shadow-xl;
    max-width: 90vw;
    max-height: 90vh;
    overflow: auto;
    position: relative;
  }
}

// Upgrade Banner Component
.upgrade-banner {
  background-color: $color-info-light;
  border-bottom: 1px solid $color-info;
  padding: $spacing-md $spacing-xl;
  position: relative;
  z-index: 100;
  
  .upgrade-banner__content {
    margin-right: $spacing-3xl;
    
    h1, h2, h3, h4, h5, h6 {
      margin: 0 0 $spacing-sm 0;
      color: $color-info;
    }
    
    p {
      margin: 0;
      color: $color-text-primary;
    }
    
    a {
      color: $color-info;
      text-decoration: underline;
      
      &:hover {
        color: $color-primary-hover;
      }
    }
  }
  
  .upgrade-banner__close {
    position: absolute;
    top: $spacing-md;
    right: $spacing-lg;
    background: none;
    border: none;
    font-size: $font-size-xl;
    color: $color-text-tertiary;
    cursor: pointer;
    padding: $spacing-xs;
    line-height: 1;
    transition: color $transition-fast;
    
    &:hover {
      color: $color-text-primary;
    }
  }
}

// Upgrade Modal Component
.upgrade-modal {
  position: relative;
  padding: $spacing-2xl;
  min-width: 400px;
  max-width: 600px;
  
  .upgrade-modal__close {
    position: absolute;
    top: $spacing-lg;
    right: $spacing-lg;
    background: none;
    border: none;
    font-size: $font-size-xl;
    color: $color-text-tertiary;
    cursor: pointer;
    padding: $spacing-xs;
    line-height: 1;
    transition: color $transition-fast;
    
    &:hover {
      color: $color-text-primary;
    }
  }
  
  .upgrade-modal__content {
    margin-top: $spacing-lg;
    
    h1, h2, h3, h4, h5, h6 {
      margin: 0 0 $spacing-lg 0;
      color: $color-text-primary;
    }
    
    p {
      margin: 0 0 $spacing-md 0;
      line-height: $line-height-relaxed;
    }
    
    a {
      color: $color-primary;
      text-decoration: underline;
      
      &:hover {
        color: $color-primary-hover;
      }
    }
    
    .button, button {
      margin-top: $spacing-lg;
    }
  }
}

// Analytics Component
.analytics-container {
  padding: $spacing-xl;
  height: 100%;
  overflow: auto;
  background-color: $color-bg-secondary;
  
  .analytics-header {
    margin-bottom: $spacing-2xl;
    
    h1 {
      font-size: $font-size-3xl;
      font-weight: $font-weight-bold;
      color: $color-text-primary;
      margin-bottom: $spacing-sm;
    }
    
    p {
      font-size: $font-size-md;
      color: $color-text-secondary;
      margin: 0;
    }
  }
  
  .analytics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: $spacing-xl;
    
    .analytics-card {
      background-color: $color-bg-primary;
      border: 1px solid $color-border-primary;
      border-radius: $radius-lg;
      padding: $spacing-xl;
      box-shadow: $shadow-card;
      
      h3 {
        font-size: $font-size-lg;
        font-weight: $font-weight-semibold;
        color: $color-text-primary;
        margin-bottom: $spacing-lg;
      }
      
      .tool-stats, .token-stats, .chat-stats {
        .tool-item, .token-item, .stat-item {
          display: flex;
          justify-content: space-between;
          align-items: center;
          padding: $spacing-sm 0;
          border-bottom: 1px solid $color-border-primary;
          
          &:last-child {
            border-bottom: none;
          }
          
          .tool-name, .stat-label {
            font-size: $font-size-sm;
            color: $color-text-primary;
          }
          
          .tool-count, .token-cost, .stat-value {
            font-size: $font-size-sm;
            font-weight: $font-weight-medium;
            color: $color-text-secondary;
          }
        }
      }
      
      .time-stats {
        p {
          font-size: $font-size-sm;
          color: $color-text-secondary;
          text-align: center;
          padding: $spacing-2xl;
          background-color: $color-bg-tertiary;
          border-radius: $radius-md;
          margin: 0;
        }
      }
    }
  }
}
```

## File: `claude-history-tool/src/components/AnalyticsPanel.tsx`
```tsx
import React from 'react';
import { useQuery } from '@tanstack/react-query';
import { LoadingSpinner } from './LoadingSpinner';
import { AnalyticsData } from '../main/getAnalytics';

export const AnalyticsPanel: React.FC = () => {
  const { data: analytics, isLoading, error } = useQuery({
    queryKey: ['analytics'],
    queryFn: async (): Promise<AnalyticsData> => {
      console.log('calling getAnalytics');
      return await window.electronAPI.getAnalytics();
    },
  });

  if (isLoading) {
    return (
      <div className="h-full flex items-center justify-center" style={{ backgroundColor: 'var(--color-bg-secondary)' }}>
        <LoadingSpinner 
          size={50} 
          message="Calculating analytics..." 
        />
      </div>
    );
  }

  if (error) {
    return (
      <div className="analytics-container">
        <div className="analytics-header">
          <h1>Analytics</h1>
          <p style={{ color: 'var(--color-error)' }}>Failed to load analytics: {String(error)}</p>
        </div>
      </div>
    );
  }

  if (!analytics) {
    return (
      <div className="analytics-container">
        <div className="analytics-header">
          <h1>Analytics</h1>
          <p>No analytics data available</p>
        </div>
      </div>
    );
  }
  return (
    <div className="analytics-container">
      <div className="analytics-header">
        <h1>Analytics</h1>
      </div>
      
      <div className="analytics-grid">
        <div className="analytics-card">
          <h3>Most Used Tools</h3>
          <div className="tool-stats">
            {analytics.toolUsage.length > 0 ? (
              analytics.toolUsage.map((tool, index) => (
                <div key={index} className="tool-item">
                  <span className="tool-name">{tool.name}</span>
                  <span className="tool-count">{tool.count} uses</span>
                </div>
              ))
            ) : (
              <div className="tool-item">
                <span className="tool-name">No tool usage data found</span>
                <span className="tool-count">-</span>
              </div>
            )}
          </div>
        </div>
        
        <div className="analytics-card">
          <h3>Token Usage</h3>
          <div className="token-stats">
            {analytics.tokenUsage.length > 0 ? (
              analytics.tokenUsage.map((token, index) => (
                <div key={index} className="token-item">
                  <span className="tool-name">{token.name}</span>
                  <span className="token-cost">{token.tokens.toLocaleString()} tokens</span>
                </div>
              ))
            ) : (
              <div className="token-item">
                <span className="tool-name">No token usage data found</span>
                <span className="token-cost">-</span>
              </div>
            )}
          </div>
        </div>
        
        <div className="analytics-card">
          <h3>Chat Statistics</h3>
          <div className="chat-stats">
            <div className="stat-item">
              <span className="stat-label">Total Chats</span>
              <span className="stat-value">{analytics.chatStats.totalChats}</span>
            </div>
            <div className="stat-item">
              <span className="stat-label">Total Messages</span>
              <span className="stat-value">{analytics.chatStats.totalMessages}</span>
            </div>
            <div className="stat-item">
              <span className="stat-label">Avg Messages/Chat</span>
              <span className="stat-value">{analytics.chatStats.averageMessagesPerChat}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
```

## File: `claude-history-tool/src/components/Badge.tsx`
```tsx
import React from 'react';

export enum BadgeType {
  User = 'user',
  Assistant = 'assistant',
  Internal = 'internal',
  Hook = 'hook',
  Tool = 'tool',
  ToolResult = 'tool-result'
}

interface BadgeProps {
  type: BadgeType;
  className?: string;
  toolNames?: string[];
}

export const Badge: React.FC<BadgeProps> = ({ type, className = '', toolNames = [] }) => {
  const getBadgeContent = () => {
    switch (type) {
      case BadgeType.User:
        return '👤 User';
      case BadgeType.Assistant:
        return '🤖 Assistant';
      case BadgeType.Internal:
        return '🔧 Internal';
      case BadgeType.Hook:
        return '🪝 Hook';
      case BadgeType.Tool:
        return toolNames.length > 0 ? `🔧 Tool: ${toolNames.join(', ')}` : '🔧 Tool';
      case BadgeType.ToolResult:
        return '📤 ToolResult';
      default:
        return '';
    }
  };

  const getBadgeClass = () => {
    switch (type) {
      case BadgeType.User:
        return 'Badge--user';
      case BadgeType.Assistant:
        return 'Badge--assistant';
      case BadgeType.Internal:
        return 'Badge--internal';
      case BadgeType.Hook:
        return 'Badge--hook';
      case BadgeType.Tool:
        return 'Badge--tool';
      case BadgeType.ToolResult:
        return 'Badge--tool-result';
      default:
        return '';
    }
  };

  return (
    <span className={`Badge ${getBadgeClass()} ${className}`}>
      {getBadgeContent()}
    </span>
  );
};
```

## File: `claude-history-tool/src/components/Button.stories.tsx`
```tsx
import type { Meta, StoryObj } from '@storybook/react';
import { Button } from './Button';

const meta: Meta<typeof Button> = {
  title: 'Components/Button',
  component: Button,
  parameters: {
    layout: 'padded',
  },
  argTypes: {
    onClick: { action: 'clicked' },
  },
};

export default meta;
type Story = StoryObj<typeof meta>;

export const PrimaryXS: Story = {
  args: {
    children: 'Primary XS',
    className: 'button-primary button-xs',
  },
};

export const SecondaryXS: Story = {
  args: {
    children: 'Secondary XS',
    className: 'button-secondary button-xs',
  },
};

export const PrimaryOnly: Story = {
  args: {
    children: 'Primary',
    className: 'button-primary',
  },
};

export const SecondaryOnly: Story = {
  args: {
    children: 'Secondary',
    className: 'button-secondary',
  },
};

export const BaseButton: Story = {
  args: {
    children: 'Base Button',
    className: '',
  },
};

export const ButtonGroup: Story = {
  render: () => (
    <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
      <Button className="button-primary button-xs">Save</Button>
      <Button className="button-secondary button-xs">Cancel</Button>
      <Button className="button-primary">Submit</Button>
      <Button className="button-secondary">Reset</Button>
    </div>
  ),
};
```

## File: `claude-history-tool/src/components/Button.tsx`
```tsx
import React from 'react';

interface ButtonProps {
  onClick: () => void;
  children: React.ReactNode;
  className?: string;
}

export const Button: React.FC<ButtonProps> = ({ 
  onClick, 
  children, 
  className = '' 
}) => {
  return (
    <button
      onClick={onClick}
      className={`button ${className}`}
    >
      {children}
    </button>
  );
};
```

## File: `claude-history-tool/src/components/ChatDetailsPanel.tsx`
```tsx
import React from 'react';
import { ChatSession } from '../types';
import { ChatSessionView } from './ChatSessionView';

interface ChatDetailsPanelProps {
  session: ChatSession;
  onBackToList: () => void;
}

export const ChatDetailsPanel: React.FC<ChatDetailsPanelProps> = ({ 
  session, 
  onBackToList 
}) => {
  return (
    <div className="h-full flex flex-col">
      <header className="flex items-center gap-md px-xl py-md" style={{
        backgroundColor: 'var(--color-bg-primary)',
        borderBottom: '1px solid var(--color-border-primary)'
      }}>
        <button 
          onClick={onBackToList}
          className="btn btn--secondary btn--small"
        >
          ← Back
        </button>
      </header>
      
      <div className="flex-1 overflow-hidden">
        <ChatSessionView session={session} />
      </div>
    </div>
  );
};
```

## File: `claude-history-tool/src/components/ChatList.stories.tsx`
```tsx
import type { Meta, StoryObj } from '@storybook/react';
import { ChatList } from './ChatList';
import { ProjectDirectory } from '../types';

const meta: Meta<typeof ChatList> = {
  title: 'Components/ChatList',
  component: ChatList,
  parameters: {
    layout: 'fullscreen',
  },
  args: {
    onSessionSelect: (session) => console.log('Selected session:', session),
  },
};

export default meta;
type Story = StoryObj<typeof meta>;

const mockProjects: ProjectDirectory[] = [
  {
    path: '-Users-johndoe-ai-coding-tools-claude-history-tool',
    sessions: [
      {
        sessionId: 'session-1',
        messages: [],
        firstMessageTimestamp: '2025-01-15T10:30:00Z',
        lastMessageTimestamp: '2025-01-15T11:45:00Z',
        projectPath: '-Users-johndoe-ai-coding-tools-claude-history-tool',
        messageCount: 25
      },
      {
        sessionId: 'session-2',
        messages: [],
        firstMessageTimestamp: '2025-01-14T14:20:00Z',
        lastMessageTimestamp: '2025-01-14T15:30:00Z',
        projectPath: '-Users-johndoe-ai-coding-tools-claude-history-tool',
        messageCount: 12
      }
    ]
  },
  {
    path: '-Users-johndoe-web-development-react-app',
    sessions: [
      {
        sessionId: 'session-3',
        messages: [],
        firstMessageTimestamp: '2025-01-13T09:15:00Z',
        lastMessageTimestamp: '2025-01-13T16:45:00Z',
        projectPath: '-Users-johndoe-web-development-react-app',
        messageCount: 87
      }
    ]
  }
];

export const Default: Story = {
  args: {
    projects: mockProjects,
  },
};

export const Empty: Story = {
  args: {
    projects: [],
  },
};

export const SingleProject: Story = {
  args: {
    projects: [mockProjects[0]],
  },
};
```

## File: `claude-history-tool/src/components/ChatList.tsx`
```tsx
import React, { useState, useEffect, useMemo, useCallback } from 'react';
import { useSearchParams, useLocation } from 'react-router-dom';
import { IoClose } from 'react-icons/io5';
import { ProjectDirectory, ChatSession } from '../types';

interface ChatListProps {
  projects: ProjectDirectory[];
  onSessionSelect: (session: ChatSession) => void;
  onRefresh?: () => void;
}

  const getFirstUserMessage = (session: ChatSession): string => {
    const firstUserMessage = session.messages.find(msg => 
      msg.type === 'user' && !msg.isMeta && !msg.internalMessageType
    );

    if (firstUserMessage && firstUserMessage.message && typeof firstUserMessage.message.content === 'string') {
      return firstUserMessage.message.content.slice(0, 100) + '...';
    }
    return 'No user message found';
  };

export const ChatList: React.FC<ChatListProps> = ({ projects, onSessionSelect, onRefresh }) => {
  const [searchParams, setSearchParams] = useSearchParams();
  const location = useLocation();
  const [searchTerm, setSearchTerm] = useState('');
  
  // Initialize expanded projects from URL params
  const [expandedProjects, setExpandedProjects] = useState<Set<string>>(() => {
    const expanded = searchParams.get('expanded');
    return expanded ? new Set(expanded.split(',')) : new Set();
  });

  // Restore scroll position when coming back from a session
  useEffect(() => {
    if (location.state?.scrollPosition) {
      window.scrollTo(0, location.state.scrollPosition);
    }
    if (location.state?.expandedProjects) {
      setExpandedProjects(new Set(location.state.expandedProjects));
    }
  }, [location.state]);

  // Update URL when expanded projects change
  useEffect(() => {
    const expandedArray = Array.from(expandedProjects);
    if (expandedArray.length > 0) {
      setSearchParams({ expanded: expandedArray.join(',') });
    } else {
      setSearchParams({});
    }
  }, [expandedProjects, setSearchParams]);

  const getProjectDisplayName = useCallback((project: ProjectDirectory) => {
    // Try to get the actual path from the first message's cwd
    if (project.sessions.length > 0 && project.sessions[0].messages.length > 0) {
      const firstMessage = project.sessions[0].messages[0];
      if (firstMessage.cwd) {
        return firstMessage.cwd;
      }
    }
    // Fallback to the encoded directory name conversion
    return project.path.replace(/^-Users-[^-]+-/, '').replace(/-/g, '/');
  }, []);
  
  // Filter projects based on search term
  const filteredProjects = useMemo(() => {
    if (!searchTerm.trim()) {
      return projects;
    }
    
    const searchLower = searchTerm.toLowerCase();
    return projects.filter(project => {
      const projectName = getProjectDisplayName(project).toLowerCase();
      const hasMatchingProject = projectName.includes(searchLower);
      
      const hasMatchingSessions = false;
      // future:Also check if any session in the project matches
      
      /*
      const hasMatchingSessions = project.sessions.some(session => {
        const firstMessage = getFirstUserMessage(session).toLowerCase();
        return firstMessage.includes(searchLower);
      });
      */
      
      return hasMatchingProject || hasMatchingSessions;
    });
  }, [projects, searchTerm, getProjectDisplayName]);

  const toggleProject = (projectPath: string) => {
    const newExpanded = new Set(expandedProjects);
    if (newExpanded.has(projectPath)) {
      newExpanded.delete(projectPath);
    } else {
      newExpanded.add(projectPath);
    }
    setExpandedProjects(newExpanded);
  };

  const clearSearch = () => {
    setSearchTerm('');
  };
  const formatTimestamp = (timestamp: string) => {
    const date = new Date(timestamp);
    return date.toLocaleString();
  };


  return (
    <div className="ChatList">
      <h2 className="ChatList__header">Session History</h2>
      
      <div className="ChatList__search">
        <input
          type="text"
          placeholder="Search projects..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="ChatList__search-input"
        />
        {searchTerm && (
          <button
            onClick={clearSearch}
            className="ChatList__search-clear"
            title="Clear search"
          >
            <IoClose />
          </button>
        )}
      </div>
      
      {filteredProjects.length === 0 && projects.length > 0 ? (
        <div className="ChatList__empty">
          <p>No projects found matching "{searchTerm}"</p>
        </div>
      ) : projects.length === 0 ? (
        <div className="ChatList__empty">
          <p>No chat history found in ~/.claude/projects</p>
        </div>
      ) : (
        filteredProjects.map((project) => {
          const isExpanded = expandedProjects.has(project.path);
          return (
            <div key={project.path} className="ChatList__project">
              <div
                onClick={() => toggleProject(project.path)}
                className="ChatList__project-header"
              >
                <span className={`ChatList__project-arrow ${isExpanded ? 'ChatList__project-arrow--expanded' : ''}`}>
                  ▶
                </span>
                <span className="ChatList__project-name">
                  {getProjectDisplayName(project)}
                </span>
                <span className="ChatList__project-count">
                  ({project.sessions.length} session{project.sessions.length !== 1 ? 's' : ''})
                </span>
              </div>
              
              {isExpanded && project.sessions.map((session) => (
                <a
                  key={session.sessionId}
                  href={`/chat/${session.sessionId}`}
                  onClick={(e) => {
                    e.preventDefault();
                    onSessionSelect(session);
                  }}
                  className="ChatList__session"
                >
                  <div className="ChatList__session-content">
                    {getFirstUserMessage(session)}
                  </div>
                  
                  <div className="ChatList__session-meta">
                    <span>{formatTimestamp(session.lastMessageTimestamp)}</span>
                    <span>{session.messageCount} messages</span>
                  </div>
                </a>
              ))}
            </div>
          );
        })
      )}
    </div>
  );
};
```

## File: `claude-history-tool/src/components/ChatSessionView.stories.tsx`
```tsx
import type { Meta, StoryObj } from '@storybook/react';
import { ChatSessionView } from './ChatSessionView';
import { ChatSession } from '../types';

const meta: Meta<typeof ChatSessionView> = {
  title: 'Components/ChatSessionView',
  component: ChatSessionView,
  parameters: {
    layout: 'fullscreen',
  },
};

export default meta;
type Story = StoryObj<typeof meta>;

const mockSession: ChatSession = {
  sessionId: 'session-123',
  messages: [],
  firstMessageTimestamp: '2025-01-15T10:30:00Z',
  lastMessageTimestamp: '2025-01-15T11:45:00Z',
  projectPath: '-Users-johndoe-ai-coding-tools-claude-history-tool',
  messageCount: 25
};

// Mock the window.electronAPI for Storybook
if (typeof window !== 'undefined') {
  (window as any).electronAPI = {
    getSessionDetails: async (sessionId: string, projectName: string) => {
      // Return mock messages for Storybook
      return [
        {
          parentUuid: null,
          isSidechain: false,
          userType: 'external',
          cwd: '/Users/johndoe/project',
          sessionId: sessionId,
          version: '1.0.0',
          gitBranch: 'main',
          type: 'user',
          message: {
            role: 'user',
            content: 'Help me create a React component for displaying user profiles.',
          },
          uuid: 'user-message-1',
          timestamp: '2025-01-15T10:30:00Z',
        },
        {
          parentUuid: 'user-message-1',
          isSidechain: false,
          userType: 'external',
          cwd: '/Users/johndoe/project',
          sessionId: sessionId,
          version: '1.0.0',
          gitBranch: 'main',
          type: 'assistant',
          message: {
            role: 'assistant',
            content: [
              {
                type: 'text',
                text: 'I\'ll help you create a React component for user profiles. Let me create the component file.'
              },
              {
                type: 'tool_use',
                id: 'tool-1',
                name: 'Write',
                input: {
                  file_path: '/Users/johndoe/project/src/UserProfile.tsx',
                  content: 'React component code here...'
                }
              }
            ],
            id: 'msg-2',
            model: 'claude-3-sonnet',
            usage: {
              input_tokens: 120,
              output_tokens: 180,
              service_tier: 'standard'
            }
          },
          uuid: 'assistant-message-1',
          timestamp: '2025-01-15T10:31:00Z',
        }
      ];
    }
  };
}

export const Default: Story = {
  args: {
    session: mockSession,
  },
};
```

## File: `claude-history-tool/src/components/ChatSessionView.tsx`
```tsx
import React, { useState, useEffect } from 'react';
import { ChatSession, ChatMessage } from '../types';
import { MessageCard } from './MessageCard';
import { LoadingSpinner } from './LoadingSpinner';

interface ChatViewerProps {
  session: ChatSession;
}

export const ChatSessionView: React.FC<ChatViewerProps> = ({ session }) => {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadSessionDetails();
  }, [session.sessionId]);

  const loadSessionDetails = async () => {
    try {
      setLoading(true);
      const data = await window.electronAPI.getSessionDetails(session.sessionId, session.projectPath);
      setMessages(data);
    } catch (error) {
      console.error('Failed to load session details:', error);
    } finally {
      setLoading(false);
    }
  };

  const formatTimestamp = (timestamp: string) => {
    const date = new Date(timestamp);
    return date.toLocaleString();
  };

  const getProjectDisplayName = (session: ChatSession) => {
    // Try to get the actual path from the first message's cwd
    if (session.messages.length > 0) {
      const firstMessage = session.messages[0];
      if (firstMessage.cwd) {
        return firstMessage.cwd;
      }
    }
    // Fallback to the encoded directory name conversion
    return session.projectPath.replace(/^-Users-[^-]+-/, '').replace(/-/g, '/');
  };

  if (loading) {
    return (
      <div className="ChatViewer__loading">
        <LoadingSpinner 
          size={40} 
          message="Loading session details..." 
        />
      </div>
    );
  }

  return (
    <div className="ChatViewer">
      <div className="ChatViewer__header">
        <h2 className="ChatViewer__title">
          {getProjectDisplayName(session)}
        </h2>
        <div className="ChatViewer__meta">
          <div>Session ID: {session.sessionId}</div>
          <div>Started: {formatTimestamp(session.firstMessageTimestamp)}</div>
          <div>Last activity: {formatTimestamp(session.lastMessageTimestamp)}</div>
          <div>{session.messageCount} messages</div>
        </div>
      </div>

      <div className="ChatViewer__content">
        {messages.map((message, index) => (
          <MessageCard 
            key={`${message.uuid}-${index}`} 
            message={message} 
          />
        ))}
      </div>
    </div>
  );
};
```

## File: `claude-history-tool/src/components/CloseButton.tsx`
```tsx
import React from 'react';

interface CloseButtonProps {
  onClose: () => void;
  className?: string;
  ariaLabel?: string;
}

export const CloseButton: React.FC<CloseButtonProps> = ({ 
  onClose, 
  className = '', 
  ariaLabel = 'Close' 
}) => {
  return (
    <button 
      className={className}
      onClick={onClose}
      aria-label={ariaLabel}
    >
      ×
    </button>
  );
};
```

## File: `claude-history-tool/src/components/HtmlContent.tsx`
```tsx
import React from 'react';

interface HtmlContentProps {
  html: string;
  className?: string;
}

export const HtmlContent: React.FC<HtmlContentProps> = ({ html, className = '' }) => {
  return (
    <div 
      className={className}
      dangerouslySetInnerHTML={{ __html: html }}
    />
  );
};
```

## File: `claude-history-tool/src/components/LeftSidebar.tsx`
```tsx
import React from 'react';
import { IoChatbubbles, IoStatsChart } from 'react-icons/io5';

export interface LeftSidebarProps {
  activeView: 'chats' | 'analytics';
  onViewChange: (view: 'chats' | 'analytics') => void;
}

export const LeftSidebar: React.FC<LeftSidebarProps> = ({ activeView, onViewChange }) => {
  return (
    <div className="left-sidebar">
      <button 
        className={`sidebar-button ${activeView === 'chats' ? 'active' : ''}`}
        onClick={() => onViewChange('chats')}
        title="Chats"
      >
        <IoChatbubbles size={24} />
      </button>
      
      <button 
        className={`sidebar-button ${activeView === 'analytics' ? 'active' : ''}`}
        onClick={() => onViewChange('analytics')}
        title="Analytics"
      >
        <IoStatsChart size={24} />
      </button>
    </div>
  );
};
```

## File: `claude-history-tool/src/components/LoadingSpinner.stories.tsx`
```tsx
import type { Meta, StoryObj } from '@storybook/react';
import { LoadingSpinner } from './LoadingSpinner';

const meta: Meta<typeof LoadingSpinner> = {
  title: 'Components/LoadingSpinner',
  component: LoadingSpinner,
  parameters: {
    layout: 'centered',
  },
  argTypes: {
    size: {
      control: {
        type: 'range',
        min: 20,
        max: 100,
        step: 5,
      },
    },
    color: {
      control: {
        type: 'color',
      },
    },
    message: {
      control: {
        type: 'text',
      },
    },
  },
};

export default meta;
type Story = StoryObj<typeof meta>;

export const Default: Story = {
  args: {
    size: 40,
    color: '#007acc',
    message: 'Loading...',
  },
};

export const Large: Story = {
  args: {
    size: 60,
    color: '#007acc',
    message: 'Loading chat history...',
  },
};

export const Small: Story = {
  args: {
    size: 24,
    color: '#007acc',
    message: 'Loading...',
  },
};

export const CustomColor: Story = {
  args: {
    size: 40,
    color: '#ff6b6b',
    message: 'Processing...',
  },
};

export const NoMessage: Story = {
  args: {
    size: 40,
    color: '#007acc',
    message: '',
  },
};

export const ChatHistoryLoading: Story = {
  args: {
    size: 50,
    color: '#007acc',
    message: 'Loading chat history...',
  },
};

export const SessionDetailsLoading: Story = {
  args: {
    size: 40,
    color: '#007acc',
    message: 'Loading session details...',
  },
};
```

## File: `claude-history-tool/src/components/LoadingSpinner.tsx`
```tsx
import React from 'react';

interface LoadingSpinnerProps {
  size?: number;
  color?: string;
  message?: string;
}

export const LoadingSpinner: React.FC<LoadingSpinnerProps> = ({ 
  size = 40, 
  color = '#007acc',
  message = 'Loading...'
}) => {
  return (
    <div className="LoadingSpinner">
      <div
        className="LoadingSpinner__spinner"
        style={{
          width: size,
          height: size
        }}
      />
      {message && (
        <div className="LoadingSpinner__message">
          {message}
        </div>
      )}
    </div>
  );
};
```

## File: `claude-history-tool/src/components/MessageCard.stories.tsx`
```tsx
import type { Meta, StoryObj } from '@storybook/react';
import { MessageCard } from './MessageCard';
import { ChatMessage } from '../types';

const meta: Meta<typeof MessageCard> = {
  title: 'Components/MessageCard',
  component: MessageCard,
  parameters: {
    layout: 'padded',
  },
};

export default meta;
type Story = StoryObj<typeof meta>;

const userMessage: ChatMessage = {
  parentUuid: null,
  isSidechain: false,
  userType: 'external',
  cwd: '/Users/johndoe/project',
  sessionId: 'session-1',
  version: '1.0.0',
  gitBranch: 'main',
  type: 'user',
  message: {
    role: 'user',
    content: 'Help me create a React component for displaying user profiles. It should include a photo, name, email, and bio section.',
  },
  uuid: 'user-message-1',
  timestamp: '2025-01-15T10:30:00Z',
};

const assistantMessage: ChatMessage = {
  parentUuid: 'user-message-1',
  isSidechain: false,
  userType: 'external',
  cwd: '/Users/johndoe/project',
  sessionId: 'session-1',
  version: '1.0.0',
  gitBranch: 'main',
  type: 'assistant',
  message: {
    role: 'assistant',
    content: 'I\'ll help you create a React component for user profiles. Let me create a clean, responsive component with the features you requested.',
    id: 'msg-1',
    model: 'claude-3-sonnet',
    usage: {
      input_tokens: 50,
      output_tokens: 25,
      service_tier: 'standard'
    }
  },
  uuid: 'assistant-message-1',
  timestamp: '2025-01-15T10:31:00Z',
};

const assistantMessageWithTools: ChatMessage = {
  parentUuid: 'user-message-1',
  isSidechain: false,
  userType: 'external',
  cwd: '/Users/johndoe/project',
  sessionId: 'session-1',
  version: '1.0.0',
  gitBranch: 'main',
  type: 'assistant',
  message: {
    role: 'assistant',
    content: [
      {
        type: 'text',
        text: 'I\'ll create a new file for the UserProfile component.'
      },
      {
        type: 'tool_use',
        id: 'tool-1',
        name: 'Write',
        input: {
          file_path: '/Users/johndoe/project/src/UserProfile.tsx',
          content: 'import React from \'react\';\n\ninterface UserProfileProps {\n  name: string;\n  email: string;\n  bio: string;\n  photoUrl: string;\n}\n\nexport const UserProfile: React.FC<UserProfileProps> = ({ name, email, bio, photoUrl }) => {\n  return (\n    <div className="user-profile">\n      <img src={photoUrl} alt={name} />\n      <h2>{name}</h2>\n      <p>{email}</p>\n      <p>{bio}</p>\n    </div>\n  );\n};'
        }
      }
    ],
    id: 'msg-2',
    model: 'claude-3-sonnet',
    usage: {
      input_tokens: 120,
      output_tokens: 180,
      cache_creation_input_tokens: 50,
      service_tier: 'standard'
    }
  },
  uuid: 'assistant-message-2',
  timestamp: '2025-01-15T10:32:00Z',
};

export const UserMessage: Story = {
  args: {
    message: userMessage,
  },
};

export const AssistantMessage: Story = {
  args: {
    message: assistantMessage,
  },
};

export const AssistantMessageWithTools: Story = {
  args: {
    message: assistantMessageWithTools,
  },
};

const metaMessage: ChatMessage = {
  parentUuid: 'user-message-1',
  isSidechain: false,
  userType: 'external',
  cwd: '/Users/johndoe/project',
  sessionId: 'session-1',
  version: '1.0.0',
  gitBranch: 'main',
  type: 'system',
  content: 'PreToolUse:Edit [/Users/johndoe/project/src/components/Button.tsx] completed successfully',
  isMeta: true,
  level: 'info',
  toolUseID: 'toolu_01ExampleToolUse',
  uuid: 'meta-message-1',
  timestamp: '2025-01-15T10:33:00Z',
};

const visibleMetaMessage: ChatMessage = {
  parentUuid: 'user-message-1',
  isSidechain: false,
  userType: 'external',
  cwd: '/Users/johndoe/project',
  sessionId: 'session-1',
  version: '1.0.0',
  gitBranch: 'main',
  type: 'system',
  content: 'Build completed successfully with 0 errors and 2 warnings',
  isMeta: false,
  level: 'info',
  uuid: 'meta-message-2',
  timestamp: '2025-01-15T10:34:00Z',
};

export const HiddenMetaMessage: Story = {
  args: {
    message: metaMessage,
  },
};

export const VisibleMetaMessage: Story = {
  args: {
    message: visibleMetaMessage,
  },
};
```

## File: `claude-history-tool/src/components/MessageCard.tsx`
```tsx
import React, { useState } from 'react';
import { FaDeezer, FaMagnifyingGlassPlus } from 'react-icons/fa6';
import { ChatMessage } from '../types';
import { Button } from './Button';
import { MetaCard } from './MetaCard';
import { Badge, BadgeType } from './Badge';
import { Tooltip } from './Tooltip';

interface MessageCardProps {
  message: ChatMessage;
}

interface ParsedMessageContent {
  textContent: Array<any>;
  toolUseContent: Array<any>;
  badgeType: BadgeType;
  toolNames: string[];
}

function parseMessage(message: ChatMessage): ParsedMessageContent {
  let textContent: Array<any> = [];
  const toolUseContent: Array<any> = [];
  const toolNames: string[] = [];

  let badgeType: BadgeType =
  message.type === 'user' ? BadgeType.User : BadgeType.Assistant;

  const messageContent = message.message?.content;

  if (typeof messageContent === 'string') {
    textContent.push(
      <div key={`text-0`} className="content">
        {messageContent}
      </div>
    );
  } else if (Array.isArray(messageContent)) {

      let itemIndex = 0;
      for (const contentItem of messageContent) {
        itemIndex++;  

        if (typeof contentItem === 'string') {
          textContent.push(
            <div key={`text-${itemIndex}`} className="content">
              {contentItem}
            </div>
          );
          continue;
        }

        switch (contentItem.type) {
          case 'tool_use':
            if (contentItem.name) {
              toolNames.push(contentItem.name);
            }
            toolUseContent.push(
              <pre key={`tool-use-${itemIndex}`} >
                {JSON.stringify(contentItem, null, 2)}
              </pre>
            );

            badgeType = BadgeType.Tool;
            break;

          case 'tool_result':
            toolUseContent.push(
              <pre key={`tool-use-${itemIndex}`} >
                {JSON.stringify(contentItem, null, 2)}
              </pre>
            );
            badgeType = BadgeType.ToolResult;
            break;
  
          case 'text':
            textContent.push(
              <div key={`text-${itemIndex}`} className="content">
                {contentItem?.text}
              </div>
            );
            break;
        }
      }
  }

  if (message.internalMessageType) {
    if (message.internalMessageType === 'hook') {
      badgeType = BadgeType.Hook;
    } else {
      badgeType = BadgeType.Internal;
    }
  }

  if (message.isMeta) {
    badgeType = BadgeType.Internal;
  }

  return {
    textContent,
    toolUseContent,
    badgeType,
    toolNames
  };
}

export const MessageCard: React.FC<MessageCardProps> = ({ message }) => {
  const { textContent, toolUseContent, badgeType, toolNames } = parseMessage(message);
  const isBackgroundMessageByDefault = message.isMeta
    || toolUseContent.length > 0
    || badgeType === BadgeType.Hook
    || badgeType === BadgeType.Tool
    || badgeType === BadgeType.ToolResult
    || badgeType === BadgeType.Internal;

  const [contentExpanded, setContentExpanded] = useState(!isBackgroundMessageByDefault);
  const [fullJsonExpanded, setFullJsonExpanded] = useState(false);

  const formatTimestamp = (timestamp: string) => {
    const date = new Date(timestamp);
    return date.toLocaleString();
  };

  const renderTokenUsage = () => {
    if (!message.message?.usage) return null;
    
    return (
      <div style={{ textAlign: 'left' }}>
        <div>Token Usage:</div>
        <div>Input: {message.message.usage.input_tokens || 0}</div>
        <div>Output: {message.message.usage.output_tokens || 0}</div>
        {message.message.usage.cache_creation_input_tokens && (
          <div>Cache Creation: {message.message.usage.cache_creation_input_tokens}</div>
        )}
      </div>
    );
  };

  // Parse the message content into a list of text and tool use/result items

  // Determine if this should use background styling (less prominent)

  const isForegroundMessage = contentExpanded || fullJsonExpanded;

  const cardClassName = isForegroundMessage ? "MessageCard message-foreground" : "MessageCard message-background";

  return (
    <div className={cardClassName} onClick={(evt) => {
      setContentExpanded(!contentExpanded)
      evt.stopPropagation();
    }}>
      <div className="header">
        <div className="header-left">
          <Badge type={badgeType} className="badge" toolNames={toolNames} />
        </div>
        
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span className="timestamp">
            {formatTimestamp(message.timestamp)}
          </span>
          {message.message?.usage && (
            <Tooltip content={renderTokenUsage()}>
              <FaDeezer 
                style={{ 
                  cursor: 'pointer', 
                  color: 'var(--color-text-secondary)',
                  fontSize: '14px'
                }} 
              />
            </Tooltip>
          )}
          <Tooltip content="See Full JSON">
            <FaMagnifyingGlassPlus 
              onClick={(evt) => {
                setFullJsonExpanded(!fullJsonExpanded)
                evt.stopPropagation();
              }}
              style={{
                cursor: 'pointer',
                color: 'var(--color-text-secondary)',
                fontSize: '14px'
              }}
            />
          </Tooltip>
        </div>
      </div>

      {contentExpanded && (
        <>
          <div onClick={(evt) => evt.stopPropagation()}>
            {textContent}
            {toolUseContent}
          </div>
        </>
      )}

      {/* temp - show the full message for debugging */} 
      {fullJsonExpanded && (
        <>
          <h3>Full Event JSON:</h3>
        <pre className="full-message">
          {JSON.stringify(message, null, 2)}
        </pre>
        </>
      )}
    </div>
  );
};
```

## File: `claude-history-tool/src/components/MetaCard.stories.tsx`
```tsx
import type { Meta, StoryObj } from '@storybook/react';
import { MetaCard } from './MetaCard';

const meta: Meta<typeof MetaCard> = {
  title: 'Components/MetaCard',
  component: MetaCard,
  parameters: {
    layout: 'padded',
  },
};

export default meta;
type Story = StoryObj<typeof meta>;

export const InfoMessage: Story = {
  args: {
    content: 'PreToolUse:Edit [/Users/andy.fischer/ai-coding-tools/ts-rubberstamp/bin/ts-rubberstamp] completed successfully',
    timestamp: '2025-07-20T05:06:24.957Z',
    level: 'info',
    toolUseID: 'toolu_01WgPC79uyPbZCwQ2EV2WpHu',
    isHiddenByDefault: true,
  },
};

export const ErrorMessage: Story = {
  args: {
    content: 'Tool execution failed: File not found',
    timestamp: '2025-07-20T05:06:24.957Z',
    level: 'error',
    isHiddenByDefault: false,
  },
};

export const WarningMessage: Story = {
  args: {
    content: 'Warning: This action will overwrite the existing file',
    timestamp: '2025-07-20T05:06:24.957Z',
    level: 'warn',
    isHiddenByDefault: false,
  },
};

export const TodoWriteMessage: Story = {
  args: {
    content: 'PreToolUse:TodoWrite [Creating todo list for refactoring task] completed successfully',
    timestamp: '2025-07-20T05:06:24.957Z',
    level: 'info',
    toolUseID: 'toolu_01TodoWriteExample',
    isHiddenByDefault: true,
  },
};

export const DebugMessage: Story = {
  args: {
    content: 'Debug: Processing file chunk 3 of 10',
    timestamp: '2025-07-20T05:06:24.957Z',
    level: 'debug',
    isHiddenByDefault: true,
  },
};

export const VisibleByDefault: Story = {
  args: {
    content: 'System notification: Build completed successfully',
    timestamp: '2025-07-20T05:06:24.957Z',
    level: 'info',
    isHiddenByDefault: false,
  },
};
```

## File: `claude-history-tool/src/components/MetaCard.tsx`
```tsx
import React, { useState } from 'react';
import { Button } from './Button';

interface MetaCardProps {
  content: string;
  timestamp: string;
  level?: string;
  toolUseID?: string;
  isHiddenByDefault?: boolean;
}

export const MetaCard: React.FC<MetaCardProps> = ({ 
  content, 
  timestamp, 
  level = 'info',
  toolUseID,
  isHiddenByDefault = true
}) => {
  const [expanded, setExpanded] = useState(!isHiddenByDefault);

  const formatTimestamp = (timestamp: string) => {
    const date = new Date(timestamp);
    return date.toLocaleString();
  };

  const getLevelEmoji = (level: string) => {
    switch (level) {
      case 'error':
        return '❌';
      case 'warn':
        return '⚠️';
      case 'info':
        return 'ℹ️';
      case 'debug':
        return '🐛';
      default:
        return '📋';
    }
  };

  const getToolEmoji = (content: string) => {
    if (content.includes('TodoWrite')) {
      return '✅';
    }
    if (content.includes('Edit')) {
      return '✏️';
    }
    if (content.includes('Read')) {
      return '📖';
    }
    if (content.includes('Write')) {
      return '📝';
    }
    if (content.includes('Bash')) {
      return '⚡';
    }
    return '🔧';
  };

  const displayEmoji = content.includes('PreToolUse') || content.includes('PostToolUse') 
    ? getToolEmoji(content) 
    : getLevelEmoji(level);

  return (
    <div className="MessageCard">
      <div className="MessageCard__header">
        <div className="MessageCard__header-left">
          <span className="MessageCard__badge MessageCard__badge--user">
            {displayEmoji} System
          </span>
          {level && level !== 'info' && (
            <span className="text-tertiary text-sm">
              [{level.toUpperCase()}]
            </span>
          )}
        </div>
        
        <span className="MessageCard__timestamp">
          {formatTimestamp(timestamp)}
        </span>
      </div>

      {expanded && (
        <div className="MessageCard__content">
          {content}
        </div>
      )}

      {toolUseID && expanded && (
        <div className="MessageCard__usage">
          <div>Tool Use ID: {toolUseID}</div>
        </div>
      )}

      {isHiddenByDefault && (
        <div className="MessageCard__expand-button">
          <Button onClick={() => setExpanded(!expanded)} className="button-secondary button-xs">
            {expanded ? 'Hide' : 'Show'}
          </Button>
        </div>
      )}
    </div>
  );
};
```

## File: `claude-history-tool/src/components/Modal.stories.tsx`
```tsx
import type { Meta, StoryObj } from '@storybook/react';
import { Modal } from './Modal';
import { Button } from './Button';
import { useState } from 'react';

const meta: Meta<typeof Modal> = {
  title: 'Components/Modal',
  component: Modal,
  parameters: {
    layout: 'fullscreen',
  },
};

export default meta;
type Story = StoryObj<typeof meta>;

const ModalWithTrigger = ({ children, title }: { children: React.ReactNode; title: string }) => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div style={{ padding: '20px' }}>
      <Button onClick={() => setIsOpen(true)}>Open {title}</Button>
      <Modal isOpen={isOpen} onClose={() => setIsOpen(false)}>
        {children}
      </Modal>
    </div>
  );
};

export const SimpleModal: Story = {
  render: () => (
    <ModalWithTrigger title="Simple Modal">
      <div style={{ padding: '24px', minWidth: '400px' }}>
        <h2 style={{ margin: '0 0 16px 0' }}>Simple Modal</h2>
        <p style={{ margin: '0 0 16px 0' }}>
          This is a simple modal dialog. You can click outside or press Escape to close it.
        </p>
        <Button onClick={() => {}}>Action Button</Button>
      </div>
    </ModalWithTrigger>
  ),
};

export const ModalWithForm: Story = {
  render: () => (
    <ModalWithTrigger title="Form Modal">
      <div style={{ padding: '24px', minWidth: '500px' }}>
        <h2 style={{ margin: '0 0 16px 0' }}>Create New Item</h2>
        <form style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
          <div>
            <label style={{ display: 'block', marginBottom: '4px', fontWeight: '500' }}>
              Name
            </label>
            <input 
              type="text" 
              style={{ 
                width: '100%', 
                padding: '8px 12px', 
                border: '1px solid #e8eaed', 
                borderRadius: '6px' 
              }} 
              placeholder="Enter name"
            />
          </div>
          <div>
            <label style={{ display: 'block', marginBottom: '4px', fontWeight: '500' }}>
              Description
            </label>
            <textarea 
              style={{ 
                width: '100%', 
                padding: '8px 12px', 
                border: '1px solid #e8eaed', 
                borderRadius: '6px',
                minHeight: '80px',
                resize: 'vertical'
              }} 
              placeholder="Enter description"
            />
          </div>
          <div style={{ display: 'flex', gap: '8px', justifyContent: 'flex-end' }}>
            <Button className="button-secondary button-xs">Cancel</Button>
            <Button className="button-primary button-xs">Create</Button>
          </div>
        </form>
      </div>
    </ModalWithTrigger>
  ),
};

export const LargeContentModal: Story = {
  render: () => (
    <ModalWithTrigger title="Large Content Modal">
      <div style={{ padding: '24px', maxWidth: '600px' }}>
        <h2 style={{ margin: '0 0 16px 0' }}>Large Content Modal</h2>
        <div style={{ marginBottom: '16px' }}>
          <p>This modal contains a lot of content to demonstrate scrolling behavior.</p>
          {Array.from({ length: 20 }, (_, i) => (
            <p key={i}>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor 
              incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis 
              nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
            </p>
          ))}
        </div>
        <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
          <Button className="button-primary">Got it</Button>
        </div>
      </div>
    </ModalWithTrigger>
  ),
};

export const ConfirmationModal: Story = {
  render: () => (
    <ModalWithTrigger title="Confirmation Modal">
      <div style={{ padding: '24px', minWidth: '400px', textAlign: 'center' }}>
        <div style={{ marginBottom: '16px', fontSize: '48px' }}>⚠️</div>
        <h2 style={{ margin: '0 0 8px 0', color: '#dc2626' }}>Confirm Delete</h2>
        <p style={{ margin: '0 0 24px 0', color: '#6b7280' }}>
          Are you sure you want to delete this item? This action cannot be undone.
        </p>
        <div style={{ display: 'flex', gap: '12px', justifyContent: 'center' }}>
          <Button className="button-secondary">Cancel</Button>
          <Button className="button-primary" style={{ backgroundColor: '#dc2626' }}>
            Delete
          </Button>
        </div>
      </div>
    </ModalWithTrigger>
  ),
};
```

## File: `claude-history-tool/src/components/Modal.tsx`
```tsx
import React from 'react';

interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  children: React.ReactNode;
}

export const Modal: React.FC<ModalProps> = ({ isOpen, onClose, children }) => {
  if (!isOpen) return null;

  const handleBackdropClick = (e: React.MouseEvent<HTMLDivElement>) => {
    if (e.target === e.currentTarget) {
      onClose();
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Escape') {
      onClose();
    }
  };

  return (
    <div 
      className="modal-overlay" 
      onClick={handleBackdropClick}
      onKeyDown={handleKeyDown}
      tabIndex={-1}
    >
      <div className="modal-content">
        {children}
      </div>
    </div>
  );
};
```

## File: `claude-history-tool/src/components/ToolUseCard.stories.tsx`
```tsx
import type { Meta, StoryObj } from '@storybook/react';
import { ToolUseCard } from './ToolUseCard';

const meta: Meta<typeof ToolUseCard> = {
  title: 'Components/ToolUseCard',
  component: ToolUseCard,
  parameters: {
    layout: 'padded',
  },
};

export default meta;
type Story = StoryObj<typeof meta>;

export const TodoWriteTool: Story = {
  args: {
    toolName: 'TodoWrite',
    toolId: 'toolu_01TodoExample',
    input: {
      todos: [
        { id: '1', content: 'Create new component', status: 'pending', priority: 'high' },
        { id: '2', content: 'Add tests', status: 'in_progress', priority: 'medium' },
        { id: '3', content: 'Update documentation', status: 'completed', priority: 'low' }
      ]
    },
    result: 'Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress.',
    timestamp: '2025-07-20T05:06:24.957Z',
  },
};

export const EditTool: Story = {
  args: {
    toolName: 'Edit',
    toolId: 'toolu_01EditExample',
    input: {
      file_path: '/Users/andy/project/src/components/Button.tsx',
      old_string: 'className="old-button"',
      new_string: 'className="new-button"'
    },
    result: 'The file /Users/andy/project/src/components/Button.tsx has been updated successfully.',
    timestamp: '2025-07-20T05:06:24.957Z',
  },
};

export const ReadTool: Story = {
  args: {
    toolName: 'Read',
    toolId: 'toolu_01ReadExample',
    input: {
      file_path: '/Users/andy/project/package.json'
    },
    result: '{\n  "name": "my-project",\n  "version": "1.0.0",\n  "dependencies": {\n    "react": "^18.0.0"\n  }\n}',
    timestamp: '2025-07-20T05:06:24.957Z',
  },
};

export const BashTool: Story = {
  args: {
    toolName: 'Bash',
    toolId: 'toolu_01BashExample',
    input: {
      command: 'npm run build',
      description: 'Build the project for production'
    },
    result: '> my-project@1.0.0 build\n> react-scripts build\n\nCreating an optimized production build...\nCompiled successfully.\n\nFile sizes after gzip:\n  41.2 KB  build/static/js/main.8f4b2c1a.js\n  1.78 KB  build/static/css/main.f855e6bc.css',
    timestamp: '2025-07-20T05:06:24.957Z',
  },
};

export const WriteTool: Story = {
  args: {
    toolName: 'Write',
    toolId: 'toolu_01WriteExample',
    input: {
      file_path: '/Users/andy/project/src/components/NewComponent.tsx',
      content: 'import React from \'react\';\n\nexport const NewComponent: React.FC = () => {\n  return <div>Hello World</div>;\n};'
    },
    result: 'File created successfully at: /Users/andy/project/src/components/NewComponent.tsx',
    timestamp: '2025-07-20T05:06:24.957Z',
  },
};

export const ToolWithoutResult: Story = {
  args: {
    toolName: 'Grep',
    toolId: 'toolu_01GrepExample',
    input: {
      pattern: 'useState',
      path: 'src/',
      output_mode: 'files_with_matches'
    },
    timestamp: '2025-07-20T05:06:24.957Z',
  },
};

export const UnknownTool: Story = {
  args: {
    toolName: 'CustomTool',
    toolId: 'toolu_01CustomExample',
    input: {
      customParam: 'value',
      anotherParam: 123
    },
    result: 'Custom tool executed successfully',
    timestamp: '2025-07-20T05:06:24.957Z',
  },
};
```

## File: `claude-history-tool/src/components/ToolUseCard.tsx`
```tsx
import React, { useState } from 'react';
import { Button } from './Button';

interface ToolUseCardProps {
  toolName: string;
  toolId: string;
  input: any;
  result?: any;
  timestamp: string;
}

export const ToolUseCard: React.FC<ToolUseCardProps> = ({ 
  toolName, 
  toolId, 
  input, 
  result, 
  timestamp 
}) => {
  const [expanded, setExpanded] = useState(false);

  const getToolEmoji = (name: string) => {
    switch (name) {
      case 'TodoWrite':
        return '✅';
      case 'Edit':
      case 'MultiEdit':
        return '✏️';
      case 'Read':
        return '📖';
      case 'Write':
        return '📝';
      case 'Bash':
        return '⚡';
      case 'Glob':
        return '🔍';
      case 'Grep':
        return '🕵️';
      default:
        return '🛠️';
    }
  };

  const formatTimestamp = (timestamp: string) => {
    const date = new Date(timestamp);
    return date.toLocaleString();
  };

  return (
    <div className="MessageCard">
      <div className="MessageCard__header">
        <div className="MessageCard__header-left">
          <span className="MessageCard__badge MessageCard__badge--assistant">
            {getToolEmoji(toolName)} {toolName}
          </span>
        </div>
        
        <span className="MessageCard__timestamp">
          {formatTimestamp(timestamp)}
        </span>
      </div>

      <div className="MessageCard__tool">
        <div className="MessageCard__tool-use">
          <div className="MessageCard__tool-header">
            Tool Use: {toolName}
          </div>
          {expanded && (
            <div>
              <div className="MessageCard__tool-id">
                ID: {toolId}
              </div>
              <pre className="MessageCard__tool-input">
                {JSON.stringify(input, null, 2)}
              </pre>
            </div>
          )}
        </div>
        
        {result && (
          <div className="MessageCard__tool-result">
            <div className="MessageCard__tool-header">
              Tool Result
            </div>
            {expanded && (
              <div>
                <pre className="MessageCard__tool-output">
                  {typeof result === 'string' ? result : JSON.stringify(result, null, 2)}
                </pre>
              </div>
            )}
          </div>
        )}
      </div>

      <div className="MessageCard__expand-button">
        <Button onClick={() => setExpanded(!expanded)} className="button-secondary button-xs">
          {expanded ? 'Collapse' : 'Expand'}
        </Button>
      </div>
    </div>
  );
};
```

## File: `claude-history-tool/src/components/Tooltip.tsx`
```tsx
import React, { useState, useRef, useEffect } from 'react';

interface TooltipProps {
  content: React.ReactNode;
  children: React.ReactNode;
  delay?: number;
}

export const Tooltip: React.FC<TooltipProps> = ({ 
  content, 
  children, 
  delay = 300 
}) => {
  const [isVisible, setIsVisible] = useState(false);
  const [position, setPosition] = useState({ top: 0, left: 0 });
  const timeoutRef = useRef<NodeJS.Timeout | null>(null);
  const targetRef = useRef<HTMLDivElement>(null);
  const tooltipRef = useRef<HTMLDivElement>(null);

  const showTooltip = () => {
    if (timeoutRef.current) {
      clearTimeout(timeoutRef.current);
    }
    timeoutRef.current = setTimeout(() => {
      setIsVisible(true);
      updatePosition();
    }, delay);
  };

  const hideTooltip = () => {
    if (timeoutRef.current) {
      clearTimeout(timeoutRef.current);
    }
    setIsVisible(false);
  };

  const updatePosition = () => {
    if (targetRef.current && tooltipRef.current) {
      const targetRect = targetRef.current.getBoundingClientRect();
      const tooltipRect = tooltipRef.current.getBoundingClientRect();
      
      let top = targetRect.top - tooltipRect.height - 8;
      let left = targetRect.left + (targetRect.width / 2) - (tooltipRect.width / 2);
      
      // Adjust if tooltip goes off screen
      if (left < 8) left = 8;
      if (left + tooltipRect.width > window.innerWidth - 8) {
        left = window.innerWidth - tooltipRect.width - 8;
      }
      if (top < 8) {
        top = targetRect.bottom + 8;
      }
      
      setPosition({ top, left });
    }
  };

  useEffect(() => {
    if (isVisible) {
      updatePosition();
      const handleScroll = () => updatePosition();
      window.addEventListener('scroll', handleScroll);
      window.addEventListener('resize', handleScroll);
      return () => {
        window.removeEventListener('scroll', handleScroll);
        window.removeEventListener('resize', handleScroll);
      };
    }
  }, [isVisible]);

  useEffect(() => {
    return () => {
      if (timeoutRef.current) {
        clearTimeout(timeoutRef.current);
      }
    };
  }, []);

  return (
    <>
      <div
        ref={targetRef}
        onMouseEnter={showTooltip}
        onMouseLeave={hideTooltip}
        style={{ display: 'inline-block' }}
      >
        {children}
      </div>
      
      {isVisible && (
        <div
          ref={tooltipRef}
          style={{
            position: 'fixed',
            top: position.top,
            left: position.left,
            backgroundColor: '#000',
            color: '#fff',
            padding: '8px 12px',
            borderRadius: '4px',
            fontSize: '12px',
            zIndex: 1000,
            pointerEvents: 'none',
            whiteSpace: 'nowrap',
            boxShadow: '0 2px 8px rgba(0, 0, 0, 0.3)'
          }}
        >
          {content}
        </div>
      )}
    </>
  );
};
```

## File: `claude-history-tool/src/components/Typography.stories.tsx`
```tsx
import type { Meta, StoryObj } from '@storybook/react';
import { Typography } from './Typography';

const meta: Meta<typeof Typography> = {
  title: 'Design System/Typography',
  component: Typography,
  parameters: {
    layout: 'padded',
  },
  argTypes: {
    variant: {
      control: { type: 'select' },
      options: ['h1', 'h2', 'h3', 'h4', 'body', 'caption', 'small'],
    },
    color: {
      control: { type: 'color' },
    },
    weight: {
      control: { type: 'select' },
      options: ['normal', 'medium', 'semibold', 'bold'],
    },
    align: {
      control: { type: 'select' },
      options: ['left', 'center', 'right'],
    },
    children: {
      control: { type: 'text' },
    },
  },
};

export default meta;
type Story = StoryObj<typeof meta>;

export const Heading1: Story = {
  args: {
    variant: 'h1',
    children: 'Claude History Tool',
  },
};

export const Heading2: Story = {
  args: {
    variant: 'h2',
    children: 'Chat Sessions',
  },
};

export const Heading3: Story = {
  args: {
    variant: 'h3',
    children: 'Project: /Users/johndoe/my-project',
  },
};

export const Heading4: Story = {
  args: {
    variant: 'h4',
    children: 'Session Details',
  },
};

export const Body: Story = {
  args: {
    variant: 'body',
    children: 'This is the main body text used throughout the application. It should be readable and comfortable for extended reading.',
  },
};

export const Caption: Story = {
  args: {
    variant: 'caption',
    children: 'Last activity: 2 hours ago • 15 messages',
  },
};

export const Small: Story = {
  args: {
    variant: 'small',
    children: 'Session ID: abc123-def456-ghi789',
  },
};

export const AllVariants: Story = {
  render: () => (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
      <Typography variant="h1">Heading 1 - Main Title</Typography>
      <Typography variant="h2">Heading 2 - Section Title</Typography>
      <Typography variant="h3">Heading 3 - Subsection</Typography>
      <Typography variant="h4">Heading 4 - Component Title</Typography>
      <Typography variant="body">
        Body text - This is the standard paragraph text used throughout the application. 
        It provides good readability and is suitable for longer content blocks.
      </Typography>
      <Typography variant="caption">
        Caption text - Used for metadata, timestamps, and secondary information
      </Typography>
      <Typography variant="small">
        Small text - Used for fine print, IDs, and tertiary information
      </Typography>
    </div>
  ),
};

export const ColorVariations: Story = {
  render: () => (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
      <Typography variant="h3" color="#333">Default Color</Typography>
      <Typography variant="body" color="#007acc">Primary Blue</Typography>
      <Typography variant="body" color="#666">Secondary Gray</Typography>
      <Typography variant="body" color="#888">Tertiary Gray</Typography>
      <Typography variant="body" color="#e74c3c">Error Red</Typography>
      <Typography variant="body" color="#27ae60">Success Green</Typography>
    </div>
  ),
};

export const WeightVariations: Story = {
  render: () => (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
      <Typography variant="body" weight="normal">Normal Weight</Typography>
      <Typography variant="body" weight="medium">Medium Weight</Typography>
      <Typography variant="body" weight="semibold">Semibold Weight</Typography>
      <Typography variant="body" weight="bold">Bold Weight</Typography>
    </div>
  ),
};

export const AlignmentVariations: Story = {
  render: () => (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
      <Typography variant="body" align="left">Left aligned text</Typography>
      <Typography variant="body" align="center">Center aligned text</Typography>
      <Typography variant="body" align="right">Right aligned text</Typography>
    </div>
  ),
};

export const ApplicationExamples: Story = {
  render: () => (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
      <div>
        <Typography variant="h1">Claude History Tool</Typography>
        <Typography variant="caption" color="#666">
          Browse and search your Claude conversation history
        </Typography>
      </div>
      
      <div>
        <Typography variant="h3" color="#333">
          /Users/johndoe/ai-coding-tools/my-project
        </Typography>
        <Typography variant="caption" color="#888">
          3 sessions • Last activity: 2 hours ago
        </Typography>
      </div>
      
      <div style={{ padding: '1rem', backgroundColor: '#f8f9fa', borderRadius: '8px' }}>
        <Typography variant="body">
          Help me create a React component for displaying user profiles. 
          It should include a photo, name, email, and bio section.
        </Typography>
        <Typography variant="small" color="#666" style={{ marginTop: '0.5rem' }}>
          Yesterday at 3:42 PM • 25 messages
        </Typography>
      </div>
    </div>
  ),
};
```

## File: `claude-history-tool/src/components/Typography.tsx`
```tsx
import React from 'react';

interface TypographyProps {
  variant?: 'h1' | 'h2' | 'h3' | 'h4' | 'body' | 'caption' | 'small';
  children: React.ReactNode;
  color?: string;
  weight?: 'normal' | 'medium' | 'semibold' | 'bold';
  align?: 'left' | 'center' | 'right';
  className?: string;
  style?: React.CSSProperties;
}

export const Typography: React.FC<TypographyProps> = ({
  variant = 'body',
  children,
  color,
  weight,
  align,
  className,
  style,
}) => {
  const getClassName = () => {
    const classes: string[] = [];
    
    // Base variant class
    switch (variant) {
      case 'h1':
        classes.push('heading-1');
        break;
      case 'h2':
        classes.push('heading-2');
        break;
      case 'h3':
        classes.push('heading-3');
        break;
      case 'h4':
        classes.push('heading-4');
        break;
      case 'caption':
        classes.push('text-sm');
        break;
      case 'small':
        classes.push('text-sm');
        break;
      default:
        break;
    }
    
    // Add color class if specified
    if (color === 'secondary') classes.push('text-secondary');
    if (color === 'tertiary') classes.push('text-tertiary');
    
    // Add custom className
    if (className) classes.push(className);
    
    return classes.join(' ');
  };

  const getInlineStyles = (): React.CSSProperties => {
    const styles: React.CSSProperties = {};
    
    if (color && !['secondary', 'tertiary'].includes(color)) {
      styles.color = color;
    }
    
    if (weight) {
      styles.fontWeight = weight === 'normal' ? 'var(--font-weight-normal)' : 
                          weight === 'medium' ? 'var(--font-weight-medium)' :
                          weight === 'semibold' ? 'var(--font-weight-semibold)' : 
                          'var(--font-weight-bold)';
    }
    
    if (align && align !== 'left') {
      styles.textAlign = align;
    }
    
    return { ...styles, ...style };
  };

  const Tag = variant.startsWith('h') ? variant as keyof JSX.IntrinsicElements : 'p';

  return (
    <Tag className={getClassName()} style={getInlineStyles()}>
      {children}
    </Tag>
  );
};
```

## File: `claude-history-tool/src/components/UpgradeBanner.stories.tsx`
```tsx
import type { Meta, StoryObj } from '@storybook/react';
import { UpgradeBanner } from './UpgradeBanner';

const meta: Meta<typeof UpgradeBanner> = {
  title: 'Components/UpgradeBanner',
  component: UpgradeBanner,
  parameters: {
    layout: 'fullscreen',
  },
  argTypes: {
    onClose: { action: 'closed' },
  },
};

export default meta;
type Story = StoryObj<typeof meta>;

export const SimpleText: Story = {
  args: {
    html: '<p>A new version of the app is available. <a href="#">Download now</a></p>',
  },
};

export const WithHeading: Story = {
  args: {
    html: '<h3>Update Available</h3><p>Version 2.0 is now available with exciting new features!</p>',
  },
};

export const RichContent: Story = {
  args: {
    html: `
      <h3>🎉 Major Update Available!</h3>
      <p>Version 2.0 includes:</p>
      <ul>
        <li>New AI-powered features</li>
        <li>Improved performance</li>
        <li>Enhanced security</li>
      </ul>
      <p><a href="#" style="font-weight: bold;">Update now</a> to get the latest features.</p>
    `,
  },
};

export const CriticalUpdate: Story = {
  args: {
    html: `
      <h3 style="color: #dc2626;">⚠️ Critical Security Update</h3>
      <p>Please update immediately to protect your data. This update fixes important security vulnerabilities.</p>
      <p><a href="#" style="background: #dc2626; color: white; padding: 8px 16px; border-radius: 4px; text-decoration: none;">Update Now</a></p>
    `,
  },
};

export const MinimalNotice: Story = {
  args: {
    html: '<a href="#">New version available - click to update</a>',
  },
};
```

## File: `claude-history-tool/src/components/UpgradeBanner.tsx`
```tsx
import React from 'react';
import { CloseButton } from './CloseButton';
import { HtmlContent } from './HtmlContent';
import { useDismissNotification } from '../hooks/useDismissNotification';

interface UpgradeBannerProps {
  html: string;
  contentCode: string;
  onClose: () => void;
}

export const UpgradeBanner: React.FC<UpgradeBannerProps> = ({ html, contentCode, onClose }) => {
  const handleClose = useDismissNotification(contentCode, onClose);

  return (
    <div className="upgrade-banner">
      <HtmlContent 
        html={html}
        className="upgrade-banner__content"
      />
      <CloseButton 
        onClose={handleClose}
        className="upgrade-banner__close"
        ariaLabel="Close banner"
      />
    </div>
  );
};
```

## File: `claude-history-tool/src/components/UpgradeModal.stories.tsx`
```tsx
import type { Meta, StoryObj } from '@storybook/react';
import { UpgradeModal } from './UpgradeModal';
import { Button } from './Button';
import { useState } from 'react';

const meta: Meta<typeof UpgradeModal> = {
  title: 'Components/UpgradeModal',
  component: UpgradeModal,
  parameters: {
    layout: 'fullscreen',
  },
};

export default meta;
type Story = StoryObj<typeof meta>;

const ModalWithTrigger = ({ html, title }: { html: string; title: string }) => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div style={{ padding: '20px' }}>
      <Button onClick={() => setIsOpen(true)}>Open {title}</Button>
      <UpgradeModal 
        isOpen={isOpen} 
        html={html}
        onClose={() => setIsOpen(false)}
      />
    </div>
  );
};

export const SimpleUpdate: Story = {
  render: () => (
    <ModalWithTrigger 
      title="Simple Update"
      html="<h2>Update Available</h2><p>A new version of the app is ready to install. Click the button below to update now.</p>"
    />
  ),
};

export const FeatureAnnouncement: Story = {
  render: () => (
    <ModalWithTrigger 
      title="Feature Announcement"
      html={`
        <h2>🎉 New Features Available!</h2>
        <p>We've added some exciting new capabilities to improve your experience:</p>
        <ul>
          <li><strong>Smart Search:</strong> Find content faster with AI-powered search</li>
          <li><strong>Dark Mode:</strong> Easier on your eyes during late-night sessions</li>
          <li><strong>Export Tools:</strong> Save your work in multiple formats</li>
        </ul>
        <p>Update now to start using these features!</p>
        <div style="text-align: center; margin-top: 24px;">
          <button style="background: #2D5CDB; color: white; border: none; padding: 12px 24px; border-radius: 6px; cursor: pointer;">Update Now</button>
        </div>
      `}
    />
  ),
};

export const CriticalSecurityUpdate: Story = {
  render: () => (
    <ModalWithTrigger 
      title="Security Update"
      html={`
        <h2 style="color: #dc2626;">🛡️ Critical Security Update</h2>
        <p style="color: #374151; margin-bottom: 16px;">We've identified and fixed important security vulnerabilities in the previous version.</p>
        <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 6px; padding: 16px; margin: 16px 0;">
          <h4 style="color: #dc2626; margin: 0 0 8px 0;">What's Fixed:</h4>
          <ul style="margin: 0; color: #374151;">
            <li>Data encryption improvements</li>
            <li>Authentication security enhancements</li>
            <li>Network communication protection</li>
          </ul>
        </div>
        <p><strong>We strongly recommend updating immediately to protect your data.</strong></p>
        <div style="text-align: center; margin-top: 24px;">
          <button style="background: #dc2626; color: white; border: none; padding: 12px 24px; border-radius: 6px; cursor: pointer; margin-right: 12px;">Update Now</button>
          <button style="background: transparent; color: #6b7280; border: 1px solid #d1d5db; padding: 12px 24px; border-radius: 6px; cursor: pointer;">Remind Me Later</button>
        </div>
      `}
    />
  ),
};

export const MaintenanceNotice: Story = {
  render: () => (
    <ModalWithTrigger 
      title="Maintenance Notice"
      html={`
        <h2>🔧 Scheduled Maintenance</h2>
        <p>We'll be performing system maintenance on <strong>Sunday, March 15th from 2:00 AM - 4:00 AM EST</strong>.</p>
        <div style="background: #fffbeb; border: 1px solid #fed7aa; border-radius: 6px; padding: 16px; margin: 16px 0;">
          <h4 style="color: #d97706; margin: 0 0 8px 0;">What to Expect:</h4>
          <ul style="margin: 0; color: #374151;">
            <li>Brief service interruptions (5-10 minutes)</li>
            <li>Improved performance after maintenance</li>
            <li>New backup system deployment</li>
          </ul>
        </div>
        <p>We apologize for any inconvenience and appreciate your patience.</p>
        <div style="text-align: center; margin-top: 24px;">
          <button style="background: #2D5CDB; color: white; border: none; padding: 12px 24px; border-radius: 6px; cursor: pointer;">Got It</button>
        </div>
      `}
    />
  ),
};

export const WelcomeMessage: Story = {
  render: () => (
    <ModalWithTrigger 
      title="Welcome Message"
      html={`
        <h2>👋 Welcome to Claude History Tool v2.0!</h2>
        <p>Thank you for updating to the latest version. Here's what's new:</p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 20px 0;">
          <div style="text-align: center;">
            <div style="font-size: 32px; margin-bottom: 8px;">🔍</div>
            <h4 style="margin: 0 0 4px 0;">Better Search</h4>
            <p style="margin: 0; font-size: 14px; color: #6b7280;">Find conversations faster</p>
          </div>
          <div style="text-align: center;">
            <div style="font-size: 32px; margin-bottom: 8px;">📊</div>
            <h4 style="margin: 0 0 4px 0;">Analytics</h4>
            <p style="margin: 0; font-size: 14px; color: #6b7280;">Track your usage patterns</p>
          </div>
        </div>
        <div style="text-align: center; margin-top: 24px;">
          <button style="background: #2D5CDB; color: white; border: none; padding: 12px 24px; border-radius: 6px; cursor: pointer;">Get Started</button>
        </div>
      `}
    />
  ),
};
```

## File: `claude-history-tool/src/components/UpgradeModal.tsx`
```tsx
import React from 'react';
import { Modal } from './Modal';
import { CloseButton } from './CloseButton';
import { HtmlContent } from './HtmlContent';
import { useDismissNotification } from '../hooks/useDismissNotification';

interface UpgradeModalProps {
  isOpen: boolean;
  html: string;
  contentCode: string;
  onClose: () => void;
}

export const UpgradeModal: React.FC<UpgradeModalProps> = ({ isOpen, html, contentCode, onClose }) => {
  const handleClose = useDismissNotification(contentCode, onClose);

  return (
    <Modal isOpen={isOpen} onClose={handleClose}>
      <div className="upgrade-modal">
        <CloseButton 
          onClose={handleClose}
          className="upgrade-modal__close"
          ariaLabel="Close modal"
        />
        <HtmlContent 
          html={html}
          className="upgrade-modal__content"
        />
      </div>
    </Modal>
  );
};
```

## File: `claude-history-tool/src/components/index.ts`
```typescript
export { ChatList } from './ChatList';
export { ChatViewer } from './ChatViewer';
export { MessageCard } from './MessageCard';
export { Modal } from './Modal';
export { UpgradeBanner } from './UpgradeBanner';
export { UpgradeModal } from './UpgradeModal';
export { CloseButton } from './CloseButton';
export { HtmlContent } from './HtmlContent';
```

## File: `claude-history-tool/src/components/__tests__/ChatList.test.tsx`
```tsx
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { ChatList } from '../ChatList';
import { ProjectDirectory } from '../../types';

const mockProjects: ProjectDirectory[] = [
  {
    path: '-Users-johndoe-ai-coding-tools-claude-history-tool',
    sessions: [
      {
        sessionId: 'session-1',
        messages: [
          {
            parentUuid: null,
            isSidechain: false,
            userType: 'external',
            cwd: '/test',
            sessionId: 'session-1',
            version: '1.0.0',
            type: 'user',
            message: {
              role: 'user',
              content: 'Test message content for session 1',
            },
            uuid: 'msg-1',
            timestamp: '2025-01-15T10:30:00Z',
          }
        ],
        firstMessageTimestamp: '2025-01-15T10:30:00Z',
        lastMessageTimestamp: '2025-01-15T11:45:00Z',
        projectPath: '-Users-johndoe-ai-coding-tools-claude-history-tool',
        messageCount: 25
      }
    ]
  }
];

describe('ChatList', () => {
  it('renders chat history title', () => {
    const mockOnSessionSelect = vi.fn();
    render(<ChatList projects={mockProjects} onSessionSelect={mockOnSessionSelect} />);
    
    expect(screen.getByText('Chat History')).toBeInTheDocument();
  });

  it('displays project name correctly', () => {
    const mockOnSessionSelect = vi.fn();
    render(<ChatList projects={mockProjects} onSessionSelect={mockOnSessionSelect} />);
    
    expect(screen.getByText('ai/coding/tools/claude/history/tool')).toBeInTheDocument();
  });

  it('displays session information', () => {
    const mockOnSessionSelect = vi.fn();
    render(<ChatList projects={mockProjects} onSessionSelect={mockOnSessionSelect} />);
    
    expect(screen.getByText('25 messages')).toBeInTheDocument();
    expect(screen.getByText(/Test message content for session 1/)).toBeInTheDocument();
  });

  it('calls onSessionSelect when session is clicked', () => {
    const mockOnSessionSelect = vi.fn();
    render(<ChatList projects={mockProjects} onSessionSelect={mockOnSessionSelect} />);
    
    const sessionElement = screen.getByText(/Test message content for session 1/).closest('div');
    fireEvent.click(sessionElement!);
    
    expect(mockOnSessionSelect).toHaveBeenCalledWith(mockProjects[0].sessions[0]);
  });

  it('displays empty state when no projects', () => {
    const mockOnSessionSelect = vi.fn();
    render(<ChatList projects={[]} onSessionSelect={mockOnSessionSelect} />);
    
    expect(screen.getByText('No chat history found in ~/.claude/projects')).toBeInTheDocument();
  });
});
```

## File: `claude-history-tool/src/components/__tests__/MessageCard.test.tsx`
```tsx
import { describe, it, expect } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { MessageCard } from '../MessageCard';
import { ChatMessage } from '../../types';

const userMessage: ChatMessage = {
  parentUuid: null,
  isSidechain: false,
  userType: 'external',
  cwd: '/test',
  sessionId: 'session-1',
  version: '1.0.0',
  type: 'user',
  message: {
    role: 'user',
    content: 'This is a test user message',
  },
  uuid: 'user-msg-1',
  timestamp: '2025-01-15T10:30:00Z',
};

const assistantMessageWithTools: ChatMessage = {
  parentUuid: 'user-msg-1',
  isSidechain: false,
  userType: 'external',
  cwd: '/test',
  sessionId: 'session-1',
  version: '1.0.0',
  type: 'assistant',
  message: {
    role: 'assistant',
    content: [
      {
        type: 'text',
        text: 'I will help you with that.'
      },
      {
        type: 'tool_use',
        id: 'tool-1',
        name: 'Write',
        input: { file_path: '/test.txt', content: 'test content' }
      }
    ],
    id: 'msg-1',
    model: 'claude-3-sonnet',
  },
  uuid: 'assistant-msg-1',
  timestamp: '2025-01-15T10:31:00Z',
};

describe('MessageCard', () => {
  it('renders user message correctly', () => {
    render(<MessageCard message={userMessage} />);
    
    expect(screen.getByText('👤 User')).toBeInTheDocument();
    expect(screen.getByText('This is a test user message')).toBeInTheDocument();
  });

  it('renders assistant message correctly', () => {
    render(<MessageCard message={assistantMessageWithTools} />);
    
    expect(screen.getByText('🤖 Assistant')).toBeInTheDocument();
    expect(screen.getByText('I will help you with that.')).toBeInTheDocument();
  });

  it('shows tool toggle button for messages with tools', () => {
    render(<MessageCard message={assistantMessageWithTools} />);
    
    expect(screen.getByText('Show Tools')).toBeInTheDocument();
  });

  it('does not show tool toggle for messages without tools', () => {
    render(<MessageCard message={userMessage} />);
    
    expect(screen.queryByText('Show Tools')).not.toBeInTheDocument();
  });

  it('expands and collapses tool content', () => {
    render(<MessageCard message={assistantMessageWithTools} />);
    
    const toggleButton = screen.getByText('Show Tools');
    
    // Tool content should not be visible initially
    expect(screen.queryByText('🛠️ Tool Use: Write')).not.toBeInTheDocument();
    
    // Click to expand
    fireEvent.click(toggleButton);
    
    // Tool content should now be visible
    expect(screen.getByText('🛠️ Tool Use: Write')).toBeInTheDocument();
    expect(screen.getByText('Hide Tools')).toBeInTheDocument();
    
    // Click to collapse
    fireEvent.click(screen.getByText('Hide Tools'));
    
    // Tool content should be hidden again
    expect(screen.queryByText('🛠️ Tool Use: Write')).not.toBeInTheDocument();
    expect(screen.getByText('Show Tools')).toBeInTheDocument();
  });

  it('displays timestamp correctly', () => {
    render(<MessageCard message={userMessage} />);
    
    // Check that some form of timestamp is displayed
    expect(screen.getByText(/1\/15\/2025/)).toBeInTheDocument();
  });
});
```

## File: `claude-history-tool/src/hooks/useDismissNotification.ts`
```typescript
import { useCallback } from 'react';

export const useDismissNotification = (contentCode: string, onClose: () => void) => {
  return useCallback(async () => {
    await window.electronAPI.dismissNotification(contentCode);
    onClose();
  }, [contentCode, onClose]);
};
```

## File: `claude-history-tool/src/hooks/useUpgradeNotice.ts`
```typescript
import { useQuery } from '@tanstack/react-query';
import { UpgradeNoticeResponse } from '../types/upgrade';

export const useUpgradeNotice = () => {
  return useQuery<UpgradeNoticeResponse>({
    queryKey: ['upgradeNotice'],
    queryFn: async (): Promise<UpgradeNoticeResponse> => {
      try {
        const apiHostname = await window.electronAPI.getApiHostname();
        const response = await fetch(`${apiHostname}/desktop_tool/upgrade-notice?appVersion=0.1.0`);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();

        const filteredData: UpgradeNoticeResponse = {};

        if (data.bannerHtml && data.bannerContentCode) {
          const bannerDismissed = await window.electronAPI.isNotificationDismissed(data.bannerContentCode);
          if (!bannerDismissed) {
            filteredData.bannerHtml = data.bannerHtml;
            filteredData.bannerContentCode = data.bannerContentCode;
          }
        }

        if (data.popupHtml && data.popupContentCode) {
          const popupDismissed = await window.electronAPI.isNotificationDismissed(data.popupContentCode);
          if (!popupDismissed) {
            filteredData.popupHtml = data.popupHtml;
            filteredData.popupContentCode = data.popupContentCode;
          }
        }

        return filteredData;
      } catch (error) {
        console.warn('Failed to fetch upgrade notice:', error);
        return {};
      }
    },
    retry: false,
    refetchOnWindowFocus: false,
    staleTime: 60 * 60 * 1000,
  });
};
```

## File: `claude-history-tool/src/main/annotateInternalMessages.ts`
```typescript
import { ChatMessage } from "../types";

// Annotate messages that are terminal control messages or hooks
export function annotateInternalMessages(messages: ChatMessage[]) {

    for (const message of messages) {
      const content = message.message?.content;
      
      if (typeof content === 'string') {
        // Check for PreToolUse hook pattern (e.g., "PreToolUse:Edit")
        if (content.includes('PreToolUse:') && message.type === 'system') {
          message.internalMessageType = 'hook';
        }
        // Check for /clear command pattern
        else if (content.includes('<command-name>/clear</command-name>')) {
          message.internalMessageType = 'terminal_control';
        }
        // Check for command stdout pattern
        else if (content.includes('<local-command-stdout>')) {
          message.internalMessageType = 'terminal_control';
        }
      }
    }
  }
```

## File: `claude-history-tool/src/main/database.ts`
```typescript
import { app } from 'electron'
import path from 'path'
import { DatabaseLoader } from '@andyfischer/sqlite-wrapper'
import { Stream } from '@andyfischer/streams'

const databaseSchema = {
    name: 'claude-history-tool',
    statements: [
        `create table dismissed_upgrade_notifications (
            id integer primary key autoincrement,
            content_code text not null unique,
            dismissed_at datetime default current_timestamp
        )`
    ]
}

let databaseLoader: DatabaseLoader | null = null

export function initializeDatabase() {
    if (databaseLoader) {
        return databaseLoader.load()
    }

    const userDataPath = app.getPath('userData')
    const dbPath = path.join(userDataPath, 'claude-history-tool.db')

    databaseLoader = new DatabaseLoader({
        filename: dbPath,
        schema: databaseSchema,
        logs: (new Stream()).logToConsole(),
    })

    return databaseLoader.load()
}

export function getDatabase() {
    if (!databaseLoader) {
        return initializeDatabase()
    }
    return databaseLoader.load()
}

export function isDismissed(contentCode: string): boolean {
    const db = getDatabase()
    const result = db.get(
        'select 1 from dismissed_upgrade_notifications where content_code = ?',
        [contentCode]
    )
    return !!result
}

export function dismissNotification(contentCode: string): void {
    const db = getDatabase()
    db.run(
        'insert or ignore into dismissed_upgrade_notifications (content_code) values (?)',
        [contentCode]
    )
}
```

## File: `claude-history-tool/src/main/getAnalytics.ts`
```typescript
import * as path from 'path';
import * as fs from 'fs';
import * as os from 'os';
import { ChatMessage, ChatSession, ProjectDirectory } from '../types';
import { annotateInternalMessages } from './annotateInternalMessages';

export interface AnalyticsData {
  toolUsage: { name: string; count: number }[];
  tokenUsage: { name: string; tokens: number }[];
  chatStats: {
    totalChats: number;
    totalMessages: number;
    averageMessagesPerChat: number;
  };
  timeStats: {
    totalTimeSpan: string;
    firstChatDate: string;
    lastChatDate: string;
  };
}

export async function getAnalytics(): Promise<AnalyticsData> {
  console.log('[getAnalytics] Starting analytics calculation');
  
  const claudeDir = path.join(os.homedir(), '.claude', 'projects');
  
  if (!fs.existsSync(claudeDir)) {
    console.log('[getAnalytics] Claude directory does not exist');
    return getEmptyAnalytics();
  }

  const projectDirs = fs.readdirSync(claudeDir, { withFileTypes: true })
    .filter(dirent => dirent.isDirectory())
    .map(dirent => dirent.name);

  console.log(`[getAnalytics] Found ${projectDirs.length} project directories`);

  const toolUsageMap = new Map<string, number>();
  const tokenUsageMap = new Map<string, number>();
  let totalChats = 0;
  let totalMessages = 0;
  const allTimestamps: string[] = [];

  for (const projectDir of projectDirs) {
    const projectPath = path.join(claudeDir, projectDir);
    const files = fs.readdirSync(projectPath)
      .filter(file => file.endsWith('.jsonl'));

    for (const file of files) {
      const filePath = path.join(projectPath, file);
      
      try {
        const content = fs.readFileSync(filePath, 'utf-8');
        const lines = content.trim().split('\n').filter(line => line.trim());
        
        if (lines.length === 0) continue;
        
        const messages: ChatMessage[] = lines.map(line => JSON.parse(line));
        
        annotateInternalMessages(messages);
        
        if (messages.length > 0) {
          totalChats++;
          totalMessages += messages.length;
          
          // Collect timestamps
          messages.forEach(msg => {
            if (msg.timestamp) {
              allTimestamps.push(msg.timestamp);
            }
          });
          
          // Analyze tool usage and token usage
          messages.forEach(msg => {
            if (msg.message?.content && Array.isArray(msg.message.content)) {
              msg.message.content.forEach(item => {
                if (item.type === 'tool_use' && item.name) {
                  const toolName = item.name;
                  toolUsageMap.set(toolName, (toolUsageMap.get(toolName) || 0) + 1);
                }
              });
            }
            
            // Track token usage
            if (msg.message?.usage) {
              const usage = msg.message.usage;
              const inputTokens = usage.input_tokens || 0;
              const outputTokens = usage.output_tokens || 0;
              const totalTokensForMessage = inputTokens + outputTokens;
              
              if (totalTokensForMessage > 0) {
                // For now, we'll attribute all tokens to "Claude Assistant"
                // In the future, we could track which tools consumed tokens
                const toolName = "Claude Assistant";
                tokenUsageMap.set(toolName, (tokenUsageMap.get(toolName) || 0) + totalTokensForMessage);
              }
            }
          });
        }
      } catch (error) {
        console.error(`[getAnalytics] Error processing file ${filePath}:`, error);
        continue;
      }
    }
  }

  // Sort tool usage by frequency
  const toolUsage = Array.from(toolUsageMap.entries())
    .map(([name, count]) => ({ name, count }))
    .sort((a, b) => b.count - a.count)
    .slice(0, 10); // Top 10

  // Sort token usage by total tokens
  const tokenUsage = Array.from(tokenUsageMap.entries())
    .map(([name, tokens]) => ({ name, tokens }))
    .sort((a, b) => b.tokens - a.tokens)
    .slice(0, 10); // Top 10

  // Calculate time stats
  const sortedTimestamps = allTimestamps.sort();
  const firstChatDate = sortedTimestamps[0] || '';
  const lastChatDate = sortedTimestamps[sortedTimestamps.length - 1] || '';
  
  let totalTimeSpan = 'N/A';
  if (firstChatDate && lastChatDate && firstChatDate !== lastChatDate) {
    const firstDate = new Date(firstChatDate);
    const lastDate = new Date(lastChatDate);
    const diffInDays = Math.ceil((lastDate.getTime() - firstDate.getTime()) / (1000 * 60 * 60 * 24));
    totalTimeSpan = `${diffInDays} days`;
  }

  const analytics: AnalyticsData = {
    toolUsage,
    tokenUsage,
    chatStats: {
      totalChats,
      totalMessages,
      averageMessagesPerChat: totalChats > 0 ? Math.round((totalMessages / totalChats) * 10) / 10 : 0
    },
    timeStats: {
      totalTimeSpan,
      firstChatDate: firstChatDate ? new Date(firstChatDate).toLocaleDateString() : 'N/A',
      lastChatDate: lastChatDate ? new Date(lastChatDate).toLocaleDateString() : 'N/A'
    }
  };

  console.log('[getAnalytics] Analytics calculated:', {
    totalChats: analytics.chatStats.totalChats,
    totalMessages: analytics.chatStats.totalMessages,
    toolsFound: analytics.toolUsage.length,
    timeSpan: analytics.timeStats.totalTimeSpan
  });

  return analytics;
}

function getEmptyAnalytics(): AnalyticsData {
  return {
    toolUsage: [],
    tokenUsage: [],
    chatStats: {
      totalChats: 0,
      totalMessages: 0,
      averageMessagesPerChat: 0
    },
    timeStats: {
      totalTimeSpan: 'N/A',
      firstChatDate: 'N/A',
      lastChatDate: 'N/A'
    }
  };
}
```

## File: `claude-history-tool/src/main/getChatSessions.ts`
```typescript
import * as path from 'path';
import * as fs from 'fs';
import * as os from 'os';
import { ChatMessage, ChatSession, ProjectDirectory } from '../types';
import { annotateInternalMessages } from './annotateInternalMessages';

export async function getChatSessions(): Promise<ProjectDirectory[]> {
  const claudeDir = path.join(os.homedir(), '.claude', 'projects');
  
  console.log(`[getChatSessions] Starting scan of Claude directory: ${claudeDir}`);
  
  if (!fs.existsSync(claudeDir)) {
    console.log('[getChatSessions] Claude directory does not exist');
    return [];
  }

  const projectDirs = fs.readdirSync(claudeDir, { withFileTypes: true })
    .filter(dirent => dirent.isDirectory())
    .map(dirent => dirent.name);

  console.log(`[getChatSessions] Found ${projectDirs.length} project directories:`, projectDirs);

  const projects: ProjectDirectory[] = [];
  const seenSessionIds = new Set<string>();
  const sessionSources = new Map<string, string>(); // Track where each session was first seen

  for (const projectDir of projectDirs) {
    const projectPath = path.join(claudeDir, projectDir);
    const files = fs.readdirSync(projectPath)
      .filter(file => file.endsWith('.jsonl'));

    console.log(`[getChatSessions] Project ${projectDir}: Found ${files.length} .jsonl files`);

    const sessions: ChatSession[] = [];

    for (const file of files) {
      const filePath = path.join(projectPath, file);
      
      try {
        const content = fs.readFileSync(filePath, 'utf-8');
        const lines = content.trim().split('\n').filter(line => line.trim());
        
        console.log(`[getChatSessions] File ${file}: ${lines.length} lines`);
        
        if (lines.length === 0) {
          console.log(`[getChatSessions] Skipping empty file: ${file}`);
          continue;
        }
        
        const messages: ChatMessage[] = lines.map((line, index) => {
          try {
            return JSON.parse(line);
          } catch (error) {
            console.error(`[getChatSessions] Failed to parse JSON at line ${index + 1} in ${file}:`, error);
            throw error;
          }
        });

        annotateInternalMessages(messages);
        
        if (messages.length > 0) {
          const sessionId = messages[0].sessionId;
          const sourceKey = `${projectDir}/${file}`;
          
          console.log(`[getChatSessions] Processing session ${sessionId} from ${sourceKey}`);
          
          // Validate sessionId exists and is a string
          if (!sessionId || typeof sessionId !== 'string') {
            console.warn(`[getChatSessions] Invalid or missing sessionId in ${sourceKey}, first message:`, messages[0]);
            continue;
          }
          
          // Check for duplicate session GUID with detailed logging
          if (seenSessionIds.has(sessionId)) {
            const originalSource = sessionSources.get(sessionId);
            console.error(`[getChatSessions] DUPLICATE SESSION DETECTED!`);
            console.error(`  Session ID: ${sessionId}`);
            console.error(`  Original source: ${originalSource}`);
            console.error(`  Duplicate source: ${sourceKey}`);
            console.error(`  Skipping duplicate session`);
            continue;
          }
          
          // Verify all messages in the file have the same sessionId
          const differentSessionIds = messages.filter(msg => msg.sessionId !== sessionId);
          if (differentSessionIds.length > 0) {
            console.warn(`[getChatSessions] Mixed session IDs in file ${sourceKey}:`);
            console.warn(`  Primary session: ${sessionId}`);
            console.warn(`  Other sessions found: ${[...new Set(differentSessionIds.map(msg => msg.sessionId))]}`);
          }
          
          seenSessionIds.add(sessionId);
          sessionSources.set(sessionId, sourceKey);
          
          const firstMessage = messages[0];
          const lastMessage = messages[messages.length - 1];
          
          sessions.push({
            sessionId,
            messages,
            firstMessageTimestamp: firstMessage.timestamp,
            lastMessageTimestamp: lastMessage.timestamp,
            projectPath: projectDir,
            messageCount: messages.length
          });
          
          console.log(`[getChatSessions] Successfully added session ${sessionId} (${messages.length} messages)`);
        }
      } catch (error) {
        console.error(`[getChatSessions] Error processing file ${filePath}:`, error);
        continue;
      }
    }

    if (sessions.length > 0) {
      console.log(`[getChatSessions] Project ${projectDir}: Successfully processed ${sessions.length} sessions`);
      
      // Sort sessions by last message timestamp
      sessions.sort((a, b) => 
        new Date(b.lastMessageTimestamp).getTime() - new Date(a.lastMessageTimestamp).getTime()
      );

      projects.push({
        path: projectDir,
        sessions
      });
    } else {
      console.log(`[getChatSessions] Project ${projectDir}: No valid sessions found`);
    }
  }

  // Final validation: Check for any duplicate sessions that made it through
  const finalSessionIds = new Set<string>();
  let finalDuplicateCount = 0;
  
  for (const project of projects) {
    for (const session of project.sessions) {
      if (finalSessionIds.has(session.sessionId)) {
        console.error(`[getChatSessions] CRITICAL: Duplicate session in final result: ${session.sessionId}`);
        finalDuplicateCount++;
      }
      finalSessionIds.add(session.sessionId);
    }
  }

  console.log(`[getChatSessions] Final summary:`);
  console.log(`  Total projects: ${projects.length}`);
  console.log(`  Total unique sessions: ${finalSessionIds.size}`);
  console.log(`  Final duplicates detected: ${finalDuplicateCount}`);

  // Sort projects by most recent session
  projects.sort((a, b) => {
    const aLatest = new Date(a.sessions[0]?.lastMessageTimestamp || 0).getTime();
    const bLatest = new Date(b.sessions[0]?.lastMessageTimestamp || 0).getTime();
    return bLatest - aLatest;
  });

  return projects;
}
```

## File: `claude-history-tool/src/main/getSessionDetails.ts`
```typescript
import * as path from 'path';
import * as fs from 'fs';
import * as os from 'os';
import { ChatMessage } from '../types';
import { annotateInternalMessages } from './annotateInternalMessages';

export async function getSessionDetails(sessionId: string, projectName: string): Promise<ChatMessage[]> {

  console.log(`[getSessionDetails] Getting session details for ${sessionId} in project ${projectName}`);

  const sessionFilePath = path.join(os.homedir(), '.claude', 'projects', projectName, `${sessionId}.jsonl`);
  
  try {
    const content = fs.readFileSync(sessionFilePath, 'utf-8');
    const lines = content.trim().split('\n');
    
    const messages: ChatMessage[] = lines.map(line => JSON.parse(line));
    
    annotateInternalMessages(messages);
    return messages;
  } catch (error) {
    console.error(`Failed to read session file: ${sessionFilePath}`, error);
    return [];
  }
}

```

## File: `claude-history-tool/src/main/main.ts`
```typescript
import { app, BrowserWindow, ipcMain } from 'electron';
import * as path from 'path';
import * as fs from 'fs';
import * as os from 'os';

// Load environment variables from .env file only in development
if (process.env.NODE_ENV === 'development') {
  try {
    const dotenv = require('dotenv');
    dotenv.config();
  } catch (error) {
    // dotenv not available in production, which is fine
  }
}
import { ChatMessage, ChatSession, ProjectDirectory } from '../types';
import { getChatSessions } from './getChatSessions';
import { getSessionDetails } from './getSessionDetails';
import { getAnalytics, AnalyticsData } from './getAnalytics';
import { initializeDatabase, isDismissed, dismissNotification } from './database';

let mainWindow: BrowserWindow;

function createWindow(): void {
  const windowWidth = parseInt(process.env.WINDOW_WIDTH || '1200');
  const windowHeight = parseInt(process.env.WINDOW_HEIGHT || '800');
  const rendererPort = process.env.RENDERER_PORT || '3447';
  const enableDevTools = process.env.ENABLE_DEV_TOOLS === 'true';

  mainWindow = new BrowserWindow({
    height: windowHeight,
    width: windowWidth,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.js'),
    },
  });

  if (process.env.NODE_ENV === 'development') {
    mainWindow.loadURL(`http://localhost:${rendererPort}`);
    if (enableDevTools) {
      mainWindow.webContents.openDevTools();
    }
  } else {
    mainWindow.loadFile(path.join(__dirname, '../renderer/index.html'));
  }
}

app.whenReady().then(() => {
  initializeDatabase();
  createWindow();
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});

// IPC handlers
ipcMain.handle('get-chat-sessions', async (): Promise<ProjectDirectory[]> => {
  return await getChatSessions();
});

ipcMain.handle('get-session-details', async (_, sessionId: string, projectName: string): Promise<ChatMessage[]> => {
  return await getSessionDetails(sessionId, projectName);
});

ipcMain.handle('get-analytics', async (): Promise<AnalyticsData> => {
  return await getAnalytics();
});

ipcMain.handle('is-notification-dismissed', async (_, contentCode: string): Promise<boolean> => {
  return isDismissed(contentCode);
});

ipcMain.handle('dismiss-notification', async (_, contentCode: string): Promise<void> => {
  dismissNotification(contentCode);
});

ipcMain.handle('get-api-hostname', async (): Promise<string> => {
  return process.env.API_HOSTNAME || 'https://api.mcp-eval.com';
});
```

## File: `claude-history-tool/src/main/preload.ts`
```typescript
import { contextBridge, ipcRenderer } from 'electron';
import { ProjectDirectory, ChatMessage } from '../types';
import { AnalyticsData } from './getAnalytics';

const electronAPI = {
  getChatSessions: (): Promise<ProjectDirectory[]> => 
    ipcRenderer.invoke('get-chat-sessions'),
  
  getSessionDetails: (sessionId: string, projectName: string): Promise<ChatMessage[]> => 
    ipcRenderer.invoke('get-session-details', sessionId, projectName),
  
  getAnalytics: (): Promise<AnalyticsData> => 
    ipcRenderer.invoke('get-analytics'),
  
  isNotificationDismissed: (contentCode: string): Promise<boolean> => 
    ipcRenderer.invoke('is-notification-dismissed', contentCode),
  
  dismissNotification: (contentCode: string): Promise<void> => 
    ipcRenderer.invoke('dismiss-notification', contentCode),
  
  getApiHostname: (): Promise<string> => 
    ipcRenderer.invoke('get-api-hostname'),
};

contextBridge.exposeInMainWorld('electronAPI', electronAPI);

declare global {
  interface Window {
    electronAPI: typeof electronAPI;
  }
}
```

## File: `claude-history-tool/src/main/__tests__/getSessionDetails.test.ts`
```typescript
import { describe, it, expect } from 'vitest';
import { ChatMessage } from '../../types';
import { annotateInternalMessages } from '../annotateInternalMessages';

const SampleChat_WithTerminalControl: ChatMessage[] = [
  {
    parentUuid: null,
    isSidechain: false,
    userType: "external",
    cwd: "cwd",
    sessionId: "d99c45c5-13fd-459e-8b01-8365b2bd3434",
    version: "1.0.56",
    gitBranch: "main",
    type: "user",
    message: {
      role: "user",
      content: "Caveat: The messages below were generated by the user while running local commands. DO NOT respond to these messages or otherwise consider them in your response unless the user explicitly asks you to."
    },
    isMeta: true,
    uuid: "6b96fd54-57ab-42d5-80e4-153889dc3d5a",
    timestamp: "2025-07-20T04:32:32.563Z"
  },
  {
    parentUuid: "6b96fd54-57ab-42d5-80e4-153889dc3d5a",
    isSidechain: false,
    userType: "external",
    cwd: "cwd",
    sessionId: "d99c45c5-13fd-459e-8b01-8365b2bd3434",
    version: "1.0.56",
    gitBranch: "main",
    type: "user",
    message: {
      role: "user",
      content: "<command-name>/clear</command-name>\n          <command-message>clear</command-message>\n          <command-args></command-args>"
    },
    uuid: "d03d0bb6-53c5-4762-91e2-5e1cf7d3307d",
    timestamp: "2025-07-20T05:00:51.573Z"
  },
  {
    parentUuid: "d03d0bb6-53c5-4762-91e2-5e1cf7d3307d",
    isSidechain: false,
    userType: "external",
    cwd: "cwd",
    sessionId: "d99c45c5-13fd-459e-8b01-8365b2bd3434",
    version: "1.0.56",
    gitBranch: "main",
    type: "user",
    message: {
      role: "user",
      content: "<local-command-stdout></local-command-stdout>"
    },
    uuid: "05df1946-1760-4a5d-8959-058177d15d97",
    timestamp: "2025-07-20T05:00:51.581Z"
  },
  {
    parentUuid: "05df1946-1760-4a5d-8959-058177d15d97",
    isSidechain: false,
    userType: "external",
    cwd: "cwd",
    sessionId: "d99c45c5-13fd-459e-8b01-8365b2bd3434",
    version: "1.0.56",
    gitBranch: "main",
    type: "user",
    message: {
      role: "user",
      content: "update the tsconfig.json so that String.startsWith is supported"
    },
    uuid: "regular-message-uuid",
    timestamp: "2025-07-20T05:01:00.000Z"
  }
];

const SampleChat: ChatMessage[] = [
  {
    parentUuid: null,
    isSidechain: false,
    userType: "external",
    cwd: "cwd",
    sessionId: "regular-session-id",
    version: "1.0.56",
    type: "user",
    message: {
      role: "user",
      content: "Hello, can you help me with this code?"
    },
    uuid: "regular-uuid-1",
    timestamp: "2025-07-20T04:32:32.563Z"
  },
  {
    parentUuid: "regular-uuid-1",
    isSidechain: false,
    userType: "external",
    cwd: "cwd",
    sessionId: "regular-session-id",
    version: "1.0.56",
    type: "assistant",
    message: {
      role: "assistant",
      content: "Of course! I'd be happy to help you with your code."
    },
    uuid: "regular-uuid-2",
    timestamp: "2025-07-20T04:33:00.000Z"
  }
];

describe('annotateInternalMessages', () => {
  it('should mark terminal control messages with internalMessageType', () => {
    // Make a copy of the sample data to avoid mutating the original
    const messages = JSON.parse(JSON.stringify(SampleChat_WithTerminalControl));
    
    annotateInternalMessages(messages);

    // Verify terminal control messages are marked correctly
    expect(messages).toHaveLength(4);
    expect(messages[0].internalMessageType).toBeUndefined(); // Caveat message (meta, not terminal control)
    expect(messages[1].internalMessageType).toBe('terminal_control'); // /clear command
    expect(messages[2].internalMessageType).toBe('terminal_control'); // command stdout
    expect(messages[3].internalMessageType).toBeUndefined(); // Regular message
  });

  it('should not mark regular messages as internal', () => {
    // Make a copy of the sample data to avoid mutating the original
    const messages = JSON.parse(JSON.stringify(SampleChat));
    
    annotateInternalMessages(messages);

    // Verify no messages are marked as internal
    expect(messages).toHaveLength(2);
    expect(messages[0].internalMessageType).toBeUndefined();
    expect(messages[1].internalMessageType).toBeUndefined();
  });

  it('should detect /clear command pattern', () => {
    const clearMessage: ChatMessage = {
      parentUuid: null,
      isSidechain: false,
      userType: "external",
      cwd: "/test",
      sessionId: "test-session",
      version: "1.0.0",
      type: "user",
      message: {
        role: "user",
        content: "<command-name>/clear</command-name>\n<command-message>clear</command-message>\n<command-args></command-args>"
      },
      uuid: "test-uuid",
      timestamp: "2025-07-20T00:00:00.000Z"
    };

    annotateInternalMessages([clearMessage]);

    expect(clearMessage.internalMessageType).toBe('terminal_control');
  });

  it('should detect local command stdout pattern', () => {
    const stdoutMessage: ChatMessage = {
      parentUuid: null,
      isSidechain: false,
      userType: "external",
      cwd: "/test",
      sessionId: "test-session",
      version: "1.0.0",
      type: "user",
      message: {
        role: "user",
        content: "<local-command-stdout>some output here</local-command-stdout>"
      },
      uuid: "test-uuid",
      timestamp: "2025-07-20T00:00:00.000Z"
    };

    annotateInternalMessages([stdoutMessage]);

    expect(stdoutMessage.internalMessageType).toBe('terminal_control');
  });

  it('should detect PreToolUse hook messages', () => {
    const hookMessage: ChatMessage = {
      parentUuid: "parent-uuid",
      isSidechain: false,
      userType: "external",
      cwd: "/test",
      sessionId: "test-session",
      version: "1.0.56",
      gitBranch: "main",
      type: "system",
      message: {
        role: "assistant",
        content: "\u001b[1mPreToolUse:Edit\u001b[22m [/Users/andy.fischer/ai-coding-tools/ts-rubberstamp/bin/ts-rubberstamp] completed successfully"
      },
      content: "\u001b[1mPreToolUse:Edit\u001b[22m [/Users/andy.fischer/ai-coding-tools/ts-rubberstamp/bin/ts-rubberstamp] completed successfully",
      isMeta: false,
      timestamp: "2025-07-20T04:46:32.040Z",
      uuid: "hook-uuid",
      toolUseID: "toolu_01QDwnBPegihfz51r1qm2tbg",
      level: "info"
    };

    annotateInternalMessages([hookMessage]);

    expect(hookMessage.internalMessageType).toBe('hook');
  });
});
```

## File: `claude-history-tool/src/renderer/App.tsx`
```tsx
import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';
import { HashRouter, Routes, Route, useNavigate, useParams, useSearchParams, useLocation } from 'react-router-dom';
import { QueryClient, QueryClientProvider, useQuery, useQueryClient } from '@tanstack/react-query';
import { ChatList } from '../components/ChatList';
import { LoadingSpinner } from '../components/LoadingSpinner';
import { LeftSidebar } from '../components/LeftSidebar';
import { AnalyticsPanel } from '../components/AnalyticsPanel';
import { ChatDetailsPanel } from '../components/ChatDetailsPanel';
import { UpgradeBanner } from '../components/UpgradeBanner';
import { UpgradeModal } from '../components/UpgradeModal';
import { useUpgradeNotice } from '../hooks/useUpgradeNotice';
import { ChatSession } from '../types';
import '../style.scss';

const ChatListPage: React.FC = () => {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  const queryClient = useQueryClient();

  const { data: projects = [], isLoading: loading, error } = useQuery({
    queryKey: ['chatSessions'],
    queryFn: async () => {
      console.log('[ChatListPage] Calling getChatSessions...');

      if (!window.electronAPI) {
        throw new Error('Electron API not available');
      }
      
      const result = await window.electronAPI.getChatSessions();
      return result;
    },
    retry: 3,
    retryDelay: 1000,
    enabled: !!window.electronAPI, // Only run query when electronAPI is available
  });

  if (error) {
    console.error('Failed to load chat sessions:', error);
    return (
      <div className="h-full flex items-center justify-center flex-col" style={{ backgroundColor: 'var(--color-bg-secondary)' }}>
        <div className="text-red-500 mb-4">Failed to load chat sessions</div>
        <div className="text-sm text-gray-600 mb-4">{error.message}</div>
        <button 
          onClick={() => queryClient.invalidateQueries({ queryKey: ['chatSessions'] })}
          className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
        >
          Retry
        </button>
      </div>
    );
  }

  const handleSessionSelect = (session: ChatSession) => {
    console.log('[ChatListPage] handleSessionSelect:', session);
    navigate(`/chat/${session.sessionId}`, { 
      state: { 
        expandedProjects: searchParams.get('expanded')?.split(',') || [],
        scrollPosition: window.scrollY 
      }
    });
  };

  const handleRefresh = () => {
    queryClient.invalidateQueries({ queryKey: ['chatSessions'] });
  };

  if (loading) {
    return (
      <div className="h-full flex items-center justify-center" style={{ backgroundColor: 'var(--color-bg-secondary)' }}>
        <LoadingSpinner 
          size={50} 
          message="Loading chat history..." 
        />
      </div>
    );
  }

  return (
    <ChatList 
      projects={projects} 
      onSessionSelect={handleSessionSelect} 
      onRefresh={handleRefresh}
    />
  );
};

const ChatDetailsPage: React.FC = () => {
  const { sessionId } = useParams<{ sessionId: string }>();
  const navigate = useNavigate();

  const { data: projects = [] } = useQuery({
    queryKey: ['chatSessions'],
    queryFn: async () => {
      return await window.electronAPI.getChatSessions();
    },
  });

  const session = projects
    .flatMap(project => project.sessions)
    .find(s => s.sessionId === sessionId);

  const handleBackToList = () => {
    navigate('/', { replace: true });
  };

  if (!session) {
    return (
      <div className="h-full flex items-center justify-center" style={{ backgroundColor: 'var(--color-bg-secondary)' }}>
        <LoadingSpinner 
          size={50} 
          message="Loading chat session..." 
        />
      </div>
    );
  }

  return (
    <ChatDetailsPanel 
      session={session} 
      onBackToList={handleBackToList}
    />
  );
};

const AppLayout: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const [showBanner, setShowBanner] = useState(true);
  const [showModal, setShowModal] = useState(true);
  
  const activeView = location.pathname === '/analytics' ? 'analytics' : 'chats';

  console.log('[AppLayout] activeView:', activeView);
  console.log('[AppLayout] location:', location);


  const handleViewChange = (view: 'chats' | 'analytics') => {
    console.log('[AppLayout] handleViewChange:', view);
    if (view === 'analytics') {
      navigate('/analytics');
    } else {
      navigate('/');
    }
  };

  const { data: upgradeNotice } = useUpgradeNotice();

  const shouldShowBanner = showBanner && upgradeNotice?.bannerHtml;
  const shouldShowModal = showModal && upgradeNotice?.popupHtml && upgradeNotice.popupHtml !== '';

  return (
    <div className="h-screen flex flex-col">
      {shouldShowBanner && (
        <UpgradeBanner 
          html={upgradeNotice.bannerHtml!}
          contentCode={upgradeNotice.bannerContentCode!}
          onClose={() => setShowBanner(false)}
        />
      )}
      
      <div className="flex flex-1 overflow-hidden">
        <LeftSidebar 
          activeView={activeView}
          onViewChange={handleViewChange}
        />
        
        <main className="flex-1 overflow-hidden">
          <Routes>
            <Route path="/" element={<ChatListPage />} />
            <Route path="/analytics" element={<AnalyticsPanel />} />
            <Route path="/chat/:sessionId" element={<ChatDetailsPage />} />
            <Route path="*" element={<ChatListPage />} />
          </Routes>
        </main>
      </div>

      {shouldShowModal && (
        <UpgradeModal 
          isOpen={shouldShowModal}
          html={upgradeNotice.popupHtml!}
          contentCode={upgradeNotice.popupContentCode!}
          onClose={() => setShowModal(false)}
        />
      )}
    </div>
  );
};

const App: React.FC = () => {
  return (
    <HashRouter>
      <AppLayout />
    </HashRouter>
  );
};

const queryClient = new QueryClient();

const container = document.getElementById('root');
if (container) {
  const root = createRoot(container);
  root.render(
    <QueryClientProvider client={queryClient}>
      <App />
    </QueryClientProvider>
  );
}
```

## File: `claude-history-tool/src/renderer/index.html`
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Claude History Tool</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lexend+Deca:wght@100..900&display=swap" rel="stylesheet">
    <style>
      body {
        font-family: "Lexend Deca", -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f5f5f5;
      }
    </style>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
```

## File: `claude-history-tool/src/test/setup.ts`
```typescript
import '@testing-library/jest-dom';
import { vi } from 'vitest';

// Mock electronAPI for tests
(global as any).window = {
  electronAPI: {
    getChatSessions: vi.fn(),
    getSessionDetails: vi.fn(),
  },
};
```

## File: `claude-history-tool/src/types/global.d.ts`
```typescript
import { AnalyticsData } from '../main/getAnalytics';
import { ProjectDirectory, ChatMessage } from './index';

declare global {
  interface Window {
    electronAPI: {
      getChatSessions: () => Promise<ProjectDirectory[]>;
      getSessionDetails: (sessionId: string, projectName: string) => Promise<ChatMessage[]>;
      getAnalytics: () => Promise<AnalyticsData>;
      isNotificationDismissed: (contentCode: string) => Promise<boolean>;
      dismissNotification: (contentCode: string) => Promise<void>;
      getApiHostname: () => Promise<string>;
    };
  }
}

export {};
```

## File: `claude-history-tool/src/types/index.ts`
```typescript
export interface ChatMessage {
  parentUuid: string | null;
  isSidechain: boolean;
  userType: string;
  cwd: string;
  sessionId: string;
  version: string;
  gitBranch?: string;
  type: 'user' | 'assistant' | 'system';
  message?: {
    role: 'user' | 'assistant';
    content: string | Array<{
      type: 'text' | 'tool_use' | 'tool_result';
      text?: string;
      id?: string;
      name?: string;
      input?: any;
      tool_use_id?: string;
    }>;
    id?: string;
    model?: string;
    stop_reason?: string | null;
    stop_sequence?: string | null;
    usage?: {
      input_tokens?: number;
      cache_creation_input_tokens?: number;
      cache_read_input_tokens?: number;
      output_tokens?: number;
      service_tier?: string;
    };
  };
  content?: string;
  isMeta?: boolean;
  level?: string;
  toolUseID?: string;
  uuid: string;
  timestamp: string;
  requestId?: string;
  toolUseResult?: any;
  internalMessageType?: 'terminal_control' | 'hook';
}

export interface ChatSession {
  sessionId: string;
  messages: ChatMessage[];
  firstMessageTimestamp: string;
  lastMessageTimestamp: string;
  projectPath: string;
  messageCount: number;
}

export interface ProjectDirectory {
  path: string;
  sessions: ChatSession[];
}
```

## File: `claude-history-tool/src/types/upgrade.ts`
```typescript
export interface UpgradeNoticeResponse {
  bannerHtml?: string;
  bannerContentCode?: string;
  popupHtml?: string;
  popupContentCode?: string;
}
```

## File: `mcp-cli/.gitignore`
```
dist
```

## File: `mcp-cli/README.md`
```markdown
# MCP CLI

Very simple terminal-based UI for browsing MCP (Model Context Protocol) servers.

You probably shouldn't use this yet, instead use this instead: https://github.com/chrishayuk/mcp-cli

## Installation

```bash
yarn install
yarn build
```

## Usage

### Connect to an MCP server via URL
```bash
node dist/index.js https://your-mcp-server.com
```

### Connect to an MCP server via stdin/stdout
```bash
node dist/index.js "python your-mcp-server.py"
```

## REPL Commands

Once connected, you can use the following commands in the interactive REPL:

- `tools/list` - List all available tools
- `resources/list` - List all available resources  
- `tools/call <tool-name> [args...]` - Call a tool with arguments
- `resources/read <uri>` - Read a resource by URI
- `help` - Show available commands
- `exit` - Exit the REPL

## Features

- **Tab completion** - Press Tab to autocomplete commands
- **Command history** - Use up/down arrows to browse command history
- **Multiple connection modes** - Support for both HTTP/SSE and stdin/stdout connections
- **Interactive REPL** - Full-featured REPL with readline support

## Example Session

```
$ node dist/index.js "python my-mcp-server.py"
Connecting to MCP server...
Connected successfully!
MCP CLI - Type "help" for available commands
mcp> tools/list
Available tools:
  get_weather
    Get current weather for a location
  calculate
    Perform mathematical calculations
mcp> tools/call get_weather location "San Francisco"
Tool result:
{
  "content": [
    {
      "type": "text",
      "text": "The weather in San Francisco is sunny, 72°F"
    }
  ]
}
mcp> exit
Goodbye!
```
```

## File: `mcp-cli/package.json`
```json
{
  "name": "mcp-cli",
  "version": "1.0.0",
  "description": "Terminal-based UI for browsing MCP (Model Context Protocol) servers",
  "main": "dist/main.js",
  "bin": {
    "mcp-cli": "bin/mcp-cli"
  },
  "scripts": {
    "build": "tsc",
    "dev": "tsx src/main.ts",
    "start": "node dist/main.js",
    "typecheck": "tsc --noEmit"
  },
  "keywords": [
    "mcp",
    "cli",
    "repl",
    "terminal"
  ],
  "author": "",
  "license": "MIT",
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.0.0",
    "source-map-support": "^0.5.21"
  },
  "devDependencies": {
    "@types/node": "^20.0.0",
    "tsx": "^4.0.0",
    "typescript": "^5.0.0"
  },
  "packageManager": "yarn@1.22.22+sha512.a6b2f7906b721bba3d67d4aff083df04dad64c399707841b7acf00f6b133b7ac24255f2652fa22ae3534329dc6180534e98d17432037ff6fd140556e2bb3137e"
}
```

## File: `mcp-cli/tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "commonjs",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": false,
    "noImplicitAny": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "resolveJsonModule": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

## File: `mcp-cli/src/main.ts`
```typescript
import 'source-map-support/register';

import { McpClient } from './mcp-client.js';
import { McpRepl } from './repl.js';

export async function main(): Promise<void> {
  const args = process.argv.slice(2);

  if (args.length === 0) {
    console.error('Error: Missing server argument');
    console.error('Usage: mcp-cli <server>');
    console.error('  server: Server address (URL or command to run in stdin mode)');
    process.exit(1);
  }

  if (args[0] === '--help' || args[0] === '-h') {
    console.log('mcp-cli - Terminal-based UI for browsing MCP (Model Context Protocol) servers');
    console.log('');
    console.log('Usage: mcp-cli <server>');
    console.log('  server: Server address (URL or command to run in stdin mode)');
    console.log('');
    console.log('Examples:');
    console.log('  mcp-cli http://localhost:3000');
    console.log('  mcp-cli npx @modelcontextprotocol/server-filesystem /path/to/dir');
    process.exit(0);
  }

  try {
    let clientOptions;
    
    const server = args[0];
    if (server.startsWith('http://') || server.startsWith('https://')) {
      // URL mode
      clientOptions = { serverUrl: server };
    } else {
      // Stdin mode - use all args as the command
      clientOptions = { command: args };
    }

    console.log('Connecting to MCP server...');
    const client = new McpClient(clientOptions);
    await client.connect();

    const repl = new McpRepl(client);
    await repl.start();
  } catch (error) {
    console.error('Error:', error);
    process.exit(1);
  }
}
```

## File: `mcp-cli/src/mcp-client.ts`
```typescript
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StdioClientTransport } from '@modelcontextprotocol/sdk/client/stdio.js';
import { SSEClientTransport } from '@modelcontextprotocol/sdk/client/sse.js';
import { spawn } from 'child_process';
import { McpClientOptions, ToolInfo, ResourceInfo } from './types.js';

export class McpClient {
  private client: Client;
  private transport!: StdioClientTransport | SSEClientTransport;

  constructor(private options: McpClientOptions) {
    this.client = new Client(
      { name: 'mcp-cli', version: '1.0.0' },
      { capabilities: {} }
    );
  }

  async connect(): Promise<void> {
    if (this.options.serverUrl) {
      // HTTP/SSE connection
      this.transport = new SSEClientTransport(new URL(this.options.serverUrl));
    } else if (this.options.command) {
      // Stdin/stdout connection
      const childProcess = spawn(this.options.command[0], this.options.command.slice(1), {
        stdio: ['pipe', 'pipe', 'inherit'],
      });
      this.transport = new StdioClientTransport({
        command: this.options.command[0],
        args: this.options.command.slice(1),
      });
    } else {
      throw new Error('Either serverUrl or command must be provided');
    }

    await this.client.connect(this.transport);
  }

  async listTools(): Promise<ToolInfo[]> {
    const response = await this.client.listTools();
    return response.tools.map(tool => ({
      name: tool.name,
      description: tool.description,
      inputSchema: tool.inputSchema
    }));
  }

  async listResources(): Promise<ResourceInfo[]> {
    const response = await this.client.listResources();
    return response.resources.map(resource => ({
      uri: resource.uri,
      name: resource.name,
      description: resource.description,
      mimeType: resource.mimeType
    }));
  }

  async callTool(name: string, args: Record<string, any>): Promise<any> {
    const response = await this.client.callTool({
      name,
      arguments: args
    });
    return response;
  }

  async readResource(uri: string): Promise<any> {
    const response = await this.client.readResource({ uri });
    return response;
  }

  async disconnect(): Promise<void> {
    await this.client.close();
  }
}
```

## File: `mcp-cli/src/repl.ts`
```typescript
import * as readline from 'readline';
import { McpClient } from './mcp-client.js';

interface Command {
  name: string;
  description: string;
  handler: (args: string[]) => Promise<void>;
}

export class McpRepl {
  private rl: readline.Interface;
  private commands: Map<string, Command> = new Map();
  private history: string[] = [];

  constructor(private client: McpClient) {
    this.rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
      prompt: 'mcp> ',
      completer: this.completer.bind(this),
      history: this.history
    });

    this.setupCommands();
  }

  private setupCommands(): void {
    this.commands.set('tools/list', {
      name: 'tools/list',
      description: 'List all available tools',
      handler: this.handleToolsList.bind(this)
    });

    this.commands.set('resources/list', {
      name: 'resources/list',
      description: 'List all available resources',
      handler: this.handleResourcesList.bind(this)
    });

    this.commands.set('tools/call', {
      name: 'tools/call',
      description: 'Call a tool: tools/call <tool-name> [args...]',
      handler: this.handleToolsCall.bind(this)
    });

    this.commands.set('resources/read', {
      name: 'resources/read',
      description: 'Read a resource: resources/read <uri>',
      handler: this.handleResourcesRead.bind(this)
    });

    this.commands.set('help', {
      name: 'help',
      description: 'Show available commands',
      handler: this.handleHelp.bind(this)
    });

    this.commands.set('exit', {
      name: 'exit',
      description: 'Exit the REPL',
      handler: this.handleExit.bind(this)
    });
  }

  private completer(line: string): [string[], string] {
    const completions = Array.from(this.commands.keys());
    const hits = completions.filter((c) => c.startsWith(line));
    return [hits.length ? hits : completions, line];
  }

  private async handleToolsList(): Promise<void> {
    try {
      const tools = await this.client.listTools();
      if (tools.length === 0) {
        console.log('No tools available');
        return;
      }
      
      console.log('Available tools:');
      tools.forEach(tool => {
        console.log(`  ${tool.name}`);
        if (tool.description) {
          console.log(`    ${tool.description}`);
        }
      });
    } catch (error) {
      console.error('Error listing tools:', error);
    }
  }

  private async handleResourcesList(): Promise<void> {
    try {
      const resources = await this.client.listResources();
      if (resources.length === 0) {
        console.log('No resources available');
        return;
      }
      
      console.log('Available resources:');
      resources.forEach(resource => {
        console.log(`  ${resource.uri}`);
        if (resource.name) {
          console.log(`    Name: ${resource.name}`);
        }
        if (resource.description) {
          console.log(`    Description: ${resource.description}`);
        }
        if (resource.mimeType) {
          console.log(`    Type: ${resource.mimeType}`);
        }
      });
    } catch (error) {
      console.error('Error listing resources:', error);
    }
  }

  private async handleToolsCall(args: string[]): Promise<void> {
    if (args.length < 1) {
      console.log('Usage: tools/call <tool-name> [args...]');
      return;
    }

    const toolName = args[0];
    const toolArgs: Record<string, any> = {};

    // Simple argument parsing
    for (let i = 1; i < args.length; i += 2) {
      if (i + 1 < args.length) {
        toolArgs[args[i]] = args[i + 1];
      }
    }

    try {
      const result = await this.client.callTool(toolName, toolArgs);
      console.log('Tool result:');
      console.log(JSON.stringify(result, null, 2));
    } catch (error) {
      console.error('Error calling tool:', error);
    }
  }

  private async handleResourcesRead(args: string[]): Promise<void> {
    if (args.length < 1) {
      console.log('Usage: resources/read <uri>');
      return;
    }

    const uri = args[0];

    try {
      const result = await this.client.readResource(uri);
      console.log('Resource content:');
      console.log(JSON.stringify(result, null, 2));
    } catch (error) {
      console.error('Error reading resource:', error);
    }
  }

  private async handleHelp(): Promise<void> {
    console.log('Available commands:');
    this.commands.forEach(command => {
      console.log(`  ${command.name} - ${command.description}`);
    });
  }

  private async handleExit(): Promise<void> {
    console.log('Goodbye!');
    await this.client.disconnect();
    process.exit(0);
  }

  async start(): Promise<void> {
    console.log('Connected - Type "help" for available commands');
    
    this.rl.on('line', async (input) => {
      const trimmed = input.trim();
      if (!trimmed) {
        this.rl.prompt();
        return;
      }

      this.history.push(trimmed);
      const parts = trimmed.split(/\s+/);
      const commandName = parts[0];
      const args = parts.slice(1);

      const command = this.commands.get(commandName);
      if (command) {
        await command.handler(args);
      } else {
        console.log(`Unknown command: ${commandName}. Type "help" for available commands.`);
      }

      this.rl.prompt();
    });

    this.rl.on('SIGINT', () => {
      console.log('\nUse "exit" to quit');
      this.rl.prompt();
    });

    this.rl.prompt();
  }
}
```

## File: `mcp-cli/src/types.ts`
```typescript
export interface McpClientOptions {
  serverUrl?: string;
  command?: string[];
}

export interface ToolCall {
  name: string;
  arguments: Record<string, any>;
}

export interface ResourceInfo {
  uri: string;
  name?: string;
  description?: string;
  mimeType?: string;
}

export interface ToolInfo {
  name: string;
  description?: string;
  inputSchema: any;
}
```


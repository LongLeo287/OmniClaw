---
id: ktab
type: knowledge
owner: OA_Triage
---
# ktab
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "ktab",
  "version": "0.4.4",
  "description": "Simple tool for effortlessly managing your tabs, bookmarks, and browser history",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/dunkbing/ktab.git"
  },
  "scripts": {
    "clean": "turbo clean && turbo daemon stop && rimraf dist && rimraf .turbo",
    "build": "turbo build",
    "build:firefox": "cross-env __FIREFOX__=true turbo build",
    "zip": "turbo zip",
    "zip:firefox": "cross-env __FIREFOX__=true turbo zip",
    "dev-server": "pnpm -F hmr ready && pnpm -F hmr dev",
    "dev": "turbo ready && turbo watch dev --concurrency 20",
    "dev:firefox": "turbo ready && cross-env __FIREFOX__=true turbo watch dev --concurrency 20",
    "test": "turbo test",
    "type-check": "turbo type-check",
    "lint": "turbo lint --continue -- --fix --cache --cache-location node_modules/.cache/.eslintcache",
    "lint:fix": "turbo lint:fix --continue -- --fix --cache --cache-location node_modules/.cache/.eslintcache",
    "prettier": "turbo prettier --continue -- --cache --cache-location node_modules/.cache/.prettiercache",
    "prepare": "husky",
    "update-version": "run-script-os",
    "update-version:win32": "bash update_version.sh",
    "update-version:default": "./update_version.sh"
  },
  "type": "module",
  "dependencies": {
    "react": "18.3.1",
    "react-dom": "18.3.1",
    "lucide-react": "^0.428.0"
  },
  "devDependencies": {
    "@types/chrome": "^0.0.270",
    "@types/node": "^22.4.1",
    "@types/react": "^18.3.3",
    "@types/react-dom": "^18.3.0",
    "@typescript-eslint/eslint-plugin": "^7.18.0",
    "@typescript-eslint/parser": "^7.18.0",
    "autoprefixer": "^10.4.19",
    "cross-env": "^7.0.3",
    "esbuild": "^0.23.0",
    "eslint": "8.57.0",
    "eslint-config-airbnb-typescript": "18.0.0",
    "eslint-config-prettier": "9.1.0",
    "eslint-plugin-import": "2.29.1",
    "eslint-plugin-jsx-a11y": "6.9.0",
    "eslint-plugin-prettier": "5.2.1",
    "eslint-plugin-react": "7.35.0",
    "eslint-plugin-react-hooks": "4.6.2",
    "husky": "^9.1.4",
    "lint-staged": "^15.2.7",
    "postcss": "^8.4.38",
    "prettier": "^3.3.3",
    "rimraf": "^6.0.1",
    "tailwindcss": "^3.4.10",
    "tslib": "^2.6.3",
    "turbo": "^2.0.12",
    "typescript": "5.5.4",
    "vite": "5.4.1",
    "run-script-os": "^1.1.6"
  },
  "lint-staged": {
    "*.{js,jsx,ts,tsx}": [
      "prettier --write"
    ]
  },
  "packageManager": "pnpm@9.8.0+sha512.8e4c3550fb500e808dbc30bb0ce4dd1eb614e30b1c55245f211591ec2cdf9c611cabd34e1364b42f564bd54b3945ed0f49d61d1bbf2ec9bd74b866fcdc723276",
  "engines": {
    "node": ">=18.12.0"
  }
}

```

### File: README.md
```md
# KTab: Command Palette Chrome Extension

![Preview](sc/sc1.png)

KTab is a Chrome extension that adds a command palette to your browser.

## Key Features

- Quick access with keyboard shortcut (Cmd+Shift+K / Ctrl+Shift+K)
- Search across tabs, history, bookmarks, and Google suggestions
- Tab management and quick actions
- Keyboard navigation

## Installation

[Download KTab from the Chrome Web Store](https://chromewebstore.google.com/detail/lpnolmmbpjnenjoanhdbgfdjiknmfpnm?authuser=0&hl=en)

## Usage

1. Open with Cmd+Shift+K (Mac) or Ctrl+Shift+K (Windows/Linux)
2. Type to search
3. Use arrow keys to navigate
4. Press Enter to select

Special commands: `/tab`, `/history`, `/bookmark`

## Development

1. Clone repo and navigate to directory
2. Run `pnpm install`
3. Build: `pnpm run build` or dev mode: `pnpm dev`
4. Load unpacked extension from `dist` directory in Chrome

Follow [@dunkbing](https://www.tiktok.com/@dunkbing) on TikTok for occasional live coding sessions.

```

### File: packages\i18n\package.json
```json
{
  "name": "@extension/i18n",
  "version": "0.3.1",
  "description": "chrome extension internationalization",
  "private": true,
  "sideEffects": false,
  "files": [
    "dist/**"
  ],
  "types": "index.ts",
  "main": "./dist/index.js",
  "scripts": {
    "clean": "rimraf ./dist",
    "genenrate-i8n": "node genenrate-i18n.mjs",
    "ready": "pnpm genenrate-i8n && node build.dev.mjs",
    "build": "pnpm genenrate-i8n && node build.prod.mjs",
    "lint": "eslint . --ext .ts,.tsx",
    "lint:fix": "pnpm lint --fix",
    "prettier": "prettier . --write --ignore-path ../../.prettierignore",
    "type-check": "tsc --noEmit"
  },
  "dependencies": {},
  "devDependencies": {
    "@extension/tsconfig": "workspace:*",
    "@extension/hmr": "workspace:*"
  }
}

```

### File: packages\i18n\README.md
```md
# I18n Package

This package provides a set of tools to help you internationalize your Chrome Extension.

https://developer.chrome.com/docs/extensions/reference/api/i18n

## Installation

If you want to use the i18n translation function in each pages, you need to add the following to the package.json file.

```json
{
  "dependencies": {
    "@extension/i18n": "workspace:*"
  }
}
```

Then run the following command to install the package.

```bash
pnpm install
```

## Manage translations

You can manage translations in the `locales` directory.

`locales/en/messages.json`

```json
{
  "helloWorld": {
    "message": "Hello, World!"
  }
}
```

`locales/ko/messages.json`

```json
{
  "helloWorld": {
    "message": "안녕하세요, 여러분!"
  }
}
```

## Delete or Add a new language

When you want to delete or add a new language, you don't need to edit some util files like `lib/types.ts` or `lib/getMessageFromLocale.ts`. 
That's because we provide a script to generate util files automatically by the `generate-i18n.mjs` file.

Following the steps below to delete or add a new language.

### Delete a language

If you want to delete unused languages, you can delete the corresponding directory in the `locales` directory.

```
locales
├── en
│   └── messages.json
└── ko // delete this directory
    └── messages.json 
```

Then run the following command. (or just run `pnpm dev` or `pnpm build` on root)

```bash
pnpm genenrate-i8n
```

### Add a new language

If you want to add a new language, you can create a new directory in the `locales` directory.

```
locales
├── en
│   └── messages.json
├── ko
│   └── messages.json
└── ja // create this directory
    └── messages.json // and create this file 
```

Then same as above, run the following command. (or just run `pnpm dev` or `pnpm build` on root)

```bash
pnpm genenrate-i8n
```


## Usage

### Translation function

Just import the `t` function and use it to translate the key.

```typescript
import { t } from '@extension/i18n';

console.log(t('loading')); // Loading...
```

```typescript jsx
import { t } from '@extension/i18n';

const Component = () => {
  return (
    <button>
      {t('toggleTheme')} // Toggle Theme
    </button>
  );
};
```

### Placeholders

If you want to use placeholders, you can use the following format.

> For more information, see the [Message Placeholders](https://developer.chrome.com/docs/extensions/how-to/ui/localization-message-formats#placeholders) section.

`locales/en/messages.json`

```json
{
  "greeting": {
    "description": "Greeting message",
    "message": "Hello, My name is $NAME$",
    "placeholders": {
      "name": {
        "content": "$1",
        "example": "John Doe"
      }
    }
  },
  "hello": {
    "description": "Placeholder example",
    "message": "Hello $1"
  }
}
```

`locales/ko/messages.json`

```json
{
  "greeting": {
    "description": "인사 메시지",
    "message": "안녕하세요, 제 이름은 $NAME$입니다.",
    "placeholders": {
      "name": {
        "content": "$1",
        "example": "서종학"
      }
    }
  },
  "hello": {
    "description": "Placeholder 예시",
    "message": "안녕 $1"
  }
}
```

If you want to replace the placeholder, you can pass the value as the second argument.

Function `t` has exactly the same interface as the `chrome.i18n.getMessage` function.

```typescript
import { t } from '@extension/i18n';

console.log(t('greeting', 'John Doe')); // Hello, My name is John Doe
console.log(t('greeting', ['John Doe'])); // Hello, My name is John Doe

console.log(t('hello')); // Hello
console.log(t('hello', 'World')); // Hello World
console.log(t('hello', ['World'])); // Hello World
```

### Locale setting on development

If you want to show specific language, you can set the `devLocale` property. (only for development)

```typescript
import { t } from '@extension/i18n';

t.devLocale = "ko";

console.log(t('hello')); // 안녕
```

### Type Safety

When you forget to add a key to all language's `messages.json` files, you will get a Typescript error.

`locales/en/messages.json`

```json
{
  "hello": {
    "message": "Hello World!"
  }
}
```

`locales/ko/messages.json`

```json
{
  "helloWorld": {
    "message": "안녕하세요, 여러분!"
  }
}
```

```typescript
import { t } from '@extension/i18n';

// Error: TS2345: Argument of type "hello" is not assignable to parameter of type
console.log(t('hello'));
```

```

### File: packages\shared\package.json
```json
{
  "name": "@extension/shared",
  "version": "0.3.1",
  "description": "chrome extension shared code",
  "private": true,
  "sideEffects": false,
  "files": [
    "dist/**"
  ],
  "types": "index.ts",
  "main": "./dist/index.js",
  "scripts": {
    "clean": "rimraf ./dist",
    "ready": "node build.mjs",
    "lint": "eslint . --ext .ts,.tsx",
    "lint:fix": "pnpm lint --fix",
    "prettier": "prettier . --write --ignore-path ../../.prettierignore",
    "type-check": "tsc --noEmit"
  },
  "dependencies": {},
  "devDependencies": {
    "@extension/storage": "workspace:*",
    "@extension/tsconfig": "workspace:*"
  }
}

```

### File: packages\shared\README.md
```md
# Shared Package

This package contains code shared with other packages.
To use the code in the package, you need to add the following to the package.json file.

```json
{
  "dependencies": {
    "@extension/shared": "workspace:*"
  }
}
```

```

### File: packages\storage\package.json
```json
{
  "name": "@extension/storage",
  "version": "0.3.1",
  "description": "chrome extension storage",
  "private": true,
  "sideEffects": false,
  "files": [
    "dist/**"
  ],
  "main": "./dist/index.js",
  "types": "index.ts",
  "scripts": {
    "clean": "rimraf ./dist",
    "ready": "node build.mjs",
    "lint": "eslint . --ext .ts,.tsx",
    "lint:fix": "pnpm lint --fix",
    "prettier": "prettier . --write --ignore-path ../../.prettierignore",
    "type-check": "tsc --noEmit"
  },
  "dependencies": {},
  "devDependencies": {
    "@extension/tsconfig": "workspace:*"
  }
}

```

### File: packages\ui\package.json
```json
{
  "name": "@extension/ui",
  "version": "0.3.1",
  "description": "chrome extension ui components",
  "private": true,
  "sideEffects": false,
  "type": "module",
  "files": [
    "dist/**",
    "dist/global.css"
  ],
  "types": "index.ts",
  "main": "./dist/index.js",
  "scripts": {
    "clean": "rimraf ./dist && rimraf .turbo",
    "ready": "node build.mjs",
    "lint": "eslint . --ext .ts,.tsx",
    "lint:fix": "pnpm lint --fix",
    "prettier": "prettier . --write",
    "type-check": "tsc --noEmit"
  },
  "devDependencies": {
    "@extension/tsconfig": "workspace:*",
    "deepmerge": "^4.3.1"
  },
  "dependencies": {
    "clsx": "^2.1.1",
    "tailwind-merge": "^2.5.2"
  }
}

```

### File: packages\ui\README.md
```md
# UI Package

This package provides components that make up the UI.

## Installation

First, move to the page you want to use.

```shell
cd pages/options
```

Add the following to the dependencies in `package.json`.

```json
{
  "dependencies": {
    "@extension/ui": "workspace:*"
  }
}
```

Then, run `pnpm install`.

```shell
pnpm install
```

Add the following to the `tailwind.config.js` file.

```js
const baseConfig = require('@extension/tailwindcss-config');
const { withUI } = require('@extension/ui');

/** @type {import('tailwindcss').Config} */
module.exports = withUI({
  ...baseConfig,
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
});
```

Add the following to the `index.tsx` file.

```tsx
import '@extension/ui/dist/global.css';
```

## Add Component

Add the following to the `lib/components/index.ts` file.

```tsx
export * from './Button';
```

Add the following to the `lib/components/Button.tsx` file.

```tsx
import { ComponentPropsWithoutRef } from 'react';
import { cn } from '../utils';

export type ButtonProps = {
  theme?: 'light' | 'dark';
} & ComponentPropsWithoutRef<'button'>;

export function Button({ theme, className, children, ...props }: ButtonProps) {
  return (
    <button
      className={cn(
        className,
        'mt-4 py-1 px-4 rounded shadow hover:scale-105',
        theme === 'light' ? 'bg-white text-black' : 'bg-black text-white',
      )}
      {...props}>
      {children}
    </button>
  );
}
```

## Usage

```tsx
import { Button } from '@extension/ui';

export default function ToggleButton() {
  const [theme, setTheme] = useState<'light' | 'dark'>('light');

  const toggle = () => {
    setTheme(theme === 'light' ? 'dark' : 'light');
  };

  return (
    <Button theme={theme} onClick={toggle}>
      Toggle
    </Button>
  );
}
```

## Modifying the tailwind config of the UI library

Modify the `tailwind.config.ts` file to make global style changes to the package.

## Modifying the css variable of the UI library

Modify the css variable in the `ui/lib/global.css` code to change the css variable of the package.

```

### File: pages\content\package.json
```json
{
  "name": "@extension/content-script",
  "version": "0.3.1",
  "description": "chrome extension content script",
  "private": true,
  "sideEffects": true,
  "files": [
    "dist/**"
  ],
  "scripts": {
    "clean": "rimraf ./dist",
    "build": "pnpm run clean&& pnpm type-check && vite build",
    "build:watch": "cross-env __DEV__=true vite build --mode development",
    "dev": "pnpm build:watch",
    "lint": "eslint . --ext .ts,.tsx",
    "lint:fix": "pnpm lint --fix",
    "prettier": "prettier . --write --ignore-path ../../.prettierignore",
    "type-check": "tsc --noEmit"
  },
  "dependencies": {
    "@extension/shared": "workspace:*",
    "@extension/storage": "workspace:*"
  },
  "devDependencies": {
    "@extension/hmr": "workspace:*",
    "@extension/tsconfig": "workspace:*",
    "@extension/vite-config": "workspace:*"
  }
}

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
      lucide-react:
        specifier: ^0.428.0
        version: 0.428.0(react@18.3.1)
      react:
        specifier: 18.3.1
        version: 18.3.1
      react-dom:
        specifier: 18.3.1
        version: 18.3.1(react@18.3.1)
    devDependencies:
      '@types/chrome':
        specifier: ^0.0.270
        version: 0.0.270
      '@types/node':
        specifier: ^22.4.1
        version: 22.4.1
      '@types/react':
        specifier: ^18.3.3
        version: 18.3.3
      '@types/react-dom':
        specifier: ^18.3.0
        version: 18.3.0
      '@typescript-eslint/eslint-plugin':
        specifier: ^7.18.0
        version: 7.18.0(@typescript-eslint/parser@7.18.0(eslint@8.57.0)(typescript@5.5.4))(eslint@8.57.0)(typescript@5.5.4)
      '@typescript-eslint/parser':
        specifier: ^7.18.0
        version: 7.18.0(eslint@8.57.0)(typescript@5.5.4)
      autoprefixer:
        specifier: ^10.4.19
        version: 10.4.19(postcss@8.4.39)
      cross-env:
        specifier: ^7.0.3
        version: 7.0.3
      esbuild:
        specifier: ^0.23.0
        version: 0.23.0
      eslint:
        specifier: 8.57.0
        version: 8.57.0
      eslint-config-airbnb-typescript:
        specifier: 18.0.0
        version: 18.0.0(@typescript-eslint/eslint-plugin@7.18.0(@typescript-eslint/parser@7.18.0(eslint@8.57.0)(typescript@5.5.4))(eslint@8.57.0)(typescript@5.5.4))(@typescript-eslint/parser@7.18.0(eslint@8.57.0)(typescript@5.5.4))(eslint-plugin-import@2.29.1(@typescript-eslint/parser@7.18.0(eslint@8.57.0)(typescript@5.5.4))(eslint@8.57.0))(eslint@8.57.0)
      eslint-config-prettier:
        specifier: 9.1.0
        version: 9.1.0(eslint@8.57.0)
      eslint-plugin-import:
        specifier: 2.29.1
        version: 2.29.1(@typescript-eslint/parser@7.18.0(eslint@8.57.0)(typescript@5.5.4))(eslint@8.57.0)
      eslint-plugin-jsx-a11y:
        specifier: 6.9.0
        version: 6.9.0(eslint@8.57.0)
      eslint-plugin-prettier:
        specifier: 5.2.1
        version: 5.2.1(@types/eslint@8.56.10)(eslint-config-prettier@9.1.0(eslint@8.57.0))(eslint@8.57.0)(prettier@3.3.3)
      eslint-plugin-react:
        specifier: 7.35.0
        version: 7.35.0(eslint@8.57.0)
      eslint-plugin-react-hooks:
        specifier: 4.6.2
        version: 4.6.2(eslint@8.57.0)
      husky:
        specifier: ^9.1.4
        version: 9.1.4
      lint-staged:
        specifier: ^15.2.7
        version: 15.2.7
      postcss:
        specifier: ^8.4.38
        version: 8.4.39
      prettier:
        specifier: ^3.3.3
        version: 3.3.3
      rimraf:
        specifier: ^6.0.1
        version: 6.0.1
      run-script-os:
        specifier: ^1.1.6
        version: 1.1.6
      tailwindcss:
        specifier: ^3.4.10
        version: 3.4.10(ts-node@10.9.2(@swc/core@1.6.13)(@types/node@22.4.1)(typescript@5.5.4))
      tslib:
        specifier: ^2.6.3
        version: 2.6.3
      turbo:
        specifier: ^2.0.12
        version: 2.0.12
      typescript:
        specifier: 5.5.4
        version: 5.5.4
      vite:
        specifier: 5.4.1
        version: 5.4.1(@types/node@22.4.1)(sass@1.77.8)(terser@5.31.1)

  chrome-extension:
    dependencies:
      '@extension/shared':
        specifier: workspace:*
        version: link:../packages/shared
      '@extension/storage':
        specifier: workspace:*
        version: link:../packages/storage
      webextension-polyfill:
        specifier: ^0.12.0
        version: 0.12.0
    devDependencies:
      '@extension/dev-utils':
        specifier: workspace:*
        version: link:../packages/dev-utils
      '@extension/hmr':
        specifier: workspace:*
        version: link:../packages/hmr
      '@extension/tsconfig':
        specifier: workspace:*
        version: link:../packages/tsconfig
      '@extension/vite-config':
        specifier: workspace:*
        version: link:../packages/vite-config
      '@laynezh/vite-plugin-lib-assets':
        specifier: ^0.5.23
        version: 0.5.23(vite@5.4.1(@types/node@22.4.1)(sass@1.77.8)(terser@5.31.1))
      '@types/ws':
        specifier: ^8.5.12
        version: 8.5.12
      deepmerge:
        specifier: ^4.3.1
        version: 4.3.1
      magic-string:
        specifier: ^0.30.10
        version: 0.30.10
      ts-loader:
        specifier: ^9.5.1
        version: 9.5.1(typescript@5.5.4)(webpack@5.92.1(@swc/core@1.6.13)(esbuild@0.23.0))

  packages/dev-utils:
    devDependencies:
      '@extension/tsconfig':
        specifier: workspace:*
        version: link:../tsconfig

  packages/hmr:
    devDependencies:
      '@extension/tsconfig':
        specifier: workspace:*
        version: link:../tsconfig
      '@rollup/plugin-sucrase':
        specifier: ^5.0.2
        version: 5.0.2(rollup@4.20.0)
      '@types/ws':
        specifier: ^8.5.12
        version: 8.5.12
      esm:
        specifier: ^3.2.25
        version: 3.2.25
      fast-glob:
        specifier: ^3.3.2
        version: 3.3.2
      rollup:
        specifier: ^4.20.0
        version: 4.20.0
      ts-node:
        specifier: ^10.9.2
        version: 10.9.2(@swc/core@1.6.13)(@types/node@22.4.1)(typescript@5.5.4)
      ws:
        specifier: 8.18.0
        version: 8.18.0

  packages/i18n:
    devDependencies:
      '@extension/hmr':
        specifier: workspace:*
        version: link:../hmr
      '@extension/tsconfig':
        specifier: workspace:*
        version: link:../tsconfig

  packages/shared:
    devDependencies:
      '@extension/storage':
        specifier: workspace:*
        version: link:../storage
      '@extension/tsconfig':
        specifier: workspace:*
        version: link:../tsconfig

  packages/storage:
    devDependencies:
      '@extension/tsconfig':
        specifier: workspace:*
        version: link:../tsconfig

  packages/tailwind-config: {}

  packages/tsconfig: {}

  packages/ui:
    dependencies:
      clsx:
        specifier: ^2.1.1
        version: 2.1.1
      tailwind-merge:
        specifier: ^2.5.2
        version: 2.5.2
    devDependencies:
      '@extension/tsconfig':
        specifier: workspace:*
        version: link:../tsconfig
      deepmerge:
        specifier: ^4.3.1
        version: 4.3.1

  packages/vite-config:
    devDependencies:
      '@extension/hmr':
        specifier: workspace:*
        version: link:../hmr
      '@extension/tsconfig':
        specifier: workspace:*
        version: link:../tsconfig
      '@vitejs/plugin-react-swc':
        specifier: ^3.6.0
        version: 3.7.0(vite@5.4.1(@types/node@22.4.1)(sass@1.77.8)(terser@5.31.1))
      deepmerge:
        specifier: ^4.3.1
        version: 4.3.1

  packages/zipper:
    devDependencies:
      '@extension/tsconfig':
        specifier: workspace:*
        version: link:../tsconfig
      fast-glob:
        specifier: ^3.3.2
        version: 3.3.2
      fflate:
        specifier: ^0.8.2
        version: 0.8.2
      tsx:
        specifier: ^4.17.0
        version: 4.17.0

  pages/content:
    dependencies:
      '@extension/shared':
        specifier: workspace:*
        version: link:../../packages/shared
      '@extension/storage':
        specifier: workspace:*
        version: link:../../packages/storage
    devDependencies:
      '@extension/hmr':
        specifier: workspace:*
        version: link:../../packages/hmr
      '@extension/tsconfig':
        specifier: workspace:*
        version: link:../../packages/tsconfig
      '@extension/vite-config':
        specifier: workspace:*
        version: link:../../packages/vite-config

  pages/content-runtime:
    devDependencies:
      '@extension/hmr':
        specifier: workspace:*
        version: link:../../packages/hmr
      '@extension/tsconfig':
        specifier: workspace:*
        version: link:../../packages/tsconfig
      '@extension/vite-config':
        specifier: workspace:*
        version: link:../../packages/vite-config

  pages/content-ui:
    dependencies:
      '@extension/shared':
        specifier: workspace:*
        version: link:../../packages/shared
      '@extension/storage':
        specifier: workspace:*
        version: link:../../packages/storage
      '@extension/ui':
        specifier: workspace:*
        version: link:../../packages/ui
    devDependencies:
      '@extension/hmr':
        specifier: workspace:*
        version: link:../../packages/hmr
      '@extension/tailwindcss-config':
        specifier: workspace:*
        version: link:../../packages/tailwind-config
      '@extension/tsconfig':
        specifier: workspace:*
        version: link:../../packages/tsconfig
      '@extension/vite-config':
        specifier: workspace:*
        version: link:../../packages/vite-config
      concurrently:
        specifier: ^8.2.2
        version: 8.2.2

  pages/new-tab:
    dependencies:
      '@extension/i18n':
        specifier: workspace:*
        version: link:../../packages/i18n
      '@extension/shared':
        specifier: workspace:*
        version: link:../../packages/shared
      '@extension/storage':
        specifier: workspace:*
        version: link:../../packages/storage
      '@extension/ui':
        specifier: workspace:*
        version: link:../../packages/ui
    devDependencies:
      '@extension/tailwindcss-config':
        specifier: workspace:*
        version: link:../../packages/tailwind-config
      '@extension/tsconfig':
        specifier: workspace:*
        version: link:../../packages/tsconfig
      '@extension/vite-config':
        specifier: workspace:*
        version: link:../../packages/vite-config
      sass:
        specifier: 1.77.8
        version: 1.77.8

  pages/options:
    dependencies:
      '@extension/shared':
        specifier: workspace:*
        version: link:../../packages/shared
      '@extension/storage':
        specifier: workspace:*
        version: link:../../packages/storage
      '@extension/ui':
        specifier: workspace:*
        version: link:../../packages/ui
    devDependencies:
      '@extension/tailwindcss-config':
        specifier: workspace:*
        version: link:../../packages/tailwind-config
      '@extension/tsconfig':
        specifier: workspace:*
        version: link:../../packages/tsconfig
      '@extension/vite-config':
        specifier: workspace:*
        version: link:../../packages/vite-config

  pages/popup:
    dependencies:
      '@extension/content-runtime-script':
        specifier: workspace:*
        version: link:../content-runtime
      '@extension/shared':
        specifier: workspace:*
        version: link:../../packages/shared
      '@extension/storage':
        specifier: workspace:*
        version: link:../../packages/storage
      '@types/node':
        specifier: ^20.14.10
        version: 20.14.10
    devDependencies:
      '@extension/tailwindcss-config':
        specifier: workspace:*
        version: link:../../packages/tailwind-config
      '@extension/tsconfig':
        specifier: workspace:*
        version: link:../../packages/tsconfig
      '@extension/vite-config':
        specifier: workspace:*
        version: link:../../packages/vite-config

packages:

  '@alloc/quick-lru@5.2.0':
    resolution: {integrity: sha512-UrcABB+4bUrFABwbluTIBErXwvbsU/V7TZWfmbgJfbkwiBuziS9gxdODUyuiecfdGQ85jglMW6juS3+z5TsKLw==}
    engines: {node: '>=10'}

  '@babel/runtime@7.25.0':
    resolution: {integrity: sha512-7dRy4DwXwtzBrPbZflqxnvfxLF8kdZXPkhymtDeFoFqE6ldzjQFgYTtYIFARcLEYDrqfBfYcZt1WqFxRoyC9Rw==}
    engines: {node: '>=6.9.0'}

  '@cspotcode/source-map-support@0.8.1':
    resolution: {integrity: sha512-IchNf6dN4tHoMFIn/7OE8LWZ19Y6q/67Bmf6vnGREv8RSbBVb9LPJxEcnwrcwX6ixSvaiGoomAUvu4YSxXrVgw==}
    engines: {node: '>=12'}

  '@esbuild/aix-ppc64@0.21.5':
    resolution: {integrity: sha512-1SDgH6ZSPTlggy1yI6+Dbkiz8xzpHJEVAlF/AM1tHPLsf5STom9rwtjE4hKAF20FfXXNTFqEYXyJNWh1GiZedQ==}
    engines: {node: '>=12'}
    cpu: [ppc64]
    os: [aix]

  '@esbuild/aix-ppc64@0.23.0':
    resolution: {integrity: sha512-3sG8Zwa5fMcA9bgqB8AfWPQ+HFke6uD3h1s3RIwUNK8EG7a4buxvuFTs3j1IMs2NXAk9F30C/FF4vxRgQCcmoQ==}
    engines: {node: '>=18'}
    cpu: [ppc64]
    os: [aix]

  '@esbuild/android-arm64@0.21.5':
    resolution: {integrity: sha512-c0uX9VAUBQ7dTDCjq+wdyGLowMdtR/GoC2U5IYk/7D1H1JYC0qseD7+11iMP2mRLN9RcCMRcjC4YMclCzGwS/A==}
    engines: {node: '>=12'}
    cpu: [arm64]
    os: [android]

  '@esbuild/android-arm64@0.23.0':
    resolution: {integrity: sha512-EuHFUYkAVfU4qBdyivULuu03FhJO4IJN9PGuABGrFy4vUuzk91P2d+npxHcFdpUnfYKy0PuV+n6bKIpHOB3prQ==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [android]

  '@esbuild/android-arm@0.21.5':
    resolution: {integrity: sha512-vCPvzSjpPHEi1siZdlvAlsPxXl7WbOVUBBAowWug4rJHb68Ox8KualB+1ocNvT5fjv6wpkX6o/iEpbDrf68zcg==}
    engines: {node: '>=12'}
    cpu: [arm]
    os: [android]

  '@esbuild/android-arm@0.23.0':
    resolution: {integrity: sha512-+KuOHTKKyIKgEEqKbGTK8W7mPp+hKinbMBeEnNzjJGyFcWsfrXjSTNluJHCY1RqhxFurdD8uNXQDei7qDlR6+g==}
    engines: {node: '>=18'}
    cpu: [arm]
    os: [android]

  '@esbuild/android-x64@0.21.5':
    resolution: {integrity: sha512-D7aPRUUNHRBwHxzxRvp856rjUHRFW1SdQATKXH2hqA0kAZb1hKmi02OpYRacl0TxIGz/ZmXWlbZgjwWYaCakTA==}
    engines: {node: '>=12'}
    cpu: [x64]
    os: [android]

  '@esbuild/android-x64@0.23.0':
    resolution: {integrity: sha512-WRrmKidLoKDl56LsbBMhzTTBxrsVwTKdNbKDalbEZr0tcsBgCLbEtoNthOW6PX942YiYq8HzEnb4yWQMLQuipQ==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [android]

  '@esbuild/darwin-arm64@0.21.5':
    resolution: {integrity: sha512-DwqXqZyuk5AiWWf3UfLiRDJ5EDd49zg6O9wclZ7kUMv2WRFr4HKjXp/5t8JZ11QbQfUS6/cRCKGwYhtNAY88kQ==}
    engines: {node: '>=12'}
    cpu: [arm64]
    os: [darwin]

  '@esbuild/darwin-arm64@0.23.0':
    resolution: {integrity: sha512-YLntie/IdS31H54Ogdn+v50NuoWF5BDkEUFpiOChVa9UnKpftgwzZRrI4J132ETIi+D8n6xh9IviFV3eXdxfow==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [darwin]

  '@esbuild/darwin-x64@0.21.5':
    resolution: {integrity: sha512-se/JjF8NlmKVG4kNIuyWMV/22ZaerB+qaSi5MdrXtd6R08kvs2qCN4C09miupktDitvh8jRFflwGFBQcxZRjbw==}
    engines: {node: '>=12'}
    cpu: [x64]
    os: [darwin]

  '@esbuild/darwin-x64@0.23.0':
    resolution: {integrity: sha512-IMQ6eme4AfznElesHUPDZ+teuGwoRmVuuixu7sv92ZkdQcPbsNHzutd+rAfaBKo8YK3IrBEi9SLLKWJdEvJniQ==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [darwin]

  '@esbuild/freebsd-arm64@0.21.5':
    resolution: {integrity: sha512-5JcRxxRDUJLX8JXp/wcBCy3pENnCgBR9bN6JsY4OmhfUtIHe3ZW0mawA7+RDAcMLrMIZaf03NlQiX9DGyB8h4g==}
    engines: {node: '>=12'}
    cpu: [arm64]
    os: [freebsd]

  '@esbuild/freebsd-arm64@0.23.0':
    resolution: {integrity: sha512-0muYWCng5vqaxobq6LB3YNtevDFSAZGlgtLoAc81PjUfiFz36n4KMpwhtAd4he8ToSI3TGyuhyx5xmiWNYZFyw==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [freebsd]

  '@esbuild/freebsd-x64@0.21.5':
    resolution: {integrity: sha512-J95kNBj1zkbMXtHVH29bBriQygMXqoVQOQYA+ISs0/2l3T9/kj42ow2mpqerRBxDJnmkUDC
... [TRUNCATED]
```

### File: pnpm-workspace.yaml
```yaml
packages:
  - "chrome-extension"
  - "pages/*"
  - "packages/*"

```

### File: turbo.json
```json
{
  "$schema": "https://turbo.build/schema.json",
  "ui": "tui",
  "globalEnv": ["__FIREFOX__"],
  "tasks": {
    "ready": {
      "outputs": [
        "dist/**",
        "build/**"
      ]
    },
    "dev": {
      "dependsOn": [
        "ready"
      ],
      "outputs": [
        "dist/**",
        "build/**",
        "i18n/locales/**"
      ],
      "persistent": true
    },
    "build": {
      "dependsOn": [
        "^build",
        "ready"
      ],
      "outputs": [
        "../../dist/**",
        "dist/**",
        "build/**"
      ]
    },
    "zip": {
      "dependsOn": [
        "build"
      ],
      "cache": false
    },
    "type-check": {
      "cache": false
    },
    "lint": {
      "cache": false
    },
    "lint:fix": {
      "cache": false
    },
    "prettier": {
      "cache": false
    },
    "test": {
      "dependsOn": [
        "^test",
        "^build"
      ],
      "cache": false
    },
    "clean": {
      "cache": false
    }
  }
}

```

### File: UPDATE-PACKAGE-VERSIONS.md
```md
For update package version in all ```package.json``` files use this command in root:

FOR WINDOWS YOU NEED TO USE E.G ```GIT BASH``` CONSOLE OR OTHER WHICH SUPPORT UNIX COMMANDS
```bash
pnpm update-version <new_version>
```

If script was run successfully you will see ```Updated versions to <new_version>```

```

### File: update_version.sh
```sh
#!/bin/bash
# Usage: ./update_version.sh <new_version>
# FORMAT IS <0.0.0>

if [[ "$1" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  find . -name 'package.json' -not -path '*/node_modules/*' -exec bash -c '
    # Parse the version from package.json
    current_version=$(grep -o "\"version\": \"[^\"]*" "$0" | cut -d"\"" -f4)

    # Update the version
    perl -i -pe"s/$current_version/'$1'/" "$0"
  '  {} \;

  echo "Updated versions to $1";
else
  echo "Version format <$1> isn't correct, proper format is <0.0.0>";
fi

```

### File: .github\pull_request_template.md
```md
<!-- Describe what this PR is for in the title. -->

> `*` Please fill in the required items.

## Priority*

- [ ] High: This PR needs to be merged first for other tasks.
- [x] Middle: This PR should be merged quickly to prevent conflicts due to common changes. (default)
- [ ] Low: This PR does not affect other tasks, so it can be merged later.

## Purpose of the PR*
<!-- Describe the purpose of the PR. -->

## Changes*


## How to check the feature
<!-- Describe how to check the feature in detail -->
<!-- If there are any changes to the screen, please attach a screenshot for easy identification. -->


## Reference
<!-- Any helpful information for understanding the PR. -->

```

### File: .github\ISSUE_TEMPLATE\bug_report.md
```md
---
name: Bug report
about: Create a report to help us improve
title: ''
labels: bug
assignees: dunkbing

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Desktop (please complete the following information):**
 - OS: [e.g. Mac, Window, Linux]
 - Browser [e.g. chrome, firefox]
 - Node Version [e.g. 18.12.0]

**Additional context**
Add any other context about the problem here.

```

### File: .github\ISSUE_TEMPLATE\feature_request.md
```md
---
name: Feature request
about: Suggest an idea for this project
title: ''
labels: enhancement
assignees: dunkbing

---

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request here.

```

### File: packages\i18n\index.ts
```ts
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
import { t as t_dev_or_prod } from './lib/i18n';
import type { t as t_dev } from './lib/i18n-dev';

export const t = t_dev_or_prod as unknown as typeof t_dev;

```

### File: packages\i18n\tsconfig.json
```json
{
  "extends": "@extension/tsconfig/utils",
  "compilerOptions": {
    "outDir": "dist",
    "baseUrl": ".",
    "types": ["chrome"]
  },
  "include": ["index.ts", "lib", "locales"]
}

```

### File: packages\shared\index.ts
```ts
export * from './lib/hooks';
export * from './lib/hoc';

```

### File: packages\shared\tsconfig.json
```json
{
  "extends": "@extension/tsconfig/utils",
  "compilerOptions": {
    "outDir": "dist",
    "jsx": "react-jsx",
    "baseUrl": ".",
    "types": ["chrome"]
  },
  "include": ["index.ts", "lib"]
}

```

### File: packages\storage\index.ts
```ts
export * from './lib';

```

### File: packages\storage\tsconfig.json
```json
{
  "extends": "@extension/tsconfig/utils",
  "compilerOptions": {
    "outDir": "dist",
    "jsx": "react-jsx",
    "baseUrl": ".",
    "types": ["chrome"]
  },
  "include": ["index.ts", "lib"]
}

```

### File: packages\ui\index.ts
```ts
export * from './lib/components';
export * from './lib/utils';
export * from './lib/withUI';

```

### File: packages\ui\tailwind.config.ts
```ts
import type { Config } from 'tailwindcss';

const config: Config = {
  content: [],
};
export default config;

```

### File: packages\ui\tsconfig.json
```json
{
  "extends": "@extension/tsconfig/utils",
  "compilerOptions": {
    "outDir": "dist",
    "jsx": "react-jsx",
    "baseUrl": ".",
    "types": ["chrome"]
  },
  "include": ["index.ts", "lib"]
}

```

### File: pages\content\tsconfig.json
```json
{
  "extends": "@extension/tsconfig/base",
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@lib/*": ["lib/*"]
    },
    "types": ["chrome"]
  },
  "include": ["lib"]
}

```

### File: packages\i18n\lib\getMessageFromLocale.ts
```ts
/**
 * This file is generated by generate-i18n.mjs
 * Do not edit this file directly
 */
import enMessage from '../locales/en/messages.json';

export function getMessageFromLocale(locale: string) {
  switch (locale) {
    case 'en':
      return enMessage;
    default:
      throw new Error('Unsupported locale');
  }
}

export const defaultLocale = (() => {
  const locales = ['en'];
  const firstLocale = locales[0];
  const defaultLocale = Intl.DateTimeFormat().resolvedOptions().locale.replace('-', '_');
  if (locales.includes(defaultLocale)) {
    return defaultLocale;
  }
  const defaultLocaleWithoutRegion = defaultLocale.split('_')[0];
  if (locales.includes(defaultLocaleWithoutRegion)) {
    return defaultLocaleWithoutRegion;
  }
  return firstLocale;
})();

```

### File: packages\i18n\lib\i18n-dev.ts
```ts
import type { DevLocale, MessageKey } from './type';
import { defaultLocale, getMessageFromLocale } from './getMessageFromLocale';

type I18nValue = {
  message: string;
  placeholders?: Record<string, { content?: string; example?: string }>;
};

function translate(key: MessageKey, substitutions?: string | string[]) {
  const value = getMessageFromLocale(t.devLocale)[key] as I18nValue;
  let message = value.message;
  /**
   * This is a placeholder replacement logic. But it's not perfect.
   * It just imitates the behavior of the Chrome extension i18n API.
   * Please check the official document for more information And double-check the behavior on production build.
   *
   * @url https://developer.chrome.com/docs/extensions/how-to/ui/localization-message-formats#placeholders
   */
  if (value.placeholders) {
    Object.entries(value.placeholders).forEach(([key, { content }]) => {
      if (!content) {
        return;
      }
      message = message.replace(new RegExp(`\\$${key}\\$`, 'gi'), content);
    });
  }
  if (!substitutions) {
    return message;
  }
  if (Array.isArray(substitutions)) {
    return substitutions.reduce((acc, cur, idx) => acc.replace(`$${idx + 1}`, cur), message);
  }
  return message.replace(/\$(\d+)/, substitutions);
}

function removePlaceholder(message: string) {
  return message.replace(/\$\d+/g, '');
}

export const t = (...args: Parameters<typeof translate>) => {
  return removePlaceholder(translate(...args));
};

t.devLocale = defaultLocale as DevLocale;

```

### File: packages\i18n\lib\i18n-prod.ts
```ts
import type { DevLocale, MessageKey } from './type';

export function t(key: MessageKey, substitutions?: string | string[]) {
  return chrome.i18n.getMessage(key, substitutions);
}

t.devLocale = '' as DevLocale; // for type consistency with i18n-dev.ts

```

### File: packages\i18n\lib\type.ts
```ts
/**
 * This file is generated by generate-i18n.mjs
 * Do not edit this file directly
 */
import type enMessage from '../locales/en/messages.json';

export type MessageKey = keyof typeof enMessage;

export type DevLocale = 'en';

```

### File: packages\shared\lib\constants.ts
```ts
import type { Suggestion } from './types';

export const commands = {
  getSuggestions: 'GET_SUGGESTIONS',
  switchTab: 'SWITCH_TAB',
  newTab: 'NEW_TAB',
  clearHistory: 'CLEAR_HISTORY',
  clearCache: 'CLEAR_CACHE',
  clearCookies: 'CLEAR_COOKIES',
  clearLocalStorage: 'CLEAR_LOCAL_STORAGE',
  bookmarkCurrentTab: 'BOOKMARK_CURRENT_TAB',
  removeBookmark: 'REMOVE_BOOKMARK',
  pinCurrentTab: 'PIN_CURRENT_TAB',
  muteCurrentTab: 'MUTE_CURRENT_TAB',
  reloadCurrentTab: 'RELOAD_CURRENT_TAB',
  fullscreenCurrentTab: 'FULLSCREEN_CURRENT_TAB',
  printCurrentTab: 'PRINT_CURRENT_TAB',
  closeCurrentTab: 'CLOSE_CURRENT_TAB',
  duplicateCurrentTab: 'DUPLICATE_CURRENT_TAB',
  openIncognitoWindow: 'OPEN_INCOGNITO_WINDOW',
  clearOtherTabs: 'CLEAR_OTHER_TABS',
};

const isMac = navigator.platform.toUpperCase().indexOf('MAC') >= 0;

export const actions: Suggestion[] = [
  {
    content: commands.bookmarkCurrentTab,
    description: 'Bookmark current tab',
    type: 'action',
    iconUrl: 'Bookmark',
    action: () => chrome.runtime.sendMessage({ type: commands.bookmarkCurrentTab }),
    shortcut: isMac ? '⌘D' : 'Ctrl+D',
  },
  {
    content: commands.removeBookmark,
    description: 'Remove bookmark for current tab',
    type: 'action',
    iconUrl: 'RemoveBookmark',
    action: () => chrome.runtime.sendMessage({ type: commands.removeBookmark }),
  },
  {
    content: commands.pinCurrentTab,
    description: 'Pin/Unpin current tab',
    type: 'action',
    iconUrl: 'Pin',
    action: () => chrome.runtime.sendMessage({ type: commands.pinCurrentTab }),
  },
  {
    content: commands.muteCurrentTab,
    description: 'Mute/Unmute current tab',
    type: 'action',
    iconUrl: 'Mute',
    action: () => chrome.runtime.sendMessage({ type: commands.muteCurrentTab }),
    shortcut: isMac ? '⌥⌘M' : 'Alt+Shift+M',
  },
  {
    content: commands.reloadCurrentTab,
    description: 'Reload current tab',
    type: 'action',
    iconUrl: 'Reload',
    action: () => chrome.runtime.sendMessage({ type: commands.reloadCurrentTab }),
    shortcut: isMac ? '⌘R' : 'Ctrl+R',
  },
  {
    content: commands.fullscreenCurrentTab,
    description: 'Toggle fullscreen for current tab',
    type: 'action',
    iconUrl: 'Fullscreen',
    action: () => chrome.runtime.sendMessage({ type: commands.fullscreenCurrentTab }),
    shortcut: 'F11',
  },
  {
    content: commands.printCurrentTab,
    description: 'Print current tab',
    type: 'action',
    iconUrl: 'Print',
    action: () => chrome.runtime.sendMessage({ type: commands.printCurrentTab }),
    shortcut: isMac ? '⌘P' : 'Ctrl+P',
  },
  {
    content: commands.closeCurrentTab,
    description: 'Close current tab',
    type: 'action',
    iconUrl: 'Close',
    action: () => chrome.runtime.sendMessage({ type: commands.closeCurrentTab }),
    shortcut: isMac ? '⌘W' : 'Ctrl+W',
  },
  {
    content: commands.duplicateCurrentTab,
    description: 'Duplicate current tab',
    type: 'action',
    iconUrl: 'Duplicate',
    action: () => chrome.runtime.sendMessage({ type: commands.duplicateCurrentTab }),
  },
  {
    content: commands.clearOtherTabs,
    description: 'Close all tabs except the current one',
    type: 'action',
    iconUrl: 'CloseOthers',
    action: () => chrome.runtime.sendMessage({ type: commands.clearOtherTabs }),
  },
  {
    content: commands.openIncognitoWindow,
    description: 'Open new incognito window',
    type: 'action',
    iconUrl: 'Incognito',
    action: () => chrome.runtime.sendMessage({ type: commands.openIncognitoWindow }),
    shortcut: isMac ? '⌘⇧N' : 'Ctrl+Shift+N',
  },
  {
    content: commands.clearCache,
    description: 'Clear browser cache',
    type: 'action',
    iconUrl: 'Cache',
    action: () => chrome.runtime.sendMessage({ type: commands.clearCache }),
  },
  {
    content: commands.clearHistory,
    description: 'Clear browsing history',
    type: 'action',
    iconUrl: 'History',
    action: () => chrome.runtime.sendMessage({ type: commands.clearHistory }),
  },
  {
    content: commands.clearCookies,
    description: 'Clear cookies',
    type: 'action',
    iconUrl: 'Cookies',
    action: () => chrome.runtime.sendMessage({ type: commands.clearCookies }),
  },
  {
    content: commands.clearLocalStorage,
    description: 'Clear local storage',
    type: 'action',
    iconUrl: 'LocalStorage',
    action: () => chrome.runtime.sendMessage({ type: commands.clearLocalStorage }),
  },
  {
    content: 'https://docs.new',
    description: 'Create a new Google Docs document',
    type: 'action',
    iconUrl: chrome.runtime.getURL('/assets/docs.png'),
  },
  {
    content: 'https://slides.new',
    description: 'Create a new Google Slides presentation',
    type: 'action',
    iconUrl: chrome.runtime.getURL('/assets/slides.png'),
  },
  {
    content: 'https://sheets.new',
    description: 'Create a new Google Sheets spreadsheet',
    type: 'action',
    iconUrl: chrome.runtime.getURL('/assets/sheets.png'),
  },
  {
    content: 'https://meet.new',
    description: 'Start a new Google Meet',
    type: 'action',
    iconUrl: chrome.runtime.getURL('/assets/meet.png'),
  },
  {
    content: 'https://www.notion.so/new',
    description: 'Create a new Notion page',
    type: 'action',
    iconUrl: chrome.runtime.getURL('/assets/notion.png'),
  },
  {
    content: 'https://github.com/new',
    description: 'Create a new GitHub repository',
    type: 'action',
    iconUrl: chrome.runtime.getURL('/assets/github.svg'),
  },
  {
    content: 'https://text2audio.cc',
    description: 'Text to Speech',
    type: 'action',
    iconUrl: chrome.runtime.getURL('/assets/text2audio.ico'),
  },
  {
    content: 'https://trello.com/create-board',
    description: 'Create new Trello board',
    type: 'action',
    iconUrl: chrome.runtime.getURL('/assets/trello.png'),
  },
  {
    content: 'https://figma.new',
    description: 'Create a new Figma design file',
    type: 'action',
    iconUrl: chrome.runtime.getURL('/assets/figma.png'),
  },
  {
    content: 'https://codepen.io/pen/',
    description: 'Create a new CodePen',
    type: 'action',
    iconUrl: chrome.runtime.getURL('/assets/codepen.ico'),
  },
];

```

### File: packages\shared\lib\types.ts
```ts
export type Suggestion = {
  content: string;
  description: string;
  type?: 'history' | 'bookmark' | 'tab' | 'search' | 'action' | 'website' | 'recently-closed';
  iconUrl?: string;
  tabId?: number;
  action?: () => void;
  shortcut?: string;
};

```

### File: packages\storage\lib\base.ts
```ts
import type { BaseStorage, StorageConfig, ValueOrUpdate } from './types';
import { SessionAccessLevelEnum, StorageEnum } from './enums';

/**
 * Chrome reference error while running `processTailwindFeatures` in tailwindcss.
 *  To avoid this, we need to check if the globalThis.chrome is available and add fallback logic.
 */
const chrome = globalThis.chrome;

/**
 * Sets or updates an arbitrary cache with a new value or the result of an update function.
 */
async function updateCache<D>(valueOrUpdate: ValueOrUpdate<D>, cache: D | null): Promise<D> {
  // Type guard to check if our value or update is a function
  function isFunction<D>(value: ValueOrUpdate<D>): value is (prev: D) => D | Promise<D> {
    return typeof value === 'function';
  }

  // Type guard to check in case of a function, if its a Promise
  function returnsPromise<D>(func: (prev: D) => D | Promise<D>): func is (prev: D) => Promise<D> {
    // Use ReturnType to infer the return type of the function and check if it's a Promise
    return (func as (prev: D) => Promise<D>) instanceof Promise;
  }

  if (isFunction(valueOrUpdate)) {
    // Check if the function returns a Promise
    if (returnsPromise(valueOrUpdate)) {
      return valueOrUpdate(cache as D);
    } else {
      return valueOrUpdate(cache as D);
    }
  } else {
    return valueOrUpdate;
  }
}

/**
 * If one session storage needs access from content scripts, we need to enable it globally.
 * @default false
 */
let globalSessionAccessLevelFlag: StorageConfig['sessionAccessForContentScripts'] = false;

/**
 * Checks if the storage permission is granted in the manifest.json.
 */
function checkStoragePermission(storageEnum: StorageEnum): void {
  if (!chrome) {
    return;
  }

  if (chrome.storage[storageEnum] === undefined) {
    throw new Error(`Check your storage permission in manifest.json: ${storageEnum} is not defined`);
  }
}

/**
 * Creates a storage area for persisting and exchanging data.
 */
export function createStorage<D = string>(key: string, fallback: D, config?: StorageConfig<D>): BaseStorage<D> {
  let cache: D | null = null;
  let listeners: Array<() => void> = [];

  const storageEnum = config?.storageEnum ?? StorageEnum.Local;
  const liveUpdate = config?.liveUpdate ?? false;

  const serialize = config?.serialization?.serialize ?? ((v: D) => v);
  const deserialize = config?.serialization?.deserialize ?? (v => v as D);

  // Set global session storage access level for StoryType.Session, only when not already done but needed.
  if (
    globalSessionAccessLevelFlag === false &&
    storageEnum === StorageEnum.Session &&
    config?.sessionAccessForContentScripts === true
  ) {
    checkStoragePermission(storageEnum);
    chrome?.storage[storageEnum]
      .setAccessLevel({
        accessLevel: SessionAccessLevelEnum.ExtensionPagesAndContentScripts,
      })
      .catch(error => {
        console.warn(error);
        console.warn('Please call setAccessLevel into different context, like a background script.');
      });
    globalSessionAccessLevelFlag = true;
  }

  // Register life cycle methods
  const get = async (): Promise<D> => {
    checkStoragePermission(storageEnum);
    const value = await chrome?.storage[storageEnum].get([key]);

    if (!value) {
      return fallback;
    }

    return deserialize(value[key]) ?? fallback;
  };

  const _emitChange = () => {
    listeners.forEach(listener => listener());
  };

  const set = async (valueOrUpdate: ValueOrUpdate<D>) => {
    cache = await updateCache(valueOrUpdate, cache);

    await chrome?.storage[storageEnum].set({ [key]: serialize(cache) });
    _emitChange();
  };

  const subscribe = (listener: () => void) => {
    listeners = [...listeners, listener];

    return () => {
      listeners = listeners.filter(l => l !== listener);
    };
  };

  const getSnapshot = () => {
    return cache;
  };

  get().then(data => {
    cache = data;
    _emitChange();
  });

  // Listener for live updates from the browser
  async function _updateFromStorageOnChanged(changes: { [key: string]: chrome.storage.StorageChange }) {
    // Check if the key we are listening for is in the changes object
    if (changes[key] === undefined) return;

    const valueOrUpdate: ValueOrUpdate<D> = deserialize(changes[key].newValue);

    if (cache === valueOrUpdate) return;

    cache = await updateCache(valueOrUpdate, cache);

    _emitChange();
  }

  // Register listener for live updates for our storage area
  if (liveUpdate) {
    chrome?.storage[storageEnum].onChanged.addListener(_updateFromStorageOnChanged);
  }

  return {
    get,
    set,
    getSnapshot,
    subscribe,
  };
}

```

### File: packages\storage\lib\enums.ts
```ts
/**
 * Storage area type for persisting and exchanging data.
 * @see https://developer.chrome.com/docs/extensions/reference/storage/#overview
 */
export enum StorageEnum {
  /**
   * Persist data locally against browser restarts. Will be deleted by uninstalling the extension.
   * @default
   */
  Local = 'local',
  /**
   * Uploads data to the users account in the cloud and syncs to the users browsers on other devices. Limits apply.
   */
  Sync = 'sync',
  /**
   * Requires an [enterprise policy](https://www.chromium.org/administrators/configuring-policy-for-extensions) with a
   * json schema for company wide config.
   */
  Managed = 'managed',
  /**
   * Only persist data until the browser is closed. Recommended for service workers which can shutdown anytime and
   * therefore need to restore their state. Set {@link SessionAccessLevelEnum} for permitting content scripts access.
   * @implements Chromes [Session Storage](https://developer.chrome.com/docs/extensions/reference/storage/#property-session)
   */
  Session = 'session',
}

/**
 * Global access level requirement for the {@link StorageEnum.Session} Storage Area.
 * @implements Chromes [Session Access Level](https://developer.chrome.com/docs/extensions/reference/storage/#method-StorageArea-setAccessLevel)
 */
export enum SessionAccessLevelEnum {
  /**
   * Storage can only be accessed by Extension pages (not Content scripts).
   * @default
   */
  ExtensionPagesOnly = 'TRUSTED_CONTEXTS',
  /**
   * Storage can be accessed by both Extension pages and Content scripts.
   */
  ExtensionPagesAndContentScripts = 'TRUSTED_AND_UNTRUSTED_CONTEXTS',
}

```

### File: packages\storage\lib\exampleThemeStorage.ts
```ts
import { createStorage } from './base';
import { StorageEnum } from './enums';
import type { Theme, ThemeStorage } from './types';

const storage = createStorage<Theme>('theme-storage-key', 'light', {
  storageEnum: StorageEnum.Local,
  liveUpdate: true,
});

// You can extend it with your own methods
export const exampleThemeStorage: ThemeStorage = {
  ...storage,
  toggle: async () => {
    await storage.set(currentTheme => {
      return currentTheme === 'light' ? 'dark' : 'light';
    });
  },
};

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

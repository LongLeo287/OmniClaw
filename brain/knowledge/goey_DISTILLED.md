---
id: goey
type: knowledge
owner: OA_Triage
---
# goey
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "goey-toast",
  "version": "0.4.0",
  "description": "A gooey, morphing toast component built on Sonner with Framer Motion animations",
  "type": "module",
  "main": "./dist/index.cjs",
  "module": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js",
      "require": "./dist/index.cjs"
    },
    "./styles.css": "./dist/index.css"
  },
  "sideEffects": [
    "*.css"
  ],
  "files": [
    "dist"
  ],
  "scripts": {
    "build": "tsup",
    "dev": "tsup --watch",
    "test": "vitest run",
    "test:watch": "vitest",
    "typecheck": "tsc --noEmit"
  },
  "peerDependencies": {
    "framer-motion": ">=10.0.0",
    "react": ">=18.0.0",
    "react-dom": ">=18.0.0"
  },
  "dependencies": {
    "sonner": "^2.0.7"
  },
  "devDependencies": {
    "@testing-library/jest-dom": "^6.9.1",
    "@testing-library/react": "^16.3.2",
    "@types/node": "^25.2.3",
    "@types/react": "^19.2.14",
    "@types/react-dom": "^19.2.3",
    "@vitejs/plugin-react": "^5.1.4",
    "framer-motion": "^12.34.0",
    "jsdom": "^28.0.0",
    "react": "^19.2.4",
    "react-dom": "^19.2.4",
    "tsup": "^8.5.1",
    "typescript": "^5.9.3",
    "vitest": "^4.0.18"
  },
  "keywords": [
    "toast",
    "notification",
    "sonner",
    "framer-motion",
    "animation",
    "morph"
  ],
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/anl331/goey-toast"
  },
  "homepage": "https://goey-toast.vercel.app",
  "bugs": {
    "url": "https://github.com/anl331/goey-toast/issues"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}

```

### File: README.md
```md
# gooey-toast

[![gooey-toast](https://goey-toast.vercel.app/og-image.png)](https://goey-toast.vercel.app)

**[Live Demo & Docs](https://goey-toast.vercel.app)**

## Features

- Organic blob morph animation (pill &rarr; blob &rarr; pill)
- Five toast types: default, success, error, warning, info
- Promise toasts with loading &rarr; success/error transitions
- Action buttons with optional success label morph-back
- Description body supporting strings and React components
- Configurable display duration and bounce intensity
- Custom fill color, border color, and border width
- CSS class overrides via `classNames` prop
- 6 positions with automatic horizontal mirroring for right-side positions
- Center positions with symmetric morph animation
- Hover pause: hovering an expanded toast pauses the dismiss timer
- Hover re-expand: hovering a collapsed pill re-expands the toast
- Pre-dismiss collapse animation
- In-place toast updates via `gooeyToast.update()`
- Dismiss by type filter: `gooeyToast.dismiss({ type: 'error' })`
- Dark mode and RTL layout support
- Animation presets: smooth, bouncy, subtle, snappy
- Timestamp display on expanded toasts with optional `showTimestamp` toggle
- Close button with configurable position (`top-left` / `top-right`)
- Countdown progress bar with hover-pause and re-expand
- Keyboard dismiss (Escape) and swipe-to-dismiss on mobile
- Toast queue with configurable overflow strategy
- Dismiss callbacks: `onDismiss` and `onAutoClose`

## Installation

```bash
npm install goey-toast
```

### shadcn/ui

```bash
npx shadcn@latest add https://goey-toast.vercel.app/r/goey-toaster.json
```

This installs a thin wrapper component at `components/ui/goey-toaster.tsx` and auto-installs the `goey-toast` and `framer-motion` packages.

### Peer Dependencies

goey-toast requires the following peer dependencies:

```bash
npm install react react-dom framer-motion
```

| Package        | Version    |
| -------------- | ---------- |
| react          | >= 18.0.0  |
| react-dom      | >= 18.0.0  |
| framer-motion  | >= 10.0.0  |

### CSS Import (Required)

You **must** import the goey-toast stylesheet for the component to render correctly:

```tsx
import 'goey-toast/styles.css'
```

Add this import once in your app's entry point (e.g., `main.tsx` or `App.tsx`). Without it, toasts will appear unstyled.

## Quick Start

```tsx
import { GooeyToaster, gooeyToast } from 'goey-toast'
import 'goey-toast/styles.css'

function App() {
  return (
    <>
      <GooeyToaster position="bottom-right" />
      <button onClick={() => gooeyToast.success('Saved!')}>
        Save
      </button>
    </>
  )
}
```

## API Reference

### `gooeyToast` Methods

```ts
gooeyToast(title, options?)              // default (neutral)
gooeyToast.success(title, options?)      // green
gooeyToast.error(title, options?)        // red
gooeyToast.warning(title, options?)      // yellow
gooeyToast.info(title, options?)         // blue
gooeyToast.promise(promise, data)        // loading -> success/error
gooeyToast.update(id, options)           // update an existing toast in-place
gooeyToast.dismiss(idOrFilter?)          // dismiss one, by type, or all toasts
```

#### `gooeyToast.update(id, options)`

Updates an existing toast in-place without removing and re-creating it.

```tsx
const id = gooeyToast('Uploading...', {
  icon: <SpinnerIcon />,
})

// Later, update the toast
gooeyToast.update(id, {
  title: 'Upload complete',
  type: 'success',
  description: '3 files uploaded.',
  icon: null, // clears the custom icon
})
```

**`GooeyToastUpdateOptions`:**

| Option        | Type              | Description                   |
| ------------- | ----------------- | ----------------------------- |
| `title`       | `string`          | New title text                |
| `description` | `ReactNode`       | New body content              |
| `type`        | `GooeyToastType`   | Change the toast type/color   |
| `action`      | `GooeyToastAction` | New action button             |
| `icon`        | `ReactNode \| null` | Custom icon (pass `null` to clear) |

#### `gooeyToast.dismiss(idOrFilter?)`

Dismiss a single toast by ID, all toasts of a given type, or all toasts at once.

```ts
// Dismiss a specific toast
gooeyToast.dismiss(toastId)

// Dismiss all error toasts
gooeyToast.dismiss({ type: 'error' })

// Dismiss multiple types
gooeyToast.dismiss({ type: ['error', 'warning'] })

// Dismiss all toasts
gooeyToast.dismiss()
```

### `GooeyToastOptions`

Options passed as the second argument to `gooeyToast()` and type-specific methods.

| Option        | Type                 | Description                        |
| ------------- | -------------------- | ---------------------------------- |
| `description` | `ReactNode`          | Body content (string or component) |
| `action`      | `GooeyToastAction`    | Action button configuration        |
| `icon`        | `ReactNode`          | Custom icon override               |
| `duration`    | `number`             | Display duration in ms             |
| `id`          | `string \| number`   | Unique toast identifier            |
| `classNames`  | `GooeyToastClassNames`| CSS class overrides                |
| `fillColor`   | `string`             | Background color of the blob       |
| `borderColor` | `string`             | Border color of the blob           |
| `borderWidth` | `number`             | Border width in px (default 1.5)   |
| `timing`      | `GooeyToastTimings`   | Animation timing overrides         |
| `spring`      | `boolean`            | Enable spring/bounce animations (default `true`) |
| `bounce`      | `number`             | Spring intensity from `0.05` (subtle) to `0.8` (dramatic), default `0.4` |
| `showTimestamp` | `boolean`         | Show/hide timestamp in toast header/body (default `true`) |
| `showProgress`| `boolean`            | Show countdown progress bar                      |
| `onDismiss`   | `(id) => void`       | Called when toast is dismissed (any reason)       |
| `onAutoClose` | `(id) => void`       | Called only on timer-based auto-dismiss           |
| `preset`      | `AnimationPresetName`| Animation preset (`'smooth'`, `'bouncy'`, `'subtle'`, `'snappy'`) |

### `GooeyToastAction`

| Property       | Type       | Required | Description                                  |
| -------------- | ---------- | -------- | -------------------------------------------- |
| `label`        | `string`   | Yes      | Button text                                  |
| `onClick`      | `() => void` | Yes   | Click handler                                |
| `successLabel` | `string`   | No       | Label shown after click (morphs back to pill)|

### `GooeyToastTimings`

Fine-tune animation speeds per toast.

| Property           | Type     | Default | Description                          |
| ------------------ | -------- | ------- | ------------------------------------ |
| `displayDuration`  | `number` | 4000    | Milliseconds toast stays expanded    |

### `GooeyToastClassNames`

Override styles for any part of the toast.

| Key             | Target           |
| --------------- | ---------------- |
| `wrapper`       | Outer container  |
| `content`       | Content area     |
| `header`        | Icon + title row |
| `title`         | Title text       |
| `icon`          | Icon wrapper     |
| `description`   | Body text        |
| `actionWrapper` | Button container |
| `actionButton`  | Action button    |

### `GooeyToasterProps`

Props for the `<GooeyToaster />` component.

| Prop         | Type                                  | Default          | Description                                   |
| ------------ | ------------------------------------- | ---------------- | --------------------------------------------- |
| `position`   | `'top-left' \| 'top-center' \| 'top-right' \| 'bottom-left' \| 'bottom-center' \| 'bottom-right'` | `'bottom-right'` | Toast position |
| `duration`   | `number`                              | --               | Default display duration in ms                |
| `gap`        | `number`                              | `14`             | Gap between stacked toasts (px)               |
| `offset`     | `number \| string`                    | `'24px'`         | Distance from screen edge                     |
| `theme`      | `'light' \| 'dark'`                   | `'light'`        | Color theme                                   |
| `toastOptions` | `Partial<ExternalToast>`            | --               | Default options passed to Sonner              |
| `spring`     | `boolean`                             | `true`           | Enable spring/bounce animations globally      |
| `bounce`     | `number`                              | `0.4`            | Spring intensity: `0.05` (subtle) to `0.8` (dramatic) |
| `preset`     | `AnimationPresetName`                 | --               | Animation preset for all toasts               |
| `closeOnEscape` | `boolean`                          | `true`           | Dismiss most recent toast on Escape key       |
| `closeButton`  | `boolean \| 'top-left' \| 'top-right'` | `false`       | Show close button on hover                    |
| `showProgress` | `boolean`                           | `false`          | Show countdown progress bar on all toasts     |
| `maxQueue`   | `number`                              | `Infinity`       | Maximum queued toasts                         |
| `queueOverflow` | `'drop-oldest' \| 'drop-newest'`   | `'drop-oldest'`  | Queue overflow strategy                       |
| `dir`        | `'ltr' \| 'rtl'`                     | `'ltr'`          | Layout direction                              |
| `swipeToDismiss` | `boolean`                         | `true`           | Enable swipe-to-dismiss on mobile             |

### `GooeyPromiseData<T>`

Configuration for `gooeyToast.promise()`.

| Property      | Type                                          | Required | Description                                    |
| ------------- | --------------------------------------------- | -------- | ---------------------------------------------- |
| `loading`     | `string`                                      | Yes      | Title shown during loading                     |
| `success`     | `string \| ((data: T) => string)`             | Yes      | Title on success (static or derived from result)|
| `error`       | `string \| ((error: unknown) => string)`      | Yes      | Title on error (static or derived from error)  |
| `description` | `object`                                      | No       | Per-phase descriptions (see below)             |
| `action`      | `object`                                      | No       | Per-phase action buttons (see below)           |
| `classNames`  | `GooeyToastClassNames`                         | No       | CSS class overrides                            |
| `fillColor`   | `string`                                      | No       | Background color of the blob                   |
| `borderColor` | `string`                                      | No       | Border color of the blob                       |
| `borderWidth` | `number`                                      | No       | Border width in px                             |
| `timing`      | `GooeyToastTimings`                            | No       | Animation timing overrides                     |
| `spring`      | `boolean`                                     | No       | Enable spring/bounce animations (default `true`) |
| `bounce`      | `number`                                      | No       | Spring intensity: `0.05` (subtle) to `0.8` (dramatic), default `0.4` |
| `onDismiss`   | `(id: string \| number) => void`              | No       | Called when toast is dismissed (any reason)       |
| `onAutoClose` | `(id: string \| number) => void`              | No       | Called only on timer-based auto-dismiss           |

**`description` sub-fields:**

| Key       | Type                                             |
| --------- | ------------------------------------------------ |
| `loading` | `ReactNode`                                      |
| `success` | `ReactNode \| ((data: T) => ReactNode)`          |
| `error`   | `ReactNode \| ((error: unknown) => ReactNode)`   |

**`action` sub-fields:**

| Key       | Type              |
| --------- | ----------------- |
| `success` | `GooeyToastAction` |
| `error`   | `GooeyToastAction` |

## Usage Examples

### Description

```tsx
gooeyToast.error('Payment failed', {
  description: 'Your card was declined. Please try again.',
})
```

### Custom React Component as Description

```tsx
gooeyToast.success('Deployment complete', {
  description: (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
      <div>
        <span>Environment:</span> <strong>Production</strong>
      </div>
      <div>
        <span>Branch:</span> <strong>main @ 3f8a2c1</strong>
      </div>
    </div>
  ),
})
```

### Action Button with Success Label

```tsx
gooeyToast.info('Share link ready', {
  description: 'Your link has been generated.',
  action: {
    label: 'Copy to Clipboard',
    onClick: () => navigator.clipboard.writeText(url),
    successLabel: 'Copied!',
  },
})
```

### Promise Toast

```tsx
gooeyToast.promise(saveData(), {
  loading: 'Saving...',
  success: 'Changes saved',
  error: 'Something went wrong',
  description: {
    success: 'All changes have been synced.',
    error: 'Please try again later.',
  },
  action: {
    error: {
      label: 'Retry',
      onClick: () => retry(),
    },
  },
})
```

### Custom Styling

```tsx
gooeyToast.success('Styled!', {
  fillColor: '#1a1a2e',
  borderColor: '#333',
  borderWidth: 2,
  classNames: {
    wrapper: 'my-wrapper',
    title: 'my-title',
    description: 'my-desc',
    actionButton: 'my-btn',
  },
})
```

### Display Duration

```tsx
gooeyToast.success('Saved', {
  description: 'Your changes have been synced.',
  timing: { displayDuration: 5000 },
})
```

### Disabling Spring Animations

Disable bounce/spring animations for a cleaner, more subtle look:

```tsx
// Per-toast: disable spring for this toast only
gooeyToast.success('Saved', {
  description: 'Your changes have been synced.',
  spring: false,
})

// Globally: disable spring for all toasts
<GooeyToaster spring={false} />
```

When `spring` is `false`, all spring-based animations (landing squish, blob squish, morph transitions, pill resize, header squish) use smooth ease-in-out curves instead. Error shake animations still work regardless of this setting.

### Bounce Intensity

Control how dramatic the spring effect feels with a single `bounce` value:

```tsx
// Subtle, barely-there spring
gooeyToast.success('Saved', { bounce: 0.1 })

// Default feel
gooeyToast.success('Saved', { bounce: 0.4 })

// Jelly mode
gooeyToast.success('Saved', { bounce: 0.8 })

// Set globally via GooeyToaster
<GooeyToaster bounce={0.6} />
```

The `bounce` value (0.05 to 0.8) controls spring stiffnes
... [TRUNCATED]
```

### File: CHANGELOG.md
```md
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4.0] - 2026-03-29

### Added

- Close button with configurable position (`top-left` / `top-right`) via `closeButton` prop on `GooeyToaster`
- Close button inherits toast border/fill styling; uses shadow when no border is set
- Close button visible on hover, touch, and keyboard focus with scale animation
- Dark mode support for close button with light glow shadow
- Optional `showTimestamp` prop to show/hide timestamp on individual toasts (default `true`)
- Backward-compatible export aliases for v0.2.x users (`GoeyToaster`, `goeyToast`, etc.)

### Fixed

- ESM export broken in v0.3.0 — rebuilt exports to reference correct renamed variables
- Center toast positioning on mobile viewports (≤600px)
- Toast header stretching full width due to `display: flex` regression — restored `inline-flex`
- Swipe-to-dismiss now works for compact (no-description) toasts — `toastId` always passed
- Close button position correctly mirrors for right-side and center toast positions

## [0.1.0] - 2026-02

### Added

- Organic blob morph animation (pill to blob and back)
- Five toast types: default, success, error, warning, info
- Description body with string or ReactNode support
- Timestamp display on toast UI with optional `showTimestamp` toggle

- Action button with optional success label morph-back
- Promise toasts with loading to success/error transitions
- Configurable timing: expand delay, morph duration, collapse, display
- Position support: top-left, top-right, bottom-left, bottom-right
- Right-side positions auto-mirror the blob horizontally
- Pre-dismiss collapse animation (blob shrinks to pill before exit)
- Custom fill color, border color, and border width
- CSS class overrides via classNames prop
- Built on Sonner and Framer Motion

```

### File: package-lock.json
```json
{
  "name": "goey-toast",
  "version": "0.3.1",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "goey-toast",
      "version": "0.3.1",
      "license": "MIT",
      "dependencies": {
        "sonner": "^2.0.7"
      },
      "devDependencies": {
        "@testing-library/jest-dom": "^6.9.1",
        "@testing-library/react": "^16.3.2",
        "@types/node": "^25.2.3",
        "@types/react": "^19.2.14",
        "@types/react-dom": "^19.2.3",
        "@vitejs/plugin-react": "^5.1.4",
        "framer-motion": "^12.34.0",
        "jsdom": "^28.0.0",
        "react": "^19.2.4",
        "react-dom": "^19.2.4",
        "tsup": "^8.5.1",
        "typescript": "^5.9.3",
        "vitest": "^4.0.18"
      },
      "engines": {
        "node": ">=18.0.0"
      },
      "peerDependencies": {
        "framer-motion": ">=10.0.0",
        "react": ">=18.0.0",
        "react-dom": ">=18.0.0"
      }
    },
    "node_modules/@acemir/cssom": {
      "version": "0.9.31",
      "resolved": "https://registry.npmjs.org/@acemir/cssom/-/cssom-0.9.31.tgz",
      "integrity": "sha512-ZnR3GSaH+/vJ0YlHau21FjfLYjMpYVIzTD8M8vIEQvIGxeOXyXdzCI140rrCY862p/C/BbzWsjc1dgnM9mkoTA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@adobe/css-tools": {
      "version": "4.4.4",
      "resolved": "https://registry.npmjs.org/@adobe/css-tools/-/css-tools-4.4.4.tgz",
      "integrity": "sha512-Elp+iwUx5rN5+Y8xLt5/GRoG20WGoDCQ/1Fb+1LiGtvwbDavuSk0jhD/eZdckHAuzcDzccnkv+rEjyWfRx18gg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@asamuzakjp/css-color": {
      "version": "4.1.2",
      "resolved": "https://registry.npmjs.org/@asamuzakjp/css-color/-/css-color-4.1.2.tgz",
      "integrity": "sha512-NfBUvBaYgKIuq6E/RBLY1m0IohzNHAYyaJGuTK79Z23uNwmz2jl1mPsC5ZxCCxylinKhT1Amn5oNTlx1wN8cQg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@csstools/css-calc": "^3.0.0",
        "@csstools/css-color-parser": "^4.0.1",
        "@csstools/css-parser-algorithms": "^4.0.0",
        "@csstools/css-tokenizer": "^4.0.0",
        "lru-cache": "^11.2.5"
      }
    },
    "node_modules/@asamuzakjp/css-color/node_modules/lru-cache": {
      "version": "11.2.6",
      "resolved": "https://registry.npmjs.org/lru-cache/-/lru-cache-11.2.6.tgz",
      "integrity": "sha512-ESL2CrkS/2wTPfuend7Zhkzo2u0daGJ/A2VucJOgQ/C48S/zB8MMeMHSGKYpXhIjbPxfuezITkaBH1wqv00DDQ==",
      "dev": true,
      "license": "BlueOak-1.0.0",
      "engines": {
        "node": "20 || >=22"
      }
    },
    "node_modules/@asamuzakjp/dom-selector": {
      "version": "6.7.8",
      "resolved": "https://registry.npmjs.org/@asamuzakjp/dom-selector/-/dom-selector-6.7.8.tgz",
      "integrity": "sha512-stisC1nULNc9oH5lakAj8MH88ZxeGxzyWNDfbdCxvJSJIvDsHNZqYvscGTgy/ysgXWLJPt6K/4t0/GjvtKcFJQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@asamuzakjp/nwsapi": "^2.3.9",
        "bidi-js": "^1.0.3",
        "css-tree": "^3.1.0",
        "is-potential-custom-element-name": "^1.0.1",
        "lru-cache": "^11.2.5"
      }
    },
    "node_modules/@asamuzakjp/dom-selector/node_modules/lru-cache": {
      "version": "11.2.6",
      "resolved": "https://registry.npmjs.org/lru-cache/-/lru-cache-11.2.6.tgz",
      "integrity": "sha512-ESL2CrkS/2wTPfuend7Zhkzo2u0daGJ/A2VucJOgQ/C48S/zB8MMeMHSGKYpXhIjbPxfuezITkaBH1wqv00DDQ==",
      "dev": true,
      "license": "BlueOak-1.0.0",
      "engines": {
        "node": "20 || >=22"
      }
    },
    "node_modules/@asamuzakjp/nwsapi": {
      "version": "2.3.9",
      "resolved": "https://registry.npmjs.org/@asamuzakjp/nwsapi/-/nwsapi-2.3.9.tgz",
      "integrity": "sha512-n8GuYSrI9bF7FFZ/SjhwevlHc8xaVlb/7HmHelnc/PZXBD2ZR49NnN9sMMuDdEGPeeRQ5d0hqlSlEpgCX3Wl0Q==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@babel/code-frame": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.29.0.tgz",
      "integrity": "sha512-9NhCeYjq9+3uxgdtp20LSiJXJvN0FeCtNGpJxuMFZ1Kv3cWUNb6DOhJwUvcVCzKGR66cw4njwM6hrJLqgOwbcw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-validator-identifier": "^7.28.5",
        "js-tokens": "^4.0.0",
        "picocolors": "^1.1.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/compat-data": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/compat-data/-/compat-data-7.29.0.tgz",
      "integrity": "sha512-T1NCJqT/j9+cn8fvkt7jtwbLBfLC/1y1c7NtCeXFRgzGTsafi68MRv8yzkYSapBnFA6L3U2VSc02ciDzoAJhJg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/core": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/core/-/core-7.29.0.tgz",
      "integrity": "sha512-CGOfOJqWjg2qW/Mb6zNsDm+u5vFQ8DxXfbM09z69p5Z6+mE1ikP2jUXw+j42Pf1XTYED2Rni5f95npYeuwMDQA==",
      "dev": true,
      "license": "MIT",
      "peer": true,
      "dependencies": {
        "@babel/code-frame": "^7.29.0",
        "@babel/generator": "^7.29.0",
        "@babel/helper-compilation-targets": "^7.28.6",
        "@babel/helper-module-transforms": "^7.28.6",
        "@babel/helpers": "^7.28.6",
        "@babel/parser": "^7.29.0",
        "@babel/template": "^7.28.6",
        "@babel/traverse": "^7.29.0",
        "@babel/types": "^7.29.0",
        "@jridgewell/remapping": "^2.3.5",
        "convert-source-map": "^2.0.0",
        "debug": "^4.1.0",
        "gensync": "^1.0.0-beta.2",
        "json5": "^2.2.3",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/babel"
      }
    },
    "node_modules/@babel/generator": {
      "version": "7.29.1",
      "resolved": "https://registry.npmjs.org/@babel/generator/-/generator-7.29.1.tgz",
      "integrity": "sha512-qsaF+9Qcm2Qv8SRIMMscAvG4O3lJ0F1GuMo5HR/Bp02LopNgnZBC/EkbevHFeGs4ls/oPz9v+Bsmzbkbe+0dUw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.29.0",
        "@babel/types": "^7.29.0",
        "@jridgewell/gen-mapping": "^0.3.12",
        "@jridgewell/trace-mapping": "^0.3.28",
        "jsesc": "^3.0.2"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-compilation-targets": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/helper-compilation-targets/-/helper-compilation-targets-7.28.6.tgz",
      "integrity": "sha512-JYtls3hqi15fcx5GaSNL7SCTJ2MNmjrkHXg4FSpOA/grxK8KwyZ5bubHsCq8FXCkua6xhuaaBit+3b7+VZRfcA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/compat-data": "^7.28.6",
        "@babel/helper-validator-option": "^7.27.1",
        "browserslist": "^4.24.0",
        "lru-cache": "^5.1.1",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-globals": {
      "version": "7.28.0",
      "resolved": "https://registry.npmjs.org/@babel/helper-globals/-/helper-globals-7.28.0.tgz",
      "integrity": "sha512-+W6cISkXFa1jXsDEdYA8HeevQT/FULhxzR99pxphltZcVaugps53THCeiWA8SguxxpSp3gKPiuYfSWopkLQ4hw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-imports": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-imports/-/helper-module-imports-7.28.6.tgz",
      "integrity": "sha512-l5XkZK7r7wa9LucGw9LwZyyCUscb4x37JWTPz7swwFE/0FMQAGpiWUZn8u9DzkSBWEcK25jmvubfpw2dnAMdbw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/traverse": "^7.28.6",
        "@babel/types": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-transforms": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-transforms/-/helper-module-transforms-7.28.6.tgz",
      "integrity": "sha512-67oXFAYr2cDLDVGLXTEABjdBJZ6drElUSI7WKp70NrpyISso3plG9SAGEF6y7zbha/wOzUByWWTJvEDVNIUGcA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-module-imports": "^7.28.6",
        "@babel/helper-validator-identifier": "^7.28.5",
        "@babel/traverse": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0"
      }
    },
    "node_modules/@babel/helper-plugin-utils": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/helper-plugin-utils/-/helper-plugin-utils-7.28.6.tgz",
      "integrity": "sha512-S9gzZ/bz83GRysI7gAD4wPT/AI3uCnY+9xn+Mx/KPs2JwHJIz1W8PZkg2cqyt3RNOBM8ejcXhV6y8Og7ly/Dug==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-string-parser": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-string-parser/-/helper-string-parser-7.27.1.tgz",
      "integrity": "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-identifier": {
      "version": "7.28.5",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.28.5.tgz",
      "integrity": "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-option": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-option/-/helper-validator-option-7.27.1.tgz",
      "integrity": "sha512-YvjJow9FxbhFFKDSuFnVCe2WxXk1zWc22fFePVNEaWJEu8IrZVlda6N0uHwzZrUM1il7NC9Mlp4MaJYbYd9JSg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helpers": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/helpers/-/helpers-7.28.6.tgz",
      "integrity": "sha512-xOBvwq86HHdB7WUDTfKfT/Vuxh7gElQ+Sfti2Cy6yIWNW05P8iUslOVcZ4/sKbE+/jQaukQAdz/gf3724kYdqw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/template": "^7.28.6",
        "@babel/types": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/parser": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/parser/-/parser-7.29.0.tgz",
      "integrity": "sha512-IyDgFV5GeDUVX4YdF/3CPULtVGSXXMLh1xVIgdCgxApktqnQV0r7/8Nqthg+8YLGaAtdyIlo2qIdZrbCv4+7ww==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.29.0"
      },
      "bin": {
        "parser": "bin/babel-parser.js"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@babel/plugin-transform-react-jsx-self": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-react-jsx-self/-/plugin-transform-react-jsx-self-7.27.1.tgz",
      "integrity": "sha512-6UzkCs+ejGdZ5mFFC/OCUrv028ab2fp1znZmCZjAOBKiBK2jXD1O+BPSfX8X2qjJ75fZBMSnQn3Rq2mrBJK2mw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/plugin-transform-react-jsx-source": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-react-jsx-source/-/plugin-transform-react-jsx-source-7.27.1.tgz",
      "integrity": "sha512-zbwoTsBruTeKB9hSq73ha66iFeJHuaFkUbwvqElnygoNbj/jHRsSeokowZFN3CZ64IvEqcmmkVe89OPXc7ldAw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/runtime": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/runtime/-/runtime-7.28.6.tgz",
      "integrity": "sha512-05WQkdpL9COIMz4LjTxGpPNCdlpyimKppYNoJ5Di5EUObifl8t4tuLuUBBZEpoLYOmfvIWrsp9fCl0HoPRVTdA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/template": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/template/-/template-7.28.6.tgz",
      "integrity": "sha512-YA6Ma2KsCdGb+WC6UpBVFJGXL58MDA6oyONbjyF/+5sBgxY/dwkhLogbMT2GXXyU84/IhRw/2D1Os1B/giz+BQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.28.6",
        "@babel/parser": "^7.28.6",
        "@babel/types": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/traverse": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/traverse/-/traverse-7.29.0.tgz",
      "integrity": "sha512-4HPiQr0X7+waHfyXPZpWPfWL/J7dcN1mx9gL6WdQVMbPnF3+ZhSMs8tCxN7oHddJE9fhNE7+lxdnlyemKfJRuA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.29.0",
        "@babel/generator": "^7.29.0",
        "@babel/helper-globals": "^7.28.0",
        "@babel/parser": "^7.29.0",
        "@babel/template": "^7.28.6",
        "@babel/types": "^7.29.0",
        "debug": "^4.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/types": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.29.0.tgz",
      "integrity": "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-string-parser": "^7.27.1",
        "@babel/helper-validator-identifier": "^7.28.5"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@csstools/color-helpers": {
      "version": "6.0.1",
      "resolved": "https://registry.npmjs.org/@csstools/color-helpers/-/color-helpers-6.0.1.tgz",
      "integrity": "sha512-NmXRccUJMk2AWA5A7e5a//3bCIMyOu2hAtdRYrhPPHjDxINuCwX1w6rnIZ4xjLcp0ayv6h8Pc3X0eJUGiAAXHQ==",
      "dev": true,
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/csstools"
        },
        {
          "typ
... [TRUNCATED]
```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "jsx": "react-jsx",
    "declaration": true,
    "declarationDir": "./dist",
    "outDir": "./dist",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  },
  "include": ["src"],
  "exclude": ["node_modules", "dist", "**/*.test.*"]
}

```

### File: tsup.config.ts
```ts
import { defineConfig } from 'tsup'

export default defineConfig({
  entry: ['src/index.ts'],
  format: ['esm', 'cjs'],
  dts: true,
  splitting: false,
  sourcemap: true,
  clean: true,
  external: ['react', 'react-dom', 'framer-motion', 'sonner'],
  treeshake: true,
})

```

### File: vercel.json
```json
{
  "buildCommand": "npm install && npm run build && cd demo && npm install && npm run build",
  "outputDirectory": "demo/dist",
  "installCommand": "echo 'skip'"
}

```

### File: vitest.config.ts
```ts
import { defineConfig } from 'vitest/config'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    globals: true,
    setupFiles: ['./src/__tests__/setup.ts'],
  },
})

```

### File: src\context.ts
```ts
import type { ToasterProps } from 'sonner'

let _position: ToasterProps['position'] = 'bottom-right'
let _dir: 'ltr' | 'rtl' = 'ltr'
let _spring: boolean = true
let _bounce: number | undefined = undefined
let _theme: 'light' | 'dark' = 'light'

export function setGooeyTheme(theme: 'light' | 'dark') {
  _theme = theme
}

export function getGooeyTheme(): 'light' | 'dark' {
  return _theme
}

export function setGooeyPosition(position: ToasterProps['position']) {
  _position = position
}

export function getGooeyPosition() {
  return _position
}

export function setGooeyDir(dir: 'ltr' | 'rtl') {
  _dir = dir
}

export function getGooeyDir(): 'ltr' | 'rtl' {
  return _dir
}

export function setGooeySpring(spring: boolean) {
  _spring = spring
}

export function getGooeySpring() {
  return _spring
}

export function setGooeyBounce(bounce: number | undefined) {
  _bounce = bounce
}

export function getGooeyBounce() {
  return _bounce
}

let _visibleToasts = 3

export function setGooeyVisibleToasts(n: number) {
  _visibleToasts = n
}

export function getGooeyVisibleToasts() {
  return _visibleToasts
}

// ---------------------------------------------------------------------------
// Container hover — broadcast from GooeyToaster to all mounted GooeyToast instances
// so timers pause and re-expand triggers correctly when hovering the stack.
// ---------------------------------------------------------------------------
let _swipeToDismiss = true

export function setGooeySwipeToDismiss(enabled: boolean) {
  _swipeToDismiss = enabled
}

export function getGooeySwipeToDismiss() {
  return _swipeToDismiss
}

let _closeOnEscape = true

export function setGooeyCloseOnEscape(enabled: boolean) {
  _closeOnEscape = enabled
}

export function getGooeyCloseOnEscape() {
  return _closeOnEscape
}

let _maxQueue = Infinity

export function setGooeyMaxQueue(n: number) {
  _maxQueue = n
}

export function getGooeyMaxQueue() {
  return _maxQueue
}

let _queueOverflow: 'drop-oldest' | 'drop-newest' = 'drop-oldest'

export function setGooeyQueueOverflow(strategy: 'drop-oldest' | 'drop-newest') {
  _queueOverflow = strategy
}

export function getGooeyQueueOverflow() {
  return _queueOverflow
}

let _showProgress = false

export function setGooeyShowProgress(show: boolean) {
  _showProgress = show
}

export function getGooeyShowProgress() {
  return _showProgress
}

let _closeButton: boolean | 'top-left' | 'top-right' = false

export function setGooeyCloseButton(value: boolean | 'top-left' | 'top-right') {
  _closeButton = value
}

export function getGooeyCloseButton(): boolean | 'top-left' | 'top-right' {
  return _closeButton
}

let _containerHovered = false
type HoverCb = (hovered: boolean) => void
const _hoverSubs: Set<HoverCb> = new Set()

export function setContainerHovered(hovered: boolean) {
  if (_containerHovered === hovered) return
  _containerHovered = hovered
  _hoverSubs.forEach(cb => cb(hovered))
}

export function getContainerHovered() {
  return _containerHovered
}

export function subscribeContainerHovered(cb: HoverCb): () => void {
  _hoverSubs.add(cb)
  return () => { _hoverSubs.delete(cb) }
}

// ---------------------------------------------------------------------------
// ARIA live region announcer — pushes text to a persistent live region so
// screen readers detect toast notifications reliably.
// ---------------------------------------------------------------------------
export type AriaLivePoliteness = 'polite' | 'assertive'

interface Announcement {
  message: string
  politeness: AriaLivePoliteness
}

type AnnounceCb = (announcement: Announcement) => void
const _announceSubs: Set<AnnounceCb> = new Set()

export function announce(message: string, politeness: AriaLivePoliteness = 'polite') {
  _announceSubs.forEach(cb => cb({ message, politeness }))
}

export function subscribeAnnouncements(cb: AnnounceCb): () => void {
  _announceSubs.add(cb)
  return () => { _announceSubs.delete(cb) }
}

```

### File: src\css-modules.d.ts
```ts
declare module "*.module.css" { const classes: { readonly [key: string]: string }; export default classes; }

```

### File: src\index.ts
```ts
import './components/GooeyToast.css'
export { GooeyToaster } from './components/GooeyToaster'
export { gooeyToast } from './gooey-toast'
export { animationPresets } from './presets'
export type { AnimationPreset, AnimationPresetName } from './presets'
export type {
  GooeyToastOptions,
  GooeyPromiseData,
  GooeyToasterProps,
  GooeyToastAction,
  GooeyToastClassNames,
  GooeyToastTimings,
  GooeyToastUpdateOptions,
  DismissFilter,
} from './types'

// Backward-compatible aliases for v0.2.x users upgrading to v0.3.0
export { GooeyToaster as GoeyToaster } from './components/GooeyToaster'
export { gooeyToast as goeyToast } from './gooey-toast'
export type { GooeyPromiseData as GoeyPromiseData } from './types'
export type { GooeyToastClassNames as GoeyToastClassNames } from './types'
export type { GooeyToastTimings as GoeyToastTimings } from './types'
export type { GooeyToastOptions as GoeyToastOptions } from './types'
export type { GooeyToasterProps as GoeyToasterProps } from './types'

```

### File: src\presets.ts
```ts
export interface AnimationPreset {
  bounce: number
  spring: boolean
}

export const animationPresets = {
  smooth: { bounce: 0.1, spring: true },
  bouncy: { bounce: 0.6, spring: true },
  subtle: { bounce: 0.05, spring: true },
  snappy: { bounce: 0.4, spring: true },
} as const satisfies Record<string, AnimationPreset>

export type AnimationPresetName = keyof typeof animationPresets

```

### File: src\types.ts
```ts
import type { ReactNode } from 'react'
import type { ExternalToast, ToasterProps } from 'sonner'
import type { AnimationPresetName } from './presets'

export type GooeyToastType = 'default' | 'success' | 'error' | 'warning' | 'info'

export interface GooeyToastTimings {
  displayDuration?: number
}

export interface GooeyToastClassNames {
  wrapper?: string
  content?: string
  header?: string
  title?: string
  icon?: string
  description?: string
  actionWrapper?: string
  actionButton?: string
}

export interface GooeyToastAction {
  label: string
  onClick: () => void
  successLabel?: string
}

export interface GooeyToastData {
  title: string
  description?: ReactNode
  type: GooeyToastType
  action?: GooeyToastAction
  icon?: ReactNode
  duration?: number
  classNames?: GooeyToastClassNames
  fillColor?: string
  borderColor?: string
  borderWidth?: number
  preset?: AnimationPresetName
  spring?: boolean
  bounce?: number
  showTimestamp?: boolean
}

export interface GooeyToastOptions {
  description?: ReactNode
  action?: GooeyToastAction
  icon?: ReactNode
  duration?: number
  id?: string | number
  classNames?: GooeyToastClassNames
  fillColor?: string
  borderColor?: string
  borderWidth?: number
  timing?: GooeyToastTimings
  preset?: AnimationPresetName
  spring?: boolean
  bounce?: number
  showProgress?: boolean
  showTimestamp?: boolean
  onDismiss?: (id: string | number) => void
  onAutoClose?: (id: string | number) => void
}

export interface GooeyPromiseData<T> {
  loading: string
  success: string | ((data: T) => string)
  error: string | ((error: unknown) => string)
  description?: {
    loading?: ReactNode
    success?: ReactNode | ((data: T) => ReactNode)
    error?: ReactNode | ((error: unknown) => ReactNode)
  }
  action?: {
    success?: GooeyToastAction
    error?: GooeyToastAction
  }
  classNames?: GooeyToastClassNames
  fillColor?: string
  borderColor?: string
  borderWidth?: number
  timing?: GooeyToastTimings
  preset?: AnimationPresetName
  spring?: boolean
  bounce?: number
  showTimestamp?: boolean
  onDismiss?: (id: string | number) => void
  onAutoClose?: (id: string | number) => void
}

export type GooeyToastPhase = 'loading' | 'default' | 'success' | 'error' | 'warning' | 'info'

export interface GooeyToastUpdateOptions {
  title?: string
  description?: ReactNode
  type?: GooeyToastType
  action?: GooeyToastAction
  icon?: ReactNode | null
  showTimestamp?: boolean
}

export interface DismissFilter {
  type: GooeyToastType | GooeyToastType[]
}

export interface GooeyToasterProps {
  position?: ToasterProps['position']
  duration?: number
  gap?: number
  offset?: number | string
  theme?: 'light' | 'dark'
  toastOptions?: Partial<ExternalToast>
  expand?: boolean
  closeButton?: boolean | 'top-left' | 'top-right'
  richColors?: boolean
  visibleToasts?: number
  dir?: 'ltr' | 'rtl'
  preset?: AnimationPresetName
  spring?: boolean
  bounce?: number
  swipeToDismiss?: boolean
  closeOnEscape?: boolean
  maxQueue?: number
  queueOverflow?: 'drop-oldest' | 'drop-newest'
  showProgress?: boolean
}

```

### File: src\usePrefersReducedMotion.ts
```ts
import { useState, useEffect } from 'react'

const QUERY = '(prefers-reduced-motion: reduce)'

function getInitialState(): boolean {
  if (typeof window === 'undefined' || typeof window.matchMedia !== 'function') {
    return false
  }
  return window.matchMedia(QUERY).matches
}

export function usePrefersReducedMotion(): boolean {
  const [prefersReducedMotion, setPrefersReducedMotion] = useState(getInitialState)

  useEffect(() => {
    if (typeof window === 'undefined' || typeof window.matchMedia !== 'function') {
      return
    }
    const mql = window.matchMedia(QUERY)
    const handler = (event: MediaQueryListEvent) => {
      setPrefersReducedMotion(event.matches)
    }
    mql.addEventListener('change', handler)
    return () => mql.removeEventListener('change', handler)
  }, [])

  return prefersReducedMotion
}

```

### File: src\components\gooey-styles.ts
```ts
/** Static class name map — avoids CSS module bundling issues with tsup */
export const styles = {
  spinnerSpin: 'gooey-spinnerSpin',
  wrapper: 'gooey-wrapper',
  blobSvg: 'gooey-blobSvg',
  content: 'gooey-content',
  contentCompact: 'gooey-contentCompact',
  contentExpanded: 'gooey-contentExpanded',
  header: 'gooey-header',
  iconWrapper: 'gooey-iconWrapper',
  title: 'gooey-title',
  titleDefault: 'gooey-titleDefault',
  titleSuccess: 'gooey-titleSuccess',
  titleError: 'gooey-titleError',
  titleWarning: 'gooey-titleWarning',
  titleInfo: 'gooey-titleInfo',
  titleLoading: 'gooey-titleLoading',
  description: 'gooey-description',
  actionWrapper: 'gooey-actionWrapper',
  actionButton: 'gooey-actionButton',
  actionDefault: 'gooey-actionDefault',
  actionSuccess: 'gooey-actionSuccess',
  actionError: 'gooey-actionError',
  actionWarning: 'gooey-actionWarning',
  actionInfo: 'gooey-actionInfo',
  progressWrapper: 'gooey-progressWrapper',
  progressBar: 'gooey-progressBar',
  progressDefault: 'gooey-progressDefault',
  progressSuccess: 'gooey-progressSuccess',
  progressError: 'gooey-progressError',
  progressWarning: 'gooey-progressWarning',
  progressInfo: 'gooey-progressInfo',
  progressPaused: 'gooey-progressPaused',
  timestamp: 'gooey-timestamp',
  closeButton: 'gooey-closeButton',
  closeButtonRight: 'gooey-closeButtonRight',
} as const

```

### File: src\components\GooeyToast.css
```css
/* Spinner animation */
.gooey-spinnerSpin {
  animation: gooey-spin 1s linear infinite;
}

@keyframes gooey-spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

/* Center position: center the toast within Sonner's container */
[data-sonner-toast][data-x-position="center"] {
  left: 0 !important;
  right: 0 !important;
  margin-left: auto !important;
  margin-right: auto !important;
  width: fit-content !important;
}

/* Fix mobile centering: override Sonner's mobile offset variables for center positions */
@media only screen and (max-width: 600px) {
  [data-sonner-toaster][data-x-position='center'] {
    left: 50% !important;
    right: auto !important;
    transform: translateX(-50%) !important;
  }
}

/* Style detection marker — used by GooeyToaster to verify CSS is loaded */
[data-gooey-toast-css] { --gooey-toast: 1; }

/* When Sonner expands the stack (hover), shorten height/transform CSS transitions
   so our syncSonnerHeights corrections apply quickly (~150ms instead of 400ms).
   Sonner writes stale --offset values from its React state; 400ms correction
   causes visible overlap. 150ms is fast enough to prevent overlap while keeping
   stacking spread and entry animations smooth. */
[data-sonner-toast][data-expanded="true"] {
  transition: transform 0.15s, opacity 0.4s, height 0.15s, box-shadow 0.2s !important;
}


/* ============================================
   Wrapper — single container for both states
   ============================================ */
.gooey-wrapper {
  pointer-events: auto;
  cursor: default;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
  position: relative;
  width: fit-content;
}

/* SVG background — parametric morph from pill to blob */
.gooey-blobSvg {
  position: absolute;
  top: 0;
  left: 0;
  overflow: visible;
  pointer-events: none;
  filter: drop-shadow(0 4px 12px rgba(0, 0, 0, 0.06))
          drop-shadow(0 1px 4px rgba(0, 0, 0, 0.04));
}

/* Content on top of SVG background */
.gooey-content {
  position: relative;
  z-index: 1;
  transition: padding 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}

.gooey-contentCompact {
  padding: 7px 10px 7px 10px;
}

.gooey-contentExpanded {
  padding: 7px 10px 16px 10px;
  min-width: 300px;
  max-width: 380px;
}

/* ============================================
   Shared
   ============================================ */
.gooey-header {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  color: inherit;
}

.gooey-header > .gooey-title,
.gooey-header > .gooey-timestamp {
  min-width: 0;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
}

.gooey-header > .gooey-timestamp {
  margin-left: auto;
}

.gooey-iconWrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  width: 18px;
  height: 18px;
  line-height: 0;
}

.gooey-title {
  font-size: 12px;
  font-weight: 700;
  line-height: 1;
  white-space: nowrap;
  color: inherit;
  padding: 0 4px 0 2px;
}

.gooey-titleDefault { color: #555; }
.gooey-titleSuccess { color: #4CAF50; }
.gooey-titleError { color: #E53935; }
.gooey-titleWarning { color: #C49000; }
.gooey-titleInfo { color: #1E88E5; }
.gooey-titleLoading { color: #555; }

.gooey-timestamp {
  font-size: 11px;
  font-weight: 400;
  color: #999;
  white-space: nowrap;
  line-height: 1;
  padding-left: 6px;
}

.gooey-description {
  font-size: 13px;
  font-weight: 400;
  color: #444;
  line-height: 1.55;
  margin-top: 16px;
  overflow: hidden;
}

.gooey-actionWrapper {
  margin-top: 12px;
  overflow: hidden;
}

.gooey-actionButton {
  display: block;
  box-sizing: border-box;
  width: 100%;
  border: none;
  border-radius: 999px;
  padding: 10px 20px;
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  font-family: inherit;
  text-align: center;
  outline: none;
  -webkit-tap-highlight-color: transparent;
  transition: background 0.15s ease;
}

.gooey-actionButton:focus:not(:focus-visible) {
  outline: none;
}

.gooey-actionButton:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.gooey-actionDefault {
  background: #E8E8E8;
  color: #555;
}
.gooey-actionDefault:hover { background: #DCDCDC; }
.gooey-actionDefault:active { background: #D0D0D0; }

.gooey-actionSuccess {
  background: #C8E6C9;
  color: #4CAF50;
}
.gooey-actionSuccess:hover { background: #A5D6A7; }
.gooey-actionSuccess:active { background: #81C784; }

.gooey-actionError {
  background: #FFCDD2;
  color: #E53935;
}
.gooey-actionError:hover { background: #EF9A9A; }
.gooey-actionError:active { background: #E57373; }

.gooey-actionWarning {
  background: #FFECB3;
  color: #C49000;
}
.gooey-actionWarning:hover { background: #FFE082; }
.gooey-actionWarning:active { background: #FFD54F; }

.gooey-actionInfo {
  background: #BBDEFB;
  color: #1E88E5;
}
.gooey-actionInfo:hover { background: #90CAF9; }
.gooey-actionInfo:active { background: #64B5F6; }

/* ============================================
   Progress countdown bar
   ============================================ */
.gooey-progressWrapper {
  margin-top: 10px;
  overflow: hidden;
  border-radius: 2px;
  height: 3px;
  background: rgba(0, 0, 0, 0.06);
}

.gooey-progressBar {
  height: 100%;
  border-radius: 2px;
  transform-origin: left center;
  animation: gooey-progress-shrink var(--gooey-progress-duration, 4000ms) linear forwards;
  animation-play-state: running;
}

.gooey-progressPaused .gooey-progressBar {
  animation-play-state: paused;
}

@keyframes gooey-progress-shrink {
  from { transform: scaleX(1); }
  to { transform: scaleX(0); }
}

.gooey-progressDefault { background: #999; }
.gooey-progressSuccess { background: #4CAF50; }
.gooey-progressError { background: #E53935; }
.gooey-progressWarning { background: #C49000; }
.gooey-progressInfo { background: #1E88E5; }

/* ============================================
   Dark mode
   ============================================ */

.gooey-wrapper[data-theme="dark"] .gooey-blobSvg {
  filter: drop-shadow(0 4px 12px rgba(0, 0, 0, 0.3))
          drop-shadow(0 1px 4px rgba(0, 0, 0, 0.2));
}

.gooey-wrapper[data-theme="dark"] .gooey-titleDefault { color: #ccc; }
.gooey-wrapper[data-theme="dark"] .gooey-titleSuccess { color: #66BB6A; }
.gooey-wrapper[data-theme="dark"] .gooey-titleError { color: #EF5350; }
.gooey-wrapper[data-theme="dark"] .gooey-titleWarning { color: #FFB300; }
.gooey-wrapper[data-theme="dark"] .gooey-titleInfo { color: #42A5F5; }
.gooey-wrapper[data-theme="dark"] .gooey-titleLoading { color: #ccc; }

.gooey-wrapper[data-theme="dark"] .gooey-timestamp {
  color: #777;
}

.gooey-wrapper[data-theme="dark"] .gooey-description {
  color: #e0e0e0;
}

.gooey-wrapper[data-theme="dark"] .gooey-actionDefault {
  background: #3a3a3a;
  color: #ccc;
}
.gooey-wrapper[data-theme="dark"] .gooey-actionDefault:hover { background: #444; }
.gooey-wrapper[data-theme="dark"] .gooey-actionDefault:active { background: #4e4e4e; }

.gooey-wrapper[data-theme="dark"] .gooey-actionSuccess {
  background: #1b5e20;
  color: #66BB6A;
}
.gooey-wrapper[data-theme="dark"] .gooey-actionSuccess:hover { background: #2e7d32; }
.gooey-wrapper[data-theme="dark"] .gooey-actionSuccess:active { background: #388e3c; }

.gooey-wrapper[data-theme="dark"] .gooey-actionError {
  background: #b71c1c;
  color: #EF5350;
}
.gooey-wrapper[data-theme="dark"] .gooey-actionError:hover { background: #c62828; }
.gooey-wrapper[data-theme="dark"] .gooey-actionError:active { background: #d32f2f; }

.gooey-wrapper[data-theme="dark"] .gooey-actionWarning {
  background: #4a3800;
  color: #FFB300;
}
.gooey-wrapper[data-theme="dark"] .gooey-actionWarning:hover { background: #5c4600; }
.gooey-wrapper[data-theme="dark"] .gooey-actionWarning:active { background: #6e5400; }

.gooey-wrapper[data-theme="dark"] .gooey-actionInfo {
  background: #0d47a1;
  color: #42A5F5;
}
.gooey-wrapper[data-theme="dark"] .gooey-actionInfo:hover { background: #1565c0; }
.gooey-wrapper[data-theme="dark"] .gooey-actionInfo:active { background: #1976d2; }

.gooey-wrapper[data-theme="dark"] .gooey-progressWrapper {
  background: rgba(255, 255, 255, 0.1);
}
.gooey-wrapper[data-theme="dark"] .gooey-progressDefault { background: #888; }
.gooey-wrapper[data-theme="dark"] .gooey-progressSuccess { background: #66BB6A; }
.gooey-wrapper[data-theme="dark"] .gooey-progressError { background: #EF5350; }
.gooey-wrapper[data-theme="dark"] .gooey-progressWarning { background: #FFB300; }
.gooey-wrapper[data-theme="dark"] .gooey-progressInfo { background: #42A5F5; }

/* ---------------------------------------------------------------------------
   Close button — appears on hover, positioned top-left by default.
   Use closeButton="top-right" on GooeyToaster for top-right placement.
   Border and background are set inline to match the toast's own styling.
   --------------------------------------------------------------------------- */
.gooey-closeButton {
  position: absolute;
  top: -6px;
  left: -6px;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  padding: 0;
  border-style: solid;
  border-radius: 50%;
  color: #444;
  cursor: pointer;
  opacity: 0;
  transition: opacity 0.15s ease, transform 0.15s ease;
  pointer-events: none;
  outline: none;
  -webkit-tap-highlight-color: transparent;
}
.gooey-closeButtonRight {
  left: auto;
  right: -1px;
  top: 6px;
}
.gooey-wrapper:hover .gooey-closeButton,
.gooey-wrapper:focus-within .gooey-closeButton,
.gooey-wrapper:active .gooey-closeButton {
  opacity: 1;
  pointer-events: auto;
}
.gooey-closeButton:focus,
.gooey-closeButton:focus-visible {
  opacity: 1;
  pointer-events: auto;
  box-shadow: 0 0 0 2px rgba(0, 0, 0, 0.15);
}
.gooey-closeButton:hover {
  transform: scale(1.15);
}
.gooey-closeButton:active {
  transform: scale(0.95);
}
.gooey-wrapper[data-theme="dark"] .gooey-closeButton {
  color: #e0e0e0;
  box-shadow: 0 1px 4px rgba(255, 255, 255, 0.25);
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

---
id: lenis
type: knowledge
owner: OA_Triage
---
# lenis
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "lenis",
  "version": "1.3.21",
  "description": "How smooth scroll should be",
  "type": "module",
  "sideEffects": false,
  "author": "darkroom.engineering",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/darkroomengineering/lenis.git"
  },
  "bugs": {
    "url": "https://github.com/darkroomengineering/lenis/issues"
  },
  "homepage": "https://github.com/darkroomengineering/lenis",
  "funding": {
    "type": "github",
    "url": "https://github.com/sponsors/darkroomengineering"
  },
  "keywords": [
    "scroll",
    "smooth",
    "lenis",
    "react",
    "vue"
  ],
  "workspaces": [
    "packages/*",
    "playground",
    "playground/*"
  ],
  "scripts": {
    "build": "tsdown",
    "dev": "bun run --parallel dev:build dev:playground",
    "dev:build": "tsdown --watch",
    "dev:playground": "bun --filter playground dev",
    "dev:nuxt": "bun --filter playground-nuxt dev",
    "readme": "node ./scripts/update-readme.js",
    "version:dev": "npm version prerelease --preid dev --force --no-git-tag-version",
    "version:patch": "npm version patch --force --no-git-tag-version",
    "version:minor": "npm version minor --force --no-git-tag-version",
    "version:major": "npm version major --force --no-git-tag-version",
    "postversion": "bun run build && bun run readme",
    "publish:dev": "npm publish --tag dev",
    "publish:main": "npm publish"
  },
  "files": [
    "dist"
  ],
  "devDependencies": {
    "@biomejs/biome": "^2.4.2",
    "tsdown": "^0.21.4",
    "typescript": "^5.7.3"
  },
  "peerDependencies": {
    "@nuxt/kit": ">=3.0.0",
    "react": ">=17.0.0",
    "vue": ">=3.0.0"
  },
  "peerDependenciesMeta": {
    "react": {
      "optional": true
    },
    "vue": {
      "optional": true
    },
    "@nuxt/kit": {
      "optional": true
    }
  },
  "unpkg": "./dist/lenis.mjs",
  "main": "./dist/lenis.mjs",
  "module": "./dist/lenis.mjs",
  "types": "./dist/lenis.d.ts",
  "exports": {
    ".": {
      "types": "./dist/lenis.d.ts",
      "default": "./dist/lenis.mjs"
    },
    "./react": {
      "types": "./dist/lenis-react.d.ts",
      "default": "./dist/lenis-react.mjs"
    },
    "./snap": {
      "types": "./dist/lenis-snap.d.ts",
      "default": "./dist/lenis-snap.mjs"
    },
    "./vue": {
      "types": "./dist/lenis-vue.d.ts",
      "default": "./dist/lenis-vue.mjs"
    },
    "./nuxt": {
      "default": "./dist/lenis-vue-nuxt.mjs"
    },
    "./nuxt/runtime/*": {
      "default": "./dist/nuxt/runtime/*.mjs"
    },
    "./dist/*": "./dist/*"
  }
}

```

### File: README.md
```md
[![LENIS](https://assets.darkroom.engineering/lenis/banner.gif)](https://github.com/darkroomengineering/lenis)

[![npm](https://img.shields.io/npm/v/lenis?colorA=E30613&colorB=000000
)](https://www.npmjs.com/package/lenis)
[![downloads](https://img.shields.io/npm/dm/lenis?colorA=E30613&colorB=000000
)](https://www.npmjs.com/package/lenis)
[![size](https://img.shields.io/bundlephobia/minzip/lenis?label=size&colorA=E30613&colorB=000000)](https://bundlephobia.com/package/lenis)

## Introduction

Lenis ("smooth" in latin) is a lightweight, robust, and performant smooth scroll library. It's designed by [@darkroom.engineering](https://twitter.com/darkroomdevs) to be simple to use and easy to integrate into your projects. It's built with performance in mind and is optimized for modern browsers. It's perfect for creating smooth scrolling experiences on your website such as WebGL scroll syncing, parallax effects, and much more, see [Demo](https://lenis.darkroom.engineering/) and [Showcase](https://www.lenis.dev/showcase).

Read our [Manifesto](https://github.com/darkroomengineering/lenis/blob/main/MANIFESTO.md) to learn more about the inspiration behind Lenis.

<br/>

- [Sponsors](#sponsors)
- [Packages](#packages)
- [Showcase](https://www.lenis.dev/showcase)
- [Installation](#installation)
- [Setup](#setup)
- [Settings](#settings)
- [Properties](#properties)
- [Methods](#methods)
- [Events](#events)
- [Considerations](#considerations)
- [Limitations](#limitations)
- [Troubleshooting](#troubleshooting)
- [Tutorials](#tutorials)
- [Plugins](#plugins)
- [License](#license)

<br/>

## Sponsors

If you’ve used Lenis and it made your site feel just a little more alive, consider [sponsoring](https://github.com/sponsors/darkroomengineering).

Your support helps us smooth out the internet one library at a time—and lets us keep building tools that care about the details most folks overlook.

<a href="https://www.osmo.supply/?utm_source=lenis.dev"><img src="https://www.lenis.dev/sponsors/osmo.png" width="128"/></a>
<br/>

<!-- sponsors -->
[![Jesse Winton](https://img.logo.dev/cosmos.so?size=64&token=pk_E-KcYZmdT--jxwGY3dAs1Q&fallback=404)](mailto:jesse@cosmos.so) [![smsunarto](https://github.com/smsunarto.png?size=64)](https://github.com/smsunarto) [![bizarro](https://github.com/bizarro.png?size=64)](https://github.com/bizarro) [![itsoffbrand](https://github.com/itsoffbrand.png?size=64)](https://github.com/itsoffbrand) [![arkconclave](https://github.com/arkconclave.png?size=64)](https://github.com/arkconclave) [![Tamas Bodo](https://img.logo.dev/framerpod.com?size=64&token=pk_E-KcYZmdT--jxwGY3dAs1Q&fallback=404)](mailto:hello@framerpod.com) [![glauber-sampaio](https://github.com/glauber-sampaio.png?size=64)](https://github.com/glauber-sampaio) [![cachet-studio](https://github.com/cachet-studio.png?size=64)](https://github.com/cachet-studio) [![OHO-Design](https://github.com/OHO-Design.png?size=64)](https://github.com/OHO-Design) [![joevingracien](https://github.com/joevingracien.png?size=64)](https://github.com/joevingracien) [![Lazar Filipovic](https://ui-avatars.com/api/?name=Lazar+Filipovic&size=64)](mailto:webdesignbylazar@gmail.com)
<!-- sponsors -->

<br/>
<a href="https://vercel.com/oss">
  <img alt="Vercel OSS Program" src="https://vercel.com/oss/program-badge.svg" />
</a>

<br/>

## Packages

- [lenis](https://github.com/darkroomengineering/lenis/blob/main/README.md)
- [lenis/react](https://github.com/darkroomengineering/lenis/blob/main/packages/react/README.md)
- [lenis/vue](https://github.com/darkroomengineering/lenis/tree/main/packages/vue/README.md)
- [lenis/framer](https://lenis.framer.website/)
- [lenis/snap](https://github.com/darkroomengineering/lenis/tree/main/packages/snap/README.md)


<br/>

## Installation

Using a package manager:

```bash
npm i lenis
# or
yarn add lenis
# or
pnpm add lenis
```

```js
import Lenis from 'lenis'
```

<br/>

Using scripts:

```html
<script src="https://unpkg.com/lenis@1.3.21/dist/lenis.min.js"></script> 
```


<br/>

## Setup

### Basic:

```js
// Initialize Lenis
const lenis = new Lenis({
  autoRaf: true,
});

// Listen for the scroll event and log the event data
lenis.on('scroll', (e) => {
  console.log(e);
});
```

### Custom raf loop:

```js
// Initialize Lenis
const lenis = new Lenis();

// Use requestAnimationFrame to continuously update the scroll
function raf(time) {
  lenis.raf(time);
  requestAnimationFrame(raf);
}

requestAnimationFrame(raf);
```

### Recommended CSS:

**Import stylesheet:**
```js
import 'lenis/dist/lenis.css'
```

**Or link the CSS file:**

```html
<link rel="stylesheet" href="https://unpkg.com/lenis@1.3.21/dist/lenis.css">
```

**Or add it manually:**

[See lenis.css stylesheet](./packages/core/lenis.css)

### GSAP ScrollTrigger:
```js
// Initialize a new Lenis instance for smooth scrolling
const lenis = new Lenis();

// Synchronize Lenis scrolling with GSAP's ScrollTrigger plugin
lenis.on('scroll', ScrollTrigger.update);

// Add Lenis's requestAnimationFrame (raf) method to GSAP's ticker
// This ensures Lenis's smooth scroll animation updates on each GSAP tick
gsap.ticker.add((time) => {
  lenis.raf(time * 1000); // Convert time from seconds to milliseconds
});

// Disable lag smoothing in GSAP to prevent any delay in scroll animations
gsap.ticker.lagSmoothing(0);

```

### React:
[See documentation for lenis/react](https://github.com/darkroomengineering/lenis/blob/main/packages/react/README.md).

### Vue:
[See documentation for lenis/vue](https://github.com/darkroomengineering/lenis/blob/main/packages/vue/README.md).


<br/>


## Settings

| Option                  | Type                       | Default                                            | Description                                                                                                                                                                                                                                                                          |
|-------------------------|----------------------------|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `wrapper`               | `HTMLElement, Window`      | `window`                                           | The element that will be used as the scroll container.                                                                                                                                                                                                                               |
| `content`               | `HTMLElement`              | `document.documentElement`                         | The element that contains the content that will be scrolled, usually `wrapper`'s direct child.                                                                                                                                                                                       |
| `eventsTarget`          | `HTMLElement, Window`      | `wrapper`                                          | The element that will listen to `wheel` and `touch` events.                                                                                                                                                                                                                          |
| `smoothWheel`           | `boolean`                  | `true`                                             | Smooth the scroll initiated by `wheel` events.                                                                                                                                                                                                                                       |
| `lerp`                  | `number`                   | `0.1`                                              | Linear interpolation (lerp) intensity (between 0 and 1).                                                                                                                                                                                                                             |
| `duration`              | `number`                   | `1.2`                                              | The duration of scroll animation (in seconds). Useless if lerp defined.                                                                                                                                                                                                              |
| `easing`                | `function`                 | `(t) => Math.min(1, 1.001 - Math.pow(2, -10 * t))` | The easing function to use for the scroll animation, our default is custom but you can pick one from [Easings.net](https://easings.net/en). Useless if lerp defined.                                                                                                                 |
| `orientation`           | `string`                   | `vertical`                                         | The orientation of the scrolling. Can be `vertical` or `horizontal`.                                                                                                                                                                                                                 |
| `gestureOrientation`    | `string`                   | `vertical`                                         | The orientation of the gestures. Can be `vertical`, `horizontal` or `both`.                                                                                                                                                                                                          |
| `syncTouch`             | `boolean`                  | `false`                                            | Mimic touch device scroll while allowing scroll sync (can be unstable on iOS<16).                                                                                                                                                                                                    |
| `syncTouchLerp`         | `number`                   | `0.075`                                            | Lerp applied during `syncTouch` inertia.                                                                                                                                                                                                                                             |
| `touchInertiaExponent`  | `number`                   | `1.7`                                              | Manage the strength of syncTouch inertia.                                                                                                                                                                                                                                            |
| `wheelMultiplier`       | `number`                   | `1`                                                | The multiplier to use for mouse wheel events.                                                                                                                                                                                                                                        |
| `touchMultiplier`       | `number`                   | `1`                                                | The multiplier to use for touch events.                                                                                                                                                                                                                                              |
| `infinite`              | `boolean`                  | `false`                                            | Enable infinite scrolling! `syncTouch: true` is required on touch devices ([See example](https://codepen.io/ClementRoche/pen/OJqBLod)).                                                                                                                                              |
| `autoResize`            | `boolean`                  | `true`                                             | Resize instance automatically       based on `ResizeObserver`. If `false` you must resize manually using `.resize()`.                                                                                                                                                                |
| `prevent`               | `function`                 | `undefined`                                        | Manually prevent scroll to be smoothed based on elements traversed by events. If `true` is returned, it will prevent the scroll to be smoothed. Example: `(node) =>  node.classList.contains('cookie-modal')`.                                                                       |
| `virtualScroll`         | `function`                 | `undefined`                                        | Manually modify the events before they get consumed. If `false` is returned, the scroll will not be smoothed. Examples: `(e) => { e.deltaY /= 2 }` (to slow down vertical scroll) or `({ event }) => !event.shiftKey` (to prevent scroll to be smoothed if shift key is pressed).    |
| `overscroll`            | `boolean`                  | `true`                                             | Similar to CSS overscroll-behavior (https://developer.mozilla.org/en-US/docs/Web/CSS/overscroll-behavior).                                                                                                                                                                           |
| `autoRaf`               | `boolean`                  | `false`                                            | Whether or not to automatically run `requestAnimationFrame` loop.                                                                                                                                                                                                                    |
| `anchors`               | `boolean, ScrollToOptions` | `false`                                            | Scroll to anchor links when clicked. If `true` is passed, it will enable anchor links with default options. If `ScrollToOptions` is passed, it will enable anchor links with the given options.                                                                                      |
| `autoToggle`            | `boolean`                  | `false`                                            | Automatically start or stop the lenis instance based on the wrapper's overflow property, ⚠️ this requires Lenis recommended CSS. Safari > 17.3, Chrome > 116 and Firefox > 128 ([https://caniuse.com/?search=transition-behavior](https://caniuse.com/?search=transition-behavior)). |
| `allowNestedScroll`     | `boolean`                
... [TRUNCATED]
```

### File: packages\core\package.json
```json
{
  "name": "lenis-core",
  "type": "module"
}

```

### File: packages\react\package.json
```json
{
  "name": "lenis-react",
  "type": "module",
  "devDependencies": {
    "@types/react": "^19.0.7",
    "react": "^19.0.0"
  }
}

```

### File: packages\react\README.md
```md
# lenis/react

## Introduction
lenis/react provides a `<ReactLenis>` component that creates a [Lenis](https://github.com/darkroomengineering/lenis) instance and provides it to its children via context. This allows you to use Lenis in your React app without worrying about passing the instance down through props. It also provides a `useLenis` hook that allows you to access the Lenis instance from any component in your app.


## Installation

```bash
npm i lenis
```

## Recommended CSS

Import the Lenis CSS to ensure proper behavior:

```js
import 'lenis/dist/lenis.css'
```

## Usage

### Basic

```jsx
import { ReactLenis, useLenis } from 'lenis/react'

function App() {
  const lenis = useLenis((lenis) => {
    // called every scroll
    console.log(lenis)
  })

  return (
    <>
      <ReactLenis root />
      { /* content */ }
    </>
  )
}
```

## Props
- `options`: [Lenis options](https://github.com/darkroomengineering/lenis#instance-settings).
- `root`: When `true`, makes the Lenis instance globally accessible via `useLenis` from anywhere in your app (even outside the provider tree). Lenis will use the default `<html>` scroll container. When `'asChild'`, renders wrapper elements for custom scroll containers while still making the instance globally accessible. Default: `false`.

## Hooks
Once the Lenis context is set (components mounted inside `<ReactLenis>`) you can use these handy hooks:

`useLenis` is a hook that returns the Lenis instance

The hook takes three arguments:
- `callback`: The function to be called whenever a scroll event is emitted
- `deps`: Trigger callback on change
- `priority`: Manage callback execution order





## Examples

### Custom requestAnimationFrame loop:

```jsx
import { ReactLenis } from 'lenis/react'
import { useEffect, useRef } from 'react'

function App() {
  const lenisRef = useRef()
  
  useEffect(() => {
    function update(time) {
      lenisRef.current?.lenis?.raf(time)
    }
  
    const rafId = requestAnimationFrame(update)
  
    return () => cancelAnimationFrame(rafId)
  }, [])
  
  return (
    <ReactLenis root options={{ autoRaf: false }} ref={lenisRef} />
  )
}
```


### GSAP integration

```jsx
import gsap from 'gsap'
import { ReactLenis } from 'lenis/react'
import { useEffect, useRef } from 'react'

function App() {
  const lenisRef = useRef()
  
  useEffect(() => {
    function update(time) {
      lenisRef.current?.lenis?.raf(time * 1000)
    }
  
    gsap.ticker.add(update)
  
    return () => gsap.ticker.remove(update)
  }, [])
  
  return (
    <ReactLenis root options={{ autoRaf: false }} ref={lenisRef} />
  )
}
```

### Framer Motion integration:
```jsx
import { ReactLenis } from 'lenis/react';
import type { LenisRef } from 'lenis/react';
import { cancelFrame, frame } from 'framer-motion';
import { useEffect, useRef } from 'react';

function App() {
  const lenisRef = useRef<LenisRef>(null)

  useEffect(() => {
    function update(data: { timestamp: number }) {
      const time = data.timestamp
      lenisRef.current?.lenis?.raf(time)
    }

    frame.update(update, true)

    return () => cancelFrame(update)
  }, [])


  return (
    <ReactLenis root options={{ autoRaf: false }} ref={lenisRef} />
  )
}
```

## lenis/react in use

- [@darkroom.engineering/satus](https://github.com/darkroomengineering/satus) Our starter kit.

<br/>

## License

MIT © [darkroom.engineering](https://github.com/darkroomengineering)

```

### File: biome.json
```json
{
  "$schema": "node_modules/@biomejs/biome/configuration_schema.json",

  "vcs": {
    "enabled": true,
    "clientKind": "git",
    "useIgnoreFile": true
  },

  "files": {
    "ignoreUnknown": true,
    "includes": [
      "**",
      "!node_modules",
      "!**/.next",
      "!**/dist",
      "!**/public",
      "!.github",
      "!.vercel",
      "!pnpm-lock.yaml",
      "!bun.lock",
      "!**/*.md",
      "!**/*.mdx",
      "!**/tailwind.css",
      "!**/root.css",
      "!**/*.grit"
    ]
  },

  "formatter": {
    "enabled": true,
    "indentStyle": "space",
    "indentWidth": 2,
    "lineEnding": "lf",
    "lineWidth": 80
  },

  "assist": {
    "actions": {
      "source": {
        "organizeImports": "on"
      }
    }
  },

  "linter": {
    "enabled": true,
    "domains": {
      "next": "recommended",
      "react": "recommended",
      "project": "recommended"
    },
    "rules": {
      "correctness": {
        "noUnusedImports": "error",
        "noUnusedVariables": "error",
        "noUnusedFunctionParameters": "warn",
        "useExhaustiveDependencies": "warn",
        "noUnknownMediaFeatureName": "off",
        "noInvalidUseBeforeDeclaration": "error"
      },

      "style": {
        "noNonNullAssertion": "off",
        "noUnusedTemplateLiteral": "off",
        "noParameterAssign": "error",
        "useAsConstAssertion": "error",
        "useDefaultParameterLast": "error",
        "useEnumInitializers": "error",
        "useSelfClosingElements": "error",
        "useSingleVarDeclarator": "error",
        "useNumberNamespace": "error",
        "noInferrableTypes": "error",
        "noUselessElse": "error",
        "useConsistentArrayType": "error",
        "useForOf": "warn",
        "useShorthandAssign": "error",
        "useTemplate": "warn",
        "useCollapsedElseIf": "warn",
        "useExponentiationOperator": "error",
        "useConsistentBuiltinInstantiation": "error",
        "useFilenamingConvention": {
          "level": "warn",
          "options": {
            "filenameCases": ["kebab-case", "camelCase"],
            "strictCase": false
          }
        },
        "noNestedTernary": "error"
      },

      "suspicious": {
        "noExplicitAny": "error",
        "noEmptyBlockStatements": "warn",
        "noDoubleEquals": "error",
        "noDebugger": "warn",
        "noGlobalIsFinite": "error",
        "noGlobalIsNan": "error",
        "noMisleadingCharacterClass": "error",
        "noPrototypeBuiltins": "warn",
        "noSelfCompare": "error",
        "noSparseArray": "error",
        "useAwait": "off"
      },

      "complexity": {
        "noForEach": "off",
        "useSimplifiedLogicExpression": "warn",
        "useFlatMap": "warn"
      },

      "security": {
        "noGlobalEval": "error",
        "noDangerouslySetInnerHtml": "warn",
        "noDangerouslySetInnerHtmlWithChildren": "error"
      },

      "a11y": {
        "useKeyWithClickEvents": "warn",
        "useValidAnchor": "warn",
        "useAltText": "error",
        "useButtonType": "error",
        "useValidAriaProps": "error",
        "useValidAriaRole": "error",
        "useValidAriaValues": "error",
        "noAriaUnsupportedElements": "error",
        "noAutofocus": "warn",
        "noDistractingElements": "error",
        "noRedundantAlt": "error",
        "useSemanticElements": "warn"
      },

      "performance": {
        "noImgElement": "error"
      },

      "nursery": {
        "useSortedClasses": {
          "level": "error",
          "fix": "safe",
          "options": {
            "attributes": ["class", "className"],
            "functions": ["cn", "clsx"]
          }
        }
      }
    }
  },

  "javascript": {
    "formatter": {
      "enabled": true,
      "quoteStyle": "single",
      "semicolons": "asNeeded",
      "trailingCommas": "es5"
    }
  },

  "json": {
    "parser": {
      "allowComments": true
    }
  },

  "css": {
    "linter": {
      "enabled": true
    },
    "formatter": {
      "enabled": true
    },
    "parser": {
      "cssModules": true
    }
  },

  "overrides": [
    {
      "includes": ["**/*.css"],
      "linter": {
        "rules": {
          "correctness": {
            "noUnknownFunction": "off"
          }
        }
      }
    },
    {
      "includes": ["**/*.tsx", "**/*.jsx"],
      "linter": {
        "rules": {
          "correctness": {
            "useJsxKeyInIterable": "error"
          },
          "a11y": {
            "useValidAnchor": "error",
            "useKeyWithClickEvents": "error",
            "useKeyWithMouseEvents": "error"
          }
        }
      }
    },
    {
      "includes": ["**/*.ts", "**/*.tsx"],
      "linter": {
        "rules": {
          "style": {
            "useImportType": "error",
            "useExportType": "error",
            "useConsistentArrayType": "error"
          },
          "correctness": {
            "noUndeclaredVariables": "off"
          }
        }
      }
    },
    {
      "includes": [
        "app/**/*.tsx",
        "app/**/*.ts",
        "app/**/*.jsx",
        "app/**/*.js"
      ],
      "linter": {
        "rules": {
          "style": {
            "noDefaultExport": "off"
          },
          "suspicious": {
            "useAwait": "off"
          }
        }
      }
    },
    {
      "includes": ["**/*.module.css"],
      "linter": {
        "rules": {
          "correctness": {
            "noUnknownProperty": "off"
          },
          "style": {
            "noDescendingSpecificity": "off"
          }
        }
      }
    },
    {
      "includes": ["lib/styles/css/root.css"],
      "linter": {
        "rules": {
          "suspicious": {
            "noDuplicateCustomProperties": "off"
          }
        }
      }
    },
    {
      "includes": ["**/*.vue"],
      "linter": {
        "rules": {
          "correctness": {
            "useHookAtTopLevel": "off"
          },
          "style": {
            "useFilenamingConvention": "off"
          }
        }
      }
    },
    {
      "includes": ["**/*.astro"],
      "linter": {
        "rules": {
          "correctness": {
            "noUnusedImports": "off",
            "noUnusedVariables": "off"
          },
          "style": {
            "useFilenamingConvention": "off"
          }
        }
      }
    }
  ]
}

```

### File: CONTRIBUTING.md
```md
# Lenis Contributing Guide

Yooo! We're really excited that you're interested in contributing to Lenis! Before submitting your contribution, please read through the following guide.

## Repo Setup

To develop locally, fork the Lenis repository and clone it in your local machine. The Lenis repo is a monorepo using bun workspaces. The package manager used to install and link dependencies must be [bun](https://bun.sh/).

To start developing Lenis, run the following commands in the root of the repository:

1. Run `bun i` in Lenis's root folder.

2. Run `bun run dev` in Lenis's root folder.

3. Open http://localhost:4321 in your browser, which has a playground for Lenis.

The dev server will automatically rebuild Lenis whenever you change its code no matter what package you are working on.
At the same time the playground will automatically reload when you change the code of any package.


## Pull Request Guidelines

- Checkout a topic branch from a base branch (e.g. `main`), and merge back against that branch.

- If adding a new feature:

  - Provide a convincing reason to add this feature. Ideally, you should open a suggestion issue first, and have it approved before working on it.

- If fixing a bug:

  - Provide a detailed description of the bug in the PR. Codepen demo preferred.

- Make sure to enable biome in your editor to format the code.

```

### File: MANIFESTO.md
```md
# For the Nerds 🧠
Alright, let's get nerdy for a minute because you probably installed Lenis for smooth scrolling and don’t even know the whole real story behind it. Originally, Lenis wasn’t built just to make your site scroll like butter (even though that’s a pretty nice side effect). No, the real mission was to tackle a major pain point in web development that most folks don't realize exists—synchronizing WebGL and the DOM while scrolling.

## The Real Problem 🤔
You see, WebGL and the DOM don’t play nicely together when you’re scrolling. With native scrolling, trying to keep WebGL animations in sync with DOM elements is like trying to teach a cat to fetch—it just doesn’t want to cooperate. There’s a constant fight over control, which means you end up with janky animations, weird timing issues, and an overall frustrating experience for developers and users alike. Lenis came in as the referee, letting us manage the scroll position smoothly and precisely, so WebGL and the DOM can finally share the spotlight.

## The Happy Mistake 🎉
But here’s the kicker—when we made Lenis to solve that problem, something interesting happened. Thanks to its ability to interpolate (or “lerp,” for the cool kids) the scroll position, it also created a super-smooth scrolling experience. And as it turns out, everyone just loves smooth scrolling. So much so that this “happy little accident” quickly overshadowed the original problem Lenis was built to solve. People started adopting it just for the silky smooth scrolling, completely unaware that Lenis was originally the secret weapon for complex WebGL-DOM synchronization.

## So… What’s the Point?
If you’re here thinking, “I just wanted my site to scroll like butter,” don’t worry—you’re not alone! Smooth scrolling is awesome, and Lenis does it really well. But for those of you who really want to know, Lenis is more than just a pretty face. It’s here to handle the hard stuff under the hood and to give you the control you need to pull off those super-synced, glitch-free animations.

In short: Lenis is the smooth scroll library that became famous by accident. So, next time you add it to your project, just know that it's not just a scrolling effect—it's a powerhouse tool for handling the impossible.
```

### File: tsconfig.json
```json
{
  "exclude": ["dist", "playground", "website"],
  "compilerOptions": {
    /* Base Options: */
    "skipLibCheck": true,
    "target": "es2022",
    "allowJs": true,
    "resolveJsonModule": true,
    "moduleDetection": "force",
    "isolatedModules": true,
    "verbatimModuleSyntax": true,
    "moduleResolution": "Bundler",
    "lib": ["ESNext", "DOM"],
    "rootDir": ".",
    "jsx": "react-jsx",

    /* Strictness */
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,

    /* If transpiling with TypeScript: */
    "module": "ESNext",
    "outDir": "dist",
    "sourceMap": true,

    /* AND if you're building for a library: */
    "declaration": true
  }
}

```

### File: tsdown.config.ts
```ts
import { defineConfig } from 'tsdown'

const shared = {
  outDir: 'dist',
  target: 'es2022' as const,
  platform: 'browser' as const,
  format: 'esm' as const,
  sourcemap: true,
  outExtensions: () => ({ js: '.mjs', dts: '.d.ts' }),
}

const iife = (globalName: string, minify = false) =>
  ({
    ...shared,
    format: 'iife' as const,
    dts: false,
    clean: false,
    globalName,
    minify,
    outExtensions: undefined,
    outputOptions: {
      entryFileNames: minify ? '[name].min.js' : '[name].js',
    },
  }) as const

export default defineConfig([
  // Core + Snap ESM
  {
    ...shared,
    entry: {
      lenis: 'packages/core/index.ts',
      'lenis-snap': 'packages/snap/index.ts',
    },
    dts: true,
    clean: true,
    copy: [{ from: 'packages/core/lenis.css', to: 'dist', flatten: true }],
    deps: { neverBundle: ['lenis'] },
  },

  // React ESM
  {
    ...shared,
    entry: { 'lenis-react': 'packages/react/index.ts' },
    dts: { resolver: 'tsc' },
    clean: false,
    banner: '"use client";',
    deps: { neverBundle: ['react', 'lenis'] },
  },

  // Vue ESM
  {
    ...shared,
    entry: { 'lenis-vue': 'packages/vue/index.ts' },
    dts: { resolver: 'tsc' },
    clean: false,
    deps: { neverBundle: ['vue', 'lenis'] },
  },

  // Nuxt ESM
  {
    ...shared,
    entry: {
      'lenis-vue-nuxt': 'packages/vue/nuxt/module.ts',
      'nuxt/runtime/lenis': 'packages/vue/nuxt/runtime/lenis.ts',
    },
    dts: false,
    sourcemap: false,
    clean: false,
    deps: { neverBundle: ['lenis', 'lenis/vue', '#imports', '#app', '@nuxt/kit'] },
  },

  // Browser IIFE builds
  { entry: { lenis: 'packages/core/browser.ts' }, ...iife('Lenis') },
  { entry: { lenis: 'packages/core/browser.ts' }, ...iife('Lenis', true) },
  { entry: { 'lenis-snap': 'packages/snap/browser.ts' }, ...iife('Snap') },
  { entry: { 'lenis-snap': 'packages/snap/browser.ts' }, ...iife('Snap', true) },
])

```

### File: scripts\update-readme.js
```js
import fs from 'node:fs'
import packageJson from '../package.json' with { type: 'json' }

const readmePath = './README.md'

function updateVersion() {
  return new Promise((resolve, reject) => {
    // update version in README
    fs.readFile(readmePath, 'utf8', (err, data) => {
      if (err) {
        console.log(`Error reading README file: ${err}`)
        return reject(err)
      }

      const updatedReadme = data.replace(
        /\/lenis@([^/]+)\//g,
        `/lenis@${packageJson.version}/`
      )

      fs.writeFile(readmePath, updatedReadme, 'utf8', (err) => {
        resolve()

        if (err) {
          return reject(err)
        }
      })
    })
  })
}

if (!packageJson.version.includes('-dev')) {
  updateVersion()
}

```

### File: .github\ISSUE_TEMPLATE\bug_report.md
```md
## Before to submit your issue
Read the [Troubleshooting](https://github.com/darkroomengineering/lenis#troubleshooting) section.

## Describe the bug
A clear and concise description of what the bug is.

## To Reproduce
Try to reproduce your issue by forking this [codepen](https://codepen.io/ClementRoche/pen/VwxgZEP). If you can't reproduce it, it means there is something wrong on your initial environment, please read the documentation again. If your issue doesn't include any reproduction link, it will take more time to be treaten.

```

### File: packages\core\browser.ts
```ts
// This file serves as an entry point for the package
import { Lenis } from './src/lenis'

// @ts-expect-error
globalThis.Lenis = Lenis
// @ts-expect-error
globalThis.Lenis.prototype = Lenis.prototype

```

### File: packages\core\index.ts
```ts
// This file serves as an entry point for the package
export { Lenis as default } from './src/lenis'
export * from './src/types'

```

### File: packages\core\lenis.css
```css
html.lenis,
html.lenis body {
  height: auto;
}

.lenis:not(.lenis-autoToggle).lenis-stopped {
  overflow: clip;
}

.lenis [data-lenis-prevent],
.lenis [data-lenis-prevent-wheel],
.lenis [data-lenis-prevent-touch],
.lenis [data-lenis-prevent-vertical],
.lenis [data-lenis-prevent-horizontal] {
  overscroll-behavior: contain;
}

.lenis.lenis-smooth iframe {
  pointer-events: none;
}

.lenis.lenis-autoToggle {
  transition-property: overflow;
  transition-duration: 1ms;
  transition-behavior: allow-discrete;
}

```

### File: packages\react\index.ts
```ts
// This file serves as an entry point for the package
export {
  LenisContext,
  ReactLenis as default,
  ReactLenis as Lenis,
  ReactLenis,
} from './src/provider'
export * from './src/types'
export { useLenis } from './src/use-lenis'

```

### File: packages\core\src\animate.ts
```ts
import { clamp, damp } from './maths'
import type { EasingFunction, FromToOptions, OnUpdateCallback } from './types'

/**
 * Animate class to handle value animations with lerping or easing
 *
 * @example
 * const animate = new Animate()
 * animate.fromTo(0, 100, { duration: 1, easing: (t) => t })
 * animate.advance(0.5) // 50
 */
export class Animate {
  isRunning = false
  value = 0
  from = 0
  to = 0
  currentTime = 0

  // These are instanciated in the fromTo method
  lerp?: number
  duration?: number
  easing?: EasingFunction
  onUpdate?: OnUpdateCallback

  /**
   * Advance the animation by the given delta time
   *
   * @param deltaTime - The time in seconds to advance the animation
   */
  advance(deltaTime: number) {
    if (!this.isRunning) return

    let completed = false

    if (this.duration && this.easing) {
      this.currentTime += deltaTime
      const linearProgress = clamp(0, this.currentTime / this.duration, 1)

      completed = linearProgress >= 1
      const easedProgress = completed ? 1 : this.easing(linearProgress)
      this.value = this.from + (this.to - this.from) * easedProgress
    } else if (this.lerp) {
      this.value = damp(this.value, this.to, this.lerp * 60, deltaTime)
      if (Math.round(this.value) === this.to) {
        this.value = this.to
        completed = true
      }
    } else {
      // If no easing or lerp, just jump to the end value
      this.value = this.to
      completed = true
    }

    if (completed) {
      this.stop()
    }

    // Call the onUpdate callback with the current value and completed status
    this.onUpdate?.(this.value, completed)
  }

  /** Stop the animation */
  stop() {
    this.isRunning = false
  }

  /**
   * Set up the animation from a starting value to an ending value
   * with optional parameters for lerping, duration, easing, and onUpdate callback
   *
   * @param from - The starting value
   * @param to - The ending value
   * @param options - Options for the animation
   */
  fromTo(
    from: number,
    to: number,
    { lerp, duration, easing, onStart, onUpdate }: FromToOptions
  ) {
    this.from = this.value = from
    this.to = to
    this.lerp = lerp
    this.duration = duration
    this.easing = easing
    this.currentTime = 0
    this.isRunning = true

    onStart?.()
    this.onUpdate = onUpdate
  }
}

```

### File: packages\core\src\debounce.ts
```ts
export function debounce<CB extends (...args: unknown[]) => void>(
  callback: CB,
  delay: number
) {
  let timer: number | undefined
  return function <T>(this: T, ...args: Parameters<typeof callback>) {
    clearTimeout(timer)
    timer = setTimeout(() => {
      timer = undefined
      callback.apply(this, args)
    }, delay)
  }
}

```

### File: packages\core\src\dimensions.ts
```ts
import { debounce } from './debounce'

/**
 * Dimensions class to handle the size of the content and wrapper
 *
 * @example
 * const dimensions = new Dimensions(wrapper, content)
 * dimensions.on('resize', (e) => {
 *   console.log(e.width, e.height)
 * })
 */
export class Dimensions {
  width = 0
  height = 0
  scrollHeight = 0
  scrollWidth = 0

  // These are instanciated in the constructor as they need information from the options
  private debouncedResize?: (...args: unknown[]) => void
  private wrapperResizeObserver?: ResizeObserver
  private contentResizeObserver?: ResizeObserver

  constructor(
    private wrapper: HTMLElement | Window | Element,
    private content: HTMLElement | Element,
    { autoResize = true, debounce: debounceValue = 250 } = {}
  ) {
    if (autoResize) {
      this.debouncedResize = debounce(this.resize, debounceValue)

      if (this.wrapper instanceof Window) {
        window.addEventListener('resize', this.debouncedResize)
      } else {
        this.wrapperResizeObserver = new ResizeObserver(this.debouncedResize)
        this.wrapperResizeObserver.observe(this.wrapper)
      }

      this.contentResizeObserver = new ResizeObserver(this.debouncedResize)
      this.contentResizeObserver.observe(this.content)
    }

    this.resize()
  }

  destroy() {
    this.wrapperResizeObserver?.disconnect()
    this.contentResizeObserver?.disconnect()

    if (this.wrapper === window && this.debouncedResize) {
      window.removeEventListener('resize', this.debouncedResize)
    }
  }

  resize = () => {
    this.onWrapperResize()
    this.onContentResize()
  }

  onWrapperResize = () => {
    if (this.wrapper instanceof Window) {
      this.width = window.innerWidth
      this.height = window.innerHeight
    } else {
      this.width = this.wrapper.clientWidth
      this.height = this.wrapper.clientHeight
    }
  }

  onContentResize = () => {
    if (this.wrapper instanceof Window) {
      this.scrollHeight = this.content.scrollHeight
      this.scrollWidth = this.content.scrollWidth
    } else {
      this.scrollHeight = this.wrapper.scrollHeight
      this.scrollWidth = this.wrapper.scrollWidth
    }
  }

  get limit() {
    return {
      x: this.scrollWidth - this.width,
      y: this.scrollHeight - this.height,
    }
  }
}

```

### File: packages\core\src\emitter.ts
```ts
/**
 * Emitter class to handle events
 * @example
 * const emitter = new Emitter()
 * emitter.on('event', (data) => {
 *   console.log(data)
 * })
 * emitter.emit('event', 'data')
 */
export class Emitter {
  private events: Record<
    string,
    Array<(...args: unknown[]) => void> | undefined
  > = {}

  /**
   * Emit an event with the given data
   * @param event Event name
   * @param args Data to pass to the event handlers
   */
  emit(event: string, ...args: unknown[]) {
    const callbacks = this.events[event] || []
    for (let i = 0, length = callbacks.length; i < length; i++) {
      callbacks[i]?.(...args)
    }
  }

  /**
   * Add a callback to the event
   * @param event Event name
   * @param cb Callback function
   * @returns Unsubscribe function
   */
  on<CB extends (...args: unknown[]) => void>(event: string, cb: CB) {
    // Add the callback to the event's callback list, or create a new list with the callback
    if (this.events[event]) {
      this.events[event].push(cb)
    } else {
      this.events[event] = [cb]
    }

    // Return an unsubscribe function
    return () => {
      this.events[event] = this.events[event]?.filter((i) => cb !== i)
    }
  }

  /**
   * Remove a callback from the event
   * @param event Event name
   * @param callback Callback function
   */
  off<CB extends (...args: unknown[]) => void>(event: string, callback: CB) {
    this.events[event] = this.events[event]?.filter((i) => callback !== i)
  }

  /**
   * Remove all event listeners and clean up
   */
  destroy() {
    this.events = {}
  }
}

```

### File: packages\core\src\lenis.ts
```ts
import { version } from '../../../package.json'
import { Animate } from './animate'
import { Dimensions } from './dimensions'
import { Emitter } from './emitter'
import { clamp, modulo } from './maths'
import type {
  LenisEvent,
  LenisOptions,
  ScrollCallback,
  Scrolling,
  ScrollToOptions,
  UserData,
  VirtualScrollCallback,
  VirtualScrollData,
} from './types'
import { VirtualScroll } from './virtual-scroll'

// Technical explanation
// - listen to 'wheel' events
// - prevent 'wheel' event to prevent scroll
// - normalize wheel delta
// - add delta to targetScroll
// - animate scroll to targetScroll (smooth context)
// - if animation is not running, listen to 'scroll' events (native context)

type OptionalPick<T, F extends keyof T> = Omit<T, F> & Partial<Pick<T, F>>

const defaultEasing = (t: number) => Math.min(1, 1.001 - 2 ** (-10 * t))

export class Lenis {
  private _isScrolling: Scrolling = false // true when scroll is animating
  private _isStopped = false // true if user should not be able to scroll - enable/disable programmatically
  private _isLocked = false // same as isStopped but enabled/disabled when scroll reaches target
  private _preventNextNativeScrollEvent = false
  private _resetVelocityTimeout: ReturnType<typeof setTimeout> | null = null
  private _rafId: number | null = null

  /**
   * Whether or not the user is touching the screen
   */
  isTouching?: boolean
  /**
   * The time in ms since the lenis instance was created
   */
  time = 0
  /**
   * User data that will be forwarded through the scroll event
   *
   * @example
   * lenis.scrollTo(100, {
   *   userData: {
   *     foo: 'bar'
   *   }
   * })
   */
  userData: UserData = {}
  /**
   * The last velocity of the scroll
   */
  lastVelocity = 0
  /**
   * The current velocity of the scroll
   */
  velocity = 0
  /**
   * The direction of the scroll
   */
  direction: 1 | -1 | 0 = 0
  /**
   * The options passed to the lenis instance
   */
  options: OptionalPick<
    Required<LenisOptions>,
    | 'duration'
    | 'easing'
    | 'prevent'
    | 'virtualScroll'
    | '__experimental__naiveDimensions'
  >
  /**
   * The target scroll value
   */
  targetScroll: number
  /**
   * The animated scroll value
   */
  animatedScroll: number

  // These are instanciated here as they don't need information from the options
  private readonly animate = new Animate()
  private readonly emitter = new Emitter()
  // These are instanciated in the constructor as they need information from the options
  readonly dimensions: Dimensions // This is not private because it's used in the Snap class
  private readonly virtualScroll: VirtualScroll

  constructor({
    wrapper = window,
    content = document.documentElement,
    eventsTarget = wrapper,
    smoothWheel = true,
    syncTouch = false,
    syncTouchLerp = 0.075,
    touchInertiaExponent = 1.7,
    duration, // in seconds
    easing,
    lerp = 0.1,
    infinite = false,
    orientation = 'vertical', // vertical, horizontal
    gestureOrientation = orientation === 'horizontal' ? 'both' : 'vertical', // vertical, horizontal, both
    touchMultiplier = 1,
    wheelMultiplier = 1,
    autoResize = true,
    prevent,
    virtualScroll,
    overscroll = true,
    autoRaf = false,
    anchors = false,
    autoToggle = false, // https://caniuse.com/?search=transition-behavior
    allowNestedScroll = false,
    __experimental__naiveDimensions = false,
    naiveDimensions = __experimental__naiveDimensions,
    stopInertiaOnNavigate = false,
  }: LenisOptions = {}) {
    // Set version (deprecated)
    window.lenisVersion = version

    if (!window.lenis) {
      window.lenis = {}
    }

    window.lenis.version = version

    if (orientation === 'horizontal') {
      window.lenis.horizontal = true
    }

    if (syncTouch === true) {
      window.lenis.touch = true
    }

    // Check if wrapper is <html>, fallback to window
    if (!wrapper || wrapper === document.documentElement) {
      wrapper = window
    }

    // flip to easing/time based animation if at least one of them is provided
    if (typeof duration === 'number' && typeof easing !== 'function') {
      easing = defaultEasing
    } else if (typeof easing === 'function' && typeof duration !== 'number') {
      duration = 1
    }

    // Setup options
    this.options = {
      wrapper,
      content,
      eventsTarget,
      smoothWheel,
      syncTouch,
      syncTouchLerp,
      touchInertiaExponent,
      duration,
      easing,
      lerp,
      infinite,
      gestureOrientation,
      orientation,
      touchMultiplier,
      wheelMultiplier,
      autoResize,
      prevent,
      virtualScroll,
      overscroll,
      autoRaf,
      anchors,
      autoToggle,
      allowNestedScroll,
      naiveDimensions,
      stopInertiaOnNavigate,
    }

    // Setup dimensions instance
    this.dimensions = new Dimensions(wrapper, content, { autoResize })

    // Setup class name
    this.updateClassName()

    // Set the initial scroll value for all scroll information
    this.targetScroll = this.animatedScroll = this.actualScroll

    // Add event listeners
    this.options.wrapper.addEventListener('scroll', this.onNativeScroll)

    this.options.wrapper.addEventListener('scrollend', this.onScrollEnd, {
      capture: true,
    })

    if (this.options.anchors || this.options.stopInertiaOnNavigate) {
      this.options.wrapper.addEventListener(
        'click',
        this.onClick as EventListener
      )
    }

    this.options.wrapper.addEventListener(
      'pointerdown',
      this.onPointerDown as EventListener
    )

    // Setup virtual scroll instance
    this.virtualScroll = new VirtualScroll(eventsTarget as HTMLElement, {
      touchMultiplier,
      wheelMultiplier,
    })
    this.virtualScroll.on('scroll', this.onVirtualScroll)

    if (this.options.autoToggle) {
      this.checkOverflow()
      this.rootElement.addEventListener('transitionend', this.onTransitionEnd)
    }

    if (this.options.autoRaf) {
      this._rafId = requestAnimationFrame(this.raf)
    }
  }

  /**
   * Destroy the lenis instance, remove all event listeners and clean up the class name
   */
  destroy() {
    this.emitter.destroy()

    this.options.wrapper.removeEventListener('scroll', this.onNativeScroll)

    this.options.wrapper.removeEventListener('scrollend', this.onScrollEnd, {
      capture: true,
    })

    this.options.wrapper.removeEventListener(
      'pointerdown',
      this.onPointerDown as EventListener
    )

    if (this.options.anchors || this.options.stopInertiaOnNavigate) {
      this.options.wrapper.removeEventListener(
        'click',
        this.onClick as EventListener
      )
    }

    this.virtualScroll.destroy()
    this.dimensions.destroy()

    this.cleanUpClassName()

    if (this._rafId) {
      cancelAnimationFrame(this._rafId)
    }
  }

  /**
   * Add an event listener for the given event and callback
   *
   * @param event Event name
   * @param callback Callback function
   * @returns Unsubscribe function
   */
  on(event: 'scroll', callback: ScrollCallback): () => void
  on(event: 'virtual-scroll', callback: VirtualScrollCallback): () => void
  on(event: LenisEvent, callback: ScrollCallback | VirtualScrollCallback) {
    return this.emitter.on(event, callback as (...args: unknown[]) => void)
  }

  /**
   * Remove an event listener for the given event and callback
   *
   * @param event Event name
   * @param callback Callback function
   */
  off(event: 'scroll', callback: ScrollCallback): void
  off(event: 'virtual-scroll', callback: VirtualScrollCallback): void
  off(event: LenisEvent, callback: ScrollCallback | VirtualScrollCallback) {
    return this.emitter.off(event, callback as (...args: unknown[]) => void)
  }

  private onScrollEnd = (e: Event | CustomEvent) => {
    if (!(e instanceof CustomEvent)) {
      if (this.isScrolling === 'smooth' || this.isScrolling === false) {
        e.stopPropagation()
      }
    }
  }

  private dispatchScrollendEvent = () => {
    this.options.wrapper.dispatchEvent(
      new CustomEvent('scrollend', {
        bubbles: this.options.wrapper === window,
        // cancelable: false,
        detail: {
          lenisScrollEnd: true,
        },
      })
    )
  }

  get overflow() {
    const property = this.isHorizontal ? 'overflow-x' : 'overflow-y'
    return getComputedStyle(this.rootElement)[
      property as keyof CSSStyleDeclaration
    ] as string
  }

  private checkOverflow() {
    if (['hidden', 'clip'].includes(this.overflow)) {
      this.internalStop()
    } else {
      this.internalStart()
    }
  }

  private onTransitionEnd = (event: TransitionEvent) => {
    if (
      event.propertyName?.includes('overflow') &&
      event.target === this.rootElement
    ) {
      this.checkOverflow()
    }
  }

  private setScroll(scroll: number) {
    // behavior: 'instant' bypasses the scroll-behavior CSS property

    if (this.isHorizontal) {
      this.options.wrapper.scrollTo({ left: scroll, behavior: 'instant' })
    } else {
      this.options.wrapper.scrollTo({ top: scroll, behavior: 'instant' })
    }
  }

  private onClick = (event: PointerEvent | MouseEvent) => {
    const path = event.composedPath()

    // filter anchor elements (elements with a valid href attribute)
    const linkElements = path.filter(
      (node) => node instanceof HTMLAnchorElement && node.href
    ) as HTMLAnchorElement[]
    const linkElementsUrls = linkElements.map(
      (element) => new URL(element.href)
    )

    const currentUrl = new URL(window.location.href)

    if (this.options.anchors) {
      const anchorElementUrl = linkElementsUrls.find(
        (targetUrl) =>
          currentUrl.host === targetUrl.host &&
          currentUrl.pathname === targetUrl.pathname &&
          targetUrl.hash
      )

      if (anchorElementUrl) {
        const options =
          typeof this.options.anchors === 'object' && this.options.anchors
            ? this.options.anchors
            : undefined

        const target = `#${anchorElementUrl.hash.split('#')[1]}`

        this.scrollTo(target, options)
        return
      }
    }

    if (this.options.stopInertiaOnNavigate) {
      const hasPageLinkElementUrl = linkElementsUrls.some(
        (targetUrl) =>
          currentUrl.host === targetUrl.host &&
          currentUrl.pathname !== targetUrl.pathname
      )

      if (hasPageLinkElementUrl) {
        this.reset()
        return
      }
    }
  }

  private onPointerDown = (event: PointerEvent | MouseEvent) => {
    if (event.button === 1) {
      this.reset()
    }
  }

  private onVirtualScroll = (data: VirtualScrollData) => {
    if (
      typeof this.options.virtualScroll === 'function' &&
      this.options.virtualScroll(data) === false
    )
      return

    const { deltaX, deltaY, event } = data

    this.emitter.emit('virtual-scroll', { deltaX, deltaY, event })

    // keep zoom feature
    if (event.ctrlKey) return
    // @ts-expect-error
    if (event.lenisStopPropagation) return

    const isTouch = event.type.includes('touch')
    const isWheel = event.type.includes('wheel')

    this.isTouching = event.type === 'touchstart' || event.type === 'touchmove'

    const isClickOrTap = deltaX === 0 && deltaY === 0

    const isTapToStop =
      this.options.syncTouch &&
      isTouch &&
      event.type === 'touchstart' &&
      isClickOrTap &&
      !this.isStopped &&
      !this.isLocked

    if (isTapToStop) {
      this.reset()
      return
    }

    // const isPullToRefresh =
    //   this.options.gestureOrientation === 'vertical' &&
    //   this.scroll === 0 &&
    //   !this.options.infinite &&
    //   deltaY <= 5 // touch pull to refresh, not reliable yet

    // most likely a touchpad gesture, this keep prev/next page navigation working
    const isUnknownGesture =
      (this.options.gestureOrientation === 'vertical' && deltaY === 0) ||
      (this.options.gestureOrientation === 'horizontal' && deltaX === 0)

    if (isClickOrTap || isUnknownGesture) {
      return
    }

    // catch if scrolling on nested scroll elements
    let composedPath = event.composedPath()
    composedPath = composedPath.slice(0, composedPath.indexOf(this.rootElement)) // remove parents elements

    const prevent = this.options.prevent

    const gestureOrientation =
      Math.abs(deltaX) >= Math.abs(deltaY) ? 'horizontal' : 'vertical'

    if (
      composedPath.find(
        (node) =>
          node instanceof HTMLElement &&
          ((typeof prevent === 'function' && prevent?.(node)) ||
            node.hasAttribute?.('data-lenis-prevent') ||
            (gestureOrientation === 'vertical' &&
              node.hasAttribute?.('data-lenis-prevent-vertical')) ||
            (gestureOrientation === 'horizontal' &&
              node.hasAttribute?.('data-lenis-prevent-horizontal')) ||
            (isTouch && node.hasAttribute?.('data-lenis-prevent-touch')) ||
            (isWheel && node.hasAttribute?.('data-lenis-prevent-wheel')) ||
            (this.options.allowNestedScroll &&
              this.hasNestedScroll(node, {
                deltaX,
                deltaY,
              })))
      )
    )
      return

    if (this.isStopped || this.isLocked) {
      if (event.cancelable) {
        event.preventDefault() // this will stop forwarding the event to the parent, this is problematic
      }
      return
    }

    const isSmooth =
      (this.options.syncTouch && isTouch) ||
      (this.options.smoothWheel && isWheel)

    if (!isSmooth) {
      this.isScrolling = 'native'
      this.animate.stop()
      // @ts-expect-error
      event.lenisStopPropagation = true
      return
    }

    let delta = deltaY
    if (this.options.gestureOrientation === 'both') {
      delta = Math.abs(deltaY) > Math.abs(deltaX) ? deltaY : deltaX
    } else if (this.options.gestureOrientation === 'horizontal') {
      delta = deltaX
    }

    if (
      !this.options.overscroll ||
      this.options.infinite ||
      (this.options.wrapper !== window &&
        this.limit > 0 &&
        ((this.animatedScroll > 0 && this.animatedScroll < this.limit) ||
          (this.animatedScroll === 0 && deltaY > 0) ||
          (this.animatedScroll === this.limit && deltaY < 0)))
    ) {
      // @ts-expect-error
      event.lenisStopPropagation = true
      // event.stopPropagation()
    }

    if (event.cancelable) {
      event.preventDefault()
    }

    const isSyncTouch = isTouch && this.options.syncTouch
    const isTouchEnd = isTouch && event.type === 'touchend'

    const hasTouchInertia = isTouchEnd

    if (hasTouchInertia) {
      delta =
        Math.sign(this.velocity) *
        Math.abs(this.velocity) ** this.options.touchInertiaExponent
    }

    this.scrollTo(this.targetScroll + delta, {
      programmatic: false,
      ...(isSyncTouch
        ? {
            lerp: hasTouchInertia ? this.options.syncTouchLerp : 1,
          }
        : {
            lerp: this.options.lerp,
          
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

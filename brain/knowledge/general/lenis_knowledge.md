---
id: lenis-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:03.921047
---

# KNOWLEDGE EXTRACT: lenis
> **Extracted on:** 2026-03-30 17:40:15
> **Source:** lenis

---

## File: `.gitignore`
```
# See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

# dependencies
node_modules
/.pnp
.pnp.js

# testing
/coverage

# next.js
.next/
/out/

# production
/build
/docs/dist

# misc
.DS_Store
*.pem

# debug
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# local env files
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# vercel
.vercel
.eslintcache

.npmrc


packages/core/dist/
packages/react/dist/
packages/snap/dist/
packages/vue/dist/

dist-new/
dist/
```

## File: `biome.json`
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

## File: `CONTRIBUTING.md`
```markdown
# Lenis Contributing Guide

Yooo! We're really excited that you're interested in contributing to Lenis! Before submitting your contribution, please read through the following guide.

## Repo Setup

To develop locally, fork the Lenis repository and clone it in your local machine. The Lenis repo is a monorepo using pnpm workspaces. The package manager used to install and link dependencies must be [pnpm](https://pnpm.io/).

To start developing Lenis, run the following commands in the root of the repository:

1. Run `pnpm i` in Lenis's root folder.

2. Run `pnpm dev` in Lenis's root folder.

3. Open http://localhost:4321 in your browser, which has a playground for Lenis.

The dev server will automatically rebuild Lenis whenever you change its code no matter what package you are working on.
At the same time the playground will automatically reload when you change the code of any package.


## Pull Request Guidelines

- Checkout a topic branch from a base branch (e.g. `main`), and merge back against that branch.

- If adding a new feature:

  - Provide a convincing reason to add this feature. Ideally, you should open a suggestion issue first, and have it approved before working on it.

- If fixing a bug:

  - Provide a detailed description of the bug in the PR. Codepen demo preferred.

- Make sure to enable prettier in your editor to format the code.
```

## File: `LICENSE`
```
The MIT License

Copyright (c) 2024 darkroom.engineering

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `MANIFESTO.md`
```markdown
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

## File: `package.json`
```json
{
  "name": "lenis",
  "version": "1.3.19",
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
  "scripts": {
    "build": "pnpm build:core && pnpm build:all",
    "build:core": "tsup --config tsup.core.ts",
    "build:all": "tsup",
    "dev": "pnpm run -w --parallel /^dev:.*/",
    "dev:build": "tsup --watch",
    "dev:playground": "pnpm --filter playground dev",
    "dev:nuxt": "pnpm --filter playground-nuxt dev",
    "readme": "node ./scripts/update-readme.js",
    "version:dev": "npm version prerelease --preid dev --force --no-git-tag-version",
    "version:patch": "npm version patch --force --no-git-tag-version",
    "version:minor": "npm version minor --force --no-git-tag-version",
    "version:major": "npm version major --force --no-git-tag-version",
    "postversion": "pnpm build && pnpm readme",
    "publish:dev": "npm publish --tag dev",
    "publish:main": "npm publish"
  },
  "files": [
    "dist"
  ],
  "devDependencies": {
    "@biomejs/biome": "^2.4.2",
    "terser": "^5.37.0",
    "tsup": "^8.5.1",
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

## File: `pnpm-workspace.yaml`
```yaml
packages:
  - 'packages/*'
  - 'playground'
  - 'playground/*'
```

## File: `README.md`
```markdown
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
<script src="https://unpkg.com/lenis@1.3.19/dist/lenis.min.js"></script> 
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
<link rel="stylesheet" href="https://unpkg.com/lenis@1.3.19/dist/lenis.css">
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
| `allowNestedScroll`     | `boolean`                  | `false`                                            | Automatically allow nested scrollable elements to scroll natively. This is the simplest way to handle nested scroll. ⚠️ Can create performance issues since it checks the DOM tree on every scroll event. If that's a concern, use `data-lenis-prevent` attributes instead.          |
| `naiveDimensions`       | `boolean`                  | `false`                                            | If `true`, Lenis will use naive dimensions calculation. ⚠️ Be careful, this has a performance impact.                                                                                                                                                                                |
| `stopInertiaOnNavigate` | `boolean`                  | `false`                                            | If `true`, Lenis will stop inertia when an internal link is clicked.                                                                                                                                                                                                                 |
<br/>

<!-- `target`: goal to reach
- `number`: value to scroll in pixels
- `string`: CSS selector or keyword (`top`, `left`, `start`, `bottom`, `right`, `end`)
- `HTMLElement`: DOM element

<br/>

`options`:
- `offset`(`number`): equivalent to [`scroll-padding-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/scroll-padding-top)
- `lerp`(`number`): animation lerp intensity
- `duration`(`number`): animation duration (in seconds)
- `easing`(`function`): animation easing
- `immediate`(`boolean`): ignore duration, easing and lerp
- `lock`(`boolean`): whether or not to prevent user from scrolling until target reached
- `onComplete`(`function`): called when target is reached -->

## Properties

| Property                | Type              | Description                                                                |
|-------------------------|-------------------|----------------------------------------------------------------------------|
| `animatedScroll`        | `number`          | Current scroll value                                                       |
| `dimensions`            | `object`          | Dimensions instance                                                        |
| `direction`             | `number`          | `1`: scrolling up, `-1`: scrolling down                                    |
 `options`               | `object`          | Instance options                                                           |
| `targetScroll`          | `number`          | Target scroll value                                                        |
| `time`                  | `number`          | Time elapsed since instance creation                                       |
| `actualScroll`          | `number`          | Current scroll value registered by the browser                             |
| `lastVelocity`          | `number`          | last scroll velocity                                                       |
| `velocity`              | `number`          | Current scroll velocity                                                    |
| `isHorizontal` (getter) | `boolean`         | Whether or not the instance is horizontal                                  |
| `isScrolling` (getter)  | `boolean, string` | Whether or not the scroll is being animated, `smooth`, `native` or `false` |
| `isStopped` (getter)    | `boolean`         | Whether or not the user should be able to scroll                           |
| `limit` (getter)        | `number`          | Maximum scroll value                                                       |
| `progress` (getter)     | `number`          | Scroll progress from `0` to `1`                                            |
| `rootElement` (getter)  | `HTMLElement`     | Element on which Lenis is instanced                                        |
| `scroll` (getter)       | `number`          | Current scroll value (handles infinite scroll if activated)                |
| `className` (getter)    | `string`          | `rootElement` className                                                    |

<br/>

## Methods

| Method                      | Description                                                                     | Arguments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `raf(time)`                 | Must be called every frame for internal usage.                                  | `time`: in ms                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `scrollTo(target, options)` | Scroll to target.                                                               | `target`: goal to reach<ul><li>`number`: value to scroll in pixels</li><li>`string`: CSS selector or keyword (`top`, `left`, `start`, `bottom`, `right`, `end`)</li><li>`HTMLElement`: DOM element</li></ul>`options`<ul><li>`offset`(`number`): equivalent to [`scroll-padding-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/scroll-padding-top)</li><li>`lerp`(`number`): animation lerp intensity</li><li>`duration`(`number`): animation duration (in seconds)</li><li>`easing`(`function`): animation easing</li><li>`immediate`(`boolean`): ignore duration, easing and lerp</li><li>`lock`(`boolean`): whether or not to prevent the user from scrolling until the target is reached</li><li>`force`(`boolean`): reach target even if instance is stopped</li><li>`onComplete`(`function`): called when the target is reached</li><li>`userData`(`object`): this object will be forwarded through `scroll` events</li></ul> |
| `on(id, function)`          | `id` can be any of the following [instance events](#instance-events) to listen. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `stop()`                    | Pauses the scroll                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `start()`                   | Resumes the scroll                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `resize()`                  | Compute internal sizes, it has to be used if `autoResize` option is `false`.    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `destroy()`                 | Destroys the instance and removes all events.                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |



## Events

| Event            | Callback Arguments        |
|------------------|---------------------------|
| `scroll`         | Lenis instance            |
| `virtual-scroll` | `{deltaX, deltaY, event}` |


<br/>

## Considerations

### Nested scroll

The simplest and most reliable way to handle nested scrollable elements is to use the `allowNestedScroll` option:

```js
const lenis = new Lenis({
  allowNestedScroll: true,
})
```

This automatically detects nested scrollable elements and lets them scroll natively. However, this can create performance issues since Lenis needs to check the DOM tree on every scroll event. If you experience performance problems, use `data-lenis-prevent` instead.

#### Using HTML attributes

```html
<div data-lenis-prevent>scrollable content</div>
```

[See example](https://codepen.io/ClementRoche/pen/PoLdjpw)

| Attribute                       | Description                          |
|---------------------------------|--------------------------------------|
| `data-lenis-prevent`            | Prevent all smooth scroll events     |
| `data-lenis-prevent-wheel`      | Prevent wheel events only            |
| `data-lenis-prevent-touch`      | Prevent touch events only            |
| `data-lenis-prevent-vertical`   | Prevent vertical scroll events only  |
| `data-lenis-prevent-horizontal` | Prevent horizontal scroll events only|

#### Using Javascript

```html
<div id="modal">scrollable content</div>
```

```js
const lenis = new Lenis({
  prevent: (node) => node.id === 'modal',
})
```

[See example](https://codepen.io/ClementRoche/pen/emONGYN)



### Anchor links
By default, Lenis will prevent anchor links from working while scrolling. To enable them, you must set `anchors: true`.

```js
new Lenis({
  anchors: true
})
```

You can also use `scrollTo` options:

```js
new Lenis({
  anchors: {
    offset: 100,
    onComplete: ()=>{
      console.log('scrolled to anchor')
    }
  }
})
```

<br/>

## Limitations

- no support for CSS scroll-snap, you must use ([lenis/snap](https://github.com/darkroomengineering/lenis/tree/main/packages/snap/README.md))
- capped to 60fps on Safari ([source](https://bugs.webkit.org/show_bug.cgi?id=173434)) and 30fps on low power mode
- smooth scroll will stop working over iframe since they don't forward wheel events
- position fixed seems to lag on MacOS Safari pre-M1 ([source](https://github.com/darkroomengineering/lenis/issues/103))
- touch events may behave unexpectedly when `syncTouch` is enabled on iOS < 16
- nested scroll containers require proper configuration to work correctly

<br/>

## Troubleshooting
- Make sure you use the latest version of [Lenis](https://www.npmjs.com/package/lenis?activeTab=versions)
- Include the recommended CSS
- If using GSAP ScrollTrigger, ensure proper integration (see [GSAP ScrollTrigger setup](#setup) section)
- Test without Lenis to ensure your element/page is scrollable
- Be sure to use `autoRaf: true` or manually call `lenis.raf(time)` in your animation loop

<br/>

## Tutorials

- [Scroll Animation Ideas for Image Grids](https://tympanus.net/Development/ScrollAnimationsGrid/) by [Codrops](https://tympanus.net/codrops)
- [How to Animate SVG Shapes on Scroll](https://tympanus.net/codrops/2022/06/08/how-to-animate-svg-shapes-on-scroll) by [Codrops](https://tympanus.net/codrops)
- [The BEST smooth scrolling library for your Webflow website! (Lenis)](https://www.youtube.com/watch?v=VtCqTLRRMII) by [Diego Toda de Oliveira](https://www.diegoliv.works/)
- [Easy smooth scroll in @Webflow with Lenis + GSAP ScrollTrigger tutorial](https://www.youtube.com/watch?v=gRKuzQTXq74) by [También Studio](https://www.tambien.studio/)

<br/>

## Plugins

- [r3f-scroll-rig](https://github.com/14islands/r3f-scroll-rig) by [14islands](https://14islands.com/)
- [locomotive-scroll](https://github.com/locomotivemtl/locomotive-scroll) by [Locomotive](https://locomotive.ca/)

<br/>

## License

MIT © [darkroom.engineering](https://github.com/darkroomengineering)
```

## File: `tsconfig.json`
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

## File: `tsup.config.ts`
```typescript
import { defineConfig, type Options } from 'tsup'

const OUT_DIR = 'dist'

function makeBuildOptions(
  fileName: string,
  entryPoint: string,
  format?: 'esm' | 'browser',
  overwrites: Options = {}
): Options[] {
  const options = {
    entryPoints: { [fileName]: entryPoint },
    format: 'esm',
    outDir: OUT_DIR,
    platform: 'browser',
    target: 'es2022',
    cjsInterop: false,
    dts: true,
    sourcemap: true,
    external: ['react', 'vue', 'lenis'],
    outExtension: () =>
      format === 'esm' ? { js: '.mjs', dts: '.d.ts' } : { js: '.js' },
    ...overwrites,
  } satisfies Options

  const minifyOptions = {
    ...options,
    minify: 'terser',
    terserOptions: {
      mangle: {
        reserved: ['Lenis'],
      },
    },
    outExtension: () => ({ js: '.min.js' }),
    ...overwrites,
  } satisfies Options

  return format === 'esm' ? [options] : [options, minifyOptions]
}

// Builds
export const coreESMOptions = makeBuildOptions(
  'lenis',
  'packages/core/index.ts',
  'esm'
)
const coreBrowserOptions = makeBuildOptions(
  'lenis',
  'packages/core/browser.ts',
  'browser',
  { dts: false }
)
const coreCSSOptions = makeBuildOptions(
  'lenis',
  'packages/core/lenis.css',
  undefined,
  { dts: false, sourcemap: false, minify: true }
)

const snapESMOptions = makeBuildOptions(
  'lenis-snap',
  'packages/snap/index.ts',
  'esm'
)
const snapBrowserOptions = makeBuildOptions(
  'lenis-snap',
  'packages/snap/browser.ts',
  'browser',
  { dts: false }
)

const reactOptions = makeBuildOptions(
  'lenis-react',
  'packages/react/index.ts',
  'esm',
  { banner: { js: '"use client";' } }
)
const vueOptions = makeBuildOptions('lenis-vue', 'packages/vue/index.ts', 'esm')
const nuxtOptions = makeBuildOptions(
  'lenis-vue-nuxt',
  'packages/vue/nuxt/module.ts',
  'esm',
  { external: ['#imports', 'lenis'], dts: false, sourcemap: false }
)

const nuxtOptionsRuntime = makeBuildOptions(
  'nuxt/runtime/lenis',
  'packages/vue/nuxt/runtime/lenis.ts',
  'esm',
  {
    external: ['#imports', '#app', 'lenis'],
    sourcemap: false,
    tsconfig: './packages/vue/nuxt/tsconfig.json',
  }
)

export default defineConfig(() => {
  console.log(`\x1b[31mLNS\x1b[0m\x1b[1m Building all packages\x1b[0m\n`)
  return [
    ...coreESMOptions,
    ...coreBrowserOptions,
    ...coreCSSOptions,
    ...snapESMOptions,
    ...snapBrowserOptions,
    ...reactOptions,
    ...vueOptions,
    ...nuxtOptions,
    ...nuxtOptionsRuntime,
  ]
})
```

## File: `tsup.core.ts`
```typescript
import { defineConfig } from 'tsup'
import { coreESMOptions } from './tsup.config'

// This file exsist as the core has to be built first as all other packages depend on it
export default defineConfig(() => {
  console.log(`\x1b[31mLNS\x1b[0m\x1b[1m Building core package\x1b[0m\n`)
  return { ...coreESMOptions[0], clean: true }
})
```


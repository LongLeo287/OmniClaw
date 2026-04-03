---
id: github.com-darkroomengineering-lenis-aa4c0b93-know
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:43.179097
---

# KNOWLEDGE EXTRACT: github.com_darkroomengineering_lenis_aa4c0b93
> **Extracted on:** 2026-04-01 16:40:53
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007525224/github.com_darkroomengineering_lenis_aa4c0b93

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
/brain/knowledge/docs_legacy/dist

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

.tldr/
.tldrignore
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
| `overscroll`            | `boolean`                  | `true`                                             | Similar to CSS overscroll-behavior (https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/CSS/overscroll-behavior).                                                                                                                                                                           |
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
- `offset`(`number`): equivalent to [`scroll-padding-top`](https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/CSS/scroll-padding-top)
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
| `scrollTo(target, options)` | Scroll to target.                                                               | `target`: goal to reach<ul><li>`number`: value to scroll in pixels</li><li>`string`: CSS selector or keyword (`top`, `left`, `start`, `bottom`, `right`, `end`)</li><li>`HTMLElement`: DOM element</li></ul>`options`<ul><li>`offset`(`number`): equivalent to [`scroll-padding-top`](https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/CSS/scroll-padding-top)</li><li>`lerp`(`number`): animation lerp intensity</li><li>`duration`(`number`): animation duration (in seconds)</li><li>`easing`(`function`): animation easing</li><li>`immediate`(`boolean`): ignore duration, easing and lerp</li><li>`lock`(`boolean`): whether or not to prevent the user from scrolling until the target is reached</li><li>`force`(`boolean`): reach target even if instance is stopped</li><li>`onComplete`(`function`): called when the target is reached</li><li>`userData`(`object`): this object will be forwarded through `scroll` events</li></ul> |
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

## File: `bun.lock`
```
{
  "lockfileVersion": 1,
  "configVersion": 1,
  "workspaces": {
    "": {
      "name": "lenis",
      "devDependencies": {
        "@biomejs/biome": "^2.4.2",
        "tsdown": "^0.21.4",
        "typescript": "^5.7.3",
      },
      "peerDependencies": {
        "@nuxt/kit": ">=3.0.0",
        "react": ">=17.0.0",
        "vue": ">=3.0.0",
      },
      "optionalPeers": [
        "@nuxt/kit",
        "react",
        "vue",
      ],
    },
    "packages/core": {
      "name": "lenis-core",
    },
    "packages/react": {
      "name": "lenis-react",
      "devDependencies": {
        "@types/react": "^19.0.7",
        "react": "^19.0.0",
      },
    },
    "packages/snap": {
      "name": "lenis-snap",
    },
    "packages/vue": {
      "name": "lenis-vue",
      "devDependencies": {
        "vue": "^3.5.13",
      },
    },
    "playground": {
      "name": "playground",
      "version": "0.0.1",
      "dependencies": {
        "@astrojs/check": "^0.9.4",
        "@astrojs/react": "^4.1.6",
        "@astrojs/vue": "^5.0.6",
        "@types/react": "^19.0.7",
        "@types/react-dom": "^19.0.3",
        "astro": "^5.1.8",
        "lenis": "*",
        "lorem-ipsum": "^2.0.8",
        "react": "^19.0.0",
        "react-dom": "^19.0.0",
        "stats-js": "1.0.1",
        "typescript": "^5.7.3",
        "vue": "^3.5.13",
      },
    },
    "playground/nuxt": {
      "name": "playground-nuxt",
      "dependencies": {
        "gsap": "latest",
        "lenis": "*",
        "nuxt": "^3.15.3",
        "vue": "latest",
        "vue-router": "latest",
      },
    },
  },
  "packages": {
    "@antfu/utils": ["@antfu/utils@0.7.10", "", {}, "sha512-+562v9k4aI80m1+VuMHehNJWLOFjBnXn3tdOitzD0il5b7smkSBal4+a3oKiQTbrwMmN/TBUMDvbdoWDehgOww=="],

    "@astrojs/check": ["@astrojs/check@0.9.8", "", { "dependencies": { "@astrojs/language-server": "^2.16.5", "chokidar": "^4.0.3", "kleur": "^4.1.5", "yargs": "^17.7.2" }, "peerDependencies": { "typescript": "^5.0.0" }, "bin": { "astro-check": "bin/astro-check.js" } }, "sha512-LDng8446QLS5ToKjRHd3bgUdirvemVVExV7nRyJfW2wV36xuv7vDxwy5NWN9zqeSEDgg0Tv84sP+T3yEq+Zlkw=="],

    "@astrojs/compiler": ["@astrojs/compiler@2.13.1", "", {}, "sha512-f3FN83d2G/v32ipNClRKgYv30onQlMZX1vCeZMjPsMMPl1mDpmbl0+N5BYo4S/ofzqJyS5hvwacEo0CCVDn/Qg=="],

    "@astrojs/internal-helpers": ["@astrojs/internal-helpers@0.7.6", "", {}, "sha512-GOle7smBWKfMSP8osUIGOlB5kaHdQLV3foCsf+5Q9Wsuu+C6Fs3Ez/ttXmhjZ1HkSgsogcM1RXSjjOVieHq16Q=="],

    "@astrojs/language-server": ["@astrojs/language-server@2.16.5", "", { "dependencies": { "@astrojs/compiler": "^2.13.1", "@astrojs/yaml2ts": "^0.2.3", "@jridgewell/sourcemap-codec": "^1.5.5", "@volar/kit": "~2.4.28", "@volar/language-core": "~2.4.28", "@volar/language-server": "~2.4.28", "@volar/language-service": "~2.4.28", "muggle-string": "^0.4.1", "tinyglobby": "^0.2.15", "volar-service-css": "0.0.70", "volar-service-emmet": "0.0.70", "volar-service-html": "0.0.70", "volar-service-prettier": "0.0.70", "volar-service-typescript": "0.0.70", "volar-service-typescript-twoslash-queries": "0.0.70", "volar-service-yaml": "0.0.70", "vscode-html-languageservice": "^5.6.2", "vscode-uri": "^3.1.0" }, "peerDependencies": { "prettier": "^3.0.0", "prettier-plugin-astro": ">=0.11.0" }, "optionalPeers": ["prettier", "prettier-plugin-astro"], "bin": { "astro-ls": "bin/nodeServer.js" } }, "sha512-MEQvrbuiFDEo+LCO4vvYuTr3eZ4IluZ/n4BbUv77AWAJNEj/n0j7VqTvdL1rGloNTIKZTUd46p5RwYKsxQGY8w=="],

    "@astrojs/markdown-remark": ["@astrojs/markdown-remark@6.3.11", "", { "dependencies": { "@astrojs/internal-helpers": "0.7.6", "@astrojs/prism": "3.3.0", "github-slugger": "^2.0.0", "hast-util-from-html": "^2.0.3", "hast-util-to-text": "^4.0.2", "import-meta-resolve": "^4.2.0", "js-yaml": "^4.1.1", "mdast-util-definitions": "^6.0.0", "rehype-raw": "^7.0.0", "rehype-stringify": "^10.0.1", "remark-gfm": "^4.0.1", "remark-parse": "^11.0.0", "remark-rehype": "^11.1.2", "remark-smartypants": "^3.0.2", "shiki": "^3.21.0", "smol-toml": "^1.6.0", "unified": "^11.0.5", "unist-util-remove-position": "^5.0.0", "unist-util-visit": "^5.0.0", "unist-util-visit-parents": "^6.0.2", "vfile": "^6.0.3" } }, "sha512-hcaxX/5aC6lQgHeGh1i+aauvSwIT6cfyFjKWvExYSxUhZZBBdvCliOtu06gbQyhbe0pGJNoNmqNlQZ5zYUuIyQ=="],

    "@astrojs/prism": ["@astrojs/prism@3.3.0", "", { "dependencies": { "prismjs": "^1.30.0" } }, "sha512-q8VwfU/fDZNoDOf+r7jUnMC2//H2l0TuQ6FkGJL8vD8nw/q5KiL3DS1KKBI3QhI9UQhpJ5dc7AtqfbXWuOgLCQ=="],

    "@astrojs/react": ["@astrojs/react@4.4.2", "", { "dependencies": { "@vitejs/plugin-react": "^4.7.0", "ultrahtml": "^1.6.0", "vite": "^6.4.1" }, "peerDependencies": { "@types/react": "^17.0.50 || ^18.0.21 || ^19.0.0", "@types/react-dom": "^17.0.17 || ^18.0.6 || ^19.0.0", "react": "^17.0.2 || ^18.0.0 || ^19.0.0", "react-dom": "^17.0.2 || ^18.0.0 || ^19.0.0" } }, "sha512-1tl95bpGfuaDMDn8O3x/5Dxii1HPvzjvpL2YTuqOOrQehs60I2DKiDgh1jrKc7G8lv+LQT5H15V6QONQ+9waeQ=="],

    "@astrojs/telemetry": ["@astrojs/telemetry@3.3.0", "", { "dependencies": { "ci-info": "^4.2.0", "debug": "^4.4.0", "dlv": "^1.1.3", "dset": "^3.1.4", "is-docker": "^3.0.0", "is-wsl": "^3.1.0", "which-pm-runs": "^1.1.0" } }, "sha512-UFBgfeldP06qu6khs/yY+q1cDAaArM2/7AEIqQ9Cuvf7B1hNLq0xDrZkct+QoIGyjq56y8IaE2I3CTvG99mlhQ=="],

    "@astrojs/vue": ["@astrojs/vue@5.1.4", "", { "dependencies": { "@vitejs/plugin-vue": "5.2.4", "@vitejs/plugin-vue-jsx": "^4.2.0", "@vue/compiler-sfc": "^3.5.26", "vite": "^6.4.1", "vite-plugin-vue-devtools": "^7.7.9" }, "peerDependencies": { "astro": "^5.0.0", "vue": "^3.2.30" } }, "sha512-srE+3tgSnGG4FVr7Bs9JAgLcUAg1mtGrbBFdwlj++Y05Awwlc967WCcmOK6rnxQ6q5PcK5+WL2x2tKoWh5SN7A=="],

    "@astrojs/yaml2ts": ["@astrojs/yaml2ts@0.2.3", "", { "dependencies": { "yaml": "^2.8.2" } }, "sha512-PJzRmgQzUxI2uwpdX2lXSHtP4G8ocp24/t+bZyf5Fy0SZLSF9f9KXZoMlFM/XCGue+B0nH/2IZ7FpBYQATBsCg=="],

    "@babel/code-frame": ["@babel/code-frame@7.29.0", "", { "dependencies": { "@babel/helper-validator-identifier": "^7.28.5", "js-tokens": "^4.0.0", "picocolors": "^1.1.1" } }, "sha512-9NhCeYjq9+3uxgdtp20LSiJXJvN0FeCtNGpJxuMFZ1Kv3cWUNb6DOhJwUvcVCzKGR66cw4njwM6hrJLqgOwbcw=="],

    "@babel/compat-data": ["@babel/compat-data@7.29.0", "", {}, "sha512-T1NCJqT/j9+cn8fvkt7jtwbLBfLC/1y1c7NtCeXFRgzGTsafi68MRv8yzkYSapBnFA6L3U2VSc02ciDzoAJhJg=="],

    "@babel/core": ["@babel/core@7.29.0", "", { "dependencies": { "@babel/code-frame": "^7.29.0", "@babel/generator": "^7.29.0", "@babel/helper-compilation-targets": "^7.28.6", "@babel/helper-module-transforms": "^7.28.6", "@babel/helpers": "^7.28.6", "@babel/parser": "^7.29.0", "@babel/template": "^7.28.6", "@babel/traverse": "^7.29.0", "@babel/types": "^7.29.0", "@jridgewell/remapping": "^2.3.5", "convert-source-map": "^2.0.0", "debug": "^4.1.0", "gensync": "^1.0.0-beta.2", "json5": "^2.2.3", "semver": "^6.3.1" } }, "sha512-CGOfOJqWjg2qW/Mb6zNsDm+u5vFQ8DxXfbM09z69p5Z6+mE1ikP2jUXw+j42Pf1XTYED2Rni5f95npYeuwMDQA=="],

    "@babel/generator": ["@babel/generator@7.29.1", "", { "dependencies": { "@babel/parser": "^7.29.0", "@babel/types": "^7.29.0", "@jridgewell/gen-mapping": "^0.3.12", "@jridgewell/trace-mapping": "^0.3.28", "jsesc": "^3.0.2" } }, "sha512-qsaF+9Qcm2Qv8SRIMMscAvG4O3lJ0F1GuMo5HR/Bp02LopNgnZBC/EkbevHFeGs4ls/oPz9v+Bsmzbkbe+0dUw=="],

    "@babel/helper-annotate-as-pure": ["@babel/helper-annotate-as-pure@7.27.3", "", { "dependencies": { "@babel/types": "^7.27.3" } }, "sha512-fXSwMQqitTGeHLBC08Eq5yXz2m37E4pJX1qAU1+2cNedz/ifv/bVXft90VeSav5nFO61EcNgwr0aJxbyPaWBPg=="],

    "@babel/helper-compilation-targets": ["@babel/helper-compilation-targets@7.28.6", "", { "dependencies": { "@babel/compat-data": "^7.28.6", "@babel/helper-validator-option": "^7.27.1", "browserslist": "^4.24.0", "lru-cache": "^5.1.1", "semver": "^6.3.1" } }, "sha512-JYtls3hqi15fcx5GaSNL7SCTJ2MNmjrkHXg4FSpOA/grxK8KwyZ5bubHsCq8FXCkua6xhuaaBit+3b7+VZRfcA=="],

    "@babel/helper-create-class-features-plugin": ["@babel/helper-create-class-features-plugin@7.28.6", "", { "dependencies": { "@babel/helper-annotate-as-pure": "^7.27.3", "@babel/helper-member-expression-to-functions": "^7.28.5", "@babel/helper-optimise-call-expression": "^7.27.1", "@babel/helper-replace-supers": "^7.28.6", "@babel/helper-skip-transparent-expression-wrappers": "^7.27.1", "@babel/traverse": "^7.28.6", "semver": "^6.3.1" }, "peerDependencies": { "@babel/core": "^7.0.0" } }, "sha512-dTOdvsjnG3xNT9Y0AUg1wAl38y+4Rl4sf9caSQZOXdNqVn+H+HbbJ4IyyHaIqNR6SW9oJpA/RuRjsjCw2IdIow=="],

    "@babel/helper-globals": ["@babel/helper-globals@7.28.0", "", {}, "sha512-+W6cISkXFa1jXsDEdYA8HeevQT/FULhxzR99pxphltZcVaugps53THCeiWA8SguxxpSp3gKPiuYfSWopkLQ4hw=="],

    "@babel/helper-member-expression-to-functions": ["@babel/helper-member-expression-to-functions@7.28.5", "", { "dependencies": { "@babel/traverse": "^7.28.5", "@babel/types": "^7.28.5" } }, "sha512-cwM7SBRZcPCLgl8a7cY0soT1SptSzAlMH39vwiRpOQkJlh53r5hdHwLSCZpQdVLT39sZt+CRpNwYG4Y2v77atg=="],

    "@babel/helper-module-imports": ["@babel/helper-module-imports@7.28.6", "", { "dependencies": { "@babel/traverse": "^7.28.6", "@babel/types": "^7.28.6" } }, "sha512-l5XkZK7r7wa9LucGw9LwZyyCUscb4x37JWTPz7swwFE/0FMQAGpiWUZn8u9DzkSBWEcK25jmvubfpw2dnAMdbw=="],

    "@babel/helper-module-transforms": ["@babel/helper-module-transforms@7.28.6", "", { "dependencies": { "@babel/helper-module-imports": "^7.28.6", "@babel/helper-validator-identifier": "^7.28.5", "@babel/traverse": "^7.28.6" }, "peerDependencies": { "@babel/core": "^7.0.0" } }, "sha512-67oXFAYr2cDLDVGLXTEABjdBJZ6drElUSI7WKp70NrpyISso3plG9SAGEF6y7zbha/wOzUByWWTJvEDVNIUGcA=="],

    "@babel/helper-optimise-call-expression": ["@babel/helper-optimise-call-expression@7.27.1", "", { "dependencies": { "@babel/types": "^7.27.1" } }, "sha512-URMGH08NzYFhubNSGJrpUEphGKQwMQYBySzat5cAByY1/YgIRkULnIy3tAMeszlL/so2HbeilYloUmSpd7GdVw=="],

    "@babel/helper-plugin-utils": ["@babel/helper-plugin-utils@7.28.6", "", {}, "sha512-S9gzZ/bz83GRysI7gAD4wPT/AI3uCnY+9xn+Mx/KPs2JwHJIz1W8PZkg2cqyt3RNOBM8ejcXhV6y8Og7ly/Dug=="],

    "@babel/helper-replace-supers": ["@babel/helper-replace-supers@7.28.6", "", { "dependencies": { "@babel/helper-member-expression-to-functions": "^7.28.5", "@babel/helper-optimise-call-expression": "^7.27.1", "@babel/traverse": "^7.28.6" }, "peerDependencies": { "@babel/core": "^7.0.0" } }, "sha512-mq8e+laIk94/yFec3DxSjCRD2Z0TAjhVbEJY3UQrlwVo15Lmt7C2wAUbK4bjnTs4APkwsYLTahXRraQXhb1WCg=="],

    "@babel/helper-skip-transparent-expression-wrappers": ["@babel/helper-skip-transparent-expression-wrappers@7.27.1", "", { "dependencies": { "@babel/traverse": "^7.27.1", "@babel/types": "^7.27.1" } }, "sha512-Tub4ZKEXqbPjXgWLl2+3JpQAYBJ8+ikpQ2Ocj/q/r0LwE3UhENh7EUabyHjz2kCEsrRY83ew2DQdHluuiDQFzg=="],

    "@babel/helper-string-parser": ["@babel/helper-string-parser@8.0.0-rc.3", "", {}, "sha512-AmwWFx1m8G/a5cXkxLxTiWl+YEoWuoFLUCwqMlNuWO1tqAYITQAbCRPUkyBHv1VOFgfjVOqEj6L3u15J5ZCzTA=="],

    "@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@8.0.0-rc.2", "", {}, "sha512-xExUBkuXWJjVuIbO7z6q7/BA9bgfJDEhVL0ggrggLMbg0IzCUWGT1hZGE8qUH7Il7/RD/a6cZ3AAFrrlp1LF/A=="],

    "@babel/helper-validator-option": ["@babel/helper-validator-option@7.27.1", "", {}, "sha512-YvjJow9FxbhFFKDSuFnVCe2WxXk1zWc22fFePVNEaWJEu8IrZVlda6N0uHwzZrUM1il7NC9Mlp4MaJYbYd9JSg=="],

    "@babel/helpers": ["@babel/helpers@7.29.2", "", { "dependencies": { "@babel/template": "^7.28.6", "@babel/types": "^7.29.0" } }, "sha512-HoGuUs4sCZNezVEKdVcwqmZN8GoHirLUcLaYVNBK2J0DadGtdcqgr3BCbvH8+XUo4NGjNl3VOtSjEKNzqfFgKw=="],

    "@babel/parser": ["@babel/parser@8.0.0-rc.2", "", { "dependencies": { "@babel/types": "^8.0.0-rc.2" }, "bin": "./bin/babel-parser.js" }, "sha512-29AhEtcq4x8Dp3T72qvUMZHx0OMXCj4Jy/TEReQa+KWLln524Cj1fWb3QFi0l/xSpptQBR6y9RNEXuxpFvwiUQ=="],

    "@babel/plugin-proposal-decorators": ["@babel/plugin-proposal-decorators@7.29.0", "", { "dependencies": { "@babel/helper-create-class-features-plugin": "^7.28.6", "@babel/helper-plugin-utils": "^7.28.6", "@babel/plugin-syntax-decorators": "^7.28.6" }, "peerDependencies": { "@babel/core": "^7.0.0-0" } }, "sha512-CVBVv3VY/XRMxRYq5dwr2DS7/MvqPm23cOCjbwNnVrfOqcWlnefua1uUs0sjdKOGjvPUG633o07uWzJq4oI6dA=="],

    "@babel/plugin-syntax-decorators": ["@babel/plugin-syntax-decorators@7.28.6", "", { "dependencies": { "@babel/helper-plugin-utils": "^7.28.6" }, "peerDependencies": { "@babel/core": "^7.0.0-0" } }, "sha512-71EYI0ONURHJBL4rSFXnITXqXrrY8q4P0q006DPfN+Rk+ASM+++IBXem/ruokgBZR8YNEWZ8R6B+rCb8VcUTqA=="],

    "@babel/plugin-syntax-import-attributes": ["@babel/plugin-syntax-import-attributes@7.28.6", "", { "dependencies": { "@babel/helper-plugin-utils": "^7.28.6" }, "peerDependencies": { "@babel/core": "^7.0.0-0" } }, "sha512-jiLC0ma9XkQT3TKJ9uYvlakm66Pamywo+qwL+oL8HJOvc6TWdZXVfhqJr8CCzbSGUAbDOzlGHJC1U+vRfLQDvw=="],

    "@babel/plugin-syntax-import-meta": ["@babel/plugin-syntax-import-meta@7.10.4", "", { "dependencies": { "@babel/helper-plugin-utils": "^7.10.4" }, "peerDependencies": { "@babel/core": "^7.0.0-0" } }, "sha512-Yqfm+XDx0+Prh3VSeEQCPU81yC+JWZ2pDPFSS4ZdpfZhp4MkFMaDC1UqseovEKwSUpnIL7+vK+Clp7bfh0iD7g=="],

    "@babel/plugin-syntax-jsx": ["@babel/plugin-syntax-jsx@7.28.6", "", { "dependencies": { "@babel/helper-plugin-utils": "^7.28.6" }, "peerDependencies": { "@babel/core": "^7.0.0-0" } }, "sha512-wgEmr06G6sIpqr8YDwA2dSRTE3bJ+V0IfpzfSY3Lfgd7YWOaAdlykvJi13ZKBt8cZHfgH1IXN+CL656W3uUa4w=="],

    "@babel/plugin-syntax-typescript": ["@babel/plugin-syntax-typescript@7.28.6", "", { "dependencies": { "@babel/helper-plugin-utils": "^7.28.6" }, "peerDependencies": { "@babel/core": "^7.0.0-0" } }, "sha512-+nDNmQye7nlnuuHDboPbGm00Vqg3oO8niRRL27/4LYHUsHYh0zJ1xWOz0uRwNFmM1Avzk8wZbc6rdiYhomzv/A=="],

    "@babel/plugin-transform-react-jsx-self": ["@babel/plugin-transform-react-jsx-self@7.27.1", "", { "dependencies": { "@babel/helper-plugin-utils": "^7.27.1" }, "peerDependencies": { "@babel/core": "^7.0.0-0" } }, "sha512-6UzkCs+ejGdZ5mFFC/OCUrv028ab2fp1znZmCZjAOBKiBK2jXD1O+BPSfX8X2qjJ75fZBMSnQn3Rq2mrBJK2mw=="],

    "@babel/plugin-transform-react-jsx-source": ["@babel/plugin-transform-react-jsx-source@7.27.1", "", { "dependencies": { "@babel/helper-plugin-utils": "^7.27.1" }, "peerDependencies": { "@babel/core": "^7.0.0-0" } }, "sha512-zbwoTsBruTeKB9hSq73ha66iFeJHuaFkUbwvqElnygoNbj/jHRsSeokowZFN3CZ64IvEqcmmkVe89OPXc7ldAw=="],

    "@babel/plugin-transform-typescript": ["@babel/plugin-transform-typescript@7.28.6", "", { "dependencies": { "@babel/helper-annotate-as-pure": "^7.27.3", "@babel/helper-create-class-features-plugin": "^7.28.6", "@babel/helper-plugin-utils": "^7.28.6", "@babel/helper-skip-transparent-expression-wrappers": "^7.27.1", "@babel/plugin-syntax-typescript": "^7.28.6" }, "peerDependencies": { "@babel/core": "^7.0.0-0" } }, "sha512-0YWL2RFxOqEm9Efk5PvreamxPME8OyY0wM5wh5lHjF+VtVhdneCWGzZeSqzOfiobVqQaNCd2z0tQvnI9DaPWPw=="],

    "@babel/template": ["@babel/template@7.28.6", "", { "dependencies": { "@babel/code-frame": "^7.28.6", "@babel/parser": "^7.28.6", "@babel/types": "^7.28.6" } }, "sha512-YA6Ma2KsCdGb+WC6UpBVFJGXL58MDA6oyONbjyF/+5sBgxY/dwkhLogbMT2GXXyU84/IhRw/2D1Os1B/giz+BQ=="],

    "@babel/traverse": ["@babel/traverse@7.29.0", "", { "dependencies": { "@babel/code-frame": "^7.29.0", "@babel/generator": "^7.29.0", "@babel/helper-globals": "^7.28.0", "@babel/parser": "^7.29.0", "@babel/template": "^7.28.6", "@babel/types": "^7.29.0", "debug": "^4.3.1" } }, "sha512-4HPiQr0X7+waHfyXPZpWPfWL/J7dcN1mx9gL6WdQVMbPnF3+ZhSMs8tCxN7oHddJE9fhNE7+lxdnlyemKfJRuA=="],

    "@babel/types": ["@babel/types@8.0.0-rc.2", "", { "dependencies": { "@babel/helper-string-parser": "^8.0.0-rc.2", "@babel/helper-validator-identifier": "^8.0.0-rc.2" } }, "sha512-91gAaWRznDwSX4E2tZ1YjBuIfnQVOFDCQ2r0Toby0gu4XEbyF623kXLMA8d4ZbCu+fINcrudkmEcwSUHgDDkNw=="],

    "@biomejs/biome": ["@biomejs/biome@2.4.7", "", { "optionalDependencies": { "@biomejs/cli-darwin-arm64": "2.4.7", "@biomejs/cli-darwin-x64": "2.4.7", "@biomejs/cli-linux-arm64": "2.4.7", "@biomejs/cli-linux-arm64-musl": "2.4.7", "@biomejs/cli-linux-x64": "2.4.7", "@biomejs/cli-linux-x64-musl": "2.4.7", "@biomejs/cli-win32-arm64": "2.4.7", "@biomejs/cli-win32-x64": "2.4.7" }, "bin": { "biome": "bin/biome" } }, "sha512-vXrgcmNGZ4lpdwZSpMf1hWw1aWS6B+SyeSYKTLrNsiUsAdSRN0J4d/7mF3ogJFbIwFFSOL3wT92Zzxia/d5/ng=="],

    "@biomejs/cli-darwin-arm64": ["@biomejs/cli-darwin-arm64@2.4.7", "", { "os": "darwin", "cpu": "arm64" }, "sha512-Oo0cF5mHzmvDmTXw8XSjhCia8K6YrZnk7aCS54+/HxyMdZMruMO3nfpDsrlar/EQWe41r1qrwKiCa2QDYHDzWA=="],

    "@biomejs/cli-darwin-x64": ["@biomejs/cli-darwin-x64@2.4.7", "", { "os": "darwin", "cpu": "x64" }, "sha512-I+cOG3sd/7HdFtvDSnF9QQPrWguUH7zrkIMMykM3PtfWU9soTcS2yRb9Myq6MHmzbeCT08D1UmY+BaiMl5CcoQ=="],

    "@biomejs/cli-linux-arm64": ["@biomejs/cli-linux-arm64@2.4.7", "", { "os": "linux", "cpu": "arm64" }, "sha512-om6FugwmibzfP/6ALj5WRDVSND4H2G9X0nkI1HZpp2ySf9lW2j0X68oQSaHEnls6666oy4KDsc5RFjT4m0kV0w=="],

    "@biomejs/cli-linux-arm64-musl": ["@biomejs/cli-linux-arm64-musl@2.4.7", "", { "os": "linux", "cpu": "arm64" }, "sha512-I2NvM9KPb09jWml93O2/5WMfNR7Lee5Latag1JThDRMURVhPX74p9UDnyTw3Ae6cE1DgXfw7sqQgX7rkvpc0vw=="],

    "@biomejs/cli-linux-x64": ["@biomejs/cli-linux-x64@2.4.7", "", { "os": "linux", "cpu": "x64" }, "sha512-bV8/uo2Tj+gumnk4sUdkerWyCPRabaZdv88IpbmDWARQQoA/Q0YaqPz1a+LSEDIL7OfrnPi9Hq1Llz4ZIGyIQQ=="],

    "@biomejs/cli-linux-x64-musl": ["@biomejs/cli-linux-x64-musl@2.4.7", "", { "os": "linux", "cpu": "x64" }, "sha512-00kx4YrBMU8374zd2wHuRV5wseh0rom5HqRND+vDldJPrWwQw+mzd/d8byI9hPx926CG+vWzq6AeiT7Yi5y59g=="],

    "@biomejs/cli-win32-arm64": ["@biomejs/cli-win32-arm64@2.4.7", "", { "os": "win32", "cpu": "arm64" }, "sha512-hOUHBMlFCvDhu3WCq6vaBoG0dp0LkWxSEnEEsxxXvOa9TfT6ZBnbh72A/xBM7CBYB7WgwqboetzFEVDnMxelyw=="],

    "@biomejs/cli-win32-x64": ["@biomejs/cli-win32-x64@2.4.7", "", { "os": "win32", "cpu": "x64" }, "sha512-qEpGjSkPC3qX4ycbMUthXvi9CkRq7kZpkqMY1OyhmYlYLnANnooDQ7hDerM8+0NJ+DZKVnsIc07h30XOpt7LtQ=="],

    "@bomb.sh/tab": ["@bomb.sh/tab@0.0.14", "", { "peerDependencies": { "cac": "^6.7.14", "citty": "^0.1.6 || ^0.2.0", "commander": "^13.1.0" }, "optionalPeers": ["cac", "citty", "commander"], "bin": { "tab": "dist/bin/cli.mjs" } }, "sha512-cHMk2LI430MVoX1unTt9oK1iZzQS4CYDz97MSxKLNErW69T43Z2QLFTpdS/3jVOIKrIADWfuxQ+nQNJkNV7E4w=="],

    "@capsizecss/unpack": ["@capsizecss/unpack@4.0.0", "", { "dependencies": { "fontkitten": "^1.0.0" } }, "sha512-VERIM64vtTP1C4mxQ5thVT9fK0apjPFobqybMtA1UdUujWka24ERHbRHFGmpbbhp73MhV+KSsHQH9C6uOTdEQA=="],

    "@clack/core": ["@clack/core@1.1.0", "", { "dependencies": { "sisteransi": "^1.0.5" } }, "sha512-SVcm4Dqm2ukn64/8Gub2wnlA5nS2iWJyCkdNHcvNHPIeBTGojpdJ+9cZKwLfmqy7irD4N5qLteSilJlE0WLAtA=="],

    "@clack/prompts": ["@clack/prompts@1.1.0", "", { "dependencies": { "@clack/core": "1.1.0", "sisteransi": "^1.0.5" } }, "sha512-pkqbPGtohJAvm4Dphs2M8xE29ggupihHdy1x84HNojZuMtFsHiUlRvqD24tM2+XmI+61LlfNceM3Wr7U5QES5g=="],

    "@cloudflare/kv-asset-handler": ["@cloudflare/kv-asset-handler@0.4.2", "", {}, "sha512-SIOD2DxrRRwQ+jgzlXCqoEFiKOFqaPjhnNTGKXSRLvp1HiOvapLaFG2kEr9dYQTYe8rKrd9uvDUzmAITeNyaHQ=="],

    "@dxup/nuxt": ["@dxup/nuxt@0.4.0", "", { "dependencies": { "@dxup/unimport": "^0.1.2", "@nuxt/kit": "^4.2.2", "chokidar": "^5.0.0", "pathe": "^2.0.3", "tinyglobby": "^0.2.15" }, "peerDependencies": { "typescript": "*" } }, "sha512-28LDotpr9G2knUse3cQYsOo6NJq5yhABv4ByRVRYJUmzf9Q31DI7rpRek4POlKy1aAcYyKgu5J2616pyqLohYg=="],

    "@dxup/unimport": ["@dxup/unimport@0.1.2", "", {}, "sha512-/B8YJGPzaYq1NbsQmwgP8EZqg40NpTw4ZB3suuI0TplbxKHeK94jeaawLmVhCv+YwUnOpiWEz9U6SeThku/8JQ=="],

    "@emmetio/abbreviation": ["@emmetio/abbreviation@2.3.3", "", { "dependencies": { "@emmetio/scanner": "^1.0.4" } }, "sha512-mgv58UrU3rh4YgbE/TzgLQwJ3pFsHHhCLqY20aJq+9comytTXUDNGG/SMtSeMJdkpxgXSXunBGLD8Boka3JyVA=="],

    "@emmetio/css-abbreviation": ["@emmetio/css-abbreviation@2.1.8", "", { "dependencies": { "@emmetio/scanner": "^1.0.4" } }, "sha512-s9yjhJ6saOO/uk1V74eifykk2CBYi01STTK3WlXWGOepyKa23ymJ053+DNQjpFcy1ingpaO7AxCcwLvHFY9tuw=="],

    "@emmetio/css-parser": ["@emmetio/css-parser@0.4.1", "", { "dependencies": { "@emmetio/stream-reader": "^2.2.0", "@emmetio/stream-reader-utils": "^0.1.0" } }, "sha512-2bC6m0MV/voF4CTZiAbG5MWKbq5EBmDPKu9Sb7s7nVcEzNQlrZP6mFFFlIaISM8X6514H9shWMme1fCm8cWAfQ=="],

    "@emmetio/html-matcher": ["@emmetio/html-matcher@1.3.0", "", { "dependencies": { "@emmetio/scanner": "^1.0.0" } }, "sha512-NTbsvppE5eVyBMuyGfVu2CRrLvo7J4YHb6t9sBFLyY03WYhXET37qA4zOYUjBWFCRHO7pS1B9khERtY0f5JXPQ=="],

    "@emmetio/scanner": ["@emmetio/scanner@1.0.4", "", {}, "sha512-IqRuJtQff7YHHBk4G8YZ45uB9BaAGcwQeVzgj/zj8/UdOhtQpEIupUhSk8dys6spFIWVZVeK20CzGEnqR5SbqA=="],

    "@emmetio/stream-reader": ["@emmetio/stream-reader@2.2.0", "", {}, "sha512-fXVXEyFA5Yv3M3n8sUGT7+fvecGrZP4k6FnWWMSZVQf69kAq0LLpaBQLGcPR30m3zMmKYhECP4k/ZkzvhEW5kw=="],

    "@emmetio/stream-reader-utils": ["@emmetio/stream-reader-utils@0.1.0", "", {}, "sha512-ZsZ2I9Vzso3Ho/pjZFsmmZ++FWeEd/txqybHTm4OgaZzdS8V9V/YYWQwg5TC38Z7uLWUV1vavpLLbjJtKubR1A=="],

    "@emnapi/core": ["@emnapi/core@1.9.0", "", { "dependencies": { "@emnapi/wasi-threads": "1.2.0", "tslib": "^2.4.0" } }, "sha512-0DQ98G9ZQZOxfUcQn1waV2yS8aWdZ6kJMbYCJB3oUBecjWYO1fqJ+a1DRfPF3O5JEkwqwP1A9QEN/9mYm2Yd0w=="],

    "@emnapi/runtime": ["@emnapi/runtime@1.9.0", "", { "dependencies": { "tslib": "^2.4.0" } }, "sha512-QN75eB0IH2ywSpRpNddCRfQIhmJYBCJ1x5Lb3IscKAL8bMnVAKnRg8dCoXbHzVLLH7P38N2Z3mtulB7W0J0FKw=="],

    "@emnapi/wasi-threads": ["@emnapi/wasi-threads@1.2.0", "", { "dependencies": { "tslib": "^2.4.0" } }, "sha512-N10dEJNSsUx41Z6pZsXU8FjPjpBEplgH24sfkmITrBED1/U2Esum9F3lfLrMjKHHjmi557zQn7kR9R+XWXu5Rg=="],

    "@esbuild/aix-ppc64": ["@esbuild/aix-ppc64@0.27.4", "", { "os": "aix", "cpu": "ppc64" }, "sha512-cQPwL2mp2nSmHHJlCyoXgHGhbEPMrEEU5xhkcy3Hs/O7nGZqEpZ2sUtLaL9MORLtDfRvVl2/3PAuEkYZH0Ty8Q=="],

    "@esbuild/android-arm": ["@esbuild/android-arm@0.27.4", "", { "os": "android", "cpu": "arm" }, "sha512-X9bUgvxiC8CHAGKYufLIHGXPJWnr0OCdR0anD2e21vdvgCI8lIfqFbnoeOz7lBjdrAGUhqLZLcQo6MLhTO2DKQ=="],

    "@esbuild/android-arm64": ["@esbuild/android-arm64@0.27.4", "", { "os": "android", "cpu": "arm64" }, "sha512-gdLscB7v75wRfu7QSm/zg6Rx29VLdy9eTr2t44sfTW7CxwAtQghZ4ZnqHk3/ogz7xao0QAgrkradbBzcqFPasw=="],

    "@esbuild/android-x64": ["@esbuild/android-x64@0.27.4", "", { "os": "android", "cpu": "x64" }, "sha512-PzPFnBNVF292sfpfhiyiXCGSn9HZg5BcAz+ivBuSsl6Rk4ga1oEXAamhOXRFyMcjwr2DVtm40G65N3GLeH1Lvw=="],

    "@esbuild/darwin-arm64": ["@esbuild/darwin-arm64@0.27.4", "", { "os": "darwin", "cpu": "arm64" }, "sha512-b7xaGIwdJlht8ZFCvMkpDN6uiSmnxxK56N2GDTMYPr2/gzvfdQN8rTfBsvVKmIVY/X7EM+/hJKEIbbHs9oA4tQ=="],

    "@esbuild/darwin-x64": ["@esbuild/darwin-x64@0.27.4", "", { "os": "darwin", "cpu": "x64" }, "sha512-sR+OiKLwd15nmCdqpXMnuJ9W2kpy0KigzqScqHI3Hqwr7IXxBp3Yva+yJwoqh7rE8V77tdoheRYataNKL4QrPw=="],

    "@esbuild/freebsd-arm64": ["@esbuild/freebsd-arm64@0.27.4", "", { "os": "freebsd", "cpu": "arm64" }, "sha512-jnfpKe+p79tCnm4GVav68A7tUFeKQwQyLgESwEAUzyxk/TJr4QdGog9sqWNcUbr/bZt/O/HXouspuQDd9JxFSw=="],

    "@esbuild/freebsd-x64": ["@esbuild/freebsd-x64@0.27.4", "", { "os": "freebsd", "cpu": "x64" }, "sha512-2kb4ceA/CpfUrIcTUl1wrP/9ad9Atrp5J94Lq69w7UwOMolPIGrfLSvAKJp0RTvkPPyn6CIWrNy13kyLikZRZQ=="],

    "@esbuild/linux-arm": ["@esbuild/linux-arm@0.27.4", "", { "os": "linux", "cpu": "arm" }, "sha512-aBYgcIxX/wd5n2ys0yESGeYMGF+pv6g0DhZr3G1ZG4jMfruU9Tl1i2Z+Wnj9/KjGz1lTLCcorqE2viePZqj4Eg=="],

    "@esbuild/linux-arm64": ["@esbuild/linux-arm64@0.27.4", "", { "os": "linux", "cpu": "arm64" }, "sha512-7nQOttdzVGth1iz57kxg9uCz57dxQLHWxopL6mYuYthohPKEK0vU0C3O21CcBK6KDlkYVcnDXY099HcCDXd9dA=="],

    "@esbuild/linux-ia32": ["@esbuild/linux-ia32@0.27.4", "", { "os": "linux", "cpu": "ia32" }, "sha512-oPtixtAIzgvzYcKBQM/qZ3R+9TEUd1aNJQu0HhGyqtx6oS7qTpvjheIWBbes4+qu1bNlo2V4cbkISr8q6gRBFA=="],

    "@esbuild/linux-loong64": ["@esbuild/linux-loong64@0.27.4", "", { "os": "linux", "cpu": "none" }, "sha512-8mL/vh8qeCoRcFH2nM8wm5uJP+ZcVYGGayMavi8GmRJjuI3g1v6Z7Ni0JJKAJW+m0EtUuARb6Lmp4hMjzCBWzA=="],

    "@esbuild/linux-mips64el": ["@esbuild/linux-mips64el@0.27.4", "", { "os": "linux", "cpu": "none" }, "sha512-1RdrWFFiiLIW7LQq9Q2NES+HiD4NyT8Itj9AUeCl0IVCA459WnPhREKgwrpaIfTOe+/2rdntisegiPWn/r/aAw=="],

    "@esbuild/linux-ppc64": ["@esbuild/linux-ppc64@0.27.4", "", { "os": "linux", "cpu": "ppc64" }, "sha512-tLCwNG47l3sd9lpfyx9LAGEGItCUeRCWeAx6x2Jmbav65nAwoPXfewtAdtbtit/pJFLUWOhpv0FpS6GQAmPrHA=="],

    "@esbuild/linux-riscv64": ["@esbuild/linux-riscv64@0.27.4", "", { "os": "linux", "cpu": "none" }, "sha512-BnASypppbUWyqjd1KIpU4AUBiIhVr6YlHx/cnPgqEkNoVOhHg+YiSVxM1RLfiy4t9cAulbRGTNCKOcqHrEQLIw=="],

    "@esbuild/linux-s390x": ["@esbuild/linux-s390x@0.27.4", "", { "os": "linux", "cpu": "s390x" }, "sha512-+eUqgb/Z7vxVLezG8bVB9SfBie89gMueS+I0xYh2tJdw3vqA/0ImZJ2ROeWwVJN59ihBeZ7Tu92dF/5dy5FttA=="],

    "@esbuild/linux-x64": ["@esbuild/linux-x64@0.27.4", "", { "os": "linux", "cpu": "x64" }, "sha512-S5qOXrKV8BQEzJPVxAwnryi2+Iq5pB40gTEIT69BQONqR7JH1EPIcQ/Uiv9mCnn05jff9umq/5nqzxlqTOg9NA=="],

    "@esbuild/netbsd-arm64": ["@esbuild/netbsd-arm64@0.27.4", "", { "os": "none", "cpu": "arm64" }, "sha512-xHT8X4sb0GS8qTqiwzHqpY00C95DPAq7nAwX35Ie/s+LO9830hrMd3oX0ZMKLvy7vsonee73x0lmcdOVXFzd6Q=="],

    "@esbuild/netbsd-x64": ["@esbuild/netbsd-x64@0.27.4", "", { "os": "none", "cpu": "x64" }, "sha512-RugOvOdXfdyi5Tyv40kgQnI0byv66BFgAqjdgtAKqHoZTbTF2QqfQrFwa7cHEORJf6X2ht+l9ABLMP0dnKYsgg=="],

    "@esbuild/openbsd-arm64": ["@esbuild/openbsd-arm64@0.27.4", "", { "os": "openbsd", "cpu": "arm64" }, "sha512-2MyL3IAaTX+1/qP0O1SwskwcwCoOI4kV2IBX1xYnDDqthmq5ArrW94qSIKCAuRraMgPOmG0RDTA74mzYNQA9ow=="],

    "@esbuild/openbsd-x64": ["@esbuild/openbsd-x64@0.27.4", "", { "os": "openbsd", "cpu": "x64" }, "sha512-u8fg/jQ5aQDfsnIV6+KwLOf1CmJnfu1ShpwqdwC0uA7ZPwFws55Ngc12vBdeUdnuWoQYx/SOQLGDcdlfXhYmXQ=="],

    "@esbuild/openharmony-arm64": ["@esbuild/openharmony-arm64@0.27.4", "", { "os": "none", "cpu": "arm64" }, "sha512-JkTZrl6VbyO8lDQO3yv26nNr2RM2yZzNrNHEsj9bm6dOwwu9OYN28CjzZkH57bh4w0I2F7IodpQvUAEd1mbWXg=="],

    "@esbuild/sunos-x64": ["@esbuild/sunos-x64@0.27.4", "", { "os": "sunos", "cpu": "x64" }, "sha512-/gOzgaewZJfeJTlsWhvUEmUG4tWEY2Spp5M20INYRg2ZKl9QPO3QEEgPeRtLjEWSW8FilRNacPOg8R1uaYkA6g=="],

    "@esbuild/win32-arm64": ["@esbuild/win32-arm64@0.27.4", "", { "os": "win32", "cpu": "arm64" }, "sha512-Z9SExBg2y32smoDQdf1HRwHRt6vAHLXcxD2uGgO/v2jK7Y718Ix4ndsbNMU/+1Qiem9OiOdaqitioZwxivhXYg=="],

    "@esbuild/win32-ia32": ["@esbuild/win32-ia32@0.27.4", "", { "os": "win32", "cpu": "ia32" }, "sha512-DAyGLS0Jz5G5iixEbMHi5KdiApqHBWMGzTtMiJ72ZOLhbu/bzxgAe8Ue8CTS3n3HbIUHQz/L51yMdGMeoxXNJw=="],

    "@esbuild/win32-x64": ["@esbuild/win32-x64@0.27.4", "", { "os": "win32", "cpu": "x64" }, "sha512-+knoa0BDoeXgkNvvV1vvbZX4+hizelrkwmGJBdT17t8FNPwG2lKemmuMZlmaNQ3ws3DKKCxpb4zRZEIp3UxFCg=="],

    "@img/colour": ["@img/colour@1.1.0", "", {}, "sha512-Td76q7j57o/tLVdgS746cYARfSyxk8iEfRxewL9h4OMzYhbW4TAcppl0mT4eyqXddh6L/jwoM75mo7ixa/pCeQ=="],

    "@img/sharp-darwin-arm64": ["@img/sharp-darwin-arm64@0.34.5", "", { "optionalDependencies": { "@img/sharp-libvips-darwin-arm64": "1.2.4" }, "os": "darwin", "cpu": "arm64" }, "sha512-imtQ3WMJXbMY4fxb/Ndp6HBTNVtWCUI0WdobyheGf5+ad6xX8VIDO8u2xE4qc/fr08CKG/7dDseFtn6M6g/r3w=="],

    "@img/sharp-darwin-x64": ["@img/sharp-darwin-x64@0.34.5", "", { "optionalDependencies": { "@img/sharp-libvips-darwin-x64": "1.2.4" }, "os": "darwin", "cpu": "x64" }, "sha512-YNEFAF/4KQ/PeW0N+r+aVVsoIY0/qxxikF2SWdp+NRkmMB7y9LBZAVqQ4yhGCm/H3H270OSykqmQMKLBhBJDEw=="],

    "@img/sharp-libvips-darwin-arm64": ["@img/sharp-libvips-darwin-arm64@1.2.4", "", { "os": "darwin", "cpu": "arm64" }, "sha512-zqjjo7RatFfFoP0MkQ51jfuFZBnVE2pRiaydKJ1G/rHZvnsrHAOcQALIi9sA5co5xenQdTugCvtb1cuf78Vf4g=="],

    "@img/sharp-libvips-darwin-x64": ["@img/sharp-libvips-darwin-x64@1.2.4", "", { "os": "darwin", "cpu": "x64" }, "sha512-1IOd5xfVhlGwX+zXv2N93k0yMONvUlANylbJw1eTah8K/Jtpi15KC+WSiaX/nBmbm2HxRM1gZ0nSdjSsrZbGKg=="],

    "@img/sharp-libvips-linux-arm": ["@img/sharp-libvips-linux-arm@1.2.4", "", { "os": "linux", "cpu": "arm" }, "sha512-bFI7xcKFELdiNCVov8e44Ia4u2byA+l3XtsAj+Q8tfCwO6BQ8iDojYdvoPMqsKDkuoOo+X6HZA0s0q11ANMQ8A=="],

    "@img/sharp-libvips-linux-arm64": ["@img/sharp-libvips-linux-arm64@1.2.4", "", { "os": "linux", "cpu": "arm64" }, "sha512-excjX8DfsIcJ10x1Kzr4RcWe1edC9PquDRRPx3YVCvQv+U5p7Yin2s32ftzikXojb1PIFc/9Mt28/y+iRklkrw=="],

    "@img/sharp-libvips-linux-ppc64": ["@img/sharp-libvips-linux-ppc64@1.2.4", "", { "os": "linux", "cpu": "ppc64" }, "sha512-FMuvGijLDYG6lW+b/UvyilUWu5Ayu+3r2d1S8notiGCIyYU/76eig1UfMmkZ7vwgOrzKzlQbFSuQfgm7GYUPpA=="],

    "@img/sharp-libvips-linux-riscv64": ["@img/sharp-libvips-linux-riscv64@1.2.4", "", { "os": "linux", "cpu": "none" }, "sha512-oVDbcR4zUC0ce82teubSm+x6ETixtKZBh/qbREIOcI3cULzDyb18Sr/Wcyx7NRQeQzOiHTNbZFF1UwPS2scyGA=="],

    "@img/sharp-libvips-linux-s390x": ["@img/sharp-libvips-linux-s390x@1.2.4", "", { "os": "linux", "cpu": "s390x" }, "sha512-qmp9VrzgPgMoGZyPvrQHqk02uyjA0/QrTO26Tqk6l4ZV0MPWIW6LTkqOIov+J1yEu7MbFQaDpwdwJKhbJvuRxQ=="],

    "@img/sharp-libvips-linux-x64": ["@img/sharp-libvips-linux-x64@1.2.4", "", { "os": "linux", "cpu": "x64" }, "sha512-tJxiiLsmHc9Ax1bz3oaOYBURTXGIRDODBqhveVHonrHJ9/+k89qbLl0bcJns+e4t4rvaNBxaEZsFtSfAdquPrw=="],

    "@img/sharp-libvips-linuxmusl-arm64": ["@img/sharp-libvips-linuxmusl-arm64@1.2.4", "", { "os": "linux", "cpu": "arm64" }, "sha512-FVQHuwx1IIuNow9QAbYUzJ+En8KcVm9Lk5+uGUQJHaZmMECZmOlix9HnH7n1TRkXMS0pGxIJokIVB9SuqZGGXw=="],

    "@img/sharp-libvips-linuxmusl-x64": ["@img/sharp-libvips-linuxmusl-x64@1.2.4", "", { "os": "linux", "cpu": "x64" }, "sha512-+LpyBk7L44ZIXwz/VYfglaX/okxezESc6UxDSoyo2Ks6Jxc4Y7sGjpgU9s4PMgqgjj1gZCylTieNamqA1MF7Dg=="],

    "@img/sharp-linux-arm": ["@img/sharp-linux-arm@0.34.5", "", { "optionalDependencies": { "@img/sharp-libvips-linux-arm": "1.2.4" }, "os": "linux", "cpu": "arm" }, "sha512-9dLqsvwtg1uuXBGZKsxem9595+ujv0sJ6Vi8wcTANSFpwV/GONat5eCkzQo/1O6zRIkh0m/8+5BjrRr7jDUSZw=="],

    "@img/sharp-linux-arm64": ["@img/sharp-linux-arm64@0.34.5", "", { "optionalDependencies": { "@img/sharp-libvips-linux-arm64": "1.2.4" }, "os": "linux", "cpu": "arm64" }, "sha512-bKQzaJRY/bkPOXyKx5EVup7qkaojECG6NLYswgktOZjaXecSAeCWiZwwiFf3/Y+O1HrauiE3FVsGxFg8c24rZg=="],

    "@img/sharp-linux-ppc64": ["@img/sharp-linux-ppc64@0.34.5", "", { "optionalDependencies": { "@img/sharp-libvips-linux-ppc64": "1.2.4" }, "os": "linux", "cpu": "ppc64" }, "sha512-7zznwNaqW6YtsfrGGDA6BRkISKAAE1Jo0QdpNYXNMHu2+0dTrPflTLNkpc8l7MUP5M16ZJcUvysVWWrMefZquA=="],

    "@img/sharp-linux-riscv64": ["@img/sharp-linux-riscv64@0.34.5", "", { "optionalDependencies": { "@img/sharp-libvips-linux-riscv64": "1.2.4" }, "os": "linux", "cpu": "none" }, "sha512-51gJuLPTKa7piYPaVs8GmByo7/U7/7TZOq+cnXJIHZKavIRHAP77e3N2HEl3dgiqdD/w0yUfiJnII77PuDDFdw=="],

    "@img/sharp-linux-s390x": ["@img/sharp-linux-s390x@0.34.5", "", { "optionalDependencies": { "@img/sharp-libvips-linux-s390x": "1.2.4" }, "os": "linux", "cpu": "s390x" }, "sha512-nQtCk0PdKfho3eC5MrbQoigJ2gd1CgddUMkabUj+rBevs8tZ2cULOx46E7oyX+04WGfABgIwmMC0VqieTiR4jg=="],

    "@img/sharp-linux-x64": ["@img/sharp-linux-x64@0.34.5", "", { "optionalDependencies": { "@img/sharp-libvips-linux-x64": "1.2.4" }, "os": "linux", "cpu": "x64" }, "sha512-MEzd8HPKxVxVenwAa+JRPwEC7QFjoPWuS5NZnBt6B3pu7EG2Ge0id1oLHZpPJdn3OQK+BQDiw9zStiHBTJQQQQ=="],

    "@img/sharp-linuxmusl-arm64": ["@img/sharp-linuxmusl-arm64@0.34.5", "", { "optionalDependencies": { "@img/sharp-libvips-linuxmusl-arm64": "1.2.4" }, "os": "linux", "cpu": "arm64" }, "sha512-fprJR6GtRsMt6Kyfq44IsChVZeGN97gTD331weR1ex1c1rypDEABN6Tm2xa1wE6lYb5DdEnk03NZPqA7Id21yg=="],

    "@img/sharp-linuxmusl-x64": ["@img/sharp-linuxmusl-x64@0.34.5", "", { "optionalDependencies": { "@img/sharp-libvips-linuxmusl-x64": "1.2.4" }, "os": "linux", "cpu": "x64" }, "sha512-Jg8wNT1MUzIvhBFxViqrEhWDGzqymo3sV7z7ZsaWbZNDLXRJZoRGrjulp60YYtV4wfY8VIKcWidjojlLcWrd8Q=="],

    "@img/sharp-wasm32": ["@img/sharp-wasm32@0.34.5", "", { "dependencies": { "@emnapi/runtime": "^1.7.0" }, "cpu": "none" }, "sha512-OdWTEiVkY2PHwqkbBI8frFxQQFekHaSSkUIJkwzclWZe64O1X4UlUjqqqLaPbUpMOQk6FBu/HtlGXNblIs0huw=="],

    "@img/sharp-win32-arm64": ["@img/sharp-win32-arm64@0.34.5", "", { "os": "win32", "cpu": "arm64" }, "sha512-WQ3AgWCWYSb2yt+IG8mnC6Jdk9Whs7O0gxphblsLvdhSpSTtmu69ZG1Gkb6NuvxsNACwiPV6cNSZNzt0KPsw7g=="],

    "@img/sharp-win32-ia32": ["@img/sharp-win32-ia32@0.34.5", "", { "os": "win32", "cpu": "ia32" }, "sha512-FV9m/7NmeCmSHDD5j4+4pNI8Cp3aW+JvLoXcTUo0IqyjSfAZJ8dIUmijx1qaJsIiU+Hosw6xM5KijAWRJCSgNg=="],

    "@img/sharp-win32-x64": ["@img/sharp-win32-x64@0.34.5", "", { "os": "win32", "cpu": "x64" }, "sha512-+29YMsqY2/9eFEiW93eqWnuLcWcufowXewwSNIT6UwZdUUCrM3oFjMWH/Z6/TMmb4hlFenmfAVbpWeup2jryCw=="],

    "@ioredis/commands": ["@ioredis/commands@1.5.1", "", {}, "sha512-JH8ZL/ywcJyR9MmJ5BNqZllXNZQqQbnVZOqpPQqE1vHiFgAw4NHbvE0FOduNU8IX9babitBT46571OnPTT0Zcw=="],

    "@isaacs/cliui": ["@isaacs/cliui@8.0.2", "", { "dependencies": { "string-width": "^5.1.2", "string-width-cjs": "npm:string-width@^4.2.0", "strip-ansi": "^7.0.1", "strip-ansi-cjs": "npm:strip-ansi@^6.0.1", "wrap-ansi": "^8.1.0", "wrap-ansi-cjs": "npm:wrap-ansi@^7.0.0" } }, "sha512-O8jcjabXaleOG9DQ0+ARXWZBTfnP4WNAqzuiJK7ll44AmxGKv/J2M4TPjxjY3znBCfvBXFzucm1twdyFybFqEA=="],

    "@isaacs/fs-minipass": ["@isaacs/fs-minipass@4.0.1", "", { "dependencies": { "minipass": "^7.0.4" } }, "sha512-wgm9Ehl2jpeqP3zw/7mo3kRHFp5MEDhqAdwy1fTGkHAwnkGOVsgpvQhL8B5n1qlb01jV3n/bI0ZfZp5lWA1k4w=="],

    "@jridgewell/gen-mapping": ["@jridgewell/gen-mapping@0.3.13", "", { "dependencies": { "@jridgewell/sourcemap-codec": "^1.5.0", "@jridgewell/trace-mapping": "^0.3.24" } }, "sha512-2kkt/7niJ6MgEPxF0bYdQ6etZaA+fQvDcLKckhy1yIQOzaoKjBBjSj63/aLVjYE3qhRt5dvM+uUyfCg6UKCBbA=="],

    "@jridgewell/remapping": ["@jridgewell/remapping@2.3.5", "", { "dependencies": { "@jridgewell/gen-mapping": "^0.3.5", "@jridgewell/trace-mapping": "^0.3.24" } }, "sha512-LI9u/+laYG4Ds1TDKSJW2YPrIlcVYOwi2fUC6xB43lueCjgxV4lffOCZCtYFiH6TNOX+tQKXx97T4IKHbhyHEQ=="],

    "@jridgewell/resolve-uri": ["@jridgewell/resolve-uri@3.1.2", "", {}, "sha512-bRISgCIjP20/tbWSPWMEi54QVPRZExkuD9lJL+UIxUKtwVJA8wW1Trb1jMs1RFXo1CBTNZ/5hpC9QvmKWdopKw=="],

    "@jridgewell/source-map": ["@jridgewell/source-map@0.3.11", "", { "dependencies": { "@jridgewell/gen-mapping": "^0.3.5", "@jridgewell/trace-mapping": "^0.3.25" } }, "sha512-ZMp1V8ZFcPG5dIWnQLr3NSI1MiCU7UETdS/A0G8V/XWHvJv3ZsFqutJn1Y5RPmAPX6F3BiE397OqveU/9NCuIA=="],

    "@jridgewell/sourcemap-codec": ["@jridgewell/sourcemap-codec@1.5.5", "", {}, "sha512-cYQ9310grqxueWbl+WuIUIaiUaDcj7WOq5fVhEljNVgRfOUhY9fy2zTvfoqWsnebh8Sl70VScFbICvJnLKB0Og=="],

    "@jridgewell/trace-mapping": ["@jridgewell/trace-mapping@0.3.31", "", { "dependencies": { "@jridgewell/resolve-uri": "^3.1.0", "@jridgewell/sourcemap-codec": "^1.4.14" } }, "sha512-zzNR+SdQSDJzc8joaeP8QQoCQr8NuYx2dIIytl1QeBEZHJ9uW6hebsrYgbz8hJwUQao3TWCMtmfV8Nu1twOLAw=="],

    "@kwsites/file-exists": ["@kwsites/file-exists@1.1.1", "", { "dependencies": { "debug": "^4.1.1" } }, "sha512-m9/5YGR18lIwxSFDwfE3oA7bWuq9kdau6ugN4H2rJeyhFQZcG9AgSHkQtSD15a8WvTgfz9aikZMrKPHvbpqFiw=="],

    "@kwsites/promise-deferred": ["@kwsites/promise-deferred@1.1.1", "", {}, "sha512-GaHYm+c0O9MjZRu0ongGBRbinu8gVAMd2UZjji6jVmqKtZluZnptXGWhz1E8j8D2HJ3f/yMxKAUC0b+57wncIw=="],

    "@mapbox/node-pre-gyp": ["@mapbox/node-pre-gyp@2.0.3", "", { "dependencies": { "consola": "^3.2.3", "detect-libc": "^2.0.0", "https-proxy-agent": "^7.0.5", "node-fetch": "^2.6.7", "nopt": "^8.0.0", "semver": "^7.5.3", "tar": "^7.4.0" }, "bin": { "node-pre-gyp": "bin/node-pre-gyp" } }, "sha512-uwPAhccfFJlsfCxMYTwOdVfOz3xqyj8xYL3zJj8f0pb30tLohnnFPhLuqp4/qoEz8sNxe4SESZedcBojRefIzg=="],

    "@napi-rs/wasm-runtime": ["@napi-rs/wasm-runtime@1.1.1", "", { "dependencies": { "@emnapi/core": "^1.7.1", "@emnapi/runtime": "^1.7.1", "@tybys/wasm-util": "^0.10.1" } }, "sha512-p64ah1M1ld8xjWv3qbvFwHiFVWrq1yFvV4f7w+mzaqiR4IlSgkqhcRdHwsGgomwzBH51sRY4NEowLxnaBjcW/A=="],

    "@nodelib/fs.scandir": ["@nodelib/fs.scandir@2.1.5", "", { "dependencies": { "@nodelib/fs.stat": "2.0.5", "run-parallel": "^1.1.9" } }, "sha512-vq24Bq3ym5HEQm2NKCr3yXDwjc7vTsEThRDnkp2DK9p1uqLR+DHurm/NOTo0KG7HYHU7eppKZj3MyqYuMBf62g=="],

    "@nodelib/fs.stat": ["@nodelib/fs.stat@2.0.5", "", {}, "sha512-RkhPPp2zrqDAQA/2jNhnztcPAlv64XdhIp7a7454A5ovI7Bukxgt7MX7udwAu3zg1DcpPU0rz3VV1SeaqvY4+A=="],

    "@nodelib/fs.walk": ["@nodelib/fs.walk@1.2.8", "", { "dependencies": { "@nodelib/fs.scandir": "2.1.5", "fastq": "^1.6.0" } }, "sha512-oGB+UxlgWcgQkgwo8GcEGwemoTFt3FIO9ababBmaGwXIoBKZ+GTy0pP185beGg7Llih/NSHSV2XAs1lnznocSg=="],

    "@nuxt/cli": ["@nuxt/cli@3.34.0", "", { "dependencies": { "@bomb.sh/tab": "^0.0.14", "@clack/prompts": "^1.1.0", "c12": "^3.3.3", "citty": "^0.2.1", "confbox": "^0.2.4", "consola": "^3.4.2", "debug": "^4.4.3", "defu": "^6.1.4", "exsolve": "^1.0.8", "fuse.js": "^7.1.0", "fzf": "^0.5.2", "giget": "^3.1.2", "jiti": "^2.6.1", "listhen": "^1.9.0", "nypm": "^0.6.5", "ofetch": "^1.5.1", "ohash": "^2.0.11", "pathe": "^2.0.3", "perfect-debounce": "^2.1.0", "pkg-types": "^2.3.0", "scule": "^1.3.0", "semver": "^7.7.4", "srvx": "^0.11.9", "std-env": "^3.10.0", "tinyclip": "^0.1.12", "tinyexec": "^1.0.2", "ufo": "^1.6.3", "youch": "^4.1.0" }, "peerDependencies": { "@nuxt/schema": "^4.3.1" }, "optionalPeers": ["@nuxt/schema"], "bin": { "nuxi": "bin/nuxi.mjs", "nuxi-ng": "bin/nuxi.mjs", "nuxt": "bin/nuxi.mjs", "nuxt-cli": "bin/nuxi.mjs" } }, "sha512-KVI4xSo96UtUUbmxr9ouWTytbj1LzTw5alsM4vC/gSY/l8kPMRAlq0XpNSAVTDJyALzLY70WhaIMX24LJLpdFw=="],

    "@nuxt/devalue": ["@nuxt/devalue@2.0.2", "", {}, "sha512-GBzP8zOc7CGWyFQS6dv1lQz8VVpz5C2yRszbXufwG/9zhStTIH50EtD87NmWbTMwXDvZLNg8GIpb1UFdH93JCA=="],

    "@nuxt/devtools": ["@nuxt/devtools@3.2.4", "", { "dependencies": { "@nuxt/devtools-kit": "3.2.4", "@nuxt/devtools-wizard": "3.2.4", "@nuxt/kit": "^4.4.2", "@vue/devtools-core": "^8.1.0", "@vue/devtools-kit": "^8.1.0", "birpc": "^4.0.0", "consola": "^3.4.2", "destr": "^2.0.5", "error-stack-parser-es": "^1.0.5", "execa": "^8.0.1", "fast-npm-meta": "^1.4.2", "get-port-please": "^3.2.0", "hookable": "^6.1.0", "image-meta": "^0.2.2", "is-installed-globally": "^1.0.0", "launch-editor": "^2.13.1", "local-pkg": "^1.1.2", "magicast": "^0.5.2", "nypm": "^0.6.5", "ohash": "^2.0.11", "pathe": "^2.0.3", "perfect-debounce": "^2.1.0", "pkg-types": "^2.3.0", "semver": "^7.7.4", "simple-git": "^3.33.0", "sirv": "^3.0.2", "structured-clone-es": "^2.0.0", "tinyglobby": "^0.2.15", "vite-plugin-inspect": "^11.3.3", "vite-plugin-vue-tracer": "^1.3.0", "which": "^6.0.1", "ws": "^8.19.0" }, "peerDependencies": { "@vitejs/devtools": "*", "vite": ">=6.0" }, "optionalPeers": ["@vitejs/devtools"], "bin": { "devtools": "cli.mjs" } }, "sha512-VPbFy7hlPzWpEZk4BsuVpNuHq1ZYGV9xezjb7/NGuePuNLqeNn74YZugU+PCtva7OwKhEeTXmMK0Mqo/6+nwNA=="],

    "@nuxt/devtools-kit": ["@nuxt/devtools-kit@3.2.4", "", { "dependencies": { "@nuxt/kit": "^4.4.2", "execa": "^8.0.1" }, "peerDependencies": { "vite": ">=6.0" } }, "sha512-Yxy2Xgmq5hf3dQy983V0xh0OJV2mYwRZz9eVIGc3EaribdFGPDNGMMbYqX9qCty3Pbxn/bCF3J0UyPaNlHVayQ=="],

    "@nuxt/devtools-wizard": ["@nuxt/devtools-wizard@3.2.4", "", { "dependencies": { "@clack/prompts": "^1.1.0", "consola": "^3.4.2", "diff": "^8.0.3", "execa": "^8.0.1", "magicast": "^0.5.2", "pathe": "^2.0.3", "pkg-types": "^2.3.0", "semver": "^7.7.4" }, "bin": { "devtools-wizard": "cli.mjs" } }, "sha512-5tu2+Quu9XTxwtpzM8CUN0UKn/bzZIfJcoGd+at5Yy1RiUQJ4E52tRK0idW1rMSUDkbkvX3dSnu8Tpj7SAtWdQ=="],

    "@nuxt/kit": ["@nuxt/kit@3.21.2", "", { "dependencies": { "c12": "^3.3.3", "consola": "^3.4.2", "defu": "^6.1.4", "destr": "^2.0.5", "errx": "^0.1.0", "exsolve": "^1.0.8", "ignore": "^7.0.5", "jiti": "^2.6.1", "klona": "^2.0.6", "knitwork": "^1.3.0", "mlly": "^1.8.1", "ohash": "^2.0.11", "pathe": "^2.0.3", "pkg-types": "^2.3.0", "rc9": "^3.0.0", "scule": "^1.3.0", "semver": "^7.7.4", "tinyglobby": "^0.2.15", "ufo": "^1.6.3", "unctx": "^2.5.0", "untyped": "^2.0.0" } }, "sha512-Bd6m6mrDrqpBEbX+g0rc66/ALd1sxlgdx5nfK9MAYO0yKLTOSK7McSYz1KcOYn3LQFCXOWfvXwaqih/b+REI1g=="],

    "@nuxt/nitro-server": ["@nuxt/nitro-server@3.21.2", "", { "dependencies": { "@nuxt/devalue": "^2.0.2", "@nuxt/kit": "3.21.2", "@unhead/vue": "^2.1.12", "@vue/shared": "^3.5.30", "consola": "^3.4.2", "defu": "^6.1.4", "destr": "^2.0.5", "devalue": "^5.6.3", "errx": "^0.1.0", "escape-string-regexp": "^5.0.0", "exsolve": "^1.0.8", "h3": "^1.15.6", "impound": "^1.1.5", "klona": "^2.0.6", "mocked-exports": "^0.1.1", "nitropack": "^2.13.1", "ohash": "^2.0.11", "pathe": "^2.0.3", "pkg-types": "^2.3.0", "rou3": "^0.8.1", "std-env": "^4.0.0", "ufo": "^1.6.3", "unctx": "^2.5.0", "unstorage": "^1.17.4", "vue": "^3.5.30", "vue-bundle-renderer": "^2.2.0", "vue-devtools-stub": "^0.1.0" }, "peerDependencies": { "nuxt": "^3.21.2" } }, "sha512-tJiyrG+chze1JP1JNDFR2Ib+EhnMzmZXW7AmW7Wbxz2LLTSapLzJCLgHcy4OBcBK22bs06bI/ivn95JNvvxWbQ=="],

    "@nuxt/schema": ["@nuxt/schema@3.21.2", "", { "dependencies": { "@vue/shared": "^3.5.30", "defu": "^6.1.4", "pathe": "^2.0.3", "pkg-types": "^2.3.0", "std-env": "^4.0.0" } }, "sha512-yZaJrZizRP4OQVCM7qRG3xIJ1xZ59npgg9jd3ng+BDs5ZvLqYP9rXnFikShc8EPUtR6+zhSPgKgy6L8wWcBKzQ=="],

    "@nuxt/telemetry": ["@nuxt/telemetry@2.7.0", "", { "dependencies": { "citty": "^0.2.0", "consola": "^3.4.2", "ofetch": "^2.0.0-alpha.3", "rc9": "^3.0.0", "std-env": "^3.10.0" }, "peerDependencies": { "@nuxt/kit": ">=3.0.0" }, "bin": { "nuxt-telemetry": "bin/nuxt-telemetry.mjs" } }, "sha512-mrKC3NjAlBOooLLVTYcIUie1meipoYq5vkoESoVTEWTB34T3a0QJzOfOPch+HYlUR+5Lqy1zLMv6epHFgYAKLA=="],

    "@nuxt/vite-builder": ["@nuxt/vite-builder@3.21.2", "", { "dependencies": { "@nuxt/kit": "3.21.2", "@rollup/plugin-replace": "^6.0.3", "@vitejs/plugin-vue": "^6.0.4", "@vitejs/plugin-vue-jsx": "^5.1.4", "autoprefixer": "^10.4.27", "consola": "^3.4.2", "cssnano": "^7.1.3", "defu": "^6.1.4", "escape-string-regexp": "^5.0.0", "exsolve": "^1.0.8", "externality": "^1.0.2", "get-port-please": "^3.2.0", "jiti": "^2.6.1", "knitwork": "^1.3.0", "magic-string": "^0.30.21", "mlly": "^1.8.1", "mocked-exports": "^0.1.1", "nypm": "^0.6.5", "ohash": "^2.0.11", "pathe": "^2.0.3", "perfect-debounce": "^2.1.0", "pkg-types": "^2.3.0", "postcss": "^8.5.8", "seroval": "^1.5.1", "std-env": "^4.0.0", "ufo": "^1.6.3", "unenv": "^2.0.0-rc.24", "vite": "^7.3.1", "vite-node": "^5.3.0", "vite-plugin-checker": "^0.12.0", "vue-bundle-renderer": "^2.2.0" }, "peerDependencies": { "nuxt": "3.21.2", "rolldown": "^1.0.0-beta.38", "rollup-plugin-visualizer": "^6.0.0 || ^7.0.1", "vue": "^3.3.4" }, "optionalPeers": ["rolldown", "rollup-plugin-visualizer"] }, "sha512-AwfvmogMzBmX8oS8QPjh9uZiUtnWmOV8w4Ei4DMukVELemkRugDOqWzCzuFneOFQ8khhOOMZ/lRcoTiPryZS5A=="],

    "@oslojs/encoding": ["@oslojs/encoding@1.1.0", "", {}, "sha512-70wQhgYmndg4GCPxPPxPGevRKqTIJ2Nh4OkiMWmDAVYsTQ+Ta7Sq+rPevXyXGdzr30/qZBnyOalCszoMxlyldQ=="],

    "@oxc-minify/binding-android-arm-eabi": ["@oxc-minify/binding-android-arm-eabi@0.117.0", "", { "os": "android", "cpu": "arm" }, "sha512-5Hf2KsGRjxp3HnPU/mse7cQJa5tWfMFUPZQcgSMVsv2JZnGFFOIDzA0Oja2KDD+VPJqMpEJKc2dCHAGZgJxsGg=="],

    "@oxc-minify/binding-android-arm64": ["@oxc-minify/binding-android-arm64@0.117.0", "", { "os": "android", "cpu": "arm64" }, "sha512-uuxGwxA5J4Sap+gz4nxyM/rer6q2A4X1Oe8HpE0CZQyb5cSBULQ15btZiVG3xOBctI5O+c2dwR1aZAP4oGKcLw=="],

    "@oxc-minify/binding-darwin-arm64": ["@oxc-minify/binding-darwin-arm64@0.117.0", "", { "os": "darwin", "cpu": "arm64" }, "sha512-lLBf75cxUSLydumToKtGTwbLqO/1urScblJ33Vx0uF38M2ZbL2x51AybBV5vlfLjYNrxvQ8ov0Bj/OhsVO/biA=="],

    "@oxc-minify/binding-darwin-x64": ["@oxc-minify/binding-darwin-x64@0.117.0", "", { "os": "darwin", "cpu": "x64" }, "sha512-wBWwP1voLZMuN4hpe1HRtkPBd4/o/1qan5XssmmI/hewBvGHEHkyvVLS0zu+cKqXDxYzYvb/p+EqU+xSXhEl4A=="],

    "@oxc-minify/binding-freebsd-x64": ["@oxc-minify/binding-freebsd-x64@0.117.0", "", { "os": "freebsd", "cpu": "x64" }, "sha512-pYSacHw698oH2vb70iP1cHk6x0zhvAuOvdskvNtEqvfziu8MSjKXa699vA9Cx72+DH5rwVuj1I3f+7no2fWglA=="],

    "@oxc-minify/binding-linux-arm-gnueabihf": ["@oxc-minify/binding-linux-arm-gnueabihf@0.117.0", "", { "os": "linux", "cpu": "arm" }, "sha512-Ugm4Qj7F2+bccjhHCjjnSNHBDPyvjPXWrntID4WJpSrPqt+Az/o0EGdty9sWOjQXRZiTVpa80uqCWZQUn94yTA=="],

    "@oxc-minify/binding-linux-arm-musleabihf": ["@oxc-minify/binding-linux-arm-musleabihf@0.117.0", "", { "os": "linux", "cpu": "arm" }, "sha512-qrY6ZviO9wVRI/jl4nRZO4B9os8jaJQemMeWIyFInZNk3lhqihId8iBqMKibJnRaf+JRxLM9j68atXkFRhOHrg=="],

    "@oxc-minify/binding-linux-arm64-gnu": ["@oxc-minify/binding-linux-arm64-gnu@0.117.0", "", { "os": "linux", "cpu": "arm64" }, "sha512-2VLJHKEFBRhCihT/8uesuDPhXpbWu1OlHCxqQ7pdFVqKik1Maj5E9oSDcYzxqfaCRStvTHkmLVWJBK5CVcIadg=="],

    "@oxc-minify/binding-linux-arm64-musl": ["@oxc-minify/binding-linux-arm64-musl@0.117.0", "", { "os": "linux", "cpu": "arm64" }, "sha512-C3zapJconWpl2Y7LR3GkRkH6jxpuV2iVUfkFcHT5Ffn4Zu7l88mZa2dhcfdULZDybN1Phka/P34YUzuskUUrXw=="],

    "@oxc-minify/binding-linux-ppc64-gnu": ["@oxc-minify/binding-linux-ppc64-gnu@0.117.0", "", { "os": "linux", "cpu": "ppc64" }, "sha512-2T/Bm+3/qTfuNS4gKSzL8qbiYk+ErHW2122CtDx+ilZAzvWcJ8IbqdZIbEWOlwwe03lESTxPwTBLFqVgQU2OeQ=="],

    "@oxc-minify/binding-linux-riscv64-gnu": ["@oxc-minify/binding-linux-riscv64-gnu@0.117.0", "", { "os": "linux", "cpu": "none" }, "sha512-MKLjpldYkeoB4T+yAi4aIAb0waifxUjLcKkCUDmYAY3RqBJTvWK34KtfaKZL0IBMIXfD92CbKkcxQirDUS9Xcg=="],

    "@oxc-minify/binding-linux-riscv64-musl": ["@oxc-minify/binding-linux-riscv64-musl@0.117.0", "", { "os": "linux", "cpu": "none" }, "sha512-UFVcbPvKUStry6JffriobBp8BHtjmLLPl4bCY+JMxIn/Q3pykCpZzRwFTcDurG/kY8tm+uSNfKKdRNa5Nh9A7g=="],

    "@oxc-minify/binding-linux-s390x-gnu": ["@oxc-minify/binding-linux-s390x-gnu@0.117.0", "", { "os": "linux", "cpu": "s390x" }, "sha512-B9GyPQ1NKbvpETVAMyJMfRlD3c6UJ7kiuFUAlx9LTYiQL+YIyT6vpuRlq1zgsXxavZluVrfeJv6x0owV4KDx4Q=="],

    "@oxc-minify/binding-linux-x64-gnu": ["@oxc-minify/binding-linux-x64-gnu@0.117.0", "", { "os": "linux", "cpu": "x64" }, "sha512-fXfhtr+WWBGNy4M5GjAF5vu/lpulR4Me34FjTyaK9nDrTZs7LM595UDsP1wliksqp4hD/KdoqHGmbCrC+6d4vA=="],

    "@oxc-minify/binding-linux-x64-musl": ["@oxc-minify/binding-linux-x64-musl@0.117.0", "", { "os": "linux", "cpu": "x64" }, "sha512-jFBgGbx1oLadb83ntJmy1dWlAHSQanXTS21G4PgkxyONmxZdZ/UMKr7KsADzMuoPsd2YhJHxzRpwJd9U+4BFBw=="],

    "@oxc-minify/binding-openharmony-arm64": ["@oxc-minify/binding-openharmony-arm64@0.117.0", "", { "os": "none", "cpu": "arm64" }, "sha512-nxPd9vx1vYz8IlIMdl9HFdOK/ood1H5hzbSFsyO8JU55tkcJoBL8TLCbuFf9pHpOy27l2gcPyV6z3p4eAcTH5Q=="],

    "@oxc-minify/binding-wasm32-wasi": ["@oxc-minify/binding-wasm32-wasi@0.117.0", "", { "dependencies": { "@napi-rs/wasm-runtime": "^1.1.1" }, "cpu": "none" }, "sha512-pSvjJ6cCCfEXSteWSiVfZhdRzvpmS3tLhlXrXTYiuTDFrkRCobRP39SRwAzK23rE9i/m2JAaES2xPEW6+xu85g=="],

    "@oxc-minify/binding-win32-arm64-msvc": ["@oxc-minify/binding-win32-arm64-msvc@0.117.0", "", { "os": "win32", "cpu": "arm64" }, "sha512-9NoT9baFrWPdJRIZVQ1jzPZW9TjPT2sbzQyDdoK7uD1V8JXCe1L2y7sp9k2ldZZheaIcmtNwHc7jyD7kYz/0XQ=="],

    "@oxc-minify/binding-win32-ia32-msvc": ["@oxc-minify/binding-win32-ia32-msvc@0.117.0", "", { "os": "win32", "cpu": "ia32" }, "sha512-E51LTjkRei5u2dpFiYSObuh+e43xg45qlmilSTd0XDGFdYJCOv62Q0MEn61TR+efQYPNleYwWdTS9t+tp9p/4w=="],

    "@oxc-minify/binding-win32-x64-msvc": ["@oxc-minify/binding-win32-x64-msvc@0.117.0", "", { "os": "win32", "cpu": "x64" }, "sha512-I8vniPOxWQdxfIbXNvQLaJ1n8SrnqES6wuiAX10CU72sKsizkds9kDaJ1KzWvDy39RKhTBmD1cJsU2uxPFgizQ=="],

    "@oxc-parser/binding-android-arm-eabi": ["@oxc-parser/binding-android-arm-eabi@0.117.0", "", { "os": "android", "cpu": "arm" }, "sha512-XarGPJpaobgKjfm7xRfCGWWszuPbm/OeP91NdMhxtcLZ/qLTmWF0P0z0gqmr0Uysi1F1v1BNtcST11THMrcEOw=="],

    "@oxc-parser/binding-android-arm64": ["@oxc-parser/binding-android-arm64@0.117.0", "", { "os": "android", "cpu": "arm64" }, "sha512-EPTs2EBijGmyhPso4rXAL0NSpECXER9IaVKFZEv83YcA6h4uhKW47kmYt+OZcSp130zhHx+lTWILDQ/LDkCRNA=="],

    "@oxc-parser/binding-darwin-arm64": ["@oxc-parser/binding-darwin-arm64@0.117.0", "", { "os": "darwin", "cpu": "arm64" }, "sha512-3bAEpyih6r/Kb+Xzn1em1qBMClOS7NsVWgF86k95jpysR5ix/HlKFKSy7cax6PcS96HeHR4kjlME20n/XK1zNg=="],

    "@oxc-parser/binding-darwin-x64": ["@oxc-parser/binding-darwin-x64@0.117.0", "", { "os": "darwin", "cpu": "x64" }, "sha512-W7S99zFwVZhSbCxvjfZkioStFU249DBc4TJw/kK6kfKwx2Zew+jvizX5Y3ZPkAh7fBVUSNOdSeOqLBHLiP50tw=="],

    "@oxc-parser/binding-freebsd-x64": ["@oxc-parser/binding-freebsd-x64@0.117.0", "", { "os": "freebsd", "cpu": "x64" }, "sha512-xH76lqSdjCSY0KUMPwLXlvQ3YEm3FFVEQmgiOCGNf+stZ6E4Mo3nC102Bo8yKd7aW0foIPAFLYsHgj7vVI/axw=="],

    "@oxc-parser/binding-linux-arm-gnueabihf": ["@oxc-parser/binding-linux-arm-gnueabihf@0.117.0", "", { "os": "linux", "cpu": "arm" }, "sha512-9Hdm1imzrn4RdMYnQKKcy+7p7QsSPIrgVIZmpGSJT02nYDuBWLdG1pdYMPFoEo46yiXry3tS3RoHIpNbT1IiyQ=="],

    "@oxc-parser/binding-linux-arm-musleabihf": ["@oxc-parser/binding-linux-arm-musleabihf@0.117.0", "", { "os": "linux", "cpu": "arm" }, "sha512-Itszer/VCeYhYVJLcuKnHktlY8QyGnVxapltP68S1XRGlV6IsM9HQAElJRMwQhT6/GkMjOhANmkv2Qu/9v44lw=="],

    "@oxc-parser/binding-linux-arm64-gnu": ["@oxc-parser/binding-linux-arm64-gnu@0.117.0", "", { "os": "linux", "cpu": "arm64" }, "sha512-jBxD7DtlHQ36ivjjZdH0noQJgWNouenzpLmXNKnYaCsBfo3jY95m5iyjYQEiWkvkhJ3TJUAs7tQ1/kEpY7x/Kg=="],

    "@oxc-parser/binding-linux-arm64-musl": ["@oxc-parser/binding-linux-arm64-musl@0.117.0", "", { "os": "linux", "cpu": "arm64" }, "sha512-QagKTDF4lrz8bCXbUi39Uq5xs7C7itAseKm51f33U+Dyar9eJY/zGKqfME9mKLOiahX7Fc1J3xMWVS0AdDXLPg=="],

    "@oxc-parser/binding-linux-ppc64-gnu": ["@oxc-parser/binding-linux-ppc64-gnu@0.117.0", "", { "os": "linux", "cpu": "ppc64" }, "sha512-RPddpcE/0xxWaommWy0c5i/JdrXcXAkxBS2GOrAUh5LKmyCh03hpJedOAWszG4ADsKQwoUQQ1/tZVGRhZIWtKA=="],

    "@oxc-parser/binding-linux-riscv64-gnu": ["@oxc-parser/binding-linux-riscv64-gnu@0.117.0", "", { "os": "linux", "cpu": "none" }, "sha512-ur/WVZF9FSOiZGxyP+nfxZzuv6r5OJDYoVxJnUR7fM/hhXLh4V/be6rjbzm9KLCDBRwYCEKJtt+XXNccwd06IA=="],

    "@oxc-parser/binding-linux-riscv64-musl": ["@oxc-parser/binding-linux-riscv64-musl@0.117.0", "", { "os": "linux", "cpu": "none" }, "sha512-ujGcAx8xAMvhy7X5sBFi3GXML1EtyORuJZ5z2T6UV3U416WgDX/4OCi3GnoteeenvxIf6JgP45B+YTHpt71vpA=="],

    "@oxc-parser/binding-linux-s390x-gnu": ["@oxc-parser/binding-linux-s390x-gnu@0.117.0", "", { "os": "linux", "cpu": "s390x" }, "sha512-hbsfKjUwRjcMZZvvmpZSc+qS0bHcHRu8aV/I3Ikn9BzOA0ZAgUE7ctPtce5zCU7bM8dnTLi4sJ1Pi9YHdx6Urw=="],

    "@oxc-parser/binding-linux-x64-gnu": ["@oxc-parser/binding-linux-x64-gnu@0.117.0", "", { "os": "linux", "cpu": "x64" }, "sha512-1QrTrf8rige7UPJrYuDKJLQOuJlgkt+nRSJLBMHWNm9TdivzP48HaK3f4q18EjNlglKtn03lgjMu4fryDm8X4A=="],

    "@oxc-parser/binding-linux-x64-musl": ["@oxc-parser/binding-linux-x64-musl@0.117.0", "", { "os": "linux", "cpu": "x64" }, "sha512-gRvK6HPzF5ITRL68fqb2WYYs/hGviPIbkV84HWCgiJX+LkaOpp+HIHQl3zVZdyKHwopXToTbXbtx/oFjDjl8pg=="],

    "@oxc-parser/binding-openharmony-arm64": ["@oxc-parser/binding-openharmony-arm64@0.117.0", "", { "os": "none", "cpu": "arm64" }, "sha512-QPJvFbnnDZZY7xc+xpbIBWLThcGBakwaYA9vKV8b3+oS5MGfAZUoTFJcix5+Zg2Ri46sOfrUim6Y6jsKNcssAQ=="],

    "@oxc-parser/binding-wasm32-wasi": ["@oxc-parser/binding-wasm32-wasi@0.117.0", "", { "dependencies": { "@napi-rs/wasm-runtime": "^1.1.1" }, "cpu": "none" }, "sha512-+XRSNA0xt3pk/6CUHM7pykVe7M8SdifJk8LX1+fIp/zefvR3HBieZCbwG5un8gogNgh7srLycoh/cQA9uozv5g=="],

    "@oxc-parser/binding-win32-arm64-msvc": ["@oxc-parser/binding-win32-arm64-msvc@0.117.0", "", { "os": "win32", "cpu": "arm64" }, "sha512-GpxeGS+Vo030DsrXeRPc7OSJOQIyAHkM3mzwBcnQjg/79XnOIDDMXJ5X6/aNdkVt/+Pv35pqKzGA4TQau97x8w=="],

    "@oxc-parser/binding-win32-ia32-msvc": ["@oxc-parser/binding-win32-ia32-msvc@0.117.0", "", { "os": "win32", "cpu": "ia32" }, "sha512-tchWEYiso1+objTZirmlR+w3fcIel6PVBOJ8NuC2Jr30dxBOiKUfFLovJLANwHg1+TzeD6pVSLIIIEf2T5o5lQ=="],

    "@oxc-parser/binding-win32-x64-msvc": ["@oxc-parser/binding-win32-x64-msvc@0.117.0", "", { "os": "win32", "cpu": "x64" }, "sha512-ysRJAjIbB4e5y+t9PZs7TwbgOV/GVT//s30AORLCT/pedYwpYzHq6ApXK7is9fvyfZtgT3anNir8+esurmyaDw=="],

    "@oxc-project/types": ["@oxc-project/types@0.115.0", "", {}, "sha512-4n91DKnebUS4yjUHl2g3/b2T+IUdCfmoZGhmwsovZCDaJSs+QkVAM+0AqqTxHSsHfeiMuueT75cZaZcT/m0pSw=="],

    "@oxc-transform/binding-android-arm-eabi": ["@oxc-transform/binding-android-arm-eabi@0.117.0", "", { "os": "android", "cpu": "arm" }, "sha512-17giX7h5VR9Eodru4OoSCFdgwLFIaUxeEn8JWe0vMZrAuRbT9NiDTy5dXdbGQBoO8aXPkbGS38FGlvbi31aujw=="],

    "@oxc-transform/binding-android-arm64": ["@oxc-transform/binding-android-arm64@0.117.0", "", { "os": "android", "cpu": "arm64" }, "sha512-1LrDd1CPochtLx04pAafdah6QtOQQj0/Evttevi+0u8rCI5FKucIG7pqBHkIQi/y7pycFYIj+GebhET80maeUg=="],

    "@oxc-transform/binding-darwin-arm64": ["@oxc-transform/binding-darwin-arm64@0.117.0", "", { "os": "darwin", "cpu": "arm64" }, "sha512-K1Xo52xJOvFfHSkz2ax9X5Qsku23RCfTIPbHZWdUCAQ1TQooI+sFcewSubhVUJ4DVK12/tYT//XXboumin+FHA=="],

    "@oxc-transform/binding-darwin-x64": ["@oxc-transform/binding-darwin-x64@0.117.0", "", { "os": "darwin", "cpu": "x64" }, "sha512-ftFT/8Laolfq49mRRWLkIhd1AbJ0MI5bW3LwddvdoAg9zXwkx4qhzTYyBPRZhvXWftts+NjlHfHsXCOqI4tPtw=="],

    "@oxc-transform/binding-freebsd-x64": ["@oxc-transform/binding-freebsd-x64@0.117.0", "", { "os": "freebsd", "cpu": "x64" }, "sha512-QDRyw0atg9BMnwOwnJeW6REzWPLEjiWtsCc2Sj612F1hCdvP+n0L3o8sHinEWM+BiOkOYtUxHA69WjUslc3G+g=="],

    "@oxc-transform/binding-linux-arm-gnueabihf": ["@oxc-transform/binding-linux-arm-gnueabihf@0.117.0", "", { "os": "linux", "cpu": "arm" }, "sha512-UvpvOjyQVgiIJahIpMT0qAsLJT8O1ibHTBgXGOsZkQgw1xmjARPQ07dpRcucPPn6cqCF3wrxfbqtr2vFHaMkdA=="],

    "@oxc-transform/binding-linux-arm-musleabihf": ["@oxc-transform/binding-linux-arm-musleabihf@0.117.0", "", { "os": "linux", "cpu": "arm" }, "sha512-cIhztGFjKk8ngP+/7EPkEhzWMGr2neezxgWirSn/f/MirjH234oHHGJ2diKIbGQEsy0aOuJMTkL9NLfzfmH51A=="],

    "@oxc-transform/binding-linux-arm64-gnu": ["@oxc-transform/binding-linux-arm64-gnu@0.117.0", "", { "os": "linux", "cpu": "arm64" }, "sha512-mXbDfvDN0RZVg7v4LohNzU0kK3fMAZgkUKTkpFVgxEvzibEG5VpSznkypUwHI4a8U8pz+K6mGaLetX3Xt+CvvA=="],

    "@oxc-transform/binding-linux-arm64-musl": ["@oxc-transform/binding-linux-arm64-musl@0.117.0", "", { "os": "linux", "cpu": "arm64" }, "sha512-ykxpPQp0eAcSmhy0Y3qKvdanHY4d8THPonDfmCoktUXb6r0X6qnjpJB3V+taN1wevW55bOEZd97kxtjTKjqhmg=="],

    "@oxc-transform/binding-linux-ppc64-gnu": ["@oxc-transform/binding-linux-ppc64-gnu@0.117.0", "", { "os": "linux", "cpu": "ppc64" }, "sha512-Rvspti4Kr7eq6zSrURK5WjscfWQPvmy/KjJZV45neRKW8RLonE3r9+NgrwSLGoHvQ3F24fbqlkplox1RtlhH5A=="],

    "@oxc-transform/binding-linux-riscv64-gnu": ["@oxc-transform/binding-linux-riscv64-gnu@0.117.0", "", { "os": "linux", "cpu": "none" }, "sha512-Dr2ZW9ZZ4l1eQ5JUEUY3smBh4JFPCPuybWaDZTLn3ADZjyd8ZtNXEjeMT8rQbbhbgSL9hEgbwaqraole3FNThQ=="],

    "@oxc-transform/binding-linux-riscv64-musl": ["@oxc-transform/binding-linux-riscv64-musl@0.117.0", "", { "os": "linux", "cpu": "none" }, "sha512-oD1Bnes1bIC3LVBSrWEoSUBj6fvatESPwAVWfJVGVQlqWuOs/ZBn1e4Nmbipo3KGPHK7DJY75r/j7CQCxhrOFQ=="],

    "@oxc-transform/binding-linux-s390x-gnu": ["@oxc-transform/binding-linux-s390x-gnu@0.117.0", "", { "os": "linux", "cpu": "s390x" }, "sha512-qT//IAPLvse844t99Kff5j055qEbXfwzWgvCMb0FyjisnB8foy25iHZxZIocNBe6qwrCYWUP1M8rNrB/WyfS1Q=="],

    "@oxc-transform/binding-linux-x64-gnu": ["@oxc-transform/binding-linux-x64-gnu@0.117.0", "", { "os": "linux", "cpu": "x64" }, "sha512-2YEO5X+KgNzFqRVO5dAkhjcI5gwxus4NSWVl/+cs2sI6P0MNPjqE3VWPawl4RTC11LvetiiZdHcujUCPM8aaUw=="],

    "@oxc-transform/binding-linux-x64-musl": ["@oxc-transform/binding-linux-x64-musl@0.117.0", "", { "os": "linux", "cpu": "x64" }, "sha512-3wqWbTSaIFZvDr1aqmTul4cg8PRWYh6VC52E8bLI7ytgS/BwJLW+sDUU2YaGIds4sAf/1yKeJRmudRCDPW9INg=="],

    "@oxc-transform/binding-openharmony-arm64": ["@oxc-transform/binding-openharmony-arm64@0.117.0", "", { "os": "none", "cpu": "arm64" }, "sha512-Ebxx6NPqhzlrjvx4+PdSqbOq+li0f7X59XtJljDghkbJsbnkHvhLmPR09ifHt5X32UlZN63ekjwcg/nbmHLLlA=="],

    "@oxc-transform/binding-wasm32-wasi": ["@oxc-transform/binding-wasm32-wasi@0.117.0", "", { "dependencies": { "@napi-rs/wasm-runtime": "^1.1.1" }, "cpu": "none" }, "sha512-Nn8mmcBiQ0XKHLTb05QBlH+CDkn7jf5YDVv9FtKhy4zJT0NEU9y3dXVbfcurOpsVrG9me4ktzDQNCaAoJjUQyw=="],

    "@oxc-transform/binding-win32-arm64-msvc": ["@oxc-transform/binding-win32-arm64-msvc@0.117.0", "", { "os": "win32", "cpu": "arm64" }, "sha512-15cbsF8diXWGnHrTsVgVeabETiT/KdMAfRAcot99xsaVecJs3pITNNjC6Qj+/TPNpehbgIFjlhhxOVSbQsTBgg=="],

    "@oxc-transform/binding-win32-ia32-msvc": ["@oxc-transform/binding-win32-ia32-msvc@0.117.0", "", { "os": "win32", "cpu": "ia32" }, "sha512-I6DkhCuFX6p9rckdWiLuZfBWrrYUC7sNX+zLaCfa5zvrPNwo1/29KkefvqXVxu3AWT/6oZAbtc0A8/mqhETJPQ=="],

    "@oxc-transform/binding-win32-x64-msvc": ["@oxc-transform/binding-win32-x64-msvc@0.117.0", "", { "os": "win32", "cpu": "x64" }, "sha512-V7YzavQnYcRJBeJkp0qpb3FKrlm5I57XJetCYB4jsjStuboQmnFMZ/XQH55Szlf/kVyeU9ddQwv72gJJ5BrGjQ=="],

    "@parcel/watcher": ["@parcel/watcher@2.5.6", "", { "dependencies": { "detect-libc": "^2.0.3", "is-glob": "^4.0.3", "node-addon-api": "^7.0.0", "picomatch": "^4.0.3" }, "optionalDependencies": { "@parcel/watcher-android-arm64": "2.5.6", "@parcel/watcher-darwin-arm64": "2.5.6", "@parcel/watcher-darwin-x64": "2.5.6", "@parcel/watcher-freebsd-x64": "2.5.6", "@parcel/watcher-linux-arm-glibc": "2.5.6", "@parcel/watcher-linux-arm-musl": "2.5.6", "@parcel/watcher-linux-arm64-glibc": "2.5.6", "@parcel/watcher-linux-arm64-musl": "2.5.6", "@parcel/watcher-linux-x64-glibc": "2.5.6", "@parcel/watcher-linux-x64-musl": "2.5.6", "@parcel/watcher-win32-arm64": "2.5.6", "@parcel/watcher-win32-ia32": "2.5.6", "@parcel/watcher-win32-x64": "2.5.6" } }, "sha512-tmmZ3lQxAe/k/+rNnXQRawJ4NjxO2hqiOLTHvWchtGZULp4RyFeh6aU4XdOYBFe2KE1oShQTv4AblOs2iOrNnQ=="],

    "@parcel/watcher-android-arm64": ["@parcel/watcher-android-arm64@2.5.6", "", { "os": "android", "cpu": "arm64" }, "sha512-YQxSS34tPF/6ZG7r/Ih9xy+kP/WwediEUsqmtf0cuCV5TPPKw/PQHRhueUo6JdeFJaqV3pyjm0GdYjZotbRt/A=="],

    "@parcel/watcher-darwin-arm64": ["@parcel/watcher-darwin-arm64@2.5.6", "", { "os": "darwin", "cpu": "arm64" }, "sha512-Z2ZdrnwyXvvvdtRHLmM4knydIdU9adO3D4n/0cVipF3rRiwP+3/sfzpAwA/qKFL6i1ModaabkU7IbpeMBgiVEA=="],

    "@parcel/watcher-darwin-x64": ["@parcel/watcher-darwin-x64@2.5.6", "", { "os": "darwin", "cpu": "x64" }, "sha512-HgvOf3W9dhithcwOWX9uDZyn1lW9R+7tPZ4sug+NGrGIo4Rk1hAXLEbcH1TQSqxts0NYXXlOWqVpvS1SFS4fRg=="],

    "@parcel/watcher-freebsd-x64": ["@parcel/watcher-freebsd-x64@2.5.6", "", { "os": "freebsd", "cpu": "x64" }, "sha512-vJVi8yd/qzJxEKHkeemh7w3YAn6RJCtYlE4HPMoVnCpIXEzSrxErBW5SJBgKLbXU3WdIpkjBTeUNtyBVn8TRng=="],

    "@parcel/watcher-linux-arm-glibc": ["@parcel/watcher-linux-arm-glibc@2.5.6", "", { "os": "linux", "cpu": "arm" }, "sha512-9JiYfB6h6BgV50CCfasfLf/uvOcJskMSwcdH1PHH9rvS1IrNy8zad6IUVPVUfmXr+u+Km9IxcfMLzgdOudz9EQ=="],

    "@parcel/watcher-linux-arm-musl": ["@parcel/watcher-linux-arm-musl@2.5.6", "", { "os": "linux", "cpu": "arm" }, "sha512-Ve3gUCG57nuUUSyjBq/MAM0CzArtuIOxsBdQ+ftz6ho8n7s1i9E1Nmk/xmP323r2YL0SONs1EuwqBp2u1k5fxg=="],

    "@parcel/watcher-linux-arm64-glibc": ["@parcel/watcher-linux-arm64-glibc@2.5.6", "", { "os": "linux", "cpu": "arm64" }, "sha512-f2g/DT3NhGPdBmMWYoxixqYr3v/UXcmLOYy16Bx0TM20Tchduwr4EaCbmxh1321TABqPGDpS8D/ggOTaljijOA=="],

    "@parcel/watcher-linux-arm64-musl": ["@parcel/watcher-linux-arm64-musl@2.5.6", "", { "os": "linux", "cpu": "arm64" }, "sha512-qb6naMDGlbCwdhLj6hgoVKJl2odL34z2sqkC7Z6kzir8b5W65WYDpLB6R06KabvZdgoHI/zxke4b3zR0wAbDTA=="],

    "@parcel/watcher-linux-x64-glibc": ["@parcel/watcher-linux-x64-glibc@2.5.6", "", { "os": "linux", "cpu": "x64" }, "sha512-kbT5wvNQlx7NaGjzPFu8nVIW1rWqV780O7ZtkjuWaPUgpv2NMFpjYERVi0UYj1msZNyCzGlaCWEtzc+exjMGbQ=="],

    "@parcel/watcher-linux-x64-musl": ["@parcel/watcher-linux-x64-musl@2.5.6", "", { "os": "linux", "cpu": "x64" }, "sha512-1JRFeC+h7RdXwldHzTsmdtYR/Ku8SylLgTU/reMuqdVD7CtLwf0VR1FqeprZ0eHQkO0vqsbvFLXUmYm/uNKJBg=="],

    "@parcel/watcher-wasm": ["@parcel/watcher-wasm@2.5.6", "", { "dependencies": { "is-glob": "^4.0.3", "napi-wasm": "^1.1.0", "picomatch": "^4.0.3" } }, "sha512-byAiBZ1t3tXQvc8dMD/eoyE7lTXYorhn+6uVW5AC+JGI1KtJC/LvDche5cfUE+qiefH+Ybq0bUCJU0aB1cSHUA=="],

    "@parcel/watcher-win32-arm64": ["@parcel/watcher-win32-arm64@2.5.6", "", { "os": "win32", "cpu": "arm64" }, "sha512-3ukyebjc6eGlw9yRt678DxVF7rjXatWiHvTXqphZLvo7aC5NdEgFufVwjFfY51ijYEWpXbqF5jtrK275z52D4Q=="],

    "@parcel/watcher-win32-ia32": ["@parcel/watcher-win32-ia32@2.5.6", "", { "os": "win32", "cpu": "ia32" }, "sha512-k35yLp1ZMwwee3Ez/pxBi5cf4AoBKYXj00CZ80jUz5h8prpiaQsiRPKQMxoLstNuqe2vR4RNPEAEcjEFzhEz/g=="],

    "@parcel/watcher-win32-x64": ["@parcel/watcher-win32-x64@2.5.6", "", { "os": "win32", "cpu": "x64" }, "sha512-hbQlYcCq5dlAX9Qx+kFb0FHue6vbjlf0FrNzSKdYK2APUf7tGfGxQCk2ihEREmbR6ZMc0MVAD5RIX/41gpUzTw=="],

    "@pkgjs/parseargs": ["@pkgjs/parseargs@0.11.0", "", {}, "sha512-+1VkjdD0QBLPodGrJUeqarH8VAIvQODIbwh9XpP5Syisf7YoQgsJKPNFoqqLQlu+VQ/tVSshMR6loPMn8U+dPg=="],

    "@polka/url": ["@polka/url@1.0.0-next.29", "", {}, "sha512-wwQAWhWSuHaag8c4q/KN/vCoeOJYshAIvMQwD4GpSb3OiZklFfvAgmj0VCBBImRpuF/aFgIRzllXlVX93Jevww=="],

    "@poppinss/colors": ["@poppinss/colors@4.1.6", "", { "dependencies": { "kleur": "^4.1.5" } }, "sha512-H9xkIdFswbS8n1d6vmRd8+c10t2Qe+rZITbbDHHkQixH5+2x1FDGmi/0K+WgWiqQFKPSlIYB7jlH6Kpfn6Fleg=="],

    "@poppinss/dumper": ["@poppinss/dumper@0.7.0", "", { "dependencies": { "@poppinss/colors": "^4.1.5", "@sindresorhus/is": "^7.0.2", "supports-color": "^10.0.0" } }, "sha512-0UTYalzk2t6S4rA2uHOz5bSSW2CHdv4vggJI6Alg90yvl0UgXs6XSXpH96OH+bRkX4J/06djv29pqXJ0lq5Kag=="],

    "@poppinss/exception": ["@poppinss/exception@1.2.3", "", {}, "sha512-dCED+QRChTVatE9ibtoaxc+WkdzOSjYTKi/+uacHWIsfodVfpsueo3+DKpgU5Px8qXjgmXkSvhXvSCz3fnP9lw=="],

    "@quansync/fs": ["@quansync/fs@1.0.0", "", { "dependencies": { "quansync": "^1.0.0" } }, "sha512-4TJ3DFtlf1L5LDMaM6CanJ/0lckGNtJcMjQ1NAV6zDmA0tEHKZtxNKin8EgPaVX1YzljbxckyT2tJrpQKAtngQ=="],

    "@rolldown/binding-android-arm64": ["@rolldown/binding-android-arm64@1.0.0-rc.9", "", { "os": "android", "cpu": "arm64" }, "sha512-lcJL0bN5hpgJfSIz/8PIf02irmyL43P+j1pTCfbD1DbLkmGRuFIA4DD3B3ZOvGqG0XiVvRznbKtN0COQVaKUTg=="],

    "@rolldown/binding-darwin-arm64": ["@rolldown/binding-darwin-arm64@1.0.0-rc.9", "", { "os": "darwin", "cpu": "arm64" }, "sha512-J7Zk3kLYFsLtuH6U+F4pS2sYVzac0qkjcO5QxHS7OS7yZu2LRs+IXo+uvJ/mvpyUljDJ3LROZPoQfgBIpCMhdQ=="],

    "@rolldown/binding-darwin-x64": ["@rolldown/binding-darwin-x64@1.0.0-rc.9", "", { "os": "darwin", "cpu": "x64" }, "sha512-iwtmmghy8nhfRGeNAIltcNXzD0QMNaaA5U/NyZc1Ia4bxrzFByNMDoppoC+hl7cDiUq5/1CnFthpT9n+UtfFyg=="],

    "@rolldown/binding-freebsd-x64": ["@rolldown/binding-freebsd-x64@1.0.0-rc.9", "", { "os": "freebsd", "cpu": "x64" }, "sha512-DLFYI78SCiZr5VvdEplsVC2Vx53lnA4/Ga5C65iyldMVaErr86aiqCoNBLl92PXPfDtUYjUh+xFFor40ueNs4Q=="],

    "@rolldown/binding-linux-arm-gnueabihf": ["@rolldown/binding-linux-arm-gnueabihf@1.0.0-rc.9", "", { "os": "linux", "cpu": "arm" }, "sha512-CsjTmTwd0Hri6iTw/DRMK7kOZ7FwAkrO4h8YWKoX/kcj833e4coqo2wzIFywtch/8Eb5enQ/lwLM7w6JX1W5RQ=="],

    "@rolldown/binding-linux-arm64-gnu": ["@rolldown/binding-linux-arm64-gnu@1.0.0-rc.9", "", { "os": "linux", "cpu": "arm64" }, "sha512-2x9O2JbSPxpxMDhP9Z74mahAStibTlrBMW0520+epJH5sac7/LwZW5Bmg/E6CXuEF53JJFW509uP+lSedaUNxg=="],

    "@rolldown/binding-linux-arm64-musl": ["@rolldown/binding-linux-arm64-musl@1.0.0-rc.9", "", { "os": "linux", "cpu": "arm64" }, "sha512-JA1QRW31ogheAIRhIg9tjMfsYbglXXYGNPLdPEYrwFxdbkQCAzvpSCSHCDWNl4hTtrol8WeboCSEpjdZK8qrCg=="],

    "@rolldown/binding-linux-ppc64-gnu": ["@rolldown/binding-linux-ppc64-gnu@1.0.0-rc.9", "", { "os": "linux", "cpu": "ppc64" }, "sha512-aOKU9dJheda8Kj8Y3w9gnt9QFOO+qKPAl8SWd7JPHP+Cu0EuDAE5wokQubLzIDQWg2myXq2XhTpOVS07qqvT+w=="],

    "@rolldown/binding-linux-s390x-gnu": ["@rolldown/binding-linux-s390x-gnu@1.0.0-rc.9", "", { "os": "linux", "cpu": "s390x" }, "sha512-OalO94fqj7IWRn3VdXWty75jC5dk4C197AWEuMhIpvVv2lw9fiPhud0+bW2ctCxb3YoBZor71QHbY+9/WToadA=="],

    "@rolldown/binding-linux-x64-gnu": ["@rolldown/binding-linux-x64-gnu@1.0.0-rc.9", "", { "os": "linux", "cpu": "x64" }, "sha512-cVEl1vZtBsBZna3YMjGXNvnYYrOJ7RzuWvZU0ffvJUexWkukMaDuGhUXn0rjnV0ptzGVkvc+vW9Yqy6h8YX4pg=="],

    "@rolldown/binding-linux-x64-musl": ["@rolldown/binding-linux-x64-musl@1.0.0-rc.9", "", { "os": "linux", "cpu": "x64" }, "sha512-UzYnKCIIc4heAKgI4PZ3dfBGUZefGCJ1TPDuLHoCzgrMYPb5Rv6TLFuYtyM4rWyHM7hymNdsg5ik2C+UD9VDbA=="],

    "@rolldown/binding-openharmony-arm64": ["@rolldown/binding-openharmony-arm64@1.0.0-rc.9", "", { "os": "none", "cpu": "arm64" }, "sha512-+6zoiF+RRyf5cdlFQP7nm58mq7+/2PFaY2DNQeD4B87N36JzfF/l9mdBkkmTvSYcYPE8tMh/o3cRlsx1ldLfog=="],

    "@rolldown/binding-wasm32-wasi": ["@rolldown/binding-wasm32-wasi@1.0.0-rc.9", "", { "dependencies": { "@napi-rs/wasm-runtime": "^1.1.1" }, "cpu": "none" }, "sha512-rgFN6sA/dyebil3YTlL2evvi/M+ivhfnyxec7AccTpRPccno/rPoNlqybEZQBkcbZu8Hy+eqNJCqfBR8P7Pg8g=="],

    "@rolldown/binding-win32-arm64-msvc": ["@rolldown/binding-win32-arm64-msvc@1.0.0-rc.9", "", { "os": "win32", "cpu": "arm64" }, "sha512-lHVNUG/8nlF1IQk1C0Ci574qKYyty2goMiPlRqkC5R+3LkXDkL5Dhx8ytbxq35m+pkHVIvIxviD+TWLdfeuadA=="],

    "@rolldown/binding-win32-x64-msvc": ["@rolldown/binding-win32-x64-msvc@1.0.0-rc.9", "", { "os": "win32", "cpu": "x64" }, "sha512-G0oA4+w1iY5AGi5HcDTxWsoxF509hrFIPB2rduV5aDqS9FtDg1CAfa7V34qImbjfhIcA8C+RekocJZA96EarwQ=="],

    "@rolldown/pluginutils": ["@rolldown/pluginutils@1.0.0-rc.9", "", {}, "sha512-w6oiRWgEBl04QkFZgmW+jnU1EC9b57Oihi2ot3HNWIQRqgHp5PnYDia5iZ5FF7rpa4EQdiqMDXjlqKGXBhsoXw=="],

    "@rollup/plugin-alias": ["@rollup/plugin-alias@6.0.0", "", { "peerDependencies": { "rollup": ">=4.0.0" }, "optionalPeers": ["rollup"] }, "sha512-tPCzJOtS7uuVZd+xPhoy5W4vThe6KWXNmsFCNktaAh5RTqcLiSfT4huPQIXkgJ6YCOjJHvecOAzQxLFhPxKr+g=="],

    "@rollup/plugin-commonjs": ["@rollup/plugin-commonjs@29.0.2", "", { "dependencies": { "@rollup/pluginutils": "^5.0.1", "commondir": "^1.0.1", "estree-walker": "^2.0.2", "fdir": "^6.2.0", "is-reference": "1.2.1", "magic-string": "^0.30.3", "picomatch": "^4.0.2" }, "peerDependencies": { "rollup": "^2.68.0||^3.0.0||^4.0.0" }, "optionalPeers": ["rollup"] }, "sha512-S/ggWH1LU7jTyi9DxZOKyxpVd4hF/OZ0JrEbeLjXk/DFXwRny0tjD2c992zOUYQobLrVkRVMDdmHP16HKP7GRg=="],

    "@rollup/plugin-inject": ["@rollup/plugin-inject@5.0.5", "", { "dependencies": { "@rollup/pluginutils": "^5.0.1", "estree-walker": "^2.0.2", "magic-string": "^0.30.3" }, "peerDependencies": { "rollup": "^1.20.0||^2.0.0||^3.0.0||^4.0.0" }, "optionalPeers": ["rollup"] }, "sha512-2+DEJbNBoPROPkgTDNe8/1YXWcqxbN5DTjASVIOx8HS+pITXushyNiBV56RB08zuptzz8gT3YfkqriTBVycepg=="],

    "@rollup/plugin-json": ["@rollup/plugin-json@6.1.0", "", { "dependencies": { "@rollup/pluginutils": "^5.1.0" }, "peerDependencies": { "rollup": "^1.20.0||^2.0.0||^3.0.0||^4.0.0" }, "optionalPeers": ["rollup"] }, "sha512-EGI2te5ENk1coGeADSIwZ7G2Q8CJS2sF120T7jLw4xFw9n7wIOXHo+kIYRAoVpJAN+kmqZSoO3Fp4JtoNF4ReA=="],

    "@rollup/plugin-node-resolve": ["@rollup/plugin-node-resolve@16.0.3", "", { "dependencies": { "@rollup/pluginutils": "^5.0.1", "@types/resolve": "1.20.2", "deepmerge": "^4.2.2", "is-module": "^1.0.0", "resolve": "^1.22.1" }, "peerDependencies": { "rollup": "^2.78.0||^3.0.0||^4.0.0" }, "optionalPeers": ["rollup"] }, "sha512-lUYM3UBGuM93CnMPG1YocWu7X802BrNF3jW2zny5gQyLQgRFJhV1Sq0Zi74+dh/6NBx1DxFC4b4GXg9wUCG5Qg=="],

    "@rollup/plugin-replace": ["@rollup/plugin-replace@6.0.3", "", { "dependencies": { "@rollup/pluginutils": "^5.0.1", "magic-string": "^0.30.3" }, "peerDependencies": { "rollup": "^1.20.0||^2.0.0||^3.0.0||^4.0.0" }, "optionalPeers": ["rollup"] }, "sha512-J4RZarRvQAm5IF0/LwUUg+obsm+xZhYnbMXmXROyoSE1ATJe3oXSb9L5MMppdxP2ylNSjv6zFBwKYjcKMucVfA=="],

    "@rollup/plugin-terser": ["@rollup/plugin-terser@0.4.4", "", { "dependencies": { "serialize-javascript": "^6.0.1", "smob": "^1.0.0", "terser": "^5.17.4" }, "peerDependencies": { "rollup": "^2.0.0||^3.0.0||^4.0.0" }, "optionalPeers": ["rollup"] }, "sha512-XHeJC5Bgvs8LfukDwWZp7yeqin6ns8RTl2B9avbejt6tZqsqvVoWI7ZTQrcNsfKEDWBTnTxM8nMDkO2IFFbd0A=="],

    "@rollup/pluginutils": ["@rollup/pluginutils@5.3.0", "", { "dependencies": { "@types/estree": "^1.0.0", "estree-walker": "^2.0.2", "picomatch": "^4.0.2" }, "peerDependencies": { "rollup": "^1.20.0||^2.0.0||^3.0.0||^4.0.0" }, "optionalPeers": ["rollup"] }, "sha512-5EdhGZtnu3V88ces7s53hhfK5KSASnJZv8Lulpc04cWO3REESroJXg73DFsOmgbU2BhwV0E20bu2IDZb3VKW4Q=="],

    "@rollup/rollup-android-arm-eabi": ["@rollup/rollup-android-arm-eabi@4.59.0", "", { "os": "android", "cpu": "arm" }, "sha512-upnNBkA6ZH2VKGcBj9Fyl9IGNPULcjXRlg0LLeaioQWueH30p6IXtJEbKAgvyv+mJaMxSm1l6xwDXYjpEMiLMg=="],

    "@rollup/rollup-android-arm64": ["@rollup/rollup-android-arm64@4.59.0", "", { "os": "android", "cpu": "arm64" }, "sha512-hZ+Zxj3SySm4A/DylsDKZAeVg0mvi++0PYVceVyX7hemkw7OreKdCvW2oQ3T1FMZvCaQXqOTHb8qmBShoqk69Q=="],

    "@rollup/rollup-darwin-arm64": ["@rollup/rollup-darwin-arm64@4.59.0", "", { "os": "darwin", "cpu": "arm64" }, "sha512-W2Psnbh1J8ZJw0xKAd8zdNgF9HRLkdWwwdWqubSVk0pUuQkoHnv7rx4GiF9rT4t5DIZGAsConRE3AxCdJ4m8rg=="],

    "@rollup/rollup-darwin-x64": ["@rollup/rollup-darwin-x64@4.59.0", "", { "os": "darwin", "cpu": "x64" }, "sha512-ZW2KkwlS4lwTv7ZVsYDiARfFCnSGhzYPdiOU4IM2fDbL+QGlyAbjgSFuqNRbSthybLbIJ915UtZBtmuLrQAT/w=="],

    "@rollup/rollup-freebsd-arm64": ["@rollup/rollup-freebsd-arm64@4.59.0", "", { "os": "freebsd", "cpu": "arm64" }, "sha512-EsKaJ5ytAu9jI3lonzn3BgG8iRBjV4LxZexygcQbpiU0wU0ATxhNVEpXKfUa0pS05gTcSDMKpn3Sx+QB9RlTTA=="],

    "@rollup/rollup-freebsd-x64": ["@rollup/rollup-freebsd-x64@4.59.0", "", { "os": "freebsd", "cpu": "x64" }, "sha512-d3DuZi2KzTMjImrxoHIAODUZYoUUMsuUiY4SRRcJy6NJoZ6iIqWnJu9IScV9jXysyGMVuW+KNzZvBLOcpdl3Vg=="],

    "@rollup/rollup-linux-arm-gnueabihf": ["@rollup/rollup-linux-arm-gnueabihf@4.59.0", "", { "os": "linux", "cpu": "arm" }, "sha512-t4ONHboXi/3E0rT6OZl1pKbl2Vgxf9vJfWgmUoCEVQVxhW6Cw/c8I6hbbu7DAvgp82RKiH7TpLwxnJeKv2pbsw=="],

    "@rollup/rollup-linux-arm-musleabihf": ["@rollup/rollup-linux-arm-musleabihf@4.59.0", "", { "os": "linux", "cpu": "arm" }, "sha512-CikFT7aYPA2ufMD086cVORBYGHffBo4K8MQ4uPS/ZnY54GKj36i196u8U+aDVT2LX4eSMbyHtyOh7D7Zvk2VvA=="],

    "@rollup/rollup-linux-arm64-gnu": ["@rollup/rollup-linux-arm64-gnu@4.59.0", "", { "os": "linux", "cpu": "arm64" }, "sha512-jYgUGk5aLd1nUb1CtQ8E+t5JhLc9x5WdBKew9ZgAXg7DBk0ZHErLHdXM24rfX+bKrFe+Xp5YuJo54I5HFjGDAA=="],

    "@rollup/rollup-linux-arm64-musl": ["@rollup/rollup-linux-arm64-musl@4.59.0", "", { "os": "linux", "cpu": "arm64" }, "sha512-peZRVEdnFWZ5Bh2KeumKG9ty7aCXzzEsHShOZEFiCQlDEepP1dpUl/SrUNXNg13UmZl+gzVDPsiCwnV1uI0RUA=="],

    "@rollup/rollup-linux-loong64-gnu": ["@rollup/rollup-linux-loong64-gnu@4.59.0", "", { "os": "linux", "cpu": "none" }, "sha512-gbUSW/97f7+r4gHy3Jlup8zDG190AuodsWnNiXErp9mT90iCy9NKKU0Xwx5k8VlRAIV2uU9CsMnEFg/xXaOfXg=="],

    "@rollup/rollup-linux-loong64-musl": ["@rollup/rollup-linux-loong64-musl@4.59.0", "", { "os": "linux", "cpu": "none" }, "sha512-yTRONe79E+o0FWFijasoTjtzG9EBedFXJMl888NBEDCDV9I2wGbFFfJQQe63OijbFCUZqxpHz1GzpbtSFikJ4Q=="],

    "@rollup/rollup-linux-ppc64-gnu": ["@rollup/rollup-linux-ppc64-gnu@4.59.0", "", { "os": "linux", "cpu": "ppc64" }, "sha512-sw1o3tfyk12k3OEpRddF68a1unZ5VCN7zoTNtSn2KndUE+ea3m3ROOKRCZxEpmT9nsGnogpFP9x6mnLTCaoLkA=="],

    "@rollup/rollup-linux-ppc64-musl": ["@rollup/rollup-linux-ppc64-musl@4.59.0", "", { "os": "linux", "cpu": "ppc64" }, "sha512-+2kLtQ4xT3AiIxkzFVFXfsmlZiG5FXYW7ZyIIvGA7Bdeuh9Z0aN4hVyXS/G1E9bTP/vqszNIN/pUKCk/BTHsKA=="],

    "@rollup/rollup-linux-riscv64-gnu": ["@rollup/rollup-linux-riscv64-gnu@4.59.0", "", { "os": "linux", "cpu": "none" }, "sha512-NDYMpsXYJJaj+I7UdwIuHHNxXZ/b/N2hR15NyH3m2qAtb/hHPA4g4SuuvrdxetTdndfj9b1WOmy73kcPRoERUg=="],

    "@rollup/rollup-linux-riscv64-musl": ["@rollup/rollup-linux-riscv64-musl@4.59.0", "", { "os": "linux", "cpu": "none" }, "sha512-nLckB8WOqHIf1bhymk+oHxvM9D3tyPndZH8i8+35p/1YiVoVswPid2yLzgX7ZJP0KQvnkhM4H6QZ5m0LzbyIAg=="],

    "@rollup/rollup-linux-s390x-gnu": ["@rollup/rollup-linux-s390x-gnu@4.59.0", "", { "os": "linux", "cpu": "s390x" }, "sha512-oF87Ie3uAIvORFBpwnCvUzdeYUqi2wY6jRFWJAy1qus/udHFYIkplYRW+wo+GRUP4sKzYdmE1Y3+rY5Gc4ZO+w=="],

    "@rollup/rollup-linux-x64-gnu": ["@rollup/rollup-linux-x64-gnu@4.59.0", "", { "os": "linux", "cpu": "x64" }, "sha512-3AHmtQq/ppNuUspKAlvA8HtLybkDflkMuLK4DPo77DfthRb71V84/c4MlWJXixZz4uruIH4uaa07IqoAkG64fg=="],

    "@rollup/rollup-linux-x64-musl": ["@rollup/rollup-linux-x64-musl@4.59.0", "", { "os": "linux", "cpu": "x64" }, "sha512-2UdiwS/9cTAx7qIUZB/fWtToJwvt0Vbo0zmnYt7ED35KPg13Q0ym1g442THLC7VyI6JfYTP4PiSOWyoMdV2/xg=="],

    "@rollup/rollup-openbsd-x64": ["@rollup/rollup-openbsd-x64@4.59.0", "", { "os": "openbsd", "cpu": "x64" }, "sha512-M3bLRAVk6GOwFlPTIxVBSYKUaqfLrn8l0psKinkCFxl4lQvOSz8ZrKDz2gxcBwHFpci0B6rttydI4IpS4IS/jQ=="],

    "@rollup/rollup-openharmony-arm64": ["@rollup/rollup-openharmony-arm64@4.59.0", "", { "os": "none", "cpu": "arm64" }, "sha512-tt9KBJqaqp5i5HUZzoafHZX8b5Q2Fe7UjYERADll83O4fGqJ49O1FsL6LpdzVFQcpwvnyd0i+K/VSwu/o/nWlA=="],

    "@rollup/rollup-win32-arm64-msvc": ["@rollup/rollup-win32-arm64-msvc@4.59.0", "", { "os": "win32", "cpu": "arm64" }, "sha512-V5B6mG7OrGTwnxaNUzZTDTjDS7F75PO1ae6MJYdiMu60sq0CqN5CVeVsbhPxalupvTX8gXVSU9gq+Rx1/hvu6A=="],

    "@rollup/rollup-win32-ia32-msvc": ["@rollup/rollup-win32-ia32-msvc@4.59.0", "", { "os": "win32", "cpu": "ia32" }, "sha512-UKFMHPuM9R0iBegwzKF4y0C4J9u8C6MEJgFuXTBerMk7EJ92GFVFYBfOZaSGLu6COf7FxpQNqhNS4c4icUPqxA=="],

    "@rollup/rollup-win32-x64-gnu": ["@rollup/rollup-win32-x64-gnu@4.59.0", "", { "os": "win32", "cpu": "x64" }, "sha512-laBkYlSS1n2L8fSo1thDNGrCTQMmxjYY5G0WFWjFFYZkKPjsMBsgJfGf4TLxXrF6RyhI60L8TMOjBMvXiTcxeA=="],

    "@rollup/rollup-win32-x64-msvc": ["@rollup/rollup-win32-x64-msvc@4.59.0", "", { "os": "win32", "cpu": "x64" }, "sha512-2HRCml6OztYXyJXAvdDXPKcawukWY2GpR5/nxKp4iBgiO3wcoEGkAaqctIbZcNB6KlUQBIqt8VYkNSj2397EfA=="],

    "@sec-ant/readable-stream": ["@sec-ant/readable-stream@0.4.1", "", {}, "sha512-831qok9r2t8AlxLko40y2ebgSDhenenCatLVeW/uBtnHPyhHOvG0C7TvfgecV+wHzIm5KUICgzmVpWS+IMEAeg=="],

    "@shikijs/core": ["@shikijs/core@3.23.0", "", { "dependencies": { "@shikijs/types": "3.23.0", "@shikijs/vscode-textmate": "^10.0.2", "@types/hast": "^3.0.4", "hast-util-to-html": "^9.0.5" } }, "sha512-NSWQz0riNb67xthdm5br6lAkvpDJRTgB36fxlo37ZzM2yq0PQFFzbd8psqC2XMPgCzo1fW6cVi18+ArJ44wqgA=="],

    "@shikijs/engine-javascript": ["@shikijs/engine-javascript@3.23.0", "", { "dependencies": { "@shikijs/types": "3.23.0", "@shikijs/vscode-textmate": "^10.0.2", "oniguruma-to-es": "^4.3.4" } }, "sha512-aHt9eiGFobmWR5uqJUViySI1bHMqrAgamWE1TYSUoftkAeCCAiGawPMwM+VCadylQtF4V3VNOZ5LmfItH5f3yA=="],

    "@shikijs/engine-oniguruma": ["@shikijs/engine-oniguruma@3.23.0", "", { "dependencies": { "@shikijs/types": "3.23.0", "@shikijs/vscode-textmate": "^10.0.2" } }, "sha512-1nWINwKXxKKLqPibT5f4pAFLej9oZzQTsby8942OTlsJzOBZ0MWKiwzMsd+jhzu8YPCHAswGnnN1YtQfirL35g=="],

    "@shikijs/langs": ["@shikijs/langs@3.23.0", "", { "dependencies": { "@shikijs/types": "3.23.0" } }, "sha512-2Ep4W3Re5aB1/62RSYQInK9mM3HsLeB91cHqznAJMuylqjzNVAVCMnNWRHFtcNHXsoNRayP9z1qj4Sq3nMqYXg=="],

    "@shikijs/themes": ["@shikijs/themes@3.23.0", "", { "dependencies": { "@shikijs/types": "3.23.0" } }, "sha512-5qySYa1ZgAT18HR/ypENL9cUSGOeI2x+4IvYJu4JgVJdizn6kG4ia5Q1jDEOi7gTbN4RbuYtmHh0W3eccOrjMA=="],

    "@shikijs/types": ["@shikijs/types@3.23.0", "", { "dependencies": { "@shikijs/vscode-textmate": "^10.0.2", "@types/hast": "^3.0.4" } }, "sha512-3JZ5HXOZfYjsYSk0yPwBrkupyYSLpAE26Qc0HLghhZNGTZg/SKxXIIgoxOpmmeQP0RRSDJTk1/vPfw9tbw+jSQ=="],

    "@shikijs/vscode-textmate": ["@shikijs/vscode-textmate@10.0.2", "", {}, "sha512-83yeghZ2xxin3Nj8z1NMd/NCuca+gsYXswywDy5bHvwlWL8tpTQmzGeUuHd9FC3E/SBEMvzJRwWEOz5gGes9Qg=="],

    "@sindresorhus/is": ["@sindresorhus/is@7.2.0", "", {}, "sha512-P1Cz1dWaFfR4IR+U13mqqiGsLFf1KbayybWwdd2vfctdV6hDpUkgCY0nKOLLTMSoRd/jJNjtbqzf13K8DCCXQw=="],

    "@sindresorhus/merge-streams": ["@sindresorhus/merge-streams@4.0.0", "", {}, "sha512-tlqY9xq5ukxTUZBmoOp+m61cqwQD5pHJtFY3Mn8CA8ps6yghLH/Hw8UPdqg4OLmFW3IFlcXnQNmo/dh8HzXYIQ=="],

    "@speed-highlight/core": ["@speed-highlight/core@1.2.14", "", {}, "sha512-G4ewlBNhUtlLvrJTb88d2mdy2KRijzs4UhnlrOSRT4bmjh/IqNElZa3zkrZ+TC47TwtlDWzVLFADljF1Ijp5hA=="],

    "@tybys/wasm-util": ["@tybys/wasm-util@0.10.1", "", { "dependencies": { "tslib": "^2.4.0" } }, "sha512-9tTaPJLSiejZKx+Bmog4uSubteqTvFrVrURwkmHixBo0G4seD0zUxp98E1DzUBJxLQ3NPwXrGKDiVjwx/DpPsg=="],

    "@types/babel__core": ["@types/babel__core@7.20.5", "", { "dependencies": { "@babel/parser": "^7.20.7", "@babel/types": "^7.20.7", "@types/babel__generator": "*", "@types/babel__template": "*", "@types/babel__traverse": "*" } }, "sha512-qoQprZvz5wQFJwMDqeseRXWv3rqMvhgpbXFfVyWhbx9X47POIA6i/+dXefEmZKoAgOaTdaIgNSMqMIU61yRyzA=="],

    "@types/babel__generator": ["@types/babel__generator@7.27.0", "", { "dependencies": { "@babel/types": "^7.0.0" } }, "sha512-ufFd2Xi92OAVPYsy+P4n7/U7e68fex0+Ee8gSG9KX7eo084CWiQ4sdxktvdl0bOPupXtVJPY19zk6EwWqUQ8lg=="],

    "@types/babel__template": ["@types/babel__template@7.4.4", "", { "dependencies": { "@babel/parser": "^7.1.0", "@babel/types": "^7.0.0" } }, "sha512-h/NUaSyG5EyxBIp8YRxo4RMe2/qQgvyowRwVMzhYhBCONbW8PUsg4lkFMrhgZhUe5z3L3MiLDuvyJ/CaPa2A8A=="],

    "@types/babel__traverse": ["@types/babel__traverse@7.28.0", "", { "dependencies": { "@babel/types": "^7.28.2" } }, "sha512-8PvcXf70gTDZBgt9ptxJ8elBeBjcLOAcOtoO/mPJjtji1+CdGbHgm77om1GrsPxsiE+uXIpNSK64UYaIwQXd4Q=="],

    "@types/debug": ["@types/debug@4.1.12", "", { "dependencies": { "@types/ms": "*" } }, "sha512-vIChWdVG3LG1SMxEvI/AK+FWJthlrqlTu7fbrlywTkkaONwk/UAGaULXRlf8vkzFBLVm0zkMdCquhL5aOjhXPQ=="],

    "@types/estree": ["@types/estree@1.0.8", "", {}, "sha512-dWHzHa2WqEXI/O1E9OjrocMTKJl2mSrEolh1Iomrv6U+JuNwaHXsXx9bLu5gG7BUWFIN0skIQJQ/L1rIex4X6w=="],

    "@types/hast": ["@types/hast@3.0.4", "", { "dependencies": { "@types/unist": "*" } }, "sha512-WPs+bbQw5aCj+x6laNGWLH3wviHtoCv/P3+otBhbOhJgG8qtpdAMlTCxLtsTWA7LH1Oh/bFCHsBn0TPS5m30EQ=="],

    "@types/jsesc": ["@types/jsesc@2.5.1", "", {}, "sha512-9VN+6yxLOPLOav+7PwjZbxiID2bVaeq0ED4qSQmdQTdjnXJSaCVKTR58t15oqH1H5t8Ng2ZX1SabJVoN9Q34bw=="],

    "@types/mdast": ["@types/mdast@4.0.4", "", { "dependencies": { "@types/unist": "*" } }, "sha512-kGaNbPh1k7AFzgpud/gMdvIm5xuECykRR+JnWKQno9TAXVa6WIVCGTPvYGekIDL4uwCZQSYbUxNBSb1aUo79oA=="],

    "@types/ms": ["@types/ms@2.1.0", "", {}, "sha512-GsCCIZDE/p3i96vtEqx+7dBUGXrc7zeSK3wwPHIaRThS+9OhWIXRqzs4d6k1SVU8g91DrNRWxWUGhp5KXQb2VA=="],

    "@types/nlcst": ["@types/nlcst@2.0.3", "", { "dependencies": { "@types/unist": "*" } }, "sha512-vSYNSDe6Ix3q+6Z7ri9lyWqgGhJTmzRjZRqyq15N0Z/1/UnVsno9G/N40NBijoYx2seFDIl0+B2mgAb9mezUCA=="],

    "@types/react": ["@types/react@19.2.14", "", { "dependencies": { "csstype": "^3.2.2" } }, "sha512-ilcTH/UniCkMdtexkoCN0bI7pMcJDvmQFPvuPvmEaYA/NSfFTAgdUSLAoVjaRJm7+6PvcM+q1zYOwS4wTYMF9w=="],

    "@types/react-dom": ["@types/react-dom@19.2.3", "", { "peerDependencies": { "@types/react": "^19.2.0" } }, "sha512-jp2L/eY6fn+KgVVQAOqYItbF0VY/YApe5Mz2F0aykSO8gx31bYCZyvSeYxCHKvzHG5eZjc+zyaS5BrBWya2+kQ=="],

    "@types/resolve": ["@types/resolve@1.20.2", "", {}, "sha512-60BCwRFOZCQhDncwQdxxeOEEkbc5dIMccYLwbxsS4TUNeVECQ/pBJ0j09mrHOl/JJvpRPGwO9SvE4nR2Nb/a4Q=="],

    "@types/unist": ["@types/unist@3.0.3", "", {}, "sha512-ko/gIFJRv177XgZsZcBwnqJN5x/Gien8qNOn0D5bQU/zAzVf9Zt3BlcUiLqhV9y4ARk0GbT3tnUiPNgnTXzc/Q=="],

    "@ungap/structured-clone": ["@ungap/structured-clone@1.3.0", "", {}, "sha512-WmoN8qaIAo7WTYWbAZuG8PYEhn5fkz7dZrqTBZ7dtt//lL2Gwms1IcnQ5yHqjDfX8Ft5j4YzDM23f87zBfDe9g=="],

    "@unhead/vue": ["@unhead/vue@2.1.12", "", { "dependencies": { "hookable": "^6.0.1", "unhead": "2.1.12" }, "peerDependencies": { "vue": ">=3.5.18" } }, "sha512-zEWqg0nZM8acpuTZE40wkeUl8AhIe0tU0OkilVi1D4fmVjACrwoh5HP6aNqJ8kUnKsoy6D+R3Vi/O+fmdNGO7g=="],

    "@vercel/nft": ["@vercel/nft@1.3.2", "", { "dependencies": { "@mapbox/node-pre-gyp": "^2.0.0", "@rollup/pluginutils": "^5.1.3", "acorn": "^8.6.0", "acorn-import-attributes": "^1.9.5", "async-sema": "^3.1.1", "bindings": "^1.4.0", "estree-walker": "2.0.2", "glob": "^13.0.0", "graceful-fs": "^4.2.9", "node-gyp-build": "^4.2.2", "picomatch": "^4.0.2", "resolve-from": "^5.0.0" }, "bin": { "nft": "out/cli.js" } }, "sha512-HC8venRc4Ya7vNeBsJneKHHMDDWpQie7VaKhAIOst3MKO+DES+Y/SbzSp8mFkD7OzwAE2HhHkeSuSmwS20mz3A=="],

    "@vitejs/plugin-react": ["@vitejs/plugin-react@4.7.0", "", { "dependencies": { "@babel/core": "^7.28.0", "@babel/plugin-transform-react-jsx-self": "^7.27.1", "@babel/plugin-transform-react-jsx-source": "^7.27.1", "@rolldown/pluginutils": "1.0.0-beta.27", "@types/babel__core": "^7.20.5", "react-refresh": "^0.17.0" }, "peerDependencies": { "vite": "^4.2.0 || ^5.0.0 || ^6.0.0 || ^7.0.0" } }, "sha512-gUu9hwfWvvEDBBmgtAowQCojwZmJ5mcLn3aufeCsitijs3+f2NsrPtlAWIR6OPiqljl96GVCUbLe0HyqIpVaoA=="],

    "@vitejs/plugin-vue": ["@vitejs/plugin-vue@5.2.4", "", { "peerDependencies": { "vite": "^5.0.0 || ^6.0.0", "vue": "^3.2.25" } }, "sha512-7Yx/SXSOcQq5HiiV3orevHUFn+pmMB4cgbEkDYgnkUWb0WfeQ/wa2yFv6D5ICiCQOVpjA7vYDXrC7AGO8yjDHA=="],

    "@vitejs/plugin-vue-jsx": ["@vitejs/plugin-vue-jsx@4.2.0", "", { "dependencies": { "@babel/core": "^7.27.1", "@babel/plugin-transform-typescript": "^7.27.1", "@rolldown/pluginutils": "^1.0.0-beta.9", "@vue/babel-plugin-jsx": "^1.4.0" }, "peerDependencies": { "vite": "^5.0.0 || ^6.0.0", "vue": "^3.0.0" } }, "sha512-DSTrmrdLp+0LDNF77fqrKfx7X0ErRbOcUAgJL/HbSesqQwoUvUQ4uYQqaex+rovqgGcoPqVk+AwUh3v9CuiYIw=="],

    "@volar/kit": ["@volar/kit@2.4.28", "", { "dependencies": { "@volar/language-service": "2.4.28", "@volar/typescript": "2.4.28", "typesafe-path": "^0.2.2", "vscode-languageserver-textdocument": "^1.0.11", "vscode-uri": "^3.0.8" }, "peerDependencies": { "typescript": "*" } }, "sha512-cKX4vK9dtZvDRaAzeoUdaAJEew6IdxHNCRrdp5Kvcl6zZOqb6jTOfk3kXkIkG3T7oTFXguEMt5+9ptyqYR84Pg=="],

    "@volar/language-core": ["@volar/language-core@2.4.28", "", { "dependencies": { "@volar/source-map": "2.4.28" } }, "sha512-w4qhIJ8ZSitgLAkVay6AbcnC7gP3glYM3fYwKV3srj8m494E3xtrCv6E+bWviiK/8hs6e6t1ij1s2Endql7vzQ=="],

    "@volar/language-server": ["@volar/language-server@2.4.28", "", { "dependencies": { "@volar/language-core": "2.4.28", "@volar/language-service": "2.4.28", "@volar/typescript": "2.4.28", "path-browserify": "^1.0.1", "request-light": "^0.7.0", "vscode-languageserver": "^9.0.1", "vscode-languageserver-protocol": "^3.17.5", "vscode-languageserver-textdocument": "^1.0.11", "vscode-uri": "^3.0.8" } }, "sha512-NqcLnE5gERKuS4PUFwlhMxf6vqYo7hXtbMFbViXcbVkbZ905AIVWhnSo0ZNBC2V127H1/2zP7RvVOVnyITFfBw=="],

    "@volar/language-service": ["@volar/language-service@2.4.28", "", { "dependencies": { "@volar/language-core": "2.4.28", "vscode-languageserver-protocol": "^3.17.5", "vscode-languageserver-textdocument": "^1.0.11", "vscode-uri": "^3.0.8" } }, "sha512-Rh/wYCZJrI5vCwMk9xyw/Z+MsWxlJY1rmMZPsxUoJKfzIRjS/NF1NmnuEcrMbEVGja00aVpCsInJfixQTMdvLw=="],

    "@volar/source-map": ["@volar/source-map@2.4.28", "", {}, "sha512-yX2BDBqJkRXfKw8my8VarTyjv48QwxdJtvRgUpNE5erCsgEUdI2DsLbpa+rOQVAJYshY99szEcRDmyHbF10ggQ=="],

    "@volar/typescript": ["@volar/typescript@2.4.28", "", { "dependencies": { "@volar/language-core": "2.4.28", "path-browserify": "^1.0.1", "vscode-uri": "^3.0.8" } }, "sha512-Ja6yvWrbis2QtN4ClAKreeUZPVYMARDYZl9LMEv1iQ1QdepB6wn0jTRxA9MftYmYa4DQ4k/DaSZpFPUfxl8giw=="],

    "@vscode/emmet-helper": ["@vscode/emmet-helper@2.11.0", "", { "dependencies": { "emmet": "^2.4.3", "jsonc-parser": "^2.3.0", "vscode-languageserver-textdocument": "^1.0.1", "vscode-languageserver-types": "^3.15.1", "vscode-uri": "^3.0.8" } }, "sha512-QLxjQR3imPZPQltfbWRnHU6JecWTF1QSWhx3GAKQpslx7y3Dp6sIIXhKjiUJ/BR9FX8PVthjr9PD6pNwOJfAzw=="],

    "@vscode/l10n": ["@vscode/l10n@0.0.18", "", {}, "sha512-KYSIHVmslkaCDyw013pphY+d7x1qV8IZupYfeIfzNA+nsaWHbn5uPuQRvdRFsa9zFzGeudPuoGoZ1Op4jrJXIQ=="],

    "@vue-macros/common": ["@vue-macros/common@3.1.2", "", { "dependencies": { "@vue/compiler-sfc": "^3.5.22", "ast-kit": "^2.1.2", "local-pkg": "^1.1.2", "magic-string-ast": "^1.0.2", "unplugin-utils": "^0.3.0" }, "peerDependencies": { "vue": "^2.7.0 || ^3.2.25" }, "optionalPeers": ["vue"] }, "sha512-h9t4ArDdniO9ekYHAD95t9AZcAbb19lEGK+26iAjUODOIJKmObDNBSe4+6ELQAA3vtYiFPPBtHh7+cQCKi3Dng=="],

    "@vue/babel-helper-vue-transform-on": ["@vue/babel-helper-vue-transform-on@1.5.0", "", {}, "sha512-0dAYkerNhhHutHZ34JtTl2czVQHUNWv6xEbkdF5W+Yrv5pCWsqjeORdOgbtW2I9gWlt+wBmVn+ttqN9ZxR5tzA=="],

    "@vue/babel-plugin-jsx": ["@vue/babel-plugin-jsx@1.5.0", "", { "dependencies": { "@babel/helper-module-imports": "^7.27.1", "@babel/helper-plugin-utils": "^7.27.1", "@babel/plugin-syntax-jsx": "^7.27.1", "@babel/template": "^7.27.2", "@babel/traverse": "^7.28.0", "@babel/types": "^7.28.2", "@vue/babel-helper-vue-transform-on": "1.5.0", "@vue/babel-plugin-resolve-type": "1.5.0", "@vue/shared": "^3.5.18" }, "peerDependencies": { "@babel/core": "^7.0.0-0" }, "optionalPeers": ["@babel/core"] }, "sha512-mneBhw1oOqCd2247O0Yw/mRwC9jIGACAJUlawkmMBiNmL4dGA2eMzuNZVNqOUfYTa6vqmND4CtOPzmEEEqLKFw=="],

    "@vue/babel-plugin-resolve-type": ["@vue/babel-plugin-resolve-type@1.5.0", "", { "dependencies": { "@babel/code-frame": "^7.27.1", "@babel/helper-module-imports": "^7.27.1", "@babel/helper-plugin-utils": "^7.27.1", "@babel/parser": "^7.28.0", "@vue/compiler-sfc": "^3.5.18" }, "peerDependencies": { "@babel/core": "^7.0.0-0" } }, "sha512-Wm/60o+53JwJODm4Knz47dxJnLDJ9FnKnGZJbUUf8nQRAtt6P+undLUAVU3Ha33LxOJe6IPoifRQ6F/0RrU31w=="],

    "@vue/compiler-core": ["@vue/compiler-core@3.5.30", "", { "dependencies": { "@babel/parser": "^7.29.0", "@vue/shared": "3.5.30", "entities": "^7.0.1", "estree-walker": "^2.0.2", "source-map-js": "^1.2.1" } }, "sha512-s3DfdZkcu/qExZ+td75015ljzHc6vE+30cFMGRPROYjqkroYI5NV2X1yAMX9UeyBNWB9MxCfPcsjpLS11nzkkw=="],

    "@vue/compiler-dom": ["@vue/compiler-dom@3.5.30", "", { "dependencies": { "@vue/compiler-core": "3.5.30", "@vue/shared": "3.5.30" } }, "sha512-eCFYESUEVYHhiMuK4SQTldO3RYxyMR/UQL4KdGD1Yrkfdx4m/HYuZ9jSfPdA+nWJY34VWndiYdW/wZXyiPEB9g=="],

    "@vue/compiler-sfc": ["@vue/compiler-sfc@3.5.30", "", { "dependencies": { "@babel/parser": "^7.29.0", "@vue/compiler-core": "3.5.30", "@vue/compiler-dom": "3.5.30", "@vue/compiler-ssr": "3.5.30", "@vue/shared": "3.5.30", "estree-walker": "^2.0.2", "magic-string": "^0.30.21", "postcss": "^8.5.8", "source-map-js": "^1.2.1" } }, "sha512-LqmFPDn89dtU9vI3wHJnwaV6GfTRD87AjWpTWpyrdVOObVtjIuSeZr181z5C4PmVx/V3j2p+0f7edFKGRMpQ5A=="],

    "@vue/compiler-ssr": ["@vue/compiler-ssr@3.5.30", "", { "dependencies": { "@vue/compiler-dom": "3.5.30", "@vue/shared": "3.5.30" } }, "sha512-NsYK6OMTnx109PSL2IAyf62JP6EUdk4Dmj6AkWcJGBvN0dQoMYtVekAmdqgTtWQgEJo+Okstbf/1p7qZr5H+bA=="],

    "@vue/devtools-api": ["@vue/devtools-api@8.1.0", "", { "dependencies": { "@vue/devtools-kit": "^8.1.0" } }, "sha512-O44X57jjkLKbLEc4OgL/6fEPOOanRJU8kYpCE8qfKlV96RQZcdzrcLI5mxMuVRUeXhHKIHGhCpHacyCk0HyO4w=="],

    "@vue/devtools-core": ["@vue/devtools-core@7.7.9", "", { "dependencies": { "@vue/devtools-kit": "^7.7.9", "@vue/devtools-shared": "^7.7.9", "mitt": "^3.0.1", "nanoid": "^5.1.0", "pathe": "^2.0.3", "vite-hot-client": "^2.0.4" }, "peerDependencies": { "vue": "^3.0.0" } }, "sha512-48jrBSwG4GVQRvVeeXn9p9+dlx+ISgasM7SxZZKczseohB0cBz+ITKr4YbLWjmJdy45UHL7UMPlR4Y0CWTRcSQ=="],

    "@vue/devtools-kit": ["@vue/devtools-kit@7.7.9", "", { "dependencies": { "@vue/devtools-shared": "^7.7.9", "birpc": "^2.3.0", "hookable": "^5.5.3", "mitt": "^3.0.1", "perfect-debounce": "^1.0.0", "speakingurl": "^14.0.1", "superjson": "^2.2.2" } }, "sha512-PyQ6odHSgiDVd4hnTP+aDk2X4gl2HmLDfiyEnn3/oV+ckFDuswRs4IbBT7vacMuGdwY/XemxBoh302ctbsptuA=="],

    "@vue/devtools-shared": ["@vue/devtools-shared@7.7.9", "", { "dependencies": { "rfdc": "^1.4.1" } }, "sha512-iWAb0v2WYf0QWmxCGy0seZNDPdO3Sp5+u78ORnyeonS6MT4PC7VPrryX2BpMJrwlDeaZ6BD4vP4XKjK0SZqaeA=="],

    "@vue/language-core": ["@vue/language-core@3.2.6", "", { "dependencies": { "@volar/language-core": "2.4.28", "@vue/compiler-dom": "^3.5.0", "@vue/shared": "^3.5.0", "alien-signals": "^3.0.0", "muggle-string": "^0.4.1", "path-browserify": "^1.0.1", "picomatch": "^4.0.2" } }, "sha512-xYYYX3/aVup576tP/23sEUpgiEnujrENaoNRbaozC1/MA9I6EGFQRJb4xrt/MmUCAGlxTKL2RmT8JLTPqagCkg=="],

    "@vue/reactivity": ["@vue/reactivity@3.5.30", "", { "dependencies": { "@vue/shared": "3.5.30" } }, "sha512-179YNgKATuwj9gB+66snskRDOitDiuOZqkYia7mHKJaidOMo/WJxHKF8DuGc4V4XbYTJANlfEKb0yxTQotnx4Q=="],

    "@vue/runtime-core": ["@vue/runtime-core@3.5.30", "", { "dependencies": { "@vue/reactivity": "3.5.30", "@vue/shared": "3.5.30" } }, "sha512-e0Z+8PQsUTdwV8TtEsLzUM7SzC7lQwYKePydb7K2ZnmS6jjND+WJXkmmfh/swYzRyfP1EY3fpdesyYoymCzYfg=="],

    "@vue/runtime-dom": ["@vue/runtime-dom@3.5.30", "", { "dependencies": { "@vue/reactivity": "3.5.30", "@vue/runtime-core": "3.5.30", "@vue/shared": "3.5.30", "csstype": "^3.2.3" } }, "sha512-2UIGakjU4WSQ0T4iwDEW0W7vQj6n7AFn7taqZ9Cvm0Q/RA2FFOziLESrDL4GmtI1wV3jXg5nMoJSYO66egDUBw=="],

    "@vue/server-renderer": ["@vue/server-renderer@3.5.30", "", { "dependencies": { "@vue/compiler-ssr": "3.5.30", "@vue/shared": "3.5.30" }, "peerDependencies": { "vue": "3.5.30" } }, "sha512-v+R34icapydRwbZRD0sXwtHqrQJv38JuMB4JxbOxd8NEpGLny7cncMp53W9UH/zo4j8eDHjQ1dEJXwzFQknjtQ=="],

    "@vue/shared": ["@vue/shared@3.5.30", "", {}, "sha512-YXgQ7JjaO18NeK2K9VTbDHaFy62WrObMa6XERNfNOkAhD1F1oDSf3ZJ7K6GqabZ0BvSDHajp8qfS5Sa2I9n8uQ=="],

    "abbrev": ["abbrev@3.0.1", "", {}, "sha512-AO2ac6pjRB3SJmGJo+v5/aK6Omggp6fsLrs6wN9bd35ulu4cCwaAU9+7ZhXjeqHVkaHThLuzH0nZr0YpCDhygg=="],

    "abort-controller": ["abort-controller@3.0.0", "", { "dependencies": { "event-target-shim": "^5.0.0" } }, "sha512-h8lQ8tacZYnR3vNQTgibj+tODHI5/+l06Au2Pcriv/Gmet0eaj4TwWH41sO9wnHDiQsEj19q0drzdWdeAHtweg=="],

    "acorn": ["acorn@8.16.0", "", { "bin": { "acorn": "bin/acorn" } }, "sha512-UVJyE9MttOsBQIDKw1skb9nAwQuR5wuGD3+82K6JgJlm/Y+KI92oNsMNGZCYdDsVtRHSak0pcV5Dno5+4jh9sw=="],

    "acorn-import-attributes": ["acorn-import-attributes@1.9.5", "", { "peerDependencies": { "acorn": "^8" } }, "sha512-n02Vykv5uA3eHGM/Z2dQrcD56kL8TyDb2p1+0P83PClMnC/nc+anbQRhIOWnSq4Ke/KvDPrY3C9hDtC/A3eHnQ=="],

    "agent-base": ["agent-base@7.1.4", "", {}, "sha512-MnA+YT8fwfJPgBx3m60MNqakm30XOkyIoH1y6huTQvC0PwZG7ki8NacLBcrPbNoo8vEZy7Jpuk7+jMO+CUovTQ=="],

    "ajv": ["ajv@8.18.0", "", { "dependencies": { "fast-deep-equal": "^3.1.3", "fast-uri": "^3.0.1", "json-schema-traverse": "^1.0.0", "require-from-string": "^2.0.2" } }, "sha512-PlXPeEWMXMZ7sPYOHqmDyCJzcfNrUr3fGNKtezX14ykXOEIvyK81d+qydx89KY5O71FKMPaQ2vBfBFI5NHR63A=="],

    "ajv-draft-04": ["ajv-draft-04@1.0.0", "", { "peerDependencies": { "ajv": "^8.5.0" }, "optionalPeers": ["ajv"] }, "sha512-mv00Te6nmYbRp5DCwclxtt7yV/joXJPGS7nM+97GdxvuttCOfgI3K4U25zboyeX0O+myI8ERluxQe5wljMmVIw=="],

    "alien-signals": ["alien-signals@3.1.2", "", {}, "sha512-d9dYqZTS90WLiU0I5c6DHj/HcKkF8ZyGN3G5x8wSbslulz70KOxaqCT0hQCo9KOyhVqzqGojvNdJXoTumZOtcw=="],

    "ansi-align": ["ansi-align@3.0.1", "", { "dependencies": { "string-width": "^4.1.0" } }, "sha512-IOfwwBF5iczOjp/WeY4YxyjqAFMQoZufdQWDd19SEExbVLNXqvpzSJ/M7Za4/sCPmQ0+GRquoA7bGcINcxew6w=="],

    "ansi-regex": ["ansi-regex@5.0.1", "", {}, "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ=="],

    "ansi-styles": ["ansi-styles@6.2.3", "", {}, "sha512-4Dj6M28JB+oAH8kFkTLUo+a2jwOFkuqb3yucU0CANcRRUbxS0cP0nZYCGjcc3BNXwRIsUVmDGgzawme7zvJHvg=="],

    "ansis": ["ansis@4.2.0", "", {}, "sha512-HqZ5rWlFjGiV0tDm3UxxgNRqsOTniqoKZu0pIAfh7TZQMGuZK+hH0drySty0si0QXj1ieop4+SkSfPZBPPkHig=="],

    "anymatch": ["anymatch@3.1.3", "", { "dependencies": { "normalize-path": "^3.0.0", "picomatch": "^2.0.4" } }, "sha512-KMReFUr0B4t+D+OBkjR3KYqvocp2XaSzO55UcB6mgQMd3KbcE+mWTyvVV7D/zsdEbNnV6acZUutkiHQXvTr1Rw=="],

    "archiver": ["archiver@7.0.1", "", { "dependencies": { "archiver-utils": "^5.0.2", "async": "^3.2.4", "buffer-crc32": "^1.0.0", "readable-stream": "^4.0.0", "readdir-glob": "^1.1.2", "tar-stream": "^3.0.0", "zip-stream": "^6.0.1" } }, "sha512-ZcbTaIqJOfCc03QwD468Unz/5Ir8ATtvAHsK+FdXbDIbGfihqh9mrvdcYunQzqn4HrvWWaFyaxJhGZagaJJpPQ=="],

    "archiver-utils": ["archiver-utils@5.0.2", "", { "dependencies": { "glob": "^10.0.0", "graceful-fs": "^4.2.0", "is-stream": "^2.0.1", "lazystream": "^1.0.0", "lodash": "^4.17.15", "normalize-path": "^3.0.0", "readable-stream": "^4.0.0" } }, "sha512-wuLJMmIBQYCsGZgYLTy5FIB2pF6Lfb6cXMSF8Qywwk3t20zWnAi7zLcQFdKQmIB8wyZpY5ER38x08GbwtR2cLA=="],

    "argparse": ["argparse@2.0.1", "", {}, "sha512-8+9WqebbFzpX9OR+Wa6O29asIogeRMzcGtAINdpMHHyAg10f05aSFVBbcEqGf/PXw1EjAZ+q2/bEBg3DvurK3Q=="],

    "aria-query": ["aria-query@5.3.2", "", {}, "sha512-COROpnaoap1E2F000S62r6A60uHZnmlvomhfyT2DlTcrY1OrBKn2UhH7qn5wTC9zMvD0AY7csdPSNwKP+7WiQw=="],

    "array-iterate": ["array-iterate@2.0.1", "", {}, "sha512-I1jXZMjAgCMmxT4qxXfPXa6SthSoE8h6gkSI9BGGNv8mP8G/v0blc+qFnZu6K42vTOiuME596QaLO0TP3Lk0xg=="],

    "ast-kit": ["ast-kit@3.0.0-beta.1", "", { "dependencies": { "@babel/parser": "^8.0.0-beta.4", "estree-walker": "^3.0.3", "pathe": "^2.0.3" } }, "sha512-trmleAnZ2PxN/loHWVhhx1qeOHSRXq4TDsBBxq3GqeJitfk3+jTQ+v/C1km/KYq9M7wKqCewMh+/NAvVH7m+bw=="],

    "ast-walker-scope": ["ast-walker-scope@0.8.3", "", { "dependencies": { "@babel/parser": "^7.28.4", "ast-kit": "^2.1.3" } }, "sha512-cbdCP0PGOBq0ASG+sjnKIoYkWMKhhz+F/h9pRexUdX2Hd38+WOlBkRKlqkGOSm0YQpcFMQBJeK4WspUAkwsEdg=="],

    "astro": ["astro@5.18.1", "", { "dependencies": { "@astrojs/compiler": "^2.13.0", "@astrojs/internal-helpers": "0.7.6", "@astrojs/markdown-remark": "6.3.11", "@astrojs/telemetry": "3.3.0", "@capsizecss/unpack": "^4.0.0", "@oslojs/encoding": "^1.1.0", "@rollup/pluginutils": "^5.3.0", "acorn": "^8.15.0", "aria-query": "^5.3.2", "axobject-query": "^4.1.0", "boxen": "8.0.1", "ci-info": "^4.3.1", "clsx": "^2.1.1", "common-ancestor-path": "^1.0.1", "cookie": "^1.1.1", "cssesc": "^3.0.0", "debug": "^4.4.3", "deterministic-object-hash": "^2.0.2", "devalue": "^5.6.2", "diff": "^8.0.3", "dlv": "^1.1.3", "dset": "^3.1.4", "es-module-lexer": "^1.7.0", "esbuild": "^0.27.3", "estree-walker": "^3.0.3", "flattie": "^1.1.1", "fontace": "~0.4.0", "github-slugger": "^2.0.0", "html-escaper": "3.0.3", "http-cache-semantics": "^4.2.0", "import-meta-resolve": "^4.2.0", "js-yaml": "^4.1.1", "magic-string": "^0.30.21", "magicast": "^0.5.1", "mrmime": "^2.0.1", "neotraverse": "^0.6.18", "p-limit": "^6.2.0", "p-queue": "^8.1.1", "package-manager-detector": "^1.6.0", "piccolore": "^0.1.3", "picomatch": "^4.0.3", "prompts": "^2.4.2", "rehype": "^13.0.2", "semver": "^7.7.3", "shiki": "^3.21.0", "smol-toml": "^1.6.0", "svgo": "^4.0.0", "tinyexec": "^1.0.2", "tinyglobby": "^0.2.15", "tsconfck": "^3.1.6", "ultrahtml": "^1.6.0", "unifont": "~0.7.3", "unist-util-visit": "^5.0.0", "unstorage": "^1.17.4", "vfile": "^6.0.3", "vite": "^6.4.1", "vitefu": "^1.1.1", "xxhash-wasm": "^1.1.0", "yargs-parser": "^21.1.1", "yocto-spinner": "^0.2.3", "zod": "^3.25.76", "zod-to-json-schema": "^3.25.1", "zod-to-ts": "^1.2.0" }, "optionalDependencies": { "sharp": "^0.34.0" }, "bin": { "astro": "astro.js" } }, "sha512-m4VWilWZ+Xt6NPoYzC4CgGZim/zQUO7WFL0RHCH0AiEavF1153iC3+me2atDvXpf/yX4PyGUeD8wZLq1cirT3g=="],

    "async": ["async@3.2.6", "", {}, "sha512-htCUDlxyyCLMgaM3xXg0C0LW2xqfuQ6p05pCEIsXuyQ+a1koYKTuBMzRNwmybfLgvJDMd0r1LTn4+E0Ti6C2AA=="],

    "async-sema": ["async-sema@3.1.1", "", {}, "sha512-tLRNUXati5MFePdAk8dw7Qt7DpxPB60ofAgn8WRhW6a2rcimZnYBP9oxHiv0OHy+Wz7kPMG+t4LGdt31+4EmGg=="],

    "autoprefixer": ["autoprefixer@10.4.27", "", { "dependencies": { "browserslist": "^4.28.1", "caniuse-lite": "^1.0.30001774", "fraction.js": "^5.3.4", "picocolors": "^1.1.1", "postcss-value-parser": "^4.2.0" }, "peerDependencies": { "postcss": "^8.1.0" }, "bin": { "autoprefixer": "bin/autoprefixer" } }, "sha512-NP9APE+tO+LuJGn7/9+cohklunJsXWiaWEfV3si4Gi/XHDwVNgkwr1J3RQYFIvPy76GmJ9/bW8vyoU1LcxwKHA=="],

    "axobject-query": ["axobject-query@4.1.0", "", {}, "sha512-qIj0G9wZbMGNLjLmg1PT6v2mE9AH2zlnADJD/2tC6E00hgmhUOfEB6greHPAfLRSufHqROIUTkw6E+M3lH0PTQ=="],

    "b4a": ["b4a@1.8.0", "", { "peerDependencies": { "react-native-b4a": "*" }, "optionalPeers": ["react-native-b4a"] }, "sha512-qRuSmNSkGQaHwNbM7J78Wwy+ghLEYF1zNrSeMxj4Kgw6y33O3mXcQ6Ie9fRvfU/YnxWkOchPXbaLb73TkIsfdg=="],

    "bail": ["bail@2.0.2", "", {}, "sha512-0xO6mYd7JB2YesxDKplafRpsiOzPt9V02ddPCLbY1xYGPOX24NTyN50qnUxgCPcSoYMhKpAuBTjQoRZCAkUDRw=="],

    "balanced-match": ["balanced-match@4.0.4", "", {}, "sha512-BLrgEcRTwX2o6gGxGOCNyMvGSp35YofuYzw9h1IMTRmKqttAZZVU67bdb9Pr2vUHA8+j3i2tJfjO6C6+4myGTA=="],

    "bare-events": ["bare-events@2.8.2", "", { "peerDependencies": { "bare-abort-controller": "*" }, "optionalPeers": ["bare-abort-controller"] }, "sha512-riJjyv1/mHLIPX4RwiK+oW9/4c3TEUeORHKefKAKnZ5kyslbN+HXowtbaVEqt4IMUB7OXlfixcs6gsFeo/jhiQ=="],

    "bare-fs": ["bare-fs@4.5.5", "", { "dependencies": { "bare-events": "^2.5.4", "bare-path": "^3.0.0", "bare-stream": "^2.6.4", "bare-url": "^2.2.2", "fast-fifo": "^1.3.2" }, "peerDependencies": { "bare-buffer": "*" }, "optionalPeers": ["bare-buffer"] }, "sha512-XvwYM6VZqKoqDll8BmSww5luA5eflDzY0uEFfBJtFKe4PAAtxBjU3YIxzIBzhyaEQBy1VXEQBto4cpN5RZJw+w=="],

    "bare-os": ["bare-os@3.8.0", "", {}, "sha512-Dc9/SlwfxkXIGYhvMQNUtKaXCaGkZYGcd1vuNUUADVqzu4/vQfvnMkYYOUnt2VwQ2AqKr/8qAVFRtwETljgeFg=="],

    "bare-path": ["bare-path@3.0.0", "", { "dependencies": { "bare-os": "^3.0.1" } }, "sha512-tyfW2cQcB5NN8Saijrhqn0Zh7AnFNsnczRcuWODH0eYAXBsJ5gVxAUuNr7tsHSC6IZ77cA0SitzT+s47kot8Mw=="],

    "bare-stream": ["bare-stream@2.8.1", "", { "dependencies": { "streamx": "^2.21.0", "teex": "^1.0.1" }, "peerDependencies": { "bare-buffer": "*", "bare-events": "*" }, "optionalPeers": ["bare-buffer", "bare-events"] }, "sha512-bSeR8RfvbRwDpD7HWZvn8M3uYNDrk7m9DQjYOFkENZlXW8Ju/MPaqUPQq5LqJ3kyjEm07siTaAQ7wBKCU59oHg=="],

    "bare-url": ["bare-url@2.3.2", "", { "dependencies": { "bare-path": "^3.0.0" } }, "sha512-ZMq4gd9ngV5aTMa5p9+UfY0b3skwhHELaDkhEHetMdX0LRkW9kzaym4oo/Eh+Ghm0CCDuMTsRIGM/ytUc1ZYmw=="],

    "base-64": ["base-64@1.0.0", "", {}, "sha512-kwDPIFCGx0NZHog36dj+tHiwP4QMzsZ3AgMViUBKI0+V5n4U0ufTCUMhnQ04diaRI8EX/QcPfql7zlhZ7j4zgg=="],

    "base64-js": ["base64-js@1.5.1", "", {}, "sha512-AKpaYlHn8t4SVbOHCy+b5+KKgvR4vrsD8vbvrbiQJps7fKDTkjkDry6ji0rUJjC0kzbNePLwzxq8iypo41qeWA=="],

    "baseline-browser-mapping": ["baseline-browser-mapping@2.10.8", "", { "bin": { "baseline-browser-mapping": "dist/cli.cjs" } }, "sha512-PCLz/LXGBsNTErbtB6i5u4eLpHeMfi93aUv5duMmj6caNu6IphS4q6UevDnL36sZQv9lrP11dbPKGMaXPwMKfQ=="],

    "bindings": ["bindings@1.5.0", "", { "dependencies": { "file-uri-to-path": "1.0.0" } }, "sha512-p2q/t/mhvuOj/UeLlV6566GD/guowlr0hHxClI0W9m7MWYkL1F0hLo+0Aexs9HSPCtR1SXQ0TD3MMKrXZajbiQ=="],

    "birpc": ["birpc@4.0.0", "", {}, "sha512-LShSxJP0KTmd101b6DRyGBj57LZxSDYWKitQNW/mi8GRMvZb078Uf9+pveax1DrVL89vm7mWe+TovdI/UDOuPw=="],

    "boolbase": ["boolbase@1.0.0", "", {}, "sha512-JZOSA7Mo9sNGB8+UjSgzdLtokWAky1zbztM3WRLCbZ70/3cTANmQmOdR7y2g+J0e2WXywy1yS468tY+IruqEww=="],

    "boxen": ["boxen@8.0.1", "", { "dependencies": { "ansi-align": "^3.0.1", "camelcase": "^8.0.0", "chalk": "^5.3.0", "cli-boxes": "^3.0.0", "string-width": "^7.2.0", "type-fest": "^4.21.0", "widest-line": "^5.0.0", "wrap-ansi": "^9.0.0" } }, "sha512-F3PH5k5juxom4xktynS7MoFY+NUWH5LC4CnH11YB8NPew+HLpmBLCybSAEyb2F+4pRXhuhWqFesoQd6DAyc2hw=="],

    "brace-expansion": ["brace-expansion@5.0.4", "", { "dependencies": { "balanced-match": "^4.0.2" } }, "sha512-h+DEnpVvxmfVefa4jFbCf5HdH5YMDXRsmKflpf1pILZWRFlTbJpxeU55nJl4Smt5HQaGzg1o6RHFPJaOqnmBDg=="],

    "braces": ["braces@3.0.3", "", { "dependencies": { "fill-range": "^7.1.1" } }, "sha512-yQbXgO/OSZVD2IsiLlro+7Hf6Q18EJrKSEsdoMzKePKXct3gvD8oLcOQdIzGupr5Fj+EDe8gO/lxc1BzfMpxvA=="],

    "browserslist": ["browserslist@4.28.1", "", { "dependencies": { "baseline-browser-mapping": "^2.9.0", "caniuse-lite": "^1.0.30001759", "electron-to-chromium": "^1.5.263", "node-releases": "^2.0.27", "update-browserslist-db": "^1.2.0" }, "bin": { "browserslist": "cli.js" } }, "sha512-ZC5Bd0LgJXgwGqUknZY/vkUQ04r8NXnJZ3yYi4vDmSiZmC/pdSN0NbNRPxZpbtO4uAfDUAFffO8IZoM3Gj8IkA=="],

    "buffer": ["buffer@6.0.3", "", { "dependencies": { "base64-js": "^1.3.1", "ieee754": "^1.2.1" } }, "sha512-FTiCpNxtwiZZHEZbcbTIcZjERVICn9yq/pDFkTl95/AxzD1naBctN7YO68riM/gLSDY7sdrMby8hofADYuuqOA=="],

    "buffer-crc32": ["buffer-crc32@1.0.0", "", {}, "sha512-Db1SbgBS/fg/392AblrMJk97KggmvYhr4pB5ZIMTWtaivCPMWLkmb7m21cJvpvgK+J3nsU2CmmixNBZx4vFj/w=="],

    "buffer-from": ["buffer-from@1.1.2", "", {}, "sha512-E+XQCRwSbaaiChtv6k6Dwgc+bx+Bs6vuKJHHl5kox/BaKbhiXzqQOwK4cO22yElGp2OCmjwVhT3HmxgyPGnJfQ=="],

    "bundle-name": ["bundle-name@4.1.0", "", { "dependencies": { "run-applescript": "^7.0.0" } }, "sha512-tjwM5exMg6BGRI+kNmTntNsvdZS1X8BFYS6tnJ2hdH0kVxM6/eVZ2xy+FqStSWvYmtfFMDLIxurorHwDKfDz5Q=="],

    "c12": ["c12@3.3.3", "", { "dependencies": { "chokidar": "^5.0.0", "confbox": "^0.2.2", "defu": "^6.1.4", "dotenv": "^17.2.3", "exsolve": "^1.0.8", "giget": "^2.0.0", "jiti": "^2.6.1", "ohash": "^2.0.11", "pathe": "^2.0.3", "perfect-debounce": "^2.0.0", "pkg-types": "^2.3.0", "rc9": "^2.1.2" }, "peerDependencies": { "magicast": "*" }, "optionalPeers": ["magicast"] }, "sha512-750hTRvgBy5kcMNPdh95Qo+XUBeGo8C7nsKSmedDmaQI+E0r82DwHeM6vBewDe4rGFbnxoa4V9pw+sPh5+Iz8Q=="],

    "cac": ["cac@7.0.0", "", {}, "sha512-tixWYgm5ZoOD+3g6UTea91eow5z6AAHaho3g0V9CNSNb45gM8SmflpAc+GRd1InC4AqN/07Unrgp56Y94N9hJQ=="],

    "camelcase": ["camelcase@8.0.0", "", {}, "sha512-8WB3Jcas3swSvjIeA2yvCJ+Miyz5l1ZmB6HFb9R1317dt9LCQoswg/BGrmAmkWVEszSrrg4RwmO46qIm2OEnSA=="],

    "caniuse-api": ["caniuse-api@3.0.0", "", { "dependencies": { "browserslist": "^4.0.0", "caniuse-lite": "^1.0.0", "lodash.memoize": "^4.1.2", "lodash.uniq": "^4.5.0" } }, "sha512-bsTwuIg/BZZK/vreVTYYbSWoe2F+71P7K5QGEX+pT250DZbfU1MQ5prOKpPR+LL6uWKK3KMwMCAS74QB3Um1uw=="],

    "caniuse-lite": ["caniuse-lite@1.0.30001780", "", {}, "sha512-llngX0E7nQci5BPJDqoZSbuZ5Bcs9F5db7EtgfwBerX9XGtkkiO4NwfDDIRzHTTwcYC8vC7bmeUEPGrKlR/TkQ=="],

    "ccount": ["ccount@2.0.1", "", {}, "sha512-eyrF0jiFpY+3drT6383f1qhkbGsLSifNAjA61IUjZjmLCWjItY6LB9ft9YhoDgwfmclB2zhu51Lc7+95b8NRAg=="],

    "chalk": ["chalk@5.6.2", "", {}, "sha512-7NzBL0rN6fMUW+f7A6Io4h40qQlG+xGmtMxfbnH/K7TAtt8JQWVQK+6g0UXKMeVJoyV5EkkNsErQ8pVD3bLHbA=="],

    "character-entities": ["character-entities@2.0.2", "", {}, "sha512-shx7oQ0Awen/BRIdkjkvz54PnEEI/EjwXDSIZp86/KKdbafHh1Df/RYGBhn4hbe2+uKC9FnT5UCEdyPz3ai9hQ=="],

    "character-entities-html4": ["character-entities-html4@2.1.0", "", {}, "sha512-1v7fgQRj6hnSwFpq1Eu0ynr/CDEw0rXo2B61qXrLNdHZmPKgb7fqS1a2JwF0rISo9q77jDI8VMEHoApn8qDoZA=="],

    "character-entities-legacy": ["character-entities-legacy@3.0.0", "", {}, "sha512-RpPp0asT/6ufRm//AJVwpViZbGM/MkjQFxJccQRHmISF/22NBtsHqAWmL+/pmkPWoIUJdWyeVleTl1wydHATVQ=="],

    "chokidar": ["chokidar@4.0.3", "", { "dependencies": { "readdirp": "^4.0.1" } }, "sha512-Qgzu8kfBvo+cA4962jnP1KkS6Dop5NS6g7R5LFYJr4b8Ub94PPQXUksCw9PvXoeXPRRddRNC5C1JQUR2SMGtnA=="],

    "chownr": ["chownr@3.0.0", "", {}, "sha512-+IxzY9BZOQd/XuYPRmrvEVjF/nqj5kgT4kEq7VofrDoM1MxoRjEWkrCC3EtLi59TVawxTAn+orJwFQcrqEN1+g=="],

    "ci-info": ["ci-info@4.4.0", "", {}, "sha512-77PSwercCZU2Fc4sX94eF8k8Pxte6JAwL4/ICZLFjJLqegs7kCuAsqqj/70NQF6TvDpgFjkubQB2FW2ZZddvQg=="],

    "citty": ["citty@0.2.1", "", {}, "sha512-kEV95lFBhQgtogAPlQfJJ0WGVSokvLr/UEoFPiKKOXF7pl98HfUVUD0ejsuTCld/9xH9vogSywZ5KqHzXrZpqg=="],

    "cli-boxes": ["cli-boxes@3.0.0", "", {}, "sha512-/lzGpEWL/8PfI0BmBOPRwp0c/wFNX1RdUML3jK/RcSBA9T8mZDdQpqYBKtCFTOfQbwPqWEOpjqW+Fnayc0969g=="],

    "clipboardy": ["clipboardy@4.0.0", "", { "dependencies": { "execa": "^8.0.1", "is-wsl": "^3.1.0", "is64bit": "^2.0.0" } }, "sha512-5mOlNS0mhX0707P2I0aZ2V/cmHUEO/fL7VFLqszkhUsxt7RwnmrInf/eEQKlf5GzvYeHIjT+Ov1HRfNmymlG0w=="],

    "cliui": ["cliui@8.0.1", "", { "dependencies": { "string-width": "^4.2.0", "strip-ansi": "^6.0.1", "wrap-ansi": "^7.0.0" } }, "sha512-BSeNnyus75C4//NQ9gQt1/csTXyo/8Sb+afLAkzAptFuMsod9HFokGNudZpi/oQV73hnVK+sR+5PVRMd+Dr7YQ=="],

    "clsx": ["clsx@2.1.1", "", {}, "sha512-eYm0QWBtUrBWZWG0d386OGAw16Z995PiOVo2B7bjWSbHedGl5e0ZWaq65kOGgUSNesEIDkB9ISbTg/JK9dhCZA=="],

    "cluster-key-slot": ["cluster-key-slot@1.1.2", "", {}, "sha512-RMr0FhtfXemyinomL4hrWcYJxmX6deFdCxpJzhDttxgO1+bcCnkk+9drydLVDmAMG7NE6aN/fl4F7ucU/90gAA=="],

    "color-convert": ["color-convert@2.0.1", "", { "dependencies": { "color-name": "~1.1.4" } }, "sha512-RRECPsj7iu/xb5oKYcsFHSppFNnsj/52OVTRKb4zP5onXwVF3zVmmToNcOfGC+CRDpfK/U584fMg38ZHCaElKQ=="],

    "color-name": ["color-name@1.1.4", "", {}, "sha512-dOy+3AuW3a2wNbZHIuMZpTcgjGuLU/uBL/ubcZF9OXbDo8ff4O8yVp5Bf0efS8uEoYo5q4Fx7dY9OgQGXgAsQA=="],

    "colord": ["colord@2.9.3", "", {}, "sha512-jeC1axXpnb0/2nn/Y1LPuLdgXBLH7aDcHu4KEKfqw3CUhX7ZpfBSlPKyqXE6btIgEzfWtrX3/tyBCaCvXvMkOw=="],

    "comma-separated-tokens": ["comma-separated-tokens@2.0.3", "", {}, "sha512-Fu4hJdvzeylCfQPp9SGWidpzrMs7tTrlu6Vb8XGaRGck8QSNZJJp538Wrb60Lax4fPwR64ViY468OIUTbRlGZg=="],

    "commander": ["commander@9.5.0", "", {}, "sha512-KRs7WVDKg86PWiuAqhDrAQnTXZKraVcCc6vFdL14qrZ/DcWwuRo7VoiYXalXO7S5GKpqYiVEwCbgFDfxNHKJBQ=="],

    "common-ancestor-path": ["common-ancestor-path@1.0.1", "", {}, "sha512-L3sHRo1pXXEqX8VU28kfgUY+YGsk09hPqZiZmLacNib6XNTCM8ubYeT7ryXQw8asB1sKgcU5lkB7ONug08aB8w=="],

    "commondir": ["commondir@1.0.1", "", {}, "sha512-W9pAhw0ja1Edb5GVdIF1mjZw/ASI0AlShXM83UUGe2DVr5TdAPEA1OA8m/g8zWp9x6On7gqufY+FatDbC3MDQg=="],

    "compatx": ["compatx@0.2.0", "", {}, "sha512-6gLRNt4ygsi5NyMVhceOCFv14CIdDFN7fQjX1U4+47qVE/+kjPoXMK65KWK+dWxmFzMTuKazoQ9sch6pM0p5oA=="],

    "compress-commons": ["compress-commons@6.0.2", "", { "dependencies": { "crc-32": "^1.2.0", "crc32-stream": "^6.0.0", "is-stream": "^2.0.1", "normalize-path": "^3.0.0", "readable-stream": "^4.0.0" } }, "sha512-6FqVXeETqWPoGcfzrXb37E50NP0LXT8kAMu5ooZayhWWdgEY4lBEEcbQNXtkuKQsGduxiIcI4gOTsxTmuq/bSg=="],

    "confbox": ["confbox@0.2.4", "", {}, "sha512-ysOGlgTFbN2/Y6Cg3Iye8YKulHw+R2fNXHrgSmXISQdMnomY6eNDprVdW9R5xBguEqI954+S6709UyiO7B+6OQ=="],

    "consola": ["consola@3.4.2", "", {}, "sha512-5IKcdX0nnYavi6G7TtOhwkYzyjfJlatbjMjuLSfE2kYT5pMDOilZ4OvMhi637CcDICTmz3wARPoyhqyX1Y+XvA=="],

    "convert-source-map": ["convert-source-map@2.0.0", "", {}, "sha512-Kvp459HrV2FEJ1CAsi1Ku+MY3kasH19TFykTz2xWmMeq6bk2NU3XXvfJ+Q61m0xktWwt+1HSYf3JZsTms3aRJg=="],

    "cookie": ["cookie@1.1.1", "", {}, "sha512-ei8Aos7ja0weRpFzJnEA9UHJ/7XQmqglbRwnf2ATjcB9Wq874VKH9kfjjirM6UhU2/E5fFYadylyhFldcqSidQ=="],

    "cookie-es": ["cookie-es@2.0.0", "", {}, "sha512-RAj4E421UYRgqokKUmotqAwuplYw15qtdXfY+hGzgCJ/MBjCVZcSoHK/kH9kocfjRjcDME7IiDWR/1WX1TM2Pg=="],

    "copy-anything": ["copy-anything@4.0.5", "", { "dependencies": { "is-what": "^5.2.0" } }, "sha512-7Vv6asjS4gMOuILabD3l739tsaxFQmC+a7pLZm02zyvs8p977bL3zEgq3yDk5rn9B0PbYgIv++jmHcuUab4RhA=="],

    "core-util-is": ["core-util-is@1.0.3", "", {}, "sha512-ZQBvi1DcpJ4GDqanjucZ2Hj3wEO5pZDS89BWbkcrvdxksJorwUDDZamX9ldFkp9aw2lmBDLgkObEA4DWNJ9FYQ=="],

    "crc-32": ["crc-32@1.2.2", "", { "bin": { "crc32": "bin/crc32.njs" } }, "sha512-ROmzCKrTnOwybPcJApAA6WBWij23HVfGVNKqqrZpuyZOHqK2CwHSvpGuyt/UNNvaIjEd8X5IFGp4Mh+Ie1IHJQ=="],

    "crc32-stream": ["crc32-stream@6.0.0", "", { "dependencies": { "crc-32": "^1.2.0", "readable-stream": "^4.0.0" } }, "sha512-piICUB6ei4IlTv1+653yq5+KoqfBYmj9bw6LqXoOneTMDXk5nM1qt12mFW1caG3LlJXEKW1Bp0WggEmIfQB34g=="],

    "croner": ["croner@9.1.0", "", {}, "sha512-p9nwwR4qyT5W996vBZhdvBCnMhicY5ytZkR4D1Xj0wuTDEiMnjwR57Q3RXYY/s0EpX6Ay3vgIcfaR+ewGHsi+g=="],

    "cross-spawn": ["cross-spawn@7.0.6", "", { "dependencies": { "path-key": "^3.1.0", "shebang-command": "^2.0.0", "which": "^2.0.1" } }, "sha512-uV2QOWP2nWzsy2aMp8aRibhi9dlzF5Hgh5SHaB9OiTGEyDTiJJyx0uy51QXdyWbtAHNua4XJzUKca3OzKUd3vA=="],

    "crossws": ["crossws@0.3.5", "", { "dependencies": { "uncrypto": "^0.1.3" } }, "sha512-ojKiDvcmByhwa8YYqbQI/hg7MEU0NC03+pSdEq4ZUnZR9xXpwk7E43SMNGkn+JxJGPFtNvQ48+vV2p+P1ml5PA=="],

    "css-declaration-sorter": ["css-declaration-sorter@7.3.1", "", { "peerDependencies": { "postcss": "^8.0.9" } }, "sha512-gz6x+KkgNCjxq3Var03pRYLhyNfwhkKF1g/yoLgDNtFvVu0/fOLV9C8fFEZRjACp/XQLumjAYo7JVjzH3wLbxA=="],

    "css-select": ["css-select@5.2.2", "", { "dependencies": { "boolbase": "^1.0.0", "css-what": "^6.1.0", "domhandler": "^5.0.2", "domutils": "^3.0.1", "nth-check": "^2.0.1" } }, "sha512-TizTzUddG/xYLA3NXodFM0fSbNizXjOKhqiQQwvhlspadZokn1KDy0NZFS0wuEubIYAV5/c1/lAr0TaaFXEXzw=="],

    "css-tree": ["css-tree@3.2.1", "", { "dependencies": { "mdn-data": "2.27.1", "source-map-js": "^1.2.1" } }, "sha512-X7sjQzceUhu1u7Y/ylrRZFU2FS6LRiFVp6rKLPg23y3x3c3DOKAwuXGDp+PAGjh6CSnCjYeAul8pcT8bAl+lSA=="],

    "css-what": ["css-what@6.2.2", "", {}, "sha512-u/O3vwbptzhMs3L1fQE82ZSLHQQfto5gyZzwteVIEyeaY5Fc7R4dapF/BvRoSYFeqfBk4m0V1Vafq5Pjv25wvA=="],

    "cssesc": ["cssesc@3.0.0", "", { "bin": { "cssesc": "bin/cssesc" } }, "sha512-/Tb/JcjK111nNScGob5MNtsntNM1aCNUDipB/TkwZFhyDrrE47SOx/18wF2bbjgc3ZzCSKW1T5nt5EbFoAz/Vg=="],

    "cssnano": ["cssnano@7.1.3", "", { "dependencies": { "cssnano-preset-default": "^7.0.11", "lilconfig": "^3.1.3" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-mLFHQAzyapMVFLiJIn7Ef4C2UCEvtlTlbyILR6B5ZsUAV3D/Pa761R5uC1YPhyBkRd3eqaDm2ncaNrD7R4mTRg=="],

    "cssnano-preset-default": ["cssnano-preset-default@7.0.11", "", { "dependencies": { "browserslist": "^4.28.1", "css-declaration-sorter": "^7.2.0", "cssnano-utils": "^5.0.1", "postcss-calc": "^10.1.1", "postcss-colormin": "^7.0.6", "postcss-convert-values": "^7.0.9", "postcss-discard-comments": "^7.0.6", "postcss-discard-duplicates": "^7.0.2", "postcss-discard-empty": "^7.0.1", "postcss-discard-overridden": "^7.0.1", "postcss-merge-longhand": "^7.0.5", "postcss-merge-rules": "^7.0.8", "postcss-minify-font-values": "^7.0.1", "postcss-minify-gradients": "^7.0.1", "postcss-minify-params": "^7.0.6", "postcss-minify-selectors": "^7.0.6", "postcss-normalize-charset": "^7.0.1", "postcss-normalize-display-values": "^7.0.1", "postcss-normalize-positions": "^7.0.1", "postcss-normalize-repeat-style": "^7.0.1", "postcss-normalize-string": "^7.0.1", "postcss-normalize-timing-functions": "^7.0.1", "postcss-normalize-unicode": "^7.0.6", "postcss-normalize-url": "^7.0.1", "postcss-normalize-whitespace": "^7.0.1", "postcss-ordered-values": "^7.0.2", "postcss-reduce-initial": "^7.0.6", "postcss-reduce-transforms": "^7.0.1", "postcss-svgo": "^7.1.1", "postcss-unique-selectors": "^7.0.5" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-waWlAMuCakP7//UCY+JPrQS1z0OSLeOXk2sKWJximKWGupVxre50bzPlvpbUwZIDylhf/ptf0Pk+Yf7C+hoa3g=="],

    "cssnano-utils": ["cssnano-utils@5.0.1", "", { "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-ZIP71eQgG9JwjVZsTPSqhc6GHgEr53uJ7tK5///VfyWj6Xp2DBmixWHqJgPno+PqATzn48pL42ww9x5SSGmhZg=="],

    "csso": ["csso@5.0.5", "", { "dependencies": { "css-tree": "~2.2.0" } }, "sha512-0LrrStPOdJj+SPCCrGhzryycLjwcgUSHBtxNA8aIDxf0GLsRh1cKYhB00Gd1lDOS4yGH69+SNn13+TWbVHETFQ=="],

    "csstype": ["csstype@3.2.3", "", {}, "sha512-z1HGKcYy2xA8AGQfwrn0PAy+PB7X/GSj3UVJW9qKyn43xWa+gl5nXmU4qqLMRzWVLFC8KusUX8T/0kCiOYpAIQ=="],

    "db0": ["db0@0.3.4", "", { "peerDependencies": { "@electric-sql/pglite": "*", "@libsql/client": "*", "better-sqlite3": "*", "drizzle-orm": "*", "mysql2": "*", "sqlite3": "*" }, "optionalPeers": ["@electric-sql/pglite", "@libsql/client", "better-sqlite3", "drizzle-orm", "mysql2", "sqlite3"] }, "sha512-RiXXi4WaNzPTHEOu8UPQKMooIbqOEyqA1t7Z6MsdxSCeb8iUC9ko3LcmsLmeUt2SM5bctfArZKkRQggKZz7JNw=="],

    "debug": ["debug@4.4.3", "", { "dependencies": { "ms": "^2.1.3" } }, "sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA=="],

    "decode-named-character-reference": ["decode-named-character-reference@1.3.0", "", { "dependencies": { "character-entities": "^2.0.0" } }, "sha512-GtpQYB283KrPp6nRw50q3U9/VfOutZOe103qlN7BPP6Ad27xYnOIWv4lPzo8HCAL+mMZofJ9KEy30fq6MfaK6Q=="],

    "deepmerge": ["deepmerge@4.3.1", "", {}, "sha512-3sUqbMEc77XqpdNO7FRyRog+eW3ph+GYCbj+rK+uYyRMuwsVy0rMiVtPn+QJlKFvWP/1PYpapqYn0Me2knFn+A=="],

    "default-browser": ["default-browser@5.5.0", "", { "dependencies": { "bundle-name": "^4.1.0", "default-browser-id": "^5.0.0" } }, "sha512-H9LMLr5zwIbSxrmvikGuI/5KGhZ8E2zH3stkMgM5LpOWDutGM2JZaj460Udnf1a+946zc7YBgrqEWwbk7zHvGw=="],

    "default-browser-id": ["default-browser-id@5.0.1", "", {}, "sha512-x1VCxdX4t+8wVfd1so/9w+vQ4vx7lKd2Qp5tDRutErwmR85OgmfX7RlLRMWafRMY7hbEiXIbudNrjOAPa/hL8Q=="],

    "define-lazy-prop": ["define-lazy-prop@3.0.0", "", {}, "sha512-N+MeXYoqr3pOgn8xfyRPREN7gHakLYjhsHhWGT3fWAiL4IkAt0iDw14QiiEm2bE30c5XX5q0FtAA3CK5f9/BUg=="],

    "defu": ["defu@6.1.4", "", {}, "sha512-mEQCMmwJu317oSz8CwdIOdwf3xMif1ttiM8LTufzc3g6kR+9Pe236twL8j3IYT1F7GfRgGcW6MWxzZjLIkuHIg=="],

    "denque": ["denque@2.1.0", "", {}, "sha512-HVQE3AAb/pxF8fQAoiqpvg9i3evqug3hoiwakOyZAwJm+6vZehbkYXZ0l4JxS+I3QxM97v5aaRNhj8v5oBhekw=="],

    "depd": ["depd@2.0.0", "", {}, "sha512-g7nH6P6dyDioJogAAGprGpCtVImJhpPk/roCzdb3fIh61/s/nPsfR6onyMwkCAR/OlC3yBC0lESvUoQEAssIrw=="],

    "dequal": ["dequal@2.0.3", "", {}, "sha512-0je+qPKHEMohvfRTCEo3CrPG6cAzAYgmzKyxRiYSSDkS6eGJdyVJm7WaYA5ECaAD9wLB2T4EEeymA5aFVcYXCA=="],

    "destr": ["destr@2.0.5", "", {}, "sha512-ugFTXCtDZunbzasqBxrK93Ik/DRYsO6S/fedkWEMKqt04xZ4csmnmwGDBAb07QWNaGMAmnTIemsYZCksjATwsA=="],

    "detect-libc": ["detect-libc@2.1.2", "", {}, "sha512-Btj2BOOO83o3WyH59e8MgXsxEQVcarkUOpEYrubB0urwnN10yQ364rsiByU11nZlqWYZm05i/of7io4mzihBtQ=="],

    "deterministic-object-hash": ["deterministic-object-hash@2.0.2", "", { "dependencies": { "base-64": "^1.0.0" } }, "sha512-KxektNH63SrbfUyDiwXqRb1rLwKt33AmMv+5Nhsw1kqZ13SJBRTgZHtGbE+hH3a1mVW1cz+4pqSWVPAtLVXTzQ=="],

    "devalue": ["devalue@5.6.4", "", {}, "sha512-Gp6rDldRsFh/7XuouDbxMH3Mx8GMCcgzIb1pDTvNyn8pZGQ22u+Wa+lGV9dQCltFQ7uVw0MhRyb8XDskNFOReA=="],

    "devlop": ["devlop@1.1.0", "", { "dependencies": { "dequal": "^2.0.0" } }, "sha512-RWmIqhcFf1lRYBvNmr7qTNuyCt/7/ns2jbpp1+PalgE/rDQcBT0fioSMUpJ93irlUhC5hrg4cYqe6U+0ImW0rA=="],

    "diff": ["diff@8.0.3", "", {}, "sha512-qejHi7bcSD4hQAZE0tNAawRK1ZtafHDmMTMkrrIGgSLl7hTnQHmKCeB45xAcbfTqK2zowkM3j3bHt/4b/ARbYQ=="],

    "dlv": ["dlv@1.1.3", "", {}, "sha512-+HlytyjlPKnIG8XuRG8WvmBP8xs8P71y+SKKS6ZXWoEgLuePxtDoUEiH7WkdePWrQ5JBpE6aoVqfZfJUQkjXwA=="],

    "dom-serializer": ["dom-serializer@2.0.0", "", { "dependencies": { "domelementtype": "^2.3.0", "domhandler": "^5.0.2", "entities": "^4.2.0" } }, "sha512-wIkAryiqt/nV5EQKqQpo3SToSOV9J0DnbJqwK7Wv/Trc92zIAYZ4FlMu+JPFW1DfGFt81ZTCGgDEabffXeLyJg=="],

    "domelementtype": ["domelementtype@2.3.0", "", {}, "sha512-OLETBj6w0OsagBwdXnPdN0cnMfF9opN69co+7ZrbfPGrdpPVNBUj02spi6B1N7wChLQiPn4CSH/zJvXw56gmHw=="],

    "domhandler": ["domhandler@5.0.3", "", { "dependencies": { "domelementtype": "^2.3.0" } }, "sha512-cgwlv/1iFQiFnU96XXgROh8xTeetsnJiDsTc7TYCLFd9+/WNkIqPTxiM/8pSd8VIrhXGTf1Ny1q1hquVqDJB5w=="],

    "domutils": ["domutils@3.2.2", "", { "dependencies": { "dom-serializer": "^2.0.0", "domelementtype": "^2.3.0", "domhandler": "^5.0.3" } }, "sha512-6kZKyUajlDuqlHKVX1w7gyslj9MPIXzIFiz/rGu35uC1wMi+kMhQwGhl4lt9unC9Vb9INnY9Z3/ZA3+FhASLaw=="],

    "dot-prop": ["dot-prop@10.1.0", "", { "dependencies": { "type-fest": "^5.0.0" } }, "sha512-MVUtAugQMOff5RnBy2d9N31iG0lNwg1qAoAOn7pOK5wf94WIaE3My2p3uwTQuvS2AcqchkcR3bHByjaM0mmi7Q=="],

    "dotenv": ["dotenv@17.3.1", "", {}, "sha512-IO8C/dzEb6O3F9/twg6ZLXz164a2fhTnEWb95H23Dm4OuN+92NmEAlTrupP9VW6Jm3sO26tQlqyvyi4CsnY9GA=="],

    "dset": ["dset@3.1.4", "", {}, "sha512-2QF/g9/zTaPDc3BjNcVTGoBbXBgYfMTTceLaYcFJ/W9kggFUkhxD/hMEeuLKbugyef9SqAx8cpgwlIP/jinUTA=="],

    "dts-resolver": ["dts-resolver@2.1.3", "", { "peerDependencies": { "oxc-resolver": ">=11.0.0" }, "optionalPeers": ["oxc-resolver"] }, "sha512-bihc7jPC90VrosXNzK0LTE2cuLP6jr0Ro8jk+kMugHReJVLIpHz/xadeq3MhuwyO4TD4OA3L1Q8pBBFRc08Tsw=="],

    "duplexer": ["duplexer@0.1.2", "", {}, "sha512-jtD6YG370ZCIi/9GTaJKQxWTZD045+4R4hTk/x1UyoqadyJ9x9CgSi1RlVDQF8U2sxLLSnFkCaMihqljHIWgMg=="],

    "eastasianwidth": ["eastasianwidth@0.2.0", "", {}, "sha512-I88TYZWc9XiYHRQ4/3c5rjjfgkjhLyW2luGIheGERbNQ6OY7yTybanSpDXZa8y7VUP9YmDcYa+eyq4ca7iLqWA=="],

    "ee-first": ["ee-first@1.1.1", "", {}, "sha512-WMwm9LhRUo+WUaRN+vRuETqG89IgZphVSNkdFgeb6sS/E4OrDIN7t48CAewSHXc6C8lefD8KKfr5vY61brQlow=="],

    "electron-to-chromium": ["electron-to-chromium@1.5.321", "", {}, "sha512-L2C7Q279W2D/J4PLZLk7sebOILDSWos7bMsMNN06rK482umHUrh/3lM8G7IlHFOYip2oAg5nha1rCMxr/rs6ZQ=="],

    "emmet": ["emmet@2.4.11", "", { "dependencies": { "@emmetio/abbreviation": "^2.3.3", "@emmetio/css-abbreviation": "^2.1.8" } }, "sha512-23QPJB3moh/U9sT4rQzGgeyyGIrcM+GH5uVYg2C6wZIxAIJq7Ng3QLT79tl8FUwDXhyq9SusfknOrofAKqvgyQ=="],

    "emoji-regex": ["emoji-regex@8.0.0", "", {}, "sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A=="],

    "empathic": ["empathic@2.0.0", "", {}, "sha512-i6UzDscO/XfAcNYD75CfICkmfLedpyPDdozrLMmQc5ORaQcdMoc21OnlEylMIqI7U8eniKrPMxxtj8k0vhmJhA=="],

    "encodeurl": ["encodeurl@2.0.0", "", {}, "sha512-Q0n9HRi4m6JuGIV1eFlmvJB7ZEVxu93IrMyiMsGC0lrMJMWzRgx6WGquyfQgZVb31vhGgXnfmPNNXmxnOkRBrg=="],

    "enhanced-resolve": ["enhanced-resolve@5.20.1", "", { "dependencies": { "graceful-fs": "^4.2.4", "tapable": "^2.3.0" } }, "sha512-Qohcme7V1inbAfvjItgw0EaxVX5q2rdVEZHRBrEQdRZTssLDGsL8Lwrznl8oQ/6kuTJONLaDcGjkNP247XEhcA=="],

    "entities": ["entities@7.0.1", "", {}, "sha512-TWrgLOFUQTH994YUyl1yT4uyavY5nNB5muff+RtWaqNVCAK408b5ZnnbNAUEWLTCpum9w6arT70i1XdQ4UeOPA=="],

    "error-stack-parser-es": ["error-stack-parser-es@1.0.5", "", {}, "sha512-5qucVt2XcuGMcEGgWI7i+yZpmpByQ8J1lHhcL7PwqCwu9FPP3VUXzT4ltHe5i2z9dePwEHcDVOAfSnHsOlCXRA=="],

    "errx": ["errx@0.1.0", "", {}, "sha512-fZmsRiDNv07K6s2KkKFTiD2aIvECa7++PKyD5NC32tpRw46qZA3sOz+aM+/V9V0GDHxVTKLziveV4JhzBHDp9Q=="],

    "es-module-lexer": ["es-module-lexer@1.7.0", "", {}, "sha512-jEQoCwk8hyb2AZziIOLhDqpm5+2ww5uIE6lkO/6jcOCusfk6LhMHpXXfBLXTZ7Ydyt0j4VoUQv6uGNYbdW+kBA=="],

    "esbuild": ["esbuild@0.27.4", "", { "optionalDependencies": { "@esbuild/aix-ppc64": "0.27.4", "@esbuild/android-arm": "0.27.4", "@esbuild/android-arm64": "0.27.4", "@esbuild/android-x64": "0.27.4", "@esbuild/darwin-arm64": "0.27.4", "@esbuild/darwin-x64": "0.27.4", "@esbuild/freebsd-arm64": "0.27.4", "@esbuild/freebsd-x64": "0.27.4", "@esbuild/linux-arm": "0.27.4", "@esbuild/linux-arm64": "0.27.4", "@esbuild/linux-ia32": "0.27.4", "@esbuild/linux-loong64": "0.27.4", "@esbuild/linux-mips64el": "0.27.4", "@esbuild/linux-ppc64": "0.27.4", "@esbuild/linux-riscv64": "0.27.4", "@esbuild/linux-s390x": "0.27.4", "@esbuild/linux-x64": "0.27.4", "@esbuild/netbsd-arm64": "0.27.4", "@esbuild/netbsd-x64": "0.27.4", "@esbuild/openbsd-arm64": "0.27.4", "@esbuild/openbsd-x64": "0.27.4", "@esbuild/openharmony-arm64": "0.27.4", "@esbuild/sunos-x64": "0.27.4", "@esbuild/win32-arm64": "0.27.4", "@esbuild/win32-ia32": "0.27.4", "@esbuild/win32-x64": "0.27.4" }, "bin": { "esbuild": "bin/esbuild" } }, "sha512-Rq4vbHnYkK5fws5NF7MYTU68FPRE1ajX7heQ/8QXXWqNgqqJ/GkmmyxIzUnf2Sr/bakf8l54716CcMGHYhMrrQ=="],

    "escalade": ["escalade@3.2.0", "", {}, "sha512-WUj2qlxaQtO4g6Pq5c29GTcWGDyd8itL8zTlipgECz3JesAiiOKotd8JU6otB3PACgG6xkJUyVhboMS+bje/jA=="],

    "escape-html": ["escape-html@1.0.3", "", {}, "sha512-NiSupZ4OeuGwr68lGIeym/ksIZMJodUGOSCZ/FSnTxcrekbvqrgdUxlJOMpijaKZVjAJrWrGs/6Jy8OMuyj9ow=="],

    "escape-string-regexp": ["escape-string-regexp@5.0.0", "", {}, "sha512-/veY75JbMK4j1yjvuUxuVsiS/hr/4iHs9FTT6cgTexxdE0Ly/glccBAkloH/DofkjRbZU3bnoj38mOmhkZ0lHw=="],

    "estree-walker": ["estree-walker@3.0.3", "", { "dependencies": { "@types/estree": "^1.0.0" } }, "sha512-7RUKfXgSMMkzt6ZuXmqapOurLGPPfgj6l9uRZ7lRGolvk0y2yocc35LdcxKC5PQZdn2DMqioAQ2NoWcrTKmm6g=="],

    "etag": ["etag@1.8.1", "", {}, "sha512-aIL5Fx7mawVa300al2BnEE4iNvo1qETxLrPI/o05L7z6go7fCw1J6EQmbK4FmJ2AS7kgVF/KEZWufBfdClMcPg=="],

    "event-target-shim": ["event-target-shim@5.0.1", "", {}, "sha512-i/2XbnSz/uxRCU6+NdVJgKWDTM427+MqYbkQzD321DuCQJUqOuJKIA0IM2+W2xtYHdKOmZ4dR6fExsd4SXL+WQ=="],

    "eventemitter3": ["eventemitter3@5.0.4", "", {}, "sha512-mlsTRyGaPBjPedk6Bvw+aqbsXDtoAyAzm5MO7JgU+yVRyMQ5O8bD4Kcci7BS85f93veegeCPkL8R4GLClnjLFw=="],

    "events": ["events@3.3.0", "", {}, "sha512-mQw+2fkQbALzQ7V0MY0IqdnXNOeTtP4r0lN9z7AAawCXgqea7bDii20AYrIBrFd/Hx0M2Ocz6S111CaFkUcb0Q=="],

    "events-universal": ["events-universal@1.0.1", "", { "dependencies": { "bare-events": "^2.7.0" } }, "sha512-LUd5euvbMLpwOF8m6ivPCbhQeSiYVNb8Vs0fQ8QjXo0JTkEHpz8pxdQf0gStltaPpw0Cca8b39KxvK9cfKRiAw=="],

    "execa": ["execa@9.6.1", "", { "dependencies": { "@sindresorhus/merge-streams": "^4.0.0", "cross-spawn": "^7.0.6", "figures": "^6.1.0", "get-stream": "^9.0.0", "human-signals": "^8.0.1", "is-plain-obj": "^4.1.0", "is-stream": "^4.0.1", "npm-run-path": "^6.0.0", "pretty-ms": "^9.2.0", "signal-exit": "^4.1.0", "strip-final-newline": "^4.0.0", "yoctocolors": "^2.1.1" } }, "sha512-9Be3ZoN4LmYR90tUoVu2te2BsbzHfhJyfEiAVfz7N5/zv+jduIfLrV2xdQXOHbaD6KgpGdO9PRPM1Y4Q9QkPkA=="],

    "exsolve": ["exsolve@1.0.8", "", {}, "sha512-LmDxfWXwcTArk8fUEnOfSZpHOJ6zOMUJKOtFLFqJLoKJetuQG874Uc7/Kki7zFLzYybmZhp1M7+98pfMqeX8yA=="],

    "extend": ["extend@3.0.2", "", {}, "sha512-fjquC59cD7CyW6urNXK0FBufkZcoiGG80wTuPujX590cB5Ttln20E2UB4S/WARVqhXffZl2LNgS+gQdPIIim/g=="],

    "externality": ["externality@1.0.2", "", { "dependencies": { "enhanced-resolve": "^5.14.1", "mlly": "^1.3.0", "pathe": "^1.1.1", "ufo": "^1.1.2" } }, "sha512-LyExtJWKxtgVzmgtEHyQtLFpw1KFhQphF9nTG8TpAIVkiI/xQ3FJh75tRFLYl4hkn7BNIIdLJInuDAavX35pMw=="],

    "fast-deep-equal": ["fast-deep-equal@3.1.3", "", {}, "sha512-f3qQ9oQy9j2AhBe/H9VC91wLmKBCCU/gDOnKNAYG5hswO7BLKj09Hc5HYNz9cGI++xlpDCIgDaitVs03ATR84Q=="],

    "fast-fifo": ["fast-fifo@1.3.2", "", {}, "sha512-/d9sfos4yxzpwkDkuN7k2SqFKtYNmCTzgfEpz82x34IM9/zc8KGxQoXg1liNC/izpRM/MBdt44Nmx41ZWqk+FQ=="],

    "fast-glob": ["fast-glob@3.3.3", "", { "dependencies": { "@nodelib/fs.stat": "^2.0.2", "@nodelib/fs.walk": "^1.2.3", "glob-parent": "^5.1.2", "merge2": "^1.3.0", "micromatch": "^4.0.8" } }, "sha512-7MptL8U0cqcFdzIzwOTHoilX9x5BrNqye7Z/LuC7kCMRio1EMSyqRK3BEAUD7sXRq4iT4AzTVuZdhgQ2TCvYLg=="],

    "fast-npm-meta": ["fast-npm-meta@1.4.2", "", { "bin": { "fast-npm-meta": "dist/cli.mjs" } }, "sha512-XXyd9d3ie/JeIIjm6WeKalvapGGFI4ShAjPJM78vgUFYzoEsuNSjvvVTuht0XZcwbVdOnEEGzhxwguRbxkIcDg=="],

    "fast-uri": ["fast-uri@3.1.0", "", {}, "sha512-iPeeDKJSWf4IEOasVVrknXpaBV0IApz/gp7S2bb7Z4Lljbl2MGJRqInZiUrQwV16cpzw/D3S5j5Julj/gT52AA=="],

    "fastq": ["fastq@1.20.1", "", { "dependencies": { "reusify": "^1.0.4" } }, "sha512-GGToxJ/w1x32s/D2EKND7kTil4n8OVk/9mycTc4VDza13lOvpUZTGX3mFSCtV9ksdGBVzvsyAVLM6mHFThxXxw=="],

    "fdir": ["fdir@6.5.0", "", { "peerDependencies": { "picomatch": "^3 || ^4" }, "optionalPeers": ["picomatch"] }, "sha512-tIbYtZbucOs0BRGqPJkshJUYdL+SDH7dVM8gjy+ERp3WAUjLEFJE+02kanyHtwjWOnwrKYBiwAmM0p4kLJAnXg=="],

    "figures": ["figures@6.1.0", "", { "dependencies": { "is-unicode-supported": "^2.0.0" } }, "sha512-d+l3qxjSesT4V7v2fh+QnmFnUWv9lSpjarhShNTgBOfA0ttejbQUAlHLitbjkoRiDulW0OPoQPYIGhIC8ohejg=="],

    "file-uri-to-path": ["file-uri-to-path@1.0.0", "", {}, "sha512-0Zt+s3L7Vf1biwWZ29aARiVYLx7iMGnEUl9x33fbB/j3jR81u/O2LbqK+Bm1CDSNDKVtJ/YjwY7TUd5SkeLQLw=="],

    "fill-range": ["fill-range@7.1.1", "", { "dependencies": { "to-regex-range": "^5.0.1" } }, "sha512-YsGpe3WHLK8ZYi4tWDg2Jy3ebRz2rXowDxnld4bkQB00cc/1Zw9AWnC0i9ztDJitivtQvaI9KaLyKrc+hBW0yg=="],

    "flattie": ["flattie@1.1.1", "", {}, "sha512-9UbaD6XdAL97+k/n+N7JwX46K/M6Zc6KcFYskrYL8wbBV/Uyk0CTAMY0VT+qiK5PM7AIc9aTWYtq65U7T+aCNQ=="],

    "fontace": ["fontace@0.4.1", "", { "dependencies": { "fontkitten": "^1.0.2" } }, "sha512-lDMvbAzSnHmbYMTEld5qdtvNH2/pWpICOqpean9IgC7vUbUJc3k+k5Dokp85CegamqQpFbXf0rAVkbzpyTA8aw=="],

    "fontkitten": ["fontkitten@1.0.3", "", { "dependencies": { "tiny-inflate": "^1.0.3" } }, "sha512-Wp1zXWPVUPBmfoa3Cqc9ctaKuzKAV6uLstRqlR56kSjplf5uAce+qeyYym7F+PHbGTk+tCEdkCW6RD7DX/gBZw=="],

    "foreground-child": ["foreground-child@3.3.1", "", { "dependencies": { "cross-spawn": "^7.0.6", "signal-exit": "^4.0.1" } }, "sha512-gIXjKqtFuWEgzFRJA9WCQeSJLZDjgJUOMCMzxtvFq/37KojM1BFGufqsCy0r4qSQmYLsZYMeyRqzIWOMup03sw=="],

    "fraction.js": ["fraction.js@5.3.4", "", {}, "sha512-1X1NTtiJphryn/uLQz3whtY6jK3fTqoE3ohKs0tT+Ujr1W59oopxmoEh7Lu5p6vBaPbgoM0bzveAW4Qi5RyWDQ=="],

    "fresh": ["fresh@2.0.0", "", {}, "sha512-Rx/WycZ60HOaqLKAi6cHRKKI7zxWbJ31MhntmtwMoaTeF7XFH9hhBp8vITaMidfljRQ6eYWCKkaTK+ykVJHP2A=="],

    "fs-extra": ["fs-extra@11.3.4", "", { "dependencies": { "graceful-fs": "^4.2.0", "jsonfile": "^6.0.1", "universalify": "^2.0.0" } }, "sha512-CTXd6rk/M3/ULNQj8FBqBWHYBVYybQ3VPBw0xGKFe3tuH7ytT6ACnvzpIQ3UZtB8yvUKC2cXn1a+x+5EVQLovA=="],

    "fsevents": ["fsevents@2.3.3", "", { "os": "darwin" }, "sha512-5xoDfX+fL7faATnagmWPpbFtwh/R77WmMMqqHGS65C3vvB0YHrgF+B1YmZ3441tMj5n63k0212XNoJwzlhffQw=="],

    "function-bind": ["function-bind@1.1.2", "", {}, "sha512-7XHNxH7qX9xG5mIwxkhumTox/MIRNcOgDrxWsMt2pAr23WHp6MrRlN7FBSFpCpr+oVO0F744iUgR82nJMfG2SA=="],

    "fuse.js": ["fuse.js@7.1.0", "", {}, "sha512-trLf4SzuuUxfusZADLINj+dE8clK1frKdmqiJNb1Es75fmI5oY6X2mxLVUciLLjxqw/xr72Dhy+lER6dGd02FQ=="],

    "fzf": ["fzf@0.5.2", "", {}, "sha512-Tt4kuxLXFKHy8KT40zwsUPUkg1CrsgY25FxA2U/j/0WgEDCk3ddc/zLTCCcbSHX9FcKtLuVaDGtGE/STWC+j3Q=="],

    "gensync": ["gensync@1.0.0-beta.2", "", {}, "sha512-3hN7NaskYvMDLQY55gnW3NQ+mesEAepTqlg+VEbj7zzqEMBVNhzcGYYeqFo/TlYz6eQiFcp1HcsCZO+nGgS8zg=="],

    "get-caller-file": ["get-caller-file@2.0.5", "", {}, "sha512-DyFP3BM/3YHTQOCUL/w0OZHR0lpKeGrxotcHWcqNEdnltqFwXVfhEBQ94eIo34AfQpo0rGki4cyIiftY06h2Fg=="],

    "get-east-asian-width": ["get-east-asian-width@1.5.0", "", {}, "sha512-CQ+bEO+Tva/qlmw24dCejulK5pMzVnUOFOijVogd3KQs07HnRIgp8TGipvCCRT06xeYEbpbgwaCxglFyiuIcmA=="],

    "get-port-please": ["get-port-please@3.2.0", "", {}, "sha512-I9QVvBw5U/hw3RmWpYKRumUeaDgxTPd401x364rLmWBJcOQ753eov1eTgzDqRG9bqFIfDc7gfzcQEWrUri3o1A=="],

    "get-stream": ["get-stream@9.0.1", "", { "dependencies": { "@sec-ant/readable-stream": "^0.4.1", "is-stream": "^4.0.1" } }, "sha512-kVCxPF3vQM/N0B1PmoqVUqgHP+EeVjmZSQn+1oCRPxd2P21P2F19lIgbR3HBosbB1PUhOAoctJnfEn2GbN2eZA=="],

    "get-tsconfig": ["get-tsconfig@4.13.6", "", { "dependencies": { "resolve-pkg-maps": "^1.0.0" } }, "sha512-shZT/QMiSHc/YBLxxOkMtgSid5HFoauqCE3/exfsEcwg1WkeqjG+V40yBbBrsD+jW2HDXcs28xOfcbm2jI8Ddw=="],

    "giget": ["giget@3.1.2", "", { "bin": { "giget": "dist/cli.mjs" } }, "sha512-T2qUpKBHeUTwHcIhydgnJzhL0Hj785ms+JkxaaWQH9SDM/llXeewnOkfJcFShAHjWI+26hOChwUfCoupaXLm8g=="],

    "github-slugger": ["github-slugger@2.0.0", "", {}, "sha512-IaOQ9puYtjrkq7Y0Ygl9KDZnrf/aiUJYUpVf89y8kyaxbRG7Y1SrX/jaumrv81vc61+kiMempujsM3Yw7w5qcw=="],

    "glob": ["glob@13.0.6", "", { "dependencies": { "minimatch": "^10.2.2", "minipass": "^7.1.3", "path-scurry": "^2.0.2" } }, "sha512-Wjlyrolmm8uDpm/ogGyXZXb1Z+Ca2B8NbJwqBVg0axK9GbBeoS7yGV6vjXnYdGm6X53iehEuxxbyiKp8QmN4Vw=="],

    "glob-parent": ["glob-parent@5.1.2", "", { "dependencies": { "is-glob": "^4.0.1" } }, "sha512-AOIgSQCepiJYwP3ARnGx+5VnTu2HBYdzbGP45eLw1vr3zB3vZLeyed1sC9hnbcOc9/SrMyM5RPQrkGz4aS9Zow=="],

    "global-directory": ["global-directory@4.0.1", "", { "dependencies": { "ini": "4.1.1" } }, "sha512-wHTUcDUoZ1H5/0iVqEudYW4/kAlN5cZ3j/bXn0Dpbizl9iaUVeWSHqiOjsgk6OW2bkLclbBjzewBz6weQ1zA2Q=="],

    "globby": ["globby@16.1.1", "", { "dependencies": { "@sindresorhus/merge-streams": "^4.0.0", "fast-glob": "^3.3.3", "ignore": "^7.0.5", "is-path-inside": "^4.0.0", "slash": "^5.1.0", "unicorn-magic": "^0.4.0" } }, "sha512-dW7vl+yiAJSp6aCekaVnVJxurRv7DCOLyXqEG3RYMYUg7AuJ2jCqPkZTA8ooqC2vtnkaMcV5WfFBMuEnTu1OQg=="],

    "graceful-fs": ["graceful-fs@4.2.11", "", {}, "sha512-RbJ5/jmFcNNCcDV5o9eTnBLJ/HszWV0P73bc+Ff4nS/rJj+YaS6IGyiOL0VoBYX+l1Wrl3k63h/KrH+nhJ0XvQ=="],

    "gsap": ["gsap@3.14.2", "", {}, "sha512-P8/mMxVLU7o4+55+1TCnQrPmgjPKnwkzkXOK1asnR9Jg2lna4tEY5qBJjMmAaOBDDZWtlRjBXjLa0w53G/uBLA=="],

    "gzip-size": ["gzip-size@7.0.0", "", { "dependencies": { "duplexer": "^0.1.2" } }, "sha512-O1Ld7Dr+nqPnmGpdhzLmMTQ4vAsD+rHwMm1NLUmoUFFymBOMKxCCrtDxqdBRYXdeEPEi3SyoR4TizJLQrnKBNA=="],

    "h3": ["h3@1.15.8", "", { "dependencies": { "cookie-es": "^1.2.2", "crossws": "^0.3.5", "defu": "^6.1.4", "destr": "^2.0.5", "iron-webcrypto": "^1.2.1", "node-mock-http": "^1.0.4", "radix3": "^1.1.2", "ufo": "^1.6.3", "uncrypto": "^0.1.3" } }, "sha512-iOH6Vl8mGd9nNfu9C0IZ+GuOAfJHcyf3VriQxWaSWIB76Fg4BnFuk4cxBxjmQSSxJS664+pgjP6e7VBnUzFfcg=="],

    "hasown": ["hasown@2.0.2", "", { "dependencies": { "function-bind": "^1.1.2" } }, "sha512-0hJU9SCPvmMzIBdZFqNPXWa6dqh7WdH0cII9y+CyS8rG3nL48Bclra9HmKhVVUHyPWNH5Y7xDwAB7bfgSjkUMQ=="],

    "hast-util-from-html": ["hast-util-from-html@2.0.3", "", { "dependencies": { "@types/hast": "^3.0.0", "devlop": "^1.1.0", "hast-util-from-parse5": "^8.0.0", "parse5": "^7.0.0", "vfile": "^6.0.0", "vfile-message": "^4.0.0" } }, "sha512-CUSRHXyKjzHov8yKsQjGOElXy/3EKpyX56ELnkHH34vDVw1N1XSQ1ZcAvTyAPtGqLTuKP/uxM+aLkSPqF/EtMw=="],

    "hast-util-from-parse5": ["hast-util-from-parse5@8.0.3", "", { "dependencies": { "@types/hast": "^3.0.0", "@types/unist": "^3.0.0", "devlop": "^1.0.0", "hastscript": "^9.0.0", "property-information": "^7.0.0", "vfile": "^6.0.0", "vfile-location": "^5.0.0", "web-namespaces": "^2.0.0" } }, "sha512-3kxEVkEKt0zvcZ3hCRYI8rqrgwtlIOFMWkbclACvjlDw8Li9S2hk/d51OI0nr/gIpdMHNepwgOKqZ/sy0Clpyg=="],

    "hast-util-is-element": ["hast-util-is-element@3.0.0", "", { "dependencies": { "@types/hast": "^3.0.0" } }, "sha512-Val9mnv2IWpLbNPqc/pUem+a7Ipj2aHacCwgNfTiK0vJKl0LF+4Ba4+v1oPHFpf3bLYmreq0/l3Gud9S5OH42g=="],

    "hast-util-parse-selector": ["hast-util-parse-selector@4.0.0", "", { "dependencies": { "@types/hast": "^3.0.0" } }, "sha512-wkQCkSYoOGCRKERFWcxMVMOcYE2K1AaNLU8DXS9arxnLOUEWbOXKXiJUNzEpqZ3JOKpnha3jkFrumEjVliDe7A=="],

    "hast-util-raw": ["hast-util-raw@9.1.0", "", { "dependencies": { "@types/hast": "^3.0.0", "@types/unist": "^3.0.0", "@ungap/structured-clone": "^1.0.0", "hast-util-from-parse5": "^8.0.0", "hast-util-to-parse5": "^8.0.0", "html-void-elements": "^3.0.0", "mdast-util-to-hast": "^13.0.0", "parse5": "^7.0.0", "unist-util-position": "^5.0.0", "unist-util-visit": "^5.0.0", "vfile": "^6.0.0", "web-namespaces": "^2.0.0", "zwitch": "^2.0.0" } }, "sha512-Y8/SBAHkZGoNkpzqqfCldijcuUKh7/su31kEBp67cFY09Wy0mTRgtsLYsiIxMJxlu0f6AA5SUTbDR8K0rxnbUw=="],

    "hast-util-to-html": ["hast-util-to-html@9.0.5", "", { "dependencies": { "@types/hast": "^3.0.0", "@types/unist": "^3.0.0", "ccount": "^2.0.0", "comma-separated-tokens": "^2.0.0", "hast-util-whitespace": "^3.0.0", "html-void-elements": "^3.0.0", "mdast-util-to-hast": "^13.0.0", "property-information": "^7.0.0", "space-separated-tokens": "^2.0.0", "stringify-entities": "^4.0.0", "zwitch": "^2.0.4" } }, "sha512-OguPdidb+fbHQSU4Q4ZiLKnzWo8Wwsf5bZfbvu7//a9oTYoqD/fWpe96NuHkoS9h0ccGOTe0C4NGXdtS0iObOw=="],

    "hast-util-to-parse5": ["hast-util-to-parse5@8.0.1", "", { "dependencies": { "@types/hast": "^3.0.0", "comma-separated-tokens": "^2.0.0", "devlop": "^1.0.0", "property-information": "^7.0.0", "space-separated-tokens": "^2.0.0", "web-namespaces": "^2.0.0", "zwitch": "^2.0.0" } }, "sha512-MlWT6Pjt4CG9lFCjiz4BH7l9wmrMkfkJYCxFwKQic8+RTZgWPuWxwAfjJElsXkex7DJjfSJsQIt931ilUgmwdA=="],

    "hast-util-to-text": ["hast-util-to-text@4.0.2", "", { "dependencies": { "@types/hast": "^3.0.0", "@types/unist": "^3.0.0", "hast-util-is-element": "^3.0.0", "unist-util-find-after": "^5.0.0" } }, "sha512-KK6y/BN8lbaq654j7JgBydev7wuNMcID54lkRav1P0CaE1e47P72AWWPiGKXTJU271ooYzcvTAn/Zt0REnvc7A=="],

    "hast-util-whitespace": ["hast-util-whitespace@3.0.0", "", { "dependencies": { "@types/hast": "^3.0.0" } }, "sha512-88JUN06ipLwsnv+dVn+OIYOvAuvBMy/Qoi6O7mQHxdPXpjy+Cd6xRkWwux7DKO+4sYILtLBRIKgsdpS2gQc7qw=="],

    "hastscript": ["hastscript@9.0.1", "", { "dependencies": { "@types/hast": "^3.0.0", "comma-separated-tokens": "^2.0.0", "hast-util-parse-selector": "^4.0.0", "property-information": "^7.0.0", "space-separated-tokens": "^2.0.0" } }, "sha512-g7df9rMFX/SPi34tyGCyUBREQoKkapwdY/T04Qn9TDWfHhAYt4/I0gMVirzK5wEzeUqIjEB+LXC/ypb7Aqno5w=="],

    "hookable": ["hookable@6.1.0", "", {}, "sha512-ZoKZSJgu8voGK2geJS+6YtYjvIzu9AOM/KZXsBxr83uhLL++e9pEv/dlgwgy3dvHg06kTz6JOh1hk3C8Ceiymw=="],

    "html-escaper": ["html-escaper@3.0.3", "", {}, "sha512-RuMffC89BOWQoY0WKGpIhn5gX3iI54O6nRA0yC124NYVtzjmFWBIiFd8M0x+ZdX0P9R4lADg1mgP8C7PxGOWuQ=="],

    "html-void-elements": ["html-void-elements@3.0.0", "", {}, "sha512-bEqo66MRXsUGxWHV5IP0PUiAWwoEjba4VCzg0LjFJBpchPaTfyfCKTG6bc5F8ucKec3q5y6qOdGyYTSBEvhCrg=="],

    "http-cache-semantics": ["http-cache-semantics@4.2.0", "", {}, "sha512-dTxcvPXqPvXBQpq5dUr6mEMJX4oIEFv6bwom3FDwKRDsuIjjJGANqhBuoAn9c1RQJIdAKav33ED65E2ys+87QQ=="],

    "http-errors": ["http-errors@2.0.1", "", { "dependencies": { "depd": "~2.0.0", "inherits": "~2.0.4", "setprototypeof": "~1.2.0", "statuses": "~2.0.2", "toidentifier": "~1.0.1" } }, "sha512-4FbRdAX+bSdmo4AUFuS0WNiPz8NgFt+r8ThgNWmlrjQjt1Q7ZR9+zTlce2859x4KSXrwIsaeTqDoKQmtP8pLmQ=="],

    "http-shutdown": ["http-shutdown@1.2.2", "", {}, "sha512-S9wWkJ/VSY9/k4qcjG318bqJNruzE4HySUhFYknwmu6LBP97KLLfwNf+n4V1BHurvFNkSKLFnK/RsuUnRTf9Vw=="],

    "https-proxy-agent": ["https-proxy-agent@7.0.6", "", { "dependencies": { "agent-base": "^7.1.2", "debug": "4" } }, "sha512-vK9P5/iUfdl95AI+JVyUuIcVtd4ofvtrOr3HNtM2yxC9bnMbEdp3x01OhQNnjb8IJYi38VlTE3mBXwcfvywuSw=="],

    "httpxy": ["httpxy@0.1.7", "", {}, "sha512-pXNx8gnANKAndgga5ahefxc++tJvNL87CXoRwxn1cJE2ZkWEojF3tNfQIEhZX/vfpt+wzeAzpUI4qkediX1MLQ=="],

    "human-signals": ["human-signals@8.0.1", "", {}, "sha512-eKCa6bwnJhvxj14kZk5NCPc6Hb6BdsU9DZcOnmQKSnO1VKrfV0zCvtttPZUsBvjmNDn8rpcJfpwSYnHBjc95MQ=="],

    "ieee754": ["ieee754@1.2.1", "", {}, "sha512-dcyqhDvX1C46lXZcVqCpK+FtMRQVdIMN6/Df5js2zouUsqG7I6sFxitIC+7KYK29KdXOLHdu9zL4sFnoVQnqaA=="],

    "ignore": ["ignore@7.0.5", "", {}, "sha512-Hs59xBNfUIunMFgWAbGX5cq6893IbWg4KnrjbYwX3tx0ztorVgTDA6B2sxf8ejHJ4wz8BqGUMYlnzNBer5NvGg=="],

    "image-meta": ["image-meta@0.2.2", "", {}, "sha512-3MOLanc3sb3LNGWQl1RlQlNWURE5g32aUphrDyFeCsxBTk08iE3VNe4CwsUZ0Qs1X+EfX0+r29Sxdpza4B+yRA=="],

    "import-meta-resolve": ["import-meta-resolve@4.2.0", "", {}, "sha512-Iqv2fzaTQN28s/FwZAoFq0ZSs/7hMAHJVX+w8PZl3cY19Pxk6jFFalxQoIfW2826i/fDLXv8IiEZRIT0lDuWcg=="],

    "import-without-cache": ["import-without-cache@0.2.5", "", {}, "sha512-B6Lc2s6yApwnD2/pMzFh/d5AVjdsDXjgkeJ766FmFuJELIGHNycKRj+l3A39yZPM4CchqNCB4RITEAYB1KUM6A=="],

    "impound": ["impound@1.1.5", "", { "dependencies": { "@jridgewell/trace-mapping": "^0.3.31", "es-module-lexer": "^2.0.0", "pathe": "^2.0.3", "unplugin": "^3.0.0", "unplugin-utils": "^0.3.1" } }, "sha512-5AUn+QE0UofqNHu5f2Skf6Svukdg4ehOIq8O0EtqIx4jta0CDZYBPqpIHt0zrlUTiFVYlLpeH39DoikXBjPKpA=="],

    "inherits": ["inherits@2.0.4", "", {}, "sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ=="],

    "ini": ["ini@4.1.1", "", {}, "sha512-QQnnxNyfvmHFIsj7gkPcYymR8Jdw/o7mp5ZFihxn6h8Ci6fh3Dx4E1gPjpQEpIuPo9XVNY/ZUwh4BPMjGyL01g=="],

    "ioredis": ["ioredis@5.10.0", "", { "dependencies": { "@ioredis/commands": "1.5.1", "cluster-key-slot": "^1.1.0", "debug": "^4.3.4", "denque": "^2.1.0", "lodash.defaults": "^4.2.0", "lodash.isarguments": "^3.1.0", "redis-errors": "^1.2.0", "redis-parser": "^3.0.0", "standard-as-callback": "^2.1.0" } }, "sha512-HVBe9OFuqs+Z6n64q09PQvP1/R4Bm+30PAyyD4wIEqssh3v9L21QjCVk4kRLucMBcDokJTcLjsGeVRlq/nH6DA=="],

    "iron-webcrypto": ["iron-webcrypto@1.2.1", "", {}, "sha512-feOM6FaSr6rEABp/eDfVseKyTMDt+KGpeB35SkVn9Tyn0CqvVsY3EwI0v5i8nMHyJnzCIQf7nsy3p41TPkJZhg=="],

    "is-core-module": ["is-core-module@2.16.1", "", { "dependencies": { "hasown": "^2.0.2" } }, "sha512-UfoeMA6fIJ8wTYFEUjelnaGI67v6+N7qXJEvQuIGa99l4xsCruSYOVSQ0uPANn4dAzm8lkYPaKLrrijLq7x23w=="],

    "is-docker": ["is-docker@3.0.0", "", { "bin": { "is-docker": "cli.js" } }, "sha512-eljcgEDlEns/7AXFosB5K/2nCM4P7FQPkGc/DWLy5rmFEWvZayGrik1d9/QIY5nJ4f9YsVvBkA6kJpHn9rISdQ=="],

    "is-extglob": ["is-extglob@2.1.1", "", {}, "sha512-SbKbANkN603Vi4jEZv49LeVJMn4yGwsbzZworEoyEiutsN3nJYdbO36zfhGJ6QEDpOZIFkDtnq5JRxmvl3jsoQ=="],

    "is-fullwidth-code-point": ["is-fullwidth-code-point@3.0.0", "", {}, "sha512-zymm5+u+sCsSWyD9qNaejV3DFvhCKclKdizYaJUuHA83RLjb7nSuGnddCHGv0hk+KY7BMAlsWeK4Ueg6EV6XQg=="],

    "is-glob": ["is-glob@4.0.3", "", { "dependencies": { "is-extglob": "^2.1.1" } }, "sha512-xelSayHH36ZgE7ZWhli7pW34hNbNl8Ojv5KVmkJD4hBdD3th8Tfk9vYasLM+mXWOZhFkgZfxhLSnrwRr4elSSg=="],

    "is-inside-container": ["is-inside-container@1.0.0", "", { "dependencies": { "is-docker": "^3.0.0" }, "bin": { "is-inside-container": "cli.js" } }, "sha512-KIYLCCJghfHZxqjYBE7rEy0OBuTd5xCHS7tHVgvCLkx7StIoaxwNW3hCALgEUjFfeRk+MG/Qxmp/vtETEF3tRA=="],

    "is-installed-globally": ["is-installed-globally@1.0.0", "", { "dependencies": { "global-directory": "^4.0.1", "is-path-inside": "^4.0.0" } }, "sha512-K55T22lfpQ63N4KEN57jZUAaAYqYHEe8veb/TycJRk9DdSCLLcovXz/mL6mOnhQaZsQGwPhuFopdQIlqGSEjiQ=="],

    "is-module": ["is-module@1.0.0", "", {}, "sha512-51ypPSPCoTEIN9dy5Oy+h4pShgJmPCygKfyRCISBI+JoWT/2oJvK8QPxmwv7b/p239jXrm9M1mlQbyKJ5A152g=="],

    "is-number": ["is-number@7.0.0", "", {}, "sha512-41Cifkg6e8TylSpdtTpeLVMqvSBEVzTttHvERD741+pnZ8ANv0004MRL43QKPDlK9cGvNp6NZWZUBlbGXYxxng=="],

    "is-path-inside": ["is-path-inside@4.0.0", "", {}, "sha512-lJJV/5dYS+RcL8uQdBDW9c9uWFLLBNRyFhnAKXw5tVqLlKZ4RMGZKv+YQ/IA3OhD+RpbJa1LLFM1FQPGyIXvOA=="],

    "is-plain-obj": ["is-plain-obj@4.1.0", "", {}, "sha512-+Pgi+vMuUNkJyExiMBt5IlFoMyKnr5zhJ4Uspz58WOhBF5QoIZkFyNHIbBAtHwzVAgk5RtndVNsDRN61/mmDqg=="],

    "is-reference": ["is-reference@1.2.1", "", { "dependencies": { "@types/estree": "*" } }, "sha512-U82MsXXiFIrjCK4otLT+o2NA2Cd2g5MLoOVXUZjIOhLurrRxpEXzI8O0KZHr3IjLvlAH1kTPYSuqer5T9ZVBKQ=="],

    "is-stream": ["is-stream@4.0.1", "", {}, "sha512-Dnz92NInDqYckGEUJv689RbRiTSEHCQ7wOVeALbkOz999YpqT46yMRIGtSNl2iCL1waAZSx40+h59NV/EwzV/A=="],

    "is-unicode-supported": ["is-unicode-supported@2.1.0", "", {}, "sha512-mE00Gnza5EEB3Ds0HfMyllZzbBrmLOX3vfWoj9A9PEnTfratQ/BcaJOuMhnkhjXvb2+FkY3VuHqtAGpTPmglFQ=="],

    "is-what": ["is-what@5.5.0", "", {}, "sha512-oG7cgbmg5kLYae2N5IVd3jm2s+vldjxJzK1pcu9LfpGuQ93MQSzo0okvRna+7y5ifrD+20FE8FvjusyGaz14fw=="],

    "is-wsl": ["is-wsl@3.1.1", "", { "dependencies": { "is-inside-container": "^1.0.0" } }, "sha512-e6rvdUCiQCAuumZslxRJWR/Doq4VpPR82kqclvcS0efgt430SlGIk05vdCN58+VrzgtIcfNODjozVielycD4Sw=="],

    "is64bit": ["is64bit@2.0.0", "", { "dependencies": { "system-architecture": "^0.1.0" } }, "sha512-jv+8jaWCl0g2lSBkNSVXdzfBA0npK1HGC2KtWM9FumFRoGS94g3NbCCLVnCYHLjp4GrW2KZeeSTMo5ddtznmGw=="],

    "isarray": ["isarray@1.0.0", "", {}, "sha512-VLghIWNM6ELQzo7zwmcg0NmTVyWKYjvIeM83yjp0wRDTmUnrM678fQbcKBo6n2CJEF0szoG//ytg+TKla89ALQ=="],

    "isexe": ["isexe@4.0.0", "", {}, "sha512-FFUtZMpoZ8RqHS3XeXEmHWLA4thH+ZxCv2lOiPIn1Xc7CxrqhWzNSDzD+/chS/zbYezmiwWLdQC09JdQKmthOw=="],

    "jackspeak": ["jackspeak@3.4.3", "", { "dependencies": { "@isaacs/cliui": "^8.0.2" }, "optionalDependencies": { "@pkgjs/parseargs": "^0.11.0" } }, "sha512-OGlZQpz2yfahA/Rd1Y8Cd9SIEsqvXkLVoSw/cgwhnhFMDbsQFeZYoJJ7bIZBS9BcamUW96asq/npPWugM+RQBw=="],

    "jiti": ["jiti@2.6.1", "", { "bin": { "jiti": "lib/jiti-cli.mjs" } }, "sha512-ekilCSN1jwRvIbgeg/57YFh8qQDNbwDb9xT/qu2DAHbFFZUicIl4ygVaAvzveMhMVr3LnpSKTNnwt8PoOfmKhQ=="],

    "js-tokens": ["js-tokens@9.0.1", "", {}, "sha512-mxa9E9ITFOt0ban3j6L5MpjwegGz6lBQmM1IJkWeBZGcMxto50+eWdjC/52xDbS2vy0k7vIMK0Fe2wfL9OQSpQ=="],

    "js-yaml": ["js-yaml@4.1.1", "", { "dependencies": { "argparse": "^2.0.1" }, "bin": { "js-yaml": "bin/js-yaml.js" } }, "sha512-qQKT4zQxXl8lLwBtHMWwaTcGfFOZviOJet3Oy/xmGk2gZH677CJM9EvtfdSkgWcATZhj/55JZ0rmy3myCT5lsA=="],

    "jsesc": ["jsesc@3.1.0", "", { "bin": { "jsesc": "bin/jsesc" } }, "sha512-/sM3dO2FOzXjKQhJuo0Q173wf2KOo8t4I8vHy6lF9poUp7bKT0/NHE8fPX23PwfhnykfqnC2xRxOnVw5XuGIaA=="],

    "json-schema-traverse": ["json-schema-traverse@1.0.0", "", {}, "sha512-NM8/P9n3XjXhIZn1lLhkFaACTOURQXjWhV4BA/RnOv8xvgqtqpAX9IO4mRQxSx1Rlo4tqzeqb0sOlruaOy3dug=="],

    "json5": ["json5@2.2.3", "", { "bin": { "json5": "lib/cli.js" } }, "sha512-XmOWe7eyHYH14cLdVPoyg+GOH3rYX++KpzrylJwSW98t3Nk+U8XOl8FWKOgwtzdb8lXGf6zYwDUzeHMWfxasyg=="],

    "jsonc-parser": ["jsonc-parser@2.3.1", "", {}, "sha512-H8jvkz1O50L3dMZCsLqiuB2tA7muqbSg1AtGEkN0leAqGjsUzDJir3Zwr02BhqdcITPg3ei3mZ+HjMocAknhhg=="],

    "jsonfile": ["jsonfile@6.2.0", "", { "dependencies": { "universalify": "^2.0.0" }, "optionalDependencies": { "graceful-fs": "^4.1.6" } }, "sha512-FGuPw30AdOIUTRMC2OMRtQV+jkVj2cfPqSeWXv1NEAJ1qZ5zb1X6z1mFhbfOB/iy3ssJCD+3KuZ8r8C3uVFlAg=="],

    "kleur": ["kleur@4.1.5", "", {}, "sha512-o+NO+8WrRiQEE4/7nwRJhN1HWpVmJm511pBHUxPLtp0BUISzlBplORYSmTclCnJvQq2tKu/sgl3xVpkc7ZWuQQ=="],

    "klona": ["klona@2.0.6", "", {}, "sha512-dhG34DXATL5hSxJbIexCft8FChFXtmskoZYnoPWjXQuebWYCNkVeV3KkGegCK9CP1oswI/vQibS2GY7Em/sJJA=="],

    "knitwork": ["knitwork@1.3.0", "", {}, "sha512-4LqMNoONzR43B1W0ek0fhXMsDNW/zxa1NdFAVMY+k28pgZLovR4G3PB5MrpTxCy1QaZCqNoiaKPr5w5qZHfSNw=="],

    "kolorist": ["kolorist@1.8.0", "", {}, "sha512-Y+60/zizpJ3HRH8DCss+q95yr6145JXZo46OTpFvDZWLfRCE4qChOyk1b26nMaNpfHHgxagk9dXT5OP0Tfe+dQ=="],

    "launch-editor": ["launch-editor@2.13.1", "", { "dependencies": { "picocolors": "^1.1.1", "shell-quote": "^1.8.3" } }, "sha512-lPSddlAAluRKJ7/cjRFoXUFzaX7q/YKI7yPHuEvSJVqoXvFnJov1/Ud87Aa4zULIbA9Nja4mSPK8l0z/7eV2wA=="],

    "lazystream": ["lazystream@1.0.1", "", { "dependencies": { "readable-stream": "^2.0.5" } }, "sha512-b94GiNHQNy6JNTrt5w6zNyffMrNkXZb3KTkCZJb2V1xaEGCk093vkZ2jk3tpaeP33/OiXC+WvK9AxUebnf5nbw=="],

    "lenis": ["lenis@1.3.19", "", { "peerDependencies": { "@nuxt/kit": ">=3.0.0", "react": ">=17.0.0", "vue": ">=3.0.0" }, "optionalPeers": ["@nuxt/kit", "react", "vue"] }, "sha512-SFSAWnkGWFyOryfnxc8MtLZiaxDt/vhTJ//7F/nGhrdzDjdqYeCpRk3ZBrqfmdNcjSYuJE4zsIY2x8ypiW01Uw=="],

    "lenis-core": ["lenis-core@workspace:packages/core"],

    "lenis-react": ["lenis-react@workspace:packages/react"],

    "lenis-snap": ["lenis-snap@workspace:packages/snap"],

    "lenis-vue": ["lenis-vue@workspace:packages/vue"],

    "lilconfig": ["lilconfig@3.1.3", "", {}, "sha512-/vlFKAoH5Cgt3Ie+JLhRbwOsCQePABiU3tJ1egGvyQ+33R/vcwM2Zl2QR/LzjsBeItPt3oSVXapn+m4nQDvpzw=="],

    "listhen": ["listhen@1.9.0", "", { "dependencies": { "@parcel/watcher": "^2.4.1", "@parcel/watcher-wasm": "^2.4.1", "citty": "^0.1.6", "clipboardy": "^4.0.0", "consola": "^3.2.3", "crossws": ">=0.2.0 <0.4.0", "defu": "^6.1.4", "get-port-please": "^3.1.2", "h3": "^1.12.0", "http-shutdown": "^1.2.2", "jiti": "^2.1.2", "mlly": "^1.7.1", "node-forge": "^1.3.1", "pathe": "^1.1.2", "std-env": "^3.7.0", "ufo": "^1.5.4", "untun": "^0.1.3", "uqr": "^0.1.2" }, "bin": { "listen": "bin/listhen.mjs", "listhen": "bin/listhen.mjs" } }, "sha512-I8oW2+QL5KJo8zXNWX046M134WchxsXC7SawLPvRQpogCbkyQIaFxPE89A2HiwR7vAK2Dm2ERBAmyjTYGYEpBg=="],

    "local-pkg": ["local-pkg@1.1.2", "", { "dependencies": { "mlly": "^1.7.4", "pkg-types": "^2.3.0", "quansync": "^0.2.11" } }, "sha512-arhlxbFRmoQHl33a0Zkle/YWlmNwoyt6QNZEIJcqNbdrsix5Lvc4HyyI3EnwxTYlZYc32EbYrQ8SzEZ7dqgg9A=="],

    "lodash": ["lodash@4.17.23", "", {}, "sha512-LgVTMpQtIopCi79SJeDiP0TfWi5CNEc/L/aRdTh3yIvmZXTnheWpKjSZhnvMl8iXbC1tFg9gdHHDMLoV7CnG+w=="],

    "lodash.defaults": ["lodash.defaults@4.2.0", "", {}, "sha512-qjxPLHd3r5DnsdGacqOMU6pb/avJzdh9tFX2ymgoZE27BmjXrNy/y4LoaiTeAb+O3gL8AfpJGtqfX/ae2leYYQ=="],

    "lodash.isarguments": ["lodash.isarguments@3.1.0", "", {}, "sha512-chi4NHZlZqZD18a0imDHnZPrDeBbTtVN7GXMwuGdRH9qotxAjYs3aVLKc7zNOG9eddR5Ksd8rvFEBc9SsggPpg=="],

    "lodash.memoize": ["lodash.memoize@4.1.2", "", {}, "sha512-t7j+NzmgnQzTAYXcsHYLgimltOV1MXHtlOWf6GjL9Kj8GK5FInw5JotxvbOs+IvV1/Dzo04/fCGfLVs7aXb4Ag=="],

    "lodash.uniq": ["lodash.uniq@4.5.0", "", {}, "sha512-xfBaXQd9ryd9dlSDvnvI0lvxfLJlYAZzXomUYzLKtUeOQvOP5piqAWuGtrhWeqaXK9hhoM/iyJc5AV+XfsX3HQ=="],

    "longest-streak": ["longest-streak@3.1.0", "", {}, "sha512-9Ri+o0JYgehTaVBBDoMqIl8GXtbWg711O3srftcHhZ0dqnETqLaoIK0x17fUw9rFSlK/0NlsKe0Ahhyl5pXE2g=="],

    "lorem-ipsum": ["lorem-ipsum@2.0.8", "", { "dependencies": { "commander": "^9.3.0" }, "bin": { "lorem-ipsum": "dist/bin/lorem-ipsum.bin.js" } }, "sha512-5RIwHuCb979RASgCJH0VKERn9cQo/+NcAi2BMe9ddj+gp7hujl6BI+qdOG4nVsLDpwWEJwTVYXNKP6BGgbcoGA=="],

    "lru-cache": ["lru-cache@11.2.7", "", {}, "sha512-aY/R+aEsRelme17KGQa/1ZSIpLpNYYrhcrepKTZgE+W3WM16YMCaPwOHLHsmopZHELU0Ojin1lPVxKR0MihncA=="],

    "magic-regexp": ["magic-regexp@0.10.0", "", { "dependencies": { "estree-walker": "^3.0.3", "magic-string": "^0.30.12", "mlly": "^1.7.2", "regexp-tree": "^0.1.27", "type-level-regexp": "~0.1.17", "ufo": "^1.5.4", "unplugin": "^2.0.0" } }, "sha512-Uly1Bu4lO1hwHUW0CQeSWuRtzCMNO00CmXtS8N6fyvB3B979GOEEeAkiTUDsmbYLAbvpUS/Kt5c4ibosAzVyVg=="],

    "magic-string": ["magic-string@0.30.21", "", { "dependencies": { "@jridgewell/sourcemap-codec": "^1.5.5" } }, "sha512-vd2F4YUyEXKGcLHoq+TEyCjxueSeHnFxyyjNp80yg0XV4vUhnDer/lvvlqM/arB5bXQN5K2/3oinyCRyx8T2CQ=="],

    "magic-string-ast": ["magic-string-ast@1.0.3", "", { "dependencies": { "magic-string": "^0.30.19" } }, "sha512-CvkkH1i81zl7mmb94DsRiFeG9V2fR2JeuK8yDgS8oiZSFa++wWLEgZ5ufEOyLHbvSbD1gTRKv9NdX69Rnvr9JA=="],

    "magicast": ["magicast@0.5.2", "", { "dependencies": { "@babel/parser": "^7.29.0", "@babel/types": "^7.29.0", "source-map-js": "^1.2.1" } }, "sha512-E3ZJh4J3S9KfwdjZhe2afj6R9lGIN5Pher1pF39UGrXRqq/VDaGVIGN13BjHd2u8B61hArAGOnso7nBOouW3TQ=="],

    "markdown-table": ["markdown-table@3.0.4", "", {}, "sha512-wiYz4+JrLyb/DqW2hkFJxP7Vd7JuTDm77fvbM8VfEQdmSMqcImWeeRbHwZjBjIFki/VaMK2BhFi7oUUZeM5bqw=="],

    "mdast-util-definitions": ["mdast-util-definitions@6.0.0", "", { "dependencies": { "@types/mdast": "^4.0.0", "@types/unist": "^3.0.0", "unist-util-visit": "^5.0.0" } }, "sha512-scTllyX6pnYNZH/AIp/0ePz6s4cZtARxImwoPJ7kS42n+MnVsI4XbnG6d4ibehRIldYMWM2LD7ImQblVhUejVQ=="],

    "mdast-util-find-and-replace": ["mdast-util-find-and-replace@3.0.2", "", { "dependencies": { "@types/mdast": "^4.0.0", "escape-string-regexp": "^5.0.0", "unist-util-is": "^6.0.0", "unist-util-visit-parents": "^6.0.0" } }, "sha512-Tmd1Vg/m3Xz43afeNxDIhWRtFZgM2VLyaf4vSTYwudTyeuTneoL3qtWMA5jeLyz/O1vDJmmV4QuScFCA2tBPwg=="],

    "mdast-util-from-markdown": ["mdast-util-from-markdown@2.0.3", "", { "dependencies": { "@types/mdast": "^4.0.0", "@types/unist": "^3.0.0", "decode-named-character-reference": "^1.0.0", "devlop": "^1.0.0", "mdast-util-to-string": "^4.0.0", "micromark": "^4.0.0", "micromark-util-decode-numeric-character-reference": "^2.0.0", "micromark-util-decode-string": "^2.0.0", "micromark-util-normalize-identifier": "^2.0.0", "micromark-util-symbol": "^2.0.0", "micromark-util-types": "^2.0.0", "unist-util-stringify-position": "^4.0.0" } }, "sha512-W4mAWTvSlKvf8L6J+VN9yLSqQ9AOAAvHuoDAmPkz4dHf553m5gVj2ejadHJhoJmcmxEnOv6Pa8XJhpxE93kb8Q=="],

    "mdast-util-gfm": ["mdast-util-gfm@3.1.0", "", { "dependencies": { "mdast-util-from-markdown": "^2.0.0", "mdast-util-gfm-autolink-literal": "^2.0.0", "mdast-util-gfm-footnote": "^2.0.0", "mdast-util-gfm-strikethrough": "^2.0.0", "mdast-util-gfm-table": "^2.0.0", "mdast-util-gfm-task-list-item": "^2.0.0", "mdast-util-to-markdown": "^2.0.0" } }, "sha512-0ulfdQOM3ysHhCJ1p06l0b0VKlhU0wuQs3thxZQagjcjPrlFRqY215uZGHHJan9GEAXd9MbfPjFJz+qMkVR6zQ=="],

    "mdast-util-gfm-autolink-literal": ["mdast-util-gfm-autolink-literal@2.0.1", "", { "dependencies": { "@types/mdast": "^4.0.0", "ccount": "^2.0.0", "devlop": "^1.0.0", "mdast-util-find-and-replace": "^3.0.0", "micromark-util-character": "^2.0.0" } }, "sha512-5HVP2MKaP6L+G6YaxPNjuL0BPrq9orG3TsrZ9YXbA3vDw/ACI4MEsnoDpn6ZNm7GnZgtAcONJyPhOP8tNJQavQ=="],

    "mdast-util-gfm-footnote": ["mdast-util-gfm-footnote@2.1.0", "", { "dependencies": { "@types/mdast": "^4.0.0", "devlop": "^1.1.0", "mdast-util-from-markdown": "^2.0.0", "mdast-util-to-markdown": "^2.0.0", "micromark-util-normalize-identifier": "^2.0.0" } }, "sha512-sqpDWlsHn7Ac9GNZQMeUzPQSMzR6Wv0WKRNvQRg0KqHh02fpTz69Qc1QSseNX29bhz1ROIyNyxExfawVKTm1GQ=="],

    "mdast-util-gfm-strikethrough": ["mdast-util-gfm-strikethrough@2.0.0", "", { "dependencies": { "@types/mdast": "^4.0.0", "mdast-util-from-markdown": "^2.0.0", "mdast-util-to-markdown": "^2.0.0" } }, "sha512-mKKb915TF+OC5ptj5bJ7WFRPdYtuHv0yTRxK2tJvi+BDqbkiG7h7u/9SI89nRAYcmap2xHQL9D+QG/6wSrTtXg=="],

    "mdast-util-gfm-table": ["mdast-util-gfm-table@2.0.0", "", { "dependencies": { "@types/mdast": "^4.0.0", "devlop": "^1.0.0", "markdown-table": "^3.0.0", "mdast-util-from-markdown": "^2.0.0", "mdast-util-to-markdown": "^2.0.0" } }, "sha512-78UEvebzz/rJIxLvE7ZtDd/vIQ0RHv+3Mh5DR96p7cS7HsBhYIICDBCu8csTNWNO6tBWfqXPWekRuj2FNOGOZg=="],

    "mdast-util-gfm-task-list-item": ["mdast-util-gfm-task-list-item@2.0.0", "", { "dependencies": { "@types/mdast": "^4.0.0", "devlop": "^1.0.0", "mdast-util-from-markdown": "^2.0.0", "mdast-util-to-markdown": "^2.0.0" } }, "sha512-IrtvNvjxC1o06taBAVJznEnkiHxLFTzgonUdy8hzFVeDun0uTjxxrRGVaNFqkU1wJR3RBPEfsxmU6jDWPofrTQ=="],

    "mdast-util-phrasing": ["mdast-util-phrasing@4.1.0", "", { "dependencies": { "@types/mdast": "^4.0.0", "unist-util-is": "^6.0.0" } }, "sha512-TqICwyvJJpBwvGAMZjj4J2n0X8QWp21b9l0o7eXyVJ25YNWYbJDVIyD1bZXE6WtV6RmKJVYmQAKWa0zWOABz2w=="],

    "mdast-util-to-hast": ["mdast-util-to-hast@13.2.1", "", { "dependencies": { "@types/hast": "^3.0.0", "@types/mdast": "^4.0.0", "@ungap/structured-clone": "^1.0.0", "devlop": "^1.0.0", "micromark-util-sanitize-uri": "^2.0.0", "trim-lines": "^3.0.0", "unist-util-position": "^5.0.0", "unist-util-visit": "^5.0.0", "vfile": "^6.0.0" } }, "sha512-cctsq2wp5vTsLIcaymblUriiTcZd0CwWtCbLvrOzYCDZoWyMNV8sZ7krj09FSnsiJi3WVsHLM4k6Dq/yaPyCXA=="],

    "mdast-util-to-markdown": ["mdast-util-to-markdown@2.1.2", "", { "dependencies": { "@types/mdast": "^4.0.0", "@types/unist": "^3.0.0", "longest-streak": "^3.0.0", "mdast-util-phrasing": "^4.0.0", "mdast-util-to-string": "^4.0.0", "micromark-util-classify-character": "^2.0.0", "micromark-util-decode-string": "^2.0.0", "unist-util-visit": "^5.0.0", "zwitch": "^2.0.0" } }, "sha512-xj68wMTvGXVOKonmog6LwyJKrYXZPvlwabaryTjLh9LuvovB/KAH+kvi8Gjj+7rJjsFi23nkUxRQv1KqSroMqA=="],

    "mdast-util-to-string": ["mdast-util-to-string@4.0.0", "", { "dependencies": { "@types/mdast": "^4.0.0" } }, "sha512-0H44vDimn51F0YwvxSJSm0eCDOJTRlmN0R1yBh4HLj9wiV1Dn0QoXGbvFAWj2hSItVTlCmBF1hqKlIyUBVFLPg=="],

    "mdn-data": ["mdn-data@2.27.1", "", {}, "sha512-9Yubnt3e8A0OKwxYSXyhLymGW4sCufcLG6VdiDdUGVkPhpqLxlvP5vl1983gQjJl3tqbrM731mjaZaP68AgosQ=="],

    "merge-stream": ["merge-stream@2.0.0", "", {}, "sha512-abv/qOcuPfk3URPfDzmZU1LKmuw8kT+0nIHvKrKgFrwifol/doWcdA4ZqsWQ8ENrFKkd67Mfpo/LovbIUsbt3w=="],

    "merge2": ["merge2@1.4.1", "", {}, "sha512-8q7VEgMJW4J8tcfVPy8g09NcQwZdbwFEqhe/WZkoIzjn/3TGDwtOCYtXGxA3O8tPzpczCCDgv+P2P5y00ZJOOg=="],

    "micromark": ["micromark@4.0.2", "", { "dependencies": { "@types/debug": "^4.0.0", "debug": "^4.0.0", "decode-named-character-reference": "^1.0.0", "devlop": "^1.0.0", "micromark-core-commonmark": "^2.0.0", "micromark-factory-space": "^2.0.0", "micromark-util-character": "^2.0.0", "micromark-util-chunked": "^2.0.0", "micromark-util-combine-extensions": "^2.0.0", "micromark-util-decode-numeric-character-reference": "^2.0.0", "micromark-util-encode": "^2.0.0", "micromark-util-normalize-identifier": "^2.0.0", "micromark-util-resolve-all": "^2.0.0", "micromark-util-sanitize-uri": "^2.0.0", "micromark-util-subtokenize": "^2.0.0", "micromark-util-symbol": "^2.0.0", "micromark-util-types": "^2.0.0" } }, "sha512-zpe98Q6kvavpCr1NPVSCMebCKfD7CA2NqZ+rykeNhONIJBpc1tFKt9hucLGwha3jNTNI8lHpctWJWoimVF4PfA=="],

    "micromark-core-commonmark": ["micromark-core-commonmark@2.0.3", "", { "dependencies": { "decode-named-character-reference": "^1.0.0", "devlop": "^1.0.0", "micromark-factory-destination": "^2.0.0", "micromark-factory-label": "^2.0.0", "micromark-factory-space": "^2.0.0", "micromark-factory-title": "^2.0.0", "micromark-factory-whitespace": "^2.0.0", "micromark-util-character": "^2.0.0", "micromark-util-chunked": "^2.0.0", "micromark-util-classify-character": "^2.0.0", "micromark-util-html-tag-name": "^2.0.0", "micromark-util-normalize-identifier": "^2.0.0", "micromark-util-resolve-all": "^2.0.0", "micromark-util-subtokenize": "^2.0.0", "micromark-util-symbol": "^2.0.0", "micromark-util-types": "^2.0.0" } }, "sha512-RDBrHEMSxVFLg6xvnXmb1Ayr2WzLAWjeSATAoxwKYJV94TeNavgoIdA0a9ytzDSVzBy2YKFK+emCPOEibLeCrg=="],

    "micromark-extension-gfm": ["micromark-extension-gfm@3.0.0", "", { "dependencies": { "micromark-extension-gfm-autolink-literal": "^2.0.0", "micromark-extension-gfm-footnote": "^2.0.0", "micromark-extension-gfm-strikethrough": "^2.0.0", "micromark-extension-gfm-table": "^2.0.0", "micromark-extension-gfm-tagfilter": "^2.0.0", "micromark-extension-gfm-task-list-item": "^2.0.0", "micromark-util-combine-extensions": "^2.0.0", "micromark-util-types": "^2.0.0" } }, "sha512-vsKArQsicm7t0z2GugkCKtZehqUm31oeGBV/KVSorWSy8ZlNAv7ytjFhvaryUiCUJYqs+NoE6AFhpQvBTM6Q4w=="],

    "micromark-extension-gfm-autolink-literal": ["micromark-extension-gfm-autolink-literal@2.1.0", "", { "dependencies": { "micromark-util-character": "^2.0.0", "micromark-util-sanitize-uri": "^2.0.0", "micromark-util-symbol": "^2.0.0", "micromark-util-types": "^2.0.0" } }, "sha512-oOg7knzhicgQ3t4QCjCWgTmfNhvQbDDnJeVu9v81r7NltNCVmhPy1fJRX27pISafdjL+SVc4d3l48Gb6pbRypw=="],

    "micromark-extension-gfm-footnote": ["micromark-extension-gfm-footnote@2.1.0", "", { "dependencies": { "devlop": "^1.0.0", "micromark-core-commonmark": "^2.0.0", "micromark-factory-space": "^2.0.0", "micromark-util-character": "^2.0.0", "micromark-util-normalize-identifier": "^2.0.0", "micromark-util-sanitize-uri": "^2.0.0", "micromark-util-symbol": "^2.0.0", "micromark-util-types": "^2.0.0" } }, "sha512-/yPhxI1ntnDNsiHtzLKYnE3vf9JZ6cAisqVDauhp4CEHxlb4uoOTxOCJ+9s51bIB8U1N1FJ1RXOKTIlD5B/gqw=="],

    "micromark-extension-gfm-strikethrough": ["micromark-extension-gfm-strikethrough@2.1.0", "", { "dependencies": { "devlop": "^1.0.0", "micromark-util-chunked": "^2.0.0", "micromark-util-classify-character": "^2.0.0", "micromark-util-resolve-all": "^2.0.0", "micromark-util-symbol": "^2.0.0", "micromark-util-types": "^2.0.0" } }, "sha512-ADVjpOOkjz1hhkZLlBiYA9cR2Anf8F4HqZUO6e5eDcPQd0Txw5fxLzzxnEkSkfnD0wziSGiv7sYhk/ktvbf1uw=="],

    "micromark-extension-gfm-table": ["micromark-extension-gfm-table@2.1.1", "", { "dependencies": { "devlop": "^1.0.0", "micromark-factory-space": "^2.0.0", "micromark-util-character": "^2.0.0", "micromark-util-symbol": "^2.0.0", "micromark-util-types": "^2.0.0" } }, "sha512-t2OU/dXXioARrC6yWfJ4hqB7rct14e8f7m0cbI5hUmDyyIlwv5vEtooptH8INkbLzOatzKuVbQmAYcbWoyz6Dg=="],

    "micromark-extension-gfm-tagfilter": ["micromark-extension-gfm-tagfilter@2.0.0", "", { "dependencies": { "micromark-util-types": "^2.0.0" } }, "sha512-xHlTOmuCSotIA8TW1mDIM6X2O1SiX5P9IuDtqGonFhEK0qgRI4yeC6vMxEV2dgyr2TiD+2PQ10o+cOhdVAcwfg=="],

    "micromark-extension-gfm-task-list-item": ["micromark-extension-gfm-task-list-item@2.1.0", "", { "dependencies": { "devlop": "^1.0.0", "micromark-factory-space": "^2.0.0", "micromark-util-character": "^2.0.0", "micromark-util-symbol": "^2.0.0", "micromark-util-types": "^2.0.0" } }, "sha512-qIBZhqxqI6fjLDYFTBIa4eivDMnP+OZqsNwmQ3xNLE4Cxwc+zfQEfbs6tzAo2Hjq+bh6q5F+Z8/cksrLFYWQQw=="],

    "micromark-factory-destination": ["micromark-factory-destination@2.0.1", "", { "dependencies": { "micromark-util-character": "^2.0.0", "micromark-util-symbol": "^2.0.0", "micromark-util-types": "^2.0.0" } }, "sha512-Xe6rDdJlkmbFRExpTOmRj9N3MaWmbAgdpSrBQvCFqhezUn4AHqJHbaEnfbVYYiexVSs//tqOdY/DxhjdCiJnIA=="],

    "micromark-factory-label": ["micromark-factory-label@2.0.1", "", { "dependencies": { "devlop": "^1.0.0", "micromark-util-character": "^2.0.0", "micromark-util-symbol": "^2.0.0", "micromark-util-types": "^2.0.0" } }, "sha512-VFMekyQExqIW7xIChcXn4ok29YE3rnuyveW3wZQWWqF4Nv9Wk5rgJ99KzPvHjkmPXF93FXIbBp6YdW3t71/7Vg=="],

    "micromark-factory-space": ["micromark-factory-space@2.0.1", "", { "dependencies": { "micromark-util-character": "^2.0.0", "micromark-util-types": "^2.0.0" } }, "sha512-zRkxjtBxxLd2Sc0d+fbnEunsTj46SWXgXciZmHq0kDYGnck/ZSGj9/wULTV95uoeYiK5hRXP2mJ98Uo4cq/LQg=="],

    "micromark-factory-title": ["micromark-factory-title@2.0.1", "", { "dependencies": { "micromark-factory-space": "^2.0.0", "micromark-util-character": "^2.0.0", "micromark-util-symbol": "^2.0.0", "micromark-util-types": "^2.0.0" } }, "sha512-5bZ+3CjhAd9eChYTHsjy6TGxpOFSKgKKJPJxr293jTbfry2KDoWkhBb6TcPVB4NmzaPhMs1Frm9AZH7OD4Cjzw=="],

    "micromark-factory-whitespace": ["micromark-factory-whitespace@2.0.1", "", { "dependencies": { "micromark-factory-space": "^2.0.0", "micromark-util-character": "^2.0.0", "micromark-util-symbol": "^2.0.0", "micromark-util-types": "^2.0.0" } }, "sha512-Ob0nuZ3PKt/n0hORHyvoD9uZhr+Za8sFoP+OnMcnWK5lngSzALgQYKMr9RJVOWLqQYuyn6ulqGWSXdwf6F80lQ=="],

    "micromark-util-character": ["micromark-util-character@2.1.1", "", { "dependencies": { "micromark-util-symbol": "^2.0.0", "micromark-util-types": "^2.0.0" } }, "sha512-wv8tdUTJ3thSFFFJKtpYKOYiGP2+v96Hvk4Tu8KpCAsTMs6yi+nVmGh1syvSCsaxz45J6Jbw+9DD6g97+NV67Q=="],

    "micromark-util-chunked": ["micromark-util-chunked@2.0.1", "", { "dependencies": { "micromark-util-symbol": "^2.0.0" } }, "sha512-QUNFEOPELfmvv+4xiNg2sRYeS/P84pTW0TCgP5zc9FpXetHY0ab7SxKyAQCNCc1eK0459uoLI1y5oO5Vc1dbhA=="],

    "micromark-util-classify-character": ["micromark-util-classify-character@2.0.1", "", { "dependencies": { "micromark-util-character": "^2.0.0", "micromark-util-symbol": "^2.0.0", "micromark-util-types": "^2.0.0" } }, "sha512-K0kHzM6afW/MbeWYWLjoHQv1sgg2Q9EccHEDzSkxiP/EaagNzCm7T/WMKZ3rjMbvIpvBiZgwR3dKMygtA4mG1Q=="],

    "micromark-util-combine-extensions": ["micromark-util-combine-extensions@2.0.1", "", { "dependencies": { "micromark-util-chunked": "^2.0.0", "micromark-util-types": "^2.0.0" } }, "sha512-OnAnH8Ujmy59JcyZw8JSbK9cGpdVY44NKgSM7E9Eh7DiLS2E9RNQf0dONaGDzEG9yjEl5hcqeIsj4hfRkLH/Bg=="],

    "micromark-util-decode-numeric-character-reference": ["micromark-util-decode-numeric-character-reference@2.0.2", "", { "dependencies": { "micromark-util-symbol": "^2.0.0" } }, "sha512-ccUbYk6CwVdkmCQMyr64dXz42EfHGkPQlBj5p7YVGzq8I7CtjXZJrubAYezf7Rp+bjPseiROqe7G6foFd+lEuw=="],

    "micromark-util-decode-string": ["micromark-util-decode-string@2.0.1", "", { "dependencies": { "decode-named-character-reference": "^1.0.0", "micromark-util-character": "^2.0.0", "micromark-util-decode-numeric-character-reference": "^2.0.0", "micromark-util-symbol": "^2.0.0" } }, "sha512-nDV/77Fj6eH1ynwscYTOsbK7rR//Uj0bZXBwJZRfaLEJ1iGBR6kIfNmlNqaqJf649EP0F3NWNdeJi03elllNUQ=="],

    "micromark-util-encode": ["micromark-util-encode@2.0.1", "", {}, "sha512-c3cVx2y4KqUnwopcO9b/SCdo2O67LwJJ/UyqGfbigahfegL9myoEFoDYZgkT7f36T0bLrM9hZTAaAyH+PCAXjw=="],

    "micromark-util-html-tag-name": ["micromark-util-html-tag-name@2.0.1", "", {}, "sha512-2cNEiYDhCWKI+Gs9T0Tiysk136SnR13hhO8yW6BGNyhOC4qYFnwF1nKfD3HFAIXA5c45RrIG1ub11GiXeYd1xA=="],

    "micromark-util-normalize-identifier": ["micromark-util-normalize-identifier@2.0.1", "", { "dependencies": { "micromark-util-symbol": "^2.0.0" } }, "sha512-sxPqmo70LyARJs0w2UclACPUUEqltCkJ6PhKdMIDuJ3gSf/Q+/GIe3WKl0Ijb/GyH9lOpUkRAO2wp0GVkLvS9Q=="],

    "micromark-util-resolve-all": ["micromark-util-resolve-all@2.0.1", "", { "dependencies": { "micromark-util-types": "^2.0.0" } }, "sha512-VdQyxFWFT2/FGJgwQnJYbe1jjQoNTS4RjglmSjTUlpUMa95Htx9NHeYW4rGDJzbjvCsl9eLjMQwGeElsqmzcHg=="],

    "micromark-util-sanitize-uri": ["micromark-util-sanitize-uri@2.0.1", "", { "dependencies": { "micromark-util-character": "^2.0.0", "micromark-util-encode": "^2.0.0", "micromark-util-symbol": "^2.0.0" } }, "sha512-9N9IomZ/YuGGZZmQec1MbgxtlgougxTodVwDzzEouPKo3qFWvymFHWcnDi2vzV1ff6kas9ucW+o3yzJK9YB1AQ=="],

    "micromark-util-subtokenize": ["micromark-util-subtokenize@2.1.0", "", { "dependencies": { "devlop": "^1.0.0", "micromark-util-chunked": "^2.0.0", "micromark-util-symbol": "^2.0.0", "micromark-util-types": "^2.0.0" } }, "sha512-XQLu552iSctvnEcgXw6+Sx75GflAPNED1qx7eBJ+wydBb2KCbRZe+NwvIEEMM83uml1+2WSXpBAcp9IUCgCYWA=="],

    "micromark-util-symbol": ["micromark-util-symbol@2.0.1", "", {}, "sha512-vs5t8Apaud9N28kgCrRUdEed4UJ+wWNvicHLPxCa9ENlYuAY31M0ETy5y1vA33YoNPDFTghEbnh6efaE8h4x0Q=="],

    "micromark-util-types": ["micromark-util-types@2.0.2", "", {}, "sha512-Yw0ECSpJoViF1qTU4DC6NwtC4aWGt1EkzaQB8KPPyCRR8z9TWeV0HbEFGTO+ZY1wB22zmxnJqhPyTpOVCpeHTA=="],

    "micromatch": ["micromatch@4.0.8", "", { "dependencies": { "braces": "^3.0.3", "picomatch": "^2.3.1" } }, "sha512-PXwfBhYu0hBCPw8Dn0E+WDYb7af3dSLVWKi3HGv84IdF4TyFoC0ysxFd0Goxw7nSv4T/PzEJQxsYsEiFCKo2BA=="],

    "mime": ["mime@4.1.0", "", { "bin": { "mime": "bin/cli.js" } }, "sha512-X5ju04+cAzsojXKes0B/S4tcYtFAJ6tTMuSPBEn9CPGlrWr8Fiw7qYeLT0XyH80HSoAoqWCaz+MWKh22P7G1cw=="],

    "mime-db": ["mime-db@1.54.0", "", {}, "sha512-aU5EJuIN2WDemCcAp2vFBfp/m4EAhWJnUNSSw0ixs7/kXbd6Pg64EmwJkNdFhB8aWt1sH2CTXrLxo/iAGV3oPQ=="],

    "mime-types": ["mime-types@3.0.2", "", { "dependencies": { "mime-db": "^1.54.0" } }, "sha512-Lbgzdk0h4juoQ9fCKXW4by0UJqj+nOOrI9MJ1sSj4nI8aI2eo1qmvQEie4VD1glsS250n15LsWsYtCugiStS5A=="],

    "mimic-fn": ["mimic-fn@4.0.0", "", {}, "sha512-vqiC06CuhBTUdZH+RYl8sFrL096vA45Ok5ISO6sE/Mr1jRbGH4Csnhi8f3wKVl7x8mO4Au7Ir9D3Oyv1VYMFJw=="],

    "minimatch": ["minimatch@10.2.4", "", { "dependencies": { "brace-expansion": "^5.0.2" } }, "sha512-oRjTw/97aTBN0RHbYCdtF1MQfvusSIBQM0IZEgzl6426+8jSC0nF1a/GmnVLpfB9yyr6g6FTqWqiZVbxrtaCIg=="],

    "minipass": ["minipass@7.1.3", "", {}, "sha512-tEBHqDnIoM/1rXME1zgka9g6Q2lcoCkxHLuc7ODJ5BxbP5d4c2Z5cGgtXAku59200Cx7diuHTOYfSBD8n6mm8A=="],

    "minizlib": ["minizlib@3.1.0", "", { "dependencies": { "minipass": "^7.1.2" } }, "sha512-KZxYo1BUkWD2TVFLr0MQoM8vUUigWD3LlD83a/75BqC+4qE0Hb1Vo5v1FgcfaNXvfXzr+5EhQ6ing/CaBijTlw=="],

    "mitt": ["mitt@3.0.1", "", {}, "sha512-vKivATfr97l2/QBCYAkXYDbrIWPM2IIKEl7YPhjCvKlG3kE2gm+uBo6nEXK3M5/Ffh/FLpKExzOQ3JJoJGFKBw=="],

    "mlly": ["mlly@1.8.1", "", { "dependencies": { "acorn": "^8.16.0", "pathe": "^2.0.3", "pkg-types": "^1.3.1", "ufo": "^1.6.3" } }, "sha512-SnL6sNutTwRWWR/vcmCYHSADjiEesp5TGQQ0pXyLhW5IoeibRlF/CbSLailbB3CNqJUk9cVJ9dUDnbD7GrcHBQ=="],

    "mocked-exports": ["mocked-exports@0.1.1", "", {}, "sha512-aF7yRQr/Q0O2/4pIXm6PZ5G+jAd7QS4Yu8m+WEeEHGnbo+7mE36CbLSDQiXYV8bVL3NfmdeqPJct0tUlnjVSnA=="],

    "mrmime": ["mrmime@2.0.1", "", {}, "sha512-Y3wQdFg2Va6etvQ5I82yUhGdsKrcYox6p7FfL1LbK2J4V01F9TGlepTIhnK24t7koZibmg82KGglhA1XK5IsLQ=="],

    "ms": ["ms@2.1.3", "", {}, "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA=="],

    "muggle-string": ["muggle-string@0.4.1", "", {}, "sha512-VNTrAak/KhO2i8dqqnqnAHOa3cYBwXEZe9h+D5h/1ZqFSTEFHdM65lR7RoIqq3tBBYavsOXV84NoHXZ0AkPyqQ=="],

    "nanoid": ["nanoid@3.3.11", "", { "bin": { "nanoid": "bin/nanoid.cjs" } }, "sha512-N8SpfPUnUp1bK+PMYW8qSWdl9U+wwNWI4QKxOYDy9JAro3WMX7p2OeVRF9v+347pnakNevPmiHhNmZ2HbFA76w=="],

    "nanotar": ["nanotar@0.3.0", "", {}, "sha512-Kv2JYYiCzt16Kt5QwAc9BFG89xfPNBx+oQL4GQXD9nLqPkZBiNaqaCWtwnbk/q7UVsTYevvM1b0UF8zmEI4pCg=="],

    "neotraverse": ["neotraverse@0.6.18", "", {}, "sha512-Z4SmBUweYa09+o6pG+eASabEpP6QkQ70yHj351pQoEXIs8uHbaU2DWVmzBANKgflPa47A50PtB2+NgRpQvr7vA=="],

    "nitropack": ["nitropack@2.13.1", "", { "dependencies": { "@cloudflare/kv-asset-handler": "^0.4.2", "@rollup/plugin-alias": "^6.0.0", "@rollup/plugin-commonjs": "^29.0.0", "@rollup/plugin-inject": "^5.0.5", "@rollup/plugin-json": "^6.1.0", "@rollup/plugin-node-resolve": "^16.0.3", "@rollup/plugin-replace": "^6.0.3", "@rollup/plugin-terser": "^0.4.4", "@vercel/nft": "^1.2.0", "archiver": "^7.0.1", "c12": "^3.3.3", "chokidar": "^5.0.0", "citty": "^0.1.6", "compatx": "^0.2.0", "confbox": "^0.2.2", "consola": "^3.4.2", "cookie-es": "^2.0.0", "croner": "^9.1.0", "crossws": "^0.3.5", "db0": "^0.3.4", "defu": "^6.1.4", "destr": "^2.0.5", "dot-prop": "^10.1.0", "esbuild": "^0.27.2", "escape-string-regexp": "^5.0.0", "etag": "^1.8.1", "exsolve": "^1.0.8", "globby": "^16.1.0", "gzip-size": "^7.0.0", "h3": "^1.15.5", "hookable": "^5.5.3", "httpxy": "^0.1.7", "ioredis": "^5.9.1", "jiti": "^2.6.1", "klona": "^2.0.6", "knitwork": "^1.3.0", "listhen": "^1.9.0", "magic-string": "^0.30.21", "magicast": "^0.5.1", "mime": "^4.1.0", "mlly": "^1.8.0", "node-fetch-native": "^1.6.7", "node-mock-http": "^1.0.4", "ofetch": "^1.5.1", "ohash": "^2.0.11", "pathe": "^2.0.3", "perfect-debounce": "^2.0.0", "pkg-types": "^2.3.0", "pretty-bytes": "^7.1.0", "radix3": "^1.1.2", "rollup": "^4.55.1", "rollup-plugin-visualizer": "^6.0.5", "scule": "^1.3.0", "semver": "^7.7.3", "serve-placeholder": "^2.0.2", "serve-static": "^2.2.1", "source-map": "^0.7.6", "std-env": "^3.10.0", "ufo": "^1.6.3", "ultrahtml": "^1.6.0", "uncrypto": "^0.1.3", "unctx": "^2.5.0", "unenv": "^2.0.0-rc.24", "unimport": "^5.6.0", "unplugin-utils": "^0.3.1", "unstorage": "^1.17.4", "untyped": "^2.0.0", "unwasm": "^0.5.3", "youch": "^4.1.0-beta.13", "youch-core": "^0.3.3" }, "peerDependencies": { "xml2js": "^0.6.2" }, "optionalPeers": ["xml2js"], "bin": { "nitro": "dist/cli/index.mjs", "nitropack": "dist/cli/index.mjs" } }, "sha512-2dDj89C4wC2uzG7guF3CnyG+zwkZosPEp7FFBGHB3AJo11AywOolWhyQJFHDzve8COvGxJaqscye9wW2IrUsNw=="],

    "nlcst-to-string": ["nlcst-to-string@4.0.0", "", { "dependencies": { "@types/nlcst": "^2.0.0" } }, "sha512-YKLBCcUYKAg0FNlOBT6aI91qFmSiFKiluk655WzPF+DDMA02qIyy8uiRqI8QXtcFpEvll12LpL5MXqEmAZ+dcA=="],

    "node-addon-api": ["node-addon-api@7.1.1", "", {}, "sha512-5m3bsyrjFWE1xf7nz7YXdN4udnVtXK6/Yfgn5qnahL6bCkf2yKt4k3nuTKAtT4r3IG8JNR2ncsIMdZuAzJjHQQ=="],

    "node-fetch": ["node-fetch@2.7.0", "", { "dependencies": { "whatwg-url": "^5.0.0" }, "peerDependencies": { "encoding": "^0.1.0" }, "optionalPeers": ["encoding"] }, "sha512-c4FRfUm/dbcWZ7U+1Wq0AwCyFL+3nt2bEw05wfxSz+DWpWsitgmSgYmy2dQdWyKC1694ELPqMs/YzUSNozLt8A=="],

    "node-fetch-native": ["node-fetch-native@1.6.7", "", {}, "sha512-g9yhqoedzIUm0nTnTqAQvueMPVOuIY16bqgAJJC8XOOubYFNwz6IER9qs0Gq2Xd0+CecCKFjtdDTMA4u4xG06Q=="],

    "node-forge": ["node-forge@1.3.3", "", {}, "sha512-rLvcdSyRCyouf6jcOIPe/BgwG/d7hKjzMKOas33/pHEr6gbq18IK9zV7DiPvzsz0oBJPme6qr6H6kGZuI9/DZg=="],

    "node-gyp-build": ["node-gyp-build@4.8.4", "", { "bin": { "node-gyp-build": "bin.js", "node-gyp-build-optional": "optional.js", "node-gyp-build-test": "build-test.js" } }, "sha512-LA4ZjwlnUblHVgq0oBF3Jl/6h/Nvs5fzBLwdEF4nuxnFdsfajde4WfxtJr3CaiH+F6ewcIB/q4jQ4UzPyid+CQ=="],

    "node-mock-http": ["node-mock-http@1.0.4", "", {}, "sha512-8DY+kFsDkNXy1sJglUfuODx1/opAGJGyrTuFqEoN90oRc2Vk0ZbD4K2qmKXBBEhZQzdKHIVfEJpDU8Ak2NJEvQ=="],

    "node-releases": ["node-releases@2.0.36", "", {}, "sha512-TdC8FSgHz8Mwtw9g5L4gR/Sh9XhSP/0DEkQxfEFXOpiul5IiHgHan2VhYYb6agDSfp4KuvltmGApc8HMgUrIkA=="],

    "nopt": ["nopt@8.1.0", "", { "dependencies": { "abbrev": "^3.0.0" }, "bin": { "nopt": "bin/nopt.js" } }, "sha512-ieGu42u/Qsa4TFktmaKEwM6MQH0pOWnaB3htzh0JRtx84+Mebc0cbZYN5bC+6WTZ4+77xrL9Pn5m7CV6VIkV7A=="],

    "normalize-path": ["normalize-path@3.0.0", "", {}, "sha512-6eZs5Ls3WtCisHWp9S2GUy8dqkpGi4BVSz3GaqiE6ezub0512ESztXUwUB6C6IKbQkY2Pnb/mD4WYojCRwcwLA=="],

    "npm-run-path": ["npm-run-path@6.0.0", "", { "dependencies": { "path-key": "^4.0.0", "unicorn-magic": "^0.3.0" } }, "sha512-9qny7Z9DsQU8Ou39ERsPU4OZQlSTP47ShQzuKZ6PRXpYLtIFgl/DEBYEXKlvcEa+9tHVcK8CF81Y2V72qaZhWA=="],

    "nth-check": ["nth-check@2.1.1", "", { "dependencies": { "boolbase": "^1.0.0" } }, "sha512-lqjrjmaOoAnWfMmBPL+XNnynZh2+swxiX3WUE0s4yEHI6m+AwrK2UZOimIRl3X/4QctVqS8AiZjFqyOGrMXb/w=="],

    "nuxt": ["nuxt@3.21.2", "", { "dependencies": { "@dxup/nuxt": "^0.4.0", "@nuxt/cli": "^3.34.0", "@nuxt/devtools": "^3.2.3", "@nuxt/kit": "3.21.2", "@nuxt/nitro-server": "3.21.2", "@nuxt/schema": "3.21.2", "@nuxt/telemetry": "^2.7.0", "@nuxt/vite-builder": "3.21.2", "@unhead/vue": "^2.1.12", "@vue/shared": "^3.5.30", "c12": "^3.3.3", "chokidar": "^5.0.0", "compatx": "^0.2.0", "consola": "^3.4.2", "cookie-es": "^2.0.0", "defu": "^6.1.4", "destr": "^2.0.5", "devalue": "^5.6.3", "errx": "^0.1.0", "escape-string-regexp": "^5.0.0", "exsolve": "^1.0.8", "h3": "^1.15.6", "hookable": "^5.5.3", "ignore": "^7.0.5", "impound": "^1.1.5", "jiti": "^2.6.1", "klona": "^2.0.6", "knitwork": "^1.3.0", "magic-string": "^0.30.21", "mlly": "^1.8.1", "nanotar": "^0.3.0", "nypm": "^0.6.5", "ofetch": "^1.5.1", "ohash": "^2.0.11", "on-change": "^6.0.2", "oxc-minify": "^0.117.0", "oxc-parser": "^0.117.0", "oxc-transform": "^0.117.0", "oxc-walker": "^0.7.0", "pathe": "^2.0.3", "perfect-debounce": "^2.1.0", "pkg-types": "^2.3.0", "rou3": "^0.8.1", "scule": "^1.3.0", "semver": "^7.7.4", "std-env": "^4.0.0", "tinyglobby": "^0.2.15", "ufo": "^1.6.3", "ultrahtml": "^1.6.0", "uncrypto": "^0.1.3", "unctx": "^2.5.0", "unimport": "^6.0.1", "unplugin": "^3.0.0", "unplugin-vue-router": "^0.19.2", "untyped": "^2.0.0", "vue": "^3.5.30", "vue-router": "^4.6.4" }, "peerDependencies": { "@parcel/watcher": "^2.1.0", "@types/node": "^18.0.0 || ^20.0.0 || >=22.0.0" }, "optionalPeers": ["@parcel/watcher", "@types/node"], "bin": { "nuxi": "bin/nuxt.mjs", "nuxt": "bin/nuxt.mjs" } }, "sha512-XzZFj2KMK16zE0TfrGpjvgc378wZWvDzIpunHOHOT0Jj8zbV5qT1uQKaJb+fAHv6lf1A4nOMMWHrTmjAK4u0Zg=="],

    "nypm": ["nypm@0.6.5", "", { "dependencies": { "citty": "^0.2.0", "pathe": "^2.0.3", "tinyexec": "^1.0.2" }, "bin": { "nypm": "dist/cli.mjs" } }, "sha512-K6AJy1GMVyfyMXRVB88700BJqNUkByijGJM8kEHpLdcAt+vSQAVfkWWHYzuRXHSY6xA2sNc5RjTj0p9rE2izVQ=="],

    "obug": ["obug@2.1.1", "", {}, "sha512-uTqF9MuPraAQ+IsnPf366RG4cP9RtUi7MLO1N3KEc+wb0a6yKpeL0lmk2IB1jY5KHPAlTc6T/JRdC/YqxHNwkQ=="],

    "ofetch": ["ofetch@1.5.1", "", { "dependencies": { "destr": "^2.0.5", "node-fetch-native": "^1.6.7", "ufo": "^1.6.1" } }, "sha512-2W4oUZlVaqAPAil6FUg/difl6YhqhUR7x2eZY4bQCko22UXg3hptq9KLQdqFClV+Wu85UX7hNtdGTngi/1BxcA=="],

    "ohash": ["ohash@2.0.11", "", {}, "sha512-RdR9FQrFwNBNXAr4GixM8YaRZRJ5PUWbKYbE5eOsrwAjJW0q2REGcf79oYPsLyskQCZG1PLN+S/K1V00joZAoQ=="],

    "on-change": ["on-change@6.0.2", "", {}, "sha512-08+12qcOVEA0fS9g/VxKS27HaT94nRutUT77J2dr8zv/unzXopvhBuF8tNLWsoLQ5IgrQ6eptGeGqUYat82U1w=="],

    "on-finished": ["on-finished@2.4.1", "", { "dependencies": { "ee-first": "1.1.1" } }, "sha512-oVlzkg3ENAhCk2zdv7IJwd/QUD4z2RxRwpkcGY8psCVcCYZNq4wYnVWALHM+brtuJjePWiYF/ClmuDr8Ch5+kg=="],

    "onetime": ["onetime@6.0.0", "", { "dependencies": { "mimic-fn": "^4.0.0" } }, "sha512-1FlR+gjXK7X+AsAHso35MnyN5KqGwJRi/31ft6x0M194ht7S+rWAvd7PHss9xSKMzE0asv1pyIHaJYq+BbacAQ=="],

    "oniguruma-parser": ["oniguruma-parser@0.12.1", "", {}, "sha512-8Unqkvk1RYc6yq2WBYRj4hdnsAxVze8i7iPfQr8e4uSP3tRv0rpZcbGUDvxfQQcdwHt/e9PrMvGCsa8OqG9X3w=="],

    "oniguruma-to-es": ["oniguruma-to-es@4.3.5", "", { "dependencies": { "oniguruma-parser": "^0.12.1", "regex": "^6.1.0", "regex-recursion": "^6.0.2" } }, "sha512-Zjygswjpsewa0NLTsiizVuMQZbp0MDyM6lIt66OxsF21npUDlzpHi1Mgb/qhQdkb+dWFTzJmFbEWdvZgRho8eQ=="],

    "open": ["open@10.2.0", "", { "dependencies": { "default-browser": "^5.2.1", "define-lazy-prop": "^3.0.0", "is-inside-container": "^1.0.0", "wsl-utils": "^0.1.0" } }, "sha512-YgBpdJHPyQ2UE5x+hlSXcnejzAvD0b22U2OuAP+8OnlJT+PjWPxtgmGqKKc+RgTM63U9gN0YzrYc71R2WT/hTA=="],

    "oxc-minify": ["oxc-minify@0.117.0", "", { "optionalDependencies": { "@oxc-minify/binding-android-arm-eabi": "0.117.0", "@oxc-minify/binding-android-arm64": "0.117.0", "@oxc-minify/binding-darwin-arm64": "0.117.0", "@oxc-minify/binding-darwin-x64": "0.117.0", "@oxc-minify/binding-freebsd-x64": "0.117.0", "@oxc-minify/binding-linux-arm-gnueabihf": "0.117.0", "@oxc-minify/binding-linux-arm-musleabihf": "0.117.0", "@oxc-minify/binding-linux-arm64-gnu": "0.117.0", "@oxc-minify/binding-linux-arm64-musl": "0.117.0", "@oxc-minify/binding-linux-ppc64-gnu": "0.117.0", "@oxc-minify/binding-linux-riscv64-gnu": "0.117.0", "@oxc-minify/binding-linux-riscv64-musl": "0.117.0", "@oxc-minify/binding-linux-s390x-gnu": "0.117.0", "@oxc-minify/binding-linux-x64-gnu": "0.117.0", "@oxc-minify/binding-linux-x64-musl": "0.117.0", "@oxc-minify/binding-openharmony-arm64": "0.117.0", "@oxc-minify/binding-wasm32-wasi": "0.117.0", "@oxc-minify/binding-win32-arm64-msvc": "0.117.0", "@oxc-minify/binding-win32-ia32-msvc": "0.117.0", "@oxc-minify/binding-win32-x64-msvc": "0.117.0" } }, "sha512-JHsv/b+bmBJkAzkHXgTN7RThloVxLHPT0ojHfjqxVeHuQB7LPpLUbJ2qfwz37sto9stZ9+AVwUP4b3gtR7p/Tw=="],

    "oxc-parser": ["oxc-parser@0.117.0", "", { "dependencies": { "@oxc-project/types": "^0.117.0" }, "optionalDependencies": { "@oxc-parser/binding-android-arm-eabi": "0.117.0", "@oxc-parser/binding-android-arm64": "0.117.0", "@oxc-parser/binding-darwin-arm64": "0.117.0", "@oxc-parser/binding-darwin-x64": "0.117.0", "@oxc-parser/binding-freebsd-x64": "0.117.0", "@oxc-parser/binding-linux-arm-gnueabihf": "0.117.0", "@oxc-parser/binding-linux-arm-musleabihf": "0.117.0", "@oxc-parser/binding-linux-arm64-gnu": "0.117.0", "@oxc-parser/binding-linux-arm64-musl": "0.117.0", "@oxc-parser/binding-linux-ppc64-gnu": "0.117.0", "@oxc-parser/binding-linux-riscv64-gnu": "0.117.0", "@oxc-parser/binding-linux-riscv64-musl": "0.117.0", "@oxc-parser/binding-linux-s390x-gnu": "0.117.0", "@oxc-parser/binding-linux-x64-gnu": "0.117.0", "@oxc-parser/binding-linux-x64-musl": "0.117.0", "@oxc-parser/binding-openharmony-arm64": "0.117.0", "@oxc-parser/binding-wasm32-wasi": "0.117.0", "@oxc-parser/binding-win32-arm64-msvc": "0.117.0", "@oxc-parser/binding-win32-ia32-msvc": "0.117.0", "@oxc-parser/binding-win32-x64-msvc": "0.117.0" } }, "sha512-l3cbgK5wUvWDVNWM/JFU77qDdGZK1wudnLsFcrRyNo/bL1CyU8pC25vDhMHikVY29lbK2InTWsX42RxVSutUdQ=="],

    "oxc-transform": ["oxc-transform@0.117.0", "", { "optionalDependencies": { "@oxc-transform/binding-android-arm-eabi": "0.117.0", "@oxc-transform/binding-android-arm64": "0.117.0", "@oxc-transform/binding-darwin-arm64": "0.117.0", "@oxc-transform/binding-darwin-x64": "0.117.0", "@oxc-transform/binding-freebsd-x64": "0.117.0", "@oxc-transform/binding-linux-arm-gnueabihf": "0.117.0", "@oxc-transform/binding-linux-arm-musleabihf": "0.117.0", "@oxc-transform/binding-linux-arm64-gnu": "0.117.0", "@oxc-transform/binding-linux-arm64-musl": "0.117.0", "@oxc-transform/binding-linux-ppc64-gnu": "0.117.0", "@oxc-transform/binding-linux-riscv64-gnu": "0.117.0", "@oxc-transform/binding-linux-riscv64-musl": "0.117.0", "@oxc-transform/binding-linux-s390x-gnu": "0.117.0", "@oxc-transform/binding-linux-x64-gnu": "0.117.0", "@oxc-transform/binding-linux-x64-musl": "0.117.0", "@oxc-transform/binding-openharmony-arm64": "0.117.0", "@oxc-transform/binding-wasm32-wasi": "0.117.0", "@oxc-transform/binding-win32-arm64-msvc": "0.117.0", "@oxc-transform/binding-win32-ia32-msvc": "0.117.0", "@oxc-transform/binding-win32-x64-msvc": "0.117.0" } }, "sha512-u1Stl2uhDh9bFuOGjGXQIqx46IRUNMyHQkq59LayXNGS2flNv7RpZpRSWs5S5deuNP6jJZ12gtMBze+m4dOhmw=="],

    "oxc-walker": ["oxc-walker@0.7.0", "", { "dependencies": { "magic-regexp": "^0.10.0" }, "peerDependencies": { "oxc-parser": ">=0.98.0" } }, "sha512-54B4KUhrzbzc4sKvKwVYm7E2PgeROpGba0/2nlNZMqfDyca+yOor5IMb4WLGBatGDT0nkzYdYuzylg7n3YfB7A=="],

    "p-limit": ["p-limit@6.2.0", "", { "dependencies": { "yocto-queue": "^1.1.1" } }, "sha512-kuUqqHNUqoIWp/c467RI4X6mmyuojY5jGutNU0wVTmEOOfcuwLqyMVoAi9MKi2Ak+5i9+nhmrK4ufZE8069kHA=="],

    "p-queue": ["p-queue@8.1.1", "", { "dependencies": { "eventemitter3": "^5.0.1", "p-timeout": "^6.1.2" } }, "sha512-aNZ+VfjobsWryoiPnEApGGmf5WmNsCo9xu8dfaYamG5qaLP7ClhLN6NgsFe6SwJ2UbLEBK5dv9x8Mn5+RVhMWQ=="],

    "p-timeout": ["p-timeout@6.1.4", "", {}, "sha512-MyIV3ZA/PmyBN/ud8vV9XzwTrNtR4jFrObymZYnZqMmW0zA8Z17vnT0rBgFE/TlohB+YCHqXMgZzb3Csp49vqg=="],

    "package-json-from-dist": ["package-json-from-dist@1.0.1", "", {}, "sha512-UEZIS3/by4OC8vL3P2dTXRETpebLI2NiI5vIrjaD/5UtrkFX/tNbwjTSRAGC/+7CAo2pIcBaRgWmcBBHcsaCIw=="],

    "package-manager-detector": ["package-manager-detector@1.6.0", "", {}, "sha512-61A5ThoTiDG/C8s8UMZwSorAGwMJ0ERVGj2OjoW5pAalsNOg15+iQiPzrLJ4jhZ1HJzmC2PIHT2oEiH3R5fzNA=="],

    "parse-latin": ["parse-latin@7.0.0", "", { "dependencies": { "@types/nlcst": "^2.0.0", "@types/unist": "^3.0.0", "nlcst-to-string": "^4.0.0", "unist-util-modify-children": "^4.0.0", "unist-util-visit-children": "^3.0.0", "vfile": "^6.0.0" } }, "sha512-mhHgobPPua5kZ98EF4HWiH167JWBfl4pvAIXXdbaVohtK7a6YBOy56kvhCqduqyo/f3yrHFWmqmiMg/BkBkYYQ=="],

    "parse-ms": ["parse-ms@4.0.0", "", {}, "sha512-TXfryirbmq34y8QBwgqCVLi+8oA3oWx2eAnSn62ITyEhEYaWRlVZ2DvMM9eZbMs/RfxPu/PK/aBLyGj4IrqMHw=="],

    "parse5": ["parse5@7.3.0", "", { "dependencies": { "entities": "^6.0.0" } }, "sha512-IInvU7fabl34qmi9gY8XOVxhYyMyuH2xUNpb2q8/Y+7552KlejkRvqvD19nMoUW/uQGGbqNpA6Tufu5FL5BZgw=="],

    "parseurl": ["parseurl@1.3.3", "", {}, "sha512-CiyeOxFT/JZyN5m0z9PfXw4SCBJ6Sygz1Dpl0wqjlhDEGGBP1GnsUVEL0p63hoG1fcj3fHynXi9NYO4nWOL+qQ=="],

    "path-browserify": ["path-browserify@1.0.1", "", {}, "sha512-b7uo2UCUOYZcnF/3ID0lulOJi/bafxa1xPe7ZPsammBSpjSWQkjNxlt635YGS2MiR9GjvuXCtz2emr3jbsz98g=="],

    "path-key": ["path-key@3.1.1", "", {}, "sha512-ojmeN0qd+y0jszEtoY48r0Peq5dwMEkIlCOu6Q5f41lfkswXuKtYrhgoTpLnyIcHm24Uhqx+5Tqm2InSwLhE6Q=="],

    "path-parse": ["path-parse@1.0.7", "", {}, "sha512-LDJzPVEEEPR+y48z93A0Ed0yXb8pAByGWo/k5YYdYgpY2/2EsOsksJrq7lOHxryrVOn1ejG6oAp8ahvOIQD8sw=="],

    "path-scurry": ["path-scurry@2.0.2", "", { "dependencies": { "lru-cache": "^11.0.0", "minipass": "^7.1.2" } }, "sha512-3O/iVVsJAPsOnpwWIeD+d6z/7PmqApyQePUtCndjatj/9I5LylHvt5qluFaBT3I5h3r1ejfR056c+FCv+NnNXg=="],

    "pathe": ["pathe@2.0.3", "", {}, "sha512-WUjGcAqP1gQacoQe+OBJsFA7Ld4DyXuUIjZ5cc75cLHvJ7dtNsTugphxIADwspS+AraAUePCKrSVtPLFj/F88w=="],

    "perfect-debounce": ["perfect-debounce@2.1.0", "", {}, "sha512-LjgdTytVFXeUgtHZr9WYViYSM/g8MkcTPYDlPa3cDqMirHjKiSZPYd6DoL7pK8AJQr+uWkQvCjHNdiMqsrJs+g=="],

    "piccolore": ["piccolore@0.1.3", "", {}, "sha512-o8bTeDWjE086iwKrROaDf31K0qC/BENdm15/uH9usSC/uZjJOKb2YGiVHfLY4GhwsERiPI1jmwI2XrA7ACOxVw=="],

    "picocolors": ["picocolors@1.1.1", "", {}, "sha512-xceH2snhtb5M9liqDsmEw56le376mTZkEX/jEb/RxNFyegNul7eNslCXP9FDj/Lcu0X8KEyMceP2ntpaHrDEVA=="],

    "picomatch": ["picomatch@4.0.3", "", {}, "sha512-5gTmgEY/sqK6gFXLIsQNH19lWb4ebPDLA4SdLP7dsWkIXHWlG66oPuVvXSGFPppYZz8ZDZq0dYYrbHfBCVUb1Q=="],

    "pkg-types": ["pkg-types@2.3.0", "", { "dependencies": { "confbox": "^0.2.2", "exsolve": "^1.0.7", "pathe": "^2.0.3" } }, "sha512-SIqCzDRg0s9npO5XQ3tNZioRY1uK06lA41ynBC1YmFTmnY6FjUjVt6s4LoADmwoig1qqD0oK8h1p/8mlMx8Oig=="],

    "playground": ["playground@workspace:playground"],

    "playground-nuxt": ["playground-nuxt@workspace:playground/nuxt"],

    "postcss": ["postcss@8.5.8", "", { "dependencies": { "nanoid": "^3.3.11", "picocolors": "^1.1.1", "source-map-js": "^1.2.1" } }, "sha512-OW/rX8O/jXnm82Ey1k44pObPtdblfiuWnrd8X7GJ7emImCOstunGbXUpp7HdBrFQX6rJzn3sPT397Wp5aCwCHg=="],

    "postcss-calc": ["postcss-calc@10.1.1", "", { "dependencies": { "postcss-selector-parser": "^7.0.0", "postcss-value-parser": "^4.2.0" }, "peerDependencies": { "postcss": "^8.4.38" } }, "sha512-NYEsLHh8DgG/PRH2+G9BTuUdtf9ViS+vdoQ0YA5OQdGsfN4ztiwtDWNtBl9EKeqNMFnIu8IKZ0cLxEQ5r5KVMw=="],

    "postcss-colormin": ["postcss-colormin@7.0.6", "", { "dependencies": { "browserslist": "^4.28.1", "caniuse-api": "^3.0.0", "colord": "^2.9.3", "postcss-value-parser": "^4.2.0" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-oXM2mdx6IBTRm39797QguYzVEWzbdlFiMNfq88fCCN1Wepw3CYmJ/1/Ifa/KjWo+j5ZURDl2NTldLJIw51IeNQ=="],

    "postcss-convert-values": ["postcss-convert-values@7.0.9", "", { "dependencies": { "browserslist": "^4.28.1", "postcss-value-parser": "^4.2.0" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-l6uATQATZaCa0bckHV+r6dLXfWtUBKXxO3jK+AtxxJJtgMPD+VhhPCCx51I4/5w8U5uHV67g3w7PXj+V3wlMlg=="],

    "postcss-discard-comments": ["postcss-discard-comments@7.0.6", "", { "dependencies": { "postcss-selector-parser": "^7.1.1" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-Sq+Fzj1Eg5/CPf1ERb0wS1Im5cvE2gDXCE+si4HCn1sf+jpQZxDI4DXEp8t77B/ImzDceWE2ebJQFXdqZ6GRJw=="],

    "postcss-discard-duplicates": ["postcss-discard-duplicates@7.0.2", "", { "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-eTonaQvPZ/3i1ASDHOKkYwAybiM45zFIc7KXils4mQmHLqIswXD9XNOKEVxtTFnsmwYzF66u4LMgSr0abDlh5w=="],

    "postcss-discard-empty": ["postcss-discard-empty@7.0.1", "", { "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-cFrJKZvcg/uxB6Ijr4l6qmn3pXQBna9zyrPC+sK0zjbkDUZew+6xDltSF7OeB7rAtzaaMVYSdbod+sZOCWnMOg=="],

    "postcss-discard-overridden": ["postcss-discard-overridden@7.0.1", "", { "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-7c3MMjjSZ/qYrx3uc1940GSOzN1Iqjtlqe8uoSg+qdVPYyRb0TILSqqmtlSFuE4mTDECwsm397Ya7iXGzfF7lg=="],

    "postcss-merge-longhand": ["postcss-merge-longhand@7.0.5", "", { "dependencies": { "postcss-value-parser": "^4.2.0", "stylehacks": "^7.0.5" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-Kpu5v4Ys6QI59FxmxtNB/iHUVDn9Y9sYw66D6+SZoIk4QTz1prC4aYkhIESu+ieG1iylod1f8MILMs1Em3mmIw=="],

    "postcss-merge-rules": ["postcss-merge-rules@7.0.8", "", { "dependencies": { "browserslist": "^4.28.1", "caniuse-api": "^3.0.0", "cssnano-utils": "^5.0.1", "postcss-selector-parser": "^7.1.1" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-BOR1iAM8jnr7zoQSlpeBmCsWV5Uudi/+5j7k05D0O/WP3+OFMPD86c1j/20xiuRtyt45bhxw/7hnhZNhW2mNFA=="],

    "postcss-minify-font-values": ["postcss-minify-font-values@7.0.1", "", { "dependencies": { "postcss-value-parser": "^4.2.0" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-2m1uiuJeTplll+tq4ENOQSzB8LRnSUChBv7oSyFLsJRtUgAAJGP6LLz0/8lkinTgxrmJSPOEhgY1bMXOQ4ZXhQ=="],

    "postcss-minify-gradients": ["postcss-minify-gradients@7.0.1", "", { "dependencies": { "colord": "^2.9.3", "cssnano-utils": "^5.0.1", "postcss-value-parser": "^4.2.0" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-X9JjaysZJwlqNkJbUDgOclyG3jZEpAMOfof6PUZjPnPrePnPG62pS17CjdM32uT1Uq1jFvNSff9l7kNbmMSL2A=="],

    "postcss-minify-params": ["postcss-minify-params@7.0.6", "", { "dependencies": { "browserslist": "^4.28.1", "cssnano-utils": "^5.0.1", "postcss-value-parser": "^4.2.0" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-YOn02gC68JijlaXVuKvFSCvQOhTpblkcfDre2hb/Aaa58r2BIaK4AtE/cyZf2wV7YKAG+UlP9DT+By0ry1E4VQ=="],

    "postcss-minify-selectors": ["postcss-minify-selectors@7.0.6", "", { "dependencies": { "cssesc": "^3.0.0", "postcss-selector-parser": "^7.1.1" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-lIbC0jy3AAwDxEgciZlBullDiMBeBCT+fz5G8RcA9MWqh/hfUkpOI3vNDUNEZHgokaoiv0juB9Y8fGcON7rU/A=="],

    "postcss-normalize-charset": ["postcss-normalize-charset@7.0.1", "", { "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-sn413ofhSQHlZFae//m9FTOfkmiZ+YQXsbosqOWRiVQncU2BA3daX3n0VF3cG6rGLSFVc5Di/yns0dFfh8NFgQ=="],

    "postcss-normalize-display-values": ["postcss-normalize-display-values@7.0.1", "", { "dependencies": { "postcss-value-parser": "^4.2.0" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-E5nnB26XjSYz/mGITm6JgiDpAbVuAkzXwLzRZtts19jHDUBFxZ0BkXAehy0uimrOjYJbocby4FVswA/5noOxrQ=="],

    "postcss-normalize-positions": ["postcss-normalize-positions@7.0.1", "", { "dependencies": { "postcss-value-parser": "^4.2.0" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-pB/SzrIP2l50ZIYu+yQZyMNmnAcwyYb9R1fVWPRxm4zcUFCY2ign7rcntGFuMXDdd9L2pPNUgoODDk91PzRZuQ=="],

    "postcss-normalize-repeat-style": ["postcss-normalize-repeat-style@7.0.1", "", { "dependencies": { "postcss-value-parser": "^4.2.0" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-NsSQJ8zj8TIDiF0ig44Byo3Jk9e4gNt9x2VIlJudnQQ5DhWAHJPF4Tr1ITwyHio2BUi/I6Iv0HRO7beHYOloYQ=="],

    "postcss-normalize-string": ["postcss-normalize-string@7.0.1", "", { "dependencies": { "postcss-value-parser": "^4.2.0" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-QByrI7hAhsoze992kpbMlJSbZ8FuCEc1OT9EFbZ6HldXNpsdpZr+YXC5di3UEv0+jeZlHbZcoCADgb7a+lPmmQ=="],

    "postcss-normalize-timing-functions": ["postcss-normalize-timing-functions@7.0.1", "", { "dependencies": { "postcss-value-parser": "^4.2.0" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-bHifyuuSNdKKsnNJ0s8fmfLMlvsQwYVxIoUBnowIVl2ZAdrkYQNGVB4RxjfpvkMjipqvbz0u7feBZybkl/6NJg=="],

    "postcss-normalize-unicode": ["postcss-normalize-unicode@7.0.6", "", { "dependencies": { "browserslist": "^4.28.1", "postcss-value-parser": "^4.2.0" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-z6bwTV84YW6ZvvNoaNLuzRW4/uWxDKYI1iIDrzk6D2YTL7hICApy+Q1LP6vBEsljX8FM7YSuV9qI79XESd4ddQ=="],

    "postcss-normalize-url": ["postcss-normalize-url@7.0.1", "", { "dependencies": { "postcss-value-parser": "^4.2.0" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-sUcD2cWtyK1AOL/82Fwy1aIVm/wwj5SdZkgZ3QiUzSzQQofrbq15jWJ3BA7Z+yVRwamCjJgZJN0I9IS7c6tgeQ=="],

    "postcss-normalize-whitespace": ["postcss-normalize-whitespace@7.0.1", "", { "dependencies": { "postcss-value-parser": "^4.2.0" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-vsbgFHMFQrJBJKrUFJNZ2pgBeBkC2IvvoHjz1to0/0Xk7sII24T0qFOiJzG6Fu3zJoq/0yI4rKWi7WhApW+EFA=="],

    "postcss-ordered-values": ["postcss-ordered-values@7.0.2", "", { "dependencies": { "cssnano-utils": "^5.0.1", "postcss-value-parser": "^4.2.0" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-AMJjt1ECBffF7CEON/Y0rekRLS6KsePU6PRP08UqYW4UGFRnTXNrByUzYK1h8AC7UWTZdQ9O3Oq9kFIhm0SFEw=="],

    "postcss-reduce-initial": ["postcss-reduce-initial@7.0.6", "", { "dependencies": { "browserslist": "^4.28.1", "caniuse-api": "^3.0.0" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-G6ZyK68AmrPdMB6wyeA37ejnnRG2S8xinJrZJnOv+IaRKf6koPAVbQsiC7MfkmXaGmF1UO+QCijb27wfpxuRNg=="],

    "postcss-reduce-transforms": ["postcss-reduce-transforms@7.0.1", "", { "dependencies": { "postcss-value-parser": "^4.2.0" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-MhyEbfrm+Mlp/36hvZ9mT9DaO7dbncU0CvWI8V93LRkY6IYlu38OPg3FObnuKTUxJ4qA8HpurdQOo5CyqqO76g=="],

    "postcss-selector-parser": ["postcss-selector-parser@7.1.1", "", { "dependencies": { "cssesc": "^3.0.0", "util-deprecate": "^1.0.2" } }, "sha512-orRsuYpJVw8LdAwqqLykBj9ecS5/cRHlI5+nvTo8LcCKmzDmqVORXtOIYEEQuL9D4BxtA1lm5isAqzQZCoQ6Eg=="],

    "postcss-svgo": ["postcss-svgo@7.1.1", "", { "dependencies": { "postcss-value-parser": "^4.2.0", "svgo": "^4.0.1" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-zU9H9oEDrUFKa0JB7w+IYL7Qs9ey1mZyjhbf0KLxwJDdDRtoPvCmaEfknzqfHj44QS9VD6c5sJnBAVYTLRg/Sg=="],

    "postcss-unique-selectors": ["postcss-unique-selectors@7.0.5", "", { "dependencies": { "postcss-selector-parser": "^7.1.1" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-3QoYmEt4qg/rUWDn6Tc8+ZVPmbp4G1hXDtCNWDx0st8SjtCbRcxRXDDM1QrEiXGG3A45zscSJFb4QH90LViyxg=="],

    "postcss-value-parser": ["postcss-value-parser@4.2.0", "", {}, "sha512-1NNCs6uurfkVbeXG4S8JFT9t19m45ICnif8zWLd5oPSZ50QnwMfK+H3jv408d4jw/7Bttv5axS5IiHoLaVNHeQ=="],

    "prettier": ["prettier@3.8.1", "", { "bin": { "prettier": "bin/prettier.cjs" } }, "sha512-UOnG6LftzbdaHZcKoPFtOcCKztrQ57WkHDeRD9t/PTQtmT0NHSeWWepj6pS0z/N7+08BHFDQVUrfmfMRcZwbMg=="],

    "pretty-bytes": ["pretty-bytes@7.1.0", "", {}, "sha512-nODzvTiYVRGRqAOvE84Vk5JDPyyxsVk0/fbA/bq7RqlnhksGpset09XTxbpvLTIjoaF7K8Z8DG8yHtKGTPSYRw=="],

    "pretty-ms": ["pretty-ms@9.3.0", "", { "dependencies": { "parse-ms": "^4.0.0" } }, "sha512-gjVS5hOP+M3wMm5nmNOucbIrqudzs9v/57bWRHQWLYklXqoXKrVfYW2W9+glfGsqtPgpiz5WwyEEB+ksXIx3gQ=="],

    "prismjs": ["prismjs@1.30.0", "", {}, "sha512-DEvV2ZF2r2/63V+tK8hQvrR2ZGn10srHbXviTlcv7Kpzw8jWiNTqbVgjO3IY8RxrrOUF8VPMQQFysYYYv0YZxw=="],

    "process": ["process@0.11.10", "", {}, "sha512-cdGef/drWFoydD1JsMzuFf8100nZl+GT+yacc2bEced5f9Rjk4z+WtFUTBu9PhOi9j/jfmBPu0mMEY4wIdAF8A=="],

    "process-nextick-args": ["process-nextick-args@2.0.1", "", {}, "sha512-3ouUOpQhtgrbOa17J7+uxOTpITYWaGP7/AhoR3+A+/1e9skrzelGi/dXzEYyvbxubEF6Wn2ypscTKiKJFFn1ag=="],

    "prompts": ["prompts@2.4.2", "", { "dependencies": { "kleur": "^3.0.3", "sisteransi": "^1.0.5" } }, "sha512-NxNv/kLguCA7p3jE8oL2aEBsrJWgAakBpgmgK6lpPWV+WuOmY6r2/zbAVnP+T8bQlA0nzHXSJSJW0Hq7ylaD2Q=="],

    "property-information": ["property-information@7.1.0", "", {}, "sha512-TwEZ+X+yCJmYfL7TPUOcvBZ4QfoT5YenQiJuX//0th53DE6w0xxLEtfK3iyryQFddXuvkIk51EEgrJQ0WJkOmQ=="],

    "quansync": ["quansync@1.0.0", "", {}, "sha512-5xZacEEufv3HSTPQuchrvV6soaiACMFnq1H8wkVioctoH3TRha9Sz66lOxRwPK/qZj7HPiSveih9yAyh98gvqA=="],

    "queue-microtask": ["queue-microtask@1.2.3", "", {}, "sha512-NuaNSa6flKT5JaSYQzJok04JzTL1CA6aGhv5rfLW3PgqA+M2ChpZQnAC8h8i4ZFkBS8X5RqkDBHA7r4hej3K9A=="],

    "radix3": ["radix3@1.1.2", "", {}, "sha512-b484I/7b8rDEdSDKckSSBA8knMpcdsXudlE/LNL639wFoHKwLbEkQFZHWEYwDC0wa0FKUcCY+GAF73Z7wxNVFA=="],

    "randombytes": ["randombytes@2.1.0", "", { "dependencies": { "safe-buffer": "^5.1.0" } }, "sha512-vYl3iOX+4CKUWuxGi9Ukhie6fsqXqS9FE2Zaic4tNFD2N2QQaXOMFbuKK4QmDHC0JO6B1Zp41J0LpT0oR68amQ=="],

    "range-parser": ["range-parser@1.2.1", "", {}, "sha512-Hrgsx+orqoygnmhFbKaHE6c296J+HTAQXoxEF6gNupROmmGJRoyzfG3ccAveqCBrwr/2yxQ5BVd/GTl5agOwSg=="],

    "rc9": ["rc9@3.0.0", "", { "dependencies": { "defu": "^6.1.4", "destr": "^2.0.5" } }, "sha512-MGOue0VqscKWQ104udASX/3GYDcKyPI4j4F8gu/jHHzglpmy9a/anZK3PNe8ug6aZFl+9GxLtdhe3kVZuMaQbA=="],

    "react": ["react@19.2.4", "", {}, "sha512-9nfp2hYpCwOjAN+8TZFGhtWEwgvWHXqESH8qT89AT/lWklpLON22Lc8pEtnpsZz7VmawabSU0gCjnj8aC0euHQ=="],

    "react-dom": ["react-dom@19.2.4", "", { "dependencies": { "scheduler": "^0.27.0" }, "peerDependencies": { "react": "^19.2.4" } }, "sha512-AXJdLo8kgMbimY95O2aKQqsz2iWi9jMgKJhRBAxECE4IFxfcazB2LmzloIoibJI3C12IlY20+KFaLv+71bUJeQ=="],

    "react-refresh": ["react-refresh@0.17.0", "", {}, "sha512-z6F7K9bV85EfseRCp2bzrpyQ0Gkw1uLoCel9XBVWPg/TjRj94SkJzUTGfOa4bs7iJvBWtQG0Wq7wnI0syw3EBQ=="],

    "readable-stream": ["readable-stream@4.7.0", "", { "dependencies": { "abort-controller": "^3.0.0", "buffer": "^6.0.3", "events": "^3.3.0", "process": "^0.11.10", "string_decoder": "^1.3.0" } }, "sha512-oIGGmcpTLwPga8Bn6/Z75SVaH1z5dUut2ibSyAMVhmUggWpmDn2dapB0n7f8nwaSiRtepAsfJyfXIO5DCVAODg=="],

    "readdir-glob": ["readdir-glob@1.1.3", "", { "dependencies": { "minimatch": "^5.1.0" } }, "sha512-v05I2k7xN8zXvPD9N+z/uhXPaj0sUFCe2rcWZIpBsqxfP7xXFQ0tipAd/wjj1YxWyWtUS5IDJpOG82JKt2EAVA=="],

    "readdirp": ["readdirp@4.1.2", "", {}, "sha512-GDhwkLfywWL2s6vEjyhri+eXmfH6j1L7JE27WhqLeYzoh/A3DBaYGEj2H/HFZCn/kMfim73FXxEJTw06WtxQwg=="],

    "redis-errors": ["redis-errors@1.2.0", "", {}, "sha512-1qny3OExCf0UvUV/5wpYKf2YwPcOqXzkwKKSmKHiE6ZMQs5heeE/c8eXK+PNllPvmjgAbfnsbpkGZWy8cBpn9w=="],

    "redis-parser": ["redis-parser@3.0.0", "", { "dependencies": { "redis-errors": "^1.0.0" } }, "sha512-DJnGAeenTdpMEH6uAJRK/uiyEIH9WVsUmoLwzudwGJUwZPp80PDBWPHXSAGNPwNvIXAbe7MSUB1zQFugFml66A=="],

    "regex": ["regex@6.1.0", "", { "dependencies": { "regex-utilities": "^2.3.0" } }, "sha512-6VwtthbV4o/7+OaAF9I5L5V3llLEsoPyq9P1JVXkedTP33c7MfCG0/5NOPcSJn0TzXcG9YUrR0gQSWioew3LDg=="],

    "regex-recursion": ["regex-recursion@6.0.2", "", { "dependencies": { "regex-utilities": "^2.3.0" } }, "sha512-0YCaSCq2VRIebiaUviZNs0cBz1kg5kVS2UKUfNIx8YVs1cN3AV7NTctO5FOKBA+UT2BPJIWZauYHPqJODG50cg=="],

    "regex-utilities": ["regex-utilities@2.3.0", "", {}, "sha512-8VhliFJAWRaUiVvREIiW2NXXTmHs4vMNnSzuJVhscgmGav3g9VDxLrQndI3dZZVVdp0ZO/5v0xmX516/7M9cng=="],

    "regexp-tree": ["regexp-tree@0.1.27", "", { "bin": { "regexp-tree": "bin/regexp-tree" } }, "sha512-iETxpjK6YoRWJG5o6hXLwvjYAoW+FEZn9os0PD/b6AP6xQwsa/Y7lCVgIixBbUPMfhu+i2LtdeAqVTgGlQarfA=="],

    "rehype": ["rehype@13.0.2", "", { "dependencies": { "@types/hast": "^3.0.0", "rehype-parse": "^9.0.0", "rehype-stringify": "^10.0.0", "unified": "^11.0.0" } }, "sha512-j31mdaRFrwFRUIlxGeuPXXKWQxet52RBQRvCmzl5eCefn/KGbomK5GMHNMsOJf55fgo3qw5tST5neDuarDYR2A=="],

    "rehype-parse": ["rehype-parse@9.0.1", "", { "dependencies": { "@types/hast": "^3.0.0", "hast-util-from-html": "^2.0.0", "unified": "^11.0.0" } }, "sha512-ksCzCD0Fgfh7trPDxr2rSylbwq9iYDkSn8TCDmEJ49ljEUBxDVCzCHv7QNzZOfODanX4+bWQ4WZqLCRWYLfhag=="],

    "rehype-raw": ["rehype-raw@7.0.0", "", { "dependencies": { "@types/hast": "^3.0.0", "hast-util-raw": "^9.0.0", "vfile": "^6.0.0" } }, "sha512-/aE8hCfKlQeA8LmyeyQvQF3eBiLRGNlfBJEvWH7ivp9sBqs7TNqBL5X3v157rM4IFETqDnIOO+z5M/biZbo9Ww=="],

    "rehype-stringify": ["rehype-stringify@10.0.1", "", { "dependencies": { "@types/hast": "^3.0.0", "hast-util-to-html": "^9.0.0", "unified": "^11.0.0" } }, "sha512-k9ecfXHmIPuFVI61B9DeLPN0qFHfawM6RsuX48hoqlaKSF61RskNjSm1lI8PhBEM0MRdLxVVm4WmTqJQccH9mA=="],

    "remark-gfm": ["remark-gfm@4.0.1", "", { "dependencies": { "@types/mdast": "^4.0.0", "mdast-util-gfm": "^3.0.0", "micromark-extension-gfm": "^3.0.0", "remark-parse": "^11.0.0", "remark-stringify": "^11.0.0", "unified": "^11.0.0" } }, "sha512-1quofZ2RQ9EWdeN34S79+KExV1764+wCUGop5CPL1WGdD0ocPpu91lzPGbwWMECpEpd42kJGQwzRfyov9j4yNg=="],

    "remark-parse": ["remark-parse@11.0.0", "", { "dependencies": { "@types/mdast": "^4.0.0", "mdast-util-from-markdown": "^2.0.0", "micromark-util-types": "^2.0.0", "unified": "^11.0.0" } }, "sha512-FCxlKLNGknS5ba/1lmpYijMUzX2esxW5xQqjWxw2eHFfS2MSdaHVINFmhjo+qN1WhZhNimq0dZATN9pH0IDrpA=="],

    "remark-rehype": ["remark-rehype@11.1.2", "", { "dependencies": { "@types/hast": "^3.0.0", "@types/mdast": "^4.0.0", "mdast-util-to-hast": "^13.0.0", "unified": "^11.0.0", "vfile": "^6.0.0" } }, "sha512-Dh7l57ianaEoIpzbp0PC9UKAdCSVklD8E5Rpw7ETfbTl3FqcOOgq5q2LVDhgGCkaBv7p24JXikPdvhhmHvKMsw=="],

    "remark-smartypants": ["remark-smartypants@3.0.2", "", { "dependencies": { "retext": "^9.0.0", "retext-smartypants": "^6.0.0", "unified": "^11.0.4", "unist-util-visit": "^5.0.0" } }, "sha512-ILTWeOriIluwEvPjv67v7Blgrcx+LZOkAUVtKI3putuhlZm84FnqDORNXPPm+HY3NdZOMhyDwZ1E+eZB/Df5dA=="],

    "remark-stringify": ["remark-stringify@11.0.0", "", { "dependencies": { "@types/mdast": "^4.0.0", "mdast-util-to-markdown": "^2.0.0", "unified": "^11.0.0" } }, "sha512-1OSmLd3awB/t8qdoEOMazZkNsfVTeY4fTsgzcQFdXNq8ToTN4ZGwrMnlda4K6smTFKD+GRV6O48i6Z4iKgPPpw=="],

    "request-light": ["request-light@0.7.0", "", {}, "sha512-lMbBMrDoxgsyO+yB3sDcrDuX85yYt7sS8BfQd11jtbW/z5ZWgLZRcEGLsLoYw7I0WSUGQBs8CC8ScIxkTX1+6Q=="],

    "require-directory": ["require-directory@2.1.1", "", {}, "sha512-fGxEI7+wsG9xrvdjsrlmL22OMTTiHRwAMroiEeMgq8gzoLC/PQr7RsRDSTLUg/bZAZtF+TVIkHc6/4RIKrui+Q=="],

    "require-from-string": ["require-from-string@2.0.2", "", {}, "sha512-Xf0nWe6RseziFMu+Ap9biiUbmplq6S9/p+7w7YXP/JBHhrUDDUhwa+vANyubuqfZWTveU//DYVGsDG7RKL/vEw=="],

    "resolve": ["resolve@1.22.11", "", { "dependencies": { "is-core-module": "^2.16.1", "path-parse": "^1.0.7", "supports-preserve-symlinks-flag": "^1.0.0" }, "bin": { "resolve": "bin/resolve" } }, "sha512-RfqAvLnMl313r7c9oclB1HhUEAezcpLjz95wFH4LVuhk9JF/r22qmVP9AMmOU4vMX7Q8pN8jwNg/CSpdFnMjTQ=="],

    "resolve-from": ["resolve-from@5.0.0", "", {}, "sha512-qYg9KP24dD5qka9J47d0aVky0N+b4fTU89LN9iDnjB5waksiC49rvMB0PrUJQGoTmH50XPiqOvAjDfaijGxYZw=="],

    "resolve-pkg-maps": ["resolve-pkg-maps@1.0.0", "", {}, "sha512-seS2Tj26TBVOC2NIc2rOe2y2ZO7efxITtLZcGSOnHHNOQ7CkiUBfw0Iw2ck6xkIhPwLhKNLS8BO+hEpngQlqzw=="],

    "retext": ["retext@9.0.0", "", { "dependencies": { "@types/nlcst": "^2.0.0", "retext-latin": "^4.0.0", "retext-stringify": "^4.0.0", "unified": "^11.0.0" } }, "sha512-sbMDcpHCNjvlheSgMfEcVrZko3cDzdbe1x/e7G66dFp0Ff7Mldvi2uv6JkJQzdRcvLYE8CA8Oe8siQx8ZOgTcA=="],

    "retext-latin": ["retext-latin@4.0.0", "", { "dependencies": { "@types/nlcst": "^2.0.0", "parse-latin": "^7.0.0", "unified": "^11.0.0" } }, "sha512-hv9woG7Fy0M9IlRQloq/N6atV82NxLGveq+3H2WOi79dtIYWN8OaxogDm77f8YnVXJL2VD3bbqowu5E3EMhBYA=="],

    "retext-smartypants": ["retext-smartypants@6.2.0", "", { "dependencies": { "@types/nlcst": "^2.0.0", "nlcst-to-string": "^4.0.0", "unist-util-visit": "^5.0.0" } }, "sha512-kk0jOU7+zGv//kfjXEBjdIryL1Acl4i9XNkHxtM7Tm5lFiCog576fjNC9hjoR7LTKQ0DsPWy09JummSsH1uqfQ=="],

    "retext-stringify": ["retext-stringify@4.0.0", "", { "dependencies": { "@types/nlcst": "^2.0.0", "nlcst-to-string": "^4.0.0", "unified": "^11.0.0" } }, "sha512-rtfN/0o8kL1e+78+uxPTqu1Klt0yPzKuQ2BfWwwfgIUSayyzxpM1PJzkKt4V8803uB9qSy32MvI7Xep9khTpiA=="],

    "reusify": ["reusify@1.1.0", "", {}, "sha512-g6QUff04oZpHs0eG5p83rFLhHeV00ug/Yf9nZM6fLeUrPguBTkTQOdpAWWspMh55TZfVQDPaN3NQJfbVRAxdIw=="],

    "rfdc": ["rfdc@1.4.1", "", {}, "sha512-q1b3N5QkRUWUl7iyylaaj3kOpIT0N2i9MqIEQXP73GVsN9cw3fdx8X63cEmWhJGi2PPCF23Ijp7ktmd39rawIA=="],

    "rolldown": ["rolldown@1.0.0-rc.9", "", { "dependencies": { "@oxc-project/types": "=0.115.0", "@rolldown/pluginutils": "1.0.0-rc.9" }, "optionalDependencies": { "@rolldown/binding-android-arm64": "1.0.0-rc.9", "@rolldown/binding-darwin-arm64": "1.0.0-rc.9", "@rolldown/binding-darwin-x64": "1.0.0-rc.9", "@rolldown/binding-freebsd-x64": "1.0.0-rc.9", "@rolldown/binding-linux-arm-gnueabihf": "1.0.0-rc.9", "@rolldown/binding-linux-arm64-gnu": "1.0.0-rc.9", "@rolldown/binding-linux-arm64-musl": "1.0.0-rc.9", "@rolldown/binding-linux-ppc64-gnu": "1.0.0-rc.9", "@rolldown/binding-linux-s390x-gnu": "1.0.0-rc.9", "@rolldown/binding-linux-x64-gnu": "1.0.0-rc.9", "@rolldown/binding-linux-x64-musl": "1.0.0-rc.9", "@rolldown/binding-openharmony-arm64": "1.0.0-rc.9", "@rolldown/binding-wasm32-wasi": "1.0.0-rc.9", "@rolldown/binding-win32-arm64-msvc": "1.0.0-rc.9", "@rolldown/binding-win32-x64-msvc": "1.0.0-rc.9" }, "bin": { "rolldown": "bin/cli.mjs" } }, "sha512-9EbgWge7ZH+yqb4d2EnELAntgPTWbfL8ajiTW+SyhJEC4qhBbkCKbqFV4Ge4zmu5ziQuVbWxb/XwLZ+RIO7E8Q=="],

    "rolldown-plugin-dts": ["rolldown-plugin-dts@0.22.5", "", { "dependencies": { "@babel/generator": "8.0.0-rc.2", "@babel/helper-validator-identifier": "8.0.0-rc.2", "@babel/parser": "8.0.0-rc.2", "@babel/types": "8.0.0-rc.2", "ast-kit": "^3.0.0-beta.1", "birpc": "^4.0.0", "dts-resolver": "^2.1.3", "get-tsconfig": "^4.13.6", "obug": "^2.1.1" }, "peerDependencies": { "@ts-macro/tsc": "^0.3.6", "@typescript/native-preview": ">=7.0.0-dev.20250601.1", "rolldown": "^1.0.0-rc.3", "typescript": "^5.0.0 || ^6.0.0-beta", "vue-tsc": "~3.2.0" }, "optionalPeers": ["@ts-macro/tsc", "@typescript/native-preview", "typescript", "vue-tsc"] }, "sha512-M/HXfM4cboo+jONx9Z0X+CUf3B5tCi7ni+kR5fUW50Fp9AlZk0oVLesibGWgCXDKFp5lpgQ9yhKoImUFjl3VZw=="],

    "rollup": ["rollup@4.59.0", "", { "dependencies": { "@types/estree": "1.0.8" }, "optionalDependencies": { "@rollup/rollup-android-arm-eabi": "4.59.0", "@rollup/rollup-android-arm64": "4.59.0", "@rollup/rollup-darwin-arm64": "4.59.0", "@rollup/rollup-darwin-x64": "4.59.0", "@rollup/rollup-freebsd-arm64": "4.59.0", "@rollup/rollup-freebsd-x64": "4.59.0", "@rollup/rollup-linux-arm-gnueabihf": "4.59.0", "@rollup/rollup-linux-arm-musleabihf": "4.59.0", "@rollup/rollup-linux-arm64-gnu": "4.59.0", "@rollup/rollup-linux-arm64-musl": "4.59.0", "@rollup/rollup-linux-loong64-gnu": "4.59.0", "@rollup/rollup-linux-loong64-musl": "4.59.0", "@rollup/rollup-linux-ppc64-gnu": "4.59.0", "@rollup/rollup-linux-ppc64-musl": "4.59.0", "@rollup/rollup-linux-riscv64-gnu": "4.59.0", "@rollup/rollup-linux-riscv64-musl": "4.59.0", "@rollup/rollup-linux-s390x-gnu": "4.59.0", "@rollup/rollup-linux-x64-gnu": "4.59.0", "@rollup/rollup-linux-x64-musl": "4.59.0", "@rollup/rollup-openbsd-x64": "4.59.0", "@rollup/rollup-openharmony-arm64": "4.59.0", "@rollup/rollup-win32-arm64-msvc": "4.59.0", "@rollup/rollup-win32-ia32-msvc": "4.59.0", "@rollup/rollup-win32-x64-gnu": "4.59.0", "@rollup/rollup-win32-x64-msvc": "4.59.0", "fsevents": "~2.3.2" }, "bin": { "rollup": "dist/bin/rollup" } }, "sha512-2oMpl67a3zCH9H79LeMcbDhXW/UmWG/y2zuqnF2jQq5uq9TbM9TVyXvA4+t+ne2IIkBdrLpAaRQAvo7YI/Yyeg=="],

    "rollup-plugin-visualizer": ["rollup-plugin-visualizer@6.0.11", "", { "dependencies": { "open": "^8.0.0", "picomatch": "^4.0.2", "source-map": "^0.7.4", "yargs": "^17.5.1" }, "peerDependencies": { "rolldown": "1.x || ^1.0.0-beta", "rollup": "2.x || 3.x || 4.x" }, "optionalPeers": ["rolldown", "rollup"], "bin": { "rollup-plugin-visualizer": "dist/bin/cli.js" } }, "sha512-TBwVHVY7buHjIKVLqr9scTVFwqZqMXINcCphPwIWKPDCOBIa+jCQfafvbjRJDZgXdq/A996Dy6yGJ/+/NtAXDQ=="],

    "rou3": ["rou3@0.8.1", "", {}, "sha512-ePa+XGk00/3HuCqrEnK3LxJW7I0SdNg6EFzKUJG73hMAdDcOUC/i/aSz7LSDwLrGr33kal/rqOGydzwl6U7zBA=="],

    "run-applescript": ["run-applescript@7.1.0", "", {}, "sha512-DPe5pVFaAsinSaV6QjQ6gdiedWDcRCbUuiQfQa2wmWV7+xC9bGulGI8+TdRmoFkAPaBXk8CrAbnlY2ISniJ47Q=="],

    "run-parallel": ["run-parallel@1.2.0", "", { "dependencies": { "queue-microtask": "^1.2.2" } }, "sha512-5l4VyZR86LZ/lDxZTR6jqL8AFE2S0IFLMP26AbjsLVADxHdhB/c0GUsH+y39UfCi3dzz8OlQuPmnaJOMoDHQBA=="],

    "safe-buffer": ["safe-buffer@5.2.1", "", {}, "sha512-rp3So07KcdmmKbGvgaNxQSJr7bGVSVk5S9Eq1F+ppbRo70+YeaDxkw5Dd8NPN+GD6bjnYm2VuPuCXmpuYvmCXQ=="],

    "sax": ["sax@1.6.0", "", {}, "sha512-6R3J5M4AcbtLUdZmRv2SygeVaM7IhrLXu9BmnOGmmACak8fiUtOsYNWUS4uK7upbmHIBbLBeFeI//477BKLBzA=="],

    "scheduler": ["scheduler@0.27.0", "", {}, "sha512-eNv+WrVbKu1f3vbYJT/xtiF5syA5HPIMtf9IgY/nKg0sWqzAUEvqY/xm7OcZc/qafLx/iO9FgOmeSAp4v5ti/Q=="],

    "scule": ["scule@1.3.0", "", {}, "sha512-6FtHJEvt+pVMIB9IBY+IcCJ6Z5f1iQnytgyfKMhDKgmzYG+TeH/wx1y3l27rshSbLiSanrR9ffZDrEsmjlQF2g=="],

    "semver": ["semver@7.7.4", "", { "bin": { "semver": "bin/semver.js" } }, "sha512-vFKC2IEtQnVhpT78h1Yp8wzwrf8CM+MzKMHGJZfBtzhZNycRFnXsHk6E5TxIkkMsgNS7mdX3AGB7x2QM2di4lA=="],

    "send": ["send@1.2.1", "", { "dependencies": { "debug": "^4.4.3", "encodeurl": "^2.0.0", "escape-html": "^1.0.3", "etag": "^1.8.1", "fresh": "^2.0.0", "http-errors": "^2.0.1", "mime-types": "^3.0.2", "ms": "^2.1.3", "on-finished": "^2.4.1", "range-parser": "^1.2.1", "statuses": "^2.0.2" } }, "sha512-1gnZf7DFcoIcajTjTwjwuDjzuz4PPcY2StKPlsGAQ1+YH20IRVrBaXSWmdjowTJ6u8Rc01PoYOGHXfP1mYcZNQ=="],

    "serialize-javascript": ["serialize-javascript@6.0.2", "", { "dependencies": { "randombytes": "^2.1.0" } }, "sha512-Saa1xPByTTq2gdeFZYLLo+RFE35NHZkAbqZeWNd3BpzppeVisAqpDjcp8dyf6uIvEqJRd46jemmyA4iFIeVk8g=="],

    "seroval": ["seroval@1.5.1", "", {}, "sha512-OwrZRZAfhHww0WEnKHDY8OM0U/Qs8OTfIDWhUD4BLpNJUfXK4cGmjiagGze086m+mhI+V2nD0gfbHEnJjb9STA=="],

    "serve-placeholder": ["serve-placeholder@2.0.2", "", { "dependencies": { "defu": "^6.1.4" } }, "sha512-/TMG8SboeiQbZJWRlfTCqMs2DD3SZgWp0kDQePz9yUuCnDfDh/92gf7/PxGhzXTKBIPASIHxFcZndoNbp6QOLQ=="],

    "serve-static": ["serve-static@2.2.1", "", { "dependencies": { "encodeurl": "^2.0.0", "escape-html": "^1.0.3", "parseurl": "^1.3.3", "send": "^1.2.0" } }, "sha512-xRXBn0pPqQTVQiC8wyQrKs2MOlX24zQ0POGaj0kultvoOCstBQM5yvOhAVSUwOMjQtTvsPWoNCHfPGwaaQJhTw=="],

    "setprototypeof": ["setprototypeof@1.2.0", "", {}, "sha512-E5LDX7Wrp85Kil5bhZv46j8jOeboKq5JMmYM3gVGdGH8xFpPWXUMsNrlODCrkoxMEeNi/XZIwuRvY4XNwYMJpw=="],

    "sharp": ["sharp@0.34.5", "", { "dependencies": { "@img/colour": "^1.0.0", "detect-libc": "^2.1.2", "semver": "^7.7.3" }, "optionalDependencies": { "@img/sharp-darwin-arm64": "0.34.5", "@img/sharp-darwin-x64": "0.34.5", "@img/sharp-libvips-darwin-arm64": "1.2.4", "@img/sharp-libvips-darwin-x64": "1.2.4", "@img/sharp-libvips-linux-arm": "1.2.4", "@img/sharp-libvips-linux-arm64": "1.2.4", "@img/sharp-libvips-linux-ppc64": "1.2.4", "@img/sharp-libvips-linux-riscv64": "1.2.4", "@img/sharp-libvips-linux-s390x": "1.2.4", "@img/sharp-libvips-linux-x64": "1.2.4", "@img/sharp-libvips-linuxmusl-arm64": "1.2.4", "@img/sharp-libvips-linuxmusl-x64": "1.2.4", "@img/sharp-linux-arm": "0.34.5", "@img/sharp-linux-arm64": "0.34.5", "@img/sharp-linux-ppc64": "0.34.5", "@img/sharp-linux-riscv64": "0.34.5", "@img/sharp-linux-s390x": "0.34.5", "@img/sharp-linux-x64": "0.34.5", "@img/sharp-linuxmusl-arm64": "0.34.5", "@img/sharp-linuxmusl-x64": "0.34.5", "@img/sharp-wasm32": "0.34.5", "@img/sharp-win32-arm64": "0.34.5", "@img/sharp-win32-ia32": "0.34.5", "@img/sharp-win32-x64": "0.34.5" } }, "sha512-Ou9I5Ft9WNcCbXrU9cMgPBcCK8LiwLqcbywW3t4oDV37n1pzpuNLsYiAV8eODnjbtQlSDwZ2cUEeQz4E54Hltg=="],

    "shebang-command": ["shebang-command@2.0.0", "", { "dependencies": { "shebang-regex": "^3.0.0" } }, "sha512-kHxr2zZpYtdmrN1qDjrrX/Z1rR1kG8Dx+gkpK1G4eXmvXswmcE1hTWBWYUzlraYw1/yZp6YuDY77YtvbN0dmDA=="],

    "shebang-regex": ["shebang-regex@3.0.0", "", {}, "sha512-7++dFhtcx3353uBaq8DDR4NuxBetBzC7ZQOhmTQInHEd6bSrXdiEyzCvG07Z44UYdLShWUyXt5M/yhz8ekcb1A=="],

    "shell-quote": ["shell-quote@1.8.3", "", {}, "sha512-ObmnIF4hXNg1BqhnHmgbDETF8dLPCggZWBjkQfhZpbszZnYur5DUljTcCHii5LC3J5E0yeO/1LIMyH+UvHQgyw=="],

    "shiki": ["shiki@3.23.0", "", { "dependencies": { "@shikijs/core": "3.23.0", "@shikijs/engine-javascript": "3.23.0", "@shikijs/engine-oniguruma": "3.23.0", "@shikijs/langs": "3.23.0", "@shikijs/themes": "3.23.0", "@shikijs/types": "3.23.0", "@shikijs/vscode-textmate": "^10.0.2", "@types/hast": "^3.0.4" } }, "sha512-55Dj73uq9ZXL5zyeRPzHQsK7Nbyt6Y10k5s7OjuFZGMhpp4r/rsLBH0o/0fstIzX1Lep9VxefWljK/SKCzygIA=="],

    "signal-exit": ["signal-exit@4.1.0", "", {}, "sha512-bzyZ1e88w9O1iNJbKnOlvYTrWPDl46O1bG0D3XInv+9tkPrxrN8jUUTiFlDkkmKWgn1M6CfIA13SuGqOa9Korw=="],

    "simple-git": ["simple-git@3.33.0", "", { "dependencies": { "@kwsites/file-exists": "^1.1.1", "@kwsites/promise-deferred": "^1.1.1", "debug": "^4.4.0" } }, "sha512-D4V/tGC2sjsoNhoMybKyGoE+v8A60hRawKQ1iFRA1zwuDgGZCBJ4ByOzZ5J8joBbi4Oam0qiPH+GhzmSBwbJng=="],

    "sirv": ["sirv@3.0.2", "", { "dependencies": { "@polka/url": "^1.0.0-next.24", "mrmime": "^2.0.0", "totalist": "^3.0.0" } }, "sha512-2wcC/oGxHis/BoHkkPwldgiPSYcpZK3JU28WoMVv55yHJgcZ8rlXvuG9iZggz+sU1d4bRgIGASwyWqjxu3FM0g=="],

    "sisteransi": ["sisteransi@1.0.5", "", {}, "sha512-bLGGlR1QxBcynn2d5YmDX4MGjlZvy2MRBDRNHLJ8VI6l6+9FUiyTFNJ0IveOSP0bcXgVDPRcfGqA0pjaqUpfVg=="],

    "slash": ["slash@5.1.0", "", {}, "sha512-ZA6oR3T/pEyuqwMgAKT0/hAv8oAXckzbkmR0UkUosQ+Mc4RxGoJkRmwHgHufaenlyAgE1Mxgpdcrf75y6XcnDg=="],

    "smob": ["smob@1.6.1", "", {}, "sha512-KAkBqZl3c2GvNgNhcoyJae1aKldDW0LO279wF9bk1PnluRTETKBq0WyzRXxEhoQLk56yHaOY4JCBEKDuJIET5g=="],

    "smol-toml": ["smol-toml@1.6.0", "", {}, "sha512-4zemZi0HvTnYwLfrpk/CF9LOd9Lt87kAt50GnqhMpyF9U3poDAP2+iukq2bZsO/ufegbYehBkqINbsWxj4l4cw=="],

    "source-map": ["source-map@0.7.6", "", {}, "sha512-i5uvt8C3ikiWeNZSVZNWcfZPItFQOsYTUAOkcUPGd8DqDy1uOUikjt5dG+uRlwyvR108Fb9DOd4GvXfT0N2/uQ=="],

    "source-map-js": ["source-map-js@1.2.1", "", {}, "sha512-UXWMKhLOwVKb728IUtQPXxfYU+usdybtUrK/8uGE8CQMvrhOpwvzDBwj0QhSL7MQc7vIsISBG8VQ8+IDQxpfQA=="],

    "source-map-support": ["source-map-support@0.5.21", "", { "dependencies": { "buffer-from": "^1.0.0", "source-map": "^0.6.0" } }, "sha512-uBHU3L3czsIyYXKX88fdrGovxdSCoTGDRZ6SYXtSRxLZUzHg5P/66Ht6uoUlHu9EZod+inXhKo3qQgwXUT/y1w=="],

    "space-separated-tokens": ["space-separated-tokens@2.0.2", "", {}, "sha512-PEGlAwrG8yXGXRjW32fGbg66JAlOAwbObuqVoJpv/mRgoWDQfgH1wDPvtzWyUSNAXBGSk8h755YDbbcEy3SH2Q=="],

    "speakingurl": ["speakingurl@14.0.1", "", {}, "sha512-1POYv7uv2gXoyGFpBCmpDVSNV74IfsWlDW216UPjbWufNf+bSU6GdbDsxdcxtfwb4xlI3yxzOTKClUosxARYrQ=="],

    "srvx": ["srvx@0.11.12", "", { "bin": { "srvx": "bin/srvx.mjs" } }, "sha512-AQfrGqntqVPXgP03pvBDN1KyevHC+KmYVqb8vVf4N+aomQqdhaZxjvoVp+AOm4u6x+GgNQY3MVzAUIn+TqwkOA=="],

    "standard-as-callback": ["standard-as-callback@2.1.0", "", {}, "sha512-qoRRSyROncaz1z0mvYqIE4lCd9p2R90i6GxW3uZv5ucSu8tU7B5HXUP1gG8pVZsYNVaXjk8ClXHPttLyxAL48A=="],

    "stats-js": ["stats-js@1.0.1", "", {}, "sha512-EAwEFghGNv8mlYC4CZzI5kWghsnP8uBKXw6VLRHtXkOk5xySfUKLTqTkjgJFfDluIkf/O7eZwi5MXP50VeTbUg=="],

    "statuses": ["statuses@2.0.2", "", {}, "sha512-DvEy55V3DB7uknRo+4iOGT5fP1slR8wQohVdknigZPMpMstaKJQWhwiYBACJE3Ul2pTnATihhBYnRhZQHGBiRw=="],

    "std-env": ["std-env@4.0.0", "", {}, "sha512-zUMPtQ/HBY3/50VbpkupYHbRroTRZJPRLvreamgErJVys0ceuzMkD44J/QjqhHjOzK42GQ3QZIeFG1OYfOtKqQ=="],

    "streamx": ["streamx@2.23.0", "", { "dependencies": { "events-universal": "^1.0.0", "fast-fifo": "^1.3.2", "text-decoder": "^1.1.0" } }, "sha512-kn+e44esVfn2Fa/O0CPFcex27fjIL6MkVae0Mm6q+E6f0hWv578YCERbv+4m02cjxvDsPKLnmxral/rR6lBMAg=="],

    "string-width": ["string-width@4.2.3", "", { "dependencies": { "emoji-regex": "^8.0.0", "is-fullwidth-code-point": "^3.0.0", "strip-ansi": "^6.0.1" } }, "sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g=="],

    "string-width-cjs": ["string-width@4.2.3", "", { "dependencies": { "emoji-regex": "^8.0.0", "is-fullwidth-code-point": "^3.0.0", "strip-ansi": "^6.0.1" } }, "sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g=="],

    "string_decoder": ["string_decoder@1.3.0", "", { "dependencies": { "safe-buffer": "~5.2.0" } }, "sha512-hkRX8U1WjJFd8LsDJ2yQ/wWWxaopEsABU1XfkM8A+j0+85JAGppt16cr1Whg6KIbb4okU6Mql6BOj+uup/wKeA=="],

    "stringify-entities": ["stringify-entities@4.0.4", "", { "dependencies": { "character-entities-html4": "^2.0.0", "character-entities-legacy": "^3.0.0" } }, "sha512-IwfBptatlO+QCJUo19AqvrPNqlVMpW9YEL2LIVY+Rpv2qsjCGxaDLNRgeGsQWJhfItebuJhsGSLjaBbNSQ+ieg=="],

    "strip-ansi": ["strip-ansi@6.0.1", "", { "dependencies": { "ansi-regex": "^5.0.1" } }, "sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A=="],

    "strip-ansi-cjs": ["strip-ansi@6.0.1", "", { "dependencies": { "ansi-regex": "^5.0.1" } }, "sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A=="],

    "strip-final-newline": ["strip-final-newline@4.0.0", "", {}, "sha512-aulFJcD6YK8V1G7iRB5tigAP4TsHBZZrOV8pjV++zdUwmeV8uzbY7yn6h9MswN62adStNZFuCIx4haBnRuMDaw=="],

    "strip-literal": ["strip-literal@3.1.0", "", { "dependencies": { "js-tokens": "^9.0.1" } }, "sha512-8r3mkIM/2+PpjHoOtiAW8Rg3jJLHaV7xPwG+YRGrv6FP0wwk/toTpATxWYOW0BKdWwl82VT2tFYi5DlROa0Mxg=="],

    "structured-clone-es": ["structured-clone-es@2.0.0", "", {}, "sha512-5UuAHmBLXYPCl22xWJrFuGmIhBKQzxISPVz6E7nmTmTcAOpUzlbjKJsRrCE4vADmMQ0dzeCnlWn9XufnAGf76Q=="],

    "stylehacks": ["stylehacks@7.0.8", "", { "dependencies": { "browserslist": "^4.28.1", "postcss-selector-parser": "^7.1.1" }, "peerDependencies": { "postcss": "^8.4.32" } }, "sha512-I3f053GBLIiS5Fg6OMFhq/c+yW+5Hc2+1fgq7gElDMMSqwlRb3tBf2ef6ucLStYRpId4q//bQO1FjcyNyy4yDQ=="],

    "superjson": ["superjson@2.2.6", "", { "dependencies": { "copy-anything": "^4" } }, "sha512-H+ue8Zo4vJmV2nRjpx86P35lzwDT3nItnIsocgumgr0hHMQ+ZGq5vrERg9kJBo5AWGmxZDhzDo+WVIJqkB0cGA=="],

    "supports-color": ["supports-color@10.2.2", "", {}, "sha512-SS+jx45GF1QjgEXQx4NJZV9ImqmO2NPz5FNsIHrsDjh2YsHnawpan7SNQ1o8NuhrbHZy9AZhIoCUiCeaW/C80g=="],

    "supports-preserve-symlinks-flag": ["supports-preserve-symlinks-flag@1.0.0", "", {}, "sha512-ot0WnXS9fgdkgIcePe6RHNk1WA8+muPa6cSjeR3V8K27q9BB1rTE3R1p7Hv0z1ZyAc8s6Vvv8DIyWf681MAt0w=="],

    "svgo": ["svgo@4.0.1", "", { "dependencies": { "commander": "^11.1.0", "css-select": "^5.1.0", "css-tree": "^3.0.1", "css-what": "^6.1.0", "csso": "^5.0.5", "picocolors": "^1.1.1", "sax": "^1.5.0" }, "bin": "./bin/svgo.js" }, "sha512-XDpWUOPC6FEibaLzjfe0ucaV0YrOjYotGJO1WpF0Zd+n6ZGEQUsSugaoLq9QkEZtAfQIxT42UChcssDVPP3+/w=="],

    "system-architecture": ["system-architecture@0.1.0", "", {}, "sha512-ulAk51I9UVUyJgxlv9M6lFot2WP3e7t8Kz9+IS6D4rVba1tR9kON+Ey69f+1R4Q8cd45Lod6a4IcJIxnzGc/zA=="],

    "tagged-tag": ["tagged-tag@1.0.0", "", {}, "sha512-yEFYrVhod+hdNyx7g5Bnkkb0G6si8HJurOoOEgC8B/O0uXLHlaey/65KRv6cuWBNhBgHKAROVpc7QyYqE5gFng=="],

    "tapable": ["tapable@2.3.0", "", {}, "sha512-g9ljZiwki/LfxmQADO3dEY1CbpmXT5Hm2fJ+QaGKwSXUylMybePR7/67YW7jOrrvjEgL1Fmz5kzyAjWVWLlucg=="],

    "tar": ["tar@7.5.11", "", { "dependencies": { "@isaacs/fs-minipass": "^4.0.0", "chownr": "^3.0.0", "minipass": "^7.1.2", "minizlib": "^3.1.0", "yallist": "^5.0.0" } }, "sha512-ChjMH33/KetonMTAtpYdgUFr0tbz69Fp2v7zWxQfYZX4g5ZN2nOBXm1R2xyA+lMIKrLKIoKAwFj93jE/avX9cQ=="],

    "tar-stream": ["tar-stream@3.1.8", "", { "dependencies": { "b4a": "^1.6.4", "bare-fs": "^4.5.5", "fast-fifo": "^1.2.0", "streamx": "^2.15.0" } }, "sha512-U6QpVRyCGHva435KoNWy9PRoi2IFYCgtEhq9nmrPPpbRacPs9IH4aJ3gbrFC8dPcXvdSZ4XXfXT5Fshbp2MtlQ=="],

    "teex": ["teex@1.0.1", "", { "dependencies": { "streamx": "^2.12.5" } }, "sha512-eYE6iEI62Ni1H8oIa7KlDU6uQBtqr4Eajni3wX7rpfXD8ysFx8z0+dri+KWEPWpBsxXfxu58x/0jvTVT1ekOSg=="],

    "terser": ["terser@5.46.1", "", { "dependencies": { "@jridgewell/source-map": "^0.3.3", "acorn": "^8.15.0", "commander": "^2.20.0", "source-map-support": "~0.5.20" }, "bin": { "terser": "bin/terser" } }, "sha512-vzCjQO/rgUuK9sf8VJZvjqiqiHFaZLnOiimmUuOKODxWL8mm/xua7viT7aqX7dgPY60otQjUotzFMmCB4VdmqQ=="],

    "text-decoder": ["text-decoder@1.2.7", "", { "dependencies": { "b4a": "^1.6.4" } }, "sha512-vlLytXkeP4xvEq2otHeJfSQIRyWxo/oZGEbXrtEEF9Hnmrdly59sUbzZ/QgyWuLYHctCHxFF4tRQZNQ9k60ExQ=="],

    "tiny-inflate": ["tiny-inflate@1.0.3", "", {}, "sha512-pkY1fj1cKHb2seWDy0B16HeWyczlJA9/WW3u3c4z/NiWDsO3DOU5D7nhTLE9CF0yXv/QZFY7sEJmj24dK+Rrqw=="],

    "tiny-invariant": ["tiny-invariant@1.3.3", "", {}, "sha512-+FbBPE1o9QAYvviau/qC5SE3caw21q3xkvWKBtja5vgqOWIHHJ3ioaq1VPfn/Szqctz2bU/oYeKd9/z5BL+PVg=="],

    "tinyclip": ["tinyclip@0.1.12", "", {}, "sha512-Ae3OVUqifDw0wBriIBS7yVaW44Dp6eSHQcyq4Igc7eN2TJH/2YsicswaW+J/OuMvhpDPOKEgpAZCjkb4hpoyeA=="],

    "tinyexec": ["tinyexec@1.0.4", "", {}, "sha512-u9r3uZC0bdpGOXtlxUIdwf9pkmvhqJdrVCH9fapQtgy/OeTTMZ1nqH7agtvEfmGui6e1XxjcdrlxvxJvc3sMqw=="],

    "tinyglobby": ["tinyglobby@0.2.15", "", { "dependencies": { "fdir": "^6.5.0", "picomatch": "^4.0.3" } }, "sha512-j2Zq4NyQYG5XMST4cbs02Ak8iJUdxRM0XI5QyxXuZOzKOINmWurp3smXu3y5wDcJrptwpSjgXHzIQxR0omXljQ=="],

    "to-regex-range": ["to-regex-range@5.0.1", "", { "dependencies": { "is-number": "^7.0.0" } }, "sha512-65P7iz6X5yEr1cwcgvQxbbIw7Uk3gOy5dIdtZ4rDveLqhrdJP+Li/Hx6tyK0NEb+2GCyneCMJiGqrADCSNk8sQ=="],

    "toidentifier": ["toidentifier@1.0.1", "", {}, "sha512-o5sSPKEkg/DIQNmH43V0/uerLrpzVedkUh8tGNvaeXpfpuwjKenlSox/2O/BTlZUtEe+JG7s5YhEz608PlAHRA=="],

    "totalist": ["totalist@3.0.1", "", {}, "sha512-sf4i37nQ2LBx4m3wB74y+ubopq6W/dIzXg0FDGjsYnZHVa1Da8FH853wlL2gtUhg+xJXjfk3kUZS3BRoQeoQBQ=="],

    "tr46": ["tr46@0.0.3", "", {}, "sha512-N3WMsuqV66lT30CrXNbEjx4GEwlow3v6rr4mCcv6prnfwhS01rkgyFdjPNBYd9br7LpXV1+Emh01fHnq2Gdgrw=="],

    "tree-kill": ["tree-kill@1.2.2", "", { "bin": { "tree-kill": "cli.js" } }, "sha512-L0Orpi8qGpRG//Nd+H90vFB+3iHnue1zSSGmNOOCh1GLJ7rUKVwV2HvijphGQS2UmhUZewS9VgvxYIdgr+fG1A=="],

    "trim-lines": ["trim-lines@3.0.1", "", {}, "sha512-kRj8B+YHZCc9kQYdWfJB2/oUl9rA99qbowYYBtr4ui4mZyAQ2JpvVBd/6U2YloATfqBhBTSMhTpgBHtU0Mf3Rg=="],

    "trough": ["trough@2.2.0", "", {}, "sha512-tmMpK00BjZiUyVyvrBK7knerNgmgvcV/KLVyuma/SC+TQN167GrMRciANTz09+k3zW8L8t60jWO1GpfkZdjTaw=="],

    "tsconfck": ["tsconfck@3.1.6", "", { "peerDependencies": { "typescript": "^5.0.0" }, "optionalPeers": ["typescript"], "bin": { "tsconfck": "bin/tsconfck.js" } }, "sha512-ks6Vjr/jEw0P1gmOVwutM3B7fWxoWBL2KRDb1JfqGVawBmO5UsvmWOQFGHBPl5yxYz4eERr19E6L7NMv+Fej4w=="],

    "tsdown": ["tsdown@0.21.4", "", { "dependencies": { "ansis": "^4.2.0", "cac": "^7.0.0", "defu": "^6.1.4", "empathic": "^2.0.0", "hookable": "^6.1.0", "import-without-cache": "^0.2.5", "obug": "^2.1.1", "picomatch": "^4.0.3", "rolldown": "1.0.0-rc.9", "rolldown-plugin-dts": "^0.22.5", "semver": "^7.7.4", "tinyexec": "^1.0.4", "tinyglobby": "^0.2.15", "tree-kill": "^1.2.2", "unconfig-core": "^7.5.0", "unrun": "^0.2.32" }, "peerDependencies": { "@arethetypeswrong/core": "^0.18.1", "@tsdown/css": "0.21.4", "@tsdown/exe": "0.21.4", "@vitejs/devtools": "*", "publint": "^0.3.0", "typescript": "^5.0.0", "unplugin-unused": "^0.5.0" }, "optionalPeers": ["@arethetypeswrong/core", "@tsdown/css", "@tsdown/exe", "@vitejs/devtools", "publint", "typescript", "unplugin-unused"], "bin": { "tsdown": "dist/run.mjs" } }, "sha512-Q/kBi8SXkr4X6JI/NAZKZY1UuiEcbuXtIskL4tZCsgpDiEPM/2W6lC+OonNA31S+V3KsWedFvbFDBs23hvt+Aw=="],

    "tslib": ["tslib@2.8.1", "", {}, "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w=="],

    "type-fest": ["type-fest@4.41.0", "", {}, "sha512-TeTSQ6H5YHvpqVwBRcnLDCBnDOHWYu7IvGbHT6N8AOymcr9PJGjc1GTtiWZTYg0NCgYwvnYWEkVChQAr9bjfwA=="],

    "type-level-regexp": ["type-level-regexp@0.1.17", "", {}, "sha512-wTk4DH3cxwk196uGLK/E9pE45aLfeKJacKmcEgEOA/q5dnPGNxXt0cfYdFxb57L+sEpf1oJH4Dnx/pnRcku9jg=="],

    "typesafe-path": ["typesafe-path@0.2.2", "", {}, "sha512-OJabfkAg1WLZSqJAJ0Z6Sdt3utnbzr/jh+NAHoyWHJe8CMSy79Gm085094M9nvTPy22KzTVn5Zq5mbapCI/hPA=="],

    "typescript": ["typescript@5.9.3", "", { "bin": { "tsc": "bin/tsc", "tsserver": "bin/tsserver" } }, "sha512-jl1vZzPDinLr9eUt3J/t7V6FgNEw9QjvBPdysz9KfQDD41fQrC2Y4vKQdiaUpFT4bXlb1RHhLpp8wtm6M5TgSw=="],

    "typescript-auto-import-cache": ["typescript-auto-import-cache@0.3.6", "", { "dependencies": { "semver": "^7.3.8" } }, "sha512-RpuHXrknHdVdK7wv/8ug3Fr0WNsNi5l5aB8MYYuXhq2UH5lnEB1htJ1smhtD5VeCsGr2p8mUDtd83LCQDFVgjQ=="],

    "ufo": ["ufo@1.6.3", "", {}, "sha512-yDJTmhydvl5lJzBmy/hyOAA0d+aqCBuwl818haVdYCRrWV84o7YyeVm4QlVHStqNrrJSTb6jKuFAVqAFsr+K3Q=="],

    "ultrahtml": ["ultrahtml@1.6.0", "", {}, "sha512-R9fBn90VTJrqqLDwyMph+HGne8eqY1iPfYhPzZrvKpIfwkWZbcYlfpsb8B9dTvBfpy1/hqAD7Wi8EKfP9e8zdw=="],

    "unconfig-core": ["unconfig-core@7.5.0", "", { "dependencies": { "@quansync/fs": "^1.0.0", "quansync": "^1.0.0" } }, "sha512-Su3FauozOGP44ZmKdHy2oE6LPjk51M/TRRjHv2HNCWiDvfvCoxC2lno6jevMA91MYAdCdwP05QnWdWpSbncX/w=="],

    "uncrypto": ["uncrypto@0.1.3", "", {}, "sha512-Ql87qFHB3s/De2ClA9e0gsnS6zXG27SkTiSJwjCc9MebbfapQfuPzumMIUMi38ezPZVNFcHI9sUIepeQfw8J8Q=="],

    "unctx": ["unctx@2.5.0", "", { "dependencies": { "acorn": "^8.15.0", "estree-walker": "^3.0.3", "magic-string": "^0.30.21", "unplugin": "^2.3.11" } }, "sha512-p+Rz9x0R7X+CYDkT+Xg8/GhpcShTlU8n+cf9OtOEf7zEQsNcCZO1dPKNRDqvUTaq+P32PMMkxWHwfrxkqfqAYg=="],

    "unenv": ["unenv@2.0.0-rc.24", "", { "dependencies": { "pathe": "^2.0.3" } }, "sha512-i7qRCmY42zmCwnYlh9H2SvLEypEFGye5iRmEMKjcGi7zk9UquigRjFtTLz0TYqr0ZGLZhaMHl/foy1bZR+Cwlw=="],

    "unhead": ["unhead@2.1.12", "", { "dependencies": { "hookable": "^6.0.1" } }, "sha512-iTHdWD9ztTunOErtfUFk6Wr11BxvzumcYJ0CzaSCBUOEtg+DUZ9+gnE99i8QkLFT2q1rZD48BYYGXpOZVDLYkA=="],

    "unicorn-magic": ["unicorn-magic@0.3.0", "", {}, "sha512-+QBBXBCvifc56fsbuxZQ6Sic3wqqc3WWaqxs58gvJrcOuN83HGTCwz3oS5phzU9LthRNE9VrJCFCLUgHeeFnfA=="],

    "unified": ["unified@11.0.5", "", { "dependencies": { "@types/unist": "^3.0.0", "bail": "^2.0.0", "devlop": "^1.0.0", "extend": "^3.0.0", "is-plain-obj": "^4.0.0", "trough": "^2.0.0", "vfile": "^6.0.0" } }, "sha512-xKvGhPWw3k84Qjh8bI3ZeJjqnyadK+GEFtazSfZv/rKeTkTjOJho6mFqh2SM96iIcZokxiOpg78GazTSg8+KHA=="],

    "unifont": ["unifont@0.7.4", "", { "dependencies": { "css-tree": "^3.1.0", "ofetch": "^1.5.1", "ohash": "^2.0.11" } }, "sha512-oHeis4/xl42HUIeHuNZRGEvxj5AaIKR+bHPNegRq5LV1gdc3jundpONbjglKpihmJf+dswygdMJn3eftGIMemg=="],

    "unimport": ["unimport@6.0.2", "", { "dependencies": { "acorn": "^8.16.0", "escape-string-regexp": "^5.0.0", "estree-walker": "^3.0.3", "local-pkg": "^1.1.2", "magic-string": "^0.30.21", "mlly": "^1.8.1", "pathe": "^2.0.3", "picomatch": "^4.0.3", "pkg-types": "^2.3.0", "scule": "^1.3.0", "strip-literal": "^3.1.0", "tinyglobby": "^0.2.15", "unplugin": "^3.0.0", "unplugin-utils": "^0.3.1" } }, "sha512-ZSOkrDw380w+KIPniY3smyXh2h7H9v2MNr9zejDuh239o5sdea44DRAYrv+rfUi2QGT186P2h0GPGKvy8avQ5g=="],

    "unist-util-find-after": ["unist-util-find-after@5.0.0", "", { "dependencies": { "@types/unist": "^3.0.0", "unist-util-is": "^6.0.0" } }, "sha512-amQa0Ep2m6hE2g72AugUItjbuM8X8cGQnFoHk0pGfrFeT9GZhzN5SW8nRsiGKK7Aif4CrACPENkA6P/Lw6fHGQ=="],

    "unist-util-is": ["unist-util-is@6.0.1", "", { "dependencies": { "@types/unist": "^3.0.0" } }, "sha512-LsiILbtBETkDz8I9p1dQ0uyRUWuaQzd/cuEeS1hoRSyW5E5XGmTzlwY1OrNzzakGowI9Dr/I8HVaw4hTtnxy8g=="],

    "unist-util-modify-children": ["unist-util-modify-children@4.0.0", "", { "dependencies": { "@types/unist": "^3.0.0", "array-iterate": "^2.0.0" } }, "sha512-+tdN5fGNddvsQdIzUF3Xx82CU9sMM+fA0dLgR9vOmT0oPT2jH+P1nd5lSqfCfXAw+93NhcXNY2qqvTUtE4cQkw=="],

    "unist-util-position": ["unist-util-position@5.0.0", "", { "dependencies": { "@types/unist": "^3.0.0" } }, "sha512-fucsC7HjXvkB5R3kTCO7kUjRdrS0BJt3M/FPxmHMBOm8JQi2BsHAHFsy27E0EolP8rp0NzXsJ+jNPyDWvOJZPA=="],

    "unist-util-remove-position": ["unist-util-remove-position@5.0.0", "", { "dependencies": { "@types/unist": "^3.0.0", "unist-util-visit": "^5.0.0" } }, "sha512-Hp5Kh3wLxv0PHj9m2yZhhLt58KzPtEYKQQ4yxfYFEO7EvHwzyDYnduhHnY1mDxoqr7VUwVuHXk9RXKIiYS1N8Q=="],

    "unist-util-stringify-position": ["unist-util-stringify-position@4.0.0", "", { "dependencies": { "@types/unist": "^3.0.0" } }, "sha512-0ASV06AAoKCDkS2+xw5RXJywruurpbC4JZSm7nr7MOt1ojAzvyyaO+UxZf18j8FCF6kmzCZKcAgN/yu2gm2XgQ=="],

    "unist-util-visit": ["unist-util-visit@5.1.0", "", { "dependencies": { "@types/unist": "^3.0.0", "unist-util-is": "^6.0.0", "unist-util-visit-parents": "^6.0.0" } }, "sha512-m+vIdyeCOpdr/QeQCu2EzxX/ohgS8KbnPDgFni4dQsfSCtpz8UqDyY5GjRru8PDKuYn7Fq19j1CQ+nJSsGKOzg=="],

    "unist-util-visit-children": ["unist-util-visit-children@3.0.0", "", { "dependencies": { "@types/unist": "^3.0.0" } }, "sha512-RgmdTfSBOg04sdPcpTSD1jzoNBjt9a80/ZCzp5cI9n1qPzLZWF9YdvWGN2zmTumP1HWhXKdUWexjy/Wy/lJ7tA=="],

    "unist-util-visit-parents": ["unist-util-visit-parents@6.0.2", "", { "dependencies": { "@types/unist": "^3.0.0", "unist-util-is": "^6.0.0" } }, "sha512-goh1s1TBrqSqukSc8wrjwWhL0hiJxgA8m4kFxGlQ+8FYQ3C/m11FcTs4YYem7V664AhHVvgoQLk890Ssdsr2IQ=="],

    "universalify": ["universalify@2.0.1", "", {}, "sha512-gptHNQghINnc/vTGIk0SOFGFNXw7JVrlRUtConJRlvaw6DuX0wO5Jeko9sWrMBhh+PsYAZ7oXAiOnf/UKogyiw=="],

    "unplugin": ["unplugin@3.0.0", "", { "dependencies": { "@jridgewell/remapping": "^2.3.5", "picomatch": "^4.0.3", "webpack-virtual-modules": "^0.6.2" } }, "sha512-0Mqk3AT2TZCXWKdcoaufeXNukv2mTrEZExeXlHIOZXdqYoHHr4n51pymnwV8x2BOVxwXbK2HLlI7usrqMpycdg=="],

    "unplugin-utils": ["unplugin-utils@0.3.1", "", { "dependencies": { "pathe": "^2.0.3", "picomatch": "^4.0.3" } }, "sha512-5lWVjgi6vuHhJ526bI4nlCOmkCIF3nnfXkCMDeMJrtdvxTs6ZFCM8oNufGTsDbKv/tJ/xj8RpvXjRuPBZJuJog=="],

    "unplugin-vue-router": ["unplugin-vue-router@0.19.2", "", { "dependencies": { "@babel/generator": "^7.28.5", "@vue-macros/common": "^3.1.1", "@vue/language-core": "^3.2.1", "ast-walker-scope": "^0.8.3", "chokidar": "^5.0.0", "json5": "^2.2.3", "local-pkg": "^1.1.2", "magic-string": "^0.30.21", "mlly": "^1.8.0", "muggle-string": "^0.4.1", "pathe": "^2.0.3", "picomatch": "^4.0.3", "scule": "^1.3.0", "tinyglobby": "^0.2.15", "unplugin": "^2.3.11", "unplugin-utils": "^0.3.1", "yaml": "^2.8.2" }, "peerDependencies": { "@vue/compiler-sfc": "^3.5.17", "vue-router": "^4.6.0" }, "optionalPeers": ["vue-router"] }, "sha512-u5dgLBarxE5cyDK/hzJGfpCTLIAyiTXGlo85COuD4Nssj6G7NxS+i9mhCWz/1p/ud1eMwdcUbTXehQe41jYZUA=="],

    "unrun": ["unrun@0.2.32", "", { "dependencies": { "rolldown": "1.0.0-rc.9" }, "peerDependencies": { "synckit": "^0.11.11" }, "optionalPeers": ["synckit"], "bin": { "unrun": "dist/cli.mjs" } }, "sha512-opd3z6791rf281JdByf0RdRQrpcc7WyzqittqIXodM/5meNWdTwrVxeyzbaCp4/Rgls/um14oUaif1gomO8YGg=="],

    "unstorage": ["unstorage@1.17.4", "", { "dependencies": { "anymatch": "^3.1.3", "chokidar": "^5.0.0", "destr": "^2.0.5", "h3": "^1.15.5", "lru-cache": "^11.2.0", "node-fetch-native": "^1.6.7", "ofetch": "^1.5.1", "ufo": "^1.6.3" }, "peerDependencies": { "@azure/app-configuration": "^1.8.0", "@azure/cosmos": "^4.2.0", "@azure/data-tables": "^13.3.0", "@azure/identity": "^4.6.0", "@azure/keyvault-secrets": "^4.9.0", "@azure/storage-blob": "^12.26.0", "@capacitor/preferences": "^6 || ^7 || ^8", "@deno/kv": ">=0.9.0", "@netlify/blobs": "^6.5.0 || ^7.0.0 || ^8.1.0 || ^9.0.0 || ^10.0.0", "@planetscale/database": "^1.19.0", "@upstash/redis": "^1.34.3", "@vercel/blob": ">=0.27.1", "@vercel/functions": "^2.2.12 || ^3.0.0", "@vercel/kv": "^1 || ^2 || ^3", "aws4fetch": "^1.0.20", "db0": ">=0.2.1", "idb-keyval": "^6.2.1", "ioredis": "^5.4.2", "uploadthing": "^7.4.4" }, "optionalPeers": ["@azure/app-configuration", "@azure/cosmos", "@azure/data-tables", "@azure/identity", "@azure/keyvault-secrets", "@azure/storage-blob", "@capacitor/preferences", "@deno/kv", "@netlify/blobs", "@planetscale/database", "@upstash/redis", "@vercel/blob", "@vercel/functions", "@vercel/kv", "aws4fetch", "db0", "idb-keyval", "ioredis", "uploadthing"] }, "sha512-fHK0yNg38tBiJKp/Vgsq4j0JEsCmgqH58HAn707S7zGkArbZsVr/CwINoi+nh3h98BRCwKvx1K3Xg9u3VV83sw=="],

    "untun": ["untun@0.1.3", "", { "dependencies": { "citty": "^0.1.5", "consola": "^3.2.3", "pathe": "^1.1.1" }, "bin": { "untun": "bin/untun.mjs" } }, "sha512-4luGP9LMYszMRZwsvyUd9MrxgEGZdZuZgpVQHEEX0lCYFESasVRvZd0EYpCkOIbJKHMuv0LskpXc/8Un+MJzEQ=="],

    "untyped": ["untyped@2.0.0", "", { "dependencies": { "citty": "^0.1.6", "defu": "^6.1.4", "jiti": "^2.4.2", "knitwork": "^1.2.0", "scule": "^1.3.0" }, "bin": { "untyped": "dist/cli.mjs" } }, "sha512-nwNCjxJTjNuLCgFr42fEak5OcLuB3ecca+9ksPFNvtfYSLpjf+iJqSIaSnIile6ZPbKYxI5k2AfXqeopGudK/g=="],

    "unwasm": ["unwasm@0.5.3", "", { "dependencies": { "exsolve": "^1.0.8", "knitwork": "^1.3.0", "magic-string": "^0.30.21", "mlly": "^1.8.0", "pathe": "^2.0.3", "pkg-types": "^2.3.0" } }, "sha512-keBgTSfp3r6+s9ZcSma+0chwxQdmLbB5+dAD9vjtB21UTMYuKAxHXCU1K2CbCtnP09EaWeRvACnXk0EJtUx+hw=="],

    "update-browserslist-db": ["update-browserslist-db@1.2.3", "", { "dependencies": { "escalade": "^3.2.0", "picocolors": "^1.1.1" }, "peerDependencies": { "browserslist": ">= 4.21.0" }, "bin": { "update-browserslist-db": "cli.js" } }, "sha512-Js0m9cx+qOgDxo0eMiFGEueWztz+d4+M3rGlmKPT+T4IS/jP4ylw3Nwpu6cpTTP8R1MAC1kF4VbdLt3ARf209w=="],

    "uqr": ["uqr@0.1.2", "", {}, "sha512-MJu7ypHq6QasgF5YRTjqscSzQp/W11zoUk6kvmlH+fmWEs63Y0Eib13hYFwAzagRJcVY8WVnlV+eBDUGMJ5IbA=="],

    "util-deprecate": ["util-deprecate@1.0.2", "", {}, "sha512-EPD5q1uXyFxJpCrLnCc1nHnq3gOa6DZBocAIiI2TaSCA7VCJ1UJDMagCzIkXNsUYfD1daK//LTEQ8xiIbrHtcw=="],

    "vfile": ["vfile@6.0.3", "", { "dependencies": { "@types/unist": "^3.0.0", "vfile-message": "^4.0.0" } }, "sha512-KzIbH/9tXat2u30jf+smMwFCsno4wHVdNmzFyL+T/L3UGqqk6JKfVqOFOZEpZSHADH1k40ab6NUIXZq422ov3Q=="],

    "vfile-location": ["vfile-location@5.0.3", "", { "dependencies": { "@types/unist": "^3.0.0", "vfile": "^6.0.0" } }, "sha512-5yXvWDEgqeiYiBe1lbxYF7UMAIm/IcopxMHrMQDq3nvKcjPKIhZklUKL+AE7J7uApI4kwe2snsK+eI6UTj9EHg=="],

    "vfile-message": ["vfile-message@4.0.3", "", { "dependencies": { "@types/unist": "^3.0.0", "unist-util-stringify-position": "^4.0.0" } }, "sha512-QTHzsGd1EhbZs4AsQ20JX1rC3cOlt/IWJruk893DfLRr57lcnOeMaWG4K0JrRta4mIJZKth2Au3mM3u03/JWKw=="],

    "vite": ["vite@6.4.1", "", { "dependencies": { "esbuild": "^0.25.0", "fdir": "^6.4.4", "picomatch": "^4.0.2", "postcss": "^8.5.3", "rollup": "^4.34.9", "tinyglobby": "^0.2.13" }, "optionalDependencies": { "fsevents": "~2.3.3" }, "peerDependencies": { "@types/node": "^18.0.0 || ^20.0.0 || >=22.0.0", "jiti": ">=1.21.0", "less": "*", "lightningcss": "^1.21.0", "sass": "*", "sass-embedded": "*", "stylus": "*", "sugarss": "*", "terser": "^5.16.0", "tsx": "^4.8.1", "yaml": "^2.4.2" }, "optionalPeers": ["@types/node", "jiti", "less", "lightningcss", "sass", "sass-embedded", "stylus", "sugarss", "terser", "tsx", "yaml"], "bin": { "vite": "bin/vite.js" } }, "sha512-+Oxm7q9hDoLMyJOYfUYBuHQo+dkAloi33apOPP56pzj+vsdJDzr+j1NISE5pyaAuKL4A3UD34qd0lx5+kfKp2g=="],

    "vite-dev-rpc": ["vite-dev-rpc@1.1.0", "", { "dependencies": { "birpc": "^2.4.0", "vite-hot-client": "^2.1.0" }, "peerDependencies": { "vite": "^2.9.0 || ^3.0.0-0 || ^4.0.0-0 || ^5.0.0-0 || ^6.0.1 || ^7.0.0-0" } }, "sha512-pKXZlgoXGoE8sEKiKJSng4hI1sQ4wi5YT24FCrwrLt6opmkjlqPPVmiPWWJn8M8byMxRGzp1CrFuqQs4M/Z39A=="],

    "vite-hot-client": ["vite-hot-client@2.1.0", "", { "peerDependencies": { "vite": "^2.6.0 || ^3.0.0 || ^4.0.0 || ^5.0.0-0 || ^6.0.0-0 || ^7.0.0-0" } }, "sha512-7SpgZmU7R+dDnSmvXE1mfDtnHLHQSisdySVR7lO8ceAXvM0otZeuQQ6C8LrS5d/aYyP/QZ0hI0L+dIPrm4YlFQ=="],

    "vite-node": ["vite-node@5.3.0", "", { "dependencies": { "cac": "^6.7.14", "es-module-lexer": "^2.0.0", "obug": "^2.1.1", "pathe": "^2.0.3", "vite": "^7.3.1" }, "bin": { "vite-node": "dist/cli.mjs" } }, "sha512-8f20COPYJujc3OKPX6OuyBy3ZIv2det4eRRU4GY1y2MjbeGSUmPjedxg1b72KnTagCofwvZ65ThzjxDW2AtQFQ=="],

    "vite-plugin-checker": ["vite-plugin-checker@0.12.0", "", { "dependencies": { "@babel/code-frame": "^7.27.1", "chokidar": "^4.0.3", "npm-run-path": "^6.0.0", "picocolors": "^1.1.1", "picomatch": "^4.0.3", "tiny-invariant": "^1.3.3", "tinyglobby": "^0.2.15", "vscode-uri": "^3.1.0" }, "peerDependencies": { "@biomejs/biome": ">=1.7", "eslint": ">=9.39.1", "meow": "^13.2.0", "optionator": "^0.9.4", "oxlint": ">=1", "stylelint": ">=16", "typescript": "*", "vite": ">=5.4.21", "vls": "*", "vti": "*", "vue-tsc": "~2.2.10 || ^3.0.0" }, "optionalPeers": ["@biomejs/biome", "eslint", "meow", "optionator", "oxlint", "stylelint", "typescript", "vls", "vti", "vue-tsc"] }, "sha512-CmdZdDOGss7kdQwv73UyVgLPv0FVYe5czAgnmRX2oKljgEvSrODGuClaV3PDR2+3ou7N/OKGauDDBjy2MB07Rg=="],

    "vite-plugin-inspect": ["vite-plugin-inspect@0.8.9", "", { "dependencies": { "@antfu/utils": "^0.7.10", "@rollup/pluginutils": "^5.1.3", "debug": "^4.3.7", "error-stack-parser-es": "^0.1.5", "fs-extra": "^11.2.0", "open": "^10.1.0", "perfect-debounce": "^1.0.0", "picocolors": "^1.1.1", "sirv": "^3.0.0" }, "peerDependencies": { "vite": "^3.1.0 || ^4.0.0 || ^5.0.0-0 || ^6.0.1" } }, "sha512-22/8qn+LYonzibb1VeFZmISdVao5kC22jmEKm24vfFE8siEn47EpVcCLYMv6iKOYMJfjSvSJfueOwcFCkUnV3A=="],

    "vite-plugin-vue-devtools": ["vite-plugin-vue-devtools@7.7.9", "", { "dependencies": { "@vue/devtools-core": "^7.7.9", "@vue/devtools-kit": "^7.7.9", "@vue/devtools-shared": "^7.7.9", "execa": "^9.5.2", "sirv": "^3.0.1", "vite-plugin-inspect": "0.8.9", "vite-plugin-vue-inspector": "^5.3.1" }, "peerDependencies": { "vite": "^3.1.0 || ^4.0.0-0 || ^5.0.0-0 || ^6.0.0-0 || ^7.0.0-0" } }, "sha512-08DvePf663SxqLFJeMVNW537zzVyakp9KIrI2K7lwgaTqA5R/ydN/N2K8dgZO34tg/Qmw0ch84fOKoBtCEdcGg=="],

    "vite-plugin-vue-inspector": ["vite-plugin-vue-inspector@5.4.0", "", { "dependencies": { "@babel/core": "^7.23.0", "@babel/plugin-proposal-decorators": "^7.23.0", "@babel/plugin-syntax-import-attributes": "^7.22.5", "@babel/plugin-syntax-import-meta": "^7.10.4", "@babel/plugin-transform-typescript": "^7.22.15", "@vue/babel-plugin-jsx": "^1.1.5", "@vue/compiler-dom": "^3.3.4", "kolorist": "^1.8.0", "magic-string": "^0.30.4" }, "peerDependencies": { "vite": "^3.0.0 || ^4.0.0 || ^5.0.0 || ^6.0.0 || ^7.0.0 || ^8.0.0" } }, "sha512-Iq/024CydcE46FZqWPU4t4lw4uYOdLnFSO1RNxJVt2qY9zxIjmnkBqhHnYaReWM82kmNnaXs7OkfgRrV2GEjyw=="],

    "vite-plugin-vue-tracer": ["vite-plugin-vue-tracer@1.3.0", "", { "dependencies": { "estree-walker": "^3.0.3", "exsolve": "^1.0.8", "magic-string": "^0.30.21", "pathe": "^2.0.3", "source-map-js": "^1.2.1" }, "peerDependencies": { "vite": "^6.0.0 || ^7.0.0", "vue": "^3.5.0" } }, "sha512-Cgfce6VikzOw5MUJTpeg50s5rRjzU1Vr61ZjuHunVVHLjZZ5AUlgyExHthZ3r59vtoz9W2rDt23FYG81avYBKw=="],

    "vitefu": ["vitefu@1.1.2", "", { "peerDependencies": { "vite": "^3.0.0 || ^4.0.0 || ^5.0.0 || ^6.0.0 || ^7.0.0 || ^8.0.0-beta.0" }, "optionalPeers": ["vite"] }, "sha512-zpKATdUbzbsycPFBN71nS2uzBUQiVnFoOrr2rvqv34S1lcAgMKKkjWleLGeiJlZ8lwCXvtWaRn7R3ZC16SYRuw=="],

    "volar-service-css": ["volar-service-css@0.0.70", "", { "dependencies": { "vscode-css-languageservice": "^6.3.0", "vscode-languageserver-textdocument": "^1.0.11", "vscode-uri": "^3.0.8" }, "peerDependencies": { "@volar/language-service": "~2.4.0" }, "optionalPeers": ["@volar/language-service"] }, "sha512-K1qyOvBpE3rzdAv3e4/6Rv5yizrYPy5R/ne3IWCAzLBuMO4qBMV3kSqWzj6KUVe6S0AnN6wxF7cRkiaKfYMYJw=="],

    "volar-service-emmet": ["volar-service-emmet@0.0.70", "", { "dependencies": { "@emmetio/css-parser": "^0.4.1", "@emmetio/html-matcher": "^1.3.0", "@vscode/emmet-helper": "^2.9.3", "vscode-uri": "^3.0.8" }, "peerDependencies": { "@volar/language-service": "~2.4.0" }, "optionalPeers": ["@volar/language-service"] }, "sha512-xi5bC4m/VyE3zy/n2CXspKeDZs3qA41tHLTw275/7dNWM/RqE2z3BnDICQybHIVp/6G1iOQj5c1qXMgQC08TNg=="],

    "volar-service-html": ["volar-service-html@0.0.70", "", { "dependencies": { "vscode-html-languageservice": "^5.3.0", "vscode-languageserver-textdocument": "^1.0.11", "vscode-uri": "^3.0.8" }, "peerDependencies": { "@volar/language-service": "~2.4.0" }, "optionalPeers": ["@volar/language-service"] }, "sha512-eR6vCgMdmYAo4n+gcT7DSyBQbwB8S3HZZvSagTf0sxNaD4WppMCFfpqWnkrlGStPKMZvMiejRRVmqsX9dYcTvQ=="],

    "volar-service-prettier": ["volar-service-prettier@0.0.70", "", { "dependencies": { "vscode-uri": "^3.0.8" }, "peerDependencies": { "@volar/language-service": "~2.4.0", "prettier": "^2.2 || ^3.0" }, "optionalPeers": ["@volar/language-service", "prettier"] }, "sha512-Z6BCFSpGVCd8BPAsZ785Kce1BGlWd5ODqmqZGVuB14MJvrR4+CYz6cDy4F+igmE1gMifqfvMhdgT8Aud4M5ngg=="],

    "volar-service-typescript": ["volar-service-typescript@0.0.70", "", { "dependencies": { "path-browserify": "^1.0.1", "semver": "^7.6.2", "typescript-auto-import-cache": "^0.3.5", "vscode-languageserver-textdocument": "^1.0.11", "vscode-nls": "^5.2.0", "vscode-uri": "^3.0.8" }, "peerDependencies": { "@volar/language-service": "~2.4.0" }, "optionalPeers": ["@volar/language-service"] }, "sha512-l46Bx4cokkUedTd74ojO5H/zqHZJ8SUuyZ0IB8JN4jfRqUM3bQFBHoOwlZCyZmOeO0A3RQNkMnFclxO4c++gsg=="],

    "volar-service-typescript-twoslash-queries": ["volar-service-typescript-twoslash-queries@0.0.70", "", { "dependencies": { "vscode-uri": "^3.0.8" }, "peerDependencies": { "@volar/language-service": "~2.4.0" }, "optionalPeers": ["@volar/language-service"] }, "sha512-IdD13Z9N2Bu8EM6CM0fDV1E69olEYGHDU25X51YXmq8Y0CmJ2LNj6gOiBJgpS5JGUqFzECVhMNBW7R0sPdRTMQ=="],

    "volar-service-yaml": ["volar-service-yaml@0.0.70", "", { "dependencies": { "vscode-uri": "^3.0.8", "yaml-language-server": "~1.20.0" }, "peerDependencies": { "@volar/language-service": "~2.4.0" }, "optionalPeers": ["@volar/language-service"] }, "sha512-0c8bXDBeoATF9F6iPIlOuYTuZAC4c+yi0siQo920u7eiBJk8oQmUmg9cDUbR4+Gl++bvGP4plj3fErbJuPqdcQ=="],

    "vscode-css-languageservice": ["vscode-css-languageservice@6.3.10", "", { "dependencies": { "@vscode/l10n": "^0.0.18", "vscode-languageserver-textdocument": "^1.0.12", "vscode-languageserver-types": "3.17.5", "vscode-uri": "^3.1.0" } }, "sha512-eq5N9Er3fC4vA9zd9EFhyBG90wtCCuXgRSpAndaOgXMh1Wgep5lBgRIeDgjZBW9pa+332yC9+49cZMW8jcL3MA=="],

    "vscode-html-languageservice": ["vscode-html-languageservice@5.6.2", "", { "dependencies": { "@vscode/l10n": "^0.0.18", "vscode-languageserver-textdocument": "^1.0.12", "vscode-languageserver-types": "^3.17.5", "vscode-uri": "^3.1.0" } }, "sha512-ulCrSnFnfQ16YzvwnYUgEbUEl/ZG7u2eV27YhvLObSHKkb8fw1Z9cgsnUwjTEeDIdJDoTDTDpxuhQwoenoLNMg=="],

    "vscode-json-languageservice": ["vscode-json-languageservice@4.1.8", "", { "dependencies": { "jsonc-parser": "^3.0.0", "vscode-languageserver-textdocument": "^1.0.1", "vscode-languageserver-types": "^3.16.0", "vscode-nls": "^5.0.0", "vscode-uri": "^3.0.2" } }, "sha512-0vSpg6Xd9hfV+eZAaYN63xVVMOTmJ4GgHxXnkLCh+9RsQBkWKIghzLhW2B9ebfG+LQQg8uLtsQ2aUKjTgE+QOg=="],

    "vscode-jsonrpc": ["vscode-jsonrpc@8.2.0", "", {}, "sha512-C+r0eKJUIfiDIfwJhria30+TYWPtuHJXHtI7J0YlOmKAo7ogxP20T0zxB7HZQIFhIyvoBPwWskjxrvAtfjyZfA=="],

    "vscode-languageserver": ["vscode-languageserver@9.0.1", "", { "dependencies": { "vscode-languageserver-protocol": "3.17.5" }, "bin": { "installServerIntoExtension": "bin/installServerIntoExtension" } }, "sha512-woByF3PDpkHFUreUa7Hos7+pUWdeWMXRd26+ZX2A8cFx6v/JPTtd4/uN0/jB6XQHYaOlHbio03NTHCqrgG5n7g=="],

    "vscode-languageserver-protocol": ["vscode-languageserver-protocol@3.17.5", "", { "dependencies": { "vscode-jsonrpc": "8.2.0", "vscode-languageserver-types": "3.17.5" } }, "sha512-mb1bvRJN8SVznADSGWM9u/b07H7Ecg0I3OgXDuLdn307rl/J3A9YD6/eYOssqhecL27hK1IPZAsaqh00i/Jljg=="],

    "vscode-languageserver-textdocument": ["vscode-languageserver-textdocument@1.0.12", "", {}, "sha512-cxWNPesCnQCcMPeenjKKsOCKQZ/L6Tv19DTRIGuLWe32lyzWhihGVJ/rcckZXJxfdKCFvRLS3fpBIsV/ZGX4zA=="],

    "vscode-languageserver-types": ["vscode-languageserver-types@3.17.5", "", {}, "sha512-Ld1VelNuX9pdF39h2Hgaeb5hEZM2Z3jUrrMgWQAu82jMtZp7p3vJT3BzToKtZI7NgQssZje5o0zryOrhQvzQAg=="],

    "vscode-nls": ["vscode-nls@5.2.0", "", {}, "sha512-RAaHx7B14ZU04EU31pT+rKz2/zSl7xMsfIZuo8pd+KZO6PXtQmpevpq3vxvWNcrGbdmhM/rr5Uw5Mz+NBfhVng=="],

    "vscode-uri": ["vscode-uri@3.1.0", "", {}, "sha512-/BpdSx+yCQGnCvecbyXdxHDkuk55/G3xwnC0GqY4gmQ3j+A+g8kzzgB4Nk/SINjqn6+waqw3EgbVF2QKExkRxQ=="],

    "vue": ["vue@3.5.30", "", { "dependencies": { "@vue/compiler-dom": "3.5.30", "@vue/compiler-sfc": "3.5.30", "@vue/runtime-dom": "3.5.30", "@vue/server-renderer": "3.5.30", "@vue/shared": "3.5.30" }, "peerDependencies": { "typescript": "*" }, "optionalPeers": ["typescript"] }, "sha512-hTHLc6VNZyzzEH/l7PFGjpcTvUgiaPK5mdLkbjrTeWSRcEfxFrv56g/XckIYlE9ckuobsdwqd5mk2g1sBkMewg=="],

    "vue-bundle-renderer": ["vue-bundle-renderer@2.2.0", "", { "dependencies": { "ufo": "^1.6.1" } }, "sha512-sz/0WEdYH1KfaOm0XaBmRZOWgYTEvUDt6yPYaUzl4E52qzgWLlknaPPTTZmp6benaPTlQAI/hN1x3tAzZygycg=="],

    "vue-devtools-stub": ["vue-devtools-stub@0.1.0", "", {}, "sha512-RutnB7X8c5hjq39NceArgXg28WZtZpGc3+J16ljMiYnFhKvd8hITxSWQSQ5bvldxMDU6gG5mkxl1MTQLXckVSQ=="],

    "vue-router": ["vue-router@5.0.3", "", { "dependencies": { "@babel/generator": "^7.28.6", "@vue-macros/common": "^3.1.1", "@vue/devtools-api": "^8.0.6", "ast-walker-scope": "^0.8.3", "chokidar": "^5.0.0", "json5": "^2.2.3", "local-pkg": "^1.1.2", "magic-string": "^0.30.21", "mlly": "^1.8.0", "muggle-string": "^0.4.1", "pathe": "^2.0.3", "picomatch": "^4.0.3", "scule": "^1.3.0", "tinyglobby": "^0.2.15", "unplugin": "^3.0.0", "unplugin-utils": "^0.3.1", "yaml": "^2.8.2" }, "peerDependencies": { "@pinia/colada": ">=0.21.2", "@vue/compiler-sfc": "^3.5.17", "pinia": "^3.0.4", "vue": "^3.5.0" }, "optionalPeers": ["@pinia/colada", "@vue/compiler-sfc", "pinia"] }, "sha512-nG1c7aAFac7NYj8Hluo68WyWfc41xkEjaR0ViLHCa3oDvTQ/nIuLJlXJX1NUPw/DXzx/8+OKMng045HHQKQKWw=="],

    "web-namespaces": ["web-namespaces@2.0.1", "", {}, "sha512-bKr1DkiNa2krS7qxNtdrtHAmzuYGFQLiQ13TsorsdT6ULTkPLKuu5+GsFpDlg6JFjUTwX2DyhMPG2be8uPrqsQ=="],

    "webidl-conversions": ["webidl-conversions@3.0.1", "", {}, "sha512-2JAn3z8AR6rjK8Sm8orRC0h/bcl/DqL7tRPdGZ4I1CjdF+EaMLmYxBHyXuKL849eucPFhvBoxMsflfOb8kxaeQ=="],

    "webpack-virtual-modules": ["webpack-virtual-modules@0.6.2", "", {}, "sha512-66/V2i5hQanC51vBQKPH4aI8NMAcBW59FVBs+rC7eGHupMyfn34q7rZIE+ETlJ+XTevqfUhVVBgSUNSW2flEUQ=="],

    "whatwg-url": ["whatwg-url@5.0.0", "", { "dependencies": { "tr46": "~0.0.3", "webidl-conversions": "^3.0.0" } }, "sha512-saE57nupxk6v3HY35+jzBwYa0rKSy0XR8JSxZPwgLr7ys0IBzhGviA1/TUGJLmSVqs8pb9AnvICXEuOHLprYTw=="],

    "which": ["which@6.0.1", "", { "dependencies": { "isexe": "^4.0.0" }, "bin": { "node-which": "bin/which.js" } }, "sha512-oGLe46MIrCRqX7ytPUf66EAYvdeMIZYn3WaocqqKZAxrBpkqHfL/qvTyJ/bTk5+AqHCjXmrv3CEWgy368zhRUg=="],

    "which-pm-runs": ["which-pm-runs@1.1.0", "", {}, "sha512-n1brCuqClxfFfq/Rb0ICg9giSZqCS+pLtccdag6C2HyufBrh3fBOiy9nb6ggRMvWOVH5GrdJskj5iGTZNxd7SA=="],

    "widest-line": ["widest-line@5.0.0", "", { "dependencies": { "string-width": "^7.0.0" } }, "sha512-c9bZp7b5YtRj2wOe6dlj32MK+Bx/M/d+9VB2SHM1OtsUHR0aV0tdP6DWh/iMt0kWi1t5g1Iudu6hQRNd1A4PVA=="],

    "wrap-ansi": ["wrap-ansi@9.0.2", "", { "dependencies": { "ansi-styles": "^6.2.1", "string-width": "^7.0.0", "strip-ansi": "^7.1.0" } }, "sha512-42AtmgqjV+X1VpdOfyTGOYRi0/zsoLqtXQckTmqTeybT+BDIbM/Guxo7x3pE2vtpr1ok6xRqM9OpBe+Jyoqyww=="],

    "wrap-ansi-cjs": ["wrap-ansi@7.0.0", "", { "dependencies": { "ansi-styles": "^4.0.0", "string-width": "^4.1.0", "strip-ansi": "^6.0.0" } }, "sha512-YVGIj2kamLSTxw6NsZjoBxfSwsn0ycdesmc4p+Q21c5zPuZ1pl+NfxVdxPtdHvmNVOQ6XSYG4AUtyt/Fi7D16Q=="],

    "ws": ["ws@8.19.0", "", { "peerDependencies": { "bufferutil": "^4.0.1", "utf-8-validate": ">=5.0.2" }, "optionalPeers": ["bufferutil", "utf-8-validate"] }, "sha512-blAT2mjOEIi0ZzruJfIhb3nps74PRWTCz1IjglWEEpQl5XS/UNama6u2/rjFkDDouqr4L67ry+1aGIALViWjDg=="],

    "wsl-utils": ["wsl-utils@0.1.0", "", { "dependencies": { "is-wsl": "^3.1.0" } }, "sha512-h3Fbisa2nKGPxCpm89Hk33lBLsnaGBvctQopaBSOW/uIs6FTe1ATyAnKFJrzVs9vpGdsTe73WF3V4lIsk4Gacw=="],

    "xxhash-wasm": ["xxhash-wasm@1.1.0", "", {}, "sha512-147y/6YNh+tlp6nd/2pWq38i9h6mz/EuQ6njIrmW8D1BS5nCqs0P6DG+m6zTGnNz5I+uhZ0SHxBs9BsPrwcKDA=="],

    "y18n": ["y18n@5.0.8", "", {}, "sha512-0pfFzegeDWJHJIAmTLRP2DwHjdF5s7jo9tuztdQxAhINCdvS+3nGINqPd00AphqJR/0LhANUS6/+7SCb98YOfA=="],

    "yallist": ["yallist@3.1.1", "", {}, "sha512-a4UGQaWPH59mOXUYnAG2ewncQS4i4F43Tv3JoAM+s2VDAmS9NsK8GpDMLrCHPksFT7h3K6TOoUNn2pb7RoXx4g=="],

    "yaml": ["yaml@2.8.2", "", { "bin": { "yaml": "bin.mjs" } }, "sha512-mplynKqc1C2hTVYxd0PU2xQAc22TI1vShAYGksCCfxbn/dFwnHTNi1bvYsBTkhdUNtGIf5xNOg938rrSSYvS9A=="],

    "yaml-language-server": ["yaml-language-server@1.20.0", "", { "dependencies": { "@vscode/l10n": "^0.0.18", "ajv": "^8.17.1", "ajv-draft-04": "^1.0.0", "prettier": "^3.5.0", "request-light": "^0.5.7", "vscode-json-languageservice": "4.1.8", "vscode-languageserver": "^9.0.0", "vscode-languageserver-textdocument": "^1.0.1", "vscode-languageserver-types": "^3.16.0", "vscode-uri": "^3.0.2", "yaml": "2.7.1" }, "bin": { "yaml-language-server": "bin/yaml-language-server" } }, "sha512-qhjK/bzSRZ6HtTvgeFvjNPJGWdZ0+x5NREV/9XZWFjIGezew2b4r5JPy66IfOhd5OA7KeFwk1JfmEbnTvev0cA=="],

    "yargs": ["yargs@17.7.2", "", { "dependencies": { "cliui": "^8.0.1", "escalade": "^3.1.1", "get-caller-file": "^2.0.5", "require-directory": "^2.1.1", "string-width": "^4.2.3", "y18n": "^5.0.5", "yargs-parser": "^21.1.1" } }, "sha512-7dSzzRQ++CKnNI/krKnYRV7JKKPUXMEh61soaHKg9mrWEhzFWhFnxPxGl+69cD1Ou63C13NUPCnmIcrvqCuM6w=="],

    "yargs-parser": ["yargs-parser@21.1.1", "", {}, "sha512-tVpsJW7DdjecAiFpbIB1e3qxIQsE6NoPc5/eTdrbbIC4h0LVsWhnoa3g+m2HclBIujHzsxZ4VJVA+GUuc2/LBw=="],

    "yocto-queue": ["yocto-queue@1.2.2", "", {}, "sha512-4LCcse/U2MHZ63HAJVE+v71o7yOdIe4cZ70Wpf8D/IyjDKYQLV5GD46B+hSTjJsvV5PztjvHoU580EftxjDZFQ=="],

    "yocto-spinner": ["yocto-spinner@0.2.3", "", { "dependencies": { "yoctocolors": "^2.1.1" } }, "sha512-sqBChb33loEnkoXte1bLg45bEBsOP9N1kzQh5JZNKj/0rik4zAPTNSAVPj3uQAdc6slYJ0Ksc403G2XgxsJQFQ=="],

    "yoctocolors": ["yoctocolors@2.1.2", "", {}, "sha512-CzhO+pFNo8ajLM2d2IW/R93ipy99LWjtwblvC1RsoSUMZgyLbYFr221TnSNT7GjGdYui6P459mw9JH/g/zW2ug=="],

    "youch": ["youch@4.1.0", "", { "dependencies": { "@poppinss/colors": "^4.1.6", "@poppinss/dumper": "^0.7.0", "@speed-highlight/core": "^1.2.14", "cookie-es": "^2.0.0", "youch-core": "^0.3.3" } }, "sha512-cYekNh2tUoU+voS11X0D0UQntVCSO6LQ1h10VriQGmfbpf0mnGTruwZICts23UUNiZCXm8H8hQBtRrdsbhuNNg=="],

    "youch-core": ["youch-core@0.3.3", "", { "dependencies": { "@poppinss/exception": "^1.2.2", "error-stack-parser-es": "^1.0.5" } }, "sha512-ho7XuGjLaJ2hWHoK8yFnsUGy2Y5uDpqSTq1FkHLK4/oqKtyUU1AFbOOxY4IpC9f0fTLjwYbslUz0Po5BpD1wrA=="],

    "zip-stream": ["zip-stream@6.0.1", "", { "dependencies": { "archiver-utils": "^5.0.0", "compress-commons": "^6.0.2", "readable-stream": "^4.0.0" } }, "sha512-zK7YHHz4ZXpW89AHXUPbQVGKI7uvkd3hzusTdotCg1UxyaVtg0zFJSTfW/Dq5f7OBBVnq6cZIaC8Ti4hb6dtCA=="],

    "zod": ["zod@3.25.76", "", {}, "sha512-gzUt/qt81nXsFGKIFcC3YnfEAx5NkunCfnDlvuBSSFS02bcXu4Lmea0AFIUwbLWxWPx3d9p8S5QoaujKcNQxcQ=="],

    "zod-to-json-schema": ["zod-to-json-schema@3.25.1", "", { "peerDependencies": { "zod": "^3.25 || ^4" } }, "sha512-pM/SU9d3YAggzi6MtR4h7ruuQlqKtad8e9S0fmxcMi+ueAK5Korys/aWcV9LIIHTVbj01NdzxcnXSN+O74ZIVA=="],

    "zod-to-ts": ["zod-to-ts@1.2.0", "", { "peerDependencies": { "typescript": "^4.9.4 || ^5.0.2", "zod": "^3" } }, "sha512-x30XE43V+InwGpvTySRNz9kB7qFU8DlyEy7BsSTCHPH1R0QasMmHWZDCzYm6bVXtj/9NNJAZF3jW8rzFvH5OFA=="],

    "zwitch": ["zwitch@2.0.4", "", {}, "sha512-bXE4cR/kVZhKZX/RjPEflHaKVhUVl85noU3v6b8apfQEc1x4A+zBxjZ4lN8LqGd6WZ3dl98pY4o717VFmoPp+A=="],

    "@babel/code-frame/@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "@babel/code-frame/js-tokens": ["js-tokens@4.0.0", "", {}, "sha512-RdJUflcE3cUzKiMqQgsCu06FPu9UdIJO0beYbPhHN4k6apgJtifcoCtT9bcxOpYBtpD2kCM6Sbzg4CausW/PKQ=="],

    "@babel/core/@babel/parser": ["@babel/parser@7.29.2", "", { "dependencies": { "@babel/types": "^7.29.0" }, "bin": "./bin/babel-parser.js" }, "sha512-4GgRzy/+fsBa72/RZVJmGKPmZu9Byn8o4MoLpmNe1m8ZfYnz5emHLQz3U4gLud6Zwl0RZIcgiLD7Uq7ySFuDLA=="],

    "@babel/core/@babel/types": ["@babel/types@7.29.0", "", { "dependencies": { "@babel/helper-string-parser": "^7.27.1", "@babel/helper-validator-identifier": "^7.28.5" } }, "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A=="],

    "@babel/core/semver": ["semver@6.3.1", "", { "bin": { "semver": "bin/semver.js" } }, "sha512-BR7VvDCVHO+q2xBEWskxS6DJE1qRnb7DxzUrogb71CWoSficBxYsiAGd+Kl0mmq/MprG9yArRkyrQxTO6XjMzA=="],

    "@babel/generator/@babel/parser": ["@babel/parser@7.29.2", "", { "dependencies": { "@babel/types": "^7.29.0" }, "bin": "./bin/babel-parser.js" }, "sha512-4GgRzy/+fsBa72/RZVJmGKPmZu9Byn8o4MoLpmNe1m8ZfYnz5emHLQz3U4gLud6Zwl0RZIcgiLD7Uq7ySFuDLA=="],

    "@babel/generator/@babel/types": ["@babel/types@7.29.0", "", { "dependencies": { "@babel/helper-string-parser": "^7.27.1", "@babel/helper-validator-identifier": "^7.28.5" } }, "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A=="],

    "@babel/helper-annotate-as-pure/@babel/types": ["@babel/types@7.29.0", "", { "dependencies": { "@babel/helper-string-parser": "^7.27.1", "@babel/helper-validator-identifier": "^7.28.5" } }, "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A=="],

    "@babel/helper-compilation-targets/lru-cache": ["lru-cache@5.1.1", "", { "dependencies": { "yallist": "^3.0.2" } }, "sha512-KpNARQA3Iwv+jTA0utUVVbrh+Jlrr1Fv0e56GGzAFOXN7dk/FviaDW8LHmK52DlcH4WP2n6gI8vN1aesBFgo9w=="],

    "@babel/helper-compilation-targets/semver": ["semver@6.3.1", "", { "bin": { "semver": "bin/semver.js" } }, "sha512-BR7VvDCVHO+q2xBEWskxS6DJE1qRnb7DxzUrogb71CWoSficBxYsiAGd+Kl0mmq/MprG9yArRkyrQxTO6XjMzA=="],

    "@babel/helper-create-class-features-plugin/semver": ["semver@6.3.1", "", { "bin": { "semver": "bin/semver.js" } }, "sha512-BR7VvDCVHO+q2xBEWskxS6DJE1qRnb7DxzUrogb71CWoSficBxYsiAGd+Kl0mmq/MprG9yArRkyrQxTO6XjMzA=="],

    "@babel/helper-member-expression-to-functions/@babel/types": ["@babel/types@7.29.0", "", { "dependencies": { "@babel/helper-string-parser": "^7.27.1", "@babel/helper-validator-identifier": "^7.28.5" } }, "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A=="],

    "@babel/helper-module-imports/@babel/types": ["@babel/types@7.29.0", "", { "dependencies": { "@babel/helper-string-parser": "^7.27.1", "@babel/helper-validator-identifier": "^7.28.5" } }, "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A=="],

    "@babel/helper-module-transforms/@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "@babel/helper-optimise-call-expression/@babel/types": ["@babel/types@7.29.0", "", { "dependencies": { "@babel/helper-string-parser": "^7.27.1", "@babel/helper-validator-identifier": "^7.28.5" } }, "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A=="],

    "@babel/helper-skip-transparent-expression-wrappers/@babel/types": ["@babel/types@7.29.0", "", { "dependencies": { "@babel/helper-string-parser": "^7.27.1", "@babel/helper-validator-identifier": "^7.28.5" } }, "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A=="],

    "@babel/helpers/@babel/types": ["@babel/types@7.29.0", "", { "dependencies": { "@babel/helper-string-parser": "^7.27.1", "@babel/helper-validator-identifier": "^7.28.5" } }, "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A=="],

    "@babel/template/@babel/parser": ["@babel/parser@7.29.2", "", { "dependencies": { "@babel/types": "^7.29.0" }, "bin": "./bin/babel-parser.js" }, "sha512-4GgRzy/+fsBa72/RZVJmGKPmZu9Byn8o4MoLpmNe1m8ZfYnz5emHLQz3U4gLud6Zwl0RZIcgiLD7Uq7ySFuDLA=="],

    "@babel/template/@babel/types": ["@babel/types@7.29.0", "", { "dependencies": { "@babel/helper-string-parser": "^7.27.1", "@babel/helper-validator-identifier": "^7.28.5" } }, "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A=="],

    "@babel/traverse/@babel/parser": ["@babel/parser@7.29.2", "", { "dependencies": { "@babel/types": "^7.29.0" }, "bin": "./bin/babel-parser.js" }, "sha512-4GgRzy/+fsBa72/RZVJmGKPmZu9Byn8o4MoLpmNe1m8ZfYnz5emHLQz3U4gLud6Zwl0RZIcgiLD7Uq7ySFuDLA=="],

    "@babel/traverse/@babel/types": ["@babel/types@7.29.0", "", { "dependencies": { "@babel/helper-string-parser": "^7.27.1", "@babel/helper-validator-identifier": "^7.28.5" } }, "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A=="],

    "@dxup/nuxt/@nuxt/kit": ["@nuxt/kit@4.4.2", "", { "dependencies": { "c12": "^3.3.3", "consola": "^3.4.2", "defu": "^6.1.4", "destr": "^2.0.5", "errx": "^0.1.0", "exsolve": "^1.0.8", "ignore": "^7.0.5", "jiti": "^2.6.1", "klona": "^2.0.6", "mlly": "^1.8.1", "ohash": "^2.0.11", "pathe": "^2.0.3", "pkg-types": "^2.3.0", "rc9": "^3.0.0", "scule": "^1.3.0", "semver": "^7.7.4", "tinyglobby": "^0.2.15", "ufo": "^1.6.3", "unctx": "^2.5.0", "untyped": "^2.0.0" } }, "sha512-5+IPRNX2CjkBhuWUwz0hBuLqiaJPRoKzQ+SvcdrQDbAyE+VDeFt74VpSFr5/R0ujrK4b+XnSHUJWdS72w6hsog=="],

    "@dxup/nuxt/chokidar": ["chokidar@5.0.0", "", { "dependencies": { "readdirp": "^5.0.0" } }, "sha512-TQMmc3w+5AxjpL8iIiwebF73dRDF4fBIieAqGn9RGCWaEVwQ6Fb2cGe31Yns0RRIzii5goJ1Y7xbMwo1TxMplw=="],

    "@isaacs/cliui/string-width": ["string-width@5.1.2", "", { "dependencies": { "eastasianwidth": "^0.2.0", "emoji-regex": "^9.2.2", "strip-ansi": "^7.0.1" } }, "sha512-HnLOCR3vjcY8beoNLtcjZ5/nxn2afmME6lhrDrebokqMap+XbeW8n9TXpPDOqdGK5qcI3oT0GKTW6wC7EMiVqA=="],

    "@isaacs/cliui/strip-ansi": ["strip-ansi@7.2.0", "", { "dependencies": { "ansi-regex": "^6.2.2" } }, "sha512-yDPMNjp4WyfYBkHnjIRLfca1i6KMyGCtsVgoKe/z1+6vukgaENdgGBZt+ZmKPc4gavvEZ5OgHfHdrazhgNyG7w=="],

    "@isaacs/cliui/wrap-ansi": ["wrap-ansi@8.1.0", "", { "dependencies": { "ansi-styles": "^6.1.0", "string-width": "^5.0.1", "strip-ansi": "^7.0.1" } }, "sha512-si7QWI6zUMq56bESFvagtmzMdGOtoxfR+Sez11Mobfc7tm+VkUckk9bW2UeffTGVUbOksxmSw0AA2gs8g71NCQ=="],

    "@nuxt/cli/std-env": ["std-env@3.10.0", "", {}, "sha512-5GS12FdOZNliM5mAOxFRg7Ir0pWz8MdpYm6AY6VPkGpbA7ZzmbzNcBJQ0GPvvyWgcY7QAhCgf9Uy89I03faLkg=="],

    "@nuxt/devtools/@nuxt/kit": ["@nuxt/kit@4.4.2", "", { "dependencies": { "c12": "^3.3.3", "consola": "^3.4.2", "defu": "^6.1.4", "destr": "^2.0.5", "errx": "^0.1.0", "exsolve": "^1.0.8", "ignore": "^7.0.5", "jiti": "^2.6.1", "klona": "^2.0.6", "mlly": "^1.8.1", "ohash": "^2.0.11", "pathe": "^2.0.3", "pkg-types": "^2.3.0", "rc9": "^3.0.0", "scule": "^1.3.0", "semver": "^7.7.4", "tinyglobby": "^0.2.15", "ufo": "^1.6.3", "unctx": "^2.5.0", "untyped": "^2.0.0" } }, "sha512-5+IPRNX2CjkBhuWUwz0hBuLqiaJPRoKzQ+SvcdrQDbAyE+VDeFt74VpSFr5/R0ujrK4b+XnSHUJWdS72w6hsog=="],

    "@nuxt/devtools/@vue/devtools-core": ["@vue/devtools-core@8.1.0", "", { "dependencies": { "@vue/devtools-kit": "^8.1.0", "@vue/devtools-shared": "^8.1.0" }, "peerDependencies": { "vue": "^3.0.0" } }, "sha512-LvD1VgDpoHmYL00IgKRLKktF6SsPAb0yaV8wB8q2jRwsAWvqhS8+vsMLEGKNs7uoKyymXhT92dhxgf/wir6YGQ=="],

    "@nuxt/devtools/@vue/devtools-kit": ["@vue/devtools-kit@8.1.0", "", { "dependencies": { "@vue/devtools-shared": "^8.1.0", "birpc": "^2.6.1", "hookable": "^5.5.3", "perfect-debounce": "^2.0.0" } }, "sha512-/NZlS4WtGIB54DA/z10gzk+n/V7zaqSzYZOVlg2CfdnpIKdB61bd7JDIMxf/zrtX41zod8E2/bbEBoW/d7x70Q=="],

    "@nuxt/devtools/execa": ["execa@8.0.1", "", { "dependencies": { "cross-spawn": "^7.0.3", "get-stream": "^8.0.1", "human-signals": "^5.0.0", "is-stream": "^3.0.0", "merge-stream": "^2.0.0", "npm-run-path": "^5.1.0", "onetime": "^6.0.0", "signal-exit": "^4.1.0", "strip-final-newline": "^3.0.0" } }, "sha512-VyhnebXciFV2DESc+p6B+y0LjSm0krU4OgJN44qFAhBY0TJ+1V61tYD2+wHusZ6F9n5K+vl8k0sTy7PEfV4qpg=="],

    "@nuxt/devtools/vite-plugin-inspect": ["vite-plugin-inspect@11.3.3", "", { "dependencies": { "ansis": "^4.1.0", "debug": "^4.4.1", "error-stack-parser-es": "^1.0.5", "ohash": "^2.0.11", "open": "^10.2.0", "perfect-debounce": "^2.0.0", "sirv": "^3.0.1", "unplugin-utils": "^0.3.0", "vite-dev-rpc": "^1.1.0" }, "peerDependencies": { "vite": "^6.0.0 || ^7.0.0-0" } }, "sha512-u2eV5La99oHoYPHE6UvbwgEqKKOQGz86wMg40CCosP6q8BkB6e5xPneZfYagK4ojPJSj5anHCrnvC20DpwVdRA=="],

    "@nuxt/devtools-kit/@nuxt/kit": ["@nuxt/kit@4.4.2", "", { "dependencies": { "c12": "^3.3.3", "consola": "^3.4.2", "defu": "^6.1.4", "destr": "^2.0.5", "errx": "^0.1.0", "exsolve": "^1.0.8", "ignore": "^7.0.5", "jiti": "^2.6.1", "klona": "^2.0.6", "mlly": "^1.8.1", "ohash": "^2.0.11", "pathe": "^2.0.3", "pkg-types": "^2.3.0", "rc9": "^3.0.0", "scule": "^1.3.0", "semver": "^7.7.4", "tinyglobby": "^0.2.15", "ufo": "^1.6.3", "unctx": "^2.5.0", "untyped": "^2.0.0" } }, "sha512-5+IPRNX2CjkBhuWUwz0hBuLqiaJPRoKzQ+SvcdrQDbAyE+VDeFt74VpSFr5/R0ujrK4b+XnSHUJWdS72w6hsog=="],

    "@nuxt/devtools-kit/execa": ["execa@8.0.1", "", { "dependencies": { "cross-spawn": "^7.0.3", "get-stream": "^8.0.1", "human-signals": "^5.0.0", "is-stream": "^3.0.0", "merge-stream": "^2.0.0", "npm-run-path": "^5.1.0", "onetime": "^6.0.0", "signal-exit": "^4.1.0", "strip-final-newline": "^3.0.0" } }, "sha512-VyhnebXciFV2DESc+p6B+y0LjSm0krU4OgJN44qFAhBY0TJ+1V61tYD2+wHusZ6F9n5K+vl8k0sTy7PEfV4qpg=="],

    "@nuxt/devtools-wizard/execa": ["execa@8.0.1", "", { "dependencies": { "cross-spawn": "^7.0.3", "get-stream": "^8.0.1", "human-signals": "^5.0.0", "is-stream": "^3.0.0", "merge-stream": "^2.0.0", "npm-run-path": "^5.1.0", "onetime": "^6.0.0", "signal-exit": "^4.1.0", "strip-final-newline": "^3.0.0" } }, "sha512-VyhnebXciFV2DESc+p6B+y0LjSm0krU4OgJN44qFAhBY0TJ+1V61tYD2+wHusZ6F9n5K+vl8k0sTy7PEfV4qpg=="],

    "@nuxt/telemetry/ofetch": ["ofetch@2.0.0-alpha.3", "", {}, "sha512-zpYTCs2byOuft65vI3z43Dd6iSdFbOZZLb9/d21aCpx2rGastVU9dOCv0lu4ykc1Ur1anAYjDi3SUvR0vq50JA=="],

    "@nuxt/telemetry/std-env": ["std-env@3.10.0", "", {}, "sha512-5GS12FdOZNliM5mAOxFRg7Ir0pWz8MdpYm6AY6VPkGpbA7ZzmbzNcBJQ0GPvvyWgcY7QAhCgf9Uy89I03faLkg=="],

    "@nuxt/vite-builder/@vitejs/plugin-vue": ["@vitejs/plugin-vue@6.0.5", "", { "dependencies": { "@rolldown/pluginutils": "1.0.0-rc.2" }, "peerDependencies": { "vite": "^5.0.0 || ^6.0.0 || ^7.0.0 || ^8.0.0", "vue": "^3.2.25" } }, "sha512-bL3AxKuQySfk1iGcBsQnoRVexTPJq0Z/ixFVM8OhVJAP6ZXXXLtM7NFKWhLl30Kg7uTBqIaPXbh+nuQCuBDedg=="],

    "@nuxt/vite-builder/@vitejs/plugin-vue-jsx": ["@vitejs/plugin-vue-jsx@5.1.5", "", { "dependencies": { "@babel/core": "^7.29.0", "@babel/plugin-syntax-typescript": "^7.28.6", "@babel/plugin-transform-typescript": "^7.28.6", "@rolldown/pluginutils": "^1.0.0-rc.2", "@vue/babel-plugin-jsx": "^2.0.1" }, "peerDependencies": { "vite": "^5.0.0 || ^6.0.0 || ^7.0.0 || ^8.0.0", "vue": "^3.0.0" } }, "sha512-jIAsvHOEtWpslLOI2MeElGFxH7M8pM83BU/Tor4RLyiwH0FM4nUW3xdvbw20EeU9wc5IspQwMq225K3CMnJEpA=="],

    "@nuxt/vite-builder/vite": ["vite@7.3.1", "", { "dependencies": { "esbuild": "^0.27.0", "fdir": "^6.5.0", "picomatch": "^4.0.3", "postcss": "^8.5.6", "rollup": "^4.43.0", "tinyglobby": "^0.2.15" }, "optionalDependencies": { "fsevents": "~2.3.3" }, "peerDependencies": { "@types/node": "^20.19.0 || >=22.12.0", "jiti": ">=1.21.0", "less": "^4.0.0", "lightningcss": "^1.21.0", "sass": "^1.70.0", "sass-embedded": "^1.70.0", "stylus": ">=0.54.8", "sugarss": "^5.0.0", "terser": "^5.16.0", "tsx": "^4.8.1", "yaml": "^2.4.2" }, "optionalPeers": ["@types/node", "jiti", "less", "lightningcss", "sass", "sass-embedded", "stylus", "sugarss", "terser", "tsx", "yaml"], "bin": { "vite": "bin/vite.js" } }, "sha512-w+N7Hifpc3gRjZ63vYBXA56dvvRlNWRczTdmCBBa+CotUzAPf5b7YMdMR/8CQoeYE5LX3W4wj6RYTgonm1b9DA=="],

    "@parcel/watcher-wasm/napi-wasm": ["napi-wasm@1.1.3", "", { "bundled": true }, "sha512-h/4nMGsHjZDCYmQVNODIrYACVJ+I9KItbG+0si6W/jSjdA9JbWDoU4LLeMXVcEQGHjttI2tuXqDrbGF7qkUHHg=="],

    "@rollup/plugin-commonjs/estree-walker": ["estree-walker@2.0.2", "", {}, "sha512-Rfkk/Mp/DL7JVje3u18FxFujQlTNR2q6QfMSMB7AvCBx91NGj/ba3kCfza0f6dVDbw7YlRf/nDrn7pQrCCyQ/w=="],

    "@rollup/plugin-inject/estree-walker": ["estree-walker@2.0.2", "", {}, "sha512-Rfkk/Mp/DL7JVje3u18FxFujQlTNR2q6QfMSMB7AvCBx91NGj/ba3kCfza0f6dVDbw7YlRf/nDrn7pQrCCyQ/w=="],

    "@rollup/pluginutils/estree-walker": ["estree-walker@2.0.2", "", {}, "sha512-Rfkk/Mp/DL7JVje3u18FxFujQlTNR2q6QfMSMB7AvCBx91NGj/ba3kCfza0f6dVDbw7YlRf/nDrn7pQrCCyQ/w=="],

    "@types/babel__core/@babel/parser": ["@babel/parser@7.29.2", "", { "dependencies": { "@babel/types": "^7.29.0" }, "bin": "./bin/babel-parser.js" }, "sha512-4GgRzy/+fsBa72/RZVJmGKPmZu9Byn8o4MoLpmNe1m8ZfYnz5emHLQz3U4gLud6Zwl0RZIcgiLD7Uq7ySFuDLA=="],

    "@types/babel__core/@babel/types": ["@babel/types@7.29.0", "", { "dependencies": { "@babel/helper-string-parser": "^7.27.1", "@babel/helper-validator-identifier": "^7.28.5" } }, "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A=="],

    "@types/babel__generator/@babel/types": ["@babel/types@7.29.0", "", { "dependencies": { "@babel/helper-string-parser": "^7.27.1", "@babel/helper-validator-identifier": "^7.28.5" } }, "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A=="],

    "@types/babel__template/@babel/parser": ["@babel/parser@7.29.2", "", { "dependencies": { "@babel/types": "^7.29.0" }, "bin": "./bin/babel-parser.js" }, "sha512-4GgRzy/+fsBa72/RZVJmGKPmZu9Byn8o4MoLpmNe1m8ZfYnz5emHLQz3U4gLud6Zwl0RZIcgiLD7Uq7ySFuDLA=="],

    "@types/babel__template/@babel/types": ["@babel/types@7.29.0", "", { "dependencies": { "@babel/helper-string-parser": "^7.27.1", "@babel/helper-validator-identifier": "^7.28.5" } }, "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A=="],

    "@types/babel__traverse/@babel/types": ["@babel/types@7.29.0", "", { "dependencies": { "@babel/helper-string-parser": "^7.27.1", "@babel/helper-validator-identifier": "^7.28.5" } }, "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A=="],

    "@vercel/nft/estree-walker": ["estree-walker@2.0.2", "", {}, "sha512-Rfkk/Mp/DL7JVje3u18FxFujQlTNR2q6QfMSMB7AvCBx91NGj/ba3kCfza0f6dVDbw7YlRf/nDrn7pQrCCyQ/w=="],

    "@vitejs/plugin-react/@rolldown/pluginutils": ["@rolldown/pluginutils@1.0.0-beta.27", "", {}, "sha512-+d0F4MKMCbeVUJwG96uQ4SgAznZNSq93I3V+9NHA4OpvqG8mRCpGdKmK8l/dl02h2CCDHwW2FqilnTyDcAnqjA=="],

    "@vue-macros/common/ast-kit": ["ast-kit@2.2.0", "", { "dependencies": { "@babel/parser": "^7.28.5", "pathe": "^2.0.3" } }, "sha512-m1Q/RaVOnTp9JxPX+F+Zn7IcLYMzM8kZofDImfsKZd8MbR+ikdOzTeztStWqfrqIxZnYWryyI9ePm3NGjnZgGw=="],

    "@vue/babel-plugin-jsx/@babel/types": ["@babel/types@7.29.0", "", { "dependencies": { "@babel/helper-string-parser": "^7.27.1", "@babel/helper-validator-identifier": "^7.28.5" } }, "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A=="],

    "@vue/babel-plugin-resolve-type/@babel/parser": ["@babel/parser@7.29.2", "", { "dependencies": { "@babel/types": "^7.29.0" }, "bin": "./bin/babel-parser.js" }, "sha512-4GgRzy/+fsBa72/RZVJmGKPmZu9Byn8o4MoLpmNe1m8ZfYnz5emHLQz3U4gLud6Zwl0RZIcgiLD7Uq7ySFuDLA=="],

    "@vue/compiler-core/@babel/parser": ["@babel/parser@7.29.2", "", { "dependencies": { "@babel/types": "^7.29.0" }, "bin": "./bin/babel-parser.js" }, "sha512-4GgRzy/+fsBa72/RZVJmGKPmZu9Byn8o4MoLpmNe1m8ZfYnz5emHLQz3U4gLud6Zwl0RZIcgiLD7Uq7ySFuDLA=="],

    "@vue/compiler-core/estree-walker": ["estree-walker@2.0.2", "", {}, "sha512-Rfkk/Mp/DL7JVje3u18FxFujQlTNR2q6QfMSMB7AvCBx91NGj/ba3kCfza0f6dVDbw7YlRf/nDrn7pQrCCyQ/w=="],

    "@vue/compiler-sfc/@babel/parser": ["@babel/parser@7.29.2", "", { "dependencies": { "@babel/types": "^7.29.0" }, "bin": "./bin/babel-parser.js" }, "sha512-4GgRzy/+fsBa72/RZVJmGKPmZu9Byn8o4MoLpmNe1m8ZfYnz5emHLQz3U4gLud6Zwl0RZIcgiLD7Uq7ySFuDLA=="],

    "@vue/compiler-sfc/estree-walker": ["estree-walker@2.0.2", "", {}, "sha512-Rfkk/Mp/DL7JVje3u18FxFujQlTNR2q6QfMSMB7AvCBx91NGj/ba3kCfza0f6dVDbw7YlRf/nDrn7pQrCCyQ/w=="],

    "@vue/devtools-api/@vue/devtools-kit": ["@vue/devtools-kit@8.1.0", "", { "dependencies": { "@vue/devtools-shared": "^8.1.0", "birpc": "^2.6.1", "hookable": "^5.5.3", "perfect-debounce": "^2.0.0" } }, "sha512-/NZlS4WtGIB54DA/z10gzk+n/V7zaqSzYZOVlg2CfdnpIKdB61bd7JDIMxf/zrtX41zod8E2/bbEBoW/d7x70Q=="],

    "@vue/devtools-core/nanoid": ["nanoid@5.1.7", "", { "bin": { "nanoid": "bin/nanoid.js" } }, "sha512-ua3NDgISf6jdwezAheMOk4mbE1LXjm1DfMUDMuJf4AqxLFK3ccGpgWizwa5YV7Yz9EpXwEaWoRXSb/BnV0t5dQ=="],

    "@vue/devtools-kit/birpc": ["birpc@2.9.0", "", {}, "sha512-KrayHS5pBi69Xi9JmvoqrIgYGDkD6mcSe/i6YKi3w5kekCLzrX4+nawcXqrj2tIp50Kw/mT/s3p+GVK0A0sKxw=="],

    "@vue/devtools-kit/hookable": ["hookable@5.5.3", "", {}, "sha512-Yc+BQe8SvoXH1643Qez1zqLRmbA5rCL+sSmk6TVos0LWVfNIB7PGncdlId77WzLGSIB5KaWgTaNTs2lNVEI6VQ=="],

    "@vue/devtools-kit/perfect-debounce": ["perfect-debounce@1.0.0", "", {}, "sha512-xCy9V055GLEqoFaHoC1SoLIaLmWctgCUaBaWxDZ7/Zx4CTyX7cJQLJOok/orfjZAh9kEYpjJa4d0KcJmCbctZA=="],

    "anymatch/picomatch": ["picomatch@2.3.1", "", {}, "sha512-JU3teHTNjmE2VCGFzuY8EXzCDVwEqB2a8fsIvwaStHhAWJEeVd1o1QD80CU6+ZdEXXSLbSsuLwJjkCBWqRQUVA=="],

    "archiver-utils/glob": ["glob@10.5.0", "", { "dependencies": { "foreground-child": "^3.1.0", "jackspeak": "^3.1.2", "minimatch": "^9.0.4", "minipass": "^7.1.2", "package-json-from-dist": "^1.0.0", "path-scurry": "^1.11.1" }, "bin": { "glob": "dist/esm/bin.mjs" } }, "sha512-DfXN8DfhJ7NH3Oe7cFmu3NCu1wKbkReJ8TorzSAFbSKrlNaQSKfIzqYqVY8zlbs2NLBbWpRiU52GX2PbaBVNkg=="],

    "archiver-utils/is-stream": ["is-stream@2.0.1", "", {}, "sha512-hFoiJiTl63nn+kstHGBtewWSKnQLpyb155KHheA1l39uvtO9nWIop1p3udqPcUd/xbF1VLMO4n7OI6p7RbngDg=="],

    "ast-walker-scope/@babel/parser": ["@babel/parser@7.29.2", "", { "dependencies": { "@babel/types": "^7.29.0" }, "bin": "./bin/babel-parser.js" }, "sha512-4GgRzy/+fsBa72/RZVJmGKPmZu9Byn8o4MoLpmNe1m8ZfYnz5emHLQz3U4gLud6Zwl0RZIcgiLD7Uq7ySFuDLA=="],

    "ast-walker-scope/ast-kit": ["ast-kit@2.2.0", "", { "dependencies": { "@babel/parser": "^7.28.5", "pathe": "^2.0.3" } }, "sha512-m1Q/RaVOnTp9JxPX+F+Zn7IcLYMzM8kZofDImfsKZd8MbR+ikdOzTeztStWqfrqIxZnYWryyI9ePm3NGjnZgGw=="],

    "boxen/string-width": ["string-width@7.2.0", "", { "dependencies": { "emoji-regex": "^10.3.0", "get-east-asian-width": "^1.0.0", "strip-ansi": "^7.1.0" } }, "sha512-tsaTIkKW9b4N+AEj+SVA+WhJzV7/zMhcSu78mLKWSk7cXMOSHsBKFWUs0fWwq8QyK3MgJBQRX6Gbi4kYbdvGkQ=="],

    "c12/chokidar": ["chokidar@5.0.0", "", { "dependencies": { "readdirp": "^5.0.0" } }, "sha512-TQMmc3w+5AxjpL8iIiwebF73dRDF4fBIieAqGn9RGCWaEVwQ6Fb2cGe31Yns0RRIzii5goJ1Y7xbMwo1TxMplw=="],

    "c12/giget": ["giget@2.0.0", "", { "dependencies": { "citty": "^0.1.6", "consola": "^3.4.0", "defu": "^6.1.4", "node-fetch-native": "^1.6.6", "nypm": "^0.6.0", "pathe": "^2.0.3" }, "bin": { "giget": "dist/cli.mjs" } }, "sha512-L5bGsVkxJbJgdnwyuheIunkGatUF/zssUoxxjACCseZYAVbaqdh9Tsmmlkl8vYan09H7sbvKt4pS8GqKLBrEzA=="],

    "c12/rc9": ["rc9@2.1.2", "", { "dependencies": { "defu": "^6.1.4", "destr": "^2.0.3" } }, "sha512-btXCnMmRIBINM2LDZoEmOogIZU7Qe7zn4BpomSKZ/ykbLObuBdvG+mFq11DL6fjH1DRwHhrlgtYWG96bJiC7Cg=="],

    "clipboardy/execa": ["execa@8.0.1", "", { "dependencies": { "cross-spawn": "^7.0.3", "get-stream": "^8.0.1", "human-signals": "^5.0.0", "is-stream": "^3.0.0", "merge-stream": "^2.0.0", "npm-run-path": "^5.1.0", "onetime": "^6.0.0", "signal-exit": "^4.1.0", "strip-final-newline": "^3.0.0" } }, "sha512-VyhnebXciFV2DESc+p6B+y0LjSm0krU4OgJN44qFAhBY0TJ+1V61tYD2+wHusZ6F9n5K+vl8k0sTy7PEfV4qpg=="],

    "cliui/wrap-ansi": ["wrap-ansi@7.0.0", "", { "dependencies": { "ansi-styles": "^4.0.0", "string-width": "^4.1.0", "strip-ansi": "^6.0.0" } }, "sha512-YVGIj2kamLSTxw6NsZjoBxfSwsn0ycdesmc4p+Q21c5zPuZ1pl+NfxVdxPtdHvmNVOQ6XSYG4AUtyt/Fi7D16Q=="],

    "compress-commons/is-stream": ["is-stream@2.0.1", "", {}, "sha512-hFoiJiTl63nn+kstHGBtewWSKnQLpyb155KHheA1l39uvtO9nWIop1p3udqPcUd/xbF1VLMO4n7OI6p7RbngDg=="],

    "cross-spawn/which": ["which@2.0.2", "", { "dependencies": { "isexe": "^2.0.0" }, "bin": { "node-which": "./bin/node-which" } }, "sha512-BLI3Tl1TW3Pvl70l3yq3Y64i+awpwXqsGBYWkkqMtnbXgrMD+yj7rhW0kuEDxzJaYXGjEW5ogapKNMEKNMjibA=="],

    "csso/css-tree": ["css-tree@2.2.1", "", { "dependencies": { "mdn-data": "2.0.28", "source-map-js": "^1.0.1" } }, "sha512-OA0mILzGc1kCOCSJerOeqDxDQ4HOh+G8NbOJFOTgOCzpw7fCBubk0fEyxp8AgOL/jvLgYA/uV0cMbe43ElF1JA=="],

    "dom-serializer/entities": ["entities@4.5.0", "", {}, "sha512-V0hjH4dGPh9Ao5p0MoRY6BVqtwCjhz6vI5LT8AJ55H+4g9/4vbHx1I54fS0XuclLhDHArPQCiMjDxjaL8fPxhw=="],

    "dot-prop/type-fest": ["type-fest@5.4.4", "", { "dependencies": { "tagged-tag": "^1.0.0" } }, "sha512-JnTrzGu+zPV3aXIUhnyWJj4z/wigMsdYajGLIYakqyOW1nPllzXEJee0QQbHj+CTIQtXGlAjuK0UY+2xTyjVAw=="],

    "externality/pathe": ["pathe@1.1.2", "", {}, "sha512-whLdWMYL2TwI08hn8/ZqAbrVemu0LNaNNJZX73O6qaIdCTfXutsLhMkjdENX0qhsQ9uIimo4/aQOmXkoon2nDQ=="],

    "globby/unicorn-magic": ["unicorn-magic@0.4.0", "", {}, "sha512-wH590V9VNgYH9g3lH9wWjTrUoKsjLF6sGLjhR4sH1LWpLmCOH0Zf7PukhDA8BiS7KHe4oPNkcTHqYkj7SOGUOw=="],

    "h3/cookie-es": ["cookie-es@1.2.2", "", {}, "sha512-+W7VmiVINB+ywl1HGXJXmrqkOhpKrIiVZV6tQuV54ZyQC7MMuBt81Vc336GMLoHBq5hV/F9eXgt5Mnx0Rha5Fg=="],

    "impound/es-module-lexer": ["es-module-lexer@2.0.0", "", {}, "sha512-5POEcUuZybH7IdmGsD8wlf0AI55wMecM9rVBTI/qEAy2c1kTOm3DjFYjrBdI2K3BaJjJYfYFeRtM0t9ssnRuxw=="],

    "lazystream/readable-stream": ["readable-stream@2.3.8", "", { "dependencies": { "core-util-is": "~1.0.0", "inherits": "~2.0.3", "isarray": "~1.0.0", "process-nextick-args": "~2.0.0", "safe-buffer": "~5.1.1", "string_decoder": "~1.1.1", "util-deprecate": "~1.0.1" } }, "sha512-8p0AUk4XODgIewSi0l8Epjs+EVnWiK7NoDIEGU0HhE7+ZyY8D1IMY7odu5lRrFXGg71L15KG8QrPmum45RTtdA=="],

    "listhen/citty": ["citty@0.1.6", "", { "dependencies": { "consola": "^3.2.3" } }, "sha512-tskPPKEs8D2KPafUypv2gxwJP8h/OaJmC82QQGGDQcHvXX43xF2VDACcJVmZ0EuSxkpO9Kc4MlrA3q0+FG58AQ=="],

    "listhen/pathe": ["pathe@1.1.2", "", {}, "sha512-whLdWMYL2TwI08hn8/ZqAbrVemu0LNaNNJZX73O6qaIdCTfXutsLhMkjdENX0qhsQ9uIimo4/aQOmXkoon2nDQ=="],

    "listhen/std-env": ["std-env@3.10.0", "", {}, "sha512-5GS12FdOZNliM5mAOxFRg7Ir0pWz8MdpYm6AY6VPkGpbA7ZzmbzNcBJQ0GPvvyWgcY7QAhCgf9Uy89I03faLkg=="],

    "local-pkg/quansync": ["quansync@0.2.11", "", {}, "sha512-AifT7QEbW9Nri4tAwR5M/uzpBuqfZf+zwaEM/QkzEjj7NBuFD2rBuy0K3dE+8wltbezDV7JMA0WfnCPYRSYbXA=="],

    "magic-regexp/unplugin": ["unplugin@2.3.11", "", { "dependencies": { "@jridgewell/remapping": "^2.3.5", "acorn": "^8.15.0", "picomatch": "^4.0.3", "webpack-virtual-modules": "^0.6.2" } }, "sha512-5uKD0nqiYVzlmCRs01Fhs2BdkEgBS3SAVP6ndrBsuK42iC2+JHyxM05Rm9G8+5mkmRtzMZGY8Ct5+mliZxU/Ww=="],

    "magicast/@babel/parser": ["@babel/parser@7.29.2", "", { "dependencies": { "@babel/types": "^7.29.0" }, "bin": "./bin/babel-parser.js" }, "sha512-4GgRzy/+fsBa72/RZVJmGKPmZu9Byn8o4MoLpmNe1m8ZfYnz5emHLQz3U4gLud6Zwl0RZIcgiLD7Uq7ySFuDLA=="],

    "magicast/@babel/types": ["@babel/types@7.29.0", "", { "dependencies": { "@babel/helper-string-parser": "^7.27.1", "@babel/helper-validator-identifier": "^7.28.5" } }, "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A=="],

    "micromatch/picomatch": ["picomatch@2.3.1", "", {}, "sha512-JU3teHTNjmE2VCGFzuY8EXzCDVwEqB2a8fsIvwaStHhAWJEeVd1o1QD80CU6+ZdEXXSLbSsuLwJjkCBWqRQUVA=="],

    "mlly/pkg-types": ["pkg-types@1.3.1", "", { "dependencies": { "confbox": "^0.1.8", "mlly": "^1.7.4", "pathe": "^2.0.1" } }, "sha512-/Jm5M4RvtBFVkKWRu2BLUTNP8/M2a+UwuAX+ae4770q1qVGtfjG+WTCupoZixokjmHiry8uI+dlY8KXYV5HVVQ=="],

    "nitropack/chokidar": ["chokidar@5.0.0", "", { "dependencies": { "readdirp": "^5.0.0" } }, "sha512-TQMmc3w+5AxjpL8iIiwebF73dRDF4fBIieAqGn9RGCWaEVwQ6Fb2cGe31Yns0RRIzii5goJ1Y7xbMwo1TxMplw=="],

    "nitropack/citty": ["citty@0.1.6", "", { "dependencies": { "consola": "^3.2.3" } }, "sha512-tskPPKEs8D2KPafUypv2gxwJP8h/OaJmC82QQGGDQcHvXX43xF2VDACcJVmZ0EuSxkpO9Kc4MlrA3q0+FG58AQ=="],

    "nitropack/hookable": ["hookable@5.5.3", "", {}, "sha512-Yc+BQe8SvoXH1643Qez1zqLRmbA5rCL+sSmk6TVos0LWVfNIB7PGncdlId77WzLGSIB5KaWgTaNTs2lNVEI6VQ=="],

    "nitropack/std-env": ["std-env@3.10.0", "", {}, "sha512-5GS12FdOZNliM5mAOxFRg7Ir0pWz8MdpYm6AY6VPkGpbA7ZzmbzNcBJQ0GPvvyWgcY7QAhCgf9Uy89I03faLkg=="],

    "nitropack/unimport": ["unimport@5.7.0", "", { "dependencies": { "acorn": "^8.16.0", "escape-string-regexp": "^5.0.0", "estree-walker": "^3.0.3", "local-pkg": "^1.1.2", "magic-string": "^0.30.21", "mlly": "^1.8.0", "pathe": "^2.0.3", "picomatch": "^4.0.3", "pkg-types": "^2.3.0", "scule": "^1.3.0", "strip-literal": "^3.1.0", "tinyglobby": "^0.2.15", "unplugin": "^2.3.11", "unplugin-utils": "^0.3.1" } }, "sha512-njnL6sp8lEA8QQbZrt+52p/g4X0rw3bnGGmUcJnt1jeG8+iiqO779aGz0PirCtydAIVcuTBRlJ52F0u46z309Q=="],

    "npm-run-path/path-key": ["path-key@4.0.0", "", {}, "sha512-haREypq7xkM7ErfgIyA0z+Bj4AGKlMSdlQE2jvJo6huWD1EdkKYV+G/T4nq0YEF2vgTT8kqMFKo1uHn950r4SQ=="],

    "nuxt/chokidar": ["chokidar@5.0.0", "", { "dependencies": { "readdirp": "^5.0.0" } }, "sha512-TQMmc3w+5AxjpL8iIiwebF73dRDF4fBIieAqGn9RGCWaEVwQ6Fb2cGe31Yns0RRIzii5goJ1Y7xbMwo1TxMplw=="],

    "nuxt/hookable": ["hookable@5.5.3", "", {}, "sha512-Yc+BQe8SvoXH1643Qez1zqLRmbA5rCL+sSmk6TVos0LWVfNIB7PGncdlId77WzLGSIB5KaWgTaNTs2lNVEI6VQ=="],

    "nuxt/vue-router": ["vue-router@4.6.4", "", { "dependencies": { "@vue/devtools-api": "^6.6.4" }, "peerDependencies": { "vue": "^3.5.0" } }, "sha512-Hz9q5sa33Yhduglwz6g9skT8OBPii+4bFn88w6J+J4MfEo4KRRpmiNG/hHHkdbRFlLBOqxN8y8gf2Fb0MTUgVg=="],

    "oxc-parser/@oxc-project/types": ["@oxc-project/types@0.117.0", "", {}, "sha512-C/kPXBphID44fXdsa2xSOCuzX8fKZiFxPsvucJ6Yfkr6CJlMA+kNLPNKyLoI+l9XlDsNxBrz6h7IIjKU8pB69w=="],

    "parse5/entities": ["entities@6.0.1", "", {}, "sha512-aN97NXWF6AWBTahfVOIrB/NShkzi5H7F9r1s9mD3cDj4Ko5f2qhhVoYMibXF7GlLveb/D2ioWay8lxI97Ven3g=="],

    "prompts/kleur": ["kleur@3.0.3", "", {}, "sha512-eTIzlVOSUR+JxdDFepEYcBMtZ9Qqdef+rnzWdRZuMbOywu5tO2w2N7rqjoANZ5k9vywhL6Br1VRjUIgTQx4E8w=="],

    "readdir-glob/minimatch": ["minimatch@5.1.9", "", { "dependencies": { "brace-expansion": "^2.0.1" } }, "sha512-7o1wEA2RyMP7Iu7GNba9vc0RWWGACJOCZBJX2GJWip0ikV+wcOsgVuY9uE8CPiyQhkGFSlhuSkZPavN7u1c2Fw=="],

    "rolldown-plugin-dts/@babel/generator": ["@babel/generator@8.0.0-rc.2", "", { "dependencies": { "@babel/parser": "^8.0.0-rc.2", "@babel/types": "^8.0.0-rc.2", "@jridgewell/gen-mapping": "^0.3.12", "@jridgewell/trace-mapping": "^0.3.28", "@types/jsesc": "^2.5.0", "jsesc": "^3.0.2" } }, "sha512-oCQ1IKPwkzCeJzAPb7Fv8rQ9k5+1sG8mf2uoHiMInPYvkRfrDJxbTIbH51U+jstlkghus0vAi3EBvkfvEsYNLQ=="],

    "rollup-plugin-visualizer/open": ["open@8.4.2", "", { "dependencies": { "define-lazy-prop": "^2.0.0", "is-docker": "^2.1.1", "is-wsl": "^2.2.0" } }, "sha512-7x81NCL719oNbsq/3mh+hVrAWmFuEYUqrq/Iw3kUzH8ReypT9QQ0BLoJS7/G9k6N81XjW4qHWtjWwe/9eLy1EQ=="],

    "source-map-support/source-map": ["source-map@0.6.1", "", {}, "sha512-UjgapumWlbMhkBgzT7Ykc5YXUT46F0iKu8SGXq0bcwP5dz/h0Plj6enJqjz1Zbq2l5WaqYnrVbwWOWMyF3F47g=="],

    "svgo/commander": ["commander@11.1.0", "", {}, "sha512-yPVavfyCcRhmorC7rWlkHn15b4wDVgVmBA7kV4QVBsF7kv/9TKJAbAXVTxvTnwP8HHKjRCJDClKbciiYS7p0DQ=="],

    "tar/yallist": ["yallist@5.0.0", "", {}, "sha512-YgvUTfwqyc7UXVMrB+SImsVYSmTS8X/tSrtdNZMImM+n7+QTriRXyXim0mBrTXNeqzVF0KWGgHPeiyViFFrNDw=="],

    "terser/commander": ["commander@2.20.3", "", {}, "sha512-GpVkmM8vF2vQUkj2LvZmD35JxeJOLCwJ9cUkugyk2nuhbv3+mJvpLYYt+0+USMxE+oj+ey/lJEnhZw75x/OMcQ=="],

    "unctx/unplugin": ["unplugin@2.3.11", "", { "dependencies": { "@jridgewell/remapping": "^2.3.5", "acorn": "^8.15.0", "picomatch": "^4.0.3", "webpack-virtual-modules": "^0.6.2" } }, "sha512-5uKD0nqiYVzlmCRs01Fhs2BdkEgBS3SAVP6ndrBsuK42iC2+JHyxM05Rm9G8+5mkmRtzMZGY8Ct5+mliZxU/Ww=="],

    "unplugin-vue-router/chokidar": ["chokidar@5.0.0", "", { "dependencies": { "readdirp": "^5.0.0" } }, "sha512-TQMmc3w+5AxjpL8iIiwebF73dRDF4fBIieAqGn9RGCWaEVwQ6Fb2cGe31Yns0RRIzii5goJ1Y7xbMwo1TxMplw=="],

    "unplugin-vue-router/unplugin": ["unplugin@2.3.11", "", { "dependencies": { "@jridgewell/remapping": "^2.3.5", "acorn": "^8.15.0", "picomatch": "^4.0.3", "webpack-virtual-modules": "^0.6.2" } }, "sha512-5uKD0nqiYVzlmCRs01Fhs2BdkEgBS3SAVP6ndrBsuK42iC2+JHyxM05Rm9G8+5mkmRtzMZGY8Ct5+mliZxU/Ww=="],

    "unstorage/chokidar": ["chokidar@5.0.0", "", { "dependencies": { "readdirp": "^5.0.0" } }, "sha512-TQMmc3w+5AxjpL8iIiwebF73dRDF4fBIieAqGn9RGCWaEVwQ6Fb2cGe31Yns0RRIzii5goJ1Y7xbMwo1TxMplw=="],

    "untun/citty": ["citty@0.1.6", "", { "dependencies": { "consola": "^3.2.3" } }, "sha512-tskPPKEs8D2KPafUypv2gxwJP8h/OaJmC82QQGGDQcHvXX43xF2VDACcJVmZ0EuSxkpO9Kc4MlrA3q0+FG58AQ=="],

    "untun/pathe": ["pathe@1.1.2", "", {}, "sha512-whLdWMYL2TwI08hn8/ZqAbrVemu0LNaNNJZX73O6qaIdCTfXutsLhMkjdENX0qhsQ9uIimo4/aQOmXkoon2nDQ=="],

    "untyped/citty": ["citty@0.1.6", "", { "dependencies": { "consola": "^3.2.3" } }, "sha512-tskPPKEs8D2KPafUypv2gxwJP8h/OaJmC82QQGGDQcHvXX43xF2VDACcJVmZ0EuSxkpO9Kc4MlrA3q0+FG58AQ=="],

    "vite/esbuild": ["esbuild@0.25.12", "", { "optionalDependencies": { "@esbuild/aix-ppc64": "0.25.12", "@esbuild/android-arm": "0.25.12", "@esbuild/android-arm64": "0.25.12", "@esbuild/android-x64": "0.25.12", "@esbuild/darwin-arm64": "0.25.12", "@esbuild/darwin-x64": "0.25.12", "@esbuild/freebsd-arm64": "0.25.12", "@esbuild/freebsd-x64": "0.25.12", "@esbuild/linux-arm": "0.25.12", "@esbuild/linux-arm64": "0.25.12", "@esbuild/linux-ia32": "0.25.12", "@esbuild/linux-loong64": "0.25.12", "@esbuild/linux-mips64el": "0.25.12", "@esbuild/linux-ppc64": "0.25.12", "@esbuild/linux-riscv64": "0.25.12", "@esbuild/linux-s390x": "0.25.12", "@esbuild/linux-x64": "0.25.12", "@esbuild/netbsd-arm64": "0.25.12", "@esbuild/netbsd-x64": "0.25.12", "@esbuild/openbsd-arm64": "0.25.12", "@esbuild/openbsd-x64": "0.25.12", "@esbuild/openharmony-arm64": "0.25.12", "@esbuild/sunos-x64": "0.25.12", "@esbuild/win32-arm64": "0.25.12", "@esbuild/win32-ia32": "0.25.12", "@esbuild/win32-x64": "0.25.12" }, "bin": { "esbuild": "bin/esbuild" } }, "sha512-bbPBYYrtZbkt6Os6FiTLCTFxvq4tt3JKall1vRwshA3fdVztsLAatFaZobhkBC8/BrPetoa0oksYoKXoG4ryJg=="],

    "vite-dev-rpc/birpc": ["birpc@2.9.0", "", {}, "sha512-KrayHS5pBi69Xi9JmvoqrIgYGDkD6mcSe/i6YKi3w5kekCLzrX4+nawcXqrj2tIp50Kw/mT/s3p+GVK0A0sKxw=="],

    "vite-node/cac": ["cac@6.7.14", "", {}, "sha512-b6Ilus+c3RrdDk+JhLKUAQfzzgLEPy6wcXqS7f/xe1EETvsDP6GORG7SFuOs6cID5YkqchW/LXZbX5bc8j7ZcQ=="],

    "vite-node/es-module-lexer": ["es-module-lexer@2.0.0", "", {}, "sha512-5POEcUuZybH7IdmGsD8wlf0AI55wMecM9rVBTI/qEAy2c1kTOm3DjFYjrBdI2K3BaJjJYfYFeRtM0t9ssnRuxw=="],

    "vite-node/vite": ["vite@7.3.1", "", { "dependencies": { "esbuild": "^0.27.0", "fdir": "^6.5.0", "picomatch": "^4.0.3", "postcss": "^8.5.6", "rollup": "^4.43.0", "tinyglobby": "^0.2.15" }, "optionalDependencies": { "fsevents": "~2.3.3" }, "peerDependencies": { "@types/node": "^20.19.0 || >=22.12.0", "jiti": ">=1.21.0", "less": "^4.0.0", "lightningcss": "^1.21.0", "sass": "^1.70.0", "sass-embedded": "^1.70.0", "stylus": ">=0.54.8", "sugarss": "^5.0.0", "terser": "^5.16.0", "tsx": "^4.8.1", "yaml": "^2.4.2" }, "optionalPeers": ["@types/node", "jiti", "less", "lightningcss", "sass", "sass-embedded", "stylus", "sugarss", "terser", "tsx", "yaml"], "bin": { "vite": "bin/vite.js" } }, "sha512-w+N7Hifpc3gRjZ63vYBXA56dvvRlNWRczTdmCBBa+CotUzAPf5b7YMdMR/8CQoeYE5LX3W4wj6RYTgonm1b9DA=="],

    "vite-plugin-inspect/error-stack-parser-es": ["error-stack-parser-es@0.1.5", "", {}, "sha512-xHku1X40RO+fO8yJ8Wh2f2rZWVjqyhb1zgq1yZ8aZRQkv6OOKhKWRUaht3eSCUbAOBaKIgM+ykwFLE+QUxgGeg=="],

    "vite-plugin-inspect/perfect-debounce": ["perfect-debounce@1.0.0", "", {}, "sha512-xCy9V055GLEqoFaHoC1SoLIaLmWctgCUaBaWxDZ7/Zx4CTyX7cJQLJOok/orfjZAh9kEYpjJa4d0KcJmCbctZA=="],

    "vscode-json-languageservice/jsonc-parser": ["jsonc-parser@3.3.1", "", {}, "sha512-HUgH65KyejrUFPvHFPbqOY0rsFip3Bo5wb4ngvdi1EpCYWUQDC5V+Y7mZws+DLkr4M//zQJoanu1SP+87Dv1oQ=="],

    "vue-router/chokidar": ["chokidar@5.0.0", "", { "dependencies": { "readdirp": "^5.0.0" } }, "sha512-TQMmc3w+5AxjpL8iIiwebF73dRDF4fBIieAqGn9RGCWaEVwQ6Fb2cGe31Yns0RRIzii5goJ1Y7xbMwo1TxMplw=="],

    "widest-line/string-width": ["string-width@7.2.0", "", { "dependencies": { "emoji-regex": "^10.3.0", "get-east-asian-width": "^1.0.0", "strip-ansi": "^7.1.0" } }, "sha512-tsaTIkKW9b4N+AEj+SVA+WhJzV7/zMhcSu78mLKWSk7cXMOSHsBKFWUs0fWwq8QyK3MgJBQRX6Gbi4kYbdvGkQ=="],

    "wrap-ansi/string-width": ["string-width@7.2.0", "", { "dependencies": { "emoji-regex": "^10.3.0", "get-east-asian-width": "^1.0.0", "strip-ansi": "^7.1.0" } }, "sha512-tsaTIkKW9b4N+AEj+SVA+WhJzV7/zMhcSu78mLKWSk7cXMOSHsBKFWUs0fWwq8QyK3MgJBQRX6Gbi4kYbdvGkQ=="],

    "wrap-ansi/strip-ansi": ["strip-ansi@7.2.0", "", { "dependencies": { "ansi-regex": "^6.2.2" } }, "sha512-yDPMNjp4WyfYBkHnjIRLfca1i6KMyGCtsVgoKe/z1+6vukgaENdgGBZt+ZmKPc4gavvEZ5OgHfHdrazhgNyG7w=="],

    "wrap-ansi-cjs/ansi-styles": ["ansi-styles@4.3.0", "", { "dependencies": { "color-convert": "^2.0.1" } }, "sha512-zbB9rCJAT1rbjiVDb2hqKFHNYLxgtk8NURxZ3IZwD3F6NtxbXZQCnnSi1Lkx+IDohdPlFp222wVALIheZJQSEg=="],

    "yaml-language-server/request-light": ["request-light@0.5.8", "", {}, "sha512-3Zjgh+8b5fhRJBQZoy+zbVKpAQGLyka0MPgW3zruTF4dFFJ8Fqcfu9YsAvi/rvdcaTeWG3MkbZv4WKxAn/84Lg=="],

    "yaml-language-server/yaml": ["yaml@2.7.1", "", { "bin": { "yaml": "bin.mjs" } }, "sha512-10ULxpnOCQXxJvBgxsn9ptjq6uviG/htZKk9veJGhlqn3w/DxQ631zFF+nlQXLwmImeS5amR2dl2U8sg6U9jsQ=="],

    "@babel/core/@babel/types/@babel/helper-string-parser": ["@babel/helper-string-parser@7.27.1", "", {}, "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA=="],

    "@babel/core/@babel/types/@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "@babel/generator/@babel/types/@babel/helper-string-parser": ["@babel/helper-string-parser@7.27.1", "", {}, "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA=="],

    "@babel/generator/@babel/types/@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "@babel/helper-annotate-as-pure/@babel/types/@babel/helper-string-parser": ["@babel/helper-string-parser@7.27.1", "", {}, "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA=="],

    "@babel/helper-annotate-as-pure/@babel/types/@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "@babel/helper-member-expression-to-functions/@babel/types/@babel/helper-string-parser": ["@babel/helper-string-parser@7.27.1", "", {}, "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA=="],

    "@babel/helper-member-expression-to-functions/@babel/types/@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "@babel/helper-module-imports/@babel/types/@babel/helper-string-parser": ["@babel/helper-string-parser@7.27.1", "", {}, "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA=="],

    "@babel/helper-module-imports/@babel/types/@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "@babel/helper-optimise-call-expression/@babel/types/@babel/helper-string-parser": ["@babel/helper-string-parser@7.27.1", "", {}, "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA=="],

    "@babel/helper-optimise-call-expression/@babel/types/@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "@babel/helper-skip-transparent-expression-wrappers/@babel/types/@babel/helper-string-parser": ["@babel/helper-string-parser@7.27.1", "", {}, "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA=="],

    "@babel/helper-skip-transparent-expression-wrappers/@babel/types/@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "@babel/helpers/@babel/types/@babel/helper-string-parser": ["@babel/helper-string-parser@7.27.1", "", {}, "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA=="],

    "@babel/helpers/@babel/types/@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "@babel/template/@babel/types/@babel/helper-string-parser": ["@babel/helper-string-parser@7.27.1", "", {}, "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA=="],

    "@babel/template/@babel/types/@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "@babel/traverse/@babel/types/@babel/helper-string-parser": ["@babel/helper-string-parser@7.27.1", "", {}, "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA=="],

    "@babel/traverse/@babel/types/@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "@dxup/nuxt/chokidar/readdirp": ["readdirp@5.0.0", "", {}, "sha512-9u/XQ1pvrQtYyMpZe7DXKv2p5CNvyVwzUB6uhLAnQwHMSgKMBR62lc7AHljaeteeHXn11XTAaLLUVZYVZyuRBQ=="],

    "@isaacs/cliui/string-width/emoji-regex": ["emoji-regex@9.2.2", "", {}, "sha512-L18DaJsXSUk2+42pv8mLs5jJT2hqFkFE4j21wOmgbUqsZ2hL72NsUU785g9RXgo3s0ZNgVl42TiHp3ZtOv/Vyg=="],

    "@isaacs/cliui/strip-ansi/ansi-regex": ["ansi-regex@6.2.2", "", {}, "sha512-Bq3SmSpyFHaWjPk8If9yc6svM8c56dB5BAtW4Qbw5jHTwwXXcTLoRMkpDJp6VL0XzlWaCHTXrkFURMYmD0sLqg=="],

    "@nuxt/devtools-kit/execa/get-stream": ["get-stream@8.0.1", "", {}, "sha512-VaUJspBffn/LMCJVoMvSAdmscJyS1auj5Zulnn5UoYcY531UWmdwhRWkcGKnGU93m5HSXP9LP2usOryrBtQowA=="],

    "@nuxt/devtools-kit/execa/human-signals": ["human-signals@5.0.0", "", {}, "sha512-AXcZb6vzzrFAUE61HnN4mpLqd/cSIwNQjtNWR0euPm6y0iqx3G4gOXaIDdtdDwZmhwe82LA6+zinmW4UBWVePQ=="],

    "@nuxt/devtools-kit/execa/is-stream": ["is-stream@3.0.0", "", {}, "sha512-LnQR4bZ9IADDRSkvpqMGvt/tEJWclzklNgSw48V5EAaAeDd6qGvN8ei6k5p0tvxSR171VmGyHuTiAOfxAbr8kA=="],

    "@nuxt/devtools-kit/execa/npm-run-path": ["npm-run-path@5.3.0", "", { "dependencies": { "path-key": "^4.0.0" } }, "sha512-ppwTtiJZq0O/ai0z7yfudtBpWIoxM8yE6nHi1X47eFR2EWORqfbu6CnPlNsjeN683eT0qG6H/Pyf9fCcvjnnnQ=="],

    "@nuxt/devtools-kit/execa/strip-final-newline": ["strip-final-newline@3.0.0", "", {}, "sha512-dOESqjYr96iWYylGObzd39EuNTa5VJxyvVAEm5Jnh7KGo75V43Hk1odPQkNDyXNmUR6k+gEiDVXnjB8HJ3crXw=="],

    "@nuxt/devtools-wizard/execa/get-stream": ["get-stream@8.0.1", "", {}, "sha512-VaUJspBffn/LMCJVoMvSAdmscJyS1auj5Zulnn5UoYcY531UWmdwhRWkcGKnGU93m5HSXP9LP2usOryrBtQowA=="],

    "@nuxt/devtools-wizard/execa/human-signals": ["human-signals@5.0.0", "", {}, "sha512-AXcZb6vzzrFAUE61HnN4mpLqd/cSIwNQjtNWR0euPm6y0iqx3G4gOXaIDdtdDwZmhwe82LA6+zinmW4UBWVePQ=="],

    "@nuxt/devtools-wizard/execa/is-stream": ["is-stream@3.0.0", "", {}, "sha512-LnQR4bZ9IADDRSkvpqMGvt/tEJWclzklNgSw48V5EAaAeDd6qGvN8ei6k5p0tvxSR171VmGyHuTiAOfxAbr8kA=="],

    "@nuxt/devtools-wizard/execa/npm-run-path": ["npm-run-path@5.3.0", "", { "dependencies": { "path-key": "^4.0.0" } }, "sha512-ppwTtiJZq0O/ai0z7yfudtBpWIoxM8yE6nHi1X47eFR2EWORqfbu6CnPlNsjeN683eT0qG6H/Pyf9fCcvjnnnQ=="],

    "@nuxt/devtools-wizard/execa/strip-final-newline": ["strip-final-newline@3.0.0", "", {}, "sha512-dOESqjYr96iWYylGObzd39EuNTa5VJxyvVAEm5Jnh7KGo75V43Hk1odPQkNDyXNmUR6k+gEiDVXnjB8HJ3crXw=="],

    "@nuxt/devtools/@vue/devtools-core/@vue/devtools-shared": ["@vue/devtools-shared@8.1.0", "", {}, "sha512-h8uCb4Qs8UT8VdTT5yjY6tOJ//qH7EpxToixR0xqejR55t5OdISIg7AJ7eBkhBs8iu1qG5gY3QQNN1DF1EelAA=="],

    "@nuxt/devtools/@vue/devtools-kit/@vue/devtools-shared": ["@vue/devtools-shared@8.1.0", "", {}, "sha512-h8uCb4Qs8UT8VdTT5yjY6tOJ//qH7EpxToixR0xqejR55t5OdISIg7AJ7eBkhBs8iu1qG5gY3QQNN1DF1EelAA=="],

    "@nuxt/devtools/@vue/devtools-kit/birpc": ["birpc@2.9.0", "", {}, "sha512-KrayHS5pBi69Xi9JmvoqrIgYGDkD6mcSe/i6YKi3w5kekCLzrX4+nawcXqrj2tIp50Kw/mT/s3p+GVK0A0sKxw=="],

    "@nuxt/devtools/@vue/devtools-kit/hookable": ["hookable@5.5.3", "", {}, "sha512-Yc+BQe8SvoXH1643Qez1zqLRmbA5rCL+sSmk6TVos0LWVfNIB7PGncdlId77WzLGSIB5KaWgTaNTs2lNVEI6VQ=="],

    "@nuxt/devtools/execa/get-stream": ["get-stream@8.0.1", "", {}, "sha512-VaUJspBffn/LMCJVoMvSAdmscJyS1auj5Zulnn5UoYcY531UWmdwhRWkcGKnGU93m5HSXP9LP2usOryrBtQowA=="],

    "@nuxt/devtools/execa/human-signals": ["human-signals@5.0.0", "", {}, "sha512-AXcZb6vzzrFAUE61HnN4mpLqd/cSIwNQjtNWR0euPm6y0iqx3G4gOXaIDdtdDwZmhwe82LA6+zinmW4UBWVePQ=="],

    "@nuxt/devtools/execa/is-stream": ["is-stream@3.0.0", "", {}, "sha512-LnQR4bZ9IADDRSkvpqMGvt/tEJWclzklNgSw48V5EAaAeDd6qGvN8ei6k5p0tvxSR171VmGyHuTiAOfxAbr8kA=="],

    "@nuxt/devtools/execa/npm-run-path": ["npm-run-path@5.3.0", "", { "dependencies": { "path-key": "^4.0.0" } }, "sha512-ppwTtiJZq0O/ai0z7yfudtBpWIoxM8yE6nHi1X47eFR2EWORqfbu6CnPlNsjeN683eT0qG6H/Pyf9fCcvjnnnQ=="],

    "@nuxt/devtools/execa/strip-final-newline": ["strip-final-newline@3.0.0", "", {}, "sha512-dOESqjYr96iWYylGObzd39EuNTa5VJxyvVAEm5Jnh7KGo75V43Hk1odPQkNDyXNmUR6k+gEiDVXnjB8HJ3crXw=="],

    "@nuxt/vite-builder/@vitejs/plugin-vue/@rolldown/pluginutils": ["@rolldown/pluginutils@1.0.0-rc.2", "", {}, "sha512-izyXV/v+cHiRfozX62W9htOAvwMo4/bXKDrQ+vom1L1qRuexPock/7VZDAhnpHCLNejd3NJ6hiab+tO0D44Rgw=="],

    "@nuxt/vite-builder/@vitejs/plugin-vue-jsx/@vue/babel-plugin-jsx": ["@vue/babel-plugin-jsx@2.0.1", "", { "dependencies": { "@babel/helper-module-imports": "^7.27.1", "@babel/helper-plugin-utils": "^7.27.1", "@babel/plugin-syntax-jsx": "^7.27.1", "@babel/template": "^7.27.2", "@babel/traverse": "^7.28.4", "@babel/types": "^7.28.4", "@vue/babel-helper-vue-transform-on": "2.0.1", "@vue/babel-plugin-resolve-type": "2.0.1", "@vue/shared": "^3.5.22" }, "peerDependencies": { "@babel/core": "^7.0.0-0" }, "optionalPeers": ["@babel/core"] }, "sha512-a8CaLQjD/s4PVdhrLD/zT574ZNPnZBOY+IhdtKWRB4HRZ0I2tXBi5ne7d9eCfaYwp5gU5+4KIyFTV1W1YL9xZA=="],

    "@types/babel__core/@babel/types/@babel/helper-string-parser": ["@babel/helper-string-parser@7.27.1", "", {}, "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA=="],

    "@types/babel__core/@babel/types/@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "@types/babel__generator/@babel/types/@babel/helper-string-parser": ["@babel/helper-string-parser@7.27.1", "", {}, "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA=="],

    "@types/babel__generator/@babel/types/@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "@types/babel__template/@babel/types/@babel/helper-string-parser": ["@babel/helper-string-parser@7.27.1", "", {}, "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA=="],

    "@types/babel__template/@babel/types/@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "@types/babel__traverse/@babel/types/@babel/helper-string-parser": ["@babel/helper-string-parser@7.27.1", "", {}, "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA=="],

    "@types/babel__traverse/@babel/types/@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "@vue-macros/common/ast-kit/@babel/parser": ["@babel/parser@7.29.2", "", { "dependencies": { "@babel/types": "^7.29.0" }, "bin": "./bin/babel-parser.js" }, "sha512-4GgRzy/+fsBa72/RZVJmGKPmZu9Byn8o4MoLpmNe1m8ZfYnz5emHLQz3U4gLud6Zwl0RZIcgiLD7Uq7ySFuDLA=="],

    "@vue/babel-plugin-jsx/@babel/types/@babel/helper-string-parser": ["@babel/helper-string-parser@7.27.1", "", {}, "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA=="],

    "@vue/babel-plugin-jsx/@babel/types/@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "@vue/babel-plugin-resolve-type/@babel/parser/@babel/types": ["@babel/types@7.29.0", "", { "dependencies": { "@babel/helper-string-parser": "^7.27.1", "@babel/helper-validator-identifier": "^7.28.5" } }, "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A=="],

    "@vue/compiler-core/@babel/parser/@babel/types": ["@babel/types@7.29.0", "", { "dependencies": { "@babel/helper-string-parser": "^7.27.1", "@babel/helper-validator-identifier": "^7.28.5" } }, "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A=="],

    "@vue/compiler-sfc/@babel/parser/@babel/types": ["@babel/types@7.29.0", "", { "dependencies": { "@babel/helper-string-parser": "^7.27.1", "@babel/helper-validator-identifier": "^7.28.5" } }, "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A=="],

    "@vue/devtools-api/@vue/devtools-kit/@vue/devtools-shared": ["@vue/devtools-shared@8.1.0", "", {}, "sha512-h8uCb4Qs8UT8VdTT5yjY6tOJ//qH7EpxToixR0xqejR55t5OdISIg7AJ7eBkhBs8iu1qG5gY3QQNN1DF1EelAA=="],

    "@vue/devtools-api/@vue/devtools-kit/birpc": ["birpc@2.9.0", "", {}, "sha512-KrayHS5pBi69Xi9JmvoqrIgYGDkD6mcSe/i6YKi3w5kekCLzrX4+nawcXqrj2tIp50Kw/mT/s3p+GVK0A0sKxw=="],

    "@vue/devtools-api/@vue/devtools-kit/hookable": ["hookable@5.5.3", "", {}, "sha512-Yc+BQe8SvoXH1643Qez1zqLRmbA5rCL+sSmk6TVos0LWVfNIB7PGncdlId77WzLGSIB5KaWgTaNTs2lNVEI6VQ=="],

    "archiver-utils/glob/minimatch": ["minimatch@9.0.9", "", { "dependencies": { "brace-expansion": "^2.0.2" } }, "sha512-OBwBN9AL4dqmETlpS2zasx+vTeWclWzkblfZk7KTA5j3jeOONz/tRCnZomUyvNg83wL5Zv9Ss6HMJXAgL8R2Yg=="],

    "archiver-utils/glob/path-scurry": ["path-scurry@1.11.1", "", { "dependencies": { "lru-cache": "^10.2.0", "minipass": "^5.0.0 || ^6.0.2 || ^7.0.0" } }, "sha512-Xa4Nw17FS9ApQFJ9umLiJS4orGjm7ZzwUrwamcGQuHSzDyth9boKDaycYdDcZDuqYATXw4HFXgaqWTctW/v1HA=="],

    "ast-walker-scope/@babel/parser/@babel/types": ["@babel/types@7.29.0", "", { "dependencies": { "@babel/helper-string-parser": "^7.27.1", "@babel/helper-validator-identifier": "^7.28.5" } }, "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A=="],

    "boxen/string-width/emoji-regex": ["emoji-regex@10.6.0", "", {}, "sha512-toUI84YS5YmxW219erniWD0CIVOo46xGKColeNQRgOzDorgBi1v4D71/OFzgD9GO2UGKIv1C3Sp8DAn0+j5w7A=="],

    "boxen/string-width/strip-ansi": ["strip-ansi@7.2.0", "", { "dependencies": { "ansi-regex": "^6.2.2" } }, "sha512-yDPMNjp4WyfYBkHnjIRLfca1i6KMyGCtsVgoKe/z1+6vukgaENdgGBZt+ZmKPc4gavvEZ5OgHfHdrazhgNyG7w=="],

    "c12/chokidar/readdirp": ["readdirp@5.0.0", "", {}, "sha512-9u/XQ1pvrQtYyMpZe7DXKv2p5CNvyVwzUB6uhLAnQwHMSgKMBR62lc7AHljaeteeHXn11XTAaLLUVZYVZyuRBQ=="],

    "c12/giget/citty": ["citty@0.1.6", "", { "dependencies": { "consola": "^3.2.3" } }, "sha512-tskPPKEs8D2KPafUypv2gxwJP8h/OaJmC82QQGGDQcHvXX43xF2VDACcJVmZ0EuSxkpO9Kc4MlrA3q0+FG58AQ=="],

    "clipboardy/execa/get-stream": ["get-stream@8.0.1", "", {}, "sha512-VaUJspBffn/LMCJVoMvSAdmscJyS1auj5Zulnn5UoYcY531UWmdwhRWkcGKnGU93m5HSXP9LP2usOryrBtQowA=="],

    "clipboardy/execa/human-signals": ["human-signals@5.0.0", "", {}, "sha512-AXcZb6vzzrFAUE61HnN4mpLqd/cSIwNQjtNWR0euPm6y0iqx3G4gOXaIDdtdDwZmhwe82LA6+zinmW4UBWVePQ=="],

    "clipboardy/execa/is-stream": ["is-stream@3.0.0", "", {}, "sha512-LnQR4bZ9IADDRSkvpqMGvt/tEJWclzklNgSw48V5EAaAeDd6qGvN8ei6k5p0tvxSR171VmGyHuTiAOfxAbr8kA=="],

    "clipboardy/execa/npm-run-path": ["npm-run-path@5.3.0", "", { "dependencies": { "path-key": "^4.0.0" } }, "sha512-ppwTtiJZq0O/ai0z7yfudtBpWIoxM8yE6nHi1X47eFR2EWORqfbu6CnPlNsjeN683eT0qG6H/Pyf9fCcvjnnnQ=="],

    "clipboardy/execa/strip-final-newline": ["strip-final-newline@3.0.0", "", {}, "sha512-dOESqjYr96iWYylGObzd39EuNTa5VJxyvVAEm5Jnh7KGo75V43Hk1odPQkNDyXNmUR6k+gEiDVXnjB8HJ3crXw=="],

    "cliui/wrap-ansi/ansi-styles": ["ansi-styles@4.3.0", "", { "dependencies": { "color-convert": "^2.0.1" } }, "sha512-zbB9rCJAT1rbjiVDb2hqKFHNYLxgtk8NURxZ3IZwD3F6NtxbXZQCnnSi1Lkx+IDohdPlFp222wVALIheZJQSEg=="],

    "cross-spawn/which/isexe": ["isexe@2.0.0", "", {}, "sha512-RHxMLp9lnKHGHRng9QFhRCMbYAcVpn69smSGcq3f36xjgVVWThj4qqLbTLlq7Ssj8B+fIQ1EuCEGI2lKsyQeIw=="],

    "csso/css-tree/mdn-data": ["mdn-data@2.0.28", "", {}, "sha512-aylIc7Z9y4yzHYAJNuESG3hfhC+0Ibp/MAMiaOZgNv4pmEdFyfZhhhny4MNiAfWdBQ1RQ2mfDWmM1x8SvGyp8g=="],

    "lazystream/readable-stream/safe-buffer": ["safe-buffer@5.1.2", "", {}, "sha512-Gd2UZBJDkXlY7GbJxfsE8/nvKkUEU1G38c1siN6QP6a9PT9MmHB8GnpscSmMJSoF8LOIrt8ud/wPtojys4G6+g=="],

    "lazystream/readable-stream/string_decoder": ["string_decoder@1.1.1", "", { "dependencies": { "safe-buffer": "~5.1.0" } }, "sha512-n/ShnvDi6FHbbVfviro+WojiFzv+s8MPMHBczVePfUpDJLwoLT0ht1l4YwBCbi8pJAveEEdnkHyPyTP/mzRfwg=="],

    "magicast/@babel/types/@babel/helper-string-parser": ["@babel/helper-string-parser@7.27.1", "", {}, "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA=="],

    "magicast/@babel/types/@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "mlly/pkg-types/confbox": ["confbox@0.1.8", "", {}, "sha512-RMtmw0iFkeR4YV+fUOSucriAQNb9g8zFR52MWCtl+cCZOFRNL6zeB395vPzFhEjjn4fMxXudmELnl/KF/WrK6w=="],

    "nitropack/chokidar/readdirp": ["readdirp@5.0.0", "", {}, "sha512-9u/XQ1pvrQtYyMpZe7DXKv2p5CNvyVwzUB6uhLAnQwHMSgKMBR62lc7AHljaeteeHXn11XTAaLLUVZYVZyuRBQ=="],

    "nitropack/unimport/unplugin": ["unplugin@2.3.11", "", { "dependencies": { "@jridgewell/remapping": "^2.3.5", "acorn": "^8.15.0", "picomatch": "^4.0.3", "webpack-virtual-modules": "^0.6.2" } }, "sha512-5uKD0nqiYVzlmCRs01Fhs2BdkEgBS3SAVP6ndrBsuK42iC2+JHyxM05Rm9G8+5mkmRtzMZGY8Ct5+mliZxU/Ww=="],

    "nuxt/chokidar/readdirp": ["readdirp@5.0.0", "", {}, "sha512-9u/XQ1pvrQtYyMpZe7DXKv2p5CNvyVwzUB6uhLAnQwHMSgKMBR62lc7AHljaeteeHXn11XTAaLLUVZYVZyuRBQ=="],

    "nuxt/vue-router/@vue/devtools-api": ["@vue/devtools-api@6.6.4", "", {}, "sha512-sGhTPMuXqZ1rVOk32RylztWkfXTRhuS7vgAKv0zjqk8gbsHkJ7xfFf+jbySxt7tWObEJwyKaHMikV/WGDiQm8g=="],

    "readdir-glob/minimatch/brace-expansion": ["brace-expansion@2.0.2", "", { "dependencies": { "balanced-match": "^1.0.0" } }, "sha512-Jt0vHyM+jmUBqojB7E1NIYadt0vI0Qxjxd2TErW94wDz+E2LAm5vKMXXwg6ZZBTHPuUlDgQHKXvjGBdfcF1ZDQ=="],

    "rollup-plugin-visualizer/open/define-lazy-prop": ["define-lazy-prop@2.0.0", "", {}, "sha512-Ds09qNh8yw3khSjiJjiUInaGX9xlqZDY7JVryGxdxV7NPeuqQfplOpQ66yJFZut3jLa5zOwkXw1g9EI2uKh4Og=="],

    "rollup-plugin-visualizer/open/is-docker": ["is-docker@2.2.1", "", { "bin": { "is-docker": "cli.js" } }, "sha512-F+i2BKsFrH66iaUFc0woD8sLy8getkwTwtOBjvs56Cx4CgJDeKQeqfz8wAYiSb8JOprWhHH5p77PbmYCvvUuXQ=="],

    "rollup-plugin-visualizer/open/is-wsl": ["is-wsl@2.2.0", "", { "dependencies": { "is-docker": "^2.0.0" } }, "sha512-fKzAra0rGJUUBwGBgNkHZuToZcn+TtXHpeCgmkMJMMYx1sQDYaCSyjJBSCa2nH1DGm7s3n1oBnohoVTBaN7Lww=="],

    "unplugin-vue-router/chokidar/readdirp": ["readdirp@5.0.0", "", {}, "sha512-9u/XQ1pvrQtYyMpZe7DXKv2p5CNvyVwzUB6uhLAnQwHMSgKMBR62lc7AHljaeteeHXn11XTAaLLUVZYVZyuRBQ=="],

    "unstorage/chokidar/readdirp": ["readdirp@5.0.0", "", {}, "sha512-9u/XQ1pvrQtYyMpZe7DXKv2p5CNvyVwzUB6uhLAnQwHMSgKMBR62lc7AHljaeteeHXn11XTAaLLUVZYVZyuRBQ=="],

    "vite/esbuild/@esbuild/aix-ppc64": ["@esbuild/aix-ppc64@0.25.12", "", { "os": "aix", "cpu": "ppc64" }, "sha512-Hhmwd6CInZ3dwpuGTF8fJG6yoWmsToE+vYgD4nytZVxcu1ulHpUQRAB1UJ8+N1Am3Mz4+xOByoQoSZf4D+CpkA=="],

    "vite/esbuild/@esbuild/android-arm": ["@esbuild/android-arm@0.25.12", "", { "os": "android", "cpu": "arm" }, "sha512-VJ+sKvNA/GE7Ccacc9Cha7bpS8nyzVv0jdVgwNDaR4gDMC/2TTRc33Ip8qrNYUcpkOHUT5OZ0bUcNNVZQ9RLlg=="],

    "vite/esbuild/@esbuild/android-arm64": ["@esbuild/android-arm64@0.25.12", "", { "os": "android", "cpu": "arm64" }, "sha512-6AAmLG7zwD1Z159jCKPvAxZd4y/VTO0VkprYy+3N2FtJ8+BQWFXU+OxARIwA46c5tdD9SsKGZ/1ocqBS/gAKHg=="],

    "vite/esbuild/@esbuild/android-x64": ["@esbuild/android-x64@0.25.12", "", { "os": "android", "cpu": "x64" }, "sha512-5jbb+2hhDHx5phYR2By8GTWEzn6I9UqR11Kwf22iKbNpYrsmRB18aX/9ivc5cabcUiAT/wM+YIZ6SG9QO6a8kg=="],

    "vite/esbuild/@esbuild/darwin-arm64": ["@esbuild/darwin-arm64@0.25.12", "", { "os": "darwin", "cpu": "arm64" }, "sha512-N3zl+lxHCifgIlcMUP5016ESkeQjLj/959RxxNYIthIg+CQHInujFuXeWbWMgnTo4cp5XVHqFPmpyu9J65C1Yg=="],

    "vite/esbuild/@esbuild/darwin-x64": ["@esbuild/darwin-x64@0.25.12", "", { "os": "darwin", "cpu": "x64" }, "sha512-HQ9ka4Kx21qHXwtlTUVbKJOAnmG1ipXhdWTmNXiPzPfWKpXqASVcWdnf2bnL73wgjNrFXAa3yYvBSd9pzfEIpA=="],

    "vite/esbuild/@esbuild/freebsd-arm64": ["@esbuild/freebsd-arm64@0.25.12", "", { "os": "freebsd", "cpu": "arm64" }, "sha512-gA0Bx759+7Jve03K1S0vkOu5Lg/85dou3EseOGUes8flVOGxbhDDh/iZaoek11Y8mtyKPGF3vP8XhnkDEAmzeg=="],

    "vite/esbuild/@esbuild/freebsd-x64": ["@esbuild/freebsd-x64@0.25.12", "", { "os": "freebsd", "cpu": "x64" }, "sha512-TGbO26Yw2xsHzxtbVFGEXBFH0FRAP7gtcPE7P5yP7wGy7cXK2oO7RyOhL5NLiqTlBh47XhmIUXuGciXEqYFfBQ=="],

    "vite/esbuild/@esbuild/linux-arm": ["@esbuild/linux-arm@0.25.12", "", { "os": "linux", "cpu": "arm" }, "sha512-lPDGyC1JPDou8kGcywY0YILzWlhhnRjdof3UlcoqYmS9El818LLfJJc3PXXgZHrHCAKs/Z2SeZtDJr5MrkxtOw=="],

    "vite/esbuild/@esbuild/linux-arm64": ["@esbuild/linux-arm64@0.25.12", "", { "os": "linux", "cpu": "arm64" }, "sha512-8bwX7a8FghIgrupcxb4aUmYDLp8pX06rGh5HqDT7bB+8Rdells6mHvrFHHW2JAOPZUbnjUpKTLg6ECyzvas2AQ=="],

    "vite/esbuild/@esbuild/linux-ia32": ["@esbuild/linux-ia32@0.25.12", "", { "os": "linux", "cpu": "ia32" }, "sha512-0y9KrdVnbMM2/vG8KfU0byhUN+EFCny9+8g202gYqSSVMonbsCfLjUO+rCci7pM0WBEtz+oK/PIwHkzxkyharA=="],

    "vite/esbuild/@esbuild/linux-loong64": ["@esbuild/linux-loong64@0.25.12", "", { "os": "linux", "cpu": "none" }, "sha512-h///Lr5a9rib/v1GGqXVGzjL4TMvVTv+s1DPoxQdz7l/AYv6LDSxdIwzxkrPW438oUXiDtwM10o9PmwS/6Z0Ng=="],

    "vite/esbuild/@esbuild/linux-mips64el": ["@esbuild/linux-mips64el@0.25.12", "", { "os": "linux", "cpu": "none" }, "sha512-iyRrM1Pzy9GFMDLsXn1iHUm18nhKnNMWscjmp4+hpafcZjrr2WbT//d20xaGljXDBYHqRcl8HnxbX6uaA/eGVw=="],

    "vite/esbuild/@esbuild/linux-ppc64": ["@esbuild/linux-ppc64@0.25.12", "", { "os": "linux", "cpu": "ppc64" }, "sha512-9meM/lRXxMi5PSUqEXRCtVjEZBGwB7P/D4yT8UG/mwIdze2aV4Vo6U5gD3+RsoHXKkHCfSxZKzmDssVlRj1QQA=="],

    "vite/esbuild/@esbuild/linux-riscv64": ["@esbuild/linux-riscv64@0.25.12", "", { "os": "linux", "cpu": "none" }, "sha512-Zr7KR4hgKUpWAwb1f3o5ygT04MzqVrGEGXGLnj15YQDJErYu/BGg+wmFlIDOdJp0PmB0lLvxFIOXZgFRrdjR0w=="],

    "vite/esbuild/@esbuild/linux-s390x": ["@esbuild/linux-s390x@0.25.12", "", { "os": "linux", "cpu": "s390x" }, "sha512-MsKncOcgTNvdtiISc/jZs/Zf8d0cl/t3gYWX8J9ubBnVOwlk65UIEEvgBORTiljloIWnBzLs4qhzPkJcitIzIg=="],

    "vite/esbuild/@esbuild/linux-x64": ["@esbuild/linux-x64@0.25.12", "", { "os": "linux", "cpu": "x64" }, "sha512-uqZMTLr/zR/ed4jIGnwSLkaHmPjOjJvnm6TVVitAa08SLS9Z0VM8wIRx7gWbJB5/J54YuIMInDquWyYvQLZkgw=="],

    "vite/esbuild/@esbuild/netbsd-arm64": ["@esbuild/netbsd-arm64@0.25.12", "", { "os": "none", "cpu": "arm64" }, "sha512-xXwcTq4GhRM7J9A8Gv5boanHhRa/Q9KLVmcyXHCTaM4wKfIpWkdXiMog/KsnxzJ0A1+nD+zoecuzqPmCRyBGjg=="],

    "vite/esbuild/@esbuild/netbsd-x64": ["@esbuild/netbsd-x64@0.25.12", "", { "os": "none", "cpu": "x64" }, "sha512-Ld5pTlzPy3YwGec4OuHh1aCVCRvOXdH8DgRjfDy/oumVovmuSzWfnSJg+VtakB9Cm0gxNO9BzWkj6mtO1FMXkQ=="],

    "vite/esbuild/@esbuild/openbsd-arm64": ["@esbuild/openbsd-arm64@0.25.12", "", { "os": "openbsd", "cpu": "arm64" }, "sha512-fF96T6KsBo/pkQI950FARU9apGNTSlZGsv1jZBAlcLL1MLjLNIWPBkj5NlSz8aAzYKg+eNqknrUJ24QBybeR5A=="],

    "vite/esbuild/@esbuild/openbsd-x64": ["@esbuild/openbsd-x64@0.25.12", "", { "os": "openbsd", "cpu": "x64" }, "sha512-MZyXUkZHjQxUvzK7rN8DJ3SRmrVrke8ZyRusHlP+kuwqTcfWLyqMOE3sScPPyeIXN/mDJIfGXvcMqCgYKekoQw=="],

    "vite/esbuild/@esbuild/openharmony-arm64": ["@esbuild/openharmony-arm64@0.25.12", "", { "os": "none", "cpu": "arm64" }, "sha512-rm0YWsqUSRrjncSXGA7Zv78Nbnw4XL6/dzr20cyrQf7ZmRcsovpcRBdhD43Nuk3y7XIoW2OxMVvwuRvk9XdASg=="],

    "vite/esbuild/@esbuild/sunos-x64": ["@esbuild/sunos-x64@0.25.12", "", { "os": "sunos", "cpu": "x64" }, "sha512-3wGSCDyuTHQUzt0nV7bocDy72r2lI33QL3gkDNGkod22EsYl04sMf0qLb8luNKTOmgF/eDEDP5BFNwoBKH441w=="],

    "vite/esbuild/@esbuild/win32-arm64": ["@esbuild/win32-arm64@0.25.12", "", { "os": "win32", "cpu": "arm64" }, "sha512-rMmLrur64A7+DKlnSuwqUdRKyd3UE7oPJZmnljqEptesKM8wx9J8gx5u0+9Pq0fQQW8vqeKebwNXdfOyP+8Bsg=="],

    "vite/esbuild/@esbuild/win32-ia32": ["@esbuild/win32-ia32@0.25.12", "", { "os": "win32", "cpu": "ia32" }, "sha512-HkqnmmBoCbCwxUKKNPBixiWDGCpQGVsrQfJoVGYLPT41XWF8lHuE5N6WhVia2n4o5QK5M4tYr21827fNhi4byQ=="],

    "vite/esbuild/@esbuild/win32-x64": ["@esbuild/win32-x64@0.25.12", "", { "os": "win32", "cpu": "x64" }, "sha512-alJC0uCZpTFrSL0CCDjcgleBXPnCrEAhTBILpeAp7M/OFgoqtAetfBzX0xM00MUsVVPpVjlPuMbREqnZCXaTnA=="],

    "vue-router/chokidar/readdirp": ["readdirp@5.0.0", "", {}, "sha512-9u/XQ1pvrQtYyMpZe7DXKv2p5CNvyVwzUB6uhLAnQwHMSgKMBR62lc7AHljaeteeHXn11XTAaLLUVZYVZyuRBQ=="],

    "widest-line/string-width/emoji-regex": ["emoji-regex@10.6.0", "", {}, "sha512-toUI84YS5YmxW219erniWD0CIVOo46xGKColeNQRgOzDorgBi1v4D71/OFzgD9GO2UGKIv1C3Sp8DAn0+j5w7A=="],

    "widest-line/string-width/strip-ansi": ["strip-ansi@7.2.0", "", { "dependencies": { "ansi-regex": "^6.2.2" } }, "sha512-yDPMNjp4WyfYBkHnjIRLfca1i6KMyGCtsVgoKe/z1+6vukgaENdgGBZt+ZmKPc4gavvEZ5OgHfHdrazhgNyG7w=="],

    "wrap-ansi/string-width/emoji-regex": ["emoji-regex@10.6.0", "", {}, "sha512-toUI84YS5YmxW219erniWD0CIVOo46xGKColeNQRgOzDorgBi1v4D71/OFzgD9GO2UGKIv1C3Sp8DAn0+j5w7A=="],

    "wrap-ansi/strip-ansi/ansi-regex": ["ansi-regex@6.2.2", "", {}, "sha512-Bq3SmSpyFHaWjPk8If9yc6svM8c56dB5BAtW4Qbw5jHTwwXXcTLoRMkpDJp6VL0XzlWaCHTXrkFURMYmD0sLqg=="],

    "@nuxt/devtools-kit/execa/npm-run-path/path-key": ["path-key@4.0.0", "", {}, "sha512-haREypq7xkM7ErfgIyA0z+Bj4AGKlMSdlQE2jvJo6huWD1EdkKYV+G/T4nq0YEF2vgTT8kqMFKo1uHn950r4SQ=="],

    "@nuxt/devtools-wizard/execa/npm-run-path/path-key": ["path-key@4.0.0", "", {}, "sha512-haREypq7xkM7ErfgIyA0z+Bj4AGKlMSdlQE2jvJo6huWD1EdkKYV+G/T4nq0YEF2vgTT8kqMFKo1uHn950r4SQ=="],

    "@nuxt/devtools/execa/npm-run-path/path-key": ["path-key@4.0.0", "", {}, "sha512-haREypq7xkM7ErfgIyA0z+Bj4AGKlMSdlQE2jvJo6huWD1EdkKYV+G/T4nq0YEF2vgTT8kqMFKo1uHn950r4SQ=="],

    "@nuxt/vite-builder/@vitejs/plugin-vue-jsx/@vue/babel-plugin-jsx/@babel/types": ["@babel/types@7.29.0", "", { "dependencies": { "@babel/helper-string-parser": "^7.27.1", "@babel/helper-validator-identifier": "^7.28.5" } }, "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A=="],

    "@nuxt/vite-builder/@vitejs/plugin-vue-jsx/@vue/babel-plugin-jsx/@vue/babel-helper-vue-transform-on": ["@vue/babel-helper-vue-transform-on@2.0.1", "", {}, "sha512-uZ66EaFbnnZSYqYEyplWvn46GhZ1KuYSThdT68p+am7MgBNbQ3hphTL9L+xSIsWkdktwhPYLwPgVWqo96jDdRA=="],

    "@nuxt/vite-builder/@vitejs/plugin-vue-jsx/@vue/babel-plugin-jsx/@vue/babel-plugin-resolve-type": ["@vue/babel-plugin-resolve-type@2.0.1", "", { "dependencies": { "@babel/code-frame": "^7.27.1", "@babel/helper-module-imports": "^7.27.1", "@babel/helper-plugin-utils": "^7.27.1", "@babel/parser": "^7.28.4", "@vue/compiler-sfc": "^3.5.22" }, "peerDependencies": { "@babel/core": "^7.0.0-0" } }, "sha512-ybwgIuRGRRBhOU37GImDoWQoz+TlSqap65qVI6iwg/J7FfLTLmMf97TS7xQH9I7Qtr/gp161kYVdhr1ZMraSYQ=="],

    "@vue-macros/common/ast-kit/@babel/parser/@babel/types": ["@babel/types@7.29.0", "", { "dependencies": { "@babel/helper-string-parser": "^7.27.1", "@babel/helper-validator-identifier": "^7.28.5" } }, "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A=="],

    "@vue/babel-plugin-resolve-type/@babel/parser/@babel/types/@babel/helper-string-parser": ["@babel/helper-string-parser@7.27.1", "", {}, "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA=="],

    "@vue/babel-plugin-resolve-type/@babel/parser/@babel/types/@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "@vue/compiler-core/@babel/parser/@babel/types/@babel/helper-string-parser": ["@babel/helper-string-parser@7.27.1", "", {}, "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA=="],

    "@vue/compiler-core/@babel/parser/@babel/types/@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "@vue/compiler-sfc/@babel/parser/@babel/types/@babel/helper-string-parser": ["@babel/helper-string-parser@7.27.1", "", {}, "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA=="],

    "@vue/compiler-sfc/@babel/parser/@babel/types/@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "archiver-utils/glob/minimatch/brace-expansion": ["brace-expansion@2.0.2", "", { "dependencies": { "balanced-match": "^1.0.0" } }, "sha512-Jt0vHyM+jmUBqojB7E1NIYadt0vI0Qxjxd2TErW94wDz+E2LAm5vKMXXwg6ZZBTHPuUlDgQHKXvjGBdfcF1ZDQ=="],

    "archiver-utils/glob/path-scurry/lru-cache": ["lru-cache@10.4.3", "", {}, "sha512-JNAzZcXrCt42VGLuYz0zfAzDfAvJWW6AfYlDBQyDV5DClI2m5sAmK+OIO7s59XfsRsWHp02jAJrRadPRGTt6SQ=="],

    "ast-walker-scope/@babel/parser/@babel/types/@babel/helper-string-parser": ["@babel/helper-string-parser@7.27.1", "", {}, "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA=="],

    "ast-walker-scope/@babel/parser/@babel/types/@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "boxen/string-width/strip-ansi/ansi-regex": ["ansi-regex@6.2.2", "", {}, "sha512-Bq3SmSpyFHaWjPk8If9yc6svM8c56dB5BAtW4Qbw5jHTwwXXcTLoRMkpDJp6VL0XzlWaCHTXrkFURMYmD0sLqg=="],

    "clipboardy/execa/npm-run-path/path-key": ["path-key@4.0.0", "", {}, "sha512-haREypq7xkM7ErfgIyA0z+Bj4AGKlMSdlQE2jvJo6huWD1EdkKYV+G/T4nq0YEF2vgTT8kqMFKo1uHn950r4SQ=="],

    "readdir-glob/minimatch/brace-expansion/balanced-match": ["balanced-match@1.0.2", "", {}, "sha512-3oSeUO0TMV67hN1AmbXsK4yaqU7tjiHlbxRDZOpH0KW9+CeX4bRAaX0Anxt0tx2MrpRpWwQaPwIlISEJhYU5Pw=="],

    "widest-line/string-width/strip-ansi/ansi-regex": ["ansi-regex@6.2.2", "", {}, "sha512-Bq3SmSpyFHaWjPk8If9yc6svM8c56dB5BAtW4Qbw5jHTwwXXcTLoRMkpDJp6VL0XzlWaCHTXrkFURMYmD0sLqg=="],

    "@nuxt/vite-builder/@vitejs/plugin-vue-jsx/@vue/babel-plugin-jsx/@babel/types/@babel/helper-string-parser": ["@babel/helper-string-parser@7.27.1", "", {}, "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA=="],

    "@nuxt/vite-builder/@vitejs/plugin-vue-jsx/@vue/babel-plugin-jsx/@babel/types/@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "@nuxt/vite-builder/@vitejs/plugin-vue-jsx/@vue/babel-plugin-jsx/@vue/babel-plugin-resolve-type/@babel/parser": ["@babel/parser@7.29.2", "", { "dependencies": { "@babel/types": "^7.29.0" }, "bin": "./bin/babel-parser.js" }, "sha512-4GgRzy/+fsBa72/RZVJmGKPmZu9Byn8o4MoLpmNe1m8ZfYnz5emHLQz3U4gLud6Zwl0RZIcgiLD7Uq7ySFuDLA=="],

    "@vue-macros/common/ast-kit/@babel/parser/@babel/types/@babel/helper-string-parser": ["@babel/helper-string-parser@7.27.1", "", {}, "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA=="],

    "@vue-macros/common/ast-kit/@babel/parser/@babel/types/@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "archiver-utils/glob/minimatch/brace-expansion/balanced-match": ["balanced-match@1.0.2", "", {}, "sha512-3oSeUO0TMV67hN1AmbXsK4yaqU7tjiHlbxRDZOpH0KW9+CeX4bRAaX0Anxt0tx2MrpRpWwQaPwIlISEJhYU5Pw=="],
  }
}
```

## File: `package.json`
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

## File: `tsdown.config.ts`
```typescript
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

## File: `packages/core/browser.ts`
```typescript
// This file serves as an entry point for the package
import { Lenis } from './src/lenis'

// @ts-expect-error
globalThis.Lenis = Lenis
// @ts-expect-error
globalThis.Lenis.prototype = Lenis.prototype
```

## File: `packages/core/index.ts`
```typescript
// This file serves as an entry point for the package
export { Lenis as default } from './src/lenis'
export * from './src/types'
```

## File: `packages/core/lenis.css`
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

## File: `packages/core/package.json`
```json
{
  "name": "lenis-core",
  "type": "module"
}
```

## File: `packages/core/src/animate.ts`
```typescript
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

## File: `packages/core/src/debounce.ts`
```typescript
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

## File: `packages/core/src/dimensions.ts`
```typescript
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

## File: `packages/core/src/emitter.ts`
```typescript
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

## File: `packages/core/src/lenis.ts`
```typescript
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
            duration: this.options.duration,
            easing: this.options.easing,
          }),
    })
  }

  /**
   * Force lenis to recalculate the dimensions
   */
  resize() {
    this.dimensions.resize()
    this.animatedScroll = this.targetScroll = this.actualScroll
    this.emit()
  }

  private emit() {
    this.emitter.emit('scroll', this)
  }

  private onNativeScroll = () => {
    if (this._resetVelocityTimeout !== null) {
      clearTimeout(this._resetVelocityTimeout)
      this._resetVelocityTimeout = null
    }

    if (this._preventNextNativeScrollEvent) {
      this._preventNextNativeScrollEvent = false
      return
    }

    if (this.isScrolling === false || this.isScrolling === 'native') {
      const lastScroll = this.animatedScroll
      this.animatedScroll = this.targetScroll = this.actualScroll
      this.lastVelocity = this.velocity
      this.velocity = this.animatedScroll - lastScroll
      this.direction = Math.sign(
        this.animatedScroll - lastScroll
      ) as Lenis['direction']

      if (!this.isStopped) {
        this.isScrolling = 'native'
      }

      this.emit()

      if (this.velocity !== 0) {
        this._resetVelocityTimeout = setTimeout(() => {
          this.lastVelocity = this.velocity
          this.velocity = 0
          this.isScrolling = false
          this.emit()
        }, 400)
      }
    }
  }

  private reset() {
    this.isLocked = false
    this.isScrolling = false
    this.animatedScroll = this.targetScroll = this.actualScroll
    this.lastVelocity = this.velocity = 0
    this.animate.stop()
  }

  /**
   * Start lenis scroll after it has been stopped
   */
  start() {
    if (!this.isStopped) return

    if (this.options.autoToggle) {
      this.rootElement.style.removeProperty('overflow')
      return
    }

    this.internalStart()
  }

  private internalStart() {
    if (!this.isStopped) return

    this.reset()
    this.isStopped = false
    this.emit()
  }

  /**
   * Stop lenis scroll
   */
  stop() {
    if (this.isStopped) return

    if (this.options.autoToggle) {
      this.rootElement.style.setProperty('overflow', 'clip')
      return
    }

    this.internalStop()
  }

  private internalStop() {
    if (this.isStopped) return

    this.reset()
    this.isStopped = true
    this.emit()
  }

  /**
   * RequestAnimationFrame for lenis
   *
   * @param time The time in ms from an external clock like `requestAnimationFrame` or Tempus
   */
  raf = (time: number) => {
    const deltaTime = time - (this.time || time)
    this.time = time

    this.animate.advance(deltaTime * 0.001)

    if (this.options.autoRaf) {
      this._rafId = requestAnimationFrame(this.raf)
    }
  }

  /**
   * Scroll to a target value
   *
   * @param target The target value to scroll to
   * @param options The options for the scroll
   *
   * @example
   * lenis.scrollTo(100, {
   *   offset: 100,
   *   duration: 1,
   *   easing: (t) => 1 - Math.cos((t * Math.PI) / 2),
   *   lerp: 0.1,
   *   onStart: () => {
   *     console.log('onStart')
   *   },
   *   onComplete: () => {
   *     console.log('onComplete')
   *   },
   * })
   */
  scrollTo(
    _target: number | string | HTMLElement,
    {
      offset = 0,
      immediate = false,
      lock = false,
      programmatic = true, // called from outside of the class
      lerp = programmatic ? this.options.lerp : undefined,
      duration = programmatic ? this.options.duration : undefined,
      easing = programmatic ? this.options.easing : undefined,
      onStart,
      onComplete,
      force = false, // scroll even if stopped
      userData,
    }: ScrollToOptions = {}
  ) {
    if ((this.isStopped || this.isLocked) && !force) return

    let target: number | string | HTMLElement = _target
    let adjustedOffset = offset

    // keywords
    if (
      typeof target === 'string' &&
      ['top', 'left', 'start', '#'].includes(target)
    ) {
      target = 0
    } else if (
      typeof target === 'string' &&
      ['bottom', 'right', 'end'].includes(target)
    ) {
      target = this.limit
    } else {
      let node: Element | null = null

      if (typeof target === 'string') {
        // CSS selector
        node = document.querySelector(target)

        if (!node) {
          if (target === '#top') {
            target = 0
          } else {
            console.warn('Lenis: Target not found', target)
          }
        }
      } else if (target instanceof HTMLElement && target?.nodeType) {
        // Node element
        node = target
      }

      if (node) {
        if (this.options.wrapper !== window) {
          // nested scroll offset correction
          const wrapperRect = this.rootElement.getBoundingClientRect()
          adjustedOffset -= this.isHorizontal
            ? wrapperRect.left
            : wrapperRect.top
        }

        const rect = node.getBoundingClientRect()

        // Account for scroll-margin CSS property on the target element
        const targetStyle = getComputedStyle(node)
        const scrollMargin = this.isHorizontal
          ? Number.parseFloat(targetStyle.scrollMarginLeft)
          : Number.parseFloat(targetStyle.scrollMarginTop)

        // Account for scroll-padding CSS property on the scroll container
        const containerStyle = getComputedStyle(this.rootElement)
        const scrollPadding = this.isHorizontal
          ? Number.parseFloat(containerStyle.scrollPaddingLeft)
          : Number.parseFloat(containerStyle.scrollPaddingTop)

        target =
          (this.isHorizontal ? rect.left : rect.top) +
          this.animatedScroll -
          (Number.isNaN(scrollMargin) ? 0 : scrollMargin) -
          (Number.isNaN(scrollPadding) ? 0 : scrollPadding)
      }
    }

    if (typeof target !== 'number') return

    target += adjustedOffset
    target = Math.round(target)

    if (this.options.infinite) {
      if (programmatic) {
        this.targetScroll = this.animatedScroll = this.scroll

        const distance = target - this.animatedScroll

        if (distance > this.limit / 2) {
          target -= this.limit
        } else if (distance < -this.limit / 2) {
          target += this.limit
        }
      }
    } else {
      target = clamp(0, target, this.limit)
    }

    if (target === this.targetScroll) {
      onStart?.(this)
      onComplete?.(this)
      return
    }

    this.userData = userData ?? {}

    if (immediate) {
      this.animatedScroll = this.targetScroll = target
      this.setScroll(this.scroll)
      this.reset()
      this.preventNextNativeScrollEvent()
      this.emit()
      onComplete?.(this)
      this.userData = {}

      requestAnimationFrame(() => {
        this.dispatchScrollendEvent()
      })
      return
    }

    if (!programmatic) {
      this.targetScroll = target
    }

    // flip to easing/time based animation if at least one of them is provided
    if (typeof duration === 'number' && typeof easing !== 'function') {
      easing = defaultEasing
    } else if (typeof easing === 'function' && typeof duration !== 'number') {
      duration = 1
    }

    this.animate.fromTo(this.animatedScroll, target, {
      duration,
      easing,
      lerp,
      onStart: () => {
        // started
        if (lock) this.isLocked = true
        this.isScrolling = 'smooth'
        onStart?.(this)
      },
      onUpdate: (value: number, completed: boolean) => {
        this.isScrolling = 'smooth'

        // updated
        this.lastVelocity = this.velocity
        this.velocity = value - this.animatedScroll
        this.direction = Math.sign(this.velocity) as Lenis['direction']

        this.animatedScroll = value
        this.setScroll(this.scroll)

        if (programmatic) {
          // wheel during programmatic should stop it
          this.targetScroll = value
        }

        if (!completed) this.emit()

        if (completed) {
          this.reset()
          this.emit()
          onComplete?.(this)
          this.userData = {}

          requestAnimationFrame(() => {
            this.dispatchScrollendEvent()
          })

          // avoid emitting event twice
          this.preventNextNativeScrollEvent()
        }
      },
    })
  }

  private preventNextNativeScrollEvent() {
    this._preventNextNativeScrollEvent = true

    requestAnimationFrame(() => {
      this._preventNextNativeScrollEvent = false
    })
  }

  private hasNestedScroll(
    node: HTMLElement,
    { deltaX, deltaY }: { deltaX: number; deltaY: number }
  ) {
    const time = Date.now()

    // @ts-expect-error - _lenis is a custom cache property
    if (!node._lenis) node._lenis = {}
    // @ts-expect-error
    const cache = node._lenis

    let hasOverflowX: boolean | undefined
    let hasOverflowY: boolean | undefined
    let isScrollableX: boolean | undefined
    let isScrollableY: boolean | undefined
    let hasOverscrollBehaviorX: boolean | undefined
    let hasOverscrollBehaviorY: boolean | undefined
    let scrollWidth: number
    let scrollHeight: number
    let clientWidth: number
    let clientHeight: number

    if (time - (cache.time ?? 0) > 2000) {
      cache.time = Date.now()

      const computedStyle = window.getComputedStyle(node)
      cache.computedStyle = computedStyle

      hasOverflowX = ['auto', 'overlay', 'scroll'].includes(
        computedStyle.overflowX
      )
      hasOverflowY = ['auto', 'overlay', 'scroll'].includes(
        computedStyle.overflowY
      )

      hasOverscrollBehaviorX = ['auto'].includes(
        computedStyle.overscrollBehaviorX
      )
      hasOverscrollBehaviorY = ['auto'].includes(
        computedStyle.overscrollBehaviorY
      )

      cache.hasOverflowX = hasOverflowX
      cache.hasOverflowY = hasOverflowY

      if (!(hasOverflowX || hasOverflowY)) return false // if no overflow, it's not scrollable no matter what, early return saves some computations

      scrollWidth = node.scrollWidth
      scrollHeight = node.scrollHeight

      clientWidth = node.clientWidth
      clientHeight = node.clientHeight

      isScrollableX = scrollWidth > clientWidth
      isScrollableY = scrollHeight > clientHeight

      cache.isScrollableX = isScrollableX
      cache.isScrollableY = isScrollableY
      cache.scrollWidth = scrollWidth
      cache.scrollHeight = scrollHeight
      cache.clientWidth = clientWidth
      cache.clientHeight = clientHeight
      cache.hasOverscrollBehaviorX = hasOverscrollBehaviorX
      cache.hasOverscrollBehaviorY = hasOverscrollBehaviorY
    } else {
      isScrollableX = cache.isScrollableX
      isScrollableY = cache.isScrollableY
      hasOverflowX = cache.hasOverflowX
      hasOverflowY = cache.hasOverflowY
      scrollWidth = cache.scrollWidth
      scrollHeight = cache.scrollHeight
      clientWidth = cache.clientWidth
      clientHeight = cache.clientHeight
      hasOverscrollBehaviorX = cache.hasOverscrollBehaviorX
      hasOverscrollBehaviorY = cache.hasOverscrollBehaviorY
    }

    if (!((hasOverflowX && isScrollableX) || (hasOverflowY && isScrollableY))) {
      return false
    }

    const orientation =
      Math.abs(deltaX) >= Math.abs(deltaY) ? 'horizontal' : 'vertical'

    let scroll: number | undefined
    let maxScroll: number | undefined
    let delta: number | undefined
    let hasOverflow: boolean | undefined
    let isScrollable: boolean | undefined
    let hasOverscrollBehavior: boolean | undefined

    if (orientation === 'horizontal') {
      scroll = Math.round(node.scrollLeft)
      maxScroll = scrollWidth - clientWidth
      delta = deltaX

      hasOverflow = hasOverflowX
      isScrollable = isScrollableX
      hasOverscrollBehavior = hasOverscrollBehaviorX
    } else if (orientation === 'vertical') {
      scroll = Math.round(node.scrollTop)
      maxScroll = scrollHeight - clientHeight
      delta = deltaY

      hasOverflow = hasOverflowY
      isScrollable = isScrollableY
      hasOverscrollBehavior = hasOverscrollBehaviorY
    } else {
      return false
    }

    if (!hasOverscrollBehavior && (scroll >= maxScroll || scroll <= 0)) {
      return true
    }

    const willScroll = delta > 0 ? scroll < maxScroll : scroll > 0

    return willScroll && hasOverflow && isScrollable
  }

  /**
   * The root element on which lenis is instanced
   */
  get rootElement() {
    return (
      this.options.wrapper === window
        ? document.documentElement
        : this.options.wrapper
    ) as HTMLElement
  }

  /**
   * The limit which is the maximum scroll value
   */
  get limit() {
    if (this.options.naiveDimensions) {
      if (this.isHorizontal) {
        return this.rootElement.scrollWidth - this.rootElement.clientWidth
      }
      return this.rootElement.scrollHeight - this.rootElement.clientHeight
    }
    return this.dimensions.limit[this.isHorizontal ? 'x' : 'y']
  }

  /**
   * Whether or not the scroll is horizontal
   */
  get isHorizontal() {
    return this.options.orientation === 'horizontal'
  }

  /**
   * The actual scroll value
   */
  get actualScroll() {
    // value browser takes into account
    // it has to be this way because of DOCTYPE declaration
    const wrapper = this.options.wrapper as Window | HTMLElement

    return this.isHorizontal
      ? ((wrapper as Window).scrollX ?? (wrapper as HTMLElement).scrollLeft)
      : ((wrapper as Window).scrollY ?? (wrapper as HTMLElement).scrollTop)
  }

  /**
   * The current scroll value
   */
  get scroll() {
    return this.options.infinite
      ? modulo(this.animatedScroll, this.limit)
      : this.animatedScroll
  }

  /**
   * The progress of the scroll relative to the limit
   */
  get progress() {
    // avoid progress to be NaN
    return this.limit === 0 ? 1 : this.scroll / this.limit
  }

  /**
   * Current scroll state
   */
  get isScrolling() {
    return this._isScrolling
  }

  private set isScrolling(value: Scrolling) {
    if (this._isScrolling !== value) {
      this._isScrolling = value
      this.updateClassName()
    }
  }

  /**
   * Check if lenis is stopped
   */
  get isStopped() {
    return this._isStopped
  }

  private set isStopped(value: boolean) {
    if (this._isStopped !== value) {
      this._isStopped = value
      this.updateClassName()
    }
  }

  /**
   * Check if lenis is locked
   */
  get isLocked() {
    return this._isLocked
  }

  private set isLocked(value: boolean) {
    if (this._isLocked !== value) {
      this._isLocked = value
      this.updateClassName()
    }
  }

  /**
   * Check if lenis is smooth scrolling
   */
  get isSmooth() {
    return this.isScrolling === 'smooth'
  }

  /**
   * The class name applied to the wrapper element
   */
  get className() {
    let className = 'lenis'
    if (this.options.autoToggle) className += ' lenis-autoToggle'
    if (this.isStopped) className += ' lenis-stopped'
    if (this.isLocked) className += ' lenis-locked'
    if (this.isScrolling) className += ' lenis-scrolling'
    if (this.isScrolling === 'smooth') className += ' lenis-smooth'
    return className
  }

  private updateClassName() {
    this.cleanUpClassName()

    this.rootElement.className =
      `${this.rootElement.className} ${this.className}`.trim()
  }

  private cleanUpClassName() {
    this.rootElement.className = this.rootElement.className
      .replace(/lenis(-\w+)?/g, '')
      .trim()
  }
}
```

## File: `packages/core/src/maths.ts`
```typescript
/**
 * Clamp a value between a minimum and maximum value
 *
 * @param min Minimum value
 * @param input Value to clamp
 * @param max Maximum value
 * @returns Clamped value
 */
export function clamp(min: number, input: number, max: number) {
  return Math.max(min, Math.min(input, max))
}

/**
 * Truncate a floating-point number to a specified number of decimal places
 *
 * @param value Value to truncate
 * @param decimals Number of decimal places to truncate to
 * @returns Truncated value
 */
export function truncate(value: number, decimals = 0) {
  return Number.parseFloat(value.toFixed(decimals))
}

/**
 *  Linearly interpolate between two values using an amount (0 <= t <= 1)
 *
 * @param x First value
 * @param y Second value
 * @param t Amount to interpolate (0 <= t <= 1)
 * @returns Interpolated value
 */
export function lerp(x: number, y: number, t: number) {
  return (1 - t) * x + t * y
}

/**
 * Damp a value over time using a damping factor
 * {@link http://www.rorydriscoll.com/2016/03/07/frame-rate-independent-damping-using-lerp/}
 *
 * @param x Initial value
 * @param y Target value
 * @param lambda Damping factor
 * @param dt Time elapsed since the last update
 * @returns Damped value
 */
export function damp(x: number, y: number, lambda: number, deltaTime: number) {
  return lerp(x, y, 1 - Math.exp(-lambda * deltaTime))
}

/**
 * Calculate the modulo of the dividend and divisor while keeping the result within the same sign as the divisor
 * {@link https://anguscroll.com/just/just-modulo}
 *
 * @param n Dividend
 * @param d Divisor
 * @returns Modulo
 */
export function modulo(n: number, d: number) {
  return ((n % d) + d) % d
}
```

## File: `packages/core/src/types.ts`
```typescript
import type { Lenis } from './lenis'

export type OnUpdateCallback = (value: number, completed: boolean) => void
export type OnStartCallback = () => void

export type FromToOptions = {
  /**
   * Linear interpolation (lerp) intensity (between 0 and 1)
   * @default 0.1
   */
  lerp?: number
  /**
   * The duration of the scroll animation (in s)
   * @default 1
   */
  duration?: number
  /**
   * The easing function to use for the scroll animation
   * @default (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t))
   */
  easing?: EasingFunction
  /**
   * Called when the scroll starts
   */
  onStart?: OnStartCallback
  /**
   * Called when the scroll progress changes
   */
  onUpdate?: OnUpdateCallback
}

export type UserData = Record<string, unknown>

export type Scrolling = boolean | 'native' | 'smooth'

export type LenisEvent = 'scroll' | 'virtual-scroll'
export type ScrollCallback = (lenis: Lenis) => void
export type VirtualScrollCallback = (data: VirtualScrollData) => void

export type VirtualScrollData = {
  deltaX: number
  deltaY: number
  event: WheelEvent | TouchEvent
}

export type Orientation = 'vertical' | 'horizontal'
export type GestureOrientation = 'vertical' | 'horizontal' | 'both'
export type EasingFunction = (time: number) => number

export type ScrollToOptions = {
  /**
   * The offset to apply to the target value
   * @default 0
   */
  offset?: number
  /**
   * Skip the animation and jump to the target value immediately
   * @default false
   */
  immediate?: boolean
  /**
   * Lock the scroll to the target value
   * @default false
   */
  lock?: boolean
  /**
   * The duration of the scroll animation (in s)
   */
  duration?: number
  /**
   * The easing function to use for the scroll animation
   * @default (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t))
   */
  easing?: EasingFunction
  /**
   * Linear interpolation (lerp) intensity (between 0 and 1)
   * @default 0.1
   */
  lerp?: number
  /**
   * Called when the scroll starts
   */
  onStart?: (lenis: Lenis) => void
  /**
   * Called when the scroll completes
   */
  onComplete?: (lenis: Lenis) => void
  /**
   * Scroll even if stopped
   * @default false
   */
  force?: boolean
  /**
   * Scroll initiated from outside of the lenis instance
   * @default false
   */
  programmatic?: boolean
  /**
   * User data that will be forwarded through the scroll event
   */
  userData?: UserData
}

export type LenisOptions = {
  /**
   * The element that will be used as the scroll container
   * @default window
   */
  wrapper?: Window | HTMLElement | Element
  /**
   * The element that contains the content that will be scrolled, usually `wrapper`'s direct child
   * @default document.documentElement
   */
  content?: HTMLElement | Element
  /**
   * The element that will listen to `wheel` and `touch` events
   * @default window
   */
  eventsTarget?: Window | HTMLElement | Element
  /**
   * Smooth the scroll initiated by `wheel` events
   * @default true
   */
  smoothWheel?: boolean
  /**
   * Mimic touch device scroll while allowing scroll sync
   * @default false
   */
  syncTouch?: boolean
  /**
   * Linear interpolation (lerp) intensity (between 0 and 1)
   * @default 0.075
   */
  syncTouchLerp?: number
  /**
   * Manage the the strength of `syncTouch` inertia
   * @default 1.7
   */
  touchInertiaExponent?: number
  /**
   * Scroll duration in seconds
   */
  duration?: number
  /**
   * Scroll easing function
   * @default (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t))
   */
  easing?: EasingFunction
  /**
   * Linear interpolation (lerp) intensity (between 0 and 1)
   * @default 0.1
   */
  lerp?: number
  /**
   * Enable infinite scrolling
   * @default false
   */
  infinite?: boolean
  /**
   * The orientation of the scrolling. Can be `vertical` or `horizontal`
   * @default vertical
   */
  orientation?: Orientation
  /**
   * The orientation of the gestures. Can be `vertical`, `horizontal` or `both`
   * @default vertical
   */
  gestureOrientation?: GestureOrientation
  /**
   * The multiplier to use for touch events
   * @default 1
   */
  touchMultiplier?: number
  /**
   * The multiplier to use for mouse wheel events
   * @default 1
   */
  wheelMultiplier?: number
  /**
   * Resize instance automatically
   * @default true
   */
  autoResize?: boolean
  /**
   * Manually prevent scroll to be smoothed based on elements traversed by events
   */
  prevent?: (node: HTMLElement) => boolean
  /**
   * Manually modify the events before they get consumed
   */
  virtualScroll?: (data: VirtualScrollData) => boolean
  /**
   * Wether or not to enable overscroll on a nested Lenis instance, similar to CSS overscroll-behavior (https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/CSS/overscroll-behavior)
   * @default true
   */
  overscroll?: boolean
  /**
   * If `true`, Lenis will automatically run `requestAnimationFrame` loop
   * @default false
   */
  autoRaf?: boolean
  /**
   * If `true`, Lenis will handle anchor links automatically
   * @default false
   */
  anchors?: boolean | ScrollToOptions
  /**
   * If `true`, Lenis will automatically start/stop based on wrapper's overflow property
   * @default false
   */
  autoToggle?: boolean
  /**
   * If `true`, Lenis will allow nested scroll
   * @default false
   */
  allowNestedScroll?: boolean
  /**
   * @deprecated use `naiveDimensions` instead
   */
  __experimental__naiveDimensions?: boolean
  /**
   * If `true`, Lenis will use naive dimensions calculation, be careful this has a performance impact
   * @default false
   */
  naiveDimensions?: boolean
  /**
   * If `true`, Lenis will stop inertia when an internal link is clicked
   * @default false
   */
  stopInertiaOnNavigate?: boolean
}

declare global {
  interface Window {
    lenisVersion: string
    lenis: {
      version?: string
      horizontal?: boolean
      snap?: boolean
      touch?: boolean
    }
  }
}
```

## File: `packages/core/src/virtual-scroll.ts`
```typescript
import { Emitter } from './emitter'
import type { VirtualScrollCallback } from './types'

const LINE_HEIGHT = 100 / 6
const listenerOptions: AddEventListenerOptions = { passive: false }

function getDeltaMultiplier(deltaMode: number, size: number): number {
  if (deltaMode === 1) return LINE_HEIGHT
  if (deltaMode === 2) return size
  return 1
}

export class VirtualScroll {
  touchStart = {
    x: 0,
    y: 0,
  }
  lastDelta = {
    x: 0,
    y: 0,
  }
  window = {
    width: 0,
    height: 0,
  }
  private emitter = new Emitter()

  constructor(
    private element: HTMLElement,
    private options = { wheelMultiplier: 1, touchMultiplier: 1 }
  ) {
    window.addEventListener('resize', this.onWindowResize)
    this.onWindowResize()

    this.element.addEventListener('wheel', this.onWheel, listenerOptions)
    this.element.addEventListener(
      'touchstart',
      this.onTouchStart,
      listenerOptions
    )
    this.element.addEventListener(
      'touchmove',
      this.onTouchMove,
      listenerOptions
    )
    this.element.addEventListener('touchend', this.onTouchEnd, listenerOptions)
  }

  /**
   * Add an event listener for the given event and callback
   *
   * @param event Event name
   * @param callback Callback function
   */
  on(event: string, callback: VirtualScrollCallback) {
    return this.emitter.on(event, callback as (...args: unknown[]) => void)
  }

  /** Remove all event listeners and clean up */
  destroy() {
    this.emitter.destroy()

    window.removeEventListener('resize', this.onWindowResize)

    this.element.removeEventListener('wheel', this.onWheel, listenerOptions)
    this.element.removeEventListener(
      'touchstart',
      this.onTouchStart,
      listenerOptions
    )
    this.element.removeEventListener(
      'touchmove',
      this.onTouchMove,
      listenerOptions
    )
    this.element.removeEventListener(
      'touchend',
      this.onTouchEnd,
      listenerOptions
    )
  }

  /**
   * Event handler for 'touchstart' event
   *
   * @param event Touch event
   */
  onTouchStart = (event: TouchEvent) => {
    // @ts-expect-error - event.targetTouches is not defined
    const { clientX, clientY } = event.targetTouches
      ? event.targetTouches[0]
      : event

    this.touchStart.x = clientX
    this.touchStart.y = clientY

    this.lastDelta = {
      x: 0,
      y: 0,
    }

    this.emitter.emit('scroll', {
      deltaX: 0,
      deltaY: 0,
      event,
    })
  }

  /** Event handler for 'touchmove' event */
  onTouchMove = (event: TouchEvent) => {
    // @ts-expect-error - event.targetTouches is not defined
    const { clientX, clientY } = event.targetTouches
      ? event.targetTouches[0]
      : event

    const deltaX = -(clientX - this.touchStart.x) * this.options.touchMultiplier
    const deltaY = -(clientY - this.touchStart.y) * this.options.touchMultiplier

    this.touchStart.x = clientX
    this.touchStart.y = clientY

    this.lastDelta = {
      x: deltaX,
      y: deltaY,
    }

    this.emitter.emit('scroll', {
      deltaX,
      deltaY,
      event,
    })
  }

  onTouchEnd = (event: TouchEvent) => {
    this.emitter.emit('scroll', {
      deltaX: this.lastDelta.x,
      deltaY: this.lastDelta.y,
      event,
    })
  }

  /** Event handler for 'wheel' event */
  onWheel = (event: WheelEvent) => {
    let { deltaX, deltaY, deltaMode } = event

    const multiplierX = getDeltaMultiplier(deltaMode, this.window.width)
    const multiplierY = getDeltaMultiplier(deltaMode, this.window.height)

    deltaX *= multiplierX
    deltaY *= multiplierY

    deltaX *= this.options.wheelMultiplier
    deltaY *= this.options.wheelMultiplier

    this.emitter.emit('scroll', { deltaX, deltaY, event })
  }

  onWindowResize = () => {
    this.window = {
      width: window.innerWidth,
      height: window.innerHeight,
    }
  }
}
```

## File: `packages/react/README.md`
```markdown
# lenis/react

## Introduction
lenis/react provides a `<ReactLenis>` component that creates a [Lenis](https://github.com/darkroomengineering/lenis) instance and provides it to its children via context. This allows you to use Lenis in your React app without worrying about passing the instance down through props. It also provides a `useLenis` hook that allows you to access the Lenis instance from any component in your app.


## Installation

```bash
npm i lenis
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

## File: `packages/react/index.ts`
```typescript
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

## File: `packages/react/package.json`
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

## File: `packages/react/src/provider.tsx`
```tsx
import Lenis, { type ScrollCallback } from 'lenis'
import {
  type ForwardRefExoticComponent,
  type RefAttributes,
  createContext,
  forwardRef,
  useCallback,
  useEffect,
  useImperativeHandle,
  useRef,
  useState,
} from 'react'
import { Store } from './store'
import type { LenisContextValue, LenisProps, LenisRef } from './types'

export const LenisContext = createContext<LenisContextValue | null>(null)

/**
 * The root store for the lenis context
 *
 * This store serves as a fallback for the context if it is not available
 * and allows us to use the global lenis instance above a provider
 */
export const rootLenisContextStore = new Store<LenisContextValue | null>(null)

/**
 * React component to setup a Lenis instance
 */
export const ReactLenis: ForwardRefExoticComponent<
  LenisProps & RefAttributes<LenisRef>
> = forwardRef<LenisRef, LenisProps>(
  (
    {
      children,
      root = false,
      options = {},
      autoRaf = true,
      className = '',
      ...props
    }: LenisProps,
    ref
  ) => {
    const wrapperRef = useRef<HTMLDivElement>(null)
    const contentRef = useRef<HTMLDivElement>(null)

    const [lenis, setLenis] = useState<Lenis | undefined>(undefined)

    // Setup ref
    useImperativeHandle(
      ref,
      () => ({
        wrapper: wrapperRef.current,
        content: contentRef.current,
        lenis,
      }),
      [lenis]
    )

    // Setup lenis instance
    useEffect(() => {
      const lenis = new Lenis({
        ...options,
        ...(wrapperRef.current &&
          contentRef.current && {
            wrapper: wrapperRef.current!,
            content: contentRef.current!,
          }),
        autoRaf: options?.autoRaf ?? autoRaf, // this is to avoid breaking the autoRaf prop if it's still used (require breaking change)
      })

      setLenis(lenis)

      return () => {
        lenis.destroy()
        setLenis(undefined)
      }
    }, [autoRaf, JSON.stringify({ ...options, wrapper: null, content: null })])

    // Handle callbacks
    const callbacksRefs = useRef<
      {
        callback: ScrollCallback
        priority: number
      }[]
    >([])

    const addCallback: LenisContextValue['addCallback'] = useCallback(
      (callback, priority) => {
        callbacksRefs.current.push({ callback, priority })
        callbacksRefs.current.sort((a, b) => a.priority - b.priority)
      },
      []
    )

    const removeCallback: LenisContextValue['removeCallback'] = useCallback(
      (callback) => {
        callbacksRefs.current = callbacksRefs.current.filter(
          (cb) => cb.callback !== callback
        )
      },
      []
    )

    // This makes sure to set the global context if the root is true
    useEffect(() => {
      if (root && lenis) {
        rootLenisContextStore.set({ lenis, addCallback, removeCallback })

        return () => rootLenisContextStore.set(null)
      }
    }, [root, lenis, addCallback, removeCallback])

    // Setup callback listeners
    useEffect(() => {
      if (!lenis) return

      const onScroll: ScrollCallback = (data) => {
        for (const { callback } of callbacksRefs.current) {
          callback(data)
        }
      }

      lenis.on('scroll', onScroll)

      return () => {
        lenis.off('scroll', onScroll)
      }
    }, [lenis])

    if (!children) return null

    return (
      <LenisContext.Provider
        value={{ lenis: lenis!, addCallback, removeCallback }}
      >
        {root && root !== 'asChild' ? (
          children
        ) : (
          <div
            ref={wrapperRef}
            className={`${className} ${lenis?.className ?? ''}`.trim()}
            {...props}
          >
            <div ref={contentRef}>{children}</div>
          </div>
        )}
      </LenisContext.Provider>
    )
  }
)
```

## File: `packages/react/src/store.ts`
```typescript
import { useEffect, useState } from 'react'

type Listener<S> = (state: S) => void

export class Store<S> {
  private listeners: Listener<S>[] = []

  constructor(private state: S) {}

  set(state: S) {
    this.state = state

    for (const listener of this.listeners) {
      listener(this.state)
    }
  }

  subscribe(listener: Listener<S>) {
    this.listeners = [...this.listeners, listener]
    return () => {
      this.listeners = this.listeners.filter((l) => l !== listener)
    }
  }

  get() {
    return this.state
  }
}

export function useStore<S>(store: Store<S>) {
  const [state, setState] = useState(store.get())

  useEffect(() => {
    return store.subscribe((state) => setState(state))
  }, [store])

  return state
}
```

## File: `packages/react/src/types.ts`
```typescript
import type Lenis from 'lenis'
import type { LenisOptions, ScrollCallback } from 'lenis'
import type { ComponentPropsWithoutRef, ReactNode } from 'react'

export type LenisContextValue = {
  lenis: Lenis
  addCallback: (callback: ScrollCallback, priority: number) => void
  removeCallback: (callback: ScrollCallback) => void
}

export type LenisProps = ComponentPropsWithoutRef<'div'> & {
  /**
   * Setup a global instance of Lenis
   * if `asChild`, the component will render wrapper and content divs
   * @default false
   */
  root?: boolean | 'asChild'
  /**
   * Lenis options
   */
  options?: LenisOptions
  /**
   * Auto-setup requestAnimationFrame
   * @default true
   * @deprecated use options.autoRaf instead
   */
  autoRaf?: boolean
  /**
   * Children
   */
  children?: ReactNode

  /**
   * Class name to be applied to the wrapper div
   * @default ''
   */
  className?: string | undefined
}

export type LenisRef = {
  /**
   * The wrapper div element
   *
   * Will only be defined if `root` is `false` or `root` is `asChild`
   */
  wrapper: HTMLDivElement | null
  /**
   * The content div element
   *
   * Will only be defined if `root` is `false` or `root` is `asChild`
   */
  content: HTMLDivElement | null
  /**
   * The lenis instance
   */
  lenis?: Lenis
}
```

## File: `packages/react/src/use-lenis.ts`
```typescript
import type Lenis from 'lenis'
import type { ScrollCallback } from 'lenis'
import { useContext, useEffect } from 'react'
import { LenisContext, rootLenisContextStore } from './provider'
import { useStore } from './store'
import type { LenisContextValue } from './types'

// Fall back to an empty object if both context and store are not available
const fallbackContext: Partial<LenisContextValue> = {}

/**
 * Hook to access the Lenis instance and its methods
 *
 * @example <caption>Scroll callback</caption>
 *          useLenis((lenis) => {
 *            if (lenis.isScrolling) {
 *              console.log('Scrolling...')
 *            }
 *
 *            if (lenis.progress === 1) {
 *              console.log('At the end!')
 *            }
 *          })
 *
 * @example <caption>Scroll callback with dependencies</caption>
 *          useLenis((lenis) => {
 *            if (lenis.isScrolling) {
 *              console.log('Scrolling...', someDependency)
 *            }
 *          }, [someDependency])
 * @example <caption>Scroll callback with priority</caption>
 *          useLenis((lenis) => {
 *            if (lenis.isScrolling) {
 *              console.log('Scrolling...')
 *            }
 *          }, [], 1)
 * @example <caption>Instance access</caption>
 *          const lenis = useLenis()
 *
 *          handleClick() {
 *            lenis.scrollTo(100, {
 *              lerp: 0.1,
 *              duration: 1,
 *              easing: (t) => t,
 *              onComplete: () => {
 *                console.log('Complete!')
 *              }
 *            })
 *          }
 */
export function useLenis(
  callback?: ScrollCallback,
  deps: unknown[] = [],
  priority = 0
): Lenis | undefined {
  // Try to get the lenis instance from the context first
  const localContext = useContext(LenisContext)
  // Fall back to the root store if the context is not available
  const rootContext = useStore(rootLenisContextStore)
  // Fall back to the fallback context if all else fails
  const currentContext = localContext ?? rootContext ?? fallbackContext

  const { lenis, addCallback, removeCallback } = currentContext

  useEffect(() => {
    if (!(callback && addCallback && removeCallback && lenis)) return

    addCallback(callback, priority)
    callback(lenis)

    return () => {
      removeCallback(callback)
    }
  }, [lenis, addCallback, removeCallback, priority, ...deps, callback])

  return lenis
}
```

## File: `packages/snap/README.md`
```markdown
# lenis/snap

## Introduction
lenis/snap provides a partial support for CSS scroll snap with [Lenis](https://github.com/darkroomengineering/lenis), see [Demo](https://lenis.darkroom.engineering/snap)

## Installation

```bash
npm i lenis
```

## Usage

### Basic

```jsx
    import Lenis from 'lenis'
    import Snap from 'lenis/snap'

    const lenis = new Lenis()

    function raf(time) {
        lenis.raf(time)
        requestAnimationFrame(raf)
    }

    requestAnimationFrame(raf)

    const snap = new Snap(lenis)

    // add snaps points
    snap.add(500) // snap at 500px
    snap.add(1000) // snap at 1000px
    snap.add(1500) // snap at 1500px

    // or add an element to snap to
    snap.addElement(document.querySelector('.element'), {
      align: ['start', 'end'], // 'start', 'center', 'end'
    })

    snap.addElement(document.querySelector('.element1'), {
      align: 'center', // 'start', 'center', 'end'
    })

    // or add elements at once
    snap.addElements(document.querySelectorAll('.section'), {
      align: ['start', 'end'], // 'start', 'center', 'end'
    })
    
    
```

### Slideshow

```jsx
    const snap = new Snap(lenis, {
      type: 'lock',
      distanceThreshold: '100%',
      debounce: 0,
    })
```

## Options

- `type`: `proximity` (default), `mandatory` see [scroll-snap-type](https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/CSS/scroll-snap-type) or `lock`.
- `distanceThreshold`: `string | number` (default: '50%'). The distance threshold from the snap point to the scroll position. Ignored when `type` is `mandatory`. If a percentage, it is relative to the viewport size. If a number, it is absolute.
- `debounce`: `number` (default: 500). The debounce time for the snap.
- `onSnapStart`: `function`. Callback when snap starts.
- `onSnapComplete`: `function`. Callback when snap completes.
- `lerp`: `number` Lerp value for snapping. (default: lenis lerp). 
- `easing`: `function`. Easing function for snapping. (default: lenis easing).
- `duration`: `number`. Duration for snapping. (default: lenis duration).


## Methods

- `add(value: number)`: Add a snap point.
- `addElement(element: HTMLElement, options: SnapElementOptions = {})`: Add an element to snap to.
- `addElements(elements: HTMLElement[], options: SnapElementOptions = {})`: Add elements at once.
- `next()`: Go to the next snap point.
- `previous()`: Go to the previous snap point.
- `goTo(index: number)`: Go to a specific snap point.
- `start()`: Start the snap.
- `stop()`: Stop the snap.
- `resize()`: Force recalculate the snap points.
```

## File: `packages/snap/browser.ts`
```typescript
// This file serves as an entry point for the package
import { Snap } from './src/snap'

// @ts-expect-error
globalThis.Snap = Snap
```

## File: `packages/snap/index.ts`
```typescript
// This file serves as an entry point for the package
export { Snap as default } from './src/snap'
export * from './src/types'
```

## File: `packages/snap/package.json`
```json
{
  "name": "lenis-snap",
  "type": "module"
}
```

## File: `packages/snap/src/debounce.ts`
```typescript
export function debounce<CB extends (...args: unknown[]) => void>(
  callback: CB,
  delay: number
) {
  let timer: ReturnType<typeof setTimeout> | undefined
  return function <T>(this: T, ...args: Parameters<typeof callback>): void {
    clearTimeout(timer)
    timer = setTimeout(() => {
      timer = undefined
      callback.apply(this, args)
    }, delay)
  }
}
```

## File: `packages/snap/src/element.ts`
```typescript
import { debounce } from './debounce'

function removeParentSticky(element: HTMLElement) {
  const position = getComputedStyle(element).position

  const isSticky = position === 'sticky'

  if (isSticky) {
    element.style.setProperty('position', 'static')
    element.dataset.sticky = 'true'
  }

  if (element.offsetParent) {
    removeParentSticky(element.offsetParent as HTMLElement)
  }
}

function addParentSticky(element: HTMLElement) {
  if (element?.dataset?.sticky === 'true') {
    element.style.removeProperty('position')
    delete element.dataset.sticky
  }

  if (element.offsetParent) {
    addParentSticky(element.offsetParent as HTMLElement)
  }
}

function offsetTop(element: HTMLElement, accumulator = 0) {
  const top = accumulator + element.offsetTop
  if (element.offsetParent) {
    return offsetTop(element.offsetParent as HTMLElement, top)
  }
  return top
}

function offsetLeft(element: HTMLElement, accumulator = 0) {
  const left = accumulator + element.offsetLeft
  if (element.offsetParent) {
    return offsetLeft(element.offsetParent as HTMLElement, left)
  }
  return left
}

function scrollTop(element: HTMLElement, accumulator = 0) {
  const top = accumulator + element.scrollTop
  if (element.offsetParent) {
    return scrollTop(element.offsetParent as HTMLElement, top)
  }
  return top + window.scrollY
}

function scrollLeft(element: HTMLElement, accumulator = 0) {
  const left = accumulator + element.scrollLeft
  if (element.offsetParent) {
    return scrollLeft(element.offsetParent as HTMLElement, left)
  }
  return left + window.scrollX
}

export type SnapElementOptions = {
  align?: string | string[]
  ignoreSticky?: boolean
  ignoreTransform?: boolean
}

type Rect = {
  top: number
  left: number
  width: number
  height: number
  x: number
  y: number
  bottom: number
  right: number
  element: HTMLElement
}

export class SnapElement {
  element: HTMLElement
  options: SnapElementOptions
  align: string[]
  // @ts-expect-error
  rect: Rect = {}
  wrapperResizeObserver: ResizeObserver
  resizeObserver: ResizeObserver
  debouncedWrapperResize: () => void

  constructor(
    element: HTMLElement,
    {
      align = ['start'],
      ignoreSticky = true,
      ignoreTransform = false,
    }: SnapElementOptions = {}
  ) {
    this.element = element

    this.options = { align, ignoreSticky, ignoreTransform }

    this.align = [align].flat()

    this.debouncedWrapperResize = debounce(this.onWrapperResize, 500)

    this.wrapperResizeObserver = new ResizeObserver(this.debouncedWrapperResize)
    this.wrapperResizeObserver.observe(document.body)
    this.onWrapperResize()

    this.resizeObserver = new ResizeObserver(this.onResize)
    this.resizeObserver.observe(this.element)
    this.setRect({
      width: this.element.offsetWidth,
      height: this.element.offsetHeight,
    })
  }

  destroy() {
    this.wrapperResizeObserver.disconnect()
    this.resizeObserver.disconnect()
  }

  setRect({
    top,
    left,
    width,
    height,
    element,
  }: {
    top?: number
    left?: number
    width?: number
    height?: number
    element?: HTMLElement
  } = {}) {
    top = top ?? this.rect.top
    left = left ?? this.rect.left
    width = width ?? this.rect.width
    height = height ?? this.rect.height
    element = element ?? this.rect.element

    if (
      top === this.rect.top &&
      left === this.rect.left &&
      width === this.rect.width &&
      height === this.rect.height &&
      element === this.rect.element
    )
      return

    this.rect.top = top
    this.rect.y = top
    this.rect.width = width
    this.rect.height = height
    this.rect.left = left
    this.rect.x = left
    this.rect.bottom = top + height
    this.rect.right = left + width
  }

  onWrapperResize = () => {
    let top: number | undefined
    let left: number | undefined

    if (this.options.ignoreSticky) removeParentSticky(this.element)
    if (this.options.ignoreTransform) {
      top = offsetTop(this.element)
      left = offsetLeft(this.element)
    } else {
      const rect = this.element.getBoundingClientRect()
      top = rect.top + scrollTop(this.element)
      left = rect.left + scrollLeft(this.element)
    }
    if (this.options.ignoreSticky) addParentSticky(this.element)

    this.setRect({ top, left })
  }

  onResize = ([entry]: ResizeObserverEntry[]) => {
    if (!entry?.borderBoxSize[0]) return
    const width = entry.borderBoxSize[0].inlineSize
    const height = entry.borderBoxSize[0].blockSize

    this.setRect({ width, height })
  }
}
```

## File: `packages/snap/src/snap.ts`
```typescript
import type Lenis from 'lenis'
import type { VirtualScrollData } from 'lenis'
import { debounce } from './debounce'
import type { SnapElementOptions } from './element'
import { SnapElement } from './element'
import type { SnapItem, SnapOptions } from './types'
import type { UID } from './uid'
import { uid } from './uid'

// TODO:
// - fix wheel scrolling after limits (see console scroll to)
// - arrow, spacebar

type RequiredPick<T, F extends keyof T> = Omit<T, F> & Required<Pick<T, F>>

/**
 * Snap class to handle the snap functionality
 *
 * @example
 * const snap = new Snap(lenis, {
 *   type: 'mandatory', // 'mandatory', 'proximity' or 'lock'
 *   onSnapStart: (snap) => {
 *     console.log('onSnapStart', snap)
 *   },
 *   onSnapComplete: (snap) => {
 *     console.log('onSnapComplete', snap)
 *   },
 * })
 *
 * snap.add(500) // snap at 500px
 *
 * const removeSnap = snap.add(500)
 *
 * if (someCondition) {
 *   removeSnap()
 * }
 */
export class Snap {
  options: RequiredPick<SnapOptions, 'type' | 'debounce'>
  elements = new Map<UID, SnapElement>()
  snaps = new Map<UID, SnapItem>()
  viewport: { width: number; height: number } = {
    width: window.innerWidth,
    height: window.innerHeight,
  }
  isStopped = false
  onSnapDebounced: (e: VirtualScrollData) => void
  currentSnapIndex?: number

  constructor(
    private lenis: Lenis,
    {
      type = 'proximity',
      lerp,
      easing,
      duration,
      distanceThreshold = '50%', // useless when type is "mandatory"
      debounce: debounceDelay = 500,
      onSnapStart,
      onSnapComplete,
    }: SnapOptions = {}
  ) {
    if (!window.lenis) {
      window.lenis = {}
    }

    window.lenis.snap = true

    this.options = {
      type,
      lerp,
      easing,
      duration,
      distanceThreshold,
      debounce: debounceDelay,
      onSnapStart,
      onSnapComplete,
    }

    this.onWindowResize()
    window.addEventListener('resize', this.onWindowResize)

    this.onSnapDebounced = debounce(
      this.onSnap as (...args: unknown[]) => void,
      this.options.debounce
    )

    this.lenis.on('virtual-scroll', this.onSnapDebounced)
  }

  /**
   * Destroy the snap instance
   */
  destroy() {
    this.lenis.off('virtual-scroll', this.onSnapDebounced)
    window.removeEventListener('resize', this.onWindowResize)
    this.elements.forEach((element) => {
      element.destroy()
    })
  }

  /**
   * Start the snap after it has been stopped
   */
  start() {
    this.isStopped = false
  }

  /**
   * Stop the snap
   */
  stop() {
    this.isStopped = true
  }

  /**
   * Add a snap to the snap instance
   *
   * @param value The value to snap to
   * @param userData User data that will be forwarded through the snap event
   * @returns Unsubscribe function
   */
  add(value: number): () => void {
    const id = uid()

    this.snaps.set(id, { value })

    return () => this.snaps.delete(id)
  }

  /**
   * Add an element to the snap instance
   *
   * @param element The element to add
   * @param options The options for the element
   * @returns Unsubscribe function
   */
  addElement(
    element: HTMLElement,
    options: SnapElementOptions = {}
  ): () => void {
    const id = uid()

    this.elements.set(id, new SnapElement(element, options))

    return () => this.elements.delete(id)
  }

  addElements(
    elements: HTMLElement[],
    options: SnapElementOptions = {}
  ): () => void {
    const map = [...elements].map((element) =>
      this.addElement(element, options)
    )
    return () => {
      map.forEach((remove) => {
        remove()
      })
    }
  }

  private onWindowResize = () => {
    this.viewport.width = window.innerWidth
    this.viewport.height = window.innerHeight
  }

  private computeSnaps = () => {
    const { isHorizontal } = this.lenis

    let snaps = [...this.snaps.values()] as SnapItem[]

    this.elements.forEach(({ rect, align }) => {
      let value: number | undefined

      align.forEach((align) => {
        if (align === 'start') {
          value = rect.top
        } else if (align === 'center') {
          value = isHorizontal
            ? rect.left + rect.width / 2 - this.viewport.width / 2
            : rect.top + rect.height / 2 - this.viewport.height / 2
        } else if (align === 'end') {
          value = isHorizontal
            ? rect.left + rect.width - this.viewport.width
            : rect.top + rect.height - this.viewport.height
        }

        if (typeof value === 'number') {
          snaps.push({ value: Math.ceil(value) })
        }
      })
    })

    snaps = snaps.sort((a, b) => Math.abs(a.value) - Math.abs(b.value))

    return snaps
  }

  previous() {
    this.goTo((this.currentSnapIndex ?? 0) - 1)
  }

  next() {
    this.goTo((this.currentSnapIndex ?? 0) + 1)
  }

  goTo(index: number) {
    const snaps = this.computeSnaps()

    if (snaps.length === 0) return

    this.currentSnapIndex = Math.max(0, Math.min(index, snaps.length - 1))

    const currentSnap = snaps[this.currentSnapIndex]
    if (currentSnap === undefined) return

    this.lenis.scrollTo(currentSnap.value, {
      duration: this.options.duration,
      easing: this.options.easing,
      lerp: this.options.lerp,
      lock: this.options.type === 'lock',
      userData: { initiator: 'snap' },
      onStart: () => {
        this.options.onSnapStart?.({
          index: this.currentSnapIndex,
          ...currentSnap,
        })
      },
      onComplete: () => {
        this.options.onSnapComplete?.({
          index: this.currentSnapIndex,
          ...currentSnap,
        })
      },
    })
  }

  get distanceThreshold() {
    let distanceThreshold = Number.POSITIVE_INFINITY
    if (this.options.type === 'mandatory') return Number.POSITIVE_INFINITY

    const { isHorizontal } = this.lenis

    const axis = isHorizontal ? 'width' : 'height'

    if (
      typeof this.options.distanceThreshold === 'string' &&
      this.options.distanceThreshold.endsWith('%')
    ) {
      distanceThreshold =
        (Number(this.options.distanceThreshold.replace('%', '')) / 100) *
        this.viewport[axis]
    } else if (typeof this.options.distanceThreshold === 'number') {
      distanceThreshold = this.options.distanceThreshold
    } else {
      distanceThreshold = this.viewport[axis]
    }

    return distanceThreshold
  }

  private onSnap = (e: VirtualScrollData) => {
    if (this.isStopped) return

    if (e.event.type === 'touchmove') return

    if (
      this.options.type === 'lock' &&
      this.lenis.userData?.initiator === 'snap'
    )
      return

    let { scroll, isHorizontal } = this.lenis
    const delta = isHorizontal ? e.deltaX : e.deltaY
    scroll = Math.ceil(this.lenis.scroll + delta)

    const snaps = this.computeSnaps()

    if (snaps.length === 0) return

    let snapIndex: number | undefined

    const prevSnapIndex = snaps.findLastIndex(({ value }) => value < scroll)
    const nextSnapIndex = snaps.findIndex(({ value }) => value > scroll)

    if (this.options.type === 'lock') {
      if (delta > 0) {
        snapIndex = nextSnapIndex
      } else if (delta < 0) {
        snapIndex = prevSnapIndex
      }
    } else {
      const prevSnap = snaps[prevSnapIndex]!
      const distanceToPrevSnap = prevSnap
        ? Math.abs(scroll - prevSnap.value)
        : Number.POSITIVE_INFINITY

      const nextSnap = snaps[nextSnapIndex]!
      const distanceToNextSnap = nextSnap
        ? Math.abs(scroll - nextSnap.value)
        : Number.POSITIVE_INFINITY
      snapIndex =
        distanceToPrevSnap < distanceToNextSnap ? prevSnapIndex : nextSnapIndex
    }

    if (snapIndex === undefined) return
    if (snapIndex === -1) return

    snapIndex = Math.max(0, Math.min(snapIndex, snaps.length - 1))

    const snap = snaps[snapIndex]!

    const distance = Math.abs(scroll - snap.value)

    if (distance <= this.distanceThreshold) {
      this.goTo(snapIndex)
    }
  }

  resize() {
    this.elements.forEach((element) => {
      element.onWrapperResize()
    })
  }
}
```

## File: `packages/snap/src/types.ts`
```typescript
import type { EasingFunction } from 'lenis'

export type SnapItem = {
  value: number
}

export type OnSnapCallback = (item: SnapItem & { index?: number }) => void

export type SnapOptions = {
  /**
   * Snap type
   * @default 'proximity'
   */
  type?: 'mandatory' | 'proximity' | 'lock'
  /**
   * @description Linear interpolation (lerp) intensity (between 0 and 1)
   */
  lerp?: number
  /**
   * @description The easing function to use for the snap animation
   */
  easing?: EasingFunction
  /**
   * @description The duration of the snap animation (in s)
   */
  duration?: number
  /**
   * @default '50%'
   * @description The distance threshold from the snap point to the scroll position. Ignored when `type` is `mandatory`. If a percentage, it is relative to the viewport size. If a number, it is absolute.
   */
  distanceThreshold?: number | `${number}%`
  /**
   * @default 500
   * @description The debounce delay (in ms) to prevent snapping too often.
   */
  debounce?: number
  /**
   * @description Called when the snap starts
   */
  onSnapStart?: OnSnapCallback
  /**
   * @description Called when the snap completes
   */
  onSnapComplete?: OnSnapCallback
}
```

## File: `packages/snap/src/uid.ts`
```typescript
let index = 0

export type UID = number

export function uid(): UID {
  return index++
}
```

## File: `packages/vue/README.md`
```markdown
# lenis/vue

## Introduction
lenis/vue provides a `<VueLenis>` component that creates a [Lenis](https://github.com/darkroomengineering/lenis) instance and provides it to its children via context. This allows you to use Lenis in your Vue app without worrying about passing the instance down through props. It also provides a `useLenis` hook that allows you to access the Lenis instance from any component in your app. lenis/vue provides a vueLenisPlugin that you can use to register the component globally. This allows you to use the component in your templates without having to import it, by using the `vue-lenis` template tag.


## Installation

```bash
npm i lenis
```

### Vue
```js
// main.js
import { createApp } from 'vue'
import LenisVue from 'lenis/vue'

const app = createApp({})

app.use(LenisVue)
```

### Nuxt

```js
// nuxt.config.js
export default defineNuxtConfig({
  modules: ['lenis/nuxt'],
})
```

## Usage

```vue
<script setup>
import { VueLenis, useLenis } from 'lenis/vue' // Also available as global imports, no need to import them manually
import { watch } from 'vue'

const lenisOptions = {
  // lenis options (optional)
}

const lenis = useLenis((lenis) => {
  // called every scroll
  console.log(lenis)
})

watch(
  lenis,
  (lenis) => {
    // lenis instance
    console.log(lenis)
  },
  { immediate: true }
)
</script>

<template>
  <VueLenis root :options="lenisOptions" />
  <!-- content -->
</template>
```

## Props
- `options`: [Lenis options](https://github.com/darkroomengineering/lenis#instance-settings).
- `root`: if `true`, Lenis will be instanciate using `<html>` scroll, then you can use the `useLenis` hook to access the Lenis instance from anywhere in your app. Default: `false`.

## Hooks
Once the Lenis context is set (components mounted inside `<VueLenis>` or `<vue-lenis>`) you can use these handy hooks:

`useLenis` is a hook that returns the Lenis instance

The hook takes two arguments:
- `callback`: The function to be called whenever a scroll event is emitted
- `priority`: Manage callback execution order

```vue
<script setup>
import { VueLenis, useLenis } from 'lenis/vue'
import { watch } from 'vue'

const scrollCallback = (lenis) => {
  // called on every scroll
  // useLenis provides the lenis instance as an argument
}

const lenis = useLenis(scrollCallback, 0) // where 0 is the default callback priority
</script>

<template>
  <VueLenis root />
  <!-- content -->
</template>
```





## Examples

### GSAP integration

```vue
<script setup>
import { ref, watchEffect } from 'vue'
import { VueLenis, useLenis } from 'lenis/vue'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

const lenisRef = ref()

watchEffect((onInvalidate) => {
   if (!lenisRef.value?.lenis) return

  //  if using GSAP ScrollTrigger, update ScrollTrigger on scroll
  lenisRef.value.lenis.on('scroll', ScrollTrigger.update)

  // add the Lenis requestAnimationFrame (raf) method to GSAP's ticker
  // this ensures Lenis's smooth scroll animation updates on each GSAP tick
  function update(time) {
    lenisRef.value.lenis.raf(time * 1000)
  }
  gsap.ticker.add(update)

  // disable lag smoothing in GSAP to prevent any delay in scroll animations
  gsap.ticker.lagSmoothing(0)

  // clean up GSAP's ticker from the previous execution of watchEffect, or when the effect is stopped
  onInvalidate(() => {
    gsap.ticker.remove(update)
  })
})

// if using GSAP ScrollTrigger, remember to register the plugin
onMounted(() => {
  gsap.registerPlugin(ScrollTrigger)
})
</script>

<template>
  <VueLenis root ref="lenisRef" :options="{ autoRaf: false }" />
  <!-- content -->
</template>
```

### Motion Integration
```vue
<script setup>
import { VueLenis } from 'lenis/vue'
import { cancelFrame, frame } from 'motion-v'
import { onMounted, onUnmounted, ref } from 'vue'

const lenisRef = ref()

function update({ timestamp }) {
  lenisRef.value?.lenis?.raf(timestamp)
}

onMounted(() => {
  frame.update(update, true)
})

onUnmounted(() => {
  cancelFrame(update)
})
</script>

<template>
  <VueLenis ref="lenisRef" root :options="{ autoRaf: false }">
  <!-- content -->
</template>
```

<br/>

## License

MIT © [darkroom.engineering](https://github.com/darkroomengineering)
```

## File: `packages/vue/index.ts`
```typescript
// This file serves as an entry point for the package
export {
  VueLenis as Lenis,
  VueLenis,
  vueLenisPlugin as default,
} from './src/provider'
export { useLenis } from './src/use-lenis'
```

## File: `packages/vue/package.json`
```json
{
  "name": "lenis-vue",
  "type": "module",
  "devDependencies": {
    "vue": "^3.5.13"
  }
}
```

## File: `packages/vue/nuxt/module.ts`
```typescript
import {
  addComponent,
  addImports,
  addPlugin,
  createResolver,
  defineNuxtModule,
} from '@nuxt/kit'

// Module options TypeScript interface definition
export type ModuleOptions = Record<string, never>

const nuxtModule = defineNuxtModule<ModuleOptions>({
  meta: {
    name: 'lenis/nuxt',
    configKey: 'lenis',
  },
  // Default configuration options of the Nuxt module
  defaults: {},
  setup(_options, _nuxt) {
    const { resolve } = createResolver(import.meta.url)

    addPlugin({
      src: resolve('./nuxt/runtime/lenis.mjs'),
      name: 'lenis',
    })

    addImports({ name: 'useLenis', from: 'lenis/vue' })
    addComponent({
      name: 'VueLenis',
      filePath: 'lenis/vue',
      global: true,
      export: 'VueLenis',
    })
  },
})

export default nuxtModule
export * from 'lenis/vue'
```

## File: `packages/vue/nuxt/tsconfig.json`
```json
{
  "extends": "../../../tsconfig.json",
  "compilerOptions": {
    "baseUrl": "./",
    "paths": {
      "#imports": ["types/imports.d.ts"],
      "#app": ["types/app.d.ts"]
    }
  }
}
```

## File: `packages/vue/nuxt/runtime/lenis.ts`
```typescript
import vuePlugin from 'lenis/vue'
import type { Plugin } from '#app'
import { defineNuxtPlugin } from '#imports'

const plugin = defineNuxtPlugin({
  name: 'lenis',
  setup(nuxtApp: unknown) {
    ;(nuxtApp as { vueApp: { use: (plugin: unknown) => void } }).vueApp.use(
      vuePlugin
    )
  },
}) satisfies Plugin

export default plugin
```

## File: `packages/vue/nuxt/types/app.d.ts`
```typescript
declare module '#app' {
  export interface Plugin {
    name?: string
    setup: (nuxtApp: unknown) => void
  }
}
```

## File: `packages/vue/nuxt/types/imports.d.ts`
```typescript
import type { Plugin } from '#app'

declare module '#imports' {
  export function defineNuxtPlugin(plugin: Plugin): Plugin
}
```

## File: `packages/vue/src/provider.ts`
```typescript
import Lenis, { type LenisOptions, type ScrollCallback } from 'lenis'
import type {
  HTMLAttributes,
  InjectionKey,
  Plugin,
  PropType,
  ShallowRef,
  ToRefs,
} from 'vue'
import {
  defineComponent,
  h,
  onWatcherCleanup,
  provide,
  reactive,
  ref,
  shallowRef,
  watch,
} from 'vue'
import { globalAddCallback, globalLenis, globalRemoveCallback } from './store'

export const LenisSymbol: InjectionKey<ShallowRef<Lenis | undefined>> =
  Symbol('LenisContext')
export const AddCallbackSymbol: InjectionKey<
  ((callback: ScrollCallback, priority: number) => void) | undefined
> = Symbol('AddCallback')
export const RemoveCallbackSymbol: InjectionKey<
  ((callback: ScrollCallback) => void) | undefined
> = Symbol('RemoveCallback')

export type LenisExposed = {
  wrapper?: HTMLDivElement
  content?: HTMLDivElement
  lenis?: Lenis
}

const VueLenisImpl = defineComponent({
  name: 'VueLenis',
  props: {
    root: {
      type: Boolean as PropType<boolean>,
      default: false,
    },
    autoRaf: {
      type: Boolean as PropType<boolean>,
      default: true,
    },
    options: {
      type: Object as PropType<LenisOptions>,
      default: () => ({}),
    },
    props: {
      type: Object as PropType<HTMLAttributes>,
      default: () => ({}),
    },
  },
  setup(props, { slots, expose }) {
    const lenisRef = shallowRef<Lenis>()
    const wrapper = ref<HTMLDivElement>()
    const content = ref<HTMLDivElement>()
    // Setup exposed properties
    expose<ToRefs<LenisExposed>>({
      lenis: lenisRef,
      wrapper,
      content,
    })

    // Sync options
    watch(
      [() => props.options, wrapper, content],
      () => {
        const isClient = typeof window !== 'undefined'

        if (!isClient) return

        if (!(props.root || (wrapper.value && content.value))) return

        lenisRef.value = new Lenis({
          ...props.options,
          ...(!props.root
            ? {
                wrapper: wrapper.value,
                content: content.value,
              }
            : {}),
          autoRaf: props.options?.autoRaf ?? props.autoRaf,
        })

        onWatcherCleanup(() => {
          lenisRef.value?.destroy()
          lenisRef.value = undefined
        })
      },
      { deep: true, immediate: true }
    )

    const callbacks = reactive<
      { callback: ScrollCallback; priority: number }[]
    >([])

    function addCallback(callback: ScrollCallback, priority: number) {
      callbacks.push({ callback, priority })
      callbacks.sort((a, b) => a.priority - b.priority)
    }

    function removeCallback(callback: ScrollCallback) {
      callbacks.splice(
        callbacks.findIndex((cb) => cb.callback === callback),
        1
      )
    }

    const onScroll: ScrollCallback = (data) => {
      for (const { callback } of callbacks) {
        callback(data)
      }
    }

    watch(
      [lenisRef, () => props.root],
      ([lenis, root]) => {
        lenis?.on('scroll', onScroll)

        if (root) {
          globalLenis.value = lenis
          globalAddCallback.value = addCallback
          globalRemoveCallback.value = removeCallback

          onWatcherCleanup(() => {
            globalLenis.value = undefined
            globalAddCallback.value = undefined
            globalRemoveCallback.value = undefined
          })
        }
      },
      { immediate: true }
    )

    if (!props.root) {
      provide(LenisSymbol, lenisRef)
      provide(AddCallbackSymbol, addCallback)
      provide(RemoveCallbackSymbol, removeCallback)
    }

    return () => {
      if (props.root) {
        return slots.default?.()
      }
      return h('div', { ref: wrapper, ...props?.props }, [
        h('div', { ref: content }, slots.default?.()),
      ])
    }
  },
})

export const VueLenis = VueLenisImpl as typeof VueLenisImpl & {
  new (): LenisExposed
}

export const vueLenisPlugin: Plugin = (app) => {
  app.component('vue-lenis', VueLenis)
  // Setup a global provide to silence top level useLenis injection warning
  app.provide(LenisSymbol, shallowRef(undefined))
  app.provide(AddCallbackSymbol, undefined)
  app.provide(RemoveCallbackSymbol, undefined)
}

// @ts-expect-error
declare module '@vue/runtime-core' {
  export interface GlobalComponents {
    'vue-lenis': typeof VueLenis
  }
}
```

## File: `packages/vue/src/store.ts`
```typescript
import type Lenis from 'lenis'
import type { ScrollCallback } from 'lenis'
import { shallowRef } from 'vue'

export const globalLenis = shallowRef<Lenis>()
export const globalAddCallback =
  shallowRef<(callback: ScrollCallback, priority: number) => void>()
export const globalRemoveCallback =
  shallowRef<(callback: ScrollCallback) => void>()
```

## File: `packages/vue/src/use-lenis.ts`
```typescript
import type Lenis from 'lenis'
import type { ScrollCallback } from 'lenis'
import { type ComputedRef, computed, inject, nextTick, onWatcherCleanup, watch } from 'vue'
import {
  AddCallbackSymbol,
  LenisSymbol,
  RemoveCallbackSymbol,
} from './provider'
import { globalAddCallback, globalLenis, globalRemoveCallback } from './store'

export function useLenis(callback?: ScrollCallback, priority = 0): ComputedRef<Lenis | undefined> {
  const lenisInjection = inject(LenisSymbol)
  const addCallbackInjection = inject(AddCallbackSymbol)
  const removeCallbackInjection = inject(RemoveCallbackSymbol)

  const addCallback = computed(() =>
    addCallbackInjection ? addCallbackInjection : globalAddCallback.value
  )
  const removeCallback = computed(() =>
    removeCallbackInjection
      ? removeCallbackInjection
      : globalRemoveCallback.value
  )

  const lenis = computed(() =>
    lenisInjection?.value ? lenisInjection.value : globalLenis.value
  )

  if (typeof window !== 'undefined') {
    // Wait two ticks to make sure the lenis instance is mounted
    nextTick(() => {
      nextTick(() => {
        // @ts-expect-error - import.meta.env is available in vite and nuxt
        if (!lenis.value && import.meta.env.DEV) {
          console.warn(
            'No lenis instance found, either mount a root lenis instance or wrap your component in a lenis provider'
          )
        }
      })
    })
  }

  watch(
    [lenis, addCallback, removeCallback],
    ([lenis, addCallback, removeCallback]) => {
      if (!(lenis && addCallback && removeCallback && callback)) return

      addCallback?.(callback, priority)
      callback?.(lenis!)

      onWatcherCleanup(() => {
        removeCallback?.(callback)
      })
    },
    {
      immediate: true,
    }
  )
  return lenis
}
```

## File: `playground/.gitignore`
```
# build output
dist/
# generated types
.astro/

# dependencies
node_modules/

# logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*


# environment variables
.env
.env.production

# macOS-specific files
.DS_Store

# jetbrains setting folder
.idea/

env.d.ts
```

## File: `playground/astro.config.mjs`
```
import path from 'node:path'
import react from '@astrojs/react'
import vue from '@astrojs/vue'
import { defineConfig } from 'astro/config'

const root = path.resolve('..')

export default defineConfig({
  integrations: [react(), vue({ appEntrypoint: './vue/setup' })],
  devToolbar: {
    enabled: false,
  },
  srcDir: './www',
  vite: {
    resolve: {
      alias: {
        'lenis/dist/lenis.css': path.resolve(root, 'dist/lenis.css'),
        'lenis/react': path.resolve(root, 'dist/lenis-react.mjs'),
        'lenis/snap': path.resolve(root, 'dist/lenis-snap.mjs'),
        'lenis/vue': path.resolve(root, 'dist/lenis-vue.mjs'),
        lenis: path.resolve(root, 'dist/lenis.mjs'),
      },
    },
  },
})
```

## File: `playground/package.json`
```json
{
  "name": "playground",
  "type": "module",
  "version": "0.0.1",
  "scripts": {
    "dev": "astro dev --host",
    "start": "astro dev",
    "build": "astro check && astro build",
    "preview": "astro preview",
    "astro": "astro"
  },
  "dependencies": {
    "@astrojs/check": "^0.9.4",
    "@astrojs/react": "^4.1.6",
    "@astrojs/vue": "^5.0.6",
    "@types/react": "^19.0.7",
    "@types/react-dom": "^19.0.3",
    "astro": "^5.1.8",
    "lenis": "*",
    "lorem-ipsum": "^2.0.8",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "stats-js": "1.0.1",
    "typescript": "^5.7.3",
    "vue": "^3.5.13"
  }
}
```

## File: `playground/tsconfig.json`
```json
{
  "extends": "astro/tsconfigs/strict",
  "compilerOptions": {
    "jsx": "react-jsx",
    "jsxImportSource": "react",
    "baseUrl": ".",
    "paths": {
      "~/*": ["./*"]
    }
  }
}
```

## File: `playground/core/browser.js`
```javascript
const lenis = new Lenis()

lenis.on('scroll', (e) => {
  console.log(e)
})

function raf(time) {
  lenis.raf(time)
  requestAnimationFrame(raf)
}

requestAnimationFrame(raf)
```

## File: `playground/core/static.html`
```html
<html lang="en">
  <head>
    <style>
      body {
        height: 300vh;
      }
    </style>
    <script src="../../dist/lenis.min.js"></script>
    <script>
      const lenis = new Lenis({
        autoRaf: true,
      })
      console.log(lenis)
    </script>
  </head>
  <body>
    Lorem ipsum dolor, sit amet consectetur adipisicing elit. Inventore aliquid
    aliquam quam officiis hic ut voluptatibus dicta perferendis, voluptate iure
    modi iste ratione explicabo architecto impedit ipsa. Blanditiis, tenetur
    itaque.
  </body>
</html>
```

## File: `playground/core/style.css`
```css
#scroll-to-top {
  position: fixed;
  bottom: 20px;
  right: 20px;
  padding: 10px;
  border: 1px solid #ccc;
  background-color: #fff;
  cursor: pointer;
}

#nested-horizontal {
  width: 50vw;
  margin: 0 auto;
  /* height: 200px; */
  overflow-x: auto;
  overscroll-behavior: contain;

  #nested-horizontal-content {
    width: 1000px;
    height: 100%;
  }
}

#nested {
  width: 50vw;
  margin: 0 auto;
  height: 200px;
  overflow-y: auto;
  overscroll-behavior: contain;
  /* overflow-x: auto; */
}

#debug {
  position: fixed;
  top: 4rem;
}

/* html {
  overflow: hidden;
  height: 100%;
}

body {
  overflow-y: auto;
  height: 100%;
} */

/* this prevents UI to collapse on scroll */
/* html,
body {
  overflow: hidden;
  height: 100%;
}

main {
  height: 100%;
  overflow-y: auto;
} */

.lenis-stopped {
  background-color: red;
}

/* html {
  overflow: hidden;
} */
```

## File: `playground/core/test.ts`
```typescript
import Lenis from 'lenis'
import { LoremIpsum } from 'lorem-ipsum'

document.querySelector('#nested-content')!.innerHTML =
  new LoremIpsum().generateParagraphs(60)
document.querySelector('#nested-horizontal-content')!.innerHTML =
  new LoremIpsum().generateParagraphs(3)
document
  .querySelector('#app')!
  .insertAdjacentText('afterbegin', new LoremIpsum().generateParagraphs(20))
document
  .querySelector('#app')!
  .insertAdjacentText(
    'beforeend',
    `${new LoremIpsum().generateParagraphs(40)}test123`
  )

// document.querySelector('main')?.addEventListener('scrollend', () => {
//   console.log('scrollend')
// })

window.addEventListener('scroll', (_e) => {
  // console.log('window scroll', e)
})

window.addEventListener('scrollend', (e) => {
  // console.log('window scrollend', e)
})

document.querySelector('#nested')?.addEventListener('scrollend', (_e) => {
  // console.log('nested scrollend', e)
})

window.addEventListener('hashchange', () => {
  console.log('hashchange')
})

const lenis = new Lenis({
  smoothWheel: true,
  autoRaf: true,
  anchors: {
    // onStart: () => {
    //   console.log('onStart')
    // },
    // onComplete: () => {
    //   console.log('onComplete')
    // },
  },
  autoToggle: true,
  allowNestedScroll: true,
  syncTouch: true,
  infinite: true,
  stopInertiaOnNavigate: true,
  // virtualScroll: ({ event }) => {
  //   console.log(lenis.options.syncTouch)

  //   return true
  // },
  // duration: 1,
  // infinite: true,
  // lerp: 0.5,
  // duration: 10,
  // easing: (t) => t,
  // syncTouch: true,
  // lerp: 0.01,
  // wrapper: document.body,
  // content: document.querySelector('main'),
  // wrapper: document.querySelector('main')!,
  // content: document.querySelector('main')?.children[0],
  // autoResize: false,
  // lerp: 0.9,
  // virtualScroll: (e) => {
  //   // e.deltaY *= 10
  //   return !e.event.shiftKey
  //   // return true
  // },
  // duration: 2,
  // easing: (t) => t,
  // prevent: () => {
  //   return true
  // },
  // prevent: (node) => {
  //   return (
  //     node.classList?.contains('lenis-scrolling') &&
  //     node.classList?.contains('lenis-smooth') &&
  //     !node.classList?.contains('lenis-stopped')
  //   )
  // },
})

// const _nestedLenis = new Lenis({
//   wrapper: document.querySelector('#nested')!,
//   content: document.querySelector('#nested-content')!,
//   autoRaf: true,
//   // overscroll: false,
//   // orientation: 'horizontal',
//   // gestureOrientation: 'horizontal',
//   // infinite: true,
// })

lenis.on('scroll', (_e) => {
  // console.log('scroll', e)
})

// document.querySelectorAll('a[href*="#"]').forEach((node) => {
//   node.addEventListener('click', (e) => {
//     // lenis.reset()
//     // e.preventDefault()
//     // console.log(node.href)
//   })
// })

// window.addEventListener('hashchange', () => {
//   console.log('hashchange')
// })

// const nestedLenis = new Lenis({
//   wrapper: document.querySelector('#nested')!,
//   content: document.querySelector('#nested-content')!,
//   autoRaf: true,
//   // overscroll: false,
//   // orientation: 'horizontal',
//   // gestureOrientation: 'horizontal',
//   // infinite: true,

//   // smoothWheel: false,
// })

// window.nestedLenis = nestedLenis

// console.log(lenis.dimensions.height)
lenis.on('scroll', (_e) => {
  // console.log(e.isScrolling)
  // console.log(e.scroll, e.velocity)
  // console.log(e.scroll, e.velocity, e.isScrolling, e.userData)
})
// lenis.on('virtual-scroll', (e) => {
//   // console.log(e)
//   // e.deltaY *= 10
//   // e.cancel = true
// })
// window.lenis = lenis

declare global {
  interface Window {
    lenis: Lenis
  }
}

// window.addEventListener('resize', () => {
//   lenis.resize()

//   console.log(lenis.actualScroll, lenis.scroll, window.scrollY)
// })

// Proxy test for lenis
// const proxyLenis = new Proxy(lenis, {})

// const scroll100 = document.getElementById('scroll-100')

// scroll100?.addEventListener('click', () => {
//   // proxyLenis?.scrollTo(100, {
//   //   lerp: 0.1,
//   // })
//   lenis.scrollTo(100, {
//     lerp: 0.1,
//   })
// })

// document.documentElement.addEventListener('wheel', (e) => {
//   console.log('wheel')
// })

// function raf(time: number) {
//   lenis.raf(time)
//   nestedLenis.raf(time)
//   requestAnimationFrame(raf)
// }

// requestAnimationFrame(raf)

document.getElementById('stop')?.addEventListener('click', () => {
  // document.documentElement.style.overflow = 'hidden'
  lenis.stop()
})

document.getElementById('start')?.addEventListener('click', () => {
  // document.documentElement.style.overflow = 'auto'
  lenis.start()
})

document.getElementById('scroll-start')?.addEventListener('click', () => {
  lenis.scrollTo(100, {
    lock: true,
    duration: 1,
    onComplete: () => {
      console.log('onComplete')
    },
  })
})

document.getElementById('scroll-center')?.addEventListener('click', () => {
  lenis.scrollTo(lenis.limit / 2, {
    // duration: 10,
    // easing: (t) => t,
  })
})

document.getElementById('scroll-end')?.addEventListener('click', () => {
  lenis.scrollTo(lenis.limit - 100)
})

// const stopButton = document.getElementById('stop')
// const startButton = document.getElementById('start')

// stopButton?.addEventListener('click', () => {
//   lenis.stop()
//   console.log('stop')
// })

// startButton?.addEventListener('click', () => {
//   lenis.start()
// })
```

## File: `playground/horizontal/browser.js`
```javascript
const lenis = new Lenis()

lenis.on('scroll', (e) => {
  console.log(e)
})

function raf(time) {
  lenis.raf(time)
  requestAnimationFrame(raf)
}

requestAnimationFrame(raf)
```

## File: `playground/horizontal/static.html`
```html
<html lang="en">
  <head>
    <style>
      body {
        height: 300vh;
      }
    </style>
    <script src="../../dist/lenis.min.js"></script>
    <script>
      const lenis = new Lenis({
        autoRaf: true,
      })
      console.log(lenis)
    </script>
  </head>
  <body>
    Lorem ipsum dolor, sit amet consectetur adipisicing elit. Inventore aliquid
    aliquam quam officiis hic ut voluptatibus dicta perferendis, voluptate iure
    modi iste ratione explicabo architecto impedit ipsa. Blanditiis, tenetur
    itaque.
  </body>
</html>
```

## File: `playground/horizontal/style.css`
```css
html {
  overflow-y: clip;
}

#wrapper {
  display: flex;
  height: 100vh;
  align-items: center;
}

#about,
#work,
#work2,
#contact {
  width: 80vw;
  flex-shrink: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

#about {
  background-color: rgb(255, 152, 162);
}

#work {
  background-color: rgb(213, 133, 169);
  overflow-x: auto;
  justify-content: flex-start;
  height: 50%;
  /* background: repeating-radial-gradient(circle, #000, #111 1px, #000 2px); */
  /* filter: blur(2px) brightness(1.2) contrast(2) saturate(3);
  mix-blend-mode: difference;
  animation: insane-rotate 0.1s infinite linear;
  transform: scale(1.001); */
}

#work2 {
  background-color: rgb(255, 152, 162);
  height: 50%;
  overflow-y: auto;

  #work2-content {
    display: block;
  }
}

#contact {
  background-color: rgb(163, 120, 164);
}

#work-content {
  min-width: 100vw;
  height: 50%;
}
```

## File: `playground/horizontal/test.ts`
```typescript
import Lenis from 'lenis'
import { LoremIpsum } from 'lorem-ipsum'

document.querySelector('#work2-content')!.innerHTML =
  new LoremIpsum().generateParagraphs(30)

new Lenis({
  orientation: 'horizontal',
  // gestureOrientation: 'vertical',
  autoRaf: true,
  allowNestedScroll: true,
  syncTouch: true,
  anchors: true,
  stopInertiaOnNavigate: true,
  // virtualScroll: (data) => {
  //   data.deltaX = 0
  //   // data.deltaY =  0.00001
  //   if (data.deltaY === 0 && data.deltaX === 0) {
  //     data.deltaY = 0.00001
  //   }
  //   console.log(data)
  //   return true
  // },
})

// setInterval(() => {
//   document.querySelector('#work').style.width = `${50 + Math.random() * 30}vw`
// }, 1000)
```

## File: `playground/infinite/browser.js`
```javascript
const lenis = new Lenis()

lenis.on('scroll', (e) => {
  console.log(e)
})

function raf(time) {
  lenis.raf(time)
  requestAnimationFrame(raf)
}

requestAnimationFrame(raf)
```

## File: `playground/infinite/static.html`
```html
<html lang="en">
  <head>
    <style>
      body {
        height: 300vh;
      }
    </style>
    <script src="../../dist/lenis.min.js"></script>
    <script>
      const lenis = new Lenis({
        autoRaf: true,
      })
      console.log(lenis)
    </script>
  </head>
  <body>
    Lorem ipsum dolor, sit amet consectetur adipisicing elit. Inventore aliquid
    aliquam quam officiis hic ut voluptatibus dicta perferendis, voluptate iure
    modi iste ratione explicabo architecto impedit ipsa. Blanditiis, tenetur
    itaque.
  </body>
</html>
```

## File: `playground/infinite/style.css`
```css
html {
  overflow-x: clip;
}

img {
  width: 100%;
}
```

## File: `playground/infinite/test.ts`
```typescript
import Lenis from 'lenis'
import Stats from 'stats-js'

new Lenis({
  infinite: true,
  autoRaf: true,
  syncTouch: true,
})

function isPrime(num: number) {
  if (num < 2) return false
  for (let i = 2; i * i <= num; i++) {
    if (num % i === 0) return false
  }
  return true
}

function sumPrimes(limit: number) {
  let sum = 0
  for (let i = 2; i <= limit; i++) {
    if (isPrime(i)) {
      sum += i
    }
  }
  return sum
}

// function raf() {
//   // const sum = sumPrimes(Math.random() * 500000)
//   // console.log(sum)
//   requestAnimationFrame(raf)
// }

// raf()

// setInterval(() => {
//   document.querySelector('#work').style.width = `${50 + Math.random() * 30}vw`
// }, 1000)

var stats = new Stats()
stats.showPanel(0) // 0: fps, 1: ms, 2: mb, 3+: custom
document.body.appendChild(stats.dom)

function animate() {
  stats.begin()

  sumPrimes(300000)

  // monitored code goes here

  stats.end()

  requestAnimationFrame(animate)
}

requestAnimationFrame(animate)
```

## File: `playground/nuxt/.gitignore`
```
# Nuxt dev/build outputs
.output
.data
.nuxt
.nitro
.cache
dist

# Node dependencies
node_modules

# Logs
logs
*.log

# Misc
.DS_Store
.fleet
.idea

# Local env files
.env
.env.*
!.env.example
```

## File: `playground/nuxt/README.md`
```markdown
# Nuxt Minimal Starter

Look at the [Nuxt documentation](https://nuxt.com/brain/knowledge/docs_legacy/getting-started/introduction) to learn more.

## Setup

Make sure to install dependencies:

```bash
# npm
npm install

# pnpm
pnpm install

# yarn
yarn install

# bun
bun install
```

## Development Server

Start the development server on `http://localhost:3000`:

```bash
# npm
npm run dev

# pnpm
pnpm dev

# yarn
yarn dev

# bun
bun run dev
```

## Production

Build the application for production:

```bash
# npm
npm run build

# pnpm
pnpm build

# yarn
yarn build

# bun
bun run build
```

Locally preview production build:

```bash
# npm
npm run preview

# pnpm
pnpm preview

# yarn
yarn preview

# bun
bun run preview
```

Check out the [deployment documentation](https://nuxt.com/brain/knowledge/docs_legacy/getting-started/deployment) for more information.
```

## File: `playground/nuxt/app.vue`
```
<script setup lang="ts">
import gsap from 'gsap'
import { watch, watchEffect } from 'vue'

const lenis = useLenis((lenis) => {
  console.log('page callback', lenis)
})

watch(
  lenis,
  (lenis) => {
    console.log('page', lenis)
  },
  { immediate: true }
)

const lenisRef = useTemplateRef('lenisRef')

watchEffect((onInvalidate) => {
  function update(time: number) {
    lenisRef.value?.lenis?.raf(time * 1000)
  }
  gsap.ticker.add(update)

  onInvalidate(() => {
    gsap.ticker.remove(update)
  })
})
</script>

<template>
  <nav>
    <NuxtLink to="/">Home</NuxtLink>
    <NuxtLink to="/about">About</NuxtLink>
  </nav>
  <VueLenis root :options="{ autoRaf: false }" ref="lenisRef" />
  <NuxtPage />
</template>

<style>
* {
  margin: 0;
}
</style>

<style scoped>
#app {
  padding-top: 24px;
}

nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  display: flex;
  gap: 1rem;
}

.scroller {
  height: 100vh;
  overflow-y: auto;
}
</style>
```

## File: `playground/nuxt/nuxt.config.ts`
```typescript
// https://nuxt.com/brain/knowledge/docs_legacy/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  modules: ['lenis/nuxt'],
})
```

## File: `playground/nuxt/package.json`
```json
{
  "name": "playground-nuxt",
  "type": "module",
  "scripts": {
    "build": "nuxt build",
    "dev": "nuxt dev",
    "generate": "nuxt generate",
    "preview": "nuxt preview"
  },
  "dependencies": {
    "lenis": "*",
    "nuxt": "^3.15.3",
    "vue": "latest",
    "vue-router": "latest",
    "gsap": "latest"
  }
}
```

## File: `playground/nuxt/tsconfig.json`
```json
{
  // https://nuxt.com/brain/knowledge/docs_legacy/guide/concepts/typescript
  "extends": "./.nuxt/tsconfig.json"
}
```

## File: `playground/nuxt/components/inner.vue`
```
<script setup>
// import { useLenis } from 'lenis/vue'

// const lenis = useLenis((lenis) => {
//   console.log('inner callback', lenis)
// })

// watch(lenis, (lenis) => {
//   console.log('inner lenis', lenis)
// })
</script>

<template>
  <div>Inner</div>
</template>
```

## File: `playground/nuxt/pages/about.vue`
```
<script setup>
import { useLenis } from 'lenis/vue'

const lenis = useLenis((lenis) => {
  console.log('page callback', lenis)
})

watch(lenis, (lenis) => {
  console.log('page', lenis)
})
</script>

<template>
  <!-- <vue-lenis root /> -->
  <!-- <vue-lenis class="scroller"> -->
  <div class="content">About <Inner /></div>
  <!-- </vue-lenis> -->
</template>

<style scoped>
.content {
  /* min-height: 200vh; */
  padding-top: 24px;
  min-height: 200vh;
}

.scroller {
  height: 100vh;
  overflow-y: auto;
}
</style>
```

## File: `playground/nuxt/pages/index.vue`
```
//
<script setup>
// import Inner from '../components/inner.vue'
// import { useLenis } from 'lenis/vue'
// import { watchEffect } from 'vue'

// const lenisRef = ref()

// watchEffect(() => {
//   console.log('lenisRef', lenisRef.value?.lenis)
// })
//
</script>

<template>
  <!-- <vue-lenis class="scroller" ref="lenisRef"> -->
  <div class="content">Home <Inner /></div>
  <!-- </vue-lenis> -->
</template>

<style scoped>
.content {
  /* min-height: 200vh; */
  padding-top: 24px;
  min-height: 200vh;
}

.scroller {
  /* height: 100vh;
  overflow-y: auto; */
  pointer-events: none;
}
</style>
```

## File: `playground/nuxt/plugins/lenis.ts`
```typescript
export default defineNuxtPlugin((_nuxtApp) => {
  //   nuxtApp.vueApp.use(LenisVue)
})
```

## File: `playground/nuxt/public/robots.txt`
```

```

## File: `playground/nuxt/server/tsconfig.json`
```json
{
  "extends": "../.nuxt/tsconfig.server.json"
}
```

## File: `playground/react/app.tsx`
```tsx
import { type LenisRef, ReactLenis, useLenis } from 'lenis/react'
import { LoremIpsum } from 'lorem-ipsum'
import { useRef, useState } from 'react'

function App() {
  const [lorem] = useState(() => new LoremIpsum().generateParagraphs(200))
  const [count, setCount] = useState(0)

  useLenis()

  const lenisRef = useRef<LenisRef>(null)

  return (
    <ReactLenis
      className={`wrapper a-${count}`}
      root="asChild"
      ref={lenisRef}
      options={{ autoToggle: true }}
    >
      <div className="debug-panel">
        <button type="button" onClick={() => setCount((c) => c + 1)}>
          Re-render ({count})
        </button>
        <p>
          <strong>DOM className:</strong>
        </p>
        <code id="class-display" />
        <p className="hint">
          Scroll, then click the button. Lenis classes should persist.
        </p>
      </div>
      {lorem}
    </ReactLenis>
  )
}

// Poll DOM className outside React to avoid extra renders
setInterval(() => {
  const wrapper = document.querySelector('.lenis')
  const display = document.getElementById('class-display')
  if (wrapper && display) {
    display.textContent = wrapper.className
  }
}, 100)

export default App
```

## File: `playground/react/style.css`
```css
html:not(.lenis) {
  body,
  & {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
  }
  body {
    position: fixed;
    overscroll-behavior-y: none;
    overscroll-behavior-x: none;
  }

  .lenis {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    overflow-y: scroll;
    -ms-scroll-chaining: none;
    overscroll-behavior: contain;
    background: #0b41cd;
  }
}

.wrapper.lenis-scrolling {
  background: #1a6b2a;
}

.debug-panel {
  position: fixed;
  bottom: 12px;
  right: 12px;
  z-index: 100;
  background: rgba(0, 0, 0, 0.85);
  color: #fff;
  padding: 16px;
  border-radius: 8px;
  font-family: monospace;
  font-size: 13px;
  max-width: 400px;
}

.debug-panel button {
  padding: 8px 16px;
  font-size: 14px;
  cursor: pointer;
  font-family: monospace;
  border: 1px solid #555;
  background: #222;
  color: #fff;
  border-radius: 4px;
}

.debug-panel button:hover {
  background: #444;
}

.debug-panel code {
  display: block;
  padding: 6px 8px;
  background: #111;
  border-radius: 4px;
  word-break: break-all;
  color: #4fc3f7;
}

.debug-panel p {
  margin: 8px 0 4px;
}

.debug-panel .hint {
  color: #999;
  font-size: 11px;
  margin-top: 10px;
}
```

## File: `playground/snap/style.css`
```css
/* html {
  scroll-snap-type: y mandatory;
  scroll-behavior: smooth;
}

.section {
  scroll-snap-align: start;
} */

/* palette from https://twitter.com/tranmautritam/status/1783420779709026785 */

.section {
  padding: 24px;

  .inner {
    height: 100%;
    width: 100%;
    border-radius: 16px;
  }
}

.section:not(:last-child) {
  margin-bottom: -24px;
}

.section-1 {
  height: 150vh;

  .inner {
    background-color: #255bec;
  }
}

.section-2 {
  height: 50vh;

  .inner {
    background-color: #f6c74d;
  }
}

.section-3 {
  height: 250vh;

  .inner {
    background-color: #b49df8;
  }
}

.section-4 {
  height: 80vh;

  .inner {
    background-color: #ea6e38;
  }
}

.section-5 {
  height: 50vh;

  .inner {
    background-color: #255bec;
  }
}

.section-6 {
  height: 100vh;

  .inner {
    background-color: #f6c74d;
  }
}

.inner {
  display: flex;
  justify-content: center;
  align-items: center;
}

/* #wrapper {
  height: 80vh;
  overflow-y: auto;
  position: relative;
  top: 10vh;
} */
```

## File: `playground/snap/test.ts`
```typescript
// import { LoremIpsum } from 'lorem-ipsum'
import Lenis from 'lenis'
import Snap from 'lenis/snap'

// import Snap from '../src/index.ts'

// document.querySelector('#app').innerHTML = new LoremIpsum().generateParagraphs(
//   200
// )

const lenis = new Lenis({
  // wrapper: document.querySelector('#wrapper'),
  // content: document.querySelector('#content'),
  lerp: 0.1,
  syncTouch: true,
})

const _i = 0

const snap = new Snap(lenis, {
  type: 'lock', // 'mandatory', 'proximity', 'lock'
  // velocityThreshold: 1.2,
  duration: 1,
  distanceThreshold: '50%',
  debounce: 500,
  // duration: 2,
  // easing: (t) => t,
  // onSnapStart: (snap) => {
  //   console.log('onSnapStart', snap)
  // },
  // onSnapComplete: (snap) => {
  //   console.log('onSnapComplete', snap)
  // },
})
declare global {
  interface Window {
    snap: Snap
  }
}

window.snap = snap

const _section1 = document.querySelector<HTMLDivElement>('.section-1')!
const section2 = document.querySelector<HTMLDivElement>('.section-2')!
const section3 = document.querySelector<HTMLDivElement>('.section-3')!
const section4 = document.querySelector<HTMLDivElement>('.section-4')!
const section5 = document.querySelector<HTMLDivElement>('.section-5')!
const _section6 = document.querySelector<HTMLDivElement>('.section-6')!

// snap.add(0, {
//   index: 0,
// })

// snap.add(643, {
//   index: 1,
// })

// snap.addElement(section1, {
//   align: ['start', 'end'],
// })

const _unsub1 = snap.addElement(section2, {
  align: 'center',
})

// console.log('unsub1', unsub1)
// unsub1()

snap.addElement(section3, {
  align: ['start', 'end'],
})

// snap.addElement(section4, {
//   align: ['center'],
// })

// snap.addElement(section5, {
//   align: ['center'],
// })

const _unsubs = snap.addElements([section4, section5], {
  align: ['center'],
})

// console.log('unsubs', unsubs)
// unsubs()

// snap.addElement(section6, {
//   align: ['end'],
// })

// snap.addElement(section4, {
//   align: ['start', 'end'], // 'start', 'center', 'end'
// })

function raf(time: number) {
  lenis.raf(time)
  requestAnimationFrame(raf)
}

requestAnimationFrame(raf)
```

## File: `playground/vue/App.vue`
```
<script setup>
import { useLenis } from 'lenis/vue'
import { LoremIpsum } from 'lorem-ipsum'
import { ref, watch } from 'vue'

const _lorem = new LoremIpsum().generateParagraphs(200)

const _lerp = ref(0.1)
const _autoRaf = ref(true)

const lenis = useLenis(
  (lenis) => {
    console.log('root scroll', lenis.options.lerp, lenis.scroll)
  },
  0,
  'root'
)

const lenisRef = ref()

watch(lenis, (lenis) => {
  console.log('lenis in callback', lenis)
})

watch(lenisRef, (lenisRef) => {
  console.log('lenis in ref', lenisRef.lenis)
})
</script>

<template>
  <vue-lenis ref="lenisRef" root :options="{ lerp, autoRaf }">
    <Child />
    <button @click="lerp += 0.1">more lerp</button>
    <button @click="lerp -= 0.1">less lerp</button>
    <button @click="lenis.scrollTo(200)">scroll to 200</button>
    <button @click="lenisRef.lenis.scrollTo(200)">ref scroll to 200</button>
    <vue-lenis
      :options="{ lerp: 0.2, autoRaf }"
      style="height: 50svh; overflow: scroll"
      class="inner"
    >
      <InnerChild />
    </vue-lenis>
    <p>
      {{ lorem }}
    </p>
  </vue-lenis>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
```

## File: `playground/vue/Child.vue`
```
<script setup>
import { useLenis } from 'lenis/vue'
import { watch } from 'vue'

const lenis = useLenis(
  (lenis) => {
    // TODO: This only works after hot reloading so lenis is not defined on mount here
    console.log('child scroll', lenis.options.lerp, lenis.scroll)
  },
  0,
  'child'
)

watch(lenis, (lenis) => {
  console.log('Child Lenis lerp:', lenis.options.lerp)
})
</script>

<template>
  <button type="button" @click="lenis?.scrollTo(100)">scroll</button>
</template>
```

## File: `playground/vue/InnerChild.vue`
```
<script setup>
import { useLenis } from 'lenis/vue'
import { LoremIpsum } from 'lorem-ipsum'

useLenis((lenis) => {
  console.log('innerchild scroll', lenis.options.lerp, lenis.scroll)
})

const _lorem = new LoremIpsum().generateParagraphs(100)
</script>

<template>
  <p>
    {{ lorem }}
  </p>
</template>
```

## File: `playground/vue/setup.ts`
```typescript
import LenisVue from 'lenis/vue'
import type { App } from 'vue'

export default (app: App) => {
  app.use(LenisVue)
}
```

## File: `playground/www/layouts/Layout.astro`
```
---
import 'lenis/dist/lenis.css'
interface Props {
  title: string
}

const { title } = Astro.props
---

<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width" />
    <meta name="generator" content={Astro.generator} />
    <title>{title}</title>
  </head>
  <body>
    <nav>
      <a href="/">
        <svg
          width="15"
          height="16"
          viewBox="0 0 15 16"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M8.6273 0C13.4362 0 15 2.35534 15 6.37565C15 11.4112 12.2502 16 6.58123 16L0.221572 16L0 15.7699L2.64556 0.216595L2.86707 0L8.6273 0Z"
            fill="#E30613"></path>
        </svg>
      </a>
      <a href="/core">Core</a>
      <a href="/snap">Snap</a>
      <a href="/react">React</a>
      <a href="/vue">Vue</a>
      <a href="/horizontal">Horizontal</a>
      <a href="/infinite">Infinite</a>
    </nav>
    <slot />
  </body>
</html>

<style is:global>
  :root {
    font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
    line-height: 1.5;
    font-weight: 400;

    font-synthesis: none;
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  * {
    box-sizing: border-box;
  }

  /* html {
	overflow-y: scroll;
} */

  body {
    margin: 0;
    /* min-width: 320px; */
    /* min-height: 100vh; */
  }
</style>

<style>
  nav {
    position: fixed;
    top: 2px;
    left: 2px;
    align-items: center;
    border-radius: 0.5rem;
    height: 3rem;
    display: flex;
    gap: 2px;
    z-index: 1;
  }

  a {
    min-width: 60px;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    font-family: monospace;
    text-transform: uppercase;
    color: white;
    background-color: #0e0e0e;
    text-decoration: none;
    border-radius: 4px;
    transition: all 0.2s ease-in-out;
    padding: 0 1rem;
  }

  a:hover {
    color: #e30613;
    border-radius: 12px;
  }

  body {
    /* padding-top: 4rem; */
  }
</style>
```

## File: `playground/www/pages/core.astro`
```
---
import '~/core/style.css'
import Layout from '../layouts/Layout.astro'
---

<Layout title="Lenis">
  <div id="debug">
    <button id="scroll-start">Scroll start</button>
    <button id="scroll-center">Scroll center</button>
    <button id="scroll-end">Scroll end</button>
    <button id="stop">Stop</button>
    <button id="start">Start</button>
  </div>
  <div id="app">
    <div id="about">
      <h2>about</h2>
      <p>
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolorum, amet
        illum repellendus vitae nulla provident eveniet totam laborum neque odio
        veritatis accusantium, hic quam et qui ipsum eos excepturi molestiae?
      </p>
    </div>
    <div id="work">
      <h2>work</h2>
      <p>
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolorum, amet
        illum repellendus vitae nulla provident eveniet totam laborum neque odio
        veritatis accusantium, hic quam et qui ipsum eos excepturi molestiae?
      </p>
    </div>

    <div id="contact">
      <h2>contact</h2>
      <p>
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolorum, amet
        illum repellendus vitae nulla provident eveniet totam laborum neque odio
        veritatis accusantium, hic quam et qui ipsum eos excepturi molestiae?
      </p>
    </div>
    <div>
      <a href="#"> <span>#</span></a>
      <a href="#top"> <span>top</span></a>
      <a href="#about"> <span>about</span></a>
      <a href="#work"> <span>work</span></a>
      <a href="#contact"> <span>contact</span></a>
      <a href="/react#a"> <span>void</span></a>
      <a
        href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/API/HTMLAnchorElement"
        target="_blank"
      >
        <span>mdn</span></a
      >
    </div>
    <div id="nested-horizontal">
      <div id="nested-horizontal-content"></div>
    </div>
    <div id="nested">
      <div id="nested-content"></div>
    </div>
  </div>
  <script src="../../core/test.ts"></script>
  <!-- THESE ARE HERE TO TEST THE BROWSER VERSION BUNDLE -->
  <!-- <script is:raw src="../../node_modules/lenis/dist/lenis.min.js"></script> -->
  <!-- <script is:raw src="../../core/browser.js"></script> -->
  <!-- <script>
		import { LoremIpsum } from 'lorem-ipsum'
		document.querySelector('#app').innerHTML = new LoremIpsum().generateParagraphs(30)
	</script> -->
</Layout>
```

## File: `playground/www/pages/horizontal.astro`
```
---
import '~/horizontal/style.css'
import Layout from '../layouts/Layout.astro'
---

<Layout title="Lenis">
  <div id="wrapper">
    <a href="twitter.com" id="about">
      <h2>about</h2>
    </a>
    <div id="work">
      <div id="work-content">
        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolore unde
        hic atque qui nobis tempore quaerat illum laborum, reiciendis maxime
        natus vero dignissimos. Magnam accusantium sint nulla velit neque magni?
        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolore unde
        hic atque qui nobis tempore quaerat illum laborum, reiciendis maxime
        natus vero dignissimos. Magnam accusantium sint nulla velit neque magni?
      </div>
    </div>

    <div id="work2">
      <div id="work2-content">
        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolore unde
        hic atque qui nobis tempore quaerat illum laborum, reiciendis maxime
        natus vero dignissimos. Magnam accusantium sint nulla velit neque magni?
        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolore unde
        hic atque qui nobis tempore quaerat illum laborum, reiciendis maxime
        natus vero dignissimos. Magnam accusantium sint nulla velit neque magni?
      </div>
    </div>

    <div id="contact">
      <h2>contact</h2>
    </div>
  </div>
  <script src="../../horizontal/test.ts"></script>
  <!-- THESE ARE HERE TO TEST THE BROWSER VERSION BUNDLE -->
  <!-- <script is:raw src="../../node_modules/lenis/dist/lenis.min.js"></script> -->
  <!-- <script is:raw src="../../core/browser.js"></script> -->
  <!-- <script>
		import { LoremIpsum } from 'lorem-ipsum'
		document.querySelector('#app').innerHTML = new LoremIpsum().generateParagraphs(30)
	</script> -->
</Layout>
```

## File: `playground/www/pages/index.astro`
```
---
import Layout from '../layouts/Layout.astro'
---

<Layout title="Lenis Playground">
  <main>
    <h1>Welcome to the Lenis Playground!</h1>
    <p>
      <br />
      This is a playground for the Lenis library. It's a great way to test and experiment
      with the library without having to set up a project.
      <br />
      <br />
      If you see this, it means you are trying to contribute to the project and we
      appreciate that!
      <br />
      Playground and build pipeline for all packages run at the same time, so you
      can change the code and see the changes in real-time in the playground.
    </p>
  </main>
</Layout>

<style>
  main {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100svh;
    width: 50vw;
    margin: 0 auto;
  }

  h1,
  p {
    margin: 0;
    font-family: monospace;
    text-align: center;
  }

  h1 {
    text-transform: uppercase;
  }
</style>
```

## File: `playground/www/pages/infinite.astro`
```
---
import '~/infinite/style.css'
import Layout from '../layouts/Layout.astro'
---

<Layout title="Lenis">
  <div id="wrapper">
    <img
      src="https://plus.unsplash.com/premium_photo-1746637010097-5e79e6283d99?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    />
    <img
      src="https://images.unsplash.com/photo-1747901718105-bf9beb57ba3a?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    />
    <img
      src="https://images.unsplash.com/photo-1747901718070-df9e38a96a53?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    />
    <img
      src="https://plus.unsplash.com/premium_photo-1747851402163-9183f38a658c?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    />
    <img
      src="https://plus.unsplash.com/premium_photo-1747751013539-b1d2a2fdeb7a?q=80&w=2016&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    />
    <img
      src="https://images.unsplash.com/photo-1747862240252-50191a60c21d?q=80&w=1965&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    />
    <img
      src="https://plus.unsplash.com/premium_photo-1746637010097-5e79e6283d99?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    />
    <img
      src="https://images.unsplash.com/photo-1747901718105-bf9beb57ba3a?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    />
    <img
      src="https://images.unsplash.com/photo-1747901718070-df9e38a96a53?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    />
    <img
      src="https://plus.unsplash.com/premium_photo-1747851402163-9183f38a658c?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    />
    <img
      src="https://plus.unsplash.com/premium_photo-1747751013539-b1d2a2fdeb7a?q=80&w=2016&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    />
    <img
      src="https://images.unsplash.com/photo-1747862240252-50191a60c21d?q=80&w=1965&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    />
    <img
      src="https://plus.unsplash.com/premium_photo-1746637010097-5e79e6283d99?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    />
    <img
      src="https://images.unsplash.com/photo-1747901718105-bf9beb57ba3a?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    />
    <img
      src="https://images.unsplash.com/photo-1747901718070-df9e38a96a53?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    />
    <img
      src="https://plus.unsplash.com/premium_photo-1747851402163-9183f38a658c?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    />
    <img
      src="https://plus.unsplash.com/premium_photo-1747751013539-b1d2a2fdeb7a?q=80&w=2016&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    />
    <img
      src="https://images.unsplash.com/photo-1747862240252-50191a60c21d?q=80&w=1965&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    />
  </div>
  <script src="../../infinite/test.ts"></script>
  <!-- THESE ARE HERE TO TEST THE BROWSER VERSION BUNDLE -->
  <!-- <script is:raw src="../../node_modules/lenis/dist/lenis.min.js"></script> -->
  <!-- <script is:raw src="../../core/browser.js"></script> -->
  <!-- <script>
		import { LoremIpsum } from 'lorem-ipsum'
		document.querySelector('#app').innerHTML = new LoremIpsum().generateParagraphs(30)
	</script> -->
</Layout>
```

## File: `playground/www/pages/react.astro`
```
---
import App from '~/react/app'
import '~/react/style.css'
import Layout from '../layouts/Layout.astro'
---
<Layout title="Lenis + React">
	<App client:only="react" />
</Layout>
```

## File: `playground/www/pages/scroll-margin.astro`
```
---
import Layout from '../layouts/Layout.astro'
---

<Layout title="Lenis - scroll-margin / scroll-padding test">
  <style>
    html {
      scroll-padding-top: 10vh;
    }

    header {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      height: 10vh;
      background: rgba(0, 0, 0, 0.9);
      color: white;
      display: flex;
      align-items: center;
      padding: 0 20px;
      gap: 16px;
      z-index: 10;
    }

    header a {
      color: white;
    }

    .spacer {
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 2rem;
      color: #999;
    }

    section {
      min-height: 100vh;
      padding: 40px 20px;
      border-top: 2px solid #333;
    }

    section h2 {
      font-size: 2rem;
      margin-bottom: 1rem;
    }

    #with-margin {
      scroll-margin-top: 5vw;
    }

    #info {
      position: fixed;
      bottom: 20px;
      right: 20px;
      background: rgba(0, 0, 0, 0.8);
      color: white;
      padding: 16px;
      border-radius: 8px;
      font-size: 14px;
      max-width: 300px;
      line-height: 1.5;
    }
  </style>

  <header>
    <strong>Fixed Header (80px)</strong>
    <a href="#default">Default</a>
    <a href="#with-margin">With scroll-margin</a>
    <a href="#with-offset">With offset</a>
  </header>

  <div class="spacer">Scroll down or click nav links</div>

  <section id="default">
    <h2>#default</h2>
    <p>This section has no scroll-margin. It relies on <code>scroll-padding-top: 10vh</code> on the html element to clear the fixed header.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolorum, amet illum repellendus vitae nulla provident eveniet totam laborum neque odio veritatis accusantium, hic quam et qui ipsum eos excepturi molestiae?</p>
  </section>

  <div class="spacer">...</div>

  <section id="with-margin">
    <h2>#with-margin</h2>
    <p>This section has <code>scroll-margin-top: 5vw</code> in addition to the container's <code>scroll-padding-top: 10vh</code>.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolorum, amet illum repellendus vitae nulla provident eveniet totam laborum neque odio veritatis accusantium, hic quam et qui ipsum eos excepturi molestiae?</p>
  </section>

  <div class="spacer">...</div>

  <section id="with-offset">
    <h2>#with-offset</h2>
    <p>This section has no scroll-margin. It tests that the Lenis <code>anchors.offset</code> option stacks with scroll-padding.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolorum, amet illum repellendus vitae nulla provident eveniet totam laborum neque odio veritatis accusantium, hic quam et qui ipsum eos excepturi molestiae?</p>
  </section>

  <div class="spacer">...</div>

  <div id="info">
    <strong>Test cases:</strong><br>
    <b>#default</b> — should clear the header (10vh scroll-padding)<br>
    <b>#with-margin</b> — should clear header + extra gap (10vh padding + 5vw margin)<br>
    <b>#with-offset</b> — should clear header + Lenis offset (10vh padding + 20px offset)
  </div>

  <script>
    import Lenis from 'lenis'

    const lenis = new Lenis({
      autoRaf: true,
      anchors: {
        offset: -20,
        onStart: () => {
          console.log('onStart')
        },
        onComplete: () => {
          console.log('onComplete')
        },
      },
    })

    lenis.on('scroll', () => {})
  </script>
</Layout>
```

## File: `playground/www/pages/snap.astro`
```
---
import '~/snap/style.css'
import Layout from '../layouts/Layout.astro'
---

<Layout title="Lenis Snap">
  <div id="wrapper">
    <div id="content">
      <section class="section section-1">
        <div class="inner">0</div>
      </section>
      <section class="section section-2">
        <div class="inner">1</div>
      </section>
      <section class="section section-3">
        <div class="inner">2</div>
      </section>
      <section class="section section-4">
        <div class="inner">3</div>
      </section>
      <section class="section section-5">
        <div class="inner">4</div>
      </section>
      <section class="section section-6">
        <div class="inner">5</div>
      </section>
    </div>
  </div>
  <script src="../../snap/test.ts"></script>
</Layout>
```

## File: `playground/www/pages/vue.astro`
```
---
import App from '~/vue/App.vue'
import '~/vue/style.css'
import Layout from '../layouts/Layout.astro'
---
<Layout title="Lenis + Vue">
	<App client:only="vue" />
</Layout>
```

## File: `scripts/update-readme.js`
```javascript
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


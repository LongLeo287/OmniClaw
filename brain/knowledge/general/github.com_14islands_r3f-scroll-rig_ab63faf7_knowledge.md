---
id: github.com-14islands-r3f-scroll-rig-ab63faf7-knowl
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:27.286842
---

# KNOWLEDGE EXTRACT: github.com_14islands_r3f-scroll-rig_ab63faf7
> **Extracted on:** 2026-04-01 15:44:44
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007524732/github.com_14islands_r3f-scroll-rig_ab63faf7

---

## File: `.editorconfig`
```
# EditorConfig is awesome: https://EditorConfig.org

# top-most EditorConfig file
root = true

# Unix-style newlines with a newline ending every file
[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
indent_style = space
indent_size = 2
trim_trailing_whitespace = true

[*.md]
trim_trailing_whitespace = false
```

## File: `.gitignore`
```
node_modules
link*
.DS_Store
yarn-error.log
```

## File: `.nvmrc`
```
v16.17.0
```

## File: `.prettierrc`
```
{
  "semi": false,
  "trailingComma": "es5",
  "singleQuote": true,
  "tabWidth": 2,
  "printWidth": 120,
  "useTabs": false
}
```

## File: `.size-snapshot.json`
```json
{
  "web.js": {
    "bundled": 48006,
    "minified": 21335,
    "gzipped": 6733,
    "treeshaked": {
      "rollup": {
        "code": 3379,
        "import_statements": 514
      },
      "webpack": {
        "code": 12370
      }
    }
  },
  "web.cjs.js": {
    "bundled": 73487,
    "minified": 36727,
    "gzipped": 8653
  },
  "vscroll.js": {
    "bundled": 12612,
    "minified": 5447,
    "gzipped": 2205,
    "treeshaked": {
      "rollup": {
        "code": 1496,
        "import_statements": 158
      },
      "webpack": {
        "code": 3013
      }
    }
  },
  "vscroll.cjs.js": {
    "bundled": 15673,
    "minified": 6575,
    "gzipped": 2419
  },
  "scrollbar.js": {
    "bundled": 17599,
    "minified": 7326,
    "gzipped": 2609,
    "treeshaked": {
      "rollup": {
        "code": 1654,
        "import_statements": 204
      },
      "webpack": {
        "code": 2971
      }
    }
  },
  "scrollbar.cjs.js": {
    "bundled": 26250,
    "minified": 12495,
    "gzipped": 3474
  },
  "examples.js": {
    "bundled": 2866,
    "minified": 1792,
    "gzipped": 822,
    "treeshaked": {
      "rollup": {
        "code": 221,
        "import_statements": 221
      },
      "webpack": {
        "code": 1403
      }
    }
  },
  "examples.cjs.js": {
    "bundled": 3788,
    "minified": 2231,
    "gzipped": 973
  },
  "stdlib.js": {
    "bundled": 9462,
    "minified": 4571,
    "gzipped": 1790,
    "treeshaked": {
      "rollup": {
        "code": 175,
        "import_statements": 175
      },
      "webpack": {
        "code": 1357
      }
    }
  },
  "stdlib.cjs.js": {
    "bundled": 17078,
    "minified": 9402,
    "gzipped": 2603
  },
  "powerups.js": {
    "bundled": 10268,
    "minified": 5103,
    "gzipped": 1946,
    "treeshaked": {
      "rollup": {
        "code": 203,
        "import_statements": 203
      },
      "webpack": {
        "code": 1418
      }
    }
  },
  "powerups.cjs.js": {
    "bundled": 17718,
    "minified": 9735,
    "gzipped": 2710
  },
  "web.cjs": {
    "bundled": 73494,
    "minified": 36736,
    "gzipped": 8651
  },
  "scrollbar.cjs": {
    "bundled": 26257,
    "minified": 12504,
    "gzipped": 3476
  },
  "powerups.cjs": {
    "bundled": 17718,
    "minified": 9735,
    "gzipped": 2710
  }
}
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2023 14 Islands AB

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
# @14islands/r3f-scroll-rig

![npm](https://img.shields.io/npm/v/@14islands/r3f-scroll-rig?color=magenta&style=flat-square)

Progressively enhance a React website with WebGL using `@react-three/fiber` and smooth scrolling.

<p align="center">
  <img width="49.5%" src="https://www.dropbox.com/s/kqaweg996jtb2ho/14islands600_10fps_2.gif?dl=0&raw=1" style="float:left" />
  <img width="49.5%" src="https://www.dropbox.com/s/vmpqf17oy0otkkl/pluto600_10fps.gif?dl=0&raw=1" style="float:right" />
</p>

[ <a href="#features-">Features</a> |
<a href="#introduction-">Introduction</a> |
<a href="#installing-">Installing</a> |
<a href="#getting-started-">Getting Started</a> |
<a href="#examples-">Examples</a> |
<a href="#api-%EF%B8%8F">API</a> |
<a href="#gotchas-">Gotchas</a> ]

# Features 🌈

- 🔍 Tracks DOM elements and draws Three.js objects in their place using correct scale and position.
- 🤷 Framework agnostic - works with `next.js`, `gatsby.js`, `create-react-app` etc.
- 📐 Can render objects in viewports. Makes it possible for each object to have a unique camera, lights, environment map, etc.
- 🌠 Helps load responsive images from the DOM. Supports `<picture>`, `srset` and `loading="lazy"`
- 🚀 Optimized for performance. Calls `getBoundingClientRect()` once on mount, and uses IntersectionObserver/ResizeObserver to keep track of elements.
- 🧈 Uses [Lenis](https://github.com/darkroomengineering/lenis) for accessible smooth scrolling
- ♻️ 100% compatible with the @react-three ecosystem, like [Drei](https://github.com/pmndrs/drei), [react-spring](https://www.react-spring.dev/) and [react-xr](https://github.com/pmndrs/react-xr)

# Introduction 📚

Mixing WebGL with scrolling HTML is hard. One way is to have multiple canvases, but there is a browser-specific limit to how many WebGL contexts can be active at any one time, and resources can't be shared between contexts.

<img align="right" width="40%" src="https://user-images.githubusercontent.com/420472/191715313-cc813f47-4e4a-454f-a2f5-d8e2ec998c95.jpeg" />

The scroll-rig has only one shared `<GlobalCanvas/>` that stays in between page loads.

React DOM components can choose to draw things on this canvas while they are mounted using a custom hook called `useCanvas()` or the `<UseCanvas/>` tunnel component.

The library also provides means to sync WebGL objects with the DOM while scrolling. We use a technique that tracks “proxy” elements in the normal page flow and updates the WebGL scene positions to match them.

The `<ScrollScene/>`, `<ViewportScrollScene/>` or the underlying `useTracker()` hook will detect initial location and dimensions of the proxy elements, and update positions while scrolling.

Everything is synchronized in lockstep with the scrollbar position on the main thread.

Further reading: [Progressive Enhancement with WebGL and React](https://medium.com/14islands/progressive-enhancement-with-webgl-and-react-71cd19e66d4)

# Installing 💾

`yarn add @14islands/r3f-scroll-rig @react-three/fiber three`

# Getting Started 🛫

1. Add `<GlobalCanvas>` to your layout. Keep it outside of your router to keep it from unmounting when navigating between pages.

2. Add `<SmoothScrollbar/>` to your layout. In order to perfectly match WebGL objects and DOM content, the browser scroll position needs to be animated on the main thread.

<details open>
<summary>Next.js</summary>

```jsx
import { GlobalCanvas, SmoothScrollbar } from '@14islands/r3f-scroll-rig'

// _app.jsx
function App({ Component, pageProps }: AppProps) {
  return (
    <>
      <GlobalCanvas />
      <SmoothScrollbar />
      <Component {...pageProps} />
    </>
  )
}
```

</details>

<details>
<summary>Gatsby.js</summary>

```jsx
// gatsby-browser.js
import { GlobalCanvas, SmoothScrollbar } from '@14islands/r3f-scroll-rig'

export const wrapRootElement = ({ element }) => (
  <>
    <GlobalCanvas />
    <SmoothScrollbar />
    {element}
  </>
)
```

</details>

2. Track a DOM element and render a Three.js object in its place

This is a basic example of a component that tracks the DOM and use the canvas to render a Mesh in its place:

```jsx
import { UseCanvas, ScrollScene } from '@14islands/r3f-scroll-rig'

export const HtmlComponent = () => (
  const el = useRef()
  return (
    <>
      <div ref={el}>Track me!</div>
      <UseCanvas>
        <ScrollScene track={el}>
          {(props) => (
            <mesh {...props}>
              <planeGeometry />
              <meshBasicMaterial color="turquoise" />
            </mesh>
          )}
        </ScrollScene>
      </UseCanvas>
    </>
  )
)
```

## How it works:

- The page layout is styled using normal HTML & CSS
- The `UseCanvas` component is used to send its children to the `GlobalCanvas` while the component is mounted
- A `<Scrollscene>` is used to track the DOM element
- Inside the `<ScrollScene>` we place a mesh which will receive the correct scale as part of the passed down `props`

**⚠️ Note:** HMR might not work for the children of `<UseCanvas>` unless you defined them outside. Also, the props on the children are not reactive by default since the component is tunneled to the global canvas. <a href="/brain/knowledge/docs_legacy/api.md#usecanvas">Updated props need to be tunneled like this.</a>

Learn more about edge cases and solutions in the <a href="#gotchas-">gotchas section</a>.

# Examples & Tutorials 🎪

Tutorials:
- [Codrops Tutorial](https://tympanus.net/codrops/2023/10/10/progressively-enhanced-webgl-lens-refraction/)

Examples:
- [ScrollScene basic example](https://codesandbox.io/s/hello-world-ibc8y7?file=/src/App.jsx)
- [ScrollScene with GLB model & events from both DOM & Canvas](https://codesandbox.io/s/scrollscene-with-glb-6l2fc3?file=/src/App.js)
- [ViewportScrollScene with custom camera and controls](https://codesandbox.io/s/hello-viewportscrollscene-fu0ky6?file=/src/App.jsx)
- [Loading textures from &lt;img&gt; tags](https://codesandbox.io/s/load-image-from-dom-n120ll?file=/src/App.jsx)
- [Load responsive texture from the DOM](https://codesandbox.io/s/load-responsive-picture-from-dom-rgcx4b?file=/src/App.jsx)
- [HTML parallax with useTracker() and Framer Motion](https://codesandbox.io/s/parallax-with-framer-motion-dx2v1p?file=/src/App.jsx)
- [A sticky ScrollScene from the powerups samples](https://codesandbox.io/s/r3f-scroll-rig-sticky-box-w5v4u7?file=/src/App.jsx)
- [A basic Post Processing example](https://codesandbox.io/p/sandbox/hello-scrollscene-forked-cp3n93?file=/src/App.jsx)

# API ⚙️

All components & hooks are described in the [API docs](api.md)

<table>
  <tr>
    <td valign="top">
      <h2><a href="/brain/knowledge/docs_legacy/api.md#components">Components</a></h2>
        <ul>
          <li><a href="/brain/knowledge/docs_legacy/api.md#globalcanvas">GlobalCanvas</a></li>
          <li><a href="/brain/knowledge/docs_legacy/api.md#smoothscrollbar">SmoothScrollbar</a></li>
          <li><a href="/brain/knowledge/docs_legacy/api.md#usecanvas">UseCanvas</a></li>
          <li><a href="/brain/knowledge/docs_legacy/api.md#scrollscene">ScrollScene</a></li>
          <li><a href="/brain/knowledge/docs_legacy/api.md#viewportscrollscene">ViewportScrollScene</a></li>
        </ul>
       <td valign="top">
       <h2> <a href="/brain/knowledge/docs_legacy/api.md#hooks">Hooks</a></h2>
        <ul>
          <li><a href="/brain/knowledge/docs_legacy/api.md#usescrollrig">useScrollRig</a></li>
          <li><a href="/brain/knowledge/docs_legacy/api.md#usescrollbar">useScrollbar</a></li>
          <li><a href="/brain/knowledge/docs_legacy/api.md#usetracker">useTracker</a></li>
          <li><a href="/brain/knowledge/docs_legacy/api.md#usecanvas-1">useCanvas</a></li>
          <li><a href="/brain/knowledge/docs_legacy/api.md#useimageastexture">useImageAsTexture</a></li>
        </ul>
    </td>

  </tr>
</table>

# Gotchas 🧐

<details>
  <summary>The default camera</summary>

The default scroll-rig camera is locked to a 50 degree Field-of-View.

In order to perfectly match DOM dimensions, the camera distance will be calculated. This calculation is based on screen height since Threejs uses a vertical FoV. This means the camera position-z will change slightly based on your height.

You can override the default camera behaviour, and for instance set the distance and have a variable FoV instead:

```jsx
<GlobalCanvas camera={{ position: [0, 0, 10] }} />
```

Or change the FoV, which would move the camera further away in this case:

```jsx
<GlobalCanvas camera={{ fov: 20 }} />
```

If you need full control of the camera you can pass in a custom camera as a child instead.

</details>

<details>
  <summary>Use relative scaling</summary>
  Always base your sizes on the `scale` passed down from ScrollScene/ViewportScrollScene/useTracker in order to have consistent scaling for all screen sizes.

The `scale` is always matching the tracked DOM element and will update based on media queries etc.

```jsx
<ScrollScene track={el}>
  {{ scale }} => (
  <mesh scale={scale} />
  )}
</ScrollScene>
```

Scale is a 3-dimensional vector type from [vecn](https://www.npmjs.com/package/vecn) that support swizzling and object notation. You can do things like:

```js
position.x === position[0]
position.xy => [x,y]
scale.xy.min() => Math.min(scale.x, scale.y)
```

</details>

<details>
  <summary>Z-Fighting on 3D objects (scaleMultiplier)</summary>

By default the scroll-rig will calculate the camera FoV so that 1 pixel = 1 viewport unit.

In some cases, this can mess up the depth sorting, leading to visual glitches in a 3D model. A 1000 pixel wide screen would make the scene 1000 viewport units wide, and by default the camera will also be positioned ~1000 units away in Z-axis (depending on the FoV and screen hight).

One way to fix this is to enable the [logarithmicDepthBuffer](https://threejs.org/brain/knowledge/docs_legacy/index.html?q=webglre#api/en/renderers/WebGLRenderer) but that can be bad for performance.

A better way to fix the issue is to change the GlobalCanvas `scaleMultiplier` to something like `0.01` which would make 1000px = 10 viewport units.

```jsx
<GlobalCanvas scaleMultiplier={0.01} />
```

The `scaleMultiplier` setting updates all internal camera and scaling logic. Hardcoded scales and positions would need to be updated if you change this setting.

</details>

<details>
  <summary>Matching exact hex colors</summary>

By default R3F uses ACES Filmic tone mapping which makes 3D scenes look great.

However, if you need to match hex colors or show editorial images, you can disable it per material like so:

```jsx
<meshBasicMaterial toneMapping={false} />
```

</details>

<details>
  <summary>Cumulative layout shift (CLS)</summary>

All items on the page should have a predictable height - always define an aspect ratio using CSS for images and other interactive elements that might impact the document height as they load.

The scroll-rig uses `ResizeObserver` to detect changes to the `document.body` height, for instance after webfonts loaded, and will automatically recalculate postions.

If this fails for some reason, you can trigger a manual `reflow()` to recalculate all cached positions.

```jsx
const { reflow } = useScrollRig()

useEffect(() => {
  heightChanged && reflow()
}, [heightChanged])
```

</details>

<details>
  <summary>Performance tips</summary>

- Use CSS animations whenever possible instead of JS for maximum smoothness
- Consider disabling SmoothScrollbar and all scrolling WebGL elements on mobile - it is usually laggy.
- Make sure you [read, understand and follow all performance recomendations](https://docs.pmnd.rs/react-three-fiber/advanced/pitfalls) associated with `React` and `three`:

</details>

<details>
  <summary>How to catch events from both DOM and Canvas</summary>

This is possible in R3F by re-attaching the event system to a parent of the canvas:

```tsx
const ref = useRef()
return (
  <div ref={ref}>
    <GlobalCanvas
      eventSource={ref} // rebind event source to a parent DOM element
      eventPrefix="client" // use clientX/Y for a scrolling page
      style={{
        pointerEvents: 'none', // delegate events to wrapper
      }}
    />
  </div>
)
```

</details>

<details>
  <summary>Can I use R3F events in `ViewportScrollScene`?</summary>

Yes, events will be correctly tunneled into the viewport, if you follow the steps above to re-attach the event system to a parent of the canvas.

</details>

<details>
  <summary>inViewportMargin is not working in CodeSandbox</summary>

The CodeSandbox editor runs in an iframe which breaks the IntersectionObserver's `rootMargin`. If you open the example outside the iframe, you'll see it's working as intended.

This is know [issue](https://github.com/thebuilder/react-intersection-observer/issues/330#issuecomment-612221114).

</details>

<details>
  <summary>HMR is not working with UseCanvas children</summary>

This is a known issue with the `UseCanvas` component.

You can either use the `useCanvas()` hook instead, or make HMR work again by defining your children as top level functions instead of inlining them:

```jsx
// HMR will work on me since I'm defined here!
const MyScrollScene = ({ el }) => <ScrollScene track={el}>/* ... */</ScrollScene>

function MyHtmlComponent() {
  return (
    <UseCanvas>
      <MyScrollScene />
    </UseCanvas>
  )
}
```

A similar [issue](https://github.com/pmndrs/tunnel-rat/issues/4) exist in `tunnel-rat`.

</details>

<details>
  <summary>Global render loop</summary>

The scroll-rig runs a custom render loop of the global scene inside r3f. It runs with priority `1000`.

You can disable the global render loop using `globalRender` or change the priority with the `globalPriority` props on the `<GlobalCanvas>`. You can still schedule your own render passes before or after the global pass using `useFrame` with your custom priority.

The main reason for running our own custom render pass instead of the default R3F render, is to be able to avoid rendering when no meshes are in the viewport. To enable this you need to set `frameloop="demand"` on the GlobalCanvas.

</details>

<details>
  <summary>Advanced - run frameloop on demand</summary>

If the R3F frameloop is set to `demand` - the scroll rig will make sure global renders and viewport renders only happens if it's needed.

To request global render call `requestRender()` from `useScrollRig` on each frame. `ScrollScene` will do this for you when the mesh is in viewport.

This library also supports rendering separate scenes in viewports as a separate render pass by calling `renderViewport()`. This way we can render scenes with separate lights or different camera than the global scene. This is how `ViewportScrollScene` works.

In this scenario you also need to call `invalidate` to trigger a new R3F frame.

</details>

<details>
  <summary>How to use post-processing</summary>

Post processing runs in a separate pass so you need to manually disable the global render loop to avoid double renders.

```jsx
<GlobalCanvas globalRender={false} scaleMultiplier={0.01}>
  <Effects />
</GlobalCanvas>
```

Note: `ViewportScrollScene` will not be affected by global postprocessing effects since it runs in a separate render pass.

</details>

<details>
  <summary>How can I wrap my UseCanvas meshes in a shared Suspense?</summary>

Please read the API docs on using [children as a render function](api.md#children-as-render-function) for an example.

</details>

# In the wild 🐾

- [14islands.com](https://14islands.com) by [14islands](https://14islands.com)
- [v3.14islands.com](https://v3.14islands.com) by [14islands](https://14islands.com)
- [Pluto.app](https://pluto-xr.netlify.app/) by [14islands](https://14islands.com)
- [Myriad.video](https://myriad.video/) by [14islands](https://14islands.com)
- [Neko Health](https://www.nekohealth.com/) by [14islands](https://14islands.com)
- ~~[Playgoals.com](https://playgoals.com/) by [14islands](https://14islands.com)~~
- [Goals studio](https://studio.playgoals.com/) by [14islands](https://14islands.com)
- ~~[Pluto dev portal](https://dev.pluto.app/) by [14islands](https://14islands.com)~~
- [Quantum Wallet](https://quantumwallet.tech/) by [14islands](https://14islands.com)
- [Metamask Learn](https://learn.metamask.io/) by [Antinomy Studio](https://antinomy.studio)
- [Lynxeye](https://lynxeye.com/) by [14islands](https://14islands.com)
- [Astra Nova](https://astranova.world/) by [estudio/nk](https://thefwa.com/profiles/estudionk-r) and [@juliperoncini](https://twitter.com/juliperoncini)
- [Axolot Games](https://www.axolotgames.com/) by [14islands](https://14islands.com)
- [Cartier 365](https://365ayearof.cartier.com/en/) by [14islands](https://14islands.com)
```

## File: `changelog.md`
```markdown
# Changelog

## v8.15.0

- `useWindowSize`
  - Feat: export added
- `StickyScrollScene`
  - Fix: better sticky area calculation when reloading while scrolled down

## v8.14.0

- `SmoothScrollbar`
  - Feat: now using `lenis` import
- `preloadScene`
  - Feat: Switched to object literal for arguments to match other render API functions
  - Fix: `scene` and `camera` props are now optional
- `UseCanvas`
  - Fix: `id` prop is now passed to the child
- `powerups` add type declaration

## v8.13.0

- `ScrollScene` improved portal support
- `StickyScrollScene` improvements

## v8.12.0

- Upgrade `@studio-freight/lenis` to `v1.0.23`
- `SmoothScrollbar`
  Passing in children is now obsolete and not needed. The only reason was to set `pointer-events: none` on the children while scrolling. We now do this directly on `doucment.documentElement`.
  This change makes it easier to dynamically import and conditionally render the scrollbar to split the bundle.

## v8.11.0

- Upgrade `@studio-freight/lenis` to `v1.0.16`

## v8.10.0

- Upgrade `@studio-freight/lenis` to `v1.0.10`

- `GlobalCanvas`
  - Add back: `as` props to allow changing the default R3F Canvas component. Prep work for supporting custom tree shaked canvas or perhaps react-three-offscreen in the future

## v8.9.0

Simplify render logic and improve camera controls.

- `ViewportScrollScene`

  - Feat: now uses portal state enclave for camera so you can use OrbitControls or pass in a custom camera as a child.
  - Feat: No longer clears depth by default
  - Feat: added `hud` prop to clear depth
  - Feat: aadded `camera` prop to allow overriding default camera settings
    - specifying `fov` will calculate distance to match the DOM
  - Removed `renderOrder` - can be set manually on children instead

- `ScrollScene`

  - Removed `renderOrder` - can be set manually on children instead

- `GlobalCanvas`

  - Fix: make sure `viewport` is correct after resize when using default perspective camera
  - Feat: `camera` prop now allows overriding `fov`. If `fov` is specified, the camera distance will be calculated to match DOM size.
  - Feat: Default camera FoV now set to 50
  - Removed: `globalClearAlpha` - can be controlled by other useFrames with higher or lower priority instead
  - Removed: `as` - always renders as a default R3F Canvas. `react-xr` no longer uses VRCanvas and ARCanvas.

- `useImageAsTexture`

  - Fix: better support for next/image loading="lazy"

- `SmoothScrollbar`
  - Fix: make sure binding an onScroll callback fires an initial scroll event

## v8.8.0

Added some properties to help support having multiple SmoothScrollbar on the page at the same time. The usecase is to open a Modal on top of the current page which also needs to be smooth scrolled.

- `useTracker`

  - Added `wrapper` option to get initial scroll offset from DOM element instead of the window object.
  - Added `scroll` prop to `update({ scroll })` to update tracker with custom scroll state. Useful when having a secondary scrollbar mounted.

- `SmoothScrollbar`
  - Added `onScroll` prop to register a scroll event callback.
  - Added `updateGlobalState` prop. True by default. Set it to false to disable updating the global scroll state. Useful when having a secondary scrollbar mounted.

## v8.7.0

- `scrollInContainer`

  - Feat: Added experimental `scrollInContainer` prop which scrolls inside the body element instead of the default window. This can be used to avoid scrolling away the URL bar on mobile. It also enables the `smoothTouch` setting in Lenis which emulates scroll using touch events.

- `useTracker`
  - Fix: Matches height of canvas element instead of window.innerHeight if possible. (Fixes position problems on mobile where canvas is 100vh)

## v8.6.0

- All files converted to TypeScript

## v8.5.0

- Fixed SSR warnings by replacing `uesLayoutEffect` with `useIsomorphicLayoutEffect`

- `GlobalCanvas`

  - removed `loadingFallback`
  - children can now be a render function (optional). It accepts the global canvas children from useCanvas as a single parameter. This can be used to add suspense boundaries.

  ```jsx
  <GlobalCanvas>
    {(globalChildren) => (
      <Suspense fallback={null}>
        {globalChildren}
        <AnotherPersistentComponent />
      </Suspense>
    )}
  </GlobalCanvas>
  ```

- `useImageAsTexture`

  - Added WebP Accept header to fetch request if supported by brower
  - Notifies the DefaultLoadingManager that something is loading while waiting for the DOM image load.

- Added global css with classes that can hide DOM elements when canvas is active
  `import "@14islands/r3f-scroll-rig/css";`

- Global export `styles` added to access CSS class names from Javascript.

```jsx
import { styles } from '@14islands/r3f-scroll-rig'

function Component() {
  return <div className={styles.hidden}>I will be `visibility: hidden` if WebGL is supported</div>
}
```

- Removed `useCanvasRef` - use exported classnames and global CSS to hide elements via SSR instead to avoid FOUC

- `SmoothScrollbar`

  - Replaced global html classname `js-has-smooth-scrollbar` with two classes: `js-smooth-scrollbar-enabled` and `js-smooth-scrollbar-disabled`

- `useCanvas` - improved option `dispose:false` to keep unused meshes mounted. Now passes an `inactive` prop to the component which is true if no hook is using the mesh.

- `useTracker` - new call signature
  - first argument is always the DOM ref
  - second argument is the optional config settings for the IntersectionObserver

## v8.4.0

- `GlobalCanvas`
  - `children` can now be a render function which accepts all global children as a single argument. Can be used if you need to wrap all canvas children with a parent.

## v8.3.0

- `useTracker` hook

  - Added `autoUpdate` configuration which decides if the tracker automatically updates on scroll events. True by default.
  - The `update` callback will now always recalculate positions even if element is outside viewport in case user wants to turn off autUpdate and take control.

- `SmoothScrollbar`
  - Added `horizontal` prop

## v8.1.0

- `useTracker` hook

  - Added `threshold` prop which can used to customize the underlying Intersection Observer of the tracked DOM element

- `ScrollScene` and `ViewportScrollScene`
  - Added `inViewportThreshold` prop which is passed to `useTracker` as `threshold`

## v8.0.0

Complete refactor with focus on reducing complexity.

Now uses mostly R3F defaults and `<GlobalCanvas>` accepts all R3F Canvas props.

Advanced use-cases are enabled only when setting `frameloop="demand"` - so most users won't have to worry about this.

### New peer deps:

- @react-three/fiber `">=8.0.0"`
- Three.js `>=0.139.0` is now required for colorManagement

### New features

- Started adding typescript
- Uses `https://github.com/studio-freight/lenis` scrollbar
- New hook `useTracker` that tracks DOM elements - refactored `ScrollScene` and `ViewportScrollScene` to use this internally.
- New hook `useCanvasRef` which can be used to hide tracked DOM elements when the canvas is active.
- New hook `useImageAsTexture` which loads images from the DOM and suspends via useLoader. Replaces the old `useImgTagAsTexture` which did not suspend properly and was more of a hack.

### Breaking Changes:

- Removed `useImgTagAsTexture`. Use `useImageAsTexture` instead.
- `ScrollScene` and `ViewportScrollScene`

  - Renamed `el` prop to `track`
  - `inViewportMargin` is now a string and maps to IntersectionObserver `rootMargin`
  - Removed `lerp`, `lerpOffset`. Uses the SmoothScrollbar position directly.
  - Removed `setInViewportProp` prop. Instead uses IntersectionObserver to always set `inViewport` prop.
  - Removed `updateLayout` - relac position using the `reflow()` method from `useSrcollRig()` instead.
  - Removed `positionFixed` - suggest implementing manually in some other way using `useTracker`.
  - Removed `autoRender` - suggest implementing manually in a custom component using `useTracker`.
  - Removed `resizeDelay`
  - Removed `hiddenStyle` - use `useCanvasRef` instead to control how tracked DOM elements are hidden.

- `VirtualScrollbar` and `HijackedScrollbar` removed. Use `SmoothScrollbar` instead which is similar to the old hijacked version.
- `GlobalCanvas`

  - Removed `config` prop and added individual props instead:
    - Added `debug` to turn on shader compile errors and show console.logs
    - Added `scaleMultiplier` to control viewport units scaling
    - Added `globalRender` - enable/disable built-in render loop
    - Added `globalPriority` - enable/disable built-in render loop
    - Added `globalAutoClear?: boolean` to control if `gl.clearDepth()` is called before render in global render loop. Default `false` - render as HUD on top of viewports without clearing them.
    - Added `globalClearDepth?: boolean` to control `gl.autoClear` in global render loop. Default `true`.
  - Renamed `fallback` property to `loadingFallback` for global Suspense fallback as R3F Canvas already has a prop with this name

- examples/ folder removed
- added new import target `@14islands/r3f-scroll-rig/powerups` with useful helpers - might become separate repo later

## v7.0.0

- update to R3f v7
- Enables autoRender by default if frameloop="always"

## v6.0.0

- Updated to R3F v6 api.

## v2.1.0

### ViewportScrollScene, ScrollScene, ScrollDomPortal

- `lerpOffset` is now a factor that is multiplied with the lerp instead of added. Default value is now `1` instead of `0`.

## v2.0.0

Breaking upgrade. Simplify and remove as much as possible.

- `requestFrame` is now removed. please use `invalidate` to trigger useFrame
- global render pass now run with priority `1000`
- `renderFullscreen` has been renamed to `requestRender` - use this to trigger a global render pass.
- `renderScissor` and `renderViewport` now renders immediately. use `useFrame() priority` to render before or after global render
- `preloadScene` now runs with priority `0`
- `ScrollScene` and `ViewportScrollScene` runs with priority `1` by default
- `ScrollScene` and `ViewportScrollScene` now accepts a `priority` prop to change the `useFrame` priority.
- all `pause` and `suspend` logic has been removed

## v1.11.0

Added `stdlib` export target with the following reusable components:

- WebGLText
- WebGLImage
- ParallaxScrollScene
- StickyScrollScene

E.g. `import { StickyScrollScene } from '@14islands/r3f-scroll-rig/stdlib`

## v1.10.0

### GlobalCanvas

- Added back Stats component. `fps` config and querystring now works again

### HijackedScrollbar

- New experimental scrollbar with animates `window.scrollTo` instead of translating sections with CSS.

## v1.9.21

### ScrollDom (Experimental)

- Removed. Consider using `ScrollPortal` or use `drei`'s `HTML` component instead.

### ScrollDomPortal

- Removed `framer-motion` dependency.

### ViewportScrollScene

- Removed `framer-motion` dependency.

### VirtualScrollbar

- Removed `framer-motion` dependency.

### ScrollScene

- Removed experimental `softDirection`
- Removed `framer-motion` dependency.

## v1.9.17

### GlobalCanvas

- Added config option `subpixelScrolling` that affects ScrollScene. If false, the scroll poition will be rounded to an integer (browsers usually do this with normal scroll)

## v1.9.13

### ScrollDomPortal

- `portalEl` now needs to be passed as an argument. GlobalCanvas no longer provides a default portal.

## v1.9.12

### GlobalCanvas

- `antialias` and `depth` are now `true` by default.
- `VirtualScrolbar` now uses same lerp & restDelta as Canvas components

## v1.9.0

### GlobalRenderer

- No more automatic switching between global vs scissor renders. To make it more predictable, scissor passes are always rendered if requested.

### ScrollScene

- `scissor` is now false by default

## v1.8.0

### VirtualScrollbar

- New prop `scrollToTop` (false by default) to automatically scroll to top of page when scrollbar mounts. (used to be true by default)

## v1.7.1

### GlobalRenderer

- `gl.autoClear` is now only turned off if we have viewports renderering before main global render call. This fixes background alpha glitch on Oculus browser and WebXR clearing issues.

## v1.7.0

### GlobalCanvas

- New property `as` to support rendering the global canvas as a `VRCanvas` for instance.

## v1.6.0

### ViewportScrollScene

- `PerspectiveCameraScene` renamed to `ViewportScrollScene` with optional property `orthographic` to switch between orthographic and perspective cameras. Both are scaled to fit the viewport exactly.

### GlobalCanvas

- Uses custom cameras for global `scaleMultiplier` to work properly. Bypasses all built-in @react-three/fiber camera logic. Property `orthogonal` is used to select which camera.
- added `fps` setting to the `config` propery which overrides scroll-rig config Querystring value for `fps` and `debug` override this config.
- Default pixelRatio scaling can now be turned off with `config={{autoPixelRatio: false}}`
- turned stencil buffer on by default (not sure disabling did anything good for perf anyway)
- removed gl properties `preserveDrawingBuffer: false` and `premultipliedAlpha: true` that are default in threejs anyway to simplify

## v1.5.0

### ScrollScene

- Deprecated `layoutOffset` and `layoutLerp`. Should be implemented by child component.

## v1.4.0

### ScrollScene

- Deprecated `state` prop passed to child. Replaced by `scrollState`

### PerspectiveCameraScene

- Deprecated `state` prop passed to child. Replaced by `scrollState`
- Accepts `scaleMultiplier` prop which overrides global setting

## v1.3.0

### GlobalCanvas

- `config` propery which overrides scroll-rig config. Props that might be useful to change are `debug`, `scaleMultiplier`, `scrollLerp`.
- `scaleMultiplier` config added which affects PerspectiveCameraScene and ScrollScene scaling. Used to scale pixels vs viewport units (1 by default, i.e. 1px = 1 viewport unit). Suggest using `0.001` for perspective scenes to avoid depth buffer sorting issues etc. (1000px == 1 viewport unit)

### ScrollScene

- Scale scene using global `config.scaleMultiplier`

### PerspectiveCameraScene

- Scale scene using global `config.scaleMultiplier`

### ResizeManager

- Fix broken resize logic under some race conditions

## v1.2.0

### GlobalRenderer

- Viewport scenes can now renderOnTop to render after global queue
- depth is no longer disabled
- config.fbo is removed, implement in your app instead
- `renderScissor`is deprecated

### PerspectiveScrollScene

- Uses `createPortal` instead of nested scene and all of its problems (sweet!)
- New prop `renderOnTop` to render after global render

## v1.0:

### GlobalCanvas

- WebGL 2.0 by default
- `resizeOnHeight` added to GlobalCanvas (default true)

### ScrollScene

- `live` flag is now called `updateLayout`
- `getOffset` -> `layoutOffset`
- `scene` prop passed to children is no longer a ref

### PerspectiveScrollScene

- Uses `createPortal` instead of nested scene and all of its problems (sweet!)

GlobalRenderer

- colorManagement=true + gl.toneMapping = NoToneMapping to match hex with DOM

### ResizeManager

- `resizeOnWebFontLoaded` added to ResizeManager
```

## File: `package.json`
```json
{
  "name": "@14islands/r3f-scroll-rig",
  "version": "8.15.0",
  "description": "Progressively enhance any React website with WebGL using @react-three/fiber",
  "private": false,
  "type": "module",
  "source": "src/index.ts",
  "main": "./dist/scrollrig.cjs",
  "module": "./dist/scrollrig.module.js",
  "unpkg": "./dist/scrollrig.umd.js",
  "types": "./dist/src/index.d.ts",
  "sideEffects": false,
  "exports": {
    "./css": {
      "default": "./dist/scrollrig.css"
    },
    "./scrollbar": {
      "types": "./dist/scrollbar/index.d.ts",
      "require": "./dist/scrollbar.cjs",
      "import": "./dist/scrollbar.modern.js"
    },
    "./powerups": {
      "types": "./dist/powerups/index.d.ts",
      "require": "./dist/powerups.cjs",
      "import": "./dist/powerups.modern.js"
    },
    ".": {
      "types": "./dist/src/index.d.ts",
      "require": "./dist/scrollrig.cjs",
      "import": "./dist/scrollrig.modern.js"
    }
  },
  "files": [
    "dist",
    "scrollbar",
    "powerups"
  ],
  "scripts": {
    "build": "yarn build-default & yarn build-scrollbar & yarn build-powerups",
    "build-default": "microbundle --globals react=React,@react-three/fiber=@react-three/fiber,@juggle/resize-observer=@juggle/resize-observer,lenis=lenis src/index.ts",
    "build-scrollbar": "microbundle --globals react=React,@react-three/fiber=@react-three/fiber,@juggle/resize-observer=@juggle/resize-observer,lenis=lenis src/scrollbar/index.ts -o dist/scrollbar.js",
    "build-powerups": "microbundle --globals react=React,@react-three/fiber=@react-three/fiber,@juggle/resize-observer=@juggle/resize-observer,lenis=lenis,@react-three/drei=@react-three/drei,@14islands/r3f-scroll-rig=@14islands/r3f-scroll-rig --external=@14islands/r3f-scroll-rig powerups/index.ts -o dist/powerups.js",
    "dev": "microbundle watch"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/14islands/r3f-scroll-rig.git"
  },
  "keywords": [
    "@react-three/fiber",
    "webgl",
    "react",
    "three"
  ],
  "author": "@14islands",
  "license": "ISC",
  "bugs": {
    "url": "https://github.com/14islands/r3f-scroll-rig/issues"
  },
  "homepage": "https://github.com/14islands/r3f-scroll-rig#readme",
  "dependencies": {
    "@14islands/lerp": "^1.0.3",
    "@juggle/resize-observer": "^3.4.0",
    "@types/query-string": "^6.3.0",
    "debounce": "^1.2.1",
    "fast-deep-equal": "^3.1.3",
    "lenis": "^1.1.9",
    "query-string": "^6.14.1",
    "react-intersection-observer": "^9.4.0",
    "supports-webp": "^3.0.0",
    "suspend-react": "^0.0.8",
    "vecn": "^1.3.1",
    "zustand": "^3.4.2"
  },
  "devDependencies": {
    "@react-three/drei": "^9.77.0",
    "@react-three/fiber": "^8.13.3",
    "@types/debounce": "^1.2.1",
    "@types/react": "^18.0.25",
    "microbundle": "^0.15.1",
    "react": "^18.1.0",
    "react-dom": "^18.1.0",
    "three": "^0.144.0"
  },
  "peerDependencies": {
    "@react-three/drei": ">=9.0.0",
    "@react-three/fiber": ">=8.0.0",
    "react": ">=18.0",
    "react-dom": ">=18.0",
    "three": ">=0.139.0"
  },
  "peerDependenciesMeta": {
    "@react-three/fiber": {
      "optional": true
    },
    "@react-three/drei": {
      "optional": true
    }
  }
}
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    "declaration": true,
    "declarationDir": "./dist",
    "module": "ESNext",
    "target": "ESNext",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": false,
    "skipLibCheck": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noEmit": true,
    "esModuleInterop": true,
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "downlevelIteration": true,
    "jsx": "react",
    "jsxFactory": "",
    "jsxFragmentFactory": "",
    "incremental": true,
    "noImplicitAny": true,
    "paths": { "@14islands/r3f-scroll-rig": ["./src/index.ts"] }
  },
  "include": ["src/**/*.ts", "src/**/*.tsx"],
  "exclude": ["node_modules", "dist"]
}
```

## File: `brain/knowledge/docs_legacy/api.md`
```markdown
# ⚙️ API

<table>
  <tr>
    <td valign="top">
      <h2><a href="#components">Components</a></h2>
        <ul>
          <li><a href="#globalcanvas">GlobalCanvas</a></li>
          <li><a href="#smoothscrollbar">SmoothScrollbar</a></li>
          <li><a href="#usecanvas">UseCanvas</a></li>
          <li><a href="#scrollscene">ScrollScene</a></li>
          <li><a href="#viewportscrollscene">ViewportScrollScene</a></li>
        </ul>
       <td valign="top">
       <h2> <a href="#hooks">Hooks</a></h2>
        <ul>
          <li><a href="#usescrollrig">useScrollRig</a></li>
          <li><a href="#usescrollbar">useScrollbar</a></li>
          <li><a href="#usetracker">useTracker</a></li>
          <li><a href="#usecanvas-1">useCanvas</a></li>
          <li><a href="#useimageastexture">useImageAsTexture</a></li>
        </ul>
    </td>

  </tr>
</table>

## Components

### `<GlobalCanvas>`

This is the global canvas component that should stay mounted in between page loads.

#### Render Props

`GlobalCanvas` is just a thin wrapper around the default R3F `Canvas` and accepts all the same props.

```tsx
<GlobalCanvas
  children // R3F global child nodes
  debug?: boolean = false
  scaleMultiplier?: number = 1 // 1 pixel = 1 viewport unit
  globalRender?: boolean
  globalPriority?: number
  globalClearDepth?: boolean
  // and all default R3F Canvas props
/>
```

**Note:** _the `GlobalCanvas` has a custom Perspective / Orthographic camera - don't override the camera unless you want full control. For the default `PerspectiveCamera`, you can either specify the `fov` or the `distance` and the other will be calculated to make sure we always match the size of DOM elements._

The following default styles are applied to the canvas:

```css
style={{
  position: 'fixed',
  top: 0,
  left: 0,
  right: 0,
  height: '100vh', // use 100vh to avoid resize on iOS when url bar goes away
  ...style,
}}
```

#### Children as render function

You can pass a render function as the single child to `GlobalCanvas` if you want full control over where the children from `UseCanvas`/`useCanvas` appear in the scene hierarchy.

This is for useful if you want to wrap the global children in a `Suspense` to prevent persistent meshes from being hidden while loading new assets.

```jsx
<GlobalCanvas>
  {(globalChildren) => (
    <>
      <MyPersistentBackground />
      <Suspense fallback={null}>{globalChildren}</Suspense>
    </>
  )}
</GlobalCanvas>
```

### `<SmoothScrollbar>`

The `SmoothScrollbar` component will animate `window.scrollY` smoothly. This allows us to match the speed of objects moving on the fixed GlobalCanvas.

Worth noting:

- it **does not** use JS to move the content using transforms
- we can use `position: sticky` etc 👌
- the component sets `pointer-events: none` on `document.documentElement` to avoid jank caused by hover states (optional, turn of using `disablePointerOnScroll={false}`)
- the R3F event loop is used to animate scroll
- `SmoothScrollbar` uses `lenis` internally. Make sure to read through their section on [considerations](https://github.com/darkroomengineering/lenis#considerations) when adding `SmoothScrollbar` to your project.
- supports horizontal scroll, adding `horizontal: true` will create a horizontal Lenis instance and will scroll the scene along the x axis.

```jsx
import { SmoothScrollbar } from '@14islands/r3f-scroll-rig'

// _app.jsx
function App({ Component, pageProps }: AppProps) {
  return (
    <>
      <SmoothScrollbar />
      <GlobalCanvas />
      <Component {...pageProps} />
    </>
  )
}
```

💡 You can either place the `SmoothScrollbar` in a persistent layout (Lenis will autmatically pick up changes to the document height when navigating). Or, you can place it inside each page in case you want some pages with smooth scrolling and some without.

#### Render Props

```tsx
<SmoothScrollbar
  scrollRestoration?: ScrollRestoration = "auto"
  enabled?: boolean = true // smooth scroll or not
  locked?: boolean = false // lock/disable scroll
  disablePointerOnScroll?: boolean = true
  horizontal?: boolean = false
  config?: object  // lenis config options
/>
```

If you attach a ref to the SmoothScrollbar you will recieve an imperative handle with access to the Lenis instance and its functions.

#### Use without GlobalCanvas

💡**Note:** _You can use `SmoothScrollbar` independently based on the project needs. If the project doesn't need WebGL, you can still use the scrollbar to implement smooth scrolling, and stay flexible to add Canvas later in the project if needed._

```jsx
import { SmoothScrollbar } from '@14islands/r3f-scroll-rig/scrollbar'
```

💡 _A The `scrollbar` import target excludes all `@react-three/fiber`, `three` related imports and allows you to slim down the bundle size._

### `<UseCanvas>`

This component tunnels the children to the GlobalCanvas using the `useCanvas` hook. It's basically just the same, but a bit more user friendly

The children will stay mounted on the canvas until this component unmounts.

#### Render Props

```tsx
<UseCanvas
  children: JSX.Element | (props) => JSX.Element
  id?: string  // persistent layout ID (optional: see below)
  dispose?: boolean // dispose on unmount (optional: true by default)
  [key: string]: any // props to reactively tunnel to the child
>
  <MyMeshComponent />
</UseCanvas>
```

`id` can be used to indicate that the same canvas componets is to be shared between DOM components. For instance it can prevent a mesh from unmounting when navigating to a new page, if that same mesh with the same ID is also present on the new page. This is similar to how Framer Motions layoutId works, but without the automatic layout animation.

The props added to `UseCanvas` will be tunneled and applied to the child component running inside the GlobalCanvas. It automatically updates the canvas component's props when any of the them change.

```jsx
const [isOpen, setIsOpen] = useState(false)

return (
  <div onClick={() => setIsOpen(true)}>
  <UseCanvas isOpen={isOpen}>
    <MyMesh /* I will receieve all props from UseCanvas when they update */ />
  </UseCanvas>
)
```

### `<ScrollScene>`

Tracks a DOM element and renders a Threejs Scene that matches the position in the viewport during scroll.

The child component is passed `scale` which can be used to match the DOM element's size. It's also passed `scrollState` which contains information regarding it's position in the viewport, this is useful for things like parallax or animations. By default it will also hide the children when leaving the viewport.

```tsx
<ScrollScene
  track: RefObject            // DOM element to track (ref)
  children: (props) => JSX.Element  // render function
  as?: string = "scene"       // renders as a Scene by default
  inViewportMargin?: string = "0%"  // IntersectionObserver rootMargin
  inViewportThreshold?: number = 0  // IntersectionObserver threshold
  hideOffscreen?: boolean = true // Hide scene when outside viewport
  visible?: boolean = true    // Scene visibility
  debug?: boolean = false     // Render a debug plane and show 50% opacity of DOM element
  scissor?: boolean = false   // Render as separate pass in a scissor
  margin?: number             // margin added outside scissor
  priority?: number = 1       // useFrame priority for scissor render
  >
  { ({ scale, ...props }) => (
    <mesh scale={scale}>
      <planeGeometry />
      <meshBasicMaterial color="turquoise" />
    </mesh>
  )}
</ScrollScene>
```

The child node will be passed the following `props`:

```ts
track: RefObject // HTML element being tracked
scale: number[]  // HTML element dimensions converted to world scale
scrollState: {
  // transient state - not reactive
  inViewport: boolean // boolean - true if currently in viewport
  progress: number // number - 0 when below viewport. 1 when above viewport
  visibility: number // number - percent of item height in view
  viewport: number // number - percent of window height scrolled since visible
}
inViewport: boolean // boolean set to true while in viewport (+/- inViewportMargin)
priority: number // the parent useFrame priority
props: any[] // tunneled from the parent
```

_Note: this is an abstraction on top of the <a href="#usetracker">useTracker</a> hook._

### `<ViewportScrollScene>`

Tracks a DOM element similar to ScrollScene, but renders a virtual scene in a separate pass.

This makes it possible to use different lights and camera settings compared to the global scene, at the cost of one extra render per instance.

The child receives the same props as the ScrollScene provides.

```tsx
<ViewportScrollScene
  track: RefObject            // DOM element to track (ref)
  children: (props) => JSX.Element  // render function
  orthographic?: boolean = false // uses a perspective camera by default
  inViewportMargin?: string = "0%"  // IntersectionObserver rootMargin
  inViewportThreshold?: number = 0  // IntersectionObserver threshold
  hideOffscreen?: boolean = true // Hide scene when outside viewport
  margin?: number             // margin added outside scissor
  visible?: boolean = true    // Scene visibility
  debug?: boolean = false     // Render a debug plane and show 50% opacity of DOM element
  priority?: number = 1       // useFrame priority
  hud?: boolean               // clear depth
  camera?: any                // camera overrides
  >
  { ({ scale, ...props }) => (
    <mesh scale={scale}>
      <planeGeometry />
      <meshBasicMaterial color="turquoise" />
    </mesh>
  )}
</ViewportScrollScene>
```

The child node will be passed the following `props`:

```ts
track: RefObject // HTML element being tracked
scale: number[]  // HTML element dimensions converted to world scale
scrollState: {
  // transient state - not reactive
  inViewport: boolean // boolean - true if currently in viewport
  progress: number // number - 0 when below viewport. 1 when above viewport
  visibility: number // number - percent of item height in view
  viewport: number // number - percent of window height scrolled since visible
}
inViewport: boolean // boolean set to true while in viewport (+/- inViewportMargin)
priority: number // the parent useFrame priority
props: any[] // tunneled from the parent
```

_Note: this is an abstraction on top of the <a href="#usetracker">useTracker</a> hook._

## Hooks

### `useScrollbar`

Use this to access the scrollbar and current scroll information.

```tsx
import { useScrollbar } from '@14islands/r3f-scroll-rig'

const {
  enabled: boolean, // True if SmoothScrollbar is enabled
  scroll: {
    // transient scroll information
    y: number
    x: number
    limit: number
    velocity: number
    progress: number
    direction: string
  },
  scrollTo: (number | element) => void, // scroll to
  onScroll: (cb) => unbindFunc // subscribe to scroll events
} = useScrollbar
```

#### Use without GlobalCanvas

💡 You can import and use `useScrollbar` in isolation from a separate `scrollbar` target. This excludes all `@react-three/fiber`, `three` related imports and allows you to slim down the bundle size.

```jsx
import { useScrollbar } from '@14islands/r3f-scroll-rig/scrollbar'
```

### `useScrollRig`

Hook to access current scroll rig state and functions related to rendering.

```tsx
import { useScrollRig } from '@14islands/r3f-scroll-rig'

const {
  isCanvasAvailable: boolean, // True if webgl is enabled and GlobalCanvas has been added to the page
  hasSmoothScrollbar: boolean, // True if a smooth scrollbar is currently enabled onm the DOM content
  scaleMultiplier: number, // current viewport unit scaling = 1 by default
  reflow: () => void, // tigger re-calculation of elements position (called automatically on resize), () => void
  debug: boolean, // whether the GloblCanvas is in debug mode or not
  // Advanced render API
  preloadScene: ({ scene?: Scene; camera?: Camera; layer?: number }, callback) => void, // request scene to do a preload render before next frame
  requestRender: (layers?: number[]) => void, // request the global render loop to render next frame
  renderScissor: ({ gl, scene, camera, top, left, width, height, layer, autoClear, clearDepth}) => void, // renders scene with a scissor to the canvas
  renderViewport:  ({ gl, scene, camera, top, left, width, height, layer, autoClear, clearDepth}) => void, // renders a scene inside a viewport to the canvas,
} = useScrollRig
```

### `useTracker`

Used internally by `ScrollScene` and `ViewportScrollScene` to track DOM elements as the user scrolls.

This hook makes a single call to `getBoundingClientRect` when it mounts and then uses scroll offsets to calculate the element's position during scroll.

It will not detect changes to the element size - only as a result of window resize.

It returns `scale` and `position` in Three.js units. `position` is not reactive to avoid expensive re-renders, so you need to read its properties in a rAF or on scroll.

```ts

interface TrackerOptions {
  rootMargin?: string = "50%" // IntersectionObserver
  threshold?: number = 0 // IntersectionObserver
  autoUpdate?: boolean = true // auto updates position/bounds/scrollState on scroll
}

const tracker: Tracker = useTracker(track: MutableRefObject<HTMLElement>, options?: TrackerOptions)

interface Tracker {
  rect: DOMRect // reactive pixel size
  scale: vec3 // reactive viewport unit scale
  inViewport: Boolean // reactive
  bounds: Bounds // non-reactive pixel bounds - updates on scroll
  position: vec3 // non-reactive viewport unit position, updates on scroll
  scrollState: ScrollState // non-reactive scroll stats, updates on scroll
  update: () => void // use to manually update position/bounds/scrollState
}
```

`vec3` is 3-dimensional vector type from [vecn](https://www.npmjs.com/package/vecn) that support swizzling and object notation. You can do things like:

```js
position.x === position[0]
position.xy => [x,y]
scale.xy.min() => Math.min(scale.x, scale.y)
```

The `scrollState` is also passed down to the children of `ScrollScene` and `ViewportScrollScene`:

```ts
export interface ScrollState {
  inViewport: boolean
  progress: number
  visibility: number
  viewport: number
}
```

### `useCanvas`

Hook used in regular DOM components to render something onto the `GlobalCanvas`.

```ts
const update = useCanvas(
  object: Object3D | (props) => Object3D,
  props = {},
  { key, dispose = true} = {}
): (props: any) => void
```

`object` will be added to the global canvas when this component is mounted and removed from the canvas when it unmounts.

`props` is an optional object can be used to automatically update those properties on the canvas object when they change due to a re-render of the parent component.

If `key` is specified, the mesh will not unmount as long as there are other hooks using this key. This can be used to make page transitions where an object moves seamlessly from one page to another.

if `dispose` is set to `false` - objects will never unmount from the canvas.

Returns a function that can be used to update the props of the `object` at any time.

```jsx
import { useCanvas } from '@14islands/r3f-scroll-rig';

function MyMesh() {
  return (
    <mesh>
      <boxGeometry args={[1,1,1]}/>
    </mesh>
  )
}

function MyComponent() {
  useCanvas(<MyMesh/>);
  return ...
}

```

### `useImageAsTexture`

Loads a `THREE.Texture` from a DOM image source.

Supports <picture> tags with multiple sources or responsive `srcset`.

It will wait for the DOM image to be loaded and then use the `currentSrc` to get a cache hit and upload the texture to the GPU.

It suspends until the texture is fully loaded and also notifies the Three.js `DefaultLoadingManager` that something is loading.

```jsx
function MyMesh({ imgTagRef, scale }) {
  const texture = useImageAsTexture(imgTagRef)
  return (
    <mesh scale={scale}>
      <planeGeometry />
      <meshBasicMaterial map={texture} />
    </mesh>
  )
}
```
```

## File: `powerups/ParallaxScrollScene.tsx`
```tsx
import React, { useRef } from 'react'
import { useFrame, useThree } from '@react-three/fiber'
import { Mesh } from 'three'

import { ScrollScene, useScrollRig } from '@14islands/r3f-scroll-rig'

// Parallax group inside ScrollScene
const ParallaxGroup = ({ children, scrollState, parallax }: any) => {
  const mesh = useRef<Mesh>(null!)
  const size = useThree((s) => s.size)
  const { scaleMultiplier } = useScrollRig()

  useFrame(() => {
    if (!scrollState.inViewport) return
    const parallaxProgress = scrollState.progress * 2 - 1
    mesh.current.position.y = parallax * parallaxProgress * scaleMultiplier * size.height
  })

  return <mesh ref={mesh}>{children}</mesh>
}

/* Speed=1 is no parallax */
export const ParallaxScrollScene = ({ children, speed = 1, ...props }: any) => {
  const extraMargin = 50 // add 50vh extra margin to avoid aggressive clipping
  const parallaxAmount = speed - 1
  return (
    // @ts-ignore
    <ScrollScene scissor={false} inViewportMargin={`${Math.max(0, 1 - 0.5) * 200 + extraMargin}%`} {...props}>
      {(props) => (
        <ParallaxGroup parallax={parallaxAmount} {...props}>
          {children(props)}
        </ParallaxGroup>
      )}
    </ScrollScene>
  )
}
```

## File: `powerups/Readme.md`
```markdown
# Powerups

These are example components built on top of the scroll-rig, useful for quick prototyping or inspiration.
```

## File: `powerups/StickyScrollScene.tsx`
```tsx
import React, { useRef, useMemo } from 'react'
import { useFrame, useThree } from '@react-three/fiber'
import { Group } from 'three'
import vecn from 'vecn'
// @ts-ignore
import lerp from '@14islands/lerp'

import { ScrollScene, useScrollRig } from '@14islands/r3f-scroll-rig'

// Sticky mesh that covers full viewport size
const StickyChild = ({
  children,
  childTop,
  childBottom,
  scrollState,
  parentScale,
  childScale,
  scaleMultiplier,
  priority,
  stickyLerp = 1.0,
  offsetTop = 0,
}: any) => {
  const group = useRef<Group>(null!)
  const size = useThree((s) => s.size)

  useFrame((_, delta) => {
    if (!scrollState.inViewport) return

    const topOffset = (childTop - offsetTop) / size.height
    const bottomOffset = (childBottom / parentScale[1]) * scaleMultiplier

    //  move to top of sticky area
    const yTop = parentScale[1] * 0.5 - childScale[1] * 0.5 - offsetTop * scaleMultiplier
    const yBottom = -parentScale[1] * 0.5 + childScale[1] * 0.5
    const ySticky =
      -childTop * scaleMultiplier +
      yTop -
      (scrollState.viewport - 1) * size.height * scaleMultiplier +
      offsetTop * scaleMultiplier

    let y = group.current.position.y

    // enter
    if (scrollState.viewport + topOffset < 1) {
      y = yTop
    }
    // sticky
    else if (scrollState.visibility - bottomOffset < 1) {
      y = ySticky
    }
    // exit
    else {
      y = yBottom
    }

    group.current.position.y = lerp(group.current.position.y, y, stickyLerp, delta)
  }, priority) // must happen after ScrollScene's useFrame to be buttery

  return <group ref={group}>{children}</group>
}

const renderAsSticky = (
  children: any,
  size: any,
  childStyle: any,
  parentStyle: any,
  scaleMultiplier: number,
  { stickyLerp, fillViewport }: any
) => {
  return ({ scale, ...props }: any) => {
    let childScale = vecn.vec3(parseFloat(childStyle.width), parseFloat(childStyle.height), 1)
    let childTop = parseFloat(childStyle.top)
    let childBottom = size.height - childTop - childScale[1]

    if (fillViewport) {
      childScale = vecn.vec3(size.width, size.height, 1)
      childTop = 0
      childBottom = 0
    }

    const offsetTop = parseFloat(parentStyle.top)

    return (
      // @ts-ignore
      <StickyChild
        offsetTop={offsetTop}
        parentScale={scale}
        childScale={childScale.times(scaleMultiplier)}
        stickyLerp={stickyLerp}
        childTop={childTop}
        childBottom={childBottom}
        scaleMultiplier={scaleMultiplier}
        {...props}
      >
        {children({
          scale: childScale.times(scaleMultiplier),
          parentScale: scale,
          ...props,
        })}
      </StickyChild>
    )
  }
}

export const StickyScrollScene = ({ children, track, stickyLerp, fillViewport, ...props }: any) => {
  const size = useThree((s) => s.size)
  const { scaleMultiplier } = useScrollRig()

  const internalRef = useRef(track.current)

  // if tracked element is position:sticky, track the parent instead
  // we want to track the progress of the entire sticky area
  const [childStyle, parentStyle] = useMemo(() => {
    const style = getComputedStyle(track.current)

    let parentStyle
    if (style.position === 'sticky') {
      internalRef.current = track.current.parentElement

      // make sure parent is relative/absolute so we get accurante offsetTop
      parentStyle = getComputedStyle(internalRef.current)
      if (parentStyle.position === 'static') {
        console.error(
          'StickyScrollScene: parent of position:sticky needs to be position:relative or position:absolute (currently set to position:static)'
        )
      }
    } else {
      console.error('StickyScrollScene: tracked element is not position:sticky')
    }
    return [style, parentStyle]
  }, [track, size])

  return (
    <ScrollScene track={internalRef} {...props}>
      {renderAsSticky(children, size, childStyle, parentStyle, scaleMultiplier, {
        stickyLerp,
        fillViewport,
      })}
    </ScrollScene>
  )
}
```

## File: `powerups/WebGLImage.tsx`
```tsx
import React, {
  useRef,
  useMemo,
  useEffect,
  forwardRef,
  MutableRefObject,
  ForwardedRef,
  useImperativeHandle,
} from 'react'
import { Color, Vector2, ShaderMaterial, Mesh, ShaderMaterialParameters } from 'three'
import { useFrame, useThree } from '@react-three/fiber'

import { useScrollRig, useImageAsTexture, useScrollbar } from '@14islands/r3f-scroll-rig'

interface WebGLImageProps {
  el: MutableRefObject<HTMLImageElement>
  scale?: any
  scrollState?: any
  vertexShader?: string
  fragmentShader?: string
  invalidateFrameLoop: boolean
  widthSegments?: number
  heightSegments?: number
}

export const WebGLImage = forwardRef(
  (
    {
      el,
      scale,
      scrollState,
      vertexShader,
      fragmentShader,
      invalidateFrameLoop = false,
      widthSegments = 128,
      heightSegments = 128,
      ...props
    }: WebGLImageProps,
    ref: ForwardedRef<Mesh>
  ) => {
    const material = useRef<ShaderMaterial>(null!)
    const mesh = useRef<Mesh>(null!)
    useImperativeHandle(ref, () => mesh.current)

    const { invalidate, gl, size } = useThree()
    const pixelRatio = useThree((s) => s.viewport.dpr)
    const { scroll } = useScrollbar()
    const { scaleMultiplier } = useScrollRig()

    const texture = useImageAsTexture(el)

    const uniforms = useMemo(() => {
      return {
        u_color: { value: new Color('black') },
        u_time: { value: 0 },
        u_pixelRatio: { value: pixelRatio },
        u_progress: { value: 0 },
        u_visibility: { value: 0 },
        u_viewport: { value: 0 },
        u_velocity: { value: 0 }, // scroll speed
        u_res: { value: new Vector2() }, // screen dimensions
        u_rect: { value: new Vector2() }, // DOM el dimensions
        u_size: { value: new Vector2() }, // Texture dimensions
        u_texture: { value: null },
        u_loaded: { value: false },
        u_scaleMultiplier: { value: scaleMultiplier },
      }
    }, [pixelRatio])

    // Fade in when texture loaded
    useEffect(() => {
      if (!texture) return
      if (!material.current) return
      material.current.uniforms.u_texture.value = texture
      material.current.uniforms.u_size.value.set(texture.image.width, texture.image.height)
      material.current.uniforms.u_loaded.value = true
    }, [texture, gl])

    useEffect(() => {
      if (!material.current) return
      material.current.uniforms.u_res.value.set(size.width, size.height)
      material.current.uniforms.u_rect.value.set(scale?.[0], scale?.[1])
    }, [size, scale])

    useFrame((_, delta) => {
      if (!scrollState.inViewport || !mesh.current || !material.current) return

      if (!material.current.uniforms.u_loaded.value) return

      material.current.uniforms.u_time.value += delta

      // update scale while animating too
      material.current.uniforms.u_rect.value.set(mesh.current.scale.x, mesh.current.scale.y)

      // px velocity
      material.current.uniforms.u_velocity.value = scroll.velocity

      // percent of total visible distance that was scrolled (0 = just outside bottom of screen, 1 = just outside top of screen)
      material.current.uniforms.u_progress.value = scrollState.progress

      // percent of item height in view
      material.current.uniforms.u_visibility.value = scrollState.visibility
      // percent of window height scrolled since visible
      material.current.uniforms.u_viewport.value = scrollState.viewport

      if (invalidateFrameLoop) invalidate()
    })

    const args = useMemo(
      () => [
        {
          vertexShader,
          fragmentShader,
        },
      ],
      [vertexShader, fragmentShader]
    )

    return (
      <>
        <mesh ref={mesh} {...props}>
          <planeGeometry attach="geometry" args={[1, 1, widthSegments, heightSegments]} />
          <shaderMaterial
            ref={material}
            args={args as [ShaderMaterialParameters]}
            transparent={true}
            uniforms={uniforms}
          />
        </mesh>
      </>
    )
  }
)
```

## File: `powerups/WebGLText.tsx`
```tsx
import React, { useMemo, useEffect, ReactNode, MutableRefObject } from 'react'
import { Color, Material } from 'three'
import { useThree } from '@react-three/fiber'
import { Text } from '@react-three/drei'

import { useScrollRig } from '@14islands/r3f-scroll-rig'

/**
 * Returns a WebGL Troika text mesh styled as the source DOM element
 */

interface WebGLTextProps {
  el: MutableRefObject<HTMLElement>
  children?: ReactNode
  material?: Material
  scale?: any
  font?: string
  fontOffsetY?: number
  fontOffsetX?: number
  overrideEmissive?: boolean
  color?: string
}

export const WebGLText = ({
  el,
  children,
  material,
  scale,
  font,
  fontOffsetY = 0,
  fontOffsetX = 0,
  overrideEmissive = false,
  color,
  ...props
}: WebGLTextProps) => {
  const { size } = useThree()
  const { scaleMultiplier } = useScrollRig()

  const { textColor, fontSize, textAlign, lineHeight, letterSpacing } = useMemo(() => {
    if (!el.current) return {}
    const cs = window.getComputedStyle(el.current)

    // get color from parent if set to transparent
    let textColor = color || cs.color
    if (!color && cs.color === 'rgba(0, 0, 0, 0)' && el.current.parentElement) {
      textColor = window.getComputedStyle(el.current.parentElement).color
    }

    // font size relative letter spacing
    const letterSpacing = (parseFloat(cs.letterSpacing) || 0) / parseFloat(cs.fontSize)
    const lineHeight = (parseFloat(cs.lineHeight) || 0) / parseFloat(cs.fontSize)

    return {
      letterSpacing,
      lineHeight,
      textColor,
      fontSize: parseFloat(cs.fontSize) * scaleMultiplier,
      textAlign: cs.textAlign,
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [el, size, scale, color, scaleMultiplier]) // recalc on resize

  useEffect(() => {
    if (material && overrideEmissive) {
      // @ts-ignore
      material.emissive = color
    }
  }, [material, color, overrideEmissive])

  let xOffset = 0
  if (textAlign === 'left' || textAlign === 'start') {
    xOffset = scale[0] * -0.5
  } else if (textAlign === 'right' || textAlign === 'end') {
    xOffset = scale[0] * 0.5
  }

  const yOffset = scale ? scale[1] * 0.5 : size.height * 0.5

  return (
    <Text
      fontSize={fontSize}
      maxWidth={scale ? scale[0] : size.width}
      lineHeight={lineHeight}
      // @ts-ignore
      textAlign={textAlign}
      letterSpacing={letterSpacing}
      overflowWrap="break-word"
      font={font}
      color={textColor}
      // @ts-ignore
      anchorX={textAlign}
      anchorY="top" // so text moves down if row breaks
      // @ts-ignore
      position={[xOffset + fontSize * fontOffsetX, yOffset + fontSize * fontOffsetY, 0]} // font specific
      material={material}
      {...props}
    >
      {children}
    </Text>
  )
}
```

## File: `powerups/index.ts`
```typescript
export { WebGLText } from './WebGLText'
export { WebGLImage } from './WebGLImage'
export { ParallaxScrollScene } from './ParallaxScrollScene'
export { StickyScrollScene } from './StickyScrollScene'
```

## File: `powerups/package.json`
```json
{
  "main": "../dist/powerups.cjs.js",
  "module": "../dist/powerups.js",
  "types": "../dist/powerups/index.d.ts",
  "type": "module",
  "exports": {
    "types": "./dist/powerups/index.d.ts",
    "require": "./dist/powerups.cjs",
    "import": "./dist/powerups.modern.js"
  }
}
```

## File: `scrollbar/Readme.md`
```markdown
# Scrollbar

Import the scrollbar from this target to avoid bundling react-three-fiber.

```jsx
import { SmoothScrollbar, useScrollbar, useTracker } from '@14islands/r3f-scroll-rig/scrollbar'
```
```

## File: `scrollbar/package.json`
```json
{
  "main": "../dist/scrollbar.cjs.js",
  "module": "../dist/scrollbar.js",
  "types": "../dist/scrollbar/index.d.ts",
  "type": "module",
  "exports": {
    "types": "./dist/scrollbar/index.d.ts",
    "require": "./dist/scrollbar.cjs",
    "import": "./dist/scrollbar.modern.js"
  }
}
```

## File: `src/config.ts`
```typescript
// Global config

// avoid Three types to ease tree shaking
type PreloadCallback = (gl: any, scene: any, camera: any) => void

export const config = {
  // Execution order for useFrames (highest = last render)
  PRIORITY_PRELOAD: 0,
  PRIORITY_SCISSORS: 1,
  PRIORITY_VIEWPORTS: 1,
  PRIORITY_GLOBAL: 1000,

  DEFAULT_SCALE_MULTIPLIER: 1,

  // Global rendering props
  preloadQueue: [] as PreloadCallback[],
}
```

## File: `src/index.ts`
```typescript
import './styles/index.css'

// Components
export { GlobalCanvas } from './components/GlobalCanvas'
export { type ScrollSceneChildProps, ScrollScene } from './components/ScrollScene'
export { type ViewportScrollSceneChildProps, ViewportScrollScene } from './components/ViewportScrollScene'
export { UseCanvas } from './components/UseCanvas'

// Hooks
export { useScrollRig } from './hooks/useScrollRig'
export { useCanvas } from './hooks/useCanvas'
export { useScrollbar } from './scrollbar/useScrollbar'
export { useTracker } from './hooks/useTracker'
export { useWindowSize } from './hooks/useWindowSize'

// Utils hooks
export { useImageAsTexture } from './hooks/useImageAsTexture'

// Scrollbar
export { default as SmoothScrollbar } from './components/R3FSmoothScrollbar'

// CSS class names for hiding stuff
// Matching css styles can be imported from @14islands/r3f-scrollr-rig/css
export const styles = {
  hidden: 'ScrollRig-visibilityHidden',
  hiddenWhenSmooth: 'ScrollRig-visibilityHidden ScrollRig-hiddenIfSmooth',
  transparentColor: 'ScrollRig-transparentColor',
  transparentColorWhenSmooth: 'ScrollRig-transparentColor ScrollRig-hiddenIfSmooth',
}

// Private-ish
// ----------------------------------
export { useCanvasStore } from './store'

// Types
export type { ScrollState } from './hooks/useTrackerTypes'
```

## File: `src/renderer-api.ts`
```typescript
import { config } from './config'
import { Vector2, WebGLRenderer, Scene, Camera } from 'three'
import { invalidate } from '@react-three/fiber'

import { setAllCulled } from './utils/helpers'
import { useCanvasStore } from './store'

const viewportSize = new Vector2()

// Flag that we need global rendering (full screen)
export const requestRender = (layers = [0]) => {
  useCanvasStore.getState().globalRenderQueue = useCanvasStore.getState().globalRenderQueue || [0]
  useCanvasStore.getState().globalRenderQueue = [...(useCanvasStore.getState().globalRenderQueue || []), ...layers]
}

export const renderScissor = ({
  gl,
  scene,
  camera,
  left,
  top,
  width,
  height,
  layer = 0,
  autoClear = false,
  clearDepth = false,
}: any) => {
  if (!scene || !camera) return
  gl.autoClear = autoClear
  gl.setScissor(left, top, width, height)
  gl.setScissorTest(true)
  camera.layers.set(layer)
  clearDepth && gl.clearDepth()
  gl.render(scene, camera)
  gl.setScissorTest(false)
}

export const renderViewport = ({
  gl,
  scene,
  camera,
  left,
  top,
  width,
  height,
  layer = 0,
  scissor = true,
  autoClear = false,
  clearDepth = false,
}: any) => {
  if (!scene || !camera) return
  gl.getSize(viewportSize)
  gl.autoClear = autoClear
  gl.setViewport(left, top, width, height)
  gl.setScissor(left, top, width, height)
  gl.setScissorTest(scissor)
  camera.layers.set(layer)
  clearDepth && gl.clearDepth()
  gl.render(scene, camera)
  gl.setScissorTest(false)
  gl.setViewport(0, 0, viewportSize.x, viewportSize.y)
}

export const preloadScene = (
  { scene, camera, layer = 0 }: { scene?: Scene; camera?: Camera; layer?: number },
  callback?: () => void
) => {
  config.preloadQueue.push((gl: WebGLRenderer, globalScene: Scene, globalCamera: Camera) => {
    gl.setScissorTest(false)
    setAllCulled(scene || globalScene, false)
    ;(camera || globalCamera).layers.set(layer)
    gl.render(scene || globalScene, camera || globalCamera)
    setAllCulled(scene || globalScene, true)
    callback && callback()
  })
  // auto trigger a new frame for the preload
  invalidate()
}
```

## File: `src/store.ts`
```typescript
import create from 'zustand'
import { config } from './config'
import type Lenis from 'lenis'

import { ScrollCallback, ScrollData } from './scrollbar/SmoothScrollbarTypes'

interface ScrollRigStore {
  debug: boolean
  scaleMultiplier: number
  globalRender: boolean
  globalPriority: number
  globalClearDepth: boolean
  globalRenderQueue: false | any[]
  clearGlobalRenderQueue: () => void
  isCanvasAvailable: boolean
  hasSmoothScrollbar: boolean
  canvasChildren: Record<string, any | undefined>
  updateCanvas: (key: string, newProps: any) => void
  renderToCanvas: (key: string, mesh: any, props: any) => void
  removeFromCanvas: (key: string, dispose: boolean) => void
  pageReflow: number
  requestReflow: () => void
  scroll: ScrollData
  __lenis: Lenis | undefined
  scrollTo: (target: any) => void
  onScroll: (cb: ScrollCallback) => () => void
}

const useCanvasStore = create<ScrollRigStore>((set) => ({
  // //////////////////////////////////////////////////////////////////////////
  // GLOBAL ScrollRig STATE
  // //////////////////////////////////////////////////////////////////////////
  debug: false,
  scaleMultiplier: config.DEFAULT_SCALE_MULTIPLIER,

  globalRender: true,
  globalPriority: config.PRIORITY_GLOBAL,
  globalClearDepth: false,

  globalRenderQueue: false,
  clearGlobalRenderQueue: () => set(() => ({ globalRenderQueue: false })),

  // true if WebGL initialized without errors
  isCanvasAvailable: false,

  // true if <VirtualScrollbar> is currently enabled
  hasSmoothScrollbar: false,

  // map of all components to render on the global canvas
  canvasChildren: {},

  // add component to canvas
  renderToCanvas: (key, mesh, props = {}) =>
    set(({ canvasChildren }) => {
      // check if already mounted
      if (Object.getOwnPropertyDescriptor(canvasChildren, key)) {
        // increase usage count
        canvasChildren[key].instances += 1
        canvasChildren[key].props.inactive = false
        return { canvasChildren }
      } else {
        // otherwise mount it
        const obj = { ...canvasChildren, [key]: { mesh, props, instances: 1 } }
        return { canvasChildren: obj }
      }
    }),

  // pass new props to a canvas component
  updateCanvas: (key, newProps) =>
    // @ts-ignore
    set(({ canvasChildren }) => {
      if (!canvasChildren[key]) return
      const {
        [key]: { mesh, props, instances },
      } = canvasChildren
      const obj = {
        ...canvasChildren,
        [key]: { mesh, props: { ...props, ...newProps }, instances },
      }
      // console.log('updateCanvas', key, { ...props, ...newProps })
      return { canvasChildren: obj }
    }),

  // remove component from canvas
  removeFromCanvas: (key, dispose = true) =>
    set(({ canvasChildren }) => {
      // check if remove or reduce instances
      if (canvasChildren[key]?.instances > 1) {
        // reduce usage count
        canvasChildren[key].instances -= 1
        return { canvasChildren }
      } else {
        if (dispose) {
          // unmount since no longer used
          const { [key]: _omit, ...obj } = canvasChildren // make a separate copy of the obj and omit
          return { canvasChildren: obj }
        } else {
          // or tell it that it is "inactive"
          canvasChildren[key].instances = 0
          canvasChildren[key].props.inactive = true
          return { canvasChildren: { ...canvasChildren } }
        }
      }
    }),

  // Used to ask components to re-calculate their positions after a layout reflow
  pageReflow: 0,
  requestReflow: () => {
    set((state) => {
      return { pageReflow: state.pageReflow + 1 }
    })
  },

  // keep track of scrollbar
  scroll: {
    y: 0,
    x: 0,
    limit: 0,
    velocity: 0,
    progress: 0,
    direction: 0,
    scrollDirection: undefined,
  },
  __lenis: undefined,
  scrollTo: () => {},
  onScroll: () => () => {},
}))

export { useCanvasStore }
```

## File: `src/components/CanvasErrorBoundary.tsx`
```tsx
// @ts-nocheck
import { Component, ReactNode } from 'react'

interface ICanvasErrorBoundary {
  children: ReactNode
  onError: () => void
}

export class CanvasErrorBoundary extends Component<{}, ICanvasErrorBoundary> {
  constructor(props) {
    super(props)
    this.state = { error: false }
    this.props = props
  }

  static getDerivedStateFromError(error) {
    // Update state so the next render will show the fallback UI.
    return { error }
  }

  // componentDidCatch(error, errorInfo) {
  //   // You can also log the error to an error reporting service
  //   // logErrorToMyService(error, errorInfo)
  // }

  render() {
    if (this.state.error) {
      this.props.onError && this.props.onError(this.state.error)
      return null
    }

    return this.props.children
  }
}
```

## File: `src/components/DebugMesh.tsx`
```tsx
import React from 'react'
import { Color } from 'three'

export const DebugMesh = ({ scale }: { scale: [x: number, y: number, z: number] }) => (
  <mesh scale={scale}>
    <planeGeometry />
    <shaderMaterial
      args={[
        {
          uniforms: {
            color: { value: new Color('hotpink') },
          },
          vertexShader: `
            void main() {
              gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
            }
          `,
          fragmentShader: `
            uniform vec3 color;
            uniform float opacity;
            void main() {
              gl_FragColor.rgba = vec4(color, .5);
            }
          `,
        },
      ]}
      transparent
    />
  </mesh>
)
```

## File: `src/components/GlobalCanvas.tsx`
```tsx
import React, { ReactNode, startTransition } from 'react'
import { Canvas, Props } from '@react-three/fiber'
import { ResizeObserver as Polyfill } from '@juggle/resize-observer'
import { parse } from 'query-string'

import { useLayoutEffect } from '../hooks/useIsomorphicLayoutEffect'
import { useCanvasStore } from '../store'
import { ResizeManager } from './ResizeManager'
import { PerspectiveCamera } from './PerspectiveCamera'
import { OrthographicCamera } from './OrthographicCamera'

import { GlobalChildren } from './GlobalChildren'
import { GlobalRenderer } from './GlobalRenderer'
import { CanvasErrorBoundary } from './CanvasErrorBoundary'

import { config } from '../config'
import { version } from '../../package.json'

let polyfill: new (callback: ResizeObserverCallback) => ResizeObserver
if (typeof window !== 'undefined') {
  polyfill = window.ResizeObserver || Polyfill
}

interface IGlobalCanvas extends Omit<Props, 'children'> {
  children?: ReactNode | ((globalChildren: ReactNode) => ReactNode)
  as?: any
  orthographic?: boolean
  onError?: (props: any) => void
  camera?: any
  // state
  debug?: boolean
  scaleMultiplier?: number
  globalRender?: boolean
  globalPriority?: number
  globalClearDepth?: boolean
}

const GlobalCanvasImpl = ({
  children,
  as = Canvas,
  gl,
  style,
  orthographic,
  camera,
  debug,
  scaleMultiplier = config.DEFAULT_SCALE_MULTIPLIER,
  globalRender = true,
  globalPriority = config.PRIORITY_GLOBAL,
  globalClearDepth = false,
  ...props
}: Omit<IGlobalCanvas, 'onError'>) => {
  const useGlobalRenderer = useCanvasStore((state) => state.globalRender)

  // enable debug mode
  useLayoutEffect(() => {
    if (typeof window !== 'undefined') {
      // @ts-ignore
      window.__r3f_scroll_rig = version
    }

    // Querystring overridess
    const qs = parse(window.location.search)

    // show debug statements
    if (debug || typeof qs.debug !== 'undefined') {
      useCanvasStore.setState({ debug: true })
      console.info('@14islands/r3f-scroll-rig@' + version)
    }
  }, [debug])

  // update state
  useLayoutEffect(() => {
    // update as transition so we don't interrupt active suspenses
    startTransition(() => {
      useCanvasStore.setState({
        scaleMultiplier,
        globalRender,
        globalPriority,
        globalClearDepth,
      })
    })
  }, [scaleMultiplier, globalPriority, globalRender, globalClearDepth])

  const As = as

  return (
    <As
      id="ScrollRig-canvas"
      // use our own default camera
      camera={{
        manual: true,
      }}
      // Some sane defaults
      gl={{
        // https://blog.tojicode.com/2013/12/failifmajorperformancecaveat-with-great.html
        failIfMajorPerformanceCaveat: true, // skip webgl if slow device
        ...gl,
      }}
      // polyfill old iOS safari
      resize={{ scroll: false, debounce: 0, polyfill }}
      // default styles
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        height: '100vh', // use 100vh to avoid resize on iOS when url bar goes away
        ...style,
      }}
      // allow to override anything of the above
      {...props}
    >
      {/* @ts-ignore */}
      {!orthographic && <PerspectiveCamera manual makeDefault {...camera} />}
      {/* @ts-ignore */}
      {orthographic && <OrthographicCamera manual makeDefault {...camera} />}

      {useGlobalRenderer && <GlobalRenderer />}

      {typeof children === 'function' ? children(<GlobalChildren />) : <GlobalChildren>{children}</GlobalChildren>}

      <ResizeManager />
    </As>
  )
}

export const GlobalCanvas = ({ children, onError, ...props }: IGlobalCanvas) => {
  useLayoutEffect(() => {
    document.documentElement.classList.add('js-has-global-canvas')
    useCanvasStore.setState({ isCanvasAvailable: true })
  }, [])

  return (
    // @ts-ignore
    <CanvasErrorBoundary
      onError={(err: any) => {
        onError && onError(err)
        useCanvasStore.setState({ isCanvasAvailable: false }) /* WebGL failed to init */
        document.documentElement.classList.remove('js-has-global-canvas')
        document.documentElement.classList.add('js-global-canvas-error')
      }}
    >
      <GlobalCanvasImpl {...props}>{children}</GlobalCanvasImpl>
      <noscript>
        <style>
          {`
          .ScrollRig-visibilityHidden,
          .ScrollRig-transparentColor {
            visibility: unset;
            color: unset;
          }
          `}
        </style>
      </noscript>
    </CanvasErrorBoundary>
  )
}
```

## File: `src/components/GlobalChildren.tsx`
```tsx
import React, { Fragment, useEffect, ReactNode, cloneElement } from 'react'
import { invalidate, useThree } from '@react-three/fiber'

import { useCanvasStore } from '../store'
import { useScrollRig } from '../hooks/useScrollRig'

/**
 * Renders global children from useCanvas hook
 */
export const GlobalChildren = ({ children }: { children?: ReactNode }) => {
  const gl = useThree((s) => s.gl)
  const canvasChildren = useCanvasStore((state) => state.canvasChildren)
  const scrollRig = useScrollRig()

  useEffect(() => {
    // render empty canvas automatically if all children were removed
    if (!Object.keys(canvasChildren).length) {
      scrollRig.debug && console.log('GlobalRenderer', 'auto render empty canvas')
      // clear leftover viewports etc from unmounted components
      gl.clear()
      // re-render global scene in case frameloop="demand" to avoid empty canvas
      scrollRig.requestRender()
      invalidate()
    }
  }, [canvasChildren])

  scrollRig.debug && console.log('GlobalChildren', Object.keys(canvasChildren).length)
  return (
    <>
      {children}
      {Object.keys(canvasChildren).map((key) => {
        const { mesh, props } = canvasChildren[key]

        if (typeof mesh === 'function') {
          return <Fragment key={key}>{mesh({ key, ...scrollRig, ...props })}</Fragment>
        }

        return cloneElement(mesh, {
          key,
          ...props,
        })
      })}
    </>
  )
}
```

## File: `src/components/GlobalRenderer.tsx`
```tsx
import { useThree, useFrame, invalidate } from '@react-three/fiber'

import { useLayoutEffect } from '../hooks/useIsomorphicLayoutEffect'
import { config } from '../config'
import { useCanvasStore } from '../store'
import { useScrollRig } from '../hooks/useScrollRig'

/**
 * Global render loop to avoid double renders on the same frame
 */
export const GlobalRenderer = () => {
  const gl = useThree((s) => s.gl)
  const frameloop = useThree((s) => s.frameloop)
  const globalClearDepth = useCanvasStore((state) => state.globalClearDepth)
  const globalPriority = useCanvasStore((state) => state.globalPriority)
  const scrollRig = useScrollRig()

  // https://threejs.org/brain/knowledge/docs_legacy/#api/en/renderers/WebGLRenderer.debug
  useLayoutEffect(() => {
    gl.debug.checkShaderErrors = scrollRig.debug
  }, [scrollRig.debug])

  // PRELOAD RENDER LOOP
  useFrame(({ camera, scene }) => {
    if (!config.preloadQueue.length) return
    // Render preload frames first and clear directly
    config.preloadQueue.forEach((render) => render(gl, scene, camera))
    // cleanup
    gl.clear()
    config.preloadQueue = []
    // trigger new frame to get correct visual state after all preloads
    scrollRig.debug && console.log('GlobalRenderer', 'preload complete. trigger global render')
    scrollRig.requestRender()
    invalidate()
  }, config.PRIORITY_PRELOAD)

  // GLOBAL RENDER LOOP
  useFrame(({ camera, scene }) => {
    const globalRenderQueue = useCanvasStore.getState().globalRenderQueue

    // Render if requested or if always on
    if (frameloop === 'always' || globalRenderQueue) {
      // render default layer, scene, camera
      camera.layers.disableAll()
      if (globalRenderQueue) {
        // @ts-ignore
        globalRenderQueue.forEach((layer) => {
          camera.layers.enable(layer)
        })
      } else {
        camera.layers.enable(0)
      }

      // render as HUD over any other renders by default
      globalClearDepth && gl.clearDepth()
      gl.render(scene, camera)
    }
    // cleanup for next frame
    useCanvasStore.getState().clearGlobalRenderQueue()
  }, globalPriority) // Take over rendering

  return null
}
```

## File: `src/components/OrthographicCamera.tsx`
```tsx
import React, { useRef, forwardRef, useMemo, useImperativeHandle } from 'react'
import { OrthographicCamera as OrthographicCameraImpl } from 'three'
import { useThree } from '@react-three/fiber'

import { useLayoutEffect } from '../hooks/useIsomorphicLayoutEffect'
import { useCanvasStore } from '../store'

type Props = JSX.IntrinsicElements['orthographicCamera'] & {
  makeDefault?: boolean
  margin?: number
}
export const OrthographicCamera = forwardRef(({ makeDefault = false, margin = 0, ...props }: Props, ref) => {
  const set = useThree((state) => state.set)
  const camera = useThree((state) => state.camera)
  const size = useThree((state) => state.size)

  const pageReflow = useCanvasStore((state) => state.pageReflow)
  const scaleMultiplier = useCanvasStore((state) => state.scaleMultiplier)

  const distance = useMemo(() => {
    const width = size.width * scaleMultiplier
    const height = size.height * scaleMultiplier
    return Math.max(width, height)
  }, [size, pageReflow, scaleMultiplier])

  const cameraRef = useRef<OrthographicCameraImpl>(null!)
  useImperativeHandle(ref, () => cameraRef.current)
  useLayoutEffect(() => {
    cameraRef.current.lookAt(0, 0, 0)
    cameraRef.current.updateProjectionMatrix()
    // https://github.com/react-spring/@react-three/fiber/issues/178
    // Update matrix world since the renderer is a frame late
    cameraRef.current.updateMatrixWorld()
  }, [distance, size])

  useLayoutEffect(() => {
    if (makeDefault) {
      const oldCam = camera
      set(() => ({ camera: cameraRef.current! }))
      return () => set(() => ({ camera: oldCam }))
    }
    // The camera should not be part of the dependency list because this components camera is a stable reference
    // that must exchange the default, and clean up after itself on unmount.
  }, [cameraRef, makeDefault, set])

  return (
    <orthographicCamera
      left={(size.width * scaleMultiplier) / -2 - margin * scaleMultiplier}
      right={(size.width * scaleMultiplier) / 2 + margin * scaleMultiplier}
      top={(size.height * scaleMultiplier) / 2 + margin * scaleMultiplier}
      bottom={(size.height * scaleMultiplier) / -2 - margin * scaleMultiplier}
      far={distance * 2}
      position={[0, 0, distance]}
      near={0.001}
      ref={cameraRef}
      onUpdate={(self) => self.updateProjectionMatrix()}
      {...props}
    />
  )
})
```

## File: `src/components/PerspectiveCamera.tsx`
```tsx
import React, { useRef, forwardRef, useMemo, useImperativeHandle } from 'react'
import { useThree } from '@react-three/fiber'
import { PerspectiveCamera as PerspectiveCameraImpl } from 'three'

import { useLayoutEffect } from '../hooks/useIsomorphicLayoutEffect'
import { useCanvasStore } from '../store'

type Props = JSX.IntrinsicElements['perspectiveCamera'] & {
  makeDefault?: boolean
  margin?: number
}

const DEFAULT_FOV = 50

export const PerspectiveCamera = forwardRef(({ makeDefault = false, margin = 0, ...props }: Props, ref) => {
  const set = useThree((state) => state.set)
  const camera = useThree((state) => state.camera)
  const size = useThree((state) => state.size)
  const viewport = useThree((state) => state.viewport)
  const cameraRef = useRef<PerspectiveCameraImpl>(null!)
  useImperativeHandle(ref, () => cameraRef.current)

  const pageReflow = useCanvasStore((state) => state.pageReflow)
  const scaleMultiplier = useCanvasStore((state) => state.scaleMultiplier)

  // Calculate FoV or distance to match DOM size
  const { fov, distance, aspect } = useMemo(() => {
    const width = (size.width + margin * 2) * scaleMultiplier
    const height = (size.height + margin * 2) * scaleMultiplier
    const aspect = width / height

    // check props vs defaults
    let fov = props.fov || DEFAULT_FOV
    let distance = (props?.position as number[])?.[2]

    // calculate either FoV or distance to match scale
    if (distance) {
      // calculate FoV based on distance
      fov = 2 * (180 / Math.PI) * Math.atan(height / (2 * distance))
    } else {
      // calculate distance for specified FoV
      const ratio = Math.tan(((fov / 2.0) * Math.PI) / 180.0) * 2.0
      distance = height / ratio
    }

    return { fov, distance, aspect }
  }, [size, scaleMultiplier, pageReflow])

  // Update camera projection and R3F viewport
  useLayoutEffect(() => {
    cameraRef.current.lookAt(0, 0, 0)
    cameraRef.current.updateProjectionMatrix()
    // https://github.com/react-spring/@react-three/fiber/issues/178
    // Update matrix world since the renderer is a frame late
    cameraRef.current.updateMatrixWorld()
    // update r3f viewport which is lagging on resize
    set((state) => ({ viewport: { ...state.viewport, ...viewport.getCurrentViewport(camera) } }))
  }, [size, scaleMultiplier, pageReflow])

  useLayoutEffect(() => {
    if (makeDefault) {
      const oldCam = camera
      set(() => ({ camera: cameraRef.current! }))
      return () => set(() => ({ camera: oldCam }))
    }
    // The camera should not be part of the dependency list because this components camera is a stable reference
    // that must exchange the default, and clean up after itself on unmount.
  }, [cameraRef, makeDefault, set])

  return (
    <perspectiveCamera
      ref={cameraRef}
      position={[0, 0, distance]}
      onUpdate={(self) => self.updateProjectionMatrix()}
      near={0.1}
      aspect={aspect}
      fov={fov}
      far={distance * 2}
      {...props}
    />
  )
})
```

## File: `src/components/R3FSmoothScrollbar.tsx`
```tsx
import React, { forwardRef } from 'react'
import { SmoothScrollbar } from '../scrollbar/SmoothScrollbar'
import { ISmoothScrollbar } from '../scrollbar/SmoothScrollbarTypes'
import { addEffect, invalidate } from '@react-three/fiber'
import { useCanvasStore } from '../store'

function R3FSmoothScrollbar(props: ISmoothScrollbar, ref: any) {
  const isCanvasAvailable = useCanvasStore((s) => s.isCanvasAvailable)
  if (!isCanvasAvailable) return <SmoothScrollbar key="native" ref={ref} {...props} />
  return <SmoothScrollbar key="r3f" ref={ref} invalidate={invalidate} addEffect={addEffect} {...props} />
}

export default forwardRef<any, ISmoothScrollbar>(R3FSmoothScrollbar)
```

## File: `src/components/ResizeManager.ts`
```typescript
import { useEffect } from 'react'
import { ResizeObserver as Polyfill } from '@juggle/resize-observer'

import { useCanvasStore } from '../store'

/**
 * Trigger reflow when WebFonts loaded
 */
export const ResizeManager = () => {
  const requestReflow = useCanvasStore((state) => state.requestReflow)
  const debug = useCanvasStore((state) => state.debug)

  // reflow on webfont loaded to prevent misalignments
  useEffect(() => {
    const ResizeObserver = window.ResizeObserver || Polyfill

    // watch out for any random height change
    let observer = new ResizeObserver(() => {
      requestReflow()
      debug && console.log('ResizeManager', 'document.body height changed')
    })
    observer.observe(document.body)
    return () => {
      observer?.disconnect()
    }
  }, [])

  return null
}
```

## File: `src/components/ScrollScene.tsx`
```tsx
import React, { useEffect, useState, useRef, MutableRefObject, ReactNode } from 'react'
import { Scene, Group } from 'three'
import { useFrame, createPortal, useThree } from '@react-three/fiber'

import { useLayoutEffect } from '../hooks/useIsomorphicLayoutEffect'
import { config } from '../config'
import { useCanvasStore } from '../store'
import { useScrollRig } from '../hooks/useScrollRig'
import { DebugMesh } from './DebugMesh'
import { useTracker } from '../hooks/useTracker'
import type { ScrollState } from '../hooks/useTrackerTypes'

export interface ScrollSceneChildProps {
  track: MutableRefObject<HTMLElement>
  margin: number
  priority: number
  scale: vec3
  scrollState: ScrollState
  inViewport: boolean
  scene: Scene
}

interface IScrollScene {
  track: MutableRefObject<HTMLElement>
  children: (state: ScrollSceneChildProps) => ReactNode
  margin?: number
  inViewportMargin?: string
  inViewportThreshold?: number
  visible?: boolean
  hideOffscreen?: boolean
  scissor?: boolean
  debug?: boolean
  as?: string
  priority?: number
  scene?: Scene
}

/**
 * Generic THREE.js Scene that tracks the dimensions and position of a DOM element while scrolling
 * Scene is positioned and scaled exactly above DOM element
 *
 * @author david@14islands.com
 */
function ScrollScene({
  track,
  children,
  margin = 0, // Margin outside scissor to avoid clipping vertex displacement (px)
  inViewportMargin,
  inViewportThreshold,
  visible = true,
  hideOffscreen = true,
  scissor = false,
  debug = false,
  as = 'scene',
  priority = config.PRIORITY_SCISSORS,
  scene,
  ...props
}: IScrollScene) {
  const globalScene = useThree((s) => s.scene)
  const contentRef = useRef<Group>()
  const [portalScene] = useState<Scene | null>(scene || (scissor ? new Scene() : null))
  const { requestRender, renderScissor } = useScrollRig()
  const globalRender = useCanvasStore((state) => state.globalRender)

  const { bounds, scale, position, scrollState, inViewport } = useTracker(track, {
    rootMargin: inViewportMargin,
    threshold: inViewportThreshold,
  })

  // Hide content when outside of viewport if `hideOffscreen` or set to `visible` prop
  useLayoutEffect(() => {
    if (!contentRef.current) return
    contentRef.current.visible = hideOffscreen ? inViewport && visible : visible
  }, [inViewport, hideOffscreen, visible])

  // move content into place visibility or scale changes
  useEffect(() => {
    if (!contentRef.current) return
    contentRef.current.position.y = position.y
    contentRef.current.position.x = position.x
  }, [scale, inViewport]) // scale updates on resize

  // RENDER FRAME
  useFrame(
    ({ gl, camera }) => {
      if (!contentRef.current) return

      if (contentRef.current.visible) {
        // move content
        contentRef.current.position.y = position.y
        contentRef.current.position.x = position.x

        if (scissor) {
          renderScissor({
            gl,
            portalScene,
            camera,
            left: bounds.left - margin,
            top: bounds.positiveYUpBottom - margin,
            width: bounds.width + margin * 2,
            height: bounds.height + margin * 2,
          })
        } else {
          requestRender()
        }
      }
    },
    globalRender ? priority : undefined
  )

  const InlineElement: any = as
  const content = (
    <InlineElement ref={contentRef}>
      {(!children || debug) && scale && <DebugMesh scale={scale} />}
      {children &&
        scale &&
        children({
          // inherited props
          track,
          margin,
          scene: portalScene || globalScene,
          // new props from tracker
          scale,
          scrollState,
          inViewport,
          // useFrame render priority (in case children need to run after)
          priority: priority,
          // tunnel the rest
          ...props,
        })}
    </InlineElement>
  )

  // render in portal if requested
  return portalScene ? createPortal(content, portalScene) : content
}

export { ScrollScene }
```

## File: `src/components/UseCanvas.tsx`
```tsx
import { forwardRef, ReactNode } from 'react'
import { useCanvas } from '../hooks/useCanvas'

import { ScrollRigState } from '../hooks/useScrollRig'

interface IUseCanvas {
  children: ReactNode | ((props: ScrollRigState) => ReactNode)
  id?: string // persistent layout id
  dispose?: boolean // dispose on unmount
  [key: string]: any // Any props to reactively tunnel to the child
}

const UseCanvas = forwardRef(({ children, id, dispose = true, ...props }: IUseCanvas, ref) => {
  if (!children) return null
  // auto update canvas with all props
  useCanvas(children, { ...props, id, ref }, { key: id, dispose })
  return null
})

export { UseCanvas }
```

## File: `src/components/ViewportScrollScene.tsx`
```tsx
import React, { useEffect, useState, useCallback, MutableRefObject, ReactNode } from 'react'
import { Scene } from 'three'
import { useFrame, createPortal, useThree } from '@react-three/fiber'

import { useLayoutEffect } from '../hooks/useIsomorphicLayoutEffect'
import { config } from '../config'
import { useScrollRig } from '../hooks/useScrollRig'
import { DebugMesh } from './DebugMesh'
import { useTracker } from '../hooks/useTracker'
import type { Tracker } from '../hooks/useTrackerTypes'
import { PerspectiveCamera } from './PerspectiveCamera'
import { OrthographicCamera } from './OrthographicCamera'
import type { ScrollState } from '../hooks/useTrackerTypes'

interface IViewportScrollScene {
  track: MutableRefObject<HTMLElement>
  children: (state: ViewportScrollSceneChildProps) => ReactNode
  margin?: number
  inViewportMargin?: string
  inViewportThreshold?: number
  visible?: boolean
  hideOffscreen?: boolean
  debug?: boolean
  orthographic?: boolean
  priority?: number
  hud?: boolean // clear depth to render on top
  camera?: any
}

export interface ViewportScrollSceneChildProps {
  track: MutableRefObject<HTMLElement>
  margin: number
  priority: number
  scale: vec3
  scrollState: ScrollState
  inViewport: boolean
}

/**
 * Generic THREE.js Scene that tracks the dimensions and position of a DOM element while scrolling
 * Scene is rendered into a GL viewport matching the DOM position for better performance
 *
 * Adapted to @react-three/fiber from https://threejsfundamentals.org/threejs/lessons/threejs-multiple-scenes.html
 * @author david@14islands.com
 */
const Viewport = ({
  track,
  children,
  margin = 0, // Margin outside viewport to avoid clipping vertex displacement (px)
  visible = true,
  hideOffscreen = true,
  debug = false,
  orthographic = false,
  priority = config.PRIORITY_VIEWPORTS,
  inViewport,
  bounds,
  scale,
  scrollState,
  camera,
  hud,
  position, // pick out in order to not pass down to child (should be safe to spread props on child)
  rect, // pick out in order to not pass down to child (should be safe to spread props on child)
  ...props
}: IViewportScrollScene & Tracker) => {
  const scene = useThree((s) => s.scene)
  const get = useThree((state) => state.get)
  const setEvents = useThree((state) => state.setEvents)

  const { renderViewport } = useScrollRig()

  // Hide scene when outside of viewport if `hideOffscreen` or set to `visible` prop
  useLayoutEffect(() => {
    scene.visible = hideOffscreen ? inViewport && visible : visible
  }, [inViewport, hideOffscreen, visible])

  // From: https://github.com/pmndrs/drei/blob/d22fe0f58fd596c7bfb60a7a543cf6c80da87624/src/web/View.tsx#L80
  useEffect(() => {
    // Connect the event layer to the tracking element
    const old = get().events.connected
    setEvents({ connected: track.current })
    return () => setEvents({ connected: old })
  }, [])

  // RENDER FRAME
  useFrame(({ gl, scene, camera }) => {
    // Render scene to viewport using local camera and limit updates using scissor test
    if (scene.visible) {
      renderViewport({
        gl,
        scene,
        camera,
        left: bounds.left - margin,
        top: bounds.positiveYUpBottom - margin,
        width: bounds.width + margin * 2,
        height: bounds.height + margin * 2,
        clearDepth: !!hud,
      })
    }
  }, priority)

  return (
    <>
      {!orthographic && <PerspectiveCamera manual margin={margin} makeDefault {...camera} />}
      {orthographic && <OrthographicCamera manual margin={margin} makeDefault {...camera} />}
      {(!children || debug) && scale && <DebugMesh scale={scale} />}
      {children &&
        // scene &&
        scale &&
        children({
          // inherited props
          track,
          margin,
          // tracker props
          scale,
          scrollState,
          inViewport,
          // useFrame render priority (in case children need to run after)
          priority,
          // tunnel the rest
          ...props,
        })}
    </>
  )
}

function ViewportScrollScene({
  track,
  margin = 0, // Margin outside viewport to avoid clipping vertex displacement (px)
  inViewportMargin,
  inViewportThreshold,
  priority,
  ...props
}: IViewportScrollScene) {
  const [scene] = useState(() => new Scene())

  const { bounds, ...trackerProps } = useTracker(track, {
    rootMargin: inViewportMargin,
    threshold: inViewportThreshold,
  })

  // From: https://github.com/pmndrs/drei/blob/d22fe0f58fd596c7bfb60a7a543cf6c80da87624/src/web/View.tsx#L80
  const compute = useCallback(
    (event: any, state: any) => {
      // limit events to DOM element bounds
      if (track.current && event.target === track.current) {
        const { width, height, left, top } = bounds
        const mWidth = width + margin * 2
        const mHeight = height + margin * 2
        const x = event.clientX - left + margin
        const y = event.clientY - top + margin
        state.pointer.set((x / mWidth) * 2 - 1, -(y / mHeight) * 2 + 1)
        state.raycaster.setFromCamera(state.pointer, state.camera)
      }
    },
    [bounds]
  )

  return (
    bounds &&
    createPortal(
      <Viewport track={track} bounds={bounds} priority={priority} margin={margin} {...props} {...trackerProps} />,
      scene,
      // @ts-ignore
      { events: { compute, priority }, size: { width: bounds.width, height: bounds.height } }
    )
  )
}

export { ViewportScrollScene }
```

## File: `src/hooks/useCanvas.ts`
```typescript
import { useEffect, useMemo, useCallback, ReactNode } from 'react'
import { MathUtils } from 'three'

import { useCanvasStore } from '../store'
import { useLayoutEffect } from '../hooks/useIsomorphicLayoutEffect'

import { ScrollRigState } from '../hooks/useScrollRig'
/**
 * Adds THREE.js object to the GlobalCanvas while the component is mounted
 * @param {object} object THREE.js object3d
 */
function useCanvas(
  object: ReactNode | ((props: ScrollRigState) => ReactNode),
  props: any = {},
  { key, dispose = true }: { key?: string; dispose?: boolean } = {}
) {
  const updateCanvas = useCanvasStore((state) => state.updateCanvas)
  const renderToCanvas = useCanvasStore((state) => state.renderToCanvas)
  const removeFromCanvas = useCanvasStore((state) => state.removeFromCanvas)

  // auto generate uuid v4 key
  const uniqueKey = useMemo(() => key || MathUtils.generateUUID(), [])

  // render to canvas if not mounted already
  useLayoutEffect(() => {
    renderToCanvas(uniqueKey, object, { ...props, inactive: false })
  }, [uniqueKey])

  // remove from canvas if no usage (after render so new users have time to register)
  useEffect(() => {
    return () => {
      removeFromCanvas(uniqueKey, dispose)
    }
  }, [uniqueKey])

  // return function that can set new props on the canvas component
  const set = useCallback(
    (props: any) => {
      updateCanvas(uniqueKey, props)
    },
    [updateCanvas, uniqueKey]
  )

  // auto update props when they change
  useEffect(() => {
    set(props)
  }, [...Object.values(props)])

  return set
}

export { useCanvas }
```

## File: `src/hooks/useImageAsTexture.ts`
```typescript
import { useEffect, RefObject, useMemo, useState } from 'react'
import { useThree, useLoader } from '@react-three/fiber'
import { Texture, CanvasTexture, ImageBitmapLoader, TextureLoader, DefaultLoadingManager } from 'three'
import { suspend } from 'suspend-react'
import supportsWebP from 'supports-webp'
import equal from 'fast-deep-equal'

import { useWindowSize } from './useWindowSize'
import { useCanvasStore } from '../store'

/**
 *  Create Threejs Texture from DOM image tag
 *
 *  - Supports <picture> and `srcset` - uses `currentSrc` to get the responsive image source
 *
 *  - Supports lazy-loading image - suspends until first load event. Warning: the GPU upload can cause jank
 *
 *  - Relies on browser cache to avoid loading image twice. We let the <img> tag load the image and suspend until it's ready.
 *
 *  - NOTE: You must add the `crossOrigin` attribute
 *     <img src="" alt="" crossOrigin="anonymous"/>
 */

let hasWebpSupport: boolean = false
// this test is fast - "should" run before first image is requested
supportsWebP.then((supported) => {
  hasWebpSupport = supported
})

function useTextureLoader() {
  // Use an ImageBitmapLoader if imageBitmaps are supported. Moves much of the
  // expensive work of uploading a texture to the GPU off the main thread.
  // Copied from: github.com/mrdoob/three.js/blob/master/examples/jsm/loaders/GLTFLoader.js#L2424
  const isSafari = /^((?!chrome|android).)*safari/i.test(navigator.userAgent) === true
  const isFirefox = navigator.userAgent.indexOf('Firefox') > -1
  // @ts-ignore
  const firefoxVersion = isFirefox ? navigator.userAgent.match(/Firefox\/([0-9]+)\./)[1] : -1
  return typeof createImageBitmap === 'undefined' || isSafari || (isFirefox && Number(firefoxVersion) < 98)
}

function useImageAsTexture(
  imgRef: RefObject<HTMLImageElement>,
  { initTexture = true, premultiplyAlpha = 'default' } = {}
) {
  const gl = useThree((s) => s.gl)
  const size = useWindowSize()
  const debug = useCanvasStore((state) => state.debug)

  // This is a workaround for detecting lazy loading images
  // unfortunately the `loadstart` event is not working everywhere: https://bugs.chromium.org/p/chromium/issues/detail?id=458851
  // So we can't suspend while lazy images are loading - only detect when they finished
  const [newSrcDetected, setNewSrcDetected] = useState(imgRef.current?.currentSrc)
  useEffect(() => {
    const el = imgRef.current
    const onLoad = () => {
      setNewSrcDetected(imgRef.current?.currentSrc)
    }
    el?.addEventListener('load', onLoad)
    return () => el?.removeEventListener('load', onLoad)
  }, [imgRef, newSrcDetected, setNewSrcDetected])

  // suspend until we have currentSrc for this `size`
  const currentSrc = suspend(
    () => {
      DefaultLoadingManager.itemStart('waiting for DOM image')
      return new Promise((resolve) => {
        const el = imgRef.current

        function returnResolve() {
          resolve(el?.currentSrc)
          DefaultLoadingManager.itemEnd('waiting for DOM image')
        }

        // respond to future load event if not cached
        el?.addEventListener('load', returnResolve, { once: true })

        // detect if loaded from browser cache
        if (el?.complete) {
          el?.removeEventListener('load', returnResolve)
          returnResolve()
        }
      })
    },
    [imgRef, size, imgRef.current?.currentSrc, newSrcDetected],
    { equal } // use deep-equal since size ref seems to update on route change
  ) as string

  const LoaderProto = useTextureLoader() ? TextureLoader : ImageBitmapLoader

  // @ts-ignore
  const result: any = useLoader(LoaderProto, currentSrc, (loader) => {
    if (loader instanceof ImageBitmapLoader) {
      loader.setOptions({
        colorSpaceConversion: 'none',
        premultiplyAlpha, // "none" increases blocking time in lighthouse
        imageOrientation: 'flipY',
      })
      // Add webp to Accept header if supported
      // TODO: add check for AVIF
      loader.setRequestHeader({
        Accept: `${hasWebpSupport ? 'image/webp,' : ''}*/*`,
      })
    }
  })

  const texture = useMemo(() => {
    if (result instanceof Texture) {
      return result
    }
    if (result instanceof ImageBitmap) {
      return new CanvasTexture(result)
    }
  }, [result]) as Texture

  // https://github.com/mrdoob/three.js/issues/22696
  // Upload the texture to the GPU immediately instead of waiting for the first render
  useEffect(
    function uploadTextureToGPU() {
      initTexture && gl.initTexture(texture)
      debug && console.log('useImageAsTexture', 'initTexture()')
    },
    [gl, texture, initTexture]
  )

  return texture
}

export { useImageAsTexture }
```

## File: `src/hooks/useIsomorphicLayoutEffect.ts`
```typescript
import { useEffect, useLayoutEffect as vanillaUseLayoutEffect } from 'react'

export const isBrowser = typeof window !== 'undefined'

export const useLayoutEffect = isBrowser ? vanillaUseLayoutEffect : useEffect
```

## File: `src/hooks/useScrollRig.ts`
```typescript
import { useEffect } from 'react'

import { useCanvasStore } from '../store'
import { preloadScene, requestRender, renderScissor, renderViewport } from '../renderer-api'

export interface ScrollRigState {
  debug: boolean
  isCanvasAvailable: boolean
  hasSmoothScrollbar: boolean
  scaleMultiplier: number
  preloadScene: typeof preloadScene
  requestRender: typeof requestRender
  renderScissor: typeof renderScissor
  renderViewport: typeof renderViewport
  reflow: () => void
}

/**
 * Public interface for ScrollRig
 */
export const useScrollRig = () => {
  const isCanvasAvailable = useCanvasStore((state) => state.isCanvasAvailable)
  const hasSmoothScrollbar = useCanvasStore((state) => state.hasSmoothScrollbar)
  const requestReflow = useCanvasStore((state) => state.requestReflow)
  const pageReflow = useCanvasStore((state) => state.pageReflow)
  const debug = useCanvasStore((state) => state.debug)
  const scaleMultiplier = useCanvasStore((state) => state.scaleMultiplier)

  useEffect(() => {
    if (debug) {
      // @ts-ignore
      window._scrollRig = window._scrollRig || {}
      // @ts-ignore
      window._scrollRig.reflow = requestReflow
    }
  }, [])

  return {
    // boolean state
    debug,
    isCanvasAvailable,
    hasSmoothScrollbar,
    // scale
    scaleMultiplier,
    // render API
    preloadScene,
    requestRender,
    renderScissor,
    renderViewport,
    // recalc all tracker positions
    reflow: requestReflow,
    reflowCompleted: pageReflow,
  } as ScrollRigState
}
```

## File: `src/hooks/useTracker.ts`
```typescript
// https://www.typescriptlang.org/brain/knowledge/docs_legacy/handbook/modules.html#ambient-modules
/// <reference path="../types/global.ts" />

import { useRef, useCallback, useEffect, useMemo, useState, MutableRefObject } from 'react'
import { useInView } from 'react-intersection-observer'
import { useWindowSize } from './useWindowSize'
import vecn from 'vecn'

import { useLayoutEffect } from '../hooks/useIsomorphicLayoutEffect'
import { mapLinear } from '../utils/math'
import { useCanvasStore } from '../store'
import { useScrollbar } from '../scrollbar/useScrollbar'
import type { ScrollData } from '../scrollbar/SmoothScrollbarTypes'

import type { Rect, Bounds, TrackerOptions, Tracker, ScrollState, UpdateCallback } from './useTrackerTypes'

function updateBounds(bounds: Bounds, rect: Rect, scroll: ScrollData, size: any) {
  bounds.top = rect.top - (scroll.y || 0)
  bounds.bottom = rect.bottom - (scroll.y || 0)
  bounds.left = rect.left - (scroll.x || 0)
  bounds.right = rect.right - (scroll.x || 0)
  bounds.width = rect.width
  bounds.height = rect.height
  // move coordinate system so 0,0 is at center of screen
  bounds.x = bounds.left + rect.width * 0.5 - size.width * 0.5
  bounds.y = bounds.top + rect.height * 0.5 - size.height * 0.5
  bounds.positiveYUpBottom = size.height - bounds.bottom // inverse Y
}

function updatePosition(position: vec3, bounds: Bounds, scaleMultiplier: number) {
  position.x = bounds.x * scaleMultiplier
  position.y = -1 * bounds.y * scaleMultiplier
}

/**
 * Returns the current Scene position of the DOM element
 * based on initial getBoundingClientRect and scroll delta from start
 */
function useTracker(track: MutableRefObject<HTMLElement>, options?: TrackerOptions): Tracker {
  const size = useWindowSize()
  const { scroll, onScroll } = useScrollbar()
  const scaleMultiplier = useCanvasStore((state) => state.scaleMultiplier)
  const pageReflow = useCanvasStore((state) => state.pageReflow)
  const debug = useCanvasStore((state) => state.debug)

  // extend defaults with optional options
  const { rootMargin, threshold, autoUpdate, wrapper } = useMemo(() => {
    const target = { rootMargin: '0%', threshold: 0, autoUpdate: true } as TrackerOptions
    const opts = options || {}
    Object.keys(opts).map((key: string, index) => {
      if (opts[key] !== undefined) target[key] = opts[key]
    })
    return target
  }, [options])

  // check if element is in viewport
  const { ref, inView: inViewport } = useInView({ rootMargin, threshold })

  // bind useInView ref to current tracking element
  useLayoutEffect(() => {
    ref(track.current)
  }, [track, track?.current])

  // Using state so it's reactive
  const [scale, setScale] = useState<vec3>(vecn.vec3(0, 0, 0))

  // Using ref because
  const scrollState: ScrollState = useRef({
    inViewport: false,
    progress: -1,
    visibility: -1,
    viewport: -1,
  }).current

  // DOM rect (initial position in pixels offset by scroll value on page load)
  // Using ref so we can calculate bounds & position without a re-render
  const rect = useRef({
    top: 0,
    bottom: 0,
    left: 0,
    right: 0,
    width: 0,
    height: 0,
  }).current

  // expose internal ref as a reactive state as well
  const [reactiveRect, setReactiveRect] = useState<Rect>(rect)

  // bounding rect in pixels - updated by scroll
  const bounds = useRef({
    top: 0,
    bottom: 0,
    left: 0,
    right: 0,
    width: 0,
    height: 0,
    x: 0,
    y: 0,
    positiveYUpBottom: 0,
  }).current

  // position in viewport units - updated by scroll
  const position = useRef(vecn.vec3(0, 0, 0)).current

  // Calculate bounding Rect as soon as it's available
  useLayoutEffect(() => {
    const _rect = track.current?.getBoundingClientRect()
    if (!_rect) return
    const initialY = wrapper ? (wrapper as HTMLElement).scrollTop : window.scrollY
    const initialX = wrapper ? (wrapper as HTMLElement).scrollLeft : window.scrollX
    rect.top = _rect.top + initialY
    rect.bottom = _rect.bottom + initialY
    rect.left = _rect.left + initialX
    rect.right = _rect.right + initialX
    rect.width = _rect.width
    rect.height = _rect.height
    setReactiveRect({ ...rect })
    setScale(vecn.vec3(rect?.width * scaleMultiplier, rect?.height * scaleMultiplier, 1))
    debug &&
      console.log(
        'useTracker.getBoundingClientRect:',
        rect,
        'intialScroll:',
        { initialY, initialX },
        'size:',
        size,
        'pageReflow:',
        pageReflow
      )
  }, [track, size, pageReflow, scaleMultiplier, debug])

  const update = useCallback(
    ({ onlyUpdateInViewport = false, scroll: overrideScroll }: UpdateCallback = {}) => {
      if (!track.current || (onlyUpdateInViewport && !scrollState.inViewport)) {
        return
      }

      const _scroll = overrideScroll || scroll

      updateBounds(bounds, rect, _scroll, size)
      updatePosition(position, bounds, scaleMultiplier)

      // scrollState setup based on scroll direction
      const isHorizontal = _scroll.scrollDirection === 'horizontal'
      const sizeProp = isHorizontal ? 'width' : 'height'
      const startProp = isHorizontal ? 'left' : 'top'

      // calculate progress of passing through viewport (0 = just entered, 1 = just exited)
      const pxInside = size[sizeProp] - bounds[startProp]
      scrollState.progress = mapLinear(pxInside, 0, size[sizeProp] + bounds[sizeProp], 0, 1) // percent of total visible distance
      scrollState.visibility = mapLinear(pxInside, 0, bounds[sizeProp], 0, 1) // percent of item height in view
      scrollState.viewport = mapLinear(pxInside, 0, size[sizeProp], 0, 1) // percent of window height scrolled since visible
    },
    [track, size, scaleMultiplier, scroll]
  )

  // update scrollState in viewport
  useLayoutEffect(() => {
    scrollState.inViewport = inViewport
    // update once more in case it went out of view
    update({ onlyUpdateInViewport: false })
    debug && console.log('useTracker.inViewport:', inViewport, 'update()')
  }, [inViewport])

  // re-run if the callback updated
  useLayoutEffect(() => {
    update({ onlyUpdateInViewport: false })
    debug && console.log('useTracker.update on resize/reflow')
  }, [update, pageReflow])

  // auto-update on scroll
  useEffect(() => {
    if (autoUpdate) return onScroll((_scroll) => update({ onlyUpdateInViewport: true }))
  }, [autoUpdate, update, onScroll])

  return {
    // Reactive props
    scale, // reactive scene scale - includes z-axis so it can be spread onto mesh directly
    inViewport, // reactive prop for when inside viewport
    // Non-reactive props (only updates on window resize)
    // Child values are updated on scroll
    rect: reactiveRect, // Dom rect
    bounds, // scrolled bounding rect in pixels
    position, // scrolled element position in viewport units
    scrollState, // scroll progress stats - not reactive
    // Utilities
    update, // optional - manually update tracker
  }
}

export { useTracker }
```

## File: `src/hooks/useTrackerTypes.ts`
```typescript
// https://www.typescriptlang.org/brain/knowledge/docs_legacy/handbook/modules.html#ambient-modules
/// <reference path="../types/global.ts" />
import type { ScrollData } from '../scrollbar/SmoothScrollbarTypes'

export interface ScrollState {
  inViewport: boolean
  progress: number
  visibility: number
  viewport: number
}

export type Rect = {
  top: number
  bottom: number
  left: number
  right: number
  width: number
  height: number
}

export type Bounds = Rect & {
  x: number
  y: number
  positiveYUpBottom: number
}

export interface Tracker {
  rect: Rect
  scale: vec3
  inViewport: boolean
  bounds: Bounds
  scrollState: ScrollState
  position: vec3
  update: (args?: { onlyUpdateInViewport?: boolean; scroll?: any }) => void
}

export interface TrackerOptions {
  rootMargin?: string
  threshold?: number
  autoUpdate?: boolean
  wrapper?: Window | HTMLDivElement
  [key: string]: any
}

export type UpdateCallback = {
  onlyUpdateInViewport?: boolean
  scroll?: ScrollData
}
```

## File: `src/hooks/useWindowSize.ts`
```typescript
import { useState, useEffect } from 'react'
import { ResizeObserver as Polyfill } from '@juggle/resize-observer'
import pkg from 'debounce'

const isBrowser = typeof window !== 'undefined'
export interface WindowSize {
  width: number
  height: number
}

type ConfigProps = {
  debounce?: number
}

/*
 * Triggers a resize only if the Canvas DOM element changed dimensions - not on window resize event
 *
 * This is to avoid costly re-renders when the URL bar is scrolled away on mobile
 *
 * Based on: https://usehooks.com/useWindowSize/
 */

export function useWindowSize({ debounce = 0 }: ConfigProps = {}) {
  // Initialize state with undefined width/height so server and client renders match
  // Learn more here: https://joshwcomeau.com/react/the-perils-of-rehydration/
  const [windowSize, setWindowSize] = useState<WindowSize>({
    width: isBrowser ? window.innerWidth : Infinity,
    height: isBrowser ? window.innerHeight : Infinity,
  })

  useEffect(() => {
    // check if we can find a canvas - if so, base size on canvas instead of window
    // since 100vh !== window.innerHeight on mobile
    const canvasEl = document.getElementById('ScrollRig-canvas')

    // Handler to call on window resize
    function handleResize() {
      const width = canvasEl ? canvasEl.clientWidth : window.innerWidth
      const height = canvasEl ? canvasEl.clientHeight : window.innerHeight

      if (width !== windowSize.width || height !== windowSize.height) {
        // Set window width/height to state
        setWindowSize({
          width,
          height,
        })
      }
    }

    const debouncedResize = pkg.debounce(handleResize, debounce)

    // Add event listener
    const ResizeObserver = window.ResizeObserver || Polyfill
    let observer: ResizeObserver
    if (canvasEl) {
      observer = new ResizeObserver(debouncedResize)
      observer.observe(canvasEl)
    } else {
      window.addEventListener('resize', debouncedResize)
    }
    // Call handler right away so state gets updated with initial window size
    handleResize()
    // Remove event listener on cleanup
    return () => {
      window.removeEventListener('resize', debouncedResize)
      observer?.disconnect()
    }
  }, [windowSize, setWindowSize])

  return windowSize
}
```

## File: `src/polyfills/requestIdleCallback.ts`
```typescript
/**
 * runtime check for requestIdleCallback
 */
export const requestIdleCallback = (callback: () => void, { timeout = 100 } = {}) => {
  if ('requestIdleCallback' in window) {
    window.requestIdleCallback(callback, { timeout })
  } else {
    setTimeout(callback, 0)
  }
}

export const cancelIdleCallback = (id: any) => {
  if ('cancelIdleCallback' in window) {
    window.cancelIdleCallback(id)
  } else {
    clearTimeout(id)
  }
}
```

## File: `src/scrollbar/SmoothScrollbar.tsx`
```tsx
import { useEffect, useRef, useCallback, forwardRef, useImperativeHandle } from 'react'
import Lenis, { ScrollCallback, VirtualScrollCallback } from 'lenis'

import { useLayoutEffect } from '../hooks/useIsomorphicLayoutEffect'
import { useCanvasStore } from '../store'
import { ISmoothScrollbar, ScrollToTarget, ScrollToConfig } from './SmoothScrollbarTypes'

const POINTER_EVENTS_ENABLE_VELOCITY = 1
const POINTER_EVENTS_DISABLE_VELOCITY = 1.5

const SmoothScrollbarImpl = (
  {
    children,
    enabled = true,
    locked = false,
    scrollRestoration = 'auto',
    disablePointerOnScroll = true,
    horizontal = false,
    scrollInContainer = false,
    updateGlobalState = true,
    onScroll,
    config = {},
    invalidate = () => {},
    addEffect,
  }: ISmoothScrollbar,
  ref: any
) => {
  const lenis = useRef<Lenis>()
  const preventPointer = useRef(false)
  const globalScrollState = useCanvasStore((s) => s.scroll)

  // Expose lenis imperative API
  useImperativeHandle(ref, () => ({
    start: () => lenis.current?.start(),
    stop: () => lenis.current?.stop(),
    on: (event: 'scroll' | 'virtual-scroll', cb: ScrollCallback | VirtualScrollCallback) =>
      // @ts-ignore
      lenis.current?.on(event, cb),
    scrollTo: (target: ScrollToTarget, props: ScrollToConfig) => lenis.current?.scrollTo(target, props),
    raf: (time: number) => lenis.current?.raf(time),
    __lenis: lenis.current,
  }))

  // disable pointer events while scrolling to avoid slow event handlers
  const preventPointerEvents = useCallback(
    (prevent: boolean) => {
      if (!disablePointerOnScroll) return
      if (preventPointer.current !== prevent) {
        preventPointer.current = prevent
        document.documentElement.style.pointerEvents = prevent ? 'none' : 'auto'
      }
    },
    [disablePointerOnScroll, preventPointer]
  )

  // apply chosen scroll restoration
  useLayoutEffect(() => {
    if ('scrollRestoration' in window.history) {
      window.history.scrollRestoration = scrollRestoration
    }
  }, [])

  // INIT LENIS
  useLayoutEffect(() => {
    // Set up scroll containers - allows scrolling without resizing window on iOS/mobile
    const html = document.documentElement
    const wrapper = document.body
    const content = document.body.firstElementChild

    html.classList.toggle('ScrollRig-scrollHtml', scrollInContainer)
    wrapper.classList.toggle('ScrollRig-scrollWrapper', scrollInContainer)

    if (scrollInContainer) {
      Object.assign(config, {
        smoothTouch: true,
        wrapper,
        content,
      })
    }

    lenis.current = new Lenis({
      orientation: horizontal ? 'horizontal' : 'vertical',
      ...config,
      // override and disable all smooth settings if scrollbar is disabled
      ...(!enabled ? { smoothWheel: false, syncTouch: false, smoothTouch: false } : {}),
    })

    // let r3f drive the frameloop
    let removeEffect: () => void
    if (addEffect) {
      removeEffect = addEffect((time: number) => lenis.current?.raf(time))
    } else {
      // manual animation frame
      // TODO use framer motion / popmotion render loop?
      let _raf: number
      function raf(time: number) {
        lenis.current?.raf(time)
        _raf = requestAnimationFrame(raf)
      }
      _raf = requestAnimationFrame(raf)
      removeEffect = () => cancelAnimationFrame(_raf)
    }

    return () => {
      removeEffect()
      lenis.current?.destroy()
    }
  }, [enabled])

  // BIND TO LENIS SCROLL EVENT
  useLayoutEffect(() => {
    const _lenis = lenis.current
    const _onScroll = ({ scroll, limit, velocity, direction, progress }: any) => {
      const y = !horizontal ? scroll : 0
      const x = horizontal ? scroll : 0

      // update global scroll store
      if (updateGlobalState) {
        globalScrollState.y = y
        globalScrollState.x = x
        globalScrollState.limit = limit
        globalScrollState.velocity = velocity
        globalScrollState.direction = direction
        globalScrollState.progress = progress || 0 // avoid NaN from Lenis
      }

      if (Math.abs(velocity) > POINTER_EVENTS_DISABLE_VELOCITY) {
        preventPointerEvents(true)
      }
      if (Math.abs(velocity) < POINTER_EVENTS_ENABLE_VELOCITY) {
        preventPointerEvents(false)
      }

      onScroll && onScroll({ scroll, limit, velocity, direction, progress })

      invalidate() // demand a R3F frame on scroll
    }

    _lenis?.on('scroll', _onScroll)

    // update global state
    if (updateGlobalState) {
      globalScrollState.scrollDirection = horizontal ? 'horizontal' : 'vertical'

      // expose global scrollTo and onScroll function to subscribe to scroll events
      useCanvasStore.setState({
        __lenis: _lenis,
        scrollTo: (...args) => {
          _lenis?.scrollTo(...args)
        },
        onScroll: (cb: ScrollCallback) => {
          _lenis?.on('scroll', cb)
          // @ts-ignore
          _lenis?.emit() // send current scroll to new subscriber
          return () => _lenis?.off('scroll', cb)
        },
      })

      // Set current scroll position on load in case reloaded further down
      useCanvasStore.getState().scroll.y = window.scrollY
      useCanvasStore.getState().scroll.x = window.scrollX
    }

    // fire our internal scroll callback to update globalState
    // @ts-ignore
    _lenis?.emit()
    return () => {
      _lenis?.off('scroll', _onScroll)
      // reset global store
      if (updateGlobalState)
        useCanvasStore.setState({
          __lenis: undefined,
          onScroll: () => () => {},
          scrollTo: () => {},
        })
    }
  }, [enabled])

  // Interaction events - invalidate R3F loop and enable pointer events
  useLayoutEffect(() => {
    const invalidateOnWheelEvent = () => invalidate()
    const onPointerInteraction = () => preventPointerEvents(false)
    window.addEventListener('pointermove', onPointerInteraction)
    window.addEventListener('pointerdown', onPointerInteraction)
    window.addEventListener('wheel', invalidateOnWheelEvent)
    return () => {
      window.removeEventListener('pointermove', onPointerInteraction)
      window.removeEventListener('pointerdown', onPointerInteraction)
      window.removeEventListener('wheel', invalidateOnWheelEvent)
    }
  }, [])

  // Mark as enabled in global state
  useEffect(() => {
    if (updateGlobalState) {
      document.documentElement.classList.toggle('js-smooth-scrollbar-enabled', enabled)
      document.documentElement.classList.toggle('js-smooth-scrollbar-disabled', !enabled)
      useCanvasStore.setState({ hasSmoothScrollbar: enabled })
    }
    return () => {
      // cleanup
      document.documentElement.classList.remove('js-smooth-scrollbar-enabled')
      document.documentElement.classList.remove('js-smooth-scrollbar-disabled')
    }
  }, [enabled])

  useEffect(() => {
    locked ? lenis.current?.stop() : lenis.current?.start()
  }, [locked])

  {
    /* Use function child so we can spread props
    - for instance disable pointer events while scrolling */
  }
  return children ? children({}) : null
}

export const SmoothScrollbar = forwardRef<any, ISmoothScrollbar>(SmoothScrollbarImpl)
```

## File: `src/scrollbar/SmoothScrollbarTypes.ts`
```typescript
import { ReactElement } from 'react'

export type ScrollCallback = (props: {
  scroll: number
  limit: number
  velocity: number
  direction: number
  progress: number
}) => void

export interface ScrollData {
  y: number
  x: number
  limit: number
  velocity: number
  progress: number
  direction: number
  scrollDirection?: string
}

export type ScrollToTarget = number | HTMLElement | string
export type ScrollToConfig = {
  offset: number
  immediate: boolean
  duration: number
  easing: (t: number) => number
}

export interface ISmoothScrollbar {
  children?: (props: any) => ReactElement
  enabled?: boolean
  locked?: boolean
  scrollRestoration?: ScrollRestoration
  disablePointerOnScroll?: boolean
  horizontal?: boolean
  scrollInContainer?: boolean
  updateGlobalState?: boolean
  onScroll?: ScrollCallback
  config?: object
  invalidate?: () => void
  addEffect?: (cb: any) => () => void
}
```

## File: `src/scrollbar/index.ts`
```typescript
export { useScrollbar } from './useScrollbar'
export { SmoothScrollbar } from './SmoothScrollbar'
export { useTracker } from '../hooks/useTracker'
```

## File: `src/scrollbar/useScrollbar.ts`
```typescript
import { useCanvasStore } from '../store'

/**
 * Public interface for ScrollRig
 */
export const useScrollbar = () => {
  const enabled = useCanvasStore((state) => state.hasSmoothScrollbar)
  const scroll = useCanvasStore((state) => state.scroll)
  const scrollTo = useCanvasStore((state) => state.scrollTo)
  const onScroll = useCanvasStore((state) => state.onScroll)
  const __lenis = useCanvasStore((state) => state.__lenis)

  return {
    enabled,
    scroll,
    scrollTo,
    onScroll,
    __lenis,
  }
}
```

## File: `src/styles/index.css`
```css
/* Use this to hide stuff when canvas is active */
.ScrollRig-visibilityHidden {
  visibility: hidden;
}
.js-global-canvas-error .ScrollRig-visibilityHidden {
  visibility: unset;
}

/* Use this to hide text but keep it selectable  */
.ScrollRig-transparentColor {
  color: transparent;
}
.js-global-canvas-error .ScrollRig-transparentColor {
  color: unset;
}

/* Show if smooth scrollbar disabled */
.js-smooth-scrollbar-disabled .ScrollRig-hiddenIfSmooth {
  visibility: unset !important;
  color: unset !important;
}

/* Used on scroll wrapper */
.ScrollRig-scrollHtml {
  overflow: hidden;
  height: 100%;
}
.ScrollRig-scrollWrapper {
  height: 100%;
  overflow-y: scroll;
}
```

## File: `src/types/global.ts`
```typescript
declare type vec2 = {
  x: number
  y: number
  xy: vec2
  yx: vec2
  times: (n: number) => vec2
  div: (n: number) => vec2
  max: () => number
  min: () => number
  sum: () => number
} & [x: number, y: number]

declare type vec3 = {
  x: number
  y: number
  z: number
  xy: vec2
  yx: vec2
  xyz: vec3
  xzy: vec3
  yxz: vec3
  yzx: vec3
  zxy: vec3
  zyx: vec3
  times: (n: number) => vec3
  div: (n: number) => vec3
  max: () => number
  min: () => number
  sum: () => number
} & [x: number, y: number, z: number]

declare module 'vecn' {
  export function vec2(x: number, y: number): vec2
  export function vec3(x: number, y: number, z: number): vec3
}
```

## File: `src/utils/helpers.ts`
```typescript
import { Object3D } from 'three'

type CulledObject = {
  wasFrustumCulled?: boolean
  wasVisible?: boolean
} & Object3D

// Use to override Frustum temporarily to pre-upload textures to GPU
export function setAllCulled(obj: CulledObject, overrideCulled: boolean) {
  if (!obj) return
  if (overrideCulled === false) {
    obj.wasFrustumCulled = obj.frustumCulled
    obj.wasVisible = obj.visible
    obj.visible = true
    obj.frustumCulled = false
  } else {
    obj.visible = !!obj.wasVisible
    obj.frustumCulled = !!obj.wasFrustumCulled
  }
  obj.children.forEach((child) => setAllCulled(child, overrideCulled))
}
```

## File: `src/utils/math.ts`
```typescript
// Linear mapping from range <a1, a2> to range <b1, b2>
export function mapLinear(x: number, a1: number, a2: number, b1: number, b2: number) {
  return b1 + ((x - a1) * (b2 - b1)) / (a2 - a1)
}
```


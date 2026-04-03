---
id: 14islands-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:37.872350
---

# KNOWLEDGE EXTRACT: 14islands
> **Extracted on:** 2026-03-30 17:29:00
> **Source:** 14islands

---

## File: `r3f-scroll-rig.md`
```markdown
# 📦 14islands/r3f-scroll-rig [🔖 PENDING/APPROVE]
🔗 https://github.com/14islands/r3f-scroll-rig


## Meta
- **Stars:** ⭐ 921 | **Forks:** 🍴 47
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A react-three-fiber scroll-rig for syncing 3D meshes and DOM elements.

## README (trích đầu)
```
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


```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


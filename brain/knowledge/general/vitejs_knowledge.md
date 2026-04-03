---
id: vitejs-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:41.318554
---

# KNOWLEDGE EXTRACT: vitejs
> **Extracted on:** 2026-03-30 17:58:10
> **Source:** vitejs

---

## File: `vite-plugin-react.md`
```markdown
# 📦 vitejs/vite-plugin-react [🔖 PENDING/APPROVE]
🔗 https://github.com/vitejs/vite-plugin-react


## Meta
- **Stars:** ⭐ 1049 | **Forks:** 🍴 238
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
The all-in-one Vite plugin for React projects.

## README (trích đầu)
```
<p align="center">
  <br>
  <br>
  <a href="https://vite.dev" target="_blank" rel="noopener noreferrer">
    <picture >
      <source media="(prefers-color-scheme: dark)" srcset="https://vite.dev/vite-light.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://vite.dev/vite-dark.svg">
      <img alt="vite logo" src="https://vite.dev/vite-dark.svg" height="60">
    </picture>
  </a>
  <br>
  <br>
</p>
<br/>
<p align="center">
  <a href="https://nodejs.org/en/about/releases/"><img src="https://img.shields.io/node/v/vite.svg" alt="node compatibility"></a>
  <a href="https://github.com/vitejs/vite-plugin-react/actions/workflows/ci.yml"><img src="https://github.com/vitejs/vite-plugin-react/actions/workflows/ci.yml/badge.svg?branch=main" alt="build status"></a>
  <a href="https://chat.vite.dev"><img src="https://img.shields.io/badge/chat-discord-blue?style=flat&logo=discord" alt="discord chat"></a>
</p>
<br/>

# Vite Plugin React

See [`@vitejs/plugin-react` documentation](packages/plugin-react/README.md) and [`@vitejs/plugin-react-swc` documentation](packages/plugin-react-swc/README.md)

# Vite Plugin RSC

See [`@vitejs/plugin-rsc` documentation](packages/plugin-rsc/README.md)

## Packages

| Package                                               | Version (click for changelogs)                                                                                                             |
| ----------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| [@vitejs/plugin-react](packages/plugin-react)         | [![plugin-react version](https://img.shields.io/npm/v/@vitejs/plugin-react.svg?label=%20)](packages/plugin-react/CHANGELOG.md)             |
| [@vitejs/plugin-react-swc](packages/plugin-react-swc) | [![plugin-react-swc version](https://img.shields.io/npm/v/@vitejs/plugin-react-swc.svg?label=%20)](packages/plugin-react-swc/CHANGELOG.md) |
| [@vitejs/plugin-rsc](packages/plugin-rsc)             | [![plugin-rsc version](https://img.shields.io/npm/v/@vitejs/plugin-rsc.svg?label=%20)](packages/plugin-rsc/CHANGELOG.md)                   |
| [@vitejs/plugin-react-oxc](packages/plugin-react-oxc) | [Deprecated](packages/plugin-react-oxc/CHANGELOG.md), merged with [`@vitejs/plugin-react`](packages/plugin-react)                          |

## License

[MIT](LICENSE).

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `vite.md`
```markdown
# 📦 vitejs/vite [🔖 PENDING]
🔗 https://github.com/vitejs/vite
🌐 http://vite.dev

## Meta
- **Stars:** ⭐ 79378 | **Forks:** 🍴 7965
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING

## Description:
Next generation frontend tooling. It's fast!

## README (trích đầu)
```
<p align="center">
  <br>
  <br>
  <a href="https://vite.dev" target="_blank" rel="noopener noreferrer">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://vite.dev/vite-light.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://vite.dev/vite-dark.svg">
      <img alt="vite logo" src="https://vite.dev/vite-dark.svg" height="60">
    </picture>
  </a>
  <br>
  <br>
</p>
<br/>
<p align="center">
  <a href="https://npmjs.com/package/vite"><img src="https://img.shields.io/npm/v/vite.svg" alt="npm package"></a>
  <a href="https://nodejs.org/en/about/previous-releases"><img src="https://img.shields.io/node/v/vite.svg" alt="node compatibility"></a>
  <a href="https://github.com/vitejs/vite/actions/workflows/ci.yml"><img src="https://github.com/vitejs/vite/actions/workflows/ci.yml/badge.svg?branch=main" alt="build status"></a>
  <a href="https://docs.warp.dev/support-and-community/community/open-source-partnership"><img src="https://img.shields.io/badge/Oz%20agents-triaging%20issues-white?logo=warp" alt="issue triage powered by Oz"></a>
  <a href="https://chat.vite.dev"><img src="https://img.shields.io/badge/chat-discord-blue?style=flat&logo=discord" alt="discord chat"></a>
</p>
<br/>

# Vite ⚡

> Next Generation Frontend Tooling

- 💡 Instant Server Start
- ⚡️ Lightning Fast HMR
- 🛠️ Rich Features
- 📦 Optimized Build
- 🔩 Universal Plugin Interface
- 🔑 Fully Typed APIs

Vite (French word for "quick", pronounced [`/viːt/`](https://cdn.jsdelivr.net/gh/vitejs/vite@main/docs/public/vite.mp3), like "veet") is a new breed of frontend build tooling that significantly improves the frontend development experience. It consists of two major parts:

- A dev server that serves your source files over [native ES modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules), with [rich built-in features](https://vite.dev/guide/features.html) and astonishingly fast [Hot Module Replacement (HMR)](https://vite.dev/guide/features.html#hot-module-replacement).

- A [build command](https://vite.dev/guide/build.html) that bundles your code with [Rollup](https://rollupjs.org), pre-configured to output highly optimized static assets for production.

In addition, Vite is highly extensible via its [Plugin API](https://vite.dev/guide/api-plugin.html) and [JavaScript API](https://vite.dev/guide/api-javascript.html) with full typing support.

[Read the Docs to Learn More](https://vite.dev).

## Packages

| Package                                         | Version (click for changelogs)                                                                                                    |
| ----------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| [vite](packages/vite)                           | [![vite version](https://img.shields.io/npm/v/vite.svg?label=%20)](packages/vite/CHANGELOG.md)        
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


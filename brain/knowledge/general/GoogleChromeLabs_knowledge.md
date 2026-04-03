---
id: googlechromelabs-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:48.848417
---

# KNOWLEDGE EXTRACT: GoogleChromeLabs
> **Extracted on:** 2026-03-30 17:38:00
> **Source:** GoogleChromeLabs

---

## File: `comlink.md`
```markdown
# 📦 GoogleChromeLabs/comlink [🔖 PENDING/APPROVE]
🔗 https://github.com/GoogleChromeLabs/comlink


## Meta
- **Stars:** ⭐ 12603 | **Forks:** 🍴 422
- **Language:** TypeScript | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Comlink makes WebWorkers enjoyable.

## README (trích đầu)
```
# Comlink

Comlink makes [WebWorkers][webworker] enjoyable. Comlink is a **tiny library (1.1kB)**, that removes the mental barrier of thinking about `postMessage` and hides the fact that you are working with workers.

At a more abstract level it is an RPC implementation for `postMessage` and [ES6 Proxies][es6 proxy].

```
$ npm install --save comlink
```

![Comlink in action](https://user-images.githubusercontent.com/234957/54164510-cdab2d80-4454-11e9-92d0-7356aa6c5746.png)

## Browsers support & bundle size

![Chrome 56+](https://img.shields.io/badge/Chrome-56+-green.svg?style=flat-square)
![Edge 15+](https://img.shields.io/badge/Edge-15+-green.svg?style=flat-square)
![Firefox 52+](https://img.shields.io/badge/Firefox-52+-green.svg?style=flat-square)
![Opera 43+](https://img.shields.io/badge/Opera-43+-green.svg?style=flat-square)
![Safari 10.1+](https://img.shields.io/badge/Safari-10.1+-green.svg?style=flat-square)
![Samsung Internet 6.0+](https://img.shields.io/badge/Samsung_Internet-6.0+-green.svg?style=flat-square)

Browsers without [ES6 Proxy] support can use the [proxy-polyfill].

**Size**: ~2.5k, ~1.2k gzip’d, ~1.1k brotli’d

## Introduction

On mobile phones, and especially on low-end mobile phones, it is important to keep the main thread as idle as possible so it can respond to user interactions quickly and provide a jank-free experience. **The UI thread ought to be for UI work only**. WebWorkers are a web API that allow you to run code in a separate thread. To communicate with another thread, WebWorkers offer the `postMessage` API. You can send JavaScript objects as messages using `myWorker.postMessage(someObject)`, triggering a `message` event inside the worker.

Comlink turns this messaged-based API into a something more developer-friendly by providing an RPC implementation: Values from one thread can be used within the other thread (and vice versa) just like local values.

## Examples

### [Running a simple function](./docs/examples/01-simple-example)

**main.js**

```javascript
import * as Comlink from "https://unpkg.com/comlink/dist/esm/comlink.mjs";
async function init() {
  const worker = new Worker("worker.js");
  // WebWorkers use `postMessage` and therefore work with Comlink.
  const obj = Comlink.wrap(worker);
  alert(`Counter: ${await obj.counter}`);
  await obj.inc();
  alert(`Counter: ${await obj.counter}`);
}
init();
```

**worker.js**

```javascript
importScripts("https://unpkg.com/comlink/dist/umd/comlink.js");
// importScripts("../../../dist/umd/comlink.js");

const obj = {
  counter: 0,
  inc() {
    this.counter++;
  },
};

Comlink.expose(obj);
```

### [Callbacks](./docs/examples/02-callback-example)

**main.js**

```javascript
import * as Comlink from "https://unpkg.com/comlink/dist/esm/comlink.mjs";
// import * as Comlink from "../../../dist/esm/comlink.mjs";
function callback(value) {
  alert(`Result: ${value}`);
}
async function init() {
  const remoteFunction = Comlink.wrap(new Worker("worker.js"));
  await rem
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


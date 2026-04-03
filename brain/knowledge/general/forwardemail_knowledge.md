---
id: forwardemail-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:25.498228
---

# KNOWLEDGE EXTRACT: forwardemail
> **Extracted on:** 2026-03-30 17:37:22
> **Source:** forwardemail

---

## File: `superagent.md`
```markdown
# 📦 forwardemail/superagent [🔖 PENDING/APPROVE]
🔗 https://github.com/forwardemail/superagent
🌐 https://forwardemail.github.io/superagent/

## Meta
- **Stars:** ⭐ 16644 | **Forks:** 🍴 1326
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Ajax for Node.js and browsers (JS HTTP client). Maintained for @forwardemail, @ladjs, @spamscanner, @breejs, @cabinjs, and @lassjs.

## README (trích đầu)
```
# superagent

[![build status](https://github.com/forwardemail/superagent/actions/workflows/ci.yml/badge.svg)](https://github.com/forwardemail/superagent/actions/workflows/ci.yml)
[![code coverage](https://img.shields.io/codecov/c/github/ladjs/superagent.svg)](https://codecov.io/gh/ladjs/superagent)
[![code style](https://img.shields.io/badge/code_style-XO-5ed9c7.svg)](https://github.com/sindresorhus/xo)
[![styled with prettier](https://img.shields.io/badge/styled_with-prettier-ff69b4.svg)](https://github.com/prettier/prettier)
[![made with lass](https://img.shields.io/badge/made_with-lass-95CC28.svg)](https://lass.js.org)
[![license](https://img.shields.io/github/license/ladjs/superagent.svg)](LICENSE)

> Small progressive client-side HTTP request library, and Node.js module with the same API, supporting many high-level HTTP client features.  Maintained for [Forward Email](https://github.com/forwardemail) and [Lad](https://github.com/ladjs).


## Table of Contents

* [Install](#install)
* [Usage](#usage)
  * [Node](#node)
  * [Browser](#browser)
* [Supported Platforms](#supported-platforms)
  * [Required Browser Features](#required-browser-features)
* [Plugins](#plugins)
* [Upgrading from previous versions](#upgrading-from-previous-versions)
* [Contributors](#contributors)
* [License](#license)


## Install

[npm][]:

```sh
npm install superagent
```

[yarn][]:

```sh
yarn add superagent
```


## Usage

### Node

```js
const superagent = require('superagent');

// callback
superagent
  .post('/api/pet')
  .send({ name: 'Manny', species: 'cat' }) // sends a JSON post body
  .set('X-API-Key', 'foobar')
  .set('accept', 'json')
  .end((err, res) => {
    // Calling the end function will send the request
  });

// promise with then/catch
superagent.post('/api/pet').then(console.log).catch(console.error);

// promise with async/await
(async () => {
  try {
    const res = await superagent.post('/api/pet');
    console.log(res);
  } catch (err) {
    console.error(err);
  }
})();
```

### Browser

**The browser-ready, minified version of `superagent` is only 50 KB (minified and gzipped).**

Browser-ready versions of this module are available via [jsdelivr][], [unpkg][], and also in the `node_modules/superagent/dist` folder in downloads of the `superagent` package.

> Note that we also provide unminified versions with `.js` instead of `.min.js` file extensions.

#### VanillaJS

This is the solution for you if you're just using `<script>` tags everywhere!

```html
<script src="https://cdnjs.cloudflare.com/polyfill/v3/polyfill.min.js?features=WeakRef,BigInt"></script>
<script src="https://cdn.jsdelivr.net/npm/superagent"></script>
<!-- if you wish to use unpkg.com instead: -->
<!-- <script src="https://unpkg.com/superagent"></script> -->
<script type="text/javascript">
  (function() {
    // superagent is exposed as `window.superagent`
    // if you wish to use "request" instead please
    // uncomment the following line of code:
    // `window.request =
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `supertest.md`
```markdown
# 📦 forwardemail/supertest [🔖 PENDING/APPROVE]
🔗 https://github.com/forwardemail/supertest


## Meta
- **Stars:** ⭐ 14334 | **Forks:** 🍴 783
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
🕷 Super-agent driven library for testing node.js HTTP servers using a fluent API.   Maintained for @forwardemail, @ladjs, @spamscanner, @breejs, @cabinjs, and @lassjs.

## README (trích đầu)
```
# [supertest](https://forwardemail.github.io/superagent/)

[![build status](https://github.com/forwardemail/supertest/actions/workflows/ci.yml/badge.svg)](https://github.com/forwardemail/supertest/actions/workflows/ci.yml)
[![code coverage](https://img.shields.io/codecov/c/github/ladjs/supertest.svg)](https://codecov.io/gh/ladjs/supertest)
[![code style](https://img.shields.io/badge/code_style-XO-5ed9c7.svg)](https://github.com/sindresorhus/xo)
[![styled with prettier](https://img.shields.io/badge/styled_with-prettier-ff69b4.svg)](https://github.com/prettier/prettier)
[![made with lass](https://img.shields.io/badge/made_with-lass-95CC28.svg)](https://lass.js.org)
[![license](https://img.shields.io/github/license/ladjs/supertest.svg)](LICENSE)

> HTTP assertions made easy via [superagent](http://github.com/ladjs/superagent).  Maintained for [Forward Email](https://github.com/forwardemail) and [Lad](https://github.com/ladjs).

## About

The motivation with this module is to provide a high-level abstraction for testing
HTTP, while still allowing you to drop down to the [lower-level API](https://forwardemail.github.io/superagent/) provided by superagent.

## Getting Started

Install supertest as an npm module and save it to your package.json file as a development dependency:

```bash
npm install supertest --save-dev
```

  Once installed it can now be referenced by simply calling ```require('supertest');```

## Example

You may pass an `http.Server`, or a `Function` to `request()` - if the server is not
already listening for connections then it is bound to an ephemeral port for you so
there is no need to keep track of ports.

supertest works with any test framework, here is an example without using any
test framework at all:

```js
const request = require('supertest');
const express = require('express');

const app = express();

app.get('/user', function(req, res) {
  res.status(200).json({ name: 'john' });
});

request(app)
  .get('/user')
  .expect('Content-Type', /json/)
  .expect('Content-Length', '15')
  .expect(200)
  .end(function(err, res) {
    if (err) throw err;
  });
```

To enable http2 protocol, simply append an options to `request` or `request.agent`:

```js
const request = require('supertest');
const express = require('express');

const app = express();

app.get('/user', function(req, res) {
  res.status(200).json({ name: 'john' });
});

request(app, { http2: true })
  .get('/user')
  .expect('Content-Type', /json/)
  .expect('Content-Length', '15')
  .expect(200)
  .end(function(err, res) {
    if (err) throw err;
  });

request.agent(app, { http2: true })
  .get('/user')
  .expect('Content-Type', /json/)
  .expect('Content-Length', '15')
  .expect(200)
  .end(function(err, res) {
    if (err) throw err;
  });
```

Here's an example with mocha, note how you can pass `done` straight to any of the `.expect()` calls:

```js
describe('GET /user', function() {
  it('responds with json', function(done) {
    request(app)
      .get('/user'
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


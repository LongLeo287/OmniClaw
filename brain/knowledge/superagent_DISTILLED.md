---
id: superagent
type: knowledge
owner: OA_Triage
---
# superagent
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "superagent",
  "description": "elegant & feature rich browser / node HTTP with a fluent API",
  "version": "10.3.0",
  "author": "TJ Holowaychuk <tj@vision-media.ca>",
  "browser": {
    "./src/node/index.js": "./src/client.js",
    "./lib/node/index.js": "./lib/client.js",
    "./test/support/server.js": "./test/support/blank.js"
  },
  "bugs": {
    "url": "https://github.com/ladjs/superagent/issues"
  },
  "contributors": [
    "Kornel Lesiński <kornel@geekhood.net>",
    "Peter Lyons <pete@peterlyons.com>",
    "Hunter Loftis <hunter@hunterloftis.com>",
    "Nick Baugh <niftylettuce@gmail.com>"
  ],
  "dependencies": {
    "component-emitter": "^1.3.1",
    "cookiejar": "^2.1.4",
    "debug": "^4.3.7",
    "fast-safe-stringify": "^2.1.1",
    "form-data": "^4.0.5",
    "formidable": "^3.5.4",
    "methods": "^1.1.2",
    "mime": "2.6.0",
    "qs": "^6.14.1"
  },
  "devDependencies": {
    "@babel/cli": "^7.20.7",
    "@babel/core": "^7.20.12",
    "@babel/plugin-transform-runtime": "^7.19.6",
    "@babel/preset-env": "^7.20.2",
    "@babel/runtime": "^7.20.13",
    "@commitlint/cli": "^19.8.1",
    "@commitlint/config-conventional": "^19.8.1",
    "babelify": "^10.0.0",
    "Base64": "^1.1.0",
    "basic-auth-connect": "^1.0.0",
    "body-parser": "^1.20.4",
    "browserify": "^17.0.0",
    "cookie-parser": "^1.4.7",
    "cross-env": "^7.0.3",
    "eslint": "^8.32.0",
    "eslint-config-xo-lass": "2",
    "eslint-plugin-compat": "4.0.2",
    "eslint-plugin-node": "^11.1.0",
    "express": "^4.18.3",
    "express-session": "^1.17.3",
    "fixpack": "^4.0.0",
    "get-port": "4.2.0",
    "husky": "^9.1.7",
    "lint-staged": "^15.5.2",
    "marked": "^4.2.12",
    "mocha": "^6.2.3",
    "multer": "1.4.5-lts.1",
    "nyc": "^15.1.0",
    "remark-cli": "^11.0.0",
    "remark-preset-github": "4.0.4",
    "rimraf": "3",
    "should": "^13.2.3",
    "should-http": "^0.1.1",
    "tinyify": "3.0.0",
    "xo": "^0.53.1",
    "zuul": "^3.12.0"
  },
  "engines": {
    "node": ">=14.18.0"
  },
  "files": [
    "dist/*.js",
    "lib/**/*.js"
  ],
  "homepage": "https://github.com/ladjs/superagent",
  "jsdelivr": "dist/superagent.min.js",
  "keywords": [
    "agent",
    "ajax",
    "ajax",
    "api",
    "async",
    "await",
    "axios",
    "cancel",
    "client",
    "frisbee",
    "got",
    "http",
    "http",
    "https",
    "ky",
    "promise",
    "promise",
    "promises",
    "request",
    "request",
    "requests",
    "response",
    "rest",
    "retry",
    "super",
    "superagent",
    "timeout",
    "transform",
    "xhr",
    "xmlhttprequest"
  ],
  "license": "MIT",
  "main": "lib/node/index.js",
  "repository": {
    "type": "git",
    "url": "git://github.com/ladjs/superagent.git"
  },
  "scripts": {
    "browserify": "browserify src/node/index.js -o dist/superagent.js -s superagent -g [ babelify --configFile ./.dist.babelrc ]",
    "build": "npm run build:clean && npm run build:lib && npm run build:dist",
    "build:clean": "rimraf lib dist",
    "build:dist": "npm run browserify && npm run minify",
    "build:lib": "babel --config-file ./.lib.babelrc src --out-dir lib",
    "build:test": "babel --config-file ./.test.babelrc test --out-dir lib/node/test",
    "coverage": "nyc report --reporter=text-lcov > coverage.lcov",
    "lint": "eslint -c .eslintrc src test && remark . -qfo && eslint -c .lib.eslintrc lib/**/*.js && eslint -c .dist.eslintrc dist/**/*.js",
    "minify": "cross-env NODE_ENV=production browserify src/node/index.js -o dist/superagent.min.js -s superagent -g [ babelify --configFile ./.dist.babelrc ] -p tinyify",
    "nyc": "cross-env NODE_ENV=test nyc ava",
    "test": "npm run build && npm run lint && make test",
    "test-http2": "npm run build && npm run lint && make test-node-http2",
    "prepare": "husky"
  },
  "unpkg": "dist/superagent.min.js"
}

```

### File: README.md
```md
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
    // `window.request = superagent;`
    superagent
      .post('/api/pet')
      .send({ name: 'Manny', species: 'cat' }) // sends a JSON post body
      .set('X-API-Key', 'foobar')
      .set('accept', 'json')
      .end(function (err, res) {
        // Calling the end function will send the request
      });
  })();
</script>
```

#### Bundler

If you are using [browserify][], [webpack][], [rollup][], or another bundler, then you can follow the same usage as [Node](#node) above.


## Supported Platforms

* Node: v14.18.0+
* Browsers (see [.browserslistrc](.browserslistrc)):

  ```sh
  npx browserslist
  ```

  ```sh
  and_chr 102
  and_ff 101
  and_qq 10.4
  and_uc 12.12
  android 101
  chrome 103
  chrome 102
  chrome 101
  chrome 100
  edge 103
  edge 102
  edge 101
  firefox 101
  firefox 100
  firefox 91
  ios_saf 15.5
  ios_saf 15.4
  ios_saf 15.2-15.3
  ios_saf 15.0-15.1
  ios_saf 14.5-14.8
  ios_saf 14.0-14.4
  ios_saf 12.2-12.5
  kaios 2.5
  op_mini all
  op_mob 64
  opera 86
  opera 85
  safari 15.5
  safari 15.4
  samsung 17.0
  samsung 16.0
  ```

### Required Browser Features

We recommend using <https://cdnjs.cloudflare.com/polyfill/> (specifically with the bundle mentioned in [VanillaJS](#vanillajs) above):

```html
<script src="https://cdnjs.cloudflare.com/polyfill/v3/polyfill.min.js?features=WeakRef,BigInt"></script>
```

* WeakRef is not supported in Opera 85, iOS Safari 12.2-12.5
* BigInt is not supported in iOS Safari 12.2-12.5


## Plugins

SuperAgent is easily extended via plugins.

```js
const nocache = require('superagent-no-cache');
const superagent = require('superagent');
const prefix = require('superagent-prefix')('/static');

superagent
  .get('/some-url')
  .query({ action: 'edit', city: 'London' }) // query string
  .use(prefix) // Prefixes *only* this request
  .use(nocache) // Prevents caching of *only* this request
  .end((err, res) => {
    // Do something
  });
```

Existing plugins:

* [superagent-no-cache](https://github.com/johntron/superagent-no-cache) - prevents caching by including Cache-Control header
* [superagent-prefix](https://github.com/johntron/superagent-prefix) - prefixes absolute URLs (useful in test environment)
* [superagent-suffix](https://github.com/timneutkens1/superagent-suffix) - suffix URLs with a given path
* [superagent-mock](https://github.com/M6Web/superagent-mock) - simulate HTTP calls by returning data fixtures based on the requested URL
* [superagent-mocker](https://github.com/shuvalov-anton/superagent-mocker) — simulate REST API
* [superagent-cache](https://github.com/jpodwys/superagent-cache) - A global SuperAgent patch with built-in, flexible caching
* [superagent-cache-plugin](https://github.com/jpodwys/superagent-cache-plugin) - A SuperAgent plugin with built-in, flexible caching
* [superagent-jsonapify](https://github.com/alex94puchades/superagent-jsonapify) - A lightweight [json-api](http://jsonapi.org/format/) client addon for superagent
* [superagent-serializer](https://github.com/zzarcon/superagent-serializer) - Converts server payload into different cases
* [superagent-httpbackend](https://www.npmjs.com/package/superagent-httpbackend) - stub out requests using AngularJS' $httpBackend syntax
* [superagent-throttle](https://github.com/leviwheatcroft/superagent-throttle) - queues and intelligently throttles requests
* [superagent-charset](https://github.com/magicdawn/superagent-charset) - add charset support for node's SuperAgent
* [superagent-verbose-errors](https://github.com/jcoreio/superagent-verbose-errors) - include response body in error messages for failed requests
* [superagent-declare](https://github.com/damoclark/superagent-declare) - A simple [declarative](https://en.wikipedia.org/wiki/Declarative_programming) API for SuperAgent
* [superagent-node-http-timings](https://github.com/webuniverseio/superagent-node-http-timings) - measure http timings in node.js
* [superagent-cheerio](https://github.com/mmmmmrob/superagent-cheerio) - add [cheerio](https://www.npmjs.com/package/cheerio) to your response content automatically. Adds `res.$` for HTML and XML response bodies.
* [@certible/superagent-aws-sign](https://github.com/certible/superagent-aws-sign) - Sign AWS endpoint requests, it uses the aws4 to authenticate the SuperAgent requests

Please prefix your plugin with `superagent-*` so that it can easily be found by others.

For SuperAgent extensions such as couchdb and oauth visit the [wiki](https://github.com/ladjs/superagent/wiki).


## Upgrading from previous versions

Please see [GitHub releases page](https://github.com/ladjs/superagent/releases) for the current changelog.

Our breaking changes are mostly in rarely used functionality and from stricter error handling.

* [6.0 to 6.1](https://github.com/ladjs/superagent/releases/tag/v6.1.0)
  * Browser behaviour changed to match Node when serializing `application/x-www-form-urlencoded`, using `arrayFormat: 'indices'` semantics of `qs` library. (See: <https://www.npmjs.com/package/qs#stringifying>)
* [5.x to 6.x](https://github.com/ladjs/superagent/releases/tag/v6.0.0):
  * Retry behavior is still opt-in, however we now have a more fine-grained list of status codes and error codes that we retry against (see updated docs)
  * A specific issue with Content-Type matching not being case-insensitive is fixed
  * Set is now required for IE 9, see [Required Browser Features](#required-browser-features) for more insight
* [4.x to 5.x](https://github.com/ladjs/superagent/releases/tag/v5.0.0):
  * We've implemented the build setup of [Lass](https://lass.js.org) to simplify our stack and linting
  * Unminified browserified build size has been reduced from 48KB to 20KB (via `tinyify` and the latest version of Babel using `@babel/preset-env` and `.browserslistrc`)
  * Linting support has been added using `caniuse-lite` and `eslint-plugin-compat`
  * We can now target what versions of Node we wish to support more easily using `.babelrc`
* [3.x to 4.x](https://github.com/ladjs/superagent/releases/tag/v4.0.0-alpha.1):
  * Ensure you're running Node 6 or later. We've dropped support for Node 4.
  * We've started using ES6 and for compatibility with Internet Explorer you may need to use Babel.
  * We suggest migrating from `.end()` callbacks to `.then()` or `await`.
* [2.x to 3.x](https://github.com/ladjs/superagent/releases/tag/v3.0.0):
  * Ensure you're running Node 4 or later. We've dropped support for Node 0.x.
  * Test code that calls `.send()` multiple times. Invalid calls to `.send()` will now throw instead of sending garbage.
* [1.x to 2.x](https://github.com/ladjs/superagent/releases/tag/v2.0.0):
  * If you use `.parse()` in the *browser* version, rename it to `.serialize()`.
  * If you rely on `undefined` in query-string values being sent literally as the text "undefined", switch to checking for missing value instead. `?key=undefined` is now `?key` (without a value).
  * If you use `.then()` in Internet Explorer, ensure that you have a polyfill that adds a global `Promise` object.
* 0.x to 1.x:
  * Instead of 1-argument callback `.end(function(res){})` use `.then(res => {})`.


## Contributors

| Name                |
| ------------------- |
| **Kornel Lesiński** |
| **Peter Lyons**     |
| **Hunter Loftis**   |
| **Nick Baugh**      |


## License

[MIT](LICENSE) © TJ Holowaychuk


##

[npm]: https://www.npmjs.com/

[yarn]: https://yarnpkg.com/

[jsdelivr]: https://www.jsdelivr.com/

[unpkg]: https://unpkg.com/

[browserify]: https://github.com/browserify/browserify

[webpack]: https://github.com/webpack/webpack

[rollup]: https://github.com/rollup/rollup

```

### File: .commitlintrc.js
```js
module.exports = {
  extends: ['@commitlint/config-conventional']
};

```

### File: .lintstagedrc.js
```js
module.exports = {
  "*.md": filenames => filenames.map(filename => `remark ${filename} -qfo`),
  '*.js': 'xo --fix'
};

```

### File: .prettierrc.js
```js
module.exports = {
  singleQuote: true,
  bracketSpacing: true,
  trailingComma: 'none'
};

```

### File: .remarkrc.js
```js
module.exports = {
  plugins: ['preset-github']
};

```

### File: .xo-config.js
```js
module.exports = {
	prettier: true,
	space: true,
	nodeVersion: false,
	extends: [
		'xo-lass',
	],
	envs: [
		'node',
		'browser',
	],
	overrides: [
		{
			files: 'test/**/*.js',
			envs: [
				'mocha',
			],
			rules: {
				'block-scoped-var': 'warn',
				complexity: 'warn',
				'default-case': 'warn',
				eqeqeq: 'warn',
				'func-name-matching': 'warn',
				'func-names': 'warn',
				'guard-for-in': 'warn',
				'handle-callback-err': 'warn',
				'import/no-extraneous-dependencies': 'warn',
				'import/no-unassigned-import': 'warn',
				'import/order': 'warn',
				'max-nested-callbacks': 'warn',
				'new-cap': 'warn',
				'no-eq-null': 'warn',
				'no-extend-native': 'warn',
				'no-implicit-coercion': 'warn',
				'no-multi-assign': 'warn',
				'no-negated-condition': 'off',
				'no-prototype-builtins': 'warn',
				'no-redeclare': 'warn',
				'no-undef': 'warn',
				'no-unused-expressions': 'warn',
				'no-unused-vars': 'warn',
				'no-use-extend-native/no-use-extend-native': 'warn',
				'no-useless-escape': 'warn',
				'no-var': 'warn',
				'no-void': 'warn',
				'n/no-deprecated-api': 'warn',
				'prefer-rest-params': 'warn',
				'prefer-spread': 'warn',
				'unicorn/filename-case': 'warn',
				'valid-jsdoc': 'warn',
				'n/no-path-concat': 'warn',
				'unicorn/no-empty-file': 'warn',
				'unicorn/expiring-todo-comments': 'off',
				'n/prefer-global/buffer': 'off',
				'n/prefer-global/process': 'off',
			},
		},
	],
	rules: {
		'unicorn/prevent-abbreviations': [
			'warn',
			{
				replacements: {
					res: false,
					args: false,
					fn: false,
					err: false,
					e: false,
					i: false,
				},
			},
		],
		'no-bitwise': 'warn',
		'n/prefer-global/buffer': 'off',
		'n/prefer-global/process': 'off',
		'unicorn/no-new-array': 'warn',
		'unicorn/no-this-assignment': 'warn',
		'unicorn/prefer-spread': 'warn',
		'unicorn/catch-error-name': 'warn',
		'unicorn/prefer-code-point': 'warn',
		'n/no-unsupported-features': [
			'error',
			{
				version: 8,
				ignores: [
					'syntax',
				],
			},
		],
    'unicorn/prefer-optional-catch-binding': 'off',
    'no-unused-vars': 'off',
    'unicorn/expiring-todo-comments': 'off'
	},
	globals: [],
};

```

### File: CONTRIBUTING.md
```md
When submitting a PR, your chance of acceptance increases if you do the following:

* Code style is consistent with existing in the file.
* Tests are passing (client and server).
* You add a test for the failing issue you are fixing.
* Code changes are focused on the area of discussion.
* Do not rebuild the distribution files or increment version numbers.

```

### File: HISTORY.md
```md
# This HISTORY log is deprecated

Please see [GitHub releases page](https://github.com/ladjs/superagent/releases) for the current changelog.

# 4.1.0 (2018-12-26)

 * `.connect()` IP/DNS override option (Kornel)
 * `.trustLocalhost()` option for allowing broken HTTPS on `localhost`
 * `.abort()` used with promises rejects the promise.

# 4.0.0 (2018-11-17)

## Breaking changes

* Node.js v4 has reached it's end of life, so we no longer support it. It's v6+ or later. We recommend Node.js 10.
* We now use ES6 in the browser code, too.
  * If you're using Browserify or Webpack to package code for Internet Explorer, you will also have to use Babel.
  * The pre-built node_modules/superagent.js is still ES5-compatible.
* `.end(…)` returns `undefined` instead of the request. If you need the request object after calling `.end()` (and you probably don't), save it in a variable and call `request.end(…)`. Consider not using `.end()` at all, and migrating to promises by calling `.then()` instead.
* In Node, responses with unknown MIME type are buffered by default. To get old behavior, if you use custom _unbuffered_ parsers, add `.buffer(false)` to requests or set `superagent.buffer[yourMimeType] = false`.
* Invalid uses of `.pipe()` throw.


## Minor changes

* Throw if `req.abort().end()` is called
* Throw if using unsupported mix of send and field
* Reject `.end()` promise on all error events (Kornel Lesiński)
* Set `https.servername` from the `Host` header (Kornel Lesiński)
* Leave backticks unencoded in query strings where possible (Ethan Resnick)
* Update node-mime to 2.x (Alexey Kucherenko)
* Allow default buffer settings based on response-type (shrey)
* `response.buffered` is more accurate.

# 3.8.3 (2018-04-29)

* Add flags for 201 & 422 responses (Nikhil Fadnis)
* Emit progress event while uploading Node `Buffer` via send method (Sergey Akhalkov)
* Fixed setting correct cookies for redirects (Damien Clark)
* Replace .catch with ['catch'] for IE9 Support (Miguel Stevens)

# 3.8.2 (2017-12-09)

* Fixed handling of exceptions thrown from callbacks
* Stricter matching of `+json` MIME types.

# 3.8.1 (2017-11-08)

* Clear authorization header on cross-domain redirect

# 3.8.0

* Added support for "globally" defined headers and event handlers via `superagent.agent()`. It now remembers default settings for all its requests.
* Added optional callback to `.retry()` (Alexander Murphy)
* Unified auth args handling in node/browser (Edmundo Alvarez)
* Fixed error handling in zlib pipes (Kornel)
* Documented that 3xx status codes are errors (Mickey Reiss)

# 3.7.0 (2017-10-17)

* Limit maximum response size. Prevents zip bombs (Kornel)
* Catch and pass along errors in `.ok()` callback (Jeremy Ruppel)
* Fixed parsing of XHR headers without a newline (nsf)

# 3.6.2 (2017-10-02)

* Upgrade MIME type dependency to a newer, secure version
* Recognize PDF MIME as binary
* Fix for error in subsequent require() calls (Steven de Salas)

# 3.6.0 (2017-08-20)

* Support disabling TCP_NODELAY option ([#1240](https://github.com/ladjs/superagent/issues/1240)) (xiamengyu)
* Send payload in query string for GET and HEAD shorthand API (Peter Lyons)
* Support passphrase with pfx certificate (Paul Westerdale (ABRS Limited))
* Documentation improvements (Peter Lyons)
* Fixed duplicated query string params ([#1200](https://github.com/ladjs/superagent/issues/1200)) (Kornel)

# 3.5.1 (2017-03-18)

* Allow crossDomain errors to be retried ([#1194](https://github.com/ladjs/superagent/issues/1194)) (Michael Olson)
* Read responseType property from the correct object (Julien Dupouy)
* Check for ownProperty before adding header (Lucas Vieira)

# 3.5.0 (2017-02-23)

* Add errno to distinguish between request timeout and body download timeout ([#1184](https://github.com/ladjs/superagent/issues/1184)) (Kornel Lesiński)
* Warn about bogus timeout options ([#1185](https://github.com/ladjs/superagent/issues/1185)) (Kornel Lesiński)

# 3.4.4 (2017-02-17)

* Treat videos like images (Kornel Lesiński)
* Avoid renaming module (Kornel Lesiński)

# 3.4.3 (2017-02-14)

* Fixed being able to define own parsers when their mime type starts with `text/` (Damien Clark)
* `withCredentials(false)` (Andy Woods)
* Use `formData.on` instead of `.once` (Kornel Lesiński)
* Ignore `attach("file",null)` (Kornel Lesiński)

# 3.4.1 (2017-01-29)

* Allow `retry()` and `retry(0)` (Alexander Pope)
* Allow optional body/data in DELETE requests (Alpha Shuro)
* Fixed query string on retried requests (Kornel Lesiński)

# 3.4.0 (2017-01-25)

* New `.retry(n)` method and `err.retries` (Alexander Pope)
* Docs for HTTPS request (Jun Wan Goh)

# 3.3.1 (2016-12-17)

* Fixed "double callback bug" warning on timeouts of gzipped responses

# 3.3.0 (2016-12-14)

* Added `.ok(callback)` that allows customizing which responses are errors (Kornel Lesiński)
* Added `.responseType()` to Node version (Kornel Lesiński)
* Added `.parse()` to browser version (jakepearson)
* Fixed parse error when using `responseType('blob')` (Kornel Lesiński)

# 3.2.0 (2016-12-11)

* Added `.timeout({response:ms})`, which allows limiting maximum response time independently from total download time (Kornel Lesiński)
* Added warnings when `.end()` is called more than once (Kornel Lesiński)
* Added `response.links` to browser version (Lukas Eipert)
* `btoa` is no longer required in IE9 (Kornel Lesiński)
* Fixed `.sortQuery()` on URLs without query strings (Kornel Lesiński)
* Refactored common response code into `ResponseBase` (Lukas Eipert)

# 3.1.0 (2016-11-28)

* Added `.sortQuery()` (vicanso)
* Added support for arrays and bools in `.field()` (Kornel Lesiński)
* Made `superagent.Request` subclassable without need to patch all static methods (Kornel Lesiński)

# 3.0.0 (2016-11-19)

* Dropped support for Node 0.x. Please upgrade to at least Node 4.
* Dropped support for componentjs (Damien Caselli)
* Removed deprecated `.part()`/`superagent.Part` APIs.
* Removed unreliable `.body` property on internal response object used by unbuffered parsers.
  Note: the normal `response.body` is unaffected.
* Multiple `.send()` calls mixing `Buffer`/`Blob` and JSON data are not possible and will now throw instead of messing up the data.
* Improved `.send()` data object type check (Fernando Mendes)
* Added common prototype for Node and browser versions (Andreas Helmberger)
* Added `http+unix:` schema to support Unix sockets (Yuki KAN)
* Added full `attach` options parameter in the Node version (Lapo Luchini)
* Added `pfx` TLS option with new `pfx()` method. (Reid Burke)
* Internally changed `.on` to `.once` to prevent possible memory leaks (Matt Blair)
* Made all errors reported as an event (Kornel Lesiński)

# 2.3.0 (2016-09-20)

* Enabled `.field()` to handle objects (Affan Shahid)
* Added authentication with client certificates (terusus)
* Added `.catch()` for more Promise-like interface (Maxim Samoilov, Kornel Lesiński)
* Silenced errors from incomplete gzip streams for compatibility with web browsers (Kornel Lesiński)
* Fixed `event.direction` in uploads (Kornel Lesiński)
* Fixed returned value of overwritten response object's `on()` method (Juan Dopazo)

# 2.2.0 (2016-08-13)

* Added `timedout` property to node Request instance (Alexander Pope)
* Unified `null` querystring values in node and browser environments. (George Chung)

# 2.1.0 (2016-06-14)

* Refactored async parsers. Now the `end` callback waits for async parsers to finish (Kornel Lesiński)
* Errors thrown in `.end()` callback don't cause the callback to be called twice (Kornel Lesiński)
* Added `headers` to `toJSON()` (Tao)

# 2.0.0 (2016-05-29)


## Breaking changes

Breaking changes are in rarely used functionality, so we hope upgrade will be smooth for most users.

* Browser: The `.parse()` method has been renamed to `.serialize()` for consistency with NodeJS version.
* Browser: Query string keys without a value used to be parsed as `'undefined'`, now their value is `''` (empty string) (shura, Kornel Lesiński).
* NodeJS: The `redirect` event is called after new query string and headers have been set and is allowed to override the request URL (Kornel Lesiński)
* `.then()` returns a real `Promise`. Note that use of superagent with promises now requires a global `Promise` object.
  If you target Internet Explorer or Node 0.10, you'll need `require('es6-promise').polyfill()` or similar.
* Upgraded all dependencies (Peter Lyons)
* Renamed properties documented as `@api private` to have `_prefixed` names (Kornel Lesiński)


## Probably not breaking changes:

* Extracted common functions to request-base (Peter Lyons)
* Fixed race condition in pipe tests (Peter Lyons)
* Handle `FormData` error events (scriptype)
* Fixed wrong jsdoc of Request#attach (George Chung)
* Updated and improved tests (Peter Lyons)
* `request.head()` supports `.redirects(5)` call (Kornel Lesiński)
* `response` event is also emitted when using `.pipe()`

# 1.8.2 (2016-03-20)

* Fixed handling of HTTP status 204 with content-encoding: gzip (Andrew Shelton)
* Handling of FormData error events (scriptype)
* Fixed parsing of `vnd+json` MIME types (Kornel Lesiński)
* Aliased browser implementation of `.parse()` as `.serialize()` for forward compatibility

# 1.8.1 (2016-03-14)

* Fixed form-data incompatibility with IE9

# 1.8.0 (2016-03-09)

* Extracted common code into request-base class (Peter Lyons)
  * It does not affect the public API, but please let us know if you notice any plugins/subclasses breaking!
* Added option `{type:'auto'}` to `auth` method, which enables browser-native auth types (Jungle, Askar Yusupov)
* Added `responseType()` to set XHR `responseType` (chris)
* Switched to form-data for browserify-compatible `FormData` (Peter Lyons)
* Added `statusCode` to error response when JSON response is malformed (mattdell)
* Prevented TCP port conflicts in all tests (Peter Lyons)
* Updated form-data dependency

# 1.7.2 (2016-01-26)

* Fix case-sensitivity of header fields introduced by [`a4ddd6a`](https://github.com/ladjs/superagent/commit/a4ddd6a). (Edward J. Jinotti)
* bump extend dependency, as former version did not contain any license information (Lukas Eipert)

# 1.7.1 (2016-01-21)

* Fixed a conflict with express when using npm 3.x (Glenn)
* Fixed redirects after a multipart/form-data POST request (cyclist2)

# 1.7.0 (2016-01-18)

* When attaching files, read default filename from the `File` object (JD Isaacks)
* Add `direction` property to `progress` events (Joseph Dykstra)
* Update component-emitter & formidable (Kornel Lesiński)
* Don't re-encode query string needlessly (Ruben Verborgh)
* ensure querystring is appended when doing `stream.pipe(request)` (Keith Grennan)
* change set header function, not call `this.request()` until call `this.end()` (vicanso)
* Add no-op `withCredentials` to Node API (markdalgleish)
* fix `delete` breaking on ie8 (kenjiokabe)
* Don't let request error override responses (Clay Reimann)
* Increased number of tests shared between node and client (Kornel Lesiński)

# 1.6.0/1.6.1 (2015-12-09)

* avoid misleading CORS error message
* added 'progress' event on file/form upload in Node (Olivier Lalonde)
* return raw response if the response parsing fails (Rei Colina)
* parse content-types ending with `+json` as JSON (Eiryyy)
* fix to avoid throwing errors on aborted requests (gjurgens)
* retain cookies on redirect when hosts match (Tom Conroy)
* added Bower manifest (Johnny Freeman)
* upgrade to latest cookiejar (Andy Burke)

# 1.5.0 (2015-11-30)

* encode array values as `key=1&key=2&key=3` etc... (aalpern, Davis Kim)
* avoid the error which is omitted from 'socket hang up'
* faster JSON parsing, handling of zlib errors (jbellenger)
* fix IE11 sends 'undefined' string if data was undefined (Vadim Goncharov)
* alias `del()` method as `delete()` (Aaron Krause)
* revert Request#parse since it was actually Response#parse

# 1.4.0 (2015-09-14)

* add Request#parse method to client library
* add missing statusCode in client response
* don't apply JSON heuristics if a valid parser is found
* fix detection of root object for webworkers

# 1.3.0 (2015-08-05)

* fix incorrect content-length of data set to buffer
* serialize request data takes into account charsets
* add basic promise support via a `then` function

# 1.2.0 (2015-04-13)

* add progress events to downlodas
* make usable in webworkers
* add support for 308 redirects
* update node-form-data dependency
* update to work in react native
* update node-mime dependency

# 1.1.0 (2015-03-13)

* Fix responseType checks without xhr2 and ie9 tests (rase-)
* errors have .status and .response fields if applicable (defunctzombie)
* fix end callback called before saving cookies (rase-)

# 1.0.0 / 2015-03-08

* All non-200 responses are treated as errors now. (The callback is called with an error when the response has a status &lt; 200 or >= 300 now. In previous versions this would not have raised an error and the client would have to check the `res` object. See [#283](https://github.com/ladjs/superagent/issues/283).
* keep timeouts intact across redirects (hopkinsth)
* handle falsy json values (themaarten)
* fire response events in browser version (Schoonology)
* getXHR exported in client version (KidsKilla)
* remove arity check on `.end()` callbacks (defunctzombie)
* avoid setting content-type for host objects (rexxars)
* don't index array strings in querystring (travisjeffery)
* fix pipe() with redirects (cyrilis)
* add xhr2 file download (vstirbu)
* set default response type to text/plain if not specified (warrenseine)

# 0.21.0 / 2014-11-11

* Trim text before parsing json (gjohnson)
* Update tests to express 4 (gaastonsr)
* Prevent double callback when error is thrown (pgn-vole)
* Fix missing clearTimeout (nickdima)
* Update debug (TooTallNate)

# 0.20.0 / 2014-10-02

* Add toJSON() to request and response instances. (yields)
* Prevent HEAD requests from getting parsed. (gjohnson)
* Update debug. (TooTallNate)

# 0.19.1 / 2014-09-24

* Fix basic auth issue when password is falsey value. (gjohnson)

# 0.19.0 / 2014-09-24

* Add unset() to browser. (shesek)
* Prefer XHR over ActiveX. (omeid)
* Catch parse errors. (jacwright)
* Update qs dependency. (wercker)
* Add use() to node. (Financial-Times)
* Add response text to errors. (yields)
* Don't send empty cookie headers. (undoZen)
* Don't parse empty response bodies. (DveMac)
* Use hostname when setting cookie host. (prasunsultania)

# 0.18.2 / 2014-07-12

* Handle parser errors. (kof)
* Ensure not to use default parsers when there is a user defined one. (kof)

# 0.18.1 / 2014-07-05

* Upgrade cookiejar dependency (juanpin)
* Support image mime types (nebulade)
* Make .agent chainable (kof)
* Upgrade debug (TooTallNate)
* Fix docs (aheckmann)

# 0.18.0 / 2014-04-29

* Use "form-data" module for the multipart/form-data implementation. (TooTallNate)
* Add basic `field()` and `attach()` functions for HTML5 FormData. (TooTallNate)
* Deprecate `part()`. (TooTallNate)
* Set de
... [TRUNCATED]
```

### File: index.html
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf8">
    <title>SuperAgent — elegant API for AJAX in Node and browsers</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/tocbot/3.0.0/tocbot.css">
    <link rel="stylesheet" href="docs/style.css">
  </head>
  <body>
    <ul id="menu"></ul>
    <div id="content">
<h1 id="superagent">SuperAgent</h1>
<p>SuperAgent is light-weight progressive ajax API crafted for flexibility, readability, and a low learning curve after being frustrated with many of the existing request APIs. It also works with Node.js!</p>
<pre><code class="language-javascript">     request
       .post(&#39;/api/pet&#39;)
       .send({ name: &#39;Manny&#39;, species: &#39;cat&#39; })
       .set(&#39;X-API-Key&#39;, &#39;foobar&#39;)
       .set(&#39;Accept&#39;, &#39;application/json&#39;)
       .then(res =&gt; {
          alert(&#39;yay got &#39; + JSON.stringify(res.body));
       });
</code></pre>
<h2 id="test-documentation">Test documentation</h2>
<p><a href="docs/zh_CN/index.html"><strong>中文文档</strong></a></p>
<p>The following <a href="docs/test.html">test documentation</a> was generated with <a href="https://mochajs.org/">Mocha&#39;s</a> &quot;doc&quot; reporter, and directly reflects the test suite. This provides an additional source of documentation.</p>
<h2 id="request-basics">Request basics</h2>
<p>A request can be initiated by invoking the appropriate method on the <code>request</code> object, then calling <code>.then()</code> (or <code>.end()</code> <a href="#promise-and-generator-support">or <code>await</code></a>) to send the request. For example a simple <strong>GET</strong> request:</p>
<pre><code class="language-javascript">     request
       .get(&#39;/search&#39;)
       .then(res =&gt; {
          // res.body, res.headers, res.status
       })
       .catch(err =&gt; {
          // err.message, err.response
       });
</code></pre>
<p>HTTP method may also be passed as a string:</p>
<pre><code class="language-javascript">    request(&#39;GET&#39;, &#39;/search&#39;).then(success, failure);
</code></pre>
<p>Old-style callbacks are also supported, but not recommended. <em>Instead of</em> <code>.then()</code> you can call <code>.end()</code>:</p>
<pre><code class="language-javascript">    request(&#39;GET&#39;, &#39;/search&#39;).end(function(err, res){
      if (res.ok) {}
    });
</code></pre>
<p>Absolute URLs can be used. In web browsers absolute URLs work only if the server implements <a href="#cors">CORS</a>.</p>
<pre><code class="language-javascript">     request
       .get(&#39;https://example.com/search&#39;)
       .then(res =&gt; {

       });
</code></pre>
<p>The <strong>Node</strong> client supports making requests to <a href="https://en.wikipedia.org/wiki/Unix_domain_socket">Unix Domain Sockets</a>:</p>
<pre><code class="language-javascript">    // pattern: https?+unix://SOCKET_PATH/REQUEST_PATH
    //          Use `%2F` as `/` in SOCKET_PATH
    try {
      const res = await request
        .get(&#39;http+unix://%2Fabsolute%2Fpath%2Fto%2Funix.sock/search&#39;);
      // res.body, res.headers, res.status
    } catch(err) {
      // err.message, err.response
    }
</code></pre>
<p><strong>DELETE</strong>, <strong>HEAD</strong>, <strong>PATCH</strong>, <strong>POST</strong>, and <strong>PUT</strong> requests can also be used, simply change the method name:</p>
<pre><code class="language-javascript">    request
      .head(&#39;/favicon.ico&#39;)
      .then(res =&gt; {

      });
</code></pre>
<p><strong>DELETE</strong> can be also called as <code>.del()</code> for compatibility with old IE where <code>delete</code> is a reserved word.</p>
<p>The HTTP method defaults to <strong>GET</strong>, so if you wish, the following is valid:</p>
<pre><code class="language-javascript">     request(&#39;/search&#39;, (err, res) =&gt; {

     });
</code></pre>
<h2 id="using-http/2">Using HTTP/2</h2>
<p>To make a request using HTTP/2 protocol only (with no HTTP/1.x fallback), use the <code>.http2()</code> method.</p>
<pre><code class="language-javascript">    const request = require(&#39;superagent&#39;);
    const res = await request
      .get(&#39;https://example.com/h2&#39;)
      .http2();
</code></pre>
<h2 id="setting-header-fields">Setting header fields</h2>
<p>Setting header fields is simple, invoke <code>.set()</code> with a field name and value:</p>
<pre><code class="language-javascript">     request
       .get(&#39;/search&#39;)
       .set(&#39;API-Key&#39;, &#39;foobar&#39;)
       .set(&#39;Accept&#39;, &#39;application/json&#39;)
       .then(callback);
</code></pre>
<p>You may also pass an object to set several fields in a single call:</p>
<pre><code class="language-javascript">     request
       .get(&#39;/search&#39;)
       .set({ &#39;API-Key&#39;: &#39;foobar&#39;, Accept: &#39;application/json&#39; })
       .then(callback);
</code></pre>
<h2 id="get-requests"><code>GET</code> requests</h2>
<p>The <code>.query()</code> method accepts objects, which when used with the <strong>GET</strong> method will form a query-string. The following will produce the path <code>/search?query=Manny&amp;range=1..5&amp;order=desc</code>.</p>
<pre><code class="language-javascript">     request
       .get(&#39;/search&#39;)
       .query({ query: &#39;Manny&#39; })
       .query({ range: &#39;1..5&#39; })
       .query({ order: &#39;desc&#39; })
       .then(res =&gt; {

       });
</code></pre>
<p>Or as a single object:</p>
<pre><code class="language-javascript">    request
      .get(&#39;/search&#39;)
      .query({ query: &#39;Manny&#39;, range: &#39;1..5&#39;, order: &#39;desc&#39; })
      .then(res =&gt; {

      });
</code></pre>
<p>The <code>.query()</code> method accepts strings as well:</p>
<pre><code class="language-javascript">      request
        .get(&#39;/querystring&#39;)
        .query(&#39;search=Manny&amp;range=1..5&#39;)
        .then(res =&gt; {

        });
</code></pre>
<p>Or joined:</p>
<pre><code class="language-javascript">      request
        .get(&#39;/querystring&#39;)
        .query(&#39;search=Manny&#39;)
        .query(&#39;range=1..5&#39;)
        .then(res =&gt; {

        });
</code></pre>
<h2 id="head-requests"><code>HEAD</code> requests</h2>
<p>You can also use the <code>.query()</code> method for HEAD requests. The following will produce the path <code>/users?email=joe@smith.com</code>.</p>
<pre><code class="language-javascript">      request
        .head(&#39;/users&#39;)
        .query({ email: &#39;joe@smith.com&#39; })
        .then(res =&gt; {

        });
</code></pre>
<h2 id="post--put-requests"><code>POST</code> / <code>PUT</code> requests</h2>
<p>A typical JSON <strong>POST</strong> request might look a little like the following, where we set the Content-Type header field appropriately, and &quot;write&quot; some data, in this case just a JSON string.</p>
<pre><code class="language-javascript">      request.post(&#39;/user&#39;)
        .set(&#39;Content-Type&#39;, &#39;application/json&#39;)
        .send(&#39;{&quot;name&quot;:&quot;tj&quot;,&quot;pet&quot;:&quot;tobi&quot;}&#39;)
        .then(callback)
        .catch(errorCallback)
</code></pre>
<p>Since JSON is undoubtedly the most common, it&#39;s the <em>default</em>! The following example is equivalent to the previous.</p>
<pre><code class="language-javascript">      request.post(&#39;/user&#39;)
        .send({ name: &#39;tj&#39;, pet: &#39;tobi&#39; })
        .then(callback, errorCallback)
</code></pre>
<p>Or using multiple <code>.send()</code> calls:</p>
<pre><code class="language-javascript">      request.post(&#39;/user&#39;)
        .send({ name: &#39;tj&#39; })
        .send({ pet: &#39;tobi&#39; })
        .then(callback, errorCallback)
</code></pre>
<p>By default sending strings will set the <code>Content-Type</code> to <code>application/x-www-form-urlencoded</code>,
  multiple calls will be concatenated with <code>&amp;</code>, here resulting in <code>name=tj&amp;pet=tobi</code>:</p>
<pre><code class="language-javascript">      request.post(&#39;/user&#39;)
        .send(&#39;name=tj&#39;)
        .send(&#39;pet=tobi&#39;)
        .then(callback, errorCallback);
</code></pre>
<p>SuperAgent formats are extensible, however by default &quot;json&quot; and &quot;form&quot; are supported. To send the data as <code>application/x-www-form-urlencoded</code> simply invoke <code>.type()</code> with &quot;form&quot;, where the default is &quot;json&quot;. This request will <strong>POST</strong> the body &quot;name=tj&amp;pet=tobi&quot;.</p>
<pre><code class="language-javascript">      request.post(&#39;/user&#39;)
        .type(&#39;form&#39;)
        .send({ name: &#39;tj&#39; })
        .send({ pet: &#39;tobi&#39; })
        .then(callback, errorCallback)
</code></pre>
<p>Sending a <a href="https://developer.mozilla.org/en-US/docs/Web/API/FormData/FormData"><code>FormData</code></a> object is also supported. The following example will <strong>POST</strong> the content of the HTML form identified by id=&quot;myForm&quot;:</p>
<pre><code class="language-javascript">      request.post(&#39;/user&#39;)
        .send(new FormData(document.getElementById(&#39;myForm&#39;)))
        .then(callback, errorCallback)
</code></pre>
<h2 id="setting-the-content-type">Setting the <code>Content-Type</code></h2>
<p>The obvious solution is to use the <code>.set()</code> method:</p>
<pre><code class="language-javascript">     request.post(&#39;/user&#39;)
       .set(&#39;Content-Type&#39;, &#39;application/json&#39;)
</code></pre>
<p>As a short-hand the <code>.type()</code> method is also available, accepting
the canonicalized MIME type name complete with type/subtype, or
simply the extension name such as &quot;xml&quot;, &quot;json&quot;, &quot;png&quot;, etc:</p>
<pre><code class="language-javascript">     request.post(&#39;/user&#39;)
       .type(&#39;application/json&#39;)

     request.post(&#39;/user&#39;)
       .type(&#39;json&#39;)

     request.post(&#39;/user&#39;)
       .type(&#39;png&#39;)
</code></pre>
<h2 id="serializing-request-body">Serializing request body</h2>
<p>SuperAgent will automatically serialize JSON and forms.
You can setup automatic serialization for other types as well:</p>
<pre><code class="language-js">request.serialize[&#39;application/xml&#39;] = function (obj) {
    return &#39;string generated from obj&#39;;
};

// going forward, all requests with a Content-type of
// &#39;application/xml&#39; will be automatically serialized
</code></pre>
<p>If you want to send the payload in a custom format, you can replace
the built-in serialization with the <code>.serialize()</code> method on a per-request basis:</p>
<pre><code class="language-js">request
    .post(&#39;/user&#39;)
    .send({foo: &#39;bar&#39;})
    .serialize(obj =&gt; {
        return &#39;string generated from obj&#39;;
    });
</code></pre>
<h2 id="retrying-requests">Retrying requests</h2>
<p>When given the <code>.retry()</code> method, SuperAgent will automatically retry requests, if they fail in a way that is transient or could be due to a flaky Internet connection.</p>
<p>This method has two optional arguments: number of retries (default 1) and a callback. It calls <code>callback(err, res)</code> before each retry. The callback may return <code>true</code>/<code>false</code> to control whether the request should be retried (but the maximum number of retries is always applied).</p>
<pre><code class="language-javascript">     request
       .get(&#39;https://example.com/search&#39;)
       .retry(2) // or:
       .retry(2, callback)
       .then(finished);
       .catch(failed);
</code></pre>
<p>Use <code>.retry()</code> only with requests that are <em>idempotent</em> (i.e. multiple requests reaching the server won&#39;t cause undesirable side effects like duplicate purchases).</p>
<p>All request methods are tried by default (which means if you do not want POST requests to be retried, you will need to pass a custom retry callback).</p>
<p>By default the following status codes are retried:</p>
<ul>
<li><code>408</code></li>
<li><code>413</code></li>
<li><code>429</code></li>
<li><code>500</code></li>
<li><code>502</code></li>
<li><code>503</code></li>
<li><code>504</code></li>
<li><code>521</code></li>
<li><code>522</code></li>
<li><code>524</code></li>
</ul>
<p>By default the following error codes are retried:</p>
<ul>
<li><code>&#39;ETIMEDOUT&#39;</code></li>
<li><code>&#39;ECONNRESET&#39;</code></li>
<li><code>&#39;EADDRINUSE&#39;</code></li>
<li><code>&#39;ECONNREFUSED&#39;</code></li>
<li><code>&#39;EPIPE&#39;</code></li>
<li><code>&#39;ENOTFOUND&#39;</code></li>
<li><code>&#39;ENETUNREACH&#39;</code></li>
<li><code>&#39;EAI_AGAIN&#39;</code></li>
</ul>
<h2 id="setting-accept">Setting Accept</h2>
<p>In a similar fashion to the <code>.type()</code> method it is also possible to set the <code>Accept</code> header via the short hand method <code>.accept()</code>. Which references <code>request.types</code> as well allowing you to specify either the full canonicalized MIME type name as <code>type/subtype</code>, or the extension suffix form as &quot;xml&quot;, &quot;json&quot;, &quot;png&quot;, etc. for convenience:</p>
<pre><code class="language-javascript">     request.get(&#39;/user&#39;)
       .accept(&#39;application/json&#39;)

     request.get(&#39;/user&#39;)
       .accept(&#39;json&#39;)

     request.post(&#39;/user&#39;)
       .accept(&#39;png&#39;)
</code></pre>
<h3 id="facebook-and-accept-json">Facebook and Accept JSON</h3>
<p>If you are calling Facebook&#39;s API, be sure to send an <code>Accept: application/json</code> header in your request. If you don&#39;t do this, Facebook will respond with <code>Content-Type: text/javascript; charset=UTF-8</code>, which SuperAgent will not parse and thus <code>res.body</code> will be undefined. You can do this with either <code>req.accept(&#39;json&#39;)</code> or <code>req.set(&#39;Accept&#39;, &#39;application/json&#39;)</code>. See <a href="https://github.com/ladjs/superagent/issues/1078">issue 1078</a> for details.</p>
<h2 id="query-strings">Query strings</h2>
<p>  <code>req.query(obj)</code> is a method which may be used to build up a query-string. For example populating <code>?format=json&amp;dest=/login</code> on a <strong>POST</strong>:</p>
<pre><code class="language-javascript">    request
      .post(&#39;/&#39;)
      .query({ format: &#39;json&#39; })
      .query({ dest: &#39;/login&#39; })
      .send({ post: &#39;data&#39;, here: &#39;wahoo&#39; })
      .then(callback);
</code></pre>
<p>By default the query string is not assembled in any particular order. An asciibetically-sorted query string can be enabled with <code>req.sortQuery()</code>. You may also provide a custom sorting comparison function with <code>req.sortQuery(myComparisonFn)</code>. The comparison function should take 2 arguments and return a negative/zero/positive integer.</p>
<pre><code class="language-js"> // default or
... [TRUNCATED]
```

### File: SECURITY.md
```md
# Security Policy


## Reporting a Vulnerability

Please report security issues to `niftylettuce@gmail.com`

```

### File: ci\remove-deps-4-old-node.js
```js
const fs = require('fs');
const path = require('path');
const package = require('../package.json');

const UNSUPPORT_DEPS_4_OLD = new Set([
  '@commitlint/cli',
  '@commitlint/config-conventional',
  'eslint',
  'eslint-config-xo-lass',
  'eslint-plugin-compat',
  'eslint-plugin-node',
  'husky',
  'lint-staged',
  'marked',
  'remark-cli',
  'remark-preset-github',
  'xo'
]);

for (const item in package.devDependencies) {
  if (UNSUPPORT_DEPS_4_OLD.has(item)) {
    package.devDependencies[item] = undefined;
  }
}

fs.writeFileSync(
  path.join(__dirname, '../package.json'),
  JSON.stringify(package, null, 2)
);

```

### File: docs\head.html
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf8">
    <title>SuperAgent — elegant API for AJAX in Node and browsers</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/tocbot/3.0.0/tocbot.css">
    <link rel="stylesheet" href="docs/style.css">
  </head>
  <body>
    <ul id="menu"></ul>
    <div id="content">

```

### File: docs\index.md
```md

# SuperAgent

SuperAgent is light-weight progressive ajax API crafted for flexibility, readability, and a low learning curve after being frustrated with many of the existing request APIs. It also works with Node.js!

```javascript
     request
       .post('/api/pet')
       .send({ name: 'Manny', species: 'cat' })
       .set('X-API-Key', 'foobar')
       .set('Accept', 'application/json')
       .then(res => {
          alert('yay got ' + JSON.stringify(res.body));
       });
```

## Test documentation

[**中文文档**](docs/zh_CN/index.html)

The following [test documentation](docs/test.html) was generated with [Mocha's](https://mochajs.org/) "doc" reporter, and directly reflects the test suite. This provides an additional source of documentation.

## Request basics

A request can be initiated by invoking the appropriate method on the `request` object, then calling `.then()` (or `.end()` [or `await`](#promise-and-generator-support)) to send the request. For example a simple __GET__ request:

```javascript
     request
       .get('/search')
       .then(res => {
          // res.body, res.headers, res.status
       })
       .catch(err => {
          // err.message, err.response
       });
```

HTTP method may also be passed as a string:

```javascript
    request('GET', '/search').then(success, failure);
```

Old-style callbacks are also supported, but not recommended. *Instead of* `.then()` you can call `.end()`:

```javascript
    request('GET', '/search').end(function(err, res){
      if (res.ok) {}
    });
```

Absolute URLs can be used. In web browsers absolute URLs work only if the server implements [CORS](#cors).

```javascript
     request
       .get('https://example.com/search')
       .then(res => {

       });
```

The __Node__ client supports making requests to [Unix Domain Sockets](https://en.wikipedia.org/wiki/Unix_domain_socket):

```javascript
    // pattern: https?+unix://SOCKET_PATH/REQUEST_PATH
    //          Use `%2F` as `/` in SOCKET_PATH
    try {
      const res = await request
        .get('http+unix://%2Fabsolute%2Fpath%2Fto%2Funix.sock/search');
      // res.body, res.headers, res.status
    } catch(err) {
      // err.message, err.response
    }
```

__DELETE__, __HEAD__, __PATCH__, __POST__, and __PUT__ requests can also be used, simply change the method name:

```javascript
    request
      .head('/favicon.ico')
      .then(res => {

      });
```

__DELETE__ can be also called as `.del()` for compatibility with old IE where `delete` is a reserved word.

The HTTP method defaults to __GET__, so if you wish, the following is valid:

```javascript
     request('/search', (err, res) => {

     });
```

## Using HTTP/2

To make a request using HTTP/2 protocol only (with no HTTP/1.x fallback), use the `.http2()` method.

```javascript
    const request = require('superagent');
    const res = await request
      .get('https://example.com/h2')
      .http2();
```

## Setting header fields

Setting header fields is simple, invoke `.set()` with a field name and value:

```javascript
     request
       .get('/search')
       .set('API-Key', 'foobar')
       .set('Accept', 'application/json')
       .then(callback);
```

You may also pass an object to set several fields in a single call:

```javascript
     request
       .get('/search')
       .set({ 'API-Key': 'foobar', Accept: 'application/json' })
       .then(callback);
```

## `GET` requests

The `.query()` method accepts objects, which when used with the __GET__ method will form a query-string. The following will produce the path `/search?query=Manny&range=1..5&order=desc`.

```javascript
     request
       .get('/search')
       .query({ query: 'Manny' })
       .query({ range: '1..5' })
       .query({ order: 'desc' })
       .then(res => {

       });
```

Or as a single object:

```javascript
    request
      .get('/search')
      .query({ query: 'Manny', range: '1..5', order: 'desc' })
      .then(res => {

      });
```

The `.query()` method accepts strings as well:

```javascript
      request
        .get('/querystring')
        .query('search=Manny&range=1..5')
        .then(res => {

        });
```

Or joined:

```javascript
      request
        .get('/querystring')
        .query('search=Manny')
        .query('range=1..5')
        .then(res => {

        });
```

## `HEAD` requests

You can also use the `.query()` method for HEAD requests. The following will produce the path `/users?email=joe@smith.com`.

```javascript
      request
        .head('/users')
        .query({ email: 'joe@smith.com' })
        .then(res => {

        });
```

## `POST` / `PUT` requests

A typical JSON __POST__ request might look a little like the following, where we set the Content-Type header field appropriately, and "write" some data, in this case just a JSON string.

```javascript
      request.post('/user')
        .set('Content-Type', 'application/json')
        .send('{"name":"tj","pet":"tobi"}')
        .then(callback)
        .catch(errorCallback)
```

Since JSON is undoubtedly the most common, it's the _default_! The following example is equivalent to the previous.

```javascript
      request.post('/user')
        .send({ name: 'tj', pet: 'tobi' })
        .then(callback, errorCallback)
```

Or using multiple `.send()` calls:

```javascript
      request.post('/user')
        .send({ name: 'tj' })
        .send({ pet: 'tobi' })
        .then(callback, errorCallback)
```

By default sending strings will set the `Content-Type` to `application/x-www-form-urlencoded`,
  multiple calls will be concatenated with `&`, here resulting in `name=tj&pet=tobi`:

```javascript
      request.post('/user')
        .send('name=tj')
        .send('pet=tobi')
        .then(callback, errorCallback);
```

SuperAgent formats are extensible, however by default "json" and "form" are supported. To send the data as `application/x-www-form-urlencoded` simply invoke `.type()` with "form", where the default is "json". This request will __POST__ the body "name=tj&pet=tobi".

```javascript
      request.post('/user')
        .type('form')
        .send({ name: 'tj' })
        .send({ pet: 'tobi' })
        .then(callback, errorCallback)
```

Sending a [`FormData`](https://developer.mozilla.org/en-US/docs/Web/API/FormData/FormData) object is also supported. The following example will __POST__ the content of the HTML form identified by id="myForm":

```javascript
      request.post('/user')
        .send(new FormData(document.getElementById('myForm')))
        .then(callback, errorCallback)
```

## Setting the `Content-Type`

The obvious solution is to use the `.set()` method:

```javascript
     request.post('/user')
       .set('Content-Type', 'application/json')
```

As a short-hand the `.type()` method is also available, accepting
the canonicalized MIME type name complete with type/subtype, or
simply the extension name such as "xml", "json", "png", etc:

```javascript
     request.post('/user')
       .type('application/json')

     request.post('/user')
       .type('json')

     request.post('/user')
       .type('png')
```

## Serializing request body

SuperAgent will automatically serialize JSON and forms.
You can setup automatic serialization for other types as well:

```js
request.serialize['application/xml'] = function (obj) {
    return 'string generated from obj';
};

// going forward, all requests with a Content-type of
// 'application/xml' will be automatically serialized
```
If you want to send the payload in a custom format, you can replace
the built-in serialization with the `.serialize()` method on a per-request basis:

```js
request
    .post('/user')
    .send({foo: 'bar'})
    .serialize(obj => {
        return 'string generated from obj';
    });
```
## Retrying requests

When given the `.retry()` method, SuperAgent will automatically retry requests, if they fail in a way that is transient or could be due to a flaky Internet connection.

This method has two optional arguments: number of retries (default 1) and a callback. It calls `callback(err, res)` before each retry. The callback may return `true`/`false` to control whether the request should be retried (but the maximum number of retries is always applied).

```javascript
     request
       .get('https://example.com/search')
       .retry(2) // or:
       .retry(2, callback)
       .then(finished);
       .catch(failed);
```

Use `.retry()` only with requests that are *idempotent* (i.e. multiple requests reaching the server won't cause undesirable side effects like duplicate purchases).

All request methods are tried by default (which means if you do not want POST requests to be retried, you will need to pass a custom retry callback).

By default the following status codes are retried:

* `408`
* `413`
* `429`
* `500`
* `502`
* `503`
* `504`
* `521`
* `522`
* `524`

By default the following error codes are retried:

* `'ETIMEDOUT'`
* `'ECONNRESET'`
* `'EADDRINUSE'`
* `'ECONNREFUSED'`
* `'EPIPE'`
* `'ENOTFOUND'`
* `'ENETUNREACH'`
* `'EAI_AGAIN'`

## Setting Accept

In a similar fashion to the `.type()` method it is also possible to set the `Accept` header via the short hand method `.accept()`. Which references `request.types` as well allowing you to specify either the full canonicalized MIME type name as `type/subtype`, or the extension suffix form as "xml", "json", "png", etc. for convenience:

```javascript
     request.get('/user')
       .accept('application/json')

     request.get('/user')
       .accept('json')

     request.post('/user')
       .accept('png')
```

### Facebook and Accept JSON

If you are calling Facebook's API, be sure to send an `Accept: application/json` header in your request. If you don't do this, Facebook will respond with `Content-Type: text/javascript; charset=UTF-8`, which SuperAgent will not parse and thus `res.body` will be undefined. You can do this with either `req.accept('json')` or `req.set('Accept', 'application/json')`. See [issue 1078](https://github.com/ladjs/superagent/issues/1078) for details.

## Query strings

  `req.query(obj)` is a method which may be used to build up a query-string. For example populating `?format=json&dest=/login` on a __POST__:

```javascript
    request
      .post('/')
      .query({ format: 'json' })
      .query({ dest: '/login' })
      .send({ post: 'data', here: 'wahoo' })
      .then(callback);
```

By default the query string is not assembled in any particular order. An asciibetically-sorted query string can be enabled with `req.sortQuery()`. You may also provide a custom sorting comparison function with `req.sortQuery(myComparisonFn)`. The comparison function should take 2 arguments and return a negative/zero/positive integer.

```js
 // default order
 request.get('/user')
   .query('name=Nick')
   .query('search=Manny')
   .sortQuery()
   .then(callback)

 // customized sort function
 request.get('/user')
   .query('name=Nick')
   .query('search=Manny')
   .sortQuery((a, b) => a.length - b.length)
   .then(callback)
```

## TLS options

In Node.js SuperAgent supports methods to configure HTTPS requests:

- `.ca()`: Set the CA certificate(s) to trust
- `.cert()`: Set the client certificate chain(s)
- `.key()`: Set the client private key(s)
- `.pfx()`: Set the client PFX or PKCS12 encoded private key and certificate chain
- `.disableTLSCerts()`: Does not reject expired or invalid TLS certs. Sets internally `rejectUnauthorized=true`. *Be warned, this method allows MITM attacks.*

For more information, see Node.js [https.request docs](https://nodejs.org/api/https.html#https_https_request_options_callback).

```js
var key = fs.readFileSync('key.pem'),
    cert = fs.readFileSync('cert.pem');

request
  .post('/client-auth')
  .key(key)
  .cert(cert)
  .then(callback);
```

```js
var ca = fs.readFileSync('ca.cert.pem');

request
  .post('https://localhost/private-ca-server')
  .ca(ca)
  .then(res => {});
```

## Parsing response bodies

SuperAgent will parse known response-body data for you,
currently supporting `application/x-www-form-urlencoded`,
`application/json`, and `multipart/form-data`. You can setup
automatic parsing for other response-body data as well:

```js
//browser
request.parse['application/xml'] = function (str) {
    return {'object': 'parsed from str'};
};

//node
request.parse['application/xml'] = function (res, cb) {
    //parse response text and set res.body here

    cb(null, res);
};

//going forward, responses of type 'application/xml'
//will be parsed automatically
```

You can set a custom parser (that takes precedence over built-in parsers) with the `.buffer(true).parse(fn)` method. If response buffering is not enabled (`.buffer(false)`) then the `response` event will be emitted without waiting for the body parser to finish, so `response.body` won't be available.

### JSON / Urlencoded

The property `res.body` is the parsed object, for example if a request responded with the JSON string '{"user":{"name":"tobi"}}', `res.body.user.name` would be "tobi". Likewise the x-www-form-urlencoded value of "user[name]=tobi" would yield the same result. Only one level of nesting is supported. If you need more complex data, send JSON instead.

Arrays are sent by repeating the key. `.send({color: ['red','blue']})` sends `color=red&color=blue`. If you want the array keys to contain `[]` in their name, you must add it yourself, as SuperAgent doesn't add it automatically.

### Multipart

The Node client supports _multipart/form-data_ via the [Formidable](https://github.com/felixge/node-formidable) module. When parsing multipart responses, the object `res.files` is also available to you. Suppose for example a request responds with the following multipart body:

    --whoop
    Content-Disposition: attachment; name="image"; filename="tobi.png"
    Content-Type: image/png

    ... data here ...
    --whoop
    Content-Disposition: form-data; name="name"
    Content-Type: text/plain

    Tobi
    --whoop--

You would have the values `res.body.name` provided as "Tobi", and `res.files.image` as a `File` object containing the path on disk, filename, and other properties.

### Binary

In browsers, you may use `.responseType('blob')` to request handling of binary response bodies. This API is unnecessary when running in node.js. The supported argument values for this method are

- `'blob'` passed through to the XmlHTTPRequest `responseType` property
- `'arraybuffer'` passed through to the XmlHTTPRequest `responseType` property

```js
req.get('/binary.data')
  .responseType('blob')
  .then(res => {
    // res.body will be a browser native Blob type here
  });
```

For more information, see the Mozilla Developer Network [xhr.responseType docs](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/responseType).

## Response properties

Many helpful flags and properties are set on the `Response` object, ranging from the response text, parsed response body, header fields, status flags and more.

### Respons
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

---
id: superagent-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:19.125125
---

# KNOWLEDGE EXTRACT: superagent
> **Extracted on:** 2026-03-30 13:23:12
> **Source:** superagent

---

## File: `.browserslistrc`
```
defaults, not ie 11
```

## File: `.commitlintrc.js`
```javascript
module.exports = {
  extends: ['@commitlint/config-conventional']
};
```

## File: `.dist.babelrc`
```
{
  "presets": [
    ["@babel/env", {
      "targets": {
        "browsers": [ "defaults, not ie 11" ]
      }
    }]
  ],
  "sourceType": "script",
  "sourceMaps": "inline",
  "comments": false
}
```

## File: `.dist.eslintrc`
```
{
  "extends": ["eslint:recommended", "plugin:compat/recommended"],
  "env": {
    "node": false,
    "browser": true,
    "amd": true,
    "es6": true
  },
  "plugins": ["compat"],
  "rules": {
    "node/no-unsupported-features/es-builtins": "off",
    "compat/compat": "error",
    "no-console": "off",
    "no-empty": "off",
    "no-extra-semi": "off",
    "no-func-assign": "off",
    "no-undef": "off",
    "no-unused-vars": "off",
    "no-useless-escape": "off",
    "no-obj-calls": "off",
    "no-cond-assign": "off",
    "no-redeclare": "off",
    "node/no-exports-assign": "off",
    "no-unsafe-finally": "off",
    "complexity": ["error", 10000],
    "max-statements": "off",
    "no-constant-condition": "off",
    "no-control-regex": "off",
    "no-fallthrough": "off",
    "operator-linebreak": "off",
    "node/no-missing-require": "warn"
  },
  "globals": {
    "regeneratorRuntime": "writable"
  },
  "settings": {
    "polyfills": [
      "WeakRef",
      "BigInt"
    ]
  }
}
```

## File: `.editorconfig`
```
root = true

[*]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true
```

## File: `.eslintrc`
```
{
  "extends": [
    "eslint:recommended",
    "plugin:node/recommended"
  ],
  "env": {
    "node": true,
    "browser": true,
    "es6": true
  },
  "parserOptions": {
    "ecmaVersion": 2021
  },
  "overrides": [
    {
      "files": "test/**/*.js",
      "env": {
        "mocha": true
      },
      "rules": {
        "no-prototype-builtins": "off",
        "node/no-deprecated-api": "warn",
        "node/no-extraneous-require": "warn",
        "no-unused-vars": "warn",
        "node/no-missing-require": "warn"
      }
    }
  ],
  "rules": {
    "node/no-unsupported-features/node-builtins": "off",
    "node/no-unsupported-features/es-syntax": "off",
    "node/no-exports-assign": "off",
    "no-unused-vars": "warn"
  },
  "globals": {
  }
}
```

## File: `.gitattributes`
```
* text=auto
```

## File: `.gitignore`
```
.vscode
build
lib-cov
coverage.html
.DS_Store
node_modules
*.sock
test.js
components
test/node/fixtures/tmp.json
.idea
superagent.js
*.log
coverage
.nyc_output
lib
dist
*.swp
yarn.lock
```

## File: `.lib.babelrc`
```
{
  "presets": [
    ["@babel/env", {
      "targets": {
        "node": "14.18.0",
        "browsers": [ "defaults, not ie 11" ]
      }
    }]
  ],
  "sourceMaps": "inline"
}
```

## File: `.lib.eslintrc`
```
{
  "extends": ["eslint:recommended", "plugin:node/recommended"],
  "env": {
    "browser": true
  },
  "rules": {
    "node/no-unsupported-features/es-builtins": ["error", {
      "version": ">=6.4.0",
      "ignores": [
      ]
    }],
    "node/no-deprecated-api": "off",
    "no-console": "off",
    "no-unused-vars": "off",
    "no-empty": "off",
    "no-func-assign": "off",
    "no-global-assign": ["error", {"exceptions": ["exports"]}],
    "no-fallthrough": "off",
    "no-constant-condition": "off",
    "node/no-exports-assign": "off",
    "no-unsafe-finally": "off"
  },
  "overrides": [
    {
      "files": [ "lib/client.js" ],
      "globals": {
      }
    },
    {
      "files": [ "lib/node/http2wrapper.js" ],
      "rules": {
        "node/no-unsupported-features/es-builtins": "off",
        "node/no-unsupported-features/node-builtins": "off"
      }
    }
  ]
}
```

## File: `.lintstagedrc.js`
```javascript
module.exports = {
  "*.md": filenames => filenames.map(filename => `remark ${filename} -qfo`),
  '*.js': 'xo --fix'
};
```

## File: `.npmrc`
```
package-lock=true
```

## File: `.prettierrc.js`
```javascript
module.exports = {
  singleQuote: true,
  bracketSpacing: true,
  trailingComma: 'none'
};
```

## File: `.remarkignore`
```
CONTRIBUTING.md
HISTORY.md
docs
```

## File: `.remarkrc.js`
```javascript
module.exports = {
  plugins: ['preset-github']
};
```

## File: `.test.babelrc`
```
{
  "presets": [
    ["@babel/env", {
      "targets": {
        "node": "14.18.0",
        "browsers": [ "defaults, not ie 11" ]
      }
    }]
  ],
  "plugins": [
    ["@babel/transform-runtime"]
  ],
  "parserOpts": {
    "allowReturnOutsideFunction": true
  },
  "sourceMaps": "inline"
}
```

## File: `.travis.yml`
```yaml
sudo: false
language: node_js
node_js:
  - '18'
  - '16'
  - '14'
after_success: npm run coverage

env:
  global:
    - SAUCE_USERNAME='shtylman-superagent'
    - SAUCE_ACCESS_KEY='39a45464-cb1d-4b8d-aa1f-83c7c04fa673'
```

## File: `.xo-config.js`
```javascript
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

## File: `.zuul.yml`
```yaml
ui: mocha-bdd
server: ./test/support/server.js
tunnel_host: http://focusaurus.com
browsers:
  - name: chrome
    version: latest
  - name: firefox
    version: latest
  - name: safari
    version: latest
  - name: ie
    version: 9..latest
browserify:
  - transform:
      name: babelify
      configFile: './.dist.babelrc'
```

## File: `CONTRIBUTING.md`
```markdown
When submitting a PR, your chance of acceptance increases if you do the following:

* Code style is consistent with existing in the file.
* Tests are passing (client and server).
* You add a test for the failing issue you are fixing.
* Code changes are focused on the area of discussion.
* Do not rebuild the distribution files or increment version numbers.
```

## File: `HISTORY.md`
```markdown
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
* Set default user-agent header. (bevacqua)
* Add `unset()` method for removing headers. (bevacqua)
* Update cookiejar. (missinglink)
* Fix response error formatting. (shesek)

# 0.17.0 / 2014-03-06

* supply uri malformed error to the callback (yields)
* add request event (yields)
* allow simple auth (yields)
* add request event (yields)
* switch to component/reduce (visionmedia)
* fix part content-disposition (mscdex)
* add browser testing via zuul (defunctzombie)
* adds request.use() (johntron)

# 0.16.0 / 2014-01-07

* remove support for 0.6 (superjoe30)
* fix CORS withCredentials (wejendorp)
* add "test" script (superjoe30)
* add request .accept() method (nickl-)
* add xml to mime types mappings (nickl-)
* fix parse body error on HEAD requests (gjohnson)
* fix documentation typos (matteofigus)
* fix content-type + charset (bengourley)
* fix null values on query parameters (cristiandouce)

# 0.15.7 / 2013-10-19

* pin should.js to 1.3.0 due to breaking change in 2.0.x
* fix browserify regression

# 0.15.5 / 2013-10-09

* add browser field to support browserify
* fix .field() value number support

# 0.15.4 / 2013-07-09

* node: add a Request#agent() function to set the http Agent to use

# 0.15.3 / 2013-07-05

* fix .pipe() unzipping on more recent nodes. Closes [#240](https://github.com/ladjs/superagent/issues/240)
* fix passing an empty object to .query() no longer appends "?"
* fix formidable error handling
* update formidable

# 0.15.2 / 2013-07-02

* fix: emit 'end' when piping.

# 0.15.1 / 2013-06-26

* add try/catch around parseLinks

# 0.15.0 / 2013-06-25

* make `Response#toError()` have a more meaningful `message`

# 0.14.9 / 2013-06-15

* add debug()s to the node client
* add .abort() method to node client

# 0.14.8 / 2013-06-13

* set .agent = false always
* remove X-Requested-With. Closes [#189](https://github.com/ladjs/superagent/issues/189)

# 0.14.7 / 2013-06-06

* fix unzip error handling

# 0.14.6 / 2013-05-23

* fix HEAD unzip bug

# 0.14.5 / 2013-05-23

* add flag to ensure the callback is **never** invoked twice

# 0.14.4 / 2013-05-22

* add superagent.js build output
* update qs
* update emitter-component
* revert "add browser field to support browserify" see [GH-221](https://github.com/ladjs/superagent/issues/221)

# 0.14.3 / 2013-05-18

* add browser field to support browserify

# 0.14.2/ 2013-05-07

* add host object check to fix serialization of File/Blobs etc as json

# 0.14.1 / 2013-04-09

* update qs

# 0.14.0 / 2013-04-02

* add client-side basic auth
* fix retaining of .set() header field case

# 0.13.0 / 2013-03-13

* add progress events to client
* add simple example
* add res.headers as alias of res.header for browser client
* add res.get(field) to node/client

# 0.12.4 / 2013-02-11

* fix get content-type even if can't get other headers in firefox. fixes [#181](https://github.com/ladjs/superagent/issues/181)

# 0.12.3 / 2013-02-11

* add quick "progress" event support

# 0.12.2 / 2013-02-04

* add test to check if response acts as a readable stream
* add ReadableStream in the Response prototype.
* add test to assert correct redirection when the host changes in the location header.
* add default Accept-Encoding. Closes [#155](https://github.com/ladjs/superagent/issues/155)
* fix req.pipe() return value of original stream for node parity. Closes [#171](https://github.com/ladjs/superagent/issues/171)
* remove the host header when cleaning headers to properly follow the redirection.

# 0.12.1 / 2013-01-10

* add x-domain error handling

# 0.12.0 / 2013-01-04

* add header persistence on redirects

# 0.11.0 / 2013-01-02

* add .error Error object. Closes [#156](https://github.com/ladjs/superagent/issues/156)
* add forcing of res.text removal for FF HEAD responses. Closes [#162](https://github.com/ladjs/superagent/issues/162)
* add reduce component usage. Closes [#90](https://github.com/ladjs/superagent/issues/90)
* move better-assert dep to development deps

# 0.10.0 / 2012-11-14

* add req.timeout(ms) support for the client

# 0.9.10 / 2012-11-14

* fix client-side .query(str) support

# 0.9.9 / 2012-11-14

* add .parse(fn) support
* fix socket hangup with dates in querystring. Closes [#146](https://github.com/ladjs/superagent/issues/146)
* fix socket hangup "error" event when a callback of arity 2 is provided

# 0.9.8 / 2012-11-03

* add emission of error from `Request#callback()`
* add a better fix for nodes weird socket hang up error
* add PUT/POST/PATCH data support to client short-hand functions
* add .license property to component.json
* change client portion to build using component(1)
* fix GET body support [guille]

# 0.9.7 / 2012-10-19

* fix `.buffer()` `res.text` when no parser matches

# 0.9.6 / 2012-10-17

* change: use `this` when `window` is undefined
* update to new component spec [juliangruber]
* fix emission of "data" events for compressed responses without encoding. Closes [#125](https://github.com/ladjs/superagent/issues/125)

# 0.9.5 / 2012-10-01

* add field name to .attach()
* add text "parser"
* refactor isObject()
* remove wtf isFunction() helper

# 0.9.4 / 2012-09-20

* fix `Buffer` responses [TooTallNate]
* fix `res.type` when a "type" param is present [TooTallNate]

# 0.9.3 / 2012-09-18

* remove **GET** `.send()` == `.query()` special-case (**API** change !!!)

# 0.9.2 / 2012-09-17

* add `.aborted` prop
* add `.abort()`. Closes [#115](https://github.com/ladjs/superagent/issues/115)

# 0.9.1 / 2012-09-07

* add `.forbidden` response property
* add component.json
* change emitter-component to 0.0.5
* fix client-side tests

# 0.9.0 / 2012-08-28

* add `.timeout(ms)`. Closes [#17](https://github.com/ladjs/superagent/issues/17)

# 0.8.2 / 2012-08-28

* fix pathname relative redirects. Closes [#112](https://github.com/ladjs/superagent/issues/112)

# 0.8.1 / 2012-08-21

* fix redirects when schema is specified

# 0.8.0 / 2012-08-19

* add `res.buffered` flag
* add buffering of text/\*, json and forms only by default. Closes [#61](https://github.com/ladjs/superagent/issues/61)
* add `.buffer(false)` cancellation
* add cookie jar support [hunterloftis]
* add agent functionality [hunterloftis]

# 0.7.0 / 2012-08-03

* allow `query()` to be called after the internal `req` has been created [tootallnate]

# 0.6.0 / 2012-07-17

* add `res.send('foo=bar')` default of "application/x-www-form-urlencoded"

# 0.5.1 / 2012-07-16

* add "methods" dep
* add `.end()` arity check to node callbacks
* fix unzip support due to weird node internals

# 0.5.0 / 2012-06-16

* Added "Link" response header field parsing, exposing `res.links`

# 0.4.3 / 2012-06-15

* Added 303, 305 and 307 as redirect status codes [slaskis]
* Fixed passing an object as the url

# 0.4.2 / 2012-06-02

* Added component support
* Fixed redirect data

# 0.4.1 / 2012-04-13

* Added HTTP PATCH support
* Fixed: GET / HEAD when following redirects. Closes [#86](https://github.com/ladjs/superagent/issues/86)
* Fixed Content-Length detection for multibyte chars

# 0.4.0 / 2012-03-04

* Added `.head()` method [browser]. Closes [#78](https://github.com/ladjs/superagent/issues/78)
* Added `make test-cov` support
* Added multipart request support. Closes [#11](https://github.com/ladjs/superagent/issues/11)
* Added all methods that node supports. Closes [#71](https://github.com/ladjs/superagent/issues/71)
* Added "response" event providing a Response object. Closes [#28](https://github.com/ladjs/superagent/issues/28)
* Added `.query(obj)`. Closes [#59](https://github.com/ladjs/superagent/issues/59)
* Added `res.type` (browser). Closes [#54](https://github.com/ladjs/superagent/issues/54)
* Changed: default `res.body` and `res.files` to {}
* Fixed: port existing query-string fix (browser). Closes [#57](https://github.com/ladjs/superagent/issues/57)

# 0.3.0 / 2012-01-24

* Added deflate/gzip support [guillermo]
* Added `res.type` (Content-Type void of params)
* Added `res.statusCode` to mirror node
* Added `res.headers` to mirror node
* Changed: parsers take callbacks
* Fixed optional schema support. Closes [#49](https://github.com/ladjs/superagent/issues/49)

# 0.2.0 / 2012-01-05

* Added url auth support
* Added `.auth(username, password)`
* Added basic auth support [node]. Closes [#41](https://github.com/ladjs/superagent/issues/41)
* Added `make test-docs`
* Added guillermo's EventEmitter. Closes [#16](https://github.com/ladjs/superagent/issues/16)
* Removed `Request#data()` for SS, renamed to `send()`
* Removed `Request#data()` from client, renamed to `send()`
* Fixed array support. [browser]
* Fixed array support. Closes [#35](https://github.com/ladjs/superagent/issues/35) [node]
* Fixed `EventEmitter#emit()`

# 0.1.3 / 2011-10-25

* Added error to callback
* Bumped node dep for 0.5.x

# 0.1.2 / 2011-09-24

* Added markdown documentation
* Added `request(url[, fn])` support to the client
* Added `qs` dependency to package.json
* Added options for `Request#pipe()`
* Added support for `request(url, callback)`
* Added `request(url)` as shortcut for `request.get(url)`
* Added `Request#pipe(stream)`
* Added inherit from `Stream`
* Added multipart support
* Added ssl support (node)
* Removed Content-Length field from client
* Fixed buffering, `setEncoding()` to utf8 [reported by stagas]
* Fixed "end" event when piping

# 0.1.1 / 2011-08-20

* Added `res.redirect` flag (node)
* Added redirect support (node)
* Added `Request#redirects(n)` (node)
* Added `.set(object)` header field support
* Fixed `Content-Length` support

# 0.1.0 / 2011-08-09

* Added support for multiple calls to `.data()`
* Added support for `.get(uri, obj)`
* Added GET `.data()` querystring support
* Added IE{6,7,8} support [alexyoung]

# 0.0.1 / 2011-08-05

* Initial commit



```

## File: `index.html`
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
<pre><code class="language-js"> // default order
 request.get(&#39;/user&#39;)
   .query(&#39;name=Nick&#39;)
   .query(&#39;search=Manny&#39;)
   .sortQuery()
   .then(callback)

 // customized sort function
 request.get(&#39;/user&#39;)
   .query(&#39;name=Nick&#39;)
   .query(&#39;search=Manny&#39;)
   .sortQuery((a, b) =&gt; a.length - b.length)
   .then(callback)
</code></pre>
<h2 id="tls-options">TLS options</h2>
<p>In Node.js SuperAgent supports methods to configure HTTPS requests:</p>
<ul>
<li><code>.ca()</code>: Set the CA certificate(s) to trust</li>
<li><code>.cert()</code>: Set the client certificate chain(s)</li>
<li><code>.key()</code>: Set the client private key(s)</li>
<li><code>.pfx()</code>: Set the client PFX or PKCS12 encoded private key and certificate chain</li>
<li><code>.disableTLSCerts()</code>: Does not reject expired or invalid TLS certs. Sets internally <code>rejectUnauthorized=true</code>. <em>Be warned, this method allows MITM attacks.</em></li>
</ul>
<p>For more information, see Node.js <a href="https://nodejs.org/api/https.html#https_https_request_options_callback">https.request docs</a>.</p>
<pre><code class="language-js">var key = fs.readFileSync(&#39;key.pem&#39;),
    cert = fs.readFileSync(&#39;cert.pem&#39;);

request
  .post(&#39;/client-auth&#39;)
  .key(key)
  .cert(cert)
  .then(callback);
</code></pre>
<pre><code class="language-js">var ca = fs.readFileSync(&#39;ca.cert.pem&#39;);

request
  .post(&#39;https://localhost/private-ca-server&#39;)
  .ca(ca)
  .then(res =&gt; {});
</code></pre>
<h2 id="parsing-response-bodies">Parsing response bodies</h2>
<p>SuperAgent will parse known response-body data for you,
currently supporting <code>application/x-www-form-urlencoded</code>,
<code>application/json</code>, and <code>multipart/form-data</code>. You can setup
automatic parsing for other response-body data as well:</p>
<pre><code class="language-js">//browser
request.parse[&#39;application/xml&#39;] = function (str) {
    return {&#39;object&#39;: &#39;parsed from str&#39;};
};

//node
request.parse[&#39;application/xml&#39;] = function (res, cb) {
    //parse response text and set res.body here

    cb(null, res);
};

//going forward, responses of type &#39;application/xml&#39;
//will be parsed automatically
</code></pre>
<p>You can set a custom parser (that takes precedence over built-in parsers) with the <code>.buffer(true).parse(fn)</code> method. If response buffering is not enabled (<code>.buffer(false)</code>) then the <code>response</code> event will be emitted without waiting for the body parser to finish, so <code>response.body</code> won&#39;t be available.</p>
<h3 id="json--urlencoded">JSON / Urlencoded</h3>
<p>The property <code>res.body</code> is the parsed object, for example if a request responded with the JSON string &#39;{&quot;user&quot;:{&quot;name&quot;:&quot;tobi&quot;}}&#39;, <code>res.body.user.name</code> would be &quot;tobi&quot;. Likewise the x-www-form-urlencoded value of &quot;user[name]=tobi&quot; would yield the same result. Only one level of nesting is supported. If you need more complex data, send JSON instead.</p>
<p>Arrays are sent by repeating the key. <code>.send({color: [&#39;red&#39;,&#39;blue&#39;]})</code> sends <code>color=red&amp;color=blue</code>. If you want the array keys to contain <code>[]</code> in their name, you must add it yourself, as SuperAgent doesn&#39;t add it automatically.</p>
<h3 id="multipart">Multipart</h3>
<p>The Node client supports <em>multipart/form-data</em> via the <a href="https://github.com/felixge/node-formidable">Formidable</a> module. When parsing multipart responses, the object <code>res.files</code> is also available to you. Suppose for example a request responds with the following multipart body:</p>
<pre><code>--whoop
Content-Disposition: attachment; name=&quot;image&quot;; filename=&quot;tobi.png&quot;
Content-Type: image/png

... data here ...
--whoop
Content-Disposition: form-data; name=&quot;name&quot;
Content-Type: text/plain

Tobi
--whoop--
</code></pre>
<p>You would have the values <code>res.body.name</code> provided as &quot;Tobi&quot;, and <code>res.files.image</code> as a <code>File</code> object containing the path on disk, filename, and other properties.</p>
<h3 id="binary">Binary</h3>
<p>In browsers, you may use <code>.responseType(&#39;blob&#39;)</code> to request handling of binary response bodies. This API is unnecessary when running in node.js. The supported argument values for this method are</p>
<ul>
<li><code>&#39;blob&#39;</code> passed through to the XmlHTTPRequest <code>responseType</code> property</li>
<li><code>&#39;arraybuffer&#39;</code> passed through to the XmlHTTPRequest <code>responseType</code> property</li>
</ul>
<pre><code class="language-js">req.get(&#39;/binary.data&#39;)
  .responseType(&#39;blob&#39;)
  .then(res =&gt; {
    // res.body will be a browser native Blob type here
  });
</code></pre>
<p>For more information, see the Mozilla Developer Network <a href="https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/responseType">xhr.responseType docs</a>.</p>
<h2 id="response-properties">Response properties</h2>
<p>Many helpful flags and properties are set on the <code>Response</code> object, ranging from the response text, parsed response body, header fields, status flags and more.</p>
<h3 id="response-text">Response text</h3>
<p>The <code>res.text</code> property contains the unparsed response body string. This property is always present for the client API, and only when the mime type matches &quot;text/<em>&quot;, &quot;</em>/json&quot;, or &quot;x-www-form-urlencoded&quot; by default for node. The reasoning is to conserve memory, as buffering text of large bodies such as multipart files or images is extremely inefficient. To force buffering see the &quot;Buffering responses&quot; section.</p>
<h3 id="response-body">Response body</h3>
<p>Much like SuperAgent can auto-serialize request data, it can also automatically parse it. When a parser is defined for the Content-Type, it is parsed, which by default includes &quot;application/json&quot; and &quot;application/x-www-form-urlencoded&quot;. The parsed object is then available via <code>res.body</code>.</p>
<h3 id="response-header-fields">Response header fields</h3>
<p>The <code>res.header</code> contains an object of parsed header fields, lowercasing field names much like node does. For example <code>res.header[&#39;content-length&#39;]</code>.</p>
<h3 id="response-content-type">Response Content-Type</h3>
<p>The Content-Type response header is special-cased, providing <code>res.type</code>, which is void of the charset (if any). For example the Content-Type of &quot;text/html; charset=utf8&quot; will provide &quot;text/html&quot; as <code>res.type</code>, and the <code>res.charset</code> property would then contain &quot;utf8&quot;.</p>
<h3 id="response-status">Response status</h3>
<p>The response status flags help determine if the request was a success, among other useful information, making SuperAgent ideal for interacting with RESTful web services. These flags are currently defined as:</p>
<pre><code class="language-javascript">     var type = status / 100 | 0;

     // status / class
     res.status = status;
     res.statusType = type;

     // basics
     res.info = 1 == type;
     res.ok = 2 == type;
     res.clientError = 4 == type;
     res.serverError = 5 == type;
     res.error = 4 == type || 5 == type;

     // sugar
     res.accepted = 202 == status;
     res.noContent = 204 == status || 1223 == status;
     res.badRequest = 400 == status;
     res.unauthorized = 401 == status;
     res.notAcceptable = 406 == status;
     res.notFound = 404 == status;
     res.forbidden = 403 == status;
</code></pre>
<h2 id="aborting-requests">Aborting requests</h2>
<p>To abort requests simply invoke the <code>req.abort()</code> method.</p>
<h2 id="timeouts">Timeouts</h2>
<p>Sometimes networks and servers get &quot;stuck&quot; and never respond after accepting a request. Set timeouts to avoid requests waiting forever.</p>
<ul>
<li><p><code>req.timeout({deadline:ms})</code> or <code>req.timeout(ms)</code> (where <code>ms</code> is a number of milliseconds &gt; 0) sets a deadline for the entire request (including all uploads, redirects, server processing time) to complete. If the response isn&#39;t fully downloaded within that time, the request will be aborted.</p>
</li>
<li><p><code>req.timeout({response:ms})</code> sets maximum time to wait for the first byte to arrive from the server, but it does not limit how long the entire download can take. Response timeout should be at least few seconds longer than just the time it takes the server to respond, because it also includes time to make DNS lookup, TCP/IP and TLS connections, and time to upload request data.</p>
</li>
</ul>
<p>You should use both <code>deadline</code> and <code>response</code> timeouts. This way you can use a short response timeout to detect unresponsive networks quickly, and a long deadline to give time for downloads on slow, but reliable, networks. Note that both of these timers limit how long <em>uploads</em> of attached files are allowed to take. Use long timeouts if you&#39;re uploading files.</p>
<pre><code class="language-javascript">    request
      .get(&#39;/big-file?network=slow&#39;)
      .timeout({
        response: 5000,  // Wait 5 seconds for the server to start sending,
        deadline: 60000, // but allow 1 minute for the file to finish loading.
      })
      .then(res =&gt; {
          /* responded in time */
        }, err =&gt; {
          if (err.timeout) { /* timed out! */ } else { /* other error */ }
      });
</code></pre>
<p>Timeout errors have a <code>.timeout</code> property.</p>
<h2 id="authentication">Authentication</h2>
<p>In both Node and browsers auth available via the <code>.auth()</code> method:</p>
<pre><code class="language-javascript">    request
      .get(&#39;http://local&#39;)
      .auth(&#39;tobi&#39;, &#39;learnboost&#39;)
      .then(callback);
</code></pre>
<p>In the <em>Node</em> client Basic auth can be in the URL as &quot;user:pass&quot;:</p>
<pre><code class="language-javascript">    request.get(&#39;http://tobi:learnboost@local&#39;).then(callback);
</code></pre>
<p>By default only <code>Basic</code> auth is used. In browser you can add <code>{type:&#39;auto&#39;}</code> to enable all methods built-in in the browser (Digest, NTLM, etc.):</p>
<pre><code class="language-javascript">    request.auth(&#39;digest&#39;, &#39;secret&#39;, {type:&#39;auto&#39;})
</code></pre>
<p>The <code>auth</code> method also supports a <code>type</code> of <code>bearer</code>, to specify token-based authentication:</p>
<pre><code class="language-javascript">    request.auth(&#39;my_token&#39;, { type: &#39;bearer&#39; })
</code></pre>
<h2 id="following-redirects">Following redirects</h2>
<p>By default up to 5 redirects will be followed, however you may specify this with the <code>res.redirects(n)</code> method:</p>
<pre><code class="language-javascript">    const response = await request.get(&#39;/some.png&#39;).redirects(2);
</code></pre>
<p>Redirects exceeding the limit are treated as errors. Use <code>.ok(res =&gt; res.status &lt; 400)</code> to read them as successful responses.</p>
<h2 id="agents-for-global-state">Agents for global state</h2>
<h3 id="saving-cookies">Saving cookies</h3>
<p>In Node SuperAgent does not save cookies by default, but you can use the <code>.agent()</code> method to create a copy of SuperAgent that saves cookies. Each copy has a separate cookie jar.</p>
<pre><code class="language-javascript">    const agent = request.agent();
    agent
      .post(&#39;/login&#39;)
      .then(() =&gt; {
        return agent.get(&#39;/cookied-page&#39;);
      });
</code></pre>
<p>In browsers cookies are managed automatically by the browser, so the <code>.agent()</code> does not isolate cookies.</p>
<h3 id="default-options-for-multiple-requests">Default options for multiple requests</h3>
<p>Regular request methods called on the agent will be used as defaults for all requests made by that agent.</p>
<pre><code class="language-javascript">    const agent = request.agent()
      .use(plugin)
      .auth(shared);

    await agent.get(&#39;/with-plugin-and-auth&#39;);
    await agent.get(&#39;/also-with-plugin-and-auth&#39;);
</code></pre>
<p>The complete list of methods that the agent can use to set defaults is: <code>use</code>, <code>on</code>, <code>once</code>, <code>set</code>, <code>query</code>, <code>type</code>, <code>accept</code>, <code>auth</code>, <code>withCredentials</code>, <code>sortQuery</code>, <code>retry</code>, <code>ok</code>, <code>redirects</code>, <code>timeout</code>, <code>buffer</code>, <code>serialize</code>, <code>parse</code>, <code>ca</code>, <code>key</code>, <code>pfx</code>, <code>cert</code>.</p>
<h2 id="piping-data">Piping data</h2>
<p>The Node client allows you to pipe data to and from the request. Please note that <code>.pipe()</code> is used <strong>instead of</strong> <code>.end()</code>/<code>.then()</code> methods.</p>
<p>For example piping a file&#39;s contents as the request:</p>
<pre><code class="language-javascript">    const request = require(&#39;superagent&#39;);
    const fs = require(&#39;fs&#39;);

    const stream = fs.createReadStream(&#39;path/to/my.json&#39;);
    const req = request.post(&#39;/somewhere&#39;);
    req.type(&#39;json&#39;);
    stream.pipe(req);
</code></pre>
<p>Note that when you pipe to a request, superagent sends the piped data with <a href="https://en.wikipedia.org/wiki/Chunked_transfer_encoding">chunked transfer encoding</a>, which isn&#39;t supported by all servers (for instance, Python WSGI servers).</p>
<p>Or piping the response to a file:</p>
<pre><code class="language-javascript">    const stream = fs.createWriteStream(&#39;path/to/my.json&#39;);
    const req = request.get(&#39;/some.json&#39;);
    req.pipe(stream);
</code></pre>
<p> It&#39;s not possible to mix pipes and callbacks or promises. Note that you should <strong>NOT</strong> attempt to pipe the result of <code>.end()</code> or the <code>Response</code> object:</p>
<pre><code class="language-javascript">    // Don&#39;t do either of these:
    const stream = getAWritableStream();
    const req = request
      .get(&#39;/some.json&#39;)
      // BAD: this pipes garbage to the stream and fails in unexpected ways
      .end((err, this_does_not_work) =&gt; this_does_not_work.pipe(stream))
    const req = request
      .get(&#39;/some.json&#39;)
      .end()
      // BAD: this is also unsupported, .pipe calls .end for you.
      .pipe(nope_its_too_late);
</code></pre>
<p>In a <a href="https://github.com/ladjs/superagent/issues/1188">future version</a> of superagent, improper calls to <code>pipe()</code> will fail.</p>
<h2 id="multipart-requests">Multipart requests</h2>
<p>SuperAgent is also great for <em>building</em> multipart requests for which it provides methods <code>.attach()</code> and <code>.field()</code>.</p>
<p>When you use <code>.field()</code> or <code>.attach()</code> you can&#39;t use <code>.send()</code> and you <em>must not</em> set <code>Content-Type</code> (the correct type will be set for you).</p>
<h3 id="attaching-files">Attaching files</h3>
<p>To send a file use <code>.attach(name, [file], [options])</code>. You can attach multiple files by calling <code>.attach</code> multiple times. The arguments are:</p>
<ul>
<li><code>name</code> — field name in the form.</li>
<li><code>file</code> — either string with file path or <code>Blob</code>/<code>Buffer</code> object.</li>
<li><code>options</code> — (optional) either string with custom file name or <code>{filename: string}</code> object. In Node also <code>{contentType: &#39;mime/type&#39;}</code> is supported. In browser create a <code>Blob</code> with an appropriate type instead.</li>
</ul>
<br>

<pre><code class="language-javascript">    request
      .post(&#39;/upload&#39;)
      .attach(&#39;image1&#39;, &#39;path/to/felix.jpeg&#39;)
      .attach(&#39;image2&#39;, imageBuffer, &#39;luna.jpeg&#39;)
      .field(&#39;caption&#39;, &#39;My cats&#39;)
      .then(callback);
</code></pre>
<h3 id="field-values">Field values</h3>
<p>Much like form fields in HTML, you can set field values with <code>.field(name, value)</code> and <code>.field({name: value})</code>. Suppose you want to upload a few images with your name and email, your request might look something like this:</p>
<pre><code class="language-javascript">     request
       .post(&#39;/upload&#39;)
       .field(&#39;user[name]&#39;, &#39;Tobi&#39;)
       .field(&#39;user[email]&#39;, &#39;tobi@learnboost.com&#39;)
       .field(&#39;friends[]&#39;, [&#39;loki&#39;, &#39;jane&#39;])
       .attach(&#39;image&#39;, &#39;path/to/tobi.png&#39;)
       .then(callback);
</code></pre>
<h2 id="compression">Compression</h2>
<p>The node client supports compressed responses, best of all, you don&#39;t have to do anything! It just works.</p>
<h2 id="buffering-responses">Buffering responses</h2>
<p>To force buffering of response bodies as <code>res.text</code> you may invoke <code>req.buffer()</code>. To undo the default of buffering for text responses such as &quot;text/plain&quot;, &quot;text/html&quot; etc you may invoke <code>req.buffer(false)</code>.</p>
<p>When buffered the <code>res.buffered</code> flag is provided, you may use this to handle both buffered and unbuffered responses in the same callback.</p>
<h2 id="cors">CORS</h2>
<p>For security reasons, browsers will block cross-origin requests unless the server opts-in using CORS headers. Browsers will also make extra <strong>OPTIONS</strong> requests to check what HTTP headers and methods are allowed by the server. <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS">Read more about CORS</a>.</p>
<p>The <code>.withCredentials()</code> method enables the ability to send cookies from the origin, however only when <code>Access-Control-Allow-Origin</code> is <em>not</em> a wildcard (&quot;*&quot;), and <code>Access-Control-Allow-Credentials</code> is &quot;true&quot;.</p>
<pre><code class="language-javascript">    request
      .get(&#39;https://api.example.com:4001/&#39;)
      .withCredentials()
      .then(res =&gt; {
        assert.equal(200, res.status);
        assert.equal(&#39;tobi&#39;, res.text);
      })
</code></pre>
<h2 id="error-handling">Error handling</h2>
<p>Your callback function will always be passed two arguments: error and response. If no error occurred, the first argument will be null:</p>
<pre><code class="language-javascript">    request
     .post(&#39;/upload&#39;)
     .attach(&#39;image&#39;, &#39;path/to/tobi.png&#39;)
     .then(res =&gt; {

     });
</code></pre>
<p>An &quot;error&quot; event is also emitted, with you can listen for:</p>
<pre><code class="language-javascript">    request
      .post(&#39;/upload&#39;)
      .attach(&#39;image&#39;, &#39;path/to/tobi.png&#39;)
      .on(&#39;error&#39;, handle)
      .then(res =&gt; {

      });
</code></pre>
<p>Note that <strong>superagent considers 4xx and 5xx responses (as well as unhandled 3xx responses) errors by default</strong>. For example, if you get a <code>304 Not modified</code>, <code>403 Forbidden</code> or <code>500 Internal server error</code> response, this status information will be available via <code>err.status</code>. Errors from such responses also contain an <code>err.response</code> field with all of the properties mentioned in &quot;<a href="#response-properties">Response properties</a>&quot;. The library behaves in this way to handle the common case of wanting success responses and treating HTTP error status codes as errors while still allowing for custom logic around specific error conditions.</p>
<p>Network failures, timeouts, and other errors that produce no response will contain no <code>err.status</code> or <code>err.response</code> fields.</p>
<p>If you wish to handle 404 or other HTTP error responses, you can query the <code>err.status</code> property. When an HTTP error occurs (4xx or 5xx response) the <code>res.error</code> property is an <code>Error</code> object, this allows you to perform checks such as:</p>
<pre><code class="language-javascript">    if (err &amp;&amp; err.status === 404) {
      alert(&#39;oh no &#39; + res.body.message);
    }
    else if (err) {
      // all other error types we handle generically
    }
</code></pre>
<p>Alternatively, you can use the <code>.ok(callback)</code> method to decide whether a response is an error or not. The callback to the <code>ok</code> function gets a response and returns <code>true</code> if the response should be interpreted as success.</p>
<pre><code class="language-javascript">    request.get(&#39;/404&#39;)
      .ok(res =&gt; res.status &lt; 500)
      .then(response =&gt; {
        // reads 404 page as a successful response
      })
</code></pre>
<h2 id="progress-tracking">Progress tracking</h2>
<p>SuperAgent fires <code>progress</code> events on upload and download of large files.</p>
<pre><code class="language-javascript">    request.post(url)
      .attach(&#39;field_name&#39;, file)
      .on(&#39;progress&#39;, event =&gt; {
        /* the event is:
        {
          direction: &quot;upload&quot; or &quot;download&quot;
          percent: 0 to 100 // may be missing if file size is unknown
          total: // total file size, may be missing
          loaded: // bytes downloaded or uploaded so far
        } */
      })
      .then()
</code></pre>
<h2 id="testing-on-localhost">Testing on localhost</h2>
<h3 id="forcing-specific-connection-ip-address">Forcing specific connection IP address</h3>
<p>In Node.js it&#39;s possible to ignore DNS resolution and direct all requests to a specific IP address using <code>.connect()</code> method. For example, this request will go to localhost instead of <code>example.com</code>:</p>
<pre><code class="language-javascript">    const res = await request.get(&quot;http://example.com&quot;).connect(&quot;127.0.0.1&quot;);
</code></pre>
<p>Because the request may be redirected, it&#39;s possible to specify multiple hostnames and multiple IPs, as well as a special <code>*</code> as the fallback (note: other wildcards are not supported). The requests will keep their <code>Host</code> header with the original value. <code>.connect(undefined)</code> turns off the feature.</p>
<pre><code class="language-javascript">    const res = await request.get(&quot;http://redir.example.com:555&quot;)
      .connect({
        &quot;redir.example.com&quot;: &quot;127.0.0.1&quot;, // redir.example.com:555 will use 127.0.0.1:555
        &quot;www.example.com&quot;: false, // don&#39;t override this one; use DNS as normal
        &quot;mapped.example.com&quot;: { host: &quot;127.0.0.1&quot;, port: 8080}, // mapped.example.com:* will use 127.0.0.1:8080
        &quot;*&quot;: &quot;proxy.example.com&quot;, // all other requests will go to this host
      });
</code></pre>
<h3 id="ignoring-brokeninsecure-https-on-localhost">Ignoring broken/insecure HTTPS on localhost</h3>
<p>In Node.js, when HTTPS is misconfigured and insecure (e.g. using self-signed certificate <em>without</em> specifying own <code>.ca()</code>), it&#39;s still possible to permit requests to <code>localhost</code> by calling <code>.trustLocalhost()</code>:</p>
<pre><code class="language-javascript">    const res = await request.get(&quot;https://localhost&quot;).trustLocalhost()
</code></pre>
<p>Together with <code>.connect(&quot;127.0.0.1&quot;)</code> this may be used to force HTTPS requests to any domain to be re-routed to <code>localhost</code> instead.</p>
<p>It&#39;s generally safe to ignore broken HTTPS on <code>localhost</code>, because the loopback interface is not exposed to untrusted networks. Trusting <code>localhost</code> may become the default in the future. Use <code>.trustLocalhost(false)</code> to force check of <code>127.0.0.1</code>&#39;s authenticity.</p>
<p>We intentionally don&#39;t support disabling of HTTPS security when making requests to any other IP, because such options end up abused as a quick &quot;fix&quot; for HTTPS problems. You can get free HTTPS certificates from <a href="https://certbot.eff.org">Let&#39;s Encrypt</a> or set your own CA (<code>.ca(ca_public_pem)</code>) to make your self-signed certificates trusted.</p>
<h2 id="promise-and-generator-support">Promise and Generator support</h2>
<p>SuperAgent&#39;s request is a &quot;thenable&quot; object that&#39;s compatible with JavaScript promises and the <code>async</code>/<code>await</code> syntax.</p>
<pre><code class="language-javascript">    const res = await request.get(url);
</code></pre>
<p>If you&#39;re using promises, <strong>do not</strong> call <code>.end()</code> or <code>.pipe()</code>. Any use of <code>.then()</code> or <code>await</code> disables all other ways of using the request.</p>
<p>Libraries like <a href="https://github.com/tj/co">co</a> or a web framework like <a href="https://github.com/koajs/koa">koa</a> can <code>yield</code> on any SuperAgent method:</p>
<pre><code class="language-javascript">    const req = request
      .get(&#39;http://local&#39;)
      .auth(&#39;tobi&#39;, &#39;learnboost&#39;);
    const res = yield req;
</code></pre>
<p>Note that SuperAgent expects the global <code>Promise</code> object to be present. You&#39;ll need to use v7 and a polyfill to use promises in Internet Explorer or Node.js 0.10.</p>
<p>We have dropped support in v8 for IE.  You must add a polyfill for WeakRef and BigInt if you wish to support Opera 85, iOS Safari 12.2-12.5, for example using <a href="https://cdnjs.cloudflare.com/polyfill/">https://cdnjs.cloudflare.com/polyfill/</a>:</p>
<pre><code class="language-html">&lt;script src=&quot;https://cdnjs.cloudflare.com/polyfill/v3/polyfill.min.js?features=WeakRef,BigInt&quot;&gt;&lt;/script&gt;
</code></pre>
<h2 id="browser-and-node-versions">Browser and node versions</h2>
<p>SuperAgent has two implementations: one for web browsers (using XHR) and one for Node.JS (using core http module). By default Browserify and WebPack will pick the browser version.</p>
<p>If want to use WebPack to compile code for Node.JS, you <em>must</em> specify <a href="https://webpack.github.io/docs/configuration.html#target">node target</a> in its configuration.</p>

    </div>
    <a href="http://github.com/ladjs/superagent"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://s3.amazonaws.com/github/ribbons/forkme_right_white_ffffff.png" alt="Fork me on GitHub"></a>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.0/jquery.min.js"></script>
    <script>
      $('code').each(function(){
        $(this).html(highlight($(this).text()));
      });

      function highlight(js) {
        return js
          .replace(/</g, '&lt;')
          .replace(/>/g, '&gt;')
          .replace(/('.*?')/gm, '<span class="string">$1</span>')
          .replace(/(\d+\.\d+)/gm, '<span class="number">$1</span>')
          .replace(/(\d+)/gm, '<span class="number">$1</span>')
          .replace(/\bnew *(\w+)/gm, '<span class="keyword">new</span> <span class="init">$1</span>')
          .replace(/\b(function|new|throw|return|var|if|else)\b/gm, '<span class="keyword">$1</span>')
      }
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/tocbot/3.0.0/tocbot.js"></script>
    <script>
      // Only use tocbot for main docs, not test docs
      if (document.querySelector('#superagent')) {
        tocbot.init({
          // Where to render the table of contents.
          tocSelector: '#menu',
          // Where to grab the headings to build the table of contents.
          contentSelector: '#content',
          // Which headings to grab inside of the contentSelector element.
          headingSelector: 'h2',
          smoothScroll: false
        });
      }
    </script>
  </body>
</html>
```

## File: `LICENSE`
```
(The MIT License)

Copyright (c) 2014-2016 TJ Holowaychuk <tj@vision-media.ca>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `Makefile`
```
OLDNODETESTS ?= lib/node/test/*.js lib/node/test/node/*.js
NODETESTS ?= test/*.js test/node/*.js
BROWSERTESTS ?= test/*.js test/client/*.js
REPORTER = spec

ifeq ("$(OLD_NODE_TEST)", "1")
	NODETESTS := $(OLDNODETESTS)
endif

test:
	@if [ "$(BROWSER)" = "1" ]; then \
		echo test on browser; \
		make test-browser; \
	fi \

	@if [ "$(NODE_TEST)" = "1" ] || [ "x$(BROWSER)" = "x" ]; then \
    echo test on node with http1; \
    export HTTP2_TEST="" && make test-node; \
    if [ "$(HTTP2_TEST_DISABLED)" != "1" ]; then \
      echo test on node with http2; \
      export HTTP2_TEST="1" && make test-node; \
    fi \
	fi

copy:
	@if [ "$(OLD_NODE_TEST)" = "1" ]; then \
		echo test on old node; \
		cp test/node/fixtures lib/node/test/node -rf; \
	else \
		echo test on plain node; \
	fi

test-node:copy
	@NODE_ENV=test HTTP2_TEST=$(HTTP2_TEST) ./node_modules/.bin/nyc ./node_modules/.bin/mocha \
		--require should \
		--trace-warnings \
		--throw-deprecation \
		--reporter $(REPORTER) \
		--slow 2000 \
		--timeout 5000 \
		--exit \
		$(NODETESTS)

test-cov: lib-cov
	SUPERAGENT_COV=1 $(MAKE) test REPORTER=html-cov > coverage.html

test-browser:
	SAUCE_APPIUM_VERSION=1.7 ./node_modules/.bin/zuul -- $(BROWSERTESTS)

test-browser-local:
	./node_modules/.bin/zuul --no-coverage --local 4000 -- $(BROWSERTESTS)

lib-cov:
	jscoverage lib lib-cov

test-server:
	@node test/server

docs: index.html test-docs docs/index.md

index.html: docs/index.md docs/head.html docs/tail.html
	marked < $< \
		| cat docs/head.html - docs/tail.html \
		> $@

docclean:
	rm -f index.html docs/test.html

test-docs: docs/head.html docs/tail.html
	make test REPORTER=doc \
		| cat docs/head.html - docs/tail.html \
		> docs/test.html

clean:
	rm -fr components

.PHONY: copy test-cov test docs test-docs clean test-browser-local
```

## File: `package.json`
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

## File: `README.md`
```markdown
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

## File: `SECURITY.md`
```markdown
# Security Policy


## Reporting a Vulnerability

Please report security issues to `niftylettuce@gmail.com`
```

## File: `ci/remove-deps-4-old-node.js`
```javascript
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

## File: `docs/head.html`
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

## File: `docs/index.md`
```markdown

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

### Response text

The `res.text` property contains the unparsed response body string. This property is always present for the client API, and only when the mime type matches "text/*", "*/json", or "x-www-form-urlencoded" by default for node. The reasoning is to conserve memory, as buffering text of large bodies such as multipart files or images is extremely inefficient. To force buffering see the "Buffering responses" section.

### Response body

Much like SuperAgent can auto-serialize request data, it can also automatically parse it. When a parser is defined for the Content-Type, it is parsed, which by default includes "application/json" and "application/x-www-form-urlencoded". The parsed object is then available via `res.body`.

### Response header fields

The `res.header` contains an object of parsed header fields, lowercasing field names much like node does. For example `res.header['content-length']`.

### Response Content-Type

The Content-Type response header is special-cased, providing `res.type`, which is void of the charset (if any). For example the Content-Type of "text/html; charset=utf8" will provide "text/html" as `res.type`, and the `res.charset` property would then contain "utf8".

### Response status

The response status flags help determine if the request was a success, among other useful information, making SuperAgent ideal for interacting with RESTful web services. These flags are currently defined as:

```javascript
     var type = status / 100 | 0;

     // status / class
     res.status = status;
     res.statusType = type;

     // basics
     res.info = 1 == type;
     res.ok = 2 == type;
     res.clientError = 4 == type;
     res.serverError = 5 == type;
     res.error = 4 == type || 5 == type;

     // sugar
     res.accepted = 202 == status;
     res.noContent = 204 == status || 1223 == status;
     res.badRequest = 400 == status;
     res.unauthorized = 401 == status;
     res.notAcceptable = 406 == status;
     res.notFound = 404 == status;
     res.forbidden = 403 == status;
```

## Aborting requests

To abort requests simply invoke the `req.abort()` method.

## Timeouts

Sometimes networks and servers get "stuck" and never respond after accepting a request. Set timeouts to avoid requests waiting forever.

  * `req.timeout({deadline:ms})` or `req.timeout(ms)` (where `ms` is a number of milliseconds > 0) sets a deadline for the entire request (including all uploads, redirects, server processing time) to complete. If the response isn't fully downloaded within that time, the request will be aborted.

  * `req.timeout({response:ms})` sets maximum time to wait for the first byte to arrive from the server, but it does not limit how long the entire download can take. Response timeout should be at least few seconds longer than just the time it takes the server to respond, because it also includes time to make DNS lookup, TCP/IP and TLS connections, and time to upload request data.

You should use both `deadline` and `response` timeouts. This way you can use a short response timeout to detect unresponsive networks quickly, and a long deadline to give time for downloads on slow, but reliable, networks. Note that both of these timers limit how long *uploads* of attached files are allowed to take. Use long timeouts if you're uploading files.

```javascript
    request
      .get('/big-file?network=slow')
      .timeout({
        response: 5000,  // Wait 5 seconds for the server to start sending,
        deadline: 60000, // but allow 1 minute for the file to finish loading.
      })
      .then(res => {
          /* responded in time */
        }, err => {
          if (err.timeout) { /* timed out! */ } else { /* other error */ }
      });
```

Timeout errors have a `.timeout` property.

## Authentication

In both Node and browsers auth available via the `.auth()` method:

```javascript
    request
      .get('http://local')
      .auth('tobi', 'learnboost')
      .then(callback);
```

In the _Node_ client Basic auth can be in the URL as "user:pass":

```javascript
    request.get('http://tobi:learnboost@local').then(callback);
```

By default only `Basic` auth is used. In browser you can add `{type:'auto'}` to enable all methods built-in in the browser (Digest, NTLM, etc.):

```javascript
    request.auth('digest', 'secret', {type:'auto'})
```

The `auth` method also supports a `type` of `bearer`, to specify token-based authentication:

```javascript
    request.auth('my_token', { type: 'bearer' })
```

## Following redirects

By default up to 5 redirects will be followed, however you may specify this with the `res.redirects(n)` method:

```javascript
    const response = await request.get('/some.png').redirects(2);
```

Redirects exceeding the limit are treated as errors. Use `.ok(res => res.status < 400)` to read them as successful responses.

## Agents for global state

### Saving cookies

In Node SuperAgent does not save cookies by default, but you can use the `.agent()` method to create a copy of SuperAgent that saves cookies. Each copy has a separate cookie jar.

```javascript
    const agent = request.agent();
    agent
      .post('/login')
      .then(() => {
        return agent.get('/cookied-page');
      });
```

In browsers cookies are managed automatically by the browser, so the `.agent()` does not isolate cookies.

### Default options for multiple requests

Regular request methods called on the agent will be used as defaults for all requests made by that agent.

```javascript
    const agent = request.agent()
      .use(plugin)
      .auth(shared);

    await agent.get('/with-plugin-and-auth');
    await agent.get('/also-with-plugin-and-auth');
```

The complete list of methods that the agent can use to set defaults is: `use`, `on`, `once`, `set`, `query`, `type`, `accept`, `auth`, `withCredentials`, `sortQuery`, `retry`, `ok`, `redirects`, `timeout`, `buffer`, `serialize`, `parse`, `ca`, `key`, `pfx`, `cert`.

## Piping data

The Node client allows you to pipe data to and from the request. Please note that `.pipe()` is used **instead of** `.end()`/`.then()` methods.

For example piping a file's contents as the request:

```javascript
    const request = require('superagent');
    const fs = require('fs');

    const stream = fs.createReadStream('path/to/my.json');
    const req = request.post('/somewhere');
    req.type('json');
    stream.pipe(req);
```

Note that when you pipe to a request, superagent sends the piped data with [chunked transfer encoding](https://en.wikipedia.org/wiki/Chunked_transfer_encoding), which isn't supported by all servers (for instance, Python WSGI servers).

Or piping the response to a file:

```javascript
    const stream = fs.createWriteStream('path/to/my.json');
    const req = request.get('/some.json');
    req.pipe(stream);
```

 It's not possible to mix pipes and callbacks or promises. Note that you should **NOT** attempt to pipe the result of `.end()` or the `Response` object:

```javascript
    // Don't do either of these:
    const stream = getAWritableStream();
    const req = request
      .get('/some.json')
      // BAD: this pipes garbage to the stream and fails in unexpected ways
      .end((err, this_does_not_work) => this_does_not_work.pipe(stream))
    const req = request
      .get('/some.json')
      .end()
      // BAD: this is also unsupported, .pipe calls .end for you.
      .pipe(nope_its_too_late);
```

In a [future version](https://github.com/ladjs/superagent/issues/1188) of superagent, improper calls to `pipe()` will fail.

## Multipart requests

SuperAgent is also great for _building_ multipart requests for which it provides methods `.attach()` and `.field()`.

When you use `.field()` or `.attach()` you can't use `.send()` and you *must not* set `Content-Type` (the correct type will be set for you).

### Attaching files

To send a file use `.attach(name, [file], [options])`. You can attach multiple files by calling `.attach` multiple times. The arguments are:

 * `name` — field name in the form.
 * `file` — either string with file path or `Blob`/`Buffer` object.
 * `options` — (optional) either string with custom file name or `{filename: string}` object. In Node also `{contentType: 'mime/type'}` is supported. In browser create a `Blob` with an appropriate type instead.

<br>

```javascript
    request
      .post('/upload')
      .attach('image1', 'path/to/felix.jpeg')
      .attach('image2', imageBuffer, 'luna.jpeg')
      .field('caption', 'My cats')
      .then(callback);
```

### Field values

Much like form fields in HTML, you can set field values with `.field(name, value)` and `.field({name: value})`. Suppose you want to upload a few images with your name and email, your request might look something like this:

```javascript
     request
       .post('/upload')
       .field('user[name]', 'Tobi')
       .field('user[email]', 'tobi@learnboost.com')
       .field('friends[]', ['loki', 'jane'])
       .attach('image', 'path/to/tobi.png')
       .then(callback);
```

## Compression

The node client supports compressed responses, best of all, you don't have to do anything! It just works.

## Buffering responses

To force buffering of response bodies as `res.text` you may invoke `req.buffer()`. To undo the default of buffering for text responses such as "text/plain", "text/html" etc you may invoke `req.buffer(false)`.

When buffered the `res.buffered` flag is provided, you may use this to handle both buffered and unbuffered responses in the same callback.

## CORS

For security reasons, browsers will block cross-origin requests unless the server opts-in using CORS headers. Browsers will also make extra __OPTIONS__ requests to check what HTTP headers and methods are allowed by the server. [Read more about CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS).

The `.withCredentials()` method enables the ability to send cookies from the origin, however only when `Access-Control-Allow-Origin` is _not_ a wildcard ("*"), and `Access-Control-Allow-Credentials` is "true".

```javascript
    request
      .get('https://api.example.com:4001/')
      .withCredentials()
      .then(res => {
        assert.equal(200, res.status);
        assert.equal('tobi', res.text);
      })
```

## Error handling

Your callback function will always be passed two arguments: error and response. If no error occurred, the first argument will be null:

```javascript
    request
     .post('/upload')
     .attach('image', 'path/to/tobi.png')
     .then(res => {

     });
```

An "error" event is also emitted, with you can listen for:

```javascript
    request
      .post('/upload')
      .attach('image', 'path/to/tobi.png')
      .on('error', handle)
      .then(res => {

      });
```

Note that **superagent considers 4xx and 5xx responses (as well as unhandled 3xx responses) errors by default**. For example, if you get a `304 Not modified`, `403 Forbidden` or `500 Internal server error` response, this status information will be available via `err.status`. Errors from such responses also contain an `err.response` field with all of the properties mentioned in "[Response properties](#response-properties)". The library behaves in this way to handle the common case of wanting success responses and treating HTTP error status codes as errors while still allowing for custom logic around specific error conditions.

Network failures, timeouts, and other errors that produce no response will contain no `err.status` or `err.response` fields.

If you wish to handle 404 or other HTTP error responses, you can query the `err.status` property. When an HTTP error occurs (4xx or 5xx response) the `res.error` property is an `Error` object, this allows you to perform checks such as:

```javascript
    if (err && err.status === 404) {
      alert('oh no ' + res.body.message);
    }
    else if (err) {
      // all other error types we handle generically
    }
```

Alternatively, you can use the `.ok(callback)` method to decide whether a response is an error or not. The callback to the `ok` function gets a response and returns `true` if the response should be interpreted as success.

```javascript
    request.get('/404')
      .ok(res => res.status < 500)
      .then(response => {
        // reads 404 page as a successful response
      })
```

## Progress tracking

SuperAgent fires `progress` events on upload and download of large files.

```javascript
    request.post(url)
      .attach('field_name', file)
      .on('progress', event => {
        /* the event is:
        {
          direction: "upload" or "download"
          percent: 0 to 100 // may be missing if file size is unknown
          total: // total file size, may be missing
          loaded: // bytes downloaded or uploaded so far
        } */
      })
      .then()
```

## Testing on localhost

### Forcing specific connection IP address

In Node.js it's possible to ignore DNS resolution and direct all requests to a specific IP address using `.connect()` method. For example, this request will go to localhost instead of `example.com`:

```javascript
    const res = await request.get("http://example.com").connect("127.0.0.1");
```

Because the request may be redirected, it's possible to specify multiple hostnames and multiple IPs, as well as a special `*` as the fallback (note: other wildcards are not supported). The requests will keep their `Host` header with the original value. `.connect(undefined)` turns off the feature.

```javascript
    const res = await request.get("http://redir.example.com:555")
      .connect({
        "redir.example.com": "127.0.0.1", // redir.example.com:555 will use 127.0.0.1:555
        "www.example.com": false, // don't override this one; use DNS as normal
        "mapped.example.com": { host: "127.0.0.1", port: 8080}, // mapped.example.com:* will use 127.0.0.1:8080
        "*": "proxy.example.com", // all other requests will go to this host
      });
```

### Ignoring broken/insecure HTTPS on localhost

In Node.js, when HTTPS is misconfigured and insecure (e.g. using self-signed certificate *without* specifying own `.ca()`), it's still possible to permit requests to `localhost` by calling `.trustLocalhost()`:

```javascript
    const res = await request.get("https://localhost").trustLocalhost()
```

Together with `.connect("127.0.0.1")` this may be used to force HTTPS requests to any domain to be re-routed to `localhost` instead.

It's generally safe to ignore broken HTTPS on `localhost`, because the loopback interface is not exposed to untrusted networks. Trusting `localhost` may become the default in the future. Use `.trustLocalhost(false)` to force check of `127.0.0.1`'s authenticity.

We intentionally don't support disabling of HTTPS security when making requests to any other IP, because such options end up abused as a quick "fix" for HTTPS problems. You can get free HTTPS certificates from [Let's Encrypt](https://certbot.eff.org) or set your own CA (`.ca(ca_public_pem)`) to make your self-signed certificates trusted.

## Promise and Generator support

SuperAgent's request is a "thenable" object that's compatible with JavaScript promises and the `async`/`await` syntax.

```javascript
    const res = await request.get(url);
```

If you're using promises, **do not** call `.end()` or `.pipe()`. Any use of `.then()` or `await` disables all other ways of using the request.

Libraries like [co](https://github.com/tj/co) or a web framework like [koa](https://github.com/koajs/koa) can `yield` on any SuperAgent method:

```javascript
    const req = request
      .get('http://local')
      .auth('tobi', 'learnboost');
    const res = yield req;
```

Note that SuperAgent expects the global `Promise` object to be present. You'll need to use v7 and a polyfill to use promises in Internet Explorer or Node.js 0.10.

We have dropped support in v8 for IE.  You must add a polyfill for WeakRef and BigInt if you wish to support Opera 85, iOS Safari 12.2-12.5, for example using <https://cdnjs.cloudflare.com/polyfill/>:

```html
<script src="https://cdnjs.cloudflare.com/polyfill/v3/polyfill.min.js?features=WeakRef,BigInt"></script>
```

## Browser and node versions

SuperAgent has two implementations: one for web browsers (using XHR) and one for Node.JS (using core http module). By default Browserify and WebPack will pick the browser version.

If want to use WebPack to compile code for Node.JS, you *must* specify [node target](https://webpack.github.io/docs/configuration.html#target) in its configuration.
```

## File: `docs/style.css`
```css
body {
  padding: 40px 80px;
  font: 14px/1.5 "Helvetica Neue", Helvetica, sans-serif;
  background: #181818 url(images/bg.png);
  text-align: center;
}

#content {
  margin: 0 auto;
  padding: 10px 40px;
  text-align: left;
  background: white;
  width: 50%;
  -webkit-border-radius: 2px;
  -moz-border-radius: 2px;
  border-radius: 2px;
  -webkit-box-shadow: 0 2px 5px 0 black;
}

#menu {
  font-size: 13px;
  margin: 0;
  padding: 0;
  text-align: left;
  position: fixed;
  top: 15px;
  left: 15px;
}

#menu ul {
  margin: 0;
  padding: 0;
}

#menu li {
  list-style: none;
}

#menu a {
  color: rgba(255,255,255,.5);
  text-decoration: none;
}

#menu a:hover {
  color: white;
}

#menu .active a {
  color: white;
}

pre {
  padding: 10px;
}

code {
  font-family: monaco, monospace, sans-serif;
  font-size: 0.85em;
}

p code {
  border: 1px solid #ECEA75;
  padding: 1px 3px;
  -webkit-border-radius: 2px;
  -moz-border-radius: 2px;
  border-radius: 2px;
  background: #FDFCD1;
}

pre {
  padding: 20px 25px;
  border: 1px solid #ddd;
  -webkit-box-shadow: inset 0 0 5px #eee;
  -moz-box-shadow: inset 0 0 5px #eee;
  box-shadow: inset 0 0 5px #eee;
  overflow: scroll;
}

code .comment { color: #ddd }
code .init { color: #2F6FAD }
code .string { color: #5890AD }
code .keyword { color: #8A6343 }
code .number { color: #2F6FAD }

/* override tocbot style to avoid vertical white line in table of content */
.toc-link::before {
  content: initial;
}
```

## File: `docs/tail.html`
```html
    </div>
    <a href="http://github.com/ladjs/superagent"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://s3.amazonaws.com/github/ribbons/forkme_right_white_ffffff.png" alt="Fork me on GitHub"></a>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.0/jquery.min.js"></script>
    <script>
      $('code').each(function(){
        $(this).html(highlight($(this).text()));
      });

      function highlight(js) {
        return js
          .replace(/</g, '&lt;')
          .replace(/>/g, '&gt;')
          .replace(/('.*?')/gm, '<span class="string">$1</span>')
          .replace(/(\d+\.\d+)/gm, '<span class="number">$1</span>')
          .replace(/(\d+)/gm, '<span class="number">$1</span>')
          .replace(/\bnew *(\w+)/gm, '<span class="keyword">new</span> <span class="init">$1</span>')
          .replace(/\b(function|new|throw|return|var|if|else)\b/gm, '<span class="keyword">$1</span>')
      }
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/tocbot/3.0.0/tocbot.js"></script>
    <script>
      // Only use tocbot for main docs, not test docs
      if (document.querySelector('#superagent')) {
        tocbot.init({
          // Where to render the table of contents.
          tocSelector: '#menu',
          // Where to grab the headings to build the table of contents.
          contentSelector: '#content',
          // Which headings to grab inside of the contentSelector element.
          headingSelector: 'h2',
          smoothScroll: false
        });
      }
    </script>
  </body>
</html>
```

## File: `docs/test.html`
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
test on node with http1
test on plain node
    <section class="suite">
      <h1>Agent</h1>
      <dl>
        <dt>should remember defaults</dt>
        <dd><pre><code>if (typeof Promise === &#x27;undefined&#x27;) {
  return;
}
let called = 0;
let event_called = 0;
const agent = request
  .agent()
  .accept(&#x27;json&#x27;)
  .use(() =&#x3E; {
    called++;
  })
  .once(&#x27;request&#x27;, () =&#x3E; {
    event_called++;
  })
  .query({ hello: &#x27;world&#x27; })
  .set(&#x27;X-test&#x27;, &#x27;testing&#x27;);
assert.equal(0, called);
assert.equal(0, event_called);
return agent
  .get(&#x60;${base}/echo&#x60;)
  .then((res) =&#x3E; {
    assert.equal(1, called);
    assert.equal(1, event_called);
    assert.equal(&#x27;application/json&#x27;, res.headers.accept);
    assert.equal(&#x27;testing&#x27;, res.headers[&#x27;x-test&#x27;]);
    return agent.get(&#x60;${base}/querystring&#x60;);
  })
  .then((res) =&#x3E; {
    assert.equal(2, called);
    assert.equal(2, event_called);
    assert.deepEqual({ hello: &#x27;world&#x27; }, res.body);
  });</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>request</h1>
      <dl>
        <section class="suite">
          <h1>res.statusCode</h1>
          <dl>
            <dt>should set statusCode</dt>
            <dd><pre><code>request.get(&#x60;${uri}/login&#x60;, (error, res) =&#x3E; {
  try {
    assert.strictEqual(res.statusCode, 200);
    done();
  } catch (err) {
    done(err);
  }
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>should allow the send shorthand</h1>
          <dl>
            <dt>with callback in the method call</dt>
            <dd><pre><code>request.get(&#x60;${uri}/login&#x60;, (error, res) =&#x3E; {
  assert.equal(res.status, 200);
  done();
});</code></pre></dd>
            <dt>with data in the method call</dt>
            <dd><pre><code>request.post(&#x60;${uri}/echo&#x60;, { foo: &#x27;bar&#x27; }).end((error, res) =&#x3E; {
  assert.equal(&#x27;{&#x22;foo&#x22;:&#x22;bar&#x22;}&#x27;, res.text);
  done();
});</code></pre></dd>
            <dt>with callback and data in the method call</dt>
            <dd><pre><code>request.post(&#x60;${uri}/echo&#x60;, { foo: &#x27;bar&#x27; }, (error, res) =&#x3E; {
  assert.equal(&#x27;{&#x22;foo&#x22;:&#x22;bar&#x22;}&#x27;, res.text);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>with a callback</h1>
          <dl>
            <dt>should invoke .end()</dt>
            <dd><pre><code>request.get(&#x60;${uri}/login&#x60;, (error, res) =&#x3E; {
  try {
    assert.equal(res.status, 200);
    done();
  } catch (err) {
    done(err);
  }
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>.end()</h1>
          <dl>
            <dt>should issue a request</dt>
            <dd><pre><code>request.get(&#x60;${uri}/login&#x60;).end((error, res) =&#x3E; {
  try {
    assert.equal(res.status, 200);
    done();
  } catch (err) {
    done(err);
  }
});</code></pre></dd>
            <dt>is optional with a promise</dt>
            <dd><pre><code>if (typeof Promise === &#x27;undefined&#x27;) {
  return;
}
return request
  .get(&#x60;${uri}/login&#x60;)
  .then((res) =&#x3E; res.status)
  .then()
  .then((status) =&#x3E; {
    assert.equal(200, status, &#x27;Real promises pass results through&#x27;);
  });</code></pre></dd>
            <dt>called only once with a promise</dt>
            <dd><pre><code>if (typeof Promise === &#x27;undefined&#x27;) {
  return;
}
const request_ = request.get(&#x60;${uri}/unique&#x60;);
return Promise.all([request_, request_, request_]).then((results) =&#x3E; {
  for (const item of results) {
    assert.deepEqual(
      item.body,
      results[0].body,
      &#x27;It should keep returning the same result after being called once&#x27;
    );
  }
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>res.error</h1>
          <dl>
            <dt>ok</dt>
            <dd><pre><code>let calledErrorEvent = false;
let calledOKHandler = false;
request
  .get(&#x60;${uri}/error&#x60;)
  .ok((res) =&#x3E; {
    assert.strictEqual(500, res.status);
    calledOKHandler = true;
    return true;
  })
  .on(&#x27;error&#x27;, (error) =&#x3E; {
    calledErrorEvent = true;
  })
  .end((error, res) =&#x3E; {
    try {
      assert.ifError(error);
      assert.strictEqual(res.status, 500);
      assert(!calledErrorEvent);
      assert(calledOKHandler);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should be an Error object</dt>
            <dd><pre><code>let calledErrorEvent = false;
request
  .get(&#x60;${uri}/error&#x60;)
  .on(&#x27;error&#x27;, (error) =&#x3E; {
    assert.strictEqual(error.status, 500);
    calledErrorEvent = true;
  })
  .end((error, res) =&#x3E; {
    try {
      if (NODE) {
        res.error.message.should.equal(&#x27;cannot GET /error (500)&#x27;);
      } else {
        res.error.message.should.equal(&#x60;cannot GET ${uri}/error (500)&#x60;);
      }
      assert.strictEqual(res.error.status, 500);
      assert(error, &#x27;should have an error for 500&#x27;);
      assert.equal(error.message, &#x27;Internal Server Error&#x27;);
      assert(calledErrorEvent);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>with .then() promise</dt>
            <dd><pre><code>if (typeof Promise === &#x27;undefined&#x27;) {
  return;
}
return request.get(&#x60;${uri}/error&#x60;).then(
  () =&#x3E; {
    assert.fail();
  },
  (err) =&#x3E; {
    assert.equal(err.message, &#x27;Internal Server Error&#x27;);
  }
);</code></pre></dd>
            <dt>with .ok() returning false</dt>
            <dd><pre><code>if (typeof Promise === &#x27;undefined&#x27;) {
  return;
}
return request
  .get(&#x60;${uri}/echo&#x60;)
  .ok(() =&#x3E; false)
  .then(
    () =&#x3E; {
      assert.fail();
    },
    (err) =&#x3E; {
      assert.equal(200, err.response.status);
      assert.equal(err.message, &#x27;OK&#x27;);
    }
  );</code></pre></dd>
            <dt>with .ok() throwing an Error</dt>
            <dd><pre><code>if (typeof Promise === &#x27;undefined&#x27;) {
  return;
}
return request
  .get(&#x60;${uri}/echo&#x60;)
  .ok(() =&#x3E; {
    throw new Error(&#x27;boom&#x27;);
  })
  .then(
    () =&#x3E; {
      assert.fail();
    },
    (err) =&#x3E; {
      assert.equal(200, err.status);
      assert.equal(200, err.response.status);
      assert.equal(err.message, &#x27;boom&#x27;);
    }
  );</code></pre></dd>
            <dt>with .ok() throwing an Error with status</dt>
            <dd><pre><code>if (typeof Promise === &#x27;undefined&#x27;) {
  return;
}
return request
  .get(&#x60;${uri}/echo&#x60;)
  .ok(() =&#x3E; {
    const err = new Error(&#x27;boom&#x27;);
    err.status = 404;
    throw err;
  })
  .then(
    () =&#x3E; {
      assert.fail();
    },
    (err) =&#x3E; {
      assert.equal(404, err.status);
      assert.equal(200, err.response.status);
      assert.equal(err.message, &#x27;boom&#x27;);
    }
  );</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>res.header</h1>
          <dl>
            <dt>should be an object</dt>
            <dd><pre><code>request.get(&#x60;${uri}/login&#x60;).end((error, res) =&#x3E; {
  try {
    assert.equal(&#x27;Express&#x27;, res.header[&#x27;x-powered-by&#x27;]);
    done();
  } catch (err) {
    done(err);
  }
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>set headers</h1>
          <dl>
            <dt>should only set headers for ownProperties of header</dt>
            <dd><pre><code>try {
  request
    .get(&#x60;${uri}/echo-headers&#x60;)
    .set(&#x27;valid&#x27;, &#x27;ok&#x27;)
    .end((error, res) =&#x3E; {
      if (
        !error &#x26;&#x26;
        res.body &#x26;&#x26;
        res.body.valid &#x26;&#x26;
        !res.body.hasOwnProperty(&#x27;invalid&#x27;)
      ) {
        return done();
      }
      done(error || new Error(&#x27;fail&#x27;));
    });
} catch (err) {
  done(err);
}</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>res.charset</h1>
          <dl>
            <dt>should be set when present</dt>
            <dd><pre><code>request.get(&#x60;${uri}/login&#x60;).end((error, res) =&#x3E; {
  try {
    res.charset.should.equal(&#x27;utf-8&#x27;);
    done();
  } catch (err) {
    done(err);
  }
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>res.statusType</h1>
          <dl>
            <dt>should provide the first digit</dt>
            <dd><pre><code>request.get(&#x60;${uri}/login&#x60;).end((error, res) =&#x3E; {
  try {
    assert(!error, &#x27;should not have an error for success responses&#x27;);
    assert.equal(200, res.status);
    assert.equal(2, res.statusType);
    done();
  } catch (err) {
    done(err);
  }
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>res.type</h1>
          <dl>
            <dt>should provide the mime-type void of params</dt>
            <dd><pre><code>request.get(&#x60;${uri}/login&#x60;).end((error, res) =&#x3E; {
  try {
    res.type.should.equal(&#x27;text/html&#x27;);
    res.charset.should.equal(&#x27;utf-8&#x27;);
    done();
  } catch (err) {
    done(err);
  }
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.set(field, val)</h1>
          <dl>
            <dt>should set the header field</dt>
            <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .set(&#x27;X-Foo&#x27;, &#x27;bar&#x27;)
  .set(&#x27;X-Bar&#x27;, &#x27;baz&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;bar&#x27;, res.header[&#x27;x-foo&#x27;]);
      assert.equal(&#x27;baz&#x27;, res.header[&#x27;x-bar&#x27;]);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.set(obj)</h1>
          <dl>
            <dt>should set the header fields</dt>
            <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .set({ &#x27;X-Foo&#x27;: &#x27;bar&#x27;, &#x27;X-Bar&#x27;: &#x27;baz&#x27; })
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;bar&#x27;, res.header[&#x27;x-foo&#x27;]);
      assert.equal(&#x27;baz&#x27;, res.header[&#x27;x-bar&#x27;]);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.type(str)</h1>
          <dl>
            <dt>should set the Content-Type</dt>
            <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .type(&#x27;text/x-foo&#x27;)
  .end((error, res) =&#x3E; {
    try {
      res.header[&#x27;content-type&#x27;].should.equal(&#x27;text/x-foo&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should map &#x22;json&#x22;</dt>
            <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .type(&#x27;json&#x27;)
  .send(&#x27;{&#x22;a&#x22;: 1}&#x27;)
  .end((error, res) =&#x3E; {
    try {
      res.should.be.json();
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should map &#x22;html&#x22;</dt>
            <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .type(&#x27;html&#x27;)
  .end((error, res) =&#x3E; {
    try {
      res.header[&#x27;content-type&#x27;].should.equal(&#x27;text/html&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.accept(str)</h1>
          <dl>
            <dt>should set Accept</dt>
            <dd><pre><code>request
  .get(&#x60;${uri}/echo&#x60;)
  .accept(&#x27;text/x-foo&#x27;)
  .end((error, res) =&#x3E; {
    try {
      res.header.accept.should.equal(&#x27;text/x-foo&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should map &#x22;json&#x22;</dt>
            <dd><pre><code>request
  .get(&#x60;${uri}/echo&#x60;)
  .accept(&#x27;json&#x27;)
  .end((error, res) =&#x3E; {
    try {
      res.header.accept.should.equal(&#x27;application/json&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should map &#x22;xml&#x22;</dt>
            <dd><pre><code>request
  .get(&#x60;${uri}/echo&#x60;)
  .accept(&#x27;xml&#x27;)
  .end((error, res) =&#x3E; {
    try {
      // Mime module keeps changing this :(
      assert(
        res.header.accept == &#x27;application/xml&#x27; ||
          res.header.accept == &#x27;text/xml&#x27;
      );
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should map &#x22;html&#x22;</dt>
            <dd><pre><code>request
  .get(&#x60;${uri}/echo&#x60;)
  .accept(&#x27;html&#x27;)
  .end((error, res) =&#x3E; {
    try {
      res.header.accept.should.equal(&#x27;text/html&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.send(str)</h1>
          <dl>
            <dt>should write the string</dt>
            <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .type(&#x27;json&#x27;)
  .send(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;}&#x27;)
  .end((error, res) =&#x3E; {
    try {
      res.text.should.equal(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;}&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.send(Object)</h1>
          <dl>
            <dt>should default to json</dt>
            <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .send({ name: &#x27;tobi&#x27; })
  .end((error, res) =&#x3E; {
    try {
      res.should.be.json();
      res.text.should.equal(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;}&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <section class="suite">
              <h1>when called several times</h1>
              <dl>
                <dt>should merge the objects</dt>
                <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .send({ name: &#x27;tobi&#x27; })
  .send({ age: 1 })
  .end((error, res) =&#x3E; {
    try {
      res.should.be.json();
      if (NODE) {
        res.buffered.should.be.true();
      }
      res.text.should.equal(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;,&#x22;age&#x22;:1}&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
              </dl>
            </section>
          </dl>
        </section>
        <section class="suite">
          <h1>.end(fn)</h1>
          <dl>
            <dt>should check arity</dt>
            <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .send({ name: &#x27;tobi&#x27; })
  .end((error, res) =&#x3E; {
    try {
      assert.ifError(error);
      res.text.should.equal(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;}&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should emit request</dt>
            <dd><pre><code>const request_ = request.post(&#x60;${uri}/echo&#x60;);
request_.on(&#x27;request&#x27;, (request) =&#x3E; {
  assert.equal(request_, request);
  done();
});
request_.end();</code></pre></dd>
            <dt>should emit response</dt>
            <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .send({ name: &#x27;tobi&#x27; })
  .on(&#x27;response&#x27;, (res) =&#x3E; {
    res.text.should.equal(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;}&#x27;);
    done();
  })
  .end();</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>.then(fulfill, reject)</h1>
          <dl>
            <dt>should support successful fulfills with .then(fulfill)</dt>
            <dd><pre><code>if (typeof Promise === &#x27;undefined&#x27;) {
  return done();
}
request
  .post(&#x60;${uri}/echo&#x60;)
  .send({ name: &#x27;tobi&#x27; })
  .then((res) =&#x3E; {
    res.type.should.equal(&#x27;application/json&#x27;);
    res.text.should.equal(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;}&#x27;);
    done();
  });</code></pre></dd>
            <dt>should reject an error with .then(null, reject)</dt>
            <dd><pre><code>if (typeof Promise === &#x27;undefined&#x27;) {
  return done();
}
request.get(&#x60;${uri}/error&#x60;).then(null, (err) =&#x3E; {
  assert.equal(err.status, 500);
  assert.equal(err.response.text, &#x27;boom&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>.catch(reject)</h1>
          <dl>
            <dt>should reject an error with .catch(reject)</dt>
            <dd><pre><code>if (typeof Promise === &#x27;undefined&#x27;) {
  return done();
}
request.get(&#x60;${uri}/error&#x60;).catch((err) =&#x3E; {
  assert.equal(err.status, 500);
  assert.equal(err.response.text, &#x27;boom&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>.abort()</h1>
          <dl>
            <dt>should abort the request</dt>
            <dd><pre><code>const request_ = request.get(&#x60;${uri}/delay/3000&#x60;);
request_.end((error, res) =&#x3E; {
  try {
    assert(false, &#x27;should not complete the request&#x27;);
  } catch (err) {
    done(err);
  }
});
request_.on(&#x27;error&#x27;, (error) =&#x3E; {
  done(error);
});
request_.on(&#x27;abort&#x27;, done);
setTimeout(() =&#x3E; {
  request_.abort();
}, 500);</code></pre></dd>
            <dt>should abort the promise</dt>
            <dd><pre><code>const request_ = request.get(&#x60;${uri}/delay/3000&#x60;);
setTimeout(() =&#x3E; {
  request_.abort();
}, 10);
return request_.then(
  () =&#x3E; {
    assert.fail(&#x27;should not complete the request&#x27;);
  },
  (err) =&#x3E; {
    assert.equal(&#x27;ABORTED&#x27;, err.code);
  }
);</code></pre></dd>
            <dt>should allow chaining .abort() several times</dt>
            <dd><pre><code>const request_ = request.get(&#x60;${uri}/delay/3000&#x60;);
request_.end((error, res) =&#x3E; {
  try {
    assert(false, &#x27;should not complete the request&#x27;);
  } catch (err) {
    done(err);
  }
});
// This also verifies only a single &#x27;done&#x27; event is emitted
request_.on(&#x27;abort&#x27;, done);
setTimeout(() =&#x3E; {
  request_.abort().abort().abort();
}, 1000);</code></pre></dd>
            <dt>should not allow abort then end</dt>
            <dd><pre><code>request
  .get(&#x60;${uri}/delay/3000&#x60;)
  .abort()
  .end((error, res) =&#x3E; {
    done(error ? undefined : new Error(&#x27;Expected abort error&#x27;));
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.toJSON()</h1>
          <dl>
            <dt>should describe the request</dt>
            <dd><pre><code>const request_ = request.post(&#x60;${uri}/echo&#x60;).send({ foo: &#x27;baz&#x27; });
request_.end((error, res) =&#x3E; {
  try {
    const json = request_.toJSON();
    assert.equal(&#x27;POST&#x27;, json.method);
    assert(/\/echo$/.test(json.url));
    assert.equal(&#x27;baz&#x27;, json.data.foo);
    done();
  } catch (err) {
    done(err);
  }
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.options()</h1>
          <dl>
            <dt>should allow request body</dt>
            <dd><pre><code>request
  .options(&#x60;${uri}/options/echo/body&#x60;)
  .send({ foo: &#x27;baz&#x27; })
  .end((error, res) =&#x3E; {
    try {
      assert.equal(error, null);
      assert.strictEqual(res.body.foo, &#x27;baz&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.sortQuery()</h1>
          <dl>
            <dt>nop with no querystring</dt>
            <dd><pre><code>request
  .get(&#x60;${uri}/url&#x60;)
  .sortQuery()
  .end((error, res) =&#x3E; {
    try {
      assert.equal(res.text, &#x27;/url&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should sort the request querystring</dt>
            <dd><pre><code>request
  .get(&#x60;${uri}/url&#x60;)
  .query(&#x27;search=Manny&#x27;)
  .query(&#x27;order=desc&#x27;)
  .sortQuery()
  .end((error, res) =&#x3E; {
    try {
      assert.equal(res.text, &#x27;/url?order=desc&#x26;search=Manny&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should allow disabling sorting</dt>
            <dd><pre><code>request
  .get(&#x60;${uri}/url&#x60;)
  .query(&#x27;search=Manny&#x27;)
  .query(&#x27;order=desc&#x27;)
  .sortQuery() // take default of true
  .sortQuery(false) // override it in later call
  .end((error, res) =&#x3E; {
    try {
      assert.equal(res.text, &#x27;/url?search=Manny&#x26;order=desc&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should sort the request querystring using customized function</dt>
            <dd><pre><code>request
  .get(&#x60;${uri}/url&#x60;)
  .query(&#x27;name=Nick&#x27;)
  .query(&#x27;search=Manny&#x27;)
  .query(&#x27;order=desc&#x27;)
  .sortQuery((a, b) =&#x3E; a.length - b.length)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(res.text, &#x27;/url?name=Nick&#x26;order=desc&#x26;search=Manny&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>req.set(&#x22;Content-Type&#x22;, contentType)</h1>
      <dl>
        <dt>should work with just the contentType component</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .set(&#x27;Content-Type&#x27;, &#x27;application/json&#x27;)
  .send({ name: &#x27;tobi&#x27; })
  .end((error) =&#x3E; {
    assert(!error);
    done();
  });</code></pre></dd>
        <dt>should work with the charset component</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .set(&#x27;Content-Type&#x27;, &#x27;application/json; charset=utf-8&#x27;)
  .send({ name: &#x27;tobi&#x27; })
  .end((error) =&#x3E; {
    assert(!error);
    done();
  });</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>req.send(Object) as &#x22;form&#x22;</h1>
      <dl>
        <section class="suite">
          <h1>with req.type() set to form</h1>
          <dl>
            <dt>should send x-www-form-urlencoded data</dt>
            <dd><pre><code>request
  .post(&#x60;${base}/echo&#x60;)
  .type(&#x27;form&#x27;)
  .send({ name: &#x27;tobi&#x27; })
  .end((error, res) =&#x3E; {
    res.header[&#x27;content-type&#x27;].should.equal(
      &#x27;application/x-www-form-urlencoded&#x27;
    );
    res.text.should.equal(&#x27;name=tobi&#x27;);
    done();
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>when called several times</h1>
          <dl>
            <dt>should merge the objects</dt>
            <dd><pre><code>request
  .post(&#x60;${base}/echo&#x60;)
  .type(&#x27;form&#x27;)
  .send({ name: { first: &#x27;tobi&#x27;, last: &#x27;holowaychuk&#x27; } })
  .send({ age: &#x27;1&#x27; })
  .end((error, res) =&#x3E; {
    res.header[&#x27;content-type&#x27;].should.equal(
      &#x27;application/x-www-form-urlencoded&#x27;
    );
    res.text.should.equal(
      &#x27;name%5Bfirst%5D=tobi&#x26;name%5Blast%5D=holowaychuk&#x26;age=1&#x27;
    );
    done();
  });</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>req.attach</h1>
      <dl>
        <dt>ignores null file</dt>
        <dd><pre><code>request
  .post(&#x27;/echo&#x27;)
  .attach(&#x27;image&#x27;, null)
  .end((error, res) =&#x3E; {
    done();
  });</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>req.field</h1>
      <dl>
        <dt>allow bools</dt>
        <dd><pre><code>if (!formDataSupported) {
  return done();
}
request
  .post(&#x60;${base}/formecho&#x60;)
  .field(&#x27;bools&#x27;, true)
  .field(&#x27;strings&#x27;, &#x27;true&#x27;)
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    assert.deepStrictEqual(res.body, { bools: &#x27;true&#x27;, strings: &#x27;true&#x27; });
    done();
  });</code></pre></dd>
        <dt>allow objects</dt>
        <dd><pre><code>if (!formDataSupported) {
  return done();
}
request
  .post(&#x60;${base}/formecho&#x60;)
  .field({ bools: true, strings: &#x27;true&#x27; })
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    assert.deepStrictEqual(res.body, { bools: &#x27;true&#x27;, strings: &#x27;true&#x27; });
    done();
  });</code></pre></dd>
        <dt>works with arrays in objects</dt>
        <dd><pre><code>if (!formDataSupported) {
  return done();
}
request
  .post(&#x60;${base}/formecho&#x60;)
  .field({ numbers: [1, 2, 3] })
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    assert.deepStrictEqual(res.body, { numbers: [&#x27;1&#x27;, &#x27;2&#x27;, &#x27;3&#x27;] });
    done();
  });</code></pre></dd>
        <dt>works with arrays</dt>
        <dd><pre><code>if (!formDataSupported) {
  return done();
}
request
  .post(&#x60;${base}/formecho&#x60;)
  .field(&#x27;letters&#x27;, [&#x27;a&#x27;, &#x27;b&#x27;, &#x27;c&#x27;])
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    assert.deepStrictEqual(res.body, { letters: [&#x27;a&#x27;, &#x27;b&#x27;, &#x27;c&#x27;] });
    done();
  });</code></pre></dd>
        <dt>throw when empty</dt>
        <dd><pre><code>should.throws(() =&#x3E; {
  request.post(&#x60;${base}/echo&#x60;).field();
}, /name/);
should.throws(() =&#x3E; {
  request.post(&#x60;${base}/echo&#x60;).field(&#x27;name&#x27;);
}, /val/);</code></pre></dd>
        <dt>cannot be mixed with send()</dt>
        <dd><pre><code>assert.throws(() =&#x3E; {
  request.post(&#x27;/echo&#x27;).field(&#x27;form&#x27;, &#x27;data&#x27;).send(&#x27;hi&#x27;);
});
assert.throws(() =&#x3E; {
  request.post(&#x27;/echo&#x27;).send(&#x27;hi&#x27;).field(&#x27;form&#x27;, &#x27;data&#x27;);
});</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>req.send(Object) as &#x22;json&#x22;</h1>
      <dl>
        <dt>should default to json</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .send({ name: &#x27;tobi&#x27; })
  .end((error, res) =&#x3E; {
    res.should.be.json();
    res.text.should.equal(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;}&#x27;);
    done();
  });</code></pre></dd>
        <dt>should work with arrays</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .send([1, 2, 3])
  .end((error, res) =&#x3E; {
    res.should.be.json();
    res.text.should.equal(&#x27;[1,2,3]&#x27;);
    done();
  });</code></pre></dd>
        <dt>should work with value null</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .type(&#x27;json&#x27;)
  .send(&#x27;null&#x27;)
  .end((error, res) =&#x3E; {
    res.should.be.json();
    assert.strictEqual(res.body, null);
    done();
  });</code></pre></dd>
        <dt>should work with value false</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .type(&#x27;json&#x27;)
  .send(&#x27;false&#x27;)
  .end((error, res) =&#x3E; {
    res.should.be.json();
    res.body.should.equal(false);
    done();
  });</code></pre></dd>
        <dt>should work with empty string value</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .type(&#x27;json&#x27;)
  .send(&#x27;&#x22;&#x22;&#x27;)
  .end((error, res) =&#x3E; {
    res.should.be.json();
    res.body.should.equal(&#x27;&#x27;);
    done();
  });</code></pre></dd>
        <dt>should work with vendor MIME type</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .set(&#x27;Content-Type&#x27;, &#x27;application/vnd.example+json&#x27;)
  .send({ name: &#x27;vendor&#x27; })
  .end((error, res) =&#x3E; {
    res.text.should.equal(&#x27;{&#x22;name&#x22;:&#x22;vendor&#x22;}&#x27;);
    ({ name: &#x27;vendor&#x27; }.should.eql(res.body));
    done();
  });</code></pre></dd>
        <section class="suite">
          <h1>when called several times</h1>
          <dl>
            <dt>should merge the objects</dt>
            <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .send({ name: &#x27;tobi&#x27; })
  .send({ age: 1 })
  .end((error, res) =&#x3E; {
    res.should.be.json();
    res.text.should.equal(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;,&#x22;age&#x22;:1}&#x27;);
    ({ name: &#x27;tobi&#x27;, age: 1 }.should.eql(res.body));
    done();
  });</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>res.body</h1>
      <dl>
        <section class="suite">
          <h1>application/json</h1>
          <dl>
            <dt>should parse the body</dt>
            <dd><pre><code>request.get(&#x60;${uri}/json&#x60;).end((error, res) =&#x3E; {
  res.text.should.equal(&#x27;{&#x22;name&#x22;:&#x22;manny&#x22;}&#x27;);
  res.body.should.eql({ name: &#x27;manny&#x27; });
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>Invalid JSON response</h1>
          <dl>
            <dt>should return the raw response</dt>
            <dd><pre><code>request.get(&#x60;${uri}/invalid-json&#x60;).end((error, res) =&#x3E; {
  assert.deepEqual(
    error.rawResponse,
    &#x22;)]}&#x27;, {&#x27;header&#x27;:{&#x27;code&#x27;:200,&#x27;text&#x27;:&#x27;OK&#x27;,&#x27;version&#x27;:&#x27;1.0&#x27;},&#x27;data&#x27;:&#x27;some data&#x27;}&#x22;
  );
  done();
});</code></pre></dd>
            <dt>should return the http status code</dt>
            <dd><pre><code>request.get(&#x60;${uri}/invalid-json-forbidden&#x60;).end((error, res) =&#x3E; {
  assert.equal(error.statusCode, 403);
  done();
});</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>request</h1>
      <dl>
        <section class="suite">
          <h1>on redirect</h1>
          <dl>
            <dt>should retain header fields</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/header&#x60;)
  .set(&#x27;X-Foo&#x27;, &#x27;bar&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert(res.body);
      res.body.should.have.property(&#x27;x-foo&#x27;, &#x27;bar&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should preserve timeout across redirects</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/movies/random&#x60;)
  .timeout(250)
  .end((error, res) =&#x3E; {
    try {
      assert(error instanceof Error, &#x27;expected an error&#x27;);
      error.should.have.property(&#x27;timeout&#x27;, 250);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should successfully redirect after retry on error</dt>
            <dd><pre><code>const id = Math.random() * 1_000_000 * Date.now();
request
  .get(&#x60;${base}/error/redirect/${id}&#x60;)
  .retry(2)
  .end((error, res) =&#x3E; {
    assert(res.ok, &#x27;response should be ok&#x27;);
    assert(res.text, &#x27;first movie page&#x27;);
    done();
  });</code></pre></dd>
            <dt>should preserve retries across redirects</dt>
            <dd><pre><code>const id = Math.random() * 1_000_000 * Date.now();
request
  .get(&#x60;${base}/error/redirect-error${id}&#x60;)
  .retry(2)
  .end((error, res) =&#x3E; {
    assert(error, &#x27;expected an error&#x27;);
    assert.equal(2, error.retries, &#x27;expected an error with .retries&#x27;);
    assert.equal(500, error.status, &#x27;expected an error status of 500&#x27;);
    done();
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>on 303</h1>
          <dl>
            <dt>should redirect with same method</dt>
            <dd><pre><code>request
  .put(&#x60;${base}/redirect-303&#x60;)
  .send({ msg: &#x27;hello&#x27; })
  .redirects(1)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    res.headers.location.should.equal(&#x27;/reply-method&#x27;);
  })
  .end((error, res) =&#x3E; {
    if (error) {
      done(error);
      return;
    }
    res.text.should.equal(&#x27;method=get&#x27;);
    done();
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>on 307</h1>
          <dl>
            <dt>should redirect with same method</dt>
            <dd><pre><code>if (isMSIE) return done(); // IE9 broken
request
  .put(&#x60;${base}/redirect-307&#x60;)
  .send({ msg: &#x27;hello&#x27; })
  .redirects(1)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    res.headers.location.should.equal(&#x27;/reply-method&#x27;);
  })
  .end((error, res) =&#x3E; {
    if (error) {
      done(error);
      return;
    }
    res.text.should.equal(&#x27;method=put&#x27;);
    done();
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>on 308</h1>
          <dl>
            <dt>should redirect with same method</dt>
            <dd><pre><code>if (isMSIE) return done(); // IE9 broken
request
  .put(&#x60;${base}/redirect-308&#x60;)
  .send({ msg: &#x27;hello&#x27; })
  .redirects(1)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    res.headers.location.should.equal(&#x27;/reply-method&#x27;);
  })
  .end((error, res) =&#x3E; {
    if (error) {
      done(error);
      return;
    }
    res.text.should.equal(&#x27;method=put&#x27;);
    done();
  });</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>request</h1>
      <dl>
        <dt>Request inheritance</dt>
        <dd><pre><code>assert(request.get(&#x60;${uri}/&#x60;) instanceof request.Request);</code></pre></dd>
        <dt>request() simple GET without callback</dt>
        <dd><pre><code>request(&#x27;GET&#x27;, &#x27;test/test.request.js&#x27;).end();
next();</code></pre></dd>
        <dt>request() simple GET</dt>
        <dd><pre><code>request(&#x27;GET&#x27;, &#x60;${uri}/ok&#x60;).end((error, res) =&#x3E; {
  try {
    assert(res instanceof request.Response, &#x27;respond with Response&#x27;);
    assert(res.ok, &#x27;response should be ok&#x27;);
    assert(res.text, &#x27;res.text&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request() simple HEAD</dt>
        <dd><pre><code>request.head(&#x60;${uri}/ok&#x60;).end((error, res) =&#x3E; {
  try {
    assert(res instanceof request.Response, &#x27;respond with Response&#x27;);
    assert(res.ok, &#x27;response should be ok&#x27;);
    assert(!res.text, &#x27;res.text&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request() GET 5xx</dt>
        <dd><pre><code>request(&#x27;GET&#x27;, &#x60;${uri}/error&#x60;).end((error, res) =&#x3E; {
  try {
    assert(error);
    assert.equal(error.message, &#x27;Internal Server Error&#x27;);
    assert(!res.ok, &#x27;response should not be ok&#x27;);
    assert(res.error, &#x27;response should be an error&#x27;);
    assert(!res.clientError, &#x27;response should not be a client error&#x27;);
    assert(res.serverError, &#x27;response should be a server error&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request() GET 4xx</dt>
        <dd><pre><code>request(&#x27;GET&#x27;, &#x60;${uri}/notfound&#x60;).end((error, res) =&#x3E; {
  try {
    assert(error);
    assert.equal(error.message, &#x27;Not Found&#x27;);
    assert(!res.ok, &#x27;response should not be ok&#x27;);
    assert(res.error, &#x27;response should be an error&#x27;);
    assert(res.clientError, &#x27;response should be a client error&#x27;);
    assert(!res.serverError, &#x27;response should not be a server error&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request() GET 404 Not Found</dt>
        <dd><pre><code>request(&#x27;GET&#x27;, &#x60;${uri}/notfound&#x60;).end((error, res) =&#x3E; {
  try {
    assert(error);
    assert(res.notFound, &#x27;response should be .notFound&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request() GET 400 Bad Request</dt>
        <dd><pre><code>request(&#x27;GET&#x27;, &#x60;${uri}/bad-request&#x60;).end((error, res) =&#x3E; {
  try {
    assert(error);
    assert(res.badRequest, &#x27;response should be .badRequest&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request() GET 401 Bad Request</dt>
        <dd><pre><code>request(&#x27;GET&#x27;, &#x60;${uri}/unauthorized&#x60;).end((error, res) =&#x3E; {
  try {
    assert(error);
    assert(res.unauthorized, &#x27;response should be .unauthorized&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request() GET 406 Not Acceptable</dt>
        <dd><pre><code>request(&#x27;GET&#x27;, &#x60;${uri}/not-acceptable&#x60;).end((error, res) =&#x3E; {
  try {
    assert(error);
    assert(res.notAcceptable, &#x27;response should be .notAcceptable&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request() GET 204 No Content</dt>
        <dd><pre><code>request(&#x27;GET&#x27;, &#x60;${uri}/no-content&#x60;).end((error, res) =&#x3E; {
  try {
    assert.ifError(error);
    assert(res.noContent, &#x27;response should be .noContent&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request() DELETE 204 No Content</dt>
        <dd><pre><code>request(&#x27;DELETE&#x27;, &#x60;${uri}/no-content&#x60;).end((error, res) =&#x3E; {
  try {
    assert.ifError(error);
    assert(res.noContent, &#x27;response should be .noContent&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request() header parsing</dt>
        <dd><pre><code>request(&#x27;GET&#x27;, &#x60;${uri}/notfound&#x60;).end((error, res) =&#x3E; {
  try {
    assert(error);
    assert.equal(&#x27;text/html; charset=utf-8&#x27;, res.header[&#x27;content-type&#x27;]);
    assert.equal(&#x27;Express&#x27;, res.header[&#x27;x-powered-by&#x27;]);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request() .status</dt>
        <dd><pre><code>request(&#x27;GET&#x27;, &#x60;${uri}/notfound&#x60;).end((error, res) =&#x3E; {
  try {
    assert(error);
    assert.equal(404, res.status, &#x27;response .status&#x27;);
    assert.equal(4, res.statusType, &#x27;response .statusType&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>get()</dt>
        <dd><pre><code>request.get(&#x60;${uri}/notfound&#x60;).end((error, res) =&#x3E; {
  try {
    assert(error);
    assert.equal(404, res.status, &#x27;response .status&#x27;);
    assert.equal(4, res.statusType, &#x27;response .statusType&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>put()</dt>
        <dd><pre><code>request.put(&#x60;${uri}/user/12&#x60;).end((error, res) =&#x3E; {
  try {
    assert.equal(&#x27;updated&#x27;, res.text, &#x27;response text&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>put().send()</dt>
        <dd><pre><code>request
  .put(&#x60;${uri}/user/13/body&#x60;)
  .send({ user: &#x27;new&#x27; })
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;received new&#x27;, res.text, &#x27;response text&#x27;);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>post()</dt>
        <dd><pre><code>request.post(&#x60;${uri}/user&#x60;).end((error, res) =&#x3E; {
  try {
    assert.equal(&#x27;created&#x27;, res.text, &#x27;response text&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>del()</dt>
        <dd><pre><code>request.del(&#x60;${uri}/user/12&#x60;).end((error, res) =&#x3E; {
  try {
    assert.equal(&#x27;deleted&#x27;, res.text, &#x27;response text&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>delete()</dt>
        <dd><pre><code>request.delete(&#x60;${uri}/user/12&#x60;).end((error, res) =&#x3E; {
  try {
    assert.equal(&#x27;deleted&#x27;, res.text, &#x27;response text&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>post() data</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/todo/item&#x60;)
  .type(&#x27;application/octet-stream&#x27;)
  .send(&#x27;tobi&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;added &#x22;tobi&#x22;&#x27;, res.text, &#x27;response text&#x27;);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>request .type()</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/user/12/pet&#x60;)
  .type(&#x27;urlencoded&#x27;)
  .send(&#x27;pet=tobi&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;added pet &#x22;tobi&#x22;&#x27;, res.text, &#x27;response text&#x27;);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>request .type() with alias</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/user/12/pet&#x60;)
  .type(&#x27;application/x-www-form-urlencoded&#x27;)
  .send(&#x27;pet=tobi&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;added pet &#x22;tobi&#x22;&#x27;, res.text, &#x27;response text&#x27;);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>request .get() with no data or callback</dt>
        <dd><pre><code>request.get(&#x60;${uri}/echo-header/content-type&#x60;);
next();</code></pre></dd>
        <dt>request .send() with no data only</dt>
        <dd><pre><code>request.post(&#x60;${uri}/user/5/pet&#x60;).type(&#x27;urlencoded&#x27;).send(&#x27;pet=tobi&#x27;);
next();</code></pre></dd>
        <dt>request .send() with callback only</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/echo-header/accept&#x60;)
  .set(&#x27;Accept&#x27;, &#x27;foo/bar&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;foo/bar&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>request .accept() with json</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/echo-header/accept&#x60;)
  .accept(&#x27;json&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;application/json&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>request .accept() with application/json</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/echo-header/accept&#x60;)
  .accept(&#x27;application/json&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;application/json&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>request .accept() with xml</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/echo-header/accept&#x60;)
  .accept(&#x27;xml&#x27;)
  .end((error, res) =&#x3E; {
    try {
      // We can&#x27;t depend on mime module to be consistent with this
      assert(res.text == &#x27;application/xml&#x27; || res.text == &#x27;text/xml&#x27;);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>request .accept() with application/xml</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/echo-header/accept&#x60;)
  .accept(&#x27;application/xml&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;application/xml&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>request .end()</dt>
        <dd><pre><code>request
  .put(&#x60;${uri}/echo-header/content-type&#x60;)
  .set(&#x27;Content-Type&#x27;, &#x27;text/plain&#x27;)
  .send(&#x27;wahoo&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;text/plain&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>request .send()</dt>
        <dd><pre><code>request
  .put(&#x60;${uri}/echo-header/content-type&#x60;)
  .set(&#x27;Content-Type&#x27;, &#x27;text/plain&#x27;)
  .send(&#x27;wahoo&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;text/plain&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>request .set()</dt>
        <dd><pre><code>request
  .put(&#x60;${uri}/echo-header/content-type&#x60;)
  .set(&#x27;Content-Type&#x27;, &#x27;text/plain&#x27;)
  .send(&#x27;wahoo&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;text/plain&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>request .set(object)</dt>
        <dd><pre><code>request
  .put(&#x60;${uri}/echo-header/content-type&#x60;)
  .set({ &#x27;Content-Type&#x27;: &#x27;text/plain&#x27; })
  .send(&#x27;wahoo&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;text/plain&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>POST urlencoded</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/pet&#x60;)
  .type(&#x27;urlencoded&#x27;)
  .send({ name: &#x27;Manny&#x27;, species: &#x27;cat&#x27; })
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;added Manny the cat&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>POST json</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/pet&#x60;)
  .type(&#x27;json&#x27;)
  .send({ name: &#x27;Manny&#x27;, species: &#x27;cat&#x27; })
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;added Manny the cat&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>POST json array</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .send([1, 2, 3])
  .end((error, res) =&#x3E; {
    try {
      assert.equal(
        &#x27;application/json&#x27;,
        res.header[&#x27;content-type&#x27;].split(&#x27;;&#x27;)[0]
      );
      assert.equal(&#x27;[1,2,3]&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>POST json default</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/pet&#x60;)
  .send({ name: &#x27;Manny&#x27;, species: &#x27;cat&#x27; })
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;added Manny the cat&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>POST json contentType charset</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .set(&#x27;Content-Type&#x27;, &#x27;application/json; charset=UTF-8&#x27;)
  .send({ data: [&#x27;data1&#x27;, &#x27;data2&#x27;] })
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;{&#x22;data&#x22;:[&#x22;data1&#x22;,&#x22;data2&#x22;]}&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>POST json contentType vendor</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .set(&#x27;Content-Type&#x27;, &#x27;application/vnd.example+json&#x27;)
  .send({ data: [&#x27;data1&#x27;, &#x27;data2&#x27;] })
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;{&#x22;data&#x22;:[&#x22;data1&#x22;,&#x22;data2&#x22;]}&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>POST multiple .send() calls</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/pet&#x60;)
  .send({ name: &#x27;Manny&#x27; })
  .send({ species: &#x27;cat&#x27; })
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;added Manny the cat&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>POST multiple .send() strings</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .send(&#x27;user[name]=tj&#x27;)
  .send(&#x27;user[email]=tj@vision-media.ca&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(
        &#x27;application/x-www-form-urlencoded&#x27;,
        res.header[&#x27;content-type&#x27;].split(&#x27;;&#x27;)[0]
      );
      assert.equal(
        res.text,
        &#x27;user[name]=tj&#x26;user[email]=tj@vision-media.ca&#x27;
      );
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>POST with no data</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/empty-body&#x60;)
  .send()
  .end((error, res) =&#x3E; {
    try {
      assert.ifError(error);
      assert(res.noContent, &#x27;response should be .noContent&#x27;);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>GET .type</dt>
        <dd><pre><code>request.get(&#x60;${uri}/pets&#x60;).end((error, res) =&#x3E; {
  try {
    assert.equal(&#x27;application/json&#x27;, res.type);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>GET Content-Type params</dt>
        <dd><pre><code>request.get(&#x60;${uri}/text&#x60;).end((error, res) =&#x3E; {
  try {
    assert.equal(&#x27;utf-8&#x27;, res.charset);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>GET json</dt>
        <dd><pre><code>request.get(&#x60;${uri}/pets&#x60;).end((error, res) =&#x3E; {
  try {
    assert.deepEqual(res.body, [&#x27;tobi&#x27;, &#x27;loki&#x27;, &#x27;jane&#x27;]);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>GET json-seq</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/json-seq&#x60;)
  .buffer()
  .end((error, res) =&#x3E; {
    try {
      assert.ifError(error);
      assert.deepEqual(res.text, &#x27;\u001E{&#x22;id&#x22;:1}\n\u001E{&#x22;id&#x22;:2}\n&#x27;);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>GET binary data</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/binary-data&#x60;)
  .buffer()
  .end((error, res) =&#x3E; {
    try {
      assert.ifError(error);
      assert.deepEqual(res.body, binData);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>GET x-www-form-urlencoded</dt>
        <dd><pre><code>request.get(&#x60;${uri}/foo&#x60;).end((error, res) =&#x3E; {
  try {
    assert.deepEqual(res.body, { foo: &#x27;bar&#x27; });
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>GET shorthand</dt>
        <dd><pre><code>request.get(&#x60;${uri}/foo&#x60;, (error, res) =&#x3E; {
  try {
    assert.equal(&#x27;foo=bar&#x27;, res.text);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>POST shorthand</dt>
        <dd><pre><code>request.post(&#x60;${uri}/user/0/pet&#x60;, { pet: &#x27;tobi&#x27; }, (error, res) =&#x3E; {
  try {
    assert.equal(&#x27;added pet &#x22;tobi&#x22;&#x27;, res.text);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>POST shorthand without callback</dt>
        <dd><pre><code>request.post(&#x60;${uri}/user/0/pet&#x60;, { pet: &#x27;tobi&#x27; }).end((error, res) =&#x3E; {
  try {
    assert.equal(&#x27;added pet &#x22;tobi&#x22;&#x27;, res.text);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>GET querystring object with array</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/querystring&#x60;)
  .query({ val: [&#x27;a&#x27;, &#x27;b&#x27;, &#x27;c&#x27;] })
  .end((error, res) =&#x3E; {
    try {
      assert.deepEqual(res.body, { val: [&#x27;a&#x27;, &#x27;b&#x27;, &#x27;c&#x27;] });
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>GET querystring object with array and primitives</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/querystring&#x60;)
  .query({ array: [&#x27;a&#x27;, &#x27;b&#x27;, &#x27;c&#x27;], string: &#x27;foo&#x27;, number: 10 })
  .end((error, res) =&#x3E; {
    try {
      assert.deepEqual(res.body, {
        array: [&#x27;a&#x27;, &#x27;b&#x27;, &#x27;c&#x27;],
        string: &#x27;foo&#x27;,
        number: 10
      });
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>GET querystring object with two arrays</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/querystring&#x60;)
  .query({ array1: [&#x27;a&#x27;, &#x27;b&#x27;, &#x27;c&#x27;], array2: [1, 2, 3] })
  .end((error, res) =&#x3E; {
    try {
      assert.deepEqual(res.body, {
        array1: [&#x27;a&#x27;, &#x27;b&#x27;, &#x27;c&#x27;],
        array2: [1, 2, 3]
      });
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>GET querystring object</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/querystring&#x60;)
  .query({ search: &#x27;Manny&#x27; })
  .end((error, res) =&#x3E; {
    try {
      assert.deepEqual(res.body, { search: &#x27;Manny&#x27; });
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>GET querystring append original</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/querystring?search=Manny&#x60;)
  .query({ range: &#x27;1..5&#x27; })
  .end((error, res) =&#x3E; {
    try {
      assert.deepEqual(res.body, { search: &#x27;Manny&#x27;, range: &#x27;1..5&#x27; });
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>GET querystring multiple objects</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/querystring&#x60;)
  .query({ search: &#x27;Manny&#x27; })
  .query({ range: &#x27;1..5&#x27; })
  .query({ order: &#x27;desc&#x27; })
  .end((error, res) =&#x3E; {
    try {
      assert.deepEqual(res.body, {
        search: &#x27;Manny&#x27;,
        range: &#x27;1..5&#x27;,
        order: &#x27;desc&#x27;
      });
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>GET querystring with strings</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/querystring&#x60;)
  .query(&#x27;search=Manny&#x27;)
  .query(&#x27;range=1..5&#x27;)
  .query(&#x27;order=desc&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.deepEqual(res.body, {
        search: &#x27;Manny&#x27;,
        range: &#x27;1..5&#x27;,
        order: &#x27;desc&#x27;
      });
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>GET querystring with strings and objects</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/querystring&#x60;)
  .query(&#x27;search=Manny&#x27;)
  .query({ order: &#x27;desc&#x27;, range: &#x27;1..5&#x27; })
  .end((error, res) =&#x3E; {
    try {
      assert.deepEqual(res.body, {
        search: &#x27;Manny&#x27;,
        range: &#x27;1..5&#x27;,
        order: &#x27;desc&#x27;
      });
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>GET shorthand payload goes to querystring</dt>
        <dd><pre><code>request.get(
  &#x60;${uri}/querystring&#x60;,
  { foo: &#x27;FOO&#x27;, bar: &#x27;BAR&#x27; },
  (error, res) =&#x3E; {
    try {
      assert.deepEqual(res.body, { foo: &#x27;FOO&#x27;, bar: &#x27;BAR&#x27; });
      next();
    } catch (err) {
      next(err);
    }
  }
);</code></pre></dd>
        <dt>HEAD shorthand payload goes to querystring</dt>
        <dd><pre><code>request.head(
  &#x60;${uri}/querystring-in-header&#x60;,
  { foo: &#x27;FOO&#x27;, bar: &#x27;BAR&#x27; },
  (error, res) =&#x3E; {
    try {
      assert.deepEqual(JSON.parse(res.headers.query), {
        foo: &#x27;FOO&#x27;,
        bar: &#x27;BAR&#x27;
      });
      next();
    } catch (err) {
      next(err);
    }
  }
);</code></pre></dd>
        <dt>request(method, url)</dt>
        <dd><pre><code>request(&#x27;GET&#x27;, &#x60;${uri}/foo&#x60;).end((error, res) =&#x3E; {
  try {
    assert.equal(&#x27;bar&#x27;, res.body.foo);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request(url)</dt>
        <dd><pre><code>request(&#x60;${uri}/foo&#x60;).end((error, res) =&#x3E; {
  try {
    assert.equal(&#x27;bar&#x27;, res.body.foo);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request(url, fn)</dt>
        <dd><pre><code>request(&#x60;${uri}/foo&#x60;, (error, res) =&#x3E; {
  try {
    assert.equal(&#x27;bar&#x27;, res.body.foo);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>req.timeout(ms)</dt>
        <dd><pre><code>const request_ = request.get(&#x60;${uri}/delay/3000&#x60;).timeout(1000);
request_.end((error, res) =&#x3E; {
  try {
    assert(error, &#x27;error missing&#x27;);
    assert.equal(1000, error.timeout, &#x27;err.timeout missing&#x27;);
    assert.equal(
      &#x27;Timeout of 1000ms exceeded&#x27;,
      error.message,
      &#x27;err.message incorrect&#x27;
    );
    assert.equal(null, res);
    assert(request_.timedout, true);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>req.timeout(ms) with redirect</dt>
        <dd><pre><code>const request_ = request.get(&#x60;${uri}/delay/const&#x60;).timeout(1000);
request_.end((error, res) =&#x3E; {
  try {
    assert(error, &#x27;error missing&#x27;);
    assert.equal(1000, error.timeout, &#x27;err.timeout missing&#x27;);
    assert.equal(
      &#x27;Timeout of 1000ms exceeded&#x27;,
      error.message,
      &#x27;err.message incorrect&#x27;
    );
    assert.equal(null, res);
    assert(request_.timedout, true);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request event</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/foo&#x60;)
  .on(&#x27;request&#x27;, (request_) =&#x3E; {
    try {
      assert.equal(&#x60;${uri}/foo&#x60;, request_.url);
      next();
    } catch (err) {
      next(err);
    }
  })
  .end();</code></pre></dd>
        <dt>response event</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/foo&#x60;)
  .on(&#x27;response&#x27;, (res) =&#x3E; {
    try {
      assert.equal(&#x27;bar&#x27;, res.body.foo);
      next();
    } catch (err) {
      next(err);
    }
  })
  .end();</code></pre></dd>
        <dt>response should set statusCode</dt>
        <dd><pre><code>request.get(&#x60;${uri}/ok&#x60;, (error, res) =&#x3E; {
  try {
    assert.strictEqual(res.statusCode, 200);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>req.toJSON()</dt>
        <dd><pre><code>request.get(&#x60;${uri}/ok&#x60;).end((error, res) =&#x3E; {
  try {
    const index = (res.request || res.req).toJSON();
    for (const property of [&#x27;url&#x27;, &#x27;method&#x27;, &#x27;data&#x27;, &#x27;headers&#x27;]) {
      assert(index.hasOwnProperty(property));
    }
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>.retry(count)</h1>
      <dl>
        <dt>should not retry if passed &#x22;0&#x22;</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/error&#x60;)
  .retry(0)
  .end((error, res) =&#x3E; {
    try {
      assert(error, &#x27;expected an error&#x27;);
      assert.equal(
        undefined,
        error.retries,
        &#x27;expected an error without .retries&#x27;
      );
      assert.equal(500, error.status, &#x27;expected an error status of 500&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should not retry if passed an invalid number</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/error&#x60;)
  .retry(-2)
  .end((error, res) =&#x3E; {
    try {
      assert(error, &#x27;expected an error&#x27;);
      assert.equal(
        undefined,
        error.retries,
        &#x27;expected an error without .retries&#x27;
      );
      assert.equal(500, error.status, &#x27;expected an error status of 500&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should not retry if passed undefined</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/error&#x60;)
  .retry(undefined)
  .end((error, res) =&#x3E; {
    try {
      assert(error, &#x27;expected an error&#x27;);
      assert.equal(
        undefined,
        error.retries,
        &#x27;expected an error without .retries&#x27;
      );
      assert.equal(500, error.status, &#x27;expected an error status of 500&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should handle server error after repeat attempt</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/error&#x60;)
  .retry(2)
  .end((error, res) =&#x3E; {
    try {
      assert(error, &#x27;expected an error&#x27;);
      assert.equal(2, error.retries, &#x27;expected an error with .retries&#x27;);
      assert.equal(500, error.status, &#x27;expected an error status of 500&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should retry if passed nothing</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/error&#x60;)
  .retry()
  .end((error, res) =&#x3E; {
    try {
      assert(error, &#x27;expected an error&#x27;);
      assert.equal(1, error.retries, &#x27;expected an error with .retries&#x27;);
      assert.equal(500, error.status, &#x27;expected an error status of 500&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should retry if passed &#x22;true&#x22;</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/error&#x60;)
  .retry(true)
  .end((error, res) =&#x3E; {
    try {
      assert(error, &#x27;expected an error&#x27;);
      assert.equal(1, error.retries, &#x27;expected an error with .retries&#x27;);
      assert.equal(500, error.status, &#x27;expected an error status of 500&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should handle successful request after repeat attempt from server error</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/error/ok/${uniqid()}&#x60;)
  .query({ qs: &#x27;present&#x27; })
  .retry(2)
  .end((error, res) =&#x3E; {
    try {
      assert.ifError(error);
      assert(res.ok, &#x27;response should be ok&#x27;);
      assert(res.text, &#x27;res.text&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should handle server timeout error after repeat attempt</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/delay/400&#x60;)
  .timeout(200)
  .retry(2)
  .end((error, res) =&#x3E; {
    try {
      assert(error, &#x27;expected an error&#x27;);
      assert.equal(2, error.retries, &#x27;expected an error with .retries&#x27;);
      assert.equal(
        &#x27;number&#x27;,
        typeof error.timeout,
        &#x27;expected an error with .timeout&#x27;
      );
      assert.equal(&#x27;ECONNABORTED&#x27;, error.code, &#x27;expected abort error code&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should handle successful request after repeat attempt from server timeout</dt>
        <dd><pre><code>const url = &#x60;/delay/1200/ok/${uniqid()}?built=in&#x60;;
request
  .get(base + url)
  .query(&#x27;string=ified&#x27;)
  .query({ json: &#x27;ed&#x27; })
  .timeout(600)
  .retry(2)
  .end((error, res) =&#x3E; {
    try {
      assert.ifError(error);
      assert(res.ok, &#x27;response should be ok&#x27;);
      assert.equal(res.text, &#x60;ok = ${url}&#x26;string=ified&#x26;json=ed&#x60;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should handle successful request after repeat attempt from server timeout when using .then(fulfill, reject)</dt>
        <dd><pre><code>const url = &#x60;/delay/1200/ok/${uniqid()}?built=in&#x60;;
request
  .get(base + url)
  .query(&#x27;string=ified&#x27;)
  .query({ json: &#x27;ed&#x27; })
  .timeout(600)
  .retry(1)
  .then((res, error) =&#x3E; {
    try {
      assert.ifError(error);
      assert(res.ok, &#x27;response should be ok&#x27;);
      assert.equal(res.text, &#x60;ok = ${url}&#x26;string=ified&#x26;json=ed&#x60;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should correctly abort a retry attempt</dt>
        <dd><pre><code>let aborted = false;
const request_ = request.get(&#x60;${base}/delay/400&#x60;).timeout(200).retry(2);
request_.end((error, res) =&#x3E; {
  try {
    assert(false, &#x27;should not complete the request&#x27;);
  } catch (err) {
    done(err);
  }
});
request_.on(&#x27;abort&#x27;, () =&#x3E; {
  aborted = true;
});
setTimeout(() =&#x3E; {
  request_.abort();
  setTimeout(() =&#x3E; {
    try {
      assert(aborted, &#x27;should be aborted&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  }, 150);
}, 150);</code></pre></dd>
        <dt>should correctly retain header fields</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/error/ok/${uniqid()}&#x60;)
  .query({ qs: &#x27;present&#x27; })
  .retry(2)
  .set(&#x27;X-Foo&#x27;, &#x27;bar&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.ifError(error);
      assert(res.body);
      res.body.should.have.property(&#x27;x-foo&#x27;, &#x27;bar&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should not retry on 4xx responses</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/bad-request&#x60;)
  .retry(2)
  .end((error, res) =&#x3E; {
    try {
      assert(error, &#x27;expected an error&#x27;);
      assert.equal(0, error.retries, &#x27;expected an error with 0 .retries&#x27;);
      assert.equal(400, error.status, &#x27;expected an error status of 400&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should execute callback on retry if passed</dt>
        <dd><pre><code>let callbackCallCount = 0;
function retryCallback(request) {
  callbackCallCount++;
}
request
  .get(&#x60;${base}/error&#x60;)
  .retry(2, retryCallback)
  .end((error, res) =&#x3E; {
    try {
      assert(error, &#x27;expected an error&#x27;);
      assert.equal(2, error.retries, &#x27;expected an error with .retries&#x27;);
      assert.equal(500, error.status, &#x27;expected an error status of 500&#x27;);
      assert.equal(
        2,
        callbackCallCount,
        &#x27;expected the callback to be called on each retry&#x27;
      );
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>.timeout(ms)</h1>
      <dl>
        <section class="suite">
          <h1>when timeout is exceeded</h1>
          <dl>
            <dt>should error</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/delay/500&#x60;)
  .timeout(150)
  .end((error, res) =&#x3E; {
    assert(error, &#x27;expected an error&#x27;);
    assert.equal(
      &#x27;number&#x27;,
      typeof error.timeout,
      &#x27;expected an error with .timeout&#x27;
    );
    assert.equal(&#x27;ECONNABORTED&#x27;, error.code, &#x27;expected abort error code&#x27;);
    done();
  });</code></pre></dd>
            <dt>should error in promise interface </dt>
            <dd><pre><code>request
  .get(&#x60;${base}/delay/500&#x60;)
  .timeout(150)
  .catch((err) =&#x3E; {
    assert(err, &#x27;expected an error&#x27;);
    assert.equal(
      &#x27;number&#x27;,
      typeof err.timeout,
      &#x27;expected an error with .timeout&#x27;
    );
    assert.equal(&#x27;ECONNABORTED&#x27;, err.code, &#x27;expected abort error code&#x27;);
    done();
  });</code></pre></dd>
            <dt>should handle gzip timeout</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/delay/zip&#x60;)
  .timeout(150)
  .end((error, res) =&#x3E; {
    assert(error, &#x27;expected an error&#x27;);
    assert.equal(
      &#x27;number&#x27;,
      typeof error.timeout,
      &#x27;expected an error with .timeout&#x27;
    );
    assert.equal(&#x27;ECONNABORTED&#x27;, error.code, &#x27;expected abort error code&#x27;);
    done();
  });</code></pre></dd>
            <dt>should handle buffer timeout</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/delay/json&#x60;)
  .buffer(true)
  .timeout(150)
  .end((error, res) =&#x3E; {
    assert(error, &#x27;expected an error&#x27;);
    assert.equal(
      &#x27;number&#x27;,
      typeof error.timeout,
      &#x27;expected an error with .timeout&#x27;
    );
    assert.equal(&#x27;ECONNABORTED&#x27;, error.code, &#x27;expected abort error code&#x27;);
    done();
  });</code></pre></dd>
            <dt>should error on deadline</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/delay/500&#x60;)
  .timeout({ deadline: 150 })
  .end((error, res) =&#x3E; {
    assert(error, &#x27;expected an error&#x27;);
    assert.equal(
      &#x27;number&#x27;,
      typeof error.timeout,
      &#x27;expected an error with .timeout&#x27;
    );
    assert.equal(&#x27;ECONNABORTED&#x27;, error.code, &#x27;expected abort error code&#x27;);
    done();
  });</code></pre></dd>
            <dt>should support setting individual options</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/delay/500&#x60;)
  .timeout({ deadline: 10 })
  .timeout({ response: 99_999 })
  .end((error, res) =&#x3E; {
    assert(error, &#x27;expected an error&#x27;);
    assert.equal(&#x27;ECONNABORTED&#x27;, error.code, &#x27;expected abort error code&#x27;);
    assert.equal(&#x27;ETIME&#x27;, error.errno);
    done();
  });</code></pre></dd>
            <dt>should error on response</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/delay/500&#x60;)
  .timeout({ response: 150 })
  .end((error, res) =&#x3E; {
    assert(error, &#x27;expected an error&#x27;);
    assert.equal(
      &#x27;number&#x27;,
      typeof error.timeout,
      &#x27;expected an error with .timeout&#x27;
    );
    assert.equal(&#x27;ECONNABORTED&#x27;, error.code, &#x27;expected abort error code&#x27;);
    assert.equal(&#x27;ETIMEDOUT&#x27;, error.errno);
    done();
  });</code></pre></dd>
            <dt>should accept slow body with fast response</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/delay/slowbody&#x60;)
  .timeout({ response: 1000 })
  .on(&#x27;progress&#x27;, () =&#x3E; {
    // This only makes the test faster without relying on arbitrary timeouts
    request.get(&#x60;${base}/delay/slowbody/finish&#x60;).end();
  })
  .end(done);</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>request</h1>
      <dl>
        <section class="suite">
          <h1>use</h1>
          <dl>
            <dt>should use plugin success</dt>
            <dd><pre><code>const now = &#x60;${Date.now()}&#x60;;
function uuid(request_) {
  request_.set(&#x27;X-UUID&#x27;, now);
  return request_;
}
function prefix(request_) {
  request_.url = uri + request_.url;
  return request_;
}
request
  .get(&#x27;/echo&#x27;)
  .use(uuid)
  .use(prefix)
  .end((error, res) =&#x3E; {
    assert.strictEqual(res.statusCode, 200);
    assert.equal(res.get(&#x27;X-UUID&#x27;), now);
    done();
  });</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>subclass</h1>
      <dl>
        <dt>should be an instance of Request</dt>
        <dd><pre><code>const request_ = request.get(&#x27;/&#x27;);
assert(request_ instanceof request.Request);</code></pre></dd>
        <dt>should use patched subclass</dt>
        <dd><pre><code>assert(OriginalRequest);
let constructorCalled;
let sendCalled;
function NewRequest(...args) {
  constructorCalled = true;
  OriginalRequest.apply(this, args);
}
NewRequest.prototype = Object.create(OriginalRequest.prototype);
NewRequest.prototype.send = function () {
  sendCalled = true;
  return this;
};
request.Request = NewRequest;
const request_ = request.get(&#x27;/&#x27;).send();
assert(constructorCalled);
assert(sendCalled);
assert(request_ instanceof NewRequest);
assert(request_ instanceof OriginalRequest);</code></pre></dd>
        <dt>should use patched subclass in agent too</dt>
        <dd><pre><code>if (!request.agent) return; // Node-only
function NewRequest(...args) {
  OriginalRequest.apply(this, args);
}
NewRequest.prototype = Object.create(OriginalRequest.prototype);
request.Request = NewRequest;
const request_ = request.agent().del(&#x27;/&#x27;);
assert(request_ instanceof NewRequest);
assert(request_ instanceof OriginalRequest);</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>request</h1>
      <dl>
        <section class="suite">
          <h1>persistent agent</h1>
          <dl>
            <dt>should gain a session on POST</dt>
            <dd><pre><code>agent3.post(&#x60;${base}/signin&#x60;).then((res) =&#x3E; {
        res.should.have.status(200);
        should.not.exist(res.headers[&#x27;set-cookie&#x27;]);
        res.text.should.containEql(&#x27;dashboard&#x27;);
      })</code></pre></dd>
            <dt>should start with empty session (set cookies)</dt>
            <dd><pre><code>agent1.get(&#x60;${base}/dashboard&#x60;).end((error, res) =&#x3E; {
  should.exist(error);
  res.should.have.status(401);
  should.exist(res.headers[&#x27;set-cookie&#x27;]);
  done();
});</code></pre></dd>
            <dt>should gain a session (cookies already set)</dt>
            <dd><pre><code>agent1.post(&#x60;${base}/signin&#x60;).then((res) =&#x3E; {
        res.should.have.status(200);
        should.not.exist(res.headers[&#x27;set-cookie&#x27;]);
        res.text.should.containEql(&#x27;dashboard&#x27;);
      })</code></pre></dd>
            <dt>should persist cookies across requests</dt>
            <dd><pre><code>agent1.get(&#x60;${base}/dashboard&#x60;).then((res) =&#x3E; {
        res.should.have.status(200);
      })</code></pre></dd>
            <dt>should have the cookie set in the end callback</dt>
            <dd><pre><code>agent4
        .post(&#x60;${base}/setcookie&#x60;)
        .then(() =&#x3E; agent4.get(&#x60;${base}/getcookie&#x60;))
        .then((res) =&#x3E; {
          res.should.have.status(200);
          assert.strictEqual(res.text, &#x27;jar&#x27;);
        })</code></pre></dd>
            <dt>should not share cookies</dt>
            <dd><pre><code>agent2.get(&#x60;${base}/dashboard&#x60;).end((error, res) =&#x3E; {
  should.exist(error);
  res.should.have.status(401);
  done();
});</code></pre></dd>
            <dt>should not lose cookies between agents</dt>
            <dd><pre><code>agent1.get(&#x60;${base}/dashboard&#x60;).then((res) =&#x3E; {
        res.should.have.status(200);
      })</code></pre></dd>
            <dt>should be able to follow redirects</dt>
            <dd><pre><code>agent1.get(base).then((res) =&#x3E; {
        res.should.have.status(200);
        res.text.should.containEql(&#x27;dashboard&#x27;);
      })</code></pre></dd>
            <dt>should be able to post redirects</dt>
            <dd><pre><code>agent1
        .post(&#x60;${base}/redirect&#x60;)
        .send({ foo: &#x27;bar&#x27;, baz: &#x27;blaaah&#x27; })
        .then((res) =&#x3E; {
          res.should.have.status(200);
          res.text.should.containEql(&#x27;simple&#x27;);
          res.redirects.should.eql([&#x60;${base}/simple&#x60;]);
        })</code></pre></dd>
            <dt>should be able to limit redirects</dt>
            <dd><pre><code>agent1
  .get(base)
  .redirects(0)
  .end((error, res) =&#x3E; {
    should.exist(error);
    res.should.have.status(302);
    res.redirects.should.eql([]);
    res.header.location.should.equal(&#x27;/dashboard&#x27;);
    done();
  });</code></pre></dd>
            <dt>should be able to create a new session (clear cookie)</dt>
            <dd><pre><code>agent1.post(&#x60;${base}/signout&#x60;).then((res) =&#x3E; {
        res.should.have.status(200);
        should.exist(res.headers[&#x27;set-cookie&#x27;]);
      })</code></pre></dd>
            <dt>should regenerate with an empty session</dt>
            <dd><pre><code>agent1.get(&#x60;${base}/dashboard&#x60;).end((error, res) =&#x3E; {
  should.exist(error);
  res.should.have.status(401);
  should.not.exist(res.headers[&#x27;set-cookie&#x27;]);
  done();
});</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>Basic auth</h1>
      <dl>
        <section class="suite">
          <h1>when credentials are present in url</h1>
          <dl>
            <dt>should set Authorization</dt>
            <dd><pre><code>const new_url = URL.parse(base);
new_url.auth = &#x27;tobi:learnboost&#x27;;
new_url.pathname = &#x27;/basic-auth&#x27;;
request.get(URL.format(new_url)).end((error, res) =&#x3E; {
  res.status.should.equal(200);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.auth(user, pass)</h1>
          <dl>
            <dt>should set Authorization</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/basic-auth&#x60;)
  .auth(&#x27;tobi&#x27;, &#x27;learnboost&#x27;)
  .end((error, res) =&#x3E; {
    res.status.should.equal(200);
    done();
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.auth(user + &#x22;:&#x22; + pass)</h1>
          <dl>
            <dt>should set authorization</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/basic-auth/again&#x60;)
  .auth(&#x27;tobi&#x27;)
  .end((error, res) =&#x3E; {
    res.status.should.eql(200);
    done();
  });</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>[node] request</h1>
      <dl>
        <dt>should send body with .get().send()</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/echo&#x60;)
  .set(&#x27;Content-Type&#x27;, &#x27;text/plain&#x27;)
  .send(&#x27;wahoo&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;wahoo&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <section class="suite">
          <h1>with an url</h1>
          <dl>
            <dt>should preserve the encoding of the url</dt>
            <dd><pre><code>request.get(&#x60;${base}/url?a=(b%29&#x60;).end((error, res) =&#x3E; {
  assert.equal(&#x27;/url?a=(b%29&#x27;, res.text);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>with an object</h1>
          <dl>
            <dt>should format the url</dt>
            <dd><pre><code>request.get(url.parse(&#x60;${base}/login&#x60;)).then((res) =&#x3E; {
        assert(res.ok);
      })</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>without a schema</h1>
          <dl>
            <dt>should default to http</dt>
            <dd><pre><code>request.get(&#x60;${base}/login&#x60;).then((res) =&#x3E; {
        assert.equal(res.status, 200);
      })</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>res.toJSON()</h1>
          <dl>
            <dt>should describe the response</dt>
            <dd><pre><code>request
        .post(&#x60;${base}/echo&#x60;)
        .send({ foo: &#x27;baz&#x27; })
        .then((res) =&#x3E; {
          const object = res.toJSON();
          assert.equal(&#x27;object&#x27;, typeof object.header);
          assert.equal(&#x27;object&#x27;, typeof object.req);
          assert.equal(200, object.status);
          assert.equal(&#x27;{&#x22;foo&#x22;:&#x22;baz&#x22;}&#x27;, object.text);
        })</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>res.links</h1>
          <dl>
            <dt>should default to an empty object</dt>
            <dd><pre><code>request.get(&#x60;${base}/login&#x60;).then((res) =&#x3E; {
        res.links.should.eql({});
      })</code></pre></dd>
            <dt>should parse the Link header field</dt>
            <dd><pre><code>request.get(&#x60;${base}/links&#x60;).end((error, res) =&#x3E; {
  res.links.next.should.equal(
    &#x27;https://api.github.com/repos/visionmedia/mocha/issues?page=2&#x27;
  );
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.unset(field)</h1>
          <dl>
            <dt>should remove the header field</dt>
            <dd><pre><code>request
  .post(&#x60;${base}/echo&#x60;)
  .unset(&#x27;User-Agent&#x27;)
  .end((error, res) =&#x3E; {
    assert.equal(void 0, res.header[&#x27;user-agent&#x27;]);
    done();
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>case-insensitive</h1>
          <dl>
            <dt>should set/get header fields case-insensitively</dt>
            <dd><pre><code>const r = request.post(&#x60;${base}/echo&#x60;);
r.set(&#x27;MiXeD&#x27;, &#x27;helloes&#x27;);
assert.strictEqual(r.get(&#x27;mixed&#x27;), &#x27;helloes&#x27;);</code></pre></dd>
            <dt>should unset header fields case-insensitively</dt>
            <dd><pre><code>const r = request.post(&#x60;${base}/echo&#x60;);
r.set(&#x27;MiXeD&#x27;, &#x27;helloes&#x27;);
r.unset(&#x27;MIXED&#x27;);
assert.strictEqual(r.get(&#x27;mixed&#x27;), undefined);</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.write(str)</h1>
          <dl>
            <dt>should write the given data</dt>
            <dd><pre><code>const request_ = request.post(&#x60;${base}/echo&#x60;);
request_.set(&#x27;Content-Type&#x27;, &#x27;application/json&#x27;);
assert.equal(&#x27;boolean&#x27;, typeof request_.write(&#x27;{&#x22;name&#x22;&#x27;));
assert.equal(&#x27;boolean&#x27;, typeof request_.write(&#x27;:&#x22;tobi&#x22;}&#x27;));
request_.end((error, res) =&#x3E; {
  res.text.should.equal(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;}&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.pipe(stream)</h1>
          <dl>
            <dt>should pipe the response to the given stream</dt>
            <dd><pre><code>const stream = new EventEmitter();
stream.buf = &#x27;&#x27;;
stream.writable = true;
stream.write = function (chunk) {
  this.buf += chunk;
};
stream.end = function () {
  this.buf.should.equal(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;}&#x27;);
  done();
};
request.post(&#x60;${base}/echo&#x60;).send(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;}&#x27;).pipe(stream);</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>.buffer()</h1>
          <dl>
            <dt>should enable buffering</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/custom&#x60;)
  .buffer()
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    assert.equal(&#x27;custom stuff&#x27;, res.text);
    assert(res.buffered);
    done();
  });</code></pre></dd>
            <dt>should take precedence over request.buffer[&#x27;someMimeType&#x27;] = false</dt>
            <dd><pre><code>const type = &#x27;application/barbaz&#x27;;
const send = &#x27;some text&#x27;;
request.buffer[type] = false;
request
  .post(&#x60;${base}/echo&#x60;)
  .type(type)
  .send(send)
  .buffer()
  .end((error, res) =&#x3E; {
    delete request.buffer[type];
    assert.ifError(error);
    assert.equal(res.type, type);
    assert.equal(send, res.text);
    assert(res.buffered);
    done();
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>.buffer(false)</h1>
          <dl>
            <dt>should disable buffering</dt>
            <dd><pre><code>request
  .post(&#x60;${base}/echo&#x60;)
  .type(&#x27;application/x-dog&#x27;)
  .send(&#x27;hello this is dog&#x27;)
  .buffer(false)
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    assert.equal(null, res.text);
    res.body.should.eql({});
    let buf = &#x27;&#x27;;
    res.setEncoding(&#x27;utf8&#x27;);
    res.on(&#x27;data&#x27;, (chunk) =&#x3E; {
      buf += chunk;
    });
    res.on(&#x27;end&#x27;, () =&#x3E; {
      buf.should.equal(&#x27;hello this is dog&#x27;);
      done();
    });
  });</code></pre></dd>
            <dt>should take precedence over request.buffer[&#x27;someMimeType&#x27;] = true</dt>
            <dd><pre><code>const type = &#x27;application/foobar&#x27;;
const send = &#x27;hello this is a dog&#x27;;
request.buffer[type] = true;
request
  .post(&#x60;${base}/echo&#x60;)
  .type(type)
  .send(send)
  .buffer(false)
  .end((error, res) =&#x3E; {
    delete request.buffer[type];
    assert.ifError(error);
    assert.equal(null, res.text);
    assert.equal(res.type, type);
    assert(!res.buffered);
    res.body.should.eql({});
    let buf = &#x27;&#x27;;
    res.setEncoding(&#x27;utf8&#x27;);
    res.on(&#x27;data&#x27;, (chunk) =&#x3E; {
      buf += chunk;
    });
    res.on(&#x27;end&#x27;, () =&#x3E; {
      buf.should.equal(send);
      done();
    });
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>.withCredentials()</h1>
          <dl>
            <dt>should not throw an error when using the client-side &#x22;withCredentials&#x22; method</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/custom&#x60;)
  .withCredentials()
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    done();
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>.agent()</h1>
          <dl>
            <dt>should return the defaut agent</dt>
            <dd><pre><code>const request_ = request.post(&#x60;${base}/echo&#x60;);
request_.agent().should.equal(false);
done();</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>.agent(undefined)</h1>
          <dl>
            <dt>should set an agent to undefined and ensure it is chainable</dt>
            <dd><pre><code>const request_ = request.get(&#x60;${base}/echo&#x60;);
const returnValue = request_.agent(undefined);
returnValue.should.equal(request_);
assert.strictEqual(request_.agent(), undefined);
done();</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>.agent(new http.Agent())</h1>
          <dl>
            <dt>should set passed agent</dt>
            <dd><pre><code>const http = require(&#x27;http&#x27;);
const request_ = request.get(&#x60;${base}/echo&#x60;);
const agent = new http.Agent();
const returnValue = request_.agent(agent);
returnValue.should.equal(request_);
request_.agent().should.equal(agent);
done();</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>with a content type other than application/json or text/*</h1>
          <dl>
            <dt>should still use buffering</dt>
            <dd><pre><code>return request
  .post(&#x60;${base}/echo&#x60;)
  .type(&#x27;application/x-dog&#x27;)
  .send(&#x27;hello this is dog&#x27;)
  .then((res) =&#x3E; {
    assert.equal(null, res.text);
    assert.equal(res.body.toString(), &#x27;hello this is dog&#x27;);
    res.buffered.should.be.true;
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>content-length</h1>
          <dl>
            <dt>should be set to the byte length of a non-buffer object</dt>
            <dd><pre><code>const decoder = new StringDecoder(&#x27;utf8&#x27;);
let img = fs.readFileSync(&#x60;${__dirname}/fixtures/test.png&#x60;);
img = decoder.write(img);
request
  .post(&#x60;${base}/echo&#x60;)
  .type(&#x27;application/x-image&#x27;)
  .send(img)
  .buffer(false)
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    assert(!res.buffered);
    assert.equal(res.header[&#x27;content-length&#x27;], Buffer.byteLength(img));
    done();
  });</code></pre></dd>
            <dt>should be set to the length of a buffer object</dt>
            <dd><pre><code>const img = fs.readFileSync(&#x60;${__dirname}/fixtures/test.png&#x60;);
request
  .post(&#x60;${base}/echo&#x60;)
  .type(&#x27;application/x-image&#x27;)
  .send(img)
  .buffer(true)
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    assert(res.buffered);
    assert.equal(res.header[&#x27;content-length&#x27;], img.length);
    done();
  });</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>req.buffer[&#x27;someMimeType&#x27;]</h1>
      <dl>
        <dt>should respect that agent.buffer(true) takes precedent</dt>
        <dd><pre><code>const agent = request.agent();
agent.buffer(true);
const type = &#x27;application/somerandomtype&#x27;;
const send = &#x27;somerandomtext&#x27;;
request.buffer[type] = false;
agent
  .post(&#x60;${base}/echo&#x60;)
  .type(type)
  .send(send)
  .end((error, res) =&#x3E; {
    delete request.buffer[type];
    assert.ifError(error);
    assert.equal(res.type, type);
    assert.equal(send, res.text);
    assert(res.buffered);
    done();
  });</code></pre></dd>
        <dt>should respect that agent.buffer(false) takes precedent</dt>
        <dd><pre><code>const agent = request.agent();
agent.buffer(false);
const type = &#x27;application/barrr&#x27;;
const send = &#x27;some random text2&#x27;;
request.buffer[type] = true;
agent
  .post(&#x60;${base}/echo&#x60;)
  .type(type)
  .send(send)
  .end((error, res) =&#x3E; {
    delete request.buffer[type];
    assert.ifError(error);
    assert.equal(null, res.text);
    assert.equal(res.type, type);
    assert(!res.buffered);
    res.body.should.eql({});
    let buf = &#x27;&#x27;;
    res.setEncoding(&#x27;utf8&#x27;);
    res.on(&#x27;data&#x27;, (chunk) =&#x3E; {
      buf += chunk;
    });
    res.on(&#x27;end&#x27;, () =&#x3E; {
      buf.should.equal(send);
      done();
    });
  });</code></pre></dd>
        <dt>should disable buffering for that mimetype when false</dt>
        <dd><pre><code>const type = &#x27;application/bar&#x27;;
const send = &#x27;some random text&#x27;;
request.buffer[type] = false;
request
  .post(&#x60;${base}/echo&#x60;)
  .type(type)
  .send(send)
  .end((error, res) =&#x3E; {
    delete request.buffer[type];
    assert.ifError(error);
    assert.equal(null, res.text);
    assert.equal(res.type, type);
    assert(!res.buffered);
    res.body.should.eql({});
    let buf = &#x27;&#x27;;
    res.setEncoding(&#x27;utf8&#x27;);
    res.on(&#x27;data&#x27;, (chunk) =&#x3E; {
      buf += chunk;
    });
    res.on(&#x27;end&#x27;, () =&#x3E; {
      buf.should.equal(send);
      done();
    });
  });</code></pre></dd>
        <dt>should enable buffering for that mimetype when true</dt>
        <dd><pre><code>const type = &#x27;application/baz&#x27;;
const send = &#x27;woooo&#x27;;
request.buffer[type] = true;
request
  .post(&#x60;${base}/echo&#x60;)
  .type(type)
  .send(send)
  .end((error, res) =&#x3E; {
    delete request.buffer[type];
    assert.ifError(error);
    assert.equal(res.type, type);
    assert.equal(send, res.text);
    assert(res.buffered);
    done();
  });</code></pre></dd>
        <dt>should fallback to default handling for that mimetype when undefined</dt>
        <dd><pre><code>const type = &#x27;application/bazzz&#x27;;
const send = &#x27;woooooo&#x27;;
return request
  .post(&#x60;${base}/echo&#x60;)
  .type(type)
  .send(send)
  .then((res) =&#x3E; {
    assert.equal(res.type, type);
    assert.equal(send, res.body.toString());
    assert(res.buffered);
  });</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>exports</h1>
      <dl>
        <dt>should expose .protocols</dt>
        <dd><pre><code>Object.keys(request.protocols).should.eql([&#x27;http:&#x27;, &#x27;https:&#x27;, &#x27;http2:&#x27;]);</code></pre></dd>
        <dt>should expose .serialize</dt>
        <dd><pre><code>Object.keys(request.serialize).should.eql([
  &#x27;application/x-www-form-urlencoded&#x27;,
  &#x27;application/json&#x27;
]);</code></pre></dd>
        <dt>should expose .parse</dt>
        <dd><pre><code>Object.keys(request.parse).should.eql([
  &#x27;application/x-www-form-urlencoded&#x27;,
  &#x27;application/json&#x27;,
  &#x27;text&#x27;,
  &#x27;application/json-seq&#x27;,
  &#x27;application/octet-stream&#x27;,
  &#x27;application/pdf&#x27;,
  &#x27;image&#x27;
]);</code></pre></dd>
        <dt>should export .buffer</dt>
        <dd><pre><code>Object.keys(request.buffer).should.eql([]);</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>flags</h1>
      <dl>
        <section class="suite">
          <h1>with 4xx response</h1>
          <dl>
            <dt>should set res.error and res.clientError</dt>
            <dd><pre><code>request.get(&#x60;${base}/notfound&#x60;).end((error, res) =&#x3E; {
  assert(error);
  assert(!res.ok, &#x27;response should not be ok&#x27;);
  assert(res.error, &#x27;response should be an error&#x27;);
  assert(res.clientError, &#x27;response should be a client error&#x27;);
  assert(!res.serverError, &#x27;response should not be a server error&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>with 5xx response</h1>
          <dl>
            <dt>should set res.error and res.serverError</dt>
            <dd><pre><code>request.get(&#x60;${base}/error&#x60;).end((error, res) =&#x3E; {
  assert(error);
  assert(!res.ok, &#x27;response should not be ok&#x27;);
  assert(!res.notFound, &#x27;response should not be notFound&#x27;);
  assert(res.error, &#x27;response should be an error&#x27;);
  assert(!res.clientError, &#x27;response should not be a client error&#x27;);
  assert(res.serverError, &#x27;response should be a server error&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>with 404 Not Found</h1>
          <dl>
            <dt>should res.notFound</dt>
            <dd><pre><code>request.get(&#x60;${base}/notfound&#x60;).end((error, res) =&#x3E; {
  assert(error);
  assert(res.notFound, &#x27;response should be .notFound&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>with 400 Bad Request</h1>
          <dl>
            <dt>should set req.badRequest</dt>
            <dd><pre><code>request.get(&#x60;${base}/bad-request&#x60;).end((error, res) =&#x3E; {
  assert(error);
  assert(res.badRequest, &#x27;response should be .badRequest&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>with 401 Bad Request</h1>
          <dl>
            <dt>should set res.unauthorized</dt>
            <dd><pre><code>request.get(&#x60;${base}/unauthorized&#x60;).end((error, res) =&#x3E; {
  assert(error);
  assert(res.unauthorized, &#x27;response should be .unauthorized&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>with 406 Not Acceptable</h1>
          <dl>
            <dt>should set res.notAcceptable</dt>
            <dd><pre><code>request.get(&#x60;${base}/not-acceptable&#x60;).end((error, res) =&#x3E; {
  assert(error);
  assert(res.notAcceptable, &#x27;response should be .notAcceptable&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>with 204 No Content</h1>
          <dl>
            <dt>should set res.noContent</dt>
            <dd><pre><code>request.get(&#x60;${base}/no-content&#x60;).end((error, res) =&#x3E; {
  assert(!error);
  assert(res.noContent, &#x27;response should be .noContent&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>with 201 Created</h1>
          <dl>
            <dt>should set res.created</dt>
            <dd><pre><code>request.post(&#x60;${base}/created&#x60;).end((error, res) =&#x3E; {
  assert(!error);
  assert(res.created, &#x27;response should be .created&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>with 422 Unprocessable Entity</h1>
          <dl>
            <dt>should set res.unprocessableEntity</dt>
            <dd><pre><code>request.post(&#x60;${base}/unprocessable-entity&#x60;).end((error, res) =&#x3E; {
  assert(error);
  assert(
    res.unprocessableEntity,
    &#x27;response should be .unprocessableEntity&#x27;
  );
  done();
});</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>Merging objects</h1>
      <dl>
        <dt>Don&#x27;t mix Buffer and JSON</dt>
        <dd><pre><code>assert.throws(() =&#x3E; {
  request
    .post(&#x27;/echo&#x27;)
    .send(Buffer.from(&#x27;some buffer&#x27;))
    .send({ allowed: false });
});</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>req.send(String)</h1>
      <dl>
        <dt>should default to &#x22;form&#x22;</dt>
        <dd><pre><code>request
  .post(&#x60;${base}/echo&#x60;)
  .send(&#x27;user[name]=tj&#x27;)
  .send(&#x27;user[email]=tj@vision-media.ca&#x27;)
  .end((error, res) =&#x3E; {
    res.header[&#x27;content-type&#x27;].should.equal(
      &#x27;application/x-www-form-urlencoded&#x27;
    );
    res.body.should.eql({
      user: { name: &#x27;tj&#x27;, email: &#x27;tj@vision-media.ca&#x27; }
    });
    done();
  });</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>res.body</h1>
      <dl>
        <section class="suite">
          <h1>application/x-www-form-urlencoded</h1>
          <dl>
            <dt>should parse the body</dt>
            <dd><pre><code>request.get(&#x60;${base}/form-data&#x60;).end((error, res) =&#x3E; {
  res.text.should.equal(&#x27;pet[name]=manny&#x27;);
  res.body.should.eql({ pet: { name: &#x27;manny&#x27; } });
  done();
});</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>https</h1>
      <dl>
        <section class="suite">
          <h1>certificate authority</h1>
          <dl>
            <section class="suite">
              <h1>request</h1>
              <dl>
                <dt>should give a good response</dt>
                <dd><pre><code>request
  .get(testEndpoint)
  .ca(ca)
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    assert(res.ok);
    assert.strictEqual(&#x27;Safe and secure!&#x27;, res.text);
    done();
  });</code></pre></dd>
                <dt>should reject unauthorized response</dt>
                <dd><pre><code>return request
  .get(testEndpoint)
  .trustLocalhost(false)
  .then(
    () =&#x3E; {
      throw new Error(&#x27;Allows MITM&#x27;);
    },
    () =&#x3E; {}
  );</code></pre></dd>
                <dt>should not reject unauthorized response</dt>
                <dd><pre><code>return request
  .get(testEndpoint)
  .disableTLSCerts()
  .then(({ status }) =&#x3E; {
    assert.strictEqual(status, 200);
  });</code></pre></dd>
                <dt>should trust localhost unauthorized response</dt>
                <dd><pre><code>return request.get(testEndpoint).trustLocalhost(true);</code></pre></dd>
                <dt>should trust overriden localhost unauthorized response</dt>
                <dd><pre><code>return request
  .get(&#x60;https://example.com:${server.address().port}&#x60;)
  .connect(&#x27;127.0.0.1&#x27;)
  .trustLocalhost();</code></pre></dd>
              </dl>
            </section>
            <section class="suite">
              <h1>.agent</h1>
              <dl>
                <dt>should be able to make multiple requests without redefining the certificate</dt>
                <dd><pre><code>const agent = request.agent({ ca });
agent.get(testEndpoint).end((error, res) =&#x3E; {
  assert.ifError(error);
  assert(res.ok);
  assert.strictEqual(&#x27;Safe and secure!&#x27;, res.text);
  agent.get(url.parse(testEndpoint)).end((error, res) =&#x3E; {
    assert.ifError(error);
    assert(res.ok);
    assert.strictEqual(&#x27;Safe and secure!&#x27;, res.text);
    done();
  });
});</code></pre></dd>
              </dl>
            </section>
          </dl>
        </section>
        <section class="suite">
          <h1>client certificates</h1>
          <dl>
            <section class="suite">
              <h1>request</h1>
              <dl>
              </dl>
            </section>
            <section class="suite">
              <h1>.agent</h1>
              <dl>
              </dl>
            </section>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>res.body</h1>
      <dl>
        <section class="suite">
          <h1>image/png</h1>
          <dl>
            <dt>should parse the body</dt>
            <dd><pre><code>request.get(&#x60;${base}/image&#x60;).end((error, res) =&#x3E; {
  res.type.should.equal(&#x27;image/png&#x27;);
  Buffer.isBuffer(res.body).should.be.true();
  (res.body.length - img.length).should.equal(0);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>application/octet-stream</h1>
          <dl>
            <dt>should parse the body</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/image-as-octets&#x60;)
  .buffer(true) // that&#x27;s tech debt :(
  .end((error, res) =&#x3E; {
    res.type.should.equal(&#x27;application/octet-stream&#x27;);
    Buffer.isBuffer(res.body).should.be.true();
    (res.body.length - img.length).should.equal(0);
    done();
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>application/octet-stream</h1>
          <dl>
            <dt>should parse the body (using responseType)</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/image-as-octets&#x60;)
  .responseType(&#x27;blob&#x27;)
  .end((error, res) =&#x3E; {
    res.type.should.equal(&#x27;application/octet-stream&#x27;);
    Buffer.isBuffer(res.body).should.be.true();
    (res.body.length - img.length).should.equal(0);
    done();
  });</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>zlib</h1>
      <dl>
        <dt>should deflate the content</dt>
        <dd><pre><code>request.get(base).end((error, res) =&#x3E; {
  res.should.have.status(200);
  res.text.should.equal(subject);
  res.headers[&#x27;content-length&#x27;].should.be.below(subject.length);
  done();
});</code></pre></dd>
        <dt>should protect from zip bombs</dt>
        <dd><pre><code>request
  .get(base)
  .buffer(true)
  .maxResponseSize(1)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;Maximum response size reached&#x27;, error &#x26;&#x26; error.message);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should ignore trailing junk</dt>
        <dd><pre><code>request.get(&#x60;${base}/junk&#x60;).end((error, res) =&#x3E; {
  res.should.have.status(200);
  res.text.should.equal(subject);
  done();
});</code></pre></dd>
        <dt>should ignore missing data</dt>
        <dd><pre><code>request.get(&#x60;${base}/chopped&#x60;).end((error, res) =&#x3E; {
  assert.equal(undefined, error);
  res.should.have.status(200);
  res.text.should.startWith(subject);
  done();
});</code></pre></dd>
        <dt>should handle corrupted responses</dt>
        <dd><pre><code>request.get(&#x60;${base}/corrupt&#x60;).end((error, res) =&#x3E; {
  assert(error, &#x27;missing error&#x27;);
  assert(!res, &#x27;response should not be defined&#x27;);
  done();
});</code></pre></dd>
        <dt>should handle no content with gzip header</dt>
        <dd><pre><code>request.get(&#x60;${base}/nocontent&#x60;).end((error, res) =&#x3E; {
  assert.ifError(error);
  assert(res);
  res.should.have.status(204);
  res.text.should.equal(&#x27;&#x27;);
  res.headers.should.not.have.property(&#x27;content-length&#x27;);
  done();
});</code></pre></dd>
        <section class="suite">
          <h1>without encoding set</h1>
          <dl>
            <dt>should buffer if asked</dt>
            <dd><pre><code>return request
  .get(&#x60;${base}/binary&#x60;)
  .buffer(true)
  .then((res) =&#x3E; {
    res.should.have.status(200);
    assert(res.headers[&#x27;content-length&#x27;]);
    assert(res.body.byteLength);
    assert.equal(subject, res.body.toString());
  });</code></pre></dd>
            <dt>should emit buffers</dt>
            <dd><pre><code>request.get(&#x60;${base}/binary&#x60;).end((error, res) =&#x3E; {
  res.should.have.status(200);
  res.headers[&#x27;content-length&#x27;].should.be.below(subject.length);
  res.on(&#x27;data&#x27;, (chunk) =&#x3E; {
    chunk.should.have.length(subject.length);
  });
  res.on(&#x27;end&#x27;, done);
});</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>req.lookup()</h1>
      <dl>
        <dt>should set a custom lookup</dt>
        <dd><pre><code>const r = request.get(&#x60;${base}/ok&#x60;).lookup(myLookup);
assert(r.lookup() === myLookup);
r.then((res) =&#x3E; {
  res.text.should.equal(&#x27;ok&#x27;);
  done();
});</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>Multipart</h1>
      <dl>
        <section class="suite">
          <h1>#field(name, value)</h1>
          <dl>
            <dt>should set a multipart field value</dt>
            <dd><pre><code>const request_ = request.post(&#x60;${base}/echo&#x60;);
request_.field(&#x27;user[name]&#x27;, &#x27;tobi&#x27;);
request_.field(&#x27;user[age]&#x27;, &#x27;2&#x27;);
request_.field(&#x27;user[species]&#x27;, &#x27;ferret&#x27;);
return request_.then((res) =&#x3E; {
  res.body[&#x27;user[name]&#x27;].should.equal(&#x27;tobi&#x27;);
  res.body[&#x27;user[age]&#x27;].should.equal(&#x27;2&#x27;);
  res.body[&#x27;user[species]&#x27;].should.equal(&#x27;ferret&#x27;);
});</code></pre></dd>
            <dt>should work with file attachments</dt>
            <dd><pre><code>const request_ = request.post(&#x60;${base}/echo&#x60;);
request_.field(&#x27;name&#x27;, &#x27;Tobi&#x27;);
request_.attach(&#x27;document&#x27;, &#x27;test/node/fixtures/user.html&#x27;);
request_.field(&#x27;species&#x27;, &#x27;ferret&#x27;);
return request_.then((res) =&#x3E; {
  res.body.name.should.equal(&#x27;Tobi&#x27;);
  res.body.species.should.equal(&#x27;ferret&#x27;);
  const html = res.files.document;
  html.originalFilename.should.equal(&#x27;user.html&#x27;);
  html.mimetype.should.equal(&#x27;text/html&#x27;);
  read(html.filepath).should.equal(&#x27;&#x3C;h1&#x3E;name&#x3C;/h1&#x3E;&#x27;);
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>#attach(name, path)</h1>
          <dl>
            <dt>should attach a file</dt>
            <dd><pre><code>const request_ = request.post(&#x60;${base}/echo&#x60;);
request_.attach(&#x27;one&#x27;, &#x27;test/node/fixtures/user.html&#x27;);
request_.attach(&#x27;two&#x27;, &#x27;test/node/fixtures/user.json&#x27;);
request_.attach(&#x27;three&#x27;, &#x27;test/node/fixtures/user.txt&#x27;);
return request_.then((res) =&#x3E; {
  const html = res.files.one;
  const json = res.files.two;
  const text = res.files.three;
  html.originalFilename.should.equal(&#x27;user.html&#x27;);
  html.mimetype.should.equal(&#x27;text/html&#x27;);
  read(html.filepath).should.equal(&#x27;&#x3C;h1&#x3E;name&#x3C;/h1&#x3E;&#x27;);
  json.originalFilename.should.equal(&#x27;user.json&#x27;);
  json.mimetype.should.equal(&#x27;application/json&#x27;);
  read(json.filepath).should.equal(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;}&#x27;);
  text.originalFilename.should.equal(&#x27;user.txt&#x27;);
  text.mimetype.should.equal(&#x27;text/plain&#x27;);
  read(text.filepath).should.equal(&#x27;Tobi&#x27;);
});</code></pre></dd>
            <section class="suite">
              <h1>when a file does not exist</h1>
              <dl>
                <dt>should fail the request with an error</dt>
                <dd><pre><code>const request_ = request.post(&#x60;${base}/echo&#x60;);
request_.attach(&#x27;name&#x27;, &#x27;foo&#x27;);
// request_.attach(&#x27;name2&#x27;, &#x27;bar&#x27;);
// request_.attach(&#x27;name3&#x27;, &#x27;baz&#x27;);
request_.end((error, res) =&#x3E; {
  assert.ok(Boolean(error), &#x27;Request should have failed.&#x27;);
  error.code.should.equal(&#x27;ENOENT&#x27;);
  error.message.should.containEql(&#x27;ENOENT&#x27;);
  if (IS_WINDOWS) {
    error.path.toLowerCase().should.equal(
      getFullPath(&#x27;foo&#x27;).toLowerCase()
    );
  } else {
    error.path.should.equal(getFullPath(&#x27;foo&#x27;));
  }
  done();
});</code></pre></dd>
                <dt>promise should fail</dt>
                <dd><pre><code>return request
  .post(&#x60;${base}/echo&#x60;)
  .field({ a: 1, b: 2 })
  .attach(&#x27;c&#x27;, &#x27;does-not-exist.txt&#x27;)
  .then(
    (res) =&#x3E; assert.fail(&#x27;It should not allow this&#x27;),
    (err) =&#x3E; {
      err.code.should.equal(&#x27;ENOENT&#x27;);
      if (IS_WINDOWS) {
        err.path.toLowerCase().should.equal(
          getFullPath(&#x27;does-not-exist.txt&#x27;).toLowerCase()
        );
      } else {
        err.path.should.equal(getFullPath(&#x27;does-not-exist.txt&#x27;));
      }
    }
  );</code></pre></dd>
                <dt>should report ENOENT via the callback</dt>
                <dd><pre><code>request
  .post(&#x60;${base}/echo&#x60;)
  .attach(&#x27;name&#x27;, &#x27;file-does-not-exist&#x27;)
  .end((error, res) =&#x3E; {
    assert.ok(Boolean(error), &#x27;Request should have failed&#x27;);
    error.code.should.equal(&#x27;ENOENT&#x27;);
    done();
  });</code></pre></dd>
                <dt>should report ENOENT via Promise</dt>
                <dd><pre><code>return request
  .post(&#x60;${base}/echo&#x60;)
  .attach(&#x27;name&#x27;, &#x27;file-does-not-exist&#x27;)
  .then(
    (res) =&#x3E; assert.fail(&#x27;Request should have failed&#x27;),
    (err) =&#x3E; err.code.should.equal(&#x27;ENOENT&#x27;)
  );</code></pre></dd>
              </dl>
            </section>
          </dl>
        </section>
        <section class="suite">
          <h1>#attach(name, path, filename)</h1>
          <dl>
            <dt>should use the custom filename</dt>
            <dd><pre><code>request
        .post(&#x60;${base}/echo&#x60;)
        .attach(&#x27;document&#x27;, &#x27;test/node/fixtures/user.html&#x27;, &#x27;doc.html&#x27;)
        .then((res) =&#x3E; {
          const html = res.files.document;
          html.originalFilename.should.equal(&#x27;doc.html&#x27;);
          html.mimetype.should.equal(&#x27;text/html&#x27;);
          read(html.filepath).should.equal(&#x27;&#x3C;h1&#x3E;name&#x3C;/h1&#x3E;&#x27;);
        })</code></pre></dd>
            <dt>should fire progress event</dt>
            <dd><pre><code>let loaded = 0;
let total = 0;
let uploadEventWasFired = false;
request
  .post(&#x60;${base}/echo&#x60;)
  .attach(&#x27;document&#x27;, &#x27;test/node/fixtures/user.html&#x27;)
  .on(&#x27;progress&#x27;, (event) =&#x3E; {
    total = event.total;
    loaded = event.loaded;
    if (event.direction === &#x27;upload&#x27;) {
      uploadEventWasFired = true;
    }
  })
  .end((error, res) =&#x3E; {
    if (error) return done(error);
    const html = res.files.document;
    html.originalFilename.should.equal(&#x27;user.html&#x27;);
    html.mimetype.should.equal(&#x27;text/html&#x27;);
    read(html.filepath).should.equal(&#x27;&#x3C;h1&#x3E;name&#x3C;/h1&#x3E;&#x27;);
    total.should.equal(223);
    loaded.should.equal(223);
    uploadEventWasFired.should.equal(true);
    done();
  });</code></pre></dd>
            <dt>filesystem errors should be caught</dt>
            <dd><pre><code>request
  .post(&#x60;${base}/echo&#x60;)
  .attach(&#x27;filedata&#x27;, &#x27;test/node/fixtures/non-existent-file.ext&#x27;)
  .end((error, res) =&#x3E; {
    assert.ok(Boolean(error), &#x27;Request should have failed.&#x27;);
    error.code.should.equal(&#x27;ENOENT&#x27;);
    if (IS_WINDOWS) {
      error.path.toLowerCase().should.equal(
        getFullPath(&#x27;test/node/fixtures/non-existent-file.ext&#x27;).toLowerCase()
      );
    } else {
      error.path.should.equal(
        getFullPath(&#x27;test/node/fixtures/non-existent-file.ext&#x27;)
      );
    }
    done();
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>#field(name, val)</h1>
          <dl>
            <dt>should set a multipart field value</dt>
            <dd><pre><code>request
  .post(&#x60;${base}/echo&#x60;)
  .field(&#x27;first-name&#x27;, &#x27;foo&#x27;)
  .field(&#x27;last-name&#x27;, &#x27;bar&#x27;)
  .end((error, res) =&#x3E; {
    if (error) done(error);
    res.should.be.ok();
    res.body[&#x27;first-name&#x27;].should.equal(&#x27;foo&#x27;);
    res.body[&#x27;last-name&#x27;].should.equal(&#x27;bar&#x27;);
    done();
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>#field(object)</h1>
          <dl>
            <dt>should set multiple multipart fields</dt>
            <dd><pre><code>request
  .post(&#x60;${base}/echo&#x60;)
  .field({ &#x27;first-name&#x27;: &#x27;foo&#x27;, &#x27;last-name&#x27;: &#x27;bar&#x27; })
  .end((error, res) =&#x3E; {
    if (error) done(error);
    res.should.be.ok();
    res.body[&#x27;first-name&#x27;].should.equal(&#x27;foo&#x27;);
    res.body[&#x27;last-name&#x27;].should.equal(&#x27;bar&#x27;);
    done();
  });</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>with network error</h1>
      <dl>
        <dt>should error</dt>
        <dd><pre><code>request.get(&#x60;http://localhost:${this.port}/&#x60;).end((error, res) =&#x3E; {
  assert(error, &#x27;expected an error&#x27;);
  done();
});</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>request</h1>
      <dl>
        <section class="suite">
          <h1>not modified</h1>
          <dl>
            <dt>should start with 200</dt>
            <dd><pre><code>request.get(&#x60;${base}/if-mod&#x60;).end((error, res) =&#x3E; {
  res.should.have.status(200);
  res.text.should.match(/^\d+$/);
  ts = Number(res.text);
  done();
});</code></pre></dd>
            <dt>should then be 304</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/if-mod&#x60;)
  .set(&#x27;If-Modified-Since&#x27;, new Date(ts).toUTCString())
  .end((error, res) =&#x3E; {
    res.should.have.status(304);
    // res.text.should.be.empty
    done();
  });</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>req.parse(fn)</h1>
      <dl>
        <dt>should take precedence over default parsers</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/manny&#x60;)
  .parse(request.parse[&#x27;application/json&#x27;])
  .end((error, res) =&#x3E; {
    assert(res.ok);
    assert.equal(&#x27;{&#x22;name&#x22;:&#x22;manny&#x22;}&#x27;, res.text);
    assert.equal(&#x27;manny&#x27;, res.body.name);
    done();
  });</code></pre></dd>
        <dt>should be the only parser</dt>
        <dd><pre><code>request
      .get(&#x60;${base}/image&#x60;)
      .buffer(false)
      .parse((res, fn) =&#x3E; {
        res.on(&#x27;data&#x27;, () =&#x3E; {});
      })
      .then((res) =&#x3E; {
        assert(res.ok);
        assert.strictEqual(res.text, undefined);
        res.body.should.eql({});
      })</code></pre></dd>
        <dt>should emit error if parser throws</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/manny&#x60;)
  .parse(() =&#x3E; {
    throw new Error(&#x27;I am broken&#x27;);
  })
  .on(&#x27;error&#x27;, (error) =&#x3E; {
    error.message.should.equal(&#x27;I am broken&#x27;);
    done();
  })
  .end();</code></pre></dd>
        <dt>should emit error if parser returns an error</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/manny&#x60;)
  .parse((res, fn) =&#x3E; {
    fn(new Error(&#x27;I am broken&#x27;));
  })
  .on(&#x27;error&#x27;, (error) =&#x3E; {
    error.message.should.equal(&#x27;I am broken&#x27;);
    done();
  })
  .end();</code></pre></dd>
        <dt>should not emit error on chunked json</dt>
        <dd><pre><code>request.get(&#x60;${base}/chunked-json&#x60;).end((error) =&#x3E; {
  assert.ifError(error);
  done();
});</code></pre></dd>
        <dt>should not emit error on aborted chunked json</dt>
        <dd><pre><code>const request_ = request.get(&#x60;${base}/chunked-json&#x60;);
request_.end((error) =&#x3E; {
  assert.ifError(error);
  done();
});
setTimeout(() =&#x3E; {
  request_.abort();
}, 50);</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>pipe on redirect</h1>
      <dl>
        <dt>should follow Location</dt>
        <dd><pre><code>const stream = fs.createWriteStream(destinationPath);
const redirects = [];
const request_ = request
  .get(base)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    redirects.push(res.headers.location);
  })
  .connect({
    inapplicable: &#x27;should be ignored&#x27;
  });
stream.on(&#x27;finish&#x27;, () =&#x3E; {
  redirects.should.eql([&#x27;/movies&#x27;, &#x27;/movies/all&#x27;, &#x27;/movies/all/0&#x27;]);
  fs.readFileSync(destinationPath, &#x27;utf8&#x27;).should.eql(&#x27;first movie page&#x27;);
  done();
});
request_.pipe(stream);</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>request pipe</h1>
      <dl>
        <dt>should act as a writable stream</dt>
        <dd><pre><code>const request_ = request.post(base);
const stream = fs.createReadStream(&#x27;test/node/fixtures/user.json&#x27;);
request_.type(&#x27;json&#x27;);
request_.on(&#x27;response&#x27;, (res) =&#x3E; {
  res.body.should.eql({ name: &#x27;tobi&#x27; });
  done();
});
stream.pipe(request_);</code></pre></dd>
        <dt>end() stops piping</dt>
        <dd><pre><code>const stream = fs.createWriteStream(destinationPath);
request.get(base).end((error, res) =&#x3E; {
  try {
    res.pipe(stream);
    return done(new Error(&#x27;Did not prevent nonsense pipe&#x27;));
  } catch {
    /* expected error */
  }
  done();
});</code></pre></dd>
        <dt>should act as a readable stream</dt>
        <dd><pre><code>const stream = fs.createWriteStream(destinationPath);
let responseCalled = false;
const request_ = request.get(base);
request_.type(&#x27;json&#x27;);
request_.on(&#x27;response&#x27;, (res) =&#x3E; {
  res.status.should.eql(200);
  responseCalled = true;
});
stream.on(&#x27;finish&#x27;, () =&#x3E; {
  JSON.parse(fs.readFileSync(destinationPath)).should.eql({
    name: &#x27;tobi&#x27;
  });
  responseCalled.should.be.true();
  done();
});
request_.pipe(stream);</code></pre></dd>
        <dt>should follow redirects</dt>
        <dd><pre><code>const stream = fs.createWriteStream(destinationPath);
let responseCalled = false;
const request_ = request.get(base + &#x27;/redirect&#x27;);
request_.type(&#x27;json&#x27;);
request_.on(&#x27;response&#x27;, (res) =&#x3E; {
  res.status.should.eql(200);
  responseCalled = true;
});
stream.on(&#x27;finish&#x27;, () =&#x3E; {
  JSON.parse(fs.readFileSync(destinationPath)).should.eql({
    name: &#x27;tobi&#x27;
  });
  responseCalled.should.be.true();
  done();
});
request_.pipe(stream);</code></pre></dd>
        <dt>should not throw on bad redirects</dt>
        <dd><pre><code>const stream = fs.createWriteStream(destinationPath);
let responseCalled = false;
let errorCalled = false;
const request_ = request.get(base + &#x27;/badRedirectNoLocation&#x27;);
request_.type(&#x27;json&#x27;);
request_.on(&#x27;response&#x27;, (res) =&#x3E; {
  responseCalled = true;
});
request_.on(&#x27;error&#x27;, (error) =&#x3E; {
  error.message.should.eql(&#x27;No location header for redirect&#x27;);
  errorCalled = true;
  stream.end();
});
stream.on(&#x27;finish&#x27;, () =&#x3E; {
  responseCalled.should.be.false();
  errorCalled.should.be.true();
  done();
});
request_.pipe(stream);</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>req.query(String)</h1>
      <dl>
        <dt>should support passing in a string</dt>
        <dd><pre><code>request
  .del(base)
  .query(&#x27;name=t%F6bi&#x27;)
  .end((error, res) =&#x3E; {
    res.body.should.eql({ name: &#x27;t%F6bi&#x27; });
    done();
  });</code></pre></dd>
        <dt>should work with url query-string and string for query</dt>
        <dd><pre><code>request
  .del(&#x60;${base}/?name=tobi&#x60;)
  .query(&#x27;age=2%20&#x27;)
  .end((error, res) =&#x3E; {
    res.body.should.eql({ name: &#x27;tobi&#x27;, age: &#x27;2 &#x27; });
    done();
  });</code></pre></dd>
        <dt>should support compound elements in a string</dt>
        <dd><pre><code>request
  .del(base)
  .query(&#x27;name=t%F6bi&#x26;age=2&#x27;)
  .end((error, res) =&#x3E; {
    res.body.should.eql({ name: &#x27;t%F6bi&#x27;, age: &#x27;2&#x27; });
    done();
  });</code></pre></dd>
        <dt>should work when called multiple times with a string</dt>
        <dd><pre><code>request
  .del(base)
  .query(&#x27;name=t%F6bi&#x27;)
  .query(&#x27;age=2%F6&#x27;)
  .end((error, res) =&#x3E; {
    res.body.should.eql({ name: &#x27;t%F6bi&#x27;, age: &#x27;2%F6&#x27; });
    done();
  });</code></pre></dd>
        <dt>should work with normal &#x60;query&#x60; object and query string</dt>
        <dd><pre><code>request
  .del(base)
  .query(&#x27;name=t%F6bi&#x27;)
  .query({ age: &#x27;2&#x27; })
  .end((error, res) =&#x3E; {
    res.body.should.eql({ name: &#x27;t%F6bi&#x27;, age: &#x27;2&#x27; });
    done();
  });</code></pre></dd>
        <dt>should not encode raw backticks, but leave encoded ones as is</dt>
        <dd><pre><code>return Promise.all([
  request
    .get(&#x60;${base}/raw-query&#x60;)
    .query(&#x27;name=&#x60;t%60bi&#x60;&#x26;age&#x60;=2&#x27;)
    .then((res) =&#x3E; {
      res.text.should.eql(&#x27;name=&#x60;t%60bi&#x60;&#x26;age&#x60;=2&#x27;);
    }),
  request.get(base + &#x27;/raw-query?&#x60;age%60&#x60;=2%60&#x60;&#x27;).then((res) =&#x3E; {
    res.text.should.eql(&#x27;&#x60;age%60&#x60;=2%60&#x60;&#x27;);
  }),
  request
    .get(&#x60;${base}/raw-query&#x60;)
    .query(&#x27;name=&#x60;t%60bi&#x60;&#x27;)
    .query(&#x27;age&#x60;=2&#x27;)
    .then((res) =&#x3E; {
      res.text.should.eql(&#x27;name=&#x60;t%60bi&#x60;&#x26;age&#x60;=2&#x27;);
    })
]);</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>req.query(Object)</h1>
      <dl>
        <dt>should construct the query-string</dt>
        <dd><pre><code>request
  .del(base)
  .query({ name: &#x27;tobi&#x27; })
  .query({ order: &#x27;asc&#x27; })
  .query({ limit: [&#x27;1&#x27;, &#x27;2&#x27;] })
  .end((error, res) =&#x3E; {
    res.body.should.eql({ name: &#x27;tobi&#x27;, order: &#x27;asc&#x27;, limit: [&#x27;1&#x27;, &#x27;2&#x27;] });
    done();
  });</code></pre></dd>
        <dt>should encode raw backticks</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/raw-query&#x60;)
  .query({ name: &#x27;&#x60;tobi&#x60;&#x27; })
  .query({ &#x27;orde%60r&#x27;: null })
  .query({ &#x27;&#x60;limit&#x60;&#x27;: [&#x27;%602&#x60;&#x27;] })
  .end((error, res) =&#x3E; {
    res.text.should.eql(&#x27;name=%60tobi%60&#x26;orde%2560r&#x26;%60limit%60=%25602%60&#x27;);
    done();
  });</code></pre></dd>
        <dt>should not error on dates</dt>
        <dd><pre><code>const date = new Date(0);
request
  .del(base)
  .query({ at: date })
  .end((error, res) =&#x3E; {
    assert.equal(date.toISOString(), res.body.at);
    done();
  });</code></pre></dd>
        <dt>should work after setting header fields</dt>
        <dd><pre><code>request
  .del(base)
  .set(&#x27;Foo&#x27;, &#x27;bar&#x27;)
  .set(&#x27;Bar&#x27;, &#x27;baz&#x27;)
  .query({ name: &#x27;tobi&#x27; })
  .query({ order: &#x27;asc&#x27; })
  .query({ limit: [&#x27;1&#x27;, &#x27;2&#x27;] })
  .end((error, res) =&#x3E; {
    res.body.should.eql({ name: &#x27;tobi&#x27;, order: &#x27;asc&#x27;, limit: [&#x27;1&#x27;, &#x27;2&#x27;] });
    done();
  });</code></pre></dd>
        <dt>should append to the original query-string</dt>
        <dd><pre><code>request
  .del(&#x60;${base}/?name=tobi&#x60;)
  .query({ order: &#x27;asc&#x27; })
  .end((error, res) =&#x3E; {
    res.body.should.eql({ name: &#x27;tobi&#x27;, order: &#x27;asc&#x27; });
    done();
  });</code></pre></dd>
        <dt>should retain the original query-string</dt>
        <dd><pre><code>request.del(&#x60;${base}/?name=tobi&#x60;).end((error, res) =&#x3E; {
  res.body.should.eql({ name: &#x27;tobi&#x27; });
  done();
});</code></pre></dd>
        <dt>should keep only keys with null querystring values</dt>
        <dd><pre><code>request
  .del(&#x60;${base}/url&#x60;)
  .query({ nil: null })
  .end((error, res) =&#x3E; {
    res.text.should.equal(&#x27;/url?nil&#x27;);
    done();
  });</code></pre></dd>
        <dt>query-string should be sent on pipe</dt>
        <dd><pre><code>this.timeout(15_000);
const request_ = request.put(&#x60;${base}/?name=tobi&#x60;);
const stream = fs.createReadStream(&#x27;test/node/fixtures/user.json&#x27;);
request_.on(&#x27;response&#x27;, (res) =&#x3E; {
  res.body.should.eql({ name: &#x27;tobi&#x27; });
  done();
});
request_.on(&#x27;error&#x27;, (err) =&#x3E; {
  done(err);
});
stream.on(&#x27;error&#x27;, function (err) {
  done(err);
});
stream.pipe(request_);</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>request.get</h1>
      <dl>
        <section class="suite">
          <h1>on 301 redirect</h1>
          <dl>
            <dt>should follow Location with a GET request</dt>
            <dd><pre><code>const request_ = request.get(&#x60;${base}/test-301&#x60;).redirects(1);
request_.end((error, res) =&#x3E; {
  const headers = request_.req.getHeaders
    ? request_.req.getHeaders()
    : request_.req._headers;
  headers.host.should.eql(&#x60;localhost:${server2.address().port}&#x60;);
  res.status.should.eql(200);
  res.text.should.eql(&#x27;GET&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>on 302 redirect</h1>
          <dl>
            <dt>should follow Location with a GET request</dt>
            <dd><pre><code>const request_ = request.get(&#x60;${base}/test-302&#x60;).redirects(1);
request_.end((error, res) =&#x3E; {
  const headers = request_.req.getHeaders
    ? request_.req.getHeaders()
    : request_.req._headers;
  res.status.should.eql(200);
  res.text.should.eql(&#x27;GET&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>on 303 redirect</h1>
          <dl>
            <dt>should follow Location with a GET request</dt>
            <dd><pre><code>const request_ = request.get(&#x60;${base}/test-303&#x60;).redirects(1);
request_.end((error, res) =&#x3E; {
  const headers = request_.req.getHeaders
    ? request_.req.getHeaders()
    : request_.req._headers;
  headers.host.should.eql(&#x60;localhost:${server2.address().port}&#x60;);
  res.status.should.eql(200);
  res.text.should.eql(&#x27;GET&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>on 307 redirect</h1>
          <dl>
            <dt>should follow Location with a GET request</dt>
            <dd><pre><code>const request_ = request.get(&#x60;${base}/test-307&#x60;).redirects(1);
request_.end((error, res) =&#x3E; {
  const headers = request_.req.getHeaders
    ? request_.req.getHeaders()
    : request_.req._headers;
  headers.host.should.eql(&#x60;localhost:${server2.address().port}&#x60;);
  res.status.should.eql(200);
  res.text.should.eql(&#x27;GET&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>on 308 redirect</h1>
          <dl>
            <dt>should follow Location with a GET request</dt>
            <dd><pre><code>const request_ = request.get(&#x60;${base}/test-308&#x60;).redirects(1);
request_.end((error, res) =&#x3E; {
  const headers = request_.req.getHeaders
    ? request_.req.getHeaders()
    : request_.req._headers;
  headers.host.should.eql(&#x60;localhost:${server2.address().port}&#x60;);
  res.status.should.eql(200);
  res.text.should.eql(&#x27;GET&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>request.post</h1>
      <dl>
        <section class="suite">
          <h1>on 301 redirect</h1>
          <dl>
            <dt>should follow Location with a GET request</dt>
            <dd><pre><code>const request_ = request.post(&#x60;${base}/test-301&#x60;).redirects(1);
request_.end((error, res) =&#x3E; {
  const headers = request_.req.getHeaders
    ? request_.req.getHeaders()
    : request_.req._headers;
  headers.host.should.eql(&#x60;localhost:${server2.address().port}&#x60;);
  res.status.should.eql(200);
  res.text.should.eql(&#x27;GET&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>on 302 redirect</h1>
          <dl>
            <dt>should follow Location with a GET request</dt>
            <dd><pre><code>const request_ = request.post(&#x60;${base}/test-302&#x60;).redirects(1);
request_.end((error, res) =&#x3E; {
  const headers = request_.req.getHeaders
    ? request_.req.getHeaders()
    : request_.req._headers;
  headers.host.should.eql(&#x60;localhost:${server2.address().port}&#x60;);
  res.status.should.eql(200);
  res.text.should.eql(&#x27;GET&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>on 303 redirect</h1>
          <dl>
            <dt>should follow Location with a GET request</dt>
            <dd><pre><code>const request_ = request.post(&#x60;${base}/test-303&#x60;).redirects(1);
request_.end((error, res) =&#x3E; {
  const headers = request_.req.getHeaders
    ? request_.req.getHeaders()
    : request_.req._headers;
  headers.host.should.eql(&#x60;localhost:${server2.address().port}&#x60;);
  res.status.should.eql(200);
  res.text.should.eql(&#x27;GET&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>on 307 redirect</h1>
          <dl>
            <dt>should follow Location with a POST request</dt>
            <dd><pre><code>const request_ = request.post(&#x60;${base}/test-307&#x60;).redirects(1);
request_.end((error, res) =&#x3E; {
  const headers = request_.req.getHeaders
    ? request_.req.getHeaders()
    : request_.req._headers;
  headers.host.should.eql(&#x60;localhost:${server2.address().port}&#x60;);
  res.status.should.eql(200);
  res.text.should.eql(&#x27;POST&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>on 308 redirect</h1>
          <dl>
            <dt>should follow Location with a POST request</dt>
            <dd><pre><code>const request_ = request.post(&#x60;${base}/test-308&#x60;).redirects(1);
request_.end((error, res) =&#x3E; {
  const headers = request_.req.getHeaders
    ? request_.req.getHeaders()
    : request_.req._headers;
  headers.host.should.eql(&#x60;localhost:${server2.address().port}&#x60;);
  res.status.should.eql(200);
  res.text.should.eql(&#x27;POST&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>request</h1>
      <dl>
        <section class="suite">
          <h1>on redirect</h1>
          <dl>
            <dt>should merge cookies if agent is used</dt>
            <dd><pre><code>request
  .agent()
  .get(&#x60;${base}/cookie-redirect&#x60;)
  .set(&#x27;Cookie&#x27;, &#x27;orig=1; replaced=not&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.ifError(error);
      assert(/orig=1/.test(res.text), &#x27;orig=1/.test&#x27;);
      assert(/replaced=yes/.test(res.text), &#x27;replaced=yes/.test&#x27;);
      assert(/from-redir=1/.test(res.text), &#x27;from-redir=1&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should not merge cookies if agent is not used</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/cookie-redirect&#x60;)
  .set(&#x27;Cookie&#x27;, &#x27;orig=1; replaced=not&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.ifError(error);
      assert(/orig=1/.test(res.text), &#x27;/orig=1&#x27;);
      assert(/replaced=not/.test(res.text), &#x27;/replaced=not&#x27;);
      assert(!/replaced=yes/.test(res.text), &#x27;!/replaced=yes&#x27;);
      assert(!/from-redir/.test(res.text), &#x27;!/from-redir&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should have previously set cookie for subsquent requests when agent is used</dt>
            <dd><pre><code>const agent = request.agent();
agent.get(&#x60;${base}/set-cookie&#x60;).end((error) =&#x3E; {
  assert.ifError(error);
  agent
    .get(&#x60;${base}/show-cookies&#x60;)
    .set({ Cookie: &#x27;orig=1&#x27; })
    .end((error, res) =&#x3E; {
      try {
        assert.ifError(error);
        assert(/orig=1/.test(res.text), &#x27;orig=1/.test&#x27;);
        assert(/persist=123/.test(res.text), &#x27;persist=123&#x27;);
        done();
      } catch (err) {
        done(err);
      }
    });
});</code></pre></dd>
            <dt>should follow Location</dt>
            <dd><pre><code>const redirects = [];
request
  .get(base)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    redirects.push(res.headers.location);
  })
  .end((error, res) =&#x3E; {
    try {
      const array = [&#x27;/movies&#x27;, &#x27;/movies/all&#x27;, &#x27;/movies/all/0&#x27;];
      redirects.should.eql(array);
      res.text.should.equal(&#x27;first movie page&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should follow Location with IP override</dt>
            <dd><pre><code>const redirects = [];
const url = URL.parse(base);
return request
  .get(&#x60;http://redir.example.com:${url.port || &#x27;80&#x27;}${url.pathname}&#x60;)
  .connect({
    &#x27;*&#x27;: url.hostname
  })
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    redirects.push(res.headers.location);
  })
  .then((res) =&#x3E; {
    const array = [&#x27;/movies&#x27;, &#x27;/movies/all&#x27;, &#x27;/movies/all/0&#x27;];
    redirects.should.eql(array);
    res.text.should.equal(&#x27;first movie page&#x27;);
  });</code></pre></dd>
            <dt>should follow Location with IP:port override</dt>
            <dd><pre><code>const redirects = [];
const url = URL.parse(base);
return request
  .get(&#x60;http://redir.example.com:9999${url.pathname}&#x60;)
  .connect({
    &#x27;*&#x27;: { host: url.hostname, port: url.port || 80 }
  })
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    redirects.push(res.headers.location);
  })
  .then((res) =&#x3E; {
    const array = [&#x27;/movies&#x27;, &#x27;/movies/all&#x27;, &#x27;/movies/all/0&#x27;];
    redirects.should.eql(array);
    res.text.should.equal(&#x27;first movie page&#x27;);
  });</code></pre></dd>
            <dt>should not follow on HEAD by default</dt>
            <dd><pre><code>const redirects = [];
return request
  .head(base)
  .ok(() =&#x3E; true)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    redirects.push(res.headers.location);
  })
  .then((res) =&#x3E; {
    redirects.should.eql([]);
    res.status.should.equal(302);
  });</code></pre></dd>
            <dt>should follow on HEAD when redirects are set</dt>
            <dd><pre><code>const redirects = [];
request
  .head(base)
  .redirects(10)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    redirects.push(res.headers.location);
  })
  .end((error, res) =&#x3E; {
    try {
      const array = [];
      array.push(&#x27;/movies&#x27;, &#x27;/movies/all&#x27;, &#x27;/movies/all/0&#x27;);
      redirects.should.eql(array);
      assert(!res.text);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should remove Content-* fields</dt>
            <dd><pre><code>request
  .post(&#x60;${base}/header&#x60;)
  .type(&#x27;txt&#x27;)
  .set(&#x27;X-Foo&#x27;, &#x27;bar&#x27;)
  .set(&#x27;X-Bar&#x27;, &#x27;baz&#x27;)
  .send(&#x27;hey&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert(res.body);
      res.body.should.have.property(&#x27;x-foo&#x27;, &#x27;bar&#x27;);
      res.body.should.have.property(&#x27;x-bar&#x27;, &#x27;baz&#x27;);
      res.body.should.not.have.property(&#x27;content-type&#x27;);
      res.body.should.not.have.property(&#x27;content-length&#x27;);
      res.body.should.not.have.property(&#x27;transfer-encoding&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should retain cookies</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/header&#x60;)
  .set(&#x27;Cookie&#x27;, &#x27;foo=bar;&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert(res.body);
      res.body.should.have.property(&#x27;cookie&#x27;, &#x27;foo=bar;&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should not resend query parameters</dt>
            <dd><pre><code>const redirects = [];
const query = [];
request
  .get(&#x60;${base}/?foo=bar&#x60;)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    query.push(res.headers.query);
    redirects.push(res.headers.location);
  })
  .end((error, res) =&#x3E; {
    try {
      const array = [];
      array.push(&#x27;/movies&#x27;, &#x27;/movies/all&#x27;, &#x27;/movies/all/0&#x27;);
      redirects.should.eql(array);
      res.text.should.equal(&#x27;first movie page&#x27;);
      query.should.eql([&#x27;{&#x22;foo&#x22;:&#x22;bar&#x22;}&#x27;, &#x27;{}&#x27;, &#x27;{}&#x27;]);
      res.headers.query.should.eql(&#x27;{}&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should handle no location header</dt>
            <dd><pre><code>request.get(&#x60;${base}/bad-redirect&#x60;).end((error, res) =&#x3E; {
  try {
    error.message.should.equal(&#x27;No location header for redirect&#x27;);
    done();
  } catch (err) {
    done(err);
  }
});</code></pre></dd>
            <section class="suite">
              <h1>when relative</h1>
              <dl>
                <dt>should redirect to a sibling path</dt>
                <dd><pre><code>const redirects = [];
request
  .get(&#x60;${base}/relative&#x60;)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    redirects.push(res.headers.location);
  })
  .end((error, res) =&#x3E; {
    try {
      redirects.should.eql([&#x27;tobi&#x27;]);
      res.text.should.equal(&#x27;tobi&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
                <dt>should redirect to a parent path</dt>
                <dd><pre><code>const redirects = [];
request
  .get(&#x60;${base}/relative/sub&#x60;)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    redirects.push(res.headers.location);
  })
  .end((error, res) =&#x3E; {
    try {
      redirects.should.eql([&#x27;../tobi&#x27;]);
      res.text.should.equal(&#x27;tobi&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
              </dl>
            </section>
          </dl>
        </section>
        <section class="suite">
          <h1>req.redirects(n)</h1>
          <dl>
            <dt>should alter the default number of redirects to follow</dt>
            <dd><pre><code>const redirects = [];
request
  .get(base)
  .redirects(2)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    redirects.push(res.headers.location);
  })
  .end((error, res) =&#x3E; {
    try {
      const array = [];
      assert(res.redirect, &#x27;res.redirect&#x27;);
      array.push(&#x27;/movies&#x27;, &#x27;/movies/all&#x27;);
      redirects.should.eql(array);
      res.text.should.match(/Moved Temporarily|Found/);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>on POST</h1>
          <dl>
            <dt>should redirect as GET</dt>
            <dd><pre><code>const redirects = [];
return request
  .post(&#x60;${base}/movie&#x60;)
  .send({ name: &#x27;Tobi&#x27; })
  .redirects(2)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    redirects.push(res.headers.location);
  })
  .then((res) =&#x3E; {
    redirects.should.eql([&#x27;/movies/all/0&#x27;]);
    res.text.should.equal(&#x27;first movie page&#x27;);
  });</code></pre></dd>
            <dt>using multipart/form-data should redirect as GET</dt>
            <dd><pre><code>const redirects = [];
request
  .post(&#x60;${base}/movie&#x60;)
  .type(&#x27;form&#x27;)
  .field(&#x27;name&#x27;, &#x27;Tobi&#x27;)
  .redirects(2)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    redirects.push(res.headers.location);
  })
  .then((res) =&#x3E; {
    redirects.should.eql([&#x27;/movies/all/0&#x27;]);
    res.text.should.equal(&#x27;first movie page&#x27;);
  });</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>response</h1>
      <dl>
        <dt>should act as a readable stream</dt>
        <dd><pre><code>const request_ = request.get(base).buffer(false);
request_.end((error, res) =&#x3E; {
  if (error) return done(error);
  let trackEndEvent = 0;
  let trackCloseEvent = 0;
  res.on(&#x27;end&#x27;, () =&#x3E; {
    trackEndEvent++;
    trackEndEvent.should.equal(1);
    if (!process.env.HTTP2_TEST) {
      trackCloseEvent.should.equal(0); // close should not have been called
    }
    done();
  });
  res.on(&#x27;close&#x27;, () =&#x3E; {
    trackCloseEvent++;
  });
  setTimeout(() =&#x3E; {
    (() =&#x3E; {
      res.pause();
    }).should.not.throw();
    (() =&#x3E; {
      res.resume();
    }).should.not.throw();
    (() =&#x3E; {
      res.destroy();
    }).should.not.throw();
  }, 50);
});</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>req.serialize(fn)</h1>
      <dl>
        <dt>should take precedence over default parsers</dt>
        <dd><pre><code>request
  .post(&#x60;${base}/echo&#x60;)
  .send({ foo: 123 })
  .serialize(() =&#x3E; &#x27;{&#x22;bar&#x22;:456}&#x27;)
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    assert.equal(&#x27;{&#x22;bar&#x22;:456}&#x27;, res.text);
    assert.equal(456, res.body.bar);
    done();
  });</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>request.get().set()</h1>
      <dl>
        <dt>should set host header after get()</dt>
        <dd><pre><code>app.get(&#x27;/&#x27;, (request_, res) =&#x3E; {
  assert.equal(request_.hostname, &#x27;example.com&#x27;);
  res.end();
});
server = http.createServer(app);
server.listen(0, function listening() {
  request
    .get(&#x60;http://localhost:${server.address().port}&#x60;)
    .set(&#x27;host&#x27;, &#x27;example.com&#x27;)
    .then(() =&#x3E; {
      return request
        .get(&#x60;http://example.com:${server.address().port}&#x60;)
        .connect({
          &#x27;example.com&#x27;: &#x27;localhost&#x27;,
          &#x27;*&#x27;: &#x27;fail&#x27;
        });
    })
    .then(() =&#x3E; done(), done);
});</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>res.toError()</h1>
      <dl>
        <dt>should return an Error</dt>
        <dd><pre><code>request.get(base).end((err, res) =&#x3E; {
  const error = res.toError();
  assert.equal(error.status, 400);
  assert.equal(error.method, &#x27;GET&#x27;);
  assert.equal(error.path, &#x27;/&#x27;);
  assert.equal(error.message, &#x27;cannot GET / (400)&#x27;);
  assert.equal(error.text, &#x27;invalid json&#x27;);
  done();
});</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>[unix-sockets] http</h1>
      <dl>
        <section class="suite">
          <h1>request</h1>
          <dl>
            <dt>path: / (root)</dt>
            <dd><pre><code>request.get(&#x60;${base}/&#x60;).end((error, res) =&#x3E; {
  assert(res.ok);
  assert.strictEqual(&#x27;root ok!&#x27;, res.text);
  done();
});</code></pre></dd>
            <dt>path: /request/path</dt>
            <dd><pre><code>request.get(&#x60;${base}/request/path&#x60;).end((error, res) =&#x3E; {
  assert(res.ok);
  assert.strictEqual(&#x27;request path ok!&#x27;, res.text);
  done();
});</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>[unix-sockets] https</h1>
      <dl>
        <section class="suite">
          <h1>request</h1>
          <dl>
            <dt>path: / (root)</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/&#x60;)
  .ca(cacert)
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    assert(res.ok);
    assert.strictEqual(&#x27;root ok!&#x27;, res.text);
    done();
  });</code></pre></dd>
            <dt>path: /request/path</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/request/path&#x60;)
  .ca(cacert)
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    assert(res.ok);
    assert.strictEqual(&#x27;request path ok!&#x27;, res.text);
    done();
  });</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>req.get()</h1>
      <dl>
        <dt>should not set a default user-agent</dt>
        <dd><pre><code>request.get(&#x60;${base}/ua&#x60;).then((res) =&#x3E; {
      assert(res.headers);
      assert(!res.headers[&#x27;user-agent&#x27;]);
    })</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>utils.type(str)</h1>
      <dl>
        <dt>should return the mime type</dt>
        <dd><pre><code>utils
  .type(&#x27;application/json; charset=utf-8&#x27;)
  .should.equal(&#x27;application/json&#x27;);
utils.type(&#x27;application/json&#x27;).should.equal(&#x27;application/json&#x27;);</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>utils.params(str)</h1>
      <dl>
        <dt>should return the field parameters</dt>
        <dd><pre><code>const object = utils.params(&#x27;application/json; charset=utf-8; foo  = bar&#x27;);
object.charset.should.equal(&#x27;utf-8&#x27;);
object.foo.should.equal(&#x27;bar&#x27;);
utils.params(&#x27;application/json&#x27;).should.eql({});</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>utils.parseLinks(str)</h1>
      <dl>
        <dt>should parse links</dt>
        <dd><pre><code>const string_ =
  &#x27;&#x3C;https://api.github.com/repos/visionmedia/mocha/issues?page=2&#x3E;; rel=&#x22;next&#x22;, &#x3C;https://api.github.com/repos/visionmedia/mocha/issues?page=5&#x3E;; rel=&#x22;last&#x22;&#x27;;
const returnValue = utils.parseLinks(string_);
returnValue.next.should.equal(
  &#x27;https://api.github.com/repos/visionmedia/mocha/issues?page=2&#x27;
);
returnValue.last.should.equal(
  &#x27;https://api.github.com/repos/visionmedia/mocha/issues?page=5&#x27;
);</code></pre></dd>
      </dl>
    </section>
-------------------|---------|----------|---------|---------|---------------------------------------
File               | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s                     
-------------------|---------|----------|---------|---------|---------------------------------------
All files          |   85.79 |    79.93 |   78.06 |    86.6 |                                       
 src               |    92.5 |    83.83 |   91.83 |   93.84 |                                       
  agent-base.js    |     100 |      100 |     100 |     100 |                                       
  request-base.js  |   91.01 |     83.9 |   94.28 |   93.06 | ...21,262,316,501,525-533,579,757,768 
  response-base.js |     100 |      100 |      75 |     100 |                                       
  utils.js         |   92.85 |    71.42 |   85.71 |   91.66 | 94-98                                 
 src/node          |   82.28 |       78 |   68.42 |   82.94 |                                       
  agent.js         |   89.79 |    66.66 |     100 |   88.63 | 39,43,47,51,101                       
  http2wrapper.js  |    24.8 |     4.34 |       0 |   21.49 | ...76,180-181,185-186,190-191,196-198 
  index.js         |   92.49 |    83.03 |   87.71 |    93.1 | ...,977,1142,1182-1186,1220-1221,1301 
  response.js      |      90 |    83.33 |   55.55 |   89.79 | 78,86,94,120-121                      
  unzip.js         |     100 |    92.85 |     100 |     100 | 47                                    
 src/node/parsers  |   97.61 |       75 |     100 |   97.61 |                                       
  image.js         |     100 |      100 |     100 |     100 |                                       
  index.js         |     100 |      100 |     100 |     100 |                                       
  json.js          |     100 |       75 |     100 |     100 | 15                                    
  text.js          |     100 |      100 |     100 |     100 |                                       
  urlencoded.js    |      90 |      100 |     100 |      90 | 17                                    
-------------------|---------|----------|---------|---------|---------------------------------------
test on node with http2
test on plain node
    <section class="suite">
      <h1>Agent</h1>
      <dl>
        <dt>should remember defaults</dt>
        <dd><pre><code>if (typeof Promise === &#x27;undefined&#x27;) {
  return;
}
let called = 0;
let event_called = 0;
const agent = request
  .agent()
  .accept(&#x27;json&#x27;)
  .use(() =&#x3E; {
    called++;
  })
  .once(&#x27;request&#x27;, () =&#x3E; {
    event_called++;
  })
  .query({ hello: &#x27;world&#x27; })
  .set(&#x27;X-test&#x27;, &#x27;testing&#x27;);
assert.equal(0, called);
assert.equal(0, event_called);
return agent
  .get(&#x60;${base}/echo&#x60;)
  .then((res) =&#x3E; {
    assert.equal(1, called);
    assert.equal(1, event_called);
    assert.equal(&#x27;application/json&#x27;, res.headers.accept);
    assert.equal(&#x27;testing&#x27;, res.headers[&#x27;x-test&#x27;]);
    return agent.get(&#x60;${base}/querystring&#x60;);
  })
  .then((res) =&#x3E; {
    assert.equal(2, called);
    assert.equal(2, event_called);
    assert.deepEqual({ hello: &#x27;world&#x27; }, res.body);
  });</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>request</h1>
      <dl>
        <section class="suite">
          <h1>res.statusCode</h1>
          <dl>
            <dt>should set statusCode</dt>
            <dd><pre><code>request.get(&#x60;${uri}/login&#x60;, (error, res) =&#x3E; {
  try {
    assert.strictEqual(res.statusCode, 200);
    done();
  } catch (err) {
    done(err);
  }
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>should allow the send shorthand</h1>
          <dl>
            <dt>with callback in the method call</dt>
            <dd><pre><code>request.get(&#x60;${uri}/login&#x60;, (error, res) =&#x3E; {
  assert.equal(res.status, 200);
  done();
});</code></pre></dd>
            <dt>with data in the method call</dt>
            <dd><pre><code>request.post(&#x60;${uri}/echo&#x60;, { foo: &#x27;bar&#x27; }).end((error, res) =&#x3E; {
  assert.equal(&#x27;{&#x22;foo&#x22;:&#x22;bar&#x22;}&#x27;, res.text);
  done();
});</code></pre></dd>
            <dt>with callback and data in the method call</dt>
            <dd><pre><code>request.post(&#x60;${uri}/echo&#x60;, { foo: &#x27;bar&#x27; }, (error, res) =&#x3E; {
  assert.equal(&#x27;{&#x22;foo&#x22;:&#x22;bar&#x22;}&#x27;, res.text);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>with a callback</h1>
          <dl>
            <dt>should invoke .end()</dt>
            <dd><pre><code>request.get(&#x60;${uri}/login&#x60;, (error, res) =&#x3E; {
  try {
    assert.equal(res.status, 200);
    done();
  } catch (err) {
    done(err);
  }
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>.end()</h1>
          <dl>
            <dt>should issue a request</dt>
            <dd><pre><code>request.get(&#x60;${uri}/login&#x60;).end((error, res) =&#x3E; {
  try {
    assert.equal(res.status, 200);
    done();
  } catch (err) {
    done(err);
  }
});</code></pre></dd>
            <dt>is optional with a promise</dt>
            <dd><pre><code>if (typeof Promise === &#x27;undefined&#x27;) {
  return;
}
return request
  .get(&#x60;${uri}/login&#x60;)
  .then((res) =&#x3E; res.status)
  .then()
  .then((status) =&#x3E; {
    assert.equal(200, status, &#x27;Real promises pass results through&#x27;);
  });</code></pre></dd>
            <dt>called only once with a promise</dt>
            <dd><pre><code>if (typeof Promise === &#x27;undefined&#x27;) {
  return;
}
const request_ = request.get(&#x60;${uri}/unique&#x60;);
return Promise.all([request_, request_, request_]).then((results) =&#x3E; {
  for (const item of results) {
    assert.deepEqual(
      item.body,
      results[0].body,
      &#x27;It should keep returning the same result after being called once&#x27;
    );
  }
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>res.error</h1>
          <dl>
            <dt>ok</dt>
            <dd><pre><code>let calledErrorEvent = false;
let calledOKHandler = false;
request
  .get(&#x60;${uri}/error&#x60;)
  .ok((res) =&#x3E; {
    assert.strictEqual(500, res.status);
    calledOKHandler = true;
    return true;
  })
  .on(&#x27;error&#x27;, (error) =&#x3E; {
    calledErrorEvent = true;
  })
  .end((error, res) =&#x3E; {
    try {
      assert.ifError(error);
      assert.strictEqual(res.status, 500);
      assert(!calledErrorEvent);
      assert(calledOKHandler);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should be an Error object</dt>
            <dd><pre><code>let calledErrorEvent = false;
request
  .get(&#x60;${uri}/error&#x60;)
  .on(&#x27;error&#x27;, (error) =&#x3E; {
    assert.strictEqual(error.status, 500);
    calledErrorEvent = true;
  })
  .end((error, res) =&#x3E; {
    try {
      if (NODE) {
        res.error.message.should.equal(&#x27;cannot GET /error (500)&#x27;);
      } else {
        res.error.message.should.equal(&#x60;cannot GET ${uri}/error (500)&#x60;);
      }
      assert.strictEqual(res.error.status, 500);
      assert(error, &#x27;should have an error for 500&#x27;);
      assert.equal(error.message, &#x27;Internal Server Error&#x27;);
      assert(calledErrorEvent);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>with .then() promise</dt>
            <dd><pre><code>if (typeof Promise === &#x27;undefined&#x27;) {
  return;
}
return request.get(&#x60;${uri}/error&#x60;).then(
  () =&#x3E; {
    assert.fail();
  },
  (err) =&#x3E; {
    assert.equal(err.message, &#x27;Internal Server Error&#x27;);
  }
);</code></pre></dd>
            <dt>with .ok() returning false</dt>
            <dd><pre><code>if (typeof Promise === &#x27;undefined&#x27;) {
  return;
}
return request
  .get(&#x60;${uri}/echo&#x60;)
  .ok(() =&#x3E; false)
  .then(
    () =&#x3E; {
      assert.fail();
    },
    (err) =&#x3E; {
      assert.equal(200, err.response.status);
      assert.equal(err.message, &#x27;OK&#x27;);
    }
  );</code></pre></dd>
            <dt>with .ok() throwing an Error</dt>
            <dd><pre><code>if (typeof Promise === &#x27;undefined&#x27;) {
  return;
}
return request
  .get(&#x60;${uri}/echo&#x60;)
  .ok(() =&#x3E; {
    throw new Error(&#x27;boom&#x27;);
  })
  .then(
    () =&#x3E; {
      assert.fail();
    },
    (err) =&#x3E; {
      assert.equal(200, err.status);
      assert.equal(200, err.response.status);
      assert.equal(err.message, &#x27;boom&#x27;);
    }
  );</code></pre></dd>
            <dt>with .ok() throwing an Error with status</dt>
            <dd><pre><code>if (typeof Promise === &#x27;undefined&#x27;) {
  return;
}
return request
  .get(&#x60;${uri}/echo&#x60;)
  .ok(() =&#x3E; {
    const err = new Error(&#x27;boom&#x27;);
    err.status = 404;
    throw err;
  })
  .then(
    () =&#x3E; {
      assert.fail();
    },
    (err) =&#x3E; {
      assert.equal(404, err.status);
      assert.equal(200, err.response.status);
      assert.equal(err.message, &#x27;boom&#x27;);
    }
  );</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>res.header</h1>
          <dl>
            <dt>should be an object</dt>
            <dd><pre><code>request.get(&#x60;${uri}/login&#x60;).end((error, res) =&#x3E; {
  try {
    assert.equal(&#x27;Express&#x27;, res.header[&#x27;x-powered-by&#x27;]);
    done();
  } catch (err) {
    done(err);
  }
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>set headers</h1>
          <dl>
            <dt>should only set headers for ownProperties of header</dt>
            <dd><pre><code>try {
  request
    .get(&#x60;${uri}/echo-headers&#x60;)
    .set(&#x27;valid&#x27;, &#x27;ok&#x27;)
    .end((error, res) =&#x3E; {
      if (
        !error &#x26;&#x26;
        res.body &#x26;&#x26;
        res.body.valid &#x26;&#x26;
        !res.body.hasOwnProperty(&#x27;invalid&#x27;)
      ) {
        return done();
      }
      done(error || new Error(&#x27;fail&#x27;));
    });
} catch (err) {
  done(err);
}</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>res.charset</h1>
          <dl>
            <dt>should be set when present</dt>
            <dd><pre><code>request.get(&#x60;${uri}/login&#x60;).end((error, res) =&#x3E; {
  try {
    res.charset.should.equal(&#x27;utf-8&#x27;);
    done();
  } catch (err) {
    done(err);
  }
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>res.statusType</h1>
          <dl>
            <dt>should provide the first digit</dt>
            <dd><pre><code>request.get(&#x60;${uri}/login&#x60;).end((error, res) =&#x3E; {
  try {
    assert(!error, &#x27;should not have an error for success responses&#x27;);
    assert.equal(200, res.status);
    assert.equal(2, res.statusType);
    done();
  } catch (err) {
    done(err);
  }
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>res.type</h1>
          <dl>
            <dt>should provide the mime-type void of params</dt>
            <dd><pre><code>request.get(&#x60;${uri}/login&#x60;).end((error, res) =&#x3E; {
  try {
    res.type.should.equal(&#x27;text/html&#x27;);
    res.charset.should.equal(&#x27;utf-8&#x27;);
    done();
  } catch (err) {
    done(err);
  }
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.set(field, val)</h1>
          <dl>
            <dt>should set the header field</dt>
            <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .set(&#x27;X-Foo&#x27;, &#x27;bar&#x27;)
  .set(&#x27;X-Bar&#x27;, &#x27;baz&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;bar&#x27;, res.header[&#x27;x-foo&#x27;]);
      assert.equal(&#x27;baz&#x27;, res.header[&#x27;x-bar&#x27;]);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.set(obj)</h1>
          <dl>
            <dt>should set the header fields</dt>
            <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .set({ &#x27;X-Foo&#x27;: &#x27;bar&#x27;, &#x27;X-Bar&#x27;: &#x27;baz&#x27; })
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;bar&#x27;, res.header[&#x27;x-foo&#x27;]);
      assert.equal(&#x27;baz&#x27;, res.header[&#x27;x-bar&#x27;]);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.type(str)</h1>
          <dl>
            <dt>should set the Content-Type</dt>
            <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .type(&#x27;text/x-foo&#x27;)
  .end((error, res) =&#x3E; {
    try {
      res.header[&#x27;content-type&#x27;].should.equal(&#x27;text/x-foo&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should map &#x22;json&#x22;</dt>
            <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .type(&#x27;json&#x27;)
  .send(&#x27;{&#x22;a&#x22;: 1}&#x27;)
  .end((error, res) =&#x3E; {
    try {
      res.should.be.json();
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should map &#x22;html&#x22;</dt>
            <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .type(&#x27;html&#x27;)
  .end((error, res) =&#x3E; {
    try {
      res.header[&#x27;content-type&#x27;].should.equal(&#x27;text/html&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.accept(str)</h1>
          <dl>
            <dt>should set Accept</dt>
            <dd><pre><code>request
  .get(&#x60;${uri}/echo&#x60;)
  .accept(&#x27;text/x-foo&#x27;)
  .end((error, res) =&#x3E; {
    try {
      res.header.accept.should.equal(&#x27;text/x-foo&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should map &#x22;json&#x22;</dt>
            <dd><pre><code>request
  .get(&#x60;${uri}/echo&#x60;)
  .accept(&#x27;json&#x27;)
  .end((error, res) =&#x3E; {
    try {
      res.header.accept.should.equal(&#x27;application/json&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should map &#x22;xml&#x22;</dt>
            <dd><pre><code>request
  .get(&#x60;${uri}/echo&#x60;)
  .accept(&#x27;xml&#x27;)
  .end((error, res) =&#x3E; {
    try {
      // Mime module keeps changing this :(
      assert(
        res.header.accept == &#x27;application/xml&#x27; ||
          res.header.accept == &#x27;text/xml&#x27;
      );
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should map &#x22;html&#x22;</dt>
            <dd><pre><code>request
  .get(&#x60;${uri}/echo&#x60;)
  .accept(&#x27;html&#x27;)
  .end((error, res) =&#x3E; {
    try {
      res.header.accept.should.equal(&#x27;text/html&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.send(str)</h1>
          <dl>
            <dt>should write the string</dt>
            <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .type(&#x27;json&#x27;)
  .send(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;}&#x27;)
  .end((error, res) =&#x3E; {
    try {
      res.text.should.equal(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;}&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.send(Object)</h1>
          <dl>
            <dt>should default to json</dt>
            <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .send({ name: &#x27;tobi&#x27; })
  .end((error, res) =&#x3E; {
    try {
      res.should.be.json();
      res.text.should.equal(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;}&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <section class="suite">
              <h1>when called several times</h1>
              <dl>
                <dt>should merge the objects</dt>
                <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .send({ name: &#x27;tobi&#x27; })
  .send({ age: 1 })
  .end((error, res) =&#x3E; {
    try {
      res.should.be.json();
      if (NODE) {
        res.buffered.should.be.true();
      }
      res.text.should.equal(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;,&#x22;age&#x22;:1}&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
              </dl>
            </section>
          </dl>
        </section>
        <section class="suite">
          <h1>.end(fn)</h1>
          <dl>
            <dt>should check arity</dt>
            <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .send({ name: &#x27;tobi&#x27; })
  .end((error, res) =&#x3E; {
    try {
      assert.ifError(error);
      res.text.should.equal(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;}&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should emit request</dt>
            <dd><pre><code>const request_ = request.post(&#x60;${uri}/echo&#x60;);
request_.on(&#x27;request&#x27;, (request) =&#x3E; {
  assert.equal(request_, request);
  done();
});
request_.end();</code></pre></dd>
            <dt>should emit response</dt>
            <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .send({ name: &#x27;tobi&#x27; })
  .on(&#x27;response&#x27;, (res) =&#x3E; {
    res.text.should.equal(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;}&#x27;);
    done();
  })
  .end();</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>.then(fulfill, reject)</h1>
          <dl>
            <dt>should support successful fulfills with .then(fulfill)</dt>
            <dd><pre><code>if (typeof Promise === &#x27;undefined&#x27;) {
  return done();
}
request
  .post(&#x60;${uri}/echo&#x60;)
  .send({ name: &#x27;tobi&#x27; })
  .then((res) =&#x3E; {
    res.type.should.equal(&#x27;application/json&#x27;);
    res.text.should.equal(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;}&#x27;);
    done();
  });</code></pre></dd>
            <dt>should reject an error with .then(null, reject)</dt>
            <dd><pre><code>if (typeof Promise === &#x27;undefined&#x27;) {
  return done();
}
request.get(&#x60;${uri}/error&#x60;).then(null, (err) =&#x3E; {
  assert.equal(err.status, 500);
  assert.equal(err.response.text, &#x27;boom&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>.catch(reject)</h1>
          <dl>
            <dt>should reject an error with .catch(reject)</dt>
            <dd><pre><code>if (typeof Promise === &#x27;undefined&#x27;) {
  return done();
}
request.get(&#x60;${uri}/error&#x60;).catch((err) =&#x3E; {
  assert.equal(err.status, 500);
  assert.equal(err.response.text, &#x27;boom&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>.abort()</h1>
          <dl>
            <dt>should abort the request</dt>
            <dd><pre><code>const request_ = request.get(&#x60;${uri}/delay/3000&#x60;);
request_.end((error, res) =&#x3E; {
  try {
    assert(false, &#x27;should not complete the request&#x27;);
  } catch (err) {
    done(err);
  }
});
request_.on(&#x27;error&#x27;, (error) =&#x3E; {
  done(error);
});
request_.on(&#x27;abort&#x27;, done);
setTimeout(() =&#x3E; {
  request_.abort();
}, 500);</code></pre></dd>
            <dt>should abort the promise</dt>
            <dd><pre><code>const request_ = request.get(&#x60;${uri}/delay/3000&#x60;);
setTimeout(() =&#x3E; {
  request_.abort();
}, 10);
return request_.then(
  () =&#x3E; {
    assert.fail(&#x27;should not complete the request&#x27;);
  },
  (err) =&#x3E; {
    assert.equal(&#x27;ABORTED&#x27;, err.code);
  }
);</code></pre></dd>
            <dt>should allow chaining .abort() several times</dt>
            <dd><pre><code>const request_ = request.get(&#x60;${uri}/delay/3000&#x60;);
request_.end((error, res) =&#x3E; {
  try {
    assert(false, &#x27;should not complete the request&#x27;);
  } catch (err) {
    done(err);
  }
});
// This also verifies only a single &#x27;done&#x27; event is emitted
request_.on(&#x27;abort&#x27;, done);
setTimeout(() =&#x3E; {
  request_.abort().abort().abort();
}, 1000);</code></pre></dd>
            <dt>should not allow abort then end</dt>
            <dd><pre><code>request
  .get(&#x60;${uri}/delay/3000&#x60;)
  .abort()
  .end((error, res) =&#x3E; {
    done(error ? undefined : new Error(&#x27;Expected abort error&#x27;));
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.toJSON()</h1>
          <dl>
            <dt>should describe the request</dt>
            <dd><pre><code>const request_ = request.post(&#x60;${uri}/echo&#x60;).send({ foo: &#x27;baz&#x27; });
request_.end((error, res) =&#x3E; {
  try {
    const json = request_.toJSON();
    assert.equal(&#x27;POST&#x27;, json.method);
    assert(/\/echo$/.test(json.url));
    assert.equal(&#x27;baz&#x27;, json.data.foo);
    done();
  } catch (err) {
    done(err);
  }
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.options()</h1>
          <dl>
            <dt>should allow request body</dt>
            <dd><pre><code>request
  .options(&#x60;${uri}/options/echo/body&#x60;)
  .send({ foo: &#x27;baz&#x27; })
  .end((error, res) =&#x3E; {
    try {
      assert.equal(error, null);
      assert.strictEqual(res.body.foo, &#x27;baz&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.sortQuery()</h1>
          <dl>
            <dt>nop with no querystring</dt>
            <dd><pre><code>request
  .get(&#x60;${uri}/url&#x60;)
  .sortQuery()
  .end((error, res) =&#x3E; {
    try {
      assert.equal(res.text, &#x27;/url&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should sort the request querystring</dt>
            <dd><pre><code>request
  .get(&#x60;${uri}/url&#x60;)
  .query(&#x27;search=Manny&#x27;)
  .query(&#x27;order=desc&#x27;)
  .sortQuery()
  .end((error, res) =&#x3E; {
    try {
      assert.equal(res.text, &#x27;/url?order=desc&#x26;search=Manny&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should allow disabling sorting</dt>
            <dd><pre><code>request
  .get(&#x60;${uri}/url&#x60;)
  .query(&#x27;search=Manny&#x27;)
  .query(&#x27;order=desc&#x27;)
  .sortQuery() // take default of true
  .sortQuery(false) // override it in later call
  .end((error, res) =&#x3E; {
    try {
      assert.equal(res.text, &#x27;/url?search=Manny&#x26;order=desc&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should sort the request querystring using customized function</dt>
            <dd><pre><code>request
  .get(&#x60;${uri}/url&#x60;)
  .query(&#x27;name=Nick&#x27;)
  .query(&#x27;search=Manny&#x27;)
  .query(&#x27;order=desc&#x27;)
  .sortQuery((a, b) =&#x3E; a.length - b.length)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(res.text, &#x27;/url?name=Nick&#x26;order=desc&#x26;search=Manny&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>req.set(&#x22;Content-Type&#x22;, contentType)</h1>
      <dl>
        <dt>should work with just the contentType component</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .set(&#x27;Content-Type&#x27;, &#x27;application/json&#x27;)
  .send({ name: &#x27;tobi&#x27; })
  .end((error) =&#x3E; {
    assert(!error);
    done();
  });</code></pre></dd>
        <dt>should work with the charset component</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .set(&#x27;Content-Type&#x27;, &#x27;application/json; charset=utf-8&#x27;)
  .send({ name: &#x27;tobi&#x27; })
  .end((error) =&#x3E; {
    assert(!error);
    done();
  });</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>req.send(Object) as &#x22;form&#x22;</h1>
      <dl>
        <section class="suite">
          <h1>with req.type() set to form</h1>
          <dl>
            <dt>should send x-www-form-urlencoded data</dt>
            <dd><pre><code>request
  .post(&#x60;${base}/echo&#x60;)
  .type(&#x27;form&#x27;)
  .send({ name: &#x27;tobi&#x27; })
  .end((error, res) =&#x3E; {
    res.header[&#x27;content-type&#x27;].should.equal(
      &#x27;application/x-www-form-urlencoded&#x27;
    );
    res.text.should.equal(&#x27;name=tobi&#x27;);
    done();
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>when called several times</h1>
          <dl>
            <dt>should merge the objects</dt>
            <dd><pre><code>request
  .post(&#x60;${base}/echo&#x60;)
  .type(&#x27;form&#x27;)
  .send({ name: { first: &#x27;tobi&#x27;, last: &#x27;holowaychuk&#x27; } })
  .send({ age: &#x27;1&#x27; })
  .end((error, res) =&#x3E; {
    res.header[&#x27;content-type&#x27;].should.equal(
      &#x27;application/x-www-form-urlencoded&#x27;
    );
    res.text.should.equal(
      &#x27;name%5Bfirst%5D=tobi&#x26;name%5Blast%5D=holowaychuk&#x26;age=1&#x27;
    );
    done();
  });</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>req.attach</h1>
      <dl>
        <dt>ignores null file</dt>
        <dd><pre><code>request
  .post(&#x27;/echo&#x27;)
  .attach(&#x27;image&#x27;, null)
  .end((error, res) =&#x3E; {
    done();
  });</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>req.field</h1>
      <dl>
        <dt>allow bools</dt>
        <dd><pre><code>if (!formDataSupported) {
  return done();
}
request
  .post(&#x60;${base}/formecho&#x60;)
  .field(&#x27;bools&#x27;, true)
  .field(&#x27;strings&#x27;, &#x27;true&#x27;)
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    assert.deepStrictEqual(res.body, { bools: &#x27;true&#x27;, strings: &#x27;true&#x27; });
    done();
  });</code></pre></dd>
        <dt>allow objects</dt>
        <dd><pre><code>if (!formDataSupported) {
  return done();
}
request
  .post(&#x60;${base}/formecho&#x60;)
  .field({ bools: true, strings: &#x27;true&#x27; })
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    assert.deepStrictEqual(res.body, { bools: &#x27;true&#x27;, strings: &#x27;true&#x27; });
    done();
  });</code></pre></dd>
        <dt>works with arrays in objects</dt>
        <dd><pre><code>if (!formDataSupported) {
  return done();
}
request
  .post(&#x60;${base}/formecho&#x60;)
  .field({ numbers: [1, 2, 3] })
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    assert.deepStrictEqual(res.body, { numbers: [&#x27;1&#x27;, &#x27;2&#x27;, &#x27;3&#x27;] });
    done();
  });</code></pre></dd>
        <dt>works with arrays</dt>
        <dd><pre><code>if (!formDataSupported) {
  return done();
}
request
  .post(&#x60;${base}/formecho&#x60;)
  .field(&#x27;letters&#x27;, [&#x27;a&#x27;, &#x27;b&#x27;, &#x27;c&#x27;])
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    assert.deepStrictEqual(res.body, { letters: [&#x27;a&#x27;, &#x27;b&#x27;, &#x27;c&#x27;] });
    done();
  });</code></pre></dd>
        <dt>throw when empty</dt>
        <dd><pre><code>should.throws(() =&#x3E; {
  request.post(&#x60;${base}/echo&#x60;).field();
}, /name/);
should.throws(() =&#x3E; {
  request.post(&#x60;${base}/echo&#x60;).field(&#x27;name&#x27;);
}, /val/);</code></pre></dd>
        <dt>cannot be mixed with send()</dt>
        <dd><pre><code>assert.throws(() =&#x3E; {
  request.post(&#x27;/echo&#x27;).field(&#x27;form&#x27;, &#x27;data&#x27;).send(&#x27;hi&#x27;);
});
assert.throws(() =&#x3E; {
  request.post(&#x27;/echo&#x27;).send(&#x27;hi&#x27;).field(&#x27;form&#x27;, &#x27;data&#x27;);
});</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>req.send(Object) as &#x22;json&#x22;</h1>
      <dl>
        <dt>should default to json</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .send({ name: &#x27;tobi&#x27; })
  .end((error, res) =&#x3E; {
    res.should.be.json();
    res.text.should.equal(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;}&#x27;);
    done();
  });</code></pre></dd>
        <dt>should work with arrays</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .send([1, 2, 3])
  .end((error, res) =&#x3E; {
    res.should.be.json();
    res.text.should.equal(&#x27;[1,2,3]&#x27;);
    done();
  });</code></pre></dd>
        <dt>should work with value null</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .type(&#x27;json&#x27;)
  .send(&#x27;null&#x27;)
  .end((error, res) =&#x3E; {
    res.should.be.json();
    assert.strictEqual(res.body, null);
    done();
  });</code></pre></dd>
        <dt>should work with value false</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .type(&#x27;json&#x27;)
  .send(&#x27;false&#x27;)
  .end((error, res) =&#x3E; {
    res.should.be.json();
    res.body.should.equal(false);
    done();
  });</code></pre></dd>
        <dt>should work with empty string value</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .type(&#x27;json&#x27;)
  .send(&#x27;&#x22;&#x22;&#x27;)
  .end((error, res) =&#x3E; {
    res.should.be.json();
    res.body.should.equal(&#x27;&#x27;);
    done();
  });</code></pre></dd>
        <dt>should work with vendor MIME type</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .set(&#x27;Content-Type&#x27;, &#x27;application/vnd.example+json&#x27;)
  .send({ name: &#x27;vendor&#x27; })
  .end((error, res) =&#x3E; {
    res.text.should.equal(&#x27;{&#x22;name&#x22;:&#x22;vendor&#x22;}&#x27;);
    ({ name: &#x27;vendor&#x27; }.should.eql(res.body));
    done();
  });</code></pre></dd>
        <section class="suite">
          <h1>when called several times</h1>
          <dl>
            <dt>should merge the objects</dt>
            <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .send({ name: &#x27;tobi&#x27; })
  .send({ age: 1 })
  .end((error, res) =&#x3E; {
    res.should.be.json();
    res.text.should.equal(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;,&#x22;age&#x22;:1}&#x27;);
    ({ name: &#x27;tobi&#x27;, age: 1 }.should.eql(res.body));
    done();
  });</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>res.body</h1>
      <dl>
        <section class="suite">
          <h1>application/json</h1>
          <dl>
            <dt>should parse the body</dt>
            <dd><pre><code>request.get(&#x60;${uri}/json&#x60;).end((error, res) =&#x3E; {
  res.text.should.equal(&#x27;{&#x22;name&#x22;:&#x22;manny&#x22;}&#x27;);
  res.body.should.eql({ name: &#x27;manny&#x27; });
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>Invalid JSON response</h1>
          <dl>
            <dt>should return the raw response</dt>
            <dd><pre><code>request.get(&#x60;${uri}/invalid-json&#x60;).end((error, res) =&#x3E; {
  assert.deepEqual(
    error.rawResponse,
    &#x22;)]}&#x27;, {&#x27;header&#x27;:{&#x27;code&#x27;:200,&#x27;text&#x27;:&#x27;OK&#x27;,&#x27;version&#x27;:&#x27;1.0&#x27;},&#x27;data&#x27;:&#x27;some data&#x27;}&#x22;
  );
  done();
});</code></pre></dd>
            <dt>should return the http status code</dt>
            <dd><pre><code>request.get(&#x60;${uri}/invalid-json-forbidden&#x60;).end((error, res) =&#x3E; {
  assert.equal(error.statusCode, 403);
  done();
});</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>request</h1>
      <dl>
        <section class="suite">
          <h1>on redirect</h1>
          <dl>
            <dt>should retain header fields</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/header&#x60;)
  .set(&#x27;X-Foo&#x27;, &#x27;bar&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert(res.body);
      res.body.should.have.property(&#x27;x-foo&#x27;, &#x27;bar&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should preserve timeout across redirects</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/movies/random&#x60;)
  .timeout(250)
  .end((error, res) =&#x3E; {
    try {
      assert(error instanceof Error, &#x27;expected an error&#x27;);
      error.should.have.property(&#x27;timeout&#x27;, 250);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should successfully redirect after retry on error</dt>
            <dd><pre><code>const id = Math.random() * 1_000_000 * Date.now();
request
  .get(&#x60;${base}/error/redirect/${id}&#x60;)
  .retry(2)
  .end((error, res) =&#x3E; {
    assert(res.ok, &#x27;response should be ok&#x27;);
    assert(res.text, &#x27;first movie page&#x27;);
    done();
  });</code></pre></dd>
            <dt>should preserve retries across redirects</dt>
            <dd><pre><code>const id = Math.random() * 1_000_000 * Date.now();
request
  .get(&#x60;${base}/error/redirect-error${id}&#x60;)
  .retry(2)
  .end((error, res) =&#x3E; {
    assert(error, &#x27;expected an error&#x27;);
    assert.equal(2, error.retries, &#x27;expected an error with .retries&#x27;);
    assert.equal(500, error.status, &#x27;expected an error status of 500&#x27;);
    done();
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>on 303</h1>
          <dl>
            <dt>should redirect with same method</dt>
            <dd><pre><code>request
  .put(&#x60;${base}/redirect-303&#x60;)
  .send({ msg: &#x27;hello&#x27; })
  .redirects(1)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    res.headers.location.should.equal(&#x27;/reply-method&#x27;);
  })
  .end((error, res) =&#x3E; {
    if (error) {
      done(error);
      return;
    }
    res.text.should.equal(&#x27;method=get&#x27;);
    done();
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>on 307</h1>
          <dl>
            <dt>should redirect with same method</dt>
            <dd><pre><code>if (isMSIE) return done(); // IE9 broken
request
  .put(&#x60;${base}/redirect-307&#x60;)
  .send({ msg: &#x27;hello&#x27; })
  .redirects(1)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    res.headers.location.should.equal(&#x27;/reply-method&#x27;);
  })
  .end((error, res) =&#x3E; {
    if (error) {
      done(error);
      return;
    }
    res.text.should.equal(&#x27;method=put&#x27;);
    done();
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>on 308</h1>
          <dl>
            <dt>should redirect with same method</dt>
            <dd><pre><code>if (isMSIE) return done(); // IE9 broken
request
  .put(&#x60;${base}/redirect-308&#x60;)
  .send({ msg: &#x27;hello&#x27; })
  .redirects(1)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    res.headers.location.should.equal(&#x27;/reply-method&#x27;);
  })
  .end((error, res) =&#x3E; {
    if (error) {
      done(error);
      return;
    }
    res.text.should.equal(&#x27;method=put&#x27;);
    done();
  });</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>request</h1>
      <dl>
        <dt>Request inheritance</dt>
        <dd><pre><code>assert(request.get(&#x60;${uri}/&#x60;) instanceof request.Request);</code></pre></dd>
        <dt>request() simple GET without callback</dt>
        <dd><pre><code>request(&#x27;GET&#x27;, &#x27;test/test.request.js&#x27;).end();
next();</code></pre></dd>
        <dt>request() simple GET</dt>
        <dd><pre><code>request(&#x27;GET&#x27;, &#x60;${uri}/ok&#x60;).end((error, res) =&#x3E; {
  try {
    assert(res instanceof request.Response, &#x27;respond with Response&#x27;);
    assert(res.ok, &#x27;response should be ok&#x27;);
    assert(res.text, &#x27;res.text&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request() simple HEAD</dt>
        <dd><pre><code>request.head(&#x60;${uri}/ok&#x60;).end((error, res) =&#x3E; {
  try {
    assert(res instanceof request.Response, &#x27;respond with Response&#x27;);
    assert(res.ok, &#x27;response should be ok&#x27;);
    assert(!res.text, &#x27;res.text&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request() GET 5xx</dt>
        <dd><pre><code>request(&#x27;GET&#x27;, &#x60;${uri}/error&#x60;).end((error, res) =&#x3E; {
  try {
    assert(error);
    assert.equal(error.message, &#x27;Internal Server Error&#x27;);
    assert(!res.ok, &#x27;response should not be ok&#x27;);
    assert(res.error, &#x27;response should be an error&#x27;);
    assert(!res.clientError, &#x27;response should not be a client error&#x27;);
    assert(res.serverError, &#x27;response should be a server error&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request() GET 4xx</dt>
        <dd><pre><code>request(&#x27;GET&#x27;, &#x60;${uri}/notfound&#x60;).end((error, res) =&#x3E; {
  try {
    assert(error);
    assert.equal(error.message, &#x27;Not Found&#x27;);
    assert(!res.ok, &#x27;response should not be ok&#x27;);
    assert(res.error, &#x27;response should be an error&#x27;);
    assert(res.clientError, &#x27;response should be a client error&#x27;);
    assert(!res.serverError, &#x27;response should not be a server error&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request() GET 404 Not Found</dt>
        <dd><pre><code>request(&#x27;GET&#x27;, &#x60;${uri}/notfound&#x60;).end((error, res) =&#x3E; {
  try {
    assert(error);
    assert(res.notFound, &#x27;response should be .notFound&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request() GET 400 Bad Request</dt>
        <dd><pre><code>request(&#x27;GET&#x27;, &#x60;${uri}/bad-request&#x60;).end((error, res) =&#x3E; {
  try {
    assert(error);
    assert(res.badRequest, &#x27;response should be .badRequest&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request() GET 401 Bad Request</dt>
        <dd><pre><code>request(&#x27;GET&#x27;, &#x60;${uri}/unauthorized&#x60;).end((error, res) =&#x3E; {
  try {
    assert(error);
    assert(res.unauthorized, &#x27;response should be .unauthorized&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request() GET 406 Not Acceptable</dt>
        <dd><pre><code>request(&#x27;GET&#x27;, &#x60;${uri}/not-acceptable&#x60;).end((error, res) =&#x3E; {
  try {
    assert(error);
    assert(res.notAcceptable, &#x27;response should be .notAcceptable&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request() GET 204 No Content</dt>
        <dd><pre><code>request(&#x27;GET&#x27;, &#x60;${uri}/no-content&#x60;).end((error, res) =&#x3E; {
  try {
    assert.ifError(error);
    assert(res.noContent, &#x27;response should be .noContent&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request() DELETE 204 No Content</dt>
        <dd><pre><code>request(&#x27;DELETE&#x27;, &#x60;${uri}/no-content&#x60;).end((error, res) =&#x3E; {
  try {
    assert.ifError(error);
    assert(res.noContent, &#x27;response should be .noContent&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request() header parsing</dt>
        <dd><pre><code>request(&#x27;GET&#x27;, &#x60;${uri}/notfound&#x60;).end((error, res) =&#x3E; {
  try {
    assert(error);
    assert.equal(&#x27;text/html; charset=utf-8&#x27;, res.header[&#x27;content-type&#x27;]);
    assert.equal(&#x27;Express&#x27;, res.header[&#x27;x-powered-by&#x27;]);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request() .status</dt>
        <dd><pre><code>request(&#x27;GET&#x27;, &#x60;${uri}/notfound&#x60;).end((error, res) =&#x3E; {
  try {
    assert(error);
    assert.equal(404, res.status, &#x27;response .status&#x27;);
    assert.equal(4, res.statusType, &#x27;response .statusType&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>get()</dt>
        <dd><pre><code>request.get(&#x60;${uri}/notfound&#x60;).end((error, res) =&#x3E; {
  try {
    assert(error);
    assert.equal(404, res.status, &#x27;response .status&#x27;);
    assert.equal(4, res.statusType, &#x27;response .statusType&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>put()</dt>
        <dd><pre><code>request.put(&#x60;${uri}/user/12&#x60;).end((error, res) =&#x3E; {
  try {
    assert.equal(&#x27;updated&#x27;, res.text, &#x27;response text&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>put().send()</dt>
        <dd><pre><code>request
  .put(&#x60;${uri}/user/13/body&#x60;)
  .send({ user: &#x27;new&#x27; })
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;received new&#x27;, res.text, &#x27;response text&#x27;);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>post()</dt>
        <dd><pre><code>request.post(&#x60;${uri}/user&#x60;).end((error, res) =&#x3E; {
  try {
    assert.equal(&#x27;created&#x27;, res.text, &#x27;response text&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>del()</dt>
        <dd><pre><code>request.del(&#x60;${uri}/user/12&#x60;).end((error, res) =&#x3E; {
  try {
    assert.equal(&#x27;deleted&#x27;, res.text, &#x27;response text&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>delete()</dt>
        <dd><pre><code>request.delete(&#x60;${uri}/user/12&#x60;).end((error, res) =&#x3E; {
  try {
    assert.equal(&#x27;deleted&#x27;, res.text, &#x27;response text&#x27;);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>post() data</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/todo/item&#x60;)
  .type(&#x27;application/octet-stream&#x27;)
  .send(&#x27;tobi&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;added &#x22;tobi&#x22;&#x27;, res.text, &#x27;response text&#x27;);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>request .type()</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/user/12/pet&#x60;)
  .type(&#x27;urlencoded&#x27;)
  .send(&#x27;pet=tobi&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;added pet &#x22;tobi&#x22;&#x27;, res.text, &#x27;response text&#x27;);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>request .type() with alias</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/user/12/pet&#x60;)
  .type(&#x27;application/x-www-form-urlencoded&#x27;)
  .send(&#x27;pet=tobi&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;added pet &#x22;tobi&#x22;&#x27;, res.text, &#x27;response text&#x27;);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>request .get() with no data or callback</dt>
        <dd><pre><code>request.get(&#x60;${uri}/echo-header/content-type&#x60;);
next();</code></pre></dd>
        <dt>request .send() with no data only</dt>
        <dd><pre><code>request.post(&#x60;${uri}/user/5/pet&#x60;).type(&#x27;urlencoded&#x27;).send(&#x27;pet=tobi&#x27;);
next();</code></pre></dd>
        <dt>request .send() with callback only</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/echo-header/accept&#x60;)
  .set(&#x27;Accept&#x27;, &#x27;foo/bar&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;foo/bar&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>request .accept() with json</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/echo-header/accept&#x60;)
  .accept(&#x27;json&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;application/json&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>request .accept() with application/json</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/echo-header/accept&#x60;)
  .accept(&#x27;application/json&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;application/json&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>request .accept() with xml</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/echo-header/accept&#x60;)
  .accept(&#x27;xml&#x27;)
  .end((error, res) =&#x3E; {
    try {
      // We can&#x27;t depend on mime module to be consistent with this
      assert(res.text == &#x27;application/xml&#x27; || res.text == &#x27;text/xml&#x27;);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>request .accept() with application/xml</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/echo-header/accept&#x60;)
  .accept(&#x27;application/xml&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;application/xml&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>request .end()</dt>
        <dd><pre><code>request
  .put(&#x60;${uri}/echo-header/content-type&#x60;)
  .set(&#x27;Content-Type&#x27;, &#x27;text/plain&#x27;)
  .send(&#x27;wahoo&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;text/plain&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>request .send()</dt>
        <dd><pre><code>request
  .put(&#x60;${uri}/echo-header/content-type&#x60;)
  .set(&#x27;Content-Type&#x27;, &#x27;text/plain&#x27;)
  .send(&#x27;wahoo&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;text/plain&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>request .set()</dt>
        <dd><pre><code>request
  .put(&#x60;${uri}/echo-header/content-type&#x60;)
  .set(&#x27;Content-Type&#x27;, &#x27;text/plain&#x27;)
  .send(&#x27;wahoo&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;text/plain&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>request .set(object)</dt>
        <dd><pre><code>request
  .put(&#x60;${uri}/echo-header/content-type&#x60;)
  .set({ &#x27;Content-Type&#x27;: &#x27;text/plain&#x27; })
  .send(&#x27;wahoo&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;text/plain&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>POST urlencoded</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/pet&#x60;)
  .type(&#x27;urlencoded&#x27;)
  .send({ name: &#x27;Manny&#x27;, species: &#x27;cat&#x27; })
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;added Manny the cat&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>POST json</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/pet&#x60;)
  .type(&#x27;json&#x27;)
  .send({ name: &#x27;Manny&#x27;, species: &#x27;cat&#x27; })
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;added Manny the cat&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>POST json array</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .send([1, 2, 3])
  .end((error, res) =&#x3E; {
    try {
      assert.equal(
        &#x27;application/json&#x27;,
        res.header[&#x27;content-type&#x27;].split(&#x27;;&#x27;)[0]
      );
      assert.equal(&#x27;[1,2,3]&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>POST json default</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/pet&#x60;)
  .send({ name: &#x27;Manny&#x27;, species: &#x27;cat&#x27; })
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;added Manny the cat&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>POST json contentType charset</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .set(&#x27;Content-Type&#x27;, &#x27;application/json; charset=UTF-8&#x27;)
  .send({ data: [&#x27;data1&#x27;, &#x27;data2&#x27;] })
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;{&#x22;data&#x22;:[&#x22;data1&#x22;,&#x22;data2&#x22;]}&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>POST json contentType vendor</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .set(&#x27;Content-Type&#x27;, &#x27;application/vnd.example+json&#x27;)
  .send({ data: [&#x27;data1&#x27;, &#x27;data2&#x27;] })
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;{&#x22;data&#x22;:[&#x22;data1&#x22;,&#x22;data2&#x22;]}&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>POST multiple .send() calls</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/pet&#x60;)
  .send({ name: &#x27;Manny&#x27; })
  .send({ species: &#x27;cat&#x27; })
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;added Manny the cat&#x27;, res.text);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>POST multiple .send() strings</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/echo&#x60;)
  .send(&#x27;user[name]=tj&#x27;)
  .send(&#x27;user[email]=tj@vision-media.ca&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(
        &#x27;application/x-www-form-urlencoded&#x27;,
        res.header[&#x27;content-type&#x27;].split(&#x27;;&#x27;)[0]
      );
      assert.equal(
        res.text,
        &#x27;user[name]=tj&#x26;user[email]=tj@vision-media.ca&#x27;
      );
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>POST with no data</dt>
        <dd><pre><code>request
  .post(&#x60;${uri}/empty-body&#x60;)
  .send()
  .end((error, res) =&#x3E; {
    try {
      assert.ifError(error);
      assert(res.noContent, &#x27;response should be .noContent&#x27;);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>GET .type</dt>
        <dd><pre><code>request.get(&#x60;${uri}/pets&#x60;).end((error, res) =&#x3E; {
  try {
    assert.equal(&#x27;application/json&#x27;, res.type);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>GET Content-Type params</dt>
        <dd><pre><code>request.get(&#x60;${uri}/text&#x60;).end((error, res) =&#x3E; {
  try {
    assert.equal(&#x27;utf-8&#x27;, res.charset);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>GET json</dt>
        <dd><pre><code>request.get(&#x60;${uri}/pets&#x60;).end((error, res) =&#x3E; {
  try {
    assert.deepEqual(res.body, [&#x27;tobi&#x27;, &#x27;loki&#x27;, &#x27;jane&#x27;]);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>GET json-seq</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/json-seq&#x60;)
  .buffer()
  .end((error, res) =&#x3E; {
    try {
      assert.ifError(error);
      assert.deepEqual(res.text, &#x27;\u001E{&#x22;id&#x22;:1}\n\u001E{&#x22;id&#x22;:2}\n&#x27;);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>GET binary data</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/binary-data&#x60;)
  .buffer()
  .end((error, res) =&#x3E; {
    try {
      assert.ifError(error);
      assert.deepEqual(res.body, binData);
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>GET x-www-form-urlencoded</dt>
        <dd><pre><code>request.get(&#x60;${uri}/foo&#x60;).end((error, res) =&#x3E; {
  try {
    assert.deepEqual(res.body, { foo: &#x27;bar&#x27; });
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>GET shorthand</dt>
        <dd><pre><code>request.get(&#x60;${uri}/foo&#x60;, (error, res) =&#x3E; {
  try {
    assert.equal(&#x27;foo=bar&#x27;, res.text);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>POST shorthand</dt>
        <dd><pre><code>request.post(&#x60;${uri}/user/0/pet&#x60;, { pet: &#x27;tobi&#x27; }, (error, res) =&#x3E; {
  try {
    assert.equal(&#x27;added pet &#x22;tobi&#x22;&#x27;, res.text);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>POST shorthand without callback</dt>
        <dd><pre><code>request.post(&#x60;${uri}/user/0/pet&#x60;, { pet: &#x27;tobi&#x27; }).end((error, res) =&#x3E; {
  try {
    assert.equal(&#x27;added pet &#x22;tobi&#x22;&#x27;, res.text);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>GET querystring object with array</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/querystring&#x60;)
  .query({ val: [&#x27;a&#x27;, &#x27;b&#x27;, &#x27;c&#x27;] })
  .end((error, res) =&#x3E; {
    try {
      assert.deepEqual(res.body, { val: [&#x27;a&#x27;, &#x27;b&#x27;, &#x27;c&#x27;] });
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>GET querystring object with array and primitives</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/querystring&#x60;)
  .query({ array: [&#x27;a&#x27;, &#x27;b&#x27;, &#x27;c&#x27;], string: &#x27;foo&#x27;, number: 10 })
  .end((error, res) =&#x3E; {
    try {
      assert.deepEqual(res.body, {
        array: [&#x27;a&#x27;, &#x27;b&#x27;, &#x27;c&#x27;],
        string: &#x27;foo&#x27;,
        number: 10
      });
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>GET querystring object with two arrays</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/querystring&#x60;)
  .query({ array1: [&#x27;a&#x27;, &#x27;b&#x27;, &#x27;c&#x27;], array2: [1, 2, 3] })
  .end((error, res) =&#x3E; {
    try {
      assert.deepEqual(res.body, {
        array1: [&#x27;a&#x27;, &#x27;b&#x27;, &#x27;c&#x27;],
        array2: [1, 2, 3]
      });
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>GET querystring object</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/querystring&#x60;)
  .query({ search: &#x27;Manny&#x27; })
  .end((error, res) =&#x3E; {
    try {
      assert.deepEqual(res.body, { search: &#x27;Manny&#x27; });
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>GET querystring append original</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/querystring?search=Manny&#x60;)
  .query({ range: &#x27;1..5&#x27; })
  .end((error, res) =&#x3E; {
    try {
      assert.deepEqual(res.body, { search: &#x27;Manny&#x27;, range: &#x27;1..5&#x27; });
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>GET querystring multiple objects</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/querystring&#x60;)
  .query({ search: &#x27;Manny&#x27; })
  .query({ range: &#x27;1..5&#x27; })
  .query({ order: &#x27;desc&#x27; })
  .end((error, res) =&#x3E; {
    try {
      assert.deepEqual(res.body, {
        search: &#x27;Manny&#x27;,
        range: &#x27;1..5&#x27;,
        order: &#x27;desc&#x27;
      });
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>GET querystring with strings</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/querystring&#x60;)
  .query(&#x27;search=Manny&#x27;)
  .query(&#x27;range=1..5&#x27;)
  .query(&#x27;order=desc&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.deepEqual(res.body, {
        search: &#x27;Manny&#x27;,
        range: &#x27;1..5&#x27;,
        order: &#x27;desc&#x27;
      });
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>GET querystring with strings and objects</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/querystring&#x60;)
  .query(&#x27;search=Manny&#x27;)
  .query({ order: &#x27;desc&#x27;, range: &#x27;1..5&#x27; })
  .end((error, res) =&#x3E; {
    try {
      assert.deepEqual(res.body, {
        search: &#x27;Manny&#x27;,
        range: &#x27;1..5&#x27;,
        order: &#x27;desc&#x27;
      });
      next();
    } catch (err) {
      next(err);
    }
  });</code></pre></dd>
        <dt>GET shorthand payload goes to querystring</dt>
        <dd><pre><code>request.get(
  &#x60;${uri}/querystring&#x60;,
  { foo: &#x27;FOO&#x27;, bar: &#x27;BAR&#x27; },
  (error, res) =&#x3E; {
    try {
      assert.deepEqual(res.body, { foo: &#x27;FOO&#x27;, bar: &#x27;BAR&#x27; });
      next();
    } catch (err) {
      next(err);
    }
  }
);</code></pre></dd>
        <dt>HEAD shorthand payload goes to querystring</dt>
        <dd><pre><code>request.head(
  &#x60;${uri}/querystring-in-header&#x60;,
  { foo: &#x27;FOO&#x27;, bar: &#x27;BAR&#x27; },
  (error, res) =&#x3E; {
    try {
      assert.deepEqual(JSON.parse(res.headers.query), {
        foo: &#x27;FOO&#x27;,
        bar: &#x27;BAR&#x27;
      });
      next();
    } catch (err) {
      next(err);
    }
  }
);</code></pre></dd>
        <dt>request(method, url)</dt>
        <dd><pre><code>request(&#x27;GET&#x27;, &#x60;${uri}/foo&#x60;).end((error, res) =&#x3E; {
  try {
    assert.equal(&#x27;bar&#x27;, res.body.foo);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request(url)</dt>
        <dd><pre><code>request(&#x60;${uri}/foo&#x60;).end((error, res) =&#x3E; {
  try {
    assert.equal(&#x27;bar&#x27;, res.body.foo);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request(url, fn)</dt>
        <dd><pre><code>request(&#x60;${uri}/foo&#x60;, (error, res) =&#x3E; {
  try {
    assert.equal(&#x27;bar&#x27;, res.body.foo);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>req.timeout(ms)</dt>
        <dd><pre><code>const request_ = request.get(&#x60;${uri}/delay/3000&#x60;).timeout(1000);
request_.end((error, res) =&#x3E; {
  try {
    assert(error, &#x27;error missing&#x27;);
    assert.equal(1000, error.timeout, &#x27;err.timeout missing&#x27;);
    assert.equal(
      &#x27;Timeout of 1000ms exceeded&#x27;,
      error.message,
      &#x27;err.message incorrect&#x27;
    );
    assert.equal(null, res);
    assert(request_.timedout, true);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>req.timeout(ms) with redirect</dt>
        <dd><pre><code>const request_ = request.get(&#x60;${uri}/delay/const&#x60;).timeout(1000);
request_.end((error, res) =&#x3E; {
  try {
    assert(error, &#x27;error missing&#x27;);
    assert.equal(1000, error.timeout, &#x27;err.timeout missing&#x27;);
    assert.equal(
      &#x27;Timeout of 1000ms exceeded&#x27;,
      error.message,
      &#x27;err.message incorrect&#x27;
    );
    assert.equal(null, res);
    assert(request_.timedout, true);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>request event</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/foo&#x60;)
  .on(&#x27;request&#x27;, (request_) =&#x3E; {
    try {
      assert.equal(&#x60;${uri}/foo&#x60;, request_.url);
      next();
    } catch (err) {
      next(err);
    }
  })
  .end();</code></pre></dd>
        <dt>response event</dt>
        <dd><pre><code>request
  .get(&#x60;${uri}/foo&#x60;)
  .on(&#x27;response&#x27;, (res) =&#x3E; {
    try {
      assert.equal(&#x27;bar&#x27;, res.body.foo);
      next();
    } catch (err) {
      next(err);
    }
  })
  .end();</code></pre></dd>
        <dt>response should set statusCode</dt>
        <dd><pre><code>request.get(&#x60;${uri}/ok&#x60;, (error, res) =&#x3E; {
  try {
    assert.strictEqual(res.statusCode, 200);
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
        <dt>req.toJSON()</dt>
        <dd><pre><code>request.get(&#x60;${uri}/ok&#x60;).end((error, res) =&#x3E; {
  try {
    const index = (res.request || res.req).toJSON();
    for (const property of [&#x27;url&#x27;, &#x27;method&#x27;, &#x27;data&#x27;, &#x27;headers&#x27;]) {
      assert(index.hasOwnProperty(property));
    }
    next();
  } catch (err) {
    next(err);
  }
});</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>.retry(count)</h1>
      <dl>
        <dt>should not retry if passed &#x22;0&#x22;</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/error&#x60;)
  .retry(0)
  .end((error, res) =&#x3E; {
    try {
      assert(error, &#x27;expected an error&#x27;);
      assert.equal(
        undefined,
        error.retries,
        &#x27;expected an error without .retries&#x27;
      );
      assert.equal(500, error.status, &#x27;expected an error status of 500&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should not retry if passed an invalid number</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/error&#x60;)
  .retry(-2)
  .end((error, res) =&#x3E; {
    try {
      assert(error, &#x27;expected an error&#x27;);
      assert.equal(
        undefined,
        error.retries,
        &#x27;expected an error without .retries&#x27;
      );
      assert.equal(500, error.status, &#x27;expected an error status of 500&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should not retry if passed undefined</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/error&#x60;)
  .retry(undefined)
  .end((error, res) =&#x3E; {
    try {
      assert(error, &#x27;expected an error&#x27;);
      assert.equal(
        undefined,
        error.retries,
        &#x27;expected an error without .retries&#x27;
      );
      assert.equal(500, error.status, &#x27;expected an error status of 500&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should handle server error after repeat attempt</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/error&#x60;)
  .retry(2)
  .end((error, res) =&#x3E; {
    try {
      assert(error, &#x27;expected an error&#x27;);
      assert.equal(2, error.retries, &#x27;expected an error with .retries&#x27;);
      assert.equal(500, error.status, &#x27;expected an error status of 500&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should retry if passed nothing</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/error&#x60;)
  .retry()
  .end((error, res) =&#x3E; {
    try {
      assert(error, &#x27;expected an error&#x27;);
      assert.equal(1, error.retries, &#x27;expected an error with .retries&#x27;);
      assert.equal(500, error.status, &#x27;expected an error status of 500&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should retry if passed &#x22;true&#x22;</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/error&#x60;)
  .retry(true)
  .end((error, res) =&#x3E; {
    try {
      assert(error, &#x27;expected an error&#x27;);
      assert.equal(1, error.retries, &#x27;expected an error with .retries&#x27;);
      assert.equal(500, error.status, &#x27;expected an error status of 500&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should handle successful request after repeat attempt from server error</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/error/ok/${uniqid()}&#x60;)
  .query({ qs: &#x27;present&#x27; })
  .retry(2)
  .end((error, res) =&#x3E; {
    try {
      assert.ifError(error);
      assert(res.ok, &#x27;response should be ok&#x27;);
      assert(res.text, &#x27;res.text&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should handle server timeout error after repeat attempt</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/delay/400&#x60;)
  .timeout(200)
  .retry(2)
  .end((error, res) =&#x3E; {
    try {
      assert(error, &#x27;expected an error&#x27;);
      assert.equal(2, error.retries, &#x27;expected an error with .retries&#x27;);
      assert.equal(
        &#x27;number&#x27;,
        typeof error.timeout,
        &#x27;expected an error with .timeout&#x27;
      );
      assert.equal(&#x27;ECONNABORTED&#x27;, error.code, &#x27;expected abort error code&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should handle successful request after repeat attempt from server timeout</dt>
        <dd><pre><code>const url = &#x60;/delay/1200/ok/${uniqid()}?built=in&#x60;;
request
  .get(base + url)
  .query(&#x27;string=ified&#x27;)
  .query({ json: &#x27;ed&#x27; })
  .timeout(600)
  .retry(2)
  .end((error, res) =&#x3E; {
    try {
      assert.ifError(error);
      assert(res.ok, &#x27;response should be ok&#x27;);
      assert.equal(res.text, &#x60;ok = ${url}&#x26;string=ified&#x26;json=ed&#x60;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should handle successful request after repeat attempt from server timeout when using .then(fulfill, reject)</dt>
        <dd><pre><code>const url = &#x60;/delay/1200/ok/${uniqid()}?built=in&#x60;;
request
  .get(base + url)
  .query(&#x27;string=ified&#x27;)
  .query({ json: &#x27;ed&#x27; })
  .timeout(600)
  .retry(1)
  .then((res, error) =&#x3E; {
    try {
      assert.ifError(error);
      assert(res.ok, &#x27;response should be ok&#x27;);
      assert.equal(res.text, &#x60;ok = ${url}&#x26;string=ified&#x26;json=ed&#x60;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should correctly abort a retry attempt</dt>
        <dd><pre><code>let aborted = false;
const request_ = request.get(&#x60;${base}/delay/400&#x60;).timeout(200).retry(2);
request_.end((error, res) =&#x3E; {
  try {
    assert(false, &#x27;should not complete the request&#x27;);
  } catch (err) {
    done(err);
  }
});
request_.on(&#x27;abort&#x27;, () =&#x3E; {
  aborted = true;
});
setTimeout(() =&#x3E; {
  request_.abort();
  setTimeout(() =&#x3E; {
    try {
      assert(aborted, &#x27;should be aborted&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  }, 150);
}, 150);</code></pre></dd>
        <dt>should correctly retain header fields</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/error/ok/${uniqid()}&#x60;)
  .query({ qs: &#x27;present&#x27; })
  .retry(2)
  .set(&#x27;X-Foo&#x27;, &#x27;bar&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.ifError(error);
      assert(res.body);
      res.body.should.have.property(&#x27;x-foo&#x27;, &#x27;bar&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should not retry on 4xx responses</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/bad-request&#x60;)
  .retry(2)
  .end((error, res) =&#x3E; {
    try {
      assert(error, &#x27;expected an error&#x27;);
      assert.equal(0, error.retries, &#x27;expected an error with 0 .retries&#x27;);
      assert.equal(400, error.status, &#x27;expected an error status of 400&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should execute callback on retry if passed</dt>
        <dd><pre><code>let callbackCallCount = 0;
function retryCallback(request) {
  callbackCallCount++;
}
request
  .get(&#x60;${base}/error&#x60;)
  .retry(2, retryCallback)
  .end((error, res) =&#x3E; {
    try {
      assert(error, &#x27;expected an error&#x27;);
      assert.equal(2, error.retries, &#x27;expected an error with .retries&#x27;);
      assert.equal(500, error.status, &#x27;expected an error status of 500&#x27;);
      assert.equal(
        2,
        callbackCallCount,
        &#x27;expected the callback to be called on each retry&#x27;
      );
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>.timeout(ms)</h1>
      <dl>
        <section class="suite">
          <h1>when timeout is exceeded</h1>
          <dl>
            <dt>should error</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/delay/500&#x60;)
  .timeout(150)
  .end((error, res) =&#x3E; {
    assert(error, &#x27;expected an error&#x27;);
    assert.equal(
      &#x27;number&#x27;,
      typeof error.timeout,
      &#x27;expected an error with .timeout&#x27;
    );
    assert.equal(&#x27;ECONNABORTED&#x27;, error.code, &#x27;expected abort error code&#x27;);
    done();
  });</code></pre></dd>
            <dt>should error in promise interface </dt>
            <dd><pre><code>request
  .get(&#x60;${base}/delay/500&#x60;)
  .timeout(150)
  .catch((err) =&#x3E; {
    assert(err, &#x27;expected an error&#x27;);
    assert.equal(
      &#x27;number&#x27;,
      typeof err.timeout,
      &#x27;expected an error with .timeout&#x27;
    );
    assert.equal(&#x27;ECONNABORTED&#x27;, err.code, &#x27;expected abort error code&#x27;);
    done();
  });</code></pre></dd>
            <dt>should handle gzip timeout</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/delay/zip&#x60;)
  .timeout(150)
  .end((error, res) =&#x3E; {
    assert(error, &#x27;expected an error&#x27;);
    assert.equal(
      &#x27;number&#x27;,
      typeof error.timeout,
      &#x27;expected an error with .timeout&#x27;
    );
    assert.equal(&#x27;ECONNABORTED&#x27;, error.code, &#x27;expected abort error code&#x27;);
    done();
  });</code></pre></dd>
            <dt>should handle buffer timeout</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/delay/json&#x60;)
  .buffer(true)
  .timeout(150)
  .end((error, res) =&#x3E; {
    assert(error, &#x27;expected an error&#x27;);
    assert.equal(
      &#x27;number&#x27;,
      typeof error.timeout,
      &#x27;expected an error with .timeout&#x27;
    );
    assert.equal(&#x27;ECONNABORTED&#x27;, error.code, &#x27;expected abort error code&#x27;);
    done();
  });</code></pre></dd>
            <dt>should error on deadline</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/delay/500&#x60;)
  .timeout({ deadline: 150 })
  .end((error, res) =&#x3E; {
    assert(error, &#x27;expected an error&#x27;);
    assert.equal(
      &#x27;number&#x27;,
      typeof error.timeout,
      &#x27;expected an error with .timeout&#x27;
    );
    assert.equal(&#x27;ECONNABORTED&#x27;, error.code, &#x27;expected abort error code&#x27;);
    done();
  });</code></pre></dd>
            <dt>should support setting individual options</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/delay/500&#x60;)
  .timeout({ deadline: 10 })
  .timeout({ response: 99_999 })
  .end((error, res) =&#x3E; {
    assert(error, &#x27;expected an error&#x27;);
    assert.equal(&#x27;ECONNABORTED&#x27;, error.code, &#x27;expected abort error code&#x27;);
    assert.equal(&#x27;ETIME&#x27;, error.errno);
    done();
  });</code></pre></dd>
            <dt>should error on response</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/delay/500&#x60;)
  .timeout({ response: 150 })
  .end((error, res) =&#x3E; {
    assert(error, &#x27;expected an error&#x27;);
    assert.equal(
      &#x27;number&#x27;,
      typeof error.timeout,
      &#x27;expected an error with .timeout&#x27;
    );
    assert.equal(&#x27;ECONNABORTED&#x27;, error.code, &#x27;expected abort error code&#x27;);
    assert.equal(&#x27;ETIMEDOUT&#x27;, error.errno);
    done();
  });</code></pre></dd>
            <dt>should accept slow body with fast response</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/delay/slowbody&#x60;)
  .timeout({ response: 1000 })
  .on(&#x27;progress&#x27;, () =&#x3E; {
    // This only makes the test faster without relying on arbitrary timeouts
    request.get(&#x60;${base}/delay/slowbody/finish&#x60;).end();
  })
  .end(done);</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>request</h1>
      <dl>
        <section class="suite">
          <h1>use</h1>
          <dl>
            <dt>should use plugin success</dt>
            <dd><pre><code>const now = &#x60;${Date.now()}&#x60;;
function uuid(request_) {
  request_.set(&#x27;X-UUID&#x27;, now);
  return request_;
}
function prefix(request_) {
  request_.url = uri + request_.url;
  return request_;
}
request
  .get(&#x27;/echo&#x27;)
  .use(uuid)
  .use(prefix)
  .end((error, res) =&#x3E; {
    assert.strictEqual(res.statusCode, 200);
    assert.equal(res.get(&#x27;X-UUID&#x27;), now);
    done();
  });</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>subclass</h1>
      <dl>
        <dt>should be an instance of Request</dt>
        <dd><pre><code>const request_ = request.get(&#x27;/&#x27;);
assert(request_ instanceof request.Request);</code></pre></dd>
        <dt>should use patched subclass</dt>
        <dd><pre><code>assert(OriginalRequest);
let constructorCalled;
let sendCalled;
function NewRequest(...args) {
  constructorCalled = true;
  OriginalRequest.apply(this, args);
}
NewRequest.prototype = Object.create(OriginalRequest.prototype);
NewRequest.prototype.send = function () {
  sendCalled = true;
  return this;
};
request.Request = NewRequest;
const request_ = request.get(&#x27;/&#x27;).send();
assert(constructorCalled);
assert(sendCalled);
assert(request_ instanceof NewRequest);
assert(request_ instanceof OriginalRequest);</code></pre></dd>
        <dt>should use patched subclass in agent too</dt>
        <dd><pre><code>if (!request.agent) return; // Node-only
function NewRequest(...args) {
  OriginalRequest.apply(this, args);
}
NewRequest.prototype = Object.create(OriginalRequest.prototype);
request.Request = NewRequest;
const request_ = request.agent().del(&#x27;/&#x27;);
assert(request_ instanceof NewRequest);
assert(request_ instanceof OriginalRequest);</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>request</h1>
      <dl>
        <section class="suite">
          <h1>persistent agent</h1>
          <dl>
            <dt>should gain a session on POST</dt>
            <dd><pre><code>agent3.post(&#x60;${base}/signin&#x60;).then((res) =&#x3E; {
        res.should.have.status(200);
        should.not.exist(res.headers[&#x27;set-cookie&#x27;]);
        res.text.should.containEql(&#x27;dashboard&#x27;);
      })</code></pre></dd>
            <dt>should start with empty session (set cookies)</dt>
            <dd><pre><code>agent1.get(&#x60;${base}/dashboard&#x60;).end((error, res) =&#x3E; {
  should.exist(error);
  res.should.have.status(401);
  should.exist(res.headers[&#x27;set-cookie&#x27;]);
  done();
});</code></pre></dd>
            <dt>should gain a session (cookies already set)</dt>
            <dd><pre><code>agent1.post(&#x60;${base}/signin&#x60;).then((res) =&#x3E; {
        res.should.have.status(200);
        should.not.exist(res.headers[&#x27;set-cookie&#x27;]);
        res.text.should.containEql(&#x27;dashboard&#x27;);
      })</code></pre></dd>
            <dt>should persist cookies across requests</dt>
            <dd><pre><code>agent1.get(&#x60;${base}/dashboard&#x60;).then((res) =&#x3E; {
        res.should.have.status(200);
      })</code></pre></dd>
            <dt>should have the cookie set in the end callback</dt>
            <dd><pre><code>agent4
        .post(&#x60;${base}/setcookie&#x60;)
        .then(() =&#x3E; agent4.get(&#x60;${base}/getcookie&#x60;))
        .then((res) =&#x3E; {
          res.should.have.status(200);
          assert.strictEqual(res.text, &#x27;jar&#x27;);
        })</code></pre></dd>
            <dt>should not share cookies</dt>
            <dd><pre><code>agent2.get(&#x60;${base}/dashboard&#x60;).end((error, res) =&#x3E; {
  should.exist(error);
  res.should.have.status(401);
  done();
});</code></pre></dd>
            <dt>should not lose cookies between agents</dt>
            <dd><pre><code>agent1.get(&#x60;${base}/dashboard&#x60;).then((res) =&#x3E; {
        res.should.have.status(200);
      })</code></pre></dd>
            <dt>should be able to follow redirects</dt>
            <dd><pre><code>agent1.get(base).then((res) =&#x3E; {
        res.should.have.status(200);
        res.text.should.containEql(&#x27;dashboard&#x27;);
      })</code></pre></dd>
            <dt>should be able to post redirects</dt>
            <dd><pre><code>agent1
        .post(&#x60;${base}/redirect&#x60;)
        .send({ foo: &#x27;bar&#x27;, baz: &#x27;blaaah&#x27; })
        .then((res) =&#x3E; {
          res.should.have.status(200);
          res.text.should.containEql(&#x27;simple&#x27;);
          res.redirects.should.eql([&#x60;${base}/simple&#x60;]);
        })</code></pre></dd>
            <dt>should be able to limit redirects</dt>
            <dd><pre><code>agent1
  .get(base)
  .redirects(0)
  .end((error, res) =&#x3E; {
    should.exist(error);
    res.should.have.status(302);
    res.redirects.should.eql([]);
    res.header.location.should.equal(&#x27;/dashboard&#x27;);
    done();
  });</code></pre></dd>
            <dt>should be able to create a new session (clear cookie)</dt>
            <dd><pre><code>agent1.post(&#x60;${base}/signout&#x60;).then((res) =&#x3E; {
        res.should.have.status(200);
        should.exist(res.headers[&#x27;set-cookie&#x27;]);
      })</code></pre></dd>
            <dt>should regenerate with an empty session</dt>
            <dd><pre><code>agent1.get(&#x60;${base}/dashboard&#x60;).end((error, res) =&#x3E; {
  should.exist(error);
  res.should.have.status(401);
  should.not.exist(res.headers[&#x27;set-cookie&#x27;]);
  done();
});</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>Basic auth</h1>
      <dl>
        <section class="suite">
          <h1>when credentials are present in url</h1>
          <dl>
            <dt>should set Authorization</dt>
            <dd><pre><code>const new_url = URL.parse(base);
new_url.auth = &#x27;tobi:learnboost&#x27;;
new_url.pathname = &#x27;/basic-auth&#x27;;
request.get(URL.format(new_url)).end((error, res) =&#x3E; {
  res.status.should.equal(200);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.auth(user, pass)</h1>
          <dl>
            <dt>should set Authorization</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/basic-auth&#x60;)
  .auth(&#x27;tobi&#x27;, &#x27;learnboost&#x27;)
  .end((error, res) =&#x3E; {
    res.status.should.equal(200);
    done();
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.auth(user + &#x22;:&#x22; + pass)</h1>
          <dl>
            <dt>should set authorization</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/basic-auth/again&#x60;)
  .auth(&#x27;tobi&#x27;)
  .end((error, res) =&#x3E; {
    res.status.should.eql(200);
    done();
  });</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>[node] request</h1>
      <dl>
        <section class="suite">
          <h1>with an url</h1>
          <dl>
            <dt>should preserve the encoding of the url</dt>
            <dd><pre><code>request.get(&#x60;${base}/url?a=(b%29&#x60;).end((error, res) =&#x3E; {
  assert.equal(&#x27;/url?a=(b%29&#x27;, res.text);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>with an object</h1>
          <dl>
            <dt>should format the url</dt>
            <dd><pre><code>request.get(url.parse(&#x60;${base}/login&#x60;)).then((res) =&#x3E; {
        assert(res.ok);
      })</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>without a schema</h1>
          <dl>
            <dt>should default to http</dt>
            <dd><pre><code>request.get(&#x60;${base}/login&#x60;).then((res) =&#x3E; {
        assert.equal(res.status, 200);
      })</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>res.toJSON()</h1>
          <dl>
            <dt>should describe the response</dt>
            <dd><pre><code>request
        .post(&#x60;${base}/echo&#x60;)
        .send({ foo: &#x27;baz&#x27; })
        .then((res) =&#x3E; {
          const object = res.toJSON();
          assert.equal(&#x27;object&#x27;, typeof object.header);
          assert.equal(&#x27;object&#x27;, typeof object.req);
          assert.equal(200, object.status);
          assert.equal(&#x27;{&#x22;foo&#x22;:&#x22;baz&#x22;}&#x27;, object.text);
        })</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>res.links</h1>
          <dl>
            <dt>should default to an empty object</dt>
            <dd><pre><code>request.get(&#x60;${base}/login&#x60;).then((res) =&#x3E; {
        res.links.should.eql({});
      })</code></pre></dd>
            <dt>should parse the Link header field</dt>
            <dd><pre><code>request.get(&#x60;${base}/links&#x60;).end((error, res) =&#x3E; {
  res.links.next.should.equal(
    &#x27;https://api.github.com/repos/visionmedia/mocha/issues?page=2&#x27;
  );
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.unset(field)</h1>
          <dl>
            <dt>should remove the header field</dt>
            <dd><pre><code>request
  .post(&#x60;${base}/echo&#x60;)
  .unset(&#x27;User-Agent&#x27;)
  .end((error, res) =&#x3E; {
    assert.equal(void 0, res.header[&#x27;user-agent&#x27;]);
    done();
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>case-insensitive</h1>
          <dl>
            <dt>should set/get header fields case-insensitively</dt>
            <dd><pre><code>const r = request.post(&#x60;${base}/echo&#x60;);
r.set(&#x27;MiXeD&#x27;, &#x27;helloes&#x27;);
assert.strictEqual(r.get(&#x27;mixed&#x27;), &#x27;helloes&#x27;);</code></pre></dd>
            <dt>should unset header fields case-insensitively</dt>
            <dd><pre><code>const r = request.post(&#x60;${base}/echo&#x60;);
r.set(&#x27;MiXeD&#x27;, &#x27;helloes&#x27;);
r.unset(&#x27;MIXED&#x27;);
assert.strictEqual(r.get(&#x27;mixed&#x27;), undefined);</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.write(str)</h1>
          <dl>
            <dt>should write the given data</dt>
            <dd><pre><code>const request_ = request.post(&#x60;${base}/echo&#x60;);
request_.set(&#x27;Content-Type&#x27;, &#x27;application/json&#x27;);
assert.equal(&#x27;boolean&#x27;, typeof request_.write(&#x27;{&#x22;name&#x22;&#x27;));
assert.equal(&#x27;boolean&#x27;, typeof request_.write(&#x27;:&#x22;tobi&#x22;}&#x27;));
request_.end((error, res) =&#x3E; {
  res.text.should.equal(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;}&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>req.pipe(stream)</h1>
          <dl>
            <dt>should pipe the response to the given stream</dt>
            <dd><pre><code>const stream = new EventEmitter();
stream.buf = &#x27;&#x27;;
stream.writable = true;
stream.write = function (chunk) {
  this.buf += chunk;
};
stream.end = function () {
  this.buf.should.equal(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;}&#x27;);
  done();
};
request.post(&#x60;${base}/echo&#x60;).send(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;}&#x27;).pipe(stream);</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>.buffer()</h1>
          <dl>
            <dt>should enable buffering</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/custom&#x60;)
  .buffer()
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    assert.equal(&#x27;custom stuff&#x27;, res.text);
    assert(res.buffered);
    done();
  });</code></pre></dd>
            <dt>should take precedence over request.buffer[&#x27;someMimeType&#x27;] = false</dt>
            <dd><pre><code>const type = &#x27;application/barbaz&#x27;;
const send = &#x27;some text&#x27;;
request.buffer[type] = false;
request
  .post(&#x60;${base}/echo&#x60;)
  .type(type)
  .send(send)
  .buffer()
  .end((error, res) =&#x3E; {
    delete request.buffer[type];
    assert.ifError(error);
    assert.equal(res.type, type);
    assert.equal(send, res.text);
    assert(res.buffered);
    done();
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>.buffer(false)</h1>
          <dl>
            <dt>should disable buffering</dt>
            <dd><pre><code>request
  .post(&#x60;${base}/echo&#x60;)
  .type(&#x27;application/x-dog&#x27;)
  .send(&#x27;hello this is dog&#x27;)
  .buffer(false)
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    assert.equal(null, res.text);
    res.body.should.eql({});
    let buf = &#x27;&#x27;;
    res.setEncoding(&#x27;utf8&#x27;);
    res.on(&#x27;data&#x27;, (chunk) =&#x3E; {
      buf += chunk;
    });
    res.on(&#x27;end&#x27;, () =&#x3E; {
      buf.should.equal(&#x27;hello this is dog&#x27;);
      done();
    });
  });</code></pre></dd>
            <dt>should take precedence over request.buffer[&#x27;someMimeType&#x27;] = true</dt>
            <dd><pre><code>const type = &#x27;application/foobar&#x27;;
const send = &#x27;hello this is a dog&#x27;;
request.buffer[type] = true;
request
  .post(&#x60;${base}/echo&#x60;)
  .type(type)
  .send(send)
  .buffer(false)
  .end((error, res) =&#x3E; {
    delete request.buffer[type];
    assert.ifError(error);
    assert.equal(null, res.text);
    assert.equal(res.type, type);
    assert(!res.buffered);
    res.body.should.eql({});
    let buf = &#x27;&#x27;;
    res.setEncoding(&#x27;utf8&#x27;);
    res.on(&#x27;data&#x27;, (chunk) =&#x3E; {
      buf += chunk;
    });
    res.on(&#x27;end&#x27;, () =&#x3E; {
      buf.should.equal(send);
      done();
    });
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>.withCredentials()</h1>
          <dl>
            <dt>should not throw an error when using the client-side &#x22;withCredentials&#x22; method</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/custom&#x60;)
  .withCredentials()
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    done();
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>.agent()</h1>
          <dl>
            <dt>should return the defaut agent</dt>
            <dd><pre><code>const request_ = request.post(&#x60;${base}/echo&#x60;);
request_.agent().should.equal(false);
done();</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>.agent(undefined)</h1>
          <dl>
            <dt>should set an agent to undefined and ensure it is chainable</dt>
            <dd><pre><code>const request_ = request.get(&#x60;${base}/echo&#x60;);
const returnValue = request_.agent(undefined);
returnValue.should.equal(request_);
assert.strictEqual(request_.agent(), undefined);
done();</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>.agent(new http.Agent())</h1>
          <dl>
            <dt>should set passed agent</dt>
            <dd><pre><code>const http = require(&#x27;http&#x27;);
const request_ = request.get(&#x60;${base}/echo&#x60;);
const agent = new http.Agent();
const returnValue = request_.agent(agent);
returnValue.should.equal(request_);
request_.agent().should.equal(agent);
done();</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>with a content type other than application/json or text/*</h1>
          <dl>
            <dt>should still use buffering</dt>
            <dd><pre><code>return request
  .post(&#x60;${base}/echo&#x60;)
  .type(&#x27;application/x-dog&#x27;)
  .send(&#x27;hello this is dog&#x27;)
  .then((res) =&#x3E; {
    assert.equal(null, res.text);
    assert.equal(res.body.toString(), &#x27;hello this is dog&#x27;);
    res.buffered.should.be.true;
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>content-length</h1>
          <dl>
            <dt>should be set to the byte length of a non-buffer object</dt>
            <dd><pre><code>const decoder = new StringDecoder(&#x27;utf8&#x27;);
let img = fs.readFileSync(&#x60;${__dirname}/fixtures/test.png&#x60;);
img = decoder.write(img);
request
  .post(&#x60;${base}/echo&#x60;)
  .type(&#x27;application/x-image&#x27;)
  .send(img)
  .buffer(false)
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    assert(!res.buffered);
    assert.equal(res.header[&#x27;content-length&#x27;], Buffer.byteLength(img));
    done();
  });</code></pre></dd>
            <dt>should be set to the length of a buffer object</dt>
            <dd><pre><code>const img = fs.readFileSync(&#x60;${__dirname}/fixtures/test.png&#x60;);
request
  .post(&#x60;${base}/echo&#x60;)
  .type(&#x27;application/x-image&#x27;)
  .send(img)
  .buffer(true)
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    assert(res.buffered);
    assert.equal(res.header[&#x27;content-length&#x27;], img.length);
    done();
  });</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>req.buffer[&#x27;someMimeType&#x27;]</h1>
      <dl>
        <dt>should respect that agent.buffer(true) takes precedent</dt>
        <dd><pre><code>const agent = request.agent();
agent.buffer(true);
const type = &#x27;application/somerandomtype&#x27;;
const send = &#x27;somerandomtext&#x27;;
request.buffer[type] = false;
agent
  .post(&#x60;${base}/echo&#x60;)
  .type(type)
  .send(send)
  .end((error, res) =&#x3E; {
    delete request.buffer[type];
    assert.ifError(error);
    assert.equal(res.type, type);
    assert.equal(send, res.text);
    assert(res.buffered);
    done();
  });</code></pre></dd>
        <dt>should respect that agent.buffer(false) takes precedent</dt>
        <dd><pre><code>const agent = request.agent();
agent.buffer(false);
const type = &#x27;application/barrr&#x27;;
const send = &#x27;some random text2&#x27;;
request.buffer[type] = true;
agent
  .post(&#x60;${base}/echo&#x60;)
  .type(type)
  .send(send)
  .end((error, res) =&#x3E; {
    delete request.buffer[type];
    assert.ifError(error);
    assert.equal(null, res.text);
    assert.equal(res.type, type);
    assert(!res.buffered);
    res.body.should.eql({});
    let buf = &#x27;&#x27;;
    res.setEncoding(&#x27;utf8&#x27;);
    res.on(&#x27;data&#x27;, (chunk) =&#x3E; {
      buf += chunk;
    });
    res.on(&#x27;end&#x27;, () =&#x3E; {
      buf.should.equal(send);
      done();
    });
  });</code></pre></dd>
        <dt>should disable buffering for that mimetype when false</dt>
        <dd><pre><code>const type = &#x27;application/bar&#x27;;
const send = &#x27;some random text&#x27;;
request.buffer[type] = false;
request
  .post(&#x60;${base}/echo&#x60;)
  .type(type)
  .send(send)
  .end((error, res) =&#x3E; {
    delete request.buffer[type];
    assert.ifError(error);
    assert.equal(null, res.text);
    assert.equal(res.type, type);
    assert(!res.buffered);
    res.body.should.eql({});
    let buf = &#x27;&#x27;;
    res.setEncoding(&#x27;utf8&#x27;);
    res.on(&#x27;data&#x27;, (chunk) =&#x3E; {
      buf += chunk;
    });
    res.on(&#x27;end&#x27;, () =&#x3E; {
      buf.should.equal(send);
      done();
    });
  });</code></pre></dd>
        <dt>should enable buffering for that mimetype when true</dt>
        <dd><pre><code>const type = &#x27;application/baz&#x27;;
const send = &#x27;woooo&#x27;;
request.buffer[type] = true;
request
  .post(&#x60;${base}/echo&#x60;)
  .type(type)
  .send(send)
  .end((error, res) =&#x3E; {
    delete request.buffer[type];
    assert.ifError(error);
    assert.equal(res.type, type);
    assert.equal(send, res.text);
    assert(res.buffered);
    done();
  });</code></pre></dd>
        <dt>should fallback to default handling for that mimetype when undefined</dt>
        <dd><pre><code>const type = &#x27;application/bazzz&#x27;;
const send = &#x27;woooooo&#x27;;
return request
  .post(&#x60;${base}/echo&#x60;)
  .type(type)
  .send(send)
  .then((res) =&#x3E; {
    assert.equal(res.type, type);
    assert.equal(send, res.body.toString());
    assert(res.buffered);
  });</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>exports</h1>
      <dl>
        <dt>should expose .protocols</dt>
        <dd><pre><code>Object.keys(request.protocols).should.eql([&#x27;http:&#x27;, &#x27;https:&#x27;, &#x27;http2:&#x27;]);</code></pre></dd>
        <dt>should expose .serialize</dt>
        <dd><pre><code>Object.keys(request.serialize).should.eql([
  &#x27;application/x-www-form-urlencoded&#x27;,
  &#x27;application/json&#x27;
]);</code></pre></dd>
        <dt>should expose .parse</dt>
        <dd><pre><code>Object.keys(request.parse).should.eql([
  &#x27;application/x-www-form-urlencoded&#x27;,
  &#x27;application/json&#x27;,
  &#x27;text&#x27;,
  &#x27;application/json-seq&#x27;,
  &#x27;application/octet-stream&#x27;,
  &#x27;application/pdf&#x27;,
  &#x27;image&#x27;
]);</code></pre></dd>
        <dt>should export .buffer</dt>
        <dd><pre><code>Object.keys(request.buffer).should.eql([]);</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>flags</h1>
      <dl>
        <section class="suite">
          <h1>with 4xx response</h1>
          <dl>
            <dt>should set res.error and res.clientError</dt>
            <dd><pre><code>request.get(&#x60;${base}/notfound&#x60;).end((error, res) =&#x3E; {
  assert(error);
  assert(!res.ok, &#x27;response should not be ok&#x27;);
  assert(res.error, &#x27;response should be an error&#x27;);
  assert(res.clientError, &#x27;response should be a client error&#x27;);
  assert(!res.serverError, &#x27;response should not be a server error&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>with 5xx response</h1>
          <dl>
            <dt>should set res.error and res.serverError</dt>
            <dd><pre><code>request.get(&#x60;${base}/error&#x60;).end((error, res) =&#x3E; {
  assert(error);
  assert(!res.ok, &#x27;response should not be ok&#x27;);
  assert(!res.notFound, &#x27;response should not be notFound&#x27;);
  assert(res.error, &#x27;response should be an error&#x27;);
  assert(!res.clientError, &#x27;response should not be a client error&#x27;);
  assert(res.serverError, &#x27;response should be a server error&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>with 404 Not Found</h1>
          <dl>
            <dt>should res.notFound</dt>
            <dd><pre><code>request.get(&#x60;${base}/notfound&#x60;).end((error, res) =&#x3E; {
  assert(error);
  assert(res.notFound, &#x27;response should be .notFound&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>with 400 Bad Request</h1>
          <dl>
            <dt>should set req.badRequest</dt>
            <dd><pre><code>request.get(&#x60;${base}/bad-request&#x60;).end((error, res) =&#x3E; {
  assert(error);
  assert(res.badRequest, &#x27;response should be .badRequest&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>with 401 Bad Request</h1>
          <dl>
            <dt>should set res.unauthorized</dt>
            <dd><pre><code>request.get(&#x60;${base}/unauthorized&#x60;).end((error, res) =&#x3E; {
  assert(error);
  assert(res.unauthorized, &#x27;response should be .unauthorized&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>with 406 Not Acceptable</h1>
          <dl>
            <dt>should set res.notAcceptable</dt>
            <dd><pre><code>request.get(&#x60;${base}/not-acceptable&#x60;).end((error, res) =&#x3E; {
  assert(error);
  assert(res.notAcceptable, &#x27;response should be .notAcceptable&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>with 204 No Content</h1>
          <dl>
            <dt>should set res.noContent</dt>
            <dd><pre><code>request.get(&#x60;${base}/no-content&#x60;).end((error, res) =&#x3E; {
  assert(!error);
  assert(res.noContent, &#x27;response should be .noContent&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>with 201 Created</h1>
          <dl>
            <dt>should set res.created</dt>
            <dd><pre><code>request.post(&#x60;${base}/created&#x60;).end((error, res) =&#x3E; {
  assert(!error);
  assert(res.created, &#x27;response should be .created&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>with 422 Unprocessable Entity</h1>
          <dl>
            <dt>should set res.unprocessableEntity</dt>
            <dd><pre><code>request.post(&#x60;${base}/unprocessable-entity&#x60;).end((error, res) =&#x3E; {
  assert(error);
  assert(
    res.unprocessableEntity,
    &#x27;response should be .unprocessableEntity&#x27;
  );
  done();
});</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>Merging objects</h1>
      <dl>
        <dt>Don&#x27;t mix Buffer and JSON</dt>
        <dd><pre><code>assert.throws(() =&#x3E; {
  request
    .post(&#x27;/echo&#x27;)
    .send(Buffer.from(&#x27;some buffer&#x27;))
    .send({ allowed: false });
});</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>req.send(String)</h1>
      <dl>
        <dt>should default to &#x22;form&#x22;</dt>
        <dd><pre><code>request
  .post(&#x60;${base}/echo&#x60;)
  .send(&#x27;user[name]=tj&#x27;)
  .send(&#x27;user[email]=tj@vision-media.ca&#x27;)
  .end((error, res) =&#x3E; {
    res.header[&#x27;content-type&#x27;].should.equal(
      &#x27;application/x-www-form-urlencoded&#x27;
    );
    res.body.should.eql({
      user: { name: &#x27;tj&#x27;, email: &#x27;tj@vision-media.ca&#x27; }
    });
    done();
  });</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>res.body</h1>
      <dl>
        <section class="suite">
          <h1>application/x-www-form-urlencoded</h1>
          <dl>
            <dt>should parse the body</dt>
            <dd><pre><code>request.get(&#x60;${base}/form-data&#x60;).end((error, res) =&#x3E; {
  res.text.should.equal(&#x27;pet[name]=manny&#x27;);
  res.body.should.eql({ pet: { name: &#x27;manny&#x27; } });
  done();
});</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>request.get().http2()</h1>
      <dl>
        <dt>should preserve the encoding of the url</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/url?a=(b%29&#x60;)
  .http2()
  .end((error, res) =&#x3E; {
    assert.equal(&#x27;/url?a=(b%29&#x27;, res.text);
    done();
  });</code></pre></dd>
        <dt>should format the url</dt>
        <dd><pre><code>request
      .get(url.parse(&#x60;${base}/login&#x60;))
      .http2()
      .then((res) =&#x3E; {
        assert(res.ok);
      })</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>https</h1>
      <dl>
        <section class="suite">
          <h1>certificate authority</h1>
          <dl>
            <section class="suite">
              <h1>request</h1>
              <dl>
                <dt>should give a good response</dt>
                <dd><pre><code>request
  .get(testEndpoint)
  .ca(ca)
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    assert(res.ok);
    assert.strictEqual(&#x27;Safe and secure!&#x27;, res.text);
    done();
  });</code></pre></dd>
                <dt>should reject unauthorized response</dt>
                <dd><pre><code>return request
  .get(testEndpoint)
  .trustLocalhost(false)
  .then(
    () =&#x3E; {
      throw new Error(&#x27;Allows MITM&#x27;);
    },
    () =&#x3E; {}
  );</code></pre></dd>
                <dt>should not reject unauthorized response</dt>
                <dd><pre><code>return request
  .get(testEndpoint)
  .disableTLSCerts()
  .then(({ status }) =&#x3E; {
    assert.strictEqual(status, 200);
  });</code></pre></dd>
                <dt>should trust localhost unauthorized response</dt>
                <dd><pre><code>return request.get(testEndpoint).trustLocalhost(true);</code></pre></dd>
                <dt>should trust overriden localhost unauthorized response</dt>
                <dd><pre><code>return request
  .get(&#x60;https://example.com:${server.address().port}&#x60;)
  .connect(&#x27;127.0.0.1&#x27;)
  .trustLocalhost();</code></pre></dd>
              </dl>
            </section>
            <section class="suite">
              <h1>.agent</h1>
              <dl>
                <dt>should be able to make multiple requests without redefining the certificate</dt>
                <dd><pre><code>const agent = request.agent({ ca });
agent.get(testEndpoint).end((error, res) =&#x3E; {
  assert.ifError(error);
  assert(res.ok);
  assert.strictEqual(&#x27;Safe and secure!&#x27;, res.text);
  agent.get(url.parse(testEndpoint)).end((error, res) =&#x3E; {
    assert.ifError(error);
    assert(res.ok);
    assert.strictEqual(&#x27;Safe and secure!&#x27;, res.text);
    done();
  });
});</code></pre></dd>
              </dl>
            </section>
          </dl>
        </section>
        <section class="suite">
          <h1>client certificates</h1>
          <dl>
            <section class="suite">
              <h1>request</h1>
              <dl>
              </dl>
            </section>
            <section class="suite">
              <h1>.agent</h1>
              <dl>
              </dl>
            </section>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>res.body</h1>
      <dl>
        <section class="suite">
          <h1>image/png</h1>
          <dl>
            <dt>should parse the body</dt>
            <dd><pre><code>request.get(&#x60;${base}/image&#x60;).end((error, res) =&#x3E; {
  res.type.should.equal(&#x27;image/png&#x27;);
  Buffer.isBuffer(res.body).should.be.true();
  (res.body.length - img.length).should.equal(0);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>application/octet-stream</h1>
          <dl>
            <dt>should parse the body</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/image-as-octets&#x60;)
  .buffer(true) // that&#x27;s tech debt :(
  .end((error, res) =&#x3E; {
    res.type.should.equal(&#x27;application/octet-stream&#x27;);
    Buffer.isBuffer(res.body).should.be.true();
    (res.body.length - img.length).should.equal(0);
    done();
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>application/octet-stream</h1>
          <dl>
            <dt>should parse the body (using responseType)</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/image-as-octets&#x60;)
  .responseType(&#x27;blob&#x27;)
  .end((error, res) =&#x3E; {
    res.type.should.equal(&#x27;application/octet-stream&#x27;);
    Buffer.isBuffer(res.body).should.be.true();
    (res.body.length - img.length).should.equal(0);
    done();
  });</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>zlib</h1>
      <dl>
        <dt>should deflate the content</dt>
        <dd><pre><code>request.get(base).end((error, res) =&#x3E; {
  res.should.have.status(200);
  res.text.should.equal(subject);
  res.headers[&#x27;content-length&#x27;].should.be.below(subject.length);
  done();
});</code></pre></dd>
        <dt>should protect from zip bombs</dt>
        <dd><pre><code>request
  .get(base)
  .buffer(true)
  .maxResponseSize(1)
  .end((error, res) =&#x3E; {
    try {
      assert.equal(&#x27;Maximum response size reached&#x27;, error &#x26;&#x26; error.message);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
        <dt>should ignore trailing junk</dt>
        <dd><pre><code>request.get(&#x60;${base}/junk&#x60;).end((error, res) =&#x3E; {
  res.should.have.status(200);
  res.text.should.equal(subject);
  done();
});</code></pre></dd>
        <dt>should ignore missing data</dt>
        <dd><pre><code>request.get(&#x60;${base}/chopped&#x60;).end((error, res) =&#x3E; {
  assert.equal(undefined, error);
  res.should.have.status(200);
  res.text.should.startWith(subject);
  done();
});</code></pre></dd>
        <dt>should handle corrupted responses</dt>
        <dd><pre><code>request.get(&#x60;${base}/corrupt&#x60;).end((error, res) =&#x3E; {
  assert(error, &#x27;missing error&#x27;);
  assert(!res, &#x27;response should not be defined&#x27;);
  done();
});</code></pre></dd>
        <dt>should handle no content with gzip header</dt>
        <dd><pre><code>request.get(&#x60;${base}/nocontent&#x60;).end((error, res) =&#x3E; {
  assert.ifError(error);
  assert(res);
  res.should.have.status(204);
  res.text.should.equal(&#x27;&#x27;);
  res.headers.should.not.have.property(&#x27;content-length&#x27;);
  done();
});</code></pre></dd>
        <section class="suite">
          <h1>without encoding set</h1>
          <dl>
            <dt>should buffer if asked</dt>
            <dd><pre><code>return request
  .get(&#x60;${base}/binary&#x60;)
  .buffer(true)
  .then((res) =&#x3E; {
    res.should.have.status(200);
    assert(res.headers[&#x27;content-length&#x27;]);
    assert(res.body.byteLength);
    assert.equal(subject, res.body.toString());
  });</code></pre></dd>
            <dt>should emit buffers</dt>
            <dd><pre><code>request.get(&#x60;${base}/binary&#x60;).end((error, res) =&#x3E; {
  res.should.have.status(200);
  res.headers[&#x27;content-length&#x27;].should.be.below(subject.length);
  res.on(&#x27;data&#x27;, (chunk) =&#x3E; {
    chunk.should.have.length(subject.length);
  });
  res.on(&#x27;end&#x27;, done);
});</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>req.lookup()</h1>
      <dl>
        <dt>should set a custom lookup</dt>
        <dd><pre><code>const r = request.get(&#x60;${base}/ok&#x60;).lookup(myLookup);
assert(r.lookup() === myLookup);
r.then((res) =&#x3E; {
  res.text.should.equal(&#x27;ok&#x27;);
  done();
});</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>Multipart</h1>
      <dl>
        <section class="suite">
          <h1>#field(name, value)</h1>
          <dl>
            <dt>should set a multipart field value</dt>
            <dd><pre><code>const request_ = request.post(&#x60;${base}/echo&#x60;);
request_.field(&#x27;user[name]&#x27;, &#x27;tobi&#x27;);
request_.field(&#x27;user[age]&#x27;, &#x27;2&#x27;);
request_.field(&#x27;user[species]&#x27;, &#x27;ferret&#x27;);
return request_.then((res) =&#x3E; {
  res.body[&#x27;user[name]&#x27;].should.equal(&#x27;tobi&#x27;);
  res.body[&#x27;user[age]&#x27;].should.equal(&#x27;2&#x27;);
  res.body[&#x27;user[species]&#x27;].should.equal(&#x27;ferret&#x27;);
});</code></pre></dd>
            <dt>should work with file attachments</dt>
            <dd><pre><code>const request_ = request.post(&#x60;${base}/echo&#x60;);
request_.field(&#x27;name&#x27;, &#x27;Tobi&#x27;);
request_.attach(&#x27;document&#x27;, &#x27;test/node/fixtures/user.html&#x27;);
request_.field(&#x27;species&#x27;, &#x27;ferret&#x27;);
return request_.then((res) =&#x3E; {
  res.body.name.should.equal(&#x27;Tobi&#x27;);
  res.body.species.should.equal(&#x27;ferret&#x27;);
  const html = res.files.document;
  html.originalFilename.should.equal(&#x27;user.html&#x27;);
  html.mimetype.should.equal(&#x27;text/html&#x27;);
  read(html.filepath).should.equal(&#x27;&#x3C;h1&#x3E;name&#x3C;/h1&#x3E;&#x27;);
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>#attach(name, path)</h1>
          <dl>
            <dt>should attach a file</dt>
            <dd><pre><code>const request_ = request.post(&#x60;${base}/echo&#x60;);
request_.attach(&#x27;one&#x27;, &#x27;test/node/fixtures/user.html&#x27;);
request_.attach(&#x27;two&#x27;, &#x27;test/node/fixtures/user.json&#x27;);
request_.attach(&#x27;three&#x27;, &#x27;test/node/fixtures/user.txt&#x27;);
return request_.then((res) =&#x3E; {
  const html = res.files.one;
  const json = res.files.two;
  const text = res.files.three;
  html.originalFilename.should.equal(&#x27;user.html&#x27;);
  html.mimetype.should.equal(&#x27;text/html&#x27;);
  read(html.filepath).should.equal(&#x27;&#x3C;h1&#x3E;name&#x3C;/h1&#x3E;&#x27;);
  json.originalFilename.should.equal(&#x27;user.json&#x27;);
  json.mimetype.should.equal(&#x27;application/json&#x27;);
  read(json.filepath).should.equal(&#x27;{&#x22;name&#x22;:&#x22;tobi&#x22;}&#x27;);
  text.originalFilename.should.equal(&#x27;user.txt&#x27;);
  text.mimetype.should.equal(&#x27;text/plain&#x27;);
  read(text.filepath).should.equal(&#x27;Tobi&#x27;);
});</code></pre></dd>
            <section class="suite">
              <h1>when a file does not exist</h1>
              <dl>
                <dt>should fail the request with an error</dt>
                <dd><pre><code>const request_ = request.post(&#x60;${base}/echo&#x60;);
request_.attach(&#x27;name&#x27;, &#x27;foo&#x27;);
// request_.attach(&#x27;name2&#x27;, &#x27;bar&#x27;);
// request_.attach(&#x27;name3&#x27;, &#x27;baz&#x27;);
request_.end((error, res) =&#x3E; {
  assert.ok(Boolean(error), &#x27;Request should have failed.&#x27;);
  error.code.should.equal(&#x27;ENOENT&#x27;);
  error.message.should.containEql(&#x27;ENOENT&#x27;);
  if (IS_WINDOWS) {
    error.path.toLowerCase().should.equal(
      getFullPath(&#x27;foo&#x27;).toLowerCase()
    );
  } else {
    error.path.should.equal(getFullPath(&#x27;foo&#x27;));
  }
  done();
});</code></pre></dd>
                <dt>promise should fail</dt>
                <dd><pre><code>return request
  .post(&#x60;${base}/echo&#x60;)
  .field({ a: 1, b: 2 })
  .attach(&#x27;c&#x27;, &#x27;does-not-exist.txt&#x27;)
  .then(
    (res) =&#x3E; assert.fail(&#x27;It should not allow this&#x27;),
    (err) =&#x3E; {
      err.code.should.equal(&#x27;ENOENT&#x27;);
      if (IS_WINDOWS) {
        err.path.toLowerCase().should.equal(
          getFullPath(&#x27;does-not-exist.txt&#x27;).toLowerCase()
        );
      } else {
        err.path.should.equal(getFullPath(&#x27;does-not-exist.txt&#x27;));
      }
    }
  );</code></pre></dd>
                <dt>should report ENOENT via the callback</dt>
                <dd><pre><code>request
  .post(&#x60;${base}/echo&#x60;)
  .attach(&#x27;name&#x27;, &#x27;file-does-not-exist&#x27;)
  .end((error, res) =&#x3E; {
    assert.ok(Boolean(error), &#x27;Request should have failed&#x27;);
    error.code.should.equal(&#x27;ENOENT&#x27;);
    done();
  });</code></pre></dd>
                <dt>should report ENOENT via Promise</dt>
                <dd><pre><code>return request
  .post(&#x60;${base}/echo&#x60;)
  .attach(&#x27;name&#x27;, &#x27;file-does-not-exist&#x27;)
  .then(
    (res) =&#x3E; assert.fail(&#x27;Request should have failed&#x27;),
    (err) =&#x3E; err.code.should.equal(&#x27;ENOENT&#x27;)
  );</code></pre></dd>
              </dl>
            </section>
          </dl>
        </section>
        <section class="suite">
          <h1>#attach(name, path, filename)</h1>
          <dl>
            <dt>should use the custom filename</dt>
            <dd><pre><code>request
        .post(&#x60;${base}/echo&#x60;)
        .attach(&#x27;document&#x27;, &#x27;test/node/fixtures/user.html&#x27;, &#x27;doc.html&#x27;)
        .then((res) =&#x3E; {
          const html = res.files.document;
          html.originalFilename.should.equal(&#x27;doc.html&#x27;);
          html.mimetype.should.equal(&#x27;text/html&#x27;);
          read(html.filepath).should.equal(&#x27;&#x3C;h1&#x3E;name&#x3C;/h1&#x3E;&#x27;);
        })</code></pre></dd>
            <dt>should fire progress event</dt>
            <dd><pre><code>let loaded = 0;
let total = 0;
let uploadEventWasFired = false;
request
  .post(&#x60;${base}/echo&#x60;)
  .attach(&#x27;document&#x27;, &#x27;test/node/fixtures/user.html&#x27;)
  .on(&#x27;progress&#x27;, (event) =&#x3E; {
    total = event.total;
    loaded = event.loaded;
    if (event.direction === &#x27;upload&#x27;) {
      uploadEventWasFired = true;
    }
  })
  .end((error, res) =&#x3E; {
    if (error) return done(error);
    const html = res.files.document;
    html.originalFilename.should.equal(&#x27;user.html&#x27;);
    html.mimetype.should.equal(&#x27;text/html&#x27;);
    read(html.filepath).should.equal(&#x27;&#x3C;h1&#x3E;name&#x3C;/h1&#x3E;&#x27;);
    total.should.equal(223);
    loaded.should.equal(223);
    uploadEventWasFired.should.equal(true);
    done();
  });</code></pre></dd>
            <dt>filesystem errors should be caught</dt>
            <dd><pre><code>request
  .post(&#x60;${base}/echo&#x60;)
  .attach(&#x27;filedata&#x27;, &#x27;test/node/fixtures/non-existent-file.ext&#x27;)
  .end((error, res) =&#x3E; {
    assert.ok(Boolean(error), &#x27;Request should have failed.&#x27;);
    error.code.should.equal(&#x27;ENOENT&#x27;);
    if (IS_WINDOWS) {
      error.path.toLowerCase().should.equal(
        getFullPath(&#x27;test/node/fixtures/non-existent-file.ext&#x27;).toLowerCase()
      );
    } else {
      error.path.should.equal(
        getFullPath(&#x27;test/node/fixtures/non-existent-file.ext&#x27;)
      );
    }
    done();
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>#field(name, val)</h1>
          <dl>
            <dt>should set a multipart field value</dt>
            <dd><pre><code>request
  .post(&#x60;${base}/echo&#x60;)
  .field(&#x27;first-name&#x27;, &#x27;foo&#x27;)
  .field(&#x27;last-name&#x27;, &#x27;bar&#x27;)
  .end((error, res) =&#x3E; {
    if (error) done(error);
    res.should.be.ok();
    res.body[&#x27;first-name&#x27;].should.equal(&#x27;foo&#x27;);
    res.body[&#x27;last-name&#x27;].should.equal(&#x27;bar&#x27;);
    done();
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>#field(object)</h1>
          <dl>
            <dt>should set multiple multipart fields</dt>
            <dd><pre><code>request
  .post(&#x60;${base}/echo&#x60;)
  .field({ &#x27;first-name&#x27;: &#x27;foo&#x27;, &#x27;last-name&#x27;: &#x27;bar&#x27; })
  .end((error, res) =&#x3E; {
    if (error) done(error);
    res.should.be.ok();
    res.body[&#x27;first-name&#x27;].should.equal(&#x27;foo&#x27;);
    res.body[&#x27;last-name&#x27;].should.equal(&#x27;bar&#x27;);
    done();
  });</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>with network error</h1>
      <dl>
        <dt>should error</dt>
        <dd><pre><code>request.get(&#x60;http://localhost:${this.port}/&#x60;).end((error, res) =&#x3E; {
  assert(error, &#x27;expected an error&#x27;);
  done();
});</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>request</h1>
      <dl>
        <section class="suite">
          <h1>not modified</h1>
          <dl>
            <dt>should start with 200</dt>
            <dd><pre><code>request.get(&#x60;${base}/if-mod&#x60;).end((error, res) =&#x3E; {
  res.should.have.status(200);
  res.text.should.match(/^\d+$/);
  ts = Number(res.text);
  done();
});</code></pre></dd>
            <dt>should then be 304</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/if-mod&#x60;)
  .set(&#x27;If-Modified-Since&#x27;, new Date(ts).toUTCString())
  .end((error, res) =&#x3E; {
    res.should.have.status(304);
    // res.text.should.be.empty
    done();
  });</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>req.parse(fn)</h1>
      <dl>
        <dt>should take precedence over default parsers</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/manny&#x60;)
  .parse(request.parse[&#x27;application/json&#x27;])
  .end((error, res) =&#x3E; {
    assert(res.ok);
    assert.equal(&#x27;{&#x22;name&#x22;:&#x22;manny&#x22;}&#x27;, res.text);
    assert.equal(&#x27;manny&#x27;, res.body.name);
    done();
  });</code></pre></dd>
        <dt>should be the only parser</dt>
        <dd><pre><code>request
      .get(&#x60;${base}/image&#x60;)
      .buffer(false)
      .parse((res, fn) =&#x3E; {
        res.on(&#x27;data&#x27;, () =&#x3E; {});
      })
      .then((res) =&#x3E; {
        assert(res.ok);
        assert.strictEqual(res.text, undefined);
        res.body.should.eql({});
      })</code></pre></dd>
        <dt>should emit error if parser throws</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/manny&#x60;)
  .parse(() =&#x3E; {
    throw new Error(&#x27;I am broken&#x27;);
  })
  .on(&#x27;error&#x27;, (error) =&#x3E; {
    error.message.should.equal(&#x27;I am broken&#x27;);
    done();
  })
  .end();</code></pre></dd>
        <dt>should emit error if parser returns an error</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/manny&#x60;)
  .parse((res, fn) =&#x3E; {
    fn(new Error(&#x27;I am broken&#x27;));
  })
  .on(&#x27;error&#x27;, (error) =&#x3E; {
    error.message.should.equal(&#x27;I am broken&#x27;);
    done();
  })
  .end();</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>pipe on redirect</h1>
      <dl>
        <dt>should follow Location</dt>
        <dd><pre><code>const stream = fs.createWriteStream(destinationPath);
const redirects = [];
const request_ = request
  .get(base)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    redirects.push(res.headers.location);
  })
  .connect({
    inapplicable: &#x27;should be ignored&#x27;
  });
stream.on(&#x27;finish&#x27;, () =&#x3E; {
  redirects.should.eql([&#x27;/movies&#x27;, &#x27;/movies/all&#x27;, &#x27;/movies/all/0&#x27;]);
  fs.readFileSync(destinationPath, &#x27;utf8&#x27;).should.eql(&#x27;first movie page&#x27;);
  done();
});
request_.pipe(stream);</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>request pipe</h1>
      <dl>
        <dt>should act as a writable stream</dt>
        <dd><pre><code>const request_ = request.post(base);
const stream = fs.createReadStream(&#x27;test/node/fixtures/user.json&#x27;);
request_.type(&#x27;json&#x27;);
request_.on(&#x27;response&#x27;, (res) =&#x3E; {
  res.body.should.eql({ name: &#x27;tobi&#x27; });
  done();
});
stream.pipe(request_);</code></pre></dd>
        <dt>end() stops piping</dt>
        <dd><pre><code>const stream = fs.createWriteStream(destinationPath);
request.get(base).end((error, res) =&#x3E; {
  try {
    res.pipe(stream);
    return done(new Error(&#x27;Did not prevent nonsense pipe&#x27;));
  } catch {
    /* expected error */
  }
  done();
});</code></pre></dd>
        <dt>should act as a readable stream</dt>
        <dd><pre><code>const stream = fs.createWriteStream(destinationPath);
let responseCalled = false;
const request_ = request.get(base);
request_.type(&#x27;json&#x27;);
request_.on(&#x27;response&#x27;, (res) =&#x3E; {
  res.status.should.eql(200);
  responseCalled = true;
});
stream.on(&#x27;finish&#x27;, () =&#x3E; {
  JSON.parse(fs.readFileSync(destinationPath)).should.eql({
    name: &#x27;tobi&#x27;
  });
  responseCalled.should.be.true();
  done();
});
request_.pipe(stream);</code></pre></dd>
        <dt>should follow redirects</dt>
        <dd><pre><code>const stream = fs.createWriteStream(destinationPath);
let responseCalled = false;
const request_ = request.get(base + &#x27;/redirect&#x27;);
request_.type(&#x27;json&#x27;);
request_.on(&#x27;response&#x27;, (res) =&#x3E; {
  res.status.should.eql(200);
  responseCalled = true;
});
stream.on(&#x27;finish&#x27;, () =&#x3E; {
  JSON.parse(fs.readFileSync(destinationPath)).should.eql({
    name: &#x27;tobi&#x27;
  });
  responseCalled.should.be.true();
  done();
});
request_.pipe(stream);</code></pre></dd>
        <dt>should not throw on bad redirects</dt>
        <dd><pre><code>const stream = fs.createWriteStream(destinationPath);
let responseCalled = false;
let errorCalled = false;
const request_ = request.get(base + &#x27;/badRedirectNoLocation&#x27;);
request_.type(&#x27;json&#x27;);
request_.on(&#x27;response&#x27;, (res) =&#x3E; {
  responseCalled = true;
});
request_.on(&#x27;error&#x27;, (error) =&#x3E; {
  error.message.should.eql(&#x27;No location header for redirect&#x27;);
  errorCalled = true;
  stream.end();
});
stream.on(&#x27;finish&#x27;, () =&#x3E; {
  responseCalled.should.be.false();
  errorCalled.should.be.true();
  done();
});
request_.pipe(stream);</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>req.query(String)</h1>
      <dl>
        <dt>should support passing in a string</dt>
        <dd><pre><code>request
  .del(base)
  .query(&#x27;name=t%F6bi&#x27;)
  .end((error, res) =&#x3E; {
    res.body.should.eql({ name: &#x27;t%F6bi&#x27; });
    done();
  });</code></pre></dd>
        <dt>should work with url query-string and string for query</dt>
        <dd><pre><code>request
  .del(&#x60;${base}/?name=tobi&#x60;)
  .query(&#x27;age=2%20&#x27;)
  .end((error, res) =&#x3E; {
    res.body.should.eql({ name: &#x27;tobi&#x27;, age: &#x27;2 &#x27; });
    done();
  });</code></pre></dd>
        <dt>should support compound elements in a string</dt>
        <dd><pre><code>request
  .del(base)
  .query(&#x27;name=t%F6bi&#x26;age=2&#x27;)
  .end((error, res) =&#x3E; {
    res.body.should.eql({ name: &#x27;t%F6bi&#x27;, age: &#x27;2&#x27; });
    done();
  });</code></pre></dd>
        <dt>should work when called multiple times with a string</dt>
        <dd><pre><code>request
  .del(base)
  .query(&#x27;name=t%F6bi&#x27;)
  .query(&#x27;age=2%F6&#x27;)
  .end((error, res) =&#x3E; {
    res.body.should.eql({ name: &#x27;t%F6bi&#x27;, age: &#x27;2%F6&#x27; });
    done();
  });</code></pre></dd>
        <dt>should work with normal &#x60;query&#x60; object and query string</dt>
        <dd><pre><code>request
  .del(base)
  .query(&#x27;name=t%F6bi&#x27;)
  .query({ age: &#x27;2&#x27; })
  .end((error, res) =&#x3E; {
    res.body.should.eql({ name: &#x27;t%F6bi&#x27;, age: &#x27;2&#x27; });
    done();
  });</code></pre></dd>
        <dt>should not encode raw backticks, but leave encoded ones as is</dt>
        <dd><pre><code>return Promise.all([
  request
    .get(&#x60;${base}/raw-query&#x60;)
    .query(&#x27;name=&#x60;t%60bi&#x60;&#x26;age&#x60;=2&#x27;)
    .then((res) =&#x3E; {
      res.text.should.eql(&#x27;name=&#x60;t%60bi&#x60;&#x26;age&#x60;=2&#x27;);
    }),
  request.get(base + &#x27;/raw-query?&#x60;age%60&#x60;=2%60&#x60;&#x27;).then((res) =&#x3E; {
    res.text.should.eql(&#x27;&#x60;age%60&#x60;=2%60&#x60;&#x27;);
  }),
  request
    .get(&#x60;${base}/raw-query&#x60;)
    .query(&#x27;name=&#x60;t%60bi&#x60;&#x27;)
    .query(&#x27;age&#x60;=2&#x27;)
    .then((res) =&#x3E; {
      res.text.should.eql(&#x27;name=&#x60;t%60bi&#x60;&#x26;age&#x60;=2&#x27;);
    })
]);</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>req.query(Object)</h1>
      <dl>
        <dt>should construct the query-string</dt>
        <dd><pre><code>request
  .del(base)
  .query({ name: &#x27;tobi&#x27; })
  .query({ order: &#x27;asc&#x27; })
  .query({ limit: [&#x27;1&#x27;, &#x27;2&#x27;] })
  .end((error, res) =&#x3E; {
    res.body.should.eql({ name: &#x27;tobi&#x27;, order: &#x27;asc&#x27;, limit: [&#x27;1&#x27;, &#x27;2&#x27;] });
    done();
  });</code></pre></dd>
        <dt>should encode raw backticks</dt>
        <dd><pre><code>request
  .get(&#x60;${base}/raw-query&#x60;)
  .query({ name: &#x27;&#x60;tobi&#x60;&#x27; })
  .query({ &#x27;orde%60r&#x27;: null })
  .query({ &#x27;&#x60;limit&#x60;&#x27;: [&#x27;%602&#x60;&#x27;] })
  .end((error, res) =&#x3E; {
    res.text.should.eql(&#x27;name=%60tobi%60&#x26;orde%2560r&#x26;%60limit%60=%25602%60&#x27;);
    done();
  });</code></pre></dd>
        <dt>should not error on dates</dt>
        <dd><pre><code>const date = new Date(0);
request
  .del(base)
  .query({ at: date })
  .end((error, res) =&#x3E; {
    assert.equal(date.toISOString(), res.body.at);
    done();
  });</code></pre></dd>
        <dt>should work after setting header fields</dt>
        <dd><pre><code>request
  .del(base)
  .set(&#x27;Foo&#x27;, &#x27;bar&#x27;)
  .set(&#x27;Bar&#x27;, &#x27;baz&#x27;)
  .query({ name: &#x27;tobi&#x27; })
  .query({ order: &#x27;asc&#x27; })
  .query({ limit: [&#x27;1&#x27;, &#x27;2&#x27;] })
  .end((error, res) =&#x3E; {
    res.body.should.eql({ name: &#x27;tobi&#x27;, order: &#x27;asc&#x27;, limit: [&#x27;1&#x27;, &#x27;2&#x27;] });
    done();
  });</code></pre></dd>
        <dt>should append to the original query-string</dt>
        <dd><pre><code>request
  .del(&#x60;${base}/?name=tobi&#x60;)
  .query({ order: &#x27;asc&#x27; })
  .end((error, res) =&#x3E; {
    res.body.should.eql({ name: &#x27;tobi&#x27;, order: &#x27;asc&#x27; });
    done();
  });</code></pre></dd>
        <dt>should retain the original query-string</dt>
        <dd><pre><code>request.del(&#x60;${base}/?name=tobi&#x60;).end((error, res) =&#x3E; {
  res.body.should.eql({ name: &#x27;tobi&#x27; });
  done();
});</code></pre></dd>
        <dt>should keep only keys with null querystring values</dt>
        <dd><pre><code>request
  .del(&#x60;${base}/url&#x60;)
  .query({ nil: null })
  .end((error, res) =&#x3E; {
    res.text.should.equal(&#x27;/url?nil&#x27;);
    done();
  });</code></pre></dd>
        <dt>query-string should be sent on pipe</dt>
        <dd><pre><code>this.timeout(15_000);
const request_ = request.put(&#x60;${base}/?name=tobi&#x60;);
const stream = fs.createReadStream(&#x27;test/node/fixtures/user.json&#x27;);
request_.on(&#x27;response&#x27;, (res) =&#x3E; {
  res.body.should.eql({ name: &#x27;tobi&#x27; });
  done();
});
request_.on(&#x27;error&#x27;, (err) =&#x3E; {
  done(err);
});
stream.on(&#x27;error&#x27;, function (err) {
  done(err);
});
stream.pipe(request_);</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>request.get</h1>
      <dl>
        <section class="suite">
          <h1>on 301 redirect</h1>
          <dl>
            <dt>should follow Location with a GET request</dt>
            <dd><pre><code>const request_ = request.get(&#x60;${base}/test-301&#x60;).redirects(1);
request_.end((error, res) =&#x3E; {
  const headers = request_.req.getHeaders
    ? request_.req.getHeaders()
    : request_.req._headers;
  headers.host.should.eql(&#x60;localhost:${server2.address().port}&#x60;);
  res.status.should.eql(200);
  res.text.should.eql(&#x27;GET&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>on 302 redirect</h1>
          <dl>
            <dt>should follow Location with a GET request</dt>
            <dd><pre><code>const request_ = request.get(&#x60;${base}/test-302&#x60;).redirects(1);
request_.end((error, res) =&#x3E; {
  const headers = request_.req.getHeaders
    ? request_.req.getHeaders()
    : request_.req._headers;
  res.status.should.eql(200);
  res.text.should.eql(&#x27;GET&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>on 303 redirect</h1>
          <dl>
            <dt>should follow Location with a GET request</dt>
            <dd><pre><code>const request_ = request.get(&#x60;${base}/test-303&#x60;).redirects(1);
request_.end((error, res) =&#x3E; {
  const headers = request_.req.getHeaders
    ? request_.req.getHeaders()
    : request_.req._headers;
  headers.host.should.eql(&#x60;localhost:${server2.address().port}&#x60;);
  res.status.should.eql(200);
  res.text.should.eql(&#x27;GET&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>on 307 redirect</h1>
          <dl>
            <dt>should follow Location with a GET request</dt>
            <dd><pre><code>const request_ = request.get(&#x60;${base}/test-307&#x60;).redirects(1);
request_.end((error, res) =&#x3E; {
  const headers = request_.req.getHeaders
    ? request_.req.getHeaders()
    : request_.req._headers;
  headers.host.should.eql(&#x60;localhost:${server2.address().port}&#x60;);
  res.status.should.eql(200);
  res.text.should.eql(&#x27;GET&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>on 308 redirect</h1>
          <dl>
            <dt>should follow Location with a GET request</dt>
            <dd><pre><code>const request_ = request.get(&#x60;${base}/test-308&#x60;).redirects(1);
request_.end((error, res) =&#x3E; {
  const headers = request_.req.getHeaders
    ? request_.req.getHeaders()
    : request_.req._headers;
  headers.host.should.eql(&#x60;localhost:${server2.address().port}&#x60;);
  res.status.should.eql(200);
  res.text.should.eql(&#x27;GET&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>request.post</h1>
      <dl>
        <section class="suite">
          <h1>on 301 redirect</h1>
          <dl>
            <dt>should follow Location with a GET request</dt>
            <dd><pre><code>const request_ = request.post(&#x60;${base}/test-301&#x60;).redirects(1);
request_.end((error, res) =&#x3E; {
  const headers = request_.req.getHeaders
    ? request_.req.getHeaders()
    : request_.req._headers;
  headers.host.should.eql(&#x60;localhost:${server2.address().port}&#x60;);
  res.status.should.eql(200);
  res.text.should.eql(&#x27;GET&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>on 302 redirect</h1>
          <dl>
            <dt>should follow Location with a GET request</dt>
            <dd><pre><code>const request_ = request.post(&#x60;${base}/test-302&#x60;).redirects(1);
request_.end((error, res) =&#x3E; {
  const headers = request_.req.getHeaders
    ? request_.req.getHeaders()
    : request_.req._headers;
  headers.host.should.eql(&#x60;localhost:${server2.address().port}&#x60;);
  res.status.should.eql(200);
  res.text.should.eql(&#x27;GET&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>on 303 redirect</h1>
          <dl>
            <dt>should follow Location with a GET request</dt>
            <dd><pre><code>const request_ = request.post(&#x60;${base}/test-303&#x60;).redirects(1);
request_.end((error, res) =&#x3E; {
  const headers = request_.req.getHeaders
    ? request_.req.getHeaders()
    : request_.req._headers;
  headers.host.should.eql(&#x60;localhost:${server2.address().port}&#x60;);
  res.status.should.eql(200);
  res.text.should.eql(&#x27;GET&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>on 307 redirect</h1>
          <dl>
            <dt>should follow Location with a POST request</dt>
            <dd><pre><code>const request_ = request.post(&#x60;${base}/test-307&#x60;).redirects(1);
request_.end((error, res) =&#x3E; {
  const headers = request_.req.getHeaders
    ? request_.req.getHeaders()
    : request_.req._headers;
  headers.host.should.eql(&#x60;localhost:${server2.address().port}&#x60;);
  res.status.should.eql(200);
  res.text.should.eql(&#x27;POST&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>on 308 redirect</h1>
          <dl>
            <dt>should follow Location with a POST request</dt>
            <dd><pre><code>const request_ = request.post(&#x60;${base}/test-308&#x60;).redirects(1);
request_.end((error, res) =&#x3E; {
  const headers = request_.req.getHeaders
    ? request_.req.getHeaders()
    : request_.req._headers;
  headers.host.should.eql(&#x60;localhost:${server2.address().port}&#x60;);
  res.status.should.eql(200);
  res.text.should.eql(&#x27;POST&#x27;);
  done();
});</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>request</h1>
      <dl>
        <section class="suite">
          <h1>on redirect</h1>
          <dl>
            <dt>should merge cookies if agent is used</dt>
            <dd><pre><code>request
  .agent()
  .get(&#x60;${base}/cookie-redirect&#x60;)
  .set(&#x27;Cookie&#x27;, &#x27;orig=1; replaced=not&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.ifError(error);
      assert(/orig=1/.test(res.text), &#x27;orig=1/.test&#x27;);
      assert(/replaced=yes/.test(res.text), &#x27;replaced=yes/.test&#x27;);
      assert(/from-redir=1/.test(res.text), &#x27;from-redir=1&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should not merge cookies if agent is not used</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/cookie-redirect&#x60;)
  .set(&#x27;Cookie&#x27;, &#x27;orig=1; replaced=not&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert.ifError(error);
      assert(/orig=1/.test(res.text), &#x27;/orig=1&#x27;);
      assert(/replaced=not/.test(res.text), &#x27;/replaced=not&#x27;);
      assert(!/replaced=yes/.test(res.text), &#x27;!/replaced=yes&#x27;);
      assert(!/from-redir/.test(res.text), &#x27;!/from-redir&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should have previously set cookie for subsquent requests when agent is used</dt>
            <dd><pre><code>const agent = request.agent();
agent.get(&#x60;${base}/set-cookie&#x60;).end((error) =&#x3E; {
  assert.ifError(error);
  agent
    .get(&#x60;${base}/show-cookies&#x60;)
    .set({ Cookie: &#x27;orig=1&#x27; })
    .end((error, res) =&#x3E; {
      try {
        assert.ifError(error);
        assert(/orig=1/.test(res.text), &#x27;orig=1/.test&#x27;);
        assert(/persist=123/.test(res.text), &#x27;persist=123&#x27;);
        done();
      } catch (err) {
        done(err);
      }
    });
});</code></pre></dd>
            <dt>should follow Location</dt>
            <dd><pre><code>const redirects = [];
request
  .get(base)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    redirects.push(res.headers.location);
  })
  .end((error, res) =&#x3E; {
    try {
      const array = [&#x27;/movies&#x27;, &#x27;/movies/all&#x27;, &#x27;/movies/all/0&#x27;];
      redirects.should.eql(array);
      res.text.should.equal(&#x27;first movie page&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should follow Location with IP override</dt>
            <dd><pre><code>const redirects = [];
const url = URL.parse(base);
return request
  .get(&#x60;http://redir.example.com:${url.port || &#x27;80&#x27;}${url.pathname}&#x60;)
  .connect({
    &#x27;*&#x27;: url.hostname
  })
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    redirects.push(res.headers.location);
  })
  .then((res) =&#x3E; {
    const array = [&#x27;/movies&#x27;, &#x27;/movies/all&#x27;, &#x27;/movies/all/0&#x27;];
    redirects.should.eql(array);
    res.text.should.equal(&#x27;first movie page&#x27;);
  });</code></pre></dd>
            <dt>should follow Location with IP:port override</dt>
            <dd><pre><code>const redirects = [];
const url = URL.parse(base);
return request
  .get(&#x60;http://redir.example.com:9999${url.pathname}&#x60;)
  .connect({
    &#x27;*&#x27;: { host: url.hostname, port: url.port || 80 }
  })
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    redirects.push(res.headers.location);
  })
  .then((res) =&#x3E; {
    const array = [&#x27;/movies&#x27;, &#x27;/movies/all&#x27;, &#x27;/movies/all/0&#x27;];
    redirects.should.eql(array);
    res.text.should.equal(&#x27;first movie page&#x27;);
  });</code></pre></dd>
            <dt>should not follow on HEAD by default</dt>
            <dd><pre><code>const redirects = [];
return request
  .head(base)
  .ok(() =&#x3E; true)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    redirects.push(res.headers.location);
  })
  .then((res) =&#x3E; {
    redirects.should.eql([]);
    res.status.should.equal(302);
  });</code></pre></dd>
            <dt>should follow on HEAD when redirects are set</dt>
            <dd><pre><code>const redirects = [];
request
  .head(base)
  .redirects(10)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    redirects.push(res.headers.location);
  })
  .end((error, res) =&#x3E; {
    try {
      const array = [];
      array.push(&#x27;/movies&#x27;, &#x27;/movies/all&#x27;, &#x27;/movies/all/0&#x27;);
      redirects.should.eql(array);
      assert(!res.text);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should remove Content-* fields</dt>
            <dd><pre><code>request
  .post(&#x60;${base}/header&#x60;)
  .type(&#x27;txt&#x27;)
  .set(&#x27;X-Foo&#x27;, &#x27;bar&#x27;)
  .set(&#x27;X-Bar&#x27;, &#x27;baz&#x27;)
  .send(&#x27;hey&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert(res.body);
      res.body.should.have.property(&#x27;x-foo&#x27;, &#x27;bar&#x27;);
      res.body.should.have.property(&#x27;x-bar&#x27;, &#x27;baz&#x27;);
      res.body.should.not.have.property(&#x27;content-type&#x27;);
      res.body.should.not.have.property(&#x27;content-length&#x27;);
      res.body.should.not.have.property(&#x27;transfer-encoding&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should retain cookies</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/header&#x60;)
  .set(&#x27;Cookie&#x27;, &#x27;foo=bar;&#x27;)
  .end((error, res) =&#x3E; {
    try {
      assert(res.body);
      res.body.should.have.property(&#x27;cookie&#x27;, &#x27;foo=bar;&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should not resend query parameters</dt>
            <dd><pre><code>const redirects = [];
const query = [];
request
  .get(&#x60;${base}/?foo=bar&#x60;)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    query.push(res.headers.query);
    redirects.push(res.headers.location);
  })
  .end((error, res) =&#x3E; {
    try {
      const array = [];
      array.push(&#x27;/movies&#x27;, &#x27;/movies/all&#x27;, &#x27;/movies/all/0&#x27;);
      redirects.should.eql(array);
      res.text.should.equal(&#x27;first movie page&#x27;);
      query.should.eql([&#x27;{&#x22;foo&#x22;:&#x22;bar&#x22;}&#x27;, &#x27;{}&#x27;, &#x27;{}&#x27;]);
      res.headers.query.should.eql(&#x27;{}&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
            <dt>should handle no location header</dt>
            <dd><pre><code>request.get(&#x60;${base}/bad-redirect&#x60;).end((error, res) =&#x3E; {
  try {
    error.message.should.equal(&#x27;No location header for redirect&#x27;);
    done();
  } catch (err) {
    done(err);
  }
});</code></pre></dd>
            <section class="suite">
              <h1>when relative</h1>
              <dl>
                <dt>should redirect to a sibling path</dt>
                <dd><pre><code>const redirects = [];
request
  .get(&#x60;${base}/relative&#x60;)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    redirects.push(res.headers.location);
  })
  .end((error, res) =&#x3E; {
    try {
      redirects.should.eql([&#x27;tobi&#x27;]);
      res.text.should.equal(&#x27;tobi&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
                <dt>should redirect to a parent path</dt>
                <dd><pre><code>const redirects = [];
request
  .get(&#x60;${base}/relative/sub&#x60;)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    redirects.push(res.headers.location);
  })
  .end((error, res) =&#x3E; {
    try {
      redirects.should.eql([&#x27;../tobi&#x27;]);
      res.text.should.equal(&#x27;tobi&#x27;);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
              </dl>
            </section>
          </dl>
        </section>
        <section class="suite">
          <h1>req.redirects(n)</h1>
          <dl>
            <dt>should alter the default number of redirects to follow</dt>
            <dd><pre><code>const redirects = [];
request
  .get(base)
  .redirects(2)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    redirects.push(res.headers.location);
  })
  .end((error, res) =&#x3E; {
    try {
      const array = [];
      assert(res.redirect, &#x27;res.redirect&#x27;);
      array.push(&#x27;/movies&#x27;, &#x27;/movies/all&#x27;);
      redirects.should.eql(array);
      res.text.should.match(/Moved Temporarily|Found/);
      done();
    } catch (err) {
      done(err);
    }
  });</code></pre></dd>
          </dl>
        </section>
        <section class="suite">
          <h1>on POST</h1>
          <dl>
            <dt>should redirect as GET</dt>
            <dd><pre><code>const redirects = [];
return request
  .post(&#x60;${base}/movie&#x60;)
  .send({ name: &#x27;Tobi&#x27; })
  .redirects(2)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    redirects.push(res.headers.location);
  })
  .then((res) =&#x3E; {
    redirects.should.eql([&#x27;/movies/all/0&#x27;]);
    res.text.should.equal(&#x27;first movie page&#x27;);
  });</code></pre></dd>
            <dt>using multipart/form-data should redirect as GET</dt>
            <dd><pre><code>const redirects = [];
request
  .post(&#x60;${base}/movie&#x60;)
  .type(&#x27;form&#x27;)
  .field(&#x27;name&#x27;, &#x27;Tobi&#x27;)
  .redirects(2)
  .on(&#x27;redirect&#x27;, (res) =&#x3E; {
    redirects.push(res.headers.location);
  })
  .then((res) =&#x3E; {
    redirects.should.eql([&#x27;/movies/all/0&#x27;]);
    res.text.should.equal(&#x27;first movie page&#x27;);
  });</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>response</h1>
      <dl>
        <dt>should act as a readable stream</dt>
        <dd><pre><code>const request_ = request.get(base).buffer(false);
request_.end((error, res) =&#x3E; {
  if (error) return done(error);
  let trackEndEvent = 0;
  let trackCloseEvent = 0;
  res.on(&#x27;end&#x27;, () =&#x3E; {
    trackEndEvent++;
    trackEndEvent.should.equal(1);
    if (!process.env.HTTP2_TEST) {
      trackCloseEvent.should.equal(0); // close should not have been called
    }
    done();
  });
  res.on(&#x27;close&#x27;, () =&#x3E; {
    trackCloseEvent++;
  });
  setTimeout(() =&#x3E; {
    (() =&#x3E; {
      res.pause();
    }).should.not.throw();
    (() =&#x3E; {
      res.resume();
    }).should.not.throw();
    (() =&#x3E; {
      res.destroy();
    }).should.not.throw();
  }, 50);
});</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>req.serialize(fn)</h1>
      <dl>
        <dt>should take precedence over default parsers</dt>
        <dd><pre><code>request
  .post(&#x60;${base}/echo&#x60;)
  .send({ foo: 123 })
  .serialize(() =&#x3E; &#x27;{&#x22;bar&#x22;:456}&#x27;)
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    assert.equal(&#x27;{&#x22;bar&#x22;:456}&#x27;, res.text);
    assert.equal(456, res.body.bar);
    done();
  });</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>res.toError()</h1>
      <dl>
        <dt>should return an Error</dt>
        <dd><pre><code>request.get(base).end((err, res) =&#x3E; {
  const error = res.toError();
  assert.equal(error.status, 400);
  assert.equal(error.method, &#x27;GET&#x27;);
  assert.equal(error.path, &#x27;/&#x27;);
  assert.equal(error.message, &#x27;cannot GET / (400)&#x27;);
  assert.equal(error.text, &#x27;invalid json&#x27;);
  done();
});</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>[unix-sockets] http</h1>
      <dl>
        <section class="suite">
          <h1>request</h1>
          <dl>
            <dt>path: / (root)</dt>
            <dd><pre><code>request.get(&#x60;${base}/&#x60;).end((error, res) =&#x3E; {
  assert(res.ok);
  assert.strictEqual(&#x27;root ok!&#x27;, res.text);
  done();
});</code></pre></dd>
            <dt>path: /request/path</dt>
            <dd><pre><code>request.get(&#x60;${base}/request/path&#x60;).end((error, res) =&#x3E; {
  assert(res.ok);
  assert.strictEqual(&#x27;request path ok!&#x27;, res.text);
  done();
});</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>[unix-sockets] https</h1>
      <dl>
        <section class="suite">
          <h1>request</h1>
          <dl>
            <dt>path: / (root)</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/&#x60;)
  .ca(cacert)
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    assert(res.ok);
    assert.strictEqual(&#x27;root ok!&#x27;, res.text);
    done();
  });</code></pre></dd>
            <dt>path: /request/path</dt>
            <dd><pre><code>request
  .get(&#x60;${base}/request/path&#x60;)
  .ca(cacert)
  .end((error, res) =&#x3E; {
    assert.ifError(error);
    assert(res.ok);
    assert.strictEqual(&#x27;request path ok!&#x27;, res.text);
    done();
  });</code></pre></dd>
          </dl>
        </section>
      </dl>
    </section>
    <section class="suite">
      <h1>req.get()</h1>
      <dl>
        <dt>should not set a default user-agent</dt>
        <dd><pre><code>request.get(&#x60;${base}/ua&#x60;).then((res) =&#x3E; {
      assert(res.headers);
      assert(!res.headers[&#x27;user-agent&#x27;]);
    })</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>utils.type(str)</h1>
      <dl>
        <dt>should return the mime type</dt>
        <dd><pre><code>utils
  .type(&#x27;application/json; charset=utf-8&#x27;)
  .should.equal(&#x27;application/json&#x27;);
utils.type(&#x27;application/json&#x27;).should.equal(&#x27;application/json&#x27;);</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>utils.params(str)</h1>
      <dl>
        <dt>should return the field parameters</dt>
        <dd><pre><code>const object = utils.params(&#x27;application/json; charset=utf-8; foo  = bar&#x27;);
object.charset.should.equal(&#x27;utf-8&#x27;);
object.foo.should.equal(&#x27;bar&#x27;);
utils.params(&#x27;application/json&#x27;).should.eql({});</code></pre></dd>
      </dl>
    </section>
    <section class="suite">
      <h1>utils.parseLinks(str)</h1>
      <dl>
        <dt>should parse links</dt>
        <dd><pre><code>const string_ =
  &#x27;&#x3C;https://api.github.com/repos/visionmedia/mocha/issues?page=2&#x3E;; rel=&#x22;next&#x22;, &#x3C;https://api.github.com/repos/visionmedia/mocha/issues?page=5&#x3E;; rel=&#x22;last&#x22;&#x27;;
const returnValue = utils.parseLinks(string_);
returnValue.next.should.equal(
  &#x27;https://api.github.com/repos/visionmedia/mocha/issues?page=2&#x27;
);
returnValue.last.should.equal(
  &#x27;https://api.github.com/repos/visionmedia/mocha/issues?page=5&#x27;
);</code></pre></dd>
      </dl>
    </section>
-------------------|---------|----------|---------|---------|---------------------------------------
File               | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s                     
-------------------|---------|----------|---------|---------|---------------------------------------
All files          |   93.42 |     83.3 |   89.67 |   93.92 |                                       
 src               |    92.5 |    83.83 |   91.83 |   93.84 |                                       
  agent-base.js    |     100 |      100 |     100 |     100 |                                       
  request-base.js  |   91.01 |     83.9 |   94.28 |   93.06 | ...21,262,316,501,525-533,579,757,768 
  response-base.js |     100 |      100 |      75 |     100 |                                       
  utils.js         |   92.85 |    71.42 |   85.71 |   91.66 | 94-98                                 
 src/node          |   93.61 |    83.12 |   87.36 |   93.75 |                                       
  agent.js         |   89.79 |    66.66 |     100 |   88.63 | 39,43,47,51,101                       
  http2wrapper.js  |      96 |     82.6 |   89.47 |   96.26 | 14,83,185-186                         
  index.js         |   93.36 |    83.63 |   89.47 |   93.66 | ...,977,1182-1186,1220-1221,1275,1301 
  response.js      |      90 |    83.33 |   55.55 |   89.79 | 78,86,94,120-121                      
  unzip.js         |     100 |    92.85 |     100 |     100 | 47                                    
 src/node/parsers  |   97.61 |       75 |     100 |   97.61 |                                       
  image.js         |     100 |      100 |     100 |     100 |                                       
  index.js         |     100 |      100 |     100 |     100 |                                       
  json.js          |     100 |       75 |     100 |     100 | 15                                    
  text.js          |     100 |      100 |     100 |     100 |                                       
  urlencoded.js    |      90 |      100 |     100 |      90 | 17                                    
-------------------|---------|----------|---------|---------|---------------------------------------
    </div>
    <a href="http://github.com/ladjs/superagent"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://s3.amazonaws.com/github/ribbons/forkme_right_white_ffffff.png" alt="Fork me on GitHub"></a>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.0/jquery.min.js"></script>
    <script>
      $('code').each(function(){
        $(this).html(highlight($(this).text()));
      });

      function highlight(js) {
        return js
          .replace(/</g, '&lt;')
          .replace(/>/g, '&gt;')
          .replace(/('.*?')/gm, '<span class="string">$1</span>')
          .replace(/(\d+\.\d+)/gm, '<span class="number">$1</span>')
          .replace(/(\d+)/gm, '<span class="number">$1</span>')
          .replace(/\bnew *(\w+)/gm, '<span class="keyword">new</span> <span class="init">$1</span>')
          .replace(/\b(function|new|throw|return|var|if|else)\b/gm, '<span class="keyword">$1</span>')
      }
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/tocbot/3.0.0/tocbot.js"></script>
    <script>
      // Only use tocbot for main docs, not test docs
      if (document.querySelector('#superagent')) {
        tocbot.init({
          // Where to render the table of contents.
          tocSelector: '#menu',
          // Where to grab the headings to build the table of contents.
          contentSelector: '#content',
          // Which headings to grab inside of the contentSelector element.
          headingSelector: 'h2',
          smoothScroll: false
        });
      }
    </script>
  </body>
</html>
```

## File: `docs/ko_KR/index.html`
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf8" />
    <title>SuperAgent — elegant API for AJAX in Node and browsers</title>
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/tocbot/3.0.0/tocbot.css"
    />
    <link rel="stylesheet" href="../style.css" />
  </head>
  <body>
    <ul id="menu"></ul>
    <div id="content">
      <h1 id="superagent">SuperAgent</h1>
      <p>
        SuperAgent는 기존의 복잡한 요청 API에 대한 불만에서 출발해 유연성,
        가독성, 그리고 낮은 학습 난이도를 목표로 설계된 경량 Ajax API입니다.
        또한 Node.js 환경에서도 동작합니다!
      </p>
      <pre><code class="language-javascript">     request
       .post(&#39;/api/pet&#39;)
       .send({ name: &#39;Manny&#39;, species: &#39;cat&#39; })
       .set(&#39;X-API-Key&#39;, &#39;foobar&#39;)
       .set(&#39;Accept&#39;, &#39;application/json&#39;)
       .then(res =&gt; {
          alert(&#39;yay got &#39; + JSON.stringify(res.body));
       });
</code></pre>
      <h2 id="test-documentation">테스트 문서</h2>
      <p>
        <a href="../../index.html"><strong>English</strong></a>
      </p>
      <p>
        다음의 <a href="../test.html">테스트 문서</a>는
        <a href="https://mochajs.org/">Mocha&#39;s</a> &quot;doc&quot; 리포터를
        사용해 생성되었으며, 실제 테스트 스위트를 직접 반영합니다. 이 문서는
        추가적인 참고 자료로 활용할 수 있습니다.
      </p>
      <h2 id="request-basics">기본 요청</h2>
      <p>
        요청은 <code>request</code> 객체에서 적절한 메서드를 호출하여 시작되며,
        그 다음 <code>.then()</code> 또는 <code>.end()</code> 혹은
        <a href="#promise-and-generator-support"><code>await</code></a
        >를 사용해 요청을 전송할 수 있습니다. 예를 들어, 간단한
        <strong>GET</strong> 요청은 다음과 같습니다.
      </p>
      <pre><code class="language-javascript">     request
       .get(&#39;/search&#39;)
       .then(res =&gt; {
          // res.body, res.headers, res.status
       })
       .catch(err =&gt; {
          // err.message, err.response
       });
</code></pre>
      <p>HTTP 메서드는 문자열로도 전달할 수 있습니다.</p>
      <pre><code class="language-javascript">    request(&#39;GET&#39;, &#39;/search&#39;).then(success, failure);
</code></pre>
      <p>
        예전 방식의 콜백도 지원되지만, 권장되지는 않습니다.
        <code>.then()</code> 대신 <code>.end()</code>를 호출하여 요청을 전송할
        수 있습니다.
      </p>
      <pre><code class="language-javascript">    request(&#39;GET&#39;, &#39;/search&#39;).end(function(err, res){
      if (res.ok) {}
    });
</code></pre>
      <p>
        절대 URL을 사용할 수 있습니다. 단, 웹 브라우저에서는 서버가
        <a href="#cors">CORS</a>를 구현한 경우에만 절대 URL이 정상적으로
        작동합니다.
      </p>
      <pre><code class="language-javascript">     request
       .get(&#39;https://example.com/search&#39;)
       .then(res =&gt; {

       });
</code></pre>
      <p>
        <strong>Node</strong> 클라이언트는
        <a
          href="https://ko.wikipedia.org/wiki/%EC%9C%A0%EB%8B%89%EC%8A%A4_%EB%8F%84%EB%A9%94%EC%9D%B8_%EC%86%8C%EC%BC%93"
          >유닉스 도메인 소켓</a
        >을 통한 요청을 지원합니다.
      </p>
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
      <p>
        <strong>DELETE</strong>, <strong>HEAD</strong>, <strong>PATCH</strong>,
        <strong>POST</strong>, and <strong>PUT</strong> 요청도 사용할 수 있으며,
        다음 예시에서 메서드 이름만 변경하면 됩니다.
      </p>
      <pre><code class="language-javascript">    request
      .head(&#39;/favicon.ico&#39;)
      .then(res =&gt; {

      });
</code></pre>
      <p>
        <strong>DELETE</strong>는 <code>delete</code>가 예약어였던 구형 IE와의
        호환성을 위해 <code>.del()</code> 메서드로도 호출할 수 있습니다.
      </p>
      <p>
        HTTP 메서드의 기본값은 <strong>GET</strong>이므로, 다음과 같이 작성해도
        유효합니다.
      </p>
      <pre><code class="language-javascript">     request(&#39;/search&#39;, (err, res) =&gt; {

     });
</code></pre>
      <h2 id="using-http/2">HTTP/2 사용하기</h2>
      <p>
        HTTP/1.x 폴백 없이 HTTP/2 프로토콜만 사용하려면
        <code>.http2()</code> 메서드를 호출하여 요청을 전송할 수 있습니다.
      </p>
      <pre><code class="language-javascript">    const request = require(&#39;superagent&#39;);
    const res = await request
      .get(&#39;https://example.com/h2&#39;)
      .http2();
</code></pre>
      <h2 id="setting-header-fields">헤더 필드 설정하기</h2>
      <p>
        헤더 필드 설정은 간단합니다. 필드 이름과 값을
        <code>.set()</code> 메서드에 전달하면 됩니다.
      </p>
      <pre><code class="language-javascript">     request
       .get(&#39;/search&#39;)
       .set(&#39;API-Key&#39;, &#39;foobar&#39;)
       .set(&#39;Accept&#39;, &#39;application/json&#39;)
       .then(callback);
</code></pre>
      <p>여러 개의 헤더 필드를 한 번에 설정하려면 객체를 전달하면 됩니다.</p>
      <pre><code class="language-javascript">     request
       .get(&#39;/search&#39;)
       .set({ &#39;API-Key&#39;: &#39;foobar&#39;, Accept: &#39;application/json&#39; })
       .then(callback);
</code></pre>
      <h2 id="get-requests"><code>GET</code> 요청</h2>
      <p>
        <code>.query()</code> 메서드는 객체를 인자로 받아
        <strong>GET</strong> 요청 시 쿼리 문자열을 자동으로 생성합니다. 예를
        들어 다음 코드는
        <code>/search?query=Manny&amp;range=1..5&amp;order=desc</code> 경로를
        생성합니다.
      </p>
      <pre><code class="language-javascript">     request
       .get(&#39;/search&#39;)
       .query({ query: &#39;Manny&#39; })
       .query({ range: &#39;1..5&#39; })
       .query({ order: &#39;desc&#39; })
       .then(res =&gt; {

       });
</code></pre>
      <p>또는 하나의 객체로 설정할 수 있습니다.</p>
      <pre><code class="language-javascript">    request
      .get(&#39;/search&#39;)
      .query({ query: &#39;Manny&#39;, range: &#39;1..5&#39;, order: &#39;desc&#39; })
      .then(res =&gt; {

      });
</code></pre>
      <p><code>.query()</code> 메서드는 문자열도 받습니다.</p>
      <pre><code class="language-javascript">      request
        .get(&#39;/querystring&#39;)
        .query(&#39;search=Manny&amp;range=1..5&#39;)
        .then(res =&gt; {

        });
</code></pre>
      <p>조인할 수도 있습니다.</p>
      <pre><code class="language-javascript">      request
        .get(&#39;/querystring&#39;)
        .query(&#39;search=Manny&#39;)
        .query(&#39;range=1..5&#39;)
        .then(res =&gt; {

        });
</code></pre>
      <h2 id="head-requests"><code>HEAD</code> 요청하기</h2>
      <p>
        HEAD 요청에서도 <code>.query()</code> 메서드를 사용할 수 있습니다. 예를
        들어 다음 코드는 <code>/users?email=joe@smith.com</code> 경로를
        생성합니다.
      </p>
      <pre><code class="language-javascript">      request
        .head(&#39;/users&#39;)
        .query({ email: &#39;joe@smith.com&#39; })
        .then(res =&gt; {

        });
</code></pre>
      <h2 id="post--put-requests"><code>POST</code> / <code>PUT</code> 요청</h2>
      <p>
        전형적인 JSON <strong>POST</strong> 요청은 Content-Type 헤더를 적절히
        설정하고, 데이터를 JSON 형식으로 전송하는 방식입니다. 예를 들어 다음과
        같은 코드가 이에 해당합니다.
      </p>
      <pre><code class="language-javascript">      request.post(&#39;/user&#39;)
        .set(&#39;Content-Type&#39;, &#39;application/json&#39;)
        .send(&#39;{&quot;name&quot;:&quot;tj&quot;,&quot;pet&quot;:&quot;tobi&quot;}&#39;)
        .then(callback)
        .catch(errorCallback)
</code></pre>
      <p>
        JSON은 가장 일반적으로 사용되므로 기본값으로 설정되어 있습니다. 다음
        예제는 앞선 예제와 동일한 동작을 수행합니다.
      </p>
      <pre><code class="language-javascript">      request.post(&#39;/user&#39;)
        .send({ name: &#39;tj&#39;, pet: &#39;tobi&#39; })
        .then(callback, errorCallback)
</code></pre>
      <p>또는 <code>.send()</code> 여러 번 호출할 수 있습니다.</p>
      <pre><code class="language-javascript">      request.post(&#39;/user&#39;)
        .send({ name: &#39;tj&#39; })
        .send({ pet: &#39;tobi&#39; })
        .then(callback, errorCallback)
</code></pre>
      <p>
        기본적으로 문자열을 전송하면 <code>Content-Type</code>이
        <code>application/x-www-form-urlencoded</code>로 자동 설정됩니다. 여러
        번 <code>.send()</code>를 호출하면 각 문자열이 <code>&amp;</code>로
        연결되어 최종적으로 <code>name=tj&amp;pet=tobi</code>와 같은 결과가
        생성됩니다.
      </p>
      <pre><code class="language-javascript">      request.post(&#39;/user&#39;)
        .send(&#39;name=tj&#39;)
        .send(&#39;pet=tobi&#39;)
        .then(callback, errorCallback);
</code></pre>
      <p>
        SuperAgent는 다양한 형식으로 확장 가능하지만, 기본적으로
        &quot;json&quot;과 &quot;form&quot; 형식을 지원합니다.
        <code>application/x-www-form-urlencoded</code> 형식으로 데이터를
        전송하려면 <code>.type('form')</code>을 호출하면 됩니다. 기본 형식은
        &quot;json&quot;입니다. 다음 요청은 본문에
        &quot;name=tj&amp;pet=tobi&quot;를 포함하여 <strong>POST</strong>됩니다.
      </p>
      <pre><code class="language-javascript">      request.post(&#39;/user&#39;)
        .type(&#39;form&#39;)
        .send({ name: &#39;tj&#39; })
        .send({ pet: &#39;tobi&#39; })
        .then(callback, errorCallback)
</code></pre>
      <p>
        <a href="https://developer.mozilla.org/ko/../Web/API/FormData/FormData"
          ><code>FormData</code></a
        >
        객체를 사용하는 것도 지원됩니다. 다음 예제는 id=&quot;myForm&quot;인
        HTML 폼의 내용을 <strong>POST</strong> 방식으로 전송합니다.
      </p>
      <pre><code class="language-javascript">      request.post(&#39;/user&#39;)
        .send(new FormData(document.getElementById(&#39;myForm&#39;)))
        .then(callback, errorCallback)
</code></pre>
      <h2 id="setting-the-content-type"><code>Content-Type</code> 설정하기</h2>
      <p>
        가장 명확한 해결책은 <code>.set()</code> 메서드를 사용하는 것입니다.
      </p>
      <pre><code class="language-javascript">     request.post(&#39;/user&#39;)
       .set(&#39;Content-Type&#39;, &#39;application/json&#39;)
</code></pre>
      <p>
        간단하게 <code>.type()</code> 메서드를 사용할 수 있으며, 표준화된 MIME
        타입(<code>type/subtype</code>)을 직접 지정하거나 &quot;xml&quot;,
        &quot;json&quot;, &quot;png&quot; 등과 같은 확장자 이름만으로도 설정할
        수 있습니다.
      </p>
      <pre><code class="language-javascript">     request.post(&#39;/user&#39;)
       .type(&#39;application/json&#39;)

     request.post(&#39;/user&#39;)
       .type(&#39;json&#39;)

     request.post(&#39;/user&#39;)
       .type(&#39;png&#39;)
</code></pre>
      <h2 id="serializing-request-body">요청 본문 직렬화하기</h2>
      <p>
        SuperAgent는 기본적으로 JSON과 폼 데이터를 자동으로 직렬화합니다. 또한
        다른 콘텐츠 유형에 대해서도 자동 직렬화를 설정할 수 있습니다.
      </p>
      <pre><code class="language-js">request.serialize[&#39;application/xml&#39;] = function (obj) {
    return &#39;string generated from obj&#39;;
};

// &#39;application/xml&#39; Content-type을 가진 모든 요청은
// 자동으로 직렬화 됩니다.
</code></pre>
      <p>
        사용자 정의 형식으로 페이로드를 전송하려면, 요청 단위로
        <code>.serialize()</code>
        메서드를 사용해 SuperAgent의 기본 직렬화 방식을 교체할 수 있습니다.
      </p>
      <pre><code class="language-js">request
    .post(&#39;/user&#39;)
    .send({foo: &#39;bar&#39;})
    .serialize(obj =&gt; {
        return &#39;string generated from obj&#39;;
    });
</code></pre>
      <h2 id="retrying-requests">요청 재시도하기</h2>
      <p>
        <code>.retry()</code> 메서드를 사용하면, 일시적인 오류나 불안정한 인터넷
        연결로 인해 요청이 실패한 경우 SuperAgent가 자동으로 재시도합니다.
      </p>
      <p>
        이 메서드는 두 개의 선택적 인자를 받습니다. 재시도 횟수(기본값은 1)와
        콜백 함수입니다. 각 재시도 전에 <code>callback(err, res)</code>를
        호출합니다. 콜백 함수는 요청을 재시도할지 여부를 결정하기 위해
        <code>true</code> 또는 <code>false</code>를 반환할 수 있습니다. 단, 최대
        재시도 횟수는 항상 적용됩니다.
      </p>
      <pre><code class="language-javascript">     request
       .get(&#39;https://example.com/search&#39;)
       .retry(2) // 혹은
       .retry(2, callback)
       .then(finished);
       .catch(failed);
</code></pre>
      <p>
        멱등한 요청인 경우에만 <code>.retry()</code> 메서드를 사용하세요. 예를
        들어, 동일한 요청이 서버에 여러 번 도달하더라도 중복 구매와 같은
        바람직하지 않은 부작용이 발생하지 않아야 합니다.
      </p>
      <p>
        모든 요청 메서드는 기본적으로 재시도 대상에 포함됩니다. 따라서 POST
        요청을 재시도하지 않도록 하려면, 사용자 정의 재시도 콜백을 전달해야
        합니다.
      </p>
      <p>기본적으로 다음과 같은 상태 코드는 자동으로 재시도됩니다.</p>
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
      <p>기본적으로 다음과 같은 오류 코드가 자동으로 재시도됩니다.</p>
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
      <h2 id="setting-accept">Accept 설정하기</h2>
      <p>
        <code>.type()</code> 메서드와 유사하게, <code>.accept()</code> 메서드를
        사용하면 <code>Accept</code> 헤더를 간편하게 설정할 수 있습니다. 이
        메서드는 <code>request.types</code>를 참조하며,
        <code>type/subtype</code> 형식의 MIME 타입 전체 이름이나
        &quot;xml&quot;, &quot;json&quot;, &quot;png&quot; 등의 확장자 형태로도
        지정할 수 있어 편리합니다.
      </p>
      <pre><code class="language-javascript">     request.get(&#39;/user&#39;)
       .accept(&#39;application/json&#39;)

     request.get(&#39;/user&#39;)
       .accept(&#39;json&#39;)

     request.post(&#39;/user&#39;)
       .accept(&#39;png&#39;)
</code></pre>
      <h3 id="facebook-and-accept-json">Facebook과 Accept JSON</h3>
      <p>
        Facebook API를 호출할 때는 반드시 요청 헤더에
        <code>Accept: application/json</code>을 포함해야 합니다. 그렇지 않으면
        Facebook은 <code>Content-Type: text/javascript; charset=UTF-8</code>으로
        응답하게 되며, SuperAgent는 이 형식을 파싱하지 못해
        <code>res.body</code>가 undefined가 됩니다.
        <code>req.accept(&#39;json&#39;)</code> 또는
        <code>req.set(&#39;Accept&#39;, &#39;application/json&#39;)</code>을
        사용할 수 있습니다. 자세한 사항은
        <a href="https://github.com/ladjs/superagent/issues/1078">issue 1078</a>
        에서 확인해보세요.
      </p>
      <h2 id="query-strings">쿼리 문자열</h2>
      <p>
        <code>req.query(obj)</code>는 쿼리 문자열을 구성하는 데 사용되는
        메서드입니다. 예를 들어 <strong>POST</strong> 요청에서
        <code>?format=json&amp;dest=/login</code>과 같은 쿼리 문자열을 추가할 수
        있습니다.
      </p>
      <pre><code class="language-javascript">    request
      .post(&#39;/&#39;)
      .query({ format: &#39;json&#39; })
      .query({ dest: &#39;/login&#39; })
      .send({ post: &#39;data&#39;, here: &#39;wahoo&#39; })
      .then(callback);
</code></pre>
      <p>
        기본적으로 쿼리 문자열은 특정한 순서로 조립되지 않습니다. ASCII 순으로
        정렬된 쿼리 문자열을 사용하려면
        <code>req.sortQuery()</code>를 호출하면 됩니다. 또한
        <code>req.sortQuery(myComparisonFn)</code>을 통해 사용자 정의 정렬 비교
        함수를 전달할 수도 있습니다. 비교 함수는 두 개의 인자를 받아 음수, 0
        또는 양수를 반환해야 합니다.
      </p>
      <pre><code class="language-js"> // 기본 정렬 방식
 request.get(&#39;/user&#39;)
   .query(&#39;name=Nick&#39;)
   .query(&#39;search=Manny&#39;)
   .sortQuery()
   .then(callback)

 // 사용자 정의 정렬 함수
 request.get(&#39;/user&#39;)
   .query(&#39;name=Nick&#39;)
   .query(&#39;search=Manny&#39;)
   .sortQuery((a, b) =&gt; a.length - b.length)
   .then(callback)
</code></pre>
      <h2 id="tls-options">TLS 옵션</h2>
      <p>
        Node.js에서 SuperAgent는 HTTPS 요청을 구성할 수 있는 다양한 메서드를
        지원합니다.
      </p>
      <ul>
        <li><code>.ca()</code>: 신뢰할 CA 인증서를 설정합니다.</li>
        <li><code>.cert()</code>: 클라이언트 인증서 체인을 설정합니다.</li>
        <li><code>.key()</code>: 클라이언트의 개인 키를 설정합니다.</li>
        <li>
          <code>.pfx()</code>: PKCS12 형식의 PFX 파일을 사용하여 클라이언트의
          개인 키와 인증서 체인을 설정합니다.
        </li>
        <li>
          <code>.disableTLSCerts()</code>: 만료되었거나 유효하지 않은 TLS
          인증서를 거부하지 않도록 설정합니다. 내부적으로
          <code>rejectUnauthorized=true</code>가 설정되며, 중간자 공격(MITM)에
          노출될 수 있으므로 주의가 필요합니다.
        </li>
      </ul>
      <p>
        더 자세한 내용은 Node.js
        <a
          href="https://nodejs.org/api/https.html#https_https_request_options_callback"
          >https.request 문서</a
        >에서 확인할 수 있습니다.
      </p>
      <pre><code class="language-js">var key = fs.readFileSync(&#39;key.pem&#39;),
    cert = fs.readFileSync(&#39;cert.pem&#39;);

request
  .post(&#39;/client-auth&#39;)
  .key(key)
  .cert(cert)
  .then(callback);
</code></pre>
      <pre><code class="language-js">var ca = fs.readFileSync(&#39;ca.cert.pem&#39;);

request
  .post(&#39;https://localhost/private-ca-server&#39;)
  .ca(ca)
  .then(res =&gt; {});
</code></pre>
      <h2 id="parsing-response-bodies">응답 본문 파싱하기</h2>
      <p>
        SuperAgent는 응답 본문 데이터를 자동으로 파싱해줍니다. 현재
        <code>application/x-www-form-urlencoded</code>,
        <code>application/json</code>, <code>multipart/form-data</code>을
        지원합니다. 이외의 응답 본문 데이터에 대해서도 자동 파싱을 설정할 수
        있습니다.
      </p>
      <pre><code class="language-js">// 브라우저
request.parse[&#39;application/xml&#39;] = function (str) {
    return {&#39;object&#39;: &#39;parsed from str&#39;};
};

// node
request.parse[&#39;application/xml&#39;] = function (res, cb) {
    //parse response text and set res.body here

    cb(null, res);
};

// 앞으로 &#39;application/xml&#39; 유형의 반응은
// 자동으로 파싱됩니다
</code></pre>
      <p>
        <code>.buffer(true).parse(fn)</code> 메서드를 사용하면 내장된 파서보다
        우선적으로 적용되는 사용자 정의 파서를 설정할 수 있습니다.
        <code>.buffer(false)</code>로 응답 버퍼링이 비활성화되어 있다면,
        <code>response</code> 이벤트는 본문 파싱이 완료되기 전에 발생하므로
        <code>response.body</code>를 사용할 수 없습니다.
      </p>
      <h3 id="json--urlencoded">JSON / Urlencoded</h3>
      <p>
        <code>res.body</code> 속성은 파싱된 객체를 나타냅니다. 예를 들어, 응답이
        JSON 문자열
        &#39;{&quot;user&quot;:{&quot;name&quot;:&quot;tobi&quot;}}&#39;를
        반환했다면, <code>res.body.user.name</code>은 &quot;tobi&quot; 값을 갖게
        됩니다. 마찬가지로 x-www-form-urlencoded 형식의
        &quot;user[name]=tobi&quot;도 동일한 결과를 제공합니다. 단, 중첩은 한
        단계까지만 지원되므로 더 복잡한 구조의 데이터를 다루려면 JSON 형식을
        사용하는 것이 좋습니다.
      </p>
      <p>
        배열은 key를 반복해서 전달하는 방식으로 전송됩니다.
        <code>.send({color: [&#39;red&#39;,&#39;blue&#39;]})</code>는
        <code>color=red&amp;color=blue</code>로 변환되어 전송됩니다. 배열의
        key에 <code>[]</code>를 포함시키고 싶다면 SuperAgent는 이를 자동으로
        처리하지 않으므로, 직접 <code>color[]</code>와 같이 key 이름에 대괄호를
        추가해야 합니다.
      </p>
      <h3 id="multipart">다중 파트</h3>
      <p>
        Node 클라이언트는
        <a href="https://github.com/felixge/node-formidable">Formidable</a>
        모듈을 통해 <em>multipart/form-data</em>를 지원합니다. 다중 파트 응답을
        파싱할 때 <code>res.files</code> 객체를 사용할 수 있으며, 이 객체에는
        업로드된 파일에 대한 정보가 포함됩니다. 예를 들어, 다음과 같은 multipart
        본문을 포함한 응답을 가정해볼 수 있습니다.
      </p>
      <pre><code>--whoop
Content-Disposition: attachment; name=&quot;image&quot;; filename=&quot;tobi.png&quot;
Content-Type: image/png

... data here ...
--whoop
Content-Disposition: form-data; name=&quot;name&quot;
Content-Type: text/plain

Tobi
--whoop--
</code></pre>
      <p>
        <code>res.body.name</code>은 &quot;Tobi&quot; 값을 가지고 있으며,
        <code>res.files.image</code>는 디스크 경로, 파일 이름 및 기타 속성을
        포함한 <code>File</code> 객체입니다.
      </p>
      <h3 id="binary">바이너리</h3>
      <p>
        브라우저에서는 바이너리 응답 본문을 처리하기 위해
        <code>.responseType(&#39;blob&#39;)</code>을 사용할 수 있습니다. 이
        API는 Node.js 환경에서는 필요하지 않습니다. 이 메서드에서 지원되는 인자
        값은 다음과 같습니다.
      </p>
      <ul>
        <li>
          <code>&#39;blob&#39;</code>는 XMLHttpRequest의
          <code>responseType</code> 속성에 그대로 전달됩니다.
        </li>
        <li>
          <code>&#39;arraybuffer&#39;</code>도 마찬가지로
          <code>responseType</code> 속성에 전달됩니다.
        </li>
      </ul>
      <pre><code class="language-js">req.get(&#39;/binary.data&#39;)
  .responseType(&#39;blob&#39;)
  .then(res =&gt; {
    // 여기서 res.body는 브라우저 기본 Blob 타입입니다.
  });
</code></pre>
      <p>
        더 자세한 내용은 Mozilla Developer Network의
        <a
          href="https://developer.mozilla.org/en-US/../Web/API/XMLHttpRequest/responseType"
          >XMLHttpRequest.responseType 문서</a
        >에서 확인할 수 있습니다.
      </p>
      <h2 id="response-properties">응답 속성</h2>
      <p>
        <code>Response</code> 객체에는 응답 텍스트, 파싱된 응답 본문, 헤더 필드,
        상태 플래그 등 다양한 유용한 플래그와 속성이 설정되어 있습니다.
      </p>
      <h3 id="response-text">응답 문자</h3>
      <p>
        <code>res.text</code> 속성에는 파싱되지 않은 응답 본문 문자열이
        포함됩니다. 이 속성은 클라이언트 API에서는 항상 존재하며, Node
        환경에서는 MIME 타입이 &quot;text/<em>&quot;, &quot;</em>/json&quot;,
        또는 &quot;x-www-form-urlencoded&quot;와 일치할 경우에만 기본적으로
        제공됩니다. 이러한 제한은 대용량 multipart 파일이나 이미지 등의 본문을
        텍스트로 버퍼링하는 것이 매우 비효율적이기 때문에 메모리를 절약하기 위한
        목적입니다. 응답을 강제로 버퍼링하려면 &quot;응답 버퍼링&quot; 섹션을
        참조하세요.
      </p>
      <h3 id="response-body">응답 본문</h3>
      <p>
        SuperAgent는 요청 데이터를 자동으로 직렬화할 뿐만 아니라, 자동으로
        파싱할 수도 있습니다. Content-Type에 대해 파서가 정의되어 있는 경우,
        해당 타입에 맞게 응답이 파싱되며 기본적으로
        &quot;application/json&quot;과
        &quot;application/x-www-form-urlencoded&quot; 형식이 포함됩니다. 파싱된
        객체는 <code>res.body</code>를 통해 접근할 수 있습니다.
      </p>
      <h3 id="response-header-fields">응답 헤더 필드</h3>
      <p>
        <code>res.header</code>는 파싱된 응답 헤더 필드를 담은 객체로, Node.js와
        마찬가지로 필드 이름을 소문자로 변환하여 저장합니다. 예를 들어,
        <code>res.header[&#39;content-length&#39;]</code>와 같이 접근할 수
        있습니다.
      </p>
      <h3 id="response-content-type">응답 콘텐츠 타입</h3>
      <p>
        Content-Type 응답 헤더는 특별하게 처리되어 <code>res.type</code> 속성은
        charset 정보를 제외한 콘텐츠 타입만을 제공합니다. 예를 들어
        Content-Type이 &quot;text/html; charset=utf8&quot;인 경우,
        <code>res.type</code>은 &quot;text/html&quot;을 반환하고,
        <code>res.charset</code> 속성에는 &quot;utf8&quot;이 포함됩니다.
      </p>
      <h3 id="response-status">응답 상태</h3>
      <p>
        응답 상태 플래그는 요청이 성공했는지 여부를 비롯한 다양한 유용한 정보를
        판단하는 데 도움을 줍니다. 이를 통해 SuperAgent는 RESTful 웹 서비스와
        효과적으로 상호작용할 수 있습니다. 현재 정의된 주요 플래그는 다음과
        같습니다.
      </p>
      <pre><code class="language-javascript">     var type = status / 100 | 0;

     // 상태 / 클래스
     res.status = status;
     res.statusType = type;

     // 기본
     res.info = 1 == type;
     res.ok = 2 == type;
     res.clientError = 4 == type;
     res.serverError = 5 == type;
     res.error = 4 == type || 5 == type;

     // 편의 기능
     res.accepted = 202 == status;
     res.noContent = 204 == status || 1223 == status;
     res.badRequest = 400 == status;
     res.unauthorized = 401 == status;
     res.notAcceptable = 406 == status;
     res.notFound = 404 == status;
     res.forbidden = 403 == status;
</code></pre>
      <h2 id="aborting-requests">요청 중단하기</h2>
      <p>
        요청을 중단하려면 <code>req.abort()</code> 메서드를 호출하기만 하면
        됩니다.
      </p>
      <h2 id="timeouts">타임아웃</h2>
      <p>
        때때로 네트워크나 서버가 요청을 수신한 후 응답 없이 멈춰버리는 경우가
        있습니다. 이러한 무한 대기를 방지하려면 타임아웃을 설정해야 합니다.
      </p>
      <ul>
        <li>
          <p>
            <code>req.timeout({deadline:ms})</code> 또는
            <code>req.timeout(ms)</code>는 업로드, 리다이렉트, 서버 처리 시간을
            포함한 전체 요청이 완료되어야 하는 최종 시간 제한을 설정합니다.
            <code>ms</code>는 0보다 큰 밀리초 단위의 숫자이며, 제한 시간 내에
            응답이 완료되지 않으면 요청은 중단됩니다.
          </p>
        </li>
        <li>
          <p>
            <code>req.timeout({response:ms})</code>는 서버로부터 첫 번째
            바이트가 도착할 때까지의 최대 대기 시간을 설정합니다. 전체 다운로드
            소요 시간은 제한하지 않습니다. 응답 타임아웃은 DNS 조회, TCP/IP 및
            TLS 연결, 요청 데이터 업로드 시간을 포함하므로, 서버의 실제 응답
            시간보다 몇 초 더 길게 설정하는 것이 좋습니다.
          </p>
        </li>
      </ul>
      <p>
        <code>deadline</code>과 <code>response</code> 타임아웃은 함께 사용하는
        것이 좋습니다. 짧은 응답 타임아웃은 응답하지 않는 네트워크를 빠르게
        감지하는 데 유용하고, 긴 데드라인은 느리지만 안정적인 네트워크 환경에서
        다운로드를 완료할 수 있도록 여유 시간을 제공합니다. 두 타이머 모두
        첨부된 파일 업로드에 허용되는 시간을 제한합니다. 파일을 업로드하는
        경우에는 충분히 긴 타임아웃을 설정하는 것이 좋습니다.
      </p>
      <pre><code class="language-javascript">    request
      .get(&#39;/big-file?network=slow&#39;)
      .timeout({
        response: 5000,  // 서버가 데이터를 보내기 시작할 때까지 최대 5초간 기다립니다.
        deadline: 60000, // 파일 전체를 로드하는 데 최대 1분까지 허용합니다.
      })
      .then(res =&gt; {
          /* 제시간 응답 수신 */
        }, err =&gt; {
          if (err.timeout) { /* 시간 초과! */ } else { /* 그 외 오류 */ }
      });
</code></pre>
      <p>타임아웃 오류에는 <code>.timeout</code> 속성이 포함되어 있습니다.</p>
      <h2 id="authentication">인증</h2>
      <p>
        Node와 브라우저 환경에서 <code>.auth()</code> 메서드를 사용하여 인증을
        수행할 수 있습니다.
      </p>
      <pre><code class="language-javascript">    request
      .get(&#39;http://local&#39;)
      .auth(&#39;tobi&#39;, &#39;learnboost&#39;)
      .then(callback);
</code></pre>
      <p>
        <em>Node</em> 클라이언트에서는 기본 인증을 URL 내에
        &quot;user:pass&quot; 형식으로 포함시킬 수 있습니다.
      </p>
      <pre><code class="language-javascript">    request.get(&#39;http://tobi:learnboost@local&#39;).then(callback);
</code></pre>
      <p>
        기본적으로 <code>Basic</code> 인증만 사용됩니다. 브라우저에서는
        <code>{type:&#39;auto&#39;}</code>를 추가하면 Digest, NTLM 등 브라우저에
        내장된 모든 인증 방식을 사용할 수 있습니다.
      </p>
      <pre><code class="language-javascript">    request.auth(&#39;digest&#39;, &#39;secret&#39;, {type:&#39;auto&#39;})
</code></pre>
      <p>
        <code>auth</code> 메서드는 토큰 기반 인증을 위한 <code>type</code>의
        <code>bearer</code> 옵션도 지원합니다.
      </p>
      <pre><code class="language-javascript">    request.auth(&#39;my_token&#39;, { type: &#39;bearer&#39; })
</code></pre>
      <h2 id="following-redirects">다음 리다이렉션 따라가기</h2>
      <p>
        기본적으로 최대 5번까지 리다이렉션이 자동으로 따라가며, 필요에 따라
        <code>res.redirects(n)</code> 메서드를 사용하여 이 횟수를 지정할 수
        있습니다.
      </p>
      <pre><code class="language-javascript">    const response = await request.get(&#39;/some.png&#39;).redirects(2);
</code></pre>
      <p>
        리다이렉션 횟수가 제한을 초과하면 오류로 간주됩니다. 이를 성공적인
        응답으로 처리하려면
        <code>.ok(res =&gt; res.status &lt; 400)</code> 메서드를 사용하세요.
      </p>
      <h2 id="agents-for-global-state">전역 상태를 위한 에이전트</h2>
      <h3 id="saving-cookies">쿠키 저장하기</h3>
      <p>
        Node에서 SuperAgent는 기본적으로 쿠키를 저장하지 않습니다. 하지만
        <code>.agent()</code> 메서드를 사용하면 쿠키를 저장하는 SuperAgent
        인스턴스를 생성할 수 있습니다. 각 인스턴스는 독립적인 쿠키 저장소를
        가지고 있습니다.
      </p>
      <pre><code class="language-javascript">    const agent = request.agent();
    agent
      .post(&#39;/login&#39;)
      .then(() =&gt; {
        return agent.get(&#39;/cookied-page&#39;);
      });
</code></pre>
      <p>
        브라우저에서는 쿠키가 자동으로 관리되므로
        <code>.agent()</code>를 사용해도 쿠키가 분리되지는 않습니다.
      </p>
      <h3 id="default-options-for-multiple-requests">
        다중 요청을 위한 기본 옵션
      </h3>
      <p>
        에이전트에서 호출된 일반 요청 메서드는 해당 에이전트가 처리하는 모든
        요청에 대해 기본값으로 적용됩니다.
      </p>
      <pre><code class="language-javascript">    const agent = request.agent()
      .use(plugin)
      .auth(shared);

    await agent.get(&#39;/with-plugin-and-auth&#39;);
    await agent.get(&#39;/also-with-plugin-and-auth&#39;);
</code></pre>
      <p>
        에이전트가 기본 옵션을 설정할 수 있도록 지원하는 메서드 목록입니다.
        <code>use</code>, <code>on</code>, <code>once</code>, <code>set</code>,
        <code>query</code>, <code>type</code>, <code>accept</code>,
        <code>auth</code>, <code>withCredentials</code>, <code>sortQuery</code>,
        <code>retry</code>, <code>ok</code>, <code>redirects</code>,
        <code>timeout</code>, <code>buffer</code>, <code>serialize</code>,
        <code>parse</code>, <code>ca</code>, <code>key</code>, <code>pfx</code>,
        <code>cert</code>.
      </p>
      <h2 id="piping-data">데이터 전달 방식</h2>
      <p>
        <code>.pipe()</code>는 <code>.end()</code> 또는
        <code>.then()</code> 메서드 <strong>대신</strong> 사용되며, Node
        클라이언트는 요청과 응답 간에 데이터를 주고받도록 파이프 처리할 수
        있습니다.
      </p>
      <p>
        예를 들어, 파일의 콘텐츠를 요청 본문으로 전달하는 경우는 다음과
        같습니다.
      </p>
      <pre><code class="language-javascript">    const request = require(&#39;superagent&#39;);
    const fs = require(&#39;fs&#39;);

    const stream = fs.createReadStream(&#39;path/to/my.json&#39;);
    const req = request.post(&#39;/somewhere&#39;);
    req.type(&#39;json&#39;);
    stream.pipe(req);
</code></pre>
      <p>
        요청에 데이터를 파이프할 경우, SuperAgent는 해당 데이터를
        <a href="https://en.wikipedia.org/wiki/Chunked_transfer_encoding"
          >청크 전송 인코딩</a
        >
        방식으로 전송합니다. 이 방식은 Python WSGI 서버 등 모든 서버에서
        지원되지는 않습니다.
      </p>
      <p>응답을 파일로 저장하려면 다음과 같이 파이프 처리할 수 있습니다.</p>
      <pre><code class="language-javascript">    const stream = fs.createWriteStream(&#39;path/to/my.json&#39;);
    const req = request.get(&#39;/some.json&#39;);
    req.pipe(stream);
</code></pre>
      <p>
        파이프와 콜백 또는 프로미스는 <strong>함께 사용할 수 없으며</strong>,
        <code>.end()</code>나 <code>Response</code> 객체의 결과를 파이프
        처리해서는 안 됩니다.
      </p>
      <pre><code class="language-javascript">    // 이러한 방식으로 하지 마세요.
    const stream = getAWritableStream();
    const req = request
      .get(&#39;/some.json&#39;)
      // 나쁨: 이 방식은 스트림에 올바르지 않은 데이터를 전달하며 예기치 못한 방식으로 실패할 수 있습니다.
      .end((err, this_does_not_work) =&gt; this_does_not_work.pipe(stream))
    const req = request
      .get(&#39;/some.json&#39;)
      .end()
      // 나쁨: 이 방식도 지원되지 않으며, .pipe는 자동으로 .end를 호출합니다.
      .pipe(nope_its_too_late);
</code></pre>
      <p>
        SuperAgent의
        <a href="https://github.com/ladjs/superagent/issues/1188">향후 버전</a
        >에서는 <code>pipe()</code>를 부적절하게 호출하면 실패하게 됩니다.
      </p>
      <h2 id="multipart-requests">다중 부분 요청</h2>
      <p>
        <code>.attach()</code>와 <code>.field()</code> 메서드를 제공하는
        SuperAgent는 다중 부분 요청을 구성하는 데에도 매우 유용합니다.
      </p>
      <p>
        <code>.field()</code> 또는 <code>.attach()</code>를 사용할 경우
        <code>.send()</code>는 사용할 수 없으며,
        <code>Content-Type</code> 헤더를 직접 설정해서는 안 됩니다. 올바른
        타입은 자동으로 지정됩니다.
      </p>
      <h3 id="attaching-files">파일 첨부하기</h3>
      <p>
        <code>.attach(name, [file], [options])</code>를 사용하여 파일을 전송할
        수 있습니다. 여러 파일을 첨부하려면 <code>.attach</code>를 반복 호출하면
        됩니다. 인자는 다음과 같습니다.
      </p>
      <ul>
        <li><code>name</code> — 폼 이름 필드.</li>
        <li>
          <code>file</code> — 파일 경로의 문자열 또는 <code>Blob</code>/<code
            >Buffer</code
          >
          객체.
        </li>
        <li>
          <code>options</code> — (선택) 사용자 정의 파일 이름의 문자열 또는
          <code>{filename: string}</code> 형식의 객체. In Node also
          <code>{contentType: &#39;mime/type&#39;}</code> is supported. In
          browser create a <code>Blob</code> with an appropriate type instead.
        </li>
      </ul>
      <br />

      <pre><code class="language-javascript">    request
      .post(&#39;/upload&#39;)
      .attach(&#39;image1&#39;, &#39;path/to/felix.jpeg&#39;)
      .attach(&#39;image2&#39;, imageBuffer, &#39;luna.jpeg&#39;)
      .field(&#39;caption&#39;, &#39;My cats&#39;)
      .then(callback);
</code></pre>
      <h3 id="field-values">필드 값</h3>
      <p>
        <code>.field(name, value)</code> 및 <code>.field({name: value})</code>를
        사용해 HTML 폼 필드처럼 값을 설정할 수 있습니다. 예를 들어 이름과 이메일
        정보를 함께 여러 이미지를 업로드하려면, 요청은 다음과 같이 구성될 수
        있습니다.
      </p>
      <pre><code class="language-javascript">     request
       .post(&#39;/upload&#39;)
       .field(&#39;user[name]&#39;, &#39;Tobi&#39;)
       .field(&#39;user[email]&#39;, &#39;tobi@learnboost.com&#39;)
       .field(&#39;friends[]&#39;, [&#39;loki&#39;, &#39;jane&#39;])
       .attach(&#39;image&#39;, &#39;path/to/tobi.png&#39;)
       .then(callback);
</code></pre>
      <h2 id="compression">압축</h2>
      <p>
        node 클라이언트는 압축된 응답을 지원하며, 아무 것도 하지 않아도 됩니다!
        그냥 작동합니다.
      </p>
      <h2 id="buffering-responses">응답 버퍼링</h2>
      <p>
        <code>.req.buffer()</code>를 호출하면 응답 본문을
        <code>res.text</code>로 강제 버퍼링할 수 있습니다.
        &quot;text/plain&quot;, &quot;text/html&quot; 등 텍스트 응답의 기본
        버퍼링을 취소하려면 <code>req.buffer(false)</code>를 호출하세요.
      </p>
      <p>
        <code>res.buffered</code> 플래그가 제공되면, 이를 활용하여 동일한 콜백
        함수에서 버퍼링된 응답과 버퍼링되지 않은 응답을 모두 처리할 수 있습니다.
      </p>
      <h2 id="cors">CORS</h2>
      <p>
        보안상의 이유로 브라우저는 서버가 CORS 헤더를 통해 명시적으로 허용하지
        않으면 교차 출처 요청(cross-origin requests)을 차단합니다. 브라우저는
        또한 서버가 어떤 HTTP 헤더와 메서드를 허용하는지 확인하기 위해 추가적인
        <strong>OPTIONS</strong> 요청을 전송합니다.
        <a
          href="https://developer.mozilla.org/ko/../Web/HTTP/Access_control_CORS"
          >CORS에 대해 더 알아보기</a
        >.
      </p>
      <p>
        <code>.withCredentials()</code> 메서드는 origin(출처)에서 쿠키를 전송할
        수 있도록 활성화합니다. 단, 이 기능은
        <code>Access-Control-Allow-Origin</code> 값이
        와일드카드(&quot;*&quot;)가 <em>아니어야</em> 하며,
        <code>Access-Control-Allow-Credentials</code> 값이 &quot;true&quot;일
        경우에만 작동합니다.
      </p>
      <pre><code class="language-javascript">    request
      .get(&#39;https://api.example.com:4001/&#39;)
      .withCredentials()
      .then(res =&gt; {
        assert.equal(200, res.status);
        assert.equal(&#39;tobi&#39;, res.text);
      })
</code></pre>
      <h2 id="error-handling">오류 처리하기</h2>
      <p>
        콜백 함수는 항상 두 개의 인자를 전달합니다. 오류와 응답입니다. 오류가
        발생하지 않으면, 첫 번째 인자는 null 입니다.
      </p>
      <pre><code class="language-javascript">    request
     .post(&#39;/upload&#39;)
     .attach(&#39;image&#39;, &#39;path/to/tobi.png&#39;)
     .then(res =&gt; {

     });
</code></pre>
      <p>
        "error" 이벤트도 발생하며, 이를 통해 오류를 감지하고 처리할 수 있습니다.
      </p>
      <pre><code class="language-javascript">    request
      .post(&#39;/upload&#39;)
      .attach(&#39;image&#39;, &#39;path/to/tobi.png&#39;)
      .on(&#39;error&#39;, handle)
      .then(res =&gt; {

      });
</code></pre>
      <p>
        <strong
          >SuperAgent는 기본적으로 4xx 및 5xx 응답(그리고 처리되지 않은 3xx
          응답도 포함)을 오류</strong
        >로 간주합니다. 예를 들어 <code>304 Not Modified</code>,
        <code>403 Forbidden</code> 또는
        <code>500 Internal Server Error</code> 같은 응답을 받으면 해당 상태
        정보는 <code>err.status</code>를 통해 확인할 수 있습니다. 이러한
        응답으로부터 발생한 오류에는 &quot;<a href="#response-properties"
          >응답 요소</a
        >&quot;에서 언급한 모든 속성을 포함한 <code>err.response</code> 필드도
        포함됩니다. 이 라이브러리는 일반적으로 성공 응답만을 원하고, HTTP 오류
        상태 코드를 오류로 처리하는 경우를 대비하여 이러한 방식으로 동작합니다.
        하지만 특정 오류 조건에 대해서는 사용자 정의 로직을 허용하도록 설계되어
        있습니다.
      </p>
      <p>
        네트워크 실패, 시간초과, 응답 없는 오류는 <code>err.status</code> 또는
        <code>err.response</code> 필드를 포함하지 않습니다.
      </p>
      <p>
        404 또는 HTTP 오류 응답을 처리하고 싶다면,
        <code>error.status</code> 요소를 사용할 수 있습니다. HTTP 오류(4xx 또는
        5xx 응답)가 발생했을 때 <code>res.error</code> 요소는
        <code>Error</code> 객체이고 이는 다음과 같이 에러 확인을 수행할 수
        있습니다.
      </p>
      <pre><code class="language-javascript">    if (err &amp;&amp; err.status === 404) {
      alert(&#39;oh no &#39; + res.body.message);
    }
    else if (err) {
      // 그 외 다른 모든 오류 유형은 일반적으로 처리합니다
    }
</code></pre>
      <p>
        대안으로, <code>.ok(callback)</code> 메서드를 사용하여 응답이 오류인지
        아닌지 결정할 수 있습니다. <code>ok</code> 콜백은 응답을 받고 응답이
        성공으로 해석되면 <code>true</code>를 반환합니다.
      </p>
      <pre><code class="language-javascript">    request.get(&#39;/404&#39;)
      .ok(res =&gt; res.status &lt; 500)
      .then(response =&gt; {
        // 404 페이지를 성공적인 응답으로 처리합니다
      })
</code></pre>
      <h2 id="progress-tracking">진행과정 추적하기</h2>
      <p>
        SuperAgent는 업로드와 큰 파일 다운로드에서
        <code>progress</code> 이벤트를 동작시킵니다.
      </p>
      <pre><code class="language-javascript">    request.post(url)
      .attach(&#39;field_name&#39;, file)
      .on(&#39;progress&#39;, event =&gt; {
        /* the event is:
        {
          direction: &quot;upload&quot; or &quot;download&quot;
          percent: 0 to 100 // 0에서 100까지 (파일 크기를 알 수 없는 경우 생략될 수 있습니다)
          total: // 전체 파일 크기 (생략될 수 있습니다)
          loaded: // 현재까지 다운로드되거나 업로드된 바이트 수
        } */
      })
      .then()
</code></pre>
      <h2 id="testing-on-localhost">로컬 호스트에서 테스트하기</h2>
      <h3 id="forcing-specific-connection-ip-address">
        특정 IP 주소 연결 설정하기
      </h3>
      <p>
        Node.js에서는 DNS를 무시하고 <code>.connect()</code> 메서드를 사용하여
        모든 요청을 특정 IP 주소로 직접 연결할 수 있습니다. 예를 들어, 이 요청은
        <code>example.com</code> 대신 로컬호스트로 전달됩니다.
      </p>
      <pre><code class="language-javascript">    const res = await request.get(&quot;http://example.com&quot;).connect(&quot;127.0.0.1&quot;);
</code></pre>
      <p>
        요청은 리다이렉트 되어, 여러 호스트명과 IP를 특정지을 수 있으며 특별한
        <code>*</code>를 대체로 설정할 수 있습니다. (다른 와일드 카드는 지원되지
        않습니다). 요청은 원본 값을 가지며 본인의 <code>Host</code> 헤더를
        유지합니다. <code>.connect(undefined)</code>는 이러한 기능을 끕니다.
      </p>
      <pre><code class="language-javascript">    const res = await request.get(&quot;http://redir.example.com:555&quot;)
      .connect({
        &quot;redir.example.com&quot;: &quot;127.0.0.1&quot;, // redir.example.com:555는 127.0.0.1:555를 사용합니다.
        &quot;www.example.com&quot;: false, // 이 항목은 재정의하지 마세요. 일반적인 DNS 설정을 사용합니다.
        &quot;mapped.example.com&quot;: { host: &quot;127.0.0.1&quot;, port: 8080}, // mapped.example.com의 모든 포트는 127.0.0.1:8080으로 매핑됩니다.
        &quot;*&quot;: &quot;proxy.example.com&quot;, // 나머지 모든 요청은 이 호스트로 전달됩니다
      });
</code></pre>
      <h3 id="ignoring-brokeninsecure-https-on-localhost">
        로컬 호스트에서 깨지거나 보안되지 않은 HTTPS 무시하기
      </h3>
      <p>
        Node.js에서 HTTPS 설정이 잘못되었거나 보안성이 떨어지는 경우(예: 자체
        서명된 인증서를 사용하면서
        <code>.ca()</code>를 지정하지 않은 경우),
        <code>.trustLocalhost()</code>를 호출하면 <code>localhost</code>로의
        요청을 허용할 수 있습니다.
      </p>
      <pre><code class="language-javascript">    const res = await request.get(&quot;https://localhost&quot;).trustLocalhost()
</code></pre>
      <p>
        <code>.connect(&quot;127.0.0.1&quot;)</code>와 함께 사용하면 HTTPS
        요청을 어떤 도메인에서든 <code>localhost</code>로 강제로 리다이렉트할 수
        있습니다.
      </p>
      <p>
        <code>localhost</code>는 신뢰되지 않은 네트워크에 노출되지 않는 루프백
        인터페이스이기 때문에, 깨진 HTTPS를 무시하는 것이 일반적으로 안전합니다.
        <code>localhost</code>를 신뢰하도록 설정하는 것이 향후 기본값이 될 수
        있습니다. <code>127.0.0.1</code>&#39;의 진위 여부를 강제로 검사하려면
        <code>.trustLocalhost(false)</code>를 사용하세요.
      </p>
      <p>
        다른 IP 주소로 요청을 보낼 때 HTTPS 보안을 비활성화하는 기능은
        의도적으로 지원하지 않습니다. 이러한 옵션은 HTTPS 문제를 빠르게
        &quot;해결&quot;하려는 방식으로 오용되는 경우가 많기 때문입니다.
        <a href="https://certbot.eff.org">Let&#39;s Encrypt</a>를 통해 무료
        HTTPS 인증서를 발급하거나, <code>.ca(ca_public_pem)</code>을 사용해 자체
        서명된 인증서를 신뢰할 수 있도록 직접 CA를 설정할 수 있습니다.
      </p>
      <h2 id="promise-and-generator-support">Promise 및 Generator 지원</h2>
      <p>
        SuperAgent의 요청은 &quot;thenable&quot; 객체이며, JavaScript의 Promise
        및 <code>async</code>/<code>await</code>
        문법과 호환됩니다.
      </p>
      <pre><code class="language-javascript">    const res = await request.get(url);
</code></pre>
      <p>
        Promise를 사용할 경우,
        <strong
          ><code>.end()</code> 또는 <code>.pipe()</code>를 호출하지
          마세요</strong
        >. <code>.then()</code> 또는 <code>await</code>를 사용하면 요청을 처리할
        수 있는 다른 방식들이 모두 비활성화됩니다.
      </p>
      <p>
        <a href="https://github.com/tj/co">co</a>와 같은 라이브러리나
        <a href="https://github.com/koajs/koa">koa</a>와 같은 웹
        프레임워크에서는 SuperAgent의 모든 메서드에서 <code>yield</code>를
        사용할 수 있습니다.
      </p>
      <pre><code class="language-javascript">    const req = request
      .get(&#39;http://local&#39;)
      .auth(&#39;tobi&#39;, &#39;learnboost&#39;);
    const res = yield req;
</code></pre>
      <p>
        SuperAgent는 전역 <code>Promise</code> 객체가 존재하는 환경에서
        동작하도록 설계되어 있습니다. Internet Explorer나 Node.js 0.10에서
        promise를 사용하려면 v7 버전과 폴리필이 필요합니다.
      </p>
      <p>
        v8 버전부터는 IE에 대한 지원이 중단되었습니다. Opera 85나 iOS Safari
        12.2–12.5 등을 지원하려면 WeakRef와 BigInt에 대한 폴리필을 추가해야
        합니다. 예를 들어
        <a href="https://cdnjs.cloudflare.com/polyfill/"
          >https://cdnjs.cloudflare.com/polyfill/</a
        >을 사용할 수 있습니다.
      </p>
      <pre><code class="language-html">&lt;script src=&quot;https://cdnjs.cloudflare.com/polyfill/v3/polyfill.min.js?features=WeakRef,BigInt&quot;&gt;&lt;/script&gt;
</code></pre>
      <h2 id="browser-and-node-versions">브라우저와 node 버전</h2>
      <p>
        SuperAgent에는 두 가지 구현 방식이 있습니다. 하나는 웹 브라우저용(XHR
        사용)이고, 다른 하나는 Node.JS용(core http 모듈 사용)입니다. 기본적으로
        Browserify와 WebPack은 브라우저 버전을 선택합니다.
      </p>
      <p>
        Node.JS용 코드를 컴파일하려면 WebPack 설정에서 반드시
        <a href="https://webpack.github.io/../configuration.html#target"
          >node target</a
        >
        을 지정해야 합니다.
      </p>
    </div>
    <a href="http://github.com/ladjs/superagent"
      ><img
        style="position: absolute; top: 0; right: 0; border: 0"
        src="https://s3.amazonaws.com/github/ribbons/forkme_right_white_ffffff.png"
        alt="Fork me on GitHub"
    /></a>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.0/jquery.min.js"></script>
    <script>
      $('code').each(function () {
        $(this).html(highlight($(this).text()));
      });

      function highlight(js) {
        return js
          .replace(/</g, '&lt;')
          .replace(/>/g, '&gt;')
          .replace(/('.*?')/gm, '<span class="string">$1</span>')
          .replace(/(\d+\.\d+)/gm, '<span class="number">$1</span>')
          .replace(/(\d+)/gm, '<span class="number">$1</span>')
          .replace(
            /\bnew *(\w+)/gm,
            '<span class="keyword">new</span> <span class="init">$1</span>'
          )
          .replace(
            /\b(function|new|throw|return|var|if|else)\b/gm,
            '<span class="keyword">$1</span>'
          );
      }
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/tocbot/3.0.0/tocbot.js"></script>
    <script>
      // Only use tocbot for main docs, not test docs
      if (document.querySelector('#superagent')) {
        tocbot.init({
          // Where to render the table of contents.
          tocSelector: '#menu',
          // Where to grab the headings to build the table of contents.
          contentSelector: '#content',
          // Which headings to grab inside of the contentSelector element.
          headingSelector: 'h2',
          smoothScroll: false
        });
      }
    </script>
  </body>
</html>
```

## File: `docs/ko_KR/index.md`
```markdown
# SuperAgent

SuperAgent는 기존의 복잡한 요청 API에 대한 불만에서 출발해 유연성, 가독성, 그리고 낮은 학습 난이도를 목표로 설계된 경량 Ajax API입니다. 또한 Node.js 환경에서도 동작합니다!

```javascript
request
  .post('/api/pet')
  .send({ name: 'Manny', species: 'cat' })
  .set('X-API-Key', 'foobar')
  .set('Accept', 'application/json')
  .then((res) => {
    alert('yay got ' + JSON.stringify(res.body));
  });
```

## 테스트 문서

[**English**](/superagent/)

다음의 [테스트 문서](../test.html)는 [Mocha](https://mochajs.org/)의 "doc" 리포터를 사용해 생성되었으며, 실제 테스트 스위트를 직접 반영합니다.  
이 문서는 추가적인 참고 자료로 활용할 수 있습니다.

## 기본 요청

요청은 `request` 객체에서 적절한 메서드를 호출하여 시작되며, 그 다음 `.then()` 또는 `.end()` 혹은 [`await`](#promise-and-generator-support)를 사용해 요청을 전송할 수 있습니다. 예를 들어, 간단한 **GET** 요청은 다음과 같습니다.

```javascript
request
  .get('/search')
  .then((res) => {
    // res.body, res.headers, res.status
  })
  .catch((err) => {
    // err.message, err.response
  });
```

HTTP 메서드는 문자열로도 전달할 수 있습니다.

```javascript
request('GET', '/search').then(success, failure);
```

예전 방식의 콜백도 지원되지만, 권장되지는 않습니다. `.then()` 대신 `.end()`를 호출하여 요청을 전송할 수 있습니다.

```javascript
request('GET', '/search').end(function (err, res) {
  if (res.ok) {
  }
});
```

절대 URL을 사용할 수 있습니다. 단, 웹 브라우저에서는 서버가 [CORS](#cors)를 구현한 경우에만 절대 URL이 정상적으로 작동합니다.

```javascript
request.get('https://example.com/search').then((res) => {});
```

**Node** 클라이언트는 [유닉스 도메인 소켓](https://ko.wikipedia.org/wiki/%EC%9C%A0%EB%8B%89%EC%8A%A4_%EB%8F%84%EB%A9%94%EC%9D%B8_%EC%86%8C%EC%BC%93)을 통한 요청을 지원합니다.

```javascript
// pattern: https?+unix://SOCKET_PATH/REQUEST_PATH
//          Use `%2F` as `/` in SOCKET_PATH
try {
  const res = await request.get(
    'http+unix://%2Fabsolute%2Fpath%2Fto%2Funix.sock/search'
  );
  // res.body, res.headers, res.status
} catch (err) {
  // err.message, err.response
}
```

**DELETE**, **HEAD**, **PATCH**, **POST**, **PUT** 요청도 사용할 수 있으며, 다음 예시에서 메서드 이름만 변경하면 됩니다.

```javascript
request.head('/favicon.ico').then((res) => {});
```

**DELETE**는 `delete`가 예약어였던 구형 IE와의 호환성을 위해 `.del()` 메서드로도 호출할 수 있습니다.

HTTP 메서드의 기본값은 **GET**이므로, 다음과 같이 작성해도 유효합니다.

```javascript
request('/search', (err, res) => {});
```

## HTTP/2 사용하기

HTTP/1.x 폴백 없이 HTTP/2 프로토콜만 사용하려면 `.http2()` 메서드를 호출하여 요청을 전송할 수 있습니다.

```javascript
const request = require('superagent');
const res = await request.get('https://example.com/h2').http2();
```

## 헤더 필드 설정하기

헤더 필드 설정은 간단합니다. 필드 이름과 값을 `.set()` 메서드에 전달하면 됩니다.

```javascript
request
  .get('/search')
  .set('API-Key', 'foobar')
  .set('Accept', 'application/json')
  .then(callback);
```

You may also pass an object to set several fields in a single call:

여러 개의 헤더 필드를 한 번에 설정하려면 객체를 전달하면 됩니다.

```javascript
request
  .get('/search')
  .set({ 'API-Key': 'foobar', Accept: 'application/json' })
  .then(callback);
```

## `GET` 요청

`.query()` 메서드는 객체를 인자로 받아 **GET** 요청 시 쿼리 문자열을 자동으로 생성합니다. 예를 들어 다음 코드는 `/search?query=Manny&range=1..5&order=desc` 경로를 생성합니다.

````js
request
  .get('/search')
  .query({ query: 'Manny', range: '1..5', order: 'desc' });


```javascript
request
  .get('/search')
  .query({ query: 'Manny' })
  .query({ range: '1..5' })
  .query({ order: 'desc' })
  .then((res) => {});
````

또는 하나의 객체로 설정할 수 있습니다.

```javascript
request
  .get('/search')
  .query({ query: 'Manny', range: '1..5', order: 'desc' })
  .then((res) => {});
```

`.query()` 메서드는 문자열도 받습니다.

```javascript
request
  .get('/querystring')
  .query('search=Manny&range=1..5')
  .then((res) => {});
```

조인할 수도 있습니다.

```javascript
request
  .get('/querystring')
  .query('search=Manny')
  .query('range=1..5')
  .then((res) => {});
```

## `HEAD` 요청하기

HEAD 요청에서도 `.query()` 메서드를 사용할 수 있습니다. 예를 들어 다음 코드는 `/users?email=joe@smith.com` 경로를 생성합니다.

```javascript
request
  .head('/users')
  .query({ email: 'joe@smith.com' })
  .then((res) => {});
```

## `POST` / `PUT` 요청

전형적인 JSON **POST** 요청은 Content-Type 헤더를 적절히 설정하고,  
데이터를 JSON 형식으로 전송하는 방식입니다. 예를 들어 다음과 같은 코드가 이에 해당합니다.

```javascript
request
  .post('/user')
  .set('Content-Type', 'application/json')
  .send('{"name":"tj","pet":"tobi"}')
  .then(callback)
  .catch(errorCallback);
```

JSON은 가장 일반적으로 사용되므로 기본값으로 설정되어 있습니다. 다음 예제는 앞선 예제와 동일한 동작을 수행합니다.

```javascript
request
  .post('/user')
  .send({ name: 'tj', pet: 'tobi' })
  .then(callback, errorCallback);
```

또는 `.send()` 여러 번 호출할 수 있습니다.

```javascript
request
  .post('/user')
  .send({ name: 'tj' })
  .send({ pet: 'tobi' })
  .then(callback, errorCallback);
```

기본적으로 문자열을 전송하면 `Content-Type`이 `application/x-www-form-urlencoded`로 자동 설정됩니다.  
여러 번 `.send()`를 호출하면 각 문자열이 `&`로 연결되어 최종적으로 `name=tj&pet=tobi`와 같은 결과가 생성됩니다.

```javascript
request
  .post('/user')
  .send('name=tj')
  .send('pet=tobi')
  .then(callback, errorCallback);
```

SuperAgent는 다양한 형식으로 확장 가능하지만, 기본적으로 "json"과 "form" 형식을 지원합니다. `application/x-www-form-urlencoded` 형식으로 데이터를 전송하려면 `.type('form')`을 호출하면 됩니다. 기본 형식은 `"json"`입니다. 다음 요청은 본문에 `"name=tj&pet=tobi"`를 포함하여 **POST**됩니다.

```javascript
request
  .post('/user')
  .type('form')
  .send({ name: 'tj' })
  .send({ pet: 'tobi' })
  .then(callback, errorCallback);
```

[`FormData`](https://developer.mozilla.org/ko/docs/Web/API/FormData/FormData) 객체를 사용하는 것도 지원됩니다. 다음 예제는 `id="myForm"`인 HTML 폼의 내용을 **POST** 방식으로 전송합니다.

```javascript
request
  .post('/user')
  .send(new FormData(document.getElementById('myForm')))
  .then(callback, errorCallback);
```

## `Content-Type` 설정하기

가장 명확한 해결책은 `.set()` 메서드를 사용하는 것입니다.

```javascript
request.post('/user').set('Content-Type', 'application/json');
```

간단하게 `.type()` 메서드를 사용할 수 있으며,  
표준화된 MIME 타입(`type/subtype`)을 직접 지정하거나  
"xml", "json", "png" 등과 같은 확장자 이름만으로도 설정할 수 있습니다.

```javascript
request.post('/user').type('application/json');

request.post('/user').type('json');

request.post('/user').type('png');
```

## 요청 본문 직렬화하기

SuperAgent는 기본적으로 JSON과 폼 데이터를 자동으로 직렬화합니다.  
또한 다른 콘텐츠 유형에 대해서도 자동 직렬화를 설정할 수 있습니다.

```js
request.serialize['application/xml'] = function (obj) {
  return 'string generated from obj';
};

// 'application/xml' Content-type을 가진 모든 요청은
// 자동으로 직렬화 됩니다.
```

사용자 정의 형식으로 페이로드를 전송하려면,  
요청 단위로 `.serialize()` 메서드를 사용해 SuperAgent의 기본 직렬화 방식을 교체할 수 있습니다.

```js
request
  .post('/user')
  .send({ foo: 'bar' })
  .serialize((obj) => {
    return 'string generated from obj';
  });
```

## 요청 재시도하기

`.retry()` 메서드를 사용하면, 일시적인 오류나 불안정한 인터넷 연결로 인해 요청이 실패한 경우 SuperAgent가 자동으로 재시도합니다.

이 메서드는 두 개의 선택적 인자를 받습니다. 재시도 횟수(기본값은 1)와 콜백 함수입니다. 각 재시도 전에 `callback(err, res)`를 호출합니다. 콜백 함수는 요청을 재시도할지 여부를 결정하기 위해 `true` 또는 `false`를 반환할 수 있습니다. 단, 최대 재시도 횟수는 항상 적용됩니다.

```javascript
     request
       .get('https://example.com/search')
       .retry(2) // 혹은
       .retry(2, callback)
       .then(finished);
       .catch(failed);
```

멱등한 요청인 경우에만 `.retry()` 메서드를 사용하세요. 예를 들어, 동일한 요청이 서버에 여러 번 도달하더라도 중복 구매와 같은 바람직하지 않은 부작용이 발생하지 않아야 합니다.

모든 요청 메서드는 기본적으로 재시도 대상에 포함됩니다. 따라서 POST 요청을 재시도하지 않도록 하려면, 사용자 정의 재시도 콜백을 전달해야 합니다.

기본적으로 다음과 같은 상태 코드는 자동으로 재시도됩니다.

- `408`
- `413`
- `429`
- `500`
- `502`
- `503`
- `504`
- `521`
- `522`
- `524`

기본적으로 다음과 같은 오류 코드가 자동으로 재시도됩니다.

- `'ETIMEDOUT'`
- `'ECONNRESET'`
- `'EADDRINUSE'`
- `'ECONNREFUSED'`
- `'EPIPE'`
- `'ENOTFOUND'`
- `'ENETUNREACH'`
- `'EAI_AGAIN'`

## Accept 설정하기

`.type()` 메서드와 유사하게, `.accept()` 메서드를 사용하면 `Accept` 헤더를 간편하게 설정할 수 있습니다. 이 메서드는 `request.types`를 참조하며, `type/subtype` 형식의 MIME 타입 전체 이름이나 "xml", "json", "png" 등의 확장자 형태로도 지정할 수 있어 편리합니다.

```javascript
request.get('/user').accept('application/json');

request.get('/user').accept('json');

request.post('/user').accept('png');
```

### Facebook과 Accept JSON

Facebook API를 호출할 때는 반드시 요청 헤더에 `Accept: application/json`을 포함해야 합니다. 그렇지 않으면 Facebook은 `Content-Type: text/javascript; charset=UTF-8`으로 응답하게 되며, SuperAgent는 이 형식을 파싱하지 못해 `res.body`가 `undefined`가 됩니다. `req.accept('json')` 또는 `req.set('Accept', 'application/json')`을 사용할 수 있습니다. 자세한 사항은 [issue 1078](https://github.com/ladjs/superagent/issues/1078)에서 확인해보세요.

## 쿼리 문자열

`req.query(obj)`는 쿼리 문자열을 구성하는 데 사용되는 메서드입니다. 예를 들어 **POST** 요청에서 `?format=json&dest=/login`과 같은 쿼리 문자열을 추가할 수 있습니다.

```javascript
request
  .post('/')
  .query({ format: 'json' })
  .query({ dest: '/login' })
  .send({ post: 'data', here: 'wahoo' })
  .then(callback);
```

기본적으로 쿼리 문자열은 특정한 순서로 조립되지 않습니다. ASCII 순으로 정렬된 쿼리 문자열을 사용하려면 `req.sortQuery()`를 호출하면 됩니다. 또한 `req.sortQuery(myComparisonFn)`을 통해 사용자 정의 정렬 비교 함수를 전달할 수도 있습니다. 비교 함수는 두 개의 인자를 받아 음수, 0 또는 양수를 반환해야 합니다.

```js
// 기본 정렬 방식
request
  .get('/user')
  .query('name=Nick')
  .query('search=Manny')
  .sortQuery()
  .then(callback);

// 사용자 정의 정렬 함수
request
  .get('/user')
  .query('name=Nick')
  .query('search=Manny')
  .sortQuery((a, b) => a.length - b.length)
  .then(callback);
```

## TLS 옵션

Node.js에서 SuperAgent는 HTTPS 요청을 구성할 수 있는 다양한 메서드를 지원합니다.

- `.ca()`: 신뢰할 CA 인증서를 설정합니다.
- `.cert()`: 클라이언트 인증서 체인을 설정합니다.
- `.key()`: 클라이언트의 개인 키를 설정합니다.
- `.pfx()`: PKCS12 형식의 PFX 파일을 사용하여 클라이언트의 개인 키와 인증서 체인을 설정합니다.
- `.disableTLSCerts()`: 만료되었거나 유효하지 않은 TLS 인증서를 거부하지 않도록 설정합니다. 내부적으로 `rejectUnauthorized=true`가 설정되며, 중간자 공격(MITM)에 노출될 수 있으므로 주의가 필요합니다.

더 자세한 내용은 Node.js [https.request 문서](https://nodejs.org/api/https.html#https_https_request_options_callback)에서 확인할 수 있습니다.

```js
var key = fs.readFileSync('key.pem'),
  cert = fs.readFileSync('cert.pem');

request.post('/client-auth').key(key).cert(cert).then(callback);
```

```js
var ca = fs.readFileSync('ca.cert.pem');

request
  .post('https://localhost/private-ca-server')
  .ca(ca)
  .then((res) => {});
```

## Parsing response bodies

## 응답 본문 파싱하기

SuperAgent will parse known response-body data for you,
currently supporting `application/x-www-form-urlencoded`,
`application/json`, and `multipart/form-data`. You can setup
automatic parsing for other response-body data as well:

SuperAgent는 응답 본문 데이터를 자동으로 파싱해줍니다.  
현재 `application/x-www-form-urlencoded`, `application/json`, `multipart/form-data`을 지원합니다. 이외의 응답 본문 데이터에 대해서도 자동 파싱을 설정할 수 있습니다.

```js
// 브라우저
request.parse['application/xml'] = function (str) {
  return { object: 'parsed from str' };
};

// node
request.parse['application/xml'] = function (res, cb) {
  // 응답 문자를 파싱하고 res.body를 여기서 설정하세요

  cb(null, res);
};

// 앞으로 'application/xml' 유형의 반응은
// 자동으로 파싱됩니다
```

`.buffer(true).parse(fn)` 메서드를 사용하면 내장된 파서보다 우선적으로 적용되는 사용자 정의 파서를 설정할 수 있습니다. `.buffer(false)`로 응답 버퍼링이 비활성화되어 있다면, `response` 이벤트는 본문 파싱이 완료되기 전에 발생하므로 `response.body`를 사용할 수 없습니다.

### JSON / Urlencoded

`res.body` 속성은 파싱된 객체를 나타냅니다. 예를 들어, 응답이 JSON 문자열 `{"user":{"name":"tobi"}}`를 반환했다면, `res.body.user.name`은 "tobi" 값을 갖게 됩니다. 마찬가지로 x-www-form-urlencoded 형식의 "user[name]=tobi"도 동일한 결과를 제공합니다. 단, 중첩은 한 단계까지만 지원되므로 더 복잡한 구조의 데이터를 다루려면 JSON 형식을 사용하는 것이 좋습니다.

배열은 key를 반복해서 전달하는 방식으로 전송됩니다. 예를 들어, `.send({ color: ['red', 'blue'] })`는 `color=red&color=blue`로 변환되어 전송됩니다. 배열의 key에 `[]`를 포함시키고 싶다면 SuperAgent는 이를 자동으로 처리하지 않으므로, 직접 `color[]`와 같이 key 이름에 대괄호를 추가해야 합니다.

### 다중 파트

Node 클라이언트는 [Formidable](https://github.com/felixge/node-formidable) 모듈을 통해 *multipart/form-data*를 지원합니다.  
다중 파트 응답을 파싱할 때 `res.files` 객체를 사용할 수 있으며, 이 객체에는 업로드된 파일에 대한 정보가 포함됩니다. 예를 들어, 다음과 같은 multipart 본문을 포함한 응답을 가정해볼 수 있습니다.

    --whoop
    Content-Disposition: attachment; name="image"; filename="tobi.png"
    Content-Type: image/png

    ... data here ...
    --whoop
    Content-Disposition: form-data; name="name"
    Content-Type: text/plain

    Tobi
    --whoop--

`res.body.name`은 "Tobi" 값을 가지고 있으며, `res.files.image`는 디스크 경로, 파일 이름 및 기타 속성을 포함한 `File` 객체입니다.

### 바이너리

브라우저에서는 바이너리 응답 본문을 처리하기 위해 `.responseType('blob')`을 사용할 수 있습니다. 이 API는 Node.js 환경에서는 필요하지 않습니다. 이 메서드에서 지원되는 인자 값은 다음과 같습니다.

- `'blob'`는 XMLHttpRequest의 `responseType` 속성에 그대로 전달됩니다.
- `'arraybuffer'`도 마찬가지로 `responseType` 속성에 전달됩니다.

```js
req
  .get('/binary.data')
  .responseType('blob')
  .then((res) => {
    // 여기서 res.body는 브라우저 기본 Blob 타입입니다.
  });
```

더 자세한 내용은 Mozilla Developer Network의 [XMLHttpRequest.responseType 문서](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/responseType)에서 확인할 수 있습니다.

## 응답 속성

`Response` 객체에는 응답 텍스트, 파싱된 응답 본문, 헤더 필드, 상태 플래그 등 다양한 유용한 플래그와 속성이 설정되어 있습니다.

### 응답 문자

`res.text` 속성에는 파싱되지 않은 응답 본문 문자열이 포함됩니다. 이 속성은 클라이언트 API에서는 항상 존재하며, Node 환경에서는 MIME 타입이 "text/_", "_/json", "x-www-form-urlencoded"와 일치할 경우에만 기본적으로 제공됩니다. 이러한 제한은 대용량 multipart 파일이나 이미지 등의 본문을 텍스트로 버퍼링하는 것이 매우 비효율적이기 때문에 메모리를 절약하기 위한 목적입니다. 응답을 강제로 버퍼링하려면 "응답 버퍼링" 섹션을 참조하세요.

### 응답 본문

SuperAgent는 요청 데이터를 자동으로 직렬화할 뿐만 아니라, 자동으로 파싱할 수도 있습니다. Content-Type에 대해 파서가 정의되어 있는 경우, 해당 타입에 맞게 응답이 파싱되며 기본적으로 "application/json"과 "application/x-www-form-urlencoded" 형식이 포함됩니다. 파싱된 객체는 `res.body`를 통해 접근할 수 있습니다.

### 응답 헤더 필드

`res.header`는 파싱된 응답 헤더 필드를 담은 객체로, Node.js와 마찬가지로 필드 이름을 소문자로 변환하여 저장합니다.  
예를 들어, `res.header['content-length']`와 같이 접근할 수 있습니다.

### 응답 콘텐츠 타입

Content-Type 응답 헤더는 특별하게 처리되어 `res.type` 속성은 charset 정보를 제외한 콘텐츠 타입만을 제공합니다. 예를 들어 Content-Type이 "text/html; charset=utf8"인 경우, `res.type`은 "text/html"을 반환하고, `res.charset` 속성에는 "utf8"이 포함됩니다.

### 응답 상태

응답 상태 플래그는 요청이 성공했는지 여부를 비롯한 다양한 유용한 정보를 판단하는 데 도움을 줍니다. 이를 통해 SuperAgent는 RESTful 웹 서비스와 효과적으로 상호작용할 수 있습니다. 현재 정의된 주요 플래그는 다음과 같습니다.

```javascript
var type = (status / 100) | 0;

// 상태 / 클래스
res.status = status;
res.statusType = type;

// 기본
res.info = 1 == type;
res.ok = 2 == type;
res.clientError = 4 == type;
res.serverError = 5 == type;
res.error = 4 == type || 5 == type;

// 편의 기능
res.accepted = 202 == status;
res.noContent = 204 == status || 1223 == status;
res.badRequest = 400 == status;
res.unauthorized = 401 == status;
res.notAcceptable = 406 == status;
res.notFound = 404 == status;
res.forbidden = 403 == status;
```

## 요청 중단하기

요청을 중단하려면 `req.abort()` 메서드를 호출하기만 하면 됩니다.

## 타임아웃

때때로 네트워크나 서버가 요청을 수신한 후 응답 없이 멈춰버리는 경우가 있습니다. 이러한 무한 대기를 방지하려면 타임아웃을 설정해야 합니다.

- `req.timeout({deadline: ms})` 또는 `req.timeout(ms)`는 업로드, 리다이렉트, 서버 처리 시간을 포함한 전체 요청이 완료되어야 하는 최종 시간 제한을 설정합니다. `ms`는 0보다 큰 밀리초 단위의 숫자이며, 제한 시간 내에 응답이 완료되지 않으면 요청은 중단됩니다.

- `req.timeout({response: ms})`는 서버로부터 첫 번째 바이트가 도착할 때까지의 최대 대기 시간을 설정합니다. 전체 다운로드 소요 시간은 제한하지 않습니다. 응답 타임아웃은 DNS 조회, TCP/IP 및 TLS 연결, 요청 데이터 업로드 시간을 포함하므로, 서버의 실제 응답 시간보다 몇 초 더 길게 설정하는 것이 좋습니다.

`deadline`과 `response` 타임아웃은 함께 사용하는 것이 좋습니다. 짧은 응답 타임아웃은 응답하지 않는 네트워크를 빠르게 감지하는 데 유용하고, 긴 데드라인은 느리지만 안정적인 네트워크 환경에서 다운로드를 완료할 수 있도록 여유 시간을 제공합니다. 두 타이머 모두 첨부된 파일 업로드에 허용되는 시간을 제한합니다. 파일을 업로드하는 경우에는 충분히 긴 타임아웃을 설정하는 것이 좋습니다.

```javascript
request
  .get('/big-file?network=slow')
  .timeout({
    response: 5000, // 서버가 데이터를 보내기 시작할 때까지 최대 5초간 기다립니다.
    deadline: 60000 // 파일 전체를 로드하는 데 최대 1분까지 허용합니다.
  })
  .then(
    (res) => {
      /* 제시간 응답 수신 */
    },
    (err) => {
      if (err.timeout) {
        /* 시간 초과! */
      } else {
        /* 그 외 오류 */
      }
    }
  );
```

타임아웃 오류에는 `.timeout` 속성이 포함되어 있습니다.

## 인증

Node와 브라우저 환경에서 `.auth()` 메서드를 사용하여 인증을 수행할 수 있습니다.

```javascript
request.get('http://local').auth('tobi', 'learnboost').then(callback);
```

_Node_ 클라이언트에서는 기본 인증을 URL 내에 "user:pass" 형식으로 포함시킬 수 있습니다.

```javascript
request.get('http://tobi:learnboost@local').then(callback);
```

기본적으로 `Basic` 인증만 사용됩니다. 브라우저에서는 `{type: 'auto'}`를 추가하면 Digest, NTLM 등 브라우저에 내장된 모든 인증 방식을 사용할 수 있습니다.

```javascript
request.auth('digest', 'secret', { type: 'auto' });
```

`auth` 메서드는 토큰 기반 인증을 위한 `type: 'bearer'` 옵션도 지원합니다.

```javascript
request.auth('my_token', { type: 'bearer' });
```

## 다음 리다이렉션 따라가기

기본적으로 최대 5번까지 리다이렉션이 자동으로 따라가며, 필요에 따라 `res.redirects(n)` 메서드를 사용하여 이 횟수를 지정할 수 있습니다.

```javascript
const response = await request.get('/some.png').redirects(2);
```

리다이렉션 횟수가 제한을 초과하면 오류로 간주됩니다. 이를 성공적인 응답으로 처리하려면 `.ok(res => res.status < 400)` 메서드를 사용하세요.

## 전역 상태를 위한 에이전트

### 쿠키 저장하기

Node에서 SuperAgent는 기본적으로 쿠키를 저장하지 않습니다. 하지만 `.agent()` 메서드를 사용하면 쿠키를 저장하는 SuperAgent 인스턴스를 생성할 수 있습니다. 각 인스턴스는 독립적인 쿠키 저장소를 가지고 있습니다.

```javascript
const agent = request.agent();
agent.post('/login').then(() => {
  return agent.get('/cookied-page');
});
```

브라우저에서는 쿠키가 자동으로 관리되므로 `.agent()`를 사용해도 쿠키가 분리되지는 않습니다.

### 다중 요청을 위한 기본 옵션

에이전트에서 호출된 일반 요청 메서드는 해당 에이전트가 처리하는 모든 요청에 대해 기본값으로 적용됩니다.

```javascript
const agent = request.agent().use(plugin).auth(shared);

await agent.get('/with-plugin-and-auth');
await agent.get('/also-with-plugin-and-auth');
```

에이전트가 기본 옵션을 설정할 수 있도록 지원하는 메서드 목록입니다. `use`, `on`, `once`, `set`, `query`, `type`, `accept`, `auth`, `withCredentials`, `sortQuery`, `retry`, `ok`, `redirects`, `timeout`, `buffer`, `serialize`, `parse`, `ca`, `key`, `pfx`, `cert`.

## 데이터 전달 방식

`.pipe()`는 `.end()` 또는 `.then()` 메서드 **대신** 사용되며, Node 클라이언트는 요청과 응답 간에 데이터를 주고받도록 파이프 처리할 수 있습니다.

예를 들어, 파일의 콘텐츠를 요청 본문으로 전달하는 경우는 다음과 같습니다.

```javascript
const request = require('superagent');
const fs = require('fs');

const stream = fs.createReadStream('path/to/my.json');
const req = request.post('/somewhere');
req.type('json');
stream.pipe(req);
```

요청에 데이터를 파이프할 경우, SuperAgent는 해당 데이터를 [청크 전송 인코딩](https://en.wikipedia.org/wiki/Chunked_transfer_encoding) 방식으로 전송합니다. 이 방식은 Python WSGI 서버 등 모든 서버에서 지원되지는 않습니다.

응답을 파일로 저장하려면 다음과 같이 파이프 처리할 수 있습니다.

```javascript
const stream = fs.createWriteStream('path/to/my.json');
const req = request.get('/some.json');
req.pipe(stream);
```

파이프와 콜백 또는 프로미스는 **함께 사용할 수 없으며**, `.end()`나 `Response` 객체의 결과를 파이프 처리해서는 안 됩니다.

```javascript
// 이러한 방식으로 하지 마세요.
const stream = getAWritableStream();
const req = request
  .get('/some.json')
  // 나쁨: 이 방식은 스트림에 올바르지 않은 데이터를 전달하며 예기치 못한 방식으로 실패할 수 있습니다.
  .end((err, this_does_not_work) => this_does_not_work.pipe(stream));
const req = request
  .get('/some.json')
  .end()
  // 나쁨: 이 방식도 지원되지 않으며, .pipe는 자동으로 .end를 호출합니다.
  .pipe(nope_its_too_late);
```

SuperAgent의 [향후 버전](https://github.com/ladjs/superagent/issues/1188)에서는 `pipe()`를 부적절하게 호출하면 실패하게 됩니다.

## 다중 부분 요청

`.attach()`와 `.field()` 메서드를 제공하는 SuperAgent는 다중 부분 요청을 구성하는 데에도 매우 유용합니다.

`.field()` 또는 `.attach()`를 사용할 경우 `.send()`는 사용할 수 없으며, `Content-Type` 헤더를 직접 설정해서는 안 됩니다. 올바른 타입은 자동으로 지정됩니다.

### 파일 첨부하기

`.attach(name, [file], [options])`를 사용하여 파일을 전송할 수 있습니다. 여러 파일을 첨부하려면 `.attach`를 반복 호출하면 됩니다. 인자는 다음과 같습니다.

- `name` — 폼 이름 필드
- `file` — 파일 경로의 문자열 또는 `Blob`/`Buffer` 객체.
- `options` — (선택) 사용자 정의 파일 이름의 문자열 또는 `{filename: string}` 형식의 객체. Node 환경에서는 `{contentType: 'mime/type'}`도 지원하며 브라우저에서는 적절한 타입의 `Blob` 객체를 생성해야 합니다.

<br>

```javascript
request
  .post('/upload')
  .attach('image1', 'path/to/felix.jpeg')
  .attach('image2', imageBuffer, 'luna.jpeg')
  .field('caption', 'My cats')
  .then(callback);
```

### 필드 값

`.field(name, value)` 및 `.field({name: value})`를 사용해 HTML 폼 필드처럼 값을 설정할 수 있습니다. 예를 들어 이름과 이메일 정보를 함께 여러 이미지를 업로드하려면, 요청은 다음과 같이 구성될 수 있습니다.

```javascript
request
  .post('/upload')
  .field('user[name]', 'Tobi')
  .field('user[email]', 'tobi@learnboost.com')
  .field('friends[]', ['loki', 'jane'])
  .attach('image', 'path/to/tobi.png')
  .then(callback);
```

## 압축

node 클라이언트는 압축된 응답을 지원하며, 아무 것도 하지 않아도 됩니다! 그냥 작동합니다.

## 응답 버퍼링

To force buffering of response bodies as `res.text` you may invoke `req.buffer()`. To undo the default of buffering for text responses such as "text/plain", "text/html" etc you may invoke `req.buffer(false)`.

`.req.buffer()`를 호출하면 응답 본문을 `res.text`로 강제 버퍼링할 수 있습니다. "text/plain", "text/html" 등 텍스트 응답의 기본 버퍼링을 취소하려면 `.req.buffer(false)`를 호출하세요.

`res.buffered` 플래그가 제공되면, 이를 활용하여 동일한 콜백 함수에서 버퍼링된 응답과 버퍼링되지 않은 응답을 모두 처리할 수 있습니다.

## CORS

보안상의 이유로 브라우저는 서버가 CORS 헤더를 통해 명시적으로 허용하지 않으면 교차 출처 요청(cross-origin requests)을 차단합니다. 브라우저는 또한 서버가 어떤 HTTP 헤더와 메서드를 허용하는지 확인하기 위해 추가적인 **OPTIONS** 요청을 전송합니다. [CORS에 대해 더 알아보기](https://developer.mozilla.org/ko/docs/Web/HTTP/Guides/CORS).

`.withCredentials()` 메서드는 origin(출처)에서 쿠키를 전송할 수 있도록 활성화합니다. 단, 이 기능은 `Access-Control-Allow-Origin` 값이 와일드카드("\*")가 _아니어야_ 하며, `Access-Control-Allow-Credentials` 값이 `"true"`일 경우에만 작동합니다.

```javascript
request
  .get('https://api.example.com:4001/')
  .withCredentials()
  .then((res) => {
    assert.equal(200, res.status);
    assert.equal('tobi', res.text);
  });
```

## 오류 처리하기

콜백 함수는 항상 두 개의 인자를 전달합니다. 오류와 응답입니다. 오류가 발생하지 않으면, 첫 번째 인자는 null 입니다.

```javascript
request
  .post('/upload')
  .attach('image', 'path/to/tobi.png')
  .then((res) => {});
```

"error" 이벤트도 발생하며, 이를 통해 오류를 감지하고 처리할 수 있습니다.

```javascript
request
  .post('/upload')
  .attach('image', 'path/to/tobi.png')
  .on('error', handle)
  .then((res) => {});
```

**SuperAgent는 기본적으로 4xx 및 5xx 응답(그리고 처리되지 않은 3xx 응답도 포함)을 오류**로 간주합니다. 예를 들어 `304 Not Modified`, `403 Forbidden`, `500 Internal Server Error` 같은 응답을 받으면 해당 상태 정보는 `err.status`를 통해 확인할 수 있습니다. 이러한 응답으로부터 발생한 오류에는 "[응답 요소](#response-properties)"에서 언급한 모든 속성을 포함한 `err.response` 필드도 포함됩니다. 이 라이브러리는 일반적으로 성공 응답만을 원하고, HTTP 오류 상태 코드를 오류로 처리하는 경우를 대비하여 이러한 방식으로 동작합니다. 하지만 특정 오류 조건에 대해서는 사용자 정의 로직을 허용하도록 설계되어 있습니다.

네트워크 실패, 시간초과, 응답 없는 오류는 `err.status` 또는 `err.response` 필드를 포함하지 않습니다.

404 또는 HTTP 오류 응답을 처리하고 싶다면, `error.status` 요소를 사용할 수 있습니다. HTTP 오류(4xx 또는 5xx 응답)가 발생했을 때 `res.error` 요소는 `Error` 객체이고 이는 다음과 같이 에러 확인을 수행할 수 있습니다.

```javascript
if (err && err.status === 404) {
  alert('oh no ' + res.body.message);
} else if (err) {
  // 그 외 다른 모든 오류 유형은 일반적으로 처리합니다
}
```

대안으로, `.ok(callback)` 메서드를 사용하여 응답이 오류인지 아닌지 결정할 수 있습니다. `ok` 콜백은 응답을 받고 응답이 성공으로 해석되면 `true`를 반환합니다.

```javascript
request
  .get('/404')
  .ok((res) => res.status < 500)
  .then((response) => {
    // 404 페이지를 성공적인 응답으로 처리합니다
  });
```

## 진행과정 추적하기

SuperAgent는 업로드와 큰 파일 다운로드에서 `progress` 이벤트를 동작시킵니다.

```javascript
request
  .post(url)
  .attach('field_name', file)
  .on('progress', (event) => {
    /* 이벤트 객체는 다음과 같습니다.
        {
          direction: "upload" or "download"
          percent: 0 to 100 // 0에서 100까지 (파일 크기를 알 수 없는 경우 생략될 수 있습니다)
          total: // 전체 파일 크기 (생략될 수 있습니다)
          loaded: // 현재까지 다운로드되거나 업로드된 바이트 수
        } */
  })
  .then();
```

## 로컬 호스트에서 테스트하기

### 특정 IP 주소 연결 설정하기

In Node.js it's possible to ignore DNS resolution and direct all requests to a specific IP address using `.connect()` method. For example, this request will go to localhost instead of `example.com`:

Node.js에서는 DNS를 무시하고 `.connect()` 메서드를 사용하여 모든 요청을 특정 IP 주소로 직접 연결할 수 있습니다. 예를 들어, 이 요청은 `example.com` 대신 로컬호스트로 전달됩니다.

```javascript
const res = await request.get('http://example.com').connect('127.0.0.1');
```

요청은 리다이렉트 되어, 여러 호스트명과 IP를 특정지을 수 있으며 특별한 `*`를 대체로 설정할 수 있습니다. (다른 와일드 카드는 지원되지 않습니다). 요청은 원본 값을 가지며 본인의 `Host` 헤더를 유지합니다. `.connect(undefined)`는 이러한 기능을 끕니다.

```javascript
const res = await request.get('http://redir.example.com:555').connect({
  'redir.example.com': '127.0.0.1', // redir.example.com:555는 127.0.0.1:555를 사용합니다.
  'www.example.com': false, // 이 항목은 재정의하지 마세요. 일반적인 DNS 설정을 사용합니다.
  'mapped.example.com': { host: '127.0.0.1', port: 8080 }, // mapped.example.com의 모든 포트는 127.0.0.1:8080으로 매핑됩니다.
  '*': 'proxy.example.com' // 나머지 모든 요청은 이 호스트로 전달됩니다
});
```

### 로컬 호스트에서 깨지거나 보안되지 않은 HTTPS 무시하기

Node.js에서 HTTPS 설정이 잘못되었거나 보안성이 떨어지는 경우(예: 자체 서명된 인증서를 사용하면서 `.ca()`를 지정하지 않은 경우), `.trustLocalhost()`를 호출하면 `localhost`로의 요청을 허용할 수 있습니다.

```javascript
const res = await request.get('https://localhost').trustLocalhost();
```

`.connect("127.0.0.1")`와 함께 사용하면 HTTPS 요청을 어떤 도메인에서든 `localhost`로 강제로 리다이렉트할 수 있습니다.

`localhost`는 신뢰되지 않은 네트워크에 노출되지 않는 루프백 인터페이스이기 때문에, 깨진 HTTPS를 무시하는 것이 일반적으로 안전합니다. `localhost`를 신뢰하도록 설정하는 것이 향후 기본값이 될 수 있습니다. `127.0.0.1`의 진위 여부를 강제로 검사하려면 `.trustLocalhost(false)`를 사용하세요.

다른 IP 주소로 요청을 보낼 때 HTTPS 보안을 비활성화하는 기능은 의도적으로 지원하지 않습니다. 이러한 옵션은 HTTPS 문제를 빠르게 "해결"하려는 방식으로 오용되는 경우가 많기 때문입니다. [Let's Encrypt](https://certbot.eff.org)를 통해 무료 HTTPS 인증서를 발급받거나, `.ca(ca_public_pem)`을 사용해 자체 서명된 인증서를 신뢰할 수 있도록 직접 CA를 설정할 수 있습니다.

## Promise 및 Generator 지원

SuperAgent의 요청은 "thenable" 객체이며, JavaScript의 Promise 및 `async`/`await` 문법과 호환됩니다.

```javascript
const res = await request.get(url);
```

Promise를 사용할 경우, **`.end()` 또는 `.pipe()`를 호출하지 마세요**. `.then()` 또는 `await`를 사용하면 요청을 처리할 수 있는 다른 방식들이 모두 비활성화됩니다.

[co](https://github.com/tj/co)와 같은 라이브러리나 [koa](https://github.com/koajs/koa)와 같은 웹 프레임워크에서는 SuperAgent의 모든 메서드에서 `yield`를 사용할 수 있습니다.

```javascript
    const req = request
      .get('http://local')
      .auth('tobi', 'learnboost');
    const res = yield req;
```

SuperAgent는 전역 `Promise` 객체가 존재하는 환경에서 동작하도록 설계되어 있습니다. Internet Explorer나 Node.js 0.10에서 promise를 사용하려면 v7 버전과 폴리필이 필요합니다.

v8 버전부터는 IE에 대한 지원이 중단되었습니다. Opera 85나 iOS Safari 12.2–12.5 등을 지원하려면 WeakRef와 BigInt에 대한 폴리필을 추가해야 합니다. 예를 들어 <https://cdnjs.cloudflare.com/polyfill/>을 사용할 수 있습니다.

```html
<script src="https://cdnjs.cloudflare.com/polyfill/v3/polyfill.min.js?features=WeakRef,BigInt"></script>
```

## 브라우저와 node 버전

SuperAgent에는 두 가지 구현 방식이 있습니다. 하나는 웹 브라우저용(XHR 사용)이고, 다른 하나는 Node.JS용(core http 모듈 사용)입니다. 기본적으로 Browserify와 WebPack은 브라우저 버전을 선택합니다.

Node.JS용 코드를 컴파일하려면 WebPack 설정에서 반드시 [node target](https://webpack.github.io/docs/configuration.html#target)을 지정해야 합니다.
```

## File: `docs/zh_CN/index.html`
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf8">
    <title>SuperAgent — elegant API for AJAX in Node and browsers</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/tocbot/3.0.0/tocbot.css">
    <link rel="stylesheet" href="../style.css">
  </head>
  <body>
    <ul id="menu"></ul>
    <div id="content">
<h1 id="superagent">SuperAgent</h1>
<p>SuperAgent是轻量级的渐进式ajax API，具有灵活性、可读性和较低的学习曲线。 它也适用于Node.js!  </p>
<pre><code> request
   .post(&#39;/api/pet&#39;)
   .send({ name: &#39;Manny&#39;, species: &#39;cat&#39; })
   .set(&#39;X-API-Key&#39;, &#39;foobar&#39;)
   .set(&#39;Accept&#39;, &#39;application/json&#39;)
   .then(res =&gt; {
      alert(&#39;yay got &#39; + JSON.stringify(res.body));
   });
</code></pre>
<h2 id="测试文档">测试文档</h2>
<p><a href="/"><strong>English</strong></a></p>
<p>下面的<a href="../test.html">测试文档</a>是用<a href="https://mochajs.org/">Mocha</a>的&quot;文档&quot;报告器生成的，并直接反映了测试套件。 这提供了额外的文档来源。  </p>
<h2 id="基本请求">基本请求</h2>
<p>可以通过调用 <code>request</code> 对象上的适当方法来发起请求，然后调用 <code>.then()</code> ( 或 <code>.end()</code> 或 <a href="#promise-and-generator-support"><code>await</code></a> )发送请求。例如一个简单的 <strong>GET</strong> 请求：</p>
<pre><code> request
   .get(&#39;/search&#39;)
   .then(res =&gt; {
      // res.body, res.headers, res.status
   })
   .catch(err =&gt; {
      // err.message, err.response
   });
</code></pre>
<p>HTTP 方法也可以作为字符串传递：<br>译者注：大小写皆可。</p>
<pre><code>request(&#39;GET&#39;, &#39;/search&#39;).then(success, failure);
</code></pre>
<p>旧式回调也受支持，但不推荐使用。您可以调用 <code>.end()</code> <em>代替</em> <code>.then()</code>：</p>
<pre><code>request(&#39;GET&#39;, &#39;/search&#39;).end(function(err, res){
  if (res.ok) {}
});
</code></pre>
<p>可以使用绝对 URL。在 Web 浏览器中，绝对 URL 仅在服务器实现 <a href="#cors">CORS</a> 时才有效。</p>
<pre><code> request
   .get(&#39;https://example.com/search&#39;)
   .then(res =&gt; {

   });
</code></pre>
<p><strong>Node</strong> 客户端支持向 <a href="https://zh.wikipedia.org/wiki/Unix%E5%9F%9F%E5%A5%97%E6%8E%A5%E5%AD%97">Unix 域套接字</a> 发出请求：</p>
<pre><code>// pattern: https?+unix://SOCKET_PATH/REQUEST_PATH
//在套接字路径中将 `%2F` 用作 `/`
try {
  const res = await request
    .get(&#39;http+unix://%2Fabsolute%2Fpath%2Fto%2Funix.sock/search&#39;);
  // res.body, res.headers, res.status
} catch(err) {
  // err.message, err.response
}
</code></pre>
<p><strong>DELETE__、__HEAD__、__PATCH__、__POST</strong> 和 <strong>PUT</strong> 请求也可以使用，只需更改方法名称：</p>
<pre><code>request
  .head(&#39;/favicon.ico&#39;)
  .then(res =&gt; {

  });
</code></pre>
<p><strong>DELETE</strong> 也可以用 <code>.del()</code> 调用以与旧版 IE 兼容，其中 <code>delete</code> 是保留字。</p>
<p>HTTP 方法默认为 __GET__，因此如果您愿意，以下代码是有效的：</p>
<pre><code> request(&#39;/search&#39;, (err, res) =&gt; {

 });
</code></pre>
<h2 id="使用-http-2">使用 HTTP/2</h2>
<p>要使用 HTTP/2 协议（没有 HTTP/1.x 后备），请使用 <code>.http2()</code> 方法。</p>
<pre><code class="language-javascript">    const request = require(&#39;superagent&#39;);
    const res = await request
      .get(&#39;https://example.com/h2&#39;)
      .http2();
</code></pre>
<h2 id="设置请求头字段">设置请求头字段</h2>
<p>设置请求头字段很简单，调用 <code>.set()</code> 时传入字段名称和值：</p>
<pre><code> request
   .get(&#39;/search&#39;)
   .set(&#39;API-Key&#39;, &#39;foobar&#39;)
   .set(&#39;Accept&#39;, &#39;application/json&#39;)
   .then(callback);
</code></pre>
<p>您还可以在一次调用中传入一个对象来设置多个字段：</p>
<pre><code> request
   .get(&#39;/search&#39;)
   .set({ &#39;API-Key&#39;: &#39;foobar&#39;, Accept: &#39;application/json&#39; })
   .then(callback);
</code></pre>
<h2 id="get-请求"><code>GET</code> 请求</h2>
<p><code>.query()</code> 方法接受对象，当与 <strong>GET</strong> 方法一起使用时将形成一个查询字符串。以下将产生路径 <code>/search?query=Manny&amp;range=1..5&amp;order=desc</code>。
译者注：<code>.query()</code> 方法的参数不需要提前进行url编码。</p>
<pre><code> request
   .get(&#39;/search&#39;)
   .query({ query: &#39;Manny&#39; })
   .query({ range: &#39;1..5&#39; })
   .query({ order: &#39;desc&#39; })
   .then(res =&gt; {

   });
</code></pre>
<p>或传入单个对象：</p>
<pre><code>request
  .get(&#39;/search&#39;)
  .query({ query: &#39;Manny&#39;, range: &#39;1..5&#39;, order: &#39;desc&#39; })
  .then(res =&gt; {

  });
</code></pre>
<p><code>.query()</code> 方法也可以接受字符串。</p>
<pre><code>  request
    .get(&#39;/querystring&#39;)
    .query(&#39;search=Manny&amp;range=1..5&#39;)
    .then(res =&gt; {

    });
</code></pre>
<p>或者一个个加入：</p>
<pre><code>  request
    .get(&#39;/querystring&#39;)
    .query(&#39;search=Manny&#39;)
    .query(&#39;range=1..5&#39;)
    .then(res =&gt; {

    });
</code></pre>
<h2 id="head-请求"><code>HEAD</code> 请求</h2>
<p>您还可以对 <strong>HEAD</strong> 请求使用 .query() 方法。以下将生成路径 <code>/users?email=joe@smith.com</code>。</p>
<pre><code>  request
    .head(&#39;/users&#39;)
    .query({ email: &#39;joe@smith.com&#39; })
    .then(res =&gt; {

    });
</code></pre>
<h2 id="post--put-请求"><code>POST</code> / <code>PUT</code> 请求</h2>
<p>一个典型的 JSON <strong>POST</strong> 请求可能如下所示，我们适当地设置 <code>Content-Type</code> 请求头字段，并&quot;写入&quot;一些数据，在本例中只是一个 JSON 字符串。</p>
<pre><code>  request.post(&#39;/user&#39;)
    .set(&#39;Content-Type&#39;, &#39;application/json&#39;)
    .send(&#39;{&quot;name&quot;:&quot;tj&quot;,&quot;pet&quot;:&quot;tobi&quot;}&#39;)
    .then(callback)
    .catch(errorCallback)
</code></pre>
<p>由于 JSON 无疑是最常见的，所以它是 <em>默认</em> 的！下面的例子与前面的例子是等价的。</p>
<pre><code>  request.post(&#39;/user&#39;)
    .send({ name: &#39;tj&#39;, pet: &#39;tobi&#39; })
    .then(callback, errorCallback)
</code></pre>
<p>或者调用多个 <code>.send()</code>：</p>
<pre><code>  request.post(&#39;/user&#39;)
    .send({ name: &#39;tj&#39; })
    .send({ pet: &#39;tobi&#39; })
    .then(callback, errorCallback)
</code></pre>
<p>默认情况下，发送字符串会将 <code>Content-Type</code> 设置为 <code>application/x-www-form-urlencoded</code>，多个调用将用 <code>&amp;</code> 连接，这里产生 <code>name=tj&amp;pet=tobi</code>：</p>
<pre><code>  request.post(&#39;/user&#39;)
    .send(&#39;name=tj&#39;)
    .send(&#39;pet=tobi&#39;)
    .then(callback, errorCallback);
</code></pre>
<p>SuperAgent 格式是可扩展的，但默认情况下支持 &quot;json&quot; 和 &quot;form&quot;。要将数据作为 <code>application/x-www-form-urlencoded</code> 发送，只需在调用 <code>.type()</code> 时传入 &quot;form&quot;，默认为 &quot;json&quot;。此 <strong>POST</strong> 请求的请求体将是 &quot;name=tj&amp;pet=tobi&quot;。</p>
<pre><code>  request.post(&#39;/user&#39;)
    .type(&#39;form&#39;)
    .send({ name: &#39;tj&#39; })
    .send({ pet: &#39;tobi&#39; })
    .then(callback, errorCallback)
</code></pre>
<p>还支持发送 <a href="https://developer.mozilla.org/zh-CN/docs/Web/API/FormData/FormData"><code>FormData</code></a> 对象。以下示例将 <strong>POST</strong> 请求由 id=&quot;myForm&quot; 标识的 HTML 表单的内容：</p>
<pre><code>  request.post(&#39;/user&#39;)
    .send(new FormData(document.getElementById(&#39;myForm&#39;)))
    .then(callback, errorCallback)
</code></pre>
<h2 id="设置-content-type">设置 <code>Content-Type</code></h2>
<p>显而易见的解决方案是使用 <code>.set()</code> 方法：</p>
<pre><code> request.post(&#39;/user&#39;)
   .set(&#39;Content-Type&#39;, &#39;application/json&#39;)
</code></pre>
<p><code>.type()</code> 方法也可以作为简写，接受带有类型/子类型的规范化 <a href="https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Basics_of_HTTP/MIME_types">MIME 类型</a> 名称，或者只是扩展名，例如&quot;xml&quot;、&quot;json&quot;、&quot;png&quot;等：</p>
<pre><code> request.post(&#39;/user&#39;)
   .type(&#39;application/json&#39;)

 request.post(&#39;/user&#39;)
   .type(&#39;json&#39;)

 request.post(&#39;/user&#39;)
   .type(&#39;png&#39;)
</code></pre>
<h2 id="序列化请求体">序列化请求体</h2>
<p>SuperAgent 将自动序列化 JSON 和表单。您也可以为其他类型设置自动序列化：</p>
<pre><code class="language-js">request.serialize[&#39;application/xml&#39;] = function (obj) {
    return &#39;从obj生成的字符串&#39;;
};

// 接下来，内容类型为 &quot;application/xml&quot; 的所有请求都将自动序列化
</code></pre>
<p>如果您想以自定义格式发送 数据体(payload)，您可以根据每个请求将内置序列化替换为 <code>.serialize()</code> 方法：</p>
<pre><code class="language-js">request
    .post(&#39;/user&#39;)
    .send({foo: &#39;bar&#39;})
    .serialize(obj =&gt; {
        return &#39;从obj生成的字符串&#39;;
    });
</code></pre>
<h2 id="重试请求">重试请求</h2>
<p>如果请求暂时失败或可能是网络连接不稳定造成的失败，且当给定 <code>.retry()</code> 方法时，SuperAgent 将自动重试请求。</p>
<p>此方法有两个可选参数：重试次数（默认为 <code>1</code>）和回调函数。它在每次重试之前调用 callback(err, res) 。回调可以返回 <code>true</code>/<code>false</code> 以控制是否应重试请求（但始终应该用最大重试次数）。
     request
       .get(&#39;<a href="https://example.com/search&#39;">https://example.com/search&#39;</a>)
       .retry(2) // 或者：
       .retry(2, callback) // 二选一
       .then(finished);
       .catch(failed);</p>
<p><code>.retry()</code> 仅用于<a href="https://baike.baidu.com/item/%E5%B9%82%E7%AD%89/8600688?fr=aladdin"><em>幂等</em></a>请求（即到达服务器的多个请求不会导致重复购买等不良副作用）。</p>
<p>默认情况下会尝试所有请求方法（这意味着如果您不希望重试 POST 请求，则需要传递自定义的重试回调函数）。</p>
<p>默认情况下会重试以下状态代码：</p>
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
<p>默认情况下会重试以下错误代码：</p>
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
<h2 id="设置-accept">设置 Accept</h2>
<p>与 <code>.type()</code> 方法类似，也可以通过简写方法 <code>.accept()</code> 设置 <code>Accept</code> 请求头。方便起见，其中还引用了 <code>request.types</code>，允许您将完整的规范化 <a href="https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Basics_of_HTTP/MIME_types">MIME 类型</a> 名称指定为<code>类型/子类型</code>，或将扩展后缀形式指定为&quot;xml&quot;、&quot;json&quot;、&quot;png&quot;等：</p>
<pre><code> request.get(&#39;/user&#39;)
   .accept(&#39;application/json&#39;)

 request.get(&#39;/user&#39;)
   .accept(&#39;json&#39;)

 request.post(&#39;/user&#39;)
   .accept(&#39;png&#39;)
</code></pre>
<h3 id="facebook-和-accept-json">Facebook 和 Accept JSON</h3>
<p>如果您正在调用 Facebook 的 API，请务必在您的请求中发送 <code>Accept: application/json</code> 请求头。如果你不这样做，Facebook 会回复 <code>Content-Type: text/javascript; charset=UTF-8</code>，SuperAgent 将不会解析，因此 <code>res.body</code> 将是未定义的。您可以使用 <code>req.accept(&#39;json&#39;)</code> 或 <code>req.header(&#39;Accept&#39;, &#39;application/json&#39;)</code> 来执行此操作。有关详细信息，请参阅 <a href="https://github.com/ladjs/superagent/issues/1078">issue 1078</a>。</p>
<h2 id="查询字符串query-strings">查询字符串(Query strings)</h2>
<p><code>req.query(obj)</code> 是一种可用于构建查询字符串的方法。例如在 <strong>POST</strong> 上增加 <code>?format=json&amp;dest=/login</code>：</p>
<pre><code>request
  .post(&#39;/&#39;)
  .query({ format: &#39;json&#39; })
  .query({ dest: &#39;/login&#39; })
  .send({ post: &#39;data&#39;, here: &#39;wahoo&#39; })
  .then(callback);
</code></pre>
<p>默认情况下，查询字符串不按任何特定顺序组装。可以使用 <code>req.sortQuery()</code> 启用 ASCIIbetically 排序的查询字符串。您还可以使用 <code>req.sortQuery(myComparisonFn)</code> 提供自定义排序比较函数。比较函数应该接受 2 个参数并返回一个负/零/正整数。</p>
<pre><code class="language-js"> // 默认顺序
 request.get(&#39;/user&#39;)
   .query(&#39;name=Nick&#39;)
   .query(&#39;search=Manny&#39;)
   .sortQuery()
   .then(callback)

 // 自定义排序函数
 request.get(&#39;/user&#39;)
   .query(&#39;name=Nick&#39;)
   .query(&#39;search=Manny&#39;)
   .sortQuery((a, b) =&gt; a.length - b.length)
   .then(callback)
</code></pre>
<h2 id="tls-选项">TLS 选项</h2>
<p>在 Node.js 中，SuperAgent 支持配置 HTTPS 请求的方法：</p>
<ul>
<li><code>.ca()</code>: 将 CA 证书设置为信任</li>
<li><code>.cert()</code>: 设置客户端证书链</li>
<li><code>.key()</code>: 设置客户端私钥</li>
<li><code>.pfx()</code>: 设置客户端 PFX 或 PKCS12 编码的私钥和证书链</li>
<li><code>.disableTLSCerts()</code>: 不拒绝过期或无效的 TLS 证书。在内部设置 <code>rejectUnauthorized=true</code>。<em>请注意，此方法允许中间人攻击。</em></li>
</ul>
<p>有关更多信息，请参阅 Node.js <a href="http://nodejs.cn/api/https.html#httpsrequesturl-options-callback">https.request 文档</a>。</p>
<pre><code class="language-js">var key = fs.readFileSync(&#39;key.pem&#39;),
    cert = fs.readFileSync(&#39;cert.pem&#39;);

request
  .post(&#39;/client-auth&#39;)
  .key(key)
  .cert(cert)
  .then(callback);
</code></pre>
<pre><code class="language-js">var ca = fs.readFileSync(&#39;ca.cert.pem&#39;);

request
  .post(&#39;https://localhost/private-ca-server&#39;)
  .ca(ca)
  .then(res =&gt; {});
</code></pre>
<h2 id="解析响应体">解析响应体</h2>
<p>SuperAgent将为您解析已知的响应主体数据，目前支持<code>application/x-www-form-urlencoded</code>，<code>application/json</code>，以及<code>multipart/form data</code>。您可以设置自动解析其他响应主体数据：</p>
<pre><code class="language-js">//浏览器
request.parse[&#39;application/xml&#39;] = function (str) {
    return {&#39;object&#39;: &#39;从str解析的&#39;};
};

//node
request.parse[&#39;application/xml&#39;] = function (res, cb) {
    //解析响应文本并在此处设置res.body

    cb(null, res);
};

//接下来，将自动解析 &#39;application/xml&#39; 类型的响应
</code></pre>
<p>您可以使用 <code>.buffer(true).parse(fn)</code> 方法设置自定义解析器（优先于内置解析器）。如果未启用响应缓冲 (<code>.buffer(false)</code>)，则将触发<code>响应(response)</code>事件而无需等待正文解析器完成，因此 <code>response.body</code> 将不可用。</p>
<h3 id="json--urlencoded">JSON / Urlencoded</h3>
<p>属性 <code>res.body</code> 是解析后的对象，例如，如果请求以 JSON 字符串 &#39;{&quot;user&quot;:{&quot;name&quot;:&quot;tobi&quot;}}&#39; 响应，则 <code>res.body.user.name</code> 将为 &quot;tobi&quot; .同样，&quot;user[name]=tobi&quot; 的 x-www-form-urlencoded 值将产生相同的结果。仅支持一级嵌套。如果您需要更复杂的数据，请改为发送 JSON。</p>
<p>通过重复的键发送数组。 <code>.send({color: [&#39;red&#39;,&#39;blue&#39;]})</code> 会发送 <code>color=red&amp;color=blue</code>。如果您希望数组键的名称中包含 <code>[]</code>，您必须自己添加它，因为 SuperAgent 不会自动添加它。</p>
<h3 id="multipart">Multipart</h3>
<p>Node 客户端通过 <a href="https://github.com/felixge/node-formidable">Formidable</a> 模块支持 _multipart/form-data_。解析 multipart 响应时，对象 <code>res.files</code> 也可供您使用。例如，假设一个请求使用以下 multipart 请求体进行响应：</p>
<pre><code>--whoop
Content-Disposition: attachment; name=&quot;image&quot;; filename=&quot;tobi.png&quot;
Content-Type: image/png

... data here ...
--whoop
Content-Disposition: form-data; name=&quot;name&quot;
Content-Type: text/plain

Tobi
--whoop--
</code></pre>
<p><code>res.body.name</code>的值将为 &quot;Tobi&quot;，并且 <code>res.files.image</code> 将作为包含磁盘路径、文件名和其他属性的 <code>File</code> 对象。</p>
<h3 id="二进制数据">二进制数据</h3>
<p>在浏览器中，您可以使用 <code>.responseType(&#39;blob&#39;)</code> 来请求处理二进制响应体。在 node.js 中运行时不需要此 API。此方法支持的参数值为</p>
<ul>
<li><code>&#39;blob&#39;</code> 赋值给 XmlHTTPRequest 的 <code>responseType</code> 属性</li>
<li><code>&#39;arraybuffer&#39;</code> 赋值给 XmlHTTPRequest 的 responseType 属性</li>
</ul>
<pre><code class="language-js">req.get(&#39;/binary.data&#39;)
  .responseType(&#39;blob&#39;)
  .then(res =&gt; {
    // res.body 将是浏览器原生 Blob 类型
  });
</code></pre>
<p>有关更多信息，请参阅 Mozilla 开发人员网络 <a href="https://developer.mozilla.org/zh-CN/docs/Web/API/XMLHttpRequest/responseType">xhr.responseType 文档</a>。</p>
<h2 id="响应属性">响应属性</h2>
<p>在 <code>Response</code> 对象上设置了许多有用的标志和属性，包括响应文本、解析的响应正文、响应头字段、状态标志等等。</p>
<h3 id="响应文本">响应文本</h3>
<p><code>res.text</code> 属性包含未解析的响应正文字符串。此属性始终存在于客户端 API 中，并且仅当默认情况下节点的 mime 类型与 &quot;text/<em>&quot;、&quot;</em>/json&quot; 或 &quot;x-www-form-urlencoded&quot; 匹配时。原因是为了节省内存，因为缓冲大型正文（例如 multipart 文件或图像）的文本效率极低。要强制缓冲，请参阅&quot;<a href="#%E7%BC%93%E5%86%B2%E5%93%8D%E5%BA%94">缓冲响应</a>&quot;部分。</p>
<h3 id="响应体">响应体</h3>
<p>就像 SuperAgent 可以自动序列化请求数据一样，它也可以自动解析响应体。为 Content-Type 定义解析器时，会对其进行解析，默认情况下包括 &quot;application/json&quot; 和 &quot;application/x-www-form-urlencoded&quot;。然后可以通过 <code>res.body</code> 获得解析的对象。</p>
<h3 id="响应头字段">响应头字段</h3>
<p><code>res.header</code> 包含已解析的响应头字段的对象，字段名称小写，就像 node 做的一样。例如 <code>res.header[&#39;content-length&#39;]</code>。</p>
<h3 id="响应内容类型content-type">响应内容类型(Content-Type)</h3>
<p>Content-Type 响应头是特殊情况，提供 <code>res.type</code>，它没有字符集（也可以有）。例如，&quot;text/html; charset=utf8&quot; 的 <code>Content-Type</code> 将提供 &quot;text/html&quot; 作为 <code>res.type</code>，然后 <code>res.charset</code> 属性将包含 &quot;utf8&quot;。</p>
<h3 id="响应状态">响应状态</h3>
<p>响应状态标志有助于确定请求是否成功，以及其他有用的信息，使 SuperAgent 成为与 RESTful Web 服务交互的理想选择。这些标志当前定义为：</p>
<pre><code> var type = status / 100 | 0;

 // status / class
 res.status = status;
 res.statusType = type;

 // basics
 res.info = 1 == type;
 res.ok = 2 == type;
 res.clientError = 4 == type;
 res.serverError = 5 == type;
 res.error = 4 == type || 5 == type;

 // 语法糖
 res.accepted = 202 == status;
 res.noContent = 204 == status || 1223 == status;
 res.badRequest = 400 == status;
 res.unauthorized = 401 == status;
 res.notAcceptable = 406 == status;
 res.notFound = 404 == status;
 res.forbidden = 403 == status;
</code></pre>
<h2 id="中止请求">中止请求</h2>
<p>要中止请求，只需调用 <code>req.abort()</code> 方法。</p>
<h2 id="超时设定">超时设定</h2>
<p>有时网络和服务器会 &quot;卡住&quot; 并且在接受请求后从不响应。设置超时以避免请求永远等待。</p>
<ul>
<li><p><code>req.timeout({deadline:ms})</code> 或 <code>req.timeout(ms)</code>（其中 <code>ms</code> 是毫秒数 &gt; 0）设置完成整个请求（包括所有上传、重定向、服务器处理时间）的最后期限。如果在这段时间内没有完全下载响应，则请求将被中止。</p>
</li>
<li><p><code>req.timeout({response:ms})</code> 设置等待第一个字节从服务器到达的最长时间，但它不限制整个下载需要多长时间。响应超时应该至少比服务器响应的时间长几秒钟，因为它还包括进行 DNS 查找、TCP/IP 和 TLS 连接的时间，以及上传请求数据的时间。</p>
</li>
</ul>
<p>您应该同时使用 <code>deadline</code> 和 <code>response</code> 超时。通过这种方式，您可以使用较短的响应超时来快速检测无响应的网络，并使用较长的截止时间来为缓慢但可靠的网络上的下载留出时间。请注意，这两个计时器都限制了允许<em>上传</em>附件的时间。如果您要上传文件，请使用长超时。</p>
<pre><code>request
  .get(&#39;/big-file?network=slow&#39;)
  .timeout({
    response: 5000,  // 等待 5 秒让服务器开始发送
    deadline: 60000, // 但允许文件用 1 分钟完成加载。
  })
  .then(res =&gt; {
      /* 及时响应 */
    }, err =&gt; {
      if (err.timeout) { /* 超时! */ } else { /* 其他错误 */ }
  });
</code></pre>
<p>超时错误有个 <code>.timeout</code> 属性。</p>
<h2 id="验证">验证</h2>
<p>在 Node 和浏览器中都可以通过 <code>.auth()</code> 方法进行身份验证：</p>
<pre><code>request
  .get(&#39;http://local&#39;)
  .auth(&#39;tobi&#39;, &#39;learnboost&#39;)
  .then(callback);
</code></pre>
<p>在 <em>Node</em> 客户端中，基本身份验证可以在 URL 中写成 &quot;user:pass&quot;：</p>
<pre><code>request.get(&#39;http://tobi:learnboost@local&#39;).then(callback);
</code></pre>
<p>默认情况下，仅使用<code>基本(Basic)</code>身份验证。在浏览器中，您可以添加 <code>{type:&#39;auto&#39;}</code> 以启用浏览器中内置的所有方法（Digest、NTLM 等）：</p>
<pre><code>request.auth(&#39;digest&#39;, &#39;secret&#39;, {type:&#39;auto&#39;})
</code></pre>
<p><code>auth</code> 方法还支持一种<code>承载类型</code>，以指定基于令牌的身份验证：</p>
<pre><code>request.auth(&#39;my_token&#39;, { type: &#39;bearer&#39; })
</code></pre>
<h2 id="跟随重定向">跟随重定向</h2>
<p>默认情况下将跟随最多 5 个重定向，但是您可以使用 <code>res.redirects(n)</code> 方法指定它：</p>
<pre><code>const response = await request.get(&#39;/some.png&#39;).redirects(2);
</code></pre>
<p>超出限制的重定向被视为错误。使用 <code>.ok(res =&gt; res.status &lt; 400)</code> 将它们读取为成功响应。</p>
<h2 id="全局状态代理程序">全局状态代理程序</h2>
<h3 id="保存-cookie">保存 cookie</h3>
<p>在 Node 中 SuperAgent 默认不保存 cookie，但您可以使用 <code>.agent()</code> 方法创建保存 cookie 的 SuperAgent 副本。每个副本都有一个单独的 cookie 储存器。</p>
<pre><code>const agent = request.agent();
agent
  .post(&#39;/login&#39;)
  .then(() =&gt; {
    return agent.get(&#39;/cookied-page&#39;);
  });
</code></pre>
<p>在浏览器中，cookie 由浏览器自动管理，因此 <code>.agent()</code> 不会隔离 cookie。</p>
<h3 id="多个请求的默认选项">多个请求的默认选项</h3>
<p>代理程序上调用的常规请求方法将用作该代理发出的所有请求的默认值。</p>
<pre><code>const agent = request.agent()
  .use(plugin)
  .auth(shared);

await agent.get(&#39;/with-plugin-and-auth&#39;); // 带有插件和身份验证
await agent.get(&#39;/also-with-plugin-and-auth&#39;); // 也带有插件和身份验证
</code></pre>
<p>代理可以用来设置默认值的完整方法列表是：<code>use</code>、 <code>on</code>、 <code>once</code>、 <code>set</code>、 <code>query</code>、 <code>type</code>、 <code>accept</code>、 <code>auth</code>、 <code>withCredentials</code>、 <code>sortQuery</code>、 <code>retry</code>、 <code>ok</code>、 <code>redirects</code>、 <code>timeout</code>、 <code>buffer</code>、 <code>serialize</code>、 <code>parse</code>、 <code>ca</code>、 <code>key</code>、 <code>pfx</code>、 <code>cert</code>.</p>
<h2 id="管道数据">管道数据</h2>
<p>Node 客户端允许您通过管道将数据传入和传出请求。请注意，使用 <code>.pipe()</code> <strong>代替</strong> <code>.end()/.then()</code> 方法。</p>
<p>管道文件的内容作为请求的例子：</p>
<pre><code>const request = require(&#39;superagent&#39;);
const fs = require(&#39;fs&#39;);

const stream = fs.createReadStream(&#39;path/to/my.json&#39;);
const req = request.post(&#39;/somewhere&#39;);
req.type(&#39;json&#39;);
stream.pipe(req);
</code></pre>
<p>请注意，当您通过管道发送请求时，superagent 使用<a href="https://baike.baidu.com/item/%E5%88%86%E5%9D%97%E4%BC%A0%E8%BE%93%E7%BC%96%E7%A0%81/8359216?fr=aladdin">分块传输编码</a>发送管道数据，并非所有服务器（例如 Python WSGI 服务器）都支持。</p>
<p>或将响应传送到文件：</p>
<pre><code>const stream = fs.createWriteStream(&#39;path/to/my.json&#39;);
const req = request.get(&#39;/some.json&#39;);
req.pipe(stream);
</code></pre>
<p> 不能混合使用管道和回调函数或 promises。请注意，您<strong>不应</strong>尝试通过管道传输 <code>.end()</code> 或 <code>Response</code> 对象的结果：</p>
<pre><code>// 别特么这么写：
const stream = getAWritableStream();
const req = request
  .get(&#39;/some.json&#39;)
  // BAD: 这会将无用信息管道传输到流中并以意想不到的方式失败
  .end((err, this_does_not_work) =&gt; this_does_not_work.pipe(stream))
const req = request
  .get(&#39;/some.json&#39;)
  .end()
  // BAD: 这也不支持，调用 .end 之后调用 .pipe。
  .pipe(nope_its_too_late);
</code></pre>
<p>在 superagent 的<a href="https://github.com/ladjs/superagent/issues/1188">未来版本</a>中，对 <code>pipe()</code> 的不当调用将失败。</p>
<h2 id="多部分请求">多部分请求</h2>
<p>SuperAgent 也非常适合 <em>构建</em> 它提供方法 <code>.attach()</code> 和 <code>.field()</code> 的多部分请求。</p>
<p>当您使用 <code>.field()</code> 或 <code>.attach()</code> 时，您不能使用 <code>.send()</code> 并且您<em>不能</em>设置 <code>Content-Type</code>（将为您设置正确的类型）。</p>
<h3 id="附加文件">附加文件</h3>
<p>要发送文件，请使用 <code>.attach(name, [file], [options])</code>。您可以通过多次调用 <code>.attach</code> 来附加多个文件。参数是：</p>
<ul>
<li><code>name</code> — form 表单中的字段名。</li>
<li><code>file</code> — 带有文件路径的字符串或 <code>Blob/Buffer</code> 对象。</li>
<li><code>options</code> — （可选）自定义文件名的字符串或 <code>{filename: string}</code> 对象。在 Node 中也支持 <code>{contentType: &#39;mime/type&#39;}</code>。在浏览器中创建一个具有适当类型的 <code>Blob</code>。</li>
</ul>
<br>

<pre><code>request
  .post(&#39;/upload&#39;)
  .attach(&#39;image1&#39;, &#39;path/to/felix.jpeg&#39;)
  .attach(&#39;image2&#39;, imageBuffer, &#39;luna.jpeg&#39;)
  .field(&#39;caption&#39;, &#39;My cats&#39;)
  .then(callback);
</code></pre>
<h3 id="字段值">字段值</h3>
<p>与 HTML 中的表单字段非常相似，您可以使用 <code>.field(name, value)</code> 和 <code>.field({name: value})</code> 设置字段值。假设您想上传一些带有您的姓名和电子邮件的图片，您的请求可能如下所示：</p>
<pre><code> request
   .post(&#39;/upload&#39;)
   .field(&#39;user[name]&#39;, &#39;Tobi&#39;)
   .field(&#39;user[email]&#39;, &#39;tobi@learnboost.com&#39;)
   .field(&#39;friends[]&#39;, [&#39;loki&#39;, &#39;jane&#39;])
   .attach(&#39;image&#39;, &#39;path/to/tobi.png&#39;)
   .then(callback);
</code></pre>
<h2 id="压缩">压缩</h2>
<p>node 客户端支持压缩过的响应，最重要的是，您无需执行任何操作！它就能用。</p>
<h2 id="缓冲响应">缓冲响应</h2>
<p>要强制将响应主体缓冲为 <code>res.text</code>，您可以调用 <code>req.buffer()</code>。要取消对文本响应（例如 &quot;text/plain&quot;、&quot;text/html&quot; 等）的默认缓冲，您可以调用 <code>req.buffer(false)</code>。 </p>
<p>当缓冲提供 <code>res.buffered</code> 标志时，您可以使用它在同一个回调中处理缓冲和非缓冲响应。</p>
<h2 id="cors">CORS</h2>
<p>出于安全原因，浏览器将阻止跨域请求，除非服务器选择使用 CORS 标头。浏览器还会发出额外的 <strong>OPTIONS</strong> 请求来检查服务器允许哪些 HTTP 标头和方法。<a href="https://developer.mozilla.org/zh-CN/docs/Web/HTTP/CORS">阅读有关 CORS 的更多信息</a>。</p>
<p><code>.withCredentials()</code> 方法支持从源发送 cookie，但仅当 Access-Control-Allow-Origin <em>不是</em> 通配符 (&quot;*&quot;) 且 <code>Access-Control-Allow-Credentials</code> 为 &quot;true&quot; 时。</p>
<pre><code>request
  .get(&#39;https://api.example.com:4001/&#39;)
  .withCredentials()
  .then(res =&gt; {
    assert.equal(200, res.status);
    assert.equal(&#39;tobi&#39;, res.text);
  })
</code></pre>
<h2 id="错误处理">错误处理</h2>
<p>您的回调函数将始终传递两个参数：错误和响应。如果没有发生错误，第一个参数将为<code>null</code>：</p>
<pre><code>request
 .post(&#39;/upload&#39;)
 .attach(&#39;image&#39;, &#39;path/to/tobi.png&#39;)
 .then(res =&gt; {

 });
</code></pre>
<p>还会触发&quot;错误&quot;事件，您可以监听：</p>
<pre><code>request
  .post(&#39;/upload&#39;)
  .attach(&#39;image&#39;, &#39;path/to/tobi.png&#39;)
  .on(&#39;error&#39;, handle)
  .then(res =&gt; {

  });
</code></pre>
<p>请注意，<strong>默认情况下，superagent 会考虑 4xx 和 5xx 响应（以及未处理的 3xx 响应）视为错误</strong>。例如，如果您收到 <code>304 Not modified</code>、<code>403 Forbidden</code> 或 <code>500 Internal server</code> 错误响应，则此状态信息将通过 <code>err.status</code> 提供。来自此类响应的错误还包含一个 <code>err.response</code> 字段，其中包含&quot;<a href="#%E5%93%8D%E5%BA%94%E5%B1%9E%E6%80%A7">响应属性</a>&quot;中提到的所有属性。该库以这种方式运行以处理需要成功响应并将 HTTP 错误状态代码视为错误的常见情况，同时仍允许围绕特定错误条件进行自定义逻辑。</p>
<p>网络故障、超时和其他不产生响应的错误将不包含 <code>err.status</code> 或 <code>err.response</code> 字段。</p>
<p>如果您希望处理 404 或其他 HTTP 错误响应，您可以查询 <code>err.status</code> 属性。当发生 HTTP 错误（4xx 或 5xx 响应）时， <code>res.error</code> 属性是一个 <code>Error</code> 对象，这允许您执行以下检查：</p>
<pre><code>if (err &amp;&amp; err.status === 404) {
  alert(&#39;oh no &#39; + res.body.message);
}
else if (err) {
  // 所有其他需要处理的错误类型
}
</code></pre>
<p>或者，您可以使用 <code>.ok(callback)</code> 方法来确定响应是否为错误。 <code>ok</code> 函数的回调函数获得响应，如果响应应该被解释为成功，则返回 true。</p>
<pre><code>request.get(&#39;/404&#39;)
  .ok(res =&gt; res.status &lt; 500)
  .then(response =&gt; {
    // 将 404 页面作为成功响应
  })
</code></pre>
<h2 id="进度跟踪">进度跟踪</h2>
<p>SuperAgent 在上传和下载大文件时触发 <code>progress</code> 事件。</p>
<pre><code>request.post(url)
  .attach(&#39;field_name&#39;, file)
  .on(&#39;progress&#39;, event =&gt; {
    /* event的值：
    {
      direction: &quot;upload&quot; or &quot;download&quot;
      percent: 0 to 100 // 如果文件大小未知，可能会没有
      total: // 总文件大小，可能没有
      loaded: // 到目前为止下载或上传的字节数
    } */
  })
  .then()
</code></pre>
<h2 id="在本地主机上测试">在本地主机上测试</h2>
<h3 id="强制连接特定-ip-地址">强制连接特定 IP 地址</h3>
<p>在 Node.js 中，可以忽略 DNS 解析并使用 <code>.connect()</code> 方法将所有请求定向到特定 IP 地址。例如，此请求将转到 localhost 而不是 <code>example.com</code>：</p>
<pre><code>const res = await request.get(&quot;http://example.com&quot;).connect(&quot;127.0.0.1&quot;);
</code></pre>
<p>因为请求可能被重定向，所以可以指定多个主机名和多个 IP，以及一个特殊的 <code>*</code> 作为后备（注意：不支持其他通配符）。请求将保留其 <code>Host</code> 请求头的原始值。</p>
<pre><code>const res = await request.get(&quot;http://redir.example.com:555&quot;)
  .connect({
    &quot;redir.example.com&quot;: &quot;127.0.0.1&quot;, // redir.example.com:555 将使用 127.0.0.1:555
    &quot;www.example.com&quot;: false, // 不覆盖这个；正常使用 DNS
    &quot;mapped.example.com&quot;: { host: &quot;127.0.0.1&quot;, port: 8080}, // mapped.example.com:* 将使用 127.0.0.1:8080
    &quot;*&quot;: &quot;proxy.example.com&quot;, // 所有其他请求都将发送到该主机
  });
</code></pre>
<h3 id="忽略本地主机上损坏不安全的-https">忽略本地主机上损坏/不安全的 HTTPS</h3>
<p>在 Node.js 中，当 HTTPS 配置错误且不安全（例如，使用自签名证书而<em>不指定</em>自己的 <code>.ca()</code>）时，仍然可以通过调用 <code>.trustLocalhost()</code> 来允许对 <code>localhost</code> 的请求：</p>
<pre><code>const res = await request.get(&quot;https://localhost&quot;).trustLocalhost()
</code></pre>
<p>与 <code>.connect(&quot;127.0.0.1&quot;)</code> 一起，这可用于强制将对任何域的 HTTPS 请求重新路由到 <code>localhost</code>。</p>
<p>忽略本地主机上损坏的 HTTPS 通常是安全的，因为环回接口不会暴露给不受信任的网络。信任 <code>localhost</code> 可能会成为未来的默认设置。使用 <code>.trustLocalhost(false)</code> 强制检查 <code>127.0.0.1</code> 的可靠性。</p>
<p>当向任何其他 IP 发出请求时，我们故意不支持禁用 HTTPS 安全性，因为这些选项最终被滥用为 HTTPS 问题的快速&quot;修复&quot;。您可以从 <a href="https://certbot.eff.org">Let&#39;s Encrypt</a> 获得免费的 HTTPS 证书或设置您自己的 CA (<code>.ca(ca_public_pem)</code>) 以使您的自签名证书受信任。</p>
<h2 id="promise-和生成器函数支持">Promise 和生成器函数支持</h2>
<p>SuperAgent 的请求是一个 &quot;thenable&quot; 对象(带有then方法的对象)，它与 JavaScript Promise 和 <code>async/await</code> 语法兼容。</p>
<pre><code>const res = await request.get(url);
</code></pre>
<p>如果你使用 Promise，<strong>不要</strong>调用 <code>.end()</code> 或 <code>.pipe()</code>。任何使用 <code>.then()</code> 或 <code>await</code> 都会禁用所有其他使用请求的方式。 像 <a href="https://github.com/tj/co">co</a> 这样的库或像 <a href="https://github.com/koajs/koa">koa</a> 这样的 web 框架可以在任何 SuperAgent 方法上 <code>yield</code>：</p>
<pre><code>const req = request
  .get(&#39;http://local&#39;)
  .auth(&#39;tobi&#39;, &#39;learnboost&#39;);
const res = yield req;
</code></pre>
<p>请注意，SuperAgent 期望全局 <code>Promise</code> 对象存在。您需要一个 polyfill 才能在 Internet Explorer 或 Node.js 0.10 中使用 Promise。</p>
<h2 id="浏览器和-node-版本">浏览器和 node 版本</h2>
<p>SuperAgent 有两种实现：一种用于 Web 浏览器（使用 XHR），另一种用于 Node.JS（使用核心 http 模块）。默认情况下，Browserify 和 WebPack 将选择浏览器版本。 </p>
<p>如果要使用 WebPack 为 Node.JS 编译代码，您<em>必须</em>在其配置中指定<a href="https://webpack.github.io/docs/configuration.html#target">node target</a>。</p>
<h3 id="在-electron-中使用浏览器版本">在 electron 中使用浏览器版本</h3>
<p><a href="https://electron.atom.io/">Electron</a> 开发人员报告说，如果您希望使用浏览器版本的 SuperAgent 而不是 Node 版本，您可以 <code>require(&#39;superagent/superagent&#39;)</code>。这样您的请求将显示在 Chrome 开发者工具的&quot;网络(Network)&quot;选项卡中。请注意，自动化测试套件未涵盖此环境，也未得到官方支持。</p>
<h2 id="使用代理发送请求">使用代理发送请求</h2>
<p>可以使用另一个作者的 <a href="https://www.npmjs.com/package/superagent-proxy">superagent-proxy</a> 模块</p>
<h2 id="翻译说明">翻译说明</h2>
<p>文档全部内容都是根据原英文文档翻译的，译者也没水平，所以如果有错误还请指出</p>
    </div>
    <a href="http://github.com/ladjs/superagent"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://s3.amazonaws.com/github/ribbons/forkme_right_white_ffffff.png" alt="Fork me on GitHub"></a>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.0/jquery.min.js"></script>
    <script>
      $('code').each(function(){
        $(this).html(highlight($(this).text()));
      });

      function highlight(js) {
        return js
          .replace(/</g, '&lt;')
          .replace(/>/g, '&gt;')
          .replace(/('.*?')/gm, '<span class="string">$1</span>')
          .replace(/(\d+\.\d+)/gm, '<span class="number">$1</span>')
          .replace(/(\d+)/gm, '<span class="number">$1</span>')
          .replace(/\bnew *(\w+)/gm, '<span class="keyword">new</span> <span class="init">$1</span>')
          .replace(/\b(function|new|throw|return|var|if|else)\b/gm, '<span class="keyword">$1</span>')
      }
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/tocbot/3.0.0/tocbot.js"></script>
    <script>
      // Only use tocbot for main docs, not test docs
      if (document.querySelector('#superagent')) {
        tocbot.init({
          // Where to render the table of contents.
          tocSelector: '#menu',
          // Where to grab the headings to build the table of contents.
          contentSelector: '#content',
          // Which headings to grab inside of the contentSelector element.
          headingSelector: 'h2',
          smoothScroll: false
        });
      }
    </script>
  </body>
</html>
```

## File: `docs/zh_CN/index.md`
```markdown
# SuperAgent

SuperAgent是轻量级的渐进式ajax API，具有灵活性、可读性和较低的学习曲线。 它也适用于Node.js!  

     request
       .post('/api/pet')
       .send({ name: 'Manny', species: 'cat' })
       .set('X-API-Key', 'foobar')
       .set('Accept', 'application/json')
       .then(res => {
          alert('yay got ' + JSON.stringify(res.body));
       });

## 测试文档 

[**English**](/superagent/)

下面的[测试文档](../test.html)是用[Mocha](https://mochajs.org/)的"文档"报告器生成的，并直接反映了测试套件。 这提供了额外的文档来源。  

## 基本请求

可以通过调用 `request` 对象上的适当方法来发起请求，然后调用 `.then()` ( 或 `.end()` 或 [`await`](#promise-and-generator-support) )发送请求。例如一个简单的 __GET__ 请求：

     request
       .get('/search')
       .then(res => {
          // res.body, res.headers, res.status
       })
       .catch(err => {
          // err.message, err.response
       });

HTTP 方法也可以作为字符串传递：  
译者注：大小写皆可。

    request('GET', '/search').then(success, failure);

旧式回调也受支持，但不推荐使用。您可以调用 `.end()` *代替* `.then()`：

    request('GET', '/search').end(function(err, res){
      if (res.ok) {}
    });

可以使用绝对 URL。在 Web 浏览器中，绝对 URL 仅在服务器实现 [CORS](#cors) 时才有效。

     request
       .get('https://example.com/search')
       .then(res => {

       });

__Node__ 客户端支持向 [Unix 域套接字](https://zh.wikipedia.org/wiki/Unix%E5%9F%9F%E5%A5%97%E6%8E%A5%E5%AD%97) 发出请求：

    // pattern: https?+unix://SOCKET_PATH/REQUEST_PATH
    //在套接字路径中将 `%2F` 用作 `/`
    try {
      const res = await request
        .get('http+unix://%2Fabsolute%2Fpath%2Fto%2Funix.sock/search');
      // res.body, res.headers, res.status
    } catch(err) {
      // err.message, err.response
    }

__DELETE__、__HEAD__、__PATCH__、__POST__ 和 __PUT__ 请求也可以使用，只需更改方法名称：

    request
      .head('/favicon.ico')
      .then(res => {

      });

__DELETE__ 也可以用 `.del()` 调用以与旧版 IE 兼容，其中 `delete` 是保留字。

HTTP 方法默认为 __GET__，因此如果您愿意，以下代码是有效的：

     request('/search', (err, res) => {

     });

## 使用 HTTP/2

要使用 HTTP/2 协议（没有 HTTP/1.x 后备），请使用 `.http2()` 方法。

    const request = require('superagent');
    const res = await request
      .get('https://example.com/h2')
      .http2();

## 设置请求头字段

设置请求头字段很简单，调用 `.set()` 时传入字段名称和值：

     request
       .get('/search')
       .set('API-Key', 'foobar')
       .set('Accept', 'application/json')
       .then(callback);

您还可以在一次调用中传入一个对象来设置多个字段：

     request
       .get('/search')
       .set({ 'API-Key': 'foobar', Accept: 'application/json' })
       .then(callback);

## `GET` 请求

`.query()` 方法接受对象，当与 __GET__ 方法一起使用时将形成一个查询字符串。以下将产生路径 `/search?query=Manny&range=1..5&order=desc`。
译者注：`.query()` 方法的参数不需要提前进行url编码。

     request
       .get('/search')
       .query({ query: 'Manny' })
       .query({ range: '1..5' })
       .query({ order: 'desc' })
       .then(res => {

       });

或传入单个对象：

    request
      .get('/search')
      .query({ query: 'Manny', range: '1..5', order: 'desc' })
      .then(res => {

      });

`.query()` 方法也可以接受字符串。

      request
        .get('/querystring')
        .query('search=Manny&range=1..5')
        .then(res => {

        });

或者一个个加入：

      request
        .get('/querystring')
        .query('search=Manny')
        .query('range=1..5')
        .then(res => {

        });

## `HEAD` 请求

您还可以对 __HEAD__ 请求使用 .query() 方法。以下将生成路径 `/users?email=joe@smith.com`。

      request
        .head('/users')
        .query({ email: 'joe@smith.com' })
        .then(res => {

        });

## `POST` / `PUT` 请求

一个典型的 JSON __POST__ 请求可能如下所示，我们适当地设置 `Content-Type` 请求头字段，并"写入"一些数据，在本例中只是一个 JSON 字符串。

      request.post('/user')
        .set('Content-Type', 'application/json')
        .send('{"name":"tj","pet":"tobi"}')
        .then(callback)
        .catch(errorCallback)

由于 JSON 无疑是最常见的，所以它是 _默认_ 的！下面的例子与前面的例子是等价的。

      request.post('/user')
        .send({ name: 'tj', pet: 'tobi' })
        .then(callback, errorCallback)

或者调用多个 `.send()`：

      request.post('/user')
        .send({ name: 'tj' })
        .send({ pet: 'tobi' })
        .then(callback, errorCallback)

默认情况下，发送字符串会将 `Content-Type` 设置为 `application/x-www-form-urlencoded`，多个调用将用 `&` 连接，这里产生 `name=tj&pet=tobi`：

      request.post('/user')
        .send('name=tj')
        .send('pet=tobi')
        .then(callback, errorCallback);

SuperAgent 格式是可扩展的，但默认情况下支持 "json" 和 "form"。要将数据作为 `application/x-www-form-urlencoded` 发送，只需在调用 `.type()` 时传入 "form"，默认为 "json"。此 __POST__ 请求的请求体将是 "name=tj&pet=tobi"。

      request.post('/user')
        .type('form')
        .send({ name: 'tj' })
        .send({ pet: 'tobi' })
        .then(callback, errorCallback)

还支持发送 [`FormData`](https://developer.mozilla.org/zh-CN/docs/Web/API/FormData/FormData) 对象。以下示例将 __POST__ 请求由 id="myForm" 标识的 HTML 表单的内容：

      request.post('/user')
        .send(new FormData(document.getElementById('myForm')))
        .then(callback, errorCallback)

## 设置 `Content-Type`

显而易见的解决方案是使用 `.set()` 方法：

     request.post('/user')
       .set('Content-Type', 'application/json')

`.type()` 方法也可以作为简写，接受带有类型/子类型的规范化 [MIME 类型](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Basics_of_HTTP/MIME_types) 名称，或者只是扩展名，例如"xml"、"json"、"png"等：

     request.post('/user')
       .type('application/json')

     request.post('/user')
       .type('json')

     request.post('/user')
       .type('png')

## 序列化请求体

SuperAgent 将自动序列化 JSON 和表单。您也可以为其他类型设置自动序列化：

```js
request.serialize['application/xml'] = function (obj) {
    return '从obj生成的字符串';
};

// 接下来，内容类型为 "application/xml" 的所有请求都将自动序列化
```
如果您想以自定义格式发送 数据体(payload)，您可以根据每个请求将内置序列化替换为 `.serialize()` 方法：

```js
request
    .post('/user')
    .send({foo: 'bar'})
    .serialize(obj => {
        return '从obj生成的字符串';
    });
```
## 重试请求

如果请求暂时失败或可能是网络连接不稳定造成的失败，且当给定 `.retry()` 方法时，SuperAgent 将自动重试请求。

此方法有两个可选参数：重试次数（默认为 `1`）和回调函数。它在每次重试之前调用 callback(err, res) 。回调可以返回 `true`/`false` 以控制是否应重试请求（但始终应该用最大重试次数）。
     request
       .get('https://example.com/search')
       .retry(2) // 或者：
       .retry(2, callback) // 二选一
       .then(finished);
       .catch(failed);

`.retry()` 仅用于[*幂等*](https://baike.baidu.com/item/%E5%B9%82%E7%AD%89/8600688?fr=aladdin)请求（即到达服务器的多个请求不会导致重复购买等不良副作用）。

默认情况下会尝试所有请求方法（这意味着如果您不希望重试 POST 请求，则需要传递自定义的重试回调函数）。

默认情况下会重试以下状态代码：

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

默认情况下会重试以下错误代码：

* `'ETIMEDOUT'`
* `'ECONNRESET'`
* `'EADDRINUSE'`
* `'ECONNREFUSED'`
* `'EPIPE'`
* `'ENOTFOUND'`
* `'ENETUNREACH'`
* `'EAI_AGAIN'`

## 设置 Accept

与 `.type()` 方法类似，也可以通过简写方法 `.accept()` 设置 `Accept` 请求头。方便起见，其中还引用了 `request.types`，允许您将完整的规范化 [MIME 类型](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Basics_of_HTTP/MIME_types) 名称指定为`类型/子类型`，或将扩展后缀形式指定为"xml"、"json"、"png"等：

     request.get('/user')
       .accept('application/json')

     request.get('/user')
       .accept('json')

     request.post('/user')
       .accept('png')

### Facebook 和 Accept JSON

如果您正在调用 Facebook 的 API，请务必在您的请求中发送 `Accept: application/json` 请求头。如果你不这样做，Facebook 会回复 `Content-Type: text/javascript; charset=UTF-8`，SuperAgent 将不会解析，因此 `res.body` 将是未定义的。您可以使用 `req.accept('json')` 或 `req.header('Accept', 'application/json')` 来执行此操作。有关详细信息，请参阅 [issue 1078](https://github.com/ladjs/superagent/issues/1078)。

## 查询字符串(Query strings)

`req.query(obj)` 是一种可用于构建查询字符串的方法。例如在 __POST__ 上增加 `?format=json&dest=/login`：

    request
      .post('/')
      .query({ format: 'json' })
      .query({ dest: '/login' })
      .send({ post: 'data', here: 'wahoo' })
      .then(callback);

默认情况下，查询字符串不按任何特定顺序组装。可以使用 `req.sortQuery()` 启用 ASCIIbetically 排序的查询字符串。您还可以使用 `req.sortQuery(myComparisonFn)` 提供自定义排序比较函数。比较函数应该接受 2 个参数并返回一个负/零/正整数。

```js
 // 默认顺序
 request.get('/user')
   .query('name=Nick')
   .query('search=Manny')
   .sortQuery()
   .then(callback)

 // 自定义排序函数
 request.get('/user')
   .query('name=Nick')
   .query('search=Manny')
   .sortQuery((a, b) => a.length - b.length)
   .then(callback)
```

## TLS 选项

在 Node.js 中，SuperAgent 支持配置 HTTPS 请求的方法：

- `.ca()`: 将 CA 证书设置为信任
- `.cert()`: 设置客户端证书链
- `.key()`: 设置客户端私钥
- `.pfx()`: 设置客户端 PFX 或 PKCS12 编码的私钥和证书链
- `.disableTLSCerts()`: 不拒绝过期或无效的 TLS 证书。在内部设置 `rejectUnauthorized=true`。*请注意，此方法允许中间人攻击。*

有关更多信息，请参阅 Node.js [https.request 文档](http://nodejs.cn/api/https.html#httpsrequesturl-options-callback)。

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

## 解析响应体

SuperAgent将为您解析已知的响应主体数据，目前支持`application/x-www-form-urlencoded`，`application/json`，以及`multipart/form data`。您可以设置自动解析其他响应主体数据：

```js
//浏览器
request.parse['application/xml'] = function (str) {
    return {'object': '从str解析的'};
};

//node
request.parse['application/xml'] = function (res, cb) {
    //解析响应文本并在此处设置res.body

    cb(null, res);
};

//接下来，将自动解析 'application/xml' 类型的响应
```

您可以使用 `.buffer(true).parse(fn)` 方法设置自定义解析器（优先于内置解析器）。如果未启用响应缓冲 (`.buffer(false)`)，则将触发`响应(response)`事件而无需等待正文解析器完成，因此 `response.body` 将不可用。

### JSON / Urlencoded

属性 `res.body` 是解析后的对象，例如，如果请求以 JSON 字符串 '{"user":{"name":"tobi"}}' 响应，则 `res.body.user.name` 将为 "tobi" .同样，"user[name]=tobi" 的 x-www-form-urlencoded 值将产生相同的结果。仅支持一级嵌套。如果您需要更复杂的数据，请改为发送 JSON。

通过重复的键发送数组。 `.send({color: ['red','blue']})` 会发送 `color=red&color=blue`。如果您希望数组键的名称中包含 `[]`，您必须自己添加它，因为 SuperAgent 不会自动添加它。

### Multipart

Node 客户端通过 [Formidable](https://github.com/felixge/node-formidable) 模块支持 _multipart/form-data_。解析 multipart 响应时，对象 `res.files` 也可供您使用。例如，假设一个请求使用以下 multipart 请求体进行响应：

    --whoop
    Content-Disposition: attachment; name="image"; filename="tobi.png"
    Content-Type: image/png

    ... data here ...
    --whoop
    Content-Disposition: form-data; name="name"
    Content-Type: text/plain

    Tobi
    --whoop--

`res.body.name`的值将为 "Tobi"，并且 `res.files.image` 将作为包含磁盘路径、文件名和其他属性的 `File` 对象。


### 二进制数据

在浏览器中，您可以使用 `.responseType('blob')` 来请求处理二进制响应体。在 node.js 中运行时不需要此 API。此方法支持的参数值为

- `'blob'` 赋值给 XmlHTTPRequest 的 `responseType` 属性
- `'arraybuffer'` 赋值给 XmlHTTPRequest 的 responseType 属性

```js
req.get('/binary.data')
  .responseType('blob')
  .then(res => {
    // res.body 将是浏览器原生 Blob 类型
  });
```

有关更多信息，请参阅 Mozilla 开发人员网络 [xhr.responseType 文档](https://developer.mozilla.org/zh-CN/docs/Web/API/XMLHttpRequest/responseType)。

## 响应属性

在 `Response` 对象上设置了许多有用的标志和属性，包括响应文本、解析的响应正文、响应头字段、状态标志等等。

### 响应文本

`res.text` 属性包含未解析的响应正文字符串。此属性始终存在于客户端 API 中，并且仅当默认情况下节点的 mime 类型与 "text/*"、"*/json" 或 "x-www-form-urlencoded" 匹配时。原因是为了节省内存，因为缓冲大型正文（例如 multipart 文件或图像）的文本效率极低。要强制缓冲，请参阅"[缓冲响应](#缓冲响应)"部分。

### 响应体

就像 SuperAgent 可以自动序列化请求数据一样，它也可以自动解析响应体。为 Content-Type 定义解析器时，会对其进行解析，默认情况下包括 "application/json" 和 "application/x-www-form-urlencoded"。然后可以通过 `res.body` 获得解析的对象。

### 响应头字段

`res.header` 包含已解析的响应头字段的对象，字段名称小写，就像 node 做的一样。例如 `res.header['content-length']`。

### 响应内容类型(Content-Type)

Content-Type 响应头是特殊情况，提供 `res.type`，它没有字符集（也可以有）。例如，"text/html; charset=utf8" 的 `Content-Type` 将提供 "text/html" 作为 `res.type`，然后 `res.charset` 属性将包含 "utf8"。

### 响应状态

响应状态标志有助于确定请求是否成功，以及其他有用的信息，使 SuperAgent 成为与 RESTful Web 服务交互的理想选择。这些标志当前定义为：

     var type = status / 100 | 0;

     // status / class
     res.status = status;
     res.statusType = type;

     // basics
     res.info = 1 == type;
     res.ok = 2 == type;
     res.clientError = 4 == type;
     res.serverError = 5 == type;
     res.error = 4 == type || 5 == type;

     // 语法糖
     res.accepted = 202 == status;
     res.noContent = 204 == status || 1223 == status;
     res.badRequest = 400 == status;
     res.unauthorized = 401 == status;
     res.notAcceptable = 406 == status;
     res.notFound = 404 == status;
     res.forbidden = 403 == status;

## 中止请求

要中止请求，只需调用 `req.abort()` 方法。

## 超时设定

有时网络和服务器会 "卡住" 并且在接受请求后从不响应。设置超时以避免请求永远等待。

  * `req.timeout({deadline:ms})` 或 `req.timeout(ms)`（其中 `ms` 是毫秒数 > 0）设置完成整个请求（包括所有上传、重定向、服务器处理时间）的最后期限。如果在这段时间内没有完全下载响应，则请求将被中止。

  * `req.timeout({response:ms})` 设置等待第一个字节从服务器到达的最长时间，但它不限制整个下载需要多长时间。响应超时应该至少比服务器响应的时间长几秒钟，因为它还包括进行 DNS 查找、TCP/IP 和 TLS 连接的时间，以及上传请求数据的时间。

您应该同时使用 `deadline` 和 `response` 超时。通过这种方式，您可以使用较短的响应超时来快速检测无响应的网络，并使用较长的截止时间来为缓慢但可靠的网络上的下载留出时间。请注意，这两个计时器都限制了允许*上传*附件的时间。如果您要上传文件，请使用长超时。

    request
      .get('/big-file?network=slow')
      .timeout({
        response: 5000,  // 等待 5 秒让服务器开始发送
        deadline: 60000, // 但允许文件用 1 分钟完成加载。
      })
      .then(res => {
          /* 及时响应 */
        }, err => {
          if (err.timeout) { /* 超时! */ } else { /* 其他错误 */ }
      });

超时错误有个 `.timeout` 属性。

## 验证

在 Node 和浏览器中都可以通过 `.auth()` 方法进行身份验证：

    request
      .get('http://local')
      .auth('tobi', 'learnboost')
      .then(callback);


在 _Node_ 客户端中，基本身份验证可以在 URL 中写成 "user:pass"：

    request.get('http://tobi:learnboost@local').then(callback);

默认情况下，仅使用`基本(Basic)`身份验证。在浏览器中，您可以添加 `{type:'auto'}` 以启用浏览器中内置的所有方法（Digest、NTLM 等）：

    request.auth('digest', 'secret', {type:'auto'})

`auth` 方法还支持一种`承载类型`，以指定基于令牌的身份验证：

    request.auth('my_token', { type: 'bearer' })

## 跟随重定向

默认情况下将跟随最多 5 个重定向，但是您可以使用 `res.redirects(n)` 方法指定它：

    const response = await request.get('/some.png').redirects(2);

超出限制的重定向被视为错误。使用 `.ok(res => res.status < 400)` 将它们读取为成功响应。

## 全局状态代理程序

### 保存 cookie

在 Node 中 SuperAgent 默认不保存 cookie，但您可以使用 `.agent()` 方法创建保存 cookie 的 SuperAgent 副本。每个副本都有一个单独的 cookie 储存器。

    const agent = request.agent();
    agent
      .post('/login')
      .then(() => {
        return agent.get('/cookied-page');
      });

在浏览器中，cookie 由浏览器自动管理，因此 `.agent()` 不会隔离 cookie。

### 多个请求的默认选项

代理程序上调用的常规请求方法将用作该代理发出的所有请求的默认值。

    const agent = request.agent()
      .use(plugin)
      .auth(shared);

    await agent.get('/with-plugin-and-auth'); // 带有插件和身份验证
    await agent.get('/also-with-plugin-and-auth'); // 也带有插件和身份验证

代理可以用来设置默认值的完整方法列表是：`use`、 `on`、 `once`、 `set`、 `query`、 `type`、 `accept`、 `auth`、 `withCredentials`、 `sortQuery`、 `retry`、 `ok`、 `redirects`、 `timeout`、 `buffer`、 `serialize`、 `parse`、 `ca`、 `key`、 `pfx`、 `cert`.

## 管道数据

Node 客户端允许您通过管道将数据传入和传出请求。请注意，使用 `.pipe()` **代替** `.end()/.then()` 方法。

管道文件的内容作为请求的例子：

    const request = require('superagent');
    const fs = require('fs');

    const stream = fs.createReadStream('path/to/my.json');
    const req = request.post('/somewhere');
    req.type('json');
    stream.pipe(req);

请注意，当您通过管道发送请求时，superagent 使用[分块传输编码](https://baike.baidu.com/item/%E5%88%86%E5%9D%97%E4%BC%A0%E8%BE%93%E7%BC%96%E7%A0%81/8359216?fr=aladdin)发送管道数据，并非所有服务器（例如 Python WSGI 服务器）都支持。

或将响应传送到文件：

    const stream = fs.createWriteStream('path/to/my.json');
    const req = request.get('/some.json');
    req.pipe(stream);

 不能混合使用管道和回调函数或 promises。请注意，您**不应**尝试通过管道传输 `.end()` 或 `Response` 对象的结果：

    // 别特么这么写：
    const stream = getAWritableStream();
    const req = request
      .get('/some.json')
      // BAD: 这会将无用信息管道传输到流中并以意想不到的方式失败
      .end((err, this_does_not_work) => this_does_not_work.pipe(stream))
    const req = request
      .get('/some.json')
      .end()
      // BAD: 这也不支持，调用 .end 之后调用 .pipe。
      .pipe(nope_its_too_late);

在 superagent 的[未来版本](https://github.com/ladjs/superagent/issues/1188)中，对 `pipe()` 的不当调用将失败。

## 多部分请求

SuperAgent 也非常适合 _构建_ 它提供方法 `.attach()` 和 `.field()` 的多部分请求。

当您使用 `.field()` 或 `.attach()` 时，您不能使用 `.send()` 并且您*不能*设置 `Content-Type`（将为您设置正确的类型）。

### 附加文件

要发送文件，请使用 `.attach(name, [file], [options])`。您可以通过多次调用 `.attach` 来附加多个文件。参数是：

 * `name` — form 表单中的字段名。
 * `file` — 带有文件路径的字符串或 `Blob/Buffer` 对象。
 * `options` — （可选）自定义文件名的字符串或 `{filename: string}` 对象。在 Node 中也支持 `{contentType: 'mime/type'}`。在浏览器中创建一个具有适当类型的 `Blob`。
 
<br>

    request
      .post('/upload')
      .attach('image1', 'path/to/felix.jpeg')
      .attach('image2', imageBuffer, 'luna.jpeg')
      .field('caption', 'My cats')
      .then(callback);

### 字段值

与 HTML 中的表单字段非常相似，您可以使用 `.field(name, value)` 和 `.field({name: value})` 设置字段值。假设您想上传一些带有您的姓名和电子邮件的图片，您的请求可能如下所示：

     request
       .post('/upload')
       .field('user[name]', 'Tobi')
       .field('user[email]', 'tobi@learnboost.com')
       .field('friends[]', ['loki', 'jane'])
       .attach('image', 'path/to/tobi.png')
       .then(callback);

## 压缩

node 客户端支持压缩过的响应，最重要的是，您无需执行任何操作！它就能用。

## 缓冲响应

要强制将响应主体缓冲为 `res.text`，您可以调用 `req.buffer()`。要取消对文本响应（例如 "text/plain"、"text/html" 等）的默认缓冲，您可以调用 `req.buffer(false)`。 

当缓冲提供 `res.buffered` 标志时，您可以使用它在同一个回调中处理缓冲和非缓冲响应。

## CORS

出于安全原因，浏览器将阻止跨域请求，除非服务器选择使用 CORS 标头。浏览器还会发出额外的 __OPTIONS__ 请求来检查服务器允许哪些 HTTP 标头和方法。[阅读有关 CORS 的更多信息](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/CORS)。

`.withCredentials()` 方法支持从源发送 cookie，但仅当 Access-Control-Allow-Origin _不是_ 通配符 ("*") 且 `Access-Control-Allow-Credentials` 为 "true" 时。

    request
      .get('https://api.example.com:4001/')
      .withCredentials()
      .then(res => {
        assert.equal(200, res.status);
        assert.equal('tobi', res.text);
      })

## 错误处理

您的回调函数将始终传递两个参数：错误和响应。如果没有发生错误，第一个参数将为`null`：

    request
     .post('/upload')
     .attach('image', 'path/to/tobi.png')
     .then(res => {

     });

还会触发"错误"事件，您可以监听：

    request
      .post('/upload')
      .attach('image', 'path/to/tobi.png')
      .on('error', handle)
      .then(res => {

      });

请注意，**默认情况下，superagent 会考虑 4xx 和 5xx 响应（以及未处理的 3xx 响应）视为错误**。例如，如果您收到 `304 Not modified`、`403 Forbidden` 或 `500 Internal server` 错误响应，则此状态信息将通过 `err.status` 提供。来自此类响应的错误还包含一个 `err.response` 字段，其中包含"[响应属性](#响应属性)"中提到的所有属性。该库以这种方式运行以处理需要成功响应并将 HTTP 错误状态代码视为错误的常见情况，同时仍允许围绕特定错误条件进行自定义逻辑。

网络故障、超时和其他不产生响应的错误将不包含 `err.status` 或 `err.response` 字段。

如果您希望处理 404 或其他 HTTP 错误响应，您可以查询 `err.status` 属性。当发生 HTTP 错误（4xx 或 5xx 响应）时， `res.error` 属性是一个 `Error` 对象，这允许您执行以下检查：

    if (err && err.status === 404) {
      alert('oh no ' + res.body.message);
    }
    else if (err) {
      // 所有其他需要处理的错误类型
    }

或者，您可以使用 `.ok(callback)` 方法来确定响应是否为错误。 `ok` 函数的回调函数获得响应，如果响应应该被解释为成功，则返回 true。

    request.get('/404')
      .ok(res => res.status < 500)
      .then(response => {
        // 将 404 页面作为成功响应
      })

## 进度跟踪

SuperAgent 在上传和下载大文件时触发 `progress` 事件。

    request.post(url)
      .attach('field_name', file)
      .on('progress', event => {
        /* event的值：
        {
          direction: "upload" or "download"
          percent: 0 to 100 // 如果文件大小未知，可能会没有
          total: // 总文件大小，可能没有
          loaded: // 到目前为止下载或上传的字节数
        } */
      })
      .then()


## 在本地主机上测试

### 强制连接特定 IP 地址

在 Node.js 中，可以忽略 DNS 解析并使用 `.connect()` 方法将所有请求定向到特定 IP 地址。例如，此请求将转到 localhost 而不是 `example.com`：

    const res = await request.get("http://example.com").connect("127.0.0.1");

因为请求可能被重定向，所以可以指定多个主机名和多个 IP，以及一个特殊的 `*` 作为后备（注意：不支持其他通配符）。请求将保留其 `Host` 请求头的原始值。

    const res = await request.get("http://redir.example.com:555")
      .connect({
        "redir.example.com": "127.0.0.1", // redir.example.com:555 将使用 127.0.0.1:555
        "www.example.com": false, // 不覆盖这个；正常使用 DNS
        "mapped.example.com": { host: "127.0.0.1", port: 8080}, // mapped.example.com:* 将使用 127.0.0.1:8080
        "*": "proxy.example.com", // 所有其他请求都将发送到该主机
      });

### 忽略本地主机上损坏/不安全的 HTTPS

在 Node.js 中，当 HTTPS 配置错误且不安全（例如，使用自签名证书而*不指定*自己的 `.ca()`）时，仍然可以通过调用 `.trustLocalhost()` 来允许对 `localhost` 的请求：

    const res = await request.get("https://localhost").trustLocalhost()

与 `.connect("127.0.0.1")` 一起，这可用于强制将对任何域的 HTTPS 请求重新路由到 `localhost`。

忽略本地主机上损坏的 HTTPS 通常是安全的，因为环回接口不会暴露给不受信任的网络。信任 `localhost` 可能会成为未来的默认设置。使用 `.trustLocalhost(false)` 强制检查 `127.0.0.1` 的可靠性。

当向任何其他 IP 发出请求时，我们故意不支持禁用 HTTPS 安全性，因为这些选项最终被滥用为 HTTPS 问题的快速"修复"。您可以从 [Let's Encrypt](https://certbot.eff.org) 获得免费的 HTTPS 证书或设置您自己的 CA (`.ca(ca_public_pem)`) 以使您的自签名证书受信任。

## Promise 和生成器函数支持

SuperAgent 的请求是一个 "thenable" 对象(带有then方法的对象)，它与 JavaScript Promise 和 `async/await` 语法兼容。

    const res = await request.get(url);

如果你使用 Promise，**不要**调用 `.end()` 或 `.pipe()`。任何使用 `.then()` 或 `await` 都会禁用所有其他使用请求的方式。 像 [co](https://github.com/tj/co) 这样的库或像 [koa](https://github.com/koajs/koa) 这样的 web 框架可以在任何 SuperAgent 方法上 `yield`：

    const req = request
      .get('http://local')
      .auth('tobi', 'learnboost');
    const res = yield req;

请注意，SuperAgent 期望全局 `Promise` 对象存在。您需要一个 polyfill 才能在 Internet Explorer 或 Node.js 0.10 中使用 Promise。

## 浏览器和 node 版本

SuperAgent 有两种实现：一种用于 Web 浏览器（使用 XHR），另一种用于 Node.JS（使用核心 http 模块）。默认情况下，Browserify 和 WebPack 将选择浏览器版本。 

如果要使用 WebPack 为 Node.JS 编译代码，您*必须*在其配置中指定[node target](https://webpack.github.io/docs/configuration.html#target)。

### 在 electron 中使用浏览器版本

[Electron](https://electron.atom.io/) 开发人员报告说，如果您希望使用浏览器版本的 SuperAgent 而不是 Node 版本，您可以 `require('superagent/superagent')`。这样您的请求将显示在 Chrome 开发者工具的"网络(Network)"选项卡中。请注意，自动化测试套件未涵盖此环境，也未得到官方支持。

## 使用代理发送请求

可以使用另一个作者的 [superagent-proxy](https://www.npmjs.com/package/superagent-proxy) 模块

## 翻译说明

文档全部内容都是根据原英文文档翻译的，译者也没水平，所以如果有错误还请指出
```

## File: `examples/simple-get.js`
```javascript
/**
 * Module dependencies.
 */

const request = require('..');

const url =
  'https://gist.githubusercontent.com/reinaldo13/cdbb4d663ba23410a77b/raw/0345267767d50790051951ddc460e2699649de2b/it-works.txt';

request.get(url, (error, res) => {
  if (error) throw error;
  console.log(res.text);
});
```

## File: `src/agent-base.js`
```javascript
const defaults = [
  'use',
  'on',
  'once',
  'set',
  'query',
  'type',
  'accept',
  'auth',
  'withCredentials',
  'sortQuery',
  'retry',
  'ok',
  'redirects',
  'timeout',
  'buffer',
  'serialize',
  'parse',
  'ca',
  'key',
  'pfx',
  'cert',
  'disableTLSCerts'
]

class Agent {
  constructor () {
    this._defaults = [];
  }

  _setDefaults (request) {
    for (const def of this._defaults) {
      request[def.fn](...def.args);
    }
  }
}

for (const fn of defaults) {
  // Default setting for all requests from this agent
  Agent.prototype[fn] = function (...args) {
    this._defaults.push({ fn, args });
    return this;
  };
}


module.exports = Agent;
```

## File: `src/client.js`
```javascript
/**
 * Root reference for iframes.
 */

let root;
if (typeof window !== 'undefined') {
  // Browser window
  root = window;
} else if (typeof self === 'undefined') {
  // Other environments
  console.warn(
    'Using browser-only version of superagent in non-browser environment'
  );
  root = this;
} else {
  // Web Worker
  root = self;
}

const Emitter = require('component-emitter');
const safeStringify = require('fast-safe-stringify');
const qs = require('qs');
const RequestBase = require('./request-base');
const { isObject, mixin, hasOwn } = require('./utils');
const ResponseBase = require('./response-base');
const Agent = require('./agent-base');

/**
 * Noop.
 */

function noop() {}

/**
 * Expose `request`.
 */

module.exports = function (method, url) {
  // callback
  if (typeof url === 'function') {
    return new exports.Request('GET', method).end(url);
  }

  // url first
  if (arguments.length === 1) {
    return new exports.Request('GET', method);
  }

  return new exports.Request(method, url);
};

exports = module.exports;

const request = exports;

exports.Request = Request;

/**
 * Determine XHR.
 */

request.getXHR = () => {
  if (root.XMLHttpRequest) {
    return new root.XMLHttpRequest();
  }

  throw new Error('Browser-only version of superagent could not find XHR');
};

/**
 * Removes leading and trailing whitespace, added to support IE.
 *
 * @param {String} s
 * @return {String}
 * @api private
 */

const trim = ''.trim ? (s) => s.trim() : (s) => s.replace(/(^\s*|\s*$)/g, '');

/**
 * Serialize the given `obj`.
 *
 * @param {Object} obj
 * @return {String}
 * @api private
 */

function serialize(object) {
  if (!isObject(object)) return object;
  const pairs = [];
  for (const key in object) {
    if (hasOwn(object, key)) pushEncodedKeyValuePair(pairs, key, object[key]);
  }

  return pairs.join('&');
}

/**
 * Helps 'serialize' with serializing arrays.
 * Mutates the pairs array.
 *
 * @param {Array} pairs
 * @param {String} key
 * @param {Mixed} val
 */

function pushEncodedKeyValuePair(pairs, key, value) {
  if (value === undefined) return;
  if (value === null) {
    pairs.push(encodeURI(key));
    return;
  }

  if (Array.isArray(value)) {
    for (const v of value) {
      pushEncodedKeyValuePair(pairs, key, v);
    }
  } else if (isObject(value)) {
    for (const subkey in value) {
      if (hasOwn(value, subkey))
        pushEncodedKeyValuePair(pairs, `${key}[${subkey}]`, value[subkey]);
    }
  } else {
    pairs.push(encodeURI(key) + '=' + encodeURIComponent(value));
  }
}

/**
 * Expose serialization method.
 */

request.serializeObject = serialize;

/**
 * Parse the given x-www-form-urlencoded `str`.
 *
 * @param {String} str
 * @return {Object}
 * @api private
 */

function parseString(string_) {
  const object = {};
  const pairs = string_.split('&');
  let pair;
  let pos;

  for (let i = 0, length_ = pairs.length; i < length_; ++i) {
    pair = pairs[i];
    pos = pair.indexOf('=');
    if (pos === -1) {
      object[decodeURIComponent(pair)] = '';
    } else {
      object[decodeURIComponent(pair.slice(0, pos))] = decodeURIComponent(
        pair.slice(pos + 1)
      );
    }
  }

  return object;
}

/**
 * Expose parser.
 */

request.parseString = parseString;

/**
 * Default MIME type map.
 *
 *     superagent.types.xml = 'application/xml';
 *
 */

request.types = {
  html: 'text/html',
  json: 'application/json',
  xml: 'text/xml',
  urlencoded: 'application/x-www-form-urlencoded',
  form: 'application/x-www-form-urlencoded',
  'form-data': 'application/x-www-form-urlencoded'
};

/**
 * Default serialization map.
 *
 *     superagent.serialize['application/xml'] = function(obj){
 *       return 'generated xml here';
 *     };
 *
 */

request.serialize = {
  'application/x-www-form-urlencoded': (obj) => {
    return qs.stringify(obj, { indices: false, strictNullHandling: true });
  },
  'application/json': safeStringify
};

/**
 * Default parsers.
 *
 *     superagent.parse['application/xml'] = function(str){
 *       return { object parsed from str };
 *     };
 *
 */

request.parse = {
  'application/x-www-form-urlencoded': parseString,
  'application/json': JSON.parse
};

/**
 * Parse the given header `str` into
 * an object containing the mapped fields.
 *
 * @param {String} str
 * @return {Object}
 * @api private
 */

function parseHeader(string_) {
  const lines = string_.split(/\r?\n/);
  const fields = {};
  let index;
  let line;
  let field;
  let value;

  for (let i = 0, length_ = lines.length; i < length_; ++i) {
    line = lines[i];
    index = line.indexOf(':');
    if (index === -1) {
      // could be empty line, just skip it
      continue;
    }

    field = line.slice(0, index).toLowerCase();
    value = trim(line.slice(index + 1));
    fields[field] = value;
  }

  return fields;
}

/**
 * Check if `mime` is json or has +json structured syntax suffix.
 *
 * @param {String} mime
 * @return {Boolean}
 * @api private
 */

function isJSON(mime) {
  // should match /json or +json
  // but not /json-seq
  return /[/+]json($|[^-\w])/i.test(mime);
}

/**
 * Initialize a new `Response` with the given `xhr`.
 *
 *  - set flags (.ok, .error, etc)
 *  - parse header
 *
 * Examples:
 *
 *  Aliasing `superagent` as `request` is nice:
 *
 *      request = superagent;
 *
 *  We can use the promise-like API, or pass callbacks:
 *
 *      request.get('/').end(function(res){});
 *      request.get('/', function(res){});
 *
 *  Sending data can be chained:
 *
 *      request
 *        .post('/user')
 *        .send({ name: 'tj' })
 *        .end(function(res){});
 *
 *  Or passed to `.send()`:
 *
 *      request
 *        .post('/user')
 *        .send({ name: 'tj' }, function(res){});
 *
 *  Or passed to `.post()`:
 *
 *      request
 *        .post('/user', { name: 'tj' })
 *        .end(function(res){});
 *
 * Or further reduced to a single call for simple cases:
 *
 *      request
 *        .post('/user', { name: 'tj' }, function(res){});
 *
 * @param {XMLHTTPRequest} xhr
 * @param {Object} options
 * @api private
 */

function Response(request_) {
  this.req = request_;
  this.xhr = this.req.xhr;
  // responseText is accessible only if responseType is '' or 'text' and on older browsers
  this.text =
    (this.req.method !== 'HEAD' &&
      (this.xhr.responseType === '' || this.xhr.responseType === 'text')) ||
    typeof this.xhr.responseType === 'undefined'
      ? this.xhr.responseText
      : null;
  this.statusText = this.req.xhr.statusText;
  let { status } = this.xhr;
  // handle IE9 bug: http://stackoverflow.com/questions/10046972/msie-returns-status-code-of-1223-for-ajax-request
  if (status === 1223) {
    status = 204;
  }

  this._setStatusProperties(status);
  this.headers = parseHeader(this.xhr.getAllResponseHeaders());
  this.header = this.headers;
  // getAllResponseHeaders sometimes falsely returns "" for CORS requests, but
  // getResponseHeader still works. so we get content-type even if getting
  // other headers fails.
  this.header['content-type'] = this.xhr.getResponseHeader('content-type');
  this._setHeaderProperties(this.header);

  if (this.text === null && request_._responseType) {
    this.body = this.xhr.response;
  } else {
    this.body =
      this.req.method === 'HEAD'
        ? null
        : this._parseBody(this.text ? this.text : this.xhr.response);
  }
}

mixin(Response.prototype, ResponseBase.prototype);

/**
 * Parse the given body `str`.
 *
 * Used for auto-parsing of bodies. Parsers
 * are defined on the `superagent.parse` object.
 *
 * @param {String} str
 * @return {Mixed}
 * @api private
 */

Response.prototype._parseBody = function (string_) {
  let parse = request.parse[this.type];
  if (this.req._parser) {
    return this.req._parser(this, string_);
  }

  if (!parse && isJSON(this.type)) {
    parse = request.parse['application/json'];
  }

  return parse && string_ && (string_.length > 0 || string_ instanceof Object)
    ? parse(string_)
    : null;
};

/**
 * Return an `Error` representative of this response.
 *
 * @return {Error}
 * @api public
 */

Response.prototype.toError = function () {
  const { req } = this;
  const { method } = req;
  const { url } = req;

  const message = `cannot ${method} ${url} (${this.status})`;
  const error = new Error(message);
  error.status = this.status;
  error.method = method;
  error.url = url;

  return error;
};

/**
 * Expose `Response`.
 */

request.Response = Response;

/**
 * Initialize a new `Request` with the given `method` and `url`.
 *
 * @param {String} method
 * @param {String} url
 * @api public
 */

function Request(method, url) {
  const self = this;
  this._query = this._query || [];
  this.method = method;
  this.url = url;
  this.header = {}; // preserves header name case
  this._header = {}; // coerces header names to lowercase
  this.on('end', () => {
    let error = null;
    let res = null;

    try {
      res = new Response(self);
    } catch (err) {
      error = new Error('Parser is unable to parse the response');
      error.parse = true;
      error.original = err;
      // issue #675: return the raw response if the response parsing fails
      if (self.xhr) {
        // ie9 doesn't have 'response' property
        error.rawResponse =
          typeof self.xhr.responseType === 'undefined'
            ? self.xhr.responseText
            : self.xhr.response;
        // issue #876: return the http status code if the response parsing fails
        error.status = self.xhr.status ? self.xhr.status : null;
        error.statusCode = error.status; // backwards-compat only
      } else {
        error.rawResponse = null;
        error.status = null;
      }

      return self.callback(error);
    }

    self.emit('response', res);

    let new_error;
    try {
      if (!self._isResponseOK(res)) {
        new_error = new Error(
          res.statusText || res.text || 'Unsuccessful HTTP response'
        );
      }
    } catch (err) {
      new_error = err; // ok() callback can throw
    }

    // #1000 don't catch errors from the callback to avoid double calling it
    if (new_error) {
      new_error.original = error;
      new_error.response = res;
      new_error.status = new_error.status || res.status;
      self.callback(new_error, res);
    } else {
      self.callback(null, res);
    }
  });
}

/**
 * Mixin `Emitter` and `RequestBase`.
 */

// eslint-disable-next-line new-cap
Emitter(Request.prototype);

mixin(Request.prototype, RequestBase.prototype);

/**
 * Set Content-Type to `type`, mapping values from `request.types`.
 *
 * Examples:
 *
 *      superagent.types.xml = 'application/xml';
 *
 *      request.post('/')
 *        .type('xml')
 *        .send(xmlstring)
 *        .end(callback);
 *
 *      request.post('/')
 *        .type('application/xml')
 *        .send(xmlstring)
 *        .end(callback);
 *
 * @param {String} type
 * @return {Request} for chaining
 * @api public
 */

Request.prototype.type = function (type) {
  this.set('Content-Type', request.types[type] || type);
  return this;
};

/**
 * Set Accept to `type`, mapping values from `request.types`.
 *
 * Examples:
 *
 *      superagent.types.json = 'application/json';
 *
 *      request.get('/agent')
 *        .accept('json')
 *        .end(callback);
 *
 *      request.get('/agent')
 *        .accept('application/json')
 *        .end(callback);
 *
 * @param {String} accept
 * @return {Request} for chaining
 * @api public
 */

Request.prototype.accept = function (type) {
  this.set('Accept', request.types[type] || type);
  return this;
};

/**
 * Set Authorization field value with `user` and `pass`.
 *
 * @param {String} user
 * @param {String} [pass] optional in case of using 'bearer' as type
 * @param {Object} options with 'type' property 'auto', 'basic' or 'bearer' (default 'basic')
 * @return {Request} for chaining
 * @api public
 */

Request.prototype.auth = function (user, pass, options) {
  if (arguments.length === 1) pass = '';
  if (typeof pass === 'object' && pass !== null) {
    // pass is optional and can be replaced with options
    options = pass;
    pass = '';
  }

  if (!options) {
    options = {
      type: typeof btoa === 'function' ? 'basic' : 'auto'
    };
  }

  const encoder = options.encoder
    ? options.encoder
    : (string) => {
        if (typeof btoa === 'function') {
          return btoa(string);
        }

        throw new Error('Cannot use basic auth, btoa is not a function');
      };

  return this._auth(user, pass, options, encoder);
};

/**
 * Add query-string `val`.
 *
 * Examples:
 *
 *   request.get('/shoes')
 *     .query('size=10')
 *     .query({ color: 'blue' })
 *
 * @param {Object|String} val
 * @return {Request} for chaining
 * @api public
 */

Request.prototype.query = function (value) {
  if (typeof value !== 'string') value = serialize(value);
  if (value) this._query.push(value);
  return this;
};

/**
 * Queue the given `file` as an attachment to the specified `field`,
 * with optional `options` (or filename).
 *
 * ``` js
 * request.post('/upload')
 *   .attach('content', new Blob(['<a id="a"><b id="b">hey!</b></a>'], { type: "text/html"}))
 *   .end(callback);
 * ```
 *
 * @param {String} field
 * @param {Blob|File} file
 * @param {String|Object} options
 * @return {Request} for chaining
 * @api public
 */

Request.prototype.attach = function (field, file, options) {
  if (file) {
    if (this._data) {
      throw new Error("superagent can't mix .send() and .attach()");
    }

    this._getFormData().append(field, file, options || file.name);
  }

  return this;
};

Request.prototype._getFormData = function () {
  if (!this._formData) {
    this._formData = new root.FormData();
  }

  return this._formData;
};

/**
 * Invoke the callback with `err` and `res`
 * and handle arity check.
 *
 * @param {Error} err
 * @param {Response} res
 * @api private
 */

Request.prototype.callback = function (error, res) {
  if (this._shouldRetry(error, res)) {
    return this._retry();
  }

  const fn = this._callback;
  this.clearTimeout();

  if (error) {
    if (this._maxRetries) error.retries = this._retries - 1;
    this.emit('error', error);
  }

  fn(error, res);
};

/**
 * Invoke callback with x-domain error.
 *
 * @api private
 */

Request.prototype.crossDomainError = function () {
  const error = new Error(
    'Request has been terminated\nPossible causes: the network is offline, Origin is not allowed by Access-Control-Allow-Origin, the page is being unloaded, etc.'
  );
  error.crossDomain = true;

  error.status = this.status;
  error.method = this.method;
  error.url = this.url;

  this.callback(error);
};

// This only warns, because the request is still likely to work
Request.prototype.agent = function () {
  console.warn('This is not supported in browser version of superagent');
  return this;
};

Request.prototype.ca = Request.prototype.agent;
Request.prototype.buffer = Request.prototype.ca;

// This throws, because it can't send/receive data as expected
Request.prototype.write = () => {
  throw new Error(
    'Streaming is not supported in browser version of superagent'
  );
};

Request.prototype.pipe = Request.prototype.write;

/**
 * Check if `obj` is a host object,
 * we don't want to serialize these :)
 *
 * @param {Object} obj host object
 * @return {Boolean} is a host object
 * @api private
 */
Request.prototype._isHost = function (object) {
  // Native objects stringify to [object File], [object Blob], [object FormData], etc.
  return (
    object &&
    typeof object === 'object' &&
    !Array.isArray(object) &&
    Object.prototype.toString.call(object) !== '[object Object]'
  );
};

/**
 * Initiate request, invoking callback `fn(res)`
 * with an instanceof `Response`.
 *
 * @param {Function} fn
 * @return {Request} for chaining
 * @api public
 */

Request.prototype.end = function (fn) {
  if (this._endCalled) {
    console.warn(
      'Warning: .end() was called twice. This is not supported in superagent'
    );
  }

  this._endCalled = true;

  // store callback
  this._callback = fn || noop;

  // querystring
  this._finalizeQueryString();

  this._end();
};

Request.prototype._setUploadTimeout = function () {
  const self = this;

  // upload timeout it's wokrs only if deadline timeout is off
  if (this._uploadTimeout && !this._uploadTimeoutTimer) {
    this._uploadTimeoutTimer = setTimeout(() => {
      self._timeoutError(
        'Upload timeout of ',
        self._uploadTimeout,
        'ETIMEDOUT'
      );
    }, this._uploadTimeout);
  }
};

// eslint-disable-next-line complexity
Request.prototype._end = function () {
  if (this._aborted)
    return this.callback(
      new Error('The request has been aborted even before .end() was called')
    );

  const self = this;
  this.xhr = request.getXHR();
  const { xhr } = this;
  let data = this._formData || this._data;

  this._setTimeouts();

  // state change
  xhr.addEventListener('readystatechange', () => {
    const { readyState } = xhr;
    if (readyState >= 2 && self._responseTimeoutTimer) {
      clearTimeout(self._responseTimeoutTimer);
    }

    if (readyState !== 4) {
      return;
    }

    // In IE9, reads to any property (e.g. status) off of an aborted XHR will
    // result in the error "Could not complete the operation due to error c00c023f"
    let status;
    try {
      status = xhr.status;
    } catch (err) {
      status = 0;
    }

    if (!status) {
      if (self.timedout || self._aborted) return;
      return self.crossDomainError();
    }

    self.emit('end');
  });

  // progress
  const handleProgress = (direction, e) => {
    if (e.total > 0) {
      e.percent = (e.loaded / e.total) * 100;

      if (e.percent === 100) {
        clearTimeout(self._uploadTimeoutTimer);
      }
    }

    e.direction = direction;
    self.emit('progress', e);
  };

  if (this.hasListeners('progress')) {
    try {
      xhr.addEventListener('progress', handleProgress.bind(null, 'download'));
      if (xhr.upload) {
        xhr.upload.addEventListener(
          'progress',
          handleProgress.bind(null, 'upload')
        );
      }
    } catch (err) {
      // Accessing xhr.upload fails in IE from a web worker, so just pretend it doesn't exist.
      // Reported here:
      // https://connect.microsoft.com/IE/feedback/details/837245/xmlhttprequest-upload-throws-invalid-argument-when-used-from-web-worker-context
    }
  }

  if (xhr.upload) {
    this._setUploadTimeout();
  }

  // initiate request
  try {
    if (this.username && this.password) {
      xhr.open(this.method, this.url, true, this.username, this.password);
    } else {
      xhr.open(this.method, this.url, true);
    }
  } catch (err) {
    // see #1149
    return this.callback(err);
  }

  // CORS
  if (this._withCredentials) xhr.withCredentials = true;

  // body
  if (
    !this._formData &&
    this.method !== 'GET' &&
    this.method !== 'HEAD' &&
    typeof data !== 'string' &&
    !this._isHost(data)
  ) {
    // serialize stuff
    const contentType = this._header['content-type'];
    let serialize =
      this._serializer ||
      request.serialize[contentType ? contentType.split(';')[0] : ''];
    if (!serialize && isJSON(contentType)) {
      serialize = request.serialize['application/json'];
    }

    if (serialize) data = serialize(data);
  }

  // set header fields
  for (const field in this.header) {
    if (this.header[field] === null) continue;

    if (hasOwn(this.header, field))
      xhr.setRequestHeader(field, this.header[field]);
  }

  if (this._responseType) {
    xhr.responseType = this._responseType;
  }

  // send stuff
  this.emit('request', this);

  // IE11 xhr.send(undefined) sends 'undefined' string as POST payload (instead of nothing)
  // We need null here if data is undefined
  xhr.send(typeof data === 'undefined' ? null : data);
};

// create a Proxy that can instantiate a new Agent without using `new` keyword
// (for backward compatibility and chaining)
const proxyAgent = new Proxy(Agent, {
  apply(target, thisArg, argumentsList) {
    return new target(...argumentsList);
  }
});
request.agent = proxyAgent;

for (const method of ['GET', 'POST', 'OPTIONS', 'PATCH', 'PUT', 'DELETE']) {
  Agent.prototype[method.toLowerCase()] = function (url, fn) {
    const request_ = new request.Request(method, url);
    this._setDefaults(request_);
    if (fn) {
      request_.end(fn);
    }

    return request_;
  };
}

Agent.prototype.del = Agent.prototype.delete;

/**
 * GET `url` with optional callback `fn(res)`.
 *
 * @param {String} url
 * @param {Mixed|Function} [data] or fn
 * @param {Function} [fn]
 * @return {Request}
 * @api public
 */

request.get = (url, data, fn) => {
  const request_ = request('GET', url);
  if (typeof data === 'function') {
    fn = data;
    data = null;
  }

  if (data) request_.query(data);
  if (fn) request_.end(fn);
  return request_;
};

/**
 * HEAD `url` with optional callback `fn(res)`.
 *
 * @param {String} url
 * @param {Mixed|Function} [data] or fn
 * @param {Function} [fn]
 * @return {Request}
 * @api public
 */

request.head = (url, data, fn) => {
  const request_ = request('HEAD', url);
  if (typeof data === 'function') {
    fn = data;
    data = null;
  }

  if (data) request_.query(data);
  if (fn) request_.end(fn);
  return request_;
};

/**
 * OPTIONS query to `url` with optional callback `fn(res)`.
 *
 * @param {String} url
 * @param {Mixed|Function} [data] or fn
 * @param {Function} [fn]
 * @return {Request}
 * @api public
 */

request.options = (url, data, fn) => {
  const request_ = request('OPTIONS', url);
  if (typeof data === 'function') {
    fn = data;
    data = null;
  }

  if (data) request_.send(data);
  if (fn) request_.end(fn);
  return request_;
};

/**
 * DELETE `url` with optional `data` and callback `fn(res)`.
 *
 * @param {String} url
 * @param {Mixed} [data]
 * @param {Function} [fn]
 * @return {Request}
 * @api public
 */

function del(url, data, fn) {
  const request_ = request('DELETE', url);
  if (typeof data === 'function') {
    fn = data;
    data = null;
  }

  if (data) request_.send(data);
  if (fn) request_.end(fn);
  return request_;
}

request.del = del;
request.delete = del;

/**
 * PATCH `url` with optional `data` and callback `fn(res)`.
 *
 * @param {String} url
 * @param {Mixed} [data]
 * @param {Function} [fn]
 * @return {Request}
 * @api public
 */

request.patch = (url, data, fn) => {
  const request_ = request('PATCH', url);
  if (typeof data === 'function') {
    fn = data;
    data = null;
  }

  if (data) request_.send(data);
  if (fn) request_.end(fn);
  return request_;
};

/**
 * POST `url` with optional `data` and callback `fn(res)`.
 *
 * @param {String} url
 * @param {Mixed} [data]
 * @param {Function} [fn]
 * @return {Request}
 * @api public
 */

request.post = (url, data, fn) => {
  const request_ = request('POST', url);
  if (typeof data === 'function') {
    fn = data;
    data = null;
  }

  if (data) request_.send(data);
  if (fn) request_.end(fn);
  return request_;
};

/**
 * PUT `url` with optional `data` and callback `fn(res)`.
 *
 * @param {String} url
 * @param {Mixed|Function} [data] or fn
 * @param {Function} [fn]
 * @return {Request}
 * @api public
 */

request.put = (url, data, fn) => {
  const request_ = request('PUT', url);
  if (typeof data === 'function') {
    fn = data;
    data = null;
  }

  if (data) request_.send(data);
  if (fn) request_.end(fn);
  return request_;
};
```

## File: `src/request-base.js`
```javascript
/**
 * Module of mixed-in functions shared between node and client code
 */
const { isObject, hasOwn } = require('./utils');

/**
 * Expose `RequestBase`.
 */

module.exports = RequestBase;

/**
 * Initialize a new `RequestBase`.
 *
 * @api public
 */

function RequestBase() {}

/**
 * Clear previous timeout.
 *
 * @return {Request} for chaining
 * @api public
 */

RequestBase.prototype.clearTimeout = function () {
  clearTimeout(this._timer);
  clearTimeout(this._responseTimeoutTimer);
  clearTimeout(this._uploadTimeoutTimer);
  delete this._timer;
  delete this._responseTimeoutTimer;
  delete this._uploadTimeoutTimer;
  return this;
};

/**
 * Override default response body parser
 *
 * This function will be called to convert incoming data into request.body
 *
 * @param {Function}
 * @api public
 */

RequestBase.prototype.parse = function (fn) {
  this._parser = fn;
  return this;
};

/**
 * Set format of binary response body.
 * In browser valid formats are 'blob' and 'arraybuffer',
 * which return Blob and ArrayBuffer, respectively.
 *
 * In Node all values result in Buffer.
 *
 * Examples:
 *
 *      req.get('/')
 *        .responseType('blob')
 *        .end(callback);
 *
 * @param {String} val
 * @return {Request} for chaining
 * @api public
 */

RequestBase.prototype.responseType = function (value) {
  this._responseType = value;
  return this;
};

/**
 * Override default request body serializer
 *
 * This function will be called to convert data set via .send or .attach into payload to send
 *
 * @param {Function}
 * @api public
 */

RequestBase.prototype.serialize = function (fn) {
  this._serializer = fn;
  return this;
};

/**
 * Set timeouts.
 *
 * - response timeout is time between sending request and receiving the first byte of the response. Includes DNS and connection time.
 * - deadline is the time from start of the request to receiving response body in full. If the deadline is too short large files may not load at all on slow connections.
 * - upload is the time  since last bit of data was sent or received. This timeout works only if deadline timeout is off
 *
 * Value of 0 or false means no timeout.
 *
 * @param {Number|Object} ms or {response, deadline}
 * @return {Request} for chaining
 * @api public
 */

RequestBase.prototype.timeout = function (options) {
  if (!options || typeof options !== 'object') {
    this._timeout = options;
    this._responseTimeout = 0;
    this._uploadTimeout = 0;
    return this;
  }

  for (const option in options) {
    if (hasOwn(options, option)) {
      switch (option) {
        case 'deadline':
          this._timeout = options.deadline;
          break;
        case 'response':
          this._responseTimeout = options.response;
          break;
        case 'upload':
          this._uploadTimeout = options.upload;
          break;
        default:
          console.warn('Unknown timeout option', option);
      }
    }
  }

  return this;
};

/**
 * Set number of retry attempts on error.
 *
 * Failed requests will be retried 'count' times if timeout or err.code >= 500.
 *
 * @param {Number} count
 * @param {Function} [fn]
 * @return {Request} for chaining
 * @api public
 */

RequestBase.prototype.retry = function (count, fn) {
  // Default to 1 if no count passed or true
  if (arguments.length === 0 || count === true) count = 1;
  if (count <= 0) count = 0;
  this._maxRetries = count;
  this._retries = 0;
  this._retryCallback = fn;
  return this;
};

//
// NOTE: we do not include ESOCKETTIMEDOUT because that is from `request` package
//       <https://github.com/sindresorhus/got/pull/537>
//
// NOTE: we do not include EADDRINFO because it was removed from libuv in 2014
//       <https://github.com/libuv/libuv/commit/02e1ebd40b807be5af46343ea873331b2ee4e9c1>
//       <https://github.com/request/request/search?q=ESOCKETTIMEDOUT&unscoped_q=ESOCKETTIMEDOUT>
//
//
// TODO: expose these as configurable defaults
//
const ERROR_CODES = new Set([
  'ETIMEDOUT',
  'ECONNRESET',
  'EADDRINUSE',
  'ECONNREFUSED',
  'EPIPE',
  'ENOTFOUND',
  'ENETUNREACH',
  'EAI_AGAIN'
]);

const STATUS_CODES = new Set([
  408, 413, 429, 500, 502, 503, 504, 521, 522, 524
]);

// TODO: we would need to make this easily configurable before adding it in (e.g. some might want to add POST)
// const METHODS = new Set(['GET', 'PUT', 'HEAD', 'DELETE', 'OPTIONS', 'TRACE']);

/**
 * Determine if a request should be retried.
 * (Inspired by https://github.com/sindresorhus/got#retry)
 *
 * @param {Error} err an error
 * @param {Response} [res] response
 * @returns {Boolean} if segment should be retried
 */
RequestBase.prototype._shouldRetry = function (error, res) {
  if (!this._maxRetries || this._retries++ >= this._maxRetries) {
    return false;
  }

  if (this._retryCallback) {
    try {
      const override = this._retryCallback(error, res);
      if (override === true) return true;
      if (override === false) return false;
      // undefined falls back to defaults
    } catch (err) {
      console.error(err);
    }
  }

  // TODO: we would need to make this easily configurable before adding it in (e.g. some might want to add POST)
  /*
  if (
    this.req &&
    this.req.method &&
    !METHODS.has(this.req.method.toUpperCase())
  )
    return false;
  */
  if (res && res.status && STATUS_CODES.has(res.status)) return true;
  if (error) {
    if (error.code && ERROR_CODES.has(error.code)) return true;
    // Superagent timeout
    if (error.timeout && error.code === 'ECONNABORTED') return true;
    if (error.crossDomain) return true;
  }

  return false;
};

/**
 * Retry request
 *
 * @return {Request} for chaining
 * @api private
 */

RequestBase.prototype._retry = function () {
  this.clearTimeout();

  // node
  if (this.req) {
    this.req = null;
    this.req = this.request();
  }

  this._aborted = false;
  this.timedout = false;
  this.timedoutError = null;

  return this._end();
};

/**
 * Promise support
 *
 * @param {Function} resolve
 * @param {Function} [reject]
 * @return {Request}
 */

RequestBase.prototype.then = function (resolve, reject) {
  if (!this._fullfilledPromise) {
    const self = this;
    if (this._endCalled) {
      console.warn(
        'Warning: superagent request was sent twice, because both .end() and .then() were called. Never call .end() if you use promises'
      );
    }

    this._fullfilledPromise = new Promise((resolve, reject) => {
      self.on('abort', () => {
        if (this._maxRetries && this._maxRetries > this._retries) {
          return;
        }

        if (this.timedout && this.timedoutError) {
          reject(this.timedoutError);
          return;
        }

        const error = new Error('Aborted');
        error.code = 'ABORTED';
        error.status = this.status;
        error.method = this.method;
        error.url = this.url;
        reject(error);
      });
      self.end((error, res) => {
        if (error) reject(error);
        else resolve(res);
      });
    });
  }

  return this._fullfilledPromise.then(resolve, reject);
};

RequestBase.prototype.catch = function (callback) {
  return this.then(undefined, callback);
};

/**
 * Allow for extension
 */

RequestBase.prototype.use = function (fn) {
  fn(this);
  return this;
};

RequestBase.prototype.ok = function (callback) {
  if (typeof callback !== 'function') throw new Error('Callback required');
  this._okCallback = callback;
  return this;
};

RequestBase.prototype._isResponseOK = function (res) {
  if (!res) {
    return false;
  }

  if (this._okCallback) {
    return this._okCallback(res);
  }

  return res.status >= 200 && res.status < 300;
};

/**
 * Get request header `field`.
 * Case-insensitive.
 *
 * @param {String} field
 * @return {String}
 * @api public
 */

RequestBase.prototype.get = function (field) {
  return this._header[field.toLowerCase()];
};

/**
 * Get case-insensitive header `field` value.
 * This is a deprecated internal API. Use `.get(field)` instead.
 *
 * (getHeader is no longer used internally by the superagent code base)
 *
 * @param {String} field
 * @return {String}
 * @api private
 * @deprecated
 */

RequestBase.prototype.getHeader = RequestBase.prototype.get;

/**
 * Set header `field` to `val`, or multiple fields with one object.
 * Case-insensitive.
 *
 * Examples:
 *
 *      req.get('/')
 *        .set('Accept', 'application/json')
 *        .set('X-API-Key', 'foobar')
 *        .end(callback);
 *
 *      req.get('/')
 *        .set({ Accept: 'application/json', 'X-API-Key': 'foobar' })
 *        .end(callback);
 *
 * @param {String|Object} field
 * @param {String} val
 * @return {Request} for chaining
 * @api public
 */

RequestBase.prototype.set = function (field, value) {
  if (isObject(field)) {
    for (const key in field) {
      if (hasOwn(field, key)) this.set(key, field[key]);
    }

    return this;
  }

  this._header[field.toLowerCase()] = value;
  this.header[field] = value;
  return this;
};

/**
 * Remove header `field`.
 * Case-insensitive.
 *
 * Example:
 *
 *      req.get('/')
 *        .unset('User-Agent')
 *        .end(callback);
 *
 * @param {String} field field name
 */
RequestBase.prototype.unset = function (field) {
  delete this._header[field.toLowerCase()];
  delete this.header[field];
  return this;
};

/**
 * Write the field `name` and `val`, or multiple fields with one object
 * for "multipart/form-data" request bodies.
 *
 * ``` js
 * request.post('/upload')
 *   .field('foo', 'bar')
 *   .end(callback);
 *
 * request.post('/upload')
 *   .field({ foo: 'bar', baz: 'qux' })
 *   .end(callback);
 * ```
 *
 * @param {String|Object} name name of field
 * @param {String|Blob|File|Buffer|fs.ReadStream} val value of field
 * @param {String} options extra options, e.g. 'blob'
 * @return {Request} for chaining
 * @api public
 */
RequestBase.prototype.field = function (name, value, options) {
  // name should be either a string or an object.
  if (name === null || undefined === name) {
    throw new Error('.field(name, val) name can not be empty');
  }

  if (this._data) {
    throw new Error(
      ".field() can't be used if .send() is used. Please use only .send() or only .field() & .attach()"
    );
  }

  if (isObject(name)) {
    for (const key in name) {
      if (hasOwn(name, key)) this.field(key, name[key]);
    }

    return this;
  }

  if (Array.isArray(value)) {
    for (const i in value) {
      if (hasOwn(value, i)) this.field(name, value[i]);
    }

    return this;
  }

  // val should be defined now
  if (value === null || undefined === value) {
    throw new Error('.field(name, val) val can not be empty');
  }

  if (typeof value === 'boolean') {
    value = String(value);
  }

  // fix https://github.com/ladjs/superagent/issues/1680
  if (options) this._getFormData().append(name, value, options);
  else this._getFormData().append(name, value);

  return this;
};

/**
 * Abort the request, and clear potential timeout.
 *
 * @return {Request} request
 * @api public
 */
RequestBase.prototype.abort = function () {
  if (this._aborted) {
    return this;
  }

  this._aborted = true;
  if (this.xhr) this.xhr.abort(); // browser
  if (this.req) {
    this.req.abort(); // node
  }

  this.clearTimeout();
  this.emit('abort');
  return this;
};

RequestBase.prototype._auth = function (user, pass, options, base64Encoder) {
  switch (options.type) {
    case 'basic':
      this.set('Authorization', `Basic ${base64Encoder(`${user}:${pass}`)}`);
      break;

    case 'auto':
      this.username = user;
      this.password = pass;
      break;

    case 'bearer': // usage would be .auth(accessToken, { type: 'bearer' })
      this.set('Authorization', `Bearer ${user}`);
      break;
    default:
      break;
  }

  return this;
};

/**
 * Enable transmission of cookies with x-domain requests.
 *
 * Note that for this to work the origin must not be
 * using "Access-Control-Allow-Origin" with a wildcard,
 * and also must set "Access-Control-Allow-Credentials"
 * to "true".
 * @param {Boolean} [on=true] - Set 'withCredentials' state
 * @return {Request} for chaining
 * @api public
 */

RequestBase.prototype.withCredentials = function (on) {
  // This is browser-only functionality. Node side is no-op.
  if (on === undefined) on = true;
  this._withCredentials = on;
  return this;
};

/**
 * Set the max redirects to `n`. Does nothing in browser XHR implementation.
 *
 * @param {Number} n
 * @return {Request} for chaining
 * @api public
 */

RequestBase.prototype.redirects = function (n) {
  this._maxRedirects = n;
  return this;
};

/**
 * Maximum size of buffered response body, in bytes. Counts uncompressed size.
 * Default 200MB.
 *
 * @param {Number} n number of bytes
 * @return {Request} for chaining
 */
RequestBase.prototype.maxResponseSize = function (n) {
  if (typeof n !== 'number') {
    throw new TypeError('Invalid argument');
  }

  this._maxResponseSize = n;
  return this;
};

/**
 * Convert to a plain javascript object (not JSON string) of scalar properties.
 * Note as this method is designed to return a useful non-this value,
 * it cannot be chained.
 *
 * @return {Object} describing method, url, and data of this request
 * @api public
 */

RequestBase.prototype.toJSON = function () {
  return {
    method: this.method,
    url: this.url,
    data: this._data,
    headers: this._header
  };
};

/**
 * Send `data` as the request body, defaulting the `.type()` to "json" when
 * an object is given.
 *
 * Examples:
 *
 *       // manual json
 *       request.post('/user')
 *         .type('json')
 *         .send('{"name":"tj"}')
 *         .end(callback)
 *
 *       // auto json
 *       request.post('/user')
 *         .send({ name: 'tj' })
 *         .end(callback)
 *
 *       // manual x-www-form-urlencoded
 *       request.post('/user')
 *         .type('form')
 *         .send('name=tj')
 *         .end(callback)
 *
 *       // auto x-www-form-urlencoded
 *       request.post('/user')
 *         .type('form')
 *         .send({ name: 'tj' })
 *         .end(callback)
 *
 *       // defaults to x-www-form-urlencoded
 *      request.post('/user')
 *        .send('name=tobi')
 *        .send('species=ferret')
 *        .end(callback)
 *
 * @param {String|Object} data
 * @return {Request} for chaining
 * @api public
 */

// eslint-disable-next-line complexity
RequestBase.prototype.send = function (data) {
  const isObject_ = isObject(data);
  let type = this._header['content-type'];

  if (this._formData) {
    throw new Error(
      ".send() can't be used if .attach() or .field() is used. Please use only .send() or only .field() & .attach()"
    );
  }

  if (isObject_ && !this._data) {
    if (Array.isArray(data)) {
      this._data = [];
    } else if (!this._isHost(data)) {
      this._data = {};
    }
  } else if (data && this._data && this._isHost(this._data)) {
    throw new Error("Can't merge these send calls");
  }

  // merge
  if (isObject_ && isObject(this._data)) {
    for (const key in data) {
      if (typeof data[key] == 'bigint' && !data[key].toJSON)
        throw new Error('Cannot serialize BigInt value to json');
      if (hasOwn(data, key)) this._data[key] = data[key];
    }
  }
  else if (typeof data === 'bigint') throw new Error("Cannot send value of type BigInt");
  else if (typeof data === 'string') {
    // default to x-www-form-urlencoded
    if (!type) this.type('form');
    type = this._header['content-type'];
    if (type) type = type.toLowerCase().trim();
    if (type === 'application/x-www-form-urlencoded') {
      this._data = this._data ? `${this._data}&${data}` : data;
    } else {
      this._data = (this._data || '') + data;
    }
  } else {
    this._data = data;
  }

  if (!isObject_ || this._isHost(data)) {
    return this;
  }

  // default to json
  if (!type) this.type('json');
  return this;
};

/**
 * Sort `querystring` by the sort function
 *
 *
 * Examples:
 *
 *       // default order
 *       request.get('/user')
 *         .query('name=Nick')
 *         .query('search=Manny')
 *         .sortQuery()
 *         .end(callback)
 *
 *       // customized sort function
 *       request.get('/user')
 *         .query('name=Nick')
 *         .query('search=Manny')
 *         .sortQuery(function(a, b){
 *           return a.length - b.length;
 *         })
 *         .end(callback)
 *
 *
 * @param {Function} sort
 * @return {Request} for chaining
 * @api public
 */

RequestBase.prototype.sortQuery = function (sort) {
  // _sort default to true but otherwise can be a function or boolean
  this._sort = typeof sort === 'undefined' ? true : sort;
  return this;
};

/**
 * Compose querystring to append to req.url
 *
 * @api private
 */
RequestBase.prototype._finalizeQueryString = function () {
  const query = this._query.join('&');
  if (query) {
    this.url += (this.url.includes('?') ? '&' : '?') + query;
  }

  this._query.length = 0; // Makes the call idempotent

  if (this._sort) {
    const index = this.url.indexOf('?');
    if (index >= 0) {
      const queryArray = this.url.slice(index + 1).split('&');
      if (typeof this._sort === 'function') {
        queryArray.sort(this._sort);
      } else {
        queryArray.sort();
      }

      this.url = this.url.slice(0, index) + '?' + queryArray.join('&');
    }
  }
};

// For backwards compat only
RequestBase.prototype._appendQueryString = () => {
  console.warn('Unsupported');
};

/**
 * Invoke callback with timeout error.
 *
 * @api private
 */

RequestBase.prototype._timeoutError = function (reason, timeout, errno) {
  if (this._aborted) {
    return;
  }

  const error = new Error(`${reason + timeout}ms exceeded`);
  error.timeout = timeout;
  error.code = 'ECONNABORTED';
  error.errno = errno;
  this.timedout = true;
  this.timedoutError = error;
  this.abort();
  this.callback(error);
};

RequestBase.prototype._setTimeouts = function () {
  const self = this;

  // deadline
  if (this._timeout && !this._timer) {
    this._timer = setTimeout(() => {
      self._timeoutError('Timeout of ', self._timeout, 'ETIME');
    }, this._timeout);
  }

  // response timeout
  if (this._responseTimeout && !this._responseTimeoutTimer) {
    this._responseTimeoutTimer = setTimeout(() => {
      self._timeoutError(
        'Response timeout of ',
        self._responseTimeout,
        'ETIMEDOUT'
      );
    }, this._responseTimeout);
  }
};
```

## File: `src/response-base.js`
```javascript
/**
 * Module dependencies.
 */

const utils = require('./utils');

/**
 * Expose `ResponseBase`.
 */

module.exports = ResponseBase;

/**
 * Initialize a new `ResponseBase`.
 *
 * @api public
 */

function ResponseBase() {}

/**
 * Get case-insensitive `field` value.
 *
 * @param {String} field
 * @return {String}
 * @api public
 */

ResponseBase.prototype.get = function (field) {
  return this.header[field.toLowerCase()];
};

/**
 * Set header related properties:
 *
 *   - `.type` the content type without params
 *
 * A response of "Content-Type: text/plain; charset=utf-8"
 * will provide you with a `.type` of "text/plain".
 *
 * @param {Object} header
 * @api private
 */

ResponseBase.prototype._setHeaderProperties = function (header) {
  // TODO: moar!
  // TODO: make this a util

  // content-type
  const ct = header['content-type'] || '';
  this.type = utils.type(ct);

  // params
  const parameters = utils.params(ct);
  for (const key in parameters) {
    if (Object.prototype.hasOwnProperty.call(parameters, key))
      this[key] = parameters[key];
  }

  this.links = {};

  // links
  try {
    if (header.link) {
      this.links = utils.parseLinks(header.link);
    }
  } catch (err) {
    // ignore
  }
};

/**
 * Set flags such as `.ok` based on `status`.
 *
 * For example a 2xx response will give you a `.ok` of __true__
 * whereas 5xx will be __false__ and `.error` will be __true__. The
 * `.clientError` and `.serverError` are also available to be more
 * specific, and `.statusType` is the class of error ranging from 1..5
 * sometimes useful for mapping respond colors etc.
 *
 * "sugar" properties are also defined for common cases. Currently providing:
 *
 *   - .noContent
 *   - .badRequest
 *   - .unauthorized
 *   - .notAcceptable
 *   - .notFound
 *
 * @param {Number} status
 * @api private
 */

ResponseBase.prototype._setStatusProperties = function (status) {
  const type = Math.trunc(status / 100);

  // status / class
  this.statusCode = status;
  this.status = this.statusCode;
  this.statusType = type;

  // basics
  this.info = type === 1;
  this.ok = type === 2;
  this.redirect = type === 3;
  this.clientError = type === 4;
  this.serverError = type === 5;
  this.error = type === 4 || type === 5 ? this.toError() : false;

  // sugar
  this.created = status === 201;
  this.accepted = status === 202;
  this.noContent = status === 204;
  this.badRequest = status === 400;
  this.unauthorized = status === 401;
  this.notAcceptable = status === 406;
  this.forbidden = status === 403;
  this.notFound = status === 404;
  this.unprocessableEntity = status === 422;
};
```

## File: `src/utils.js`
```javascript

/**
 * Return the mime type for the given `str`.
 *
 * @param {String} str
 * @return {String}
 * @api private
 */

exports.type = (string_) => string_.split(/ *; */).shift();

/**
 * Return header field parameters.
 *
 * @param {String} str
 * @return {Object}
 * @api private
 */

exports.params = (value) => {
  const object = {};
  for (const string_ of value.split(/ *; */)) {
    const parts = string_.split(/ *= */);
    const key = parts.shift();
    const value = parts.shift();

    if (key && value) object[key] = value;
  }

  return object;
};

/**
 * Parse Link header fields.
 *
 * @param {String} str
 * @return {Object}
 * @api private
 */

exports.parseLinks = (value) => {
  const object = {};
  for (const string_ of value.split(/ *, */)) {
    const parts = string_.split(/ *; */);
    const url = parts[0].slice(1, -1);
    const rel = parts[1].split(/ *= */)[1].slice(1, -1);
    object[rel] = url;
  }

  return object;
};

/**
 * Strip content related fields from `header`.
 *
 * @param {Object} header
 * @return {Object} header
 * @api private
 */

exports.cleanHeader = (header, changesOrigin) => {
  delete header['content-type'];
  delete header['content-length'];
  delete header['transfer-encoding'];
  delete header.host;
  // secuirty
  if (changesOrigin) {
    delete header.authorization;
    delete header.cookie;
  }

  return header;
};

exports.normalizeHostname = (hostname) => {
  const [,normalized] = hostname.match(/^\[([^\]]+)\]$/) || [];
  return normalized || hostname;
};

/**
 * Check if `obj` is an object.
 *
 * @param {Object} object
 * @return {Boolean}
 * @api private
 */
exports.isObject = (object) => {
  return object !== null && typeof object === 'object';
};

/**
 * Object.hasOwn fallback/polyfill.
 *
 * @type {(object: object, property: string) => boolean} object
 * @api private
 */
exports.hasOwn =
  Object.hasOwn ||
  function (object, property) {
    if (object == null) {
      throw new TypeError('Cannot convert undefined or null to object');
    }

    return Object.prototype.hasOwnProperty.call(new Object(object), property);
  };

exports.mixin = (target, source) => {
  for (const key in source) {
    if (exports.hasOwn(source, key)) {
      target[key] = source[key];
    }
  }
};

/**
 * Check if the response is compressed using Gzip or Deflate.
 * @param {Object} res
 * @return {Boolean}
 */

exports.isGzipOrDeflateEncoding = (res) => {
  return new RegExp(/^\s*(?:deflate|gzip)\s*$/).test(res.headers['content-encoding']);
};

/**
 * Check if the response is compressed using Brotli.
 * @param {Object} res
 * @return {Boolean}
 */

exports.isBrotliEncoding = (res) => {
  return new RegExp(/^\s*(?:br)\s*$/).test(res.headers['content-encoding']);
};
```

## File: `src/node/agent.js`
```javascript
/**
 * Module dependencies.
 */

const { CookieJar } = require('cookiejar');
const { CookieAccessInfo } = require('cookiejar');
const methods = require('methods');
const request = require('../..');
const AgentBase = require('../agent-base');

/**
 * Initialize a new `Agent`.
 *
 * @api public
 */

class Agent extends AgentBase {
  constructor (options) {
    super();

    this.jar = new CookieJar();

    if (options) {
      if (options.ca) {
        this.ca(options.ca);
      }

      if (options.key) {
        this.key(options.key);
      }

      if (options.pfx) {
        this.pfx(options.pfx);
      }

      if (options.cert) {
        this.cert(options.cert);
      }

      if (options.rejectUnauthorized === false) {
        this.disableTLSCerts();
      }
    }
  }

  /**
   * Save the cookies in the given `res` to
   * the agent's cookie jar for persistence.
   *
   * @param {Response} res
   * @api private
   */
  _saveCookies (res) {
    const cookies = res.headers['set-cookie'];
    if (cookies) {
      const url = new URL(res.request?.url || '');
      this.jar.setCookies(cookies, url.hostname, url.pathname);
    }
  }

  /**
   * Attach cookies when available to the given `req`.
   *
   * @param {Request} req
   * @api private
   */
  _attachCookies (request_) {
    const url = new URL(request_.url);
    const access = new CookieAccessInfo(
      url.hostname,
      url.pathname,
      url.protocol === 'https:'
    );
    const cookies = this.jar.getCookies(access).toValueString();
    request_.cookies = cookies;
  }
}

for (const name of methods) {
  const method = name.toUpperCase();
  if (method === "QUERY") continue;
  Agent.prototype[name] = function (url, fn) {
    const request_ = new request.Request(method, url);

    request_.on('response', this._saveCookies.bind(this));
    request_.on('redirect', this._saveCookies.bind(this));
    request_.on('redirect', this._attachCookies.bind(this, request_));
    this._setDefaults(request_);
    this._attachCookies(request_);

    if (fn) {
      request_.end(fn);
    }

    return request_;
  };
}

Agent.prototype.del = Agent.prototype.delete;

// create a Proxy that can instantiate a new Agent without using `new` keyword
// (for backward compatibility and chaining)
const proxyAgent = new Proxy(Agent, {
  apply (target, thisArg, argumentsList) {
    return new target(...argumentsList);
  }
});

module.exports = proxyAgent;
```

## File: `src/node/decompress.js`
```javascript
const zlib = require('zlib');
const utils = require('../utils');
const { isGzipOrDeflateEncoding, isBrotliEncoding } = utils;

exports.chooseDecompresser = (res) => {
  let decompresser;
  if (isGzipOrDeflateEncoding(res)) {
    decompresser = zlib.createUnzip();
  } else if (isBrotliEncoding(res)) {
    decompresser = zlib.createBrotliDecompress();
  } else {
    throw new Error('unknown content-encoding');
  }
  return decompresser;
}
```

## File: `src/node/http2wrapper.js`
```javascript
const http2 = require('http2');
const Stream = require('stream');
const net = require('net');
const tls = require('tls');

const {
  HTTP2_HEADER_PATH,
  HTTP2_HEADER_STATUS,
  HTTP2_HEADER_METHOD,
  HTTP2_HEADER_AUTHORITY,
  HTTP2_HEADER_HOST,
  HTTP2_HEADER_SET_COOKIE,
  NGHTTP2_CANCEL
} = http2.constants;

function setProtocol(protocol) {
  return {
    request(options) {
      return new Request(protocol, options);
    }
  };
}

function normalizeIpv6Host(host) {
  return net.isIP(host) === 6 ? `[${host}]` : host;
}

class Request extends Stream {
  constructor(protocol, options) {
    super();
    const defaultPort = protocol === 'https:' ? 443 : 80;
    const defaultHost = 'localhost';
    const port = options.port || defaultPort;
    const host = options.host || defaultHost;

    delete options.port;
    delete options.host;

    this.method = options.method;
    this.path = options.path;
    this.protocol = protocol;
    this.host = host;

    delete options.method;
    delete options.path;

    const sessionOptions = { ...options };
    if (options.socketPath) {
      sessionOptions.socketPath = options.socketPath;
      sessionOptions.createConnection = this.createUnixConnection.bind(this);
    }

    this._headers = {};

    const normalizedHost = normalizeIpv6Host(host);
    const session = http2.connect(
      `${protocol}//${normalizedHost}:${port}`,
      sessionOptions
    );
    this.setHeader('host', `${normalizedHost}:${port}`);

    session.on('error', (error) => this.emit('error', error));

    this.session = session;
  }

  createUnixConnection(authority, options) {
    switch (this.protocol) {
      case 'http:':
        return net.connect(options.socketPath);
      case 'https:':
        options.ALPNProtocols = ['h2'];
        options.servername = this.host;
        options.allowHalfOpen = true;
        return tls.connect(options.socketPath, options);
      default:
        throw new Error('Unsupported protocol', this.protocol);
    }
  }

  setNoDelay(bool) {
    // We can not use setNoDelay with HTTP/2.
    // Node 10 limits http2session.socket methods to ones safe to use with HTTP/2.
    // See also https://nodejs.org/api/http2.html#http2_http2session_socket
  }

  getFrame() {
    if (this.frame) {
      return this.frame;
    }

    const method = {
      [HTTP2_HEADER_PATH]: this.path,
      [HTTP2_HEADER_METHOD]: this.method
    };

    let headers = this.mapToHttp2Header(this._headers);

    headers = Object.assign(headers, method);

    const frame = this.session.request(headers);

    frame.once('response', (headers, flags) => {
      headers = this.mapToHttpHeader(headers);
      frame.headers = headers;
      frame.statusCode = headers[HTTP2_HEADER_STATUS];
      frame.status = frame.statusCode;
      this.emit('response', frame);
    });

    this._headerSent = true;

    frame.once('drain', () => this.emit('drain'));
    frame.on('error', (error) => this.emit('error', error));
    frame.on('close', () => this.session.close());

    this.frame = frame;
    return frame;
  }

  mapToHttpHeader(headers) {
    const keys = Object.keys(headers);
    const http2Headers = {};
    for (let key of keys) {
      let value = headers[key];
      key = key.toLowerCase();
      switch (key) {
        case HTTP2_HEADER_SET_COOKIE:
          value = Array.isArray(value) ? value : [value];
          break;
        default:
          break;
      }

      http2Headers[key] = value;
    }

    return http2Headers;
  }

  mapToHttp2Header(headers) {
    const keys = Object.keys(headers);
    const http2Headers = {};
    for (let key of keys) {
      let value = headers[key];
      key = key.toLowerCase();
      switch (key) {
        case HTTP2_HEADER_HOST:
          key = HTTP2_HEADER_AUTHORITY;
          value = /^http:\/\/|^https:\/\//.test(value)
            ? new URL(value).host
            : value;
          break;
        default:
          break;
      }

      http2Headers[key] = value;
    }

    return http2Headers;
  }

  setHeader(name, value) {
    this._headers[name.toLowerCase()] = value;
  }

  getHeader(name) {
    return this._headers[name.toLowerCase()];
  }

  write(data, encoding) {
    const frame = this.getFrame();
    return frame.write(data, encoding);
  }

  pipe(stream, options) {
    const frame = this.getFrame();
    return frame.pipe(stream, options);
  }

  end(data) {
    const frame = this.getFrame();
    frame.end(data);
  }

  abort(data) {
    const frame = this.getFrame();
    frame.close(NGHTTP2_CANCEL);
    this.session.destroy();
  }
}

exports.setProtocol = setProtocol;
```

## File: `src/node/index.js`
```javascript
/**
 * Module dependencies.
 */

const { format } = require('url');
const Stream = require('stream');
const https = require('https');
const http = require('http');
const fs = require('fs');
const zlib = require('zlib');
const util = require('util');
const qs = require('qs');
const mime = require('mime');
let methods = require('methods');
const FormData = require('form-data');
const formidable = require('formidable');
const debug = require('debug')('superagent');
const CookieJar = require('cookiejar');
const safeStringify = require('fast-safe-stringify');

const utils = require('../utils');
const RequestBase = require('../request-base');
const http2 = require('./http2wrapper');
const { decompress } = require('./unzip');
const Response = require('./response');

const { mixin, hasOwn, isBrotliEncoding, isGzipOrDeflateEncoding } = utils;
const { chooseDecompresser } = require('./decompress');

function request(method, url) {
  // callback
  if (typeof url === 'function') {
    return new exports.Request('GET', method).end(url);
  }

  // url first
  if (arguments.length === 1) {
    return new exports.Request('GET', method);
  }

  return new exports.Request(method, url);
}

module.exports = request;
exports = module.exports;

/**
 * Expose `Request`.
 */

exports.Request = Request;

/**
 * Expose the agent function
 */

exports.agent = require('./agent');

/**
 * Noop.
 */

function noop() {}

/**
 * Expose `Response`.
 */

exports.Response = Response;

/**
 * Define "form" mime type.
 */

mime.define(
  {
    'application/x-www-form-urlencoded': ['form', 'urlencoded', 'form-data']
  },
  true
);

/**
 * Protocol map.
 */

exports.protocols = {
  'http:': http,
  'https:': https,
  'http2:': http2
};

/**
 * Default serialization map.
 *
 *     superagent.serialize['application/xml'] = function(obj){
 *       return 'generated xml here';
 *     };
 *
 */

exports.serialize = {
  'application/x-www-form-urlencoded': (obj) => {
    return qs.stringify(obj, { indices: false, strictNullHandling: true });
  },
  'application/json': safeStringify
};

/**
 * Default parsers.
 *
 *     superagent.parse['application/xml'] = function(res, fn){
 *       fn(null, res);
 *     };
 *
 */

exports.parse = require('./parsers');

/**
 * Default buffering map. Can be used to set certain
 * response types to buffer/not buffer.
 *
 *     superagent.buffer['application/xml'] = true;
 */
exports.buffer = {};

/**
 * Initialize internal header tracking properties on a request instance.
 *
 * @param {Object} req the instance
 * @api private
 */
function _initHeaders(request_) {
  request_._header = {
    // coerces header names to lowercase
  };
  request_.header = {
    // preserves header name case
  };
}

/**
 * Initialize a new `Request` with the given `method` and `url`.
 *
 * @param {String} method
 * @param {String|Object} url
 * @api public
 */

function Request(method, url) {
  Stream.call(this);
  if (typeof url !== 'string') url = format(url);
  this._enableHttp2 = Boolean(process.env.HTTP2_TEST); // internal only
  this._agent = false;
  this._formData = null;
  this.method = method;
  this.url = url;
  _initHeaders(this);
  this.writable = true;
  this._redirects = 0;
  this.redirects(method === 'HEAD' ? 0 : 5);
  this.cookies = '';
  this.qs = {};
  this._query = [];
  this.qsRaw = this._query; // Unused, for backwards compatibility only
  this._redirectList = [];
  this._streamRequest = false;
  this._lookup = undefined;
  this.once('end', this.clearTimeout.bind(this));
}

/**
 * Inherit from `Stream` (which inherits from `EventEmitter`).
 * Mixin `RequestBase`.
 */
util.inherits(Request, Stream);

mixin(Request.prototype, RequestBase.prototype);

/**
 * Enable or Disable http2.
 *
 * Enable http2.
 *
 * ``` js
 * request.get('http://localhost/')
 *   .http2()
 *   .end(callback);
 *
 * request.get('http://localhost/')
 *   .http2(true)
 *   .end(callback);
 * ```
 *
 * Disable http2.
 *
 * ``` js
 * request = request.http2();
 * request.get('http://localhost/')
 *   .http2(false)
 *   .end(callback);
 * ```
 *
 * @param {Boolean} enable
 * @return {Request} for chaining
 * @api public
 */

Request.prototype.http2 = function (bool) {
  if (exports.protocols['http2:'] === undefined) {
    throw new Error(
      'superagent: this version of Node.js does not support http2'
    );
  }

  this._enableHttp2 = bool === undefined ? true : bool;
  return this;
};

/**
 * Queue the given `file` as an attachment to the specified `field`,
 * with optional `options` (or filename).
 *
 * ``` js
 * request.post('http://localhost/upload')
 *   .attach('field', Buffer.from('<b>Hello world</b>'), 'hello.html')
 *   .end(callback);
 * ```
 *
 * A filename may also be used:
 *
 * ``` js
 * request.post('http://localhost/upload')
 *   .attach('files', 'image.jpg')
 *   .end(callback);
 * ```
 *
 * @param {String} field
 * @param {String|fs.ReadStream|Buffer} file
 * @param {String|Object} options
 * @return {Request} for chaining
 * @api public
 */

Request.prototype.attach = function (field, file, options) {
  if (file) {
    if (this._data) {
      throw new Error("superagent can't mix .send() and .attach()");
    }

    let o = options || {};
    if (typeof options === 'string') {
      o = { filename: options };
    }

    if (typeof file === 'string') {
      if (!o.filename) o.filename = file;
      debug('creating `fs.ReadStream` instance for file: %s', file);
      file = fs.createReadStream(file);
      file.on('error', (error) => {
        const formData = this._getFormData();
        formData.emit('error', error);
      });
    } else if (!o.filename && file.path) {
      o.filename = file.path;
    }

    this._getFormData().append(field, file, o);
  }

  return this;
};

Request.prototype._getFormData = function () {
  if (!this._formData) {
    this._formData = new FormData();
    this._formData.on('error', (error) => {
      debug('FormData error', error);
      if (this.called) {
        // The request has already finished and the callback was called.
        // Silently ignore the error.
        return;
      }

      this.callback(error);
      this.abort();
    });
  }

  return this._formData;
};

/**
 * Gets/sets the `Agent` to use for this HTTP request. The default (if this
 * function is not called) is to opt out of connection pooling (`agent: false`).
 *
 * @param {http.Agent} agent
 * @return {http.Agent}
 * @api public
 */

Request.prototype.agent = function (agent) {
  if (arguments.length === 0) return this._agent;
  this._agent = agent;
  return this;
};

/**
 * Gets/sets the `lookup` function to use custom DNS resolver.
 *
 * @param {Function} lookup
 * @return {Function}
 * @api public
 */

Request.prototype.lookup = function (lookup) {
  if (arguments.length === 0) return this._lookup;
  this._lookup = lookup;
  return this;
};

/**
 * Set _Content-Type_ response header passed through `mime.getType()`.
 *
 * Examples:
 *
 *      request.post('/')
 *        .type('xml')
 *        .send(xmlstring)
 *        .end(callback);
 *
 *      request.post('/')
 *        .type('json')
 *        .send(jsonstring)
 *        .end(callback);
 *
 *      request.post('/')
 *        .type('application/json')
 *        .send(jsonstring)
 *        .end(callback);
 *
 * @param {String} type
 * @return {Request} for chaining
 * @api public
 */

Request.prototype.type = function (type) {
  return this.set(
    'Content-Type',
    type.includes('/') ? type : mime.getType(type)
  );
};

/**
 * Set _Accept_ response header passed through `mime.getType()`.
 *
 * Examples:
 *
 *      superagent.types.json = 'application/json';
 *
 *      request.get('/agent')
 *        .accept('json')
 *        .end(callback);
 *
 *      request.get('/agent')
 *        .accept('application/json')
 *        .end(callback);
 *
 * @param {String} accept
 * @return {Request} for chaining
 * @api public
 */

Request.prototype.accept = function (type) {
  return this.set('Accept', type.includes('/') ? type : mime.getType(type));
};

/**
 * Add query-string `val`.
 *
 * Examples:
 *
 *   request.get('/shoes')
 *     .query('size=10')
 *     .query({ color: 'blue' })
 *
 * @param {Object|String} val
 * @return {Request} for chaining
 * @api public
 */

Request.prototype.query = function (value) {
  if (typeof value === 'string') {
    this._query.push(value);
  } else {
    Object.assign(this.qs, value);
  }

  return this;
};

/**
 * Write raw `data` / `encoding` to the socket.
 *
 * @param {Buffer|String} data
 * @param {String} encoding
 * @return {Boolean}
 * @api public
 */

Request.prototype.write = function (data, encoding) {
  const request_ = this.request();
  if (!this._streamRequest) {
    this._streamRequest = true;
  }

  return request_.write(data, encoding);
};

/**
 * Pipe the request body to `stream`.
 *
 * @param {Stream} stream
 * @param {Object} options
 * @return {Stream}
 * @api public
 */

Request.prototype.pipe = function (stream, options) {
  this.piped = true; // HACK...
  this.buffer(false);
  this.end();
  return this._pipeContinue(stream, options);
};

Request.prototype._pipeContinue = function (stream, options) {
  this.req.once('response', (res) => {
    // redirect
    if (
      isRedirect(res.statusCode) &&
      this._redirects++ !== this._maxRedirects
    ) {
      return this._redirect(res) === this
        ? this._pipeContinue(stream, options)
        : undefined;
    }

    this.res = res;
    this._emitResponse();
    if (this._aborted) return;

    if (this._shouldDecompress(res)) {

      let decompresser = chooseDecompresser(res);

      decompresser.on('error', (error) => {
        if (error && error.code === 'Z_BUF_ERROR') {
          // unexpected end of file is ignored by browsers and curl
          stream.emit('end');
          return;
        }

        stream.emit('error', error);
      });
      res.pipe(decompresser).pipe(stream, options);
      // don't emit 'end' until decompresser has completed writing all its data.
      decompresser.once('end', () => this.emit('end'));
    } else {
      res.pipe(stream, options);
      res.once('end', () => this.emit('end'));
    }
  });
  return stream;
};

/**
 * Enable / disable buffering.
 *
 * @return {Boolean} [val]
 * @return {Request} for chaining
 * @api public
 */

Request.prototype.buffer = function (value) {
  this._buffer = value !== false;
  return this;
};

/**
 * Redirect to `url
 *
 * @param {IncomingMessage} res
 * @return {Request} for chaining
 * @api private
 */

Request.prototype._redirect = function (res) {
  let url = res.headers.location;
  if (!url) {
    return this.callback(new Error('No location header for redirect'), res);
  }

  debug('redirect %s -> %s', this.url, url);

  // location
  url = new URL(url, this.url).href;

  // ensure the response is being consumed
  // this is required for Node v0.10+
  res.resume();

  let headers = this.req.getHeaders ? this.req.getHeaders() : this.req._headers;

  const changesOrigin = new URL(url).host !== new URL(this.url).host;

  // implementation of 302 following defacto standard
  if (res.statusCode === 301 || res.statusCode === 302) {
    // strip Content-* related fields
    // in case of POST etc
    headers = utils.cleanHeader(headers, changesOrigin);

    // force GET
    this.method = this.method === 'HEAD' ? 'HEAD' : 'GET';

    // clear data
    this._data = null;
  }

  // 303 is always GET
  if (res.statusCode === 303) {
    // strip Content-* related fields
    // in case of POST etc
    headers = utils.cleanHeader(headers, changesOrigin);

    // force method
    this.method = 'GET';

    // clear data
    this._data = null;
  }

  // 307 preserves method
  // 308 preserves method
  delete headers.host;

  delete this.req;
  delete this._formData;

  // remove all add header except User-Agent
  _initHeaders(this);

  // redirect
  this.res = res;
  this._endCalled = false;
  this.url = url;
  this.qs = {};
  this._query.length = 0;
  this.set(headers);
  this._emitRedirect();
  this._redirectList.push(this.url);
  this.end(this._callback);
  return this;
};

/**
 * Set Authorization field value with `user` and `pass`.
 *
 * Examples:
 *
 *   .auth('tobi', 'learnboost')
 *   .auth('tobi:learnboost')
 *   .auth('tobi')
 *   .auth(accessToken, { type: 'bearer' })
 *
 * @param {String} user
 * @param {String} [pass]
 * @param {Object} [options] options with authorization type 'basic' or 'bearer' ('basic' is default)
 * @return {Request} for chaining
 * @api public
 */

Request.prototype.auth = function (user, pass, options) {
  if (arguments.length === 1) pass = '';
  if (typeof pass === 'object' && pass !== null) {
    // pass is optional and can be replaced with options
    options = pass;
    pass = '';
  }

  if (!options) {
    options = { type: 'basic' };
  }

  const encoder = (string) => Buffer.from(string).toString('base64');

  return this._auth(user, pass, options, encoder);
};

/**
 * Set the certificate authority option for https request.
 *
 * @param {Buffer | Array} cert
 * @return {Request} for chaining
 * @api public
 */

Request.prototype.ca = function (cert) {
  this._ca = cert;
  return this;
};

/**
 * Set the client certificate key option for https request.
 *
 * @param {Buffer | String} cert
 * @return {Request} for chaining
 * @api public
 */

Request.prototype.key = function (cert) {
  this._key = cert;
  return this;
};

/**
 * Set the key, certificate, and CA certs of the client in PFX or PKCS12 format.
 *
 * @param {Buffer | String} cert
 * @return {Request} for chaining
 * @api public
 */

Request.prototype.pfx = function (cert) {
  if (typeof cert === 'object' && !Buffer.isBuffer(cert)) {
    this._pfx = cert.pfx;
    this._passphrase = cert.passphrase;
  } else {
    this._pfx = cert;
  }

  return this;
};

/**
 * Set the client certificate option for https request.
 *
 * @param {Buffer | String} cert
 * @return {Request} for chaining
 * @api public
 */

Request.prototype.cert = function (cert) {
  this._cert = cert;
  return this;
};

/**
 * Do not reject expired or invalid TLS certs.
 * sets `rejectUnauthorized=true`. Be warned that this allows MITM attacks.
 *
 * @return {Request} for chaining
 * @api public
 */

Request.prototype.disableTLSCerts = function () {
  this._disableTLSCerts = true;
  return this;
};

/**
 * Return an http[s] request.
 *
 * @return {OutgoingMessage}
 * @api private
 */

// eslint-disable-next-line complexity
Request.prototype.request = function () {
  if (this.req) return this.req;

  const options = {};

  try {
    const query = qs.stringify(this.qs, {
      indices: false,
      strictNullHandling: true
    });
    if (query) {
      this.qs = {};
      this._query.push(query);
    }

    this._finalizeQueryString();
  } catch (err) {
    return this.emit('error', err);
  }

  let { url: urlString } = this;
  const retries = this._retries;

  // default to http://
  if (urlString.indexOf('http') !== 0) urlString = `http://${urlString}`;
  const url = new URL(urlString);
  let { protocol } = url;
  let path = `${url.pathname}${url.search}`;

  // support unix sockets
  if (/^https?\+unix:/.test(protocol) === true) {
    // get the protocol
    protocol = `${protocol.split('+')[0]}:`;

    // get the socket path
    options.socketPath = url.hostname.replace(/%2F/g, '/');
    url.host = '';
    url.hostname = '';
  }

  // Override IP address of a hostname
  if (this._connectOverride) {
    const { hostname } = url;
    const match =
      hostname in this._connectOverride
        ? this._connectOverride[hostname]
        : this._connectOverride['*'];
    if (match) {
      // backup the real host
      if (!this._header.host) {
        this.set('host', url.host);
      }

      let newHost;
      let newPort;

      if (typeof match === 'object') {
        newHost = match.host;
        newPort = match.port;
      } else {
        newHost = match;
        newPort = url.port;
      }

      // wrap [ipv6]
      url.host = /:/.test(newHost) ? `[${newHost}]` : newHost;
      if (newPort) {
        url.host += `:${newPort}`;
        url.port = newPort;
      }

      url.hostname = newHost;
    }
  }

  // options
  options.method = this.method;
  options.port = url.port;
  options.path = path;
  options.host = utils.normalizeHostname(url.hostname); // ex: [::1] -> ::1
  options.ca = this._ca;
  options.key = this._key;
  options.pfx = this._pfx;
  options.cert = this._cert;
  options.passphrase = this._passphrase;
  options.agent = this._agent;
  options.lookup = this._lookup;
  options.rejectUnauthorized =
    typeof this._disableTLSCerts === 'boolean'
      ? !this._disableTLSCerts
      : process.env.NODE_TLS_REJECT_UNAUTHORIZED !== '0';

  // Allows request.get('https://1.2.3.4/').set('Host', 'example.com')
  if (this._header.host) {
    options.servername = this._header.host.replace(/:\d+$/, '');
  }

  if (
    this._trustLocalhost &&
    /^(?:localhost|127\.0\.0\.\d+|(0*:)+:0*1)$/.test(url.hostname)
  ) {
    options.rejectUnauthorized = false;
  }

  // initiate request
  const module_ = this._enableHttp2
    ? exports.protocols['http2:'].setProtocol(protocol)
    : exports.protocols[protocol];

  // request
  this.req = module_.request(options);
  const { req } = this;

  // set tcp no delay
  req.setNoDelay(true);

  if (options.method !== 'HEAD') {
    req.setHeader('Accept-Encoding', 'gzip, deflate');
  }

  this.protocol = protocol;
  this.host = url.host;

  // expose events
  req.once('drain', () => {
    this.emit('drain');
  });

  req.on('error', (error) => {
    // flag abortion here for out timeouts
    // because node will emit a faux-error "socket hang up"
    // when request is aborted before a connection is made
    if (this._aborted) return;
    // if not the same, we are in the **old** (cancelled) request,
    // so need to continue (same as for above)
    if (this._retries !== retries) return;
    // if we've received a response then we don't want to let
    // an error in the request blow up the response
    if (this.response) return;
    this.callback(error);
  });

  // auth
  if (url.username || url.password) {
    this.auth(url.username, url.password);
  }

  if (this.username && this.password) {
    this.auth(this.username, this.password);
  }

  for (const key in this.header) {
    if (hasOwn(this.header, key)) req.setHeader(key, this.header[key]);
  }

  // add cookies
  if (this.cookies) {
    if (hasOwn(this._header, 'cookie')) {
      // merge
      const temporaryJar = new CookieJar.CookieJar();
      temporaryJar.setCookies(this._header.cookie.split('; '));
      temporaryJar.setCookies(this.cookies.split('; '));
      req.setHeader(
        'Cookie',
        temporaryJar.getCookies(CookieJar.CookieAccessInfo.All).toValueString()
      );
    } else {
      req.setHeader('Cookie', this.cookies);
    }
  }

  return req;
};

/**
 * Invoke the callback with `err` and `res`
 * and handle arity check.
 *
 * @param {Error} err
 * @param {Response} res
 * @api private
 */

Request.prototype.callback = function (error, res) {
  if (this._shouldRetry(error, res)) {
    return this._retry();
  }

  // Avoid the error which is emitted from 'socket hang up' to cause the fn undefined error on JS runtime.
  const fn = this._callback || noop;
  this.clearTimeout();
  if (this.called) return console.warn('superagent: double callback bug');
  this.called = true;

  if (!error) {
    try {
      if (!this._isResponseOK(res)) {
        let message = 'Unsuccessful HTTP response';
        if (res) {
          message = http.STATUS_CODES[res.status] || message;
        }

        error = new Error(message);
        error.status = res ? res.status : undefined;
      }
    } catch (err) {
      error = err;
      error.status = error.status || (res ? res.status : undefined);
    }
  }

  // It's important that the callback is called outside try/catch
  // to avoid double callback
  if (!error) {
    return fn(null, res);
  }

  error.response = res;
  if (this._maxRetries) error.retries = this._retries - 1;

  // only emit error event if there is a listener
  // otherwise we assume the callback to `.end()` will get the error
  if (error && this.listeners('error').length > 0) {
    this.emit('error', error);
  }

  fn(error, res);
};

/**
 * Check if `obj` is a host object,
 *
 * @param {Object} obj host object
 * @return {Boolean} is a host object
 * @api private
 */
Request.prototype._isHost = function (object) {
  return (
    Buffer.isBuffer(object) ||
    object instanceof Stream ||
    object instanceof FormData
  );
};

/**
 * Initiate request, invoking callback `fn(err, res)`
 * with an instanceof `Response`.
 *
 * @param {Function} fn
 * @return {Request} for chaining
 * @api public
 */

Request.prototype._emitResponse = function (body, files) {
  const response = new Response(this);
  this.response = response;
  response.redirects = this._redirectList;
  if (undefined !== body) {
    response.body = body;
  }

  response.files = files;
  if (this._endCalled) {
    response.pipe = function () {
      throw new Error(
        "end() has already been called, so it's too late to start piping"
      );
    };
  }

  this.emit('response', response);
  return response;
};

/**
 * Emit `redirect` event, passing an instanceof `Response`.
 *
 * @api private
 */

Request.prototype._emitRedirect = function () {
  const response = new Response(this);
  response.redirects = this._redirectList;
  this.emit('redirect', response);
};

Request.prototype.end = function (fn) {
  this.request();
  debug('%s %s', this.method, this.url);

  if (this._endCalled) {
    throw new Error(
      '.end() was called twice. This is not supported in superagent'
    );
  }

  this._endCalled = true;

  // store callback
  this._callback = fn || noop;

  this._end();
};

Request.prototype._end = function () {
  if (this._aborted)
    return this.callback(
      new Error('The request has been aborted even before .end() was called')
    );

  let data = this._data;
  const { req } = this;
  const { method } = this;

  this._setTimeouts();

  // body
  if (method !== 'HEAD' && !req._headerSent) {
    // serialize stuff
    if (typeof data !== 'string') {
      let contentType = req.getHeader('Content-Type');
      // Parse out just the content type from the header (ignore the charset)
      if (contentType) contentType = contentType.split(';')[0];
      let serialize = this._serializer || exports.serialize[contentType];
      if (!serialize && isJSON(contentType)) {
        serialize = exports.serialize['application/json'];
      }

      if (serialize) data = serialize(data);
    }

    // content-length
    if (data && !req.getHeader('Content-Length')) {
      req.setHeader(
        'Content-Length',
        Buffer.isBuffer(data) ? data.length : Buffer.byteLength(data)
      );
    }
  }

  // response
  // eslint-disable-next-line complexity
  req.once('response', (res) => {
    debug('%s %s -> %s', this.method, this.url, res.statusCode);

    if (this._responseTimeoutTimer) {
      clearTimeout(this._responseTimeoutTimer);
    }

    if (this.piped) {
      return;
    }

    const max = this._maxRedirects;
    const mime = utils.type(res.headers['content-type'] || '') || 'text/plain';
    let type = mime.split('/')[0];
    if (type) type = type.toLowerCase().trim();
    const multipart = type === 'multipart';
    const redirect = isRedirect(res.statusCode);
    const responseType = this._responseType;

    this.res = res;

    // redirect
    if (redirect && this._redirects++ !== max) {
      return this._redirect(res);
    }

    if (this.method === 'HEAD') {
      this.emit('end');
      this.callback(null, this._emitResponse());
      return;
    }

    // zlib support
    if (this._shouldDecompress(res)) {
      decompress(req, res);
    }

    let buffer = this._buffer;
    if (buffer === undefined && mime in exports.buffer) {
      buffer = Boolean(exports.buffer[mime]);
    }

    let parser = this._parser;
    if (undefined === buffer && parser) {
      console.warn(
        "A custom superagent parser has been set, but buffering strategy for the parser hasn't been configured. Call `req.buffer(true or false)` or set `superagent.buffer[mime] = true or false`"
      );
      buffer = true;
    }

    if (!parser) {
      if (responseType) {
        parser = exports.parse.image; // It's actually a generic Buffer
        buffer = true;
      } else if (multipart) {
        const form = formidable.formidable();
        parser = (res, callback) => {
          // Create a PassThrough stream that acts as a proper HTTP request
          const bridgeStream = new Stream.PassThrough();

          // Add HTTP request properties from the current request context
          bridgeStream.method = this.method || 'POST';
          bridgeStream.url = this.url || '/';
          bridgeStream.httpVersion = res.httpVersion || '1.1';
          bridgeStream.headers = res.headers || {};
          bridgeStream.socket = res.socket || { readable: true };

          // Pipe the response data through the bridge stream
          res.pipe(bridgeStream);

          form.parse(bridgeStream, (err, fields, files) => {
            if (err) return callback(err);

            // Formidable v3 always returns arrays, but SuperAgent expects single values
            // Flatten single-item arrays to maintain backward compatibility
            const flattenedFields = {};
            if (fields) {
              for (const key in fields) {
                const value = fields[key];
                flattenedFields[key] = Array.isArray(value) && value.length === 1 ? value[0] : value;
              }
            }

            const flattenedFiles = {};
            if (files) {
              for (const key in files) {
                const value = files[key];
                flattenedFiles[key] = Array.isArray(value) && value.length === 1 ? value[0] : value;
              }
            }

            // Return flattened fields as the object parameter to match SuperAgent's expected format
            callback(null, flattenedFields, flattenedFiles);
          });
        };
        buffer = true;
      } else if (isBinary(mime)) {
        parser = exports.parse.image;
        buffer = true; // For backwards-compatibility buffering default is ad-hoc MIME-dependent
      } else if (exports.parse[mime]) {
        parser = exports.parse[mime];
      } else if (type === 'text') {
        parser = exports.parse.text;
        buffer = buffer !== false;
        // everyone wants their own white-labeled json
      } else if (isJSON(mime)) {
        parser = exports.parse['application/json'];
        buffer = buffer !== false;
      } else if (buffer) {
        parser = exports.parse.text;
      } else if (undefined === buffer) {
        parser = exports.parse.image; // It's actually a generic Buffer
        buffer = true;
      }
    }

    // by default only buffer text/*, json and messed up thing from hell
    if ((undefined === buffer && isText(mime)) || isJSON(mime)) {
      buffer = true;
    }

    this._resBuffered = buffer;
    let parserHandlesEnd = false;
    if (buffer) {
      // Protectiona against zip bombs and other nuisance
      let responseBytesLeft = this._maxResponseSize || 200000000;
      res.on('data', (buf) => {
        responseBytesLeft -= buf.byteLength || buf.length > 0 ? buf.length : 0;
        if (responseBytesLeft < 0) {
          // This will propagate through error event
          const error = new Error('Maximum response size reached');
          error.code = 'ETOOLARGE';
          // Parsers aren't required to observe error event,
          // so would incorrectly report success
          parserHandlesEnd = false;
          // Will not emit error event
          res.destroy(error);
          // so we do callback now
          this.callback(error, null);
        }
      });
    }

    if (parser) {
      try {
        // Unbuffered parsers are supposed to emit response early,
        // which is weird BTW, because response.body won't be there.
        parserHandlesEnd = buffer;

        parser(res, (error, object, files) => {
          if (this.timedout) {
            // Timeout has already handled all callbacks
            return;
          }

          // Intentional (non-timeout) abort is supposed to preserve partial response,
          // even if it doesn't parse.
          if (error && !this._aborted) {
            return this.callback(error);
          }

          if (parserHandlesEnd) {
            this.emit('end');
            this.callback(null, this._emitResponse(object, files));
          }
        });
      } catch (err) {
        this.callback(err);
        return;
      }
    }

    this.res = res;

    // unbuffered
    if (!buffer) {
      debug('unbuffered %s %s', this.method, this.url);
      this.callback(null, this._emitResponse());
      if (multipart) return; // allow multipart to handle end event
      res.once('end', () => {
        debug('end %s %s', this.method, this.url);
        this.emit('end');
      });
      return;
    }

    // terminating events
    res.once('error', (error) => {
      parserHandlesEnd = false;
      this.callback(error, null);
    });
    if (!parserHandlesEnd)
      res.once('end', () => {
        debug('end %s %s', this.method, this.url);
        // TODO: unless buffering emit earlier to stream
        this.emit('end');
        this.callback(null, this._emitResponse());
      });
  });

  this.emit('request', this);

  const getProgressMonitor = () => {
    const lengthComputable = true;
    const total = req.getHeader('Content-Length');
    let loaded = 0;

    const progress = new Stream.Transform();
    progress._transform = (chunk, encoding, callback) => {
      loaded += chunk.length;
      this.emit('progress', {
        direction: 'upload',
        lengthComputable,
        loaded,
        total
      });
      callback(null, chunk);
    };

    return progress;
  };

  const bufferToChunks = (buffer) => {
    const chunkSize = 16 * 1024; // default highWaterMark value
    const chunking = new Stream.Readable();
    const totalLength = buffer.length;
    const remainder = totalLength % chunkSize;
    const cutoff = totalLength - remainder;

    for (let i = 0; i < cutoff; i += chunkSize) {
      const chunk = buffer.slice(i, i + chunkSize);
      chunking.push(chunk);
    }

    if (remainder > 0) {
      const remainderBuffer = buffer.slice(-remainder);
      chunking.push(remainderBuffer);
    }

    chunking.push(null); // no more data

    return chunking;
  };

  // if a FormData instance got created, then we send that as the request body
  const formData = this._formData;
  if (formData) {
    // set headers
    const headers = formData.getHeaders();
    for (const i in headers) {
      if (hasOwn(headers, i)) {
        debug('setting FormData header: "%s: %s"', i, headers[i]);
        req.setHeader(i, headers[i]);
      }
    }

    // attempt to get "Content-Length" header
    formData.getLength((error, length) => {
      // TODO: Add chunked encoding when no length (if err)
      if (error) debug('formData.getLength had error', error, length);

      debug('got FormData Content-Length: %s', length);
      if (typeof length === 'number') {
        req.setHeader('Content-Length', length);
      }

      formData.pipe(getProgressMonitor()).pipe(req);
    });
  } else if (Buffer.isBuffer(data)) {
    bufferToChunks(data).pipe(getProgressMonitor()).pipe(req);
  } else {
    req.end(data);
  }
};

// Check whether response has a non-0-sized gzip-encoded body
Request.prototype._shouldDecompress = (res) => {
  return hasNonEmptyResponseContent(res) && (isGzipOrDeflateEncoding(res) || isBrotliEncoding(res));
};


/**
 * Overrides DNS for selected hostnames. Takes object mapping hostnames to IP addresses.
 *
 * When making a request to a URL with a hostname exactly matching a key in the object,
 * use the given IP address to connect, instead of using DNS to resolve the hostname.
 *
 * A special host `*` matches every hostname (keep redirects in mind!)
 *
 *      request.connect({
 *        'test.example.com': '127.0.0.1',
 *        'ipv6.example.com': '::1',
 *      })
 */
Request.prototype.connect = function (connectOverride) {
  if (typeof connectOverride === 'string') {
    this._connectOverride = { '*': connectOverride };
  } else if (typeof connectOverride === 'object') {
    this._connectOverride = connectOverride;
  } else {
    this._connectOverride = undefined;
  }

  return this;
};

Request.prototype.trustLocalhost = function (toggle) {
  this._trustLocalhost = toggle === undefined ? true : toggle;
  return this;
};

// generate HTTP verb methods
if (!methods.includes('del')) {
  // create a copy so we don't cause conflicts with
  // other packages using the methods package and
  // npm 3.x
  methods = [...methods];
  methods.push('del');
}

for (let method of methods) {
  const name = method;
  method = method === 'del' ? 'delete' : method;

  method = method.toUpperCase();
  request[name] = (url, data, fn) => {
    const request_ = request(method, url);
    if (typeof data === 'function') {
      fn = data;
      data = null;
    }

    if (data) {
      if (method === 'GET' || method === 'HEAD') {
        request_.query(data);
      } else {
        request_.send(data);
      }
    }

    if (fn) request_.end(fn);
    return request_;
  };
}

/**
 * Check if `mime` is text and should be buffered.
 *
 * @param {String} mime
 * @return {Boolean}
 * @api public
 */

function isText(mime) {
  const parts = mime.split('/');
  let type = parts[0];
  if (type) type = type.toLowerCase().trim();
  let subtype = parts[1];
  if (subtype) subtype = subtype.toLowerCase().trim();

  return type === 'text' || subtype === 'x-www-form-urlencoded';
}

// This is not a catchall, but a start. It might be useful
// in the long run to have file that includes all binary
// content types from https://www.iana.org/assignments/media-types/media-types.xhtml
function isBinary(mime) {
  let [registry, name] = mime.split('/');
  if (registry) registry = registry.toLowerCase().trim();
  if (name) name = name.toLowerCase().trim();
  return (
    ['audio', 'font', 'image', 'video'].includes(registry) ||
    ['gz', 'gzip'].includes(name)
  );
}

/**
 * Check if `mime` is json or has +json structured syntax suffix.
 *
 * @param {String} mime
 * @return {Boolean}
 * @api private
 */

function isJSON(mime) {
  // should match /json or +json
  // but not /json-seq
  return /[/+]json($|[^-\w])/i.test(mime);
}

/**
 * Check if we should follow the redirect `code`.
 *
 * @param {Number} code
 * @return {Boolean}
 * @api private
 */

function isRedirect(code) {
  return [301, 302, 303, 305, 307, 308].includes(code);
}

function hasNonEmptyResponseContent(res) {
  if (res.statusCode === 204 || res.statusCode === 304) {
    // These aren't supposed to have any body
    return false;
  }

  // header content is a string, and distinction between 0 and no information is crucial
  if (res.headers['content-length'] === '0') {
    // We know that the body is empty (unfortunately, this check does not cover chunked encoding)
    return false;
  }

  return true;
}
```

## File: `src/node/response.js`
```javascript
/**
 * Module dependencies.
 */

const util = require('util');
const Stream = require('stream');
const ResponseBase = require('../response-base');
const { mixin } = require('../utils');

/**
 * Expose `Response`.
 */

module.exports = Response;

/**
 * Initialize a new `Response` with the given `xhr`.
 *
 *  - set flags (.ok, .error, etc)
 *  - parse header
 *
 * @param {Request} req
 * @param {Object} options
 * @constructor
 * @extends {Stream}
 * @implements {ReadableStream}
 * @api private
 */

function Response(request) {
  Stream.call(this);
  this.res = request.res;
  const { res } = this;
  this.request = request;
  this.req = request.req;
  this.text = res.text;
  this.files = res.files || {};
  this.buffered = request._resBuffered;
  this.headers = res.headers;
  this.header = this.headers;
  this._setStatusProperties(res.statusCode);
  this._setHeaderProperties(this.header);
  this.setEncoding = res.setEncoding.bind(res);
  res.on('data', this.emit.bind(this, 'data'));
  res.on('end', this.emit.bind(this, 'end'));
  res.on('close', this.emit.bind(this, 'close'));
  res.on('error', this.emit.bind(this, 'error'));
}

// Lazy access res.body.
// https://github.com/nodejs/node/pull/39520#issuecomment-889697136
Object.defineProperty(Response.prototype, 'body', {
  get() {
    return this._body !== undefined
      ? this._body
      : this.res.body !== undefined
      ? this.res.body
      : {};
  },
  set(value) {
    this._body = value;
  }
});

/**
 * Inherit from `Stream`.
 */

util.inherits(Response, Stream);

mixin(Response.prototype, ResponseBase.prototype);

/**
 * Implements methods of a `ReadableStream`
 */

Response.prototype.destroy = function (error) {
  this.res.destroy(error);
};

/**
 * Pause.
 */

Response.prototype.pause = function () {
  this.res.pause();
};

/**
 * Resume.
 */

Response.prototype.resume = function () {
  this.res.resume();
};

/**
 * Return an `Error` representative of this response.
 *
 * @return {Error}
 * @api public
 */

Response.prototype.toError = function () {
  const { req } = this;
  const { method } = req;
  const { path } = req;

  const message = `cannot ${method} ${path} (${this.status})`;
  const error = new Error(message);
  error.status = this.status;
  error.text = this.text;
  error.method = method;
  error.path = path;

  return error;
};

Response.prototype.setStatusProperties = function (status) {
  console.warn('In superagent 2.x setStatusProperties is a private method');
  return this._setStatusProperties(status);
};

/**
 * To json.
 *
 * @return {Object}
 * @api public
 */

Response.prototype.toJSON = function () {
  return {
    req: this.request.toJSON(),
    header: this.header,
    status: this.status,
    text: this.text
  };
};
```

## File: `src/node/unzip.js`
```javascript
/**
 * Module dependencies.
 */

const { StringDecoder } = require('string_decoder');
const Stream = require('stream');
const { chooseDecompresser } = require('./decompress');

/**
 * Buffers response data events and re-emits when they're decompressed.
 *
 * @param {Request} req
 * @param {Response} res
 * @api private
 */

exports.decompress = (request, res) => {
  let decompresser = chooseDecompresser(res);

  const stream = new Stream();
  let decoder;

  // make node responseOnEnd() happy
  stream.req = request;

  decompresser.on('error', (error) => {
    if (error && error.code === 'Z_BUF_ERROR') {
      // unexpected end of file is ignored by browsers and curl
      stream.emit('end');
      return;
    }

    stream.emit('error', error);
  });

  // pipe to unzip
  res.pipe(decompresser);

  // override `setEncoding` to capture encoding
  res.setEncoding = (type) => {
    decoder = new StringDecoder(type);
  };

  // decode upon decompressing with captured encoding
  decompresser.on('data', (buf) => {
    if (decoder) {
      const string_ = decoder.write(buf);
      if (string_.length > 0) stream.emit('data', string_);
    } else {
      stream.emit('data', buf);
    }
  });

  decompresser.on('end', () => {
    stream.emit('end');
  });

  // override `on` to capture data listeners
  const _on = res.on;
  res.on = function (type, fn) {
    if (type === 'data' || type === 'end') {
      stream.on(type, fn.bind(res));
    } else if (type === 'error') {
      stream.on(type, fn.bind(res));
      _on.call(res, type, fn);
    } else {
      _on.call(res, type, fn);
    }

    return this;
  };
};
```

## File: `src/node/parsers/image.js`
```javascript
module.exports = (res, fn) => {
  const data = []; // Binary data needs binary storage

  res.on('data', (chunk) => {
    data.push(chunk);
  });
  res.on('end', () => {
    fn(null, Buffer.concat(data));
  });
};
```

## File: `src/node/parsers/index.js`
```javascript
exports['application/x-www-form-urlencoded'] = require('./urlencoded');
exports['application/json'] = require('./json');
exports.text = require('./text');

exports['application/json-seq'] = exports.text;

const binary = require('./image');

exports['application/octet-stream'] = binary;
exports['application/pdf'] = binary;
exports.image = binary;
```

## File: `src/node/parsers/json.js`
```javascript
module.exports = function (res, fn) {
  res.text = '';
  res.setEncoding('utf8');
  res.on('data', (chunk) => {
    res.text += chunk;
  });
  res.on('end', () => {
    let body;
    let error;
    try {
      body = res.text && JSON.parse(res.text);
    } catch (err) {
      error = err;
      // issue #675: return the raw response if the response parsing fails
      error.rawResponse = res.text || null;
      // issue #876: return the http status code if the response parsing fails
      error.statusCode = res.statusCode;
    } finally {
      fn(error, body);
    }
  });
};
```

## File: `src/node/parsers/text.js`
```javascript
module.exports = (res, fn) => {
  res.text = '';
  res.setEncoding('utf8');
  res.on('data', (chunk) => {
    res.text += chunk;
  });
  res.on('end', fn);
};
```

## File: `src/node/parsers/urlencoded.js`
```javascript
/**
 * Module dependencies.
 */

const qs = require('qs');

module.exports = (res, fn) => {
  res.text = '';
  res.setEncoding('ascii');
  res.on('data', (chunk) => {
    res.text += chunk;
  });
  res.on('end', () => {
    try {
      fn(null, qs.parse(res.text));
    } catch (err) {
      fn(err);
    }
  });
};
```

## File: `test/agent-base.js`
```javascript
const assert = require('assert');
const getSetup = require('./support/setup');

const request = require('./support/client');

describe('Agent', () => {
  let setup;
  let base;

  before(async () => {
    setup = await getSetup();
    base = setup.uri;
  });

  it('should remember defaults', () => {
    if (typeof Promise === 'undefined') {
      return;
    }

    let called = 0;
    let event_called = 0;
    const agent = request
      .agent()
      .accept('json')
      .use(() => {
        called++;
      })
      .once('request', () => {
        event_called++;
      })
      .query({ hello: 'world' })
      .set('X-test', 'testing');
    assert.equal(0, called);
    assert.equal(0, event_called);

    return agent
      .get(`${base}/echo`)
      .then((res) => {
        assert.equal(1, called);
        assert.equal(1, event_called);
        assert.equal('application/json', res.headers.accept);
        assert.equal('testing', res.headers['x-test']);

        return agent.get(`${base}/querystring`);
      })
      .then((res) => {
        assert.equal(2, called);
        assert.equal(2, event_called);
        assert.deepEqual({ hello: 'world' }, res.body);
      });
  });
});
```

## File: `test/basic.js`
```javascript
const assert = require('assert');
const getSetup = require('./support/setup');

const request = require('./support/client');

describe('request', function () {
  let setup;
  let NODE;
  let uri;

  before(async () => {
    setup = await getSetup();
    NODE = setup.NODE;
    uri = setup.uri;
  });

  this.timeout(20_000);

  describe('res.statusCode', () => {
    it('should set statusCode', (done) => {
      request.get(`${uri}/login`, (error, res) => {
        try {
          assert.strictEqual(res.statusCode, 200);
          done();
        } catch (err) {
          done(err);
        }
      });
    });
  });

  describe('should allow the send shorthand', () => {
    it('with callback in the method call', (done) => {
      request.get(`${uri}/login`, (error, res) => {
        assert.equal(res.status, 200);
        done();
      });
    });

    it('with data in the method call', (done) => {
      request.post(`${uri}/echo`, { foo: 'bar' }).end((error, res) => {
        assert.equal('{"foo":"bar"}', res.text);
        done();
      });
    });

    it('with callback and data in the method call', (done) => {
      request.post(`${uri}/echo`, { foo: 'bar' }, (error, res) => {
        assert.equal('{"foo":"bar"}', res.text);
        done();
      });
    });
  });

  describe('with a callback', () => {
    it('should invoke .end()', (done) => {
      request.get(`${uri}/login`, (error, res) => {
        try {
          assert.equal(res.status, 200);
          done();
        } catch (err) {
          done(err);
        }
      });
    });
  });

  describe('.end()', () => {
    it('should issue a request', (done) => {
      request.get(`${uri}/login`).end((error, res) => {
        try {
          assert.equal(res.status, 200);
          done();
        } catch (err) {
          done(err);
        }
      });
    });

    it('is optional with a promise', () => {
      if (typeof Promise === 'undefined') {
        return;
      }

      return request
        .get(`${uri}/login`)
        .then((res) => res.status)
        .then()
        .then((status) => {
          assert.equal(200, status, 'Real promises pass results through');
        });
    });

    it('called only once with a promise', () => {
      if (typeof Promise === 'undefined') {
        return;
      }

      const request_ = request.get(`${uri}/unique`);

      return Promise.all([request_, request_, request_]).then((results) => {
        for (const item of results) {
          assert.deepEqual(
            item.body,
            results[0].body,
            'It should keep returning the same result after being called once'
          );
        }
      });
    });
  });

  describe('res.error', () => {
    it('ok', (done) => {
      let calledErrorEvent = false;
      let calledOKHandler = false;
      request
        .get(`${uri}/error`)
        .ok((res) => {
          assert.strictEqual(500, res.status);
          calledOKHandler = true;
          return true;
        })
        .on('error', (error) => {
          calledErrorEvent = true;
        })
        .end((error, res) => {
          try {
            assert.ifError(error);
            assert.strictEqual(res.status, 500);
            assert(!calledErrorEvent);
            assert(calledOKHandler);
            done();
          } catch (err) {
            done(err);
          }
        });
    });

    it('should be an Error object', (done) => {
      let calledErrorEvent = false;
      request
        .get(`${uri}/error`)
        .on('error', (error) => {
          assert.strictEqual(error.status, 500);
          calledErrorEvent = true;
        })
        .end((error, res) => {
          try {
            if (NODE) {
              res.error.message.should.equal('cannot GET /error (500)');
            } else {
              res.error.message.should.equal(`cannot GET ${uri}/error (500)`);
            }

            assert.strictEqual(res.error.status, 500);
            assert(error, 'should have an error for 500');
            assert.equal(error.message, 'Internal Server Error');
            assert(calledErrorEvent);
            done();
          } catch (err) {
            done(err);
          }
        });
    });

    it('with .then() promise', () => {
      if (typeof Promise === 'undefined') {
        return;
      }

      return request.get(`${uri}/error`).then(
        () => {
          assert.fail();
        },
        (err) => {
          assert.equal(err.message, 'Internal Server Error');
        }
      );
    });

    it('with .ok() returning false', () => {
      if (typeof Promise === 'undefined') {
        return;
      }

      return request
        .get(`${uri}/echo`)
        .ok(() => false)
        .then(
          () => {
            assert.fail();
          },
          (err) => {
            assert.equal(200, err.response.status);
            assert.equal(err.message, 'OK');
          }
        );
    });

    it('with .ok() throwing an Error', () => {
      if (typeof Promise === 'undefined') {
        return;
      }

      return request
        .get(`${uri}/echo`)
        .ok(() => {
          throw new Error('boom');
        })
        .then(
          () => {
            assert.fail();
          },
          (err) => {
            assert.equal(200, err.status);
            assert.equal(200, err.response.status);
            assert.equal(err.message, 'boom');
          }
        );
    });

    it('with .ok() throwing an Error with status', () => {
      if (typeof Promise === 'undefined') {
        return;
      }

      return request
        .get(`${uri}/echo`)
        .ok(() => {
          const err = new Error('boom');
          err.status = 404;
          throw err;
        })
        .then(
          () => {
            assert.fail();
          },
          (err) => {
            assert.equal(404, err.status);
            assert.equal(200, err.response.status);
            assert.equal(err.message, 'boom');
          }
        );
    });
  });

  describe('res.header', () => {
    it('should be an object', (done) => {
      request.get(`${uri}/login`).end((error, res) => {
        try {
          assert.equal('Express', res.header['x-powered-by']);
          done();
        } catch (err) {
          done(err);
        }
      });
    });
  });

  describe('set headers', () => {
    before(() => {
      Object.prototype.invalid = 'invalid';
    });

    after(() => {
      delete Object.prototype.invalid;
    });

    it('should only set headers for ownProperties of header', (done) => {
      try {
        request
          .get(`${uri}/echo-headers`)
          .set('valid', 'ok')
          .end((error, res) => {
            if (
              !error &&
              res.body &&
              res.body.valid &&
              !res.body.hasOwnProperty('invalid')
            ) {
              return done();
            }

            done(error || new Error('fail'));
          });
      } catch (err) {
        done(err);
      }
    });
  });

  describe('res.charset', () => {
    it('should be set when present', (done) => {
      request.get(`${uri}/login`).end((error, res) => {
        try {
          res.charset.should.equal('utf-8');
          done();
        } catch (err) {
          done(err);
        }
      });
    });
  });

  describe('res.statusType', () => {
    it('should provide the first digit', (done) => {
      request.get(`${uri}/login`).end((error, res) => {
        try {
          assert(!error, 'should not have an error for success responses');
          assert.equal(200, res.status);
          assert.equal(2, res.statusType);
          done();
        } catch (err) {
          done(err);
        }
      });
    });
  });

  describe('res.type', () => {
    it('should provide the mime-type void of params', (done) => {
      request.get(`${uri}/login`).end((error, res) => {
        try {
          res.type.should.equal('text/html');
          res.charset.should.equal('utf-8');
          done();
        } catch (err) {
          done(err);
        }
      });
    });
  });

  describe('req.set(field, val)', () => {
    it('should set the header field', (done) => {
      request
        .post(`${uri}/echo`)
        .set('X-Foo', 'bar')
        .set('X-Bar', 'baz')
        .end((error, res) => {
          try {
            assert.equal('bar', res.header['x-foo']);
            assert.equal('baz', res.header['x-bar']);
            done();
          } catch (err) {
            done(err);
          }
        });
    });
  });

  describe('req.set(obj)', () => {
    it('should set the header fields', (done) => {
      request
        .post(`${uri}/echo`)
        .set({ 'X-Foo': 'bar', 'X-Bar': 'baz' })
        .end((error, res) => {
          try {
            assert.equal('bar', res.header['x-foo']);
            assert.equal('baz', res.header['x-bar']);
            done();
          } catch (err) {
            done(err);
          }
        });
    });
  });

  describe('req.type(str)', () => {
    it('should set the Content-Type', (done) => {
      request
        .post(`${uri}/echo`)
        .type('text/x-foo')
        .end((error, res) => {
          try {
            res.header['content-type'].should.equal('text/x-foo');
            done();
          } catch (err) {
            done(err);
          }
        });
    });

    it('should map "json"', (done) => {
      request
        .post(`${uri}/echo`)
        .type('json')
        .send('{"a": 1}')
        .end((error, res) => {
          try {
            res.should.be.json();
            done();
          } catch (err) {
            done(err);
          }
        });
    });

    it('should map "html"', (done) => {
      request
        .post(`${uri}/echo`)
        .type('html')
        .end((error, res) => {
          try {
            res.header['content-type'].should.equal('text/html');
            done();
          } catch (err) {
            done(err);
          }
        });
    });
  });

  describe('req.accept(str)', () => {
    it('should set Accept', (done) => {
      request
        .get(`${uri}/echo`)
        .accept('text/x-foo')
        .end((error, res) => {
          try {
            res.header.accept.should.equal('text/x-foo');
            done();
          } catch (err) {
            done(err);
          }
        });
    });

    it('should map "json"', (done) => {
      request
        .get(`${uri}/echo`)
        .accept('json')
        .end((error, res) => {
          try {
            res.header.accept.should.equal('application/json');
            done();
          } catch (err) {
            done(err);
          }
        });
    });

    it('should map "xml"', (done) => {
      request
        .get(`${uri}/echo`)
        .accept('xml')
        .end((error, res) => {
          try {
            // Mime module keeps changing this :(
            assert(
              res.header.accept == 'application/xml' ||
                res.header.accept == 'text/xml'
            );
            done();
          } catch (err) {
            done(err);
          }
        });
    });

    it('should map "html"', (done) => {
      request
        .get(`${uri}/echo`)
        .accept('html')
        .end((error, res) => {
          try {
            res.header.accept.should.equal('text/html');
            done();
          } catch (err) {
            done(err);
          }
        });
    });
  });

  describe('req.send(str)', () => {
    it('should write the string', (done) => {
      request
        .post(`${uri}/echo`)
        .type('json')
        .send('{"name":"tobi"}')
        .end((error, res) => {
          try {
            res.text.should.equal('{"name":"tobi"}');
            done();
          } catch (err) {
            done(err);
          }
        });
    });
  });

  describe('req.send(Object)', () => {
    it('should default to json', (done) => {
      request
        .post(`${uri}/echo`)
        .send({ name: 'tobi' })
        .end((error, res) => {
          try {
            res.should.be.json();
            res.text.should.equal('{"name":"tobi"}');
            done();
          } catch (err) {
            done(err);
          }
        });
    });

    describe('when called several times', () => {
      it('should merge the objects', (done) => {
        request
          .post(`${uri}/echo`)
          .send({ name: 'tobi' })
          .send({ age: 1 })
          .end((error, res) => {
            try {
              res.should.be.json();
              if (NODE) {
                res.buffered.should.be.true();
              }

              res.text.should.equal('{"name":"tobi","age":1}');
              done();
            } catch (err) {
              done(err);
            }
          });
      });
    });
  });

  describe('.end(fn)', () => {
    it('should check arity', (done) => {
      request
        .post(`${uri}/echo`)
        .send({ name: 'tobi' })
        .end((error, res) => {
          try {
            assert.ifError(error);
            res.text.should.equal('{"name":"tobi"}');
            done();
          } catch (err) {
            done(err);
          }
        });
    });

    it('should emit request', (done) => {
      const request_ = request.post(`${uri}/echo`);
      request_.on('request', (request) => {
        assert.equal(request_, request);
        done();
      });
      request_.end();
    });

    it('should emit response', (done) => {
      request
        .post(`${uri}/echo`)
        .send({ name: 'tobi' })
        .on('response', (res) => {
          res.text.should.equal('{"name":"tobi"}');
          done();
        })
        .end();
    });
  });

  describe('.then(fulfill, reject)', () => {
    it('should support successful fulfills with .then(fulfill)', (done) => {
      if (typeof Promise === 'undefined') {
        return done();
      }

      request
        .post(`${uri}/echo`)
        .send({ name: 'tobi' })
        .then((res) => {
          res.type.should.equal('application/json');
          res.text.should.equal('{"name":"tobi"}');
          done();
        });
    });

    it('should reject an error with .then(null, reject)', (done) => {
      if (typeof Promise === 'undefined') {
        return done();
      }

      request.get(`${uri}/error`).then(null, (err) => {
        assert.equal(err.status, 500);
        assert.equal(err.response.text, 'boom');
        done();
      });
    });
  });

  describe('.catch(reject)', () => {
    it('should reject an error with .catch(reject)', (done) => {
      if (typeof Promise === 'undefined') {
        return done();
      }

      request.get(`${uri}/error`).catch((err) => {
        assert.equal(err.status, 500);
        assert.equal(err.response.text, 'boom');
        done();
      });
    });
  });

  describe('.abort()', () => {
    it('should abort the request', (done) => {
      const request_ = request.get(`${uri}/delay/3000`);
      request_.end((error, res) => {
        try {
          assert(false, 'should not complete the request');
        } catch (err) {
          done(err);
        }
      });

      request_.on('error', (error) => {
        done(error);
      });
      request_.on('abort', done);

      setTimeout(() => {
        request_.abort();
      }, 500);
    });
    it('should abort the promise', () => {
      const request_ = request.get(`${uri}/delay/3000`);
      setTimeout(() => {
        request_.abort();
      }, 10);
      return request_.then(
        () => {
          assert.fail('should not complete the request');
        },
        (err) => {
          assert.equal('ABORTED', err.code);
        }
      );
    });

    it('should allow chaining .abort() several times', (done) => {
      const request_ = request.get(`${uri}/delay/3000`);
      request_.end((error, res) => {
        try {
          assert(false, 'should not complete the request');
        } catch (err) {
          done(err);
        }
      });

      // This also verifies only a single 'done' event is emitted
      request_.on('abort', done);

      setTimeout(() => {
        request_.abort().abort().abort();
      }, 1000);
    });

    it('should not allow abort then end', (done) => {
      request
        .get(`${uri}/delay/3000`)
        .abort()
        .end((error, res) => {
          done(error ? undefined : new Error('Expected abort error'));
        });
    });
  });

  describe('req.toJSON()', () => {
    it('should describe the request', (done) => {
      const request_ = request.post(`${uri}/echo`).send({ foo: 'baz' });
      request_.end((error, res) => {
        try {
          const json = request_.toJSON();
          assert.equal('POST', json.method);
          assert(/\/echo$/.test(json.url));
          assert.equal('baz', json.data.foo);
          done();
        } catch (err) {
          done(err);
        }
      });
    });
  });

  describe('req.options()', () => {
    it('should allow request body', (done) => {
      request
        .options(`${uri}/options/echo/body`)
        .send({ foo: 'baz' })
        .end((error, res) => {
          try {
            assert.equal(error, null);
            assert.strictEqual(res.body.foo, 'baz');
            done();
          } catch (err) {
            done(err);
          }
        });
    });
  });

  describe('req.sortQuery()', () => {
    it('nop with no querystring', (done) => {
      request
        .get(`${uri}/url`)
        .sortQuery()
        .end((error, res) => {
          try {
            assert.equal(res.text, '/url');
            done();
          } catch (err) {
            done(err);
          }
        });
    });

    it('should sort the request querystring', (done) => {
      request
        .get(`${uri}/url`)
        .query('search=Manny')
        .query('order=desc')
        .sortQuery()
        .end((error, res) => {
          try {
            assert.equal(res.text, '/url?order=desc&search=Manny');
            done();
          } catch (err) {
            done(err);
          }
        });
    });

    it('should allow disabling sorting', (done) => {
      request
        .get(`${uri}/url`)
        .query('search=Manny')
        .query('order=desc')
        .sortQuery() // take default of true
        .sortQuery(false) // override it in later call
        .end((error, res) => {
          try {
            assert.equal(res.text, '/url?search=Manny&order=desc');
            done();
          } catch (err) {
            done(err);
          }
        });
    });

    it('should sort the request querystring using customized function', (done) => {
      request
        .get(`${uri}/url`)
        .query('name=Nick')
        .query('search=Manny')
        .query('order=desc')
        .sortQuery((a, b) => a.length - b.length)
        .end((error, res) => {
          try {
            assert.equal(res.text, '/url?name=Nick&order=desc&search=Manny');
            done();
          } catch (err) {
            done(err);
          }
        });
    });
  });
});
```

## File: `test/content-type.js`
```javascript
const assert = require('assert');
const getSetup = require('./support/setup');

const request = require('./support/client');

describe('req.set("Content-Type", contentType)', function () {
  let setup;
  let uri;

  before(async () => {
    setup = await getSetup();
    uri = setup.uri;
  });

  this.timeout(20_000);

  it('should work with just the contentType component', (done) => {
    request
      .post(`${uri}/echo`)
      .set('Content-Type', 'application/json')
      .send({ name: 'tobi' })
      .end((error) => {
        assert(!error);
        done();
      });
  });

  it('should work with the charset component', (done) => {
    request
      .post(`${uri}/echo`)
      .set('Content-Type', 'application/json; charset=utf-8')
      .send({ name: 'tobi' })
      .end((error) => {
        assert(!error);
        done();
      });
  });
});
```

## File: `test/form.js`
```javascript
const assert = require('assert');
const should = require('should');

const getSetup = require('./support/setup');
const request = require('./support/client');

if (!assert.deepStrictEqual) assert.deepStrictEqual = assert.deepEqual;

describe('req.send(Object) as "form"', () => {
  let setup;
  let base;

  before(async () => {
    setup = await getSetup();
    base = setup.uri;
  });

  describe('with req.type() set to form', () => {
    it('should send x-www-form-urlencoded data', (done) => {
      request
        .post(`${base}/echo`)
        .type('form')
        .send({ name: 'tobi' })
        .end((error, res) => {
          res.header['content-type'].should.equal(
            'application/x-www-form-urlencoded'
          );
          res.text.should.equal('name=tobi');
          done();
        });
    });
  });

  describe('when called several times', () => {
    it('should merge the objects', (done) => {
      request
        .post(`${base}/echo`)
        .type('form')
        .send({ name: { first: 'tobi', last: 'holowaychuk' } })
        .send({ age: '1' })
        .end((error, res) => {
          res.header['content-type'].should.equal(
            'application/x-www-form-urlencoded'
          );
          res.text.should.equal(
            'name%5Bfirst%5D=tobi&name%5Blast%5D=holowaychuk&age=1'
          );
          done();
        });
    });
  });
});

describe('req.attach', () => {
  it('ignores null file', (done) => {
    request
      .post('/echo')
      .attach('image', null)
      .end((error, res) => {
        done();
      });
  });
});

describe('req.field', function () {
  let setup;
  let base;
  let formDataSupported;

  before(async () => {
    setup = await getSetup();
    base = setup.uri;

    formDataSupported = setup.NODE || FormData !== 'undefined';
  });

  this.timeout(5000);
  it('allow bools', (done) => {
    if (!formDataSupported) {
      return done();
    }

    request
      .post(`${base}/formecho`)
      .field('bools', true)
      .field('strings', 'true')
      .end((error, res) => {
        assert.ifError(error);
        assert.deepStrictEqual(res.body, { bools: 'true', strings: 'true' });
        done();
      });
  });

  it('allow objects', (done) => {
    if (!formDataSupported) {
      return done();
    }

    request
      .post(`${base}/formecho`)
      .field({ bools: true, strings: 'true' })
      .end((error, res) => {
        assert.ifError(error);
        assert.deepStrictEqual(res.body, { bools: 'true', strings: 'true' });
        done();
      });
  });

  it('works with arrays in objects', (done) => {
    if (!formDataSupported) {
      return done();
    }

    request
      .post(`${base}/formecho`)
      .field({ numbers: [1, 2, 3] })
      .end((error, res) => {
        assert.ifError(error);
        assert.deepStrictEqual(res.body, { numbers: ['1', '2', '3'] });
        done();
      });
  });

  it('works with arrays', (done) => {
    if (!formDataSupported) {
      return done();
    }

    request
      .post(`${base}/formecho`)
      .field('letters', ['a', 'b', 'c'])
      .end((error, res) => {
        assert.ifError(error);
        assert.deepStrictEqual(res.body, { letters: ['a', 'b', 'c'] });
        done();
      });
  });

  it('throw when empty', () => {
    should.throws(() => {
      request.post(`${base}/echo`).field();
    }, /name/);

    should.throws(() => {
      request.post(`${base}/echo`).field('name');
    }, /val/);
  });

  it('cannot be mixed with send()', () => {
    assert.throws(() => {
      request.post('/echo').field('form', 'data').send('hi');
    });

    assert.throws(() => {
      request.post('/echo').send('hi').field('form', 'data');
    });
  });
});
```

## File: `test/json.js`
```javascript
const getSetup = require('./support/setup');

const doesntWorkInHttp2 = !process.env.HTTP2_TEST;

const assert = require('assert');
const request = require('./support/client');

describe('req.send(Object) as "json"', function () {
  let setup;
  let uri;
  let doesntWorkInBrowserYet;

  before(async () => {
    setup = await getSetup();
    uri = setup.uri;
    doesntWorkInBrowserYet = setup.NODE;
  });

  this.timeout(20_000);

  it('should default to json', (done) => {
    request
      .post(`${uri}/echo`)
      .send({ name: 'tobi' })
      .end((error, res) => {
        res.should.be.json();
        res.text.should.equal('{"name":"tobi"}');
        done();
      });
  });

  it('should work with arrays', (done) => {
    request
      .post(`${uri}/echo`)
      .send([1, 2, 3])
      .end((error, res) => {
        res.should.be.json();
        res.text.should.equal('[1,2,3]');
        done();
      });
  });

  it('should work with value null', (done) => {
    request
      .post(`${uri}/echo`)
      .type('json')
      .send('null')
      .end((error, res) => {
        res.should.be.json();
        assert.strictEqual(res.body, null);
        done();
      });
  });

  it('should work with value false', (done) => {
    request
      .post(`${uri}/echo`)
      .type('json')
      .send('false')
      .end((error, res) => {
        res.should.be.json();
        res.body.should.equal(false);
        done();
      });
  });

  if (doesntWorkInBrowserYet)
    it('should work with value 0', (done) => {
      // fails in IE9
      request
        .post(`${uri}/echo`)
        .type('json')
        .send('0')
        .end((error, res) => {
          res.should.be.json();
          res.body.should.equal(0);
          done();
        });
    });

  it('should work with empty string value', (done) => {
    request
      .post(`${uri}/echo`)
      .type('json')
      .send('""')
      .end((error, res) => {
        res.should.be.json();
        res.body.should.equal('');
        done();
      });
  });

  if (doesntWorkInBrowserYet && doesntWorkInHttp2)
    it('should work with GET', (done) => {
      request
        .get(`${uri}/echo`)
        .send({ tobi: 'ferret' })
        .end((error, res) => {
          try {
            res.should.be.json();
            res.text.should.equal('{"tobi":"ferret"}');
            ({ tobi: 'ferret' }.should.eql(res.body));
            done();
          } catch (err) {
            done(err);
          }
        });
    });

  it('should work with vendor MIME type', (done) => {
    request
      .post(`${uri}/echo`)
      .set('Content-Type', 'application/vnd.example+json')
      .send({ name: 'vendor' })
      .end((error, res) => {
        res.text.should.equal('{"name":"vendor"}');
        ({ name: 'vendor' }.should.eql(res.body));
        done();
      });
  });

  it('should error for BigInt object', (done) => {
    try {
      request
        .post(`${uri}/echo`)
        .type('json')
        .send({number: 1n})
        throw new Error('Should have thrown error for object with BigInt')
    } catch (error) {
      assert.strictEqual(error.message, 'Cannot serialize BigInt value to json');
    }
    done();
  });

  describe('when BigInts have a .toJSON property', function () {
    before(function () {
      // eslint-disable-next-line node/no-unsupported-features/es-builtins
      BigInt.prototype.toJSON = function () {
        return this.toString();
      };
    });

    it('should accept BigInt properties', (done) => {
      request
        .post(`${uri}/echo`)
        .send({ number: 1n })
        .end((error, res) => {
          res.should.be.json();
          res.text.should.equal('{"number":"1"}');
          done();
        });
    });

    after(function () {
      // eslint-disable-next-line node/no-unsupported-features/es-builtins
      delete BigInt.prototype.toJSON;
    });
  });


  it('should error for BigInt primitive', (done) => {
    try {
      request
        .post(`${uri}/echo`)
        .type('json')
        .send(1n)
        throw new Error('Should have thrown error for BigInt primitive')
    } catch (error) {
      assert.strictEqual(error.message, 'Cannot send value of type BigInt');
    }
    done();
  });

  describe('when called several times', () => {
    it('should merge the objects', (done) => {
      request
        .post(`${uri}/echo`)
        .send({ name: 'tobi' })
        .send({ age: 1 })
        .end((error, res) => {
          res.should.be.json();
          res.text.should.equal('{"name":"tobi","age":1}');
          ({ name: 'tobi', age: 1 }.should.eql(res.body));
          done();
        });
    });
  });
});

describe('res.body', function () {
  let setup;
  let uri;
  let doesntWorkInBrowserYet;

  before(async () => {
    setup = await getSetup();
    uri = setup.uri;
    doesntWorkInBrowserYet = setup.NODE;
  });

  this.timeout(20_000);

  describe('application/json', () => {
    it('should parse the body', (done) => {
      request.get(`${uri}/json`).end((error, res) => {
        res.text.should.equal('{"name":"manny"}');
        res.body.should.eql({ name: 'manny' });
        done();
      });
    });
  });

  if (doesntWorkInBrowserYet)
    describe('HEAD requests', () => {
      it('should not throw a parse error', (done) => {
        request.head(`${uri}/json`).end((error, res) => {
          try {
            assert.strictEqual(error, null);
            assert.strictEqual(res.text, undefined);
            assert.strictEqual(Object.keys(res.body).length, 0);
            done();
          } catch (err) {
            done(err);
          }
        });
      });
    });

  describe('Invalid JSON response', () => {
    it('should return the raw response', (done) => {
      request.get(`${uri}/invalid-json`).end((error, res) => {
        assert.deepEqual(
          error.rawResponse,
          ")]}', {'header':{'code':200,'text':'OK','version':'1.0'},'data':'some data'}"
        );
        done();
      });
    });

    it('should return the http status code', (done) => {
      request.get(`${uri}/invalid-json-forbidden`).end((error, res) => {
        assert.equal(error.statusCode, 403);
        done();
      });
    });
  });

  if (doesntWorkInBrowserYet)
    describe('No content', () => {
      it('should not throw a parse error', (done) => {
        request.get(`${uri}/no-content`).end((error, res) => {
          try {
            assert.strictEqual(error, null);
            assert.strictEqual(res.text, '');
            assert.strictEqual(Object.keys(res.body).length, 0);
            done();
          } catch (err) {
            done(err);
          }
        });
      });
    });

  if (doesntWorkInBrowserYet)
    describe('application/json+hal', () => {
      it('should parse the body', (done) => {
        request.get(`${uri}/json-hal`).end((error, res) => {
          if (error) return done(error);
          res.text.should.equal('{"name":"hal 5000"}');
          res.body.should.eql({ name: 'hal 5000' });
          done();
        });
      });
    });

  if (doesntWorkInBrowserYet)
    describe('vnd.collection+json', () => {
      it('should parse the body', (done) => {
        request.get(`${uri}/collection-json`).end((error, res) => {
          res.text.should.equal('{"name":"chewbacca"}');
          res.body.should.eql({ name: 'chewbacca' });
          done();
        });
      });
    });
});
```

## File: `test/redirects.js`
```javascript
const assert = require('assert');

const getSetup = require('./support/setup');
const request = require('./support/client');

describe('request', function () {
  let setup;
  let base;
  let isMSIE;

  before(async () => {
    setup = await getSetup();
    base = setup.uri;
    isMSIE = !setup.NODE && /Trident\//.test(navigator.userAgent);
  });

  this.timeout(20_000);
  describe('on redirect', () => {
    it('should retain header fields', (done) => {
      request
        .get(`${base}/header`)
        .set('X-Foo', 'bar')
        .end((error, res) => {
          try {
            assert(res.body);
            res.body.should.have.property('x-foo', 'bar');
            done();
          } catch (err) {
            done(err);
          }
        });
    });

    it('should preserve timeout across redirects', (done) => {
      request
        .get(`${base}/movies/random`)
        .timeout(250)
        .end((error, res) => {
          try {
            assert(error instanceof Error, 'expected an error');
            error.should.have.property('timeout', 250);
            done();
          } catch (err) {
            done(err);
          }
        });
    });

    it('should successfully redirect after retry on error', (done) => {
      const id = Math.random() * 1_000_000 * Date.now();
      request
        .get(`${base}/error/redirect/${id}`)
        .retry(2)
        .end((error, res) => {
          assert(res.ok, 'response should be ok');
          assert(res.text, 'first movie page');
          done();
        });
    });

    it('should preserve retries across redirects', (done) => {
      const id = Math.random() * 1_000_000 * Date.now();
      request
        .get(`${base}/error/redirect-error${id}`)
        .retry(2)
        .end((error, res) => {
          assert(error, 'expected an error');
          assert.equal(2, error.retries, 'expected an error with .retries');
          assert.equal(500, error.status, 'expected an error status of 500');
          done();
        });
    });
  });

  describe('on 303', () => {
    it('should redirect with same method', (done) => {
      request
        .put(`${base}/redirect-303`)
        .send({ msg: 'hello' })
        .redirects(1)
        .on('redirect', (res) => {
          res.headers.location.should.equal('/reply-method');
        })
        .end((error, res) => {
          if (error) {
            done(error);
            return;
          }

          res.text.should.equal('method=get');
          done();
        });
    });
  });

  describe('on 307', () => {
    it('should redirect with same method', (done) => {
      if (isMSIE) return done(); // IE9 broken

      request
        .put(`${base}/redirect-307`)
        .send({ msg: 'hello' })
        .redirects(1)
        .on('redirect', (res) => {
          res.headers.location.should.equal('/reply-method');
        })
        .end((error, res) => {
          if (error) {
            done(error);
            return;
          }

          res.text.should.equal('method=put');
          done();
        });
    });
  });

  describe('on 308', () => {
    it('should redirect with same method', (done) => {
      if (isMSIE) return done(); // IE9 broken

      request
        .put(`${base}/redirect-308`)
        .send({ msg: 'hello' })
        .redirects(1)
        .on('redirect', (res) => {
          res.headers.location.should.equal('/reply-method');
        })
        .end((error, res) => {
          if (error) {
            done(error);
            return;
          }

          res.text.should.equal('method=put');
          done();
        });
    });
  });
});
```

## File: `test/request.js`
```javascript
const fs = require('fs');

const assert = require('assert');
const getSetup = require('./support/setup');

const request = require('./support/client');

const binData = fs.readFileSync(`${__dirname}/node/fixtures/test.aac`);

describe('request', function () {
  let setup;
  let uri;

  before(async () => {
    setup = await getSetup();
    uri = setup.uri;
  });

  this.timeout(20_000);

  it('Request inheritance', () => {
    assert(request.get(`${uri}/`) instanceof request.Request);
  });

  it('request() simple GET without callback', (next) => {
    request('GET', 'test/test.request.js').end();
    next();
  });

  it('request() simple GET', (next) => {
    request('GET', `${uri}/ok`).end((error, res) => {
      try {
        assert(res instanceof request.Response, 'respond with Response');
        assert(res.ok, 'response should be ok');
        assert(res.text, 'res.text');
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('request() simple HEAD', (next) => {
    request.head(`${uri}/ok`).end((error, res) => {
      try {
        assert(res instanceof request.Response, 'respond with Response');
        assert(res.ok, 'response should be ok');
        assert(!res.text, 'res.text');
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('request() GET 5xx', (next) => {
    request('GET', `${uri}/error`).end((error, res) => {
      try {
        assert(error);
        assert.equal(error.message, 'Internal Server Error');
        assert(!res.ok, 'response should not be ok');
        assert(res.error, 'response should be an error');
        assert(!res.clientError, 'response should not be a client error');
        assert(res.serverError, 'response should be a server error');
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('request() GET 4xx', (next) => {
    request('GET', `${uri}/notfound`).end((error, res) => {
      try {
        assert(error);
        assert.equal(error.message, 'Not Found');
        assert(!res.ok, 'response should not be ok');
        assert(res.error, 'response should be an error');
        assert(res.clientError, 'response should be a client error');
        assert(!res.serverError, 'response should not be a server error');
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('request() GET 404 Not Found', (next) => {
    request('GET', `${uri}/notfound`).end((error, res) => {
      try {
        assert(error);
        assert(res.notFound, 'response should be .notFound');
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('request() GET 400 Bad Request', (next) => {
    request('GET', `${uri}/bad-request`).end((error, res) => {
      try {
        assert(error);
        assert(res.badRequest, 'response should be .badRequest');
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('request() GET 401 Bad Request', (next) => {
    request('GET', `${uri}/unauthorized`).end((error, res) => {
      try {
        assert(error);
        assert(res.unauthorized, 'response should be .unauthorized');
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('request() GET 406 Not Acceptable', (next) => {
    request('GET', `${uri}/not-acceptable`).end((error, res) => {
      try {
        assert(error);
        assert(res.notAcceptable, 'response should be .notAcceptable');
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('request() GET 204 No Content', (next) => {
    request('GET', `${uri}/no-content`).end((error, res) => {
      try {
        assert.ifError(error);
        assert(res.noContent, 'response should be .noContent');
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('request() DELETE 204 No Content', (next) => {
    request('DELETE', `${uri}/no-content`).end((error, res) => {
      try {
        assert.ifError(error);
        assert(res.noContent, 'response should be .noContent');
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('request() header parsing', (next) => {
    request('GET', `${uri}/notfound`).end((error, res) => {
      try {
        assert(error);
        assert.equal('text/html; charset=utf-8', res.header['content-type']);
        assert.equal('Express', res.header['x-powered-by']);
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('request() .status', (next) => {
    request('GET', `${uri}/notfound`).end((error, res) => {
      try {
        assert(error);
        assert.equal(404, res.status, 'response .status');
        assert.equal(4, res.statusType, 'response .statusType');
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('get()', (next) => {
    request.get(`${uri}/notfound`).end((error, res) => {
      try {
        assert(error);
        assert.equal(404, res.status, 'response .status');
        assert.equal(4, res.statusType, 'response .statusType');
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('put()', (next) => {
    request.put(`${uri}/user/12`).end((error, res) => {
      try {
        assert.equal('updated', res.text, 'response text');
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('put().send()', (next) => {
    request
      .put(`${uri}/user/13/body`)
      .send({ user: 'new' })
      .end((error, res) => {
        try {
          assert.equal('received new', res.text, 'response text');
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('post()', (next) => {
    request.post(`${uri}/user`).end((error, res) => {
      try {
        assert.equal('created', res.text, 'response text');
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('del()', (next) => {
    request.del(`${uri}/user/12`).end((error, res) => {
      try {
        assert.equal('deleted', res.text, 'response text');
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('delete()', (next) => {
    request.delete(`${uri}/user/12`).end((error, res) => {
      try {
        assert.equal('deleted', res.text, 'response text');
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('post() data', (next) => {
    request
      .post(`${uri}/todo/item`)
      .type('application/octet-stream')
      .send('tobi')
      .end((error, res) => {
        try {
          assert.equal('added "tobi"', res.text, 'response text');
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('request .type()', (next) => {
    request
      .post(`${uri}/user/12/pet`)
      .type('urlencoded')
      .send('pet=tobi')
      .end((error, res) => {
        try {
          assert.equal('added pet "tobi"', res.text, 'response text');
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('request .type() with alias', (next) => {
    request
      .post(`${uri}/user/12/pet`)
      .type('application/x-www-form-urlencoded')
      .send('pet=tobi')
      .end((error, res) => {
        try {
          assert.equal('added pet "tobi"', res.text, 'response text');
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('request .get() with no data or callback', (next) => {
    request.get(`${uri}/echo-header/content-type`);
    next();
  });

  it('request .send() with no data only', (next) => {
    request.post(`${uri}/user/5/pet`).type('urlencoded').send('pet=tobi');
    next();
  });

  it('request .send() with callback only', (next) => {
    request
      .get(`${uri}/echo-header/accept`)
      .set('Accept', 'foo/bar')
      .end((error, res) => {
        try {
          assert.equal('foo/bar', res.text);
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('request .accept() with json', (next) => {
    request
      .get(`${uri}/echo-header/accept`)
      .accept('json')
      .end((error, res) => {
        try {
          assert.equal('application/json', res.text);
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('request .accept() with application/json', (next) => {
    request
      .get(`${uri}/echo-header/accept`)
      .accept('application/json')
      .end((error, res) => {
        try {
          assert.equal('application/json', res.text);
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('request .accept() with xml', (next) => {
    request
      .get(`${uri}/echo-header/accept`)
      .accept('xml')
      .end((error, res) => {
        try {
          // We can't depend on mime module to be consistent with this
          assert(res.text == 'application/xml' || res.text == 'text/xml');
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('request .accept() with application/xml', (next) => {
    request
      .get(`${uri}/echo-header/accept`)
      .accept('application/xml')
      .end((error, res) => {
        try {
          assert.equal('application/xml', res.text);
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  // FIXME: ie6 will POST rather than GET here due to data(),
  //        but I'm not 100% sure why.  Newer IEs are OK.
  it('request .end()', (next) => {
    request
      .put(`${uri}/echo-header/content-type`)
      .set('Content-Type', 'text/plain')
      .send('wahoo')
      .end((error, res) => {
        try {
          assert.equal('text/plain', res.text);
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('request .send()', (next) => {
    request
      .put(`${uri}/echo-header/content-type`)
      .set('Content-Type', 'text/plain')
      .send('wahoo')
      .end((error, res) => {
        try {
          assert.equal('text/plain', res.text);
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('request .set()', (next) => {
    request
      .put(`${uri}/echo-header/content-type`)
      .set('Content-Type', 'text/plain')
      .send('wahoo')
      .end((error, res) => {
        try {
          assert.equal('text/plain', res.text);
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('request .set(object)', (next) => {
    request
      .put(`${uri}/echo-header/content-type`)
      .set({ 'Content-Type': 'text/plain' })
      .send('wahoo')
      .end((error, res) => {
        try {
          assert.equal('text/plain', res.text);
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('POST urlencoded', (next) => {
    request
      .post(`${uri}/pet`)
      .type('urlencoded')
      .send({ name: 'Manny', species: 'cat' })
      .end((error, res) => {
        try {
          assert.equal('added Manny the cat', res.text);
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('POST json', (next) => {
    request
      .post(`${uri}/pet`)
      .type('json')
      .send({ name: 'Manny', species: 'cat' })
      .end((error, res) => {
        try {
          assert.equal('added Manny the cat', res.text);
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('POST json array', (next) => {
    request
      .post(`${uri}/echo`)
      .send([1, 2, 3])
      .end((error, res) => {
        try {
          assert.equal(
            'application/json',
            res.header['content-type'].split(';')[0]
          );
          assert.equal('[1,2,3]', res.text);
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('POST json default', (next) => {
    request
      .post(`${uri}/pet`)
      .send({ name: 'Manny', species: 'cat' })
      .end((error, res) => {
        try {
          assert.equal('added Manny the cat', res.text);
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('POST json contentType charset', (next) => {
    request
      .post(`${uri}/echo`)
      .set('Content-Type', 'application/json; charset=UTF-8')
      .send({ data: ['data1', 'data2'] })
      .end((error, res) => {
        try {
          assert.equal('{"data":["data1","data2"]}', res.text);
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('POST json contentType vendor', (next) => {
    request
      .post(`${uri}/echo`)
      .set('Content-Type', 'application/vnd.example+json')
      .send({ data: ['data1', 'data2'] })
      .end((error, res) => {
        try {
          assert.equal('{"data":["data1","data2"]}', res.text);
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('POST multiple .send() calls', (next) => {
    request
      .post(`${uri}/pet`)
      .send({ name: 'Manny' })
      .send({ species: 'cat' })
      .end((error, res) => {
        try {
          assert.equal('added Manny the cat', res.text);
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('POST multiple .send() strings', (next) => {
    request
      .post(`${uri}/echo`)
      .send('user[name]=tj')
      .send('user[email]=tj@vision-media.ca')
      .end((error, res) => {
        try {
          assert.equal(
            'application/x-www-form-urlencoded',
            res.header['content-type'].split(';')[0]
          );
          assert.equal(
            res.text,
            'user[name]=tj&user[email]=tj@vision-media.ca'
          );
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('POST with no data', (next) => {
    request
      .post(`${uri}/empty-body`)
      .send()
      .end((error, res) => {
        try {
          assert.ifError(error);
          assert(res.noContent, 'response should be .noContent');
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('GET .type', (next) => {
    request.get(`${uri}/pets`).end((error, res) => {
      try {
        assert.equal('application/json', res.type);
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('GET Content-Type params', (next) => {
    request.get(`${uri}/text`).end((error, res) => {
      try {
        assert.equal('utf-8', res.charset);
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('GET json', (next) => {
    request.get(`${uri}/pets`).end((error, res) => {
      try {
        assert.deepEqual(res.body, ['tobi', 'loki', 'jane']);
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('GET json-seq', (next) => {
    request
      .get(`${uri}/json-seq`)
      .buffer()
      .end((error, res) => {
        try {
          assert.ifError(error);
          assert.deepEqual(res.text, '\u001E{"id":1}\n\u001E{"id":2}\n');
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('GET binary data', (next) => {
    request
      .get(`${uri}/binary-data`)
      .buffer()
      .end((error, res) => {
        try {
          assert.ifError(error);
          assert.deepEqual(res.body, binData);
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('GET x-www-form-urlencoded', (next) => {
    request.get(`${uri}/foo`).end((error, res) => {
      try {
        assert.deepEqual(res.body, { foo: 'bar' });
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('GET shorthand', (next) => {
    request.get(`${uri}/foo`, (error, res) => {
      try {
        assert.equal('foo=bar', res.text);
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('POST shorthand', (next) => {
    request.post(`${uri}/user/0/pet`, { pet: 'tobi' }, (error, res) => {
      try {
        assert.equal('added pet "tobi"', res.text);
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('POST shorthand without callback', (next) => {
    request.post(`${uri}/user/0/pet`, { pet: 'tobi' }).end((error, res) => {
      try {
        assert.equal('added pet "tobi"', res.text);
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('GET querystring object with array', (next) => {
    request
      .get(`${uri}/querystring`)
      .query({ val: ['a', 'b', 'c'] })
      .end((error, res) => {
        try {
          assert.deepEqual(res.body, { val: ['a', 'b', 'c'] });
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('GET querystring object with array and primitives', (next) => {
    request
      .get(`${uri}/querystring`)
      .query({ array: ['a', 'b', 'c'], string: 'foo', number: 10 })
      .end((error, res) => {
        try {
          assert.deepEqual(res.body, {
            array: ['a', 'b', 'c'],
            string: 'foo',
            number: 10
          });
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('GET querystring object with two arrays', (next) => {
    request
      .get(`${uri}/querystring`)
      .query({ array1: ['a', 'b', 'c'], array2: [1, 2, 3] })
      .end((error, res) => {
        try {
          assert.deepEqual(res.body, {
            array1: ['a', 'b', 'c'],
            array2: [1, 2, 3]
          });
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('GET querystring object', (next) => {
    request
      .get(`${uri}/querystring`)
      .query({ search: 'Manny' })
      .end((error, res) => {
        try {
          assert.deepEqual(res.body, { search: 'Manny' });
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('GET querystring append original', (next) => {
    request
      .get(`${uri}/querystring?search=Manny`)
      .query({ range: '1..5' })
      .end((error, res) => {
        try {
          assert.deepEqual(res.body, { search: 'Manny', range: '1..5' });
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('GET querystring multiple objects', (next) => {
    request
      .get(`${uri}/querystring`)
      .query({ search: 'Manny' })
      .query({ range: '1..5' })
      .query({ order: 'desc' })
      .end((error, res) => {
        try {
          assert.deepEqual(res.body, {
            search: 'Manny',
            range: '1..5',
            order: 'desc'
          });
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('GET querystring with strings', (next) => {
    request
      .get(`${uri}/querystring`)
      .query('search=Manny')
      .query('range=1..5')
      .query('order=desc')
      .end((error, res) => {
        try {
          assert.deepEqual(res.body, {
            search: 'Manny',
            range: '1..5',
            order: 'desc'
          });
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('GET querystring with strings and objects', (next) => {
    request
      .get(`${uri}/querystring`)
      .query('search=Manny')
      .query({ order: 'desc', range: '1..5' })
      .end((error, res) => {
        try {
          assert.deepEqual(res.body, {
            search: 'Manny',
            range: '1..5',
            order: 'desc'
          });
          next();
        } catch (err) {
          next(err);
        }
      });
  });

  it('GET shorthand payload goes to querystring', (next) => {
    request.get(
      `${uri}/querystring`,
      { foo: 'FOO', bar: 'BAR' },
      (error, res) => {
        try {
          assert.deepEqual(res.body, { foo: 'FOO', bar: 'BAR' });
          next();
        } catch (err) {
          next(err);
        }
      }
    );
  });

  it('HEAD shorthand payload goes to querystring', (next) => {
    request.head(
      `${uri}/querystring-in-header`,
      { foo: 'FOO', bar: 'BAR' },
      (error, res) => {
        try {
          assert.deepEqual(JSON.parse(res.headers.query), {
            foo: 'FOO',
            bar: 'BAR'
          });
          next();
        } catch (err) {
          next(err);
        }
      }
    );
  });

  it('request(method, url)', (next) => {
    request('GET', `${uri}/foo`).end((error, res) => {
      try {
        assert.equal('bar', res.body.foo);
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('request(url)', (next) => {
    request(`${uri}/foo`).end((error, res) => {
      try {
        assert.equal('bar', res.body.foo);
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('request(url, fn)', (next) => {
    request(`${uri}/foo`, (error, res) => {
      try {
        assert.equal('bar', res.body.foo);
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('req.timeout(ms)', (next) => {
    const request_ = request.get(`${uri}/delay/3000`).timeout(1000);
    request_.end((error, res) => {
      try {
        assert(error, 'error missing');
        assert.equal(1000, error.timeout, 'err.timeout missing');
        assert.equal(
          'Timeout of 1000ms exceeded',
          error.message,
          'err.message incorrect'
        );
        assert.equal(null, res);
        assert(request_.timedout, true);
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('req.timeout(ms) with redirect', (next) => {
    const request_ = request.get(`${uri}/delay/const`).timeout(1000);
    request_.end((error, res) => {
      try {
        assert(error, 'error missing');
        assert.equal(1000, error.timeout, 'err.timeout missing');
        assert.equal(
          'Timeout of 1000ms exceeded',
          error.message,
          'err.message incorrect'
        );
        assert.equal(null, res);
        assert(request_.timedout, true);
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('request event', (next) => {
    request
      .get(`${uri}/foo`)
      .on('request', (request_) => {
        try {
          assert.equal(`${uri}/foo`, request_.url);
          next();
        } catch (err) {
          next(err);
        }
      })
      .end();
  });

  it('response event', (next) => {
    request
      .get(`${uri}/foo`)
      .on('response', (res) => {
        try {
          assert.equal('bar', res.body.foo);
          next();
        } catch (err) {
          next(err);
        }
      })
      .end();
  });

  it('response should set statusCode', (next) => {
    request.get(`${uri}/ok`, (error, res) => {
      try {
        assert.strictEqual(res.statusCode, 200);
        next();
      } catch (err) {
        next(err);
      }
    });
  });

  it('req.toJSON()', (next) => {
    request.get(`${uri}/ok`).end((error, res) => {
      try {
        const index = (res.request || res.req).toJSON();
        for (const property of ['url', 'method', 'data', 'headers']) {
          assert(index.hasOwnProperty(property));
        }

        next();
      } catch (err) {
        next(err);
      }
    });
  });
});
```

## File: `test/retry.js`
```javascript
const assert = require('assert');
const getSetup = require('./support/setup');

const request = require('./support/client');

function uniqid() {
  return Math.random() * 10_000_000;
}

describe('.retry(count)', function () {
  let setup;
  let base;

  before(async () => {
    setup = await getSetup();
    base = setup.uri;
  });

  this.timeout(15_000);

  it('should not retry if passed "0"', (done) => {
    request
      .get(`${base}/error`)
      .retry(0)
      .end((error, res) => {
        try {
          assert(error, 'expected an error');
          assert.equal(
            undefined,
            error.retries,
            'expected an error without .retries'
          );
          assert.equal(500, error.status, 'expected an error status of 500');
          done();
        } catch (err) {
          done(err);
        }
      });
  });

  it('should not retry if passed an invalid number', (done) => {
    request
      .get(`${base}/error`)
      .retry(-2)
      .end((error, res) => {
        try {
          assert(error, 'expected an error');
          assert.equal(
            undefined,
            error.retries,
            'expected an error without .retries'
          );
          assert.equal(500, error.status, 'expected an error status of 500');
          done();
        } catch (err) {
          done(err);
        }
      });
  });

  it('should not retry if passed undefined', (done) => {
    request
      .get(`${base}/error`)
      .retry(undefined)
      .end((error, res) => {
        try {
          assert(error, 'expected an error');
          assert.equal(
            undefined,
            error.retries,
            'expected an error without .retries'
          );
          assert.equal(500, error.status, 'expected an error status of 500');
          done();
        } catch (err) {
          done(err);
        }
      });
  });

  it('should handle server error after repeat attempt', (done) => {
    request
      .get(`${base}/error`)
      .retry(2)
      .end((error, res) => {
        try {
          assert(error, 'expected an error');
          assert.equal(2, error.retries, 'expected an error with .retries');
          assert.equal(500, error.status, 'expected an error status of 500');
          done();
        } catch (err) {
          done(err);
        }
      });
  });

  it('should retry if passed nothing', (done) => {
    request
      .get(`${base}/error`)
      .retry()
      .end((error, res) => {
        try {
          assert(error, 'expected an error');
          assert.equal(1, error.retries, 'expected an error with .retries');
          assert.equal(500, error.status, 'expected an error status of 500');
          done();
        } catch (err) {
          done(err);
        }
      });
  });

  it('should retry if passed "true"', (done) => {
    request
      .get(`${base}/error`)
      .retry(true)
      .end((error, res) => {
        try {
          assert(error, 'expected an error');
          assert.equal(1, error.retries, 'expected an error with .retries');
          assert.equal(500, error.status, 'expected an error status of 500');
          done();
        } catch (err) {
          done(err);
        }
      });
  });

  it('should handle successful request after repeat attempt from server error', (done) => {
    request
      .get(`${base}/error/ok/${uniqid()}`)
      .query({ qs: 'present' })
      .retry(2)
      .end((error, res) => {
        try {
          assert.ifError(error);
          assert(res.ok, 'response should be ok');
          assert(res.text, 'res.text');
          done();
        } catch (err) {
          done(err);
        }
      });
  });

  it('should handle server timeout error after repeat attempt', (done) => {
    request
      .get(`${base}/delay/400`)
      .timeout(200)
      .retry(2)
      .end((error, res) => {
        try {
          assert(error, 'expected an error');
          assert.equal(2, error.retries, 'expected an error with .retries');
          assert.equal(
            'number',
            typeof error.timeout,
            'expected an error with .timeout'
          );
          assert.equal('ECONNABORTED', error.code, 'expected abort error code');
          done();
        } catch (err) {
          done(err);
        }
      });
  });

  it('should handle successful request after repeat attempt from server timeout', (done) => {
    const url = `/delay/1200/ok/${uniqid()}?built=in`;
    request
      .get(base + url)
      .query('string=ified')
      .query({ json: 'ed' })
      .timeout(600)
      .retry(2)
      .end((error, res) => {
        try {
          assert.ifError(error);
          assert(res.ok, 'response should be ok');
          assert.equal(res.text, `ok = ${url}&string=ified&json=ed`);
          done();
        } catch (err) {
          done(err);
        }
      });
  });

  it('should handle successful request after repeat attempt from server timeout when using .then(fulfill, reject)', (done) => {
    const url = `/delay/1200/ok/${uniqid()}?built=in`;
    request
      .get(base + url)
      .query('string=ified')
      .query({ json: 'ed' })
      .timeout(600)
      .retry(1)
      .then((res, error) => {
        try {
          assert.ifError(error);
          assert(res.ok, 'response should be ok');
          assert.equal(res.text, `ok = ${url}&string=ified&json=ed`);
          done();
        } catch (err) {
          done(err);
        }
      });
  });

  it('should correctly abort a retry attempt', (done) => {
    let aborted = false;
    const request_ = request.get(`${base}/delay/400`).timeout(200).retry(2);
    request_.end((error, res) => {
      try {
        assert(false, 'should not complete the request');
      } catch (err) {
        done(err);
      }
    });

    request_.on('abort', () => {
      aborted = true;
    });

    setTimeout(() => {
      request_.abort();
      setTimeout(() => {
        try {
          assert(aborted, 'should be aborted');
          done();
        } catch (err) {
          done(err);
        }
      }, 150);
    }, 150);
  });

  it('should correctly retain header fields', (done) => {
    request
      .get(`${base}/error/ok/${uniqid()}`)
      .query({ qs: 'present' })
      .retry(2)
      .set('X-Foo', 'bar')
      .end((error, res) => {
        try {
          assert.ifError(error);
          assert(res.body);
          res.body.should.have.property('x-foo', 'bar');
          done();
        } catch (err) {
          done(err);
        }
      });
  });

  it('should not retry on 4xx responses', (done) => {
    request
      .get(`${base}/bad-request`)
      .retry(2)
      .end((error, res) => {
        try {
          assert(error, 'expected an error');
          assert.equal(0, error.retries, 'expected an error with 0 .retries');
          assert.equal(400, error.status, 'expected an error status of 400');
          done();
        } catch (err) {
          done(err);
        }
      });
  });

  it('should execute callback on retry if passed', (done) => {
    let callbackCallCount = 0;
    function retryCallback(request) {
      callbackCallCount++;
    }

    request
      .get(`${base}/error`)
      .retry(2, retryCallback)
      .end((error, res) => {
        try {
          assert(error, 'expected an error');
          assert.equal(2, error.retries, 'expected an error with .retries');
          assert.equal(500, error.status, 'expected an error status of 500');
          assert.equal(
            2,
            callbackCallCount,
            'expected the callback to be called on each retry'
          );
          done();
        } catch (err) {
          done(err);
        }
      });
  });
});
```

## File: `test/timeout.js`
```javascript
const assert = require('assert');
const getSetup = require('./support/setup');

const request = require('./support/client');

describe('.timeout(ms)', function () {
  let setup;
  let base;

  before(async () => {
    setup = await getSetup();
    base = setup.uri;
  });

  this.timeout(15_000);

  describe('when timeout is exceeded', () => {
    it('should error', (done) => {
      request
        .get(`${base}/delay/500`)
        .timeout(150)
        .end((error, res) => {
          assert(error, 'expected an error');
          assert.equal(
            'number',
            typeof error.timeout,
            'expected an error with .timeout'
          );
          assert.equal('ECONNABORTED', error.code, 'expected abort error code');
          done();
        });
    });

    it('should error in promise interface ', (done) => {
      request
        .get(`${base}/delay/500`)
        .timeout(150)
        .catch((err) => {
          assert(err, 'expected an error');
          assert.equal(
            'number',
            typeof err.timeout,
            'expected an error with .timeout'
          );
          assert.equal('ECONNABORTED', err.code, 'expected abort error code');
          done();
        });
    });

    it('should handle gzip timeout', (done) => {
      request
        .get(`${base}/delay/zip`)
        .timeout(150)
        .end((error, res) => {
          assert(error, 'expected an error');
          assert.equal(
            'number',
            typeof error.timeout,
            'expected an error with .timeout'
          );
          assert.equal('ECONNABORTED', error.code, 'expected abort error code');
          done();
        });
    });

    it('should handle buffer timeout', (done) => {
      request
        .get(`${base}/delay/json`)
        .buffer(true)
        .timeout(150)
        .end((error, res) => {
          assert(error, 'expected an error');
          assert.equal(
            'number',
            typeof error.timeout,
            'expected an error with .timeout'
          );
          assert.equal('ECONNABORTED', error.code, 'expected abort error code');
          done();
        });
    });

    it('should error on deadline', (done) => {
      request
        .get(`${base}/delay/500`)
        .timeout({ deadline: 150 })
        .end((error, res) => {
          assert(error, 'expected an error');
          assert.equal(
            'number',
            typeof error.timeout,
            'expected an error with .timeout'
          );
          assert.equal('ECONNABORTED', error.code, 'expected abort error code');
          done();
        });
    });

    it('should support setting individual options', (done) => {
      request
        .get(`${base}/delay/500`)
        .timeout({ deadline: 10 })
        .timeout({ response: 99_999 })
        .end((error, res) => {
          assert(error, 'expected an error');
          assert.equal('ECONNABORTED', error.code, 'expected abort error code');
          assert.equal('ETIME', error.errno);
          done();
        });
    });

    it('should error on response', (done) => {
      request
        .get(`${base}/delay/500`)
        .timeout({ response: 150 })
        .end((error, res) => {
          assert(error, 'expected an error');
          assert.equal(
            'number',
            typeof error.timeout,
            'expected an error with .timeout'
          );
          assert.equal('ECONNABORTED', error.code, 'expected abort error code');
          assert.equal('ETIMEDOUT', error.errno);
          done();
        });
    });

    it('should accept slow body with fast response', (done) => {
      request
        .get(`${base}/delay/slowbody`)
        .timeout({ response: 1000 })
        .on('progress', () => {
          // This only makes the test faster without relying on arbitrary timeouts
          request.get(`${base}/delay/slowbody/finish`).end();
        })
        .end(done);
    });
  });
});
```

## File: `test/use.js`
```javascript
const assert = require('assert');
const getSetup = require('./support/setup');

const request = require('./support/client');

describe('request', function () {
  let setup;
  let uri;

  before(async function () {
    setup = await getSetup();
    uri = setup.uri;
  });

  this.timeout(20_000);
  describe('use', () => {
    it('should use plugin success', (done) => {
      const now = `${Date.now()}`;
      function uuid(request_) {
        request_.set('X-UUID', now);
        return request_;
      }

      function prefix(request_) {
        request_.url = uri + request_.url;
        return request_;
      }

      request
        .get('/echo')
        .use(uuid)
        .use(prefix)
        .end((error, res) => {
          assert.strictEqual(res.statusCode, 200);
          assert.equal(res.get('X-UUID'), now);
          done();
        });
    });
  });
});

describe('subclass', () => {
  let OriginalRequest;
  beforeEach(() => {
    OriginalRequest = request.Request;
  });
  afterEach(() => {
    request.Request = OriginalRequest;
  });

  it('should be an instance of Request', () => {
    const request_ = request.get('/');
    assert(request_ instanceof request.Request);
  });

  it('should use patched subclass', () => {
    assert(OriginalRequest);

    let constructorCalled;
    let sendCalled;
    function NewRequest(...args) {
      constructorCalled = true;
      OriginalRequest.apply(this, args);
    }

    NewRequest.prototype = Object.create(OriginalRequest.prototype);
    NewRequest.prototype.send = function () {
      sendCalled = true;
      return this;
    };

    request.Request = NewRequest;

    const request_ = request.get('/').send();
    assert(constructorCalled);
    assert(sendCalled);
    assert(request_ instanceof NewRequest);
    assert(request_ instanceof OriginalRequest);
  });

  it('should use patched subclass in agent too', () => {
    if (!request.agent) return; // Node-only

    function NewRequest(...args) {
      OriginalRequest.apply(this, args);
    }

    NewRequest.prototype = Object.create(OriginalRequest.prototype);
    request.Request = NewRequest;

    const request_ = request.agent().del('http://test.com/');
    assert(request_ instanceof NewRequest);
    assert(request_ instanceof OriginalRequest);
  });
});
```

## File: `test/client/request.js`
```javascript
const assert = require('assert');
const request = require('../support/client');

describe('request', function () {
  this.timeout(20_000);

  it('request() error object', (next) => {
    request('GET', '/error').end((error, res) => {
      assert(error);
      assert(res.error, 'response should be an error');
      assert.equal(res.error.message, 'cannot GET /error (500)');
      assert.equal(res.error.status, 500);
      assert.equal(res.error.method, 'GET');
      assert.equal(res.error.url, '/error');
      next();
    });
  });

  // This test results in a weird Jetty error on IE9 and IE11 saying PATCH is not a supported method. Looks like something's up with SauceLabs
  const isIE11 = Boolean(/Trident.*rv[ :]*11\./.test(navigator.userAgent));
  const isIE9OrOlder = !window.atob;
  if (!isIE9OrOlder && !isIE11) {
    // Don't run on IE9 or older, or IE11
    it('patch()', (next) => {
      request.patch('/user/12').end((error, res) => {
        assert.equal('updated', res.text);
        next();
      });
    });
  }

  it('POST native FormData', (next) => {
    if (!window.FormData) {
      // Skip test if FormData is not supported by browser
      return next();
    }

    const data = new FormData();
    data.append('foo', 'bar');

    request
      .post('/echo')
      .send(data)
      .end((error, res) => {
        assert.equal('multipart/form-data', res.type);
        next();
      });
  });

  it('defaults attached files to original file names', (next) => {
    if (!window.FormData) {
      // Skip test if FormData is are not supported by browser
      return next();
    }

    try {
      var file = new File([''], 'image.jpg', { type: 'image/jpeg' });
    } catch (err) {
      // Skip if file constructor not supported.
      return next();
    }

    request
      .post('/echo')
      .attach('image', file)
      .end((error, res) => {
        const regx = new RegExp(`filename="${file.name}"`);
        assert.notEqual(res.text.match(regx), null);
        next();
      });
  });

  it('attach() cannot be mixed with send()', () => {
    if (!window.FormData || !window.File) {
      // Skip test if FormData is are not supported by browser
      return;
    }

    assert.throws(() => {
      const file = new File([''], 'image.jpg', { type: 'image/jpeg' });
      request.post('/echo').attach('image', file).send('hi');
    });

    assert.throws(() => {
      const file = new File([''], 'image.jpg', { type: 'image/jpeg' });
      request.post('/echo').send('hi').attach('image', file);
    });
  });

  it('GET invalid json', (next) => {
    request.get('/invalid-json').end((error, res) => {
      assert(error.parse);
      assert.deepEqual(
        error.rawResponse,
        ")]}', {'header':{'code':200,'text':'OK','version':'1.0'},'data':'some data'}"
      );
      next();
    });
  });

  it('GET querystring empty objects', (next) => {
    const request_ = request.get('/querystring').query({});
    request_.end((error, res) => {
      assert.deepEqual(request_._query, []);
      assert.deepEqual(res.body, {});
      next();
    });
  });

  it('GET querystring object .get(uri, obj)', (next) => {
    request.get('/querystring', { search: 'Manny' }).end((error, res) => {
      assert.deepEqual(res.body, { search: 'Manny' });
      next();
    });
  });

  it('GET querystring object .get(uri, obj, fn)', (next) => {
    request.get('/querystring', { search: 'Manny' }, (error, res) => {
      assert.deepEqual(res.body, { search: 'Manny' });
      next();
    });
  });

  it('GET querystring object with null value', (next) => {
    request.get('/url', { nil: null }).end((error, res) => {
      assert.equal(res.text, '/url?nil');
      next();
    });
  });

  it('GET blob object', (next) => {
    if (typeof Blob === 'undefined') {
      return next();
    }

    request
      .get('/blob', { foo: 'bar' })
      .responseType('blob')
      .end((error, res) => {
        assert(res.xhr.response instanceof Blob);
        assert(res.body instanceof Blob);
        next();
      });
  });

  it('Reject node-only function', () => {
    assert.throws(() => {
      request.get().write();
    });
    assert.throws(() => {
      request.get().pipe();
    });
  });

  window.btoa = window.btoa || null;
  it('basic auth', (next) => {
    window.btoa = window.btoa || require('Base64').btoa;

    request
      .post('/auth')
      .auth('foo', 'bar')
      .end((error, res) => {
        assert.equal('foo', res.body.user);
        assert.equal('bar', res.body.pass);
        next();
      });
  });

  it('auth type "basic"', (next) => {
    window.btoa = window.btoa || require('Base64').btoa;

    request
      .post('/auth')
      .auth('foo', 'bar', { type: 'basic' })
      .end((error, res) => {
        assert.equal('foo', res.body.user);
        assert.equal('bar', res.body.pass);
        next();
      });
  });

  it('auth type "auto"', (next) => {
    window.btoa = window.btoa || require('Base64').btoa;

    request
      .post('/auth')
      .auth('foo', 'bar', { type: 'auto' })
      .end((error, res) => {
        assert.equal('foo', res.body.user);
        assert.equal('bar', res.body.pass);
        next();
      });
  });

  it('progress event listener on xhr object registered when some on the request', () => {
    const request_ = request.get('/foo').on('progress', (data) => {});
    request_.end();

    if (request_.xhr.upload) {
      // Only run assertion on capable browsers
      assert.notEqual(null, request_.xhr.upload.onprogress);
    }
  });

  it('no progress event listener on xhr object when none registered on request', () => {
    const request_ = request.get('/foo');
    request_.end();

    if (request_.xhr.upload) {
      // Only run assertion on capable browsers
      assert.strictEqual(null, request_.xhr.upload.onprogress);
    }
  });

  it('Request#parse overrides body parser no matter Content-Type', (done) => {
    let runParser = false;

    function testParser(data) {
      runParser = true;
      return JSON.stringify(data);
    }

    request
      .post('/user')
      .serialize(testParser)
      .type('json')
      .send({ foo: 123 })
      .end((error) => {
        if (error) return done(error);
        assert(runParser);
        done();
      });
  });

  // Don't run on browsers without xhr2 support
  if ('FormData' in window) {
    it('xhr2 download file old hack', (next) => {
      request.parse['application/vnd.superagent'] = (object) => object;

      request
        .get('/arraybuffer')
        .on('request', function () {
          this.xhr.responseType = 'arraybuffer';
        })
        .on('response', (res) => {
          assert(res.body instanceof ArrayBuffer);
          next();
        })
        .end();
    });

    it('xhr2 download file responseType', (next) => {
      request.parse['application/vnd.superagent'] = (object) => object;

      request
        .get('/arraybuffer')
        .responseType('arraybuffer')
        .on('response', (res) => {
          assert(res.body instanceof ArrayBuffer);
          next();
        })
        .end();
    });

    it('get error status code and rawResponse on file download', (next) => {
      request
        .get('/arraybuffer-unauthorized')
        .responseType('arraybuffer')
        .end((error, res) => {
          assert.equal(error.status, 401);
          assert(res.body instanceof ArrayBuffer);
          assert(error.response.body instanceof ArrayBuffer);
          const decodedString = String.fromCharCode.apply(
            null,
            new Uint8Array(res.body)
          );
          assert(
            decodedString,
            '{"message":"Authorization has been denied for this request."}'
          );
          next();
        });
    });
  }

  it('parse should take precedence over default parse', (done) => {
    request
      .get('/foo')
      .parse((res, text) => `customText: ${res.status}`)
      .end((error, res) => {
        assert(res.ok);
        assert(res.body === 'customText: 200');
        done();
      });
  });

  it('handles `xhr.open()` errors', (done) => {
    request
      .get('http://foo\0.com') // throws "Failed to execute 'open' on 'XMLHttpRequest': Invalid URL"
      .end((error, res) => {
        assert(error);
        done();
      });
  });
});
```

## File: `test/client/serialize.js`
```javascript
const assert = require('assert');

const request = require('../support/client');

function serialize(object, res) {
  const value = request.serializeObject(object);
  assert.equal(
    value,
    res,
    `${JSON.stringify(
      object
    )} to "${res}" serialization failed. got: "${value}"`
  );
}

function parse(string_, object) {
  const value = request.parseString(string_);
  assert.deepEqual(
    value,
    object,
    `"${string_}" to ${JSON.stringify(
      object
    )} parse failed. got: ${JSON.stringify(value)}`
  );
}

describe('request.serializeObject()', () => {
  it('should serialize', () => {
    serialize('test', 'test');
    serialize('foo=bar', 'foo=bar');
    serialize({ foo: 'bar' }, 'foo=bar');
    serialize({ foo: null }, 'foo');
    serialize({ foo: 'null' }, 'foo=null');
    serialize({ foo: undefined }, '');
    serialize({ foo: 'undefined' }, 'foo=undefined');
    serialize({ name: 'tj', age: 24 }, 'name=tj&age=24');
    serialize({ name: '&tj&' }, 'name=%26tj%26');
    serialize({ '&name&': 'tj' }, '%26name%26=tj');
    serialize({ hello: '`test`' }, 'hello=%60test%60');
    serialize({ $hello: 'test' }, '$hello=test');
    // eslint-disable-next-line no-dupe-keys
    serialize({ foo: 'foo', foo: 'bar' }, 'foo=foo&foo=bar');
  });
});

describe('request.parseString()', () => {
  it('should parse', () => {
    parse('name=tj', { name: 'tj' });
    parse('name=Manny&species=cat', { name: 'Manny', species: 'cat' });
    parse('redirect=/&ok', { redirect: '/', ok: '' });
    parse('%26name=tj', { '&name': 'tj' });
    parse('name=tj%26', { name: 'tj&' });
    parse('%60', { '`': '' });
  });
});

describe('Merging objects', () => {
  it("Don't mix FormData and JSON", () => {
    if (!window.FormData) {
      // Skip test if FormData is not supported by browser
      return;
    }

    const data = new FormData();
    data.append('foo', 'bar');

    assert.throws(() => {
      request.post('/echo').send(data).send({ allowed: false });
    });
  });

  it("Don't mix Blob and JSON", () => {
    if (!window.Blob) {
      return;
    }

    request
      .post('/echo')
      .send(new Blob(['will be cleared']))
      .send(false)
      .send({ allowed: true });

    assert.throws(() => {
      request
        .post('/echo')
        .send(new Blob(['hello']))
        .send({ allowed: false });
    });
  });
});
```

## File: `test/client/xdomain.js`
```javascript
const assert = require('assert');
const request = require('../support/client');

describe('xdomain', function () {
  this.timeout(20_000);

  // TODO (defunctzombie) I am not certain this actually forces xdomain request
  // use localtunnel.me and tunnel127.com alias instead
  it('should support req.withCredentials()', (next) => {
    request
      .get(`//${window.location.host}/xdomain`)
      .withCredentials()
      .end((error, res) => {
        assert.equal(200, res.status);
        assert.equal('tobi', res.text);
        next();
      });
  });

  // xdomain not supported in old IE and IE11 gives weird Jetty errors (looks like a SauceLabs issue)
  const isIE11 = Boolean(/Trident.*rv[ :]*11\./.test(navigator.userAgent));
  const isIE9OrOlder = !window.atob;
  if (!isIE9OrOlder && !isIE11) {
    // Don't run on IE9 or older, or IE11
    it('should handle x-domain failure', (next) => {
      request.get('//tunne127.com').end((error, res) => {
        assert(error, 'error missing');
        assert(error.crossDomain, 'not .crossDomain');
        next();
      });
    });

    it('should handle x-domain failure after repeat attempts', (next) => {
      request
        .get('//tunne127.com')
        .retry(2)
        .end((error, res) => {
          try {
            assert(error, 'error missing');
            assert(error.crossDomain, 'not .crossDomain');
            assert.equal(2, error.retries, 'expected an error with .retries');
            next();
          } catch (err) {
            next(err);
          }
        });
    });
  }
});
```

## File: `test/node/agency.js`
```javascript
'use strict';

const express = require('../support/express');

const app = express();
const request = require('../support/client');
const assert = require('assert');
const cookieParser = require('cookie-parser');
const cookiejar = require('cookiejar');
const session = require('express-session');
let http = require('http');

if (process.env.HTTP2_TEST) {
  http = require('http2');
  http.Http2ServerResponse.prototype._implicitHeader = function () {
    this.writeHead(this.statusCode);
  };
}

app.use(cookieParser());
app.use(
  session({
    secret: 'secret',
    resave: true,
    saveUninitialized: true
  })
);

app.post('/signin', (request_, res) => {
  request_.session.user = 'hunter@hunterloftis.com';
  res.redirect('/dashboard');
});

app.post('/setcookie', (request_, res) => {
  res.cookie('cookie', 'jar');
  res.sendStatus(200);
});

app.get('/getcookie', (request_, res) => {
  res.status(200).send(request_.cookies.cookie);
});

app.get('/cookieheader', (request_, res) => {
  res.status(200).send(request_.headers.cookie);
});

app.get('/dashboard', (request_, res) => {
  if (request_.session.user) return res.status(200).send('dashboard');
  res.status(401).send('dashboard');
});

app.all('/signout', (request_, res) => {
  request_.session.regenerate(() => {
    res.status(200).send('signout');
  });
});

app.get('/', (request_, res) => {
  if (request_.session.user) return res.redirect('/dashboard');
  res.status(200).send('home');
});

app.post('/redirect', (request_, res) => {
  res.redirect('/simple');
});

app.get('/simple', (request_, res) => {
  res.status(200).send('simple');
});

let base = 'http://localhost';
let server;
before(function listen(done) {
  server = http.createServer(app);
  server = server.listen(0, function listening() {
    base += `:${server.address().port}`;
    done();
  });
});

describe('request', () => {
  describe('persistent agent', () => {
    const agent1 = request.agent();
    const agent2 = request.agent();
    const agent3 = request.agent();
    const agent4 = request.agent();

    it('should gain a session on POST', () =>
      agent3.post(`${base}/signin`).then((res) => {
        assert.equal(res.status, 200);
        assert.ok('set-cookie' in res.headers === false);
        assert.equal(res.text, 'dashboard');
      }));

    it('should start with empty session (set cookies)', (done) => {
      agent1.get(`${base}/dashboard`).end((error, res) => {
        assert.ok(error instanceof Error);
        assert.equal(res.status, 401);
        assert.ok('set-cookie' in res.headers);
        done();
      });
    });

    it('should gain a session (cookies already set)', () =>
      agent1.post(`${base}/signin`).then((res) => {
        assert.equal(res.status, 200);
        assert.ok('set-cookie' in res.headers === false);
        assert.equal('dashboard', res.text);
      }));

    it('should persist cookies across requests', () =>
      agent1.get(`${base}/dashboard`).then((res) => {
        assert.equal(res.status, 200);
      }));

    it('should have the cookie set in the end callback', () =>
      agent4
        .post(`${base}/setcookie`)
        .then(() => agent4.get(`${base}/getcookie`))
        .then((res) => {
          assert.equal(res.status, 200);
          assert.strictEqual(res.text, 'jar');
        }));

    it('should produce a valid cookie header', (done) => {
      agent4
        .set('Cookie', 'first_cookie=dummy; cookie=jam')
        .get(`${base}/cookieheader`)
        .then((res) => {
          const cookiePairs = res.text.split('; '); // https://httpwg.org/specs/rfc6265.html#rfc.section.4.2.1
          assert.deepStrictEqual(cookiePairs, [
            'first_cookie=dummy',
            'cookie=jar',
            `connect.sid=${agent4.jar.getCookie('connect.sid', cookiejar.CookieAccessInfo.All).value}`,
          ]);
          done();
        });
    });

    it('should not share cookies between domains', () => {
      assert.equal(agent4.get('https://google.com').cookies, "");
    });

    it('should send cookies to allowed domain with a different path', () => {
      const postRequest = agent4.post(`${base}/x/y/z`)
      const cookiesNames = postRequest.cookies.split(';').map(cookie => cookie.split('=')[0])
      assert.deepStrictEqual(cookiesNames, ['cookie', ' connect.sid']);
    });

    it('should not share cookies', (done) => {
      agent2.get(`${base}/dashboard`).end((error, res) => {
        assert.ok(error instanceof Error);
        assert.equal(res.status, 401);
        done();
      });
    });

    it('should not lose cookies between agents', () =>
      agent1.get(`${base}/dashboard`).then((res) => {
        assert.equal(res.status, 200);
      }));

    it('should be able to follow redirects', () =>
      agent1.get(base).then((res) => {
        assert.equal(res.status, 200);
        assert.equal(res.text, 'dashboard');
      }));

    it('should be able to post redirects', () =>
      agent1
        .post(`${base}/redirect`)
        .send({ foo: 'bar', baz: 'blaaah' })
        .then((res) => {
          assert.equal(res.status, 200);
          assert.equal(res.text, 'simple');
          assert.deepStrictEqual(res.redirects, [`${base}/simple`]);
        }));

    it('should be able to limit redirects', (done) => {
      agent1
        .get(base)
        .redirects(0)
        .end((error, res) => {
          assert.ok(error instanceof Error);
          assert.equal(res.status, 302);
          assert.deepEqual(res.redirects, []);
          assert.equal(res.header.location, '/dashboard');
          done();
        });
    });

    it('should be able to create a new session (clear cookie)', () =>
      agent1.post(`${base}/signout`).then((res) => {
        assert.equal(res.status, 200);
        assert.ok('set-cookie' in res.headers);
      }));

    it('should regenerate with an empty session', (done) => {
      agent1.get(`${base}/dashboard`).end((error, res) => {
        assert.ok(error instanceof Error);
        assert.equal(res.status, 401);
        assert.ok('set-cookie' in res.headers === false);
        done();
      });
    });
  });
});
```

## File: `test/node/basic-auth.js`
```javascript
const assert = require('assert');
const { format } = require('url');
const request = require('../support/client');
const getSetup = require('../support/setup');

describe('Basic auth', () => {
  let setup;
  let base;

  before(async () => {
    setup = await getSetup();
    base = setup.uri;
  });

  describe('when credentials are present in url', () => {
    it('should set Authorization', (done) => {
      const new_url = new URL(base);
      new_url.username = 'tobi';
      new_url.password = 'learnboost';
      new_url.pathname = '/basic-auth';

      request.get(format(new_url)).end((error, res) => {
        assert.equal(res.status, 200);
        done();
      });
    });
  });

  describe('req.auth(user, pass)', () => {
    it('should set Authorization', (done) => {
      request
        .get(`${base}/basic-auth`)
        .auth('tobi', 'learnboost')
        .end((error, res) => {
          assert.equal(res.status, 200);
          done();
        });
    });
  });

  describe('req.auth(user + ":" + pass)', () => {
    it('should set authorization', (done) => {
      request
        .get(`${base}/basic-auth/again`)
        .auth('tobi')
        .end((error, res) => {
          assert.equal(res.status, 200);
          done();
        });
    });
  });
});
```

## File: `test/node/basic.js`
```javascript
'use strict';

const assert = require('assert');
const fs = require('fs');
const { EventEmitter } = require('events');
const { StringDecoder } = require('string_decoder');
const getSetup = require('../support/setup');
const request = require('../support/client');

const doesntWorkInHttp2 = !process.env.HTTP2_TEST;

describe('[node] request', () => {
  let setup;
  let base;

  before(async () => {
    setup = await getSetup();
    base = setup.uri;
  });

  describe('with an url', () => {
    it('should preserve the encoding of the url', (done) => {
      request.get(`${base}/url?a=(b%29`).end((error, res) => {
        assert.equal('/url?a=(b%29', res.text);
        done();
      });
    });
  });

  describe('with an object', () => {
    it('should format the url', () =>
      request.get(new URL(`${base}/login`)).then((res) => {
        assert.ok(res.ok);
      }));
  });

  describe('without a schema', () => {
    it('should default to http', () =>
      request.get(`${base}/login`).then((res) => {
        assert.equal(res.status, 200);
      }));
  });

  describe('res.toJSON()', () => {
    it('should describe the response', () =>
      request
        .post(`${base}/echo`)
        .send({ foo: 'baz' })
        .then((res) => {
          const object = res.toJSON();
          assert.equal('object', typeof object.header);
          assert.equal('object', typeof object.req);
          assert.equal(200, object.status);
          assert.equal('{"foo":"baz"}', object.text);
        }));
  });

  describe('res.links', () => {
    it('should default to an empty object', () =>
      request.get(`${base}/login`).then((res) => {
        assert.deepEqual(res.links, {});
      }));

    it('should parse the Link header field', (done) => {
      request.get(`${base}/links`).end((error, res) => {
        assert.equal(
          res.links.next,
          'https://api.github.com/repos/visionmedia/mocha/issues?page=2'
        );
        done();
      });
    });
  });

  describe('req.unset(field)', () => {
    it('should remove the header field', (done) => {
      request
        .post(`${base}/echo`)
        .unset('User-Agent')
        .end((error, res) => {
          assert.equal(res.header['user-agent'], undefined);
          done();
        });
    });
  });

  describe('case-insensitive', () => {
    it('should set/get header fields case-insensitively', () => {
      const req = request.post(`${base}/echo`);
      req.set('MiXeD', 'helloes');
      assert.strictEqual(req.get('mixed'), 'helloes');
    });

    it('should unset header fields case-insensitively', () => {
      const req = request.post(`${base}/echo`);
      req.set('MiXeD', 'helloes');
      req.unset('MIXED');
      assert.strictEqual(req.get('mixed'), undefined);
    });
  });

  describe('req.write(str)', () => {
    it('should write the given data', (done) => {
      const request_ = request.post(`${base}/echo`);
      request_.set('Content-Type', 'application/json');
      assert.equal('boolean', typeof request_.write('{"name"'));
      assert.equal('boolean', typeof request_.write(':"tobi"}'));
      request_.end((error, res) => {
        assert.equal(res.text, '{"name":"tobi"}');
        done();
      });
    });
  });

  describe('req.pipe(stream)', () => {
    it('should pipe the response to the given stream', (done) => {
      const stream = new EventEmitter();

      let buf = '';
      stream.writable = true;

      stream.write = function (chunk) {
        buf += chunk;
      };

      stream.end = function () {
        assert.equal(buf, '{"name":"tobi"}');
        done();
      };

      request.post(`${base}/echo`)
        .send('{"name":"tobi"}')
        .pipe(stream);
    });
  });

  describe('ipv6 address', () => {
    it('should successfully query an ipv6 address', (done) => {
      request.get(`http://[::]:${process.env.ZUUL_PORT}/url?a=(b%29`).end((error, res) => {
        assert.equal('/url?a=(b%29', res.text);
        done();
      });
    });

    it('should successfully query an ipv6 address', (done) => {
      request.get(`http://[::1]:${process.env.ZUUL_PORT}/url?a=(b%29`).end((error, res) => {
        assert.equal('/url?a=(b%29', res.text);
        done();
      });
    });
  });

  describe('.buffer()', () => {
    it('should enable buffering', (done) => {
      request
        .get(`${base}/custom`)
        .buffer()
        .end((error, res) => {
          assert.ifError(error);
          assert.equal('custom stuff', res.text);
          assert.ok(res.buffered);
          done();
        });
    });
    it("should take precedence over request.buffer['someMimeType'] = false", (done) => {
      const type = 'application/barbaz';
      const send = 'some text';
      request.buffer[type] = false;
      request
        .post(`${base}/echo`)
        .type(type)
        .send(send)
        .buffer()
        .end((error, res) => {
          delete request.buffer[type];
          assert.ifError(error);
          assert.equal(res.type, type);
          assert.equal(send, res.text);
          assert.ok(res.buffered);
          done();
        });
    });
  });

  describe('.buffer(false)', () => {
    it('should disable buffering', (done) => {
      request
        .post(`${base}/echo`)
        .type('application/x-dog')
        .send('hello this is dog')
        .buffer(false)
        .end((error, res) => {
          assert.ifError(error);
          assert.equal(null, res.text);
          assert.deepEqual(res.body, {});
          let str = '';
          res.setEncoding('utf8');
          res.on('data', (chunk) => {
            str += chunk;
          });
          res.on('end', () => {
            assert.equal(str, 'hello this is dog');
            done();
          });
        });
    });

    it("should take precedence over request.buffer['someMimeType'] = true", (done) => {
      const type = 'application/foobar';
      const send = 'hello this is a dog';
      request.buffer[type] = true;
      request
        .post(`${base}/echo`)
        .type(type)
        .send(send)
        .buffer(false)
        .end((error, res) => {
          delete request.buffer[type];
          assert.ifError(error);
          assert.equal(null, res.text);
          assert.equal(res.type, type);
          assert.equal(res.buffered, false);
          assert.deepEqual(res.body, {});
          let str = '';
          res.setEncoding('utf8');
          res.on('data', (chunk) => {
            str += chunk;
          });
          res.on('end', () => {
            assert.equal(str, send);
            done();
          });
        });
    });
  });

  describe('.withCredentials()', () => {
    it('should not throw an error when using the client-side "withCredentials" method', (done) => {
      request
        .get(`${base}/custom`)
        .withCredentials()
        .end((error, res) => {
          assert.ifError(error);
          done();
        });
    });
  });

  describe('.agent()', () => {
    it('should return the defaut agent', (done) => {
      const agent = request.post(`${base}/echo`).agent();
      assert.equal(agent, false);
      done();
    });
  });

  describe('.agent(undefined)', () => {
    it('should set an agent to undefined and ensure it is chainable', (done) => {
      const request_ = request.get(`${base}/echo`);
      const returnValue = request_.agent(undefined);
      assert.equal(returnValue, request_);
      assert.strictEqual(request_.agent(), undefined);
      done();
    });
  });

  describe('.agent(new http.Agent())', () => {
    it('should set passed agent', (done) => {
      const http = require('http');
      const request_ = request.get(`${base}/echo`);
      const agent = new http.Agent();
      const returnValue = request_.agent(agent);
      assert.equal(returnValue, request_);
      assert.equal(request_.agent(), agent);
      done();
    });
  });

  describe('with a content type other than application/json or text/*', () => {
    it('should still use buffering', () => {
      return request
        .post(`${base}/echo`)
        .type('application/x-dog')
        .send('hello this is dog')
        .then((res) => {
          assert.equal(res.text, null);
          assert.equal(res.body.toString(), 'hello this is dog');
          assert.equal(res.buffered, true);
        });
    });
  });

  describe('content-length', () => {
    it('should be set to the byte length of a non-buffer object', (done) => {
      const decoder = new StringDecoder('utf8');
      let img = fs.readFileSync(`${__dirname}/fixtures/test.png`);
      img = decoder.write(img);
      request
        .post(`${base}/echo`)
        .type('application/x-image')
        .send(img)
        .buffer(false)
        .end((error, res) => {
          assert.ifError(error);
          assert.equal(res.buffered, false);
          assert.equal(res.header['content-length'], Buffer.byteLength(img));
          done();
        });
    });

    it('should be set to the length of a buffer object', (done) => {
      const img = fs.readFileSync(`${__dirname}/fixtures/test.png`);
      request
        .post(`${base}/echo`)
        .type('application/x-image')
        .send(img)
        .buffer(true)
        .end((error, res) => {
          assert.ifError(error);
          assert(res.buffered);
          assert.equal(res.header['content-length'], img.length);
          done();
        });
    });
  });

  if (doesntWorkInHttp2)
    it('should send body with .get().send()', (next) => {
      request
        .get(`${base}/echo`)
        .set('Content-Type', 'text/plain')
        .send('wahoo')
        .end((error, res) => {
          try {
            assert.equal(res.text, 'wahoo');
            next();
          } catch (err) {
            next(err);
          }
        });
    });
});
```

## File: `test/node/buffers.js`
```javascript
'use strict';
const assert = require('assert');
const request = require('../support/client');
const getSetup = require('../support/setup');

describe("req.buffer['someMimeType']", () => {
  let setup;
  let base;

  before(async () => {
    setup = await getSetup();
    base = setup.uri;
  });

  it('should respect that agent.buffer(true) takes precedent', (done) => {
    const agent = request.agent();
    agent.buffer(true);
    const type = 'application/somerandomtype';
    const send = 'somerandomtext';
    request.buffer[type] = false;
    agent
      .post(`${base}/echo`)
      .type(type)
      .send(send)
      .end((error, res) => {
        delete request.buffer[type];
        assert.ifError(error);
        assert.equal(res.type, type);
        assert.equal(send, res.text);
        assert(res.buffered);
        done();
      });
  });

  it('should respect that agent.buffer(false) takes precedent', (done) => {
    const agent = request.agent();
    agent.buffer(false);
    const type = 'application/barrr';
    const send = 'some random text2';
    request.buffer[type] = true;
    agent
      .post(`${base}/echo`)
      .type(type)
      .send(send)
      .end((error, res) => {
        delete request.buffer[type];
        assert.ifError(error);
        assert.equal(null, res.text);
        assert.equal(res.type, type);
        assert(!res.buffered);
        res.body.should.eql({});
        let buf = '';
        res.setEncoding('utf8');
        res.on('data', (chunk) => {
          buf += chunk;
        });
        res.on('end', () => {
          buf.should.equal(send);
          done();
        });
      });
  });

  it('should disable buffering for that mimetype when false', (done) => {
    const type = 'application/bar';
    const send = 'some random text';
    request.buffer[type] = false;
    request
      .post(`${base}/echo`)
      .type(type)
      .send(send)
      .end((error, res) => {
        delete request.buffer[type];
        assert.ifError(error);
        assert.equal(null, res.text);
        assert.equal(res.type, type);
        assert(!res.buffered);
        res.body.should.eql({});
        let buf = '';
        res.setEncoding('utf8');
        res.on('data', (chunk) => {
          buf += chunk;
        });
        res.on('end', () => {
          buf.should.equal(send);
          done();
        });
      });
  });
  it('should enable buffering for that mimetype when true', (done) => {
    const type = 'application/baz';
    const send = 'woooo';
    request.buffer[type] = true;
    request
      .post(`${base}/echo`)
      .type(type)
      .send(send)
      .end((error, res) => {
        delete request.buffer[type];
        assert.ifError(error);
        assert.equal(res.type, type);
        assert.equal(send, res.text);
        assert(res.buffered);
        done();
      });
  });
  it('should fallback to default handling for that mimetype when undefined', () => {
    const type = 'application/bazzz';
    const send = 'woooooo';
    return request
      .post(`${base}/echo`)
      .type(type)
      .send(send)
      .then((res) => {
        assert.equal(res.type, type);
        assert.equal(send, res.body.toString());
        assert(res.buffered);
      });
  });
});
```

## File: `test/node/exports.js`
```javascript
'use strict';
const request = require('../support/client');

describe('exports', () => {
  it('should expose .protocols', () => {
    Object.keys(request.protocols).should.eql(['http:', 'https:', 'http2:']);
  });

  it('should expose .serialize', () => {
    Object.keys(request.serialize).should.eql([
      'application/x-www-form-urlencoded',
      'application/json'
    ]);
  });

  it('should expose .parse', () => {
    Object.keys(request.parse).should.eql([
      'application/x-www-form-urlencoded',
      'application/json',
      'text',
      'application/json-seq',
      'application/octet-stream',
      'application/pdf',
      'image'
    ]);
  });

  it('should export .buffer', () => {
    Object.keys(request.buffer).should.eql([]);
  });
});
```

## File: `test/node/flags.js`
```javascript
'use strict';

const assert = require('assert');
const request = require('../support/client');
const getSetup = require('../support/setup');

describe('flags', () => {
  let setup;
  let base;

  before(async () => {
    setup = await getSetup();
    base = setup.uri;
  });

  describe('with 4xx response', () => {
    it('should set res.error and res.clientError', (done) => {
      request.get(`${base}/notfound`).end((error, res) => {
        assert(error);
        assert(!res.ok, 'response should not be ok');
        assert(res.error, 'response should be an error');
        assert(res.clientError, 'response should be a client error');
        assert(!res.serverError, 'response should not be a server error');
        done();
      });
    });
  });

  describe('with 5xx response', () => {
    it('should set res.error and res.serverError', (done) => {
      request.get(`${base}/error`).end((error, res) => {
        assert(error);
        assert(!res.ok, 'response should not be ok');
        assert(!res.notFound, 'response should not be notFound');
        assert(res.error, 'response should be an error');
        assert(!res.clientError, 'response should not be a client error');
        assert(res.serverError, 'response should be a server error');
        done();
      });
    });
  });

  describe('with 404 Not Found', () => {
    it('should res.notFound', (done) => {
      request.get(`${base}/notfound`).end((error, res) => {
        assert(error);
        assert(res.notFound, 'response should be .notFound');
        done();
      });
    });
  });

  describe('with 400 Bad Request', () => {
    it('should set req.badRequest', (done) => {
      request.get(`${base}/bad-request`).end((error, res) => {
        assert(error);
        assert(res.badRequest, 'response should be .badRequest');
        done();
      });
    });
  });

  describe('with 401 Bad Request', () => {
    it('should set res.unauthorized', (done) => {
      request.get(`${base}/unauthorized`).end((error, res) => {
        assert(error);
        assert(res.unauthorized, 'response should be .unauthorized');
        done();
      });
    });
  });

  describe('with 406 Not Acceptable', () => {
    it('should set res.notAcceptable', (done) => {
      request.get(`${base}/not-acceptable`).end((error, res) => {
        assert(error);
        assert(res.notAcceptable, 'response should be .notAcceptable');
        done();
      });
    });
  });

  describe('with 204 No Content', () => {
    it('should set res.noContent', (done) => {
      request.get(`${base}/no-content`).end((error, res) => {
        assert(!error);
        assert(res.noContent, 'response should be .noContent');
        done();
      });
    });
  });

  describe('with 201 Created', () => {
    it('should set res.created', (done) => {
      request.post(`${base}/created`).end((error, res) => {
        assert(!error);
        assert(res.created, 'response should be .created');
        done();
      });
    });
  });

  describe('with 422 Unprocessable Entity', () => {
    it('should set res.unprocessableEntity', (done) => {
      request.post(`${base}/unprocessable-entity`).end((error, res) => {
        assert(error);
        assert(
          res.unprocessableEntity,
          'response should be .unprocessableEntity'
        );

        done();
      });
    });
  });
});
```

## File: `test/node/form.js`
```javascript
'use strict';

const assert = require('assert');
const request = require('../support/client');
const getSetup = require('../support/setup');

describe('Merging objects', () => {
  let setup;
  let base;

  before(async () => {
    setup = await getSetup();
    base = setup.uri;
  });

  it("Don't mix Buffer and JSON", () => {
    assert.throws(() => {
      request
        .post('/echo')
        .send(Buffer.from('some buffer'))
        .send({ allowed: false });
    });
  });
});

describe('req.send(String)', () => {
  let setup;
  let base;

  before(async () => {
    setup = await getSetup();
    base = setup.uri;
  });

  it('should default to "form"', (done) => {
    request
      .post(`${base}/echo`)
      .send('user[name]=tj')
      .send('user[email]=tj@vision-media.ca')
      .end((error, res) => {
        res.header['content-type'].should.equal(
          'application/x-www-form-urlencoded'
        );
        res.body.should.eql({
          user: { name: 'tj', email: 'tj@vision-media.ca' }
        });
        done();
      });
  });
});

describe('res.body', () => {
  let setup;
  let base;

  before(async () => {
    setup = await getSetup();
    base = setup.uri;
  });

  describe('application/x-www-form-urlencoded', () => {
    it('should parse the body', (done) => {
      request.get(`${base}/form-data`).end((error, res) => {
        res.text.should.equal('pet[name]=manny');
        res.body.should.eql({ pet: { name: 'manny' } });
        done();
      });
    });
  });
});
```

## File: `test/node/http2.js`
```javascript
'use strict';
if (!process.env.HTTP2_TEST) {
  return;
}

const assert = require('assert');
const request = require('../..');
const getSetup = require('../support/setup');

describe('request.get().http2()', () => {
  let setup;
  let base;

  before(async () => {
    setup = await getSetup();
    base = setup.uri;
  });

  it('should preserve the encoding of the url', (done) => {
    request
      .get(`${base}/url?a=(b%29`)
      .http2()
      .end((error, res) => {
        assert.equal('/url?a=(b%29', res.text);
        done();
      });
  });

  it('should format the url', () =>
    request
      .get(new URL(`${base}/login`))
      .http2()
      .then((res) => {
        assert(res.ok);
      }));

  it.skip('should default to http', () =>
    request
      .get('localhost:5000/login')
      .http2()
      .then((res) => {
        assert.equal(res.status, 200);
      }));
});
```

## File: `test/node/https.js`
```javascript
'use strict';

const assert = require('assert');

const https = require('https');
const fs = require('fs');
const express = require('../support/express');
const request = require('../support/client');

const app = express();

const ca = fs.readFileSync(`${__dirname}/fixtures/ca.cert.pem`);
const key = fs.readFileSync(`${__dirname}/fixtures/key.pem`);
const pfx = fs.readFileSync(`${__dirname}/fixtures/cert.pfx`);
const cert = fs.readFileSync(`${__dirname}/fixtures/cert.pem`);
const passpfx = fs.readFileSync(`${__dirname}/fixtures/passcert.pfx`);

/*

openssl genrsa -out ca.key.pem 2048
openssl req -x509 -new -nodes -key ca.key.pem -sha256 -days 5000 -out ca.cert.pem # specify CN = CA

openssl genrsa -out key.pem 2048
openssl req -new -key key.pem -out cert.csr # specify CN = localhost

openssl x509 -req -in cert.csr -CA ca.cert.pem -CAkey ca.key.pem -CAcreateserial -out cert.pem -days 5000 -sha256
openssl pkcs12 -export -in cert.pem -inkey key.pem -out cert.pfx # empty password

openssl pkcs12 -export -in cert.pem -inkey key.pem -out passcert.pfx # password test

 */
let http2;
if (process.env.HTTP2_TEST) {
  http2 = require('http2');
}

let server;

app.get('/', (request_, res) => {
  res.send('Safe and secure!');
});

// WARNING: this .listen() boilerplate is slightly different from most tests
// due to HTTPS. Do not copy/paste without examination.
const base = 'https://localhost';
let testEndpoint;

describe('https', () => {
  describe('certificate authority', () => {
    before(function listen(done) {
      server = process.env.HTTP2_TEST
        ? http2.createSecureServer(
            {
              key,
              cert
            },
            app
          )
        : https.createServer(
            {
              key,
              cert
            },
            app
          );

      server.listen(0, function listening() {
        testEndpoint = `${base}:${server.address().port}`;
        done();
      });
    });

    after(() => {
      if (server) server.close();
    });

    describe('request', () => {
      it('should give a good response', (done) => {
        request
          .get(testEndpoint)
          .ca(ca)
          .end((error, res) => {
            assert.ifError(error);
            assert(res.ok);
            assert.strictEqual('Safe and secure!', res.text);
            done();
          });
      });

      it('should reject unauthorized response', () => {
        return request
          .get(testEndpoint)
          .trustLocalhost(false)
          .then(
            () => {
              throw new Error('Allows MITM');
            },
            () => {}
          );
      });

      it('should not reject unauthorized response', () => {
        return request
          .get(testEndpoint)
          .disableTLSCerts()
          .then(({ status }) => {
            assert.strictEqual(status, 200);
          });
      });

      it('should trust localhost unauthorized response', () => {
        return request.get(testEndpoint).trustLocalhost(true);
      });

      it('should trust overriden localhost unauthorized response', () => {
        return request
          .get(`https://example.com:${server.address().port}`)
          .connect('127.0.0.1')
          .trustLocalhost();
      });
    });

    describe('.agent', () => {
      it('should be able to make multiple requests without redefining the certificate', (done) => {
        const agent = request.agent({ ca });
        agent.get(testEndpoint).end((error, res) => {
          assert.ifError(error);
          assert(res.ok);
          assert.strictEqual('Safe and secure!', res.text);
          agent.get(new URL(testEndpoint)).end((error, res) => {
            assert.ifError(error);
            assert(res.ok);
            assert.strictEqual('Safe and secure!', res.text);
            done();
          });
        });
      });
    });
  });

  describe.skip('client certificates', () => {
    before(function listen(done) {
      server = process.env.HTTP2_TEST
        ? http2.createSecureServer(
            {
              ca,
              key,
              cert,
              requestCert: true,
              rejectUnauthorized: true
            },
            app
          )
        : https.createServer(
            {
              ca,
              key,
              cert,
              requestCert: true,
              rejectUnauthorized: true
            },
            app
          );

      server.listen(0, function listening() {
        testEndpoint = `${base}:${server.address().port}`;
        done();
      });
    });

    after(() => {
      if (server) server.close();
    });

    describe('request', () => {
      it('should give a good response with client certificates and CA', (done) => {
        request
          .get(testEndpoint)
          .ca(ca)
          .key(key)
          .cert(cert)
          .end((error, res) => {
            assert.ifError(error);
            assert(res.ok);
            assert.strictEqual('Safe and secure!', res.text);
            done();
          });
      });
      it('should give a good response with client pfx', (done) => {
        request
          .get(testEndpoint)
          .pfx(pfx)
          .end((error, res) => {
            assert.ifError(error);
            assert(res.ok);
            assert.strictEqual('Safe and secure!', res.text);
            done();
          });
      });
      it('should give a good response with client pfx with passphrase', (done) => {
        request
          .get(testEndpoint)
          .pfx({
            pfx: passpfx,
            passphrase: 'test'
          })
          .end((error, res) => {
            assert.ifError(error);
            assert(res.ok);
            assert.strictEqual('Safe and secure!', res.text);
            done();
          });
      });
    });

    describe('.agent', () => {
      it('should be able to make multiple requests without redefining the certificates', (done) => {
        const agent = request.agent({ ca, key, cert });
        agent.get(testEndpoint).end((error, res) => {
          assert.ifError(error);
          assert(res.ok);
          assert.strictEqual('Safe and secure!', res.text);
          agent.get(new URL(testEndpoint)).end((error, res) => {
            assert.ifError(error);
            assert(res.ok);
            assert.strictEqual('Safe and secure!', res.text);
            done();
          });
        });
      });
      it('should be able to make multiple requests without redefining pfx', (done) => {
        const agent = request.agent({ pfx });
        agent.get(testEndpoint).end((error, res) => {
          assert.ifError(error);
          assert(res.ok);
          assert.strictEqual('Safe and secure!', res.text);
          agent.get(new URL(testEndpoint)).end((error, res) => {
            assert.ifError(error);
            assert(res.ok);
            assert.strictEqual('Safe and secure!', res.text);
            done();
          });
        });
      });
    });
  });
});
```

## File: `test/node/image.js`
```javascript
'use strict';

const fs = require('fs');
const request = require('../support/client');
const getSetup = require('../support/setup');

const img = fs.readFileSync(`${__dirname}/fixtures/test.png`);

describe('res.body', () => {
  let setup;
  let base;

  before(async () => {
    setup = await getSetup();
    base = setup.uri;
  });

  describe('image/png', () => {
    it('should parse the body', (done) => {
      request.get(`${base}/image`).end((error, res) => {
        res.type.should.equal('image/png');
        Buffer.isBuffer(res.body).should.be.true();
        (res.body.length - img.length).should.equal(0);
        done();
      });
    });
  });
  describe('application/octet-stream', () => {
    it('should parse the body', (done) => {
      request
        .get(`${base}/image-as-octets`)
        .buffer(true) // that's tech debt :(
        .end((error, res) => {
          res.type.should.equal('application/octet-stream');
          Buffer.isBuffer(res.body).should.be.true();
          (res.body.length - img.length).should.equal(0);
          done();
        });
    });
  });
  describe('application/octet-stream', () => {
    it('should parse the body (using responseType)', (done) => {
      request
        .get(`${base}/image-as-octets`)
        .responseType('blob')
        .end((error, res) => {
          res.type.should.equal('application/octet-stream');
          Buffer.isBuffer(res.body).should.be.true();
          (res.body.length - img.length).should.equal(0);
          done();
        });
    });
  });
});
```

## File: `test/node/incoming-multipart.js`
```javascript
// var request = require('../support/client')
//   , express = require('express')
//   , assert = require('assert')
//   , app = express()
//   , fs = require('fs');

// app.get('/', function(req, res){
//   res.set('Content-Type', 'multipart/form-data; boundary=awesome');
//   // res.write('\r\n'); TODO: formidable bug
//   res.write('--awesome\r\n');
//   res.write('Content-Disposition: attachment; name="image"; filename="something.png"\r\n');
//   res.write('Content-Type: image/png\r\n');
//   res.write('\r\n');
//   res.write('some data');
//   res.write('\r\n--awesome\r\n');
//   res.write('Content-Disposition: form-data; name="name"\r\n');
//   res.write('Content-Type: text/plain\r\n');
//   res.write('\r\n');
//   res.write('tobi');
//   res.write('\r\n--awesome--');
//   setTimeout(function(){ // TODO: lolnode...
//     res.end();
//   }, 1000);
// });

// var base = 'http://localhost'
// var server;
// before(function listen(done) {
//   server = app.listen(0, function listening() {
//     base += ':' + server.address().port;
//     done();
//   });
// });

// describe('request multipart/form-data', function(){
//   describe('req.body', function(){
//     it('should be populated with fields', function(done){
//       request.get(base, function(err, res){
//         if (err) return done(err);
//         res.status.should.equal(200);
//         res.body.should.eql({ name: 'tobi' });
//         res.files.image.name.should.equal('something.png');
//         res.files.image.type.should.equal('image/png');
//         assert.equal(null, res.text, 'res.text should be empty for multipart');
//         done();
//       });
//     })
//   })
// })
```

## File: `test/node/inflate.js`
```javascript
'use strict';
require('should');
require('should-http');

const assert = require('assert');
const zlib = require('zlib');
let http = require('http');
const getPort = require('get-port');
const express = require('../support/express');
const request = require('../support/client');

if (process.env.HTTP2_TEST) {
  http = require('http2');
}

const app = express();
const subject = 'some long long long long string';

let base = 'http://localhost';
let server;

before(function listen(done) {
  server = http.createServer(app);

  getPort().then((port) => {
    server = server.listen(port, function listening() {
      base += `:${server.address().port}`;
      done();
    });
  });
});

app.get('/binary', (request_, res) => {
  zlib.deflate(subject, (error, buf) => {
    res.set('Content-Encoding', 'gzip');
    res.send(buf);
  });
});

app.get('/binary-brotli', (request_, res) => {
  zlib.brotliCompress(subject, (error, buf) => {
    res.set('Content-Encoding', 'br');
    res.send(buf);
  });
});

app.get('/corrupt', (request_, res) => {
  res.set('Content-Encoding', 'gzip');
  res.send('blah');
});

app.get('/corrupt-brotli', (request_, res) => {
  res.set('Content-Encoding', 'br');
  res.send('blah');
});

app.get('/nocontent', (request_, res, next) => {
  res.statusCode = 204;
  res.set('Content-Type', 'text/plain');
  res.set('Content-Encoding', 'gzip');
  res.send('');
});

app.get('/nocontent-brotli', (request_, res, next) => {
  res.statusCode = 204;
  res.set('Content-Type', 'text/plain');
  res.set('Content-Encoding', 'br');
  res.send('');
});

app.get('/', (request_, res, next) => {
  zlib.deflate(subject, (error, buf) => {
    res.set('Content-Type', 'text/plain');
    res.set('Content-Encoding', 'gzip');
    res.send(buf);
  });
});

app.get('/junk', (request_, res) => {
  zlib.deflate(subject, (error, buf) => {
    res.set('Content-Type', 'text/plain');
    res.set('Content-Encoding', 'gzip');
    res.write(buf);
    res.end(' 0 junk');
  });
});

app.get('/junk-brotli', (request_, res) => {
  zlib.brotliCompress(subject, (error, buf) => {
    res.set('Content-Type', 'text/plain');
    res.set('Content-Encoding', 'br');
    res.write(buf);
    res.end(' 0 junk');
  });
});

app.get('/chopped', (request_, res) => {
  zlib.deflate(`${subject}123456`, (error, buf) => {
    res.set('Content-Type', 'text/plain');
    res.set('Content-Encoding', 'gzip');
    res.send(buf.slice(0, -1));
  });
});

app.get('/chopped-brotli', (request_, res) => {
  zlib.brotliCompress(`${subject}123456`, (error, buf) => {
    res.set('Content-Type', 'text/plain');
    res.set('Content-Encoding', 'br');
    res.send(buf.slice(0, -1));
  });
});

describe('zlib', () => {
  it('should deflate the content', (done) => {
    request.get(base).end((error, res) => {
      res.should.have.status(200);
      res.text.should.equal(subject);
      res.headers['content-length'].should.be.below(subject.length);
      done();
    });
  });

  it('should protect from zip bombs', (done) => {
    request
      .get(base)
      .buffer(true)
      .maxResponseSize(1)
      .end((error, res) => {
        try {
          assert.equal('Maximum response size reached', error && error.message);
          done();
        } catch (err) {
          done(err);
        }
      });
  });

  it('should ignore trailing junk', (done) => {
    request.get(`${base}/junk`).end((error, res) => {
      res.should.have.status(200);
      res.text.should.equal(subject);
      done();
    });
  });

  it('should ignore trailing junk-brotli', (done) => {
    request.get(`${base}/junk-brotli`).end((error, res) => {
      res.should.have.status(200);
      res.text.should.equal(subject);
      done();
    });
  });

  it('should ignore missing data', (done) => {
    request.get(`${base}/chopped`).end((error, res) => {
      assert.equal(undefined, error);
      res.should.have.status(200);
      res.text.should.startWith(subject);
      done();
    });
  });

  it('should ignore missing brotli data', (done) => {
    request.get(`${base}/chopped-brotli`).end((error, res) => {
      assert.equal(undefined, error);
      res.should.have.status(200);
      res.text.should.startWith(subject);
      done();
    });
  });

  it('should handle corrupted responses', (done) => {
    request.get(`${base}/corrupt`).end((error, res) => {
      assert(error, 'missing error');
      assert(!res, 'response should not be defined');
      done();
    });
  });

  it('should handle brotli corrupted responses', (done) => {
    request.get(`${base}/corrupt-brotli`).end((error, res) => {
      res.text.should.equal('');
      done();
    });
  });

  it('should handle no content with gzip header', (done) => {
    request.get(`${base}/nocontent`).end((error, res) => {
      assert.ifError(error);
      assert(res);
      res.should.have.status(204);
      res.text.should.equal('');
      res.headers.should.not.have.property('content-length');
      done();
    });
  });

  it('should handle no content with gzip header', (done) => {
    request.get(`${base}/nocontent-brotli`).end((error, res) => {
      assert.ifError(error);
      assert(res);
      res.should.have.status(204);
      res.text.should.equal('');
      res.headers.should.not.have.property('content-length');
      done();
    });
  });

  describe('without encoding set', () => {
    it('should buffer if asked', () => {
      return request
        .get(`${base}/binary`)
        .buffer(true)
        .then((res) => {
          res.should.have.status(200);
          assert(res.headers['content-length']);
          assert(res.body.byteLength);
          assert.equal(subject, res.body.toString());
        });
    });

    it('should buffer Brotli if asked', () => {
      return request
        .get(`${base}/binary-brotli`)
        .buffer(true)
        .then((res) => {
          res.should.have.status(200);
          assert(res.headers['content-length']);
          assert(res.body.byteLength);
          assert.equal(subject, res.body.toString());
        });
    });

    it('should emit buffers', (done) => {
      request.get(`${base}/binary`).end((error, res) => {
        res.should.have.status(200);
        res.headers['content-length'].should.be.below(subject.length);

        res.on('data', (chunk) => {
          chunk.should.have.length(subject.length);
        });

        res.on('end', done);
      });
    });
  });
});
```

## File: `test/node/lookup.js`
```javascript
'use strict';
const assert = require('assert');
const dns = require('dns');
const request = require('../support/client');
const getSetup = require('../support/setup');

let base = null;

function myLookup(hostname, options, callback) {
  dns.lookup(hostname, options, callback);
}

describe('req.lookup()', () => {
  before(async () => {
    const setup = await getSetup();
    base = setup.uri;
  });
  it('should set a custom lookup', (done) => {
    const r = request.get(`${base}/ok`).lookup(myLookup);
    assert(r.lookup() === myLookup);
    r.then((res) => {
      res.text.should.equal('ok');
      done();
    });
  });
});
```

## File: `test/node/multipart.js`
```javascript
'use strict';

const assert = require('assert');
const fs = require('fs');
const path = require('path');
const should = require('should');
const getPort = require('get-port');
const request = require('../support/client');
const getSetup = require('../support/setup');
const IS_WINDOWS = require('os').platform() === 'win32';

function read(file) {
  return fs.readFileSync(file, 'utf8');
}

function getFullPath(filename) {
  if (!IS_WINDOWS) {
    return filename;
  }

  const fullPath = path.join(__dirname, '../../', filename);
  return fullPath;
}

describe('Multipart', () => {
  let setup;
  let base;

  before(async () => {
    setup = await getSetup();
    base = setup.uri;
  });

  describe('#field(name, value)', () => {
    it('should set a multipart field value', () => {
      const request_ = request.post(`${base}/echo`);

      request_.field('user[name]', 'tobi');
      request_.field('user[age]', '2');
      request_.field('user[species]', 'ferret');

      return request_.then((res) => {
        res.body['user[name]'].should.equal('tobi');
        res.body['user[age]'].should.equal('2');
        res.body['user[species]'].should.equal('ferret');
      });
    });

    it('should work with file attachments', () => {
      const request_ = request.post(`${base}/echo`);

      request_.field('name', 'Tobi');
      request_.attach('document', 'test/node/fixtures/user.html');
      request_.field('species', 'ferret');

      return request_.then((res) => {
        res.body.name.should.equal('Tobi');
        res.body.species.should.equal('ferret');

        const html = res.files.document;
        html.originalFilename.should.equal('user.html');
        html.mimetype.should.equal('text/html');
        read(html.filepath).should.equal('<h1>name</h1>');
      });
    });
  });

  describe('#attach(name, path)', () => {
    it('should attach a file', () => {
      const request_ = request.post(`${base}/echo`);

      request_.attach('one', 'test/node/fixtures/user.html');
      request_.attach('two', 'test/node/fixtures/user.json');
      request_.attach('three', 'test/node/fixtures/user.txt');

      return request_.then((res) => {
        const html = res.files.one;
        const json = res.files.two;
        const text = res.files.three;

        html.originalFilename.should.equal('user.html');
        html.mimetype.should.equal('text/html');
        read(html.filepath).should.equal('<h1>name</h1>');

        json.originalFilename.should.equal('user.json');
        json.mimetype.should.equal('application/json');
        read(json.filepath).should.equal('{"name":"tobi"}');

        text.originalFilename.should.equal('user.txt');
        text.mimetype.should.equal('text/plain');
        read(text.filepath).should.equal('Tobi');
      });
    });

    describe('when a file does not exist', () => {
      it('should fail the request with an error', (done) => {
        const request_ = request.post(`${base}/echo`);

        request_.attach('name', 'foo');
        // request_.attach('name2', 'bar');
        // request_.attach('name3', 'baz');

        request_.end((error, res) => {
          assert.ok(Boolean(error), 'Request should have failed.');
          error.code.should.equal('ENOENT');
          error.message.should.containEql('ENOENT');
          if (IS_WINDOWS) {
            error.path
              .toLowerCase()
              .should.equal(getFullPath('foo').toLowerCase());
          } else {
            error.path.should.equal(getFullPath('foo'));
          }

          done();
        });
      });

      it('promise should fail', () => {
        return request
          .post(`${base}/echo`)
          .field({ a: 1, b: 2 })
          .attach('c', 'does-not-exist.txt')
          .then(
            (res) => assert.fail('It should not allow this'),
            (err) => {
              err.code.should.equal('ENOENT');
              if (IS_WINDOWS) {
                err.path
                  .toLowerCase()
                  .should.equal(
                    getFullPath('does-not-exist.txt').toLowerCase()
                  );
              } else {
                err.path.should.equal(getFullPath('does-not-exist.txt'));
              }
            }
          );
      });

      it('should report ENOENT via the callback', (done) => {
        request
          .post(`${base}/echo`)
          .attach('name', 'file-does-not-exist')
          .end((error, res) => {
            assert.ok(Boolean(error), 'Request should have failed');
            error.code.should.equal('ENOENT');
            done();
          });
      });

      it('should report ENOENT via Promise', () => {
        return request
          .post(`${base}/echo`)
          .attach('name', 'file-does-not-exist')
          .then(
            (res) => assert.fail('Request should have failed'),
            (err) => err.code.should.equal('ENOENT')
          );
      });
    });
  });

  describe('#attach(name, path, filename)', () => {
    it('should use the custom filename', () =>
      request
        .post(`${base}/echo`)
        .attach('document', 'test/node/fixtures/user.html', 'doc.html')
        .then((res) => {
          const html = res.files.document;
          html.originalFilename.should.equal('doc.html');
          html.mimetype.should.equal('text/html');
          read(html.filepath).should.equal('<h1>name</h1>');
        }));
    it('should fire progress event', (done) => {
      let loaded = 0;
      let total = 0;
      let uploadEventWasFired = false;
      request
        .post(`${base}/echo`)
        .attach('document', 'test/node/fixtures/user.html')
        .on('progress', (event) => {
          total = event.total;
          loaded = event.loaded;
          if (event.direction === 'upload') {
            uploadEventWasFired = true;
          }
        })
        .end((error, res) => {
          if (error) return done(error);
          const html = res.files.document;
          html.originalFilename.should.equal('user.html');
          html.mimetype.should.equal('text/html');
          read(html.filepath).should.equal('<h1>name</h1>');
          total.should.equal(223);
          loaded.should.equal(223);
          uploadEventWasFired.should.equal(true);
          done();
        });
    });
    it('filesystem errors should be caught', (done) => {
      request
        .post(`${base}/echo`)
        .attach('filedata', 'test/node/fixtures/non-existent-file.ext')
        .end((error, res) => {
          assert.ok(Boolean(error), 'Request should have failed.');
          error.code.should.equal('ENOENT');
          if (IS_WINDOWS) {
            error.path
              .toLowerCase()
              .should.equal(
                getFullPath(
                  'test/node/fixtures/non-existent-file.ext'
                ).toLowerCase()
              );
          } else {
            error.path.should.equal(
              getFullPath('test/node/fixtures/non-existent-file.ext')
            );
          }

          done();
        });
    });
  });

  describe('#field(name, val)', () => {
    it('should set a multipart field value', (done) => {
      request
        .post(`${base}/echo`)
        .field('first-name', 'foo')
        .field('last-name', 'bar')
        .end((error, res) => {
          if (error) done(error);
          res.should.be.ok();
          res.body['first-name'].should.equal('foo');
          res.body['last-name'].should.equal('bar');
          done();
        });
    });
  });

  describe('#field(object)', () => {
    it('should set multiple multipart fields', (done) => {
      request
        .post(`${base}/echo`)
        .field({ 'first-name': 'foo', 'last-name': 'bar' })
        .end((error, res) => {
          if (error) done(error);
          res.should.be.ok();
          res.body['first-name'].should.equal('foo');
          res.body['last-name'].should.equal('bar');
          done();
        });
    });
  });
});
```

## File: `test/node/network-error.js`
```javascript
'use strict';
const assert = require('assert');
const net = require('net');
const request = require('../support/client');
const express = require('../support/express');

function getFreePort(fn) {
  const server = net.createServer();
  server.listen(0, () => {
    const { port } = server.address();
    server.close(() => {
      fn(port);
    });
  });
}

describe('with network error', () => {
  before(function (done) {
    // connecting to a free port
    // will trigger a connection refused
    getFreePort((port) => {
      this.port = port;
      done();
    });
  });

  it('should error', function (done) {
    request.get(`http://localhost:${this.port}/`).end((error, res) => {
      assert(error, 'expected an error');
      done();
    });
  });
});
```

## File: `test/node/not-modified.js`
```javascript
'use strict';
const request = require('../support/client');
const getSetup = require('../support/setup');

describe('request', () => {
  let setup;
  let base;

  before(async () => {
    setup = await getSetup();
    base = setup.uri;
  });

  describe('not modified', () => {
    let ts;
    it('should start with 200', (done) => {
      request.get(`${base}/if-mod`).end((error, res) => {
        res.should.have.status(200);
        res.text.should.match(/^\d+$/);
        ts = Number(res.text);
        done();
      });
    });

    it('should then be 304', (done) => {
      request
        .get(`${base}/if-mod`)
        .set('If-Modified-Since', new Date(ts).toUTCString())
        .end((error, res) => {
          res.should.have.status(304);
          // res.text.should.be.empty
          done();
        });
    });
  });
});
```

## File: `test/node/parsers.js`
```javascript
'use strict';
const assert = require('assert');
const request = require('../support/client');
const getSetup = require('../support/setup');

const doesntWorkInHttp2 = !process.env.HTTP2_TEST;

describe('req.parse(fn)', () => {
  let setup;
  let base;

  before(async () => {
    setup = await getSetup();
    base = setup.uri;
  });

  it('should take precedence over default parsers', (done) => {
    request
      .get(`${base}/manny`)
      .parse(request.parse['application/json'])
      .end((error, res) => {
        assert(res.ok);
        assert.equal('{"name":"manny"}', res.text);
        assert.equal('manny', res.body.name);
        done();
      });
  });

  it('should be the only parser', () =>
    request
      .get(`${base}/image`)
      .buffer(false)
      .parse((res, fn) => {
        res.on('data', () => {});
      })
      .then((res) => {
        assert(res.ok);
        assert.strictEqual(res.text, undefined);
        res.body.should.eql({});
      }));

  it('should emit error if parser throws', (done) => {
    request
      .get(`${base}/manny`)
      .parse(() => {
        throw new Error('I am broken');
      })
      .on('error', (error) => {
        error.message.should.equal('I am broken');
        done();
      })
      .end();
  });

  it('should emit error if parser returns an error', (done) => {
    request
      .get(`${base}/manny`)
      .parse((res, fn) => {
        fn(new Error('I am broken'));
      })
      .on('error', (error) => {
        error.message.should.equal('I am broken');
        done();
      })
      .end();
  });

  if (doesntWorkInHttp2)
    it('should not emit error on chunked json', (done) => {
      request.get(`${base}/chunked-json`).end((error) => {
        assert.ifError(error);
        done();
      });
    });

  if (doesntWorkInHttp2)
    it('should not emit error on aborted chunked json', (done) => {
      const request_ = request.get(`${base}/chunked-json`);
      request_.end((error) => {
        assert.ifError(error);
        done();
      });

      setTimeout(() => {
        request_.abort();
      }, 150);
    });
});
```

## File: `test/node/pipe-callback.js`
```javascript
const assert = require('node:assert');
const { Readable } = require('node:stream');
const getSetup = require('../support/setup');
const request = require('../support/client');

describe('[node] pipe callback handling', () => {
  let setup;
  let base;

  before(async () => {
    setup = await getSetup();
    base = setup.uri;
  });

  it('should work with pipe without callback', (done) => {
    const body = Readable.from(JSON.stringify({ name: 'john' }));
    const request_ = request
      .post(`${base}/echo`)
      .set('Content-Type', 'application/json')
      .on('response', (res) => {
        assert(res);
        assert.equal(res.status, 200);
        assert.equal(res.text, '{"name":"john"}');
        done();
      });

    body.pipe(request_);
  });

  it('should work with pipe and callback', (done) => {
    const body = Readable.from(JSON.stringify({ name: 'jane' }));
    const request_ = request
      .post(`${base}/echo`)
      .set('Content-Type', 'application/json')
      .on('response', (res) => {
        assert(res);
        assert.equal(res.status, 200);
        assert.equal(res.text, '{"name":"jane"}');
        done();
      });

    body.pipe(request_);
  });
});
```

## File: `test/node/pipe-redirect.js`
```javascript
'use strict';
const fs = require('fs');
const request = require('../support/client');
const getSetup = require('../support/setup');

describe('pipe on redirect', () => {
  let setup;
  let base;
  const destinationPath = 'test/node/fixtures/pipe.txt';

  before(async () => {
    setup = await getSetup();
    base = setup.uri;
  });

  after((done) => {
    // Remove tmp file
    fs.unlink(destinationPath, done);
  });

  it('should follow Location', (done) => {
    const stream = fs.createWriteStream(destinationPath);
    const redirects = [];
    const request_ = request
      .get(base)
      .on('redirect', (res) => {
        redirects.push(res.headers.location);
      })
      .connect({
        inapplicable: 'should be ignored'
      });
    stream.on('finish', () => {
      redirects.should.eql(['/movies', '/movies/all', '/movies/all/0']);
      fs.readFileSync(destinationPath, 'utf8').should.eql('first movie page');
      done();
    });
    request_.pipe(stream);
  });
});
```

## File: `test/node/pipe.js`
```javascript
'use strict';
const request = require('../support/client');
const express = require('../support/express');

const app = express();
const fs = require('fs');
const bodyParser = require('body-parser');
let http = require('http');
const zlib = require('zlib');
const { pipeline } = require('stream');

if (process.env.HTTP2_TEST) {
  http = require('http2');
}

app.use(bodyParser.json());

app.get('/', (request_, res) => {
  fs.createReadStream('test/node/fixtures/user.json').pipe(res);
});

app.get('/gzip', (request_, res) => {
  res.writeHead(200, {
    'Content-Encoding': 'gzip'
  });
  fs.createReadStream('test/node/fixtures/user.json').pipe(new zlib.createGzip()).pipe(res);
});

app.get('/redirect', (request_, res) => {
  res.set('Location', '/').sendStatus(302);
});

app.get('/badRedirectNoLocation', (request_, res) => {
  res.set('Location', '').sendStatus(302);
});

app.post('/', (request_, res) => {
  if (process.env.HTTP2_TEST) {
    // body-parser does not support http2 yet.
    // This section can be remove after body-parser supporting http2.
    res.set('content-type', 'application/json');
    request_.pipe(res);
  } else {
    res.send(request_.body);
  }
});

let base = 'http://localhost';
let server;
before(function listen(done) {
  server = http.createServer(app);
  server.listen(0, function listening() {
    base += `:${server.address().port}`;
    done();
  });
});

describe('request pipe', () => {
  const destinationPath = 'test/node/fixtures/tmp.json';

  after(function removeTmpfile(done) {
    fs.unlink(destinationPath, done);
  });

  it('should act as a writable stream', (done) => {
    const request_ = request.post(base);
    const stream = fs.createReadStream('test/node/fixtures/user.json');

    request_.type('json');

    request_.on('response', (res) => {
      res.body.should.eql({ name: 'tobi' });
      done();
    });

    stream.pipe(request_);
  });

  it('end() stops piping', (done) => {
    const stream = fs.createWriteStream(destinationPath);
    request.get(base).end((error, res) => {
      try {
        res.pipe(stream);
        return done(new Error('Did not prevent nonsense pipe'));
      } catch {
        /* expected error */
      }

      done();
    });
  });

  it('should act as a readable stream', (done) => {
    const stream = fs.createWriteStream(destinationPath);

    let responseCalled = false;
    const request_ = request.get(base);
    request_.type('json');

    request_.on('response', (res) => {
      res.status.should.eql(200);
      responseCalled = true;
    });
    stream.on('finish', () => {
      JSON.parse(fs.readFileSync(destinationPath)).should.eql({
        name: 'tobi'
      });
      responseCalled.should.be.true();
      done();
    });
    request_.pipe(stream);
  });

  it('should act as a readable stream with unzip', (done) => {
    const stream = fs.createWriteStream(destinationPath);

    let responseCalled = false;
    const request_ = request.get(base + '/gzip');
    request_.type('json');

    request_.on('response', (res) => {
      res.status.should.eql(200);
      responseCalled = true;
    });
    stream.on('finish', () => {
      JSON.parse(fs.readFileSync(destinationPath)).should.eql({
        name: 'tobi'
      });
      responseCalled.should.be.true();
      done();
    });
    request_.pipe(stream);
  });

  it('should act as a readable stream with unzip and node.stream.pipeline', (done) => {
    const stream = fs.createWriteStream(destinationPath);

    let responseCalled = false;
    const request_ = request.get(base + '/gzip');
    request_.type('json');

    request_.on('response', (res) => {
      res.status.should.eql(200);
      responseCalled = true;
    });
    // pipeline automatically ends streams by default.  Since unzipping introduces a transform stream that is
    // not monitored by pipeline, we need to make sure request_ does not emit 'end' until the unzip step
    // has finished writing data.  Otherwise, we'll either end up with truncated data or a 'write after end' error.
    pipeline(request_, stream, function (err) {
      (!!err).should.be.false();
      responseCalled.should.be.true();

      JSON.parse(fs.readFileSync(destinationPath)).should.eql({
        name: 'tobi'
      });
      done();
    });
  });

  it('should follow redirects', (done) => {
    const stream = fs.createWriteStream(destinationPath);

    let responseCalled = false;
    const request_ = request.get(base + '/redirect');
    request_.type('json');

    request_.on('response', (res) => {
      res.status.should.eql(200);
      responseCalled = true;
    });
    stream.on('finish', () => {
      JSON.parse(fs.readFileSync(destinationPath)).should.eql({
        name: 'tobi'
      });
      responseCalled.should.be.true();
      done();
    });
    request_.pipe(stream);
  });

  it('should not throw on bad redirects', (done) => {
    const stream = fs.createWriteStream(destinationPath);

    let responseCalled = false;
    let errorCalled = false;
    const request_ = request.get(base + '/badRedirectNoLocation');
    request_.type('json');

    request_.on('response', (res) => {
      responseCalled = true;
    });
    request_.on('error', (error) => {
      error.message.should.eql('No location header for redirect');
      errorCalled = true;
      stream.end();
    });
    stream.on('finish', () => {
      responseCalled.should.be.false();
      errorCalled.should.be.true();
      done();
    });
    request_.pipe(stream);
  });
});
```

## File: `test/node/query.js`
```javascript
'use strict';
let http = require('http');
const assert = require('assert');
const fs = require('fs');
const request = require('../support/client');
const express = require('../support/express');

const app = express();

if (process.env.HTTP2_TEST) {
  http = require('http2');
}

app.get('/raw-query', (request_, res) => {
  res.status(200).send(request_.url.slice(request_.url.indexOf('?') + 1));
});

app.get('/', (request_, res) => {
  res.status(200).send(request_.query);
});

app.delete('/url', (request_, res) => {
  res.status(200).send(request_.url);
});

app.delete('/', (request_, res) => {
  res.status(200).send(request_.query);
});

app.put('/', (request_, res) => {
  res.status(200).send(request_.query);
});

let base = 'http://localhost';
let server;
before(function listen(done) {
  server = http.createServer(app);
  server = server.listen(0, function listening() {
    base += `:${server.address().port}`;
    done();
  });
});

describe('req.query(String)', () => {
  // This is no longer true as of qs v3.0.0 (https://github.com/ljharb/qs/commit/0c6f2a6318c94f6226d3cf7fe36094e9685042b6)
  // it('should supply uri malformed error to the callback')

  it('should support passing in a string', (done) => {
    request
      .del(base)
      .query('name=t%F6bi')
      .end((error, res) => {
        res.body.should.eql({ name: 't%F6bi' });
        done();
      });
  });

  it('should work with url query-string and string for query', (done) => {
    request
      .del(`${base}/?name=tobi`)
      .query('age=2%20')
      .end((error, res) => {
        res.body.should.eql({ name: 'tobi', age: '2 ' });
        done();
      });
  });

  it('should support compound elements in a string', (done) => {
    request
      .del(base)
      .query('name=t%F6bi&age=2')
      .end((error, res) => {
        res.body.should.eql({ name: 't%F6bi', age: '2' });
        done();
      });
  });

  it('should work when called multiple times with a string', (done) => {
    request
      .del(base)
      .query('name=t%F6bi')
      .query('age=2%F6')
      .end((error, res) => {
        res.body.should.eql({ name: 't%F6bi', age: '2%F6' });
        done();
      });
  });

  it('should work with normal `query` object and query string', (done) => {
    request
      .del(base)
      .query('name=t%F6bi')
      .query({ age: '2' })
      .end((error, res) => {
        res.body.should.eql({ name: 't%F6bi', age: '2' });
        done();
      });
  });

  it('should not encode raw backticks, but leave encoded ones as is', () => {
    return Promise.all([
      request
        .get(`${base}/raw-query`)
        .query('name=`t%60bi`&age`=2')
        .then((res) => {
          res.text.should.eql('name=`t%60bi`&age`=2');
        }),

      request.get(base + '/raw-query?`age%60`=2%60`').then((res) => {
        res.text.should.eql('`age%60`=2%60`');
      }),

      request
        .get(`${base}/raw-query`)
        .query('name=`t%60bi`')
        .query('age`=2')
        .then((res) => {
          res.text.should.eql('name=`t%60bi`&age`=2');
        })
    ]);
  });
});

describe('req.query(Object)', () => {
  it('should construct the query-string', (done) => {
    request
      .del(base)
      .query({ name: 'tobi' })
      .query({ order: 'asc' })
      .query({ limit: ['1', '2'] })
      .end((error, res) => {
        res.body.should.eql({ name: 'tobi', order: 'asc', limit: ['1', '2'] });
        done();
      });
  });

  // See commit message for the reasoning here.
  it('should encode raw backticks', (done) => {
    request
      .get(`${base}/raw-query`)
      .query({ name: '`tobi`' })
      .query({ 'orde%60r': null })
      .query({ '`limit`': ['%602`'] })
      .end((error, res) => {
        res.text.should.eql('name=%60tobi%60&orde%2560r&%60limit%60=%25602%60');
        done();
      });
  });

  it('should not error on dates', (done) => {
    const date = new Date(0);

    request
      .del(base)
      .query({ at: date })
      .end((error, res) => {
        assert.equal(date.toISOString(), res.body.at);
        done();
      });
  });

  it('should work after setting header fields', (done) => {
    request
      .del(base)
      .set('Foo', 'bar')
      .set('Bar', 'baz')
      .query({ name: 'tobi' })
      .query({ order: 'asc' })
      .query({ limit: ['1', '2'] })
      .end((error, res) => {
        res.body.should.eql({ name: 'tobi', order: 'asc', limit: ['1', '2'] });
        done();
      });
  });

  it('should append to the original query-string', (done) => {
    request
      .del(`${base}/?name=tobi`)
      .query({ order: 'asc' })
      .end((error, res) => {
        res.body.should.eql({ name: 'tobi', order: 'asc' });
        done();
      });
  });

  it('should retain the original query-string', (done) => {
    request.del(`${base}/?name=tobi`).end((error, res) => {
      res.body.should.eql({ name: 'tobi' });
      done();
    });
  });

  it('should keep only keys with null querystring values', (done) => {
    request
      .del(`${base}/url`)
      .query({ nil: null })
      .end((error, res) => {
        res.text.should.equal('/url?nil');
        done();
      });
  });

  it('query-string should be sent on pipe', (done) => {
    const request_ = request.put(`${base}/?name=tobi`);
    const stream = fs.createReadStream('test/node/fixtures/user.json');

    request_.on('response', (res) => {
      res.body.should.eql({ name: 'tobi' });
      done();
    });
    request_.on('error', (err) => {
      done(err);
    });

    stream.on('error', (err) => {
      done(err);
    });

    // wait until stream is valid before piping
    stream.on('open', () => {
      // wait until request_ is ready before piping
      setTimeout(() => {
        stream.pipe(request_);
      }, 10);
    });
  });
});
```

## File: `test/node/redirects-other-host.js`
```javascript
'use strict';
const assert = require('assert');
const request = require('../support/client');
const express = require('../support/express');

const app = express();
const app2 = express();
const should = require('should');
let http = require('http');

if (process.env.HTTP2_TEST) {
  http = require('http2');
}

let base = 'http://localhost';
let server;
before(function listen(done) {
  server = http.createServer(app);
  server = server.listen(0, function listening() {
    base += `:${server.address().port}`;
    done();
  });
});

let base2 = 'http://localhost';
let server2;
before(function listen(done) {
  server2 = http.createServer(app2);
  server2 = server2.listen(0, function listening() {
    base2 += `:${server2.address().port}`;
    done();
  });
});

app.all('/test-301', (request_, res) => {
  res.redirect(301, `${base2}/`);
});
app.all('/test-302', (request_, res) => {
  res.redirect(302, `${base2}/`);
});
app.all('/test-303', (request_, res) => {
  res.redirect(303, `${base2}/`);
});
app.all('/test-307', (request_, res) => {
  res.redirect(307, `${base2}/`);
});
app.all('/test-308', (request_, res) => {
  res.redirect(308, `${base2}/`);
});

app2.all('/', (request_, res) => {
  res.send(request_.method);
});

describe('request.get', () => {
  describe('on 301 redirect', () => {
    it('should follow Location with a GET request', (done) => {
      const request_ = request.get(`${base}/test-301`).redirects(1);
      request_.end((error, res) => {
        const headers = request_.req.getHeaders
          ? request_.req.getHeaders()
          : request_.req._headers;
        headers.host.should.eql(`localhost:${server2.address().port}`);
        res.status.should.eql(200);
        res.text.should.eql('GET');
        done();
      });
    });
  });
  describe('on 302 redirect', () => {
    it('should follow Location with a GET request', (done) => {
      const request_ = request.get(`${base}/test-302`).redirects(1);
      request_.end((error, res) => {
        const headers = request_.req.getHeaders
          ? request_.req.getHeaders()
          : request_.req._headers;
        res.status.should.eql(200);
        res.text.should.eql('GET');
        done();
      });
    });
  });
  describe('on 303 redirect', () => {
    it('should follow Location with a GET request', (done) => {
      const request_ = request.get(`${base}/test-303`).redirects(1);
      request_.end((error, res) => {
        const headers = request_.req.getHeaders
          ? request_.req.getHeaders()
          : request_.req._headers;
        headers.host.should.eql(`localhost:${server2.address().port}`);
        res.status.should.eql(200);
        res.text.should.eql('GET');
        done();
      });
    });
  });
  describe('on 307 redirect', () => {
    it('should follow Location with a GET request', (done) => {
      const request_ = request.get(`${base}/test-307`).redirects(1);
      request_.end((error, res) => {
        const headers = request_.req.getHeaders
          ? request_.req.getHeaders()
          : request_.req._headers;
        headers.host.should.eql(`localhost:${server2.address().port}`);
        res.status.should.eql(200);
        res.text.should.eql('GET');
        done();
      });
    });
  });
  describe('on 308 redirect', () => {
    it('should follow Location with a GET request', (done) => {
      const request_ = request.get(`${base}/test-308`).redirects(1);
      request_.end((error, res) => {
        const headers = request_.req.getHeaders
          ? request_.req.getHeaders()
          : request_.req._headers;
        headers.host.should.eql(`localhost:${server2.address().port}`);
        res.status.should.eql(200);
        res.text.should.eql('GET');
        done();
      });
    });
  });
});

describe('request.post', () => {
  describe('on 301 redirect', () => {
    it('should follow Location with a GET request', (done) => {
      const request_ = request.post(`${base}/test-301`).redirects(1);
      request_.end((error, res) => {
        const headers = request_.req.getHeaders
          ? request_.req.getHeaders()
          : request_.req._headers;
        headers.host.should.eql(`localhost:${server2.address().port}`);
        res.status.should.eql(200);
        res.text.should.eql('GET');
        done();
      });
    });
  });
  describe('on 302 redirect', () => {
    it('should follow Location with a GET request', (done) => {
      const request_ = request.post(`${base}/test-302`).redirects(1);
      request_.end((error, res) => {
        const headers = request_.req.getHeaders
          ? request_.req.getHeaders()
          : request_.req._headers;
        headers.host.should.eql(`localhost:${server2.address().port}`);
        res.status.should.eql(200);
        res.text.should.eql('GET');
        done();
      });
    });
  });
  describe('on 303 redirect', () => {
    it('should follow Location with a GET request', (done) => {
      const request_ = request.post(`${base}/test-303`).redirects(1);
      request_.end((error, res) => {
        const headers = request_.req.getHeaders
          ? request_.req.getHeaders()
          : request_.req._headers;
        headers.host.should.eql(`localhost:${server2.address().port}`);
        res.status.should.eql(200);
        res.text.should.eql('GET');
        done();
      });
    });
  });
  describe('on 307 redirect', () => {
    it('should follow Location with a POST request', (done) => {
      const request_ = request.post(`${base}/test-307`).redirects(1);
      request_.end((error, res) => {
        const headers = request_.req.getHeaders
          ? request_.req.getHeaders()
          : request_.req._headers;
        headers.host.should.eql(`localhost:${server2.address().port}`);
        res.status.should.eql(200);
        res.text.should.eql('POST');
        done();
      });
    });
  });
  describe('on 308 redirect', () => {
    it('should follow Location with a POST request', (done) => {
      const request_ = request.post(`${base}/test-308`).redirects(1);
      request_.end((error, res) => {
        const headers = request_.req.getHeaders
          ? request_.req.getHeaders()
          : request_.req._headers;
        headers.host.should.eql(`localhost:${server2.address().port}`);
        res.status.should.eql(200);
        res.text.should.eql('POST');
        done();
      });
    });
  });
});
```

## File: `test/node/redirects.js`
```javascript
'use strict';

const assert = require('assert');
const getSetup = require('../support/setup');
const request = require('../support/client');

describe('request', () => {
  let setup;
  let base;

  before(async () => {
    setup = await getSetup();
    base = setup.uri;
  });

  describe('on redirect', () => {
    it('should merge cookies if agent is used', (done) => {
      request
        .agent()
        .get(`${base}/cookie-redirect`)
        .set('Cookie', 'orig=1; replaced=not')
        .end((error, res) => {
          try {
            assert.ifError(error);
            assert(/orig=1/.test(res.text), 'orig=1/.test');
            assert(/replaced=yes/.test(res.text), 'replaced=yes/.test');
            assert(/from-redir=1/.test(res.text), 'from-redir=1');
            done();
          } catch (err) {
            done(err);
          }
        });
    });

    it('should not merge cookies if agent is not used', (done) => {
      request
        .get(`${base}/cookie-redirect`)
        .set('Cookie', 'orig=1; replaced=not')
        .end((error, res) => {
          try {
            assert.ifError(error);
            assert(/orig=1/.test(res.text), '/orig=1');
            assert(/replaced=not/.test(res.text), '/replaced=not');
            assert(!/replaced=yes/.test(res.text), '!/replaced=yes');
            assert(!/from-redir/.test(res.text), '!/from-redir');
            done();
          } catch (err) {
            done(err);
          }
        });
    });

    it('should have previously set cookie for subsquent requests when agent is used', (done) => {
      const agent = request.agent();
      agent.get(`${base}/set-cookie`).end((error) => {
        assert.ifError(error);
        agent
          .get(`${base}/show-cookies`)
          .set({ Cookie: 'orig=1' })
          .end((error, res) => {
            try {
              assert.ifError(error);
              assert(/orig=1/.test(res.text), 'orig=1/.test');
              assert(/persist=123/.test(res.text), 'persist=123');
              done();
            } catch (err) {
              done(err);
            }
          });
      });
    });

    it('should overwrite previously set cookie during a redirect when agent is used', (done) => {
      const agent = request.agent();
      agent.get(`${base}/set-cookie`).end((error) => {
        assert.ifError(error);
        agent
          .get(`${base}/cookie-redirect`)
          .redirects(1)
          .end((error, res) => {
            try {
              assert.ifError(error);
              assert(/replaced=yes/.test(res.text), 'replaced=yes');
              done();
            } catch (err) {
              done(err);
            }
          });
      });
    })

    it('should follow Location', (done) => {
      const redirects = [];

      request
        .get(base)
        .on('redirect', (res) => {
          redirects.push(res.headers.location);
        })
        .end((error, res) => {
          try {
            const array = ['/movies', '/movies/all', '/movies/all/0'];
            redirects.should.eql(array);
            res.text.should.equal('first movie page');
            done();
          } catch (err) {
            done(err);
          }
        });
    });

    it('should follow Location with IP override', () => {
      const redirects = [];
      const url = new URL(base);
      return request
        .get(`http://redir.example.com:${url.port || '80'}${url.pathname}`)
        .connect({
          '*': url.hostname
        })
        .on('redirect', (res) => {
          redirects.push(res.headers.location);
        })
        .then((res) => {
          const array = ['/movies', '/movies/all', '/movies/all/0'];
          redirects.should.eql(array);
          res.text.should.equal('first movie page');
        });
    });

    it('should follow Location with IP:port override', () => {
      const redirects = [];
      const url = new URL(base);
      return request
        .get(`http://redir.example.com:9999${url.pathname}`)
        .connect({
          '*': { host: url.hostname, port: url.port || 80 }
        })
        .on('redirect', (res) => {
          redirects.push(res.headers.location);
        })
        .then((res) => {
          const array = ['/movies', '/movies/all', '/movies/all/0'];
          redirects.should.eql(array);
          res.text.should.equal('first movie page');
        });
    });

    it('should not follow on HEAD by default', () => {
      const redirects = [];

      return request
        .head(base)
        .ok(() => true)
        .on('redirect', (res) => {
          redirects.push(res.headers.location);
        })
        .then((res) => {
          redirects.should.eql([]);
          res.status.should.equal(302);
        });
    });

    it('should follow on HEAD when redirects are set', (done) => {
      const redirects = [];

      request
        .head(base)
        .redirects(10)
        .on('redirect', (res) => {
          redirects.push(res.headers.location);
        })
        .end((error, res) => {
          try {
            const array = [];
            array.push('/movies', '/movies/all', '/movies/all/0');
            redirects.should.eql(array);
            assert(!res.text);
            done();
          } catch (err) {
            done(err);
          }
        });
    });

    it('should remove Content-* fields', (done) => {
      request
        .post(`${base}/header`)
        .type('txt')
        .set('X-Foo', 'bar')
        .set('X-Bar', 'baz')
        .send('hey')
        .end((error, res) => {
          try {
            assert(res.body);
            res.body.should.have.property('x-foo', 'bar');
            res.body.should.have.property('x-bar', 'baz');
            res.body.should.not.have.property('content-type');
            res.body.should.not.have.property('content-length');
            res.body.should.not.have.property('transfer-encoding');
            done();
          } catch (err) {
            done(err);
          }
        });
    });

    it('should retain cookies', (done) => {
      request
        .get(`${base}/header`)
        .set('Cookie', 'foo=bar;')
        .end((error, res) => {
          try {
            assert(res.body);
            res.body.should.have.property('cookie', 'foo=bar;');
            done();
          } catch (err) {
            done(err);
          }
        });
    });

    it('should not resend query parameters', (done) => {
      const redirects = [];
      const query = [];

      request
        .get(`${base}/?foo=bar`)
        .on('redirect', (res) => {
          query.push(res.headers.query);
          redirects.push(res.headers.location);
        })
        .end((error, res) => {
          try {
            const array = [];
            array.push('/movies', '/movies/all', '/movies/all/0');
            redirects.should.eql(array);
            res.text.should.equal('first movie page');

            query.should.eql(['{"foo":"bar"}', '{}', '{}']);
            res.headers.query.should.eql('{}');
            done();
          } catch (err) {
            done(err);
          }
        });
    });

    it('should handle no location header', (done) => {
      request.get(`${base}/bad-redirect`).end((error, res) => {
        try {
          error.message.should.equal('No location header for redirect');
          done();
        } catch (err) {
          done(err);
        }
      });
    });

    describe('when relative', () => {
      it('should redirect to a sibling path', (done) => {
        const redirects = [];

        request
          .get(`${base}/relative`)
          .on('redirect', (res) => {
            redirects.push(res.headers.location);
          })
          .end((error, res) => {
            try {
              redirects.should.eql(['tobi']);
              res.text.should.equal('tobi');
              done();
            } catch (err) {
              done(err);
            }
          });
      });

      it('should redirect to a parent path', (done) => {
        const redirects = [];

        request
          .get(`${base}/relative/sub`)
          .on('redirect', (res) => {
            redirects.push(res.headers.location);
          })
          .end((error, res) => {
            try {
              redirects.should.eql(['../tobi']);
              res.text.should.equal('tobi');
              done();
            } catch (err) {
              done(err);
            }
          });
      });
    });
  });

  describe('req.redirects(n)', () => {
    it('should alter the default number of redirects to follow', (done) => {
      const redirects = [];

      request
        .get(base)
        .redirects(2)
        .on('redirect', (res) => {
          redirects.push(res.headers.location);
        })
        .end((error, res) => {
          try {
            const array = [];
            assert(res.redirect, 'res.redirect');
            array.push('/movies', '/movies/all');
            redirects.should.eql(array);
            res.text.should.match(/Moved Temporarily|Found/);
            done();
          } catch (err) {
            done(err);
          }
        });
    });
  });

  describe('on POST', () => {
    it('should redirect as GET', () => {
      const redirects = [];

      return request
        .post(`${base}/movie`)
        .send({ name: 'Tobi' })
        .redirects(2)
        .on('redirect', (res) => {
          redirects.push(res.headers.location);
        })
        .then((res) => {
          redirects.should.eql(['/movies/all/0']);
          res.text.should.equal('first movie page');
        });
    });

    it('using multipart/form-data should redirect as GET', () => {
      const redirects = [];

      request
        .post(`${base}/movie`)
        .type('form')
        .field('name', 'Tobi')
        .redirects(2)
        .on('redirect', (res) => {
          redirects.push(res.headers.location);
        })
        .then((res) => {
          redirects.should.eql(['/movies/all/0']);
          res.text.should.equal('first movie page');
        });
    });
  });
});
```

## File: `test/node/response-readable-stream.js`
```javascript
'use strict';
const request = require('../support/client');
const express = require('../support/express');

const app = express();
const fs = require('fs');
let http = require('http');

if (process.env.HTTP2_TEST) {
  http = require('http2');
}

app.get('/', (request_, res) => {
  fs.createReadStream('test/node/fixtures/user.json').pipe(res);
});

let base = 'http://localhost';
let server;
before(function listen(done) {
  server = http.createServer(app);
  server = server.listen(0, function listening() {
    base += `:${server.address().port}`;
    done();
  });
});

describe('response', () => {
  it('should act as a readable stream', (done) => {
    const request_ = request.get(base).buffer(false);

    request_.end((error, res) => {
      if (error) return done(error);
      let trackEndEvent = 0;
      let trackCloseEvent = 0;

      res.on('end', () => {
        trackEndEvent++;
        trackEndEvent.should.equal(1);
        if (!process.env.HTTP2_TEST) {
          trackCloseEvent.should.equal(0); // close should not have been called
        }

        done();
      });

      res.on('close', () => {
        trackCloseEvent++;
      });

      setTimeout(() => {
        (() => {
          res.pause();
        }).should.not.throw();
        (() => {
          res.resume();
        }).should.not.throw();
        (() => {
          res.destroy();
        }).should.not.throw();
      }, 50);
    });
  });
});
```

## File: `test/node/serialize.js`
```javascript
'use strict';

const assert = require('assert');
const request = require('../support/client');
const getSetup = require('../support/setup');

describe('req.serialize(fn)', () => {
  let setup;
  let base;

  before(async () => {
    setup = await getSetup();
    base = setup.uri;
  });

  it('should take precedence over default parsers', (done) => {
    request
      .post(`${base}/echo`)
      .send({ foo: 123 })
      .serialize(() => '{"bar":456}')
      .end((error, res) => {
        assert.ifError(error);
        assert.equal('{"bar":456}', res.text);
        assert.equal(456, res.body.bar);
        done();
      });
  });
});
```

## File: `test/node/set-host.js`
```javascript
'use strict';
const request = require('../support/client');
const express = require('../support/express');

const app = express();
const http = require('http');
const assert = require('assert');

describe('request.get().set()', () => {
  if (process.env.HTTP2_TEST) {
    return; // request object doesn't look the same
  }

  let server;

  after(function exitServer() {
    if (typeof server.close === 'function') {
      server.close();
    } else {
      server.destroy();
    }
  });

  it('should set host header after get()', (done) => {
    app.get('/', (request_, res) => {
      assert.equal(request_.hostname, 'example.com');
      res.end();
    });

    server = http.createServer(app);
    server.listen(0, function listening() {
      request
        .get(`http://localhost:${server.address().port}`)
        .set('host', 'example.com')
        .then(() => {
          return request
            .get(`http://example.com:${server.address().port}`)
            .connect({
              'example.com': 'localhost',
              '*': 'fail'
            });
        })
        .then(() => done(), done);
    });
  });
});
```

## File: `test/node/toError.js`
```javascript
'use strict';
const assert = require('assert');
const request = require('../support/client');
const express = require('../support/express');

const app = express();
let http = require('http');

if (process.env.HTTP2_TEST) {
  http = require('http2');
}

app.get('/', (request_, res) => {
  res.status(400).send('invalid json');
});

let base = 'http://localhost';
let server;
before(function listen(done) {
  server = http.createServer(app);
  server = server.listen(0, function listening() {
    base += `:${server.address().port}`;
    done();
  });
});

describe('res.toError()', () => {
  it('should return an Error', (done) => {
    request.get(base).end((err, res) => {
      const error = res.toError();
      assert.equal(error.status, 400);
      assert.equal(error.method, 'GET');
      assert.equal(error.path, '/');
      assert.equal(error.message, 'cannot GET / (400)');
      assert.equal(error.text, 'invalid json');
      done();
    });
  });
});
```

## File: `test/node/unix-sockets.js`
```javascript
'use strict';
const assert = require('assert');

let http = require('http');
let https = require('https');
const os = require('os');
const fs = require('fs');
const express = require('../support/express');
const request = require('../support/client');

const app = express();

const key = fs.readFileSync(`${__dirname}/fixtures/key.pem`);
const cert = fs.readFileSync(`${__dirname}/fixtures/cert.pem`);
const cacert = fs.readFileSync(`${__dirname}/fixtures/ca.cert.pem`);
const httpSockPath = [os.tmpdir(), 'superagent-http.sock'].join('/');
const httpsSockPath = [os.tmpdir(), 'superagent-https.sock'].join('/');
let httpServer;
let httpsServer;

if (process.env.HTTP2_TEST) {
  http = https = require('http2');
}

app.get('/', (request_, res) => {
  res.send('root ok!');
});

app.get('/request/path', (request_, res) => {
  res.send('request path ok!');
});

describe('[unix-sockets] http', () => {
  if (process.platform === 'win32') {
    return;
  }

  before((done) => {
    if (fs.existsSync(httpSockPath) === true) {
      // try unlink if sock file exists
      fs.unlinkSync(httpSockPath);
    }

    httpServer = http.createServer(app);
    httpServer.listen(httpSockPath, done);
  });

  const base = `http+unix://${httpSockPath.replace(/\//g, '%2F')}`;

  describe('request', () => {
    it('path: / (root)', (done) => {
      request.get(`${base}/`).end((error, res) => {
        assert(res.ok);
        assert.strictEqual('root ok!', res.text);
        done();
      });
    });

    it('path: /request/path', (done) => {
      request.get(`${base}/request/path`).end((error, res) => {
        assert(res.ok);
        assert.strictEqual('request path ok!', res.text);
        done();
      });
    });
  });

  after(() => {
    if (typeof httpServer.close === 'function') {
      httpServer.close();
    } else httpServer.destroy();
  });
});

describe('[unix-sockets] https', () => {
  if (process.platform === 'win32') {
    return;
  }

  before((done) => {
    if (fs.existsSync(httpsSockPath) === true) {
      // try unlink if sock file exists
      fs.unlinkSync(httpsSockPath);
    }

    httpsServer = process.env.HTTP2_TEST
      ? https.createSecureServer({ key, cert }, app)
      : https.createServer({ key, cert }, app);

    httpsServer.listen(httpsSockPath, done);
  });

  const base = `https+unix://${httpsSockPath.replace(/\//g, '%2F')}`;

  describe('request', () => {
    it('path: / (root)', (done) => {
      request
        .get(`${base}/`)
        .ca(cacert)
        .end((error, res) => {
          assert.ifError(error);
          assert(res.ok);
          assert.strictEqual('root ok!', res.text);
          done();
        });
    });

    it('path: /request/path', (done) => {
      request
        .get(`${base}/request/path`)
        .ca(cacert)
        .end((error, res) => {
          assert.ifError(error);
          assert(res.ok);
          assert.strictEqual('request path ok!', res.text);
          done();
        });
    });
  });

  after((done) => {
    httpsServer.close(done);
  });
});
```

## File: `test/node/user-agent.js`
```javascript
'use strict';
const assert = require('assert');
const request = require('../support/client');
const getSetup = require('../support/setup');

describe('req.get()', () => {
  let setup;
  let base;

  before(async () => {
    setup = await getSetup();
    base = setup.uri;
  });

  it('should not set a default user-agent', () =>
    request.get(`${base}/ua`).then((res) => {
      assert(res.headers);
      assert(!res.headers['user-agent']);
    }));
});
```

## File: `test/node/utils.js`
```javascript
'use strict';
const assert = require('assert');
const utils =
  process.env.OLD_NODE_TEST === '1'
    ? // eslint-disable-next-line node/no-missing-require
      require('../../../utils')
    : require('../../lib/utils');

describe('utils.type(str)', () => {
  it('should return the mime type', () => {
    utils
      .type('application/json; charset=utf-8')
      .should.equal('application/json');

    utils.type('application/json').should.equal('application/json');
  });
});

describe('utils.params(str)', () => {
  it('should return the field parameters', () => {
    const object = utils.params('application/json; charset=utf-8; foo  = bar');
    object.charset.should.equal('utf-8');
    object.foo.should.equal('bar');

    utils.params('application/json').should.eql({});
  });
});

describe('utils.parseLinks(str)', () => {
  it('should parse links', () => {
    const string_ =
      '<https://api.github.com/repos/visionmedia/mocha/issues?page=2>; rel="next", <https://api.github.com/repos/visionmedia/mocha/issues?page=5>; rel="last"';
    const returnValue = utils.parseLinks(string_);
    returnValue.next.should.equal(
      'https://api.github.com/repos/visionmedia/mocha/issues?page=2'
    );
    returnValue.last.should.equal(
      'https://api.github.com/repos/visionmedia/mocha/issues?page=5'
    );
  });
});

describe('utils.isGzipOrDeflateEncoding(res)', () => {
  it('should return true when content encoding is gzip', () => {
    utils.isGzipOrDeflateEncoding({
      headers: {
        'content-encoding': 'gzip',
      },
    }).should.equal(true);
  });
  it('should return true when content encoding is deflate', () => {
    utils.isGzipOrDeflateEncoding({
      headers: {
        'content-encoding': 'deflate',
      },
    }).should.equal(true);
  });
  it('should return false when content encoding is bla', () => {
    utils.isGzipOrDeflateEncoding({
      headers: {
        'content-encoding': 'bla',
      },
    }).should.equal(false);
  });
  
  it('should return true when content encoding has a lot of spaces followed with gzip', () => {
    utils.isGzipOrDeflateEncoding({
      headers: {
        'content-encoding': " " * 10**6 + " gzip",
      },
    }).should.equal(false);
  });
  
  it('should return true when content encoding repeates it self', () => {
    utils.isGzipOrDeflateEncoding({
      headers: {
        'content-encoding': "gzip deflate gzip deflate gzip deflate gzip deflate gzip deflate gzip deflate gzip deflate gzip deflate",
      },
    }).should.equal(false);
  });
  
  it('should return true when content encoding repeates it self wuth a lot of spaces', () => {
    utils.isGzipOrDeflateEncoding({
      headers: {
        'content-encoding': " gzip   deflate   gzip   deflate   gzip   deflate   gzip   deflate   gzip   deflate   gzip   deflate",
      },
    }).should.equal(false);
  });
  
  it('should return true when content encoding - nested patterns', () => {
    utils.isGzipOrDeflateEncoding({
      headers: {
        'content-encoding': " " * 10**5 + ("gzip deflate " * 1000)
      },
    }).should.equal(false);
  });

  
});

describe('utils.isBrotliEncoding(res)', () => {
  it('should return true when content encoding is br', () => {
    utils.isBrotliEncoding({
      headers: {
        'content-encoding': 'br',
      },
    }).should.equal(true);
  });
  it('should return false when content encoding is bla', () => {
    utils.isBrotliEncoding({
      headers: {
        'content-encoding': 'bla',
      },
    }).should.equal(false);
  });
  
  it('should return true when content encoding has a lot of spaces followed with br', () => {
    utils.isBrotliEncoding({
      headers: {
        'content-encoding': " " * 10**6 + " br",
      },
    }).should.equal(false);
  });
  
  it('should return true when content encoding repeates it self', () => {
    utils.isBrotliEncoding({
      headers: {
        'content-encoding': " br br br br br  br br br br br  br br br br br br br br br br  br br br br br  br br br br br",
      },
    }).should.equal(false);
  });
  
  it('should return true when content encoding repeates it self wuth a lot of spaces', () => {
    utils.isBrotliEncoding({
      headers: {
        'content-encoding': "br     br     br     br     br     br     br     br     br     br     br     br     br     br",
      },
    }).should.equal(false);
  });
  
  it('should return true when content encoding - nested patterns', () => {
    utils.isBrotliEncoding({
      headers: {
        'content-encoding': " " * 10**5 + ("br " * 1000)
      },
    }).should.equal(false);
  });
  
});
```

## File: `test/node/fixtures/ca.cert.pem`
```
-----BEGIN CERTIFICATE-----
MIICljCCAX4CCQDnGz3+qH/zGzANBgkqhkiG9w0BAQsFADANMQswCQYDVQQDDAJD
QTAeFw0xODEyMDIxNjIyMThaFw0zMjA4MTAxNjIyMThaMA0xCzAJBgNVBAMMAkNB
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtgUDcB7R94A22I0D8Iba
c000ZBINtvnyvoPP5U2hRsxI9tcW/LLm0GhzM5XJJNQ0jSv0ixIFKomtFBSjKMq/
NH156SqKqyDGU1fPnGjzcJulxceODIokAqNCbZ7Bys6nqUdilNfLQ4bBBWYsEUWT
vgbUeDRHvQGycou/pLpYGLCJ4tpc4n6ybox1uPi0qlvFI7aWvQFjOxxR0VeRixXf
qXjVCDIr9OJIWiXLrJYDlYqG2gRF/yTDZ4qmQxbZzJ6AXMpaRUiHUO0FHu7baEux
ylIc0KVcAmYMGdhFlmDrMNRsmnADKPX9DIMh92XWyE10oNK50I1rIhpvN4XfQx6E
UwIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQCIXj1vfTVRB4ea/udjazPHaLAeocbg
d8babbDItOm1ApAoUhNuxPVxyISSFrowCVlaWxB+1ztfeUAB/Axfj0mbXk1hgo2D
4+rft8hOtdg91bU+gHPd/7QGkpPIs5PC+TsnVj0mNqZ5o8qZsLhgoXp3Dl5yMhEs
sRegLkmBQHzEsKFU2cSxVD7BXXGLDJxcoR4friGOXdIZeYwqHTZsuR3O7JOVbLew
dURqD70jPuf9v1tBnkJPbUECMlL7BCw6ZQtglSvjPP/waWir9TMsDk+xwPK8NPbv
DGi+w++cImBbxcnIMBTk4XtlFcOnCCAYUfkaxZMw2jNhYbjiEZOGUG8m
-----END CERTIFICATE-----
```

## File: `test/node/fixtures/ca.key.pem`
```
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAtgUDcB7R94A22I0D8Ibac000ZBINtvnyvoPP5U2hRsxI9tcW
/LLm0GhzM5XJJNQ0jSv0ixIFKomtFBSjKMq/NH156SqKqyDGU1fPnGjzcJulxceO
DIokAqNCbZ7Bys6nqUdilNfLQ4bBBWYsEUWTvgbUeDRHvQGycou/pLpYGLCJ4tpc
4n6ybox1uPi0qlvFI7aWvQFjOxxR0VeRixXfqXjVCDIr9OJIWiXLrJYDlYqG2gRF
/yTDZ4qmQxbZzJ6AXMpaRUiHUO0FHu7baEuxylIc0KVcAmYMGdhFlmDrMNRsmnAD
KPX9DIMh92XWyE10oNK50I1rIhpvN4XfQx6EUwIDAQABAoIBAAomAWkQ7tgD2Ar+
4cdZXXisR02FDCq1iOlCZCb+yw0teqv4lhmEyAW6rSGlKk/ZXQy59KqEWLFkd7f0
5pvxofOFQ3TSoGSmMSiYbsTjvR78LqP2Wl8snJFhFOUTwu5R01tG1aJC3dxn+P8a
ET7tSC2CJ/qDv7Q0EgT88bR3h03pAc2PJAGWJ2QwutAwV+6Ilyt3hcz29f7JGQac
Da0jY/7RIpvZL20gsecb/6Q0a50VEbkuJ+OF5QyIQNT9qtfvsqavtsjHgBWs3iFG
yKaDCey4X7D+NsyJBKNCuDqWXzq/4+mQ3atBIvYq2mcIpIbaku7TEWHvpxfzsT/F
SzLncMECgYEA4qR1GU38UxZ/8x6Cc4Z3DKUuCLBqvv69IHPcfSkhrtTeApdsv14U
KE66/Z3g4FXeV018GYUzGODfjBt4VnDCutz9tmiHFH+T2zDpgC7hvODC8rJ+D21b
G3Q5eyA+XRao1XHjc2UD/Ev6iJPjgCT23Lur2bhAqCKkV4g2EAWCgyMCgYEAzZjY
5M7Jw+0g5b6ILnFX66JbESrw87OtiIpiQh5XUQssKsmfONzbXUp6ch/MRTFVHVDZ
XmG35Xyg6vy1FYg9HTALl1tnkh9UIhKrH7jx+6euhc0HyWCCqSp/3CpJqVjdoxtS
vtZigSaxwTDaOYc8r54cWhHIIrpTrcqY4mxdZRECgYBpGWhv9pkXEqz82d4Wonlc
dNDXGLA3p7uea/wIUmWbRH07aGr2hzMDyhaue2MHxOoZRAZTc1BRrh4cQ7TXKO00
aDyDNQ/G8q5nC9SMK7FkvDnK//izQLvqDEiHj1k8I8DhUjHulh52BenFIgdyqjGM
BL9ZdDcPgRkCuliPr25pTwKBgG8rf9QxEJ51oT05Sk+6j+zk7FMbIhDUjjfvg/P2
jgZPgUFdpk/L9H28YPtGwGCFrV1dszu6oQJg4m5N2OjcsxcOPKZKEXXMpOSLraZI
jegiolbNJ7G3Es/AIET/RLdiSu4APzzblYX6U1GARe+ndaQMXY5CYTKOB+NIUmTU
bafRAoGAV8PptnjWf9ehJvt96Rz0FdfpN7leqdweK2JrGZwJQ9BRcKwUO758lmyN
nC62Sd0mwHivxRqI6e2u7OSvGj9e7iLnHMl4qYie7VvsWAWmztH2ntEI0iWA3V3N
M3T9+sz+nslfhWKgIA80EqOWB1AF0EmbmmqK0igWEbYynAr6v0Q=
-----END RSA PRIVATE KEY-----
```

## File: `test/node/fixtures/ca.srl`
```
B23299143E26EFC5
```

## File: `test/node/fixtures/cert.csr`
```
-----BEGIN CERTIFICATE REQUEST-----
MIICWTCCAUECAQAwFDESMBAGA1UEAwwJbG9jYWxob3N0MIIBIjANBgkqhkiG9w0B
AQEFAAOCAQ8AMIIBCgKCAQEAsjNYMUk1HzBLM4fL/8c6Z86X/b13V1bMXrrcV28w
jmvQv4lADlghZGt/zbinyvZrASp8v1btR9gLaNTdrxxnz5FWu1bY947ljgadudh0
STLNs4jWI2wcjgguA8B2rDtvap0bn9JkpjQGcFuqEdJRlr26OwsC5SNCtFxQmTrb
sneFMWK3JsL1riCrV9Cw0L3joki/YKYTTwRZJ2TXrrHvOLQCIUacwCU4oJg19D0F
KU/rDtdUFFojnTio0RFU4/OpjxKzwqjSJE80nPSRHAqXtSgmphrRk4ZVeTxKEGKC
oAt/RBwqvxPFjNlbr1EWY9S7SpFu06V35jXJYD9CWD/WcQIDAQABoAAwDQYJKoZI
hvcNAQELBQADggEBACia2hDAe1YqzVn/P2KSX+/9yDrjOhU20hKF1CTZr3Zfjep9
R86ldz1aFc2N2yqDjUYpj0+DODEXlEfNaYcD2nn93qgy/gAmfQUvCejBh6vsGiIW
qc41lzEGHa9/ErxQ7yvETeuY8OozjDAoUs5NUbFL6OmwJFqX9VzLbQ8uQxNU3z3l
AKVkWBWIubqpSa8tDn/+wf8vW/xtOCZ/Zd5YBQdTCwb5BdS3vpBkwpJbPBvR97Mc
2d+2a5qyNqZdb1CuATS2MJC35zp62FErhcnnVqtaAcaE/C/in1OO3wLJvXa5/LKp
1riBUJLHscGbIhe+KjlLoosXuOcUNvBkNbt8MFQ=
-----END CERTIFICATE REQUEST-----
```

## File: `test/node/fixtures/cert.pem`
```
-----BEGIN CERTIFICATE-----
MIICnTCCAYUCCQCyMpkUPibvxTANBgkqhkiG9w0BAQsFADANMQswCQYDVQQDDAJD
QTAeFw0xODEyMDIxNjIzNTBaFw0zMjA4MTAxNjIzNTBaMBQxEjAQBgNVBAMMCWxv
Y2FsaG9zdDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALIzWDFJNR8w
SzOHy//HOmfOl/29d1dWzF663FdvMI5r0L+JQA5YIWRrf824p8r2awEqfL9W7UfY
C2jU3a8cZ8+RVrtW2PeO5Y4GnbnYdEkyzbOI1iNsHI4ILgPAdqw7b2qdG5/SZKY0
BnBbqhHSUZa9ujsLAuUjQrRcUJk627J3hTFitybC9a4gq1fQsNC946JIv2CmE08E
WSdk166x7zi0AiFGnMAlOKCYNfQ9BSlP6w7XVBRaI504qNERVOPzqY8Ss8Ko0iRP
NJz0kRwKl7UoJqYa0ZOGVXk8ShBigqALf0QcKr8TxYzZW69RFmPUu0qRbtOld+Y1
yWA/Qlg/1nECAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAWYlRC8e5flZED/JDP0VG
aNENVwv0bFbbzp1urgQeq1TVBDHGKuMJM9klVMBQiMT9q+nPjEgfynSiLVuY7FWs
yD/hFjQMLV2cz7tdBY6l+IV1sAtBdX3ZRmmzttaAs4xmFXCLXdTm4KJ5bPcRnRLA
klMKOsvNY90mRteXvhQy04J2TJVpIld05+yjnYVWoODyX9A/Xda+33qjZECLTnj4
c5L3mamPZEo4nwY+329d7dNvEu+ETp4UzwkzwPFHSGLD01YEJIu83TTi1WDBZygz
dxPUkLKYzRkpYVp3hbZsvkCQVtruY/e6DADZTKAlhL41V6VdH35Es0uw7JrbPf7z
jQ==
-----END CERTIFICATE-----
```

## File: `test/node/fixtures/key.pem`
```
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAsjNYMUk1HzBLM4fL/8c6Z86X/b13V1bMXrrcV28wjmvQv4lA
DlghZGt/zbinyvZrASp8v1btR9gLaNTdrxxnz5FWu1bY947ljgadudh0STLNs4jW
I2wcjgguA8B2rDtvap0bn9JkpjQGcFuqEdJRlr26OwsC5SNCtFxQmTrbsneFMWK3
JsL1riCrV9Cw0L3joki/YKYTTwRZJ2TXrrHvOLQCIUacwCU4oJg19D0FKU/rDtdU
FFojnTio0RFU4/OpjxKzwqjSJE80nPSRHAqXtSgmphrRk4ZVeTxKEGKCoAt/RBwq
vxPFjNlbr1EWY9S7SpFu06V35jXJYD9CWD/WcQIDAQABAoIBAGvpieO2yHONpEyd
VJ0dAbJxOjuPa+C5EGPhVqOgEtB8W9pRfDfziK0uKCPlSb8wAFahaw/XzTMvkqE2
HtT3J6pcAiDKk/M+VqbuPL+ZY7ocCNNK7xpeUuBz9aGSAIuGJo9yepMLLqYzZR7P
c6r9KSlW1ZsBrQwjkTZ1nN1d9kMY+SBpW4PY3lfA69dfPDQ6hsbg+7e37MkP2ygP
LL3H+oljAZJiRSWu7+F2FwTUkNom9va6aKr2FuUgr7pd9PnBoDIEyEWu1sF6nJ85
vVbGRCCkvub+D55U6Q7PsscOY8lc6Z3JaQA7sv8alSHR+q9AOEvkc4uc2V4J9LOa
ZlZzOD0CgYEA1nYxoHe1hNIKHRjY38wSbyfPAKZ9tzrPLq44JBe+9MoMN+pOLA9N
SVorLz9OHl8A4gCMeLgXrX06ECHor1dbC90k+jiU0taOdcADs0BwAbWrgMyiOsjJ
RbwTRUTsAuLLldTBf4sFysCyG0SYCqFL7hJJh2HJKOg428V8b0sfaV8CgYEA1Lcw
eEc11R80Huv5yV8WeYu+uqBo38P1qoC+zlpa7PRw9GX4Ovi20hwkqWNlOyho0TJa
x9HLl87WW/p7pjCM6kcBdHOn0eqHgoUYknYbsVyK0o2P5ajMldOkRu03lqjNuB9/
Q4BYp8Sqwyv/aTGMNDa/TlX8S+3Lk8WIkhBPQi8CgYEAm6xoEadTp/ofRUfIBYvI
xc8Lv9ka4GpcAfKM5gYmouIXRG9cFzd0To6ZUk6NkhY8OdFUJjzbUx/XieZTVRQA
DviT4t43iWQdPPQIu5FGvLb2qyPfjvQ4xdnj0yBYgS/HwBcT7lUn+yktIAYGp5C1
4TZ9ETy2HG+U9lLAJLlPL9kCgYA+N6rMs39ya+MR3FG+bbqkKJTL/5lNQgL8MRYe
Q11vC3xyb9TwYskOob6zcOguKn6mGcVlxt5287/NPXGnRXIiIEyzpBSFGMU0DvwF
8tfcw8WzGkbplLrqY/Ib8Myem5c4cLYHp2XHBIYx+g+F1EE/EHhaUFowV0iBW3i7
yFt2bwKBgG1EycLZ5EMXtitMNdPigRR7UJnNAPSreYrSrFSKYrR6tAHhsAf/uiK/
Wf3hXJvIwRrJOJc29juCi3r8i5xhcoRN7kdd1dOXzEX4azn6PCi27b7wDN20w/Wv
QeeV1QQ0x1ok7AHWLBEZLuYFaded0UnGrDwtwKQ9wg8oH98n8jkR
-----END RSA PRIVATE KEY-----
```

## File: `test/node/fixtures/user.html`
```html
<h1>name</h1>
```

## File: `test/node/fixtures/user.json`
```json
{"name":"tobi"}
```

## File: `test/node/fixtures/user.txt`
```
Tobi
```

## File: `test/support/client.js`
```javascript
const request = require('../..');

if (process.env.HTTP2_TEST) {
  request.http2 = true;
}

exports = module.exports = request;
```

## File: `test/support/server.js`
```javascript
const fs = require('node:fs');
const path = require('node:path');
const process = require('node:process');
const { Buffer } = require('node:buffer');
let http = require('node:http');
const multer = require('multer');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const basicAuth = require('basic-auth-connect');
const express = require('./express');

let isPseudoHeader;

if (process.env.HTTP2_TEST) {
  http = require('node:http2');
  const {
    HTTP2_HEADER_AUTHORITY,
    HTTP2_HEADER_METHOD,
    HTTP2_HEADER_PATH,
    HTTP2_HEADER_SCHEME,
    HTTP2_HEADER_STATUS
  } = http.constants;
  isPseudoHeader = function (name) {
    switch (name) {
      case HTTP2_HEADER_STATUS: // :status
      case HTTP2_HEADER_METHOD: // :method
      case HTTP2_HEADER_PATH: // :path
      case HTTP2_HEADER_AUTHORITY: // :authority
      case HTTP2_HEADER_SCHEME: {
        // :scheme
        return true;
      }

      default: {
        return false;
      }
    }
  };
}

const app = express();

app.use((request, res, next) => {
  res.set('Cache-Control', 'no-cache, no-store');
  next();
});

app.all('/url', (request, res) => {
  res.send(request.url);
});

app.all('/echo', (request, res) => {
  const { headers } = request;
  if (process.env.HTTP2_TEST) {
    for (const name of Object.keys(headers)) {
      if (isPseudoHeader(name)) {
        delete headers[name];
      }
    }
  }

  res.writeHead(200, headers);
  request.pipe(res);
});

let uniq = 0;
app.all('/unique', (request, res) => {
  res.send(`never the same ${uniq++}`);
});

app.use(bodyParser.urlencoded({ extended: true }));
app.use(multer().none());

app.all('/formecho', (request, res) => {
  if (
    !/application\/x-www-form-urlencoded|multipart\/form-data/.test(
      request.headers['content-type']
    )
  ) {
    return res.status(400).end('wrong type');
  }

  res.json(request.body);
});

app.use(bodyParser.json());
app.use(cookieParser());

app.use('/xdomain', (request, res, next) => {
  if (!request.get('Origin')) return next();
  res.set('Access-Control-Allow-Origin', request.get('Origin'));
  res.set('Access-Control-Allow-Credentials', 'true');
  res.set('Access-Control-Allow-Methods', 'POST');
  res.set('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type');
  if (request.method === 'OPTIONS') return res.send(200);
  next();
});

app.get('/xdomain', (request, res) => {
  res.send('tobi');
});

app.get('/login', (request, res) => {
  res.status(200).send('<form id="login"></form>');
});

app.get('/json', (request, res) => {
  res.status(200).json({ name: 'manny' });
});

app.get('/json-hal', (request, res) => {
  res.set('content-type', 'application/hal+json');
  res.send({ name: 'hal 5000' });
});

app.get('/ok', (request, res) => {
  res.send('ok');
});

app.get('/foo', (request, res) => {
  res
    .header('Content-Type', 'application/x-www-form-urlencoded')
    .send('foo=bar');
});

app.get('/form-data', (request, res) => {
  res.header('Content-Type', 'application/x-www-form-urlencoded');
  res.send('pet[name]=manny');
});

app.post('/movie', (request, res) => {
  res.redirect('/movies/all/0');
});

app.get('/', (request, res) => {
  res.set('QUERY', JSON.stringify(request.query));
  res.redirect('/movies');
});

app.get('/movies', (request, res) => {
  res.set('QUERY', JSON.stringify(request.query));
  res.redirect('/movies/all');
});

app.get('/movies/all', (request, res) => {
  res.set('QUERY', JSON.stringify(request.query));
  res.redirect('/movies/all/0');
});

app.get('/movies/all/0', (request, res) => {
  res.set('QUERY', JSON.stringify(request.query));
  res.status(200).send('first movie page');
});

app.get('/movies/random', (request, res) => {
  res.redirect('/movie/4');
});

app.get('/movie/4', (request, res) => {
  setTimeout(() => {
    res.send('not-so-random movie');
  }, 1000);
});

app.get('/links', (request, res) => {
  res.header(
    'Link',
    '<https://api.github.com/repos/visionmedia/mocha/issues?page=2>; rel="next"'
  );
  res.end();
});

app.get('/xml', (request, res) => {
  res.type('xml');
  res.status(200).send('<some><xml></xml></some>');
});

app.get('/custom', (request, res) => {
  res.type('application/x-custom');
  res.status(200).send('custom stuff');
});

app.put('/user/:id', (request, res) => {
  res.send('updated');
});

app.put('/user/:id/body', (request, res) => {
  res.send(`received ${request.body.user}`);
});

app.patch('/user/:id', (request, res) => {
  res.send('updated');
});

app.post('/user/:id/pet', (request, res) => {
  res.send(`added pet "${request.body.pet}"`);
});

app.post('/user', (request, res) => {
  res.send('created');
});

app.delete('/user/:id', (request, res) => {
  res.send('deleted');
});

app.post('/todo/item', (request, res) => {
  let buf = '';
  request.on('data', (chunk) => {
    buf += chunk;
  });
  request.on('end', () => {
    res.send(`added "${buf}"`);
  });
});

app.get('/delay/const', (request, res) => {
  res.redirect('/delay/3000');
});

app.get('/delay/zip', (request, res) => {
  res.writeHead(200, {
    'Content-Type': 'text/plain',
    'Content-Encoding': 'gzip'
  });
  setTimeout(() => {
    res.end();
  }, 10_000);
});

app.get('/delay/json', (request, res) => {
  res.writeHead(200, { 'Content-Type': 'application/json' });
  setTimeout(() => {
    res.end();
  }, 10_000);
});

let slowBodyCallback;
app.get('/delay/slowbody', (request, res) => {
  res.writeHead(200, { 'Content-Type': 'application/octet-stream' });

  // Send lots of garbage data to overflow all buffers along the way,
  // so that the browser gets some data before the request is done
  const initialDataSent = new Promise((resolve) => {
    res.write(Buffer.alloc(4000), () => {
      res.write(Buffer.alloc(16_000));
      resolve();
    });
  });

  // Make sure sending of request body takes over 1s,
  // so that the test can't pass by accident.
  const minimumTime = new Promise((resolve) => {
    setTimeout(resolve, 1001);
  });

  new Promise((resolve) => {
    // Waiting full 10 seconds for the test would be too annoying,
    // so the remote callback is a hack to push the test forward
    slowBodyCallback = resolve;
    setTimeout(resolve, 10_000);
  })
    .then(() => Promise.all([initialDataSent, minimumTime]))
    .then(() => {
      res.end('bye');
    });
});

app.get('/delay/slowbody/finish', (request, res) => {
  if (slowBodyCallback) slowBodyCallback();
  res.sendStatus(204);
});

app.get('/delay/:ms', (request, res) => {
  const ms = Math.trunc(request.params.ms);
  setTimeout(() => {
    res.sendStatus(200);
  }, ms);
});

app.get('/querystring', (request, res) => {
  res.send(request.query);
});

app.get('/querystring-in-header', (request, res) => {
  res.set('query', JSON.stringify(request.query));
  res.send();
});

app.all('/echo-header/:field', (request, res) => {
  res.send(request.headers[request.params.field]);
});

app.get('/echo-headers', (request, res) => {
  res.json(request.headers);
});

app.post('/pet', (request, res) => {
  res.send(`added ${request.body.name} the ${request.body.species}`);
});

app.get('/pets', (request, res) => {
  res.send(['tobi', 'loki', 'jane']);
});

app.get('/json-seq', (request, res) => {
  res
    .set('content-type', 'application/json-seq')
    .send('\u001E{"id":1}\n\u001E{"id":2}\n');
});

app.get('/invalid-json', (request, res) => {
  res.set('content-type', 'application/json');
  // sample invalid json taken from https://github.com/swagger-api/swagger-ui/issues/1354
  res.send(
    ")]}', {'header':{'code':200,'text':'OK','version':'1.0'},'data':'some data'}"
  );
});

app.get('/invalid-json-forbidden', (request, res) => {
  res.set('content-type', 'application/json');
  res.status(403).send('Forbidden');
});

app.get('/text', (request, res) => {
  res.send('just some text');
});

app.get('/basic-auth', basicAuth('tobi', 'learnboost'), (request, res) => {
  res.end('you win!');
});

app.get('/basic-auth/again', basicAuth('tobi', ''), (request, res) => {
  res.end('you win again!');
});

app.post('/auth', basicAuth('foo', 'bar'), (request, res) => {
  const auth = request.headers.authorization;
  const parts = auth.split(' ');
  const credentials = Buffer.from(parts[1], 'base64').toString().split(':');
  const user = credentials[0];
  const pass = credentials[1];

  res.send({ user, pass });
});

app.get('/error', (request, res) => {
  res.status(500).send('boom');
});

app.get('/unauthorized', (request, res) => {
  res.sendStatus(401);
});

app.get('/bad-request', (request, res) => {
  res.sendStatus(400);
});

app.get('/not-acceptable', (request, res) => {
  res.sendStatus(406);
});

app.get('/no-content', (request, res) => {
  res.sendStatus(204);
});

app.delete('/no-content', (request, res) => {
  res.set('content-type', 'application/json');
  res.sendStatus(204);
});

app.post('/created', (request, res) => {
  res.status(201).send('created');
});

app.post('/unprocessable-entity', (request, res) => {
  res.status(422).send('unprocessable entity');
});

app.get('/arraybuffer', (request, res) => {
  const content = new ArrayBuffer(1000);
  res.set('Content-Type', 'application/vnd.superagent');
  res.send(content);
});

app.get('/arraybuffer-unauthorized', (request, res) => {
  res.set('Content-Type', 'application/json');
  res
    .status(401)
    .send('{"message":"Authorization has been denied for this request."}');
});

app.post('/empty-body', bodyParser.text(), (request, res) => {
  if (
    typeof request.body === 'object' &&
    Object.keys(request.body).length === 0
  ) {
    res.sendStatus(204);
  } else {
    res.sendStatus(400);
  }
});

app.get('/collection-json', (request, res) => {
  res.set('content-type', 'application/vnd.collection+json');
  res.send({ name: 'chewbacca' });
});

app.get('/invalid-json', (request, res) => {
  res.set('content-type', 'application/json');
  // sample invalid json taken from https://github.com/swagger-api/swagger-ui/issues/1354
  res.send(
    ")]}', {'header':{'code':200,'text':'OK','version':'1.0'},'data':'some data'}"
  );
});

app.options('/options/echo/body', bodyParser.json(), (request, res) => {
  res.send(request.body);
});

app.get('/cookie-redirect', (request, res) => {
  res.set('Set-Cookie', 'replaced=yes');
  res.append('Set-Cookie', 'from-redir=1', true);
  res.redirect(303, '/show-cookies');
});

app.get('/set-cookie', (request, res) => {
  res.cookie('replaced', 'no');
  res.cookie('persist', '123');
  res.send('ok');
});

app.get('/show-cookies', (request, res) => {
  res.set('content-type', 'text/plain');
  res.send(request.headers.cookie);
});

app.put('/redirect-303', (request, res) => {
  res.redirect(303, '/reply-method');
});

app.put('/redirect-307', (request, res) => {
  res.redirect(307, '/reply-method');
});

app.put('/redirect-308', (request, res) => {
  res.redirect(308, '/reply-method');
});

app.all('/reply-method', (request, res) => {
  res.send(`method=${request.method.toLowerCase()}`);
});

app.get('/tobi', (request, res) => {
  res.send('tobi');
});

app.get('/relative', (request, res) => {
  res.redirect('tobi');
});

app.get('/relative/sub', (request, res) => {
  res.redirect('../tobi');
});

app.get('/header', (request, res) => {
  res.redirect('/header/2');
});

app.post('/header', (request, res) => {
  res.redirect('/header/2');
});

app.get('/header/2', (request, res) => {
  res.send(request.headers);
});

app.get('/bad-redirect', (request, res) => {
  res.status(307).end();
});

app.all('/ua', (request, res) => {
  const { headers } = request;
  if (process.env.HTTP2_TEST) {
    for (const name of Object.keys(headers)) {
      if (isPseudoHeader(name)) {
        delete headers[name];
      }
    }
  }

  res.writeHead(200, headers);
  request.pipe(res);
});

app.get('/manny', (request, res) => {
  res.status(200).json({ name: 'manny' });
});

function serveImageWithType(res, type) {
  const img = fs.readFileSync(
    path.join(__dirname, '../node/fixtures/test.png')
  );
  res.writeHead(200, { 'Content-Type': type });
  res.end(img, 'binary');
}

app.get('/image', (request, res) => {
  serveImageWithType(res, 'image/png');
});
app.get('/image-as-octets', (request, res) => {
  serveImageWithType(res, 'application/octet-stream');
});

app.get('/binary-data', (request, res) => {
  const binData = fs.readFileSync(
    path.join(__dirname, '../node/fixtures/test.aac')
  );
  res.writeHead(200, { 'Content-type': 'audio/aac' });
  res.end(binData, 'binary');
});

app.get('/chunked-json', (request, res) => {
  res.set('content-type', 'application/json');
  res.set('Transfer-Encoding', 'chunked');

  let chunk = 0;
  const interval = setInterval(() => {
    chunk++;
    if (chunk === 1) res.write(`{ "name_${chunk}": "`);
    if (chunk > 1) res.write(`value_${chunk}", "name_${chunk}": "`);
    if (chunk === 10) {
      clearInterval(interval);
      res.write(`value_${chunk}"}`);
      res.end();
    }
  }, 10);
});

app.get('/if-mod', (request, res) => {
  if (request.header('if-modified-since')) {
    res.status(304).end();
  } else {
    res.send(`${Date.now()}`);
  }
});

const called = {};
app.get('/error/ok/:id', (request, res) => {
  if (request.query.qs !== 'present') {
    return res.status(400).end('query string lost');
  }

  const { id } = request.params;
  if (!called[id]) {
    called[id] = true;
    res.status(500).send('boom');
  } else {
    res.send(request.headers);
    delete called[id];
  }
});

app.get('/delay/:ms/ok/:id', (request, res) => {
  const { id } = request.params;
  if (!called[id]) {
    called[id] = true;
    const ms = Math.trunc(request.params.ms);
    setTimeout(() => {
      res.sendStatus(200);
    }, ms);
  } else {
    res.send(`ok = ${request.url}`);
    delete called[id];
  }
});

app.get('/error/redirect/:id', (request, res) => {
  const { id } = request.params;
  if (!called[id]) {
    called[id] = true;
    res.status(500).send('boom');
  } else {
    res.redirect('/movies');
    delete called[id];
  }
});

app.get('/error/redirect-error:id', (request, res) => {
  const { id } = request.params;
  if (!called[id]) {
    called[id] = true;
    res.status(500).send('boom');
  } else {
    res.redirect('/error');
    delete called[id];
  }
});

const server = http.createServer(app);
server.listen(process.env.ZUUL_PORT);
```

## File: `test/support/setup.js`
```javascript
require('should');
require('should-http');

const getPort = require('get-port');

let NODE;
let uri;

async function getSetup() {
  if (NODE && uri) {
    return { NODE, uri };
  }

  NODE = true;
  if (typeof window !== 'undefined') {
    NODE = false;
    uri = `//${window.location.host}`;
  } else {
    try {
      const port = await getPort();

      // check that another call to the function hasn't set the uri already
      if (!uri) {
        process.env.ZUUL_PORT = port;
        uri = `http://localhost:${process.env.ZUUL_PORT}`;
        require('./server');
      }
    } catch (err) {
      console.error(err);
    }
  }

  return { NODE, uri };
}

module.exports = getSetup;
```

## File: `test/support/express/index.js`
```javascript
const process = require('process');
const express = require('express');

let http2Request;
let http2Res;
if (process.env.HTTP2_TEST) {
  const http2 = require('http2');
  const requestDecorator = require('./requestDecorator');
  const resDecorator = require('./responseDecorator');
  http2Request = requestDecorator(
    Object.create(http2.Http2ServerRequest.prototype)
  );
  http2Res = resDecorator(Object.create(http2.Http2ServerResponse.prototype));
}

function createApp() {
  const app = express();
  if (process.env.HTTP2_TEST) {
    app.request = Object.create(http2Request, {
      app: { configurable: true, enumerable: true, writable: true, value: app }
    });
    app.response = Object.create(http2Res, {
      app: { configurable: true, enumerable: true, writable: true, value: app }
    });
  }

  return app;
}

module.exports = createApp;
```

## File: `test/support/express/requestDecorator.js`
```javascript
/*!
 * express
 * Copyright(c) 2009-2013 TJ Holowaychuk
 * Copyright(c) 2013 Roman Shtylman
 * Copyright(c) 2014-2015 Douglas Christopher Wilson
 * MIT Licensed
 */

'use strict';

/**
 * Module dependencies.
 * @private
 */

const { isIP } = require('net');
const accepts = require('accepts');
const typeis = require('type-is');
const fresh = require('fresh');
const parseRange = require('range-parser');
const parse = require('parseurl');
const proxyaddr = require('proxy-addr');

/**
 * Request prototype.
 * @public
 */

/**
 * Module exports.
 * @public
 */

module.exports = setMethods;

function setMethods(request) {
  /**
   * Return request header.
   *
   * The `Referrer` header field is special-cased,
   * both `Referrer` and `Referer` are interchangeable.
   *
   * Examples:
   *
   *     req.get('Content-Type');
   *     // => "text/plain"
   *
   *     req.get('content-type');
   *     // => "text/plain"
   *
   *     req.get('Something');
   *     // => undefined
   *
   * Aliased as `req.header()`.
   *
   * @param {String} name
   * @return {String}
   * @public
   */

  request.get = request.header = function header(name) {
    if (!name) {
      throw new TypeError('name argument is required to req.get');
    }

    if (typeof name !== 'string') {
      throw new TypeError('name must be a string to req.get');
    }

    const lc = name.toLowerCase();

    switch (lc) {
      case 'referer':
      case 'referrer':
        return this.headers.referrer || this.headers.referer;
      default:
        return this.headers[lc];
    }
  };

  /**
   * To do: update docs.
   *
   * Check if the given `type(s)` is acceptable, returning
   * the best match when true, otherwise `undefined`, in which
   * case you should respond with 406 "Not Acceptable".
   *
   * The `type` value may be a single MIME type string
   * such as "application/json", an extension name
   * such as "json", a comma-delimited list such as "json, html, text/plain",
   * an argument list such as `"json", "html", "text/plain"`,
   * or an array `["json", "html", "text/plain"]`. When a list
   * or array is given, the _best_ match, if any is returned.
   *
   * Examples:
   *
   *     // Accept: text/html
   *     req.accepts('html');
   *     // => "html"
   *
   *     // Accept: text/*, application/json
   *     req.accepts('html');
   *     // => "html"
   *     req.accepts('text/html');
   *     // => "text/html"
   *     req.accepts('json, text');
   *     // => "json"
   *     req.accepts('application/json');
   *     // => "application/json"
   *
   *     // Accept: text/*, application/json
   *     req.accepts('image/png');
   *     req.accepts('png');
   *     // => undefined
   *
   *     // Accept: text/*;q=.5, application/json
   *     req.accepts(['html', 'json']);
   *     req.accepts('html', 'json');
   *     req.accepts('html, json');
   *     // => "json"
   *
   * @param {String|Array} type(s)
   * @return {String|Array|Boolean}
   * @public
   */

  request.accepts = function () {
    const accept = accepts(this);
    return accept.types.apply(accept, arguments);
  };

  /**
   * Check if the given `encoding`s are accepted.
   *
   * @param {String} ...encoding
   * @return {String|Array}
   * @public
   */

  request.acceptsEncodings = function () {
    const accept = accepts(this);
    return accept.encodings.apply(accept, arguments);
  };

  /**
   * Check if the given `charset`s are acceptable,
   * otherwise you should respond with 406 "Not Acceptable".
   *
   * @param {String} ...charset
   * @return {String|Array}
   * @public
   */

  request.acceptsCharsets = function () {
    const accept = accepts(this);
    return accept.charsets.apply(accept, arguments);
  };

  /**
   * Check if the given `lang`s are acceptable,
   * otherwise you should respond with 406 "Not Acceptable".
   *
   * @param {String} ...lang
   * @return {String|Array}
   * @public
   */

  request.acceptsLanguages = function () {
    const accept = accepts(this);
    return accept.languages.apply(accept, arguments);
  };

  /**
   * Parse Range header field, capping to the given `size`.
   *
   * Unspecified ranges such as "0-" require knowledge of your resource length. In
   * the case of a byte range this is of course the total number of bytes. If the
   * Range header field is not given `undefined` is returned, `-1` when unsatisfiable,
   * and `-2` when syntactically invalid.
   *
   * When ranges are returned, the array has a "type" property which is the type of
   * range that is required (most commonly, "bytes"). Each array element is an object
   * with a "start" and "end" property for the portion of the range.
   *
   * The "combine" option can be set to `true` and overlapping & adjacent ranges
   * will be combined into a single range.
   *
   * NOTE: remember that ranges are inclusive, so for example "Range: users=0-3"
   * should respond with 4 users when available, not 3.
   *
   * @param {number} size
   * @param {object} [options]
   * @param {boolean} [options.combine=false]
   * @return {number|array}
   * @public
   */

  request.range = function range(size, options) {
    const range = this.get('Range');
    if (!range) return;
    return parseRange(size, range, options);
  };

  /**
   * Parse the query string of `req.url`.
   *
   * This uses the "query parser" setting to parse the raw
   * string into an object.
   *
   * @return {String}
   * @api public
   */

  defineGetter(request, 'query', function query() {
    const queryparse = this.app.get('query parser fn');

    if (!queryparse) {
      // parsing is disabled
      return Object.create(null);
    }

    const querystring = parse(this).query;

    return queryparse(querystring);
  });

  /**
   * Check if the incoming request contains the "Content-Type"
   * header field, and it contains the give mime `type`.
   *
   * Examples:
   *
   *      // With Content-Type: text/html; charset=utf-8
   *      req.is('html');
   *      req.is('text/html');
   *      req.is('text/*');
   *      // => true
   *
   *      // When Content-Type is application/json
   *      req.is('json');
   *      req.is('application/json');
   *      req.is('application/*');
   *      // => true
   *
   *      req.is('html');
   *      // => false
   *
   * @param {String|Array} types...
   * @return {String|false|null}
   * @public
   */

  request.is = function is(types) {
    let array = types;

    // support flattened arguments
    if (!Array.isArray(types)) {
      array = Array.from({ length: arguments.length });
      for (let i = 0; i < array.length; i++) {
        array[i] = arguments[i];
      }
    }

    return typeis(this, array);
  };

  /**
   * Return the protocol string "http" or "https"
   * when requested with TLS. When the "trust proxy"
   * setting trusts the socket address, the
   * "X-Forwarded-Proto" header field will be trusted
   * and used if present.
   *
   * If you're running behind a reverse proxy that
   * supplies https for you this may be enabled.
   *
   * @return {String}
   * @public
   */

  defineGetter(request, 'protocol', function protocol() {
    const proto = this.connection.encrypted ? 'https' : 'http';
    const trust = this.app.get('trust proxy fn');

    if (!trust(this.connection.remoteAddress, 0)) {
      return proto;
    }

    // Note: X-Forwarded-Proto is normally only ever a
    //       single value, but this is to be safe.
    const header = this.get('X-Forwarded-Proto') || proto;
    const index = header.indexOf(',');

    return index !== -1 ? header.slice(0, index).trim() : header.trim();
  });

  /**
   * Short-hand for:
   *
   *    req.protocol === 'https'
   *
   * @return {Boolean}
   * @public
   */

  defineGetter(request, 'secure', function secure() {
    return this.protocol === 'https';
  });

  /**
   * Return the remote address from the trusted proxy.
   *
   * The is the remote address on the socket unless
   * "trust proxy" is set.
   *
   * @return {String}
   * @public
   */

  defineGetter(request, 'ip', function ip() {
    const trust = this.app.get('trust proxy fn');
    return proxyaddr(this, trust);
  });

  /**
   * When "trust proxy" is set, trusted proxy addresses + client.
   *
   * For example if the value were "client, proxy1, proxy2"
   * you would receive the array `["client", "proxy1", "proxy2"]`
   * where "proxy2" is the furthest down-stream and "proxy1" and
   * "proxy2" were trusted.
   *
   * @return {Array}
   * @public
   */

  defineGetter(request, 'ips', function ips() {
    const trust = this.app.get('trust proxy fn');
    const addrs = proxyaddr.all(this, trust);

    // reverse the order (to farthest -> closest)
    // and remove socket address
    addrs.reverse().pop();

    return addrs;
  });

  /**
   * Return subdomains as an array.
   *
   * Subdomains are the dot-separated parts of the host before the main domain of
   * the app. By default, the domain of the app is assumed to be the last two
   * parts of the host. This can be changed by setting "subdomain offset".
   *
   * For example, if the domain is "tobi.ferrets.example.com":
   * If "subdomain offset" is not set, req.subdomains is `["ferrets", "tobi"]`.
   * If "subdomain offset" is 3, req.subdomains is `["tobi"]`.
   *
   * @return {Array}
   * @public
   */

  defineGetter(request, 'subdomains', function subdomains() {
    const { hostname } = this;

    if (!hostname) return [];

    const offset = this.app.get('subdomain offset');
    const subdomains = !isIP(hostname)
      ? hostname.split('.').reverse()
      : [hostname];

    return subdomains.slice(offset);
  });

  /**
   * Short-hand for `url.parse(req.url).pathname`.
   *
   * @return {String}
   * @public
   */

  defineGetter(request, 'path', function path() {
    return parse(this).pathname;
  });

  /**
   * Parse the "Host" header field to a host.
   *
   * When the "trust proxy" setting trusts the socket
   * address, the "X-Forwarded-Host" header field will
   * be trusted.
   *
   * @return {String}
   * @public
   */

  defineGetter(request, 'host', function host() {
    const trust = this.app.get('trust proxy fn');
    let value = this.get('X-Forwarded-Host');

    if (!value || !trust(this.connection.remoteAddress, 0)) {
      value = this.get('Host');
    }

    return value || undefined;
  });

  /**
   * Parse the "Host" header field to a hostname.
   *
   * When the "trust proxy" setting trusts the socket
   * address, the "X-Forwarded-Host" header field will
   * be trusted.
   *
   * @return {String}
   * @api public
   */

  defineGetter(request, 'hostname', function hostname() {
    const { host } = this;

    if (!host) return;

    // IPv6 literal support
    const offset = host[0] === '[' ? host.indexOf(']') + 1 : 0;
    const index = host.indexOf(':', offset);

    return index !== -1 ? host.slice(0, index) : host;
  });

  /**
   * Check if the request is fresh, aka
   * Last-Modified and/or the ETag
   * still match.
   *
   * @return {Boolean}
   * @public
   */

  defineGetter(request, 'fresh', function () {
    const { method } = this;
    const { res } = this;
    const status = res.statusCode;

    // GET or HEAD for weak freshness validation only
    if (method !== 'GET' && method !== 'HEAD') return false;

    // 2xx or 304 as per rfc2616 14.26
    if ((status >= 200 && status < 300) || status === 304) {
      return fresh(this.headers, {
        etag: res.get('ETag'),
        'last-modified': res.get('Last-Modified')
      });
    }

    return false;
  });

  /**
   * Check if the request is stale, aka
   * "Last-Modified" and / or the "ETag" for the
   * resource has changed.
   *
   * @return {Boolean}
   * @public
   */

  defineGetter(request, 'stale', function stale() {
    return !this.fresh;
  });

  /**
   * Check if the request was an _XMLHttpRequest_.
   *
   * @return {Boolean}
   * @public
   */

  defineGetter(request, 'xhr', function xhr() {
    const value = this.get('X-Requested-With') || '';
    return value.toLowerCase() === 'xmlhttprequest';
  });

  return request;
}

/**
 * Helper function for creating a getter on an object.
 *
 * @param {Object} obj
 * @param {String} name
 * @param {Function} getter
 * @private
 */
function defineGetter(object, name, getter) {
  Object.defineProperty(object, name, {
    configurable: true,
    enumerable: true,
    get: getter
  });
}
```

## File: `test/support/express/responseDecorator.js`
```javascript
/*!
 * express
 * Copyright(c) 2009-2013 TJ Holowaychuk
 * Copyright(c) 2014-2015 Douglas Christopher Wilson
 * MIT Licensed
 */

'use strict';

/**
 * Module dependencies.
 * @private
 */

const path = require('path');
const { Buffer } = require('safe-buffer');
const contentDisposition = require('content-disposition');
const encodeUrl = require('encodeurl');
const escapeHtml = require('escape-html');
const onFinished = require('on-finished');
const pathIsAbsolute = require('path-is-absolute');
const statuses = require('statuses');
const merge = require('utils-merge');
const { sign } = require('cookie-signature');
const cookie = require('cookie');
const send = require('send');
const { normalizeType } = require('./utils');
const { normalizeTypes } = require('./utils');
const { setCharset } = require('./utils');

const { extname } = path;
const { mime } = send;
const { resolve } = path;
const vary = require('vary');
/**
 * Module exports.
 * @public
 */

module.exports = setMethods;

function setMethods(res) {
  /**
   * Module variables.
   * @private
   */

  const charsetRegExp = /;\s*charset\s*=/;

  /**
   * Set status `code`.
   *
   * @param {Number} code
   * @return {ServerResponse}
   * @public
   */

  res.status = function status(code) {
    this.statusCode = code;
    return this;
  };

  /**
   * Set Link header field with the given `links`.
   *
   * Examples:
   *
   *    res.links({
   *      next: 'http://api.example.com/users?page=2',
   *      last: 'http://api.example.com/users?page=5'
   *    });
   *
   * @param {Object} links
   * @return {ServerResponse}
   * @public
   */

  res.links = function (links) {
    let link = this.get('Link') || '';
    if (link) link += ', ';
    return this.set(
      'Link',
      link +
        Object.keys(links)
          .map((rel) => {
            return '<' + links[rel] + '>; rel="' + rel + '"';
          })
          .join(', ')
    );
  };

  /**
   * Send a response.
   *
   * Examples:
   *
   *     res.send(Buffer.from('wahoo'));
   *     res.send({ some: 'json' });
   *     res.send('<p>some html</p>');
   *
   * @param {string|number|boolean|object|Buffer} body
   * @public
   */

  res.send = function send(body) {
    let chunk = body;
    let encoding;
    const { req } = this;
    let type;

    // settings
    const { app } = this;

    switch (typeof chunk) {
      // string defaulting to html
      case 'string':
        if (!this.get('Content-Type')) {
          this.type('html');
        }

        break;
      case 'boolean':
      case 'number':
      case 'object':
        if (chunk === null) {
          chunk = '';
        } else if (Buffer.isBuffer(chunk)) {
          if (!this.get('Content-Type')) {
            this.type('bin');
          }
        } else {
          return this.json(chunk);
        }

        break;
    }

    // write strings in utf-8
    if (typeof chunk === 'string') {
      encoding = 'utf8';
      type = this.get('Content-Type');

      // reflect this in content-type
      if (typeof type === 'string') {
        this.set('Content-Type', setCharset(type, 'utf-8'));
      }
    }

    // determine if ETag should be generated
    const etagFn = app.get('etag fn');
    const generateETag = !this.get('ETag') && typeof etagFn === 'function';

    // populate Content-Length
    let length_;
    if (chunk !== undefined) {
      if (Buffer.isBuffer(chunk)) {
        // get length of Buffer
        length_ = chunk.length;
      } else if (!generateETag && chunk.length < 1000) {
        // just calculate length when no ETag + small chunk
        length_ = Buffer.byteLength(chunk, encoding);
      } else {
        // convert chunk to Buffer and calculate
        chunk = Buffer.from(chunk, encoding);
        encoding = undefined;
        length_ = chunk.length;
      }

      this.set('Content-Length', length_);
    }

    // populate ETag
    let etag;
    if (
      generateETag &&
      length_ !== undefined &&
      (etag = etagFn(chunk, encoding))
    ) {
      this.set('ETag', etag);
    }

    // freshness
    if (req.fresh) this.statusCode = 304;

    // strip irrelevant headers
    if (this.statusCode === 204 || this.statusCode === 304) {
      this.removeHeader('Content-Type');
      this.removeHeader('Content-Length');
      this.removeHeader('Transfer-Encoding');
      chunk = '';
    }

    if (req.method === 'HEAD') {
      // skip body for HEAD
      this.end();
    } else {
      // respond
      this.end(chunk, encoding);
    }

    return this;
  };

  /**
   * Send JSON response.
   *
   * Examples:
   *
   *     res.json(null);
   *     res.json({ user: 'tj' });
   *
   * @param {string|number|boolean|object} obj
   * @public
   */

  res.json = function json(object) {
    // settings
    const { app } = this;
    const escape = app.get('json escape');
    const replacer = app.get('json replacer');
    const spaces = app.get('json spaces');
    const body = stringify(object, replacer, spaces, escape);

    // content-type
    if (!this.get('Content-Type')) {
      this.set('Content-Type', 'application/json');
    }

    return this.send(body);
  };

  /**
   * Send JSON response with JSONP callback support.
   *
   * Examples:
   *
   *     res.jsonp(null);
   *     res.jsonp({ user: 'tj' });
   *
   * @param {string|number|boolean|object} obj
   * @public
   */

  res.jsonp = function jsonp(object) {
    // settings
    const { app } = this;
    const escape = app.get('json escape');
    const replacer = app.get('json replacer');
    const spaces = app.get('json spaces');
    let body = stringify(object, replacer, spaces, escape);
    let callback = this.req.query[app.get('jsonp callback name')];

    // content-type
    if (!this.get('Content-Type')) {
      this.set('X-Content-Type-Options', 'nosniff');
      this.set('Content-Type', 'application/json');
    }

    // fixup callback
    if (Array.isArray(callback)) {
      callback = callback[0];
    }

    // jsonp
    if (typeof callback === 'string' && callback.length > 0) {
      this.set('X-Content-Type-Options', 'nosniff');
      this.set('Content-Type', 'text/javascript');

      // restrict callback charset
      callback = callback.replace(/[^[\]\w$.]/g, '');

      // replace chars not allowed in JavaScript that are in JSON
      body = body.replace(/\u2028/g, '\\u2028').replace(/\u2029/g, '\\u2029');

      // the /**/ is a specific security mitigation for "Rosetta Flash JSONP abuse"
      // the typeof check is just to reduce client error noise
      body =
        '/**/ typeof ' +
        callback +
        " === 'function' && " +
        callback +
        '(' +
        body +
        ');';
    }

    return this.send(body);
  };

  /**
   * Send given HTTP status code.
   *
   * Sets the response status to `statusCode` and the body of the
   * response to the standard description from node's http.STATUS_CODES
   * or the statusCode number if no description.
   *
   * Examples:
   *
   *     res.sendStatus(200);
   *
   * @param {number} statusCode
   * @public
   */

  res.sendStatus = function sendStatus(statusCode) {
    const body = statuses(statusCode) || String(statusCode);

    this.statusCode = statusCode;
    this.type('txt');

    return this.send(body);
  };

  /**
   * Transfer the file at the given `path`.
   *
   * Automatically sets the _Content-Type_ response header field.
   * The callback `callback(err)` is invoked when the transfer is complete
   * or when an error occurs. Be sure to check `res.sentHeader`
   * if you wish to attempt responding, as the header and some data
   * may have already been transferred.
   *
   * Options:
   *
   *   - `maxAge`   defaulting to 0 (can be string converted by `ms`)
   *   - `root`     root directory for relative filenames
   *   - `headers`  object of headers to serve with file
   *   - `dotfiles` serve dotfiles, defaulting to false; can be `"allow"` to send them
   *
   * Other options are passed along to `send`.
   *
   * Examples:
   *
   *  The following example illustrates how `res.sendFile()` may
   *  be used as an alternative for the `static()` middleware for
   *  dynamic situations. The code backing `res.sendFile()` is actually
   *  the same code, so HTTP cache support etc is identical.
   *
   *     app.get('/user/:uid/photos/:file', function(req, res){
   *       var uid = req.params.uid
   *         , file = req.params.file;
   *
   *       req.user.mayViewFilesFrom(uid, function(yes){
   *         if (yes) {
   *           res.sendFile('/uploads/' + uid + '/' + file);
   *         } else {
   *           res.send(403, 'Sorry! you cant see that.');
   *         }
   *       });
   *     });
   *
   * @public
   */

  res.sendFile = function sendFile(path, options, callback) {
    let done = callback;
    const { req } = this;
    const res = this;
    const { next } = req;
    let options_ = options || {};

    if (!path) {
      throw new TypeError('path argument is required to res.sendFile');
    }

    // support function as second arg
    if (typeof options === 'function') {
      done = options;
      options_ = {};
    }

    if (!options_.root && !pathIsAbsolute(path)) {
      throw new TypeError(
        'path must be absolute or specify root to res.sendFile'
      );
    }

    // create file stream
    const pathname = encodeURI(path);
    const file = send(req, pathname, options_);

    // transfer
    sendfile(res, file, options_, (error) => {
      if (done) return done(error);
      if (error && error.code === 'EISDIR') return next();

      // next() all but write errors
      if (error && error.code !== 'ECONNABORTED' && error.syscall !== 'write') {
        next(error);
      }
    });
  };

  /**
   * Transfer the file at the given `path` as an attachment.
   *
   * Optionally providing an alternate attachment `filename`,
   * and optional callback `callback(err)`. The callback is invoked
   * when the data transfer is complete, or when an error has
   * ocurred. Be sure to check `res.headersSent` if you plan to respond.
   *
   * Optionally providing an `options` object to use with `res.sendFile()`.
   * This function will set the `Content-Disposition` header, overriding
   * any `Content-Disposition` header passed as header options in order
   * to set the attachment and filename.
   *
   * This method uses `res.sendFile()`.
   *
   * @public
   */

  res.download = function download(path, filename, options, callback) {
    let done = callback;
    let name = filename;
    let options_ = options || null;

    // support function as second or third arg
    if (typeof filename === 'function') {
      done = filename;
      name = null;
      options_ = null;
    } else if (typeof options === 'function') {
      done = options;
      options_ = null;
    }

    // set Content-Disposition when file is sent
    const headers = {
      'Content-Disposition': contentDisposition(name || path)
    };

    // merge user-provided headers
    if (options_ && options_.headers) {
      const keys = Object.keys(options_.headers);
      for (const key of keys) {
        if (key.toLowerCase() !== 'content-disposition') {
          headers[key] = options_.headers[key];
        }
      }
    }

    // merge user-provided options
    options_ = Object.create(options_);
    options_.headers = headers;

    // Resolve the full path for sendFile
    const fullPath = resolve(path);

    // send file
    return this.sendFile(fullPath, options_, done);
  };

  /**
   * Set _Content-Type_ response header with `type` through `mime.lookup()`
   * when it does not contain "/", or set the Content-Type to `type` otherwise.
   *
   * Examples:
   *
   *     res.type('.html');
   *     res.type('html');
   *     res.type('json');
   *     res.type('application/json');
   *     res.type('png');
   *
   * @param {String} type
   * @return {ServerResponse} for chaining
   * @public
   */

  res.contentType = res.type = function contentType(type) {
    const ct = !type.includes('/') ? mime.lookup(type) : type;

    return this.set('Content-Type', ct);
  };

  /**
   * Respond to the Acceptable formats using an `obj`
   * of mime-type callbacks.
   *
   * This method uses `req.accepted`, an array of
   * acceptable types ordered by their quality values.
   * When "Accept" is not present the _first_ callback
   * is invoked, otherwise the first match is used. When
   * no match is performed the server responds with
   * 406 "Not Acceptable".
   *
   * Content-Type is set for you, however if you choose
   * you may alter this within the callback using `res.type()`
   * or `res.set('Content-Type', ...)`.
   *
   *    res.format({
   *      'text/plain': function(){
   *        res.send('hey');
   *      },
   *
   *      'text/html': function(){
   *        res.send('<p>hey</p>');
   *      },
   *
   *      'appliation/json': function(){
   *        res.send({ message: 'hey' });
   *      }
   *    });
   *
   * In addition to canonicalized MIME types you may
   * also use extnames mapped to these types:
   *
   *    res.format({
   *      text: function(){
   *        res.send('hey');
   *      },
   *
   *      html: function(){
   *        res.send('<p>hey</p>');
   *      },
   *
   *      json: function(){
   *        res.send({ message: 'hey' });
   *      }
   *    });
   *
   * By default Express passes an `Error`
   * with a `.status` of 406 to `next(err)`
   * if a match is not made. If you provide
   * a `.default` callback it will be invoked
   * instead.
   *
   * @param {Object} obj
   * @return {ServerResponse} for chaining
   * @public
   */

  res.format = function (object) {
    const { req } = this;
    const { next } = req;

    const fn = object.default;
    if (fn) delete object.default;
    const keys = Object.keys(object);

    const key = keys.length > 0 ? req.accepts(keys) : false;

    this.vary('Accept');

    if (key) {
      this.set('Content-Type', normalizeType(key).value);
      object[key](req, this, next);
    } else if (fn) {
      fn();
    } else {
      const error = new Error('Not Acceptable');
      error.status = error.statusCode = 406;
      error.types = normalizeTypes(keys).map((o) => {
        return o.value;
      });
      next(error);
    }

    return this;
  };

  /**
   * Set _Content-Disposition_ header to _attachment_ with optional `filename`.
   *
   * @param {String} filename
   * @return {ServerResponse}
   * @public
   */

  res.attachment = function attachment(filename) {
    if (filename) {
      this.type(extname(filename));
    }

    this.set('Content-Disposition', contentDisposition(filename));

    return this;
  };

  /**
   * Append additional header `field` with value `val`.
   *
   * Example:
   *
   *    res.append('Link', ['<http://localhost/>', '<http://localhost:3000/>']);
   *    res.append('Set-Cookie', 'foo=bar; Path=/; HttpOnly');
   *    res.append('Warning', '199 Miscellaneous warning');
   *
   * @param {String} field
   * @param {String|Array} val
   * @return {ServerResponse} for chaining
   * @public
   */

  res.append = function append(field, value_) {
    const previous = this.get(field);
    let value = value_;

    if (previous) {
      // concat the new and prev vals
      value = Array.isArray(previous)
        ? previous.concat(value_)
        : Array.isArray(value_)
        ? [previous].concat(value_)
        : [previous, value_];
    }

    return this.set(field, value);
  };

  /**
   * Set header `field` to `val`, or pass
   * an object of header fields.
   *
   * Examples:
   *
   *    res.set('Foo', ['bar', 'baz']);
   *    res.set('Accept', 'application/json');
   *    res.set({ Accept: 'text/plain', 'X-API-Key': 'tobi' });
   *
   * Aliased as `res.header()`.
   *
   * @param {String|Object} field
   * @param {String|Array} val
   * @return {ServerResponse} for chaining
   * @public
   */

  res.set = res.header = function header(field, value_) {
    if (arguments.length === 2) {
      let value = Array.isArray(value_) ? value_.map(String) : String(value_);

      // add charset to content-type
      if (field.toLowerCase() === 'content-type') {
        if (Array.isArray(value)) {
          throw new TypeError('Content-Type cannot be set to an Array');
        }

        if (!charsetRegExp.test(value)) {
          const charset = mime.charsets.lookup(value.split(';')[0]);
          if (charset) value += '; charset=' + charset.toLowerCase();
        }
      }

      this.setHeader(field, value);
    } else {
      for (const key in field) {
        this.set(key, field[key]);
      }
    }

    return this;
  };

  /**
   * Get value for header `field`.
   *
   * @param {String} field
   * @return {String}
   * @public
   */

  res.get = function (field) {
    return this.getHeader(field);
  };

  /**
   * Clear cookie `name`.
   *
   * @param {String} name
   * @param {Object} [options]
   * @return {ServerResponse} for chaining
   * @public
   */

  res.clearCookie = function clearCookie(name, options) {
    const options_ = merge({ expires: new Date(1), path: '/' }, options);

    return this.cookie(name, '', options_);
  };

  /**
   * Set cookie `name` to `value`, with the given `options`.
   *
   * Options:
   *
   *    - `maxAge`   max-age in milliseconds, converted to `expires`
   *    - `signed`   sign the cookie
   *    - `path`     defaults to "/"
   *
   * Examples:
   *
   *    // "Remember Me" for 15 minutes
   *    res.cookie('rememberme', '1', { expires: new Date(Date.now() + 900000), httpOnly: true });
   *
   *    // save as above
   *    res.cookie('rememberme', '1', { maxAge: 900000, httpOnly: true })
   *
   * @param {String} name
   * @param {String|Object} value
   * @param {Object} [options]
   * @return {ServerResponse} for chaining
   * @public
   */

  res.cookie = function (name, value, options) {
    const options_ = merge({}, options);
    const { secret } = this.req;
    const { signed } = options_;

    if (signed && !secret) {
      throw new Error('cookieParser("secret") required for signed cookies');
    }

    let value_ =
      typeof value === 'object' ? 'j:' + JSON.stringify(value) : String(value);

    if (signed) {
      value_ = 's:' + sign(value_, secret);
    }

    if ('maxAge' in options_) {
      options_.expires = new Date(Date.now() + options_.maxAge);
      options_.maxAge /= 1000;
    }

    if (options_.path == null) {
      options_.path = '/';
    }

    this.append('Set-Cookie', cookie.serialize(name, String(value_), options_));

    return this;
  };

  /**
   * Set the location header to `url`.
   *
   * The given `url` can also be "back", which redirects
   * to the _Referrer_ or _Referer_ headers or "/".
   *
   * Examples:
   *
   *    res.location('/foo/bar').;
   *    res.location('http://example.com');
   *    res.location('../login');
   *
   * @param {String} url
   * @return {ServerResponse} for chaining
   * @public
   */

  res.location = function location(url) {
    let loc = url;

    // "back" is an alias for the referrer
    if (url === 'back') {
      loc = this.req.get('Referrer') || '/';
    }

    // set location
    return this.set('Location', encodeUrl(loc));
  };

  /**
   * Redirect to the given `url` with optional response `status`
   * defaulting to 302.
   *
   * The resulting `url` is determined by `res.location()`, so
   * it will play nicely with mounted apps, relative paths,
   * `"back"` etc.
   *
   * Examples:
   *
   *    res.redirect('/foo/bar');
   *    res.redirect('http://example.com');
   *    res.redirect(301, 'http://example.com');
   *    res.redirect('../login'); // /blog/post/1 -> /blog/login
   *
   * @public
   */

  res.redirect = function redirect(url) {
    let address = url;
    let body;
    let status = 302;

    // allow status / url
    if (arguments.length === 2) {
      status = arguments[0];
      address = arguments[1];
    }

    // Set location header
    address = this.location(address).get('Location');

    // Support text/{plain,html} by default
    this.format({
      text() {
        body = statuses(status) + '. Redirecting to ' + address;
      },

      html() {
        const u = escapeHtml(address);
        body =
          '<p>' +
          statuses(status) +
          '. Redirecting to <a href="' +
          u +
          '">' +
          u +
          '</a></p>';
      },

      default() {
        body = '';
      }
    });

    // Respond
    this.statusCode = status;
    this.set('Content-Length', Buffer.byteLength(body));

    if (this.req.method === 'HEAD') {
      this.end();
    } else {
      this.end(body);
    }
  };

  /**
   * Add `field` to Vary. If already present in the Vary set, then
   * this call is simply ignored.
   *
   * @param {Array|String} field
   * @return {ServerResponse} for chaining
   * @public
   */

  res.vary = function (field) {
    vary(this, field);

    return this;
  };

  /**
   * Render `view` with the given `options` and optional callback `fn`.
   * When a callback function is given a response will _not_ be made
   * automatically, otherwise a response of _200_ and _text/html_ is given.
   *
   * Options:
   *
   *  - `cache`     boolean hinting to the engine it should cache
   *  - `filename`  filename of the view being rendered
   *
   * @public
   */

  res.render = function render(view, options, callback) {
    const { app } = this.req;
    let done = callback;
    let options_ = options || {};
    const { req } = this;
    const self = this;

    // support callback function as second arg
    if (typeof options === 'function') {
      done = options;
      options_ = {};
    }

    // merge res.locals
    options_._locals = self.locals;

    // default callback to respond
    done =
      done ||
      function (error, string_) {
        if (error) return req.next(error);
        self.send(string_);
      };

    // render
    app.render(view, options_, done);
  };

  // pipe the send file stream
  function sendfile(res, file, options, callback) {
    let done = false;
    let streaming;

    // request aborted
    function onaborted() {
      if (done) return;
      done = true;

      const error = new Error('Request aborted');
      error.code = 'ECONNABORTED';
      callback(error);
    }

    // directory
    function ondirectory() {
      if (done) return;
      done = true;

      const error = new Error('EISDIR, read');
      error.code = 'EISDIR';
      callback(error);
    }

    // errors
    function onerror(error) {
      if (done) return;
      done = true;
      callback(error);
    }

    // ended
    function onend() {
      if (done) return;
      done = true;
      callback();
    }

    // file
    function onfile() {
      streaming = false;
    }

    // finished
    function onfinish(error) {
      if (error && error.code === 'ECONNRESET') return onaborted();
      if (error) return onerror(error);
      if (done) return;

      setImmediate(() => {
        if (streaming !== false && !done) {
          onaborted();
          return;
        }

        if (done) return;
        done = true;
        callback();
      });
    }

    // streaming
    function onstream() {
      streaming = true;
    }

    file.on('directory', ondirectory);
    file.on('end', onend);
    file.on('error', onerror);
    file.on('file', onfile);
    file.on('stream', onstream);

    if (options.headers) {
      // set headers on successful transfer
      file.on('headers', function headers(res) {
        const object = options.headers;
        const keys = Object.keys(object);

        for (const k of keys) {
          res.setHeader(k, object[k]);
        }
      });
    }

    // pipe
    file.pipe(res);

    onFinished(res, onfinish);
  }

  return res;
}

/**
 * Stringify JSON, like JSON.stringify, but v8 optimized, with the
 * ability to escape characters that can trigger HTML sniffing.
 *
 * @param {*} value
 * @param {function} replaces
 * @param {number} spaces
 * @param {boolean} escape
 * @returns {string}
 * @private
 */

function stringify(value, replacer, spaces, escape) {
  // v8 checks arguments.length for optimizing simple call
  // https://bugs.chromium.org/p/v8/issues/detail?id=4730
  let json =
    replacer || spaces
      ? JSON.stringify(value, replacer, spaces)
      : JSON.stringify(value);

  if (escape) {
    json = json.replace(/[<>&]/g, (c) => {
      switch (c.charCodeAt(0)) {
        case 0x3c:
          return '\\u003c';
        case 0x3e:
          return '\\u003e';
        case 0x26:
          return '\\u0026';
        default:
          return c;
      }
    });
  }

  return json;
}
```

## File: `test/support/express/utils.js`
```javascript
/*!
 * express
 * Copyright(c) 2009-2013 TJ Holowaychuk
 * Copyright(c) 2014-2015 Douglas Christopher Wilson
 * MIT Licensed
 */

'use strict';

/**
 * Module dependencies.
 * @api private
 */

const querystring = require('querystring');
const { Buffer } = require('safe-buffer');
const contentType = require('content-type');
const { mime } = require('send');
const etag = require('etag');
const proxyaddr = require('proxy-addr');
const qs = require('qs');

let isHttp2Supported = true;

/**
 * Test for http2 support
 * @api private
 */
try {
  require('http2');
} catch {
  isHttp2Supported = false;
}
/**
 * Return strong ETag for `body`.
 *
 * @param {String|Buffer} body
 * @param {String} [encoding]
 * @return {String}
 * @api private
 */

exports.etag = createETagGenerator({ weak: false });

/**
 * Return weak ETag for `body`.
 *
 * @param {String|Buffer} body
 * @param {String} [encoding]
 * @return {String}
 * @api private
 */

exports.wetag = createETagGenerator({ weak: true });

/**
 * Normalize the given `type`, for example "html" becomes "text/html".
 *
 * @param {String} type
 * @return {Object}
 * @api private
 */

exports.normalizeType = function (type) {
  return ~type.indexOf('/')
    ? acceptParameters(type)
    : { value: mime.lookup(type), params: {} };
};

/**
 * Normalize `types`, for example "html" becomes "text/html".
 *
 * @param {Array} types
 * @return {Array}
 * @api private
 */

exports.normalizeTypes = function (types) {
  const returnValue = [];

  for (const element of types) {
    returnValue.push(exports.normalizeType(element));
  }

  return returnValue;
};

/**
 * Parse accept params `str` returning an
 * object with `.value`, `.quality` and `.params`.
 * also includes `.originalIndex` for stable sorting
 *
 * @param {String} str
 * @return {Object}
 * @api private
 */

function acceptParameters(string_, index) {
  const parts = string_.split(/ *; */);
  const returnValue = {
    value: parts[0],
    quality: 1,
    params: {},
    originalIndex: index
  };

  for (let i = 1; i < parts.length; ++i) {
    const pms = parts[i].split(/ *= */);
    if (pms[0] === 'q') {
      returnValue.quality = Number.parseFloat(pms[1]);
    } else {
      returnValue.params[pms[0]] = pms[1];
    }
  }

  return returnValue;
}

/**
 * Compile "etag" value to function.
 *
 * @param  {Boolean|String|Function} val
 * @return {Function}
 * @api private
 */

exports.compileETag = function (value) {
  let fn;

  if (typeof value === 'function') {
    return value;
  }

  switch (value) {
    case true:
      fn = exports.wetag;
      break;
    case false:
      break;
    case 'strong':
      fn = exports.etag;
      break;
    case 'weak':
      fn = exports.wetag;
      break;
    default:
      throw new TypeError('unknown value for etag function: ' + value);
  }

  return fn;
};

/**
 * Compile "query parser" value to function.
 *
 * @param  {String|Function} val
 * @return {Function}
 * @api private
 */

exports.compileQueryParser = function compileQueryParser(value) {
  let fn;

  if (typeof value === 'function') {
    return value;
  }

  switch (value) {
    case true:
      fn = querystring.parse;
      break;
    case false:
      break;
    case 'extended':
      fn = parseExtendedQueryString;
      break;
    case 'simple':
      fn = querystring.parse;
      break;
    default:
      throw new TypeError('unknown value for query parser function: ' + value);
  }

  return fn;
};

/**
 * Compile "proxy trust" value to function.
 *
 * @param  {Boolean|String|Number|Array|Function} val
 * @return {Function}
 * @api private
 */

exports.compileTrust = function (value) {
  if (typeof value === 'function') return value;

  if (value === true) {
    // Support plain true/false
    return function () {
      return true;
    };
  }

  if (typeof value === 'number') {
    // Support trusting hop count
    return function (a, i) {
      return i < value;
    };
  }

  if (typeof value === 'string') {
    // Support comma-separated values
    value = value.split(/ *, */);
  }

  return proxyaddr.compile(value || []);
};

/**
 * Flag for http2 support
 */
exports.isHttp2Supported = isHttp2Supported;
/**
 * Set the charset in a given Content-Type string.
 *
 * @param {String} type
 * @param {String} charset
 * @return {String}
 * @api private
 */

exports.setCharset = function setCharset(type, charset) {
  if (!type || !charset) {
    return type;
  }

  // parse type
  const parsed = contentType.parse(type);

  // set charset
  parsed.parameters.charset = charset;

  // format type
  return contentType.format(parsed);
};

/**
 * Create an ETag generator function, generating ETags with
 * the given options.
 *
 * @param {object} options
 * @return {function}
 * @private
 */

function createETagGenerator(options) {
  return function generateETag(body, encoding) {
    const buf = !Buffer.isBuffer(body) ? Buffer.from(body, encoding) : body;

    return etag(buf, options);
  };
}

/**
 * Parse an extended query string with qs.
 *
 * @return {Object}
 * @private
 */

function parseExtendedQueryString(string_) {
  return qs.parse(string_, {
    allowPrototypes: true
  });
}
```


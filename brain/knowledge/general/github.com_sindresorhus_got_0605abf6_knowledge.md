---
id: github.com-sindresorhus-got-0605abf6-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:22.747034
---

# KNOWLEDGE EXTRACT: github.com_sindresorhus_got_0605abf6
> **Extracted on:** 2026-04-01 12:54:23
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007522111/github.com_sindresorhus_got_0605abf6

---

## File: `.editorconfig`
```
root = true

[*]
indent_style = tab
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.yml]
indent_style = space
indent_size = 2
```

## File: `.gitattributes`
```
* text=auto eol=lf
*.ai binary
```

## File: `.gitignore`
```
node_modules
yarn.lock
coverage
.nyc_output
dist
*.0x
```

## File: `.npmrc`
```
package-lock=false
```

## File: `license`
```
MIT License

Copyright (c) Sindre Sorhus <sindresorhus@gmail.com> (https://sindresorhus.com)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `maintainer.md`
```markdown
# Notes

## Testing

Never use `nock` in tests. nock v14 uses `@mswjs/interceptors` under the hood and auto-activates MSW interceptors for the entire process on import — affecting all HTTP requests, even in tests that don't use nock at all. Use real local test servers via `withServer` / `withServer.exec` instead.
```

## File: `package.json`
```json
{
	"name": "got",
	"version": "14.6.6",
	"description": "Human-friendly and powerful HTTP request library for Node.js",
	"license": "MIT",
	"repository": "sindresorhus/got",
	"funding": "https://github.com/sindresorhus/got?sponsor=1",
	"type": "module",
	"exports": {
		"types": "./dist/source/index.d.ts",
		"default": "./dist/source/index.js"
	},
	"sideEffects": false,
	"engines": {
		"node": ">=22"
	},
	"scripts": {
		"test": "xo && tsc --noEmit && NODE_OPTIONS='--import=tsx/esm' ava",
		"test:coverage": "xo && tsc --noEmit && NODE_OPTIONS='--import=tsx/esm' c8 ava",
		"release": "np",
		"build": "del-cli dist && tsc",
		"prepare": "npm run build"
	},
	"files": [
		"dist/source"
	],
	"keywords": [
		"http",
		"https",
		"http2",
		"get",
		"got",
		"url",
		"uri",
		"request",
		"simple",
		"curl",
		"wget",
		"fetch",
		"net",
		"network",
		"gzip",
		"brotli",
		"zstd",
		"zstandard",
		"requests",
		"human-friendly",
		"axios",
		"superagent",
		"node-fetch",
		"ky"
	],
	"dependencies": {
		"@sindresorhus/is": "^7.2.0",
		"byte-counter": "^0.1.0",
		"cacheable-lookup": "^7.0.0",
		"cacheable-request": "^13.0.18",
		"chunk-data": "^0.1.0",
		"decompress-response": "^10.0.0",
		"http2-wrapper": "^2.2.1",
		"keyv": "^5.6.0",
		"lowercase-keys": "^4.0.1",
		"responselike": "^4.0.2",
		"type-fest": "^5.4.4"
	},
	"devDependencies": {
		"@hapi/bourne": "^3.0.0",
		"@sindresorhus/tsconfig": "^8.1.0",
		"@sinonjs/fake-timers": "^15.1.0",
		"@types/benchmark": "^2.1.5",
		"@types/express": "^5.0.6",
		"@types/node": "^25.3.0",
		"@types/pem": "^1.14.4",
		"@types/readable-stream": "^4.0.23",
		"@types/request": "^2.48.13",
		"@types/sinon": "^21.0.0",
		"@types/sinonjs__fake-timers": "^15.0.1",
		"ava": "^6.4.1",
		"axios": "^1.13.5",
		"benchmark": "^2.1.4",
		"bluebird": "^3.7.2",
		"body-parser": "^2.2.2",
		"c8": "^10.1.3",
		"create-cert": "^1.0.6",
		"create-test-server": "^3.0.1",
		"del-cli": "^7.0.0",
		"delay": "^7.0.0",
		"expect-type": "^1.3.0",
		"express": "^5.2.1",
		"get-stream": "^9.0.1",
		"node-fetch": "^3.3.2",
		"np": "^11.0.2",
		"p-event": "^7.1.0",
		"pem": "^1.14.8",
		"pify": "^6.1.0",
		"quick-lru": "^7.3.0",
		"readable-stream": "^4.7.0",
		"request": "^2.88.2",
		"sinon": "^21.0.1",
		"slow-stream": "0.0.4",
		"tempy": "^3.2.0",
		"then-busboy": "^5.2.1",
		"tough-cookie": "^6.0.0",
		"tsx": "^4.21.0",
		"typescript": "^5.9.3",
		"xo": "^1.2.3"
	},
	"ava": {
		"files": [
			"test/*",
			"!test/*.types.ts"
		],
		"timeout": "10m",
		"extensions": {
			"ts": "module"
		},
		"workerThreads": false
	},
	"c8": {
		"reporter": [
			"text",
			"html",
			"lcov"
		],
		"exclude": [
			"test/**",
			"dist/**"
		]
	},
	"xo": {
		"ignores": [
			"documentation/examples/*"
		],
		"rules": {
			"@typescript-eslint/no-empty-function": "off",
			"n/no-deprecated-api": "off",
			"@typescript-eslint/no-implicit-any-catch": "off",
			"ava/assertion-arguments": "off",
			"@typescript-eslint/no-unsafe-member-access": "off",
			"@typescript-eslint/no-unsafe-return": "off",
			"@typescript-eslint/no-unsafe-assignment": "off",
			"@typescript-eslint/no-unsafe-call": "off",
			"@typescript-eslint/await-thenable": "off",
			"@typescript-eslint/no-redundant-type-constituents": "off",
			"@typescript-eslint/no-unsafe-argument": "off",
			"@typescript-eslint/promise-function-async": "off",
			"no-lone-blocks": "off",
			"unicorn/no-await-expression-member": "off",
			"unicorn/prefer-event-target": "off"
		}
	},
	"runkitExampleFilename": "./documentation/examples/runkit-example.js"
}
```

## File: `readme.md`
```markdown
<div align="center">
	<br>
	<br>
	<img width="360" src="media/logo.svg" alt="Got">
	<br>
	<br>
	<br>
	<br>
	<hr>
	<p>
		<p>
			<sup>
				Sindre's open source work is supported by the community.<br>Special thanks to:
			</sup>
		</p>
		<br>
		<br>
		<a href="https://www.fame.fi#gh-light-mode-only">
			<img src="https://sindresorhus.com/assets/thanks/fame-logo-light.svg" width="200" alt="Fame Helsinki">
		</a>
		<a href="https://www.fame.fi#gh-dark-mode-only">
			<img src="https://sindresorhus.com/assets/thanks/fame-logo-dark.svg" width="200" alt="Fame Helsinki">
		</a>
		<br>
		<br>
		<br>
		<br>
		<a href="https://depot.dev?utm_source=github&utm_medium=sindresorhus">
			<div>
				<picture>
					<source width="180" media="(prefers-color-scheme: dark)" srcset="https://sindresorhus.com/assets/thanks/depot-logo-dark.svg">
					<source width="180" media="(prefers-color-scheme: light)" srcset="https://sindresorhus.com/assets/thanks/depot-logo-light.svg">
					<img width="180" src="https://sindresorhus.com/assets/thanks/depot-logo-light.svg" alt="Depot logo">
				</picture>
			</div>
			<b>Fast remote container builds and GitHub Actions runners.</b>
		</a>
		<br>
		<br>
		<br>
	</p>
	<hr>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
</div>

> Human-friendly and powerful HTTP request library for Node.js

<!-- [![Coverage Status](https://codecov.io/gh/sindresorhus/got/branch/main/graph/badge.svg)](https://codecov.io/gh/sindresorhus/got/branch/main) -->
[![Downloads](https://img.shields.io/npm/dm/got.svg)](https://npmjs.com/got)
[![Install size](https://packagephobia.com/badge?p=got)](https://packagephobia.com/result?p=got)

[See how Got compares to other HTTP libraries](#comparison)

---

**You probably want [Ky](https://github.com/sindresorhus/ky) instead, by the same people. It's smaller, works in the browser too, and is more stable since it's built on [`Fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API). Or [fetch-extras](https://github.com/sindresorhus/fetch-extras) for simple needs.**

---

**Support questions should be asked [here](https://github.com/sindresorhus/got/discussions).**

## Install

```sh
npm install got
```

**Warning:** This package is native [ESM](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules) and no longer provides a CommonJS export. If your project uses CommonJS, you will have to [convert to ESM](https://gist.github.com/sindresorhus/a39789f98801d908bbc7ff3ecc99d99c). Please don't open issues for questions regarding CommonJS / ESM.

**Got v11 is no longer maintained and we will not accept any backport requests.**

## Take a peek

**A [quick start](quick-start.md) guide is available.**

### JSON mode

Got has a dedicated option for handling JSON payload.\
Furthermore, the promise exposes a `.json<T>()` function that returns `Promise<T>`.

```js
import got from 'got';

const {data} = await got.post('https://httpbin.org/anything', {
	json: {
		hello: 'world'
	}
}).json();

console.log(data);
//=> {"hello": "world"}
```

For advanced JSON usage, check out the [`parseJson`](documentation/2-options.md#parsejson) and [`stringifyJson`](documentation/2-options.md#stringifyjson) options.

**For more useful tips like this, visit the [Tips](../../../core/security/QUARANTINE/vetted/repos/hermes_agent/website/docs/guides/tips.md) page.**

## Highlights

- [Used by 10K+ packages and 5M+ repos](https://github.com/sindresorhus/got/network/dependents)
- [Actively maintained](https://github.com/sindresorhus/got/graphs/contributors)
- [Trusted by many companies](#widely-used)

## Documentation

By default, Got will retry on failure. To disable this option, set [`options.retry.limit`](documentation/7-retry.md#retry) to 0.

#### Main API

- [x] [Promise API](documentation/1-promise.md)
- [x] [Options](documentation/2-options.md)
- [x] [Stream API](documentation/3-streams.md)
- [x] [Pagination API](documentation/4-pagination.md)
- [x] [Advanced HTTPS API](documentation/5-https.md)
- [x] [HTTP/2 support](documentation/2-options.md#http2)
- [x] [`Response` class](documentation/3-streams.md#response-2)

#### Timeouts and retries

- [x] [Advanced timeout handling](documentation/6-timeout.md)
- [x] [Retries on failure](documentation/7-retry.md)
- [x] [Errors with metadata](documentation/8-errors.md)

#### Advanced creation

- [x] [Hooks](documentation/9-hooks.md)
- [x] [Instances](documentation/10-instances.md)
- [x] [Progress events & other events](documentation/3-streams.md#events)
- [x] [Plugins](documentation/lets-make-a-plugin.md)
- [x] [Compose](documentation/examples/advanced-creation.js)

#### Cache, Proxy and UNIX sockets

- [x] [RFC compliant caching](../../../core/security/QUARANTINE/vetted/repos/trivy/docs/guide/configuration/cache.md)
- [x] [Proxy support](../../../core/security/QUARANTINE/vetted/repos/hermes_agent/website/docs/guides/tips.md#proxying)
- [x] [Unix Domain Sockets](documentation/2-options.md#enableunixsockets)

#### Integration

- [x] [Diagnostics Channel](documentation/diagnostics-channel.md)
- [x] [TypeScript support](typescript.md)
- [x] [AWS](../../../core/security/QUARANTINE/vetted/repos/hermes_agent/website/docs/guides/tips.md#aws)
- [x] [Testing](../../../core/security/QUARANTINE/vetted/repos/hermes_agent/website/docs/guides/tips.md#testing)

---

### Migration guides

- [Request migration guide](documentation/migration-guides/request.md)
  - [*(Note that Request is unmaintained)*](https://github.com/request/request/issues/3142)
- [Axios](documentation/migration-guides/axios.md)
- [Node.js](nodejs.md)

## Got plugins

- [`got4aws`](https://github.com/SamVerschueren/got4aws) - Got convenience wrapper to interact with AWS v4 signed APIs
- [`gh-got`](https://github.com/sindresorhus/gh-got) - Got convenience wrapper to interact with the GitHub API
- [`gl-got`](https://github.com/singapore/gl-got) - Got convenience wrapper to interact with the GitLab API
- [`gotql`](https://github.com/khaosdoctor/gotql) - Got convenience wrapper to interact with GraphQL using JSON-parsed queries instead of strings
- [`got-fetch`](https://github.com/alexghr/got-fetch) - Got with a [`fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) interface
- [`got-scraping`](https://github.com/apify/got-scraping) - Got wrapper specifically designed for web scraping purposes
- [`got-ssrf`](https://github.com/JaneJeon/got-ssrf) - Got wrapper to protect server-side requests against SSRF attacks

## Comparison

|                       | `got`               | [`node-fetch`][n0]   | [`ky`][k0]               | [`axios`][a0]      | [`superagent`][s0]     |
|-----------------------|:-------------------:|:--------------------:|:------------------------:|:------------------:|:----------------------:|
| HTTP/2 support        | :heavy_check_mark:¹ | :x:                  | :heavy_check_mark:       | :x:                | :heavy_check_mark:\*\* |
| Browser support       | :x:                 | :heavy_check_mark:\* | :heavy_check_mark:       | :heavy_check_mark: | :heavy_check_mark:     |
| Promise API           | :heavy_check_mark:  | :heavy_check_mark:   | :heavy_check_mark:       | :heavy_check_mark: | :heavy_check_mark:     |
| Stream API            | :heavy_check_mark:  | Node.js only         | :x:                      | :x:                | :heavy_check_mark:     |
| Pagination API        | :heavy_check_mark:  | :x:                  | :x:                      | :x:                | :x:                    |
| Request aborting       | :heavy_check_mark:  | :heavy_check_mark:   | :heavy_check_mark:       | :heavy_check_mark: | :heavy_check_mark:     |
| RFC compliant caching | :heavy_check_mark:  | :x:                  | :x:                      | :x:                | :x:                    |
| Cookies (out-of-the-box) | :heavy_check_mark: | :x:                | :x:                      | :x:                | :x:                    |
| Follows redirects     | :heavy_check_mark:  | :heavy_check_mark:   | :heavy_check_mark:       | :heavy_check_mark: | :heavy_check_mark:     |
| Retries on failure    | :heavy_check_mark:  | :x:                  | :heavy_check_mark:       | :x:                | :heavy_check_mark:     |
| Progress events       | :heavy_check_mark:  | :x:                  | :heavy_check_mark: | Browser only       | :heavy_check_mark:     |
| Handles gzip/deflate  | :heavy_check_mark:  | :heavy_check_mark:   | :heavy_check_mark:       | :heavy_check_mark: | :heavy_check_mark:     |
| Advanced timeouts     | :heavy_check_mark:  | :x:                  | :x:                      | :x:                | :x:                    |
| Timings               | :heavy_check_mark:  | :x:                  | :x:                      | :x:                | :x:                    |
| Errors with metadata  | :heavy_check_mark:  | :x:                  | :heavy_check_mark:       | :heavy_check_mark: | :x:                    |
| JSON mode             | :heavy_check_mark:  | :heavy_check_mark:   | :heavy_check_mark:       | :heavy_check_mark: | :heavy_check_mark:     |
| Custom defaults       | :heavy_check_mark:  | :x:                  | :heavy_check_mark:       | :heavy_check_mark: | :x:                    |
| Composable            | :heavy_check_mark:  | :x:                  | :x:                      | :x:                | :heavy_check_mark:     |
| Hooks                 | :heavy_check_mark:  | :x:                  | :heavy_check_mark:       | :heavy_check_mark: | :x:                    |
| Issues open           | [![][gio]][g1]      | [![][nio]][n1]       | [![][kio]][k1]           | [![][aio]][a1]     | [![][sio]][s1]         |
| Issues closed         | [![][gic]][g2]      | [![][nic]][n2]       | [![][kic]][k2]           | [![][aic]][a2]     | [![][sic]][s2]         |
| Downloads             | [![][gd]][g3]       | [![][nd]][n3]        | [![][kd]][k3]            | [![][ad]][a3]      | [![][sd]][s3]          |
| Coverage              | TBD                 | [![][nc]][n4]        | [![][kc]][k4]            | [![][ac]][a4]      | [![][sc]][s4]          |
| Build                 | [![][gb]][g5]       | [![][nb]][n5]        | [![][kb]][k5]            | [![][ab]][a5]      | [![][sb]][s5]          |
| Bugs                  | [![][gbg]][g6]      | [![][nbg]][n6]       | [![][kbg]][k6]           | [![][abg]][a6]     | [![][sbg]][s6]         |
| Dependents            | [![][gdp]][g7]      | [![][ndp]][n7]       | [![][kdp]][k7]           | [![][adp]][a7]     | [![][sdp]][s7]         |
| Install size          | [![][gis]][g8]      | [![][nis]][n8]       | [![][kis]][k8]           | [![][ais]][a8]     | [![][sis]][s8]         |
| GitHub stars          | [![][gs]][g9]       | [![][ns]][n9]        | [![][ks]][k9]            | [![][as]][a9]      | [![][ss]][s9]          |
| TypeScript support    | [![][gts]][g10]     | [![][nts]][n10]      | [![][kts]][k10]          | [![][ats]][a10]    | [![][sts]][s11]        |
| Last commit           | [![][glc]][g11]     | [![][nlc]][n11]      | [![][klc]][k11]          | [![][alc]][a11]    | [![][slc]][s11]        |

\* It's almost API compatible with the browser `fetch` API.\
\*\* Need to switch the protocol manually. Doesn't accept PUSH streams and doesn't reuse HTTP/2 sessions.\
¹ Requires Node.js 15.10.0 or above.\
:sparkle: Almost-stable feature, but the API may change. Don't hesitate to try it out!\
:grey_question: Feature in early stage of development. Very experimental.

<!-- GITHUB -->
[k0]: https://github.com/sindresorhus/ky
[n0]: https://github.com/node-fetch/node-fetch
[a0]: https://github.com/axios/axios
[s0]: https://github.com/visionmedia/superagent

<!-- ISSUES OPEN -->
[gio]: https://img.shields.io/github/issues-raw/sindresorhus/got?color=gray&label
[kio]: https://img.shields.io/github/issues-raw/sindresorhus/ky?color=gray&label
[nio]: https://img.shields.io/github/issues-raw/bitinn/node-fetch?color=gray&label
[aio]: https://img.shields.io/github/issues-raw/axios/axios?color=gray&label
[sio]: https://img.shields.io/github/issues-raw/visionmedia/superagent?color=gray&label

[g1]: https://github.com/sindresorhus/got/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc
[k1]: https://github.com/sindresorhus/ky/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc
[n1]: https://github.com/bitinn/node-fetch/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc
[a1]: https://github.com/axios/axios/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc
[s1]: https://github.com/visionmedia/superagent/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc

<!-- ISSUES CLOSED -->
[gic]: https://img.shields.io/github/issues-closed-raw/sindresorhus/got?color=blue&label
[kic]: https://img.shields.io/github/issues-closed-raw/sindresorhus/ky?color=blue&label
[nic]: https://img.shields.io/github/issues-closed-raw/bitinn/node-fetch?color=blue&label
[aic]: https://img.shields.io/github/issues-closed-raw/axios/axios?color=blue&label
[sic]: https://img.shields.io/github/issues-closed-raw/visionmedia/superagent?color=blue&label

[g2]: https://github.com/sindresorhus/got/issues?q=is%3Aissue+is%3Aclosed+sort%3Aupdated-desc
[k2]: https://github.com/sindresorhus/ky/issues?q=is%3Aissue+is%3Aclosed+sort%3Aupdated-desc
[n2]: https://github.com/bitinn/node-fetch/issues?q=is%3Aissue+is%3Aclosed+sort%3Aupdated-desc
[a2]: https://github.com/axios/axios/issues?q=is%3Aissue+is%3Aclosed+sort%3Aupdated-desc
[s2]: https://github.com/visionmedia/superagent/issues?q=is%3Aissue+is%3Aclosed+sort%3Aupdated-desc

<!-- DOWNLOADS -->
[gd]: https://img.shields.io/npm/dm/got?color=darkgreen&label
[kd]: https://img.shields.io/npm/dm/ky?color=darkgreen&label
[nd]: https://img.shields.io/npm/dm/node-fetch?color=darkgreen&label
[ad]: https://img.shields.io/npm/dm/axios?color=darkgreen&label
[sd]: https://img.shields.io/npm/dm/superagent?color=darkgreen&label

[g3]: https://www.npmjs.com/package/got
[k3]: https://www.npmjs.com/package/ky
[n3]: https://www.npmjs.com/package/node-fetch
[a3]: https://www.npmjs.com/package/axios
[s3]: https://www.npmjs.com/package/superagent

<!-- COVERAGE -->
[gc]: https://img.shields.io/coveralls/github/sindresorhus/got?color=0b9062&label
[kc]: https://img.shields.io/codecov/c/github/sindresorhus/ky?color=0b9062&label
[nc]: https://img.shields.io/coveralls/github/bitinn/node-fetch?color=0b9062&label
[ac]: https://img.shields.io/coveralls/github/mzabriskie/axios?color=0b9062&label
[sc]: https://img.shields.io/codecov/c/github/visionmedia/superagent?color=0b9062&label

[g4]: https://coveralls.io/github/sindresorhus/got
[k4]: https://codecov.io/gh/sindresorhus/ky
[n4]: https://coveralls.io/github/bitinn/node-fetch
[a4]: https://coveralls.io/github/mzabriskie/axios
[s4]: https://codecov.io/gh/visionmedia/superagent

<!-- BUILD -->
[gb]: https://github.com/sindresorhus/got/actions/workflows/main.yml/badge.svg
[kb]: https://github.com/sindresorhus/ky/actions/workflows/main.yml/badge.svg
[nb]: https://img.shields.io/travis/bitinn/node-fetch?label
[ab]: https://img.shields.io/travis/axios/axios?label
[sb]: https://img.shields.io/travis/visionmedia/superagent?label

[g5]: https://github.com/sindresorhus/got/actions/workflows/main.yml
[k5]: https://github.com/sindresorhus/ky/actions/workflows/main.yml
[n5]: https://travis-ci.org/github/bitinn/node-fetch
[a5]: https://travis-ci.org/github/axios/axios
[s5]: https://travis-ci.org/github/visionmedia/superagent

<!-- BUGS -->
[gbg]: https://img.shields.io/github/issues-raw/sindresorhus/got/bug?color=darkred&label
[kbg]: https://img.shields.io/github/issues-raw/sindresorhus/ky/bug?color=darkred&label
[nbg]: https://img.shields.io/github/issues-raw/bitinn/node-fetch/bug?color=darkred&label
[abg]: https://img.shields.io/github/issues-raw/axios/axios/bug-fix?color=darkred&label
[sbg]: https://img.shields.io/github/issues-raw/visionmedia/superagent/Bug?color=darkred&label

[g6]: https://github.com/sindresorhus/got/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc+label%3Abug
[k6]: https://github.com/sindresorhus/ky/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc+label%3Abug
[n6]: https://github.com/bitinn/node-fetch/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc+label%3Abug
[a6]: https://github.com/axios/axios/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc+label%3A%22bug-fix%22
[s6]: https://github.com/visionmedia/superagent/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc+label%3ABug

<!-- DEPENDENTS -->
[gdp]: https://badgen.net/npm/dependents/got?color=orange&label
[kdp]: https://badgen.net/npm/dependents/ky?color=orange&label
[ndp]: https://badgen.net/npm/dependents/node-fetch?color=orange&label
[adp]: https://badgen.net/npm/dependents/axios?color=orange&label
[sdp]: https://badgen.net/npm/dependents/superagent?color=orange&label

[g7]: https://www.npmjs.com/package/got?activeTab=dependents
[k7]: https://www.npmjs.com/package/ky?activeTab=dependents
[n7]: https://www.npmjs.com/package/node-fetch?activeTab=dependents
[a7]: https://www.npmjs.com/package/axios?activeTab=dependents
[s7]: https://www.npmjs.com/package/visionmedia?activeTab=dependents

<!-- INSTALL SIZE -->
[gis]: https://packagephobia.com/badge?p=got
[kis]: https://packagephobia.com/badge?p=ky
[nis]: https://packagephobia.com/badge?p=node-fetch
[ais]: https://packagephobia.com/badge?p=axios
[sis]: https://packagephobia.com/badge?p=superagent

[g8]: https://packagephobia.com/result?p=got
[k8]: https://packagephobia.com/result?p=ky
[n8]: https://packagephobia.com/result?p=node-fetch
[a8]: https://packagephobia.com/result?p=axios
[s8]: https://packagephobia.com/result?p=superagent

<!-- GITHUB STARS -->
[gs]: https://img.shields.io/github/stars/sindresorhus/got?color=white&label
[ks]: https://img.shields.io/github/stars/sindresorhus/ky?color=white&label
[ns]: https://img.shields.io/github/stars/bitinn/node-fetch?color=white&label
[as]: https://img.shields.io/github/stars/axios/axios?color=white&label
[ss]: https://img.shields.io/github/stars/visionmedia/superagent?color=white&label

[g9]: https://github.com/sindresorhus/got
[k9]: https://github.com/sindresorhus/ky
[n9]: https://github.com/node-fetch/node-fetch
[a9]: https://github.com/axios/axios
[s9]: https://github.com/visionmedia/superagent

<!-- TYPESCRIPT SUPPORT -->
[gts]: https://badgen.net/npm/types/got?label
[kts]: https://badgen.net/npm/types/ky?label
[nts]: https://badgen.net/npm/types/node-fetch?label
[ats]: https://badgen.net/npm/types/axios?label
[sts]: https://badgen.net/npm/types/superagent?label

[g10]: https://github.com/sindresorhus/got
[k10]: https://github.com/sindresorhus/ky
[n10]: https://github.com/node-fetch/node-fetch
[a10]: https://github.com/axios/axios
[s10]: https://github.com/visionmedia/superagent

<!-- LAST COMMIT -->
[glc]: https://img.shields.io/github/last-commit/sindresorhus/got?color=gray&label
[klc]: https://img.shields.io/github/last-commit/sindresorhus/ky?color=gray&label
[nlc]: https://img.shields.io/github/last-commit/bitinn/node-fetch?color=gray&label
[alc]: https://img.shields.io/github/last-commit/axios/axios?color=gray&label
[slc]: https://img.shields.io/github/last-commit/visionmedia/superagent?color=gray&label

[g11]: https://github.com/sindresorhus/got/commits
[k11]: https://github.com/sindresorhus/ky/commits
[n11]: https://github.com/node-fetch/node-fetch/commits
[a11]: https://github.com/axios/axios/commits
[s11]: https://github.com/visionmedia/superagent/commits

[Click here][InstallSizeOfTheDependencies] to see the install size of the Got dependencies.

[InstallSizeOfTheDependencies]: https://packagephobia.com/result?p=@sindresorhus/is@7.2.0,byte-counter@0.1.0,cacheable-lookup@7.0.0,cacheable-request@13.0.18,chunk-data@0.1.0,decompress-response@10.0.0,http2-wrapper@2.2.1,keyv@5.6.0,lowercase-keys@4.0.1,responselike@4.0.2,type-fest@5.4.4

## Maintainers

[![Sindre Sorhus](https://github.com/sindresorhus.png?size=100)](https://sindresorhus.com) | [![Szymon Marczak](https://github.com/szmarczak.png?size=100)](https://github.com/szmarczak)
---|---
[Sindre Sorhus](https://sindresorhus.com) | [Szymon Marczak](https://github.com/szmarczak)

<a name="widely-used"></a>
## These amazing companies are using Got

<table>
<tbody>
	<tr>
		<td align="center">
			<a href="https://segment.com">
				<img width="90" valign="middle" src="https://user-images.githubusercontent.com/697676/47693700-ddb62500-dbb7-11e8-8332-716a91010c2d.png">
			</a>
		</td>
		<td align="center">
			<a href="https://antora.org">
				<img width="100" valign="middle" src="https://user-images.githubusercontent.com/79351/47706840-d874cc80-dbef-11e8-87c6-5f0c60cbf5dc.png">
			</a>
		</td>
		<td align="center">
			<a href="https://getvoip.com">
				<img width="150" valign="middle" src="https://user-images.githubusercontent.com/10832620/47869404-429e9480-dddd-11e8-8a7a-ca43d7f06020.png">
			</a>
		</td>
		<td align="center">
			<a href="https://github.com/exoframejs/exoframe">
				<img width="150" valign="middle" src="https://user-images.githubusercontent.com/365944/47791460-11a95b80-dd1a-11e8-9070-e8f2a215e03a.png">
			</a>
		</td>
	</tr>
	<tr>
		<td align="center">
			<a href="http://karaokes.moe">
				<img width="140" valign="middle" src="https://karaokes.moe/assets/images/index.png">
			</a>
		</td>
		<td align="center">
			<a href="https://github.com/renovatebot/renovate">
				<img width="150" valign="middle" src="https://avatars.githubusercontent.com/u/38656520?s=200&v=4">
			</a>
		</td>
		<td align="center">
			<a href="https://resist.bot">
				<img width="150" valign="middle" src="https://user-images.githubusercontent.com/3322287/51992724-28736180-2473-11e9-9764-599cfda4b012.png">
			</a>
		</td>
		<td align="center">
			<a href="https://www.naturalcycles.com">
				<img width="150" valign="middle" src="https://user-images.githubusercontent.com/170270/92244143-d0a8a200-eec2-11ea-9fc0-1c07f90b2113.png">
			</a>
		</td>
	</tr>
	<tr>
		<td align="center">
			<a href="https://microlink.io">
				<img width="150" valign="middle" src="https://user-images.githubusercontent.com/36894700/91992974-1cc5dc00-ed35-11ea-9d04-f58b42ce6a5e.png">
			</a>
		</td>
		<td align="center">
			<a href="https://radity.com">
				<img width="150" valign="middle" src="https://user-images.githubusercontent.com/29518613/91814036-97fb9500-ec44-11ea-8c6c-d198cc23ca29.png">
			</a>
		</td>
	</tr>
</tbody>
</table>

<!-- <br> -->

<!-- *Creating an awesome product? Open an issue to get listed here.* -->

<br>

> Segment is a happy user of Got! Got powers the main backend API that our app talks to. It's used by our in-house RPC client that we use to communicate with all microservices.
>
> — <a href="https://github.com/vadimdemedes">Vadim Demedes</a>

> Antora, a static site generator for creating documentation sites, uses Got to download the UI bundle. In Antora, the UI bundle (aka theme) is maintained as a separate project. That project exports the UI as a zip file we call the UI bundle. The main site generator downloads that UI from a URL using Got and streams it to vinyl-zip to extract the files. Those files go on to be used to create the HTML pages and supporting assets.
>
> — <a href="https://github.com/mojavelinux">Dan Allen</a>

> GetVoIP is happily using Got in production. One of the unique capabilities of Got is the ability to handle Unix sockets which enables us to build a full control interfaces for our docker stack.
>
> — <a href="https://github.com/danielkalen">Daniel Kalen</a>

> We're using Got inside of Exoframe to handle all the communication between CLI and server. Exoframe is a self-hosted tool that allows simple one-command deployments using Docker.
>
> — <a href="https://github.com/yamalight">Tim Ermilov</a>

> Karaoke Mugen uses Got to fetch content updates from its online server.
>
> — <a href="https://github.com/AxelTerizaki">Axel Terizaki</a>

> Renovate uses Got, gh-got and gl-got to send millions of queries per day to GitHub, GitLab, npmjs, PyPi, Packagist, Docker Hub, Terraform, CircleCI, and more.
>
> — <a href="https://github.com/rarkins">Rhys Arkins</a>

> Resistbot uses Got to communicate from the API frontend where all correspondence ingresses to the officials lookup database in back.
>
> — <a href="https://github.com/chris-erickson">Chris Erickson</a>

> Natural Cycles is using Got to communicate with all kinds of 3rd-party REST APIs (over 9000!).
>
> — <a href="https://github.com/kirillgroshkov">Kirill Groshkov</a>

> Microlink is a cloud browser as an API service that uses Got widely as the main HTTP client, serving ~22M requests a month, every time a network call needs to be performed.
>
> — <a href="https://github.com/Kikobeats">Kiko Beats</a>

> We’re using Got at Radity. Thanks for such an amazing work!
>
> — <a href="https://github.com/MirzayevFarid">Mirzayev Farid</a>
```

## File: `tsconfig.json`
```json
{
	"extends": "@sindresorhus/tsconfig",
	"compilerOptions": {
		"outDir": "dist",
		"target": "es2024", // Node.js 22
		"lib": [
			"es2024",
			"esnext.array"
		],
		"noPropertyAccessFromIndexSignature": false,
		"isolatedModules": true
	},
	"include": [
		"source",
		"test",
		"benchmark"
	]
}
```

## File: `benchmark/index.ts`
```typescript
import https from 'node:https';
/// import axios from 'axios';
import Benchmark from 'benchmark';
import fetch from 'node-fetch';
import request from 'request';
import got from '../source/index.js';
import Request from '../source/core/index.js';
import Options, {type OptionsInit} from '../source/core/options.js';

// Configuration
const httpsAgent = new https.Agent({
	keepAlive: true,
	rejectUnauthorized: false,
});

const url = new URL('https://127.0.0.1:8081');
const urlString = url.toString();

const gotOptions: OptionsInit = {
	agent: {
		https: httpsAgent,
	},
	https: {
		rejectUnauthorized: false,
	},
	retry: {
		limit: 0,
	},
};

const normalizedGotOptions = new Options(url, gotOptions);

const requestOptions = {
	// eslint-disable-next-line @typescript-eslint/naming-convention
	strictSSL: false,
	agent: httpsAgent,
};

const fetchOptions = {
	agent: httpsAgent,
};

/// const axiosOptions = {
// 	url: urlString,
// 	httpsAgent,
// 	https: {
// 		rejectUnauthorized: false,
// 	},
// };

// const axiosStreamOptions: typeof axiosOptions & {responseType: 'stream'} = {
// 	...axiosOptions,
// 	responseType: 'stream',
// };

const httpsOptions = {
	https: {
		rejectUnauthorized: false,
	},
	agent: httpsAgent,
};

const suite = new Benchmark.Suite();

// Benchmarking
suite.add('got - promise', {
	defer: true,
	async fn(deferred: {resolve: () => void}) {
		await got(url, gotOptions);
		deferred.resolve();
	},
}).add('got - stream', {
	defer: true,
	async fn(deferred: {resolve: () => void}) {
		got.stream(url, gotOptions).resume().once('end', () => {
			deferred.resolve();
		});
	},
}).add('got - core', {
	defer: true,
	async fn(deferred: {resolve: () => void}) {
		const stream = new Request(url, gotOptions);
		void stream.flush();
		stream.resume().once('end', () => {
			deferred.resolve();
		});
	},
}).add('got - core - normalized options', {
	defer: true,
	async fn(deferred: {resolve: () => void}) {
		const stream = new Request(undefined, undefined, normalizedGotOptions);
		void stream.flush();
		stream.resume().once('end', () => {
			deferred.resolve();
		});
	},
}).add('request - callback', {
	defer: true,
	fn(deferred: {resolve: () => void}) {
		request(urlString, requestOptions, (error: Error) => {
			if (error) {
				throw error;
			}

			deferred.resolve();
		});
	},
}).add('request - stream', {
	defer: true,
	fn(deferred: {resolve: () => void}) {
		const stream = request(urlString, requestOptions);
		stream.resume();
		stream.once('end', () => {
			deferred.resolve();
		});
	},
}).add('node-fetch - promise', {
	defer: true,
	async fn(deferred: {resolve: () => void}) {
		const response = await fetch(urlString, fetchOptions);
		await response.text();

		deferred.resolve();
	},
}).add('node-fetch - stream', {
	defer: true,
	async fn(deferred: {resolve: () => void}) {
		const {body} = await fetch(urlString, fetchOptions);

		body!.resume();
		body!.once('end', () => {
			deferred.resolve();
		});
	},
}).add('axios - promise', {
	defer: true,
	async fn(deferred: {resolve: () => void}) {
		// Disabled until it has correct types.
		// await axios.request(axiosOptions);
		deferred.resolve();
	},
}).add('axios - stream', {
	defer: true,
	async fn(deferred: {resolve: () => void}) {
		// Disabled until it has correct types.
		// const result = await axios.request(axiosStreamOptions);
		// const {data}: any = result;

		// data.resume();
		// data.once('end', () => {
		// 	deferred.resolve();
		// });

		deferred.resolve();
	},
}).add('https - stream', {
	defer: true,
	fn(deferred: {resolve: () => void}) {
		https.request(urlString, httpsOptions, response => {
			response.resume();
			response.once('end', () => {
				deferred.resolve();
			});
		}).end();
	},
}).on('cycle', (event: Benchmark.Event) => {
	// eslint-disable-next-line @typescript-eslint/no-base-to-string
	console.log(event.target.toString());
}).on('complete', function (this: any) {
	console.log(`Fastest is ${this.filter('fastest').map('name') as string}`);

	internalBenchmark();
}).run();

const internalBenchmark = (): void => {
	console.log();

	const internalSuite = new Benchmark.Suite();
	internalSuite.add('got - normalize options', {
		fn() {
			// eslint-disable-next-line no-new
			new Options(url, gotOptions);
		},
	}).on('cycle', (event: Benchmark.Event) => {
		// eslint-disable-next-line @typescript-eslint/no-base-to-string
		console.log(event.target.toString());
	});

	internalSuite.run();
};

// Results (i7-7700k, CPU governor: performance):

// H2O server:
// got - promise                   x 2,846 ops/sec ±3.71% (74 runs sampled)
// got - stream                    x 3,840 ops/sec ±1.97% (83 runs sampled)
// got - core                      x 3,929 ops/sec ±2.31% (83 runs sampled)
// got - core - normalized options x 4,483 ops/sec ±2.25% (80 runs sampled)
// request - callback              x 4,784 ops/sec ±4.25% (77 runs sampled)
// request - stream                x 5,138 ops/sec ±2.10% (80 runs sampled)
// node-fetch - promise            x 6,693 ops/sec ±4.56% (77 runs sampled)
// node-fetch - stream             x 7,332 ops/sec ±3.22% (80 runs sampled)
// axios - promise                 x 5,365 ops/sec ±4.30% (74 runs sampled)
// axios - stream                  x 7,424 ops/sec ±3.09% (80 runs sampled)
// https - stream                  x 8,850 ops/sec ±2.77% (71 runs sampled)
// Fastest is https - stream

// got - normalize options         x 73,484 ops/sec ±0.85% (95 runs sampled)
```

## File: `benchmark/server.ts`
```typescript
import type {AddressInfo} from 'node:net';
import https from 'node:https';
// @ts-expect-error No types
import createCert from 'create-cert';

const keys = await createCert({days: 365, commonName: 'localhost'});

const server = https.createServer(keys, (_request, response) => {
	response.end('ok');
}).listen(8080, () => {
	const {port} = server.address() as AddressInfo;
	console.log(`Listening at https://localhost:${port}`);
});
```

## File: `documentation/1-promise.md`
```markdown
[> Back to homepage](../../../README.md#documentation)

## Promise API

Source code: [`source/as-promise/index.ts`](../source/as-promise/index.ts)

The main Got function returns a [`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise).\
Request aborting is supported via the [`signal` option](2-options.md#signal) and [`AbortController`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController).

### <code>got(url: string | URL, options?: [OptionsInit](typescript.md#optionsinit), defaults?: [Options](2-options.md))</code>

**Returns: <code>Promise<[Response](response.md)></code>**

The most common way is to pass the URL as the first argument, then the options as the second.

```js
import got from 'got';

const {headers} = await got(
	'https://httpbin.org/anything',
	{
		headers: {
			foo: 'bar'
		}
	}
).json();
```

### `promise.json<T>()`

**Returns: `Promise<T>`**

A shortcut method that gives a Promise returning a JSON object.

It is semantically the same as setting [`options.resolveBodyOnly`](2-options.md#resolvebodyonly) to `true` and [`options.responseType`](2-options.md#responsetype) to `'json'`.

### `promise.buffer()`

**Returns: `Promise<Uint8Array>`**

A shortcut method that gives a Promise returning a [Uint8Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array).

It is semantically the same as setting [`options.resolveBodyOnly`](2-options.md#resolvebodyonly) to `true` and [`options.responseType`](2-options.md#responsetype) to `'buffer'`.

### `promise.text()`

**Returns: `Promise<string>`**

A shortcut method that gives a Promise returning a string.

It is semantically the same as setting [`options.resolveBodyOnly`](2-options.md#resolvebodyonly) to `true` and [`options.responseType`](2-options.md#responsetype) to `'text'`.

### `promise.on(event, handler)`

The events are the same as in [Stream API](3-streams.md#events).

### `promise.once(event, handler)`

Registers a one-time listener for events from [Stream API](3-streams.md#events).

### `promise.off(event, handler)`

Removes listener registered with [`promise.on`](1-promise.md#promiseonevent-handler).

```js
import {createReadStream} from 'node:fs';
import got from 'got';

const ongoingRequestPromise = got.post(uploadUrl, {
    body: createReadStream('sample.txt')
});

const eventListener = (progress: Progress) => {
    console.log(progress);
};

ongoingRequestPromise.on('uploadProgress', eventListener);

setTimeout(() => {
    ongoingRequestPromise.off('uploadProgress', eventListener);
}, 500);

await ongoingRequestPromise;
```
```

## File: `documentation/10-instances.md`
```markdown
[> Back to homepage](../../../README.md#documentation)

## Instances

Source code: [`source/create.ts`](../source/create.ts)

### `got.defaults`

#### `options`

**Type: [`Options`](2-options.md)**

The options used for this instance.

#### `handlers`

**Type: [`Handler[]`](typescript.md#handler)**

```ts
(options: Options, next: …) => next(options)
```

An array of handlers. The `next` function returns a [`Promise`](1-promise.md) or a [`Request` Got stream](3-streams.md).

You execute them directly by calling `got(…)`. They are some sort of "global hooks" - these functions are called first. The last handler (it's invisible) is either `asPromise` or `asStream`, depending on whether `got()` or `got.stream()` was called.

#### `mutableDefaults`

**Type: `boolean`**\
**Default: `false`**

Determines whether `got.defaults.options` can be modified.

### `got.extend(…options, …instances)`

**Tip:**
> - `options` can include `handlers` and `mutableDefaults`.

**Note:**
> - Properties that are not enumerable, such as `body`, `json`, and `form`, will not be merged.

Configure a new `got` instance with merged default options. The options are merged with the parent instance's `defaults.options` using [`options.merge(…)`](2-options.md#merge).

```js
import got from 'got';

const client = got.extend({
	prefixUrl: 'https://httpbin.org',
	headers: {
		'x-foo': 'bar'
	}
});

const {headers} = await client.get('headers').json();
console.log(headers['x-foo']); //=> 'bar'

const jsonClient = client.extend({
	responseType: 'json',
	resolveBodyOnly: true,
	headers: {
		'x-lorem': 'impsum'
	}
});

const {headers: headers2} = await jsonClient.get('headers');
console.log(headers2['x-foo']);   //=> 'bar'
console.log(headers2['x-lorem']); //=> 'impsum'
```

**Note:**
> - Handlers can be asynchronous and can return a `Promise`, but never a `Promise<Stream>` when `options.isStream` is `true` (set internally for `got.stream()` requests).
> - Streams must always be handled synchronously.
> - In order to perform async work using streams, the `beforeRequest` hook should be used instead.

The recommended approach for creating handlers that can handle both promises and streams is:

```js
import got from 'got';

// Create a non-async handler, but we can return a Promise later.
const handler = (options, next) => {
	// Internally set for requests created via `got.stream()`.
	if (options.isStream) {
		// It's a Stream, return synchronously.
		return next(options);
	}

	// For asynchronous work, return a Promise.
	return (async () => {
		try {
			const response = await next(options);
			response.yourOwnProperty = true;
			return response;
		} catch (error) {
			// Every error will be replaced by this one.
			// Before you receive any error here,
			// it will be passed to the `beforeError` hooks first.
			// Note: this one won't be passed to `beforeError` hook. It's final.
			throw new Error('Your very own error.');
		}
	})();
};

const instance = got.extend({handlers: [handler]});
```
```

## File: `documentation/2-options.md`
```markdown
[> Back to homepage](../../../README.md#documentation)

## Options

Source code: [`source/core/options.ts`](../source/core/options.ts)

Like `fetch` stores the options in a `Request` instance, Got does so in `Options`.\
It is made of getters and setters that provide fast option normalization and validation.

**By default, Got will retry on failure. To disable this option, set [`options.retry`](7-retry.md) to `{limit: 0}`.**

#### Merge behavior explained

When an option is already set, setting it again replaces it with a deep clone by default.\
Otherwise the merge behavior is documented in the corresponding section for the option.

#### How to store options

The `Options` class is useful for storing and validating configuration for Got instances.

The constructor - `new Options(url, options, defaults)` - takes the same arguments as the `got` function.

To use an `Options` instance, create an extended Got instance:

```js
import got, {Options} from 'got';

const options = new Options({
	prefixUrl: 'https://httpbin.org',
	headers: {
		foo: 'foo'
	}
});

options.headers.foo = 'bar';

// Use got.extend() to create an instance with the Options
const instance = got.extend(options);

const {headers} = await instance('anything').json();
console.log(headers.foo);
//=> 'bar'
```

For most use cases, plain objects are simpler and more convenient:

```js
import got from 'got';

const options = {
	prefixUrl: 'https://httpbin.org',
	headers: {
		foo: 'foo'
	}
};

options.headers.foo = 'bar';

// Plain objects can be passed directly as the second argument
const {headers} = await got('anything', options).json();
console.log(headers.foo);
//=> 'bar'
```

Note that the `Options` constructor throws immediately when an invalid option is provided, such as a non-existing option or a typo. With plain objects, validation only happens when the request is made.

For TypeScript users, `got` exports a dedicated type called `OptionsInit`.\
It is a plain object that can store the same properties as `Options`.

The `Options` class is useful for storing the base configuration of a custom Got client, especially when you want early validation of options.

#### Resetting options

Unlike Got 11, explicitly specifying `undefined` no longer keeps the parent value.\
In order to keep the parent value, you must not set an option to `undefined`.\
Doing so will reset those values:

```js
instance(…, {searchParams: undefined});
instance(…, {cookieJar: undefined});
instance(…, {responseType: undefined});
instance(…, {prefixUrl: ''});
instance(…, {agent: {http: undefined, https: undefined, http2: undefined}});
instance(…, {context: {token: undefined, …}});
instance(…, {https: {rejectUnauthorized: undefined, …}});
instance(…, {cacheOptions: {immutableMinTimeToLive: undefined, …}});
instance(…, {headers: {'user-agent': undefined, …}});
instance(…, {timeout: {request: undefined, …}});
```

In order to reset `hooks`, `retry` and `pagination`, another Got instance must be created:

```js
const defaults = new Options();

const secondInstance = instance.extend({mutableDefaults: true});
secondInstance.defaults.options.hooks = defaults.hooks;
secondInstance.defaults.options.retry = defaults.retry;
secondInstance.defaults.options.pagination = defaults.pagination;
```

### `url`

**Type: <code>string | [URL](https://nodejs.org/api/url.html#url_the_whatwg_url_api)</code>**

The URL to request. Usually the `url` represents a [WHATWG URL](https://url.spec.whatwg.org/#url-class).
Pass it as the first argument to `got(url, options)`. Passing `url` in an options object is not supported.

```js
import got from 'got';

// This:
await got('https://httpbin.org/anything');

// is semantically the same as this:
await got(new URL('https://httpbin.org/anything'));
```

#### **Note:**
> - Throws if no protocol specified.

#### **Note:**
> - If `url` is a string, then the `query` string will **not** be parsed as search params.\
>  This is in accordance to [the specification](https://datatracker.ietf.org/doc/html/rfc7230#section-2.7).\
>  If you want to pass search params instead, use the `searchParams` option below.

```js
import got from 'got';

await got('https://httpbin.org/anything?query=a b'); //=> ?query=a%20b
await got('https://httpbin.org/anything', {searchParams: {query: 'a b'}}); //=> ?query=a+b

// The query string is overridden by `searchParams`
await got('https://httpbin.org/anything?query=a b', {searchParams: {query: 'a b'}}); //=> ?query=a+b
```

#### **Note:**
> - Leading slashes are disallowed to enforce consistency and avoid confusion.\
>  For example, when the prefix URL is `https://example.com/foo` and the input is `/bar`, there's ambiguity whether the resulting URL would become `https://example.com/foo/bar` or `https://example.com/bar`. The latter is used by browsers.

### `searchParams`

**Type: <code>string | [URLSearchParams](https://nodejs.org/api/url.html#url_class_urlsearchparams) | object&lt;string, [Primitive](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)&gt;</code>**

[WHATWG URL Search Params](https://url.spec.whatwg.org/#interface-urlsearchparams) to be added to the request URL.

```js
import got from 'got';

const response = await got('https://httpbin.org/anything', {
	searchParams: {
		hello: 'world',
		foo: 123
	}
}).json();

console.log(response.args);
//=> {hello: 'world', foo: 123}
```

If you need to pass an array, you can do it using a `URLSearchParams` instance:

```js
import got from 'got';

const searchParams = new URLSearchParams([['key', 'a'], ['key', 'b']]);

await got('https://httpbin.org/anything', {searchParams});

console.log(searchParams.toString());
//=> 'key=a&key=b'
```

#### **Note:**
> - This will override the `query` string in `url`.

#### **Note:**
> - `null` values are not stringified, an empty string is used instead.
> - `undefined` values will clear the original keys.

#### **Merge behavior:**
> - Overrides existing properties.

### `prefixUrl`

**Type: `string`**\
**Default: `''`**

The string to be prepended to `url`.

The prefix can be any valid URL, either relative or [absolute](https://url.spec.whatwg.org/#absolute-url-string).
A trailing slash `/` is optional - one will be added automatically.

```js
import got from 'got';

// This:
const instance = got.extend({prefixUrl: 'https://httpbin.org'});
await instance('anything');

// is semantically the same as this:
await got('https://httpbin.org/anything');
```

#### **Note:**
> - Changing `prefixUrl` also updates the `url` option if set.

#### **Note:**
> - If you're passing an absolute URL as `url`, you need to set `prefixUrl` to an empty string.

### `signal`

**Type: [`AbortSignal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal)**

You can abort the `request` using [`AbortController`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController).

```js
import got from 'got';

const abortController = new AbortController();

const request = got('https://httpbin.org/anything', {
	signal: abortController.signal
});

setTimeout(() => {
	abortController.abort();
}, 100);
```

### `method`

**Type: `string`**\
**Default: `GET`**

The [HTTP method](https://datatracker.ietf.org/doc/html/rfc7231#section-4) used to make the request.\
The most common methods are: `GET`, `HEAD`, `POST`, `PUT`, `DELETE`.

```js
import got from 'got';

const {method} = await got('https://httpbin.org/anything', {
	method: 'POST'
}).json();

console.log(method);
// => 'POST'
```

### `headers`

**Type: `object<string, string>`**\
**Default: `{}`**

The [HTTP headers](https://datatracker.ietf.org/doc/html/rfc7231#section-8.3) to be sent. Headers set to `undefined` will be omitted.

```js
import got from 'got';

const {headers} = await got.post('https://httpbin.org/anything', {
	headers: {
		hello: 'world'
	}
}).json();

console.log(headers);
// => {hello: 'world'}
```

#### **Merge behavior:**
> - Overrides existing properties.

### `body`

**Type: `string | Uint8Array | TypedArray | stream.Readable | Generator | AsyncGenerator | Iterable | AsyncIterable | FormData`**

The payload to send.

For `string`, `Uint8Array`, and `TypedArray` types, the `content-length` header is automatically set if the `content-length` and `transfer-encoding` headers are missing.

**The `content-length` header is not automatically set when `body` is an instance of [`fs.createReadStream()`](https://nodejs.org/api/fs.html#fs_fs_createreadstream_path_options).**

To set `content-length` for file streams, you need to manually provide it using `fs.promises.stat()`:

```js
import fs from 'node:fs';
import fsPromises from 'node:fs/promises';
import got from 'got';

const filePath = 'path/to/file';
const fileStats = await fsPromises.stat(filePath);
const fileStream = fs.createReadStream(filePath);

await got.post('https://httpbin.org/anything', {
	body: fileStream,
	headers: {
		'content-length': fileStats.size.toString()
	}
});
```

```js
import got from 'got';

const {data} = await got.post('https://httpbin.org/anything', {
	body: 'Hello, world!'
}).json();

console.log(data);
//=> 'Hello, world!'
```

You can also use typed arrays (Uint8Array, Uint16Array, etc.) as request body:

```js
import got from 'got';

const uint8Body = new Uint8Array([104, 101, 108, 108, 111]); // 'hello' in ASCII

const {data} = await got.post('https://httpbin.org/anything', {
	body: uint8Body
}).json();

console.log(data);
//=> 'hello'
```

You can use `Iterable` and `AsyncIterable` objects as request body, including Web [`ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream):

```js
import got from 'got';

// Using an async generator
async function* generateData() {
	yield 'Hello, ';
	yield 'world!';
}

await got.post('https://httpbin.org/anything', {
	body: generateData()
});
```

You can use [`FormData`](https://developer.mozilla.org/en-US/docs/Web/API/FormData) objects as request body:

```js
import got from 'got';

const form = new FormData();
form.set('greeting', 'Hello, world!');

const data = await got.post('https://httpbin.org/post', {
	body: form
}).json();

console.log(data.form.greeting);
//=> 'Hello, world!'
```

#### **Note:**
> - If `body` is specified, then the `json` or `form` option cannot be used.

#### **Note:**
> - If you use this option, `got.stream()` will be read-only.

#### **Note:**
> - Passing `body` with `GET` will throw unless the [`allowGetBody` option](#allowgetbody) is set to `true`.

#### **Note:**
> - This option is not enumerable and will not be merged with the instance defaults.

### `json`

**Type: JSON-serializable values**

JSON **request** body. If set, the `content-type` header defaults to `application/json`.

> [!IMPORTANT]
> This option only affects the **request body** you send to the server. To parse the **response** as JSON, you must either call `.json()` on the promise or set [`responseType: 'json'`](#responsetype) in the options.

```js
import got from 'got';

const {data} = await got.post('https://httpbin.org/anything', {
	json: {
		hello: 'world'
	}
}).json();

console.log(data);
//=> `{hello: 'world'}`
```

### `form`

**Type: <code>object&lt;string, [Primitive](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)&gt;</code>**

The form body is converted to a query string using `(new URLSearchParams(form)).toString()`.

If set, the `content-type` header defaults to [`application/x-www-form-urlencoded`](https://url.spec.whatwg.org/#application/x-www-form-urlencoded).

```js
import got from 'got';

const {data} = await got.post('https://httpbin.org/anything', {
	form: {
		hello: 'world'
	}
}).json();

console.log(data);
//=> 'hello=world'
```

### `parseJson`

**Type: `(text: string) => unknown`**\
**Default: `(text: string) => JSON.parse(text)`**

The function used to parse JSON responses.

```js
import got from 'got';
import Bourne from '@hapi/bourne';

// Preventing prototype pollution by using Bourne
const parsed = await got('https://example.com', {
	parseJson: text => Bourne.parse(text)
}).json();

console.log(parsed);
```

### `stringifyJson`

**Type: `(object: unknown) => string`**\
**Default: `(object: unknown) => JSON.stringify(object)`**

The function used to stringify the body of JSON requests.

**Example: ignore all properties starting with an underscore**

```js
import got from 'got';

await got.post('https://example.com', {
	stringifyJson: object => JSON.stringify(object, (key, value) => {
		if (key.startsWith('_')) {
			return;
		}

		return value;
	}),
	json: {
		some: 'payload',
		_ignoreMe: 1234
	}
});
```

**Example: all numbers as strings**

```js
import got from 'got';

await got.post('https://example.com', {
	stringifyJson: object => JSON.stringify(object, (key, value) => {
		if (typeof value === 'number') {
			return value.toString();
		}

		return value;
	}),
	json: {
		some: 'payload',
		number: 1
	}
});
```

### `allowGetBody`

**Type: `boolean`**\
**Default: `false`**

Set this to `true` to allow sending body for the `GET` method.

However, the [HTTP/2 specification](https://datatracker.ietf.org/doc/html/rfc7540#section-8.1.3) says:

> An HTTP GET request includes request header fields and no payload body

Therefore this option has no effect when using HTTP/2.

#### **Note:**
> - This option is only meant to interact with non-compliant servers when you have no other choice.

#### **Note:**
> - The [RFC 7231](https://tools.ietf.org/html/rfc7231#section-4.3.1) doesn't specify any particular behavior for the GET method having a payload, therefore it's considered an [**anti-pattern**](https://en.wikipedia.org/wiki/Anti-pattern).

### `copyPipedHeaders`

**Type: `boolean`**\
**Default: `false`**

Automatically copy headers from piped streams.

When piping a request into a Got stream (e.g., `request.pipe(got.stream(url))`), this controls whether headers from the source stream are automatically merged into the Got request headers.

**Note:** Explicitly set headers take precedence over piped headers. Piped headers are only copied when a header is not already explicitly set.

Useful for proxy scenarios when explicitly enabled, but you may still want to filter out headers like `Host`, `Connection`, `Authorization`, etc.

**Example: Opt in to automatic header copying for proxy scenarios**

```js
import got from 'got';
import {pipeline} from 'node:stream/promises';

server.get('/proxy', async (request, response) => {
	const gotStream = got.stream('https://example.com', {
		copyPipedHeaders: true,
		// Explicit headers win over piped headers
		headers: {
			host: 'example.com',
		}
	});

	await pipeline(request, gotStream, response);
});
```

**Example: Keep it disabled and manually copy only safe headers**

```js
import got from 'got';
import {pipeline} from 'node:stream/promises';

server.get('/proxy', async (request, response) => {
	const gotStream = got.stream('https://example.com', {
		headers: {
			'user-agent': request.headers['user-agent'],
			'accept': request.headers['accept'],
			// Explicitly NOT copying host, connection, authorization, etc.
		}
	});

	await pipeline(request, gotStream, response);
});
```

### `timeout`

**Type: `object`**

See the [Timeout API](6-timeout.md).

#### **Merge behavior:**
> - Overrides existing properties.

### `retry`

**Type: `object`**

See the [Retry API](7-retry.md).

#### **Merge behavior:**
> - Overrides existing properties.

### `hooks`

**Type: `object`**

See the [Hooks API](9-hooks.md).

#### **Merge behavior:**
> - Merges arrays via `[...hooksArray, ...next]`

### `encoding`

**Type: `string`**\
**Default: `'utf8'`**

[Encoding](https://nodejs.org/api/buffer.html#buffer_buffers_and_character_encodings) to be used on [`setEncoding`](https://nodejs.org/api/stream.html#stream_readable_setencoding_encoding) of the response data.

To get a [`Uint8Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array), you need to set `responseType` to `'buffer'` instead. Don't set this option to `null`.

```js
import got from 'got';

const response = await got('https://httpbin.org/anything', {
	encoding: 'base64'
}).text();

console.log(response);
//=> base64 string
```

#### **Note:**
> - This option does not affect streams! Instead, do:

```js
import got from 'got';

const stream = got.stream('https://httpbin.org/anything');

stream.setEncoding('base64');
stream.on('data', console.log);
```

### `responseType`

**Type: `'text' | 'json' | 'buffer'`**\
**Default: `'text'`**

The parsing method.

The promise also has `.text()`, `.json()` and `.buffer()` methods which return another Got promise for the parsed body.\
It's like setting the options to `{responseType: 'json', resolveBodyOnly: true}` but without affecting the main Got promise.

```js
import got from 'got';

const responsePromise = got('https://httpbin.org/anything');
const bufferPromise = responsePromise.buffer();
const jsonPromise = responsePromise.json();

const [response, buffer, json] = await Promise.all([responsePromise, bufferPromise, jsonPromise]);
// `response` is an instance of Got Response
// `buffer` is an instance of Uint8Array
// `json` is an object
```

#### **Note:**
> - When using streams, this option is ignored.

#### **Note:**
> - `'buffer'` will return the raw body bytes as a `Uint8Array`. Any modifications will also alter the result of `.text()` and `.json()`. Before overwriting it, please copy it first via `new Uint8Array(buffer)`.\
>  See https://github.com/nodejs/node/issues/27080

### `resolveBodyOnly`

**Type: `boolean`**\
**Default: `false`**

If `true`, the promise will return the [Response body](3-streams.md#response-1) instead of the [Response object](3-streams.md#response-1).

```js
import got from 'got';

const url = 'https://httpbin.org/anything';

// This:
const body = await got(url).json();

// is semantically the same as this:
const body = await got(url, {responseType: 'json', resolveBodyOnly: true});
```

### `context`

**Type: `object<string, unknown>`**\
**Default: `{}`**

**Note:**
> - Non-enumerable properties inside are **not** merged.

Contains user data. It's very useful for storing auth tokens:

```js
import got from 'got';

const instance = got.extend({
	hooks: {
		beforeRequest: [
			options => {
				if (typeof options.context.token !== 'string') {
					throw new Error('Token required');
				}

				options.headers.token = options.context.token;
			}
		]
	}
});

const context = {
	token: 'secret'
};

const {headers} = await instance('https://httpbin.org/headers', {context}).json();

console.log(headers);
//=> {token: 'secret', …}
```

This option is enumerable. In order to define non-enumerable properties inside, do the following:

```js
import got from 'got';

const context = {};

Object.defineProperties(context, {
	token: {
		value: 'secret',
		enumerable: false,
		configurable: true,
		writable: true
	}
});

const instance = got.extend({context});

console.log(instance.defaults.options.context);
//=> {}
```

#### **Merge behavior:**
> - Overrides existing properties.

### `cookieJar`

**Type: <code>object | [tough.cookieJar](https://github.com/salesforce/tough-cookie#cookiejar)</code>**

#### **Note:**
> - Setting this option will result in the `cookie` header being overwritten.

Cookie support. Handles parsing and storing automatically.

```js
import got from 'got';
import {CookieJar} from 'tough-cookie';

const cookieJar = new CookieJar();

await cookieJar.setCookie('foo=bar', 'https://example.com');
await got('https://example.com', {cookieJar});
```

#### `cookieJar.setCookie`

**Type: `(rawCookie: string, url: string) => void | Promise<void>`**

See [ToughCookie API](https://github.com/salesforce/tough-cookie#setcookiecookieorstring-currenturl-options-cberrcookie) for more information.

#### `cookieJar.getCookieString`

**Type: `(currentUrl: string) => string | Promise<string>`**

See [ToughCookie API](https://github.com/salesforce/tough-cookie#getcookiestring) for more information.

### `ignoreInvalidCookies`

**Type: `boolean`**\
**Default: `false`**

Ignore invalid cookies instead of throwing an error.\
Only useful when the `cookieJar` option has been set.

#### **Note:**
> - This is not recommended! Use at your own risk.

### `followRedirect`

**Type: `boolean | (response: PlainResponse) => boolean`**\
**Default: `true`**

Whether redirect responses should be followed automatically.

Optionally, pass a function to dynamically decide based on the response object.

#### **Note:**
> - If a `303` is sent by the server in response to any request type (POST, DELETE, etc.), Got will request the resource pointed to in the location header via GET.\
>  This is in accordance with the [specification](https://tools.ietf.org/html/rfc7231#section-6.4.4). You can optionally turn on this behavior also for other redirect codes - see [`methodRewriting`](#methodrewriting).

```js
import got from 'got';

const instance = got.extend({followRedirect: false});

const response = await instance('http://google.com');

console.log(response.headers.location);
//=> 'https://google.com'
```

### `maxRedirects`

**Type: `number`**\
**Default: `10`**

If exceeded, the request will be aborted and a [`MaxRedirectsError`](8-errors.md#maxredirectserror) will be thrown.

```js
import got from 'got';

const instance = got.extend({maxRedirects: 3});

try {
	await instance('https://nghttp2.org/httpbin/absolute-redirect/5');
} catch (error) {
	//=> 'Redirected 3 times. Aborting.'
	console.log(error.message);
}
```

### `decompress`

**Type: `boolean`**\
**Default: `true`**

Decompress the response automatically. This will set the `accept-encoding` header to `gzip, deflate, br` (and `zstd` on Node.js >= 22.15.0).

If disabled, a compressed response is returned as a `Uint8Array`. This may be useful if you want to handle decompression yourself.

> [!NOTE]
> Zstandard (`zstd`) compression support is available on Node.js >= 22.15.0 and will be automatically enabled when available.

```js
import got from 'got';

const response = await got('https://google.com');

console.log(response.headers['content-encoding']);
//=> 'gzip'
```

### `strictContentLength`

**Type: `boolean`**\
**Default: `true`**

Throw an error if the server response's `content-length` header value doesn't match the number of bytes received.

This is useful for detecting truncated responses and follows RFC 9112 requirements for message completeness.

> [!NOTE]
> - Responses without a `content-length` header are not validated.
> - When enabled and validation fails, a [`ReadError`](8-errors.md#readerror) with code `ERR_HTTP_CONTENT_LENGTH_MISMATCH` will be thrown.

### `dnsLookup`

**Type: `Function`**\
**Default: [`dns.lookup`](https://nodejs.org/api/dns.html#dns_dns_lookup_hostname_options_callback)**

Custom DNS resolution logic.

The function signature is the same as `dns.lookup`.

### `dnsCache`

**Type: <code>[CacheableLookup](https://github.com/szmarczak/cacheable-lookup) | false</code>**

An instance of `CacheableLookup` used for making DNS lookups.\
Useful when making lots of requests to different public hostnames.

**Note:**
> - This should stay disabled when making requests to internal hostnames such as localhost, database.local etc.
> - CacheableLookup uses `dns.resolver4(…)` and `dns.resolver6(…)` under the hood and falls back to `dns.lookup(…)` when the first two fail, which may lead to additional delay.

### `dnsLookupIpVersion`

**Type: `4 | 6`**\
**Default: `undefined`**

The IP version to use. Specifying `undefined` will use the default configuration.

### `request`

**Type: <code>Function<[ClientRequest](https://nodejs.org/api/http.html#http_class_http_clientrequest) | [IncomingMessage](https://nodejs.org/api/http.html#http_class_http_incomingmessage) | undefined> | AsyncFunction<[ClientRequest](https://nodejs.org/api/http.html#http_class_http_clientrequest) | [IncomingMessage](https://nodejs.org/api/http.html#http_class_http_incomingmessage) | undefined></code>**\
**Default: `http.request | https.request` *(depending on the protocol)***

Custom request function.

The main purpose of this is to [support HTTP/2 using a wrapper](https://github.com/szmarczak/http2-wrapper).

Returning `undefined` (or resolving to `undefined`) will fall back to Got's native request implementation.

### `cache`

**Type: `object | false`**\
**Default: `false`**

[Cache adapter instance](../../../core/security/QUARANTINE/vetted/repos/trivy/docs/guide/configuration/cache.md) for storing cached response data.

### `cacheOptions`

**Type: `object`**\
**Default: `{}`**

[Cache options](https://github.com/kornelski/http-cache-semantics#constructor-options) used for the specified request.

### `http2`

**Type: `boolean`**\
**Default: `false`**

**Note:**
> - This option requires Node.js 15.10.0 or newer as HTTP/2 support on older Node.js versions is very buggy.

If `true`, the `request` option will default to `http2wrapper.auto` and the entire `agent` object will be passed.

**Note:**
> - ALPN negotiation will have place in order to determine if the server actually supports HTTP/2. If it doesn't, HTTP/1.1 will be used.

**Note:**
> - Setting the `request` option to `https.request` will disable HTTP/2 usage. It is required to use `http2wrapper.auto`.

**Note:**
> - There is no direct [`h2c`](https://datatracker.ietf.org/doc/html/rfc7540#section-3.1) support. However, you can provide a `h2session` option in a `beforeRequest` hook. See [an example](examples/h2c.js).

```js
import got from 'got';

const {headers} = await got(
	'https://httpbin.org/anything',
	{
		http2: true
	}
);

console.log(headers[':status']);
//=> 200
```

**Note:**
> - The current Got version may use an older version of [`http2-wrapper`](https://github.com/szmarczak/http2-wrapper).\
> If you prefer to use the newest one, set both `request` to `http2wrapper.auto` and `http2` to `true`.

```js
import http2wrapper from 'http2-wrapper';
import got from 'got';

const {headers} = await got(
	'https://httpbin.org/anything',
	{
		http2: true,
		request: http2wrapper.auto
	}
);

console.log(headers[':status']);
//=> 200
```

See the [`http2-wrapper` docs](https://github.com/szmarczak/http2-wrapper) to learn more about Agent and Proxy support.

### `agent`

**Type: `object`**\
**Default: `{}`**

An object with `http`, `https` and `http2` properties.

Got will automatically resolve the protocol and use the corresponding agent. It defaults to:

```js
{
	http: http.globalAgent,
	https: https.globalAgent,
	http2: http2.globalAgent
}
```

**Note:**
> The HTTP/2 `Agent` must be an instance of [`http2wrapper.Agent`](https://github.com/szmarczak/http2-wrapper#new-http2agentoptions)

### `throwHttpErrors`

**Type: `boolean`**\
**Default: `true`**

If `true`, it will [throw](8-errors.md#httperror) when the status code is not `2xx` / `3xx`.

If this is disabled, requests that encounter an error status code will be resolved with the response instead of throwing. This may be useful if you are checking for resource availability and are expecting error responses.

### `username`

**Type: `string`**\
**Default: `''`**

The `username` used for [Basic authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication).

### `password`

**Type: `string`**\
**Default: `''`**

The `password` used for [Basic authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication).

### `localAddress`

**Type: `string | undefined`**\
**Default: `undefined`**

The local IP address used to make the request.

### `createConnection`

**Type: `Function | undefined`**\
**Default: `undefined`**

The function used to retrieve a `net.Socket` instance when the `agent` option is not used.

### `https`

**Type: `object`**

See [Advanced HTTPS API](5-https.md).

### `pagination`

**Type: `object`**

See [Pagination API](4-pagination.md).

### `setHost`

**Type: `boolean`**\
**Default: `true`**

Specifies whether or not to automatically add the `Host` header.

### `maxHeaderSize`

**Type: `number | undefined`**\
**Default: `undefined`**

Optionally overrides the value of [`--max-http-header-size`](https://nodejs.org/api/cli.html#cli_max_http_header_size_size) (default 16KB: `16384`).

### `methodRewriting`

**Type: `boolean`**\
**Default: `false`**

Specifies if the HTTP request method should be [rewritten as `GET`](https://tools.ietf.org/html/rfc7231#section-6.4) on redirects.

As the [specification](https://tools.ietf.org/html/rfc7231#section-6.4) prefers to rewrite the HTTP method only on `303` responses, this is Got's default behavior. Setting `methodRewriting` to `true` will also rewrite `301` and `302` responses, as allowed by the spec. This is the behavior followed by `curl` and browsers.

**Note:**
> - Got never performs method rewriting on `307` and `308` responses, as this is [explicitly prohibited by the specification](https://www.rfc-editor.org/rfc/rfc7231#section-6.4.7).

### `enableUnixSockets`

**Type: `boolean`**\
**Default: `false`**

When enabled, requests can also be sent via [UNIX Domain Sockets](https://serverfault.com/questions/124517/what-is-the-difference-between-unix-sockets-and-tcp-ip-sockets).

> **Warning**
> Make sure you do your own URL sanitizing if you accept untrusted user input for the URL.

Use the following URL scheme: `PROTOCOL://unix:SOCKET:PATH`

- `PROTOCOL` - `http` or `https`
- `SOCKET` - Absolute path to a UNIX domain socket, for example: `/var/run/docker.sock`
- `PATH` - Request path, for example: `/v2/keys`

```js
import got from 'got';

await got('http://unix:/var/run/docker.sock:/containers/json', {enableUnixSockets: true});

// Or without protocol (HTTP by default)
await got('unix:/var/run/docker.sock:/containers/json', {enableUnixSockets: true});

// Enable Unix sockets for the whole instance.
const gotWithUnixSockets = got.extend({enableUnixSockets: true});

await gotWithUnixSockets('http://unix:/var/run/docker.sock:/containers/json');
```

## Methods

### `options.merge(other: Options | OptionsInit)`

Merges `other` into the current instance.

If you look at the [source code](../source/core/options.ts), you will notice that options track internal merge state.\
Setters work a bit differently while merge is in progress.

### `options.toJSON()`

Returns a new plain object that can be stored as [JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#tojson_behavior).

### `options.createNativeRequestOptions()`

Creates a new object for native Node.js HTTP request options.

In other words, this translates Got options into Node.js options.

**Note:**
> - Some other stuff, such as timeouts, is handled internally by Got.

### `options.getRequestFunction()`

Returns a [`http.request`-like](https://nodejs.org/api/http.html#http_http_request_url_options_callback) function used to make the request.

### `options.freeze()`

Makes the entire `Options` instance read-only.
```

## File: `documentation/3-streams.md`
```markdown
[> Back to homepage](../../../README.md#documentation)

## Stream API

Source code: [`source/core/index.ts`](../source/core/index.ts)

### `got.stream(url, options, defaults)`

The function above is exposed by the `got` main interface and returns a new instance of `Request`.

### `new Request(url, options, defaults)`

**Extends: [`Duplex` stream](https://nodejs.org/api/stream.html#stream_class_stream_duplex)**

This constructor takes the same arguments as the Got promise.

**Note:**
> When piping to [`ServerResponse`](https://nodejs.org/api/http.html#http_class_http_serverresponse), the headers will be automatically copied.\
> When `decompress` is `true` (default) and the response is compressed, the `content-encoding` and `content-length` headers are not copied, as the response is decompressed.\
> To filter which headers are copied, listen to the `response` event and modify `response.headers` before piping to the destination.

**Note:**
> If the `body`, `json` or `form` option is used, this stream will be read-only. Check [`stream.isReadonly`](#streamisreadonly) to detect this condition.

**Note:**
> - While `got.post('https://example.com')` resolves, `got.stream.post('https://example.com')` will hang indefinitely until a body is provided.
> - If there's no body on purpose, remember to `stream.end()` or set the body option to an empty string.
> - `got.stream` does not auto-end for `OPTIONS`, `DELETE`, or `PATCH` so you can pipe or write a body without getting `write after end`. Call `stream.end()` when you are not piping a body.

```js
import stream from 'node:stream';
import {pipeline as streamPipeline} from 'node:stream/promises';
import fs from 'node:fs';
import got from 'got';

// This example streams the GET response of a URL to a file.
await streamPipeline(
	got.stream('https://sindresorhus.com'),
	fs.createWriteStream('index.html')
);

// For POST, PUT, PATCH, and DELETE methods, `got.stream` returns a `stream.Writable`.
// This example POSTs the contents of a file to a URL.
await streamPipeline(
	fs.createReadStream('index.html'),
	got.stream.post('https://sindresorhus.com'),
	new stream.PassThrough()
);

// In order to POST, PUT, PATCH, or DELETE without a request body, explicitly specify an empty body:
await streamPipeline(
	got.stream.post('https://sindresorhus.com', { body: '' }),
	new stream.PassThrough()
)
```

Please note that `new stream.PassThrough()` is required in order to catch read errors.\
If it was missing then `pipeline` wouldn't catch any read errors because there would be no stream to pipe to.\
In other words, it would only check errors when writing.

**Tip:**
> - Avoid `from.pipe(to)` as it doesn't forward errors.

### `stream.options`

**Type: [`Options`](2-options.md)**

The options used to make the request.

### `stream.response`

**Type: [`IncomingMessage`](https://nodejs.org/api/http.html#http_class_http_incomingmessage)**

The underlying `IncomingMessage` instance.

### `stream.requestUrl`

**Type: [`URL`](https://nodejs.org/api/url.html#url_the_whatwg_url_api)**

The current `URL` object in this try.

### `stream.redirectUrls`

**Type: [`URL[]`](https://nodejs.org/api/url.html#url_the_whatwg_url_api)**

An array of URLs of consecutive requests.

### `stream.retryCount`

**Type: `number`**

The current retry count.

**Note:**
> - Must be overriden when retrying.

### `stream.ip`

**Type: `string | undefined`**

The destination IP address.

### `stream.isAborted`

**Type: `boolean`**

Whether the request has been aborted or not.

### `stream.socket`

**Type: `net.Socket | tls.Socket | undefined`**

The socket used for this particular request.

### `stream.downloadProgress`

**Type: [`Progress`](typescript.md#progress)**

An object representing how much data have been downloaded.

### `stream.uploadProgress`

**Type: [`Progress`](typescript.md#progress)**

An object representing how much data have been uploaded.

Granular upload progress is automatically supported for non-stream `body` (string/Uint8Array/TypedArray), `json`, and `form` options. For Node.js streams, you can use the [`chunk-data`](https://github.com/sindresorhus/chunk-data) package to get granular progress:

```js
import fs from 'node:fs';
import got from 'got';
import {chunkFromAsync} from 'chunk-data';

const filePath = 'large-file.bin';
const stream = fs.createReadStream(filePath);
const size = fs.statSync(filePath).size;

await got.post('https://httpbin.org/anything', {
	body: chunkFromAsync(stream, 65_536),
	headers: {
		'content-length': size
	}
})
.on('uploadProgress', progress => {
	console.log(progress);
});
```

### `stream.timings`

**Type: [`Timings`](typescript.md#timings)**

An object representing performance information.

To generate the timings, Got uses the [`http-timer`](https://github.com/szmarczak/http-timer) package.

### `stream.isFromCache`

**Type: `boolean | undefined`**

Whether the response has been fetched from cache.

### `stream.reusedSocket`

**Type: `boolean`**

Whether the socket was used for other previous requests.

### `stream.isReadonly`

**Type: `boolean`**

Whether the stream is read-only. Returns `true` when `body`, `json`, or `form` options are provided.

## Events

### `stream.on('response', …)`

#### `response`

**Type: [`PlainResponse`](typescript.md#plainresponse)**

This is emitted when a HTTP response is received.

```js
import {pipeline as streamPipeline} from 'node:stream/promises';
import {createWriteStream} from 'node:fs';
import got from 'got';

const readStream = got.stream('http://example.com/image.png', {throwHttpErrors: false});

const onError = error => {
	// Do something with it.
};

readStream.on('response', async response => {
	if (response.headers.age > 3600) {
		console.log('Failure - response too old');
		readStream.destroy(); // Destroy the stream to prevent hanging resources.
		return;
	}

	// Prevent `onError` being called twice.
	readStream.off('error', onError);

	try {
		await streamPipeline(
			readStream,
			createWriteStream('image.png')
		);

		console.log('Success');
	} catch (error) {
		onError(error);
	}
});

readStream.once('error', onError);
```

### Example: Reading HTTP error response bodies

By default, Got throws HTTP errors before the stream becomes readable. To read error response bodies:

```js
import {pipeline as streamPipeline} from 'node:stream/promises';
import got from 'got';

const stream = got.stream('https://httpbin.org/status/404', {
	throwHttpErrors: false
});

stream.on('response', response => {
	if (!response.ok) {
		console.log(`HTTP Error: ${response.statusCode}`);
		// Stream is readable, you can pipe or read the error body
	}
});

await streamPipeline(stream, process.stdout);
```

**Example: Filter headers when proxying to ServerResponse**

```js
import {pipeline as streamPipeline} from 'node:stream/promises';
import got from 'got';
import express from 'express';

const app = express();

// Allowlist specific headers when proxying
app.get('/proxy', async (request, response) => {
	await streamPipeline(
		got.stream(request.query.url).on('response', upstreamResponse => {
			// Only allow specific headers
			for (const header of Object.keys(upstreamResponse.headers)) {
				if (!['content-type', 'content-length'].includes(header.toLowerCase())) {
					delete upstreamResponse.headers[header];
				}
			}
		}),
		response
	);
});
```

### `stream.on('downloadProgress', …)`

#### `progress`

**Type: [`Progress`](typescript.md#progress)**

This is emitted on every time `stream.downloadProgress` is updated.

### `stream.on('uploadProgress', …)`

#### `progress`

**Type: [`Progress`](typescript.md#progress)**

This is emitted on every time `stream.uploadProgress` is updated.

<a name="retry"></a>
### `stream.on('retry', …)`

To enable retrying when using streams, a retry handler must be attached.

When this event is emitted, you should reset the stream you were writing to and prepare the body again.

**Note:**
> - [`HTTPError`s](./8-errors.md#httperror) cannot be retried if [`options.throwHttpErrors`](./2-options.md#throwhttperrors) is `false`.
>   This is because stream data is saved to `error.response.body` and streams can be read only once.
> - For the Promise API, there is no such limitation.
> - If you need to read HTTP error response bodies without retry, see [Reading HTTP error response bodies](#example-reading-http-error-response-bodies).

#### `retryCount`

**Type: `number`**

The current retry count.

#### `error`

**Type: [`RequestError`](8-errors.md#requesterror)**

The error that caused this retry.

#### `createRetryStream`

**Type: `(options?: OptionsInit) => Request`**

```js
import fs from 'node:fs';
import got from 'got';

let writeStream;

const fn = retryStream => {
	const options = {
		headers: {
			foo: 'bar'
		},
	};

	const stream = retryStream ?? got.stream('https://example.com', options);

	if (writeStream) {
		writeStream.destroy();
	}

	writeStream = fs.createWriteStream('example-com.html');

	stream.pipe(writeStream);

	// If you don't attach the listener, it will NOT make a retry.
	// It automatically checks the listener count so it knows whether to retry or not :)
	stream.once('retry', (retryCount, error, createRetryStream) => {
		fn(createRetryStream()); // or: fn(createRetryStream(optionsToMerge))
	});
};

fn();
```

### `stream.on('redirect', …)`

#### `updatedOptions`

**Type: [`Options`](2-options.md)**

The new options used to make the next request.

#### `response`

**Type: [`IncomingMessage`](https://nodejs.org/api/http.html#http_class_http_incomingmessage)**

The `IncomingMessage` instance the redirect came from.

## Internal usage

These are the functions used internally by Got.\
Other non-documented functions are private and should not be accessible.

### `stream.flush()`

This function is executed automatically by Got. It marks the current stream as ready. If an error occurs before `stream.flush()` is called, it's thrown immediately after `stream.flush()`.

### `stream._beforeError(error)`

This function is called instead of `stream.destroy(error)`, required in order to execute async logic, such as reading the response (e.g. when `ERR_NON_2XX_3XX_RESPONSE` occurs).

### `stream._noPipe`

**Type: `boolean`**

Whether piping is disabled or not. This property is used by the Promise API.

---

## `Response`

Source code: [`source/core/response.ts`](../source/core/response.ts)

**Extends: [`IncomingMessage`](https://nodejs.org/api/http.html#http_class_http_incomingmessage)**

### `requestUrl`

**Type: `URL`**

The original request URL. It is the first argument when calling `got(…)`.

### `redirectUrls`

**Type: `URL[]`**

The redirect URLs.

### `request`

**Type: `Request`**

The underlying Got stream.

### `ip`

**Type: `string`**

The server's IP address.

**Note:**
> - Not available when the response is cached.

### `isFromCache`

**Type: `boolean`**

Whether the response comes from cache or not.

### `ok`

**Type: `boolean`**

Whether the response was successful

**Note:**
> - A request is successful when the status code of the final request is `2xx` or `3xx`.
> - When [following redirects](2-options.md#followredirect), a request is successful **only** when the status code of the final request is `2xx`.
> - `304` responses are always considered successful.
> - Got throws automatically when `response.ok` is `false` and `throwHttpErrors` is `true`.
> - **To read HTTP error response bodies with streams**, set `throwHttpErrors: false` and check `response.ok` in the `response` event handler. [See example above](#example-reading-http-error-response-bodies).

### `statusCode`

**Type: `number`**

The [HTTP status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status).

### `url`

**Type: `string`**

The final URL after all redirects.

### `timings`

**Type: [`Timings`](typescript.md#timings)**

The same as `request.timings`.

### `retryCount`

**Type: `number`**

The same as `request.retryCount`.

### `rawBody`

**Type: `Uint8Array`**

**Note:**
> - This property is only accessible when using Promise API.

The raw response body bytes.

### `body`

**Type: `unknown`**

**Note:**
> - This property is only accessible when using Promise API.

The parsed response body.

### `aborted`

**Type: `boolean`**

The same as `request.aborted`.

### `complete`

**Type: `boolean`**

If `true`, the response has been fully parsed.

### `socket`

**Type: `net.Socket | tls.TLSSocket`**

The same as `request.socket`.

### `headers`

**Type: `object<string, string>`**

The [response headers](https://nodejs.org/api/http.html#http_message_headers).

### `statusMessage`

**Type: `string`**

The status message corresponding to the status code.
```

## File: `documentation/4-pagination.md`
```markdown
[> Back to homepage](../../../README.md#documentation)

## Pagination API

Source code: [`source/create.ts`](../source/create.ts)

### How does the `Link` header work?

The [RFC5988](https://datatracker.ietf.org/doc/html/rfc5988#section-5) defines how the `Link` header looks like.

When the response has been processed, Got looks for [the reference of the `next` relation](https://datatracker.ietf.org/doc/html/rfc5988#section-6.2.2).\
This way Got knows the URL it should visit afterwards. The header can look like this:

```
Link: <https://api.github.com/repositories/18193978/commits?page=2>; rel="next", <https://api.github.com/repositories/18193978/commits?page=44>; rel="last"
```

By default, Got looks only at the `next` relation. To use [other relations](https://datatracker.ietf.org/doc/html/rfc5988#section-6.2.2), you need to customize the `paginate` function below.

### `got.paginate(url, options?)`
### `got.paginate.each(url, options?)`

Returns an [async iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of).

This is memory efficient, as the logic is executed immediately when new data comes in.

```js
import got from 'got';

const countLimit = 10;

const pagination = got.paginate(
	'https://api.github.com/repos/sindresorhus/got/commits',
	{
		pagination: {countLimit}
	}
);

console.log(`Printing latest ${countLimit} Got commits (newest to oldest):`);

for await (const commitData of pagination) {
	console.log(commitData.commit.message);
}
```

### `got.paginate.all(url, options?)`

**Note:**
> - Querying a large dataset significantly increases memory usage.

Returns a Promise for an array of all results.

```js
import got from 'got';

const countLimit = 10;

const results = await got.paginate.all('https://api.github.com/repos/sindresorhus/got/commits', {
	pagination: {countLimit}
});

console.log(`Printing latest ${countLimit} Got commits (newest to oldest):`);
console.log(results);
```

### `pagination`

**Type: `object`**\
**Default:**

```js
{
	transform: (response: Response) => {
		if (response.request.options.responseType === 'json') {
			return response.body;
		}

		return JSON.parse(response.body as string);
	},
	paginate: ({response}) => {
		const rawLinkHeader = response.headers.link;
		if (typeof rawLinkHeader !== 'string' || rawLinkHeader.trim() === '') {
			return false;
		}

		const parsed = parseLinkHeader(rawLinkHeader);
		const next = parsed.find(entry => entry.parameters.rel === 'next' || entry.parameters.rel === '"next"');

		if (next) {
			return {
				url: new URL(next.reference, response.requestUrl)
			};
		}

		return false;
	},
	filter: () => true,
	shouldContinue: () => true,
	countLimit: Number.POSITIVE_INFINITY,
	backoff: 0,
	requestLimit: 10_000,
	stackAllItems: false
}
```

This option represents the `pagination` object.

#### `transform`

**Type: `Function`**\
**Default: `response => JSON.parse(response.body)`**

A function that transforms [`Response`](3-streams.md#response-1) into an array of items.\
This is where you should do the parsing.

#### `paginate`

**Type: `Function`**\
**Default: `Link` header logic**

The function takes an object with the following properties:

- `response` - The current response object,
- `currentItems` - Items from the current response,
- `allItems` - An empty array, unless `stackAllItems` is `true`, otherwise it contains all emitted items.

It should return an object representing Got options pointing to the next page. If there is no next page, `false` should be returned instead.

The options are merged automatically with the previous request.\
Therefore the options returned by `pagination.paginate(…)` must reflect changes only.

**Note:**
> - The `url` option (if set) accepts **only** a [`URL`](https://developer.mozilla.org/en-US/docs/Web/API/URL) instance.\
>   This prevents `prefixUrl` ambiguity. In order to use a relative URL string, merge it via `new URL(relativeUrl, response.url)`.

#### `filter`

**Type: `Function`**\
**Default: `({item, currentItems, allItems}) => true`**

Whether the item should be emitted or not.

#### `shouldContinue`

**Type: `Function`**\
**Default: `({item, currentItems, allItems}) => true`**

**Note:**
> - This function executes only when `filter` returns `true`.

For example, if you need to stop before emitting an entry with some flag, you should use `({item}) => !item.flag`.

If you want to stop after emitting the entry, you should use `({item, allItems}) => allItems.some(item => item.flag)` instead.

#### `countLimit`

**Type: `number`**\
**Default: `Number.POSITIVE_INFINITY`**

The maximum amount of items that should be emitted.

#### `backoff`

**Type: `number`**\
**Default: `0`**

Milliseconds to wait before the next request is triggered.

#### `requestLimit`

**Type: `number`**\
**Default: `10000`**

The maximum amount of request that should be triggered.

**Note:**
> - [Retries on failure](7-retry.md) are not counted towards this limit.

#### `stackAllItems`

**Type: `boolean`**\
**Default: `false`**

Defines how `allItems` is managed in `pagination.paginate`, `pagination.filter` and `pagination.shouldContinue`.

By default, `allItems` is always an empty array. Setting this to `true` will significantly increase memory usage when working with a large dataset.

### Example

In this example we will use `searchParams` instead of `Link` header.\
Just to show how you can customize the `paginate` function.

The reason `filter` looks exactly the same like `shouldContinue` is that the latter will tell Got to stop once we reach our timestamp.
The `filter` function is needed as well, because in the same response we can get results with different timestamps.

```js
import got from 'got';
import Bourne from '@hapi/bourne';

const max = Date.now() - 1000 * 86400 * 7;

const iterator = got.paginate('https://api.github.com/repos/sindresorhus/got/commits', {
	pagination: {
		paginate: ({response, currentItems}) => {
			// If there are no more data, finish.
			if (currentItems.length === 0) {
				return false;
			}

			// Get the current page number.
			const {searchParams} = response.request.options;
			const previousPage = Number(searchParams.get('page') ?? 1);

			// Update the page number by one.
			return {
				searchParams: {
					page: previousPage + 1
				}
			};
		},
		// Using `Bourne` to prevent prototype pollution.
		transform: response => Bourne.parse(response.body),
		filter: ({item}) => {
			// Check if the commit time exceeds our range.
			const date = new Date(item.commit.committer.date);
			const end = date.getTime() - max >= 0;

			return end;
		},
		shouldContinue: ({item}) => {
			// Check if the commit time exceeds our range.
			const date = new Date(item.commit.committer.date);
			const end = date.getTime() - max >= 0;

			return end;
		},
		// We want only 50 results.
		countLimit: 50,
		// Wait 1s before making another request to prevent API rate limiting.
		backoff: 1000,
		// It is a good practice to set an upper limit of how many requests can be made.
		// This way we can avoid infinite loops.
		requestLimit: 10,
		// In this case, we don't need to store all the items we receive.
		// They are processed immediately.
		stackAllItems: false
	}
});

console.log('Last 50 commits from now to week ago:');
for await (const item of iterator) {
	console.log(item.commit.message.split('\n')[0]);
}
```
```

## File: `documentation/5-https.md`
```markdown
[> Back to homepage](../../../README.md#documentation)

## Advanced HTTPS API

### `https`

**Type: `object`**

This option represents the options used to make HTTPS requests.

#### `alpnProtocols`

**Type: `string[]`**\
**Default: `['http/1.1']`**

Acceptable [ALPN](https://en.wikipedia.org/wiki/Application-Layer_Protocol_Negotiation) protocols.

If the `http2` option is `true`, this defaults to `['h2', 'http/1.1']`.

#### `rejectUnauthorized`

**Type: `boolean`**\
**Default: `true`**

If `true`, it will throw on invalid certificates, such as expired or self-signed ones.

#### `checkServerIdentity`

**Type: `(hostname: string, certificate: DetailedPeerCertificate) => Error | undefined`**\
**Default: `tls.checkServerIdentity`**

Custom check of the certificate. Useful for pinning certificates.

The function must return `undefined` if the check succeeded.\
If it failed, an `Error` should be returned.

**Note:**
> - In order to have the function called, the certificate must not be expired, self-signed nor with an untrusted-root.

Check [Node.js docs](https://nodejs.org/api/https.html#https_https_request_url_options_callback) for an example.

#### `serverName`

**Type: `string`**\
**Default: `undefined`**

Server name for the [Server Name Indication (SNI)](https://en.wikipedia.org/wiki/Server_Name_Indication) TLS extension.

This is useful when requesting to servers that don't have a proper domain name but use a certificate with a known CN/SAN.

```js
import got from 'got';

// Request to IP address with specific servername for TLS
await got('https://192.168.1.100', {
	https: {
		serverName: 'example.com'
	}
});
```

#### `certificateAuthority`

**Type: `string | Uint8Array | string[] | Uint8Array[]`**

**Note:**
> - The option has been renamed from the [`ca` TLS option](https://nodejs.org/api/tls.html#tls_tls_createsecurecontext_options) for better readability.

Overrides trusted [CA](https://en.wikipedia.org/wiki/Certificate_authority) certificates.

Defaults to CAs provided by [Mozilla](https://ccadb-public.secure.force.com/mozilla/IncludedCACertificateReport).

```js
import got from 'got';

// Single Certificate Authority
await got('https://example.com', {
	https: {
		certificateAuthority: fs.readFileSync('./my_ca.pem')
	}
});
```

#### `key`

**Type: `string | Uint8Array | string[] | Uint8Array[] | object[]`**

Private keys in [PEM format](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail).

Multiple keys with different passphrases can be provided as an array of `{pem: <string | Uint8Array>, passphrase: <string>}`.

**Note:**
> - Encrypted keys will be decrypted with `https.passphrase`.

#### `passphrase`

**Type: `string`**

Shared passphrase used for a single private key and/or a PFX.

#### `certificate`

**Type: `string | Uint8Array | string[] | Uint8Array[]`**

**Note:**
> - The option has been renamed from the [`cert` TLS option](https://nodejs.org/api/tls.html#tls_tls_createsecurecontext_options) for better readability.

[Certificate chains](https://en.wikipedia.org/wiki/X.509#Certificate_chains_and_cross-certification) in [PEM format](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail).

One certificate chain should be provided per private key.

When providing multiple certificate chains, they do not have to be in the same order as their private keys in `https.key`.

#### `pfx`

**Type: `string | Uint8Array | string[] | Uint8Array[] | object[]`**

[PFX or PKCS12](https://en.wikipedia.org/wiki/PKCS_12) encoded private key and certificate chain. Using `https.pfx` is an alternative to providing `https.key` and `https.certificate` individually. A PFX is usually encrypted, then `https.passphrase` will be used to decrypt it.

Multiple PFX can be provided as an array of unencrypted buffers or an array of objects like:

```ts
{
	buffer: string | Uint8Array,
	passphrase?: string
}
```

#### `certificateRevocationLists`

**Type: `string | Uint8Array | string[] | Uint8Array[]`**

**Note:**
> - The option has been renamed from the [`crl` TLS option](https://nodejs.org/api/tls.html#tls_tls_createsecurecontext_options) for better readability.

#### `secureOptions`

**Type: `number`**

Optionally affect the OpenSSL protocol behavior, which is not usually necessary. This should be used carefully if at all!

The value is a numeric bitmask of the `SSL_OP_*` options from OpenSSL.

For example, to allow connections to legacy servers that do not support secure renegotiation, you can use `crypto.constants.SSL_OP_LEGACY_SERVER_CONNECT`.

```js
import crypto from 'node:crypto';
import got from 'got';

// Allow connections to servers with legacy renegotiation
await got('https://legacy-server.com', {
	https: {
		secureOptions: crypto.constants.SSL_OP_LEGACY_SERVER_CONNECT
	}
});
```

### Other HTTPS options

[Documentation for the below options.](https://nodejs.org/api/tls.html#tls_tls_createsecurecontext_options)

- `ciphers`
- `dhparam`
- `signatureAlgorithms` (renamed from `sigalgs`)
- `minVersion`
- `maxVersion`
- `honorCipherOrder`
- `tlsSessionLifetime` (renamed from `sessionTimeout`)
- `ecdhCurve`

### Examples

```js
import got from 'got';

// Single key with certificate
await got('https://example.com', {
	https: {
		key: fs.readFileSync('./client_key.pem'),
		certificate: fs.readFileSync('./client_cert.pem')
	}
});

// Multiple keys with certificates (out of order)
await got('https://example.com', {
	https: {
		key: [
			fs.readFileSync('./client_key1.pem'),
			fs.readFileSync('./client_key2.pem')
		],
		certificate: [
			fs.readFileSync('./client_cert2.pem'),
			fs.readFileSync('./client_cert1.pem')
		]
	}
});

// Single key with passphrase
await got('https://example.com', {
	https: {
		key: fs.readFileSync('./client_key.pem'),
		certificate: fs.readFileSync('./client_cert.pem'),
		passphrase: 'client_key_passphrase'
	}
});

// Multiple keys with different passphrases
await got('https://example.com', {
	https: {
		key: [
			{pem: fs.readFileSync('./client_key1.pem'), passphrase: 'passphrase1'},
			{pem: fs.readFileSync('./client_key2.pem'), passphrase: 'passphrase2'},
		],
		certificate: [
			fs.readFileSync('./client_cert1.pem'),
			fs.readFileSync('./client_cert2.pem')
		]
	}
});

// Single encrypted PFX with passphrase
await got('https://example.com', {
	https: {
		pfx: fs.readFileSync('./fake.pfx'),
		passphrase: 'passphrase'
	}
});

// Multiple encrypted PFX's with different passphrases
await got('https://example.com', {
	https: {
		pfx: [
			{
				buffer: fs.readFileSync('./key1.pfx'),
				passphrase: 'passphrase1'
			},
			{
				buffer: fs.readFileSync('./key2.pfx'),
				passphrase: 'passphrase2'
			}
		]
	}
});

// Multiple encrypted PFX's with single passphrase
await got('https://example.com', {
	https: {
		passphrase: 'passphrase',
		pfx: [
			{
				buffer: fs.readFileSync('./key1.pfx')
			},
			{
				buffer: fs.readFileSync('./key2.pfx')
			}
		]
	}
});
```
```

## File: `documentation/6-timeout.md`
```markdown
[> Back to homepage](../../../README.md#documentation)

## Timeout options

Source code: [`source/core/timed-out.ts`](../source/core/timed-out.ts)

It is a good practice to set a timeout to prevent hanging requests.\
By default, there is no timeout set.

Note: The [`retry` configuration](7-retry.md) also applies to timeouts.

**All numbers refer to milliseconds.**

```js
import got from 'got';

const {timings} = await got('https://example.com', {
	timeout: {
		lookup: 100,
		connect: 50,
		secureConnect: 50,
		socket: 1000,
		send: 10000,
		response: 1000
	}
});

// Alternatively:
const {timings} = await got('https://example.com', {
	timeout: {
		request: 10000
	}
});

console.log(timings);
// {
// 	start: 1625474926602,
// 	socket: 1625474926605,
// 	lookup: 1625474926610,
// 	connect: 1625474926617,
// 	secureConnect: 1625474926631,
// 	upload: 1625474926631,
// 	response: 1625474926638,
// 	end: 1625474926642,
// 	error: undefined,
// 	abort: undefined,
// 	phases: {
// 		wait: 3,
// 		dns: 5,
// 		tcp: 7,
// 		tls: 14,
// 		request: 0,
// 		firstByte: 7,
// 		download: 4,
// 		total: 40
// 	}
// }
```

### `timeout`

**Type: `object`**

This object describes the maximum allowed time for particular events.

#### `lookup`

**Type: `number`**

Starts when a socket is assigned.\
Ends when the hostname has been resolved.

Does not apply when using a Unix domain socket.\
Does not apply when passing an IP address.

It is preferred to not use any greater value than `100`.

#### `connect`

**Type: `number`**

Starts when lookup completes.\
Ends when the socket is fully connected.

If `lookup` does not apply to the request, this event starts when the socket is assigned and ends when the socket is connected.

#### `secureConnect`

**Type: `number`**

Starts when `connect` completes.\
Ends when the handshake process completes.

This timeout applies only to HTTPS requests.

#### `socket`

**Type: `number`**

Starts when the socket is connected.\
Resets when new data is transferred.

It is the same as [`request.setTimeout(timeout)`](https://nodejs.org/api/http.html#http_request_settimeout_timeout_callback) which calls [`socket.setTimeout(timeout)`](https://nodejs.org/api/net.html#socketsettimeouttimeout-callback) after a socket is assigned to this request and is connected.

#### `send`

**Type: `number`**

Starts when the socket is connected.\
Ends when all data have been written to the socket.

**Note:**
> - This does not assure the data have been received by the other end!
> - It only assures that the data have been passed to the underlying OS.

#### `response`

**Type: `number`**

Starts when request has been flushed.\
Ends when the headers are received.

#### ~~`read`~~

**Type: `number`**

Starts when the headers are received.\
Ends when the response's `end` event fires.

**Note:**
> - This timeout is blocked by https://github.com/nodejs/node/issues/35923

#### `request`

**Type: `number`**

Starts when the request is initiated.\
Ends when the response's `end` event fires.

In other words, this is the global timeout.
```

## File: `documentation/7-retry.md`
```markdown
[> Back to homepage](../../../README.md#documentation)

## Retry API

**Note:**
> If you're looking for retry implementation using streams, check out the [Retry Stream API](3-streams.md#retry).

**Tip:**
> You can trigger a retry by throwing the [`RetryError`](8-errors.md#retryerror) in any hook.

**Tip:**
> The `afterResponse` hook exposes a dedicated function to retry with merged options. [Read more](9-hooks.md#afterresponse).

### `retry`

**Type: `object`**\
**Default:**

```js
{
	limit: 2,
	methods: [
		'GET',
		'PUT',
		'HEAD',
		'DELETE',
		'OPTIONS',
		'TRACE'
	],
	statusCodes: [
		408,
		413,
		429,
		500,
		502,
		503,
		504,
		521,
		522,
		524
	],
	errorCodes: [
		'ETIMEDOUT',
		'ECONNRESET',
		'EADDRINUSE',
		'ECONNREFUSED',
		'EPIPE',
		'ENOTFOUND',
		'ENETUNREACH',
		'EAI_AGAIN'
	],
	maxRetryAfter: undefined,
	calculateDelay: ({computedValue}) => computedValue,
	backoffLimit: Number.POSITIVE_INFINITY,
	noise: 100
}
```

This option represents the `retry` object.

#### `limit`

**Type: `number`**

The maximum retry count.

#### `methods`

**Type: `string[]`**

The allowed methods to retry on.

**Note:**
> - By default, Got does not retry on `POST`.

#### `statusCodes`

**Type: `number[]`**

**Note:**
> - Only [**unsuccessful**](8-errors.md#) requests are retried. In order to retry successful requests, use an [`afterResponse`](9-hooks.md#afterresponse) hook.

The allowed [HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) to retry on.

#### `errorCodes`

**Type: `string[]`**

The allowed error codes to retry on.

- `ETIMEDOUT` - One of the [timeout limits](6-timeout.md) was reached.
- `ECONNRESET`- The connection was forcibly closed.
- `EADDRINUSE`- Could not bind to any free port.
- `ECONNREFUSED`- The connection was refused by the server.
- `EPIPE` - The remote side of the stream being written has been closed.
- `ENOTFOUND` - Could not resolve the hostname to an IP address.
- `ENETUNREACH` - No internet connection.
- `EAI_AGAIN` - DNS lookup timed out.

#### `maxRetryAfter`

**Type: `number | undefined`**\
**Default: `options.timeout.request`**

The upper limit of [`retry-after` header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After). If `undefined`, it will use `options.timeout` as the value.

If the limit is exceeded, the request is aborted.

#### `calculateDelay`

**Type: `Function`**

```ts
(retryObject: RetryObject) => Promisable<number>
```

```ts
interface RetryObject {
	attemptCount: number;
	retryOptions: RetryOptions;
	error: RequestError;
	computedValue: number;
	retryAfter?: number;
}
```

The function used to calculate the delay before the next request is made. Returning `0` aborts the retry.

**Note:**
> - By default, retry rules are enforced before `calculateDelay` runs (`enforceRetryRules: true`), so this function is only called when a retry is allowed.
> - If you set `enforceRetryRules: false`, `calculateDelay` takes full control of retry behavior. In that mode, check `computedValue` and return `0` when it is `0` to preserve default retry safeguards.

**Tip:**
> - This is especially useful when you want to scale down the computed value.

```js
import got from 'got';

await got('https://httpbin.org/anything', {
	retry: {
		limit: 3,
		calculateDelay: ({computedValue}) => {
			// When computedValue is 0, the default logic says don't retry
			// (limit exceeded, non-retryable error, etc.)
			if (computedValue === 0) {
				return 0;
			}

			// Scale down the delay
			return computedValue / 10;
		}
	}
});
```

#### `backoffLimit`

**Type: `number`**

The upper limit of the `computedValue`.

By default, the `computedValue` is calculated in the following way:

```ts
((2 ** (attemptCount - 1)) * 1000) + noise
```

The delay increases exponentially.\
In order to prevent this, you can set this value to a fixed value, such as `1000`.

#### `noise`

**Type: `number`**

The maximum acceptable retry noise in the range of `-100` to `+100`.
```

## File: `documentation/8-errors.md`
```markdown
[> Back to homepage](../../../README.md#documentation)

## Errors

Source code:
- [`source/core/errors.ts`](../source/core/errors.ts)
- [`source/as-promise/types.ts`](../source/as-promise/types.ts)
- [`source/core/response.ts`](../source/core/response.ts)

All Got errors contain various metadata, such as:

- `code` - A string like `ERR_NON_2XX_3XX_RESPONSE`,
- `options` - An instance of [`Options`](2-options.md),
- `request` - An instance of Got Stream,
- `response` (optional) - An instance of Got Response,
- `timings` (optional) - Points to `response.timings`.

#### Capturing async stack traces

Read the article [here](async-stack-traces.md).

> [!NOTE]
> - The error codes may differ when the root error has a `code` property set.
> - The root error will be propagated as is via the [`cause`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause) property.

### `RequestError`

**Code: `ERR_GOT_REQUEST_ERROR`**

When a request fails. Contains a `code` property with error class code, like `ECONNREFUSED`. All the errors below inherit this one.

### `CacheError`

**Code: `ERR_CACHE_ACCESS`**

When a cache method fails, for example, if the database goes down or there's a filesystem error.

### `ReadError`

**Code: `ERR_READING_RESPONSE_STREAM` or `ERR_HTTP_CONTENT_LENGTH_MISMATCH`**

When reading from response stream fails.

The error code will be `ERR_HTTP_CONTENT_LENGTH_MISMATCH` when the `strictContentLength` option is enabled and the server specifies a `content-length` header but the actual number of bytes received doesn't match.

### `ParseError`

**Code: `ERR_BODY_PARSE_FAILURE`**

When server response code is 2xx, and parsing body fails. Includes a `response` property.

### `UploadError`

**Code: `ERR_UPLOAD`**

When the request body is a stream and an error occurs while reading from that stream.

### `HTTPError`

**Code: `ERR_NON_2XX_3XX_RESPONSE`**

When the request is unsuccessful.

A request is successful when the status code of the final request is `2xx` or `3xx`.

When [following redirects](2-options.md#followredirect), a request is successful **only** when the status code of the final request is `2xx`.

> [!NOTE]
> `304` responses are always considered successful.

### `MaxRedirectsError`

**Code: `ERR_TOO_MANY_REDIRECTS`**

When the server redirects you more than ten times. Includes a `response` property.

### `UnsupportedProtocolError`

> [!NOTE]
> This error is not public.

**Code: `ERR_UNSUPPORTED_PROTOCOL`**

When given an unsupported protocol.

### `TimeoutError`

**Code: `ETIMEDOUT`**

When the request is aborted due to a [timeout](6-timeout.md). Includes an `event` (a string) property along with `timings`.

### `RetryError`

**Code: `ERR_RETRYING`**

Always triggers a new retry when thrown.

### `AbortError`

**Code: `ERR_ABORTED`**

When the request is aborted with [AbortController.abort()](https://developer.mozilla.org/en-US/docs/Web/API/AbortController/abort).
```

## File: `documentation/9-hooks.md`
```markdown
[> Back to homepage](../../../README.md#documentation)

## Hooks API

### `hooks`

**Type: `object<string, Function[]>`**

This option represents the hooks to run. Thrown errors will be automatically converted to [`RequestError`](8-errors.md#requesterror).

#### `init`

**Type: `InitHook[]`**\
**Default: `[]`**

```ts
(plainRequestOptions: OptionsInit, options: Options) => void
```

Called with the plain request options, right before their normalization.\
The second argument represents the current [`Options`](2-options.md) instance.

**Note:**
> - This hook must be synchronous.

**Note:**
> - This is called every time options are merged.

**Note:**
> - The `options` object may not have the `url` property. To modify it, use a `beforeRequest` hook instead.

**Note:**
> - This hook is called when a new instance of `Options` is created.
> - Do not confuse this with the creation of `Request` or `got(…)`.

**Note:**
> - When using `got(url)` or `got(url, undefined, defaults)` this hook will **not** be called.

This is especially useful in conjunction with `got.extend()` when the input needs custom handling.

For example, this can be used to fix typos to migrate from older versions faster.

```js
import got from 'got';

const instance = got.extend({
	hooks: {
		init: [
			plain => {
				if ('followRedirects' in plain) {
					plain.followRedirect = plain.followRedirects;
					delete plain.followRedirects;
				}
			}
		]
	}
});

// Normally, the following would throw:
const response = await instance(
	'https://example.com',
	{
		followRedirects: true
	}
);

// There is no option named `followRedirects`, but we correct it in an `init` hook.
```

Or you can create your own option and store it in a context:

```js
import got from 'got';

const instance = got.extend({
	hooks: {
		init: [
			(plain, options) => {
				if ('secret' in plain) {
					options.context.secret = plain.secret;
					delete plain.secret;
				}
			}
		],
		beforeRequest: [
			options => {
				options.headers.secret = options.context.secret;
			}
		]
	}
});

const {headers} = await instance(
	'https://httpbin.org/anything',
	{
		secret: 'passphrase'
	}
).json();

console.log(headers.Secret);
//=> 'passphrase'
```

#### `beforeRequest`

**Type: `BeforeRequestHook[]`**\
**Default: `[]`**

```ts
(options: Options, context: BeforeRequestHookContext) => Promisable<void | Response | ResponseLike>
```

Called right before making the request with `options.createNativeRequestOptions()`.\
This hook is especially useful in conjunction with `got.extend()` when you want to sign your request.

The second parameter is a context object with the following properties:
- `retryCount` - The current retry count (0 for the initial request, 1+ for retries).

**Note:**
> - Got will make no further changes to the request before it is sent.

**Note:**
> - Changing `options.json` or `options.form` has no effect on the request. You should change `options.body` instead. If needed, update the `options.headers` accordingly.

```js
import got from 'got';

const response = await got.post(
	'https://httpbin.org/anything',
	{
		json: {payload: 'old'},
		hooks: {
			beforeRequest: [
				(options, context) => {
					options.body = JSON.stringify({payload: 'new'});
					options.headers['content-length'] = new TextEncoder().encode(options.body).byteLength.toString();
				}
			]
		}
	}
);
```

You can use `context.retryCount` to conditionally modify behavior based on whether it's the initial request or a retry:

```js
import got from 'got';

const response = await got('https://httpbin.org/status/500', {
	retry: {
		limit: 2
	},
	hooks: {
		beforeRequest: [
			(options, context) => {
				// Only log on initial request, not on retries
				if (context.retryCount === 0) {
					console.log('Making initial request');
				}
			}
		]
	}
});
```

**Tip:**
> - You can indirectly override the `request` function by early returning a [`ClientRequest`-like](https://nodejs.org/api/http.html#http_class_http_clientrequest) instance or a [`IncomingMessage`-like](https://nodejs.org/api/http.html#http_class_http_incomingmessage) instance. This is very useful when creating a custom cache mechanism.
> - [Read more about this tip](../../../core/security/QUARANTINE/vetted/repos/trivy/docs/guide/configuration/cache.md#advanced-caching-mechanisms).

#### `beforeRedirect`

**Type: `BeforeRedirectHook[]`**\
**Default: `[]`**

```ts
(updatedOptions: Options, plainResponse: PlainResponse) => Promisable<void>
```

The equivalent of `beforeRequest` but when redirecting.

**Tip:**
> - This is especially useful when you want to avoid dead sites.

```js
import got from 'got';

const response = await got('https://example.com', {
	hooks: {
		beforeRedirect: [
			(options, response) => {
				if (options.hostname === 'deadSite') {
					options.hostname = 'fallbackSite';
				}
			}
		]
	}
});
```

#### `beforeRetry`

**Type: `BeforeRetryHook[]`**\
**Default: `[]`**

```ts
(error: RequestError, retryCount: number) => Promisable<void>
```

The equivalent of `beforeError` but when retrying. Additionally, there is a second argument `retryCount`, the current retry number.

**Note:**
> - When using the Stream API, this hook is ignored.

**Note:**
> - When retrying, the `beforeRequest` hook is called afterwards.

**Note:**
> - If no retry occurs, the `beforeError` hook is called instead.

This hook is especially useful when you want to retrieve the cause of a retry.

```js
import got from 'got';

await got('https://httpbin.org/status/500', {
	hooks: {
		beforeRetry: [
			(error, retryCount) => {
				console.log(`Retrying [${retryCount}]: ${error.code}`);
				// Retrying [1]: ERR_NON_2XX_3XX_RESPONSE
			}
		]
	}
});
```

#### `beforeCache`

**Type: `BeforeCacheHook[]`**\
**Default: `[]`**

```ts
(response: PlainResponse) => false | void
```

Called right before the response is cached. Allows you to control caching behavior by modifying response properties or preventing caching entirely.

This is especially useful when you want to prevent caching of specific responses or modify cache headers.

**Return value:**
> - `false` - Prevent caching (remaining hooks are skipped)
> - `void`/`undefined` - Use default caching behavior (mutations take effect)

**Modifying the response:**
> - Hooks can directly mutate response properties like `headers`, `statusCode`, and `statusMessage`
> - Mutations to `response.headers` affect how the caching layer decides whether to cache the response and for how long
> - Changes are applied to what gets cached, not to the response the user receives (they are separate objects)

**Note:**
> - This hook is only called when the `cache` option is enabled.

**Note:**
> - This hook must be synchronous. It cannot return a Promise. If you need async logic to determine caching behavior, use a `beforeRequest` hook instead.

**Note:**
> - When returning `false`, remaining hooks are skipped. The response headers the user receives are NOT modified - only the caching layer sees modified headers.

**Note:**
> - If a hook throws an error, it will be propagated and the request will fail. This is consistent with how other hooks in Got handle errors.

**Note:**
> - At this stage, the response body has not been read yet - it's still a stream. Properties like `response.body` and `response.rawBody` are not available. You can only inspect/modify response headers and status code.

```js
import got from 'got';

// Simple: Don't cache errors
const instance = got.extend({
	cache: new Map(),
	hooks: {
		beforeCache: [
			(response) => response.statusCode >= 400 ? false : undefined
		]
	}
});

await instance('https://example.com');
```

```js
import got from 'got';

// Advanced: Modify headers for fine control
const instance2 = got.extend({
	cache: new Map(),
	hooks: {
		beforeCache: [
			(response) => {
				// Force caching with explicit duration
				// Mutations work directly - no need to return
				response.headers['cache-control'] = 'public, max-age=3600';
			}
		]
	}
});
```

#### `afterResponse`

**Type: `AfterResponseHook[]`**\
**Default: `[]`**

```ts
(response: Response, retryWithMergedOptions: (options: OptionsInit) => never) => Promisable<Response | RequestPromise<Response>>
```

Each function should return the response. This is especially useful when you want to refresh an access token.

**Note:**
> - When using the Stream API, this hook is ignored.

**Note:**
> - Calling the `retryWithMergedOptions` function will trigger `beforeRetry` hooks. By default, remaining `afterResponse` hooks are removed to prevent duplicate execution. To preserve remaining hooks on retry, set `preserveHooks: true` in the options passed to `retryWithMergedOptions`. In case of an error, `beforeRetry` hooks will be called instead.
> - Meanwhile, the `init`, `beforeRequest`, and `beforeRedirect` hooks, as well as already executed `afterResponse` hooks, are skipped.

**Note:**
> - To preserve remaining `afterResponse` hooks after calling `retryWithMergedOptions`, set `preserveHooks: true` in the options passed to `retryWithMergedOptions`. This is useful when you want hooks to run on retried requests.

**Warning:**
> - Be cautious when using `preserveHooks: true`. If a hook unconditionally calls `retryWithMergedOptions` with `preserveHooks: true`, it will create an infinite retry loop. Always ensure hooks have proper conditional logic to avoid infinite retries.

```js
import got from 'got';

const instance = got.extend({
	hooks: {
		afterResponse: [
			(response, retryWithMergedOptions) => {
				// Unauthorized
				if (response.statusCode === 401) {
					// Refresh the access token
					const updatedOptions = {
						headers: {
							token: getNewToken()
						}
					};

					// Update the defaults
					instance.defaults.options.merge(updatedOptions);

					// Make a new retry
					return retryWithMergedOptions(updatedOptions);
				}

				// No changes otherwise
				return response;
			}
		],
		beforeRetry: [
			error => {
				// This will be called on `retryWithMergedOptions(...)`
			}
		]
	},
	mutableDefaults: true
});
```

**Example with `preserveHooks`:**

```js
import got from 'got';

const instance = got.extend({
	hooks: {
		afterResponse: [
			(response, retryWithMergedOptions) => {
				if (response.statusCode === 401) {
					return retryWithMergedOptions({
						headers: {
							authorization: getNewToken()
						},
						preserveHooks: true  // Keep remaining hooks
					});
				}

				return response;
			},
			(response) => {
				// This hook will run on the retried request
				// (the original request is interrupted when the first hook triggers a retry)
				console.log('Response received:', response.statusCode);
				return response;
			}
		]
	}
});
```

#### `beforeError`

**Type: `BeforeErrorHook[]`**\
**Default: `[]`**

```ts
(error: RequestError) => Promisable<Error>
```

Called with a [`RequestError`](8-errors.md#requesterror) instance. The error is passed to the hook right before it's thrown.

This hook can return any `Error` instance, allowing you to:
- Return custom error classes for better error handling in your application
- Extend `RequestError` with additional properties
- Return plain `Error` instances when you don't need Got-specific error information

This is especially useful when you want to have more detailed errors or maintain backward compatibility with existing error handling code.

```js
import got from 'got';

// Modify and return the error
await got('https://api.github.com/repos/sindresorhus/got/commits', {
	responseType: 'json',
	hooks: {
		beforeError: [
			error => {
				const {response} = error;
				if (response && response.body) {
					error.name = 'GitHubError';
					error.message = `${response.body.message} (${response.statusCode})`;
				}

				return error;
			}
		]
	}
});

// Return a custom error class
class CustomAPIError extends Error {
	constructor(message, statusCode) {
		super(message);
		this.name = 'CustomAPIError';
		this.statusCode = statusCode;
	}
}

await got('https://api.example.com/endpoint', {
	hooks: {
		beforeError: [
			error => {
				// Return a custom error for backward compatibility with your application
				return new CustomAPIError(
					error.message,
					error.response?.statusCode
				);
			}
		]
	}
});
```
```

## File: `documentation/async-stack-traces.md`
```markdown
[> Back to homepage](../../../README.md#documentation)

### Capturing async stack traces

**Caution:**
> - Capturing async stack traces can severely degrade performance!

**Want to skip the article? See the [Conclusion](#conclusion) where we discuss a mediocre solution.**

We live in a world full of bugs. Software is getting more and more complicated, which makes debugging increasingly more difficult. Ever had an error with no idea where it came from? Yeah, it's often not easy to track this down.

You might have noticed that the `.stack` of an error sometimes look incomplete. This is often due to the execution of an async function that is triggered by a timer. Following the example:

```js
await new Promise((resolve, reject) => {
	setTimeout(() => {
		reject(new Error('here'));
	});
});
```

```js
file:///home/szm/Desktop/got/demo.js:3
                reject(new Error('here'));
                       ^

Error: here
    at Timeout._onTimeout (file:///home/szm/Desktop/got/demo.js:3:10)
    at listOnTimeout (node:internal/timers:557:17)
    at processTimers (node:internal/timers:500:7)
```

The stack trace does not show where the timeout was set. It's currently not possible to determine this with the native `Promise`s. However, [`bluebird`](https://github.com/petkaantonov/bluebird/) exposes an option dedicated to capturing async stack traces:

```js
import Bluebird from 'bluebird';

Bluebird.config({longStackTraces: true});
global.Promise = Bluebird;

await new Promise((resolve, reject) => {
	setTimeout(() => {
		reject(new Error('here'));
	});
});
```

```
node:internal/process/esm_loader:74
    internalBinding('errors').triggerUncaughtException(
                              ^

Error: here
    at Timeout._onTimeout (file:///home/szm/Desktop/got/demo.js:7:10)
    at listOnTimeout (node:internal/timers:557:17)
    at processTimers (node:internal/timers:500:7)
From previous event:
    at file:///home/szm/Desktop/got/demo.js:5:7
    at ModuleJob.run (node:internal/modules/esm/module_job:183:25)
    at async Loader.import (node:internal/modules/esm/loader:178:24)
    at async Object.loadESM (node:internal/process/esm_loader:68:5)
    at async handleMainPromise (node:internal/modules/run_main:63:12)
```

Now it's clear. We know that the timeout was set on line 5. Bluebird should be sufficient for Got:

```js
import Bluebird from 'bluebird';
import got from 'got';

Bluebird.config({longStackTraces: true});
global.Promise = Bluebird;

try {
	await got('https://httpbin.org/delay/1', {
		timeout: {
			request: 1
		},
		retry: {
			limit: 0
		}
	});
} catch (error) {
	console.error(error.stack);
}
```

```
TimeoutError: Timeout awaiting 'request' for 1ms
    at ClientRequest.<anonymous> (file:///home/szm/Desktop/got/dist/source/core/index.js:780:61)
    at Object.onceWrapper (node:events:514:26)
    at ClientRequest.emit (node:events:406:35)
    at TLSSocket.socketErrorListener (node:_http_client:447:9)
    at TLSSocket.emit (node:events:394:28)
    at emitErrorNT (node:internal/streams/destroy:157:8)
    at emitErrorCloseNT (node:internal/streams/destroy:122:3)
    at processTicksAndRejections (node:internal/process/task_queues:83:21)
    at Timeout.timeoutHandler [as _onTimeout] (file:///home/szm/Desktop/got/dist/source/core/timed-out.js:42:25)
    at listOnTimeout (node:internal/timers:559:11)
    at processTimers (node:internal/timers:500:7)
From previous event:
    at new Promise (<anonymous>)
    at asPromise (file:///home/szm/Desktop/got/dist/source/as-promise/index.js:21:21)
    at lastHandler (file:///home/szm/Desktop/got/dist/source/create.js:42:27)
    at iterateHandlers (file:///home/szm/Desktop/got/dist/source/create.js:49:28)
    at got (file:///home/szm/Desktop/got/dist/source/create.js:69:16)
    at file:///home/szm/Desktop/got/demo.js:8:8
    at ModuleJob.run (node:internal/modules/esm/module_job:183:25)
    at async Loader.import (node:internal/modules/esm/loader:178:24)
    at async Object.loadESM (node:internal/process/esm_loader:68:5)
    at async handleMainPromise (node:internal/modules/run_main:63:12)
```

As expected, we know where the timeout has been set. Unfortunately, if we increase our retry count limit to `1`, the stack trace remains the same. That's because `bluebird` doesn't track I/O events. Please note that this should be sufficient for most cases. In order to debug further, we can use [`async_hooks`](https://nodejs.org/api/async_hooks.html) instead. A Stack Overflow user has come up with an awesome solution:

```js
import asyncHooks from 'node:async_hooks';

const traces = new Map();

asyncHooks.createHook({
	init(id) {
		const trace = {};
		Error.captureStackTrace(trace);
		traces.set(id, trace.stack.replace(/(^.+$\n){4}/m, '\n'));
	},
	destroy(id) {
		traces.delete(id);
	},
}).enable();

globalThis.Error = class extends Error {
	constructor(message) {
		super(message);
		this.constructor.captureStackTrace(this, this.constructor);
	}

	static captureStackTrace(what, where) {
		super.captureStackTrace.call(Error, what, where);

		const trace = traces.get(asyncHooks.executionAsyncId());
		if (trace) {
			what.stack += trace;
		}
	}
};
```

If we replace the `bluebird` part with this, we get:

```
Error: Timeout awaiting 'request' for 1ms
    at ClientRequest.<anonymous> (file:///home/szm/Desktop/got/dist/source/core/index.js:780:61)
    at Object.onceWrapper (node:events:514:26)
    at ClientRequest.emit (node:events:406:35)
    at TLSSocket.socketErrorListener (node:_http_client:447:9)
    at TLSSocket.emit (node:events:394:28)
    at emitErrorNT (node:internal/streams/destroy:157:8)
    at emitErrorCloseNT (node:internal/streams/destroy:122:3)
    at processTicksAndRejections (node:internal/process/task_queues:83:21)
    at emitInitScript (node:internal/async_hooks:493:3)
    at process.nextTick (node:internal/process/task_queues:133:5)
    at onDestroy (node:internal/streams/destroy:96:15)
    at TLSSocket.Socket._destroy (node:net:677:5)
    at _destroy (node:internal/streams/destroy:102:25)
    at TLSSocket.destroy (node:internal/streams/destroy:64:5)
    at ClientRequest.destroy (node:_http_client:371:16)
    at emitInitScript (node:internal/async_hooks:493:3)
    at initAsyncResource (node:internal/timers:162:5)
    at new Timeout (node:internal/timers:196:3)
    at setTimeout (node:timers:164:19)
    at addTimeout (file:///home/szm/Desktop/got/dist/source/core/timed-out.js:32:25)
    at timedOut (file:///home/szm/Desktop/got/dist/source/core/timed-out.js:59:31)
    at Request._onRequest (file:///home/szm/Desktop/got/dist/source/core/index.js:771:32)
    at emitInitScript (node:internal/async_hooks:493:3)
    at promiseInitHook (node:internal/async_hooks:323:3)
    at promiseInitHookWithDestroyTracking (node:internal/async_hooks:327:3)
    at Request.flush (file:///home/szm/Desktop/got/dist/source/core/index.js:274:24)
    at makeRequest (file:///home/szm/Desktop/got/dist/source/as-promise/index.js:125:30)
    at Request.<anonymous> (file:///home/szm/Desktop/got/dist/source/as-promise/index.js:121:17)
    at Object.onceWrapper (node:events:514:26)
    at emitInitScript (node:internal/async_hooks:493:3)
    at promiseInitHook (node:internal/async_hooks:323:3)
    at promiseInitHookWithDestroyTracking (node:internal/async_hooks:327:3)
    at file:///home/szm/Desktop/got/dist/source/core/index.js:357:27
    at processTicksAndRejections (node:internal/process/task_queues:96:5)
    at emitInitScript (node:internal/async_hooks:493:3)
    at promiseInitHook (node:internal/async_hooks:323:3)
    at promiseInitHookWithDestroyTracking (node:internal/async_hooks:327:3)
    at file:///home/szm/Desktop/got/dist/source/core/index.js:338:50
    at Request._beforeError (file:///home/szm/Desktop/got/dist/source/core/index.js:388:11)
    at ClientRequest.<anonymous> (file:///home/szm/Desktop/got/dist/source/core/index.js:781:18)
    at Object.onceWrapper (node:events:514:26)
    at emitInitScript (node:internal/async_hooks:493:3)
    at process.nextTick (node:internal/process/task_queues:133:5)
    at onDestroy (node:internal/streams/destroy:96:15)
    at TLSSocket.Socket._destroy (node:net:677:5)
    at _destroy (node:internal/streams/destroy:102:25)
    at TLSSocket.destroy (node:internal/streams/destroy:64:5)
    at ClientRequest.destroy (node:_http_client:371:16)
    at emitInitScript (node:internal/async_hooks:493:3)
    at initAsyncResource (node:internal/timers:162:5)
    at new Timeout (node:internal/timers:196:3)
    at setTimeout (node:timers:164:19)
    at addTimeout (file:///home/szm/Desktop/got/dist/source/core/timed-out.js:32:25)
    at timedOut (file:///home/szm/Desktop/got/dist/source/core/timed-out.js:59:31)
    at Request._onRequest (file:///home/szm/Desktop/got/dist/source/core/index.js:771:32)
    at emitInitScript (node:internal/async_hooks:493:3)
    at promiseInitHook (node:internal/async_hooks:323:3)
    at promiseInitHookWithDestroyTracking (node:internal/async_hooks:327:3)
    at Request.flush (file:///home/szm/Desktop/got/dist/source/core/index.js:274:24)
    at lastHandler (file:///home/szm/Desktop/got/dist/source/create.js:37:26)
    at iterateHandlers (file:///home/szm/Desktop/got/dist/source/create.js:49:28)
    at got (file:///home/szm/Desktop/got/dist/source/create.js:69:16)
    at Timeout.timeoutHandler [as _onTimeout] (file:///home/szm/Desktop/got/dist/source/core/timed-out.js:42:25)
    at listOnTimeout (node:internal/timers:559:11)
    at processTimers (node:internal/timers:500:7)
```

This is extremely long, and not a complete Node.js app. Just a demo. Imagine how long it would be if this was used with databases, file systems, etc.

#### Conclusion

All these workarounds have a large impact on performance. However, there is a possible solution to this madness. Got provides handlers, hooks, and context. We can capture the stack trace in a handler, store it in a context and expose it in a `beforeError` hook.

```js
import got from 'got';

const instance = got.extend({
	handlers: [
		(options, next) => {
			Error.captureStackTrace(options.context);
			return next(options);
		}
	],
	hooks: {
		beforeError: [
			error => {
				error.source = error.options.context.stack.split('\n');
				return error;
			}
		]
	}
});

try {
	await instance('https://httpbin.org/delay/1', {
		timeout: {
			request: 100
		},
		retry: {
			limit: 0
		}
	});
} catch (error) {
	console.error(error);
}
```

```
RequestError: Timeout awaiting 'request' for 100ms
    at ClientRequest.<anonymous> (file:///home/szm/Desktop/got/dist/source/core/index.js:780:61)
    at Object.onceWrapper (node:events:514:26)
    at ClientRequest.emit (node:events:406:35)
    at TLSSocket.socketErrorListener (node:_http_client:447:9)
    at TLSSocket.emit (node:events:394:28)
    at emitErrorNT (node:internal/streams/destroy:157:8)
    at emitErrorCloseNT (node:internal/streams/destroy:122:3)
    at processTicksAndRejections (node:internal/process/task_queues:83:21)
    at Timeout.timeoutHandler [as _onTimeout] (file:///home/szm/Desktop/got/dist/source/core/timed-out.js:42:25)
    at listOnTimeout (node:internal/timers:559:11)
    at processTimers (node:internal/timers:500:7) {
  input: undefined,
  code: 'ETIMEDOUT',
  timings: { <too long to include> },
  name: 'TimeoutError',
  options: { <too long to include> },
  event: 'request',
  source: [
    'Error',
    '    at got.extend.handlers (file:///home/szm/Desktop/got/demo.js:6:10)',
    '    at iterateHandlers (file:///home/szm/Desktop/got/dist/source/create.js:49:28)',
    '    at got (file:///home/szm/Desktop/got/dist/source/create.js:69:16)',
    '    at file:///home/szm/Desktop/got/demo.js:23:8',
    '    at ModuleJob.run (node:internal/modules/esm/module_job:183:25)',
    '    at async Loader.import (node:internal/modules/esm/loader:178:24)',
    '    at async Object.loadESM (node:internal/process/esm_loader:68:5)',
    '    at async handleMainPromise (node:internal/modules/run_main:63:12)'
  ]
}
```

Yay! This is much more readable. Furthermore, we capture the stack trace only when `got` is called. This is definitely going to have some performance impact, but it will be much more performant than the other mentioned solutions.

Curious to know more? Check out these links:
- https://stackoverflow.com/questions/54914770/is-there-a-good-way-to-surface-error-traces-in-production-across-event-emitters
- https://github.com/nodejs/node/issues/11370
- https://github.com/puppeteer/puppeteer/issues/2037
- https://github.com/nodejs/node/pull/13870
```

## File: `documentation/cache.md`
```markdown
[> Back to homepage](../../../README.md#documentation)

## Cache

Got implements [RFC 7234](https://httpwg.org/specs/rfc7234.html) compliant HTTP caching which works out of the box in-memory and is easily pluggable with a wide range of storage adapters. Fresh cache entries are served directly from the cache, and stale cache entries are revalidated with `If-None-Match` / `If-Modified-Since` headers. You can read more about the underlying cache behavior in the [`cacheable-request` documentation](https://www.npmjs.com/package/cacheable-request).

You can use the JavaScript `Map` type as an in-memory cache:

```js
import got from 'got';

const map = new Map();

let response = await got('https://sindresorhus.com', {cache: map});
console.log(response.isFromCache);
//=> false

response = await got('https://sindresorhus.com', {cache: map});
console.log(response.isFromCache);
//=> true
```

Got uses [Keyv](https://github.com/lukechilds/keyv) internally to support a wide range of storage adapters. For something more scalable you could use an [official Keyv storage adapter](https://github.com/lukechilds/keyv#official-storage-adapters):

```
$ npm install @keyv/redis
```

```js
import got from 'got';
import KeyvRedis from '@keyv/redis';

const redis = new KeyvRedis('redis://user:pass@localhost:6379');

await got('https://sindresorhus.com', {cache: redis});
```

Got supports anything that follows the Map API, so it's easy to write your own storage adapter or use a third-party solution.

For example, the following are all valid storage adapters:

```js
const storageAdapter = new Map();

await got('https://sindresorhus.com', {cache: storageAdapter});
```

```js
import storageAdapter from './my-storage-adapter';

await got('https://sindresorhus.com', {cache: storageAdapter});
```

```js
import QuickLRU from 'quick-lru';

const storageAdapter = new QuickLRU({maxSize: 1000});

await got('https://sindresorhus.com', {cache: storageAdapter});
```

View the [Keyv docs](https://github.com/lukechilds/keyv) for more information on how to use storage adapters.

### Advanced caching mechanisms

The `request` function may return an instance of `IncomingMessage`-like class.

```js
import https from 'node:https';
import {Readable} from 'node:stream';
import got from 'got';

const getCachedResponse = (url, options) => {
	const response = new Readable({
		read() {
			this.push("Hello, world!");
			this.push(null);
		}
	});

	response.statusCode = 200;
	response.headers = {};
	response.trailers = {};
	response.socket = null;
	response.aborted = false;
	response.complete = true;
	response.httpVersion = '1.1';
	response.httpVersionMinor = 1;
	response.httpVersionMajor = 1;

	return response;
};

const instance = got.extend({
	request: (url, options, callback) => {
		return getCachedResponse(url, options);
	}
});

const body = await instance('https://example.com').text();

console.log(body);
//=> "Hello, world!"
```

If you don't want to alter the `request` function, you can return a cached response in a `beforeRequest` hook:

```js
import https from 'node:https';
import {Readable} from 'node:stream';
import got from 'got';

const getCachedResponse = (url, options) => {
	const response = new Readable({
		read() {
			this.push("Hello, world!");
			this.push(null);
		}
	});

	response.statusCode = 200;
	response.headers = {};
	response.trailers = {};
	response.socket = null;
	response.aborted = false;
	response.complete = true;
	response.httpVersion = '1.1';
	response.httpVersionMinor = 1;
	response.httpVersionMajor = 1;

	return response;
};

const instance = got.extend({
	hooks: {
		beforeRequest: [
			options => {
				return getCachedResponse(options.url, options);
			}
		]
	}
});

const body = await instance('https://example.com').text();

console.log(body);
//=> "Hello, world!"
```

If you want to prevent duplicating the same requests, you can use a handler instead.

```js
import got from 'got';

const map = new Map();

const instance = got.extend({
	handlers: [
		(options, next) => {
			if (options.isStream) {
				return next(options);
			}

			const pending = map.get(options.url.href);
			if (pending) {
				return pending;
			}

			const promise = next(options);

			map.set(options.url.href, promise);
			promise.finally(() => {
				map.delete(options.url.href);
			});

			return promise;
		}
	]
});

const [first, second] = await Promise.all([
	instance('https://httpbin.org/anything'),
	instance('https://httpbin.org/anything')
]);

console.log(first === second);
//=> true
```
```

## File: `documentation/diagnostics-channel.md`
```markdown
[> Back to homepage](../../../README.md#documentation)

## Diagnostics Channel

Got integrates with Node.js [diagnostic channels](https://nodejs.org/api/diagnostics_channel.html) for low-overhead observability. Events are only published when subscribers exist.

### Channels

#### `got:request:create`

Emitted when a request is created.

```ts
{requestId: string, url: string, method: string}
```

#### `got:request:start`

Emitted before the native HTTP request is sent.

```ts
{requestId: string, url: string, method: string, headers: Record<string, string | string[] | undefined>}
```

#### `got:response:start`

Emitted when response headers are received.

```ts
{requestId: string, url: string, statusCode: number, headers: Record<string, string | string[] | undefined>, isFromCache: boolean}
```

#### `got:response:end`

Emitted when the response completes.

```ts
{requestId: string, url: string, statusCode: number, bodySize?: number, timings?: Timings}
```

#### `got:request:retry`

Emitted when retrying a request.

```ts
{requestId: string, retryCount: number, error: RequestError, delay: number}
```

#### `got:request:error`

Emitted when a request fails.

```ts
{requestId: string, url: string, error: RequestError, timings?: Timings}
```

#### `got:response:redirect`

Emitted when following a redirect.

```ts
{requestId: string, fromUrl: string, toUrl: string, statusCode: number}
```

### Example

```js
import diagnosticsChannel from 'node:diagnostics_channel';

const channel = diagnosticsChannel.channel('got:request:start');

channel.subscribe(message => {
	console.log(`${message.method} ${message.url}`);
});
```

All events for a single request share the same `requestId`.

### TypeScript

All message types are exported from the main package:

```ts
import type {
	DiagnosticRequestCreate,
	DiagnosticRequestStart,
	DiagnosticResponseStart,
	DiagnosticResponseEnd,
	DiagnosticRequestRetry,
	DiagnosticRequestError,
	DiagnosticResponseRedirect,
} from 'got';
```
```

## File: `documentation/lets-make-a-plugin.md`
```markdown
[> Back to homepage](../../../README.md#documentation)

## Let's make a plugin!

> Another example on how to use Got like a boss :electric_plug:

Okay, so you already have learned some basics. That's great!

When it comes to advanced usage, custom instances are really helpful.
For example, take a look at [`gh-got`](https://github.com/sindresorhus/gh-got).
It looks pretty complicated, but... it's simple and extremely useful.

Before we start, we need to find the [GitHub API docs](https://developer.github.com/v3/).

Let's write down the most important information:
1. The root endpoint is `https://api.github.com/`.
2. We will use version 3 of the API.\
   The `Accept` header needs to be set to `application/vnd.github.v3+json`.
3. The body is in a JSON format.
4. We will use OAuth2 for authorization.
5. We may receive `400 Bad Request` or `422 Unprocessable Entity`.\
   The body contains detailed information about the error.
6. *Pagination?* Yeah! Supported natively by Got.
7. Rate limiting. These headers are interesting:

- `X-RateLimit-Limit`
- `X-RateLimit-Remaining`
- `X-RateLimit-Reset`

Also `X-GitHub-Request-Id` may be useful for debugging.

8. The `User-Agent` header is required.

When we have all the necessary info, we can start mixing :cake:

### The root endpoint

Not much to do here. Just extend an instance and provide the `prefixUrl` option:

```js
import got from 'got';

const instance = got.extend({
	prefixUrl: 'https://api.github.com'
});

export default instance;
```

### v3 API

GitHub needs to know which API version we are using. We'll use the `Accept` header for that:

```js
import got from 'got';

const instance = got.extend({
	prefixUrl: 'https://api.github.com',
	headers: {
		accept: 'application/vnd.github.v3+json'
	}
});

export default instance;
```

### JSON body

We'll use [`options.responseType`](2-options.md#responsetype):

```js
import got from 'got';

const instance = got.extend({
	prefixUrl: 'https://api.github.com',
	headers: {
		accept: 'application/vnd.github.v3+json'
	},
	responseType: 'json'
});

export default instance;
```

### Authorization

It's common to set some environment variables, for example, `GITHUB_TOKEN`. You can modify the tokens in all your apps easily, right? Cool. What about... we want to provide a unique token for each app. Then we will need to create a new option - it will default to the environment variable, but you can easily override it.

Got performs option validation and doesn't know that `token` is a wanted option so it will throw. We can handle it inside an `init` hook and save it in `options.context`.

```js
import got from 'got';

const instance = got.extend({
	prefixUrl: 'https://api.github.com',
	headers: {
		accept: 'application/vnd.github.v3+json'
	},
	responseType: 'json',
	context: {
		token: process.env.GITHUB_TOKEN,
	},
	hooks: {
		init: [
			(raw, options) => {
				if ('token' in raw) {
					options.context.token = raw.token;
					delete raw.token;
				}
			}
		]
	}
});

export default instance;
```

For the rest we will use a handler. We could use hooks, but this way it will be more readable. Having `beforeRequest`, `beforeError` and `afterResponse` hooks for just a few lines of code would complicate things unnecessarily.

**Tip:**
> - It's a good practice to use hooks when your plugin gets complicated.
> - Try not to overload the handler function, but don't abuse hooks either.

```js
import got from 'got';

const instance = got.extend({
	prefixUrl: 'https://api.github.com',
	headers: {
		accept: 'application/vnd.github.v3+json'
	},
	responseType: 'json',
	context: {
		token: process.env.GITHUB_TOKEN,
	},
	hooks: {
		init: [
			(raw, options) => {
				if ('token' in raw) {
					options.context.token = raw.token;
					delete raw.token;
				}
			}
		]
	},
	handlers: [
		(options, next) => {
			// Authorization
			const {token} = options.context;
			if (token && !options.headers.authorization) {
				options.headers.authorization = `token ${token}`;
			}

			return next(options);
		}
	]
});

export default instance;
```

### Errors

We should name our errors, just to know if the error is from the API response. Superb errors, here we come!

```js
...
	handlers: [
		(options, next) => {
			// Authorization
			const {token} = options.context;
			if (token && !options.headers.authorization) {
				options.headers.authorization = `token ${token}`;
			}

			// Don't touch streams
			if (options.isStream) {
				return next(options);
			}

			// Magic begins
			return (async () => {
				try {
					const response = await next(options);

					return response;
				} catch (error) {
					const {response} = error;

					// Nicer errors
					if (response && response.body) {
						error.name = 'GitHubError';
						error.message = `${response.body.message} (${response.statusCode} status code)`;
					}

					throw error;
				}
			})();
		}
	]
...
```

Note that by providing our own errors in handlers, we don't alter the ones in `beforeError` hooks.\
The conversion is the last thing here.

### Rate limiting

Umm... `response.headers['x-ratelimit-remaining']` doesn't look good. What about `response.rateLimit.limit` instead?\
Yeah, definitely. Since `response.headers` is an object, we can easily parse these:

```js
const getRateLimit = (headers) => ({
	limit: Number.parseInt(headers['x-ratelimit-limit'], 10),
	remaining: Number.parseInt(headers['x-ratelimit-remaining'], 10),
	reset: new Date(Number.parseInt(headers['x-ratelimit-reset'], 10) * 1000)
});

getRateLimit({
	'x-ratelimit-limit': '60',
	'x-ratelimit-remaining': '55',
	'x-ratelimit-reset': '1562852139'
});
// => {
// 	limit: 60,
// 	remaining: 55,
// 	reset: 2019-07-11T13:35:39.000Z
// }
```

Let's integrate it:

```js
const getRateLimit = (headers) => ({
	limit: Number.parseInt(headers['x-ratelimit-limit'], 10),
	remaining: Number.parseInt(headers['x-ratelimit-remaining'], 10),
	reset: new Date(Number.parseInt(headers['x-ratelimit-reset'], 10) * 1000)
});

...
	handlers: [
		(options, next) => {
			// Authorization
			const {token} = options.context;
			if (token && !options.headers.authorization) {
				options.headers.authorization = `token ${token}`;
			}

			// Don't touch streams
			if (options.isStream) {
				return next(options);
			}

			// Magic begins
			return (async () => {
				try {
					const response = await next(options);

					// Rate limit for the Response object
					response.rateLimit = getRateLimit(response.headers);

					return response;
				} catch (error) {
					const {response} = error;

					// Nicer errors
					if (response && response.body) {
						error.name = 'GitHubError';
						error.message = `${response.body.message} (${response.statusCode} status code)`;
					}

					// Rate limit for errors
					if (response) {
						error.rateLimit = getRateLimit(response.headers);
					}

					throw error;
				}
			})();
		}
	]
...
```

### The frosting on the cake: `User-Agent` header.

```js
const packageJson = {
	name: 'gh-got',
	version: '12.0.0'
};

const instance = got.extend({
	...
	headers: {
		accept: 'application/vnd.github.v3+json',
		'user-agent': `${packageJson.name}/${packageJson.version}`
	},
	...
});
```

## Woah. Is that it?

Yup. View the full source code [here](examples/gh-got.js). Here's an example of how to use it:

```js
import ghGot from 'gh-got';

const response = await ghGot('users/sindresorhus');
const creationDate = new Date(response.created_at);

console.log(`Sindre's GitHub profile was created on ${creationDate.toGMTString()}`);
// => Sindre's GitHub profile was created on Sun, 20 Dec 2009 22:57:02 GMT
```

### Pagination

```js
import ghGot from 'gh-got';

const countLimit = 50;
const pagination = ghGot.paginate(
	'repos/sindresorhus/got/commits',
	{
		pagination: {countLimit}
	}
);

console.log(`Printing latest ${countLimit} Got commits (newest to oldest):`);

for await (const commitData of pagination) {
	console.log(commitData.commit.message);
}
```

That's... astonishing! We don't have to implement pagination on our own. Got handles it all.

### At the end

Did you know you can mix many instances into a bigger, more powerful one? Check out the [Advanced Creation](examples/advanced-creation.js) guide.
```

## File: `documentation/quick-start.md`
```markdown
# Quick Start Guide

## Getting and posting data with promises

The simplest `GET` request:

```js
import got from 'got';

const url = 'https://httpbin.org/anything';
const response = await got(url);
```

The call returns a <code>Promise<[Response](3-streams.md#response-1)></code>. If the body contains JSON, it can be retrieved directly:

```js
import got from 'got';

const url = 'https://httpbin.org/anything';
const data = await got(url).json();
```

The similar <code>[got.text](1-promise.md#promisetext)</code> method returns plain text.

All `got` methods accept an options object for passing extra configuration, such as headers:

```js
import got from 'got';

const url = 'https://httpbin.org/anything';

const options = {
	headers: {
		'Custom-Header': 'Quick start',
	},
	timeout: {
		send: 3500
	},
};

const data = await got(url, options).json();
```

A `POST` request is very similar:

```js
import got from 'got';

const url = 'https://httpbin.org/anything';

const options = {
	json: {
		documentName: 'Quick Start',
	},
};

const data = await got.post(url, options);
```

The request body is passed in the options object. The `json` property will automatically set headers accordingly. Custom headers can be added exactly as above.

## Using streams

The [Stream API](3-streams.md) allows to leverage [Node.js Streams](https://nodejs.dev/learn/nodejs-streams) capabilities:

```js
import fs from 'node:fs';
import {pipeline as streamPipeline} from 'node:stream/promises';
import got from 'got';

const url = 'https://httpbin.org/anything';

const options = {
	json: {
		documentName: 'Quick Start',
	},
};

const gotStream = got.stream.post(url, options);

const outStream = fs.createWriteStream('anything.json');

try {
	await streamPipeline(gotStream, outStream);
} catch (error) {
	console.error(error);
}
```

## Options

Options can be set at the client level and reused in subsequent queries:

```js
import got from 'got';

const options = {
	prefixUrl: 'https://httpbin.org',
	headers: {
		Authorization: getTokenFromVault(),
	},
};

const client = got.extend(options);

export default client;
```

Some noticeable common options are:
- [`searchParams`](2-options.md#searchparams): A query string object.
- [`prefixUrl`](2-options.md#prefixurl): Prepended to query paths. Paths must be relative to prefix, i.e. not begin with a `/`.
- [`method`](2-options.md#method): The HTTP method name.
- [`headers`](2-options.md#headers): Query headers.
- [`json`](2-options.md#json): JSON body.
- [`form`](2-options.md#form): A form query string object.

See the documentation for other [options](2-options.md#options).

## Errors

Both Promise and Stream APIs throw errors with metadata.

```js
import got from 'got';

try {
	const data = await got.get('https://httpbin.org/status/404');
} catch (error) {
	console.error(error.response.statusCode);
}
```

```js
import got from 'got';

const stream = got.stream
	.get('https://httpbin.org/status/404')
	.once('error', error => {
		console.error(error.response.statusCode);
	});
```

## Miscellaneous

The HTTP method name can also be given as an option, this may be convenient when it is known only at runtime:

```js
import got from 'got';

const url = 'https://httpbin.org/anything';

const method = 'POST';

const options = {
	method,
	json: {
		documentName: 'Quick Start',
	},
};

const data = await got(url, options);
```

For most apps, HTTP clients just do `GET` and `POST` queries (`PUT`, `PATCH` or `DELETE` methods work similarly).
The following sections will give some pointers to more advanced usage.

### Timeouts

By default, requests have no timeout. It is a good practice to set one:

```js
import got from 'got';

const options = {
	timeout: {
		request: 10000,
	},
};

const client = got.extend(options);

export default client;
```

The above sets a global timeout of 10000 milliseconds for all requests issued by the exported `client`. Like all options, timeouts can also be set at the request level. See the [`timeout` option](6-timeout.md#timeout-options).

### Retries

A failed request is retried twice. The retry policy may be tuned with a [`retry`](7-retry.md#retry) options object.

```js
import got from 'got';

const options = {
	retry: {
		limit: 5,
		errorCodes: [
			'ETIMEDOUT'
		],
	},
};
```

Retries with stream are a little trickier, see [`stream.on('retry', …)`](3-streams.md#streamonretry-).

### Hooks

Hooks are custom functions called on some request events:

```js
import got from 'got';

const logRetry = (error, retryCount) => {
	console.error(`Retrying after error ${error.code}, retry #: ${retryCount}`);
};

const options = {
	hooks: {
		beforeRetry: [
			logRetry,
		],
	},
};

const client = got.extend(options);

export default client;
```

*Note that hooks are given as arrays*, thus multiple hooks can be given. See documentation for other possible [hooks](9-hooks.md#hooks-api).

### Going further

There is a lot more to discover in the [documentation](../../../README.md#documentation) and [tips](../../../core/security/QUARANTINE/vetted/repos/hermes_agent/website/docs/guides/tips.md#tips). Among others, `Got` can handle [cookies](../../../core/security/QUARANTINE/vetted/repos/hermes_agent/website/docs/guides/tips.md#cookies), [pagination](4-pagination.md#pagination-api), [cache](../../../core/security/QUARANTINE/vetted/repos/trivy/docs/guide/configuration/cache.md#cache). Please read the documentation before implementing something that is already done by `Got` :innocent:.
```

## File: `documentation/tips.md`
```markdown
[> Back to homepage](../../../README.md#documentation)

## Tips

### Timeout

Each request can have a maximum allowed time to run.\
In order to use this, specify the `request` timeout option.

```js
import got from 'got';

const body = await got('https://httpbin.org/anything', {
	timeout: {
		request: 30000
	}
});
```

For more specific timeouts, visit the [Timeout API](6-timeout.md).

### Retries

By default, Got makes a new retry on a failed request if possible.

It is possible to disable this feature entirely by setting the amount of maximum allowed retries to `0`.

```js
import got from 'got';

const noRetryGot = got.extend({
	retry: {
		limit: 0
	}
});
```

In order to specify retriable errors, use the [Retry API](7-retry.md).

### Cookies

Got supports cookies out of box. There is no need to parse them manually.\
In order to use cookies, pass a `CookieJar` instance from the [`tough-cookie`](https://github.com/salesforce/tough-cookie) package.

```js
import got from 'got';
import {CookieJar} from 'tough-cookie';

const cookieJar = new CookieJar();

await cookieJar.setCookie('foo=bar', 'https://httpbin.org');
await got('https://httpbin.org/anything', {cookieJar});
```

### Sessions

You can create a session by extending Got with a shared `CookieJar`. This automatically saves and reuses cookies between requests:

```js
import got from 'got';
import {CookieJar} from 'tough-cookie';

const cookieJar = new CookieJar();
const sessionGot = got.extend({cookieJar});

// The cookie is saved within the cookie jar of the session
await sessionGot('http://httpbin.org/cookies/set?my_cookie=my_value');

await sessionGot('http://httpbin.org/cookies', {responseType: 'json', resolveBodyOnly: true});
//=> {cookies: {my_cookie: 'my_value'}}

// The cookies only apply to the session
await got('http://httpbin.org/cookies', {responseType: 'json', resolveBodyOnly: true});
//=> {cookies: {}}
```

This also works with caching and other Got features.

### AWS

Requests to AWS services need to have their headers signed.\
This can be accomplished by using the [`got4aws`](https://github.com/SamVerschueren/got4aws) package.

This is an example for querying an [`API Gateway`](https://docs.aws.amazon.com/apigateway/api-reference/signing-requests/) with a signed request.

```js
import got4aws from 'got4aws';

const got = got4aws();

const response = await got('https://<api-id>.execute-api.<api-region>.amazonaws.com/<stage>/endpoint/path', {
	// …
});
```

### Pagination

When working with large datasets, it's very efficient to use pagination.\
By default, Got uses the [`Link` header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Link) to retrieve the next page.\
However, this behavior can be customized, see the [Pagination API](4-pagination.md).

```js
const countLimit = 50;

const pagination = got.paginate('https://api.github.com/repos/sindresorhus/got/commits', {
	pagination: {countLimit}
});

console.log(`Printing latest ${countLimit} Got commits (newest to oldest):`);

for await (const commitData of pagination) {
	console.log(commitData.commit.message);
}
```

### Measuring traffic usage

You can measure the total bytes transferred (sent and received) for a request by accessing the underlying socket's `bytesWritten` and `bytesRead` properties.\
The socket is available via [`stream.socket`](3-streams.md#streamsocket) or [`response.request.socket`](3-streams.md#socket).

**Note:**
> - The socket's byte counters include HTTP headers and all protocol overhead, not just the request/response body.
> - The socket may be `undefined` when using cached responses.

```js
import got from 'got';

const stream = got.stream('https://httpbin.org/json');

stream.on('response', () => {
	console.log(`Downloaded: ${stream.socket.bytesRead} bytes`);
	console.log(`Uploaded: ${stream.socket.bytesWritten} bytes`);
});

stream.on('end', () => {
	const totalTraffic = stream.socket.bytesRead + stream.socket.bytesWritten;
	console.log(`Total traffic: ${totalTraffic} bytes`);
});

stream.resume();
```

You can also access the socket when using the Promise API:

```js
import got from 'got';

const request = got('https://httpbin.org/json');

request.on('response', response => {
	console.log(`Downloaded: ${response.request.socket.bytesRead} bytes`);
	console.log(`Uploaded: ${response.request.socket.bytesWritten} bytes`);
});

const response = await request;

if (response.request.socket) {
	const totalTraffic = response.request.socket.bytesRead + response.request.socket.bytesWritten;
	console.log(`Total traffic: ${totalTraffic} bytes`);
}
```

### Rate limiting (throttling transfer speed)

Got doesn't include built-in bandwidth throttling, but you can implement it using stream transformers.

> [!NOTE]
> - To limit total transfer **size** (not rate), see the [advanced-creation example](examples/advanced-creation.js).
> - For production use, consider something like  [`bandwidth-throttle-stream`](https://github.com/patrickkunka/bandwidth-throttle-stream).

```js
import got from 'got';
import {Transform} from 'node:stream';
import {setTimeout} from 'node:timers/promises';

class ThrottleTransform extends Transform {
	constructor(bytesPerSecond) {
		super();
		this.bytesPerSecond = bytesPerSecond;
	}

	async _transform(chunk, encoding, callback) {
		const delay = (chunk.length / this.bytesPerSecond) * 1000;
		if (delay > 0) {
			await setTimeout(delay);
		}

		callback(null, chunk);
	}
}

// Throttle download
got.stream('https://httpbin.org/bytes/1048576')
	.pipe(new ThrottleTransform(100000)) // 100 KB/s
	.pipe(process.stdout);
```

For uploads, throttle the body stream before passing to Got:

```js
import {createReadStream} from 'node:fs';

await got.post('https://httpbin.org/post', {
	body: createReadStream('file.bin').pipe(new ThrottleTransform(100000))
});
```

<a name="unix"></a>
### UNIX Domain Sockets

See the [`enableUnixSockets` option](./2-options.md#enableunixsockets).

### Testing

Got uses the native [`http`](https://nodejs.org/api/http.html) module, which depends on the native [`net`](https://nodejs.org/api/net.html) module.\
This means there are two possible ways to test:

1. Use a mocking library like [`nock`](https://github.com/nock/nock),
2. Create a server.

The first approach should cover all common use cases.\
Bear in mind that it overrides the native `http` module, so bugs may occur due to the differences.

The most solid way is to create a server.\
There may be cases where `nock` won't be sufficient or lacks functionality.

#### Nock

By default `nock` mocks only one request.\
Got will [retry](7-retry.md) on failed requests by default, causing a `No match for request ...` error.\
The solution is to either disable retrying (set `options.retry.limit` to `0`) or call `.persist()` on the mocked request.

```js
import got from 'got';
import nock from 'nock';

const scope = nock('https://sindresorhus.com')
	.get('/')
	.reply(500, 'Internal server error')
	.persist();

try {
	await got('https://sindresorhus.com')
} catch (error) {
	console.log(error.response.body);
	//=> 'Internal server error'

	console.log(error.response.retryCount);
	//=> 2
}

scope.persist(false);
```

### Proxying

**Note:**
> - The popular [`tunnel`](https://www.npmjs.com/package/tunnel) package is unmaintained. Use at your own risk.
> - The [`proxy-agent`](https://www.npmjs.com/package/proxy-agent) family doesn't follow newest Node.js features and lacks support.

Although there isn't a perfect, bug-free package, [Apify](https://apify.com/)'s solution is a modern one.\
See [`got-scraping/src/agent/h1-proxy-agent.ts`](https://github.com/apify/got-scraping/blob/2ec7f9148917a6a38d6d1c8c695606767c46cce5/src/agent/h1-proxy-agent.ts). It has the same API as `hpagent`.

[`hpagent`](https://github.com/delvedor/hpagent) is a modern package as well. In contrast to `tunnel`, it allows keeping the internal sockets alive to be reused.

```js
import got from 'got';
import {HttpsProxyAgent} from 'hpagent';

await got('https://sindresorhus.com', {
	agent: {
		https: new HttpsProxyAgent({
			keepAlive: true,
			keepAliveMsecs: 1000,
			maxSockets: 256,
			maxFreeSockets: 256,
			scheduling: 'lifo',
			proxy: 'https://localhost:8080'
		})
	}
});
```

Alternatively, use [`global-agent`](https://github.com/gajus/global-agent) to configure a global proxy for all HTTP/HTTPS traffic in your program.

If you're using HTTP/2, the [`http2-wrapper`](https://github.com/szmarczak/http2-wrapper/#proxy-support) package provides proxy support out-of-box.\
[Learn more.](https://github.com/szmarczak/http2-wrapper#proxy-support)

### Retry without an agent

If you're using proxies, you may run into connection issues.\
One way out is to disable proxies when retrying. The solution for the Stream API looks like this:

```js
import https from 'node:https';
import fs from 'node:fs';
import got from 'got';

class MyAgent extends https.Agent {
	createConnection(port, options, callback) {
		console.log(`Connecting with MyAgent`);
		return https.Agent.prototype.createConnection.call(this, port, options, callback);
	}
}

const proxy = new MyAgent();

let writeStream;

const fn = retryStream => {
	const options = {
		agent: {
			https: proxy,
		}
	};

	const stream = retryStream ?? got.stream('https://example.com', options);

	if (writeStream) {
		writeStream.destroy();
	}

	writeStream = fs.createWriteStream('example-com.html');

	stream.pipe(writeStream);
	stream.once('retry', (retryCount, error, createRetryStream) => {
		fn(createRetryStream({
			agent: {
				http: undefined,
				https: undefined,
				http2: undefined,
			},
		}));
	});
};

fn();
```

### `h2c`

There is no direct [`h2c`](https://datatracker.ietf.org/doc/html/rfc7540#section-3.1) support.

However, you can provide a `h2session` option in a `beforeRequest` hook. See [an example](examples/h2c.js).

### Uppercase headers

Got always normalizes the headers, therefore passing an `Uppercase-Header` will transform it into `uppercase-header`. To fix this, you need to pass a wrapped agent:

```js
class WrappedAgent {
    constructor(agent) {
        this.agent = agent;
    }

    addRequest(request, options) {
        return this.agent.addRequest(request, options);
    }

    get keepAlive() {
        return this.agent.keepAlive;
    }

    get maxSockets() {
        return this.agent.maxSockets;
    }

    get options() {
        return this.agent.options;
    }

    get defaultPort() {
        return this.agent.defaultPort;
    }

    get protocol() {
        return this.agent.protocol;
    }
}

class TransformHeadersAgent extends WrappedAgent {
    addRequest(request, options) {
        const headers = request.getHeaderNames();

        for (const header of headers) {
            request.setHeader(this.transformHeader(header), request.getHeader(header));
        }

        return super.addRequest(request, options);
    }

    transformHeader(header) {
        return header.split('-').map(part => {
            return part[0].toUpperCase() + part.slice(1);
        }).join('-');
    }
}

const agent = new http.Agent({
    keepAlive: true
});

const wrappedAgent = new TransformHeadersAgent(agent);
```

See [an example](examples/uppercase-headers.js).

### Custom options

Got v12 throws when an option does not exist. Therefore passing a top-level option such as:

```js
import got from 'got';

await got('https://example.com', {
	foo: 'bar'
});
```

will throw. To prevent this, you need read the option in an `init` hook:

```js
import got from 'got';

const convertFoo = got.extend({
	hooks: {
		init: [
			(rawOptions, options) => {
				if ('foo' in rawOptions) {
					options.context.foo = rawOptions.foo;
					delete rawOptions.foo;
				}
			}
		]
	}
});

const instance = got.extend(convertFoo, {
	hooks: {
		beforeRequest: [
			options => {
				options.headers.foo = options.context.foo;
			}
		]
	}
});

const {headers} = await instance('https://httpbin.org/anything', {foo: 'bar'}).json();
console.log(headers.Foo); //=> 'bar'
```

Eventually, you may want to create a catch-all instance:

```js
import got from 'got';

const catchAllOptions = got.extend({
    hooks: {
        init: [
            (raw, options) => {
                for (const key in raw) {
                    if (!(key in options)) {
                        options.context[key] = raw[key];
                        delete raw[key];
                    }
                }
            }
        ]
    }
});

const instance = got.extend(catchAllOptions, {
	hooks: {
		beforeRequest: [
			options => {
				// All custom options will be visible under `options.context`
				options.headers.foo = options.context.foo;
			}
		]
	}
});

const {headers} = await instance('https://httpbin.org/anything', {foo: 'bar'}).json();
console.log(headers.Foo); //=> 'bar'
```

**Note:**
> - It's a good practice to perform the validation inside the `init` hook. You can safely throw when an option is unknown! Internally, Got uses the [`@sindresorhus/is`](https://github.com/sindresorhus/is) package.

### Electron `net` module is not supported

**Note:** Got v12 and later is an ESM package, but Electron does not yet support ESM. So you need to use Got v11.

Got doesn't support the `electron.net` module. It's missing crucial APIs that are available in Node.js.\
While Got used to support `electron.net`, it got very unstable and caused many errors.

However, you can use [IPC communication](https://www.electronjs.org/docs/api/ipc-main#ipcmainhandlechannel-listener) to get the Response object:

```js
// Main process
const got = require('got');

const instance = got.extend({
	// ...
});

ipcMain.handle('got', async (event, ...args) => {
	const {statusCode, headers, body} = await instance(...args);
	return {statusCode, headers, body};
});

// Renderer process
async () => {
	const {statusCode, headers, body} = await ipcRenderer.invoke('got', 'https://httpbin.org/anything');
	// ...
}
```
```

## File: `documentation/typescript.md`
```markdown
[> Back to homepage](../../../README.md#documentation)

## TypeScript

Got is fully written in TypeScript, so the integration is seamless.\
Furthermore, types have saved Got from many bugs and inconsistencies.

### Wrapping Got in an API client

You can wrap Got in a type-safe API client while preserving all Got features including progress/events support:

```typescript
import got, {type RequestPromise, type OptionsOfJSONResponseBody, type Progress} from 'got';

interface FizzBuzz {
	fizz: boolean;
	buzz: boolean;
}

class ExampleAPI {
	private client = got.extend({
		prefixUrl: 'https://api.example.com'
	});

	isFizzBuzz(number: number): RequestPromise<FizzBuzz> {
		return this.client.get('fizzbuzz', {
			searchParams: {number},
			responseType: 'json',
			resolveBodyOnly: true
		}).json<FizzBuzz>();
	}

	// For more complex cases, you can specify options
	getData(id: string, options?: OptionsOfJSONResponseBody): RequestPromise<FizzBuzz> {
		return this.client.get(`data/${id}`, {
			...options,
			responseType: 'json',
			resolveBodyOnly: true
		}).json<FizzBuzz>();
	}
}

const api = new ExampleAPI();

// The promise has full type support
const promise = api.isFizzBuzz(20);

// Event methods are available
promise.on('downloadProgress', (progress: Progress) => {
	console.log(progress.percent);
});

// The result is properly typed
const result = await promise;
console.log(result.fizz); // boolean
console.log(result.buzz); // boolean
```

**Note:**
> - Use `.json<T>()` to get `RequestPromise<T>` with the body-only response.
> - Use `.buffer()` or `.text()` for other response types.
> - Without calling these methods, you'll get `RequestPromise<Response<T>>`.
> - Use `signal` and `AbortController` to abort requests.

### Types

Here's a list of types that Got exports:

**Note:**
> - The list may be incomplete. If you find a type is missing, please open an issue about it.

### [`Got`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/types.ts#L200)

### [`GotStream`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/types.ts#L195)

### [`GotRequestFunction`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/types.ts#L142)

### [`GotPaginate`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/types.ts#L87)

### [`OptionsWithPagination<T = unknown, R = unknown>`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/types.ts#L82)

### [`OptionsOfTextResponseBody`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/types.ts#L74)

### [`OptionsOfJSONResponseBody`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/types.ts#L75)

### [`OptionsOfBufferResponseBody`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/types.ts#L76)

### [`OptionsOfUnknownResponseBody`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/types.ts#L77)

### [`StrictOptions`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/types.ts#L78)

### [`StreamOptions`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/types.ts#L79)

### [`OptionsInit`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/core/options.ts#L535)

### [`ExtendOptions`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/types.ts#L55)

### [`PlainResponse`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/core/response.ts#L6)

### [`Response<T = unknown>`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/core/response.ts#L95)

### [`Request`](https://github.com/sindresorhus/got/blob/ecb05343dea3bd35933585a1ec5bcea01348d109/source/core/index.ts#L139)

### [`RequestEvents<T>`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/core/index.ts#L108)

### [`Progress`](https://github.com/sindresorhus/got/blob/0f9f2b83b77710f2dc08c2a6bce1c78ba8d46760/source/core/index.ts#L40)

### [`InstanceDefaults`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/types.ts#L17)

### [`GotReturn`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/types.ts#L44)

### [`HandlerFunction`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/types.ts#L50)

### [`RequestPromise<T extends Response | Response['body'] = Response['body']>`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/as-promise/types.ts#L26)

### [`Delays`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/core/timed-out.ts#L14)

### [`CreateConnectionFunction`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/core/options.ts#L302)

### [`CheckServerIdentityFunction`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/core/options.ts#L303)

### [`CacheOptions`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/core/options.ts#L305)

### [`HttpsOptions`](https://github.com/sindresorhus/got/blob/ae04c0e36cf3f5b2e356df7d48a5b19988f935a2/source/core/options.ts#L319)

### [`PaginateData<BodyType, ElementType>`](https://github.com/sindresorhus/got/blob/215e06a4993329578d92d4f44607913239a03094/source/core/options.ts#L382)

### [`PaginationOptions<ElementType, BodyType>`](https://github.com/sindresorhus/got/blob/215e06a4993329578d92d4f44607913239a03094/source/core/options.ts#L397)

### [`SearchParameters`](https://github.com/sindresorhus/got/blob/215e06a4993329578d92d4f44607913239a03094/source/core/options.ts#L504)

### [`ResponseType`](https://github.com/sindresorhus/got/blob/215e06a4993329578d92d4f44607913239a03094/source/core/options.ts#L518)

### [`FilterData<ElementType>`](https://github.com/sindresorhus/got/blob/215e06a4993329578d92d4f44607913239a03094/source/core/options.ts#L388)

### [`RetryObject`](https://github.com/sindresorhus/got/blob/215e06a4993329578d92d4f44607913239a03094/source/core/options.ts#L259)

### [`RetryFunction`](https://github.com/sindresorhus/got/blob/215e06a4993329578d92d4f44607913239a03094/source/core/options.ts#L267)

### [`ParseJsonFunction`](https://github.com/sindresorhus/got/blob/215e06a4993329578d92d4f44607913239a03094/source/core/options.ts#L235)

### [`StringifyJsonFunction`](https://github.com/sindresorhus/got/blob/215e06a4993329578d92d4f44607913239a03094/source/core/options.ts#L236)

### [`Method`](https://github.com/sindresorhus/got/blob/215e06a4993329578d92d4f44607913239a03094/source/core/options.ts#L241)

### [`ToughCookieJar`](https://github.com/sindresorhus/got/blob/215e06a4993329578d92d4f44607913239a03094/source/core/options.ts#L53)

### [`PromiseCookieJar`](https://github.com/sindresorhus/got/blob/215e06a4993329578d92d4f44607913239a03094/source/core/options.ts#L60)

### [`DnsLookupIpVersion`](https://github.com/sindresorhus/got/blob/215e06a4993329578d92d4f44607913239a03094/source/core/options.ts#L35)

### [`RequestFunction`](https://github.com/sindresorhus/got/blob/215e06a4993329578d92d4f44607913239a03094/source/core/options.ts#L43)

### [`Agents`](https://github.com/sindresorhus/got/blob/215e06a4993329578d92d4f44607913239a03094/source/core/options.ts#L45)

### [`Headers`](https://github.com/sindresorhus/got/blob/215e06a4993329578d92d4f44607913239a03094/source/core/options.ts#L51)

### [`Hooks`](https://github.com/sindresorhus/got/blob/215e06a4993329578d92d4f44607913239a03094/source/core/options.ts#L75)

### [`InitHook`](https://github.com/sindresorhus/got/blob/215e06a4993329578d92d4f44607913239a03094/source/core/options.ts#L65)

### [`BeforeRequestHook`](https://github.com/sindresorhus/got/blob/215e06a4993329578d92d4f44607913239a03094/source/core/options.ts#L66)

### [`BeforeRedirectHook`](https://github.com/sindresorhus/got/blob/215e06a4993329578d92d4f44607913239a03094/source/core/options.ts#L67)

### [`BeforeErrorHook`](https://github.com/sindresorhus/got/blob/215e06a4993329578d92d4f44607913239a03094/source/core/options.ts#L68)

### [`BeforeRetryHook`](https://github.com/sindresorhus/got/blob/215e06a4993329578d92d4f44607913239a03094/source/core/options.ts#L69)

### [`AfterResponseHook`](https://github.com/sindresorhus/got/blob/215e06a4993329578d92d4f44607913239a03094/source/core/options.ts#L70)
```

## File: `documentation/examples/advanced-creation.js`
```javascript
import process from 'node:process';
import crypto from 'node:crypto';
import got from '../../dist/source/index.js';

// Signing requests

/*
Got supports composing multiple instances together. This is very powerful.

You can create a client that limits download/upload size, then compose it with an instance that signs a request.

It's like plugins without any of the plugin mess.
You just create instances and then compose them together.

To mix them use `instanceA.extend(instanceB, instanceC, ...)`, that's all.

Let's begin.
*/

// Logging all `got(…)` calls
const logger = got.extend({
	handlers: [
		(options, next) => {
			console.log(`Sending ${options.method} to ${options.url}`);
			return next(options);
		},
	],
});

// Denying redirects to foreign hosts
const controlRedirects = got.extend({
	hooks: {
		beforeRedirect: [
			(options, response) => {
				const {origin} = response.request.options.url;
				if (options.url.origin !== origin) {
					throw new Error(`Redirection to ${options.url.origin} is not allowed from ${origin}`);
				}
			},
		],
	},
});

// Limiting download & upload size
// This can prevent crashing due to insufficient memory
const limitDownloadUpload = got.extend({
	handlers: [
		(options, next) => {
			const {downloadLimit, uploadLimit} = options.context;

			// Create an AbortController if limits are set and signal not already provided
			let controller;
			let {signal} = options;

			if ((downloadLimit || uploadLimit) && !signal) {
				controller = new AbortController();
				signal = controller.signal;
				options.signal = signal;
			}

			const promiseOrStream = next(options);

			if (typeof downloadLimit === 'number') {
				promiseOrStream.on('downloadProgress', progress => {
					if (progress.transferred > downloadLimit && progress.percent !== 1) {
						const error = new Error(`Exceeded the download limit of ${downloadLimit} bytes`);

						if (options.isStream) {
							promiseOrStream.destroy(error);
						} else {
							controller?.abort(error);
						}
					}
				});
			}

			if (typeof uploadLimit === 'number') {
				promiseOrStream.on('uploadProgress', progress => {
					if (progress.transferred > uploadLimit && progress.percent !== 1) {
						const error = new Error(`Exceeded the upload limit of ${uploadLimit} bytes`);

						if (options.isStream) {
							promiseOrStream.destroy(error);
						} else {
							controller?.abort(error);
						}
					}
				});
			}

			return promiseOrStream;
		},
	],
});

// No user agent
const noUserAgent = got.extend({
	headers: {
		'user-agent': undefined,
	},
});

// Custom endpoint
const httpbin = got.extend({
	prefixUrl: 'https://httpbin.org/',
});

const getMessageSignature = (data, secret) => crypto.createHmac('sha256', secret).update(data).digest('hex').toUpperCase();
const signRequest = got.extend({
	hooks: {
		beforeRequest: [
			options => {
				const secret = options.context.secret ?? process.env.SECRET;

				if (secret) {
					options.headers.sign = getMessageSignature(options.body ?? '', secret);
				}
			},
		],
	},
});

/*
* Putting it all together
*/
const merged = got.extend(
	noUserAgent,
	logger,
	limitDownloadUpload,
	httpbin,
	signRequest,
	controlRedirects,
);

// There's no 'user-agent' header :)
const {headers} = await merged.post('anything', {
	body: 'foobar',
	context: {
		secret: 'password',
	},
}).json();

console.log(headers);
// Sending POST to https://httpbin.org/anything
// {
//   Accept: 'application/json',
//   'Accept-Encoding': 'gzip, deflate, br',
//   'Content-Length': '6',
//   Host: 'httpbin.org',
//   Sign: 'EB0167A1EBF205510BAFF5DA1465537944225F0E0140E1880B746F361FF11DCA'
// }

const MEGABYTE = 1_048_576;
try {
	await merged('https://pop-iso.sfo2.cdn.digitaloceanspaces.com/21.04/amd64/intel/5/pop-os_21.04_amd64_intel_5.iso', {
		context: {
			downloadLimit: MEGABYTE,
		},
		prefixUrl: '',
	});
} catch (error) {
	// AbortError: This operation was aborted.
	console.log(error.message);
}
```

## File: `documentation/examples/gh-got.js`
```javascript
import process from 'node:process';
import got from '../../dist/source/index.js';

const packageJson = {
	name: 'gh-got',
	version: '12.0.0',
};

const getRateLimit = headers => ({
	limit: Number.parseInt(headers['x-ratelimit-limit'], 10),
	remaining: Number.parseInt(headers['x-ratelimit-remaining'], 10),
	reset: new Date(Number.parseInt(headers['x-ratelimit-reset'], 10) * 1000),
});

const instance = got.extend({
	prefixUrl: 'https://api.github.com',
	headers: {
		accept: 'application/vnd.github.v3+json',
		'user-agent': `${packageJson.name}/${packageJson.version}`,
	},
	responseType: 'json',
	context: {
		token: process.env.GITHUB_TOKEN,
	},
	hooks: {
		init: [
			(raw, options) => {
				if ('token' in raw) {
					options.context.token = raw.token;
					delete raw.token;
				}
			},
		],
	},
	handlers: [
		(options, next) => {
			// Authorization
			const {token} = options.context;
			if (token && !options.headers.authorization) {
				options.headers.authorization = `token ${token}`;
			}

			// Don't touch streams
			if (options.isStream) {
				return next(options);
			}

			// Magic begins
			return (async () => {
				try {
					const response = await next(options);

					// Rate limit for the Response object
					response.rateLimit = getRateLimit(response.headers);

					return response;
				} catch (error) {
					const {response} = error;

					// Nicer errors
					if (response && response.body) {
						error.name = 'GitHubError';
						error.message = `${response.body.message} (${response.statusCode} status code)`;
					}

					// Rate limit for errors
					if (response) {
						error.rateLimit = getRateLimit(response.headers);
					}

					throw error;
				}
			})();
		},
	],
});

export default instance;
```

## File: `documentation/examples/h2c.js`
```javascript
import http2 from 'http2-wrapper';
import got from '../../dist/source/index.js';

let sessions = {};
const getSession = ({origin}) => {
	if (sessions[origin] && !sessions[origin].destroyed) {
		return sessions[origin];
	}

	const session = http2.connect(origin);
	session.once('error', () => {
		delete sessions[origin];
	});

	sessions[origin] = session;

	return session;
};

const closeSessions = () => {
	for (const key in sessions) {
		if (!Object.hasOwn(sessions, key)) {
			continue;
		}

		sessions[key].close();
	}

	sessions = {};
};

const instance = got.extend({
	hooks: {
		beforeRequest: [
			options => {
				options.h2session = getSession(options.url);
				options.http2 = true;
				options.request = http2.request;
			},
		],
	},
});

const server = http2.createServer((request, response) => {
	response.end('{}');
});

server.listen(async () => {
	const url = `http://localhost:${server.address().port}`;
	const {body, headers} = await instance(url, {context: {h2c: true}});
	console.log(headers, body);

	closeSessions();
	server.close();
});
```

## File: `documentation/examples/pagination.js`
```javascript
import Bourne from '@hapi/bourne';
import got from '../../dist/source/index.js';

const max = Date.now() - (1000 * 86_400 * 7);

const iterator = got.paginate('https://api.github.com/repos/sindresorhus/got/commits', {
	pagination: {
		paginate({response, currentItems}) {
			// If there are no more data, finish.
			if (currentItems.length === 0) {
				return false;
			}

			// Get the current page number.
			const {searchParams} = response.request.options;
			const previousPage = Number(searchParams.get('page') ?? 1);

			// Update the page number by one.
			return {
				searchParams: {
					page: previousPage + 1,
				},
			};
		},
		// Using `Bourne` to prevent prototype pollution.
		transform: response => Bourne.parse(response.body),
		filter({item}) {
			// Check if the commit time exceeds our range.
			const date = new Date(item.commit.committer.date);
			const end = date.getTime() - max >= 0;

			return end;
		},
		shouldContinue({item}) {
			// Check if the commit time exceeds our range.
			const date = new Date(item.commit.committer.date);
			const end = date.getTime() - max >= 0;

			return end;
		},
		// We want only 50 results.
		countLimit: 50,
		// Wait 1s before making another request to prevent API rate limiting.
		backoff: 1000,
		// It is a good practice to set an upper limit of how many requests can be made.
		// This way we can avoid infinite loops.
		requestLimit: 10,
		// In this case, we don't need to store all the items we receive.
		// They are processed immediately.
		stackAllItems: false,
	},
});

console.log('Last 50 commits from now to week ago:');
for await (const item of iterator) {
	console.log(item.commit.message.split('\n')[0]);
}
```

## File: `documentation/examples/runkit-example.js`
```javascript
import got from 'got';

const issUrl = 'http://api.open-notify.org/iss-now.json';

const {iss_position: issPosition} = await got(issUrl).json();

console.log(issPosition);
//=> {latitude: '20.4956', longitude: '42.2216'}
```

## File: `documentation/examples/uppercase-headers.js`
```javascript
import http from 'node:http';
import got from '../../dist/source/index.js';

// Wraps an existing Agent instance
class WrappedAgent {
	constructor(agent) {
		this.agent = agent;
	}

	addRequest(request, options) {
		return this.agent.addRequest(request, options);
	}

	get keepAlive() {
		return this.agent.keepAlive;
	}

	get maxSockets() {
		return this.agent.maxSockets;
	}

	get options() {
		return this.agent.options;
	}

	get defaultPort() {
		return this.agent.defaultPort;
	}

	get protocol() {
		return this.agent.protocol;
	}
}

class TransformHeadersAgent extends WrappedAgent {
	addRequest(request, options) {
		const headers = request.getHeaderNames();

		for (const header of headers) {
			request.setHeader(this.transformHeader(header), request.getHeader(header));
		}

		return super.addRequest(request, options);
	}

	transformHeader(header) {
		return header.split('-').map(part => part[0].toUpperCase() + part.slice(1)).join('-');
	}
}

const agent = new http.Agent({
	keepAlive: true,
});

const wrappedAgent = new TransformHeadersAgent(agent);

const main = async () => {
	const headers = await got(`http://localhost:${server.address().port}`, {
		agent: {
			http: wrappedAgent,
		},
		headers: {
			foo: 'bar',
		},
	}).json();

	console.log(headers);

	agent.destroy();
	server.close();
};

const server = http.createServer((request, response) => {
	const {rawHeaders} = request;
	const headers = {};

	for (let i = 0; i < rawHeaders.length; i += 2) {
		headers[rawHeaders[i]] = rawHeaders[i + 1];
	}

	response.end(JSON.stringify(headers));
}).listen(0, main);
```

## File: `documentation/migration-guides/axios.md`
```markdown
[> Back to homepage](../../../README.md#documentation)

## Migration guides

> You may think it's too hard to switch, but it's really not. 🦄

### Axios

Axios is very similar to Got. The difference is that Axios targets browsers first, while Got fully makes use of Node.js features.

#### Common options

These options remain the same as well:

- [`url`](../2-options.md#url)
- [`method`](../2-options.md#method)
- [`headers`](../2-options.md#headers)
- [`maxRedirects`](../2-options.md#maxredirects)
- [`decompress`](../2-options.md#decompress)

#### Renamed options

We deeply care about readability, so we renamed these options:

- `httpAgent` → [`agent.http`](../2-options.md#agent)
- `httpsAgent` → [`agent.https`](../2-options.md#agent)
- `socketPath` → [`url`](../2-options.md#enableunixsockets)
- `responseEncoding` → [`encoding`](../2-options.md#encoding)
- `auth.username` → [`username`](../2-options.md#username)
- `auth.password` → [`password`](../2-options.md#password)
- `data` → [`body`](../2-options.md#body) / [`json`](../2-options.md#json) / [`form`](../2-options.md#form)
- `params` → [`searchParams`](../2-options.md#searchparams)

#### Changes in behavior

- `transformRequest` → [`hooks.beforeRequest`](../9-hooks.md#beforerequest)
  - The API is different.
- `transformResponse` → [`hooks.afterResponse`](../9-hooks.md#afterresponse)
  - The API is different.
- `baseUrl` → [`prefixUrl`](../2-options.md#prefixurl)
  - The `prefixUrl` is always prepended to the `url`.
- [`timeout`](../6-timeout.md)
  - This option is now an object. You can now set timeouts on particular events!
- [`responseType`](../2-options.md#responsetype)
  - Accepts `'text'`, `'json'` or `'buffer'`.

#### Breaking changes

- `onUploadProgress`
  - This option does not exist. Instead, use [`got(…).on('uploadProgress', …)`](../3-streams.md#uploadprogress).
- `onDownloadProgress`
  - This option does not exist. Instead, use [`got(…).on('downloadProgress', …)`](../3-streams.md#downloadprogress).
- `maxContentLength`
  - This option does not exist. Instead, use [a handler](../examples/advanced-creation.js).
- `validateStatus`
  - This option does not exist. Got automatically validates the status according to [the specification](https://datatracker.ietf.org/doc/html/rfc7231#section-6).
- `proxy`
  - This option does not exist. You need to pass [an `agent`](../../../core/security/QUARANTINE/vetted/repos/hermes_agent/website/docs/guides/tips.md#proxy) instead.
- `cancelToken`
  - Use the [`signal`](../2-options.md#signal) option with [`AbortController`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController).
- `paramsSerializer`
  - This option does not exist.
- `maxBodyLength`
  - This option does not exist.

#### Response

The response object is different as well:

- `response.data` → [`response.body`](../3-streams.md#response-1)
- `response.status` → [`response.statusCode`](../3-streams.md#response-1)
- `response.statusText` → [`response.statusMessage`](../3-streams.md#response-1)
- `response.config` → [`response.request.options`](../3-streams.md#response-1)
- [`response.request`](../3-streams.md#response-1)
  - Returns [a Got stream](../3-streams.md).

The `response.headers` object remains the same.

#### Interceptors

Got offers [hooks](../9-hooks.md) instead, which are more flexible.

#### Errors

Errors look the same, with the difference `error.request` returns a Got stream. Furthermore, Got provides [more details](../8-errors.md) to make debugging easier.

#### Abort

Got supports [`AbortController`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController) via the [`signal`](../2-options.md#signal) option.

#### Convenience methods

Convenience methods, such as `axios.get(…)` etc. remain the same: `got.get(…)`. Instead of `axios.create(…)` use `got.extend(…)`.

#### You're good to go!

Well, you have already come this far :tada:\
Take a look at the [documentation](../../../README.md#documentation). It's worth the time to read it.\
There are [some great tips](../../../core/security/QUARANTINE/vetted/repos/hermes_agent/website/docs/guides/tips.md).

If something is unclear or doesn't work as it should, don't hesitate to [open an issue](https://github.com/sindresorhus/got/issues/new/choose).
```

## File: `documentation/migration-guides/nodejs.md`
```markdown
[> Back to homepage](../../../README.md#documentation)

## Migration guides

> You may think it's too hard to switch, but it's really not. 🦄

### Node.js

Let's make a simple request. With Node.js, this is:

```js
import http from 'node:http';

const request = http.request('https://httpbin.org/anything', response => {
	if (response.statusCode >= 400) {
		request.destroy(new Error());
		return;
	}

	const chunks = [];
	let totalLength = 0;

	response.on('data', chunk => {
		chunks.push(chunk);
		totalLength += chunk.length;
	});

	response.once('end', () => {
		const bytes = new Uint8Array(totalLength);
		let offset = 0;
		for (const chunk of chunks) {
			bytes.set(chunk, offset);
			offset += chunk.length;
		}

		if (response.statusCode >= 400) {
			const error = new Error(`Unsuccessful response: ${response.statusCode}`);
			error.body = new TextDecoder().decode(bytes);
			return;
		}

		const text = new TextDecoder().decode(bytes);

		console.log(text);
	});

	response.once('error', console.error);
});

request.once('error', console.error);
request.end();
```

With Got, this becomes:

```js
import got from 'got';

try {
	const {body} = await got('https://httpbin.org/anything');
	console.log(body);
} catch (error) {
	console.error(error);
}
```

Much cleaner. But what about streams?

```js
import http from 'node:http';
import fs from 'node:fs';

const source = fs.createReadStream('article.txt');

const request = http.request('https://httpbin.org/anything', {
	method: 'POST'
}, response => {
	response.pipe(fs.createWriteStream('httpbin.txt'));
});

source.pipe(request);
```

Well, it's easy as that:

```js
import got from 'got';
import {pipeline as streamPipeline} from 'node:stream/promises';
import fs from 'node:fs';

await streamPipeline(
	fs.createReadStream('article.txt'),
	got.stream.post('https://httpbin.org/anything'),
	fs.createWriteStream('httpbin.txt')
);
```

The advantage is that Got also handles errors automatically, so you don't have to create custom listeners.

Furthermore, Got supports redirects, compression, advanced timeouts, cache, pagination, cookies, hooks, and more!

#### What next?

Unfortunately Got options differ too much from the Node.js options. It's not possible to provide a brief summary.\
Don't worry, you will learn them fast - they are easy to understand! Every option has an example attached.

Take a look at the [documentation](../../../README.md#documentation). It's worth the time to read it.\
There are [some great tips](../../../core/security/QUARANTINE/vetted/repos/hermes_agent/website/docs/guides/tips.md).

If something is unclear or doesn't work as it should, don't hesitate to [open an issue](https://github.com/sindresorhus/got/issues/new/choose).
```

## File: `documentation/migration-guides/request.md`
```markdown
[> Back to homepage](../../../README.md#documentation)

## Migration guides

> You may think it's too hard to switch, but it's really not. 🦄

### Request

Let's take the very first example from [Request's readme](https://github.com/request/request#super-simple-to-use):

```js
import request from 'request';

request('https://google.com', (error, response, body) => {
	console.log('error:', error);
	console.log('statusCode:', response && response.statusCode);
	console.log('body:', body);
});
```

With Got, it is:

```js
import got from 'got';

try {
	const response = await got('https://google.com');
	console.log('statusCode:', response.statusCode);
	console.log('body:', response.body);
} catch (error) {
	console.log('error:', error);
}
```

Looks better now, huh? 😎

#### Common options

These Got options are the same as with Request:

- [`url`](../2-options.md#url)
- [`body`](../2-options.md#body)
- [`followRedirect`](../2-options.md#followredirect)
- [`encoding`](../2-options.md#encoding)
- [`maxRedirects`](../2-options.md#maxredirects)
- [`localAddress`](../2-options.md#localaddress)
- [`headers`](../2-options.md#headers)
- [`createConnection`](../2-options.md#createconnection)
- [UNIX sockets](../2-options.md#enableunixsockets): `http://unix:SOCKET:PATH`

The `time` option does not exist, assume [it's always true](../6-timeout.md).

So if you're familiar with these, you're good to go.

#### Renamed options

**Note:**
> - Got stores HTTPS options inside [`https`](../2-options.md#https). Some of them have been renamed. [Read more](../5-https.md).

Readability is very important to us, so we have different names for these options:

- `qs` → [`searchParams`](../2-options.md#searchparams)
- `strictSSL` → [`rejectUnauthorized`](../2-options.md#rejectunauthorized)
- `gzip` → [`decompress`](../2-options.md#decompress)
- `jar` → [`cookieJar`](../2-options.md#cookiejar) (accepts [`tough-cookie`](https://github.com/salesforce/tough-cookie) jar)
- `jsonReviver` → [`parseJson`](../2-options.md#parsejson)
- `jsonReplacer` → [`stringifyJson`](../2-options.md#stringifyjson)

#### Changes in behavior

- The [`agent` option](../2-options.md#agent) is now an object with `http`, `https` and `http2` properties.
- The [`timeout` option](../6-timeout.md) is now an object. You can set timeouts on particular events!
- The [`searchParams` option](../2-options.md#searchparams) is always serialized using [`URLSearchParams`](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams).
- In order to pass a custom query string, provide it with the `url` option.\
  `got('https://example.com', {searchParams: {test: ''}})` → `https://example.com/?test=`\
  `got('https://example.com/?test')` → `https://example.com/?test`
- To use streams, call `got.stream(url, options)`.

#### Breaking changes

- The `json` option is not a `boolean`, it's an `object`. It will be stringified and used as a body.
- The `form` option is an `object` and will be used as `application/x-www-form-urlencoded` body.
- All headers are converted to lowercase.\
  According to [the spec](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2), the headers are case-insensitive.
- No `oauth` / `hawk` / `aws` / `httpSignature` option.\
  To sign requests, you need to create a [custom instance](../examples/advanced-creation.js).
- No `agentClass` / `agentOptions` / `pool` option.
- No `forever` option.\
  You need to pass an agent with `keepAlive` option set to `true`.
- No `proxy` option. You need to [pass a custom agent](../../../core/security/QUARANTINE/vetted/repos/hermes_agent/website/docs/guides/tips.md#proxying).
- No `auth` option.\
  You need to use [`username`](../2-options.md#username) / [`password`](../2-options.md#password) instead or set the `authorization` header manually.
- No `baseUrl` option.\
  Instead, there is [`prefixUrl`](../2-options.md#prefixurl) which appends a trailing slash if not present.
- No `removeRefererHeader` option.\
  You can remove the `referer` header in a [`beforeRequest` hook](../9-hooks.md#beforerequest).
- No `followAllRedirects` option.
- [`copyPipedHeaders`](../2-options.md#copypipedheaders) defaults to `false`.\
  Piped request headers are no longer copied automatically. Opt in with `copyPipedHeaders: true` for proxy scenarios.
- With `copyPipedHeaders: true`, explicitly set headers win over piped headers.\
  Piped headers only fill headers that were not explicitly set.

Hooks are very powerful. [Read more](../9-hooks.md) to see what else you achieve using hooks.

#### More about streams

Let's take a quick look at another example from Request's readme:

```js
http.createServer((serverRequest, serverResponse) => {
	if (serverRequest.url === '/doodle.png') {
		serverRequest.pipe(request('https://example.com/doodle.png')).pipe(serverResponse);
	}
});
```

Request can proxy headers with the stream. Got can do that too, but it is opt-in:

```js
import {pipeline as streamPipeline} from 'node:stream/promises';
import got from 'got';

const server = http.createServer(async (serverRequest, serverResponse) => {
	if (serverRequest.url === '/doodle.png') {
		await streamPipeline(
			serverRequest,
			got.stream('https://example.com/doodle.png', {copyPipedHeaders: true}),
			serverResponse
		);
	}
});

server.listen(8080);
```

In terms of stream usage, nothing has really changed, but header proxying is opt-in via `copyPipedHeaders: true`.

#### Convenience methods

- If you were using `request.get`, `request.post`, and so on - you can do the same with Got.
- The `request.defaults({…})` method has been renamed. You can do the same with `got.extend({…})`.
- There is no `request.cookie()` nor `request.jar()`. You have to use `tough-cookie` directly.

#### You're good to go!

Well, you have already come this far :tada:\
Take a look at the [documentation](../../../README.md#documentation). It's worth the time to read it.\
There are [some great tips](../../../core/security/QUARANTINE/vetted/repos/hermes_agent/website/docs/guides/tips.md).

If something is unclear or doesn't work as it should, don't hesitate to [open an issue](https://github.com/sindresorhus/got/issues/new/choose).
```

## File: `source/create.ts`
```typescript
import {setTimeout as delay} from 'node:timers/promises';
import is, {assert} from '@sindresorhus/is';
import asPromise from './as-promise/index.js';
import type {
	GotReturn,
	ExtendOptions,
	Got,
	HTTPAlias,
	InstanceDefaults,
	GotPaginate,
	GotStream,
	GotRequestFunction,
	OptionsWithPagination,
	StreamOptions,
} from './types.js';
import Request from './core/index.js';
import type {Response} from './core/response.js';
import Options, {type OptionsInit} from './core/options.js';
import type {RequestPromise} from './as-promise/types.js';

const isGotInstance = (value: Got | ExtendOptions): value is Got => is.function(value);

const aliases: readonly HTTPAlias[] = [
	'get',
	'post',
	'put',
	'patch',
	'head',
	'delete',
];

const optionsObjectUrlErrorMessage = 'The `url` option is not supported in options objects. Pass it as the first argument instead.';

const assertNoUrlInOptionsObject = (options: Record<string, unknown>): void => {
	if (Object.hasOwn(options, 'url')) {
		throw new TypeError(optionsObjectUrlErrorMessage);
	}
};

const create = (defaults: InstanceDefaults): Got => {
	defaults = {
		options: new Options(undefined, undefined, defaults.options),
		handlers: [...defaults.handlers],
		mutableDefaults: defaults.mutableDefaults,
	};

	Object.defineProperty(defaults, 'mutableDefaults', {
		enumerable: true,
		configurable: false,
		writable: false,
	});

	const makeRequest = (url: string | URL | OptionsInit | undefined, options: OptionsInit | undefined, defaultOptions: Options, isStream: boolean): GotReturn => {
		let requestInput = url;
		let requestOptions = options;

		if (is.plainObject(url)) {
			assertNoUrlInOptionsObject(url);
		}

		if (is.plainObject(options)) {
			assertNoUrlInOptionsObject(options);
		}

		if (isStream) {
			const createStreamOptions = (value: OptionsInit): OptionsInit => {
				const clone = Object.create(Object.getPrototypeOf(value), Object.getOwnPropertyDescriptors(value)) as OptionsInit;
				Object.defineProperty(clone, 'isStream', {
					value: true,
					enumerable: true,
					configurable: true,
					writable: true,
				});

				return clone;
			};

			if (is.plainObject(url)) {
				requestInput = createStreamOptions(url);

				if (options) {
					requestOptions = createStreamOptions(options);
				}
			} else {
				requestOptions = createStreamOptions(options ?? {});
			}
		}

		const request = new Request(requestInput, requestOptions, defaultOptions);

		if (
			isStream
			&& request.options
		) {
			request.options.isStream = true;
		}

		let promise: RequestPromise | undefined;

		const lastHandler = (normalized: Options): GotReturn => {
			// Note: `options` is `undefined` when `new Options(...)` fails
			request.options = normalized;
			const shouldReturnStream = normalized?.isStream ?? isStream;
			request._noPipe = !shouldReturnStream;
			void request.flush();

			if (shouldReturnStream) {
				return request;
			}

			promise ??= asPromise(request);

			return promise;
		};

		let iteration = 0;
		const iterateHandlers = (newOptions: Options): GotReturn => {
			const handler = defaults.handlers[iteration++] ?? lastHandler;

			const result = handler(newOptions, iterateHandlers) as GotReturn;

			if (is.promise(result) && !request.options?.isStream) {
				promise ??= asPromise(request);

				if (result !== promise) {
					const descriptors = Object.getOwnPropertyDescriptors(promise);

					for (const key in descriptors) {
						if (key in result) {
							// eslint-disable-next-line @typescript-eslint/no-dynamic-delete
							delete descriptors[key];
						}
					}

					// eslint-disable-next-line @typescript-eslint/no-floating-promises
					Object.defineProperties(result, descriptors);
				}
			}

			return result;
		};

		return iterateHandlers(request.options);
	};

	// Got interface
	const got: Got = ((url: string | URL | OptionsInit | undefined, options?: OptionsInit, defaultOptions: Options = defaults.options): GotReturn =>
		makeRequest(url, options, defaultOptions, false)) as Got;

	got.extend = (...instancesOrOptions) => {
		const options = new Options(undefined, undefined, defaults.options);
		const handlers = [...defaults.handlers];

		let mutableDefaults: boolean | undefined;

		for (const value of instancesOrOptions) {
			if (isGotInstance(value)) {
				options.merge(value.defaults.options);
				handlers.push(...value.defaults.handlers);
				mutableDefaults = value.defaults.mutableDefaults;
			} else {
				assertNoUrlInOptionsObject(value);
				options.merge(value);

				if (value.handlers) {
					handlers.push(...value.handlers);
				}

				mutableDefaults = value.mutableDefaults;
			}
		}

		return create({
			options,
			handlers,
			mutableDefaults: Boolean(mutableDefaults),
		});
	};

	// Pagination
	const paginateEach = (async function * <T, R>(url: string | URL, options?: OptionsWithPagination<T, R>): AsyncIterableIterator<T> {
		if (is.plainObject(url)) {
			assertNoUrlInOptionsObject(url);
		}

		if (is.plainObject(options)) {
			assertNoUrlInOptionsObject(options);
		}

		let normalizedOptions = new Options(url, options as OptionsInit, defaults.options);
		normalizedOptions.resolveBodyOnly = false;

		const {pagination} = normalizedOptions;

		assert.function(pagination.transform);
		assert.function(pagination.shouldContinue);
		assert.function(pagination.filter);
		assert.function(pagination.paginate);
		assert.number(pagination.countLimit);
		assert.number(pagination.requestLimit);
		assert.number(pagination.backoff);

		const allItems: T[] = [];
		let {countLimit} = pagination;

		let numberOfRequests = 0;
		while (numberOfRequests < pagination.requestLimit) {
			if (numberOfRequests !== 0) {
				// eslint-disable-next-line no-await-in-loop
				await delay(pagination.backoff);
			}

			// eslint-disable-next-line no-await-in-loop
			const response = (await got(undefined, undefined, normalizedOptions)) as Response;

			// eslint-disable-next-line no-await-in-loop
			const parsed: unknown[] = await pagination.transform(response);
			const currentItems: T[] = [];

			assert.array(parsed);

			for (const item of parsed) {
				if (pagination.filter({item, currentItems, allItems})) {
					if (!pagination.shouldContinue({item, currentItems, allItems})) {
						return;
					}

					yield item as T;

					if (pagination.stackAllItems) {
						allItems.push(item as T);
					}

					currentItems.push(item as T);

					if (--countLimit <= 0) {
						return;
					}
				}
			}

			const optionsToMerge = pagination.paginate({
				response,
				currentItems,
				allItems,
			});

			if (optionsToMerge === false) {
				return;
			}

			if (optionsToMerge === response.request.options) {
				normalizedOptions = response.request.options;
			} else {
				normalizedOptions.merge(optionsToMerge);

				try {
					assert.any([is.urlInstance, is.undefined], optionsToMerge.url);
				} catch (error) {
					if (error instanceof Error) {
						error.message = `Option 'pagination.paginate.url': ${error.message}`;
					}

					throw error;
				}

				if (optionsToMerge.url !== undefined) {
					normalizedOptions.prefixUrl = '';
					normalizedOptions.url = optionsToMerge.url;
				}
			}

			numberOfRequests++;
		}
	});

	got.paginate = paginateEach as GotPaginate;

	got.paginate.all = (async <T, R>(url: string | URL, options?: OptionsWithPagination<T, R>) => Array.fromAsync(paginateEach<T, R>(url, options))) as GotPaginate['all'];

	// For those who like very descriptive names
	got.paginate.each = paginateEach as GotPaginate['each'];

	// Stream API
	got.stream = ((url: string | URL, options?: StreamOptions) =>
		makeRequest(url, options, defaults.options, true)) as GotStream;

	// Shortcuts
	for (const method of aliases) {
		got[method] = ((url: string | URL, options?: Options): GotReturn => got(url, {...options, method})) as GotRequestFunction;

		got.stream[method] = ((url: string | URL, options?: StreamOptions) =>
			makeRequest(url, {...options, method}, defaults.options, true)) as GotStream;
	}

	if (!defaults.mutableDefaults) {
		Object.freeze(defaults.handlers);
		defaults.options.freeze();
	}

	Object.defineProperty(got, 'defaults', {
		value: defaults,
		writable: false,
		configurable: false,
		enumerable: true,
	});

	return got;
};

export default create;
```

## File: `source/index.ts`
```typescript
import create from './create.js';
import type {InstanceDefaults} from './types.js';
import Options from './core/options.js';

const defaults: InstanceDefaults = {
	options: new Options(),
	handlers: [],
	mutableDefaults: false,
};

const got = create(defaults);

export default got;

export {default as Options} from './core/options.js';
export * from './core/options.js';
export * from './core/response.js';
export type {default as Request} from './core/index.js';
export * from './core/index.js';
export * from './core/errors.js';
export * from './core/diagnostics-channel.js';
export type {Delays} from './core/timed-out.js';
export {default as calculateRetryDelay} from './core/calculate-retry-delay.js';
export type * from './as-promise/types.js';
export type * from './types.js';
export {default as create} from './create.js';
export {default as parseLinkHeader} from './core/parse-link-header.js';
```

## File: `source/types.ts`
```typescript
import type {Spread} from 'type-fest';
import type {RequestPromise} from './as-promise/types.js';
import type {Response} from './core/response.js';
import type Options from './core/options.js';
import {type PaginationOptions, type OptionsInit} from './core/options.js';
import type Request from './core/index.js';

// `type-fest` utilities
type Except<ObjectType, KeysType extends keyof ObjectType> = Pick<ObjectType, Exclude<keyof ObjectType, KeysType>>;
type Merge<FirstType, SecondType> = Except<FirstType, Extract<keyof FirstType, keyof SecondType>> & SecondType;

/**
Defaults for each Got instance.
*/
export type InstanceDefaults = {
	/**
	An object containing the default options of Got.
	*/
	options: Options;

	/**
	An array of functions. You execute them directly by calling `got()`.
	They are some sort of "global hooks" - these functions are called first.
	The last handler (*it's hidden*) is either `asPromise` or `asStream`, depending on whether `got()` or `got.stream()` was called.

	@default []
	*/
	handlers: HandlerFunction[];

	/**
	A read-only boolean describing whether the defaults are mutable or not.
	If set to `true`, you can update headers over time, for example, update an access token when it expires.

	@default false
	*/
	mutableDefaults: boolean;
};

/**
A Request object returned by calling Got, or any of the Got HTTP alias request functions.
*/
export type GotReturn = Request | RequestPromise;

/**
A function to handle options and returns a Request object.
It acts sort of like a "global hook", and will be called before any actual request is made.
*/
export type HandlerFunction = <T extends GotReturn>(options: Options, next: (options: Options) => T) => T | Promise<T>;

/**
The options available for `got.extend()`.
*/
export type ExtendOptions = {
	/**
	An array of functions. You execute them directly by calling `got()`.
	They are some sort of "global hooks" - these functions are called first.
	The last handler (*it's hidden*) is either `asPromise` or `asStream`, depending on whether `got()` or `got.stream()` was called.

	@default []
	*/
	handlers?: HandlerFunction[];

	/**
	A read-only boolean describing whether the defaults are mutable or not.
	If set to `true`, you can update headers over time, for example, update an access token when it expires.

	@default false
	*/
	mutableDefaults?: boolean;
} & Except<OptionsInit, 'url'>;

type OptionsInitWithoutUrl = Except<OptionsInit, 'url'>;

export type StrictOptions = Except<OptionsInitWithoutUrl, 'responseType' | 'resolveBodyOnly'>;
export type StreamOptions = OptionsInitWithoutUrl;

export type OptionsWithPagination<T = unknown, R = unknown> = Merge<OptionsInitWithoutUrl, {pagination?: PaginationOptions<T, R>}>;

/**
An instance of `got.paginate`.
*/
export type GotPaginate = {
	/**
	Same as `GotPaginate.each`.
	*/
	<T, R = unknown>(url: string | URL, options?: OptionsWithPagination<T, R>): AsyncIterableIterator<T>;

	/**
	Same as `GotPaginate.each`.
	*/
	<T, R = unknown>(options?: OptionsWithPagination<T, R>): AsyncIterableIterator<T>;

	/**
	Returns an async iterator.

	See pagination.options for more pagination options.

	@example
	```
	import got from 'got';

	const countLimit = 10;

	const pagination = got.paginate('https://api.github.com/repos/sindresorhus/got/commits', {
		pagination: {countLimit}
	});

	console.log(`Printing latest ${countLimit} Got commits (newest to oldest):`);

	for await (const commitData of pagination) {
		console.log(commitData.commit.message);
	}
	```
	*/
	each: (<T, R = unknown>(url: string | URL, options?: OptionsWithPagination<T, R>) => AsyncIterableIterator<T>)
		& (<T, R = unknown>(options?: OptionsWithPagination<T, R>) => AsyncIterableIterator<T>);

	/**
	Returns a Promise for an array of all results.

	See pagination.options for more pagination options.

	@example
	```
	import got from 'got';

	const countLimit = 10;

	const results = await got.paginate.all('https://api.github.com/repos/sindresorhus/got/commits', {
		pagination: {countLimit}
	});

	console.log(`Printing latest ${countLimit} Got commits (newest to oldest):`);
	console.log(results);
	```
	*/
	all: (<T, R = unknown>(url: string | URL, options?: OptionsWithPagination<T, R>) => Promise<T[]>)
		& (<T, R = unknown>(options?: OptionsWithPagination<T, R>) => Promise<T[]>);
};

export type OptionsOfTextResponseBody = Merge<StrictOptions, {responseType?: 'text'}>;
export type OptionsOfTextResponseBodyOnly = Merge<StrictOptions, {resolveBodyOnly: true; responseType?: 'text'}>;
export type OptionsOfTextResponseBodyWrapped = Merge<StrictOptions, {resolveBodyOnly: false; responseType?: 'text'}>;

export type OptionsOfJSONResponseBody = Merge<StrictOptions, {responseType?: 'json'}>; // eslint-disable-line @typescript-eslint/naming-convention
export type OptionsOfJSONResponseBodyOnly = Merge<StrictOptions, {resolveBodyOnly: true; responseType?: 'json'}>; // eslint-disable-line @typescript-eslint/naming-convention
export type OptionsOfJSONResponseBodyWrapped = Merge<StrictOptions, {resolveBodyOnly: false; responseType?: 'json'}>; // eslint-disable-line @typescript-eslint/naming-convention

export type OptionsOfBufferResponseBody = Merge<StrictOptions, {responseType?: 'buffer'}>;
export type OptionsOfBufferResponseBodyOnly = Merge<StrictOptions, {resolveBodyOnly: true; responseType?: 'buffer'}>;
export type OptionsOfBufferResponseBodyWrapped = Merge<StrictOptions, {resolveBodyOnly: false; responseType?: 'buffer'}>;

export type OptionsOfUnknownResponseBody = StrictOptions;
export type OptionsOfUnknownResponseBodyOnly = Merge<StrictOptions, {resolveBodyOnly: true}>;
export type OptionsOfUnknownResponseBodyWrapped = Merge<StrictOptions, {resolveBodyOnly: false}>;

// Helper type to determine the default response body type based on extended options
type DefaultResponseBodyType<U extends ExtendOptions> =
	U['responseType'] extends 'json' ? unknown :
		U['responseType'] extends 'buffer' ? Uint8Array :
			string;

type GotResponseResult<U extends ExtendOptions, BodyType> = U['resolveBodyOnly'] extends true
	? RequestPromise<BodyType>
	: RequestPromise<Response<BodyType>>;

export type GotRequestFunction<U extends ExtendOptions = Record<string, unknown>> = {
	// `asPromise` usage
	// IMPORTANT: This overload must come first to match when no explicit responseType is provided
	(url: string | URL, options?: OptionsOfUnknownResponseBody): GotResponseResult<U, DefaultResponseBodyType<U>>;
	(url: string | URL, options?: OptionsOfUnknownResponseBodyWrapped): RequestPromise<Response<DefaultResponseBodyType<U>>>;
	(url: string | URL, options?: OptionsOfUnknownResponseBodyOnly): RequestPromise<DefaultResponseBodyType<U>>;

	(url: string | URL, options?: OptionsOfTextResponseBody): GotResponseResult<U, string>;
	<T>(url: string | URL, options?: OptionsOfJSONResponseBody): GotResponseResult<U, T>;
	(url: string | URL, options?: OptionsOfBufferResponseBody): GotResponseResult<U, Uint8Array>;

	(url: string | URL, options?: OptionsOfTextResponseBodyWrapped): RequestPromise<Response<string>>;
	<T>(url: string | URL, options?: OptionsOfJSONResponseBodyWrapped): RequestPromise<Response<T>>;
	(url: string | URL, options?: OptionsOfBufferResponseBodyWrapped): RequestPromise<Response<Uint8Array>>;

	(url: string | URL, options?: OptionsOfTextResponseBodyOnly): RequestPromise<string>;
	<T>(url: string | URL, options?: OptionsOfJSONResponseBodyOnly): RequestPromise<T>;
	(url: string | URL, options?: OptionsOfBufferResponseBodyOnly): RequestPromise<Uint8Array>;

	(options: OptionsOfUnknownResponseBody): GotResponseResult<U, DefaultResponseBodyType<U>>;
	(options: OptionsOfUnknownResponseBodyWrapped): RequestPromise<Response<DefaultResponseBodyType<U>>>;
	(options: OptionsOfUnknownResponseBodyOnly): RequestPromise<DefaultResponseBodyType<U>>;

	(options: OptionsOfTextResponseBody): GotResponseResult<U, string>;
	<T>(options: OptionsOfJSONResponseBody): GotResponseResult<U, T>;
	(options: OptionsOfBufferResponseBody): GotResponseResult<U, Uint8Array>;

	(options: OptionsOfTextResponseBodyWrapped): RequestPromise<Response<string>>;
	<T>(options: OptionsOfJSONResponseBodyWrapped): RequestPromise<Response<T>>;
	(options: OptionsOfBufferResponseBodyWrapped): RequestPromise<Response<Uint8Array>>;

	(options: OptionsOfTextResponseBodyOnly): RequestPromise<string>;
	<T>(options: OptionsOfJSONResponseBodyOnly): RequestPromise<T>;
	(options: OptionsOfBufferResponseBodyOnly): RequestPromise<Uint8Array>;

	// Fallback
	(url: string | URL, options?: OptionsInitWithoutUrl): RequestPromise | Request;

	(options: OptionsInitWithoutUrl): RequestPromise | Request;

	// Internal usage
	(url: undefined, options: undefined, defaults: Options): RequestPromise | Request;
};

/**
All available HTTP request methods provided by Got.
*/
// eslint-disable-next-line @typescript-eslint/naming-convention
export type HTTPAlias =
	| 'get'
	| 'post'
	| 'put'
	| 'patch'
	| 'head'
	| 'delete';

type GotStreamFunction =
	((url?: string | URL, options?: StreamOptions) => Request) &
	((options?: StreamOptions) => Request);

/**
An instance of `got.stream()`.
*/
export type GotStream = GotStreamFunction & Record<HTTPAlias, GotStreamFunction>;

/**
An instance of `got`.
*/
export type Got<GotOptions extends ExtendOptions = ExtendOptions> = {
	/**
	Returns a [duplex stream](https://nodejs.org/api/stream.html#stream_class_stream_duplex) with additional events:
	- request
	- response
	- redirect
	- uploadProgress
	- downloadProgress
	- error

	Note: For writable request streams, call `stream.end()` when you are not piping a body. `got.stream` does not auto-end for OPTIONS, DELETE, or PATCH so you can pipe or write a body without getting `write after end`.
	*/
	stream: GotStream;

	/**
	Returns an async iterator.

	See pagination.options for more pagination options.

	@example
	```
	import got from 'got';

	const countLimit = 10;

	const pagination = got.paginate('https://api.github.com/repos/sindresorhus/got/commits', {
		pagination: {countLimit}
	});

	console.log(`Printing latest ${countLimit} Got commits (newest to oldest):`);

	for await (const commitData of pagination) {
		console.log(commitData.commit.message);
	}
	```
	*/
	paginate: GotPaginate;

	/**
	The Got defaults used in that instance.
	*/
	defaults: InstanceDefaults;

	/**
	Configure a new `got` instance with default `options`.
	The `options` are merged with the parent instance's `defaults.options` using `got.mergeOptions`.
	You can access the resolved options with the `.defaults` property on the instance.

	Additionally, `got.extend()` accepts two properties from the `defaults` object: `mutableDefaults` and `handlers`.

	It is also possible to merges many instances into a single one:
	- options are merged using `got.mergeOptions()` (including hooks),
	- handlers are stored in an array (you can access them through `instance.defaults.handlers`).

	@example
	```
	import got from 'got';

	const client = got.extend({
		prefixUrl: 'https://example.com',
		headers: {
			'x-unicorn': 'rainbow'
		}
	});

	client.get('demo');

	// HTTP Request =>
	// GET /demo HTTP/1.1
	// Host: example.com
	// x-unicorn: rainbow
	```
	*/
	extend<T extends Array<Got | ExtendOptions>>(...instancesOrOptions: T): Got<MergeExtendsConfig<T>>;
}
& Record<HTTPAlias, GotRequestFunction<GotOptions>>
& GotRequestFunction<GotOptions>;

export type ExtractExtendOptions<T> = T extends Got<infer GotOptions>
	? GotOptions
	: T;

/**
Merges the options of multiple Got instances.
*/
export type MergeExtendsConfig<Value extends Array<Got | ExtendOptions>> =
Value extends readonly [Value[0], ...infer NextValue]
	? NextValue[0] extends undefined
		? Value[0] extends infer OnlyValue
			? OnlyValue extends ExtendOptions
				? OnlyValue
				: OnlyValue extends Got<infer GotOptions>
					? GotOptions
					: OnlyValue
			: never
		: ExtractExtendOptions<Value[0]> extends infer FirstArg extends ExtendOptions
			? ExtractExtendOptions<NextValue[0] extends ExtendOptions | Got ? NextValue[0] : never> extends infer NextArg extends ExtendOptions
				? Spread<FirstArg, NextArg> extends infer Merged extends ExtendOptions
					? NextValue extends [NextValue[0], ...infer NextRest]
						? NextRest extends Array<Got | ExtendOptions>
							? MergeExtendsConfig<[Merged, ...NextRest]>
							: never
						: never
					: never
				: never
			: never
	: never;
```

## File: `source/as-promise/index.ts`
```typescript
import {Buffer} from 'node:buffer';
import {EventEmitter} from 'node:events';
import is from '@sindresorhus/is';
import {
	HTTPError,
	RetryError,
	type RequestError,
} from '../core/errors.js';
import Request from '../core/index.js';
import {
	parseBody,
	isResponseOk,
	type Response, ParseError,
} from '../core/response.js';
import proxyEvents from '../core/utils/proxy-events.js';
import type Options from '../core/options.js';
import {type RequestPromise} from './types.js';

const proxiedRequestEvents = [
	'request',
	'response',
	'redirect',
	'uploadProgress',
	'downloadProgress',
];

const normalizeError = (error: unknown): Error => {
	if (error instanceof Error) {
		return error;
	}

	if (is.object(error)) {
		const errorLike = error as Partial<Error & {code?: string; input?: string}>;
		const message = typeof errorLike.message === 'string' ? errorLike.message : 'Non-error object thrown';
		const normalizedError = new Error(message, {cause: error}) as Error & {code?: string; input?: string};

		if (typeof errorLike.stack === 'string') {
			normalizedError.stack = errorLike.stack;
		}

		if (typeof errorLike.code === 'string') {
			normalizedError.code = errorLike.code;
		}

		if (typeof errorLike.input === 'string') {
			normalizedError.input = errorLike.input;
		}

		return normalizedError;
	}

	return new Error(String(error));
};

export default function asPromise<T>(firstRequest?: Request): RequestPromise<T> {
	let globalRequest: Request;
	let globalResponse: Response;
	const emitter = new EventEmitter();
	let promiseSettled = false;

	const promise = new Promise<T>((resolve, reject) => {
		const makeRequest = (retryCount: number, defaultOptions?: Options): void => {
			const request = firstRequest ?? new Request(undefined, undefined, defaultOptions);
			request.retryCount = retryCount;
			request._noPipe = true;

			globalRequest = request;

			request.once('response', async (response: Response) => {
				// Parse body
				const contentEncoding = (response.headers['content-encoding'] ?? '').toLowerCase();
				const isCompressed = contentEncoding === 'gzip' || contentEncoding === 'deflate' || contentEncoding === 'br' || contentEncoding === 'zstd';

				const {options} = request;

				if (isCompressed && !options.decompress) {
					response.body = response.rawBody;
				} else {
					try {
						response.body = parseBody(response, options.responseType, options.parseJson, options.encoding);
					} catch (error: unknown) {
						// Fall back to `utf8`
						try {
							response.body = Buffer.from(response.rawBody).toString();
						} catch (error) {
							request._beforeError(new ParseError(normalizeError(error), response));
							return;
						}

						if (isResponseOk(response)) {
							request._beforeError(normalizeError(error));
							return;
						}
					}
				}

				try {
					const hooks = options.hooks.afterResponse;

					for (const [index, hook] of hooks.entries()) {
						// @ts-expect-error TS doesn't notice that RequestPromise is a Promise
						// eslint-disable-next-line no-await-in-loop
						response = await hook(response, async (updatedOptions): RequestPromise<Response> => {
							const preserveHooks = updatedOptions.preserveHooks ?? false;

							options.merge(updatedOptions);
							options.prefixUrl = '';

							if (updatedOptions.url) {
								options.url = updatedOptions.url;
							}

							// Remove any further hooks for that request, because we'll call them anyway.
							// The loop continues. We don't want duplicates (asPromise recursion).
							// Unless preserveHooks is true, in which case we keep the remaining hooks.
							if (!preserveHooks) {
								options.hooks.afterResponse = options.hooks.afterResponse.slice(0, index);
							}

							throw new RetryError(request);
						});

						if (!(is.object(response) && is.number(response.statusCode) && 'body' in response)) {
							throw new TypeError('The `afterResponse` hook returned an invalid value');
						}
					}
				} catch (error: unknown) {
					request._beforeError(normalizeError(error));
					return;
				}

				globalResponse = response;

				if (!isResponseOk(response)) {
					request._beforeError(new HTTPError(response));
					return;
				}

				request.destroy();
				promiseSettled = true;
				resolve(request.options.resolveBodyOnly ? response.body as T : response as unknown as T);
			});

			let handledFinalError = false;

			const onError = (error: RequestError) => {
				// Route errors emitted directly on the stream (e.g., EPIPE from Node.js)
				// through retry logic first, then handle them here after retries are exhausted.
				// See https://github.com/sindresorhus/got/issues/1995
				if (!request._stopReading) {
					request._beforeError(error);
					return;
				}

				// Allow the manual re-emission from Request to land only once.
				if (handledFinalError) {
					return;
				}

				handledFinalError = true;

				promiseSettled = true;
				const {options} = request;

				if (error instanceof HTTPError && !options.throwHttpErrors) {
					const {response} = error;

					request.destroy();
					resolve(request.options.resolveBodyOnly ? response.body as T : response as unknown as T);
					return;
				}

				reject(error);
			};

			// Use .on() instead of .once() to keep the listener active across retries.
			// When _stopReading is false, we return early and the error gets re-emitted
			// after retry logic completes, so we need this listener to remain active.
			// See https://github.com/sindresorhus/got/issues/1995
			request.on('error', onError);

			const previousBody = request.options?.body;

			request.once('retry', (newRetryCount: number, error: RequestError) => {
				firstRequest = undefined;

				// If promise already settled, don't retry
				// This prevents the race condition in #1489 where a late error
				// (e.g., ECONNRESET after successful response) triggers retry
				// after the promise has already resolved/rejected
				if (promiseSettled) {
					return;
				}

				const newBody = request.options.body;

				if (previousBody === newBody && (is.nodeStream(newBody) || newBody instanceof ReadableStream)) {
					error.message = 'Cannot retry with consumed body stream';

					onError(error);
					return;
				}

				// This is needed! We need to reuse `request.options` because they can get modified!
				// For example, by calling `promise.json()`.
				makeRequest(newRetryCount, request.options);
			});

			proxyEvents(request, emitter, proxiedRequestEvents);

			if (is.undefined(firstRequest)) {
				void request.flush();
			}
		};

		makeRequest(0);
	}) as RequestPromise<T>;

	promise.on = function (this: RequestPromise<T>, event: string, function_: (...arguments_: any[]) => void) {
		emitter.on(event, function_);
		return this;
	};

	promise.once = function (this: RequestPromise<T>, event: string, function_: (...arguments_: any[]) => void) {
		emitter.once(event, function_);
		return this;
	};

	promise.off = function (this: RequestPromise<T>, event: string, function_: (...arguments_: any[]) => void) {
		emitter.off(event, function_);
		return this;
	};

	const shortcut = <T>(promiseToAwait: RequestPromise, responseType: Options['responseType']): RequestPromise<T> => {
		const newPromise = (async () => {
			// Wait until downloading has ended
			await promiseToAwait;

			const {options} = globalResponse.request;

			return parseBody(globalResponse, responseType, options.parseJson, options.encoding);
		})();

		// eslint-disable-next-line @typescript-eslint/no-floating-promises
		Object.defineProperties(newPromise, Object.getOwnPropertyDescriptors(promiseToAwait));

		return newPromise as RequestPromise<T>;
	};

	// Note: These use `function` syntax (not arrows) to access `this` context.
	// When custom handlers wrap the promise to transform errors, these methods
	// are copied to the handler's promise. Using `this` ensures we await the
	// handler's wrapped promise, not the original, so errors propagate correctly.
	promise.json = function (this: RequestPromise) {
		if (globalRequest.options) {
			const {headers} = globalRequest.options;

			if (!globalRequest.writableFinished && !('accept' in headers)) {
				headers.accept = 'application/json';
			}
		}

		return shortcut(this, 'json');
	};

	promise.buffer = function (this: RequestPromise) {
		return shortcut(this, 'buffer');
	};

	promise.text = function (this: RequestPromise) {
		return shortcut(this, 'text');
	};

	return promise;
}
```

## File: `source/as-promise/types.ts`
```typescript
import {type RequestEvents} from '../core/index.js';
import type {Response} from '../core/response.js';

// eslint-disable-next-line @typescript-eslint/consistent-type-definitions -- Internal recursive shape requires interface; public API remains a type alias.
interface RequestPromiseShape<T extends Response | Response['body'] = Response['body']> extends RequestEvents<RequestPromise<T>> {
	/**
	A shortcut method that gives a Promise returning a JSON object.

	It is semantically the same as setting `options.resolveBodyOnly` to `true` and `options.responseType` to `'json'`.
	*/
	json: <ReturnType>() => RequestPromise<ReturnType>;

	/**
	A shortcut method that gives a Promise returning a [Uint8Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array).

	It is semantically the same as setting `options.resolveBodyOnly` to `true` and `options.responseType` to `'buffer'`.
	*/
	buffer: () => RequestPromise<Uint8Array>;

	/**
	A shortcut method that gives a Promise returning a string.

	It is semantically the same as setting `options.resolveBodyOnly` to `true` and `options.responseType` to `'text'`.
	*/
	text: () => RequestPromise<string>;
}

// This is intentionally a type alias to keep structural typing predictable.
// Augmenting it via interface merging is not supported.
export type RequestPromise<T extends Response | Response['body'] = Response['body']> = Promise<T> & RequestPromiseShape<T>;
```

## File: `source/core/calculate-retry-delay.ts`
```typescript
import type {RetryFunction} from './options.js';

type Returns<T extends (...arguments_: any) => unknown, V> = (...arguments_: Parameters<T>) => V;

const calculateRetryDelay: Returns<RetryFunction, number> = ({
	attemptCount,
	retryOptions,
	error,
	retryAfter,
	computedValue,
}) => {
	if (error.name === 'RetryError') {
		return 1;
	}

	if (attemptCount > retryOptions.limit) {
		return 0;
	}

	const hasMethod = retryOptions.methods.includes(error.options.method);
	const hasErrorCode = retryOptions.errorCodes.includes(error.code);
	const hasStatusCode = error.response && retryOptions.statusCodes.includes(error.response.statusCode);
	if (!hasMethod || (!hasErrorCode && !hasStatusCode)) {
		return 0;
	}

	if (error.response) {
		if (retryAfter) {
			// In this case `computedValue` is `options.request.timeout`
			if (retryAfter > computedValue) {
				return 0;
			}

			return retryAfter;
		}

		if (error.response.statusCode === 413) {
			return 0;
		}
	}

	const noise = Math.random() * retryOptions.noise;
	return Math.min(((2 ** (attemptCount - 1)) * 1000), retryOptions.backoffLimit) + noise;
};

export default calculateRetryDelay;
```

## File: `source/core/diagnostics-channel.ts`
```typescript
import {randomUUID} from 'node:crypto';
import diagnosticsChannel from 'node:diagnostics_channel';
import type {Timings} from './utils/timer.js';
import type {RequestError} from './errors.js';

const channels = {
	requestCreate: diagnosticsChannel.channel('got:request:create'),
	requestStart: diagnosticsChannel.channel('got:request:start'),
	responseStart: diagnosticsChannel.channel('got:response:start'),
	responseEnd: diagnosticsChannel.channel('got:response:end'),
	retry: diagnosticsChannel.channel('got:request:retry'),
	error: diagnosticsChannel.channel('got:request:error'),
	redirect: diagnosticsChannel.channel('got:response:redirect'),
};

export type RequestId = string;

/**
Message for the `got:request:create` diagnostic channel.

Emitted when a request is created.
*/
export type DiagnosticRequestCreate = {
	requestId: RequestId;
	url: string;
	method: string;
};

/**
Message for the `got:request:start` diagnostic channel.

Emitted before the native HTTP request is sent.
*/
export type DiagnosticRequestStart = {
	requestId: RequestId;
	url: string;
	method: string;
	headers: Record<string, string | string[] | undefined>;
};

/**
Message for the `got:response:start` diagnostic channel.

Emitted when response headers are received.
*/
export type DiagnosticResponseStart = {
	requestId: RequestId;
	url: string;
	statusCode: number;
	headers: Record<string, string | string[] | undefined>;
	isFromCache: boolean;
};

/**
Message for the `got:response:end` diagnostic channel.

Emitted when the response completes.
*/
export type DiagnosticResponseEnd = {
	requestId: RequestId;
	url: string;
	statusCode: number;
	bodySize?: number;
	timings?: Timings;
};

/**
Message for the `got:request:retry` diagnostic channel.

Emitted when retrying a request.
*/
export type DiagnosticRequestRetry = {
	requestId: RequestId;
	retryCount: number;
	error: RequestError;
	delay: number;
};

/**
Message for the `got:request:error` diagnostic channel.

Emitted when a request fails.
*/
export type DiagnosticRequestError = {
	requestId: RequestId;
	url: string;
	error: RequestError;
	timings?: Timings;
};

/**
Message for the `got:response:redirect` diagnostic channel.

Emitted when following a redirect.
*/
export type DiagnosticResponseRedirect = {
	requestId: RequestId;
	fromUrl: string;
	toUrl: string;
	statusCode: number;
};

export function generateRequestId(): RequestId {
	return randomUUID();
}

export function publishRequestCreate(message: DiagnosticRequestCreate): void {
	if (channels.requestCreate.hasSubscribers) {
		channels.requestCreate.publish(message);
	}
}

export function publishRequestStart(message: DiagnosticRequestStart): void {
	if (channels.requestStart.hasSubscribers) {
		channels.requestStart.publish(message);
	}
}

export function publishResponseStart(message: DiagnosticResponseStart): void {
	if (channels.responseStart.hasSubscribers) {
		channels.responseStart.publish(message);
	}
}

export function publishResponseEnd(message: DiagnosticResponseEnd): void {
	if (channels.responseEnd.hasSubscribers) {
		channels.responseEnd.publish(message);
	}
}

export function publishRetry(message: DiagnosticRequestRetry): void {
	if (channels.retry.hasSubscribers) {
		channels.retry.publish(message);
	}
}

export function publishError(message: DiagnosticRequestError): void {
	if (channels.error.hasSubscribers) {
		channels.error.publish(message);
	}
}

export function publishRedirect(message: DiagnosticResponseRedirect): void {
	if (channels.redirect.hasSubscribers) {
		channels.redirect.publish(message);
	}
}
```

## File: `source/core/errors.ts`
```typescript
import is from '@sindresorhus/is';
import stripUrlAuth from './utils/strip-url-auth.js';
import type {Timings} from './utils/timer.js';
import type Options from './options.js';
import type {TimeoutError as TimedOutTimeoutError} from './timed-out.js';
import type {PlainResponse, Response} from './response.js';
import type Request from './index.js';

type Error = NodeJS.ErrnoException;

// A hacky check to prevent circular references.
function isRequest(x: unknown): x is Request {
	return is.object(x) && '_onResponse' in x;
}

/**
An error to be thrown when a request fails.
Contains a `code` property with error class code, like `ECONNREFUSED`.
*/
export class RequestError<T = unknown> extends Error {
	override name = 'RequestError';
	code = 'ERR_GOT_REQUEST_ERROR';
	input?: string;
	override stack!: string;
	declare readonly options: Options;
	readonly response?: Response<T>;
	readonly request?: Request;
	readonly timings?: Timings;

	constructor(message: string, error: Partial<Error & {code?: string}>, self: Request | Options) {
		super(message, {cause: error});
		Error.captureStackTrace(this, this.constructor);

		if (error.code) {
			this.code = error.code;
		}

		this.input = (error as any).input;

		if (isRequest(self)) {
			Object.defineProperty(this, 'request', {
				enumerable: false,
				value: self,
			});

			Object.defineProperty(this, 'response', {
				enumerable: false,
				value: self.response,
			});

			this.options = self.options;
		} else {
			this.options = self;
		}

		this.timings = this.request?.timings;

		// Recover the original stacktrace
		if (is.string(error.stack) && is.string(this.stack)) {
			const indexOfMessage = this.stack.indexOf(this.message) + this.message.length;
			const thisStackTrace = this.stack.slice(indexOfMessage).split('\n').reverse();
			const errorStackTrace = error.stack.slice(error.stack.indexOf(error.message!) + error.message!.length).split('\n').reverse();

			// Remove duplicated traces
			while (errorStackTrace.length > 0 && errorStackTrace[0] === thisStackTrace[0]) {
				thisStackTrace.shift();
			}

			this.stack = `${this.stack.slice(0, indexOfMessage)}${thisStackTrace.reverse().join('\n')}${errorStackTrace.reverse().join('\n')}`;
		}
	}
}

/**
An error to be thrown when the server redirects you more than ten times.
Includes a `response` property.
*/
export class MaxRedirectsError extends RequestError {
	override name = 'MaxRedirectsError';
	override code = 'ERR_TOO_MANY_REDIRECTS';
	declare readonly response: Response;
	declare readonly request: Request;
	declare readonly timings: Timings;

	constructor(request: Request) {
		super(`Redirected ${request.options.maxRedirects} times. Aborting.`, {}, request);
	}
}

/**
An error to be thrown when the server response code is not 2xx nor 3xx if `options.followRedirect` is `true`, but always except for 304.
Includes a `response` property.
*/
// eslint-disable-next-line @typescript-eslint/naming-convention
export class HTTPError<T = unknown> extends RequestError<T> {
	override name = 'HTTPError';
	override code = 'ERR_NON_2XX_3XX_RESPONSE';
	declare readonly response: Response<T>;
	declare readonly request: Request;
	declare readonly timings: Timings;

	constructor(response: PlainResponse) {
		super(`Request failed with status code ${response.statusCode} (${response.statusMessage!}): ${response.request.options.method} ${stripUrlAuth(response.request.options.url!)}`, {}, response.request);
	}
}

/**
An error to be thrown when a cache method fails.
For example, if the database goes down or there's a filesystem error.
*/
export class CacheError extends RequestError {
	override name = 'CacheError';
	declare readonly request: Request;

	constructor(error: Error, request: Request) {
		super(error.message, error, request);
		if (this.code === 'ERR_GOT_REQUEST_ERROR') {
			this.code = 'ERR_CACHE_ACCESS';
		}
	}
}

/**
An error to be thrown when the request body is a stream and an error occurs while reading from that stream.
*/
export class UploadError extends RequestError {
	override name = 'UploadError';
	declare readonly request: Request;

	constructor(error: Error, request: Request) {
		super(error.message, error, request);
		if (this.code === 'ERR_GOT_REQUEST_ERROR') {
			this.code = 'ERR_UPLOAD';
		}
	}
}

/**
An error to be thrown when the request is aborted due to a timeout.
Includes an `event` and `timings` property.
*/
export class TimeoutError extends RequestError {
	override name = 'TimeoutError';
	declare readonly request: Request;
	override readonly timings: Timings;
	readonly event: string;

	constructor(error: TimedOutTimeoutError, timings: Timings, request: Request) {
		super(error.message, error, request);
		this.event = error.event;
		this.timings = timings;
	}
}

/**
An error to be thrown when reading from response stream fails.
*/
export class ReadError extends RequestError {
	override name = 'ReadError';
	declare readonly request: Request;
	declare readonly response: Response;
	declare readonly timings: Timings;

	constructor(error: Error, request: Request) {
		super(error.message, error, request);
		if (this.code === 'ERR_GOT_REQUEST_ERROR') {
			this.code = 'ERR_READING_RESPONSE_STREAM';
		}
	}
}

/**
An error which always triggers a new retry when thrown.
*/
export class RetryError extends RequestError {
	override name = 'RetryError';
	override code = 'ERR_RETRYING';

	constructor(request: Request) {
		super('Retrying', {}, request);
	}
}

/**
An error to be thrown when the request is aborted by AbortController.
*/
export class AbortError extends RequestError {
	override name = 'AbortError';
	override code = 'ERR_ABORTED';

	constructor(request: Request) {
		super('This operation was aborted.', {}, request);
	}
}
```

## File: `source/core/index.ts`
```typescript
import process from 'node:process';
import {Buffer} from 'node:buffer';
import {Duplex, type Readable} from 'node:stream';
import {addAbortListener} from 'node:events';
import http, {ServerResponse, type ClientRequest, type RequestOptions} from 'node:http';
import type {Socket} from 'node:net';
import {byteLength} from 'byte-counter';
import {chunk} from 'chunk-data';
import CacheableRequest, {
	CacheError as CacheableCacheError,
	type CacheableRequestFunction,
	type CacheableOptions,
} from 'cacheable-request';
import decompressResponse from 'decompress-response';
import type {KeyvStoreAdapter} from 'keyv';
import type KeyvType from 'keyv';
import is, {isBuffer} from '@sindresorhus/is';
import type ResponseLike from 'responselike';
import timer, {type ClientRequestWithTimings, type Timings, type IncomingMessageWithTimings} from './utils/timer.js';
import getBodySize from './utils/get-body-size.js';
import proxyEvents from './utils/proxy-events.js';
import timedOut, {TimeoutError as TimedOutTimeoutError} from './timed-out.js';
import stripUrlAuth from './utils/strip-url-auth.js';
import WeakableMap from './utils/weakable-map.js';
import calculateRetryDelay from './calculate-retry-delay.js';
import Options, {
	type PromiseCookieJar,
	type NativeRequestOptions,
	type RetryOptions,
	type OptionsError,
	type OptionsInit,
	type NormalizedOptions,
} from './options.js';
import {
	cacheDecodedBody,
	isResponseOk,
	type PlainResponse,
	type Response,
} from './response.js';
import isClientRequest from './utils/is-client-request.js';
import isUnixSocketURL, {getUnixSocketPath} from './utils/is-unix-socket-url.js';
import {
	RequestError,
	ReadError,
	MaxRedirectsError,
	HTTPError,
	TimeoutError,
	UploadError,
	CacheError,
	AbortError,
} from './errors.js';
import {
	generateRequestId,
	publishRequestCreate,
	publishRequestStart,
	publishResponseStart,
	publishResponseEnd,
	publishRetry,
	publishError,
	publishRedirect,
} from './diagnostics-channel.js';

type Error = NodeJS.ErrnoException;

export type Progress = {
	percent: number;
	transferred: number;
	total?: number;
};

const supportsBrotli = is.string(process.versions.brotli);
const supportsZstd = is.string(process.versions.zstd);
const isUtf8Encoding = (encoding?: BufferEncoding): boolean => encoding === undefined || encoding.toLowerCase().replace('-', '') === 'utf8';
const textEncoder = new TextEncoder();
const concatUint8Arrays = (chunks: readonly Uint8Array[]): Uint8Array => {
	let totalLength = 0;
	for (const chunk of chunks) {
		totalLength += chunk.byteLength;
	}

	const result = new Uint8Array(totalLength);
	let offset = 0;

	for (const chunk of chunks) {
		result.set(chunk, offset);
		offset += chunk.byteLength;
	}

	return result;
};

const methodsWithoutBody: ReadonlySet<string> = new Set(['GET', 'HEAD']);

export type GotEventFunction<T> =
	/**
	`request` event to get the request object of the request.

	 __Tip__: You can use `request` event to abort requests.

	@example
	```
	import got from 'got';

	got.stream('https://github.com')
		.on('request', request => setTimeout(() => request.destroy(), 50));
	```
	*/
	((name: 'request', listener: (request: ClientRequest) => void) => T)

	/**
	The `response` event to get the response object of the final request.
	*/
	& (<R extends Response>(name: 'response', listener: (response: R) => void) => T)

	/**
	The `redirect` event to get the response object of a redirect. The second argument is options for the next request to the redirect location.
	*/
	& (<R extends Response, N extends Options>(name: 'redirect', listener: (response: R, nextOptions: N) => void) => T)

	/**
	Progress events for uploading (sending a request) and downloading (receiving a response).
	The `progress` argument is an object like:

	```
	{
		percent: 0.1,
		transferred: 1024,
		total: 10240
	}
	```

	If the `content-length` header is missing, `total` will be `undefined`.

	@example
	```
	import got from 'got';

	const response = await got('https://sindresorhus.com')
		.on('downloadProgress', progress => {
			// Report download progress
		})
		.on('uploadProgress', progress => {
			// Report upload progress
		});

	console.log(response);
	```
	*/
	& ((name: 'uploadProgress' | 'downloadProgress', listener: (progress: Progress) => void) => T)
	/**
	To enable retrying on a Got stream, it is required to have a `retry` handler attached.

	When this event is emitted, you should reset the stream you were writing to and prepare the body again.

	See `got.options.retry` for more information.
	*/
	& ((name: 'retry', listener: (retryCount: number, error: RequestError, createRetryStream: (options?: OptionsInit) => Request) => void) => T);

export type RequestEvents<T> = {
	on: GotEventFunction<T>;
	once: GotEventFunction<T>;
	off: GotEventFunction<T>;
};

type StorageAdapter = KeyvStoreAdapter | KeyvType | Map<unknown, unknown>;

const cacheableStore = new WeakableMap<string | StorageAdapter, CacheableRequestFunction>();

const redirectCodes: ReadonlySet<number> = new Set([300, 301, 302, 303, 304, 307, 308]);
const transientWriteErrorCodes: ReadonlySet<string> = new Set(['EPIPE', 'ECONNRESET']);

// Track errors that have been processed by beforeError hooks to preserve custom error types
const errorsProcessedByHooks = new WeakSet<Error>();

const proxiedRequestEvents = [
	'socket',
	'connect',
	'continue',
	'information',
	'upgrade',
] as const;

const noop = (): void => {};

const isTransientWriteError = (error: Error): boolean => {
	const {code} = error;
	return typeof code === 'string' && transientWriteErrorCodes.has(code);
};

const normalizeError = (error: unknown): Error => {
	if (error instanceof globalThis.Error) {
		return error;
	}

	if (is.object(error)) {
		const errorLike = error as Partial<Error & {code?: string; input?: string}>;
		const message = typeof errorLike.message === 'string' ? errorLike.message : 'Non-error object thrown';
		const normalizedError = new globalThis.Error(message, {cause: error}) as Error & {code?: string; input?: string};

		if (typeof errorLike.stack === 'string') {
			normalizedError.stack = errorLike.stack;
		}

		if (typeof errorLike.code === 'string') {
			normalizedError.code = errorLike.code;
		}

		if (typeof errorLike.input === 'string') {
			normalizedError.input = errorLike.input;
		}

		return normalizedError;
	}

	return new globalThis.Error(String(error));
};

type UrlType = ConstructorParameters<typeof Options>[0];
type OptionsType = ConstructorParameters<typeof Options>[1];
type DefaultsType = ConstructorParameters<typeof Options>[2];
const getSanitizedUrl = (options?: Options): string => options?.url ? stripUrlAuth(options.url) : '';

export default class Request extends Duplex implements RequestEvents<Request> {
	// @ts-expect-error - Ignoring for now.
	override ['constructor']: typeof Request;

	_noPipe?: boolean;

	// @ts-expect-error https://github.com/microsoft/TypeScript/issues/9568
	options: Options;
	response?: PlainResponse;
	requestUrl?: URL;
	redirectUrls: URL[] = [];
	retryCount = 0;
	_stopReading = false;

	declare private _requestOptions: NativeRequestOptions;

	private _stopRetry = noop;
	private _downloadedSize = 0;
	private _uploadedSize = 0;
	private readonly _pipedServerResponses = new Set<ServerResponse>();
	private _request?: ClientRequest;
	private _responseSize?: number;
	private _bodySize?: number;
	private _unproxyEvents = noop;
	private _isFromCache?: boolean;
	private _triggerRead = false;
	private readonly _jobs: Array<() => void> = [];
	private _cancelTimeouts = noop;
	private readonly _removeListeners = noop;
	private _nativeResponse?: IncomingMessageWithTimings;
	private _flushed = false;
	private _aborted = false;
	private _expectedContentLength?: number;
	private _compressedBytesCount?: number;
	private _skipRequestEndInFinal = false;
	private _incrementalBodyDecoder?: TextDecoder;
	private _incrementalDecodedBodyChunks: string[] = [];
	private readonly _requestId = generateRequestId();

	// We need this because `this._request` if `undefined` when using cache
	private _requestInitialized = false;

	constructor(url: UrlType, options?: OptionsType, defaults?: DefaultsType) {
		super({
			// Don't destroy immediately, as the error may be emitted on unsuccessful retry
			autoDestroy: false,
			// It needs to be zero because we're just proxying the data to another stream
			highWaterMark: 0,
		});

		this.on('pipe', (source: NodeJS.ReadableStream & {headers?: Record<string, string | string[] | undefined>}) => {
			if (this.options.copyPipedHeaders && source?.headers) {
				for (const [header, value] of Object.entries(source.headers)) {
					const normalizedHeader = header.toLowerCase();

					if (!this.options.shouldCopyPipedHeader(normalizedHeader)) {
						continue;
					}

					this.options.setPipedHeader(normalizedHeader, value);
				}
			}
		});

		this.on('newListener', event => {
			if (event === 'retry' && this.listenerCount('retry') > 0) {
				throw new Error('A retry listener has been attached already.');
			}
		});

		try {
			this.options = new Options(url, options, defaults);

			if (!this.options.url) {
				if (this.options.prefixUrl === '') {
					throw new TypeError('Missing `url` property');
				}

				this.options.url = '';
			}

			this.requestUrl = this.options.url as URL;

			// Publish request creation event
			publishRequestCreate({
				requestId: this._requestId,
				url: getSanitizedUrl(this.options),
				method: this.options.method,
			});
		} catch (error: unknown) {
			const {options} = error as OptionsError;
			if (options) {
				this.options = options;
			}

			this.flush = async () => {
				this.flush = async () => {};

				// Defer error emission to next tick to allow user to attach error handlers
				process.nextTick(() => {
					// _beforeError requires options to access retry logic and hooks
					if (this.options) {
						this._beforeError(normalizeError(error));
					} else {
						// Options is undefined, skip _beforeError and destroy directly
						const normalizedError = normalizeError(error);
						const requestError = normalizedError instanceof RequestError ? normalizedError : new RequestError(normalizedError.message, normalizedError, this);
						this.destroy(requestError);
					}
				});
			};

			return;
		}

		// Important! If you replace `body` in a handler with another stream, make sure it's readable first.
		// The below is run only once.
		const {body} = this.options;
		if (is.nodeStream(body)) {
			body.once('error', error => {
				if (this._flushed) {
					this._beforeError(new UploadError(error, this));
				} else {
					this.flush = async () => {
						this.flush = async () => {};

						this._beforeError(new UploadError(error, this));
					};
				}
			});
		}

		if (this.options.signal) {
			const abort = () => {
				// See https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal/timeout_static#return_value
				if (this.options.signal?.reason?.name === 'TimeoutError') {
					this.destroy(new TimeoutError(this.options.signal.reason, this.timings!, this));
				} else {
					this.destroy(new AbortError(this));
				}
			};

			if (this.options.signal.aborted) {
				abort();
			} else {
				const abortListenerDisposer = addAbortListener(this.options.signal, abort);

				this._removeListeners = () => {
					abortListenerDisposer[Symbol.dispose]();
				};
			}
		}
	}

	async flush() {
		if (this._flushed) {
			return;
		}

		this._flushed = true;

		try {
			await this._finalizeBody();

			if (this.destroyed) {
				return;
			}

			await this._makeRequest();

			if (this.destroyed) {
				this._request?.destroy();
				return;
			}

			// Queued writes etc.
			for (const job of this._jobs) {
				job();
			}

			// Prevent memory leak
			this._jobs.length = 0;

			this._requestInitialized = true;
		} catch (error: unknown) {
			this._beforeError(normalizeError(error));
		}
	}

	_beforeError(error: Error): void {
		if (this._stopReading) {
			return;
		}

		const {response, options} = this;
		const attemptCount = this.retryCount + (error.name === 'RetryError' ? 0 : 1);

		this._stopReading = true;

		if (!(error instanceof RequestError)) {
			error = new RequestError(error.message, error, this);
		}

		const typedError = error as RequestError;

		void (async () => {
			// Node.js parser is really weird.
			// It emits post-request Parse Errors on the same instance as previous request. WTF.
			// Therefore, we need to check if it has been destroyed as well.
			//
			// Furthermore, Node.js 16 `response.destroy()` doesn't immediately destroy the socket,
			// but makes the response unreadable. So we additionally need to check `response.readable`.
			if (response?.readable && !response.rawBody && !this._request?.socket?.destroyed) {
				// @types/node has incorrect typings. `setEncoding` accepts `null` as well.
				response.setEncoding(this.readableEncoding!);

				const success = await this._setRawBody(response);

				if (success) {
					response.body = Buffer.from(response.rawBody!).toString();
				}
			}

			if (this.listenerCount('retry') !== 0) {
				let backoff: number;

				try {
					let retryAfter;
					if (response && 'retry-after' in response.headers) {
						retryAfter = Number(response.headers['retry-after']);
						if (Number.isNaN(retryAfter)) {
							retryAfter = Date.parse(response.headers['retry-after']!) - Date.now();

							if (retryAfter <= 0) {
								retryAfter = 1;
							}
						} else {
							retryAfter *= 1000;
						}
					}

					const retryOptions = options.retry as RetryOptions;

					const computedValue = calculateRetryDelay({
						attemptCount,
						retryOptions,
						error: typedError,
						retryAfter,
						computedValue: retryOptions.maxRetryAfter ?? options.timeout.request ?? Number.POSITIVE_INFINITY,
					});

					// When enforceRetryRules is true, respect the retry rules (limit, methods, statusCodes, errorCodes)
					// before calling the user's calculateDelay function. If computedValue is 0 (meaning retry is not allowed
					// based on these rules), skip calling calculateDelay entirely.
					// When false, always call calculateDelay, allowing it to override retry decisions.
					if (retryOptions.enforceRetryRules && computedValue === 0) {
						backoff = 0;
					} else {
						backoff = await retryOptions.calculateDelay({
							attemptCount,
							retryOptions,
							error: typedError,
							retryAfter,
							computedValue,
						});
					}
				} catch (error_: unknown) {
					const normalizedError = normalizeError(error_);
					void this._error(new RequestError(normalizedError.message, normalizedError, this));
					return;
				}

				if (backoff) {
					await new Promise<void>(resolve => {
						const timeout = setTimeout(resolve, backoff);
						this._stopRetry = () => {
							clearTimeout(timeout);
							resolve();
						};
					});

					// Something forced us to abort the retry
					if (this.destroyed) {
						return;
					}

					// Capture body BEFORE hooks run to detect reassignment
					const bodyBeforeHooks = this.options.body;

					try {
						for (const hook of this.options.hooks.beforeRetry) {
							// eslint-disable-next-line no-await-in-loop
							await hook(typedError, this.retryCount + 1);
						}
					} catch (error_: unknown) {
						const normalizedError = normalizeError(error_);
						void this._error(new RequestError(normalizedError.message, normalizedError, this));
						return;
					}

					// Something forced us to abort the retry
					if (this.destroyed) {
						return;
					}

					// Preserve stream body reassigned in beforeRetry hooks.
					const bodyAfterHooks = this.options.body;
					const bodyWasReassigned = bodyBeforeHooks !== bodyAfterHooks;

					// Resource cleanup and preservation logic for retry with body reassignment.
					// The Promise wrapper (as-promise/index.ts) compares body identity to detect consumed streams,
					// so we must preserve the body reference across destroy(). However, destroy() calls _destroy()
					// which destroys this.options.body, creating a complex dance of clear/restore operations.
					//
					// Key constraints:
					// 1. If body was reassigned, we must NOT destroy the NEW stream (it will be used for retry)
					// 2. If body was reassigned, we MUST destroy the OLD stream to prevent memory leaks
					// 3. We must restore the body reference after destroy() for identity checks in promise wrapper
					// 4. We cannot use the normal setter after destroy() because it validates stream readability
					if (bodyWasReassigned) {
						const oldBody = bodyBeforeHooks;
						// Temporarily clear body to prevent destroy() from destroying the new stream
						this.options.body = undefined;
						this.destroy();

						// Clean up the old stream resource if it's a stream and different from new body
						// (edge case: if old and new are same stream object, don't destroy it)
						if (is.nodeStream(oldBody) && oldBody !== bodyAfterHooks) {
							oldBody.destroy();
						}

						// Restore new body for promise wrapper's identity check
						if (is.nodeStream(bodyAfterHooks) && (bodyAfterHooks.readableEnded || bodyAfterHooks.destroyed)) {
							throw new TypeError('The reassigned stream body must be readable. Ensure you provide a fresh, readable stream in the beforeRetry hook.');
						}

						this.options.body = bodyAfterHooks;
					} else {
						// Body wasn't reassigned - use normal destroy flow which handles body cleanup
						this.destroy();
						// Note: We do NOT restore the body reference here. The stream was destroyed by _destroy()
						// and should not be accessed. The promise wrapper will see that body identity hasn't changed
						// and will detect it's a consumed stream, which is the correct behavior.
					}

					// Publish retry event
					publishRetry({
						requestId: this._requestId,
						retryCount: this.retryCount + 1,
						error: typedError,
						delay: backoff,
					});

					this.emit('retry', this.retryCount + 1, error, (updatedOptions?: OptionsInit) => {
						const request = new Request(options.url, updatedOptions, options);
						request.retryCount = this.retryCount + 1;

						process.nextTick(() => {
							void request.flush();
						});

						return request;
					});
					return;
				}
			}

			void this._error(typedError);
		})();
	}

	override _read(): void {
		this._triggerRead = true;

		const {response} = this;
		if (response && !this._stopReading) {
			// We cannot put this in the `if` above
			// because `.read()` also triggers the `end` event
			if (response.readableLength) {
				this._triggerRead = false;
			}

			let data;

			while ((data = response.read()) !== null) {
				this._downloadedSize += data.length; // eslint-disable-line @typescript-eslint/restrict-plus-operands

				if (this._incrementalBodyDecoder) {
					try {
						const decodedChunk = isBuffer(data) ? this._incrementalBodyDecoder.decode(data, {stream: true}) : String(data);
						if (decodedChunk.length > 0) {
							this._incrementalDecodedBodyChunks.push(decodedChunk);
						}
					} catch {
						this._incrementalBodyDecoder = undefined;
						this._incrementalDecodedBodyChunks = [];
					}
				}

				const progress = this.downloadProgress;

				if (progress.percent < 1) {
					this.emit('downloadProgress', progress);
				}

				this.push(data);
			}
		}
	}

	override _write(chunk: unknown, encoding: BufferEncoding | undefined, callback: (error?: Error | null) => void): void { // eslint-disable-line @typescript-eslint/no-restricted-types
		const write = (): void => {
			this._writeRequest(chunk, encoding, callback);
		};

		if (this._requestInitialized) {
			write();
		} else {
			this._jobs.push(write);
		}
	}

	override _final(callback: (error?: Error | null) => void): void { // eslint-disable-line @typescript-eslint/no-restricted-types
		const endRequest = (): void => {
			if (this._skipRequestEndInFinal) {
				this._skipRequestEndInFinal = false;
				callback();
				return;
			}

			const request = this._request;

			// We need to check if `this._request` is present,
			// because it isn't when we use cache.
			if (!request || request.destroyed) {
				callback();
				return;
			}

			request.end((error?: Error | null) => { // eslint-disable-line @typescript-eslint/no-restricted-types
				// The request has been destroyed before `_final` finished.
				// See https://github.com/nodejs/node/issues/39356
				if ((request as any)?._writableState?.errored) {
					return;
				}

				if (!error) {
					this._emitUploadComplete(request);
				}

				callback(error);
			});
		};

		if (this._requestInitialized) {
			endRequest();
		} else {
			this._jobs.push(endRequest);
		}
	}

	override _destroy(error: Error | null, callback: (error: Error | null) => void): void { // eslint-disable-line @typescript-eslint/no-restricted-types
		this._stopReading = true;
		this.flush = async () => {};

		// Prevent further retries
		this._stopRetry();
		this._cancelTimeouts();
		this._removeListeners();

		if (this.options) {
			const {body} = this.options;
			if (is.nodeStream(body)) {
				body.destroy();
			}
		}

		if (this._request) {
			this._request.destroy();
		}

		// Workaround: http-timer only sets timings.end when the response emits 'end'.
		// When a stream is destroyed before completion, the 'end' event may not fire,
		// leaving timings.end undefined. This should ideally be fixed in http-timer
		// by listening to the 'close' event, but we handle it here for now.
		// Only set timings.end if there was no error or abort (to maintain semantic correctness).
		const timings = (this._request as ClientRequestWithTimings)?.timings;
		if (timings && is.undefined(timings.end) && !is.undefined(timings.response) && is.undefined(timings.error) && is.undefined(timings.abort)) {
			timings.end = Date.now();
			if (is.undefined(timings.phases.total)) {
				timings.phases.download = timings.end - timings.response;
				timings.phases.total = timings.end - timings.start;
			}
		}

		// Preserve custom errors returned by beforeError hooks.
		// For other errors, wrap non-RequestError instances for consistency.
		if (error !== null && !is.undefined(error)) {
			const processedByHooks = error instanceof Error && errorsProcessedByHooks.has(error);

			if (!processedByHooks && !(error instanceof RequestError)) {
				error = error instanceof Error
					? new RequestError(error.message, error, this)
					: new RequestError(String(error), {}, this);
			}
		}

		callback(error);
	}

	override pipe<T extends NodeJS.WritableStream>(destination: T, options?: {end?: boolean}): T {
		if (destination instanceof ServerResponse) {
			this._pipedServerResponses.add(destination);
		}

		return super.pipe(destination, options);
	}

	override unpipe<T extends NodeJS.WritableStream>(destination: T): this {
		if (destination instanceof ServerResponse) {
			this._pipedServerResponses.delete(destination);
		}

		super.unpipe(destination);

		return this;
	}

	private _shouldIncrementallyDecodeBody(): boolean {
		const {responseType, encoding} = this.options;

		return Boolean(this._noPipe)
			&& (responseType === 'text' || responseType === 'json')
			&& isUtf8Encoding(encoding)
			&& typeof globalThis.TextDecoder === 'function';
	}

	private _checkContentLengthMismatch(): boolean {
		if (this.options.strictContentLength && this._expectedContentLength !== undefined) {
			// Use compressed bytes count when available (for compressed responses),
			// otherwise use _downloadedSize (for uncompressed responses)
			const actualSize = this._compressedBytesCount ?? this._downloadedSize;
			if (actualSize !== this._expectedContentLength) {
				this._beforeError(new ReadError({
					message: `Content-Length mismatch: expected ${this._expectedContentLength} bytes, received ${actualSize} bytes`,
					name: 'Error',
					code: 'ERR_HTTP_CONTENT_LENGTH_MISMATCH',
				}, this));
				return true;
			}
		}

		return false;
	}

	private async _finalizeBody(): Promise<void> {
		const {options} = this;
		const headers = options.getInternalHeaders();

		const isForm = !is.undefined(options.form);
		// eslint-disable-next-line @typescript-eslint/naming-convention
		const isJSON = !is.undefined(options.json);
		const isBody = !is.undefined(options.body);
		const cannotHaveBody = methodsWithoutBody.has(options.method) && !(options.method === 'GET' && options.allowGetBody);

		if (isForm || isJSON || isBody) {
			if (cannotHaveBody) {
				throw new TypeError(`The \`${options.method}\` method cannot be used with a body`);
			}

			// Serialize body
			const noContentType = !is.string(headers['content-type']);

			if (isBody) {
				// Native FormData
				if (options.body instanceof FormData) {
					const response = new Response(options.body);

					if (noContentType) {
						headers['content-type'] = response.headers.get('content-type') ?? 'multipart/form-data';
					}

					options.body = response.body!;
				} else if (Object.prototype.toString.call(options.body) === '[object FormData]') {
					throw new TypeError('Non-native FormData is not supported. Use globalThis.FormData instead.');
				}
			} else if (isForm) {
				if (noContentType) {
					headers['content-type'] = 'application/x-www-form-urlencoded';
				}

				const {form} = options;
				options.form = undefined;

				options.body = (new URLSearchParams(form as Record<string, string>)).toString();
			} else {
				if (noContentType) {
					headers['content-type'] = 'application/json';
				}

				const {json} = options;
				options.json = undefined;

				options.body = options.stringifyJson(json);
			}

			const uploadBodySize = getBodySize(options.body, headers);

			// See https://tools.ietf.org/html/rfc7230#section-3.3.2
			// A user agent SHOULD send a Content-Length in a request message when
			// no Transfer-Encoding is sent and the request method defines a meaning
			// for an enclosed payload body.  For example, a Content-Length header
			// field is normally sent in a POST request even when the value is 0
			// (indicating an empty payload body).  A user agent SHOULD NOT send a
			// Content-Length header field when the request message does not contain
			// a payload body and the method semantics do not anticipate such a
			// body.
			if (is.undefined(headers['content-length']) && is.undefined(headers['transfer-encoding']) && !cannotHaveBody && !is.undefined(uploadBodySize)) {
				headers['content-length'] = String(uploadBodySize);
			}
		}

		if (options.responseType === 'json' && !('accept' in headers)) {
			headers.accept = 'application/json';
		}

		this._bodySize = Number(headers['content-length']) || undefined;
	}

	private async _onResponseBase(response: IncomingMessageWithTimings): Promise<void> {
		// This will be called e.g. when using cache so we need to check if this request has been aborted.
		if (this.isAborted) {
			return;
		}

		const {options} = this;
		const {url} = options;

		this._nativeResponse = response;

		const statusCode = response.statusCode!;
		const {method} = options;

		// Skip decompression for responses that must not have bodies per RFC 9110:
		// - HEAD responses (any status code)
		// - 1xx (Informational): 100, 101, 102, 103, etc.
		// - 204 (No Content)
		// - 205 (Reset Content)
		// - 304 (Not Modified)
		const hasNoBody = method === 'HEAD'
			|| (statusCode >= 100 && statusCode < 200)
			|| statusCode === 204
			|| statusCode === 205
			|| statusCode === 304;

		if (options.decompress && !hasNoBody) {
			// When strictContentLength is enabled, track compressed bytes by listening to
			// the native response's data events before decompression
			if (options.strictContentLength) {
				this._compressedBytesCount = 0;
				this._nativeResponse.on('data', (chunk: Uint8Array) => {
					this._compressedBytesCount! += byteLength(chunk);
				});
			}

			response = decompressResponse(response);
		}

		const typedResponse = response as PlainResponse;
		if (!Object.hasOwn(typedResponse, 'headers')) {
			Object.defineProperty(typedResponse, 'headers', {
				value: typedResponse.headers,
				enumerable: true,
				writable: true,
				configurable: true,
			});
		}

		typedResponse.statusMessage ||= http.STATUS_CODES[statusCode]; // eslint-disable-line @typescript-eslint/prefer-nullish-coalescing -- The status message can be empty.
		typedResponse.url = stripUrlAuth(options.url!);
		typedResponse.requestUrl = this.requestUrl!;
		typedResponse.redirectUrls = this.redirectUrls;
		typedResponse.request = this;
		const nativeResponse = this._nativeResponse as IncomingMessageWithTimings & {fromCache?: boolean};
		typedResponse.isFromCache = nativeResponse.fromCache ?? false;
		typedResponse.ip = this.ip;
		typedResponse.retryCount = this.retryCount;
		typedResponse.ok = isResponseOk(typedResponse);

		this._isFromCache = typedResponse.isFromCache;

		this._responseSize = Number(response.headers['content-length']) || undefined;

		this.response = typedResponse;
		// eslint-disable-next-line @typescript-eslint/naming-convention
		this._incrementalBodyDecoder = this._shouldIncrementallyDecodeBody() ? new globalThis.TextDecoder('utf8', {ignoreBOM: true}) : undefined;
		this._incrementalDecodedBodyChunks = [];

		// Publish response start event
		publishResponseStart({
			requestId: this._requestId,
			url: typedResponse.url,
			statusCode,
			headers: response.headers,
			isFromCache: typedResponse.isFromCache,
		});

		response.once('error', (error: Error) => {
			this._aborted = true;

			this._beforeError(new ReadError(error, this));
		});

		response.once('aborted', () => {
			this._aborted = true;

			// Check if there's a content-length mismatch to provide a more specific error
			if (!this._checkContentLengthMismatch()) {
				this._beforeError(new ReadError({
					name: 'Error',
					message: 'The server aborted pending request',
					code: 'ECONNRESET',
				}, this));
			}
		});

		const noPipeCookieJarRawBodyPromise = this._noPipe
			&& is.object(options.cookieJar)
			&& !(response.headers.location && redirectCodes.has(statusCode))
			? this._setRawBody(response)
			: undefined;

		const rawCookies = response.headers['set-cookie'];
		if (is.object(options.cookieJar) && rawCookies) {
			let promises: Array<Promise<unknown>> = rawCookies.map(async (rawCookie: string) => (options.cookieJar as PromiseCookieJar).setCookie(rawCookie, url!.toString()));

			if (options.ignoreInvalidCookies) {
				promises = promises.map(async promise => {
					try {
						await promise;
					} catch {}
				});
			}

			try {
				await Promise.all(promises);
			} catch (error: unknown) {
				this._beforeError(normalizeError(error));
				return;
			}
		}

		// The above is running a promise, therefore we need to check if this request has been aborted yet again.
		if (this.isAborted) {
			return;
		}

		if (response.headers.location && redirectCodes.has(statusCode)) {
			// We're being redirected, we don't care about the response.
			// It'd be best to abort the request, but we can't because
			// we would have to sacrifice the TCP connection. We don't want that.
			const shouldFollow = typeof options.followRedirect === 'function' ? options.followRedirect(typedResponse) : options.followRedirect;
			if (shouldFollow) {
				response.resume();

				this._cancelTimeouts();
				this._unproxyEvents();

				if (this.redirectUrls.length >= options.maxRedirects) {
					this._beforeError(new MaxRedirectsError(this));
					return;
				}

				this._request = undefined;

				// Reset progress for the new request.
				this._downloadedSize = 0;
				this._uploadedSize = 0;

				const updatedOptions = new Options(undefined, undefined, this.options);

				const serverRequestedGet = statusCode === 303 && updatedOptions.method !== 'GET' && updatedOptions.method !== 'HEAD';
				const canRewrite = statusCode !== 307 && statusCode !== 308;
				const userRequestedGet = updatedOptions.methodRewriting && canRewrite;
				const shouldDropBody = serverRequestedGet || userRequestedGet;

				if (shouldDropBody) {
					updatedOptions.method = 'GET';

					updatedOptions.body = undefined;
					updatedOptions.json = undefined;
					updatedOptions.form = undefined;

					updatedOptions.deleteInternalHeader('content-length');
					// Only clear `_bodySize` when the redirect drops the request body.
					this._bodySize = undefined;
				}

				try {
					// We need this in order to support UTF-8
					const redirectBuffer = Buffer.from(response.headers.location, 'binary').toString();
					const redirectUrl = new URL(redirectBuffer, url);

					if (!isUnixSocketURL(url as URL) && isUnixSocketURL(redirectUrl)) {
						this._beforeError(new RequestError('Cannot redirect to UNIX socket', {}, this));
						return;
					}

					// Redirecting to a different site, clear sensitive data.
					// For UNIX sockets, different socket paths are also different origins.
					const isDifferentOrigin = redirectUrl.protocol !== (url as URL).protocol
						|| redirectUrl.hostname !== (url as URL).hostname
						|| redirectUrl.port !== (url as URL).port
						|| getUnixSocketPath(url as URL) !== getUnixSocketPath(redirectUrl);

					if (isDifferentOrigin) {
						const updatedHeaders = updatedOptions.getInternalHeaders();

						if ('host' in updatedHeaders) {
							updatedOptions.deleteInternalHeader('host');
						}

						if ('cookie' in updatedHeaders) {
							updatedOptions.deleteInternalHeader('cookie');
						}

						if ('authorization' in updatedHeaders) {
							updatedOptions.deleteInternalHeader('authorization');
						}

						if (updatedOptions.username || updatedOptions.password) {
							updatedOptions.username = '';
							updatedOptions.password = '';
						}
					} else {
						redirectUrl.username = updatedOptions.username;
						redirectUrl.password = updatedOptions.password;
					}

					this.redirectUrls.push(redirectUrl);
					updatedOptions.url = redirectUrl;

					for (const hook of updatedOptions.hooks.beforeRedirect) {
						// eslint-disable-next-line no-await-in-loop
						await hook(updatedOptions as NormalizedOptions, typedResponse);
					}

					// Publish redirect event
					publishRedirect({
						requestId: this._requestId,
						fromUrl: url!.toString(),
						toUrl: redirectUrl.toString(),
						statusCode,
					});

					this.emit('redirect', updatedOptions, typedResponse);

					this.options = updatedOptions;

					await this._makeRequest();
				} catch (error: unknown) {
					this._beforeError(normalizeError(error));
					return;
				}

				return;
			}
		}

		// `HTTPError`s always have `error.response.body` defined.
		// Therefore, we cannot retry if `options.throwHttpErrors` is false.
		// On the last retry, if `options.throwHttpErrors` is false, we would need to return the body,
		// but that wouldn't be possible since the body would be already read in `error.response.body`.
		if (options.isStream && options.throwHttpErrors && !isResponseOk(typedResponse)) {
			this._beforeError(new HTTPError(typedResponse));
			return;
		}

		// Store the expected content-length from the native response for validation.
		// This is the content-length before decompression, which is what actually gets transferred.
		// Skip storing for responses that shouldn't have bodies per RFC 9110.
		// When decompression occurs, only store if strictContentLength is enabled.
		const wasDecompressed = response !== this._nativeResponse;
		if (!hasNoBody && (!wasDecompressed || options.strictContentLength)) {
			const contentLengthHeader = this._nativeResponse.headers['content-length'];
			if (contentLengthHeader !== undefined) {
				const expectedLength = Number(contentLengthHeader);
				if (!Number.isNaN(expectedLength) && expectedLength >= 0) {
					this._expectedContentLength = expectedLength;
				}
			}
		}

		// Set up end listener AFTER redirect check to avoid emitting progress for redirect responses
		let responseEndHandled = false;
		const handleResponseEnd = () => {
			if (responseEndHandled) {
				return;
			}

			responseEndHandled = true;

			// Validate content-length if it was provided
			// Per RFC 9112: "If the sender closes the connection before the indicated number
			// of octets are received, the recipient MUST consider the message to be incomplete"
			if (this._checkContentLengthMismatch()) {
				return;
			}

			this._responseSize = this._downloadedSize;
			this.emit('downloadProgress', this.downloadProgress);

			// Publish response end event
			publishResponseEnd({
				requestId: this._requestId,
				url: typedResponse.url,
				statusCode,
				bodySize: this._downloadedSize,
				timings: this.timings,
			});

			this.push(null);
		};

		response.once('end', handleResponseEnd);

		this.emit('downloadProgress', this.downloadProgress);

		response.on('readable', () => {
			if (this._triggerRead) {
				this._read();
			}
		});

		this.on('resume', () => {
			response.resume();
		});

		this.on('pause', () => {
			response.pause();
		});

		if (this._noPipe) {
			const captureFromResponse = response.readableEnded || noPipeCookieJarRawBodyPromise !== undefined;
			const success = noPipeCookieJarRawBodyPromise
				? await noPipeCookieJarRawBodyPromise
				: await this._setRawBody(captureFromResponse ? response : this);

			if (captureFromResponse) {
				handleResponseEnd();
			}

			if (success) {
				this.emit('response', response);
			}

			return;
		}

		this.emit('response', response);

		for (const destination of this._pipedServerResponses) {
			if (destination.headersSent) {
				continue;
			}

			// Check if decompression actually occurred by comparing stream objects.
			// decompressResponse wraps the response stream when it decompresses,
			// so response !== this._nativeResponse indicates decompression happened.
			const wasDecompressed = response !== this._nativeResponse;

			for (const key in response.headers) {
				if (Object.hasOwn(response.headers, key)) {
					const value = response.headers[key];

					// When decompression occurred, skip content-encoding and content-length
					// as they refer to the compressed data, not the decompressed stream.
					if (wasDecompressed && (key === 'content-encoding' || key === 'content-length')) {
						continue;
					}

					// Skip if value is undefined
					if (value !== undefined) {
						destination.setHeader(key, value);
					}
				}
			}

			destination.statusCode = statusCode;
		}
	}

	private async _setRawBody(from: Readable = this): Promise<boolean> {
		try {
			// Errors are emitted via the `error` event
			const fromArray = await from.toArray();
			const hasNonStringChunk = fromArray.some(chunk => typeof chunk !== 'string');
			const rawBody = hasNonStringChunk
				? concatUint8Arrays((fromArray as Array<string | Uint8Array>).map(chunk => typeof chunk === 'string' ? textEncoder.encode(chunk) : chunk))
				: textEncoder.encode((fromArray as string[]).join(''));
			const shouldUseIncrementalDecodedBody = from === this && this._incrementalBodyDecoder !== undefined;

			// On retry Request is destroyed with no error, therefore the above will successfully resolve.
			// So in order to check if this was really successful, we need to check if it has been properly ended.
			if (
				!this.isAborted
				&& this.response
			) {
				this.response.rawBody = rawBody;
				if (from !== this) {
					this._downloadedSize = rawBody.byteLength;
				}

				if (shouldUseIncrementalDecodedBody) {
					try {
						const decoder = this._incrementalBodyDecoder!;
						const finalDecodedChunk = decoder.decode();
						if (finalDecodedChunk.length > 0) {
							this._incrementalDecodedBodyChunks.push(finalDecodedChunk);
						}

						cacheDecodedBody(this.response, this._incrementalDecodedBodyChunks.join(''));
					} catch {}
				}

				this._incrementalBodyDecoder = undefined;
				this._incrementalDecodedBodyChunks = [];

				return true;
			}
		} catch {}

		this._incrementalBodyDecoder = undefined;
		this._incrementalDecodedBodyChunks = [];

		return false;
	}

	private async _onResponse(response: IncomingMessageWithTimings): Promise<void> {
		try {
			await this._onResponseBase(response);
		} catch (error: unknown) {
			/* istanbul ignore next: better safe than sorry */
			this._beforeError(normalizeError(error));
		}
	}

	private _onRequest(request: ClientRequest): void {
		const {options} = this;
		const {timeout, url} = options;

		// Publish request start event
		publishRequestStart({
			requestId: this._requestId,
			url: getSanitizedUrl(this.options),
			method: options.method,
			headers: options.headers,
		});

		timer(request);

		this._cancelTimeouts = timedOut(request, timeout, url as URL);

		if (this.options.http2) {
			// Unset stream timeout, as the `timeout` option was used only for connection timeout.
			// We remove all 'timeout' listeners instead of calling setTimeout(0) because:
			// 1. setTimeout(0) causes a memory leak (see https://github.com/sindresorhus/got/issues/690)
			// 2. With HTTP/2 connection reuse, setTimeout(0) accumulates listeners on the socket
			// 3. removeAllListeners('timeout') properly cleans up without the memory leak
			request.removeAllListeners('timeout');

			// For HTTP/2, wait for socket and remove timeout listeners from it
			request.once('socket', (socket: Socket) => {
				socket.removeAllListeners('timeout');
			});
		}

		let lastRequestError: Error | undefined;
		const responseEventName = options.cache ? 'cacheableResponse' : 'response';

		const responseHandler = (response: IncomingMessageWithTimings) => {
			void this._onResponse(response);
		};

		request.once(responseEventName, responseHandler);

		const emitRequestError = (error: Error): void => {
			this._aborted = true;

			// Force clean-up, because some packages (e.g. nock) don't do this.
			request.destroy();

			const wrappedError = error instanceof TimedOutTimeoutError ? new TimeoutError(error, this.timings!, this) : new RequestError(error.message, error, this);
			this._beforeError(wrappedError);
		};

		request.once('error', (error: Error) => {
			lastRequestError = error;

			// Ignore errors from requests superseded by a redirect.
			if (this._request !== request) {
				return;
			}

			/*
			Transient write errors (EPIPE, ECONNRESET) often fire during redirects when the
			server closes the connection after sending the redirect response. Defer by one
			microtask to let the response event make the request stale.
			*/
			if (isTransientWriteError(error)) {
				queueMicrotask(() => {
					if (this._isRequestStale(request)) {
						return;
					}

					emitRequestError(error);
				});

				return;
			}

			emitRequestError(error);
		});

		if (!options.cache) {
			request.once('close', () => {
				if (this._request !== request || this._requestHasResponse(request) || this._stopReading) {
					return;
				}

				this._beforeError(lastRequestError ?? new ReadError({
					name: 'Error',
					message: 'The server aborted pending request',
					code: 'ECONNRESET',
				}, this));
			});
		}

		this._unproxyEvents = proxyEvents(request, this, proxiedRequestEvents);
		this._request = request;

		this.emit('uploadProgress', this.uploadProgress);

		this._sendBody();

		this.emit('request', request);
	}

	private _requestHasResponse(request: ClientRequest): boolean {
		return Boolean((request as ClientRequest & {res?: unknown}).res);
	}

	private _isRequestStale(request: ClientRequest): boolean {
		return this._request !== request || this._requestHasResponse(request) || request.destroyed || request.writableEnded;
	}

	private async _asyncWrite(chunk: any): Promise<void> {
		return new Promise((resolve, reject) => {
			super.write(chunk, error => {
				if (error) {
					reject(error);
					return;
				}

				resolve();
			});
		});
	}

	private _sendBody() {
		// Send body
		const {body} = this.options;
		const currentRequest = this.redirectUrls.length === 0 ? this : this._request ?? this;

		if (is.nodeStream(body)) {
			body.pipe(currentRequest);
		} else if (is.buffer(body)) {
			// Buffer should be sent directly without conversion
			this._writeBodyInChunks(body, currentRequest);
		} else if (is.typedArray(body)) {
			// Typed arrays should be treated like buffers, not iterated over
			// Create a Uint8Array view over the data (Node.js streams accept Uint8Array)
			const typedArray = body as ArrayBufferView;
			const uint8View = new Uint8Array(typedArray.buffer, typedArray.byteOffset, typedArray.byteLength);
			this._writeBodyInChunks(uint8View, currentRequest);
		} else if (is.asyncIterable(body) || (is.iterable(body) && !is.string(body) && !isBuffer(body))) {
			(async () => {
				try {
					for await (const chunk of body) {
						await this._asyncWrite(chunk);
					}

					super.end();
				} catch (error: unknown) {
					this._beforeError(normalizeError(error));
				}
			})();
		} else if (is.undefined(body)) {
			// No body to send, end the request
			const cannotHaveBody = methodsWithoutBody.has(this.options.method) && !(this.options.method === 'GET' && this.options.allowGetBody);

			if ((this._noPipe ?? false) || cannotHaveBody || currentRequest !== this) {
				currentRequest.end();
			}
		} else {
			// Handles string bodies (from json/form options).
			this._writeBodyInChunks(Buffer.from(body as string), currentRequest);
		}
	}

	/*
	Write a body buffer in chunks to enable granular `uploadProgress` events.

	Without chunking, string/Uint8Array/TypedArray bodies are written in a single call, causing `uploadProgress` to only emit 0% and 100% with nothing in between.

	The 64 KB chunk size matches Node.js fs stream defaults.
	*/
	private _writeBodyInChunks(buffer: Uint8Array, currentRequest: Request | ClientRequest) {
		const isInitialRequest = currentRequest === this;

		(async () => {
			let request: ClientRequest | undefined;

			try {
				request = isInitialRequest ? this._request : currentRequest as ClientRequest;
				const activeRequest = request;

				if (!activeRequest) {
					if (isInitialRequest) {
						super.end();
					}

					return;
				}

				if (activeRequest.destroyed) {
					return;
				}

				await this._writeChunksToRequest(buffer, activeRequest);

				if (this._isRequestStale(activeRequest)) {
					this._finalizeStaleChunkedWrite(activeRequest, isInitialRequest);
					return;
				}

				if (isInitialRequest) {
					super.end();
					return;
				}

				await new Promise<void>((resolve, reject) => {
					activeRequest.end((error?: Error | null) => { // eslint-disable-line @typescript-eslint/no-restricted-types
						if (error) {
							reject(error);
							return;
						}

						if (this._request === activeRequest && !activeRequest.destroyed) {
							this._emitUploadComplete(activeRequest);
						}

						resolve();
					});
				});
			} catch (error: unknown) {
				const normalizedError = normalizeError(error);

				// Transient write errors (EPIPE, ECONNRESET) are handled by the request-level
				// error and close handlers. For initial redirected writes, still finalize
				// writable state once the stale transition becomes observable.
				if (isTransientWriteError(normalizedError)) {
					if (isInitialRequest && request) {
						const initialRequest = request;
						let didFinalize = false;
						const finalizeIfStale = () => {
							if (didFinalize || !this._isRequestStale(initialRequest)) {
								return;
							}

							didFinalize = true;
							this._finalizeStaleChunkedWrite(initialRequest, true);
						};

						finalizeIfStale();

						if (!didFinalize) {
							initialRequest.once('response', finalizeIfStale);
							queueMicrotask(finalizeIfStale);
						}
					}

					return;
				}

				if (!isInitialRequest && this._isRequestStale(currentRequest as ClientRequest)) {
					return;
				}

				this._beforeError(normalizedError);
			}
		})();
	}

	private _finalizeStaleChunkedWrite(request: ClientRequest, isInitialRequest: boolean) {
		if (!request.destroyed && !request.writableEnded) {
			request.destroy();
		}

		if (isInitialRequest) {
			// Finalize writable state without ending the active redirected request.
			this._skipRequestEndInFinal = true;
			super.end();
		}
	}

	private _emitUploadComplete(request: ClientRequest) {
		this._bodySize = this._uploadedSize;
		this.emit('uploadProgress', this.uploadProgress);
		request.emit('upload-complete');
	}

	private async _writeChunksToRequest(buffer: Uint8Array, request: ClientRequest): Promise<void> {
		const chunkSize = 65_536; // 64 KB
		const isStale = () => this._isRequestStale(request);

		for (const part of chunk(buffer, chunkSize)) {
			if (isStale()) {
				return;
			}

			// eslint-disable-next-line no-await-in-loop
			await new Promise<void>((resolve, reject) => {
				this._writeRequest(part, undefined, error => {
					if (error) {
						if (isStale()) {
							resolve();
							return;
						}

						reject(error);
						return;
					}

					if (isStale()) {
						resolve();
						return;
					}

					setImmediate(resolve);
				}, request);
			});
		}
	}

	private _prepareCache(cache: string | StorageAdapter) {
		if (cacheableStore.has(cache)) {
			return;
		}

		const cacheableRequest = new CacheableRequest(
			((requestOptions: RequestOptions, handler?: (response: IncomingMessageWithTimings) => void): ClientRequest => {
				/**
				Wraps the cacheable-request handler to run beforeCache hooks.
				These hooks control caching behavior by:
				- Directly mutating the response object (changes apply to what gets cached)
				- Returning `false` to prevent caching
				- Returning `void`/`undefined` to use default caching behavior

				Hooks use direct mutation - they can modify response.headers, response.statusCode, etc.
				Mutations take effect immediately and determine what gets cached.
				*/
				const wrappedHandler = handler
					? (response: IncomingMessageWithTimings) => {
						const {beforeCacheHooks, gotRequest} = requestOptions as any;

						// Early return if no hooks - cache the original response
						if (!beforeCacheHooks || beforeCacheHooks.length === 0) {
							handler(response);
							return;
						}

						try {
							// Call each beforeCache hook with the response
							// Hooks can directly mutate the response - mutations take effect immediately
							for (const hook of beforeCacheHooks) {
								const result = hook(response);

								if (result === false) {
									// Prevent caching by adding no-cache headers
									// Mutate the response directly to add headers
									response.headers['cache-control'] = 'no-cache, no-store, must-revalidate';
									response.headers.pragma = 'no-cache';
									response.headers.expires = '0';
									handler(response);
									// Don't call remaining hooks - we've decided not to cache
									return;
								}

								if (is.promise(result)) {
									// BeforeCache hooks must be synchronous because cacheable-request's handler is synchronous
									throw new TypeError('beforeCache hooks must be synchronous. The hook returned a Promise, but this hook must return synchronously. If you need async logic, use beforeRequest hook instead.');
								}

								if (result !== undefined) {
									// Hooks should return false or undefined only
									// Mutations work directly - no need to return the response
									throw new TypeError('beforeCache hook must return false or undefined. To modify the response, mutate it directly.');
								}
								// Else: void/undefined = continue
							}
						} catch (error: unknown) {
							const normalizedError = normalizeError(error);
							// Convert hook errors to RequestError and propagate
							// This is consistent with how other hooks handle errors
							if (gotRequest) {
								gotRequest._beforeError(normalizedError instanceof RequestError ? normalizedError : new RequestError(normalizedError.message, normalizedError, gotRequest));
								// Don't call handler when error was propagated successfully
								return;
							}

							// If gotRequest is missing, log the error to aid debugging
							// We still call the handler to prevent the request from hanging
							console.error('Got: beforeCache hook error (request context unavailable):', normalizedError);
							// Call handler with response (potentially partially modified)
							handler(response);
							return;
						}

						// All hooks ran successfully
						// Cache the response with any mutations applied
						handler(response);
					}
					: handler;

				const result = (requestOptions as any)._request(requestOptions, wrappedHandler);

				// TODO: remove this when `cacheable-request` supports async request functions.
				if (is.promise(result)) {
					// We only need to implement the error handler in order to support HTTP2 caching.
					// The result will be a promise anyway.
					// @ts-expect-error ignore
					result.once = (event: string, handler: (reason: unknown) => void) => {
						if (event === 'error') {
							(async () => {
								try {
									await result;
								} catch (error) {
									handler(error);
								}
							})();
						} else if (event === 'abort' || event === 'destroy') {
							// The empty catch is needed here in case when
							// it rejects before it's `await`ed in `_makeRequest`.
							(async () => {
								try {
									const request = (await result) as ClientRequest;
									request.once(event, handler);
								} catch {}
							})();
						} else {
							/* istanbul ignore next: safety check */
							throw new Error(`Unknown HTTP2 promise event: ${event}`);
						}

						return result;
					};
				}

				return result;
			}) as typeof http.request,
			cache as StorageAdapter,
		);
		cacheableStore.set(cache, cacheableRequest.request());
	}

	private async _createCacheableRequest(url: URL, options: RequestOptions): Promise<ClientRequest | ResponseLike> {
		return new Promise<ClientRequest | ResponseLike>((resolve, reject) => {
			Object.assign(options, {
				protocol: url.protocol,
				hostname: is.string(url.hostname) && url.hostname.startsWith('[') ? url.hostname.slice(1, -1) : url.hostname,
				host: url.host,
				hash: url.hash === '' ? '' : (url.hash ?? null),
				search: url.search === '' ? '' : (url.search ?? null),
				pathname: url.pathname,
				href: url.href,
				path: `${url.pathname || ''}${url.search || ''}`,
				...(is.string(url.port) && url.port.length > 0 ? {port: Number(url.port)} : {}),
				...(url.username || url.password ? {auth: `${url.username || ''}:${url.password || ''}`} : {}),
			});

			let request: ClientRequest | Promise<ClientRequest>;

			// TODO: Fix `cacheable-response`. This is ugly.
			const cacheRequest = cacheableStore.get((options as any).cache)!(options as CacheableOptions, async (response: any) => {
				response._readableState.autoDestroy = false;

				if (request) {
					const fix = () => {
						// For ResponseLike objects from cache, set complete to true if not already set.
						// For real HTTP responses, copy from the underlying response.
						if (response.req) {
							response.complete = response.req.res.complete;
						} else if (response.complete === undefined) {
							// ResponseLike from cache should have complete = true
							response.complete = true;
						}
					};

					response.prependOnceListener('end', fix);
					fix();

					(await request).emit('cacheableResponse', response);
				}

				resolve(response);
			});

			cacheRequest.once('error', reject);
			cacheRequest.once('request', async (requestOrPromise: ClientRequest | Promise<ClientRequest>) => {
				request = requestOrPromise;
				resolve(request);
			});
		});
	}

	private async _makeRequest(): Promise<void> {
		const {options} = this;
		const headers = options.getInternalHeaders();
		const {username, password} = options;
		const cookieJar = options.cookieJar as PromiseCookieJar | undefined;

		for (const key in headers) {
			if (is.undefined(headers[key])) {
				options.deleteInternalHeader(key);
			} else if (is.null(headers[key])) {
				throw new TypeError(`Use \`undefined\` instead of \`null\` to delete the \`${key}\` header`);
			}
		}

		if (options.decompress && is.undefined(headers['accept-encoding'])) {
			const encodings = ['gzip', 'deflate'];
			if (supportsBrotli) {
				encodings.push('br');
			}

			if (supportsZstd) {
				encodings.push('zstd');
			}

			options.setInternalHeader('accept-encoding', encodings.join(', '));
		}

		if (username || password) {
			const credentials = Buffer.from(`${username}:${password}`).toString('base64');
			options.setInternalHeader('authorization', `Basic ${credentials}`);
		}

		// Set cookies
		if (cookieJar) {
			let cookieString = '';
			cookieString = await cookieJar.getCookieString(options.url!.toString());

			if (is.nonEmptyString(cookieString)) {
				options.setInternalHeader('cookie', cookieString);
			}
		}

		let request: ReturnType<Options['getRequestFunction']> | undefined;

		for (const hook of options.hooks.beforeRequest) {
			// eslint-disable-next-line no-await-in-loop
			const result = await hook(options as NormalizedOptions, {retryCount: this.retryCount});

			if (!is.undefined(result)) {
				// @ts-expect-error Skip the type mismatch to support abstract responses
				request = () => result;
				break;
			}
		}

		request ??= options.getRequestFunction();

		const url = options.url as URL;

		this._requestOptions = options.createNativeRequestOptions() as NativeRequestOptions;

		if (options.cache) {
			(this._requestOptions as any)._request = request;
			(this._requestOptions as any).cache = options.cache;
			(this._requestOptions as any).body = options.body;
			(this._requestOptions as any).beforeCacheHooks = options.hooks.beforeCache;
			(this._requestOptions as any).gotRequest = this;

			try {
				this._prepareCache(options.cache as StorageAdapter);
			} catch (error: unknown) {
				throw new CacheError(normalizeError(error), this);
			}
		}

		// Cache support
		const function_ = options.cache ? this._createCacheableRequest : request;

		try {
			// We can't do `await fn(...)`,
			// because stream `error` event can be emitted before `Promise.resolve()`.
			let requestOrResponse = function_!(url, this._requestOptions);

			if (is.promise(requestOrResponse)) {
				requestOrResponse = await requestOrResponse;
			}

			if (isClientRequest(requestOrResponse!)) {
				this._onRequest(requestOrResponse);
			} else if (this.writableEnded) {
				void this._onResponse(requestOrResponse as IncomingMessageWithTimings);
			} else {
				this.once('finish', () => {
					void this._onResponse(requestOrResponse as IncomingMessageWithTimings);
				});

				this._sendBody();
			}
		} catch (error) {
			if (error instanceof CacheableCacheError) {
				throw new CacheError(error, this);
			}

			throw error;
		}
	}

	private async _error(error: RequestError): Promise<void> {
		try {
			if (this.options && error instanceof HTTPError && !this.options.throwHttpErrors) {
				// This branch can be reached only when using the Promise API
				// Skip calling the hooks on purpose.
				// See https://github.com/sindresorhus/got/issues/2103
			} else if (this.options) {
				const hooks = this.options.hooks.beforeError;
				if (hooks.length > 0) {
					for (const hook of hooks) {
						// eslint-disable-next-line no-await-in-loop
						error = await hook(error) as RequestError;

						// Validate hook return value
						if (!(error instanceof Error)) {
							throw new TypeError(`The \`beforeError\` hook must return an Error instance. Received ${is.string(error) ? 'string' : String(typeof error)}.`);
						}
					}

					// Mark this error as processed by hooks so _destroy preserves custom error types.
					// Only mark non-RequestError errors, since RequestErrors are already preserved
					// by the instanceof check in _destroy (line 642).
					if (!(error instanceof RequestError)) {
						errorsProcessedByHooks.add(error);
					}
				}
			}
		} catch (error_: unknown) {
			const normalizedError = normalizeError(error_);
			error = new RequestError(normalizedError.message, normalizedError, this);
		}

		// Publish error event
		publishError({
			requestId: this._requestId,
			url: getSanitizedUrl(this.options),
			error,
			timings: this.timings,
		});

		this.destroy(error);

		// Manually emit error for Promise API to ensure it receives it.
		// Node.js streams may not re-emit if an error was already emitted during retry attempts.
		// Only emit for Promise API (_noPipe = true) to avoid double emissions in stream mode.
		// Use process.nextTick to defer emission and allow destroy() to complete first.
		// See https://github.com/sindresorhus/got/issues/1995
		if (this._noPipe) {
			process.nextTick(() => {
				this.emit('error', error);
			});
		}
	}

	private _writeRequest(chunk: any, encoding: BufferEncoding | undefined, callback: (error?: Error | null) => void, request: ClientRequest | undefined = this._request): void { // eslint-disable-line @typescript-eslint/no-restricted-types
		if (!request || request.destroyed) {
			// When there's no request (e.g., using cached response from beforeRequest hook),
			// we still need to call the callback to allow the stream to finish properly.
			callback();
			return;
		}

		request.write(chunk, encoding as any, (error?: Error | null) => { // eslint-disable-line @typescript-eslint/no-restricted-types
			// The `!destroyed` check is required to prevent `uploadProgress` being emitted after the stream was destroyed.
			// The `this._request === request` check prevents stale write callbacks from a pre-redirect request from incrementing `_uploadedSize` after it's been reset.
			if (!error && !request.destroyed && this._request === request) {
				// For strings, encode them first to measure the actual bytes that will be sent
				const bytes = typeof chunk === 'string' ? Buffer.from(chunk, encoding) : chunk;
				this._uploadedSize += byteLength(bytes);

				const progress = this.uploadProgress;

				if (progress.percent < 1) {
					this.emit('uploadProgress', progress);
				}
			}

			callback(error);
		});
	}

	/**
	The remote IP address.
	*/
	get ip(): string | undefined {
		return this.socket?.remoteAddress;
	}

	/**
	Indicates whether the request has been aborted or not.
	*/
	get isAborted(): boolean {
		return this._aborted;
	}

	get socket(): Socket | undefined {
		return this._request?.socket ?? undefined;
	}

	/**
	Progress event for downloading (receiving a response).
	*/
	get downloadProgress(): Progress {
		let percent;
		if (this._responseSize) {
			percent = this._downloadedSize / this._responseSize;
		} else if (this._responseSize === this._downloadedSize) {
			percent = 1;
		} else {
			percent = 0;
		}

		return {
			percent,
			transferred: this._downloadedSize,
			total: this._responseSize,
		};
	}

	/**
	Progress event for uploading (sending a request).
	*/
	get uploadProgress(): Progress {
		let percent;
		if (this._bodySize) {
			percent = this._uploadedSize / this._bodySize;
		} else if (this._bodySize === this._uploadedSize) {
			percent = 1;
		} else {
			percent = 0;
		}

		return {
			percent,
			transferred: this._uploadedSize,
			total: this._bodySize,
		};
	}

	/**
	The object contains the following properties:

	- `start` - Time when the request started.
	- `socket` - Time when a socket was assigned to the request.
	- `lookup` - Time when the DNS lookup finished.
	- `connect` - Time when the socket successfully connected.
	- `secureConnect` - Time when the socket securely connected.
	- `upload` - Time when the request finished uploading.
	- `response` - Time when the request fired `response` event.
	- `end` - Time when the response fired `end` event.
	- `error` - Time when the request fired `error` event.
	- `abort` - Time when the request fired `abort` event.
	- `phases`
		- `wait` - `timings.socket - timings.start`
		- `dns` - `timings.lookup - timings.socket`
		- `tcp` - `timings.connect - timings.lookup`
		- `tls` - `timings.secureConnect - timings.connect`
		- `request` - `timings.upload - (timings.secureConnect || timings.connect)`
		- `firstByte` - `timings.response - timings.upload`
		- `download` - `timings.end - timings.response`
		- `total` - `(timings.end || timings.error || timings.abort) - timings.start`

	If something has not been measured yet, it will be `undefined`.

	__Note__: The time is a `number` representing the milliseconds elapsed since the UNIX epoch.
	*/
	get timings(): Timings | undefined {
		return (this._request as ClientRequestWithTimings)?.timings;
	}

	/**
	Whether the response was retrieved from the cache.
	*/
	get isFromCache(): boolean | undefined {
		return this._isFromCache;
	}

	get reusedSocket(): boolean | undefined {
		return this._request?.reusedSocket;
	}

	/**
	Whether the stream is read-only. Returns `true` when `body`, `json`, or `form` options are provided.
	*/
	get isReadonly(): boolean {
		return !is.undefined(this.options?.body) || !is.undefined(this.options?.json) || !is.undefined(this.options?.form);
	}
}
```

## File: `source/core/options.ts`
```typescript
import process from 'node:process';
import {promisify, inspect, type InspectOptions} from 'node:util';
import {checkServerIdentity, type SecureContextOptions, type DetailedPeerCertificate} from 'node:tls';
// DO NOT use destructuring for `https.request` and `http.request` as it's not compatible with `nock`.
import https, {
	type RequestOptions as HttpsRequestOptions,
	type Agent as HttpsAgent,
} from 'node:https';
import http, {
	type Agent as HttpAgent,
	type ClientRequest,
} from 'node:http';
import type {Readable} from 'node:stream';
import type {Socket, LookupFunction} from 'node:net';
import is, {assert} from '@sindresorhus/is';
import lowercaseKeys from 'lowercase-keys';
import CacheableLookup from 'cacheable-lookup';
import http2wrapper, {type ClientHttp2Session} from 'http2-wrapper';
import type {KeyvStoreAdapter} from 'keyv';
import type KeyvType from 'keyv';
import type ResponseLike from 'responselike';
import type {RequestPromise} from '../as-promise/types.js';
import type {IncomingMessageWithTimings} from './utils/timer.js';
import parseLinkHeader from './parse-link-header.js';
import type {PlainResponse, Response} from './response.js';
import type {RequestError} from './errors.js';
import type {Delays} from './timed-out.js';

type StorageAdapter = KeyvStoreAdapter | KeyvType | Map<unknown, unknown>;

type Promisable<T> = T | Promise<T>;

const [major, minor] = process.versions.node.split('.').map(Number) as [number, number, number];

export type DnsLookupIpVersion = undefined | 4 | 6;

type Except<ObjectType, KeysType extends keyof ObjectType> = Pick<ObjectType, Exclude<keyof ObjectType, KeysType>>;

export type NativeRequestOptions = HttpsRequestOptions & CacheOptions & {checkServerIdentity?: CheckServerIdentityFunction};

type AcceptableResponse = IncomingMessageWithTimings | ResponseLike;
type AcceptableRequestResult = Promisable<AcceptableResponse | ClientRequest | undefined>;
export type RequestFunction = (url: URL, options: NativeRequestOptions, callback?: (response: AcceptableResponse) => void) => AcceptableRequestResult;

export type Agents = {
	http?: HttpAgent | false;
	https?: HttpsAgent | false;
	http2?: unknown | false;
};

export type Headers = Record<string, string | string[] | undefined>;

export type ToughCookieJar = {
	getCookieString: ((currentUrl: string, options: Record<string, unknown>, callback: (error: Error | undefined, cookies: string) => void) => void)
		& ((url: string, callback: (error: Error | undefined, cookieHeader: string) => void) => void);
	setCookie: ((cookieOrString: unknown, currentUrl: string, options: Record<string, unknown>, callback: (error: Error | undefined, cookie: unknown) => void) => void)
		& ((rawCookie: string, url: string, callback: (error: Error | undefined, result: unknown) => void) => void);
};

export type PromiseCookieJar = {
	getCookieString: (url: string) => Promise<string>;
	setCookie: (rawCookie: string, url: string) => Promise<unknown>;
};

/**
Utility type to override specific properties in a type.

Uses `Omit` to remove properties before adding them back to ensure proper type replacement rather than intersection, which handles edge cases with optional/required properties correctly.
*/
type OverrideProperties<T, U> = Omit<T, keyof U> & U;

/**
Represents the runtime state of Options as seen by hooks after normalization.

Some Options properties accept multiple input types but are normalized to a single type internally by the Options class setters. This type reflects the actual runtime types that hooks receive, ensuring type safety when accessing options within hook functions.
*/
export type NormalizedOptions = OverrideProperties<Options, {
	// The URL is always normalized to a URL instance (or undefined) by the time hooks execute.
	url: URL | undefined;

	// When set to `true`, dnsCache is normalized to a CacheableLookup instance. When set to `false`, it becomes `undefined`.
	dnsCache: CacheableLookup | undefined;

	// When set to `true`, cache is normalized to the global cache Map. When set to `false`, it becomes `undefined`. Strings and other values are wrapped/processed into a StorageAdapter.
	cache: StorageAdapter | undefined;

	// The prefix URL is always normalized to a string.
	prefixUrl: string;
}>;

export type InitHook = (init: OptionsInit, self: Options) => void;

export type BeforeRequestHookContext = {
	/**
	The current retry count.

	It will be `0` for the initial request and increment for each retry.
	*/
	retryCount: number;
};

export type BeforeRequestHook = (options: NormalizedOptions, context: BeforeRequestHookContext) => Promisable<void | Response | ResponseLike>;
export type BeforeRedirectHook = (updatedOptions: NormalizedOptions, plainResponse: PlainResponse) => Promisable<void>;
export type BeforeErrorHook = (error: RequestError) => Promisable<Error>;
export type BeforeRetryHook = (error: RequestError, retryCount: number) => Promisable<void>;
export type BeforeCacheHook = (response: PlainResponse) => false | void;
export type AfterResponseHook<ResponseType = unknown> = (response: Response<ResponseType>, retryWithMergedOptions: (options: OptionsInit) => never) => Promisable<Response | RequestPromise<Response>>;

/**
All available hooks of Got.
*/
export type Hooks = {
	/**
	Called with the plain request options, right before their normalization.

	The second argument represents the current `Options` instance.

	@default []

	**Note:**
	> - This hook must be synchronous.

	**Note:**
	> - This is called every time options are merged.

	**Note:**
	> - The `options` object may not have the `url` property. To modify it, use a `beforeRequest` hook instead.

	**Note:**
	> - This hook is called when a new instance of `Options` is created.
	> - Do not confuse this with the creation of `Request` or `got(…)`.

	**Note:**
	> - When using `got(url)` or `got(url, undefined, defaults)` this hook will **not** be called.

	This is especially useful in conjunction with `got.extend()` when the input needs custom handling.

	For example, this can be used to fix typos to migrate from older versions faster.

	@example
	```
	import got from 'got';

	const instance = got.extend({
		hooks: {
			init: [
				plain => {
					if ('followRedirects' in plain) {
						plain.followRedirect = plain.followRedirects;
						delete plain.followRedirects;
					}
				}
			]
		}
	});

	// Normally, the following would throw:
	const response = await instance(
		'https://example.com',
		{
			followRedirects: true
		}
	);

	// There is no option named `followRedirects`, but we correct it in an `init` hook.
	```

	Or you can create your own option and store it in a context:

	```
	import got from 'got';

	const instance = got.extend({
		hooks: {
			init: [
				(plain, options) => {
					if ('secret' in plain) {
						options.context.secret = plain.secret;
						delete plain.secret;
					}
				}
			],
			beforeRequest: [
				options => {
					options.headers.secret = options.context.secret;
				}
			]
		}
	});

	const {headers} = await instance(
		'https://httpbin.org/anything',
		{
			secret: 'passphrase'
		}
	).json();

	console.log(headers.Secret);
	//=> 'passphrase'
	```
	*/
	init: InitHook[];

	/**
	Called right before making the request with `options.createNativeRequestOptions()`.

	The second argument is a context object containing request state information.

	This hook is especially useful in conjunction with `got.extend()` when you want to sign your request.

	@default []

	**Note:**
	> - Got will make no further changes to the request before it is sent.

	**Note:**
	> - Changing `options.json` or `options.form` has no effect on the request. You should change `options.body` instead. If needed, update the `options.headers` accordingly.

	@example
	```
	import got from 'got';

	const response = await got.post(
		'https://httpbin.org/anything',
		{
			json: {payload: 'old'},
			hooks: {
				beforeRequest: [
					(options, context) => {
						options.body = JSON.stringify({payload: 'new'});
						options.headers['content-length'] = options.body.length.toString();
					}
				]
			}
		}
	);
	```

	**Example using `context.retryCount`:**

	```
	import got from 'got';

	await got('https://httpbin.org/status/500', {
		retry: {
			limit: 2
		},
		hooks: {
			beforeRequest: [
				(options, context) => {
					// Only log on the initial request, not on retries
					if (context.retryCount === 0) {
						console.log('Making initial request');
					}
				}
			]
		}
	});
	```

	**Tip:**
	> - You can indirectly override the `request` function by early returning a [`ClientRequest`-like](https://nodejs.org/api/http.html#http_class_http_clientrequest) instance or a [`IncomingMessage`-like](https://nodejs.org/api/http.html#http_class_http_incomingmessage) instance. This is very useful when creating a custom cache mechanism.
	> - [Read more about this tip](https://github.com/sindresorhus/got/blob/main/documentation/cache.md#advanced-caching-mechanisms).
	*/
	beforeRequest: BeforeRequestHook[];

	/**
	The equivalent of `beforeRequest` but when redirecting.

	@default []

	**Tip:**
	> - This is especially useful when you want to avoid dead sites.

	@example
	```
	import got from 'got';

	const response = await got('https://example.com', {
		hooks: {
			beforeRedirect: [
				(options, response) => {
					if (options.hostname === 'deadSite') {
						options.hostname = 'fallbackSite';
					}
				}
			]
		}
	});
	```
	*/
	beforeRedirect: BeforeRedirectHook[];

	/**
	Called with a `RequestError` instance. The error is passed to the hook right before it's thrown.

	This hook can return any `Error` instance, allowing you to:
	- Return custom error classes for better error handling in your application
	- Extend `RequestError` with additional properties
	- Return plain `Error` instances when you don't need Got-specific error information

	This is especially useful when you want to have more detailed errors or maintain backward compatibility with existing error handling code.

	@default []

	@example
	```
	import got from 'got';

	// Modify and return the error
	await got('https://api.github.com/repos/sindresorhus/got/commits', {
		responseType: 'json',
		hooks: {
			beforeError: [
				error => {
					const {response} = error;
					if (response && response.body) {
						error.name = 'GitHubError';
						error.message = `${response.body.message} (${response.statusCode})`;
					}

					return error;
				}
			]
		}
	});

	// Return a custom error class
	class CustomAPIError extends Error {
		constructor(message, statusCode) {
			super(message);
			this.name = 'CustomAPIError';
			this.statusCode = statusCode;
		}
	}

	await got('https://api.example.com/endpoint', {
		hooks: {
			beforeError: [
				error => {
					// Return a custom error for backward compatibility with your application
					return new CustomAPIError(
						error.message,
						error.response?.statusCode
					);
				}
			]
		}
	});
	```
	*/
	beforeError: BeforeErrorHook[];

	/**
	The equivalent of `beforeError` but when retrying. Additionally, there is a second argument `retryCount`, the current retry number.

	@default []

	**Note:**
	> - When using the Stream API, this hook is ignored.

	**Note:**
	> - When retrying, the `beforeRequest` hook is called afterwards.

	**Note:**
	> - If no retry occurs, the `beforeError` hook is called instead.

	This hook is especially useful when you want to retrieve the cause of a retry.

	@example
	```
	import got from 'got';

	await got('https://httpbin.org/status/500', {
		hooks: {
			beforeRetry: [
				(error, retryCount) => {
					console.log(`Retrying [${retryCount}]: ${error.code}`);
					// Retrying [1]: ERR_NON_2XX_3XX_RESPONSE
				}
			]
		}
	});
	```
	*/
	beforeRetry: BeforeRetryHook[];

	/**
	Called right before the response is cached. Allows you to control caching behavior by directly modifying the response or preventing caching.

	This is especially useful when you want to prevent caching of specific responses or modify cache headers.

	@default []

	**Return value:**
	> - `false` - Prevent caching (remaining hooks are skipped)
	> - `void`/`undefined` - Use default caching behavior (mutations take effect)

	**Modifying the response:**
	> - Hooks can directly mutate response properties like `headers`, `statusCode`, and `statusMessage`
	> - Mutations to `response.headers` affect how the caching layer decides whether to cache the response and for how long
	> - Changes are applied to what gets cached

	**Note:**
	> - This hook is only called when the `cache` option is enabled.

	**Note:**
	> - This hook must be synchronous. It cannot return a Promise. If you need async logic to determine caching behavior, use a `beforeRequest` hook instead.

	**Note:**
	> - When returning `false`, remaining hooks are skipped and the response will not be cached.

	**Note:**
	> - Returning anything other than `false` or `undefined` will throw a TypeError.

	**Note:**
	> - If a hook throws an error, it will be propagated and the request will fail. This is consistent with how other hooks in Got handle errors.

	**Note:**
	> - At this stage, the response body has not been read yet - it's still a stream. Properties like `response.body` and `response.rawBody` are not available. You can only inspect/modify response headers and status code.

	@example
	```
	import got from 'got';

	// Simple: Don't cache errors
	const instance = got.extend({
		cache: new Map(),
		hooks: {
			beforeCache: [
				(response) => response.statusCode >= 400 ? false : undefined
			]
		}
	});

	// Advanced: Modify headers for fine control
	const instance2 = got.extend({
		cache: new Map(),
		hooks: {
			beforeCache: [
				(response) => {
					// Force caching with explicit duration
					// Mutations work directly - no need to return
					response.headers['cache-control'] = 'public, max-age=3600';
				}
			]
		}
	});

	await instance('https://example.com');
	```
	*/
	beforeCache: BeforeCacheHook[];

	/**
	Each function should return the response. This is especially useful when you want to refresh an access token.

	@default []

	**Note:**
	> - When using the Stream API, this hook is ignored.

	**Note:**
	> - Calling the `retryWithMergedOptions` function will trigger `beforeRetry` hooks. By default, remaining `afterResponse` hooks are removed to prevent duplicate execution. To preserve remaining hooks on retry, set `preserveHooks: true` in the options passed to `retryWithMergedOptions`. In case of an error, `beforeRetry` hooks will be called instead.
	Meanwhile the `init`, `beforeRequest` , `beforeRedirect` as well as already executed `afterResponse` hooks will be skipped.

	**Note:**
	> - To preserve remaining `afterResponse` hooks after calling `retryWithMergedOptions`, set `preserveHooks: true` in the options passed to `retryWithMergedOptions`. This is useful when you want hooks to run on retried requests.

	**Warning:**
	> - Be cautious when using `preserveHooks: true`. If a hook unconditionally calls `retryWithMergedOptions` with `preserveHooks: true`, it will create an infinite retry loop. Always ensure hooks have proper conditional logic to avoid infinite retries.

	@example
	```
	import got from 'got';

	const instance = got.extend({
		hooks: {
			afterResponse: [
				(response, retryWithMergedOptions) => {
					// Unauthorized
					if (response.statusCode === 401) {
						// Refresh the access token
						const updatedOptions = {
							headers: {
								token: getNewToken()
							}
						};

						// Update the defaults
						instance.defaults.options.merge(updatedOptions);

						// Make a new retry
						return retryWithMergedOptions(updatedOptions);
					}

					// No changes otherwise
					return response;
				}
			],
			beforeRetry: [
				error => {
					// This will be called on `retryWithMergedOptions(...)`
				}
			]
		},
		mutableDefaults: true
	});
	```

	@example
	```
	// Example with preserveHooks
	import got from 'got';

	const instance = got.extend({
		hooks: {
			afterResponse: [
				(response, retryWithMergedOptions) => {
					if (response.statusCode === 401) {
						return retryWithMergedOptions({
							headers: {
								authorization: getNewToken()
							},
							preserveHooks: true  // Keep remaining hooks
						});
					}

					return response;
				},
				(response) => {
					// This hook will run on the retried request
					// (the original request is interrupted when the first hook triggers a retry)
					console.log('Response received:', response.statusCode);
					return response;
				}
			]
		}
	});
	```
	*/
	afterResponse: AfterResponseHook[];
};

export type ParseJsonFunction = (text: string) => unknown;
export type StringifyJsonFunction = (object: unknown) => string;

/**
All available HTTP request methods provided by Got.
*/
export type Method =
	| 'GET'
	| 'POST'
	| 'PUT'
	| 'PATCH'
	| 'HEAD'
	| 'DELETE'
	| 'OPTIONS'
	| 'TRACE'
	| 'get'
	| 'post'
	| 'put'
	| 'patch'
	| 'head'
	| 'delete'
	| 'options'
	| 'trace';

export type RetryObject = {
	attemptCount: number;
	retryOptions: RetryOptions;
	error: RequestError;
	computedValue: number;
	retryAfter?: number;
};

export type RetryFunction = (retryObject: RetryObject) => Promisable<number>;

/**
An object representing `limit`, `calculateDelay`, `methods`, `statusCodes`, `maxRetryAfter` and `errorCodes` fields for maximum retry count, retry handler, allowed methods, allowed status codes, maximum [`Retry-After`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After) time and allowed error codes.

Delays between retries counts with function `1000 * Math.pow(2, retry) + Math.random() * 100`, where `retry` is attempt number (starts from 1).

The `calculateDelay` property is a `function` that receives an object with `attemptCount`, `retryOptions`, `error` and `computedValue` properties for current retry count, the retry options, error and default computed value.
The function must return a delay in milliseconds (or a Promise resolving with it) (`0` return value cancels retry).

The `enforceRetryRules` property is a `boolean` that, when set to `true` (default), enforces the `limit`, `methods`, `statusCodes`, and `errorCodes` options before calling `calculateDelay`. Your `calculateDelay` function is only invoked when a retry is allowed based on these criteria. When `false`, `calculateDelay` receives the computed value but can override all retry logic.

__Note:__ When `enforceRetryRules` is `false`, you must check `computedValue` in your `calculateDelay` function to respect retry rules. When `true` (default), the retry rules are enforced automatically.

By default, it retries *only* on the specified methods, status codes, and on these network errors:
- `ETIMEDOUT`: One of the [timeout](#timeout) limits were reached.
- `ECONNRESET`: Connection was forcibly closed by a peer.
- `EADDRINUSE`: Could not bind to any free port.
- `ECONNREFUSED`: Connection was refused by the server.
- `EPIPE`: The remote side of the stream being written has been closed.
- `ENOTFOUND`: Couldn't resolve the hostname to an IP address.
- `ENETUNREACH`: No internet connection.
- `EAI_AGAIN`: DNS lookup timed out.

__Note:__ Got does not retry on `POST` by default.
__Note:__ If `maxRetryAfter` is set to `undefined`, it will use `options.timeout`.
__Note:__ If [`Retry-After`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After) header is greater than `maxRetryAfter`, it will cancel the request.
*/
export type RetryOptions = {
	limit: number;
	methods: Method[];
	statusCodes: number[];
	errorCodes: string[];
	calculateDelay: RetryFunction;
	backoffLimit: number;
	noise: number;
	maxRetryAfter?: number;
	enforceRetryRules?: boolean;
};

export type CreateConnectionFunction = (options: NativeRequestOptions, oncreate: (error: NodeJS.ErrnoException, socket: Socket) => void) => Socket;
export type CheckServerIdentityFunction = (hostname: string, certificate: DetailedPeerCertificate) => NodeJS.ErrnoException | void;

export type CacheOptions = {
	shared?: boolean;
	cacheHeuristic?: number;
	immutableMinTimeToLive?: number;
	ignoreCargoCult?: boolean;
};

type PfxObject = {
	buffer: string | Uint8Array;
	passphrase?: string | undefined;
};

type PfxType = string | Uint8Array | Array<string | Uint8Array | PfxObject> | undefined;

export type HttpsOptions = {
	alpnProtocols?: string[];

	// From `http.RequestOptions` and `tls.CommonConnectionOptions`
	rejectUnauthorized?: NativeRequestOptions['rejectUnauthorized'];

	// From `tls.ConnectionOptions`
	checkServerIdentity?: CheckServerIdentityFunction;

	/**
	Server name for the [Server Name Indication (SNI)](https://en.wikipedia.org/wiki/Server_Name_Indication) TLS extension.

	This is useful when requesting to servers that don't have a proper domain name but use a certificate with a known CN/SAN.

	@example
	```
	import got from 'got';

	// Request to IP address with specific servername for TLS
	await got('https://192.168.1.100', {
		https: {
			serverName: 'example.com'
		}
	});
	```
	*/
	serverName?: string;

	// From `tls.SecureContextOptions`
	/**
	Override the default Certificate Authorities ([from Mozilla](https://ccadb-public.secure.force.com/mozilla/IncludedCACertificateReport)).

	@example
	```
	// Single Certificate Authority
	await got('https://example.com', {
		https: {
			certificateAuthority: fs.readFileSync('./my_ca.pem')
		}
	});
	```
	*/
	certificateAuthority?: SecureContextOptions['ca'];

	/**
	Private keys in [PEM](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail) format.

	[PEM](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail) allows the option of private keys being encrypted.
	Encrypted keys will be decrypted with `options.https.passphrase`.

	Multiple keys with different passphrases can be provided as an array of `{pem: <string | Uint8Array>, passphrase: <string>}`
	*/
	key?: SecureContextOptions['key'];

	/**
	[Certificate chains](https://en.wikipedia.org/wiki/X.509#Certificate_chains_and_cross-certification) in [PEM](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail) format.

	One cert chain should be provided per private key (`options.https.key`).

	When providing multiple cert chains, they do not have to be in the same order as their private keys in `options.https.key`.

	If the intermediate certificates are not provided, the peer will not be able to validate the certificate, and the handshake will fail.
	*/
	certificate?: SecureContextOptions['cert'];

	/**
	The passphrase to decrypt the `options.https.key` (if different keys have different passphrases refer to `options.https.key` documentation).
	*/
	passphrase?: SecureContextOptions['passphrase'];
	pfx?: PfxType;

	ciphers?: SecureContextOptions['ciphers'];
	honorCipherOrder?: SecureContextOptions['honorCipherOrder'];
	minVersion?: SecureContextOptions['minVersion'];
	maxVersion?: SecureContextOptions['maxVersion'];
	signatureAlgorithms?: SecureContextOptions['sigalgs'];
	tlsSessionLifetime?: SecureContextOptions['sessionTimeout'];
	dhparam?: SecureContextOptions['dhparam'];
	ecdhCurve?: SecureContextOptions['ecdhCurve'];
	certificateRevocationLists?: SecureContextOptions['crl'];

	/**
	Optionally affect the OpenSSL protocol behavior, which is not usually necessary. This should be used carefully if at all!

	The value is a numeric bitmask of the `SSL_OP_*` options from OpenSSL.

	For example, to allow connections to legacy servers that do not support secure renegotiation, you can use `crypto.constants.SSL_OP_LEGACY_SERVER_CONNECT`.

	@example
	```
	import crypto from 'node:crypto';
	import got from 'got';

	// Allow connections to servers with legacy renegotiation
	await got('https://legacy-server.com', {
		https: {
			secureOptions: crypto.constants.SSL_OP_LEGACY_SERVER_CONNECT
		}
	});
	```
	*/
	secureOptions?: number;
};

export type PaginateData<BodyType, ElementType> = {
	response: Response<BodyType>;
	currentItems: ElementType[];
	allItems: ElementType[];
};

export type FilterData<ElementType> = {
	item: ElementType;
	currentItems: ElementType[];
	allItems: ElementType[];
};

/**
All options accepted by `got.paginate()`.
*/
export type PaginationOptions<ElementType, BodyType> = {
	/**
	A function that transform [`Response`](#response) into an array of items.
	This is where you should do the parsing.

	@default response => JSON.parse(response.body)
	*/
	transform?: (response: Response<BodyType>) => Promise<ElementType[]> | ElementType[];

	/**
	Checks whether the item should be emitted or not.

	@default ({item, currentItems, allItems}) => true
	*/
	filter?: (data: FilterData<ElementType>) => boolean;

	/**
	The function takes an object with the following properties:
	- `response` - The current response object.
	- `currentItems` - Items from the current response.
	- `allItems` - An empty array, unless `pagination.stackAllItems` is set to `true`, in which case, it's an array of the emitted items.

	It should return an object representing Got options pointing to the next page. The options are merged automatically with the previous request, therefore the options returned `pagination.paginate(...)` must reflect changes only. If there are no more pages, `false` should be returned.

	@example
	```
	import got from 'got';

	const limit = 10;

	const items = got.paginate('https://example.com/items', {
		searchParams: {
			limit,
			offset: 0
		},
		pagination: {
			paginate: ({response, currentItems}) => {
				const previousSearchParams = response.request.options.searchParams;
				const previousOffset = previousSearchParams.get('offset');

				if (currentItems.length < limit) {
					return false;
				}

				return {
					searchParams: {
						...previousSearchParams,
						offset: Number(previousOffset) + limit,
					}
				};
			}
		}
	});

	console.log('Items from all pages:', items);
	```
	*/
	paginate?: (data: PaginateData<BodyType, ElementType>) => OptionsInit | false;

	/**
	Checks whether the pagination should continue.

	For example, if you need to stop **before** emitting an entry with some flag, you should use `({item}) => !item.flag`.

	If you want to stop **after** emitting the entry, you should use
	`({item, allItems}) => allItems.some(item => item.flag)` instead.

	@default ({item, currentItems, allItems}) => true
	*/
	shouldContinue?: (data: FilterData<ElementType>) => boolean;

	/**
	The maximum amount of items that should be emitted.

	@default Infinity
	*/
	countLimit?: number;

	/**
	Milliseconds to wait before the next request is triggered.

	@default 0
	*/
	backoff?: number;

	/**
	The maximum amount of request that should be triggered.
	Retries on failure are not counted towards this limit.

	For example, it can be helpful during development to avoid an infinite number of requests.

	@default 10000
	*/
	requestLimit?: number;

	/**
	Defines how the property `allItems` in `pagination.paginate`, `pagination.filter` and `pagination.shouldContinue` is managed.

	By default, the property `allItems` is always an empty array. This setting can be helpful to save on memory usage when working with a large dataset.

	When set to `true`, the property `allItems` is an array of the emitted items.

	@default false
	*/
	stackAllItems?: boolean;
};

export type SearchParameters = Record<string, string | number | boolean | undefined>;

/**
Generic helper that wraps any assertion function to add context to error messages.
*/
function wrapAssertionWithContext(optionName: string, assertionFn: () => void): void {
	try {
		assertionFn();
	} catch (error) {
		if (error instanceof Error) {
			error.message = `Option '${optionName}': ${error.message}`;
		}

		throw error;
	}
}

/**
Helper function that wraps assert.any() to provide better error messages.
When assertion fails, it includes the option name in the error message.
*/
function assertAny(optionName: string, validators: Array<(value: unknown) => boolean>, value: unknown): void {
	wrapAssertionWithContext(optionName, () => {
		assert.any(validators, value);
	});
}

/**
Helper function that wraps assert.plainObject() to provide better error messages.
When assertion fails, it includes the option name in the error message.
*/
function assertPlainObject(optionName: string, value: unknown): void {
	wrapAssertionWithContext(optionName, () => {
		assert.plainObject(value);
	});
}

function validateSearchParameters(searchParameters: Record<string, unknown>): asserts searchParameters is Record<string, string | number | boolean | undefined> {
	// eslint-disable-next-line guard-for-in
	for (const key in searchParameters) {
		const value = searchParameters[key];
		assertAny(`searchParams.${key}`, [is.string, is.number, is.boolean, is.null, is.undefined], value);
	}
}

/**
All parsing methods supported by Got.
*/
export type ResponseType = 'json' | 'buffer' | 'text';

type OptionsToSkip =
	'searchParameters' |
	'followRedirects' |
	'auth' |
	'toJSON' |
	'merge' |
	'isHeaderExplicitlySet' |
	'shouldCopyPipedHeader' |
	'setPipedHeader' |
	'getInternalHeaders' |
	'setInternalHeader' |
	'deleteInternalHeader' |
	'createNativeRequestOptions' |
	'getRequestFunction' |
	'freeze';

export type InternalsType = Except<Options, OptionsToSkip>;

export type OptionsError = NodeJS.ErrnoException & {options?: Options};

export type OptionsInit =
	Except<Partial<InternalsType>, 'hooks' | 'retry' | 'isStream'>
	& {
		hooks?: Partial<Hooks>;
		retry?: Partial<RetryOptions>;
		preserveHooks?: boolean;
	};

const globalCache = new Map();
let globalDnsCache: CacheableLookup;

const getGlobalDnsCache = (): CacheableLookup => {
	if (globalDnsCache) {
		return globalDnsCache;
	}

	globalDnsCache = new CacheableLookup();
	return globalDnsCache;
};

// Detects and wraps QuickLRU v7+ instances to make them compatible with the StorageAdapter interface
const wrapQuickLruIfNeeded = (value: any): any => {
	// Check if this is QuickLRU v7+ using Symbol.toStringTag and the evict method (added in v7)
	if (value?.[Symbol.toStringTag] === 'QuickLRU' && typeof value.evict === 'function') {
		// QuickLRU v7+ uses set(key, value, {maxAge: number}) but StorageAdapter expects set(key, value, ttl)
		// Wrap it to translate the interface
		return {
			get(key: string) {
				return value.get(key);
			},
			set(key: string, cacheValue: any, ttl?: number) {
				if (ttl === undefined) {
					value.set(key, cacheValue);
				} else {
					value.set(key, cacheValue, {maxAge: ttl});
				}

				return true;
			},
			delete(key: string) {
				return value.delete(key);
			},
			clear() {
				return value.clear();
			},
			has(key: string) {
				return value.has(key);
			},
		};
	}

	// QuickLRU v5 and other caches work as-is
	return value;
};

const defaultInternals: InternalsType = {
	request: undefined,
	agent: {
		http: undefined,
		https: undefined,
		http2: undefined,
	},
	h2session: undefined,
	decompress: true,
	timeout: {
		connect: undefined,
		lookup: undefined,
		read: undefined,
		request: undefined,
		response: undefined,
		secureConnect: undefined,
		send: undefined,
		socket: undefined,
	},
	prefixUrl: '',
	body: undefined,
	form: undefined,
	json: undefined,
	cookieJar: undefined,
	ignoreInvalidCookies: false,
	searchParams: undefined,
	dnsLookup: undefined,
	dnsCache: undefined,
	context: {},
	hooks: {
		init: [],
		beforeRequest: [],
		beforeError: [],
		beforeRedirect: [],
		beforeRetry: [],
		beforeCache: [],
		afterResponse: [],
	},
	followRedirect: true,
	maxRedirects: 10,
	cache: undefined,
	throwHttpErrors: true,
	username: '',
	password: '',
	http2: false,
	allowGetBody: false,
	copyPipedHeaders: false,
	headers: {
		'user-agent': 'got (https://github.com/sindresorhus/got)',
	},
	methodRewriting: false,
	dnsLookupIpVersion: undefined,
	parseJson: JSON.parse,
	stringifyJson: JSON.stringify,
	retry: {
		limit: 2,
		methods: [
			'GET',
			'PUT',
			'HEAD',
			'DELETE',
			'OPTIONS',
			'TRACE',
		],
		statusCodes: [
			408,
			413,
			429,
			500,
			502,
			503,
			504,
			521,
			522,
			524,
		],
		errorCodes: [
			'ETIMEDOUT',
			'ECONNRESET',
			'EADDRINUSE',
			'ECONNREFUSED',
			'EPIPE',
			'ENOTFOUND',
			'ENETUNREACH',
			'EAI_AGAIN',
		],
		maxRetryAfter: undefined,
		calculateDelay: ({computedValue}) => computedValue,
		backoffLimit: Number.POSITIVE_INFINITY,
		noise: 100,
		enforceRetryRules: true,
	},
	localAddress: undefined,
	method: 'GET',
	createConnection: undefined,
	cacheOptions: {
		shared: undefined,
		cacheHeuristic: undefined,
		immutableMinTimeToLive: undefined,
		ignoreCargoCult: undefined,
	},
	https: {
		alpnProtocols: undefined,
		rejectUnauthorized: undefined,
		checkServerIdentity: undefined,
		serverName: undefined,
		certificateAuthority: undefined,
		key: undefined,
		certificate: undefined,
		passphrase: undefined,
		pfx: undefined,
		ciphers: undefined,
		honorCipherOrder: undefined,
		minVersion: undefined,
		maxVersion: undefined,
		signatureAlgorithms: undefined,
		tlsSessionLifetime: undefined,
		dhparam: undefined,
		ecdhCurve: undefined,
		certificateRevocationLists: undefined,
		secureOptions: undefined,
	},
	encoding: undefined,
	resolveBodyOnly: false,
	isStream: false,
	responseType: 'text',
	url: undefined,
	pagination: {
		transform(response: Response) {
			if (response.request.options.responseType === 'json') {
				return response.body;
			}

			return JSON.parse(response.body as string);
		},
		paginate({response}) {
			const rawLinkHeader = response.headers.link;
			if (typeof rawLinkHeader !== 'string' || rawLinkHeader.trim() === '') {
				return false;
			}

			const parsed = parseLinkHeader(rawLinkHeader);
			const next = parsed.find(entry => entry.parameters.rel === 'next' || entry.parameters.rel === '"next"');

			if (next) {
				const baseUrl = response.request.options.url ?? response.url;

				return {
					url: new URL(next.reference, baseUrl),
				};
			}

			return false;
		},
		filter: () => true,
		shouldContinue: () => true,
		countLimit: Number.POSITIVE_INFINITY,
		backoff: 0,
		requestLimit: 10_000,
		stackAllItems: false,
	},
	setHost: true,
	maxHeaderSize: undefined,
	signal: undefined,
	enableUnixSockets: false,
	strictContentLength: true,
};

const cloneInternals = (internals: typeof defaultInternals) => {
	const {hooks, retry} = internals;

	const result: typeof defaultInternals = {
		...internals,
		context: {...internals.context},
		cacheOptions: {...internals.cacheOptions},
		https: {...internals.https},
		agent: {...internals.agent},
		headers: {...internals.headers},
		retry: {
			...retry,
			errorCodes: [...retry.errorCodes!],
			methods: [...retry.methods!],
			statusCodes: [...retry.statusCodes!],
		},
		timeout: {...internals.timeout},
		hooks: {
			init: [...hooks.init],
			beforeRequest: [...hooks.beforeRequest],
			beforeError: [...hooks.beforeError],
			beforeRedirect: [...hooks.beforeRedirect],
			beforeRetry: [...hooks.beforeRetry],
			beforeCache: [...hooks.beforeCache],
			afterResponse: [...hooks.afterResponse],
		},
		searchParams: internals.searchParams ? new URLSearchParams(internals.searchParams as URLSearchParams) : undefined,
		pagination: {...internals.pagination},
	};

	return result;
};

const cloneRaw = (raw: OptionsInit) => {
	const {hooks, retry} = raw;

	const result: OptionsInit = {...raw};

	if (is.object(raw.context)) {
		result.context = {...raw.context};
	}

	if (is.object(raw.cacheOptions)) {
		result.cacheOptions = {...raw.cacheOptions};
	}

	if (is.object(raw.https)) {
		result.https = {...raw.https};
	}

	if (is.object(raw.cacheOptions)) {
		result.cacheOptions = {...result.cacheOptions};
	}

	if (is.object(raw.agent)) {
		result.agent = {...raw.agent};
	}

	if (is.object(raw.headers)) {
		result.headers = {...raw.headers};
	}

	if (is.object(retry)) {
		result.retry = {...retry};

		if (is.array(retry.errorCodes)) {
			result.retry.errorCodes = [...retry.errorCodes];
		}

		if (is.array(retry.methods)) {
			result.retry.methods = [...retry.methods];
		}

		if (is.array(retry.statusCodes)) {
			result.retry.statusCodes = [...retry.statusCodes];
		}
	}

	if (is.object(raw.timeout)) {
		result.timeout = {...raw.timeout};
	}

	if (is.object(hooks)) {
		result.hooks = {
			...hooks,
		};

		if (is.array(hooks.init)) {
			result.hooks.init = [...hooks.init];
		}

		if (is.array(hooks.beforeRequest)) {
			result.hooks.beforeRequest = [...hooks.beforeRequest];
		}

		if (is.array(hooks.beforeError)) {
			result.hooks.beforeError = [...hooks.beforeError];
		}

		if (is.array(hooks.beforeRedirect)) {
			result.hooks.beforeRedirect = [...hooks.beforeRedirect];
		}

		if (is.array(hooks.beforeRetry)) {
			result.hooks.beforeRetry = [...hooks.beforeRetry];
		}

		if (is.array(hooks.beforeCache)) {
			result.hooks.beforeCache = [...hooks.beforeCache];
		}

		if (is.array(hooks.afterResponse)) {
			result.hooks.afterResponse = [...hooks.afterResponse];
		}
	}

	if (raw.searchParams) {
		if (is.string(raw.searchParams)) {
			result.searchParams = raw.searchParams;
		} else if (raw.searchParams instanceof URLSearchParams) {
			result.searchParams = new URLSearchParams(raw.searchParams);
		} else if (is.object(raw.searchParams)) {
			result.searchParams = {...raw.searchParams};
		}
	}

	if (is.object(raw.pagination)) {
		result.pagination = {...raw.pagination};
	}

	return result;
};

const getHttp2TimeoutOption = (internals: typeof defaultInternals): number | undefined => {
	const delays = [internals.timeout.socket, internals.timeout.connect, internals.timeout.lookup, internals.timeout.request, internals.timeout.secureConnect].filter(delay => typeof delay === 'number');

	if (delays.length > 0) {
		return Math.min(...delays);
	}

	return undefined;
};

const init = (options: OptionsInit, withOptions: OptionsInit, self: Options): void => {
	const initHooks = options.hooks?.init;
	if (initHooks) {
		for (const hook of initHooks) {
			hook(withOptions, self);
		}
	}
};

export default class Options {
	#unixOptions?: NativeRequestOptions;
	readonly #internals: InternalsType;
	#headersProxy: Headers;
	#merging = false;
	readonly #init: OptionsInit[];
	readonly #explicitHeaders: Set<string>;

	constructor(input?: string | URL | OptionsInit, options?: OptionsInit, defaults?: Options) {
		assertAny('input', [is.string, is.urlInstance, is.object, is.undefined], input);
		assertAny('options', [is.object, is.undefined], options);
		assertAny('defaults', [is.object, is.undefined], defaults);

		if (input instanceof Options || options instanceof Options) {
			throw new TypeError('The defaults must be passed as the third argument');
		}

		if (defaults) {
			this.#internals = cloneInternals(defaults.#internals);
			this.#init = [...defaults.#init];
			this.#explicitHeaders = new Set(defaults.#explicitHeaders);
		} else {
			this.#internals = cloneInternals(defaultInternals);
			this.#init = [];
			this.#explicitHeaders = new Set();
		}

		this.#headersProxy = this.#createHeadersProxy();

		// This rule allows `finally` to be considered more important.
		// Meaning no matter the error thrown in the `try` block,
		// if `finally` throws then the `finally` error will be thrown.
		//
		// Yes, we want this. If we set `url` first, then the `url.searchParams`
		// would get merged. Instead we set the `searchParams` first, then
		// `url.searchParams` is overwritten as expected.
		//
		/* eslint-disable no-unsafe-finally */
		try {
			if (is.plainObject(input)) {
				try {
					this.merge(input);
					this.merge(options);
				} finally {
					this.url = input.url;
				}
			} else {
				try {
					this.merge(options);
				} finally {
					if (options?.url !== undefined) {
						if (input === undefined) {
							this.url = options.url;
						} else {
							throw new TypeError('The `url` option is mutually exclusive with the `input` argument');
						}
					} else if (input !== undefined) {
						this.url = input;
					}
				}
			}
		} catch (error) {
			(error as OptionsError).options = this;

			throw error;
		}
		/* eslint-enable no-unsafe-finally */
	}

	merge(options?: OptionsInit | Options) {
		if (!options) {
			return;
		}

		if (options instanceof Options) {
			// Create a copy of the #init array to avoid infinite loop
			// when merging an Options instance with itself
			const initArray = [...options.#init];
			for (const init of initArray) {
				this.merge(init);
			}

			return;
		}

		options = cloneRaw(options);

		init(this, options, this);
		init(options, options, this);

		this.#merging = true;

		try {
			let push = false;

			for (const key in options) {
				// `got.extend()` options
				if (key === 'mutableDefaults' || key === 'handlers') {
					continue;
				}

				// Never merge `url`
				if (key === 'url') {
					continue;
				}

				// Never merge `preserveHooks` - it's a control flag, not a persistent option
				if (key === 'preserveHooks') {
					continue;
				}

				// `isStream` is set internally by `got.stream()`, not by user options
				if (key === 'isStream') {
					continue;
				}

				if (!(key in this)) {
					throw new Error(`Unexpected option: ${key}`);
				}

				// @ts-expect-error Type 'unknown' is not assignable to type 'never'.
				const value = options[key as keyof Options];
				if (value === undefined) {
					continue;
				}

				// @ts-expect-error Type 'unknown' is not assignable to type 'never'.
				this[key as keyof Options] = value;

				push = true;
			}

			if (push) {
				this.#init.push(options);
			}
		} finally {
			this.#merging = false;
		}
	}

	/**
	Custom request function.
	The main purpose of this is to [support HTTP2 using a wrapper](https://github.com/szmarczak/http2-wrapper).

	@default http.request | https.request
	*/
	get request(): RequestFunction | undefined {
		return this.#internals.request;
	}

	set request(value: RequestFunction | undefined) {
		assertAny('request', [is.function, is.undefined], value);

		this.#internals.request = value;
	}

	/**
	An object representing `http`, `https` and `http2` keys for [`http.Agent`](https://nodejs.org/api/http.html#http_class_http_agent), [`https.Agent`](https://nodejs.org/api/https.html#https_class_https_agent) and [`http2wrapper.Agent`](https://github.com/szmarczak/http2-wrapper#new-http2agentoptions) instance.
	This is necessary because a request to one protocol might redirect to another.
	In such a scenario, Got will switch over to the right protocol agent for you.

	If a key is not present, it will default to a global agent.

	@example
	```
	import got from 'got';
	import HttpAgent from 'agentkeepalive';

	const {HttpsAgent} = HttpAgent;

	await got('https://sindresorhus.com', {
		agent: {
			http: new HttpAgent(),
			https: new HttpsAgent()
		}
	});
	```
	*/
	get agent(): Agents {
		return this.#internals.agent;
	}

	set agent(value: Agents) {
		assertPlainObject('agent', value);

		// eslint-disable-next-line guard-for-in
		for (const key in value) {
			if (!(key in this.#internals.agent)) {
				throw new TypeError(`Unexpected agent option: ${key}`);
			}

			// @ts-expect-error - No idea why `value[key]` doesn't work here.
			assertAny(`agent.${key}`, [is.object, is.undefined, (v: unknown) => v === false], value[key]);
		}

		if (this.#merging) {
			Object.assign(this.#internals.agent, value);
		} else {
			this.#internals.agent = {...value};
		}
	}

	get h2session(): ClientHttp2Session | undefined {
		return this.#internals.h2session;
	}

	set h2session(value: ClientHttp2Session | undefined) {
		this.#internals.h2session = value;
	}

	/**
	Decompress the response automatically.

	This will set the `accept-encoding` header to `gzip, deflate, br` unless you set it yourself.

	If this is disabled, a compressed response is returned as a `Uint8Array`.
	This may be useful if you want to handle decompression yourself or stream the raw compressed data.

	@default true
	*/
	get decompress(): boolean {
		return this.#internals.decompress;
	}

	set decompress(value: boolean) {
		assert.boolean(value);

		this.#internals.decompress = value;
	}

	/**
	Milliseconds to wait for the server to end the response before aborting the request with `got.TimeoutError` error (a.k.a. `request` property).
	By default, there's no timeout.

	This also accepts an `object` with the following fields to constrain the duration of each phase of the request lifecycle:

	- `lookup` starts when a socket is assigned and ends when the hostname has been resolved.
		Does not apply when using a Unix domain socket.
	- `connect` starts when `lookup` completes (or when the socket is assigned if lookup does not apply to the request) and ends when the socket is connected.
	- `secureConnect` starts when `connect` completes and ends when the handshaking process completes (HTTPS only).
	- `socket` starts when the socket is connected. See [request.setTimeout](https://nodejs.org/api/http.html#http_request_settimeout_timeout_callback).
	- `response` starts when the request has been written to the socket and ends when the response headers are received.
	- `send` starts when the socket is connected and ends with the request has been written to the socket.
	- `request` starts when the request is initiated and ends when the response's end event fires.
	*/
	get timeout(): Delays {
		// We always return `Delays` here.
		// It has to be `Delays | number`, otherwise TypeScript will error because the getter and the setter have incompatible types.
		return this.#internals.timeout;
	}

	set timeout(value: Delays) {
		assertPlainObject('timeout', value);

		// eslint-disable-next-line guard-for-in
		for (const key in value) {
			if (!(key in this.#internals.timeout)) {
				throw new Error(`Unexpected timeout option: ${key}`);
			}

			// @ts-expect-error - No idea why `value[key]` doesn't work here.
			assertAny(`timeout.${key}`, [is.number, is.undefined], value[key]);
		}

		if (this.#merging) {
			Object.assign(this.#internals.timeout, value);
		} else {
			this.#internals.timeout = {...value};
		}
	}

	/**
	When specified, `prefixUrl` will be prepended to `url`.
	The prefix can be any valid URL, either relative or absolute.
	A trailing slash `/` is optional - one will be added automatically.

	__Note__: `prefixUrl` will be ignored if the `url` argument is a URL instance.

	__Note__: Leading slashes in `input` are disallowed when using this option to enforce consistency and avoid confusion.
	For example, when the prefix URL is `https://example.com/foo` and the input is `/bar`, there's ambiguity whether the resulting URL would become `https://example.com/foo/bar` or `https://example.com/bar`.
	The latter is used by browsers.

	__Tip__: Useful when used with `got.extend()` to create niche-specific Got instances.

	__Tip__: You can change `prefixUrl` using hooks as long as the URL still includes the `prefixUrl`.
	If the URL doesn't include it anymore, it will throw.

	@example
	```
	import got from 'got';

	await got('unicorn', {prefixUrl: 'https://cats.com'});
	//=> 'https://cats.com/unicorn'

	const instance = got.extend({
		prefixUrl: 'https://google.com'
	});

	await instance('unicorn', {
		hooks: {
			beforeRequest: [
				options => {
					options.prefixUrl = 'https://cats.com';
				}
			]
		}
	});
	//=> 'https://cats.com/unicorn'
	```
	*/
	get prefixUrl(): string | URL {
		// We always return `string` here.
		// It has to be `string | URL`, otherwise TypeScript will error because the getter and the setter have incompatible types.
		return this.#internals.prefixUrl;
	}

	set prefixUrl(value: string | URL) {
		assertAny('prefixUrl', [is.string, is.urlInstance], value);

		if (value === '') {
			this.#internals.prefixUrl = '';
			return;
		}

		value = value.toString();

		if (!value.endsWith('/')) {
			value += '/';
		}

		if (this.#internals.prefixUrl && this.#internals.url) {
			const {href} = this.#internals.url as URL;

			(this.#internals.url as URL).href = value + href.slice((this.#internals.prefixUrl as string).length);
		}

		this.#internals.prefixUrl = value;
	}

	/**
	__Note #1__: The `body` option cannot be used with the `json` or `form` option.

	__Note #2__: If you provide this option, `got.stream()` will be read-only.

	__Note #3__: If you provide a payload with the `GET` or `HEAD` method, it will throw a `TypeError` unless the method is `GET` and the `allowGetBody` option is set to `true`.

	__Note #4__: This option is not enumerable and will not be merged with the instance defaults.

	The `content-length` header will be automatically set if `body` is a `string` / `Uint8Array` / typed array, and `content-length` and `transfer-encoding` are not manually set in `options.headers`.

	Since Got 12, the `content-length` is not automatically set when `body` is a `fs.createReadStream`.

	You can use `Iterable` and `AsyncIterable` objects as request body, including Web [`ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream):

	@example
	```
	import got from 'got';

	// Using an async generator
	async function* generateData() {
		yield 'Hello, ';
		yield 'world!';
	}

	await got.post('https://httpbin.org/anything', {
		body: generateData()
	});
	```
	*/
	get body(): string | Uint8Array | Readable | Generator | AsyncGenerator | Iterable<unknown> | AsyncIterable<unknown> | FormData | ArrayBufferView | undefined {
		return this.#internals.body;
	}

	set body(value: string | Uint8Array | Readable | Generator | AsyncGenerator | Iterable<unknown> | AsyncIterable<unknown> | FormData | ArrayBufferView | undefined) {
		assertAny('body', [is.string, is.buffer, is.nodeStream, is.generator, is.asyncGenerator, is.iterable, is.asyncIterable, is.typedArray, is.undefined], value);

		if (is.nodeStream(value)) {
			assert.truthy(value.readable);
		}

		if (value !== undefined) {
			assert.undefined(this.#internals.form);
			assert.undefined(this.#internals.json);
		}

		this.#internals.body = value;
	}

	/**
	The form body is converted to a query string using [`(new URLSearchParams(object)).toString()`](https://nodejs.org/api/url.html#url_constructor_new_urlsearchparams_obj).

	If the `Content-Type` header is not present, it will be set to `application/x-www-form-urlencoded`.

	__Note #1__: If you provide this option, `got.stream()` will be read-only.

	__Note #2__: This option is not enumerable and will not be merged with the instance defaults.
	*/
	get form(): Record<string, any> | undefined {
		return this.#internals.form;
	}

	set form(value: Record<string, any> | undefined) {
		assertAny('form', [is.plainObject, is.undefined], value);

		if (value !== undefined) {
			assert.undefined(this.#internals.body);
			assert.undefined(this.#internals.json);
		}

		this.#internals.form = value;
	}

	/**
	JSON request body. If the `content-type` header is not set, it will be set to `application/json`.

	__Important__: This option only affects the request body you send to the server. To parse the response as JSON, you must either call `.json()` on the promise or set `responseType: 'json'` in the options.

	__Note #1__: If you provide this option, `got.stream()` will be read-only.

	__Note #2__: This option is not enumerable and will not be merged with the instance defaults.
	*/
	get json(): unknown {
		return this.#internals.json;
	}

	set json(value: unknown) {
		if (value !== undefined) {
			assert.undefined(this.#internals.body);
			assert.undefined(this.#internals.form);
		}

		this.#internals.json = value;
	}

	/**
	The URL to request, as a string, a [`https.request` options object](https://nodejs.org/api/https.html#https_https_request_options_callback), or a [WHATWG `URL`](https://nodejs.org/api/url.html#url_class_url).

	Properties from `options` will override properties in the parsed `url`.

	If no protocol is specified, it will throw a `TypeError`.

	__Note__: The query string is **not** parsed as search params.

	@example
	```
	await got('https://example.com/?query=a b'); //=> https://example.com/?query=a%20b
	await got('https://example.com/', {searchParams: {query: 'a b'}}); //=> https://example.com/?query=a+b

	// The query string is overridden by `searchParams`
	await got('https://example.com/?query=a b', {searchParams: {query: 'a b'}}); //=> https://example.com/?query=a+b
	```
	*/
	get url(): string | URL | undefined {
		return this.#internals.url;
	}

	set url(value: string | URL | undefined) {
		assertAny('url', [is.string, is.urlInstance, is.undefined], value);

		if (value === undefined) {
			this.#internals.url = undefined;
			return;
		}

		if (is.string(value) && value.startsWith('/')) {
			throw new Error('`url` must not start with a slash');
		}

		// Detect if URL is already absolute (has a protocol/scheme)
		const valueString = value.toString();
		const isAbsolute = is.urlInstance(value) || /^[a-z][a-z\d+.-]*:\/\//i.test(valueString);

		// Only concatenate prefixUrl if the URL is relative
		const urlString = isAbsolute ? valueString : `${this.prefixUrl as string}${valueString}`;
		const url = new URL(urlString);
		this.#internals.url = url;

		if (url.protocol === 'unix:') {
			url.href = `http://unix${url.pathname}${url.search}`;
		}

		if (url.protocol !== 'http:' && url.protocol !== 'https:') {
			const error: NodeJS.ErrnoException = new Error(`Unsupported protocol: ${url.protocol}`);
			error.code = 'ERR_UNSUPPORTED_PROTOCOL';

			throw error;
		}

		if (this.#internals.username) {
			url.username = this.#internals.username;
			this.#internals.username = '';
		}

		if (this.#internals.password) {
			url.password = this.#internals.password;
			this.#internals.password = '';
		}

		if (this.#internals.searchParams) {
			url.search = (this.#internals.searchParams as URLSearchParams).toString();
			this.#internals.searchParams = undefined;
		}

		if (url.hostname === 'unix') {
			if (!this.#internals.enableUnixSockets) {
				throw new Error('Using UNIX domain sockets but option `enableUnixSockets` is not enabled');
			}

			const matches = /(?<socketPath>.+?):(?<path>.+)/.exec(`${url.pathname}${url.search}`);

			if (matches?.groups) {
				const {socketPath, path} = matches.groups;

				this.#unixOptions = {
					socketPath,
					path,
					host: '',
				};
			} else {
				this.#unixOptions = undefined;
			}

			return;
		}

		this.#unixOptions = undefined;
	}

	/**
	Cookie support. You don't have to care about parsing or how to store them.

	__Note__: If you provide this option, `options.headers.cookie` will be overridden.
	*/
	get cookieJar(): PromiseCookieJar | ToughCookieJar | undefined {
		return this.#internals.cookieJar;
	}

	set cookieJar(value: PromiseCookieJar | ToughCookieJar | undefined) {
		assertAny('cookieJar', [is.object, is.undefined], value);

		if (value === undefined) {
			this.#internals.cookieJar = undefined;
			return;
		}

		let {setCookie, getCookieString} = value;

		assert.function(setCookie);
		assert.function(getCookieString);

		/* istanbul ignore next: Horrible `tough-cookie` v3 check */
		if (setCookie.length === 4 && getCookieString.length === 0) {
			setCookie = promisify(setCookie.bind(value));
			getCookieString = promisify(getCookieString.bind(value));

			this.#internals.cookieJar = {
				setCookie,
				getCookieString: getCookieString as PromiseCookieJar['getCookieString'],
			};
		} else {
			this.#internals.cookieJar = value;
		}
	}

	/**
	You can abort the `request` using [`AbortController`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController).

	@example
	```
	import got from 'got';

	const abortController = new AbortController();

	const request = got('https://httpbin.org/anything', {
		signal: abortController.signal
	});

	setTimeout(() => {
		abortController.abort();
	}, 100);
	```
	*/
	get signal(): AbortSignal | undefined {
		return this.#internals.signal;
	}

	set signal(value: AbortSignal | undefined) {
		assertAny('signal', [is.object, is.undefined], value);

		this.#internals.signal = value;
	}

	/**
	Ignore invalid cookies instead of throwing an error.
	Only useful when the `cookieJar` option has been set. Not recommended.

	@default false
	*/
	get ignoreInvalidCookies(): boolean {
		return this.#internals.ignoreInvalidCookies;
	}

	set ignoreInvalidCookies(value: boolean) {
		assert.boolean(value);

		this.#internals.ignoreInvalidCookies = value;
	}

	/**
	Query string that will be added to the request URL.
	This will override the query string in `url`.

	If you need to pass in an array, you can do it using a `URLSearchParams` instance.

	@example
	```
	import got from 'got';

	const searchParams = new URLSearchParams([['key', 'a'], ['key', 'b']]);

	await got('https://example.com', {searchParams});

	console.log(searchParams.toString());
	//=> 'key=a&key=b'
	```
	*/
	get searchParams(): string | SearchParameters | URLSearchParams | undefined {
		if (this.#internals.url) {
			return (this.#internals.url as URL).searchParams;
		}

		this.#internals.searchParams ??= new URLSearchParams();

		return this.#internals.searchParams;
	}

	set searchParams(value: string | SearchParameters | URLSearchParams | undefined) {
		assertAny('searchParams', [is.string, is.object, is.undefined], value);

		const url = this.#internals.url as URL;

		if (value === undefined) {
			this.#internals.searchParams = undefined;

			if (url) {
				url.search = '';
			}

			return;
		}

		const searchParameters = this.searchParams as URLSearchParams;
		let updated;

		if (is.string(value)) {
			updated = new URLSearchParams(value);
		} else if (value instanceof URLSearchParams) {
			updated = value;
		} else {
			validateSearchParameters(value);

			updated = new URLSearchParams();

			// eslint-disable-next-line guard-for-in
			for (const key in value) {
				const entry = value[key];

				if (entry === null) {
					updated.append(key, '');
				} else if (entry === undefined) {
					searchParameters.delete(key);
				} else {
					updated.append(key, entry as string);
				}
			}
		}

		if (this.#merging) {
			// These keys will be replaced
			for (const key of updated.keys()) {
				searchParameters.delete(key);
			}

			for (const [key, value] of updated) {
				searchParameters.append(key, value);
			}
		} else if (url) {
			url.search = searchParameters.toString();
		} else {
			this.#internals.searchParams = searchParameters;
		}
	}

	get searchParameters() {
		throw new Error('The `searchParameters` option does not exist. Use `searchParams` instead.');
	}

	set searchParameters(_value: unknown) {
		throw new Error('The `searchParameters` option does not exist. Use `searchParams` instead.');
	}

	get dnsLookup(): LookupFunction | undefined {
		return this.#internals.dnsLookup;
	}

	set dnsLookup(value: LookupFunction | undefined) {
		assertAny('dnsLookup', [is.function, is.undefined], value);

		this.#internals.dnsLookup = value;
	}

	/**
	An instance of [`CacheableLookup`](https://github.com/szmarczak/cacheable-lookup) used for making DNS lookups.
	Useful when making lots of requests to different *public* hostnames.

	`CacheableLookup` uses `dns.resolver4(..)` and `dns.resolver6(...)` under the hood and fall backs to `dns.lookup(...)` when the first two fail, which may lead to additional delay.

	__Note__: This should stay disabled when making requests to internal hostnames such as `localhost`, `database.local` etc.

	@default false
	*/
	get dnsCache(): CacheableLookup | boolean | undefined {
		return this.#internals.dnsCache;
	}

	set dnsCache(value: CacheableLookup | boolean | undefined) {
		assertAny('dnsCache', [is.object, is.boolean, is.undefined], value);

		if (value === true) {
			this.#internals.dnsCache = getGlobalDnsCache();
		} else if (value === false) {
			this.#internals.dnsCache = undefined;
		} else {
			this.#internals.dnsCache = value;
		}
	}

	/**
	User data. `context` is shallow merged and enumerable. If it contains non-enumerable properties they will NOT be merged.

	@example
	```
	import got from 'got';

	const instance = got.extend({
		hooks: {
			beforeRequest: [
				options => {
					if (!options.context || !options.context.token) {
						throw new Error('Token required');
					}

					options.headers.token = options.context.token;
				}
			]
		}
	});

	const context = {
		token: 'secret'
	};

	const response = await instance('https://httpbin.org/headers', {context});

	// Let's see the headers
	console.log(response.body);
	```
	*/
	get context(): Record<string, unknown> {
		return this.#internals.context;
	}

	set context(value: Record<string, unknown>) {
		assert.object(value);

		if (this.#merging) {
			Object.assign(this.#internals.context, value);
		} else {
			this.#internals.context = {...value};
		}
	}

	/**
	Hooks allow modifications during the request lifecycle.
	Hook functions may be async and are run serially.
	*/
	get hooks(): Hooks {
		return this.#internals.hooks;
	}

	set hooks(value: Hooks) {
		assert.object(value);

		// eslint-disable-next-line guard-for-in
		for (const knownHookEvent in value) {
			if (!(knownHookEvent in this.#internals.hooks)) {
				throw new Error(`Unexpected hook event: ${knownHookEvent}`);
			}

			const typedKnownHookEvent = knownHookEvent as keyof Hooks;
			const hooks = value[typedKnownHookEvent];

			assertAny(`hooks.${knownHookEvent}`, [is.array, is.undefined], hooks);

			if (hooks) {
				for (const hook of hooks) {
					assert.function(hook);
				}
			}

			if (this.#merging) {
				if (hooks) {
					// @ts-expect-error FIXME
					this.#internals.hooks[typedKnownHookEvent].push(...hooks);
				}
			} else {
				if (!hooks) {
					throw new Error(`Missing hook event: ${knownHookEvent}`);
				}

				// @ts-expect-error FIXME
				this.#internals.hooks[knownHookEvent] = [...hooks];
			}
		}
	}

	/**
	Whether redirect responses should be followed automatically.

 	Optionally, pass a function to dynamically decide based on the response object.

	Note that if a `303` is sent by the server in response to any request type (`POST`, `DELETE`, etc.), Got will automatically request the resource pointed to in the location header via `GET`.
	This is in accordance with [the spec](https://tools.ietf.org/html/rfc7231#section-6.4.4). You can optionally turn on this behavior also for other redirect codes - see `methodRewriting`.

	@default true
	*/
	get followRedirect(): boolean | ((response: PlainResponse) => boolean) {
		return this.#internals.followRedirect;
	}

	set followRedirect(value: boolean | ((response: PlainResponse) => boolean)) {
		assertAny('followRedirect', [is.boolean, is.function], value);

		this.#internals.followRedirect = value;
	}

	get followRedirects() {
		throw new TypeError('The `followRedirects` option does not exist. Use `followRedirect` instead.');
	}

	set followRedirects(_value: unknown) {
		throw new TypeError('The `followRedirects` option does not exist. Use `followRedirect` instead.');
	}

	/**
	If exceeded, the request will be aborted and a `MaxRedirectsError` will be thrown.

	@default 10
	*/
	get maxRedirects(): number {
		return this.#internals.maxRedirects;
	}

	set maxRedirects(value: number) {
		assert.number(value);

		this.#internals.maxRedirects = value;
	}

	/**
	A cache adapter instance for storing cached response data.

	@default false
	*/
	get cache(): string | StorageAdapter | boolean | undefined {
		return this.#internals.cache;
	}

	set cache(value: string | StorageAdapter | boolean | undefined) {
		assertAny('cache', [is.object, is.string, is.boolean, is.undefined], value);

		if (value === true) {
			this.#internals.cache = globalCache;
		} else if (value === false) {
			this.#internals.cache = undefined;
		} else {
			this.#internals.cache = wrapQuickLruIfNeeded(value);
		}
	}

	/**
	Determines if a `got.HTTPError` is thrown for unsuccessful responses.

	If this is disabled, requests that encounter an error status code will be resolved with the `response` instead of throwing.
	This may be useful if you are checking for resource availability and are expecting error responses.

	@default true
	*/
	get throwHttpErrors(): boolean {
		return this.#internals.throwHttpErrors;
	}

	set throwHttpErrors(value: boolean) {
		assert.boolean(value);

		this.#internals.throwHttpErrors = value;
	}

	get username(): string {
		const url = this.#internals.url as URL;

		const value = url ? url.username : this.#internals.username;

		return decodeURIComponent(value);
	}

	set username(value: string) {
		assert.string(value);

		const url = this.#internals.url as URL;
		const fixedValue = encodeURIComponent(value);

		if (url) {
			url.username = fixedValue;
		} else {
			this.#internals.username = fixedValue;
		}
	}

	get password(): string {
		const url = this.#internals.url as URL;

		const value = url ? url.password : this.#internals.password;

		return decodeURIComponent(value);
	}

	set password(value: string) {
		assert.string(value);

		const url = this.#internals.url as URL;

		const fixedValue = encodeURIComponent(value);

		if (url) {
			url.password = fixedValue;
		} else {
			this.#internals.password = fixedValue;
		}
	}

	/**
	If set to `true`, Got will additionally accept HTTP2 requests.

	It will choose either HTTP/1.1 or HTTP/2 depending on the ALPN protocol.

	__Note__: This option requires Node.js 15.10.0 or newer as HTTP/2 support on older Node.js versions is very buggy.

	__Note__: Overriding `options.request` will disable HTTP2 support.

	@default false

	@example
	```
	import got from 'got';

	const {headers} = await got('https://nghttp2.org/httpbin/anything', {http2: true});

	console.log(headers.via);
	//=> '2 nghttpx'
	```
	*/
	get http2(): boolean {
		return this.#internals.http2;
	}

	set http2(value: boolean) {
		assert.boolean(value);

		this.#internals.http2 = value;
	}

	/**
	Set this to `true` to allow sending body for the `GET` method.
	However, the [HTTP/2 specification](https://tools.ietf.org/html/rfc7540#section-8.1.3) says that `An HTTP GET request includes request header fields and no payload body`, therefore when using the HTTP/2 protocol this option will have no effect.
	This option is only meant to interact with non-compliant servers when you have no other choice.

	__Note__: The [RFC 7231](https://tools.ietf.org/html/rfc7231#section-4.3.1) doesn't specify any particular behavior for the GET method having a payload, therefore __it's considered an [anti-pattern](https://en.wikipedia.org/wiki/Anti-pattern)__.

	@default false
	*/
	get allowGetBody(): boolean {
		return this.#internals.allowGetBody;
	}

	set allowGetBody(value: boolean) {
		assert.boolean(value);

		this.#internals.allowGetBody = value;
	}

	/**
	Automatically copy headers from piped streams.

	When piping a request into a Got stream (e.g., `request.pipe(got.stream(url))`), this controls whether headers from the source stream are automatically merged into the Got request headers.

	Note: Explicitly set headers take precedence over piped headers. Piped headers are only copied when a header is not already explicitly set.

	Useful for proxy scenarios when explicitly enabled, but you may still want to filter out headers like `Host`, `Connection`, `Authorization`, etc.

	@default false

	@example
	```
	import got from 'got';
	import {pipeline} from 'node:stream/promises';

	// Opt in to automatic header copying for proxy scenarios
	server.get('/proxy', async (request, response) => {
		const gotStream = got.stream('https://example.com', {
			copyPipedHeaders: true,
			// Explicit headers win over piped headers
			headers: {
				host: 'example.com',
			}
		});

		await pipeline(request, gotStream, response);
	});
	```

	@example
	```
	import got from 'got';
	import {pipeline} from 'node:stream/promises';

	// Keep it disabled and manually copy only safe headers
	server.get('/proxy', async (request, response) => {
		const gotStream = got.stream('https://example.com', {
			headers: {
				'user-agent': request.headers['user-agent'],
				'accept': request.headers['accept'],
				// Explicitly NOT copying host, connection, authorization, etc.
			}
		});

		await pipeline(request, gotStream, response);
	});
	```
	*/
	get copyPipedHeaders(): boolean {
		return this.#internals.copyPipedHeaders;
	}

	set copyPipedHeaders(value: boolean) {
		assert.boolean(value);

		this.#internals.copyPipedHeaders = value;
	}

	isHeaderExplicitlySet(name: string): boolean {
		return this.#explicitHeaders.has(name.toLowerCase());
	}

	shouldCopyPipedHeader(name: string): boolean {
		const normalizedHeader = name.toLowerCase();

		if (this.isHeaderExplicitlySet(normalizedHeader)) {
			return false;
		}

		return true;
	}

	setPipedHeader(name: string, value: string | string[] | undefined): void {
		this.#internals.headers[name.toLowerCase()] = value;
	}

	getInternalHeaders(): Headers {
		return this.#internals.headers;
	}

	setInternalHeader(name: string, value: string | string[] | undefined): void {
		this.#internals.headers[name.toLowerCase()] = value;
	}

	deleteInternalHeader(name: string): void {
		// eslint-disable-next-line @typescript-eslint/no-dynamic-delete
		delete this.#internals.headers[name.toLowerCase()];
	}

	/**
	Request headers.

	Existing headers will be overwritten. Headers set to `undefined` will be omitted.

	@default {}
	*/
	get headers(): Headers {
		return this.#headersProxy;
	}

	set headers(value: Headers) {
		assertPlainObject('headers', value);
		const normalizedHeaders = lowercaseKeys(value);

		if (this.#merging) {
			Object.assign(this.#internals.headers, normalizedHeaders);
		} else {
			this.#internals.headers = normalizedHeaders;
			this.#headersProxy = this.#createHeadersProxy();
			this.#explicitHeaders.clear();
		}

		for (const header of Object.keys(normalizedHeaders)) {
			this.#explicitHeaders.add(header);
		}
	}

	/**
	Specifies if the HTTP request method should be [rewritten as `GET`](https://tools.ietf.org/html/rfc7231#section-6.4) on redirects.

	As the [specification](https://tools.ietf.org/html/rfc7231#section-6.4) prefers to rewrite the HTTP method only on `303` responses, this is Got's default behavior.
	Setting `methodRewriting` to `true` will also rewrite `301` and `302` responses, as allowed by the spec. This is the behavior followed by `curl` and browsers.

	__Note__: Got never performs method rewriting on `307` and `308` responses, as this is [explicitly prohibited by the specification](https://www.rfc-editor.org/rfc/rfc7231#section-6.4.7).

	@default false
	*/
	get methodRewriting(): boolean {
		return this.#internals.methodRewriting;
	}

	set methodRewriting(value: boolean) {
		assert.boolean(value);

		this.#internals.methodRewriting = value;
	}

	/**
	Indicates which DNS record family to use.

	Values:
	- `undefined`: IPv4 (if present) or IPv6
	- `4`: Only IPv4
	- `6`: Only IPv6

	@default undefined
	*/
	get dnsLookupIpVersion(): DnsLookupIpVersion {
		return this.#internals.dnsLookupIpVersion;
	}

	set dnsLookupIpVersion(value: DnsLookupIpVersion) {
		if (value !== undefined && value !== 4 && value !== 6) {
			throw new TypeError(`Invalid DNS lookup IP version: ${value as string}`);
		}

		this.#internals.dnsLookupIpVersion = value;
	}

	/**
	A function used to parse JSON responses.

	@example
	```
	import got from 'got';
	import Bourne from '@hapi/bourne';

	const parsed = await got('https://example.com', {
		parseJson: text => Bourne.parse(text)
	}).json();

	console.log(parsed);
	```
	*/
	get parseJson(): ParseJsonFunction {
		return this.#internals.parseJson;
	}

	set parseJson(value: ParseJsonFunction) {
		assert.function(value);

		this.#internals.parseJson = value;
	}

	/**
	A function used to stringify the body of JSON requests.

	@example
	```
	import got from 'got';

	await got.post('https://example.com', {
		stringifyJson: object => JSON.stringify(object, (key, value) => {
			if (key.startsWith('_')) {
				return;
			}

			return value;
		}),
		json: {
			some: 'payload',
			_ignoreMe: 1234
		}
	});
	```

	@example
	```
	import got from 'got';

	await got.post('https://example.com', {
		stringifyJson: object => JSON.stringify(object, (key, value) => {
			if (typeof value === 'number') {
				return value.toString();
			}

			return value;
		}),
		json: {
			some: 'payload',
			number: 1
		}
	});
	```
	*/
	get stringifyJson(): StringifyJsonFunction {
		return this.#internals.stringifyJson;
	}

	set stringifyJson(value: StringifyJsonFunction) {
		assert.function(value);

		this.#internals.stringifyJson = value;
	}

	/**
	An object representing `limit`, `calculateDelay`, `methods`, `statusCodes`, `maxRetryAfter` and `errorCodes` fields for maximum retry count, retry handler, allowed methods, allowed status codes, maximum [`Retry-After`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After) time and allowed error codes.

	Delays between retries counts with function `1000 * Math.pow(2, retry) + Math.random() * 100`, where `retry` is attempt number (starts from 1).

	The `calculateDelay` property is a `function` that receives an object with `attemptCount`, `retryOptions`, `error` and `computedValue` properties for current retry count, the retry options, error and default computed value.
	The function must return a delay in milliseconds (or a Promise resolving with it) (`0` return value cancels retry).

	The `enforceRetryRules` property is a `boolean` that, when set to `true` (default), enforces the `limit`, `methods`, `statusCodes`, and `errorCodes` options before calling `calculateDelay`. Your `calculateDelay` function is only invoked when a retry is allowed based on these criteria. When `false`, `calculateDelay` receives the computed value but can override all retry logic.

	__Note:__ When `enforceRetryRules` is `false`, you must check `computedValue` in your `calculateDelay` function to respect retry rules. When `true` (default), the retry rules are enforced automatically.

	By default, it retries *only* on the specified methods, status codes, and on these network errors:

	- `ETIMEDOUT`: One of the [timeout](#timeout) limits were reached.
	- `ECONNRESET`: Connection was forcibly closed by a peer.
	- `EADDRINUSE`: Could not bind to any free port.
	- `ECONNREFUSED`: Connection was refused by the server.
	- `EPIPE`: The remote side of the stream being written has been closed.
	- `ENOTFOUND`: Couldn't resolve the hostname to an IP address.
	- `ENETUNREACH`: No internet connection.
	- `EAI_AGAIN`: DNS lookup timed out.

	__Note__: If `maxRetryAfter` is set to `undefined`, it will use `options.timeout`.
	__Note__: If [`Retry-After`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After) header is greater than `maxRetryAfter`, it will cancel the request.
	*/
	get retry(): Partial<RetryOptions> {
		return this.#internals.retry;
	}

	set retry(value: Partial<RetryOptions>) {
		assertPlainObject('retry', value);

		assertAny('retry.calculateDelay', [is.function, is.undefined], value.calculateDelay);
		assertAny('retry.maxRetryAfter', [is.number, is.undefined], value.maxRetryAfter);
		assertAny('retry.limit', [is.number, is.undefined], value.limit);
		assertAny('retry.methods', [is.array, is.undefined], value.methods);
		assertAny('retry.statusCodes', [is.array, is.undefined], value.statusCodes);
		assertAny('retry.errorCodes', [is.array, is.undefined], value.errorCodes);
		assertAny('retry.noise', [is.number, is.undefined], value.noise);
		assertAny('retry.enforceRetryRules', [is.boolean, is.undefined], value.enforceRetryRules);

		if (value.noise && Math.abs(value.noise) > 100) {
			throw new Error(`The maximum acceptable retry noise is +/- 100ms, got ${value.noise}`);
		}

		for (const key in value) {
			if (!(key in this.#internals.retry)) {
				throw new Error(`Unexpected retry option: ${key}`);
			}
		}

		if (this.#merging) {
			Object.assign(this.#internals.retry, value);
		} else {
			this.#internals.retry = {...value};
		}

		const {retry} = this.#internals;

		retry.methods = [...new Set(retry.methods!.map(method => method.toUpperCase() as Method))];
		retry.statusCodes = [...new Set(retry.statusCodes)];
		retry.errorCodes = [...new Set(retry.errorCodes)];
	}

	/**
	From `http.RequestOptions`.

	The IP address used to send the request from.
	*/
	get localAddress(): string | undefined {
		return this.#internals.localAddress;
	}

	set localAddress(value: string | undefined) {
		assertAny('localAddress', [is.string, is.undefined], value);

		this.#internals.localAddress = value;
	}

	/**
	The HTTP method used to make the request.

	@default 'GET'
	*/
	get method(): Method {
		return this.#internals.method;
	}

	set method(value: Method) {
		assert.string(value);

		this.#internals.method = value.toUpperCase() as Method;
	}

	get createConnection(): CreateConnectionFunction | undefined {
		return this.#internals.createConnection;
	}

	set createConnection(value: CreateConnectionFunction | undefined) {
		assertAny('createConnection', [is.function, is.undefined], value);

		this.#internals.createConnection = value;
	}

	/**
	From `http-cache-semantics`

	@default {}
	*/
	get cacheOptions(): CacheOptions {
		return this.#internals.cacheOptions;
	}

	set cacheOptions(value: CacheOptions) {
		assertPlainObject('cacheOptions', value);

		assertAny('cacheOptions.shared', [is.boolean, is.undefined], value.shared);
		assertAny('cacheOptions.cacheHeuristic', [is.number, is.undefined], value.cacheHeuristic);
		assertAny('cacheOptions.immutableMinTimeToLive', [is.number, is.undefined], value.immutableMinTimeToLive);
		assertAny('cacheOptions.ignoreCargoCult', [is.boolean, is.undefined], value.ignoreCargoCult);

		for (const key in value) {
			if (!(key in this.#internals.cacheOptions)) {
				throw new Error(`Cache option \`${key}\` does not exist`);
			}
		}

		if (this.#merging) {
			Object.assign(this.#internals.cacheOptions, value);
		} else {
			this.#internals.cacheOptions = {...value};
		}
	}

	/**
	Options for the advanced HTTPS API.
	*/
	get https(): HttpsOptions {
		return this.#internals.https;
	}

	set https(value: HttpsOptions) {
		assertPlainObject('https', value);

		assertAny('https.rejectUnauthorized', [is.boolean, is.undefined], value.rejectUnauthorized);
		assertAny('https.checkServerIdentity', [is.function, is.undefined], value.checkServerIdentity);
		assertAny('https.serverName', [is.string, is.undefined], value.serverName);
		assertAny('https.certificateAuthority', [is.string, is.object, is.array, is.undefined], value.certificateAuthority);
		assertAny('https.key', [is.string, is.object, is.array, is.undefined], value.key);
		assertAny('https.certificate', [is.string, is.object, is.array, is.undefined], value.certificate);
		assertAny('https.passphrase', [is.string, is.undefined], value.passphrase);
		assertAny('https.pfx', [is.string, is.buffer, is.array, is.undefined], value.pfx);
		assertAny('https.alpnProtocols', [is.array, is.undefined], value.alpnProtocols);
		assertAny('https.ciphers', [is.string, is.undefined], value.ciphers);
		assertAny('https.dhparam', [is.string, is.buffer, is.undefined], value.dhparam);
		assertAny('https.signatureAlgorithms', [is.string, is.undefined], value.signatureAlgorithms);
		assertAny('https.minVersion', [is.string, is.undefined], value.minVersion);
		assertAny('https.maxVersion', [is.string, is.undefined], value.maxVersion);
		assertAny('https.honorCipherOrder', [is.boolean, is.undefined], value.honorCipherOrder);
		assertAny('https.tlsSessionLifetime', [is.number, is.undefined], value.tlsSessionLifetime);
		assertAny('https.ecdhCurve', [is.string, is.undefined], value.ecdhCurve);
		assertAny('https.certificateRevocationLists', [is.string, is.buffer, is.array, is.undefined], value.certificateRevocationLists);
		assertAny('https.secureOptions', [is.number, is.undefined], value.secureOptions);

		for (const key in value) {
			if (!(key in this.#internals.https)) {
				throw new Error(`HTTPS option \`${key}\` does not exist`);
			}
		}

		if (this.#merging) {
			Object.assign(this.#internals.https, value);
		} else {
			this.#internals.https = {...value};
		}
	}

	/**
	[Encoding](https://nodejs.org/api/buffer.html#buffer_buffers_and_character_encodings) to be used on `setEncoding` of the response data.

	To get a [`Uint8Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array), you need to set `responseType` to `buffer` instead.
	Don't set this option to `null`.

	__Note__: This doesn't affect streams! Instead, you need to do `got.stream(...).setEncoding(encoding)`.

	@default 'utf-8'
	*/
	get encoding(): BufferEncoding | undefined {
		return this.#internals.encoding;
	}

	set encoding(value: BufferEncoding | undefined) {
		if (value === null) {
			throw new TypeError('To get a Uint8Array, set `options.responseType` to `buffer` instead');
		}

		assertAny('encoding', [is.string, is.undefined], value);

		this.#internals.encoding = value;
	}

	/**
	When set to `true` the promise will return the Response body instead of the Response object.

	@default false
	*/
	get resolveBodyOnly(): boolean {
		return this.#internals.resolveBodyOnly;
	}

	set resolveBodyOnly(value: boolean) {
		assert.boolean(value);

		this.#internals.resolveBodyOnly = value;
	}

	/**
	@internal
	Returns a `Stream` instead of a `Promise`.
	Set internally by `got.stream()`.

	@default false
	*/
	get isStream(): boolean {
		return this.#internals.isStream;
	}

	set isStream(value: boolean) {
		assert.boolean(value);

		this.#internals.isStream = value;
	}

	/**
	The parsing method.

	The promise also has `.text()`, `.json()` and `.buffer()` methods which return another Got promise for the parsed body.

	It's like setting the options to `{responseType: 'json', resolveBodyOnly: true}` but without affecting the main Got promise.

	__Note__: When using streams, this option is ignored.

	@example
	```
	const responsePromise = got(url);
	const bufferPromise = responsePromise.buffer();
	const jsonPromise = responsePromise.json();

	const [response, buffer, json] = Promise.all([responsePromise, bufferPromise, jsonPromise]);
	// `response` is an instance of Got Response
	// `buffer` is an instance of Uint8Array
	// `json` is an object
	```

	@example
	```
	// This
	const body = await got(url).json();

	// is semantically the same as this
	const body = await got(url, {responseType: 'json', resolveBodyOnly: true});
	```
	*/
	get responseType(): ResponseType {
		return this.#internals.responseType;
	}

	set responseType(value: ResponseType) {
		if (value === undefined) {
			this.#internals.responseType = 'text';
			return;
		}

		if (value !== 'text' && value !== 'buffer' && value !== 'json') {
			throw new Error(`Invalid \`responseType\` option: ${value as string}`);
		}

		this.#internals.responseType = value;
	}

	get pagination(): PaginationOptions<unknown, unknown> {
		return this.#internals.pagination;
	}

	set pagination(value: PaginationOptions<unknown, unknown>) {
		assert.object(value);

		if (this.#merging) {
			Object.assign(this.#internals.pagination, value);
		} else {
			this.#internals.pagination = value;
		}
	}

	get auth() {
		throw new Error('Parameter `auth` is deprecated. Use `username` / `password` instead.');
	}

	set auth(_value: unknown) {
		throw new Error('Parameter `auth` is deprecated. Use `username` / `password` instead.');
	}

	get setHost() {
		return this.#internals.setHost;
	}

	set setHost(value: boolean) {
		assert.boolean(value);

		this.#internals.setHost = value;
	}

	get maxHeaderSize() {
		return this.#internals.maxHeaderSize;
	}

	set maxHeaderSize(value: number | undefined) {
		assertAny('maxHeaderSize', [is.number, is.undefined], value);

		this.#internals.maxHeaderSize = value;
	}

	get enableUnixSockets() {
		return this.#internals.enableUnixSockets;
	}

	set enableUnixSockets(value: boolean) {
		assert.boolean(value);

		this.#internals.enableUnixSockets = value;
	}

	/**
	Throw an error if the server response's `content-length` header value doesn't match the number of bytes received.

	This is useful for detecting truncated responses and follows RFC 9112 requirements for message completeness.

	__Note__: Responses without a `content-length` header are not validated.
	__Note__: When enabled and validation fails, a `ReadError` with code `ERR_HTTP_CONTENT_LENGTH_MISMATCH` will be thrown.

	@default true
	*/
	get strictContentLength() {
		return this.#internals.strictContentLength;
	}

	set strictContentLength(value: boolean) {
		assert.boolean(value);

		this.#internals.strictContentLength = value;
	}

	// eslint-disable-next-line @typescript-eslint/naming-convention
	toJSON() {
		return {...this.#internals};
	}

	[Symbol.for('nodejs.util.inspect.custom')](_depth: number, options: InspectOptions) {
		return inspect(this.#internals, options);
	}

	createNativeRequestOptions() {
		const internals = this.#internals;
		const url = internals.url as URL;

		let agent;
		if (url.protocol === 'https:') {
			if (internals.http2) {
				// Ensure HTTP/2 agent is configured for connection reuse
				// If no custom agent.http2 is provided, use the global agent for connection pooling
				agent = {
					...internals.agent,
					http2: internals.agent.http2 ?? http2wrapper.globalAgent,
				};
			} else {
				agent = internals.agent.https;
			}
		} else {
			agent = internals.agent.http;
		}

		const {https} = internals;
		let {pfx} = https;

		if (is.array(pfx) && is.plainObject(pfx[0])) {
			pfx = (pfx as PfxObject[]).map(object => ({
				buf: object.buffer,
				passphrase: object.passphrase,
			})) as any;
		}

		return {
			...internals.cacheOptions,
			...this.#unixOptions,

			// HTTPS options
			// eslint-disable-next-line @typescript-eslint/naming-convention
			ALPNProtocols: https.alpnProtocols,
			ca: https.certificateAuthority,
			cert: https.certificate,
			key: https.key,
			passphrase: https.passphrase,
			pfx,
			rejectUnauthorized: https.rejectUnauthorized,
			checkServerIdentity: https.checkServerIdentity ?? checkServerIdentity,
			servername: https.serverName,
			ciphers: https.ciphers,
			honorCipherOrder: https.honorCipherOrder,
			minVersion: https.minVersion,
			maxVersion: https.maxVersion,
			sigalgs: https.signatureAlgorithms,
			sessionTimeout: https.tlsSessionLifetime,
			dhparam: https.dhparam,
			ecdhCurve: https.ecdhCurve,
			crl: https.certificateRevocationLists,
			secureOptions: https.secureOptions,

			// HTTP options
			lookup: internals.dnsLookup ?? (internals.dnsCache as CacheableLookup | undefined)?.lookup,
			family: internals.dnsLookupIpVersion,
			agent,
			setHost: internals.setHost,
			method: internals.method,
			maxHeaderSize: internals.maxHeaderSize,
			localAddress: internals.localAddress,
			headers: internals.headers,
			createConnection: internals.createConnection,
			timeout: internals.http2 ? getHttp2TimeoutOption(internals) : undefined,

			// HTTP/2 options
			h2session: internals.h2session,
		};
	}

	getRequestFunction() {
		const {request: customRequest} = this.#internals;

		if (!customRequest) {
			return this.#getFallbackRequestFunction();
		}

		const requestWithFallback: RequestFunction = (url, options, callback?) => {
			const result = customRequest(url, options, callback);

			if (is.promise(result)) {
				return this.#resolveRequestWithFallback(result, url, options, callback);
			}

			if (result !== undefined) {
				return result;
			}

			return this.#callFallbackRequest(url, options, callback);
		};

		return requestWithFallback;
	}

	freeze() {
		const options = this.#internals;

		Object.freeze(options);
		Object.freeze(options.hooks);
		Object.freeze(options.hooks.afterResponse);
		Object.freeze(options.hooks.beforeError);
		Object.freeze(options.hooks.beforeRedirect);
		Object.freeze(options.hooks.beforeRequest);
		Object.freeze(options.hooks.beforeRetry);
		Object.freeze(options.hooks.init);
		Object.freeze(options.https);
		Object.freeze(options.cacheOptions);
		Object.freeze(options.agent);
		Object.freeze(options.headers);
		Object.freeze(options.timeout);
		Object.freeze(options.retry);
		Object.freeze(options.retry.errorCodes);
		Object.freeze(options.retry.methods);
		Object.freeze(options.retry.statusCodes);
	}

	#createHeadersProxy(): Headers {
		return new Proxy(this.#internals.headers, {
			get(target, property, receiver): unknown {
				if (typeof property === 'string') {
					if (Reflect.has(target, property)) {
						return Reflect.get(target, property, receiver);
					}

					const normalizedProperty = property.toLowerCase();
					return Reflect.get(target, normalizedProperty, receiver);
				}

				return Reflect.get(target, property, receiver);
			},
			set: (target, property, value): boolean => {
				if (typeof property === 'string') {
					const normalizedProperty = property.toLowerCase();
					const isSuccess = Reflect.set(target, normalizedProperty, value);

					if (isSuccess) {
						this.#explicitHeaders.add(normalizedProperty);
					}

					return isSuccess;
				}

				return Reflect.set(target, property, value);
			},
			deleteProperty: (target, property): boolean => {
				if (typeof property === 'string') {
					const normalizedProperty = property.toLowerCase();
					const isSuccess = Reflect.deleteProperty(target, normalizedProperty);

					if (isSuccess) {
						this.#explicitHeaders.delete(normalizedProperty);
					}

					return isSuccess;
				}

				return Reflect.deleteProperty(target, property);
			},
		});
	}

	#getFallbackRequestFunction() {
		const url = this.#internals.url as (URL | undefined);

		if (!url) {
			return;
		}

		if (url.protocol === 'https:') {
			if (this.#internals.http2) {
				if (major < 15 || (major === 15 && minor < 10)) {
					const error = new Error('To use the `http2` option, install Node.js 15.10.0 or above');
					(error as NodeJS.ErrnoException).code = 'EUNSUPPORTED';

					throw error;
				}

				return http2wrapper.auto as RequestFunction;
			}

			return https.request;
		}

		return http.request;
	}

	#callFallbackRequest(
		url: URL,
		options: NativeRequestOptions,
		callback?: (response: AcceptableResponse) => void,
	): AcceptableResponse | ClientRequest | Promise<AcceptableResponse | ClientRequest> {
		const fallbackRequest = this.#getFallbackRequestFunction();

		if (!fallbackRequest) {
			throw new TypeError('The request function must return a value');
		}

		const fallbackResult = fallbackRequest(url, options, callback);

		if (fallbackResult === undefined) {
			throw new TypeError('The request function must return a value');
		}

		if (is.promise(fallbackResult)) {
			return this.#resolveFallbackRequestResult(fallbackResult);
		}

		return fallbackResult;
	}

	async #resolveRequestWithFallback(
		requestResult: Promise<AcceptableResponse | ClientRequest | undefined>,
		url: URL,
		options: NativeRequestOptions,
		callback?: (response: AcceptableResponse) => void,
	): Promise<AcceptableResponse | ClientRequest> {
		const result = await requestResult;

		if (result !== undefined) {
			return result;
		}

		return this.#callFallbackRequest(url, options, callback);
	}

	async #resolveFallbackRequestResult(fallbackResult: Promise<AcceptableResponse | ClientRequest | undefined>): Promise<AcceptableResponse | ClientRequest> {
		const resolvedFallbackResult = await fallbackResult;

		if (resolvedFallbackResult === undefined) {
			throw new TypeError('The request function must return a value');
		}

		return resolvedFallbackResult;
	}
}
```

## File: `source/core/parse-link-header.ts`
```typescript
export default function parseLinkHeader(link: string) {
	const parsed = [];

	const items = link.split(',');

	for (const item of items) {
		// https://tools.ietf.org/html/rfc5988#section-5
		const [rawUriReference, ...rawLinkParameters] = item.split(';') as [string, ...string[]];
		const trimmedUriReference = rawUriReference.trim();

		// eslint-disable-next-line @typescript-eslint/prefer-string-starts-ends-with
		if (trimmedUriReference[0] !== '<' || trimmedUriReference.at(-1) !== '>') {
			throw new Error(`Invalid format of the Link header reference: ${trimmedUriReference}`);
		}

		const reference = trimmedUriReference.slice(1, -1);
		const parameters: Record<string, string> = {};

		if (rawLinkParameters.length === 0) {
			throw new Error(`Unexpected end of Link header parameters: ${rawLinkParameters.join(';')}`);
		}

		for (const rawParameter of rawLinkParameters) {
			const trimmedRawParameter = rawParameter.trim();
			const center = trimmedRawParameter.indexOf('=');

			if (center === -1) {
				throw new Error(`Failed to parse Link header: ${link}`);
			}

			const name = trimmedRawParameter.slice(0, center).trim();
			const value = trimmedRawParameter.slice(center + 1).trim();

			parameters[name] = value;
		}

		parsed.push({
			reference,
			parameters,
		});
	}

	return parsed;
}
```

## File: `source/core/response.ts`
```typescript
import {Buffer} from 'node:buffer';
import type {IncomingMessageWithTimings, Timings} from './utils/timer.js';
import {RequestError} from './errors.js';
import stripUrlAuth from './utils/strip-url-auth.js';
import type {ParseJsonFunction, ResponseType} from './options.js';
import type Request from './index.js';

const decodedBodyCache = new WeakMap<PlainResponse, string>();

export type PlainResponse = {
	/**
	The original request URL.
	*/
	requestUrl: URL;

	/**
	The redirect URLs.
	*/
	redirectUrls: URL[];

	/**
	- `options` - The Got options that were set on this request.

	__Note__: This is not a [http.ClientRequest](https://nodejs.org/api/http.html#http_class_http_clientrequest).
	*/
	request: Request;

	/**
	The remote IP address.

	This is hopefully a temporary limitation, see [lukechilds/cacheable-request#86](https://web.archive.org/web/20220804165050/https://github.com/jaredwray/cacheable-request/issues/86).

	__Note__: Not available when the response is cached.
	*/
	ip?: string;

	/**
	Whether the response was retrieved from the cache.
	*/
	isFromCache: boolean;

	/**
	The status code of the response.
	*/
	statusCode: number;

	/**
	The request URL or the final URL after redirects.
	*/
	url: string;

	/**
	The object contains the following properties:

	- `start` - Time when the request started.
	- `socket` - Time when a socket was assigned to the request.
	- `lookup` - Time when the DNS lookup finished.
	- `connect` - Time when the socket successfully connected.
	- `secureConnect` - Time when the socket securely connected.
	- `upload` - Time when the request finished uploading.
	- `response` - Time when the request fired `response` event.
	- `end` - Time when the response fired `end` event.
	- `error` - Time when the request fired `error` event.
	- `abort` - Time when the request fired `abort` event.
	- `phases`
		- `wait` - `timings.socket - timings.start`
		- `dns` - `timings.lookup - timings.socket`
		- `tcp` - `timings.connect - timings.lookup`
		- `tls` - `timings.secureConnect - timings.connect`
		- `request` - `timings.upload - (timings.secureConnect || timings.connect)`
		- `firstByte` - `timings.response - timings.upload`
		- `download` - `timings.end - timings.response`
		- `total` - `(timings.end || timings.error || timings.abort) - timings.start`

	If something has not been measured yet, it will be `undefined`.

	__Note__: The time is a `number` representing the milliseconds elapsed since the UNIX epoch.
	*/
	timings: Timings;

	/**
	The number of times the request was retried.
	*/
	retryCount: number;

	// Defined only if request errored
	/**
	The raw result of the request.
	*/
	rawBody?: Uint8Array;

	/**
	The result of the request.
	*/
	body?: unknown;

	/**
	Whether the response was successful.

	__Note__: Got throws automatically when `response.ok` is `false` and `throwHttpErrors` is `true`.
	*/
	ok: boolean;
} & IncomingMessageWithTimings;

// For Promise support
export type Response<T = unknown> = {
	/**
	The result of the request.
	*/
	body: T;

	/**
	The raw result of the request.
	*/
	rawBody: Uint8Array;
} & PlainResponse;

export const isResponseOk = (response: PlainResponse): boolean => {
	const {statusCode} = response;
	const {followRedirect} = response.request.options;
	const shouldFollow = typeof followRedirect === 'function' ? followRedirect(response) : followRedirect;
	const limitStatusCode = shouldFollow ? 299 : 399;

	return (statusCode >= 200 && statusCode <= limitStatusCode) || statusCode === 304;
};

/**
An error to be thrown when server response code is 2xx, and parsing body fails.
Includes a `response` property.
*/
export class ParseError extends RequestError {
	override name = 'ParseError';
	override code = 'ERR_BODY_PARSE_FAILURE';
	declare readonly response: Response;

	constructor(error: Error, response: Response) {
		const {options} = response.request;
		super(`${error.message} in "${stripUrlAuth(options.url!)}"`, error, response.request);
	}
}

export const cacheDecodedBody = (response: PlainResponse, decodedBody: string): void => {
	decodedBodyCache.set(response, decodedBody);
};

export const parseBody = (response: Response, responseType: ResponseType, parseJson: ParseJsonFunction, encoding?: BufferEncoding): unknown => {
	const {rawBody} = response;
	const cachedDecodedBody = decodedBodyCache.get(response);

	try {
		if (responseType === 'text') {
			if (cachedDecodedBody !== undefined) {
				return cachedDecodedBody;
			}

			return Buffer.from(rawBody).toString(encoding);
		}

		if (responseType === 'json') {
			if (rawBody.length === 0) {
				return '';
			}

			const text = cachedDecodedBody ?? Buffer.from(rawBody).toString(encoding);
			return parseJson(text);
		}

		if (responseType === 'buffer') {
			return rawBody;
		}
	} catch (error) {
		throw new ParseError(error as Error, response);
	}

	throw new ParseError({
		message: `Unknown body type '${responseType as string}'`,
		name: 'Error',
	}, response);
};
```

## File: `source/core/timed-out.ts`
```typescript
import net from 'node:net';
import type {ClientRequest, IncomingMessage} from 'node:http';
import unhandler from './utils/unhandle.js';

const reentry: unique symbol = Symbol('reentry');
const noop = (): void => {};

type TimedOutOptions = {
	host?: string;
	hostname?: string;
	protocol?: string;
};

export type Delays = {
	lookup?: number;
	socket?: number;
	connect?: number;
	secureConnect?: number;
	send?: number;
	response?: number;
	read?: number;
	request?: number;
};

export type ErrorCode =
	| 'ETIMEDOUT'
	| 'ECONNRESET'
	| 'EADDRINUSE'
	| 'ECONNREFUSED'
	| 'EPIPE'
	| 'ENOTFOUND'
	| 'ENETUNREACH'
	| 'EAI_AGAIN';

export class TimeoutError extends Error {
	override name = 'TimeoutError';
	code: ErrorCode = 'ETIMEDOUT';
	event: string;

	constructor(threshold: number, event: string) {
		super(`Timeout awaiting '${event}' for ${threshold}ms`);
		this.event = event;
	}
}

export default function timedOut(request: ClientRequest, delays: Delays, options: TimedOutOptions): () => void {
	if (reentry in request) {
		return noop;
	}

	request[reentry] = true;
	const cancelers: Array<typeof noop> = [];
	const {once, unhandleAll} = unhandler();
	const handled: Map<string, boolean> = new Map<string, boolean>();

	const addTimeout = (delay: number, callback: (delay: number, event: string) => void, event: string): (typeof noop) => {
		const timeout = setTimeout(callback, delay, delay, event) as unknown as NodeJS.Timeout;

		timeout.unref?.();

		const cancel = (): void => {
			handled.set(event, true);
			clearTimeout(timeout);
		};

		cancelers.push(cancel);

		return cancel;
	};

	const {host, hostname} = options;

	const timeoutHandler = (delay: number, event: string): void => {
		// Use setTimeout to allow for any cancelled events to be handled first,
		// to prevent firing any TimeoutError unneeded when the event loop is busy or blocked
		setTimeout(() => {
			if (!handled.has(event)) {
				request.destroy(new TimeoutError(delay, event));
			}
		}, 0);
	};

	const cancelTimeouts = (): void => {
		for (const cancel of cancelers) {
			cancel();
		}

		unhandleAll();
	};

	request.once('error', error => {
		cancelTimeouts();

		// Save original behavior
		/* istanbul ignore next */
		if (request.listenerCount('error') === 0) {
			throw error;
		}
	});

	if (delays.request !== undefined) {
		const cancelTimeout = addTimeout(delays.request, timeoutHandler, 'request');

		once(request, 'response', (response: IncomingMessage): void => {
			once(response, 'end', cancelTimeout);
		});
	}

	if (delays.socket !== undefined) {
		const {socket} = delays;

		const socketTimeoutHandler = (): void => {
			timeoutHandler(socket, 'socket');
		};

		request.setTimeout(socket, socketTimeoutHandler);

		// `request.setTimeout(0)` causes a memory leak.
		// We can just remove the listener and forget about the timer - it's unreffed.
		// See https://github.com/sindresorhus/got/issues/690
		cancelers.push(() => {
			request.removeListener('timeout', socketTimeoutHandler);
		});
	}

	const hasLookup = delays.lookup !== undefined;
	const hasConnect = delays.connect !== undefined;
	const hasSecureConnect = delays.secureConnect !== undefined;
	const hasSend = delays.send !== undefined;
	if (hasLookup || hasConnect || hasSecureConnect || hasSend) {
		once(request, 'socket', (socket: net.Socket): void => {
			const {socketPath} = request as ClientRequest & {socketPath?: string};

			/* istanbul ignore next: hard to test */
			if (socket.connecting) {
				const hasPath = Boolean(socketPath ?? net.isIP(hostname ?? host ?? '') !== 0);

				if (hasLookup && !hasPath && (socket.address() as net.AddressInfo).address === undefined) {
					const cancelTimeout = addTimeout(delays.lookup!, timeoutHandler, 'lookup');
					once(socket, 'lookup', cancelTimeout);
				}

				if (hasConnect) {
					const timeConnect = (): (() => void) => addTimeout(delays.connect!, timeoutHandler, 'connect');

					if (hasPath) {
						once(socket, 'connect', timeConnect());
					} else {
						once(socket, 'lookup', (error: Error): void => {
							if (error === null) {
								once(socket, 'connect', timeConnect());
							}
						});
					}
				}

				if (hasSecureConnect && options.protocol === 'https:') {
					once(socket, 'connect', (): void => {
						const cancelTimeout = addTimeout(delays.secureConnect!, timeoutHandler, 'secureConnect');
						once(socket, 'secureConnect', cancelTimeout);
					});
				}
			}

			if (hasSend) {
				const timeRequest = (): (() => void) => addTimeout(delays.send!, timeoutHandler, 'send');
				/* istanbul ignore next: hard to test */
				if (socket.connecting) {
					once(socket, 'connect', (): void => {
						once(request, 'upload-complete', timeRequest());
					});
				} else {
					once(request, 'upload-complete', timeRequest());
				}
			}
		});
	}

	if (delays.response !== undefined) {
		once(request, 'upload-complete', (): void => {
			const cancelTimeout = addTimeout(delays.response!, timeoutHandler, 'response');
			once(request, 'response', cancelTimeout);
		});
	}

	if (delays.read !== undefined) {
		once(request, 'response', (response: IncomingMessage): void => {
			const cancelTimeout = addTimeout(delays.read!, timeoutHandler, 'read');
			once(response, 'end', cancelTimeout);
		});
	}

	return cancelTimeouts;
}

declare module 'http' {
	// eslint-disable-next-line @typescript-eslint/consistent-type-definitions -- This has to be an `interface` to be able to be merged.
	interface ClientRequest {
		[reentry]?: boolean;
	}
}
```

## File: `source/core/utils/defer-to-connect.ts`
```typescript
import type {Socket} from 'node:net';
import type {TLSSocket} from 'node:tls';

type Listeners = {
	connect?: () => void;
	secureConnect?: () => void;
	close?: (hadError: boolean) => void;
};

function isTlsSocket(socket: Socket | TLSSocket): socket is TLSSocket {
	return 'encrypted' in socket;
}

const deferToConnect = (socket: TLSSocket | Socket, fn: Listeners | (() => void)): void => {
	let listeners: Listeners;
	if (typeof fn === 'function') {
		const connect = fn;
		listeners = {connect};
	} else {
		listeners = fn;
	}

	const hasConnectListener = typeof listeners.connect === 'function';
	const hasSecureConnectListener = typeof listeners.secureConnect === 'function';
	const hasCloseListener = typeof listeners.close === 'function';

	const onConnect = () => {
		if (hasConnectListener) {
			listeners.connect!();
		}

		if (isTlsSocket(socket) && hasSecureConnectListener) {
			if (socket.authorized) {
				listeners.secureConnect!();
			} else {
				// Wait for secureConnect event (even if authorization fails, we need the timing)
				socket.once('secureConnect', listeners.secureConnect!);
			}
		}

		if (hasCloseListener) {
			socket.once('close', listeners.close!);
		}
	};

	if (socket.writable && !socket.connecting) {
		onConnect();
	} else if (socket.connecting) {
		socket.once('connect', onConnect);
	} else if (socket.destroyed && hasCloseListener) {
		const hadError = '_hadError' in socket ? Boolean((socket as any)._hadError) : false;
		listeners.close!(hadError);
	}
};

export default deferToConnect;
```

## File: `source/core/utils/get-body-size.ts`
```typescript
import type {ClientRequestArgs} from 'node:http';
import is from '@sindresorhus/is';

export default function getBodySize(body: unknown, headers: ClientRequestArgs['headers']): number | undefined {
	if (headers && 'content-length' in headers) {
		return Number(headers['content-length']);
	}

	if (!body) {
		return 0;
	}

	if (is.string(body)) {
		return new TextEncoder().encode(body).byteLength;
	}

	if (is.buffer(body)) {
		return body.length;
	}

	if (is.typedArray(body)) {
		return (body as ArrayBufferView).byteLength;
	}

	return undefined;
}
```

## File: `source/core/utils/is-client-request.ts`
```typescript
import type {Writable, Readable} from 'node:stream';
import type {ClientRequest} from 'node:http';

function isClientRequest(clientRequest: Writable | Readable): clientRequest is ClientRequest {
	return (clientRequest as Writable).writable && !(clientRequest as Writable).writableEnded;
}

export default isClientRequest;
```

## File: `source/core/utils/is-unix-socket-url.ts`
```typescript
// eslint-disable-next-line @typescript-eslint/naming-convention
export default function isUnixSocketURL(url: URL) {
	return url.protocol === 'unix:' || url.hostname === 'unix';
}

/**
Extract the socket path from a UNIX socket URL.

@example
```
getUnixSocketPath(new URL('http://unix/foo:/path'));
//=> '/foo'

getUnixSocketPath(new URL('unix:/foo:/path'));
//=> '/foo'

getUnixSocketPath(new URL('http://example.com'));
//=> undefined
```
*/
export function getUnixSocketPath(url: URL): string | undefined {
	if (!isUnixSocketURL(url)) {
		return undefined;
	}

	return /(?<socketPath>.+?):(?<path>.+)/.exec(`${url.pathname}${url.search}`)?.groups?.socketPath;
}
```

## File: `source/core/utils/options-to-url.ts`
```typescript
// eslint-disable-next-line @typescript-eslint/naming-convention
export type URLOptions = {
	href?: string;
	protocol?: string;
	host?: string;
	hostname?: string;
	port?: string | number;
	pathname?: string;
	search?: string;
	searchParams?: unknown;
	path?: string;
};

const keys: Array<Exclude<keyof URLOptions, 'searchParams' | 'path'>> = [
	'protocol',
	'host',
	'hostname',
	'port',
	'pathname',
	'search',
];

export default function optionsToUrl(origin: string, options: URLOptions): URL {
	if (options.path) {
		if (options.pathname) {
			throw new TypeError('Parameters `path` and `pathname` are mutually exclusive.');
		}

		if (options.search) {
			throw new TypeError('Parameters `path` and `search` are mutually exclusive.');
		}

		if (options.searchParams) {
			throw new TypeError('Parameters `path` and `searchParams` are mutually exclusive.');
		}
	}

	if (options.search && options.searchParams) {
		throw new TypeError('Parameters `search` and `searchParams` are mutually exclusive.');
	}

	if (!origin) {
		if (!options.protocol) {
			throw new TypeError('No URL protocol specified');
		}

		origin = `${options.protocol}//${options.hostname ?? options.host ?? ''}`;
	}

	const url = new URL(origin);

	if (options.path) {
		const searchIndex = options.path.indexOf('?');
		if (searchIndex === -1) {
			options.pathname = options.path;
		} else {
			options.pathname = options.path.slice(0, searchIndex);
			options.search = options.path.slice(searchIndex + 1);
		}

		delete options.path;
	}

	for (const key of keys) {
		if (options[key]) {
			url[key] = options[key].toString();
		}
	}

	return url;
}
```

## File: `source/core/utils/proxy-events.ts`
```typescript
import type {EventEmitter} from 'node:events';

type AnyFunction = (...arguments_: unknown[]) => void;
type Functions = Record<string, AnyFunction>;

export default function proxyEvents(from: EventEmitter, to: EventEmitter, events: readonly string[]): () => void {
	const eventFunctions: Functions = {};

	for (const event of events) {
		const eventFunction = (...arguments_: unknown[]) => {
			to.emit(event, ...arguments_);
		};

		eventFunctions[event] = eventFunction;

		from.on(event, eventFunction);
	}

	return () => {
		for (const [event, eventFunction] of Object.entries(eventFunctions)) {
			from.off(event, eventFunction);
		}
	};
}
```

## File: `source/core/utils/strip-url-auth.ts`
```typescript
/*
Returns the URL as a string with `username` and `password` stripped.
*/
export default function stripUrlAuth(url: URL | string): string {
	const sanitized = new URL(url);
	sanitized.username = '';
	sanitized.password = '';
	return sanitized.toString();
}
```

## File: `source/core/utils/timer.ts`
```typescript
import {errorMonitor} from 'node:events';
import {types} from 'node:util';
import type {ClientRequest, IncomingMessage} from 'node:http';
import type {Socket} from 'node:net';
import deferToConnect from './defer-to-connect.js';

export type Timings = {
	start: number;
	socket?: number;
	lookup?: number;
	connect?: number;
	secureConnect?: number;
	upload?: number;
	response?: number;
	end?: number;
	error?: number;
	abort?: number;
	phases: {
		wait?: number;
		dns?: number;
		tcp?: number;
		tls?: number;
		request?: number;
		firstByte?: number;
		download?: number;
		total?: number;
	};
};

export type ClientRequestWithTimings = ClientRequest & {
	timings?: Timings;
};

export type IncomingMessageWithTimings = IncomingMessage & {
	timings?: Timings;
};

type SocketWithConnectionTimings = Socket & {
	__initial_connection_timings__?: {
		dnsPhase: number;
		tcpPhase: number;
		tlsPhase?: number;
	};
};

const timer = (request: ClientRequestWithTimings): Timings => {
	if (request.timings) {
		return request.timings;
	}

	const timings: Timings = {
		start: Date.now(),
		socket: undefined,
		lookup: undefined,
		connect: undefined,
		secureConnect: undefined,
		upload: undefined,
		response: undefined,
		end: undefined,
		error: undefined,
		abort: undefined,
		phases: {
			wait: undefined,
			dns: undefined,
			tcp: undefined,
			tls: undefined,
			request: undefined,
			firstByte: undefined,
			download: undefined,
			total: undefined,
		},
	};

	request.timings = timings;

	const handleError = (origin: ClientRequest | IncomingMessage) => {
		origin.once(errorMonitor, () => {
			timings.error = Date.now();
			timings.phases.total = timings.error - timings.start;
		});
	};

	handleError(request);

	const onAbort = () => {
		timings.abort = Date.now();
		timings.phases.total = timings.abort - timings.start;
	};

	request.prependOnceListener('abort', onAbort);

	const onSocket = (socket: SocketWithConnectionTimings) => {
		timings.socket = Date.now();
		timings.phases.wait = timings.socket - timings.start;

		if (types.isProxy(socket)) {
			// HTTP/2: The socket is a proxy, so connection events won't fire.
			// We can't measure connection timings, so leave them undefined.
			// This prevents NaN in phases.request calculation.
			return;
		}

		// Check if socket is already connected (reused from connection pool)
		const socketAlreadyConnected = socket.writable && !socket.connecting;

		if (socketAlreadyConnected) {
			// Socket reuse detected: the socket was already connected from a previous request.
			// For reused sockets, set all connection timestamps to socket time since no new
			// connection was made for THIS request. But preserve phase durations from the
			// original connection so they're not lost.
			timings.lookup = timings.socket;
			timings.connect = timings.socket;

			if (socket.__initial_connection_timings__) {
				// Restore the phase timings from the initial connection
				timings.phases.dns = socket.__initial_connection_timings__.dnsPhase;
				timings.phases.tcp = socket.__initial_connection_timings__.tcpPhase;
				timings.phases.tls = socket.__initial_connection_timings__.tlsPhase;

				// Set secureConnect timestamp if there was TLS
				if (timings.phases.tls !== undefined) {
					timings.secureConnect = timings.socket;
				}
			} else {
				// Socket reused but no initial timings stored (e.g., from external code)
				// Set phases to 0
				timings.phases.dns = 0;
				timings.phases.tcp = 0;
			}

			return;
		}

		const lookupListener = () => {
			timings.lookup = Date.now();
			timings.phases.dns = timings.lookup - timings.socket!;
		};

		socket.prependOnceListener('lookup', lookupListener);

		deferToConnect(socket, {
			connect() {
				timings.connect = Date.now();
				if (timings.lookup === undefined) {
					// No DNS lookup occurred (e.g., connecting to an IP address directly)
					// Set lookup to socket time (no time elapsed for DNS)
					socket.removeListener('lookup', lookupListener);
					timings.lookup = timings.socket!;
					timings.phases.dns = 0;
				}

				timings.phases.tcp = timings.connect - timings.lookup;

				// If lookup and connect happen at the EXACT same time (tcp = 0),
				// DNS was served from cache and the dns value is just event loop overhead.
				// Set dns to 0 to indicate no actual DNS resolution occurred.
				// Fixes https://github.com/szmarczak/http-timer/issues/35
				if (timings.phases.tcp === 0 && timings.phases.dns && timings.phases.dns > 0) {
					timings.phases.dns = 0;
				}

				// Store connection phase timings on socket for potential reuse
				socket.__initial_connection_timings__ ??= {
					dnsPhase: timings.phases.dns!,
					// eslint-disable-next-line @typescript-eslint/no-unnecessary-type-assertion -- TypeScript can't prove this is defined due to callback structure
					tcpPhase: timings.phases.tcp!,
				};
			},
			secureConnect() {
				timings.secureConnect = Date.now();
				timings.phases.tls = timings.secureConnect - timings.connect!;

				// Update stored timings with TLS phase timing
				if (socket.__initial_connection_timings__) {
					socket.__initial_connection_timings__.tlsPhase = timings.phases.tls;
				}
			},
		});
	};

	if (request.socket) {
		onSocket(request.socket as SocketWithConnectionTimings);
	} else {
		request.prependOnceListener('socket', onSocket as (socket: Socket) => void);
	}

	const onUpload = () => {
		timings.upload = Date.now();

		// Calculate request phase if we have connection timings
		const secureOrConnect = timings.secureConnect ?? timings.connect;
		if (secureOrConnect !== undefined) {
			timings.phases.request = timings.upload - secureOrConnect;
		}
		// If both are undefined (HTTP/2), phases.request stays undefined (not NaN)
	};

	if (request.writableFinished) {
		onUpload();
	} else {
		request.prependOnceListener('finish', onUpload);
	}

	request.prependOnceListener('response', (response: IncomingMessageWithTimings) => {
		timings.response = Date.now();
		timings.phases.firstByte = timings.response - timings.upload!;

		response.timings = timings;
		handleError(response);

		response.prependOnceListener('end', () => {
			request.off('abort', onAbort);
			response.off('aborted', onAbort);

			if (timings.phases.total !== undefined) {
				// Aborted or errored
				return;
			}

			timings.end = Date.now();
			timings.phases.download = timings.end - timings.response!;
			timings.phases.total = timings.end - timings.start;
		});

		response.prependOnceListener('aborted', onAbort);
	});

	return timings;
};

export default timer;
```

## File: `source/core/utils/unhandle.ts`
```typescript
import type {EventEmitter} from 'node:events';

type Origin = EventEmitter;
type Event = string | symbol;
type AnyFunction = (...arguments_: any[]) => void;

type Handler = {
	origin: Origin;
	event: Event;
	fn: AnyFunction;
};

type Unhandler = {
	once: (origin: Origin, event: Event, function_: AnyFunction) => void;
	unhandleAll: () => void;
};

// When attaching listeners, it's very easy to forget about them.
// Especially if you do error handling and set timeouts.
// So instead of checking if it's proper to throw an error on every timeout ever,
// use this simple tool which will remove all listeners you have attached.
export default function unhandle(): Unhandler {
	const handlers: Handler[] = [];

	return {
		once(origin: Origin, event: Event, function_: AnyFunction) {
			origin.once(event, function_);
			handlers.push({origin, event, fn: function_});
		},

		unhandleAll() {
			for (const handler of handlers) {
				const {origin, event, fn} = handler;
				origin.removeListener(event, fn);
			}

			handlers.length = 0;
		},
	};
}
```

## File: `source/core/utils/weakable-map.ts`
```typescript
export default class WeakableMap<K, V> {
	weakMap = new WeakMap<Record<string, unknown>, V>();
	map = new Map<K, V>();

	set(key: K, value: V): void {
		if (typeof key === 'object') {
			this.weakMap.set(key as unknown as Record<string, unknown>, value);
		} else {
			this.map.set(key, value);
		}
	}

	get(key: K): V | undefined {
		if (typeof key === 'object') {
			return this.weakMap.get(key as unknown as Record<string, unknown>);
		}

		return this.map.get(key);
	}

	has(key: K): boolean {
		if (typeof key === 'object') {
			return this.weakMap.has(key as unknown as Record<string, unknown>);
		}

		return this.map.has(key);
	}
}
```

## File: `test/abort.ts`
```typescript
import process from 'node:process';
import {EventEmitter} from 'node:events';
import {Readable as ReadableStream} from 'node:stream';
import {pipeline as streamPipeline} from 'node:stream/promises';
import test from 'ava';
import delay from 'delay';
import getStream from 'get-stream';
import {pEvent} from 'p-event';
import type {Handler} from 'express';
import {createSandbox} from 'sinon';
import got from '../source/index.js';
import slowDataStream from './helpers/slow-data-stream.js';
import type {GlobalClock} from './helpers/types.js';
import type {ExtendedHttpTestServer} from './helpers/create-http-test-server.js';
import withServer, {withServerAndFakeTimers} from './helpers/with-server.js';

const prepareServer = (server: ExtendedHttpTestServer, clock: GlobalClock): {
	emitter: EventEmitter;
	promise: Promise<unknown>;
	redirectRequestCount: () => number;
} => {
	const emitter = new EventEmitter();
	let redirectRequestCount = 0;

	const promise = new Promise<void>((resolve, reject) => {
		server.all('/abort', async (request, response) => {
			emitter.emit('connection');

			request.once('aborted', resolve);
			response.once('finish', reject.bind(null, new Error('Request finished instead of aborting.')));

			try {
				await pEvent(request, 'end');
			} catch {
				// Node.js 15.0.0 throws AND emits `aborted`
			}

			response.end();
		});

		server.get('/redirect', (_request, response) => {
			redirectRequestCount++;
			response.writeHead(302, {
				location: `${server.url}/abort`,
			});
			response.end();

			emitter.emit('sentRedirect');

			clock.tick(3000);
			resolve();
		});
	});

	return {
		emitter,
		promise,
		redirectRequestCount: () => redirectRequestCount,
	};
};

const downloadHandler = (clock?: GlobalClock): Handler => (_request, response) => {
	response.writeHead(200, {
		'transfer-encoding': 'chunked',
	});

	response.flushHeaders();

	(async () => {
		try {
			await streamPipeline(
				slowDataStream(clock),
				response,
			);
		} catch {}

		response.end();
	})();
};

const sandbox = createSandbox();

const createAbortController = (): {controller: AbortController; signalHandlersRemoved: () => boolean} => {
	const controller = new AbortController();
	sandbox.spy(controller.signal);
	// @ts-expect-error AbortSignal type definition issue: https://github.com/DefinitelyTyped/DefinitelyTyped/discussions/57805
	const signalHandlersRemoved = () => controller.signal.addEventListener.callCount === controller.signal.removeEventListener.callCount;
	return {
		controller, signalHandlersRemoved,
	};
};

test.afterEach(() => {
	sandbox.restore();
});

test.serial('does not retry after abort', withServerAndFakeTimers, async (t, server, got, clock) => {
	const {emitter, promise} = prepareServer(server, clock);
	const {controller, signalHandlersRemoved} = createAbortController();

	const gotPromise = got('redirect', {
		signal: controller.signal,
		retry: {
			calculateDelay() {
				t.fail('Makes a new try after abort');
				return 0;
			},
		},
	});

	emitter.once('sentRedirect', () => {
		controller.abort();
	});

	await t.throwsAsync(gotPromise, {
		code: 'ERR_ABORTED',
		message: 'This operation was aborted.',
	});

	await t.notThrowsAsync(promise, 'Request finished instead of aborting.');

	t.true(signalHandlersRemoved(), 'Abort signal event handlers not removed');
});

test.serial('does not make a retry request after abort when calculateDelay returns a positive value', withServerAndFakeTimers, async (t, server, got, clock) => {
	const {emitter, promise, redirectRequestCount} = prepareServer(server, clock);
	const {controller, signalHandlersRemoved} = createAbortController();

	const gotPromise = got('redirect', {
		signal: controller.signal,
		retry: {
			calculateDelay: () => 100,
			limit: 1,
		},
	});

	emitter.once('sentRedirect', () => {
		controller.abort();
	});

	await t.throwsAsync(gotPromise, {
		code: 'ERR_ABORTED',
		message: 'This operation was aborted.',
	});

	clock.tick(1000);

	await t.notThrowsAsync(promise, 'Request finished instead of aborting.');
	t.is(redirectRequestCount(), 1);
	t.true(signalHandlersRemoved(), 'Abort signal event handlers not removed');
});

test.serial('abort request timeouts', withServer, async (t, server, got) => {
	server.get('/', () => {});

	const {controller, signalHandlersRemoved} = createAbortController();

	const gotPromise = got({
		signal: controller.signal,
		timeout: {
			request: 10,
		},
		retry: {
			calculateDelay({computedValue}) {
				process.nextTick(() => {
					controller.abort();
				});

				if (computedValue) {
					return 20;
				}

				return 0;
			},
			limit: 1,
		},
	});

	await t.throwsAsync(gotPromise, {
		code: 'ERR_ABORTED',
		message: 'This operation was aborted.',
	});

	t.true(signalHandlersRemoved(), 'Abort signal event handlers not removed');

	// Wait for unhandled errors
	await delay(40);
});

test.serial('aborts in-progress request', withServerAndFakeTimers, async (t, server, got, clock) => {
	const {emitter, promise} = prepareServer(server, clock);

	const {controller, signalHandlersRemoved} = createAbortController();

	const body = new ReadableStream({
		read() {},
	});
	body.push('1');

	const gotPromise = got.post('abort', {body, signal: controller.signal});

	// Wait for the connection to be established before canceling
	emitter.once('connection', () => {
		controller.abort();
		body.push(null);
	});

	await t.throwsAsync(gotPromise, {
		code: 'ERR_ABORTED',
		message: 'This operation was aborted.',
	});
	await t.notThrowsAsync(promise, 'Request finished instead of aborting.');

	t.true(signalHandlersRemoved(), 'Abort signal event handlers not removed');
});

test.serial('aborts in-progress request with timeout', withServerAndFakeTimers, async (t, server, got, clock) => {
	const {emitter, promise} = prepareServer(server, clock);

	const {controller, signalHandlersRemoved} = createAbortController();

	const body = new ReadableStream({
		read() {},
	});
	body.push('1');

	const gotPromise = got.post('abort', {body, timeout: {request: 10_000}, signal: controller.signal});

	// Wait for the connection to be established before canceling
	emitter.once('connection', () => {
		controller.abort();
		body.push(null);
	});

	await t.throwsAsync(gotPromise, {
		code: 'ERR_ABORTED',
		message: 'This operation was aborted.',
	});
	await t.notThrowsAsync(promise, 'Request finished instead of aborting.');

	t.true(signalHandlersRemoved(), 'Abort signal event handlers not removed');
});

test.serial('abort immediately', withServerAndFakeTimers, async (t, server, got, clock) => {
	const {controller, signalHandlersRemoved} = createAbortController();

	const promise = new Promise<void>((resolve, reject) => {
		// We won't get an abort or even a connection
		// We assume no request within 1000ms equals a (client side) aborted request
		server.get('/abort', (_request, response) => {
			response.once('finish', reject.bind(globalThis, new Error('Request finished instead of aborting.')));
			response.end();
		});

		clock.tick(1000);
		resolve();
	});

	const gotPromise = got('abort', {signal: controller.signal});
	controller.abort();

	await t.throwsAsync(gotPromise, {
		code: 'ERR_ABORTED',
		message: 'This operation was aborted.',
	});
	await t.notThrowsAsync(promise, 'Request finished instead of aborting.');

	t.true(signalHandlersRemoved(), 'Abort signal event handlers not removed');
});

test('recover from abort using abortable promise attribute', async t => {
	// Abort before connection started
	const {controller, signalHandlersRemoved} = createAbortController();

	const promise = got('http://example.com', {signal: controller.signal});

	controller.abort();

	await t.notThrowsAsync(async () => {
		try {
			await promise;
		} catch (error: unknown) {
			if (controller.signal.aborted) {
				return;
			}

			throw error;
		}
	});

	t.true(signalHandlersRemoved(), 'Abort signal event handlers not removed');
});

test('recover from abort using error instance', async t => {
	const {controller, signalHandlersRemoved} = createAbortController();

	const promise = got('http://example.com', {signal: controller.signal});

	controller.abort();

	await t.notThrowsAsync(async () => {
		try {
			await promise;
		} catch (error: unknown) {
			if (error instanceof Error && error.message === 'This operation was aborted.') {
				return;
			}

			throw error;
		}
	});

	t.true(signalHandlersRemoved(), 'Abort signal event handlers not removed');
});

test.serial('throws on incomplete (aborted) response', withServerAndFakeTimers, async (t, server, got, clock) => {
	server.get('/', downloadHandler());

	const {controller, signalHandlersRemoved} = createAbortController();

	const promise = got('', {signal: controller.signal});

	clock.setTimeout(() => {
		controller.abort();
	}, 400);
	clock.tick(400);

	await t.throwsAsync(promise, {
		code: 'ERR_ABORTED',
		message: 'This operation was aborted.',
	});

	t.true(signalHandlersRemoved(), 'Abort signal event handlers not removed');
});

test.serial('throws on incomplete (aborted) stream response', withServerAndFakeTimers, async (t, server, got, clock) => {
	server.get('/', downloadHandler(clock));

	const {controller, signalHandlersRemoved} = createAbortController();

	const stream = got.stream('', {signal: controller.signal});

	clock.setTimeout(() => {
		controller.abort();
	}, 400);
	clock.tick(400);

	await t.throwsAsync(getStream(stream), {
		code: 'ERR_ABORTED',
		message: 'This operation was aborted.',
	});

	t.true(signalHandlersRemoved(), 'Abort signal event handlers not removed');
});

test('throws when aborting cached request', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.setHeader('Cache-Control', 'public, max-age=60');
		response.end(Date.now().toString());
	});

	const cache = new Map();

	await got({cache});

	const {controller, signalHandlersRemoved} = createAbortController();
	const promise = got({cache, signal: controller.signal});
	controller.abort();

	await t.throwsAsync(promise, {
		code: 'ERR_ABORTED',
		message: 'This operation was aborted.',
	});

	t.true(signalHandlersRemoved(), 'Abort signal event handlers not removed');
});

test('removes abort signal event handlers after successful request', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	const {controller, signalHandlersRemoved} = createAbortController();
	const response = await got('', {signal: controller.signal});

	t.is(response.body, 'ok');
	t.true(signalHandlersRemoved(), 'Abort signal event handlers not removed');
});

test('support setting the signal as a default option', async t => {
	const {controller, signalHandlersRemoved} = createAbortController();

	const got2 = got.extend({signal: controller.signal});
	const p = got2('http://example.com');
	controller.abort();

	await t.throwsAsync(p, {
		code: 'ERR_ABORTED',
		message: 'This operation was aborted.',
	});

	t.true(signalHandlersRemoved(), 'Abort signal event handlers not removed');
});

const timeoutErrorCode = 23;
// See https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal/timeout_static
test('support AbortSignal.timeout()', async t => {
	const signal = AbortSignal.timeout(1);

	const p = got('http://example.com', {signal});

	await t.throwsAsync(p, {
		name: 'TimeoutError',
		code: timeoutErrorCode,
		message: 'The operation was aborted due to timeout',
	});
});

test.serial('support AbortSignal.timeout() with stream', withServerAndFakeTimers, async (t, server, got, clock) => {
	server.get('/', downloadHandler(clock));

	const signal = AbortSignal.timeout(1);
	const stream = got.stream('', {signal});

	clock.tick(1);

	await t.throwsAsync(getStream(stream), {
		name: 'TimeoutError',
		code: timeoutErrorCode,
		message: 'The operation was aborted due to timeout',
	});
});

test.serial('support AbortSignal.timeout() with user abort on stream', withServerAndFakeTimers, async (t, server, got, clock) => {
	server.get('/', downloadHandler(clock));

	const controller = new AbortController();
	const timeoutSignal = AbortSignal.timeout(1000);
	const signal = AbortSignal.any([
		controller.signal,
		timeoutSignal,
	]);

	const stream = got.stream('', {signal});

	clock.setTimeout(() => {
		controller.abort();
	}, 10);
	clock.tick(10);

	await t.throwsAsync(getStream(stream), {
		name: 'AbortError',
		code: 'ERR_ABORTED',
		message: 'This operation was aborted.',
	});
});

test('support AbortSignal.timeout() without user abort', async t => {
	const {controller, signalHandlersRemoved} = createAbortController();
	const timeoutSignal = AbortSignal.timeout(1);
	const signal = AbortSignal.any([
		controller.signal,
		timeoutSignal,
	]);
	const p = got('http://example.com', {signal});

	await t.throwsAsync(p, {
		name: 'TimeoutError',
		code: timeoutErrorCode,
		message: 'The operation was aborted due to timeout',
	});

	t.true(signalHandlersRemoved(), 'Abort signal event handlers not removed');
});

test('support AbortSignal.timeout() with user abort', async t => {
	const {controller, signalHandlersRemoved} = createAbortController();
	const timeoutSignal = AbortSignal.timeout(1000);
	const signal = AbortSignal.any([
		controller.signal,
		timeoutSignal,
	]);

	setTimeout(() => {
		controller.abort();
	}, 10);

	const p = got('http://example.com', {signal});

	await t.throwsAsync(p, {
		name: 'AbortError',
		code: 'ERR_ABORTED',
		message: 'This operation was aborted.',
	});

	t.true(signalHandlersRemoved(), 'Abort signal event handlers not removed');
});
```

## File: `test/agent.ts`
```typescript
import {Agent as HttpAgent} from 'node:http';
import {Agent as HttpsAgent} from 'node:https';
import test from 'ava';
import sinon from 'sinon';
import type {Constructor} from 'type-fest';
import withServer, {withHttpsServer} from './helpers/with-server.js';

const createAgentSpy = <T extends HttpsAgent>(AgentClass: Constructor<any>): {agent: T; spy: sinon.SinonSpy} => {
	const agent: T = new AgentClass({keepAlive: true});
	const spy = sinon.spy(agent, 'addRequest' as any);
	return {agent, spy};
};

test('non-object agent option works with http', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	const {agent, spy} = createAgentSpy(HttpAgent);

	t.truthy((await got({
		https: {
			rejectUnauthorized: false,
		},
		agent: {
			http: agent,
		},
	})).body);
	t.true(spy.calledOnce);

	// Make sure to close all open sockets
	agent.destroy();
});

test('non-object agent option works with https', withHttpsServer(), async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	const {agent, spy} = createAgentSpy(HttpsAgent);

	t.truthy((await got({
		https: {
			rejectUnauthorized: false,
		},
		agent: {
			https: agent,
		},
	})).body);
	t.true(spy.calledOnce);

	// Make sure to close all open sockets
	agent.destroy();
});

test('redirects from http to https work with an agent object', withServer, async (t, serverHttp) => {
	await withHttpsServer().exec(t, async (t, serverHttps, got) => {
		serverHttp.get('/', (_request, response) => {
			response.end('http');
		});

		serverHttps.get('/', (_request, response) => {
			response.end('https');
		});

		serverHttp.get('/httpToHttps', (_request, response) => {
			response.writeHead(302, {
				location: serverHttps.url,
			});
			response.end();
		});

		const {agent: httpAgent, spy: httpSpy} = createAgentSpy(HttpAgent);
		const {agent: httpsAgent, spy: httpsSpy} = createAgentSpy<HttpsAgent>(HttpsAgent);

		t.truthy((await got('httpToHttps', {
			prefixUrl: serverHttp.url,
			agent: {
				http: httpAgent,
				https: httpsAgent,
			},
		})).body);
		t.true(httpSpy.calledOnce);
		t.true(httpsSpy.calledOnce);

		// Make sure to close all open sockets
		httpAgent.destroy();
		httpsAgent.destroy();
	});
});

test('redirects from https to http work with an agent object', withHttpsServer(), async (t, serverHttps, got) => {
	await withServer.exec(t, async (t, serverHttp) => {
		serverHttp.get('/', (_request, response) => {
			response.end('http');
		});

		serverHttps.get('/', (_request, response) => {
			response.end('https');
		});

		serverHttps.get('/httpsToHttp', (_request, response) => {
			response.writeHead(302, {
				location: serverHttp.url,
			});
			response.end();
		});

		const {agent: httpAgent, spy: httpSpy} = createAgentSpy(HttpAgent);
		const {agent: httpsAgent, spy: httpsSpy} = createAgentSpy(HttpsAgent);

		t.truthy((await got('httpsToHttp', {
			prefixUrl: serverHttps.url,
			agent: {
				http: httpAgent,
				https: httpsAgent,
			},
		})).body);
		t.true(httpSpy.calledOnce);
		t.true(httpsSpy.calledOnce);

		// Make sure to close all open sockets
		httpAgent.destroy();
		httpsAgent.destroy();
	});
});

test('socket connect listener cleaned up after request', withHttpsServer(), async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	const {agent} = createAgentSpy(HttpsAgent);

	// Make sure there are no memory leaks when reusing keep-alive sockets
	for (let index = 0; index < 20; index++) {
		// eslint-disable-next-line no-await-in-loop
		await got({
			agent: {
				https: agent,
			},
		});
	}

	for (const value of Object.values(agent.freeSockets)) {
		if (!value) {
			continue;
		}

		for (const sock of value) {
			t.is(sock.listenerCount('connect'), 0);
		}
	}

	// Make sure to close all open sockets
	agent.destroy();
});

test('no socket hung up regression', withServer, async (t, server, got) => {
	const agent = new HttpAgent({keepAlive: true});
	const token = 'helloworld';

	server.get('/', (request, response) => {
		if (request.headers.token !== token) {
			response.statusCode = 401;
			response.end();
			return;
		}

		response.end('ok');
	});

	const {body} = await got({
		agent: {
			http: agent,
		},
		hooks: {
			afterResponse: [
				async (response, retryWithMergedOptions) => {
					// Force clean-up
					response.socket?.destroy();

					// Unauthorized
					if (response.statusCode === 401) {
						return retryWithMergedOptions({
							headers: {
								token,
							},
						});
					}

					// No changes otherwise
					return response;
				},
			],
		},
		// Disable automatic retries, manual retries are allowed
		retry: {
			limit: 0,
		},
	});

	t.is(body, 'ok');

	agent.destroy();
});

test('accept undefined agent', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	const undefinedAgent = undefined;
	t.truthy((await got({
		https: {
			rejectUnauthorized: false,
		},
		agent: undefinedAgent,
	})).body);
});

test('accept false as agent value', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	// Should not throw error when setting agent types to false
	t.notThrows(() => got.extend({
		agent: {
			http: false,
			https: false,
			http2: false,
		},
	}));

	// Should successfully make request with false agent values
	const response = await got({
		agent: {
			http: false,
		},
	});

	t.is(response.body, 'ok');
});

test('accept mixed agent values with false', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	const {agent: httpAgent} = createAgentSpy(HttpAgent);

	// Should accept a mix of agent instance and false values
	const response = await got({
		agent: {
			http: httpAgent,
			https: false,
			http2: false,
		},
	});

	t.is(response.body, 'ok');

	httpAgent.destroy();
});
```

## File: `test/arguments.ts`
```typescript
import test from 'ava';
import type {Handler} from 'express';
import getStream from 'get-stream';
import got, {Options, RequestError, type StrictOptions} from '../source/index.js';
import withServer, {withBodyParsingServer} from './helpers/with-server.js';
import invalidUrl from './helpers/invalid-url.js';

const echoUrl: Handler = (request, response) => {
	response.end(request.url);
};

test('`url` is required', async t => {
	await t.throwsAsync(
		// @ts-expect-error No argument on purpose.
		got(),
		{
			instanceOf: RequestError,
			message: 'Missing `url` property',
		},
	);

	const firstError = await t.throwsAsync(got(''));
	invalidUrl(t, firstError, '');

	t.throws(() => {
		void got({url: ''} as any);
	}, {
		instanceOf: TypeError,
		message: 'The `url` option is not supported in options objects. Pass it as the first argument instead.',
	});
});

test('throws if no arguments provided', async t => {
	// @ts-expect-error Error tests
	await t.throwsAsync(got(), {
		instanceOf: RequestError,
		message: 'Missing `url` property',
	});
});

test('throws if the url option is missing', async t => {
	await t.throwsAsync(got({}), {
		instanceOf: RequestError,
		message: 'Missing `url` property',
	});
});

test('throws if an invalid argument is passed', async t => {
	await t.throwsAsync(
		// @ts-expect-error Error tests
		got(false),
		{
			instanceOf: RequestError,
			message: 'Option \'input\': Expected values which are `string`, `URL`, `Object`, or `undefined`. Received values of type `boolean`.',
		},
	);
});

test('throws an error if the protocol is not specified', async t => {
	const error = await t.throwsAsync(got('example.com'));
	invalidUrl(t, error, 'example.com');
});

test('properly encodes query string', withServer, async (t, server, got) => {
	server.get('/', echoUrl);

	const path = '?test=http://example.com?foo=bar';
	const {body} = await got(path);
	t.is(body, '/?test=http://example.com?foo=bar');
});

test('options are optional', withServer, async (t, server, got) => {
	server.get('/test', echoUrl);

	t.is((await got('test')).body, '/test');
});

test('methods are normalized', withServer, async (t, server, got) => {
	server.post('/test', echoUrl);

	const instance = got.extend({
		handlers: [
			(options, next) => {
				if (options.method === options.method.toUpperCase()) {
					t.pass();
				} else {
					t.fail();
				}

				return next(options);
			},
		],
	});

	await instance('test', {method: 'post'});
});

test('throws an error when legacy URL is passed', withServer, async (t, server) => {
	server.get('/test', echoUrl);

	await t.throwsAsync(
		got({href: `${server.url}/test`} as any),
		{
			instanceOf: RequestError,
			message: 'Unexpected option: href',
		},
	);

	await t.throwsAsync(
		got({
			protocol: 'http:',
			hostname: 'localhost',
			port: server.port,
		} as any),
		{
			instanceOf: RequestError,
			message: 'Unexpected option: protocol',
		},
	);
});

test('overrides `searchParams` from options', withServer, async (t, server, got) => {
	server.get('/', echoUrl);

	const {body} = await got(
		'?drop=this',
		{
			searchParams: {
				test: 'wow',
			},
		},
	);

	t.is(body, '/?test=wow');
});

test('does not duplicate `searchParams`', withServer, async (t, server, got) => {
	server.get('/', echoUrl);

	const instance = got.extend({
		searchParams: new URLSearchParams({foo: '123'}),
	});

	const body = await instance('?bar=456').text();

	t.is(body, '/?foo=123');
});

test('escapes `searchParams` parameter values', withServer, async (t, server, got) => {
	server.get('/', echoUrl);

	const {body} = await got({
		searchParams: {
			test: 'it’s ok',
		},
	});

	t.is(body, '/?test=it%E2%80%99s+ok');
});

test('the `searchParams` option can be a URLSearchParams', withServer, async (t, server, got) => {
	server.get('/', echoUrl);

	// eslint-disable-next-line unicorn/prevent-abbreviations
	const searchParams = new URLSearchParams({test: 'wow'});
	const {body} = await got({searchParams});
	t.is(body, '/?test=wow');
});

test('ignores empty searchParams object', withServer, async (t, server, got) => {
	server.get('/test', echoUrl);

	t.is((await got('test', {searchParams: {}})).requestUrl.toString(), `${server.url}/test`);
});

test('throws when passing body with a non payload method', async t => {
	await t.throwsAsync(got('https://example.com', {body: 'asdf'}), {
		instanceOf: RequestError,
		message: 'The `GET` method cannot be used with a body',
	});
});

test('`allowGetBody` option', withServer, async (t, server, got) => {
	server.get('/test', echoUrl);

	await t.notThrowsAsync(got('test', {body: 'asdf', allowGetBody: true}));
});

test('WHATWG URL support', withServer, async (t, server) => {
	server.get('/test', echoUrl);

	const url = new URL(`${server.url}/test`);
	await t.notThrowsAsync(got(url));
});

test('`got.stream()` exposes internal `isStream` in init hook context', withServer, async (t, server, got) => {
	server.get('/stream', (_request, response) => {
		response.end('ok');
	});

	const streamWithInput = got.stream('stream', {
		hooks: {
			init: [
				plain => {
					t.true(Reflect.get(plain as Record<string, unknown>, 'isStream') === true);
				},
			],
		},
	});

	t.is(await getStream(streamWithInput), 'ok');
});

test('`isStream` option is ignored on promise API', withServer, async (t, server, got) => {
	server.get('/stream', (_request, response) => {
		response.end('ok');
	});

	const result = got('stream', {
		// @ts-expect-error Removed option
		isStream: true,
	});

	t.true(typeof result.then === 'function');
	t.is(await result.text(), 'ok');
});

test('throws when `url` is passed in options object', t => {
	t.throws(() => {
		void got({url: 'https://example.com'} as any);
	}, {
		instanceOf: TypeError,
		message: 'The `url` option is not supported in options objects. Pass it as the first argument instead.',
	});
});

test('throws when `url` is passed in stream options object', t => {
	const error = t.throws(() => {
		got.stream({url: 'https://example.com'} as any);
	});

	t.true(error instanceof TypeError);
	t.is(error.message, 'The `url` option is not supported in options objects. Pass it as the first argument instead.');
});

test('throws when `url` is passed as second argument option', t => {
	const error = t.throws(() => {
		void got('https://example.com', {url: 'https://example.com'} as any);
	});

	t.true(error instanceof TypeError);
	t.is(error.message, 'The `url` option is not supported in options objects. Pass it as the first argument instead.');
});

test('throws when `url` is passed to extend defaults', t => {
	const error = t.throws(() => {
		got.extend({url: 'https://example.com'} as any);
	});

	t.true(error instanceof TypeError);
	t.is(error.message, 'The `url` option is not supported in options objects. Pass it as the first argument instead.');
});

test('can omit `url` option if using `prefixUrl`', withServer, async (t, server, got) => {
	server.get('/', echoUrl);

	await t.notThrowsAsync(got({}));
});

test('throws when `options.hooks` is not an object', async t => {
	await t.throwsAsync(
		// @ts-expect-error Error tests
		got('https://example.com', {hooks: 'not object'}),
		{
			instanceOf: RequestError,
			message: 'Expected value which is `Object`, received value of type `string`.',
		},
	);
});

test('throws when known `options.hooks` value is not an array', async t => {
	await t.throwsAsync(
		// @ts-expect-error Error tests
		got('https://example.com', {hooks: {beforeRequest: {}}}),
		{
			instanceOf: RequestError,
			message: 'Option \'hooks.beforeRequest\': Expected values which are `Array` or `undefined`. Received values of type `Object`.',
		},
	);
});

test('throws when known `options.hooks` array item is not a function', async t => {
	await t.throwsAsync(
		// @ts-expect-error Error tests
		got('https://example.com', {hooks: {beforeRequest: [{}]}}),
		{
			instanceOf: RequestError,
			message: 'Expected value which is `Function`, received value of type `Object`.',
		},
	);
});

test('does not allow extra keys in `options.hooks`', withServer, async (t, server, got) => {
	server.get('/test', echoUrl);

	// @ts-expect-error Error tests
	await t.throwsAsync(got('test', {hooks: {extra: []}}), {
		instanceOf: RequestError,
		message: 'Unexpected hook event: extra',
	});
});

test('`prefixUrl` option works', withServer, async (t, server, got) => {
	server.get('/test/foobar', echoUrl);

	const instanceA = got.extend({prefixUrl: `${server.url}/test`});
	const {body} = await instanceA('foobar');
	t.is(body, '/test/foobar');
});

test('accepts WHATWG URL as the `prefixUrl` option', withServer, async (t, server, got) => {
	server.get('/test/foobar', echoUrl);

	const instanceA = got.extend({prefixUrl: new URL(`${server.url}/test`)});
	const {body} = await instanceA('foobar');
	t.is(body, '/test/foobar');
});

test('backslash in the end of `prefixUrl` option is optional', withServer, async (t, server) => {
	server.get('/test/foobar', echoUrl);

	const instanceA = got.extend({prefixUrl: `${server.url}/test/`});
	const {body} = await instanceA('foobar');
	t.is(body, '/test/foobar');
});

test('`prefixUrl` can be changed if the URL contains the old one', withServer, async (t, server) => {
	server.get('/', echoUrl);

	const instanceA = got.extend({
		prefixUrl: `${server.url}/meh`,
		handlers: [
			(options, next) => {
				options.prefixUrl = server.url;
				return next(options);
			},
		],
	});

	const {body} = await instanceA('');
	t.is(body, '/');
});

test('throws if the `searchParams` value is invalid', async t => {
	await t.throwsAsync(
		got('https://example.com', {
			searchParams: {
			// @ts-expect-error Error tests
				foo: [],
			},
		}),
		{
			instanceOf: RequestError,
			message: 'Option \'searchParams.foo\': Expected values which are `string`, `number`, `boolean`, `null`, or `undefined`. Received values of type `Array`.',
		},
	);
});

// Note: This test was added in commit 2b8ed1f (Oct 2020) when context was changed to be enumerable,
// but it has been marked as .failing since it was introduced. The feature was never fully implemented
// because making context enumerable breaks other tests that expect it to be non-enumerable.
// This represents an unfinished feature request from 3+ years ago, not a recent regression.
test.failing('`context` option is enumerable', withServer, async (t, server, got) => {
	server.get('/', echoUrl);

	const context = {
		foo: 'bar',
	};

	await got({
		context,
		hooks: {
			beforeRequest: [
				options => {
					t.deepEqual(options.context, context);
					t.true(Object.prototype.propertyIsEnumerable.call(options, 'context'));
				},
			],
		},
	});
});

test('`context` option is never frozen', t => {
	const client = got.extend({
		context: {
			token: 'foobar',
		},
	});

	client.defaults.options.context.token = '1234';

	t.is(client.defaults.options.context.token, '1234');
});

test('`context` option is accessible when using hooks', withServer, async (t, server) => {
	server.get('/', echoUrl);

	const context = {
		foo: 'bar',
	};

	await got(server.url, {
		context,
		hooks: {
			beforeRequest: [
				options => {
					t.deepEqual(options.context, context);
					t.false(Object.prototype.propertyIsEnumerable.call(options, 'context'));
				},
			],
		},
	});
});

test('`context` option is accessible when extending instances', t => {
	const context = {
		foo: 'bar',
	};

	const instance = got.extend({context});

	t.deepEqual(instance.defaults.options.context, context);
	t.false(Object.prototype.propertyIsEnumerable.call(instance.defaults.options, 'context'));
});

test('`context` option is shallow merged', t => {
	const context = {
		foo: 'bar',
	};

	const context2 = {
		bar: 'baz',
	};

	const instance1 = got.extend({context});

	t.deepEqual(instance1.defaults.options.context, context);
	t.false(Object.prototype.propertyIsEnumerable.call(instance1.defaults.options, 'context'));

	const instance2 = instance1.extend({context: context2});

	t.deepEqual(instance2.defaults.options.context, {...context, ...context2});
});

test('throws if `options.encoding` is `null`', async t => {
	await t.throwsAsync(got('https://example.com', {
		// @ts-expect-error For testing purposes
		encoding: null,
	}), {
		instanceOf: RequestError,
		message: 'To get a Uint8Array, set `options.responseType` to `buffer` instead',
	});
});

test('throws when `url` is passed as option with input argument', t => {
	const error = t.throws(() => {
		void got('https://example.com', {
			url: 'https://example.com',
		} as any);
	});

	t.true(error instanceof TypeError);
	t.is(error.message, 'The `url` option is not supported in options objects. Pass it as the first argument instead.');
});

test('throws a helpful error when passing `followRedirects`', async t => {
	await t.throwsAsync(got('https://example.com', {
		// @ts-expect-error For testing purposes
		followRedirects: true,
	}), {
		instanceOf: RequestError,
		message: 'The `followRedirects` option does not exist. Use `followRedirect` instead.',
	});
});

test('merges `searchParams` instances', t => {
	const instance = got.extend({
		searchParams: new URLSearchParams('a=1'),
	}, {
		searchParams: new URLSearchParams('b=2'),
	});

	// eslint-disable-next-line unicorn/prevent-abbreviations
	const searchParams = instance.defaults.options.searchParams as URLSearchParams;

	t.is(searchParams.get('a'), '1');
	t.is(searchParams.get('b'), '2');
});

test('throws a helpful error when passing `auth`', async t => {
	await t.throwsAsync(got('https://example.com', {
		// @ts-expect-error For testing purposes
		auth: 'username:password',
	}), {
		instanceOf: RequestError,
		message: 'Parameter `auth` is deprecated. Use `username` / `password` instead.',
	});
});

test('throws on leading slashes', async t => {
	await t.throwsAsync(got('/asdf', {prefixUrl: 'https://example.com'}), {
		instanceOf: RequestError,
		message: '`url` must not start with a slash',
	});
});

test('throws on invalid `dnsCache` option', async t => {
	await t.throwsAsync(
		got('https://example.com', {
		// @ts-expect-error Error tests
			dnsCache: 123,
		}),
		{
			instanceOf: RequestError,
			message: 'Option \'dnsCache\': Expected values which are `Object`, `boolean`, or `undefined`. Received values of type `number`.',
		},
	);
});

test('throws on invalid `agent` option', async t => {
	await t.throwsAsync(got('https://example.com', {
		agent: {
			// @ts-expect-error Error tests
			asdf: 123,
		},
	}), {
		instanceOf: RequestError,
		message: 'Unexpected agent option: asdf',
	});
});

test('fallbacks to native http if `request(...)` returns undefined', withServer, async (t, server, got) => {
	server.get('/', echoUrl);

	const {body} = await got('', {request: () => undefined});

	t.is(body, '/');
});

test('fallbacks to native http if async `request(...)` resolves to undefined', withServer, async (t, server, got) => {
	server.get('/', echoUrl);

	const {body} = await got('', {request: async () => undefined});

	t.is(body, '/');
});

test('strict options', withServer, async (t, server, got) => {
	server.get('/', echoUrl);

	const options: StrictOptions = {};

	const {body} = await got(options);

	t.is(body, '/');
});

test('does not throw on frozen options', withServer, async (t, server, got) => {
	server.get('/', echoUrl);

	const options: StrictOptions = {};

	Object.freeze(options);

	const {body} = await got(options);

	t.is(body, '/');
});

test('encodes query string included in input', t => {
	const {url} = new Options({
		url: new URL('https://example.com/?a=b c'),
	});

	t.is(url!.search, '?a=b%20c');
});

test('normalizes search params included in options', t => {
	const {url} = new Options({
		url: new URL('https://example.com'),
		searchParams: 'a=b c',
	});

	t.is(url!.search, '?a=b+c');
});

test('reuse options while using init hook', withServer, async (t, server, got) => {
	t.plan(2);

	server.get('/', echoUrl);

	const options = {
		hooks: {
			init: [
				() => {
					t.pass();
				},
			],
		},
	};

	await got('', options);
	await got('', options);
});

test('allowGetBody sends json payload', withBodyParsingServer, async (t, server, got) => {
	server.get('/', (request, response) => {
		if (request.body.hello !== 'world') {
			response.statusCode = 400;
		}

		response.end();
	});

	const {statusCode} = await got({
		allowGetBody: true,
		json: {hello: 'world'},
		retry: {
			limit: 0,
		},
		throwHttpErrors: false,
	});
	t.is(statusCode, 200);
});

test('no URL pollution', withServer, async (t, server) => {
	server.get('/ok', echoUrl);

	const url = new URL(server.url);

	const {body} = await got(url, {
		hooks: {
			beforeRequest: [
				options => {
					options.url!.pathname = '/ok';
				},
			],
		},
	});

	t.is(url.pathname, '/');
	t.is(body, '/ok');
});

test('prefixUrl is properly replaced when extending', withServer, async (t, server) => {
	server.get('/', (request, response) => {
		response.end(request.url);
	});

	server.get('/other/path/', (request, response) => {
		response.end(request.url);
	});

	const parent = got.extend({prefixUrl: server.url});
	const child = parent.extend({prefixUrl: `${server.url}/other/path/`});

	t.is(await child.get('').text(), '/other/path/');
});

test('throws on too large noise', t => {
	/* eslint-disable no-new */
	t.throws(() => {
		new Options({
			retry: {
				noise: 101,
			},
		});
	}, {
		instanceOf: Error,
		message: 'The maximum acceptable retry noise is +/- 100ms, got 101',
	});

	t.throws(() => {
		new Options({
			retry: {
				noise: -101,
			},
		});
	}, {
		instanceOf: Error,
		message: 'The maximum acceptable retry noise is +/- 100ms, got -101',
	});

	t.throws(() => {
		new Options({
			retry: {
				noise: Number.POSITIVE_INFINITY,
			},
		});
	}, {
		instanceOf: Error,
		message: 'The maximum acceptable retry noise is +/- 100ms, got Infinity',
	});

	t.throws(() => {
		new Options({
			retry: {
				noise: Number.NEGATIVE_INFINITY,
			},
		});
	}, {
		instanceOf: Error,
		message: 'The maximum acceptable retry noise is +/- 100ms, got -Infinity',
	});

	t.notThrows(() => {
		new Options({
			retry: {
				noise: 0,
			},
		});
	});

	/* eslint-enable no-new */
});

test('options have url even if some are invalid', async t => {
	const error = await t.throwsAsync<RequestError>(got('https://example.com', {
		// @ts-expect-error Testing purposes
		invalid: true,
	}));

	t.is((error.options.url! as URL).href, 'https://example.com/');
	t.true(error instanceof Error);
});

test('options have url even if some are invalid - got.extend', async t => {
	const instance = got.extend({
		handlers: [
			(options, next) => {
				t.is((options.url! as URL).href, 'https://example.com/');
				return next(options);
			},
		],
	});

	await t.throwsAsync(
		instance('https://example.com', {
		// @ts-expect-error Testing purposes
			invalid: true,
		}),
		{
			instanceOf: Error,
		},
	);
});
```

## File: `test/cache.ts`
```typescript
import {Buffer} from 'node:buffer';
import {promisify} from 'node:util';
import {Readable as ReadableStream} from 'node:stream';
import {Agent} from 'node:http';
import {gzip} from 'node:zlib';
import process from 'node:process';
import test from 'ava';
import {pEvent} from 'p-event';
import getStream from 'get-stream';
import type {Handler} from 'express';
import CacheableLookup from 'cacheable-lookup';
import delay from 'delay';
import got, {CacheError, type Response} from '../source/index.js';
import withServer from './helpers/with-server.js';

const cacheEndpoint: Handler = (_request, response) => {
	response.setHeader('Cache-Control', 'public, max-age=60');
	response.end(Date.now().toString());
};

test('non-cacheable responses are not cached', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.setHeader('Cache-Control', 'public, no-cache, no-store');
		response.end(Date.now().toString());
	});

	const cache = new Map();

	const firstResponseInt = Number((await got({cache})).body);
	const secondResponseInt = Number((await got({cache})).body);

	t.is(cache.size, 0);
	t.true(firstResponseInt < secondResponseInt);
});

test('cacheable responses are cached', withServer, async (t, server, got) => {
	server.get('/', cacheEndpoint);

	const cache = new Map();

	const firstResponse = await got({cache});
	const secondResponse = await got({cache});

	t.is(cache.size, 1);
	t.is(firstResponse.body, secondResponse.body);
});

test('cacheable responses to POST requests are cached', withServer, async (t, server, got) => {
	server.post('/', cacheEndpoint);

	const cache = new Map();

	const firstResponse = await got({method: 'POST', body: 'test', cache});
	const secondResponse = await got({method: 'POST', body: 'test', cache});

	t.is(cache.size, 1);
	t.is(firstResponse.body, secondResponse.body);
});

test('non-cacheable responses to POST requests are not cached', withServer, async (t, server, got) => {
	server.post('/', cacheEndpoint);

	const cache = new Map();

	// POST requests with streams are not cached
	const body1 = ReadableStream.from(Buffer.from([1, 2, 3]));
	const body2 = ReadableStream.from(Buffer.from([1, 2, 3]));

	const firstResponseInt = Number((await got({method: 'POST', body: body1, cache})).body);
	const secondResponseInt = Number((await got({method: 'POST', body: body2, cache})).body);

	t.is(cache.size, 0);
	t.true(firstResponseInt < secondResponseInt);
});

test('cached response is re-encoded to current encoding option', withServer, async (t, server, got) => {
	server.get('/', cacheEndpoint);

	const cache = new Map();
	const firstEncoding = 'base64';
	const secondEncoding = 'hex';

	const firstResponse = await got({cache, encoding: firstEncoding});
	const secondResponse = await got({cache, encoding: secondEncoding});

	const expectedSecondResponseBody = Buffer.from(firstResponse.body, firstEncoding).toString(secondEncoding);

	t.is(cache.size, 1);
	t.is(secondResponse.body, expectedSecondResponseBody);
});

test('redirects are cached and re-used internally', withServer, async (t, server, got) => {
	let status301Index = 0;
	server.get('/301', (_request, response) => {
		if (status301Index === 0) {
			response.setHeader('Cache-Control', 'public, max-age=60');
			response.setHeader('Location', '/');
			response.statusCode = 301;
		}

		response.end();
		status301Index++;
	});

	let status302Index = 0;
	server.get('/302', (_request, response) => {
		if (status302Index === 0) {
			response.setHeader('Cache-Control', 'public, max-age=60');
			response.setHeader('Location', '/');
			response.statusCode = 302;
		}

		response.end();
		status302Index++;
	});

	server.get('/', cacheEndpoint);

	const cache = new Map();
	const a1 = await got('301', {cache});
	const b1 = await got('302', {cache});

	const a2 = await got('301', {cache});
	const b2 = await got('302', {cache});

	t.is(cache.size, 3);
	t.is(a1.body, b1.body);
	t.is(a1.body, a2.body);
	t.is(b1.body, b2.body);
});

test('cached response has got options', withServer, async (t, server, got) => {
	server.get('/', cacheEndpoint);

	const cache = new Map();
	const options = {
		username: 'foo',
		cache,
	};

	await got(options);
	const secondResponse = await got(options);

	t.is(secondResponse.request.options.username, options.username);
});

test('cache error throws `CacheError`', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	const cache = {};

	// @ts-expect-error Error tests
	await t.throwsAsync(got({cache}), {
		instanceOf: CacheError,
		code: 'ERR_CACHE_ACCESS',
	});
});

test('doesn\'t cache response when received HTTP error', withServer, async (t, server, got) => {
	let isFirstErrorCalled = false;
	server.get('/', (_request, response) => {
		if (!isFirstErrorCalled) {
			response.end('ok');
			return;
		}

		isFirstErrorCalled = true;
		response.statusCode = 502;
		response.end('received 502');
	});

	const cache = new Map();

	const {statusCode, body} = await got('', {cache, throwHttpErrors: false});
	t.is(statusCode, 200);
	t.is(body, 'ok');
});

test('cache should work with http2', withServer, async (t, server, got) => {
	server.get('/', cacheEndpoint);

	const instance = got.extend({
		cache: true,
		http2: true,
	});

	await t.notThrowsAsync(instance(''));
});

test('DNS cache works', async t => {
	const instance = got.extend({
		dnsCache: true,
		https: {
			rejectUnauthorized: false,
		},
	});

	await t.notThrowsAsync(instance('https://example.com'));

	// @ts-expect-error Accessing private property
	t.is(instance.defaults.options.dnsCache!._cache.size, 1);
});

test('DNS cache works - CacheableLookup instance', async t => {
	const cache = new CacheableLookup();
	await t.notThrowsAsync(got('https://example.com', {
		dnsCache: cache,
		https: {
			rejectUnauthorized: false,
		},
	}));

	t.is((cache as any)._cache.size, 1);
});

test('`isFromCache` stream property is undefined before the `response` event', withServer, async (t, server, got) => {
	server.get('/', cacheEndpoint);

	const cache = new Map();
	const stream = got.stream({cache});
	t.is(stream.isFromCache, undefined);

	await getStream(stream);
});

test('`isFromCache` stream property is false after the `response` event', withServer, async (t, server, got) => {
	server.get('/', cacheEndpoint);

	const cache = new Map();
	const stream = got.stream({cache});

	const response: Response = await pEvent(stream, 'response') as Response;
	t.is(response.isFromCache, false);
	t.is(stream.isFromCache, false);

	await getStream(stream);
});

test('`isFromCache` stream property is true if the response was cached', withServer, async (t, server, got) => {
	server.get('/', cacheEndpoint);

	const cache = new Map();

	await getStream(got.stream({cache}));
	const stream = got.stream({cache});

	const response: Response = await pEvent(stream, 'response') as Response;
	t.is(response.isFromCache, true);
	t.is(stream.isFromCache, true);

	await getStream(stream);
});

test('can disable cache by extending the instance', withServer, async (t, server, got) => {
	server.get('/', cacheEndpoint);

	const cache = new Map();

	const instance = got.extend({cache});

	await getStream(instance.stream(''));
	const stream = instance.extend({cache: false}).stream('');

	const response: Response = await pEvent(stream, 'response') as Response;
	t.is(response.isFromCache, false);
	t.is(stream.isFromCache, false);

	await getStream(stream);
});

test('does not break POST requests', withServer, async (t, server, got) => {
	server.post('/', async (request, response) => {
		request.resume();
		response.end(JSON.stringify(request.headers));
	});

	const headers = await got.post('', {
		body: '',
		cache: new Map(),
	}).json<{'content-length': string}>();

	t.is(headers['content-length'], '0');
});

test('decompresses cached responses', withServer, async (t, server, got) => {
	const etag = 'foobar';

	const payload = JSON.stringify({foo: 'bar'});
	const compressed = await promisify(gzip)(payload);

	server.get('/', (request, response) => {
		if (request.headers['if-none-match'] === etag) {
			response.statusCode = 304;
			response.end();
		} else {
			response.setHeader('content-encoding', 'gzip');
			response.setHeader('cache-control', 'public, max-age=60');
			response.setHeader('etag', etag);
			response.end(compressed);
		}
	});

	const cache = new Map();

	for (let i = 0; i < 2; i++) {
		// eslint-disable-next-line no-await-in-loop
		await t.notThrowsAsync(got({
			cache,
			responseType: 'json',
			decompress: true,
			retry: {
				limit: 2,
			},
		}));
	}

	t.is(cache.size, 1);
});

test('can replace the instance\'s HTTP cache', withServer, async (t, server, got) => {
	server.get('/', cacheEndpoint);

	const cache = new Map();
	const secondCache = new Map();

	const instance = got.extend({
		mutableDefaults: true,
		cache,
	});

	await t.notThrowsAsync(instance(''));
	await t.notThrowsAsync(instance(''));

	instance.defaults.options.cache = secondCache;

	await t.notThrowsAsync(instance(''));
	await t.notThrowsAsync(instance(''));

	t.is(cache.size, 1);
	t.is(secondCache.size, 1);
});

test('does not hang on huge response', withServer, async (t, server, got) => {
	const bufferSize = 3 * 16 * 1024;
	const times = 10;

	const buffer = Buffer.alloc(bufferSize);

	server.get('/', async (_request, response) => {
		for (let i = 0; i < 10; i++) {
			response.write(buffer);

			// eslint-disable-next-line no-await-in-loop
			await delay(100);
		}

		response.end();
	});

	const body = await got('', {
		cache: new Map(),
	}).buffer();

	t.is(body.length, bufferSize * times);
});

test('cached response ETag', withServer, async (t, server, got) => {
	const etag = 'foobar';
	const body = 'responseBody';

	server.get('/', (request, response) => {
		if (request.headers['if-none-match'] === etag) {
			response.writeHead(304);
			response.end();
		} else {
			response.writeHead(200, {etag});
			response.end(body);
		}
	});

	const cache = new Map();

	const originalResponse = await got({cache});

	t.false(originalResponse.isFromCache);
	t.is(originalResponse.body, body);

	await delay(100); // Added small delay in order to wait the cache to be populated

	t.is(cache.size, 1);

	const cachedResponse = await got({cache});

	t.true(cachedResponse.isFromCache);
	t.is(cachedResponse.body, body);
});

// Kept disabled because it depends on an external endpoint; local HTTP/2 cache coverage exists above.
// test('works with http2', async t => {
// 	const cache = new Map();

// 	const client = got.extend({
// 		http2: true,
// 		cache,
// 	});

// 	try {
// 		await client('https://httpbin.org/anything');

// 		t.pass();
// 	} catch (error: any) {
// 		if (error.message.includes('install Node.js')) {
// 			t.pass();
// 			return;
// 		}

// 		t.fail(error.message);
// 	}
// });

test('http-cache-semantics typings', t => {
	const instance = got.extend({
		cacheOptions: {
			shared: false,
		},
	});

	t.is(instance.defaults.options.cacheOptions.shared, false);
});

test('allows internal modifications', withServer, async (t, server, got) => {
	let requestCount = 0;

	server.get('/test', (_request, response) => {
		requestCount++;
		if (requestCount === 1) {
			response.writeHead(401);
			response.end();
		} else {
			response.writeHead(200);
			response.end(JSON.stringify({wat: ['123']}));
		}
	});

	const client = got.extend({
		cache: new Map(),
		hooks: {
			afterResponse: [
				async (response, retryWithMergedOptions) => {
					if (response.statusCode === 401) {
						return retryWithMergedOptions({});
					}

					return response;
				},
			],
		},
	});

	await t.notThrowsAsync(client.get('test'));
});

test('response.complete is true when using keepalive agent', withServer, async (t, server, got) => {
	const agent = {
		http: new Agent({keepAlive: true}),
	};

	const etag = 'foobar';

	const payload = JSON.stringify({foo: 'bar'});
	const compressed = await promisify(gzip)(payload);

	server.get('/', (request, response) => {
		if (request.headers['if-none-match'] === etag) {
			response.statusCode = 304;
			response.end();
		} else {
			response.setHeader('content-encoding', 'gzip');
			response.setHeader('cache-control', 'public, max-age=60');
			response.setHeader('etag', etag);
			response.end(compressed);
		}
	});

	const cache = new Map();

	const first = await got({
		cache,
		responseType: 'json',
		decompress: true,
		retry: {
			limit: 2,
		},
		agent,
	});

	t.true(first.complete);
});

test('revalidated uncompressed responses are retrieved from cache', withServer, async (t, server, got) => {
	let revalidated = false;

	const payload = JSON.stringify([1]);

	server.get('/', (request, response) => {
		if (request.headers['if-none-match'] === 'asdf') {
			revalidated = true;
			response.writeHead(304, {etag: 'asdf'});
			response.end();
		} else {
			response.writeHead(200, {
				etag: 'asdf',
				'cache-control': 'public, max-age=1, s-maxage=1',
				'content-type': 'application/json',
			});
			response.write(payload);
			response.end();
		}
	});

	t.timeout(5000);

	const client = got.extend({cache: new Map(), responseType: 'json'});

	const firstResponse = (await client('')) as unknown as Response<number[]>;
	t.false(revalidated);
	t.deepEqual(firstResponse.body, [1]);
	t.true(firstResponse.complete);

	// eslint-disable-next-line no-promise-executor-return
	await new Promise(resolve => setTimeout(resolve, 3000));

	console.log('max-age has expired, performing second request');

	const secondResponse = (await client('')) as unknown as Response<number[]>;
	t.true(revalidated);
	t.deepEqual(secondResponse.body, [1]);
	t.true(secondResponse.complete); // Fails here.
});

test('revalidated compressed responses are retrieved from cache', withServer, async (t, server, got) => {
	let revalidated = false;

	const payload = JSON.stringify([1]);
	const compressed = await promisify(gzip)(payload);

	server.get('/', (request, response) => {
		if (request.headers['if-none-match'] === 'asdf') {
			revalidated = true;
			response.writeHead(304, {etag: 'asdf'});
			response.end();
		} else {
			response.writeHead(200, {
				etag: 'asdf',
				'cache-control': 'public, max-age=1, s-maxage=1',
				'content-type': 'application/json',
				'content-encoding': 'gzip',
			});
			response.write(compressed);
			response.end();
		}
	});

	t.timeout(5000);

	const client = got.extend({cache: new Map(), responseType: 'json'});

	const firstResponse = (await client('')) as unknown as Response<number[]>;
	t.false(revalidated);
	t.deepEqual(firstResponse.body, [1]);
	t.true(firstResponse.complete);

	// eslint-disable-next-line no-promise-executor-return
	await new Promise(resolve => setTimeout(resolve, 3000));

	console.log('max-age has expired, performing second request (but it will actually hang)');

	const secondResponse = (await client('')) as unknown as Response<number[]>;
	t.true(revalidated);
	t.deepEqual(secondResponse.body, [1]);
	t.true(secondResponse.complete);
});

// eslint-disable-next-line ava/no-skip-test -- Unreliable
test.skip('revalidated uncompressed responses from github are retrieved from cache', async t => {
	const client = got.extend({
		cache: new Map(),
		cacheOptions: {shared: false},
		responseType: 'json',
		headers: {
			'accept-encoding': 'identity',
			...(process.env.GITHUB_TOKEN ? {authorization: `token ${process.env.GITHUB_TOKEN}`} : {}),
		},
	});

	t.timeout(70_000);

	{
		const response = await client('https://api.github.com/repos/octocat/Spoon-Knife');
		t.is((response.body as any).name, 'Spoon-Knife');
		t.true(response.complete);
	}

	// eslint-disable-next-line no-promise-executor-return
	await new Promise(resolve => setTimeout(resolve, 65_000));

	console.log('max-age has expired, performing second request');

	{
		const response = await client('https://api.github.com/repos/octocat/Spoon-Knife');
		t.is((response.body as any).name, 'Spoon-Knife');
		t.true(response.complete); // Fails here.
	}
});

// eslint-disable-next-line ava/no-skip-test -- Unreliable
test.skip('revalidated compressed responses from github are retrieved from cache', async t => {
	const client = got.extend({
		cache: new Map(),
		cacheOptions: {shared: false},
		responseType: 'json',
		headers: process.env.GITHUB_TOKEN ? {authorization: `token ${process.env.GITHUB_TOKEN}`} : {},
	});

	t.timeout(70_000);

	{
		const response = await client('https://api.github.com/repos/octocat/Spoon-Knife');
		t.is((response.body as any).name, 'Spoon-Knife');
		t.true(response.complete);
	}

	// eslint-disable-next-line no-promise-executor-return
	await new Promise(resolve => setTimeout(resolve, 65_000));

	console.log('max-age has expired, performing second request (but it will actually hang)');

	{
		const response = await client('https://api.github.com/repos/octocat/Spoon-Knife');
		t.is((response.body as any).name, 'Spoon-Knife');
		t.true(response.complete);
	}
});

test('QuickLRU works as cache adapter (auto-wrapped)', withServer, async (t, server, got) => {
	server.get('/', cacheEndpoint);

	// Using dynamic import to handle potential missing dependency
	let cacheConstructor;
	try {
		cacheConstructor = (await import('quick-lru')).default;
	} catch {
		t.pass('QuickLRU not available, skipping test');
		return;
	}

	// eslint-disable-next-line new-cap
	const cache = new cacheConstructor({maxSize: 1000});

	// QuickLRU is auto-wrapped by Got to be compatible with StorageAdapter
	const firstResponse = await got({cache: cache as any});
	const secondResponse = await got({cache: cache as any});

	t.is(firstResponse.body, secondResponse.body);
	t.false(firstResponse.isFromCache);
	t.true(secondResponse.isFromCache);
	t.is(cache.size, 1);
});

test('beforeCache hook: returning false prevents caching', withServer, async (t, server, got) => {
	server.get('/', cacheEndpoint);

	const cache = new Map();

	const firstResponse = await got({
		cache,
		hooks: {
			beforeCache: [
				(): false => false,
			],
		},
	});

	const secondResponse = await got({
		cache,
		hooks: {
			beforeCache: [
				(): false => false,
			],
		},
	});

	t.is(cache.size, 0);
	t.not(firstResponse.body, secondResponse.body);
});

test('beforeCache hook: returning void uses default caching', withServer, async (t, server, got) => {
	server.get('/', cacheEndpoint);

	const cache = new Map();

	const firstResponse = await got({
		cache,
		hooks: {
			beforeCache: [
				() => undefined,
			],
		},
	});

	const secondResponse = await got({
		cache,
		hooks: {
			beforeCache: [
				() => undefined,
			],
		},
	});

	t.is(cache.size, 1);
	t.is(firstResponse.body, secondResponse.body);
});

test('beforeCache hook: conditionally prevent caching based on status code', withServer, async (t, server, got) => {
	server.get('/success', cacheEndpoint);
	server.get('/error', (_request, response) => {
		response.setHeader('Cache-Control', 'public, max-age=60');
		response.statusCode = 500;
		response.end('error');
	});

	const cache = new Map();

	const hooks = {
		beforeCache: [
			(response: any) => response.statusCode >= 400 ? false : undefined,
		],
	};

	await got('success', {cache, hooks});
	await got('error', {cache, hooks, throwHttpErrors: false});

	t.is(cache.size, 1);
});

test('beforeCache hook: modify cache-control headers', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.setHeader('Cache-Control', 'no-cache');
		response.end(Date.now().toString());
	});

	const cache = new Map();

	const firstResponse = await got({
		cache,
		hooks: {
			beforeCache: [
				(response: any) => {
					response.headers['cache-control'] = 'public, max-age=3600';
				},
			],
		},
	});

	const secondResponse = await got({
		cache,
		hooks: {
			beforeCache: [
				(response: any) => {
					response.headers['cache-control'] = 'public, max-age=3600';
				},
			],
		},
	});

	t.is(cache.size, 1);
	t.is(firstResponse.body, secondResponse.body);
});

test('beforeCache hook: multiple hooks are executed in order', withServer, async (t, server, got) => {
	server.get('/', cacheEndpoint);

	const cache = new Map();
	const order: number[] = [];

	await got({
		cache,
		hooks: {
			beforeCache: [
				(response: any) => {
					order.push(1);
					response.headers['x-hook-1'] = 'executed';
				},
				(response: any) => {
					order.push(2);
					t.is(response.headers['x-hook-1'], 'executed');
				},
			],
		},
	});

	t.deepEqual(order, [1, 2]);
	t.is(cache.size, 1);
});

test('beforeCache hook: first hook returning false skips remaining hooks', withServer, async (t, server, got) => {
	server.get('/', cacheEndpoint);

	const cache = new Map();
	let secondHookCalled = false;

	await got({
		cache,
		hooks: {
			beforeCache: [
				(): false => false,
				() => {
					secondHookCalled = true;
					return undefined;
				},
			],
		},
	});

	t.false(secondHookCalled);
	t.is(cache.size, 0);
});

test('beforeCache hook: not called when cache option is disabled', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	let hookCalled = false;

	await got({
		hooks: {
			beforeCache: [
				() => {
					hookCalled = true;
					return undefined;
				},
			],
		},
	});

	t.false(hookCalled);
});

test('beforeCache hook: works with extended instances', withServer, async (t, server, got) => {
	server.get('/', cacheEndpoint);

	const cache = new Map();
	const instance = got.extend({
		cache,
		hooks: {
			beforeCache: [
				(response: any) => response.statusCode >= 400 ? false : undefined,
			],
		},
	});

	const firstResponse = await instance('');
	const secondResponse = await instance('');

	t.is(cache.size, 1);
	t.is(firstResponse.body, secondResponse.body);
});

test('beforeCache hook: errors are propagated', withServer, async (t, server, got) => {
	server.get('/', cacheEndpoint);

	const cache = new Map();

	const error = await t.throwsAsync(got({
		cache,
		hooks: {
			beforeCache: [
				() => {
					throw new Error('Hook error message');
				},
			],
		},
	}));

	t.is(error?.message, 'Hook error message');
});

test('beforeCache hook: returning undefined caches the original response correctly', withServer, async (t, server, got) => {
	server.get('/', cacheEndpoint);

	const cache = new Map();

	// First request - hook returns undefined
	const firstResponse = await got({
		cache,
		hooks: {
			beforeCache: [
				() => undefined,
			],
		},
	});

	// Second request - should get cached response
	const secondResponse = await got({
		cache,
		hooks: {
			beforeCache: [
				() => undefined,
			],
		},
	});

	// Verify caching worked correctly
	t.is(cache.size, 1);
	t.is(firstResponse.body, secondResponse.body);
	t.false(firstResponse.isFromCache);
	t.true(secondResponse.isFromCache);
});

test('beforeCache hook: mixed hook results work correctly', withServer, async (t, server, got) => {
	server.get('/', cacheEndpoint);

	const cache = new Map();

	// First request - first hook returns undefined, second hook modifies and returns
	const firstResponse = await got({
		cache,
		hooks: {
			beforeCache: [
				(response: any) => {
					// This hook returns undefined - its mutations take effect
					response.headers['x-ignored'] = 'ignored';
					return undefined;
				},
				(response: any) => {
					// This hook also mutates - all mutations are cached
					response.headers['x-custom'] = 'cached';
				},
			],
		},
	});

	// Second request - should get cached response with modifications from the hook that returned
	const secondResponse = await got({cache});

	t.is(cache.size, 1);
	t.false(firstResponse.isFromCache);
	t.true(secondResponse.isFromCache);
	// The cached response should have the custom header from the hook that returned
	t.is(secondResponse.headers['x-custom'], 'cached');
	// Both mutations are included because mutations work directly
	t.is(secondResponse.headers['x-ignored'], 'ignored');
});

test('beforeCache hook: response body is correctly cached when hook returns undefined', withServer, async (t, server, got) => {
	let requestCount = 0;
	server.get('/', (_request, response) => {
		requestCount++;
		response.setHeader('Cache-Control', 'public, max-age=60');
		response.end(`Response ${requestCount}`);
	});

	const cache = new Map();

	// First request
	const firstResponse = await got({
		cache,
		hooks: {
			beforeCache: [
				() => undefined,
			],
		},
	});

	// Second request - should be from cache
	const secondResponse = await got({
		cache,
		hooks: {
			beforeCache: [
				() => undefined,
			],
		},
	});

	// Verify the body was cached correctly (not corrupted by defensive copy)
	t.is(firstResponse.body, 'Response 1');
	t.is(secondResponse.body, 'Response 1'); // Same body from cache
	t.is(requestCount, 1); // Only one actual request was made
	t.true(secondResponse.isFromCache);
});
```

## File: `test/cookies.ts`
```typescript
import net from 'node:net';
import test from 'ava';
import * as toughCookie from 'tough-cookie';
import delay from 'delay';
import got, {RequestError} from '../source/index.js';
import withServer from './helpers/with-server.js';

test('reads a cookie', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.setHeader('set-cookie', 'hello=world');
		response.end();
	});

	const cookieJar = new toughCookie.CookieJar();

	await got({cookieJar});

	const cookie = cookieJar.getCookiesSync(server.url)[0];
	t.is(cookie?.key, 'hello');
	t.is(cookie?.value, 'world');
});

test('reads multiple cookies', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.setHeader('set-cookie', ['hello=world', 'foo=bar']);
		response.end();
	});

	const cookieJar = new toughCookie.CookieJar();

	await got({cookieJar});

	const [cookieA, cookieB] = cookieJar.getCookiesSync(server.url);
	t.is(cookieA!.key, 'hello');
	t.is(cookieA!.value, 'world');
	t.is(cookieB!.key, 'foo');
	t.is(cookieB!.value, 'bar');
});

test('cookies doesn\'t break on redirects', withServer, async (t, server, got) => {
	server.get('/redirect', (_request, response) => {
		response.setHeader('set-cookie', ['hello=world', 'foo=bar']);
		response.setHeader('location', '/');
		response.statusCode = 302;
		response.end();
	});

	server.get('/', (request, response) => {
		response.end(request.headers.cookie ?? '');
	});

	const cookieJar = new toughCookie.CookieJar();

	const {body} = await got('redirect', {cookieJar});
	t.is(body, 'hello=world; foo=bar');
});

test('throws on invalid cookies', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.setHeader('set-cookie', 'invalid cookie; domain=localhost');
		response.end();
	});

	const cookieJar = new toughCookie.CookieJar();

	await t.throwsAsync(got({cookieJar}), {
		instanceOf: RequestError,
		message: 'Cookie failed to parse',
	});
});

test('does not throw on invalid cookies when options.ignoreInvalidCookies is set', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.setHeader('set-cookie', 'invalid cookie; domain=localhost');
		response.end();
	});

	const cookieJar = new toughCookie.CookieJar();

	await got({
		cookieJar,
		ignoreInvalidCookies: true,
	});

	const cookies = cookieJar.getCookiesSync(server.url);
	t.is(cookies.length, 0);
});

test('catches store errors', async t => {
	const error = 'Some error';
	const cookieJar = new toughCookie.CookieJar({
		findCookies(_domain: any, _path: any, _allowSpecialUseDomain: any, callback: any) {
			callback(new Error(error), []);
		},
		findCookie() {},
		getAllCookies() {},
		putCookie() {},
		removeCookies() {},
		removeCookie() {},
		updateCookie() {},
		synchronous: false,
	} as any);

	await t.throwsAsync(got('https://example.com', {cookieJar}), {
		instanceOf: RequestError,
		message: error,
	});
});

test('overrides options.headers.cookie', withServer, async (t, server, got) => {
	server.get('/redirect', (_request, response) => {
		response.setHeader('set-cookie', ['hello=world', 'foo=bar']);
		response.setHeader('location', '/');
		response.statusCode = 302;
		response.end();
	});

	server.get('/', (request, response) => {
		response.end(request.headers.cookie ?? '');
	});

	const cookieJar = new toughCookie.CookieJar();
	const {body} = await got('redirect', {
		cookieJar,
		headers: {
			cookie: 'a=b',
		},
	});
	t.is(body, 'hello=world; foo=bar');
});

test('no unhandled errors', async t => {
	const server = net.createServer(connection => {
		connection.end('blah');
	}).listen(0);

	const message = 'snap!';

	const options = {
		cookieJar: {
			async setCookie(_rawCookie: string, _url: string) {},
			async getCookieString(_url: string) {
				throw new Error(message);
			},
		},
	};

	await t.throwsAsync(got(`http://127.0.0.1:${(server.address() as net.AddressInfo).port}`, options), {
		instanceOf: RequestError,
		message,
	});
	await delay(500);
	t.pass();

	server.close();
});

test('accepts custom `cookieJar` object', withServer, async (t, server, got) => {
	server.get('/', (request, response) => {
		response.setHeader('set-cookie', ['hello=world']);
		response.end(request.headers.cookie);
	});

	const cookies: Record<string, string> = {};
	const cookieJar = {
		async getCookieString(url: string) {
			t.is(typeof url, 'string');
			return cookies[url] ?? '';
		},

		async setCookie(rawCookie: string, url: string) {
			cookies[url] = rawCookie;
		},
	};

	const first = await got('', {cookieJar});
	const second = await got('', {cookieJar});

	t.is(first.body, '');
	t.is(second.body, 'hello=world');
});

test('throws on invalid `options.cookieJar.setCookie`', async t => {
	await t.throwsAsync(got('https://example.com', {
		cookieJar: {
			// @ts-expect-error Error tests
			setCookie: 123,
		},
	}), {
		instanceOf: RequestError,
		message: 'Expected value which is `Function`, received value of type `number`.',
	});
});

test('throws on invalid `options.cookieJar.getCookieString`', async t => {
	await t.throwsAsync(got('https://example.com', {
		cookieJar: {
			async setCookie() {},
			// @ts-expect-error Error tests
			getCookieString: 123,
		},
	}), {
		instanceOf: RequestError,
		message: 'Expected value which is `Function`, received value of type `number`.',
	});
});

test('cookies are cleared when redirecting to a different hostname (no cookieJar)', withServer, async (t, server1, got) => {
	await withServer.exec(t, async (t, server2) => {
		server1.get('/', (_request, response) => {
			response.writeHead(302, {
				location: `http://localhost:${server2.port}/`,
			});
			response.end();
		});

		server2.get('/', (request, response) => {
			response.end(JSON.stringify({headers: request.headers}));
		});

		const {headers} = await got('', {
			headers: {
				cookie: 'foo=bar',
				'user-agent': 'custom',
			},
		}).json<{headers: Record<string, string | undefined>}>();
		t.is(headers.cookie, undefined);
		t.is(headers['user-agent'], 'custom');
	});
});
```

## File: `test/create.ts`
```typescript
import {Buffer} from 'node:buffer';
import {
	Agent as HttpAgent,
	request as httpRequest,
	type IncomingMessage,
	type RequestOptions,
} from 'node:http';
import test from 'ava';
import is from '@sindresorhus/is';
import type {Handler} from 'express';
import delay from 'delay';
import got, {
	Options,
	type BeforeRequestHook,
	type Headers,
	type Hooks,
	type OptionsInit,
	type RequestFunction,
} from '../source/index.js';
import withServer from './helpers/with-server.js';

const echoHeaders: Handler = (request, response) => {
	request.resume();
	response.end(JSON.stringify(request.headers));
};

test('preserves global defaults', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const globalHeaders = await got('').json();
	const instanceHeaders = await got.extend()('').json();
	t.deepEqual(instanceHeaders, globalHeaders);
});

test('supports instance defaults', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const instance = got.extend({
		headers: {
			'user-agent': 'custom-ua-string',
		},
	});
	const headers = await instance('').json<Headers>();
	t.is(headers['user-agent'], 'custom-ua-string');
});

test('supports invocation overrides', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const instance = got.extend({
		headers: {
			'user-agent': 'custom-ua-string',
		},
	});
	const headers = await instance({
		headers: {
			'user-agent': 'different-ua-string',
		},
	}).json<Headers>();
	t.is(headers['user-agent'], 'different-ua-string');
});

test('carries previous instance defaults', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const instanceA = got.extend({
		headers: {
			'x-foo': 'foo',
		},
	});
	const instanceB = instanceA.extend({
		headers: {
			'x-bar': 'bar',
		},
	});
	const headers = await instanceB('').json<Headers>();
	t.is(headers['x-foo'], 'foo');
	t.is(headers['x-bar'], 'bar');
});

test('custom headers (extend)', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const options = {headers: {unicorn: 'rainbow'}};

	const instance = got.extend(options);
	const headers = await instance('').json<Headers>();
	t.is(headers.unicorn, 'rainbow');
});

test('extend overwrites arrays with a deep clone', t => {
	const x = () => {};
	const y = () => {};

	const beforeRequest = [x];
	const a = got.extend({hooks: {beforeRequest} as unknown as Hooks});
	beforeRequest[0] = y;
	t.deepEqual(a.defaults.options.hooks.beforeRequest, [x] as unknown as BeforeRequestHook[]);
	t.not(a.defaults.options.hooks.beforeRequest, beforeRequest as unknown as BeforeRequestHook[]);
});

test('hooks are merged on got.extend()', t => {
	const hooksA = [() => {}];
	const hooksB = [() => {}];

	const instanceA = got.extend({hooks: {beforeRequest: hooksA}});

	const extended = instanceA.extend({hooks: {beforeRequest: hooksB}});
	t.deepEqual(extended.defaults.options.hooks.beforeRequest, [...hooksA, ...hooksB]);
});

test('custom endpoint with custom headers (extend)', withServer, async (t, server) => {
	server.all('/', echoHeaders);

	const instance = got.extend({headers: {unicorn: 'rainbow'}, prefixUrl: server.url});
	const headers = await instance('').json<Headers>();
	t.is(headers.unicorn, 'rainbow');
	t.not(headers['user-agent'], undefined);
});

test('no tampering with defaults', t => {
	t.throws(() => {
		got.defaults.options.prefixUrl = 'http://google.com';
	});

	t.is(got.defaults.options.prefixUrl, '');
});

test('mixed-case header introspection does not throw on frozen defaults', t => {
	t.notThrows(() => {
		t.is(got.defaults.options.headers['User-Agent'], got.defaults.options.headers['user-agent']);
		Object.hasOwn(got.defaults.options.headers, 'User-Agent');
		Object.getOwnPropertyDescriptor(got.defaults.options.headers, 'User-Agent');
	});
});

test('failed header writes on frozen defaults do not mark headers as explicit', t => {
	t.throws(() => {
		got.defaults.options.headers.foo = 'bar';
	}, {
		instanceOf: TypeError,
	});

	t.false(got.defaults.options.isHeaderExplicitlySet('foo'));
});

test('failed header deletes on frozen defaults do not unmark explicit headers', t => {
	const instance = got.extend({
		headers: {
			foo: 'bar',
		},
	});

	t.true(instance.defaults.options.isHeaderExplicitlySet('foo'));

	t.throws(() => {
		delete instance.defaults.options.headers.foo;
	}, {
		instanceOf: TypeError,
	});

	t.true(instance.defaults.options.isHeaderExplicitlySet('foo'));
});

test('can unset mutable default abort signal', t => {
	const firstController = new AbortController();
	const instance = got.extend({
		mutableDefaults: true,
		signal: firstController.signal,
	});

	t.is(instance.defaults.options.signal, firstController.signal);

	t.notThrows(() => {
		instance.defaults.options.signal = undefined;
	});

	t.is(instance.defaults.options.signal, undefined);
});

test('normalizes https.pfx object arrays for native request options', t => {
	const options = new Options('https://example.com', {
		https: {
			pfx: [{
				buffer: Buffer.from('hello'),
				passphrase: 'world',
			}],
		},
	});

	const nativeRequestOptions = options.createNativeRequestOptions();
	t.deepEqual(nativeRequestOptions.pfx, [{
		buf: Buffer.from('hello'),
		passphrase: 'world',
	}]);
});

test('can set defaults to `new Options(...)`', t => {
	const instance = got.extend({
		mutableDefaults: true,
		followRedirect: false,
	});

	t.notThrows(() => {
		instance.defaults.options = new Options({
			followRedirect: false,
		}, undefined, instance.defaults.options);
	});

	t.false(instance.defaults.options.followRedirect);

	t.notThrows(() => {
		instance.defaults.options = new Options({});
	});

	t.true(instance.defaults.options.followRedirect);
});

test('can set mutable defaults using got.extend', t => {
	const instance = got.extend({
		mutableDefaults: true,
		followRedirect: false,
	});

	t.notThrows(() => {
		instance.defaults.options.followRedirect = true;
	});

	t.true(instance.defaults.options.followRedirect);
});

test('only plain objects are freezed', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const instance = got.extend({
		agent: {
			http: new HttpAgent({keepAlive: true}),
		},
		mutableDefaults: true,
	});

	t.notThrows(() => {
		(instance.defaults.options.agent as any).http.keepAlive = true;
	});
});

test('defaults are cloned on instance creation', t => {
	const options: OptionsInit = {hooks: {beforeRequest: [() => {}]}};
	const instance = got.extend(options);
	const context = {
		foo: {},
	};

	t.notThrows(() => {
		options.context = context;
		options.hooks!.beforeRequest!.splice(0, 1);
	});

	t.not(options.context!.foo, instance.defaults.options.context.foo);
	t.not(options.hooks!.beforeRequest, instance.defaults.options.hooks.beforeRequest);
});

test('ability to pass a custom request method', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	let isCalled = false;

	const request: RequestFunction = (...arguments_: [
		string | URL | RequestOptions,
		(RequestOptions | ((response: IncomingMessage) => void))?,
		((response: IncomingMessage) => void)?,
	]) => {
		isCalled = true;
		// @ts-expect-error Overload error
		return httpRequest(...arguments_);
	};

	const instance = got.extend({request});
	await instance('');

	t.true(isCalled);
});

test('does not include the `request` option in normalized `http` options', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	let isCalled = false;

	const request: RequestFunction = (...arguments_: [
		string | URL | RequestOptions,
		(RequestOptions | ((response: IncomingMessage) => void))?,
		((response: IncomingMessage) => void)?,
	]) => {
		isCalled = true;

		t.false(Reflect.has(arguments_[0] as RequestOptions, 'request'));

		// @ts-expect-error Overload error
		return httpRequest(...arguments_);
	};

	const instance = got.extend({request});
	await instance('');

	t.true(isCalled);
});

test('should pass an options object into an initialization hook after .extend', withServer, async (t, server, got) => {
	t.plan(1);

	server.get('/', echoHeaders);

	let first = true;

	const instance = got.extend({
		hooks: {
			init: [
				options => {
					if (!first) {
						t.deepEqual(options, {});
					}

					first = false;
				},
			],
		},
	});

	await instance('', {});
});

test('handlers detect stream mode via `options.isStream`', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	let promiseModeCount = 0;
	let streamModeCount = 0;

	const instance = got.extend({
		handlers: [
			(options, next) => {
				if (options.isStream) {
					streamModeCount++;
				} else {
					promiseModeCount++;
				}

				return next(options);
			},
		],
	});

	await instance('').text();

	const stream = instance.stream('');
	await new Promise<void>((resolve, reject) => {
		stream.once('end', resolve);
		stream.once('error', reject);
		stream.resume();
	});

	t.is(promiseModeCount, 1);
	t.is(streamModeCount, 1);
});

test('hooks aren\'t overriden when merging options', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	let isCalled = false;
	const instance = got.extend({
		hooks: {
			beforeRequest: [
				() => {
					isCalled = true;
				},
			],
		},
	});

	await instance({});

	t.true(isCalled);
});

test('extend with custom handlers', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const instance = got.extend({
		handlers: [
			(options, next) => {
				options.headers.unicorn = 'rainbow';
				return next(options);
			},
		],
	});
	const headers = await instance('').json<Headers>();
	t.is(headers.unicorn, 'rainbow');
});

test('extend with instances', t => {
	const a = got.extend({prefixUrl: new URL('https://example.com/')});
	const b = got.extend(a);
	t.is(b.defaults.options.prefixUrl.toString(), 'https://example.com/');
});

test('extend with a chain', t => {
	const a = got.extend({prefixUrl: 'https://example.com/'});
	const b = got.extend(a, {headers: {foo: 'bar'}});
	t.is(b.defaults.options.prefixUrl.toString(), 'https://example.com/');
	t.is(b.defaults.options.headers.foo, 'bar');
});

test('async handlers', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const instance = got.extend({
		handlers: [
			(options, next) => {
				if (options.isStream) {
					return next(options);
				}

				return (async () => {
					const result = await next(options);
					// @ts-expect-error Manual tests
					result.modified = true;

					return result;
				})();
			},
		],
	});

	const promise = instance('');
	t.true(is.function(promise.json));
	t.true(is.function(promise.once));

	let responseEventCount = 0;
	const returnedPromise = promise.once('response', () => {
		responseEventCount++;
	});
	t.is(returnedPromise, promise);

	// @ts-expect-error Manual tests
	t.true((await promise).modified);
	t.is(responseEventCount, 1);
});

test('async handlers can throw', async t => {
	const message = 'meh';

	const instance = got.extend({
		handlers: [
			async () => {
				throw new Error(message);
			},
		],
	});

	await t.throwsAsync(instance('https://example.com'), {
		instanceOf: Error,
		message,
	});
});

test('setting dnsCache to true points to global cache', t => {
	const a = got.extend({
		dnsCache: true,
	});

	const b = got.extend({
		dnsCache: true,
	});

	t.is(a.defaults.options.dnsCache, b.defaults.options.dnsCache);
});

test('waits for handlers to finish', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const instance = got.extend({
		handlers: [
			async (options, next) => {
				await delay(1000);
				return next(options);
			},
			async (options, next) => {
				options.headers.foo = 'bar';
				return next(options);
			},
		],
	});

	const {foo} = await instance('').json<{foo: 'bar'}>();
	t.is(foo, 'bar');
});

test('does not leak per-request options into extended defaults', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const instance = got.extend({
		mutableDefaults: true,
	});

	await instance('', {
		headers: {
			'x-transient': 'present-once',
		},
	});

	const extendedInstance = instance.extend({});
	const headers = await extendedInstance('').json<Record<string, string>>();

	t.is(headers['x-transient'], undefined);
});

test('extend clones searchParams object', t => {
	const searchParameters = {foo: 'bar', page: '1'};
	const instance = got.extend({searchParams: searchParameters});

	// Mutate the original
	searchParameters.foo = 'changed';
	searchParameters.page = '999';

	// Instance should have the original values (converted to URLSearchParams)
	const instanceParameters = instance.defaults.options.searchParams as URLSearchParams;
	t.is(instanceParameters.get('foo'), 'bar');
	t.is(instanceParameters.get('page'), '1');
});

test('extend clones URLSearchParams instance', t => {
	const searchParameters = new URLSearchParams({foo: 'bar', page: '1'});
	const instance = got.extend({searchParams: searchParameters});

	// Mutate the original
	searchParameters.set('foo', 'changed');
	searchParameters.set('page', '999');

	// Instance should have the original values
	const instanceParameters = instance.defaults.options.searchParams as URLSearchParams;
	t.is(instanceParameters.get('foo'), 'bar');
	t.is(instanceParameters.get('page'), '1');
	t.not(instanceParameters, searchParameters);
});

test('extend handles string searchParams', t => {
	const searchParameters = 'foo=bar&page=1';
	const instance = got.extend({searchParams: searchParameters});

	// String gets converted to URLSearchParams
	const instanceParameters = instance.defaults.options.searchParams as URLSearchParams;
	t.is(instanceParameters.get('foo'), 'bar');
	t.is(instanceParameters.get('page'), '1');
});

test('extended instances carry searchParams', t => {
	const instanceA = got.extend({
		searchParams: {foo: 'bar'},
	});

	const instanceB = instanceA.extend({
		searchParams: {page: '1'},
	});

	const instanceParametersB = instanceB.defaults.options.searchParams as URLSearchParams;
	t.is(instanceParametersB.get('foo'), 'bar');
	t.is(instanceParametersB.get('page'), '1');
});

test('extend creates independent searchParams copies', t => {
	const searchParameters = {foo: 'bar'};
	const instanceA = got.extend({searchParams: searchParameters, mutableDefaults: true});
	const instanceB = got.extend({searchParams: searchParameters, mutableDefaults: true});

	// Modify instanceA's searchParams
	(instanceA.defaults.options.searchParams as URLSearchParams).set('foo', 'modified');

	// InstanceB should be unaffected
	t.is((instanceB.defaults.options.searchParams as URLSearchParams).get('foo'), 'bar');
});

test('got.extend() with responseType works at runtime', withServer, async (t, server) => {
	server.get('/json', (_request, response) => {
		response.writeHead(200, {'content-type': 'application/json'});
		response.end('{"data": "test"}');
	});

	server.get('/buffer', (_request, response) => {
		response.writeHead(200, {'content-type': 'application/octet-stream'});
		response.end(Buffer.from('binary'));
	});

	// Test responseType: 'json' works
	const jsonClient = got.extend({
		prefixUrl: server.url,
		responseType: 'json',
	});

	const jsonResponse = await jsonClient('json');
	t.deepEqual(jsonResponse.body, {data: 'test'});

	// Test responseType: 'buffer' works
	const bufferClient = got.extend({
		prefixUrl: server.url,
		responseType: 'buffer',
	});

	const bufferResponse = await bufferClient('buffer');
	t.true(bufferResponse.body instanceof Uint8Array);
	t.false(Buffer.isBuffer(bufferResponse.body));
	t.is(Buffer.from(bufferResponse.body).toString(), 'binary');

	// Test resolveBodyOnly works with extended responseType
	const jsonBodyClient = got.extend({
		prefixUrl: server.url,
		responseType: 'json',
		resolveBodyOnly: true,
	});

	const jsonBody = await jsonBodyClient('json');
	t.deepEqual(jsonBody, {data: 'test'});
});
```

## File: `test/diagnostics-channel.ts`
```typescript
import diagnosticsChannel from 'node:diagnostics_channel';
import test from 'ava';
import type {Handler} from 'express';
import withServer from './helpers/with-server.js';

const echoHeaders: Handler = (request, response) => {
	request.resume();
	response.end(JSON.stringify(request.headers));
};

test('diagnostics channel - request:create event', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const events: any[] = [];
	const channel = diagnosticsChannel.channel('got:request:create');
	const testUrl = `${server.url}/`;

	const handler = (message: any) => {
		if (message.url === testUrl) {
			events.push(message);
		}
	};

	channel.subscribe(handler);

	try {
		await got('');

		t.is(events.length, 1);
		const event = events[0];
		t.truthy(event.requestId);
		t.is(typeof event.url, 'string');
		t.is(event.method, 'GET');
	} finally {
		channel.unsubscribe(handler);
	}
});

test('diagnostics channel - request:start event', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const events: any[] = [];
	const channel = diagnosticsChannel.channel('got:request:start');
	const testUrl = `${server.url}/`;

	const handler = (message: any) => {
		if (message.url === testUrl) {
			events.push(message);
		}
	};

	channel.subscribe(handler);

	try {
		await got('');

		t.is(events.length, 1);
		const event = events[0];
		t.truthy(event.requestId);
		t.is(typeof event.url, 'string');
		t.is(event.method, 'GET');
		t.truthy(event.headers);
	} finally {
		channel.unsubscribe(handler);
	}
});

test('diagnostics channel - request URLs are sanitized', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const createEvents: any[] = [];
	const startEvents: any[] = [];
	const createChannel = diagnosticsChannel.channel('got:request:create');
	const startChannel = diagnosticsChannel.channel('got:request:start');

	const createHandler = (message: any) => {
		if (message.method === 'GET') {
			createEvents.push(message);
		}
	};

	const startHandler = (message: any) => {
		if (message.method === 'GET') {
			startEvents.push(message);
		}
	};

	createChannel.subscribe(createHandler);
	startChannel.subscribe(startHandler);

	try {
		const url = new URL(server.url);
		url.username = 'user';
		url.password = 'secret';
		const expectedUrl = `${server.url}/`;

		await got(url);

		t.true(createEvents.length > 0);
		t.true(startEvents.length > 0);
		t.true(createEvents.some(event => event.url === expectedUrl));
		t.true(startEvents.some(event => event.url === expectedUrl));
		t.false(createEvents.some(event => event.url.includes('user')) || createEvents.some(event => event.url.includes('secret')));
		t.false(startEvents.some(event => event.url.includes('user')) || startEvents.some(event => event.url.includes('secret')));
	} finally {
		createChannel.unsubscribe(createHandler);
		startChannel.unsubscribe(startHandler);
	}
});

test('diagnostics channel - response:start event', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const events: any[] = [];
	const channel = diagnosticsChannel.channel('got:response:start');
	const testUrl = `${server.url}/`;

	const handler = (message: any) => {
		if (message.url === testUrl) {
			events.push(message);
		}
	};

	channel.subscribe(handler);

	try {
		await got('');

		t.is(events.length, 1);
		const event = events[0];
		t.truthy(event.requestId);
		t.is(event.statusCode, 200);
		t.truthy(event.headers);
		t.is(typeof event.url, 'string');
		t.is(event.isFromCache, false);
	} finally {
		channel.unsubscribe(handler);
	}
});

test('diagnostics channel - response:end event', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const events: any[] = [];
	const channel = diagnosticsChannel.channel('got:response:end');
	const testUrl = `${server.url}/`;

	const handler = (message: any) => {
		if (message.url === testUrl) {
			events.push(message);
		}
	};

	channel.subscribe(handler);

	try {
		await got('');

		t.is(events.length, 1);
		const event = events[0];
		t.truthy(event.requestId);
		t.is(event.statusCode, 200);
		t.is(typeof event.bodySize, 'number');
		t.truthy(event.timings);
	} finally {
		channel.unsubscribe(handler);
	}
});

test('diagnostics channel - request:error event', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 500;
		response.end('error');
	});

	const events: any[] = [];
	const channel = diagnosticsChannel.channel('got:request:error');
	const testUrl = `${server.url}/`;

	const handler = (message: any) => {
		if (message.url === testUrl) {
			events.push(message);
		}
	};

	channel.subscribe(handler);

	try {
		await t.throwsAsync(got(''));

		t.is(events.length, 1);
		const event = events[0];
		t.truthy(event.requestId);
		t.truthy(event.error);
		t.is(typeof event.url, 'string');
	} finally {
		channel.unsubscribe(handler);
	}
});

test('diagnostics channel - request:error URL is sanitized', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 500;
		response.end('error');
	});

	const events: any[] = [];
	const channel = diagnosticsChannel.channel('got:request:error');

	const handler = (message: any) => {
		events.push(message);
	};

	channel.subscribe(handler);

	try {
		const url = new URL(server.url);
		url.username = 'user';
		url.password = 'secret';

		await t.throwsAsync(got(url, {
			retry: {
				limit: 0,
			},
		}));

		t.is(events.length, 1);
		t.is(events[0].url, `${server.url}/`);
		t.false(events[0].url.includes('user'));
		t.false(events[0].url.includes('secret'));
	} finally {
		channel.unsubscribe(handler);
	}
});

test('diagnostics channel - request:retry event', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 500;
		response.end('error');
	});

	const events: any[] = [];
	const retryChannel = diagnosticsChannel.channel('got:request:retry');
	const createChannel = diagnosticsChannel.channel('got:request:create');
	const testUrl = `${server.url}/`;
	let testRequestId: string | undefined;

	const createHandler = (message: any) => {
		if (message.url === testUrl) {
			testRequestId = message.requestId;
		}
	};

	const retryHandler = (message: any) => {
		if (testRequestId && message.requestId === testRequestId) {
			events.push(message);
		}
	};

	createChannel.subscribe(createHandler);
	retryChannel.subscribe(retryHandler);

	try {
		await t.throwsAsync(got('', {
			retry: {
				limit: 2,
			},
		}));

		t.is(events.length, 2);
		t.is(events[0].retryCount, 1);
		t.is(events[1].retryCount, 2);
		t.truthy(events[0].error);
		t.truthy(events[1].error);
		t.is(typeof events[0].delay, 'number');
		t.is(typeof events[1].delay, 'number');
	} finally {
		createChannel.unsubscribe(createHandler);
		retryChannel.unsubscribe(retryHandler);
	}
});

test('diagnostics channel - response:redirect event', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.writeHead(302, {
			location: '/redirect',
		});
		response.end();
	});

	server.get('/redirect', echoHeaders);

	const events: any[] = [];
	const channel = diagnosticsChannel.channel('got:response:redirect');
	const testUrl = `${server.url}/`;

	const handler = (message: any) => {
		if (message.fromUrl === testUrl) {
			events.push(message);
		}
	};

	channel.subscribe(handler);

	try {
		await got('');

		t.is(events.length, 1);
		const event = events[0];
		t.truthy(event.requestId);
		t.is(typeof event.fromUrl, 'string');
		t.is(typeof event.toUrl, 'string');
		t.is(event.statusCode, 302);
	} finally {
		channel.unsubscribe(handler);
	}
});

test('diagnostics channel - all events have consistent requestId', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const requestIds = new Set<string>();
	const handlers: Array<{channel: any; handler: (message: any) => void}> = [];
	const testUrl = `${server.url}/`;

	const channels = [
		'got:request:create',
		'got:request:start',
		'got:response:start',
		'got:response:end',
	];

	for (const channelName of channels) {
		const channel = diagnosticsChannel.channel(channelName);
		const handler = (message: any) => {
			if (message.url === testUrl) {
				requestIds.add(message.requestId);
			}
		};

		channel.subscribe(handler);
		handlers.push({channel, handler});
	}

	try {
		await got('');

		t.is(requestIds.size, 1);
	} finally {
		for (const {channel, handler} of handlers) {
			channel.unsubscribe(handler);
		}
	}
});

test('diagnostics channel - cache hit detection', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.setHeader('cache-control', 'public, max-age=60');
		response.end('ok');
	});

	const events: any[] = [];
	const channel = diagnosticsChannel.channel('got:response:start');
	const testUrl = `${server.url}/`;

	const handler = (message: any) => {
		if (message.url === testUrl) {
			events.push(message);
		}
	};

	channel.subscribe(handler);

	try {
		const cache = new Map();
		await got('', {cache});
		await got('', {cache});

		t.is(events.length, 2);
		t.is(events[0].isFromCache, false);
		t.is(events[1].isFromCache, true);
	} finally {
		channel.unsubscribe(handler);
	}
});

test('diagnostics channel - no overhead when no subscribers', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	// Just verify it works without subscribers
	await got('');

	t.pass();
});
```

## File: `test/early-307-redirects.ts`
```typescript
import {Buffer} from 'node:buffer';
import {Agent as HttpAgent, request as httpRequest, type ClientRequest} from 'node:http';
import {setTimeout as delay} from 'node:timers/promises';
import test from 'ava';
import type {Handler} from 'express';
import withServer from './helpers/with-server.js';

const early307RedirectHandler = (location: string): Handler => (request, response) => {
	let redirected = false;

	request.on('error', () => {});
	request.on('data', () => {
		if (redirected) {
			return;
		}

		redirected = true;
		response.writeHead(307, {
			location,
		});
		response.end();
	});

	request.resume();
};

/*
Intercepts write callbacks on a request and delays them until after the response event, then calls them with the injected error. This simulates a delayed write error (EPIPE, ECONNRESET, etc.) arriving after the server has already sent a response.
*/
const injectWriteErrorAfterResponse = (request: ClientRequest, writeError: NodeJS.ErrnoException, onInjected?: () => void): void => {
	let responseReceived = false;
	let errorInjected = false;
	const pendingCallbacks: Array<(error: Error | undefined) => void> = [];
	const originalWrite = request.write.bind(request);

	const flushPendingWithError = () => {
		errorInjected = true;
		onInjected?.();

		const callbacks = [...pendingCallbacks];
		pendingCallbacks.length = 0;

		setTimeout(() => {
			for (const callback of callbacks) {
				callback(writeError);
			}
		}, 0);
	};

	request.once('response', () => {
		responseReceived = true;
		if (!errorInjected) {
			flushPendingWithError();
		}
	});

	// eslint-disable-next-line @typescript-eslint/no-restricted-types
	const wrapCallback = (callback: (error: Error | null | undefined) => void): (error: Error | null | undefined) => void =>
		error => {
			// After injection, pass through errors as-is.
			if (errorInjected) {
				callback(error);
				return;
			}

			// If the real write errored, forward it immediately.
			if (error !== undefined && error !== null) {
				callback(error);
				return;
			}

			// If response already arrived, inject the error now.
			if (responseReceived) {
				flushPendingWithError();
				callback(writeError);
				return;
			}

			// Queue the callback to be flushed with the injected error when the response arrives.
			pendingCallbacks.push(callback);
		};

	// eslint-disable-next-line @typescript-eslint/no-restricted-types
	request.write = ((chunk: any, encoding: BufferEncoding | undefined, callback?: (error: Error | null | undefined) => void) => {
		if (typeof encoding === 'function') {
			callback = encoding;
			encoding = undefined;
		}

		if (typeof callback !== 'function') {
			return encoding === undefined ? originalWrite(chunk) : originalWrite(chunk, encoding);
		}

		return encoding === undefined
			? originalWrite(chunk, wrapCallback(callback))
			: originalWrite(chunk, encoding, wrapCallback(callback));
	}) as typeof request.write;
};

/*
Injects a transient write callback error before the request receives a response.

This simulates the race where chunk writing fails before redirect handling marks the original request stale.
*/
const injectWriteErrorBeforeResponse = (request: ClientRequest, writeError: NodeJS.ErrnoException, onInjected?: () => void): void => {
	let injected = false;
	const originalWrite = request.write.bind(request);

	// eslint-disable-next-line @typescript-eslint/no-restricted-types
	request.write = ((chunk: any, encoding: BufferEncoding | undefined, callback?: (error: Error | null | undefined) => void) => {
		if (typeof encoding === 'function') {
			callback = encoding;
			encoding = undefined;
		}

		if (!injected && typeof callback === 'function') {
			injected = true;
			const result = encoding === undefined ? originalWrite(chunk) : originalWrite(chunk, encoding);
			onInjected?.();
			callback(writeError);
			return result;
		}

		if (encoding === undefined) {
			return callback ? originalWrite(chunk, callback) : originalWrite(chunk);
		}

		return callback ? originalWrite(chunk, encoding, callback) : originalWrite(chunk, encoding);
	}) as typeof request.write;
};

test('large body is preserved on early 307 redirect', withServer, async (t, server, got) => {
	const requestBody = Buffer.alloc(1024 * 1024 * 4, 'b');
	const agent = new HttpAgent({
		keepAlive: true,
		maxSockets: 1,
	});
	const requests: ClientRequest[] = [];

	server.post('/redirect-early', early307RedirectHandler('/target-early'));

	server.post('/target-early', async (request, response) => {
		const receivedChunks: Uint8Array[] = [];

		for await (const receivedChunk of request) {
			receivedChunks.push(Buffer.from(receivedChunk));
		}

		const receivedBody = Buffer.concat(receivedChunks);

		t.true(receivedBody.equals(requestBody));
		response.end('ok');
	});

	try {
		const {body} = await got.post('redirect-early', {
			body: requestBody,
			retry: {
				limit: 0,
			},
			agent: {
				http: agent,
			},
		}).on('request', request => {
			requests.push(request);
		});

		t.is(body, 'ok');
		t.is(requests.length, 2);

		const staleRequest = requests[0];
		if (!staleRequest) {
			throw new Error('Expected a stale redirected request');
		}

		if (!staleRequest.destroyed && !staleRequest.writableEnded) {
			await Promise.race([
				new Promise<void>(resolve => {
					staleRequest.once('finish', resolve);
					staleRequest.once('close', resolve);
				}),
				(async () => {
					await delay(1000);
					throw new Error('Stale redirected request was not finalized');
				})(),
			]);
		}

		t.true(staleRequest.destroyed || staleRequest.writableEnded);
	} finally {
		agent.destroy();
	}
});

test('early 307 redirect emits final upload progress event', withServer, async (t, server, got) => {
	const requestBody = Buffer.alloc(1024 * 1024 * 4, 'c');
	const events: Array<{percent: number; transferred: number; total?: number}> = [];

	server.post('/redirect-early-progress', early307RedirectHandler('/target-early-progress'));

	server.post('/target-early-progress', async (request, response) => {
		for await (const receivedChunk of request) {
			void receivedChunk;
		}

		response.end('ok');
	});

	const {body} = await got.post('redirect-early-progress', {
		body: requestBody,
		retry: {
			limit: 0,
		},
	}).on('uploadProgress', event => {
		events.push({
			percent: event.percent,
			transferred: event.transferred,
			total: event.total,
		});
	});

	t.is(body, 'ok');
	t.true(events.length > 1);

	const finalEvent = events.at(-1);
	t.truthy(finalEvent);
	t.is(finalEvent?.percent, 1);
	t.is(finalEvent?.transferred, requestBody.byteLength);
	t.is(finalEvent?.total, requestBody.byteLength);
});

test('early 307 redirect emits final upload progress event for small body', withServer, async (t, server, got) => {
	const requestBody = Buffer.alloc(32, 'd');
	const events: Array<{percent: number; transferred: number; total?: number}> = [];

	server.post('/redirect-early-progress-small', early307RedirectHandler('/target-early-progress-small'));

	server.post('/target-early-progress-small', async (request, response) => {
		for await (const receivedChunk of request) {
			void receivedChunk;
		}

		response.end('ok');
	});

	const {body} = await got.post('redirect-early-progress-small', {
		body: requestBody,
		retry: {
			limit: 0,
		},
	}).on('uploadProgress', event => {
		events.push({
			percent: event.percent,
			transferred: event.transferred,
			total: event.total,
		});
	});

	t.is(body, 'ok');
	t.true(events.length > 1);

	const finalEvent = events.at(-1);
	t.truthy(finalEvent);
	t.is(finalEvent?.percent, 1);
	t.is(finalEvent?.transferred, requestBody.byteLength);
	t.is(finalEvent?.total, requestBody.byteLength);
});

test('early 307 redirect preserves upload progress totals', withServer, async (t, server, got) => {
	const requestBody = Buffer.alloc(1024 * 1024 * 4, 'e');
	const events: Array<{percent: number; transferred: number; total: number | undefined}> = [];
	const requestMethods: string[] = [];

	server.post('/redirect-early-progress-preserve', early307RedirectHandler('/target-early-progress-preserve'));

	server.post('/target-early-progress-preserve', async (request, response) => {
		for await (const receivedChunk of request) {
			void receivedChunk;
		}

		response.end('ok');
	});

	const {body} = await got.post('redirect-early-progress-preserve', {
		body: requestBody,
		retry: {
			limit: 0,
		},
	}).on('request', request => {
		requestMethods.push(request.method ?? '');
	}).on('uploadProgress', event => {
		events.push({
			percent: event.percent,
			transferred: event.transferred,
			total: event.total,
		});
	});

	t.is(body, 'ok');
	t.deepEqual(requestMethods, ['POST', 'POST']);

	let redirectedStartEventIndex = -1;
	for (let index = events.length - 1; index >= 0; index--) {
		if (events[index]!.transferred === 0) {
			redirectedStartEventIndex = index;
			break;
		}
	}

	t.true(redirectedStartEventIndex >= 0);

	const redirectedStartEvent = events[redirectedStartEventIndex]!;
	t.is(redirectedStartEvent.total, requestBody.byteLength);

	const redirectedProgressEvents = events.slice(redirectedStartEventIndex + 1).filter(event => event.transferred > 0 && event.transferred < requestBody.byteLength);
	t.true(redirectedProgressEvents.length > 0);

	for (const event of redirectedProgressEvents) {
		t.is(event.total, requestBody.byteLength);
		t.true(event.percent > 0);
		t.true(event.percent < 1);
	}
});

test('early 307 redirect finalizes writable side for buffered body', withServer, async (t, server, got) => {
	const requestBody = Buffer.alloc(1024 * 1024 * 4, 'f');

	server.post('/redirect-early-writable-finish', early307RedirectHandler('/target-early-writable-finish'));

	server.post('/target-early-writable-finish', async (request, response) => {
		for await (const receivedChunk of request) {
			void receivedChunk;
		}

		response.end('ok');
	});

	const requestStream = got.stream.post('redirect-early-writable-finish', {
		body: requestBody,
		retry: {
			limit: 0,
		},
	});

	let finished = false;
	requestStream.once('finish', () => {
		finished = true;
	});

	let responseBody = '';
	for await (const chunk of requestStream) {
		responseBody += Buffer.isBuffer(chunk) ? chunk.toString() : String(chunk);
	}

	if (!finished) {
		await Promise.race([
			new Promise<void>(resolve => {
				requestStream.once('finish', resolve);
			}),
			(async () => {
				await delay(1000);
				throw new Error('Redirected buffered stream did not emit finish');
			})(),
		]);
	}

	t.is(responseBody, 'ok');
	t.true(requestStream.writableFinished);
});

test('early 307 redirect finalizes writable side when transient chunk write callback errors before stale mark', withServer, async (t, server, got) => {
	const requestBody = Buffer.alloc(1024 * 1024 * 4, 'l');
	const requests: ClientRequest[] = [];
	const writeError = new Error('write EPIPE') as NodeJS.ErrnoException;
	let isFirstRequest = true;
	let injectedError = false;
	writeError.code = 'EPIPE';

	server.post('/redirect-early-transient-finish', early307RedirectHandler('/target-early-transient-finish'));

	server.post('/target-early-transient-finish', async (request, response) => {
		for await (const receivedChunk of request) {
			void receivedChunk;
		}

		response.end('ok');
	});

	const requestFunction = (...arguments_: Parameters<typeof httpRequest>): ClientRequest => {
		const request = httpRequest(...arguments_);
		requests.push(request);

		if (isFirstRequest) {
			isFirstRequest = false;
			injectWriteErrorBeforeResponse(request, writeError, () => {
				injectedError = true;
			});
		}

		return request;
	};

	const requestStream = got.stream.post('redirect-early-transient-finish', {
		body: requestBody,
		retry: {
			limit: 0,
		},
		request: requestFunction,
	});

	let responseBody = '';
	for await (const responseChunk of requestStream) {
		responseBody += Buffer.isBuffer(responseChunk) ? responseChunk.toString() : String(responseChunk);
	}

	if (!requestStream.writableFinished) {
		await Promise.race([
			new Promise<void>(resolve => {
				requestStream.once('finish', resolve);
			}),
			(async () => {
				await delay(1000);
				throw new Error('Redirected buffered stream did not emit finish after transient write callback error');
			})(),
		]);
	}

	t.is(responseBody, 'ok');
	t.true(injectedError);
	t.is(requests.length, 2);
	t.true(requestStream.writableFinished);
});

test('early 307 redirect does not prematurely end redirected request while replaying body', withServer, async (t, server, got) => {
	const requestBody = Buffer.alloc(1024 * 1024 * 4, 'g');
	let redirectedRequestAborted = false;
	let redirectedBodyLength = 0;

	server.post('/redirect-early-race', early307RedirectHandler('/target-early-race'));

	server.post('/target-early-race', async (request, response) => {
		request.on('aborted', () => {
			redirectedRequestAborted = true;
		});

		const receivedChunks: Uint8Array[] = [];
		for await (const receivedChunk of request) {
			receivedChunks.push(Buffer.from(receivedChunk));
		}

		redirectedBodyLength = Buffer.concat(receivedChunks).byteLength;
		response.end('ok');
	});

	const {body} = await got.post('redirect-early-race', {
		body: requestBody,
		retry: {
			limit: 0,
		},
	}).on('request', request => {
		const originalWrite = request.write.bind(request);

		request.write = ((chunk: any, encoding?: any, callback?: any) => {
			if (typeof encoding === 'function') {
				callback = encoding;
				encoding = undefined;
			}

			if (typeof callback === 'function') {
				const originalCallback = callback;
				callback = (error?: Error) => {
					setTimeout(() => {
						originalCallback(error);
					}, 25);
				};
			}

			return originalWrite(chunk, encoding, callback);
		}) as typeof request.write;
	});

	t.is(body, 'ok');
	t.false(redirectedRequestAborted);
	t.is(redirectedBodyLength, requestBody.byteLength);
});

test('early 307 redirect preserves body when beforeRedirect hook is delayed', withServer, async (t, server, got) => {
	const requestBody = Buffer.alloc(1024 * 1024 * 2, 'h');

	server.post('/redirect-early-delayed-before-redirect', early307RedirectHandler('/target-early-delayed-before-redirect'));

	server.post('/target-early-delayed-before-redirect', async (request, response) => {
		const receivedChunks: Uint8Array[] = [];
		for await (const receivedChunk of request) {
			receivedChunks.push(Buffer.from(receivedChunk));
		}

		const receivedBody = Buffer.concat(receivedChunks);
		t.true(receivedBody.equals(requestBody));
		response.end('ok');
	});

	const {body} = await got.post('redirect-early-delayed-before-redirect', {
		body: requestBody,
		retry: {
			limit: 0,
		},
		hooks: {
			beforeRedirect: [
				async () => {
					await delay(50);
				},
			],
		},
	});

	t.is(body, 'ok');
});

test('early 307 redirect does not emit stale original request write error', withServer, async (t, server, got) => {
	const requestBody = Buffer.alloc(1024 * 1024 * 2, 'i');
	const requestErrors: Error[] = [];
	const requests: ClientRequest[] = [];

	server.post('/redirect-early-stale-error', early307RedirectHandler('/target-early-stale-error'));

	server.post('/target-early-stale-error', async (request, response) => {
		for await (const receivedChunk of request) {
			void receivedChunk;
		}

		response.end('ok');
	});

	const {body} = await got.post('redirect-early-stale-error', {
		body: requestBody,
		retry: {
			limit: 0,
		},
	}).on('request', request => {
		requests.push(request);
		request.once('error', error => {
			requestErrors.push(error);
		});
	});

	t.is(body, 'ok');
	t.is(requests.length, 2);

	const originalRequest = requests[0];
	t.truthy(originalRequest);
	t.false(requestErrors.some(error => {
		const {code} = error as NodeJS.ErrnoException;
		return code === 'EPIPE' || code === 'ECONNRESET' || code === 'ECANCELED';
	}));
});

const staleWriteErrorCases = [
	{
		name: 'EPIPE',
		code: 'EPIPE',
		redirectPath: '/redirect-early-injected-transient',
		targetPath: '/target-early-injected-transient',
	},
	{
		name: 'ECONNRESET',
		code: 'ECONNRESET',
		redirectPath: '/redirect-early-injected-connreset',
		targetPath: '/target-early-injected-connreset',
	},
	{
		name: 'non-transient',
		code: 'EACCES',
		redirectPath: '/redirect-early-injected-non-transient',
		targetPath: '/target-early-injected-non-transient',
	},
] as const;

for (const staleWriteErrorCase of staleWriteErrorCases) {
	test(`early 307 redirect ignores delayed stale ${staleWriteErrorCase.name} write error`, withServer, async (t, server, got) => {
		const requestBody = Buffer.alloc(1024 * 1024 * 2, 'k');
		const requests: ClientRequest[] = [];
		const requestErrors: Error[] = [];
		let injectedError = false;

		server.post(staleWriteErrorCase.redirectPath, early307RedirectHandler(staleWriteErrorCase.targetPath));

		server.post(staleWriteErrorCase.targetPath, async (request, response) => {
			for await (const receivedChunk of request) {
				void receivedChunk;
			}

			response.end('ok');
		});

		const staleError = new Error('stale request write error') as NodeJS.ErrnoException;
		staleError.code = staleWriteErrorCase.code;

		const {body} = await got.post(staleWriteErrorCase.redirectPath.slice(1), {
			body: requestBody,
			retry: {
				limit: 0,
			},
		}).on('request', request => {
			requests.push(request);

			request.on('error', error => {
				requestErrors.push(error);
			});

			if (requests.length === 1) {
				injectWriteErrorAfterResponse(request, staleError, () => {
					injectedError = true;
				});
			}
		});

		t.is(body, 'ok');
		t.is(requests.length, 2);
		t.true(injectedError);
		t.is(requestErrors.length, 0);
	});
}

test('early 307 redirect final upload progress remains complete with delayed beforeRedirect', withServer, async (t, server, got) => {
	const requestBody = Buffer.alloc(1024 * 1024 * 2, 'j');
	const events: Array<{percent: number; transferred: number; total?: number}> = [];

	server.post('/redirect-early-progress-delayed-before-redirect', early307RedirectHandler('/target-early-progress-delayed-before-redirect'));

	server.post('/target-early-progress-delayed-before-redirect', async (request, response) => {
		for await (const receivedChunk of request) {
			void receivedChunk;
		}

		response.end('ok');
	});

	const {body} = await got.post('redirect-early-progress-delayed-before-redirect', {
		body: requestBody,
		retry: {
			limit: 0,
		},
		hooks: {
			beforeRedirect: [
				async () => {
					await delay(50);
				},
			],
		},
	}).on('uploadProgress', event => {
		events.push({
			percent: event.percent,
			transferred: event.transferred,
			total: event.total,
		});
	});

	t.is(body, 'ok');
	t.true(events.length > 1);

	const finalEvent = events.at(-1);
	t.truthy(finalEvent);
	t.is(finalEvent?.percent, 1);
	t.is(finalEvent?.transferred, requestBody.byteLength);
	t.is(finalEvent?.total, requestBody.byteLength);
});
```

## File: `test/encoding.ts`
```typescript
import {Buffer} from 'node:buffer';
import test from 'ava';
import withServer from './helpers/with-server.js';

test('encoding works with json', withServer, async (t, server, got) => {
	const json = {data: 'é'};

	server.get('/', (_request, response) => {
		response.set('Content-Type', 'application-json');
		response.send(Buffer.from(JSON.stringify(json), 'latin1'));
	});

	const response = await got('', {
		encoding: 'latin1',
		responseType: 'json',
	});

	t.deepEqual(response.body, json);
});
```

## File: `test/error.ts`
```typescript
import {Buffer} from 'node:buffer';
import {promisify} from 'node:util';
import net from 'node:net';
import http from 'node:http';
import stream from 'node:stream';
import {pipeline as streamPipeline} from 'node:stream/promises';
import {Agent} from 'node:https';
import test from 'ava';
import getStream from 'get-stream';
import is from '@sindresorhus/is';
import got, {RequestError, HTTPError, TimeoutError} from '../source/index.js';
import withServer from './helpers/with-server.js';
import invalidUrl from './helpers/invalid-url.js';

test('properties', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 404;
		response.end('not');
	});

	const url = new URL(server.url);

	const error = (await t.throwsAsync<HTTPError<string>>(got('')));
	t.truthy(error);
	t.truthy(error.response);
	t.truthy(error.options);
	t.true(Object.prototype.propertyIsEnumerable.call(error, 'options'));
	t.false(Object.prototype.propertyIsEnumerable.call(error, 'response'));
	t.is(error.code, 'ERR_NON_2XX_3XX_RESPONSE');
	t.regex(error.message, /^Request failed with status code 404 \(Not Found\): GET http:\/\/localhost:\d+\/$/);
	t.deepEqual(error.options.url, url);
	t.is(error.response.headers.connection, 'keep-alive');
	// Assert is used for type checking
	t.assert(error.response.body === 'not');
});

test('catches dns errors', async t => {
	const error = (await t.throwsAsync<RequestError<undefined>>(got('http://doesntexist', {retry: {limit: 0}})));
	t.truthy(error);
	t.regex(error.message, /ENOTFOUND|EAI_AGAIN/);
	t.is((error.options.url as URL).host, 'doesntexist');
	t.is(error.options.method, 'GET');
	t.true(['ENOTFOUND', 'EAI_AGAIN'].includes(error.code));
});

test('`options.body` form error message', async t => {
	await t.throwsAsync(
		got.post('https://example.com', {body: Buffer.from('test'), form: '' as any}),
		{
			instanceOf: RequestError,
			message: 'Option \'form\': Expected values which are `plain object` or `undefined`. Received values of type `string`.',
		},
		// {message: 'The `body`, `json` and `form` options are mutually exclusive'}
	);
});

test('no plain object restriction on json body', withServer, async (t, server, got) => {
	server.post('/body', async (request, response) => {
		await streamPipeline(request, response);
	});

	class CustomObject {
		a = 123;
	}

	const body = await got.post('body', {json: new CustomObject()}).json();

	t.deepEqual(body, {a: 123});
});

test('default status message', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 400;
		response.end('body');
	});

	const error = await t.throwsAsync<HTTPError>(
		got(''),
		{
			instanceOf: HTTPError,
			message: /^Request failed with status code 400 \(Bad Request\): GET http:\/\/localhost:\d+\/$/,
		},
	);
	t.is(error?.response.statusCode, 400);
	t.is(error?.response.statusMessage, 'Bad Request');
});

test('custom status message', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 400;
		response.statusMessage = 'Something Exploded';
		response.end('body');
	});

	const error = await t.throwsAsync<HTTPError>(
		got(''),
		{
			instanceOf: HTTPError,
			message: /^Request failed with status code 400 \(Something Exploded\): GET http:\/\/localhost:\d+\/$/,
		},
	);
	t.is(error?.response.statusCode, 400);
	t.is(error?.response.statusMessage, 'Something Exploded');
});

test('credentials are stripped from HTTPError message URL', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 400;
		response.end('body');
	});

	const error = await t.throwsAsync<HTTPError>(
		got('', {username: 'user', password: 'secret'}),
		{instanceOf: HTTPError},
	);
	t.false(error?.message.includes('user'));
	t.false(error?.message.includes('secret'));
	t.regex(error?.message ?? '', /^Request failed with status code 400 \(Bad Request\): GET http:\/\/localhost:\d+\/$/);
});

test('custom body', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 404;
		response.end('not');
	});

	const error = await t.throwsAsync<HTTPError>(
		got(''),
		{
			instanceOf: HTTPError,
			message: /^Request failed with status code 404 \(Not Found\): GET http:\/\/localhost:\d+\/$/,
		},
	);
	t.is(error?.response.statusCode, 404);
	// Typecheck for default `any` type
	t.assert(error?.response.body === 'not');
});

test('custom json body', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 404;
		response.header('content-type', 'application/json');
		response.end(JSON.stringify({
			message: 'not found',
		}));
	});

	const error = await t.throwsAsync<HTTPError<{message: string}>>(
		got('', {responseType: 'json'}),
		{
			instanceOf: HTTPError,
			message: /^Request failed with status code 404 \(Not Found\): GET http:\/\/localhost:\d+\/$/,
		},
	);
	t.is(error?.response.statusCode, 404);
	// Assert is used for body typecheck
	t.assert(error?.response.body.message === 'not found');
});

test('contains Got options', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 404;
		response.end();
	});

	const options = {
		context: {
			foo: 'bar',
		},
	} as const;

	const error = await t.throwsAsync<HTTPError>(
		got(options),
		{
			instanceOf: HTTPError,
			message: /^Request failed with status code 404 \(Not Found\): GET http:\/\/localhost:\d+\/$/,
		},
	);
	t.is(error?.response.statusCode, 404);
	t.is(error?.options.context.foo, options.context.foo);
});

test('empty status message is overriden by the default one', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.writeHead(400, '');
		response.end('body');
	});

	const error = await t.throwsAsync<HTTPError>(
		got(''),
		{
			instanceOf: HTTPError,
			message: /^Request failed with status code 400 \(Bad Request\): GET http:\/\/localhost:\d+\/$/,
		},
	);
	t.is(error?.response.statusCode, 400);
	t.is(error?.response.statusMessage, http.STATUS_CODES[400]);
});

test('`http.request` error', async t => {
	await t.throwsAsync(got('https://example.com', {
		request() {
			throw new TypeError('The header content contains invalid characters');
		},
	}), {
		instanceOf: RequestError,
		message: 'The header content contains invalid characters',
		code: 'ERR_GOT_REQUEST_ERROR',
	});
});

test('`http.request` pipe error', async t => {
	const message = 'snap!';

	await t.throwsAsync(got('https://example.com', {
		// @ts-expect-error Error tests
		request() {
			const proxy = new stream.PassThrough();

			const anyProxy = proxy as any;
			anyProxy.socket = {
				remoteAddress: '',
				prependOnceListener() {},
			};

			anyProxy.headers = {};

			anyProxy.abort = () => {};

			proxy.resume();
			proxy.read = () => {
				proxy.destroy(new Error(message));

				return null;
			};

			return proxy;
		},
		throwHttpErrors: false,
	}), {
		instanceOf: RequestError,
		message,
	});
});

test('`http.request` error through CacheableRequest', async t => {
	await t.throwsAsync(got('https://example.com', {
		request() {
			throw new TypeError('The header content contains invalid characters');
		},
		cache: new Map(),
	}), {
		instanceOf: RequestError,
		message: 'The header content contains invalid characters',
	});
});

test('returns a stream even if normalization fails', async t => {
	const stream = got.stream('https://example.com', {
		// @ts-expect-error Testing purposes
		hooks: false,
	});

	await t.throwsAsync(getStream(stream), {
		instanceOf: RequestError,
		message: 'Expected value which is `Object`, received value of type `boolean`.',
	});
});

test('returns a stream even if the input type is invalid', async t => {
	// @ts-expect-error Testing purposes
	const stream = got.stream(123);

	await t.throwsAsync(getStream(stream), {
		instanceOf: RequestError,
		message: 'Option \'input\': Expected values which are `string`, `URL`, `Object`, or `undefined`. Received values of type `number`.',
	});
});

test('normalization errors using convenience methods', async t => {
	const url = 'undefined/https://example.com';

	{
		const error = await t.throwsAsync(got(url).json());
		invalidUrl(t, error, url);
	}

	{
		const error = await t.throwsAsync(got(url).text());
		invalidUrl(t, error, url);
	}

	{
		const error = await t.throwsAsync(got(url).buffer());
		invalidUrl(t, error, url);
	}
});

test('errors can have request property', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 404;
		response.end();
	});

	const error = await t.throwsAsync<HTTPError>(got(''));

	t.truthy(error?.response);
	t.truthy(error?.request.downloadProgress);
});

test('promise does not hang on timeout on HTTP error', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 404;
		response.write('asdf');
	});

	await t.throwsAsync(got({
		timeout: {
			request: 100,
		},
	}), {
		instanceOf: TimeoutError,
		code: 'ETIMEDOUT',
	});
});

test('no uncaught parse errors', async t => {
	const server = net.createServer();

	const listen = promisify(server.listen.bind(server));
	const close = promisify(server.close.bind(server));

	await listen();

	server.on('connection', socket => {
		socket.resume();
		socket.end([
			'HTTP/1.1 404 Not Found',
			'transfer-encoding: chunked',
			'',
			'0',
			'',
			'',
		].join('\r\n'));
	});

	await t.throwsAsync(got.head(`http://localhost:${(server.address() as net.AddressInfo).port}`), {
		instanceOf: RequestError,
		message: /^Parse Error/,
	});

	await close();
});

test('no uncaught parse errors #2', async t => {
	const server = net.createServer();

	const listen = promisify(server.listen.bind(server));
	const close = promisify(server.close.bind(server));

	await listen();

	server.on('connection', socket => {
		socket.resume();
		socket.write([
			'HTTP/1.1 200 OK',
			'content-length: 1',
			'',
			'0a',
		].join('\r\n'));
	});

	await t.throwsAsync(got(`http://localhost:${(server.address() as net.AddressInfo).port}`), {
		instanceOf: RequestError,
		message: /^Parse Error/,
	});

	await close();
});

test('no uncaught parse errors on fallback to utf8', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		const buffer = Buffer.alloc(536_870_912, 'A');
		response.statusCode = 200;
		response.end(buffer);
	});

	await t.throwsAsync(got({
		timeout: {
			request: 60_000,
		},
	}), {
		instanceOf: RequestError,
		code: 'ERR_BODY_PARSE_FAILURE',
	});
});

test('the old stacktrace is recovered', async t => {
	const error = await t.throwsAsync(got('https://example.com', {
		request() {
			throw new Error('foobar');
		},
	}));

	// The stacktrace should include the original error location (the custom request function)
	t.true(error?.stack!.includes('at request'));

	// The stacktrace should include Got's error handling code
	t.true(error?.stack!.includes('Request._beforeError') ?? error?.stack!.includes('_beforeError'));

	// Verify that Got's internal code paths are in the stack
	t.true(error?.stack!.includes('Request.flush') ?? error?.stack!.includes('.flush'));
});

test('should wrap got cause', async t => {
	const error = await t.throwsAsync<RequestError>(got('https://github.com', {retry: {limit: 0}, timeout: {request: 1}}));
	const cause = error?.cause as TimeoutError;
	t.is(error?.code, cause.code);
	t.is(error?.message, cause.message);
});

test('should wrap non-got cause', async t => {
	class SocksProxyAgent extends Agent {
		override createConnection(..._args: Parameters<InstanceType<typeof Agent>['createConnection']>): ReturnType<InstanceType<typeof Agent>['createConnection']> {
			throw new SocksClientError('oh no');
		}
	}
	class SocksClientError extends Error {}
	const error = await t.throwsAsync<RequestError>(got('https://github.com', {retry: {limit: 0}, timeout: {read: 1}, agent: {https: new SocksProxyAgent()}}));
	const cause = error?.cause as Error;
	t.is(error?.code, 'ERR_GOT_REQUEST_ERROR');
	t.is(error?.message, cause.message);
	t.is(error?.message, 'oh no');
	t.assert(cause instanceof SocksClientError);
});

test.serial('custom stack trace', withServer, async (t, _server, got) => {
	// eslint-disable-next-line @typescript-eslint/naming-convention
	const ErrorCaptureStackTrace = Error.captureStackTrace;

	const enable = () => {
		Error.captureStackTrace = (target: {stack: any}) => {
			target.stack = [
				'line 1',
				'line 2',
			];
		};
	};

	const disable = () => {
		Error.captureStackTrace = ErrorCaptureStackTrace;
	};

	// Node.js default behavior
	{
		const stream = got.stream('');
		stream.destroy(new Error('oh no'));

		const caught = await t.throwsAsync(getStream(stream));
		t.is(is(caught?.stack), 'string');
	}

	// Passing a custom error
	{
		enable();
		const error = new Error('oh no');
		disable();

		const stream = got.stream('');
		stream.destroy(error);

		const caught = await t.throwsAsync(getStream(stream));
		t.is(is(caught?.stack), 'string');
	}

	// Custom global behavior
	{
		enable();
		const error = new Error('oh no');

		const stream = got.stream('');
		stream.destroy(error);

		const caught = await t.throwsAsync(getStream(stream));
		t.is(is(caught?.stack), 'Array');

		disable();
	}

	// Passing a default error that needs some processing
	{
		const error = new Error('oh no');
		enable();

		const stream = got.stream('');
		stream.destroy(error);

		const caught = await t.throwsAsync(getStream(stream));
		t.is(is(caught?.stack), 'Array');

		disable();
	}
});
```

## File: `test/extend.types.ts`
```typescript
/* eslint-disable @typescript-eslint/no-unnecessary-type-arguments */
import {expectTypeOf} from 'expect-type';
import got, {type RequestPromise, type Response} from '../source/index.js';
import {
	type Got,
	type MergeExtendsConfig,
	type ExtractExtendOptions,
	type StrictOptions,
	type ExtendOptions,
} from '../source/types.js';

// Ensure we properly extract the `extend` options from a Got instance which is used in MergeExtendsConfig generic
expectTypeOf<ExtractExtendOptions<Got<{resolveBodyOnly: false}>>>().toEqualTypeOf<{resolveBodyOnly: false}>();
expectTypeOf<ExtractExtendOptions<Got<{resolveBodyOnly: true}>>>().toEqualTypeOf<{resolveBodyOnly: true}>();
expectTypeOf<ExtractExtendOptions<{resolveBodyOnly: false}>>().toEqualTypeOf<{resolveBodyOnly: false}>();
expectTypeOf<ExtractExtendOptions<{resolveBodyOnly: true}>>().toEqualTypeOf<{resolveBodyOnly: true}>();

//
// Tests for MergeExtendsConfig - which merges the potential arguments of the `got.extend` method
//
// MergeExtendsConfig works with a single value
expectTypeOf<MergeExtendsConfig<[{resolveBodyOnly: false}]>>().toEqualTypeOf<{resolveBodyOnly: false}>();
expectTypeOf<MergeExtendsConfig<[{resolveBodyOnly: true}]>>().toEqualTypeOf<{resolveBodyOnly: true}>();
expectTypeOf<MergeExtendsConfig<[Got<{resolveBodyOnly: false}>]>>().toEqualTypeOf<{resolveBodyOnly: false}>();
expectTypeOf<MergeExtendsConfig<[Got<{resolveBodyOnly: true}>]>>().toEqualTypeOf<{resolveBodyOnly: true}>();

// MergeExtendsConfig merges multiple ExtendOptions
expectTypeOf<MergeExtendsConfig<[{resolveBodyOnly: false}, {resolveBodyOnly: true}]>>().toEqualTypeOf<{resolveBodyOnly: true}>();
expectTypeOf<MergeExtendsConfig<[{resolveBodyOnly: true}, {resolveBodyOnly: false}]>>().toEqualTypeOf<{resolveBodyOnly: false}>();

// MergeExtendsConfig merges multiple Got instances
expectTypeOf<MergeExtendsConfig<[Got<{resolveBodyOnly: false}>, Got<{resolveBodyOnly: true}>]>>().toEqualTypeOf<{resolveBodyOnly: true}>();
expectTypeOf<MergeExtendsConfig<[Got<{resolveBodyOnly: true}>, Got<{resolveBodyOnly: false}>]>>().toEqualTypeOf<{resolveBodyOnly: false}>();

// MergeExtendsConfig merges multiple Got instances and ExtendOptions with Got first argument
expectTypeOf<MergeExtendsConfig<[Got<{resolveBodyOnly: false}>, {resolveBodyOnly: true}]>>().toEqualTypeOf<{resolveBodyOnly: true}>();
expectTypeOf<MergeExtendsConfig<[Got<{resolveBodyOnly: true}>, {resolveBodyOnly: false}]>>().toEqualTypeOf<{resolveBodyOnly: false}>();

// MergeExtendsConfig merges multiple Got instances and ExtendOptions with ExtendOptions first argument
expectTypeOf<MergeExtendsConfig<[{resolveBodyOnly: true}, Got<{resolveBodyOnly: false}>]>>().toEqualTypeOf<{resolveBodyOnly: false}>();
expectTypeOf<MergeExtendsConfig<[{resolveBodyOnly: false}, Got<{resolveBodyOnly: true}>]>>().toEqualTypeOf<{resolveBodyOnly: true}>();

//
// Test the implementation of got.extend types
//
expectTypeOf(got.extend({resolveBodyOnly: false})).toEqualTypeOf<Got<{resolveBodyOnly: false}>>();
expectTypeOf(got.extend({resolveBodyOnly: true})).toEqualTypeOf<Got<{resolveBodyOnly: true}>>();
expectTypeOf(got.extend(got.extend({resolveBodyOnly: true}))).toEqualTypeOf<Got<{resolveBodyOnly: true}>>();
expectTypeOf(got.extend(got.extend({resolveBodyOnly: false}))).toEqualTypeOf<Got<{resolveBodyOnly: false}>>();
expectTypeOf(got.extend(got.extend({resolveBodyOnly: true}), {resolveBodyOnly: false})).toEqualTypeOf<Got<{resolveBodyOnly: false}>>();
expectTypeOf(got.extend(got.extend({resolveBodyOnly: false}), {resolveBodyOnly: true})).toEqualTypeOf<Got<{resolveBodyOnly: true}>>();
expectTypeOf(got.extend({resolveBodyOnly: true}, got.extend({resolveBodyOnly: false}))).toEqualTypeOf<Got<{resolveBodyOnly: false}>>();
expectTypeOf(got.extend({resolveBodyOnly: false}, got.extend({resolveBodyOnly: true}))).toEqualTypeOf<Got<{resolveBodyOnly: true}>>();

//
// Test that created instances enable the correct return types for the request functions
//
const gotWrapped = got.extend({});

// The following tests would apply to all of the method signatures (get, post, put, delete, etc...), but we only test the base function for brevity

// Test the default instance
expectTypeOf(gotWrapped('https://example.com')).toEqualTypeOf<RequestPromise<Response<string>>>();
expectTypeOf(gotWrapped<{test: 'test'}>('https://example.com')).toEqualTypeOf<RequestPromise<Response<{test: 'test'}>>>();
expectTypeOf(gotWrapped('https://example.com', {responseType: 'buffer'})).toEqualTypeOf<RequestPromise<Response<Uint8Array>>>();

// Test the default instance can be overridden at the request function level
expectTypeOf(gotWrapped('https://example.com', {resolveBodyOnly: true})).toEqualTypeOf<RequestPromise<string>>();
expectTypeOf(gotWrapped<{test: 'test'}>('https://example.com', {resolveBodyOnly: true})).toEqualTypeOf<RequestPromise<{test: 'test'}>>();
expectTypeOf(gotWrapped('https://example.com', {responseType: 'buffer', resolveBodyOnly: true})).toEqualTypeOf<RequestPromise<Uint8Array>>();

const gotBodyOnly = got.extend({resolveBodyOnly: true});

// Test the instance with resolveBodyOnly as an extend option
expectTypeOf(gotBodyOnly('https://example.com')).toEqualTypeOf<RequestPromise<string>>();
expectTypeOf(gotBodyOnly<{test: 'test'}>('https://example.com')).toEqualTypeOf<RequestPromise<{test: 'test'}>>();
expectTypeOf(gotBodyOnly('https://example.com', {responseType: 'buffer'})).toEqualTypeOf<RequestPromise<Uint8Array>>();

// Test the instance with resolveBodyOnly as an extend option can be overridden at the request function level
expectTypeOf(gotBodyOnly('https://example.com', {resolveBodyOnly: false})).toEqualTypeOf<RequestPromise<Response<string>>>();
expectTypeOf(gotBodyOnly<{test: 'test'}>('https://example.com', {resolveBodyOnly: false})).toEqualTypeOf<RequestPromise<Response<{test: 'test'}>>>();
expectTypeOf(gotBodyOnly('https://example.com', {responseType: 'buffer', resolveBodyOnly: false})).toEqualTypeOf<RequestPromise<Response<Uint8Array>>>();

//
// Test got.extend() with responseType correctly infers types (fix for issue #2427)
//
const gotJson = got.extend({responseType: 'json'});
const gotJsonBodyOnly = got.extend({responseType: 'json', resolveBodyOnly: true});
const gotBuffer = got.extend({responseType: 'buffer'});
const gotBufferBodyOnly = got.extend({responseType: 'buffer', resolveBodyOnly: true});
const gotText = got.extend({responseType: 'text'});
const gotTextBodyOnly = got.extend({responseType: 'text', resolveBodyOnly: true});

// Test URL-first syntax without options - should infer correct type based on extended responseType
expectTypeOf(gotJson('https://example.com')).toEqualTypeOf<RequestPromise<Response<unknown>>>();
expectTypeOf(gotJsonBodyOnly('https://example.com')).toEqualTypeOf<RequestPromise<unknown>>();
expectTypeOf(gotBuffer('https://example.com')).toEqualTypeOf<RequestPromise<Response<Uint8Array>>>();
expectTypeOf(gotBufferBodyOnly('https://example.com')).toEqualTypeOf<RequestPromise<Uint8Array>>();
expectTypeOf(gotText('https://example.com')).toEqualTypeOf<RequestPromise<Response<string>>>();
expectTypeOf(gotTextBodyOnly('https://example.com')).toEqualTypeOf<RequestPromise<string>>();

// @ts-expect-error `url` must be passed as the first argument.
const invalidStrictOptions: StrictOptions = {url: 'https://example.com'};
void invalidStrictOptions;

// Test that generic type parameter still works with extended responseType
expectTypeOf(gotJson<{data: string}>('https://example.com')).toEqualTypeOf<RequestPromise<Response<{data: string}>>>();
expectTypeOf(gotJsonBodyOnly<{data: string}>('https://example.com')).toEqualTypeOf<RequestPromise<{data: string}>>();

// Test that explicit responseType in call overrides extended responseType
expectTypeOf(gotJson('https://example.com', {responseType: 'buffer'})).toEqualTypeOf<RequestPromise<Response<Uint8Array>>>();
expectTypeOf(gotJson('https://example.com', {responseType: 'text'})).toEqualTypeOf<RequestPromise<Response<string>>>();
expectTypeOf(gotBuffer('https://example.com', {responseType: 'json'})).toEqualTypeOf<RequestPromise<Response<unknown>>>();
expectTypeOf(gotBuffer('https://example.com', {responseType: 'text'})).toEqualTypeOf<RequestPromise<Response<string>>>();

// Test that resolveBodyOnly can be overridden with explicit responseType
expectTypeOf(gotJson('https://example.com', {responseType: 'json', resolveBodyOnly: true})).toEqualTypeOf<RequestPromise<unknown>>();
expectTypeOf(gotJsonBodyOnly('https://example.com', {responseType: 'json', resolveBodyOnly: false})).toEqualTypeOf<RequestPromise<Response<unknown>>>();
expectTypeOf(gotBuffer('https://example.com', {responseType: 'buffer', resolveBodyOnly: true})).toEqualTypeOf<RequestPromise<Uint8Array>>();
expectTypeOf(gotBufferBodyOnly('https://example.com', {responseType: 'buffer', resolveBodyOnly: false})).toEqualTypeOf<RequestPromise<Response<Uint8Array>>>();

// @ts-expect-error `url` must not be accepted by extend options.
const invalidExtendOptions: ExtendOptions = {url: 'https://example.com'};
void invalidExtendOptions;

// Test shortcut methods preserve RequestPromise return shape
expectTypeOf(got('https://example.com').json<{data: string}>()).toEqualTypeOf<RequestPromise<{data: string}>>();
expectTypeOf(got('https://example.com').buffer()).toEqualTypeOf<RequestPromise<Uint8Array>>();
expectTypeOf(got('https://example.com').text()).toEqualTypeOf<RequestPromise<string>>();
```

## File: `test/get-unix-socket-path.ts`
```typescript
import test from 'ava';
import {getUnixSocketPath} from '../source/core/utils/is-unix-socket-url.js';

test('returns socket path for unix: protocol URLs', t => {
	const url = new URL('unix:/foo/bar.sock:/path');
	t.is(getUnixSocketPath(url), '/foo/bar.sock');
});

test('returns socket path for http://unix URLs', t => {
	const url = new URL('http://unix/foo/bar.sock:/path');
	t.is(getUnixSocketPath(url), '/foo/bar.sock');
});

test('returns different socket paths for different sockets', t => {
	const url1 = new URL('http://unix/tmp/socket1:/path');
	const url2 = new URL('http://unix/tmp/socket2:/path');

	t.is(getUnixSocketPath(url1), '/tmp/socket1');
	t.is(getUnixSocketPath(url2), '/tmp/socket2');
	t.not(getUnixSocketPath(url1), getUnixSocketPath(url2));
});

test('returns undefined for regular HTTP URLs', t => {
	const url = new URL('http://example.com/path');
	t.is(getUnixSocketPath(url), undefined);
});

test('returns undefined for HTTPS URLs', t => {
	const url = new URL('https://example.com/path');
	t.is(getUnixSocketPath(url), undefined);
});

test('handles socket paths with special characters', t => {
	const url = new URL('http://unix/tmp/my-app.sock:/api/endpoint');
	t.is(getUnixSocketPath(url), '/tmp/my-app.sock');
});
```

## File: `test/gzip.ts`
```typescript
import {Buffer} from 'node:buffer';
import {promisify} from 'node:util';
import zlib from 'node:zlib';
import test from 'ava';
import getStream from 'get-stream';
import {ReadError, type HTTPError} from '../source/index.js';
import withServer from './helpers/with-server.js';

const testContent = 'Compressible response content.\n';
const testContentUncompressed = 'Uncompressed response content.\n';

let gzipData: Uint8Array;
test.before('setup', async () => {
	gzipData = await promisify<string, Uint8Array>(zlib.gzip)(testContent);
});

test('decompress content', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.setHeader('Content-Encoding', 'gzip');
		response.end(gzipData);
	});

	t.is((await got('')).body, testContent);
});

test('decompress content on error', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.setHeader('Content-Encoding', 'gzip');
		response.status(404);
		response.end(gzipData);
	});

	const error = await t.throwsAsync<HTTPError>(got(''));

	t.is(error?.response.body, testContent);
});

test('decompress content - stream', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.setHeader('Content-Encoding', 'gzip');
		response.end(gzipData);
	});

	t.is((await getStream(got.stream(''))), testContent);
});

test('handles gzip error', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.setHeader('Content-Encoding', 'gzip');
		response.end('Not gzipped content');
	});

	await t.throwsAsync(got(''), {
		name: 'ReadError',
		message: 'incorrect header check',
	});
});

test('no unhandled `Premature close` error', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.setHeader('Content-Encoding', 'gzip');
		response.write('Not gzipped content');
	});

	await t.throwsAsync(got(''), {
		name: 'ReadError',
		// `The server aborted pending request` on Node.js 15 or later.
		message: /incorrect header check|The server aborted pending request/,
	});
});

test('handles gzip error - stream', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.setHeader('Content-Encoding', 'gzip');
		response.end('Not gzipped content');
	});

	await t.throwsAsync(getStream(got.stream('')), {
		name: 'ReadError',
		message: 'incorrect header check',
	});
});

test('decompress option opts out of decompressing', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.setHeader('Content-Encoding', 'gzip');
		response.end(gzipData);
	});

	const {body} = await got({decompress: false, responseType: 'buffer'});
	t.is(Buffer.compare(body, gzipData), 0);
	t.false(Buffer.isBuffer(body));
});

test('decompress option doesn\'t alter encoding of uncompressed responses', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end(testContentUncompressed);
	});

	const {body} = await got({decompress: false});
	t.is(body, testContentUncompressed);
});

test('preserves `headers` property', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.setHeader('Content-Encoding', 'gzip');
		response.end(gzipData);
	});

	t.truthy((await got('')).headers);
});

test('does not break HEAD responses', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end();
	});

	t.is((await got.head('')).body, '');
});

test('does not ignore missing data', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.setHeader('Content-Encoding', 'gzip');
		response.end(gzipData.subarray(0, -1));
	});

	await t.throwsAsync(got(''), {
		instanceOf: ReadError,
		message: 'unexpected end of file',
	});
});

test('response has `url` and `requestUrl` properties', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.setHeader('Content-Encoding', 'gzip');
		response.end(gzipData);
	});

	const response = await got('');
	t.truthy(response.url);
	t.truthy(response.requestUrl);
});

test('compressed and uncompressed responses have consistent spreadability', withServer, async (t, server, got) => {
	server.get('/compressed', (_request, response) => {
		response.setHeader('Content-Encoding', 'gzip');
		response.end(gzipData);
	});

	server.get('/uncompressed', (_request, response) => {
		response.end(testContentUncompressed);
	});

	// Test compressed response spreadability
	const compressedResponse = await got('compressed');
	t.true(Object.hasOwn(compressedResponse, 'headers'));
	t.true(Object.getOwnPropertyDescriptor(compressedResponse, 'headers')?.enumerable ?? false);
	const compressedSpread = {...compressedResponse};

	t.true(Object.hasOwn(compressedSpread, 'headers'));
	t.truthy(compressedSpread.headers);
	t.is(compressedSpread.statusCode, 200);
	t.truthy(compressedSpread.body);

	// Test uncompressed response spreadability
	const uncompressedResponse = await got('uncompressed');
	t.true(Object.hasOwn(uncompressedResponse, 'headers'));
	t.true(Object.getOwnPropertyDescriptor(uncompressedResponse, 'headers')?.enumerable ?? false);
	const uncompressedSpread = {...uncompressedResponse};

	t.true(Object.hasOwn(uncompressedSpread, 'headers'));
	t.truthy(uncompressedSpread.headers);
	t.is(uncompressedSpread.statusCode, 200);
	t.truthy(uncompressedSpread.body);

	// Both should have the same spreadable properties
	t.truthy(compressedSpread.headers && uncompressedSpread.headers);
	t.truthy(compressedSpread.statusCode && uncompressedSpread.statusCode);
});
```

## File: `test/headers.ts`
```typescript
import process from 'node:process';
import {Buffer} from 'node:buffer';
import fs from 'node:fs';
import path from 'node:path';
import test from 'ava';
import type {Handler} from 'express';
import got, {type Headers} from '../source/index.js';
import withServer from './helpers/with-server.js';

const supportsBrotli = typeof (process.versions as any).brotli === 'string';
const supportsZstd = typeof (process.versions as any).zstd === 'string';

const echoHeaders: Handler = (request, response) => {
	request.resume();
	response.end(JSON.stringify(request.headers));
};

test('`user-agent`', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const headers = await got('').json<Headers>();
	t.is(headers['user-agent'], 'got (https://github.com/sindresorhus/got)');
});

test('`accept-encoding`', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const headers = await got('').json<Headers>();
	const encodings = ['gzip', 'deflate'];
	if (supportsBrotli) {
		encodings.push('br');
	}

	if (supportsZstd) {
		encodings.push('zstd');
	}

	t.is(headers['accept-encoding'], encodings.join(', '));
});

test('does not override provided `accept-encoding`', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const headers = await got({
		headers: {
			'accept-encoding': 'gzip',
		},
	}).json<Headers>();
	t.is(headers['accept-encoding'], 'gzip');
});

test('does not remove user headers from `url` object argument', withServer, async (t, server) => {
	server.get('/', echoHeaders);

	const headers = (await got<Headers>(`http://${server.hostname}:${server.port}`, {
		responseType: 'json',
		headers: {
			'X-Request-Id': 'value',
		},
	})).body;

	const encodings = ['gzip', 'deflate'];
	if (supportsBrotli) {
		encodings.push('br');
	}

	if (supportsZstd) {
		encodings.push('zstd');
	}

	t.is(headers.accept, 'application/json');
	t.is(headers['user-agent'], 'got (https://github.com/sindresorhus/got)');
	t.is(headers['accept-encoding'], encodings.join(', '));
	t.is(headers['x-request-id'], 'value');
});

test('does not set `accept-encoding` header when `options.decompress` is false', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const headers = await got({
		decompress: false,
	}).json();
	// @ts-expect-error Error tests
	t.false(Reflect.has(headers, 'accept-encoding'));
});

test('`accept` header with `json` option', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	let headers = await got('').json<Headers>();
	t.is(headers.accept, 'application/json');

	headers = await got({
		headers: {
			accept: '',
		},
	}).json<Headers>();
	t.is(headers.accept, '');
});

test('`host` header', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const headers = await got('').json<Headers>();
	t.is(headers.host, `localhost:${server.port}`);
});

test('transforms names to lowercase', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const headers = (await got<Headers>({
		headers: {
			'ACCEPT-ENCODING': 'identity',
		},
		responseType: 'json',
	})).body;
	t.is(headers['accept-encoding'], 'identity');
});

test('setting `content-length` to 0', withServer, async (t, server, got) => {
	server.post('/', echoHeaders);

	const {body} = await got.post({
		headers: {
			'content-length': '0',
		},
		body: 'sup',
	});
	const headers = JSON.parse(body);
	t.is(headers['content-length'], '0');
});

test('sets `content-length` to `0` when requesting PUT with empty body', withServer, async (t, server, got) => {
	server.put('/', echoHeaders);

	const {body} = await got({
		method: 'PUT',
	});
	const headers = JSON.parse(body);
	t.is(headers['content-length'], '0');
});

test('form manual `content-type` header', withServer, async (t, server, got) => {
	server.post('/', echoHeaders);

	const {body} = await got.post({
		headers: {
			'content-type': 'custom',
		},
		form: {
			a: 1,
		},
	});
	const headers = JSON.parse(body);
	t.is(headers['content-type'], 'custom');
});

test('sets `content-type` header for native FormData', withServer, async (t, server, got) => {
	server.post('/', echoHeaders);

	const form = new globalThis.FormData();
	form.set('a', 'b');
	const {body} = await got.post({body: form});
	const headers = JSON.parse(body);
	t.true((headers['content-type'] as string).startsWith('multipart/form-data'));
});

test('native FormData uses chunked transfer-encoding instead of content-length', withServer, async (t, server, got) => {
	server.post('/', echoHeaders);

	const form = new globalThis.FormData();
	form.set('a', 'b');
	const {body} = await got.post({body: form});
	const headers = JSON.parse(body);
	t.is(headers['content-length'], undefined);
	t.is(headers['transfer-encoding'], 'chunked');
});

test('manual `content-type` header should be allowed with native FormData', withServer, async (t, server, got) => {
	server.post('/', echoHeaders);

	const form = new globalThis.FormData();
	form.set('a', 'b');
	const {body} = await got.post({
		headers: {
			'content-type': 'custom',
		},
		body: form,
	});
	const headers = JSON.parse(body);
	t.is(headers['content-type'], 'custom');
});

test('stream as `options.body` does not set `content-length` header', withServer, async (t, server, got) => {
	server.post('/', echoHeaders);

	const fixture = path.resolve('test/fixtures/stream-content-length');
	const {body} = await got.post({
		body: fs.createReadStream(fixture),
	});
	const headers = JSON.parse(body);
	t.is(headers['content-length'], undefined);
});

test('buffer as `options.body` sets `content-length` header', withServer, async (t, server, got) => {
	server.post('/', echoHeaders);

	const buffer = Buffer.from('unicorn');
	const {body} = await got.post({
		body: buffer,
	});
	const headers = JSON.parse(body);
	t.is(Number(headers['content-length']), buffer.length);
});

test('throws on null value headers', async t => {
	await t.throwsAsync(got('https://example.com', {
		headers: {
			// @ts-expect-error For testing purposes
			'user-agent': null,
		},
	}), {
		message: 'Use `undefined` instead of `null` to delete the `user-agent` header',
	});
});

test('removes undefined value headers', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const {body} = await got({
		headers: {
			'user-agent': undefined,
		},
	});
	const headers = JSON.parse(body);
	t.is(headers['user-agent'], undefined);
});

test('non-existent headers set to undefined are omitted', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const fixtureHeaders = {
		blah: undefined,
	} as const;

	const {body} = await got({
		headers: fixtureHeaders,
	});

	const headers = JSON.parse(body) as typeof fixtureHeaders;
	t.false(Reflect.has(headers, 'blah'));
});

test('preserve port in host header if non-standard port', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const body = await got('').json<Headers>();
	t.is(body.host, `localhost:${server.port}`);
});

test('strip port in host header if explicit standard port (:80) & protocol (HTTP)', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	// Start HTTP server on port 80 is not possible without root, so we test with local server instead
	const body = await got('').json<Headers>();
	// For non-standard ports, the host header should include the port
	t.is(body.host, `localhost:${server.port}`);
});

test('strip port in host header if explicit standard port (:443) & protocol (HTTPS)', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	// Start HTTPS server on port 443 is not possible without root, so we test with local server instead
	const body = await got('').json<Headers>();
	// For non-standard ports, the host header should include the port
	t.is(body.host, `localhost:${server.port}`);
});

test('strip port in host header if implicit standard port & protocol (HTTP)', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const body = await got('').json<Headers>();
	// For non-standard ports, the host header should include the port
	t.is(body.host, `localhost:${server.port}`);
});

test('strip port in host header if implicit standard port & protocol (HTTPS)', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const body = await got('').json<Headers>();
	// For non-standard ports, the host header should include the port
	t.is(body.host, `localhost:${server.port}`);
});

test('correctly encodes authorization header', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const {authorization} = await got('', {username: 'test@'}).json<{authorization: string}>();

	t.is(authorization, `Basic ${Buffer.from('test@:').toString('base64')}`);
});

test('url passes if credentials contain special characters', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const {authorization} = await got('', {password: 't$es%t'}).json<{authorization: string}>();

	t.is(authorization, `Basic ${Buffer.from(':t$es%t').toString('base64')}`);
});
```

## File: `test/helpers.ts`
```typescript
import test from 'ava';
import got, {HTTPError} from '../source/index.js';
import withServer from './helpers/with-server.js';
import invalidUrl from './helpers/invalid-url.js';

test('works', withServer, async (t, server) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	server.get('/404', (_request, response) => {
		response.statusCode = 404;
		response.end('not found');
	});

	const {body} = await got.get(server.url);
	t.is(body, 'ok');

	const error = await t.throwsAsync<HTTPError>(got.get(`${server.url}/404`), {instanceOf: HTTPError});
	t.is(error?.response.body, 'not found');

	const secondError = await t.throwsAsync(got.get('.com', {retry: {limit: 0}}));
	invalidUrl(t, secondError, '.com');
});
```

## File: `test/hooks.ts`
```typescript
import {Buffer} from 'node:buffer';
import {Agent as HttpAgent} from 'node:http';
import test from 'ava';
import getStream from 'get-stream';
import sinon from 'sinon';
import delay from 'delay';
import type {Handler} from 'express';
import Responselike from 'responselike';
import type {Constructor} from 'type-fest';
import got, {
	RequestError,
	HTTPError,
	type Response,
	type OptionsInit,
} from '../source/index.js';
import withServer from './helpers/with-server.js';

const errorString = 'oops';
const error = new Error(errorString);

const echoHeaders: Handler = (request, response) => {
	response.end(JSON.stringify(request.headers));
};

const echoBody: Handler = async (request, response) => {
	response.end(await getStream(request));
};

const echoUrl: Handler = (request, response) => {
	response.end(request.url);
};

const retryEndpoint: Handler = (request, response) => {
	if (request.headers.foo) {
		response.statusCode = 302;
		response.setHeader('location', '/');
		response.end();
	}

	response.statusCode = 500;
	response.end();
};

const redirectEndpoint: Handler = (_request, response) => {
	response.statusCode = 302;
	response.setHeader('location', '/');
	response.end();
};

const createAgentSpy = <T extends HttpAgent>(AgentClass: Constructor<any>): {agent: T; spy: sinon.SinonSpy} => {
	const agent: T = new AgentClass({keepAlive: true});
	const spy = sinon.spy(agent, 'addRequest' as any);
	return {agent, spy};
};

test('async hooks', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const {body} = await got<Record<string, string>>({
		responseType: 'json',
		hooks: {
			beforeRequest: [
				async options => {
					await delay(100);
					options.headers.foo = 'bar';
				},
			],
		},
	});
	t.is(body.foo, 'bar');
});

test('catches init thrown errors', async t => {
	await t.throwsAsync(got('https://example.com', {
		hooks: {
			init: [() => {
				throw error;
			}],
		},
	}), {
		instanceOf: RequestError,
		message: errorString,
	});
});

test('passes init thrown errors to beforeError hooks (promise-only)', async t => {
	t.plan(1);

	await t.throwsAsync(got('https://example.com', {
		hooks: {
			init: [() => {
				throw error;
			}],
			beforeError: [error => {
				t.is(error.message, errorString);

				return error;
			}],
		},
	}), {
		instanceOf: RequestError,
		message: errorString,
	});
});

test('catches beforeRequest thrown errors', async t => {
	await t.throwsAsync(got('https://example.com', {
		hooks: {
			beforeRequest: [() => {
				throw error;
			}],
		},
	}), {
		instanceOf: RequestError,
		message: errorString,
	});
});

test('catches beforeRedirect thrown errors', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);
	server.get('/redirect', redirectEndpoint);

	await t.throwsAsync(got('redirect', {
		hooks: {
			beforeRedirect: [() => {
				throw error;
			}],
		},
	}), {
		instanceOf: RequestError,
		message: errorString,
	});
});

test('catches beforeRetry thrown errors', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);
	server.get('/retry', retryEndpoint);

	await t.throwsAsync(got('retry', {
		hooks: {
			beforeRetry: [() => {
				throw error;
			}],
		},
	}), {
		instanceOf: RequestError,
		message: errorString,
	});
});

test('throws if afterResponse returns an invalid value', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	await t.throwsAsync(got('', {
		hooks: {
			afterResponse: [
				// @ts-expect-error Testing purposes
				() => {},
			],
		},
	}), {
		message: 'The `afterResponse` hook returned an invalid value',
	});
});

test('catches afterResponse thrown errors', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	await t.throwsAsync(got({
		hooks: {
			afterResponse: [() => {
				throw error;
			}],
		},
	}), {
		instanceOf: RequestError,
		message: errorString,
	});
});

test('accepts an async function as init hook', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	await got('', {
		hooks: {
			init: [
				async () => {
					t.pass();
				},
			],
		},
	});
});

test('catches beforeRequest promise rejections', async t => {
	await t.throwsAsync(got('https://example.com', {
		hooks: {
			beforeRequest: [
				async () => {
					throw error;
				},
			],
		},
	}), {
		instanceOf: RequestError,
		message: errorString,
	});
});

test('catches beforeRedirect promise rejections', withServer, async (t, server, got) => {
	server.get('/', redirectEndpoint);

	await t.throwsAsync(got({
		hooks: {
			beforeRedirect: [
				async () => {
					throw error;
				},
			],
		},
	}), {
		instanceOf: RequestError,
		message: errorString,
	});
});

test('catches beforeRetry promise rejections', withServer, async (t, server, got) => {
	server.get('/retry', retryEndpoint);

	await t.throwsAsync(got('retry', {
		hooks: {
			beforeRetry: [
				async () => {
					throw error;
				},
			],
		},
	}), {
		instanceOf: RequestError,
		message: errorString,
	});
});

test('catches afterResponse promise rejections', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	await t.throwsAsync(got({
		hooks: {
			afterResponse: [
				async () => {
					throw error;
				},
			],
		},
	}), {message: errorString});
});

test('catches beforeError errors', async t => {
	await t.throwsAsync(got('https://example.com', {
		request() {
			throw new Error('No way');
		},
		hooks: {
			beforeError: [
				async () => {
					throw error;
				},
			],
		},
	}), {message: errorString});
});

test('init is called with options', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const context = {};

	await got({
		hooks: {
			init: [
				options => {
					t.deepEqual(options.context, context);
				},
			],
		},
		context,
	});
});

test('init from defaults is called with options', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const context = {};

	let count = 0;

	const instance = got.extend({
		hooks: {
			init: [
				options => {
					count += options.context ? 1 : 0;
				},
			],
		},
	});

	await instance({context});

	t.is(count, 1);
});

test('init allows modifications', withServer, async (t, server, got) => {
	server.get('/', (request, response) => {
		response.end(request.headers.foo);
	});

	const options = {
		headers: {},
		hooks: {
			init: [
				(options: OptionsInit) => {
					options.headers = {
						foo: 'bar',
					};
				},
			],
		},
	};

	const {body} = await got('', options);

	t.deepEqual(options.headers, {});
	t.is(body, 'bar');
});

test('beforeRequest is called with options', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	await got({
		responseType: 'json',
		hooks: {
			beforeRequest: [
				options => {
					const url = options.url!;
					t.is(url.pathname, '/');
					t.is(url.hostname, 'localhost');
				},
			],
		},
	});
});

test('beforeRequest allows modifications', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const {body} = await got<Record<string, string>>({
		responseType: 'json',
		hooks: {
			beforeRequest: [
				options => {
					options.headers.foo = 'bar';
				},
			],
		},
	});
	t.is(body.foo, 'bar');
});

test('beforeRequest is called with context', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	await got({
		hooks: {
			beforeRequest: [
				(_options, context) => {
					t.truthy(context);
					t.is(typeof context.retryCount, 'number');
				},
			],
		},
	});
});

test('beforeRequest context has retryCount 0 on initial request', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	await got({
		hooks: {
			beforeRequest: [
				(_options, context) => {
					t.is(context.retryCount, 0);
				},
			],
		},
	});
});

test('beforeRequest context retryCount increments on retries', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 500;
		response.end();
	});

	const retryCounts: number[] = [];

	await t.throwsAsync(got({
		retry: {
			limit: 2,
		},
		hooks: {
			beforeRequest: [
				(_options, context) => {
					retryCounts.push(context.retryCount);
				},
			],
		},
	}), {instanceOf: HTTPError});

	t.is(retryCounts.length, 3);
	t.is(retryCounts[0], 0); // Initial request
	t.is(retryCounts[1], 1); // First retry
	t.is(retryCounts[2], 2); // Second retry
});

test('returning HTTP response from a beforeRequest hook', withServer, async (t, server, got) => {
	server.get('/', echoUrl);

	const {statusCode, headers, body} = await got({
		hooks: {
			beforeRequest: [
				() => new Responselike({
					statusCode: 200,
					headers: {
						foo: 'bar',
					},
					body: Buffer.from('Hi!'),
					url: '',
				}),
			],
		},
	});

	t.is(statusCode, 200);
	t.is(headers.foo, 'bar');
	t.is(body, 'Hi!');
});

test('returning HTTP response from a beforeRequest hook with FormData body', withServer, async (t, server, got) => {
	server.post('/', echoBody);

	const form = new globalThis.FormData();
	form.set('field', 'value');

	const data = await got.post({
		body: form,
		hooks: {
			beforeRequest: [
				() => new Responselike({
					statusCode: 200,
					headers: {},
					body: Buffer.from('{"cached": "response"}'),
					url: '',
				}),
			],
		},
	}).json<{cached: string}>();

	t.is(data.cached, 'response');
});

test('returning HTTP response from a beforeRequest hook with large buffer body', withServer, async (t, server, got) => {
	server.post('/', echoBody);

	const {body} = await got.post({
		body: Buffer.alloc(1024 * 256, 'a'),
		hooks: {
			beforeRequest: [
				() => new Responselike({
					statusCode: 200,
					headers: {},
					body: Buffer.from('hooked'),
					url: '',
				}),
			],
		},
	});

	t.is(body, 'hooked');
});

test('returning HTTP response from a beforeRequest hook with large json body', withServer, async (t, server, got) => {
	server.post('/', echoBody);

	const data = await got.post({
		json: {
			key: '.'.repeat(1024 * 256),
		},
		hooks: {
			beforeRequest: [
				() => new Responselike({
					statusCode: 200,
					headers: {},
					body: Buffer.from('{"cached":"json"}'),
					url: '',
				}),
			],
		},
	}).json<{cached: string}>();

	t.is(data.cached, 'json');
});

test('returning HTTP response from a beforeRequest hook with large typed array body', withServer, async (t, server, got) => {
	server.post('/', echoBody);

	const {body} = await got.post({
		body: new Uint8Array(1024 * 256),
		hooks: {
			beforeRequest: [
				() => new Responselike({
					statusCode: 200,
					headers: {},
					body: Buffer.from('typed-array'),
					url: '',
				}),
			],
		},
	});

	t.is(body, 'typed-array');
});

test('beforeRedirect is called with options and response', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);
	server.get('/redirect', redirectEndpoint);

	await got('redirect', {
		responseType: 'json',
		hooks: {
			beforeRedirect: [
				(options, response) => {
					const url = options.url!;
					t.is(url.pathname, '/');
					t.is(url.hostname, 'localhost');

					t.is(response.statusCode, 302);
					t.is(new URL(response.url).pathname, '/redirect');
					t.is(response.redirectUrls.length, 1);
				},
			],
		},
	});
});

test('beforeRedirect allows modifications', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);
	server.get('/redirect', redirectEndpoint);

	const {body} = await got<Record<string, string>>('redirect', {
		responseType: 'json',
		hooks: {
			beforeRedirect: [
				options => {
					options.headers.foo = 'bar';
				},
			],
		},
	});
	t.is(body.foo, 'bar');
});

test('beforeRetry is called with options', withServer, async (t, server) => {
	server.get('/', echoHeaders);
	server.get('/retry', retryEndpoint);

	const context = {};

	await got('retry', {
		prefixUrl: server.url,
		responseType: 'json',
		retry: {
			limit: 1,
		},
		throwHttpErrors: false,
		context,
		hooks: {
			beforeRetry: [
				(error, retryCount) => {
					const {options} = error;
					const {retryCount: requestRetryCount} = error.request!;
					t.is((options.url as URL).hostname, 'localhost');
					t.deepEqual(options.context, context);
					t.truthy(error);
					t.is(requestRetryCount, 0);
					t.is(retryCount, 1);
				},
			],
		},
	});
});

test('beforeRetry allows modifications', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);
	server.get('/retry', retryEndpoint);

	const {body} = await got<Record<string, string>>('retry', {
		responseType: 'json',
		hooks: {
			beforeRetry: [
				({options}) => {
					options.headers.foo = 'bar';
				},
			],
		},
	});
	t.is(body.foo, 'bar');
});

test('beforeRetry allows stream body if different from original', withServer, async (t, server, got) => {
	server.post('/retry', async (request, response) => {
		if (request.headers.foo) {
			response.send('test');
		} else {
			response.statusCode = 500;
		}

		response.end();
	});

	const generateBody = () => {
		const form = new globalThis.FormData();
		form.set('A', 'B');
		return form;
	};

	const {body} = await got.post('retry', {
		body: generateBody(),
		retry: {
			methods: ['POST'],
		},
		hooks: {
			beforeRetry: [
				({options}) => {
					options.body = generateBody();
					options.headers.foo = 'bar';
				},
			],
		},
	});

	t.is(body, 'test');
});

test('prefixUrl is preserved in beforeRequest hook', withServer, async (t, server, got) => {
	server.get('/endpoint', (_request, response) => {
		response.end('success');
	});

	let capturedPrefixUrl: string | URL | undefined;

	await got('endpoint', {
		prefixUrl: server.url,
		hooks: {
			beforeRequest: [
				options => {
					capturedPrefixUrl = options.prefixUrl;
				},
			],
		},
	});

	const normalizedServerUrl = new URL(server.url).toString();
	t.is(capturedPrefixUrl, normalizedServerUrl);
});

test('prefixUrl is preserved in beforeRetry hook', withServer, async (t, server, got) => {
	server.get('/retry', (_request, response) => {
		response.statusCode = 500;
		response.end();
	});

	let capturedPrefixUrl: string | URL | undefined;

	await t.throwsAsync(got('retry', {
		prefixUrl: server.url,
		retry: {
			limit: 1,
		},
		hooks: {
			beforeRetry: [
				({options}) => {
					capturedPrefixUrl = options.prefixUrl;
				},
			],
		},
	}));

	const normalizedServerUrl = new URL(server.url).toString();
	t.is(capturedPrefixUrl, normalizedServerUrl);
});

test('setting absolute URL in hook does not concatenate with prefixUrl', withServer, async (t, server, got) => {
	server.get('/original', (_request, response) => {
		response.end('original');
	});

	server.get('/changed', (_request, response) => {
		response.end('changed');
	});

	const {body} = await got('original', {
		prefixUrl: server.url,
		hooks: {
			beforeRequest: [
				options => {
					// Set absolute URL - should not concatenate with prefixUrl
					options.url = new URL(`${server.url}/changed`);
				},
			],
		},
	});

	t.is(body, 'changed');
});

test('allows colon in path segment with prefixUrl (CouchDB user URLs)', withServer, async (t, server, serverGot) => {
	server.get('/_users/org.couchdb.user:test@user.com', (_request, response) => {
		response.end('user document');
	});

	const client = serverGot.extend({
		prefixUrl: `${server.url}/_users/`,
	});

	const {body} = await client.get('org.couchdb.user:test@user.com');
	t.is(body, 'user document');
});

test('allows multiple colons in path with prefixUrl', withServer, async (t, server, serverGot) => {
	server.get(/^\/api\/ns:type:id$/, (_request, response) => {
		response.end('namespaced');
	});

	const client = serverGot.extend({
		prefixUrl: `${server.url}/api/`,
	});

	const {body} = await client.get('ns:type:id');
	t.is(body, 'namespaced');
});

test('allows mailto-like patterns in path with prefixUrl', withServer, async (t, server, serverGot) => {
	server.get('/users/mailto:test@example.com', (_request, response) => {
		response.end('email user');
	});

	const client = serverGot.extend({
		prefixUrl: `${server.url}/users/`,
	});

	const {body} = await client.get('mailto:test@example.com');
	t.is(body, 'email user');
});

test('allows URN-like patterns in path with prefixUrl', withServer, async (t, server, serverGot) => {
	server.get(/^\/resources\/urn:isbn:123$/, (_request, response) => {
		response.end('book');
	});

	const client = serverGot.extend({
		prefixUrl: `${server.url}/resources/`,
	});

	const {body} = await client.get('urn:isbn:123');
	t.is(body, 'book');
});

test('afterResponse is called with response', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	await got({
		responseType: 'json',
		hooks: {
			afterResponse: [
				response => {
					t.is(typeof response.body, 'object');

					return response;
				},
			],
		},
	});
});

test('afterResponse allows modifications', withServer, async (t, server, got) => {
	server.get('/', echoHeaders);

	const {body} = await got<Record<string, string>>({
		responseType: 'json',
		hooks: {
			afterResponse: [
				response => {
					response.body = {hello: 'world'};
					return response;
				},
			],
		},
	});
	t.is(body.hello, 'world');
});

test('afterResponse allows to retry', withServer, async (t, server, got) => {
	server.get('/', (request, response) => {
		if (request.headers.token !== 'unicorn') {
			response.statusCode = 401;
		}

		response.end();
	});

	const {statusCode} = await got({
		hooks: {
			afterResponse: [
				(response, retryWithMergedOptions) => {
					if (response.statusCode === 401) {
						return retryWithMergedOptions({
							headers: {
								token: 'unicorn',
							},
						});
					}

					return response;
				},
			],
		},
	});
	t.is(statusCode, 200);
});

test('afterResponse allows to retry without losing the port', withServer, async (t, server) => {
	server.get('/', (request, response) => {
		if (request.headers.token !== 'unicorn') {
			response.statusCode = 401;
		}

		response.end();
	});

	const {statusCode} = await got(server.url, {
		hooks: {
			afterResponse: [
				(response: Response, retryWithMergedOptions: (options: OptionsInit) => never) => {
					if (response.statusCode === 401) {
						return retryWithMergedOptions({
							headers: {
								token: 'unicorn',
							},
						});
					}

					return response;
				},
			],
		},
	});
	t.is(statusCode, 200);
});

test('cancelling the request after retrying in a afterResponse hook', withServer, async (t, server, got) => {
	let requests = 0;
	server.get('/', (_request, response) => {
		requests++;
		response.end();
	});

	const controller = new AbortController();

	const gotPromise = got({
		signal: controller.signal,
		hooks: {
			afterResponse: [
				(_response, retryWithMergedOptions) => {
					const promise = retryWithMergedOptions({
						headers: {
							token: 'unicorn',
						},
					});

					controller.abort();

					return promise;
				},
			],
		},
		retry: {
			calculateDelay: () => 1,
		},
	});

	await t.throwsAsync(gotPromise);
	await delay(100);
	t.is(requests, 1);
});

test('afterResponse allows to retry - `beforeRetry` hook', withServer, async (t, server, got) => {
	server.get('/', (request, response) => {
		if (request.headers.token !== 'unicorn') {
			response.statusCode = 401;
		}

		response.end();
	});

	let isCalled = false;

	const {statusCode} = await got({
		hooks: {
			afterResponse: [
				(response, retryWithMergedOptions) => {
					if (response.statusCode === 401) {
						return retryWithMergedOptions({
							headers: {
								token: 'unicorn',
							},
						});
					}

					return response;
				},
			],
			beforeRetry: [
				options => {
					t.truthy(options);
					isCalled = true;
				},
			],
		},
	});
	t.is(statusCode, 200);
	t.true(isCalled);
});

test('no infinity loop when retrying on afterResponse', withServer, async (t, server, got) => {
	server.get('/', (request, response) => {
		if (request.headers.token !== 'unicorn') {
			response.statusCode = 401;
		}

		response.end();
	});

	await t.throwsAsync(got({
		retry: {
			limit: 0,
		},
		hooks: {
			afterResponse: [
				(_response, retryWithMergedOptions) => retryWithMergedOptions({
					headers: {
						token: 'invalid',
					},
				}),
			],
		},
	}), {instanceOf: HTTPError, message: /^Request failed with status code 401 \(Unauthorized\): GET http:\/\/localhost:\d+\/$/});
});

test('throws on afterResponse retry failure', withServer, async (t, server, got) => {
	let didVisit401then500: boolean;
	server.get('/', (_request, response) => {
		if (didVisit401then500) {
			response.statusCode = 500;
		} else {
			didVisit401then500 = true;
			response.statusCode = 401;
		}

		response.end();
	});

	await t.throwsAsync(got({
		retry: {
			limit: 1,
		},
		hooks: {
			afterResponse: [
				(response, retryWithMergedOptions) => {
					if (response.statusCode === 401) {
						return retryWithMergedOptions({
							headers: {
								token: 'unicorn',
							},
						});
					}

					return response;
				},
			],
		},
	}), {instanceOf: HTTPError, message: /^Request failed with status code 500 \(Internal Server Error\): GET http:\/\/localhost:\d+\/$/});
});

test('does not throw on afterResponse retry HTTP failure if throwHttpErrors is false', withServer, async (t, server, got) => {
	let didVisit401then500: boolean;
	server.get('/', (_request, response) => {
		if (didVisit401then500) {
			response.statusCode = 500;
		} else {
			didVisit401then500 = true;
			response.statusCode = 401;
		}

		response.end();
	});

	const {statusCode} = await got({
		throwHttpErrors: false,
		retry: {
			limit: 1,
		},
		hooks: {
			afterResponse: [
				(response, retryWithMergedOptions) => {
					if (response.statusCode === 401) {
						return retryWithMergedOptions({
							headers: {
								token: 'unicorn',
							},
						});
					}

					return response;
				},
			],
		},
	});
	t.is(statusCode, 500);
});

test('afterResponse preserveHooks keeps remaining hooks on retry', withServer, async (t, server, got) => {
	server.get('/', (request, response) => {
		if (request.headers.token !== 'unicorn') {
			response.statusCode = 401;
		}

		response.end();
	});

	let firstHookCalls = 0;
	let secondHookCalls = 0;

	const {statusCode} = await got({
		hooks: {
			afterResponse: [
				(response, retryWithMergedOptions) => {
					firstHookCalls++;

					if (response.statusCode === 401) {
						return retryWithMergedOptions({
							headers: {
								token: 'unicorn',
							},
							preserveHooks: true,
						});
					}

					return response;
				},
				response => {
					secondHookCalls++;
					return response;
				},
			],
		},
	});

	t.is(statusCode, 200);
	t.is(firstHookCalls, 2); // Called for both original and retry
	t.is(secondHookCalls, 1); // Called only on retry (original was interrupted by RetryError)
});

test('afterResponse without preserveHooks skips remaining hooks on retry', withServer, async (t, server, got) => {
	server.get('/', (request, response) => {
		if (request.headers.token !== 'unicorn') {
			response.statusCode = 401;
		}

		response.end();
	});

	let firstHookCalls = 0;
	let secondHookCalls = 0;

	const {statusCode} = await got({
		hooks: {
			afterResponse: [
				(response, retryWithMergedOptions) => {
					firstHookCalls++;

					if (response.statusCode === 401) {
						return retryWithMergedOptions({
							headers: {
								token: 'unicorn',
							},
						});
					}

					return response;
				},
				response => {
					secondHookCalls++;
					return response;
				},
			],
		},
	});

	t.is(statusCode, 200);
	t.is(firstHookCalls, 1); // Called only on original request (removed from retry by default)
	t.is(secondHookCalls, 0); // Never called (removed by slice before it could run)
});

test('afterResponse preserveHooks with three hooks', withServer, async (t, server, got) => {
	server.get('/', (request, response) => {
		if (request.headers.token !== 'unicorn') {
			response.statusCode = 401;
		}

		response.end();
	});

	let firstHookCalls = 0;
	let secondHookCalls = 0;
	let thirdHookCalls = 0;

	const {statusCode} = await got({
		hooks: {
			afterResponse: [
				(response, retryWithMergedOptions) => {
					firstHookCalls++;

					if (response.statusCode === 401) {
						return retryWithMergedOptions({
							headers: {
								token: 'unicorn',
							},
							preserveHooks: true,
						});
					}

					return response;
				},
				response => {
					secondHookCalls++;
					return response;
				},
				response => {
					thirdHookCalls++;
					return response;
				},
			],
		},
	});

	t.is(statusCode, 200);
	t.is(firstHookCalls, 2); // Called for both original and retry
	t.is(secondHookCalls, 1); // Called only on retry
	t.is(thirdHookCalls, 1); // Called only on retry
});

test('afterResponse preserveHooks when second hook triggers retry', withServer, async (t, server, got) => {
	server.get('/', (request, response) => {
		if (request.headers.token !== 'unicorn') {
			response.statusCode = 401;
		}

		response.end();
	});

	let firstHookCalls = 0;
	let secondHookCalls = 0;
	let thirdHookCalls = 0;

	const {statusCode} = await got({
		hooks: {
			afterResponse: [
				response => {
					firstHookCalls++;
					return response;
				},
				(response, retryWithMergedOptions) => {
					secondHookCalls++;

					if (response.statusCode === 401) {
						return retryWithMergedOptions({
							headers: {
								token: 'unicorn',
							},
							preserveHooks: true,
						});
					}

					return response;
				},
				response => {
					thirdHookCalls++;
					return response;
				},
			],
		},
	});

	t.is(statusCode, 200);
	t.is(firstHookCalls, 2); // Called for both original and retry (preserved by preserveHooks)
	t.is(secondHookCalls, 2); // Called for both original and retry
	t.is(thirdHookCalls, 1); // Called only on retry
});

test('throwing in a beforeError hook - promise', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	await t.throwsAsync(got({
		hooks: {
			afterResponse: [
				() => {
					throw error;
				},
			],
			beforeError: [
				(): never => {
					throw new Error('foobar');
				},
				() => {
					throw new Error('This shouldn\'t be called at all');
				},
			],
		},
	}), {message: 'foobar'});
});

test('throwing in a beforeError hook - stream', withServer, async (t, _server, got) => {
	await t.throwsAsync(getStream(got.stream({
		hooks: {
			beforeError: [
				() => {
					throw new Error('foobar');
				},
				() => {
					throw new Error('This shouldn\'t be called at all');
				},
			],
		},
	})), {message: 'foobar'});
});

test('beforeError is called with an error - promise', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	await t.throwsAsync(got({
		hooks: {
			afterResponse: [
				() => {
					throw error;
				},
			],
			beforeError: [error2 => {
				t.true(error2 instanceof Error);
				return error2;
			}],
		},
	}), {message: errorString});
});

test('beforeError is called with an error - stream', withServer, async (t, _server, got) => {
	await t.throwsAsync(getStream(got.stream({
		hooks: {
			beforeError: [error2 => {
				t.true(error2 instanceof Error);
				return error2;
			}],
		},
	})), {message: /^Request failed with status code 404 \(Not Found\): GET http:\/\/localhost:\d+\/$/});
});

test('beforeError allows modifications', async t => {
	const errorString2 = 'foobar';

	await t.throwsAsync(got('https://example.com', {
		request() {
			throw error;
		},
		hooks: {
			beforeError: [
				error => {
					const newError = new Error(errorString2);

					return new RequestError(newError.message, newError, error.options);
				},
			],
		},
	}), {message: errorString2});
});

test('does not break on `afterResponse` hook with JSON mode', withServer, async (t, server, got) => {
	server.get('/foobar', echoHeaders);

	await t.notThrowsAsync(got('', {
		hooks: {
			afterResponse: [
				(response, retryWithMergedOptions) => {
					if (response.statusCode === 404) {
						return retryWithMergedOptions({
							url: new URL('/foobar', response.url),
						});
					}

					return response;
				},
			],
		},
		responseType: 'json',
	}));
});

test('catches HTTPErrors', withServer, async (t, _server, got) => {
	t.plan(2);

	await t.throwsAsync(got({
		hooks: {
			beforeError: [
				error => {
					t.true(error instanceof HTTPError);
					return error;
				},
			],
		},
	}));
});

test('timeout can be modified using a hook', withServer, async (t, server, got) => {
	server.get('/', () => {});

	await t.throwsAsync(got({
		timeout: {
			request: 1000,
		},
		hooks: {
			beforeRequest: [
				options => {
					options.timeout.request = 500;
				},
			],
		},
		retry: {
			limit: 1,
		},
	}), {message: 'Timeout awaiting \'request\' for 500ms'});
});

test('beforeRequest hook is called before each request', withServer, async (t, server, got) => {
	server.post('/', echoUrl);
	server.post('/redirect', redirectEndpoint);

	const buffer = Buffer.from('Hello, Got!');
	let counts = 0;

	await got.post('redirect', {
		body: buffer,
		hooks: {
			beforeRequest: [
				options => {
					counts++;
					t.is(options.headers['content-length'], String(buffer.length));
				},
			],
		},
	});

	t.is(counts, 2);
});

test('beforeError emits valid promise `HTTPError`s', withServer, async (t, server, got) => {
	t.plan(3);

	server.get('/', (_request, response) => {
		response.writeHead(422);
		response.end('no');
	});

	const instance = got.extend({
		hooks: {
			beforeError: [
				error => {
					t.true(error instanceof HTTPError);
					t.truthy(error.response!.body);

					return error;
				},
			],
		},
		retry: {
			limit: 0,
		},
	});

	await t.throwsAsync(instance(''));
});

test('hooks are not duplicated', withServer, async (t, _server, got) => {
	let calls = 0;

	await t.throwsAsync(got({
		hooks: {
			beforeError: [
				error => {
					calls++;

					return error;
				},
			],
		},
		retry: {
			limit: 0,
		},
	}), {message: /^Request failed with status code 404 \(Not Found\): GET http:\/\/localhost:\d+\/$/});

	t.is(calls, 1);
});

test('async afterResponse allows to retry with allowGetBody and json payload', withServer, async (t, server, got) => {
	server.get('/', (request, response) => {
		if (request.headers.token !== 'unicorn') {
			response.statusCode = 401;
		}

		response.end();
	});

	const {statusCode} = await got({
		allowGetBody: true,
		json: {hello: 'world'},
		hooks: {
			afterResponse: [
				(response, retryWithMergedOptions) => {
					if (response.statusCode === 401) {
						return retryWithMergedOptions({headers: {token: 'unicorn'}});
					}

					return response;
				},
			],
		},
		retry: {
			limit: 0,
		},
		throwHttpErrors: false,
	});

	t.is(statusCode, 200);
});

test('beforeRequest hook respect `agent` option', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	const {agent} = createAgentSpy(HttpAgent);

	t.truthy((await got({
		hooks: {
			beforeRequest: [
				options => {
					options.agent = {
						http: agent,
					};
				},
			],
		},
	})).body);

	// Make sure to close all open sockets
	agent.destroy();
});

test('beforeRequest hook respect `url` option', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ko');
	});

	server.get('/changed', (_request, response) => {
		response.end('ok');
	});

	t.is((await got(server.hostname, {
		hooks: {
			beforeRequest: [
				options => {
					options.url = new URL(`${server.url}/changed`);
				},
			],
		},
	})).body, 'ok');
});

test('no duplicate hook calls in single-page paginated requests', withServer, async (t, server, got) => {
	server.get('/get', (_request, response) => {
		response.end('i <3 koalas');
	});

	let beforeHookCount = 0;
	let beforeHookCountAdditional = 0;
	let afterHookCount = 0;
	let afterHookCountAdditional = 0;

	const hooks = {
		beforeRequest: [
			() => {
				beforeHookCount++;
			},
		],
		afterResponse: [
			(response: any) => {
				afterHookCount++;
				return response;
			},
		],
	};

	// Test only one request
	const instance = got.extend({
		hooks,
		pagination: {
			paginate: () => false,
			countLimit: 2009,
			transform: response => [response],
		},
	});

	await instance.paginate.all('get');
	t.is(beforeHookCount, 1);
	t.is(afterHookCount, 1);

	await instance.paginate.all('get', {
		hooks: {
			beforeRequest: [
				() => {
					beforeHookCountAdditional++;
				},
			],
			afterResponse: [
				(response: any) => {
					afterHookCountAdditional++;
					return response;
				},
			],
		},
	});
	t.is(beforeHookCount, 2);
	t.is(afterHookCount, 2);
	t.is(beforeHookCountAdditional, 1);
	t.is(afterHookCountAdditional, 1);

	await got.paginate.all('get', {
		hooks,
		pagination: {
			paginate: () => false,
			transform: response => [response],
		},
	});

	t.is(beforeHookCount, 3);
	t.is(afterHookCount, 3);
});

test('no duplicate hook calls in sequential paginated requests', withServer, async (t, server, got) => {
	server.get('/get', (_request, response) => {
		response.end('i <3 unicorns');
	});

	let requestNumber = 0;
	let beforeHookCount = 0;
	let afterHookCount = 0;

	const hooks = {
		beforeRequest: [
			() => {
				beforeHookCount++;
			},
		],
		afterResponse: [
			(response: any) => {
				afterHookCount++;
				return response;
			},
		],
	};

	// Test only two requests, one after another
	const paginate = () => requestNumber++ === 0 ? {} : false;

	const instance = got.extend({
		hooks,
		pagination: {
			paginate,
			countLimit: 2009,
			transform: response => [response],
		},
	});

	await instance.paginate.all('get');

	t.is(beforeHookCount, 2);
	t.is(afterHookCount, 2);
	requestNumber = 0;

	await got.paginate.all('get', {
		hooks,
		pagination: {
			paginate,
			transform: response => [response],
		},
	});

	t.is(beforeHookCount, 4);
	t.is(afterHookCount, 4);
});

test('intentional duplicate hooks in pagination with extended instance', withServer, async (t, server, got) => {
	server.get('/get', (_request, response) => {
		response.end('<3');
	});

	let beforeCount = 0; // Number of times the hooks from `extend` are called
	let afterCount = 0;
	let beforeCountAdditional = 0; // Number of times the added hooks are called
	let afterCountAdditional = 0;

	const beforeHook = () => {
		beforeCount++;
	};

	const afterHook = (response: any) => {
		afterCount++;
		return response;
	};

	const instance = got.extend({
		hooks: {
			beforeRequest: [
				beforeHook,
				beforeHook,
			],
			afterResponse: [
				afterHook,
				afterHook,
			],
		},
		pagination: {
			paginate: () => false,
			countLimit: 2009,
			transform: response => [response],
		},
	});

	// Add duplicate hooks when calling paginate
	const beforeHookAdditional = () => {
		beforeCountAdditional++;
	};

	const afterHookAdditional = (response: any) => {
		afterCountAdditional++;
		return response;
	};

	await instance.paginate.all('get', {
		hooks: {
			beforeRequest: [
				beforeHook,
				beforeHookAdditional,
				beforeHookAdditional,
			],
			afterResponse: [
				afterHook,
				afterHookAdditional,
				afterHookAdditional,
			],
		},
	});

	t.is(beforeCount, 3);
	t.is(afterCount, 3);
	t.is(beforeCountAdditional, 2);
	t.is(afterCountAdditional, 2);
});

test('no duplicate hook calls when returning original request options', withServer, async (t, server, got) => {
	server.get('/get', (_request, response) => {
		response.end('i <3 unicorns');
	});

	let requestNumber = 0;
	let beforeHookCount = 0;
	let afterHookCount = 0;

	const hooks = {
		beforeRequest: [
			() => {
				beforeHookCount++;
			},
		],
		afterResponse: [
			(response: any) => {
				afterHookCount++;
				return response;
			},
		],
	};

	// Test only two requests, one after another
	const paginate = ({response}: {response: Response}) => requestNumber++ === 0 ? response.request.options : false;

	const instance = got.extend({
		hooks,
		pagination: {
			paginate,
			countLimit: 2009,
			transform: response => [response],
		},
	});

	await instance.paginate.all('get');

	t.is(beforeHookCount, 2);
	t.is(afterHookCount, 2);
	requestNumber = 0;

	await got.paginate.all('get', {
		hooks,
		pagination: {
			paginate,
			transform: response => [response],
		},
	});

	t.is(beforeHookCount, 4);
	t.is(afterHookCount, 4);
});

test('`beforeRequest` change body', withServer, async (t, server, got) => {
	server.post('/', echoBody);

	const response = await got.post({
		json: {payload: 'old'},
		hooks: {
			beforeRequest: [
				options => {
					options.body = JSON.stringify({payload: 'new'});
					options.headers['content-length'] = Buffer.byteLength(options.body as string).toString();
				},
			],
		},
	});

	t.is(JSON.parse(response.body).payload, 'new');
});

test('`beforeRequest` change body with multi-byte characters', withServer, async (t, server, got) => {
	server.post('/', echoBody);

	const response = await got.post({
		json: {payload: 'old'},
		hooks: {
			beforeRequest: [
				options => {
					// Use multi-byte UTF-8 characters (emoji, accented characters)
					options.body = JSON.stringify({payload: 'new 🦄 café'});
					options.headers['content-length'] = Buffer.byteLength(options.body as string).toString();
				},
			],
		},
	});

	t.is(JSON.parse(response.body).payload, 'new 🦄 café');
});

test('can retry without an agent', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 408;
		response.end();
	});

	let counter = 0;

	class MyAgent extends HttpAgent {
		override createConnection(...args: Parameters<InstanceType<typeof HttpAgent>['createConnection']>): ReturnType<InstanceType<typeof HttpAgent>['createConnection']> {
			counter++;

			return (HttpAgent as any).prototype.createConnection.apply(this, args as any);
		}
	}

	const {response} = (await t.throwsAsync<HTTPError>(got({
		agent: {
			http: new MyAgent(),
		},
		hooks: {
			beforeRetry: [
				error => {
					error.options.agent.http = undefined;
				},
			],
		},
		retry: {
			calculateDelay: ({computedValue}) => computedValue ? 1 : 0,
		},
	})));

	t.is(response.retryCount, 2);
	t.is(counter, 1);
});

test('does not throw on empty body when running afterResponse hooks', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end();
	});

	await t.notThrowsAsync(got('', {
		hooks: {
			afterResponse: [
				response => response,
			],
		},
	}));
});

test('does not throw on null body with afterResponse hook and responseType json', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.setHeader('content-type', 'application/json');
		response.end('null');
	});

	const instance = got.extend({
		hooks: {
			afterResponse: [response => response],
		},
	});

	const {body} = await instance.get('', {responseType: 'json'});
	t.is(body, null);
});

test('does not throw on null body with afterResponse hook and responseType json - resolveBodyOnly', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.setHeader('content-type', 'application/json');
		response.end('null');
	});

	const instance = got.extend({
		hooks: {
			afterResponse: [response => response],
		},
	});

	const body = await instance.get('', {
		responseType: 'json',
		resolveBodyOnly: true,
	});
	t.is(body, null);
});

test('does not call beforeError hooks on falsy throwHttpErrors', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 404;
		response.end();
	});

	let called = false;

	await got('', {
		throwHttpErrors: false,
		hooks: {
			beforeError: [
				error => {
					called = true;
					return error;
				},
			],
		},
	});

	t.false(called);
});

test('beforeError hook is called for ERR_UNSUPPORTED_PROTOCOL', async t => {
	let hookCalled = false;

	const beforeErrorHook = (error: RequestError) => {
		hookCalled = true;
		return error;
	};

	await t.throwsAsync(
		got.post('xhttps://example.com', {
			headers: {authorization: 'Bearer secret'},
			json: {foo: 42},
			hooks: {
				beforeError: [beforeErrorHook],
			},
		}),
		{code: 'ERR_UNSUPPORTED_PROTOCOL'},
	);

	t.true(hookCalled);
});

test('beforeError hook can redact sensitive headers for ERR_UNSUPPORTED_PROTOCOL', async t => {
	const redactAuthorizationHeader = (error: RequestError) => {
		if (error.options?.headers?.authorization) {
			error.options.headers.authorization = '<redacted>';
		}

		return error;
	};

	const error = await t.throwsAsync<RequestError>(
		got.post('xhttps://example.com/some/resource', {
			headers: {authorization: 'Bearer secret'},
			json: {foo: 42},
			hooks: {
				beforeError: [redactAuthorizationHeader],
			},
		}),
		{code: 'ERR_UNSUPPORTED_PROTOCOL'},
	);

	t.is(error?.options.headers.authorization, '<redacted>');
});

test('beforeRetry can reassign plain stream body', withServer, async (t, server, got) => {
	const {Readable: readable} = await import('node:stream');
	let requestCount = 0;
	const testData = 'Hello, Got!';

	server.post('/retry', async (request, response) => {
		requestCount++;
		let body = '';
		for await (const chunk of request) {
			body += String(chunk);
		}

		// First request fails, second succeeds
		if (requestCount === 1) {
			response.statusCode = 500;
			response.end('Server Error');
		} else {
			response.statusCode = 200;
			response.end(`Received: ${body}`);
		}
	});

	// Factory function to create fresh streams
	const createStream = () => readable.from([testData]);

	const response = await got.post('retry', {
		body: createStream(),
		retry: {
			limit: 1,
			methods: ['POST'],
		},
		hooks: {
			beforeRetry: [
				({options}) => {
					// Reassign with a fresh stream - this previously failed
					options.body = createStream();
				},
			],
		},
	});

	t.is(response.statusCode, 200);
	t.is(response.body, `Received: ${testData}`);
	t.is(requestCount, 2);
});

test('beforeRetry destroys old stream when reassigning body', withServer, async (t, server, got) => {
	const {Readable: readable} = await import('node:stream');
	let requestCount = 0;
	const testData = 'Stream data';

	server.post('/retry', async (request, response) => {
		requestCount++;
		let body = '';
		for await (const chunk of request) {
			body += String(chunk);
		}

		// First request fails, second succeeds
		if (requestCount === 1) {
			response.statusCode = 500;
			response.end('Server Error');
		} else {
			response.statusCode = 200;
			response.end(`Received: ${body}`);
		}
	});

	const createStream = () => readable.from([testData]);
	const firstStream = createStream();
	let oldStreamDestroyed = false;

	// Monitor when the old stream is destroyed
	firstStream.on('close', () => {
		oldStreamDestroyed = true;
	});

	await got.post('retry', {
		body: firstStream,
		retry: {
			limit: 1,
			methods: ['POST'],
		},
		hooks: {
			beforeRetry: [
				({options}) => {
					// Reassign with a fresh stream
					options.body = createStream();
				},
			],
		},
	});

	t.true(oldStreamDestroyed, 'Old stream should be destroyed to prevent memory leak');
	t.is(requestCount, 2);
});

test('beforeRetry handles multiple retries with stream reassignment', withServer, async (t, server, got) => {
	const {Readable: readable} = await import('node:stream');
	let requestCount = 0;
	const testData = 'Multi-retry data';

	server.post('/retry', async (request, response) => {
		requestCount++;
		let body = '';
		for await (const chunk of request) {
			body += String(chunk);
		}

		// First two requests fail, third succeeds
		if (requestCount < 3) {
			response.statusCode = 500;
			response.end('Server Error');
		} else {
			response.statusCode = 200;
			response.end(`Received: ${body}`);
		}
	});

	const createStream = () => readable.from([testData]);
	const destroyedStreams: number[] = [];
	let streamId = 0;

	const response = await got.post('retry', {
		body: createStream(),
		retry: {
			limit: 2,
			methods: ['POST'],
		},
		hooks: {
			beforeRetry: [
				({options}) => {
					const currentStreamId = ++streamId;
					const newStream = createStream();
					newStream.on('close', () => {
						destroyedStreams.push(currentStreamId);
					});
					options.body = newStream;
				},
			],
		},
	});

	t.is(response.statusCode, 200);
	t.is(response.body, `Received: ${testData}`);
	t.is(requestCount, 3);
	t.is(destroyedStreams.length, 2, 'All old streams should be destroyed');
});

test('beforeRetry handles non-stream body reassignment', withServer, async (t, server, got) => {
	let requestCount = 0;

	server.post('/retry', async (request, response) => {
		requestCount++;
		let body = '';
		for await (const chunk of request) {
			body += String(chunk);
		}

		if (requestCount === 1) {
			response.statusCode = 500;
			response.end('Server Error');
		} else {
			response.statusCode = 200;
			response.end(`Received: ${body}`);
		}
	});

	const response = await got.post('retry', {
		body: 'initial body',
		retry: {
			limit: 1,
			methods: ['POST'],
		},
		hooks: {
			beforeRetry: [
				({options}) => {
					// Reassign with a different string body
					options.body = 'retried body';
				},
			],
		},
	});

	t.is(response.statusCode, 200);
	t.is(response.body, 'Received: retried body');
	t.is(requestCount, 2);
});

test('beforeRetry handles body set to undefined', withServer, async (t, server, got) => {
	const {Readable: readable} = await import('node:stream');
	let requestCount = 0;

	server.post('/retry', async (_request, response) => {
		requestCount++;
		// First request fails, second succeeds (with no body)
		if (requestCount === 1) {
			response.statusCode = 500;
			response.end('Error');
		} else {
			response.statusCode = 200;
			response.end('Success');
		}
	});

	await got.post('retry', {
		body: readable.from(['initial']),
		retry: {
			limit: 1,
			methods: ['POST'],
		},
		hooks: {
			beforeRetry: [
				({options}) => {
					options.body = undefined;
				},
			],
		},
	});

	t.is(requestCount, 2);
});

test('beforeRetry handles body from undefined to stream', withServer, async (t, server, got) => {
	const {Readable: readable} = await import('node:stream');
	let requestCount = 0;

	server.post('/retry', async (request, response) => {
		requestCount++;
		let body = '';
		for await (const chunk of request) {
			body += String(chunk);
		}

		if (requestCount === 1) {
			response.statusCode = 500;
			response.end('Error');
		} else {
			response.statusCode = 200;
			response.end(`Got: ${body}`);
		}
	});

	const response = await got.post('retry', {
		retry: {
			limit: 1,
			methods: ['POST'],
		},
		hooks: {
			beforeRetry: [
				({options}) => {
					options.body = readable.from(['stream-data']);
				},
			],
		},
	});

	t.is(response.body, 'Got: stream-data');
	t.is(requestCount, 2);
});

test('beforeRetry handles stream to Buffer conversion', withServer, async (t, server, got) => {
	const {Readable: readable} = await import('node:stream');
	let requestCount = 0;

	server.post('/retry', async (request, response) => {
		requestCount++;
		let body = '';
		for await (const chunk of request) {
			body += String(chunk);
		}

		if (requestCount === 1) {
			response.statusCode = 500;
			response.end('Error');
		} else {
			response.statusCode = 200;
			response.end(`Got: ${body}`);
		}
	});

	const response = await got.post('retry', {
		body: readable.from(['initial']),
		retry: {
			limit: 1,
			methods: ['POST'],
		},
		hooks: {
			beforeRetry: [
				({options}) => {
					options.body = Buffer.from('buffer-data');
				},
			],
		},
	});

	t.is(response.body, 'Got: buffer-data');
	t.is(requestCount, 2);
});

test('handler error is properly thrown in .json()', withServer, async (t, _server, got) => {
	const customError = new Error('Custom handler error');
	const instance = got.extend({
		handlers: [
			(options, next) => (async () => {
				try {
					return await next(options);
				} catch {
					throw customError;
				}
			})(),
		],
	});

	await t.throwsAsync(instance('').json(), {message: 'Custom handler error'});
});

test('handler error is properly thrown in .text()', withServer, async (t, _server, got) => {
	const customError = new Error('Custom handler error for text');
	const instance = got.extend({
		handlers: [
			(options, next) => (async () => {
				try {
					return await next(options);
				} catch {
					throw customError;
				}
			})(),
		],
	});

	await t.throwsAsync(instance('').text(), {message: 'Custom handler error for text'});
});

test('handler error is properly thrown in .buffer()', withServer, async (t, _server, got) => {
	const customError = new Error('Custom handler error for buffer');
	const instance = got.extend({
		handlers: [
			(options, next) => (async () => {
				try {
					return await next(options);
				} catch {
					throw customError;
				}
			})(),
		],
	});

	await t.throwsAsync(instance('').buffer(), {message: 'Custom handler error for buffer'});
});

test('handler throwing on successful response works with .json()', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.setHeader('content-type', 'application/json');
		response.end('{"success": true}');
	});

	const customError = new Error('Handler rejected success');
	const instance = got.extend({
		handlers: [
			(options, next) => (async () => {
				await next(options);
				throw customError;
			})(),
		],
	});

	await t.throwsAsync(instance('').json(), {message: 'Handler rejected success'});
});

test('multiple handlers with error transformation work with .json()', withServer, async (t, _server, got) => {
	const instance = got.extend({
		handlers: [
			// First handler: catches and wraps error
			(options, next) => (async () => {
				try {
					return await next(options);
				} catch (error: any) {
					const wrappedError = new Error(`Handler 1: ${error.message}`);
					throw wrappedError;
				}
			})(),
			// Second handler: catches and wraps error again
			(options, next) => (async () => {
				try {
					return await next(options);
				} catch (error: any) {
					const wrappedError = new Error(`Handler 2: ${error.message}`);
					throw wrappedError;
				}
			})(),
		],
	});

	// Should get error from first handler (outermost)
	await t.throwsAsync(instance('').json(), {message: /Handler 1: Handler 2:/});
});

test('beforeError can return custom Error class', async t => {
	class CustomError extends Error {
		constructor(message: string) {
			super(message);
			this.name = 'CustomError';
		}
	}

	const customMessage = 'This is a custom error';

	const error = await t.throwsAsync(got('https://example.com', {
		request() {
			throw new Error('Original error');
		},
		hooks: {
			beforeError: [
				() => new CustomError(customMessage),
			],
		},
	}));

	t.is(error?.name, 'CustomError');
	t.is(error?.message, customMessage);
	t.true(error instanceof CustomError);
});

test('beforeError can extend RequestError with custom error', async t => {
	class MyCustomError extends RequestError {
		constructor(message: string, error: Error, request: any) {
			super(message, error, request);
			this.name = 'MyCustomError';
		}
	}

	const customMessage = 'Custom RequestError';

	const error = await t.throwsAsync(got('https://example.com', {
		request() {
			throw new Error('Original error');
		},
		hooks: {
			beforeError: [
				error => new MyCustomError(customMessage, error, error.request),
			],
		},
	}));

	t.is(error?.name, 'MyCustomError');
	t.is(error?.message, customMessage);
	t.true(error instanceof MyCustomError);
	t.true(error instanceof RequestError);
});
```

## File: `test/http.ts`
```typescript
import process from 'node:process';
import {Buffer} from 'node:buffer';
import {STATUS_CODES, Agent} from 'node:http';
import os from 'node:os';
import {
	isIPv4,
	isIPv6,
	isIP,
	type Socket,
} from 'node:net';
import test from 'ava';
import type {Handler} from 'express';
import getStream from 'get-stream';
import {pEvent} from 'p-event';
import got, {HTTPError, RequestError, type ReadError} from '../source/index.js';
import withServer from './helpers/with-server.js';

// eslint-disable-next-line @typescript-eslint/naming-convention
const IPv6supported = Object.values(os.networkInterfaces()).some(iface => iface?.some(addr => !addr.internal && addr.family === 'IPv6'));

// eslint-disable-next-line @typescript-eslint/naming-convention
const testIPv6 = (IPv6supported && process.env.TRAVIS_DIST !== 'bionic' && process.env.TRAVIS_DIST !== 'focal') ? test : test.skip;

const echoIp: Handler = (request, response) => {
	const address = request.socket.remoteAddress;
	if (address === undefined) {
		response.end();
		return;
	}

	// IPv4 address mapped to IPv6
	response.end(address === '::ffff:127.0.0.1' ? '127.0.0.1' : address);
};

const echoBody: Handler = async (request, response) => {
	response.end(await getStream(request));
};

test('simple request', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	t.is((await got('')).body, 'ok');
});

test('empty response', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end();
	});

	t.is((await got('')).body, '');
});

test('response has `requestUrl` property', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	server.get('/empty', (_request, response) => {
		response.end();
	});

	t.is((await got('')).requestUrl.toString(), `${server.url}/`);
	t.is((await got('empty')).requestUrl.toString(), `${server.url}/empty`);
});

test('http errors have `response` property', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 404;
		response.end('not');
	});

	const error = await t.throwsAsync<HTTPError>(got(''), {instanceOf: HTTPError});
	t.is(error?.response.statusCode, 404);
	t.is(error?.response.body, 'not');
});

test('status code 304 doesn\'t throw', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 304;
		response.end();
	});

	const promise = got('');
	await t.notThrowsAsync(promise);
	const {statusCode, body} = await promise;
	t.is(statusCode, 304);
	t.is(body, '');
});

test('doesn\'t throw if `options.throwHttpErrors` is false', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 404;
		response.end('not');
	});

	t.is((await got({throwHttpErrors: false})).body, 'not');
});

test('invalid protocol throws', async t => {
	await t.throwsAsync(got('c:/nope.com').json(), {
		instanceOf: RequestError,
		message: 'Unsupported protocol: c:',
		code: 'ERR_UNSUPPORTED_PROTOCOL',
	});
});

test('custom `options.encoding`', withServer, async (t, server, got) => {
	const string = 'ok';

	server.get('/', (_request, response) => {
		response.end(string);
	});

	const data = (await got({encoding: 'base64'})).body;
	t.is(data, Buffer.from(string).toString('base64'));
});

test('`options.encoding` doesn\'t affect streams', withServer, async (t, server, got) => {
	const string = 'ok';

	server.get('/', (_request, response) => {
		response.end(string);
	});

	const data = await getStream(got.stream({encoding: 'base64'}));
	t.is(data, string);
});

test('`got.stream(...).setEncoding(...)` works', withServer, async (t, server, got) => {
	const string = 'ok';

	server.get('/', (_request, response) => {
		response.end(string);
	});

	const data = await getStream(got.stream('').setEncoding('base64'));
	t.is(data, Buffer.from(string).toString('base64'));
});

test('`searchParams` option', withServer, async (t, server, got) => {
	server.get('/', (request, response) => {
		t.is(request.query.recent, 'true');
		response.end('recent');
	});

	t.is((await got({searchParams: {recent: true}})).body, 'recent');
	t.is((await got({searchParams: 'recent=true'})).body, 'recent');
});

test('response contains url', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	t.is((await got('')).url, `${server.url}/`);
});

test('response contains got options', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	{
		const options = {
			username: 'foo',
			password: 'bar',
		};

		const {options: normalizedOptions} = (await got(options)).request;

		t.is(normalizedOptions.username, options.username);
		t.is(normalizedOptions.password, options.password);
	}

	{
		const options = {
			username: 'foo',
		};

		const {options: normalizedOptions} = (await got(options)).request;

		t.is(normalizedOptions.username, options.username);
		t.is(normalizedOptions.password, '');
	}

	{
		const options = {
			password: 'bar',
		};

		const {options: normalizedOptions} = (await got(options)).request;

		t.is(normalizedOptions.username, '');
		t.is(normalizedOptions.password, options.password);
	}
});

test('socket destroyed by the server throws ECONNRESET', withServer, async (t, server, got) => {
	server.get('/', request => {
		request.socket.destroy();
	});

	await t.throwsAsync(got('', {retry: {limit: 0}}), {
		code: 'ECONNRESET',
	});
});

test('the response contains timings property', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	const {timings} = await got('');

	t.truthy(timings);
	t.true(timings.phases.total! >= 0);
});

test('throws an error if the server aborted the request', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.writeHead(200, {
			'content-type': 'text/plain',
		});
		response.write('chunk 1');

		setImmediate(() => {
			response.write('chunk 2');

			setImmediate(() => {
				response.destroy();
			});
		});
	});

	const error = await t.throwsAsync<ReadError>(got(''), {
		message: 'The server aborted pending request',
		code: 'ECONNRESET',
	});

	t.truthy(error?.response.retryCount);
});

test('statusMessage fallback', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.writeHead(503);
		response.end();
	});

	const {statusMessage} = await got('', {
		throwHttpErrors: false,
		retry: {limit: 0},
	});

	t.is(statusMessage, STATUS_CODES[503]);
});

test('does not destroy completed requests', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.setHeader('content-encoding', 'gzip');
		response.end('');
	});

	const options = {
		agent: {
			http: new Agent({keepAlive: true}),
		},
		retry: {
			limit: 0,
		},
	};

	const stream = got.stream(options);
	stream.resume();

	const endPromise = pEvent(stream, 'end');

	const socket = await pEvent(stream, 'socket') as Socket;

	const closeListener = () => {
		t.fail('Socket has been destroyed');
	};

	socket.once('close', closeListener);

	await new Promise(resolve => {
		setTimeout(resolve, 10);
	});

	socket.off('close', closeListener);

	await endPromise;

	options.agent.http.destroy();

	t.pass();
});

testIPv6('IPv6 request', withServer, async (t, server) => {
	server.get('/ok', echoIp);

	const response = await got(`http://[::1]:${server.port}/ok`);

	t.is(response.body, '::1');
});

test('DNS auto', withServer, async (t, server, got) => {
	server.get('/ok', echoIp);

	const response = await got('ok', {
		dnsLookupIpVersion: undefined,
	});

	const version = isIP(response.body);

	t.true(version === 4 || version === 6);
});

test('DNS IPv4', withServer, async (t, server, got) => {
	server.get('/ok', echoIp);

	const response = await got('ok', {
		dnsLookupIpVersion: 4,
	});

	t.true(isIPv4(response.body));
});

// Travis CI Ubuntu Focal VM does not resolve IPv6 hostnames
testIPv6('DNS IPv6', withServer, async (t, server, got) => {
	server.get('/ok', echoIp);

	const response = await got('ok', {
		dnsLookupIpVersion: 6,
	});

	t.true(isIPv6(response.body));
});

test('invalid `dnsLookupIpVersion`', withServer, async (t, server, got) => {
	server.get('/ok', echoIp);

	await t.throwsAsync(got('ok', {
		dnsLookupIpVersion: 'test',
	} as any));
});

test('deprecated `family` option', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	await t.throwsAsync(got({
		// @ts-expect-error Legacy option
		family: 4,
	}), {
		message: 'Unexpected option: family',
	});
});

test('JSON request custom stringifier', withServer, async (t, server, got) => {
	server.post('/', echoBody);

	const payload = {a: 'b'};
	const customStringify = (object: any) => JSON.stringify({...object, c: 'd'});

	t.deepEqual((await got.post({
		stringifyJson: customStringify,
		json: payload,
	})).body, customStringify(payload));
});

test('ClientRequest can throw before promise resolves', async t => {
	const error = await t.throwsAsync<RequestError>(got('http://example.com', {
		dnsLookup: ((_hostname: string, _options: unknown, callback: (error: undefined, hostname: string, family: number) => void) => {
			queueMicrotask(() => {
				callback(undefined, 'fe80::0000:0000:0000:0000', 6);
			});
		}) as any,
	}));

	// Node.js 20+ returns ERR_INVALID_IP_ADDRESS, older versions return EINVAL, EHOSTUNREACH, or ETIMEDOUT
	t.true(['EINVAL', 'EHOSTUNREACH', 'ETIMEDOUT', 'ERR_INVALID_IP_ADDRESS'].includes(error.code));
});

test('dnsLookup option accepts Node.js dns.lookup', withServer, async (t, server, got) => {
	const dns = await import('node:dns');

	server.get('/', (_request, response) => {
		response.end('ok');
	});

	// This should work without type casting (regression test for #2426)
	const {body} = await got('', {
		dnsLookup: dns.lookup,
	});

	t.is(body, 'ok');
});

test('status code 200 has response ok is true', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 200;
		response.end();
	});

	const promise = got('');
	await t.notThrowsAsync(promise);
	const {statusCode, body, ok} = await promise;
	t.true(ok);
	t.is(statusCode, 200);
	t.is(body, '');
});

test('status code 404 has response ok is false if error is not thrown', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 404;
		response.end();
	});

	const promise = got('', {throwHttpErrors: false});
	await t.notThrowsAsync(promise);
	const {statusCode, body, ok} = await promise;
	t.is(ok, false);
	t.is(statusCode, 404);
	t.is(body, '');
});

test('status code 404 has error response ok is false if error is thrown', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 404;
		response.end('not');
	});

	const error = (await t.throwsAsync<HTTPError>(got(''), {instanceOf: HTTPError}));
	t.is(error.response.statusCode, 404);
	t.is(error.response.ok, false);
	t.is(error.response.body, 'not');
});
```

## File: `test/https.ts`
```typescript
import process from 'node:process';
import tls, {type DetailedPeerCertificate} from 'node:tls';
import test from 'ava';
import {pEvent} from 'p-event';
import pify from 'pify';
import pem from 'pem';
import {withHttpsServer} from './helpers/with-server.js';
import type {CreatePrivateKey, CreateCsr, CreateCertificate} from './types/pem.js';

const createPrivateKey = pify(pem.createPrivateKey as CreatePrivateKey);
const createCsr = pify(pem.createCSR as CreateCsr);
const createCertificate = pify(pem.createCertificate as CreateCertificate);

test('https request without ca', withHttpsServer(), async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	t.truthy((await got({
		https: {
			certificateAuthority: [],
			rejectUnauthorized: false,
		},
	})).body);
});

test('https request with ca', withHttpsServer(), async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got({});

	t.is(body, 'ok');
});

test('https request with ca and afterResponse hook', withHttpsServer(), async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	const warningListener = (warning: any) => {
		if (
			warning.name === 'DeprecationWarning'
			&& warning.message === 'Got: "options.ca" was never documented, please use '
			+ '"options.https.certificateAuthority"'
		) {
			process.off('warning', warningListener);
			t.fail('unexpected deprecation warning');
		}
	};

	process.once('warning', warningListener);

	let shouldRetry = true;
	const {body} = await got({
		hooks: {
			afterResponse: [
				(response, retry) => {
					if (shouldRetry) {
						shouldRetry = false;

						return retry({});
					}

					return response;
				},
			],
		},
	});

	t.is(body, 'ok');
});

test('https request with `checkServerIdentity` OK', withHttpsServer(), async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got({
		https: {
			checkServerIdentity(hostname: string, certificate: DetailedPeerCertificate) {
				t.is(hostname, 'localhost');
				t.is(certificate.subject.CN, 'localhost');
				t.is(certificate.issuer.CN, 'authority');
			},
		},
	});

	t.is(body, 'ok');
});

test('https request with `checkServerIdentity` NOT OK', withHttpsServer(), async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	const promise = got({
		https: {
			checkServerIdentity(hostname: string, certificate: DetailedPeerCertificate) {
				t.is(hostname, 'localhost');
				t.is(certificate.subject.CN, 'localhost');
				t.is(certificate.issuer.CN, 'authority');

				return new Error('CUSTOM_ERROR');
			},
		},
	});

	await t.throwsAsync(
		promise,
		{
			message: 'CUSTOM_ERROR',
		},
	);
});

test('https request with `serverName` option', withHttpsServer(), async (t, server, got) => {
	server.get('/', (request, response) => {
		// Get the servername from the TLS connection
		const {servername} = request.socket as any;
		response.json({servername});
	});

	const {servername} = await got({
		https: {
			serverName: 'custom.example.com',
			rejectUnauthorized: false,
		},
	}).json<{servername: string}>();

	t.is(servername, 'custom.example.com');
});

// The built-in `openssl` on macOS does not support negative days.
{
	const testFunction = process.platform === 'darwin' ? test.skip : test;
	testFunction('https request with expired certificate', withHttpsServer({days: -1}), async (t, _server, got) => {
		await t.throwsAsync(
			got({}),
			{
				code: 'CERT_HAS_EXPIRED',
			},
		);
	});
}

test('https request with wrong host', withHttpsServer({commonName: 'not-localhost.com'}), async (t, _server, got) => {
	await t.throwsAsync(
		got({}),
		{
			code: 'ERR_TLS_CERT_ALTNAME_INVALID',
		},
	);
});

test('http2', withHttpsServer(), async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.json({method: 'GET', data: 'test'});
	});

	const promise = got({
		http2: true,
	});

	try {
		const {statusCode, body} = await promise;
		await promise.json();

		t.is(statusCode, 200);
		t.is(typeof body, 'string');

		t.pass();
	} catch (error: any) {
		if (error.message.includes('install Node.js')) {
			t.pass();
			return;
		}

		t.fail(error.stack);
	}
});

test('http2 connection reuse with default agent', withHttpsServer(), async (t, server, got) => {
	server.get('/200', (_request, response) => {
		response.status(200).end('OK');
	});

	server.get('/201', (_request, response) => {
		response.status(201).end('Created');
	});

	try {
		const response1 = await got('200', {http2: true});
		const response2 = await got('201', {http2: true});

		t.is(response1.statusCode, 200);
		t.is(response2.statusCode, 201);
	} catch (error: any) {
		if (error.message.includes('install Node.js')) {
			t.pass();
			return;
		}

		t.fail(error.stack);
	}
});

test('http2 connection reuse with custom agent', withHttpsServer(), async (t, server, got) => {
	server.get('/200', (_request, response) => {
		response.status(200).end('OK');
	});

	server.get('/201', (_request, response) => {
		response.status(201).end('Created');
	});

	try {
		const {default: http2wrapper} = await import('http2-wrapper');
		const customAgent = new http2wrapper.Agent({maxEmptySessions: 5});

		const response1 = await got('200', {
			http2: true,
			agent: {http2: customAgent},
		});

		const response2 = await got('201', {
			http2: true,
			agent: {http2: customAgent},
		});

		t.is(response1.statusCode, 200);
		t.is(response2.statusCode, 201);

		customAgent.destroy();
	} catch (error: any) {
		if (error.message.includes('install Node.js')) {
			t.pass();
			return;
		}

		t.fail(error.stack);
	}
});

test.serial('deprecated `rejectUnauthorized` option', withHttpsServer(), async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	await t.throwsAsync(got({
		// @ts-expect-error Testing purposes
		rejectUnauthorized: false,
	}), {
		message: 'Unexpected option: rejectUnauthorized',
	});
});

test.serial('non-deprecated `rejectUnauthorized` option', withHttpsServer(), async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	(async () => {
		const warning = await pEvent(process, 'warning') as Error;
		t.not(warning.name, 'DeprecationWarning');
	})();

	await got({
		https: {
			rejectUnauthorized: false,
		},
	});

	t.pass();
});

test('client certificate', withHttpsServer(), async (t, server, got) => {
	server.get('/', (request, response) => {
		const peerCertificate = (request.socket as any).getPeerCertificate(true);
		peerCertificate.issuerCertificate.issuerCertificate = undefined; // Circular structure

		response.json({
			authorized: (request.socket as any).authorized,
			peerCertificate,
		});
	});

	const clientCsrResult = await createCsr({commonName: 'client'});
	const clientResult = await createCertificate({
		csr: clientCsrResult.csr,
		clientKey: clientCsrResult.clientKey,
		serviceKey: (server as any).caKey,
		serviceCertificate: (server as any).caCert,
	});
	// eslint-disable-next-line prefer-destructuring
	const clientKey = clientResult.clientKey;
	const clientCert = clientResult.certificate;

	const response = await got({
		https: {
			key: clientKey,
			certificate: clientCert,
		},
	}).json<{
		authorized: boolean;
		peerCertificate: {
			subject: {CN: string};
			issuer: {CN: string};
		};
	}>();

	t.true(response.authorized);
	t.is(response.peerCertificate.subject.CN, 'client');
	t.is(response.peerCertificate.issuer.CN, 'authority');
});

test('invalid client certificate (self-signed)', withHttpsServer(), async (t, server, got) => {
	server.get('/', (request, response) => {
		const peerCertificate = (request.socket as any).getPeerCertificate(true);
		peerCertificate.issuerCertificate = undefined; // Circular structure

		response.json({
			authorized: (request.socket as any).authorized,
			peerCertificate,
		});
	});

	const clientCsrResult = await createCsr({commonName: 'other-client'});
	const clientResult = await createCertificate({
		csr: clientCsrResult.csr,
		clientKey: clientCsrResult.clientKey,
		selfSigned: true,
	});
	// eslint-disable-next-line prefer-destructuring
	const clientKey = clientResult.clientKey;
	const clientCert = clientResult.certificate;

	const response = await got({
		https: {
			key: clientKey,
			certificate: clientCert,
		},
	}).json<{
		authorized: boolean;
	}>();

	t.is(response.authorized, false);
});

test('invalid client certificate (other CA)', withHttpsServer(), async (t, server, got) => {
	server.get('/', (request, response) => {
		const peerCertificate = (request.socket as any).getPeerCertificate(true);

		response.json({
			authorized: (request.socket as any).authorized,
			peerCertificate,
		});
	});

	const caCsrResult = await createCsr({commonName: 'other-authority'});
	const caResult = await createCertificate({
		csr: caCsrResult.csr,
		clientKey: caCsrResult.clientKey,
		selfSigned: true,
	});
	const caKey = caResult.clientKey;
	const caCert = caResult.certificate;

	const clientCsrResult = await createCsr({commonName: 'other-client'});
	const clientResult = await createCertificate({
		csr: clientCsrResult.csr,
		clientKey: clientCsrResult.clientKey,
		serviceKey: caKey,
		serviceCertificate: caCert,
	});
	// eslint-disable-next-line prefer-destructuring
	const clientKey = clientResult.clientKey;
	const clientCert = clientResult.certificate;

	const response = await got({
		https: {
			key: clientKey,
			certificate: clientCert,
		},
	}).json<{
		authorized: boolean;
		peerCertificate: {
			subject: {CN: string};
			issuer: {CN: string};
		};
	}>();

	t.false(response.authorized);
	t.is(response.peerCertificate.subject.CN, 'other-client');
	t.is(response.peerCertificate.issuer.CN, 'other-authority');
});

test('key passphrase', withHttpsServer(), async (t, server, got) => {
	// Ignore macOS for now as it fails with some internal OpenSSL error.
	if (process.platform === 'darwin') {
		t.pass();
		return;
	}

	server.get('/', (request, response) => {
		const peerCertificate = (request.socket as any).getPeerCertificate(true);
		peerCertificate.issuerCertificate.issuerCertificate = undefined; // Circular structure

		response.json({
			authorized: (request.socket as any).authorized,
			peerCertificate,
		});
	});

	const {key: clientKey} = await createPrivateKey(2048, {
		cipher: 'aes256',
		password: 'randomPassword',
	});
	const clientCsrResult = await createCsr({
		// eslint-disable-next-line object-shorthand
		clientKey: clientKey,
		clientKeyPassword: 'randomPassword',
		commonName: 'client',
	});
	const clientResult = await createCertificate({
		csr: clientCsrResult.csr,
		clientKey: clientCsrResult.clientKey,
		clientKeyPassword: 'randomPassword',
		serviceKey: (server as any).caKey,
		serviceCertificate: (server as any).caCert,
	});
	const clientCert = clientResult.certificate;

	const response = await got({
		https: {
			key: clientKey,
			passphrase: 'randomPassword',
			certificate: clientCert,
		},
	}).json<{
		authorized: boolean;
		peerCertificate: {
			subject: {CN: string};
			issuer: {CN: string};
		};
	}>();

	t.true(response.authorized);
	t.is(response.peerCertificate.subject.CN, 'client');
	t.is(response.peerCertificate.issuer.CN, 'authority');
});

test('invalid key passphrase', withHttpsServer(), async (t, server, got) => {
	// Ignore macOS for now as it fails with some internal OpenSSL error.
	if (process.platform === 'darwin') {
		t.pass();
		return;
	}

	server.get('/', (request, response) => {
		const peerCertificate = (request.socket as any).getPeerCertificate(true);
		peerCertificate.issuerCertificate.issuerCertificate = undefined; // Circular structure

		response.json({
			authorized: (request.socket as any).authorized,
			peerCertificate,
		});
	});

	const {key: clientKey} = await createPrivateKey(2048, {
		cipher: 'aes256',
		password: 'randomPassword',
	});
	const clientCsrResult = await createCsr({
		// eslint-disable-next-line object-shorthand
		clientKey: clientKey,
		clientKeyPassword: 'randomPassword',
		commonName: 'client',
	});
	const clientResult = await createCertificate({
		csr: clientCsrResult.csr,
		clientKey: clientCsrResult.clientKey,
		clientKeyPassword: 'randomPassword',
		serviceKey: (server as any).caKey,
		serviceCertificate: (server as any).caCert,
	});
	const clientCert = clientResult.certificate;

	const request = got({
		https: {
			key: clientKey,
			passphrase: 'wrongPassword',
			certificate: clientCert,
		},
	});

	const {code}: NodeJS.ErrnoException = (await t.throwsAsync(request));
	t.true(code === 'ERR_OSSL_BAD_DECRYPT' || code === 'ERR_OSSL_EVP_BAD_DECRYPT', code);
});

// Use TLS 1.3 ciphers that are stable across Node.js versions
// TLS 1.3 ciphers work best because they're consistently supported
const tlsCiphers = tls.getCiphers().map(cipher => cipher.toUpperCase()).filter(cipher => cipher.startsWith('TLS_'));

// Pick ciphers that exist in both Node.js 20 and 24
// TLS_AES_128_GCM_SHA256 and TLS_AES_256_GCM_SHA384 are always available in TLS 1.3
const stableCiphers = [
	tlsCiphers.find(c => c === 'TLS_AES_128_GCM_SHA256')!,
	tlsCiphers.find(c => c === 'TLS_AES_256_GCM_SHA384')!,
	tlsCiphers.find(c => c === 'TLS_CHACHA20_POLY1305_SHA256')!,
].filter(Boolean);

test('https request with `ciphers` option', withHttpsServer({ciphers: stableCiphers.join(':'), minVersion: 'TLSv1.3'}), async (t, server, got) => {
	server.get('/', (request, response) => {
		response.json({
			cipher: (request.socket as any).getCipher().name,
		});
	});

	const response = await got({
		https: {
			ciphers: stableCiphers[0],
			minVersion: 'TLSv1.3',
		},
	}).json<{cipher: string}>();

	t.is(response.cipher, stableCiphers[0]!);
});

test('https request with `honorCipherOrder` option', withHttpsServer({ciphers: `${stableCiphers[0]!}:${stableCiphers[1]!}`, minVersion: 'TLSv1.3'}), async (t, server, got) => {
	server.get('/', (request, response) => {
		response.json({
			cipher: (request.socket as any).getCipher().name,
		});
	});

	const response = await got({
		https: {
			ciphers: `${stableCiphers[1]!}:${stableCiphers[0]!}`,
			honorCipherOrder: true,
			minVersion: 'TLSv1.3',
		},
	}).json<{cipher: string}>();

	t.is(response.cipher, stableCiphers[0]!);
});

test('https request with `minVersion` option', withHttpsServer({maxVersion: 'TLSv1.2'}), async (t, server, got) => {
	server.get('/', (request, response) => {
		response.json({
			version: (request.socket as any).getCipher().version,
		});
	});

	const request = got({
		https: {
			minVersion: 'TLSv1.3',
		},
	});

	await t.throwsAsync(request, {
		code: 'EPROTO',
	});
});
```

## File: `test/infinite-loop-issue.ts`
```typescript
import test from 'ava';
import withServer from './helpers/with-server.js';

// Test for issue #2414: Endless recurrent loop upon retry in options.js
// https://github.com/sindresorhus/got/issues/2414
test('does not cause infinite loop when retrying with request.options', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 401;
		response.end();
	});

	let isCalled = false;

	await got({
		hooks: {
			afterResponse: [
				(response, retry) => {
					if (!isCalled) {
						isCalled = true;
						// This used to cause an infinite loop in versions 12-14
						return retry(response.request.options);
					}

					return response;
				},
			],
		},
		throwHttpErrors: false,
		retry: {
			limit: 0,
		},
	});

	t.true(isCalled);
});
```

## File: `test/merge-instances.ts`
```typescript
import test from 'ava';
import type {Handler} from 'express';
import got, {type BeforeRequestHook, type Got, type Headers} from '../source/index.js';
import withServer from './helpers/with-server.js';

const echoHeaders: Handler = (request, response) => {
	response.end(JSON.stringify(request.headers));
};

test('merging instances', withServer, async (t, server) => {
	server.get('/', echoHeaders);

	const instanceA = got.extend({headers: {unicorn: 'rainbow'}});
	const instanceB = got.extend({prefixUrl: server.url});
	const merged = instanceA.extend(instanceB);

	const headers = await merged('').json<Headers>();
	t.is(headers.unicorn, 'rainbow');
	t.not(headers['user-agent'], undefined);
});

test('merges default handlers & custom handlers', withServer, async (t, server) => {
	server.get('/', echoHeaders);

	const instanceA = got.extend({headers: {unicorn: 'rainbow'}});
	const instanceB = got.extend({
		handlers: [
			(options, next) => {
				options.headers.cat = 'meow';
				return next(options);
			},
		],
	});
	const merged = instanceA.extend(instanceB);

	const headers = await merged(server.url).json<Headers>();
	t.is(headers.unicorn, 'rainbow');
	t.is(headers.cat, 'meow');
});

test('merging one group & one instance', withServer, async (t, server) => {
	server.get('/', echoHeaders);

	const instanceA = got.extend({headers: {dog: 'woof'}});
	const instanceB = got.extend({headers: {cat: 'meow'}});
	const instanceC = got.extend({headers: {bird: 'tweet'}});
	const instanceD = got.extend({headers: {mouse: 'squeek'}});

	const merged = instanceA.extend(instanceB, instanceC);
	const doubleMerged = merged.extend(instanceD);

	const headers = await doubleMerged(server.url).json<Headers>();
	t.is(headers.dog, 'woof');
	t.is(headers.cat, 'meow');
	t.is(headers.bird, 'tweet');
	t.is(headers.mouse, 'squeek');
});

test('merging two groups of merged instances', withServer, async (t, server) => {
	server.get('/', echoHeaders);

	const instanceA = got.extend({headers: {dog: 'woof'}});
	const instanceB = got.extend({headers: {cat: 'meow'}});
	const instanceC = got.extend({headers: {bird: 'tweet'}});
	const instanceD = got.extend({headers: {mouse: 'squeek'}});

	const groupA = instanceA.extend(instanceB);
	const groupB = instanceC.extend(instanceD);

	const merged = groupA.extend(groupB);

	const headers = await merged(server.url).json<Headers>();
	t.is(headers.dog, 'woof');
	t.is(headers.cat, 'meow');
	t.is(headers.bird, 'tweet');
	t.is(headers.mouse, 'squeek');
});

test('hooks are merged', t => {
	const getBeforeRequestHooks = (instance: Got): BeforeRequestHook[] => instance.defaults.options.hooks.beforeRequest;

	const instanceA = got.extend({
		hooks: {
			beforeRequest: [
				options => {
					options.headers.dog = 'woof';
				},
			],
		},
	});
	const instanceB = got.extend({
		hooks: {
			beforeRequest: [
				options => {
					options.headers.cat = 'meow';
				},
			],
		},
	});

	const merged = instanceA.extend(instanceB);
	t.deepEqual(getBeforeRequestHooks(merged), [...getBeforeRequestHooks(instanceA), ...getBeforeRequestHooks(instanceB)]);
});

test('default handlers are not duplicated', t => {
	const instance = got.extend(got);
	t.is(instance.defaults.handlers.length, 0);
});

test('URL is not polluted', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	await got({
		username: 'foo',
	});

	const {options: normalizedOptions} = (await got({})).request;

	t.is(normalizedOptions.username, '');
});

test('merging instances with HTTPS options', t => {
	const instanceA = got.extend({
		https: {
			rejectUnauthorized: true,
			certificate: 'FIRST',
		},
	});
	const instanceB = got.extend({
		https: {
			certificate: 'SECOND',
		},
	});

	const merged = instanceA.extend(instanceB);

	t.true(merged.defaults.options.https.rejectUnauthorized);
	t.is(merged.defaults.options.https.certificate, 'SECOND');
});

test('merging instances with HTTPS options undefined', t => {
	const instanceA = got.extend({
		https: {
			rejectUnauthorized: true,
			certificate: 'FIRST',
		},
	});
	const instanceB = got.extend({
		https: {
			certificate: undefined,
		},
	});

	const merged = instanceA.extend(instanceB);

	t.true(merged.defaults.options.https.rejectUnauthorized);
	t.is(merged.defaults.options.https.certificate, undefined);
});

test('accepts options for promise API', t => {
	got.extend({
		hooks: {
			beforeRequest: [
				options => {
					options.responseType = 'buffer';
				},
			],
		},
	});

	t.pass();
});

test('merging `prefixUrl`', t => {
	const prefixUrl = 'http://example.com/';

	const instanceA = got.extend({headers: {unicorn: 'rainbow'}});
	const instanceB = got.extend({prefixUrl});
	const mergedAonB = instanceB.extend(instanceA);
	const mergedBonA = instanceA.extend(instanceB);

	t.is(mergedAonB.defaults.options.prefixUrl, prefixUrl);
	t.is(mergedBonA.defaults.options.prefixUrl, prefixUrl);

	t.is(instanceB.extend({}).defaults.options.prefixUrl, prefixUrl);
});
```

## File: `test/no-body-status-codes.ts`
```typescript
import test from 'ava';
import withServer from './helpers/with-server.js';

test('does not decompress 304 Not Modified responses with content-encoding header', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.writeHead(304, {
			'content-encoding': 'gzip',
		});
		response.end();
	});

	// Should not hang even though the response has content-encoding header but no body
	const response = await got({
		throwHttpErrors: false,
		timeout: {
			request: 1000, // 1 second timeout to catch hangs
		},
	});

	t.is(response.statusCode, 304);
	t.is(response.body, '');
});

test('does not decompress 204 No Content responses with content-encoding header', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.writeHead(204, {
			'content-encoding': 'gzip',
		});
		response.end();
	});

	const response = await got({
		throwHttpErrors: false,
		timeout: {
			request: 1000,
		},
	});

	t.is(response.statusCode, 204);
	t.is(response.body, '');
});

test('does not decompress 205 Reset Content responses with content-encoding header', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.writeHead(205, {
			'content-encoding': 'gzip',
		});
		response.end();
	});

	const response = await got({
		throwHttpErrors: false,
		timeout: {
			request: 1000,
		},
	});

	t.is(response.statusCode, 205);
	t.is(response.body, '');
});

test('does not decompress HEAD responses with content-encoding header', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		// HEAD responses should never have a body, regardless of status code
		response.writeHead(200, {
			'content-encoding': 'gzip',
			'content-type': 'text/plain',
			'content-length': '11', // Would be the length if it had a body
		});
		response.end();
	});

	const response = await got.head({
		throwHttpErrors: false,
		timeout: {
			request: 1000,
		},
	});

	t.is(response.statusCode, 200);
	t.is(response.body, '');
});

// Note: 1xx responses are handled specially by Node.js and typically
// don't reach user code in the same way as other status codes
```

## File: `test/normalize-arguments.ts`
```typescript
import test from 'ava';
import got, {Options} from '../source/index.js';

test('should merge options replacing responseType', t => {
	const responseType = 'json';
	const options = new Options({
		responseType,
	}, undefined, got.defaults.options);

	t.is(options.responseType, responseType);
});

test('no duplicated searchParams values', t => {
	const options = new Options({
		searchParams: 'string=true&noDuplication=true',
	}, {
		searchParams: new URLSearchParams({
			instance: 'true',
			noDuplication: 'true',
		}),
	});

	// eslint-disable-next-line unicorn/prevent-abbreviations
	const searchParams = options.searchParams as URLSearchParams;

	t.is(searchParams.get('string'), 'true');
	t.is(searchParams.get('instance'), 'true');
	t.is(searchParams.getAll('noDuplication').length, 1);
});

test('should copy non-numerable properties', t => {
	const options = {
		json: {hello: '123'},
	};

	const merged = new Options(options, undefined, got.defaults.options);
	const mergedTwice = new Options(undefined, undefined, merged);

	t.is(mergedTwice.json, options.json);
});

test('should get username and password from the URL', t => {
	const options = new Options({
		url: 'http://user:pass@localhost:41285',
	});

	t.is(options.username, 'user');
	t.is(options.password, 'pass');
});

test('should get username and password from the options', t => {
	const options = new Options({
		url: 'http://user:pass@localhost:41285',
		username: 'user_OPT',
		password: 'pass_OPT',
	});

	t.is(options.username, 'user_OPT');
	t.is(options.password, 'pass_OPT');
});

test('should get username and password from the merged options', t => {
	const options = new Options(
		{
			url: 'http://user:pass@localhost:41285',
		},
		{
			username: 'user_OPT_MERGE',
			password: 'pass_OPT_MERGE',
		},
	);

	t.is(options.username, 'user_OPT_MERGE');
	t.is(options.password, 'pass_OPT_MERGE');
});

test('null value in search params means empty', t => {
	const options = new Options({
		url: new URL('http://localhost'),
		searchParams: {
			foo: null as any,
		},
	});

	t.is((options.url as URL).href, 'http://localhost/?foo=');
});

test('undefined value in search params means it does not exist', t => {
	const options = new Options({
		url: new URL('http://localhost'),
		searchParams: {
			foo: undefined,
		},
	});

	t.is((options.url as URL).href, 'http://localhost/');
});

test('prefixUrl alone does not set url', t => {
	const options = new Options({
		prefixUrl: 'https://example.com',
	});

	t.is(options.url, undefined);
});

test('maxRetryAfter is calculated separately from request timeout', t => {
	const options = new Options({
		timeout: {
			request: 1000,
		},
		retry: {
			maxRetryAfter: undefined,
		},
	});

	t.is(options.retry.maxRetryAfter, undefined);

	options.merge({
		timeout: {
			request: 2000,
		},
	});

	t.is(options.retry.maxRetryAfter, undefined);

	options.merge({
		retry: {
			maxRetryAfter: 300,
		},
	});

	t.is(options.retry.maxRetryAfter, 300);
});

test('extending responseType', t => {
	const instance1 = got.extend({
		prefixUrl: 'https://localhost',
		responseType: 'json',
	});

	const instance2 = got.extend({
		headers: {
			'x-test': 'test',
		},
	});

	const merged = instance1.extend(instance2);

	t.is(merged.defaults.options.responseType, 'json');
});

test('searchParams - multiple values for one key', t => {
	const searchParameters = new URLSearchParams();

	searchParameters.append('a', '100');
	searchParameters.append('a', '200');
	searchParameters.append('a', '300');

	const options = new Options({
		searchParams: searchParameters,
	});

	t.deepEqual(
		(options.searchParams as URLSearchParams).getAll('a'),
		['100', '200', '300'],
	);
});

if (globalThis.AbortSignal !== undefined) {
	test('signal does not get frozen', t => {
		const controller = new AbortController();
		const {signal} = controller;

		const options = new Options({
			url: new URL('http://localhost'),
			signal,
		});
		options.freeze();

		t.is(Object.isFrozen(options.signal), false);
	});
}
```

## File: `test/pagination.ts`
```typescript
import {Buffer} from 'node:buffer';
import test from 'ava';
import delay from 'delay';
import getStream from 'get-stream';
import got, {type Response} from '../source/index.js';
import withServer, {withBodyParsingServer} from './helpers/with-server.js';
import type {ExtendedHttpTestServer} from './helpers/create-http-test-server.js';

const thrower = (): any => {
	throw new Error('This should not be called');
};

const resetPagination = {
	paginate: undefined,
	transform: undefined,
	filter: undefined,
	shouldContinue: undefined,
};

// eslint-disable-next-line unicorn/no-object-as-default-parameter
const attachHandler = (server: ExtendedHttpTestServer, count: number, {relative} = {relative: false}): void => {
	server.get('/', (request, response) => {
		const searchParameters = new URLSearchParams(request.url.split('?')[1]);
		const page = Number(searchParameters.get('page')) || 1;

		if (page < count) {
			response.setHeader('link', `<${relative ? '' : server.url}/?page=${page + 1}>; rel="next"`);
		}

		response.end(`[${page <= count ? page : ''}]`);
	});
};

test('the link header has no next value', withServer, async (t, server, got) => {
	const items = [1];

	server.get('/', (_request, response) => {
		response.setHeader('link', '<https://example.com>; rel="prev"');
		response.end(JSON.stringify(items));
	});

	const received = await got.paginate.all<number>('');
	t.deepEqual(received, items);
});

test('the link header is empty', withServer, async (t, server, got) => {
	const items = [1];

	server.get('/', (_request, response) => {
		response.setHeader('link', '');
		response.end(JSON.stringify(items));
	});

	const received = await got.paginate.all<number>('');
	t.deepEqual(received, items);
});

test('retrieves all elements', withServer, async (t, server, got) => {
	attachHandler(server, 2);

	const result = await got.paginate.all<number>('');

	t.deepEqual(result, [1, 2]);
});

test('retrieves all elements with JSON responseType', withServer, async (t, server, got) => {
	attachHandler(server, 2);

	const result = await got.extend({
		responseType: 'json',
	}).paginate.all<number>('');

	t.deepEqual(result, [1, 2]);
});

test('preserves URL credentials for relative next-page links', withServer, async (t, server, got) => {
	const expectedAuthorization = `Basic ${Buffer.from('hello:world').toString('base64')}`;

	server.get('/', (request, response) => {
		if (request.headers.authorization !== expectedAuthorization) {
			response.statusCode = 401;
			response.end('Unauthorized');
			return;
		}

		const searchParameters = new URLSearchParams(request.url.split('?')[1]);
		const page = Number(searchParameters.get('page')) || 1;

		if (page < 2) {
			response.setHeader('link', '</?page=2>; rel="next"');
		}

		response.end(`[${page}]`);
	});

	const url = new URL(server.url);
	url.username = 'hello';
	url.password = 'world';

	const result = await got.paginate.all<number>(url);

	t.deepEqual(result, [1, 2]);
});

test('points to defaults when extending Got without custom `pagination`', withServer, async (t, server, got) => {
	attachHandler(server, 2);

	const result = await got.extend().paginate.all<number>('');

	t.deepEqual(result, [1, 2]);
});

test('pagination options can be extended', withServer, async (t, server, got) => {
	attachHandler(server, 2);

	const result = await got.extend({
		pagination: {
			shouldContinue: () => false,
		},
	}).paginate.all<number>('');

	t.deepEqual(result, []);
});

test('filters elements', withServer, async (t, server, got) => {
	attachHandler(server, 3);

	const result = await got.paginate.all<number>({
		pagination: {
			filter({item, currentItems, allItems}) {
				t.true(Array.isArray(allItems));
				t.true(Array.isArray(currentItems));

				return item !== 2;
			},
		},
	});

	t.deepEqual(result, [1, 3]);
});

test('parses elements', withServer, async (t, server, got) => {
	attachHandler(server, 100);

	const result = await got.paginate.all<number, string>('?page=100', {
		pagination: {
			transform: response => [response.body.length],
		},
	});

	t.deepEqual(result, [5]);
});

test('parses elements - async function', withServer, async (t, server, got) => {
	attachHandler(server, 100);

	const result = await got.paginate.all<number, string>('?page=100', {
		pagination: {
			transform: async response => [response.body.length],
		},
	});

	t.deepEqual(result, [5]);
});

test('custom paginate function', withServer, async (t, server, got) => {
	attachHandler(server, 3);

	const result = await got.paginate.all<number>({
		pagination: {
			paginate({response}) {
				const url = new URL(response.url);

				if (url.search === '?page=3') {
					return false;
				}

				url.search = '?page=3';

				return {url};
			},
		},
	});

	t.deepEqual(result, [1, 3]);
});

test('custom paginate function using allItems', withServer, async (t, server, got) => {
	attachHandler(server, 3);

	const result = await got.paginate.all<number>({
		pagination: {
			paginate({allItems, response}) {
				if (allItems.length === 2) {
					return false;
				}

				return {
					url: new URL('/?page=3', response.url),
				};
			},
			stackAllItems: true,
		},
	});

	t.deepEqual(result, [1, 3]);
});

test('custom paginate function using currentItems', withServer, async (t, server, got) => {
	attachHandler(server, 3);

	const result = await got.paginate.all<number>({
		pagination: {
			paginate({currentItems, response}) {
				if (currentItems[0] === 3) {
					return false;
				}

				return {
					url: new URL('/?page=3', response.url),
				};
			},
		},
	});

	t.deepEqual(result, [1, 3]);
});

test('iterator works', withServer, async (t, server, got) => {
	attachHandler(server, 5);

	const results = await Array.fromAsync(got.paginate<number>(''));

	t.deepEqual(results, [1, 2, 3, 4, 5]);
});

test('iterator works #2', withServer, async (t, server, got) => {
	attachHandler(server, 5);

	const results = await Array.fromAsync(got.paginate.each<number>(''));

	t.deepEqual(results, [1, 2, 3, 4, 5]);
});

test('`shouldContinue` works', withServer, async (t, server, got) => {
	attachHandler(server, 2);

	const options = {
		pagination: {
			shouldContinue({currentItems, allItems}: {allItems: number[]; currentItems: number[]}) {
				t.true(Array.isArray(allItems));
				t.true(Array.isArray(currentItems));

				return false;
			},
		},
	};

	const results = await Array.fromAsync(got.paginate<number>(options));

	t.deepEqual(results, []);
});

test('`countLimit` works', withServer, async (t, server, got) => {
	attachHandler(server, 2);

	const options = {
		pagination: {
			countLimit: 1,
		},
	};

	const results = await Array.fromAsync(got.paginate<number>(options));

	t.deepEqual(results, [1]);
});

test('throws if the `pagination` option does not have `transform` property', async t => {
	const iterator = got.paginate('', {
		pagination: {...resetPagination},
		prefixUrl: 'https://example.com',
	});

	await t.throwsAsync(iterator.next());
});

test('throws if the `pagination` option does not have `shouldContinue` property', async t => {
	const iterator = got.paginate('', {
		pagination: {
			...resetPagination,
			transform: thrower,
		},
		prefixUrl: 'https://example.com',
	});

	await t.throwsAsync(iterator.next());
});

test('throws if the `pagination` option does not have `filter` property', async t => {
	const iterator = got.paginate('', {
		pagination: {
			...resetPagination,
			transform: thrower,
			shouldContinue: thrower,
			paginate: thrower,
		},
		prefixUrl: 'https://example.com',
	});

	await t.throwsAsync(iterator.next());
});

test('throws if the `pagination` option does not have `paginate` property', async t => {
	const iterator = got.paginate('', {
		pagination: {
			...resetPagination,
			transform: thrower,
			shouldContinue: thrower,
			filter: thrower,
		},
		prefixUrl: 'https://example.com',
	});

	await t.throwsAsync(iterator.next());
});

test('ignores the `resolveBodyOnly` option', withServer, async (t, server, got) => {
	attachHandler(server, 2);

	const items = await got.paginate.all('', {
		resolveBodyOnly: true,
	});

	t.deepEqual(items, [1, 2]);
});

test('allowGetBody sends json payload with .paginate()', withBodyParsingServer, async (t, server, got) => {
	server.get('/', (request, response) => {
		if (request.body.hello !== 'world') {
			response.statusCode = 400;
		}

		response.end(JSON.stringify([1, 2, 3]));
	});

	const iterator = got.paginate<number>({
		allowGetBody: true,
		json: {hello: 'world'},
		retry: {
			limit: 0,
		},
	});

	const results = await Array.fromAsync(iterator);

	t.deepEqual(results, [1, 2, 3]);
});

test('`hooks` are not duplicated', withServer, async (t, server, got) => {
	let page = 1;
	server.get('/', (_request, response) => {
		response.end(JSON.stringify([page++]));
	});

	const nopHook = () => {};

	const result = await got.paginate.all<number>({
		pagination: {
			paginate({response}) {
				if ((response.body as string) === '[3]') {
					return false; // Stop after page 3
				}

				const {options} = response.request;
				const {init, beforeRequest, beforeRedirect, beforeRetry, afterResponse, beforeError} = options.hooks;
				const hooksCount = [init, beforeRequest, beforeRedirect, beforeRetry, afterResponse, beforeError].map(a => a.length);

				t.deepEqual(hooksCount, [1, 1, 1, 1, 1, 1]);

				return options;
			},
		},
		hooks: {
			init: [nopHook],
			beforeRequest: [nopHook],
			beforeRedirect: [nopHook],
			beforeRetry: [nopHook],
			afterResponse: [response => response],
			beforeError: [error => error],
		},
	});

	t.deepEqual(result, [1, 2, 3]);
});

test('allowGetBody sends correct json payload with .paginate()', withServer, async (t, server, got) => {
	let page = 1;
	server.get('/', async (request, response) => {
		const payload = await getStream(request);

		try {
			JSON.parse(payload);
		} catch {
			response.statusCode = 422;
		}

		if (request.headers['content-length']) {
			t.is(Number(request.headers['content-length'] || 0), Buffer.byteLength(payload));
		}

		response.end(JSON.stringify([page++]));
	});

	let body = '';

	const iterator = got.paginate<number>({
		allowGetBody: true,
		retry: {
			limit: 0,
		},
		json: {body},
		pagination: {
			paginate() {
				if (body.length === 2) {
					return false;
				}

				body += 'a';

				return {
					json: {body},
				};
			},
		},
	});

	const results = await Array.fromAsync(iterator);

	t.deepEqual(results, [1, 2, 3]);
});

test('`requestLimit` works', withServer, async (t, server, got) => {
	attachHandler(server, 2);

	const options = {
		pagination: {
			requestLimit: 1,
		},
	};

	const results = await Array.fromAsync(got.paginate<number>(options));

	t.deepEqual(results, [1]);
});

test('`backoff` works', withServer, async (t, server, got) => {
	attachHandler(server, 2);

	const backoff = 200;

	const asyncIterator: AsyncIterator<number> = got.paginate<number>('', {
		pagination: {
			backoff,
		},
	});

	t.is((await asyncIterator.next()).value, 1);

	let receivedLastOne = false;
	const start = Date.now();
	const promise = asyncIterator.next();
	(async () => {
		await promise;
		receivedLastOne = true;
	})();

	await delay(backoff / 2);
	t.false(receivedLastOne);

	await promise;
	t.true(Date.now() - start >= backoff);
});

test('`stackAllItems` set to true', withServer, async (t, server, got) => {
	attachHandler(server, 3);

	let itemCount = 0;
	const result = await got.paginate.all<number>({
		pagination: {
			stackAllItems: true,
			filter({allItems}) {
				t.is(allItems.length, itemCount);

				return true;
			},
			shouldContinue({allItems}) {
				t.is(allItems.length, itemCount);

				return true;
			},
			paginate({response, currentItems, allItems}) {
				itemCount += 1;
				t.is(allItems.length, itemCount);

				return got.defaults.options.pagination.paginate!({response, currentItems, allItems});
			},
		},
	});

	t.deepEqual(result, [1, 2, 3]);
});

test('`stackAllItems` set to false', withServer, async (t, server, got) => {
	attachHandler(server, 3);

	const result = await got.paginate.all<number>({
		pagination: {
			stackAllItems: false,
			filter({allItems}) {
				t.is(allItems.length, 0);

				return true;
			},
			shouldContinue({allItems}) {
				t.is(allItems.length, 0);

				return true;
			},
			paginate({response, currentItems, allItems}) {
				t.is(allItems.length, 0);

				return got.defaults.options.pagination.paginate!({response, allItems, currentItems});
			},
		},
	});

	t.deepEqual(result, [1, 2, 3]);
});

test('next url in json response', withServer, async (t, server, got) => {
	server.get('/', (request, response) => {
		const parameters = new URLSearchParams(request.url.slice(2));
		const page = Number(parameters.get('page') ?? 0);

		response.end(JSON.stringify({
			currentUrl: request.url,
			next: page < 3 ? `${server.url}/?page=${page + 1}` : undefined,
		}));
	});

	type Page = {
		currentUrl: string;
		next?: string;
	};

	const all = await got.paginate.all('', {
		searchParams: {
			page: 0,
		},
		responseType: 'json',
		pagination: {
			transform: (response: Response<Page>) => [response.body.currentUrl],
			paginate({response}) {
				const {next} = response.body;

				if (!next) {
					return false;
				}

				return {
					url: new URL(next),
					prefixUrl: '',
					searchParams: undefined,
				};
			},
		},
	});

	t.deepEqual(all, [
		'/?page=0',
		'/?page=1',
		'/?page=2',
		'/?page=3',
	]);
});

test('pagination using searchParams', withServer, async (t, server, got) => {
	server.get('/', (request, response) => {
		const parameters = new URLSearchParams(request.url.slice(2));
		const page = Number(parameters.get('page') ?? 0);

		response.end(JSON.stringify({
			currentUrl: request.url,
			next: page < 3,
		}));
	});

	type Page = {
		currentUrl: string;
		next?: string;
	};

	const all = await got.paginate.all('', {
		searchParams: {
			page: 0,
		},
		responseType: 'json',
		pagination: {
			transform: (response: Response<Page>) => [response.body.currentUrl],
			paginate({response}) {
				const {next} = response.body;
				// eslint-disable-next-line unicorn/prevent-abbreviations
				const searchParams = response.request.options.searchParams as URLSearchParams;
				const previousPage = Number(searchParams.get('page'));

				if (!next) {
					return false;
				}

				return {
					searchParams: {
						page: previousPage + 1,
					},
				};
			},
		},
	});

	t.deepEqual(all, [
		'/?page=0',
		'/?page=1',
		'/?page=2',
		'/?page=3',
	]);
});

test('pagination using extended searchParams', withServer, async (t, server, got) => {
	server.get('/', (request, response) => {
		const parameters = new URLSearchParams(request.url.slice(2));
		const page = Number(parameters.get('page') ?? 0);

		response.end(JSON.stringify({
			currentUrl: request.url,
			next: page < 3,
		}));
	});

	type Page = {
		currentUrl: string;
		next?: string;
	};

	const client = got.extend({
		searchParams: {
			limit: 10,
		},
	});

	const all = await client.paginate.all('', {
		searchParams: {
			page: 0,
		},
		responseType: 'json',
		pagination: {
			transform: (response: Response<Page>) => [response.body.currentUrl],
			paginate({response}) {
				const {next} = response.body;
				// eslint-disable-next-line unicorn/prevent-abbreviations
				const searchParams = response.request.options.searchParams as URLSearchParams;
				const previousPage = Number(searchParams.get('page'));

				if (!next) {
					return false;
				}

				return {
					searchParams: {
						page: previousPage + 1,
					},
				};
			},
		},
	});

	t.is(all.length, 4);

	for (let i = 0; i < 4; i++) {
		t.true(all[i] === `/?page=${i}&limit=10` || all[i] === `/?limit=10&page=${i}`);
	}
});

test('calls init hooks on pagination', withServer, async (t, server) => {
	server.get('/', (request, response) => {
		response.end(JSON.stringify([request.url]));
	});

	const instance = got.extend({
		hooks: {
			init: [
				options => {
					options.searchParams = 'foobar';
				},
			],
		},
	});

	const received = await instance.paginate.all<string>(server.url, {
		searchParams: 'unicorn',
	});

	t.deepEqual(received, [
		'/?foobar=',
	]);
});

test('retrieves all elements - relative url', withServer, async (t, server, got) => {
	attachHandler(server, 2, {relative: true});

	const result = await got.paginate.all<number>('');

	t.deepEqual(result, [1, 2]);
});

test('throws when `url` is passed in pagination options object', async t => {
	await t.throwsAsync(got.paginate.all<number>({url: 'https://example.com'} as any), {
		instanceOf: TypeError,
		message: 'The `url` option is not supported in options objects. Pass it as the first argument instead.',
	});
});

test('throws when `url` is passed in pagination second argument options object', async t => {
	await t.throwsAsync(got.paginate.all<number>('https://example.com', {url: 'https://example.com'} as any), {
		instanceOf: TypeError,
		message: 'The `url` option is not supported in options objects. Pass it as the first argument instead.',
	});
});

test('throws if url is not an instance of URL', withServer, async (t, server, got) => {
	attachHandler(server, 2);

	await t.throwsAsync(got.paginate.all<number>('', {
		pagination: {
			paginate: () => ({
				url: 'not an instance of URL',
			}),
		},
	}), {
		instanceOf: TypeError,
	});
});

test('throws when transform does not return an array', withServer, async (t, server) => {
	server.get('/', (_request, response) => {
		response.end(JSON.stringify(''));
	});

	await t.throwsAsync(got.paginate.all<string>(server.url), {
		instanceOf: TypeError,
	});
});
```

## File: `test/parse-link-header.ts`
```typescript
import test from 'ava';
import parseLinkHeader from '../source/core/parse-link-header.js';

test('works as expected', t => {
	t.deepEqual(
		parseLinkHeader('<https://one.example.com>; rel="preconnect", <https://two.example.com>; rel="preconnect", <https://three.example.com>; rel="preconnect"'),
		[
			{
				reference: 'https://one.example.com',
				parameters: {rel: '"preconnect"'},
			},
			{
				reference: 'https://two.example.com',
				parameters: {rel: '"preconnect"'},
			},
			{
				reference: 'https://three.example.com',
				parameters: {rel: '"preconnect"'},
			},
		],
	);

	t.deepEqual(
		parseLinkHeader('<https://one.example.com>; rel="previous"; title="previous chapter"'),
		[
			{
				reference: 'https://one.example.com',
				parameters: {rel: '"previous"', title: '"previous chapter"'},
			},
		],
	);

	t.deepEqual(
		parseLinkHeader('</>; rel="http://example.net/foo"'),
		[
			{
				reference: '/',
				parameters: {rel: '"http://example.net/foo"'},
			},
		],
	);

	t.deepEqual(
		parseLinkHeader('</terms>; rel="copyright"; anchor="#foo"'),
		[
			{
				reference: '/terms',
				parameters: {rel: '"copyright"', anchor: '"#foo"'},
			},
		],
	);

	t.deepEqual(parseLinkHeader(`</TheBook/chapter2>;
	rel="previous"; title*=UTF-8'de'letztes%20Kapitel,
	</TheBook/chapter4>;
	rel="next"; title*=UTF-8'de'n%c3%a4chstes%20Kapitel`), [
		{
			reference: '/TheBook/chapter2',
			parameters: {
				rel: '"previous"',
				// eslint-disable-next-line @typescript-eslint/naming-convention
				'title*': 'UTF-8\'de\'letztes%20Kapitel',
			},
		},
		{
			reference: '/TheBook/chapter4',
			parameters: {
				rel: '"next"',
				// eslint-disable-next-line @typescript-eslint/naming-convention
				'title*': 'UTF-8\'de\'n%c3%a4chstes%20Kapitel',
			},
		},
	]);

	t.throws(() => parseLinkHeader('https://bad.example; rel="preconnect"'), {
		message: 'Invalid format of the Link header reference: https://bad.example',
	});

	t.throws(() => parseLinkHeader('https://bad.example; rel'), {
		message: 'Invalid format of the Link header reference: https://bad.example',
	});

	t.throws(() => parseLinkHeader('https://bad.example'), {
		message: 'Invalid format of the Link header reference: https://bad.example',
	});

	t.throws(() => parseLinkHeader(''), {
		message: 'Invalid format of the Link header reference: ',
	});

	t.throws(() => parseLinkHeader('<https://bad.example>; rel'), {
		message: 'Failed to parse Link header: <https://bad.example>; rel',
	});

	t.throws(() => parseLinkHeader('<https://bad.example>'), {
		message: 'Unexpected end of Link header parameters: ',
	});

	t.throws(() => parseLinkHeader('<>'), {
		message: 'Unexpected end of Link header parameters: ',
	});

	t.throws(() => parseLinkHeader('<https://bad.example'), {
		message: 'Invalid format of the Link header reference: <https://bad.example',
	});

	t.throws(() => parseLinkHeader('https://bad.example>'), {
		message: 'Invalid format of the Link header reference: https://bad.example>',
	});
});
```

## File: `test/post.ts`
```typescript
import process from 'node:process';
import {Buffer} from 'node:buffer';
import stream from 'node:stream';
import {pipeline as streamPipeline} from 'node:stream/promises';
import fs from 'node:fs';
import fsPromises from 'node:fs/promises';
import path from 'node:path';
import test from 'ava';
import delay from 'delay';
import {pEvent} from 'p-event';
import type {Handler} from 'express';
import {
	parse,
	Body,
	isBodyFile,
	type BodyEntryPath,
	type BodyEntryRawValue,
} from 'then-busboy';
import getStream from 'get-stream';
import {FormData as NodeFetchFormData} from 'node-fetch';
import got, {UploadError} from '../source/index.js';
import withServer from './helpers/with-server.js';

const defaultEndpoint: Handler = async (request, response) => {
	response.setHeader('method', request.method);
	await streamPipeline(request, response);
};

const echoHeaders: Handler = (request, response) => {
	response.end(JSON.stringify(request.headers));
};

const echoMultipartBody: Handler = async (request, response) => {
	const body = await parse(request);
	const entries = await Promise.all([...body.entries()].map<Promise<[BodyEntryPath, BodyEntryRawValue]>>(async ([name, value]) => [name, isBodyFile(value) ? await value.text() : value]));

	response.json(Body.json(entries));
};

test('GET cannot have body without the `allowGetBody` option', withServer, async (t, server, got) => {
	server.post('/', defaultEndpoint);

	await t.throwsAsync(got.get({body: 'hi'}), {message: 'The `GET` method cannot be used with a body'});
});

test('GET can have body with option allowGetBody', withServer, async (t, server, got) => {
	server.get('/', defaultEndpoint);

	await t.notThrowsAsync(got.get({body: 'hi', allowGetBody: true}));
});

test('invalid body', async t => {
	// @ts-expect-error Error tests
	await t.throwsAsync(got.post('https://example.com', {body: {}}));
});

test('sends strings', withServer, async (t, server, got) => {
	server.post('/', defaultEndpoint);

	const {body} = await got.post({body: 'wow'});
	t.is(body, 'wow');
});

test('sends Buffers', withServer, async (t, server, got) => {
	server.post('/', defaultEndpoint);

	const {body} = await got.post({body: Buffer.from('wow')});
	t.is(body, 'wow');
});

test('sends Uint8Array', withServer, async (t, server, got) => {
	server.post('/', defaultEndpoint);

	const uint8Body = new Uint8Array([119, 111, 119]); // 'wow' in ASCII
	const {body} = await got.post({body: uint8Body});
	t.is(body, 'wow');
});

test('sends Uint16Array', withServer, async (t, server, got) => {
	server.post('/', defaultEndpoint);

	const text = 'hello';
	const buffer = Buffer.from(text);
	const uint16Body = new Uint16Array(buffer.buffer, buffer.byteOffset, buffer.byteLength / Uint16Array.BYTES_PER_ELEMENT);
	const {body} = await got.post({body: uint16Body});
	t.is(Buffer.from(uint16Body.buffer, uint16Body.byteOffset, uint16Body.byteLength).toString(), body);
});

test('`content-length` header with Uint8Array body', withServer, async (t, server, got) => {
	server.post('/', echoHeaders);

	const uint8Body = new Uint8Array([119, 111, 119]);
	const {body} = await got.post({body: uint8Body});
	const headers = JSON.parse(body);
	t.is(headers['content-length'], '3');
});

test('sends Streams', withServer, async (t, server, got) => {
	server.post('/', defaultEndpoint);

	const {body} = await got.post({body: stream.Readable.from('wow')});
	t.is(body, 'wow');
});

test('sends plain objects as forms', withServer, async (t, server, got) => {
	server.post('/', defaultEndpoint);

	const {body} = await got.post({
		form: {such: 'wow'},
	});

	t.is(body, 'such=wow');
});

test('does not support sending arrays as forms', withServer, async (t, server, got) => {
	server.post('/', defaultEndpoint);

	await t.throwsAsync(got.post({
		form: ['such', 'wow'],
	}));
});

test('sends plain objects as JSON', withServer, async (t, server, got) => {
	server.post('/', defaultEndpoint);

	const {body} = await got.post({
		json: {such: 'wow'},
		responseType: 'json',
	});
	t.deepEqual(body, {such: 'wow'});
});

test('sends arrays as JSON', withServer, async (t, server, got) => {
	server.post('/', defaultEndpoint);

	const {body} = await got.post({
		json: ['such', 'wow'],
		responseType: 'json',
	});
	t.deepEqual(body, ['such', 'wow']);
});

test('works with empty post response', withServer, async (t, server, got) => {
	server.post('/empty', (_request, response) => {
		response.end();
	});

	const {body} = await got.post('empty', {body: 'wow'});
	t.is(body, '');
});

test('`content-length` header with string body', withServer, async (t, server, got) => {
	server.post('/', echoHeaders);

	const {body} = await got.post({body: 'wow'});
	const headers = JSON.parse(body);
	t.is(headers['content-length'], '3');
});

test('`content-length` header with json body', withServer, async (t, server, got) => {
	server.post('/', echoHeaders);

	const {body} = await got.post({json: {foo: 'bar'}});
	const headers = JSON.parse(body);
	t.is(headers['content-length'], '13');
});

test('`content-length` header with form body', withServer, async (t, server, got) => {
	server.post('/', echoHeaders);

	const {body} = await got.post({form: {foo: 'bar'}});
	const headers = JSON.parse(body);
	t.is(headers['content-length'], '7');
});

test('`content-length` header with Buffer body', withServer, async (t, server, got) => {
	server.post('/', echoHeaders);

	const {body} = await got.post({body: Buffer.from('wow')});
	const headers = JSON.parse(body);
	t.is(headers['content-length'], '3');
});

test('`content-length` header with Stream body', withServer, async (t, server, got) => {
	server.post('/', echoHeaders);

	const {body} = await got.post({body: stream.Readable.from('wow')});
	const headers = JSON.parse(body);
	t.is(headers['transfer-encoding'], 'chunked', 'likely failed to get headers at all');
	t.is(headers['content-length'], undefined);
});

test('`content-length` header is not overriden', withServer, async (t, server, got) => {
	server.post('/', echoHeaders);

	const {body} = await got.post({
		body: 'wow',
		headers: {
			'content-length': '10',
		},
	});
	const headers = JSON.parse(body);
	t.is(headers['content-length'], '10');
});

test('`content-length` header is present when using custom content-type', withServer, async (t, server, got) => {
	server.post('/', echoHeaders);

	const {body} = await got.post({
		json: {foo: 'bar'},
		headers: {
			'content-type': 'custom',
		},
	});
	const headers = JSON.parse(body);
	t.is(headers['content-length'], '13');
});

test('`content-length` header disabled for chunked transfer-encoding', withServer, async (t, server, got) => {
	server.post('/', echoHeaders);

	const {body} = await got.post({
		body: '3\r\nwow\r\n0\r\n',
		headers: {
			'transfer-encoding': 'chunked',
		},
	});
	const headers = JSON.parse(body);
	t.is(headers['transfer-encoding'], 'chunked', 'likely failed to get headers at all');
	t.is(headers['content-length'], undefined);
});

test('`content-type` header is not overriden when object in `options.body`', withServer, async (t, server, got) => {
	server.post('/', echoHeaders);

	const {body: headers} = await got.post<Record<string, string>>({
		headers: {
			'content-type': 'doge',
		},
		json: {
			such: 'wow',
		},
		responseType: 'json',
	});
	t.is(headers['content-type'], 'doge');
});

test('throws when form body is not a plain object or array', async t => {
	// @ts-expect-error Manual test
	await t.throwsAsync(got.post('https://example.com', {form: 'such=wow'}));
});

// See https://github.com/sindresorhus/got/issues/897
test('the `json` payload is not touched', withServer, async (t, server, got) => {
	server.post('/', defaultEndpoint);

	const {body} = await got.post<{context: {foo: true}}>({
		json: {
			context: {
				foo: true,
			},
		},
		responseType: 'json',
	});

	t.true('context' in body);
	t.true(body.context.foo);
});

test('the `body` payload is not touched', withServer, async (t, server, got) => {
	server.post('/', defaultEndpoint);

	const buffer = Buffer.from('Hello, Got!') as Uint8Array & {context?: unknown};
	buffer.context = {foo: 'bar'};

	const body = await got.post({body: buffer}).text();
	t.is(body, 'Hello, Got!');
});

test('the `form` payload is not touched', withServer, async (t, server, got) => {
	server.post('/', defaultEndpoint);

	const form = {
		context: true,
	};

	const body = await got.post({form}).text();
	t.is(body, 'context=true');
});

test('DELETE method sends plain objects as JSON', withServer, async (t, server, got) => {
	server.delete('/', defaultEndpoint);

	const {body} = await got.delete({
		json: {such: 'wow'},
		responseType: 'json',
	});
	t.deepEqual(body, {such: 'wow'});
});

test('catches body errors before calling pipeline() - promise', withServer, async (t, server, got) => {
	server.post('/', defaultEndpoint);

	await t.throwsAsync(got.post({
		body: fs.createReadStream('./file-that-does-not-exist.txt'),
	}), {
		message: /ENOENT: no such file or directory/,
	});

	// Wait for unhandled errors
	await delay(100);
});

test('catches body errors before calling pipeline() - stream', withServer, async (t, server, got) => {
	server.post('/', defaultEndpoint);

	await t.throwsAsync(getStream(got.stream.post({
		body: fs.createReadStream('./file-that-does-not-exist.txt'),
	})), {
		message: /ENOENT: no such file or directory/,
	});

	// Wait for unhandled errors
	await delay(100);
});

test('body - file read stream', withServer, async (t, server, got) => {
	server.post('/', defaultEndpoint);

	const fullPath = path.resolve('test/fixtures/ok');
	const toSend = await getStream(fs.createReadStream(fullPath));

	const body = await got.post({
		body: fs.createReadStream(fullPath),
	}).text();

	t.is(toSend, body);
});

test('body - file read stream, wait for `ready` event', withServer, async (t, server, got) => {
	server.post('/', defaultEndpoint);

	const fullPath = path.resolve('test/fixtures/ok');
	const toSend = await getStream(fs.createReadStream(fullPath));
	const ifStream = fs.createReadStream(fullPath);

	await pEvent(ifStream, 'ready');

	const body = await got.post({
		body: ifStream,
	}).text();

	t.is(toSend, body);
});

test('body - sends native FormData', withServer, async (t, server, got) => {
	server.post('/', echoMultipartBody);

	const form = new globalThis.FormData();
	form.set('a', 'b');
	const body = await got.post({body: form}).json<{a: string}>();
	t.is(body.a, 'b');
});

test('body - sends files with native FormData', withServer, async (t, server, got) => {
	server.post('/', echoMultipartBody);

	const fullPath = path.resolve('test/fixtures/ok');
	const blobContent = 'Blob content';
	const fileContent = 'File content';
	const anotherFileContent = await fsPromises.readFile(fullPath, 'utf8');
	const expected = {
		blob: blobContent,
		file: fileContent,
		anotherFile: anotherFileContent,
	};

	const form = new globalThis.FormData();
	form.set('blob', new Blob([blobContent]));
	form.set('file', new File([fileContent], 'file.txt', {type: 'text/plain'}));
	form.set('anotherFile', new File([anotherFileContent], 'ok', {type: 'text/plain'}));
	const body = await got.post({body: form}).json<typeof expected>();
	t.deepEqual(body, expected);
});

test('body - throws on non-native FormData', withServer, async (t, server, got) => {
	server.post('/', echoMultipartBody);

	const form = new NodeFetchFormData();
	form.set('a', 'b');

	await t.throwsAsync(got.post({body: form}), {
		code: 'ERR_GOT_REQUEST_ERROR',
		message: 'Non-native FormData is not supported. Use globalThis.FormData instead.',
	});
});

test('throws on upload error', withServer, async (t, server, got) => {
	server.post('/', defaultEndpoint);

	const body = new stream.PassThrough();
	const message = 'oh no';

	await t.throwsAsync(getStream(got.stream.post({
		body,
		hooks: {
			beforeRequest: [
				() => {
					process.nextTick(() => {
						body.destroy(new Error(message));
					});
				},
			],
		},
	})), {
		instanceOf: UploadError,
		message,
		code: 'ERR_UPLOAD',
	});
});

test('formdata retry', withServer, async (t, server, got) => {
	server.post('/', echoHeaders);

	const instance = got.extend({
		hooks: {
			afterResponse: [
				async (_response, retryWithMergedOptions) => retryWithMergedOptions({
					headers: {
						foo: 'bar',
					},
				}),
			],
		},
	});

	const form = new globalThis.FormData();
	form.set('hello', 'world');

	await t.throwsAsync(instance.post({
		body: form,
	}).json<{foo?: string}>(), {
		message: 'Cannot retry with consumed body stream',
	});
});

test('body - sends async iterable', withServer, async (t, server, got) => {
	server.post('/', defaultEndpoint);

	async function * generateData() {
		yield 'Hello, ';
		yield 'world!';
	}

	const body = await got.post({
		body: generateData(),
	}).text();

	t.is(body, 'Hello, world!');
});

test('body - sends iterable', withServer, async (t, server, got) => {
	server.post('/', defaultEndpoint);

	function * generateData() {
		yield 'foo';
		yield 'bar';
	}

	const body = await got.post({
		body: generateData(),
	}).text();

	t.is(body, 'foobar');
});
```

## File: `test/progress.ts`
```typescript
import process from 'node:process';
import {Buffer} from 'node:buffer';
import {promisify} from 'node:util';
import stream from 'node:stream';
import {pipeline as streamPipeline} from 'node:stream/promises';
import fs from 'node:fs';
// @ts-expect-error Fails to find slow-stream/index.d.ts
import SlowStream from 'slow-stream';
import getStream from 'get-stream';
import {temporaryFile} from 'tempy';
import is from '@sindresorhus/is';
import test, {type ExecutionContext} from 'ava';
import type {Handler} from 'express';
import {pEvent} from 'p-event';
import {chunk, chunkFromAsync} from 'chunk-data';
import type {Progress} from '../source/index.js';
import withServer from './helpers/with-server.js';

const checkEvents = (t: ExecutionContext, events: Progress[], bodySize?: number) => {
	t.true(events.length >= 2);

	let lastEvent = events.shift()!;

	if (!is.number(bodySize)) {
		t.is(lastEvent.percent, 0);
	}

	for (const [index, event] of events.entries()) {
		const isLastEvent = index === events.length - 1;

		if (is.number(bodySize)) {
			t.is(event.percent, event.transferred / bodySize);
			t.true(event.percent > lastEvent.percent);
			t.true(event.transferred > lastEvent.transferred);
		} else if (isLastEvent) {
			t.is(event.percent, 1);
			t.is(event.transferred, lastEvent.transferred);
			t.is(event.total, event.transferred);
		} else {
			t.is(event.percent, 0);
			t.true(event.transferred > lastEvent.transferred);
		}

		lastEvent = event;
	}
};

const file = Buffer.alloc(1024 * 1024 * 2);

const downloadEndpoint: Handler = (_request, response) => {
	response.setHeader('content-length', file.length);

	(async () => {
		try {
			await streamPipeline(
				stream.Readable.from(file),
				new SlowStream({maxWriteInterval: 50}),
				response,
			);
		} catch {}

		response.end();
	})();
};

const noTotalEndpoint: Handler = (_request, response) => {
	response.write('hello');
	response.end();
};

const uploadEndpoint: Handler = (request, response) => {
	(async () => {
		try {
			await streamPipeline(
				request,
				new SlowStream({maxWriteInterval: 100}),
			);
		} catch {}

		response.end();
	})();
};

test('download progress', withServer, async (t, server, got) => {
	server.get('/', downloadEndpoint);

	const events: Progress[] = [];

	const {body} = await got({responseType: 'buffer'})
		.on('downloadProgress', event => events.push(event));

	checkEvents(t, events, body.length);
});

test('download progress - missing total size', withServer, async (t, server, got) => {
	server.get('/', noTotalEndpoint);

	const events: Progress[] = [];

	await got('').on('downloadProgress', (event: Progress) => events.push(event));

	t.is(events[0]?.total, undefined);
	checkEvents(t, events);
});

test('download progress - stream', withServer, async (t, server, got) => {
	server.get('/', downloadEndpoint);

	const events: Progress[] = [];

	const stream = got.stream({responseType: 'buffer'})
		.on('downloadProgress', event => events.push(event));

	await getStream(stream);

	checkEvents(t, events, file.length);
});

test('upload progress - file', withServer, async (t, server, got) => {
	server.post('/', uploadEndpoint);

	const events: Progress[] = [];

	await got.post({body: file}).on('uploadProgress', (event: Progress) => events.push(event));

	checkEvents(t, events, file.length);
});

test('upload progress - file stream', withServer, async (t, server, got) => {
	server.post('/', uploadEndpoint);

	const path = temporaryFile();
	fs.writeFileSync(path, file);

	const {size} = await promisify(fs.stat)(path);

	const events: Progress[] = [];

	await got.post({
		body: fs.createReadStream(path),
		headers: {
			'content-length': size.toString(),
		},
	})
		.on('uploadProgress', (event: Progress) => events.push(event));

	checkEvents(t, events, file.length);
});

test('upload progress - form data', withServer, async (t, server, got) => {
	server.post('/', uploadEndpoint);

	const events: Progress[] = [];

	const body = new globalThis.FormData();
	body.set('key', 'value');
	body.set('file', new File([file], 'file'));

	await got.post({body}).on('uploadProgress', (event: Progress) => events.push(event));

	checkEvents(t, events);
});

test('upload progress - json', withServer, async (t, server, got) => {
	server.post('/', uploadEndpoint);

	const body = JSON.stringify({key: 'value'});
	const size = Buffer.byteLength(body);
	const events: Progress[] = [];

	await got.post({body}).on('uploadProgress', (event: Progress) => events.push(event));

	checkEvents(t, events, size);
});

test('upload progress - measures bytes correctly for non-UTF-8 encoded strings', withServer, async (t, server, got) => {
	server.post('/', uploadEndpoint);

	// String with emoji - 'Hello 👋' is 10 bytes in UTF-8, but 16 bytes in UTF-16LE
	const text = 'Hello 👋';
	const utf8Size = Buffer.from(text, 'utf8').byteLength; // 10 bytes
	const utf16Size = Buffer.from(text, 'utf16le').byteLength; // 16 bytes

	t.is(utf8Size, 10);
	t.is(utf16Size, 16);

	const events: Progress[] = [];

	// Upload as UTF-8 (default)
	await got.post({body: text}).on('uploadProgress', (event: Progress) => events.push(event));

	// Verify the progress measures UTF-8 bytes correctly
	const finalEvent = events.at(-1)!;
	t.is(finalEvent.transferred, utf8Size);
	t.is(finalEvent.total, utf8Size);
});

test('upload progress - stream with known body size', withServer, async (t, server, got) => {
	server.post('/', uploadEndpoint);

	const events: Progress[] = [];
	const options = {
		headers: {'content-length': file.length.toString()},
	};

	const request = got.stream.post(options)
		.on('uploadProgress', event => {
			events.push(event);
		});

	await streamPipeline(stream.Readable.from(file), request);
	await getStream(request);

	checkEvents(t, events, file.length);
});

test('upload progress - stream with unknown body size', withServer, async (t, server, got) => {
	server.post('/', uploadEndpoint);

	const events: Progress[] = [];

	const request = got.stream.post('')
		.on('uploadProgress', event => {
			events.push(event);
		});

	await streamPipeline(stream.Readable.from(file), request);
	await getStream(request);

	t.is(events[0]?.total, undefined);
	checkEvents(t, events);
});

test('upload progress - no body', withServer, async (t, server, got) => {
	server.post('/', uploadEndpoint);

	const events: Progress[] = [];

	await got.post('').on('uploadProgress', (event: Progress) => events.push(event));

	t.deepEqual(events, [
		{
			percent: 0,
			transferred: 0,
			total: undefined,
		},
		{
			percent: 1,
			transferred: 0,
			total: 0,
		},
	]);
});

test('upload progress - no events when immediately removed listener', withServer, async (t, server, got) => {
	server.post('/', uploadEndpoint);

	const events: Progress[] = [];

	const listener = (event: Progress) => events.push(event);

	const promise = got.post('')
		.on('uploadProgress', listener)
		.off('uploadProgress', listener);

	await promise;

	t.is(events.length, 0);
});

test('upload progress - one event when removed listener', withServer, async (t, server, got) => {
	server.post('/', uploadEndpoint);

	const events: Progress[] = [];

	const promise = got.post('');

	const listener = (event: Progress) => {
		events.push(event);
		void promise.off('uploadProgress', listener);
	};

	void promise.on('uploadProgress', listener);

	await promise;

	t.deepEqual(events, [
		{
			percent: 0,
			transferred: 0,
			total: undefined,
		},
	]);
});

test('does not emit uploadProgress after cancelation', withServer, async (t, server, got) => {
	server.post('/', () => {});

	const stream = got.stream.post();

	stream.once('uploadProgress', () => { // 0%
		stream.once('uploadProgress', () => { // 'foo'
			stream.write('bar');

			process.nextTick(() => {
				process.nextTick(() => {
					stream.on('uploadProgress', () => {
						t.fail('Emitted uploadProgress after cancelation');
					});

					stream.destroy();
				});
			});
		});
	});

	stream.write('foo');

	await pEvent(stream, 'close');

	t.pass();
});

test('upload progress - chunk generator with buffer', withServer, async (t, server, got) => {
	server.post('/', uploadEndpoint);

	const events: Progress[] = [];

	await got.post({
		body: chunk(file, 65_536),
		headers: {
			'content-length': file.length.toString(),
		},
	})
		.on('uploadProgress', (event: Progress) => events.push(event));

	checkEvents(t, events, file.length);

	// Ensure we got more than just 0% and 100%
	t.true(events.length > 2, `Expected more than 2 events with chunk, got ${events.length}`);
});

test('upload progress - chunkFromAsync async generator with stream', withServer, async (t, server, got) => {
	server.post('/', uploadEndpoint);

	const events: Progress[] = [];

	await got.post({
		body: chunkFromAsync(stream.Readable.from([file]), 65_536),
		headers: {
			'content-length': file.length.toString(),
		},
	})
		.on('uploadProgress', (event: Progress) => events.push(event));

	checkEvents(t, events, file.length);

	// Ensure we got more than just 0% and 100%
	t.true(events.length > 2, `Expected more than 2 events with chunkFromAsync, got ${events.length}`);
});

test('upload progress - buffer body', withServer, async (t, server, got) => {
	server.post('/', uploadEndpoint);

	const events: Progress[] = [];
	const body = Buffer.alloc(1024 * 256); // 256 KB

	await got.post({
		body,
		headers: {'content-length': body.byteLength.toString()},
	}).on('uploadProgress', (event: Progress) => events.push(event));

	checkEvents(t, events, body.byteLength);

	// Ensure we got more than just 0% and 100%
	t.true(events.length > 2, `Expected more than 2 events with buffer body, got ${events.length}`);
});

test('upload progress - typed array body', withServer, async (t, server, got) => {
	server.post('/', uploadEndpoint);

	const events: Progress[] = [];
	const body = new Uint8Array(1024 * 256); // 256 KB

	await got.post({
		body,
		headers: {'content-length': body.byteLength.toString()},
	}).on('uploadProgress', (event: Progress) => events.push(event));

	checkEvents(t, events, body.byteLength);

	// Ensure we got more than just 0% and 100%
	t.true(events.length > 2, `Expected more than 2 events with typed array body, got ${events.length}`);
});

test('upload progress - small json option', withServer, async (t, server, got) => {
	server.post('/', uploadEndpoint);

	const events: Progress[] = [];
	const payload = {key: 'value'};
	const size = Buffer.byteLength(JSON.stringify(payload));

	await got.post({json: payload}).on('uploadProgress', (event: Progress) => events.push(event));

	checkEvents(t, events, size);
});

test('upload progress - json option', withServer, async (t, server, got) => {
	server.post('/', uploadEndpoint);

	const events: Progress[] = [];
	const payload = {key: '.'.repeat(1e6)};
	const size = Buffer.byteLength(JSON.stringify(payload));

	await got.post({json: payload}).on('uploadProgress', (event: Progress) => events.push(event));

	checkEvents(t, events, size);

	// Ensure we got more than just 0% and 100%
	t.true(events.length > 2, `Expected more than 2 events with json option, got ${events.length}`);
});

test('upload progress - form option', withServer, async (t, server, got) => {
	server.post('/', uploadEndpoint);

	const events: Progress[] = [];
	const payload = {key: '.'.repeat(1e6)};
	const size = Buffer.byteLength(new URLSearchParams(payload).toString());

	await got.post({form: payload}).on('uploadProgress', (event: Progress) => events.push(event));

	checkEvents(t, events, size);

	// Ensure we got more than just 0% and 100%
	t.true(events.length > 2, `Expected more than 2 events with form option, got ${events.length}`);
});
```

## File: `test/promise.ts`
```typescript
import {Buffer} from 'node:buffer';
import {ReadStream} from 'node:fs';
import {ClientRequest} from 'node:http';
import test from 'ava';
import {type Response, AbortError} from '../source/index.js';
import withServer from './helpers/with-server.js';

test('emits request event as promise', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 200;
		response.end('null');
	});

	await got('').json().on('request', (request: ClientRequest) => {
		t.true(request instanceof ClientRequest);
	});
});

test('emits response event as promise', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 200;
		response.end('null');
	});

	await got('').json().on('response', (response: Response) => {
		t.is(response.statusCode, 200);
		t.false(response.readable);
		t.is(response.statusCode, 200);
		t.true(response.ip === '127.0.0.1' || response.ip === '::1');
	});
});

test('returns Uint8Array on compressed response', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.setHeader('content-encoding', 'gzip');
		response.end();
	});

	const {body} = await got({decompress: false});
	if (!ArrayBuffer.isView(body)) {
		t.fail('Expected Uint8Array response body when `decompress` is false for compressed responses');
		return;
	}

	t.is(body.constructor.name, 'Uint8Array');

	t.false(Buffer.isBuffer(body));
});

test('no unhandled `The server aborted pending request` rejection', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 503;
		response.write('asdf');

		setTimeout(() => {
			response.end();
		}, 100);
	});

	await t.throwsAsync(got(''));
});

test('promise.json() can be called before a file stream body is open', withServer, async (t, server, got) => {
	server.post('/', (request, response) => {
		request.resume();
		request.once('end', () => {
			response.end('""');
		});
	});

	// @ts-expect-error @types/node has wrong types.
	const body = new ReadStream('', {
		fs: {
			open() {},
			read() {},
			close() {},
		},
	});

	const controller = new AbortController();

	const promise = got({body, signal: controller.signal});
	const checks = [
		t.throwsAsync(promise, {
			instanceOf: AbortError,
			code: 'ERR_ABORTED',
		}),
		t.throwsAsync(promise.json(), {
			instanceOf: AbortError,
			code: 'ERR_ABORTED',
		}),
	];

	controller.abort();

	await Promise.all(checks);
});

test('promise.json() does not fail when server returns an error', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 400;
		response.end('{}');
	});

	const promise = got('', {throwHttpErrors: false});
	await t.notThrowsAsync(promise.json());
});
```

## File: `test/redirects.ts`
```typescript
import {Buffer} from 'node:buffer';
import test from 'ava';
import type {Handler} from 'express';
import got, {MaxRedirectsError, RequestError} from '../source/index.js';
import withServer, {withHttpsServer} from './helpers/with-server.js';

const reachedHandler: Handler = (_request, response) => {
	const body = 'reached';

	response.writeHead(200, {
		'content-length': body.length,
	});
	response.end(body);
};

const finiteHandler: Handler = (_request, response) => {
	response.writeHead(302, {
		location: '/',
	});
	response.end();
};

const relativeHandler: Handler = (_request, response) => {
	response.writeHead(302, {
		location: '/',
	});
	response.end();
};

const unixProtocol: Handler = (_request, response) => {
	response.writeHead(302, {
		location: 'unix:/var/run/docker.sock:/containers/json',
	});
	response.end();
};

const unixHostname: Handler = (_request, response) => {
	response.writeHead(302, {
		location: 'http://unix:/var/run/docker.sock:/containers/json',
	});
	response.end();
};

test('cannot redirect to UNIX protocol when UNIX sockets are enabled', withServer, async (t, server, got) => {
	server.get('/protocol', unixProtocol);
	server.get('/hostname', unixHostname);

	const gotUnixSocketsEnabled = got.extend({enableUnixSockets: true});

	t.true(gotUnixSocketsEnabled.defaults.options.enableUnixSockets);

	await t.throwsAsync(gotUnixSocketsEnabled('protocol'), {
		message: 'Cannot redirect to UNIX socket',
		instanceOf: RequestError,
	});

	await t.throwsAsync(gotUnixSocketsEnabled('hostname'), {
		message: 'Cannot redirect to UNIX socket',
		instanceOf: RequestError,
	});
});

test('cannot redirect to UNIX protocol when UNIX sockets are not enabled', withServer, async (t, server, got) => {
	server.get('/protocol', unixProtocol);
	server.get('/hostname', unixHostname);

	const gotUnixSocketsDisabled = got.extend({enableUnixSockets: false});

	t.false(gotUnixSocketsDisabled.defaults.options.enableUnixSockets);

	await t.throwsAsync(gotUnixSocketsDisabled('protocol'), {
		message: 'Cannot redirect to UNIX socket',
		instanceOf: RequestError,
	});

	await t.throwsAsync(gotUnixSocketsDisabled('hostname'), {
		message: 'Cannot redirect to UNIX socket',
		instanceOf: RequestError,
	});
});

test('follows redirect', withServer, async (t, server, got) => {
	server.get('/', reachedHandler);
	server.get('/finite', finiteHandler);

	const {body, redirectUrls} = await got('finite');
	t.is(body, 'reached');
	t.deepEqual(redirectUrls.map(String), [`${server.url}/`]);
});

test('does not follow redirect when followRedirect is a function and returns false', withServer, async (t, server, got) => {
	server.get('/', reachedHandler);
	server.get('/finite', finiteHandler);

	const {body, statusCode} = await got('finite', {followRedirect: () => false});
	t.not(body, 'reached');
	t.is(statusCode, 302);
});

test('follows redirect when followRedirect is a function and returns true', withServer, async (t, server, got) => {
	server.get('/', reachedHandler);
	server.get('/finite', finiteHandler);

	const {body, redirectUrls} = await got('finite', {followRedirect: () => true});
	t.is(body, 'reached');
	t.deepEqual(redirectUrls.map(String), [`${server.url}/`]);
});

test('followRedirect gets plainResponse and does not follow', withServer, async (t, server, got) => {
	server.get('/temporary', (_request, response) => {
		response.writeHead(307, {
			location: '/redirect',
		});
		response.end();
	});

	const {statusCode} = await got('temporary', {
		followRedirect(response) {
			t.is(response.headers.location, '/redirect');
			return false;
		},
	});
	t.is(statusCode, 307);
});

test('follows 307, 308 redirect', withServer, async (t, server, got) => {
	server.get('/', reachedHandler);

	server.get('/temporary', (_request, response) => {
		response.writeHead(307, {
			location: '/',
		});
		response.end();
	});

	server.get('/permanent', (_request, response) => {
		response.writeHead(308, {
			location: '/',
		});
		response.end();
	});

	const temporaryBody = (await got('temporary')).body;
	t.is(temporaryBody, 'reached');

	const permBody = (await got('permanent')).body;
	t.is(permBody, 'reached');
});

test('does not follow redirect when disabled', withServer, async (t, server, got) => {
	server.get('/', finiteHandler);

	t.is((await got({followRedirect: false})).statusCode, 302);
});

test('relative redirect works', withServer, async (t, server, got) => {
	server.get('/', reachedHandler);
	server.get('/relative', relativeHandler);

	t.is((await got('relative')).body, 'reached');
});

test('throws on endless redirects - default behavior', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.writeHead(302, {
			location: server.url,
		});
		response.end();
	});

	const error = await t.throwsAsync<MaxRedirectsError>(got(''), {message: 'Redirected 10 times. Aborting.'});

	t.deepEqual(error?.response.redirectUrls.map(String), Array.from({length: 10}).fill(`${server.url}/`));
	t.is(error?.code, 'ERR_TOO_MANY_REDIRECTS');
});

test('custom `maxRedirects` option', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.writeHead(302, {
			location: server.url,
		});
		response.end();
	});

	const error = await t.throwsAsync<MaxRedirectsError>(got('', {maxRedirects: 5}), {message: 'Redirected 5 times. Aborting.'});

	t.deepEqual(error?.response.redirectUrls.map(String), Array.from({length: 5}).fill(`${server.url}/`));
	t.is(error?.code, 'ERR_TOO_MANY_REDIRECTS');
});

test('searchParams are not breaking redirects', withServer, async (t, server, got) => {
	server.get('/', reachedHandler);

	server.get('/relativeSearchParam', (request, response) => {
		t.is(request.query.bang, '1');

		response.writeHead(302, {
			location: '/',
		});
		response.end();
	});

	t.is((await got('relativeSearchParam', {searchParams: 'bang=1'})).body, 'reached');
});

test('redirects GET and HEAD requests', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.writeHead(308, {
			location: '/',
		});
		response.end();
	});

	await t.throwsAsync(got.get(''), {
		instanceOf: MaxRedirectsError,
		code: 'ERR_TOO_MANY_REDIRECTS',
	});
});

test('redirects POST requests', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.writeHead(308, {
			location: '/',
		});
		response.end();
	});

	await t.throwsAsync(got.post({body: 'wow'}), {
		instanceOf: MaxRedirectsError,
		code: 'ERR_TOO_MANY_REDIRECTS',
	});
});

test('redirects on 303 if GET or HEAD', withServer, async (t, server, got) => {
	server.get('/', reachedHandler);

	server.head('/seeOther', (_request, response) => {
		response.writeHead(303, {
			location: '/',
		});
		response.end();
	});

	const {url, headers, request} = await got.head('seeOther');
	t.is(url, `${server.url}/`);
	t.is(headers['content-length'], 'reached'.length.toString());
	t.is(request.options.method, 'HEAD');
});

test('removes body on GET redirect', withServer, async (t, server, got) => {
	server.get('/', (request, response) => {
		request.pipe(response);
	});

	server.post('/seeOther', (_request, response) => {
		response.writeHead(303, {
			location: '/',
		});
		response.end();
	});

	const {headers, body} = await got.post('seeOther', {body: 'hello'});
	t.is(body, '');
	t.is(headers['content-length'], '0');
});

test('redirects on 303 response even on post, put, delete', withServer, async (t, server, got) => {
	server.get('/', reachedHandler);

	server.post('/seeOther', (_request, response) => {
		response.writeHead(303, {
			location: '/',
		});
		response.end();
	});

	const {url, body} = await got.post('seeOther', {body: 'wow'});
	t.is(url, `${server.url}/`);
	t.is(body, 'reached');
});

test('redirects from http to https work', withServer, async (t, serverHttp) => {
	await withHttpsServer().exec(t, async (t, serverHttps, got) => {
		serverHttp.get('/', (_request, response) => {
			response.end('http');
		});

		serverHttps.get('/', (_request, response) => {
			response.end('https');
		});

		serverHttp.get('/httpToHttps', (_request, response) => {
			response.writeHead(302, {
				location: serverHttps.url,
			});
			response.end();
		});

		t.is((await got('httpToHttps', {
			prefixUrl: serverHttp.url,
		})).body, 'https');
	});
});

test('redirects from https to http work', withHttpsServer(), async (t, serverHttps, got) => {
	await withServer.exec(t, async (t, serverHttp) => {
		serverHttp.get('/', (_request, response) => {
			response.end('http');
		});

		serverHttps.get('/', (_request, response) => {
			response.end('https');
		});

		serverHttps.get('/httpsToHttp', (_request, response) => {
			response.writeHead(302, {
				location: serverHttp.url,
			});
			response.end();
		});

		t.is((await got('httpsToHttp', {
			prefixUrl: serverHttps.url,
		})).body, 'http');
	});
});

test('redirects works with lowercase method', withServer, async (t, server, got) => {
	server.get('/', reachedHandler);
	server.get('/relative', relativeHandler);

	const {body} = await got('relative', {method: 'head'});
	t.is(body, '');
});

test('redirect response contains new url', withServer, async (t, server, got) => {
	server.get('/', reachedHandler);
	server.get('/finite', finiteHandler);

	const {url} = await got('finite');
	t.is(url, `${server.url}/`);
});

test('redirect response contains old url', withServer, async (t, server, got) => {
	server.get('/', reachedHandler);
	server.get('/finite', finiteHandler);

	const {requestUrl} = await got('finite');
	t.is(requestUrl.toString(), `${server.url}/finite`);
});

test('redirect response contains UTF-8 with binary encoding', withServer, async (t, server, got) => {
	server.get('/utf8-url-%C3%A1%C3%A9', reachedHandler);

	server.get('/redirect-with-utf8-binary', (_request, response) => {
		response.writeHead(302, {
			location: Buffer.from((new URL('/utf8-url-áé', server.url)).toString(), 'utf8').toString('binary'),
		});
		response.end();
	});

	t.is((await got('redirect-with-utf8-binary')).body, 'reached');
});

test('redirect response contains UTF-8 with URI encoding', withServer, async (t, server, got) => {
	server.get('/', (request, response) => {
		t.is(request.query.test, 'it’s ok');
		response.end('reached');
	});

	server.get('/redirect-with-uri-encoded-location', (_request, response) => {
		response.writeHead(302, {
			location: new URL('/?test=it’s+ok', server.url).toString(),
		});
		response.end();
	});

	t.is((await got('redirect-with-uri-encoded-location')).body, 'reached');
});

test('throws on invalid redirect URL', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.writeHead(302, {
			location: 'http://',
		});
		response.end();
	});

	await t.throwsAsync(got(''), {
		code: 'ERR_INVALID_URL',
	});
});

test('redirect uses port from redirect URL, not from original request', withServer, async (t, server1, got) => {
	await withServer.exec(t, async (t, server2) => {
		server1.get('/', (_request, response) => {
			response.writeHead(307, {
				location: `http://localhost:${server2.port}/`,
			});
			response.end();
		});

		server2.get('/', (_request, response) => {
			response.end('ok');
		});

		const {body} = await got('');
		t.is(body, 'ok');
	});
});

test('body is reset on GET redirect', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.writeHead(303, {
			location: '/',
		});
		response.end();
	});

	server.get('/', (_request, response) => {
		response.end();
	});

	await got.post('', {
		body: 'foobar',
		hooks: {
			beforeRedirect: [
				options => {
					t.is(options.body, undefined);
				},
			],
		},
	});

	await got.post('', {
		json: {foo: 'bar'},
		hooks: {
			beforeRedirect: [
				options => {
					t.is(options.body, undefined);
				},
			],
		},
	});

	await got.post('', {
		form: {foo: 'bar'},
		hooks: {
			beforeRedirect: [
				options => {
					t.is(options.body, undefined);
				},
			],
		},
	});
});

test('body is passed on POST redirect', withServer, async (t, server, got) => {
	server.post('/redirect', (_request, response) => {
		response.writeHead(302, {
			location: '/',
		});
		response.end();
	});

	server.post('/', (request, response) => {
		request.pipe(response);
	});

	const {body} = await got.post('redirect', {
		body: 'foobar',
		hooks: {
			beforeRedirect: [
				options => {
					t.is(options.body, 'foobar');
				},
			],
		},
	});

	t.is(body, 'foobar');
});

test('large body is preserved on 307 redirect', withServer, async (t, server, got) => {
	const requestBody = Buffer.alloc(1024 * 1024 * 2, 'a');

	server.post('/redirect', async (request, response) => {
		for await (const receivedChunk of request) {
			void receivedChunk;
		}

		response.writeHead(307, {
			location: '/target',
		});
		response.end();
	});

	server.post('/target', async (request, response) => {
		const receivedChunks: Uint8Array[] = [];

		for await (const receivedChunk of request) {
			receivedChunks.push(Buffer.from(receivedChunk));
		}

		const receivedBody = Buffer.concat(receivedChunks);

		t.true(receivedBody.equals(requestBody));
		response.end('ok');
	});

	const {body} = await got.post('redirect', {
		body: requestBody,
		retry: {
			limit: 0,
		},
	});

	t.is(body, 'ok');
});

test('injected request close before response emits pending request abort error', withServer, async (t, server, got) => {
	server.get('/pending-close', (_request, _response) => {
		// Keep request open until client-side close is injected below.
	});

	const pendingRequest = got('pending-close').on('request', clientRequest => {
		// Simulate the pre-response close edge case directly on the request object.
		clientRequest.emit('close');
	});

	const error = await t.throwsAsync<RequestError>(pendingRequest, {
		instanceOf: RequestError,
		message: 'The server aborted pending request',
	});

	t.is(error?.code, 'ECONNRESET');
});

test('method rewriting', withServer, async (t, server, got) => {
	server.post('/redirect', (_request, response) => {
		response.writeHead(302, {
			location: '/',
		});
		response.end();
	});
	server.get('/', (_request, response) => {
		response.end();
	});

	server.post('/temporaryRedirect', (_request, response) => {
		response.writeHead(307, {
			location: '/',
		});
		response.end();
	});
	server.post('/', (request, response) => {
		request.pipe(response);
	});

	const {body} = await got.post('redirect', {
		body: 'foobar',
		methodRewriting: true,
		hooks: {
			beforeRedirect: [
				options => {
					t.is(options.body, undefined);
				},
			],
		},
	});

	t.is(body, '');

	// Do not rewrite method on 307 or 308
	const {body: temporaryRedirectBody} = await got.post('temporaryRedirect', {
		body: 'foobar',
		methodRewriting: true,
		hooks: {
			beforeRedirect: [
				options => {
					t.is(options.body, 'foobar');
				},
			],
		},
	});

	t.is(temporaryRedirectBody, 'foobar');
});

test('upload progress total is reset on redirected GET request', withServer, async (t, server, got) => {
	server.post('/redirect-upload-progress', (_request, response) => {
		response.writeHead(303, {
			location: '/redirect-upload-progress-target',
		});
		response.end();
	});
	server.get('/redirect-upload-progress-target', (_request, response) => {
		response.end('ok');
	});

	const events: Array<{transferred: number; total: number | undefined}> = [];
	const requestMethods: string[] = [];
	const {body} = await got.post('redirect-upload-progress', {
		body: 'foobar',
		retry: {
			limit: 0,
		},
	}).on('request', request => {
		requestMethods.push(request.method ?? '');
	}).on('uploadProgress', event => {
		events.push({
			transferred: event.transferred,
			total: event.total,
		});
	});

	t.is(body, 'ok');
	t.deepEqual(requestMethods, ['POST', 'GET']);

	const zeroTransferredEvents = events.filter(event => event.transferred === 0);
	t.true(zeroTransferredEvents.length >= 2);

	const redirectedRequestEvent = zeroTransferredEvents.at(-1);
	t.truthy(redirectedRequestEvent);
	t.is(redirectedRequestEvent?.total, undefined);
});

test('clears username and password when redirecting to a different hostname', withServer, async (t, server1, got) => {
	await withServer.exec(t, async (t, server2) => {
		server1.get('/', (_request, response) => {
			response.writeHead(302, {
				location: `http://localhost:${server2.port}/`,
			});
			response.end();
		});

		server2.get('/', (request, response) => {
			response.end(JSON.stringify({headers: request.headers}));
		});

		const {headers} = await got('', {
			username: 'hello',
			password: 'world',
		}).json<{headers: Record<string, string | undefined>}>();
		t.is(headers.authorization, undefined);
	});
});

test('clears the authorization header when redirecting to a different hostname', withServer, async (t, server1, got) => {
	await withServer.exec(t, async (t, server2) => {
		server1.get('/', (_request, response) => {
			response.writeHead(302, {
				location: `http://localhost:${server2.port}/`,
			});
			response.end();
		});

		server2.get('/', (request, response) => {
			response.end(JSON.stringify({headers: request.headers}));
		});

		const {headers} = await got('', {
			headers: {
				authorization: 'Basic aGVsbG86d29ybGQ=',
			},
		}).json<{headers: Record<string, string | undefined>}>();
		t.is(headers.authorization, undefined);
	});
});

test('clears credentials and sensitive headers when redirecting to a different protocol on the same hostname', withHttpsServer(), async (t, serverHttps, got) => {
	await withServer.exec(t, async (t, serverHttp) => {
		serverHttps.get('/', (_request, response) => {
			response.writeHead(302, {
				location: `http://${serverHttp.hostname}:${serverHttp.port}/target`,
			});
			response.end();
		});

		serverHttp.get('/target', (request, response) => {
			response.end(JSON.stringify(request.headers));
		});

		const headers = await got('', {
			username: 'hello',
			password: 'world',
			headers: {
				cookie: 'session=123',
			},
		}).json<Record<string, string | undefined>>();

		t.is(headers.authorization, undefined);
		t.is(headers.cookie, undefined);
	});
});

test('preserves userinfo on redirect to the same origin', withServer, async (t, server) => {
	server.get('/redirect', (_request, response) => {
		response.writeHead(303, {
			location: `http://localhost:${server.port}/`,
		});
		response.end();
	});

	server.get('/', (request, response) => {
		t.is(request.headers.authorization, 'Basic aGVsbG86d29ybGQ=');
		response.end();
	});

	await got(`http://hello:world@localhost:${server.port}/redirect`);
});

test('clears the host header when redirecting to a different hostname', withServer, async (t, server1, got) => {
	await withServer.exec(t, async (t, server2) => {
		server1.get('/redirect', (_request, response) => {
			response.writeHead(302, {
				location: `http://localhost:${server2.port}/`,
			});
			response.end();
		});

		server2.get('/', (request, response) => {
			response.end(request.headers.host);
		});

		const resp = await got('redirect', {headers: {host: 'wrongsite.com'}});
		t.is(resp.body, `localhost:${server2.port}`);
	});
});

test('correct port on redirect', withServer, async (t, server1, got) => {
	await withServer.exec(t, async (t, server2) => {
		server1.get('/redirect', (_request, response) => {
			response.redirect(`http://${server2.hostname}:${server2.port}/`);
		});

		server1.get('/', (_request, response) => {
			response.end('SERVER1');
		});

		server2.get('/', (_request, response) => {
			response.end('SERVER2');
		});

		const response = await got(`${server1.url}/redirect`, {prefixUrl: ''});

		t.is(response.body, 'SERVER2');
	});
});

test('downloadProgress does not fire for redirect responses', withServer, async (t, server, got) => {
	const body = Buffer.alloc(1024);

	server.get('/', (_request, response) => {
		response.writeHead(200, {
			'content-length': body.length,
		});
		response.end(body);
	});

	server.get('/redirect', (_request, response) => {
		response.writeHead(302, {
			location: '/',
			'content-length': '0',
		});
		response.end();
	});

	const progressEvents: Array<{transferred: number; total?: number}> = [];

	await got('redirect', {responseType: 'buffer'})
		.on('downloadProgress', event => {
			progressEvents.push({transferred: event.transferred, total: event.total});
		});

	// Should have at least 2 events: initial and final
	// All events should be for the final response (total = 1024), not the redirect
	t.true(progressEvents.length >= 2);

	// First event should be initial progress for final response
	t.is(progressEvents[0]?.transferred, 0);
	t.is(progressEvents[0]?.total, 1024);

	// Last event should be completion
	const lastEvent = progressEvents.at(-1)!;
	t.is(lastEvent.transferred, 1024);
	t.is(lastEvent.total, 1024);

	// All events should have total = 1024 (the final response size, not 0 from redirect)
	for (const event of progressEvents) {
		t.is(event.total, 1024);
	}
});
```

## File: `test/response-parse.ts`
```typescript
import {Buffer} from 'node:buffer';
import test from 'ava';
import type {Handler} from 'express';
import getStream from 'get-stream';
import {HTTPError, ParseError} from '../source/index.js';
import withServer from './helpers/with-server.js';

const dog = {data: 'dog'};
const jsonResponse = JSON.stringify(dog);

const defaultHandler: Handler = (_request, response) => {
	response.end(jsonResponse);
};

test('`options.resolveBodyOnly` works', withServer, async (t, server, got) => {
	server.get('/', defaultHandler);

	t.deepEqual(await got<Record<string, unknown>>({responseType: 'json', resolveBodyOnly: true}), dog);
});

test('`options.resolveBodyOnly` combined with `options.throwHttpErrors`', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 404;
		response.end('/');
	});

	t.is(await got({resolveBodyOnly: true, throwHttpErrors: false}), '/');
});

test('JSON response', withServer, async (t, server, got) => {
	server.get('/', defaultHandler);

	t.deepEqual((await got({responseType: 'json'})).body, dog);
});

test('Uint8Array response', withServer, async (t, server, got) => {
	server.get('/', defaultHandler);

	const {body} = await got({responseType: 'buffer'});
	t.deepEqual(body, new TextEncoder().encode(jsonResponse));
	t.true(body instanceof Uint8Array);
	t.false(Buffer.isBuffer(body));
});

test('Text response', withServer, async (t, server, got) => {
	server.get('/', defaultHandler);

	t.is((await got({responseType: 'text'})).body, jsonResponse);
});

test('Text response #2', withServer, async (t, server, got) => {
	server.get('/', defaultHandler);

	t.is((await got({responseType: undefined})).body, jsonResponse);
});

test('Text response preserves UTF-8 BOM', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end(Buffer.from([0xEF, 0xBB, 0xBF, ...Buffer.from('hello')]));
	});

	t.is((await got({responseType: 'text'})).body, '\uFEFFhello');
});

test('JSON response - promise.json()', withServer, async (t, server, got) => {
	server.get('/', defaultHandler);

	t.deepEqual(await got('').json(), dog);
});

test('Uint8Array response - promise.buffer()', withServer, async (t, server, got) => {
	server.get('/', defaultHandler);

	const body = await got('').buffer();
	t.deepEqual(body, new TextEncoder().encode(jsonResponse));
	t.true(body instanceof Uint8Array);
	t.false(Buffer.isBuffer(body));
});

test('Text response - promise.text()', withServer, async (t, server, got) => {
	server.get('/', defaultHandler);

	t.is(await got('').text(), jsonResponse);
});

test('Text response - promise.json().text()', withServer, async (t, server, got) => {
	server.get('/', defaultHandler);

	t.is(await got('').json().text(), jsonResponse);
});

test('works if promise has been already resolved', withServer, async (t, server, got) => {
	server.get('/', defaultHandler);

	const promise = got('').text();
	t.is(await promise, jsonResponse);
	t.deepEqual(await promise.json(), dog);
});

test('throws an error on invalid response type', withServer, async (t, server, got) => {
	server.get('/', defaultHandler);

	// @ts-expect-error Error tests
	const error = await t.throwsAsync<ParseError>(got({responseType: 'invalid'}));
	t.is(error?.message, 'Invalid `responseType` option: invalid');
});

test('wraps parsing errors', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('/');
	});

	const error = await t.throwsAsync<ParseError>(got({responseType: 'json'}), {instanceOf: ParseError});
	t.true(error?.message.includes((error.options.url as URL).hostname));
	t.is((error?.options.url as URL).pathname, '/');
	t.is(error?.code, 'ERR_BODY_PARSE_FAILURE');
});

test('credentials are stripped from ParseError message URL', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('/');
	});

	const url = new URL(server.url);
	url.username = 'user';
	url.password = 'secret';

	const error = await t.throwsAsync<ParseError>(got(url, {responseType: 'json'}), {instanceOf: ParseError});
	t.false(error?.message.includes('user'));
	t.false(error?.message.includes('secret'));
	t.regex(error?.message ?? '', /in "http:\/\/localhost:\d+\/"$/);
});

test('JSON response with UTF-8 BOM throws ParseError', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end(Buffer.from([0xEF, 0xBB, 0xBF, ...Buffer.from(jsonResponse)]));
	});

	await t.throwsAsync(got({responseType: 'json'}), {instanceOf: ParseError});
});

test('parses non-200 responses', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 500;
		response.end(jsonResponse);
	});

	const error = await t.throwsAsync<HTTPError>(got({responseType: 'json', retry: {limit: 0}}), {instanceOf: HTTPError});
	t.deepEqual(error?.response.body, dog);
});

test('ignores errors on invalid non-200 responses', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 500;
		response.end('Internal error');
	});

	const error = await t.throwsAsync<HTTPError>(got({responseType: 'json', retry: {limit: 0}}), {
		instanceOf: HTTPError,
		message: /^Request failed with status code 500 \(Internal Server Error\): GET http:\/\/localhost:\d+\/$/,
	});

	t.is(error?.response.body, 'Internal error');
	t.is((error?.options.url as URL).pathname, '/');
});

test('parse errors have `response` property', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('/');
	});

	const error = await t.throwsAsync<ParseError>(got({responseType: 'json'}), {instanceOf: ParseError});

	t.is(error?.response.statusCode, 200);
	t.is(error?.response.body, '/');
	t.is(error?.code, 'ERR_BODY_PARSE_FAILURE');
});

test('sets correct headers', withServer, async (t, server, got) => {
	server.post('/', (request, response) => {
		response.end(JSON.stringify(request.headers));
	});

	const {body: headers} = await got.post<Record<string, string>>({responseType: 'json', json: {}});
	t.is(headers['content-type'], 'application/json');
	t.is(headers.accept, 'application/json');
});

test('doesn\'t throw on 204 No Content', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 204;
		response.end();
	});

	const body = await got('').json();
	t.is(body, '');
});

test('doesn\'t throw on empty bodies', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 200;
		response.end();
	});

	const body = await got('').json();
	t.is(body, '');
});

test('.buffer() returns binary content', withServer, async (t, server, got) => {
	const body = Buffer.from('89504E470D0A1A0A0000000D49484452', 'hex');

	server.get('/', (_request, response) => {
		response.end(body);
	});

	const buffer = await got('').buffer();
	t.is(Buffer.compare(buffer, body), 0);
});

test('shortcuts throw ParseErrors', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('not a json');
	});

	await t.throwsAsync(got('').json(), {
		instanceOf: ParseError,
		message: /^Unexpected token/,
		code: 'ERR_BODY_PARSE_FAILURE',
	});
});

test('shortcuts result properly when retrying in afterResponse', withServer, async (t, server, got) => {
	const nasty = JSON.stringify({hello: 'nasty'});
	const proper = JSON.stringify({hello: 'world'});

	server.get('/', (request, response) => {
		if (request.headers.token === 'unicorn') {
			response.end(proper);
		} else {
			response.statusCode = 401;
			response.end(nasty);
		}
	});

	const promise = got({
		hooks: {
			afterResponse: [
				(response, retryWithMergedOptions) => {
					if (response.statusCode === 401) {
						return retryWithMergedOptions({
							headers: {
								token: 'unicorn',
							},
						});
					}

					return response;
				},
			],
		},
	});

	const json = await promise.json<{hello: string}>();
	const text = await promise.text();
	const buffer = await promise.buffer();

	t.is(json.hello, 'world');
	t.is(text, proper);
	t.is(Buffer.from(buffer).compare(Buffer.from(proper)), 0);
});

test('responseType is optional when using template', withServer, async (t, server, got) => {
	const data = {hello: 'world'};

	server.post('/', async (request, response) => {
		response.end(await getStream(request));
	});

	const jsonClient = got.extend({responseType: 'json'});
	const {body} = await jsonClient.post<typeof data>('', {json: data});

	t.deepEqual(body, data);
});

test('JSON response custom parser', withServer, async (t, server, got) => {
	server.get('/', defaultHandler);

	t.deepEqual((await got({
		responseType: 'json',
		parseJson: text => ({...JSON.parse(text), custom: 'parser'}),
	})).body, {...dog, custom: 'parser'});
});

test.serial('incrementally decodes UTF-8 text response while downloading', withServer, async (t, server, got) => {
	if (globalThis.TextDecoder === undefined) {
		t.pass();
		return;
	}

	const originalDecode = globalThis.TextDecoder.prototype.decode;
	let responseEnded = false;
	let streamDecodeCallCount = 0;
	let decodedBeforeResponseEnded = false;

	globalThis.TextDecoder.prototype.decode = function (input?: BufferSource, options?: TextDecodeOptions): string {
		if (options?.stream) {
			streamDecodeCallCount++;
			if (!responseEnded) {
				decodedBeforeResponseEnded = true;
			}
		}

		return originalDecode.call(this, input, options);
	};

	server.get('/', (_request, response) => {
		response.write('hello ');

		setTimeout(() => {
			responseEnded = true;
			response.end('world');
		}, 25);
	});

	try {
		const {body} = await got({responseType: 'text'});
		t.is(body, 'hello world');
		t.true(streamDecodeCallCount > 0);
		t.true(decodedBeforeResponseEnded);
	} finally {
		globalThis.TextDecoder.prototype.decode = originalDecode;
	}
});

test.serial('incrementally decodes UTF-8 JSON response while downloading', withServer, async (t, server, got) => {
	if (globalThis.TextDecoder === undefined) {
		t.pass();
		return;
	}

	const originalDecode = globalThis.TextDecoder.prototype.decode;
	let responseEnded = false;
	let streamDecodeCallCount = 0;
	let decodedBeforeResponseEnded = false;

	globalThis.TextDecoder.prototype.decode = function (input?: BufferSource, options?: TextDecodeOptions): string {
		if (options?.stream) {
			streamDecodeCallCount++;
			if (!responseEnded) {
				decodedBeforeResponseEnded = true;
			}
		}

		return originalDecode.call(this, input, options);
	};

	server.get('/', (_request, response) => {
		response.write('{"hello":"');

		setTimeout(() => {
			responseEnded = true;
			response.end('world"}');
		}, 25);
	});

	try {
		const {body} = await got<{hello: string}>({responseType: 'json'});
		t.deepEqual(body, {hello: 'world'});
		t.true(streamDecodeCallCount > 0);
		t.true(decodedBeforeResponseEnded);
	} finally {
		globalThis.TextDecoder.prototype.decode = originalDecode;
	}
});

test.serial('falls back to buffered decode when incremental decode throws', withServer, async (t, server, got) => {
	if (globalThis.TextDecoder === undefined) {
		t.pass();
		return;
	}

	const originalDecode = globalThis.TextDecoder.prototype.decode;
	const payload = {hello: 'world'};
	let thrown = false;

	globalThis.TextDecoder.prototype.decode = function (input?: BufferSource, options?: TextDecodeOptions): string {
		if (!thrown && options?.stream) {
			thrown = true;
			throw new TypeError('Injected decode failure');
		}

		return originalDecode.call(this, input, options);
	};

	server.get('/', (_request, response) => {
		response.end(JSON.stringify(payload));
	});

	try {
		const {body} = await got<typeof payload>({responseType: 'json'});
		t.true(thrown);
		t.deepEqual(body, payload);
	} finally {
		globalThis.TextDecoder.prototype.decode = originalDecode;
	}
});

test.serial('falls back to buffered decode when incremental decoder final flush throws', withServer, async (t, server, got) => {
	if (globalThis.TextDecoder === undefined) {
		t.pass();
		return;
	}

	const originalDecode = globalThis.TextDecoder.prototype.decode;
	const payload = {hello: 'world'};
	let thrown = false;

	globalThis.TextDecoder.prototype.decode = function (input?: BufferSource, options?: TextDecodeOptions): string {
		if (!thrown && options === undefined) {
			thrown = true;
			throw new TypeError('Injected final flush decode failure');
		}

		return originalDecode.call(this, input, options);
	};

	server.get('/', (_request, response) => {
		response.end(JSON.stringify(payload));
	});

	try {
		const {body} = await got<typeof payload>({responseType: 'json'});
		t.true(thrown);
		t.deepEqual(body, payload);
	} finally {
		globalThis.TextDecoder.prototype.decode = originalDecode;
	}
});

test.serial('does not incrementally decode for non-UTF-8 encoding', withServer, async (t, server, got) => {
	if (globalThis.TextDecoder === undefined) {
		t.pass();
		return;
	}

	const originalDecode = globalThis.TextDecoder.prototype.decode;
	const payload = 'a'.repeat(1024);
	let streamDecodeCallCount = 0;

	globalThis.TextDecoder.prototype.decode = function (input?: BufferSource, options?: TextDecodeOptions): string {
		if (options?.stream) {
			streamDecodeCallCount++;
		}

		return originalDecode.call(this, input, options);
	};

	server.get('/', (_request, response) => {
		response.end(payload);
	});

	try {
		const {body} = await got({
			responseType: 'text',
			encoding: 'base64',
		});

		t.is(body, Buffer.from(payload).toString('base64'));
		t.is(streamDecodeCallCount, 0);
	} finally {
		globalThis.TextDecoder.prototype.decode = originalDecode;
	}
});

test.serial('incrementally decodes for case-insensitive UTF-8 encoding names', withServer, async (t, server, got) => {
	if (globalThis.TextDecoder === undefined) {
		t.pass();
		return;
	}

	const originalDecode = globalThis.TextDecoder.prototype.decode;
	const payload = 'hello world';
	const encoding = Buffer.from([85, 84, 70, 45, 56]).toString() as BufferEncoding;
	let streamDecodeCallCount = 0;

	globalThis.TextDecoder.prototype.decode = function (input?: BufferSource, options?: TextDecodeOptions): string {
		if (options?.stream) {
			streamDecodeCallCount++;
		}

		return originalDecode.call(this, input, options);
	};

	server.get('/', (_request, response) => {
		response.end(payload);
	});

	try {
		const encodingWithoutHyphen = Buffer.from([85, 84, 70, 56]).toString() as BufferEncoding;
		const responses = await Promise.all([
			got({
				responseType: 'text',
				encoding,
			}),
			got({
				responseType: 'text',
				encoding: encodingWithoutHyphen,
			}),
		]);

		for (const response of responses) {
			t.is(response.body, payload);
		}

		t.true(streamDecodeCallCount > 0);
	} finally {
		globalThis.TextDecoder.prototype.decode = originalDecode;
	}
});

test.serial('does not incrementally decode in stream mode', withServer, async (t, server, got) => {
	if (globalThis.TextDecoder === undefined) {
		t.pass();
		return;
	}

	const originalDecode = globalThis.TextDecoder.prototype.decode;
	let streamDecodeCallCount = 0;

	globalThis.TextDecoder.prototype.decode = function (input?: BufferSource, options?: TextDecodeOptions): string {
		if (options?.stream) {
			streamDecodeCallCount++;
		}

		return originalDecode.call(this, input, options);
	};

	server.get('/', (_request, response) => {
		response.end('hello');
	});

	try {
		await new Promise<void>((resolve, reject) => {
			const streamRequest = got.stream({responseType: 'text'});
			streamRequest.on('error', reject);
			streamRequest.on('end', resolve);
			streamRequest.resume();
		});

		t.is(streamDecodeCallCount, 0);
	} finally {
		globalThis.TextDecoder.prototype.decode = originalDecode;
	}
});
```

## File: `test/retry.ts`
```typescript
import {EventEmitter} from 'node:events';
import {PassThrough as PassThroughStream} from 'node:stream';
import type {Socket} from 'node:net';
import http from 'node:http';
import https from 'node:https';
import test from 'ava';
import is from '@sindresorhus/is';
import type {Handler} from 'express';
import getStream from 'get-stream';
import {pEvent} from 'p-event';
import got, {HTTPError, TimeoutError} from '../source/index.js';
import type Request from '../source/core/index.js';
import withServer from './helpers/with-server.js';

const retryAfterOn413 = 2;
const socketTimeout = 300;

const handler413: Handler = (_request, response) => {
	response.writeHead(413, {
		'Retry-After': retryAfterOn413,
	});
	response.end();
};

const createSocketTimeoutStream = (url: string): http.ClientRequest => {
	if (url.includes('https:')) {
		return https.request(url, {
			timeout: 1,
		});
	}

	return http.request(url, {
		timeout: socketTimeout,
	});
};

test('works on timeout', withServer, async (t, server, got) => {
	let knocks = 0;
	server.get('/', (_request, response) => {
		response.end('who`s there?');
	});

	t.is((await got({
		timeout: {
			socket: socketTimeout,
		},
		request(...arguments_: [
			string | URL | http.RequestOptions,
			(http.RequestOptions | ((response: http.IncomingMessage) => void))?,
			((response: http.IncomingMessage) => void)?,
		]) {
			if (knocks === 1) {
				// @ts-expect-error Overload error
				return http.request(...arguments_);
			}

			knocks++;
			return createSocketTimeoutStream(server.url);
		},
	})).body, 'who`s there?');
});

test('retry function gets iteration count', withServer, async (t, server, got) => {
	let knocks = 0;
	server.get('/', (_request, response) => {
		if (knocks++ === 1) {
			response.end('who`s there?');
			return;
		}

		response.statusCode = 500;
		response.end();
	});

	await got({
		retry: {
			calculateDelay({attemptCount}) {
				t.true(is.number(attemptCount));
				return attemptCount < 2 ? 1 : 0;
			},
		},
	});
});

test('setting to `0` disables retrying', async t => {
	await t.throwsAsync(got('https://example.com', {
		timeout: {socket: socketTimeout},
		retry: {
			calculateDelay({attemptCount}) {
				t.is(attemptCount, 1);
				return 0;
			},
		},
		request: () => createSocketTimeoutStream('https://example.com'),
	}), {
		instanceOf: TimeoutError,
		message: `Timeout awaiting 'socket' for ${socketTimeout}ms`,
	});
});

test('custom retries', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 500;
		response.end();
	});

	let hasTried = false;
	const error = await t.throwsAsync<HTTPError>(got({
		throwHttpErrors: true,
		retry: {
			calculateDelay({attemptCount}) {
				if (attemptCount === 1) {
					hasTried = true;
					return 1;
				}

				return 0;
			},
			methods: [
				'GET',
			],
			statusCodes: [
				500,
			],
		},
	}));
	t.is(error?.response.statusCode, 500);
	t.true(hasTried);
});

test('custom retries async', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 500;
		response.end();
	});

	let hasTried = false;
	const error = await t.throwsAsync<HTTPError>(got({
		throwHttpErrors: true,
		retry: {
			async calculateDelay({attemptCount}) {
				await new Promise(resolve => {
					setTimeout(resolve, 1000);
				});

				if (attemptCount === 1) {
					hasTried = true;
					return 1;
				}

				return 0;
			},
			methods: [
				'GET',
			],
			statusCodes: [
				500,
			],
		},
	}));
	t.is(error?.response.statusCode, 500);
	t.true(hasTried);
});

test('custom error codes', async t => {
	const errorCode = 'OH_SNAP';

	const error = await t.throwsAsync<Error & {code: typeof errorCode}>(got('https://example.com', {
		request() {
			const emitter = new EventEmitter() as http.ClientRequest;
			(emitter as any).end = () => {};
			(emitter as any).destroy = () => {};
			(emitter as any).writable = true;
			(emitter as any).writableEnded = false;

			const error = new Error('Snap!');
			(error as Error & {code: typeof errorCode}).code = errorCode;
			setTimeout(() => {
				emitter.emit('error', error);
			});

			return emitter;
		},
		retry: {
			calculateDelay({error}) {
				t.is(error.code, errorCode);
				return 0;
			},
			methods: [
				'GET',
			],
			errorCodes: [
				errorCode,
			],
		},
	}));

	t.is(error?.code, errorCode);
});

test('respects 413 Retry-After', withServer, async (t, server, got) => {
	let lastTried413access = Date.now();
	server.get('/', (_request, response) => {
		response.writeHead(413, {
			'Retry-After': retryAfterOn413,
		});
		response.end((Date.now() - lastTried413access).toString());

		lastTried413access = Date.now();
	});

	const {statusCode, body} = await got({
		throwHttpErrors: false,
		retry: {
			limit: 1,
		},
	});
	t.is(statusCode, 413);
	t.true(Number(body) >= retryAfterOn413 * 1000);
});

test('respects 413 Retry-After with RFC-1123 timestamp', withServer, async (t, server, got) => {
	let lastTried413TimestampAccess: string;
	server.get('/', (_request, response) => {
		const date = (new Date(Date.now() + (retryAfterOn413 * 1000))).toUTCString();

		response.writeHead(413, {
			'Retry-After': date,
		});
		response.end(lastTried413TimestampAccess);
		lastTried413TimestampAccess = date;
	});

	const {statusCode, body} = await got({
		throwHttpErrors: false,
		retry: {
			limit: 1,
		},
	});
	t.is(statusCode, 413);
	t.true(Date.now() >= Date.parse(body));
});

test('doesn\'t retry on 413 with empty statusCodes and methods', withServer, async (t, server, got) => {
	server.get('/', handler413);

	const {statusCode, retryCount} = await got({
		throwHttpErrors: false,
		retry: {
			limit: 1,
			statusCodes: [],
			methods: [],
		},
	});
	t.is(statusCode, 413);
	t.is(retryCount, 0);
});

test('doesn\'t retry on 413 with empty methods', withServer, async (t, server, got) => {
	server.get('/', handler413);

	const {statusCode, retryCount} = await got({
		throwHttpErrors: false,
		retry: {
			limit: 1,
			statusCodes: [413],
			methods: [],
		},
	});
	t.is(statusCode, 413);
	t.is(retryCount, 0);
});

test('doesn\'t retry on 413 without Retry-After header', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 413;
		response.end();
	});

	const {retryCount} = await got({
		throwHttpErrors: false,
	});
	t.is(retryCount, 0);
});

test('retries on 503 without Retry-After header', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 503;
		response.end();
	});

	const {retryCount} = await got({
		throwHttpErrors: false,
		retry: {
			limit: 1,
		},
	});
	t.is(retryCount, 1);
});

test('doesn\'t retry on streams', withServer, async (t, server, got) => {
	server.get('/', () => {});

	// @ts-expect-error Error tests
	const stream = got.stream({
		timeout: {
			request: 1,
		},
		retry: {
			calculateDelay() {
				t.fail('Retries on streams');
			},
		},
	});
	await t.throwsAsync(pEvent(stream, 'response'));
});

test('doesn\'t retry if Retry-After header is greater than maxRetryAfter', withServer, async (t, server, got) => {
	server.get('/', handler413);

	const {retryCount} = await got({
		retry: {maxRetryAfter: 1000},
		throwHttpErrors: false,
	});
	t.is(retryCount, 0);
});

test('doesn\'t retry when set to 0', withServer, async (t, server, got) => {
	server.get('/', handler413);

	const {statusCode, retryCount} = await got({
		throwHttpErrors: false,
		retry: {
			limit: 0,
		},
	});
	t.is(statusCode, 413);
	t.is(retryCount, 0);
});

test('works when defaults.options.retry is a number', withServer, async (t, server, got) => {
	server.get('/', handler413);

	const instance = got.extend({
		retry: {
			limit: 2,
		},
	});

	const {retryCount} = await instance({
		throwHttpErrors: false,
	});
	t.is(retryCount, 2);
});

test('retry function can throw', withServer, async (t, server, got) => {
	server.get('/', handler413);

	const error = 'Simple error';
	await t.throwsAsync(got({
		retry: {
			calculateDelay() {
				throw new Error(error);
			},
		},
	}), {message: error});
});

test('does not retry on POST', withServer, async (t, server, got) => {
	server.post('/', () => {});

	await t.throwsAsync(got.post({
		timeout: {
			request: 200,
		},
		hooks: {
			beforeRetry: [
				() => {
					t.fail('Retries on POST requests');
				},
			],
		},
	}), {instanceOf: TimeoutError});
});

test('does not break on redirect', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 500;
		response.end();
	});

	let tries = 0;
	server.get('/redirect', (_request, response) => {
		tries++;

		response.writeHead(302, {
			location: '/',
		});
		response.end();
	});

	await t.throwsAsync(got('redirect'), {message: /^Request failed with status code 500 \(Internal Server Error\): GET http:\/\/localhost:\d+\/$/});
	t.is(tries, 1);
});

test('does not destroy the socket on HTTP error', withServer, async (t, server, got) => {
	let returnServerError = true;

	server.get('/', (_request, response) => {
		if (returnServerError) {
			response.statusCode = 500;
			returnServerError = false;
		}

		response.end();
	});

	const sockets: Socket[] = [];

	const agent = new http.Agent({
		keepAlive: true,
	});

	await got('', {
		agent: {
			http: agent,
		},
	}).on('request', request => {
		sockets.push(request.socket!);
	});

	t.is(sockets.length, 2);
	t.is(sockets[0], sockets[1]);

	agent.destroy();
});

test('can retry a Got stream', withServer, async (t, server, got) => {
	let returnServerError = true;

	server.get('/', (_request, response) => {
		if (returnServerError) {
			response.statusCode = 500;
			response.end('not ok');

			returnServerError = false;
			return;
		}

		response.end('ok');
	});

	let globalRetryCount = 0;

	const responseStreamPromise = new Promise<PassThroughStream>((resolve, reject) => {
		let writeStream: PassThroughStream;

		const function_ = (retryStream?: Request) => {
			const stream = retryStream ?? got.stream('');

			globalRetryCount = stream.retryCount;

			if (writeStream) {
				writeStream.destroy();
			}

			writeStream = new PassThroughStream();

			stream.pipe(writeStream);

			stream.once('retry', (_retryCount, _error, createRetryStream) => {
				function_(createRetryStream());
			});

			stream.once('error', reject);
			stream.once('end', () => {
				resolve(writeStream);
			});
		};

		function_();
	});

	const responseStream = await responseStreamPromise;
	const data = await getStream(responseStream);

	t.is(data, 'ok');
	t.is(globalRetryCount, 1);
});

test('throws when cannot retry a Got stream', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.statusCode = 500;
		response.end('not ok');
	});

	let globalRetryCount = 0;

	const streamPromise = new Promise<PassThroughStream>((resolve, reject) => {
		const function_ = (retryStream?: Request) => {
			const stream = retryStream ?? got.stream('');

			globalRetryCount = stream.retryCount;

			stream.resume();
			stream.once('retry', (_retryCount, _error, createRetryStream) => {
				function_(createRetryStream());
			});

			stream.once('data', () => {
				stream.destroy(new Error('data event has been emitted'));
			});

			stream.once('error', reject);
			stream.once('end', resolve);
		};

		function_();
	});

	const error = await t.throwsAsync<HTTPError>(streamPromise, {
		instanceOf: HTTPError,
	});

	t.is(error?.response.statusCode, 500);
	t.is(error?.response.body, 'not ok');
	t.is(globalRetryCount, 2);
});

test('can attach only one retry listener to a stream', withServer, async (t, _server, got) => {
	const stream = got.stream('');

	t.notThrows(() => {
		stream.on('retry', () => {});
	});

	t.throws(() => {
		stream.on('retry', () => {});
	}, {
		message: 'A retry listener has been attached already.',
	});

	stream.destroy();
});

test('createRetryStream accepts options', withServer, async (t, server, got) => {
	let returnServerError = true;
	let receivedCustomHeader = false;

	server.get('/', (request, response) => {
		if (request.headers['x-custom-header'] === 'custom-value') {
			receivedCustomHeader = true;
		}

		if (returnServerError) {
			response.statusCode = 500;
			response.end('not ok');
			returnServerError = false;
			return;
		}

		response.end('ok');
	});

	const responseStreamPromise = new Promise<PassThroughStream>((resolve, reject) => {
		let writeStream: PassThroughStream;

		const function_ = (retryStream?: Request) => {
			const stream = retryStream ?? got.stream('');

			if (writeStream) {
				writeStream.destroy();
			}

			writeStream = new PassThroughStream();

			stream.pipe(writeStream);

			stream.once('retry', (_retryCount, _error, createRetryStream) => {
				// Pass custom options on retry
				function_(createRetryStream({
					headers: {
						'x-custom-header': 'custom-value',
					},
				}));
			});

			stream.once('error', reject);
			stream.once('end', () => {
				resolve(writeStream);
			});
		};

		function_();
	});

	const responseStream = await responseStreamPromise;
	const data = await getStream(responseStream);

	t.is(data, 'ok');
	t.true(receivedCustomHeader);
});

test('createRetryStream re-copies piped headers on retry', withServer, async (t, server, got) => {
	let returnServerError = true;

	server.put('/', (request, response) => {
		if (returnServerError) {
			returnServerError = false;
			response.statusCode = 500;
			response.end('not ok');
			return;
		}

		response.end(JSON.stringify(request.headers));
	});

	const responseStreamPromise = new Promise<PassThroughStream>((resolve, reject) => {
		let writeStream: PassThroughStream;
		let attempt = 0;

		const function_ = (retryStream?: Request) => {
			attempt++;
			const stream = retryStream ?? got.stream.put('', {copyPipedHeaders: true});

			if (writeStream) {
				writeStream.destroy();
			}

			writeStream = new PassThroughStream();
			const sourceStream = new PassThroughStream() as PassThroughStream & {headers: Record<string, string>};
			sourceStream.headers = {
				'x-custom-header': attempt === 1 ? 'first-value' : 'second-value',
			};

			sourceStream.pipe(stream);
			sourceStream.end('request body');
			stream.pipe(writeStream);

			stream.once('retry', (_retryCount, _error, createRetryStream) => {
				function_(createRetryStream());
			});

			stream.once('error', reject);
			stream.once('end', () => {
				if (stream.retryCount === 1) {
					resolve(writeStream);
				}
			});
		};

		function_();
	});

	const responseStream = await responseStreamPromise;
	const headers = JSON.parse(await getStream(responseStream)) as Record<string, string>;

	t.is(headers['x-custom-header'], 'second-value');
});

test('createRetryStream preserves explicit header omissions after undefined header pruning', withServer, async (t, server, got) => {
	let returnServerError = true;

	server.put('/', (request, response) => {
		if (returnServerError) {
			returnServerError = false;
			response.statusCode = 500;
			response.end('not ok');
			return;
		}

		response.end(JSON.stringify(request.headers));
	});

	const responseStreamPromise = new Promise<PassThroughStream>((resolve, reject) => {
		let writeStream: PassThroughStream;

		const function_ = (retryStream?: Request) => {
			const stream = retryStream ?? got.stream.put('', {
				copyPipedHeaders: true,
				headers: {
					authorization: undefined,
				},
			});

			if (writeStream) {
				writeStream.destroy();
			}

			writeStream = new PassThroughStream();
			const sourceStream = new PassThroughStream() as PassThroughStream & {headers: Record<string, string>};
			sourceStream.headers = {
				authorization: 'Bearer piped-token',
			};

			sourceStream.pipe(stream);
			sourceStream.end('request body');
			stream.pipe(writeStream);

			stream.once('retry', (_retryCount, _error, createRetryStream) => {
				function_(createRetryStream());
			});

			stream.once('error', reject);
			stream.once('end', () => {
				if (stream.retryCount === 1) {
					resolve(writeStream);
				}
			});
		};

		function_();
	});

	const responseStream = await responseStreamPromise;
	const headers = JSON.parse(await getStream(responseStream)) as Record<string, string | undefined>;

	t.is(headers.authorization, undefined);
});

test('createRetryStream re-copies piped headers after internal header additions on previous attempt', withServer, async (t, server, got) => {
	let returnServerError = true;
	let attempt = 0;

	server.put('/', (request, response) => {
		if (returnServerError) {
			returnServerError = false;
			response.statusCode = 500;
			response.end('not ok');
			return;
		}

		response.end(JSON.stringify(request.headers));
	});

	const responseStreamPromise = new Promise<PassThroughStream>((resolve, reject) => {
		let writeStream: PassThroughStream;

		const function_ = (retryStream?: Request) => {
			attempt++;
			const stream = retryStream ?? got.stream.put('', {copyPipedHeaders: true});

			if (writeStream) {
				writeStream.destroy();
			}

			writeStream = new PassThroughStream();
			const sourceStream = new PassThroughStream() as PassThroughStream & {headers: Record<string, string>};
			sourceStream.headers = attempt === 1
				? {}
				: {'accept-encoding': 'identity'};

			sourceStream.pipe(stream);
			sourceStream.end('request body');
			stream.pipe(writeStream);

			stream.once('retry', (_retryCount, _error, createRetryStream) => {
				function_(createRetryStream());
			});

			stream.once('error', reject);
			stream.once('end', () => {
				if (stream.retryCount === 1) {
					resolve(writeStream);
				}
			});
		};

		function_();
	});

	const responseStream = await responseStreamPromise;
	const headers = JSON.parse(await getStream(responseStream)) as Record<string, string>;

	t.is(headers['accept-encoding'], 'identity');
});

test('createRetryStream preserves header omission from direct header mutation', withServer, async (t, server, got) => {
	let returnServerError = true;

	server.put('/', (request, response) => {
		if (returnServerError) {
			returnServerError = false;
			response.statusCode = 500;
			response.end('not ok');
			return;
		}

		response.end(JSON.stringify(request.headers));
	});

	const responseStreamPromise = new Promise<PassThroughStream>((resolve, reject) => {
		let writeStream: PassThroughStream;

		const function_ = (retryStream?: Request) => {
			const stream = retryStream ?? got.stream.put('', {copyPipedHeaders: true});
			stream.options.headers.authorization = undefined;

			if (writeStream) {
				writeStream.destroy();
			}

			writeStream = new PassThroughStream();
			const sourceStream = new PassThroughStream() as PassThroughStream & {headers: Record<string, string>};
			sourceStream.headers = {
				authorization: 'Bearer piped-token',
			};

			sourceStream.pipe(stream);
			sourceStream.end('request body');
			stream.pipe(writeStream);

			stream.once('retry', (_retryCount, _error, createRetryStream) => {
				function_(createRetryStream());
			});

			stream.once('error', reject);
			stream.once('end', () => {
				if (stream.retryCount === 1) {
					resolve(writeStream);
				}
			});
		};

		function_();
	});

	const responseStream = await responseStreamPromise;
	const headers = JSON.parse(await getStream(responseStream)) as Record<string, string | undefined>;

	t.is(headers.authorization, undefined);
});

test('createRetryStream preserves mixed-case header omission from direct header mutation', withServer, async (t, server, got) => {
	let returnServerError = true;

	server.put('/', (request, response) => {
		if (returnServerError) {
			returnServerError = false;
			response.statusCode = 500;
			response.end('not ok');
			return;
		}

		response.end(JSON.stringify(request.headers));
	});

	const responseStreamPromise = new Promise<PassThroughStream>((resolve, reject) => {
		let writeStream: PassThroughStream;

		const function_ = (retryStream?: Request) => {
			const stream = retryStream ?? got.stream.put('', {copyPipedHeaders: true});
			stream.options.headers.Authorization = undefined;

			if (writeStream) {
				writeStream.destroy();
			}

			writeStream = new PassThroughStream();
			const sourceStream = new PassThroughStream() as PassThroughStream & {headers: Record<string, string>};
			sourceStream.headers = {
				authorization: 'Bearer piped-token',
			};

			sourceStream.pipe(stream);
			sourceStream.end('request body');
			stream.pipe(writeStream);

			stream.once('retry', (_retryCount, _error, createRetryStream) => {
				function_(createRetryStream());
			});

			stream.once('error', reject);
			stream.once('end', () => {
				if (stream.retryCount === 1) {
					resolve(writeStream);
				}
			});
		};

		function_();
	});

	const responseStream = await responseStreamPromise;
	const headers = JSON.parse(await getStream(responseStream)) as Record<string, string | undefined>;

	t.is(headers.authorization, undefined);
});

test('createRetryStream keeps username/password authorization precedence over piped authorization', withServer, async (t, server, got) => {
	let returnServerError = true;
	let attempt = 0;

	server.put('/', (request, response) => {
		if (returnServerError) {
			returnServerError = false;
			response.statusCode = 500;
			response.end('not ok');
			return;
		}

		response.end(JSON.stringify(request.headers));
	});

	const responseStreamPromise = new Promise<PassThroughStream>((resolve, reject) => {
		let writeStream: PassThroughStream;

		const function_ = (retryStream?: Request) => {
			attempt++;
			const stream = retryStream ?? got.stream.put('', {
				copyPipedHeaders: true,
				username: 'foo',
				password: 'bar',
			});

			if (writeStream) {
				writeStream.destroy();
			}

			writeStream = new PassThroughStream();
			const sourceStream = new PassThroughStream() as PassThroughStream & {headers: Record<string, string>};
			sourceStream.headers = attempt === 1
				? {}
				: {authorization: 'Bearer retry-token'};

			sourceStream.pipe(stream);
			sourceStream.end('request body');
			stream.pipe(writeStream);

			stream.once('retry', (_retryCount, _error, createRetryStream) => {
				function_(createRetryStream());
			});

			stream.once('error', reject);
			stream.once('end', () => {
				if (stream.retryCount === 1) {
					resolve(writeStream);
				}
			});
		};

		function_();
	});

	const responseStream = await responseStreamPromise;
	const headers = JSON.parse(await getStream(responseStream)) as Record<string, string>;

	t.is(headers.authorization, 'Basic Zm9vOmJhcg==');
});

test('promise does not retry when body is a stream', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.statusCode = 500;
		response.end('not ok');
	});

	const body = new PassThroughStream();
	body.end('hello');

	const response = await got.post({
		retry: {
			methods: ['POST'],
		},
		body,
		throwHttpErrors: false,
	});

	t.is(response.retryCount, 0);
});

test('reuses request options on retry', withServer, async (t, server, got) => {
	let first = true;
	server.get('/', (request, response) => {
		if (first) {
			first = false;
			return;
		}

		response.end(JSON.stringify(request.headers));
	});

	const {body, retryCount} = await got('', {timeout: {request: 1000}, responseType: 'json'});
	t.is(retryCount, 1);
	t.is((body as any).accept, 'application/json');
});

test('respects backoffLimit', withServer, async (t, server, got) => {
	let count = 0;
	let timestamp = Date.now();
	const data: number[] = [];

	server.get('/', (_request, response) => {
		count++;

		const now = Date.now();
		data.push(now - timestamp);
		timestamp = now;

		if (count === 3) {
			response.end(JSON.stringify(data));
		} else {
			response.statusCode = 408;
			response.end();
		}
	});

	const body = await got('', {
		retry: {
			backoffLimit: 0,
		},
	}).json<number[]>();

	t.is(body.length, 3);
	t.true(body[0]! < 400);
	t.true(body[1]! < 400);
	t.true(body[2]! < 400);
});

test('enforceRetryRules respects statusCodes with custom calculateDelay', withServer, async (t, server, got) => {
	let requestCount = 0;
	server.get('/', (_request, response) => {
		requestCount++;
		// Return 500 on first request, 429 on second, 200 on third
		if (requestCount === 1) {
			response.statusCode = 500;
		} else if (requestCount === 2) {
			response.statusCode = 429;
		}

		response.end();
	});

	const {statusCode, retryCount} = await got({
		throwHttpErrors: false,
		retry: {
			limit: 5,
			statusCodes: [429], // Should only retry on 429
			enforceRetryRules: true,
			calculateDelay({attemptCount}) {
				// Custom delay but should still respect statusCodes
				return attemptCount * 100;
			},
		},
	});

	// Should not retry on 500 (not in statusCodes list)
	t.is(statusCode, 500);
	t.is(retryCount, 0);
});

test('enforces retry rules by default with custom calculateDelay', withServer, async (t, server, got) => {
	let requestCount = 0;
	server.get('/', (_request, response) => {
		requestCount++;
		if (requestCount === 1) {
			response.statusCode = 500;
		} else if (requestCount === 2) {
			response.statusCode = 429;
		}

		response.end();
	});

	const {statusCode, retryCount} = await got({
		throwHttpErrors: false,
		retry: {
			limit: 5,
			statusCodes: [429],
			calculateDelay({attemptCount}) {
				return attemptCount * 100;
			},
		},
	});

	t.is(statusCode, 500);
	t.is(retryCount, 0);
});

test('enforceRetryRules respects limit with custom calculateDelay', withServer, async (t, server, got) => {
	let requestCount = 0;
	server.get('/', (_request, response) => {
		requestCount++;
		response.statusCode = 500;
		response.end();
	});

	const {retryCount} = await got({
		throwHttpErrors: false,
		retry: {
			limit: 2,
			enforceRetryRules: true,
			calculateDelay({attemptCount}) {
				// With enforceRetryRules, limit is enforced automatically
				return attemptCount * 100;
			},
		},
	});

	// Should stop at limit even with custom calculateDelay
	t.is(retryCount, 2);
	t.is(requestCount, 3); // Initial request + 2 retries
});

test('retries on stream errors like EPIPE when configured', async t => {
	let attemptCount = 0;
	let retryCount = 0;

	const error = await t.throwsAsync<Error & {code: string}>(got.post('https://example.com', {
		retry: {
			limit: 2,
			methods: ['POST'],
			errorCodes: ['EPIPE'],
		},
		hooks: {
			beforeRetry: [
				() => {
					retryCount++;
				},
			],
		},
		request() {
			attemptCount++;

			const emitter = new EventEmitter() as http.ClientRequest;
			(emitter as any).end = (callback: any) => {
				// Simulate EPIPE error from Node.js during write/end
				// This mimics what happens when a socket is torn down (e.g., AWS Lambda pause)
				const error = new Error('write EPIPE');
				(error as NodeJS.ErrnoException).code = 'EPIPE';

				if (callback) {
					setTimeout(() => {
						callback(error);
					}, 10);
				}
			};

			emitter.destroyed = false;

			(emitter as any).destroy = () => {
				emitter.destroyed = true;
			};

			(emitter as any).write = () => true;

			(emitter as any).writable = true;
			(emitter as any).writableEnded = false;

			return emitter;
		},
	}), {code: 'EPIPE'});

	// Should retry twice (limit: 2) for a total of 3 attempts
	t.is(attemptCount, 3);
	t.is(retryCount, 2);
	t.is(error?.code, 'EPIPE');
});

test('does not retry on stream errors when not in errorCodes', async t => {
	let attemptCount = 0;

	const error = await t.throwsAsync<Error & {code: string}>(got('https://example.com', {
		retry: {
			limit: 2,
			errorCodes: [], // Empty list means no errors should be retried
		},
		request() {
			attemptCount++;

			const emitter = new EventEmitter() as http.ClientRequest;
			(emitter as any).end = (callback: any) => {
				const error = new Error('write ETEST');
				(error as NodeJS.ErrnoException).code = 'ETEST';

				if (callback) {
					setTimeout(() => {
						callback(error);
					}, 10);
				}
			};

			emitter.destroyed = false;

			(emitter as any).destroy = () => {
				emitter.destroyed = true;
			};

			(emitter as any).write = () => true;

			(emitter as any).writable = true;
			(emitter as any).writableEnded = false;

			return emitter;
		},
	}), {code: 'ETEST'});

	// Should NOT retry since errorCodes is empty
	t.is(attemptCount, 1);
	t.is(error?.code, 'ETEST');
});

test('does not retry after promise settles (issue #1489)', async t => {
	let retryTriggered = false;

	const response = await got('https://example.com', {
		retry: {limit: 2, errorCodes: ['ECONNRESET']},
		hooks: {
			beforeRetry: [() => {
				retryTriggered = true;
			}],
		},
		request() {
			const emitter = new EventEmitter() as http.ClientRequest;
			(emitter as any).end = () => {};
			emitter.destroyed = false;
			(emitter as any).destroy = () => {
				emitter.destroyed = true;
			};

			(emitter as any).write = () => true;
			(emitter as any).writable = true;
			(emitter as any).writableEnded = false;

			setTimeout(() => {
				const incomingMessage = new PassThroughStream() as unknown as http.IncomingMessage;
				incomingMessage.statusCode = 200;
				incomingMessage.headers = {};

				emitter.emit('response', incomingMessage);

				setImmediate(() => {
					// @ts-expect-error PassThrough method
					incomingMessage.end('ok');
				});

				// Late error after response - should NOT trigger retry
				setTimeout(() => {
					const error = new Error('read ECONNRESET');
					(error as NodeJS.ErrnoException).code = 'ECONNRESET';
					emitter.emit('error', error);
				}, 10);
			});

			return emitter;
		},
		throwHttpErrors: false,
	});

	t.is(response.statusCode, 200);
	t.false(retryTriggered);
});
```

## File: `test/stream.ts`
```typescript
import process from 'node:process';
import {Buffer} from 'node:buffer';
import fs from 'node:fs';
import {Agent as HttpAgent, type ClientRequest} from 'node:http';
import stream, {Readable as ReadableStream, Writable} from 'node:stream';
import {pipeline as streamPipeline} from 'node:stream/promises';
import {Readable as Readable2} from 'readable-stream';
import test from 'ava';
import type {Handler} from 'express';
import getStream from 'get-stream';
import {pEvent} from 'p-event';
import is from '@sindresorhus/is';
import delay from 'delay';
import got, {HTTPError, RequestError} from '../source/index.js';
import type {Response} from '../source/core/response.js';
import withServer from './helpers/with-server.js';

const defaultHandler: Handler = (_request, response) => {
	response.writeHead(200, {
		unicorn: 'rainbow',
		'content-encoding': 'gzip',
	});
	response.end(Buffer.from('H4sIAAAAAAAA/8vPBgBH3dx5AgAAAA==', 'base64')); // 'ok'
};

const redirectHandler: Handler = (_request, response) => {
	response.writeHead(302, {
		location: '/',
	});
	response.end();
};

const postHandler: Handler = async (request, response) => {
	await streamPipeline(request, response);
};

const errorHandler: Handler = (_request, response) => {
	response.statusCode = 404;
	response.end();
};

const headersHandler: Handler = (request, response) => {
	response.end(JSON.stringify(request.headers));
};

const infiniteHandler: Handler = (_request, response) => {
	response.write('foobar');
};

test('reusedSocket getter', withServer, async (t, server, got) => {
	server.get('/', defaultHandler);

	const agent = new HttpAgent({keepAlive: true});

	const stream = got.stream('', {agent: {http: agent}});
	t.is(stream.reusedSocket, undefined);

	await pEvent(stream, 'response');

	stream.resume();
	await pEvent(stream, 'end');

	t.false(stream.reusedSocket);

	const secondStream = got.stream('', {agent: {http: agent}});
	secondStream.resume();
	await pEvent(secondStream, 'end');

	t.true(secondStream.reusedSocket);
});

test('`options.responseType` is ignored', withServer, async (t, server, got) => {
	server.get('/', defaultHandler);

	await t.notThrowsAsync(getStream(got.stream({responseType: 'json'})));
});

test('returns readable stream', withServer, async (t, server, got) => {
	server.get('/', defaultHandler);

	const data = await getStream(got.stream(''));
	t.is(data, 'ok');
});

test('returns writeable stream', withServer, async (t, server, got) => {
	server.post('/', postHandler);

	const stream = got.stream.post('');
	const promise = getStream(stream);
	stream.end('wow');

	t.is(await promise, 'wow');
});

test('does not throw if using stream and passing a json option', withServer, async (t, server, got) => {
	server.post('/', postHandler);

	await t.notThrowsAsync(getStream(got.stream.post({json: {}})));
});

test('does not throw if using stream and passing a form option', withServer, async (t, server, got) => {
	server.post('/', postHandler);

	await t.notThrowsAsync(getStream(got.stream.post({form: {}})));
});

test('has request event', withServer, async (t, server, got) => {
	server.get('/', defaultHandler);

	const stream = got.stream('');
	const request = await pEvent(stream, 'request') as ClientRequest;
	t.truthy(request);
	t.is(request.method, 'GET');

	await getStream(stream);
});

test('has redirect event', withServer, async (t, server, got) => {
	server.get('/', defaultHandler);
	server.get('/redirect', redirectHandler);

	const stream = got.stream('redirect');
	const [, {headers}] = await pEvent(stream, 'redirect', {multiArgs: true}) as [unknown, {headers: Record<string, string>}];
	t.is(headers.location, '/');

	await getStream(stream);
});

test('has response event', withServer, async (t, server, got) => {
	server.get('/', defaultHandler);

	const {statusCode} = await pEvent(got.stream(''), 'response') as Response;
	t.is(statusCode, 200);
});

test('has error event', withServer, async (t, server, got) => {
	server.get('/', errorHandler);

	const stream = got.stream('');
	await t.throwsAsync(pEvent(stream, 'response'), {
		instanceOf: HTTPError,
		message: /^Request failed with status code 404 \(Not Found\): GET http:\/\/localhost:\d+\/$/,
	});
});

test('has error event #2', async t => {
	const stream = got.stream('http://doesntexist');
	try {
		await pEvent(stream, 'response');
	} catch (error: any) {
		t.regex(error.code, /ENOTFOUND|EAI_AGAIN/);
	}
});

test('validation errors can be caught with synchronous error handler', withServer, async (t, _server, got) => {
	const stream = got.stream('', {
		// @ts-expect-error - Testing invalid option
		meaningless: 'option',
	});

	const error: any = await new Promise((resolve, reject) => {
		// Attach error handler immediately (synchronously)
		stream.on('error', error => {
			resolve(error);
		});

		// Timeout in case error is never emitted
		setTimeout(() => {
			reject(new Error('Error was not emitted'));
		}, 1000);
	});

	t.true(error instanceof Error);
	t.regex(error.message, /Unexpected option: meaningless/);
});

test('has response event if `options.throwHttpErrors` is false', withServer, async (t, server, got) => {
	server.get('/', errorHandler);

	const {statusCode} = await pEvent(got.stream({throwHttpErrors: false}), 'response') as Response;
	t.is(statusCode, 404);
});

test('accepts `options.body` as a Stream', withServer, async (t, server, got) => {
	server.post('/', postHandler);

	const stream = got.stream.post({body: ReadableStream.from('wow')});
	t.is(await getStream(stream), 'wow');
});

test('redirect response contains old url', withServer, async (t, server, got) => {
	server.get('/', defaultHandler);
	server.get('/redirect', redirectHandler);

	const {requestUrl} = await pEvent(got.stream('redirect'), 'response') as Response;
	t.is(requestUrl.toString(), `${server.url}/redirect`);
});

test('check for pipe method', withServer, (t, server, got) => {
	server.get('/', defaultHandler);

	const stream = got.stream('');
	t.true(is.function(stream.pipe));
	t.true(is.function(stream.on('foobar', () => {}).pipe));

	stream.destroy();
});

test('piping works', withServer, async (t, server, got) => {
	server.get('/', defaultHandler);

	t.is(await getStream(got.stream('')), 'ok');
	t.is(await getStream(got.stream('').on('foobar', () => {})), 'ok');
});

test('proxying headers works', withServer, async (t, server, got) => {
	server.get('/', defaultHandler);
	server.get('/proxy', async (_request, response) => {
		await streamPipeline(
			got.stream(''),
			response,
		);
	});

	const {headers, body} = await got('proxy');
	t.is(headers.unicorn, 'rainbow');
	t.is(headers['content-encoding'], undefined);
	t.is(headers['content-length'], undefined);
	t.is(body, 'ok');
});

test('piping server request to Got does not proxy headers by default', withServer, async (t, server, got) => {
	server.get('/', headersHandler);
	server.get('/proxy', async (request, response) => {
		await streamPipeline(
			request,
			got.stream(''),
			response,
		);
	});

	const headers: Record<string, string> = await got('proxy', {
		headers: {
			foo: 'bar',
		},
	}).json();
	t.is(headers.foo, undefined);
	t.truthy(headers['user-agent']); // Got's default user-agent should still be present
});

test('piping server request to Got proxies headers when copyPipedHeaders is true', withServer, async (t, server, got) => {
	server.get('/', headersHandler);
	server.get('/proxy', async (request, response) => {
		await streamPipeline(
			request,
			got.stream('', {copyPipedHeaders: true}),
			response,
		);
	});

	const {foo}: {foo: string} = await got('proxy', {
		headers: {
			foo: 'bar',
		},
	}).json();
	t.is(foo, 'bar');
});

test('piping server request to Got does not proxy headers when copyPipedHeaders is false', withServer, async (t, server, got) => {
	server.get('/', headersHandler);
	server.get('/proxy', async (request, response) => {
		await streamPipeline(
			request,
			got.stream('', {copyPipedHeaders: false}),
			response,
		);
	});

	const headers: Record<string, string> = await got('proxy', {
		headers: {
			foo: 'bar',
		},
	}).json();
	t.is(headers.foo, undefined);
	t.truthy(headers['user-agent']); // Got's default user-agent should still be present
});

test('explicit headers are not overwritten by piped headers when copyPipedHeaders is true', withServer, async (t, server, got) => {
	server.get('/', headersHandler);
	server.get('/proxy', async (request, response) => {
		await streamPipeline(
			request,
			got.stream('', {
				copyPipedHeaders: true,
				headers: {
					'x-custom': 'explicit-value',
				},
			}),
			response,
		);
	});

	const headers: Record<string, string> = await got('proxy', {
		headers: {
			'x-custom': 'piped-value',
		},
	}).json();
	t.is(headers['x-custom'], 'explicit-value');
});

test('headers from extended defaults are not overwritten by piped headers when copyPipedHeaders is true', withServer, async (t, server, got) => {
	server.get('/', headersHandler);

	const gotWithDefaultHeaders = got.extend({
		headers: {
			'x-custom': 'default-explicit-value',
		},
	});

	server.get('/proxy', async (request, response) => {
		await streamPipeline(
			request,
			gotWithDefaultHeaders.stream('', {
				copyPipedHeaders: true,
			}),
			response,
		);
	});

	const headers: Record<string, string> = await got('proxy', {
		headers: {
			'x-custom': 'piped-value',
		},
	}).json();
	t.is(headers['x-custom'], 'default-explicit-value');
});

test('explicitly omitted headers are not backfilled by piped headers when copyPipedHeaders is true', withServer, async (t, server, got) => {
	server.get('/', headersHandler);
	server.get('/proxy', async (request, response) => {
		await streamPipeline(
			request,
			got.stream('', {
				copyPipedHeaders: true,
				headers: {
					foo: undefined,
				},
			}),
			response,
		);
	});

	const headers: Record<string, string> = await got('proxy', {
		headers: {
			foo: 'piped-value',
		},
	}).json();
	t.is(headers.foo, undefined);
});

test('headers set by mutating stream options are not overwritten by piped headers', withServer, async (t, server, got) => {
	server.get('/', headersHandler);
	server.get('/proxy', async (request, response) => {
		const gotStream = got.stream('', {copyPipedHeaders: true});
		gotStream.options.headers['x-custom'] = 'explicit-value';

		await streamPipeline(
			request,
			gotStream,
			response,
		);
	});

	const headers: Record<string, string> = await got('proxy', {
		headers: {
			'x-custom': 'piped-value',
		},
	}).json();
	t.is(headers['x-custom'], 'explicit-value');
});

test('mixed-case headers set by mutating stream options are not overwritten by piped headers', withServer, async (t, server, got) => {
	server.get('/', headersHandler);
	server.get('/proxy', async (request, response) => {
		const gotStream = got.stream('', {copyPipedHeaders: true});
		gotStream.options.headers.Authorization = 'Bearer explicit-token';

		await streamPipeline(
			request,
			gotStream,
			response,
		);
	});

	const headers: Record<string, string> = await got('proxy', {
		headers: {
			authorization: 'Bearer piped-token',
		},
	}).json();
	t.is(headers.authorization, 'Bearer explicit-token');
});

test('mixed-case headers omitted by mutating stream options are not backfilled by piped headers', withServer, async (t, server, got) => {
	server.get('/', headersHandler);
	server.get('/proxy', async (request, response) => {
		const gotStream = got.stream('', {copyPipedHeaders: true});
		gotStream.options.headers.Authorization = undefined;

		await streamPipeline(
			request,
			gotStream,
			response,
		);
	});

	const headers: Record<string, string> = await got('proxy', {
		headers: {
			authorization: 'Bearer piped-token',
		},
	}).json();
	t.is(headers.authorization, undefined);
});

test('headers omitted by mutating stream options are not backfilled by piped headers', withServer, async (t, server, got) => {
	server.get('/', headersHandler);
	server.get('/proxy', async (request, response) => {
		const gotStream = got.stream('', {copyPipedHeaders: true});
		gotStream.options.headers.authorization = undefined;

		await streamPipeline(
			request,
			gotStream,
			response,
		);
	});

	const headers: Record<string, string> = await got('proxy', {
		headers: {
			authorization: 'Bearer piped-token',
		},
	}).json();
	t.is(headers.authorization, undefined);
});

test('deleted explicit headers can be backfilled by piped headers', withServer, async (t, server, got) => {
	server.get('/', headersHandler);
	server.get('/proxy', async (request, response) => {
		const gotStream = got.stream('', {
			copyPipedHeaders: true,
			headers: {
				'x-custom': 'explicit-value',
			},
		});
		delete gotStream.options.headers['x-custom'];

		await streamPipeline(
			request,
			gotStream,
			response,
		);
	});

	const headers: Record<string, string> = await got('proxy', {
		headers: {
			'x-custom': 'piped-value',
		},
	}).json();
	t.is(headers['x-custom'], 'piped-value');
});

test('explicit user-agent header is not overwritten by piped header', withServer, async (t, server, got) => {
	server.get('/', headersHandler);
	server.get('/proxy', async (request, response) => {
		await streamPipeline(
			request,
			got.stream('', {
				copyPipedHeaders: true,
				headers: {
					'user-agent': 'got (https://github.com/sindresorhus/got)',
				},
			}),
			response,
		);
	});

	const headers: Record<string, string> = await got('proxy', {
		headers: {
			'user-agent': 'piped-user-agent',
		},
	}).json();
	t.is(headers['user-agent'], 'got (https://github.com/sindresorhus/got)');
});

test('default-valued user-agent set by mutating stream options is not overwritten by piped header', withServer, async (t, server, got) => {
	server.get('/', headersHandler);
	server.get('/proxy', async (request, response) => {
		const gotStream = got.stream('', {copyPipedHeaders: true});
		gotStream.options.headers['user-agent'] = 'got (https://github.com/sindresorhus/got)';

		await streamPipeline(
			request,
			gotStream,
			response,
		);
	});

	const headers: Record<string, string> = await got('proxy', {
		headers: {
			'user-agent': 'piped-user-agent',
		},
	}).json();
	t.is(headers['user-agent'], 'got (https://github.com/sindresorhus/got)');
});

test('default user-agent is overwritten by piped user-agent when copyPipedHeaders is true', withServer, async (t, server, got) => {
	server.get('/', headersHandler);
	server.get('/proxy', async (request, response) => {
		await streamPipeline(
			request,
			got.stream('', {copyPipedHeaders: true}),
			response,
		);
	});

	const headers: Record<string, string> = await got('proxy', {
		headers: {
			'user-agent': 'custom-user-agent',
		},
	}).json();
	t.is(headers['user-agent'], 'custom-user-agent');
});

test('skips proxying headers after server has sent them already', withServer, async (t, server, got) => {
	server.get('/', defaultHandler);
	server.get('/proxy', async (_request, response) => {
		response.writeHead(200);

		await streamPipeline(
			got.stream(''),
			response,
		);
	});

	const {headers} = await got('proxy');
	t.is(headers.unicorn, undefined);
});

test('proxies `content-encoding` header when `options.decompress` is false', withServer, async (t, server, got) => {
	server.get('/', defaultHandler);
	server.get('/proxy', async (_request, response) => {
		await streamPipeline(
			got.stream({decompress: false}),
			response,
		);
	});

	const {headers} = await got('proxy', {decompress: false});
	t.is(headers.unicorn, 'rainbow');
	t.is(headers['content-encoding'], 'gzip');
});

{
	const nodejsMajorVersion = Number(process.versions.node.split('.')[0]);
	const testFunction = nodejsMajorVersion < 14 ? test.failing : test;

	testFunction('destroying got.stream() destroys the request - `request` event', withServer, async (t, server, got) => {
		server.get('/', defaultHandler);

		const stream = got.stream('');
		const request = await pEvent(stream, 'request') as ClientRequest;
		stream.destroy();
		t.truthy(request.destroyed);
	});

	testFunction('destroying got.stream() destroys the request - `response` event', withServer, async (t, server, got) => {
		server.get('/', (_request, response) => {
			response.write('hello');
		});

		const stream = got.stream('');
		const request = await pEvent(stream, 'request') as ClientRequest;
		await pEvent(stream, 'response');
		stream.destroy();
		t.truthy(request.destroyed);
	});
}

test('piping to got.stream.put()', withServer, async (t, server, got) => {
	server.get('/', defaultHandler);
	server.put('/post', postHandler);

	await t.notThrowsAsync(async () => {
		const stream = got.stream.put('post');

		await streamPipeline(
			got.stream(''),
			stream,
		);

		await getStream(stream);
	});
});

// See https://github.com/nodejs/node/issues/35237
// eslint-disable-next-line ava/no-skip-test
test.skip('no unhandled body stream errors', async t => {
	const body = new globalThis.FormData();
	body.set('upload', new File([fs.readFileSync('/bin/sh')], 'sh'));

	await t.throwsAsync(got.post(`https://offlinesite${Date.now()}.com`, {
		body,
	}), {
		code: 'ENOTFOUND',
	});
});

test('works with pipeline', async t => {
	const error = await t.throwsAsync<RequestError>(streamPipeline(
		new ReadableStream({
			read() {
				this.push(null);
			},
		}),
		got.stream.put('http://localhost:7777'),
	), {
		instanceOf: RequestError,
	});

	t.is(typeof error?.code, 'string');
});

test('errors have body', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.setHeader('set-cookie', 'foo=bar');
		response.end('yay');
	});

	const error = await t.throwsAsync<RequestError>(getStream(got.stream('', {
		strictContentLength: false,
		cookieJar: {
			async setCookie() {
				throw new Error('snap');
			},
			getCookieString: async () => '',
		},
	})));

	t.is(error?.message, 'snap');
	t.is(error?.response?.body, 'yay');
});

test('pipe can send modified headers', withServer, async (t, server, got) => {
	server.get('/foobar', (_request, response) => {
		response.setHeader('foo', 'bar');
		response.end();
	});

	server.get('/', (_request, response) => {
		got.stream('foobar').on('response', response => {
			response.headers.foo = 'boo';
		}).pipe(response);
	});

	const {headers} = await got('');
	t.is(headers.foo, 'boo');
});

test('the socket is alive on a successful pipeline', withServer, async (t, server, got) => {
	const payload = 'ok';

	server.get('/', (_request, response) => {
		response.end(payload);
	});

	const gotStream = got.stream('');
	t.is(gotStream.socket, undefined);

	const receiver = new stream.PassThrough();
	await streamPipeline(gotStream, receiver);

	t.is(await getStream(receiver), payload);
	t.truthy(gotStream.socket);
	t.false(gotStream.socket!.destroyed);
});

test('async iterator works', withServer, async (t, server, got) => {
	const payload = 'ok';

	server.get('/', (_request, response) => {
		response.end(payload);
	});

	const gotStream = got.stream('');
	const chunks = [];

	for await (const chunk of gotStream) {
		chunks.push(chunk);
	}

	t.is(Buffer.concat(chunks).toString(), payload);
});

test('destroys only once', async t => {
	const stream = got.stream('https://example.com');
	stream.destroy();
	stream.destroy(new Error('oh no'));

	let errored = false;

	stream.once('error', () => {
		errored = true;
	});

	await delay(1);

	t.false(errored);
});

test('does not accept unreadable stream as body', withServer, async (t, server, got) => {
	server.post('/', (_request, _response) => {});

	const body = new ReadableStream();
	body.push(null);
	body.resume();

	await pEvent(body, 'end');

	const request = got.post({body});

	await t.throwsAsync(request, {
		instanceOf: RequestError,
	});
});

test('accepts readable-stream as body', withServer, async (t, server, got) => {
	server.post('/', (request, response) => {
		request.pipe(response);
	});

	const body = new Readable2({
		read() {
			this.push('ok');
			this.push(null);
		},
	});

	const response = await got.post({
		// We need to cast body as any,
		// because @types/readable-stream has incorrect types
		// and causes a lot of errors.
		body: body as any,
	});

	t.is(response.body, 'ok');
});

test('prevents `Cannot call end` error', async t => {
	const stream = got.stream('https://example.com', {
		request: () => new Writable({
			final() {},
		}) as any,
		timeout: {
			request: 1,
		},
	});

	const error = await pEvent(stream, 'error') as RequestError;
	t.is(error.code, 'ETIMEDOUT');
});

if (Number.parseInt(process.versions.node.split('.')[0]!, 10) <= 12) {
	test('does not emit end event on error', withServer, async (t, server, got) => {
		server.get('/', infiniteHandler);

		await t.notThrowsAsync(new Promise((resolve, reject) => {
			got.stream({
				timeout: {
					request: 100,
				},
				hooks: {
					beforeError: [
						async error => {
							await new Promise(resolve => {
								setTimeout(resolve, 50);
							});

							return error;
						},
					],
				},
			}).once('end', () => {
				reject(new Error('Stream has ended before erroring'));
			}).once('error', resolve).resume();
		}));
	});
}

// Test only on Linux
const testFunction = process.platform === 'linux' ? test : test.skip;
testFunction('it sends a body of file with size on stat = 0', withServer, async (t, server, got) => {
	server.post('/', async (request, response) => {
		response.end(await getStream(request));
	});

	const response = await got.post({
		body: fs.createReadStream('/proc/cpuinfo'),
	});

	t.truthy(response.body);
});

test('OPTIONS stream without body completes successfully', withServer, async (t, server, got) => {
	server.options('/', (_request, response) => {
		response.writeHead(200, {
			allow: 'OPTIONS, GET, HEAD, POST',
		});
		response.end();
	});

	const stream = got.stream({method: 'OPTIONS'});
	stream.end();
	await t.notThrowsAsync(getStream(stream));
});

test('DELETE stream without body completes successfully', withServer, async (t, server, got) => {
	server.delete('/', (_request, response) => {
		response.writeHead(204);
		response.end();
	});

	const stream = got.stream({method: 'DELETE'});
	stream.end();
	await t.notThrowsAsync(getStream(stream));
});

test('PATCH stream without body completes successfully', withServer, async (t, server, got) => {
	server.patch('/', (_request, response) => {
		response.writeHead(200);
		response.end('patched');
	});

	const stream = got.stream({method: 'PATCH'});
	stream.end();
	const data = await getStream(stream);
	t.is(data, 'patched');
});

test('PATCH stream waits for piped body', withServer, async (t, server, got) => {
	server.patch('/', postHandler);

	const destination = new stream.PassThrough();
	const responsePromise = getStream(destination);

	await streamPipeline(
		ReadableStream.from(['Hello, world!']),
		got.stream.patch(''),
		destination,
	);

	t.is(await responsePromise, 'Hello, world!');
});

test('throws error when content-length does not match bytes transferred - stream', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.writeHead(200, {
			'content-length': '100',
		});
		response.write('ok'); // Only 2 bytes
		response.end();
	});

	await t.throwsAsync(
		getStream(got.stream('', {strictContentLength: true})),
		{
			instanceOf: RequestError,
			message: /Content-Length mismatch/,
		},
	);
});

test('throws error when content-length does not match bytes transferred - promise', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.writeHead(200, {
			'content-length': '100',
		});
		response.write('ok');
		response.end();
	});

	await t.throwsAsync(
		got('', {strictContentLength: true}),
		{
			instanceOf: RequestError,
			message: /Content-Length mismatch/,
		},
	);
});

test('does not throw when content-length matches bytes transferred', withServer, async (t, server, got) => {
	const payload = 'hello world';
	server.get('/', (_request, response) => {
		response.writeHead(200, {
			'content-length': String(Buffer.byteLength(payload)),
		});
		response.end(payload);
	});

	const body = await got('', {strictContentLength: true}).text();
	t.is(body, payload);
});

test('does not throw when content-length header is absent', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.writeHead(200);
		response.end('hello');
	});

	const body = await got('', {strictContentLength: true}).text();
	t.is(body, 'hello');
});

test('throws content-length mismatch error by default', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.writeHead(200, {
			'content-length': '100',
		});
		response.write('ok'); // Only 2 bytes
		response.end();
	});

	await t.throwsAsync(
		got('').text(),
		{
			instanceOf: RequestError,
			message: /Content-Length mismatch/,
		},
	);
});

test('validates content-length for gzip compressed responses', withServer, async (t, server, got) => {
	// Gzipped 'ok' - H4sIAAAAAAAA/8vPBgBH3dx5AgAAAA== base64 encoded
	const gzippedData = Buffer.from('H4sIAAAAAAAA/8vPBgBH3dx5AgAAAA==', 'base64');
	const incorrectLength = gzippedData.length + 10; // Intentionally wrong

	server.get('/', (_request, response) => {
		response.writeHead(200, {
			'content-encoding': 'gzip',
			'content-length': String(incorrectLength),
		});
		response.end(gzippedData);
	});

	await t.throwsAsync(
		got('', {strictContentLength: true}).text(),
		{
			instanceOf: RequestError,
			message: /Content-Length mismatch/,
		},
	);
});

test('handles empty gzip compressed responses with strictContentLength', withServer, async (t, server, got) => {
	// Empty gzip (10 byte header + 8 byte footer, no data)
	const emptyGzippedData = Buffer.from('H4sIAAAAAAAAAwMAAAAAAAAAAAA=', 'base64');

	server.get('/', (_request, response) => {
		response.writeHead(200, {
			'content-encoding': 'gzip',
			'content-length': String(emptyGzippedData.length),
		});
		response.end(emptyGzippedData);
	});

	const body = await got('', {strictContentLength: true}).text();
	t.is(body, '');
});

test('isReadonly is false for streams without body', withServer, async (t, server, got) => {
	server.post('/', postHandler);

	const stream = got.stream.post('');
	t.false(stream.isReadonly);

	stream.end('data');
	await getStream(stream);
});

test('isReadonly is true when body option is provided', withServer, async (t, server, got) => {
	server.post('/', postHandler);

	const stream = got.stream.post({body: 'test data'});
	t.true(stream.isReadonly);

	await t.notThrowsAsync(getStream(stream));
});

test('isReadonly is true when json option is provided', withServer, async (t, server, got) => {
	server.post('/', postHandler);

	const stream = got.stream.post({json: {foo: 'bar'}});
	t.true(stream.isReadonly);

	await t.notThrowsAsync(getStream(stream));
});

test('isReadonly is true when form option is provided', withServer, async (t, server, got) => {
	server.post('/', postHandler);

	const stream = got.stream.post({form: {foo: 'bar'}});
	t.true(stream.isReadonly);

	await t.notThrowsAsync(getStream(stream));
});
```

## File: `test/timeout.ts`
```typescript
import process from 'node:process';
import {EventEmitter} from 'node:events';
import stream from 'node:stream';
import {pipeline as streamPipeline} from 'node:stream/promises';
import http from 'node:http';
import https from 'node:https';
import net from 'node:net';
import getStream from 'get-stream';
import test from 'ava';
import delay from 'delay';
import type {Handler} from 'express';
import {pEvent} from 'p-event';
import got, {type RequestError, TimeoutError} from '../source/index.js';
import type {NativeRequestOptions} from '../source/core/options.js';
import timedOut from '../source/core/timed-out.js';
import slowDataStream from './helpers/slow-data-stream.js';
import type {GlobalClock} from './helpers/types.js';
import withServer, {withServerAndFakeTimers, withHttpsServer} from './helpers/with-server.js';

const requestDelay = 800;

const errorMatcher = {
	instanceOf: TimeoutError,
	code: 'ETIMEDOUT',
};

const keepAliveAgent = new http.Agent({
	keepAlive: true,
});

const defaultHandler = (clock: GlobalClock): Handler => (request, response) => {
	request.resume();
	request.on('end', () => {
		clock.tick(requestDelay);
		response.end('OK');
	});
};

const downloadHandler = (clock?: GlobalClock): Handler => (_request, response) => {
	response.writeHead(200, {
		'transfer-encoding': 'chunked',
	});
	response.flushHeaders();

	setImmediate(async () => {
		await streamPipeline(slowDataStream(clock), response);
	});
};

test.serial('timeout option', withServerAndFakeTimers, async (t, server, got, clock) => {
	server.get('/', defaultHandler(clock));

	await t.throwsAsync(
		got({
			timeout: {
				request: 1,
			},
			retry: {
				limit: 0,
			},
		}),
		{
			...errorMatcher,
			message: 'Timeout awaiting \'request\' for 1ms',
		},
	);
});

test.serial('timeout option as object', withServerAndFakeTimers, async (t, server, got, clock) => {
	server.get('/', defaultHandler(clock));

	await t.throwsAsync(
		got({
			timeout: {request: 1},
			retry: {
				limit: 0,
			},
		}),
		{
			...errorMatcher,
			message: 'Timeout awaiting \'request\' for 1ms',
		},
	);
});

test.serial('socket timeout', async t => {
	await t.throwsAsync(
		got('https://example.com', {
			timeout: {socket: 1},
			retry: {
				limit: 0,
			},
			https: {
				rejectUnauthorized: false,
			},
			request() {
				return https.request('https://example.com', {
					timeout: 0,
					rejectUnauthorized: false,
				});
			},
		}),
		{
			instanceOf: TimeoutError,
			code: 'ETIMEDOUT',
			message: 'Timeout awaiting \'socket\' for 1ms',
		},
	);
});

test.serial('send timeout', withServerAndFakeTimers, async (t, server, got, clock) => {
	server.post('/', defaultHandler(clock));

	await t.throwsAsync(
		got.post({
			timeout: {send: 1},
			body: new stream.PassThrough(),
			retry: {
				limit: 0,
			},
		}).on('request', request => {
			request.once('socket', socket => {
				socket.once('connect', () => {
					clock.tick(10);
				});
			});
		}),
		{
			...errorMatcher,
			message: 'Timeout awaiting \'send\' for 1ms',
		},
	);
});

test.serial('send timeout (keepalive)', withServerAndFakeTimers, async (t, server, got, clock) => {
	server.post('/', defaultHandler(clock));
	server.get('/prime', (_request, response) => {
		response.end('ok');
	});

	await got('prime', {agent: {http: keepAliveAgent}});

	await t.throwsAsync(
		got.post({
			agent: {
				http: keepAliveAgent,
			},
			timeout: {send: 1},
			retry: {
				limit: 0,
			},
			body: slowDataStream(clock),
		}).on('request', (request: http.ClientRequest) => {
			request.once('socket', socket => {
				t.false(socket.connecting);

				socket.once('connect', () => {
					t.fail('\'connect\' event fired, invalidating test');
				});
			});
		}),
		{
			...errorMatcher,
			message: 'Timeout awaiting \'send\' for 1ms',
		},
	);
});

test.serial('response timeout', withServerAndFakeTimers, async (t, server, got, clock) => {
	server.get('/', defaultHandler(clock));

	await t.throwsAsync(
		got({
			timeout: {response: 1},
			retry: {
				limit: 0,
			},
		}),
		{
			...errorMatcher,
			message: 'Timeout awaiting \'response\' for 1ms',
		},
	);
});

test.serial('response timeout unaffected by slow upload', withServerAndFakeTimers, async (t, server, got, clock) => {
	server.post('/', defaultHandler(clock));

	await t.notThrowsAsync(got.post({
		retry: {
			limit: 0,
		},
		body: slowDataStream(clock),
	}));
});

test.serial('response timeout unaffected by slow download', withServer, async (t, server, got) => {
	server.get('/', downloadHandler());

	await t.notThrowsAsync(got({
		timeout: {response: 200},
		retry: {
			limit: 0,
		},
	}));

	await delay(100);
});

test.serial('response timeout (keepalive)', withServerAndFakeTimers, async (t, server, got, clock) => {
	server.get('/', defaultHandler(clock));
	server.get('/prime', (_request, response) => {
		response.end('ok');
	});

	await got('prime', {agent: {http: keepAliveAgent}});

	const request = got({
		agent: {
			http: keepAliveAgent,
		},
		timeout: {response: 1},
		retry: {
			limit: 0,
		},
	}).on('request', (request: http.ClientRequest) => {
		request.once('socket', socket => {
			t.false(socket.connecting);
			socket.once('connect', () => {
				t.fail('\'connect\' event fired, invalidating test');
			});
		});
	});

	await t.throwsAsync(request, {
		...errorMatcher,
		message: 'Timeout awaiting \'response\' for 1ms',
	});
});

test.serial('connect timeout', withServerAndFakeTimers, async (t, _server, got, clock) => {
	await t.throwsAsync(
		got({
			createConnection(options: NativeRequestOptions) {
				const socket = new net.Socket(options as Record<string, unknown> as net.SocketConstructorOpts);
				// @ts-expect-error We know that it is readonly, but we have to test it
				socket.connecting = true;
				setImmediate(() => {
					socket.emit('lookup', null, '127.0.0.1', 4, 'localhost');
				});
				return socket;
			},
			timeout: {connect: 1},
			retry: {
				limit: 0,
			},
		}).on('request', (request: http.ClientRequest) => {
			request.on('socket', () => {
				clock.runAll();
			});
		}),
		{
			...errorMatcher,
			message: 'Timeout awaiting \'connect\' for 1ms',
		},
	);
});

test.serial('connect timeout (ip address)', withServerAndFakeTimers, async (t, _server, _got, clock) => {
	await t.throwsAsync(
		got('http://127.0.0.1', {
			createConnection(options: NativeRequestOptions) {
				const socket = new net.Socket(options as Record<string, unknown> as net.SocketConstructorOpts);
				// @ts-expect-error We know that it is readonly, but we have to test it
				socket.connecting = true;
				return socket;
			},
			timeout: {connect: 1},
			retry: {
				limit: 0,
			},
		}).on('request', (request: http.ClientRequest) => {
			request.on('socket', () => {
				clock.runAll();
			});
		}),
		{
			...errorMatcher,
			message: 'Timeout awaiting \'connect\' for 1ms',
		},
	);
});

test.serial('secureConnect timeout', withHttpsServer({}, true), async (t, _server, got, clock) => {
	await t.throwsAsync(
		got({
			createConnection(options: NativeRequestOptions) {
				const socket = new net.Socket(options as Record<string, unknown> as net.SocketConstructorOpts);
				// @ts-expect-error We know that it is readonly, but we have to test it
				socket.connecting = true;
				setImmediate(() => {
					socket.emit('lookup', null, '127.0.0.1', 4, 'localhost');

					setImmediate(() => {
						socket.emit('connect');
					});
				});
				return socket;
			},
			timeout: {secureConnect: 0},
			retry: {
				limit: 0,
			},
		}).on('request', (request: http.ClientRequest) => {
			request.on('socket', () => {
				clock.runAll();
			});
		}),
		{
			...errorMatcher,
			message: 'Timeout awaiting \'secureConnect\' for 0ms',
		},
	);
});

test('secureConnect timeout not breached', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	await t.notThrowsAsync(got({
		timeout: {secureConnect: 200},
		retry: {
			limit: 0,
		},
		https: {
			rejectUnauthorized: false,
		},
	}));
});

test.serial('lookup timeout', withServerAndFakeTimers, async (t, server, got, clock) => {
	server.get('/', defaultHandler(clock));

	await t.throwsAsync(
		got({
			dnsLookup() {},
			timeout: {lookup: 1},
			retry: {
				limit: 0,
			},
		}).on('request', (request: http.ClientRequest) => {
			request.on('socket', () => {
				clock.runAll();
			});
		}),
		{
			...errorMatcher,
			message: 'Timeout awaiting \'lookup\' for 1ms',
		},
	);
});

test.serial('lookup timeout no error (ip address)', withServerAndFakeTimers, async (t, server, _got, clock) => {
	server.get('/', defaultHandler(clock));

	await t.notThrowsAsync(got(`http://127.0.0.1:${server.port}`, {
		timeout: {lookup: 1},
		retry: {limit: 0},
	}));
});

test.serial('lookup timeout no error (keepalive)', withServerAndFakeTimers, async (t, server, got, clock) => {
	server.get('/', defaultHandler(clock));
	server.get('/prime', (_request, response) => {
		response.end('ok');
	});

	await got('prime', {agent: {http: keepAliveAgent}});
	await t.notThrowsAsync(got({
		agent: {http: keepAliveAgent},
		timeout: {lookup: 1},
		retry: {limit: 0},
	}).on('request', (request: http.ClientRequest) => {
		request.once('connect', () => {
			t.fail('connect event fired, invalidating test');
		});
	}));

	keepAliveAgent.destroy();
});

test.serial('retries on timeout', withServer, async (t, server, got) => {
	server.get('/', () => {});

	let hasTried = false;
	await t.throwsAsync(got({
		timeout: {
			request: 1,
		},
		retry: {
			calculateDelay() {
				if (hasTried) {
					return 0;
				}

				hasTried = true;
				return 1;
			},
		},
	}), {
		...errorMatcher,
		message: 'Timeout awaiting \'request\' for 1ms',
	});

	t.true(hasTried);
});

test.serial('timeout with streams', withServerAndFakeTimers, async (t, server, got, clock) => {
	server.get('/', defaultHandler(clock));

	const stream = got.stream({
		timeout: {request: 0},
		retry: {limit: 0},
	});
	await t.throwsAsync(pEvent(stream, 'response'), {code: 'ETIMEDOUT'});
});

test.serial('no error emitted when timeout is not breached (stream)', withServerAndFakeTimers, async (t, server, got, clock) => {
	server.get('/', defaultHandler(clock));

	const stream = got.stream({
		retry: {
			limit: 0,
		},
		timeout: {
			request: requestDelay * 2,
		},
	});

	await t.notThrowsAsync(getStream(stream));
});

test.serial('no error emitted when timeout is not breached (promise)', withServerAndFakeTimers, async (t, server, got, clock) => {
	server.get('/', defaultHandler(clock));

	await t.notThrowsAsync(got({
		retry: {
			limit: 0,
		},
		timeout: {
			request: requestDelay * 2,
		},
	}));
});

test.serial('no unhandled `socket hung up` errors', withServerAndFakeTimers, async (t, server, got, clock) => {
	server.get('/', defaultHandler(clock));

	await t.throwsAsync(
		got({
			retry: {
				limit: 0,
			},
			timeout: {
				request: requestDelay / 2,
			},
		}),
		{instanceOf: TimeoutError},
	);
});

test.serial('no unhandled timeout errors', withServerAndFakeTimers, async (t, _server, got, clock) => {
	await t.throwsAsync(got({
		retry: {limit: 0},
		timeout: {request: 100},
		request(...arguments_) {
			const result = http.request(...arguments_);

			result.once('socket', () => {
				result.socket?.destroy();
			});

			return result;
		},
	}), {message: 'socket hang up'});

	clock.tick(200);
});

test.serial('no unhandled timeout errors #2', withServerAndFakeTimers, async (t, server, got, clock) => {
	server.get('/', (_request, response) => {
		response.write('Hello world!');
	});

	const gotPromise = got('', {
		timeout: {
			request: 20,
		},
		retry: {
			calculateDelay({computedValue}) {
				if (computedValue) {
					return 10;
				}

				return 0;
			},
			limit: 1,
		},
	});

	await t.throwsAsync(gotPromise, {instanceOf: TimeoutError});

	clock.tick(100);
});

test.serial('no more timeouts after an error', withServer, async (t, _server, got) => {
	const {setTimeout} = globalThis;
	const {clearTimeout} = globalThis;

	// @ts-expect-error FIXME
	globalThis.setTimeout = (callback, _ms, ...arguments_) => {
		const timeout = {
			isCleared: false,
		};

		process.nextTick(() => {
			if (timeout.isCleared) {
				return;
			}

			callback(...arguments_);
		});

		return timeout;
	};

	globalThis.clearTimeout = timeout => {
		if (timeout) {
			// @ts-expect-error FIXME
			timeout.isCleared = true;
		}
	};

	try {
		await t.throwsAsync(got(`http://${Date.now()}.dev`, {
			retry: {limit: 1},
			timeout: {
				lookup: 1,
				connect: 1,
				secureConnect: 1,
				socket: 1,
				response: 1,
				send: 1,
				request: 1,
			},
		}), {instanceOf: TimeoutError});

		await delay(100);
	} finally {
		globalThis.setTimeout = setTimeout;
		globalThis.clearTimeout = clearTimeout;
	}
});

test.serial('socket timeout is canceled on error', withServerAndFakeTimers, async (t, _server, got, clock) => {
	const message = 'oh, snap!';

	const promise = got({
		timeout: {socket: 50},
		retry: {limit: 0},
	}).on('request', (request: http.ClientRequest) => {
		request.destroy(new Error(message));
	});

	await t.throwsAsync(promise, {message});

	// Wait a bit more to check if there are any unhandled errors
	clock.tick(100);
});

test.serial('no memory leak when using socket timeout and keepalive agent', withServerAndFakeTimers, async (t, server, got, clock) => {
	server.get('/', defaultHandler(clock));

	let request: any;

	await got({
		agent: {http: keepAliveAgent},
		timeout: {socket: requestDelay * 2},
	}).on('request', _request => {
		request = _request;
	});

	t.is(request.timeoutCb, null);

	keepAliveAgent.destroy();
});

test('ensure there are no new timeouts after cancelation', t => {
	const emitter = new EventEmitter();
	const socket = new EventEmitter();
	(socket as any).connecting = true;

	timedOut(emitter as http.ClientRequest, {
		connect: 1,
	}, {
		hostname: '127.0.0.1',
	})();

	emitter.emit('socket', socket);
	socket.emit('lookup', null);
	t.is(socket.listenerCount('connect'), 0);
});

test('double calling timedOut has no effect', t => {
	const emitter = new EventEmitter();

	const attach = (): () => void => timedOut(emitter as http.ClientRequest, {
		connect: 1,
	}, {
		hostname: '127.0.0.1',
	});

	attach();
	attach();

	t.is(emitter.listenerCount('socket'), 1);
});

// Regression test for issue #857: Fast DNS lookups (e.g., from cache) that complete synchronously
// used to incorrectly trigger lookup timeouts because Got couldn't attach the 'lookup' event listener
// in time. The fix in commit 4faf5c7 checks if the lookup has already completed (socket.address() is
// defined) before setting a lookup timeout, preventing false timeout errors on cached/fast lookups.
test.serial('doesn\'t throw on early lookup', withServerAndFakeTimers, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	await t.notThrowsAsync(got('', {
		timeout: {
			lookup: 1,
		},
		retry: {limit: 0},
		dnsLookup(_hostname, options, callback) {
			if (typeof options === 'function') {
				callback = options;
				// Call with default (non-all) signature
				callback(null, '127.0.0.1', 4);
			} else if (options.all) {
				// When options.all is true, callback expects an array of address objects
				callback(null, [{address: '127.0.0.1', family: 4}]);
			} else {
				callback(null, '127.0.0.1', 4);
			}
		},
	}));
});

test.serial('no unhandled `Premature close` error', withServerAndFakeTimers, async (t, server, got, clock) => {
	server.get('/', async (_request, response) => {
		response.write('hello');
	});

	await t.throwsAsync(got({
		timeout: {request: 10},
		retry: {limit: 0},
	}), {message: 'Timeout awaiting \'request\' for 10ms'});

	clock.tick(20);
});

test.serial('`read` timeout - promise', withServerAndFakeTimers, async (t, server, got, clock) => {
	server.get('/', (_request, response) => {
		response.write('o');
	});

	const gotPromise = got({
		timeout: {
			read: 10,
		},
		retry: {
			limit: 0,
		},
	});

	clock.tick(20);
	await t.throwsAsync(gotPromise, {message: 'Timeout awaiting \'read\' for 10ms'});
});

test.serial('`read` timeout - stream', withServerAndFakeTimers, async (t, server, got, clock) => {
	t.timeout(100);

	server.get('/', (_request, response) => {
		response.end('ok');
	});

	const stream = got.stream({
		timeout: {
			read: 10,
		},
	});

	clock.tick(20);
	await t.throwsAsync(pEvent(stream, 'end'), {message: 'Timeout awaiting \'read\' for 10ms'});
});

test.serial('cancelling the request removes timeouts', withServerAndFakeTimers, async (t, server, got, clock) => {
	server.get('/', (_request, response) => {
		response.write('hello');
	});

	const controller = new AbortController();

	const promise = got({
		signal: controller.signal,
		timeout: {
			request: 500,
		},
		retry: {
			limit: 0,
		},
	}).on('downloadProgress', () => {
		controller.abort();
	}).on('request', request => {
		request.on('error', error => {
			if (error.message === 'Timeout awaiting \'request\' for 500ms') {
				t.fail(error.message);
			}
		});
	});

	await t.throwsAsync(promise, {message: 'This operation was aborted.'});

	clock.tick(1000);
});

test.serial('timeouts are emitted ASAP', withServer, async (t, server, got) => {
	server.get('/test', () => {
		// Never respond - forces a timeout
	});

	const timeout = 500;
	const marginOfError = process.env.CI ? 200 : 100;
	const startTime = Date.now();

	const error = await t.throwsAsync<TimeoutError>(got('test', {
		retry: {
			limit: 0,
		},
		timeout: {
			request: timeout,
		},
	}), {instanceOf: TimeoutError});

	const elapsed = Date.now() - startTime;
	t.true(elapsed < (timeout + marginOfError), `Expected timeout ${elapsed}ms to be less than ${timeout + marginOfError}ms`);
	t.true(error.timings.phases.total! < (timeout + marginOfError));
});

test('http2 timeout', async t => {
	const error = await t.throwsAsync<RequestError>(got('https://123.123.123.123', {
		timeout: {
			request: 1,
		},
		http2: true,
		retry: {
			calculateDelay: ({computedValue}) => computedValue ? 1 : 0,
		},
	}));

	t.true(error?.code === 'ETIMEDOUT' || error?.code === 'EUNSUPPORTED', error?.stack);
});

// Reproduces the memory leak reported in https://github.com/sindresorhus/got/issues/2351
test.serial('no memory leak when using http2 with socket timeout and connection reuse', withHttpsServer(), async (t, server, got) => {
	const {default: http2wrapper} = await import('http2-wrapper');
	const customAgent = new http2wrapper.Agent();

	server.get('/:id', (_request, response) => {
		response.end('ok');
	});

	const requestCount = 15; // Make concurrent requests to accumulate listeners
	let sharedSocket: any;
	let maxListenerCount = 0;

	// Make requests that overlap in time to reproduce the listener accumulation
	server.get('/slow/:id', async (_request, response) => {
		// Slow response to keep requests active simultaneously
		await delay(200);
		response.end('ok');
	});

	// Start many concurrent requests with the same agent to reuse the connection
	const promises = [];
	const handleRequest = (request: any) => {
		// Track socket and check listener count DURING requests
		request.once('socket', (socket: any) => {
			sharedSocket ??= socket;

			// Check how many listeners are on the socket while requests are active
			const currentCount = socket.listenerCount('timeout');
			if (currentCount > maxListenerCount) {
				maxListenerCount = currentCount;
			}
		});
	};

	for (let i = 0; i < requestCount; i++) {
		const promise = got(`slow/${i}`, {
			http2: true,
			agent: {http2: customAgent},
			timeout: {socket: 30_000},
			https: {rejectUnauthorized: false},
		}).on('request', handleRequest);
		promises.push(promise);
	}

	// Wait for all concurrent requests to finish
	await Promise.all(promises);

	// The bug: setTimeout(0) doesn't remove timeout listeners, so with HTTP/2
	// connection reuse and concurrent requests, listeners accumulate on the shared socket
	// The fix: removeAllListeners('timeout') properly cleans up

	t.truthy(sharedSocket, 'Should have a socket');

	// With the bug (setTimeout(0)), maxListenerCount would be >> 1 (grows with concurrent requests)
	// With the fix (removeAllListeners), maxListenerCount should be 0 or 1
	t.true(maxListenerCount <= 1, `Socket peaked at ${maxListenerCount} timeout listeners (expected ≤ 1)`);

	customAgent.destroy();
});
```

## File: `test/timer-utils.ts`
```typescript
import {EventEmitter} from 'node:events';
import test from 'ava';
import timer from '../source/core/utils/timer.js';

// Helper for delays
const delay = async (ms: number) => new Promise(resolve => {
	setTimeout(resolve, ms);
});

// Helper to create a mock request
function createMockRequest() {
	const request = new EventEmitter() as any;
	request.prependOnceListener = request.once.bind(request);
	request.off = request.removeListener.bind(request);
	request.writableFinished = false;
	return request;
}

// Helper to create a mock socket
function createMockSocket(options: {connecting?: boolean; writable?: boolean; destroyed?: boolean} = {}) {
	const socket = new EventEmitter() as any;
	socket.prependOnceListener = socket.once.bind(socket);
	socket.connecting = options.connecting ?? false;
	socket.writable = options.writable ?? true;
	socket.destroyed = options.destroyed ?? false;
	socket.removeListener = socket.off.bind(socket);
	return socket;
}

// Helper to create a mock response
function createMockResponse() {
	const response = new EventEmitter() as any;
	response.prependOnceListener = response.once.bind(response);
	response.off = response.removeListener.bind(response);
	return response;
}

test('timer returns same object on subsequent calls (singleton)', t => {
	const request = createMockRequest();
	const timings1 = timer(request);
	const timings2 = timer(request);

	t.is(timings1, timings2, 'should return the same timings object');
});

test('timer initializes all properties to undefined except start', t => {
	const request = createMockRequest();
	const timings = timer(request);

	t.is(typeof timings.start, 'number');
	t.is(timings.socket, undefined);
	t.is(timings.lookup, undefined);
	t.is(timings.connect, undefined);
	t.is(timings.secureConnect, undefined);
	t.is(timings.upload, undefined);
	t.is(timings.response, undefined);
	t.is(timings.end, undefined);
	t.is(timings.error, undefined);
	t.is(timings.abort, undefined);

	t.is(timings.phases.wait, undefined);
	t.is(timings.phases.dns, undefined);
	t.is(timings.phases.tcp, undefined);
	t.is(timings.phases.tls, undefined);
	t.is(timings.phases.request, undefined);
	t.is(timings.phases.firstByte, undefined);
	t.is(timings.phases.download, undefined);
	t.is(timings.phases.total, undefined);
});

test('timer sets socket timing when socket event fires', t => {
	const request = createMockRequest();
	const timings = timer(request);
	const socket = createMockSocket({connecting: true});

	request.emit('socket', socket);

	t.is(typeof timings.socket, 'number');
	t.is(typeof timings.phases.wait, 'number');
	t.true(timings.phases.wait! >= 0);
});

test('timer handles already attached socket', t => {
	const request = createMockRequest();
	const socket = createMockSocket({connecting: true});
	request.socket = socket;

	const timings = timer(request);

	t.is(typeof timings.socket, 'number');
	t.is(typeof timings.phases.wait, 'number');
});

test('timer measures DNS lookup timing', async t => {
	const request = createMockRequest();
	const timings = timer(request);
	const socket = createMockSocket({connecting: true});

	request.emit('socket', socket);
	await delay(10);
	socket.emit('lookup');
	await delay(5);
	socket.emit('connect');

	t.is(typeof timings.lookup, 'number');
	t.is(typeof timings.phases.dns, 'number');
	t.true(timings.phases.dns! > 0);
	t.is(timings.phases.dns, timings.lookup! - timings.socket!);
});

test('timer handles IP address connection (no DNS lookup)', t => {
	const request = createMockRequest();
	const timings = timer(request);
	const socket = createMockSocket({connecting: true});

	request.emit('socket', socket);
	// Emit connect without lookup (simulates IP address connection)
	socket.emit('connect');

	t.is(timings.lookup, timings.socket);
	t.is(timings.phases.dns, 0);
	t.is(typeof timings.connect, 'number');
});

test('timer measures TCP connection timing', async t => {
	const request = createMockRequest();
	const timings = timer(request);
	const socket = createMockSocket({connecting: true});

	request.emit('socket', socket);
	socket.emit('lookup');
	await delay(10);
	socket.emit('connect');

	t.is(typeof timings.connect, 'number');
	t.is(typeof timings.phases.tcp, 'number');
	t.true(timings.phases.tcp! >= 0);
	t.is(timings.phases.tcp, timings.connect! - timings.lookup!);
});

test('timer measures TLS handshake timing', async t => {
	const request = createMockRequest();
	const timings = timer(request);
	const socket = createMockSocket({connecting: true});
	socket.encrypted = true; // Mark as TLS socket
	socket.authorized = false;

	request.emit('socket', socket);
	socket.emit('lookup');
	socket.emit('connect');
	await delay(10);
	socket.emit('secureConnect');

	t.is(typeof timings.secureConnect, 'number');
	t.is(typeof timings.phases.tls, 'number');
	t.true(timings.phases.tls! > 0);
	t.is(timings.phases.tls, timings.secureConnect! - timings.connect!);
});

test('timer handles socket reuse with stored timings', t => {
	const request = createMockRequest();
	const timings = timer(request);
	const socket = createMockSocket({writable: true, connecting: false});

	// Simulate stored timings from previous request
	socket.__initial_connection_timings__ = {
		dnsPhase: 5,
		tcpPhase: 10,
		tlsPhase: 15,
	};

	request.emit('socket', socket);

	// Verify phases are restored from initial connection
	t.is(timings.phases.dns, 5);
	t.is(timings.phases.tcp, 10);
	t.is(timings.phases.tls, 15);

	// Verify all timestamps are at socket time (no new connection for THIS request)
	t.is(timings.lookup, timings.socket);
	t.is(timings.connect, timings.socket);
	t.is(timings.secureConnect, timings.socket);
});

test('timer handles socket reuse without TLS', t => {
	const request = createMockRequest();
	const timings = timer(request);
	const socket = createMockSocket({writable: true, connecting: false});

	socket.__initial_connection_timings__ = {
		dnsPhase: 3,
		tcpPhase: 7,
	};

	request.emit('socket', socket);

	t.is(timings.phases.dns, 3);
	t.is(timings.phases.tcp, 7);
	t.is(timings.phases.tls, undefined);
	t.is(timings.secureConnect, undefined);
});

test('timer handles socket reuse without stored timings', t => {
	const request = createMockRequest();
	const timings = timer(request);
	const socket = createMockSocket({writable: true, connecting: false});

	// No __initial_connection_timings__ stored
	request.emit('socket', socket);

	// Should set phases to 0 and timestamps to socket time
	t.is(timings.lookup, timings.socket);
	t.is(timings.connect, timings.socket);
	t.is(timings.phases.dns, 0);
	t.is(timings.phases.tcp, 0);
});

// Note: HTTP/2 proxy socket behavior is tested in integration tests (test/timings.ts)

test('timer stores connection timings on socket for reuse', async t => {
	const request = createMockRequest();
	timer(request);
	const socket = createMockSocket({connecting: true});

	request.emit('socket', socket);
	socket.emit('lookup');
	await delay(5);
	socket.emit('connect');

	// Verify timings are stored on socket
	t.truthy(socket.__initial_connection_timings__);
	t.is(typeof socket.__initial_connection_timings__.dnsPhase, 'number');
	t.is(typeof socket.__initial_connection_timings__.tcpPhase, 'number');
	t.true(socket.__initial_connection_timings__.dnsPhase >= 0);
	t.true(socket.__initial_connection_timings__.tcpPhase >= 0);
});

test('timer measures upload timing', async t => {
	const request = createMockRequest();
	const timings = timer(request);
	const socket = createMockSocket({connecting: true});

	request.emit('socket', socket);
	socket.emit('connect');
	await delay(10);
	request.emit('finish');

	t.is(typeof timings.upload, 'number');
	t.true(timings.upload! >= timings.connect!);
});

test('timer handles already finished write', t => {
	const request = createMockRequest();
	request.writableFinished = true;
	const timings = timer(request);
	const socket = createMockSocket({connecting: true});

	request.emit('socket', socket);
	socket.emit('connect');

	t.is(typeof timings.upload, 'number');
});

test('timer measures response timing', async t => {
	const request = createMockRequest();
	const timings = timer(request);
	const socket = createMockSocket({connecting: true});
	const response = createMockResponse();

	request.emit('socket', socket);
	socket.emit('connect');
	request.emit('finish');
	await delay(10);
	request.emit('response', response);

	t.is(typeof timings.response, 'number');
	t.is(typeof timings.phases.firstByte, 'number');
	t.true(timings.phases.firstByte! >= 0);
	t.is(timings.phases.firstByte, timings.response! - timings.upload!);
});

test('timer measures download timing', async t => {
	const request = createMockRequest();
	const timings = timer(request);
	const socket = createMockSocket({connecting: true});
	const response = createMockResponse();

	request.emit('socket', socket);
	socket.emit('connect');
	request.emit('finish');
	request.emit('response', response);
	await delay(10);
	response.emit('end');

	t.is(typeof timings.end, 'number');
	t.is(typeof timings.phases.download, 'number');
	t.is(typeof timings.phases.total, 'number');
	t.true(timings.phases.download! >= 0);
	t.true(timings.phases.total! > 0);
	t.is(timings.phases.download, timings.end! - timings.response!);
	t.is(timings.phases.total, timings.end! - timings.start);
});

test('timer captures error timing', t => {
	const request = createMockRequest();
	const timings = timer(request);

	// Add error handler to prevent unhandled error
	request.on('error', () => {});

	const error = new Error('Test error');
	request.emit('error', error);

	t.is(typeof timings.error, 'number');
	t.is(typeof timings.phases.total, 'number');
	t.is(timings.phases.total, timings.error! - timings.start);
});

test('timer captures abort timing', t => {
	const request = createMockRequest();
	const timings = timer(request);

	request.emit('abort');

	t.is(typeof timings.abort, 'number');
	t.is(typeof timings.phases.total, 'number');
	t.is(timings.phases.total, timings.abort! - timings.start);
});

test('timer handles response abort', t => {
	const request = createMockRequest();
	const timings = timer(request);
	const socket = createMockSocket({connecting: true});
	const response = createMockResponse();

	request.emit('socket', socket);
	socket.emit('connect');
	request.emit('finish');
	request.emit('response', response);
	response.emit('aborted');

	t.is(typeof timings.abort, 'number');
	t.is(typeof timings.phases.total, 'number');
});

test('timer does not overwrite total phase on normal completion', t => {
	const request = createMockRequest();
	const timings = timer(request);
	const socket = createMockSocket({connecting: true});
	const response = createMockResponse();

	request.emit('socket', socket);
	socket.emit('connect');
	request.emit('finish');
	request.emit('response', response);

	// Simulate abort before end
	response.emit('aborted');
	const abortTotal = timings.phases.total;

	// Now emit end - should not overwrite the abort total
	response.emit('end');

	t.is(timings.phases.total, abortTotal, 'should preserve abort total');
});

test('timer calculates request phase correctly', async t => {
	const request = createMockRequest();
	const timings = timer(request);
	const socket = createMockSocket({connecting: true});

	request.emit('socket', socket);
	socket.emit('connect');
	await delay(10);
	request.emit('finish');

	t.is(typeof timings.phases.request, 'number');
	t.true(timings.phases.request! >= 0);
	t.is(timings.phases.request, timings.upload! - timings.connect!);
});

test('timer calculates request phase with TLS', async t => {
	const request = createMockRequest();
	const timings = timer(request);
	const socket = createMockSocket({connecting: true});
	socket.encrypted = true;
	socket.authorized = false;

	request.emit('socket', socket);
	socket.emit('connect');
	socket.emit('secureConnect');
	await delay(10);
	request.emit('finish');

	t.is(typeof timings.phases.request, 'number');
	t.true(timings.phases.request! >= 0);
	t.is(timings.phases.request, timings.upload! - timings.secureConnect!);
});

// HTTP/2 request phase test is not included here because it requires mocking util.types.isProxy
// which is difficult in ESM. This behavior is tested in integration tests with actual HTTP/2 requests.
```

## File: `test/timings.ts`
```typescript
import http from 'node:http';
import {promises as dnsPromises} from 'node:dns';
import test from 'ava';
import CacheableLookup from 'cacheable-lookup';
import got from '../source/index.js';
import withServer from './helpers/with-server.js';

test('http/1 timings', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	const {timings} = await got('');

	t.true(timings.start >= 0);
	t.true(timings.socket! >= 0);
	t.true(timings.lookup! >= 0);
	t.true(timings.connect! >= 0);
	t.true(timings.upload! >= 0);
	t.true(timings.response! >= 0);
	t.true(timings.end! >= 0);

	const {phases} = timings;

	t.true(phases.wait! >= 0);
	t.true(phases.dns! >= 0);
	t.true(phases.tcp! >= 0);
	t.true(phases.request! >= 0);
	t.true(phases.firstByte! >= 0);
	t.true(phases.download! >= 0);
	t.true(phases.total! >= 0);
});

test('http/2 timings', async t => {
	// Use a real HTTP/2 server (Google supports HTTP/2)
	const {timings} = await got('https://www.google.com/', {
		http2: true,
		https: {
			rejectUnauthorized: false,
		},
	});

	// These timings are available even for HTTP/2
	t.true(timings.start >= 0);
	t.true(timings.socket! >= 0);
	t.true(timings.upload! >= 0);
	t.true(timings.response! >= 0);
	t.true(timings.end! >= 0);

	// These connection timings are unavailable for HTTP/2 (socket is a proxy)
	// See https://github.com/sindresorhus/got/issues/1958
	t.is(timings.lookup, undefined);
	t.is(timings.connect, undefined);
	t.is(timings.secureConnect, undefined);

	const {phases} = timings;

	// Available phases
	t.true(phases.wait! >= 0);
	t.true(phases.firstByte! >= 0);
	t.true(phases.download! >= 0);
	t.true(phases.total! >= 0);

	// Unavailable phases (due to missing connection timings)
	t.is(phases.dns, undefined);
	t.is(phases.tcp, undefined);
	t.is(phases.tls, undefined);
	// Most importantly: phases.request should be undefined, NOT NaN
	t.is(phases.request, undefined);
	t.false(Number.isNaN(phases.request));
});

test('timings.end is set when stream is destroyed before completion', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.write('chunk1');
		// Don't end the response, so it stays open
	});

	await new Promise<void>((resolve, reject) => {
		const stream = got.stream('');

		stream.on('data', () => {
			stream.destroy(new Error('Manual destroy'));
		});

		stream.on('error', (error: Error) => {
			t.is(error.message, 'Manual destroy');
			t.truthy(stream.timings);
			t.truthy(stream.timings!.response);
			t.truthy(stream.timings!.end);
			t.true(stream.timings!.end! >= stream.timings!.response!);
			t.truthy(stream.timings!.phases.total);
			resolve();
		});

		stream.on('end', () => {
			reject(new Error('Stream should not end normally'));
		});
	});

	t.pass();
});

test('dns timing is 0 for IP addresses', withServer, async (t, server) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	// Get the actual IP address the server is bound to
	const address = server.http.address() as {address: string; family: string; port: number};
	const host = address.family === 'IPv6' ? `[${address.address}]` : address.address;
	const {timings} = await got(`http://${host}:${server.port}/`);

	// When connecting to an IP address, there is no DNS lookup
	t.is(timings.phases.dns, 0);
	// Lookup timestamp should equal socket timestamp (no time elapsed for DNS)
	t.is(timings.lookup, timings.socket);
});

test('dns timing is 0 for cached DNS lookups', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	let resolve4CallCount = 0;
	let resolve6CallCount = 0;
	const serverAddress = server.http.address() as {family: string};
	const isIpv6Server = serverAddress.family === 'IPv6';

	const resolver = new dnsPromises.Resolver();
	resolver.resolve4 = (async (_hostname: string, _options: unknown) => {
		resolve4CallCount++;
		if (isIpv6Server) {
			return [];
		}

		return [{address: '127.0.0.1', ttl: 60}];
	}) as typeof resolver.resolve4;
	resolver.resolve6 = (async (_hostname: string, _options: unknown) => {
		resolve6CallCount++;
		if (isIpv6Server) {
			return [{address: '::1', ttl: 60}];
		}

		return [];
	}) as typeof resolver.resolve6;

	// Enable DNS cache and disable keep-alive to get new connections
	const instance = got.extend({
		dnsCache: new CacheableLookup({resolver}),
		agent: {
			http: new http.Agent({
				keepAlive: false,
			}),
		},
	});

	// First request: real DNS lookup
	const response1 = await instance('');
	const firstDns = response1.timings.phases.dns;

	// First request should have some DNS time (for localhost lookup)
	// or 0 if it's fast enough to trigger the cache threshold
	t.true(firstDns! >= 0);

	// Subsequent requests: DNS should be cached
	const response2 = await instance('');
	const response3 = await instance('');

	t.is(resolve4CallCount, 1);
	t.is(resolve6CallCount, 1);

	// When DNS is cached, if lookup and connect happen at the exact same time (tcp=0),
	// then dns is set to 0 to indicate no actual DNS resolution occurred.
	// Otherwise, dns will be small but may vary on CI due to system load.
	// The key fix from http-timer #35 is that we handle this case, not enforce exact values.
	const secondIsInstant = response2.timings.phases.tcp === 0;
	const thirdIsInstant = response3.timings.phases.tcp === 0;

	if (secondIsInstant) {
		t.is(response2.timings.phases.dns, 0, 'instant cached DNS (tcp=0) should have dns=0');
	} else {
		t.true(response2.timings.phases.dns! >= 0, 'cached DNS should have dns >= 0');
	}

	if (thirdIsInstant) {
		t.is(response3.timings.phases.dns, 0, 'instant cached DNS (tcp=0) should have dns=0');
	} else {
		t.true(response3.timings.phases.dns! >= 0, 'cached DNS should have dns >= 0');
	}
});

test('redirect timings preserve connection timings from initial request', withServer, async (t, server, got) => {
	// Set up a redirect chain to test socket reuse scenario
	server.get('/', (_request, response) => {
		response.writeHead(302, {
			location: '/redirect1',
		});
		response.end();
	});

	server.get('/redirect1', (_request, response) => {
		response.writeHead(302, {
			location: '/final',
		});
		response.end();
	});

	server.get('/final', (_request, response) => {
		response.end('final content');
	});

	const response = await got('');
	const {timings} = response;

	// Verify the response went through redirects
	t.is(response.redirectUrls.length, 2);
	t.is(response.body, 'final content');

	// The bug (#2425) was that on redirects with socket reuse, all timestamps
	// were set to socket time, causing all phases to be 0.

	// After the fix, for reused sockets:
	// - Timestamps are still all at socket time (correct for reused sockets)
	// - But phases preserve the original connection durations (not 0)

	// Verify timestamps are at socket time for reused socket
	t.is(timings.lookup, timings.socket);
	t.is(timings.connect, timings.socket);

	// Verify phases are preserved (not all 0)
	// For localhost, dns is 0 (IP address), but tcp should have some value
	t.is(typeof timings.phases.dns, 'number');
	t.is(typeof timings.phases.tcp, 'number');
	t.true(timings.phases.dns! >= 0);
	t.true(timings.phases.tcp! >= 0);

	// Verify basic timing chronology
	t.true(response.timings.start <= response.timings.socket!);
	t.true(response.timings.socket! <= response.timings.response!);
	t.true(response.timings.response! <= response.timings.end!);
});
```

## File: `test/unix-socket.ts`
```typescript
import process from 'node:process';
import {format} from 'node:util';
import test from 'ava';
import type {Handler} from 'express';
import baseGot from '../source/index.js';
import {withSocketServer} from './helpers/with-server.js';

const got = baseGot.extend({enableUnixSockets: true});

const okHandler: Handler = (_request, response) => {
	response.end('ok');
};

const redirectHandler: Handler = (_request, response) => {
	response.writeHead(302, {
		location: 'foo',
	});
	response.end();
};

if (process.platform !== 'win32') {
	test('works', withSocketServer, async (t, server) => {
		server.on('/', okHandler);

		const url = format('http://unix:%s:%s', server.socketPath, '/');
		t.is((await got(url, {})).body, 'ok');
	});

	test('protocol-less works', withSocketServer, async (t, server) => {
		server.on('/', okHandler);

		const url = format('unix:%s:%s', server.socketPath, '/');
		t.is((await got(url)).body, 'ok');
	});

	test('address with : works', withSocketServer, async (t, server) => {
		server.on('/foo:bar', okHandler);

		const url = format('unix:%s:%s', server.socketPath, '/foo:bar');
		t.is((await got(url)).body, 'ok');
	});

	test('throws on invalid URL', async t => {
		try {
			await got('unix:', {retry: {limit: 0}});
		} catch (error: any) {
			t.regex(error.code, /ENOTFOUND|EAI_AGAIN/);
		}
	});

	test('works when extending instances', withSocketServer, async (t, server) => {
		server.on('/', okHandler);

		const url = format('unix:%s:%s', server.socketPath, '/');
		const instance = got.extend({prefixUrl: url});
		t.is((await instance('')).body, 'ok');
	});

	test('passes search params', withSocketServer, async (t, server) => {
		server.on('/?a=1', okHandler);

		const url = format('http://unix:%s:%s', server.socketPath, '/?a=1');
		t.is((await got(url)).body, 'ok');
	});

	test('redirects work', withSocketServer, async (t, server) => {
		server.on('/', redirectHandler);
		server.on('/foo', okHandler);

		const url = format('http://unix:%s:%s', server.socketPath, '/');
		t.is((await got(url)).body, 'ok');
	});

	test('`unix:` fails when UNIX sockets are not enabled', async t => {
		const gotUnixSocketsDisabled = got.extend({enableUnixSockets: false});

		t.false(gotUnixSocketsDisabled.defaults.options.enableUnixSockets);
		await t.throwsAsync(
			gotUnixSocketsDisabled('unix:'),
			{
				message: 'Using UNIX domain sockets but option `enableUnixSockets` is not enabled',
			},
		);
	});

	test('`http://unix:/` fails when UNIX sockets are not enabled', async t => {
		const gotUnixSocketsDisabled = got.extend({enableUnixSockets: false});

		t.false(gotUnixSocketsDisabled.defaults.options.enableUnixSockets);

		await t.throwsAsync(
			gotUnixSocketsDisabled('http://unix:'),
			{
				message: 'Using UNIX domain sockets but option `enableUnixSockets` is not enabled',
			},
		);
	});
}
```

## File: `test/weakable-map.ts`
```typescript
import test from 'ava';
import WeakableMap from '../source/core/utils/weakable-map.js';

test('works as expected', t => {
	const weakable = new WeakableMap();

	weakable.set('hello', 'world');

	t.true(weakable.has('hello'));
	t.false(weakable.has('foobar'));
	t.is(weakable.get('hello'), 'world');
	t.is(weakable.get('foobar'), undefined);

	const object = {};
	const anotherObject = {};
	weakable.set(object, 'world');

	t.true(weakable.has(object));
	t.false(weakable.has(anotherObject));
	t.is(weakable.get(object), 'world');
	t.is(weakable.get(anotherObject), undefined);
});
```

## File: `test/zstd.ts`
```typescript
import {Buffer} from 'node:buffer';
import {promisify} from 'node:util';
import zlib from 'node:zlib';
import test from 'ava';
import getStream from 'get-stream';
import {type HTTPError} from '../source/index.js';
import withServer from './helpers/with-server.js';

const supportsZstd = typeof zlib.zstdCompress === 'function';

if (supportsZstd) {
	const testContent = 'Compressible response content.\n';

	let zstdData: Uint8Array;
	test.before('setup', async () => {
		zstdData = await promisify<string, Uint8Array>(zlib.zstdCompress)(testContent);
	});

	test('decompress content', withServer, async (t, server, got) => {
		server.get('/', (_request, response) => {
			response.setHeader('Content-Encoding', 'zstd');
			response.end(zstdData);
		});

		t.is((await got('')).body, testContent);
	});

	test('decompress content on error', withServer, async (t, server, got) => {
		server.get('/', (_request, response) => {
			response.setHeader('Content-Encoding', 'zstd');
			response.status(404);
			response.end(zstdData);
		});

		const error = await t.throwsAsync<HTTPError>(got(''));

		t.is(error?.response.body, testContent);
	});

	test('decompress content - stream', withServer, async (t, server, got) => {
		server.get('/', (_request, response) => {
			response.setHeader('Content-Encoding', 'zstd');
			response.end(zstdData);
		});

		t.is((await getStream(got.stream(''))), testContent);
	});

	test('handles zstd error', withServer, async (t, server, got) => {
		server.get('/', (_request, response) => {
			response.setHeader('Content-Encoding', 'zstd');
			response.end('Not zstd content');
		});

		await t.throwsAsync(got(''), {
			name: 'ReadError',
		});
	});

	test('handles zstd error - stream', withServer, async (t, server, got) => {
		server.get('/', (_request, response) => {
			response.setHeader('Content-Encoding', 'zstd');
			response.end('Not zstd content');
		});

		await t.throwsAsync(getStream(got.stream('')), {
			name: 'ReadError',
		});
	});

	test('decompress option opts out of decompressing', withServer, async (t, server, got) => {
		server.get('/', (_request, response) => {
			response.setHeader('Content-Encoding', 'zstd');
			response.end(zstdData);
		});

		const {body} = await got({decompress: false, responseType: 'buffer'});
		t.is(Buffer.compare(body, zstdData), 0);
		t.false(Buffer.isBuffer(body));
	});

	test('preserves `headers` property', withServer, async (t, server, got) => {
		server.get('/', (_request, response) => {
			response.setHeader('Content-Encoding', 'zstd');
			response.end(zstdData);
		});

		t.truthy((await got('')).headers);
	});

	test('response has `url` and `requestUrl` properties', withServer, async (t, server, got) => {
		server.get('/', (_request, response) => {
			response.setHeader('Content-Encoding', 'zstd');
			response.end(zstdData);
		});

		const response = await got('');
		t.truthy(response.url);
		t.truthy(response.requestUrl);
	});
} else {
	test('zstd support not available - Node.js >= 22.15.0 required', t => {
		t.pass('Skipping zstd tests - not supported in this Node.js version');
	});
}
```

## File: `test/fixtures/ok`
```
ok
```

## File: `test/fixtures/stream-content-length`
```
Unicorns
```

## File: `test/helpers/create-http-test-server.ts`
```typescript
import http from 'node:http';
import type net from 'node:net';
import express, {type Express, type NextFunction} from 'express';
import bodyParser from 'body-parser';

export type HttpServerOptions = {
	bodyParser?: NextFunction | false;
};

export type ExtendedHttpTestServer = {
	http: http.Server;
	url: string;
	port: number;
	hostname: string;
	close: () => Promise<void>;
} & Express;

const createHttpTestServer = async (options: HttpServerOptions = {}): Promise<ExtendedHttpTestServer> => {
	const server = express() as ExtendedHttpTestServer;
	server.http = http.createServer(server);

	server.set('etag', false);

	if (options.bodyParser !== false) {
		server.use(bodyParser.json({limit: '1mb', type: 'application/json', ...options.bodyParser}));
		server.use(bodyParser.text({limit: '1mb', type: 'text/plain', ...options.bodyParser}));

		server.use(bodyParser.urlencoded({
			limit: '1mb',
			type: 'application/x-www-form-urlencoded',
			extended: true,
			...options.bodyParser,
		}));

		server.use(bodyParser.raw({limit: '1mb', type: 'application/octet-stream', ...options.bodyParser}));
	}

	await new Promise<void>((resolve, reject) => {
		const onError = (error: Error): void => {
			reject(error);
		};

		server.http.once('error', onError);
		server.http.listen(0, () => {
			server.http.off('error', onError);
			resolve();
		});
	});
	server.port = (server.http.address() as net.AddressInfo).port;
	server.url = `http://localhost:${server.port}`;
	server.hostname = 'localhost';

	server.close = async () => new Promise<void>((resolve, reject) => {
		server.http.closeAllConnections?.();
		server.http.close(error => {
			if (error) {
				reject(error);
				return;
			}

			resolve();
		});
	});

	return server;
};

export default createHttpTestServer;
```

## File: `test/helpers/create-https-test-server.ts`
```typescript
import https from 'node:https';
import type net from 'node:net';
import type {SecureContextOptions} from 'node:tls';
import express from 'express';
import pify from 'pify';
import pem from 'pem';
import type {CreateCsr, CreateCertificate} from '../types/pem.js';

export type HttpsServerOptions = {
	commonName?: string;
	days?: number;
	ciphers?: SecureContextOptions['ciphers'];
	honorCipherOrder?: SecureContextOptions['honorCipherOrder'];
	minVersion?: SecureContextOptions['minVersion'];
	maxVersion?: SecureContextOptions['maxVersion'];
};

export type ExtendedHttpsTestServer = {
	https: https.Server;
	caKey: Uint8Array;
	caCert: Uint8Array;
	url: string;
	port: number;
	close: () => Promise<void>;
} & express.Express;

const createHttpsTestServer = async (options: HttpsServerOptions = {}): Promise<ExtendedHttpsTestServer> => {
	const createCsr = pify(pem.createCSR as CreateCsr);
	const createCertificate = pify(pem.createCertificate as CreateCertificate);
	const commonName = options.commonName ?? 'localhost';
	const serverCertificateConfiguration = `
[req]
req_extensions = v3_req
[dn]
CN = ${commonName}
[v3_req]
basicConstraints = critical,CA:FALSE
keyUsage = critical,digitalSignature,keyEncipherment
extendedKeyUsage = serverAuth
subjectAltName = @alt_names
[alt_names]
DNS.1 = ${commonName}
`;
	const caCertificateConfiguration = `
[req]
req_extensions = v3_req
[dn]
CN = authority
[v3_req]
basicConstraints = critical,CA:TRUE
keyUsage = critical,keyCertSign,cRLSign
`;

	const caCsrResult = await createCsr({commonName: 'authority'});
	const caResult = await createCertificate({
		csr: caCsrResult.csr,
		clientKey: caCsrResult.clientKey,
		selfSigned: true,
		config: caCertificateConfiguration,
	});
	const caKey = caResult.clientKey;
	const caCert = caResult.certificate;

	const serverCsrResult = await createCsr({commonName});
	const serverResult = await createCertificate({
		csr: serverCsrResult.csr,
		clientKey: serverCsrResult.clientKey,
		serviceKey: caKey,
		serviceCertificate: caCert,
		config: serverCertificateConfiguration,
		days: options.days ?? 365,
	});
	const serverKey = serverResult.clientKey;
	const serverCert = serverResult.certificate;

	const server = express() as ExtendedHttpsTestServer;
	server.https = https.createServer(
		{
			key: serverKey,
			cert: serverCert,
			ca: caCert,
			requestCert: true,
			rejectUnauthorized: false, // This should be checked by the test
			ciphers: options.ciphers,
			honorCipherOrder: options.honorCipherOrder,
			minVersion: options.minVersion,
			maxVersion: options.maxVersion,
		},
		server,
	);

	server.set('etag', false);

	await pify(server.https.listen.bind(server.https))();

	server.caKey = caKey as any;
	server.caCert = caCert;
	server.port = (server.https.address() as net.AddressInfo).port;
	server.url = `https://localhost:${server.port}`;

	server.close = async () => new Promise<void>((resolve, reject) => {
		server.https.closeAllConnections?.();
		server.https.close(error => {
			if (error) {
				reject(error);
				return;
			}

			resolve();
		});
	});

	return server;
};

export default createHttpsTestServer;
```

## File: `test/helpers/invalid-url.ts`
```typescript

import type {ExecutionContext} from 'ava';

export default function invalidUrl(t: ExecutionContext, error: TypeError & NodeJS.ErrnoException, url: string) {
	t.is(error.code, 'ERR_INVALID_URL');

	if (error.message === 'Invalid URL') {
		t.is((error as any).input, url);
	} else {
		t.is(error.message.slice('Invalid URL: '.length), url);
	}
}
```

## File: `test/helpers/slow-data-stream.ts`
```typescript
import {Readable} from 'node:stream';
import type {Clock} from '@sinonjs/fake-timers';
import delay from 'delay';

export default function slowDataStream(clock?: Clock): Readable {
	let index = 0;

	return new Readable({
		async read() {
			if (clock) {
				clock.tick(100);
			} else {
				await delay(100);
			}

			if (index++ < 10) {
				this.push('data\n'.repeat(100));
			} else {
				this.push(null);
			}
		},
	});
}
```

## File: `test/helpers/types.ts`
```typescript
import type {Server} from 'node:http';
import type {TestServer} from 'create-test-server';

export type ExtendedHttpServer = {
	socketPath: string;
} & Server;

export type ExtendedTestServer = {
	hostname: string;
	sslHostname: string;
} & TestServer;

// https://github.com/sinonjs/fake-timers/pull/386
export type InstalledClock = any;
export type GlobalClock = any;
```

## File: `test/helpers/with-server.ts`
```typescript
import http from 'node:http';
import {promisify} from 'node:util';
import type {ExecutionContext, Macro} from 'ava';
import is from '@sindresorhus/is';
import {temporaryFile} from 'tempy';
import FakeTimers from '@sinonjs/fake-timers';
import got, {type Got, type ExtendOptions} from '../../source/index.js';
import createHttpsTestServer, {
	type ExtendedHttpsTestServer,
	type HttpsServerOptions,
} from './create-https-test-server.js';
import createHttpTestServer, {
	type ExtendedHttpTestServer,
	type HttpServerOptions,
} from './create-http-test-server.js';
import type {ExtendedHttpServer, GlobalClock, InstalledClock} from './types.js';

export type RunTestWithServer = (t: ExecutionContext, server: ExtendedHttpTestServer, got: Got, clock: GlobalClock) => Promise<void> | void;
export type RunTestWithHttpsServer = (t: ExecutionContext, server: ExtendedHttpsTestServer, got: Got, fakeTimer?: GlobalClock) => Promise<void> | void;
export type RunTestWithSocket = (t: ExecutionContext, server: ExtendedHttpServer) => Promise<void> | void;

const generateHook = ({install, options: testServerOptions}: {install?: boolean; options?: HttpServerOptions}): Macro<[RunTestWithServer]> => ({
	async exec(t, run) {
		// Re-enable body parsing to investigate https://github.com/sindresorhus/got/issues/1186
		const server = await createHttpTestServer(is.plainObject(testServerOptions)
			? testServerOptions
			: {
				bodyParser: {
					type: () => false,
				} as any,
			});

		const clock = install
			? FakeTimers.install({
				toFake: ['setTimeout', 'clearTimeout', 'setInterval', 'clearInterval'],
				shouldAdvanceTime: true,
				advanceTimeDelta: 1,
			})
			: FakeTimers.createClock() as GlobalClock;

		const context: Record<string, unknown> = {};
		Object.defineProperty(context, 'avaTest', {
			value: t.title,
			enumerable: false,
			writable: true,
			configurable: true,
		});

		const options: ExtendOptions = {
			context,
			handlers: [
				(options, next) => {
					const result = next(options);

					clock.tick(0);

					// @ts-expect-error FIXME: Incompatible union type signatures
					result.on('response', () => {
						clock.tick(0);
					});

					return result;
				},
			],
		};

		const preparedGot = got.extend({prefixUrl: server.url, ...options});

		try {
			await run(t, server, preparedGot, clock);
		} finally {
			await server.close();
		}

		if (install) {
			// eslint-disable-next-line @typescript-eslint/no-unnecessary-type-assertion
			(clock as InstalledClock).uninstall();
		}
	},
});

export const withBodyParsingServer = generateHook({install: false, options: {}});
export default generateHook({install: false});

export const withServerAndFakeTimers = generateHook({install: true});

const generateHttpsHook = (options?: HttpsServerOptions, installFakeTimer = false): Macro<[RunTestWithHttpsServer]> => ({
	async exec(t, run) {
		const server = await createHttpsTestServer(options);

		const fakeTimer = installFakeTimer
			? FakeTimers.install({
				toFake: ['setTimeout', 'clearTimeout', 'setInterval', 'clearInterval'],
				shouldAdvanceTime: true,
				advanceTimeDelta: 1,
			}) as GlobalClock
			: undefined;

		const httpsContext: Record<string, unknown> = {};
		Object.defineProperty(httpsContext, 'avaTest', {
			value: t.title,
			enumerable: false,
			writable: true,
			configurable: true,
		});

		const preparedGot = got.extend({
			context: httpsContext,
			handlers: [
				(options, next) => {
					const result = next(options);

					fakeTimer?.tick(0);

					// @ts-expect-error FIXME: Incompatible union type signatures
					result.on('response', () => {
						fakeTimer?.tick(0);
					});

					return result;
				},
			],
			prefixUrl: server.url,
			https: {
				certificateAuthority: (server as any).caCert,
				rejectUnauthorized: true,
			},
		});

		try {
			await run(t, server, preparedGot, fakeTimer);
		} finally {
			await server.close();
		}

		if (installFakeTimer) {
			// eslint-disable-next-line @typescript-eslint/no-unnecessary-type-assertion
			(fakeTimer as InstalledClock).uninstall();
		}
	},
});

export const withHttpsServer = generateHttpsHook;

// eslint-disable-next-line no-warning-comments
// TODO: Remove this when `create-test-server` supports custom listen.
export const withSocketServer: Macro<[RunTestWithSocket]> = {
	async exec(t, run) {
		const socketPath = temporaryFile({extension: 'socket'});

		const server = http.createServer((request, response) => {
			server.emit(request.url!, request, response);
		}) as ExtendedHttpServer;

		server.socketPath = socketPath;

		// @ts-expect-error TypeScript doesn't accept `callback` with no arguments
		await promisify<any>(server.listen.bind(server))(socketPath);

		try {
			await run(t, server);
		} finally {
			await promisify(server.close.bind(server))();
		}
	},
};
```

## File: `test/types/pem.ts`
```typescript
import type {
	CertificateCreationOptions,
	CertificateCreationResult,
	PrivateKeyCreationOptions,
	CSRCreationOptions,
	Callback,
} from 'pem';

export type CreateCertificate = (options: CertificateCreationOptions, callback: Callback<CertificateCreationResult>) => void;

export type CreateCsr = (options: CSRCreationOptions, callback: Callback<{csr: string; clientKey: string}>) => void;

export type CreatePrivateKey = (keyBitsize: number, options: PrivateKeyCreationOptions, callback: Callback<{key: string}>) => void;
```

## File: `test/types/create-test-server/index.d.ts`
```typescript
declare module 'create-test-server' {
	import type {Express} from 'express';

	function createTestServer(options: unknown): Promise<createTestServer.TestServer>;

	export = createTestServer;

	namespace createTestServer {
		export type TestServer = {
			caCert: string | Uint8Array | Array<string | Uint8Array>;
			port: number;
			url: string;
			sslPort: number;
			sslUrl: string;

			close: () => Promise<void>;
		} & Express;
	}
}
```

## File: `test/types/slow-stream/index.d.ts`
```typescript
import {PassThrough} from 'node:stream';

declare module 'slow-stream' {
	export = PassThrough;
}
```


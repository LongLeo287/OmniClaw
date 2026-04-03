---
id: avajs-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:51.977757
---

# KNOWLEDGE EXTRACT: avajs
> **Extracted on:** 2026-03-30 17:29:59
> **Source:** avajs

---

## File: `ava.md`
```markdown
# 📦 avajs/ava [🔖 PENDING/APPROVE]
🔗 https://github.com/avajs/ava


## Meta
- **Stars:** ⭐ 20852 | **Forks:** 🍴 1405
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Node.js test runner that lets you develop with confidence 🚀

## README (trích đầu)
```
*[Please support our friend Vadim Demedes and the people in Ukraine.](https://stand-with-ukraine.pp.ua/)*

---

# <img src="media/header.png" title="AVA" alt="AVA logo" width="530">

AVA is a test runner for Node.js with a concise API, detailed error output, embrace of new language features and thread isolation that lets you develop with confidence 🚀

Watch this repository and follow the [Discussions](https://github.com/avajs/ava/discussions) for updates.

Read our [contributing guide](../bmad_repo/CONTRIBUTING.md) if you're looking to contribute (issues / PRs / etc).

![](media/verbose-reporter.png)


Translations: [Español](https://github.com/avajs/ava-brain/knowledge/docs_legacy/blob/main/es_ES/readme.md), [Français](https://github.com/avajs/ava-brain/knowledge/docs_legacy/blob/main/fr_FR/readme.md), [Italiano](https://github.com/avajs/ava-brain/knowledge/docs_legacy/blob/main/it_IT/readme.md), [日本語](https://github.com/avajs/ava-brain/knowledge/docs_legacy/blob/main/ja_JP/readme.md), [한국어](https://github.com/avajs/ava-brain/knowledge/docs_legacy/blob/main/ko_KR/readme.md), [Português](https://github.com/avajs/ava-brain/knowledge/docs_legacy/blob/main/pt_BR/readme.md), [Русский](https://github.com/avajs/ava-brain/knowledge/docs_legacy/blob/main/ru_RU/readme.md), [简体中文](https://github.com/avajs/ava-brain/knowledge/docs_legacy/blob/main/zh_CN/readme.md)


## Why AVA?

- Minimal and fast
- Simple test syntax
- Runs tests concurrently
- Enforces writing atomic tests
- No implicit globals
- Includes TypeScript definitions
- [Magic assert](#magic-assert)
- [Isolated environment for each test file](./brain/knowledge/docs_legacy/01-writing-tests.md#test-isolation)
- [Promise support](./brain/knowledge/docs_legacy/01-writing-tests.md#promise-support)
- [Async function support](./brain/knowledge/docs_legacy/01-writing-tests.md#async-function-support)
- [Observable support](./brain/knowledge/docs_legacy/01-writing-tests.md#observable-support)
- [Enhanced assertion messages](./brain/knowledge/docs_legacy/03-assertions.md#enhanced-assertion-messages)
- [Automatic parallel test runs in CI](#parallel-runs-in-ci)
- [TAP reporter](./brain/knowledge/docs_legacy/05-command-line.md#tap-reporter)


## Usage

To install and set up AVA, run:

```console
npm init ava
```

Your `package.json` will then look like this (exact version notwithstanding):

```json
{
	"name": "awesome-package",
	"type": "module",
	"scripts": {
		"test": "ava"
	},
	"devDependencies": {
		"ava": "^5.0.0"
	}
}
```

Or if you prefer using Yarn:

```console
yarn add ava --dev
```

Alternatively you can install `ava` manually:

```console
npm install --save-dev ava
```

*Make sure to install AVA locally. AVA cannot be run globally.*

Don't forget to configure the `test` script in your `package.json` as per above.

### Create your test file

Create a file named `test.js` in the project root directory.

_Note that AVA's documentation assumes you're using ES modules._

```js
import test from 'ava';

test('foo', t => {
	t.pass();
});

test('bar', async t => {
	const bar = Promise.resolve('bar');
	t.is(await bar, 'bar');
});
```

### Running your tests

```console
npm test
```

Or with `npx`:

```console
npx ava
```

Run with the `--watch` flag to enable AVA's [watch mode](brain/knowledge/docs_legacy/recipes/watch-mode.md):

```console
npx ava --
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


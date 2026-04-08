---
id: repo-fetched-ava-133732
type: knowledge
owner: OA
registered_at: 2026-04-05T03:40:03.889661
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_ava_133732

## Assimilation Report
Auto-cloned repository: FETCHED_ava_133732

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: readme.md
```md
*[Please support our friend Vadim Demedes and the people in Ukraine.](https://stand-with-ukraine.pp.ua/)*

---

# <img src="media/header.png" title="AVA" alt="AVA logo" width="530">

AVA is a test runner for Node.js with a concise API, detailed error output, embrace of new language features and thread isolation that lets you develop with confidence 🚀

Watch this repository and follow the [Discussions](https://github.com/avajs/ava/discussions) for updates.

Read our [contributing guide](.github/CONTRIBUTING.md) if you're looking to contribute (issues / PRs / etc).

![](media/verbose-reporter.png)


Translations: [Español](https://github.com/avajs/ava-docs/blob/main/es_ES/readme.md), [Français](https://github.com/avajs/ava-docs/blob/main/fr_FR/readme.md), [Italiano](https://github.com/avajs/ava-docs/blob/main/it_IT/readme.md), [日本語](https://github.com/avajs/ava-docs/blob/main/ja_JP/readme.md), [한국어](https://github.com/avajs/ava-docs/blob/main/ko_KR/readme.md), [Português](https://github.com/avajs/ava-docs/blob/main/pt_BR/readme.md), [Русский](https://github.com/avajs/ava-docs/blob/main/ru_RU/readme.md), [简体中文](https://github.com/avajs/ava-docs/blob/main/zh_CN/readme.md)


## Why AVA?

- Minimal and fast
- Simple test syntax
- Runs tests concurrently
- Enforces writing atomic tests
- No implicit globals
- Includes TypeScript definitions
- [Magic assert](#magic-assert)
- [Isolated environment for each test file](./docs/01-writing-tests.md#test-isolation)
- [Promise support](./docs/01-writing-tests.md#promise-support)
- [Async function support](./docs/01-writing-tests.md#async-function-support)
- [Observable support](./docs/01-writing-tests.md#observable-support)
- [Enhanced assertion messages](./docs/03-assertions.md#enhanced-assertion-messages)
- [Automatic parallel test runs in CI](#parallel-runs-in-ci)
- [TAP reporter](./docs/05-command-line.md#tap-reporter)


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

Run with the `--watch` flag to enable AVA's [watch mode](docs/recipes/watch-mode.md):

```console
npx ava --watch
```

## Supported Node.js versions

AVA supports the latest release of any major version that [is supported by Node.js itself](https://github.com/nodejs/Release#release-schedule). Read more in our [support statement](docs/support-statement.md).

## Highlights

### Magic assert

AVA adds code excerpts and clean diffs for actual and expected values. If values in the assertion are objects or arrays, only a diff is displayed, to remove the noise and focus on the problem. The diff is syntax-highlighted too! If you are comparing strings, both single and multi line, AVA displays a different kind of output, highlighting the added or missing characters.

![](media/magic-assert-combined.png)

### Clean stack traces

AVA automatically removes unrelated lines in stack traces, allowing you to find the source of an error much faster, as seen above.

### Parallel runs in CI

AVA automatically detects whether your CI environment supports parallel builds. Each build will run a subset of all test files, while still making sure all tests get executed. See the [`ci-parallel-vars`](https://www.npmjs.com/package/ci-parallel-vars) package for a list of supported CI environments.

## Documentation

Please see the [files in the `docs` directory](./docs):

* [Writing tests](./docs/01-writing-tests.md)
* [Execution context](./docs/02-execution-context.md)
* [Assertions](./docs/03-assertions.md)
* [Snapshot testing](./docs/04-snapshot-testing.md)
* [Command line (CLI)](./docs/05-command-line.md)
* [Configuration](./docs/06-configuration.md)
* [Test timeouts](./docs/07-test-timeouts.md)

### Common pitfalls

We have a growing list of [common pitfalls](docs/08-common-pitfalls.md) you may experience while using AVA. If you encounter any issues you think are common, comment in [this issue](https://github.com/avajs/ava/issues/404).

### Recipes

- [Test setup](docs/recipes/test-setup.md)
- [TypeScript](docs/recipes/typescript.md)
- [Shared workers](docs/recipes/shared-workers.md)
- [Watch mode](docs/recipes/watch-mode.md)
- [When to use `t.plan()`](docs/recipes/when-to-use-plan.md)
- [Passing arguments to your test files](docs/recipes/passing-arguments-to-your-test-files.md)
- [Splitting tests in CI](docs/recipes/splitting-tests-ci.md)
- [Code coverage](docs/recipes/code-coverage.md)
- [Endpoint testing](docs/recipes/endpoint-testing.md)
- [Browser testing](docs/recipes/browser-testing.md)
- [Testing Vue.js components](docs/recipes/vue.md)
- [Debugging tests with Chrome DevTools](docs/recipes/debugging-with-chrome-devtools.md)
- [Debugging tests with VSCode](docs/recipes/debugging-with-vscode.md)
- [Debugging tests with WebStorm](docs/recipes/debugging-with-webstorm.md)
- [Isolated MongoDB integration tests](docs/recipes/isolated-mongodb-integration-tests.md)
- [Testing web apps using Puppeteer](docs/recipes/puppeteer.md)
- [Testing web apps using Selenium WebDriverJS](docs/recipes/testing-with-selenium-webdriverjs.md)

## FAQ

### How is the name written and pronounced?

AVA, not Ava or ava. Pronounced [`/ˈeɪvə/`](media/pronunciation.m4a?raw=true): Ay (f**a**ce, m**a**de) V (**v**ie, ha**v**e) A (comm**a**, **a**go)

### What is the header background?

It's the [Andromeda galaxy](https://simple.wikipedia.org/wiki/Andromeda_galaxy).

### What is the difference between concurrency and parallelism?

[Concurrency is not parallelism. It enables parallelism.](https://stackoverflow.com/q/1050222)

## Support

- [GitHub Discussions](https://github.com/avajs/ava/discussions)

## Related

- [eslint-plugin-ava](https://github.com/avajs/eslint-plugin-ava) — Lint rules for AVA tests
- [@ava/typescript](https://github.com/avajs/typescript) — Test TypeScript projects
- [@ava/cooperate](https://github.com/avajs/cooperate) — Low-level primitives to enable cooperation between test files
- [@ava/get-port](https://github.com/avajs/get-port) — Reserve a port while testing

## Links

- [AVA stickers, t-shirts, etc](https://www.redbubble.com/people/sindresorhus/works/30330590-ava-logo)
- [Awesome list](https://github.com/avajs/awesome-ava)
- [Do you like AVA? Donate here!](https://opencollective.com/ava)
- [More…](https://github.com/avajs/awesome-ava)

## Team

[![Mark Wubben](https://github.com/novemberborn.png?size=100)](https://github.com/novemberborn) | [![Sindre Sorhus](https://github.com/sindresorhus.png?size=100)](https://github.com/sindresorhus)
---|---
[Mark Wubben](https://novemberborn.net) | [Sindre Sorhus](https://sindresorhus.com)

###### Former

- [Kevin Mårtensson](https://github.com/kevva)
- [James Talmage](https://github.com/jamestalmage)
- [Juan Soto](https://github.com/sotojuan)
- [Jeroen Engels](https://github.com/jfmengels)
- [Vadim Demedes](https://github.com/vadimdemedes)


<div align="center">
	<br>
	<br>
	<br>
	<a href="https://avajs.dev">
		<img src="media/logo.svg" width="200" alt="AVA">
	</a>
	<br>
	<br>
</div>

```

### File: maintaining.md
```md
# Maintaining

## Conduct

**Be kind to everyone.** Read and adhere to the [Code of Conduct](.github/CODE_OF_CONDUCT.md).

## Testing

- `npm test`: Lint the code and run the entire test suite with coverage.
- `npx tap test-tap/fork.js --bail`: Run a specific test file and bail on the first failure (useful when hunting bugs).
- `npx test-ava test/{file}.js`: Run self-hosted tests.

## CI

- Tests sometimes fail on Windows. Review the errors carefully.
- At least one Windows job must pass.
- All other jobs must pass.

## Updating dependencies

- Make sure new dependency versions are compatible with our supported Node.js versions.
- Leave the TypeScript dependency as it is, to avoid accidental breakage.
- Open a PR with the updates and only merge when CI passes (see the previous section).

## Updating TypeScript

TypeScript itself does not follow SemVer. Consequently we may have to make changes to the type definition that, technically, are breaking changes for users with an older TypeScript version. That's OK, but we should be aware.

Only update the TypeScript dependency when truly necessary. This helps avoid accidental breakage. For instance we won't accidentally rely on newer TypeScript features.

Speaking of, using newer TypeScript features could be considered a breaking change. This needs to be assessed on a case-by-case basis.

## Pull requests

- New features should come with tests and documentation.
- Ensure the [contributing guidelines](.github/CONTRIBUTING.md) are followed.
- Squash commits when merging.

## Experiments

- Implement breaking changes as an experiment first, requiring opt-in.
- Ship new features early by treating them as an experiment, requiring opt-in.

## Release process

Releases are triggered manually via the [*Release* workflow](https://github.com/avajs/ava/actions/workflows/release.yml).

### Releasing a new version from `main`

1. Go to the [*Release* workflow](https://github.com/avajs/ava/actions/workflows/release.yml) and click "Run workflow".
1. Set **ref** to the commit SHA that should be released (must be HEAD of `main`).
1. Set **new version** to the desired `npm version` increment (e.g. `patch`, `minor`, `major`, or an explicit version like `1.2.3`).
1. Leave **skip CI status check** unchecked unless you have a specific reason.

The workflow will:

- Validate that the commit is HEAD of `main` and that CI has passed for it.
- Pause for manual approval in the [`npm` environment](https://github.com/avajs/ava/settings/environments).
- After approval, re-verify the commit is still HEAD of `main`.
- Then run `npm version` to update `package.json` and `package-lock.json`, commit the result, and push the commit and the resulting tag to `main`.
- Publish to npm with provenance via OIDC, and create a draft GitHub release.

### Releasing from an existing tag

If a version tag already exists on `main` (e.g. `v1.2.3`):

1. Go to the [*Release* workflow](https://github.com/avajs/ava/actions/workflows/release.yml) and click "Run workflow".
1. Set **ref** to the existing tag (e.g. `v1.2.3`).
1. Leave **new version** empty.

The workflow will verify that the tag matches the version in `package.json`, check CI, then publish and create a draft release after approval.

### After the workflow completes

Review and publish the [draft GitHub release](https://github.com/avajs/ava/releases).

### Setup requirements

The npm package must have [trusted publishing](https://docs.npmjs.com/generating-provenance-statements) configured for this repository and the `Release` workflow so that OIDC-based publishing works.

The [`npm` environment](https://github.com/avajs/ava/settings/environments) must have at least one required reviewer configured to gate the publish step behind manual approval.

#### GitHub App for bypassing branch rulesets

The `main` branch has rulesets that prevent direct pushes, including from `GITHUB_TOKEN`. When releasing a new version from a commit ref, the workflow creates the version commit (updating `package.json` and `package-lock.json`) and the version tag via the GitHub API. The commit is created using a GitHub App token so that the App's identity can be granted a ruleset bypass, while the lightweight tag is created with `GITHUB_TOKEN`.

The App must be configured with:

- **Repository permissions:** Write access to the `package.json` and `package-lock.json` files
- **Ruleset bypass** granted in the `main` branch ruleset settings

Two repository configuration values are required:

- **Variable** `LAUNCHBOT_ID` — the numeric App ID (found in the App's settings page)
- **Secret** `LAUNCHBOT_PRIVATE_KEY` — the App's private key in PEM format

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for ava
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: .github\CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

Translations: [Español](https://github.com/avajs/ava-docs/blob/main/es_ES/code-of-conduct.md), [Français](https://github.com/avajs/ava-docs/blob/main/fr_FR/code-of-conduct.md), [Italiano](https://github.com/avajs/ava-docs/blob/main/it_IT/code-of-conduct.md), [日本語](https://github.com/avajs/ava-docs/blob/main/ja_JP/code-of-conduct.md), [Português](https://github.com/avajs/ava-docs/blob/main/pt_BR/code-of-conduct.md), [Русский](https://github.com/avajs/ava-docs/blob/main/ru_RU/code-of-conduct.md), [简体中文](https://github.com/avajs/ava-docs/blob/main/zh_CN/code-of-conduct.md)

## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of experience,
nationality, personal appearance, race, religion, or sexual identity and
orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at sindresorhus@gmail.com. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at [http://contributor-covenant.org/version/1/4][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/

```

### File: .github\CONTRIBUTING.md
```md
# Contributing to AVA

✨ Thanks for contributing to AVA! ✨

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

Translations: [Español](https://github.com/avajs/ava-docs/blob/main/es_ES/contributing.md), [Français](https://github.com/avajs/ava-docs/blob/main/fr_FR/contributing.md), [Italiano](https://github.com/avajs/ava-docs/blob/main/it_IT/contributing.md), [日本語](https://github.com/avajs/ava-docs/blob/main/ja_JP/contributing.md), [Português](https://github.com/avajs/ava-docs/blob/main/pt_BR/contributing.md), [Русский](https://github.com/avajs/ava-docs/blob/main/ru_RU/contributing.md), [简体中文](https://github.com/avajs/ava-docs/blob/main/zh_CN/contributing.md)

## How can I contribute?

### Improve documentation

As a user of AVA you're the perfect candidate to help us improve our documentation. Typo corrections, error fixes, better explanations, more examples, etc. Open issues for things that could be improved. [Help translate our docs.](https://github.com/avajs/ava-docs) Anything. Even improvements to this document.

Use the [`scope:documentation` label](https://github.com/avajs/ava/labels/scope%3Adocumentation) to find suggestions for what we'd love to see more documentation on.

### Improve issues

Some issues are created with missing information, not reproducible, or plain invalid. Help make them easier to resolve. Handling issues takes a lot of time that we could rather spend on fixing bugs and adding features.

### Give feedback on issues

We're always looking for more opinions on discussions in the issue tracker. It's a good opportunity to influence the future direction of AVA.

The [`needs triage`](https://github.com/avajs/ava/labels/needs%20triage) and [`question`](https://github.com/avajs/ava/labels/question) labels are a good place to find ongoing discussions.

### Help out

You can use issue labels to discover issues you could help out with:

* [`blocked` issues](https://github.com/avajs/ava/labels/blocked) need help getting unstuck
* [`bug` issues](https://github.com/avajs/ava/labels/bug) are known bugs we'd like to fix
* [`enhancement` issues](https://github.com/avajs/ava/labels/enhancement) are features we're open to including
* [`performance` issues](https://github.com/avajs/ava/labels/performance) track ideas on how to improve AVA's performance

The [`help wanted`](https://github.com/avajs/ava/labels/help%20wanted) and [`good for beginner`](https://github.com/avajs/ava/labels/good%20for%20beginner) labels are especially useful.

You may find an issue is assigned. Please double-check before starting on this issue because somebody else is likely already working on it.

We'd like to fix [`priority` issues](https://github.com/avajs/ava/labels/priority) first. We'd love to see progress on [`low-priority` issues](https://github.com/avajs/ava/labels/low%20priority) too. [`future` issues](https://github.com/avajs/ava/labels/future) are those that we'd like to get to, but not anytime soon. Please check before working on these since we may not yet want to take on the burden of supporting those features.

Read on for tips on contributing code.

### Hang out and chat

We're using [GitHub Discussions](https://github.com/avajs/ava/discussions). Jump in there and lurk, talk to us, and help others.

## Contributing code

Once you find an issue you'd like to work on leave a comment so others are aware. We'll then assign you to the issue.

Of course you can work on things that do not yet have an issue. However if you're going to be putting in a lot of effort it's best to discuss it first.

When you're ready to get feedback on your work, open a [draft pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests#draft-pull-requests). It's fine if the work's not yet done, but please do let us know what's remaining. This lets reviewers know not to nit-pick small details or point out improvements you already know you need to make.

Reviewing large pull requests can take a lot of time. Time that may not always be available. Smaller pull requests may land more quickly. If you're introducing a new feature think about how it might be broken up. It's OK to land features as [opt-in experiments](https://github.com/avajs/ava/blob/master/docs/06-configuration.md#experiments). These require less documentation and test coverage.

Try and avoid making breaking changes. Those take more time to ship. Instead make the new behavior opt-in. This way your feature can ship, and you can use it, on its own schedule.

Non-experimental features should be accompanied with tests and documentation.

Don't include unrelated changes in your pull request. Make sure tests pass on your machine by running `npm test`. You can run specific test files as well using `npx tap test-tap/{file}.js` or `npx test-ava test/{file}.js`.

When you make a pull request please use a clear and descriptive title. Be specific about what's changed and why.

Please make sure the *Allow edits from maintainers* box is checked. That way we can make certain minor changes ourselves, allowing your pull request to be merged sooner.

You might be asked to make changes to your pull request. There's never a need to open another pull request. Push more commits to your existing branch. We'll squash them when we merge the PR.

Dependencies are managed using `npm`. Only update dependencies when needed for your pull request. Don't rebuild the lockfile.

And finally, have fun!

```

### File: docs\01-writing-tests.md
```md
# Writing tests

Translations: [Français](https://github.com/avajs/ava-docs/blob/main/fr_FR/docs/01-writing-tests.md)

Tests are run concurrently. You can specify synchronous and asynchronous tests. Tests are considered synchronous unless you return a promise or an [observable](https://github.com/zenparsing/zen-observable).

You must define all tests synchronously. They can't be defined inside `setTimeout`, `setImmediate`, etc.

AVA tries to run test files with their current working directory set to the directory that contains your `package.json` file.

## Test isolation

By default each test file is run in a new worker thread. You can fall back running in separate processes (see `workerThreads` [CLI option](./06-configuration.md#options)).

AVA will set `process.env.NODE_ENV` to `test`, unless the `NODE_ENV` environment variable has been set. This is useful if the code you're testing has test defaults (for example when picking what database to connect to). It may cause your code or its dependencies to behave differently though. Note that `'NODE_ENV' in process.env` will always be `true`.

## Declaring tests

To declare a test you call the `test` function you imported from AVA. Provide the required title and implementation function. Titles must be unique within each test file. The function will be called when your test is run. It's passed an [execution object](./02-execution-context.md) as its first argument.

```js
import test from 'ava';

test('my passing test', t => {
	t.pass();
});
```

## Running tests serially

Tests are run concurrently by default, however, sometimes you have to write tests that cannot run concurrently. In these rare cases you can use the `.serial` modifier. It will force those tests to run serially *before* the concurrent ones.

```js
test.serial('passes serially', t => {
	t.pass();
});
```

Note that this only applies to tests within a particular test file. AVA will still run multiple tests files at the same time unless you pass the [`--serial` CLI flag](./05-command-line.md).

You can use the `.serial` modifier with all tests, hooks and even `.todo()`, but it's only available on the `test` function.

## Promise support

Tests may return a promise. AVA will wait for the promise to resolve before ending the test. If the promise rejects the test will fail.

```js
test('resolves with unicorn', t => {
	return somePromise().then(result => {
		t.is(result, 'unicorn');
	});
});
```

## Async function support

AVA comes with built-in support for [async functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function).

```js
test(async function (t) {
	const value = await promiseFn();
	t.true(value);
});

// Async arrow function
test('promises the truth', async t => {
	const value = await promiseFn();
	t.true(value);
});
```

## Observable support

AVA comes with built-in support for [observables](https://github.com/zenparsing/es-observable). If you return an observable from a test, AVA will automatically consume it to completion before ending the test.

```js
test('handles observables', t => {
	t.plan(3);
	return Observable.of(1, 2, 3, 4, 5, 6)
		.filter(n => {
			// Only even numbers
			return n % 2 === 0;
		})
		.map(() => t.pass());
});
```

## Running specific tests

During development it can be helpful to only run a few specific tests. This can be accomplished using the `.only` modifier:

```js
test('will not be run', t => {
	t.fail();
});

test.only('will be run', t => {
	t.pass();
});
```

You can use the `.only` modifier with all tests. It cannot be used with hooks or `.todo()`.

*Note:* The `.only` modifier applies to the test file it's defined in, so if you run multiple test files, tests in other files will still run. If you want to only run the `test.only` test, provide just that test file to AVA.

## Skipping tests

Sometimes failing tests can be hard to fix. You can tell AVA to temporarily skip these tests using the `.skip` modifier. They'll still be shown in the output (as having been skipped) but are never run.

```js
test.skip('will not be run', t => {
	t.fail();
});
```

You must specify the implementation function. You can use the `.skip` modifier with all tests and hooks, but not with `.todo()`. You can not apply further modifiers to `.skip`.

If the test is likely to be failing for a while, use `.failing()` instead.

## Test placeholders ("todo")

You can use the `.todo` modifier when you're planning to write a test. Like skipped tests these placeholders are shown in the output. They only require a title; you cannot specify the implementation function.

```js
test.todo('will think about writing this later');
```

You can signal that you need to write a serial test:

```js
test.serial.todo('will think about writing this later');
```

## Failing tests

You can use the `.failing` modifier to document issues with your code that need to be fixed. Failing tests are run just like normal ones, but they are expected to fail, and will not break your build when they do. If a test marked as failing actually passes, it will be reported as an error and fail the build with a helpful message instructing you to remove the `.failing` modifier.

This allows you to merge `.failing` tests before a fix is implemented without breaking CI. This is a great way to recognize good bug report PR's with a commit credit, even if the reporter is unable to actually fix the problem.

```js
// See: github.com/user/repo/issues/1234
test.failing('demonstrate some bug', t => {
	t.fail(); // Test will count as passed
});
```

## Before & after hooks

AVA lets you register hooks that are run before and after your tests. This allows you to run setup and/or teardown code.

`test.before()` registers a hook to be run before the first test in your test file. Similarly `test.after()` registers a hook to be run after the last test. Use `test.after.always()` to register a hook that will **always** run once your tests and other hooks complete. `.always()` hooks run regardless of whether there were earlier failures, so they are ideal for cleanup tasks. Note however that uncaught exceptions, unhandled rejections or timeouts will crash your tests, possibly preventing `.always()` hooks from running.

`test.beforeEach()` registers a hook to be run before each test in your test file. Similarly `test.afterEach()` registers a hook to be run after each test. Use `test.afterEach.always()` to register an after hook that is called even if other test hooks, or the test itself, fail.

If a test is skipped with the `.skip` modifier, the respective `.beforeEach()`, `.afterEach()` and `.afterEach.always()` hooks are not run. Likewise, if all tests in a test file are skipped `.before()`, `.after()` and `.after.always()` hooks for the file are not run.

*You may not need to use `.afterEach.always()` hooks to clean up after a test.* You can use [`t.teardown()`](./02-execution-context.md#tteardownfn) to undo side-effects *within* a particular test. Or use [`registerCompletionHandler()`](./08-common-pitfalls.md#timeouts-because-a-file-failed-to-exit) to run cleanup code after AVA has completed its work.

Like `test()` these methods take an optional title and an implementation function. The title is shown if your hook fails to execute. The implementation is called with an [execution object](./02-execution-context.md). You can use assertions in your hooks. You can also pass a [macro function](#reusing-test-logic-through-macros) and additional arguments.

`.before()` hooks execute before `.beforeEach()` hooks. `.afterEach()` hooks execute before `.after()` hooks. Within their category the hooks execute in the order they were defined. By default hooks execute concurrently, but you can use `test.serial` to ensure only that single hook is run at a time. Unlike with tests, serial hooks are *not* run before other hooks:

```js
test.before(t => {
	// This runs before all tests
});

test.before(t => {
	// This runs concurrently with the above
});

test.serial.before(t => {
	// This runs after the above
});

test.serial.before(t => {
	// This too runs after the above, and before tests
});

test.after('cleanup', t => {
	// This runs after all tests
});

test.after.always('guaranteed cleanup', t => {
	// This will always run, regardless of earlier failures
});

test.beforeEach(t => {
	// This runs before each test
});

test.afterEach(t => {
	// This runs after each test
});

test.afterEach.always(t => {
	// This runs after each test and other test hooks, even if they failed
});

test('title', t => {
	// Regular test
});
```

Hooks can be synchronous or asynchronous, just like tests. To make a hook asynchronous return a promise or observable, or use an async function.

```js
test.before(async t => {
	await promiseFn();
});

test.after(t => {
	return new Promise(/* ... */);
});
```

Keep in mind that the `.beforeEach()` and `.afterEach()` hooks run just before and after a test is run, and that by default tests run concurrently. This means each multiple `.beforeEach()` hooks may run concurrently. Using `test.serial.beforeEach()` does not change this. If you need to set up global state for each test (like spying on `console.log` [for example](https://github.com/avajs/ava/issues/560)), you'll need to make sure the tests themselves are [run serially](#running-tests-serially).

Remember that AVA runs each test file in its own process. You may not have to clean up global state in a `.after()`-hook since that's only called right before the process exits.

## Test context

Hooks can share context with the test:

```js
test.beforeEach(t => {
	t.context.data = generateUniqueData();
});

test('context data is foo', t => {
	t.is(t.context.data + 'bar', 'foobar');
});
```

If `.before()` hooks treat `t.context` as an object, a shallow copy is made and passed to `.beforeEach()` hooks and / or tests. Other types of values are passed as-is. The `.after()` and `.after.always()` hooks receive the original context value.

For `.beforeEach()`, `.afterEach()` and `.afterEach.always()` hooks the context is *not* shared between different tests, allowing you to set up data such that it will not leak to other tests.

By default `t.context` is an object but you can reassign it:

```js
test.before(t => {
	t.context = 'unicorn';
});

test('context is unicorn', t => {
	t.is(t.context, 'unicorn');
});
```

## Retrieving test metadata

Access data about the currently loaded test file run by reading `test.meta`.

Available properties:

* `file`: path to the test file, as a file URL string
* `snapshotDirectory`: directory where snapshots are stored, as a file URL string

```js
import test from 'ava';

console.log('Test file currently being run:', test.meta.file);
```

## Reusing test logic through macros

[![Open in StackBlitz](https://developer.stackblitz.com/img/open_in_stackblitz.svg)](https://stackblitz.com/github/avajs/ava/tree/main/examples/macros?file=test.js&terminal=test&view=editor)

Additional arguments passed to the test declaration will be passed to the test implementation. This is useful for creating reusable test macros.

You _could_ use plain functions:

```js
function macro(t, input, expected) {
	t.is(eval(input), expected);
}

test('2 + 2 = 4', macro, '2 + 2', 4);
test('2 * 3 = 6', macro, '2 * 3', 6);
```

However the preferred approach is to use the `test.macro()` helper:

```js
import test from 'ava';

const macro = test.macro((t, input, expected) => {
	t.is(eval(input), expected);
});

test('title', macro, '3 * 3', 9);
```

Or with a title function:

```js
import test from 'ava';

const macro = test.macro({
	exec(t, input, expected) {
		t.is(eval(input), expected);
	},
	title(providedTitle = '', input, expected) {
		return `${providedTitle} ${input} = ${expected}`.trim();
	},
});

test(macro, '2 + 2', 4);
test(macro, '2 * 3', 6);
test('providedTitle', macro, '3 * 3', 9);
```

The `providedTitle` argument defaults to `undefined` if the user does not supply a string title. This means you can use a parameter assignment to set the default value. The example above uses the empty string as the default.

```

### File: docs\02-execution-context.md
```md
# Execution Context (`t` argument)

Translations: [Français](https://github.com/avajs/ava-docs/blob/main/fr_FR/docs/02-execution-context.md)

Each test or hook is called with an execution context. By convention it's named `t`.

```js
import test from 'ava';

test('my passing test', t => {
	t.pass();
});
```

Each test or hook receives a different object. It contains the [assertions](./03-assertions.md) as well as the methods and properties listed below.

## `t.title`

The test title.

## `t.context`

Contains shared state from hooks.

## `t.passed`

When used in `test.afterEach()` or `test.afterEach.always()` hooks this tells you whether the test has passed. When used in a test itself (including teardown functions) this remains `true` until an assertion fails, the test has ended with an error, or a teardown function caused an error. This value has no meaning in other hooks.

## `t.log(...values)`

Log values contextually alongside the test result instead of immediately printing them to `stdout`. Behaves somewhat like `console.log`, but without support for placeholder tokens.

## `t.plan(count)`

Plan how many assertions there are in the test. The test will fail if the actual assertion count doesn't match the number of planned assertions. See [assertion planning](./03-assertions.md#assertion-planning).

## `t.teardown(fn)`

Registers the `fn` function to be run after the test has finished. You can register multiple functions. They'll run in reverse order, so the last registered function is run first. You can use asynchronous functions: only one will run at a time.

You cannot perform assertions using the `t` object or register additional functions from inside `fn`.

You cannot use `t.teardown()` in hooks either.

## `t.timeout(ms)`

Set a timeout for the test, in milliseconds. The test will fail if this timeout is exceeded. The timeout is reset each time an assertion is made.

Use `t.timeout.clear()` to clear the timeout and restore the default behavior.

```

### File: docs\03-assertions.md
```md
# Assertions

Translations: [Français](https://github.com/avajs/ava-docs/blob/main/fr_FR/docs/03-assertions.md)

Assertions are mixed into the [execution object](./02-execution-context.md) provided to each test implementation:

```js
test('unicorns are truthy', t => {
	t.truthy('unicorn'); // Assertion
});
```

Assertions are bound to their test so you can assign them to a variable or pass them around:

```js
test('unicorns are truthy', t => {
	const truthy = t.truthy;
	truthy('unicorn');
});
```

If multiple assertion failures are encountered within a single test, AVA will only display the *first* one.

Assertions return `true` if they've passed and throw otherwise. Catching this error does not cause the test to pass. The error value is undocumented.

If you use TypeScript you can use some assertions as type guards.

Note that the "throws" assertions return the error that was thrown (provided the assertion passed).

## Assertion planning

Assertion plans ensure tests only pass when a specific number of assertions have been executed. They'll help you catch cases where tests exit too early. They'll also cause tests to fail if too many assertions are executed, which can be useful if you have assertions inside callbacks or loops.

If you do not specify an assertion plan, your test will still fail if no assertions are executed. Set the `failWithoutAssertions` option to `false` in AVA's [`package.json` configuration](./06-configuration.md) to disable this behavior.

Note that, unlike [`tap`](https://www.npmjs.com/package/tap) and [`tape`](https://www.npmjs.com/package/tape), AVA does *not* automatically end a test when the planned assertion count is reached.

These examples will result in a passed test:

```js
test('resolves with 3', t => {
	t.plan(1);

	return Promise.resolve(3).then(n => {
		t.is(n, 3);
	});
});
```

These won't:

```js
test('loops twice', t => {
	t.plan(2);

	for (let i = 0; i < 3; i++) {
		t.true(i < 3);
	}
}); // Fails, 3 assertions are executed which is too many

test('invokes callback synchronously', t => {
	t.plan(1);

	someAsyncFunction(() => {
		t.pass();
	});
}); // Fails, the test ends synchronously before the assertion is executed
```

## Skipping assertions

Any assertion can be skipped using the `skip` modifier. Skipped assertions are still counted, so there is no need to change your planned assertion count.

```js
test('skip assertion', t => {
	t.plan(2);
	t.is.skip(foo(), 5); // No need to change your plan count when skipping
	t.is(1, 1);
});
```

## Custom assertions

You can use any assertion library instead of or in addition to the built-in one, provided it throws exceptions when the assertion fails.

This won't give you as nice an experience as you'd get with the [built-in assertions](#built-in-assertions) though, and you won't be able to use the [assertion planning](#assertion-planning) ([see #25](https://github.com/avajs/ava/issues/25)).

You'll have to configure AVA to not fail tests if no assertions are executed, because AVA can't tell if custom assertions pass. Set the `failWithoutAssertions` option to `false` in AVA's [`package.json` configuration](./06-configuration.md).

```js
import assert from 'assert';

test('custom assertion', t => {
	assert(true);
});
```

## Built-in assertions

### `.pass(message?)`

Passing assertion.

### `.fail(message?)`

Failing assertion.

### `.assert(actual, message?)`

Asserts that `actual` is truthy.

### `.truthy(actual, message?)`

Assert that `actual` is truthy.

### `.falsy(actual, message?)`

Assert that `actual` is falsy.

### `.true(actual, message?)`

Assert that `actual` is `true`.

### `.false(actual, message?)`

Assert that `actual` is `false`.

### `.is(actual, expected, message?)`

Assert that `actual` is the same as `expected`. This is based on [`Object.is()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/is).

### `.not(actual, expected, message?)`

Assert that `actual` is not the same as `expected`. This is based on [`Object.is()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/is).

### `.deepEqual(actual, expected, message?)`

Assert that `actual` is deeply equal to `expected`. See [Concordance](https://github.com/concordancejs/concordance) for details.

### `.notDeepEqual(actual, expected, message?)`

Assert that `actual` is not deeply equal to `expected`. The inverse of `.deepEqual()`.

### `.like(actual, selector, message?)`

Assert that `actual` is like `selector`. This is a variant of `.deepEqual()`, however `selector` does not need to have the same enumerable properties as `actual` does.

Instead AVA derives a *comparable* value from `actual`, recursively based on the enumerable shape of `selector`. This value is then compared to `selector` using `.deepEqual()`.

Any values in `selector` that are not arrays or regular objects should be deeply equal to the corresponding values in `actual`.

In the following example, the `map` property of `actual` must be deeply equal to that of `selector`. However `nested.qux` is ignored, because it's not in `selector`.

```js
t.like({
	map: new Map([['foo', 'bar']]),
	nested: {
		baz: 'thud',
		qux: 'quux'
	}
}, {
	map: new Map([['foo', 'bar']]),
	nested: {
		baz: 'thud',
	}
})
```

You can also use arrays, but note that any indices in `actual` that are not in `selector` are ignored:

```js
t.like([1, 2, 3, 4], [1, , 3])
```

### `.throws(fn, expectation?, message?)`

Assert that an error is thrown. `fn` must be a function which should throw. By default, the thrown value *must* be an error. It is returned so you can run more assertions against it.
`expectation` can be an object with one or more of the following properties:

* `any`: a boolean, if `true` then the thrown value does not need to be an error. Defaults to `false`
* `instanceOf`: a constructor, the thrown error must be an instance of
* `is`: the thrown error must be strictly equal to `expectation.is`
* `message`: the following types are valid:
  * *string* - it is compared against the thrown error's message
  * *regular expression* - it is matched against this message
  * *function* - it is passed the thrown error message and must return a boolean for whether the assertion passed
* `name`: the expected `.name` value of the thrown error
* `code`: the expected `.code` value of the thrown error

`expectation` does not need to be specified. If you don't need it but do want to set an assertion message you have to specify `undefined`.

Example:

```js
const fn = () => {
	throw new TypeError('🦄');
};

test('throws', t => {
	const error = t.throws(() => {
		fn();
	}, {instanceOf: TypeError});

	t.is(error.message, '🦄');
});
```

### `.throwsAsync(thrower, expectation?, message?)`

Assert that an error is thrown. `thrower` can be an async function which should throw, or a promise that should reject. This assertion must be awaited.

By default, the thrown value *must* be an error. It is returned so you can run more assertions against it.
`expectation` can be an object with one or more of the following properties:

* `any`: a boolean, if `true` then the thrown value does not need to be an error. Defaults to `false`
* `instanceOf`: a constructor, the thrown error must be an instance of
* `is`: the thrown error must be strictly equal to `expectation.is`
* `message`: the following types are valid:
  * *string* - it is compared against the thrown error's message
  * *regular expression* - it is matched against this message
  * *function* - it is passed the thrown error message and must return a boolean for whether the assertion passed
* `name`: the expected `.name` value of the thrown error
* `code`: the expected `.code` value of the thrown error

`expectation` does not need to be specified. If you don't need it but do want to set an assertion message you have to specify `undefined`.

Example:

```js
test('throws', async t => {
	await t.throwsAsync(async () => {
		throw new TypeError('🦄');
	}, {instanceOf: TypeError, message: '🦄'});
});
```

```js
const promise = Promise.reject(new TypeError('🦄'));

test('rejects', async t => {
	const error = await t.throwsAsync(promise);
	t.is(error.message, '🦄');
});
```

### `.notThrows(fn, message?)`

Assert that no error is thrown. `fn` must be a function which shouldn't throw.

### `.notThrowsAsync(nonThrower, message?)`

Assert that no error is thrown. `nonThrower` can be an async function which shouldn't throw, or a promise that should resolve.

Like the `.throwsAsync()` assertion, you must wait for the assertion to complete:

```js
test('resolves', async t => {
	await t.notThrowsAsync(promise);
});
```

### `.regex(contents, regex, message?)`

Assert that `contents` matches `regex`.

### `.notRegex(contents, regex, message?)`

Assert that `contents` does not match `regex`.

### `.snapshot(expected, message?)`

Compares the `expected` value with a previously recorded snapshot. Snapshots are stored for each test, so ensure you give your tests unique titles.

### `.try(title?, implementation | macro, ...args?)`

`.try()` allows you to *try* assertions without causing the test to fail.

The implementation function behaves the same as any other test function. You can even use macros. The first title argument is always optional. Additional arguments are passed to the implementation or macro function.

`.try()` is an asynchronous function. You must `await` it. The result object has `commit()` and `discard()` methods. You must decide whether to commit or discard the result. If you commit a failed result, your test will fail. Calling `commit()` on a failed result will throw an error.

You can check whether the attempt passed using the `passed` property. Any assertion errors are available through the `errors` property. The attempt title is available through the `title` property.

Logs from `t.log()` are available through the `logs` property. You can choose to retain these logs as part of your test by passing `{retainLogs: true}` to the `commit()` and `discard()` methods.

The implementation function receives its own [execution context](./02-execution-context.md), just like a test function. You must be careful to only perform assertions using the attempt's execution context. At least one assertion must pass for your attempt to pass.

You may run multiple attempts concurrently, within a single test. However you can't use snapshots when you do so.

Example:

```js
const twoRandomIntegers = () => {
	const rnd = Math.round(Math.random() * 100);
	const x = rnd % 10;
	const y = Math.floor(rnd / 10);
	return [x, y];
};

test('flaky macro', async t => {
	const firstTry = await t.try((tt, a, b) => {
		tt.is(a, b);
	}, ...twoRandomIntegers());

	if (firstTry.passed) {
		firstTry.commit();
		return;
	}

	firstTry.discard();
	t.log(firstTry.errors);

	const secondTry = await t.try((tt, a, b) => {
		tt.is(a, b);
	}, ...twoRandomIntegers());
	secondTry.commit();
});
```

```

### File: docs\04-snapshot-testing.md
```md
# Snapshot testing

Translations: [Français](https://github.com/avajs/ava-docs/blob/main/fr_FR/docs/04-snapshot-testing.md)

AVA supports snapshot testing, [as introduced by Jest](https://facebook.github.io/jest/docs/snapshot-testing.html), through its [Assertions](./03-assertions.md) interface. You can snapshot any value.

Snapshots are stored alongside your test files. If your tests are in a `test` or `tests` folder the snapshots will be stored in a `snapshots` folder. If your tests are in a `__tests__` folder then they they'll be stored in a `__snapshots__` folder.

Say you have `~/project/test/main.js` which contains snapshot assertions. AVA will create two files:

* `~/project/test/snapshots/main.js.snap`
* `~/project/test/snapshots/main.js.md`

The first file contains the actual snapshot and is required for future comparisons. The second file contains your *snapshot report*. It's regenerated when you update your snapshots. If you commit it to source control you can diff it to see the changes to your snapshot.

AVA will show why your snapshot assertion failed:

<img src="../media/snapshot-testing.png" width="1048">

You can then check your code. If the change was intentional you can use the `--update-snapshots` (or `-u`) flag to update the snapshots:

```console
$ ava --update-snapshots
```

If you need to update snapshots for only a particular test, you can use `--update-snapshots` together with e.g. `--match` or `.only()` to select the test.

You can specify a fixed location for storing the snapshot files in AVA's [`package.json` configuration](./06-configuration.md):

**`package.json`:**

```json
{
	"ava": {
		"snapshotDir": "custom-directory"
	}
}
```

The snapshot files will be saved in a directory structure that mirrors that of your test files.

If you are running AVA against precompiled test files, AVA will try and use source maps to determine the location of the original files. Snapshots will be stored next to these files, following the same rules as if AVA had executed the original files directly. This is great if you're writing your tests in TypeScript (see our [TypeScript recipe](./recipes/typescript.md)).

```

### File: docs\05-command-line.md
```md
# CLI

Translations: [Français](https://github.com/avajs/ava-docs/blob/main/fr_FR/docs/05-command-line.md)

```console
ava [<pattern>...]
ava debug [<pattern>...]
ava reset-cache

Commands:
  ava [<pattern>...]        Run tests                                  [default]
  ava debug [<pattern>...]  Activate Node.js inspector and run a single test
                            file
  ava reset-cache           Delete any temporary files and state kept by AVA,
                            then exit

Positionals:
  pattern  Select which test files to run. Leave empty if you want AVA to run
           all test files as per your configuration. Accepts glob patterns,
           directories that (recursively) contain test files, and file paths
           optionally suffixed with a colon and comma-separated numbers and/or
           ranges identifying the 1-based line(s) of specific tests to run
                                                                        [string]

Options:
      --version            Show version number                         [boolean]
      --color              Force color output                          [boolean]
      --config             Specific JavaScript file for AVA to read its config
                           from, instead of using package.json or ava.config.*
                           files
      --help               Show help                                   [boolean]
  -c, --concurrency        Max number of test files running at the same time
                           (default: CPU cores)                         [number]
      --fail-fast          Stop after first test failure               [boolean]
  -m, --match              Only run tests with matching title (can be repeated)
                                                                        [string]
      --no-worker-threads  Don't use worker threads                    [boolean]
      --node-arguments     Additional Node.js arguments for launching worker
                           processes (specify as a single string)       [string]
  -s, --serial             Run tests serially                          [boolean]
  -t, --tap                Generate TAP output                         [boolean]
  -T, --timeout            Set global timeout (milliseconds or human-readable,
                           e.g. 10s, 2m)                                [string]
  -u, --update-snapshots   Update snapshots                            [boolean]
  -v, --verbose            Enable verbose output (default)             [boolean]
  -w, --watch              Re-run tests when files change              [boolean]

Examples:
  ava
  ava test.js
  ava test.js:4,7-9
```

AVA searches for test files using the following patterns:

* `test.js`
* `src/test.js`
* `source/test.js`
* `**/test-*.js`
* `**/*.spec.js`
* `**/*.test.js`
* `**/test/**/*.js`
* `**/tests/**/*.js`
* `**/__tests__/**/*.js`

Files inside `node_modules` are *always* ignored. So are files starting with `_` or inside of directories that start with a single `_`. Additionally, files matching these patterns are ignored by default, unless different patterns are configured:

* `**/__tests__/**/__helper__/**/*`
* `**/__tests__/**/__helpers__/**/*`
* `**/__tests__/**/__fixture__/**/*`
* `**/__tests__/**/__fixtures__/**/*`
* `**/test/**/helper/**/*`
* `**/test/**/helpers/**/*`
* `**/test/**/fixture/**/*`
* `**/test/**/fixtures/**/*`
* `**/tests/**/helper/**/*`
* `**/tests/**/helpers/**/*`
* `**/tests/**/fixture/**/*`
* `**/tests/**/fixtures/**/*`

When using `npm test`, you can pass positional arguments directly `npm test test2.js`, but flags needs to be passed like `npm test -- --verbose`.

## Running tests with matching titles

[![Open in StackBlitz](https://developer.stackblitz.com/img/open_in_stackblitz.svg)](https://stackblitz.com/github/avajs/ava/tree/main/examples/matching-titles?file=test.js&terminal=test&view=editor)

The `--match` flag allows you to run just the tests that have a matching title. This is achieved with simple wildcard patterns. Patterns are case insensitive. See [`matcher`](https://github.com/sindresorhus/matcher) for more details.

Match titles ending with `foo`:

```console
npx ava --match='*foo'
```

Match titles starting with `foo`:

```console
npx ava --match='foo*'
```

Match titles containing `foo`:

```console
npx ava --match='*foo*'
```

Match titles that are *exactly* `foo` (albeit case insensitively):

```console
npx ava --match='foo'
```

Match titles not containing `foo`:

```console
npx ava --match='!*foo*'
```

Match titles starting with `foo` and ending with `bar`:

```console
npx ava --match='foo*bar'
```

Match titles starting with `foo` or ending with `bar`:

```console
npx ava --match='foo*' --match='*bar'
```

Note that a match pattern takes precedence over the `.only` modifier. Only tests with an explicit title are matched. Tests without titles or whose title is derived from the implementation function will be skipped when `--match` is used.

Here's what happens when you run AVA with a match pattern of `*oo*` and the following tests:

```js
test('foo will run', t => {
	t.pass();
});

test('moo will also run', t => {
	t.pass();
});

test.only('boo will run but not exclusively', t => {
	t.pass();
});
```

## Running tests at specific line numbers

[![Open in StackBlitz](https://developer.stackblitz.com/img/open_in_stackblitz.svg)](https://stackblitz.com/github/avajs/ava/tree/main/examples/specific-line-numbers?file=test.js&terminal=test&view=editor)

AVA lets you run tests exclusively by referring to their line numbers. Target a single line, a range of lines or both. You can select any line number of a test.

The format is a comma-separated list of `[X|Y-Z]` where `X`, `Y` and `Z` are integers between `1` and the last line number of the file.

This feature is only available from the command line.

### Running a single test

To only run a particular test in a file, append the line number of the test to the path or pattern passed to AVA.

Given the following test file:

`test.js`

```js
1: test('unicorn', t => {
2:   t.pass();
3: });
4:
5: test('rainbow', t => {
6:  t.fail();
7: });
```

Running `npx ava test.js:2` for would run the `unicorn` test. In fact you could use any line number between `1` and `3`.

### Running multiple tests

To run multiple tests, either target them one by one or select a range of line numbers. As line numbers are given per file, you can run multiple files with different line numbers for each file. If the same file is provided multiple times, line numbers are merged and only run once.

### Examples

Single line numbers:

```console
npx ava test.js:2,9
```

Range:

```console
npx ava test.js:4-7
```

Mix of single line number and range:

```console
npx ava test.js:4,9-12
```

Different files:

```console
npx ava test.js:3 test2.js:4,7-9
```

When running a file with and without line numbers, line numbers take precedence.

## Resetting AVA's cache

AVA maintains some temporary state. You can clear this state by running:

```console
npx ava reset-cache
```

This deletes all files in the `node_modules/.cache/ava` directory.

## Reporters

AVA uses a human readable reporter by default:

<img src="../media/verbose-reporter.png" width="294">

### TAP reporter

[![Open in StackBlitz](https://developer.stackblitz.com/img/open_in_stackblitz.svg)](https://stackblitz.com/github/avajs/ava/tree/main/examples/tap-reporter?file=test.js&terminal=test&view=editor)

AVA supports the TAP format and thus is compatible with [any TAP reporter](https://github.com/sindresorhus/awesome-tap#reporters). Use the `--tap` flag to enable TAP output.

```console
$ npx ava --tap | npx tap-nyan
```

<img src="../media/tap-reporter.png" width="420">

Please note that the TAP reporter is unavailable when using [watch mode](./recipes/watch-mode.md).

## Node arguments

The `--node-arguments` argument may be used to specify additional arguments for launching worker processes. These are combined with the `nodeArguments` configuration and any arguments passed to the `node` binary when starting AVA.

**Only pass trusted values.**

Specify the arguments as a single string:

```console
npx ava --node-arguments="--throw-deprecation --zero-fill-buffers"
```

**Only pass trusted values.**

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

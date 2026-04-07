---
id: create-react-app
type: knowledge
owner: OA_Triage
---
# create-react-app
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "private": true,
  "workspaces": [
    "packages/*",
    "docusaurus/website"
  ],
  "scripts": {
    "build": "cd packages/react-scripts && node bin/react-scripts.js build",
    "changelog": "lerna-changelog",
    "create-react-app": "node tasks/cra.js",
    "e2e": "tasks/e2e-simple.sh",
    "e2e:docker": "tasks/local-test.sh",
    "postinstall": "npm run build:prod -w react-error-overlay",
    "publish": "tasks/publish.sh",
    "start": "cd packages/react-scripts && node bin/react-scripts.js start",
    "screencast": "node ./tasks/screencast.js",
    "screencast:error": "svg-term --cast jyu19xGl88FQ3poMY8Hbmfw8y --out screencast-error.svg --window --at 12000 --no-cursor",
    "alex": "alex .",
    "test:integration": "jest test/integration",
    "test": "cd packages/react-scripts && node bin/react-scripts.js test",
    "eslint": "eslint .",
    "prettier": "prettier .",
    "format": "npm run prettier -- --write"
  },
  "devDependencies": {
    "@testing-library/jest-dom": "^5.15.1",
    "@testing-library/react": "^12.1.2",
    "@testing-library/user-event": "^13.5.0",
    "alex": "^8.2.0",
    "eslint": "^8.3.0",
    "execa": "^5.1.1",
    "fs-extra": "^10.0.0",
    "get-port": "^5.1.1",
    "globby": "^11.0.4",
    "husky": "^4.3.8",
    "jest": "^27.4.3",
    "lerna": "^4.0.0",
    "lerna-changelog": "^2.2.0",
    "lint-staged": "^12.1.2",
    "meow": "^9.0.0",
    "multimatch": "^5.0.0",
    "prettier": "^2.5.0",
    "puppeteer": "^12.0.1",
    "strip-ansi": "^6.0.1",
    "svg-term-cli": "^2.1.1",
    "tempy": "^1.0.1",
    "wait-for-localhost": "^3.3.0",
    "web-vitals": "^2.1.2"
  },
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  },
  "lint-staged": {
    "*.{js,json,yml,yaml,css,scss,ts,tsx,md}": [
      "prettier --write"
    ]
  }
}

```

### File: README.md
```md
## Create React App [![Build & Test](https://github.com/facebook/create-react-app/actions/workflows/build-and-test.yml/badge.svg?branch=main)](https://github.com/facebook/create-react-app/actions/workflows/build-and-test.yml) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-green.svg)](https://github.com/facebook/create-react-app/blob/main/CONTRIBUTING.md)

> [!CAUTION]
>
> ## Deprecated
>
> Create React App was one of the key tools for getting a React project up-and-running in 2017-2021, it is now in long-term stasis and we recommend that you migrate to one of React frameworks documented on [Start a New React Project](https://react.dev/learn/start-a-new-react-project).
>
> If you are following a tutorial to learn React, there is still value in continuing your tutorial, but we do not recommend starting production apps based on Create React App.

<img alt="Logo" align="right" src="https://create-react-app.dev/img/logo.svg" width="20%" />

Create React apps with no build configuration.

- [Creating an App](#creating-an-app) – How to create a new app.
- [User Guide](https://facebook.github.io/create-react-app/) – How to develop apps bootstrapped with Create React App.

Create React App works on macOS, Windows, and Linux.<br>
If something doesn’t work, please [file an issue](https://github.com/facebook/create-react-app/issues/new).<br>
If you have questions or need help, please ask in [GitHub Discussions](https://github.com/facebook/create-react-app/discussions).

## Quick Overview

```sh
npx create-react-app my-app
cd my-app
npm start
```

If you've previously installed `create-react-app` globally via `npm install -g create-react-app`, we recommend you uninstall the package using `npm uninstall -g create-react-app` or `yarn global remove create-react-app` to ensure that npx always uses the latest version.

_([npx](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b) comes with npm 5.2+ and higher, see [instructions for older npm versions](https://gist.github.com/gaearon/4064d3c23a77c74a3614c498a8bb1c5f))_

Then open [http://localhost:3000/](http://localhost:3000/) to see your app.<br>
When you’re ready to deploy to production, create a minified bundle with `npm run build`.

<p align='center'>
<img src='https://cdn.jsdelivr.net/gh/facebook/create-react-app@27b42ac7efa018f2541153ab30d63180f5fa39e0/screencast.svg' width='600' alt='npm start'>
</p>

### Get Started Immediately

You **don’t** need to install or configure tools like webpack or Babel.<br>
They are preconfigured and hidden so that you can focus on the code.

Create a project, and you’re good to go.

## Creating an App

**You’ll need to have Node 14.0.0 or later version on your local development machine** (but it’s not required on the server). We recommend using the latest LTS version. You can use [nvm](https://github.com/creationix/nvm#installation) (macOS/Linux) or [nvm-windows](https://github.com/coreybutler/nvm-windows#node-version-manager-nvm-for-windows) to switch Node versions between different projects.

To create a new app, you may choose one of the following methods:

### npx

```sh
npx create-react-app my-app
```

_([npx](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b) is a package runner tool that comes with npm 5.2+ and higher, see [instructions for older npm versions](https://gist.github.com/gaearon/4064d3c23a77c74a3614c498a8bb1c5f))_

### npm

```sh
npm init react-app my-app
```

_`npm init <initializer>` is available in npm 6+_

### Yarn

```sh
yarn create react-app my-app
```

_[`yarn create <starter-kit-package>`](https://yarnpkg.com/lang/en/docs/cli/create/) is available in Yarn 0.25+_

It will create a directory called `my-app` inside the current folder.<br>
Inside that directory, it will generate the initial project structure and install the transitive dependencies:

```
my-app
├── README.md
├── node_modules
├── package.json
├── .gitignore
├── public
│   ├── favicon.ico
│   ├── index.html
│   └── manifest.json
└── src
    ├── App.css
    ├── App.js
    ├── App.test.js
    ├── index.css
    ├── index.js
    ├── logo.svg
    └── serviceWorker.js
    └── setupTests.js
```

No configuration or complicated folder structures, only the files you need to build your app.<br>
Once the installation is done, you can open your project folder:

```sh
cd my-app
```

Inside the newly created project, you can run some built-in commands:

### `npm start` or `yarn start`

Runs the app in development mode.<br>
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will automatically reload if you make changes to the code.<br>
You will see the build errors and lint warnings in the console.

<p align='center'>
<img src='https://cdn.jsdelivr.net/gh/marionebl/create-react-app@9f6282671c54f0874afd37a72f6689727b562498/screencast-error.svg' width='600' alt='Build errors'>
</p>

### `npm test` or `yarn test`

Runs the test watcher in an interactive mode.<br>
By default, runs tests related to files changed since the last commit.

[Read more about testing.](https://facebook.github.io/create-react-app/docs/running-tests)

### `npm run build` or `yarn build`

Builds the app for production to the `build` folder.<br>
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br>

Your app is ready to be deployed.

## User Guide

You can find detailed instructions on using Create React App and many tips in [its documentation](https://facebook.github.io/create-react-app/).

## How to Update to New Versions?

Please refer to the [User Guide](https://facebook.github.io/create-react-app/docs/updating-to-new-releases) for this and other information.

## Philosophy

- **One Dependency:** There is only one build dependency. It uses webpack, Babel, ESLint, and other amazing projects, but provides a cohesive curated experience on top of them.

- **No Configuration Required:** You don't need to configure anything. A reasonably good configuration of both development and production builds is handled for you so you can focus on writing code.

- **No Lock-In:** You can “eject” to a custom setup at any time. Run a single command, and all the configuration and build dependencies will be moved directly into your project, so you can pick up right where you left off.

## What’s Included?

Your environment will have everything you need to build a modern single-page React app:

- React, JSX, ES6, TypeScript and Flow syntax support.
- Language extras beyond ES6 like the object spread operator.
- Autoprefixed CSS, so you don’t need `-webkit-` or other prefixes.
- A fast interactive unit test runner with built-in support for coverage reporting.
- A live development server that warns about common mistakes.
- A build script to bundle JS, CSS, and images for production, with hashes and sourcemaps.
- An offline-first [service worker](https://developers.google.com/web/fundamentals/getting-started/primers/service-workers) and a [web app manifest](https://developers.google.com/web/fundamentals/engage-and-retain/web-app-manifest/), meeting all the [Progressive Web App](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app) criteria. (_Note: Using the service worker is opt-in as of `react-scripts@2.0.0` and higher_)
- Hassle-free updates for the above tools with a single dependency.

Check out [this guide](https://github.com/nitishdayal/cra_closer_look) for an overview of how these tools fit together.

The tradeoff is that **these tools are preconfigured to work in a specific way**. If your project needs more customization, you can ["eject"](https://facebook.github.io/create-react-app/docs/available-scripts#npm-run-eject) and customize it, but then you will need to maintain this configuration.

## Popular Alternatives

Create React App is a great fit for:

- **Learning React** in a comfortable and feature-rich development environment.
- **Starting new single-page React applications.**
- **Creating examples** with React for your libraries and components.

Here are a few common cases where you might want to try something else:

- If you want to **try React** without hundreds of transitive build tool dependencies, consider [using a single HTML file or an online sandbox instead](https://reactjs.org/docs/getting-started.html#try-react).

- If you need to **integrate React code with a server-side template framework** like Rails, Django or Symfony, or if you’re **not building a single-page app**, consider using [nwb](https://github.com/insin/nwb), or [Neutrino](https://neutrino.js.org/) which are more flexible. For Rails specifically, you can use [Rails Webpacker](https://github.com/rails/webpacker). For Symfony, try [Symfony's webpack Encore](https://symfony.com/doc/current/frontend/encore/reactjs.html).

- If you need to **publish a React component**, [nwb](https://github.com/insin/nwb) can [also do this](https://github.com/insin/nwb#react-components-and-libraries), as well as [Neutrino's react-components preset](https://neutrino.js.org/packages/react-components/).

- If you want to do **server rendering** with React and Node.js, check out [Next.js](https://nextjs.org/) or [Razzle](https://github.com/jaredpalmer/razzle). Create React App is agnostic of the backend, and only produces static HTML/JS/CSS bundles.

- If your website is **mostly static** (for example, a portfolio or a blog), consider using [Gatsby](https://www.gatsbyjs.org/) or [Next.js](https://nextjs.org/). Unlike Create React App, Gatsby pre-renders the website into HTML at build time. Next.js supports both server rendering and pre-rendering.

- Finally, if you need **more customization**, check out [Neutrino](https://neutrino.js.org/) and its [React preset](https://neutrino.js.org/packages/react/).

All of the above tools can work with little to no configuration.

If you prefer configuring the build yourself, [follow this guide](https://reactjs.org/docs/add-react-to-a-website.html).

## React Native

Looking for something similar, but for React Native?<br>
Check out [Expo CLI](https://github.com/expo/expo-cli).

## Contributing

We'd love to have your helping hand on `create-react-app`! See [CONTRIBUTING.md](CONTRIBUTING.md) for more information on what we're looking for and how to get started.

## Supporting Create React App

Create React App is a community maintained project and all contributors are volunteers. If you'd like to support the future development of Create React App then please consider donating to our [Open Collective](https://opencollective.com/create-react-app).

## Credits

This project exists thanks to all the people who [contribute](CONTRIBUTING.md).<br>
<a href="https://github.com/facebook/create-react-app/graphs/contributors"><img src="https://opencollective.com/create-react-app/contributors.svg?width=890&button=false" /></a>

Thanks to [Netlify](https://www.netlify.com/) for hosting our documentation.

## Acknowledgements

We are grateful to the authors of existing related projects for their ideas and collaboration:

- [@eanplatter](https://github.com/eanplatter)
- [@insin](https://github.com/insin)
- [@mxstbr](https://github.com/mxstbr)

## License

Create React App is open source software [licensed as MIT](https://github.com/facebook/create-react-app/blob/main/LICENSE). The Create React App logo is licensed under a [Creative Commons Attribution 4.0 International license](https://creativecommons.org/licenses/by/4.0/).

```

### File: test\README.md
```md
# Create React App End-to-End Tests

## Usage

These tests ensure various functionality contracts are upheld across dependency upgrades.

To get started locally, run `npx jest test/ --watchAll`.

It's suggested that you filter down tests to avoid re-running everything. The most common tests will be the webpack messages.<br>
To only run the webpack messages, type `p` followed by `webpack-message` and press `[enter]`.

## How do these work?

### `fixtures/`

Each `fixture/` gets spun up in a temporary directory and has its dependencies installed with Yarn PnP (for speed).<br>
To opt-out of PnP, create a `.disable-pnp` file in the specific fixture directory.

A global (`testSetup`) is created which has a few interesting properties:

- `testSetup.testDirectory`: the directory containing the test application
- `testSetup.scripts`: an object allowing you to invoke `react-scripts` commands and friends

All tests for each `fixture/` are then ran.

#### `testSetup.scripts`

##### `start`

This will run the `start` command, it can be ran asynchronously or blocking if `{ smoke: true }` is used.<br>
If ran asynchronously, it will return the `port` and a `done` function to clean up the process.
If ran blocking, it will return the `stdout` and `stderr` of the process.

##### `build`

This will run the `build` command and return the `stdout` and `stderr` of the process.

##### `test`

This will run the `test` command and return the `stdout` and `stderr` of the process.

##### `serve`

This will run serve the application.
It will return the `port` and a `done` function to clean up the process.

```

### File: .eslintrc.json
```json
{
  "extends": "eslint:recommended",
  "env": {
    "browser": true,
    "commonjs": true,
    "node": true,
    "es6": true,
    "jest": true
  },
  "parserOptions": {
    "ecmaVersion": 2018
  },
  "rules": {
    "no-console": "off",
    "strict": ["error", "global"],
    "curly": "warn"
  },
  "overrides": [
    {
      "files": [
        "docusaurus/website/src/**/*.js",
        "packages/cra-template/**/*.js",
        "packages/react-error-overlay/**/*.js",
        "packages/react-scripts/fixtures/kitchensink/template/{src,integration}/**/*.js",
        "test/fixtures/*/src/*.js"
      ],
      "excludedFiles": ["packages/react-error-overlay/*.js"],
      "extends": ["react-app", "react-app/jest"]
    },
    {
      "files": [
        "test/fixtures/webpack-message-formatting/src/{AppLintError,AppLintWarning,AppUnknownFile}.js"
      ],
      "rules": {
        "no-unused-vars": "off",
        "no-undef": "off"
      }
    },
    {
      "files": ["test/fixtures/webpack-message-formatting/src/Export5.js"],
      "rules": {
        "import/no-anonymous-default-export": "off"
      }
    },
    {
      "files": ["test/fixtures/issue-5176-flow-class-properties/src/App.js"],
      "rules": {
        "no-dupe-class-members": "off"
      }
    }
  ]
}

```

### File: CHANGELOG-0.x.md
```md
## 1.0.0 and Newer Versions

**Please refer to [CHANGELOG-1.x.md](./CHANGELOG-1.x.md) for the 1.x range, and [CHANGELOG.md](CHANGELOG.md) for the newer versions.**

## 0.9.5 (March 9, 2017)

#### :bug: Bug Fix

- `react-scripts`

  - [#1783](https://github.com/facebook/create-react-app/pull/1783) **Work around Node 7.7.2 bug that crashes `npm start`.** ([@ryanwalters](https://github.com/ryanwalters))

#### :nail_care: Enhancement

- `eslint-config-react-app`

  - [#1773](https://github.com/facebook/create-react-app/pull/1773) Remove `guard-for-in` lint rule. ([@spicyj](https://github.com/spicyj))

- `react-scripts`
  - [#1760](https://github.com/facebook/create-react-app/pull/1760) Suggest `serve` for running in production. ([@leo](https://github.com/leo))
  - [#1747](https://github.com/facebook/create-react-app/pull/1747) Display `yarn` instead of `yarnpkg` when creating a new app. ([@lpalmes](https://github.com/lpalmes))

#### :memo: Documentation

- `react-scripts`

  - [#1756](https://github.com/facebook/create-react-app/pull/1756) Add Yarn steps for adding Flow. ([@zertosh](https://github.com/zertosh))

#### :house: Internal

- `babel-preset-react-app`

  - [#1742](https://github.com/facebook/create-react-app/pull/1742) Switch to `babel-preset-env` to remove the deprecation warning. ([@Timer](https://github.com/Timer))

#### Committers: 6

- Andres Suarez ([zertosh](https://github.com/zertosh))
- Ben Alpert ([spicyj](https://github.com/spicyj))
- Joe Haddad ([Timer](https://github.com/Timer))
- Leo Lamprecht ([leo](https://github.com/leo))
- Lorenzo Palmes ([lpalmes](https://github.com/lpalmes))
- Ryan Walters ([ryanwalters](https://github.com/ryanwalters))

### Migrating from 0.9.4 to 0.9.5

Inside any created project that has not been ejected, run:

```sh
npm install --save-dev --save-exact react-scripts@0.9.5
```

## 0.9.4 (March 6, 2017)

#### :bug: Bug Fix

- `create-react-app`

  - [#1706](https://github.com/facebook/create-react-app/pull/1706) Extract compressed package for package name. ([@Timer](https://github.com/Timer))

    You may now specify a scoped package for `--scripts-version` and obtain a working installation.

  - [#1695](https://github.com/facebook/create-react-app/pull/1695) Print why installation was aborted. ([@tgig](https://github.com/tgig))

- `react-scripts`

  - [#1727](https://github.com/facebook/create-react-app/pull/1727) Fix ejecting from a scoped fork. ([@gaearon](https://github.com/gaearon))

    Ejecting now works within a scoped fork.

  - [#1721](https://github.com/facebook/create-react-app/pull/1721) Fix hot reloading for WebpackDevServer after eject. ([@gaearon](https://github.com/gaearon))

- `react-dev-utils`

  - [#1690](https://github.com/facebook/create-react-app/pull/1690) Fix `openBrowser()` when `BROWSER=open` on macOS. ([@bpierre](https://github.com/bpierre))

  - [#1696](https://github.com/facebook/create-react-app/pull/1696) Improve reliability of port detection. ([@chrisdrackett](https://github.com/chrisdrackett))

#### :nail_care: Enhancement

- `eslint-config-react-app`, `react-scripts`

  - [#1705](https://github.com/facebook/create-react-app/pull/1705) Add support for `ignoreRestSiblings` in `no-unused-vars`. ([@chrisdrackett](https://github.com/chrisdrackett))

    Linter no longer warns when using rest properties to remove variables from an object.

  - [#1542](https://github.com/facebook/create-react-app/pull/1542) Bump `jsx-a11y` version. ([@bondz](https://github.com/bondz))

- `react-dev-utils`, `react-scripts`

  - [#1726](https://github.com/facebook/create-react-app/pull/1726) Extract generic build functions into `react-dev-utils`. ([@viankakrisna](https://github.com/viankakrisna))

- Other

  - [#1402](https://github.com/facebook/create-react-app/pull/1402) Stub `package.json` for e2e test. ([@matoilic](https://github.com/matoilic))

#### :memo: Documentation

- `react-scripts`
  - [#1710](https://github.com/facebook/create-react-app/pull/1710) Update now.sh deployment instructions. ([@replaid](https://github.com/replaid))
  - [#1717](https://github.com/facebook/create-react-app/pull/1717) Add docs for Apache client side routing. ([@viankakrisna](https://github.com/viankakrisna))
  - [#1698](https://github.com/facebook/create-react-app/pull/1698) Suggest to use `.env` for enabling polling mode. ([@gaearon](https://github.com/gaearon))
  - [#1687](https://github.com/facebook/create-react-app/pull/1687) Fixed missing `--recursive` flag in first `npm run watch-css` command. ([@mklemme](https://github.com/mklemme))

#### :house: Internal

- `react-scripts`
  - [#1736](https://github.com/facebook/create-react-app/pull/1736) Fix eject for linked react-scripts. ([@tuchk4](https://github.com/tuchk4))
  - [#1741](https://github.com/facebook/create-react-app/pull/1741) Fix internal linting setup. ([@gaearon](https://github.com/gaearon))
  - [#1730](https://github.com/facebook/create-react-app/pull/1730) Fix Node 4 e2e tests. ([@Timer](https://github.com/Timer))
- `eslint-config-react-app`
  - [#1740](https://github.com/facebook/create-react-app/pull/1740) Relax ESLint config peerDependency. ([@gaearon](https://github.com/gaearon))
- `eslint-config-react-app`, `react-dev-utils`, `react-scripts`
  - [#1729](https://github.com/facebook/create-react-app/pull/1729) Lint internal scripts with `eslint:recommended`. ([@gaearon](https://github.com/gaearon))
- `react-dev-utils`
  - [#1724](https://github.com/facebook/create-react-app/pull/1724) Don't use ES6 in a file that should run on Node 4. ([@gaearon](https://github.com/gaearon))
- Other
  - [#1723](https://github.com/facebook/create-react-app/pull/1723) Skip AppVeyor CI builds for Markdown changes. ([@gaearon](https://github.com/gaearon))
  - [#1707](https://github.com/facebook/create-react-app/pull/1707) Add double quotes to escape spaces in paths in e2e. ([@viankakrisna](https://github.com/viankakrisna))
  - [#1688](https://github.com/facebook/create-react-app/pull/1688) Upgrade `lerna` version. ([@viankakrisna](https://github.com/viankakrisna))

#### Committers: 11

- Ade Viankakrisna Fadlil ([viankakrisna](https://github.com/viankakrisna))
- Bond ([bondz](https://github.com/bondz))
- Chris Drackett ([chrisdrackett](https://github.com/chrisdrackett))
- Dan Abramov ([gaearon](https://github.com/gaearon))
- Joe Haddad ([Timer](https://github.com/Timer))
- Mato Ilic ([matoilic](https://github.com/matoilic))
- Myk Klemme ([mklemme](https://github.com/mklemme))
- Pierre Bertet ([bpierre](https://github.com/bpierre))
- Ryan Platte ([replaid](https://github.com/replaid))
- Travis Giggy ([tgig](https://github.com/tgig))
- Valerii Sorokobatko ([tuchk4](https://github.com/tuchk4))

### Migrating from 0.9.3 to 0.9.4

Inside any created project that has not been ejected, run:

```sh
npm install --save-dev --save-exact react-scripts@0.9.4
```

You may also optionally update the global command-line utility for scoped package support:

```sh
npm install -g create-react-app@1.3.0
```

## 0.9.3 (February 28, 2017)

#### :rocket: New Feature

- `create-react-app`

  - [#1423](https://github.com/facebook/create-react-app/pull/1423) **Fall back to Yarn offline cache when creating a new project.** ([@voxsim](https://github.com/voxsim))

  If you are using Yarn, and you have created at least one app previously, Create React App now works offline.

  <img src="https://i.imgur.com/1FLa9Tg.gif" width="500" alt="Yarn offline installation demo">

#### :bug: Bug Fix

- `react-scripts`

  - [#1665](https://github.com/facebook/create-react-app/pull/1665) Temporarily disable ESLint caching because of a bug. ([@gaearon](https://github.com/gaearon))

- `create-react-app`
  - [#1675](https://github.com/facebook/create-react-app/pull/1675) Delete project folder on failed installation on Windows. ([@johann-sonntagbauer](https://github.com/johann-sonntagbauer))
  - [#1662](https://github.com/facebook/create-react-app/pull/1662) Validate project name before creating a project. ([@johann-sonntagbauer](https://github.com/johann-sonntagbauer))
  - [#1669](https://github.com/facebook/create-react-app/pull/1669) Make sure React dependencies aren’t pinned in new projects. ([@johann-sonntagbauer](https://github.com/johann-sonntagbauer))

#### :nail_care: Enhancement

- `react-scripts`

  - [#1677](https://github.com/facebook/create-react-app/pull/1677) Add `X-FORWARDED` headers for proxy requests. ([@johann-sonntagbauer](https://github.com/johann-sonntagbauer))

#### :memo: Documentation

- `react-scripts`

  - [#1657](https://github.com/facebook/create-react-app/pull/1657) Tweak the Visual Studio Code debugging guide. ([@ryansully](https://github.com/ryansully))

#### :house: Internal

- End-to-end Tests

  - [#1648](https://github.com/facebook/create-react-app/pull/1648) Add Windows CI tests for better stability. ([@Timer](https://github.com/Timer))

#### Committers: 5

- Dan Abramov ([gaearon](https://github.com/gaearon))
- Joe Haddad ([Timer](https://github.com/Timer))
- Johann Hubert Sonntagbauer ([johann-sonntagbauer](https://github.com/johann-sonntagbauer))
- Ryan Sullivan ([ryansully](https://github.com/ryansully))
- Simon Vocella ([voxsim](https://github.com/voxsim))

### Migrating from 0.9.2 to 0.9.3

Inside any created project that has not been ejected, run:

```sh
npm install --save-dev --save-exact react-scripts@0.9.3
```

You may also optionally update the global command-line utility for offline Yarn cache support:

```sh
npm install -g create-react-app@1.2.1
```

## 0.9.2 (February 26, 2017)

#### :nail_care: Enhancement

- `create-react-app`

  - [#1253](https://github.com/facebook/create-react-app/pull/1253) **Install time optimization.** ([@n3tr](https://github.com/n3tr))

    React, ReactDOM, and `react-scripts` are now installed in the same install instead of two different installs. This reduces app creation time by a noticeable amount.

  - [#1512](https://github.com/facebook/create-react-app/pull/1512) **Graceful error handling.** ([@chitchu](https://github.com/chitchu))

    If an error occurs while `create-react-app` is running, it will now clean up and not leave a broken project to reduce confusion.

  - [#1193](https://github.com/facebook/create-react-app/pull/1193) Suggest upgrading to NPM >= 3 for faster install times. ([@mobinni](https://github.com/mobinni))

  - [#1603](https://github.com/facebook/create-react-app/pull/1603) Allow app creation in a WebStorm project. ([@driquelme](https://github.com/driquelme))

  - [#1570](https://github.com/facebook/create-react-app/pull/1570) Allow git urls in `--scripts-version`. ([@tomconroy](https://github.com/tomconroy))

- `react-scripts`

  - [#1578](https://github.com/facebook/create-react-app/pull/1578) Enable lint caching in development. ([@viankakrisna](https://github.com/viankakrisna))

  - [#1478](https://github.com/facebook/create-react-app/pull/1478) Update the build script message to show the correct port. ([@chyipin](https://github.com/chyipin))

  - [#1567](https://github.com/facebook/create-react-app/pull/1567) Remove .bin files after eject. ([@tuchk4](https://github.com/tuchk4))

  - [#1560](https://github.com/facebook/create-react-app/pull/1560) Bump `recursive-readdir`. ([@wtgtybhertgeghgtwtg](https://github.com/wtgtybhertgeghgtwtg))

#### :bug: Bug Fix

- `react-scripts`

  - [#1635](https://github.com/facebook/create-react-app/pull/1635) **Fix Jest configuration.** ([@Timer](https://github.com/Timer))

    Fixes ejecting on Windows for macOS and Linux machines.

  - [#1356](https://github.com/facebook/create-react-app/pull/1356) Fix workflow if react-scripts package is linked via npm-link. ([@tuchk4](https://github.com/tuchk4))

    Advanced users may opt to fork `react-scripts` instead of ejecting so they still receive upstream updates.<br>
    `react-scripts` will now function as expected when linking to a development version.<br>
    Previously, you could not test changes with an existing application via linking.

  - [#1585](https://github.com/facebook/create-react-app/pull/1585) Ensure PORT environment variable is an integer. ([@matoilic](https://github.com/matoilic))

  - [#1628](https://github.com/facebook/create-react-app/pull/1628) Show correct port for pushstate-server URL text. ([@mattccrampton](https://github.com/mattccrampton))

  - [#1647](https://github.com/facebook/create-react-app/pull/1647) Fix `npm test` on Windows ([@gaearon](https://github.com/gaearon))

#### :memo: Documentation

- User Guides
  - [#1391](https://github.com/facebook/create-react-app/pull/1391) Add note how to resolve missing required files for Heroku. ([@sbritoig](https://github.com/sbritoig))
  - [#1577](https://github.com/facebook/create-react-app/pull/1577) Add a how-to on `react-snapshot`. ([@superhighfives](https://github.com/superhighfives))
  - [#1121](https://github.com/facebook/create-react-app/pull/1121) Add documentation for customizing Bootstrap theme. ([@myappincome](https://github.com/myappincome))
  - [#1540](https://github.com/facebook/create-react-app/pull/1540) Document debugging in Visual Studio Code. ([@bondz](https://github.com/bondz))
  - [#1618](https://github.com/facebook/create-react-app/pull/1618) Add note about when to import Bootstrap CSS. ([@joewoodhouse](https://github.com/joewoodhouse))
  - [#1518](https://github.com/facebook/create-react-app/pull/1518) Update flow configuration documentation. ([@SBrown52](https://github.com/SBrown52))
  - [#1625](https://github.com/facebook/create-react-app/pull/1625) Specify that NODE_ENV is set to 'production' during the build step. ([@mderazon](https://github.com/mderazon))
  - [#1573](https://github.com/facebook/create-react-app/pull/1573) Update Jest documentation links. ([@mkermani144](https://github.com/mkermani144))
  - [#1564](https://github.com/facebook/create-react-app/pull/1564) Add --recursive to Sass watch script. ([@aleburato](https://github.com/aleburato))
  - [#1561](https://github.com/facebook/create-react-app/pull/1561) Use https in link in documentation. ([@dariocravero](https://github.com/dariocravero))
  - [#1562](https://github.com/facebook/create-react-app/pull/1562) Update `jest-enzyme` documentation. ([@kiranps](https://github.com/kiranps))
  - [#1543](https://github.com/facebook/create-react-app/pull/1543) Update CSS preprocessor instructions. ([@aleburato](https://github.com/aleburato))
  - [#1338](https://github.com/facebook/create-react-app/pull/1338) Add link to Azure deployment tutorial. ([@tpetrina](https://github.com/tpetrina))
  - [#1320](https://github.com/facebook/create-react-app/pull/1320) Document how to disable autoprefix feature. ([@rrubas](https://github.com/rrubas))
  - [#1313](https://github.com/facebook/create-react-app/pull/1313) List features beyond ES6 supported by create-react-app. ([@jonathanconway](https://github.com/jonathanconway))
  - [#1008](https://github.com/facebook/create-react-app/pull/1008) Add Saas support documentation. ([@tsironis](https://gith
... [TRUNCATED]
```

### File: CHANGELOG-1.x.md
```md
## 2.0.3 and Newer Versions

**Please refer to [CHANGELOG-2.x.md](./CHANGELOG-2.x.md) for the 2.x range, and [CHANGELOG.md](CHANGELOG.md) for the newer versions.**

## 1.1.5 (August 24, 2018)

- `react-scripts`

  - Update the `webpack-dev-server` dependency

- `react-dev-utils`

  - [#4866](https://github.com/facebook/create-react-app/pull/4866) Fix a Windows-only vulnerability (`CVE-2018-6342`) in the development server ([@acdlite](https://github.com/acdlite))
  - Update the `sockjs-client` dependency

#### Committers: 1

- Andrew Clark ([acdlite](https://github.com/acdlite))

### Migrating from 1.1.4 to 1.1.5

Inside any created project that has not been ejected, run:

```sh
npm install --save --save-exact react-scripts@1.1.5
```

or

```sh
yarn add --exact react-scripts@1.1.5
```

## 1.1.4 (April 3, 2018)

#### :bug: Bug Fix

- `react-dev-utils`

  - [#4250](https://github.com/facebook/create-react-app/pull/4250) Upgrade `detect-port-alt` to fix [#4189](https://github.com/facebook/create-react-app/issues/4189). ([@Timer](https://github.com/Timer))

#### Committers: 1

- Joe Haddad ([Timer](https://github.com/Timer))

### Migrating from 1.1.3 to 1.1.4

Inside any created project that has not been ejected, run:

```sh
npm install --save --save-exact react-scripts@1.1.4
```

or

```sh
yarn add --exact react-scripts@1.1.4
```

## 1.1.3 (April 3, 2018)

#### :bug: Bug Fix

- `react-scripts`

  - [#4247](https://github.com/facebook/create-react-app/pull/4247) Fix `environment.dispose is not a function` error caused by a Jest bug. ([@gaearon](https://github.com/gaearon))

#### Committers: 1

- Dan Abramov ([gaearon](https://github.com/gaearon))

### Migrating from 1.1.2 to 1.1.3

Inside any created project that has not been ejected, run:

```sh
npm install --save --save-exact react-scripts@1.1.3
```

or

```sh
yarn add --exact react-scripts@1.1.3
```

## 1.1.2 (April 3, 2018)

#### :bug: Bug Fix

- `react-scripts`

  - [#4085](https://github.com/facebook/create-react-app/pull/4085) Resolve `.js` before `.mjs` files to unbreak dependencies with native ESM support. ([@leebyron](https://github.com/leebyron))

#### :memo: Documentation

- `react-scripts`

  - [#4197](https://github.com/facebook/create-react-app/pull/4197) Add troubleshooting for Github Pages. ([@xnt](https://github.com/xnt))

#### Committers: 2

- Lee Byron ([leebyron](https://github.com/leebyron))
- Vicente Plata ([xnt](https://github.com/xnt))

### Migrating from 1.1.1 to 1.1.2

Inside any created project that has not been ejected, run:

```sh
npm install --save --save-exact react-scripts@1.1.2
```

or

```sh
yarn add --exact react-scripts@1.1.2
```

## 1.1.1 (February 2, 2018)

#### :bug: Bug Fix

- `react-scripts`
  - [#4000](https://github.com/facebook/create-react-app/pull/4000) Fix escaping `$` in environment variables. ([@iansu](https://github.com/iansu))

#### :nail_care: Enhancement

- `react-scripts`
  - [#4006](https://github.com/facebook/create-react-app/pull/4006) Add Node 9 compatibility for `fsevents`. ([@gaearon](https://github.com/gaearon))

#### :memo: Documentation

- `react-scripts`
  - [#3971](https://github.com/facebook/create-react-app/pull/3971) Update instructions for continuous delivery with Netlify. ([@hubgit](https://github.com/hubgit))
  - [#3894](https://github.com/facebook/create-react-app/pull/3894) Include `{json,css}` files in prettier command. ([@reyronald](https://github.com/reyronald))

#### :house: Internal

- `create-react-app`
  - [#3853](https://github.com/facebook/create-react-app/pull/3853) pin envinfo version to 3.4.2. ([@bondz](https://github.com/bondz))

#### Committers: 6

- Alf Eaton ([hubgit](https://github.com/hubgit))
- Bond ([bondz](https://github.com/bondz))
- Dan Abramov ([gaearon](https://github.com/gaearon))
- Ian Sutherland ([iansu](https://github.com/iansu))
- Ronald Rey ([reyronald](https://github.com/reyronald))

### Migrating from 1.1.0 to 1.1.1

Inside any created project that has not been ejected, run:

```sh
npm install --save --save-exact react-scripts@1.1.1
```

or

```sh
yarn add --exact react-scripts@1.1.1
```

## 1.1.0 (January 15, 2018)

#### :rocket: New Feature

- `react-scripts`

  - [#3387](https://github.com/facebook/create-react-app/pull/3387) Add support for variable expansion in `.env` files. ([@moos](https://github.com/moos))

- `react-error-overlay`

  - [#3474](https://github.com/facebook/create-react-app/pull/3474) Allow the error overlay to be unregistered. ([@Timer](https://github.com/Timer))

- `create-react-app`

  - [#3408](https://github.com/facebook/create-react-app/pull/3408) Add `--info` flag to help gather bug reports. ([@tabrindle](https://github.com/tabrindle))
  - [#3409](https://github.com/facebook/create-react-app/pull/3409) Add `--use-npm` flag to bypass Yarn even on systems that have it. ([@tabrindle](https://github.com/tabrindle))
  - [#3725](https://github.com/facebook/create-react-app/pull/3725) Extend `--scripts-version` to include `.tar.gz` format. ([@SaschaDens](https://github.com/SaschaDens))
  - [#3629](https://github.com/facebook/create-react-app/pull/3629) Allowing `"file:<path>"` `--scripts-version` values. ([@GreenGremlin](https://github.com/GreenGremlin))

#### :bug: Bug Fix

- `babel-preset-react-app`, `react-scripts`

  - [#3788](https://github.com/facebook/create-react-app/pull/3788) Fix object destructuring inside an array on Node 6. ([@gaearon](https://github.com/gaearon))

- `react-dev-utils`

  - [#3784](https://github.com/facebook/create-react-app/pull/3784) Detach browser process from the shell on Linux. ([@gaearon](https://github.com/gaearon))
  - [#3726](https://github.com/facebook/create-react-app/pull/3726) Use proxy for all request methods other than `GET`. ([@doshisid](https://github.com/doshisid))
  - [#3440](https://github.com/facebook/create-react-app/pull/3440) Print full directory name from `lsof`. ([@rmccue](https://github.com/rmccue))
  - [#2071](https://github.com/facebook/create-react-app/pull/2071) Fix broken console clearing on Windows. ([@danielverejan](https://github.com/danielverejan))
  - [#3686](https://github.com/facebook/create-react-app/pull/3686) Fix starting a project in directory with `++` in the name. ([@Norris1z](https://github.com/Norris1z))

- `create-react-app`

  - [#3320](https://github.com/facebook/create-react-app/pull/3320) Fix offline installation to respect proxy from `.npmrc`. ([@mdogadailo](https://github.com/mdogadailo))

- `react-scripts`

  - [#3537](https://github.com/facebook/create-react-app/pull/3537) Add `mjs` and `jsx` filename extensions to `file-loader` exclude pattern. ([@iansu](https://github.com/iansu))
  - [#3511](https://github.com/facebook/create-react-app/pull/3511) Unmount the component in the default generated test. ([@gaearon](https://github.com/gaearon))

#### :nail_care: Enhancement

- `react-scripts`

  - [#3730](https://github.com/facebook/create-react-app/pull/3730) Print when `HOST` environment variable is set. ([@iansu](https://github.com/iansu))
  - [#3455](https://github.com/facebook/create-react-app/pull/3455) Add a localhost-only log message pointing folks to the PWA docs. ([@jeffposnick](https://github.com/jeffposnick))
  - [#3416](https://github.com/facebook/create-react-app/pull/3416) Improve eject message. ([@xjlim](https://github.com/xjlim))

- `create-react-app`

  - [#3740](https://github.com/facebook/create-react-app/pull/3740) Allow more non-conflicting files in initial project directory. ([@GreenGremlin](https://github.com/GreenGremlin))

- `react-dev-utils`

  - [#3104](https://github.com/facebook/create-react-app/pull/3104) Add link to deployment docs after build. ([@viankakrisna](https://github.com/viankakrisna))
  - [#3652](https://github.com/facebook/create-react-app/pull/3652) Add `code-insiders` to the editor list. ([@shrynx](https://github.com/shrynx))
  - [#3700](https://github.com/facebook/create-react-app/pull/3700) Add editor support for Sublime Dev & VSCode Insiders. ([@yyx990803](https://github.com/yyx990803))
  - [#3545](https://github.com/facebook/create-react-app/pull/3545) Autodetect MacVim editor. ([@gnapse](https://github.com/gnapse))

- `react-dev-utils`, `react-error-overlay`

  - [#3465](https://github.com/facebook/create-react-app/pull/3465) Open editor to exact column from build error overlay. ([@tharakawj](https://github.com/tharakawj))

- `react-dev-utils`, `react-scripts`

  - [#3721](https://github.com/facebook/create-react-app/pull/3721) Support setting `none` in `REACT_EDITOR` environment variable. ([@raerpo](https://github.com/raerpo))

- `eslint-config-react-app`

  - [#3716](https://github.com/facebook/create-react-app/pull/3716) Relax `no-cond-assign` rule. ([@gaearon](https://github.com/gaearon))

#### :memo: Documentation

- User Guide

  - [#3659](https://github.com/facebook/create-react-app/pull/3659) Add info about service-worker and HTTP caching headers into Firebase section. ([@bobrosoft](https://github.com/bobrosoft))
  - [#3515](https://github.com/facebook/create-react-app/pull/3515) Add Powershell commands to README.md. ([@Gua-naiko-che](https://github.com/Gua-naiko-che))
  - [#3656](https://github.com/facebook/create-react-app/pull/3656) Better documentation for setupTests.js when ejecting. ([@dannycalleri](https://github.com/dannycalleri))
  - [#1791](https://github.com/facebook/create-react-app/pull/1791) Add link for automatic deployment to azure. ([@ulrikstrid](https://github.com/ulrikstrid))
  - [#3717](https://github.com/facebook/create-react-app/pull/3717) Update README.md. ([@maecapozzi](https://github.com/maecapozzi))
  - [#3710](https://github.com/facebook/create-react-app/pull/3710) Link to an explanation for forking react-scripts. ([@gaearon](https://github.com/gaearon))
  - [#3709](https://github.com/facebook/create-react-app/pull/3709) Document adding a router. ([@gaearon](https://github.com/gaearon))
  - [#3670](https://github.com/facebook/create-react-app/pull/3670) Fix typo in the User Guide. ([@qbahers](https://github.com/qbahers))
  - [#3645](https://github.com/facebook/create-react-app/pull/3645) Update README.md. ([@elie222](https://github.com/elie222))
  - [#3533](https://github.com/facebook/create-react-app/pull/3533) Use safer/more aesthetic syntax for setting environment variables on Windows. ([@cdanielsen](https://github.com/cdanielsen))
  - [#3605](https://github.com/facebook/create-react-app/pull/3605) Updated Debugging Tests for VSCode. ([@amadeogallardo](https://github.com/amadeogallardo))
  - [#3601](https://github.com/facebook/create-react-app/pull/3601) Fixed typo in webpack.config.dev.js. ([@nmenglund](https://github.com/nmenglund))
  - [#3576](https://github.com/facebook/create-react-app/pull/3576) Updates comment to reflect codebase. ([@rahulcs](https://github.com/rahulcs))
  - [#3510](https://github.com/facebook/create-react-app/pull/3510) Update User Guide with deploying to GitHub User pages. ([@aaronlna](https://github.com/aaronlna))
  - [#3503](https://github.com/facebook/create-react-app/pull/3503) Update Prettier editor integration link. ([@gaving](https://github.com/gaving))
  - [#3453](https://github.com/facebook/create-react-app/pull/3453) Fix dead links. ([@vannio](https://github.com/vannio))
  - [#2992](https://github.com/facebook/create-react-app/pull/2992) Docs: How to Debug Unit Tests. ([@MattMorgis](https://github.com/MattMorgis))

- Other

  - [#3729](https://github.com/facebook/create-react-app/pull/3729) Update README.md to note Neutrino's support of react components. ([@eliperelman](https://github.com/eliperelman))
  - [#2841](https://github.com/facebook/create-react-app/pull/2841) Documentation to help windows contributors. ([@Dubes](https://github.com/Dubes))
  - [#3489](https://github.com/facebook/create-react-app/pull/3489) Add link to nvm-windows. ([@davidgilbertson](https://github.com/davidgilbertson))

- `eslint-config-react-app`

  - [#3460](https://github.com/facebook/create-react-app/pull/3460) Fix broken link to `href-no-hash` eslint rule. ([@hazolsky](https://github.com/hazolsky))

#### :house: Internal

- Other

  - [#3769](https://github.com/facebook/create-react-app/pull/3769) Enable Yarn check files. ([@Timer](https://github.com/Timer))
  - [#3756](https://github.com/facebook/create-react-app/pull/3756) Clean up changes to npm and yarn registry in E2E tests. ([@viankakrisna](https://github.com/viankakrisna))
  - [#3744](https://github.com/facebook/create-react-app/pull/3744) Use private registry in E2E tests. ([@Timer](https://github.com/Timer))
  - [#3738](https://github.com/facebook/create-react-app/pull/3738) Always use Yarn on CI. ([@gaearon](https://github.com/gaearon))
  - [#2309](https://github.com/facebook/create-react-app/pull/2309) Port `cra.sh` development task to javascript. ([@ianschmitz](https://github.com/ianschmitz))
  - [#3411](https://github.com/facebook/create-react-app/pull/3411) Simplify waiting for app start in E2E tests. ([@xjlim](https://github.com/xjlim))
  - [#3755](https://github.com/facebook/create-react-app/pull/3755) Switch to Yarn Workspaces. ([@gaearon](https://github.com/gaearon))
  - [#3757](https://github.com/facebook/create-react-app/pull/3757) Try updating Flow. ([@gaearon](https://github.com/gaearon))
  - [#3414](https://github.com/facebook/create-react-app/pull/3414) Export `dismissRuntimeErrors` function. ([@skidding](https://github.com/skidding))
  - [#3036](https://github.com/facebook/create-react-app/pull/3036) Cleaning up `printHostingInstructions` a bit. ([@GreenGremlin](https://github.com/GreenGremlin))
  - [#3514](https://github.com/facebook/create-react-app/pull/3514) Fix `FileSizeReporter` for multi build webpack setups. ([@iiska](https://github.com/iiska))
  - [#3362](https://github.com/facebook/create-react-app/pull/3362) Refactor extra watch options regex to `react-dev-utils`. ([@xjlim](https://github.com/xjlim))

#### Committers: 47

- Aaron Lamb ([aaronlna](https://github.com/aaronlna))
- Ade Viankakrisna Fadlil ([viankakrisna](https://github.com/viankakrisna))
- Amadeo Gallardo ([amadeogallardo](https://github.com/amadeogallardo))
- Andy Kenward ([andykenward](https://github.com/andykenward))
- Christian Danielsen ([cdanielsen](https://github.com/cdanielsen))
- Clayton Ray ([iamclaytonray](https://github.com/iamclaytonray))
- Dan Abramov ([gaearon](https://github.com/gaearon))
- Daniel Verejan ([danielverejan](https://github.com/danielverejan))
- Danny Calleri ([dannycalleri](https://github.com/dannycalleri))
- David Boyne ([boyney123](https://github.com/boyney123))
- David Gilbertson ([davidgilbertson](https://github.com/davidgilbertson))
- Eli Perelman ([eliperelman](https://github.com/eliperelman))
- Elie ([elie222](https://github.com/elie222))
- Ernesto García ([gnapse](https://github.com/gnapse))
- Evan You ([yyx990803](https://github.com/yyx990803))
- Gavin Gilmour ([gaving](https://github.com/gaving))
- Ian Schmitz ([ianschmitz](https://github.com/ianschmitz))
- Ian Sutherl
... [TRUNCATED]
```

### File: CHANGELOG-2.x.md
```md
## 3.0.0 and Newer Versions

**Please refer to [CHANGELOG.md](./CHANGELOG.md) for the newer versions.**

## 2.1.8 (March 7, 2019)

v2.1.8 is a maintenance release that reapplies the TypeScript speed improvements ([#6406](https://github.com/facebook/create-react-app/pull/6406)) in a new major version of `react-dev-utils`.

### Migrating from 2.1.7 to 2.1.8

Inside any created project that has not been ejected, run:

```sh
npm install --save --save-exact react-scripts@2.1.8
```

or

```sh
yarn add --exact react-scripts@2.1.8
```

## 2.1.7 (March 7, 2019)

v2.1.7 is a maintenance release that temporarily reverts the TypeScript speed improvements ([#6406](https://github.com/facebook/create-react-app/pull/6406)) to fix a dependency issue in `react-dev-utils`.

### Migrating from 2.1.6 to 2.1.7

Inside any created project that has not been ejected, run:

```sh
npm install --save --save-exact react-scripts@2.1.7
```

or

```sh
yarn add --exact react-scripts@2.1.7
```

## 2.1.6 (March 6, 2019)

v2.1.6 is a maintenance release that brings a few new improvements, most notably:

- :rocket: Reduced TypeScript rebuild times while running the development server. This was previously introduced in v2.1.4 but had to be reverted. Thanks to [@ianschmitz](https://github.com/ianschmitz) for getting this ready.

#### :bug: Bug Fix

- `react-dev-utils`
  - [#6511](https://github.com/facebook/create-react-app/pull/6511) Fix deploy instructions to make link clickable. ([@sbimochan](https://github.com/sbimochan))
- `react-scripts`
  - [#6472](https://github.com/facebook/create-react-app/pull/6472) Revert CSS sourcemaps in development. ([@bugzpodder](https://github.com/bugzpodder))
  - [#6444](https://github.com/facebook/create-react-app/pull/6444) Revert "Switch to eval-source-map (#5060)". ([@ianschmitz](https://github.com/ianschmitz))

#### :nail_care: Enhancement

- `react-dev-utils`, `react-scripts`
  - [#6406](https://github.com/facebook/create-react-app/pull/6406) Speed up TypeScript rebuild times in development. ([@ianschmitz](https://github.com/ianschmitz))
- `create-react-app`
  - [#6253](https://github.com/facebook/create-react-app/pull/6253) Only use `yarn.lock.cached` if using the default Yarn registry. ([@hangryCat](https://github.com/hangryCat))
- `react-scripts`
  - [#5457](https://github.com/facebook/create-react-app/pull/5457) Add forward ref to React SVG Component. ([@GasimGasimzada](https://github.com/GasimGasimzada))

#### :memo: Documentation

- `babel-preset-react-app`
  - [#6254](https://github.com/facebook/create-react-app/pull/6254) Improve Flow and TypeScript usage docs. ([@saranshkataria](https://github.com/saranshkataria))
- `babel-preset-react-app`, `confusing-browser-globals`, `react-app-polyfill`
  - [#6419](https://github.com/facebook/create-react-app/pull/6419) Improve language used in markdown code blocks. ([@cherouvim](https://github.com/cherouvim))
- `create-react-app`
  - [#6481](https://github.com/facebook/create-react-app/pull/6481) Fix typo. ([@adyouri](https://github.com/adyouri))
- `react-dev-utils`
  - [#6482](https://github.com/facebook/create-react-app/pull/6482) Fix typo. ([@mattfwood](https://github.com/mattfwood))
- Other
  - [#6438](https://github.com/facebook/create-react-app/pull/6438) Update `source-map-explorer` docs to analyze all chunks. ([@Kamahl19](https://github.com/Kamahl19))
  - [#6454](https://github.com/facebook/create-react-app/pull/6454) Fix typo. ([@DenrizSusam](https://github.com/DenrizSusam))
  - [#5767](https://github.com/facebook/create-react-app/pull/5767) Add information about using custom registries in e2e testing #4488. ([@juanpicado](https://github.com/juanpicado))
- `react-dev-utils`, `react-scripts`
  - [#6239](https://github.com/facebook/create-react-app/pull/6239) Convert all bit.ly links from http to https. ([@leighhalliday](https://github.com/leighhalliday))

#### :house: Internal

- [#6493](https://github.com/facebook/create-react-app/pull/6493) Remove AppVeyor config files. ([@iansu](https://github.com/iansu))
- [#6474](https://github.com/facebook/create-react-app/pull/6474) Remove latest Node version from Travis config. ([@iansu](https://github.com/iansu))

#### :hammer: Underlying Tools

- `react-scripts`
  - [#6387](https://github.com/facebook/create-react-app/pull/6387) Use contenthash instead of chunkhash for better long-term caching. ([@ianschmitz](https://github.com/ianschmitz))
- Other
  - [#6365](https://github.com/facebook/create-react-app/pull/6365) Upgrade Docusaurus and enable new features. ([@yangshun](https://github.com/yangshun))

#### Committers: 15

- Abdelhadi Dyouri ([adyouri](https://github.com/adyouri))
- Bimochan Shrestha ([sbimochan](https://github.com/sbimochan))
- Deniz Susman ([DenrizSusam](https://github.com/DenrizSusam))
- Gasim Gasimzada ([GasimGasimzada](https://github.com/GasimGasimzada))
- Ian Schmitz ([ianschmitz](https://github.com/ianschmitz))
- Ian Sutherland ([iansu](https://github.com/iansu))
- Ioannis Cherouvim ([cherouvim](https://github.com/cherouvim))
- Jack Zhao ([bugzpodder](https://github.com/bugzpodder))
- Juan Picado @jotadeveloper ([juanpicado](https://github.com/juanpicado))
- Leigh Halliday ([leighhalliday](https://github.com/leighhalliday))
- Martin Litvaj ([Kamahl19](https://github.com/Kamahl19))
- Matt Wood ([mattfwood](https://github.com/mattfwood))
- Meo H. ([hangryCat](https://github.com/hangryCat))
- Saransh Kataria ([saranshkataria](https://github.com/saranshkataria))
- Yangshun Tay ([yangshun](https://github.com/yangshun))

### Migrating from 2.1.5 to 2.1.6

Inside any created project that has not been ejected, run:

```sh
npm install --save --save-exact react-scripts@2.1.6
```

or

```sh
yarn add --exact react-scripts@2.1.6
```

## 2.1.5 (February 11, 2019)

v2.1.5 is a maintenance release that reverts the TypeScript speed improvements ([#5903](https://github.com/facebook/create-react-app/pull/5903)) to fix a dependency issue in `react-dev-utils`.

### Migrating from 2.1.4 to 2.1.5

Inside any created project that has not been ejected, run:

```sh
npm install --save --save-exact react-scripts@2.1.5
```

or

```sh
yarn add --exact react-scripts@2.1.5
```

## 2.1.4 (February 10, 2019)

v2.1.4 is a maintenance release that brings a number of awesome improvements. A few notable ones include:

- :rocket: Reduced TypeScript rebuild times while running the development server. TypeScript is now blazing fast! Special thanks to [@deftomat](https://github.com/deftomat) and [@johnnyreilly](https://github.com/johnnyreilly) and the other contributors for their hard work on this. ([#5903](https://github.com/facebook/create-react-app/pull/5903))
- Jest [type ahead support](https://github.com/jest-community/jest-watch-typeahead) which provides a much nicer experience when filtering your tests using the Jest CLI ([#5213](https://github.com/facebook/create-react-app/pull/5213))
- And many more improvements!

#### :bug: Bug Fix

- `react-scripts`
  - [#6364](https://github.com/facebook/create-react-app/pull/6364) Use semicolons in the ProcessEnv interface. ([@DominikPalo](https://github.com/DominikPalo))
  - [#6276](https://github.com/facebook/create-react-app/pull/6276) Prevent cursor events on app-logo svg. ([@kostadriano](https://github.com/kostadriano))

#### :nail_care: Enhancement

- `react-scripts`
  - [#5213](https://github.com/facebook/create-react-app/pull/5213) Add Jest typeahead plugin. ([@gaearon](https://github.com/gaearon))
  - [#5713](https://github.com/facebook/create-react-app/pull/5713) Sass source map for dev. ([@zhuoli99](https://github.com/zhuoli99))
  - [#6285](https://github.com/facebook/create-react-app/pull/6285) Allow react-scripts test --no-watch. ([@ricokahler](https://github.com/ricokahler))
  - [#5060](https://github.com/facebook/create-react-app/pull/5060) Enable eval-source-map for firefox. ([@jasonLaster](https://github.com/jasonLaster))
- `react-dev-utils`, `react-scripts`
  - [#5903](https://github.com/facebook/create-react-app/pull/5903) Speed up TypeScript projects. ([@deftomat](https://github.com/deftomat))

#### :memo: Documentation

- Other
  - [#6383](https://github.com/facebook/create-react-app/pull/6383) Update docs links to prefer HTTPS for supported domains. ([@ianschmitz](https://github.com/ianschmitz))
  - [#6062](https://github.com/facebook/create-react-app/pull/6062) [docs] Warn/clarify that env vars are NOT "SECRET". ([@JBallin](https://github.com/JBallin))
  - [#6359](https://github.com/facebook/create-react-app/pull/6359) Update ZEIT Now deployment instructions. ([@timothyis](https://github.com/timothyis))
  - [#6346](https://github.com/facebook/create-react-app/pull/6346) Minor issue in README.md. ([@nathanlschneider](https://github.com/nathanlschneider))
  - [#6331](https://github.com/facebook/create-react-app/pull/6331) Update docs to document `--no-watch`. ([@ricokahler](https://github.com/ricokahler))
  - [#6229](https://github.com/facebook/create-react-app/pull/6229) Update `serve` port flag and add example. ([@lyzhovnik](https://github.com/lyzhovnik))
  - [#6190](https://github.com/facebook/create-react-app/pull/6190) Updating updating-to-new-releases.md for users who installed CRA globally. ([@carpben](https://github.com/carpben))
  - [#6095](https://github.com/facebook/create-react-app/pull/6095) Changes to steps for publishing GitHub User Page. ([@StevenTan](https://github.com/StevenTan))
  - [#6157](https://github.com/facebook/create-react-app/pull/6157) Add note for global install of CLI. ([@ianschmitz](https://github.com/ianschmitz))
  - [#6149](https://github.com/facebook/create-react-app/pull/6149) update link for difference between proposal stages. ([@loveky](https://github.com/loveky))
  - [#6141](https://github.com/facebook/create-react-app/pull/6141) Remove extra table cell. ([@yangshun](https://github.com/yangshun))
- `react-scripts`
  - [#6355](https://github.com/facebook/create-react-app/pull/6355) Make manifest.json description more generic. ([@chrisself](https://github.com/chrisself))

#### :house: Internal

- Other
  - [#6050](https://github.com/facebook/create-react-app/pull/6050) Fix e2e:docker failure with "access denied". ([@jamesknelson](https://github.com/jamesknelson))
  - [#6179](https://github.com/facebook/create-react-app/pull/6179) Update local-test.sh to return test exit code. ([@dallonf](https://github.com/dallonf))
  - [#6165](https://github.com/facebook/create-react-app/pull/6165) Fix CI builds. ([@ianschmitz](https://github.com/ianschmitz))
- `react-scripts`
  - [#5798](https://github.com/facebook/create-react-app/pull/5798) Added `module` to ignored node modules list. ([@dotansimha](https://github.com/dotansimha))
  - [#6022](https://github.com/facebook/create-react-app/pull/6022) TypeScript detection filtering 'node_modules'.. ([@holloway](https://github.com/holloway))
- `react-dev-utils`, `react-scripts`
  - [#6150](https://github.com/facebook/create-react-app/pull/6150) dependencies: move chalk to react-dev-utils. ([@otaviopace](https://github.com/otaviopace))
- `babel-plugin-named-asset-import`, `react-scripts`
  - [#5816](https://github.com/facebook/create-react-app/pull/5816) Upgrade @svgr/webpack to 4.1.0. ([@alaycock](https://github.com/alaycock))
- `react-dev-utils`
  - [#6162](https://github.com/facebook/create-react-app/pull/6162) Update react-dev-util globby dependency to v8.0.2. ([@davidlukerice](https://github.com/davidlukerice))
- `babel-preset-react-app`, `react-app-polyfill`, `react-dev-utils`, `react-error-overlay`, `react-scripts`
  - [#6137](https://github.com/facebook/create-react-app/pull/6137) Fix CI and upgrade dependencies. ([@Timer](https://github.com/Timer))

#### :hammer: Underlying Tools

- `babel-preset-react-app`, `react-app-polyfill`, `react-dev-utils`, `react-scripts`
  - [#6393](https://github.com/facebook/create-react-app/pull/6393) Upgrade dependencies. ([@ianschmitz](https://github.com/ianschmitz))
- `babel-preset-react-app`
  - [#6307](https://github.com/facebook/create-react-app/pull/6307) Update babel-plugin-macros 2.4.4 -> 2.4.5. ([@maniax89](https://github.com/maniax89))
- `eslint-config-react-app`, `react-scripts`
  - [#6132](https://github.com/facebook/create-react-app/pull/6132) Bump eslint-plugin-react version and update webpack config. ([@ianschmitz](https://github.com/ianschmitz))

#### Committers: 29

- Adam Laycock ([alaycock](https://github.com/alaycock))
- Adriano Costa ([kostadriano](https://github.com/kostadriano))
- Andrew Turgeon ([maniax89](https://github.com/maniax89))
- Ben Carp ([carpben](https://github.com/carpben))
- Charles Pritchard ([Downchuck](https://github.com/Downchuck))
- Chris Self ([chrisself](https://github.com/chrisself))
- Dallon Feldner ([dallonf](https://github.com/dallonf))
- Dan Abramov ([gaearon](https://github.com/gaearon))
- David Rice ([davidlukerice](https://github.com/davidlukerice))
- Dominik Palo ([DominikPalo](https://github.com/DominikPalo))
- Dotan Simha ([dotansimha](https://github.com/dotansimha))
- Ian Schmitz ([ianschmitz](https://github.com/ianschmitz))
- JBallin ([JBallin](https://github.com/JBallin))
- James George ([jamesgeorge007](https://github.com/jamesgeorge007))
- James K Nelson ([jamesknelson](https://github.com/jamesknelson))
- Jason Laster ([jasonLaster](https://github.com/jasonLaster))
- Joe Haddad ([Timer](https://github.com/Timer))
- Matthew Holloway ([holloway](https://github.com/holloway))
- Nathan Schneider ([nathanlschneider](https://github.com/nathanlschneider))
- Nikita Lyzhov ([lyzhovnik](https://github.com/lyzhovnik))
- Otávio Pace ([otaviopace](https://github.com/otaviopace))
- Rico Kahler ([ricokahler](https://github.com/ricokahler))
- Steven Tan ([StevenTan](https://github.com/StevenTan))
- Timothy ([timothyis](https://github.com/timothyis))
- Tomáš Szabo ([deftomat](https://github.com/deftomat))
- Yangshun Tay ([yangshun](https://github.com/yangshun))
- [gottfired](https://github.com/gottfired)
- [zhuoli99](https://github.com/zhuoli99)
- loveky ([loveky](https://github.com/loveky))

### Migrating from 2.1.3 to 2.1.4

Inside any created project that has not been ejected, run:

```sh
npm install --save --save-exact react-scripts@2.1.4
```

or

```sh
yarn add --exact react-scripts@2.1.4
```

## 2.1.3 (January 4, 2019)

v2.1.3 is a maintenance release to fix a [vulnerability in webpack-dev-server](https://www.npmjs.com/advisories/725).

#### :memo: Documentation

- Other
  - [#6067](https://github.com/facebook/create-react-app/pull/6067) Correct an error for documentation. ([@hardo](https://github.com/hardo))
  - [#6110](https://github.com/facebook/create-react-app/pull/6110) Replace deprecated VSCode launch.json variable. ([@raiskila](https://github.com/raiskila))
  - [#5631](https://github.com/facebook/create-react-app/pull/5631) Generalize the adding bootstrap documentation. ([@jquense](https://github.com/jquense))
  - [#6084](https://github.com/facebook/create-react-app/pull/6084) Remove outdated docs fo
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

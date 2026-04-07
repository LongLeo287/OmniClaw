---
id: ReactiveTraderCloud
type: knowledge
owner: OA_Triage
---
# ReactiveTraderCloud
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
[![example workflow](https://github.com/AdaptiveConsulting/ReactiveTraderCloud/actions/workflows/branch.yml/badge.svg?branch=master)](https://github.com/AdaptiveConsulting/ReactiveTraderCloud/actions/workflows/branch.yml)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/AdaptiveConsulting/ReactiveTraderCloud)](https://github.com/AdaptiveConsulting/ReactiveTraderCloud/releases/latest)
[![GitHub](https://img.shields.io/github/license/AdaptiveConsulting/ReactiveTraderCloud)](https://opensource.org/licenses/Apache-2.0)

[![image](images/adaptive-logo.svg)](http://weareadaptive.com/)

# Reactive Trader® (ARCHIVED)

THIS REPO WILL NOT BE UPDATED IN FUTURE.

However, it remains as a public example of a reactive UI of significant scale using React, Rxjs, and react-rxjs, with desktop variants for OpenFin and Finsemble, connecting to an Adaptive Hydra® / Aeron® backend.
The showcase linked below will remain current, but the desktop variants will not be part of the suite in future.

## Description

Reactive Trader® is a real-time FX trading platform designed to showcase reactive programming principles across the full application stack.

Written in React and RxJs / React-RxJs and running on [Hydra](https://weareadaptive.com/hydra/), the platform will continue to evolve and use the latest technologies.

Please see [our Showcase page](https://weareadaptive.com/showcase/) for a full list of the latest features.

![image](/packages/client/public-workspace/images/previews/reactive-trader.PNG)

## Demo

- [Web & Mobile](https://www.reactivetrader.com)
- [OpenFin([]](https://openfin.co/)) & [Finsemble](https://cosaic.io/finsemble/) installers [here](./packages/client/install/README.md)
- [Style guide](https://www.reactivetrader.com/storybook): Colours, iconography, typography, atoms and molecules
- [Storybook](https://www.reactivetrader.com/styleguide): Explore individual React components

## Who are we?

Reactive Trader was written by the team at [Adaptive](http://weareadaptive.com/), a consultancy that specialises in building real-time trading systems.

Please [contact us](https://weareadaptive.com/contact/) if you'd like to learn more, or follow us via our [blog](https://weareadaptive.com/life-at-adaptive/), [Twitter](https://twitter.com/WeAreAdaptive), or [LinkedIn](https://www.linkedin.com/company/adaptive-consulting-ltd/).

## License

This application is made available under the [Apache license v2.0](./LICENSE).

```

### File: FETCHED_ReactiveTraderCloud_033152\README.md
```md
[![example workflow](https://github.com/AdaptiveConsulting/ReactiveTraderCloud/actions/workflows/branch.yml/badge.svg?branch=master)](https://github.com/AdaptiveConsulting/ReactiveTraderCloud/actions/workflows/branch.yml)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/AdaptiveConsulting/ReactiveTraderCloud)](https://github.com/AdaptiveConsulting/ReactiveTraderCloud/releases/latest)
[![GitHub](https://img.shields.io/github/license/AdaptiveConsulting/ReactiveTraderCloud)](https://opensource.org/licenses/Apache-2.0)

[![image](images/adaptive-logo.svg)](http://weareadaptive.com/)

# Reactive Trader® (ARCHIVED)

THIS REPO WILL NOT BE UPDATED IN FUTURE.

However, it remains as a public example of a reactive UI of significant scale using React, Rxjs, and react-rxjs, with desktop variants for OpenFin and Finsemble, connecting to an Adaptive Hydra® / Aeron® backend.
The showcase linked below will remain current, but the desktop variants will not be part of the suite in future.

## Description

Reactive Trader® is a real-time FX trading platform designed to showcase reactive programming principles across the full application stack.

Written in React and RxJs / React-RxJs and running on [Hydra](https://weareadaptive.com/hydra/), the platform will continue to evolve and use the latest technologies.

Please see [our Showcase page](https://weareadaptive.com/showcase/) for a full list of the latest features.

![image](/packages/client/public-workspace/images/previews/reactive-trader.PNG)

## Demo

- [Web & Mobile](https://www.reactivetrader.com)
- [OpenFin([]](https://openfin.co/)) & [Finsemble](https://cosaic.io/finsemble/) installers [here](./packages/client/install/README.md)
- [Style guide](https://www.reactivetrader.com/storybook): Colours, iconography, typography, atoms and molecules
- [Storybook](https://www.reactivetrader.com/styleguide): Explore individual React components

## Who are we?

Reactive Trader was written by the team at [Adaptive](http://weareadaptive.com/), a consultancy that specialises in building real-time trading systems.

Please [contact us](https://weareadaptive.com/contact/) if you'd like to learn more, or follow us via our [blog](https://weareadaptive.com/life-at-adaptive/), [Twitter](https://twitter.com/WeAreAdaptive), or [LinkedIn](https://www.linkedin.com/company/adaptive-consulting-ltd/).

## License

This application is made available under the [Apache license v2.0](./LICENSE).

```

### File: packages\client\package.json
```json
{
  "name": "reactive-trader-cloud",
  "description": "Reactive Trader® - Cloud edition. Example reactive currency pair trading app",
  "sideEffects": false,
  "type": "module",
  "keywords": [
    "react",
    "fx",
    "spot",
    "cloud",
    "rxjs"
  ],
  "authors": [
    {
      "name": "Adaptive Financial Consulting",
      "email": "@AdaptiveLimited"
    }
  ],
  "engines": {
    "node": ">= 22.14.0"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/AdaptiveConsulting/ReactiveTraderCloud.git"
  },
  "scripts": {
    "typecheck": "tsc",
    "lint": "eslint . --max-warnings 0",
    "lint:fix": "npm run lint -- --fix",
    "lint:cache": "npm run lint -- --cache",
    "_format": "prettier README.md src e2e",
    "format": "npm run _format -- --write",
    "format:check": "npm run _format -- --check",
    "test": "vitest",
    "test:run": "vitest run --no-coverage",
    "test:coverage": "vitest run",
    "verify": "npm run typecheck && npm run lint && npm run format:check && npm run test:run",
    "_runLocal": "cross-env VITE_HYDRA_URL=ws://localhost:8929 $npm_config_runcmd",
    "start:local": "npm run _runLocal --runcmd=vite",
    "start": "vite",
    "build": "vite build",
    "serve": "vite preview",
    "preview": "vite preview",
    "openfin:dev": "cross-env TARGET=openfin vite",
    "openfin:local": "npm run _runLocal --runcmd=\"TARGET=openfin vite\"",
    "_openfin:run": "cross-env-shell \"wait-on -l $npm_config_manifest_url && openfin -l -c $npm_config_manifest_url\"",
    "openfin:run:fx": "npm run _openfin:run --manifest_url=http://localhost:1917/config/rt-fx.json",
    "openfin:run:credit": "npm run _openfin:run --manifest_url=http://localhost:1917/config/rt-credit.json",
    "openfin:run:limitchecker": "npm run _openfin:run --manifest_url=http://localhost:1917/config/limit-checker.json",
    "openfin:run:launcher": "npm run _openfin:run --manifest_url=http://localhost:1917/config/launcher.json",
    "openfin:run:workspace": "npm run _openfin:run --manifest_url=http://localhost:1917/workspace/config/workspace.json",
    "openfin:start:fx": "concurrently \"npm:openfin:dev\" \"npm:openfin:run:fx\"",
    "openfin:start:fx:local": "concurrently \"npm:openfin:local\" \"npm:openfin:run:fx\"",
    "openfin:start:credit": "concurrently \"npm:openfin:dev\" \"npm:openfin:run:credit\"",
    "openfin:start:credit:local": "concurrently \"npm:openfin:local\" \"npm:openfin:run:credit\"",
    "openfin:start:limitchecker": "concurrently \"npm:openfin:dev\" \"npm:openfin:run:limitchecker\"",
    "openfin:start:launcher": "concurrently \"npm:openfin:dev\" \"npm:openfin:run:launcher\"",
    "openfin:start:launcher:local": "concurrently \"npm:openfin:local\" \"npm:openfin:run:launcher\"",
    "openfin:start:workspace": "concurrently \"npm:openfin:dev\" \"npm:workspace:run\"",
    "openfin:build": "cross-env TARGET=openfin vite build",
    "openfin:preview:launcher": "npm:openfin:build && concurrently \"npm:serve\" \"npm:openfin:run:launcher\"",
    "openfin:preview:workspace": "npm:openfin:build && concurrently \"npm:serve\" \"npm:workspace:run\"",
    "finsemble:dev": "cross-env TARGET=finsemble vite",
    "finsemble:build": "cross-env TARGET=finsemble vite build",
    "storybook": "storybook dev -p 6006",
    "storybook:build": "cross-env STORYBOOK=true storybook build -o ./dist/storybook",
    "_e2e:openfin:run": "cross-env-shell of-automation $npm_config_manifest_url ./e2e/openfin.spec.js --devToolsPort=9091 --closeRuntime=never",
    "e2e:openfin": "playwright test --project=openfin",
    "e2e:openfin:smoke": "playwright test --project=openfin --grep @smoke",
    "e2e:web": "playwright test --project=web",
    "e2e:web:smoke": "playwright test --project=web --grep @smoke",
    "generateCod": "hydra-web-codegen -i ../../trading-gateway.hyer -o src/generated"
  },
  "dependencies": {
    "@adaptive/hydra-platform": "4.70.0",
    "@finos/fdc3": "^1.2.0",
    "@openfin/core": "33.77.11",
    "@openfin/workspace": "16.1.7",
    "@openfin/workspace-platform": "16.1.7",
    "@react-rxjs/core": "^0.10.3",
    "@react-rxjs/utils": "^0.9.5",
    "d3": "7.9.0",
    "date-fns": "^2.19.0",
    "downshift": "^6.1.9",
    "lodash": "4.17.21",
    "polished": "^4.1.1",
    "query-string": "^7.1.3",
    "react": "18.3.1",
    "react-dom": "18.3.1",
    "react-icons": "^4.2.0",
    "react-measure": "2.5.2",
    "react-router-dom": "6.10.0",
    "react-switch": "7.0.0",
    "react-virtualized-auto-sizer": "^1.0.7",
    "react-window": "1.8.8",
    "ress": "^3.0.0",
    "rxjs": "7.8.1",
    "styled-components": "5.3.9"
  },
  "overrides": {
    "cookie": "0.x",
    "next": "14.2.26",
    "tar-fs": "3.0.8"
  },
  "optionalDependencies": {
    "@adaptive-uikit/figma-to-theme": "0.0.2"
  },
  "devDependencies": {
    "@adaptive/hydra-web-codegen": "4.70.0",
    "@eslint/js": "9.21.0",
    "@google-cloud/dialogflow": "6.7.0",
    "@openfin/automation-cli": "1.3.0",
    "@playwright/test": "1.49.0",
    "@storybook/addon-essentials": "8.6.0",
    "@storybook/react": "8.6.0",
    "@storybook/react-vite": "8.6.0",
    "@testing-library/react": "16.0.0",
    "@testing-library/user-event": "14.5.2",
    "@types/d3": "7.4.3",
    "@types/eslint": "9.6.1",
    "@types/lodash": "4.17.10",
    "@types/node": "20.x",
    "@types/react": "18.3.3",
    "@types/react-dom": "18.3.0",
    "@types/react-measure": "2.0.12",
    "@types/react-virtualized-auto-sizer": "^1.0.1",
    "@types/react-window": "^1.8.5",
    "@types/styled-components": "5.1.26",
    "@vitejs/plugin-react": "4.3.4",
    "@vitest/browser": "3.0.7",
    "@vitest/eslint-plugin": "1.1.32",
    "concurrently": "9.0.1",
    "cross-env": "^6.0.3",
    "csstype": "^3.0.2",
    "eslint": "9.21.0",
    "eslint-plugin-import": "2.31.0",
    "eslint-plugin-playwright": "2.2.0",
    "eslint-plugin-react": "7.37.4",
    "eslint-plugin-react-hooks": "5.2.0",
    "eslint-plugin-simple-import-sort": "12.1.1",
    "globals": "16.0.0",
    "jest-styled-components": "7.2.0",
    "jsdom": "26.0.0",
    "openfin-cli": "4.0.0",
    "prettier": "3.5.2",
    "rollup-plugin-workbox": "8.1.2",
    "storybook": "8.6.0",
    "storybook-dark-mode": "4.0.2",
    "typescript": "5.5.4",
    "typescript-eslint": "8.25.0",
    "unplugin-fonts": "1.3.1",
    "vite": "6.2.4",
    "vite-plugin-html": "3.2.2",
    "vite-plugin-static-copy": "2.2.0",
    "vitest": "3.0.7",
    "wait-on": "8.0.1"
  }
}

```

### File: packages\client\README.md
```md
# Reactive Trader Client

The trading client GUI is a single page app (SPA) built using Typescript, React, RxJs and Styled Components. Separate builds can be run in the browser, on mobile or desktop as a PWA, and as a desktop platform application using Openfin or Finsemble.

[High Level Technologies](#high-level-technologies)  
[Local Development Setup](#local-development-setup)  
[Running the client locally](#running-the-client-locally)  
[Openfin](#openfin)  
[Finsemble](#finsemble)  
[Storybook](#storybook)  
[Progressive Web App](#progressive-web-app-or-pwa)  
[E2E Testing](#end-to-end-testing)  
[Token replacement](#token-replacement)  
[Deployment](#deployment)

## High level technologies

- Build system [Vite](https://vitejs.dev/)
- Tests use [Vitest](https://vitest.dev/)
- Streaming data abstractions are build with [RxJs](https://github.com/Reactive-Extensions/RxJS).
- Mapping Rx to React components with [react-rxjs](https://react-rxjs.org/).
- Styles build using [Styled Components](https://www.styled-components.com/).
- Connectivity to the backend is done via Hydra.

## Local Development Setup

Required:

- [Node](https://nodejs.org) (v20+ see "engine" spec in package.json - suggest using `nvm` to manage node instances)

VS Code / Plugins

Suggest ESLint, Prettier extensions for immediate code quality management, with configuration such as:

```json
  "editor.codeActionsOnSave": {
    "source.fixAll": "always",
    "source.addMissingImports": "explicit"
  },
  "editor.formatOnSave": true,
```

Suggest [vitest](https://marketplace.visualstudio.com/items?itemName=vitest.explorer) for running tests in the IDE (currently requires Node path to be explicitly stated as `"vitest.nodeExecutable"` in VS Code settings)

### Testing and Quality Checks

Run `npm run verify` before pushing any commits to origin to run type checking, linting, format checking, and tests. This command is run as part of the continuous integration pipeline on GitHub actions.

### Mac and Windows

There are no additional packages to install other than Git and a recent build of Node.

### Linux

You might want to [increase the limit](http://stackoverflow.com/questions/16748737/grunt-watch-error-waiting-fatal-error-watch-enospc) on the number of files Linux will watch. [Here's why](https://github.com/coryhouse/react-slingshot/issues/6).

```sh
echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
```

## Running the client locally

Clone the repo, then install the necessary node modules:

```sh
npm install
```

Run the local (vite) dev server, by default this will point to the **dev** backend.

```sh
npm start
```

You can then browse the app at http://localhost:1917

### Additional commands

Any VITE\_\* properties may be added to a `.env.local` file (not checked in) or used to prefix an npm command.

Runs unit tests with Vitest.

```sh
npm run test
```

Create a production version of the application in the dist folder

```sh
npm run build
```

.. and run it

```sh
npm run serve
```

## Openfin

How to run a web server, to serve the client in OpenFin

```sh
npm run openfin:dev
```

and to run up the RT clients using OpenFin

```sh
npm run openfin:run:<app>
```

where `<app>` is `fx`, `credit`, `launcher`, or `limitchecker`

As a shortcut, to run the local dev server and client in one command, use

```sh
npm run openfin:start:<app>
```

#### Configs

Config files (OpenFin manifests) are located in [./public-openfin](./public-openfin).

Vite will replace placeholders at build time.

#### Troubleshooting

To debug OpenFin windows more easily (using Chromium devtools), check the relevant manifest for the appropriate port in e.g.

```json
    "arguments": "--remote-debugging-port=9092"
```

navigate to [chrome://inspect/#devices](chrome://inspect/#devices) in a Chrome tab

add the address in the dialog you get when you click "Configure ..."

```
http://localhost:<debug-port-from-above>
```

and any running OpenFin windows should be displayed, with Inspect links etc.

### NLP in the OpenFin Launcher and Workspace (below)

The OpenFin Launcher and Workspace Home UI have a search command line interface powered by [DialogFlow](https://cloud.google.com/dialogflow), where you can enter commands like

`buy 10m USDJPY`

For more insight into how NLP works see the diagflow function [doc](https://github.com/AdaptiveConsulting/ReactiveTraderCloud/blob/master/packages/server/cloud/nlp/README.md).

### Workspace

<img src="./public-workspace/images/previews/home.PNG">

Reactive Trader Workspace is a standalone application built on the [Openfin Workspace](https://developers.openfin.co/of-docs/docs/overview-of-workspace) platform.
It is built and deployed as a separate app in the Openfin bucket in Google Cloud Storage (under the subfolder/workspace)

The manifest file is available at:
http://openfin.prod.reactivetrader.com/workspace/config/workspace.json

and at the same `/workspace/config/workspace.json` path on every other (openfin) deployment ..

#### Running Locally

Working with OpenFin workspace locally using the OpenFin CLI ...

`npm run openfin:dev` as above to serve RT apps, views and the workspace platform

`npm run openfin:run:workspace` to launch workspace (when running local dev server, you'll see the "provider" window first)

As a shortcut, to run the local dev server and client in one command, use

```sh
npm run openfin:start:workspace
```

#### Configs

Config files are located in [./public-workspace/config](./public-workspace/config).

Vite will replace placeholders at build time.

[workspace.json](./public-workspace/config/workspace.json) - This is the manifest file Openfin uses to run the workspace provider.

[snapshot.json](./public-workspace/config/snapshot.json) - A workspace window _layout_ or 'snapshot', saved from previous layout modifications - on launching this (from the Home UI) the Trading Workspace will be displayed.

`analytics, live-rates, trades.json` - Basic .json files that contain the bare minimum to launch a view in the Openfin browser using `platform.launchApp`

#### Working with Workspace Data

Workspace config for pages / snapshots is stored in IndexedDB - example below is retrieving a saved workspace snapshot

```javascript
db = indexedDB.open(
  "openfin-workspace-platform-workspaces-adaptive-workspace-provider-local",
  1,
)
db.onsuccess = () => {
  console.log("Success")
  dbResult = db.result
}
db.onerror = () => {
  console.error("BAH")
}

// check what object stores you have under that DB (can also just look in devtools)
dbResult.objectStoreNames

// open transaction, get the object store and grab the key for the saved workspace
// annoyingly you have to do this even to just "look" at the data
data = dbResult
  .transaction("workspaces")
  .objectStore("workspaces")
  .get("fc9cdd93-104c-4305-97fa-92ea5a560546")

console.log(data.result)
```

## Finsemble

How to run a web server, to serve the client in Finsemble

```sh
npm run finsemble:dev
```

The Finsemble platform code (conceptually similar to the Workspace platform above) is in an internal repo .. ask a colleague for details.

## Storybook

How to run local instance of RT storybook

```sh
npm run storybook
```

_Tech Note: Since we are no longer using a middleware, we are able to serve Storybook from root (separate web server entirely from the main RT one) during development but for production, the build is all apart of the same bundle/server from /storybook/ which is handled in `.storybook/main.ts`._

There seems to be some issues with storybook cache on some machines, we can solve it by running it without the cache. We added --no-manager-cache to the storybook script

## End to End testing

How to run e2e tests against the web

```sh
npm start
```

```sh
npm run e2e:web -- --headed --workers=1
```

arguments: --headed (launches a browser visible to the user) and --workers=1 to serialise the tests (use e.g. --workers=2 to run tests in parallel)

How to run e2e tests against openfin

```sh
npm run openfin:start:launcher
```

and launch all of the apps from the launcher

```sh
npm run e2e:openfin -- --workers=1
```

## Progressive Web App or PWA

Reactive Trader can be installed as a progressive web application.

The [service worker](src/client/Web/serviceWorkerRegistration.ts) will need to be running for local development.

The settings for the PWA are configured in [`manifest.json`](public-pwa/manifest.json), plus various settings in index.html `<head>`. All attempts to date to bring iOS splash screens back to life have been fruitless, see [pwa-splash-screens](https://github.com/applification/pwa-splash-screens/blob/master/index.html) for reference.

## Token replacement

The PWA [`manifest.json`](public-pwa/manifest.json) file and the [OpenFin manifests](public-openfin) contain tokens in the form `<BLAH>` that are replaced at build time with environment-specific values (e.g. the application name may have an environment suffix).
This is either driven by config/logic in the [workflow files](../../.github/workflows) or constants/logic in the vite build.

## Deployment

Automatic branch, PR and Dev deployment (from master branch) is through [GitHub Actions](../../.github/workflows).

Actions also make UAT (branch) and Prod (tag) builds available on Google Cloud.

```

### File: FETCHED_ReactiveTraderCloud_033152\packages\client\package.json
```json
{
  "name": "reactive-trader-cloud",
  "description": "Reactive Trader® - Cloud edition. Example reactive currency pair trading app",
  "sideEffects": false,
  "type": "module",
  "keywords": [
    "react",
    "fx",
    "spot",
    "cloud",
    "rxjs"
  ],
  "authors": [
    {
      "name": "Adaptive Financial Consulting",
      "email": "@AdaptiveLimited"
    }
  ],
  "engines": {
    "node": ">= 22.14.0"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/AdaptiveConsulting/ReactiveTraderCloud.git"
  },
  "scripts": {
    "typecheck": "tsc",
    "lint": "eslint . --max-warnings 0",
    "lint:fix": "npm run lint -- --fix",
    "lint:cache": "npm run lint -- --cache",
    "_format": "prettier README.md src e2e",
    "format": "npm run _format -- --write",
    "format:check": "npm run _format -- --check",
    "test": "vitest",
    "test:run": "vitest run --no-coverage",
    "test:coverage": "vitest run",
    "verify": "npm run typecheck && npm run lint && npm run format:check && npm run test:run",
    "_runLocal": "cross-env VITE_HYDRA_URL=ws://localhost:8929 $npm_config_runcmd",
    "start:local": "npm run _runLocal --runcmd=vite",
    "start": "vite",
    "build": "vite build",
    "serve": "vite preview",
    "preview": "vite preview",
    "openfin:dev": "cross-env TARGET=openfin vite",
    "openfin:local": "npm run _runLocal --runcmd=\"TARGET=openfin vite\"",
    "_openfin:run": "cross-env-shell \"wait-on -l $npm_config_manifest_url && openfin -l -c $npm_config_manifest_url\"",
    "openfin:run:fx": "npm run _openfin:run --manifest_url=http://localhost:1917/config/rt-fx.json",
    "openfin:run:credit": "npm run _openfin:run --manifest_url=http://localhost:1917/config/rt-credit.json",
    "openfin:run:limitchecker": "npm run _openfin:run --manifest_url=http://localhost:1917/config/limit-checker.json",
    "openfin:run:launcher": "npm run _openfin:run --manifest_url=http://localhost:1917/config/launcher.json",
    "openfin:run:workspace": "npm run _openfin:run --manifest_url=http://localhost:1917/workspace/config/workspace.json",
    "openfin:start:fx": "concurrently \"npm:openfin:dev\" \"npm:openfin:run:fx\"",
    "openfin:start:fx:local": "concurrently \"npm:openfin:local\" \"npm:openfin:run:fx\"",
    "openfin:start:credit": "concurrently \"npm:openfin:dev\" \"npm:openfin:run:credit\"",
    "openfin:start:credit:local": "concurrently \"npm:openfin:local\" \"npm:openfin:run:credit\"",
    "openfin:start:limitchecker": "concurrently \"npm:openfin:dev\" \"npm:openfin:run:limitchecker\"",
    "openfin:start:launcher": "concurrently \"npm:openfin:dev\" \"npm:openfin:run:launcher\"",
    "openfin:start:launcher:local": "concurrently \"npm:openfin:local\" \"npm:openfin:run:launcher\"",
    "openfin:start:workspace": "concurrently \"npm:openfin:dev\" \"npm:workspace:run\"",
    "openfin:build": "cross-env TARGET=openfin vite build",
    "openfin:preview:launcher": "npm:openfin:build && concurrently \"npm:serve\" \"npm:openfin:run:launcher\"",
    "openfin:preview:workspace": "npm:openfin:build && concurrently \"npm:serve\" \"npm:workspace:run\"",
    "finsemble:dev": "cross-env TARGET=finsemble vite",
    "finsemble:build": "cross-env TARGET=finsemble vite build",
    "storybook": "storybook dev -p 6006",
    "storybook:build": "cross-env STORYBOOK=true storybook build -o ./dist/storybook",
    "_e2e:openfin:run": "cross-env-shell of-automation $npm_config_manifest_url ./e2e/openfin.spec.js --devToolsPort=9091 --closeRuntime=never",
    "e2e:openfin": "playwright test --project=openfin",
    "e2e:openfin:smoke": "playwright test --project=openfin --grep @smoke",
    "e2e:web": "playwright test --project=web",
    "e2e:web:smoke": "playwright test --project=web --grep @smoke",
    "generateCod": "hydra-web-codegen -i ../../trading-gateway.hyer -o src/generated"
  },
  "dependencies": {
    "@adaptive/hydra-platform": "4.70.0",
    "@finos/fdc3": "^1.2.0",
    "@openfin/core": "33.77.11",
    "@openfin/workspace": "16.1.7",
    "@openfin/workspace-platform": "16.1.7",
    "@react-rxjs/core": "^0.10.3",
    "@react-rxjs/utils": "^0.9.5",
    "d3": "7.9.0",
    "date-fns": "^2.19.0",
    "downshift": "^6.1.9",
    "lodash": "4.17.21",
    "polished": "^4.1.1",
    "query-string": "^7.1.3",
    "react": "18.3.1",
    "react-dom": "18.3.1",
    "react-icons": "^4.2.0",
    "react-measure": "2.5.2",
    "react-router-dom": "6.10.0",
    "react-switch": "7.0.0",
    "react-virtualized-auto-sizer": "^1.0.7",
    "react-window": "1.8.8",
    "ress": "^3.0.0",
    "rxjs": "7.8.1",
    "styled-components": "5.3.9"
  },
  "overrides": {
    "cookie": "0.x",
    "next": "14.2.26",
    "tar-fs": "3.0.8"
  },
  "optionalDependencies": {
    "@adaptive-uikit/figma-to-theme": "0.0.2"
  },
  "devDependencies": {
    "@adaptive/hydra-web-codegen": "4.70.0",
    "@eslint/js": "9.21.0",
    "@google-cloud/dialogflow": "6.7.0",
    "@openfin/automation-cli": "1.3.0",
    "@playwright/test": "1.49.0",
    "@storybook/addon-essentials": "8.6.0",
    "@storybook/react": "8.6.0",
    "@storybook/react-vite": "8.6.0",
    "@testing-library/react": "16.0.0",
    "@testing-library/user-event": "14.5.2",
    "@types/d3": "7.4.3",
    "@types/eslint": "9.6.1",
    "@types/lodash": "4.17.10",
    "@types/node": "20.x",
    "@types/react": "18.3.3",
    "@types/react-dom": "18.3.0",
    "@types/react-measure": "2.0.12",
    "@types/react-virtualized-auto-sizer": "^1.0.1",
    "@types/react-window": "^1.8.5",
    "@types/styled-components": "5.1.26",
    "@vitejs/plugin-react": "4.3.4",
    "@vitest/browser": "3.0.7",
    "@vitest/eslint-plugin": "1.1.32",
    "concurrently": "9.0.1",
    "cross-env": "^6.0.3",
    "csstype": "^3.0.2",
    "eslint": "9.21.0",
    "eslint-plugin-import": "2.31.0",
    "eslint-plugin-playwright": "2.2.0",
    "eslint-plugin-react": "7.37.4",
    "eslint-plugin-react-hooks": "5.2.0",
    "eslint-plugin-simple-import-sort": "12.1.1",
    "globals": "16.0.0",
    "jest-styled-components": "7.2.0",
    "jsdom": "26.0.0",
    "openfin-cli": "4.0.0",
    "prettier": "3.5.2",
    "rollup-plugin-workbox": "8.1.2",
    "storybook": "8.6.0",
    "storybook-dark-mode": "4.0.2",
    "typescript": "5.5.4",
    "typescript-eslint": "8.25.0",
    "unplugin-fonts": "1.3.1",
    "vite": "6.2.4",
    "vite-plugin-html": "3.2.2",
    "vite-plugin-static-copy": "2.2.0",
    "vitest": "3.0.7",
    "wait-on": "8.0.1"
  }
}

```

### File: FETCHED_ReactiveTraderCloud_033152\packages\client\README.md
```md
# Reactive Trader Client

The trading client GUI is a single page app (SPA) built using Typescript, React, RxJs and Styled Components. Separate builds can be run in the browser, on mobile or desktop as a PWA, and as a desktop platform application using Openfin or Finsemble.

[High Level Technologies](#high-level-technologies)  
[Local Development Setup](#local-development-setup)  
[Running the client locally](#running-the-client-locally)  
[Openfin](#openfin)  
[Finsemble](#finsemble)  
[Storybook](#storybook)  
[Progressive Web App](#progressive-web-app-or-pwa)  
[E2E Testing](#end-to-end-testing)  
[Token replacement](#token-replacement)  
[Deployment](#deployment)

## High level technologies

- Build system [Vite](https://vitejs.dev/)
- Tests use [Vitest](https://vitest.dev/)
- Streaming data abstractions are build with [RxJs](https://github.com/Reactive-Extensions/RxJS).
- Mapping Rx to React components with [react-rxjs](https://react-rxjs.org/).
- Styles build using [Styled Components](https://www.styled-components.com/).
- Connectivity to the backend is done via Hydra.

## Local Development Setup

Required:

- [Node](https://nodejs.org) (v20+ see "engine" spec in package.json - suggest using `nvm` to manage node instances)

VS Code / Plugins

Suggest ESLint, Prettier extensions for immediate code quality management, with configuration such as:

```json
  "editor.codeActionsOnSave": {
    "source.fixAll": "always",
    "source.addMissingImports": "explicit"
  },
  "editor.formatOnSave": true,
```

Suggest [vitest](https://marketplace.visualstudio.com/items?itemName=vitest.explorer) for running tests in the IDE (currently requires Node path to be explicitly stated as `"vitest.nodeExecutable"` in VS Code settings)

### Testing and Quality Checks

Run `npm run verify` before pushing any commits to origin to run type checking, linting, format checking, and tests. This command is run as part of the continuous integration pipeline on GitHub actions.

### Mac and Windows

There are no additional packages to install other than Git and a recent build of Node.

### Linux

You might want to [increase the limit](http://stackoverflow.com/questions/16748737/grunt-watch-error-waiting-fatal-error-watch-enospc) on the number of files Linux will watch. [Here's why](https://github.com/coryhouse/react-slingshot/issues/6).

```sh
echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
```

## Running the client locally

Clone the repo, then install the necessary node modules:

```sh
npm install
```

Run the local (vite) dev server, by default this will point to the **dev** backend.

```sh
npm start
```

You can then browse the app at http://localhost:1917

### Additional commands

Any VITE\_\* properties may be added to a `.env.local` file (not checked in) or used to prefix an npm command.

Runs unit tests with Vitest.

```sh
npm run test
```

Create a production version of the application in the dist folder

```sh
npm run build
```

.. and run it

```sh
npm run serve
```

## Openfin

How to run a web server, to serve the client in OpenFin

```sh
npm run openfin:dev
```

and to run up the RT clients using OpenFin

```sh
npm run openfin:run:<app>
```

where `<app>` is `fx`, `credit`, `launcher`, or `limitchecker`

As a shortcut, to run the local dev server and client in one command, use

```sh
npm run openfin:start:<app>
```

#### Configs

Config files (OpenFin manifests) are located in [./public-openfin](./public-openfin).

Vite will replace placeholders at build time.

#### Troubleshooting

To debug OpenFin windows more easily (using Chromium devtools), check the relevant manifest for the appropriate port in e.g.

```json
    "arguments": "--remote-debugging-port=9092"
```

navigate to [chrome://inspect/#devices](chrome://inspect/#devices) in a Chrome tab

add the address in the dialog you get when you click "Configure ..."

```
http://localhost:<debug-port-from-above>
```

and any running OpenFin windows should be displayed, with Inspect links etc.

### NLP in the OpenFin Launcher and Workspace (below)

The OpenFin Launcher and Workspace Home UI have a search command line interface powered by [DialogFlow](https://cloud.google.com/dialogflow), where you can enter commands like

`buy 10m USDJPY`

For more insight into how NLP works see the diagflow function [doc](https://github.com/AdaptiveConsulting/ReactiveTraderCloud/blob/master/packages/server/cloud/nlp/README.md).

### Workspace

<img src="./public-workspace/images/previews/home.PNG">

Reactive Trader Workspace is a standalone application built on the [Openfin Workspace](https://developers.openfin.co/of-docs/docs/overview-of-workspace) platform.
It is built and deployed as a separate app in the Openfin bucket in Google Cloud Storage (under the subfolder/workspace)

The manifest file is available at:
http://openfin.prod.reactivetrader.com/workspace/config/workspace.json

and at the same `/workspace/config/workspace.json` path on every other (openfin) deployment ..

#### Running Locally

Working with OpenFin workspace locally using the OpenFin CLI ...

`npm run openfin:dev` as above to serve RT apps, views and the workspace platform

`npm run openfin:run:workspace` to launch workspace (when running local dev server, you'll see the "provider" window first)

As a shortcut, to run the local dev server and client in one command, use

```sh
npm run openfin:start:workspace
```

#### Configs

Config files are located in [./public-workspace/config](./public-workspace/config).

Vite will replace placeholders at build time.

[workspace.json](./public-workspace/config/workspace.json) - This is the manifest file Openfin uses to run the workspace provider.

[snapshot.json](./public-workspace/config/snapshot.json) - A workspace window _layout_ or 'snapshot', saved from previous layout modifications - on launching this (from the Home UI) the Trading Workspace will be displayed.

`analytics, live-rates, trades.json` - Basic .json files that contain the bare minimum to launch a view in the Openfin browser using `platform.launchApp`

#### Working with Workspace Data

Workspace config for pages / snapshots is stored in IndexedDB - example below is retrieving a saved workspace snapshot

```javascript
db = indexedDB.open(
  "openfin-workspace-platform-workspaces-adaptive-workspace-provider-local",
  1,
)
db.onsuccess = () => {
  console.log("Success")
  dbResult = db.result
}
db.onerror = () => {
  console.error("BAH")
}

// check what object stores you have under that DB (can also just look in devtools)
dbResult.objectStoreNames

// open transaction, get the object store and grab the key for the saved workspace
// annoyingly you have to do this even to just "look" at the data
data = dbResult
  .transaction("workspaces")
  .objectStore("workspaces")
  .get("fc9cdd93-104c-4305-97fa-92ea5a560546")

console.log(data.result)
```

## Finsemble

How to run a web server, to serve the client in Finsemble

```sh
npm run finsemble:dev
```

The Finsemble platform code (conceptually similar to the Workspace platform above) is in an internal repo .. ask a colleague for details.

## Storybook

How to run local instance of RT storybook

```sh
npm run storybook
```

_Tech Note: Since we are no longer using a middleware, we are able to serve Storybook from root (separate web server entirely from the main RT one) during development but for production, the build is all apart of the same bundle/server from /storybook/ which is handled in `.storybook/main.ts`._

There seems to be some issues with storybook cache on some machines, we can solve it by running it without the cache. We added --no-manager-cache to the storybook script

## End to End testing

How to run e2e tests against the web

```sh
npm start
```

```sh
npm run e2e:web -- --headed --workers=1
```

arguments: --headed (launches a browser visible to the user) and --workers=1 to serialise the tests (use e.g. --workers=2 to run tests in parallel)

How to run e2e tests against openfin

```sh
npm run openfin:start:launcher
```

and launch all of the apps from the launcher

```sh
npm run e2e:openfin -- --workers=1
```

## Progressive Web App or PWA

Reactive Trader can be installed as a progressive web application.

The [service worker](src/client/Web/serviceWorkerRegistration.ts) will need to be running for local development.

The settings for the PWA are configured in [`manifest.json`](public-pwa/manifest.json), plus various settings in index.html `<head>`. All attempts to date to bring iOS splash screens back to life have been fruitless, see [pwa-splash-screens](https://github.com/applification/pwa-splash-screens/blob/master/index.html) for reference.

## Token replacement

The PWA [`manifest.json`](public-pwa/manifest.json) file and the [OpenFin manifests](public-openfin) contain tokens in the form `<BLAH>` that are replaced at build time with environment-specific values (e.g. the application name may have an environment suffix).
This is either driven by config/logic in the [workflow files](../../.github/workflows) or constants/logic in the vite build.

## Deployment

Automatic branch, PR and Dev deployment (from master branch) is through [GitHub Actions](../../.github/workflows).

Actions also make UAT (branch) and Prod (tag) builds available on Google Cloud.

```

### File: packages\client\install\README.md
```md
# Installers

Reactive Trader® supports multiple desktop platforms, including [OpenFin](https://www.openfin.co/), now known by the brand name **Here&trade;** and [Finsemble](https://documentation.finsemble.com/) now known under the product name [io.connect](https://interop.io/products/io-connect/).

Below you can find links to the installers for the various platforms.

## OpenFin

### Reactive Workspace

Generate (best, to be up-to-date) or Download the appropriate `.exe`/`.pkg` installer below

> _**Demo** Windows / Mac unless you are developing & testing Reactive Trader_.

This will install the OpenFin RVM, Runtime and Reactive Workspace app on to your desktop, including Reactive Trader® components and workspaces.

| Environment | Windows                                                                                                                                 | Mac                                                                                                                                         |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Demo        | [Generate][rw-demo] / [Download](https://storage.googleapis.com/reactive-trader-openfin-installers/workspace/Reactive-Workspace.exe)    | [Generate][rw-demo-mac] / [Download](https://storage.googleapis.com/reactive-trader-openfin-installers/workspace/Reactive-Workspace.pkg)    |
| UAT         | [Generate][rw-uat] / [Download](https://storage.googleapis.com/reactive-trader-openfin-installers/workspace/Reactive-Workspace-UAT.exe) | [Generate][rw-uat-mac] / [Download](https://storage.googleapis.com/reactive-trader-openfin-installers/workspace/Reactive-Workspace-UAT.pkg) |
| Dev         | [Generate][rw-dev] / [Download](https://storage.googleapis.com/reactive-trader-openfin-installers/workspace/Reactive-Workspace-Dev.exe) | [Generate][rw-dev-mac] / [Download](https://storage.googleapis.com/reactive-trader-openfin-installers/workspace/Reactive-Workspace-Dev.pkg) |

[rw-demo]: https://install.openfin.co/download/?os=win&config=https%3A%2F%2Fopenfin.prod.reactivetrader.com%2Fworkspace%2Fconfig%2Fworkspace.json&fileName=Reactive-Workspace&unzipped=true
[rw-uat]: https://install.openfin.co/download/?os=win&config=https%3A%2F%2Fopenfin.uat.reactivetrader.com%2Fworkspace%2Fconfig%2Fworkspace.json&fileName=Reactive-Workspace-UAT&unzipped=true
[rw-dev]: https://install.openfin.co/download/?os=win&config=https%3A%2F%2Fopenfin.dev.reactivetrader.com%2Fworkspace%2Fconfig%2Fworkspace.json&fileName=Reactive-Workspace-Dev&unzipped=true
[rw-demo-mac]: https://install.openfin.co/download/?os=osx&config=https%3A%2F%2Fopenfin.prod.reactivetrader.com%2Fworkspace%2Fconfig%2Fworkspace.json&fileName=Reactive-Workspace&iconFile=https%3A%2F%2Fopenfin.prod.reactivetrader.com%2Fstatic%2Fmedia%2Fadaptive-icon-256x256.png&appName=Reactive%20Workspace&notarize=true
[rw-uat-mac]: https://install.openfin.co/download/?os=osx&config=https%3A%2F%2Fopenfin.uat.reactivetrader.com%2Fworkspace%2Fconfig%2Fworkspace.json&fileName=Reactive-Workspace-UAT&iconFile=https%3A%2F%2Fopenfin.uat.reactivetrader.com%2Fstatic%2Fmedia%2Fadaptive-icon-256x256.png&appName=Reactive%20Workspace%20UAT&notarize=true
[rw-dev-mac]: https://install.openfin.co/download/?os=osx&config=https%3A%2F%2Fopenfin.dev.reactivetrader.com%2Fworkspace%2Fconfig%2Fworkspace.json&fileName=Reactive-Workspace-Dev&iconFile=https%3A%2F%2Fopenfin.dev.reactivetrader.com%2Fstatic%2Fmedia%2Fadaptive-icon-256x256.png&appName=Reactive%20Workspace%20Dev&notarize=true

### Reactive Launcher

Generate (best, to be up-to-date) or Download the appropriate `.exe`/`.pkg` installer below.

> _**Demo** Windows / Mac unless you are developing & testing Reactive Trader_.
>
> This will install the OpenFin RVM, Runtime and Reactive Launcher (OpenFin Platform) app on to your desktop, including Reactive Trader® components.

| Environment | Windows                                                                                                                                   | Mac                                                                                                                                       |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Demo        | [Generate][rl-demo-win] / [Download](https://storage.googleapis.com/reactive-trader-openfin-installers/launcher/Reactive-Launcher.exe)    | [Generate][rl-demo-mac] / [Download](https://storage.googleapis.com/reactive-trader-openfin-installers/launcher/Reactive-Launcher.pkg)    |
| UAT         | [Generate][rl-uat-win] / [Download](https://storage.googleapis.com/reactive-trader-openfin-installers/launcher/Reactive-Launcher-UAT.exe) | [Generate][rl-uat-mac] / [Download](https://storage.googleapis.com/reactive-trader-openfin-installers/launcher/Reactive-Launcher-UAT.pkg) |
| Dev         | [Generate][rl-dev-win] / [Download](https://storage.googleapis.com/reactive-trader-openfin-installers/launcher/Reactive-Launcher-Dev.exe) | [Generate][rl-dev-mac] / [Download](https://storage.googleapis.com/reactive-trader-openfin-installers/launcher/Reactive-Launcher-Dev.pkg) |

[rl-demo-win]: https://install.openfin.co/download/?os=win&config=https%3A%2F%2Fopenfin.prod.reactivetrader.com%2Fconfig%2Flauncher.json&fileName=Reactive-Launcher&unzipped=true
[rl-uat-win]: https://install.openfin.co/download/?os=win&config=https%3A%2F%2Fopenfin.uat.reactivetrader.com%2Fconfig%2Flauncher.json&fileName=Reactive-Launcher-UAT&unzipped=true
[rl-dev-win]: https://install.openfin.co/download/?os=win&config=https%3A%2F%2Fopenfin.dev.reactivetrader.com%2Fconfig%2Flauncher.json&fileName=Reactive-Launcher-Dev&unzipped=true
[rl-demo-mac]: https://install.openfin.co/download/?os=osx&config=https%3A%2F%2Fopenfin.prod.reactivetrader.com%2Fconfig%2Flauncher.json&fileName=Reactive-Launcher&iconFile=https%3A%2F%2Fopenfin.prod.reactivetrader.com%2Fstatic%2Fmedia%2Fadaptive-icon-256x256.png&appName=Reactive%20Launcher&notarize=true
[rl-uat-mac]: https://install.openfin.co/download/?os=osx&config=https%3A%2F%2Fopenfin.uat.reactivetrader.com%2Fconfig%2Flauncher.json&fileName=Reactive-Launcher-UAT&iconFile=https%3A%2F%2Fopenfin.uat.reactivetrader.com%2Fstatic%2Fmedia%2Fadaptive-icon-256x256.png&appName=Reactive%20Launcher%20UAT&notarize=true
[rl-dev-mac]: https://install.openfin.co/download/?os=osx&config=https%3A%2F%2Fopenfin.dev.reactivetrader.com%2Fconfig%2Flauncher.json&fileName=Reactive-Launcher-Dev&iconFile=https%3A%2F%2Fopenfin.dev.reactivetrader.com%2Fstatic%2Fmedia%2Fadaptive-icon-256x256.png&appName=Reactive%20Launcher%20Dev&notarize=true

## Finsemble Toolbar (Windows Only)

Download and run the exe below to install the integrated toolbar on your desktop, including Reactive Trader® components and workspaces.

| Environment | Windows               |
| ----------- | --------------------- |
| Demo        | [Download][fsbl-demo] |
| UAT         | [Download][fsbl-uat]  |

[fsbl-demo]: https://storage.googleapis.com/reactive-trader-finsemble/pkg/ReactiveTraderFinsemble.exe
[fsbl-uat]: https://storage.googleapis.com/reactive-trader-finsemble-uat/pkg/ReactiveTraderFinsemble-UAT.exe

```

### File: FETCHED_ReactiveTraderCloud_033152\packages\client\install\README.md
```md
# Installers

Reactive Trader® supports multiple desktop platforms, including [OpenFin](https://www.openfin.co/), now known by the brand name **Here&trade;** and [Finsemble](https://documentation.finsemble.com/) now known under the product name [io.connect](https://interop.io/products/io-connect/).

Below you can find links to the installers for the various platforms.

## OpenFin

### Reactive Workspace

Generate (best, to be up-to-date) or Download the appropriate `.exe`/`.pkg` installer below

> _**Demo** Windows / Mac unless you are developing & testing Reactive Trader_.

This will install the OpenFin RVM, Runtime and Reactive Workspace app on to your desktop, including Reactive Trader® components and workspaces.

| Environment | Windows                                                                                                                                 | Mac                                                                                                                                         |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Demo        | [Generate][rw-demo] / [Download](https://storage.googleapis.com/reactive-trader-openfin-installers/workspace/Reactive-Workspace.exe)    | [Generate][rw-demo-mac] / [Download](https://storage.googleapis.com/reactive-trader-openfin-installers/workspace/Reactive-Workspace.pkg)    |
| UAT         | [Generate][rw-uat] / [Download](https://storage.googleapis.com/reactive-trader-openfin-installers/workspace/Reactive-Workspace-UAT.exe) | [Generate][rw-uat-mac] / [Download](https://storage.googleapis.com/reactive-trader-openfin-installers/workspace/Reactive-Workspace-UAT.pkg) |
| Dev         | [Generate][rw-dev] / [Download](https://storage.googleapis.com/reactive-trader-openfin-installers/workspace/Reactive-Workspace-Dev.exe) | [Generate][rw-dev-mac] / [Download](https://storage.googleapis.com/reactive-trader-openfin-installers/workspace/Reactive-Workspace-Dev.pkg) |

[rw-demo]: https://install.openfin.co/download/?os=win&config=https%3A%2F%2Fopenfin.prod.reactivetrader.com%2Fworkspace%2Fconfig%2Fworkspace.json&fileName=Reactive-Workspace&unzipped=true
[rw-uat]: https://install.openfin.co/download/?os=win&config=https%3A%2F%2Fopenfin.uat.reactivetrader.com%2Fworkspace%2Fconfig%2Fworkspace.json&fileName=Reactive-Workspace-UAT&unzipped=true
[rw-dev]: https://install.openfin.co/download/?os=win&config=https%3A%2F%2Fopenfin.dev.reactivetrader.com%2Fworkspace%2Fconfig%2Fworkspace.json&fileName=Reactive-Workspace-Dev&unzipped=true
[rw-demo-mac]: https://install.openfin.co/download/?os=osx&config=https%3A%2F%2Fopenfin.prod.reactivetrader.com%2Fworkspace%2Fconfig%2Fworkspace.json&fileName=Reactive-Workspace&iconFile=https%3A%2F%2Fopenfin.prod.reactivetrader.com%2Fstatic%2Fmedia%2Fadaptive-icon-256x256.png&appName=Reactive%20Workspace&notarize=true
[rw-uat-mac]: https://install.openfin.co/download/?os=osx&config=https%3A%2F%2Fopenfin.uat.reactivetrader.com%2Fworkspace%2Fconfig%2Fworkspace.json&fileName=Reactive-Workspace-UAT&iconFile=https%3A%2F%2Fopenfin.uat.reactivetrader.com%2Fstatic%2Fmedia%2Fadaptive-icon-256x256.png&appName=Reactive%20Workspace%20UAT&notarize=true
[rw-dev-mac]: https://install.openfin.co/download/?os=osx&config=https%3A%2F%2Fopenfin.dev.reactivetrader.com%2Fworkspace%2Fconfig%2Fworkspace.json&fileName=Reactive-Workspace-Dev&iconFile=https%3A%2F%2Fopenfin.dev.reactivetrader.com%2Fstatic%2Fmedia%2Fadaptive-icon-256x256.png&appName=Reactive%20Workspace%20Dev&notarize=true

### Reactive Launcher

Generate (best, to be up-to-date) or Download the appropriate `.exe`/`.pkg` installer below.

> _**Demo** Windows / Mac unless you are developing & testing Reactive Trader_.
>
> This will install the OpenFin RVM, Runtime and Reactive Launcher (OpenFin Platform) app on to your desktop, including Reactive Trader® components.

| Environment | Windows                                                                                                                                   | Mac                                                                                                                                       |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Demo        | [Generate][rl-demo-win] / [Download](https://storage.googleapis.com/reactive-trader-openfin-installers/launcher/Reactive-Launcher.exe)    | [Generate][rl-demo-mac] / [Download](https://storage.googleapis.com/reactive-trader-openfin-installers/launcher/Reactive-Launcher.pkg)    |
| UAT         | [Generate][rl-uat-win] / [Download](https://storage.googleapis.com/reactive-trader-openfin-installers/launcher/Reactive-Launcher-UAT.exe) | [Generate][rl-uat-mac] / [Download](https://storage.googleapis.com/reactive-trader-openfin-installers/launcher/Reactive-Launcher-UAT.pkg) |
| Dev         | [Generate][rl-dev-win] / [Download](https://storage.googleapis.com/reactive-trader-openfin-installers/launcher/Reactive-Launcher-Dev.exe) | [Generate][rl-dev-mac] / [Download](https://storage.googleapis.com/reactive-trader-openfin-installers/launcher/Reactive-Launcher-Dev.pkg) |

[rl-demo-win]: https://install.openfin.co/download/?os=win&config=https%3A%2F%2Fopenfin.prod.reactivetrader.com%2Fconfig%2Flauncher.json&fileName=Reactive-Launcher&unzipped=true
[rl-uat-win]: https://install.openfin.co/download/?os=win&config=https%3A%2F%2Fopenfin.uat.reactivetrader.com%2Fconfig%2Flauncher.json&fileName=Reactive-Launcher-UAT&unzipped=true
[rl-dev-win]: https://install.openfin.co/download/?os=win&config=https%3A%2F%2Fopenfin.dev.reactivetrader.com%2Fconfig%2Flauncher.json&fileName=Reactive-Launcher-Dev&unzipped=true
[rl-demo-mac]: https://install.openfin.co/download/?os=osx&config=https%3A%2F%2Fopenfin.prod.reactivetrader.com%2Fconfig%2Flauncher.json&fileName=Reactive-Launcher&iconFile=https%3A%2F%2Fopenfin.prod.reactivetrader.com%2Fstatic%2Fmedia%2Fadaptive-icon-256x256.png&appName=Reactive%20Launcher&notarize=true
[rl-uat-mac]: https://install.openfin.co/download/?os=osx&config=https%3A%2F%2Fopenfin.uat.reactivetrader.com%2Fconfig%2Flauncher.json&fileName=Reactive-Launcher-UAT&iconFile=https%3A%2F%2Fopenfin.uat.reactivetrader.com%2Fstatic%2Fmedia%2Fadaptive-icon-256x256.png&appName=Reactive%20Launcher%20UAT&notarize=true
[rl-dev-mac]: https://install.openfin.co/download/?os=osx&config=https%3A%2F%2Fopenfin.dev.reactivetrader.com%2Fconfig%2Flauncher.json&fileName=Reactive-Launcher-Dev&iconFile=https%3A%2F%2Fopenfin.dev.reactivetrader.com%2Fstatic%2Fmedia%2Fadaptive-icon-256x256.png&appName=Reactive%20Launcher%20Dev&notarize=true

## Finsemble Toolbar (Windows Only)

Download and run the exe below to install the integrated toolbar on your desktop, including Reactive Trader® components and workspaces.

| Environment | Windows               |
| ----------- | --------------------- |
| Demo        | [Download][fsbl-demo] |
| UAT         | [Download][fsbl-uat]  |

[fsbl-demo]: https://storage.googleapis.com/reactive-trader-finsemble/pkg/ReactiveTraderFinsemble.exe
[fsbl-uat]: https://storage.googleapis.com/reactive-trader-finsemble-uat/pkg/ReactiveTraderFinsemble-UAT.exe

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

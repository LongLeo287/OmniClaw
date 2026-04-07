---
id: books
type: knowledge
owner: OA_Triage
---
# books
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "frappe-books",
  "version": "0.37.0",
  "description": "Simple book-keeping app for everyone",
  "author": {
    "name": "Frappe Technologies Pvt. Ltd.",
    "email": "hello@frappe.io"
  },
  "scripts": {
    "dev": "node build/scripts/dev.mjs",
    "build": "node build/scripts/build.mjs",
    "release": "scripts/publish-mac-arm.sh",
    "postinstall": "electron-rebuild",
    "postuninstall": "electron-rebuild",
    "script:translate": "scripts/runner.sh scripts/generateTranslations.ts",
    "script:profile": "scripts/profile.sh",
    "test": "scripts/test.sh",
    "uitest": "node uitest/index.mjs | tap-spec",
    "lint": "eslint . --ext ts,vue",
    "format": "prettier --write ."
  },
  "dependencies": {
    "@codemirror/autocomplete": "^6.4.2",
    "@codemirror/lang-vue": "^0.1.1",
    "@popperjs/core": "^2.10.2",
    "better-sqlite3": "^9.2.2",
    "bree": "^9.2.4",
    "codemirror": "^6.0.1",
    "core-js": "^3.19.0",
    "electron-store": "^8.0.1",
    "feather-icons": "^4.28.0",
    "knex": "^2.4.0",
    "lodash": "^4.17.23",
    "luxon": "^2.5.2",
    "node-fetch": "2",
    "pesa": "^1.1.12",
    "source-map-support": "^0.5.21",
    "vue": "^3.2.40",
    "vue-router": "^4.0.12"
  },
  "devDependencies": {
    "@codemirror/language": "^6.0.0",
    "@codemirror/state": "^6.0.0",
    "@codemirror/view": "^6.0.0",
    "@electron/rebuild": "^3.4.1",
    "@lezer/common": "^1.0.0",
    "@types/assert": "^1.5.6",
    "@types/better-sqlite3": "^7.6.4",
    "@types/electron-devtools-installer": "^2.2.0",
    "@types/lodash": "^4.14.179",
    "@types/luxon": "^2.3.1",
    "@types/node": "^17.0.23",
    "@types/node-fetch": "^2.6.1",
    "@types/tape": "^4.13.2",
    "@typescript-eslint/eslint-plugin": "5.60.0",
    "@typescript-eslint/parser": "5.60.0",
    "@vitejs/plugin-vue": "^4.2.3",
    "autoprefixer": "^9",
    "chokidar": "^3.5.3",
    "dotenv": "^16.0.0",
    "electron": "22.3.27",
    "electron-builder": "^24.9.1",
    "electron-devtools-installer": "^3.2.0",
    "electron-updater": "^6.3.0",
    "eslint": "^8.43.0",
    "eslint-config-prettier": "^8.3.0",
    "eslint-plugin-prettier": "^4.0.0",
    "eslint-plugin-vue": "^9.15.0",
    "execa": "^7.1.1",
    "fs-extra": "^11.1.1",
    "playwright": "^1.55.1",
    "postcss": "^8",
    "prettier": "^2.4.1",
    "tailwindcss": "npm:@tailwindcss/postcss7-compat",
    "tailwindcss-rtl": "^0.9.0",
    "tap-spec": "^5.0.0",
    "tape": "^5.6.1",
    "ts-node": "^10.7.0",
    "tsconfig-paths": "^3.14.1",
    "tslib": "^2.3.1",
    "typescript": "^4.6.2",
    "vite": "^5.4.21",
    "vue-tsc": "^1.6.5",
    "yargs": "^17.7.2"
  },
  "resolutions": {
    "node-abi": "^3.54.0"
  },
  "prettier": {
    "semi": true,
    "singleQuote": true,
    "trailingComma": "es5"
  },
  "homepage": "https://frappe.io/books",
  "repository": {
    "url": "https://github.com/frappe/books"
  },
  "license": "AGPL-3.0-only"
}

```

### File: README.md
```md
<div align="center" markdown="1">
<br/>

<img src="https://frappe.io/files/books.png" alt="Frappe Books logo" width="80"/>

<br/>

<h1>Frappe Books</h1>

**Modern Accounting Made Simple**

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/frappe/books)](https://github.com/frappe/books/releases)
![Platforms](https://img.shields.io/badge/platform-mac%2C%20windows%2C%20linux-yellowgreen)
[![Publish](https://github.com/frappe/books/actions/workflows/publish.yml/badge.svg)](https://github.com/frappe/books/actions/workflows/publish.yml)

</div>

<div align="center">
<img src="https://user-images.githubusercontent.com/29507195/207267857-4ae48890-3fb2-4046-80cf-3256b46c72a0.png" alt="Frappe Books Preview"/>
</div>
<br />
<div align="center">
	<a href="https://frappe.io/books">Website</a>
	-
	<a href="https://docs.frappe.io/books">Documentation</a>
</div>

## Frappe Books

Frappe Books is an open-source accounting software aimed at simplifying financial management for businesses. With its clean and user-friendly interface, it streamlines accounting tasks for small and medium-sized enterprises, offering a seamless solution for modern businesses to manage their finances with ease.

<details>
<summary>Screenshots</summary>
<br/>
<img  alt="Pos" src="https://github.com/user-attachments/assets/f75116b4-cf5f-45ee-9927-ba380fa56a46" />
    <br/><br/>
    <img  alt="General Ledger" src="https://github.com/user-attachments/assets/58d8bcdf-1576-4008-b010-7054fb64a12d" />
    <br/><br/>
    <img  alt="Profit and Loss" src="https://github.com/user-attachments/assets/11bd67d1-d808-496b-ac4d-ef68c18b9419" />

</details>

### Motivation

Frappe Books addresses a market gap where small businesses face expensive, complex accounting tools. It offers an intuitive, open-source solution that combines simplicity with essential features, empowering businesses to manage finances effectively—even offline.

### Key Features

- **Dashboard**: Provides an overview of key financial data and performance metrics.
- **Point of Sale**: Simplifies retail transactions with an integrated POS system for easy sales processing.
- **Works Offline**: Enables users to continue working without an internet connection and sync later.
- **Double-entry accounting**: Ensures accurate financial tracking by recording each transaction in two accounts.
- **Entries**
  - **Invoicing**: Allows businesses to create and manage professional invoices effortlessly.
  - **Billing**: Billing processes by generating bills and tracking payments.
  - **Payments**: Records and tracks payments received and made.
  - **Journal Entries**: Records financial transactions in the general ledger with detailed notes and adjustments.
- **Financial Reports**
  - **General Ledger**: Centralized record of all financial transactions, providing a comprehensive view of accounts.
  - **Profit and Loss Statement**: Summarizes revenues, costs, and expenses to show business profitability.
  - **Balance Sheet**: Displays a company’s assets, liabilities, and equity at a specific point in time.
  - **Trial Balance**: Verifies the accuracy of accounting records by ensuring that debits and credits are balanced.
    <br/>

### Under the Hood

- **Vue.js**: In Frappe Books, Vue.js powers the front-end, enabling a reactive and component-based UI. It ensures seamless interactions and dynamic updates, giving users a modern, responsive experience.

- **Electron**: Electron is used to package Frappe Books as a standalone desktop application, allowing it to run offline and provide a native-like experience across Windows, macOS, and Linux.

- **SQLite**: Frappe Books uses SQLite as its local database. All financial data, transactions, and configurations are stored securely in an SQLite file on the user's machine.

## Production Setup

### Manual

Download and install the latest release for your platform from the [releases
page](https://github.com/frappe/books/releases) .

### Using Homebrew (for MacOS and Linux)

```zsh
brew install --cask frappe-books
```

### Via Flatpak (Linux)

<a href='https://flathub.org/apps/io.frappe.books'>
    <img width='120' alt='Get it on Flathub' src='https://flathub.org/api/badge?locale=en'/>
</a>

## Development Setup

### Pre-requisites

To get the dev environment up and running you need to first set up Node.js `v20.18.1` and npm. For this, we suggest using
[nvm](https://github.com/nvm-sh/nvm#installing-and-updating).

Next, you will need to install [yarn](https://classic.yarnpkg.com/lang/en/docs/install/#mac-stable).

### Clone and Run

Once you are through the Pre-requisites, you can run the following commands to
setup Frappe Books for development and building:

```bash
# clone the repository
git clone https://github.com/frappe/books.git

# change directory
cd books

# install dependencies
yarn
```

To run Frappe Books in development mode (with hot reload, etc):

```bash
# start the electron app
yarn dev
```

**Note: First Boot**

When you run `yarn dev` electron will run immediately but the UI will take a
couple of seconds to render this because of how dev mode works. Each file is
individually served by the dev server. And there are many files that have to be
sent.

**Note: Debug Electron Main Process**

When in dev mode electron runs with the `--inspect` flag which allows an
external debugger to connect to port 5858. You can use chrome for this by
visiting `chrome://inspect` while Frappe Books is running in dev mode.

See more [here](https://www.electronjs.org/docs/latest/tutorial/debugging-main-process#external-debuggers).

#### Build

To build Frappe Books and create an installer:

```bash
# start the electron app
yarn build
```

**Note: Build Target**
By default the above command will build for your computer's operating system and
architecture. To build for other environments (example: for linux from a windows
computer) check the _Building_ section at
[electron.build/cli](https://www.electron.build/cli).

So to build for linux you could use the `--linux` flag like so: `yarn build --linux`.

## Want to Just Try Out or Contribute?

If you want to contribute to Frappe Books, please check our [Contribution Guidelines](https://github.com/frappe/books/blob/master/.github/CONTRIBUTING.md). There are many ways you can contribute even if you don't code:

1. If you find any issues, no matter how small (even typos), you can [raise an issue](https://github.com/frappe/books/issues/new) to inform us.
2. You can help us with language support by [contributing translations](https://github.com/frappe/books/wiki/Contributing-Translations).
3. If you're an ardent user you can tell us what you would like to see.
4. If you have accounting requirements, you can become an ardent user. 🙂

If you want to contribute code then you can fork this repo, make changes and raise a PR. ([see how to](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork))

## Translation Contributors

| Language              | Contributors                                                                                                                                                                                                                                      |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Arabic                | [taha2002](https://github.com/taha2002), [Faridget](https://github.com/faridget), [Osama Muhammed](https://github.com/osama1998H)                                                                                                                 |
| Albanian              | [xoniks](https://github.com/xoniks)                                                                                                                                                                                                               |
| Catalan               | Dídac E. Jiménez                                                                                                                                                                                                                                  |
| Chinese - Simplified  | [wcxu21](https://github.com/wcxu21), [wolone](https://github.com/wolone), [Ji Qu](https://github.com/winkidney)                                                                                                                                   |
| Chinese - Traditional | [Ethan Deng](https://github.com/ethandengs)                                                                                                                                                                                                       |
| Danish                | [Tummas Joensen](https://github.com/slang123)                                                                                                                                                                                                     |
| Dutch                 | [RijckAlex](https://github.com/RijckAlex), [Stan M](https://github.com/stxm)                                                                                                                                                                      |
| French                | [DeepL](https://www.deepl.com/), [mael-chouteau](https://github.com/mael-chouteau), [joandreux](https://github.com/joandreux)                                                                                                                     |
| German                | [DeepL](https://www.deepl.com/), [barredterra](https://github.com/barredterra), [promexio](https://github.com/promexio), [C2H6-383](https://github.com/C2H6-383), [0xflotus](https://github.com/0xflotus), [Tim](https://github.com/Rocket-Quack) |
| Gujarati              | [dhruvilxcode](https://github.com/dhruvilxcode), [4silvertooth](https://github.com/4silvertooth)                                                                                                                                                  |
| Hindi                 | [bnsinghgit](https://github.com/bnsinghgit)                                                                                                                                                                                                       |
| Indonesian            | [Aji Prakoso](https://github.com/jipraks)                                                                                                                                                                                                         |
| Korean                | [Isaac-Kwon](https://github.com/Isaac-Kwon)                                                                                                                                                                                                       |
| Portuguese            | [DeepL](https://www.deepl.com/), [Valdir Amaral](https://github.com/valdir-amaral)                                                                                                                                                                |
| Spanish               | [talmax1124](https://github.com/talmax1124), [delbertf](https://github.com/delbertf), [Ignacio Chemes](https://github.com/ignaciochemes)                                                                                                          |
| Swedish               | [papplo](https://github.com/papplo), [Crims-on](https://github.com/Crims-on)                                                                                                                                                                      |
| Turkish               | Eyuq, [XTechnology-TR](https://github.com/XTechnology-TR)                                                                                                                                                                                         |

## Learn and connect

- [Telegram Group](https://t.me/frappebooks): Used for discussions and decisions regarding everything Frappe Books.
- [GitHub Discussions](https://github.com/frappe/books/discussions): Used for discussions around a specific topic.
- [Documentation](https://docs.frappe.io/books): Official documentation for more details.

```

### File: src\README.md
```md
# src

This is where all the frontend code lives

## Fyo Initialization

The initialization flows are different when the instance is new or is existing.
All of them are triggered from `src/App.vue`.

**New Instance**

1. Run _Setup Wizard_ for init values (eg: `country`).
2. Call `setupInstance.ts/setupInstance` using init values.

**Existing Instance**

1. Connect to db.
2. Check if _Setup Wizard_ has been completed, if not, jump to **New Instance**
3. Call `initFyo/initializeInstance` with `dbPath` and `countryCode`

## Global Fyo

Global fyo is exported from `initFyo.ts`. Only code that isn't going to be unit
tested using `mocha` should use this, i.e. code in `src`

```

### File: .eslintrc.js
```js
module.exports = {
  root: true,
  env: {
    node: true,
    browser: true,
    es2018: true,
  },
  rules: {
    'no-console': 'warn',
    'no-debugger': 'warn',
    'arrow-body-style': 'off',
    'prettier/prettier': 'warn',
    'prefer-arrow-callback': 'warn',
    'vue/no-mutating-props': 'off',
    'vue/multi-word-component-names': 'off',
    'vue/no-useless-template-attributes': 'off',
    'vue/one-component-per-file': 'off',
    'vue/no-reserved-component-names': 'off',
    '@typescript-eslint/ban-ts-comment': 'off',
    '@typescript-eslint/no-var-requires': 'off',
    '@typescript-eslint/no-non-null-assertion': 'off',
    '@typescript-eslint/no-floating-promises': 'warn',
    '@typescript-eslint/no-misused-promises': 'warn',
  },
  parser: 'vue-eslint-parser',
  parserOptions: {
    parser: '@typescript-eslint/parser',
    project: true,
    tsconfigRootDir: __dirname,
    sourceType: 'module',
    extraFileExtensions: ['.vue'],
  },
  plugins: ['@typescript-eslint', 'prettier'],
  extends: [
    'plugin:vue/vue3-recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:@typescript-eslint/recommended-requiring-type-checking',
    'plugin:prettier/recommended',
  ],
  overrides: [
    {
      files: ['*.vue'],
      rules: {
        '@typescript-eslint/no-misused-promises': 'off',
        '@typescript-eslint/no-unsafe-assignment': 'off',
        '@typescript-eslint/no-unsafe-member-access': 'off',
        '@typescript-eslint/no-unsafe-call': 'off',
      },
    },
  ],
  ignorePatterns: [
    '*.mjs',
    'uitest',
    '.eslintrc.js',
    'tailwind.config.js',
    'node_modules',
    'dist_electron',
    '*.spec.ts',
    'vite.config.ts',
    'postcss.config.js',
    'src/components/**/*.vue', // Incrementally fix these
    'electron-builder.ts',
  ],
};

```

### File: colors.json
```json
{
  "black": "#1E293B",
  "gray": {
    "25": "#FBFBFB",
    "50": "#F8F8F8",
    "100": "#F3F3F3",
    "200": "#EDEDED",
    "300": "#E2E2E2",
    "400": "#C7C7C7",
    "500": "#999999",
    "600": "#7C7C7C",
    "700": "#525252",
    "800": "#383838",
    "850": "#282828",
    "875": "#212121",
    "890": "#1C1C1C",
    "900": "#171717"
  },
  "red": {
    "50": "#FFF7F7",
    "100": "#FFF0F0",
    "200": "#FCD7D7",
    "300": "#F9C6C6",
    "400": "#EB9091",
    "500": "#E03636",
    "600": "#CC2929",
    "700": "#B52A2A",
    "800": "#941F1F",
    "900": "#6B1515"
  },
  "orange": {
    "50": "#FFF9F5",
    "100": "#FFF1E7",
    "200": "#FCE6D5",
    "300": "#F7D6BD",
    "400": "#F0B58B",
    "500": "#E86C13",
    "600": "#D45A08",
    "700": "#BD3E0C",
    "800": "#9E3513",
    "900": "#6B2711"
  },
  "yellow": {
    "50": "#FFFCEF",
    "100": "#FFF7D3",
    "200": "#F7E9A8",
    "300": "#F5E171",
    "400": "#F2D14B",
    "500": "#EDBA13",
    "600": "#D1930D",
    "700": "#AB6E05",
    "800": "#8C5600",
    "900": "#733F12"
  },
  "green": {
    "50": "#F3FCF5",
    "100": "#E4F5E9",
    "200": "#DAF0E1",
    "300": "#CAE5D4",
    "400": "#B6DEC5",
    "500": "#59BA8B",
    "600": "#30A66D",
    "700": "#278F5E",
    "800": "#16794C",
    "900": "#173B2C"
  },
  "teal": {
    "50": "#F0FDFA",
    "100": "#E6F7F4",
    "200": "#BAE8E1",
    "300": "#97DED4",
    "400": "#73D1C4",
    "500": "#36BAAD",
    "600": "#0B9E92",
    "700": "#0F736B",
    "800": "#115C57",
    "900": "#114541"
  },
  "blue": {
    "50": "#F7FBFD",
    "100": "#EDF6FD",
    "200": "#E3F1FD",
    "300": "#C9E7FC",
    "400": "#70B6F0",
    "500": "#33A1FF",
    "600": "#007BE0",
    "700": "#0070CC",
    "800": "#005CA3",
    "900": "#004880"
  },
  "indigo": {
    "100": "#ebf4ff",
    "200": "#c3dafe",
    "300": "#a3bffa",
    "400": "#7f9cf5",
    "500": "#667eea",
    "600": "#5a67d8",
    "700": "#4c51bf",
    "800": "#434190",
    "900": "#3c366b"
  },
  "purple": {
    "50": "#FDFAFF",
    "100": "#F9F0FF",
    "200": "#F1E5FA",
    "300": "#E9D6F5",
    "400": "#D6C1E6",
    "500": "#9C45E3",
    "600": "#8642C2",
    "700": "#6E399D",
    "800": "#5C2F83",
    "900": "#401863"
  },
  "pink": {
    "50": "#FFF7FC",
    "100": "#FEEEF8",
    "200": "#F8E2F0",
    "300": "#F2D4E6",
    "400": "#E9C4DA",
    "500": "#DF9EB8",
    "600": "#CF3A96",
    "700": "#9C2671",
    "800": "#801458",
    "900": "#570F3E"
  },
  "violet": {
    "50": "#FBFAFF",
    "100": "#F5F2FF",
    "200": "#E5E1FA",
    "300": "#DAD2F7",
    "400": "#BDB1F0",
    "500": "#6846E3",
    "600": "#5F46C7",
    "700": "#4F3DA1",
    "800": "#392980",
    "900": "#251959"
  },
  "cyan": {
    "50": "#F5FBFC",
    "100": "#E0F8FF",
    "200": "#B3ECFC",
    "300": "#94E6FF",
    "400": "#6BD3F2",
    "500": "#34BAE3",
    "600": "#32A4C7",
    "700": "#267A94",
    "800": "#125C73",
    "900": "#164759"
  },
  "amber": {
    "50": "#FDFAED",
    "100": "#FCF3CF",
    "200": "#F7E28D",
    "300": "#F5D261",
    "400": "#F2BE3A",
    "500": "#E79913",
    "600": "#DB7706",
    "700": "#B35309",
    "800": "#91400D",
    "900": "#763813"
  }
}

```

### File: main.ts
```ts
// eslint-disable-next-line
require('source-map-support').install({
  handleUncaughtException: false,
  environment: 'node',
});

import { emitMainProcessError } from 'backend/helpers';
import {
  app,
  BrowserWindow,
  BrowserWindowConstructorOptions,
  protocol,
  ProtocolRequest,
  ProtocolResponse,
} from 'electron';
import { autoUpdater } from 'electron-updater';
import fs from 'fs';
import path from 'path';
import registerAppLifecycleListeners from './main/registerAppLifecycleListeners';
import registerAutoUpdaterListeners from './main/registerAutoUpdaterListeners';
import registerIpcMainActionListeners from './main/registerIpcMainActionListeners';
import registerIpcMainMessageListeners from './main/registerIpcMainMessageListeners';
import registerProcessListeners from './main/registerProcessListeners';

export class Main {
  title = 'Frappe Books';
  icon: string;

  winURL = '';
  checkedForUpdate = false;
  mainWindow: BrowserWindow | null = null;

  WIDTH = 1200;
  HEIGHT = process.platform === 'win32' ? 826 : 800;

  constructor() {
    this.icon = this.isDevelopment
      ? path.resolve('./build/icon.png')
      : path.join(__dirname, 'icons', '512x512.png');

    protocol.registerSchemesAsPrivileged([
      { scheme: 'app', privileges: { secure: true, standard: true } },
    ]);

    if (this.isDevelopment) {
      autoUpdater.logger = console;
    }

    // https://github.com/electron-userland/electron-builder/issues/4987
    app.commandLine.appendSwitch('disable-http2');
    autoUpdater.requestHeaders = {
      'Cache-Control':
        'no-store, no-cache, must-revalidate, proxy-revalidate, max-age=0',
    };

    this.registerListeners();
    if (this.isMac && this.isDevelopment) {
      app.dock.setIcon(this.icon);
    }
  }

  get isDevelopment() {
    return process.env.NODE_ENV === 'development';
  }

  get isTest() {
    return !!process.env.IS_TEST;
  }

  get isMac() {
    return process.platform === 'darwin';
  }

  get isLinux() {
    return process.platform === 'linux';
  }

  registerListeners() {
    registerIpcMainMessageListeners(this);
    registerIpcMainActionListeners(this);
    registerAutoUpdaterListeners(this);
    registerAppLifecycleListeners(this);
    registerProcessListeners(this);
  }

  getOptions(): BrowserWindowConstructorOptions {
    const preload = path.join(__dirname, 'main', 'preload.js');
    const options: BrowserWindowConstructorOptions = {
      width: this.WIDTH,
      height: this.HEIGHT,
      title: this.title,
      titleBarStyle: 'hidden',
      trafficLightPosition: { x: 16, y: 16 },
      webPreferences: {
        contextIsolation: true,
        nodeIntegration: false,
        sandbox: false,
        preload,
      },
      autoHideMenuBar: true,
      frame: !this.isMac,
      resizable: true,
    };

    if (this.isDevelopment || this.isLinux) {
      Object.assign(options, { icon: this.icon });
    }

    if (this.isLinux) {
      Object.assign(options, {
        icon: path.join(__dirname, '/icons/512x512.png'),
      });
    }

    return options;
  }

  async createWindow() {
    const options = this.getOptions();
    this.mainWindow = new BrowserWindow(options);

    if (this.isDevelopment) {
      this.setViteServerURL();
    } else {
      this.registerAppProtocol();
    }

    await this.mainWindow.loadURL(this.winURL);
    if (this.isDevelopment && !this.isTest) {
      this.mainWindow.webContents.openDevTools();
    }

    this.setMainWindowListeners();
  }

  setViteServerURL() {
    let port = 6969;
    let host = '0.0.0.0';

    if (process.env.VITE_PORT && process.env.VITE_HOST) {
      port = Number(process.env.VITE_PORT);
      host = process.env.VITE_HOST;
    }

    // Load the url of the dev server if in development mode
    this.winURL = `http://${host}:${port}/`;
  }

  registerAppProtocol() {
    protocol.registerBufferProtocol('app', bufferProtocolCallback);

    // Use the registered protocol url to load the files.
    this.winURL = 'app://./index.html';
  }

  setMainWindowListeners() {
    if (this.mainWindow === null) {
      return;
    }

    this.mainWindow.on('closed', () => {
      this.mainWindow = null;
    });

    this.mainWindow.webContents.on('did-fail-load', () => {
      this.mainWindow!.loadURL(this.winURL).catch((err) =>
        emitMainProcessError(err)
      );
    });
  }
}

/**
 * Callback used to register the custom app protocol,
 * during prod, files are read and served by using this
 * protocol.
 */
function bufferProtocolCallback(
  request: ProtocolRequest,
  callback: (response: ProtocolResponse) => void
) {
  const { pathname, host } = new URL(request.url);
  const filePath = path.join(
    __dirname,
    'src',
    decodeURI(host),
    decodeURI(pathname)
  );

  fs.readFile(filePath, (_, data) => {
    const extension = path.extname(filePath).toLowerCase();
    const mimeType =
      {
        '.js': 'text/javascript',
        '.css': 'text/css',
        '.html': 'text/html',
        '.svg': 'image/svg+xml',
        '.json': 'application/json',
      }[extension] ?? '';

    callback({ mimeType, data });
  });
}

export default new Main();

```

### File: META.md
```md
This `md` lays out how this project is structured.

## Execution

Since it's an electron project, there are two points from where the execution
begins.

1. **Main Process**: Think of this as the _server_, the file where this beings
   is `books/main.ts`
2. **Renderer Process**: Think of this as the _client_, the file where this
   begins is `books/src/main.js`

_Note: For more insight into how electron execution is structured check out electron's
[Process Model](https://www.electronjs.org/docs/latest/tutorial/process-model)._

This process is architected in a _client-server_ manner. If the _client_ side
requires resources from the _server_ side, it does so by making use of
`ipcRenderer.send` or `ipcRenderer.invoke` i.e. if the front end is being run on
electron.

The `ipcRenderer` calls are done only in `fyo/demux/*.ts` files. I.e. these
are the only files on the _client_ side that are aware of the platform the
_client_ is being run on i.e. `electron` or Browser. So all platform specific
calls should go through these _demux_ files.

## Code Structure

Code is structured in a way so as to maintain clear separation between what each
set of files structured under some subdirectory does. It is also to maintain a
clear separation between the _client_ and the _server_.

The _client_ code should not be calling _server_ code directly (i.e. by
importing it) and vice-versa. This is to maintain the _client_ code in a
platform agnostic manner.

Some of the code is side agnostic, i.e. can be called from the _client_ or the
_server_. Only code that doesn't have platform specific calls example using
`node` `fs` or the browsers `window`. Ideally this code won't have an imports.

### Special Folders

Here's a list of subdirectories and their purposes, for more details on
individual ones, check the `README.md` in those subdirectories:

| Folder         | Side       | Description                                                                                                                |
| -------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------- |
| `main`         | _server_   | Electron main process specific code called from `books/main.ts`                                                            |
| `schemas`      | _server_   | Collection of database schemas in a `json` format and the code to combine them                                             |
| `backend`      | _server_   | Database management and CRUD calls                                                                                         |
| `scripts`      | _server_   | Code that is not called when the project is running, but separately to run some task for instance to generate translations |
| `build`        | _server_   | Build specific files not used unless building the project                                                                  |
| `translations` | _server_   | Collection of csv files containing translations                                                                            |
| `src`          | _client_   | Code that mainly deals with the view layer (all `.vue` are stored here)                                                    |
| `reports`      | _client\*_ | Collection of logic code and view layer config files for displaying reports.                                               |
| `models`       | _client\*_ | Collection of `Model.ts` files that manage the data and some business logic on the client side.                            |
| `fyo`          | _client\*_ | Code for the underlying library that manages the client side                                                               |
| `utils`        | _agnostic_ | Collection of code used by either sides.                                                                                   |
| `dummy`        | _agnostic_ | Code used to generate dummy data for testing or demo purposes                                                              |

#### _client\*_

The code in these folders is called during runtime from the _client_
side but since they contain business logic, they are tested using `mocha` on the
_server_ side. This is a bit stupid and so will be fixed later.

Due to this, the code in these files should not be calling _client_ side code
directly. If client side code is to be called, it should be done so only by
using dynamic imports, i.e. `await import('...')` along pathways that won't run
in a test.

### Special Files

Other than this there are two special types of files:

#### `**/types.ts`

These contains all the type information, these files are side agnostic and
should only import code from other type files.

The type information contained depends on the folder it is under i.e. where the
code associated with the types is written.

If trying to understand the code in this project I'd suggest not ignoring these.

#### `**/test/*.spec.ts`

These contain tests, as of now all tests run on the _server_ side using `mocha`.

The tests files are located in `**/test` folders which are nested under the
directories of what they are testing. No code from these files is called during
runtime.

```

### File: postcss.config.js
```js
module.exports = {
  plugins: [require('tailwindcss'), require('autoprefixer')],
};

```

### File: scripts_DISTILLED.md
```md
---
id: scripts
type: distilled_knowledge
---
# scripts

## SWALLOW ENGINE DISTILLATION

### File: generateTranslations.ts
```ts
import fs from 'fs/promises';
import path from 'path';
import { UnknownMap } from 'utils/types';
import { generateCSV, parseCSV } from '../utils/csvParser';
import {
  getIndexFormat,
  getWhitespaceSanitized,
  schemaTranslateables,
} from '../utils/translationHelpers';

/* eslint-disable no-console, @typescript-eslint/no-floating-promises */

const translationsFolder = path.resolve(__dirname, '..', 'translations');
const PATTERN = /(?<!\w)t`([^`]+)`/g;

type Content = { fileName: string; content: string };

function shouldIgnore(p: string, ignoreList: string[]): boolean {
  const name = p.split(path.sep).at(-1) ?? '';
  return ignoreList.includes(name);
}

async function getFileList(
  root: string,
  ignoreList: string[],
  extPattern = /\.(js|ts|vue)$/
): Promise<string[]> {
  const contents: string[] = await fs.readdir(root);
  const files: string[] = [];
  const promises: Promise<void>[] = [];

  for (const c of contents) {
    const absPath = path.resolve(root, c);
    const isDir = (await fs.stat(absPath)).isDirectory();

    if (isDir && !shouldIgnore(absPath, ignoreList)) {
      const pr = getFileList(absPath, ignoreList, extPattern).then((fl) => {
        files.push(...fl);
      });
      promises.push(pr);
    } else if (absPath.match(extPattern) !== null) {
      files.push(absPath);
    }
  }

  await Promise.all(promises);
  return files;
}

async function getFileContents(fileList: string[]): Promise<Content[]> {
  const contents: Content[] = [];
  const promises: Promise<void>[] = [];
  for (const fileName of fileList) {
    const pr = fs.readFile(fileName, { encoding: 'utf-8' }).then((content) => {
      contents.push({ fileName, content });
    });
    promises.push(pr);
  }
  await Promise.all(promises);
  return contents;
}

async function getAllTStringsMap(
  contents: Content[]
): Promise<Map<string, string[]>> {
  const strings: Map<string, string[]> = new Map();
  const promises: Promise<void>[] = [];

  contents.forEach(({ fileName, content }) => {
    const pr = getTStrings(content).then((ts) => {
      if (ts.length === 0) {
        return;
      }
      strings.set(fileName, ts);
    });
    promises.push(pr);
  });

  await Promise.all(promises);
  return strings;
}

function getTStrings(content: string): Promise<string[]> {
  return new Promise((resolve) => {
    const tStrings = tStringFinder(content);
    resolve(tStrings);
  });
}

function tStringFinder(content: string): string[] {
  return [...content.matchAll(PATTERN)].map(([, t]) => {
    t = getIndexFormat(t);
    return getWhitespaceSanitized(t);
  });
}

function tStringsToArray(
  tMap: Map<string, string[]>,
  tStrings: string[]
): string[] {
  const tSet: Set<string> = new Set();
  for (const k of tMap.keys()) {
    tMap.get(k)!.forEach((s) => tSet.add(s));
  }

  for (const ts of tStrings) {
    tSet.add(ts);
  }

  return Array.from(tSet).sort();
}

function printHelp() {
  const shouldPrint = process.argv.findIndex((i) => i === '-h') !== -1;
  if (shouldPrint) {
    console.log(
      `Usage: ` +
        `\tyarn script:translate\n` +
        `\tyarn script:translate -h\n` +
        `\tyarn script:translate -l [language_code]\n` +
        `\n` +
        `Example: $ yarn script:translate -l de\n` +
        `\n` +
        `Description:\n` +
        `\tPassing a language code will create a '.csv' file in\n` +
        `\tthe 'translations' subdirectory. Translated strings are to\n` +
        `\tbe added to this file.\n\n` +
        `\tCalling the script without args will update the translation csv\n` +
        `\tfile with new strings if any. Existing translations won't\n` +
        `\tbe removed.\n` +
        `\n` +
        `Parameters:\n` +
        `\tlanguage_code : An ISO 693-1 code or a locale identifier.\n` +
        `\n` +
        `Reference:\n` +
        `\tISO 693-1 codes: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes\n` +
        `\tLocale identifier: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#locale_identification_and_negotiation`
    );
  }
  return shouldPrint;
}

function getLanguageCode() {
  const i = process.argv.findIndex((i) => i === '-l');
  if (i === -1) {
    return '';
  }
  return process.argv[i + 1] ?? '';
}

function getTranslationFilePath(languageCode: string) {
  return path.resolve(translationsFolder, `${languageCode}.csv`);
}

async function regenerateTranslation(tArray: string[], path: string) {
  // Removes old strings, adds new strings
  const storedCSV = await fs.readFile(path, { encoding: 'utf-8' });
  const storedMatrix = parseCSV(storedCSV);

  const map: Map<string, string[]> = new Map();
  for (const row of storedMatrix) {
    const tstring = row[0];
    map.set(tstring, row.slice(1));
  }

  const matrix = tArray.map((source) => {
    const stored = map.get(source) ?? [];
    const translation = stored[0] ?? '';
    const context = stored[1] ?? '';

    return [source, translation, context];
  });
  const csv = generateCSV(matrix);

  await fs.writeFile(path, csv, { encoding: 'utf-8' });
  console.log(`\tregenerated: ${path}`);
}

async function regenerateTranslations(languageCode: string, tArray: string[]) {
  // regenerate one file
  if (languageCode.length !== 0) {
    const path = getTranslationFilePath(languageCode);
    regenerateTranslation(tArray, path);
    return;
  }

  // regenerate all translation files
  console.log(`Language code not passed, regenerating all translations.`);
  for (const filePath of await fs.readdir(translationsFolder)) {
    if (!filePath.endsWith('.csv')) {
      continue;
    }

    regenerateTranslation(tArray, path.resolve(translationsFolder, filePath));
  }
}

async function writeTranslations(languageCode: string, tArray: string[]) {
  const path = getTranslationFilePath(languageCode);
  try {
    const stat = await fs.stat(path);
    if (!stat.isFile()) {
      throw new Error(`${path} is not a translation file`);
    }

    console.log(
      `Existing file found for '${languageCode}': ${path}\n` +
        `regenerating it's translations.`
    );
    regenerateTranslations(languageCode, tArray);
  } catch (err) {
    if ((err as NodeJS.ErrnoException).code !== 'ENOENT') {
      throw err;
    }

    const matrix = tArray.map((s) => [s, '', '']);
    const csv = generateCSV(matrix);
    await fs.writeFile(path, csv, { encoding: 'utf-8' });
    console.log(`Generated translation file for '${languageCode}': ${path}`);
  }
}

async function getTStringsFromJsonFileList(
  fileList: string[]
): Promise<string[]> {
  const promises: Promise<void>[] = [];
  const schemaTStrings: string[][] = [];

  for (const filePath of fileList) {
    const promise = fs
      .readFile(filePath, { encoding: 'utf8' })
      .then((content) => {
        const schema = JSON.parse(content) as Record<string, unknown>;
        const tStrings: string[] = [];
        pushTStringsFromSchema(schema, tStrings, schemaTranslateables);
        return tStrings;
      })
      .then((ts) => {
        schemaTStrings.push(ts);
      });

    promises.push(promise);
  }

  await Promise.all(promises);
  return schemaTStrings.flat();
}

function pushTStringsFromSchema(
  map: UnknownMap | UnknownMap[],
  array: string[],
  translateables: string[]
) {
  if (Array.isArray(map)) {
    for (const item of map) {
      pushTStringsFromSchema(item, array, translateables);
    }
    return;
  }

  if (typeof map !== 'object') {
    return;
  }

  for (const key of Object.keys(map)) {
    const value = map[key];
    if (translateables.includes(key) && typeof value === 'string') {
      array.push(value);
    }

    if (typeof value !== 'object') {
      continue;
    }

    pushTStringsFromSchema(
      value as UnknownMap | UnknownMap[],
      array,
      translateables
    );
  }
}

async function getSchemaTStrings() {
  const root = path.resolve(__dirname, '../schemas');
  const fileList = await getFileList(root, ['tests', 'regional'], /\.json$/);
  return await getTStringsFromJsonFileList(fileList);
}

async function run() {
  if (printHelp()) {
    return;
  }

  const root = path.resolve(__dirname, '..');
  const ignoreList = ['node_modules', 'dist_electron', 'scripts'];
  const languageCode = getLanguageCode();

  console.log();
  const fileList: string[] = await getFileList(root, ignoreList);
  const contents: Content[] = await getFileContents(fileList);
  const tMap: Map<string, string[]> = await getAllTStringsMap(contents);
  const schemaTStrings: string[] = await getSchemaTStrings();
  const tArray: string[] = tStringsToArray(tMap, schemaTStrings);

  try {
    await fs.stat(translationsFolder);
  } catch (err) {
    if ((err as NodeJS.ErrnoException).code !== 'ENOENT') {
      throw err;
    }

    await fs.mkdir(translationsFolder);
  }

  if (languageCode === '') {
    regenerateTranslations('', tArray);
    return;
  }

  writeTranslations(languageCode, tArray);
}

run();

```

### File: profile.sh
```sh
#! /usr/bin/env zsh

# https://nodejs.org/en/docs/guides/simple-profiling/

export TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}'

rm ./isolate-*-v8.log 2> /dev/null
rm ./profiler-output.log 2> /dev/null

export ELECTRON_RUN_AS_NODE=true
alias electron_node=./node_modules/.bin/electron

echo "running profile.ts"
electron_node --require ts-node/register --require tsconfig-paths/register --prof ./scripts/profile.ts

echo "processing tick file"
electron_node --prof-process ./isolate-*-v8.log > ./profiler-output.log && echo "generated profiler-output.log"
rm ./isolate-*-v8.log
```

### File: profile.ts
```ts
import { DatabaseManager } from 'backend/database/manager';
import { setupDummyInstance } from 'dummy';
import { unlink } from 'fs/promises';
import { Fyo } from 'fyo';
import { DummyAuthDemux } from 'fyo/tests/helpers';
import { getTestDbPath } from 'tests/helpers';

async function run() {
  const fyo = new Fyo({
    DatabaseDemux: DatabaseManager,
    AuthDemux: DummyAuthDemux,
    isTest: true,
    isElectron: false,
  });
  const dbPath = getTestDbPath();

  await setupDummyInstance(dbPath, fyo, 1, 100);
  await fyo.close();
  await unlink(dbPath);
}

// eslint-disable-next-line @typescript-eslint/no-floating-promises
run();

```

### File: publish-mac-arm.sh
```sh
# #! /bin/zsh

set -e

# Check node and yarn versions
YARN_VERSION=$(yarn --version)
if [ "$YARN_VERSION" != "1.22.18" ]; then
  echo "Incorrect yarn version: $YARN_VERSION"
  exit 1
fi

# Source secrets
source .env.publish

# Create folder for the publish build
cd ../
rm -rf build_publish
mkdir build_publish
cd build_publish

# Clone and cd into books
git clone https://github.com/frappe/books --depth 1
cd books

# Copy creds to log_creds.txt
echo $ERR_LOG_KEY > log_creds.txt
echo $ERR_LOG_SECRET >> log_creds.txt
echo $ERR_LOG_URL >> log_creds.txt
echo $TELEMETRY_URL >> log_creds.txt


# Install Dependencies
yarn install

# Set .env and build
export GH_TOKEN=$GH_TOKEN &&
 export CSC_IDENTITY_AUTO_DISCOVERY=true &&
 export APPLE_ID=$APPLE_ID &&
 export APPLE_TEAM_ID=$APPLE_TEAM_ID &&
 export APPLE_APP_SPECIFIC_PASSWORD=$APPLE_APP_SPECIFIC_PASSWORD &&
 yarn build --mac --publish=always

cd ../books

```

### File: runner.sh
```sh
#! /usr/bin/env zsh

# basically uses electron's node to prevent
# mismatch in NODE_MODULE_VERSION when running
# better-sqlite3

export TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}'
export ELECTRON_RUN_AS_NODE=true
alias electron_node="./node_modules/.bin/electron --require ts-node/register --require tsconfig-paths/register"
electron_node $@
```

### File: test.sh
```sh
TEST_PATH=$@

if [ $# -eq 0 ]
  then
    TEST_PATH=./**/tests/**/*.spec.ts
fi

export IS_TEST=true
./scripts/runner.sh ./node_modules/.bin/tape $TEST_PATH | ./node_modules/.bin/tap-spec
```


```

### File: src_DISTILLED.md
```md
---
id: src
type: distilled_knowledge
---
# src

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# src

This is where all the frontend code lives

## Fyo Initialization

The initialization flows are different when the instance is new or is existing.
All of them are triggered from `src/App.vue`.

**New Instance**

1. Run _Setup Wizard_ for init values (eg: `country`).
2. Call `setupInstance.ts/setupInstance` using init values.

**Existing Instance**

1. Connect to db.
2. Check if _Setup Wizard_ has been completed, if not, jump to **New Instance**
3. Call `initFyo/initializeInstance` with `dbPath` and `countryCode`

## Global Fyo

Global fyo is exported from `initFyo.ts`. Only code that isn't going to be unit
tested using `mocha` should use this, i.e. code in `src`

```

### File: errorHandling.ts
```ts
import { t } from 'fyo';
import type { Doc } from 'fyo/model/doc';
import { BaseError } from 'fyo/utils/errors';
import { ErrorLog } from 'fyo/utils/types';
import { truncate } from 'lodash';
import { showDialog } from 'src/utils/interactive';
import { fyo } from './initFyo';
import router from './router';
import { getErrorMessage, stringifyCircular } from './utils';
import type { DialogOptions, ToastOptions } from './utils/types';
import { ModelNameEnum } from 'models/types';

function shouldNotStore(error: Error) {
  const shouldLog = (error as BaseError).shouldStore ?? true;
  return !shouldLog;
}

export async function sendError(errorLogObj: ErrorLog) {
  if (!errorLogObj.stack) {
    return;
  }

  errorLogObj.more ??= {};
  errorLogObj.more.path ??= router.currentRoute.value.fullPath;

  const body = {
    error_name: errorLogObj.name,
    message: errorLogObj.message,
    stack: errorLogObj.stack,
    platform: fyo.store.platform,
    version: fyo.store.appVersion,
    language: fyo.store.language,
    instance_id: fyo.store.instanceId,
    device_id: fyo.store.deviceId,
    open_count: fyo.store.openCount,
    country_code: fyo.singles.SystemSettings?.countryCode,
    more: stringifyCircular(errorLogObj.more),
  };

  if (fyo.store.isDevelopment) {
    // eslint-disable-next-line no-console
    console.log('sendError', body);
  }

  await ipc.sendError(JSON.stringify(body));
}

function getToastProps(errorLogObj: ErrorLog) {
  const props: ToastOptions = {
    message: errorLogObj.name ?? t`Error`,
    type: 'error',
    actionText: t`Report Error`,
    action: () => reportIssue(errorLogObj),
  };

  return props;
}

export function getErrorLogObject(
  error: Error,
  more: Record<string, unknown>
): ErrorLog {
  const { name, stack, message, cause } = error;
  if (cause) {
    more.cause = cause;
  }

  const errorLogObj = { name, stack, message, more };

  fyo.errorLog.push(errorLogObj);

  return errorLogObj;
}

export async function handleError(
  logToConsole: boolean,
  error: Error,
  more: Record<string, unknown> = {},
  notifyUser = true
) {
  if (logToConsole) {
    // eslint-disable-next-line no-console
    console.error(error);
  }

  if (shouldNotStore(error)) {
    return;
  }

  const errorLogObj = getErrorLogObject(error, more);
  await sendError(errorLogObj);

  if (notifyUser) {
    const toastProps = getToastProps(errorLogObj);
    const { showToast } = await import('src/utils/interactive');
    showToast(toastProps);
  }
}

export async function handleErrorWithDialog(
  error: unknown,
  doc?: Doc,
  reportError?: boolean,
  dontThrow?: boolean
) {
  if (!(error instanceof Error)) {
    return;
  }

  const errorMessage = getErrorMessage(error, doc);
  await handleError(false, error, { errorMessage, doc });

  const label = getErrorLabel(error);
  const options: DialogOptions = {
    title: label,
    detail: errorMessage,
    type: 'error',
  };

  if (reportError) {
    options.detail = truncate(String(options.detail), { length: 128 });
    options.buttons = [
      {
        label: t`Report`,
        action() {
          reportIssue(getErrorLogObject(error, { errorMessage }));
        },
        isPrimary: true,
      },
      {
        label: t`Cancel`,
        action() {
          return null;
        },
        isEscape: true,
      },
    ];
  }

  await showDialog(options);
  if (dontThrow) {
    if (fyo.store.isDevelopment) {
      // eslint-disable-next-line no-console
      console.error(error);
    }
    return;
  }

  throw error;
}

export async function showErrorDialog(title?: string, content?: string) {
  // To be used for  show stopper errors
  title ??= t`Error`;
  content ??= t`Something has gone terribly wrong. Please check the console and raise an issue.`;
  await ipc.showError(title, content);
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function getErrorHandled<T extends (...args: any[]) => Promise<any>>(
  func: T
) {
  type Return = ReturnType<T> extends Promise<infer P> ? P : true;
  return async function errorHandled(...args: Parameters<T>): Promise<Return> {
    try {
      return (await func(...args)) as Return;
    } catch (error) {
      await handleError(false, error as Error, {
        functionName: func.name,
        functionArgs: args,
      });

      throw error;
    }
  };
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function getErrorHandledSync<T extends (...args: any[]) => any>(
  func: T
) {
  type Return = ReturnType<T> extends Promise<infer P> ? P : ReturnType<T>;
  return function errorHandledSync(...args: Parameters<T>) {
    try {
      return func(...args) as Return;
    } catch (error) {
      // eslint-disable-next-line @typescript-eslint/no-floating-promises
      handleError(false, error as Error, {
        functionName: func.name,
        functionArgs: args,
      });
    }
  };
}

function getFeatureFlags(): string[] {
  const getBooleanFields = (docName: string) => {
    const doc = fyo.singles[docName];

    return Object.entries(doc as Doc).reduce((acc, [key, value]) => {
      const fieldsArray = fyo.schemaMap[docName]?.fields ?? [];
      const fieldsMap = new Map(fieldsArray.map((f) => [f.fieldname, f]));

      const field = fieldsMap.get(key);
      if (
        typeof value === 'boolean' &&
        !field?.hidden &&
        !key.startsWith('_')
      ) {
        acc[key] = value;
      }
      return acc;
    }, {} as Record<string, boolean>);
  };

  const sections = [
    {
      name: 'Accounting',
      flags: getBooleanFields(ModelNameEnum.AccountingSettings),
    },
    { name: 'POS', flags: getBooleanFields(ModelNameEnum.POSSettings) },
    {
      name: 'Inventory',
      flags: getBooleanFields(ModelNameEnum.InventorySettings),
    },
  ]

    .filter(({ flags }) => Object.keys(flags).length > 0)
    .flatMap(({ name, flags }) => [
      `**${name} Settings**:`,
      '```json',
      JSON.stringify(flags, null, 2),
      '```',
      '',
    ]);

  return sections.length
    ? [
        '<details>',
        '<summary><strong>Feature Flags</strong></summary>',
        '',
        ...sections,
        '</details>',
      ]
    : [];
}

function getIssueUrlQuery(errorLogObj?: ErrorLog): string {
  const baseUrl = 'https://github.com/frappe/books/issues/new?labels=bug';

  const body = [
    '<h2>Description</h2>',
    'Add some description...',
    '',
    '<h2>Steps to Reproduce</h2>',
    'Add steps to reproduce the error...',
    '',
    '<h2>Info</h2>',
    '',
  ];

  if (errorLogObj) {
    body.push(`**Error**: _${errorLogObj.name}: ${errorLogObj.message}_`, '');
  }

  if (errorLogObj?.stack) {
    body.push('**Stack**:', '```', errorLogObj.stack, '```', '');
  }

  body.push(`**Version**: \`${fyo.store.appVersion}\``);
  body.push(`**Platform**: \`${fyo.store.platform}\``);
  body.push(`**Path**: \`${router.currentRoute.value.fullPath}\``);

  body.push(`**Language**: \`${fyo.config.get('language') ?? '-'}\``);
  if (fyo.singles.SystemSettings?.countryCode) {
    body.push(`**Country**: \`${fyo.singles.SystemSettings.countryCode}\``);
  }
  body.push('', ...getFeatureFlags());

  const encodedBody = encodeURIComponent(body.join('\n'));
  return `${baseUrl}&body=${encodedBody}`;
}

export function reportIssue(errorLogObj?: ErrorLog) {
  const urlQuery = getIssueUrlQuery(errorLogObj);
  ipc.openExternalUrl(urlQuery);
}

function getErrorLabel(error: Error) {
  const name = error.name;
  if (!name) {
    return t`Error`;
  }

  if (name === 'BaseError') {
    return t`Error`;
  }

  if (name === 'ValidationError') {
    return t`Validation Error`;
  }

  if (name === 'NotFoundError') {
    return t`Not Found`;
  }

  if (name === 'ForbiddenError') {
    return t`Forbidden Error`;
  }

  if (name === 'DuplicateEntryError') {
    return t`Duplicate Entry`;
  }

  if (name === 'LinkValidationError') {
    return t`Link Validation Error`;
  }

  if (name === 'MandatoryError') {
    return t`Mandatory Error`;
  }

  if (name === 'DatabaseError') {
    return t`Database Error`;
  }

  if (name === 'CannotCommitError') {
    return t`Cannot Commit Error`;
  }

  if (name === 'NotImplemented') {
    return t`Error`;
  }

  if (name === 'ToDebugError') {
    return t`Error`;
  }

  return t`Error`;
}

```

### File: importer.ts
```ts
import { Fyo } from 'fyo';
import { Converter } from 'fyo/core/converter';
import { DocValue, DocValueMap } from 'fyo/core/types';
import { Doc } from 'fyo/model/doc';
import { getEmptyValuesByFieldTypes } from 'fyo/utils';
import { ValidationError } from 'fyo/utils/errors';
import {
  Field,
  FieldType,
  FieldTypeEnum,
  OptionField,
  RawValue,
  Schema,
  TargetField,
} from 'schemas/types';
import { generateCSV, parseCSV } from 'utils/csvParser';
import { getValueMapFromList } from 'utils/index';

export type TemplateField = Field & TemplateFieldProps;

type TemplateFieldProps = {
  schemaName: string;
  schemaLabel: string;
  fieldKey: string;
  parentSchemaChildField?: TargetField;
};

type ValueMatrixItem =
  | {
      value: DocValue;
      rawValue?: RawValue;
      error?: boolean;
    }
  | { value?: DocValue; rawValue: RawValue; error?: boolean };

type ValueMatrix = ValueMatrixItem[][];

const skippedFieldsTypes: FieldType[] = [
  FieldTypeEnum.AttachImage,
  FieldTypeEnum.Attachment,
  FieldTypeEnum.Table,
];

/**
 * Tool that
 * - Can make bulk entries for any kind of Doc
 * - Takes in unstructured CSV data, converts it into Docs
 * - Saves and or Submits the converted Docs
 */
export class Importer {
  schemaName: string;
  fyo: Fyo;

  /**
   * List of template fields that have been assigned a column, in
   * the order they have been assigned.
   */
  assignedTemplateFields: (string | null)[];

  /**
   * Map of all the template fields that can be imported.
   */
  templateFieldsMap: Map<string, TemplateField>;

  /**
   * Map of Fields that have been picked, i.e.
   * - Fields which will be included in the template
   * - Fields for which values will be provided
   */
  templateFieldsPicked: Map<string, boolean>;

  /**
   * Whether the schema type being imported has table fields
   */
  hasChildTables: boolean;

  /**
   * Matrix containing the raw values which will be converted to
   * doc values before importing.
   */
  valueMatrix: ValueMatrix;

  /**
   * Data from the valueMatrix rows will be converted into Docs
   * which will be stored in this array.
   */
  docs: Doc[];

  /**
   * Used if an options field is imported where the import data
   * provided maybe the label and not the value
   */
  optionsMap: {
    values: Record<string, Set<string>>;
    labelValueMap: Record<string, Record<string, string>>;
  };

  constructor(schemaName: string, fyo: Fyo) {
    if (!fyo.schemaMap[schemaName]) {
      throw new ValidationError(
        `Invalid schemaName ${schemaName} found in importer`
      );
    }

    this.hasChildTables = false;
    this.schemaName = schemaName;
    this.fyo = fyo;
    this.docs = [];
    this.valueMatrix = [];
    this.optionsMap = {
      values: {},
      labelValueMap: {},
    };

    const templateFields = getTemplateFields(schemaName, fyo, this);
    this.assignedTemplateFields = templateFields.map((f) => f.fieldKey);
    this.templateFieldsMap = new Map();
    this.templateFieldsPicked = new Map();

    templateFields.forEach((f) => {
      this.templateFieldsMap.set(f.fieldKey, f);
      this.templateFieldsPicked.set(f.fieldKey, true);
    });
  }

  selectFile(data: string): boolean {
    try {
      const parsed = parseCSV(data);
      this.selectParsed(parsed);
    } catch {
      return false;
    }

    return true;
  }

  async checkLinks() {
    const tfKeys = this.assignedTemplateFields
      .map((key, index) => ({
        key,
        index,
        tf: this.templateFieldsMap.get(key ?? ''),
      }))
      .filter(({ key, tf }) => {
        if (!key || !tf) {
          return false;
        }

        return tf.fieldtype === FieldTypeEnum.Link;
      }) as { key: string; index: number; tf: TemplateField }[];

    const linksNames: Map<string, Set<string>> = new Map();
    for (const row of this.valueMatrix) {
      for (const { tf, index } of tfKeys) {
        const target = (tf as TargetField).target;
        const value = row[index]?.value;
        if (typeof value !== 'string' || !value) {
          continue;
        }

        if (!linksNames.has(target)) {
          linksNames.set(target, new Set());
        }

        linksNames.get(target)?.add(value);
      }
    }

    const doesNotExist = [];
    for (const [target, values] of linksNames.entries()) {
      for (const value of values) {
        const exists = await this.fyo.db.exists(target, value);
        if (exists) {
          continue;
        }

        doesNotExist.push({
          schemaName: target,
          schemaLabel: this.fyo.schemaMap[this.schemaName]?.label,
          name: value,
        });
      }
    }

    return doesNotExist;
  }

  checkCellErrors() {
    const assigned = this.assignedTemplateFields
      .map((key, index) => ({
        key,
        index,
        tf: this.templateFieldsMap.get(key ?? ''),
      }))
      .filter(({ key, tf }) => !!key && !!tf) as {
      key: string;
      index: number;
      tf: TemplateField;
    }[];

    const cellErrors = [];
    for (let i = 0; i < this.valueMatrix.length; i++) {
      const row = this.valueMatrix[i];
      for (const { tf, index } of assigned) {
        if (!row[index]?.error) {
          continue;
        }

        const rowLabel = this.fyo.t`Row ${i + 1}`;
        const columnLabel = getColumnLabel(tf);
        cellErrors.push(`(${rowLabel}, ${columnLabel})`);
      }
    }

    return cellErrors;
  }

  populateDocs() {
    const { dataMap, childTableMap } =
      this.getDataAndChildTableMapFromValueMatrix();

    const schema = this.fyo.schemaMap[this.schemaName];
    const targetFieldnameMap = schema?.fields
      .filter((f) => f.fieldtype === FieldTypeEnum.Table)
      .reduce((acc, f) => {
        const { target, fieldname } = f as TargetField;
        acc[target] = fieldname;
        return acc;
      }, {
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

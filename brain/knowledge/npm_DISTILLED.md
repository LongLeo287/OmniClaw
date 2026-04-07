---
id: npm
type: knowledge
owner: OA_Triage
---
# npm
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "npm-to-yarn",
  "version": "3.0.1",
  "description": "Convert npm CLI commands to Yarn commands, and vice versa",
  "keywords": [
    "string convert",
    "documentation",
    "yarn to npm"
  ],
  "main": "dist/npm-to-yarn.umd.js",
  "module": "dist/npm-to-yarn.mjs",
  "typings": "dist/types/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/types/index.d.ts",
      "import": "./dist/npm-to-yarn.mjs",
      "require": "./dist/npm-to-yarn.umd.js",
      "default": "./dist/npm-to-yarn.umd.js"
    }
  },
  "sideEffects": false,
  "files": [
    "dist"
  ],
  "author": "Ben Gubler <nebrelbug@gmail.com>",
  "homepage": "https://github.com/nebrelbug/npm-to-yarn#readme",
  "funding": "https://github.com/nebrelbug/npm-to-yarn?sponsor=1",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/nebrelbug/npm-to-yarn.git"
  },
  "bugs": {
    "url": "https://github.com/nebrelbug/npm-to-yarn/issues"
  },
  "license": "MIT",
  "engines": {
    "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
  },
  "type": "commonjs",
  "scripts": {
    "lint": "eslint src/*.ts test/*.spec.ts --ext .js,.ts",
    "prebuild": "rimraf dist",
    "build": "rollup -c rollup.config.mjs",
    "start": "rollup -c rollup.config.mjs -w",
    "test": "jest --coverage",
    "test:watch": "jest --coverage --watch",
    "test:prod": "npm run lint && npm run test -- --no-cache",
    "format": "prettier-standard --format"
  },
  "lint-staged": {
    "{src,test}/**/*.ts": [
      "prettier-standard --lint"
    ]
  },
  "devDependencies": {
    "@types/jest": "^29.2.4",
    "@types/node": "^18.11.15",
    "@typescript-eslint/eslint-plugin": "^5.54.0",
    "@typescript-eslint/parser": "^5.54.0",
    "@rollup/plugin-typescript": "^11.0.0",
    "eslint": "^8.29.0",
    "eslint-config-prettier": "^8.5.0",
    "jest": "^29.3.1",
    "lint-staged": "^13.1.0",
    "prettier-standard": "^16.4.1",
    "rimraf": "^3.0.2",
    "rollup": "^3.18.0",
    "ts-jest": "^29.0.5",
    "typescript": "^4.9.4"
  }
}

```

### File: README.md
```md
# npm-to-yarn

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[logo]: https://img.shields.io/badge/all_contributors-0-orange.svg 'Number of contributors on All-Contributors'

<!-- ALL-CONTRIBUTORS-BADGE:END -->

[![npm](https://img.shields.io/npm/v/npm-to-yarn)](https://www.npmjs.com/package/npm-to-yarn)
[![License](https://img.shields.io/npm/l/npm-to-yarn)](./LICENSE)
[![CI](https://github.com/nebrelbug/npm-to-yarn/actions/workflows/ci.yml/badge.svg)](https://github.com/nebrelbug/npm-to-yarn/actions/workflows/ci.yml)
[![Coveralls](https://img.shields.io/coveralls/nebrelbug/npm-to-yarn.svg)](https://coveralls.io/github/nebrelbug/npm-to-yarn)

[![styled with prettier](https://img.shields.io/badge/styled_with-prettier-ff69b4.svg)](https://github.com/prettier/prettier)
[![Donate](https://img.shields.io/badge/donate-paypal-blue.svg)](https://paypal.me/bengubler)

**Summary**

`npm-to-yarn` is designed to convert NPM CLI commands to their Yarn equivalents (and vice versa).

## Why `npm-to-yarn`?

`npm-to-yarn` is super helpful in documentation, for example in generating code tabs.

## 📜 Docs

```js
import convert from 'npm-to-yarn'

// or
// var convert = require('npm-to-yarn')

convert('npm install squirrelly', 'yarn')
// yarn add squirrelly

// npx conversions

convert('npx create-next-app', 'yarn')
// yarn dlx create-next-app
```

`npm-to-yarn` exposes a UMD build, so you can also install it with a CDN (it exposes global variable `n2y`)

### API

```ts
/**
 * Converts between npm and yarn command
 */
export default function convert (str: string, to: 'npm' | 'yarn' | 'pnpm' | 'bun'): string
```

## ✔️ Tests

Tests can be run with `npm test`. Multiple tests check that parsing, rendering, and compiling return expected results, formatting follows guidelines, and code coverage is at the expected level.

## 📦 Contributing to `npm-to-yarn` - Setup Guide

Install Dependencies

```sh copy
npm install
```

Run the development server

```sh
npm run start
```

A new file: `npm-to-yarn.mjs` is created in `dist` folder. <br>
Open `node` inside the terminal and write the following code to test new changes

```js
const npmToYarn = await import('./dist/npm-to-yarn.mjs')
const convert = npmToYarn.default

convert('npm install react', 'bun')
```

## Resources

To be added

## Projects using `npm-to-yarn`

- [Dynamoose](https://dynamoosejs.com)
- [Docusaurus](https://docusaurus.io)

## Contributors

Made with ❤ by [@nebrelbug](https://github.com/nebrelbug) and all these wonderful contributors ([emoji key](https://github.com/kentcdodds/all-contributors#emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->


<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/kentcdodds/all-contributors) specification. Contributions of any kind are welcome!

```

### File: .eslintrc.js
```js
module.exports = {
  env: {
    browser: true,
    node: true
  },
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/eslint-recommended',
    'plugin:@typescript-eslint/recommended',
    'prettier'
  ],
  parser: '@typescript-eslint/parser',
  parserOptions: {
    project: 'tsconfig.eslint.json',
    sourceType: 'module'
  },
  plugins: ['@typescript-eslint']
}

```

### File: jest.config.js
```js
'use strict'

// @ts-check
/** @type {import('@jest/types').Config.InitialOptions} */
module.exports = {
  transform: {
    '.(ts)': 'ts-jest'
  },
  testEnvironment: 'node',
  testRegex: '(/test/.*|\\.(test|spec))\\.(ts|js)$',
  moduleFileExtensions: ['ts', 'js'],
  coveragePathIgnorePatterns: ['/node_modules/', '/test/'],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 95,
      lines: 95,
      statements: 95
    }
  },
  collectCoverageFrom: ['src/*.ts']
}

```

### File: test.html
```html
<!--Based on @olado's excellent tester from doT.js-->
<!--Modified by Ben Gubler-->
<!--NOTE: You have to serve this file if you want to see the sourcemaps. NPM Package 'serve' works-->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0"
    />
    <meta name="description" content="Test out Squirrelly code in the browser here" />
    <script src="./dist/npm-to-yarn.umd.js"></script>
    <style>
      body {
        background-color: #f4f4f4;
        color: #555;
        max-width: 800px;
        padding: 20px;
        font-size: 16px;
        font-weight: 200;
        margin: 0 auto;
        font-family: Helvetica Neue, arial, verdana;
      }

      h2 {
        text-shadow: 0 1px 2px #fff;
        margin: 0;
      }

      h2 span {
        font-weight: 200;
        font-size: 14px;
      }

      a {
        color: #2b80ff;
      }

      .smaller {
        font-size: 0.8em;
      }

      h4 {
        margin: 4px 0;
        font-weight: 400;
        font-size: 20px;
      }

      textarea {
        border: 1px solid lightgrey;
        outline: none;
        font-size: 14px;
        width: 96%;
        height: 210px;
        padding: 10px;
        text-align: left;
        resize: vertical;
      }

      .templategroup,
      .datagroup,
      .functiongroup,
      .resultgroup {
        width: 48%;
        margin: 4px 2% 4px 0;
        float: left;
        min-width: 300px;
      }

      #function,
      #result {
        background: #ddd;
        height: 212px;
        padding: 10px;
        font-size: 14px;
        overflow-y: auto;
      }

      #result {
        white-space: pre;
      }

      .definegroup {
        display: none;
      }

      .templategroup.withdefs .definegroup {
        display: block;
      }

      .templategroup.withdefs #template {
        height: 90px;
      }

      textarea.defines {
        height: 60px;
      }

      .stripgroup {
        padding-top: 8px;
        width: 160px;
        float: left;
      }

      #sampletabs {
        list-style: none;
        margin: 0;
        padding: 0;
      }

      #sampletabs li {
        float: left;
        margin: 4px;
        padding: 4px 8px;
        background: #ddd;
        cursor: pointer;
      }

      #sampletabs li.active {
        background: #2b80ff;
        color: #fff;
      }

      @media all and (max-width: 740px) {
        .templategroup,
        .datagroup,
        .functiongroup,
        .resultgroup {
          width: 100%;
          margin-right: 0;
        }

        pre {
          overflow-x: scroll;
        }
      }
    </style>
    <title>NPM-to-Yarn Playground</title>
  </head>

  <body>
    <h2>
      Playground
      <span
        >Based on the excellent
        <a href="http://olado.github.io/doT/index.html">DoT.js</a> website</span
      >
    </h2>
    <div id="samples">
      <div style="clear: both; height: 10px"></div>
      <div class="templategroup">
        <h4>NPM</h4>
        <textarea autocomplete="off" id="npm-text">
npm install squirrelly --global

npm install squirrelly --save-dev
</textarea
        >
      </div>
      <div class="resultgroup">
        <h4>Yarn</h4>
        <textarea autocomplete="off" id="yarn-text"> </textarea>
      </div>
      <div class="resultgroup">
        <h4>PNPM</h4>
        <textarea readonly autocomplete="off" id="pnpm-text"> </textarea>
      </div>
      <div class="resultgroup">
        <h4>Bun</h4>
        <textarea readonly autocomplete="off" id="bun-text"> </textarea>
      </div>
    </div>
    <script>
      /* global Sqrl */
      window.onload = function () {
        function npmToYarn () {
          console.clear()
          var npmText = document.getElementById('npm-text').value
          document.getElementById('yarn-text').value = n2y(npmText, 'yarn')
          document.getElementById('pnpm-text').value = n2y(npmText, 'pnpm')
          document.getElementById('bun-text').value = n2y(npmText, 'bun')
        }

        function yarnToNpm () {
          console.clear()
          var yarnText = document.getElementById('yarn-text').value
          var npmText = n2y(yarnText, 'npm')
          document.getElementById('npm-text').value = npmText
          document.getElementById('pnpm-text').value = n2y(npmText, 'pnpm')
          document.getElementById('bun-text').value = n2y(npmText, 'bun')
        }

        npmToYarn()
        document.getElementById('npm-text').addEventListener('input', npmToYarn)
        document.getElementById('yarn-text').addEventListener('input', yarnToNpm)
      }
    </script>
  </body>
</html>

```

### File: tsconfig.eslint.json
```json
{
  "compilerOptions": {
    "moduleResolution": "node",
    "target": "es5",
    "module": "es2015",
    "lib": ["es2015", "es2016", "es2017", "dom"],
    "strict": true,
    "sourceMap": true,
    "declaration": true,
    "allowSyntheticDefaultImports": true,
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true,
    "declarationDir": "dist/types",
    "outDir": "build"
  },
  "include": ["src", "test", "examples"],
  "exclude": ["node_modules", "typings"]
}

```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    "moduleResolution": "node",
    "target": "es5",
    "module": "es2015",
    "lib": ["es2015", "es2016", "es2017", "dom"],
    "strict": true,
    "sourceMap": true,
    "declaration": true,
    "allowSyntheticDefaultImports": true,
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true,
    "declarationDir": "dist/types",
    "outDir": "build"
  },
  "include": ["src"],
  "exclude": ["node_modules", "typings"]
}

```

### File: .github\CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

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

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

- The use of sexualized language or imagery and unwelcome sexual attention or
  advances
- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or electronic
  address, without explicit permission
- Other conduct which could reasonably be considered inappropriate in a
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
reported by contacting the project team at alexjovermorales@gmail.com. All
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
We're really glad you're reading this, because we need volunteer developers to help this project come to fruition. 👏

## Instructions

These steps will guide you through contributing to this project:

- Fork the repo
- Clone it and install dependencies

```
git clone https://github.com/nebrelbug/npm-to-yarn
npm install
```

Keep in mind that after running `npm install` the git repo is reset. So a good way to cope with this is to have a copy of the folder to push the changes, and the other to try them.

Make and commit your changes. Make sure the commands npm run build and npm run test:prod are working.

Finally send a [GitHub Pull Request](https://github.com/nebrelbug/npm-to-yarn/compare?expand=1) with a clear list of what you've done (read more [about pull requests](https://help.github.com/articles/about-pull-requests/)). Make sure all of your commits are atomic (one feature per commit).

```

### File: src\command.ts
```ts
export function parse (command: string) {
  const args: string[] = []
  let lastQuote: string | false = false
  let escaped = false
  let part = ''
  for (let i = 0; i < command.length; ++i) {
    const char = command.charAt(i)
    if (char === '\\') {
      part += char
      escaped = true
    } else {
      if (char === ' ' && !lastQuote) {
        args.push(part)
        part = ''
      } else if (!escaped && (char === '"' || char === "'")) {
        part += char
        if (char === lastQuote) {
          lastQuote = false
        } else if (!lastQuote) {
          lastQuote = char
        }
      } else {
        part += char
      }
      escaped = false
    }
  }
  args.push(part)
  return args
}

```

### File: src\index.ts
```ts
import { yarnToNPM } from './yarnToNpm'
import { npmToYarn } from './npmToYarn'
import { npmToPnpm } from './npmToPnpm'
import { npmToBun } from './npmToBun'

import { executorCommands } from './utils'

/**
 * Converts between npm and yarn command
 */
export default function convert (str: string, to: 'npm' | 'yarn' | 'pnpm' | 'bun'): string {
  if (
    str.includes('npx') ||
    str.includes('yarn dlx') ||
    str.includes('pnpm dlx') ||
    str.includes('bun x')
  ) {
    const executor = str.includes('npx')
      ? 'npx'
      : str.includes('yarn dlx')
      ? 'yarn dlx'
      : str.includes('pnpm dlx')
      ? 'pnpm dlx'
      : 'bun x'
    return str.replace(executor, executorCommands[to])
  } else if (to === 'npm') {
    return str.replace(/yarn(?: +([^&\n\r]*))?/gm, yarnToNPM)
  } else if (to === 'pnpm') {
    return str.replace(/npm(?: +([^&\n\r]*))?/gm, npmToPnpm)
  } else if (to === 'bun') {
    return str.replace(/npm(?: +([^&\n\r]*))?/gm, npmToBun)
  } else {
    return str.replace(/npm(?: +([^&\n\r]*))?/gm, npmToYarn)
  }
}

```

### File: src\npmToBun.ts
```ts
import { parse } from './command'

function convertInstallArgs (args: string[]) {
  // bun uses -g and --global flags
  // bun mostly conforms to Yarn's CLI
  return args.map(item => {
    switch (item) {
      case '--save-dev':
      case '--development':
      case '-D':
        return '--dev'
      case '--save-prod':
      case '-P':
        return '--production'
      case '--no-package-lock':
        return '--no-save'
      case '--save-optional':
      case '-O':
        return '--optional'
      case '--save-exact':
      case '-E':
        return '--exact'
      case '--save':
      case '-S':
        // this is default in bun
        return ''
      case '--global':
      case '-g':
        return '--global'
      default:
        return item
    }
  })
}

export const bunCLICommands = [
  'init',
  'run',
  'add',
  'pm',
  'help',
  'install',
  'remove',
  'upgrade',
  'version'
] as const
type bunCLICommands = typeof bunCLICommands[number]

export function npmToBun (_m: string, command: string): string {
  let args = parse((command || '').trim())

  const index = args.findIndex(a => a === '--')
  if (index >= 0) {
    args.splice(index, 1)
  }

  let cmd = 'bun'
  switch (args[0]) {
    case 'install':
    case 'i':
      if (args.length === 1) {
        args = ['install']
      } else {
        args[0] = 'add'
      }
      args = convertInstallArgs(args)
      break
    case 'uninstall':
    case 'un':
    case 'remove':
    case 'r':
    case 'rm':
      args[0] = 'remove'
      args = convertInstallArgs(args)
      break
    case 'cache':
      if (args[1] === 'clean') {
        args = ['pm', 'cache', 'rm'].concat(args.slice(2))
      } else {
        cmd = 'npm'
      }
      break
    case 'rebuild':
    case 'rb':
      args[0] = 'add'
      args.push('--force')
      break
    case 'run':
      break
    case 'list':
    case 'ls':
      // 'npm ls' => 'bun pm ls'
      args = convertInstallArgs(args)
      args[0] = 'ls'
      args.unshift('pm')
      break
    case 'init':
    case 'create':
      if (args[1]) {
        if (args[1].startsWith('@')) {
          cmd = 'bunx'

          args[1] = args[1].replace('/', '/create-')
          args = args.slice(1)
        } else if (!args[1].startsWith('-')) {
          cmd = 'bunx'
          args[1] = `create-${args[1].replace('@latest', '')}`
          args = args.slice(1)
        } else {
          args[0] = 'init'
        }
      }
      break

    case 'link':
    case 'ln':
      args = convertInstallArgs(args)
      args[0] = 'link'
      break
    case 'stop':
    case 'start':
    case 'unlink':
      break
    case 'test':
    case 't':
    case 'tst':
      args[0] = 'test'
      args.unshift('run')
      break
    case 'exec':
      cmd = 'bunx'
      args.splice(0, 1)
      break
    default:
      // null == keep `npm` command
      cmd = 'npm'
      break
  }

  const filtered = args.filter(Boolean).filter(arg => arg !== '--')
  return `${cmd} ${filtered.join(' ')}${
    cmd === 'npm' ? "\n# couldn't auto-convert command" : ''
  }`.replace('=', ' ')
}

```

### File: src\npmToPnpm.ts
```ts
import { parse } from './command'

function convertPnpmInstallArgs (args: string[]) {
  return args.map(item => {
    switch (item) {
      case '--save':
      case '-S':
        return ''
      case '--no-package-lock':
        return '--frozen-lockfile'
      // case '--save-dev':
      // case '-D':
      // case '--save-prod':
      // case '-P':
      // case '--save-optional':
      // case '-O':
      // case '--save-exact':
      // case '-E':
      // case '--global':
      // case '-g':
      default:
        return item
    }
  })
}

function convertFilterArg (args: string[]) {
  if (args.length > 1) {
    const filter = args.filter((item, index) => index !== 0 && !item.startsWith('-'))
    if (filter.length > 0) {
      args = args.filter((item, index) => index === 0 || item.startsWith('-'))
      args.push('--filter')
      args.push(filter.join(' '))
    }
  }

  return args
}

const npmToPnpmTable = {
  // ------------------------------
  install (args: string[]) {
    if (args.length > 1 && args.filter(item => !item.startsWith('-')).length > 1) {
      args[0] = 'add'
    }
    return convertPnpmInstallArgs(args)
  },
  i (args: string[]) {
    return npmToPnpmTable.install(args)
  },
  // ------------------------------
  uninstall (args: string[]) {
    args[0] = 'remove'

    return convertPnpmInstallArgs(args)
  },
  un (args: string[]) {
    return npmToPnpmTable.uninstall(args)
  },
  remove (args: string[]) {
    return npmToPnpmTable.uninstall(args)
  },
  r (args: string[]) {
    return npmToPnpmTable.uninstall(args)
  },
  rm (args: string[]) {
    return npmToPnpmTable.uninstall(args)
  },
  // ------------------------------
  rb (args: string[]) {
    return npmToPnpmTable.rebuild(args)
  },
  rebuild (args: string[]) {
    args[0] = 'rebuild'
    return convertFilterArg(args)
  },
  run: 'run',
  exec: 'exec',
  ls (args: string[]) {
    return npmToPnpmTable.list(args)
  },
  list (args: string[]) {
    return args.map(item => {
      if (item.startsWith('--depth=')) {
        return `--depth ${item.split('=')[1]}`
      }
      switch (item) {
        case '--production':
          return '--prod'
        case '--development':
          return '--dev'
        default:
          return item
      }
    })
  },
  init (args: string[]) {
    if (args[1] && !args[1].startsWith('-')) {
      args[0] = 'create'
      const m = args[1].match(/(.+)@latest/)
      if (m) {
        args[1] = m[1]
      }
    }
    return args.filter(item => item !== '--scope')
  },
  create (args: string[]) {
    return npmToPnpmTable.init(args)
  },
  ln: 'link',
  t: 'test',
  test: 'test',
  tst: 'test',
  start: 'start',
  link: 'link',
  unlink (args: string[]) {
    return convertFilterArg(args)
  },
  outdated: 'outdated',
  pack: (args: string[]) => {
    return args.map(item => {
      if (item.startsWith('--pack-destination')) {
        return item.replace(/^--pack-destination[\s=]/, '--pack-destination ')
      }
      return item
    })
  }
}

export function npmToPnpm (_m: string, command: string): string {
  let args = parse((command || '').trim())

  const index = args.findIndex(a => a === '--')
  if (index >= 0) {
    args.splice(index, 1)
  }

  if (args[0] in npmToPnpmTable) {
    const converter = npmToPnpmTable[args[0] as keyof typeof npmToPnpmTable]

    if (typeof converter === 'function') {
      args = converter(args)
    } else {
      args[0] = converter
    }

    return 'pnpm ' + args.filter(Boolean).join(' ')
  } else {
    return 'npm ' + command + "\n# couldn't auto-convert command"
  }
}

```

### File: src\npmToYarn.ts
```ts
import { unchangedCLICommands, yarnCLICommands } from './utils'
import { parse } from './command'

function convertInstallArgs (args: string[]) {
  if (args.includes('--global') || args.includes('-g')) {
    args.unshift('global')
  }

  return args.map(item => {
    switch (item) {
      case '--save-dev':
      case '-D':
        return '--dev'
      case '--save-prod':
      case '-P':
        return '--production'
      case '--no-package-lock':
        return '--no-lockfile'
      case '--save-optional':
      case '-O':
        return '--optional'
      case '--save-exact':
      case '-E':
        return '--exact'
      case '--save':
      case '-S':
      case '--global':
      case '-g':
        return ''
      default:
        return item
    }
  })
}

const npmToYarnTable = {
  install (args: string[]) {
    if (args.length === 1) {
      return ['install']
    }
    args[0] = 'add'

    return convertInstallArgs(args)
  },
  i (args: string[]) {
    return npmToYarnTable.install(args)
  },
  uninstall (args: string[]) {
    args[0] = 'remove'

    return convertInstallArgs(args)
  },
  un (args: string[]) {
    return npmToYarnTable.uninstall(args)
  },
  remove (args: string[]) {
    return npmToYarnTable.uninstall(args)
  },
  r (args: string[]) {
    return npmToYarnTable.uninstall(args)
  },
  rm (args: string[]) {
    return npmToYarnTable.uninstall(args)
  },
  version (args: string[]) {
    return args.map(item => {
      switch (item) {
        case 'major':
          return '--major'
        case 'minor':
          return '--minor'
        case 'patch':
          return '--patch'
        default:
          return item
      }
    })
  },
  rb (args: string[]) {
    return npmToYarnTable.rebuild(args)
  },
  rebuild (args: string[]) {
    args[0] = 'add'
    args.push('--force')
    return args
  },
  run (args: string[]) {
    if (args[1] && !unchangedCLICommands.includes(args[1]) && !yarnCLICommands.includes(args[1])) {
      args.splice(0, 1)
    }
    return args
  },
  exec (args: string[]) {
    args[0] = 'run'
    return npmToYarnTable.run(args)
  },
  ls (args: string[]) {
    args[0] = 'list'

    let ended = false
    const packages = args.filter((item, id) => {
      if (id > 0 && !ended) {
        ended = item.startsWith('-')
        return !ended
      }
      return false
    })
    if (packages.length > 0) {
      args.splice(1, packages.length, '--pattern', '"' + packages.join('|') + '"')
    }
    return args
  },
  list (args: string[]) {
    return npmToYarnTable.ls(args)
  },
  init (args: string[]) {
    if (args[1] && !args[1].startsWith('-')) {
      args[0] = 'create'
      const m = args[1].match(/(.+)@latest/)
      if (m) {
        args[1] = m[1]
      }
    }
    return args.filter(item => item !== '--scope')
  },
  create (args: string[]) {
    return npmToYarnTable.init(args)
  },
  ln: 'link',
  t: 'test',
  tst: 'test',
  outdated: 'outdated',
  pack (args: string[]) {
    return args.map(item => {
      if (item.startsWith('--pack-destination')) {
        return item.replace(/^--pack-destination[\s=]/, '--filename ')
      }
      return item
    })
  }
}

export function npmToYarn (_m: string, command: string): string {
  let args = parse((command || '').trim())

  const index = args.findIndex(a => a === '--')
  if (index >= 0) {
    args.splice(index, 1)
  }

  if (unchangedCLICommands.includes(args[0])) {
    return 'yarn ' + args.filter(Boolean).join(' ')
  } else if (args[0] in npmToYarnTable) {
    const converter = npmToYarnTable[args[0] as keyof typeof npmToYarnTable]

    if (typeof converter === 'function') {
      args = converter(args)
    } else {
      args[0] = converter
    }

    return 'yarn ' + args.filter(Boolean).join(' ')
  } else {
    return 'npm ' + command + "\n# couldn't auto-convert command"
  }
}

```

### File: src\utils.ts
```ts
export const unchangedCLICommands = [
  'test',
  'login',
  'logout',
  'link',
  'unlink',
  'publish',
  'cache',
  'start',
  'stop',
  'test'
]

export const yarnCLICommands = [
  'init',
  'run',
  'add',
  'audit',
  'autoclean',
  'bin',
  'check',
  'config',
  'create',
  'dedupe',
  'generate-lock-entry',
  'global',
  'help',
  'import',
  'info',
  'install',
  'licenses',
  'list',
  'lockfile',
  'outdated',
  'owner',
  'pack',
  'policies',
  'prune',
  'remove',
  'self-update',
  'tag',
  'team',
  'upgrade',
  'upgrade-interactive',
  'version',
  'versions',
  'why',
  'workspace',
  'workspaces'
]

export const npmCLICommands = [
  'init',
  'run',
  'access',
  'adduser',
  'audit',
  'bin',
  'bugs',
  'build',
  'bundle',
  'ci',
  'completion',
  'config',
  'dedupe',
  'deprecate',
  'dist-tag',
  'docs',
  'doctor',
  'edit',
  'explore',
  'exec',
  'fund',
  'help-search',
  'help',
  'hook',
  'install-ci-test',
  'install-test',
  'install',
  'ls',
  'list',
  'npm',
  'org',
  'outdated',
  'owner',
  'pack',
  'ping',
  'prefix',
  'profile',
  'prune',
  'rebuild',
  'repo',
  'restart',
  'root',
  'run-script',
  'search',
  'shrinkwrap',
  'star',
  'stars',
  'start',
  'stop',
  'team',
  'token',
  'uninstall',
  'unpublish',
  'update',
  'version',
  'view',
  'whoami'
]

export const executorCommands = {
  npm: 'npx',
  yarn: 'yarn dlx',
  pnpm: 'pnpm dlx',
  bun: 'bun x'
}

```

### File: src\yarnToNpm.ts
```ts
import { unchangedCLICommands, yarnCLICommands } from './utils'
import { parse } from './command'

function convertAddRemoveArgs (args: string[]) {
  return args.map(item => {
    switch (item) {
      case '--no-lockfile':
        return '--no-package-lock'
      case '--production':
        return '--save-prod'
      case '--dev':
        return '--save-dev'
      case '--optional':
        return '--save-optional'
      case '--exact':
        return '--save-exact'
      default:
        return item
    }
  })
}

const yarnToNpmTable = {
  add (args: string[]) {
    if (args.length === 2 && args[1] === '--force') {
      return ['rebuild']
    }
    args[0] = 'install'
    return convertAddRemoveArgs(args)
  },
  remove (args: string[]) {
    args[0] = 'uninstall'
    return convertAddRemoveArgs(args)
  },
  version (args: string[]) {
    return args.map(item => {
      switch (item) {
        case '--major':
          return 'major'
        case '--minor':
          return 'minor'
        case '--patch':
          return 'patch'
        default:
          return item
      }
    })
  },
  install: 'install',
  list (args: string[]) {
    args[0] = 'ls'
    const patternIndex = args.findIndex(item => item === '--pattern')
    if (patternIndex >= 0 && args[patternIndex + 1]) {
      const packages = args[patternIndex + 1].replace(/["']([^"']+)["']/, '$1').split('|')
      args.splice(patternIndex, 2, packages.join(' '))
    }
    return args
  },
  init: 'init',
  create: 'init',
  outdated: 'outdated',
  run: 'run',
  global (args: string[]) {
    switch (args[1]) {
      case 'add':
        args.shift()
        args = yarnToNpmTable.add(args)
        args.push('--global')
        return args
      case 'remove':
        args.shift()
        args = yarnToNpmTable.remove(args)
        args.push('--global')
        return args
      case 'list':
        args.shift()
        args = yarnToNpmTable.list(args)
        args.push('--global')
        return args
      // case 'bin':
      // case 'upgrade':
      default:
        args.push("\n# couldn't auto-convert command")
        return args
    }
  },
  pack (args: string[]) {
    return args.map(item => {
      if (item === '--filename') {
        return '--pack-destination'
      }
      return item
    })
  }
}

export function yarnToNPM (_m: string, command: string): string {
  command = (command || '').trim()
  if (command === '') {
    return 'npm install'
  }
  let args = parse(command)
  const firstCommand = (/\w+/.exec(command) || [''])[0]

  if (unchangedCLICommands.includes(args[0])) {
    return 'npm ' + command
  } else if (args[0] in yarnToNpmTable) {
    const converter = yarnToNpmTable[args[0] as keyof typeof yarnToNpmTable]

    if (typeof converter === 'function') {
      args = converter(args)
    } else {
      args[0] = converter
    }

    return 'npm ' + args.filter(Boolean).join(' ')
  } else if (!yarnCLICommands.includes(firstCommand)) {
    // i.e., yarn grunt -> npm run grunt
    return 'npm run ' + command
  } else {
    return 'npm ' + command + "\n# couldn't auto-convert command"
  }
}

```

### File: test\commands.spec.ts
```ts
import { parse } from '../src/command'

describe('should parse command correctly', () => {
  it('simple', () => {
    expect(parse('npm')).toEqual(['npm'])
    expect(parse('npm test')).toEqual(['npm', 'test'])
    expect(parse('npm test bar')).toEqual(['npm', 'test', 'bar'])
  })
  it('with params', () => {
    expect(parse('npm --bar')).toEqual(['npm', '--bar'])
    expect(parse('npm -- --bar')).toEqual(['npm', '--', '--bar'])
  })
  it('with strings', () => {
    expect(parse('npm ""')).toEqual(['npm', '""'])
    expect(parse('npm "test"')).toEqual(['npm', '"test"'])
    expect(parse("npm ''")).toEqual(['npm', "''"])
    expect(parse("npm 'test'")).toEqual(['npm', "'test'"])
  })
  it('with string params', () => {
    expect(parse('npm --bar ""')).toEqual(['npm', '--bar', '""'])
    expect(parse('npm --bar "test"')).toEqual(['npm', '--bar', '"test"'])
    expect(parse("npm --bar ''")).toEqual(['npm', '--bar', "''"])
    expect(parse("npm --bar 'test'")).toEqual(['npm', '--bar', "'test'"])
    expect(parse('yarn add test --no-lockfile')).toEqual(['yarn', 'add', 'test', '--no-lockfile'])
  })
  it('with space in strings', () => {
    expect(parse('npm --bar "test 123"')).toEqual(['npm', '--bar', '"test 123"'])
    expect(parse("npm --bar 'test 123'")).toEqual(['npm', '--bar', "'test 123'"])
    expect(parse('npm --bar "test \' 123"')).toEqual(['npm', '--bar', '"test \' 123"'])
    expect(parse('npm --bar "test \\" 123"')).toEqual(['npm', '--bar', '"test \\" 123"'])
    expect(parse("npm --bar 'test \" 123'")).toEqual(['npm', '--bar', "'test \" 123'"])
    expect(parse("npm --bar 'test \\' 123'")).toEqual(['npm', '--bar', "'test \\' 123'"])
    expect(parse("npm 'test \\' 123 --bar'")).toEqual(['npm', "'test \\' 123 --bar'"])
    expect(parse('npm "test \\" 123 --bar"')).toEqual(['npm', '"test \\" 123 --bar"'])
    expect(parse('npm "a \\" 11" "b \\" 22"')).toEqual(['npm', '"a \\" 11"', '"b \\" 22"'])
  })
})

```

### File: test\index.spec.ts
```ts
/* global it, expect, describe */

import convert from '../src'

describe('NPM tests', () => {
  const tests: [npm: string, yarn: string, pnpm: string, bun: string][] = [
    // install
    ['npm install', 'yarn install', 'pnpm install', 'bun install'],
    ['npm i', 'yarn install', 'pnpm i', 'bun install'],
    ['npm i squirrelly', 'yarn add squirrelly', 'pnpm add squirrelly', 'bun add squirrelly'],
    ['npm install squirrelly', 'yarn add squirrelly', 'pnpm add squirrelly', 'bun add squirrelly'],
    [
      'npm install my--save-dev',
      'yarn add my--save-dev',
      'pnpm add my--save-dev',
      'bun add my--save-dev',
    ],
    [
      'npm install squirrelly --no-package-lock',
      'yarn add squirrelly --no-lockfile',
      'pnpm add squirrelly --frozen-lockfile',
      'bun add squirrelly --no-save',
    ],
    [
      'npm install squirrelly --save-optional',
      'yarn add squirrelly --optional',
      'pnpm add squirrelly --save-optional',
      'bun add squirrelly --optional',
    ],
    [
      'npm install squirrelly -O',
      'yarn add squirrelly --optional',
      'pnpm add squirrelly -O',
      'bun add squirrelly --optional',
    ],
    [
      'npm install squirrelly --save-exact',
      'yarn add squirrelly --exact',
      'pnpm add squirrelly --save-exact',
      'bun add squirrelly --exact',
    ],
    [
      'npm install squirrelly -E',
      'yarn add squirrelly --exact',
      'pnpm add squirrelly -E',
      'bun add squirrelly --exact',
    ],
    [
      'npm install squirrelly --save-dev',
      'yarn add squirrelly --dev',
      'pnpm add squirrelly --save-dev',
      'bun add squirrelly --dev',
    ],
    [
      'npm install squirrelly -D',
      'yarn add squirrelly --dev',
      'pnpm add squirrelly -D',
      'bun add squirrelly --dev',
    ],
    [
      'npm install squirrelly --save-prod',
      'yarn add squirrelly --production',
      'pnpm add squirrelly --save-prod',
      'bun add squirrelly --production',
    ],
    [
      'npm install squirrelly -P',
      'yarn add squirrelly --production',
      'pnpm add squirrelly -P',
      'bun add squirrelly --production',
    ],
    [
      'npm install squirrelly --save',
      'yarn add squirrelly',
      'pnpm add squirrelly',
      'bun add squirrelly',
    ],
    [
      'npm install squirrelly -S',
      'yarn add squirrelly',
      'pnpm add squirrelly',
      'bun add squirrelly',
    ],
    [
      'npm install squirrelly --global',
      'yarn global add squirrelly',
      'pnpm add squirrelly --global',
      'bun add squirrelly --global',
    ],
    [
      'npm install squirrelly -g',
      'yarn global add squirrelly',
      'pnpm add squirrelly -g',
      'bun add squirrelly --global',
    ],
    [
      'npm install squirrelly --no-save',
      'yarn add squirrelly --no-save',
      'pnpm add squirrelly --no-save',
      'bun add squirrelly --no-save',
    ],
    // uninstall
    ['npm r squirrelly', 'yarn remove squirrelly', 'pnpm remove squirrelly', 'bun remove squirrelly'],
    ['npm remove squirrelly', 'yarn remove squirrelly', 'pnpm remove squirrelly', 'bun remove squirrelly'],
    ['npm uninstall squirrelly', 'yarn remove squirrelly', 'pnpm remove squirrelly', 'bun remove squirrelly'],
    [
      'npm un squirrelly',
      'yarn remove squirrelly',
      'pnpm remove squirrelly',
      'bun remove squirrelly',
    ],
    [
      'npm uninstall squirrelly --global',
      'yarn global remove squirrelly',
      'pnpm remove squirrelly --global',
      'bun remove squirrelly --global',
    ],
    // cache
    [
      'npm cache clean',
      'yarn cache clean',
      "npm cache clean\n# couldn't auto-convert command",
      'bun pm cache rm',
    ],
    // version
    [
      'npm version',
      'yarn version',
      "npm version\n# couldn't auto-convert command",
      "npm version\n# couldn't auto-convert command",
    ],
    [
      'npm version major',
      'yarn version --major',
      "npm version major\n# couldn't auto-convert command",
      "npm version major\n# couldn't auto-convert command",
    ],
    [
      'npm version minor',
      'yarn version --minor',
      "npm version minor\n# couldn't auto-convert command",
      "npm version minor\n# couldn't auto-convert command",
    ],
    [
      'npm version patch',
      'yarn version --patch',
      "npm version patch\n# couldn't auto-convert command",
      "npm version patch\n# couldn't auto-convert command",
    ],
    // rebuild
    ['npm rebuild', 'yarn add --force', 'pnpm rebuild', 'bun add --force'],
    ['npm rb', 'yarn add --force', 'pnpm rebuild', 'bun add --force'],
    [
      'npm rebuild package',
      'yarn add package --force',
      'pnpm rebuild --filter package',
      'bun add package --force',
    ],
    [
      'npm rb package',
      'yarn add package --force',
      'pnpm rebuild --filter package',
      'bun add package --force',
    ],
    // run
    ['npm run', 'yarn run', 'pnpm run', 'bun run'],
    ['npm run package', 'yarn package', 'pnpm run package', 'bun run package'],
    [
      'npm run test -- --version',
      'yarn run test --version',
      'pnpm run test --version',
      'bun run test --version',
    ],
    ['npm run test -- -v', 'yarn run test -v', 'pnpm run test -v', 'bun run test -v'],
    ['npm run custom', 'yarn custom', 'pnpm run custom', 'bun run custom'],
    ['npm run add', 'yarn run add', 'pnpm run add', 'bun run add'],
    ['npm run install', 'yarn run install', 'pnpm run install', 'bun run install'],
    ['npm run run', 'yarn run run', 'pnpm run run', 'bun run run'],
    ['npm exec custom', 'yarn custom', 'pnpm exec custom', 'bunx custom'],
    ['npm exec add', 'yarn run add', 'pnpm exec add', 'bunx add'],
    ['npm exec install', 'yarn run install', 'pnpm exec install', 'bunx install'],
    ['npm exec run', 'yarn run run', 'pnpm exec run', 'bunx run'],
    ['npm exec custom -- --version', 'yarn custom --version', 'pnpm exec custom --version', 'bunx custom --version'],
    // test
    ['npm test', 'yarn test', 'pnpm test', 'bun run test'],
    ['npm t', 'yarn test', 'pnpm test', 'bun run test'],
    ['npm tst', 'yarn test', 'pnpm test', 'bun run test'],
    [
      'npm test -- --version',
      'yarn test --version',
      'pnpm test --version',
      'bun run test --version',
    ],
    ['npm test -- -v', 'yarn test -v', 'pnpm test -v', 'bun run test -v'],
    // unchanged
    ['npm start', 'yarn start', 'pnpm start', 'bun start'],
    ['npm stop', 'yarn stop', "npm stop\n# couldn't auto-convert command", 'bun stop'],
    // unsupported
    [
      'npm whoami',
      "npm whoami\n# couldn't auto-convert command",
      "npm whoami\n# couldn't auto-convert command",
      "npm whoami\n# couldn't auto-convert command",
    ],
    // init
    ['npm init', 'yarn init', 'pnpm init', 'bun init'],
    ['npm init -y', 'yarn init -y', 'pnpm init -y', 'bun init -y'],
    ['npm init --yes', 'yarn init --yes', 'pnpm init --yes', 'bun init --yes'],
    ['npm init --scope', 'yarn init', 'pnpm init', 'bun init --scope'],
    ['npm init --private', 'yarn init --private', 'pnpm init --private', 'bun init --private'],
    [
      'npm init --unknown-arg',
      'yarn init --unknown-arg',
      'pnpm init --unknown-arg',
      'bun init --unknown-arg',
    ],
    ['npm init esm --yes', 'yarn create esm --yes', 'pnpm create esm --yes', 'bunx create-esm --yes'],
    [
      'npm init @scope/my-package',
      'yarn create @scope/my-package',
      'pnpm create @scope/my-package',
      'bunx @scope/create-my-package',
    ],
    [
      'npm init react-app ./my-react-app',
      'yarn create react-app ./my-react-app',
      'pnpm create react-app ./my-react-app',
      'bunx create-react-app ./my-react-app',
    ],
    // create
    [
      'npm create react-app ./my-react-app',
      'yarn create react-app ./my-react-app',
      'pnpm create react-app ./my-react-app',
      'bunx create-react-app ./my-react-app',
    ],
    [
      'npm create vite@latest',
      'yarn create vite',
      'pnpm create vite',
      'bunx create-vite',
    ],
    // list
    ['npm list', 'yarn list', 'pnpm list', 'bun pm ls'],
    ['npm ls', 'yarn list', 'pnpm ls', 'bun pm ls'],
    [
      'npm list --production',
      'yarn list --production',
      'pnpm list --prod',
      'bun pm ls --production',
    ],
    ['npm list --development', 'yarn list --development', 'pnpm list --dev', 'bun pm ls --dev'],
    ['npm list --global', 'yarn list --global', 'pnpm list --global', 'bun pm ls --global'],
    ['npm list --depth=0', 'yarn list --depth=0', 'pnpm list --depth 0', 'bun pm ls --depth 0'],
    ['npm list package', 'yarn list --pattern "package"', 'pnpm list package', 'bun pm ls package'],
    [
      'npm list package package2',
      'yarn list --pattern "package|package2"',
      'pnpm list package package2',
      'bun pm ls package package2',
    ],
    [
      'npm list @scope/package @scope/package2',
      'yarn list --pattern "@scope/package|@scope/package2"',
      'pnpm list @scope/package @scope/package2',
      'bun pm ls @scope/package @scope/package2',
    ],
    [
      'npm list @scope/package @scope/package2 --depth=2',
      'yarn list --pattern "@scope/package|@scope/package2" --depth=2',
      'pnpm list @scope/package @scope/package2 --depth 2',
      'bun pm ls @scope/package @scope/package2 --depth 2',
    ],
    [
      'npm list @scope/package @scope/package2 --depth 2',
      'yarn list --pattern "@scope/package|@scope/package2" --depth 2',
      'pnpm list @scope/package @scope/package2 --depth 2',
      'bun pm ls @scope/package @scope/package2 --depth 2',
    ],
    [
      'npm list @scope/package --json',
      'yarn list --pattern "@scope/package" --json',
      'pnpm list @scope/package --json',
      'bun pm ls @scope/package --json',
    ],
    // link
    ['npm ln', 'yarn link', 'pnpm link', 'bun link'],
    ['npm ln package', 'yarn link package', 'pnpm link package', 'bun link package'],
    ['npm link', 'yarn link', 'pnpm link', 'bun link'],
    ['npm link package', 'yarn link package', 'pnpm link package', 'bun link package'],
    // unlink
    ['npm unlink', 'yarn unlink', 'pnpm unlink', 'bun unlink'],
    [
      'npm unlink package',
      'yarn unlink package',
      'pnpm unlink --filter package',
      'bun unlink package',
    ],
    // outdated
    [
      'npm outdated',
      'yarn outdated',
      'pnpm outdated',
      "npm outdated\n# couldn't auto-convert command",
    ],
    [
      'npm outdated --json',
      'yarn outdated --json',
      'pnpm outdated --json',
      "npm outdated --json\n# couldn't auto-convert command",
    ],
    [
      'npm outdated --long',
      'yarn outdated --long',
      'pnpm outdated --long',
      "npm outdated --long\n# couldn't auto-convert command",
    ],
    [
      'npm outdated lodash',
      'yarn outdated lodash',
      'pnpm outdated lodash',
      "npm outdated lodash\n# couldn't auto-convert command",
    ],
    // pack
    ['npm pack', 'yarn pack', 'pnpm pack', "npm pack\n# couldn't auto-convert command"],
    [
      'npm pack --pack-destination=foobar',
      'yarn pack --filename foobar',
      'pnpm pack --pack-destination foobar',
      "npm pack --pack-destination foobar\n# couldn't auto-convert command",
    ],
  ];

  describe('to Yarn', () => {
    it.each(tests)('%s', (npmValue, yarnValue) => {
      expect(convert(npmValue, 'yarn')).toEqual(yarnValue)
    })
  })

  describe('to PNPM', () => {
    it.each(tests)('%s', (npmValue, _yarnValue, pnpmValue) => {
      expect(convert(npmValue, 'pnpm')).toEqual(pnpmValue)
    })
  })

  describe('to Bun', () => {
    it.each(tests)('%s', (npmValue, _yarnValue, _pnpmValue, bunValue) => {
      expect(convert(npmValue, 'bun')).toEqual(bunValue)
    })
  })
})

describe('Yarn to NPM tests', () => {
  const tests = [
    // install
    ['yarn', 'npm install'],
    ['yarn install', 'npm install'],
    // add
    ['yarn add squirrelly', 'npm install squirrelly'],
    ['yarn add squirrelly --no-lockfile', 'npm install squirrelly --no-package-lock'],
    ['yarn add squirrelly --optional', 'npm install squirrelly --save-optional'],
    ['yarn add squirrelly --exact', 'npm install squirrelly --save-exact'],
    ['yarn add squirrelly --production', 'npm install squirrelly --save-prod'],
    ['yarn add squirrelly --dev', 'npm install squirrelly --save-dev'],
    ['yarn add --force', 'npm rebuild'],
    ['yarn add package --force', 'npm install package --force'],
    // remove
    ['yarn remove squirrelly', 'npm uninstall squirrelly'],
    ['yarn remove squirrelly --dev', 'npm uninstall squirrelly --save-dev'],
    // cache
    ['yarn cache clean', 'npm cache clean'],
    // implied run
    ['yarn grunt', 'npm run grunt'],
    // global
    ['yarn global add squirrelly', 'npm install squirrelly --global'],
    ['yarn global remove squirrelly', 'npm uninstall squirrelly --global'],
    ['yarn global squirrelly', "npm global squirrelly \n# couldn't auto-convert command"],
    ['yarn global list', 'npm ls --global'],
    // version
    ['yarn version', 'npm version'],
    ['yarn version --major', 'npm version major'],
    ['yarn version --minor', 'npm version minor'],
    ['yarn version --patch', 'npm version patch'],
    // init
    ['yarn init', 'npm init'],
    ['yarn init -y', 'npm init -y'],
    ['yarn init --yes', 'npm init --yes'],
    ['yarn init --private', 'npm init --private'],
    ['yarn init --unknown-arg', 'npm init --unknown-arg'],
    // create
    ['yarn create esm --yes', 'npm init esm --yes'],
    ['yarn create @scope/my-package', 'npm init @scope/my-package'],
    ['yarn create react-app ./my-react-app', 'npm init react-app ./my-react-app'],
    // unchanged
    ['yarn start', 'npm start'],
    ['yarn stop', 'npm stop'],
    ['yarn test', 'npm test'],
    // run
    ['yarn run', 'npm run'],
    ['yarn custom', 'npm run custom'],
    ['yarn run custom', 'npm run custom'],
    ['yarn run add', 'npm run add'],
    ['yarn run install', 'npm run install'],
    ['yarn run run', 'npm run run'],
    ['yarn run --silent', 'npm run --silent'],
    ['yarn custom -- --version', 'npm run custom -- --version'],
    ['yarn run custom -- --version', 'npm run custom -- --version'],
    ['yarn run custom --version', 'npm run custom --version'],
    // list
    ['yarn list', 'npm ls'],
    ['yarn list --pattern "package"', 'npm ls package'],
    ['yarn list --pattern "package|package2"', 'npm ls package package2'],
    [
      'yarn list --pattern "@scope/package|@scope/package2"',
      'npm ls @scope/package @scope/package2'
    ],
    ['yarn list --depth 2', 'npm ls --depth 2'],
    ['yarn list --json', 'npm ls --json'],
    ['yarn list --production', 'npm ls --production'],
    ['yarn list --development', 'npm ls --development'],
    // link/unlink
    ['yarn link', 'npm link'],
    ['yarn link custom', 'npm link custom'],
    ['yarn unlink', 'npm unlink'],
    ['yarn 
... [TRUNCATED]
```

### File: .github\ISSUE_TEMPLATE\bug_report.md
```md
---
name: 🐛 Bug report
about: Create a report to help us improve
---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:

1. Type in '...'
2. Call function '...'
3. Look at result in '...'

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Package & Environment Details**

- Environment: ex. Node, Chrome, Firefox, etc. and what version
- Version: ex. 8.1.0

**Additional context**
Add any other context about the problem here.

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

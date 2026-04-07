---
id: npkill
type: knowledge
owner: OA_Triage
---
# npkill
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "npkill",
  "version": "0.12.2",
  "description": "List any node_modules directories in your system, as well as the space they take up. You can then select which ones you want to erase to free up space.",
  "exports": "./lib/index.js",
  "type": "module",
  "engines": {
    "node": ">=18.18.0"
  },
  "publishConfig": {
    "access": "public"
  },
  "bin": {
    "npkill": "lib/index.js"
  },
  "author": "Nya Garcia & Juan Torres",
  "repository": {
    "type": "git",
    "url": "https://github.com/zaldih/npkill"
  },
  "license": "MIT",
  "keywords": [
    "cli",
    "free up space",
    "npm",
    "node",
    "modules",
    "clean",
    "tool",
    "delete",
    "find",
    "interactive"
  ],
  "files": [
    "lib/**/*"
  ],
  "scripts": {
    "build": "tsc",
    "start": "node -r tsconfig-paths/register --loader ts-node/esm --no-warnings ./src/index.ts",
    "test": "node --experimental-vm-modules --experimental-modules node_modules/jest/bin/jest.js",
    "test:watch": "npm run test -- --watch",
    "test:mutant": "stryker run",
    "release": "npm run build && np",
    "debug": "TS_NODE_FILES=true node --inspect -r ts-node/register ./src/index.ts",
    "prepare": "husky install",
    "format": "prettier --write .",
    "lint": "eslint"
  },
  "dependencies": {
    "ansi-escapes": "7.1.1",
    "open-file-explorer": "1.0.2",
    "picocolors": "1.1.1"
  },
  "devDependencies": {
    "@commitlint/config-conventional": "20.0.0",
    "@eslint/js": "9.38.0",
    "@jest/globals": "30.2.0",
    "@stryker-mutator/core": "9.2.0",
    "@stryker-mutator/jest-runner": "9.2.0",
    "@types/jest": "30.0.0",
    "@types/node": "18.18.0",
    "commitlint": "20.1.0",
    "del": "8.0.1",
    "eslint": "9.38.0",
    "eslint-config-prettier": "10.1.8",
    "eslint-plugin-n": "17.23.1",
    "eslint-plugin-promise": "7.2.1",
    "husky": "9.1.7",
    "jest": "30.2.0",
    "lint-staged": "15.5.2",
    "np": "10.2.0",
    "prettier": "3.6.2",
    "rimraf": "5.0.10",
    "ts-jest": "29.4.5",
    "ts-node": "10.9.2",
    "tslint": "6.1.3",
    "typescript": "5.8.3",
    "typescript-eslint": "8.46.2"
  },
  "peerDependencies": {
    "rxjs": "^7.8.2"
  },
  "husky": {
    "hooks": {
      "commit-msg": "commitlint -E HUSKY_GIT_PARAMS",
      "pre-commit": "lint-staged"
    }
  },
  "commitlint": {
    "extends": [
      "@commitlint/config-conventional"
    ]
  },
  "lint-staged": {
    "*.{js,ts,css,json,md}": [
      "prettier --write"
    ]
  },
  "ethereum": "0x7668e86c8bdb52034606db5aa0d2d4d73a0d4259"
}

```

### File: README.md
```md
<p align="center">
  <img src="./docs/npkill-text-clean.svg" width="380" alt="npkill logo" />
</p>
<p align="center">
<img alt="npm" src="https://img.shields.io/npm/dy/npkill.svg">
<a href="#donations"><img src="https://img.shields.io/badge/donate-<3-red" alt="Donations Badge"/></a>
<img alt="npm version" src="https://img.shields.io/npm/v/npkill.svg">
<img alt="NPM" src="https://img.shields.io/npm/l/npkill.svg">
</p>

### Easily find and **remove** old and heavy <font color="red">**node_modules**</font> folders :sparkles:

<p align="center">
  <img src="/docs/npkill-demo-0.10.0.gif" alt="npkill demo GIF" />
</p>

This tool allows you to list any _node_modules_ directories in your system, as well as the space they take up. You can then select which ones you want to erase to free up space. Yay!

## i18n

We're making an effort to internationalize the Npkill docs. Here's a list of the available translations:

- [Español](./README.es.md)
- [Indonesian](./README.id.md)
- [Português](./README.pt.md)
- [Turkish](./README.tr.md)

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Multi-Select Mode](#multi-select-mode)
  - [Options](#options)
  - [Examples](#examples)
  - [JSON Output](#json-output)
- [Set Up Locally](#setup-locally)
- [API](#API)
- [Roadmap](#roadmap)
- [Known bugs](#known-bugs)
- [Contributing](#contributing)
- [Buy us a coffee](#donations)
- [License](#license)

<a name="features"></a>

# :heavy_check_mark: Features

- **Clear space:** Get rid of old and dusty _node_modules_ cluttering up your machine.

- **Last Workspace Usage**: Check when was the last time you modified a file in the workspace (indicated in the **last_mod** column).

- **Very fast:** NPKILL is written in TypeScript, but searches are performed at a low level, improving performance greatly.

- **Easy to use:** Say goodbye to lengthy commands. Using npkill is as simple as reading a list of your node_modules, and pressing Del to get rid of them. Could it be any easier? ;)

- **Minified:** It barely has any dependencies.

<a name="installation"></a>

# :cloud: Installation

You don't really need to install it to use it!
Simply use the following command:

```bash
$ npx npkill
```

Or if for some reason you really want to install it:

```bash
$ npm i -g npkill
# Unix users may need to run the command with sudo. Go carefully
```

> NPKILL does not support node<v14. If this affects you you can use `npkill@0.8.3`

<a name="usage"></a>

# :clipboard: Usage

```bash
$ npx npkill
# or just npkill if installed globally
```

By default, npkill will scan for node_modules starting at the path where `npkill` command is executed.

Move between the listed folders with <kbd>↓</kbd> <kbd>↑</kbd>, and use <kbd>Space</kbd> or <kbd>Del</kbd> to delete the selected folder.
You can also use <kbd>j</kbd> and <kbd>k</kbd> to move between the results.

You can open the directory where the selected result is placed by pressing <kbd>o</kbd>.

To exit, <kbd>Q</kbd> or <kbd>Ctrl</kbd> + <kbd>c</kbd> if you're brave.

**Important!** Some applications installed on the system need their node_modules directory to work and deleting them may break them. NPKILL will highlight them by displaying a :warning: to be careful.

## Search Mode

Search mode allows you to filter results. This can be particularly useful for limiting the view to a specific route or ensuring that only those results that meet the specified condition are “selected all.”

For example, you can use this expression to limit the results to those that are in the `work` directory and that include `data` somewhere in the path: `/work/.*/data`.

Press <kbd>/</kbd> to enter search mode. You can type a regex pattern to filter results.

Press <kbd>Enter</kbd> to confirm the search and navigate the filtered results, or <kbd>Esc</kbd> to clear and exit.

To exit from this mode, leave empty.

## Multi-Select Mode

This mode allows you to select and delete multiple folders at once, making it more efficient when cleaning up many directories.

### Entering Multi-Select Mode

Press <kbd>T</kbd> to toggle multi-select mode. When active, you'll see a selection counter and additional instructions at the top of the results.

### Controls

- **<kbd>Space</kbd>**: Toggle selection of the current folder.
- **<kbd>V</kbd>**: Start/end range selection mode.
- **<kbd>A</kbd>**: Toggle select/unselect all folders.
- **<kbd>Enter</kbd>**: Delete all selected folders.
- **<kbd>T</kbd>**: Unselect all and back to normal mode.

### Range Selection

After pressing <kbd>V</kbd> to enter range selection mode:

- Move the cursor with arrow keys, <kbd>j</kbd>/<kbd>k</kbd>, <kbd>Home</kbd>/<kbd>End</kbd>, or page up/down
- All folders between the starting position and current cursor position will be selected/deselected
- Press <kbd>V</kbd> again to exit range selection mode

<a name="options"></a>

## Options

| ARGUMENT                | DESCRIPTION                                                                                                                                                                   |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -p, --profiles          | Allows you to select the [profile](./docs/profiles.md) (set of targets) to use. If no option is specified, the available ones will be listed _(**node** by default)_.         |
| --config                | Path to a custom .npkillrc configuration file. By default, npkill looks first for `./.npkillrc` and then for `~/.npkillrc`.                                                   |
| -d, --directory         | Set the directory from which to begin searching. By default, starting-point is .                                                                                              |
| -D, --delete-all        | Automatically delete all folders that are found. Suggested to be used together with `-x`.                                                                                     |
| -e, --hide-errors       | Hide errors if any                                                                                                                                                            |
| -E, --exclude           | Exclude directories from search (directory list must be inside double quotes "", each directory separated by ',' ) Example: "ignore1, ignore2"                                |
| -f, --full              | Start searching from the home of the user (example: "/home/user" in linux)                                                                                                    |
| --size-unit             | Set the unit for displaying folder sizes. _(Available: **auto**, mb, gb)_. With auto, sizes < 1024MB are shown in MB (rounded), larger sizes in GB (with decimals).           |
| -h, --help, ?           | Show help page                                                                                                                                                                |
| -nu, --no-check-update  | Don't check for updates on startup                                                                                                                                            |
| -s, --sort              | Sort results by: `size`, `path` or `age`                                                                                                                                      |
| -t, --targets           | Disable profiles feature and specify the name of the directories you want to search for. You can define multiple targets separating with comma. Ej. `-t node_modules,.cache`. |
| -x, --exclude-sensitive | Exclude sensitive directories.                                                                                                                                                |
| -y                      | Avoid displaying a warning when executing --delete-all.                                                                                                                       |
| --dry-run               | It does not delete anything (will simulate it with a random delay).                                                                                                           |
| --json                  | Output results in JSON format at the end of the scan. Useful for automation and scripting.                                                                                    |
| --json-stream           | Output results in streaming JSON format (one JSON object per line as results are found). Useful for real-time processing.                                                     |
| -v, --version           | Show npkill version                                                                                                                                                           |

<a name="examples"></a>

## Examples

- Search **node_modules** directories in your _projects_ directory:

```bash
npkill -d ~/projects

# other alternative:
cd ~/projects
npkill
```

- List **node_modules** in your _projects_ directory, excluding the ones in _progress_ and _ignore-this_ directories:

```bash
npkill -d 'projects' --exclude "progress, ignore-this"
```

- Automatically delete all node_modules that have sneaked into your backups:

```bash
npkill -d ~/backups/ --delete-all
```

- Get results in JSON format for automation or further processing:

```bash
npkill --json > results.json
```

- Stream results in real-time as JSON (useful for monitoring or piping to other tools):

```bash
npkill --json-stream | jq '.'
```

- Save only successful results to a file, ignoring errors:

```bash
npkill --json-stream 2>/dev/null | jq -s '.' > clean-results.json
```

<a name="json-output"></a>

## JSON Output

Npkill supports JSON output formats for automation and integration with other tools:

- **`--json`**: Output all results as a single JSON object at the end of the scan
- **`--json-stream`**: Output each result as a separate JSON object in real-time

For detailed documentation, examples, and TypeScript interfaces, see [JSON Output Documentation](./docs/json-output.md).

**Quick Examples:**

```bash
# Get all results as JSON
npkill --json > results.json

# Process results in real-time
npkill --json-stream | jq '.result.path'

# Find directories larger than 100MB
npkill --json | jq '.results[] | select(.size > 104857600)'
```

<a name="setup-locally"></a>

# :pager: Set Up Locally

```bash
# -- First, clone the repository
git clone https://github.com/voidcosmos/npkill.git

# -- Navigate to the dir
cd npkill

# -- Install dependencies
npm install

# -- And run!
npm run start


# -- If you want to run it with some parameter, you will have to add "--" as in the following example:
npm run start -- -f -e
```

<a name="API"></a>

# :bookmark_tabs: API

The api allows you to interact with npkill from node to create your own implementations in your scripts (automations, for example).

You can check the basic API [here](./API.md) or on the web (comming soon).

<a name="roadmap"></a>

# :crystal_ball: Roadmap

- [x] Release 0.1.0 !
- [x] Improve code
  - [x] Improve performance
  - [ ] Improve performance even more!
- [x] Sort results by size and path
- [x] Allow the search for other types of directories (targets)
- [ ] Reduce dependencies to be a more minimalist module
- [ ] Allow to filter by directories that have not been used in a period of time
- [ ] Create option for displaying directories in tree format
- [x] Add some menus
- [x] Add log service
- [ ] Periodic and automatic cleaning (?)

<a name="known-bugs"></a>

# :bug: Known bugs :bug:

- Sometimes, CLI is blocked while folder is deleting.
- Sorting, especially by routes, can slow down the terminal when there are many results at the same time.
- Sometimes, size calculations are higher than they should be.
- (SOLVED) Performance issues when searching from high level directories (like / in linux).
- (SOLVED) Sometimes text collapses when updating the cli.
- (SOLVED) Analyzing the size of the directories takes longer than it should.

> If you find any bugs, don't hesitate and open an issue :)

<a name="contributing"></a>

# :revolving_hearts: Contributing

If you want to contribute check the [CONTRIBUTING.md](.github/CONTRIBUTING.md)

<a name="donations"></a>

# :coffee: Buy us a coffee

<img align="right" width="300" src="https://npkill.js.org/img/cat-donation-cup.png">
We have developed npkill in our free time, because we are passionate about the programming sector.
Tomorrow we would like to dedicate ourselves to this, but first, we have a long way to go.

We will continue to do things anyway, but donations are one of the many ways to support what we do.

<span class="badge-opencollective"><a href="https://opencollective.com/npkill/contribute" title="Donate to this project using Open Collective"><img src="https://img.shields.io/badge/open%20collective-donate-green.svg" alt="Open Collective donate button" /></a></span>

### Thanks!!

## A huge thank you to our backers :heart:

<a href="https://opencollective.com/npkill#backers" target="_blank"><img width="535" src="https://opencollective.com/npkill/tiers/backer.svg?width=535"></a>

---

### Crypto alternative

- btc: 1ML2DihUoFTqhoQnrWy4WLxKbVYkUXpMAX
- bch: 1HVpaicQL5jWKkbChgPf6cvkH8nyktVnVk
- eth: 0x7668e86c8bdb52034606db5aa0d2d4d73a0d4259

<a name="license"></a>

# :scroll: License

MIT © [Nya García Gallardo](https://github.com/NyaGarcia) and [Juan Torres Gómez](https://github.com/zaldih)

:cat::baby_chick:

---

```

### File: API.md
```md
# NPKill API

This document does not include all project documentation at this stage. It brings together the basic concepts.
For more details see the project interfaces.

- [NPKill API](#npkill-api)
  - [Interface: `Npkill`](#interface-npkill)
    - [`startScan$(rootPath, options?)`](#startscanrootpath-options)
    - [`stopScan()`](#stopscan)
    - [`getSize$(path, options?)`](#getsizepath-options)
    - [`getNewestFile$(path)`](#getnewestfilepath)
    - [`delete$(path, options?)`](#deletepath-options)
    - [`getLogs$()`](#getlogs)
    - [`isValidRootFolder(path)`](#isvalidrootfolderpath)
    - [`getVersion()`](#getversion)
  - [Interfaces & Types](#interfaces-types)
    - [`ScanOptions`](#scanoptions)
    - [`ScanFoundFolder`](#scanfoundfolder)
    - [`RiskAnalysis`](#riskanalysis)
    - [`GetSizeOptions`](#getsizeoptions)
    - [`GetSizeResult`](#getsizeresult)
    - [`GetNewestFileResult`](#getnewestfileresult)
    - [`DeleteOptions`](#deleteoptions)
  - [Usage Example](#usage-example)

---

## Interface: `Npkill`

The core of the system is the `NpkillInterface`. It offers methods to:

- Scan folders recursively.
- Get metadata about folders (size, last modified).
- Perform safe deletions.
- Stream logs and validate folders.

### `startScan$(rootPath, options?)`

Starts a recursive scan from a given root folder.

- **Parameters**:
  - `rootPath`: `string` — Folder to start scanning from.
  - `options`: [`ScanOptions`](#scanoptions) — Optional scan configuration.

- **Returns**: `Observable<ScanFoundFolder>`
- **Description**: Emits each matching folder as it's found.

---

### `stopScan()`

Stops any ongoing scan and releases resources.

---

### `getSize$(path, options?)`

Returns the total size of a directory.

- **Parameters**:
  - `path`: `string` — Path to folder.
  - `options`: [`GetSizeOptions`](#getsizeoptions)

- **Returns**: `Observable<GetSizeResult>`

---

### `getNewestFile$(path)`

Gets the most recently modified file inside a directory (recursively).

- **Parameters**:
  - `path`: `string`

- **Returns**: `Observable<GetNewestFileResult | null>`

---

### `delete$(path, options?)`

Deletes a folder, optionally as a dry-run. Only allowed if the folder is within the `target` of the initial scan.

- **Parameters**:
  - `path`: `string`
  - `options`: [`DeleteOptions`](#deleteoptions)

- **Returns**: `Observable<DeleteResult>`
- **Throws**: If the path is outside the original target.

---

### `getLogs$()`

Streams internal log entries.

- **Returns**: `Observable<LogEntry[]>`

---

### `isValidRootFolder(path)`

Validates whether a folder is suitable for scanning.

- **Parameters**:
  - `path`: `string`

- **Returns**: [`IsValidRootFolderResult`](#isvalidrootfolderresult)

---

### `getVersion()`

Returns the current version of npkill from `package.json`.

- **Returns**: `string`

---

## Interfaces & Types

---

### `ScanOptions`

```ts
interface ScanOptions {
  targets: string[];
  exclude?: string[];
  sortBy?: 'path' | 'size' | 'age';
  performRiskAnalysis?: boolean; // Default: true
}
```

---

### `ScanFoundFolder`

```ts
interface ScanFoundFolder {
  path: string;
  riskAnalysis?: RiskAnalysis;
}
```

---

### `RiskAnalysis`

Determines whether a result is safe to delete. That is, if it is likely to belong to some application and deleting it could break it.

```ts
interface RiskAnalysis {
  isSensitive: boolean;
  reason?: string;
}
```

---

### `GetSizeOptions`

```ts
interface GetSizeOptions {
  unit?: 'bytes'; // Default: 'bytes'
}
```

---

### `GetSizeResult`

```ts
interface GetSizeResult {
  size: number;
  unit: 'bytes';
}
```

---

### `GetNewestFileResult`

```ts
interface GetNewestFileResult {
  path: string;
  name: string;
  timestamp: number;
}
```

---

### `DeleteOptions`

```ts
interface DeleteOptions {
  dryRun?: boolean;
}
```

---

## Usage Example

This is a minimal example where:

1. it will start a search for `.nx` folders.
2. Get the most recent file
3. Get the total size of the directory

```ts
import { Npkill } from 'npkill';
import { mergeMap, filter, map } from 'rxjs';

const npkill = new Npkill();

let files: {
  path: string;
  size: number;
  newestFile: string;
}[] = [];

npkill
  .startScan$('/home/user/projects/', { target: '.nx' })
  .pipe(
    // Step 1: For each scan result, get the newest file
    mergeMap((scanResult) =>
      npkill.getNewestFile$(scanResult.path).pipe(
        // Step 2: If no newest file, skip this result
        filter((newestFile) => newestFile !== null),
        // Step 3: Combine scanResult and newestFile
        map((newestFile) => ({
          path: scanResult.path,
          newestFile: newestFile.path,
        })),
      ),
    ),
    // Step 4: For each result, get the folder size
    mergeMap((result) =>
      npkill.getSize$(result.path).pipe(
        map(({ size }) => ({
          ...result,
          size,
        })),
      ),
    ),
  )
  .subscribe({
    next: (result) => {
      files.push(result);
    },
    complete: () => {
      console.log('✅ Scan complete. Found folders:', files.length);
      console.table(files);
      console.log(JSON.stringify(files));
    },
  });
```

Output:

```bash
✅ Scan complete. Found folders: 3
┌─────────┬───────────────────────────────────────────┬──────────────────────────────────────────────────────────────────────────┬─────────┐
│ (index) │ path                                      │ newestFile                                                               │ size    │
├─────────┼───────────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────┼─────────┤
│ 0       │ '/home/user/projects/hello-world/.nx'     │ '/home/user/projects/hello-world/.nx/cache/18.3.4-nx.linux-x64-gnu.node' │ 9388032 │
│ 1       │ '/home/user/projects/another-project/.nx' │ '/home/user/projects/another-project/.nx/workspace-data/d/daemon.log'    │ 3182592 │
│ 2       │ '/home/user/projects/ARCHIVED/demo/.nx'   │ '/home/user/projects/ARCHIVED/demo/.nx/cache/d/daemon.log'               │ 2375680 │
└─────────┴───────────────────────────────────────────┴──────────────────────────────────────────────────────────────────────────┴─────────┘
[
  {
    "path": "/home/user/projects/hello-world/.nx",
    "newestFile": "/home/user/projects/hello-world/.nx/cache/18.3.4-nx.linux-x64-gnu.node",
    "size": 9388032
  },
  {
    "path": "/home/user/projects/another-project/.nx",
    "newestFile": "/home/user/projects/another-project/.nx/workspace-data/d/daemon.log",
    "size": 3182592
  },
  ........
]
```

```

### File: jest.config.ts
```ts
import type { JestConfigWithTsJest } from 'ts-jest';

const config: JestConfigWithTsJest = {
  preset: 'ts-jest/presets/default-esm',
  testEnvironment: 'node',
  extensionsToTreatAsEsm: ['.ts'],
  testRegex: '(/tests/.*|(\\.|/)(test|spec))\\.(jsx?|tsx?)$',
  moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx', 'json', 'node'],
  moduleNameMapper: {
    '^(\\.{1,2}/.*)\\.js$': '$1',
  },
  // moduleNameMapper: {
  //   '^@core/(.*)$': '<rootDir>/src/$1',
  //   '^@services/(.*)$': '<rootDir>/src/services/$1',
  //   '^@interfaces/(.*)$': '<rootDir>/src/interfaces/$1',
  //   '^@constants/(.*)$': '<rootDir>/src/constants/$1',
  // },
  // transform: {
  //   '^.+\\.(t|j)sx?$': ['ts-jest', { useESM: true }],
  // },
  transform: {
    '^.+\\.(t|j)sx?$': ['ts-jest', { useESM: true }],
  },
  testPathIgnorePatterns: ['<rootDir>/.stryker*'],
};

export default config;

```

### File: README.es.md
```md
<p align="center">
  <img src="https://npkill.js.org/img/npkill-text-outlined.svg" width="320" alt="npkill logo" />
  <img src="https://npkill.js.org/img/npkill-scope-mono.svg" width="50" alt="npkill logo scope" />
</p>
<p align="center">
<img alt="npm" src="https://img.shields.io/npm/dy/npkill.svg">
<a href="#donations"><img src="https://img.shields.io/badge/donate-<3-red" alt="Donations Badge"/></a>
<img alt="npm version" src="https://img.shields.io/npm/v/npkill.svg">
<img alt="NPM" src="https://img.shields.io/npm/l/npkill.svg">
</p>

### Encuentra y **destruye** directorios <font color="red">**node_modules**</font> viejos y pesados :sparkles:

<p align="center">
  <img src="/docs/npkill-demo-0.10.0.gif" alt="npkill demo GIF" />
</p>

Esta herramienta te permite listar cualquier directorio _node_modules_ que haya en tu sistema, además del espacio que ocupa. Entonces puedes seleccionar los que quieras borrar para liberar espacio. ¡Yay!

## i18n

Nos estamos esforzando por internacionalizar la documentación de Npkill. Aquí tienes una lista de las traducciones disponibles:

- [Español](./README.es.md)
- [Português](./README.pt.md)

## Table of Contents

- [Características](#features)
- [Instalación](#installation)
- [Uso](#usage)
  - [Opciones](#options)
  - [Ejemplos](#examples)
- [Configuración local](#setup-locally)
- [Roadmap](#roadmap)
- [Bugs conocidos](#known-bugs)
- [Cómo contribuir](#contributing)
- [Invítanos a un café](#donations)
- [Licencia](#license)

<a name="features"></a>

# :heavy_check_mark: Características

- **Libera espacio:** Elimina tus directorios _node_modules_ viejos y polvorientos que le roban espacio a tu máquina.

- **Último uso del Workspace**: Comprueba cuándo ha sido la última vez que has modificado un fichero en el workspace (indicado en la columna **last_mod**).

- **Rapidez:** NPKILL está escrito en TypeScript, pero las búsquedas se llevan a cabo a bajo nivel, lo que supone una mejora considerable del rendimiento.

- **Fácil de utilizar:** Despídete de comandos largos y difíciles. Utilizar Npkill es tan sencillo como leer la lista de tus node_modules, y pulsar la tecla Del para eliminarlos. ¿Podría ser más fácil? ;)

- **Minificado:** Apenas tiene dependencias.

<a name="installation"></a>

# :cloud: Instalación

¡Lo mejor es que no tienes que instalar Npkill para utilizarlo!
Simplemente utiliza el siguiente comando:

```bash
$ npx npkill
```

O, si por alguna razón te apetece instalarlo:

```bash
$ npm i -g npkill
# Los usuarios de Unix quizá tengan que ejecutar el comando con sudo. Ve con cuidado
```

> NPKILL no tiene soporte para node<v14. Si esto te afecta puedes utilizar `npkill@0.8.3`

<a name="usage"></a>

# :clipboard: Uso

```bash
$ npx npkill
# o solo npkill si está instalado de forma global
```

Por defecto, Npkill comenzará la búsqueda de node_modules comenzando en la ruta donde se ejecute el comando `npkill`.

Muévete por los distintos directorios listados con <kbd>↓</kbd> <kbd>↑</kbd>, y utiliza <kbd>Space</kbd> para borrar el directorio seleccionado.

También puedes usar <kbd>j</kbd> y <kbd>k</kbd> para moverte por los resultados.

Puedes abrir el directorio donde se aloja el resultado seleccionado pulsando <kbd>o</kbd>.

Para salir de Npkill, utiliza <kbd>Q</kbd>, o si te sientes valiente, <kbd>Ctrl</kbd> + <kbd>c</kbd>.

**¡Importante!** Algunas aplicaciones que están instaladas en el sistema necesitan su directorio node_modules para funcionar, y borrarlo puede romperlas. NPKILL te mostrará un :warning: para que sepas que tienes que tener cuidado.

<a name="options"></a>

## Opciones

| ARGUMENTO                        | DESCRIPCIÓN                                                                                                                                                    |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -c, --bg-color                   | Cambia el color de selección de la fila. _(Colores disponibles: **azul**, cyan, magenta, blanco, rojo y amarillo)_                                             |
| -d, --directory                  | Permite seleccionar el directorio desde el que comienza la búsqueda. Por defecto, se empieza en .                                                              |
| -D, --delete-all                 | Borra automáticamente todos los node_modules que se encuentren. Recomendable utilizar junto a `-x`                                                             |
| -e, --hide-errors                | Esconde los errores en el caso de que ocurra alguno                                                                                                            |
| -E, --exclude                    | Excluye directorios de la búsqueda (la lista de directorios debe estar entre comillas dobles "", cada directorio separado por ',' Ejemplo: "ignore1, ignore2") |
| -f, --full                       | Comienza la búsqueda en el home del usuario (ejemplo: "/home/user" en Linux)                                                                                   |
| -gb                              | Muestra el tamaño en Gigabytes en lugar de en Megabytes.                                                                                                       |
| -h, --help, ?                    | Muestra esta página de ayuda y finaliza                                                                                                                        |
| -nu, --no-check-update           | No comprobar si hay actualizaciones al iniciar la aplicación                                                                                                   |
| -s, --sort                       | Ordena los resultados por: `size`, `path` or `last-mod`                                                                                                        |
| -t, --target                     | Especifica el nombre del directorio que se buscará (por defecto es node_modules)                                                                               |
| -x, --exclude-hidden-directories | Excluye directorios ocultos (directorios "dot") de la búsqueda                                                                                                 |
| --dry-run                        | No borra nada (simula un tiempo de borrado aleatorio)                                                                                                          |
| -v, --version                    | Muestra la versión de Npkill                                                                                                                                   |

**Precaución:** _Algunos comandos pueden cambiar en versiones futuras_

<a name="examples"></a>

## Ejemplo

- Busca y encuentra los directorios **node_modules** en un directorio _projects_ :

```bash
npkill -d ~/projects

# otra alternativa:
cd ~/projects
npkill
```

- Lista los directorios llamados "dist" y muestra los errores que ocurran:

```bash
npkill --target dist -e
```

- Muestra el cursor de color magenta... ¡Porque me gusta el magenta!

```bash
npkill --bg-color magenta
```

- Lista los directorios **vendor** en un directorio _projects_, ordenados por tamaño y mostrando el tamaño en gb:

```bash
npkill -d '~/more projects' -gb --sort size --target vendor
```

- Lista los **node_modules** en el directorio _projects_, excluyendo los que están en los directorios _progress_ e _ignore-this_:

```bash
npkill -d 'projects' --exclude "progress, ignore-this"
```

- Borra automáticamente todos los **node_modules** que se encuentren en el directorio _backups_:

```bash
npkill -d ~/backups/ --delete-all
```

<a name="setup-locally"></a>

# :pager: Configuración local

```bash
# -- Primero, clona el repositorio
git clone https://github.com/voidcosmos/npkill.git

# -- Navega al dir
cd npkill

# -- Instala las dependencias
npm install

# -- ¡Y ejecuta!
npm run start


# -- Si quieres ejecutar con algún parámetro, hay que añadir "--", tal y como se muestra a continuación:
npm run start -- -f -e
```

<a name="roadmap"></a>

# :crystal_ball: Roadmap

- [x] Lanzar la versión 0.1.0 !
- [x] Mejorar el código
  - [x] Mejorar el rendimiento
  - [ ] ¡Mejorar el rendimiento aún más!
- [x] Ordenar los resultados por tamaño y ruta
- [x] Permitir la búsqueda de otro tipo de directorios (targets)
- [ ] Reducir las dependencies para ser un módulo más minimalista
- [ ] Permitir el filtrado por directorios que no se hayan utilizado en un periodo de tiempo determinado
- [ ] Crear una opción para mostrar los directorios en formato árbol
- [x] Añadir menús
- [x] Añadir un servicio de logs
- [ ] Limpieza periódica y automática (?)

<a name="known-bugs"></a>

# :bug: Bugs conocidos :bug:

- A veces, el CLI se bloquea mientras un directorio se está borrando.
- La ordenación, especialmente por rutas, puede ralentizar la terminal cuando haya muchos resultados al mismo tiempo.
- A veces, los cálculos de tamaño son mayores de lo que deberían ser.
- (RESUELTO) Problemas de rendimiento al hacer la búsqueda desde directorios de alto nivel (como / en Linux).
- (RESUELTO) A veces el texto se colapsa al actualizar el CLI.
- (RESUELTO) Analizar el tamaño de los directorios tarda más de lo que debería.

> Si encuentras algún bug, no dudes en abrir un issue :)

<a name="contributing"></a>

# :revolving_hearts: Cómo contribuir

Si quieres contribuir, échale un vistazo al [CONTRIBUTING.md](.github/CONTRIBUTING.es.md)

<a name="donations"></a>

# :coffee: Invítanos a un café

<img align="right" width="300" src="https://npkill.js.org/img/cat-donation-cup.png">
Hemos desarrollado Npkill en nuestro tiempo libre, porque nos apasiona la programación.

El día de mañana nos gustaría dedicarnos al open source completamente, pero antes, nos queda un largo camino por recorrer.

Seguiremos contribuyendo al open source por y para siempre, pero las donaciones son una de las muchas formas de apoyarnos.

¡Invítanos a un café! (O a un té para Nya, la única programadora a la que no le gusta el café).

<span class="badge-opencollective"><a href="https://opencollective.com/npkill/contribute" title="Dona a este proyecto utilizando Open Collective"><img src="https://img.shields.io/badge/open%20collective-donate-green.svg" alt="Botón de donar con Open Collective" /></a></span>

### ¡¡Mil gracias!!

## Muchísimas gracias a todos los que nos han apoyado :heart:

<a href="https://opencollective.com/npkill#backers" target="_blank"><img width="535" src="https://opencollective.com/npkill/tiers/backer.svg?width=535"></a>

---

### Alternativa cripto

- btc: 1ML2DihUoFTqhoQnrWy4WLxKbVYkUXpMAX
- bch: 1HVpaicQL5jWKkbChgPf6cvkH8nyktVnVk
- eth: 0x7668e86c8bdb52034606db5aa0d2d4d73a0d4259

<a name="license"></a>

# :scroll: Licencia

MIT © [Nya García Gallardo](https://github.com/NyaGarcia) y [Juan Torres Gómez](https://github.com/zaldih)

:cat::baby_chick:

---

```

### File: README.id.md
```md
<p align="center">
  <img src="https://npkill.js.org/img/npkill-text-outlined.svg" width="320" alt="npkill logo" />
  <img src="https://npkill.js.org/img/npkill-scope-mono.svg" width="50" alt="npkill logo scope" />
</p>
<p align="center">
<img alt="npm" src="https://img.shields.io/npm/dy/npkill.svg">
<a href="#donations"><img src="https://img.shields.io/badge/donate-<3-red" alt="Donations Badge"/></a>
<img alt="npm version" src="https://img.shields.io/npm/v/npkill.svg">
<img alt="NPM" src="https://img.shields.io/npm/l/npkill.svg">
</p>

### Mudah menemukan dan **menghapus** folder <font color="red">**node_modules**</font> yang lama dan berat :sparkles:

<p align="center">
  <img src="/docs/npkill-demo-0.10.0.gif" alt="npkill demo GIF" />
</p>

Alat ini memungkinkan Anda untuk mencantumkan semua direktori _node_modules_ di sistem Anda, serta ruang yang mereka gunakan. Anda kemudian dapat memilih mana yang ingin Anda hapus untuk mengosongkan ruang penyimpanan. Yay!

## i18n

Kami berusaha untuk menerjemahkan dokumen Npkill ke berbagai bahasa. Berikut daftar terjemahan yang tersedia:

- [Español](./README.es.md)
- [Indonesian](./README.id.md)
- [Portugis](./README.pt.md)
- [Turki](./README.tr.md)

## Daftar Isi

- [Fitur](#features)
- [Instalasi](#installation)
- [Penggunaan](#usage)
  - [Opsi](#options)
  - [Contoh](#examples)
- [Pengaturan Lokal](#setup-locally)
- [Peta Jalan](#roadmap)
- [Bug yang Diketahui](#known-bugs)
- [Kontribusi](#contributing)
- [Buy us a coffee](#donations)
- [Lisensi](#license)

<a name="features"></a>

# :heavy_check_mark: Fitur

- **Bersihkan Ruang:** Hapus _node_modules_ lama yang tidak digunakan yang memenuhi mesin Anda.

- **Penggunaan Terakhir Workspace:** Cek kapan terakhir kali Anda mengubah file di workspace (ditunjukkan di kolom **last_mod**).

- **Sangat Cepat:** NPKILL ditulis dalam TypeScript, tetapi pencarian dilakukan di tingkat rendah, sehingga performanya sangat baik.

- **Mudah Digunakan:** Tidak perlu perintah panjang. Menggunakan npkill semudah membaca daftar _node_modules_ Anda, dan menekan tombol Del untuk menghapusnya. Bisa lebih mudah dari itu?

- **Ringkas:** Hampir tidak memiliki dependensi.

<a name="installation"></a>

# :cloud: Instalasi

Anda tidak perlu menginstal untuk menggunakannya! Cukup gunakan perintah berikut:

```bash
$ npx npkill
```

Atau jika Anda benar-benar ingin menginstalnya:

```bash
$ npm i -g npkill
# Pengguna Unix mungkin perlu menjalankan perintah dengan sudo. Gunakan dengan hati-hati
```

> NPKILL tidak mendukung node<v14. Jika ini memengaruhi Anda, gunakan `npkill@0.8.3`

<a name="usage"></a>

# :clipboard: Penggunaan

```bash
$ npx npkill
# atau cukup npkill jika telah diinstal secara global
```

Secara default, npkill akan memindai _node_modules_ mulai dari jalur tempat perintah `npkill` dijalankan.

Pindah di antara folder yang terdaftar menggunakan <kbd>↓</kbd> <kbd>↑</kbd>, dan gunakan <kbd>Space</kbd> atau <kbd>Del</kbd> untuk menghapus folder yang dipilih. Anda juga dapat menggunakan <kbd>j</kbd> dan <kbd>k</kbd> untuk bergerak di antara hasil.

Anda dapat membuka direktori tempat hasil yang dipilih berada dengan menekan <kbd>o</kbd>.

Untuk keluar, tekan <kbd>Q</kbd> atau <kbd>Ctrl</kbd> + <kbd>c</kbd> jika Anda pemberani.

**Penting!** Beberapa aplikasi yang diinstal di sistem membutuhkan direktori _node_modules_ untuk berfungsi, dan menghapusnya dapat menyebabkan kerusakan. NPKILL akan menandainya dengan :warning: agar berhati-hati.

<a name="options"></a>

## Opsi

| ARGUMEN                          | DESKRIPSI                                                                                                     |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| -c, --bg-color                   | Ubah warna sorotan baris. _(Tersedia: **blue**, cyan, magenta, white, red, dan yellow)_                       |
| -d, --directory                  | Tetapkan direktori awal pencarian. Secara default, mulai dari .                                               |
| -D, --delete-all                 | Secara otomatis hapus semua folder _node_modules_ yang ditemukan. Disarankan digunakan bersama `-x`.          |
| -e, --hide-errors                | Sembunyikan kesalahan (jika ada)                                                                              |
| -E, --exclude                    | Kecualikan direktori dari pencarian. Daftar direktori harus dalam tanda kutip ganda "", dipisahkan dengan ',' |
| -f, --full                       | Mulai pencarian dari direktori home pengguna (contoh: "/home/user" di Linux)                                  |
| -gb                              | Tampilkan folder dalam Gigabyte daripada Megabyte.                                                            |
| -h, --help, ?                    | Tampilkan halaman bantuan ini dan keluar                                                                      |
| -nu, --no-check-update           | Jangan memeriksa pembaruan saat startup                                                                       |
| -s, --sort                       | Urutkan hasil berdasarkan: `size`, `path`, atau `last-mod`                                                    |
| -t, --target                     | Tentukan nama direktori yang ingin Anda cari (default: node_modules)                                          |
| -x, --exclude-hidden-directories | Kecualikan direktori tersembunyi dari pencarian.                                                              |
| --dry-run                        | Tidak menghapus apa pun (hanya simulasi dengan delay acak).                                                   |
| -v, --version                    | Tampilkan versi npkill                                                                                        |

**Peringatan:** _Di versi mendatang, beberapa perintah mungkin berubah._

<a name="examples"></a>

## Contoh

- Cari direktori **node_modules** di direktori _projects_ Anda:

```bash
npkill -d ~/projects

# alternatif lain:
cd ~/projects
npkill
```

- Daftar direktori bernama "dist" dan tampilkan kesalahan jika ada:

```bash
npkill --target dist -e
```

- Tampilkan kursor warna magenta... karena saya suka magenta!

```bash
npkill --color magenta
```

- Daftar direktori **vendor** di _projects_, urutkan berdasarkan ukuran, dan tampilkan ukuran dalam GB:

```bash
npkill -d '~/more projects' -gb --sort size --target vendor
```

- Secara otomatis hapus semua _node_modules_ di folder cadangan Anda:

```bash
npkill -d ~/backups/ --delete-all
```

<a name="setup-locally"></a>

# :pager: Pengaturan Lokal

```bash
# -- Pertama, kloning repositori
git clone https://github.com/voidcosmos/npkill.git

# -- Masuk ke direktori
cd npkill

# -- Instal dependensi
npm install

# -- Dan jalankan!
npm run start

# -- Jika ingin menjalankannya dengan parameter, tambahkan "--" seperti contoh berikut:
npm run start -- -f -e
```

<a name="roadmap"></a>

# :crystal_ball: Peta Jalan

- [x] Rilis versi 0.1.0!
- [x] Tingkatkan kode
  - [x] Tingkatkan performa
  - [ ] Tingkatkan performa lebih lanjut!
- [x] Urutkan hasil berdasarkan ukuran dan jalur
- [x] Izinkan pencarian untuk jenis direktori (target) lainnya
- [ ] Kurangi dependensi agar minimalis
- [ ] Filter berdasarkan waktu terakhir penggunaan
- [ ] Tampilkan direktori dalam format tree
- [x] Tambahkan beberapa menu
- [x] Tambahkan log
- [ ] Pembersihan otomatis berkala (?)

<a name="known-bugs"></a>

# :bug: Bug yang Diketahui :bug:

- CLI terkadang berhenti saat menghapus folder.
- Beberapa terminal tanpa TTY (seperti Git Bash di Windows) tidak bekerja.
- Mengurutkan berdasarkan jalur dapat memperlambat terminal dengan banyak hasil.
- Perhitungan ukuran kadang lebih besar dari seharusnya.
- (TERPECAHKAN) Masalah performa pada direktori tingkat tinggi (seperti / di Linux).
- (TERPECAHKAN) Teks terkadang kacau saat CLI diperbarui.
- (TERPECAHKAN) Analisis ukuran direktori memakan waktu lebih lama dari seharusnya.

> Jika menemukan bug, jangan ragu untuk membuka issue. :)

<a name="contributing"></a>

# :revolving_hearts: Kontribusi

Jika ingin berkontribusi, cek [CONTRIBUTING.md](.github/CONTRIBUTING.md).

<a name="donations"></a>

# :coffee: Buy us a coffee

<img align="right" width="300" src="https://npkill.js.org/img/cat-donation-cup.png">
Kami mengembangkan npkill di waktu luang karena kami mencintai pemrograman.

Kami akan terus mengerjakan ini, tetapi donasi adalah salah satu cara mendukung apa yang kami lakukan.

<span class="badge-opencollective"><a href="https://opencollective.com/npkill/contribute" title="Donate to this project using Open Collective"><img src="https://img.shields.io/badge/open%20collective-donate-green.svg" alt="Open Collective donate button" /></a></span>

### Terima Kasih!!

## Terima kasih banyak kepada pendukung kami :heart:

<a href="https://opencollective.com/npkill#backers" target="_blank"><img width="535" src="https://opencollective.com/npkill/tiers/backer.svg?width=535"></a>

---

### Alternatif Crypto

- btc: 1ML2DihUoFTqhoQnrWy4WLxKbVYkUXpMAX
- bch: 1HVpaicQL5jWKkbChgPf6cvkH8nyktVnVk
- eth: 0x7668e86c8bdb52034606db5aa0d2d4d73a0d4259

<a name="license"></a>

# :scroll: Lisensi

MIT © [Nya García Gallardo](https://github.com/NyaGarcia) dan [Juan Torres Gómez](https://github.com/zaldih)

:cat::baby_chick:

---

```

### File: README.pt.md
```md
<p align="center">
  <img src="https://npkill.js.org/img/npkill-text-outlined.svg" width="320" alt="npkill logo" />
  <img src="https://npkill.js.org/img/npkill-scope-mono.svg" width="50" alt="npkill logo scope" />
</p>
<p align="center">
<img alt="npm" src="https://img.shields.io/npm/dy/npkill.svg">
<a href="#donations"><img src="https://img.shields.io/badge/donate-<3-red" alt="Donations Badge"/></a>
<img alt="npm version" src="https://img.shields.io/npm/v/npkill.svg">
<img alt="NPM" src="https://img.shields.io/npm/l/npkill.svg">
</p>

### Encontre e **remova** facilemente pastas <font color="red">**node_modules**</font> antigas e pesadas :sparkles:

<p align="center">
  <img src="/docs/npkill-demo-0.10.0.gif" alt="npkill demo GIF" />
</p>

Esta ferramenta permite que você liste as pastas _node_modules_ em seu sistema, bem como o espaço que ocupam. Então você pode selecionar quais deles deseja apagar para liberar espaço. ¡Yay!

## i18n

Estamos fazendo esforço para internacionalizar a documentação do Npkill. Aqui está uma lista das traduções disponíveis:

- [Español](./README.es.md)
- [Português](./README.pt.md)

## Table of Contents

- [Funcionalidades](#features)
- [Instalação](#installation)
- [Utilização](#usage)
  - [Opções](#options)
  - [Exemplos](#examples)
- [Configurar localmente](#setup-locally)
- [Roteiro](#roadmap)
- [Problemas conhecidos](#known-bugs)
- [Contribuindo](#contributing)
- [Compre-nos um café](#donations)
- [Licença](#license)

<a name="features"></a>

# :heavy_check_mark: Funcionalidades

- **Liberar espaço:** Livre-se dos antigos e empoeirados node_modules que ocupam espaço em sua máquina.

- **Último Uso do Espaço de Trabalho**: Verifique quando foi a última vez que você modificou um arquivo no espaço de trabalho (indicado na coluna **última_modificação**).

- **Muito rápido:** O NPKILL é escrito em TypeScript, mas as pesquisas são realizadas em um nível baixo, melhorando muito o desempenho.

- **Fácil de usar:** Diga adeus aos comandos longos. Usar o npkill é tão simples quanto ler uma lista de seus node_modules e pressionar Delete para se livrar deles. Pode ser mais fácil do que isso? ;)

- **Minificado:** Ele mal possui dependências.

<a name="installation"></a>

# :cloud: Instalação

Você nem precisa instalá-lo para usar!
Basta usar o seguinte comando:

```bash
$ npx npkill
```

Ou, se por algum motivo você realmente deseja instalá-lo:

```bash
$ npm i -g npkill
# Usuários do Unix podem precisar executar o comando com sudo. Tome cuidado.
```

> O NPKILL não suporta versões node<v14. Se isso afeta você, use npkill@0.8.3.

<a name="usage"></a>

# :clipboard: Utilização

```bash
$ npx npkill
# ou apenas npkill se você instalou globalmente
```

Por padrão, o npkill fará a varredura em busca de node_modules a partir do local onde o comando npkill é executado.

Para mover entre as pastas listadas, utilize as teclas <kbd>↓</kbd> e <kbd>↑</kbd>, e use <kbd>Space</kbd> ou <kbd>Del</kbd> para excluir a pasta selecionada.
Você também pode usar <kbd>j</kbd> e <kbd>k</kbd> para se mover entre os resultados.

Para abrir o diretório onde o resultado selecionado está localizado, pressione <kbd>o</kbd>.

Para sair, use <kbd>Q</kbd> ou <kbd>Ctrl</kbd> + <kbd>c</kbd> se você estiver se sentindo corajoso.

**Importante!** Algumas aplicações instaladas no sistema precisam do diretório node_modules delas para funcionar, e excluí-los pode quebrá-las. O NPKILL irá destacá-los exibindo um :warning: para que você tenha cuidado.

<a name="options"></a>

## Opções

| Comando                          | Descrição                                                                                                                                                           |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -c, --bg-color                   | Troca a cor de destaque da linha. _(Disponível: **blue**, cyan, magenta, white, red e yellow)_                                                                      |
| -d, --directory                  | Defina o diretório a partir do qual iniciar a pesquisa. Por padrão, o ponto de partida é a raiz is .                                                                |
| -D, --delete-all                 | Exclui automaticamente todos os node_modules encontrados. Recomendado para usar junto com `-x`                                                                      |
| -e, --hide-errors                | Oculta erros                                                                                                                                                        |
| -E, --exclude                    | Excluir diretórios da pesquisa (a lista de diretórios deve estar entre aspas duplas "", com cada diretório separado por vírgula ','). Exemplo: "ignorar1, ignorar2" |
| -f, --full                       | Iniciar a pesquisa a partir do diretório pessoal do usuário (exemplo: "/home/user" no Linux)                                                                        |
| -gb                              | Mostra as pastas em Gigabytes ao invés de Megabytes.                                                                                                                |
| -h, --help, ?                    | Mostrar a página de ajuda e sair                                                                                                                                    |
| -nu, --no-check-update           | Não verificar atualizações na inicialização                                                                                                                         |
| -s, --sort                       | Ordenar resultados por: `size` (tamanho), `path`(localização) ou `last-mod`(última modificação)                                                                     |
| -t, --target                     | Especifique o nome dos diretórios que deseja pesquisar (por padrão, é node_modules)                                                                                 |
| -x, --exclude-hidden-directories | Excluir diretórios ocultos ("diretórios com ponto") da pesquisa.                                                                                                    |
| --dry-run                        | Não exclui nada (irá simular com um atraso aleatório).                                                                                                              |
| -v, --version                    | Mostrar versão do npkill                                                                                                                                            |

**Aviso:** _No futuro alguns comandos podem mudar_

<a name="examples"></a>

## Examples

- Busque pastas **node_modules** no seu diretório de projetos:

```bash
npkill -d ~/projetos

# alternativa:
cd ~/projetos
npkill
```

- Listar diretórios com o nome "dist" e mostrar erros, se houver algum:

```bash
npkill --target dist -e
```

- Exibe o cursor na cor magenta... porque eu gosto de magenta!

```bash
npkill --bg-color magenta
```

- Listar pastas **vendor** no seu diretório de _projetos_, ordenar por tamanho e mostrar o tamanho em GB:

```bash
npkill -d '~/more projetos' -gb --sort size --target vendor
```

- Listar **node_modules** no seu diretório de _projetos_, exceto nas pastas _progresso_ e _ignorar_:

```bash
npkill -d 'projetos' --exclude "progresso, ignorar"
```

- Exclua automaticamente todos os node_modules que tenham entrado em seus backups:

```bash
npkill -d ~/backups/ --delete-all
```

<a name="setup-locally"></a>

# :pager: Configurar localmente

```bash
# -- Primeiramente, clone o repositório
git clone https://github.com/voidcosmos/npkill.git

# -- Acesse a pasta
cd npkill

# -- Instale as dependências
npm install

# -- E rode!
npm run start


# -- Se você deseja executá-lo com algum parâmetro, você terá que adicionar "--" como no seguinte exemplo:
npm run start -- -f -e
```

<a name="roadmap"></a>

# :crystal_ball: Roteiro

- [x] Lançamento 0.1.0 !
- [x] Melhorias de código
  - [x] Melhorias de performance
  - [ ] Ainda mais melhorias de performance!
- [x] Ordenação de resultados por tamanho e localização
- [x] Permitir a pesquisa por outros tipos de diretórios (alvo)
- [ ] Reduzir as dependências para tornar o módulo mais minimalista
- [ ] Permitir filtrar por diretórios que não foram usados em um período de tempo
- [ ] Criar opção para mostrar as pastas em formato de árvore
- [x] Adicionar menus
- [x] Adicionar logs
- [ ] Limpeza automatizada periódica (?)

<a name="known-bugs"></a>

# :bug: Problemas conhecidos :bug:

- Às vezes, a CLI fica bloqueada enquanto a pasta está sendo excluída.
- Alguns terminais que não utilizam TTY (como o git bash no Windows) não funcionam.
- A ordenação, especialmente por rotas, pode deixar o terminal mais lento quando há muitos resultados ao mesmo tempo.
- Às vezes, os cálculos de tamanho são maiores do que deveriam ser.
- (RESOLVIDO) Problemas de desempenho ao pesquisar em diretórios de alto nível (como / no Linux).
- (RESOLVIDO) Às vezes, o texto se desfaz ao atualizar a interface de linha de comando (CLI).
- (RESOLVIDO) A análise do tamanho dos diretórios leva mais tempo do que deveria.

> Se você encontrar algum erro, não hesite em abrir uma solicitação (via issue) :)

<a name="contributing"></a>

# :revolving_hearts: Contribuindo

Se você quer contribuir confira o [CONTRIBUTING.md](.github/CONTRIBUTING.md)

<a name="donations"></a>

# :coffee: Compre-nos um café

<img align="right" width="300" src="https://npkill.js.org/img/cat-donation-cup.png">
Desenvolvemos o npkill em nosso tempo livre, porque somos apaixonados pelo setor de programação. Amanhã, gostaríamos de nos dedicar mais a isso, mas antes, temos um longo caminho a percorrer.

Continuaremos a fazer as coisas de qualquer maneira, mas as doações são uma das muitas formas de apoiar o que fazemos.

<span class="badge-opencollective"><a href="https://opencollective.com/npkill/contribute" title="Faça uma doação para este projeto usando o Open Collective"><img src="https://img.shields.io/badge/open%20collective-donate-green.svg" alt="Open Collective donate button" /></a></span>

### Obrigado!!

## Um enorme agradecimento aos nossos apoiadores :heart:

<a href="https://opencollective.com/npkill#backers" target="_blank"><img width="535" src="https://opencollective.com/npkill/tiers/backer.svg?width=535"></a>

---

### via Crypto

- btc: 1ML2DihUoFTqhoQnrWy4WLxKbVYkUXpMAX
- bch: 1HVpaicQL5jWKkbChgPf6cvkH8nyktVnVk
- eth: 0x7668e86c8bdb52034606db5aa0d2d4d73a0d4259

<a name="license"></a>

# :scroll: Licença

MIT © [Nya García Gallardo](https://github.com/NyaGarcia) e [Juan Torres Gómez](https://github.com/zaldih)

:cat::baby_chick:

---

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

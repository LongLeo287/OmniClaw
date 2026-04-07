---
id: ak-endfield-api-archive
type: knowledge
owner: OA_Triage
---
# ak-endfield-api-archive
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "ak-endfield-api-archive",
  "version": "0.1.0",
  "description": "Arknights Endfield game API response archive",
  "author": "daydreamer-json <atarakima1@icloud.com> (https://github.com/daydreamer-json)",
  "license": "AGPL-3.0-or-later",
  "module": "src/main.ts",
  "type": "module",
  "private": true,
  "repository": {
    "type": "git",
    "url": "git+https://github.com/daydreamer-json/ak-endfield-api-archive.git"
  },
  "scripts": {
    "start": "bun src/main.ts archive && bun x oxfmt output"
  },
  "dependencies": {
    "@octokit/rest": "^22.0.1",
    "chalk": "^5.6.2",
    "cli-table3": "^0.6.5",
    "cookie": "^1.1.1",
    "deepmerge": "^4.3.1",
    "ky": "^1.14.2",
    "log4js": "^6.9.1",
    "luxon": "^3.7.2",
    "ora": "^9.1.0",
    "p-queue": "^9.1.0",
    "prompts": "^2.4.2",
    "qs": "^6.14.1",
    "semver": "^7.7.3",
    "uuid": "^13.0.0",
    "yaml": "^2.8.2",
    "yargs": "^18.0.0"
  },
  "devDependencies": {
    "@biomejs/biome": "^2.3.11",
    "@tsconfig/bun": "^1.0.10",
    "@tsconfig/node24": "^24.0.4",
    "@tsconfig/recommended": "^1.0.13",
    "@tsconfig/strictest": "^2.0.8",
    "@types/bun": "latest",
    "@types/luxon": "^3.7.1",
    "@types/node": "^25.0.9",
    "@types/prompts": "^2.4.9",
    "@types/qs": "^6.14.0",
    "@types/semver": "^7.7.1",
    "@types/yargs": "^17.0.35",
    "nodemon": "^3.1.11",
    "oxfmt": "^0.26.0"
  },
  "peerDependencies": {
    "typescript": "^5"
  }
}

```

### File: README.md
```md
<h1 align="center">ak-endfield-api-archive</h1>

<p align="center">
  <a href="https://github.com/palmcivet/awesome-arknights-endfield"><img src="https://raw.githubusercontent.com/palmcivet/awesome-arknights-endfield/refs/heads/main/assets/badge-for-the-badge.svg" alt="Awesome Arknights Endfield" /></a>
</p>
<p align="center">
  <a href="https://github.com/daydreamer-json/ak-endfield-api-archive/actions/workflows/main.yml"><img src="https://github.com/daydreamer-json/ak-endfield-api-archive/actions/workflows/main.yml/badge.svg" alt="GitHub Actions" /></a>
  <img src="https://api.cron-job.org/jobs/7183534/5f3f37a732a92096/status-0.svg" alt="Cron Job" />
</p>

This repository monitors and records changes to various Arknights: Endfield API responses.

Updates are checked approximately every 5 minutes and automatically pushed via GitHub Actions.  
API outputs are stored in the [`output`](/output/) directory.

## [Download Library](https://ak-endfield-api-archive.daydreamer-json.cc/)

For a historical overview of game packages and other resources, please click the link above.

## Contents of the Archive

The following APIs are currently being monitored:
- Launcher
  - Get latest game (Global, China)
  - Get latest game resources (Global, China)
  - Get latest launcher (Global, China)
  - Get launcher web resources (Global, China)
    - Announcements
    - Banners
    - Main background images
    - Single Ent.
    - Sidebar
- Raw
  - Game resource manifests (index, patch)
  - Launcher image resources

Most raw data is provided "as-is" without modification. Some files (e.g., `index_*.json`) have been decrypted for readability.

The following data is archived in an external repository:
- Game packages (.zip)
- Game patch packages (.zip)
- Game hotfix resources
  - To avoid the overhead of managing numerous small files, these are bundled into larger chunk files.
- Launcher packages (.exe, .zip)

For a full list of externally archived files, please refer to the mirror list JSON in the `output` directory. (Note: `*_pending` files are temporary files used during the archiving process.)

For users in Asia (including China, Japan, Korea): To speed up downloads, use any GitHub proxy service (such as [`gh-proxy.org`](https://gh-proxy.org/), which is cached by Cloudflare).

## Contributing

As I can only test the game on the platforms and operating systems available to me, some data may contain inaccuracies. If you have information—particularly regarding **Chinese regional data** or beta versions—or if you would like to improve the code, please feel free to submit an issue or a pull request.

## Thanks

- [Vivi029](https://github.com/Vivi029): Added Windows Google Play Games channel support.

## Disclaimer

This project is not affiliated with Hypergryph (GRYPHLINE) and was created solely for **private use, educational, and research purposes.**

The author assumes no responsibility for any consequences arising from the use of this project. **USE AT YOUR OWN RISK.**

```

### File: .oxfmtrc.json
```json
{
  "$schema": "./node_modules/oxfmt/configuration_schema.json",
  "ignorePatterns": [
    "output/raw/**/index_main.json",
    "output/raw/**/index_initial.json"
  ],
  "useTabs": false,
  "printWidth": 120,
  "tabWidth": 2,
  "endOfLine": "lf",
  "arrowParens": "always",
  "bracketSameLine": false,
  "bracketSpacing": true,
  "htmlWhitespaceSensitivity": "css",
  "insertFinalNewline": true,
  "jsxSingleQuote": true,
  "objectWrap": "preserve",
  "proseWrap": "preserve",
  "quoteProps": "as-needed",
  "semi": true,
  "singleQuote": true,
  "trailingComma": "all"
}

```

### File: biome.json
```json
{
  "$schema": "https://biomejs.dev/schemas/2.2.4/schema.json",
  "vcs": { "enabled": true, "clientKind": "git", "useIgnoreFile": true },
  "files": { "ignoreUnknown": false, "includes": ["**"] },
  "formatter": {
    "enabled": true,
    "useEditorconfig": true,
    "formatWithErrors": false,
    "indentStyle": "space",
    "indentWidth": 2,
    "lineEnding": "lf",
    "lineWidth": 120,
    "attributePosition": "auto",
    "bracketSpacing": true
  },
  "linter": { "enabled": false, "rules": { "recommended": true } },
  "javascript": {
    "formatter": {
      "jsxQuoteStyle": "single",
      "quoteProperties": "asNeeded",
      "trailingCommas": "all",
      "semicolons": "always",
      "arrowParentheses": "always",
      "bracketSameLine": false,
      "quoteStyle": "single",
      "attributePosition": "auto",
      "bracketSpacing": true
    }
  },
  "assist": {
    "enabled": true,
    "actions": {
      "source": {
        "organizeImports": "on"
      }
    }
  }
}

```

### File: src_DISTILLED.md
```md
---
id: src
type: distilled_knowledge
---
# src

## SWALLOW ENGINE DISTILLATION

### File: cmd.ts
```ts
import path from 'node:path';
import yargs from 'yargs';
import { hideBin } from 'yargs/helpers';
import cmds from './cmds.js';
import * as TypesLogLevels from './types/LogLevels.js';
import argvUtils from './utils/argv.js';
import appConfig from './utils/config.js';
import configEmbed from './utils/configEmbed.js';
import exitUtils from './utils/exit.js';
import logger from './utils/logger.js';

if (configEmbed.VERSION_NUMBER === null) throw new Error('Embed VERSION_NUMBER is null');

function wrapHandler(handler: (argv: any) => Promise<void>) {
  return async (argv: any) => {
    try {
      await handler(argv);
      await exitUtils.exit(0);
    } catch (error) {
      logger.error('Error caught:', error);
      await exitUtils.exit(1);
    }
  };
}

async function parseCommand() {
  const yargsInstance = yargs(hideBin(process.argv));
  await yargsInstance
    .command(
      ['archive'],
      'Archive all APIs',
      (yargs) => {
        yargs.options({
          'output-dir': {
            alias: ['o'],
            desc: 'Output root directory',
            default: path.resolve('output'),
            normalize: true,
            type: 'string',
          },
        });
      },
      wrapHandler(cmds.archive),
    )
    .command(
      ['ghMirrorUpload'],
      'Upload pending large binary file to GitHub mirror',
      (yargs) => {
        yargs.options({
          'output-dir': {
            alias: ['o'],
            desc: 'Output root directory',
            default: path.resolve('output'),
            normalize: true,
            type: 'string',
          },
        });
      },
      wrapHandler(cmds.ghMirrorUpload),
    )
    .command(
      ['authTest [token] [email] [password]'],
      'Auth and gacha fetch test command',
      (yargs) => {
        yargs
          .positional('token', {
            describe: 'Gryphline account service token',
            type: 'string',
          })
          .positional('email', {
            describe: 'Gryphline account email address',
            type: 'string',
          })
          .positional('password', {
            describe: 'Gryphline account password',
            type: 'string',
          })
          .options({});
      },
      wrapHandler(cmds.authTest),
    )
    .options({
      'log-level': {
        desc: 'Set log level (' + TypesLogLevels.LOG_LEVELS_NUM.join(', ') + ')',
        default: appConfig.logger.logLevel,
        type: 'number',
        coerce: (arg: number): TypesLogLevels.LogLevelString => {
          if (arg < TypesLogLevels.LOG_LEVELS_NUM[0] || arg > TypesLogLevels.LOG_LEVELS_NUM.slice(-1)[0]!) {
            throw new Error(`Invalid log level: ${arg} (Expected: ${TypesLogLevels.LOG_LEVELS_NUM.join(', ')})`);
          } else {
            return TypesLogLevels.LOG_LEVELS[arg as TypesLogLevels.LogLevelNumber];
          }
        },
      },
    })
    .middleware(async (argv) => {
      argvUtils.setArgv(argv);
      logger.level = argvUtils.getArgv()['logLevel'];
      logger.trace('Process started: ' + `${configEmbed.APPLICATION_NAME} v${configEmbed.VERSION_NUMBER}`);
    })
    .scriptName(configEmbed.APPLICATION_NAME)
    .version(String(configEmbed.VERSION_NUMBER))
    .usage('$0 <command> [argument] [option]')
    .help()
    .alias('help', 'h')
    .alias('help', '?')
    .alias('version', 'V')
    .demandCommand(1)
    .strict()
    .recommendCommands()
    .parse();
}

export default parseCommand;

```

### File: cmds.ts
```ts
import archive from './cmds/archive.js';
import authTest from './cmds/authTest.js';
import ghMirrorUpload from './cmds/ghMirrorUpload.js';

export default {
  authTest,
  archive,
  ghMirrorUpload,
};

```

### File: main.ts
```ts
#!/usr/bin/env node

import childProcess from 'node:child_process';
import util from 'node:util';
import parseCommand from './cmd.js';
import exitUtils from './utils/exit.js';

async function main(): Promise<void> {
  try {
    process.platform === 'win32' ? await util.promisify(childProcess.exec)('chcp 65001') : undefined;
    await parseCommand();
  } catch (error) {
    console.log(error);
    exitUtils.pressAnyKeyToExit(1);
  }
}

await main();

```


```

### File: tsconfig.json
```json
{
  "extends": [
    // "@tsconfig/bun",
    "@tsconfig/recommended",
    "@tsconfig/node24",
    "@tsconfig/strictest"
  ],
  "compilerOptions": {
    "outDir": "./dist",
    "sourceMap": false,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}

```

### File: src\cmd.ts
```ts
import path from 'node:path';
import yargs from 'yargs';
import { hideBin } from 'yargs/helpers';
import cmds from './cmds.js';
import * as TypesLogLevels from './types/LogLevels.js';
import argvUtils from './utils/argv.js';
import appConfig from './utils/config.js';
import configEmbed from './utils/configEmbed.js';
import exitUtils from './utils/exit.js';
import logger from './utils/logger.js';

if (configEmbed.VERSION_NUMBER === null) throw new Error('Embed VERSION_NUMBER is null');

function wrapHandler(handler: (argv: any) => Promise<void>) {
  return async (argv: any) => {
    try {
      await handler(argv);
      await exitUtils.exit(0);
    } catch (error) {
      logger.error('Error caught:', error);
      await exitUtils.exit(1);
    }
  };
}

async function parseCommand() {
  const yargsInstance = yargs(hideBin(process.argv));
  await yargsInstance
    .command(
      ['archive'],
      'Archive all APIs',
      (yargs) => {
        yargs.options({
          'output-dir': {
            alias: ['o'],
            desc: 'Output root directory',
            default: path.resolve('output'),
            normalize: true,
            type: 'string',
          },
        });
      },
      wrapHandler(cmds.archive),
    )
    .command(
      ['ghMirrorUpload'],
      'Upload pending large binary file to GitHub mirror',
      (yargs) => {
        yargs.options({
          'output-dir': {
            alias: ['o'],
            desc: 'Output root directory',
            default: path.resolve('output'),
            normalize: true,
            type: 'string',
          },
        });
      },
      wrapHandler(cmds.ghMirrorUpload),
    )
    .command(
      ['authTest [token] [email] [password]'],
      'Auth and gacha fetch test command',
      (yargs) => {
        yargs
          .positional('token', {
            describe: 'Gryphline account service token',
            type: 'string',
          })
          .positional('email', {
            describe: 'Gryphline account email address',
            type: 'string',
          })
          .positional('password', {
            describe: 'Gryphline account password',
            type: 'string',
          })
          .options({});
      },
      wrapHandler(cmds.authTest),
    )
    .options({
      'log-level': {
        desc: 'Set log level (' + TypesLogLevels.LOG_LEVELS_NUM.join(', ') + ')',
        default: appConfig.logger.logLevel,
        type: 'number',
        coerce: (arg: number): TypesLogLevels.LogLevelString => {
          if (arg < TypesLogLevels.LOG_LEVELS_NUM[0] || arg > TypesLogLevels.LOG_LEVELS_NUM.slice(-1)[0]!) {
            throw new Error(`Invalid log level: ${arg} (Expected: ${TypesLogLevels.LOG_LEVELS_NUM.join(', ')})`);
          } else {
            return TypesLogLevels.LOG_LEVELS[arg as TypesLogLevels.LogLevelNumber];
          }
        },
      },
    })
    .middleware(async (argv) => {
      argvUtils.setArgv(argv);
      logger.level = argvUtils.getArgv()['logLevel'];
      logger.trace('Process started: ' + `${configEmbed.APPLICATION_NAME} v${configEmbed.VERSION_NUMBER}`);
    })
    .scriptName(configEmbed.APPLICATION_NAME)
    .version(String(configEmbed.VERSION_NUMBER))
    .usage('$0 <command> [argument] [option]')
    .help()
    .alias('help', 'h')
    .alias('help', '?')
    .alias('version', 'V')
    .demandCommand(1)
    .strict()
    .recommendCommands()
    .parse();
}

export default parseCommand;

```

### File: src\cmds.ts
```ts
import archive from './cmds/archive.js';
import authTest from './cmds/authTest.js';
import ghMirrorUpload from './cmds/ghMirrorUpload.js';

export default {
  authTest,
  archive,
  ghMirrorUpload,
};

```

### File: src\main.ts
```ts
#!/usr/bin/env node

import childProcess from 'node:child_process';
import util from 'node:util';
import parseCommand from './cmd.js';
import exitUtils from './utils/exit.js';

async function main(): Promise<void> {
  try {
    process.platform === 'win32' ? await util.promisify(childProcess.exec)('chcp 65001') : undefined;
    await parseCommand();
  } catch (error) {
    console.log(error);
    exitUtils.pressAnyKeyToExit(1);
  }
}

await main();

```


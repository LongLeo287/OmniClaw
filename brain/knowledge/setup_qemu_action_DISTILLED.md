---
id: setup-qemu-action
type: knowledge
owner: OA_Triage
---
# setup-qemu-action
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "docker-setup-qemu",
  "description": "Install QEMU static binaries",
  "type": "module",
  "main": "src/main.ts",
  "scripts": {
    "build": "ncc build src/main.ts --source-map --minify --license licenses.txt",
    "lint": "eslint --max-warnings=0 .",
    "format": "eslint --fix .",
    "test": "vitest run"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/docker/setup-qemu-action.git"
  },
  "keywords": [
    "actions",
    "docker",
    "qemu"
  ],
  "author": "Docker Inc.",
  "license": "Apache-2.0",
  "packageManager": "yarn@4.9.2",
  "dependencies": {
    "@actions/core": "^3.0.0",
    "@docker/actions-toolkit": "^0.79.0"
  },
  "devDependencies": {
    "@eslint/js": "^9.39.3",
    "@types/node": "^24.11.0",
    "@typescript-eslint/eslint-plugin": "^8.56.1",
    "@typescript-eslint/parser": "^8.56.1",
    "@vercel/ncc": "^0.38.4",
    "@vitest/coverage-v8": "^4.0.18",
    "@vitest/eslint-plugin": "^1.6.9",
    "eslint": "^9.39.3",
    "eslint-config-prettier": "^10.1.8",
    "eslint-plugin-prettier": "^5.5.5",
    "globals": "^17.3.0",
    "prettier": "^3.8.1",
    "typescript": "^5.9.3",
    "vitest": "^4.0.18"
  }
}

```

### File: README.md
```md
[![GitHub release](https://img.shields.io/github/release/docker/setup-qemu-action.svg?style=flat-square)](https://github.com/docker/setup-qemu-action/releases/latest)
[![GitHub marketplace](https://img.shields.io/badge/marketplace-docker--setup--qemu-blue?logo=github&style=flat-square)](https://github.com/marketplace/actions/docker-setup-qemu)
[![CI workflow](https://img.shields.io/github/actions/workflow/status/docker/setup-qemu-action/ci.yml?branch=master&label=ci&logo=github&style=flat-square)](https://github.com/docker/setup-qemu-action/actions?workflow=ci)
[![Test workflow](https://img.shields.io/github/actions/workflow/status/docker/setup-qemu-action/test.yml?branch=master&label=test&logo=github&style=flat-square)](https://github.com/docker/setup-qemu-action/actions?workflow=test)
[![Codecov](https://img.shields.io/codecov/c/github/docker/setup-qemu-action?logo=codecov&style=flat-square)](https://codecov.io/gh/docker/setup-qemu-action)

## About

GitHub Action to install [QEMU](https://github.com/qemu/qemu) static binaries.

![Screenshot](.github/setup-qemu-action.png)

___

* [Usage](#usage)
* [Customizing](#customizing)
  * [inputs](#inputs)
  * [outputs](#outputs)
* [Contributing](#contributing)

## Usage

```yaml
name: ci

on:
  push:

jobs:
  qemu:
    runs-on: ubuntu-latest
    steps:
      -
        name: Set up QEMU
        uses: docker/setup-qemu-action@v4
```

> [!NOTE]
> If you are using [`docker/setup-buildx-action`](https://github.com/docker/setup-buildx-action),
> this action should come before it:
> 
> ```yaml
>     -
>       name: Set up QEMU
>       uses: docker/setup-qemu-action@v4
>     -
>       name: Set up Docker Buildx
>       uses: docker/setup-buildx-action@v4
> ```

## Customizing

### inputs

The following inputs can be used as `step.with` keys:

| Name          | Type   | Default                                                                       | Description                                        |
|---------------|--------|-------------------------------------------------------------------------------|----------------------------------------------------|
| `image`       | String | [`tonistiigi/binfmt:latest`](https://hub.docker.com/r/tonistiigi/binfmt/tags) | QEMU static binaries Docker image                  |
| `platforms`   | String | `all`                                                                         | Platforms to install (e.g., `arm64,riscv64,arm`)   |
| `cache-image` | Bool   | `true`                                                                        | Cache binfmt image to GitHub Actions cache backend |

### outputs

The following outputs are available:

| Name          | Type    | Description                           |
|---------------|---------|---------------------------------------|
| `platforms`   | String  | Available platforms (comma separated) |

## Contributing

Want to contribute? Awesome! You can find information about contributing to
this project in the [CONTRIBUTING.md](/.github/CONTRIBUTING.md)

```

### File: .prettierrc.json
```json
{
  "printWidth": 120,
  "tabWidth": 2,
  "useTabs": false,
  "semi": true,
  "singleQuote": true,
  "trailingComma": "none",
  "bracketSpacing": false,
  "arrowParens": "avoid"
}

```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    "module": "nodenext",
    "moduleResolution": "nodenext",
    "esModuleInterop": true,
    "newLine": "lf",
    "outDir": "./lib",
    "rootDir": "./src",
    "forceConsistentCasingInFileNames": true,
    "noImplicitAny": false,
    "resolveJsonModule": true,
    "useUnknownInCatchVariables": false,
  },
  "include": [
    "src/**/*.ts"
  ]
}

```

### File: vitest.config.ts
```ts
import {defineConfig} from 'vitest/config';

export default defineConfig({
  test: {
    clearMocks: true,
    environment: 'node',
    setupFiles: ['./__tests__/setup.unit.ts'],
    include: ['**/*.test.ts'],
    coverage: {
      provider: 'v8',
      reporter: ['clover'],
      include: ['src/**/*.ts'],
      exclude: ['src/**/main.ts']
    }
  }
});

```

### File: .github\CODE_OF_CONDUCT.md
```md
# Code of conduct

- [Moby community guidelines](https://github.com/moby/moby/blob/master/CONTRIBUTING.md#moby-community-guidelines)

```

### File: .github\CONTRIBUTING.md
```md
## Contributing

Hi there! We're thrilled that you'd like to contribute to this project. Your help is essential for keeping it great.

Contributions to this project are [released](https://docs.github.com/en/github/site-policy/github-terms-of-service#6-contributions-under-repository-license)
to the public under the [project's open source license](LICENSE).

## Submitting a pull request

1. [Fork](https://github.com/docker/setup-qemu-action/fork) and clone the repository
2. Configure and install the dependencies: `yarn install`
3. Create a new branch: `git checkout -b my-branch-name`
4. Make your changes
5. Format code and build javascript artifacts: `docker buildx bake pre-checkin`
6. Validate all code has correctly formatted and built: `docker buildx bake validate`
7. Push to your fork and [submit a pull request](https://github.com/docker/setup-qemu-action/compare)
8. Pat yourself on the back and wait for your pull request to be reviewed and merged.

Here are a few things you can do that will increase the likelihood of your pull request being accepted:

- Make sure the `README.md` and any other relevant **documentation are kept up-to-date**.
- We try to follow [SemVer v2.0.0](https://semver.org/). Randomly breaking public APIs is not an option.
- Keep your change as focused as possible. If there are multiple changes you would like to make that are not dependent upon each other, consider submitting them as **separate pull requests**.
- Write a [good commit message](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html).

## Resources

- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [Using Pull Requests](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests)
- [GitHub Help](https://docs.github.com/en)

```

### File: .github\SECURITY.md
```md
# Reporting security issues

The project maintainers take security seriously. If you discover a security
issue, please bring it to their attention right away!

**Please _DO NOT_ file a public issue**, instead send your report privately to
[security@docker.com](mailto:security@docker.com).

Security reports are greatly appreciated, and we will publicly thank you for it.
We also like to send gifts&mdash;if you'd like Docker swag, make sure to let
us know. We currently do not offer a paid security bounty program, but are not
ruling it out in the future.

```

### File: src\context.ts
```ts
import * as core from '@actions/core';
import {Util} from '@docker/actions-toolkit/lib/util.js';

export interface Inputs {
  image: string;
  platforms: string;
  cacheImage: boolean;
}

export function getInputs(): Inputs {
  return {
    image: core.getInput('image') || 'docker.io/tonistiigi/binfmt:latest',
    platforms: Util.getInputList('platforms').join(',') || 'all',
    cacheImage: core.getBooleanInput('cache-image')
  };
}

```

### File: src\main.ts
```ts
import * as core from '@actions/core';
import * as actionsToolkit from '@docker/actions-toolkit';

import {Docker} from '@docker/actions-toolkit/lib/docker/docker.js';

import * as context from './context.js';

interface Platforms {
  supported: string[];
  available: string[];
}

actionsToolkit.run(
  // main
  async () => {
    const input: context.Inputs = context.getInputs();

    await core.group(`Docker info`, async () => {
      await Docker.printVersion();
      await Docker.printInfo();
    });

    await core.group(`Pulling binfmt Docker image`, async () => {
      await Docker.pull(input.image, input.cacheImage);
    });

    await core.group(`Image info`, async () => {
      await Docker.getExecOutput(['image', 'inspect', input.image], {
        ignoreReturnCode: true
      }).then(res => {
        if (res.stderr.length > 0 && res.exitCode != 0) {
          throw new Error(res.stderr.match(/(.*)\s*$/)?.[0]?.trim() ?? 'unknown error');
        }
      });
    });

    await core.group(`Binfmt version`, async () => {
      await Docker.getExecOutput(['run', '--rm', '--privileged', input.image, '--version'], {
        ignoreReturnCode: true
      }).then(res => {
        if (res.stderr.length > 0 && res.exitCode != 0) {
          throw new Error(res.stderr.match(/(.*)\s*$/)?.[0]?.trim() ?? 'unknown error');
        }
      });
    });

    await core.group(`Installing QEMU static binaries`, async () => {
      await Docker.getExecOutput(['run', '--rm', '--privileged', input.image, '--install', input.platforms], {
        ignoreReturnCode: true
      }).then(res => {
        if (res.stderr.length > 0 && res.exitCode != 0) {
          throw new Error(res.stderr.match(/(.*)\s*$/)?.[0]?.trim() ?? 'unknown error');
        }
      });
    });

    await core.group(`Extracting available platforms`, async () => {
      await Docker.getExecOutput(['run', '--rm', '--privileged', input.image], {
        ignoreReturnCode: true,
        silent: true
      }).then(res => {
        if (res.stderr.length > 0 && res.exitCode != 0) {
          throw new Error(res.stderr.match(/(.*)\s*$/)?.[0]?.trim() ?? 'unknown error');
        }
        const platforms: Platforms = JSON.parse(res.stdout.trim());
        core.info(`${platforms.supported.join(',')}`);
        core.setOutput('platforms', platforms.supported.join(','));
      });
    });
  }
);

```

### File: __tests__\context.test.ts
```ts
import {beforeEach, describe, expect, test} from 'vitest';

import * as context from '../src/context.js';

describe('getInputs', () => {
  beforeEach(() => {
    process.env = Object.keys(process.env).reduce((object, key) => {
      if (!key.startsWith('INPUT_')) {
        object[key] = process.env[key];
      }
      return object;
    }, {});
  });

  // prettier-ignore
  const cases: [number, Map<string, string>, context.Inputs][] = [
    [
      0,
      new Map<string, string>([
        ['cache-image', 'true'],
      ]),
      {
        image: 'docker.io/tonistiigi/binfmt:latest',
        platforms: 'all',
        cacheImage: true,
      }
    ],
    [
      1,
      new Map<string, string>([
        ['image', 'docker/binfmt:latest'],
        ['platforms', 'arm64,riscv64,arm'],
        ['cache-image', 'false'],
      ]),
      {
        image: 'docker/binfmt:latest',
        platforms: 'arm64,riscv64,arm',
        cacheImage: false,
      }
    ],
    [
      2,
      new Map<string, string>([
        ['platforms', 'arm64, riscv64, arm '],
        ['cache-image', 'true'],
      ]),
      {
        image: 'docker.io/tonistiigi/binfmt:latest',
        platforms: 'arm64,riscv64,arm',
        cacheImage: true,
      }
    ]
  ];
  test.each(cases)(
    '[%d] given %o as inputs, returns %o',
    async (num: number, inputs: Map<string, string>, expected: context.Inputs) => {
      inputs.forEach((value: string, name: string) => {
        setInput(name, value);
      });
      const res = await context.getInputs();
      expect(res).toEqual(expected);
    }
  );
});

// See: https://github.com/actions/toolkit/blob/master/packages/core/src/core.ts#L67
function getInputName(name: string): string {
  return `INPUT_${name.replace(/ /g, '_').toUpperCase()}`;
}

function setInput(name: string, value: string): void {
  process.env[getInputName(name)] = value;
}

```

### File: __tests__\setup.unit.ts
```ts
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'docker-setup-qemu-action-'));

process.env = Object.assign({}, process.env, {
  TEMP: tmpDir,
  GITHUB_REPOSITORY: 'docker/setup-qemu-action',
  RUNNER_TEMP: path.join(tmpDir, 'runner-temp'),
  RUNNER_TOOL_CACHE: path.join(tmpDir, 'runner-tool-cache')
});

```


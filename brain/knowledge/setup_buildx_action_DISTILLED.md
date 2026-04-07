---
id: setup-buildx-action
type: knowledge
owner: OA_Triage
---
# setup-buildx-action
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "docker-setup-buildx",
  "description": "Set up Docker Buildx",
  "type": "module",
  "main": "src/main.ts",
  "scripts": {
    "build": "ncc build --source-map --minify --license licenses.txt",
    "lint": "eslint --max-warnings=0 .",
    "format": "eslint --fix .",
    "test": "vitest run"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/docker/setup-buildx-action.git"
  },
  "keywords": [
    "actions",
    "docker",
    "buildx"
  ],
  "author": "Docker Inc.",
  "license": "Apache-2.0",
  "packageManager": "yarn@4.9.2",
  "dependencies": {
    "@actions/core": "^3.0.0",
    "@docker/actions-toolkit": "^0.79.0",
    "js-yaml": "^4.1.1"
  },
  "devDependencies": {
    "@eslint/js": "^9.39.3",
    "@types/js-yaml": "^4.0.9",
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
[![GitHub release](https://img.shields.io/github/release/docker/setup-buildx-action.svg?style=flat-square)](https://github.com/docker/setup-buildx-action/releases/latest)
[![GitHub marketplace](https://img.shields.io/badge/marketplace-docker--setup--buildx-blue?logo=github&style=flat-square)](https://github.com/marketplace/actions/docker-setup-buildx)
[![CI workflow](https://img.shields.io/github/actions/workflow/status/docker/setup-buildx-action/ci.yml?branch=master&label=ci&logo=github&style=flat-square)](https://github.com/docker/setup-buildx-action/actions?workflow=ci)
[![Test workflow](https://img.shields.io/github/actions/workflow/status/docker/setup-buildx-action/test.yml?branch=master&label=test&logo=github&style=flat-square)](https://github.com/docker/setup-buildx-action/actions?workflow=test)
[![Codecov](https://img.shields.io/codecov/c/github/docker/setup-buildx-action?logo=codecov&style=flat-square)](https://codecov.io/gh/docker/setup-buildx-action)

## About

GitHub Action to set up Docker [Buildx](https://github.com/docker/buildx).

This action will create and boot a builder that can be used in the following
steps of your workflow if you're using Buildx or the [`build-push` action](https://github.com/docker/build-push-action/).
By default, the [`docker-container` driver](https://docs.docker.com/build/building/drivers/docker-container/)
will be used to be able to build multi-platform images and export cache using
a [BuildKit](https://github.com/moby/buildkit) container.

![Screenshot](.github/setup-buildx-action.png)

___

* [Usage](#usage)
* [Configuring your builder](#configuring-your-builder)
* [Customizing](#customizing)
  * [inputs](#inputs)
  * [outputs](#outputs)
  * [environment variables](#environment-variables)
* [Notes](#notes)
  * [`nodes` output](#nodes-output)
* [Contributing](#contributing)

## Usage

```yaml
name: ci

on:
  push:

jobs:
  buildx:
    runs-on: ubuntu-latest
    steps:
      -
        # Add support for more platforms with QEMU (optional)
        # https://github.com/docker/setup-qemu-action
        name: Set up QEMU
        uses: docker/setup-qemu-action@v4
      -
        name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v4
```

## Configuring your builder

* [Version pinning](https://docs.docker.com/build/ci/github-actions/configure-builder/#version-pinning): Pin to a specific Buildx or BuildKit version
* [BuildKit container logs](https://docs.docker.com/build/ci/github-actions/configure-builder/#buildkit-container-logs): Enable BuildKit container logs for debugging purposes
* [BuildKit Daemon configuration](https://docs.docker.com/build/ci/github-actions/configure-builder/#buildkit-daemon-configuration)
  * [Registry mirror](https://docs.docker.com/build/ci/github-actions/configure-builder/#registry-mirror): Configure a registry mirror for your builds
  * [Max parallelism](https://docs.docker.com/build/ci/github-actions/configure-builder/#max-parallelism): Configure the maximum parallelism for your builds
* [Append additional nodes to the builder](https://docs.docker.com/build/ci/github-actions/configure-builder/#append-additional-nodes-to-the-builder): Create additional nodes for your builder
* [Authentication for remote builders](https://docs.docker.com/build/ci/github-actions/configure-builder/#authentication-for-remote-builders)
  * [SSH authentication](https://docs.docker.com/build/ci/github-actions/configure-builder/#ssh-authentication): Authenticate to a remote builder using SSH
  * [TLS authentication](https://docs.docker.com/build/ci/github-actions/configure-builder/#tls-authentication): Authenticate to a remote builder using TLS
* [Standalone mode](https://docs.docker.com/build/ci/github-actions/configure-builder/#standalone-mode): Use Buildx as a standalone binary (without the Docker CLI)
* [Isolated builders](https://docs.docker.com/build/ci/github-actions/configure-builder/#isolated-builders): Create isolated builders for your builds

## Customizing

### inputs

The following inputs can be used as `step.with` keys:

> `List` type is a newline-delimited string
> ```yaml
> driver-opts: |
>   image=moby/buildkit:master
>   network=host
> ```

> `CSV` type must be a comma-delimited string
> ```yaml
> platforms: linux/amd64,linux/arm64
> ```

| Name                         | Type     | Default            | Description                                                                                                                                                                 |
|------------------------------|----------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `version`                    | String   |                    | [Buildx](https://github.com/docker/buildx) version. (eg. `v0.3.0`, `latest`, `https://github.com/docker/buildx.git#master`)                                                 |
| `name`                       | String   |                    | Name of the builder. If not specified, one will be generated or if it already exists, it will be used instead of creating a new one                                         |
| `driver`                     | String   | `docker-container` | Sets the [builder driver](https://docs.docker.com/engine/reference/commandline/buildx_create/#driver) to be used                                                            |
| `driver-opts`                | List     |                    | List of additional [driver-specific options](https://docs.docker.com/engine/reference/commandline/buildx_create/#driver-opt) (eg. `image=moby/buildkit:master`)             |
| `buildkitd-flags`            | String   |                    | [BuildKit daemon flags](https://docs.docker.com/engine/reference/commandline/buildx_create/#buildkitd-flags)                                                                |
| `buildkitd-config` \*        | String   |                    | [BuildKit daemon config file](https://docs.docker.com/engine/reference/commandline/buildx_create/#config)                                                                   |
| `buildkitd-config-inline` \* | String   |                    | Same as `buildkitd-config` but inline                                                                                                                                       |
| `use`                        | Bool     | `true`             | Switch to this builder instance                                                                                                                                             |
| `endpoint`                   | String   |                    | [Optional address for docker socket](https://docs.docker.com/engine/reference/commandline/buildx_create/#description) or context from `docker context ls`                   |
| `platforms`                  | List/CSV |                    | Fixed [platforms](https://docs.docker.com/engine/reference/commandline/buildx_create/#platform) for current node. If not empty, values take priority over the detected ones |
| `append`                     | YAML     |                    | [Append additional nodes](https://docs.docker.com/build/ci/github-actions/configure-builder/#append-additional-nodes-to-the-builder) to the builder                         |
| `keep-state`                 | Bool     | `false`            | Keep BuildKit state on `cleanup`. This is only useful on persistent self-hosted runners                                                                                     |
| `cache-binary`               | Bool     | `true`             | Cache buildx binary to GitHub Actions cache backend                                                                                                                         |
| `cleanup`                    | Bool     | `true`             | Cleanup temp files and remove builder at the end of a job                                                                                                                   |

> [!IMPORTANT]
> If you set the `buildkitd-flags` input, the default flags (`--allow-insecure-entitlement security.insecure --allow-insecure-entitlement network.host`)
> will be reset. If you want to retain the default behavior, make sure to
> include these flags in your custom `buildkitd-flags` value.

> [!NOTE]
> `buildkitd-config` and `buildkitd-config-inline` are mutually exclusive.

### outputs

The following outputs are available:

| Name        | Type   | Description                                         |
|-------------|--------|-----------------------------------------------------|
| `name`      | String | Builder name                                        |
| `driver`    | String | Builder driver                                      |
| `platforms` | String | Builder node platforms (preferred and/or available) |
| `nodes`     | JSON   | Builder [nodes metadata](#nodes-output)             |

### environment variables

The following [official docker environment variables](https://docs.docker.com/engine/reference/commandline/cli/#environment-variables) are supported:

| Name            | Type   | Default     | Description                                     |
|-----------------|--------|-------------|-------------------------------------------------|
| `DOCKER_CONFIG` | String | `~/.docker` | The location of your client configuration files |

## Notes

### `nodes` output

| Name              | Type   | Description                |
|-------------------|--------|----------------------------|
| `name`            | String | Node name                  |
| `endpoint`        | String | Node endpoint              |
| `driver-opts`     | List   | Options for the driver     |
| `status`          | String | Node status                |
| `buildkitd-flags` | String | Flags for buildkitd daemon |
| `buildkit`        | String | BuildKit version           |
| `platforms`       | String | Platforms available        |

Example:

```json
[
  {
    "name": "builder-8fa135e1-9bce-4a29-9368-46a09a1d750d0",
    "endpoint": "unix:///var/run/docker.sock",
    "status": "running",
    "buildkitd-flags": "--allow-insecure-entitlement security.insecure --allow-insecure-entitlement network.host",
    "buildkit": "v0.27.1",
    "platforms": "linux/amd64,linux/amd64/v2,linux/amd64/v3,linux/386"
  }
]
```

## Contributing

Want to contribute? Awesome! You can find information about contributing to
this project in the [CONTRIBUTING.md](/.github/CONTRIBUTING.md)

```

### File: .prettierrc.json
```json
{
  "printWidth": 240,
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

1. [Fork](https://github.com/docker/setup-buildx-action/fork) and clone the repository
2. Configure and install the dependencies: `yarn install`
3. Create a new branch: `git checkout -b my-branch-name`
4. Make your changes
5. Make sure the tests pass: `docker buildx bake test`
6. Format code and build javascript artifacts: `docker buildx bake pre-checkin`
7. Validate all code has correctly formatted and built: `docker buildx bake validate`
8. Push to your fork and [submit a pull request](https://github.com/docker/setup-buildx-action/compare)
9. Pat your self on the back and wait for your pull request to be reviewed and merged.

Here are a few things you can do that will increase the likelihood of your pull request being accepted:

- Write tests.
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
import * as crypto from 'crypto';
import * as core from '@actions/core';

import {Docker} from '@docker/actions-toolkit/lib/docker/docker.js';
import {Util} from '@docker/actions-toolkit/lib/util.js';
import {Toolkit} from '@docker/actions-toolkit/lib/toolkit.js';

import {Node} from '@docker/actions-toolkit/lib/types/buildx/builder.js';

export const builderNodeEnvPrefix = 'BUILDER_NODE';
const defaultBuildkitdFlags = '--allow-insecure-entitlement security.insecure --allow-insecure-entitlement network.host';

export interface Inputs {
  version: string;
  name: string;
  driver: string;
  driverOpts: string[];
  buildkitdFlags: string;
  buildkitdConfig: string;
  buildkitdConfigInline: string;
  platforms: string[];
  use: boolean;
  endpoint: string;
  append: string;
  cacheBinary: boolean;
  cleanup: boolean;
  keepState: boolean;
}

export async function getInputs(): Promise<Inputs> {
  return {
    version: core.getInput('version'),
    name: await getBuilderName(core.getInput('name'), core.getInput('driver') || 'docker-container'),
    driver: core.getInput('driver') || 'docker-container',
    driverOpts: Util.getInputList('driver-opts', {ignoreComma: true, quote: false}),
    buildkitdFlags: core.getInput('buildkitd-flags'),
    platforms: Util.getInputList('platforms'),
    use: core.getBooleanInput('use'),
    endpoint: core.getInput('endpoint'),
    buildkitdConfig: core.getInput('buildkitd-config'),
    buildkitdConfigInline: core.getInput('buildkitd-config-inline'),
    append: core.getInput('append'),
    keepState: core.getBooleanInput('keep-state'),
    cacheBinary: core.getBooleanInput('cache-binary'),
    cleanup: core.getBooleanInput('cleanup')
  };
}

export async function getBuilderName(name: string, driver: string): Promise<string> {
  return driver == 'docker' ? await Docker.context() : name || `builder-${crypto.randomUUID()}`;
}

export async function getCreateArgs(inputs: Inputs, toolkit: Toolkit): Promise<Array<string>> {
  const args: Array<string> = ['create', '--name', inputs.name, '--driver', inputs.driver];
  if (await toolkit.buildx.versionSatisfies('>=0.3.0')) {
    await Util.asyncForEach(inputs.driverOpts, async (driverOpt: string) => {
      args.push('--driver-opt', driverOpt);
    });
    if (inputs.buildkitdFlags) {
      args.push('--buildkitd-flags', inputs.buildkitdFlags);
    } else if (driverSupportsBuildkitdFlags(inputs.driver)) {
      args.push('--buildkitd-flags', defaultBuildkitdFlags);
    }
  }
  if (inputs.platforms.length > 0) {
    args.push('--platform', inputs.platforms.join(','));
  }
  if (inputs.use) {
    args.push('--use');
  }
  if (inputs.buildkitdConfig) {
    args.push('--config', toolkit.buildkit.config.resolveFromFile(inputs.buildkitdConfig));
  } else if (inputs.buildkitdConfigInline) {
    args.push('--config', toolkit.buildkit.config.resolveFromString(inputs.buildkitdConfigInline));
  }
  if (inputs.endpoint) {
    args.push(inputs.endpoint);
  }
  return args;
}

export async function getAppendArgs(inputs: Inputs, node: Node, toolkit: Toolkit): Promise<Array<string>> {
  const args: Array<string> = ['create', '--name', inputs.name, '--append'];
  if (node.name) {
    args.push('--node', node.name);
  } else if (inputs.driver == 'kubernetes' && (await toolkit.buildx.versionSatisfies('<0.11.0'))) {
    args.push('--node', `node-${crypto.randomUUID()}`);
  }
  if (node['driver-opts'] && (await toolkit.buildx.versionSatisfies('>=0.3.0'))) {
    await Util.asyncForEach(node['driver-opts'], async (driverOpt: string) => {
      args.push('--driver-opt', driverOpt);
    });
    if (node['buildkitd-flags']) {
      args.push('--buildkitd-flags', node['buildkitd-flags']);
    } else if (driverSupportsBuildkitdFlags(inputs.driver)) {
      args.push('--buildkitd-flags', defaultBuildkitdFlags);
    }
  }
  if (node.platforms) {
    args.push('--platform', node.platforms);
  }
  if (node.endpoint) {
    args.push(node.endpoint);
  }
  return args;
}

export async function getInspectArgs(inputs: Inputs, toolkit: Toolkit): Promise<Array<string>> {
  const args: Array<string> = ['inspect', '--bootstrap'];
  if (await toolkit.buildx.versionSatisfies('>=0.4.0')) {
    args.push('--builder', inputs.name);
  }
  return args;
}

function driverSupportsBuildkitdFlags(driver: string): boolean {
  return driver == '' || driver == 'docker-container' || driver == 'docker' || driver == 'kubernetes';
}

export function getVersion(inputs: Inputs): string {
  const version = inputs.version;
  if (inputs.driver === 'cloud') {
    if (!version || version === 'latest') {
      return 'cloud:latest';
    }
    if (version.startsWith('cloud:') || version.startsWith('lab:')) {
      return version;
    }
    return `cloud:${version}`;
  }
  return version;
}

```

### File: src\main.ts
```ts
import * as crypto from 'crypto';
import * as fs from 'fs';
import * as yaml from 'js-yaml';
import * as core from '@actions/core';
import * as actionsToolkit from '@docker/actions-toolkit';

import {Buildx} from '@docker/actions-toolkit/lib/buildx/buildx.js';
import {Builder} from '@docker/actions-toolkit/lib/buildx/builder.js';
import {Docker} from '@docker/actions-toolkit/lib/docker/docker.js';
import {Exec} from '@docker/actions-toolkit/lib/exec.js';
import {Toolkit} from '@docker/actions-toolkit/lib/toolkit.js';
import {Util} from '@docker/actions-toolkit/lib/util.js';

import {Node} from '@docker/actions-toolkit/lib/types/buildx/builder.js';
import {ContextInfo} from '@docker/actions-toolkit/lib/types/docker/docker.js';

import * as context from './context.js';
import * as stateHelper from './state-helper.js';

actionsToolkit.run(
  // main
  async () => {
    const inputs: context.Inputs = await context.getInputs();
    stateHelper.setCleanup(inputs.cleanup);
    const version = context.getVersion(inputs);

    const toolkit = new Toolkit();
    const standalone = await toolkit.buildx.isStandalone();
    stateHelper.setStandalone(standalone);

    if (inputs.keepState && inputs.driver !== 'docker-container') {
      // https://docs.docker.com/reference/cli/docker/buildx/rm/#keep-state
      throw new Error(`Cannot use keep-state with ${inputs.driver} driver`);
    }
    stateHelper.setKeepState(inputs.keepState);

    await core.group(`Docker info`, async () => {
      try {
        await Docker.printVersion();
        await Docker.printInfo();
      } catch (e) {
        core.info(e.message);
      }
    });

    let toolPath;
    if (Util.isValidRef(version)) {
      if (standalone) {
        throw new Error(`Cannot build from source without the Docker CLI`);
      }
      await core.group(`Build buildx from source`, async () => {
        toolPath = await toolkit.buildxInstall.build(version, !inputs.cacheBinary);
      });
    } else if (!(await toolkit.buildx.isAvailable()) || version) {
      await core.group(`Download buildx from GitHub Releases`, async () => {
        toolPath = await toolkit.buildxInstall.download({
          version: version || 'latest',
          ghaNoCache: !inputs.cacheBinary
        });
      });
    }
    if (toolPath) {
      await core.group(`Install buildx`, async () => {
        if (standalone) {
          await toolkit.buildxInstall.installStandalone(toolPath);
        } else {
          await toolkit.buildxInstall.installPlugin(toolPath);
        }
      });
    }

    await core.group(`Buildx version`, async () => {
      await toolkit.buildx.printVersion();
    });

    core.setOutput('name', inputs.name);
    stateHelper.setBuilderName(inputs.name);
    stateHelper.setBuilderDriver(inputs.driver);

    fs.mkdirSync(Buildx.certsDir, {recursive: true});
    stateHelper.setCertsDir(Buildx.certsDir);

    // if the default context has TLS data loaded and endpoint is not set, then
    // we create a temporary docker context only if driver is docker-container
    // https://github.com/docker/buildx/blob/b96ad59f64d40873e4959336d294b648bb3937fe/builder/builder.go#L489
    // https://github.com/docker/setup-buildx-action/issues/105
    if (!standalone && inputs.driver == 'docker-container' && (await Docker.context()) == 'default' && inputs.endpoint.length == 0) {
      let defaultContextWithTLS: boolean = false;
      await core.group(`Inspecting default docker context`, async () => {
        await Docker.getExecOutput(['context', 'inspect', '--format=json', 'default'], {
          ignoreReturnCode: true,
          silent: true
        }).then(res => {
          if (res.stderr.length > 0 && res.exitCode != 0) {
            core.info(`Cannot inspect default docker context: ${res.stderr.trim()}`);
          } else {
            try {
              const contextInfo = (<Array<ContextInfo>>JSON.parse(res.stdout.trim()))[0];
              core.info(JSON.stringify(JSON.parse(res.stdout.trim()), undefined, 2));
              const hasTLSData = Object.keys(contextInfo.Endpoints).length > 0 && Object.values(contextInfo.Endpoints)[0].TLSData !== undefined;
              const hasTLSMaterial = Object.keys(contextInfo.TLSMaterial).length > 0 && Object.values(contextInfo.TLSMaterial)[0].length > 0;
              defaultContextWithTLS = hasTLSData || hasTLSMaterial;
            } catch (e) {
              core.info(`Unable to parse default docker context info: ${e}`);
              core.info(res.stdout.trim());
            }
          }
        });
      });
      if (defaultContextWithTLS) {
        const tmpDockerContext = `buildx-${crypto.randomUUID()}`;
        await core.group(`Creating temp docker context (TLS data loaded in default one)`, async () => {
          await Docker.getExecOutput(['context', 'create', tmpDockerContext], {
            ignoreReturnCode: true
          }).then(res => {
            if (res.stderr.length > 0 && res.exitCode != 0) {
              core.warning(`Cannot create docker context ${tmpDockerContext}: ${res.stderr.match(/(.*)\s*$/)?.[0]?.trim() ?? 'unknown error'}`);
            } else {
              core.info(`Setting builder endpoint to ${tmpDockerContext} context`);
              inputs.endpoint = tmpDockerContext;
              stateHelper.setTmpDockerContext(tmpDockerContext);
            }
          });
        });
      }
    }

    if (inputs.driver !== 'docker') {
      await core.group(`Creating a new builder instance`, async () => {
        if (await toolkit.builder.exists(inputs.name)) {
          core.info(`Builder ${inputs.name} already exists, skipping creation`);
        } else {
          const certsDriverOpts = Buildx.resolveCertsDriverOpts(inputs.driver, inputs.endpoint, {
            cacert: process.env[`${context.builderNodeEnvPrefix}_0_AUTH_TLS_CACERT`],
            cert: process.env[`${context.builderNodeEnvPrefix}_0_AUTH_TLS_CERT`],
            key: process.env[`${context.builderNodeEnvPrefix}_0_AUTH_TLS_KEY`]
          });
          if (certsDriverOpts.length > 0) {
            inputs.driverOpts = [...inputs.driverOpts, ...certsDriverOpts];
          }
          const createCmd = await toolkit.buildx.getCommand(await context.getCreateArgs(inputs, toolkit));
          await Exec.getExecOutput(createCmd.command, createCmd.args, {
            ignoreReturnCode: true
          }).then(res => {
            if (res.stderr.length > 0 && res.exitCode != 0) {
              throw new Error(res.stderr.match(/(.*)\s*$/)?.[0]?.trim() ?? 'unknown error');
            }
          });
        }
      });
    }

    if (inputs.append) {
      await core.group(`Appending node(s) to builder`, async () => {
        let nodeIndex = 1;
        const nodes = yaml.load(inputs.append) as Node[];
        for (const node of nodes) {
          const certsDriverOpts = Buildx.resolveCertsDriverOpts(inputs.driver, `${node.endpoint}`, {
            cacert: process.env[`${context.builderNodeEnvPrefix}_${nodeIndex}_AUTH_TLS_CACERT`],
            cert: process.env[`${context.builderNodeEnvPrefix}_${nodeIndex}_AUTH_TLS_CERT`],
            key: process.env[`${context.builderNodeEnvPrefix}_${nodeIndex}_AUTH_TLS_KEY`]
          });
          if (certsDriverOpts.length > 0) {
            node['driver-opts'] = [...(node['driver-opts'] || []), ...certsDriverOpts];
          }
          const appendCmd = await toolkit.buildx.getCommand(await context.getAppendArgs(inputs, node, toolkit));
          await Exec.getExecOutput(appendCmd.command, appendCmd.args, {
            ignoreReturnCode: true
          }).then(res => {
            if (res.stderr.length > 0 && res.exitCode != 0) {
              throw new Error(`Failed to append node ${node.name}: ${res.stderr.match(/(.*)\s*$/)?.[0]?.trim() ?? 'unknown error'}`);
            }
          });
          nodeIndex++;
        }
      });
    }

    await core.group(`Booting builder`, async () => {
      const inspectCmd = await toolkit.buildx.getCommand(await context.getInspectArgs(inputs, toolkit));
      await Exec.getExecOutput(inspectCmd.command, inspectCmd.args, {
        ignoreReturnCode: true
      }).then(res => {
        if (res.stderr.length > 0 && res.exitCode != 0) {
          throw new Error(res.stderr.match(/(.*)\s*$/)?.[0]?.trim() ?? 'unknown error');
        }
      });
    });

    const builderInspect = await toolkit.builder.inspect(inputs.name);
    const firstNode = builderInspect.nodes[0];

    await core.group(`Inspect builder`, async () => {
      const reducedPlatforms: Array<string> = [];
      for (const node of builderInspect.nodes) {
        for (const platform of node.platforms?.split(',') || []) {
          if (reducedPlatforms.indexOf(platform) > -1) {
            continue;
          }
          reducedPlatforms.push(platform);
        }
      }
      core.info(JSON.stringify(builderInspect, undefined, 2));
      core.setOutput('driver', builderInspect.driver);
      core.setOutput('platforms', reducedPlatforms.join(','));
      core.setOutput('nodes', JSON.stringify(builderInspect.nodes, undefined, 2));
    });

    if (!standalone && builderInspect.driver == 'docker-container') {
      stateHelper.setContainerName(`${Buildx.containerNamePrefix}${firstNode.name}`);
      await core.group(`BuildKit version`, async () => {
        for (const node of builderInspect.nodes) {
          const buildkitVersion = await toolkit.buildkit.getVersion(node);
          core.info(`${node.name}: ${buildkitVersion}`);
        }
      });
    }
    if (core.isDebug() || firstNode['buildkitd-flags']?.includes('--debug')) {
      stateHelper.setDebug('true');
    }
  },
  // post
  async () => {
    if (stateHelper.IsDebug && stateHelper.containerName.length > 0) {
      await core.group(`BuildKit container logs`, async () => {
        await Docker.getExecOutput(['logs', `${stateHelper.containerName}`], {
          ignoreReturnCode: true
        }).then(res => {
          if (res.stderr.length > 0 && res.exitCode != 0) {
            core.warning(res.stderr.match(/(.*)\s*$/)?.[0]?.trim() ?? 'unknown error');
          }
        });
      });
    }

    if (!stateHelper.cleanup) {
      return;
    }

    if (stateHelper.builderDriver != 'docker' && stateHelper.builderName.length > 0) {
      await core.group(`Removing builder`, async () => {
        const buildx = new Buildx({standalone: stateHelper.standalone});
        const builder = new Builder({buildx: buildx});
        if (await builder.exists(stateHelper.builderName)) {
          const rmCmd = await buildx.getCommand(['rm', stateHelper.builderName, ...(stateHelper.keepState ? ['--keep-state'] : [])]);
          await Exec.getExecOutput(rmCmd.command, rmCmd.args, {
            ignoreReturnCode: true
          }).then(res => {
            if (res.stderr.length > 0 && res.exitCode != 0) {
              core.warning(res.stderr.match(/(.*)\s*$/)?.[0]?.trim() ?? 'unknown error');
            }
          });
        } else {
          core.info(`${stateHelper.builderName} does not exist`);
        }
      });
    }

    if (stateHelper.tmpDockerContext) {
      await core.group(`Removing temp docker context`, async () => {
        await Exec.getExecOutput('docker', ['context', 'rm', '-f', stateHelper.tmpDockerContext], {
          ignoreReturnCode: true
        }).then(res => {
          if (res.stderr.length > 0 && res.exitCode != 0) {
            core.warning(`${res.stderr.match(/(.*)\s*$/)?.[0]?.trim() ?? 'unknown error'}`);
          }
        });
      });
    }

    if (stateHelper.certsDir.length > 0 && fs.existsSync(stateHelper.certsDir)) {
      await core.group(`Cleaning up certificates`, async () => {
        fs.rmSync(stateHelper.certsDir, {recursive: true});
      });
    }
  }
);

```

### File: src\state-helper.ts
```ts
import * as core from '@actions/core';

export const IsDebug = !!process.env['STATE_isDebug'];
export const standalone = /true/i.test(process.env['STATE_standalone'] || '');
export const builderName = process.env['STATE_builderName'] || '';
export const builderDriver = process.env['STATE_builderDriver'] || '';
export const containerName = process.env['STATE_containerName'] || '';
export const certsDir = process.env['STATE_certsDir'] || '';
export const tmpDockerContext = process.env['STATE_tmpDockerContext'] || '';
export const cleanup = /true/i.test(process.env['STATE_cleanup'] || '');
export const keepState = /true/i.test(process.env['STATE_keepState'] || '');

export function setDebug(debug: string) {
  core.saveState('isDebug', debug);
}

export function setStandalone(standalone: boolean) {
  core.saveState('standalone', standalone);
}

export function setBuilderName(builderName: string) {
  core.saveState('builderName', builderName);
}

export function setBuilderDriver(builderDriver: string) {
  core.saveState('builderDriver', builderDriver);
}

export function setContainerName(containerName: string) {
  core.saveState('containerName', containerName);
}

export function setCertsDir(certsDir: string) {
  core.saveState('certsDir', certsDir);
}

export function setTmpDockerContext(tmpDockerContext: string) {
  core.saveState('tmpDockerContext', tmpDockerContext);
}

export function setCleanup(cleanup: boolean) {
  core.saveState('cleanup', cleanup);
}

export function setKeepState(keepState: boolean) {
  core.saveState('keepState', keepState);
}

```

### File: __tests__\context.test.ts
```ts
import {beforeEach, describe, expect, test, vi} from 'vitest';
import * as fs from 'fs';
import * as os from 'os';
import * as path from 'path';

import {Buildx} from '@docker/actions-toolkit/lib/buildx/buildx.js';
import {Context} from '@docker/actions-toolkit/lib/context.js';
import {Docker} from '@docker/actions-toolkit/lib/docker/docker.js';
import {Toolkit} from '@docker/actions-toolkit/lib/toolkit.js';

import {Node} from '@docker/actions-toolkit/lib/types/buildx/builder.js';

import * as context from '../src/context.js';

const fixturesDir = path.join(__dirname, 'fixtures');
const tmpDir = fs.mkdtempSync(path.join(process.env.TEMP || os.tmpdir(), 'context-'));
const tmpName = path.join(tmpDir, '.tmpname-vi');

vi.spyOn(Context, 'tmpDir').mockImplementation((): string => {
  if (!fs.existsSync(tmpDir)) {
    fs.mkdirSync(tmpDir, {recursive: true});
  }
  return tmpDir;
});

vi.spyOn(Context, 'tmpName').mockImplementation((): string => {
  return tmpName;
});

vi.mock('crypto', async () => {
  return {
    ...(await vi.importActual('crypto')),
    randomUUID: vi.fn(() => '9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d')
  };
});

vi.spyOn(Docker, 'context').mockImplementation((): Promise<string> => {
  return Promise.resolve('default');
});

describe('getCreateArgs', () => {
  beforeEach(() => {
    process.env = Object.keys(process.env).reduce((object, key) => {
      if (!key.startsWith('INPUT_')) {
        object[key] = process.env[key];
      }
      return object;
    }, {});
  });

  // prettier-ignore
  test.each([
    [
      0,
      'v0.10.3',
      new Map<string, string>([
        ['use', 'true'],
        ['cache-binary', 'true'],
        ['cleanup', 'true'],
        ['keep-state', 'false']
      ]),
      [
        'create',
        '--name', 'builder-9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d',
        '--driver', 'docker-container',
        '--buildkitd-flags', '--allow-insecure-entitlement security.insecure --allow-insecure-entitlement network.host',
        '--use'
      ]
    ],
    [
      1,
      'v0.10.3',
      new Map<string, string>([
        ['driver', 'docker'],
        ['use', 'true'],
        ['cache-binary', 'true'],
        ['cleanup', 'true'],
        ['keep-state', 'false']
      ]),
      [
        'create',
        '--name', 'default',
        '--driver', 'docker',
        '--buildkitd-flags', '--allow-insecure-entitlement security.insecure --allow-insecure-entitlement network.host',
        '--use'
      ]
    ],
    [
      2,
      'v0.10.3',
      new Map<string, string>([
        ['use', 'false'],
        ['driver-opts', 'image=moby/buildkit:master\nnetwork=host'],
        ['cache-binary', 'true'],
        ['cleanup', 'true'],
        ['keep-state', 'false']
      ]),
      [
        'create',
        '--name', 'builder-9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d',
        '--driver', 'docker-container',
        '--driver-opt', 'image=moby/buildkit:master',
        '--driver-opt', 'network=host',
        '--buildkitd-flags', '--allow-insecure-entitlement security.insecure --allow-insecure-entitlement network.host'
      ]
    ],
    [
      3,
      'v0.10.3',
      new Map<string, string>([
        ['driver', 'remote'],
        ['endpoint', 'tls://foo:1234'],
        ['use', 'true'],
        ['cache-binary', 'true'],
        ['cleanup', 'true'],
        ['keep-state', 'false']
      ]),
      [
        'create',
        '--name', 'builder-9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d',
        '--driver', 'remote',
        '--use',
        'tls://foo:1234'
      ]
    ],
    [
      4,
      'v0.10.3',
      new Map<string, string>([
        ['driver', 'remote'],
        ['platforms', 'linux/arm64,linux/arm/v7'],
        ['endpoint', 'tls://foo:1234'],
        ['use', 'true'],
        ['cache-binary', 'true'],
        ['cleanup', 'true'],
        ['keep-state', 'false']
      ]),
      [
        'create',
        '--name', 'builder-9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d',
        '--driver', 'remote',
        '--platform', 'linux/arm64,linux/arm/v7',
        '--use',
        'tls://foo:1234'
      ]
    ],
    [
      5,
      'v0.10.3',
      new Map<string, string>([
        ['use', 'false'],
        ['driver-opts', `"env.no_proxy=localhost,127.0.0.1,.mydomain"`],
        ['cache-binary', 'true'],
        ['cleanup', 'true'],
        ['keep-state', 'false'],
      ]),
      [
        'create',
        '--name', 'builder-9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d',
        '--driver', 'docker-container',
        '--driver-opt', '"env.no_proxy=localhost,127.0.0.1,.mydomain"',
        '--buildkitd-flags', '--allow-insecure-entitlement security.insecure --allow-insecure-entitlement network.host'
      ]
    ],
    [
      6,
      'v0.10.3',
      new Map<string, string>([
        ['use', 'false'],
        ['platforms', 'linux/amd64\n"linux/arm64,linux/arm/v7"'],
        ['cache-binary', 'true'],
        ['cleanup', 'true'],
        ['keep-state', 'false'],
      ]),
      [
        'create',
        '--name', 'builder-9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d',
        '--driver', 'docker-container',
        '--buildkitd-flags', '--allow-insecure-entitlement security.insecure --allow-insecure-entitlement network.host',
        '--platform', 'linux/amd64,linux/arm64,linux/arm/v7'
      ]
    ],
    [
      7,
      'v0.10.3',
      new Map<string, string>([
        ['use', 'false'],
        ['driver', 'unknown'],
        ['cache-binary', 'true'],
        ['cleanup', 'true'],
        ['keep-state', 'false'],
      ]),
      [
        'create',
        '--name', 'builder-9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d',
        '--driver', 'unknown',
      ]
    ],
    [
      8,
      'v0.10.3',
      new Map<string, string>([
        ['use', 'false'],
        ['buildkitd-config', path.join(fixturesDir, 'buildkitd.toml')],
        ['cache-binary', 'true'],
        ['cleanup', 'true'],
        ['keep-state', 'false'],
      ]),
      [
        'create',
        '--name', 'builder-9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d',
        '--driver', 'docker-container',
        '--buildkitd-flags', '--allow-insecure-entitlement security.insecure --allow-insecure-entitlement network.host',
        '--config', tmpName,
      ]
    ],
    [
      9,
      'v0.10.3',
      new Map<string, string>([
        ['use', 'false'],
        ['buildkitd-config-inline', 'debug = true'],
        ['cache-binary', 'true'],
        ['cleanup', 'true'],
        ['keep-state', 'false'],
      ]),
      [
        'create',
        '--name', 'builder-9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d',
        '--driver', 'docker-container',
        '--buildkitd-flags', '--allow-insecure-entitlement security.insecure --allow-insecure-entitlement network.host',
        '--config', tmpName,
      ]
    ],
    [
      10,
      'v0.10.3',
      new Map<string, string>([
        ['use', 'false'],
        ['driver', 'cloud'],
        ['buildkitd-flags', '--allow-insecure-entitlement network.host'],
        ['cache-binary', 'true'],
        ['cleanup', 'true'],
        ['keep-state', 'false'],
      ]),
      [
        'create',
        '--name', 'builder-9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d',
        '--driver', 'cloud',
        '--buildkitd-flags', '--allow-insecure-entitlement network.host',
      ]
    ],
    [
      11,
      'v0.10.3',
      new Map<string, string>([
        ['use', 'true'],
        ['cleanup', 'true'],
        ['cache-binary', 'true'],
        ['keep-state', 'false'],
        ['name', 'test-builder-name'],
      ]),
      [
        'create',
        '--name', 'test-builder-name',
        '--driver', 'docker-container',
        '--buildkitd-flags', '--allow-insecure-entitlement security.insecure --allow-insecure-entitlement network.host',
        '--use'
      ]
    ],
    [
      12,
      'v0.10.3',
      new Map<string, string>([
        ['use', 'true'],
        ['cleanup', 'true'],
        ['cache-binary', 'true'],
        ['keep-state', 'true'],
        ['name', 'test-builder-name'],
      ]),
      [
        'create',
        '--name', 'test-builder-name',
        '--driver', 'docker-container',
        '--buildkitd-flags', '--allow-insecure-entitlement security.insecure --allow-insecure-entitlement network.host',
        '--use',
      ]
    ],
  ])(
    '[%d] given buildx %o and %o as inputs, returns %o',
    async (num: number, buildxVersion: string, inputs: Map<string, string>, expected: Array<string>) => {
      inputs.forEach((value: string, name: string) => {
        setInput(name, value);
      });
      const toolkit = new Toolkit();
      vi.spyOn(Buildx.prototype, 'version').mockImplementation(async (): Promise<string> => {
        return buildxVersion;
      });
      const inp = await context.getInputs();
      const res = await context.getCreateArgs(inp, toolkit);
      expect(res).toEqual(expected);
    }
  );
});

describe('getAppendArgs', () => {
  beforeEach(() => {
    process.env = Object.keys(process.env).reduce((object, key) => {
      if (!key.startsWith('INPUT_')) {
        object[key] = process.env[key];
      }
      return object;
    }, {});
  });

  // prettier-ignore
  test.each([
    [
      0,
      'v0.10.3',
      new Map<string, string>([
        ['use', 'true'],
        ['cache-binary', 'true'],
        ['cleanup', 'true'],
        ['keep-state', 'false']
      ]),
      {
        "name": "aws_graviton2",
        "endpoint": "ssh://me@graviton2",
        "driver-opts": [
          "image=moby/buildkit:latest"
        ],
        "buildkitd-flags": "--allow-insecure-entitlement security.insecure --allow-insecure-entitlement network.host",
        "platforms": "linux/arm64"
      },
      [
        'create',
        '--name', 'builder-9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d',
        '--append',
        '--node', 'aws_graviton2',
        '--driver-opt', 'image=moby/buildkit:latest',
        '--buildkitd-flags', '--allow-insecure-entitlement security.insecure --allow-insecure-entitlement network.host',
        '--platform', 'linux/arm64',
        'ssh://me@graviton2'
      ]
    ]
  ])(
    '[%d] given buildx %o and %o as inputs, returns %o',
    async (num: number, buildxVersion: string, inputs: Map<string, string>, node: Node, expected: Array<string>) => {
      inputs.forEach((value: string, name: string) => {
        setInput(name, value);
      });
      const toolkit = new Toolkit();
      vi.spyOn(Buildx.prototype, 'version').mockImplementation(async (): Promise<string> => {
        return buildxVersion;
      });
      const inp = await context.getInputs();
      const res = await context.getAppendArgs(inp, node, toolkit);
      expect(res).toEqual(expected);
    }
  );
});

describe('getVersion', () => {
  beforeEach(() => {
    process.env = Object.keys(process.env).reduce((object, key) => {
      if (!key.startsWith('INPUT_')) {
        object[key] = process.env[key];
      }
      return object;
    }, {});
  });

  // prettier-ignore
  test.each([
    [
      0,
      new Map<string, string>([
        // defaults
        ['use', 'true'],
        ['cache-binary', 'true'],
        ['cleanup', 'true'],
        ['keep-state', 'false']
      ]),
      ''
    ],
    [
      1,
      new Map<string, string>([
        ['version', 'latest'],
        // defaults
        ['use', 'true'],
        ['cache-binary', 'true'],
        ['cleanup', 'true'],
        ['keep-state', 'false']
      ]),
      'latest'
    ],
    [
      2,
      new Map<string, string>([
        ['version', 'edge'],
        // defaults
        ['use', 'true'],
        ['cache-binary', 'true'],
        ['cleanup', 'true'],
        ['keep-state', 'false']
      ]),
      'edge'
    ],
    [
      3,
      new Map<string, string>([
        ['version', 'v0.19.2'],
        // defaults
        ['use', 'true'],
        ['cache-binary', 'true'],
        ['cleanup', 'true'],
        ['keep-state', 'false']
      ]),
      'v0.19.2'
    ],
    [
      4,
      new Map<string, string>([
        ['version', 'latest'],
        ['driver', 'cloud'],
        // defaults
        ['use', 'true'],
        ['cache-binary', 'true'],
        ['cleanup', 'true'],
        ['keep-state', 'false']
      ]),
      'cloud:latest'
    ],
    [
      5,
      new Map<string, string>([
        ['version', 'edge'],
        ['driver', 'cloud'],
        // defaults
        ['use', 'true'],
        ['cache-binary', 'true'],
        ['cleanup', 'true'],
        ['keep-state', 'false']
      ]),
      'cloud:edge'
    ],
    [
      6,
      new Map<string, string>([
        ['driver', 'cloud'],
        // defaults
        ['use', 'true'],
        ['cache-binary', 'true'],
        ['cleanup', 'true'],
        ['keep-state', 'false']
      ]),
      'cloud:latest'
    ],
    [
      7,
      new Map<string, string>([
        ['version', 'cloud:v0.11.2-desktop.2'],
        ['driver', 'cloud'],
        // defaults
        ['use', 'true'],
        ['cache-binary', 'true'],
        ['cleanup', 'true'],
        ['keep-state', 'false']
      ]),
      'cloud:v0.11.2-desktop.2'
    ],
    [
      8,
      new Map<string, string>([
        ['version', 'cloud:v0.11.2-desktop.2'],
        // defaults
        ['use', 'true'],
        ['cache-binary', 'true'],
        ['cleanup', 'true'],
        ['keep-state', 'false']
      ]),
      'cloud:v0.11.2-desktop.2'
    ],
  ])(
    '[%d] given %o as inputs, returns version %o',
    async (num: number, inputs: Map<string, string>, expected: string) => {
      inputs.forEach((value: string, name: string) => {
        setInput(name, value);
      });
      const inp = await context.getInputs();
      expect(context.getVersion(inp)).toEqual(expected);
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

const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'docker-setup-buildx-action-'));

process.env = Object.assign({}, process.env, {
  TEMP: tmpDir,
  GITHUB_REPOSITORY: 'docker/setup-buildx-action',
  RUNNER_TEMP: path.join(tmpDir, 'runner-temp'),
  RUNNER_TOOL_CACHE: path.join(tmpDir, 'runner-tool-cache')
});

```


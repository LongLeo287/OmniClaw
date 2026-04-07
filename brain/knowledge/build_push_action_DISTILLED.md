---
id: build-push-action
type: knowledge
owner: OA_Triage
---
# build-push-action
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "docker-build-push",
  "description": "Build and push Docker images",
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
    "url": "git+https://github.com/docker/build-push-action.git"
  },
  "keywords": [
    "actions",
    "docker",
    "build",
    "push"
  ],
  "author": "Docker Inc.",
  "license": "Apache-2.0",
  "packageManager": "yarn@4.9.2",
  "dependencies": {
    "@actions/core": "^3.0.0",
    "@docker/actions-toolkit": "0.79.0",
    "handlebars": "^4.7.9"
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
[![GitHub release](https://img.shields.io/github/release/docker/build-push-action.svg?style=flat-square)](https://github.com/docker/build-push-action/releases/latest)
[![GitHub marketplace](https://img.shields.io/badge/marketplace-build--and--push--docker--images-blue?logo=github&style=flat-square)](https://github.com/marketplace/actions/build-and-push-docker-images)
[![CI workflow](https://img.shields.io/github/actions/workflow/status/docker/build-push-action/ci.yml?branch=master&label=ci&logo=github&style=flat-square)](https://github.com/docker/build-push-action/actions?workflow=ci)
[![Test workflow](https://img.shields.io/github/actions/workflow/status/docker/build-push-action/test.yml?branch=master&label=test&logo=github&style=flat-square)](https://github.com/docker/build-push-action/actions?workflow=test)
[![Codecov](https://img.shields.io/codecov/c/github/docker/build-push-action?logo=codecov&style=flat-square)](https://codecov.io/gh/docker/build-push-action)

## About

GitHub Action to build and push Docker images with [Buildx](https://github.com/docker/buildx)
with full support of the features provided by [Moby BuildKit](https://github.com/moby/buildkit)
builder toolkit. This includes multi-platform build, secrets, remote cache, etc.
and different builder deployment/namespacing options.

![Screenshot](.github/build-push-action.png)

___

* [Usage](#usage)
  * [Git context](#git-context)
  * [Path context](#path-context)
* [Examples](#examples)
* [Summaries](#summaries)
* [Customizing](#customizing)
  * [inputs](#inputs)
  * [outputs](#outputs)
  * [environment variables](#environment-variables)
* [Troubleshooting](#troubleshooting)
* [Contributing](#contributing)

## Usage

In the examples below we are also using 3 other actions:

* [`setup-buildx`](https://github.com/docker/setup-buildx-action) action will
  create and boot a builder using by default the [`docker-container` driver](https://docs.docker.com/build/building/drivers/docker-container/).
  This is **not required but recommended** using it to be able to build
  multi-platform images, export cache, etc.
* [`setup-qemu`](https://github.com/docker/setup-qemu-action) action can be
  useful if you want to add emulation support with QEMU to be able to build
  against more platforms. 
* [`login`](https://github.com/docker/login-action) action will take care to
  log in against a Docker registry.

### Git context

By default, this action uses the [Git context](https://docs.docker.com/engine/reference/commandline/build/#git-repositories),
so you don't need to use the [`actions/checkout`](https://github.com/actions/checkout/)
action to check out the repository as this will be done directly by [BuildKit](https://github.com/moby/buildkit).

The git reference will be based on the [event that triggered your workflow](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows)
and will result in the following context: `https://github.com/<owner>/<repo>.git#<ref>`.

```yaml
name: ci

on:
  push:

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to Docker Hub
        uses: docker/login-action@v4
        with:
          username: ${{ vars.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      -
        name: Set up QEMU
        uses: docker/setup-qemu-action@v4
      -
        name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v4
      -
        name: Build and push
        uses: docker/build-push-action@v7
        with:
          push: true
          tags: user/app:latest
```

Be careful because **any file mutation in the steps that precede the build step
will be ignored, including processing of the `.dockerignore` file** since
the context is based on the Git reference. However, you can use the
[Path context](#path-context) using the [`context` input](#inputs) alongside
the [`actions/checkout`](https://github.com/actions/checkout/) action to remove
this restriction.

Default Git context can also be provided using the [Handlebars template](https://handlebarsjs.com/guide/)
expression `{{defaultContext}}`. Here we can use it to provide a subdirectory
to the default Git context:

```yaml
      -
        name: Build and push
        uses: docker/build-push-action@v7
        with:
          context: "{{defaultContext}}:mysubdir"
          push: true
          tags: user/app:latest
```

Building from the current repository automatically uses the [GitHub Token](https://docs.github.com/en/actions/security-guides/automatic-token-authentication),
so it does not need to be passed. If you want to authenticate against another
private repository, you have to use a [secret](https://docs.docker.com/build/ci/github-actions/secrets)
named `GIT_AUTH_TOKEN` to be able to authenticate against it with Buildx:

```yaml
      -
        name: Build and push
        uses: docker/build-push-action@v7
        with:
          push: true
          tags: user/app:latest
          secrets: |
            GIT_AUTH_TOKEN=${{ secrets.MYTOKEN }}
```

### Path context

```yaml
name: ci

on:
  push:

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      -
        name: Checkout
        uses: actions/checkout@v6
      -
        name: Login to Docker Hub
        uses: docker/login-action@v4
        with:
          username: ${{ vars.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      -
        name: Set up QEMU
        uses: docker/setup-qemu-action@v4
      -
        name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v4
      -
        name: Build and push
        uses: docker/build-push-action@v7
        with:
          context: .
          push: true
          tags: user/app:latest
```

## Examples

* [Multi-platform image](https://docs.docker.com/build/ci/github-actions/multi-platform/)
* [Secrets](https://docs.docker.com/build/ci/github-actions/secrets/)
* [Push to multi-registries](https://docs.docker.com/build/ci/github-actions/push-multi-registries/)
* [Manage tags and labels](https://docs.docker.com/build/ci/github-actions/manage-tags-labels/)
* [Cache management](https://docs.docker.com/build/ci/github-actions/cache/)
* [Export to Docker](https://docs.docker.com/build/ci/github-actions/export-docker/)
* [Test before push](https://docs.docker.com/build/ci/github-actions/test-before-push/)
* [Validating build configuration](https://docs.docker.com/build/ci/github-actions/checks/)
* [Local registry](https://docs.docker.com/build/ci/github-actions/local-registry/)
* [Share built image between jobs](https://docs.docker.com/build/ci/github-actions/share-image-jobs/)
* [Named contexts](https://docs.docker.com/build/ci/github-actions/named-contexts/)
* [Copy image between registries](https://docs.docker.com/build/ci/github-actions/copy-image-registries/)
* [Update Docker Hub repo description](https://docs.docker.com/build/ci/github-actions/update-dockerhub-desc/)
* [SBOM and provenance attestations](https://docs.docker.com/build/ci/github-actions/attestations/)
* [Annotations](https://docs.docker.com/build/ci/github-actions/annotations/)
* [Reproducible builds](https://docs.docker.com/build/ci/github-actions/reproducible-builds/)

## Summaries

This action generates a [job summary](https://github.blog/2022-05-09-supercharging-github-actions-with-job-summaries/)
that provides a detailed overview of the build execution. The summary shows an
overview of all the steps executed during the build, including the build inputs
and eventual errors.

![build-push-action job summary](./.github/build-push-summary.png)

The summary also includes a link for downloading the build record with
additional details about the build, including build stats, logs, outputs, and
more. The build record can be imported to Docker Desktop for inspecting the
build in greater detail.

> [!WARNING]
>
> If you're using the [`actions/download-artifact`](https://github.com/actions/download-artifact)
> action in your workflow, you need to ignore the build record artifacts
> if `name` and `pattern` inputs are not specified ([defaults to download all artifacts](https://github.com/actions/download-artifact?tab=readme-ov-file#download-all-artifacts) of the workflow),
> otherwise the action will fail:
> ```yaml
> - uses: actions/download-artifact@v4
>   with:
>     pattern: "!*.dockerbuild"
> ```
> More info: https://github.com/actions/toolkit/pull/1874

Summaries are enabled by default, but can be disabled with the
`DOCKER_BUILD_SUMMARY` [environment variable](#environment-variables).

For more information about summaries, refer to the
[documentation](https://docs.docker.com/go/build-summary/).

## Customizing

### inputs

The following inputs can be used as `step.with` keys:

> `List` type is a newline-delimited string
> ```yaml
> cache-from: |
>   user/app:cache
>   type=local,src=path/to/dir
> ```

> `CSV` type is a comma-delimited string
> ```yaml
> tags: name/app:latest,name/app:1.0.0
> ```

| Name               | Type        | Description                                                                                                                                                                       |
|--------------------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `add-hosts`        | List/CSV    | List of [customs host-to-IP mapping](https://docs.docker.com/engine/reference/commandline/build/#add-entries-to-container-hosts-file---add-host) (e.g., `docker:10.180.0.1`)      |
| `allow`            | List/CSV    | List of [extra privileged entitlement](https://docs.docker.com/engine/reference/commandline/buildx_build/#allow) (e.g., `network.host,security.insecure`)                         |
| `annotations`      | List        | List of annotation to set to the image                                                                                                                                            |
| `attests`          | List        | List of [attestation](https://docs.docker.com/build/attestations/) parameters (e.g., `type=sbom,generator=image`)                                                                 | 
| `builder`          | String      | Builder instance (see [setup-buildx](https://github.com/docker/setup-buildx-action) action)                                                                                       |
| `build-args`       | List        | List of [build-time variables](https://docs.docker.com/engine/reference/commandline/buildx_build/#build-arg)                                                                      |
| `build-contexts`   | List        | List of additional [build contexts](https://docs.docker.com/engine/reference/commandline/buildx_build/#build-context) (e.g., `name=path`)                                         |
| `cache-from`       | List        | List of [external cache sources](https://docs.docker.com/engine/reference/commandline/buildx_build/#cache-from) (e.g., `type=local,src=path/to/dir`)                              |
| `cache-to`         | List        | List of [cache export destinations](https://docs.docker.com/engine/reference/commandline/buildx_build/#cache-to) (e.g., `type=local,dest=path/to/dir`)                            |
| `call`             | String      | Set [method for evaluating build](https://docs.docker.com/reference/cli/docker/buildx/build/#call) (e.g., `check`)                                                                |
| `cgroup-parent`    | String      | Optional [parent cgroup](https://docs.docker.com/engine/reference/commandline/build/#use-a-custom-parent-cgroup---cgroup-parent) for the container used in the build              |
| `context`          | String      | Build's context is the set of files located in the specified [`PATH` or `URL`](https://docs.docker.com/engine/reference/commandline/build/) (default [Git context](#git-context)) |
| `file`             | String      | Path to the Dockerfile. (default `{context}/Dockerfile`)                                                                                                                          |
| `labels`           | List        | List of metadata for an image                                                                                                                                                     |
| `load`             | Bool        | [Load](https://docs.docker.com/engine/reference/commandline/buildx_build/#load) is a shorthand for `--output=type=docker` (default `false`)                                       |
| `network`          | String      | Set the networking mode for the `RUN` instructions during build                                                                                                                   |
| `no-cache`         | Bool        | Do not use cache when building the image (default `false`)                                                                                                                        |
| `no-cache-filters` | List/CSV    | Do not cache specified stages                                                                                                                                                     |
| `outputs`          | List        | List of [output destinations](https://docs.docker.com/engine/reference/commandline/buildx_build/#output) (format: `type=local,dest=path`)                                         |
| `platforms`        | List/CSV    | List of [target platforms](https://docs.docker.com/engine/reference/commandline/buildx_build/#platform) for build                                                                 |
| `provenance`       | Bool/String | Generate [provenance](https://docs.docker.com/build/attestations/slsa-provenance/) attestation for the build (shorthand for `--attest=type=provenance`)                           |
| `pull`             | Bool        | Always attempt to pull all referenced images (default `false`)                                                                                                                    |
| `push`             | Bool        | [Push](https://docs.docker.com/engine/reference/commandline/buildx_build/#push) is a shorthand for `--output=type=registry` (default `false`)                                     |
| `sbom`             | Bool/String | Generate [SBOM](https://docs.docker.com/build/attestations/sbom/) attestation for the build (shorthand for `--attest=type=sbom`)                                                  |
| `secrets`          | List        | List of [secrets](https://docs.docker.com/engine/reference/commandline/buildx_build/#secret) to expose to the build (e.g., `key=string`, `GIT_AUTH_TOKEN=mytoken`)                |
| `secret-envs`      | List/CSV    | List of [secret env vars](https://docs.docker.com/engine/reference/commandline/buildx_build/#secret) to expose to the buil
... [TRUNCATED]
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

### File: src_DISTILLED.md
```md
---
id: src
type: distilled_knowledge
---
# src

## SWALLOW ENGINE DISTILLATION

### File: context.ts
```ts
import * as core from '@actions/core';
import * as handlebars from 'handlebars';

import {Build} from '@docker/actions-toolkit/lib/buildx/build.js';
import {Context} from '@docker/actions-toolkit/lib/context.js';
import {GitHub} from '@docker/actions-toolkit/lib/github/github.js';
import {Toolkit} from '@docker/actions-toolkit/lib/toolkit.js';
import {Util} from '@docker/actions-toolkit/lib/util.js';

export interface Inputs {
  'add-hosts': string[];
  allow: string[];
  annotations: string[];
  attests: string[];
  'build-args': string[];
  'build-contexts': string[];
  builder: string;
  'cache-from': string[];
  'cache-to': string[];
  call: string;
  'cgroup-parent': string;
  context: string;
  file: string;
  labels: string[];
  load: boolean;
  network: string;
  'no-cache': boolean;
  'no-cache-filters': string[];
  outputs: string[];
  platforms: string[];
  provenance: string;
  pull: boolean;
  push: boolean;
  sbom: string;
  secrets: string[];
  'secret-envs': string[];
  'secret-files': string[];
  'shm-size': string;
  ssh: string[];
  tags: string[];
  target: string;
  ulimit: string[];
  'github-token': string;
}

export async function getInputs(): Promise<Inputs> {
  return {
    'add-hosts': Util.getInputList('add-hosts'),
    allow: Util.getInputList('allow'),
    annotations: Util.getInputList('annotations', {ignoreComma: true}),
    attests: Util.getInputList('attests', {ignoreComma: true}),
    'build-args': Util.getInputList('build-args', {ignoreComma: true}),
    'build-contexts': Util.getInputList('build-contexts', {ignoreComma: true}),
    builder: core.getInput('builder'),
    'cache-from': Util.getInputList('cache-from', {ignoreComma: true}),
    'cache-to': Util.getInputList('cache-to', {ignoreComma: true}),
    call: core.getInput('call'),
    'cgroup-parent': core.getInput('cgroup-parent'),
    context: core.getInput('context') || Context.gitContext(),
    file: core.getInput('file'),
    labels: Util.getInputList('labels', {ignoreComma: true}),
    load: core.getBooleanInput('load'),
    network: core.getInput('network'),
    'no-cache': core.getBooleanInput('no-cache'),
    'no-cache-filters': Util.getInputList('no-cache-filters'),
    outputs: Util.getInputList('outputs', {ignoreComma: true, quote: false}),
    platforms: Util.getInputList('platforms'),
    provenance: Build.getProvenanceInput('provenance'),
    pull: core.getBooleanInput('pull'),
    push: core.getBooleanInput('push'),
    sbom: core.getInput('sbom'),
    secrets: Util.getInputList('secrets', {ignoreComma: true}),
    'secret-envs': Util.getInputList('secret-envs'),
    'secret-files': Util.getInputList('secret-files', {ignoreComma: true}),
    'shm-size': core.getInput('shm-size'),
    ssh: Util.getInputList('ssh'),
    tags: Util.getInputList('tags'),
    target: core.getInput('target'),
    ulimit: Util.getInputList('ulimit', {ignoreComma: true}),
    'github-token': core.getInput('github-token')
  };
}

export async function getArgs(inputs: Inputs, toolkit: Toolkit): Promise<Array<string>> {
  const context = handlebars.compile(inputs.context)({
    defaultContext: Context.gitContext()
  });
  // prettier-ignore
  return [
    ...await getBuildArgs(inputs, context, toolkit),
    ...await getCommonArgs(inputs, toolkit),
    context
  ];
}

async function getBuildArgs(inputs: Inputs, context: string, toolkit: Toolkit): Promise<Array<string>> {
  const args: Array<string> = ['build'];
  await Util.asyncForEach(inputs['add-hosts'], async addHost => {
    args.push('--add-host', addHost);
  });
  await Util.asyncForEach(inputs.allow, async allow => {
    args.push('--allow', allow);
  });
  if (await toolkit.buildx.versionSatisfies('>=0.12.0')) {
    await Util.asyncForEach(inputs.annotations, async annotation => {
      args.push('--annotation', annotation);
    });
  } else if (inputs.annotations.length > 0) {
    core.warning("Annotations are only supported by buildx >= 0.12.0; the input 'annotations' is ignored.");
  }
  await Util.asyncForEach(inputs['build-args'], async buildArg => {
    args.push('--build-arg', buildArg);
  });
  if (await toolkit.buildx.versionSatisfies('>=0.8.0')) {
    await Util.asyncForEach(inputs['build-contexts'], async buildContext => {
      args.push(
        '--build-context',
        handlebars.compile(buildContext)({
          defaultContext: Context.gitContext()
        })
      );
    });
  } else if (inputs['build-contexts'].length > 0) {
    core.warning("Build contexts are only supported by buildx >= 0.8.0; the input 'build-contexts' is ignored.");
  }
  await Util.asyncForEach(inputs['cache-from'], async cacheFrom => {
    args.push('--cache-from', cacheFrom);
  });
  await Util.asyncForEach(inputs['cache-to'], async cacheTo => {
    args.push('--cache-to', cacheTo);
  });
  if (inputs.call) {
    if (!(await toolkit.buildx.versionSatisfies('>=0.15.0'))) {
      throw new Error(`Buildx >= 0.15.0 is required to use the call flag.`);
    }
    args.push('--call', inputs.call);
  }
  if (inputs['cgroup-parent']) {
    args.push('--cgroup-parent', inputs['cgroup-parent']);
  }
  await Util.asyncForEach(inputs['secret-envs'], async secretEnv => {
    try {
      args.push('--secret', Build.resolveSecretEnv(secretEnv));
    } catch (err) {
      core.warning(err.message);
    }
  });
  if (inputs.file) {
    args.push('--file', inputs.file);
  }
  if (!Build.hasLocalExporter(inputs.outputs) && !Build.hasTarExporter(inputs.outputs) && (inputs.platforms.length == 0 || (await toolkit.buildx.versionSatisfies('>=0.4.2')))) {
    args.push('--iidfile', toolkit.buildxBuild.getImageIDFilePath());
  }
  await Util.asyncForEach(inputs.labels, async label => {
    args.push('--label', label);
  });
  await Util.asyncForEach(inputs['no-cache-filters'], async noCacheFilter => {
    args.push('--no-cache-filter', noCacheFilter);
  });
  await Util.asyncForEach(inputs.outputs, async output => {
    args.push('--output', output);
  });
  if (inputs.platforms.length > 0) {
    args.push('--platform', inputs.platforms.join(','));
  }
  if (await toolkit.buildx.versionSatisfies('>=0.10.0')) {
    args.push(...(await getAttestArgs(inputs, toolkit)));
  } else {
    core.warning("Attestations are only supported by buildx >= 0.10.0; the inputs 'attests', 'provenance' and 'sbom' are ignored.");
  }
  await Util.asyncForEach(inputs.secrets, async secret => {
    try {
      args.push('--secret', Build.resolveSecretString(secret));
    } catch (err) {
      core.warning(err.message);
    }
  });
  await Util.asyncForEach(inputs['secret-files'], async secretFile => {
    try {
      args.push('--secret', Build.resolveSecretFile(secretFile));
    } catch (err) {
      core.warning(err.message);
    }
  });
  if (inputs['github-token'] && !Build.hasGitAuthTokenSecret(inputs.secrets) && context.startsWith(Context.gitContext())) {
    args.push('--secret', Build.resolveSecretString(`GIT_AUTH_TOKEN.${new URL(GitHub.serverURL).host.trimEnd()}=${inputs['github-token']}`));
  }
  if (inputs['shm-size']) {
    args.push('--shm-size', inputs['shm-size']);
  }
  await Util.asyncForEach(inputs.ssh, async ssh => {
    args.push('--ssh', ssh);
  });
  await Util.asyncForEach(inputs.tags, async tag => {
    args.push('--tag', tag);
  });
  if (inputs.target) {
    args.push('--target', inputs.target);
  }
  await Util.asyncForEach(inputs.ulimit, async ulimit => {
    args.push('--ulimit', ulimit);
  });
  return args;
}

async function getCommonArgs(inputs: Inputs, toolkit: Toolkit): Promise<Array<string>> {
  const args: Array<string> = [];
  if (inputs.builder) {
    args.push('--builder', inputs.builder);
  }
  if (inputs.load) {
    args.push('--load');
  }
  if (await toolkit.buildx.versionSatisfies('>=0.6.0')) {
    args.push('--metadata-file', toolkit.buildxBuild.getMetadataFilePath());
  }
  if (inputs.network) {
    args.push('--network', inputs.network);
  }
  if (inputs['no-cache']) {
    args.push('--no-cache');
  }
  if (inputs.pull) {
    args.push('--pull');
  }
  if (inputs.push) {
    args.push('--push');
  }
  return args;
}

async function getAttestArgs(inputs: Inputs, toolkit: Toolkit): Promise<Array<string>> {
  const args: Array<string> = [];

  // check if provenance attestation is set in attests input
  let hasAttestProvenance = false;
  await Util.asyncForEach(inputs.attests, async (attest: string) => {
    if (Build.hasAttestationType('provenance', attest)) {
      hasAttestProvenance = true;
    }
  });

  let provenanceSet = false;
  let sbomSet = false;
  if (inputs.provenance) {
    args.push('--attest', Build.resolveAttestationAttrs(`type=provenance,${inputs.provenance}`));
    provenanceSet = true;
  } else if (!hasAttestProvenance && !noDefaultAttestations() && (await toolkit.buildkit.versionSatisfies(inputs.builder, '>=0.11.0')) && !Build.hasDockerExporter(inputs.outputs, inputs.load)) {
    // if provenance not specified in provenance or attests inputs and BuildKit
    // version compatible for attestation, set default provenance. Also needs
    // to make sure user doesn't want to explicitly load the image to docker.
    if (GitHub.context.payload.repository?.private ?? false) {
      // if this is a private repository, we set the default provenance
      // attributes being set in buildx: https://github.com/docker/buildx/blob/fb27e3f919dcbf614d7126b10c2bc2d0b1927eb6/build/build.go#L603
      args.push('--attest', `type=provenance,${Build.resolveProvenanceAttrs(`mode=min,inline-only=true`)}`);
    } else {
      // for a public repository, we set max provenance mode.
      args.push('--attest', `type=provenance,${Build.resolveProvenanceAttrs(`mode=max`)}`);
    }
  }
  if (inputs.sbom) {
    args.push('--attest', Build.resolveAttestationAttrs(`type=sbom,${inputs.sbom}`));
    sbomSet = true;
  }

  // set attests but check if provenance or sbom types already set as
  // provenance and sbom inputs take precedence over attests input.
  await Util.asyncForEach(inputs.attests, async (attest: string) => {
    if (!Build.hasAttestationType('provenance', attest) && !Build.hasAttestationType('sbom', attest)) {
      args.push('--attest', Build.resolveAttestationAttrs(attest));
    } else if (!provenanceSet && Build.hasAttestationType('provenance', attest)) {
      args.push('--attest', Build.resolveProvenanceAttrs(attest));
    } else if (!sbomSet && Build.hasAttestationType('sbom', attest)) {
      args.push('--attest', attest);
    }
  });

  return args;
}

function noDefaultAttestations(): boolean {
  if (process.env.BUILDX_NO_DEFAULT_ATTESTATIONS) {
    return Util.parseBool(process.env.BUILDX_NO_DEFAULT_ATTESTATIONS);
  }
  return false;
}

```

### File: main.ts
```ts
import * as fs from 'fs';
import * as path from 'path';
import * as core from '@actions/core';
import * as actionsToolkit from '@docker/actions-toolkit';

import {Buildx} from '@docker/actions-toolkit/lib/buildx/buildx.js';
import {History as BuildxHistory} from '@docker/actions-toolkit/lib/buildx/history.js';
import {Context} from '@docker/actions-toolkit/lib/context.js';
import {Docker} from '@docker/actions-toolkit/lib/docker/docker.js';
import {Exec} from '@docker/actions-toolkit/lib/exec.js';
import {GitHub} from '@docker/actions-toolkit/lib/github/github.js';
import {GitHubArtifact} from '@docker/actions-toolkit/lib/github/artifact.js';
import {GitHubSummary} from '@docker/actions-toolkit/lib/github/summary.js';
import {Toolkit} from '@docker/actions-toolkit/lib/toolkit.js';
import {Util} from '@docker/actions-toolkit/lib/util.js';

import {BuilderInfo} from '@docker/actions-toolkit/lib/types/buildx/builder.js';
import {ConfigFile} from '@docker/actions-toolkit/lib/types/docker/docker.js';
import {UploadResponse as UploadArtifactResponse} from '@docker/actions-toolkit/lib/types/github/artifact.js';

import * as context from './context.js';
import * as stateHelper from './state-helper.js';

actionsToolkit.run(
  // main
  async () => {
    const startedTime = new Date();
    const inputs: context.Inputs = await context.getInputs();
    stateHelper.setSummaryInputs(inputs);
    core.debug(`inputs: ${JSON.stringify(inputs)}`);

    const toolkit = new Toolkit();

    await core.group(`GitHub Actions runtime token ACs`, async () => {
      try {
        await GitHub.printActionsRuntimeTokenACs();
      } catch (e) {
        core.warning(e.message);
      }
    });

    await core.group(`Docker info`, async () => {
      try {
        await Docker.printVersion();
        await Docker.printInfo();
      } catch (e) {
        core.info(e.message);
      }
    });

    await core.group(`Proxy configuration`, async () => {
      let dockerConfig: ConfigFile | undefined;
      let dockerConfigMalformed = false;
      try {
        dockerConfig = await Docker.configFile();
      } catch (e) {
        dockerConfigMalformed = true;
        core.warning(`Unable to parse config file ${path.join(Docker.configDir, 'config.json')}: ${e}`);
      }
      if (dockerConfig && dockerConfig.proxies) {
        for (const host in dockerConfig.proxies) {
          let prefix = '';
          if (Object.keys(dockerConfig.proxies).length > 1) {
            prefix = '  ';
            core.info(host);
          }
          for (const key in dockerConfig.proxies[host]) {
            core.info(`${prefix}${key}: ${dockerConfig.proxies[host][key]}`);
          }
        }
      } else if (!dockerConfigMalformed) {
        core.info('No proxy configuration found');
      }
    });

    if (!(await toolkit.buildx.isAvailable())) {
      core.setFailed(`Docker buildx is required. See https://github.com/docker/setup-buildx-action to set up buildx.`);
      return;
    }

    stateHelper.setTmpDir(Context.tmpDir());

    await core.group(`Buildx version`, async () => {
      await toolkit.buildx.printVersion();
    });

    let builder: BuilderInfo;
    await core.group(`Builder info`, async () => {
      builder = await toolkit.builder.inspect(inputs.builder);
      stateHelper.setBuilderDriver(builder.driver ?? '');
      stateHelper.setBuilderEndpoint(builder.nodes?.[0]?.endpoint ?? '');
      core.info(JSON.stringify(builder, null, 2));
    });

    const args: string[] = await context.getArgs(inputs, toolkit);
    core.debug(`context.getArgs: ${JSON.stringify(args)}`);

    const buildCmd = await toolkit.buildx.getCommand(args);
    core.debug(`buildCmd.command: ${buildCmd.command}`);
    core.debug(`buildCmd.args: ${JSON.stringify(buildCmd.args)}`);

    let err: Error | undefined;
    await Exec.getExecOutput(buildCmd.command, buildCmd.args, {
      ignoreReturnCode: true,
      env: Object.assign({}, process.env, {
        BUILDX_METADATA_WARNINGS: 'true'
      }) as {
        [key: string]: string;
      }
    }).then(res => {
      if (res.exitCode != 0) {
        if (inputs.call && inputs.call === 'check' && res.stdout.length > 0)
... [TRUNCATED]
```

### File: TROUBLESHOOTING.md
```md
# Troubleshooting

* [Cannot push to a registry](#cannot-push-to-a-registry)
* [`repository name must be lowercase`](#repository-name-must-be-lowercase)

## Cannot push to a registry

While pushing to a registry, you may encounter these kinds of issues:

* `failed commit on ref "layer-sha256:...": invalid content digest in response: invalid checksum digest format`
* `failed commit on ref "layer-sha256:...": no response`
* `failed commit on ref "manifest-sha256:...": unexpected status: 400 Bad Request`
* `failed commit on ref "manifest-sha256:...": unexpected status: 401 Unauthorized`
* `unexpected response: 401 Unauthorized`

These issues are not directly related to this action but are rather linked to
[Buildx](https://github.com/docker/buildx), [BuildKit](https://github.com/moby/buildkit),
[containerd](https://github.com/containerd/containerd) or the registry on which
you're pushing your image. The quality of error message depends on the registry
and are usually not very informative.

To help you solve this, you have to [enable debugging in the setup-buildx](https://github.com/docker/setup-buildx-action#buildkit-container-logs)
action step and attach BuildKit container logs to your issue.

## `repository name must be lowercase`

You may encounter this issue if you're using `github.repository` as a repo slug
in your tag:

```
#6 exporting to image
#6 exporting layers
#6 exporting layers 1.2s done
#6 exporting manifest sha256:b47f7dfb97b89ccd5de553af3c8cd94c4795884cbe5693e93946b1d95a7b1d12 0.0s done
#6 exporting config sha256:995e93fab8196893192f08a38deea6769dc4d98f86cf705eccc24ec96a3e271c 0.0s done
#6 ERROR: invalid reference format: repository name must be lowercase
------
 > exporting to image:
------
error: failed to solve: invalid reference format: repository name must be lowercase
```

or a cache reference:

```
#10 importing cache manifest from ghcr.io/My-Org/repo:main
#10 ERROR: invalid reference format: repository name must be lowercase
```

To fix this issue you can use our [metadata action](https://github.com/docker/metadata-action)
to generate sanitized tags:

```yaml
- name: Docker meta
  id: meta
  uses: docker/metadata-action@v6
  with:
    images: ghcr.io/${{ github.repository }}
    tags: latest

- name: Build and push
  uses: docker/build-push-action@v7
  with:
    push: true
    tags: ${{ steps.meta.outputs.tags }}
```

Or a dedicated step to sanitize the slug:

```yaml
- name: Sanitize repo slug
  uses: actions/github-script@v8
  id: repo_slug
  with:
    result-encoding: string
    script: return 'ghcr.io/${{ github.repository }}'.toLowerCase()

- name: Build and push
  uses: docker/build-push-action@v7
  with:
    push: true
    tags: ${{ steps.repo_slug.outputs.result }}:latest
```

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

1. [Fork](https://github.com/docker/build-push-action/fork) and clone the repository
2. Configure and install the dependencies: `yarn install`
3. Create a new branch: `git checkout -b my-branch-name`
4. Make your changes
5. Make sure the tests pass: `docker buildx bake test`
6. Format code and build javascript artifacts: `docker buildx bake pre-checkin`
7. Validate all code has correctly formatted and built: `docker buildx bake validate`
8. Push to your fork and [submit a pull request](https://github.com/docker/build-push-action/compare)
9. Pat your self on the back and wait for your pull request to be reviewed and merged.

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
import * as handlebars from 'handlebars';

import {Build} from '@docker/actions-toolkit/lib/buildx/build.js';
import {Context} from '@docker/actions-toolkit/lib/context.js';
import {GitHub} from '@docker/actions-toolkit/lib/github/github.js';
import {Toolkit} from '@docker/actions-toolkit/lib/toolkit.js';
import {Util} from '@docker/actions-toolkit/lib/util.js';

export interface Inputs {
  'add-hosts': string[];
  allow: string[];
  annotations: string[];
  attests: string[];
  'build-args': string[];
  'build-contexts': string[];
  builder: string;
  'cache-from': string[];
  'cache-to': string[];
  call: string;
  'cgroup-parent': string;
  context: string;
  file: string;
  labels: string[];
  load: boolean;
  network: string;
  'no-cache': boolean;
  'no-cache-filters': string[];
  outputs: string[];
  platforms: string[];
  provenance: string;
  pull: boolean;
  push: boolean;
  sbom: string;
  secrets: string[];
  'secret-envs': string[];
  'secret-files': string[];
  'shm-size': string;
  ssh: string[];
  tags: string[];
  target: string;
  ulimit: string[];
  'github-token': string;
}

export async function getInputs(): Promise<Inputs> {
  return {
    'add-hosts': Util.getInputList('add-hosts'),
    allow: Util.getInputList('allow'),
    annotations: Util.getInputList('annotations', {ignoreComma: true}),
    attests: Util.getInputList('attests', {ignoreComma: true}),
    'build-args': Util.getInputList('build-args', {ignoreComma: true}),
    'build-contexts': Util.getInputList('build-contexts', {ignoreComma: true}),
    builder: core.getInput('builder'),
    'cache-from': Util.getInputList('cache-from', {ignoreComma: true}),
    'cache-to': Util.getInputList('cache-to', {ignoreComma: true}),
    call: core.getInput('call'),
    'cgroup-parent': core.getInput('cgroup-parent'),
    context: core.getInput('context') || Context.gitContext(),
    file: core.getInput('file'),
    labels: Util.getInputList('labels', {ignoreComma: true}),
    load: core.getBooleanInput('load'),
    network: core.getInput('network'),
    'no-cache': core.getBooleanInput('no-cache'),
    'no-cache-filters': Util.getInputList('no-cache-filters'),
    outputs: Util.getInputList('outputs', {ignoreComma: true, quote: false}),
    platforms: Util.getInputList('platforms'),
    provenance: Build.getProvenanceInput('provenance'),
    pull: core.getBooleanInput('pull'),
    push: core.getBooleanInput('push'),
    sbom: core.getInput('sbom'),
    secrets: Util.getInputList('secrets', {ignoreComma: true}),
    'secret-envs': Util.getInputList('secret-envs'),
    'secret-files': Util.getInputList('secret-files', {ignoreComma: true}),
    'shm-size': core.getInput('shm-size'),
    ssh: Util.getInputList('ssh'),
    tags: Util.getInputList('tags'),
    target: core.getInput('target'),
    ulimit: Util.getInputList('ulimit', {ignoreComma: true}),
    'github-token': core.getInput('github-token')
  };
}

export async function getArgs(inputs: Inputs, toolkit: Toolkit): Promise<Array<string>> {
  const context = handlebars.compile(inputs.context)({
    defaultContext: Context.gitContext()
  });
  // prettier-ignore
  return [
    ...await getBuildArgs(inputs, context, toolkit),
    ...await getCommonArgs(inputs, toolkit),
    context
  ];
}

async function getBuildArgs(inputs: Inputs, context: string, toolkit: Toolkit): Promise<Array<string>> {
  const args: Array<string> = ['build'];
  await Util.asyncForEach(inputs['add-hosts'], async addHost => {
    args.push('--add-host', addHost);
  });
  await Util.asyncForEach(inputs.allow, async allow => {
    args.push('--allow', allow);
  });
  if (await toolkit.buildx.versionSatisfies('>=0.12.0')) {
    await Util.asyncForEach(inputs.annotations, async annotation => {
      args.push('--annotation', annotation);
    });
  } else if (inputs.annotations.length > 0) {
    core.warning("Annotations are only supported by buildx >= 0.12.0; the input 'annotations' is ignored.");
  }
  await Util.asyncForEach(inputs['build-args'], async buildArg => {
    args.push('--build-arg', buildArg);
  });
  if (await toolkit.buildx.versionSatisfies('>=0.8.0')) {
    await Util.asyncForEach(inputs['build-contexts'], async buildContext => {
      args.push(
        '--build-context',
        handlebars.compile(buildContext)({
          defaultContext: Context.gitContext()
        })
      );
    });
  } else if (inputs['build-contexts'].length > 0) {
    core.warning("Build contexts are only supported by buildx >= 0.8.0; the input 'build-contexts' is ignored.");
  }
  await Util.asyncForEach(inputs['cache-from'], async cacheFrom => {
    args.push('--cache-from', cacheFrom);
  });
  await Util.asyncForEach(inputs['cache-to'], async cacheTo => {
    args.push('--cache-to', cacheTo);
  });
  if (inputs.call) {
    if (!(await toolkit.buildx.versionSatisfies('>=0.15.0'))) {
      throw new Error(`Buildx >= 0.15.0 is required to use the call flag.`);
    }
    args.push('--call', inputs.call);
  }
  if (inputs['cgroup-parent']) {
    args.push('--cgroup-parent', inputs['cgroup-parent']);
  }
  await Util.asyncForEach(inputs['secret-envs'], async secretEnv => {
    try {
      args.push('--secret', Build.resolveSecretEnv(secretEnv));
    } catch (err) {
      core.warning(err.message);
    }
  });
  if (inputs.file) {
    args.push('--file', inputs.file);
  }
  if (!Build.hasLocalExporter(inputs.outputs) && !Build.hasTarExporter(inputs.outputs) && (inputs.platforms.length == 0 || (await toolkit.buildx.versionSatisfies('>=0.4.2')))) {
    args.push('--iidfile', toolkit.buildxBuild.getImageIDFilePath());
  }
  await Util.asyncForEach(inputs.labels, async label => {
    args.push('--label', label);
  });
  await Util.asyncForEach(inputs['no-cache-filters'], async noCacheFilter => {
    args.push('--no-cache-filter', noCacheFilter);
  });
  await Util.asyncForEach(inputs.outputs, async output => {
    args.push('--output', output);
  });
  if (inputs.platforms.length > 0) {
    args.push('--platform', inputs.platforms.join(','));
  }
  if (await toolkit.buildx.versionSatisfies('>=0.10.0')) {
    args.push(...(await getAttestArgs(inputs, toolkit)));
  } else {
    core.warning("Attestations are only supported by buildx >= 0.10.0; the inputs 'attests', 'provenance' and 'sbom' are ignored.");
  }
  await Util.asyncForEach(inputs.secrets, async secret => {
    try {
      args.push('--secret', Build.resolveSecretString(secret));
    } catch (err) {
      core.warning(err.message);
    }
  });
  await Util.asyncForEach(inputs['secret-files'], async secretFile => {
    try {
      args.push('--secret', Build.resolveSecretFile(secretFile));
    } catch (err) {
      core.warning(err.message);
    }
  });
  if (inputs['github-token'] && !Build.hasGitAuthTokenSecret(inputs.secrets) && context.startsWith(Context.gitContext())) {
    args.push('--secret', Build.resolveSecretString(`GIT_AUTH_TOKEN.${new URL(GitHub.serverURL).host.trimEnd()}=${inputs['github-token']}`));
  }
  if (inputs['shm-size']) {
    args.push('--shm-size', inputs['shm-size']);
  }
  await Util.asyncForEach(inputs.ssh, async ssh => {
    args.push('--ssh', ssh);
  });
  await Util.asyncForEach(inputs.tags, async tag => {
    args.push('--tag', tag);
  });
  if (inputs.target) {
    args.push('--target', inputs.target);
  }
  await Util.asyncForEach(inputs.ulimit, async ulimit => {
    args.push('--ulimit', ulimit);
  });
  return args;
}

async function getCommonArgs(inputs: Inputs, toolkit: Toolkit): Promise<Array<string>> {
  const args: Array<string> = [];
  if (inputs.builder) {
    args.push('--builder', inputs.builder);
  }
  if (inputs.load) {
    args.push('--load');
  }
  if (await toolkit.buildx.versionSatisfies('>=0.6.0')) {
    args.push('--metadata-file', toolkit.buildxBuild.getMetadataFilePath());
  }
  if (inputs.network) {
    args.push('--network', inputs.network);
  }
  if (inputs['no-cache']) {
    args.push('--no-cache');
  }
  if (inputs.pull) {
    args.push('--pull');
  }
  if (inputs.push) {
    args.push('--push');
  }
  return args;
}

async function getAttestArgs(inputs: Inputs, toolkit: Toolkit): Promise<Array<string>> {
  const args: Array<string> = [];

  // check if provenance attestation is set in attests input
  let hasAttestProvenance = false;
  await Util.asyncForEach(inputs.attests, async (attest: string) => {
    if (Build.hasAttestationType('provenance', attest)) {
      hasAttestProvenance = true;
    }
  });

  let provenanceSet = false;
  let sbomSet = false;
  if (inputs.provenance) {
    args.push('--attest', Build.resolveAttestationAttrs(`type=provenance,${inputs.provenance}`));
    provenanceSet = true;
  } else if (!hasAttestProvenance && !noDefaultAttestations() && (await toolkit.buildkit.versionSatisfies(inputs.builder, '>=0.11.0')) && !Build.hasDockerExporter(inputs.outputs, inputs.load)) {
    // if provenance not specified in provenance or attests inputs and BuildKit
    // version compatible for attestation, set default provenance. Also needs
    // to make sure user doesn't want to explicitly load the image to docker.
    if (GitHub.context.payload.repository?.private ?? false) {
      // if this is a private repository, we set the default provenance
      // attributes being set in buildx: https://github.com/docker/buildx/blob/fb27e3f919dcbf614d7126b10c2bc2d0b1927eb6/build/build.go#L603
      args.push('--attest', `type=provenance,${Build.resolveProvenanceAttrs(`mode=min,inline-only=true`)}`);
    } else {
      // for a public repository, we set max provenance mode.
      args.push('--attest', `type=provenance,${Build.resolveProvenanceAttrs(`mode=max`)}`);
    }
  }
  if (inputs.sbom) {
    args.push('--attest', Build.resolveAttestationAttrs(`type=sbom,${inputs.sbom}`));
    sbomSet = true;
  }

  // set attests but check if provenance or sbom types already set as
  // provenance and sbom inputs take precedence over attests input.
  await Util.asyncForEach(inputs.attests, async (attest: string) => {
    if (!Build.hasAttestationType('provenance', attest) && !Build.hasAttestationType('sbom', attest)) {
      args.push('--attest', Build.resolveAttestationAttrs(attest));
    } else if (!provenanceSet && Build.hasAttestationType('provenance', attest)) {
      args.push('--attest', Build.resolveProvenanceAttrs(attest));
    } else if (!sbomSet && Build.hasAttestationType('sbom', attest)) {
      args.push('--attest', attest);
    }
  });

  return args;
}

function noDefaultAttestations(): boolean {
  if (process.env.BUILDX_NO_DEFAULT_ATTESTATIONS) {
    return Util.parseBool(process.env.BUILDX_NO_DEFAULT_ATTESTATIONS);
  }
  return false;
}

```

### File: src\main.ts
```ts
import * as fs from 'fs';
import * as path from 'path';
import * as core from '@actions/core';
import * as actionsToolkit from '@docker/actions-toolkit';

import {Buildx} from '@docker/actions-toolkit/lib/buildx/buildx.js';
import {History as BuildxHistory} from '@docker/actions-toolkit/lib/buildx/history.js';
import {Context} from '@docker/actions-toolkit/lib/context.js';
import {Docker} from '@docker/actions-toolkit/lib/docker/docker.js';
import {Exec} from '@docker/actions-toolkit/lib/exec.js';
import {GitHub} from '@docker/actions-toolkit/lib/github/github.js';
import {GitHubArtifact} from '@docker/actions-toolkit/lib/github/artifact.js';
import {GitHubSummary} from '@docker/actions-toolkit/lib/github/summary.js';
import {Toolkit} from '@docker/actions-toolkit/lib/toolkit.js';
import {Util} from '@docker/actions-toolkit/lib/util.js';

import {BuilderInfo} from '@docker/actions-toolkit/lib/types/buildx/builder.js';
import {ConfigFile} from '@docker/actions-toolkit/lib/types/docker/docker.js';
import {UploadResponse as UploadArtifactResponse} from '@docker/actions-toolkit/lib/types/github/artifact.js';

import * as context from './context.js';
import * as stateHelper from './state-helper.js';

actionsToolkit.run(
  // main
  async () => {
    const startedTime = new Date();
    const inputs: context.Inputs = await context.getInputs();
    stateHelper.setSummaryInputs(inputs);
    core.debug(`inputs: ${JSON.stringify(inputs)}`);

    const toolkit = new Toolkit();

    await core.group(`GitHub Actions runtime token ACs`, async () => {
      try {
        await GitHub.printActionsRuntimeTokenACs();
      } catch (e) {
        core.warning(e.message);
      }
    });

    await core.group(`Docker info`, async () => {
      try {
        await Docker.printVersion();
        await Docker.printInfo();
      } catch (e) {
        core.info(e.message);
      }
    });

    await core.group(`Proxy configuration`, async () => {
      let dockerConfig: ConfigFile | undefined;
      let dockerConfigMalformed = false;
      try {
        dockerConfig = await Docker.configFile();
      } catch (e) {
        dockerConfigMalformed = true;
        core.warning(`Unable to parse config file ${path.join(Docker.configDir, 'config.json')}: ${e}`);
      }
      if (dockerConfig && dockerConfig.proxies) {
        for (const host in dockerConfig.proxies) {
          let prefix = '';
          if (Object.keys(dockerConfig.proxies).length > 1) {
            prefix = '  ';
            core.info(host);
          }
          for (const key in dockerConfig.proxies[host]) {
            core.info(`${prefix}${key}: ${dockerConfig.proxies[host][key]}`);
          }
        }
      } else if (!dockerConfigMalformed) {
        core.info('No proxy configuration found');
      }
    });

    if (!(await toolkit.buildx.isAvailable())) {
      core.setFailed(`Docker buildx is required. See https://github.com/docker/setup-buildx-action to set up buildx.`);
      return;
    }

    stateHelper.setTmpDir(Context.tmpDir());

    await core.group(`Buildx version`, async () => {
      await toolkit.buildx.printVersion();
    });

    let builder: BuilderInfo;
    await core.group(`Builder info`, async () => {
      builder = await toolkit.builder.inspect(inputs.builder);
      stateHelper.setBuilderDriver(builder.driver ?? '');
      stateHelper.setBuilderEndpoint(builder.nodes?.[0]?.endpoint ?? '');
      core.info(JSON.stringify(builder, null, 2));
    });

    const args: string[] = await context.getArgs(inputs, toolkit);
    core.debug(`context.getArgs: ${JSON.stringify(args)}`);

    const buildCmd = await toolkit.buildx.getCommand(args);
    core.debug(`buildCmd.command: ${buildCmd.command}`);
    core.debug(`buildCmd.args: ${JSON.stringify(buildCmd.args)}`);

    let err: Error | undefined;
    await Exec.getExecOutput(buildCmd.command, buildCmd.args, {
      ignoreReturnCode: true,
      env: Object.assign({}, process.env, {
        BUILDX_METADATA_WARNINGS: 'true'
      }) as {
        [key: string]: string;
      }
    }).then(res => {
      if (res.exitCode != 0) {
        if (inputs.call && inputs.call === 'check' && res.stdout.length > 0) {
          // checks warnings are printed to stdout: https://github.com/docker/buildx/pull/2647
          // take the first line with the message summaryzing the warnings
          err = new Error(res.stdout.split('\n')[0]?.trim());
        } else if (res.stderr.length > 0) {
          err = new Error(`buildx failed with: ${res.stderr.match(/(.*)\s*$/)?.[0]?.trim() ?? 'unknown error'}`);
        }
      }
    });

    const imageID = toolkit.buildxBuild.resolveImageID();
    const metadata = toolkit.buildxBuild.resolveMetadata();
    const digest = toolkit.buildxBuild.resolveDigest(metadata);
    if (imageID) {
      await core.group(`ImageID`, async () => {
        core.info(imageID);
        core.setOutput('imageid', imageID);
      });
    }
    if (digest) {
      await core.group(`Digest`, async () => {
        core.info(digest);
        core.setOutput('digest', digest);
      });
    }
    if (metadata) {
      await core.group(`Metadata`, async () => {
        const metadatadt = JSON.stringify(metadata, null, 2);
        core.info(metadatadt);
        core.setOutput('metadata', metadatadt);
      });
    }

    let ref: string | undefined;
    await core.group(`Reference`, async () => {
      ref = await buildRef(toolkit, startedTime, inputs.builder);
      if (ref) {
        core.info(ref);
        stateHelper.setBuildRef(ref);
      } else {
        core.info('No build reference found');
      }
    });

    if (buildChecksAnnotationsEnabled()) {
      const warnings = toolkit.buildxBuild.resolveWarnings(metadata);
      if (ref && warnings && warnings.length > 0) {
        const annotations = await Buildx.convertWarningsToGitHubAnnotations(warnings, [ref]);
        core.debug(`annotations: ${JSON.stringify(annotations, null, 2)}`);
        if (annotations && annotations.length > 0) {
          await core.group(`Generating GitHub annotations (${annotations.length} build checks found)`, async () => {
            for (const annotation of annotations) {
              core.warning(annotation.message, annotation);
            }
          });
        }
      }
    }

    await core.group(`Check build summary support`, async () => {
      if (!buildSummaryEnabled()) {
        core.info('Build summary disabled');
      } else if (inputs.call && inputs.call !== 'build') {
        core.info(`Build summary skipped for ${inputs.call} subrequest`);
      } else if (GitHub.isGHES) {
        core.info('Build summary is not yet supported on GHES');
      } else if (!(await toolkit.buildx.versionSatisfies('>=0.23.0'))) {
        core.info('Build summary requires Buildx >= 0.23.0');
      } else if (!ref) {
        core.info('Build summary requires a build reference');
      } else {
        core.info('Build summary supported!');
        stateHelper.setSummarySupported();
      }
    });

    if (err) {
      throw err;
    }
  },
  // post
  async () => {
    if (stateHelper.isSummarySupported) {
      await core.group(`Generating build summary`, async () => {
        try {
          const recordUploadEnabled = buildRecordUploadEnabled();
          let recordRetentionDays: number | undefined;
          if (recordUploadEnabled) {
            recordRetentionDays = buildRecordRetentionDays();
          }

          const buildxHistory = new BuildxHistory();
          const exportRes = await buildxHistory.export({
            refs: stateHelper.buildRef ? [stateHelper.buildRef] : []
          });
          core.info(`Build record written to ${exportRes.dockerbuildFilename} (${Util.formatFileSize(exportRes.dockerbuildSize)})`);

          let uploadRes: UploadArtifactResponse | undefined;
          if (recordUploadEnabled) {
            uploadRes = await GitHubArtifact.upload({
              filename: exportRes.dockerbuildFilename,
              retentionDays: recordRetentionDays
            });
          }

          await GitHubSummary.writeBuildSummary({
            exportRes: exportRes,
            uploadRes: uploadRes,
            inputs: stateHelper.summaryInputs,
            driver: stateHelper.builderDriver,
            endpoint: stateHelper.builderEndpoint
          });
        } catch (e) {
          core.warning(e.message);
        }
      });
    }
    if (stateHelper.tmpDir.length > 0) {
      await core.group(`Removing temp folder ${stateHelper.tmpDir}`, async () => {
        try {
          fs.rmSync(stateHelper.tmpDir, {recursive: true});
        } catch {
          core.warning(`Failed to remove temp folder ${stateHelper.tmpDir}`);
        }
      });
    }
  }
);

async function buildRef(toolkit: Toolkit, since: Date, builder?: string): Promise<string> {
  // get ref from metadata file
  const ref = toolkit.buildxBuild.resolveRef();
  if (ref) {
    return ref;
  }
  // otherwise, look for the very first build ref since the build has started
  if (!builder) {
    const currentBuilder = await toolkit.builder.inspect();
    builder = currentBuilder.name;
  }
  const refs = Buildx.refs({
    dir: Buildx.refsDir,
    builderName: builder,
    since: since
  });
  return Object.keys(refs).length > 0 ? Object.keys(refs)[0] : '';
}

function buildChecksAnnotationsEnabled(): boolean {
  if (process.env.DOCKER_BUILD_CHECKS_ANNOTATIONS) {
    return Util.parseBool(process.env.DOCKER_BUILD_CHECKS_ANNOTATIONS);
  }
  return true;
}

function buildSummaryEnabled(): boolean {
  if (process.env.DOCKER_BUILD_SUMMARY) {
    return Util.parseBool(process.env.DOCKER_BUILD_SUMMARY);
  }
  return true;
}

function buildRecordUploadEnabled(): boolean {
  if (process.env.DOCKER_BUILD_RECORD_UPLOAD) {
    return Util.parseBool(process.env.DOCKER_BUILD_RECORD_UPLOAD);
  }
  return true;
}

function buildRecordRetentionDays(): number | undefined {
  const val = process.env.DOCKER_BUILD_RECORD_RETENTION_DAYS;
  if (val) {
    const res = parseInt(val);
    if (isNaN(res)) {
      throw new Error(`Invalid build record retention days: ${val}`);
    }
    return res;
  }
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

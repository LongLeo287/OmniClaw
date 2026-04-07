---
id: metadata-action
type: knowledge
owner: OA_Triage
---
# metadata-action
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "docker-metadata-action",
  "description": "GitHub Action to extract metadata (tags, labels) for Docker",
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
    "url": "git+https://github.com/docker/metadata-action.git"
  },
  "keywords": [
    "actions",
    "docker",
    "metadata",
    "tag",
    "label"
  ],
  "author": "Docker Inc.",
  "license": "Apache-2.0",
  "packageManager": "yarn@4.9.2",
  "dependencies": {
    "@actions/core": "^3.0.0",
    "@actions/github": "^9.0.0",
    "@docker/actions-toolkit": "^0.79.0",
    "@renovate/pep440": "^1.0.0",
    "csv-parse": "^6.1.0",
    "handlebars": "^4.7.8",
    "moment": "^2.30.1",
    "moment-timezone": "^0.6.1",
    "semver": "^7.7.4"
  },
  "devDependencies": {
    "@eslint/js": "^9.39.3",
    "@types/node": "^24.11.0",
    "@types/semver": "^7.7.1",
    "@typescript-eslint/eslint-plugin": "^8.56.1",
    "@typescript-eslint/parser": "^8.56.1",
    "@vercel/ncc": "^0.38.4",
    "@vitest/coverage-v8": "^4.0.18",
    "@vitest/eslint-plugin": "^1.6.9",
    "dotenv": "^17.3.1",
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
[![GitHub release](https://img.shields.io/github/release/docker/metadata-action.svg?style=flat-square)](https://github.com/docker/metadata-action/releases/latest)
[![GitHub marketplace](https://img.shields.io/badge/marketplace-docker--metadata--action-blue?logo=github&style=flat-square)](https://github.com/marketplace/actions/docker-metadata-action)
[![CI workflow](https://img.shields.io/github/actions/workflow/status/docker/metadata-action/ci.yml?branch=master&label=ci&logo=github&style=flat-square)](https://github.com/docker/metadata-action/actions?workflow=ci)
[![Test workflow](https://img.shields.io/github/actions/workflow/status/docker/metadata-action/test.yml?branch=master&label=test&logo=github&style=flat-square)](https://github.com/docker/metadata-action/actions?workflow=test)
[![Codecov](https://img.shields.io/codecov/c/github/docker/metadata-action?logo=codecov&style=flat-square)](https://codecov.io/gh/docker/metadata-action)

## About

GitHub Action to extract metadata from Git reference and GitHub events. This action
is particularly useful if used with [Docker Build Push](https://github.com/docker/build-push-action)
action to tag and label Docker images.

![Screenshot](.github/metadata-action.png)

___

* [Usage](#usage)
  * [Basic](#basic)
  * [Semver](#semver)
  * [Bake definition](#bake-definition)
* [Customizing](#customizing)
  * [inputs](#inputs)
  * [outputs](#outputs)
  * [environment variables](#environment-variables)
* [`context` input](#context-input)
* [`images` input](#images-input)
* [`flavor` input](#flavor-input)
* [`tags` input](#tags-input)
  * [`type=schedule`](#typeschedule)
  * [`type=semver`](#typesemver)
  * [`type=pep440`](#typepep440)
  * [`type=match`](#typematch)
  * [`type=edge`](#typeedge)
  * [`type=ref`](#typeref)
  * [`type=raw`](#typeraw)
  * [`type=sha`](#typesha)
* [Notes](#notes)
  * [Image name and tag sanitization](#image-name-and-tag-sanitization)
  * [Latest tag](#latest-tag)
  * [`priority` attribute](#priority-attribute)
  * [Global expressions](#global-expressions)
    * [`{{branch}}`](#branch)
    * [`{{tag}}`](#tag)
    * [`{{sha}}`](#sha)
    * [`{{base_ref}}`](#base_ref)
    * [`{{is_default_branch}}`](#is_default_branch)
    * [`{{is_not_default_branch}}`](#is_not_default_branch)
    * [`{{date '<format>' tz='<timezone>'}}`](#date-format-tztimezone)
    * [`{{commit_date '<format>' tz='<timezone>'}}`](#commit_date-format-tztimezone)
  * [Major version zero](#major-version-zero)
  * [JSON output object](#json-output-object)
  * [Overwrite labels and annotations](#overwrite-labels-and-annotations)
  * [Annotations](#annotations)
* [Contributing](#contributing)

## Usage

### Basic

```yaml
name: ci

on:
  workflow_dispatch:
  push:
    branches:
      - 'master'
    tags:
      - 'v*'
  pull_request:
    branches:
      - 'master'

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      -
        name: Docker meta
        id: meta
        uses: docker/metadata-action@v6
        with:
          images: name/app
      -
        name: Login to DockerHub
        if: github.event_name != 'pull_request'
        uses: docker/login-action@v4
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      -
        name: Build and push
        uses: docker/build-push-action@v7
        with:
          push: ${{ github.event_name != 'pull_request' }}
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
```

| Event               | Ref                           | Docker Tags                |
|---------------------|-------------------------------|----------------------------|
| `pull_request`      | `refs/pull/2/merge`           | `pr-2`                     |
| `push`              | `refs/heads/master`           | `master`                   |
| `push`              | `refs/heads/releases/v1`      | `releases-v1`              |
| `push tag`          | `refs/tags/v1.2.3`            | `v1.2.3`, `latest`         |
| `push tag`          | `refs/tags/v2.0.8-beta.67`    | `v2.0.8-beta.67`, `latest` |
| `workflow_dispatch` | `refs/heads/master`           | `master`                   |

### Semver

```yaml
name: ci

on:
  push:
    branches:
      - 'master'
    tags:
      - 'v*'
  pull_request:
    branches:
      - 'master'

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      -
        name: Docker meta
        id: meta
        uses: docker/metadata-action@v6
        with:
          images: |
            name/app
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}
      -
        name: Login to DockerHub
        if: github.event_name != 'pull_request'
        uses: docker/login-action@v4
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      -
        name: Build and push
        uses: docker/build-push-action@v7
        with:
          push: ${{ github.event_name != 'pull_request' }}
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
```

| Event           | Ref                           | Docker Tags                         |
|-----------------|-------------------------------|-------------------------------------|
| `pull_request`  | `refs/pull/2/merge`           | `pr-2`                              |
| `push`          | `refs/heads/master`           | `master`                            |
| `push`          | `refs/heads/releases/v1`      | `releases-v1`                       |
| `push tag`      | `refs/tags/v1.2.3`            | `1.2.3`, `1.2`, `latest`            |
| `push tag`      | `refs/tags/v2.0.8-beta.67`    | `2.0.8-beta.67`                     |

### Bake definition

This action also handles a bake definition file that can be used with the
[Docker Bake action](https://github.com/docker/bake-action). You just have to
declare an empty target named `docker-metadata-action` and inherit from it.

```hcl
// docker-bake.hcl
target "docker-metadata-action" {}

target "build" {
  inherits = ["docker-metadata-action"]
  context = "./"
  dockerfile = "Dockerfile"
  platforms = [
    "linux/amd64",
    "linux/arm/v6",
    "linux/arm/v7",
    "linux/arm64",
    "linux/386"
  ]
}
```

```yaml
name: ci

on:
  push:
    branches:
      - 'master'
    tags:
      - 'v*'

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      -
        name: Docker meta
        id: meta
        uses: docker/metadata-action@v6
        with:
          images: |
            name/app
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}
            type=sha
      -
        name: Build
        uses: docker/bake-action@v7
        with:
          files: |
            ./docker-bake.hcl
            cwd://${{ steps.meta.outputs.bake-file }}
          targets: build
```

Content of `${{ steps.meta.outputs.bake-file }}` file, combining tags and
labels, will look like this with `refs/tags/v1.2.3` ref:

```json
{
  "target": {
    "docker-metadata-action": {
      "tags": [
        "name/app:1.2.3",
        "name/app:1.2",
        "name/app:sha-90dd603",
        "name/app:latest"
      ],
      "labels": {
        "org.opencontainers.image.title": "Hello-World",
        "org.opencontainers.image.description": "This your first repo!",
        "org.opencontainers.image.url": "https://github.com/octocat/Hello-World",
        "org.opencontainers.image.source": "https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version": "1.2.3",
        "org.opencontainers.image.created": "2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.revision": "860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.licenses": "MIT"
      },
      "args": {
        "DOCKER_META_IMAGES": "name/app",
        "DOCKER_META_VERSION": "1.2.3"
      }
    }
  }
}
```

You can also use the `bake-file-tags` and `bake-file-labels` outputs if you
just want to use tags and/or labels respectively. The following example is
similar to the previous one:

```yaml
      -
        name: Build
        uses: docker/bake-action@v7
        with:
          files: |
            ./docker-bake.hcl
            cwd://${{ steps.meta.outputs.bake-file-tags }}
            cwd://${{ steps.meta.outputs.bake-file-labels }}
          targets: build
```

## Customizing

### inputs

The following inputs can be used as `step.with` keys:

> [!NOTE]
> `List` type is a newline-delimited string
> ```yaml
> labels: |
>   org.opencontainers.image.title=MyCustomTitle
>   org.opencontainers.image.description=Another description
>   org.opencontainers.image.vendor=MyCompany
> ```

| Name              | Type   | Description                                                                  |
|-------------------|--------|------------------------------------------------------------------------------|
| `context`         | String | Where to get context data. Allowed options are: `workflow` (default), `git`. |
| `images`          | List   | List of Docker images to use as base name for tags                           |
| `tags`            | List   | List of [tags](#tags-input) as key-value pair attributes                     |
| `flavor`          | List   | [Flavor](#flavor-input) to apply                                             |
| `labels`          | List   | List of custom labels                                                        |
| `annotations`     | List   | List of custom annotations                                                   |
| `sep-tags`        | String | Separator to use for tags output (default `\n`)                              |
| `sep-labels`      | String | Separator to use for labels output (default `\n`)                            |
| `sep-annotations` | String | Separator to use for annotations output (default `\n`)                       |
| `bake-target`     | String | Bake target name (default `docker-metadata-action`)                          |

### outputs

The following outputs are available:

| Name                    | Type   | Description                                                                                                                                                     |
|-------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `version`               | String | Docker image version                                                                                                                                            |
| `tags`                  | String | Docker tags                                                                                                                                                     |
| `tag-names`             | String | Docker tag names without image base name                                                                                                                        |
| `labels`                | String | Docker labels                                                                                                                                                   |
| `annotations`           | String | [Annotations](https://github.com/moby/buildkit/blob/master/docs/annotations.md)                                                                                 |
| `json`                  | String | JSON output of tags and labels                                                                                                                                  |
| `bake-file-tags`        | File   | [Bake file definition](https://docs.docker.com/build/bake/reference/) path with tags                                                                            |
| `bake-file-labels`      | File   | [Bake file definition](https://docs.docker.com/build/bake/reference/) path with labels                                                                          |
| `bake-file-annotations` | File   | [Bake file definition](https://docs.docker.com/build/bake/reference/) path with [annotations](https://github.com/moby/buildkit/blob/master/docs/annotations.md) |

Alternatively, each output is also exported as an environment variable when `DOCKER_METADATA_SET_OUTPUT_ENV` is `true`:

* `DOCKER_METADATA_OUTPUT_VERSION`
* `DOCKER_METADATA_OUTPUT_TAGS`
* `DOCKER_METADATA_OUTPUT_LABELS`
* `DOCKER_METADATA_OUTPUT_ANNOTATIONS`
* `DOCKER_METADATA_OUTPUT_JSON`
* `DOCKER_METADATA_OUTPUT_BAKE_FILE_TAGS`
* `DOCKER_METADATA_OUTPUT_BAKE_FILE_LABELS`
* `DOCKER_METADATA_OUTPUT_BAKE_FILE_ANNOTATIONS`

So it can be used with our [Docker Build Push action](https://github.com/docker/build-push-action/):

```yaml
- uses: docker/build-push-action@v7
  with:
    build-args: |
      DOCKER_METADATA_OUTPUT_JSON
```

### environment variables

| Name                                 | Type   | Description                                                                                                                                  |
|--------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------|
| `DOCKER_METADATA_PR_HEAD_SHA`        | Bool   | If `true`, set associated head SHA instead of commit SHA that triggered the workflow on pull request event                                   |
| `DOCKER_METADATA_SHORT_SHA_LENGTH`   | Number | Specifies the length of the [short commit SHA](#typesha) to ensure uniqueness. Default is `7`, but can be increased for larger repositories. |
| `DOCKER_METADATA_ANNOTATIONS_LEVELS` | String | Comma separated list of annotations levels to set for annotations output separated (default `manifest`)                                      |
| `DOCKER_METADATA_SET_OUTPUT_ENV`     | Bool   | If `true`, sets each output as an environment variable (default `true`)                                                                      |

## `context` input

`context` defines where to get context metadata:

```yaml
# default
context: workflow
# or
context: git
```

* `workflow`: Get context metadata from the workflow (GitHub context). See https://docs.github.com/en/actions/learn-github-actions/contexts#github-context
* `git`: Get context metadata from the workflow and overrides some of them with current Git context, such as `ref` and `sha`.

## `images` input

`images` defines a list of Docker images to use as base name for [`tags`](#tags-input):

```yaml
images: |
  name/foo
  ghcr.io/name/bar
  # or
  name=name/foo
  name=ghcr.io/name/bar
```

Extended attributes and default values:

```yaml
images: |
  name=,enable=true
```

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

1. [Fork](https://github.com/docker/metadata-action/fork) and clone the repository
2. Configure and install the dependencies: `yarn install`
3. Create a new branch: `git checkout -b my-branch-name`
4. Make your changes
5. Make sure the tests pass: `docker buildx bake test`
6. Format code and build javascript artifacts: `docker buildx bake pre-checkin`
7. Validate all code has correctly formatted and built: `docker buildx bake validate`
8. Push to your fork and [submit a pull request](https://github.com/docker/metadata-action/compare)
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
import * as core from '@actions/core';

import {Util} from '@docker/actions-toolkit/lib/util.js';
import {Git} from '@docker/actions-toolkit/lib/git.js';
import {GitHub} from '@docker/actions-toolkit/lib/github/github.js';
import {Toolkit} from '@docker/actions-toolkit/lib/toolkit.js';

type GithubContext = typeof GitHub.context;

export interface Context extends GithubContext {
  commitDate: Date;
}

export interface Inputs {
  context: ContextSource;
  images: string[];
  tags: string[];
  flavor: string[];
  labels: string[];
  annotations: string[];
  sepTags: string;
  sepLabels: string;
  sepAnnotations: string;
  bakeTarget: string;
  githubToken: string;
}

export function getInputs(): Inputs {
  return {
    context: (core.getInput('context') || ContextSource.workflow) as ContextSource,
    images: Util.getInputList('images', {ignoreComma: true, comment: '#', commentNoInfix: true}),
    tags: Util.getInputList('tags', {ignoreComma: true, comment: '#', commentNoInfix: true}),
    flavor: Util.getInputList('flavor', {ignoreComma: true, comment: '#', commentNoInfix: true}),
    labels: Util.getInputList('labels', {ignoreComma: true, comment: '#', commentNoInfix: true}),
    annotations: Util.getInputList('annotations', {ignoreComma: true, comment: '#', commentNoInfix: true}),
    sepTags: core.getInput('sep-tags', {trimWhitespace: false}) || `\n`,
    sepLabels: core.getInput('sep-labels', {trimWhitespace: false}) || `\n`,
    sepAnnotations: core.getInput('sep-annotations', {trimWhitespace: false}) || `\n`,
    bakeTarget: core.getInput('bake-target') || `docker-metadata-action`,
    githubToken: core.getInput('github-token')
  };
}

export enum ContextSource {
  workflow = 'workflow',
  git = 'git'
}

export async function getContext(source: ContextSource, toolkit: Toolkit): Promise<Context> {
  switch (source) {
    case ContextSource.workflow:
      return await getContextFromWorkflow(toolkit);
    case ContextSource.git:
      return await getContextFromGit();
    default:
      throw new Error(`Invalid context source: ${source}`);
  }
}

async function getContextFromWorkflow(toolkit: Toolkit): Promise<Context> {
  const context = GitHub.context;

  // Needs to override Git reference with pr ref instead of upstream branch ref
  // for pull_request_target event
  // https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request_target
  if (/pull_request_target/.test(context.eventName)) {
    context.ref = `refs/pull/${context.payload.number}/merge`;
  }

  // DOCKER_METADATA_PR_HEAD_SHA env var can be used to set associated head
  // SHA instead of commit SHA that triggered the workflow on pull request
  // event.
  if (/true/i.test(process.env.DOCKER_METADATA_PR_HEAD_SHA || '')) {
    if ((/pull_request/.test(context.eventName) || /pull_request_target/.test(context.eventName)) && context.payload?.pull_request?.head?.sha != undefined) {
      context.sha = context.payload.pull_request.head.sha;
    }
  }

  return {
    commitDate: await getCommitDateFromWorkflow(context.sha, toolkit),
    ...context
  } as Context;
}

async function getContextFromGit(): Promise<Context> {
  const ctx = await Git.context();

  return {
    commitDate: await Git.commitDate(ctx.sha),
    ...ctx
  } as Context;
}

async function getCommitDateFromWorkflow(sha: string, toolkit: Toolkit): Promise<Date> {
  const event = GitHub.context.payload as unknown as {
    // branch push
    commits?: Array<{
      timestamp: string;
      // commit sha
      id: string;
    }>;
    // tags
    head_commit?: {
      timestamp: string;
      // commit sha
      id: string;
    };
  };

  if (event.commits) {
    const commitDate = event.commits.find(x => x.id === sha)?.timestamp;
    if (commitDate) {
      return new Date(commitDate);
    }
  }

  if (event.head_commit) {
    if (event.head_commit.id === sha) {
      return new Date(event.head_commit.timestamp);
    }
  }

  // fallback to github api for commit date
  try {
    const commit = await toolkit.github.octokit.rest.repos.getCommit({
      owner: GitHub.context.repo.owner,
      repo: GitHub.context.repo.repo,
      ref: sha
    });
    if (commit.data.commit.committer?.date) {
      return new Date(commit.data.commit.committer.date);
    }
    throw new Error('Committer date not found');
  } catch (error) {
    core.debug(`Failed to get commit date from GitHub API: ${error.message}`);
    return new Date();
  }
}

```

### File: src\flavor.ts
```ts
import {parse} from 'csv-parse/sync';
import * as core from '@actions/core';

export interface Flavor {
  latest: string;
  prefix: string;
  prefixLatest: boolean;
  suffix: string;
  suffixLatest: boolean;
}

export function Transform(inputs: string[]): Flavor {
  const flavor: Flavor = {
    latest: 'auto',
    prefix: '',
    prefixLatest: false,
    suffix: '',
    suffixLatest: false
  };

  for (const input of inputs) {
    const fields = parse(input, {
      relaxColumnCount: true,
      skipEmptyLines: true
    })[0];
    let onlatestfor = '';
    for (const field of fields) {
      const parts = field
        .toString()
        .split('=')
        .map(item => item.trim());
      if (parts.length == 1) {
        throw new Error(`Invalid flavor entry: ${input}`);
      }
      const key = parts[0].toLowerCase();
      const value = parts[1];
      switch (key) {
        case 'latest': {
          flavor.latest = value;
          if (!['auto', 'true', 'false'].includes(flavor.latest)) {
            throw new Error(`Invalid latest flavor entry: ${input}`);
          }
          break;
        }
        case 'prefix': {
          flavor.prefix = value;
          onlatestfor = 'prefix';
          break;
        }
        case 'suffix': {
          flavor.suffix = value;
          onlatestfor = 'suffix';
          break;
        }
        case 'onlatest': {
          if (!['true', 'false'].includes(value)) {
            throw new Error(`Invalid value for onlatest attribute: ${value}`);
          }
          switch (onlatestfor) {
            case 'prefix': {
              flavor.prefixLatest = /true/i.test(value);
              break;
            }
            case 'suffix': {
              flavor.suffixLatest = /true/i.test(value);
              break;
            }
          }
          break;
        }
        default: {
          throw new Error(`Unknown flavor entry: ${input}`);
        }
      }
    }
  }

  core.startGroup(`Processing flavor input`);
  core.info(`latest=${flavor.latest}`);
  core.info(`prefix=${flavor.prefix}`);
  core.info(`prefixLatest=${flavor.prefixLatest}`);
  core.info(`suffix=${flavor.suffix}`);
  core.info(`suffixLatest=${flavor.suffixLatest}`);
  core.endGroup();

  return flavor;
}

```

### File: src\image.ts
```ts
import {parse} from 'csv-parse/sync';
import * as core from '@actions/core';

export interface Image {
  name: string;
  enable: boolean;
}

export function Transform(inputs: string[]): Image[] {
  let images: Image[] = [];

  // backward compatibility with old format
  if (inputs.length == 1) {
    let newformat = false;
    const fields = parse(inputs[0], {
      relaxColumnCount: true,
      skipEmptyLines: true
    })[0];
    for (const field of fields) {
      const parts = field
        .toString()
        .split('=')
        .map(item => item.trim());
      if (parts.length == 1) {
        images.push({name: parts[0], enable: true});
      } else {
        newformat = true;
        break;
      }
    }
    if (!newformat) {
      return output(images);
    }
  }

  images = [];
  for (const input of inputs) {
    const image: Image = {name: '', enable: true};
    const fields = parse(input, {
      relaxColumnCount: true,
      skipEmptyLines: true
    })[0];
    for (const field of fields) {
      const parts = field
        .toString()
        .split('=')
        .map(item => item.trim());
      if (parts.length == 1) {
        image.name = parts[0];
      } else {
        const key = parts[0].toLowerCase();
        const value = parts[1];
        switch (key) {
          case 'name': {
            image.name = value;
            break;
          }
          case 'enable': {
            if (!['true', 'false'].includes(value)) {
              throw new Error(`Invalid enable attribute value: ${input}`);
            }
            image.enable = /true/i.test(value);
            break;
          }
          default: {
            throw new Error(`Unknown image attribute: ${input}`);
          }
        }
      }
    }
    if (image.name.length == 0) {
      throw new Error(`Image name attribute empty: ${input}`);
    }
    images.push(image);
  }
  return output(images);
}

function output(images: Image[]): Image[] {
  core.startGroup(`Processing images input`);
  for (const image of images) {
    core.info(`name=${image.name},enable=${image.enable}`);
  }
  core.endGroup();
  return images;
}

```

### File: src\main.ts
```ts
import * as fs from 'fs';
import * as core from '@actions/core';
import * as actionsToolkit from '@docker/actions-toolkit';
import {Toolkit} from '@docker/actions-toolkit/lib/toolkit.js';
import {Util} from '@docker/actions-toolkit/lib/util.js';

import {getContext, getInputs, Inputs} from './context.js';
import {Meta, Version} from './meta.js';

actionsToolkit.run(
  // main
  async () => {
    const inputs: Inputs = getInputs();
    const toolkit = new Toolkit({githubToken: inputs.githubToken});
    const context = await getContext(inputs.context, toolkit);
    const repo = await toolkit.github.repoData();
    const setOutput = outputEnvEnabled() ? setOutputAndEnv : core.setOutput;

    await core.group(`Context info`, async () => {
      core.info(`eventName: ${context.eventName}`);
      core.info(`sha: ${context.sha}`);
      core.info(`ref: ${context.ref}`);
      core.info(`workflow: ${context.workflow}`);
      core.info(`action: ${context.action}`);
      core.info(`actor: ${context.actor}`);
      core.info(`runNumber: ${context.runNumber}`);
      core.info(`runId: ${context.runId}`);
      core.info(`commitDate: ${context.commitDate}`);
    });

    if (core.isDebug()) {
      await core.group(`Webhook payload`, async () => {
        core.info(JSON.stringify(context.payload, null, 2));
      });
    }

    const meta: Meta = new Meta(inputs, context, repo);

    const version: Version = meta.version;
    if (meta.version.main == undefined || meta.version.main.length == 0) {
      core.warning(`No Docker image version has been generated. Check tags input.`);
    } else {
      await core.group(`Docker image version`, async () => {
        core.info(version.main || '');
      });
    }
    setOutput('version', version.main || '');

    // Docker tags
    const tags = meta.getTags();
    if (tags.length == 0) {
      core.warning('No Docker tag has been generated. Check tags input.');
    } else {
      await core.group(`Docker tags`, async () => {
        for (const tag of tags) {
          core.info(tag);
        }
      });
    }
    setOutput('tags', tags.join(inputs.sepTags));
    setOutput('tag-names', meta.getTags(true).join(inputs.sepTags));

    // Docker labels
    const labels: Array<string> = meta.getLabels();
    await core.group(`Docker labels`, async () => {
      for (const label of labels) {
        core.info(label);
      }
      setOutput('labels', labels.join(inputs.sepLabels));
    });

    // Annotations
    const annotationsRaw: Array<string> = meta.getAnnotations();
    const annotationsLevels = process.env.DOCKER_METADATA_ANNOTATIONS_LEVELS || 'manifest';
    await core.group(`Annotations`, async () => {
      const annotations: Array<string> = [];
      for (const level of annotationsLevels.split(',')) {
        annotations.push(
          ...annotationsRaw.map(label => {
            const v = `${level}:${label}`;
            core.info(v);
            return v;
          })
        );
      }
      setOutput(`annotations`, annotations.join(inputs.sepAnnotations));
    });

    // JSON
    const jsonOutput = meta.getJSON(annotationsLevels.split(','));
    await core.group(`JSON output`, async () => {
      core.info(JSON.stringify(jsonOutput, null, 2));
      setOutput('json', JSON.stringify(jsonOutput));
    });

    // Bake files
    for (const kind of ['tags', 'labels', 'annotations:' + annotationsLevels]) {
      const outputName = kind.split(':')[0];
      const bakeFile: string = meta.getBakeFile(kind);
      await core.group(`Bake file definition (${outputName})`, async () => {
        core.info(fs.readFileSync(bakeFile, 'utf8'));
        setOutput(`bake-file-${outputName}`, bakeFile);
      });
    }

    // Bake file with tags and labels
    setOutput(`bake-file`, `${meta.getBakeFileTagsLabels()}`);
  }
);

function setOutputAndEnv(name: string, value: string) {
  core.setOutput(name, value);
  core.exportVariable(`DOCKER_METADATA_OUTPUT_${name.replace(/\W/g, '_').toUpperCase()}`, value);
}

function outputEnvEnabled(): boolean {
  if (process.env.DOCKER_METADATA_SET_OUTPUT_ENV) {
    return Util.parseBool(process.env.DOCKER_METADATA_SET_OUTPUT_ENV);
  }
  return true;
}

```

### File: src\meta.ts
```ts
import * as handlebars from 'handlebars';
import * as fs from 'fs';
import * as path from 'path';
import moment from 'moment-timezone';
import * as pep440 from '@renovate/pep440';
import * as semver from 'semver';
import * as core from '@actions/core';
import {Context as ToolkitContext} from '@docker/actions-toolkit/lib/context.js';
import {GitHubRepo} from '@docker/actions-toolkit/lib/types/github/github.js';

import {Inputs, Context} from './context.js';
import * as icl from './image.js';
import * as tcl from './tag.js';
import * as fcl from './flavor.js';

const defaultShortShaLength = 7;

export interface Version {
  main: string | undefined;
  partial: string[];
  latest: boolean | undefined;
}

export class Meta {
  public readonly version: Version;

  private readonly inputs: Inputs;
  private readonly context: Context;
  private readonly repo: GitHubRepo;
  private readonly images: icl.Image[];
  private readonly tags: tcl.Tag[];
  private readonly flavor: fcl.Flavor;
  private readonly date: Date;

  constructor(inputs: Inputs, context: Context, repo: GitHubRepo) {
    this.inputs = inputs;
    this.context = context;
    this.repo = repo;
    this.images = icl.Transform(inputs.images);
    this.tags = tcl.Transform(inputs.tags);
    this.flavor = fcl.Transform(inputs.flavor);
    this.date = new Date();
    this.version = this.getVersion();
  }

  private getVersion(): Version {
    let version: Version = {
      main: undefined,
      partial: [],
      latest: undefined
    };

    for (const tag of this.tags) {
      const enabled = this.setGlobalExp(tag.attrs['enable']);
      if (!['true', 'false'].includes(enabled)) {
        throw new Error(`Invalid value for enable attribute: ${enabled}`);
      }
      if (!/true/i.test(enabled)) {
        continue;
      }
      switch (tag.type) {
        case tcl.Type.Schedule: {
          version = this.procSchedule(version, tag);
          break;
        }
        case tcl.Type.Semver: {
          version = this.procSemver(version, tag);
          break;
        }
        case tcl.Type.Pep440: {
          version = this.procPep440(version, tag);
          break;
        }
        case tcl.Type.Match: {
          version = this.procMatch(version, tag);
          break;
        }
        case tcl.Type.Ref: {
          if (tag.attrs['event'] == tcl.RefEvent.Branch) {
            version = this.procRefBranch(version, tag);
          } else if (tag.attrs['event'] == tcl.RefEvent.Tag) {
            version = this.procRefTag(version, tag);
          } else if (tag.attrs['event'] == tcl.RefEvent.PR) {
            version = this.procRefPr(version, tag);
          }
          break;
        }
        case tcl.Type.Edge: {
          version = this.procEdge(version, tag);
          break;
        }
        case tcl.Type.Raw: {
          version = this.procRaw(version, tag);
          break;
        }
        case tcl.Type.Sha: {
          version = this.procSha(version, tag);
          break;
        }
      }
    }

    version.partial = version.partial.filter((item, index) => version.partial.indexOf(item) === index);
    if (version.latest == undefined) {
      version.latest = false;
    }

    return version;
  }

  private procSchedule(version: Version, tag: tcl.Tag): Version {
    if (!/schedule/.test(this.context.eventName)) {
      return version;
    }

    const currentDate = this.date;
    const commitDate = this.context.commitDate;
    const vraw = this.setValue(
      handlebars.compile(tag.attrs['pattern'])({
        date: function (format, options) {
          const m = moment(currentDate);
          let tz = 'UTC';
          Object.keys(options.hash).forEach(key => {
            switch (key) {
              case 'tz':
                tz = options.hash[key];
                break;
              default:
                throw new Error(`Unknown ${key} attribute`);
            }
          });
          return m.tz(tz).format(format);
        },
        commit_date: function (format, options) {
          const m = moment(commitDate);
          let tz = 'UTC';
          Object.keys(options.hash).forEach(key => {
            switch (key) {
              case 'tz':
                tz = options.hash[key];
                break;
              default:
                throw new Error(`Unknown ${key} attribute`);
            }
          });
          return m.tz(tz).format(format);
        }
      }),
      tag
    );

    return Meta.setVersion(version, vraw, this.flavor.latest == 'auto' ? false : this.flavor.latest == 'true');
  }

  private procSemver(version: Version, tag: tcl.Tag): Version {
    if (!/^refs\/tags\//.test(this.context.ref) && tag.attrs['value'].length == 0) {
      return version;
    }

    let vraw: string;
    if (tag.attrs['value'].length > 0) {
      vraw = this.setGlobalExp(tag.attrs['value']);
    } else {
      vraw = this.context.ref.replace(/^refs\/tags\//g, '');
    }

    if (tag.attrs['match'].length > 0) {
      const tmatch = vraw.match(tag.attrs['match']);
      if (!tmatch) {
        core.warning(`${tag.attrs['match']} does not match ${vraw}.`);
      } else {
        vraw = tmatch[1];
      }
    }

    vraw = vraw.replace(/\//g, '-');

    if (!semver.valid(vraw)) {
      core.warning(`${vraw} is not a valid semver. More info: https://semver.org/`);
      return version;
    }

    let latest = false;
    const sver = semver.parse(vraw, {
      loose: true
    });
    if (semver.prerelease(vraw)) {
      if (Meta.isRawStatement(tag.attrs['pattern'])) {
        vraw = this.setValue(handlebars.compile(tag.attrs['pattern'])(sver), tag);
      } else {
        vraw = this.setValue(handlebars.compile('{{version}}')(sver), tag);
      }
    } else {
      vraw = this.setValue(handlebars.compile(tag.attrs['pattern'])(sver), tag);
      latest = true;
    }

    return Meta.setVersion(version, vraw, this.flavor.latest == 'auto' ? latest : this.flavor.latest == 'true');
  }

  private procPep440(version: Version, tag: tcl.Tag): Version {
    if (!/^refs\/tags\//.test(this.context.ref) && tag.attrs['value'].length == 0) {
      return version;
    }

    let vraw: string;
    if (tag.attrs['value'].length > 0) {
      vraw = this.setGlobalExp(tag.attrs['value']);
    } else {
      vraw = this.context.ref.replace(/^refs\/tags\//g, '');
    }

    if (tag.attrs['match'].length > 0) {
      const tmatch = vraw.match(tag.attrs['match']);
      if (!tmatch) {
        core.warning(`${tag.attrs['match']} does not match ${vraw}.`);
      } else {
        vraw = tmatch[1];
      }
    }

    vraw = vraw.replace(/\//g, '-');

    if (!pep440.valid(vraw)) {
      core.warning(`${vraw} does not conform to PEP 440. More info: https://www.python.org/dev/peps/pep-0440`);
      return version;
    }

    let latest = false;
    const pver = pep440.explain(vraw);
    if (pver.is_prerelease || pver.is_postrelease || pver.is_devrelease) {
      if (Meta.isRawStatement(tag.attrs['pattern'])) {
        vraw = this.setValue(vraw, tag);
      } else {
        vraw = this.setValue(pep440.clean(vraw), tag);
      }
    } else {
      vraw = this.setValue(
        handlebars.compile(tag.attrs['pattern'])({
          raw: function () {
            return vraw;
          },
          version: function () {
            return pep440.clean(vraw);
          },
          major: function () {
            return pep440.major(vraw);
          },
          minor: function () {
            return pep440.minor(vraw);
          },
          patch: function () {
            return pep440.patch(vraw);
          }
        }),
        tag
      );
      latest = true;
    }

    return Meta.setVersion(version, vraw, this.flavor.latest == 'auto' ? latest : this.flavor.latest == 'true');
  }

  private procMatch(version: Version, tag: tcl.Tag): Version {
    if (!/^refs\/tags\//.test(this.context.ref) && tag.attrs['value'].length == 0) {
      return version;
    }

    let vraw: string;
    if (tag.attrs['value'].length > 0) {
      vraw = this.setGlobalExp(tag.attrs['value']);
    } else {
      vraw = this.context.ref.replace(/^refs\/tags\//g, '');
    }

    let tmatch;
    const isRegEx = tag.attrs['pattern'].match(/^\/(.+)\/(.*)$/);
    if (isRegEx) {
      tmatch = vraw.match(new RegExp(isRegEx[1], isRegEx[2]));
    } else {
      tmatch = vraw.match(tag.attrs['pattern']);
    }
    if (!tmatch) {
      core.warning(`${tag.attrs['pattern']} does not match ${vraw}.`);
      return version;
    }
    if (typeof tmatch[tag.attrs['group']] === 'undefined') {
      core.warning(`Group ${tag.attrs['group']} does not exist for ${tag.attrs['pattern']} pattern.`);
      return version;
    }

    vraw = this.setValue(tmatch[tag.attrs['group']], tag);
    return Meta.setVersion(version, vraw, this.flavor.latest == 'auto' ? true : this.flavor.latest == 'true');
  }

  private procRefBranch(version: Version, tag: tcl.Tag): Version {
    if (!/^refs\/heads\//.test(this.context.ref)) {
      return version;
    }
    const vraw = this.setValue(this.context.ref.replace(/^refs\/heads\//g, ''), tag);
    return Meta.setVersion(version, vraw, this.flavor.latest == 'auto' ? false : this.flavor.latest == 'true');
  }

  private procRefTag(version: Version, tag: tcl.Tag): Version {
    if (!/^refs\/tags\//.test(this.context.ref)) {
      return version;
    }
    const vraw = this.setValue(this.context.ref.replace(/^refs\/tags\//g, ''), tag);
    return Meta.setVersion(version, vraw, this.flavor.latest == 'auto' ? true : this.flavor.latest == 'true');
  }

  private procRefPr(version: Version, tag: tcl.Tag): Version {
    if (!/^refs\/pull\//.test(this.context.ref)) {
      return version;
    }

    const vraw = this.setValue(this.context.ref.replace(/^refs\/pull\//g, '').replace(/\/merge$/g, ''), tag);
    return Meta.setVersion(version, vraw, this.flavor.latest == 'auto' ? false : this.flavor.latest == 'true');
  }

  private procEdge(version: Version, tag: tcl.Tag): Version {
    if (!/^refs\/heads\//.test(this.context.ref)) {
      return version;
    }

    const val = this.context.ref.replace(/^refs\/heads\//g, '');
    if (tag.attrs['branch'].length == 0) {
      tag.attrs['branch'] = this.repo.default_branch;
    }
    if (tag.attrs['branch'] != val) {
      return version;
    }

    const vraw = this.setValue('edge', tag);
    return Meta.setVersion(version, vraw, this.flavor.latest == 'auto' ? false : this.flavor.latest == 'true');
  }

  private procRaw(version: Version, tag: tcl.Tag): Version {
    const vraw = this.setValue(this.setGlobalExp(tag.attrs['value']), tag);
    return Meta.setVersion(version, vraw, this.flavor.latest == 'auto' ? false : this.flavor.latest == 'true');
  }

  private procSha(version: Version, tag: tcl.Tag): Version {
    if (!this.context.sha) {
      return version;
    }

    let val = this.context.sha;
    if (tag.attrs['format'] === tcl.ShaFormat.Short) {
      val = Meta.shortSha(this.context.sha);
    }

    const vraw = this.setValue(val, tag);
    return Meta.setVersion(version, vraw, this.flavor.latest == 'auto' ? false : this.flavor.latest == 'true');
  }

  private static setVersion(version: Version, val: string, latest: boolean): Version {
    if (val.length == 0) {
      return version;
    }
    val = Meta.sanitizeTag(val);
    if (version.main == undefined) {
      version.main = val;
    } else if (val !== version.main) {
      version.partial.push(val);
    }
    if (version.latest == undefined) {
      version.latest = latest;
    }
    return version;
  }

  public static isRawStatement(pattern: string): boolean {
    try {
      const hp = handlebars.parseWithoutProcessing(pattern);
      if (hp.body.length == 1 && hp.body[0].type == 'MustacheStatement') {
        return hp.body[0]['path']['parts'].length == 1 && hp.body[0]['path']['parts'][0] == 'raw';
      }
    } catch {
      return false;
    }
    return false;
  }

  private setValue(val: string, tag: tcl.Tag): string {
    if (Object.prototype.hasOwnProperty.call(tag.attrs, 'prefix')) {
      val = `${this.setGlobalExp(tag.attrs['prefix'])}${val}`;
    } else if (this.flavor.prefix.length > 0) {
      val = `${this.setGlobalExp(this.flavor.prefix)}${val}`;
    }
    if (Object.prototype.hasOwnProperty.call(tag.attrs, 'suffix')) {
      val = `${val}${this.setGlobalExp(tag.attrs['suffix'])}`;
    } else if (this.flavor.suffix.length > 0) {
      val = `${val}${this.setGlobalExp(this.flavor.suffix)}`;
    }
    return val;
  }

  private setGlobalExp(val: string): string {
    const context = this.context;
    const currentDate = this.date;
    const commitDate = this.context.commitDate;
    return handlebars.compile(val)({
      branch: function () {
        if (!/^refs\/heads\//.test(context.ref)) {
          return '';
        }
        return context.ref.replace(/^refs\/heads\//g, '');
      },
      tag: function () {
        if (!/^refs\/tags\//.test(context.ref)) {
          return '';
        }
        return context.ref.replace(/^refs\/tags\//g, '');
      },
      sha: function () {
        return Meta.shortSha(context.sha);
      },
      base_ref: function () {
        if (/^refs\/tags\//.test(context.ref) && context.payload?.base_ref != undefined) {
          return context.payload.base_ref.replace(/^refs\/heads\//g, '');
        }
        // FIXME: keep this for backward compatibility even if doesn't always seem
        //  to return the expected branch. See the comment below.
        if (/^refs\/pull\//.test(context.ref) && context.payload?.pull_request?.base?.ref != undefined) {
          return context.payload.pull_request.base.ref;
        }
        return '';
      },
      commit_date: function (format, options) {
        const m = moment(commitDate);
        let tz = 'UTC';
        Object.keys(options.hash).forEach(key => {
          switch (key) {
            case 'tz':
              tz = options.hash[key];
              break;
            default:
              throw new Error(`Unknown ${key} attribute`);
          }
        });
        return m.tz(tz).format(format);
      },
      is_default_branch: function () {
        const branch = context.ref.replace(/^refs\/heads\//g, '');
        // TODO: "base_ref" is available in the push payload but doesn't always seem to
        //  return the expected branch when the push tag event occurs. It's also not
        //  documented in GitHub docs: https://docs.github.com/en/developers/webhooks-and-events/webhooks/webhook-events-and-payloads#push
        //  more context: https://github.com/docker/metadata-action/pull/192#discussion_r854673012
        // if (/^refs\/tags\//.test(context.ref) && context.payload?.base_ref != undefined) {
        //   branch = context.payload.base_ref.replace(/^refs\/heads\//g, '');
        // }
        if (branch == undefined || branch.length == 0) {
          return 'false';
        }
        if (context.payload?.repository?.default_branch == branch) {
          return 'true';
... [TRUNCATED]
```

### File: src\pep440.d.ts
```ts
interface ExplainedVersion {
  epoch: number;
  release: [number, number, number];
  pre?: [string, number];
  post?: number;
  dev?: number;
  local?: string;
  public: string;
  base_version: string;
  is_prerelease: boolean;
  is_devrelease: boolean;
  is_postrelease: boolean;
}

interface Version {
  epoch: number;
  release: [number, number, number];
  pre?: [string, number] | null;
  post?: [string, number] | null;
  dev?: [string, number] | null;
  local?: Array<number> | null;
  public: string;
  base_version: string;
}

declare module '@renovate/pep440' {
  function valid(version: string): string | null;
  function clean(version: string): string;
  function explain(version: string): ExplainedVersion;
  function major(input: string): string;
  function minor(input: string): string;
  function patch(input: string): string;
  function inc(input: string, release: string, preReleaseIdentifier?: string): string;
}

declare module '@renovate/pep440/lib/version' {
  function stringify(parsed: Version): string;
  function parse(version: string): Version;
}

```

### File: src\tag.ts
```ts
import {parse} from 'csv-parse/sync';
import * as core from '@actions/core';

export enum Type {
  Schedule = 'schedule',
  Semver = 'semver',
  Pep440 = 'pep440',
  Match = 'match',
  Edge = 'edge',
  Ref = 'ref',
  Raw = 'raw',
  Sha = 'sha'
}

export enum RefEvent {
  Branch = 'branch',
  Tag = 'tag',
  PR = 'pr'
}

export enum ShaFormat {
  Short = 'short',
  Long = 'long'
}

export class Tag {
  public type?: Type;
  public attrs: Record<string, string>;

  constructor() {
    this.attrs = {};
  }

  public toString(): string {
    const out: string[] = [`type=${this.type}`];
    for (const attr in this.attrs) {
      out.push(`${attr}=${this.attrs[attr]}`);
    }
    return out.join(',');
  }
}

export const DefaultPriorities: Record<Type, string> = {
  [Type.Schedule]: '1000',
  [Type.Semver]: '900',
  [Type.Pep440]: '900',
  [Type.Match]: '800',
  [Type.Edge]: '700',
  [Type.Ref]: '600',
  [Type.Raw]: '200',
  [Type.Sha]: '100'
};

export function Transform(inputs: string[]): Tag[] {
  const tags: Tag[] = [];
  if (inputs.length == 0) {
    // prettier-ignore
    inputs = [
      `type=schedule`,
      `type=ref,event=${RefEvent.Branch}`,
      `type=ref,event=${RefEvent.Tag}`,
      `type=ref,event=${RefEvent.PR}`
    ];
  }

  for (const input of inputs) {
    tags.push(Parse(input));
  }
  const sorted = tags.sort((tag1, tag2) => {
    if (Number(tag1.attrs['priority']) < Number(tag2.attrs['priority'])) {
      return 1;
    }
    if (Number(tag1.attrs['priority']) > Number(tag2.attrs['priority'])) {
      return -1;
    }
    return 0;
  });

  core.startGroup(`Processing tags input`);
  for (const tag of sorted) {
    core.info(tag.toString());
  }
  core.endGroup();

  return sorted;
}

export function Parse(s: string): Tag {
  const fields = parse(s, {
    relaxColumnCount: true,
    skipEmptyLines: true
  })[0];

  const tag = new Tag();
  for (const field of fields) {
    const parts = field
      .toString()
      .split(/(?<=^[^=]+?)=/)
      .map(item => item.trim());
    if (parts.length == 1) {
      tag.attrs['value'] = parts[0];
    } else {
      const key = parts[0].toLowerCase();
      const value = parts[1];
      switch (key) {
        case 'type': {
          if (!Object.values(Type).includes(value as Type)) {
            throw new Error(`Unknown tag type attribute: ${value}`);
          }
          tag.type = value as Type;
          break;
        }
        default: {
          tag.attrs[key] = value;
          break;
        }
      }
    }
  }

  if (tag.type == undefined) {
    tag.type = Type.Raw;
  }

  switch (tag.type) {
    case Type.Schedule: {
      if (!Object.prototype.hasOwnProperty.call(tag.attrs, 'pattern')) {
        tag.attrs['pattern'] = 'nightly';
      }
      break;
    }
    case Type.Semver:
    case Type.Pep440: {
      if (!Object.prototype.hasOwnProperty.call(tag.attrs, 'pattern')) {
        throw new Error(`Missing pattern attribute for ${s}`);
      }
      if (!Object.prototype.hasOwnProperty.call(tag.attrs, 'value')) {
        tag.attrs['value'] = '';
      }
      if (!Object.prototype.hasOwnProperty.call(tag.attrs, 'match')) {
        tag.attrs['match'] = '';
      }
      break;
    }
    case Type.Match: {
      if (!Object.prototype.hasOwnProperty.call(tag.attrs, 'pattern')) {
        throw new Error(`Missing pattern attribute for ${s}`);
      }
      if (!Object.prototype.hasOwnProperty.call(tag.attrs, 'group')) {
        tag.attrs['group'] = '0';
      }
      if (isNaN(+tag.attrs['group'])) {
        throw new Error(`Invalid match group for ${s}`);
      }
      if (!Object.prototype.hasOwnProperty.call(tag.attrs, 'value')) {
        tag.attrs['value'] = '';
      }
      break;
    }
    case Type.Edge: {
      if (!Object.prototype.hasOwnProperty.call(tag.attrs, 'branch')) {
        tag.attrs['branch'] = '';
      }
      break;
    }
    case Type.Ref: {
      if (!Object.prototype.hasOwnProperty.call(tag.attrs, 'event')) {
        throw new Error(`Missing event attribute for ${s}`);
      }
      if (
        !Object.keys(RefEvent)
          .map(k => RefEvent[k])
          .includes(tag.attrs['event'])
      ) {
        throw new Error(`Invalid event for ${s}`);
      }
      if (tag.attrs['event'] == RefEvent.PR && !Object.prototype.hasOwnProperty.call(tag.attrs, 'prefix')) {
        tag.attrs['prefix'] = 'pr-';
      }
      break;
    }
    case Type.Raw: {
      if (!Object.prototype.hasOwnProperty.call(tag.attrs, 'value')) {
        throw new Error(`Missing value attribute for ${s}`);
      }
      break;
    }
    case Type.Sha: {
      if (!Object.prototype.hasOwnProperty.call(tag.attrs, 'prefix')) {
        tag.attrs['prefix'] = 'sha-';
      }
      if (!Object.prototype.hasOwnProperty.call(tag.attrs, 'format')) {
        tag.attrs['format'] = ShaFormat.Short;
      }
      if (
        !Object.keys(ShaFormat)
          .map(k => ShaFormat[k])
          .includes(tag.attrs['format'])
      ) {
        throw new Error(`Invalid format for ${s}`);
      }
      break;
    }
  }

  if (!Object.prototype.hasOwnProperty.call(tag.attrs, 'enable')) {
    tag.attrs['enable'] = 'true';
  }
  if (!Object.prototype.hasOwnProperty.call(tag.attrs, 'priority')) {
    tag.attrs['priority'] = DefaultPriorities[tag.type];
  }

  return tag;
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

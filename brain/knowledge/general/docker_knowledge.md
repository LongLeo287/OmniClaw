---
id: docker-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:20.461416
---

# KNOWLEDGE EXTRACT: docker
> **Extracted on:** 2026-03-30 17:35:58
> **Source:** docker

---

## File: `build-push-action.md`
```markdown
# 📦 docker/build-push-action [🔖 PENDING/APPROVE]
🔗 https://github.com/docker/build-push-action
🌐 https://github.com/marketplace/actions/build-and-push-docker-images

## Meta
- **Stars:** ⭐ 5216 | **Forks:** 🍴 709
- **Language:** TypeScript | **License:** Apache-2.0
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
GitHub Action to build and push Docker images with Buildx

## README (trích đầu)
```
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

```yam
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `login-action.md`
```markdown
# 📦 docker/login-action [🔖 PENDING/APPROVE]
🔗 https://github.com/docker/login-action
🌐 https://github.com/marketplace/actions/docker-login

## Meta
- **Stars:** ⭐ 1383 | **Forks:** 🍴 283
- **Language:** TypeScript | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
GitHub Action to login against a Docker registry

## README (trích đầu)
```
[![GitHub release](https://img.shields.io/github/release/docker/login-action.svg?style=flat-square)](https://github.com/docker/login-action/releases/latest)
[![GitHub marketplace](https://img.shields.io/badge/marketplace-docker--login-blue?logo=github&style=flat-square)](https://github.com/marketplace/actions/docker-login)
[![CI workflow](https://img.shields.io/github/actions/workflow/status/docker/login-action/ci.yml?branch=master&label=ci&logo=github&style=flat-square)](https://github.com/docker/login-action/actions?workflow=ci)
[![Test workflow](https://img.shields.io/github/actions/workflow/status/docker/login-action/test.yml?branch=master&label=test&logo=github&style=flat-square)](https://github.com/docker/login-action/actions?workflow=test)
[![Codecov](https://img.shields.io/codecov/c/github/docker/login-action?logo=codecov&style=flat-square)](https://codecov.io/gh/docker/login-action)

## About

GitHub Action to login against a Docker registry.

![Screenshot](.github/docker-login.png)

___

* [Usage](#usage)
  * [Docker Hub](#docker-hub)
  * [GitHub Container Registry](#github-container-registry)
  * [GitLab](#gitlab)
  * [Azure Container Registry (ACR)](#azure-container-registry-acr)
  * [Google Container Registry (GCR)](#google-container-registry-gcr)
  * [Google Artifact Registry (GAR)](#google-artifact-registry-gar)
  * [AWS Elastic Container Registry (ECR)](#aws-elastic-container-registry-ecr)
  * [AWS Public Elastic Container Registry (ECR)](#aws-public-elastic-container-registry-ecr)
  * [OCI Oracle Cloud Infrastructure Registry (OCIR)](#oci-oracle-cloud-infrastructure-registry-ocir)
  * [Quay.io](#quayio)
  * [DigitalOcean](#digitalocean-container-registry)
  * [Authenticate to multiple registries](#authenticate-to-multiple-registries)
  * [Set scopes for the authentication token](#set-scopes-for-the-authentication-token)
* [Customizing](#customizing)
  * [inputs](#inputs)
* [Contributing](#contributing)

## Usage

### Docker Hub

When authenticating to [Docker Hub](https://hub.docker.com) with GitHub Actions,
use a [personal access token](https://docs.docker.com/docker-hub/access-tokens/).
Don't use your account password.

```yaml
name: ci

on:
  push:
    branches: main

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to Docker Hub
        uses: docker/login-action@v4
        with:
          username: ${{ vars.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
```

### GitHub Container Registry

To authenticate to the [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry),
use the [`GITHUB_TOKEN`](https://docs.github.com/en/actions/reference/authentication-in-a-workflow)
secret.

```yaml
name: ci

on:
  push:
    branches: main

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to GitHub Container Registry
        uses: docker/login-action@v4
        with:
    
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `metadata-action.md`
```markdown
# 📦 docker/metadata-action [🔖 PENDING/APPROVE]
🔗 https://github.com/docker/metadata-action
🌐 https://github.com/marketplace/actions/docker-metadata-action

## Meta
- **Stars:** ⭐ 1107 | **Forks:** 🍴 151
- **Language:** TypeScript | **License:** Apache-2.0
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
GitHub Action to extract metadata (tags, labels) from Git reference and GitHub events for Docker

## README (trích đầu)
```
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
 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `setup-buildx-action.md`
```markdown
# 📦 docker/setup-buildx-action [🔖 PENDING/APPROVE]
🔗 https://github.com/docker/setup-buildx-action
🌐 https://github.com/marketplace/actions/docker-setup-buildx

## Meta
- **Stars:** ⭐ 1304 | **Forks:** 🍴 231
- **Language:** TypeScript | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
GitHub Action to set up Docker Buildx

## README (trích đầu)
```
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
  * [Max parallelism](https://docs.docker.com/build/ci/github-actions/configure-builder/#max-parallelism): Configure the maximum para
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `setup-qemu-action.md`
```markdown
# 📦 docker/setup-qemu-action [🔖 PENDING/APPROVE]
🔗 https://github.com/docker/setup-qemu-action
🌐 https://github.com/marketplace/actions/docker-setup-qemu

## Meta
- **Stars:** ⭐ 564 | **Forks:** 🍴 93
- **Language:** TypeScript | **License:** Apache-2.0
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
GitHub Action to install QEMU static binaries

## README (trích đầu)
```
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
this project in the [CONTRIBUTING.md](/.
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


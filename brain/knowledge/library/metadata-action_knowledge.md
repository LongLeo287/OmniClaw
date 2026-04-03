---
id: metadata-action-knowledge
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:22.033390
---

# KNOWLEDGE EXTRACT: metadata-action
> **Extracted on:** 2026-03-29 20:54:33
> **Source:** metadata-action

---

## File: `.dockerignore`
```
/coverage

# Dependency directories
node_modules/
jspm_packages/

# yarn v2
.yarn/cache
.yarn/unplugged
.yarn/build-state.yml
.yarn/install-state.gz
.pnp.*
```

## File: `.editorconfig`
```
# This file is for unifying the coding style for different editors and IDEs.
# More information at http://editorconfig.org

root = true

[*]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.md]
trim_trailing_whitespace = false
```

## File: `.gitattributes`
```
/.yarn/releases/** binary
/.yarn/plugins/** binary
/__tests__/fixtures/** -linguist-detectable
/dist/** linguist-generated=true
/lib/** linguist-generated=true
```

## File: `.gitignore`
```
# https://raw.githubusercontent.com/github/gitignore/main/Node.gitignore

# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*
.pnpm-debug.log*

# Diagnostic reports (https://nodejs.org/api/report.html)
report.[0-9]*.[0-9]*.[0-9]*.[0-9]*.json

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Coverage directory used by tools like istanbul
coverage
*.lcov

# Dependency directories
node_modules/
jspm_packages/

# TypeScript cache
*.tsbuildinfo

# Optional npm cache directory
.npm

# Optional eslint cache
.eslintcache

# Yarn Integrity file
.yarn-integrity

# dotenv environment variable files
.env
.env.development.local
.env.test.local
.env.production.local
.env.local

# yarn v2
.yarn/cache
.yarn/unplugged
.yarn/build-state.yml
.yarn/install-state.gz
.pnp.*
```

## File: `.prettierignore`
```
# Dependency directories
node_modules/
jspm_packages/

# yarn v2
.yarn/
```

## File: `.prettierrc.json`
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

## File: `.yarnrc.yml`
```yaml
# https://yarnpkg.com/configuration/yarnrc

compressionLevel: mixed
enableGlobalCache: false
enableHardenedMode: true

logFilters:
  - code: YN0013
    level: discard
  - code: YN0019
    level: discard
  - code: YN0076
    level: discard
  - code: YN0086
    level: discard

nodeLinker: node-modules
```

## File: `action.yml`
```yaml
# https://help.github.com/en/articles/metadata-syntax-for-github-actions
name: 'Docker Metadata action'
description: "GitHub Action to extract metadata (tags, labels) for Docker"
author: 'docker'
branding:
  icon: 'anchor'
  color: 'blue'

inputs:
  context:
    description: 'Where to get context data. Allowed options are "workflow"  (default), "git".'
    default: "workflow"
    required: true
  images:
    description: 'List of Docker images to use as base name for tags'
    required: false
  tags:
    description: 'List of tags as key-value pair attributes'
    required: false
  flavor:
    description: 'Flavors to apply'
    required: false
  labels:
    description: 'List of custom labels'
    required: false
  annotations:
    description: 'List of custom annotations'
    required: false
  sep-tags:
    description: 'Separator to use for tags output (default \n)'
    required: false
  sep-labels:
    description: 'Separator to use for labels output (default \n)'
    required: false
  sep-annotations:
    description: 'Separator to use for annotations output (default \n)'
    required: false
  bake-target:
    description: 'Bake target name (default docker-metadata-action)'
    required: false
  github-token:
    description: 'GitHub Token as provided by secrets'
    default: ${{ github.token }}
    required: true

outputs:
  version:
    description: 'Generated Docker image version'
  tags:
    description: 'Generated Docker tags'
  tag-names:
    description: 'Generated Docker tag names without image base name'
  labels:
    description: 'Generated Docker labels'
  annotations:
    description: 'Generated annotations'
  json:
    description: 'JSON output of tags and labels'
  bake-file-tags:
    description: 'Bake definition file with tags'
  bake-file-labels:
    description: 'Bake definition file with labels'
  bake-file-annotations:
    description: 'Bake definition file with annotations'
  bake-file:
    description: 'Bake definition file with tags and labels'

runs:
  using: 'node24'
  main: 'dist/index.js'
```

## File: `codecov.yml`
```yaml
comment: false
github_checks:
  annotations: false
```

## File: `dev.Dockerfile`
```
# syntax=docker/dockerfile:1

ARG NODE_VERSION=24

FROM node:${NODE_VERSION}-alpine AS base
RUN apk add --no-cache cpio findutils git rsync
WORKDIR /src
RUN --mount=type=bind,target=.,rw \
  --mount=type=cache,target=/src/.yarn/cache <<EOT
  set -e
  corepack enable
  yarn --version
  yarn config set --home enableTelemetry 0
EOT

FROM base AS deps
RUN --mount=type=bind,target=.,rw \
  --mount=type=cache,target=/src/.yarn/cache \
  --mount=type=cache,target=/src/node_modules \
  yarn install && mkdir /vendor && cp yarn.lock /vendor

FROM scratch AS vendor-update
COPY --from=deps /vendor /

FROM deps AS vendor-validate
RUN --mount=type=bind,target=.,rw <<EOT
  set -e
  git add -A
  cp -rf /vendor/* .
  if [ -n "$(git status --porcelain -- yarn.lock)" ]; then
    echo >&2 'ERROR: Vendor result differs. Please vendor your package with "docker buildx bake vendor"'
    git status --porcelain -- yarn.lock
    exit 1
  fi
EOT

FROM deps AS build
RUN --mount=target=/context \
  --mount=type=cache,target=/src/.yarn/cache \
  --mount=type=cache,target=/src/node_modules <<EOT
  set -e
  rsync -a /context/. .
  rm -rf dist
  yarn run build
  mkdir /out
  cp -r dist /out
EOT

FROM scratch AS build-update
COPY --from=build /out /

FROM build AS build-validate
RUN --mount=target=/context \
  --mount=target=.,type=tmpfs <<EOT
  set -e
  rsync -a /context/. .
  git add -A
  rm -rf dist
  cp -rf /out/* .
  if [ -n "$(git status --porcelain -- dist)" ]; then
    echo >&2 'ERROR: Build result differs. Please build first with "docker buildx bake build"'
    git status --porcelain -- dist
    exit 1
  fi
EOT

FROM deps AS format
RUN --mount=type=bind,target=.,rw \
  --mount=type=cache,target=/src/.yarn/cache \
  --mount=type=cache,target=/src/node_modules \
  yarn run format && mkdir /out && find . -name '*.ts' -not -path './node_modules/*' -not -path './.yarn/*' | cpio -pdm /out

FROM scratch AS format-update
COPY --from=format /out /

FROM deps AS lint
RUN --mount=type=bind,target=.,rw \
  --mount=type=cache,target=/src/.yarn/cache \
  --mount=type=cache,target=/src/node_modules \
  yarn run lint

FROM deps AS test
RUN --mount=type=bind,target=.,rw \
  --mount=type=cache,target=/src/.yarn/cache \
  --mount=type=cache,target=/src/node_modules \
  yarn run test --coverage --coverage.reportsDirectory=/tmp/coverage

FROM scratch AS test-coverage
COPY --from=test /tmp/coverage /
```

## File: `docker-bake.hcl`
```
target "_common" {
  args = {
    BUILDKIT_CONTEXT_KEEP_GIT_DIR = 1
  }
}

group "default" {
  targets = ["build"]
}

group "pre-checkin" {
  targets = ["vendor", "format", "build"]
}

group "validate" {
  targets = ["lint", "build-validate", "vendor-validate"]
}

target "build" {
  inherits = ["_common"]
  dockerfile = "dev.Dockerfile"
  target = "build-update"
  output = ["."]
}

target "build-validate" {
  inherits = ["_common"]
  dockerfile = "dev.Dockerfile"
  target = "build-validate"
  output = ["type=cacheonly"]
}

target "format" {
  inherits = ["_common"]
  dockerfile = "dev.Dockerfile"
  target = "format-update"
  output = ["."]
}

target "lint" {
  inherits = ["_common"]
  dockerfile = "dev.Dockerfile"
  target = "lint"
  output = ["type=cacheonly"]
}

target "vendor" {
  inherits = ["_common"]
  dockerfile = "dev.Dockerfile"
  target = "vendor-update"
  output = ["."]
}

target "vendor-validate" {
  inherits = ["_common"]
  dockerfile = "dev.Dockerfile"
  target = "vendor-validate"
  output = ["type=cacheonly"]
}

target "test" {
  inherits = ["_common"]
  dockerfile = "dev.Dockerfile"
  target = "test-coverage"
  output = ["./coverage"]
}
```

## File: `eslint.config.mjs`
```
import {defineConfig} from 'eslint/config';
import js from '@eslint/js';
import tseslint from '@typescript-eslint/eslint-plugin';
import vitest from '@vitest/eslint-plugin';
import globals from 'globals';
import eslintConfigPrettier from 'eslint-config-prettier/flat';
import eslintPluginPrettier from 'eslint-plugin-prettier';

export default defineConfig([
  {
    ignores: ['.yarn/**/*', 'coverage/**/*', 'dist/**/*']
  },
  js.configs.recommended,
  ...tseslint.configs['flat/recommended'],
  eslintConfigPrettier,
  {
    languageOptions: {
      globals: {
        ...globals.node
      }
    }
  },
  {
    files: ['__tests__/**'],
    ...vitest.configs.recommended,
    languageOptions: {
      globals: {
        ...globals.node,
        ...vitest.environments.env.globals
      }
    },
    rules: {
      ...vitest.configs.recommended.rules,
      'vitest/no-conditional-expect': 'error',
      'vitest/no-disabled-tests': 0
    }
  },
  {
    plugins: {
      prettier: eslintPluginPrettier
    },
    rules: {
      'prettier/prettier': 'error',
      '@typescript-eslint/no-require-imports': [
        'error',
        {
          allowAsImport: true
        }
      ]
    }
  }
]);
```

## File: `LICENSE`
```

                                 Apache License
                           Version 2.0, January 2004
                        https://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   Copyright 2013-2018 Docker, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       https://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## File: `package.json`
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

## File: `README.md`
```markdown
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

* `name=<string>` image base name
* `enable=<true|false>` enable this entry (default `true`)

If `images` is empty, tags will be generated without base name.

## `flavor` input

`flavor` defines a global behavior for [`tags`](#tags-input):

```yaml
flavor: |
  latest=auto
  prefix=
  suffix=
```

* `latest=<auto|true|false>`: Handle [latest tag](#latest-tag) (default `auto`)
* `prefix=<string>,onlatest=<true|false>`: A global prefix for each generated
  tag and optionally for `latest`
* `suffix=<string>,onlatest=<true|false>`: A global suffix for each generated
  tag and optionally for `latest`

## `tags` input

`tags` is the core input of this action as everything related to it will
reflect the output metadata. This one is in the form of a key-value pair list
in CSV format to remove limitations intrinsically linked to GitHub Actions
(only string format is handled in the input fields). Here is an example:

```yaml
tags: |
  type=schedule
  type=semver,pattern={{version}}
  type=semver,pattern={{major}}.{{minor}}
  type=semver,pattern={{major}}
  type=ref,event=branch
  type=ref,event=pr
  type=sha
```

Each entry is defined by a `type`, which are:

* [`type=schedule`](#typeschedule)
* [`type=semver`](#typesemver)
* [`type=pep440`](#typepep440)
* [`type=match`](#typematch)
* [`type=edge`](#typeedge)
* [`type=ref`](#typeref)
* [`type=raw`](#typeraw)
* [`type=sha`](#typesha)

And global attributes:

* `enable=<true|false>` enable this entry (default `true`)
* `priority=<number>` set tag [priority](#priority-attribute) order
* `prefix=<string>` add prefix
* `suffix=<string>` add suffix

Default entries if `tags` input is empty:

```yaml
tags: |
  type=schedule
  type=ref,event=branch
  type=ref,event=tag
  type=ref,event=pr
```

### `type=schedule`

```yaml
tags: |
  # minimal
  type=schedule
  # default
  type=schedule,pattern=nightly
  # handlebars
  type=schedule,pattern={{date 'YYYYMMDD'}}
  # handlebars with timezone
  type=schedule,pattern={{date 'YYYYMMDD-HHmmss' tz='Asia/Tokyo'}}
```

Will be used on [schedule event](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule).

`pattern` is a specially crafted attribute to support [Handlebars' template](https://handlebarsjs.com/guide/)
with the following expressions:

* `date 'format' tz='Timezone'` ; render date by its [moment format](https://momentjs.com/docs/#/displaying/format/).
  Default `tz` is UTC.

| Pattern                                      | Output            |
|----------------------------------------------|-------------------|
| `nightly`                                    | `nightly`         |
| `{{date 'YYYYMMDD'}}`                        | `20200110`        |
| `{{date 'YYYYMMDD-HHmmss' tz='Asia/Tokyo'}}` | `20200110-093000` |

Extended attributes and default values:

```yaml
tags: |
  type=schedule,enable=true,priority=1000,prefix=,suffix=,pattern=nightly
```

### `type=semver`

```yaml
tags: |
  # minimal
  type=semver,pattern={{version}}
  # use custom value instead of git tag
  type=semver,pattern={{version}},value=v1.0.0
  # use custom value and match part of it
  type=semver,pattern={{version}},value=p1/v1.0.0,match=v(\d.\d.\d)$
```

Will be used on a [push tag event](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#push)
and requires a valid [semver](https://semver.org/) Git tag, but you can also
use a custom value through `value` attribute.

`pattern` attribute supports [Handlebars template](https://handlebarsjs.com/guide/)
with the following expressions:

* `raw` ; the actual tag
* `version` ; shorthand for `{{major}}.{{minor}}.{{patch}}` (can include pre-release)
* `major` ; major version identifier
* `minor` ; minor version identifier
* `patch` ; patch version identifier

| Git tag          | Pattern               | Match          | Output           |
|------------------|-----------------------|----------------|------------------|
| `v1.2.3`         | `{{raw}}`             |                | `v1.2.3`         |
| `v1.2.3`         | `{{version}}`         |                | `1.2.3`          |
| `v1.2.3`         | `{{major}}.{{minor}}` |                | `1.2`            |
| `v1.2.3`         | `v{{major}}`          |                | `v1`             |
| `v1.2.3`         | `{{minor}}`           |                | `2`              |
| `v1.2.3`         | `{{patch}}`           |                | `3`              |
| `p1/v1.2.3`      | `{{version}}`         | `v(\d.\d.\d)$` | `1.2.3`          |
| `v2.0.8-beta.67` | `{{raw}}`             |                | `v2.0.8-beta.67` |
| `v2.0.8-beta.67` | `{{version}}`         |                | `2.0.8-beta.67`  |
| `v2.0.8-beta.67` | `{{major}}`           |                | `2.0.8-beta.67`* |
| `v2.0.8-beta.67` | `{{major}}.{{minor}}` |                | `2.0.8-beta.67`* |

> [!IMPORTANT]
> *Pre-release (rc, beta, alpha) will only extend `{{version}}` (or `{{raw}}`
> if specified) as tag because they are updated frequently, and contain many
> breaking changes that are (by the author's design) not yet fit for public
> consumption.

Extended attributes and default values:

```yaml
tags: |
  type=semver,enable=true,priority=900,prefix=,suffix=,pattern=,value=,match=
```

### `type=pep440`

```yaml
tags: |
  # minimal
  type=pep440,pattern={{version}}
  # use custom value instead of git tag
  type=pep440,pattern={{version}},value=1.0.0
  # use custom value and match part of it
  type=pep440,pattern={{version}},value=p1/v1.0.0,match=v(\d.\d.\d)$
```

Will be used on a [push tag event](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#push)
and requires a Git tag that conforms to [PEP 440](https://www.python.org/dev/peps/pep-0440/),
but you can also use a custom value through `value` attribute.

`pattern` attribute supports [Handlebars template](https://handlebarsjs.com/guide/)
with the following expressions:

* `raw` ; the actual tag
* `version` ; cleaned version
* `major` ; major version identifier
* `minor` ; minor version identifier
* `patch` ; patch version identifier

| Git tag      | Pattern               | Match          | Output         |
|--------------|-----------------------|----------------|----------------|
| `1.2.3`      | `{{raw}}`             |                | `1.2.3`        |
| `1.2.3`      | `{{version}}`         |                | `1.2.3`        |
| `v1.2.3`     | `{{version}}`         |                | `1.2.3`        |
| `1.2.3`      | `{{major}}.{{minor}}` |                | `1.2`          |
| `1.2.3`      | `v{{major}}`          |                | `v1`           |
| `v1.2.3rc2`  | `{{raw}}`             |                | `v1.2.3rc2`    |
| `1.2.3rc2`   | `{{version}}`         |                | `1.2.3rc2`     |
| `p1/v1.2.3`  | `{{version}}`         | `v(\d.\d.\d)$` | `1.2.3`        |
| `1.2.3rc2`   | `{{major}}.{{minor}}` |                | `1.2.3rc2`*    |
| `1.2.3post1` | `{{major}}.{{minor}}` |                | `1.2.3.post1`* |
| `1.2.3beta2` | `{{major}}.{{minor}}` |                | `1.2.3b2`*     |
| `1.0dev4`    | `{{major}}.{{minor}}` |                | `1.0.dev4`*    |

> [!IMPORTANT]
> *dev/pre/post release will only extend `{{version}}` (or `{{raw}}` if
> specified) as tag because they are updated frequently, and contain many
> breaking changes that are (by the author's design) not yet fit for public
> consumption.

Extended attributes and default values:

```yaml
tags: |
  type=pep440,enable=true,priority=900,prefix=,suffix=,pattern=,value=
```

### `type=match`

```yaml
tags: |
  # minimal
  type=match,pattern=\d.\d.\d
  # define match group
  type=match,pattern=v(.*),group=1
  # use custom value instead of git tag
  type=match,pattern=v(.*),group=1,value=v1.0.0
```

Can create a regular expression for matching Git tag with a pattern and
capturing group. Will be used on a [push tag event](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#push)
but, you can also use a custom value through `value` attribute.

| Git tag                 | Pattern          | Group   | Output                 |
|-------------------------|------------------|---------|------------------------|
| `v1.2.3`                | `\d.\d.\d`       | `0`     | `1.2.3`                |
| `v2.0.8-beta.67`        | `v(.*)`          | `1`     | `2.0.8-beta.67`        |
| `v2.0.8-beta.67`        | `v(\d.\d)`       | `1`     | `2.0`                  |
| `20200110-RC2`          | `\d+`            | `0`     | `20200110`             |
| `p1/v1.2.3`             | `p1/v(\d.\d.\d)` | `1`     | `1.2.3`                |

Extended attributes and default values:

```yaml
tags: |
  type=match,enable=true,priority=800,prefix=,suffix=,pattern=,group=0,value=
```

### `type=edge`

```yaml
tags: |
  # minimal
  type=edge
  # define default branch
  type=edge,branch=main
```

An `edge` tag reflects the last commit of the active branch on your Git
repository. I usually prefer to use `edge` as a Docker tag for a better
distinction or common pattern. This is also used by official images like [Alpine](https://hub.docker.com/_/alpine).

Extended attributes and default values:

```yaml
tags: |
  type=edge,enable=true,priority=700,prefix=,suffix=,branch=$repo.default_branch
```

### `type=ref`

```yaml
tags: |
  # branch event
  type=ref,event=branch
  # tag event
  type=ref,event=tag
  # pull request event
  type=ref,event=pr
```

This type handles Git ref (or reference) for the following events:

* `branch` ; eg. `refs/heads/master`
* `tag` ; eg. `refs/tags/v1.0.0`
* `pr` ; eg. `refs/pull/318/merge`

| Event               | Ref                           | Output           |
|---------------------|-------------------------------|------------------|
| `pull_request`      | `refs/pull/2/merge`           | `pr-2`           |
| `push`              | `refs/heads/master`           | `master`         |
| `push`              | `refs/heads/my/branch`        | `my-branch`      |
| `push tag`          | `refs/tags/v1.2.3`            | `v1.2.3`         |
| `push tag`          | `refs/tags/v2.0.8-beta.67`    | `v2.0.8-beta.67` |
| `workflow_dispatch` | `refs/heads/master`           | `master`         |

Extended attributes and default values:

```yaml
tags: |
  # branch event
  type=ref,enable=true,priority=600,prefix=,suffix=,event=branch
  # tag event
  type=ref,enable=true,priority=600,prefix=,suffix=,event=tag
  # pull request event
  type=ref,enable=true,priority=600,prefix=pr-,suffix=,event=pr
```

### `type=raw`

```yaml
tags: |
  type=raw,value=foo
  type=raw,value=bar
  # or
  type=raw,foo
  type=raw,bar
  # or
  foo
  bar
```

Output custom tags according to your needs.

Extended attributes and default values:

```yaml
tags: |
  type=raw,enable=true,priority=200,prefix=,suffix=,value=
```

### `type=sha`

```yaml
tags: |
  # minimal (short sha)
  type=sha
  # full length sha
  type=sha,format=long
```

Output Git short commit (or long if specified) as Docker tag like
`sha-860c190`.

By default, the length of the short commit SHA is `7` characters. You can
increase this length for larger repositories by setting the
[`DOCKER_METADATA_SHORT_SHA_LENGTH` environment variable](#environment-variables):

```yaml
      -
        name: Docker meta
        id: meta
        uses: docker/metadata-action@v6
        with:
          images: |
            name/app
          tags: |
            type=sha
        env:
          DOCKER_METADATA_SHORT_SHA_LENGTH: 12
```

Extended attributes and default values:

```yaml
tags: |
  type=sha,enable=true,priority=100,prefix=sha-,suffix=,format=short
```

## Notes

### Image name and tag sanitization

In order to comply with [the specification](https://docs.docker.com/engine/reference/commandline/tag/#description),
the image name components may contain lowercase letters, digits and separators.
A separator is defined as a period, one or two underscores, or one or more
dashes. A name component may not start or end with a separator.

A tag name must be a valid ASCII chars sequences and may contain lowercase and
uppercase letters, digits, underscores, periods and dashes. A tag name may not
start with a period or a dash and may contain a maximum of 128 characters.

To ease the integration in your workflow, this action will automatically:

* Lowercase the image name
* Replace invalid chars sequences with `-` for tags

### Latest tag

`latest` tag is handled through the [`flavor` input](#flavor-input). It will be
generated by default (`auto` mode) for:

* [`type=ref,event=tag`](#typeref)
* [`type=semver,pattern=...`](#typesemver)
* [`type=pep440,pattern=...`](#typepep440)
* [`type=match,pattern=...`](#typematch)

For conditionally tagging with latest for a specific branch name, e.g. if your
default branch name is not `master`, use `type=raw` with a boolean expression:

```yaml
tags: |
  # set latest tag for master branch
  type=raw,value=latest,enable=${{ github.ref == format('refs/heads/{0}', 'master') }}
```

You can also use the [`{{is_default_branch}}` global expression](#is_default_branch)
to conditionally tag with latest for the default branch:

```yaml
tags: |
  # set latest tag for default branch
  type=raw,value=latest,enable={{is_default_branch}}
```

### `priority` attribute

`priority=<int>` attribute is used to sort tags in the final list. The higher
the value, the higher the priority. The first tag in the list (higher priority)
will be used as the image version for generated OCI label and [`version` output](#outputs).
Each tags `type` attribute has a default priority:

| Attribute  | Default priority |
|------------|------------------|
| `schedule` | `1000`           |
| `semver`   | `900`            |
| `pep440`   | `900`            |
| `match`    | `800`            |
| `edge`     | `700`            |
| `ref`      | `600`            |
| `raw`      | `200`            |
| `sha`      | `100`            |

### Global expressions

The following [Handlebars' template](https://handlebarsjs.com/guide/) expressions
for `prefix`, `suffix`, `value` and `enable` attributes of `tags` input are
available:

```yaml
tags: |
  # dynamically set the branch name as a prefix
  type=sha,prefix={{branch}}-
  # dynamically set the branch name and sha as a custom tag
  type=raw,value=mytag-{{branch}}-{{sha}}
```

They can also be applied to `labels` and `annotations` inputs:

```yaml
labels: |
  org.opencontainers.image.created={{commit_date 'YYYY-MM-DDTHH:mm:ss.SSS[Z]'}}
```

#### `{{branch}}`

Returns the branch name that triggered the workflow run. Will be empty if not 
a branch reference:

| Event          | Ref                    | Output      |
|----------------|------------------------|-------------|
| `pull_request` | `refs/pull/2/merge`    |             |
| `push`         | `refs/heads/master`    | `master`    |
| `push`         | `refs/heads/my/branch` | `my-branch` |
| `push tag`     | `refs/tags/v1.2.3`     |             |

#### `{{tag}}`

Returns the tag name that triggered the workflow run. Will be empty if not a
tag reference:

| Event           | Ref                           | Output             |
|-----------------|-------------------------------|--------------------|
| `pull_request`  | `refs/pull/2/merge`           |                    |
| `push`          | `refs/heads/master`           |                    |
| `push`          | `refs/heads/my/branch`        |                    |
| `push tag`      | `refs/tags/v1.2.3`            | `v1.2.3`           |

#### `{{sha}}`

Returns the short commit SHA that triggered the workflow run (e.g., `90dd603`).

#### `{{base_ref}}`

Returns the base ref or target branch of the pull request that triggered the
workflow run. Will be empty for a branch reference:

| Event          | Ref                           | Output             |
|----------------|-------------------------------|--------------------|
| `pull_request` | `refs/pull/2/merge`           | `master`           |
| `push`         | `refs/heads/master`           |                    |
| `push`         | `refs/heads/my/branch`        |                    |
| `push tag`*    | `refs/tags/v1.2.3`            | `master`           |

> [!IMPORTANT]
> *`base_ref` is available in the push payload but doesn't always seem to 
> return the expected branch when the push tag event occurs. It's also
> [not documented in GitHub docs](https://docs.github.com/en/developers/webhooks-and-events/webhooks/webhook-events-and-payloads#push).
> We keep it for backward compatibility, but it's **not recommended relying on it**.
> More context in [#192](https://github.com/docker/metadata-action/pull/192#discussion_r854673012). 

#### `{{is_default_branch}}`

Returns `true` if the branch that triggered the workflow run is the default
one, otherwise `false`.

#### `{{is_not_default_branch}}`

Returns `true` if the branch that triggered the workflow run is not the default
one, otherwise `false`.

#### `{{date '<format>' tz='<timezone>'}}`

Returns the current date rendered by its [moment format](https://momentjs.com/docs/#/displaying/format/).
Default `tz` is UTC.

| Expression                                   | Output example                          |
|----------------------------------------------|-----------------------------------------|
| `{{date 'YYYYMMDD'}}`                        | `20200110`                              |
| `{{date 'dddd, MMMM Do YYYY, h:mm:ss a'}}`   | `Friday, January 10th 2020, 3:25:50 pm` |
| `{{date 'YYYYMMDD-HHmmss' tz='Asia/Tokyo'}}` | `20200110-093000`                       |

#### `{{commit_date '<format>' tz='<timezone>'}}`

Returns the date when the current git commit is committed, rendered by its
[moment format](https://momentjs.com/docs/#/displaying/format/). It falls back
to the current date if the commit date is not available.

Default `tz` is UTC.

| Expression                                          | Output example                          |
|-----------------------------------------------------|-----------------------------------------|
| `{{commit_date 'YYYYMMDD'}}`                        | `20200110`                              |
| `{{commit_date 'dddd, MMMM Do YYYY, h:mm:ss a'}}`   | `Friday, January 10th 2020, 3:25:50 pm` |
| `{{commit_date 'YYYYMMDD-HHmmss' tz='Asia/Tokyo'}}` | `20200110-093000`                       |

### Major version zero

Major version zero (`0.y.z`) is for initial development and **may** change at
any time. This means the public API [**should not** be considered stable](https://semver.org/#spec-item-4).

In this case, Docker tag `0` **should not** be generated if you're using [`type=semver`](#typesemver)
with `{{major}}` pattern. You can manage this behavior like this:

```yaml
# refs/tags/v0.1.2
tags: |
  # output 0.1.2
  type=semver,pattern={{version}}
  # output 0.1
  type=semver,pattern={{major}}.{{minor}}
  # disabled if major zero
  type=semver,pattern={{major}},enable=${{ !startsWith(github.ref, 'refs/tags/v0.') }}
```

### JSON output object

The `json` output is a JSON object composed of the generated tags and labels so
that you can reuse them further in your workflow using the [`fromJSON` function](https://docs.github.com/en/actions/learn-github-actions/expressions#fromjson):

```yaml
      -
        name: Docker meta
        uses: docker/metadata-action@v6
        id: meta
        with:
          images: name/app
      -
        name: Build and push
        uses: docker/build-push-action@v7
        with:
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          build-args: |
            BUILDTIME=${{ fromJSON(steps.meta.outputs.json).labels['org.opencontainers.image.created'] }}
            VERSION=${{ fromJSON(steps.meta.outputs.json).labels['org.opencontainers.image.version'] }}
            REVISION=${{ fromJSON(steps.meta.outputs.json).labels['org.opencontainers.image.revision'] }}
```

### Overwrite labels and annotations

If some [OCI Image Format Specification](https://github.com/opencontainers/image-spec/blob/master/annotations.md)
generated are not suitable as labels/annotations, you can overwrite them like
this:

```yaml
      -
        name: Docker meta
        id: meta
        uses: docker/metadata-action@v6
        with:
          images: name/app
          labels: |
            maintainer=CrazyMax
            org.opencontainers.image.title=MyCustomTitle
            org.opencontainers.image.description=Another description
            org.opencontainers.image.vendor=MyCompany
```

### Annotations

Since Buildx 0.12, it is possible to set annotations to your image through the
`--annotation` flag.

With the [`build-push-action`](https://github.com/docker/build-push-action/),
you can set the `annotations` input with the value of the `annotations` output
of the `metadata-action`:

```yaml
      -
        name: Docker meta
        uses: docker/metadata-action@v6
        with:
          images: name/app
      -
        name: Build and push
        uses: docker/build-push-action@v7
        with:
          tags: ${{ steps.meta.outputs.tags }}
          annotations: ${{ steps.meta.outputs.annotations }}
```

The same can be done with the [`bake-action`](https://github.com/docker/bake-action/):

```yaml
      -
        name: Docker meta
        uses: docker/metadata-action@v6
        with:
          images: name/app
      -
        name: Build
        uses: docker/bake-action@v7
        with:
          files: |
            ./docker-bake.hcl
            cwd://${{ steps.meta.outputs.bake-file-tags }}
            cwd://${{ steps.meta.outputs.bake-file-annotations }}
          targets: build
```

Note that annotations can be attached at many different levels within a manifest.
By default, the generated annotations will be attached to image manifests,
but different registries may expect annotations at different places;
a common practice is to read annotations at _image indexes_ if present,
which are often used by multi-arch builds to index platform-specific images.
If you want to specify level(s) for your annotations, you can use the
[`DOCKER_METADATA_ANNOTATIONS_LEVELS` environment variable](#environment-variables)
with a comma separated list of all levels the annotations should be attached to (defaults to `manifest`).
The following configuration demonstrates the ability to attach annotations to both image manifests and image indexes,
though your registry may only need annotations at the index level. (That is, `index` alone may be enough.)
Please consult the documentation of your registry.

```yaml
      -
        name: Docker meta
        uses: docker/metadata-action@v6
        with:
          images: name/app
        env:
          DOCKER_METADATA_ANNOTATIONS_LEVELS: manifest,index
      -
        name: Build and push
        uses: docker/build-push-action@v7
        with:
          tags: ${{ steps.meta.outputs.tags }}
          annotations: ${{ steps.meta.outputs.annotations }}
```

More information about annotations in the [BuildKit documentation](https://github.com/moby/buildkit/blob/master/docs/annotations.md).

## Contributing

Want to contribute? Awesome! You can find information about contributing to
this project in the [CONTRIBUTING.md](/.github/CONTRIBUTING.md)
```

## File: `tsconfig.json`
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

## File: `vitest.config.ts`
```typescript
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

## File: `src/context.ts`
```typescript
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

## File: `src/flavor.ts`
```typescript
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

## File: `src/image.ts`
```typescript
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

## File: `src/main.ts`
```typescript
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

## File: `src/meta.ts`
```typescript
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
        }
        // following events always trigger for last commit on default branch
        // https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows
        if (/create/.test(context.eventName) || /discussion/.test(context.eventName) || /issues/.test(context.eventName) || /schedule/.test(context.eventName)) {
          return 'true';
        }
        return 'false';
      },
      is_not_default_branch: function () {
        return this.is_default_branch() === 'false' ? 'true' : 'false';
      },
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
      }
    });
  }

  private getImageNames(): Array<string> {
    const images: Array<string> = [];
    for (const image of this.images) {
      if (!image.enable) {
        continue;
      }
      images.push(Meta.sanitizeImageName(image.name));
    }
    return images;
  }

  public getTags(namesOnly?: boolean): Array<string> {
    if (!this.version.main) {
      return [];
    }
    if (namesOnly) {
      return this.generateTags(this.version.main);
    }

    const tags: Array<string> = [];
    const images = this.getImageNames();
    if (images.length > 0) {
      for (const imageName of images) {
        tags.push(...this.generateTags(this.version.main, imageName));
      }
    } else {
      tags.push(...this.generateTags(this.version.main));
    }

    return tags;
  }

  private generateTags(version: string, imageName?: string): Array<string> {
    const tags: Array<string> = [];
    const prefix = imageName ? `${imageName}:` : '';
    tags.push(`${prefix}${version}`);
    for (const partial of this.version.partial) {
      tags.push(`${prefix}${partial}`);
    }
    if (this.version.latest) {
      const latestTag = `${this.flavor.prefixLatest ? this.flavor.prefix : ''}latest${this.flavor.suffixLatest ? this.flavor.suffix : ''}`;
      tags.push(`${prefix}${Meta.sanitizeTag(latestTag)}`);
    }
    return tags;
  }

  public getLabels(): Array<string> {
    return this.getOCIAnnotationsWithCustoms(this.inputs.labels);
  }

  public getAnnotations(): Array<string> {
    return this.getOCIAnnotationsWithCustoms(this.inputs.annotations);
  }

  private getOCIAnnotationsWithCustoms(extra: string[]): Array<string> {
    const res: Array<string> = [
      `org.opencontainers.image.title=${this.repo.name || ''}`,
      `org.opencontainers.image.description=${this.repo.description || ''}`,
      `org.opencontainers.image.url=${this.repo.html_url || ''}`,
      `org.opencontainers.image.source=${this.repo.html_url || ''}`,
      `org.opencontainers.image.version=${this.version.main || ''}`,
      `org.opencontainers.image.created=${this.date.toISOString()}`,
      `org.opencontainers.image.revision=${this.context.sha || ''}`,
      `org.opencontainers.image.licenses=${this.repo.license?.spdx_id || ''}`
    ];
    extra.forEach(label => {
      res.push(this.setGlobalExp(label));
    });

    return Array.from(
      new Map<string, string>(
        res
          .map(label => label.split('='))
          // eslint-disable-next-line @typescript-eslint/no-unused-vars
          .filter(([_key, ...values]) => values.length > 0)
          .map(([key, ...values]) => [key, values.join('=')] as [string, string])
      )
    )
      .sort((a, b) => a[0].localeCompare(b[0]))
      .map(([key, value]) => `${key}=${value}`);
  }

  public getJSON(alevels: string[]): unknown {
    const annotations: Array<string> = [];
    for (const level of alevels) {
      annotations.push(...this.getAnnotations().map(label => `${level}:${label}`));
    }
    return {
      tags: this.getTags(),
      'tag-names': this.getTags(true),
      labels: this.getLabels().reduce((res, label) => {
        const matches = label.match(/([^=]*)=(.*)/);
        if (!matches) {
          return res;
        }
        res[matches[1]] = matches[2];
        return res;
      }, {}),
      annotations: annotations
    };
  }

  public getBakeFile(kind: string): string {
    if (kind == 'tags') {
      return this.generateBakeFile(
        {
          tags: this.getTags(),
          args: {
            DOCKER_META_IMAGES: this.getImageNames().join(','),
            DOCKER_META_VERSION: this.version.main
          }
        },
        kind
      );
    } else if (kind == 'labels') {
      return this.generateBakeFile(
        {
          labels: this.getLabels().reduce((res, label) => {
            const matches = label.match(/([^=]*)=(.*)/);
            if (!matches) {
              return res;
            }
            res[matches[1]] = matches[2];
            return res;
          }, {})
        },
        kind
      );
    } else if (kind.startsWith('annotations:')) {
      const name = kind.split(':')[0];
      const annotations: Array<string> = [];
      for (const level of kind.split(':')[1].split(',')) {
        annotations.push(...this.getAnnotations().map(label => `${level}:${label}`));
      }
      return this.generateBakeFile(
        {
          annotations: annotations
        },
        name
      );
    }
    throw new Error(`Unknown bake file type: ${kind}`);
  }

  public getBakeFileTagsLabels(): string {
    return this.generateBakeFile({
      tags: this.getTags(),
      labels: this.getLabels().reduce((res, label) => {
        const matches = label.match(/([^=]*)=(.*)/);
        if (!matches) {
          return res;
        }
        res[matches[1]] = matches[2];
        return res;
      }, {}),
      args: {
        DOCKER_META_IMAGES: this.getImageNames().join(','),
        DOCKER_META_VERSION: this.version.main
      }
    });
  }

  private generateBakeFile(dt, suffix?: string): string {
    const bakeFile = path.join(ToolkitContext.tmpDir(), `docker-metadata-action-bake${suffix ? `-${suffix}` : ''}.json`);
    fs.writeFileSync(bakeFile, JSON.stringify({target: {[this.inputs.bakeTarget]: dt}}, null, 2));
    return bakeFile;
  }

  private static sanitizeImageName(name: string): string {
    return name.toLowerCase();
  }

  private static sanitizeTag(tag: string): string {
    return tag.replace(/[^a-zA-Z0-9._-]+/g, '-');
  }

  private static shortSha(sha: string): string {
    let shortShaLength = defaultShortShaLength;
    if (process.env.DOCKER_METADATA_SHORT_SHA_LENGTH) {
      if (isNaN(Number(process.env.DOCKER_METADATA_SHORT_SHA_LENGTH))) {
        throw new Error(`DOCKER_METADATA_SHORT_SHA_LENGTH is not a valid number: ${process.env.DOCKER_METADATA_SHORT_SHA_LENGTH}`);
      }
      shortShaLength = Number(process.env.DOCKER_METADATA_SHORT_SHA_LENGTH);
    }
    if (shortShaLength >= sha.length) {
      return sha;
    }
    return sha.substring(0, shortShaLength);
  }
}
```

## File: `src/pep440.d.ts`
```typescript
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

## File: `src/tag.ts`
```typescript
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

## File: `test/docker-bake.hcl`
```
target "docker-metadata-action" {}

group "default" {
  targets = ["db", "app"]
}

group "release" {
  targets = ["db", "app-plus"]
}

target "db" {
  context = "./test"
  tags = ["docker.io/tonistiigi/db"]
}

target "app" {
  inherits = ["docker-metadata-action"]
  context = "./test"
  dockerfile = "Dockerfile"
  args = {
    name = "foo"
  }
}

target "cross" {
  platforms = [
    "linux/amd64",
    "linux/arm64",
    "linux/386"
  ]
}

target "app-plus" {
  inherits = ["app", "cross"]
  args = {
    IAMPLUS = "true"
  }
}
```

## File: `test/Dockerfile`
```
# syntax=docker/dockerfile:1
FROM alpine
RUN echo "Hello world!"
```

## File: `test/output.Dockerfile`
```
# syntax=docker/dockerfile:1
FROM alpine
RUN apk add --no-cache coreutils jq
ARG DOCKER_METADATA_OUTPUT_VERSION
ARG DOCKER_METADATA_OUTPUT_TAGS
ARG DOCKER_METADATA_OUTPUT_LABELS
ARG DOCKER_METADATA_OUTPUT_ANNOTATIONS
ARG DOCKER_METADATA_OUTPUT_JSON
RUN printenv DOCKER_METADATA_OUTPUT_VERSION
RUN printenv DOCKER_METADATA_OUTPUT_TAGS
RUN printenv DOCKER_METADATA_OUTPUT_LABELS
RUN printenv DOCKER_METADATA_OUTPUT_ANNOTATIONS
RUN printenv DOCKER_METADATA_OUTPUT_JSON
RUN echo $DOCKER_METADATA_OUTPUT_JSON | jq
```

## File: `__tests__/context.test.ts`
```typescript
import {beforeEach, describe, expect, test, it, vi} from 'vitest';
import {Git} from '@docker/actions-toolkit/lib/git.js';
import {Toolkit} from '@docker/actions-toolkit/lib/toolkit.js';

import * as context from '../src/context.js';

const toolkit = new Toolkit({githubToken: 'fake-github-token'});

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
        ['images', 'moby/buildkit\nghcr.io/moby/mbuildkit'],
      ]),
      {
        context: context.ContextSource.workflow,
        bakeTarget: 'docker-metadata-action',
        flavor: [],
        githubToken: '',
        images: ['moby/buildkit', 'ghcr.io/moby/mbuildkit'],
        labels: [],
        annotations: [],
        sepLabels: '\n',
        sepTags: '\n',
        sepAnnotations: '\n',
        tags: [],
      }
    ],
    [
      1,
      new Map<string, string>([
        ['bake-target', 'metadata'],
        ['images', 'moby/buildkit'],
        ['sep-labels', ','],
        ['sep-tags', ','],
        ['sep-annotations', ',']
      ]),
      {
        context: context.ContextSource.workflow,
        bakeTarget: 'metadata',
        flavor: [],
        githubToken: '',
        images: ['moby/buildkit'],
        labels: [],
        annotations: [],
        sepLabels: ',',
        sepTags: ',',
        sepAnnotations: ',',
        tags: [],
      }
    ],
    [
      2,
      new Map<string, string>([
        ['images', 'moby/buildkit\n#comment\nghcr.io/moby/mbuildkit'],
      ]),
      {
        context: context.ContextSource.workflow,
        bakeTarget: 'docker-metadata-action',
        flavor: [],
        githubToken: '',
        images: ['moby/buildkit', 'ghcr.io/moby/mbuildkit'],
        labels: [],
        annotations: [],
        sepLabels: '\n',
        sepTags: '\n',
        sepAnnotations: '\n',
        tags: [],
      }
    ],
    [
      3,
      new Map<string, string>([
        ['labels', 'mylabel=foo#bar\n#comment\nanother=bar'],
      ]),
      {
        context: context.ContextSource.workflow,
        bakeTarget: 'docker-metadata-action',
        flavor: [],
        githubToken: '',
        images: [],
        labels: ['mylabel=foo#bar', 'another=bar'],
        annotations: [],
        sepLabels: '\n',
        sepTags: '\n',
        sepAnnotations: '\n',
        tags: [],
      }
    ],
    [
      4,
      new Map<string, string>([
        ['annotations', 'org.opencontainers.image.url=https://example.com/path#readme\n#comment\norg.opencontainers.image.source=https://github.com/docker/metadata-action'],
      ]),
      {
        context: context.ContextSource.workflow,
        bakeTarget: 'docker-metadata-action',
        flavor: [],
        githubToken: '',
        images: [],
        labels: [],
        annotations: [
          'org.opencontainers.image.url=https://example.com/path#readme',
          'org.opencontainers.image.source=https://github.com/docker/metadata-action'
        ],
        sepLabels: '\n',
        sepTags: '\n',
        sepAnnotations: '\n',
        tags: [],
      }
    ],
    [
      5,
      new Map<string, string>([
        ['tags', 'type=raw,value=foo#bar\n#comment'],
        ['flavor', 'prefix=v#1\n#comment'],
      ]),
      {
        context: context.ContextSource.workflow,
        bakeTarget: 'docker-metadata-action',
        flavor: ['prefix=v#1'],
        githubToken: '',
        images: [],
        labels: [],
        annotations: [],
        sepLabels: '\n',
        sepTags: '\n',
        sepAnnotations: '\n',
        tags: ['type=raw,value=foo#bar'],
      }
    ],
  ];
  test.each(cases)('[%d] given %o as inputs, returns %o', async (num: number, inputs: Map<string, string>, expected: context.Inputs) => {
    inputs.forEach((value: string, name: string) => {
      setInput(name, value);
    });
    const res = await context.getInputs();
    expect(res).toEqual(expected);
  });
});

describe('getContext', () => {
  it('workflow', async () => {
    const ctx = await context.getContext(context.ContextSource.workflow, toolkit);
    expect(ctx.ref).toEqual('refs/heads/dev');
    expect(ctx.sha).toEqual('5f3331d7f7044c18ca9f12c77d961c4d7cf3276a');
    expect(ctx.commitDate).toEqual(new Date('2024-11-13T13:42:28.000Z'));
  });
  it('git', async () => {
    vi.spyOn(Git, 'context').mockImplementation((): Promise<context.Context> => {
      return Promise.resolve({
        ref: 'refs/heads/git-test',
        sha: 'git-test-sha'
      } as context.Context);
    });
    vi.spyOn(Git, 'commitDate').mockImplementation(async (): Promise<Date> => {
      return new Date('2023-01-01T13:42:28.000Z');
    });
    const ctx = await context.getContext(context.ContextSource.git, toolkit);
    expect(ctx.ref).toEqual('refs/heads/git-test');
    expect(ctx.sha).toEqual('git-test-sha');
    expect(ctx.commitDate).toEqual(new Date('2023-01-01T13:42:28.000Z'));
  });
});

// See: https://github.com/actions/toolkit/blob/master/packages/core/src/core.ts#L67
function getInputName(name: string): string {
  return `INPUT_${name.replace(/ /g, '_').toUpperCase()}`;
}

function setInput(name: string, value: string): void {
  process.env[getInputName(name)] = value;
}
```

## File: `__tests__/flavor.test.ts`
```typescript
import {describe, expect, test} from 'vitest';

import {Flavor, Transform} from '../src/flavor.js';

describe('transform', () => {
  // prettier-ignore
  test.each([
    [
      [
        `randomstr`,
        `latest=auto`
      ],
      {} as Flavor,
      true
    ],
    [
      [
        `unknwown=foo`
      ],
      {} as Flavor,
      true
    ],
    [
      [
        `latest`,
      ],
      {} as Flavor,
      true
    ],
    [
      [
        `latest=true`
      ],
      {
        latest: "true",
        prefix: "",
        prefixLatest: false,
        suffix: "",
        suffixLatest: false,
      } as Flavor,
      false
    ],
    [
      [
        `latest=false`
      ],
      {
        latest: "false",
        prefix: "",
        prefixLatest: false,
        suffix: "",
        suffixLatest: false,
      } as Flavor,
      false
    ],
    [
      [
        `latest=auto`
      ],
      {
        latest: "auto",
        prefix: "",
        prefixLatest: false,
        suffix: "",
        suffixLatest: false,
      } as Flavor,
      false
    ],
    [
      [
        `latest=foo`
      ],
      {} as Flavor,
      true
    ],
    [
      [
        `prefix=sha-`
      ],
      {
        latest: "auto",
        prefix: "sha-",
        prefixLatest: false,
        suffix: "",
        suffixLatest: false,
      } as Flavor,
      false
    ],
    [
      [
        `suffix=-alpine`
      ],
      {
        latest: "auto",
        prefix: "",
        prefixLatest: false,
        suffix: "-alpine",
        suffixLatest: false,
      } as Flavor,
      false
    ],
    [
      [
        `latest=false`,
        `prefix=dev-`,
        `suffix=-alpine`
      ],
      {
        latest: "false",
        prefix: "dev-",
        prefixLatest: false,
        suffix: "-alpine",
        suffixLatest: false,
      } as Flavor,
      false
    ],
    [
      [
        `prefix=dev-,onlatest=true`,
      ],
      {
        latest: "auto",
        prefix: "dev-",
        prefixLatest: true,
        suffix: "",
        suffixLatest: false,
      } as Flavor,
      false
    ],
    [
      [
        `suffix=-alpine,onlatest=true`,
      ],
      {
        latest: "auto",
        prefix: "",
        prefixLatest: false,
        suffix: "-alpine",
        suffixLatest: true,
      } as Flavor,
      false
    ],
    [
      [
        `prefix=dev-,onlatest=true`,
        `suffix=-alpine,onlatest=true`,
      ],
      {
        latest: "auto",
        prefix: "dev-",
        prefixLatest: true,
        suffix: "-alpine",
        suffixLatest: true,
      } as Flavor,
      false
    ],
    [
      [
        `prefix= `,
      ],
      {
        latest: "auto",
        prefix: "",
        prefixLatest: false,
        suffix: "",
        suffixLatest: false,
      } as Flavor,
      false
    ]
  ])('given %p attributes', async (inputs: string[], expected: Flavor, invalid: boolean) => {
    try {
      const flavor = Transform(inputs);
      expect(flavor).toEqual(expected);
    } catch (err) {
      if (!invalid) {
        console.error(err);
      }
      // eslint-disable-next-line vitest/no-conditional-expect
      expect(true).toBe(invalid);
    }
  });
});
```

## File: `__tests__/image.test.ts`
```typescript
import {describe, expect, test} from 'vitest';

import {Transform, Image} from '../src/image.js';

describe('transform', () => {
  // prettier-ignore
  test.each([
    [
      [
        `name/foo`
      ],
      [
        {
          name: `name/foo`,
          enable: true,
        }
      ] as Image[],
      false
    ],
    [
      [
        `name/foo,name/bar`
      ],
      [
        {
          name: `name/foo`,
          enable: true,
        },
        {
          name: `name/bar`,
          enable: true,
        }
      ] as Image[],
      false
    ],
    [
      [
        `name/foo`,
        `name/bar`
      ],
      [
        {
          name: `name/foo`,
          enable: true,
        },
        {
          name: `name/bar`,
          enable: true,
        }
      ] as Image[],
      false
    ],
    [
      [
        `name=name/bar`,
        `name/foo,enable=false`,
        `name=ghcr.io/UserName/Foo,enable=true`
      ],
      [
        {
          name: `name/bar`,
          enable: true,
        },
        {
          name: `name/foo`,
          enable: false,
        },
        {
          name: `ghcr.io/UserName/Foo`,
          enable: true,
        },
      ] as Image[],
      false
    ],
    [
      [`value=name/foo`], undefined, true
    ],
    [
      [`name/foo,enable=bar`], undefined, true
    ],
    [
      [`name/foo,bar=baz`], undefined, true
    ],
    [
      [`name=,enable=true`], undefined, true
    ],
    [
      [`name/foo,name=name/bar,enable=true`], undefined, true
    ]
  ])('given %p', async (l: string[], expected: Image[] | undefined, invalid: boolean) => {
    try {
      const images = Transform(l);
      expect(images).toEqual(expected);
    } catch (err) {
      if (!invalid) {
        console.error(err);
      }
      // eslint-disable-next-line vitest/no-conditional-expect
      expect(true).toBe(invalid);
    }
  });
});
```

## File: `__tests__/meta.test.ts`
```typescript
import {beforeEach, describe, expect, test, vi} from 'vitest';
import * as fs from 'fs';
import * as path from 'path';
import * as dotenv from 'dotenv';

import {GitHub} from '@docker/actions-toolkit/lib/github/github.js';
import {Toolkit} from '@docker/actions-toolkit/lib/toolkit.js';
import {GitHubRepo} from '@docker/actions-toolkit/lib/types/github/github.js';

import {ContextSource, getContext, getInputs, Inputs} from '../src/context.js';
import type {Context as MetadataContext} from '../src/context.js';
import {Meta, Version} from '../src/meta.js';

import repoFixture from './fixtures/repo.json' with {type: 'json'};

vi.spyOn(GitHub.prototype, 'repoData').mockImplementation((): Promise<GitHubRepo> => {
  return <Promise<GitHubRepo>>(repoFixture as unknown);
});

vi.spyOn(global.Date.prototype, 'toISOString').mockImplementation(() => {
  return '2020-01-10T00:30:00.000Z';
});

vi.mock('moment-timezone', async () => {
  const actual = await vi.importActual<unknown>('moment-timezone');
  const actualModule = actual as {default?: (input?: string | Date) => unknown};
  const momentTimezone = (typeof actual === 'function' ? actual : actualModule.default) as (input?: string | Date) => unknown;
  return {
    __esModule: true,
    default: () => momentTimezone('2020-01-10T00:30:00.000Z')
  };
});

beforeEach(() => {
  vi.clearAllMocks();
  Object.keys(process.env).forEach(function (key) {
    if (key !== 'GITHUB_TOKEN' && key.startsWith('GITHUB_')) {
      delete process.env[key];
    }
  });
  vi.spyOn(GitHub, 'context', 'get').mockImplementation((): MetadataContext => {
    const repository = process.env.GITHUB_REPOSITORY || 'docker/repo';
    const [owner, repo] = repository.includes('/') ? repository.split('/', 2) : ['docker', 'repo'];
    const eventPath = process.env.GITHUB_EVENT_PATH;
    const payload = eventPath && fs.existsSync(eventPath) ? JSON.parse(fs.readFileSync(eventPath, 'utf8')) : {};
    return {
      payload,
      eventName: process.env.GITHUB_EVENT_NAME || '',
      sha: process.env.GITHUB_SHA || '',
      ref: process.env.GITHUB_REF || '',
      workflow: process.env.GITHUB_WORKFLOW || '',
      action: process.env.GITHUB_ACTION || '',
      actor: process.env.GITHUB_ACTOR || '',
      job: process.env.GITHUB_JOB || '',
      runAttempt: +(process.env.GITHUB_RUN_ATTEMPT || 1),
      runNumber: +(process.env.GITHUB_RUN_NUMBER || 0),
      runId: +(process.env.GITHUB_RUN_ID || 0),
      apiUrl: process.env.GITHUB_API_URL || 'https://api.github.com',
      serverUrl: process.env.GITHUB_SERVER_URL || 'https://github.com',
      graphqlUrl: process.env.GITHUB_GRAPHQL_URL || 'https://api.github.com/graphql',
      repo: {owner, repo}
    } as MetadataContext;
  });
});

describe('isRawStatement', () => {
  // prettier-ignore
  test.each([
    ['{{ raw }}.{{ version }}', false],
    ['{{ version }},{{raw }.', false],
    ['{{ raw }}', true],
    ['{{ raw}}', true],
    ['{{raw}}', true],
  ])('given %o pattern', async (pattern: string, expected: boolean) => {
    expect(Meta.isRawStatement(pattern)).toEqual(expected);
  });
});

const tagsLabelsTest = async (name: string, envFile: string, inputs: Inputs, exVersion: Version, exTags: Array<string>, exLabels: Array<string>, exAnnotations: Array<string> | undefined) => {
  process.env = dotenv.parse(fs.readFileSync(path.join(__dirname, 'fixtures', envFile)));
  const toolkit = new Toolkit();
  const repo = await toolkit.github.repoData();
  const meta = new Meta({...getInputs(), ...inputs}, await getContext(ContextSource.workflow, toolkit), repo);

  const version = meta.version;
  expect(version).toEqual(exVersion);

  const tags = meta.getTags();
  expect(tags).toEqual(exTags);

  const labels = meta.getLabels();
  expect(labels).toEqual(exLabels);

  const annotations = meta.getAnnotations();
  expect(annotations).toEqual(exAnnotations ?? exLabels);
};

describe('null', () => {
  // prettier-ignore
  // eslint-disable-next-line vitest/expect-expect
  test.each([
    [
      'null01',
      'event_null.env',
      {
        images: ['user/app'],
      } as Inputs,
      {
        main: undefined,
        partial: [],
        latest: false
      } as Version,
      [],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version="
      ],
      undefined
    ],
    [
      'null02',
      'event_empty.env',
      {
        images: ['user/app'],
        tags: [
          `type=sha`,
          `type=raw,{{branch}}`,
        ]
      } as Inputs,
      {
        main: undefined,
        partial: [],
        latest: false
      } as Version,
      [],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version="
      ],
      undefined
    ],
  ])('given %o with %o event', tagsLabelsTest);
});

describe('push', () => {
  // prettier-ignore
  // eslint-disable-next-line vitest/expect-expect
  test.each([
    [
      'push01',
      'event_push_dev.env',
      {
        images: ['user/app'],
      } as Inputs,
      {
        main: 'dev',
        partial: [],
        latest: false
      } as Version,
      [
        'user/app:dev'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=dev"
      ],
      undefined
    ],
    [
      'push02',
      'event_push_master.env',
      {
        images: ['user/app'],
        tags: [
          `type=edge`
        ],
      } as Inputs,
      {
        main: 'edge',
        partial: [],
        latest: false
      } as Version,
      [
        'user/app:edge'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=266574110acf203503badf966df2ea24b5d732d7",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=edge"
      ],
      undefined
    ],
    [
      'push03',
      'event_push_master.env',
      {
        images: ['user/app'],
      } as Inputs,
      {
        main: 'master',
        partial: [],
        latest: false
      } as Version,
      [
        'user/app:master'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=266574110acf203503badf966df2ea24b5d732d7",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=master"
      ],
      undefined
    ],
    [
      'push04',
      'event_workflow_dispatch.env',
      {
        images: ['user/app'],
        tags: [
          `type=edge`
        ],
      } as Inputs,
      {
        main: 'edge',
        partial: [],
        latest: false
      } as Version,
      [
        'user/app:edge'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=edge"
      ],
      undefined
    ],
    [
      'push05',
      'event_push_dev.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
      } as Inputs,
      {
        main: 'dev',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:dev',
        'ghcr.io/user/app:dev'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=dev"
      ],
      undefined
    ],
    [
      'push06',
      'event_push_master.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=edge`
        ],
      } as Inputs,
      {
        main: 'edge',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:edge',
        'ghcr.io/user/app:edge'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=266574110acf203503badf966df2ea24b5d732d7",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=edge"
      ],
      undefined
    ],
    [
      'push07',
      'event_push_dev.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=ref,event=branch`,
          `type=sha`
        ],
      } as Inputs,
      {
        main: 'dev',
        partial: ['sha-860c190'],
        latest: false
      } as Version,
      [
        'org/app:dev',
        'org/app:sha-860c190',
        'ghcr.io/user/app:dev',
        'ghcr.io/user/app:sha-860c190'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=dev"
      ],
      undefined
    ],
    [
      'push08',
      'event_push_master.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=edge`,
          `type=sha`
        ],
      } as Inputs,
      {
        main: 'edge',
        partial: ['sha-2665741'],
        latest: false
      } as Version,
      [
        'org/app:edge',
        'org/app:sha-2665741',
        'ghcr.io/user/app:edge',
        'ghcr.io/user/app:sha-2665741'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=266574110acf203503badf966df2ea24b5d732d7",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=edge"
      ],
      undefined
    ],
    [
      'push09',
      'event_push_dev.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=edge,branch=dev`,
          `type=sha`
        ],
      } as Inputs,
      {
        main: 'edge',
        partial: ['sha-860c190'],
        latest: false
      } as Version,
      [
        'org/app:edge',
        'org/app:sha-860c190',
        'ghcr.io/user/app:edge',
        'ghcr.io/user/app:sha-860c190'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=edge"
      ],
      undefined
    ],
    [
      'push10',
      'event_push_master.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=edge,branch=dev`,
          `type=sha`
        ],
      } as Inputs,
      {
        main: 'sha-2665741',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:sha-2665741',
        'ghcr.io/user/app:sha-2665741'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=266574110acf203503badf966df2ea24b5d732d7",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=sha-2665741"
      ],
      undefined
    ],
    [
      'push11',
      'event_push_invalidchars.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=edge`,
          `type=sha`
        ],
      } as Inputs,
      {
        main: 'sha-983315b',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:sha-983315b',
        'ghcr.io/user/app:sha-983315b'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=983315b5e8d46e46fc4c49869e85e7ee5fb289ba",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=sha-983315b"
      ],
      undefined
    ],
    [
      'push12',
      'event_push_invalidchars.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=semver,pattern={{version}}`,
          `type=pep440,pattern={{version}}`,
          `type=edge`
        ],
      } as Inputs,
      {
        main: undefined,
        partial: [],
        latest: false
      } as Version,
      [],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=983315b5e8d46e46fc4c49869e85e7ee5fb289ba",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version="
      ],
      undefined
    ],
    [
      'push13',
      'event_push_master.env',
      {
        images: ['user/app'],
        tags: [
          `type=ref,priority=2000,event=branch`,
          `type=edge`
        ],
      } as Inputs,
      {
        main: 'master',
        partial: ['edge'],
        latest: false
      } as Version,
      [
        'user/app:master',
        'user/app:edge'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=266574110acf203503badf966df2ea24b5d732d7",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=master"
      ],
      undefined
    ],
    [
      'push14',
      'event_push_master.env',
      {
        images: ['user/app'],
        tags: [
          `type=semver,pattern={{version}},value=v1.2.3`,
          `type=pep440,pattern={{version}},value=v1.2.3`,
          `type=edge`
        ],
      } as Inputs,
      {
        main: '1.2.3',
        partial: ['edge'],
        latest: true
      } as Version,
      [
        'user/app:1.2.3',
        'user/app:edge',
        'user/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=266574110acf203503badf966df2ea24b5d732d7",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=1.2.3"
      ],
      undefined
    ],
    [
      'push15',
      'event_push_master.env',
      {
        images: ['user/app'],
        tags: [
          `type=match,pattern=v(.*),group=1,value=v1.2.3`,
          `type=edge`
        ],
      } as Inputs,
      {
        main: '1.2.3',
        partial: ['edge'],
        latest: true
      } as Version,
      [
        'user/app:1.2.3',
        'user/app:edge',
        'user/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=266574110acf203503badf966df2ea24b5d732d7",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=1.2.3"
      ],
      undefined
    ],
    [
      'push16',
      'event_push_master.env',
      {
        images: ['user/app'],
        tags: [
          `type=match,enable=false,pattern=v(.*),group=1,value=v1.2.3`,
          `type=edge`
        ],
      } as Inputs,
      {
        main: 'edge',
        partial: [],
        latest: false
      } as Version,
      [
        'user/app:edge'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=266574110acf203503badf966df2ea24b5d732d7",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=edge"
      ],
      undefined
    ],
    [
      'push17',
      'event_push_master.env',
      {
        images: ['user/app'],
        tags: [
          `type=raw,value=mytag-{{branch}}`,
          `type=raw,value=mytag-{{date 'YYYYMMDD'}}`,
          `type=raw,value=mytag-cd-{{commit_date 'YYYYMMDD'}}`,
          `type=raw,value=mytag-{{date 'YYYYMMDD-HHmmss' tz='Asia/Tokyo'}}`,
          `type=raw,value=mytag-tag-{{tag}}`,
          `type=raw,value=mytag-baseref-{{base_ref}}`,
          `type=raw,value=mytag-defbranch,enable={{is_default_branch}}`
        ],
      } as Inputs,
      {
        main: 'mytag-master',
        partial: [
          'mytag-20200110',
          "mytag-cd-20200110",
          'mytag-20200110-093000',
          'mytag-tag-',
          'mytag-baseref-',
          'mytag-defbranch'
        ],
        latest: false
      } as Version,
      [
        'user/app:mytag-master',
        'user/app:mytag-20200110',
        'user/app:mytag-cd-20200110',
        'user/app:mytag-20200110-093000',
        'user/app:mytag-tag-',
        'user/app:mytag-baseref-',
        'user/app:mytag-defbranch'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=266574110acf203503badf966df2ea24b5d732d7",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=mytag-master"
      ],
      undefined
    ],
    [
      'push18',
      'event_push_dev.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=ref,event=branch`,
          `type=sha,format=long`
        ],
      } as Inputs,
      {
        main: 'dev',
        partial: ['sha-860c1904a1ce19322e91ac35af1ab07466440c37'],
        latest: false
      } as Version,
      [
        'org/app:dev',
        'org/app:sha-860c1904a1ce19322e91ac35af1ab07466440c37',
        'ghcr.io/user/app:dev',
        'ghcr.io/user/app:sha-860c1904a1ce19322e91ac35af1ab07466440c37'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=dev"
      ],
      undefined
    ],
    [
      'push19',
      'event_push_dev.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=edge,branch=master`,
          `type=ref,event=branch,enable=false`,
          `type=sha,format=long`,
          `type=raw,value=defbranch,enable={{is_default_branch}}`
        ],
      } as Inputs,
      {
        main: 'sha-860c1904a1ce19322e91ac35af1ab07466440c37',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:sha-860c1904a1ce19322e91ac35af1ab07466440c37',
        'ghcr.io/user/app:sha-860c1904a1ce19322e91ac35af1ab07466440c37'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=sha-860c1904a1ce19322e91ac35af1ab07466440c37"
      ],
      undefined
    ],
    [
      'push20',
      'event_push_dev.env',
      {
        images: [
          'org/app',
          'ghcr.io/user/app,enable=false'
        ],
        tags: [
          `type=edge,branch=master`,
          `type=ref,event=branch,enable=false`,
          `type=sha,format=long`
        ],
      } as Inputs,
      {
        main: 'sha-860c1904a1ce19322e91ac35af1ab07466440c37',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:sha-860c1904a1ce19322e91ac35af1ab07466440c37'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=sha-860c1904a1ce19322e91ac35af1ab07466440c37"
      ],
      undefined
    ],
    [
      'push21',
      'event_push_master.env',
      {
        images: [] as string[],
        tags: [
          `type=raw,value=mytag-{{branch}}`,
          `type=raw,value=mytag-{{date 'YYYYMMDD'}}`,
          `type=raw,value=mytag-{{date 'YYYYMMDD-HHmmss' tz='Asia/Tokyo'}}`,
          `type=raw,value=mytag-src-{{commit_date 'YYYYMMDD'}}`,
          `type=raw,value=mytag-tag-{{tag}}`,
          `type=raw,value=mytag-baseref-{{base_ref}}`,
          `type=raw,value=mytag-defbranch,enable={{is_default_branch}}`
        ],
        labels: [
          "org.opencontainers.image.created={{commit_date 'YYYY-MM-DDTHH:mm:ss.SSS[Z]'}}"
        ]
      } as Inputs,
      {
        main: 'mytag-master',
        partial: [
          'mytag-20200110',
          'mytag-20200110-093000',
          'mytag-src-20200110',
          'mytag-tag-',
          'mytag-baseref-',
          'mytag-defbranch'
        ],
        latest: false
      } as Version,
      [
        'mytag-master',
        'mytag-20200110',
        'mytag-20200110-093000',
        'mytag-src-20200110',
        'mytag-tag-',
        'mytag-baseref-',
        'mytag-defbranch'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=266574110acf203503badf966df2ea24b5d732d7",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=mytag-master"
      ],
      undefined
    ],
    [
      'push22',
      'event_push_dev.env',
      {
        images: ['org/app'],
        tags: [
          `type=edge,branch=master`,
          `type=sha,format=long`,
          `type=raw,value=notdefbranch,enable={{is_not_default_branch}}`
        ],
      } as Inputs,
      {
        main: 'notdefbranch',
        partial: [
          'sha-860c1904a1ce19322e91ac35af1ab07466440c37'
        ],
        latest: false
      } as Version,
      [
        "org/app:notdefbranch",
        "org/app:sha-860c1904a1ce19322e91ac35af1ab07466440c37"
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=notdefbranch"
      ],
      undefined
    ]
  ])('given %o with %o event', tagsLabelsTest);
});

describe('tag', () => {
  // prettier-ignore
  // eslint-disable-next-line vitest/expect-expect
  test.each([
    [
      'tag01',
      'event_tag_release1.env',
      {
        images: ['user/app'],
      } as Inputs,
      {
        main: 'release1',
        partial: [],
        latest: true
      } as Version,
      [
        'user/app:release1',
        'user/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=release1"
      ],
      undefined
    ],
    [
      'tag02',
      'event_tag_20200110-RC2.env',
      {
        images: ['user/app'],
      } as Inputs,
      {
        main: '20200110-RC2',
        partial: [],
        latest: true
      } as Version,
      [
        'user/app:20200110-RC2',
        'user/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=20200110-RC2"
      ],
      undefined
    ],
    [
      'tag03',
      'event_tag_20200110-RC2.env',
      {
        images: ['user/app'],
        tags: [
          `type=match,pattern=\\d{8}`
        ],
        flavor: [
          `latest=false`
        ]
      } as Inputs,
      {
        main: '20200110',
        partial: [],
        latest: false
      } as Version,
      [
        'user/app:20200110'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=20200110"
      ],
      undefined
    ],
    [
      'tag04',
      'event_tag_20200110-RC2.env',
      {
        images: ['user/app'],
        tags: [
          `type=match,pattern=(.*)-RC,group=1`
        ],
        flavor: [
          `latest=false`
        ]
      } as Inputs,
      {
        main: '20200110',
        partial: [],
        latest: false
      } as Version,
      [
        'user/app:20200110'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=20200110"
      ],
      undefined
    ],
    [
      'tag05',
      'event_tag_v1.1.1.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=match,"pattern=\\d.\\d.\\d"`
        ]
      } as Inputs,
      {
        main: '1.1.1',
        partial: [],
        latest: true
      } as Version,
      [
        'org/app:1.1.1',
        'org/app:latest',
        'ghcr.io/user/app:1.1.1',
        'ghcr.io/user/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=1.1.1"
      ],
      undefined
    ],
    [
      'tag06',
      'event_tag_v1.1.1.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=match,"pattern=^v(\\d.\\d.\\d)$",group=1`
        ]
      } as Inputs,
      {
        main: '1.1.1',
        partial: [],
        latest: true
      } as Version,
      [
        'org/app:1.1.1',
        'org/app:latest',
        'ghcr.io/user/app:1.1.1',
        'ghcr.io/user/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=1.1.1"
      ],
      undefined
    ],
    [
      'tag07',
      'event_tag_v2.0.8-beta.67.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=match,"pattern=\\d.\\d.\\d-(alpha|beta).\\d+"`
        ]
      } as Inputs,
      {
        main: '2.0.8-beta.67',
        partial: [],
        latest: true
      } as Version,
      [
        'org/app:2.0.8-beta.67',
        'org/app:latest',
        'ghcr.io/user/app:2.0.8-beta.67',
        'ghcr.io/user/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=2.0.8-beta.67"
      ],
      undefined
    ],
    [
      'tag08',
      'event_tag_v2.0.8-beta.67.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=match,"pattern=\\d.\\d"`
        ]
      } as Inputs,
      {
        main: '2.0',
        partial: [],
        latest: true
      } as Version,
      [
        'org/app:2.0',
        'org/app:latest',
        'ghcr.io/user/app:2.0',
        'ghcr.io/user/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=2.0"
      ],
      undefined
    ],
    [
      'tag09',
      'event_tag_v2.0.8-beta.67.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=match,"pattern=v(.*)-beta.(.*)",group=1`,
          `type=match,"pattern=v(.*)-beta.(.*)",group=2`,
        ]
      } as Inputs,
      {
        main: '2.0.8',
        partial: ['67'],
        latest: true
      } as Version,
      [
        'org/app:2.0.8',
        'org/app:67',
        'org/app:latest',
        'ghcr.io/user/app:2.0.8',
        'ghcr.io/user/app:67',
        'ghcr.io/user/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=2.0.8"
      ],
      undefined
    ],
    [
      'tag10',
      'event_tag_sometag.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=match,"pattern=\\d.\\d"`
        ]
      } as Inputs,
      {
        main: undefined,
        partial: [],
        latest: false
      } as Version,
      [],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version="
      ],
      undefined
    ],
    [
      'tag11',
      'event_tag_v1.1.1.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=semver,pattern={{version}}`,
          `type=semver,pattern={{major}}.{{minor}}`,
          `type=semver,pattern={{major}}`
        ]
      } as Inputs,
      {
        main: '1.1.1',
        partial: ['1.1', '1'],
        latest: true
      } as Version,
      [
        'org/app:1.1.1',
        'org/app:1.1',
        'org/app:1',
        'org/app:latest',
        'ghcr.io/user/app:1.1.1',
        'ghcr.io/user/app:1.1',
        'ghcr.io/user/app:1',
        'ghcr.io/user/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=1.1.1"
      ],
      undefined
    ],
    [
      'tag12',
      'event_tag_v1.1.1.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=semver,pattern={{version}}`,
          `type=semver,pattern={{major}}.{{minor}}.{{patch}}`
        ]
      } as Inputs,
      {
        main: '1.1.1',
        partial: [],
        latest: true
      } as Version,
      [
        'org/app:1.1.1',
        'org/app:latest',
        'ghcr.io/user/app:1.1.1',
        'ghcr.io/user/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=1.1.1"
      ],
      undefined
    ],
    [
      'tag13',
      'event_tag_v2.0.8-beta.67.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=semver,pattern={{major}}.{{minor}}`,
          `type=semver,pattern={{major}}`
        ]
      } as Inputs,
      {
        main: '2.0.8-beta.67',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:2.0.8-beta.67',
        'ghcr.io/user/app:2.0.8-beta.67'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=2.0.8-beta.67"
      ],
      undefined
    ],
    [
      'tag14',
      'event_tag_sometag.env',
      {
        images: ['ghcr.io/user/app'],
        tags: [
          `type=ref,event=tag`,
          `type=semver,pattern={{version}}`,
          `type=semver,pattern={{major}}.{{minor}}`,
          `type=semver,pattern={{major}}`
        ],
        flavor: [
          `latest=false`
        ]
      } as Inputs,
      {
        main: 'sometag',
        partial: [],
        latest: false
      } as Version,
      [
        'ghcr.io/user/app:sometag'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=sometag"
      ],
      undefined
    ],
    [
      'tag15',
      'event_tag_v2.0.8-beta.67.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=raw,priority=2000,foo`,
          `type=semver,pattern={{version}}`,
          `type=match,"pattern=\\d.\\d"`
        ]
      } as Inputs,
      {
        main: 'foo',
        partial: ['2.0.8-beta.67', '2.0'],
        latest: false
      } as Version,
      [
        'org/app:foo',
        'org/app:2.0.8-beta.67',
        'org/app:2.0',
        'ghcr.io/user/app:foo',
        'ghcr.io/user/app:2.0.8-beta.67',
        'ghcr.io/user/app:2.0'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=foo"
      ],
      undefined
    ],
    [
      'tag16',
      'event_tag_v1.1.1.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=raw,priority=2000,foo`,
          `type=ref,event=tag`,
          `type=edge`
        ]
      } as Inputs,
      {
        main: 'foo',
        partial: ['v1.1.1'],
        latest: false
      } as Version,
      [
        'org/app:foo',
        'org/app:v1.1.1',
        'ghcr.io/user/app:foo',
        'ghcr.io/user/app:v1.1.1',
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=foo"
      ],
      undefined
    ],
    [
      'tag17',
      'event_tag_p1-v1.0.0.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=match,"pattern=/^v(\\d.\\d.\\d)$/ig",group=1`,
          `type=match,pattern=\\d.\\d.\\d`,
          `type=match,pattern=\\d.\\d`,
          `type=ref,event=pr`,
          `type=sha`
        ]
      } as Inputs,
      {
        main: '1.0.0',
        partial: ['1.0', 'sha-860c190'],
        latest: true
      } as Version,
      [
        'org/app:1.0.0',
        'org/app:1.0',
        'org/app:sha-860c190',
        'org/app:latest',
        'ghcr.io/user/app:1.0.0',
        'ghcr.io/user/app:1.0',
        'ghcr.io/user/app:sha-860c190',
        'ghcr.io/user/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=1.0.0"
      ],
      undefined
    ],
    [
      'tag18',
      'event_tag_p1-v1.0.0.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=match,pattern=p1/v(\\d.\\d.\\d),group=1`,
          `type=match,pattern=p1/v(\\d.\\d),group=1`,
          `type=match,pattern=p1/v(\\d.\\d),group=3`,
          `type=ref,event=pr`,
          `type=sha`
        ]
      } as Inputs,
      {
        main: '1.0.0',
        partial: ['1.0', 'sha-860c190'],
        latest: true
      } as Version,
      [
        'org/app:1.0.0',
        'org/app:1.0',
        'org/app:sha-860c190',
        'org/app:latest',
        'ghcr.io/user/app:1.0.0',
        'ghcr.io/user/app:1.0',
        'ghcr.io/user/app:sha-860c190',
        'ghcr.io/user/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=1.0.0"
      ],
      undefined
    ],
    [
      'tag19',
      'event_tag_p1-v1.0.0.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=match,pattern=p1/v(\\d.\\d.\\d),group=1`,
          `type=match,pattern=p1/v(\\d.\\d),group=1,suffix=`,
          `type=ref,event=pr`,
          `type=sha`
        ],
        flavor: [
          `suffix=-dev`
        ]
      } as Inputs,
      {
        main: '1.0.0-dev',
        partial: ['1.0', 'sha-860c190-dev'],
        latest: true
      } as Version,
      [
        'org/app:1.0.0-dev',
        'org/app:1.0',
        'org/app:sha-860c190-dev',
        'org/app:latest',
        'ghcr.io/user/app:1.0.0-dev',
        'ghcr.io/user/app:1.0',
        'ghcr.io/user/app:sha-860c190-dev',
        'ghcr.io/user/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=1.0.0-dev"
      ],
      undefined
    ],
    [
      'tag20',
      'event_tag_v1.1.1.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=raw,{{tag}}-{{sha}}-foo`,
          `type=raw,{{base_ref}}-foo`,
          `type=raw,defbranch-foo,enable={{is_default_branch}}`
        ]
      } as Inputs,
      {
        main: 'v1.1.1-860c190-foo',
        partial: [
          'master-foo'
        ],
        latest: false
      } as Version,
      [
        'org/app:v1.1.1-860c190-foo',
        'org/app:master-foo',
        'ghcr.io/user/app:v1.1.1-860c190-foo',
        'ghcr.io/user/app:master-foo'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=v1.1.1-860c190-foo"
      ],
      undefined
    ],
    [
      'tag21',
      'event_tag_v1.1.1.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=semver,pattern={{version}}`,
          `type=semver,pattern={{major}}.{{minor}}.{{patch}}`
        ],
        flavor: [
          `suffix=-dev,onlatest=true`
        ]
      } as Inputs,
      {
        main: '1.1.1-dev',
        partial: [],
        latest: true
      } as Version,
      [
        'org/app:1.1.1-dev',
        'org/app:latest-dev',
        'ghcr.io/user/app:1.1.1-dev',
        'ghcr.io/user/app:latest-dev'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=1.1.1-dev"
      ],
      undefined
    ],
    [
      'tag22',
      'event_tag_v1.1.1.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=semver,pattern={{version}}`,
          `type=semver,pattern={{major}}.{{minor}}.{{patch}}`
        ],
        flavor: [
          `prefix=foo-,onlatest=true`,
          `suffix=-dev,onlatest=true`
        ]
      } as Inputs,
      {
        main: 'foo-1.1.1-dev',
        partial: [],
        latest: true
      } as Version,
      [
        'org/app:foo-1.1.1-dev',
        'org/app:foo-latest-dev',
        'ghcr.io/user/app:foo-1.1.1-dev',
        'ghcr.io/user/app:foo-latest-dev'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=foo-1.1.1-dev"
      ],
      undefined
    ],
    [
      'tag23',
      'event_tag_v1.1.1.env',
      {
        images: ['org/app'],
        tags: [
          `type=pep440,pattern={{raw}}`,
          `type=pep440,pattern={{major}}.{{minor}}`
        ]
      } as Inputs,
      {
        main: 'v1.1.1',
        partial: ['1.1'],
        latest: true
      } as Version,
      [
        'org/app:v1.1.1',
        'org/app:1.1',
        'org/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=v1.1.1"
      ],
      undefined
    ],
    [
      'tag24',
      'event_tag_1.2.env',
      {
        images: ['org/app'],
        tags: [
          `type=pep440,pattern={{version}}`,
          `type=pep440,pattern={{major}}.{{minor}}`
        ]
      } as Inputs,
      {
        main: '1.2',
        partial: [],
        latest: true
      } as Version,
      [
        'org/app:1.2',
        'org/app:latest',
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=1.2"
      ],
      undefined
    ],
    [
      'tag25',
      'event_tag_1.1beta2.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=pep440,pattern={{major}}.{{minor}}`,
          `type=pep440,pattern={{major}}`
        ]
      } as Inputs,
      {
        main: '1.1b2',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:1.1b2',
        'ghcr.io/user/app:1.1b2'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=1.1b2"
      ],
      undefined
    ],
    [
      'tag26',
      'event_tag_1.0dev4.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=pep440,pattern={{major}}.{{minor}}`,
          `type=pep440,pattern={{major}}`
        ]
      } as Inputs,
      {
        main: '1.0.dev4',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:1.0.dev4',
        'ghcr.io/user/app:1.0.dev4'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=1.0.dev4"
      ],
      undefined
    ],
    [
      'tag27',
      'event_tag_1.2.3rc2.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=pep440,pattern={{raw}}`,
          `type=pep440,pattern={{version}}`,
          `type=pep440,pattern={{major}}.{{minor}}`,
          `type=pep440,pattern={{major}}`
        ]
      } as Inputs,
      {
        main: '1.2.3rc2',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:1.2.3rc2',
        'ghcr.io/user/app:1.2.3rc2'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=1.2.3rc2"
      ],
      undefined
    ],
    [
      'tag28',
      'event_tag_v1.1.1.env',
      {
        images: ['org/app'],
        tags: [
          `type=pep440,pattern={{version}}`,
          `type=pep440,pattern={{major}}.{{minor}}.{{patch}}`,
          `type=pep440,pattern={{major}}.{{minor}}`,
          `type=pep440,pattern={{major}}`
        ]
      } as Inputs,
      {
        main: '1.1.1',
        partial: [
          "1.1",
          "1"
        ],
        latest: true
      } as Version,
      [
        'org/app:1.1.1',
        'org/app:1.1',
        'org/app:1',
        'org/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=1.1.1"
      ],
      undefined
    ],
    [
      'tag29',
      'event_tag_1.2post1.env',
      {
        images: ['org/app'],
        tags: [
          `type=pep440,pattern={{version}}`,
          `type=pep440,pattern={{major}}.{{minor}}`,
          `type=pep440,pattern={{major}}`
        ]
      } as Inputs,
      {
        main: '1.2.post1',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:1.2.post1'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=1.2.post1"
      ],
      undefined
    ],
    [
      'tag30',
      'event_tag_sometag.env',
      {
        images: ['ghcr.io/user/app'],
        tags: [
          `type=ref,event=tag`,
          `type=pep440,pattern={{version}}`,
          `type=pep440,pattern={{major}}.{{minor}}`,
          `type=pep440,pattern={{major}}`
        ],
        flavor: [
          `latest=false`
        ]
      } as Inputs,
      {
        main: 'sometag',
        partial: [],
        latest: false
      } as Version,
      [
        'ghcr.io/user/app:sometag'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=sometag"
      ],
      undefined
    ],
    [
      'tag31',
      'event_tag_v2.0.8-beta.67.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=semver,pattern={{raw}}`
        ]
      } as Inputs,
      {
        main: 'v2.0.8-beta.67',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:v2.0.8-beta.67',
        'ghcr.io/user/app:v2.0.8-beta.67'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=v2.0.8-beta.67"
      ],
      undefined
    ],
    [
      'tag32',
      'event_tag_v1.2.3rc2.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=pep440,pattern={{raw}}`,
          `type=pep440,pattern={{major}}.{{minor}}`
        ]
      } as Inputs,
      {
        main: 'v1.2.3rc2',
        partial: ['1.2.3rc2'],
        latest: false
      } as Version,
      [
        'org/app:v1.2.3rc2',
        'org/app:1.2.3rc2',
        'ghcr.io/user/app:v1.2.3rc2',
        'ghcr.io/user/app:1.2.3rc2'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=v1.2.3rc2"
      ],
      undefined
    ],
    [
      'tag33',
      'event_tag_v1.1.1.env',
      {
        images: [] as string[],
        tags: [
          `type=pep440,pattern={{version}}`,
          `type=pep440,pattern={{major}}.{{minor}}.{{patch}}`,
          `type=pep440,pattern={{major}}.{{minor}}`,
          `type=pep440,pattern={{major}}`
        ]
      } as Inputs,
      {
        main: '1.1.1',
        partial: [
          "1.1",
          "1"
        ],
        latest: true
      } as Version,
      [
        '1.1.1',
        '1.1',
        '1',
        'latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=1.1.1"
      ],
      undefined
    ],
    [
      'tag34',
      'event_tag_p1-v1.0.0.env',
      {
        images: ['org/app'],
        tags: [
          `type=semver,pattern={{version}},"match=v(\\d.\\d.\\d)$"`,
        ]
      } as Inputs,
      {
        main: '1.0.0',
        partial: [],
        latest: true
      } as Version,
      [
        'org/app:1.0.0',
        'org/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=1.0.0"
      ],
      undefined
    ],
    [
      'push35',
      'event_push_master.env',
      {
        images: ['user/app'],
        tags: [
          `type=semver,pattern={{version}},value=p1/v1.2.3,"match=v(\\d.\\d.\\d)$"`,
          `type=pep440,pattern={{version}},value=p1/v1.2.3,"match=v(\\d.\\d.\\d)$"`,
          `type=edge`
        ],
      } as Inputs,
      {
        main: '1.2.3',
        partial: ['edge'],
        latest: true
      } as Version,
      [
        'user/app:1.2.3',
        'user/app:edge',
        'user/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=266574110acf203503badf966df2ea24b5d732d7",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=1.2.3"
      ],
      undefined
    ]
  ])('given %o with %o event', tagsLabelsTest);
});

describe('latest', () => {
  // prettier-ignore
  // eslint-disable-next-line vitest/expect-expect
  test.each([
    [
      'latest01',
      'event_tag_release1.env',
      {
        images: ['user/app'],
        tags: [
          `type=match,"pattern=^release\\d{1,2}"`
        ],
      } as Inputs,
      {
        main: 'release1',
        partial: [],
        latest: true,
      } as Version,
      [
        'user/app:release1',
        'user/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=release1"
      ],
      undefined
    ],
    [
      'latest02',
      'event_tag_20200110-RC2.env',
      {
        images: ['user/app'],
        tags: [
          `type=match,"pattern=^\\d+-RC\\d{1,2}"`
        ]
      } as Inputs,
      {
        main: '20200110-RC2',
        partial: [],
        latest: true
      } as Version,
      [
        'user/app:20200110-RC2',
        'user/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=20200110-RC2"
      ],
      undefined
    ],
    [
      'latest03',
      'event_tag_20200110-RC2.env',
      {
        images: ['user/app'],
        tags: [
          `type=match,pattern=\\d{8}`
        ]
      } as Inputs,
      {
        main: '20200110',
        partial: [],
        latest: true
      } as Version,
      [
        'user/app:20200110',
        'user/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=20200110"
      ],
      undefined
    ],
    [
      'latest04',
      'event_tag_v1.1.1.env',
      {
        images: ['user/app'],
        tags: [
          `type=match,"pattern=\\d.\\d.\\d"`
        ]
      } as Inputs,
      {
        main: '1.1.1',
        partial: [],
        latest: true
      } as Version,
      [
        'user/app:1.1.1',
        'user/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=1.1.1"
      ],
      undefined
    ],
    [
      'latest05',
      'event_tag_v1.1.1.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
      } as Inputs,
      {
        main: 'v1.1.1',
        partial: [],
        latest: true
      } as Version,
      [
        'org/app:v1.1.1',
        'org/app:latest',
        'ghcr.io/user/app:v1.1.1',
        'ghcr.io/user/app:latest',
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=v1.1.1"
      ],
      undefined
    ],
    [
      'latest06',
      'event_tag_v2.0.8-beta.67.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=match,"pattern=\\d.\\d.\\d"`
        ]
      } as Inputs,
      {
        main: '2.0.8',
        partial: [],
        latest: true
      } as Version,
      [
        'org/app:2.0.8',
        'org/app:latest',
        'ghcr.io/user/app:2.0.8',
        'ghcr.io/user/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=2.0.8"
      ],
      undefined
    ],
    [
      'latest07',
      'event_tag_v1.1.1.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=ref,event=tag`
        ],
        flavor: [
          `latest=false`
        ]
      } as Inputs,
      {
        main: 'v1.1.1',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:v1.1.1',
        'ghcr.io/user/app:v1.1.1',
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=v1.1.1"
      ],
      undefined
    ],
    [
      'latest08',
      'event_tag_v1.1.1.env',
      {
        images: ['org/app', 'ghcr.io/MyUSER/MyApp'],
        tags: [
          `type=ref,event=tag`
        ],
        flavor: [
          `latest=false`
        ]
      } as Inputs,
      {
        main: 'v1.1.1',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:v1.1.1',
        'ghcr.io/myuser/myapp:v1.1.1',
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=v1.1.1"
      ],
      undefined
    ],
    [
      'latest09',
      'event_tag_v1.1.1.env',
      {
        images: ['org/app', 'ghcr.io/MyUSER/MyApp'],
        tags: [
          `type=ref,event=tag`
        ],
        flavor: [
          `latest=false`
        ],
        labels: [
          "maintainer=CrazyMax",
          `org.opencontainers.image.description=this is a "good" example`,
          "org.opencontainers.image.title=MyCustomTitle",
          "org.opencontainers.image.vendor=MyCompany",
        ],
        annotations: [
          "maintainer=Foo",
          `org.opencontainers.image.description=this is a "bad" example`,
          "org.opencontainers.image.title=MyNotTitle",
          "org.opencontainers.image.vendor=MyNotCompany",
        ]
      } as Inputs,
      {
        main: 'v1.1.1',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:v1.1.1',
        'ghcr.io/myuser/myapp:v1.1.1',
      ],
      [
        "maintainer=CrazyMax",
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        `org.opencontainers.image.description=this is a "good" example`,
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=MyCustomTitle",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.vendor=MyCompany",
        "org.opencontainers.image.version=v1.1.1"
      ],
      [
        "maintainer=Foo",
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        `org.opencontainers.image.description=this is a "bad" example`,
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=MyNotTitle",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.vendor=MyNotCompany",
        "org.opencontainers.image.version=v1.1.1"
      ]
    ],
    [
      'latest10',
      'event_tag_v2.0.8-beta.67.env',
      {
        images: [] as string[],
        tags: [
          `type=match,"pattern=\\d.\\d.\\d"`
        ]
      } as Inputs,
      {
        main: '2.0.8',
        partial: [],
        latest: true
      } as Version,
      [
        '2.0.8',
        'latest',
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=2.0.8"
      ],
      undefined
    ]
  ])('given %o with %o event', tagsLabelsTest);
});

describe('pr', () => {
  // prettier-ignore
  // eslint-disable-next-line vitest/expect-expect
  test.each([
    [
      'pr01',
      'event_pull_request.env',
      {
        images: ['user/app'],
      } as Inputs,
      {
        main: 'pr-15',
        partial: [],
        latest: false
      } as Version,
      [
        'user/app:pr-15'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=a9c8c5828b91be19d9728548b24759e352367ef1",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=pr-15"
      ],
      undefined
    ],
    [
      'pr02',
      'event_pull_request.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
      } as Inputs,
      {
        main: 'pr-15',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:pr-15',
        'ghcr.io/user/app:pr-15'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=a9c8c5828b91be19d9728548b24759e352367ef1",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=pr-15"
      ],
      undefined
    ],
    [
      'pr03',
      'event_pull_request.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=ref,event=pr`,
          `type=sha`
        ]
      } as Inputs,
      {
        main: 'pr-15',
        partial: ['sha-a9c8c58'],
        latest: false
      } as Version,
      [
        'org/app:pr-15',
        'org/app:sha-a9c8c58',
        'ghcr.io/user/app:pr-15',
        'ghcr.io/user/app:sha-a9c8c58'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=a9c8c5828b91be19d9728548b24759e352367ef1",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=pr-15"
      ],
      undefined
    ],
    [
      'pr04',
      'event_pull_request.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=sha,priority=2000`,
          `type=ref,event=pr`
        ]
      } as Inputs,
      {
        main: 'sha-a9c8c58',
        partial: ['pr-15'],
        latest: false
      } as Version,
      [
        'org/app:sha-a9c8c58',
        'org/app:pr-15',
        'ghcr.io/user/app:sha-a9c8c58',
        'ghcr.io/user/app:pr-15'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=a9c8c5828b91be19d9728548b24759e352367ef1",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=sha-a9c8c58"
      ],
      undefined
    ],
    [
      'pr05',
      'event_pull_request.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=ref,event=pr`
        ],
        flavor: [
          `prefix=glo-`,
          `suffix=-bal`
        ]
      } as Inputs,
      {
        main: 'pr-15-bal',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:pr-15-bal',
        'ghcr.io/user/app:pr-15-bal'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=a9c8c5828b91be19d9728548b24759e352367ef1",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=pr-15-bal"
      ],
      undefined
    ],
    [
      'pr06',
      'event_pull_request.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=ref,event=pr,prefix=`
        ],
        flavor: [
          `prefix=glo-`,
          `suffix=-bal`
        ]
      } as Inputs,
      {
        main: '15-bal',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:15-bal',
        'ghcr.io/user/app:15-bal'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=a9c8c5828b91be19d9728548b24759e352367ef1",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=15-bal"
      ],
      undefined
    ],
    [
      'pr07',
      'event_pull_request_target.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=sha,priority=2000`,
          `type=ref,event=pr`
        ]
      } as Inputs,
      {
        main: 'sha-2665741',
        partial: ['pr-15'],
        latest: false
      } as Version,
      [
        'org/app:sha-2665741',
        'org/app:pr-15',
        'ghcr.io/user/app:sha-2665741',
        'ghcr.io/user/app:pr-15'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=266574110acf203503badf966df2ea24b5d732d7",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=sha-2665741"
      ],
      undefined
    ],
    [
      'pr08',
      'event_pull_request_target.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=ref,event=pr,prefix=`
        ],
        flavor: [
          `prefix=glo-`,
          `suffix=-bal`
        ]
      } as Inputs,
      {
        main: '15-bal',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:15-bal',
        'ghcr.io/user/app:15-bal'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=266574110acf203503badf966df2ea24b5d732d7",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=15-bal"
      ],
      undefined
    ],
    [
      'pr09',
      'event_pull_request_target.env',
      {
        images: ['org/app'],
        tags: [
          `type=ref,event=tag`,
          `type=ref,event=pr`,
          `type=ref,event=branch`,
          `type=sha`,
          `type=sha,format=long`
        ]
      } as Inputs,
      {
        main: 'pr-15',
        partial: [
          'sha-2665741',
          'sha-266574110acf203503badf966df2ea24b5d732d7'
        ],
        latest: false
      } as Version,
      [
        'org/app:pr-15',
        'org/app:sha-2665741',
        'org/app:sha-266574110acf203503badf966df2ea24b5d732d7'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=266574110acf203503badf966df2ea24b5d732d7",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=pr-15"
      ],
      undefined
    ],
    [
      'pr10',
      'event_pull_request_target.env',
      {
        images: ['org/app'],
        tags: [
          `type=raw,value=mytag-{{base_ref}}`,
          `type=raw,mytag-defbranch,enable={{is_default_branch}}`
        ]
      } as Inputs,
      {
        main: 'mytag-master',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:mytag-master'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=266574110acf203503badf966df2ea24b5d732d7",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=mytag-master"
      ],
      undefined
    ],
    [
      'pr11',
      'event_pull_request.env',
      {
        images: ['org/app'],
        tags: [
          `type=raw,value=mytag-{{base_ref}}`,
          `type=raw,mytag-defbranch,enable={{is_default_branch}}`
        ]
      } as Inputs,
      {
        main: 'mytag-master',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:mytag-master'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=a9c8c5828b91be19d9728548b24759e352367ef1",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=mytag-master"
      ],
      undefined
    ],
    [
      'pr12',
      'event_pull_request.env',
      {
        images: ['org/app'],
        tags: [
          `type=raw,value={{commit_date YYYY-MM-DD-HHmmSS}}`,
        ]
      } as Inputs,
      {
        main: "2020-01-10T00-30-00Z",
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:2020-01-10T00-30-00Z'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=a9c8c5828b91be19d9728548b24759e352367ef1",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=2020-01-10T00-30-00Z"
      ],
      undefined
    ],
  ])('given %o with %o event', tagsLabelsTest);
});

describe('pr-head-sha', () => {
  // prettier-ignore
  test.each([
    [
      'pr01',
      'event_pull_request.env',
      {
        images: ['user/app'],
      } as Inputs,
      {
        main: 'pr-15',
        partial: [],
        latest: false
      } as Version,
      [
        'user/app:pr-15'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=3370e228f2209994d57af4427fe64e71bb79ac96",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=pr-15"
      ]
    ],
    [
      'pr02',
      'event_pull_request.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
      } as Inputs,
      {
        main: 'pr-15',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:pr-15',
        'ghcr.io/user/app:pr-15'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=3370e228f2209994d57af4427fe64e71bb79ac96",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=pr-15"
      ]
    ],
    [
      'pr03',
      'event_pull_request.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=ref,event=pr`,
          `type=sha`
        ]
      } as Inputs,
      {
        main: 'pr-15',
        partial: ['sha-3370e22'],
        latest: false
      } as Version,
      [
        'org/app:pr-15',
        'org/app:sha-3370e22',
        'ghcr.io/user/app:pr-15',
        'ghcr.io/user/app:sha-3370e22'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=3370e228f2209994d57af4427fe64e71bb79ac96",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=pr-15"
      ]
    ],
    [
      'pr04',
      'event_pull_request.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=sha,priority=2000`,
          `type=ref,event=pr`
        ]
      } as Inputs,
      {
        main: 'sha-3370e22',
        partial: ['pr-15'],
        latest: false
      } as Version,
      [
        'org/app:sha-3370e22',
        'org/app:pr-15',
        'ghcr.io/user/app:sha-3370e22',
        'ghcr.io/user/app:pr-15'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=3370e228f2209994d57af4427fe64e71bb79ac96",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=sha-3370e22"
      ]
    ],
    [
      'pr05',
      'event_pull_request.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=ref,event=pr`
        ],
        flavor: [
          `prefix=glo-`,
          `suffix=-bal`
        ]
      } as Inputs,
      {
        main: 'pr-15-bal',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:pr-15-bal',
        'ghcr.io/user/app:pr-15-bal'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=3370e228f2209994d57af4427fe64e71bb79ac96",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=pr-15-bal"
      ]
    ],
    [
      'pr06',
      'event_pull_request.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=ref,event=pr,prefix=`
        ],
        flavor: [
          `prefix=glo-`,
          `suffix=-bal`
        ]
      } as Inputs,
      {
        main: '15-bal',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:15-bal',
        'ghcr.io/user/app:15-bal'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=3370e228f2209994d57af4427fe64e71bb79ac96",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=15-bal"
      ]
    ],
    [
      'pr07',
      'event_pull_request_target.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=sha,priority=2000`,
          `type=ref,event=pr`
        ]
      } as Inputs,
      {
        main: 'sha-3370e22',
        partial: ['pr-15'],
        latest: false
      } as Version,
      [
        'org/app:sha-3370e22',
        'org/app:pr-15',
        'ghcr.io/user/app:sha-3370e22',
        'ghcr.io/user/app:pr-15'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=3370e228f2209994d57af4427fe64e71bb79ac96",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=sha-3370e22"
      ]
    ],
    [
      'pr08',
      'event_pull_request_target.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=ref,event=pr,prefix=`
        ],
        flavor: [
          `prefix=glo-`,
          `suffix=-bal`
        ]
      } as Inputs,
      {
        main: '15-bal',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:15-bal',
        'ghcr.io/user/app:15-bal'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=3370e228f2209994d57af4427fe64e71bb79ac96",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=15-bal"
      ]
    ],
    [
      'pr09',
      'event_pull_request_target.env',
      {
        images: ['org/app'],
        tags: [
          `type=ref,event=tag`,
          `type=ref,event=pr`,
          `type=ref,event=branch`,
          `type=sha`,
          `type=sha,format=long`
        ]
      } as Inputs,
      {
        main: 'pr-15',
        partial: [
          'sha-3370e22',
          'sha-3370e228f2209994d57af4427fe64e71bb79ac96'
        ],
        latest: false
      } as Version,
      [
        'org/app:pr-15',
        'org/app:sha-3370e22',
        'org/app:sha-3370e228f2209994d57af4427fe64e71bb79ac96'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=3370e228f2209994d57af4427fe64e71bb79ac96",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=pr-15"
      ]
    ],
    [
      'pr10',
      'event_pull_request_target.env',
      {
        images: ['org/app'],
        tags: [
          `type=raw,value=mytag-{{base_ref}}`,
          `type=raw,mytag-defbranch,enable={{is_default_branch}}`
        ]
      } as Inputs,
      {
        main: 'mytag-master',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:mytag-master'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=3370e228f2209994d57af4427fe64e71bb79ac96",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=mytag-master"
      ]
    ],
    [
      'pr11',
      'event_pull_request.env',
      {
        images: ['org/app'],
        tags: [
          `type=raw,value=mytag-{{base_ref}}`,
          `type=raw,mytag-defbranch,enable={{is_default_branch}}`
        ]
      } as Inputs,
      {
        main: 'mytag-master',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:mytag-master'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=3370e228f2209994d57af4427fe64e71bb79ac96",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=mytag-master"
      ]
    ],
    [
      'pr12',
      'event_pull_request.env',
      {
        images: ['org/app'],
        tags: [
          `type=raw,value=src-{{commit_date YYYY-MM-DD}}`,
        ]
      } as Inputs,
      {
        main: "src-2020-01-10T00-30-00Z",
        partial: [],
        latest: false
      } as Version,
      [
        "org/app:src-2020-01-10T00-30-00Z",
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=3370e228f2209994d57af4427fe64e71bb79ac96",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=src-2020-01-10T00-30-00Z",
      ]
    ],
  ])('given %o with %o event', async (name: string, envFile: string, inputs: Inputs, exVersion: Version, exTags: Array<string>, exLabelsAnnotations: Array<string>) => {
    process.env = dotenv.parse(fs.readFileSync(path.join(__dirname, 'fixtures', envFile)));
    process.env.DOCKER_METADATA_PR_HEAD_SHA = 'true';

    const toolkit = new Toolkit();
    const repo = await toolkit.github.repoData();
    const meta = new Meta({...getInputs(), ...inputs}, await getContext(ContextSource.workflow, toolkit), repo);

    const version = meta.version;
    expect(version).toEqual(exVersion);

    const tags = meta.getTags();
    expect(tags).toEqual(exTags);

    const labels = meta.getLabels();
    expect(labels).toEqual(exLabelsAnnotations);

    const annotations = meta.getAnnotations();
    expect(annotations).toEqual(exLabelsAnnotations);
  });
});

describe('schedule', () => {
  // prettier-ignore
  // eslint-disable-next-line vitest/expect-expect
  test.each([
    [
      'schedule01',
      'event_schedule.env',
      {
        images: ['user/app'],
      } as Inputs,
      {
        main: 'nightly',
        partial: ['master'],
        latest: false
      } as Version,
      [
        'user/app:nightly',
        'user/app:master'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=nightly"
      ],
      undefined
    ],
    [
      'schedule02',
      'event_schedule.env',
      {
        images: ['user/app'],
        tags: [
          `type=schedule,pattern={{date 'YYYYMMDD'}}`,
          `type=schedule,pattern=source-date-{{commit_date 'YYYY-MM-DD'}}`
        ]
      } as Inputs,
      {
        main: '20200110',
        partial: [
          "source-date-2020-01-10",
        ],
        latest: false
      } as Version,
      [
        'user/app:20200110',
        'user/app:source-date-2020-01-10'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=20200110"
      ],
      undefined
    ],
    [
      'schedule03',
      'event_schedule.env',
      {
        images: ['user/app'],
        tags: [
          `type=schedule,pattern={{date 'YYYYMMDD-HHmmss'}}`
        ]
      } as Inputs,
      {
        main: '20200110-003000',
        partial: [],
        latest: false
      } as Version,
      [
        'user/app:20200110-003000'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=20200110-003000"
      ],
      undefined
    ],
    [
      'schedule04',
      'event_schedule.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
      } as Inputs,
      {
        main: 'nightly',
        partial: ['master'],
        latest: false
      } as Version,
      [
        'org/app:nightly',
        'org/app:master',
        'ghcr.io/user/app:nightly',
        'ghcr.io/user/app:master'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=nightly"
      ],
      undefined
    ],
    [
      'schedule05',
      'event_schedule.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=schedule`,
          `type=sha`
        ]
      } as Inputs,
      {
        main: 'nightly',
        partial: ['sha-860c190'],
        latest: false
      } as Version,
      [
        'org/app:nightly',
        'org/app:sha-860c190',
        'ghcr.io/user/app:nightly',
        'ghcr.io/user/app:sha-860c190'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=nightly"
      ],
      undefined
    ],
    [
      'schedule06',
      'event_schedule.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=schedule`,
          `type=sha,priority=2000`,
          `type=raw,value=defbranch,enable={{is_default_branch}}`
        ]
      } as Inputs,
      {
        main: 'sha-860c190',
        partial: [
          'nightly',
          'defbranch'
        ],
        latest: false
      } as Version,
      [
        'org/app:sha-860c190',
        'org/app:nightly',
        'org/app:defbranch',
        'ghcr.io/user/app:sha-860c190',
        'ghcr.io/user/app:nightly',
        'ghcr.io/user/app:defbranch'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=sha-860c190"
      ],
      undefined
    ],
    [
      'schedule07',
      'event_schedule.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=schedule`,
        ],
        flavor: [
          `prefix=glo-`,
          `suffix=-bal`
        ]
      } as Inputs,
      {
        main: 'glo-nightly-bal',
        partial: [],
        latest: false
      } as Version,
      [
        'org/app:glo-nightly-bal',
        'ghcr.io/user/app:glo-nightly-bal'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=glo-nightly-bal"
      ],
      undefined
    ],
    [
      'schedule08',
      'event_schedule.env',
      {
        images: ['user/app'],
        tags: [
          `type=schedule,pattern={{date 'YYYYMMDD-HHmmss' tz='Asia/Tokyo'}}`,
          `type=schedule,pattern=src-{{commit_date 'YYYYMMDD-HHmmss' tz='Asia/Tokyo'}}`,
        ]
      } as Inputs,
      {
        main: '20200110-093000',
        partial: [
          "src-20200110-093000",
        ],
        latest: false
      } as Version,
      [
        'user/app:20200110-093000',
        'user/app:src-20200110-093000'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=20200110-093000"
      ],
      undefined
    ],
  ])('given %o with %o event', tagsLabelsTest);
});

describe('release', () => {
  // prettier-ignore
  // eslint-disable-next-line vitest/expect-expect
  test.each([
    [
      'release01',
      'event_release_created.env',
      {
        images: ['user/app'],
      } as Inputs,
      {
        main: 'v1.1.1',
        partial: [],
        latest: true
      } as Version,
      [
        'user/app:v1.1.1',
        'user/app:latest',
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=v1.1.1"
      ],
      undefined
    ],
    [
      'release02',
      'event_release_created.env',
      {
        images: ['user/app'],
        tags: [
          `type=ref,event=tag`,
          `type=raw,value=baseref-{{base_ref}}`,
          `type=raw,value=defbranch,enable={{is_default_branch}}`
        ]
      } as Inputs,
      {
        main: 'v1.1.1',
        partial: [
          'baseref-'
        ],
        latest: true
      } as Version,
      [
        'user/app:v1.1.1',
        'user/app:baseref-',
        'user/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=v1.1.1"
      ],
      undefined
    ],
    [
      'release03',
      'event_release_created.env',
      {
        images: ['user/app'],
        tags: [
          `type=raw,value=src-{{commit_date 'YYYYMMDD-HHmmss'}}`,
          `type=raw,value={{date 'YYYYMMDD-HHmmss'}}`,
        ]
      } as Inputs,
      {
      "main": "src-20200110-003000",
        partial: [
        "20200110-003000",
        ],
"latest": false,
      } as Version,
      [
        "user/app:src-20200110-003000",
        "user/app:20200110-003000",
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
      "org.opencontainers.image.version=src-20200110-003000",
      ],
      undefined
    ]
  ])('given %o with %o event', tagsLabelsTest);
});

describe('raw', () => {
  // prettier-ignore
  // eslint-disable-next-line vitest/expect-expect
  test.each([
    [
      'raw01',
      'event_push_dev.env',
      {
        images: ['user/app'],
        tags: [
          `type=ref,event=branch`,
          `type=raw,my`,
          `type=raw,custom`,
          `type=raw,tags`
        ]
      } as Inputs,
      {
        main: 'dev',
        partial: ['my', 'custom', 'tags'],
        latest: false
      } as Version,
      [
        'user/app:dev',
        'user/app:my',
        'user/app:custom',
        'user/app:tags'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=dev"
      ],
      undefined
    ],
    [
      'raw02',
      'event_push_dev.env',
      {
        images: ['user/app'],
        tags: [
          `type=ref,event=branch`,
          `type=raw,my`
        ]
      } as Inputs,
      {
        main: 'dev',
        partial: ['my'],
        latest: false
      } as Version,
      [
        'user/app:dev',
        'user/app:my'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=dev"
      ],
      undefined
    ],
    [
      'raw03',
      'event_tag_release1.env',
      {
        images: ['user/app'],
        tags: [
          `type=ref,event=tag`,
          `type=raw,my`,
          `type=raw,custom`,
          `type=raw,tags`
        ]
      } as Inputs,
      {
        main: 'release1',
        partial: ['my', 'custom', 'tags'],
        latest: true
      } as Version,
      [
        'user/app:release1',
        'user/app:my',
        'user/app:custom',
        'user/app:tags',
        'user/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=release1"
      ],
      undefined
    ],
    [
      'raw04',
      'event_tag_20200110-RC2.env',
      {
        images: ['user/app'],
        tags: [
          `type=match,pattern=\\d{8}`,
          `type=raw,my`,
          `type=raw,custom`,
          `type=raw,tags`
        ],
        flavor: [
          `latest=false`
        ]
      } as Inputs,
      {
        main: '20200110',
        partial: ['my', 'custom', 'tags'],
        latest: false
      } as Version,
      [
        'user/app:20200110',
        'user/app:my',
        'user/app:custom',
        'user/app:tags'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=20200110"
      ],
      undefined
    ],
    [
      'raw05',
      'event_tag_v1.1.1.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=semver,pattern={{version}}`,
          `type=semver,pattern={{major}}.{{minor}}`,
          `type=semver,pattern={{major}}`,
          `type=raw,my`,
          `type=raw,custom`,
          `type=raw,tags`
        ]
      } as Inputs,
      {
        main: '1.1.1',
        partial: ['1.1', '1', 'my', 'custom', 'tags'],
        latest: true
      } as Version,
      [
        'org/app:1.1.1',
        'org/app:1.1',
        'org/app:1',
        'org/app:my',
        'org/app:custom',
        'org/app:tags',
        'org/app:latest',
        'ghcr.io/user/app:1.1.1',
        'ghcr.io/user/app:1.1',
        'ghcr.io/user/app:1',
        'ghcr.io/user/app:my',
        'ghcr.io/user/app:custom',
        'ghcr.io/user/app:tags',
        'ghcr.io/user/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=1.1.1"
      ],
      undefined
    ],
    [
      'raw06',
      'event_tag_v1.1.1.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=raw,my`,
          `type=raw,custom`,
          `type=raw,tags`
        ]
      } as Inputs,
      {
        main: 'my',
        partial: ['custom', 'tags'],
        latest: false
      } as Version,
      [
        'org/app:my',
        'org/app:custom',
        'org/app:tags',
        'ghcr.io/user/app:my',
        'ghcr.io/user/app:custom',
        'ghcr.io/user/app:tags'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=my"
      ],
      undefined
    ],
    [
      'raw07',
      'event_push_dev.env',
      {
        images: ['user/app'],
        tags: [
          `type=ref,priority=90,event=branch`,
          `type=raw,my`,
          `type=raw,custom`,
          `type=raw,tags`
        ],
        flavor: [
          `latest=true`
        ]
      } as Inputs,
      {
        main: 'my',
        partial: ['custom', 'tags', 'dev'],
        latest: true
      } as Version,
      [
        'user/app:my',
        'user/app:custom',
        'user/app:tags',
        'user/app:dev',
        'user/app:latest'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=my"
      ],
      undefined
    ],
    [
      'raw08',
      'event_push_dev.env',
      {
        images: ['user/app'],
        tags: [
          `type=match,pattern=\\d{8}`,
          `type=raw,my`,
          `type=raw,custom`,
          `type=raw,tags`
        ],
        flavor: [
          `latest=false`
        ]
      } as Inputs,
      {
        main: 'my',
        partial: ['custom', 'tags'],
        latest: false
      } as Version,
      [
        'user/app:my',
        'user/app:custom',
        'user/app:tags'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=my"
      ],
      undefined
    ],
    [
      'raw09',
      'event_push_dev.env',
      {
        images: ['user/app'],
        tags: [
          `type=match,pattern=\\d{8}`,
          `type=raw,my,prefix=foo-,suffix=-bar`,
          `type=raw,custom`,
          `type=raw,tags`
        ],
        flavor: [
          `latest=false`,
          `prefix=glo-`,
          `suffix=-bal`
        ]
      } as Inputs,
      {
        main: 'foo-my-bar',
        partial: ['glo-custom-bal', 'glo-tags-bal'],
        latest: false
      } as Version,
      [
        'user/app:foo-my-bar',
        'user/app:glo-custom-bal',
        'user/app:glo-tags-bal'
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=foo-my-bar"
      ],
      undefined
    ],
    [
      'raw10',
      'event_push_dev.env',
      {
        images: ['user/app'],
        tags: [
          `type=raw,foo`,
          `type=raw,bar,enable=false`,
          `type=raw,baz,enable=true`
        ],
        flavor: [
          `latest=false`
        ]
      } as Inputs,
      {
        main: 'foo',
        partial: ['baz'],
        latest: false
      } as Version,
      [
        'user/app:foo',
        'user/app:baz',
      ],
      [
        "org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
        "org.opencontainers.image.description=This your first repo!",
        "org.opencontainers.image.licenses=MIT",
        "org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
        "org.opencontainers.image.source=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.title=Hello-World",
        "org.opencontainers.image.url=https://github.com/octocat/Hello-World",
        "org.opencontainers.image.version=foo"
      ],
      undefined
    ],
  ])('given %o with %o event', tagsLabelsTest);
});

describe('json', () => {
  // prettier-ignore
  test.each([
    [
      'json01',
      'event_push_dev.env',
      {
        images: ['user/app'],
        tags: [
          `type=ref,event=branch`,
          `type=raw,my`,
          `type=raw,custom`,
          `type=raw,tags`
        ],
        labels: [
          "invalid",
          "foo="
        ]
      } as Inputs,
      {
        "tags": [
          "user/app:dev",
          "user/app:my",
          "user/app:custom",
          "user/app:tags"
        ],
        "tag-names": [
          "dev",
          "my",
          "custom",
          "tags"
        ],
        "labels": {
          "foo": "",
          "org.opencontainers.image.created": "2020-01-10T00:30:00.000Z",
          "org.opencontainers.image.description": "This your first repo!",
          "org.opencontainers.image.licenses": "MIT",
          "org.opencontainers.image.revision": "860c1904a1ce19322e91ac35af1ab07466440c37",
          "org.opencontainers.image.source": "https://github.com/octocat/Hello-World",
          "org.opencontainers.image.title": "Hello-World",
          "org.opencontainers.image.url": "https://github.com/octocat/Hello-World",
          "org.opencontainers.image.version": "dev"
        },
        "annotations": [
          "manifest:org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
          "manifest:org.opencontainers.image.description=This your first repo!",
          "manifest:org.opencontainers.image.licenses=MIT",
          "manifest:org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
          "manifest:org.opencontainers.image.source=https://github.com/octocat/Hello-World",
          "manifest:org.opencontainers.image.title=Hello-World",
          "manifest:org.opencontainers.image.url=https://github.com/octocat/Hello-World",
          "manifest:org.opencontainers.image.version=dev"
        ]
      }
    ],
    [
      'json02',
      'event_push_dev.env',
      {
        images: ['user/app'],
        tags: [
          `type=ref,event=branch`,
          `type=raw,my`
        ]
      } as Inputs,
      {
        "tags": [
          "user/app:dev",
          "user/app:my",
        ],
        "tag-names": [
          "dev",
          "my",
        ],
        "labels": {
          "org.opencontainers.image.created": "2020-01-10T00:30:00.000Z",
          "org.opencontainers.image.description": "This your first repo!",
          "org.opencontainers.image.licenses": "MIT",
          "org.opencontainers.image.revision": "860c1904a1ce19322e91ac35af1ab07466440c37",
          "org.opencontainers.image.source": "https://github.com/octocat/Hello-World",
          "org.opencontainers.image.title": "Hello-World",
          "org.opencontainers.image.url": "https://github.com/octocat/Hello-World",
          "org.opencontainers.image.version": "dev"
        },
        "annotations": [
          "manifest:org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
          "manifest:org.opencontainers.image.description=This your first repo!",
          "manifest:org.opencontainers.image.licenses=MIT",
          "manifest:org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
          "manifest:org.opencontainers.image.source=https://github.com/octocat/Hello-World",
          "manifest:org.opencontainers.image.title=Hello-World",
          "manifest:org.opencontainers.image.url=https://github.com/octocat/Hello-World",
          "manifest:org.opencontainers.image.version=dev"
        ]
      }
    ],
    [
      'json03',
      'event_tag_release1.env',
      {
        images: ['user/app'],
        tags: [
          `type=ref,event=tag`,
          `type=raw,my`,
          `type=raw,custom`,
          `type=raw,tags`
        ],
        bakeTarget: "meta"
      } as Inputs,
      {
        "tags": [
          "user/app:release1",
          "user/app:my",
          "user/app:custom",
          "user/app:tags",
          "user/app:latest"
        ],
        "tag-names": [
          "release1",
          "my",
          "custom",
          "tags",
          "latest"
        ],
        "labels": {
          "org.opencontainers.image.created": "2020-01-10T00:30:00.000Z",
          "org.opencontainers.image.description": "This your first repo!",
          "org.opencontainers.image.licenses": "MIT",
          "org.opencontainers.image.revision": "860c1904a1ce19322e91ac35af1ab07466440c37",
          "org.opencontainers.image.source": "https://github.com/octocat/Hello-World",
          "org.opencontainers.image.title": "Hello-World",
          "org.opencontainers.image.url": "https://github.com/octocat/Hello-World",
          "org.opencontainers.image.version": "release1"
        },
        "annotations": [
          "manifest:org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
          "manifest:org.opencontainers.image.description=This your first repo!",
          "manifest:org.opencontainers.image.licenses=MIT",
          "manifest:org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
          "manifest:org.opencontainers.image.source=https://github.com/octocat/Hello-World",
          "manifest:org.opencontainers.image.title=Hello-World",
          "manifest:org.opencontainers.image.url=https://github.com/octocat/Hello-World",
          "manifest:org.opencontainers.image.version=release1"
        ]
      }
    ],
    [
      'json04',
      'event_tag_20200110-RC2.env',
      {
        images: ['user/app'],
        tags: [
          `type=match,pattern=\\d{8}`,
          `type=raw,my`,
          `type=raw,custom`,
          `type=raw,tags`
        ],
        flavor: [
          `latest=false`
        ]
      } as Inputs,
      {
        "tags": [
          "user/app:20200110",
          "user/app:my",
          "user/app:custom",
          "user/app:tags"
        ],
        "tag-names": [
          "20200110",
          "my",
          "custom",
          "tags"
        ],
        "labels": {
          "org.opencontainers.image.created": "2020-01-10T00:30:00.000Z",
          "org.opencontainers.image.description": "This your first repo!",
          "org.opencontainers.image.licenses": "MIT",
          "org.opencontainers.image.revision": "860c1904a1ce19322e91ac35af1ab07466440c37",
          "org.opencontainers.image.source": "https://github.com/octocat/Hello-World",
          "org.opencontainers.image.title": "Hello-World",
          "org.opencontainers.image.url": "https://github.com/octocat/Hello-World",
          "org.opencontainers.image.version": "20200110"
        },
        "annotations": [
          "manifest:org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
          "manifest:org.opencontainers.image.description=This your first repo!",
          "manifest:org.opencontainers.image.licenses=MIT",
          "manifest:org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
          "manifest:org.opencontainers.image.source=https://github.com/octocat/Hello-World",
          "manifest:org.opencontainers.image.title=Hello-World",
          "manifest:org.opencontainers.image.url=https://github.com/octocat/Hello-World",
          "manifest:org.opencontainers.image.version=20200110"
        ]
      }
    ],
    [
      'json05',
      'event_tag_v1.1.1.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=semver,pattern={{version}}`,
          `type=semver,pattern={{major}}.{{minor}}`,
          `type=semver,pattern={{major}}`,
          `type=raw,my`,
          `type=raw,custom`,
          `type=raw,tags`
        ]
      } as Inputs,
      {
        "tags": [
          "org/app:1.1.1",
          "org/app:1.1",
          "org/app:1",
          "org/app:my",
          "org/app:custom",
          "org/app:tags",
          "org/app:latest",
          "ghcr.io/user/app:1.1.1",
          "ghcr.io/user/app:1.1",
          "ghcr.io/user/app:1",
          "ghcr.io/user/app:my",
          "ghcr.io/user/app:custom",
          "ghcr.io/user/app:tags",
          "ghcr.io/user/app:latest"
        ],
        "tag-names": [
          "1.1.1",
          "1.1",
          "1",
          "my",
          "custom",
          "tags",
          "latest",
        ],
        "labels": {
          "org.opencontainers.image.created": "2020-01-10T00:30:00.000Z",
          "org.opencontainers.image.description": "This your first repo!",
          "org.opencontainers.image.licenses": "MIT",
          "org.opencontainers.image.revision": "860c1904a1ce19322e91ac35af1ab07466440c37",
          "org.opencontainers.image.source": "https://github.com/octocat/Hello-World",
          "org.opencontainers.image.title": "Hello-World",
          "org.opencontainers.image.url": "https://github.com/octocat/Hello-World",
          "org.opencontainers.image.version": "1.1.1"
        },
        "annotations": [
          "manifest:org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
          "manifest:org.opencontainers.image.description=This your first repo!",
          "manifest:org.opencontainers.image.licenses=MIT",
          "manifest:org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
          "manifest:org.opencontainers.image.source=https://github.com/octocat/Hello-World",
          "manifest:org.opencontainers.image.title=Hello-World",
          "manifest:org.opencontainers.image.url=https://github.com/octocat/Hello-World",
          "manifest:org.opencontainers.image.version=1.1.1"
        ]
      }
    ],
    [
      'json06',
      'event_tag_v1.1.1.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=raw,my`,
          `type=raw,custom`,
          `type=raw,tags`
        ]
      } as Inputs,
      {
        "tags": [
          "org/app:my",
          "org/app:custom",
          "org/app:tags",
          "ghcr.io/user/app:my",
          "ghcr.io/user/app:custom",
          "ghcr.io/user/app:tags"
        ],
        "tag-names": [
          "my",
          "custom",
          "tags",
        ],
        "labels": {
          "org.opencontainers.image.created": "2020-01-10T00:30:00.000Z",
          "org.opencontainers.image.description": "This your first repo!",
          "org.opencontainers.image.licenses": "MIT",
          "org.opencontainers.image.revision": "860c1904a1ce19322e91ac35af1ab07466440c37",
          "org.opencontainers.image.source": "https://github.com/octocat/Hello-World",
          "org.opencontainers.image.title": "Hello-World",
          "org.opencontainers.image.url": "https://github.com/octocat/Hello-World",
          "org.opencontainers.image.version": "my"
        },
        "annotations": [
          "manifest:org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
          "manifest:org.opencontainers.image.description=This your first repo!",
          "manifest:org.opencontainers.image.licenses=MIT",
          "manifest:org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
          "manifest:org.opencontainers.image.source=https://github.com/octocat/Hello-World",
          "manifest:org.opencontainers.image.title=Hello-World",
          "manifest:org.opencontainers.image.url=https://github.com/octocat/Hello-World",
          "manifest:org.opencontainers.image.version=my"
        ]
      }
    ],
    [
      'json07',
      'event_tag_v1.1.1.env',
      {
        images: ['org/app'],
        labels: [
          "foo",
          "maintainer=CrazyMax",
          "org.opencontainers.image.title=MyCustom=Title",
          "org.opencontainers.image.description=Another description",
          "org.opencontainers.image.vendor=MyCompany",
        ],
      } as Inputs,
      {
        "tags": [
          "org/app:v1.1.1",
          "org/app:latest"
        ],
        "tag-names": [
          "v1.1.1",
          "latest"
        ],
        "labels": {
          "maintainer": "CrazyMax",
          "org.opencontainers.image.created": "2020-01-10T00:30:00.000Z",
          "org.opencontainers.image.description": "Another description",
          "org.opencontainers.image.licenses": "MIT",
          "org.opencontainers.image.revision": "860c1904a1ce19322e91ac35af1ab07466440c37",
          "org.opencontainers.image.source": "https://github.com/octocat/Hello-World",
          "org.opencontainers.image.title": "MyCustom=Title",
          "org.opencontainers.image.url": "https://github.com/octocat/Hello-World",
          "org.opencontainers.image.vendor": "MyCompany",
          "org.opencontainers.image.version": "v1.1.1"
        },
        "annotations": [
          "manifest:org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
          "manifest:org.opencontainers.image.description=This your first repo!",
          "manifest:org.opencontainers.image.licenses=MIT",
          "manifest:org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
          "manifest:org.opencontainers.image.source=https://github.com/octocat/Hello-World",
          "manifest:org.opencontainers.image.title=Hello-World",
          "manifest:org.opencontainers.image.url=https://github.com/octocat/Hello-World",
          "manifest:org.opencontainers.image.version=v1.1.1"
        ]
      }
    ]
  ])('given %o with %o event', async (name: string, envFile: string, inputs: Inputs, exJSON: unknown) => {
    process.env = dotenv.parse(fs.readFileSync(path.join(__dirname, 'fixtures', envFile)));

    const toolkit = new Toolkit();
    const repo = await toolkit.github.repoData();
    const meta = new Meta({...getInputs(), ...inputs}, await getContext(ContextSource.workflow,toolkit), repo);

    const jsonOutput = meta.getJSON(['manifest']);
    expect(jsonOutput).toEqual(exJSON);
  });
});

describe('bakeFile', () => {
  // prettier-ignore
  test.each([
    [
      'bakeFile01',
      'event_push_dev.env',
      {
        images: ['user/app'],
        tags: [
          `type=ref,event=branch`,
          `type=raw,my`,
          `type=raw,custom`,
          `type=raw,tags`
        ],
        labels: [
          "invalid"
        ]
      } as Inputs,
      {
        "target": {
          "docker-metadata-action": {
            "tags": [
              "user/app:dev",
              "user/app:my",
              "user/app:custom",
              "user/app:tags"
            ],
            "args": {
              "DOCKER_META_IMAGES": "user/app",
              "DOCKER_META_VERSION": "dev",
            }
          }
        }
      },
      {
        "target": {
          "docker-metadata-action": {
            "labels": {
              "org.opencontainers.image.created": "2020-01-10T00:30:00.000Z",
              "org.opencontainers.image.description": "This your first repo!",
              "org.opencontainers.image.licenses": "MIT",
              "org.opencontainers.image.revision": "860c1904a1ce19322e91ac35af1ab07466440c37",
              "org.opencontainers.image.source": "https://github.com/octocat/Hello-World",
              "org.opencontainers.image.title": "Hello-World",
              "org.opencontainers.image.url": "https://github.com/octocat/Hello-World",
              "org.opencontainers.image.version": "dev"
            }
          }
        }
      },
      {
        "target": {
          "docker-metadata-action": {
            "annotations": [
              "index:org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
              "index:org.opencontainers.image.description=This your first repo!",
              "index:org.opencontainers.image.licenses=MIT",
              "index:org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
              "index:org.opencontainers.image.source=https://github.com/octocat/Hello-World",
              "index:org.opencontainers.image.title=Hello-World",
              "index:org.opencontainers.image.url=https://github.com/octocat/Hello-World",
              "index:org.opencontainers.image.version=dev",
              "manifest-descriptor:org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
              "manifest-descriptor:org.opencontainers.image.description=This your first repo!",
              "manifest-descriptor:org.opencontainers.image.licenses=MIT",
              "manifest-descriptor:org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
              "manifest-descriptor:org.opencontainers.image.source=https://github.com/octocat/Hello-World",
              "manifest-descriptor:org.opencontainers.image.title=Hello-World",
              "manifest-descriptor:org.opencontainers.image.url=https://github.com/octocat/Hello-World",
              "manifest-descriptor:org.opencontainers.image.version=dev"
            ]
          }
        }
      }
    ],
    [
      'bakeFile02',
      'event_push_dev.env',
      {
        images: ['user/app'],
        tags: [
          `type=ref,event=branch`,
          `type=raw,my`
        ]
      } as Inputs,
      {
        "target": {
          "docker-metadata-action": {
            "tags": [
              "user/app:dev",
              "user/app:my",
            ],
            "args": {
              "DOCKER_META_IMAGES": "user/app",
              "DOCKER_META_VERSION": "dev",
            }
          }
        }
      },
      {
        "target": {
          "docker-metadata-action": {
            "labels": {
              "org.opencontainers.image.created": "2020-01-10T00:30:00.000Z",
              "org.opencontainers.image.description": "This your first repo!",
              "org.opencontainers.image.licenses": "MIT",
              "org.opencontainers.image.revision": "860c1904a1ce19322e91ac35af1ab07466440c37",
              "org.opencontainers.image.source": "https://github.com/octocat/Hello-World",
              "org.opencontainers.image.title": "Hello-World",
              "org.opencontainers.image.url": "https://github.com/octocat/Hello-World",
              "org.opencontainers.image.version": "dev"
            }
          }
        }
      },
      {
        "target": {
          "docker-metadata-action": {
            "annotations": [
              "index:org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
              "index:org.opencontainers.image.description=This your first repo!",
              "index:org.opencontainers.image.licenses=MIT",
              "index:org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
              "index:org.opencontainers.image.source=https://github.com/octocat/Hello-World",
              "index:org.opencontainers.image.title=Hello-World",
              "index:org.opencontainers.image.url=https://github.com/octocat/Hello-World",
              "index:org.opencontainers.image.version=dev",
              "manifest-descriptor:org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
              "manifest-descriptor:org.opencontainers.image.description=This your first repo!",
              "manifest-descriptor:org.opencontainers.image.licenses=MIT",
              "manifest-descriptor:org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
              "manifest-descriptor:org.opencontainers.image.source=https://github.com/octocat/Hello-World",
              "manifest-descriptor:org.opencontainers.image.title=Hello-World",
              "manifest-descriptor:org.opencontainers.image.url=https://github.com/octocat/Hello-World",
              "manifest-descriptor:org.opencontainers.image.version=dev"
            ]
          }
        }
      }
    ],
    [
      'bakeFile03',
      'event_tag_release1.env',
      {
        images: ['user/app'],
        tags: [
          `type=ref,event=tag`,
          `type=raw,my`,
          `type=raw,custom`,
          `type=raw,tags`
        ],
        bakeTarget: "meta"
      } as Inputs,
      {
        "target": {
          "meta": {
            "tags": [
              "user/app:release1",
              "user/app:my",
              "user/app:custom",
              "user/app:tags",
              "user/app:latest"
            ],
            "args": {
              "DOCKER_META_IMAGES": "user/app",
              "DOCKER_META_VERSION": "release1",
            }
          }
        }
      },
      {
        "target": {
          "meta": {
            "labels": {
              "org.opencontainers.image.created": "2020-01-10T00:30:00.000Z",
              "org.opencontainers.image.description": "This your first repo!",
              "org.opencontainers.image.licenses": "MIT",
              "org.opencontainers.image.revision": "860c1904a1ce19322e91ac35af1ab07466440c37",
              "org.opencontainers.image.source": "https://github.com/octocat/Hello-World",
              "org.opencontainers.image.title": "Hello-World",
              "org.opencontainers.image.url": "https://github.com/octocat/Hello-World",
              "org.opencontainers.image.version": "release1"
            }
          }
        }
      },
      {
        "target": {
          "meta": {
            "annotations": [
              "index:org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
              "index:org.opencontainers.image.description=This your first repo!",
              "index:org.opencontainers.image.licenses=MIT",
              "index:org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
              "index:org.opencontainers.image.source=https://github.com/octocat/Hello-World",
              "index:org.opencontainers.image.title=Hello-World",
              "index:org.opencontainers.image.url=https://github.com/octocat/Hello-World",
              "index:org.opencontainers.image.version=release1",
              "manifest-descriptor:org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
              "manifest-descriptor:org.opencontainers.image.description=This your first repo!",
              "manifest-descriptor:org.opencontainers.image.licenses=MIT",
              "manifest-descriptor:org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
              "manifest-descriptor:org.opencontainers.image.source=https://github.com/octocat/Hello-World",
              "manifest-descriptor:org.opencontainers.image.title=Hello-World",
              "manifest-descriptor:org.opencontainers.image.url=https://github.com/octocat/Hello-World",
              "manifest-descriptor:org.opencontainers.image.version=release1"
            ]
          }
        }
      }
    ],
    [
      'bakeFile04',
      'event_tag_20200110-RC2.env',
      {
        images: ['user/app'],
        tags: [
          `type=match,pattern=\\d{8}`,
          `type=raw,my`,
          `type=raw,custom`,
          `type=raw,tags`
        ],
        flavor: [
          `latest=false`
        ]
      } as Inputs,
      {
        "target": {
          "docker-metadata-action": {
            "tags": [
              "user/app:20200110",
              "user/app:my",
              "user/app:custom",
              "user/app:tags"
            ],
            "args": {
              "DOCKER_META_IMAGES": "user/app",
              "DOCKER_META_VERSION": "20200110",
            }
          }
        }
      },
      {
        "target": {
          "docker-metadata-action": {
            "labels": {
              "org.opencontainers.image.created": "2020-01-10T00:30:00.000Z",
              "org.opencontainers.image.description": "This your first repo!",
              "org.opencontainers.image.licenses": "MIT",
              "org.opencontainers.image.revision": "860c1904a1ce19322e91ac35af1ab07466440c37",
              "org.opencontainers.image.source": "https://github.com/octocat/Hello-World",
              "org.opencontainers.image.title": "Hello-World",
              "org.opencontainers.image.url": "https://github.com/octocat/Hello-World",
              "org.opencontainers.image.version": "20200110"
            }
          }
        }
      },
      {
        "target": {
          "docker-metadata-action": {
            "annotations": [
              "index:org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
              "index:org.opencontainers.image.description=This your first repo!",
              "index:org.opencontainers.image.licenses=MIT",
              "index:org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
              "index:org.opencontainers.image.source=https://github.com/octocat/Hello-World",
              "index:org.opencontainers.image.title=Hello-World",
              "index:org.opencontainers.image.url=https://github.com/octocat/Hello-World",
              "index:org.opencontainers.image.version=20200110",
              "manifest-descriptor:org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
              "manifest-descriptor:org.opencontainers.image.description=This your first repo!",
              "manifest-descriptor:org.opencontainers.image.licenses=MIT",
              "manifest-descriptor:org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
              "manifest-descriptor:org.opencontainers.image.source=https://github.com/octocat/Hello-World",
              "manifest-descriptor:org.opencontainers.image.title=Hello-World",
              "manifest-descriptor:org.opencontainers.image.url=https://github.com/octocat/Hello-World",
              "manifest-descriptor:org.opencontainers.image.version=20200110"
            ]
          }
        }
      }
    ],
    [
      'bakeFile05',
      'event_tag_v1.1.1.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=semver,pattern={{version}}`,
          `type=semver,pattern={{major}}.{{minor}}`,
          `type=semver,pattern={{major}}`,
          `type=raw,my`,
          `type=raw,custom`,
          `type=raw,tags`
        ]
      } as Inputs,
      {
        "target": {
          "docker-metadata-action": {
            "tags": [
              "org/app:1.1.1",
              "org/app:1.1",
              "org/app:1",
              "org/app:my",
              "org/app:custom",
              "org/app:tags",
              "org/app:latest",
              "ghcr.io/user/app:1.1.1",
              "ghcr.io/user/app:1.1",
              "ghcr.io/user/app:1",
              "ghcr.io/user/app:my",
              "ghcr.io/user/app:custom",
              "ghcr.io/user/app:tags",
              "ghcr.io/user/app:latest"
            ],
            "args": {
              "DOCKER_META_IMAGES": "org/app,ghcr.io/user/app",
              "DOCKER_META_VERSION": "1.1.1",
            }
          }
        }
      },
      {
        "target": {
          "docker-metadata-action": {
            "labels": {
              "org.opencontainers.image.created": "2020-01-10T00:30:00.000Z",
              "org.opencontainers.image.description": "This your first repo!",
              "org.opencontainers.image.licenses": "MIT",
              "org.opencontainers.image.revision": "860c1904a1ce19322e91ac35af1ab07466440c37",
              "org.opencontainers.image.source": "https://github.com/octocat/Hello-World",
              "org.opencontainers.image.title": "Hello-World",
              "org.opencontainers.image.url": "https://github.com/octocat/Hello-World",
              "org.opencontainers.image.version": "1.1.1"
            }
          }
        }
      },
      {
        "target": {
          "docker-metadata-action": {
            "annotations": [
              "index:org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
              "index:org.opencontainers.image.description=This your first repo!",
              "index:org.opencontainers.image.licenses=MIT",
              "index:org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
              "index:org.opencontainers.image.source=https://github.com/octocat/Hello-World",
              "index:org.opencontainers.image.title=Hello-World",
              "index:org.opencontainers.image.url=https://github.com/octocat/Hello-World",
              "index:org.opencontainers.image.version=1.1.1",
              "manifest-descriptor:org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
              "manifest-descriptor:org.opencontainers.image.description=This your first repo!",
              "manifest-descriptor:org.opencontainers.image.licenses=MIT",
              "manifest-descriptor:org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
              "manifest-descriptor:org.opencontainers.image.source=https://github.com/octocat/Hello-World",
              "manifest-descriptor:org.opencontainers.image.title=Hello-World",
              "manifest-descriptor:org.opencontainers.image.url=https://github.com/octocat/Hello-World",
              "manifest-descriptor:org.opencontainers.image.version=1.1.1"
            ]
          }
        }
      }
    ],
    [
      'bakeFile06',
      'event_tag_v1.1.1.env',
      {
        images: ['org/app', 'ghcr.io/user/app'],
        tags: [
          `type=raw,my`,
          `type=raw,custom`,
          `type=raw,tags`
        ]
      } as Inputs,
      {
        "target": {
          "docker-metadata-action": {
            "tags": [
              "org/app:my",
              "org/app:custom",
              "org/app:tags",
              "ghcr.io/user/app:my",
              "ghcr.io/user/app:custom",
              "ghcr.io/user/app:tags"
            ],
            "args": {
              "DOCKER_META_IMAGES": "org/app,ghcr.io/user/app",
              "DOCKER_META_VERSION": "my",
            }
          }
        }
      },
      {
        "target": {
          "docker-metadata-action": {
            "labels": {
              "org.opencontainers.image.created": "2020-01-10T00:30:00.000Z",
              "org.opencontainers.image.description": "This your first repo!",
              "org.opencontainers.image.licenses": "MIT",
              "org.opencontainers.image.revision": "860c1904a1ce19322e91ac35af1ab07466440c37",
              "org.opencontainers.image.source": "https://github.com/octocat/Hello-World",
              "org.opencontainers.image.title": "Hello-World",
              "org.opencontainers.image.url": "https://github.com/octocat/Hello-World",
              "org.opencontainers.image.version": "my"
            }
          }
        }
      },
      {
        "target": {
          "docker-metadata-action": {
            "annotations": [
              "index:org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
              "index:org.opencontainers.image.description=This your first repo!",
              "index:org.opencontainers.image.licenses=MIT",
              "index:org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
              "index:org.opencontainers.image.source=https://github.com/octocat/Hello-World",
              "index:org.opencontainers.image.title=Hello-World",
              "index:org.opencontainers.image.url=https://github.com/octocat/Hello-World",
              "index:org.opencontainers.image.version=my",
              "manifest-descriptor:org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
              "manifest-descriptor:org.opencontainers.image.description=This your first repo!",
              "manifest-descriptor:org.opencontainers.image.licenses=MIT",
              "manifest-descriptor:org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
              "manifest-descriptor:org.opencontainers.image.source=https://github.com/octocat/Hello-World",
              "manifest-descriptor:org.opencontainers.image.title=Hello-World",
              "manifest-descriptor:org.opencontainers.image.url=https://github.com/octocat/Hello-World",
              "manifest-descriptor:org.opencontainers.image.version=my"
            ]
          }
        }
      }
    ],
    [
      'bakeFile07',
      'event_tag_v1.1.1.env',
      {
        images: ['org/app'],
        labels: [
          "maintainer=CrazyMax",
          "org.opencontainers.image.title=MyCustom=Title",
          "org.opencontainers.image.description=Another description",
          "org.opencontainers.image.vendor=MyCompany",
        ],
      } as Inputs,
      {
        "target": {
          "docker-metadata-action": {
            "tags": [
              "org/app:v1.1.1",
              "org/app:latest"
            ],
            "args": {
              "DOCKER_META_IMAGES": "org/app",
              "DOCKER_META_VERSION": "v1.1.1",
            }
          }
        }
      },
      {
        "target": {
          "docker-metadata-action": {
            "labels": {
              "maintainer": "CrazyMax",
              "org.opencontainers.image.created": "2020-01-10T00:30:00.000Z",
              "org.opencontainers.image.description": "Another description",
              "org.opencontainers.image.licenses": "MIT",
              "org.opencontainers.image.revision": "860c1904a1ce19322e91ac35af1ab07466440c37",
              "org.opencontainers.image.source": "https://github.com/octocat/Hello-World",
              "org.opencontainers.image.title": "MyCustom=Title",
              "org.opencontainers.image.url": "https://github.com/octocat/Hello-World",
              "org.opencontainers.image.vendor": "MyCompany",
              "org.opencontainers.image.version": "v1.1.1"
            }
          }
        }
      },
      {
        "target": {
          "docker-metadata-action": {
            "annotations": [
              "index:org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
              "index:org.opencontainers.image.description=This your first repo!",
              "index:org.opencontainers.image.licenses=MIT",
              "index:org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
              "index:org.opencontainers.image.source=https://github.com/octocat/Hello-World",
              "index:org.opencontainers.image.title=Hello-World",
              "index:org.opencontainers.image.url=https://github.com/octocat/Hello-World",
              "index:org.opencontainers.image.version=v1.1.1",
              "manifest-descriptor:org.opencontainers.image.created=2020-01-10T00:30:00.000Z",
              "manifest-descriptor:org.opencontainers.image.description=This your first repo!",
              "manifest-descriptor:org.opencontainers.image.licenses=MIT",
              "manifest-descriptor:org.opencontainers.image.revision=860c1904a1ce19322e91ac35af1ab07466440c37",
              "manifest-descriptor:org.opencontainers.image.source=https://github.com/octocat/Hello-World",
              "manifest-descriptor:org.opencontainers.image.title=Hello-World",
              "manifest-descriptor:org.opencontainers.image.url=https://github.com/octocat/Hello-World",
              "manifest-descriptor:org.opencontainers.image.version=v1.1.1"
            ]
          }
        }
      }
    ]
  ])('given %o with %o event', async (name: string, envFile: string, inputs: Inputs, exBakeTags: unknown, exBakeLabels: unknown, exBakeAnnotations: unknown) => {
    process.env = dotenv.parse(fs.readFileSync(path.join(__dirname, 'fixtures', envFile)));

    const toolkit = new Toolkit();
    const repo = await toolkit.github.repoData();
    const meta = new Meta({...getInputs(), ...inputs}, await getContext(ContextSource.workflow,toolkit), repo);

    const bakeFileTags = meta.getBakeFile('tags');
    expect(JSON.parse(fs.readFileSync(bakeFileTags, 'utf8'))).toEqual(exBakeTags);

    const bakeFileLabels = meta.getBakeFile('labels');
    expect(JSON.parse(fs.readFileSync(bakeFileLabels, 'utf8'))).toEqual(exBakeLabels);

    const bakeFileAnnotations = meta.getBakeFile('annotations:index,manifest-descriptor');
    expect(JSON.parse(fs.readFileSync(bakeFileAnnotations, 'utf8'))).toEqual(exBakeAnnotations);
  });
});

describe('bakeFileTagsLabels', () => {
  // prettier-ignore
  test.each([
    [
      'bakeFileTagsLabels01',
      'event_push_dev.env',
      {
        images: ['user/app'],
        tags: [
          `type=ref,event=branch`,
          `type=raw,my`,
          `type=raw,custom`,
          `type=raw,tags`
        ],
        labels: [
          "invalid"
        ]
      } as Inputs,
      {
        "target": {
          "docker-metadata-action": {
            "tags": [
              "user/app:dev",
              "user/app:my",
              "user/app:custom",
              "user/app:tags"
            ],
            "labels": {
              "org.opencontainers.image.created": "2020-01-10T00:30:00.000Z",
              "org.opencontainers.image.description": "This your first repo!",
              "org.opencontainers.image.licenses": "MIT",
              "org.opencontainers.image.revision": "860c1904a1ce19322e91ac35af1ab07466440c37",
              "org.opencontainers.image.source": "https://github.com/octocat/Hello-World",
              "org.opencontainers.image.title": "Hello-World",
              "org.opencontainers.image.url": "https://github.com/octocat/Hello-World",
              "org.opencontainers.image.version": "dev"
            },
            "args": {
              "DOCKER_META_IMAGES": "user/app",
              "DOCKER_META_VERSION": "dev",
            }
          }
        }
      }
    ]
  ])('given %o with %o event', async (name: string, envFile: string, inputs: Inputs, exBakeDefinition: unknown) => {
    process.env = dotenv.parse(fs.readFileSync(path.join(__dirname, 'fixtures', envFile)));

    const toolkit = new Toolkit();
    const repo = await toolkit.github.repoData();
    const meta = new Meta({...getInputs(), ...inputs}, await getContext(ContextSource.workflow,toolkit), repo);

    const bakeFile = meta.getBakeFileTagsLabels();
    expect(JSON.parse(fs.readFileSync(bakeFile, 'utf8'))).toEqual(exBakeDefinition);
  });
});

describe('sepTags', () => {
  // prettier-ignore
  test.each([
    [
      'sepTags01',
      'event_push_dev.env',
      {
        images: ['user/app'],
        tags: [
          `type=ref,event=branch`,
          `type=raw,my`,
          `type=raw,custom`,
          `type=raw,tags`
        ],
        sepTags: " "
      } as Inputs,
      "user/app:dev user/app:my user/app:custom user/app:tags"
    ],
    [
      'sepTags02',
      'event_push_dev.env',
      {
        images: ['user/app'],
        tags: [
          `type=ref,event=branch`,
          `type=raw,my`,
          `type=raw,custom`,
          `type=raw,tags`
        ],
        sepTags: ","
      } as Inputs,
      "user/app:dev,user/app:my,user/app:custom,user/app:tags"
    ]
  ])('given %o with %o event', async (name: string, envFile: string, inputs: Inputs, expTags: string) => {
    process.env = dotenv.parse(fs.readFileSync(path.join(__dirname, 'fixtures', envFile)));

    const toolkit = new Toolkit();
    const repo = await toolkit.github.repoData();
    const meta = new Meta({...getInputs(), ...inputs}, await getContext(ContextSource.workflow, toolkit), repo);

    expect(meta.getTags().join(inputs.sepTags)).toEqual(expTags);
  });
});
```

## File: `__tests__/setup.unit.ts`
```typescript
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {vi} from 'vitest';

const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'docker-metadata-action-'));

const githubPayload = {
  after: '860c1904a1ce19322e91ac35af1ab07466440c37',
  base_ref: null,
  before: '5f3331d7f7044c18ca9f12c77d961c4d7cf3276a',
  commits: [
    {
      author: {
        email: 'crazy-max@users.noreply.github.com',
        name: 'CrazyMax',
        username: 'crazy-max'
      },
      committer: {
        email: 'crazy-max@users.noreply.github.com',
        name: 'CrazyMax',
        username: 'crazy-max'
      },
      distinct: true,
      id: '5f3331d7f7044c18ca9f12c77d961c4d7cf3276a',
      message: 'hello dev',
      timestamp: '2024-11-13T13:42:28Z',
      tree_id: 'd2c60af597e863787d2d27f569e30495b0b92820',
      url: 'https://github.com/docker/test-docker-action/commit/5f3331d7f7044c18ca9f12c77d961c4d7cf3276a'
    }
  ],
  compare: 'https://github.com/docker/test-docker-action/compare/5f3331d7f704...860c1904a1ce',
  created: false,
  deleted: false,
  forced: false,
  head_commit: {
    author: {
      email: 'crazy-max@users.noreply.github.com',
      name: 'CrazyMax',
      username: 'crazy-max'
    },
    committer: {
      email: 'crazy-max@users.noreply.github.com',
      name: 'CrazyMax',
      username: 'crazy-max'
    },
    distinct: true,
    id: '5f3331d7f7044c18ca9f12c77d961c4d7cf3276a',
    message: 'hello dev',
    timestamp: '2024-11-13T13:42:28Z',
    tree_id: 'd2c60af597e863787d2d27f569e30495b0b92820',
    url: 'https://github.com/docker/test-docker-action/commit/5f3331d7f7044c18ca9f12c77d961c4d7cf3276a'
  },
  organization: {
    avatar_url: 'https://avatars.githubusercontent.com/u/5429470?v=4',
    description: 'Docker helps developers bring their ideas to life by conquering the complexity of app development.',
    events_url: 'https://api.github.com/orgs/docker/events',
    hooks_url: 'https://api.github.com/orgs/docker/hooks',
    id: 5429470,
    issues_url: 'https://api.github.com/orgs/docker/issues',
    login: 'docker',
    members_url: 'https://api.github.com/orgs/docker/members{/member}',
    node_id: 'MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=',
    public_members_url: 'https://api.github.com/orgs/docker/public_members{/member}',
    repos_url: 'https://api.github.com/orgs/docker/repos',
    url: 'https://api.github.com/orgs/docker'
  },
  pusher: {
    email: 'github@crazymax.dev',
    name: 'crazy-max'
  },
  ref: 'refs/heads/dev',
  repository: {
    allow_forking: true,
    archive_url: 'https://api.github.com/repos/docker/test-docker-action/{archive_format}{/ref}',
    archived: false,
    assignees_url: 'https://api.github.com/repos/docker/test-docker-action/assignees{/user}',
    blobs_url: 'https://api.github.com/repos/docker/test-docker-action/git/blobs{/sha}',
    branches_url: 'https://api.github.com/repos/docker/test-docker-action/branches{/branch}',
    clone_url: 'https://github.com/docker/test-docker-action.git',
    collaborators_url: 'https://api.github.com/repos/docker/test-docker-action/collaborators{/collaborator}',
    comments_url: 'https://api.github.com/repos/docker/test-docker-action/comments{/number}',
    commits_url: 'https://api.github.com/repos/docker/test-docker-action/commits{/sha}',
    compare_url: 'https://api.github.com/repos/docker/test-docker-action/compare/{base}...{head}',
    contents_url: 'https://api.github.com/repos/docker/test-docker-action/contents/{+path}',
    contributors_url: 'https://api.github.com/repos/docker/test-docker-action/contributors',
    created_at: 1596792180,
    default_branch: 'master',
    deployments_url: 'https://api.github.com/repos/docker/test-docker-action/deployments',
    description: 'Test "Docker" Actions',
    disabled: false,
    downloads_url: 'https://api.github.com/repos/docker/test-docker-action/downloads',
    events_url: 'https://api.github.com/repos/docker/test-docker-action/events',
    fork: false,
    forks: 1,
    forks_count: 1,
    forks_url: 'https://api.github.com/repos/docker/test-docker-action/forks',
    full_name: 'docker/test-docker-action',
    git_commits_url: 'https://api.github.com/repos/docker/test-docker-action/git/commits{/sha}',
    git_refs_url: 'https://api.github.com/repos/docker/test-docker-action/git/refs{/sha}',
    git_tags_url: 'https://api.github.com/repos/docker/test-docker-action/git/tags{/sha}',
    git_url: 'git://github.com/docker/test-docker-action.git',
    has_downloads: true,
    has_issues: true,
    has_pages: false,
    has_projects: true,
    has_wiki: true,
    homepage: '',
    hooks_url: 'https://api.github.com/repos/docker/test-docker-action/hooks',
    html_url: 'https://github.com/docker/test-docker-action',
    id: 285789493,
    is_template: false,
    issue_comment_url: 'https://api.github.com/repos/docker/test-docker-action/issues/comments{/number}',
    issue_events_url: 'https://api.github.com/repos/docker/test-docker-action/issues/events{/number}',
    issues_url: 'https://api.github.com/repos/docker/test-docker-action/issues{/number}',
    keys_url: 'https://api.github.com/repos/docker/test-docker-action/keys{/key_id}',
    labels_url: 'https://api.github.com/repos/docker/test-docker-action/labels{/name}',
    language: 'JavaScript',
    languages_url: 'https://api.github.com/repos/docker/test-docker-action/languages',
    license: {
      key: 'mit',
      name: 'MIT License',
      node_id: 'MDc6TGljZW5zZTEz',
      spdx_id: 'MIT',
      url: 'https://api.github.com/licenses/mit'
    },
    master_branch: 'master',
    merges_url: 'https://api.github.com/repos/docker/test-docker-action/merges',
    milestones_url: 'https://api.github.com/repos/docker/test-docker-action/milestones{/number}',
    mirror_url: null,
    name: 'test-docker-action',
    node_id: 'MDEwOlJlcG9zaXRvcnkyODU3ODk0OTM=',
    notifications_url: 'https://api.github.com/repos/docker/test-docker-action/notifications{?since,all,participating}',
    open_issues: 6,
    open_issues_count: 6,
    organization: 'docker',
    owner: {
      avatar_url: 'https://avatars.githubusercontent.com/u/5429470?v=4',
      email: 'info@docker.com',
      events_url: 'https://api.github.com/users/docker/events{/privacy}',
      followers_url: 'https://api.github.com/users/docker/followers',
      following_url: 'https://api.github.com/users/docker/following{/other_user}',
      gists_url: 'https://api.github.com/users/docker/gists{/gist_id}',
      gravatar_id: '',
      html_url: 'https://github.com/docker',
      id: 5429470,
      login: 'docker',
      name: 'docker',
      node_id: 'MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=',
      organizations_url: 'https://api.github.com/users/docker/orgs',
      received_events_url: 'https://api.github.com/users/docker/received_events',
      repos_url: 'https://api.github.com/users/docker/repos',
      site_admin: false,
      starred_url: 'https://api.github.com/users/docker/starred{/owner}{/repo}',
      subscriptions_url: 'https://api.github.com/users/docker/subscriptions',
      type: 'Organization',
      url: 'https://api.github.com/users/docker'
    },
    private: true,
    pulls_url: 'https://api.github.com/repos/docker/test-docker-action/pulls{/number}',
    pushed_at: 1650360446,
    releases_url: 'https://api.github.com/repos/docker/test-docker-action/releases{/id}',
    size: 796,
    ssh_url: 'git@github.com:docker/test-docker-action.git',
    stargazers: 0,
    stargazers_count: 0,
    stargazers_url: 'https://api.github.com/repos/docker/test-docker-action/stargazers',
    statuses_url: 'https://api.github.com/repos/docker/test-docker-action/statuses/{sha}',
    subscribers_url: 'https://api.github.com/repos/docker/test-docker-action/subscribers',
    subscription_url: 'https://api.github.com/repos/docker/test-docker-action/subscription',
    svn_url: 'https://github.com/docker/test-docker-action',
    tags_url: 'https://api.github.com/repos/docker/test-docker-action/tags',
    teams_url: 'https://api.github.com/repos/docker/test-docker-action/teams',
    topics: [],
    trees_url: 'https://api.github.com/repos/docker/test-docker-action/git/trees{/sha}',
    updated_at: '2022-04-19T09:05:09Z',
    url: 'https://github.com/docker/test-docker-action',
    visibility: 'private',
    watchers: 0,
    watchers_count: 0
  },
  sender: {
    avatar_url: 'https://avatars.githubusercontent.com/u/1951866?v=4',
    events_url: 'https://api.github.com/users/crazy-max/events{/privacy}',
    followers_url: 'https://api.github.com/users/crazy-max/followers',
    following_url: 'https://api.github.com/users/crazy-max/following{/other_user}',
    gists_url: 'https://api.github.com/users/crazy-max/gists{/gist_id}',
    gravatar_id: '',
    html_url: 'https://github.com/crazy-max',
    id: 1951866,
    login: 'crazy-max',
    node_id: 'MDQ6VXNlcjE5NTE4NjY=',
    organizations_url: 'https://api.github.com/users/crazy-max/orgs',
    received_events_url: 'https://api.github.com/users/crazy-max/received_events',
    repos_url: 'https://api.github.com/users/crazy-max/repos',
    site_admin: false,
    starred_url: 'https://api.github.com/users/crazy-max/starred{/owner}{/repo}',
    subscriptions_url: 'https://api.github.com/users/crazy-max/subscriptions',
    type: 'User',
    url: 'https://api.github.com/users/crazy-max'
  }
};

const githubEventPath = path.join(tmpDir, 'github-event.json');
fs.writeFileSync(githubEventPath, JSON.stringify(githubPayload));

process.env = Object.assign({}, process.env, {
  TEMP: tmpDir,
  GITHUB_REPOSITORY: 'docker/metadata-action',
  GITHUB_REF: 'refs/heads/dev',
  GITHUB_RUN_ID: '2188748038',
  GITHUB_RUN_ATTEMPT: '1',
  GITHUB_RUN_NUMBER: '15',
  GITHUB_SHA: '5f3331d7f7044c18ca9f12c77d961c4d7cf3276a',
  GITHUB_EVENT_PATH: githubEventPath,
  RUNNER_TEMP: path.join(tmpDir, 'runner-temp'),
  RUNNER_TOOL_CACHE: path.join(tmpDir, 'runner-tool-cache')
});

const getCommitMock = vi.hoisted(() =>
  vi.fn(async () => ({
    data: {
      commit: {
        committer: {
          date: '2024-11-13T13:42:28Z'
        }
      }
    }
  }))
);

const getOctokitMock = vi.hoisted(() =>
  vi.fn(() => ({
    rest: {
      repos: {
        getCommit: getCommitMock
      }
    }
  }))
);

vi.mock('@actions/github', async importOriginal => {
  const actual = await importOriginal<typeof import('@actions/github')>();
  return {
    ...actual,
    context: {
      ...actual.context,
      payload: githubPayload
    },
    getOctokit: getOctokitMock
  };
});
```

## File: `__tests__/tag.test.ts`
```typescript
import {describe, expect, test} from 'vitest';

import {Transform, Parse, Tag, Type, RefEvent, ShaFormat, DefaultPriorities} from '../src/tag.js';

describe('transform', () => {
  // prettier-ignore
  test.each([
    [
      [
        `type=ref,event=branch`,
        `type=ref,event=tag`,
        `type=ref,event=pr`,
        `type=schedule`,
        `type=sha`,
        `type=raw,foo`,
        `type=edge`,
        `type=semver,pattern={{version}}`,
        `type=match,"pattern=\\d.\\d.\\d",group=0`
      ],
      [
        {
          type: Type.Schedule,
          attrs: {
            "priority": DefaultPriorities[Type.Schedule],
            "enable": "true",
            "pattern": "nightly"
          }
        },
        {
          type: Type.Semver,
          attrs: {
            "priority": DefaultPriorities[Type.Semver],
            "enable": "true",
            "pattern": "{{version}}",
            "value": "",
            "match": ""
          }
        },
        {
          type: Type.Match,
          attrs: {
            "priority": DefaultPriorities[Type.Match],
            "enable": "true",
            "pattern": "\\d.\\d.\\d",
            "group": "0",
            "value": ""
          }
        },
        {
          type: Type.Edge,
          attrs: {
            "priority": DefaultPriorities[Type.Edge],
            "enable": "true",
            "branch": ""
          }
        },
        {
          type: Type.Ref,
          attrs: {
            "priority": DefaultPriorities[Type.Ref],
            "enable": "true",
            "event": RefEvent.Branch
          }
        },
        {
          type: Type.Ref,
          attrs: {
            "priority": DefaultPriorities[Type.Ref],
            "enable": "true",
            "event": RefEvent.Tag
          }
        },
        {
          type: Type.Ref,
          attrs: {
            "priority": DefaultPriorities[Type.Ref],
            "enable": "true",
            "prefix": "pr-",
            "event": RefEvent.PR
          }
        },
        {
          type: Type.Raw,
          attrs: {
            "priority": DefaultPriorities[Type.Raw],
            "enable": "true",
            "value": "foo"
          }
        },
        {
          type: Type.Sha,
          attrs: {
            "priority": DefaultPriorities[Type.Sha],
            "enable": "true",
            "prefix": "sha-",
            "format": ShaFormat.Short
          }
        }
      ] as Tag[],
      false
    ]
  ])('given %p', async (l: string[], expected: Tag[], invalid: boolean) => {
    try {
      const tags = Transform(l);
      expect(tags).toEqual(expected);
    } catch (err) {
      if (!invalid) {
        console.error(err);
      }
      // eslint-disable-next-line vitest/no-conditional-expect
      expect(true).toBe(invalid);
    }
  });
});

describe('parse', () => {
  // prettier-ignore
  test.each([
    [
      `type=schedule,enable=true,pattern={{date 'YYYYMMDD'}}`,
      {
        type: Type.Schedule,
        attrs: {
          "priority": DefaultPriorities[Type.Schedule],
          "enable": "true",
          "pattern": "{{date 'YYYYMMDD'}}"
        }
      } as Tag,
      false
    ],
    [
      `type=schedule,enable=true,pattern={{date 'YYYYMMDD' tz='Asia/Tokyo'}}`,
      {
        type: Type.Schedule,
        attrs: {
          "priority": DefaultPriorities[Type.Schedule],
          "enable": "true",
          "pattern": `{{date 'YYYYMMDD' tz='Asia/Tokyo'}}`
        }
      } as Tag,
      false
    ],
    [
      `type=semver,enable=true,pattern={{version}}`,
      {
        type: Type.Semver,
        attrs: {
          "priority": DefaultPriorities[Type.Semver],
          "enable": "true",
          "pattern": "{{version}}",
          "value": "",
          "match": ""
        }
      } as Tag,
      false
    ],
    [
      `type=semver,priority=1,enable=true,pattern={{version}}`,
      {
        type: Type.Semver,
        attrs: {
          "priority": "1",
          "enable": "true",
          "pattern": "{{version}}",
          "value": "",
          "match": ""
        }
      } as Tag,
      false
    ],
    [
      `type=semver,priority=1,enable=true,pattern={{version}},value=v1.0.0`,
      {
        type: Type.Semver,
        attrs: {
          "priority": "1",
          "enable": "true",
          "pattern": "{{version}}",
          "value": "v1.0.0",
          "match": ""
        }
      } as Tag,
      false
    ],
    [
      `type=semver,priority=1,enable=true,pattern={{version}},value=p1/v1.0.0,"match=v(\\d.\\d.\\d)$"`,
      {
        type: Type.Semver,
        attrs: {
          "priority": "1",
          "enable": "true",
          "pattern": "{{version}}",
          "value": "p1/v1.0.0",
          "match": "v(\\d.\\d.\\d)$"
        }
      } as Tag,
      false
    ],
    [
      `type=match,enable=true,pattern=v(.*),group=1`,
      {
        type: Type.Match,
        attrs: {
          "priority": DefaultPriorities[Type.Match],
          "enable": "true",
          "pattern": "v(.*)",
          "group": "1",
          "value": ""
        }
      } as Tag,
      false
    ],
    [
      `type=match,enable=true,"pattern=^v(\\d.\\d.\\d)$",group=1`,
      {
        type: Type.Match,
        attrs: {
          "priority": DefaultPriorities[Type.Match],
          "enable": "true",
          "pattern": "^v(\\d.\\d.\\d)$",
          "group": "1",
          "value": ""
        }
      } as Tag,
      false
    ],
    [
      `type=match,priority=700,enable=true,pattern=v(.*),group=1`,
      {
        type: Type.Match,
        attrs: {
          "priority": "700",
          "enable": "true",
          "pattern": "v(.*)",
          "group": "1",
          "value": ""
        }
      } as Tag,
      false
    ],
    [
      `type=match,enable=true,pattern=v(.*),group=1,value=v1.2.3`,
      {
        type: Type.Match,
        attrs: {
          "priority": DefaultPriorities[Type.Match],
          "enable": "true",
          "pattern": "v(.*)",
          "group": "1",
          "value": "v1.2.3"
        }
      } as Tag,
      false
    ],
    [
      `type=match,enable=true,pattern=v(.*),group=foo`,
      {} as Tag,
      true
    ],
    [
      `type=edge`,
      {
        type: Type.Edge,
        attrs: {
          "priority": DefaultPriorities[Type.Edge],
          "enable": "true",
          "branch": ""
        }
      } as Tag,
      false
    ],
    [
      `type=edge,enable=true,branch=master`,
      {
        type: Type.Edge,
        attrs: {
          "priority": DefaultPriorities[Type.Edge],
          "enable": "true",
          "branch": "master"
        }
      } as Tag,
      false
    ],
    [
      `type=ref,event=tag`,
      {
        type: Type.Ref,
        attrs: {
          "priority": DefaultPriorities[Type.Ref],
          "enable": "true",
          "event": RefEvent.Tag
        }
      } as Tag,
      false
    ],
    [
      `type=ref,event=branch`,
      {
        type: Type.Ref,
        attrs: {
          "priority": DefaultPriorities[Type.Ref],
          "enable": "true",
          "event": RefEvent.Branch
        }
      } as Tag,
      false
    ],
    [
      `type=ref,event=pr`,
      {
        type: Type.Ref,
        attrs: {
          "priority": DefaultPriorities[Type.Ref],
          "enable": "true",
          "prefix": "pr-",
          "event": RefEvent.PR
        }
      } as Tag,
      false
    ],
    [
      `type=ref,event=foo`,
      {} as Tag,
      true
    ],
    [
      `type=ref`,
      {} as Tag,
      true
    ],
    [
      `acustomtag`,
      {
        type: Type.Raw,
        attrs: {
          "priority": DefaultPriorities[Type.Raw],
          "enable": "true",
          "value": "acustomtag"
        }
      } as Tag,
      false
    ],
    [
      `type=raw`,
      {} as Tag,
      true
    ],
    [
      `type=raw,value=acustomtag2`,
      {
        type: Type.Raw,
        attrs: {
          "priority": DefaultPriorities[Type.Raw],
          "enable": "true",
          "value": "acustomtag2"
        }
      } as Tag,
      false
    ],
    [
      `type=raw,enable=true,value=acustomtag4`,
      {
        type: Type.Raw,
        attrs: {
          "priority": DefaultPriorities[Type.Raw],
          "enable": "true",
          "value": "acustomtag4"
        }
      } as Tag,
      false
    ],
    [
      `type=raw,enable=false,value=acustomtag5`,
      {
        type: Type.Raw,
        attrs: {
          "priority": DefaultPriorities[Type.Raw],
          "enable": "false",
          "value": "acustomtag5"
        }
      } as Tag,
      false
    ],
    [
      `type=sha`,
      {
        type: Type.Sha,
        attrs: {
          "priority": DefaultPriorities[Type.Sha],
          "enable": "true",
          "prefix": "sha-",
          "format": ShaFormat.Short
        }
      } as Tag,
      false
    ],
    [
      `type=sha,format=long`,
      {
        type: Type.Sha,
        attrs: {
          "priority": DefaultPriorities[Type.Sha],
          "enable": "true",
          "prefix": "sha-",
          "format": ShaFormat.Long
        }
      } as Tag,
      false
    ],
    [
      `type=sha,prefix=`,
      {
        type: Type.Sha,
        attrs: {
          "priority": DefaultPriorities[Type.Sha],
          "enable": "true",
          "prefix": "",
          "format": ShaFormat.Short
        }
      } as Tag,
      false
    ],
    [
      `type=sha,enable=false`,
      {
        type: Type.Sha,
        attrs: {
          "priority": DefaultPriorities[Type.Sha],
          "enable": "false",
          "prefix": "sha-",
          "format": ShaFormat.Short
        }
      } as Tag,
      false
    ],
    [
      `type=semver`,
      {} as Tag,
      true
    ],
    [
      `type=match`,
      {} as Tag,
      true
    ],
    [
      `type=foo`,
      {} as Tag,
      true
    ],
    [
      `type=sha,format=foo`,
      {} as Tag,
      true
    ]
  ])('given %p event', async (s: string, expected: Tag, invalid: boolean) => {
    try {
      const tag = Parse(s);
      expect(tag).toEqual(expected);
    } catch (err) {
      if (!invalid) {
        console.error(err);
      }
      // eslint-disable-next-line vitest/no-conditional-expect
      expect(true).toBe(invalid);
    }
  });
});
```

## File: `__tests__/fixtures/event_create_branch.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_49ba9b4e-1733-447c-b700-1cea19f95b82
GITHUB_EVENT_NAME=create
GITHUB_EVENT_PATH=./__tests__/fixtures/event_create_branch.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_49ba9b4e-1733-447c-b700-1cea19f95b82
GITHUB_REF=refs/heads/dev
GITHUB_REF_NAME=dev
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=branch
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188731929
GITHUB_RUN_NUMBER=14
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=5f3331d7f7044c18ca9f12c77d961c4d7cf3276a
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_49ba9b4e-1733-447c-b700-1cea19f95b82
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_create_branch.json`
```json
{
  "description": "Test \"Docker\" Actions",
  "master_branch": "master",
  "organization": {
    "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
    "description": "Docker helps developers bring their ideas to life by conquering the complexity of app development.",
    "events_url": "https://api.github.com/orgs/docker/events",
    "hooks_url": "https://api.github.com/orgs/docker/hooks",
    "id": 5429470,
    "issues_url": "https://api.github.com/orgs/docker/issues",
    "login": "docker",
    "members_url": "https://api.github.com/orgs/docker/members{/member}",
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
    "public_members_url": "https://api.github.com/orgs/docker/public_members{/member}",
    "repos_url": "https://api.github.com/orgs/docker/repos",
    "url": "https://api.github.com/orgs/docker"
  },
  "pusher_type": "user",
  "ref": "dev",
  "ref_type": "branch",
  "repository": {
    "allow_forking": true,
    "archive_url": "https://api.github.com/repos/docker/test-docker-action/{archive_format}{/ref}",
    "archived": false,
    "assignees_url": "https://api.github.com/repos/docker/test-docker-action/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/docker/test-docker-action/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/docker/test-docker-action/branches{/branch}",
    "clone_url": "https://github.com/docker/test-docker-action.git",
    "collaborators_url": "https://api.github.com/repos/docker/test-docker-action/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/docker/test-docker-action/comments{/number}",
    "commits_url": "https://api.github.com/repos/docker/test-docker-action/commits{/sha}",
    "compare_url": "https://api.github.com/repos/docker/test-docker-action/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/docker/test-docker-action/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/docker/test-docker-action/contributors",
    "created_at": "2020-08-07T09:23:00Z",
    "default_branch": "master",
    "deployments_url": "https://api.github.com/repos/docker/test-docker-action/deployments",
    "description": "Test \"Docker\" Actions",
    "disabled": false,
    "downloads_url": "https://api.github.com/repos/docker/test-docker-action/downloads",
    "events_url": "https://api.github.com/repos/docker/test-docker-action/events",
    "fork": false,
    "forks": 1,
    "forks_count": 1,
    "forks_url": "https://api.github.com/repos/docker/test-docker-action/forks",
    "full_name": "docker/test-docker-action",
    "git_commits_url": "https://api.github.com/repos/docker/test-docker-action/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/docker/test-docker-action/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/docker/test-docker-action/git/tags{/sha}",
    "git_url": "git://github.com/docker/test-docker-action.git",
    "has_downloads": true,
    "has_issues": true,
    "has_pages": false,
    "has_projects": true,
    "has_wiki": true,
    "homepage": "",
    "hooks_url": "https://api.github.com/repos/docker/test-docker-action/hooks",
    "html_url": "https://github.com/docker/test-docker-action",
    "id": 285789493,
    "is_template": false,
    "issue_comment_url": "https://api.github.com/repos/docker/test-docker-action/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/docker/test-docker-action/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/docker/test-docker-action/issues{/number}",
    "keys_url": "https://api.github.com/repos/docker/test-docker-action/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/docker/test-docker-action/labels{/name}",
    "language": "JavaScript",
    "languages_url": "https://api.github.com/repos/docker/test-docker-action/languages",
    "license": {
      "key": "mit",
      "name": "MIT License",
      "node_id": "MDc6TGljZW5zZTEz",
      "spdx_id": "MIT",
      "url": "https://api.github.com/licenses/mit"
    },
    "merges_url": "https://api.github.com/repos/docker/test-docker-action/merges",
    "milestones_url": "https://api.github.com/repos/docker/test-docker-action/milestones{/number}",
    "mirror_url": null,
    "name": "test-docker-action",
    "node_id": "MDEwOlJlcG9zaXRvcnkyODU3ODk0OTM=",
    "notifications_url": "https://api.github.com/repos/docker/test-docker-action/notifications{?since,all,participating}",
    "open_issues": 6,
    "open_issues_count": 6,
    "owner": {
      "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
      "events_url": "https://api.github.com/users/docker/events{/privacy}",
      "followers_url": "https://api.github.com/users/docker/followers",
      "following_url": "https://api.github.com/users/docker/following{/other_user}",
      "gists_url": "https://api.github.com/users/docker/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/docker",
      "id": 5429470,
      "login": "docker",
      "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
      "organizations_url": "https://api.github.com/users/docker/orgs",
      "received_events_url": "https://api.github.com/users/docker/received_events",
      "repos_url": "https://api.github.com/users/docker/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/docker/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/docker/subscriptions",
      "type": "Organization",
      "url": "https://api.github.com/users/docker"
    },
    "private": true,
    "pulls_url": "https://api.github.com/repos/docker/test-docker-action/pulls{/number}",
    "pushed_at": "2022-04-19T09:24:14Z",
    "releases_url": "https://api.github.com/repos/docker/test-docker-action/releases{/id}",
    "size": 796,
    "ssh_url": "git@github.com:docker/test-docker-action.git",
    "stargazers_count": 0,
    "stargazers_url": "https://api.github.com/repos/docker/test-docker-action/stargazers",
    "statuses_url": "https://api.github.com/repos/docker/test-docker-action/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/docker/test-docker-action/subscribers",
    "subscription_url": "https://api.github.com/repos/docker/test-docker-action/subscription",
    "svn_url": "https://github.com/docker/test-docker-action",
    "tags_url": "https://api.github.com/repos/docker/test-docker-action/tags",
    "teams_url": "https://api.github.com/repos/docker/test-docker-action/teams",
    "topics": [],
    "trees_url": "https://api.github.com/repos/docker/test-docker-action/git/trees{/sha}",
    "updated_at": "2022-04-19T09:05:09Z",
    "url": "https://api.github.com/repos/docker/test-docker-action",
    "visibility": "private",
    "watchers": 0,
    "watchers_count": 0
  },
  "sender": {
    "avatar_url": "https://avatars.githubusercontent.com/u/1951866?v=4",
    "events_url": "https://api.github.com/users/crazy-max/events{/privacy}",
    "followers_url": "https://api.github.com/users/crazy-max/followers",
    "following_url": "https://api.github.com/users/crazy-max/following{/other_user}",
    "gists_url": "https://api.github.com/users/crazy-max/gists{/gist_id}",
    "gravatar_id": "",
    "html_url": "https://github.com/crazy-max",
    "id": 1951866,
    "login": "crazy-max",
    "node_id": "MDQ6VXNlcjE5NTE4NjY=",
    "organizations_url": "https://api.github.com/users/crazy-max/orgs",
    "received_events_url": "https://api.github.com/users/crazy-max/received_events",
    "repos_url": "https://api.github.com/users/crazy-max/repos",
    "site_admin": false,
    "starred_url": "https://api.github.com/users/crazy-max/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/crazy-max/subscriptions",
    "type": "User",
    "url": "https://api.github.com/users/crazy-max"
  }
}
```

## File: `__tests__/fixtures/event_create_tag.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_06751acb-da10-4e54-916a-60749556fc8b
GITHUB_EVENT_NAME=create
GITHUB_EVENT_PATH=./__tests__/fixtures/event_create_tag.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_06751acb-da10-4e54-916a-60749556fc8b
GITHUB_REF=refs/tags/v2.1.8-beta.67
GITHUB_REF_NAME=v2.1.8-beta.67
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=tag
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188815957
GITHUB_RUN_NUMBER=22
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=860c1904a1ce19322e91ac35af1ab07466440c37
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_06751acb-da10-4e54-916a-60749556fc8b
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_create_tag.json`
```json
{
  "description": "Test \"Docker\" Actions",
  "master_branch": "master",
  "organization": {
    "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
    "description": "Docker helps developers bring their ideas to life by conquering the complexity of app development.",
    "events_url": "https://api.github.com/orgs/docker/events",
    "hooks_url": "https://api.github.com/orgs/docker/hooks",
    "id": 5429470,
    "issues_url": "https://api.github.com/orgs/docker/issues",
    "login": "docker",
    "members_url": "https://api.github.com/orgs/docker/members{/member}",
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
    "public_members_url": "https://api.github.com/orgs/docker/public_members{/member}",
    "repos_url": "https://api.github.com/orgs/docker/repos",
    "url": "https://api.github.com/orgs/docker"
  },
  "pusher_type": "user",
  "ref": "v2.1.8-beta.67",
  "ref_type": "tag",
  "repository": {
    "allow_forking": true,
    "archive_url": "https://api.github.com/repos/docker/test-docker-action/{archive_format}{/ref}",
    "archived": false,
    "assignees_url": "https://api.github.com/repos/docker/test-docker-action/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/docker/test-docker-action/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/docker/test-docker-action/branches{/branch}",
    "clone_url": "https://github.com/docker/test-docker-action.git",
    "collaborators_url": "https://api.github.com/repos/docker/test-docker-action/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/docker/test-docker-action/comments{/number}",
    "commits_url": "https://api.github.com/repos/docker/test-docker-action/commits{/sha}",
    "compare_url": "https://api.github.com/repos/docker/test-docker-action/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/docker/test-docker-action/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/docker/test-docker-action/contributors",
    "created_at": "2020-08-07T09:23:00Z",
    "default_branch": "master",
    "deployments_url": "https://api.github.com/repos/docker/test-docker-action/deployments",
    "description": "Test \"Docker\" Actions",
    "disabled": false,
    "downloads_url": "https://api.github.com/repos/docker/test-docker-action/downloads",
    "events_url": "https://api.github.com/repos/docker/test-docker-action/events",
    "fork": false,
    "forks": 1,
    "forks_count": 1,
    "forks_url": "https://api.github.com/repos/docker/test-docker-action/forks",
    "full_name": "docker/test-docker-action",
    "git_commits_url": "https://api.github.com/repos/docker/test-docker-action/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/docker/test-docker-action/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/docker/test-docker-action/git/tags{/sha}",
    "git_url": "git://github.com/docker/test-docker-action.git",
    "has_downloads": true,
    "has_issues": true,
    "has_pages": false,
    "has_projects": true,
    "has_wiki": true,
    "homepage": "",
    "hooks_url": "https://api.github.com/repos/docker/test-docker-action/hooks",
    "html_url": "https://github.com/docker/test-docker-action",
    "id": 285789493,
    "is_template": false,
    "issue_comment_url": "https://api.github.com/repos/docker/test-docker-action/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/docker/test-docker-action/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/docker/test-docker-action/issues{/number}",
    "keys_url": "https://api.github.com/repos/docker/test-docker-action/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/docker/test-docker-action/labels{/name}",
    "language": "JavaScript",
    "languages_url": "https://api.github.com/repos/docker/test-docker-action/languages",
    "license": {
      "key": "mit",
      "name": "MIT License",
      "node_id": "MDc6TGljZW5zZTEz",
      "spdx_id": "MIT",
      "url": "https://api.github.com/licenses/mit"
    },
    "merges_url": "https://api.github.com/repos/docker/test-docker-action/merges",
    "milestones_url": "https://api.github.com/repos/docker/test-docker-action/milestones{/number}",
    "mirror_url": null,
    "name": "test-docker-action",
    "node_id": "MDEwOlJlcG9zaXRvcnkyODU3ODk0OTM=",
    "notifications_url": "https://api.github.com/repos/docker/test-docker-action/notifications{?since,all,participating}",
    "open_issues": 6,
    "open_issues_count": 6,
    "owner": {
      "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
      "events_url": "https://api.github.com/users/docker/events{/privacy}",
      "followers_url": "https://api.github.com/users/docker/followers",
      "following_url": "https://api.github.com/users/docker/following{/other_user}",
      "gists_url": "https://api.github.com/users/docker/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/docker",
      "id": 5429470,
      "login": "docker",
      "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
      "organizations_url": "https://api.github.com/users/docker/orgs",
      "received_events_url": "https://api.github.com/users/docker/received_events",
      "repos_url": "https://api.github.com/users/docker/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/docker/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/docker/subscriptions",
      "type": "Organization",
      "url": "https://api.github.com/users/docker"
    },
    "private": true,
    "pulls_url": "https://api.github.com/repos/docker/test-docker-action/pulls{/number}",
    "pushed_at": "2022-04-19T09:41:03Z",
    "releases_url": "https://api.github.com/repos/docker/test-docker-action/releases{/id}",
    "size": 796,
    "ssh_url": "git@github.com:docker/test-docker-action.git",
    "stargazers_count": 0,
    "stargazers_url": "https://api.github.com/repos/docker/test-docker-action/stargazers",
    "statuses_url": "https://api.github.com/repos/docker/test-docker-action/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/docker/test-docker-action/subscribers",
    "subscription_url": "https://api.github.com/repos/docker/test-docker-action/subscription",
    "svn_url": "https://github.com/docker/test-docker-action",
    "tags_url": "https://api.github.com/repos/docker/test-docker-action/tags",
    "teams_url": "https://api.github.com/repos/docker/test-docker-action/teams",
    "topics": [],
    "trees_url": "https://api.github.com/repos/docker/test-docker-action/git/trees{/sha}",
    "updated_at": "2022-04-19T09:05:09Z",
    "url": "https://api.github.com/repos/docker/test-docker-action",
    "visibility": "private",
    "watchers": 0,
    "watchers_count": 0
  },
  "sender": {
    "avatar_url": "https://avatars.githubusercontent.com/u/1951866?v=4",
    "events_url": "https://api.github.com/users/crazy-max/events{/privacy}",
    "followers_url": "https://api.github.com/users/crazy-max/followers",
    "following_url": "https://api.github.com/users/crazy-max/following{/other_user}",
    "gists_url": "https://api.github.com/users/crazy-max/gists{/gist_id}",
    "gravatar_id": "",
    "html_url": "https://github.com/crazy-max",
    "id": 1951866,
    "login": "crazy-max",
    "node_id": "MDQ6VXNlcjE5NTE4NjY=",
    "organizations_url": "https://api.github.com/users/crazy-max/orgs",
    "received_events_url": "https://api.github.com/users/crazy-max/received_events",
    "repos_url": "https://api.github.com/users/crazy-max/repos",
    "site_admin": false,
    "starred_url": "https://api.github.com/users/crazy-max/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/crazy-max/subscriptions",
    "type": "User",
    "url": "https://api.github.com/users/crazy-max"
  }
}
```

## File: `__tests__/fixtures/event_discussion_created.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_5f8f9da1-1c58-4a8e-bef4-dba436a05edf
GITHUB_EVENT_NAME=discussion
GITHUB_EVENT_PATH=./__tests__/fixtures/event_discussion_created.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_5f8f9da1-1c58-4a8e-bef4-dba436a05edf
GITHUB_REF=refs/heads/master
GITHUB_REF_NAME=master
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=branch
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188642055
GITHUB_RUN_NUMBER=7
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=266574110acf203503badf966df2ea24b5d732d7
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_5f8f9da1-1c58-4a8e-bef4-dba436a05edf
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_discussion_created.json`
```json
{
  "action": "created",
  "discussion": {
    "active_lock_reason": null,
    "answer_chosen_at": null,
    "answer_chosen_by": null,
    "answer_html_url": null,
    "author_association": "COLLABORATOR",
    "body": "bar",
    "category": {
      "created_at": "2022-04-19T11:05:12.000+02:00",
      "description": "Chat about anything and everything here",
      "emoji": ":speech_balloon:",
      "id": 37396924,
      "is_answerable": false,
      "name": "General",
      "node_id": "DIC_kwDOEQjNNc4COqG8",
      "repository_id": 285789493,
      "slug": "general",
      "updated_at": "2022-04-19T11:05:12.000+02:00"
    },
    "comments": 0,
    "created_at": "2022-04-19T09:07:32Z",
    "html_url": "https://github.com/docker/test-docker-action/discussions/13",
    "id": 4019118,
    "locked": false,
    "node_id": "D_kwDOEQjNNc4APVOu",
    "number": 13,
    "reactions": {
      "+1": 0,
      "-1": 0,
      "confused": 0,
      "eyes": 0,
      "heart": 0,
      "hooray": 0,
      "laugh": 0,
      "rocket": 0,
      "total_count": 0,
      "url": "https://api.github.com/repos/docker/test-docker-action/discussions/13/reactions"
    },
    "repository_url": "https://api.github.com/repos/docker/test-docker-action",
    "state": "open",
    "timeline_url": "https://api.github.com/repos/docker/test-docker-action/discussions/13/timeline",
    "title": "foo",
    "updated_at": "2022-04-19T09:07:32Z",
    "user": {
      "avatar_url": "https://avatars.githubusercontent.com/u/1951866?v=4",
      "events_url": "https://api.github.com/users/crazy-max/events{/privacy}",
      "followers_url": "https://api.github.com/users/crazy-max/followers",
      "following_url": "https://api.github.com/users/crazy-max/following{/other_user}",
      "gists_url": "https://api.github.com/users/crazy-max/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/crazy-max",
      "id": 1951866,
      "login": "crazy-max",
      "node_id": "MDQ6VXNlcjE5NTE4NjY=",
      "organizations_url": "https://api.github.com/users/crazy-max/orgs",
      "received_events_url": "https://api.github.com/users/crazy-max/received_events",
      "repos_url": "https://api.github.com/users/crazy-max/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/crazy-max/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/crazy-max/subscriptions",
      "type": "User",
      "url": "https://api.github.com/users/crazy-max"
    }
  },
  "organization": {
    "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
    "description": "Docker helps developers bring their ideas to life by conquering the complexity of app development.",
    "events_url": "https://api.github.com/orgs/docker/events",
    "hooks_url": "https://api.github.com/orgs/docker/hooks",
    "id": 5429470,
    "issues_url": "https://api.github.com/orgs/docker/issues",
    "login": "docker",
    "members_url": "https://api.github.com/orgs/docker/members{/member}",
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
    "public_members_url": "https://api.github.com/orgs/docker/public_members{/member}",
    "repos_url": "https://api.github.com/orgs/docker/repos",
    "url": "https://api.github.com/orgs/docker"
  },
  "repository": {
    "allow_forking": true,
    "archive_url": "https://api.github.com/repos/docker/test-docker-action/{archive_format}{/ref}",
    "archived": false,
    "assignees_url": "https://api.github.com/repos/docker/test-docker-action/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/docker/test-docker-action/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/docker/test-docker-action/branches{/branch}",
    "clone_url": "https://github.com/docker/test-docker-action.git",
    "collaborators_url": "https://api.github.com/repos/docker/test-docker-action/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/docker/test-docker-action/comments{/number}",
    "commits_url": "https://api.github.com/repos/docker/test-docker-action/commits{/sha}",
    "compare_url": "https://api.github.com/repos/docker/test-docker-action/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/docker/test-docker-action/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/docker/test-docker-action/contributors",
    "created_at": "2020-08-07T09:23:00Z",
    "default_branch": "master",
    "deployments_url": "https://api.github.com/repos/docker/test-docker-action/deployments",
    "description": "Test \"Docker\" Actions",
    "disabled": false,
    "downloads_url": "https://api.github.com/repos/docker/test-docker-action/downloads",
    "events_url": "https://api.github.com/repos/docker/test-docker-action/events",
    "fork": false,
    "forks": 1,
    "forks_count": 1,
    "forks_url": "https://api.github.com/repos/docker/test-docker-action/forks",
    "full_name": "docker/test-docker-action",
    "git_commits_url": "https://api.github.com/repos/docker/test-docker-action/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/docker/test-docker-action/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/docker/test-docker-action/git/tags{/sha}",
    "git_url": "git://github.com/docker/test-docker-action.git",
    "has_downloads": true,
    "has_issues": true,
    "has_pages": false,
    "has_projects": true,
    "has_wiki": true,
    "homepage": "",
    "hooks_url": "https://api.github.com/repos/docker/test-docker-action/hooks",
    "html_url": "https://github.com/docker/test-docker-action",
    "id": 285789493,
    "is_template": false,
    "issue_comment_url": "https://api.github.com/repos/docker/test-docker-action/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/docker/test-docker-action/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/docker/test-docker-action/issues{/number}",
    "keys_url": "https://api.github.com/repos/docker/test-docker-action/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/docker/test-docker-action/labels{/name}",
    "language": "JavaScript",
    "languages_url": "https://api.github.com/repos/docker/test-docker-action/languages",
    "license": {
      "key": "mit",
      "name": "MIT License",
      "node_id": "MDc6TGljZW5zZTEz",
      "spdx_id": "MIT",
      "url": "https://api.github.com/licenses/mit"
    },
    "merges_url": "https://api.github.com/repos/docker/test-docker-action/merges",
    "milestones_url": "https://api.github.com/repos/docker/test-docker-action/milestones{/number}",
    "mirror_url": null,
    "name": "test-docker-action",
    "node_id": "MDEwOlJlcG9zaXRvcnkyODU3ODk0OTM=",
    "notifications_url": "https://api.github.com/repos/docker/test-docker-action/notifications{?since,all,participating}",
    "open_issues": 4,
    "open_issues_count": 4,
    "owner": {
      "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
      "events_url": "https://api.github.com/users/docker/events{/privacy}",
      "followers_url": "https://api.github.com/users/docker/followers",
      "following_url": "https://api.github.com/users/docker/following{/other_user}",
      "gists_url": "https://api.github.com/users/docker/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/docker",
      "id": 5429470,
      "login": "docker",
      "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
      "organizations_url": "https://api.github.com/users/docker/orgs",
      "received_events_url": "https://api.github.com/users/docker/received_events",
      "repos_url": "https://api.github.com/users/docker/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/docker/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/docker/subscriptions",
      "type": "Organization",
      "url": "https://api.github.com/users/docker"
    },
    "private": true,
    "pulls_url": "https://api.github.com/repos/docker/test-docker-action/pulls{/number}",
    "pushed_at": "2022-04-19T09:04:50Z",
    "releases_url": "https://api.github.com/repos/docker/test-docker-action/releases{/id}",
    "size": 796,
    "ssh_url": "git@github.com:docker/test-docker-action.git",
    "stargazers_count": 0,
    "stargazers_url": "https://api.github.com/repos/docker/test-docker-action/stargazers",
    "statuses_url": "https://api.github.com/repos/docker/test-docker-action/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/docker/test-docker-action/subscribers",
    "subscription_url": "https://api.github.com/repos/docker/test-docker-action/subscription",
    "svn_url": "https://github.com/docker/test-docker-action",
    "tags_url": "https://api.github.com/repos/docker/test-docker-action/tags",
    "teams_url": "https://api.github.com/repos/docker/test-docker-action/teams",
    "topics": [],
    "trees_url": "https://api.github.com/repos/docker/test-docker-action/git/trees{/sha}",
    "updated_at": "2022-04-19T09:05:09Z",
    "url": "https://api.github.com/repos/docker/test-docker-action",
    "visibility": "private",
    "watchers": 0,
    "watchers_count": 0
  },
  "sender": {
    "avatar_url": "https://avatars.githubusercontent.com/u/1951866?v=4",
    "events_url": "https://api.github.com/users/crazy-max/events{/privacy}",
    "followers_url": "https://api.github.com/users/crazy-max/followers",
    "following_url": "https://api.github.com/users/crazy-max/following{/other_user}",
    "gists_url": "https://api.github.com/users/crazy-max/gists{/gist_id}",
    "gravatar_id": "",
    "html_url": "https://github.com/crazy-max",
    "id": 1951866,
    "login": "crazy-max",
    "node_id": "MDQ6VXNlcjE5NTE4NjY=",
    "organizations_url": "https://api.github.com/users/crazy-max/orgs",
    "received_events_url": "https://api.github.com/users/crazy-max/received_events",
    "repos_url": "https://api.github.com/users/crazy-max/repos",
    "site_admin": false,
    "starred_url": "https://api.github.com/users/crazy-max/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/crazy-max/subscriptions",
    "type": "User",
    "url": "https://api.github.com/users/crazy-max"
  }
}
```

## File: `__tests__/fixtures/event_discussion_pinned.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_940c04a5-537a-4401-afe6-1f044e1d3836
GITHUB_EVENT_NAME=discussion
GITHUB_EVENT_PATH=./__tests__/fixtures/event_discussion_pinned.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_940c04a5-537a-4401-afe6-1f044e1d3836
GITHUB_REF=refs/heads/master
GITHUB_REF_NAME=master
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=branch
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188642074
GITHUB_RUN_NUMBER=8
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=266574110acf203503badf966df2ea24b5d732d7
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_940c04a5-537a-4401-afe6-1f044e1d3836
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_discussion_pinned.json`
```json
{
  "action": "pinned",
  "discussion": {
    "active_lock_reason": null,
    "answer_chosen_at": null,
    "answer_chosen_by": null,
    "answer_html_url": null,
    "author_association": "COLLABORATOR",
    "body": "bar",
    "category": {
      "created_at": "2022-04-19T11:05:12.000+02:00",
      "description": "Chat about anything and everything here",
      "emoji": ":speech_balloon:",
      "id": 37396924,
      "is_answerable": false,
      "name": "General",
      "node_id": "DIC_kwDOEQjNNc4COqG8",
      "repository_id": 285789493,
      "slug": "general",
      "updated_at": "2022-04-19T11:05:12.000+02:00"
    },
    "comments": 0,
    "created_at": "2022-04-19T09:07:32Z",
    "html_url": "https://github.com/docker/test-docker-action/discussions/13",
    "id": 4019118,
    "locked": false,
    "node_id": "D_kwDOEQjNNc4APVOu",
    "number": 13,
    "reactions": {
      "+1": 0,
      "-1": 0,
      "confused": 0,
      "eyes": 0,
      "heart": 0,
      "hooray": 0,
      "laugh": 0,
      "rocket": 0,
      "total_count": 0,
      "url": "https://api.github.com/repos/docker/test-docker-action/discussions/13/reactions"
    },
    "repository_url": "https://api.github.com/repos/docker/test-docker-action",
    "state": "open",
    "timeline_url": "https://api.github.com/repos/docker/test-docker-action/discussions/13/timeline",
    "title": "foo",
    "updated_at": "2022-04-19T09:07:32Z",
    "user": {
      "avatar_url": "https://avatars.githubusercontent.com/u/1951866?v=4",
      "events_url": "https://api.github.com/users/crazy-max/events{/privacy}",
      "followers_url": "https://api.github.com/users/crazy-max/followers",
      "following_url": "https://api.github.com/users/crazy-max/following{/other_user}",
      "gists_url": "https://api.github.com/users/crazy-max/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/crazy-max",
      "id": 1951866,
      "login": "crazy-max",
      "node_id": "MDQ6VXNlcjE5NTE4NjY=",
      "organizations_url": "https://api.github.com/users/crazy-max/orgs",
      "received_events_url": "https://api.github.com/users/crazy-max/received_events",
      "repos_url": "https://api.github.com/users/crazy-max/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/crazy-max/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/crazy-max/subscriptions",
      "type": "User",
      "url": "https://api.github.com/users/crazy-max"
    }
  },
  "organization": {
    "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
    "description": "Docker helps developers bring their ideas to life by conquering the complexity of app development.",
    "events_url": "https://api.github.com/orgs/docker/events",
    "hooks_url": "https://api.github.com/orgs/docker/hooks",
    "id": 5429470,
    "issues_url": "https://api.github.com/orgs/docker/issues",
    "login": "docker",
    "members_url": "https://api.github.com/orgs/docker/members{/member}",
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
    "public_members_url": "https://api.github.com/orgs/docker/public_members{/member}",
    "repos_url": "https://api.github.com/orgs/docker/repos",
    "url": "https://api.github.com/orgs/docker"
  },
  "repository": {
    "allow_forking": true,
    "archive_url": "https://api.github.com/repos/docker/test-docker-action/{archive_format}{/ref}",
    "archived": false,
    "assignees_url": "https://api.github.com/repos/docker/test-docker-action/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/docker/test-docker-action/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/docker/test-docker-action/branches{/branch}",
    "clone_url": "https://github.com/docker/test-docker-action.git",
    "collaborators_url": "https://api.github.com/repos/docker/test-docker-action/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/docker/test-docker-action/comments{/number}",
    "commits_url": "https://api.github.com/repos/docker/test-docker-action/commits{/sha}",
    "compare_url": "https://api.github.com/repos/docker/test-docker-action/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/docker/test-docker-action/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/docker/test-docker-action/contributors",
    "created_at": "2020-08-07T09:23:00Z",
    "default_branch": "master",
    "deployments_url": "https://api.github.com/repos/docker/test-docker-action/deployments",
    "description": "Test \"Docker\" Actions",
    "disabled": false,
    "downloads_url": "https://api.github.com/repos/docker/test-docker-action/downloads",
    "events_url": "https://api.github.com/repos/docker/test-docker-action/events",
    "fork": false,
    "forks": 1,
    "forks_count": 1,
    "forks_url": "https://api.github.com/repos/docker/test-docker-action/forks",
    "full_name": "docker/test-docker-action",
    "git_commits_url": "https://api.github.com/repos/docker/test-docker-action/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/docker/test-docker-action/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/docker/test-docker-action/git/tags{/sha}",
    "git_url": "git://github.com/docker/test-docker-action.git",
    "has_downloads": true,
    "has_issues": true,
    "has_pages": false,
    "has_projects": true,
    "has_wiki": true,
    "homepage": "",
    "hooks_url": "https://api.github.com/repos/docker/test-docker-action/hooks",
    "html_url": "https://github.com/docker/test-docker-action",
    "id": 285789493,
    "is_template": false,
    "issue_comment_url": "https://api.github.com/repos/docker/test-docker-action/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/docker/test-docker-action/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/docker/test-docker-action/issues{/number}",
    "keys_url": "https://api.github.com/repos/docker/test-docker-action/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/docker/test-docker-action/labels{/name}",
    "language": "JavaScript",
    "languages_url": "https://api.github.com/repos/docker/test-docker-action/languages",
    "license": {
      "key": "mit",
      "name": "MIT License",
      "node_id": "MDc6TGljZW5zZTEz",
      "spdx_id": "MIT",
      "url": "https://api.github.com/licenses/mit"
    },
    "merges_url": "https://api.github.com/repos/docker/test-docker-action/merges",
    "milestones_url": "https://api.github.com/repos/docker/test-docker-action/milestones{/number}",
    "mirror_url": null,
    "name": "test-docker-action",
    "node_id": "MDEwOlJlcG9zaXRvcnkyODU3ODk0OTM=",
    "notifications_url": "https://api.github.com/repos/docker/test-docker-action/notifications{?since,all,participating}",
    "open_issues": 4,
    "open_issues_count": 4,
    "owner": {
      "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
      "events_url": "https://api.github.com/users/docker/events{/privacy}",
      "followers_url": "https://api.github.com/users/docker/followers",
      "following_url": "https://api.github.com/users/docker/following{/other_user}",
      "gists_url": "https://api.github.com/users/docker/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/docker",
      "id": 5429470,
      "login": "docker",
      "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
      "organizations_url": "https://api.github.com/users/docker/orgs",
      "received_events_url": "https://api.github.com/users/docker/received_events",
      "repos_url": "https://api.github.com/users/docker/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/docker/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/docker/subscriptions",
      "type": "Organization",
      "url": "https://api.github.com/users/docker"
    },
    "private": true,
    "pulls_url": "https://api.github.com/repos/docker/test-docker-action/pulls{/number}",
    "pushed_at": "2022-04-19T09:04:50Z",
    "releases_url": "https://api.github.com/repos/docker/test-docker-action/releases{/id}",
    "size": 796,
    "ssh_url": "git@github.com:docker/test-docker-action.git",
    "stargazers_count": 0,
    "stargazers_url": "https://api.github.com/repos/docker/test-docker-action/stargazers",
    "statuses_url": "https://api.github.com/repos/docker/test-docker-action/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/docker/test-docker-action/subscribers",
    "subscription_url": "https://api.github.com/repos/docker/test-docker-action/subscription",
    "svn_url": "https://github.com/docker/test-docker-action",
    "tags_url": "https://api.github.com/repos/docker/test-docker-action/tags",
    "teams_url": "https://api.github.com/repos/docker/test-docker-action/teams",
    "topics": [],
    "trees_url": "https://api.github.com/repos/docker/test-docker-action/git/trees{/sha}",
    "updated_at": "2022-04-19T09:05:09Z",
    "url": "https://api.github.com/repos/docker/test-docker-action",
    "visibility": "private",
    "watchers": 0,
    "watchers_count": 0
  },
  "sender": {
    "avatar_url": "https://avatars.githubusercontent.com/u/1951866?v=4",
    "events_url": "https://api.github.com/users/crazy-max/events{/privacy}",
    "followers_url": "https://api.github.com/users/crazy-max/followers",
    "following_url": "https://api.github.com/users/crazy-max/following{/other_user}",
    "gists_url": "https://api.github.com/users/crazy-max/gists{/gist_id}",
    "gravatar_id": "",
    "html_url": "https://github.com/crazy-max",
    "id": 1951866,
    "login": "crazy-max",
    "node_id": "MDQ6VXNlcjE5NTE4NjY=",
    "organizations_url": "https://api.github.com/users/crazy-max/orgs",
    "received_events_url": "https://api.github.com/users/crazy-max/received_events",
    "repos_url": "https://api.github.com/users/crazy-max/repos",
    "site_admin": false,
    "starred_url": "https://api.github.com/users/crazy-max/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/crazy-max/subscriptions",
    "type": "User",
    "url": "https://api.github.com/users/crazy-max"
  }
}
```

## File: `__tests__/fixtures/event_empty.env`
```
GITHUB_ACTION=
GITHUB_ACTIONS=
GITHUB_ACTION_PATH=
GITHUB_ACTOR=
GITHUB_API_URL=
GITHUB_BASE_REF=
GITHUB_ENV=
GITHUB_EVENT_NAME=
GITHUB_EVENT_PATH=
GITHUB_GRAPHQL_URL=
GITHUB_HEAD_REF=
GITHUB_JOB=
GITHUB_PATH=
GITHUB_REF=
GITHUB_REPOSITORY=
GITHUB_REPOSITORY_OWNER=
GITHUB_RETENTION_DAYS=
GITHUB_RUN_ID=
GITHUB_RUN_NUMBER=
GITHUB_SERVER_URL=
GITHUB_SHA=
GITHUB_WORKFLOW=
GITHUB_WORKSPACE=
```

## File: `__tests__/fixtures/event_issue_opened.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_b598b668-2cad-465a-b526-d21912b7d2b2
GITHUB_EVENT_NAME=issues
GITHUB_EVENT_PATH=./__tests__/fixtures/event_issue_opened.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_b598b668-2cad-465a-b526-d21912b7d2b2
GITHUB_REF=refs/heads/master
GITHUB_REF_NAME=master
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=branch
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188657159
GITHUB_RUN_NUMBER=9
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=266574110acf203503badf966df2ea24b5d732d7
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_b598b668-2cad-465a-b526-d21912b7d2b2
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_issue_opened.json`
```json
{
  "action": "opened",
  "issue": {
    "active_lock_reason": null,
    "assignee": null,
    "assignees": [],
    "author_association": "COLLABORATOR",
    "body": "bar",
    "closed_at": null,
    "comments": 0,
    "comments_url": "https://api.github.com/repos/docker/test-docker-action/issues/14/comments",
    "created_at": "2022-04-19T09:10:26Z",
    "events_url": "https://api.github.com/repos/docker/test-docker-action/issues/14/events",
    "html_url": "https://github.com/docker/test-docker-action/issues/14",
    "id": 1208034626,
    "labels": [],
    "labels_url": "https://api.github.com/repos/docker/test-docker-action/issues/14/labels{/name}",
    "locked": false,
    "milestone": null,
    "node_id": "I_kwDOEQjNNc5IASVC",
    "number": 14,
    "performed_via_github_app": null,
    "reactions": {
      "+1": 0,
      "-1": 0,
      "confused": 0,
      "eyes": 0,
      "heart": 0,
      "hooray": 0,
      "laugh": 0,
      "rocket": 0,
      "total_count": 0,
      "url": "https://api.github.com/repos/docker/test-docker-action/issues/14/reactions"
    },
    "repository_url": "https://api.github.com/repos/docker/test-docker-action",
    "state": "open",
    "timeline_url": "https://api.github.com/repos/docker/test-docker-action/issues/14/timeline",
    "title": "foo",
    "updated_at": "2022-04-19T09:10:26Z",
    "url": "https://api.github.com/repos/docker/test-docker-action/issues/14",
    "user": {
      "avatar_url": "https://avatars.githubusercontent.com/u/1951866?v=4",
      "events_url": "https://api.github.com/users/crazy-max/events{/privacy}",
      "followers_url": "https://api.github.com/users/crazy-max/followers",
      "following_url": "https://api.github.com/users/crazy-max/following{/other_user}",
      "gists_url": "https://api.github.com/users/crazy-max/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/crazy-max",
      "id": 1951866,
      "login": "crazy-max",
      "node_id": "MDQ6VXNlcjE5NTE4NjY=",
      "organizations_url": "https://api.github.com/users/crazy-max/orgs",
      "received_events_url": "https://api.github.com/users/crazy-max/received_events",
      "repos_url": "https://api.github.com/users/crazy-max/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/crazy-max/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/crazy-max/subscriptions",
      "type": "User",
      "url": "https://api.github.com/users/crazy-max"
    }
  },
  "organization": {
    "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
    "description": "Docker helps developers bring their ideas to life by conquering the complexity of app development.",
    "events_url": "https://api.github.com/orgs/docker/events",
    "hooks_url": "https://api.github.com/orgs/docker/hooks",
    "id": 5429470,
    "issues_url": "https://api.github.com/orgs/docker/issues",
    "login": "docker",
    "members_url": "https://api.github.com/orgs/docker/members{/member}",
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
    "public_members_url": "https://api.github.com/orgs/docker/public_members{/member}",
    "repos_url": "https://api.github.com/orgs/docker/repos",
    "url": "https://api.github.com/orgs/docker"
  },
  "repository": {
    "allow_forking": true,
    "archive_url": "https://api.github.com/repos/docker/test-docker-action/{archive_format}{/ref}",
    "archived": false,
    "assignees_url": "https://api.github.com/repos/docker/test-docker-action/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/docker/test-docker-action/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/docker/test-docker-action/branches{/branch}",
    "clone_url": "https://github.com/docker/test-docker-action.git",
    "collaborators_url": "https://api.github.com/repos/docker/test-docker-action/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/docker/test-docker-action/comments{/number}",
    "commits_url": "https://api.github.com/repos/docker/test-docker-action/commits{/sha}",
    "compare_url": "https://api.github.com/repos/docker/test-docker-action/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/docker/test-docker-action/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/docker/test-docker-action/contributors",
    "created_at": "2020-08-07T09:23:00Z",
    "default_branch": "master",
    "deployments_url": "https://api.github.com/repos/docker/test-docker-action/deployments",
    "description": "Test \"Docker\" Actions",
    "disabled": false,
    "downloads_url": "https://api.github.com/repos/docker/test-docker-action/downloads",
    "events_url": "https://api.github.com/repos/docker/test-docker-action/events",
    "fork": false,
    "forks": 1,
    "forks_count": 1,
    "forks_url": "https://api.github.com/repos/docker/test-docker-action/forks",
    "full_name": "docker/test-docker-action",
    "git_commits_url": "https://api.github.com/repos/docker/test-docker-action/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/docker/test-docker-action/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/docker/test-docker-action/git/tags{/sha}",
    "git_url": "git://github.com/docker/test-docker-action.git",
    "has_downloads": true,
    "has_issues": true,
    "has_pages": false,
    "has_projects": true,
    "has_wiki": true,
    "homepage": "",
    "hooks_url": "https://api.github.com/repos/docker/test-docker-action/hooks",
    "html_url": "https://github.com/docker/test-docker-action",
    "id": 285789493,
    "is_template": false,
    "issue_comment_url": "https://api.github.com/repos/docker/test-docker-action/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/docker/test-docker-action/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/docker/test-docker-action/issues{/number}",
    "keys_url": "https://api.github.com/repos/docker/test-docker-action/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/docker/test-docker-action/labels{/name}",
    "language": "JavaScript",
    "languages_url": "https://api.github.com/repos/docker/test-docker-action/languages",
    "license": {
      "key": "mit",
      "name": "MIT License",
      "node_id": "MDc6TGljZW5zZTEz",
      "spdx_id": "MIT",
      "url": "https://api.github.com/licenses/mit"
    },
    "merges_url": "https://api.github.com/repos/docker/test-docker-action/merges",
    "milestones_url": "https://api.github.com/repos/docker/test-docker-action/milestones{/number}",
    "mirror_url": null,
    "name": "test-docker-action",
    "node_id": "MDEwOlJlcG9zaXRvcnkyODU3ODk0OTM=",
    "notifications_url": "https://api.github.com/repos/docker/test-docker-action/notifications{?since,all,participating}",
    "open_issues": 5,
    "open_issues_count": 5,
    "owner": {
      "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
      "events_url": "https://api.github.com/users/docker/events{/privacy}",
      "followers_url": "https://api.github.com/users/docker/followers",
      "following_url": "https://api.github.com/users/docker/following{/other_user}",
      "gists_url": "https://api.github.com/users/docker/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/docker",
      "id": 5429470,
      "login": "docker",
      "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
      "organizations_url": "https://api.github.com/users/docker/orgs",
      "received_events_url": "https://api.github.com/users/docker/received_events",
      "repos_url": "https://api.github.com/users/docker/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/docker/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/docker/subscriptions",
      "type": "Organization",
      "url": "https://api.github.com/users/docker"
    },
    "private": true,
    "pulls_url": "https://api.github.com/repos/docker/test-docker-action/pulls{/number}",
    "pushed_at": "2022-04-19T09:04:50Z",
    "releases_url": "https://api.github.com/repos/docker/test-docker-action/releases{/id}",
    "size": 796,
    "ssh_url": "git@github.com:docker/test-docker-action.git",
    "stargazers_count": 0,
    "stargazers_url": "https://api.github.com/repos/docker/test-docker-action/stargazers",
    "statuses_url": "https://api.github.com/repos/docker/test-docker-action/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/docker/test-docker-action/subscribers",
    "subscription_url": "https://api.github.com/repos/docker/test-docker-action/subscription",
    "svn_url": "https://github.com/docker/test-docker-action",
    "tags_url": "https://api.github.com/repos/docker/test-docker-action/tags",
    "teams_url": "https://api.github.com/repos/docker/test-docker-action/teams",
    "topics": [],
    "trees_url": "https://api.github.com/repos/docker/test-docker-action/git/trees{/sha}",
    "updated_at": "2022-04-19T09:05:09Z",
    "url": "https://api.github.com/repos/docker/test-docker-action",
    "visibility": "private",
    "watchers": 0,
    "watchers_count": 0
  },
  "sender": {
    "avatar_url": "https://avatars.githubusercontent.com/u/1951866?v=4",
    "events_url": "https://api.github.com/users/crazy-max/events{/privacy}",
    "followers_url": "https://api.github.com/users/crazy-max/followers",
    "following_url": "https://api.github.com/users/crazy-max/following{/other_user}",
    "gists_url": "https://api.github.com/users/crazy-max/gists{/gist_id}",
    "gravatar_id": "",
    "html_url": "https://github.com/crazy-max",
    "id": 1951866,
    "login": "crazy-max",
    "node_id": "MDQ6VXNlcjE5NTE4NjY=",
    "organizations_url": "https://api.github.com/users/crazy-max/orgs",
    "received_events_url": "https://api.github.com/users/crazy-max/received_events",
    "repos_url": "https://api.github.com/users/crazy-max/repos",
    "site_admin": false,
    "starred_url": "https://api.github.com/users/crazy-max/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/crazy-max/subscriptions",
    "type": "User",
    "url": "https://api.github.com/users/crazy-max"
  }
}
```

## File: `__tests__/fixtures/event_pull_request.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=master
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_ca953e95-2f41-4926-bc52-a1c8d90e94c1
GITHUB_EVENT_NAME=pull_request
GITHUB_EVENT_PATH=./__tests__/fixtures/event_pull_request.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=test-pr
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_ca953e95-2f41-4926-bc52-a1c8d90e94c1
GITHUB_REF=refs/pull/15/merge
GITHUB_REF_NAME=15/merge
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=branch
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188688025
GITHUB_RUN_NUMBER=11
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=a9c8c5828b91be19d9728548b24759e352367ef1
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_ca953e95-2f41-4926-bc52-a1c8d90e94c1
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_pull_request.json`
```json
{
  "action": "opened",
  "number": 15,
  "organization": {
    "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
    "description": "Docker helps developers bring their ideas to life by conquering the complexity of app development.",
    "events_url": "https://api.github.com/orgs/docker/events",
    "hooks_url": "https://api.github.com/orgs/docker/hooks",
    "id": 5429470,
    "issues_url": "https://api.github.com/orgs/docker/issues",
    "login": "docker",
    "members_url": "https://api.github.com/orgs/docker/members{/member}",
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
    "public_members_url": "https://api.github.com/orgs/docker/public_members{/member}",
    "repos_url": "https://api.github.com/orgs/docker/repos",
    "url": "https://api.github.com/orgs/docker"
  },
  "pull_request": {
    "_links": {
      "comments": {
        "href": "https://api.github.com/repos/docker/test-docker-action/issues/15/comments"
      },
      "commits": {
        "href": "https://api.github.com/repos/docker/test-docker-action/pulls/15/commits"
      },
      "html": {
        "href": "https://github.com/docker/test-docker-action/pull/15"
      },
      "issue": {
        "href": "https://api.github.com/repos/docker/test-docker-action/issues/15"
      },
      "review_comment": {
        "href": "https://api.github.com/repos/docker/test-docker-action/pulls/comments{/number}"
      },
      "review_comments": {
        "href": "https://api.github.com/repos/docker/test-docker-action/pulls/15/comments"
      },
      "self": {
        "href": "https://api.github.com/repos/docker/test-docker-action/pulls/15"
      },
      "statuses": {
        "href": "https://api.github.com/repos/docker/test-docker-action/statuses/3370e228f2209994d57af4427fe64e71bb79ac96"
      }
    },
    "active_lock_reason": null,
    "additions": 1,
    "assignee": null,
    "assignees": [],
    "author_association": "COLLABORATOR",
    "auto_merge": null,
    "base": {
      "label": "docker:master",
      "ref": "master",
      "repo": {
        "allow_auto_merge": false,
        "allow_forking": true,
        "allow_merge_commit": true,
        "allow_rebase_merge": true,
        "allow_squash_merge": true,
        "allow_update_branch": false,
        "archive_url": "https://api.github.com/repos/docker/test-docker-action/{archive_format}{/ref}",
        "archived": false,
        "assignees_url": "https://api.github.com/repos/docker/test-docker-action/assignees{/user}",
        "blobs_url": "https://api.github.com/repos/docker/test-docker-action/git/blobs{/sha}",
        "branches_url": "https://api.github.com/repos/docker/test-docker-action/branches{/branch}",
        "clone_url": "https://github.com/docker/test-docker-action.git",
        "collaborators_url": "https://api.github.com/repos/docker/test-docker-action/collaborators{/collaborator}",
        "comments_url": "https://api.github.com/repos/docker/test-docker-action/comments{/number}",
        "commits_url": "https://api.github.com/repos/docker/test-docker-action/commits{/sha}",
        "compare_url": "https://api.github.com/repos/docker/test-docker-action/compare/{base}...{head}",
        "contents_url": "https://api.github.com/repos/docker/test-docker-action/contents/{+path}",
        "contributors_url": "https://api.github.com/repos/docker/test-docker-action/contributors",
        "created_at": "2020-08-07T09:23:00Z",
        "default_branch": "master",
        "delete_branch_on_merge": false,
        "deployments_url": "https://api.github.com/repos/docker/test-docker-action/deployments",
        "description": "Test \"Docker\" Actions",
        "disabled": false,
        "downloads_url": "https://api.github.com/repos/docker/test-docker-action/downloads",
        "events_url": "https://api.github.com/repos/docker/test-docker-action/events",
        "fork": false,
        "forks": 1,
        "forks_count": 1,
        "forks_url": "https://api.github.com/repos/docker/test-docker-action/forks",
        "full_name": "docker/test-docker-action",
        "git_commits_url": "https://api.github.com/repos/docker/test-docker-action/git/commits{/sha}",
        "git_refs_url": "https://api.github.com/repos/docker/test-docker-action/git/refs{/sha}",
        "git_tags_url": "https://api.github.com/repos/docker/test-docker-action/git/tags{/sha}",
        "git_url": "git://github.com/docker/test-docker-action.git",
        "has_downloads": true,
        "has_issues": true,
        "has_pages": false,
        "has_projects": true,
        "has_wiki": true,
        "homepage": "",
        "hooks_url": "https://api.github.com/repos/docker/test-docker-action/hooks",
        "html_url": "https://github.com/docker/test-docker-action",
        "id": 285789493,
        "is_template": false,
        "issue_comment_url": "https://api.github.com/repos/docker/test-docker-action/issues/comments{/number}",
        "issue_events_url": "https://api.github.com/repos/docker/test-docker-action/issues/events{/number}",
        "issues_url": "https://api.github.com/repos/docker/test-docker-action/issues{/number}",
        "keys_url": "https://api.github.com/repos/docker/test-docker-action/keys{/key_id}",
        "labels_url": "https://api.github.com/repos/docker/test-docker-action/labels{/name}",
        "language": "JavaScript",
        "languages_url": "https://api.github.com/repos/docker/test-docker-action/languages",
        "license": {
          "key": "mit",
          "name": "MIT License",
          "node_id": "MDc6TGljZW5zZTEz",
          "spdx_id": "MIT",
          "url": "https://api.github.com/licenses/mit"
        },
        "merges_url": "https://api.github.com/repos/docker/test-docker-action/merges",
        "milestones_url": "https://api.github.com/repos/docker/test-docker-action/milestones{/number}",
        "mirror_url": null,
        "name": "test-docker-action",
        "node_id": "MDEwOlJlcG9zaXRvcnkyODU3ODk0OTM=",
        "notifications_url": "https://api.github.com/repos/docker/test-docker-action/notifications{?since,all,participating}",
        "open_issues": 6,
        "open_issues_count": 6,
        "owner": {
          "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
          "events_url": "https://api.github.com/users/docker/events{/privacy}",
          "followers_url": "https://api.github.com/users/docker/followers",
          "following_url": "https://api.github.com/users/docker/following{/other_user}",
          "gists_url": "https://api.github.com/users/docker/gists{/gist_id}",
          "gravatar_id": "",
          "html_url": "https://github.com/docker",
          "id": 5429470,
          "login": "docker",
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
          "organizations_url": "https://api.github.com/users/docker/orgs",
          "received_events_url": "https://api.github.com/users/docker/received_events",
          "repos_url": "https://api.github.com/users/docker/repos",
          "site_admin": false,
          "starred_url": "https://api.github.com/users/docker/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/docker/subscriptions",
          "type": "Organization",
          "url": "https://api.github.com/users/docker"
        },
        "private": true,
        "pulls_url": "https://api.github.com/repos/docker/test-docker-action/pulls{/number}",
        "pushed_at": "2022-04-19T09:04:50Z",
        "releases_url": "https://api.github.com/repos/docker/test-docker-action/releases{/id}",
        "size": 796,
        "ssh_url": "git@github.com:docker/test-docker-action.git",
        "stargazers_count": 0,
        "stargazers_url": "https://api.github.com/repos/docker/test-docker-action/stargazers",
        "statuses_url": "https://api.github.com/repos/docker/test-docker-action/statuses/{sha}",
        "subscribers_url": "https://api.github.com/repos/docker/test-docker-action/subscribers",
        "subscription_url": "https://api.github.com/repos/docker/test-docker-action/subscription",
        "svn_url": "https://github.com/docker/test-docker-action",
        "tags_url": "https://api.github.com/repos/docker/test-docker-action/tags",
        "teams_url": "https://api.github.com/repos/docker/test-docker-action/teams",
        "topics": [],
        "trees_url": "https://api.github.com/repos/docker/test-docker-action/git/trees{/sha}",
        "updated_at": "2022-04-19T09:05:09Z",
        "url": "https://api.github.com/repos/docker/test-docker-action",
        "visibility": "private",
        "watchers": 0,
        "watchers_count": 0
      },
      "sha": "266574110acf203503badf966df2ea24b5d732d7",
      "user": {
        "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
        "events_url": "https://api.github.com/users/docker/events{/privacy}",
        "followers_url": "https://api.github.com/users/docker/followers",
        "following_url": "https://api.github.com/users/docker/following{/other_user}",
        "gists_url": "https://api.github.com/users/docker/gists{/gist_id}",
        "gravatar_id": "",
        "html_url": "https://github.com/docker",
        "id": 5429470,
        "login": "docker",
        "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
        "organizations_url": "https://api.github.com/users/docker/orgs",
        "received_events_url": "https://api.github.com/users/docker/received_events",
        "repos_url": "https://api.github.com/users/docker/repos",
        "site_admin": false,
        "starred_url": "https://api.github.com/users/docker/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/docker/subscriptions",
        "type": "Organization",
        "url": "https://api.github.com/users/docker"
      }
    },
    "body": null,
    "changed_files": 1,
    "closed_at": null,
    "comments": 0,
    "comments_url": "https://api.github.com/repos/docker/test-docker-action/issues/15/comments",
    "commits": 1,
    "commits_url": "https://api.github.com/repos/docker/test-docker-action/pulls/15/commits",
    "created_at": "2022-04-19T09:16:17Z",
    "deletions": 1,
    "diff_url": "https://github.com/docker/test-docker-action/pull/15.diff",
    "draft": false,
    "head": {
      "label": "crazy-max:test-pr",
      "ref": "test-pr",
      "repo": {
        "allow_auto_merge": false,
        "allow_forking": true,
        "allow_merge_commit": true,
        "allow_rebase_merge": true,
        "allow_squash_merge": true,
        "allow_update_branch": false,
        "archive_url": "https://api.github.com/repos/crazy-max/test-docker-action/{archive_format}{/ref}",
        "archived": false,
        "assignees_url": "https://api.github.com/repos/crazy-max/test-docker-action/assignees{/user}",
        "blobs_url": "https://api.github.com/repos/crazy-max/test-docker-action/git/blobs{/sha}",
        "branches_url": "https://api.github.com/repos/crazy-max/test-docker-action/branches{/branch}",
        "clone_url": "https://github.com/crazy-max/test-docker-action.git",
        "collaborators_url": "https://api.github.com/repos/crazy-max/test-docker-action/collaborators{/collaborator}",
        "comments_url": "https://api.github.com/repos/crazy-max/test-docker-action/comments{/number}",
        "commits_url": "https://api.github.com/repos/crazy-max/test-docker-action/commits{/sha}",
        "compare_url": "https://api.github.com/repos/crazy-max/test-docker-action/compare/{base}...{head}",
        "contents_url": "https://api.github.com/repos/crazy-max/test-docker-action/contents/{+path}",
        "contributors_url": "https://api.github.com/repos/crazy-max/test-docker-action/contributors",
        "created_at": "2021-07-11T17:34:22Z",
        "default_branch": "master",
        "delete_branch_on_merge": false,
        "deployments_url": "https://api.github.com/repos/crazy-max/test-docker-action/deployments",
        "description": "Test \"Docker\" Actions",
        "disabled": false,
        "downloads_url": "https://api.github.com/repos/crazy-max/test-docker-action/downloads",
        "events_url": "https://api.github.com/repos/crazy-max/test-docker-action/events",
        "fork": true,
        "forks": 0,
        "forks_count": 0,
        "forks_url": "https://api.github.com/repos/crazy-max/test-docker-action/forks",
        "full_name": "crazy-max/test-docker-action",
        "git_commits_url": "https://api.github.com/repos/crazy-max/test-docker-action/git/commits{/sha}",
        "git_refs_url": "https://api.github.com/repos/crazy-max/test-docker-action/git/refs{/sha}",
        "git_tags_url": "https://api.github.com/repos/crazy-max/test-docker-action/git/tags{/sha}",
        "git_url": "git://github.com/crazy-max/test-docker-action.git",
        "has_downloads": true,
        "has_issues": false,
        "has_pages": false,
        "has_projects": true,
        "has_wiki": false,
        "homepage": "",
        "hooks_url": "https://api.github.com/repos/crazy-max/test-docker-action/hooks",
        "html_url": "https://github.com/crazy-max/test-docker-action",
        "id": 385013169,
        "is_template": false,
        "issue_comment_url": "https://api.github.com/repos/crazy-max/test-docker-action/issues/comments{/number}",
        "issue_events_url": "https://api.github.com/repos/crazy-max/test-docker-action/issues/events{/number}",
        "issues_url": "https://api.github.com/repos/crazy-max/test-docker-action/issues{/number}",
        "keys_url": "https://api.github.com/repos/crazy-max/test-docker-action/keys{/key_id}",
        "labels_url": "https://api.github.com/repos/crazy-max/test-docker-action/labels{/name}",
        "language": "JavaScript",
        "languages_url": "https://api.github.com/repos/crazy-max/test-docker-action/languages",
        "license": {
          "key": "mit",
          "name": "MIT License",
          "node_id": "MDc6TGljZW5zZTEz",
          "spdx_id": "MIT",
          "url": "https://api.github.com/licenses/mit"
        },
        "merges_url": "https://api.github.com/repos/crazy-max/test-docker-action/merges",
        "milestones_url": "https://api.github.com/repos/crazy-max/test-docker-action/milestones{/number}",
        "mirror_url": null,
        "name": "test-docker-action",
        "node_id": "MDEwOlJlcG9zaXRvcnkzODUwMTMxNjk=",
        "notifications_url": "https://api.github.com/repos/crazy-max/test-docker-action/notifications{?since,all,participating}",
        "open_issues": 0,
        "open_issues_count": 0,
        "owner": {
          "avatar_url": "https://avatars.githubusercontent.com/u/1951866?v=4",
          "events_url": "https://api.github.com/users/crazy-max/events{/privacy}",
          "followers_url": "https://api.github.com/users/crazy-max/followers",
          "following_url": "https://api.github.com/users/crazy-max/following{/other_user}",
          "gists_url": "https://api.github.com/users/crazy-max/gists{/gist_id}",
          "gravatar_id": "",
          "html_url": "https://github.com/crazy-max",
          "id": 1951866,
          "login": "crazy-max",
          "node_id": "MDQ6VXNlcjE5NTE4NjY=",
          "organizations_url": "https://api.github.com/users/crazy-max/orgs",
          "received_events_url": "https://api.github.com/users/crazy-max/received_events",
          "repos_url": "https://api.github.com/users/crazy-max/repos",
          "site_admin": false,
          "starred_url": "https://api.github.com/users/crazy-max/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/crazy-max/subscriptions",
          "type": "User",
          "url": "https://api.github.com/users/crazy-max"
        },
        "private": true,
        "pulls_url": "https://api.github.com/repos/crazy-max/test-docker-action/pulls{/number}",
        "pushed_at": "2022-04-19T09:16:07Z",
        "releases_url": "https://api.github.com/repos/crazy-max/test-docker-action/releases{/id}",
        "size": 151,
        "ssh_url": "git@github.com:crazy-max/test-docker-action.git",
        "stargazers_count": 0,
        "stargazers_url": "https://api.github.com/repos/crazy-max/test-docker-action/stargazers",
        "statuses_url": "https://api.github.com/repos/crazy-max/test-docker-action/statuses/{sha}",
        "subscribers_url": "https://api.github.com/repos/crazy-max/test-docker-action/subscribers",
        "subscription_url": "https://api.github.com/repos/crazy-max/test-docker-action/subscription",
        "svn_url": "https://github.com/crazy-max/test-docker-action",
        "tags_url": "https://api.github.com/repos/crazy-max/test-docker-action/tags",
        "teams_url": "https://api.github.com/repos/crazy-max/test-docker-action/teams",
        "topics": [],
        "trees_url": "https://api.github.com/repos/crazy-max/test-docker-action/git/trees{/sha}",
        "updated_at": "2022-04-19T09:13:10Z",
        "url": "https://api.github.com/repos/crazy-max/test-docker-action",
        "visibility": "private",
        "watchers": 0,
        "watchers_count": 0
      },
      "sha": "3370e228f2209994d57af4427fe64e71bb79ac96",
      "user": {
        "avatar_url": "https://avatars.githubusercontent.com/u/1951866?v=4",
        "events_url": "https://api.github.com/users/crazy-max/events{/privacy}",
        "followers_url": "https://api.github.com/users/crazy-max/followers",
        "following_url": "https://api.github.com/users/crazy-max/following{/other_user}",
        "gists_url": "https://api.github.com/users/crazy-max/gists{/gist_id}",
        "gravatar_id": "",
        "html_url": "https://github.com/crazy-max",
        "id": 1951866,
        "login": "crazy-max",
        "node_id": "MDQ6VXNlcjE5NTE4NjY=",
        "organizations_url": "https://api.github.com/users/crazy-max/orgs",
        "received_events_url": "https://api.github.com/users/crazy-max/received_events",
        "repos_url": "https://api.github.com/users/crazy-max/repos",
        "site_admin": false,
        "starred_url": "https://api.github.com/users/crazy-max/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/crazy-max/subscriptions",
        "type": "User",
        "url": "https://api.github.com/users/crazy-max"
      }
    },
    "html_url": "https://github.com/docker/test-docker-action/pull/15",
    "id": 912840343,
    "issue_url": "https://api.github.com/repos/docker/test-docker-action/issues/15",
    "labels": [],
    "locked": false,
    "maintainer_can_modify": true,
    "merge_commit_sha": null,
    "mergeable": null,
    "mergeable_state": "unknown",
    "merged": false,
    "merged_at": null,
    "merged_by": null,
    "milestone": null,
    "node_id": "PR_kwDOEQjNNc42aNaX",
    "number": 15,
    "patch_url": "https://github.com/docker/test-docker-action/pull/15.patch",
    "rebaseable": null,
    "requested_reviewers": [],
    "requested_teams": [],
    "review_comment_url": "https://api.github.com/repos/docker/test-docker-action/pulls/comments{/number}",
    "review_comments": 0,
    "review_comments_url": "https://api.github.com/repos/docker/test-docker-action/pulls/15/comments",
    "state": "open",
    "statuses_url": "https://api.github.com/repos/docker/test-docker-action/statuses/3370e228f2209994d57af4427fe64e71bb79ac96",
    "title": "small change",
    "updated_at": "2022-04-19T09:16:17Z",
    "url": "https://api.github.com/repos/docker/test-docker-action/pulls/15",
    "user": {
      "avatar_url": "https://avatars.githubusercontent.com/u/1951866?v=4",
      "events_url": "https://api.github.com/users/crazy-max/events{/privacy}",
      "followers_url": "https://api.github.com/users/crazy-max/followers",
      "following_url": "https://api.github.com/users/crazy-max/following{/other_user}",
      "gists_url": "https://api.github.com/users/crazy-max/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/crazy-max",
      "id": 1951866,
      "login": "crazy-max",
      "node_id": "MDQ6VXNlcjE5NTE4NjY=",
      "organizations_url": "https://api.github.com/users/crazy-max/orgs",
      "received_events_url": "https://api.github.com/users/crazy-max/received_events",
      "repos_url": "https://api.github.com/users/crazy-max/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/crazy-max/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/crazy-max/subscriptions",
      "type": "User",
      "url": "https://api.github.com/users/crazy-max"
    }
  },
  "repository": {
    "allow_forking": true,
    "archive_url": "https://api.github.com/repos/docker/test-docker-action/{archive_format}{/ref}",
    "archived": false,
    "assignees_url": "https://api.github.com/repos/docker/test-docker-action/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/docker/test-docker-action/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/docker/test-docker-action/branches{/branch}",
    "clone_url": "https://github.com/docker/test-docker-action.git",
    "collaborators_url": "https://api.github.com/repos/docker/test-docker-action/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/docker/test-docker-action/comments{/number}",
    "commits_url": "https://api.github.com/repos/docker/test-docker-action/commits{/sha}",
    "compare_url": "https://api.github.com/repos/docker/test-docker-action/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/docker/test-docker-action/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/docker/test-docker-action/contributors",
    "created_at": "2020-08-07T09:23:00Z",
    "default_branch": "master",
    "deployments_url": "https://api.github.com/repos/docker/test-docker-action/deployments",
    "description": "Test \"Docker\" Actions",
    "disabled": false,
    "downloads_url": "https://api.github.com/repos/docker/test-docker-action/downloads",
    "events_url": "https://api.github.com/repos/docker/test-docker-action/events",
    "fork": false,
    "forks": 1,
    "forks_count": 1,
    "forks_url": "https://api.github.com/repos/docker/test-docker-action/forks",
    "full_name": "docker/test-docker-action",
    "git_commits_url": "https://api.github.com/repos/docker/test-docker-action/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/docker/test-docker-action/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/docker/test-docker-action/git/tags{/sha}",
    "git_url": "git://github.com/docker/test-docker-action.git",
    "has_downloads": true,
    "has_issues": true,
    "has_pages": false,
    "has_projects": true,
    "has_wiki": true,
    "homepage": "",
    "hooks_url": "https://api.github.com/repos/docker/test-docker-action/hooks",
    "html_url": "https://github.com/docker/test-docker-action",
    "id": 285789493,
    "is_template": false,
    "issue_comment_url": "https://api.github.com/repos/docker/test-docker-action/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/docker/test-docker-action/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/docker/test-docker-action/issues{/number}",
    "keys_url": "https://api.github.com/repos/docker/test-docker-action/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/docker/test-docker-action/labels{/name}",
    "language": "JavaScript",
    "languages_url": "https://api.github.com/repos/docker/test-docker-action/languages",
    "license": {
      "key": "mit",
      "name": "MIT License",
      "node_id": "MDc6TGljZW5zZTEz",
      "spdx_id": "MIT",
      "url": "https://api.github.com/licenses/mit"
    },
    "merges_url": "https://api.github.com/repos/docker/test-docker-action/merges",
    "milestones_url": "https://api.github.com/repos/docker/test-docker-action/milestones{/number}",
    "mirror_url": null,
    "name": "test-docker-action",
    "node_id": "MDEwOlJlcG9zaXRvcnkyODU3ODk0OTM=",
    "notifications_url": "https://api.github.com/repos/docker/test-docker-action/notifications{?since,all,participating}",
    "open_issues": 6,
    "open_issues_count": 6,
    "owner": {
      "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
      "events_url": "https://api.github.com/users/docker/events{/privacy}",
      "followers_url": "https://api.github.com/users/docker/followers",
      "following_url": "https://api.github.com/users/docker/following{/other_user}",
      "gists_url": "https://api.github.com/users/docker/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/docker",
      "id": 5429470,
      "login": "docker",
      "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
      "organizations_url": "https://api.github.com/users/docker/orgs",
      "received_events_url": "https://api.github.com/users/docker/received_events",
      "repos_url": "https://api.github.com/users/docker/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/docker/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/docker/subscriptions",
      "type": "Organization",
      "url": "https://api.github.com/users/docker"
    },
    "private": true,
    "pulls_url": "https://api.github.com/repos/docker/test-docker-action/pulls{/number}",
    "pushed_at": "2022-04-19T09:04:50Z",
    "releases_url": "https://api.github.com/repos/docker/test-docker-action/releases{/id}",
    "size": 796,
    "ssh_url": "git@github.com:docker/test-docker-action.git",
    "stargazers_count": 0,
    "stargazers_url": "https://api.github.com/repos/docker/test-docker-action/stargazers",
    "statuses_url": "https://api.github.com/repos/docker/test-docker-action/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/docker/test-docker-action/subscribers",
    "subscription_url": "https://api.github.com/repos/docker/test-docker-action/subscription",
    "svn_url": "https://github.com/docker/test-docker-action",
    "tags_url": "https://api.github.com/repos/docker/test-docker-action/tags",
    "teams_url": "https://api.github.com/repos/docker/test-docker-action/teams",
    "topics": [],
    "trees_url": "https://api.github.com/repos/docker/test-docker-action/git/trees{/sha}",
    "updated_at": "2022-04-19T09:05:09Z",
    "url": "https://api.github.com/repos/docker/test-docker-action",
    "visibility": "private",
    "watchers": 0,
    "watchers_count": 0
  },
  "sender": {
    "avatar_url": "https://avatars.githubusercontent.com/u/1951866?v=4",
    "events_url": "https://api.github.com/users/crazy-max/events{/privacy}",
    "followers_url": "https://api.github.com/users/crazy-max/followers",
    "following_url": "https://api.github.com/users/crazy-max/following{/other_user}",
    "gists_url": "https://api.github.com/users/crazy-max/gists{/gist_id}",
    "gravatar_id": "",
    "html_url": "https://github.com/crazy-max",
    "id": 1951866,
    "login": "crazy-max",
    "node_id": "MDQ6VXNlcjE5NTE4NjY=",
    "organizations_url": "https://api.github.com/users/crazy-max/orgs",
    "received_events_url": "https://api.github.com/users/crazy-max/received_events",
    "repos_url": "https://api.github.com/users/crazy-max/repos",
    "site_admin": false,
    "starred_url": "https://api.github.com/users/crazy-max/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/crazy-max/subscriptions",
    "type": "User",
    "url": "https://api.github.com/users/crazy-max"
  }
}
```

## File: `__tests__/fixtures/event_pull_request_target.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=master
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_2f69f48f-fb93-475f-a6a5-91dc7866f518
GITHUB_EVENT_NAME=pull_request_target
GITHUB_EVENT_PATH=./__tests__/fixtures/event_pull_request_target.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=test-pr
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_2f69f48f-fb93-475f-a6a5-91dc7866f518
GITHUB_REF=refs/heads/master
GITHUB_REF_NAME=master
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=branch
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188688000
GITHUB_RUN_NUMBER=10
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=266574110acf203503badf966df2ea24b5d732d7
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_2f69f48f-fb93-475f-a6a5-91dc7866f518
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_pull_request_target.json`
```json
{
  "action": "opened",
  "number": 15,
  "organization": {
    "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
    "description": "Docker helps developers bring their ideas to life by conquering the complexity of app development.",
    "events_url": "https://api.github.com/orgs/docker/events",
    "hooks_url": "https://api.github.com/orgs/docker/hooks",
    "id": 5429470,
    "issues_url": "https://api.github.com/orgs/docker/issues",
    "login": "docker",
    "members_url": "https://api.github.com/orgs/docker/members{/member}",
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
    "public_members_url": "https://api.github.com/orgs/docker/public_members{/member}",
    "repos_url": "https://api.github.com/orgs/docker/repos",
    "url": "https://api.github.com/orgs/docker"
  },
  "pull_request": {
    "_links": {
      "comments": {
        "href": "https://api.github.com/repos/docker/test-docker-action/issues/15/comments"
      },
      "commits": {
        "href": "https://api.github.com/repos/docker/test-docker-action/pulls/15/commits"
      },
      "html": {
        "href": "https://github.com/docker/test-docker-action/pull/15"
      },
      "issue": {
        "href": "https://api.github.com/repos/docker/test-docker-action/issues/15"
      },
      "review_comment": {
        "href": "https://api.github.com/repos/docker/test-docker-action/pulls/comments{/number}"
      },
      "review_comments": {
        "href": "https://api.github.com/repos/docker/test-docker-action/pulls/15/comments"
      },
      "self": {
        "href": "https://api.github.com/repos/docker/test-docker-action/pulls/15"
      },
      "statuses": {
        "href": "https://api.github.com/repos/docker/test-docker-action/statuses/3370e228f2209994d57af4427fe64e71bb79ac96"
      }
    },
    "active_lock_reason": null,
    "additions": 1,
    "assignee": null,
    "assignees": [],
    "author_association": "COLLABORATOR",
    "auto_merge": null,
    "base": {
      "label": "docker:master",
      "ref": "master",
      "repo": {
        "allow_auto_merge": false,
        "allow_forking": true,
        "allow_merge_commit": true,
        "allow_rebase_merge": true,
        "allow_squash_merge": true,
        "allow_update_branch": false,
        "archive_url": "https://api.github.com/repos/docker/test-docker-action/{archive_format}{/ref}",
        "archived": false,
        "assignees_url": "https://api.github.com/repos/docker/test-docker-action/assignees{/user}",
        "blobs_url": "https://api.github.com/repos/docker/test-docker-action/git/blobs{/sha}",
        "branches_url": "https://api.github.com/repos/docker/test-docker-action/branches{/branch}",
        "clone_url": "https://github.com/docker/test-docker-action.git",
        "collaborators_url": "https://api.github.com/repos/docker/test-docker-action/collaborators{/collaborator}",
        "comments_url": "https://api.github.com/repos/docker/test-docker-action/comments{/number}",
        "commits_url": "https://api.github.com/repos/docker/test-docker-action/commits{/sha}",
        "compare_url": "https://api.github.com/repos/docker/test-docker-action/compare/{base}...{head}",
        "contents_url": "https://api.github.com/repos/docker/test-docker-action/contents/{+path}",
        "contributors_url": "https://api.github.com/repos/docker/test-docker-action/contributors",
        "created_at": "2020-08-07T09:23:00Z",
        "default_branch": "master",
        "delete_branch_on_merge": false,
        "deployments_url": "https://api.github.com/repos/docker/test-docker-action/deployments",
        "description": "Test \"Docker\" Actions",
        "disabled": false,
        "downloads_url": "https://api.github.com/repos/docker/test-docker-action/downloads",
        "events_url": "https://api.github.com/repos/docker/test-docker-action/events",
        "fork": false,
        "forks": 1,
        "forks_count": 1,
        "forks_url": "https://api.github.com/repos/docker/test-docker-action/forks",
        "full_name": "docker/test-docker-action",
        "git_commits_url": "https://api.github.com/repos/docker/test-docker-action/git/commits{/sha}",
        "git_refs_url": "https://api.github.com/repos/docker/test-docker-action/git/refs{/sha}",
        "git_tags_url": "https://api.github.com/repos/docker/test-docker-action/git/tags{/sha}",
        "git_url": "git://github.com/docker/test-docker-action.git",
        "has_downloads": true,
        "has_issues": true,
        "has_pages": false,
        "has_projects": true,
        "has_wiki": true,
        "homepage": "",
        "hooks_url": "https://api.github.com/repos/docker/test-docker-action/hooks",
        "html_url": "https://github.com/docker/test-docker-action",
        "id": 285789493,
        "is_template": false,
        "issue_comment_url": "https://api.github.com/repos/docker/test-docker-action/issues/comments{/number}",
        "issue_events_url": "https://api.github.com/repos/docker/test-docker-action/issues/events{/number}",
        "issues_url": "https://api.github.com/repos/docker/test-docker-action/issues{/number}",
        "keys_url": "https://api.github.com/repos/docker/test-docker-action/keys{/key_id}",
        "labels_url": "https://api.github.com/repos/docker/test-docker-action/labels{/name}",
        "language": "JavaScript",
        "languages_url": "https://api.github.com/repos/docker/test-docker-action/languages",
        "license": {
          "key": "mit",
          "name": "MIT License",
          "node_id": "MDc6TGljZW5zZTEz",
          "spdx_id": "MIT",
          "url": "https://api.github.com/licenses/mit"
        },
        "merges_url": "https://api.github.com/repos/docker/test-docker-action/merges",
        "milestones_url": "https://api.github.com/repos/docker/test-docker-action/milestones{/number}",
        "mirror_url": null,
        "name": "test-docker-action",
        "node_id": "MDEwOlJlcG9zaXRvcnkyODU3ODk0OTM=",
        "notifications_url": "https://api.github.com/repos/docker/test-docker-action/notifications{?since,all,participating}",
        "open_issues": 6,
        "open_issues_count": 6,
        "owner": {
          "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
          "events_url": "https://api.github.com/users/docker/events{/privacy}",
          "followers_url": "https://api.github.com/users/docker/followers",
          "following_url": "https://api.github.com/users/docker/following{/other_user}",
          "gists_url": "https://api.github.com/users/docker/gists{/gist_id}",
          "gravatar_id": "",
          "html_url": "https://github.com/docker",
          "id": 5429470,
          "login": "docker",
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
          "organizations_url": "https://api.github.com/users/docker/orgs",
          "received_events_url": "https://api.github.com/users/docker/received_events",
          "repos_url": "https://api.github.com/users/docker/repos",
          "site_admin": false,
          "starred_url": "https://api.github.com/users/docker/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/docker/subscriptions",
          "type": "Organization",
          "url": "https://api.github.com/users/docker"
        },
        "private": true,
        "pulls_url": "https://api.github.com/repos/docker/test-docker-action/pulls{/number}",
        "pushed_at": "2022-04-19T09:04:50Z",
        "releases_url": "https://api.github.com/repos/docker/test-docker-action/releases{/id}",
        "size": 796,
        "ssh_url": "git@github.com:docker/test-docker-action.git",
        "stargazers_count": 0,
        "stargazers_url": "https://api.github.com/repos/docker/test-docker-action/stargazers",
        "statuses_url": "https://api.github.com/repos/docker/test-docker-action/statuses/{sha}",
        "subscribers_url": "https://api.github.com/repos/docker/test-docker-action/subscribers",
        "subscription_url": "https://api.github.com/repos/docker/test-docker-action/subscription",
        "svn_url": "https://github.com/docker/test-docker-action",
        "tags_url": "https://api.github.com/repos/docker/test-docker-action/tags",
        "teams_url": "https://api.github.com/repos/docker/test-docker-action/teams",
        "topics": [],
        "trees_url": "https://api.github.com/repos/docker/test-docker-action/git/trees{/sha}",
        "updated_at": "2022-04-19T09:05:09Z",
        "url": "https://api.github.com/repos/docker/test-docker-action",
        "visibility": "private",
        "watchers": 0,
        "watchers_count": 0
      },
      "sha": "266574110acf203503badf966df2ea24b5d732d7",
      "user": {
        "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
        "events_url": "https://api.github.com/users/docker/events{/privacy}",
        "followers_url": "https://api.github.com/users/docker/followers",
        "following_url": "https://api.github.com/users/docker/following{/other_user}",
        "gists_url": "https://api.github.com/users/docker/gists{/gist_id}",
        "gravatar_id": "",
        "html_url": "https://github.com/docker",
        "id": 5429470,
        "login": "docker",
        "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
        "organizations_url": "https://api.github.com/users/docker/orgs",
        "received_events_url": "https://api.github.com/users/docker/received_events",
        "repos_url": "https://api.github.com/users/docker/repos",
        "site_admin": false,
        "starred_url": "https://api.github.com/users/docker/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/docker/subscriptions",
        "type": "Organization",
        "url": "https://api.github.com/users/docker"
      }
    },
    "body": null,
    "changed_files": 1,
    "closed_at": null,
    "comments": 0,
    "comments_url": "https://api.github.com/repos/docker/test-docker-action/issues/15/comments",
    "commits": 1,
    "commits_url": "https://api.github.com/repos/docker/test-docker-action/pulls/15/commits",
    "created_at": "2022-04-19T09:16:17Z",
    "deletions": 1,
    "diff_url": "https://github.com/docker/test-docker-action/pull/15.diff",
    "draft": false,
    "head": {
      "label": "crazy-max:test-pr",
      "ref": "test-pr",
      "repo": {
        "allow_auto_merge": false,
        "allow_forking": true,
        "allow_merge_commit": true,
        "allow_rebase_merge": true,
        "allow_squash_merge": true,
        "allow_update_branch": false,
        "archive_url": "https://api.github.com/repos/crazy-max/test-docker-action/{archive_format}{/ref}",
        "archived": false,
        "assignees_url": "https://api.github.com/repos/crazy-max/test-docker-action/assignees{/user}",
        "blobs_url": "https://api.github.com/repos/crazy-max/test-docker-action/git/blobs{/sha}",
        "branches_url": "https://api.github.com/repos/crazy-max/test-docker-action/branches{/branch}",
        "clone_url": "https://github.com/crazy-max/test-docker-action.git",
        "collaborators_url": "https://api.github.com/repos/crazy-max/test-docker-action/collaborators{/collaborator}",
        "comments_url": "https://api.github.com/repos/crazy-max/test-docker-action/comments{/number}",
        "commits_url": "https://api.github.com/repos/crazy-max/test-docker-action/commits{/sha}",
        "compare_url": "https://api.github.com/repos/crazy-max/test-docker-action/compare/{base}...{head}",
        "contents_url": "https://api.github.com/repos/crazy-max/test-docker-action/contents/{+path}",
        "contributors_url": "https://api.github.com/repos/crazy-max/test-docker-action/contributors",
        "created_at": "2021-07-11T17:34:22Z",
        "default_branch": "master",
        "delete_branch_on_merge": false,
        "deployments_url": "https://api.github.com/repos/crazy-max/test-docker-action/deployments",
        "description": "Test \"Docker\" Actions",
        "disabled": false,
        "downloads_url": "https://api.github.com/repos/crazy-max/test-docker-action/downloads",
        "events_url": "https://api.github.com/repos/crazy-max/test-docker-action/events",
        "fork": true,
        "forks": 0,
        "forks_count": 0,
        "forks_url": "https://api.github.com/repos/crazy-max/test-docker-action/forks",
        "full_name": "crazy-max/test-docker-action",
        "git_commits_url": "https://api.github.com/repos/crazy-max/test-docker-action/git/commits{/sha}",
        "git_refs_url": "https://api.github.com/repos/crazy-max/test-docker-action/git/refs{/sha}",
        "git_tags_url": "https://api.github.com/repos/crazy-max/test-docker-action/git/tags{/sha}",
        "git_url": "git://github.com/crazy-max/test-docker-action.git",
        "has_downloads": true,
        "has_issues": false,
        "has_pages": false,
        "has_projects": true,
        "has_wiki": false,
        "homepage": "",
        "hooks_url": "https://api.github.com/repos/crazy-max/test-docker-action/hooks",
        "html_url": "https://github.com/crazy-max/test-docker-action",
        "id": 385013169,
        "is_template": false,
        "issue_comment_url": "https://api.github.com/repos/crazy-max/test-docker-action/issues/comments{/number}",
        "issue_events_url": "https://api.github.com/repos/crazy-max/test-docker-action/issues/events{/number}",
        "issues_url": "https://api.github.com/repos/crazy-max/test-docker-action/issues{/number}",
        "keys_url": "https://api.github.com/repos/crazy-max/test-docker-action/keys{/key_id}",
        "labels_url": "https://api.github.com/repos/crazy-max/test-docker-action/labels{/name}",
        "language": "JavaScript",
        "languages_url": "https://api.github.com/repos/crazy-max/test-docker-action/languages",
        "license": {
          "key": "mit",
          "name": "MIT License",
          "node_id": "MDc6TGljZW5zZTEz",
          "spdx_id": "MIT",
          "url": "https://api.github.com/licenses/mit"
        },
        "merges_url": "https://api.github.com/repos/crazy-max/test-docker-action/merges",
        "milestones_url": "https://api.github.com/repos/crazy-max/test-docker-action/milestones{/number}",
        "mirror_url": null,
        "name": "test-docker-action",
        "node_id": "MDEwOlJlcG9zaXRvcnkzODUwMTMxNjk=",
        "notifications_url": "https://api.github.com/repos/crazy-max/test-docker-action/notifications{?since,all,participating}",
        "open_issues": 0,
        "open_issues_count": 0,
        "owner": {
          "avatar_url": "https://avatars.githubusercontent.com/u/1951866?v=4",
          "events_url": "https://api.github.com/users/crazy-max/events{/privacy}",
          "followers_url": "https://api.github.com/users/crazy-max/followers",
          "following_url": "https://api.github.com/users/crazy-max/following{/other_user}",
          "gists_url": "https://api.github.com/users/crazy-max/gists{/gist_id}",
          "gravatar_id": "",
          "html_url": "https://github.com/crazy-max",
          "id": 1951866,
          "login": "crazy-max",
          "node_id": "MDQ6VXNlcjE5NTE4NjY=",
          "organizations_url": "https://api.github.com/users/crazy-max/orgs",
          "received_events_url": "https://api.github.com/users/crazy-max/received_events",
          "repos_url": "https://api.github.com/users/crazy-max/repos",
          "site_admin": false,
          "starred_url": "https://api.github.com/users/crazy-max/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/crazy-max/subscriptions",
          "type": "User",
          "url": "https://api.github.com/users/crazy-max"
        },
        "private": true,
        "pulls_url": "https://api.github.com/repos/crazy-max/test-docker-action/pulls{/number}",
        "pushed_at": "2022-04-19T09:16:07Z",
        "releases_url": "https://api.github.com/repos/crazy-max/test-docker-action/releases{/id}",
        "size": 151,
        "ssh_url": "git@github.com:crazy-max/test-docker-action.git",
        "stargazers_count": 0,
        "stargazers_url": "https://api.github.com/repos/crazy-max/test-docker-action/stargazers",
        "statuses_url": "https://api.github.com/repos/crazy-max/test-docker-action/statuses/{sha}",
        "subscribers_url": "https://api.github.com/repos/crazy-max/test-docker-action/subscribers",
        "subscription_url": "https://api.github.com/repos/crazy-max/test-docker-action/subscription",
        "svn_url": "https://github.com/crazy-max/test-docker-action",
        "tags_url": "https://api.github.com/repos/crazy-max/test-docker-action/tags",
        "teams_url": "https://api.github.com/repos/crazy-max/test-docker-action/teams",
        "topics": [],
        "trees_url": "https://api.github.com/repos/crazy-max/test-docker-action/git/trees{/sha}",
        "updated_at": "2022-04-19T09:13:10Z",
        "url": "https://api.github.com/repos/crazy-max/test-docker-action",
        "visibility": "private",
        "watchers": 0,
        "watchers_count": 0
      },
      "sha": "3370e228f2209994d57af4427fe64e71bb79ac96",
      "user": {
        "avatar_url": "https://avatars.githubusercontent.com/u/1951866?v=4",
        "events_url": "https://api.github.com/users/crazy-max/events{/privacy}",
        "followers_url": "https://api.github.com/users/crazy-max/followers",
        "following_url": "https://api.github.com/users/crazy-max/following{/other_user}",
        "gists_url": "https://api.github.com/users/crazy-max/gists{/gist_id}",
        "gravatar_id": "",
        "html_url": "https://github.com/crazy-max",
        "id": 1951866,
        "login": "crazy-max",
        "node_id": "MDQ6VXNlcjE5NTE4NjY=",
        "organizations_url": "https://api.github.com/users/crazy-max/orgs",
        "received_events_url": "https://api.github.com/users/crazy-max/received_events",
        "repos_url": "https://api.github.com/users/crazy-max/repos",
        "site_admin": false,
        "starred_url": "https://api.github.com/users/crazy-max/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/crazy-max/subscriptions",
        "type": "User",
        "url": "https://api.github.com/users/crazy-max"
      }
    },
    "html_url": "https://github.com/docker/test-docker-action/pull/15",
    "id": 912840343,
    "issue_url": "https://api.github.com/repos/docker/test-docker-action/issues/15",
    "labels": [],
    "locked": false,
    "maintainer_can_modify": true,
    "merge_commit_sha": null,
    "mergeable": null,
    "mergeable_state": "unknown",
    "merged": false,
    "merged_at": null,
    "merged_by": null,
    "milestone": null,
    "node_id": "PR_kwDOEQjNNc42aNaX",
    "number": 15,
    "patch_url": "https://github.com/docker/test-docker-action/pull/15.patch",
    "rebaseable": null,
    "requested_reviewers": [],
    "requested_teams": [],
    "review_comment_url": "https://api.github.com/repos/docker/test-docker-action/pulls/comments{/number}",
    "review_comments": 0,
    "review_comments_url": "https://api.github.com/repos/docker/test-docker-action/pulls/15/comments",
    "state": "open",
    "statuses_url": "https://api.github.com/repos/docker/test-docker-action/statuses/3370e228f2209994d57af4427fe64e71bb79ac96",
    "title": "small change",
    "updated_at": "2022-04-19T09:16:17Z",
    "url": "https://api.github.com/repos/docker/test-docker-action/pulls/15",
    "user": {
      "avatar_url": "https://avatars.githubusercontent.com/u/1951866?v=4",
      "events_url": "https://api.github.com/users/crazy-max/events{/privacy}",
      "followers_url": "https://api.github.com/users/crazy-max/followers",
      "following_url": "https://api.github.com/users/crazy-max/following{/other_user}",
      "gists_url": "https://api.github.com/users/crazy-max/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/crazy-max",
      "id": 1951866,
      "login": "crazy-max",
      "node_id": "MDQ6VXNlcjE5NTE4NjY=",
      "organizations_url": "https://api.github.com/users/crazy-max/orgs",
      "received_events_url": "https://api.github.com/users/crazy-max/received_events",
      "repos_url": "https://api.github.com/users/crazy-max/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/crazy-max/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/crazy-max/subscriptions",
      "type": "User",
      "url": "https://api.github.com/users/crazy-max"
    }
  },
  "repository": {
    "allow_forking": true,
    "archive_url": "https://api.github.com/repos/docker/test-docker-action/{archive_format}{/ref}",
    "archived": false,
    "assignees_url": "https://api.github.com/repos/docker/test-docker-action/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/docker/test-docker-action/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/docker/test-docker-action/branches{/branch}",
    "clone_url": "https://github.com/docker/test-docker-action.git",
    "collaborators_url": "https://api.github.com/repos/docker/test-docker-action/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/docker/test-docker-action/comments{/number}",
    "commits_url": "https://api.github.com/repos/docker/test-docker-action/commits{/sha}",
    "compare_url": "https://api.github.com/repos/docker/test-docker-action/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/docker/test-docker-action/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/docker/test-docker-action/contributors",
    "created_at": "2020-08-07T09:23:00Z",
    "default_branch": "master",
    "deployments_url": "https://api.github.com/repos/docker/test-docker-action/deployments",
    "description": "Test \"Docker\" Actions",
    "disabled": false,
    "downloads_url": "https://api.github.com/repos/docker/test-docker-action/downloads",
    "events_url": "https://api.github.com/repos/docker/test-docker-action/events",
    "fork": false,
    "forks": 1,
    "forks_count": 1,
    "forks_url": "https://api.github.com/repos/docker/test-docker-action/forks",
    "full_name": "docker/test-docker-action",
    "git_commits_url": "https://api.github.com/repos/docker/test-docker-action/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/docker/test-docker-action/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/docker/test-docker-action/git/tags{/sha}",
    "git_url": "git://github.com/docker/test-docker-action.git",
    "has_downloads": true,
    "has_issues": true,
    "has_pages": false,
    "has_projects": true,
    "has_wiki": true,
    "homepage": "",
    "hooks_url": "https://api.github.com/repos/docker/test-docker-action/hooks",
    "html_url": "https://github.com/docker/test-docker-action",
    "id": 285789493,
    "is_template": false,
    "issue_comment_url": "https://api.github.com/repos/docker/test-docker-action/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/docker/test-docker-action/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/docker/test-docker-action/issues{/number}",
    "keys_url": "https://api.github.com/repos/docker/test-docker-action/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/docker/test-docker-action/labels{/name}",
    "language": "JavaScript",
    "languages_url": "https://api.github.com/repos/docker/test-docker-action/languages",
    "license": {
      "key": "mit",
      "name": "MIT License",
      "node_id": "MDc6TGljZW5zZTEz",
      "spdx_id": "MIT",
      "url": "https://api.github.com/licenses/mit"
    },
    "merges_url": "https://api.github.com/repos/docker/test-docker-action/merges",
    "milestones_url": "https://api.github.com/repos/docker/test-docker-action/milestones{/number}",
    "mirror_url": null,
    "name": "test-docker-action",
    "node_id": "MDEwOlJlcG9zaXRvcnkyODU3ODk0OTM=",
    "notifications_url": "https://api.github.com/repos/docker/test-docker-action/notifications{?since,all,participating}",
    "open_issues": 6,
    "open_issues_count": 6,
    "owner": {
      "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
      "events_url": "https://api.github.com/users/docker/events{/privacy}",
      "followers_url": "https://api.github.com/users/docker/followers",
      "following_url": "https://api.github.com/users/docker/following{/other_user}",
      "gists_url": "https://api.github.com/users/docker/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/docker",
      "id": 5429470,
      "login": "docker",
      "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
      "organizations_url": "https://api.github.com/users/docker/orgs",
      "received_events_url": "https://api.github.com/users/docker/received_events",
      "repos_url": "https://api.github.com/users/docker/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/docker/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/docker/subscriptions",
      "type": "Organization",
      "url": "https://api.github.com/users/docker"
    },
    "private": true,
    "pulls_url": "https://api.github.com/repos/docker/test-docker-action/pulls{/number}",
    "pushed_at": "2022-04-19T09:04:50Z",
    "releases_url": "https://api.github.com/repos/docker/test-docker-action/releases{/id}",
    "size": 796,
    "ssh_url": "git@github.com:docker/test-docker-action.git",
    "stargazers_count": 0,
    "stargazers_url": "https://api.github.com/repos/docker/test-docker-action/stargazers",
    "statuses_url": "https://api.github.com/repos/docker/test-docker-action/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/docker/test-docker-action/subscribers",
    "subscription_url": "https://api.github.com/repos/docker/test-docker-action/subscription",
    "svn_url": "https://github.com/docker/test-docker-action",
    "tags_url": "https://api.github.com/repos/docker/test-docker-action/tags",
    "teams_url": "https://api.github.com/repos/docker/test-docker-action/teams",
    "topics": [],
    "trees_url": "https://api.github.com/repos/docker/test-docker-action/git/trees{/sha}",
    "updated_at": "2022-04-19T09:05:09Z",
    "url": "https://api.github.com/repos/docker/test-docker-action",
    "visibility": "private",
    "watchers": 0,
    "watchers_count": 0
  },
  "sender": {
    "avatar_url": "https://avatars.githubusercontent.com/u/1951866?v=4",
    "events_url": "https://api.github.com/users/crazy-max/events{/privacy}",
    "followers_url": "https://api.github.com/users/crazy-max/followers",
    "following_url": "https://api.github.com/users/crazy-max/following{/other_user}",
    "gists_url": "https://api.github.com/users/crazy-max/gists{/gist_id}",
    "gravatar_id": "",
    "html_url": "https://github.com/crazy-max",
    "id": 1951866,
    "login": "crazy-max",
    "node_id": "MDQ6VXNlcjE5NTE4NjY=",
    "organizations_url": "https://api.github.com/users/crazy-max/orgs",
    "received_events_url": "https://api.github.com/users/crazy-max/received_events",
    "repos_url": "https://api.github.com/users/crazy-max/repos",
    "site_admin": false,
    "starred_url": "https://api.github.com/users/crazy-max/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/crazy-max/subscriptions",
    "type": "User",
    "url": "https://api.github.com/users/crazy-max"
  }
}
```

## File: `__tests__/fixtures/event_push_dev.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_dce158a5-37b3-4081-8414-32238d5cfa7b
GITHUB_EVENT_NAME=push
GITHUB_EVENT_PATH=./__tests__/fixtures/event_push_dev.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_dce158a5-37b3-4081-8414-32238d5cfa7b
GITHUB_REF=refs/heads/dev
GITHUB_REF_NAME=dev
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=branch
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188748038
GITHUB_RUN_NUMBER=15
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=860c1904a1ce19322e91ac35af1ab07466440c37
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_dce158a5-37b3-4081-8414-32238d5cfa7b
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_push_dev.json`
```json
{
  "after": "860c1904a1ce19322e91ac35af1ab07466440c37",
  "base_ref": null,
  "before": "5f3331d7f7044c18ca9f12c77d961c4d7cf3276a",
  "commits": [
    {
      "author": {
        "email": "crazy-max@users.noreply.github.com",
        "name": "CrazyMax",
        "username": "crazy-max"
      },
      "committer": {
        "email": "crazy-max@users.noreply.github.com",
        "name": "CrazyMax",
        "username": "crazy-max"
      },
      "distinct": true,
      "id": "860c1904a1ce19322e91ac35af1ab07466440c37",
      "message": "hello dev",
      "timestamp": "2022-04-19T11:27:24+02:00",
      "tree_id": "d2c60af597e863787d2d27f569e30495b0b92820",
      "url": "https://github.com/docker/test-docker-action/commit/860c1904a1ce19322e91ac35af1ab07466440c37"
    }
  ],
  "compare": "https://github.com/docker/test-docker-action/compare/5f3331d7f704...860c1904a1ce",
  "created": false,
  "deleted": false,
  "forced": false,
  "head_commit": {
    "author": {
      "email": "crazy-max@users.noreply.github.com",
      "name": "CrazyMax",
      "username": "crazy-max"
    },
    "committer": {
      "email": "crazy-max@users.noreply.github.com",
      "name": "CrazyMax",
      "username": "crazy-max"
    },
    "distinct": true,
    "id": "860c1904a1ce19322e91ac35af1ab07466440c37",
    "message": "hello dev",
    "timestamp": "2022-04-19T11:27:24+02:00",
    "tree_id": "d2c60af597e863787d2d27f569e30495b0b92820",
    "url": "https://github.com/docker/test-docker-action/commit/860c1904a1ce19322e91ac35af1ab07466440c37"
  },
  "organization": {
    "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
    "description": "Docker helps developers bring their ideas to life by conquering the complexity of app development.",
    "events_url": "https://api.github.com/orgs/docker/events",
    "hooks_url": "https://api.github.com/orgs/docker/hooks",
    "id": 5429470,
    "issues_url": "https://api.github.com/orgs/docker/issues",
    "login": "docker",
    "members_url": "https://api.github.com/orgs/docker/members{/member}",
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
    "public_members_url": "https://api.github.com/orgs/docker/public_members{/member}",
    "repos_url": "https://api.github.com/orgs/docker/repos",
    "url": "https://api.github.com/orgs/docker"
  },
  "pusher": {
    "email": "github@crazymax.dev",
    "name": "crazy-max"
  },
  "ref": "refs/heads/dev",
  "repository": {
    "allow_forking": true,
    "archive_url": "https://api.github.com/repos/docker/test-docker-action/{archive_format}{/ref}",
    "archived": false,
    "assignees_url": "https://api.github.com/repos/docker/test-docker-action/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/docker/test-docker-action/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/docker/test-docker-action/branches{/branch}",
    "clone_url": "https://github.com/docker/test-docker-action.git",
    "collaborators_url": "https://api.github.com/repos/docker/test-docker-action/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/docker/test-docker-action/comments{/number}",
    "commits_url": "https://api.github.com/repos/docker/test-docker-action/commits{/sha}",
    "compare_url": "https://api.github.com/repos/docker/test-docker-action/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/docker/test-docker-action/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/docker/test-docker-action/contributors",
    "created_at": 1596792180,
    "default_branch": "master",
    "deployments_url": "https://api.github.com/repos/docker/test-docker-action/deployments",
    "description": "Test \"Docker\" Actions",
    "disabled": false,
    "downloads_url": "https://api.github.com/repos/docker/test-docker-action/downloads",
    "events_url": "https://api.github.com/repos/docker/test-docker-action/events",
    "fork": false,
    "forks": 1,
    "forks_count": 1,
    "forks_url": "https://api.github.com/repos/docker/test-docker-action/forks",
    "full_name": "docker/test-docker-action",
    "git_commits_url": "https://api.github.com/repos/docker/test-docker-action/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/docker/test-docker-action/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/docker/test-docker-action/git/tags{/sha}",
    "git_url": "git://github.com/docker/test-docker-action.git",
    "has_downloads": true,
    "has_issues": true,
    "has_pages": false,
    "has_projects": true,
    "has_wiki": true,
    "homepage": "",
    "hooks_url": "https://api.github.com/repos/docker/test-docker-action/hooks",
    "html_url": "https://github.com/docker/test-docker-action",
    "id": 285789493,
    "is_template": false,
    "issue_comment_url": "https://api.github.com/repos/docker/test-docker-action/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/docker/test-docker-action/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/docker/test-docker-action/issues{/number}",
    "keys_url": "https://api.github.com/repos/docker/test-docker-action/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/docker/test-docker-action/labels{/name}",
    "language": "JavaScript",
    "languages_url": "https://api.github.com/repos/docker/test-docker-action/languages",
    "license": {
      "key": "mit",
      "name": "MIT License",
      "node_id": "MDc6TGljZW5zZTEz",
      "spdx_id": "MIT",
      "url": "https://api.github.com/licenses/mit"
    },
    "master_branch": "master",
    "merges_url": "https://api.github.com/repos/docker/test-docker-action/merges",
    "milestones_url": "https://api.github.com/repos/docker/test-docker-action/milestones{/number}",
    "mirror_url": null,
    "name": "test-docker-action",
    "node_id": "MDEwOlJlcG9zaXRvcnkyODU3ODk0OTM=",
    "notifications_url": "https://api.github.com/repos/docker/test-docker-action/notifications{?since,all,participating}",
    "open_issues": 6,
    "open_issues_count": 6,
    "organization": "docker",
    "owner": {
      "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
      "email": "info@docker.com",
      "events_url": "https://api.github.com/users/docker/events{/privacy}",
      "followers_url": "https://api.github.com/users/docker/followers",
      "following_url": "https://api.github.com/users/docker/following{/other_user}",
      "gists_url": "https://api.github.com/users/docker/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/docker",
      "id": 5429470,
      "login": "docker",
      "name": "docker",
      "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
      "organizations_url": "https://api.github.com/users/docker/orgs",
      "received_events_url": "https://api.github.com/users/docker/received_events",
      "repos_url": "https://api.github.com/users/docker/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/docker/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/docker/subscriptions",
      "type": "Organization",
      "url": "https://api.github.com/users/docker"
    },
    "private": true,
    "pulls_url": "https://api.github.com/repos/docker/test-docker-action/pulls{/number}",
    "pushed_at": 1650360446,
    "releases_url": "https://api.github.com/repos/docker/test-docker-action/releases{/id}",
    "size": 796,
    "ssh_url": "git@github.com:docker/test-docker-action.git",
    "stargazers": 0,
    "stargazers_count": 0,
    "stargazers_url": "https://api.github.com/repos/docker/test-docker-action/stargazers",
    "statuses_url": "https://api.github.com/repos/docker/test-docker-action/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/docker/test-docker-action/subscribers",
    "subscription_url": "https://api.github.com/repos/docker/test-docker-action/subscription",
    "svn_url": "https://github.com/docker/test-docker-action",
    "tags_url": "https://api.github.com/repos/docker/test-docker-action/tags",
    "teams_url": "https://api.github.com/repos/docker/test-docker-action/teams",
    "topics": [],
    "trees_url": "https://api.github.com/repos/docker/test-docker-action/git/trees{/sha}",
    "updated_at": "2022-04-19T09:05:09Z",
    "url": "https://github.com/docker/test-docker-action",
    "visibility": "private",
    "watchers": 0,
    "watchers_count": 0
  },
  "sender": {
    "avatar_url": "https://avatars.githubusercontent.com/u/1951866?v=4",
    "events_url": "https://api.github.com/users/crazy-max/events{/privacy}",
    "followers_url": "https://api.github.com/users/crazy-max/followers",
    "following_url": "https://api.github.com/users/crazy-max/following{/other_user}",
    "gists_url": "https://api.github.com/users/crazy-max/gists{/gist_id}",
    "gravatar_id": "",
    "html_url": "https://github.com/crazy-max",
    "id": 1951866,
    "login": "crazy-max",
    "node_id": "MDQ6VXNlcjE5NTE4NjY=",
    "organizations_url": "https://api.github.com/users/crazy-max/orgs",
    "received_events_url": "https://api.github.com/users/crazy-max/received_events",
    "repos_url": "https://api.github.com/users/crazy-max/repos",
    "site_admin": false,
    "starred_url": "https://api.github.com/users/crazy-max/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/crazy-max/subscriptions",
    "type": "User",
    "url": "https://api.github.com/users/crazy-max"
  }
}
```

## File: `__tests__/fixtures/event_push_invalidchars.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_5d7d8f7f-4b47-4f4c-b32a-e7fa634790c9
GITHUB_EVENT_NAME=push
GITHUB_EVENT_PATH=./__tests__/fixtures/event_push_invalidchars.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_5d7d8f7f-4b47-4f4c-b32a-e7fa634790c9
GITHUB_REF=refs/heads/my/feature#1245
GITHUB_REF_NAME=my/feature#1245
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=branch
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188792787
GITHUB_RUN_NUMBER=19
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=983315b5e8d46e46fc4c49869e85e7ee5fb289ba
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_5d7d8f7f-4b47-4f4c-b32a-e7fa634790c9
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_push_invalidchars.json`
```json
{
  "after": "983315b5e8d46e46fc4c49869e85e7ee5fb289ba",
  "base_ref": null,
  "before": "4af2cc040e1cee6ee91e2491f34e5787121eb902",
  "commits": [
    {
      "author": {
        "email": "crazy-max@users.noreply.github.com",
        "name": "CrazyMax",
        "username": "crazy-max"
      },
      "committer": {
        "email": "crazy-max@users.noreply.github.com",
        "name": "CrazyMax",
        "username": "crazy-max"
      },
      "distinct": true,
      "id": "983315b5e8d46e46fc4c49869e85e7ee5fb289ba",
      "message": "feature 1245",
      "timestamp": "2022-04-19T11:36:08+02:00",
      "tree_id": "e9f7b0bf689a49a4792d518088710dadb52d7e9a",
      "url": "https://github.com/docker/test-docker-action/commit/983315b5e8d46e46fc4c49869e85e7ee5fb289ba"
    }
  ],
  "compare": "https://github.com/docker/test-docker-action/compare/4af2cc040e1c...983315b5e8d4",
  "created": false,
  "deleted": false,
  "forced": true,
  "head_commit": {
    "author": {
      "email": "crazy-max@users.noreply.github.com",
      "name": "CrazyMax",
      "username": "crazy-max"
    },
    "committer": {
      "email": "crazy-max@users.noreply.github.com",
      "name": "CrazyMax",
      "username": "crazy-max"
    },
    "distinct": true,
    "id": "983315b5e8d46e46fc4c49869e85e7ee5fb289ba",
    "message": "feature 1245",
    "timestamp": "2022-04-19T11:36:08+02:00",
    "tree_id": "e9f7b0bf689a49a4792d518088710dadb52d7e9a",
    "url": "https://github.com/docker/test-docker-action/commit/983315b5e8d46e46fc4c49869e85e7ee5fb289ba"
  },
  "organization": {
    "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
    "description": "Docker helps developers bring their ideas to life by conquering the complexity of app development.",
    "events_url": "https://api.github.com/orgs/docker/events",
    "hooks_url": "https://api.github.com/orgs/docker/hooks",
    "id": 5429470,
    "issues_url": "https://api.github.com/orgs/docker/issues",
    "login": "docker",
    "members_url": "https://api.github.com/orgs/docker/members{/member}",
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
    "public_members_url": "https://api.github.com/orgs/docker/public_members{/member}",
    "repos_url": "https://api.github.com/orgs/docker/repos",
    "url": "https://api.github.com/orgs/docker"
  },
  "pusher": {
    "email": "github@crazymax.dev",
    "name": "crazy-max"
  },
  "ref": "refs/heads/my/feature#1245",
  "repository": {
    "allow_forking": true,
    "archive_url": "https://api.github.com/repos/docker/test-docker-action/{archive_format}{/ref}",
    "archived": false,
    "assignees_url": "https://api.github.com/repos/docker/test-docker-action/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/docker/test-docker-action/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/docker/test-docker-action/branches{/branch}",
    "clone_url": "https://github.com/docker/test-docker-action.git",
    "collaborators_url": "https://api.github.com/repos/docker/test-docker-action/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/docker/test-docker-action/comments{/number}",
    "commits_url": "https://api.github.com/repos/docker/test-docker-action/commits{/sha}",
    "compare_url": "https://api.github.com/repos/docker/test-docker-action/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/docker/test-docker-action/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/docker/test-docker-action/contributors",
    "created_at": 1596792180,
    "default_branch": "master",
    "deployments_url": "https://api.github.com/repos/docker/test-docker-action/deployments",
    "description": "Test \"Docker\" Actions",
    "disabled": false,
    "downloads_url": "https://api.github.com/repos/docker/test-docker-action/downloads",
    "events_url": "https://api.github.com/repos/docker/test-docker-action/events",
    "fork": false,
    "forks": 1,
    "forks_count": 1,
    "forks_url": "https://api.github.com/repos/docker/test-docker-action/forks",
    "full_name": "docker/test-docker-action",
    "git_commits_url": "https://api.github.com/repos/docker/test-docker-action/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/docker/test-docker-action/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/docker/test-docker-action/git/tags{/sha}",
    "git_url": "git://github.com/docker/test-docker-action.git",
    "has_downloads": true,
    "has_issues": true,
    "has_pages": false,
    "has_projects": true,
    "has_wiki": true,
    "homepage": "",
    "hooks_url": "https://api.github.com/repos/docker/test-docker-action/hooks",
    "html_url": "https://github.com/docker/test-docker-action",
    "id": 285789493,
    "is_template": false,
    "issue_comment_url": "https://api.github.com/repos/docker/test-docker-action/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/docker/test-docker-action/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/docker/test-docker-action/issues{/number}",
    "keys_url": "https://api.github.com/repos/docker/test-docker-action/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/docker/test-docker-action/labels{/name}",
    "language": "JavaScript",
    "languages_url": "https://api.github.com/repos/docker/test-docker-action/languages",
    "license": {
      "key": "mit",
      "name": "MIT License",
      "node_id": "MDc6TGljZW5zZTEz",
      "spdx_id": "MIT",
      "url": "https://api.github.com/licenses/mit"
    },
    "master_branch": "master",
    "merges_url": "https://api.github.com/repos/docker/test-docker-action/merges",
    "milestones_url": "https://api.github.com/repos/docker/test-docker-action/milestones{/number}",
    "mirror_url": null,
    "name": "test-docker-action",
    "node_id": "MDEwOlJlcG9zaXRvcnkyODU3ODk0OTM=",
    "notifications_url": "https://api.github.com/repos/docker/test-docker-action/notifications{?since,all,participating}",
    "open_issues": 6,
    "open_issues_count": 6,
    "organization": "docker",
    "owner": {
      "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
      "email": "info@docker.com",
      "events_url": "https://api.github.com/users/docker/events{/privacy}",
      "followers_url": "https://api.github.com/users/docker/followers",
      "following_url": "https://api.github.com/users/docker/following{/other_user}",
      "gists_url": "https://api.github.com/users/docker/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/docker",
      "id": 5429470,
      "login": "docker",
      "name": "docker",
      "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
      "organizations_url": "https://api.github.com/users/docker/orgs",
      "received_events_url": "https://api.github.com/users/docker/received_events",
      "repos_url": "https://api.github.com/users/docker/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/docker/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/docker/subscriptions",
      "type": "Organization",
      "url": "https://api.github.com/users/docker"
    },
    "private": true,
    "pulls_url": "https://api.github.com/repos/docker/test-docker-action/pulls{/number}",
    "pushed_at": 1650360972,
    "releases_url": "https://api.github.com/repos/docker/test-docker-action/releases{/id}",
    "size": 796,
    "ssh_url": "git@github.com:docker/test-docker-action.git",
    "stargazers": 0,
    "stargazers_count": 0,
    "stargazers_url": "https://api.github.com/repos/docker/test-docker-action/stargazers",
    "statuses_url": "https://api.github.com/repos/docker/test-docker-action/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/docker/test-docker-action/subscribers",
    "subscription_url": "https://api.github.com/repos/docker/test-docker-action/subscription",
    "svn_url": "https://github.com/docker/test-docker-action",
    "tags_url": "https://api.github.com/repos/docker/test-docker-action/tags",
    "teams_url": "https://api.github.com/repos/docker/test-docker-action/teams",
    "topics": [],
    "trees_url": "https://api.github.com/repos/docker/test-docker-action/git/trees{/sha}",
    "updated_at": "2022-04-19T09:05:09Z",
    "url": "https://github.com/docker/test-docker-action",
    "visibility": "private",
    "watchers": 0,
    "watchers_count": 0
  },
  "sender": {
    "avatar_url": "https://avatars.githubusercontent.com/u/1951866?v=4",
    "events_url": "https://api.github.com/users/crazy-max/events{/privacy}",
    "followers_url": "https://api.github.com/users/crazy-max/followers",
    "following_url": "https://api.github.com/users/crazy-max/following{/other_user}",
    "gists_url": "https://api.github.com/users/crazy-max/gists{/gist_id}",
    "gravatar_id": "",
    "html_url": "https://github.com/crazy-max",
    "id": 1951866,
    "login": "crazy-max",
    "node_id": "MDQ6VXNlcjE5NTE4NjY=",
    "organizations_url": "https://api.github.com/users/crazy-max/orgs",
    "received_events_url": "https://api.github.com/users/crazy-max/received_events",
    "repos_url": "https://api.github.com/users/crazy-max/repos",
    "site_admin": false,
    "starred_url": "https://api.github.com/users/crazy-max/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/crazy-max/subscriptions",
    "type": "User",
    "url": "https://api.github.com/users/crazy-max"
  }
}
```

## File: `__tests__/fixtures/event_push_master.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_f5600b76-1b08-404a-8e90-7f2cd620928b
GITHUB_EVENT_NAME=push
GITHUB_EVENT_PATH=./__tests__/fixtures/event_push_master.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_f5600b76-1b08-404a-8e90-7f2cd620928b
GITHUB_REF=refs/heads/master
GITHUB_REF_NAME=master
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=branch
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188627423
GITHUB_RUN_NUMBER=6
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=266574110acf203503badf966df2ea24b5d732d7
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_f5600b76-1b08-404a-8e90-7f2cd620928b
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_push_master.json`
```json
{
  "after": "266574110acf203503badf966df2ea24b5d732d7",
  "base_ref": null,
  "before": "ef1a8e2e6a91ffa6837f19f7743405b709363225",
  "commits": [
    {
      "author": {
        "email": "crazy-max@users.noreply.github.com",
        "name": "CrazyMax",
        "username": "crazy-max"
      },
      "committer": {
        "email": "crazy-max@users.noreply.github.com",
        "name": "CrazyMax",
        "username": "crazy-max"
      },
      "distinct": true,
      "id": "266574110acf203503badf966df2ea24b5d732d7",
      "message": "more events",
      "timestamp": "2022-04-19T11:04:39+02:00",
      "tree_id": "03b667a843ece33c75ef5eb23ca5bc8fc3b876e4",
      "url": "https://github.com/docker/test-docker-action/commit/266574110acf203503badf966df2ea24b5d732d7"
    }
  ],
  "compare": "https://github.com/docker/test-docker-action/compare/ef1a8e2e6a91...266574110acf",
  "created": false,
  "deleted": false,
  "forced": false,
  "head_commit": {
    "author": {
      "email": "crazy-max@users.noreply.github.com",
      "name": "CrazyMax",
      "username": "crazy-max"
    },
    "committer": {
      "email": "crazy-max@users.noreply.github.com",
      "name": "CrazyMax",
      "username": "crazy-max"
    },
    "distinct": true,
    "id": "266574110acf203503badf966df2ea24b5d732d7",
    "message": "more events",
    "timestamp": "2022-04-19T11:04:39+02:00",
    "tree_id": "03b667a843ece33c75ef5eb23ca5bc8fc3b876e4",
    "url": "https://github.com/docker/test-docker-action/commit/266574110acf203503badf966df2ea24b5d732d7"
  },
  "organization": {
    "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
    "description": "Docker helps developers bring their ideas to life by conquering the complexity of app development.",
    "events_url": "https://api.github.com/orgs/docker/events",
    "hooks_url": "https://api.github.com/orgs/docker/hooks",
    "id": 5429470,
    "issues_url": "https://api.github.com/orgs/docker/issues",
    "login": "docker",
    "members_url": "https://api.github.com/orgs/docker/members{/member}",
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
    "public_members_url": "https://api.github.com/orgs/docker/public_members{/member}",
    "repos_url": "https://api.github.com/orgs/docker/repos",
    "url": "https://api.github.com/orgs/docker"
  },
  "pusher": {
    "email": "github@crazymax.dev",
    "name": "crazy-max"
  },
  "ref": "refs/heads/master",
  "repository": {
    "allow_forking": true,
    "archive_url": "https://api.github.com/repos/docker/test-docker-action/{archive_format}{/ref}",
    "archived": false,
    "assignees_url": "https://api.github.com/repos/docker/test-docker-action/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/docker/test-docker-action/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/docker/test-docker-action/branches{/branch}",
    "clone_url": "https://github.com/docker/test-docker-action.git",
    "collaborators_url": "https://api.github.com/repos/docker/test-docker-action/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/docker/test-docker-action/comments{/number}",
    "commits_url": "https://api.github.com/repos/docker/test-docker-action/commits{/sha}",
    "compare_url": "https://api.github.com/repos/docker/test-docker-action/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/docker/test-docker-action/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/docker/test-docker-action/contributors",
    "created_at": 1596792180,
    "default_branch": "master",
    "deployments_url": "https://api.github.com/repos/docker/test-docker-action/deployments",
    "description": "Test \"Docker\" Actions",
    "disabled": false,
    "downloads_url": "https://api.github.com/repos/docker/test-docker-action/downloads",
    "events_url": "https://api.github.com/repos/docker/test-docker-action/events",
    "fork": false,
    "forks": 1,
    "forks_count": 1,
    "forks_url": "https://api.github.com/repos/docker/test-docker-action/forks",
    "full_name": "docker/test-docker-action",
    "git_commits_url": "https://api.github.com/repos/docker/test-docker-action/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/docker/test-docker-action/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/docker/test-docker-action/git/tags{/sha}",
    "git_url": "git://github.com/docker/test-docker-action.git",
    "has_downloads": true,
    "has_issues": false,
    "has_pages": false,
    "has_projects": false,
    "has_wiki": false,
    "homepage": "",
    "hooks_url": "https://api.github.com/repos/docker/test-docker-action/hooks",
    "html_url": "https://github.com/docker/test-docker-action",
    "id": 285789493,
    "is_template": false,
    "issue_comment_url": "https://api.github.com/repos/docker/test-docker-action/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/docker/test-docker-action/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/docker/test-docker-action/issues{/number}",
    "keys_url": "https://api.github.com/repos/docker/test-docker-action/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/docker/test-docker-action/labels{/name}",
    "language": "JavaScript",
    "languages_url": "https://api.github.com/repos/docker/test-docker-action/languages",
    "license": {
      "key": "mit",
      "name": "MIT License",
      "node_id": "MDc6TGljZW5zZTEz",
      "spdx_id": "MIT",
      "url": "https://api.github.com/licenses/mit"
    },
    "master_branch": "master",
    "merges_url": "https://api.github.com/repos/docker/test-docker-action/merges",
    "milestones_url": "https://api.github.com/repos/docker/test-docker-action/milestones{/number}",
    "mirror_url": null,
    "name": "test-docker-action",
    "node_id": "MDEwOlJlcG9zaXRvcnkyODU3ODk0OTM=",
    "notifications_url": "https://api.github.com/repos/docker/test-docker-action/notifications{?since,all,participating}",
    "open_issues": 4,
    "open_issues_count": 4,
    "organization": "docker",
    "owner": {
      "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
      "email": "info@docker.com",
      "events_url": "https://api.github.com/users/docker/events{/privacy}",
      "followers_url": "https://api.github.com/users/docker/followers",
      "following_url": "https://api.github.com/users/docker/following{/other_user}",
      "gists_url": "https://api.github.com/users/docker/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/docker",
      "id": 5429470,
      "login": "docker",
      "name": "docker",
      "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
      "organizations_url": "https://api.github.com/users/docker/orgs",
      "received_events_url": "https://api.github.com/users/docker/received_events",
      "repos_url": "https://api.github.com/users/docker/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/docker/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/docker/subscriptions",
      "type": "Organization",
      "url": "https://api.github.com/users/docker"
    },
    "private": true,
    "pulls_url": "https://api.github.com/repos/docker/test-docker-action/pulls{/number}",
    "pushed_at": 1650359090,
    "releases_url": "https://api.github.com/repos/docker/test-docker-action/releases{/id}",
    "size": 796,
    "ssh_url": "git@github.com:docker/test-docker-action.git",
    "stargazers": 0,
    "stargazers_count": 0,
    "stargazers_url": "https://api.github.com/repos/docker/test-docker-action/stargazers",
    "statuses_url": "https://api.github.com/repos/docker/test-docker-action/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/docker/test-docker-action/subscribers",
    "subscription_url": "https://api.github.com/repos/docker/test-docker-action/subscription",
    "svn_url": "https://github.com/docker/test-docker-action",
    "tags_url": "https://api.github.com/repos/docker/test-docker-action/tags",
    "teams_url": "https://api.github.com/repos/docker/test-docker-action/teams",
    "topics": [],
    "trees_url": "https://api.github.com/repos/docker/test-docker-action/git/trees{/sha}",
    "updated_at": "2021-12-21T21:49:29Z",
    "url": "https://github.com/docker/test-docker-action",
    "visibility": "private",
    "watchers": 0,
    "watchers_count": 0
  },
  "sender": {
    "avatar_url": "https://avatars.githubusercontent.com/u/1951866?v=4",
    "events_url": "https://api.github.com/users/crazy-max/events{/privacy}",
    "followers_url": "https://api.github.com/users/crazy-max/followers",
    "following_url": "https://api.github.com/users/crazy-max/following{/other_user}",
    "gists_url": "https://api.github.com/users/crazy-max/gists{/gist_id}",
    "gravatar_id": "",
    "html_url": "https://github.com/crazy-max",
    "id": 1951866,
    "login": "crazy-max",
    "node_id": "MDQ6VXNlcjE5NTE4NjY=",
    "organizations_url": "https://api.github.com/users/crazy-max/orgs",
    "received_events_url": "https://api.github.com/users/crazy-max/received_events",
    "repos_url": "https://api.github.com/users/crazy-max/repos",
    "site_admin": false,
    "starred_url": "https://api.github.com/users/crazy-max/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/crazy-max/subscriptions",
    "type": "User",
    "url": "https://api.github.com/users/crazy-max"
  }
}
```

## File: `__tests__/fixtures/event_release_created.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_82c844c7-54b3-4b5d-a1e1-4f9f2e936d4f
GITHUB_EVENT_NAME=release
GITHUB_EVENT_PATH=./__tests__/fixtures/event_release_created.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_82c844c7-54b3-4b5d-a1e1-4f9f2e936d4f
GITHUB_REF=refs/tags/v1.1.1
GITHUB_REF_NAME=v1.1.1
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=tag
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188867972
GITHUB_RUN_NUMBER=26
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=860c1904a1ce19322e91ac35af1ab07466440c37
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_82c844c7-54b3-4b5d-a1e1-4f9f2e936d4f
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_release_created.json`
```json
{
  "action": "created",
  "organization": {
    "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
    "description": "Docker helps developers bring their ideas to life by conquering the complexity of app development.",
    "events_url": "https://api.github.com/orgs/docker/events",
    "hooks_url": "https://api.github.com/orgs/docker/hooks",
    "id": 5429470,
    "issues_url": "https://api.github.com/orgs/docker/issues",
    "login": "docker",
    "members_url": "https://api.github.com/orgs/docker/members{/member}",
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
    "public_members_url": "https://api.github.com/orgs/docker/public_members{/member}",
    "repos_url": "https://api.github.com/orgs/docker/repos",
    "url": "https://api.github.com/orgs/docker"
  },
  "release": {
    "assets": [],
    "assets_url": "https://api.github.com/repos/docker/test-docker-action/releases/64718198/assets",
    "author": {
      "avatar_url": "https://avatars.githubusercontent.com/u/1951866?v=4",
      "events_url": "https://api.github.com/users/crazy-max/events{/privacy}",
      "followers_url": "https://api.github.com/users/crazy-max/followers",
      "following_url": "https://api.github.com/users/crazy-max/following{/other_user}",
      "gists_url": "https://api.github.com/users/crazy-max/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/crazy-max",
      "id": 1951866,
      "login": "crazy-max",
      "node_id": "MDQ6VXNlcjE5NTE4NjY=",
      "organizations_url": "https://api.github.com/users/crazy-max/orgs",
      "received_events_url": "https://api.github.com/users/crazy-max/received_events",
      "repos_url": "https://api.github.com/users/crazy-max/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/crazy-max/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/crazy-max/subscriptions",
      "type": "User",
      "url": "https://api.github.com/users/crazy-max"
    },
    "body": "foo",
    "created_at": "2022-04-19T09:39:35Z",
    "draft": false,
    "html_url": "https://github.com/docker/test-docker-action/releases/tag/v1.1.1",
    "id": 64718198,
    "name": "v1.1.1",
    "node_id": "RE_kwDOEQjNNc4D24V2",
    "prerelease": true,
    "subscription_url": "https://api.github.com/repos/docker/test-docker-action/subscription",
    "svn_url": "https://github.com/docker/test-docker-action",
    "tags_url": "https://api.github.com/repos/docker/test-docker-action/tags",
    "teams_url": "https://api.github.com/repos/docker/test-docker-action/teams",
    "topics": [],
    "trees_url": "https://api.github.com/repos/docker/test-docker-action/git/trees{/sha}",
    "updated_at": "2022-04-19T09:05:09Z",
    "url": "https://api.github.com/repos/docker/test-docker-action",
    "visibility": "private",
    "watchers": 0,
    "watchers_count": 0
  },
  "sender": {
    "avatar_url": "https://avatars.githubusercontent.com/u/1951866?v=4",
    "events_url": "https://api.github.com/users/crazy-max/events{/privacy}",
    "followers_url": "https://api.github.com/users/crazy-max/followers",
    "following_url": "https://api.github.com/users/crazy-max/following{/other_user}",
    "gists_url": "https://api.github.com/users/crazy-max/gists{/gist_id}",
    "gravatar_id": "",
    "html_url": "https://github.com/crazy-max",
    "id": 1951866,
    "login": "crazy-max",
    "node_id": "MDQ6VXNlcjE5NTE4NjY=",
    "organizations_url": "https://api.github.com/users/crazy-max/orgs",
    "received_events_url": "https://api.github.com/users/crazy-max/received_events",
    "repos_url": "https://api.github.com/users/crazy-max/repos",
    "site_admin": false,
    "starred_url": "https://api.github.com/users/crazy-max/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/crazy-max/subscriptions",
    "type": "User",
    "url": "https://api.github.com/users/crazy-max"
  }
}
```

## File: `__tests__/fixtures/event_schedule.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_c8594ff3-bed7-4fb7-b495-c63872db99a2
GITHUB_EVENT_NAME=schedule
GITHUB_EVENT_PATH=./__tests__/fixtures/event_schedule.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_c8594ff3-bed7-4fb7-b495-c63872db99a2
GITHUB_REF=refs/heads/master
GITHUB_REF_NAME=master
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=branch
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188841209
GITHUB_RUN_NUMBER=24
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=860c1904a1ce19322e91ac35af1ab07466440c37
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_c8594ff3-bed7-4fb7-b495-c63872db99a2
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_schedule.json`
```json
{
  "schedule": "*/10 * * * *"
}
```

## File: `__tests__/fixtures/event_tag_1.0dev4.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_EVENT_NAME=push
#GITHUB_EVENT_PATH=./__tests__/fixtures/event_tag_1.0dev4.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_REF=refs/tags/1.0dev4
GITHUB_REF_NAME=1.0dev4
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=tag
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188815933
GITHUB_RUN_NUMBER=21
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=860c1904a1ce19322e91ac35af1ab07466440c37
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_tag_1.1beta2.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_EVENT_NAME=push
#GITHUB_EVENT_PATH=./__tests__/fixtures/event_tag_1.1beta2.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_REF=refs/tags/1.1beta2
GITHUB_REF_NAME=1.1beta2
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=tag
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188815933
GITHUB_RUN_NUMBER=21
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=860c1904a1ce19322e91ac35af1ab07466440c37
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_tag_1.2.3rc2.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_EVENT_NAME=push
#GITHUB_EVENT_PATH=./__tests__/fixtures/event_tag_1.2.3rc2.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_REF=refs/tags/1.2.3rc2
GITHUB_REF_NAME=1.2.3rc2
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=tag
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188815933
GITHUB_RUN_NUMBER=21
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=860c1904a1ce19322e91ac35af1ab07466440c37
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_tag_1.2.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_EVENT_NAME=push
#GITHUB_EVENT_PATH=./__tests__/fixtures/event_tag_1.2.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_REF=refs/tags/1.2
GITHUB_REF_NAME=1.2
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=tag
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188815933
GITHUB_RUN_NUMBER=21
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=860c1904a1ce19322e91ac35af1ab07466440c37
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_tag_1.2post1.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_EVENT_NAME=push
#GITHUB_EVENT_PATH=./__tests__/fixtures/event_tag_1.2post1.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_REF=refs/tags/1.2post1
GITHUB_REF_NAME=1.2post1
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=tag
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188815933
GITHUB_RUN_NUMBER=21
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=860c1904a1ce19322e91ac35af1ab07466440c37
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_tag_20200110-RC2.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_EVENT_NAME=push
#GITHUB_EVENT_PATH=./__tests__/fixtures/event_tag_20200110-RC2.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_REF=refs/tags/20200110-RC2
GITHUB_REF_NAME=20200110-RC2
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=tag
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188815933
GITHUB_RUN_NUMBER=21
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=860c1904a1ce19322e91ac35af1ab07466440c37
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_tag_p1-v1.0.0.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_EVENT_NAME=push
#GITHUB_EVENT_PATH=./__tests__/fixtures/event_tag_p1-v1.0.0.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_REF=refs/tags/p1/v1.0.0
GITHUB_REF_NAME=p1/v1.0.0
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=tag
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188815933
GITHUB_RUN_NUMBER=21
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=860c1904a1ce19322e91ac35af1ab07466440c37
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_tag_release1.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_EVENT_NAME=push
#GITHUB_EVENT_PATH=./__tests__/fixtures/event_tag_release1.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_REF=refs/tags/release1
GITHUB_REF_NAME=release1
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=tag
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188815933
GITHUB_RUN_NUMBER=21
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=860c1904a1ce19322e91ac35af1ab07466440c37
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_tag_sometag.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_EVENT_NAME=push
#GITHUB_EVENT_PATH=./__tests__/fixtures/event_tag_sometag.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_REF=refs/tags/sometag
GITHUB_REF_NAME=sometag
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=tag
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188815933
GITHUB_RUN_NUMBER=21
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=860c1904a1ce19322e91ac35af1ab07466440c37
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_tag_v1.1.1.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_EVENT_NAME=push
GITHUB_EVENT_PATH=./__tests__/fixtures/event_tag_v1.1.1.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_REF=refs/tags/v1.1.1
GITHUB_REF_NAME=v1.1.1
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=tag
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188815933
GITHUB_RUN_NUMBER=21
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=860c1904a1ce19322e91ac35af1ab07466440c37
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_tag_v1.1.1.json`
```json
{
  "after": "860c1904a1ce19322e91ac35af1ab07466440c37",
  "base_ref": "refs/heads/master",
  "before": "0000000000000000000000000000000000000000",
  "commits": [],
  "compare": "https://github.com/docker/test-docker-action/compare/v1.1.1",
  "created": true,
  "deleted": false,
  "forced": false,
  "head_commit": {
    "author": {
      "email": "crazy-max@users.noreply.github.com",
      "name": "CrazyMax",
      "username": "crazy-max"
    },
    "committer": {
      "email": "crazy-max@users.noreply.github.com",
      "name": "CrazyMax",
      "username": "crazy-max"
    },
    "distinct": true,
    "id": "860c1904a1ce19322e91ac35af1ab07466440c37",
    "message": "scheduled",
    "timestamp": "2022-04-19T11:39:35+02:00",
    "tree_id": "1d3608c3f204a4d754a1db925264929afd54daad",
    "url": "https://github.com/docker/test-docker-action/commit/860c1904a1ce19322e91ac35af1ab07466440c37"
  },
  "organization": {
    "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
    "description": "Docker helps developers bring their ideas to life by conquering the complexity of app development.",
    "events_url": "https://api.github.com/orgs/docker/events",
    "hooks_url": "https://api.github.com/orgs/docker/hooks",
    "id": 5429470,
    "issues_url": "https://api.github.com/orgs/docker/issues",
    "login": "docker",
    "members_url": "https://api.github.com/orgs/docker/members{/member}",
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
    "public_members_url": "https://api.github.com/orgs/docker/public_members{/member}",
    "repos_url": "https://api.github.com/orgs/docker/repos",
    "url": "https://api.github.com/orgs/docker"
  },
  "pusher": {
    "email": "github@crazymax.dev",
    "name": "crazy-max"
  },
  "ref": "refs/tags/v1.1.1",
  "repository": {
    "allow_forking": true,
    "archive_url": "https://api.github.com/repos/docker/test-docker-action/{archive_format}{/ref}",
    "archived": false,
    "assignees_url": "https://api.github.com/repos/docker/test-docker-action/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/docker/test-docker-action/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/docker/test-docker-action/branches{/branch}",
    "clone_url": "https://github.com/docker/test-docker-action.git",
    "collaborators_url": "https://api.github.com/repos/docker/test-docker-action/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/docker/test-docker-action/comments{/number}",
    "commits_url": "https://api.github.com/repos/docker/test-docker-action/commits{/sha}",
    "compare_url": "https://api.github.com/repos/docker/test-docker-action/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/docker/test-docker-action/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/docker/test-docker-action/contributors",
    "created_at": 1596792180,
    "default_branch": "master",
    "deployments_url": "https://api.github.com/repos/docker/test-docker-action/deployments",
    "description": "Test \"Docker\" Actions",
    "disabled": false,
    "downloads_url": "https://api.github.com/repos/docker/test-docker-action/downloads",
    "events_url": "https://api.github.com/repos/docker/test-docker-action/events",
    "fork": false,
    "forks": 1,
    "forks_count": 1,
    "forks_url": "https://api.github.com/repos/docker/test-docker-action/forks",
    "full_name": "docker/test-docker-action",
    "git_commits_url": "https://api.github.com/repos/docker/test-docker-action/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/docker/test-docker-action/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/docker/test-docker-action/git/tags{/sha}",
    "git_url": "git://github.com/docker/test-docker-action.git",
    "has_downloads": true,
    "has_issues": true,
    "has_pages": false,
    "has_projects": true,
    "has_wiki": true,
    "homepage": "",
    "hooks_url": "https://api.github.com/repos/docker/test-docker-action/hooks",
    "html_url": "https://github.com/docker/test-docker-action",
    "id": 285789493,
    "is_template": false,
    "issue_comment_url": "https://api.github.com/repos/docker/test-docker-action/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/docker/test-docker-action/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/docker/test-docker-action/issues{/number}",
    "keys_url": "https://api.github.com/repos/docker/test-docker-action/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/docker/test-docker-action/labels{/name}",
    "language": "JavaScript",
    "languages_url": "https://api.github.com/repos/docker/test-docker-action/languages",
    "license": {
      "key": "mit",
      "name": "MIT License",
      "node_id": "MDc6TGljZW5zZTEz",
      "spdx_id": "MIT",
      "url": "https://api.github.com/licenses/mit"
    },
    "master_branch": "master",
    "merges_url": "https://api.github.com/repos/docker/test-docker-action/merges",
    "milestones_url": "https://api.github.com/repos/docker/test-docker-action/milestones{/number}",
    "mirror_url": null,
    "name": "test-docker-action",
    "node_id": "MDEwOlJlcG9zaXRvcnkyODU3ODk0OTM=",
    "notifications_url": "https://api.github.com/repos/docker/test-docker-action/notifications{?since,all,participating}",
    "open_issues": 6,
    "open_issues_count": 6,
    "organization": "docker",
    "owner": {
      "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
      "email": "info@docker.com",
      "events_url": "https://api.github.com/users/docker/events{/privacy}",
      "followers_url": "https://api.github.com/users/docker/followers",
      "following_url": "https://api.github.com/users/docker/following{/other_user}",
      "gists_url": "https://api.github.com/users/docker/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/docker",
      "id": 5429470,
      "login": "docker",
      "name": "docker",
      "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
      "organizations_url": "https://api.github.com/users/docker/orgs",
      "received_events_url": "https://api.github.com/users/docker/received_events",
      "repos_url": "https://api.github.com/users/docker/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/docker/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/docker/subscriptions",
      "type": "Organization",
      "url": "https://api.github.com/users/docker"
    },
    "private": true,
    "pulls_url": "https://api.github.com/repos/docker/test-docker-action/pulls{/number}",
    "pushed_at": 1650361263,
    "releases_url": "https://api.github.com/repos/docker/test-docker-action/releases{/id}",
    "size": 796,
    "ssh_url": "git@github.com:docker/test-docker-action.git",
    "stargazers": 0,
    "stargazers_count": 0,
    "stargazers_url": "https://api.github.com/repos/docker/test-docker-action/stargazers",
    "statuses_url": "https://api.github.com/repos/docker/test-docker-action/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/docker/test-docker-action/subscribers",
    "subscription_url": "https://api.github.com/repos/docker/test-docker-action/subscription",
    "svn_url": "https://github.com/docker/test-docker-action",
    "tags_url": "https://api.github.com/repos/docker/test-docker-action/tags",
    "teams_url": "https://api.github.com/repos/docker/test-docker-action/teams",
    "topics": [],
    "trees_url": "https://api.github.com/repos/docker/test-docker-action/git/trees{/sha}",
    "updated_at": "2022-04-19T09:05:09Z",
    "url": "https://github.com/docker/test-docker-action",
    "visibility": "private",
    "watchers": 0,
    "watchers_count": 0
  },
  "sender": {
    "avatar_url": "https://avatars.githubusercontent.com/u/1951866?v=4",
    "events_url": "https://api.github.com/users/crazy-max/events{/privacy}",
    "followers_url": "https://api.github.com/users/crazy-max/followers",
    "following_url": "https://api.github.com/users/crazy-max/following{/other_user}",
    "gists_url": "https://api.github.com/users/crazy-max/gists{/gist_id}",
    "gravatar_id": "",
    "html_url": "https://github.com/crazy-max",
    "id": 1951866,
    "login": "crazy-max",
    "node_id": "MDQ6VXNlcjE5NTE4NjY=",
    "organizations_url": "https://api.github.com/users/crazy-max/orgs",
    "received_events_url": "https://api.github.com/users/crazy-max/received_events",
    "repos_url": "https://api.github.com/users/crazy-max/repos",
    "site_admin": false,
    "starred_url": "https://api.github.com/users/crazy-max/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/crazy-max/subscriptions",
    "type": "User",
    "url": "https://api.github.com/users/crazy-max"
  }
}
```

## File: `__tests__/fixtures/event_tag_v1.2.3rc2.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_EVENT_NAME=push
#GITHUB_EVENT_PATH=./__tests__/fixtures/event_tag_v1.2.3rc2.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_REF=refs/tags/v1.2.3rc2
GITHUB_REF_NAME=v1.2.3rc2
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=tag
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188815933
GITHUB_RUN_NUMBER=21
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=860c1904a1ce19322e91ac35af1ab07466440c37
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_tag_v2.0.8-beta.67.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_EVENT_NAME=push
#GITHUB_EVENT_PATH=./__tests__/fixtures/event_tag_v2.0.8-beta.67.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_REF=refs/tags/v2.0.8-beta.67
GITHUB_REF_NAME=v2.0.8-beta.67
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=tag
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188815933
GITHUB_RUN_NUMBER=21
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=860c1904a1ce19322e91ac35af1ab07466440c37
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_7703d3cb-84db-438f-9f97-46e159388a55
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_workflow_dispatch.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_397d8f76-d5a2-478b-94ec-cadbffd1c08e
GITHUB_EVENT_NAME=workflow_dispatch
GITHUB_EVENT_PATH=./__tests__/fixtures/event_workflow_dispatch.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_397d8f76-d5a2-478b-94ec-cadbffd1c08e
GITHUB_REF=refs/heads/master
GITHUB_REF_NAME=master
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=branch
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188839914
GITHUB_RUN_NUMBER=23
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=860c1904a1ce19322e91ac35af1ab07466440c37
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_397d8f76-d5a2-478b-94ec-cadbffd1c08e
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_workflow_dispatch.json`
```json
{
  "inputs": {
    "logLevel": "warning"
  },
  "organization": {
    "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
    "description": "Docker helps developers bring their ideas to life by conquering the complexity of app development.",
    "events_url": "https://api.github.com/orgs/docker/events",
    "hooks_url": "https://api.github.com/orgs/docker/hooks",
    "id": 5429470,
    "issues_url": "https://api.github.com/orgs/docker/issues",
    "login": "docker",
    "members_url": "https://api.github.com/orgs/docker/members{/member}",
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
    "public_members_url": "https://api.github.com/orgs/docker/public_members{/member}",
    "repos_url": "https://api.github.com/orgs/docker/repos",
    "url": "https://api.github.com/orgs/docker"
  },
  "ref": "refs/heads/master",
  "repository": {
    "allow_forking": true,
    "archive_url": "https://api.github.com/repos/docker/test-docker-action/{archive_format}{/ref}",
    "archived": false,
    "assignees_url": "https://api.github.com/repos/docker/test-docker-action/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/docker/test-docker-action/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/docker/test-docker-action/branches{/branch}",
    "clone_url": "https://github.com/docker/test-docker-action.git",
    "collaborators_url": "https://api.github.com/repos/docker/test-docker-action/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/docker/test-docker-action/comments{/number}",
    "commits_url": "https://api.github.com/repos/docker/test-docker-action/commits{/sha}",
    "compare_url": "https://api.github.com/repos/docker/test-docker-action/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/docker/test-docker-action/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/docker/test-docker-action/contributors",
    "created_at": "2020-08-07T09:23:00Z",
    "default_branch": "master",
    "deployments_url": "https://api.github.com/repos/docker/test-docker-action/deployments",
    "description": "Test \"Docker\" Actions",
    "disabled": false,
    "downloads_url": "https://api.github.com/repos/docker/test-docker-action/downloads",
    "events_url": "https://api.github.com/repos/docker/test-docker-action/events",
    "fork": false,
    "forks": 1,
    "forks_count": 1,
    "forks_url": "https://api.github.com/repos/docker/test-docker-action/forks",
    "full_name": "docker/test-docker-action",
    "git_commits_url": "https://api.github.com/repos/docker/test-docker-action/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/docker/test-docker-action/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/docker/test-docker-action/git/tags{/sha}",
    "git_url": "git://github.com/docker/test-docker-action.git",
    "has_downloads": true,
    "has_issues": true,
    "has_pages": false,
    "has_projects": true,
    "has_wiki": true,
    "homepage": "",
    "hooks_url": "https://api.github.com/repos/docker/test-docker-action/hooks",
    "html_url": "https://github.com/docker/test-docker-action",
    "id": 285789493,
    "is_template": false,
    "issue_comment_url": "https://api.github.com/repos/docker/test-docker-action/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/docker/test-docker-action/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/docker/test-docker-action/issues{/number}",
    "keys_url": "https://api.github.com/repos/docker/test-docker-action/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/docker/test-docker-action/labels{/name}",
    "language": "JavaScript",
    "languages_url": "https://api.github.com/repos/docker/test-docker-action/languages",
    "license": {
      "key": "mit",
      "name": "MIT License",
      "node_id": "MDc6TGljZW5zZTEz",
      "spdx_id": "MIT",
      "url": "https://api.github.com/licenses/mit"
    },
    "merges_url": "https://api.github.com/repos/docker/test-docker-action/merges",
    "milestones_url": "https://api.github.com/repos/docker/test-docker-action/milestones{/number}",
    "mirror_url": null,
    "name": "test-docker-action",
    "node_id": "MDEwOlJlcG9zaXRvcnkyODU3ODk0OTM=",
    "notifications_url": "https://api.github.com/repos/docker/test-docker-action/notifications{?since,all,participating}",
    "open_issues": 6,
    "open_issues_count": 6,
    "owner": {
      "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
      "events_url": "https://api.github.com/users/docker/events{/privacy}",
      "followers_url": "https://api.github.com/users/docker/followers",
      "following_url": "https://api.github.com/users/docker/following{/other_user}",
      "gists_url": "https://api.github.com/users/docker/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/docker",
      "id": 5429470,
      "login": "docker",
      "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
      "organizations_url": "https://api.github.com/users/docker/orgs",
      "received_events_url": "https://api.github.com/users/docker/received_events",
      "repos_url": "https://api.github.com/users/docker/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/docker/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/docker/subscriptions",
      "type": "Organization",
      "url": "https://api.github.com/users/docker"
    },
    "private": true,
    "pulls_url": "https://api.github.com/repos/docker/test-docker-action/pulls{/number}",
    "pushed_at": "2022-04-19T09:41:03Z",
    "releases_url": "https://api.github.com/repos/docker/test-docker-action/releases{/id}",
    "size": 796,
    "ssh_url": "git@github.com:docker/test-docker-action.git",
    "stargazers_count": 0,
    "stargazers_url": "https://api.github.com/repos/docker/test-docker-action/stargazers",
    "statuses_url": "https://api.github.com/repos/docker/test-docker-action/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/docker/test-docker-action/subscribers",
    "subscription_url": "https://api.github.com/repos/docker/test-docker-action/subscription",
    "svn_url": "https://github.com/docker/test-docker-action",
    "tags_url": "https://api.github.com/repos/docker/test-docker-action/tags",
    "teams_url": "https://api.github.com/repos/docker/test-docker-action/teams",
    "topics": [],
    "trees_url": "https://api.github.com/repos/docker/test-docker-action/git/trees{/sha}",
    "updated_at": "2022-04-19T09:05:09Z",
    "url": "https://api.github.com/repos/docker/test-docker-action",
    "visibility": "private",
    "watchers": 0,
    "watchers_count": 0
  },
  "sender": {
    "avatar_url": "https://avatars.githubusercontent.com/u/1951866?v=4",
    "events_url": "https://api.github.com/users/crazy-max/events{/privacy}",
    "followers_url": "https://api.github.com/users/crazy-max/followers",
    "following_url": "https://api.github.com/users/crazy-max/following{/other_user}",
    "gists_url": "https://api.github.com/users/crazy-max/gists{/gist_id}",
    "gravatar_id": "",
    "html_url": "https://github.com/crazy-max",
    "id": 1951866,
    "login": "crazy-max",
    "node_id": "MDQ6VXNlcjE5NTE4NjY=",
    "organizations_url": "https://api.github.com/users/crazy-max/orgs",
    "received_events_url": "https://api.github.com/users/crazy-max/received_events",
    "repos_url": "https://api.github.com/users/crazy-max/repos",
    "site_admin": false,
    "starred_url": "https://api.github.com/users/crazy-max/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/crazy-max/subscriptions",
    "type": "User",
    "url": "https://api.github.com/users/crazy-max"
  },
  "workflow": ".github/workflows/metadata.yml"
}
```

## File: `__tests__/fixtures/event_workflow_dispatch_dev.env`
```
GITHUB_ACTION=__crazy-max_ghaction-dump-context
GITHUB_ACTIONS=true
GITHUB_ACTION_PATH=/home/runner/work/_actions/crazy-max/ghaction-dump-context/v1
GITHUB_ACTION_REF=
GITHUB_ACTION_REPOSITORY=
GITHUB_ACTOR=crazy-max
GITHUB_API_URL=https://api.github.com
GITHUB_BASE_REF=
GITHUB_ENV=/home/runner/work/_temp/_runner_file_commands/set_env_81f7da89-3d0b-493a-af1f-c67e5f779727
GITHUB_EVENT_NAME=workflow_dispatch
GITHUB_EVENT_PATH=./__tests__/fixtures/event_workflow_dispatch_dev.json
GITHUB_GRAPHQL_URL=https://api.github.com/graphql
GITHUB_HEAD_REF=
GITHUB_JOB=test
GITHUB_PATH=/home/runner/work/_temp/_runner_file_commands/add_path_81f7da89-3d0b-493a-af1f-c67e5f779727
GITHUB_REF=refs/heads/dev
GITHUB_REF_NAME=dev
GITHUB_REF_PROTECTED=false
GITHUB_REF_TYPE=branch
GITHUB_REPOSITORY=docker/test-docker-action
GITHUB_REPOSITORY_OWNER=docker
GITHUB_RETENTION_DAYS=90
GITHUB_RUN_ATTEMPT=1
GITHUB_RUN_ID=2188848679
GITHUB_RUN_NUMBER=25
GITHUB_SERVER_URL=https://github.com
GITHUB_SHA=860c1904a1ce19322e91ac35af1ab07466440c37
GITHUB_STEP_SUMMARY=/home/runner/work/_temp/_runner_file_commands/step_summary_81f7da89-3d0b-493a-af1f-c67e5f779727
GITHUB_WORKFLOW=metadata
GITHUB_WORKSPACE=/home/runner/work/test-docker-action/test-docker-action
```

## File: `__tests__/fixtures/event_workflow_dispatch_dev.json`
```json
{
  "inputs": {
    "logLevel": "warning"
  },
  "organization": {
    "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
    "description": "Docker helps developers bring their ideas to life by conquering the complexity of app development.",
    "events_url": "https://api.github.com/orgs/docker/events",
    "hooks_url": "https://api.github.com/orgs/docker/hooks",
    "id": 5429470,
    "issues_url": "https://api.github.com/orgs/docker/issues",
    "login": "docker",
    "members_url": "https://api.github.com/orgs/docker/members{/member}",
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
    "public_members_url": "https://api.github.com/orgs/docker/public_members{/member}",
    "repos_url": "https://api.github.com/orgs/docker/repos",
    "url": "https://api.github.com/orgs/docker"
  },
  "ref": "refs/heads/dev",
  "repository": {
    "allow_forking": true,
    "archive_url": "https://api.github.com/repos/docker/test-docker-action/{archive_format}{/ref}",
    "archived": false,
    "assignees_url": "https://api.github.com/repos/docker/test-docker-action/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/docker/test-docker-action/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/docker/test-docker-action/branches{/branch}",
    "clone_url": "https://github.com/docker/test-docker-action.git",
    "collaborators_url": "https://api.github.com/repos/docker/test-docker-action/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/docker/test-docker-action/comments{/number}",
    "commits_url": "https://api.github.com/repos/docker/test-docker-action/commits{/sha}",
    "compare_url": "https://api.github.com/repos/docker/test-docker-action/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/docker/test-docker-action/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/docker/test-docker-action/contributors",
    "created_at": "2020-08-07T09:23:00Z",
    "default_branch": "master",
    "deployments_url": "https://api.github.com/repos/docker/test-docker-action/deployments",
    "description": "Test \"Docker\" Actions",
    "disabled": false,
    "downloads_url": "https://api.github.com/repos/docker/test-docker-action/downloads",
    "events_url": "https://api.github.com/repos/docker/test-docker-action/events",
    "fork": false,
    "forks": 1,
    "forks_count": 1,
    "forks_url": "https://api.github.com/repos/docker/test-docker-action/forks",
    "full_name": "docker/test-docker-action",
    "git_commits_url": "https://api.github.com/repos/docker/test-docker-action/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/docker/test-docker-action/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/docker/test-docker-action/git/tags{/sha}",
    "git_url": "git://github.com/docker/test-docker-action.git",
    "has_downloads": true,
    "has_issues": true,
    "has_pages": false,
    "has_projects": true,
    "has_wiki": true,
    "homepage": "",
    "hooks_url": "https://api.github.com/repos/docker/test-docker-action/hooks",
    "html_url": "https://github.com/docker/test-docker-action",
    "id": 285789493,
    "is_template": false,
    "issue_comment_url": "https://api.github.com/repos/docker/test-docker-action/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/docker/test-docker-action/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/docker/test-docker-action/issues{/number}",
    "keys_url": "https://api.github.com/repos/docker/test-docker-action/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/docker/test-docker-action/labels{/name}",
    "language": "JavaScript",
    "languages_url": "https://api.github.com/repos/docker/test-docker-action/languages",
    "license": {
      "key": "mit",
      "name": "MIT License",
      "node_id": "MDc6TGljZW5zZTEz",
      "spdx_id": "MIT",
      "url": "https://api.github.com/licenses/mit"
    },
    "merges_url": "https://api.github.com/repos/docker/test-docker-action/merges",
    "milestones_url": "https://api.github.com/repos/docker/test-docker-action/milestones{/number}",
    "mirror_url": null,
    "name": "test-docker-action",
    "node_id": "MDEwOlJlcG9zaXRvcnkyODU3ODk0OTM=",
    "notifications_url": "https://api.github.com/repos/docker/test-docker-action/notifications{?since,all,participating}",
    "open_issues": 6,
    "open_issues_count": 6,
    "owner": {
      "avatar_url": "https://avatars.githubusercontent.com/u/5429470?v=4",
      "events_url": "https://api.github.com/users/docker/events{/privacy}",
      "followers_url": "https://api.github.com/users/docker/followers",
      "following_url": "https://api.github.com/users/docker/following{/other_user}",
      "gists_url": "https://api.github.com/users/docker/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/docker",
      "id": 5429470,
      "login": "docker",
      "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0Mjk0NzA=",
      "organizations_url": "https://api.github.com/users/docker/orgs",
      "received_events_url": "https://api.github.com/users/docker/received_events",
      "repos_url": "https://api.github.com/users/docker/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/docker/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/docker/subscriptions",
      "type": "Organization",
      "url": "https://api.github.com/users/docker"
    },
    "private": true,
    "pulls_url": "https://api.github.com/repos/docker/test-docker-action/pulls{/number}",
    "pushed_at": "2022-04-19T09:41:03Z",
    "releases_url": "https://api.github.com/repos/docker/test-docker-action/releases{/id}",
    "size": 796,
    "ssh_url": "git@github.com:docker/test-docker-action.git",
    "stargazers_count": 0,
    "stargazers_url": "https://api.github.com/repos/docker/test-docker-action/stargazers",
    "statuses_url": "https://api.github.com/repos/docker/test-docker-action/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/docker/test-docker-action/subscribers",
    "subscription_url": "https://api.github.com/repos/docker/test-docker-action/subscription",
    "svn_url": "https://github.com/docker/test-docker-action",
    "tags_url": "https://api.github.com/repos/docker/test-docker-action/tags",
    "teams_url": "https://api.github.com/repos/docker/test-docker-action/teams",
    "topics": [],
    "trees_url": "https://api.github.com/repos/docker/test-docker-action/git/trees{/sha}",
    "updated_at": "2022-04-19T09:05:09Z",
    "url": "https://api.github.com/repos/docker/test-docker-action",
    "visibility": "private",
    "watchers": 0,
    "watchers_count": 0
  },
  "sender": {
    "avatar_url": "https://avatars.githubusercontent.com/u/1951866?v=4",
    "events_url": "https://api.github.com/users/crazy-max/events{/privacy}",
    "followers_url": "https://api.github.com/users/crazy-max/followers",
    "following_url": "https://api.github.com/users/crazy-max/following{/other_user}",
    "gists_url": "https://api.github.com/users/crazy-max/gists{/gist_id}",
    "gravatar_id": "",
    "html_url": "https://github.com/crazy-max",
    "id": 1951866,
    "login": "crazy-max",
    "node_id": "MDQ6VXNlcjE5NTE4NjY=",
    "organizations_url": "https://api.github.com/users/crazy-max/orgs",
    "received_events_url": "https://api.github.com/users/crazy-max/received_events",
    "repos_url": "https://api.github.com/users/crazy-max/repos",
    "site_admin": false,
    "starred_url": "https://api.github.com/users/crazy-max/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/crazy-max/subscriptions",
    "type": "User",
    "url": "https://api.github.com/users/crazy-max"
  },
  "workflow": ".github/workflows/metadata.yml"
}
```

## File: `__tests__/fixtures/repo.json`
```json
{
  "id": 1296269,
  "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
  "name": "Hello-World",
  "full_name": "octocat/Hello-World",
  "owner": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
    "site_admin": false
  },
  "private": false,
  "html_url": "https://github.com/octocat/Hello-World",
  "description": "This your first repo!",
  "fork": false,
  "url": "https://api.github.com/repos/octocat/Hello-World",
  "archive_url": "http://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
  "assignees_url": "http://api.github.com/repos/octocat/Hello-World/assignees{/user}",
  "blobs_url": "http://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
  "branches_url": "http://api.github.com/repos/octocat/Hello-World/branches{/branch}",
  "collaborators_url": "http://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
  "comments_url": "http://api.github.com/repos/octocat/Hello-World/comments{/number}",
  "commits_url": "http://api.github.com/repos/octocat/Hello-World/commits{/sha}",
  "compare_url": "http://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
  "contents_url": "http://api.github.com/repos/octocat/Hello-World/contents/{+path}",
  "contributors_url": "http://api.github.com/repos/octocat/Hello-World/contributors",
  "deployments_url": "http://api.github.com/repos/octocat/Hello-World/deployments",
  "downloads_url": "http://api.github.com/repos/octocat/Hello-World/downloads",
  "events_url": "http://api.github.com/repos/octocat/Hello-World/events",
  "forks_url": "http://api.github.com/repos/octocat/Hello-World/forks",
  "git_commits_url": "http://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
  "git_refs_url": "http://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
  "git_tags_url": "http://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
  "git_url": "git:github.com/octocat/Hello-World.git",
  "issue_comment_url": "http://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
  "issue_events_url": "http://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
  "issues_url": "http://api.github.com/repos/octocat/Hello-World/issues{/number}",
  "keys_url": "http://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
  "labels_url": "http://api.github.com/repos/octocat/Hello-World/labels{/name}",
  "languages_url": "http://api.github.com/repos/octocat/Hello-World/languages",
  "merges_url": "http://api.github.com/repos/octocat/Hello-World/merges",
  "milestones_url": "http://api.github.com/repos/octocat/Hello-World/milestones{/number}",
  "notifications_url": "http://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
  "pulls_url": "http://api.github.com/repos/octocat/Hello-World/pulls{/number}",
  "releases_url": "http://api.github.com/repos/octocat/Hello-World/releases{/id}",
  "ssh_url": "git@github.com:octocat/Hello-World.git",
  "stargazers_url": "http://api.github.com/repos/octocat/Hello-World/stargazers",
  "statuses_url": "http://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
  "subscribers_url": "http://api.github.com/repos/octocat/Hello-World/subscribers",
  "subscription_url": "http://api.github.com/repos/octocat/Hello-World/subscription",
  "tags_url": "http://api.github.com/repos/octocat/Hello-World/tags",
  "teams_url": "http://api.github.com/repos/octocat/Hello-World/teams",
  "trees_url": "http://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
  "clone_url": "https://github.com/octocat/Hello-World.git",
  "mirror_url": "git:git.example.com/octocat/Hello-World",
  "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks",
  "svn_url": "https://svn.github.com/octocat/Hello-World",
  "homepage": "https://github.com",
  "language": null,
  "forks_count": 9,
  "stargazers_count": 80,
  "watchers_count": 80,
  "size": 108,
  "default_branch": "master",
  "open_issues_count": 0,
  "is_template": true,
  "topics": [
    "octocat",
    "atom",
    "electron",
    "api"
  ],
  "has_issues": true,
  "has_projects": true,
  "has_wiki": true,
  "has_pages": false,
  "has_downloads": true,
  "archived": false,
  "disabled": false,
  "visibility": "public",
  "pushed_at": "2011-01-26T19:06:43Z",
  "created_at": "2011-01-26T19:01:12Z",
  "updated_at": "2011-01-26T19:14:43Z",
  "permissions": {
    "pull": true,
    "triage": true,
    "push": false,
    "maintain": false,
    "admin": false
  },
  "allow_rebase_merge": true,
  "template_repository": null,
  "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
  "allow_squash_merge": true,
  "delete_branch_on_merge": true,
  "allow_merge_commit": true,
  "subscribers_count": 42,
  "network_count": 0,
  "license": {
    "key": "mit",
    "name": "MIT License",
    "spdx_id": "MIT",
    "url": "https://api.github.com/licenses/mit",
    "node_id": "MDc6TGljZW5zZW1pdA=="
  },
  "organization": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "Organization",
    "site_admin": false
  },
  "parent": {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World",
    "full_name": "octocat/Hello-World",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "archive_url": "http://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
    "assignees_url": "http://api.github.com/repos/octocat/Hello-World/assignees{/user}",
    "blobs_url": "http://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
    "branches_url": "http://api.github.com/repos/octocat/Hello-World/branches{/branch}",
    "collaborators_url": "http://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
    "comments_url": "http://api.github.com/repos/octocat/Hello-World/comments{/number}",
    "commits_url": "http://api.github.com/repos/octocat/Hello-World/commits{/sha}",
    "compare_url": "http://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
    "contents_url": "http://api.github.com/repos/octocat/Hello-World/contents/{+path}",
    "contributors_url": "http://api.github.com/repos/octocat/Hello-World/contributors",
    "deployments_url": "http://api.github.com/repos/octocat/Hello-World/deployments",
    "downloads_url": "http://api.github.com/repos/octocat/Hello-World/downloads",
    "events_url": "http://api.github.com/repos/octocat/Hello-World/events",
    "forks_url": "http://api.github.com/repos/octocat/Hello-World/forks",
    "git_commits_url": "http://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
    "git_refs_url": "http://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
    "git_tags_url": "http://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World.git",
    "issue_comment_url": "http://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
    "issue_events_url": "http://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
    "issues_url": "http://api.github.com/repos/octocat/Hello-World/issues{/number}",
    "keys_url": "http://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
    "labels_url": "http://api.github.com/repos/octocat/Hello-World/labels{/name}",
    "languages_url": "http://api.github.com/repos/octocat/Hello-World/languages",
    "merges_url": "http://api.github.com/repos/octocat/Hello-World/merges",
    "milestones_url": "http://api.github.com/repos/octocat/Hello-World/milestones{/number}",
    "notifications_url": "http://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
    "pulls_url": "http://api.github.com/repos/octocat/Hello-World/pulls{/number}",
    "releases_url": "http://api.github.com/repos/octocat/Hello-World/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "http://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "http://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
    "subscribers_url": "http://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "http://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "http://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "http://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "http://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World",
    "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World",
    "homepage": "https://github.com",
    "language": null,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues_count": 0,
    "is_template": true,
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "allow_rebase_merge": true,
    "template_repository": null,
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "allow_squash_merge": true,
    "delete_branch_on_merge": true,
    "allow_merge_commit": true,
    "subscribers_count": 42,
    "network_count": 0
  },
  "source": {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World",
    "full_name": "octocat/Hello-World",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "archive_url": "http://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
    "assignees_url": "http://api.github.com/repos/octocat/Hello-World/assignees{/user}",
    "blobs_url": "http://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
    "branches_url": "http://api.github.com/repos/octocat/Hello-World/branches{/branch}",
    "collaborators_url": "http://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
    "comments_url": "http://api.github.com/repos/octocat/Hello-World/comments{/number}",
    "commits_url": "http://api.github.com/repos/octocat/Hello-World/commits{/sha}",
    "compare_url": "http://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
    "contents_url": "http://api.github.com/repos/octocat/Hello-World/contents/{+path}",
    "contributors_url": "http://api.github.com/repos/octocat/Hello-World/contributors",
    "deployments_url": "http://api.github.com/repos/octocat/Hello-World/deployments",
    "downloads_url": "http://api.github.com/repos/octocat/Hello-World/downloads",
    "events_url": "http://api.github.com/repos/octocat/Hello-World/events",
    "forks_url": "http://api.github.com/repos/octocat/Hello-World/forks",
    "git_commits_url": "http://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
    "git_refs_url": "http://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
    "git_tags_url": "http://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World.git",
    "issue_comment_url": "http://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
    "issue_events_url": "http://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
    "issues_url": "http://api.github.com/repos/octocat/Hello-World/issues{/number}",
    "keys_url": "http://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
    "labels_url": "http://api.github.com/repos/octocat/Hello-World/labels{/name}",
    "languages_url": "http://api.github.com/repos/octocat/Hello-World/languages",
    "merges_url": "http://api.github.com/repos/octocat/Hello-World/merges",
    "milestones_url": "http://api.github.com/repos/octocat/Hello-World/milestones{/number}",
    "notifications_url": "http://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
    "pulls_url": "http://api.github.com/repos/octocat/Hello-World/pulls{/number}",
    "releases_url": "http://api.github.com/repos/octocat/Hello-World/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "http://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "http://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
    "subscribers_url": "http://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "http://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "http://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "http://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "http://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World",
    "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World",
    "homepage": "https://github.com",
    "language": null,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues_count": 0,
    "is_template": true,
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "allow_rebase_merge": true,
    "template_repository": null,
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "allow_squash_merge": true,
    "delete_branch_on_merge": true,
    "allow_merge_commit": true,
    "subscribers_count": 42,
    "network_count": 0
  }
}
```


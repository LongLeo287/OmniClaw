---
id: github.com-mislav-bump-homebrew-formula-action-5a0
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:27:59.775941
---

# KNOWLEDGE EXTRACT: github.com_mislav_bump-homebrew-formula-action_5a07195a
> **Extracted on:** 2026-04-01 08:15:46
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519340/github.com_mislav_bump-homebrew-formula-action_5a07195a

---

## File: `.envrc`
```
PATH_add /opt/homebrew/opt/node@24/bin
layout node
```

## File: `.gitignore`
```
node_modules/
lib/
```

## File: `LICENSE`
```
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org>
```

## File: `Makefile`
```
lib/run.js: src/*.ts
	./node_modules/.bin/tsc
```

## File: `README.md`
```markdown
A minimal GitHub action that uses the GitHub API to bump a Homebrew formula
after a new release in your repository.

Usage example:

```yml
on:
  push:
    tags: 'v*'

jobs:
  homebrew:
    name: Bump Homebrew formula
    runs-on: ubuntu-latest
    steps:
      - uses: mislav/bump-homebrew-formula-action@v4
        with:
          # By default, this will edit the `my_formula.rb` formula in
          # homebrew-core to update its "url" field to:
          # `https://github.com/OWNER/REPO/archive/refs/tags/<tag-name>.tar.gz`
          # The "sha256" formula field will get automatically recomputed.
          formula-name: my_formula
        env:
          # the personal access token should have "repo" & "workflow" scopes
          COMMITTER_TOKEN: ${{ secrets.COMMITTER_TOKEN }}
```

The `COMMITTER_TOKEN` secret is required because this action will want to write
to an external repository. You can [generate a new Personal Access Token (classic)
here](https://github.com/settings/tokens) and give it `repo` and `workflow` scopes.

## How it works

Given a Homebrew formula `Formula/my_formula.rb` in the
[homebrew-core](https://github.com/Homebrew/homebrew-core) repo:

```rb
class MyFormula < Formula
  url "https://github.com/me/myproject/archive/refs/tags/v1.2.3.tar.gz"
  sha256 "<OLDSHA>"
  # ...
end
```

After we push a `v2.0.0` git tag to a project that has this action configured,
the formula will be updated to:

```rb
class MyFormula < Formula
  url "https://github.com/me/myproject/archive/refs/tags/v2.0.0.tar.gz"
  sha256 "<NEWSHA>"
  # ...
end
```

This action can update the following Homebrew formula fields:

- `version`
- `url`
- `sha256` - for non-git `download-url` action input
- `tag` - for git-based `download-url`
- `revision` - for git-based `download-url`

## Action inputs

Formula parameters:

- `formula-name`: the name of the Homebrew formula to bump. Defaults to
  lower-cased repository name.

- `formula-path`: the relative path of the Homebrew formula file to edit within the `homebrew-tap` repository. Defaults to
  `Formula/<letter>/<formula-name>.rb` for homebrew-core formulae and `Formula/<formula-name>.rb` otherwise.

- `tag-name`: the git tag name to bump the formula to. Defaults to the
  currently pushed tag.

- `download-url`: the package download URL for the Homebrew formula.

  Defaults to `https://github.com/OWNER/REPO/archive/refs/tags/<tag-name>.tar.gz`, where `OWNER/REPO` is the repository that is running the Actions workflow.

- `download-sha256`: the SHA256 checksum of the archive at `download-url`.
  Defaults to calculating the checksum by fetching the archive at run time.

Repository parameters:

- `homebrew-tap`: the full GitHub repository name (in the `NAME/OWNER` format) where the Homebrew formula should be updated. Defaults
  to `Homebrew/homebrew-core`.

- `push-to`: a specific fork of `homebrew-tap` where the edit should be pushed to.
  Defaults to creating or reusing a personal fork of the owner of COMMITTER_TOKEN.
  (Note: avoid using an organization-owned fork, as that
  [breaks automation for `homebrew-core`](https://github.com/foxglove/mcap/issues/1063)).

- `base-branch`: the branch name in the `homebrew-tap` repository where the
  formula should be updated. Defaults to the main branch of the repository.

- `create-pullrequest`: a boolean value to either force or prohibit submitting
  a pull request to `homebrew-tap`. Defaults to false if `COMMITTER_TOKEN` has
  the privileges to directly push to `base-branch` in `homebrew-tap`.

- `create-branch`: a boolean value to either force or prohibit creating a
  branch on `homebrew-tap`. Defaults to false if `COMMITTER_TOKEN` has
  the privileges to directly push to `base-branch` in `homebrew-tap`.
  You cannot set this to `false` if `create-pullrequest` is set to `true`.

- `commit-message`: the git commit message template to use when updating the
  formula. The following placeholders be expanded:

  | Placeholder       | Description                                        |
  | ----------------- | -------------------------------------------------- |
  | `{{formulaName}}` | the name of the formula supplied in `formula-name` |
  | `{{version}}`     | the version number for this release                |

  It's recommended that `commit-message` has _both subject and body_, i.e. that
  it contains a subject line followed by a blank line followed by body text.
  Otherwise, pull requests to `Homebrew/homebrew-core` might get denied by
  their automation.

  Defaults to:

  ```
  {{formulaName}} {{version}}

  Created by https://github.com/mislav/bump-homebrew-formula-action
  ```

### Environment variables

- `COMMITTER_TOKEN` (required): needs _write access_ to the repository specified
  by the `homebrew-tap` input, or enough privileges to _fork the tap repo_
  (usually `homebrew-core`) and submit a PR to it.

  Recommended "classic" token scopes: `repo` & `workflow`.

- `GITHUB_TOKEN` (optional): needs _read access_ to the contents of the
  repository that is executing this action; will be used for verifying the
  SHA256 checksum of the downloadable archive for this release. Useful only if
  the repository that runs this Action is private _and_ if `COMMITTER_TOKEN` has
  the `public_repo` scope only.

## Examples

Comprehensive usage example:

```yml
on:
  push:
    tags: 'v*'
  # Alternatively, trigger this workflow after a stable release has been published:
  #release:
  #  types: [ released ]

jobs:
  homebrew:
    name: Bump Homebrew formula
    # Skip this job in case of git pushes to prerelease tags
    if: ${{ github.event_name != 'push' || !contains(github.ref, '-') }}
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - name: Extract version
        id: extract-version
        # Strip a string prefix from the git tag name:
        run: |
          echo "tag-name=${GITHUB_REF#refs/tags/}" >> $GITHUB_OUTPUT

      - uses: mislav/bump-homebrew-formula-action@v4
        with:
          formula-name: my_formula
          formula-path: Formula/m/my_formula.rb
          homebrew-tap: Homebrew/homebrew-core
          base-branch: main
          download-url: https://example.com/packages/myformula-${{ steps.extract-version.outputs.tag-name }}.tar.gz
          commit-message: |
            {{formulaName}} {{version}}

            Created by https://github.com/mislav/bump-homebrew-formula-action
        env:
          COMMITTER_TOKEN: ${{ secrets.COMMITTER_TOKEN }}
          # GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Manual trigger

How to set up this action to be manually triggered instead of being triggered by
pushing to a git tag:

```yml
on:
  workflow_dispatch:
    inputs:
      tag-name:
        description: 'The git tag name to bump the formula to'
        required: true

jobs:
  homebrew:
    name: Bump Homebrew formula
    runs-on: ubuntu-latest
    steps:
      - uses: mislav/bump-homebrew-formula-action@v4
        with:
          formula-name: my_formula
          tag-name: ${{ github.event.inputs.tag-name }}
          download-url: https://example.com/foo/myproject-${{ github.event.inputs.tag-name }}.tar.gz
        env:
          COMMITTER_TOKEN: ${{ secrets.COMMITTER_TOKEN }}
```

You could then use GitHub CLI to [trigger that workflow](https://cli.github.com/manual/gh_workflow_run):

```sh
gh workflow -R <OWNER>/<REPO> run release.yml --ref <BRANCH> -f "tag-name=v1.2.3"
```

## Known limitations

This action is designed to be minimal, fast, and to run with very few
requirements. For example, this action does not require a working Homebrew
installation, nor cloning the Homebrew tap repository (since cloning the massive
`Homebrew/homebrew-core` repository with git can take a long time). The only
thing it does is using the GitHub API to make file edits to a Homebrew formula
and to submit those edits as a PR.

Because of said design, this action is less featured than the [official `brew
bump-formula-pr` command][1] that ships with Homebrew. Known limitations are:

- Limited support for [bumping Homebrew casks](https://github.com/mislav/bump-homebrew-formula-action/issues/42#issuecomment-1410441868)

- Cannot bump formulae that need their versions to be [synced with other formulae](https://github.com/mislav/bump-homebrew-formula-action/issues/44)

- Cannot bump formulae which use Ruby `if...else` conditions to determine [alternate download locations](https://github.com/mislav/bump-homebrew-formula-action/issues/5) at runtime

- Cannot bump Python-based formulae which [declare their PyPI dependencies](https://github.com/ansible/ansible-lint/pull/3812#issuecomment-1747105780) as additional `resource` blocks

[1]: https://docs.brew.sh/How-To-Open-a-Homebrew-Pull-Request#submit-a-new-version-of-an-existing-formula
```

## File: `action.yml`
```yaml
name: bump-homebrew-formula
description: 'Bump Homebrew formula after a new release'
author: '@mislav'
runs:
  using: node24
  main: './lib/index.js'
inputs:
  formula-name:
    description: The name of the Homebrew formula (defaults to lower-cased repository name)
  formula-path:
    description: The path to the Homebrew formula file (defaults to `Formula/<formula-name>.rb`)
  tag-name:
    description: The git tag name to bump the formula to (defaults to the currently pushed tag)
  download-url:
    description: The package download URL for the Homebrew formula (defaults to the release tarball)
  download-sha256:
    description: The SHA256 checksum of the archive at download-url (defaults to calculating it)
  homebrew-tap:
    description: The repository where the formula should be updated
    default: Homebrew/homebrew-core
  push-to:
    description: An existing fork of the homebrew-tap repository where the edit should be pushed to (defaults to creating or reusing a personal fork)
  base-branch:
    description: The branch name in the homebrew-tap repository to update the formula in
  create-pullrequest:
    description: Set to a boolean value to either force or prohibit making a pull request to homebrew-tap
  create-branch:
    description: Set to a boolean value to either force or prohibit creating a separate branch on homebrew-tap
  commit-message:
    description: The git commit message template to use when updating the formula
    default: |
      {{formulaName}} {{version}}

      Created by https://github.com/mislav/bump-homebrew-formula-action
branding:
  icon: box
  color: orange
```

## File: `eslint.config.mjs`
```
// @ts-check

import eslint from '@eslint/js'
import tseslint from 'typescript-eslint'

export default tseslint.config(
  eslint.configs.recommended,
  tseslint.configs.recommended,
  {
    ignores: ['lib/*', '.github/*'],
  }
)
```

## File: `package.json`
```json
{
  "private": true,
  "type": "module",
  "scripts": {
    "build": "rm -rf lib && ncc build src/run.ts -o lib --source-map --no-source-map-register",
    "lint": "eslint .",
    "test": "tsc --sourceMap && ava"
  },
  "dependencies": {
    "@actions/core": "^2.0.2",
    "@actions/github": "^9.0.0",
    "@octokit/core": "^7.0.6",
    "@octokit/plugin-request-log": "^6.0.0",
    "@octokit/plugin-rest-endpoint-methods": "^17.0.0"
  },
  "devDependencies": {
    "@ava/typescript": "^6.0.0",
    "@eslint/js": "^10.0.1",
    "@tsconfig/node24": "^24.0.4",
    "@types/node": "^25.0.9",
    "@vercel/ncc": "^0.38.4",
    "ava": "^6.4.1",
    "eslint": "^10.0.0",
    "typescript": "5.9.x",
    "typescript-eslint": "^8.54.0"
  },
  "prettier": {
    "trailingComma": "es5",
    "semi": false,
    "singleQuote": true
  },
  "ava": {
    "files": [
      "src/*test.ts"
    ],
    "typescript": {
      "rewritePaths": {
        "src/": "lib/"
      },
      "compile": false
    }
  }
}
```

## File: `tsconfig.json`
```json
{
  "extends": "@tsconfig/node24/tsconfig.json",
  "compilerOptions": {
    "outDir": "./lib",
    "rootDir": "./src"
  },
  "include": ["src/**/*.ts"],
  "exclude": ["node_modules"]
}
```

## File: `src/api.ts`
```typescript
import { isDebug } from '@actions/core'
import { Octokit } from '@octokit/core'
import { restEndpointMethods } from '@octokit/plugin-rest-endpoint-methods'
import { requestLog } from '@octokit/plugin-request-log'

const GitHub = Octokit.plugin(restEndpointMethods, requestLog).defaults({
  baseUrl: 'https://api.github.com',
})

export type API = InstanceType<typeof GitHub>

type fetch = (url: string, options: fetchOptions) => Promise<Response>
type fetchOptions = {
  method: string
  body: string | null
}

export default function (
  token: string,
  options?: { logRequests?: boolean; fetch?: fetch }
): API {
  return new GitHub({
    request: { fetch: options && options.fetch },
    auth: `token ${token}`,
    log: {
      info(msg: string) {
        if (options && options.logRequests === false) return
        return console.info(msg)
      },
      debug(msg: string) {
        if (!isDebug()) return
        return console.debug(msg)
      },
      warn(msg: string) {
        return console.warn(msg)
      },
      error(msg: string) {
        return console.error(msg)
      },
    },
  })
}
```

## File: `src/calculate-download-checksum-test.ts`
```typescript
import test from 'ava'
import { URL } from 'url'
import {
  parseArchiveUrl,
  parseReleaseDownloadUrl,
} from './calculate-download-checksum.js'
import stream from './calculate-download-checksum.js'
import { createServer } from 'http'
import api from './api.js'

test('calculate-download-checksum parseArchiveUrl', (t) => {
  const tests = [
    {
      url: 'https://github.com/mislav/will_paginate/archive/v3.3.1.zip',
      wants: {
        owner: 'mislav',
        repo: 'will_paginate',
        ref: 'v3.3.1',
        ext: '.zip',
      },
    },
    {
      url: 'https://github.com/cli/cli/archive/refs/tags/v2.13.0.tar.gz',
      wants: {
        owner: 'cli',
        repo: 'cli',
        ref: 'refs/tags/v2.13.0',
        ext: '.tar.gz',
      },
    },
    {
      url: 'https://github.com/john-u/smartthings-cli/archive/refs/tags/@smartthings/cli@1.0.0-beta.9.tar.gz',
      wants: {
        owner: 'john-u',
        repo: 'smartthings-cli',
        ref: 'refs/tags/@smartthings/cli@1.0.0-beta.9',
        ext: '.tar.gz',
      },
    },
  ]
  tests.forEach((tt) => {
    const archive = parseArchiveUrl(new URL(tt.url))
    if (archive == null) {
      t.fail(`did not match: ${tt.url}`)
      return
    }
    t.is(tt.wants.owner, archive.owner)
    t.is(tt.wants.repo, archive.repo)
    t.is(tt.wants.ref, archive.ref)
    t.is(tt.wants.ext, archive.ext)
  })
})

test('calculate-download-checksum parseReleaseDownloadUrl', (t) => {
  const tests = [
    {
      url: 'https://github.com/john-u/smartthings-cli/releases/download/%40smartthings%2Fcli%401.0.0-beta.9/smartthings-macos.tar.gz',
      wants: {
        owner: 'john-u',
        repo: 'smartthings-cli',
        tagname: '@smartthings/cli@1.0.0-beta.9',
        name: 'smartthings-macos.tar.gz',
      },
    },
    {
      url: 'https://github.com/john-u/smartthings-cli/releases/download/@smartthings/cli@1.0.0-beta.9/smartthings-macos.tar.gz',
      wants: {
        owner: 'john-u',
        repo: 'smartthings-cli',
        tagname: '@smartthings/cli@1.0.0-beta.9',
        name: 'smartthings-macos.tar.gz',
      },
    },
  ]
  tests.forEach((tt) => {
    const asset = parseReleaseDownloadUrl(new URL(tt.url))
    if (asset == null) {
      t.fail(`did not match: ${tt.url}`)
      return
    }
    t.is(tt.wants.owner, asset.owner)
    t.is(tt.wants.repo, asset.repo)
    t.is(tt.wants.tagname, asset.tagname)
    t.is(tt.wants.name, asset.name)
  })
})

test('calculate-download-checksum stream', async (t) => {
  const server = createServer((req, res) => {
    if (req.url == '/redirect') {
      res.writeHead(302, { location: `http://${req.headers['host']}/download` })
      res.end()
    } else if (req.url == '/download') {
      res.writeHead(200, { 'Content-Type': 'text/plain' })
      res.end('hello world')
    } else {
      res.writeHead(404)
      res.end()
    }
  })

  // start a test server on a randomly available port
  await new Promise<void>((resolve) => server.listen(0, resolve))
  const address = server.address()
  if (typeof address !== 'object' || address == null) {
    t.fail('Could not get server address')
    return
  }

  const apiClient = api('ATOKEN')
  const shasum = await stream(
    apiClient,
    `http://localhost:${address.port}/redirect`,
    'sha256'
  )
  t.is(
    shasum,
    'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9' // sha256 of 'hello world'
  )

  t.teardown(
    () =>
      new Promise<void>((resolve) => {
        server.close(() => resolve())
      })
  )
})
```

## File: `src/calculate-download-checksum.ts`
```typescript
import type { API } from './api.js'
import { debug } from '@actions/core'
import { URL } from 'url'
import { createHash } from 'crypto'
import { get as HTTP } from 'http'
import { get as HTTPS, request } from 'https'

interface Headers {
  [name: string]: string
}

function stream(
  url: URL,
  headers: Headers,
  cb: (chunk: Buffer) => void
): Promise<void> {
  return new Promise((resolve, reject): void => {
    ;(url.protocol == 'https:' ? HTTPS : HTTP)(url, { headers }, (res) => {
      if (res.statusCode && res.statusCode >= 300 && res.statusCode < 400) {
        const loc = res.headers['location']
        res.resume()
        if (loc == null) throw `HTTP ${res.statusCode} but no Location header`
        const nextURL = new URL(loc)
        log(nextURL)
        resolve(stream(nextURL, headers, cb))
        return
      } else if (res.statusCode && res.statusCode >= 400) {
        res.resume()
        throw new Error(`HTTP ${res.statusCode}`)
      }
      res.on('data', (d) => cb(d))
      res.on('end', () => resolve())
    }).on('error', (err) => reject(err))
  })
}

type authInfo = {
  token: string
}

async function resolveRedirect(
  apiClient: API,
  url: URL,
  asBinary: boolean
): Promise<URL> {
  const authInfo = (await apiClient.auth()) as authInfo
  return new Promise((resolve, reject) => {
    const req = request(
      url,
      {
        method: 'HEAD',
        headers: {
          authorization: authInfo.token ? `bearer ${authInfo.token}` : '',
          accept: asBinary ? 'application/octet-stream' : '*/*',
          'User-Agent': 'bump-homebrew-formula-action',
        },
      },
      (res) => {
        res.resume() // ensure the response body has been fully read
        if (res.statusCode == 302) {
          const loc = res.headers['location']
          if (loc != null) {
            resolve(new URL(loc))
          } else {
            reject(
              new Error(`got HTTP ${res.statusCode} but no Location header`)
            )
          }
        } else {
          reject(new Error(`unexpected HTTP ${res.statusCode} response`))
        }
      }
    )
    req.end()
  })
}

async function resolveDownload(apiClient: API, url: URL): Promise<URL> {
  if (url.hostname == 'github.com') {
    const api = apiClient.rest
    const archive = parseArchiveUrl(url)
    if (archive != null) {
      const archiveType = archive.ext == '.zip' ? 'zipball' : 'tarball'
      const endpoint = new URL(
        `https://api.github.com/repos/${archive.owner}/${archive.repo}/${archiveType}/${archive.ref}`
      )
      const loc = await resolveRedirect(apiClient, endpoint, false)
      // HACK: removing "legacy" from the codeload URL ensures that we get the
      // same archive file as web download. Otherwise, the downloaded archive
      // contains resolved commit SHA instead of the tag name in directory path.
      return new URL(loc.href.replace('/legacy.', '/'))
    }

    const download = parseReleaseDownloadUrl(url)
    if (download != null) {
      const { owner, repo } = download
      const tag = download.tagname
      const res = await api.repos.getReleaseByTag({ owner, repo, tag })
      const asset = res.data.assets.find((a) => a.name == download.name)
      if (asset == null) {
        throw new Error(
          `could not find asset '${download.name}' in '${tag}' release`
        )
      }
      return await resolveRedirect(apiClient, new URL(asset.url), true)
    }
  }
  return url
}

type archive = {
  owner: string
  repo: string
  ref: string
  ext: string
}

export function parseArchiveUrl(url: URL): archive | null {
  const match = url.pathname.match(
    /^\/([^/]+)\/([^/]+)\/archive\/(.+)(\.tar\.gz|\.zip)$/
  )
  if (match == null) {
    return null
  }
  return {
    owner: match[1],
    repo: match[2],
    ref: match[3],
    ext: match[4],
  }
}

type asset = {
  owner: string
  repo: string
  tagname: string
  name: string
}

export function parseReleaseDownloadUrl(url: URL): asset | null {
  const match = url.pathname.match(
    /^\/([^/]+)\/([^/]+)\/releases\/download\/(.+)$/
  )
  if (match == null) {
    return null
  }
  const parts = match[3].split('/')
  if (parts.length < 2) {
    return null
  }
  const name = parts.pop() || ''
  return {
    owner: match[1],
    repo: match[2],
    tagname: decodeURIComponent(parts.join('/')),
    name: name,
  }
}

function log(url: URL): void {
  const params = Array.from(url.searchParams.keys())
  const q = params.length > 0 ? `?${params.join(',')}` : ''
  debug(`GET ${url.protocol}//${url.hostname}${url.pathname}${q}`)
}

export default async function (
  api: API,
  url: string,
  algorithm: string
): Promise<string> {
  const downloadUrl = await resolveDownload(api, new URL(url))
  const requestHeaders = { accept: 'application/octet-stream' }
  const hash = createHash(algorithm)
  log(downloadUrl)
  await stream(downloadUrl, requestHeaders, (chunk) => hash.update(chunk))
  return hash.digest('hex')
}
```

## File: `src/edit-github-blob-test.ts`
```typescript
import test from 'ava'
import api from './api.js'
import editGithubBlob from './edit-github-blob.js'

type fetchOptions = {
  method: string
  body: string | null
}

function replyJSON(status: number, body: unknown): Promise<Response> {
  return Promise.resolve(
    new Response(JSON.stringify(body), {
      status,
      headers: {
        'Content-Type': 'application/json',
      },
    })
  )
}

test('edit-github-blob direct push', async (t) => {
  const stubbedFetch = function (url: string, options: fetchOptions) {
    function route(method: string, path: string): boolean {
      return (
        method.toUpperCase() === options.method.toUpperCase() &&
        `https://api.github.com/${path}` === url
      )
    }

    if (route('GET', 'repos/OWNER/REPO')) {
      return replyJSON(200, {
        default_branch: 'main',
        permissions: { push: true },
      })
    } else if (route('GET', 'repos/OWNER/REPO/branches/main')) {
      return replyJSON(200, {
        commit: { sha: 'COMMITSHA' },
        protected: false,
      })
    } else if (
      route('GET', 'repos/OWNER/REPO/contents/formula%2Ftest.rb?ref=main')
    ) {
      return replyJSON(200, {
        content: Buffer.from(`old content`).toString('base64'),
      })
    } else if (route('PUT', 'repos/OWNER/REPO/contents/formula%2Ftest.rb')) {
      const payload = JSON.parse(options.body || '')
      t.is('main', payload.branch)
      t.is('Update formula/test.rb', payload.message)
      t.is(
        'OLD CONTENT',
        Buffer.from(payload.content, 'base64').toString('utf8')
      )
      return replyJSON(200, {
        commit: { html_url: 'https://github.com/OWNER/REPO/commit/NEWSHA' },
      })
    }
    throw `not stubbed: ${options.method} ${url}`
  }

  const url = await editGithubBlob({
    apiClient: api('ATOKEN', { fetch: stubbedFetch, logRequests: false }),
    owner: 'OWNER',
    repo: 'REPO',
    filePath: 'formula/test.rb',
    replace: (oldContent) => oldContent.toUpperCase(),
  })
  t.is('https://github.com/OWNER/REPO/commit/NEWSHA', url)
})

test('edit-github-blob via pull request', async (t) => {
  let newBranchName: string
  const stubbedFetch = function (url: string, options: fetchOptions) {
    function route(method: string, path: string): boolean {
      return (
        method.toUpperCase() === options.method.toUpperCase() &&
        `https://api.github.com/${path}` === url
      )
    }

    if (route('GET', 'repos/OWNER/REPO')) {
      return replyJSON(200, {
        default_branch: 'main',
        permissions: { push: false },
      })
    } else if (route('GET', 'repos/OWNER/REPO/branches/main')) {
      return replyJSON(200, {
        commit: { sha: 'COMMITSHA' },
        protected: false,
      })
    } else if (route('POST', 'repos/OWNER/REPO/forks')) {
      return replyJSON(200, {})
    } else if (route('GET', 'user')) {
      return replyJSON(200, { login: 'FORKOWNER' })
    } else if (route('POST', 'repos/FORKOWNER/REPO/merge-upstream')) {
      const payload = JSON.parse(options.body || '')
      t.is('main', payload.branch)
      return replyJSON(409, {})
    } else if (route('POST', 'repos/FORKOWNER/REPO/git/refs')) {
      const payload = JSON.parse(options.body || '')
      t.regex(payload.ref, /^refs\/heads\/update-test\.rb-\d+$/)
      newBranchName = payload.ref.replace('refs/heads/', '')
      t.is('COMMITSHA', payload.sha)
      return replyJSON(201, {})
    } else if (
      route(
        'GET',
        `repos/FORKOWNER/REPO/contents/formula%2Ftest.rb?ref=${newBranchName}`
      )
    ) {
      return replyJSON(200, {
        content: Buffer.from(`old content`).toString('base64'),
      })
    } else if (
      route('PUT', 'repos/FORKOWNER/REPO/contents/formula%2Ftest.rb')
    ) {
      const payload = JSON.parse(options.body || '')
      t.is(newBranchName, payload.branch)
      t.is('Update formula/test.rb', payload.message)
      t.is(
        'OLD CONTENT',
        Buffer.from(payload.content, 'base64').toString('utf8')
      )
      return replyJSON(200, {
        commit: { html_url: 'https://github.com/OWNER/REPO/commit/NEWSHA' },
      })
    } else if (route('POST', 'repos/OWNER/REPO/pulls')) {
      const payload = JSON.parse(options.body || '')
      t.is('main', payload.base)
      t.is(`FORKOWNER:${newBranchName}`, payload.head)
      t.is('Update formula/test.rb', payload.title)
      t.is('', payload.body)
      return replyJSON(201, {
        html_url: 'https://github.com/OWNER/REPO/pull/123',
      })
    }
    throw `not stubbed: ${options.method} ${url}`
  }

  const url = await editGithubBlob({
    apiClient: api('ATOKEN', { fetch: stubbedFetch, logRequests: false }),
    owner: 'OWNER',
    repo: 'REPO',
    filePath: 'formula/test.rb',
    replace: (oldContent) => oldContent.toUpperCase(),
  })
  t.is('https://github.com/OWNER/REPO/pull/123', url)
})

test('edit-github-blob with pushTo a fork', async (t) => {
  let newBranchName: string
  const stubbedFetch = function (url: string, options: fetchOptions) {
    function route(method: string, path: string): boolean {
      return (
        method.toUpperCase() === options.method.toUpperCase() &&
        `https://api.github.com/${path}` === url
      )
    }

    if (route('GET', 'repos/OWNER/REPO')) {
      return replyJSON(200, {
        default_branch: 'main',
        permissions: { push: false },
      })
    } else if (route('GET', 'repos/OWNER/REPO/branches/main')) {
      return replyJSON(200, {
        commit: { sha: 'COMMITSHA' },
        protected: false,
      })
    } else if (route('POST', 'repos/FORKOWNER/REPO/merge-upstream')) {
      const payload = JSON.parse(options.body || '')
      t.is('main', payload.branch)
      return replyJSON(409, {})
    } else if (route('POST', 'repos/FORKOWNER/REPO/git/refs')) {
      const payload = JSON.parse(options.body || '')
      t.regex(payload.ref, /^refs\/heads\/update-test\.rb-\d+$/)
      newBranchName = payload.ref.replace('refs/heads/', '')
      t.is('COMMITSHA', payload.sha)
      return replyJSON(201, {})
    } else if (
      route(
        'GET',
        `repos/FORKOWNER/REPO/contents/formula%2Ftest.rb?ref=${newBranchName}`
      )
    ) {
      return replyJSON(200, {
        content: Buffer.from(`old content`).toString('base64'),
      })
    } else if (
      route('PUT', 'repos/FORKOWNER/REPO/contents/formula%2Ftest.rb')
    ) {
      const payload = JSON.parse(options.body || '')
      t.is(newBranchName, payload.branch)
      t.is('Update formula/test.rb', payload.message)
      t.is(
        'OLD CONTENT',
        Buffer.from(payload.content, 'base64').toString('utf8')
      )
      return replyJSON(200, {
        commit: { html_url: 'https://github.com/OWNER/REPO/commit/NEWSHA' },
      })
    } else if (route('POST', 'repos/OWNER/REPO/pulls')) {
      const payload = JSON.parse(options.body || '')
      t.is('main', payload.base)
      t.is(`FORKOWNER:${newBranchName}`, payload.head)
      t.is('Update formula/test.rb', payload.title)
      t.is('', payload.body)
      return replyJSON(201, {
        html_url: 'https://github.com/OWNER/REPO/pull/123',
      })
    }
    throw `not stubbed: ${options.method} ${url}`
  }

  const url = await editGithubBlob({
    apiClient: api('ATOKEN', { fetch: stubbedFetch, logRequests: false }),
    owner: 'OWNER',
    repo: 'REPO',
    pushTo: { owner: 'FORKOWNER', repo: 'REPO' },
    filePath: 'formula/test.rb',
    replace: (oldContent) => oldContent.toUpperCase(),
  })
  t.is('https://github.com/OWNER/REPO/pull/123', url)
})

test('edit-github-blob with pushTo the base repo', async (t) => {
  const stubbedFetch = function (url: string, options: fetchOptions) {
    function route(method: string, path: string): boolean {
      return (
        method.toUpperCase() === options.method.toUpperCase() &&
        `https://api.github.com/${path}` === url
      )
    }

    if (route('GET', 'repos/OWNER/REPO')) {
      return replyJSON(200, {
        default_branch: 'main',
        permissions: { push: false },
      })
    } else if (route('GET', 'repos/OWNER/REPO/branches/main')) {
      return replyJSON(200, {
        commit: { sha: 'COMMITSHA' },
        protected: false,
      })
    } else if (
      route('GET', `repos/OWNER/REPO/contents/formula%2Ftest.rb?ref=main`)
    ) {
      return replyJSON(200, {
        content: Buffer.from(`old content`).toString('base64'),
      })
    } else if (route('PUT', 'repos/OWNER/REPO/contents/formula%2Ftest.rb')) {
      const payload = JSON.parse(options.body || '')
      t.is(payload.branch, 'main')
      t.is(payload.message, 'Update formula/test.rb')
      t.is(
        Buffer.from(payload.content, 'base64').toString('utf8'),
        'OLD CONTENT'
      )
      return replyJSON(200, {
        commit: { html_url: 'https://github.com/OWNER/REPO/commit/NEWSHA' },
      })
    }
    throw `not stubbed: ${options.method} ${url}`
  }

  const url = await editGithubBlob({
    apiClient: api('ATOKEN', { fetch: stubbedFetch, logRequests: false }),
    owner: 'OWNER',
    repo: 'REPO',
    pushTo: { owner: 'OWNER', repo: 'REPO' },
    filePath: 'formula/test.rb',
    replace: (oldContent) => oldContent.toUpperCase(),
  })
  t.is(url, 'https://github.com/OWNER/REPO/commit/NEWSHA')
})

test('edit-github-blob with create-branch set to false', async (t) => {
  const stubbedFetch = function (url: string, options: fetchOptions) {
    function route(method: string, path: string): boolean {
      return (
        method.toUpperCase() === options.method.toUpperCase() &&
        `https://api.github.com/${path}` === url
      )
    }

    if (route('GET', 'repos/OWNER/REPO')) {
      return replyJSON(200, {
        default_branch: 'main',
        permissions: { push: true, admin: false },
      })
    } else if (route('GET', 'repos/OWNER/REPO/branches/main')) {
      return replyJSON(200, {
        commit: { sha: 'COMMITSHA' },
        protected: true,
      })
    } else if (
      route('GET', `repos/OWNER/REPO/contents/formula%2Ftest.rb?ref=main`)
    ) {
      return replyJSON(200, {
        content: Buffer.from(`old content`).toString('base64'),
      })
    } else if (route('PUT', 'repos/OWNER/REPO/contents/formula%2Ftest.rb')) {
      const payload = JSON.parse(options.body || '')
      t.is(payload.branch, 'main')
      t.is(payload.message, 'Update formula/test.rb')
      t.is(
        Buffer.from(payload.content, 'base64').toString('utf8'),
        'OLD CONTENT'
      )
      return replyJSON(200, {
        commit: { html_url: 'https://github.com/OWNER/REPO/commit/NEWSHA' },
      })
    }
    throw `not stubbed: ${options.method} ${url}`
  }

  const url = await editGithubBlob({
    apiClient: api('ATOKEN', { fetch: stubbedFetch, logRequests: false }),
    owner: 'OWNER',
    repo: 'REPO',
    filePath: 'formula/test.rb',
    makeBranch: false,
    replace: (oldContent) => oldContent.toUpperCase(),
  })
  t.is(url, 'https://github.com/OWNER/REPO/commit/NEWSHA')
})
```

## File: `src/edit-github-blob.ts`
```typescript
import type { API } from './api.js'
import { basename } from 'path'

// avoid importing @octokit/request-error to not have to keep it in sync in package.json
interface RequestError {
  status: number
}

async function retry<T>(
  times: number,
  delay: number,
  fn: () => Promise<T>
): Promise<T> {
  try {
    return await fn()
  } catch (err) {
    if (times > 0) {
      return new Promise((resolve): void => {
        setTimeout(() => {
          resolve(retry(times - 1, delay, fn))
        }, delay)
      })
    }
    throw err
  }
}

export type Options = {
  owner: string
  repo: string
  filePath: string
  formulaName?: string
  version?: string
  branch?: string
  apiClient: API
  replace: (oldContent: string) => string
  commitMessage?: string
  pushTo?: {
    owner: string
    repo: string
  }
  makePR?: boolean
  makeBranch?: boolean
}

export default async function (params: Options): Promise<string> {
  const baseRepo = {
    owner: params.owner,
    repo: params.repo,
  }
  let headRepo = params.pushTo == null ? baseRepo : params.pushTo
  const filePath = params.filePath
  const api = params.apiClient.rest

  const repoRes = await api.repos.get(baseRepo)
  const makeFork =
    params.pushTo == null &&
    (repoRes.data.permissions == null || !repoRes.data.permissions.push)
  const inFork =
    makeFork ||
    `${baseRepo.owner}/${baseRepo.repo}`.toLowerCase() !=
      `${headRepo.owner}/${headRepo.repo}`.toLowerCase()

  const baseBranch = params.branch ? params.branch : repoRes.data.default_branch
  let headBranch = baseBranch
  const branchRes = await api.repos.getBranch({
    ...baseRepo,
    branch: baseBranch,
  })
  const needsBranch =
    params.makeBranch == null
      ? inFork || branchRes.data.protected || params.makePR === true
      : params.makeBranch

  if (makeFork) {
    const res = await Promise.all([
      api.repos.createFork(baseRepo),
      api.users.getAuthenticated(),
    ])
    headRepo = {
      owner: res[1].data.login,
      repo: baseRepo.repo,
    }
  }

  if (needsBranch) {
    const timestamp = Math.round(Date.now() / 1000)
    headBranch = `update-${basename(filePath)}-${timestamp}`
    if (inFork) {
      try {
        await api.repos.mergeUpstream({
          ...headRepo,
          branch: repoRes.data.default_branch,
        })
      } catch (err) {
        if ((err as RequestError).status === 409) {
          // ignore
        } else {
          throw err
        }
      }
    }
    await retry(makeFork ? 6 : 0, 5000, async () => {
      await api.git.createRef({
        ...headRepo,
        ref: `refs/heads/${headBranch}`,
        sha: branchRes.data.commit.sha,
      })
    })
  }

  const fileRes = await api.repos.getContent({
    ...headRepo,
    path: filePath,
    ref: headBranch,
  })
  const fileData = fileRes.data
  if (Array.isArray(fileData)) {
    throw new Error(`expected '${filePath}' is a file, got a directory`)
  }
  const content = ('content' in fileData && fileData.content) || ''
  const contentBuf = Buffer.from(content, 'base64')

  const oldContent = contentBuf.toString('utf8')
  const newContent = params.replace(oldContent)
  if (newContent == oldContent) {
    throw new Error('no replacements ocurred')
  }

  const commitMessage = params.commitMessage
    ? params.commitMessage
    : `Update ${filePath}`
  const commitRes = await api.repos.createOrUpdateFileContents({
    ...headRepo,
    path: filePath,
    message: commitMessage,
    content: Buffer.from(newContent).toString('base64'),
    sha: fileData.sha,
    branch: headBranch,
  })

  if (needsBranch && params.makePR !== false) {
    const parts = commitMessage.split('\n\n')
    const title = parts[0]
    const body = parts.slice(1).join('\n\n')

    const prRes = await api.pulls.create({
      ...baseRepo,
      base: baseBranch,
      head: `${headRepo.owner}:${headBranch}`,
      title,
      body,
    })
    return prRes.data.html_url
  } else {
    return commitRes.data.commit.html_url || ''
  }
}
```

## File: `src/main-test.ts`
```typescript
import test from 'ava'
import api from './api.js'
import { commitForRelease, prepareEdit } from './main.js'

test('commitForRelease()', (t) => {
  t.is(
    commitForRelease('This is a fixed commit message', {
      formulaName: 'test formula',
    }),
    'This is a fixed commit message'
  )
  t.is(
    commitForRelease('chore({{formulaName}}): version {{version}}', {
      formulaName: 'test formula',
    }),
    'chore(test formula): version {{version}}'
  )
  t.is(
    commitForRelease('{formulaName} {version}', {
      formulaName: 'test formula',
      version: 'v1.2.3',
    }),
    '{formulaName} {version}'
  )
  t.is(
    commitForRelease('chore({{formulaName}}): upgrade to version {{version}}', {
      formulaName: 'test formula',
      version: 'v1.2.3',
    }),
    'chore(test formula): upgrade to version v1.2.3'
  )
  t.is(
    commitForRelease(
      '{{formulaName}} {{version}}: upgrade {{formulaName}} to version {{version}}',
      {
        formulaName: 'test formula',
        version: 'v1.2.3',
      }
    ),
    'test formula v1.2.3: upgrade test formula to version v1.2.3'
  )
  t.is(
    commitForRelease('{{constructor}}{{__proto__}}', {}),
    '{{constructor}}{{__proto__}}'
  )
  t.is(
    commitForRelease('{{version}}', { version: 'v{{version}}' }),
    'v{{version}}'
  )
})

test('prepareEdit() homebrew-core', async (t) => {
  const ctx = {
    sha: 'TAGSHA',
    ref: 'refs/tags/v1.9',
    repo: {
      owner: 'mislav',
      repo: 'bump-homebrew-formula-action',
    },
  }

  process.env['GITHUB_REPOSITORY'] = 'monalisa/hello-world'
  process.env['INPUT_HOMEBREW-TAP'] = 'Homebrew/homebrew-core'
  process.env['INPUT_COMMIT-MESSAGE'] = 'Upgrade {{formulaName}} to {{version}}'

  // FIXME: this tests results in a live HTTP request. Figure out how to stub
  // `stream()` and `resolveRedirect()` methods in calculate-download-checksum.
  const stubbedFetch = function (url: string) {
    throw url
  }
  const apiClient = api('', { fetch: stubbedFetch, logRequests: false })

  const opts = await prepareEdit(ctx, apiClient, apiClient)
  t.is(opts.owner, 'Homebrew')
  t.is(opts.repo, 'homebrew-core')
  t.is(opts.branch, '')
  t.is(opts.filePath, 'Formula/b/bump-homebrew-formula-action.rb')
  t.is(opts.commitMessage, 'Upgrade bump-homebrew-formula-action to 1.9')

  const oldFormula = `
    class MyProgram < Formula
      url "OLDURL"
      sha256 "OLDSHA"
      revision 12
      head "git://example.com/repo.git",
        revision: "GITSHA"
    end
  `
  t.is(
    `
    class MyProgram < Formula
      url "https://github.com/mislav/bump-homebrew-formula-action/archive/refs/tags/v1.9.tar.gz"
      sha256 "c036fbc44901b266f6d408d6ca36ba56f63c14cc97994a935fb9741b55edee83"
      head "git://example.com/repo.git",
        revision: "GITSHA"
    end
  `,
    opts.replace(oldFormula)
  )
})

test('prepareEdit() non-homebrew-core', async (t) => {
  const ctx = {
    sha: 'TAGSHA',
    ref: 'refs/tags/v0.8.2',
    repo: {
      owner: 'OWNER',
      repo: 'REPO',
    },
  }

  process.env['GITHUB_REPOSITORY'] = 'monalisa/hello-world'
  process.env['INPUT_HOMEBREW-TAP'] = 'myorg/homebrew-utils'
  process.env['INPUT_COMMIT-MESSAGE'] = 'Upgrade {{formulaName}} to {{version}}'
  process.env['INPUT_DOWNLOAD-SHA256'] = 'MOCK-SHA-256'

  const apiClient = api('ATOKEN', {
    fetch: function (url: string) {
      throw url
    },
    logRequests: false,
  })

  const opts = await prepareEdit(ctx, apiClient, apiClient)
  t.is(opts.owner, 'myorg')
  t.is(opts.repo, 'homebrew-utils')
  t.is(opts.branch, '')
  t.is(opts.filePath, 'Formula/repo.rb')
  t.is(opts.formulaName, 'repo')
  t.is(opts.version, '0.8.2')
  t.is(opts.commitMessage, 'Upgrade repo to 0.8.2')
})
```

## File: `src/main.ts`
```typescript
import { getInput, getBooleanInput, summary } from '@actions/core'
import type { API } from './api.js'
import editGitHubBlob from './edit-github-blob.js'
import { Options as EditOptions } from './edit-github-blob.js'
import { removeRevisionLine, replaceFields } from './replace-formula-fields.js'
import calculateDownloadChecksum from './calculate-download-checksum.js'
import { context } from '@actions/github'

function tarballForRelease(
  owner: string,
  repo: string,
  tagName: string
): string {
  return `https://github.com/${owner}/${repo}/archive/refs/tags/${tagName}.tar.gz`
}

function formulaPath(owner: string, repo: string, formulaName: string): string {
  if (
    owner.toLowerCase() == 'homebrew' &&
    repo.toLowerCase() == 'homebrew-core'
  ) {
    // respect formula sharding structure in `Homebrew/homebrew-core`
    return `Formula/${formulaName.charAt(0)}/${formulaName}.rb`
  }
  return `Formula/${formulaName}.rb`
}

export function commitForRelease(
  messageTemplate: string,
  params: { [key: string]: string } = {}
): string {
  return messageTemplate.replace(
    /\{\{(\w+)\}\}/g,
    (m: string, key: string): string => {
      if (Object.hasOwnProperty.call(params, key)) {
        return params[key]
      }
      return m
    }
  )
}

export default async function (api: (token: string) => API): Promise<void> {
  const internalToken =
    process.env.GITHUB_TOKEN || process.env.COMMITTER_TOKEN || ''
  const externalToken = process.env.COMMITTER_TOKEN || ''

  const options = await prepareEdit(
    context,
    api(internalToken),
    api(externalToken)
  )
  const createdUrl = await editGitHubBlob(options)
  console.log(createdUrl)

  if (options.formulaName && options.version) {
    summary.addRaw(`🍺 Bumped ${options.formulaName} to ${options.version} `)
    summary.addLink(createdUrl, createdUrl)
    summary.addEOL()
    summary.write()
  }
}

type Context = {
  ref: string
  sha: string
  repo: {
    owner: string
    repo: string
  }
}

export async function prepareEdit(
  ctx: Context,
  sameRepoClient: API,
  crossRepoClient: API
): Promise<EditOptions> {
  const tagName =
    getInput('tag-name') ||
    ((ref) => {
      if (!ref.startsWith('refs/tags/')) throw `invalid ref: ${ref}`
      return ref.replace('refs/tags/', '')
    })(ctx.ref)

  const [owner, repo] = getInput('homebrew-tap', { required: true }).split('/')
  let pushTo: { owner: string; repo: string } | undefined
  const pushToSpec = getInput('push-to')
  if (pushToSpec) {
    const [pushToOwner, pushToRepo] = pushToSpec.split('/')
    pushTo = { owner: pushToOwner, repo: pushToRepo }
  } else if (
    owner.toLowerCase() == context.repo.owner.toLowerCase() &&
    repo.toLowerCase() == context.repo.repo.toLowerCase()
  ) {
    // If the homebrew-tap to update is the same repository that is running the Actions workflow,
    // explicitly set the same repository as the push-to target to skip any attempt of making a
    // fork of the repository. This is because a generated GITHUB_TOKEN would still appear as it
    // doesn't have permissions to push to homebrew-tap, even though it does.
    pushTo = context.repo
  }
  const formulaName = getInput('formula-name') || ctx.repo.repo.toLowerCase()
  const branch = getInput('base-branch')
  const filePath =
    getInput('formula-path') || formulaPath(owner, repo, formulaName)
  const version = tagName.replace(/^v(\d)/, '$1')
  const downloadUrl =
    getInput('download-url') ||
    tarballForRelease(ctx.repo.owner, ctx.repo.repo, tagName)
  const messageTemplate = getInput('commit-message', { required: true })

  let makePR: boolean | undefined
  if (getInput('create-pullrequest')) {
    makePR = getBooleanInput('create-pullrequest')
  }

  let makeBranch: boolean | undefined
  if (getInput('create-branch')) {
    makeBranch = getBooleanInput('create-branch')
  }

  if (makePR === true && makeBranch === false) {
    throw new Error(
      'create-pullrequest cannot be true if create-branch is false'
    )
  }

  const replacements = new Map<string, string>()
  replacements.set('version', version)
  replacements.set('url', downloadUrl)
  if (downloadUrl.endsWith('.git')) {
    replacements.set('tag', tagName)
    replacements.set(
      'revision',
      await (async () => {
        if (ctx.ref == `refs/tags/${tagName}`) return ctx.sha
        else {
          const res = await sameRepoClient.rest.git.getRef({
            ...ctx.repo,
            ref: `tags/${tagName}`,
          })
          return res.data.object.sha
        }
      })()
    )
  } else {
    replacements.set(
      'sha256',
      getInput('download-sha256') ||
        (await calculateDownloadChecksum(sameRepoClient, downloadUrl, 'sha256'))
    )
  }

  const commitMessage = commitForRelease(messageTemplate, {
    formulaName,
    version,
  })

  return {
    apiClient: crossRepoClient,
    owner,
    repo,
    branch,
    filePath,
    formulaName,
    version,
    commitMessage,
    pushTo,
    makePR,
    makeBranch,
    replace(oldContent: string) {
      return removeRevisionLine(replaceFields(oldContent, replacements))
    },
  }
}
```

## File: `src/replace-formula-fields-test.ts`
```typescript
import test from 'ava'
import { replaceFields } from './replace-formula-fields.js'

test('replaceFields()', (t) => {
  const input = `
  url "https://github.com/old/url.git",
    tag: 'v0.9.0',
    revision => "OLDREV"
`
  const expected = `
  url "https://github.com/cli/cli.git",
    tag: 'v0.11.1',
    revision => "NEWREV"
`

  const replacements = new Map<string, string>()
  replacements.set('url', 'https://github.com/cli/cli.git')
  replacements.set('tag', 'v0.11.1')
  replacements.set('revision', 'NEWREV')

  t.is(replaceFields(input, replacements), expected)
})
```

## File: `src/replace-formula-fields.ts`
```typescript
import { compare, fromUrl } from './version.js'

export class UpgradeError extends Error {}

function assertNewer(v1: string, v2: string): void {
  const c = compare(v1, v2)
  if (c == 0) {
    throw new UpgradeError(`the formula is already at version '${v1}'`)
  } else if (c == -1) {
    throw new UpgradeError(`the formula version '${v2}' is newer than '${v1}'`)
  }
}

function escape(value: string, char: string): string {
  return value.replace(new RegExp(`\\${char}`, 'g'), `\\${char}`)
}

export function replaceFields(
  oldContent: string,
  replacements: Map<string, string>
): string {
  let newContent = oldContent
  for (const [field, value] of replacements) {
    newContent = newContent.replace(
      new RegExp(`^(\\s*)${field}((?::| *=>)? *)(['"])([^'"]+)\\3`, 'm'),
      (
        _: string,
        indent: string,
        sep: string,
        q: string,
        old: string
      ): string => {
        if (field == 'version') assertNewer(value, old)
        else if (field == 'url' && !value.endsWith('.git'))
          assertNewer(fromUrl(value), fromUrl(old))
        return `${indent}${field}${sep}${q}${escape(value, q)}${q}`
      }
    )
  }
  return newContent
}

export function removeRevisionLine(oldContent: string): string {
  return oldContent.replace(/^[ \t]*revision \d+ *\r?\n/m, '')
}
```

## File: `src/run.ts`
```typescript
import { setFailed } from '@actions/core'
import api from './api.js'
import { UpgradeError } from './replace-formula-fields.js'
import run from './main.js'

run(api).catch((error) => {
  if (error instanceof UpgradeError) {
    console.warn('Skipping: %s', error.message)
    return
  }
  setFailed(error.toString())
  if (process.env.GITHUB_ACTIONS == undefined) {
    console.error(error.stack)
  }
})
```

## File: `src/version-test.ts`
```typescript
import test from 'ava'
import { compare, fromUrl } from './version.js'

test('fromUrl()', (t) => {
  const cases = new Map<string, string>([
    [
      'https://github.com/me/myproject/archive/refs/tags/v1.2.3.tar.gz',
      'v1.2.3',
    ],
    [
      'https://github.com/me/myproject/releases/download/v1.2.3/file.tgz',
      'v1.2.3',
    ],
    ['http://myproject.net/download/v1.2.3.tgz', 'v1.2.3'],
    ['https://example.com/v1.2.3.zip', 'v1.2.3'],
    [
      'https://github.com/SmartThingsCommunity/smartthings-cli/releases/download/%40smartthings%2Fcli%401.7.0/smartthings-macos-arm64.tar.gz',
      '@smartthings/cli@1.7.0',
    ],
    [
      'https://github.com/SmartThingsCommunity/smartthings-cli/releases/download/@smartthings/cli@1.7.0/smartthings-macos-x64.tar.gz',
      '@smartthings/cli@1.7.0',
    ],
    [
      'https://github.com/orf/gping/archive/refs/tags/gping-v1.14.0.tar.gz',
      'gping-v1.14.0',
    ],
  ])
  for (const item of cases) {
    t.is(fromUrl(item[0]), item[1], item[0])
  }
})

test('compare()', (t) => {
  t.is(compare('v1.2.0', 'v1.2.1'), -1)
  t.is(compare('v1.2.0', 'v1.1.9.0'), 1)
  t.is(compare('gping-v1.13', 'gping-v1.14.0'), -1)
  t.is(compare('@smartthings/cli@1.7.0', '@smartthings/cli@1.7.0-rc2'), 1)
  t.is(compare('@smartthings/cli@1.7.0', '@smartthings/cli@1.7.0'), 0)
  t.is(compare('@smartthings/cli@1.7.0', '@smartthings/cli@1.10.0'), -1)
})
```

## File: `src/version.ts`
```typescript
import { basename } from 'path'

const RE = /([0-9]+)|([a-zA-Z]+)/g

function parse(ver: string): ReadonlyArray<string | number> {
  const parts = []
  for (const m of ver.matchAll(RE)) {
    parts.push(m[1] ? parseInt(m[1]) : m[2])
  }
  if (parts[0] == 'v') parts.shift()
  return parts
}

export function compare(v1: string, v2: string): -1 | 0 | 1 {
  const p1 = parse(v1)
  const p2 = parse(v2)
  const len = Math.min(p1.length, p2.length)
  for (let i = 0; i <= len; i++) {
    const n1 = p1[i] || 0
    const n2 = p2[i] || 0
    if (typeof n1 == typeof n2) {
      if (n1 < n2) return -1
      if (n1 > n2) return 1
    } else {
      return typeof n1 == 'string' ? -1 : 1
    }
  }
  return 0
}

const ghDownloadRE =
  /^https:\/\/github.com\/[^/]+\/[^/]+\/releases\/download\/(.+)\/[^/]+$/

export function fromUrl(url: string): string {
  const downloadMatch = url.match(ghDownloadRE)
  if (downloadMatch) {
    return decodeURIComponent(downloadMatch[1])
  }
  return basename(url).replace(/\.(tar\.gz|tgz|zip)$/, '')
}
```


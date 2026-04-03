---
id: octokit-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:14.011696
---

# KNOWLEDGE EXTRACT: octokit
> **Extracted on:** 2026-03-30 17:49:32
> **Source:** octokit

---

## File: `graphql.js.md`
```markdown
# 📦 octokit/graphql.js [🔖 PENDING/APPROVE]
🔗 https://github.com/octokit/graphql.js


## Meta
- **Stars:** ⭐ 493 | **Forks:** 🍴 90
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-17
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
GitHub GraphQL API client for browsers and Node

## README (trích đầu)
```
# graphql.js

> GitHub GraphQL API client for browsers and Node

[![@latest](https://img.shields.io/npm/v/@octokit/graphql.svg)](https://www.npmjs.com/package/@octokit/graphql)
[![Build Status](https://github.com/octokit/graphql.js/workflows/Test/badge.svg)](https://github.com/octokit/graphql.js/actions?query=workflow%3ATest+branch%3Amain)

<!-- toc -->

- [Usage](#usage)
  - [Send a simple query](#send-a-simple-query)
  - [Authentication](#authentication)
  - [Variables](#variables)
  - [Pass query together with headers and variables](#pass-query-together-with-headers-and-variables)
  - [Use with GitHub Enterprise](#use-with-github-enterprise)
  - [Use custom `@octokit/request` instance](#use-custom-octokitrequest-instance)
- [TypeScript](#typescript)
  - [Additional Types](#additional-types)
- [Errors](#errors)
- [Partial responses](#partial-responses)
- [Writing tests](#writing-tests)
- [License](#license)

<!-- tocstop -->

## Usage

<table>
<tbody valign=top align=left>
<tr><th>
Browsers
</th><td width=100%>

Load `@octokit/graphql` directly from [esm.sh](https://esm.sh)

```html
<script type="module">
  import { graphql } from "https://esm.sh/@octokit/graphql";
</script>
```

</td></tr>
<tr><th>
Node
</th><td>

Install with <code>npm install @octokit/graphql</code>

```js
import { graphql } from "@octokit/graphql";
```

</td></tr>
</tbody>
</table>

### Send a simple query

```js
const { repository } = await graphql(
  `
    {
      repository(owner: "octokit", name: "graphql.js") {
        issues(last: 3) {
          edges {
            node {
              title
            }
          }
        }
      }
    }
  `,
  {
    headers: {
      authorization: `token secret123`,
    },
  },
);
```

### Authentication

The simplest way to authenticate a request is to set the `Authorization` header, e.g. to a [personal access token](https://github.com/settings/tokens/).

```js
const graphqlWithAuth = graphql.defaults({
  headers: {
    authorization: `token secret123`,
  },
});
const { repository } = await graphqlWithAuth(`
  {
    repository(owner: "octokit", name: "graphql.js") {
      issues(last: 3) {
        edges {
          node {
            title
          }
        }
      }
    }
  }
`);
```

For more complex authentication strategies such as GitHub Apps or Basic, we recommend the according authentication library exported by [`@octokit/auth`](https://github.com/octokit/auth.js).

```js
const { createAppAuth } = await import("@octokit/auth-app");
const auth = createAppAuth({
  appId: process.env.APP_ID,
  privateKey: process.env.PRIVATE_KEY,
  installationId: 123,
});
const graphqlWithAuth = graphql.defaults({
  request: {
    hook: auth.hook,
  },
});

const { repository } = await graphqlWithAuth(
  `{
    repository(owner: "octokit", name: "graphql.js") {
      issues(last: 3) {
        edges {
          node {
            title
          }
        }
      }
    }
  }`,
);
```

### Variables

⚠️ Do not use [template literals](https:/
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `octokit.rb.md`
```markdown
# 📦 octokit/octokit.rb [🔖 PENDING/APPROVE]
🔗 https://github.com/octokit/octokit.rb
🌐 http://octokit.github.io/octokit.rb/

## Meta
- **Stars:** ⭐ 3920 | **Forks:** 🍴 1160
- **Language:** Ruby | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Ruby toolkit for the GitHub API

## README (trích đầu)
```
# Octokit

> **Note**
> We've recently renamed the `4-stable` branch to `main`. This might affect you if you're making changes to Octokit's code locally. For more details and for the steps to reconfigure your local clone for the new branch name, check out [this post](https://github.com/octokit/octokit.rb/discussions/1455).

Ruby toolkit for the GitHub API.

![logo](https://docs.github.com/assets/images/gundamcat.png)

Upgrading? Check the [Upgrade Guide](#upgrading-guide) before bumping to a new
[major version][semver].

## Table of Contents

1. [Philosophy](#philosophy)
2. [Installation](#installation)
3. [Making requests](#making-requests)
   1. [Additional Query Parameters](#additional-query-parameters)
4. [Consuming resources](#consuming-resources)
5. [Accessing HTTP responses](#accessing-http-responses)
6. [Handling errors](#handling-errors)
7. [Authentication](#authentication)
   1. [Basic Authentication](#basic-authentication)
   2. [OAuth access tokens](#oauth-access-tokens)
   3. [Two-Factor Authentication](#two-factor-authentication)
   4. [Using a .netrc file](#using-a-netrc-file)
   5. [Application authentication](#application-authentication)
   6. [GitHub App](#github-app)
8. [Default results per_page](#default-results-per_page)
9. [Pagination](#pagination)
   1. [Auto pagination](#auto-pagination)
10. [Working with GitHub Enterprise](#working-with-github-enterprise)
   1. [Interacting with the GitHub.com APIs in GitHub Enterprise](#interacting-with-the-githubcom-apis-in-github-enterprise)
   2. [Interacting with the GitHub Enterprise Admin APIs](#interacting-with-the-github-enterprise-admin-apis)
   3. [Interacting with the GHES Manage API](#interacting-with-the-ghes-manage-api)
   4. [SSL Connection Errors](#ssl-connection-errors)
11. [Configuration and defaults](#configuration-and-defaults)
    1. [Configuring module defaults](#configuring-module-defaults)
    2. [Using ENV variables](#using-env-variables)
    3. [Timeouts](#timeouts)
12. [Hypermedia agent](#hypermedia-agent)
    1. [Hypermedia in Octokit](#hypermedia-in-octokit)
    2. [URI templates](#uri-templates)
    3. [The Full Hypermedia Experience™](#the-full-hypermedia-experience)
13. [Upgrading guide](#upgrading-guide)
    1. [Upgrading from 1.x.x](#upgrading-from-1xx)
14. [Advanced usage](#advanced-usage)
    1. [Debugging](#debugging)
    2. [Caching](#caching)
15. [Hacking on Octokit.rb](#hacking-on-octokitrb)
    1. [Code of Conduct](#code-of-conduct)
    2. [Running and writing new tests](#running-and-writing-new-tests)
16. [Supported Ruby Versions](#supported-ruby-versions)
17. [Versioning](#versioning)
18. [Making Repeating Requests](#making-repeating-requests)
19. [License](#license)

## Philosophy

API wrappers [should reflect the idioms of the language in which they were
written][wrappers]. Octokit.rb wraps the [GitHub API][github-api] in a flat API
client that follows Ruby conventions and requires little knowledge of REST.
Most methods have positional argumen
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `rest.js.md`
```markdown
# 📦 octokit/rest.js [🔖 PENDING/APPROVE]
🔗 https://github.com/octokit/rest.js
🌐 https://octokit.github.io/rest.js

## Meta
- **Stars:** ⭐ 651 | **Forks:** 🍴 73
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
GitHub REST API client for JavaScript

## README (trích đầu)
```
# rest.js

> GitHub REST API client for JavaScript

[![@latest](https://img.shields.io/npm/v/@octokit/rest.svg)](https://www.npmjs.com/package/@octokit/rest)
[![Build Status](https://github.com/octokit/rest.js/workflows/Test/badge.svg)](https://github.com/octokit/rest.js/actions?query=workflow%3ATest+branch%3Amain)

## Usage

<table>
<tbody valign=top align=left>
<tr><th>
Browsers
</th><td width=100%>
Load <code>@octokit/rest</code> directly from <a href="https://esm.sh">esm.sh</a>

```html
<script type="module">
  import { Octokit } from "https://esm.sh/@octokit/rest";
</script>
```

</td></tr>
<tr><th>
Node
</th><td>

Install with <code>npm install @octokit/rest</code>

```js
import { Octokit } from "@octokit/rest";
```

</td></tr>
</tbody>
</table>

> [!IMPORTANT]
> As we use [conditional exports](https://nodejs.org/api/packages.html#conditional-exports), you will need to adapt your `tsconfig.json` by setting `"moduleResolution": "node16", "module": "node16"`.
>
> See the TypeScript docs on [package.json "exports"](https://www.typescriptlang.org/docs/handbook/modules/reference.html#packagejson-exports).<br>
> See this [helpful guide on transitioning to ESM](https://gist.github.com/sindresorhus/a39789f98801d908bbc7ff3ecc99d99c) from [@sindresorhus](https://github.com/sindresorhus)

```js
const octokit = new Octokit();

// Compare: https://docs.github.com/en/rest/reference/repos/#list-organization-repositories
octokit.rest.repos
  .listForOrg({
    org: "octokit",
    type: "public",
  })
  .then(({ data }) => {
    // handle data
  });
```

See https://octokit.github.io/rest.js for full documentation.

> [!IMPORTANT]
> As we use [conditional exports](https://nodejs.org/api/packages.html#conditional-exports), you will need to adapt your `tsconfig.json` by setting `"moduleResolution": "node16", "module": "node16"`.
>
> See the TypeScript docs on [package.json "exports"](https://www.typescriptlang.org/docs/handbook/modules/reference.html#packagejson-exports).<br>
> See this [helpful guide on transitioning to ESM](https://gist.github.com/sindresorhus/a39789f98801d908bbc7ff3ecc99d99c) from [@sindresorhus](https://github.com/sindresorhus)

## Contributing

We would love you to contribute to `@octokit/rest`, pull requests are very welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for more information.

## Credits

`@octokit/rest` was originally created as [`node-github`](https://www.npmjs.com/package/github) in 2012 by Mike de Boer from Cloud9 IDE, Inc. [The original commit](https://github.blog/2020-04-09-from-48k-lines-of-code-to-10-the-story-of-githubs-javascript-sdk/) is from 2010 which predates the npm registry.

It was adopted and renamed by GitHub in 2017. Learn more about its origin on GitHub's blog: [From 48k lines of code to 10—the story of GitHub’s JavaScript SDK](https://github.blog/2020-04-09-from-48k-lines-of-code-to-10-the-story-of-githubs-javascript-sdk/)

## LICENSE

[MIT](LICENSE)

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


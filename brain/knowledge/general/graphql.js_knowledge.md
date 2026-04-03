---
id: graphql.js-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:49.437469
---

# KNOWLEDGE EXTRACT: graphql.js
> **Extracted on:** 2026-03-30 13:24:07
> **Source:** graphql.js

---

## File: `.gitignore`
```
coverage/
node_modules/
pkg/
```

## File: `CODE_OF_CONDUCT.md`
```markdown
# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct, or to ban temporarily or permanently any contributor for other behaviors that they deem inappropriate, threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces when an individual is representing the project or its community. Examples of representing a project or community include using an official project e-mail address, posting via an official social media account, or acting as an appointed representative at an online or offline event. Representation of a project may be further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team at opensource+octokit@github.com. The project team will review and investigate all complaints, and will respond in a way that it deems appropriate to the circumstances. The project team is obligated to maintain confidentiality with regard to the reporter of an incident. Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good faith may face temporary or permanent repercussions as determined by other members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4, available at [http://contributor-covenant.org/version/1/4][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/
```

## File: `LICENSE`
```
The MIT License

Copyright (c) 2018 Octokit contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

## File: `package.json`
```json
{
  "name": "@octokit/graphql",
  "version": "0.0.0-development",
  "publishConfig": {
    "access": "public",
    "provenance": true
  },
  "type": "module",
  "description": "GitHub GraphQL API client for browsers and Node",
  "scripts": {
    "build": "node scripts/build.mjs && tsc -p tsconfig.json",
    "lint": "prettier --check {src,test}/* README.md package.json",
    "lint:fix": "prettier --write {src,test}/* README.md package.json",
    "pretest": "npm run lint -s",
    "test": "vitest run --coverage"
  },
  "repository": "github:octokit/graphql.js",
  "keywords": [
    "octokit",
    "github",
    "api",
    "graphql"
  ],
  "author": "Gregor Martynus (https://github.com/gr2m)",
  "license": "MIT",
  "dependencies": {
    "@octokit/request": "^10.0.6",
    "@octokit/types": "^16.0.0",
    "universal-user-agent": "^7.0.0"
  },
  "devDependencies": {
    "@octokit/tsconfig": "^4.0.0",
    "@types/node": "^24.0.0",
    "@vitest/coverage-v8": "^4.0.0",
    "esbuild": "^0.27.0",
    "fetch-mock": "^12.0.0",
    "prettier": "3.6.2",
    "semantic-release-plugin-update-version-in-files": "^2.0.0",
    "tinyglobby": "^0.2.15",
    "typescript": "^5.3.0",
    "vitest": "^4.0.5"
  },
  "release": {
    "branches": [
      "+([0-9]).x",
      "main",
      "next",
      {
        "name": "beta",
        "prerelease": true
      }
    ],
    "plugins": [
      "@semantic-release/commit-analyzer",
      "@semantic-release/release-notes-generator",
      "@semantic-release/github",
      [
        "@semantic-release/npm",
        {
          "pkgRoot": "./pkg"
        }
      ],
      [
        "semantic-release-plugin-update-version-in-files",
        {
          "files": [
            "pkg/dist-web/*",
            "pkg/dist-node/*",
            "pkg/*/version.*"
          ]
        }
      ]
    ]
  },
  "engines": {
    "node": ">= 20"
  }
}
```

## File: `README.md`
```markdown
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

⚠️ Do not use [template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) in the query strings as they make your code vulnerable to query injection attacks (see [#2](https://github.com/octokit/graphql.js/issues/2)). Use variables instead:

```js
const { repository } = await graphql(
  `
    query lastIssues($owner: String!, $repo: String!, $num: Int = 3) {
      repository(owner: $owner, name: $repo) {
        issues(last: $num) {
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
    owner: "octokit",
    repo: "graphql.js",
    headers: {
      authorization: `token secret123`,
    },
  },
);
```

### Pass query together with headers and variables

```js
import { graphql } from("@octokit/graphql");
const { repository } = await graphql({
  query: `query lastIssues($owner: String!, $repo: String!, $num: Int = 3) {
    repository(owner: $owner, name: $repo) {
      issues(last: $num) {
        edges {
          node {
            title
          }
        }
      }
    }
  }`,
  owner: "octokit",
  repo: "graphql.js",
  headers: {
    authorization: `token secret123`,
  },
});
```

### Use with GitHub Enterprise

```js
import { graphql } from "@octokit/graphql";
graphql = graphql.defaults({
  baseUrl: "https://github-enterprise.acme-inc.com/api",
  headers: {
    authorization: `token secret123`,
  },
});
const { repository } = await graphql(`
  {
    repository(owner: "acme-project", name: "acme-repo") {
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

### Use custom `@octokit/request` instance

```js
import { request } from "@octokit/request";
import { withCustomRequest } from "@octokit/graphql";

let requestCounter = 0;
const myRequest = request.defaults({
  headers: {
    authorization: "bearer secret123",
  },
  request: {
    hook(request, options) {
      requestCounter++;
      return request(options);
    },
  },
});
const myGraphql = withCustomRequest(myRequest);
await request("/");
await myGraphql(`
  {
    repository(owner: "acme-project", name: "acme-repo") {
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
// requestCounter is now 2
```

## TypeScript

`@octokit/graphql` is exposing proper types for its usage with TypeScript projects.

### Additional Types

Additionally, `GraphQlQueryResponseData` has been exposed to users:

```ts
import type { GraphQlQueryResponseData } from "@octokit/graphql";
```

## Errors

In case of a GraphQL error, `error.message` is set to a combined message describing all errors returned by the endpoint.
All errors can be accessed at `error.errors`. `error.request` has the request options such as query, variables and headers set for easier debugging.

```js
import { graphql, GraphqlResponseError } from "@octokit/graphql";
graphql = graphql.defaults({
  headers: {
    authorization: `token secret123`,
  },
});
const query = `{
  viewer {
    bioHtml
  }
}`;

try {
  const result = await graphql(query);
} catch (error) {
  if (error instanceof GraphqlResponseError) {
    // do something with the error, allowing you to detect a graphql response error,
    // compared to accidentally catching unrelated errors.

    // server responds with an object like the following (as an example)
    // class GraphqlResponseError {
    //  "headers": {
    //    "status": "403",
    //  },
    //  "data": null,
    //  "errors": [{
    //   "message": "Field 'bioHtml' doesn't exist on type 'User'",
    //   "locations": [{
    //    "line": 3,
    //    "column": 5
    //   }]
    //  }]
    // }

    console.log("Request failed:", error.request); // { query, variables: {}, headers: { authorization: 'token secret123' } }
    console.log(error.message); // Field 'bioHtml' doesn't exist on type 'User'
  } else {
    // handle non-GraphQL error
  }
}
```

## Partial responses

A GraphQL query may respond with partial data accompanied by errors. In this case we will throw an error but the partial data will still be accessible through `error.data`

```js
import { graphql } from "@octokit/graphql";
graphql = graphql.defaults({
  headers: {
    authorization: `token secret123`,
  },
});
const query = `{
  repository(name: "probot", owner: "probot") {
    name
    ref(qualifiedName: "master") {
      target {
        ... on Commit {
          history(first: 25, after: "invalid cursor") {
            nodes {
              message
            }
          }
        }
      }
    }
  }
}`;

try {
  const result = await graphql(query);
} catch (error) {
  // server responds with
  // {
  //   "data": {
  //     "repository": {
  //       "name": "probot",
  //       "ref": null
  //     }
  //   },
  //   "errors": [
  //     {
  //       "type": "INVALID_CURSOR_ARGUMENTS",
  //       "path": [
  //         "repository",
  //         "ref",
  //         "target",
  //         "history"
  //       ],
  //       "locations": [
  //         {
  //           "line": 7,
  //           "column": 11
  //         }
  //       ],
  //       "message": "`invalid cursor` does not appear to be a valid cursor."
  //     }
  //   ]
  // }

  console.log("Request failed:", error.request); // { query, variables: {}, headers: { authorization: 'token secret123' } }
  console.log(error.message); // `invalid cursor` does not appear to be a valid cursor.
  console.log(error.data); // { repository: { name: 'probot', ref: null } }
}
```

## Writing tests

You can pass a replacement for [the built-in fetch implementation](https://github.com/bitinn/node-fetch) as `request.fetch` option. For example, using [fetch-mock](http://www.wheresrhys.co.uk/fetch-mock/) works great to write tests

```js
import assert from "assert";
import fetchMock from "fetch-mock";

import { graphql } from "@octokit/graphql";

graphql("{ viewer { login } }", {
  headers: {
    authorization: "token secret123",
  },
  request: {
    fetch: fetchMock
      .sandbox()
      .post("https://api.github.com/graphql", (url, options) => {
        assert.strictEqual(options.headers.authorization, "token secret123");
        assert.strictEqual(
          options.body,
          '{"query":"{ viewer { login } }"}',
          "Sends correct query",
        );
        return { data: {} };
      }),
  },
});
```

## License

[MIT](LICENSE)
```

## File: `SECURITY.md`
```markdown
# Security Policy

Thanks for helping make GitHub Open Source Software safe for everyone.

GitHub takes the security of our software products and services seriously, including all of the open source code repositories managed through our GitHub organizations, such as [Octokit](https://github.com/octokit).

Even though [open source repositories are outside of the scope of our bug bounty program](https://bounty.github.com/index.html#scope) and therefore not eligible for bounty rewards, we want to make sure that your finding gets passed along to the maintainers of this project for remediation. 


## Reporting a Vulnerability

Since this source is part of [Octokit](https://github.com/octokit) (a GitHub organization) we ask that you follow the guidelines [here](https://github.com/github/.github/blob/master/SECURITY.md#reporting-security-issues) to report anything that you might've found.
```

## File: `tsconfig.json`
```json
{
  "extends": "@octokit/tsconfig",
  "compilerOptions": {
    "esModuleInterop": true,
    "declaration": true,
    "outDir": "pkg/dist-types",
    "emitDeclarationOnly": true,
    "sourceMap": true
  },
  "include": ["src/**/*"]
}
```

## File: `vite.config.js`
```javascript
import { defineConfig } from "vite";

export default defineConfig({
  test: {
    coverage: {
      include: ["src/**/*.ts"],
      reporter: ["html"],
      thresholds: {
        100: true,
      },
    },
  },
});
```

## File: `scripts/build.mjs`
```
// @ts-check
import esbuild from "esbuild";
import { copyFile, readFile, writeFile, rm } from "node:fs/promises";
import { glob } from "tinyglobby";

/**
 * @type {esbuild.BuildOptions}
 */
const sharedOptions = {
  sourcemap: "external",
  sourcesContent: true,
  minify: false,
  allowOverwrite: true,
  packages: "external",
};

async function main() {
  // Start with a clean slate
  await rm("pkg", { recursive: true, force: true });
  // Build the source code for a neutral platform as ESM
  await esbuild.build({
    entryPoints: await glob(["./src/*.ts", "./src/**/*.ts"]),
    outdir: "pkg/dist-src",
    bundle: false,
    platform: "neutral",
    format: "esm",
    ...sharedOptions,
    sourcemap: false,
  });

  // Remove the types file from the dist-src folder
  const typeFiles = await glob([
    "./pkg/dist-src/**/types.js.map",
    "./pkg/dist-src/**/types.js",
  ]);
  for (const typeFile of typeFiles) {
    await rm(typeFile);
  }

  const entryPoints = ["./pkg/dist-src/index.js"];

  await esbuild.build({
    entryPoints,
    outdir: "pkg/dist-bundle",
    bundle: true,
    platform: "neutral",
    format: "esm",
    ...sharedOptions,
  });

  // Copy the README, LICENSE to the pkg folder
  await copyFile("LICENSE", "pkg/LICENSE");
  await copyFile("README.md", "pkg/README.md");

  // Handle the package.json
  let pkg = JSON.parse((await readFile("package.json", "utf8")).toString());
  // Remove unnecessary fields from the package.json
  delete pkg.scripts;
  delete pkg.prettier;
  delete pkg.release;
  delete pkg.jest;
  await writeFile(
    "pkg/package.json",
    JSON.stringify(
      {
        ...pkg,
        files: ["dist-*/**", "bin/**"],
        types: "./dist-types/index.d.ts",
        exports: {
          ".": {
            types: "./dist-types/index.d.ts",
            import: "./dist-bundle/index.js",
            default: "./dist-bundle/index.js",
          },
          "./types": {
            types: "./dist-types/types.d.ts",
          },
        },
        sideEffects: false,
      },
      null,
      2,
    ),
  );
}
main();
```

## File: `src/error.ts`
```typescript
import type { ResponseHeaders } from "@octokit/types";
import type { GraphQlEndpointOptions, GraphQlQueryResponse } from "./types.js";

type ServerResponseData<T> = Required<GraphQlQueryResponse<T>>;

function _buildMessageForResponseErrors(
  data: ServerResponseData<unknown>,
): string {
  return (
    `Request failed due to following response errors:\n` +
    data.errors.map((e) => ` - ${e.message}`).join("\n")
  );
}

export class GraphqlResponseError<ResponseData> extends Error {
  override name = "GraphqlResponseError";

  readonly errors: GraphQlQueryResponse<never>["errors"];
  readonly data: ResponseData;

  constructor(
    readonly request: GraphQlEndpointOptions,
    readonly headers: ResponseHeaders,
    readonly response: ServerResponseData<ResponseData>,
  ) {
    super(_buildMessageForResponseErrors(response));

    // Expose the errors and response data in their shorthand properties.
    this.errors = response.errors;
    this.data = response.data;

    // Maintains proper stack trace (only available on V8)
    /* v8 ignore if -- @preserve */
    if (Error.captureStackTrace) {
      Error.captureStackTrace(this, this.constructor);
    }
  }
}
```

## File: `src/graphql.ts`
```typescript
import { request as Request } from "@octokit/request";
import type { ResponseHeaders } from "@octokit/types";
import { GraphqlResponseError } from "./error.js";
import type {
  GraphQlEndpointOptions,
  RequestParameters,
  GraphQlQueryResponse,
  GraphQlQueryResponseData,
} from "./types.js";

const NON_VARIABLE_OPTIONS = [
  "method",
  "baseUrl",
  "url",
  "headers",
  "request",
  "query",
  "mediaType",
  "operationName",
];

const FORBIDDEN_VARIABLE_OPTIONS = ["query", "method", "url"];

const GHES_V3_SUFFIX_REGEX = /\/api\/v3\/?$/;

export function graphql<ResponseData = GraphQlQueryResponseData>(
  request: typeof Request,
  query: string | RequestParameters,
  options?: RequestParameters,
): Promise<ResponseData> {
  if (options) {
    if (typeof query === "string" && "query" in options) {
      return Promise.reject(
        new Error(`[@octokit/graphql] "query" cannot be used as variable name`),
      );
    }

    for (const key in options) {
      if (!FORBIDDEN_VARIABLE_OPTIONS.includes(key)) continue;

      return Promise.reject(
        new Error(
          `[@octokit/graphql] "${key}" cannot be used as variable name`,
        ),
      );
    }
  }

  const parsedOptions =
    typeof query === "string" ? Object.assign({ query }, options) : query;

  const requestOptions = Object.keys(
    parsedOptions,
  ).reduce<GraphQlEndpointOptions>((result, key) => {
    if (NON_VARIABLE_OPTIONS.includes(key)) {
      result[key] = parsedOptions[key];
      return result;
    }

    if (!result.variables) {
      result.variables = {};
    }

    result.variables[key] = parsedOptions[key];
    return result;
  }, {} as GraphQlEndpointOptions);

  // workaround for GitHub Enterprise baseUrl set with /api/v3 suffix
  // https://github.com/octokit/auth-app.js/issues/111#issuecomment-657610451
  const baseUrl = parsedOptions.baseUrl || request.endpoint.DEFAULTS.baseUrl;
  if (GHES_V3_SUFFIX_REGEX.test(baseUrl)) {
    requestOptions.url = baseUrl.replace(GHES_V3_SUFFIX_REGEX, "/api/graphql");
  }

  return request(requestOptions).then((response) => {
    if (response.data.errors) {
      const headers: ResponseHeaders = {};
      for (const key of Object.keys(response.headers)) {
        headers[key] = response.headers[key];
      }

      throw new GraphqlResponseError(
        requestOptions,
        headers,
        response.data as Required<GraphQlQueryResponse<ResponseData>>,
      );
    }

    return response.data.data;
  });
}
```

## File: `src/index.ts`
```typescript
import { request } from "@octokit/request";
import { getUserAgent } from "universal-user-agent";

import { VERSION } from "./version.js";

import { withDefaults } from "./with-defaults.js";

export const graphql = withDefaults(request, {
  headers: {
    "user-agent": `octokit-graphql.js/${VERSION} ${getUserAgent()}`,
  },
  method: "POST",
  url: "/graphql",
});

export type { GraphQlQueryResponseData } from "./types.js";
export { GraphqlResponseError } from "./error.js";

export function withCustomRequest(customRequest: typeof request) {
  return withDefaults(customRequest, {
    method: "POST",
    url: "/graphql",
  });
}
```

## File: `src/types.ts`
```typescript
import type {
  EndpointOptions,
  RequestParameters as RequestParametersType,
  EndpointInterface,
} from "@octokit/types";

import type { graphql } from "./graphql.js";

export type GraphQlEndpointOptions = EndpointOptions & {
  variables?: { [key: string]: unknown };
};
export type RequestParameters = RequestParametersType;

export type Query = string;

export interface graphql {
  /**
   * Sends a GraphQL query request based on endpoint options
   * The GraphQL query must be specified in `options`.
   *
   * @param {object} endpoint Must set `method` and `url`. Plus URL, query or body parameters, as well as `headers`, `mediaType.{format|previews}`, `request`, or `baseUrl`.
   */
  <ResponseData>(options: RequestParameters): GraphQlResponse<ResponseData>;

  /**
   * Sends a GraphQL query request based on endpoint options
   *
   * @param {string} query GraphQL query. Example: `'query { viewer { login } }'`.
   * @param {object} [parameters] URL, query or body parameters, as well as `headers`, `mediaType.{format|previews}`, `request`, or `baseUrl`.
   */
  <ResponseData>(
    query: Query,
    parameters?: RequestParameters,
  ): GraphQlResponse<ResponseData>;

  /**
   * Returns a new `endpoint` with updated route and parameters
   */
  defaults: (newDefaults: RequestParameters) => graphql;

  /**
   * Octokit endpoint API, see {@link https://github.com/octokit/endpoint.js|@octokit/endpoint}
   */
  endpoint: EndpointInterface;
}

// export type withCustomRequest = (request: typeof Request) => graphql;

export type GraphQlResponse<ResponseData> = Promise<ResponseData>;

export type GraphQlQueryResponseData = {
  [key: string]: any;
};

export type GraphQlQueryResponse<ResponseData> = {
  data: ResponseData;
  errors?: [
    {
      // https://github.com/octokit/graphql.js/pull/314
      type: string;
      message: string;
      path: [string];
      extensions: { [key: string]: any };
      locations: [
        {
          line: number;
          column: number;
        },
      ];
    },
  ];
};
```

## File: `src/version.ts`
```typescript
export const VERSION = "0.0.0-development";
```

## File: `src/with-defaults.ts`
```typescript
import { request as Request } from "@octokit/request";
import type {
  graphql as ApiInterface,
  Query,
  RequestParameters,
} from "./types.js";
import { graphql } from "./graphql.js";

export function withDefaults(
  request: typeof Request,
  newDefaults: RequestParameters,
): ApiInterface {
  const newRequest = request.defaults(newDefaults);
  const newApi = <ResponseData>(
    query: Query | RequestParameters,
    options?: RequestParameters,
  ) => {
    return graphql<ResponseData>(newRequest, query, options);
  };

  return Object.assign(newApi, {
    defaults: withDefaults.bind(null, newRequest),
    endpoint: newRequest.endpoint,
  });
}
```

## File: `test/defaults.test.ts`
```typescript
import { describe, expect, it } from "vitest";
import fetchMock, { type CallLog } from "fetch-mock";
import { getUserAgent } from "universal-user-agent";

import { VERSION } from "../src/version";
import { graphql } from "../src";

const userAgent = `octokit-graphql.js/${VERSION} ${getUserAgent()}`;

describe("graphql.defaults()", () => {
  it("is a function", () => {
    expect(graphql.defaults).toBeInstanceOf(Function);
  });

  it("README example", () => {
    const mockData = {
      repository: {
        issues: {
          edges: [
            {
              node: {
                title: "Foo",
              },
            },
            {
              node: {
                title: "Bar",
              },
            },
            {
              node: {
                title: "Baz",
              },
            },
          ],
        },
      },
    };

    const mock = fetchMock.createInstance().post(
      "https://api.github.com/graphql",
      { data: mockData },
      {
        headers: {
          authorization: "token secret123",
        },
      },
    );

    const authenticatedGraphql = graphql.defaults({
      headers: {
        authorization: `token secret123`,
      },
      request: {
        fetch: mock.fetchHandler,
      },
    });
    return authenticatedGraphql(`{
      repository(owner:"octokit", name:"graphql.js") {
        issues(last:3) {
          edges {
            node {
              title
            }
          }
        }
      }
    }`).then((result) => {
      expect(JSON.stringify(result)).toStrictEqual(JSON.stringify(mockData));
    });
  });

  it("repeated defaults", () => {
    const mockData = {
      repository: {
        issues: {
          edges: [
            {
              node: {
                title: "Foo",
              },
            },
            {
              node: {
                title: "Bar",
              },
            },
            {
              node: {
                title: "Baz",
              },
            },
          ],
        },
      },
    };

    const mock = fetchMock.createInstance().post(
      "https://github.acme-inc.com/api/graphql",
      { data: mockData },
      {
        headers: {
          authorization: "token secret123",
        },
      },
    );

    const authenticatedGraphql = graphql.defaults({
      headers: {
        authorization: `token secret123`,
      },
      request: {
        fetch: mock.fetchHandler,
      },
    });
    const acmeGraphql = authenticatedGraphql.defaults({
      baseUrl: "https://github.acme-inc.com/api",
    });
    return acmeGraphql(`{
      repository(owner:"octokit", name:"graphql.js") {
        issues(last:3) {
          edges {
            node {
              title
            }
          }
        }
      }
    }`).then((result) => {
      expect(JSON.stringify(result)).toStrictEqual(JSON.stringify(mockData));
    });
  });

  it("handle baseUrl set with /api/v3 suffix", () => {
    const mock = fetchMock.createInstance().post(
      "https://github.acme-inc.com/api/graphql",
      { data: { ok: true } },
      {
        headers: {
          authorization: "token secret123",
        },
      },
    );

    const ghesGraphQl = graphql.defaults({
      baseUrl: "https://github.acme-inc.com/api/v3",
      headers: {
        authorization: `token secret123`,
      },
      request: {
        fetch: mock.fetchHandler,
      },
    });

    return ghesGraphQl(`query {
      viewer {
        login
      }
    }`);
  });

  it("set defaults on .endpoint", () => {
    const mockData = {
      repository: {
        issues: {
          edges: [
            {
              node: {
                title: "Foo",
              },
            },
            {
              node: {
                title: "Bar",
              },
            },
            {
              node: {
                title: "Baz",
              },
            },
          ],
        },
      },
    };

    const authenticatedGraphql = graphql.defaults({
      headers: {
        authorization: `token secret123`,
      },
      request: {
        fetch: fetchMock.createInstance().post(
          "https://github.acme-inc.com/api/graphql",
          { data: mockData },
          {
            headers: {
              authorization: "token secret123",
            },
          },
        ),
      },
    });

    const { request: _request, ...requestOptions } =
      // @ts-expect-error - TODO: expects to set { url } but it really shouldn't
      authenticatedGraphql.endpoint();
    expect(requestOptions).toStrictEqual({
      method: "POST",
      url: "https://api.github.com/graphql",
      headers: {
        accept: "application/vnd.github.v3+json",
        authorization: "token secret123",
        "user-agent": userAgent,
      },
    });
  });

  it("Allows user to specify non variable options", () => {
    const mockData = {
      repository: {
        issues: {
          edges: [
            {
              node: {
                title: "Foo",
              },
            },
            {
              node: {
                title: "Bar",
              },
            },
            {
              node: {
                title: "Baz",
              },
            },
          ],
        },
      },
    };

    const query = /* GraphQL */ `
        query Blue($last: Int) {
          repository(owner: "blue", name: "graphql.js") {
            issues(last: $last) {
              edges {
                node {
                  title
                }
              }
            }
          }
        }

        query Green($last: Int) {
          repository(owner: "green", name: "graphql.js") {
            issues(last: $last) {
              edges {
                node {
                  title
                }
              }
            }
          }
        }
        `.trim();

    const fetch = fetchMock.createInstance();

    fetch.post(
      "https://api.github.com/graphql",
      { data: mockData },
      {
        method: "POST",
        headers: {
          accept: "application/vnd.github.v3+json",
          authorization: "token secret123",
          "user-agent": userAgent,
        },
        matcherFunction: (callLog: CallLog) => {
          const expected = {
            query: query,
            operationName: "Blue",
            variables: { last: 3 },
          };
          const result = callLog.options.body === JSON.stringify(expected);
          if (!result) {
            console.warn("Body did not match expected value", {
              expected,
              actual: JSON.parse(callLog.options.body as string),
            });
          }
          return result;
        },
      },
    );

    const authenticatedGraphql = graphql.defaults({
      headers: {
        authorization: `token secret123`,
      },
      request: {
        fetch: fetch.fetchHandler,
      },
    });

    return new Promise<void>((res, rej) =>
      authenticatedGraphql({
        query,
        headers: {
          authorization: `token secret123`,
        },
        request: {
          fetch: fetch.fetchHandler,
        },
        operationName: "Blue",
        last: 3,
      })
        .then((result) => {
          expect(JSON.stringify(result)).toStrictEqual(
            JSON.stringify(mockData),
          );
          res();
        })
        .catch(() => {
          rej("Should have resolved");
        }),
    );
  });
});
```

## File: `test/error.test.ts`
```typescript
import { describe, expect, it } from "vitest";
import fetchMock from "fetch-mock";

import { graphql, GraphqlResponseError } from "../src";

describe("errors", () => {
  it("Invalid query", () => {
    const query = `{
  viewer {
    bioHtml
  }
}`;
    const mockResponse = {
      data: null,
      errors: [
        {
          locations: [
            {
              column: 5,
              line: 3,
            },
          ],
          message: "Field 'bioHtml' doesn't exist on type 'User'",
        },
      ],
    };

    const mock = fetchMock
      .createInstance()
      .post("https://api.github.com/graphql", mockResponse);

    return graphql(query, {
      headers: {
        authorization: `token secret123`,
      },
      request: {
        fetch: mock.fetchHandler,
      },
    })
      .then(() => {
        throw new Error("Should not resolve");
      })

      .catch((error) => {
        expect(error.message).toEqual(
          "Request failed due to following response errors:\n" +
            " - Field 'bioHtml' doesn't exist on type 'User'",
        );
        expect(JSON.stringify(error.errors)).toStrictEqual(
          JSON.stringify(mockResponse.errors),
        );
        expect(error.request.query).toEqual(query);
      });
  });

  it("Should be able check if an error is instance of a GraphQL response error", () => {
    const query = `{
      repository {
        name
      }
    }`;

    const mockResponse = {
      data: null,
      errors: [
        {
          locations: [
            {
              column: 5,
              line: 3,
            },
          ],
          message: "Some error message",
        },
      ],
    };

    const mock = fetchMock
      .createInstance()
      .post("https://api.github.com/graphql", mockResponse);

    return graphql(query, {
      headers: {
        authorization: `token secret123`,
      },
      request: {
        fetch: mock.fetchHandler,
      },
    })
      .then(() => {
        throw new Error("Should not resolve");
      })

      .catch((error) => {
        expect(error instanceof GraphqlResponseError).toBe(true);
      });
  });

  it("Should throw an error for a partial response accompanied by errors", () => {
    const query = `{
      repository(name: "probot", owner: "probot") {
        name
        ref(qualifiedName: "master") {
          target {
            ... on Commit {
              history(first: 25, after: "invalid cursor") {
                nodes {
                  message
                }
              }
            }
          }
        }
      }
    }`;

    const mockResponse = {
      data: {
        repository: {
          name: "probot",
          ref: null,
        },
      },
      errors: [
        {
          locations: [
            {
              column: 11,
              line: 7,
            },
          ],
          message: "`invalid cursor` does not appear to be a valid cursor.",
          path: ["repository", "ref", "target", "history"],
          type: "INVALID_CURSOR_ARGUMENTS",
        },
      ],
    };

    const mock = fetchMock
      .createInstance()
      .post("https://api.github.com/graphql", {
        body: mockResponse,
        headers: {
          "x-github-request-id": "C5E6:259A:1351B40:2E88B87:5F1F9C41",
        },
      });

    return graphql(query, {
      headers: {
        authorization: `token secret123`,
      },
      request: {
        fetch: mock.fetchHandler,
      },
    })
      .then(() => {
        throw new Error("Should not resolve");
      })
      .catch((error) => {
        expect(error.message).toEqual(
          "Request failed due to following response errors:\n" +
            " - `invalid cursor` does not appear to be a valid cursor.",
        );
        expect(JSON.stringify(error.errors)).toStrictEqual(
          JSON.stringify(mockResponse.errors),
        );
        expect(error.request.query).toEqual(query);
        expect(JSON.stringify(error.data)).toStrictEqual(
          JSON.stringify(mockResponse.data),
        );
        expect(error.headers).toHaveProperty("x-github-request-id");
        expect(error.headers["x-github-request-id"]).toEqual(
          "C5E6:259A:1351B40:2E88B87:5F1F9C41",
        );
      });
  });

  it("Should throw for server error", () => {
    const query = `{
      viewer {
        login
      }
    }`;

    const mock = fetchMock
      .createInstance()
      .post("https://api.github.com/graphql", 500);

    return graphql(query, {
      headers: {
        authorization: `token secret123`,
      },
      request: {
        fetch: mock.fetchHandler,
      },
    })
      .then(() => {
        throw new Error("Should not resolve");
      })
      .catch((error) => {
        expect(error.status).toEqual(500);
      });
  });
});
```

## File: `test/graphql.test.ts`
```typescript
import { describe, expect, it } from "vitest";
import fetchMock, { type CallLog } from "fetch-mock";
import { getUserAgent } from "universal-user-agent";

import { graphql } from "../src";
import { VERSION } from "../src/version";
import type { RequestParameters } from "../src/types";

const userAgent = `octokit-graphql.js/${VERSION} ${getUserAgent()}`;

describe("graphql()", () => {
  it("is a function", () => {
    expect(graphql).toBeInstanceOf(Function);
  });

  it("README simple query example", () => {
    const mockData = {
      repository: {
        issues: {
          edges: [
            {
              node: {
                title: "Foo",
              },
            },
            {
              node: {
                title: "Bar",
              },
            },
            {
              node: {
                title: "Baz",
              },
            },
          ],
        },
      },
    };

    const mock = fetchMock.createInstance().post(
      "https://api.github.com/graphql",
      { data: mockData },
      {
        headers: {
          accept: "application/vnd.github.v3+json",
          authorization: "token secret123",
          "user-agent": userAgent,
        },
      },
    );

    return graphql(
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
        request: {
          fetch: mock.fetchHandler,
        },
      },
    ).then((result) => {
      expect(JSON.stringify(result)).toStrictEqual(JSON.stringify(mockData));
    });
  });

  it("Variables", () => {
    const query = `query lastIssues($owner: String!, $repo: String!, $num: Int = 3) {
      repository(owner:$owner, name:$repo) {
        issues(last:$num) {
          edges {
            node {
              title
            }
          }
        }
      }
    }`;

    const mock = fetchMock
      .createInstance()
      .post("https://api.github.com/graphql", (_url: any) => {
        //@ts-ignore mock.fetchHandler is not typed
        const body = JSON.parse(mock.callHistory.calls()[0].options.body);
        expect(body.query).toEqual(query);
        expect(body.variables).toStrictEqual({
          owner: "octokit",
          repo: "graphql.js",
        });

        return { data: {} };
      });

    return graphql(query, {
      headers: {
        authorization: `token secret123`,
      },
      owner: "octokit",
      repo: "graphql.js",
      request: {
        fetch: mock.fetchHandler,
      },
    });
  });

  it("Pass headers together with variables as 2nd argument", () => {
    const query = `query lastIssues($owner: String!, $repo: String!, $num: Int = 3) {
      repository(owner:$owner, name:$repo) {
        issues(last:$num) {
          edges {
            node {
              title
            }
          }
        }
      }
    }`;

    const mock = fetchMock
      .createInstance()
      .post("https://api.github.com/graphql", (_url: any) => {
        //@ts-ignore mock.fetchHandler is not typed
        const body = JSON.parse(mock.callHistory.calls()[0].options.body);
        expect(body.query).toEqual(query);
        expect(body.variables).toStrictEqual({
          owner: "octokit",
          repo: "graphql.js",
        });
        expect(options.headers!.authorization).toEqual("token secret123");
        // @ts-ignore `request.headers` are typed incorrectly by fetch-mock
        const custom = mock.callHistory.calls()[0].options.headers!["x-custom"];
        expect(custom).toContain("value");
        return { data: {} };
      });

    const options: RequestParameters = {
      headers: {
        authorization: `token secret123`,
        "x-custom": "value",
      },
      owner: "octokit",
      repo: "graphql.js",
      request: {
        fetch: mock.fetchHandler,
      },
    };

    return graphql(query, options);
  });

  it("Pass query together with headers and variables", () => {
    const query = `query lastIssues($owner: String!, $repo: String!, $num: Int = 3) {
      repository(owner:$owner, name:$repo) {
        issues(last:$num) {
          edges {
            node {
              title
            }
          }
        }
      }
    }`;

    const mock = fetchMock
      .createInstance()
      .post("https://api.github.com/graphql", (_url: any) => {
        //@ts-ignore mock.fetchHandler is not typed
        const body = JSON.parse(mock.callHistory.calls()[0].options.body);
        expect(body.query).toEqual(query);
        expect(body.variables).toStrictEqual({
          owner: "octokit",
          repo: "graphql.js",
        });

        return { data: {} };
      });

    const options: RequestParameters = {
      headers: {
        authorization: `token secret123`,
      },
      owner: "octokit",
      query,
      repo: "graphql.js",
      request: {
        fetch: mock.fetchHandler,
      },
    };

    return graphql(options);
  });

  it("Don’t send empty variables object", () => {
    const query = "{ viewer { login } }";

    const mock = fetchMock
      .createInstance()
      .post("https://api.github.com/graphql", (_url: any) => {
        //@ts-ignore mock.fetchHandler is not typed
        const body = JSON.parse(mock.callHistory.calls()[0].options.body);
        expect(body.query).toEqual(query);
        expect(body.variables).toEqual(undefined);
        return { data: {} };
      });

    return graphql(query, {
      headers: {
        authorization: `token secret123`,
      },
      request: {
        fetch: mock.fetchHandler,
      },
    });
  });

  it("MediaType previews are added to header", async () => {
    const query = `{ viewer { login } }`;

    // Create a new FetchMock instance
    const mock = fetchMock
      .createInstance()
      .postOnce("https://api.github.com/graphql", (_url: any) => {
        // @ts-ignore `request.headers` are typed incorrectly by fetch-mock
        const accept = mock.callHistory.calls()[0].options.headers["accept"];
        expect(accept).toContain("antiope-preview");
        expect(accept).toContain("testpkg-preview");
        return {
          status: 200,
          body: { data: {} },
        };
      });

    // Perform the GraphQL request using mock.fetchHandler
    const response = await graphql(query, {
      headers: {
        authorization: `token secret123`,
      },
      mediaType: { previews: ["antiope", "testpkg"] },
      request: {
        fetch: mock.fetchHandler,
      },
    });

    expect(response).toEqual({});
  });

  it("query variable (#166)", () => {
    expect.assertions(1);

    const query = `query search($query: String!) {
      search(query: $query, first: 10, type: ISSUE) {
        edges {
          node {
            ... on PullRequest {
              title
            }
          }
        }
      }
    }`;

    return graphql(query, {
      headers: {
        authorization: `token secret123`,
      },
      query: "test",
    }).catch((error) => {
      expect(error.message).toEqual(
        `[@octokit/graphql] "query" cannot be used as variable name`,
      );
    });
  });

  it("url variable (#264)", () => {
    expect.assertions(1);

    const query = `query GetCommitStatus($url: URI!) {
      resource(url: $url) {
        ... on Commit {
          status {
            state
          }
        }
      }
    }`;

    return graphql(query, {
      url: "https://example.com",
    }).catch((error) => {
      expect(error.message).toEqual(
        `[@octokit/graphql] "url" cannot be used as variable name`,
      );
    });
  });

  it("method variable", () => {
    expect.assertions(1);

    const query = `query($method:String!){
      search(query:$method,type:ISSUE) {
        codeCount
      }
    }`;

    return graphql(query, {
      method: "test",
    }).catch((error) => {
      expect(error.message).toEqual(
        `[@octokit/graphql] "method" cannot be used as variable name`,
      );
    });
  });

  describe("When using a query with multiple operations", () => {
    const mockData = {
      repository: {
        issues: {
          edges: [
            {
              node: {
                title: "Foo",
              },
            },
            {
              node: {
                title: "Bar",
              },
            },
            {
              node: {
                title: "Baz",
              },
            },
          ],
        },
      },
    };

    const mockErrors = {
      errors: [{ message: "An operation name is required" }],
      data: undefined,
      status: 400,
    };

    const query = /* GraphQL */ `
      query Blue($last: Int) {
        repository(owner: "blue", name: "graphql.js") {
          issues(last: $last) {
            edges {
              node {
                title
              }
            }
          }
        }
      }

      query Green($last: Int) {
        repository(owner: "green", name: "graphql.js") {
          issues(last: $last) {
            edges {
              node {
                title
              }
            }
          }
        }
      }
      `.trim();

    it("Sends both queries to the server (which will respond with bad request)", () => {
      const fetch = fetchMock.createInstance();

      fetch.post("https://api.github.com/graphql", mockErrors, {
        method: "POST",
        headers: {
          accept: "application/vnd.github.v3+json",
          authorization: "token secret123",
          "user-agent": userAgent,
        },
        matcherFunction: (callLog: CallLog) => {
          const expected = {
            query: query,
            variables: { last: 3 },
          };
          const result = callLog.options.body === JSON.stringify(expected);
          if (!result) {
            console.warn("Body did not match expected value", {
              expected,
              actual: JSON.parse(callLog.options.body as string),
            });
          }
          return result;
        },
      });

      return new Promise<void>((res, rej) =>
        graphql(query, {
          headers: {
            authorization: `token secret123`,
          },
          request: {
            fetch: fetch.fetchHandler,
          },
          last: 3,
        })
          .then(() => {
            rej("Should have thrown an error");
          })
          .catch((result) => {
            expect(JSON.stringify(result.response)).toStrictEqual(
              JSON.stringify(mockErrors),
            );
            res();
          }),
      );
    });

    it('Allows the user to specify the operation name in the "operationName" option', () => {
      const fetch = fetchMock.createInstance();

      fetch.post(
        "https://api.github.com/graphql",
        { data: mockData },
        {
          method: "POST",
          headers: {
            accept: "application/vnd.github.v3+json",
            authorization: "token secret123",
            "user-agent": userAgent,
          },
          matcherFunction: (callLog: CallLog) => {
            const expected = {
              query: query,
              operationName: "Blue",
              variables: { last: 3 },
            };
            const result = callLog.options.body === JSON.stringify(expected);
            if (!result) {
              console.warn("Body did not match expected value", {
                expected,
                actual: JSON.parse(callLog.options.body as string),
              });
            }
            return result;
          },
        },
      );

      return new Promise<void>((res, rej) =>
        graphql(query, {
          headers: {
            authorization: `token secret123`,
          },
          request: {
            fetch: fetch.fetchHandler,
          },
          operationName: "Blue",
          last: 3,
        })
          .then((result) => {
            expect(JSON.stringify(result)).toStrictEqual(
              JSON.stringify(mockData),
            );
            res();
          })
          .catch((error) => {
            rej(error);
          }),
      );
    });
  });
});
```

## File: `test/tsconfig.test.json`
```json
{
  "extends": "../tsconfig.json",
  "compilerOptions": {
    "emitDeclarationOnly": false,
    "noEmit": true,
    "allowImportingTsExtensions": true
  },
  "include": ["src/**/*"]
}
```

## File: `test/with-custom-request.test.ts`
```typescript
import { describe, expect, it } from "vitest";
import fetchMock from "fetch-mock";
import { request } from "@octokit/request";

import { withCustomRequest } from "../src";

describe("withCustomRequest()", () => {
  it("README example", () => {
    const myRequest = request.defaults({
      headers: {
        authorization: "token secret123",
        "user-agent": "test",
      },
    });
    const myGraphql = withCustomRequest(myRequest);

    const mockData = {
      repository: {
        issues: {
          edges: [
            {
              node: {
                title: "Foo",
              },
            },
            {
              node: {
                title: "Bar",
              },
            },
            {
              node: {
                title: "Baz",
              },
            },
          ],
        },
      },
    };

    const mock = fetchMock.createInstance().post(
      "https://api.github.com/graphql",
      { data: mockData },
      {
        headers: {
          accept: "application/vnd.github.v3+json",
          authorization: "token secret123",
          "user-agent": "test",
        },
      },
    );

    return myGraphql(
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
        request: {
          fetch: mock.fetchHandler,
        },
      },
    ).then((result) => {
      expect(JSON.stringify(result)).toStrictEqual(JSON.stringify(mockData));
    });
  });
});
```


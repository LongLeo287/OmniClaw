---
id: slonik
type: knowledge
owner: OA_Triage
---
# slonik
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "workspaces": [
    "packages/types",
    "packages/utilities",
    "packages/errors",
    "packages/sql-tag",
    "packages/driver",
    "packages/pg-driver",
    "packages/slonik",
    "packages/*"
  ],
  "scripts": {
    "lint:knip": "knip",
    "lint:oxlint": "oxlint",
    "lint:oxfmt": "oxfmt --check .",
    "lint": "npm run lint:knip && npm run lint:oxlint && npm run lint:oxfmt"
  },
  "dependencies": {
    "@changesets/cli": "^2.29.8"
  },
  "devDependencies": {
    "@changesets/changelog-github": "^0.5.2",
    "husky": "^9.1.7",
    "knip": "^5.83.1",
    "oxfmt": "^0.40.0",
    "oxlint": "^1",
    "oxlint-config-canonical": "^1"
  }
}

```

### File: README.md
```md
# Slonik

[![NPM version](http://img.shields.io/npm/v/slonik.svg?style=flat-square)](https://www.npmjs.org/package/slonik)
[![Canonical Code Style](https://img.shields.io/badge/code%20style-canonical-blue.svg?style=flat-square)](https://github.com/gajus/canonical)
[![Twitter Follow](https://img.shields.io/twitter/follow/kuizinas.svg?style=social&label=Follow)](https://twitter.com/kuizinas)

A [battle-tested](#battle-tested) Node.js PostgreSQL client with strict types, detailed logging and assertions.

> [!NOTE]
> NEW! Use Slonik with [`eslint-plugin-slonik`](https://github.com/gajus/eslint-plugin-slonik) to validate your SQL queries against your database schema.

![Tailing Slonik logs](./.README/slonik-log-tailing.gif)

(The above GIF shows Slonik producing [query logs](https://github.com/gajus/slonik#logging). Slonik produces logs using [Roarr](https://github.com/gajus/roarr). Logs include stack trace of the actual query invocation location and values used to execute the query.)

## Sponsors

If you value my work and want to see Slonik and [many other of my](https://github.com/gajus/) Open-Source projects to be continuously improved, then please consider becoming a patron:

[![Buy Me A Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/gajus)
[![Become a Patron](https://c5.patreon.com/external/logo/become_a_patron_button.png)](https://www.patreon.com/gajus)

## Principles

- Promotes writing raw SQL.
- Discourages ad-hoc dynamic generation of SQL.

Read: [Stop using Knex.js](https://medium.com/@gajus/bf410349856c)

Note: Using this project does not require TypeScript. It is a regular ES6 module. Ignore the type definitions used in the documentation if you do not use a type system.

## Features

- [Runtime validation](#runtime-validation).
- [Assertions and type safety](#repeating-code-patterns-and-type-safety).
- [Safe connection handling](#protecting-against-unsafe-connection-handling).
- [Safe transaction handling](#protecting-against-unsafe-transaction-handling).
- [Safe value interpolation](#protecting-against-unsafe-value-interpolation).
- [Transaction nesting](#transaction-nesting).
- [Transaction events](#transaction-events).
- [Transaction retrying](#transaction-retrying).
- [Query retrying](#query-retrying).
- Detailed [logging](#debugging).
- [Asynchronous stack trace resolution](#capture-stack-trace).
- [Middlewares](#interceptors).
- [Mapped errors](#error-handling).
- [ESLint plugin](https://github.com/gajus/eslint-plugin-sql).

## Contents

- [Slonik](#slonik)
  - [Sponsors](#sponsors)
  - [Principles](#principles)
  - [Features](#features)
  - [Contents](#contents)
  - [About Slonik](#about-slonik)
    - [Battle-Tested](#battle-tested)
    - [Origin of the name](#origin-of-the-name)
    - [Repeating code patterns and type safety](#repeating-code-patterns-and-type-safety)
    - [Protecting against unsafe connection handling](#protecting-against-unsafe-connection-handling)
    - [Protecting against unsafe transaction handling](#protecting-against-unsafe-transaction-handling)
    - [Protecting against unsafe value interpolation](#protecting-against-unsafe-value-interpolation)
  - [Documentation](#documentation)
  - [Usage](#usage)
    - [Connection URI](#connection-uri)
    - [Create connection](#create-connection)
    - [End connection pool](#end-connection-pool)
    - [Describing the current state of the connection pool](#describing-the-current-state-of-the-connection-pool)
    - [API](#api)
    - [Default configuration](#default-configuration)
    - [Checking out a client from the connection pool](#checking-out-a-client-from-the-connection-pool)
    - [Events](#events)
  - [How are they different?](#how-are-they-different)
    - [`pg` vs `slonik`](#pg-vs-slonik)
    - [`pg-promise` vs `slonik`](#pg-promise-vs-slonik)
    - [`postgres` vs `slonik`](#postgres-vs-slonik)
  - [Type parsers](#type-parsers)
    - [Built-in type parsers](#built-in-type-parsers)
  - [Interceptors](#interceptors)
    - [Interceptor methods](#interceptor-methods)
    - [Community interceptors](#community-interceptors)
  - [Recipes](#recipes)
    - [Inserting large number of rows](#inserting-large-number-of-rows)
    - [Routing queries to different connections](#routing-queries-to-different-connections)
    - [Building Utility Statements](#building-utility-statements)
    - [Inserting vector data](#inserting-vector-data)
  - [Runtime validation](#runtime-validation)
    - [Motivation](#motivation)
    - [Result parser interceptor](#result-parser-interceptor)
    - [Example use of `sql.type`](#example-use-of-sqltype)
    - [Performance penalty](#performance-penalty)
    - [Unknown keys](#unknown-keys)
    - [Handling schema validation errors](#handling-schema-validation-errors)
    - [Inferring types](#inferring-types)
    - [Transforming results](#transforming-results)
  - [`sql` tag](#sql-tag)
    - [Type aliases](#type-aliases)
    - [Typing `sql` tag](#typing-sql-tag)
  - [Value placeholders](#value-placeholders)
    - [Tagged template literals](#tagged-template-literals)
    - [Manually constructing the query](#manually-constructing-the-query)
    - [Nesting `sql`](#nesting-sql)
  - [Query building](#query-building)
    - [`sql.array`](#sqlarray)
    - [`sql.binary`](#sqlbinary)
    - [`sql.date`](#sqldate)
    - [`sql.fragment`](#sqlfragment)
    - [`sql.identifier`](#sqlidentifier)
    - [`sql.interval`](#sqlinterval)
    - [`sql.join`](#sqljoin)
    - [`sql.json`](#sqljson)
    - [`sql.jsonb`](#sqljsonb)
    - [`sql.literalValue`](#sqlliteralvalue)
    - [`sql.timestamp`](#sqltimestamp)
    - [`sql.unnest`](#sqlunnest)
    - [`sql.unsafe`](#sqlunsafe)
    - [`sql.uuid`](#sqluuid)
    - [`sql.prepared`](#sqlprepared)
  - [Query methods](#query-methods)
    - [`any`](#any)
    - [`anyFirst`](#anyfirst)
    - [`exists`](#exists)
    - [`many`](#many)
    - [`manyFirst`](#manyfirst)
    - [`maybeOne`](#maybeone)
    - [`maybeOneFirst`](#maybeonefirst)
    - [`one`](#one)
    - [`oneFirst`](#onefirst)
    - [`query`](#query)
    - [`stream`](#stream)
    - [`transaction`](#transaction)
  - [Utilities](#utilities)
    - [`parseDsn`](#parsedsn)
    - [`stringifyDsn`](#stringifydsn)
  - [Error handling](#error-handling)
    - [Original `node-postgres` error](#original-node-postgres-error)
    - [Handling `BackendTerminatedError`](#handling-backendterminatederror)
    - [Handling `CheckIntegrityConstraintViolationError`](#handling-checkintegrityconstraintviolationerror)
    - [Handling `ConnectionError`](#handling-connectionerror)
    - [Handling `DataIntegrityError`](#handling-dataintegrityerror)
    - [Handling `ForeignKeyIntegrityConstraintViolationError`](#handling-foreignkeyintegrityconstraintviolationerror)
    - [Handling `NotFoundError`](#handling-notfounderror)
    - [Handling `NotNullIntegrityConstraintViolationError`](#handling-notnullintegrityconstraintviolationerror)
    - [Handling `StatementCancelledError`](#handling-statementcancellederror)
    - [Handling `StatementTimeoutError`](#handling-statementtimeouterror)
    - [Handling `UniqueIntegrityConstraintViolationError`](#handling-uniqueintegrityconstraintviolationerror)
    - [Handling `TupleMovedToAnotherPartitionError`](#handling-tuplemovedtoanotherpartitionerror)
  - [Migrations](#migrations)
  - [Types](#types)
  - [Debugging](#debugging)
    - [Logging](#logging)
    - [Capture stack trace](#capture-stack-trace)
  - [Syntax Highlighting](#syntax-highlighting)
    - [Atom Syntax Highlighting Plugin](#atom-syntax-highlighting-plugin)
    - [VS Code Syntax Highlighting Extension](#vs-code-syntax-highlighting-extension)
  - [Development](#development)

## About Slonik

### Battle-Tested

Slonik began as a collection of utilities designed for working with [`node-postgres`](https://github.com/brianc/node-postgres). It continues to use `node-postgres` driver as it provides a robust foundation for interacting with PostgreSQL. However, what once was a collection of utilities has since grown into a framework that abstracts repeating code patterns, protects against unsafe connection handling and value interpolation, and provides a rich debugging experience.

Slonik has been [battle-tested](https://medium.com/@gajus/lessons-learned-scaling-postgresql-database-to-1-2bn-records-month-edc5449b3067) with large data volumes and queries ranging from simple CRUD operations to data-warehousing needs.

### Origin of the name

![Slonik](./.README/postgresql-elephant.png)

**"Słonik"** is a Polish diminutive of **"słoń,"** meaning “little elephant” or “baby elephant.” The word **"słoń"** itself comes from Proto-Slavic \*_slonъ_, which was likely borrowed from a Germanic language and may ultimately trace back to Latin.

### Repeating code patterns and type safety

Among the primary reasons for developing Slonik, was the motivation to reduce the repeating code patterns and add a level of type safety. This is primarily achieved through the methods such as `one`, `many`, etc. But what is the issue? It is best illustrated with an example.

Suppose the requirement is to write a method that retrieves a resource ID given values defining (what we assume to be) a unique constraint. If we did not have the aforementioned helper methods available, then it would need to be written as:

```ts
import { sql, type DatabaseConnection } from "slonik";

type DatabaseRecordIdType = number;

const getFooIdByBar = async (
  connection: DatabaseConnection,
  bar: string,
): Promise<DatabaseRecordIdType> => {
  const fooResult = await connection.query(sql.typeAlias("id")`
    SELECT id
    FROM foo
    WHERE bar = ${bar}
  `);

  if (fooResult.rowCount === 0) {
    throw new Error("Resource not found.");
  }

  if (fooResult.rowCount > 1) {
    throw new Error("Data integrity constraint violation.");
  }

  return fooResult[0].id;
};
```

`oneFirst` method abstracts all of the above logic into:

```ts
const getFooIdByBar = (
  connection: DatabaseConnection,
  bar: string,
): Promise<DatabaseRecordIdType> => {
  return connection.oneFirst(sql.typeAlias("id")`
    SELECT id
    FROM foo
    WHERE bar = ${bar}
  `);
};
```

`oneFirst` throws:

- `NotFoundError` if query returns no rows
- `DataIntegrityError` if query returns multiple rows
- `DataIntegrityError` if query returns multiple columns

In the absence of helper methods, the overhead of repeating code becomes particularly visible when writing routines where multiple queries depend on the proceeding query results. Using methods with inbuilt assertions ensures that in case of an error, the error points to the source of the problem. In contrast, unless assertions for all possible outcomes are typed out as in the previous example, the unexpected result of the query will be fed to the next operation. If you are lucky, the next operation will simply break; if you are unlucky, you are risking data corruption and hard-to-locate bugs.

Furthermore, using methods that guarantee the shape of the results allows us to leverage static type checking and catch some of the errors even before executing the code, e.g.

```ts
const fooId = await connection.many(sql.typeAlias("id")`
  SELECT id
  FROM foo
  WHERE bar = ${bar}
`);

await connection.query(sql.typeAlias("void")`
  DELETE FROM baz
  WHERE foo_id = ${fooId}
`);
```

Static type check of the above example will produce a warning as the `fooId` is guaranteed to be an array and binding of the last query is expecting a primitive value.

### Protecting against unsafe connection handling

Slonik only allows to check out a connection for the duration of the promise routine supplied to the `pool#connect()` method.

The primary reason for implementing _only_ this connection pooling method is because the alternative is inherently unsafe, e.g.

```ts
// This is not valid Slonik API

const main = async () => {
  const connection = await pool.connect();

  await connection.query(sql.typeAlias("foo")`SELECT foo()`);

  await connection.release();
};
```

In this example, if `SELECT foo()` produces an error, then connection is never released, i.e. the connection hangs indefinitely.

A fix to the above is to ensure that `connection#release()` is always called, i.e.

```ts
// This is not valid Slonik API

const main = async () => {
  const connection = await pool.connect();

  let lastExecutionResult;

  try {
    lastExecutionResult = await connection.query(sql.typeAlias("foo")`SELECT foo()`);
  } finally {
    await connection.release();
  }

  return lastExecutionResult;
};
```

Slonik abstracts the latter pattern into `pool#connect()` method.

```ts
const main = () => {
  return pool.connect((connection) => {
    return connection.query(sql.typeAlias("foo")`SELECT foo()`);
  });
};
```

Using this pattern, we guarantee that connection is always released as soon as the `connect()` routine resolves or is rejected.

#### Resetting connection state

After the connection is released, Slonik resets the connection state. This is to prevent connection state from leaking between queries.

The default behaviour is to execute `DISCARD ALL` command. This behaviour can be adjusted by configuring `resetConnection` routine, e.g.

```ts
import { createPool, sql } from "slonik";
import { createPgDriverFactory } from "@slonik/pg-driver";

const pool = createPool("postgres://", {
  driverFactory: createPgDriverFactory(),
  resetConnection: async (connection) => {
    await connection.query("DISCARD ALL");
  },
});
```

> [!NOTE]
> Resetting a connection is a heavy operation. Depending on the application requirements, it may make sense to disable connection reset, e.g.
>
> ```ts
> import { createPool } from "slonik";
> import { createPgDriverFactory } from "@slonik/pg-driver";
>
> const pool = createPool("postgres://", {
>   driverFactory: createPgDriverFactory(),
>   resetConnection: async () => {},
> });
> ```

### Protecting against unsafe transaction handling

Just like in the [unsafe connection handling](#protecting-against-unsafe-connection-handling) example, Slonik only allows to create a transaction for the duration of the promise routine supplied to the `connection#transaction()` method.

```ts
connection.transaction(async (transactionConnection) => {
  await transactionConnection.query(sql.typeAlias("void")`INSERT INTO foo (bar) VALUES ('baz')`);
  await transactionConnection.query(sql.typeAlias("void")`INSERT INTO qux (quux) VALUES ('quuz')`);
});
```

This pattern ensures that the transaction is either committed or aborted the moment the promise is either resolved or rejected.

> [!NOTE]
> If you receive an error `UnexpectedForeignConnectionError`, then you are trying to execute a query using a connection that is not associated with the transaction. This error is thrown to prevent accidental unsafe transaction handling, e.g.
>
> ```ts
> pool.transaction(async (transactionConnection) => {
>   await pool.query(sql.typeAlias("void")`INSERT INTO foo (bar) VALUES ('baz')`);

... [TRUNCATED]
```

### File: .changeset\README.md
```md
# Changesets

Hello and welcome! This folder has been automatically generated by `@changesets/cli`, a build tool that works
with multi-package repos, or single-package repos to help you version and publish your code. You can
find the full documentation for it [in our repository](https://github.com/changesets/changesets)

We have a quick list of common questions to get you started engaging with this project in
[our documentation](https://github.com/changesets/changesets/blob/main/docs/common-questions.md)

```

### File: packages\benchmark\package.json
```json
{
  "name": "@slonik/benchmark",
  "version": "48.13.2",
  "private": true,
  "scripts": {
    "benchmark": "NODE_ENV=production node benchmark.js"
  },
  "dependencies": {
    "benny": "^3.7.1",
    "pg": "^8.18.0",
    "pg-promise": "^11.15.0",
    "postgres": "^3.4.7",
    "slonik": "^48.13.2"
  }
}

```

### File: packages\benchmark\README.md
```md
# Node.js PostgreSQL Client Benchmark

## Results

| **client**                                             | **select**      | **select_arg** | **select_args** | **select_where** |
| ------------------------------------------------------ | --------------- | -------------- | --------------- | ---------------- |
| [`pg`](https://github.com/brianc/node-postgres)        | 1,287 ⚡️        | 831 (-31.89%)  | 819 (-24.03%)   | 890 (-22.27%)    |
| [`pg-promise`](https://github.com/vitaly-t/pg-promise) | 1,050 (-18.41%) | 1,171 (-4.02%) | 965 (-10.48%)   | 1,099 (-4.02%)   |
| [`slonik`](https://github.com/gajus/slonik)            | 988 (-23.23%)   | 1,220 ⚡️       | 1,039 (-3.62%)  | 1,021 (-10.83%)  |
| [`postgres`](https://github.com/porsager/postgres)     | 1,191 (-7.46%)  | 1,175 (-3.69%) | 1,078 ⚡️        | 1,145 ⚡️         |

Results show operations per second (greater is better).

System used to run benchmarks:

```
System:
  OS: macOS 10.15.6
  CPU: (16) x64 Intel(R) Core(TM) i9-9980HK CPU @ 2.40GHz
  Memory: 64.00 GB
Binaries:
  Node: 15.2.1
```

<!-- Use https://npmjs.com/envinfo to generate the system information. -->

## Note about the results

[`pg-promise`](https://github.com/vitaly-t/pg-promise) and Slonik are both based on [`pg`](https://github.com/brianc/node-postgres). Therefore, with a few exceptions, they cannot perform better than the underlying driver. What these results show is that all abstractions perform about the same, and that the bottleneck is always the query execution time.

## Run benchmark

```bash
docker run --name slonik-test --rm -it -e POSTGRES_PASSWORD=postgres -p 5432:5432 postgres -N 1000
```

```bash
npm install
npm run benchmark
```

## Disclaimer

Take these benchmarks with a grain of salt. I say this because running these benchmarks several times in a row will prompt outliers.

```

### File: packages\errors\package.json
```json
{
  "name": "@slonik/errors",
  "version": "48.13.2",
  "description": "A Node.js PostgreSQL client with strict types, detailed logging and assertions.",
  "keywords": [
    "postgresql",
    "promise",
    "types"
  ],
  "license": "BSD-3-Clause",
  "author": {
    "name": "Gajus Kuizinas",
    "email": "gajus@gajus.com",
    "url": "http://gajus.com"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/gajus/slonik"
  },
  "files": [
    "./src",
    "./dist"
  ],
  "type": "module",
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "scripts": {
    "build": "rm -fr ./dist && tsc --project ./tsconfig.json",
    "lint": "npm run lint:cspell && npm run lint:tsc",
    "lint:cspell": "cspell . --no-progress --gitignore",
    "lint:tsc": "tsc --noEmit",
    "test": "ava --verbose --serial"
  },
  "dependencies": {
    "@slonik/types": "^48.13.2"
  },
  "devDependencies": {
    "@standard-schema/spec": "^1.0.0",
    "@types/node": "^24.10.13",
    "ava": "^6.4.1",
    "cspell": "^9.6.4",
    "tsimp": "^2.0.12",
    "typescript": "^5.9.3"
  },
  "ava": {
    "extensions": [
      "ts"
    ],
    "files": [
      "src/**/*.test.ts"
    ],
    "nodeArguments": [
      "--import=tsimp"
    ]
  },
  "engines": {
    "node": ">=24"
  }
}

```

### File: packages\errors\README.md
```md
# Slonik Errors

```

### File: packages\types\package.json
```json
{
  "name": "@slonik/types",
  "version": "48.13.2",
  "description": "A Node.js PostgreSQL client with strict types, detailed logging and assertions.",
  "keywords": [
    "postgresql",
    "promise",
    "types"
  ],
  "license": "BSD-3-Clause",
  "author": {
    "name": "Gajus Kuizinas",
    "email": "gajus@gajus.com",
    "url": "http://gajus.com"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/gajus/slonik"
  },
  "files": [
    "./src",
    "./dist"
  ],
  "type": "module",
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "scripts": {
    "build": "rm -fr ./dist && tsc --project ./tsconfig.json",
    "lint": "npm run lint:cspell && npm run lint:tsc",
    "lint:cspell": "cspell . --no-progress --gitignore",
    "lint:tsc": "tsc --noEmit",
    "test": "ava --verbose --serial"
  },
  "devDependencies": {
    "@types/node": "^24.10.13",
    "ava": "^6.4.1",
    "cspell": "^9.6.4",
    "tsimp": "^2.0.12",
    "typescript": "^5.9.3"
  },
  "peerDependencies": {
    "zod": "^3.25 || ^4"
  },
  "ava": {
    "extensions": [
      "ts"
    ],
    "files": [
      "src/**/*.test.ts"
    ],
    "nodeArguments": [
      "--import=tsimp"
    ]
  },
  "engines": {
    "node": ">=24"
  }
}

```

### File: packages\types\README.md
```md
# Slonik Types

Slonik type primitives.

```

### File: .oxfmtrc.json
```json
{
  "$schema": "./node_modules/oxfmt/configuration_schema.json",
  "ignorePatterns": ["**/CHANGELOG.md"]
}

```

### File: CONTRIBUTING.md
```md
# Contributing to Slonik

## Setup Instructions

```bash
pnpm install
```

## Running tests

```bash
pnpm run -r build
pnpm run -r lint
pnpm run -r test
```

### Supporting Database

Running Slonik tests requires having a local PostgreSQL instance.

The easiest way to setup a temporary instance for testing is using Docker, e.g.

```bash
docker run --name slonik-test --rm -it -e POSTGRES_PASSWORD=postgres -p 5432:5432 postgres -N 1000
```

### Making Releases

We use [Changesets](https://github.com/changesets/changesets) to manage releases.

When done with your changes, run `pnpm changeset` to create a new changeset.

Then commit the changes and push to your branch.

```

### File: knip.json
```json
{
  "$schema": "https://unpkg.com/knip@2/schema.json",
  "entry": ["src/index.ts!", "src/**/*.test.ts"],
  "ignoreDependencies": [
    "@changesets/cli",
    "@slonik/test-ssls",
    "husky",
    "oxlint-config-canonical"
  ],
  "project": ["src/**/*.ts"]
}

```

### File: oxlint.config.ts
```ts
import { config } from "oxlint-config-canonical";
import { defineConfig } from "oxlint";

export default defineConfig({
  extends: [config],
  ignorePatterns: ["**/dist/", "**/.*/", "**/CHANGELOG.md"],
  overrides: [
    {
      files: ["**/*.{ts,tsx}"],
      rules: {
        "@typescript-eslint/no-explicit-any": "off",
        "id-length": "off",
        "no-promise-executor-return": "off",
        "no-unused-expressions": "off",
        "no-unused-vars": "off",
        "no-warning-comments": "off",
        "perfectionist/sort-classes": "off",
        "perfectionist/sort-modules": "off",
      },
    },
  ],
});

```

### File: pnpm-workspace.yaml
```yaml
packages:
  - "packages/*"

```

### File: .changeset\config.json
```json
{
  "___experimentalUnsafeOptions_WILL_CHANGE_IN_PATCH": {
    "onlyUpdatePeerDependentsWhenOutOfRange": true
  },
  "$schema": "https://unpkg.com/@changesets/config@3.0.0/schema.json",
  "changelog": [
    "@changesets/changelog-github",
    {
      "repo": "gajus/slonik"
    }
  ],
  "commit": false,
  "linked": [],
  "fixed": [["@slonik/*", "*"]],
  "access": "public",
  "baseBranch": "main",
  "updateInternalDependencies": "patch",
  "ignore": []
}

```

### File: .github\ISSUE_TEMPLATE\bug_report.md
```md
---
name: Bug report
about: Create a bug report to help us improve Slonik
title: ""
labels: bug
assignees: ""
---

<!--

Bug reports without a reproduction are not accepted.

To raise a bug, fork the repository, add a failing test and submit a pull request with a failing test case.

Issues without a reproducible test case will be closed.

-->

```

### File: .github\ISSUE_TEMPLATE\feature_request.md
```md
---
name: Feature request
about: Create an enhancement request to help us improve Slonik
title: ""
labels: enhancement
assignees: ""
---

<!--- Provide a general summary of the request in the Title above -->

## Desired Behavior

<!--- Tell us what should happen and/or provide example code that shows the desired usage -->

## Motivation

<!--- Tell us what the status quo is, and why it should change -->

## Implementation

<!--- (optional) Suggest a possible implementation for the enhancement -->

```

### File: .github\workflows\feature.yaml
```yaml
jobs:
  build:
    environment: release
    name: Build
    runs-on: ubuntu-latest
    steps:
      - name: setup repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: setup node.js
        uses: actions/setup-node@v4
        with:
          node-version: "24"
      - uses: pnpm/action-setup@v4
        name: install pnpm
        with:
          version: 8
          run_install: |
            - recursive: true
      - run: pnpm run -r build
    timeout-minutes: 10
  lint:
    environment: release
    name: Lint
    runs-on: ubuntu-latest
    steps:
      - name: setup repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: setup node.js
        uses: actions/setup-node@v4
        with:
          node-version: "24"
      - uses: pnpm/action-setup@v4
        name: install pnpm
        with:
          version: 8
          run_install: |
            - recursive: true
      - run: pnpm run -r build
      - run: pnpm run lint
      - run: pnpm run -r lint
    timeout-minutes: 10
  test:
    environment: release
    name: "Test node_version:${{ matrix.node_version }} test_only:${{ matrix.test_only }}"
    runs-on: ubuntu-latest
    services:
      postgres:
        env:
          POSTGRES_DB: postgres
          POSTGRES_PASSWORD: postgres
          POSTGRES_USER: postgres
        image: postgres:17
        options: >-
          --health-cmd pg_isready
          --health-interval 5s
          --health-timeout 5s
          --health-retries 5
          --name my_postgres_container
        ports:
          - 5432:5432
    steps:
      - name: install psql
        run: |
          sudo apt-get update
          sudo apt-get install --yes postgresql-client
      - name: Increase max_connections and shared_buffers
        run: |
          docker exec -i my_postgres_container bash << EOF
            sed -i -e 's/max_connections = 100/max_connections = 1000/' /var/lib/postgresql/data/postgresql.conf
            sed -i -e 's/shared_buffers = 128MB/shared_buffers = 2GB/' /var/lib/postgresql/data/postgresql.conf
          EOF
      - run: docker restart --time 0 my_postgres_container
      - run: sleep 10
      - run: docker exec my_postgres_container psql -U postgres -c 'SHOW max_connections;'
      - name: setup repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: setup node.js
        uses: actions/setup-node@v4
        with:
          node-version: "${{ matrix.node_version }}"
      - uses: pnpm/action-setup@v4
        name: install pnpm
        with:
          version: 8
          run_install: |
            - recursive: true
      - run: pnpm run -r build
      - env:
          POSTGRES_DSN: "postgres://postgres:postgres@localhost:5432"
          TEST_ONLY: "${{ matrix.test_only }}"
        run: pnpm run -r test
    strategy:
      fail-fast: false
      matrix:
        test_only:
          - utilities
          - pg-integration
        node_version:
          - 24
      max-parallel: 3
    timeout-minutes: 10
name: Test and build
on:
  pull_request:
    branches:
      - main
    paths-ignore:
      - ".editorconfig"
      - ".husky/**"
      - ".lintstagedrc.js"
      - ".mergify.yml"
      - ".nvmrc"
      - "README.md"
    types:
      - opened
      - synchronize
      - reopened
      - ready_for_review

```

### File: .github\workflows\main.yaml
```yaml
jobs:
  lint:
    environment: release
    name: Lint
    runs-on: ubuntu-latest
    steps:
      - name: setup repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: setup node.js
        uses: actions/setup-node@v4
        with:
          node-version: "24"
      - uses: pnpm/action-setup@v4
        name: install pnpm
        with:
          version: 8
          run_install: |
            - recursive: true
      - run: pnpm run -r build
      - run: pnpm run lint
      - run: pnpm run -r lint
    timeout-minutes: 10
  release:
    environment: release
    name: Release
    needs:
      - lint
      - test
    runs-on: ubuntu-latest
    permissions:
      contents: write
      id-token: write
      issues: write
      pull-requests: write
    steps:
      - name: setup repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: setup node.js
        uses: actions/setup-node@v4
        with:
          node-version: "24"
      - uses: pnpm/action-setup@v4
        name: install pnpm
        with:
          version: 8
          run_install: |
            - recursive: true
      - run: pnpm run -r build
      - env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          # Use OIDC for npm authentication instead of NPM_TOKEN
          # https://github.com/changesets/changesets/issues/1152#issuecomment-3190884868
          NPM_TOKEN: ""
        uses: changesets/action@v1
        with:
          publish: npx changeset publish
  test:
    environment: release
    name: "Test node_version:${{ matrix.node_version }} test_only:${{ matrix.test_only }}"
    runs-on: ubuntu-latest
    services:
      postgres:
        env:
          POSTGRES_DB: postgres
          POSTGRES_PASSWORD: postgres
          POSTGRES_USER: postgres
        image: postgres:17
        options: >-
          --health-cmd pg_isready
          --health-interval 5s
          --health-timeout 5s
          --health-retries 5
          --name my_postgres_container
        ports:
          - 5432:5432
    steps:
      - name: install psql
        run: |
          sudo apt-get update
          sudo apt-get install --yes postgresql-client
      - name: Increase max_connections and shared_buffers
        run: |
          docker exec -i my_postgres_container bash << EOF
            sed -i -e 's/max_connections = 100/max_connections = 1000/' /var/lib/postgresql/data/postgresql.conf
            sed -i -e 's/shared_buffers = 128MB/shared_buffers = 2GB/' /var/lib/postgresql/data/postgresql.conf
          EOF
      - run: docker restart --time 0 my_postgres_container
      - run: sleep 10
      - run: docker ps
      - run: docker exec my_postgres_container psql -U postgres -c 'SHOW max_connections;'
      - name: setup repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: setup node.js
        uses: actions/setup-node@v4
        with:
          node-version: "${{ matrix.node_version }}"
      - uses: pnpm/action-setup@v4
        name: install pnpm
        with:
          version: 8
          run_install: |
            - recursive: true
      - run: pnpm run -r build
      - env:
          POSTGRES_DSN: "postgres://postgres:postgres@localhost:5432"
          TEST_ONLY: "${{ matrix.test_only }}"
        run: pnpm run -r test
    strategy:
      fail-fast: false
      matrix:
        test_only:
          - utilities
          - pg-integration
        node_version:
          - 24
      max-parallel: 3
    timeout-minutes: 10
name: Lint, build and release
on:
  push:
    branches:
      - main

```

### File: packages\benchmark\benchmark.js
```js
/* eslint-disable n/global-require */

const { add, complete, cycle, suite } = require("benny");

const clients = [
  require("./clients/pg"),
  require("./clients/pg-promise"),
  require("./clients/slonik"),
  require("./clients/postgres"),
];

const tests = ["select", "select_arg", "select_args", "select_where"];

(async () => {
  const table = [
    "|**client**|" +
      tests
        .map((test) => {
          return "**" + test + "**";
        })
        .join("|") +
      "|",
    "|-|" +
      tests
        .map(() => {
          return "-";
        })
        .join("|") +
      "|",
  ];

  const clientResults = {};

  for (const test of tests) {
    const benchmarks = [];

    for (const client of clients) {
      benchmarks.push(add(client.name, client.tests[test]));
    }

    await suite(
      test,
      ...benchmarks,
      cycle(),
      complete((summary) => {
        for (const result of summary.results) {
          clientResults[result.name] = clientResults[result.name] || {};
          clientResults[result.name][summary.name] = result;
        }
      }),
    );
  }

  for (const client of clients) {
    const row = ["[`" + client.name + "`](" + client.url + ")"];

    for (const test of tests) {
      if (clientResults[client.name][test].percentSlower) {
        row.push(
          new Intl.NumberFormat("en-US").format(clientResults[client.name][test].ops) +
            " (-" +
            clientResults[client.name][test].percentSlower +
            "%)",
        );
      } else {
        row.push(
          new Intl.NumberFormat("en-US").format(clientResults[client.name][test].ops) + " ⚡️",
        );
      }
    }

    table.push("|" + row.join("|") + "|");
  }

  // eslint-disable-next-line no-console
  console.log(table.join("\n"));
})();

```

### File: packages\benchmark\CHANGELOG.md
```md
# @slonik/benchmark

## 48.13.2

### Patch Changes

- Updated dependencies [[`60a19c8`](https://github.com/gajus/slonik/commit/60a19c8f8265187a6d0d412d5629d2a49ae111d4)]:
  - slonik@48.13.2

## 48.13.1

### Patch Changes

- Updated dependencies [[`0cc29b6`](https://github.com/gajus/slonik/commit/0cc29b66efe0e7143639bca5daf7d9abe2fc38c1)]:
  - slonik@48.13.1

## 48.13.0

### Patch Changes

- Updated dependencies [[`c92d1df`](https://github.com/gajus/slonik/commit/c92d1df8e0e7fa3124dc69f32175a8b6df1b866d)]:
  - slonik@48.13.0

## 48.12.3

### Patch Changes

- Updated dependencies [[`e44b096`](https://github.com/gajus/slonik/commit/e44b096c65e5dbc8ac1c40a227dbcb6050f3d5aa)]:
  - slonik@48.12.3

## 48.12.2

### Patch Changes

- Updated dependencies [[`c477b3f`](https://github.com/gajus/slonik/commit/c477b3f9b3fb3f9522796451ad4c4105286b13c6)]:
  - slonik@48.12.2

## 48.12.1

### Patch Changes

- Updated dependencies [[`1deeb3b`](https://github.com/gajus/slonik/commit/1deeb3bcd0d8b1e914a62763df47b7edc662f437)]:
  - slonik@48.12.1

## 48.12.0

### Patch Changes

- Updated dependencies [[`e89dc6a`](https://github.com/gajus/slonik/commit/e89dc6aa3470ce1e186428a59ce70a1ee12a1f69)]:
  - slonik@48.12.0

## 48.11.0

### Patch Changes

- Updated dependencies [[`b3a0539`](https://github.com/gajus/slonik/commit/b3a053941d4abb73f4c4228890b1637bb499127b)]:
  - slonik@48.11.0

## 48.10.3

### Patch Changes

- Updated dependencies [[`31dfd11`](https://github.com/gajus/slonik/commit/31dfd11f4004b0ff77d481362901faf43f92d040)]:
  - slonik@48.10.3

## 48.10.2

### Patch Changes

- Updated dependencies [[`7cf3abc`](https://github.com/gajus/slonik/commit/7cf3abc560f1de937a044c0140a5d5e99f434f67)]:
  - slonik@48.10.2

## 48.10.1

### Patch Changes

- Updated dependencies [[`383d6e0`](https://github.com/gajus/slonik/commit/383d6e06ce8c6e399f090cca3eba2ab29f7844d2), [`61a8b67`](https://github.com/gajus/slonik/commit/61a8b6795fb5495f6221121cd5350b425f7f726c)]:
  - slonik@48.10.1

## 48.10.0

### Patch Changes

- Updated dependencies []:
  - slonik@48.10.0

## 48.9.0

### Patch Changes

- Updated dependencies [[`b9629b3`](https://github.com/gajus/slonik/commit/b9629b385fd75b6126a8356b5cf76d2dc45211d6)]:
  - slonik@48.9.0

## 48.8.12

### Patch Changes

- Updated dependencies [[`680b5dd`](https://github.com/gajus/slonik/commit/680b5dd245bb981cebd5911d75e668f7aade922e), [`fddc5b0`](https://github.com/gajus/slonik/commit/fddc5b0231e7398ad1a84848b5219a028af68ce7), [`f821c59`](https://github.com/gajus/slonik/commit/f821c5994f319c18435ef381bf766bdb79912db9), [`874cec3`](https://github.com/gajus/slonik/commit/874cec39f333a1772fbccc964c221a725947f328)]:
  - slonik@48.8.12

## 48.8.11

### Patch Changes

- Updated dependencies [[`3ce8e14`](https://github.com/gajus/slonik/commit/3ce8e1471c4ab7d471ba04ffbd601b286aae2bf4)]:
  - slonik@48.8.11

## 48.8.10

### Patch Changes

- Updated dependencies [[`0380c06`](https://github.com/gajus/slonik/commit/0380c069fef3376ee618d434695d0937312c339a)]:
  - slonik@48.8.10

## 48.8.9

### Patch Changes

- Updated dependencies [[`ebd94dd`](https://github.com/gajus/slonik/commit/ebd94ddc996f9b6ac0f62492a62c112fecc343bc)]:
  - slonik@48.8.9

## 48.8.8

### Patch Changes

- Updated dependencies [[`40edc3c`](https://github.com/gajus/slonik/commit/40edc3c02bbfe43478bfba053c8320dc793c8260)]:
  - slonik@48.8.8

## 48.8.7

### Patch Changes

- Updated dependencies [[`4d132f4`](https://github.com/gajus/slonik/commit/4d132f4dac330ace304de45b8b445cf03a13bdd6)]:
  - slonik@48.8.7

## 48.8.6

### Patch Changes

- Updated dependencies []:
  - slonik@48.8.6

## 48.8.5

### Patch Changes

- Updated dependencies [[`d6629d3`](https://github.com/gajus/slonik/commit/d6629d39ff0c5fd8f7edc5b6e4959ecf2a24905d)]:
  - slonik@48.8.5

## 48.8.4

### Patch Changes

- Updated dependencies [[`3238a49`](https://github.com/gajus/slonik/commit/3238a499e998e818408429d211602605546ef859)]:
  - slonik@48.8.4

## 48.8.3

### Patch Changes

- Updated dependencies [[`872c0a7`](https://github.com/gajus/slonik/commit/872c0a728e3b58854bafb6afcfb44bca02a72cd0)]:
  - slonik@48.8.3

## 48.8.2

### Patch Changes

- Updated dependencies [[`046be14`](https://github.com/gajus/slonik/commit/046be1476c96ea801fbb62d9cd7fde6a1e8da273)]:
  - slonik@48.8.2

## 48.8.1

### Patch Changes

- Updated dependencies [[`d548a71`](https://github.com/gajus/slonik/commit/d548a71c19cd97bc957b3b26e3f9d17afcc687f7)]:
  - slonik@48.8.1

## 48.8.0

### Patch Changes

- Updated dependencies [[`0166816`](https://github.com/gajus/slonik/commit/0166816b9608addbf19802b34c250a3039534f09)]:
  - slonik@48.8.0

## 48.7.1

### Patch Changes

- Updated dependencies []:
  - slonik@48.7.1

## 48.7.0

### Patch Changes

- Updated dependencies []:
  - slonik@48.7.0

## 48.6.0

### Patch Changes

- Updated dependencies [[`652d2ff`](https://github.com/gajus/slonik/commit/652d2ffee4eeb5cef791bb2673bb4092ef2abbeb)]:
  - slonik@48.6.0

## 48.5.0

### Patch Changes

- Updated dependencies [[`86d232c`](https://github.com/gajus/slonik/commit/86d232c20b092f59426ef9e90b250d2a69ab3eb7)]:
  - slonik@48.5.0

## 48.4.2

### Patch Changes

- Updated dependencies [[`a777bcf`](https://github.com/gajus/slonik/commit/a777bcfe14cae1e281f184063c268bb983b93c24)]:
  - slonik@48.4.2

## 48.4.1

### Patch Changes

- Updated dependencies [[`3cc5531`](https://github.com/gajus/slonik/commit/3cc5531ea17427efabf1dab5b23fadc6b6a3fe33)]:
  - slonik@48.4.1

## 48.4.0

### Patch Changes

- Updated dependencies [[`ae6bd40`](https://github.com/gajus/slonik/commit/ae6bd4070cedaca1fe6050f47e56d3a35b48a63a)]:
  - slonik@48.4.0

## 48.3.0

### Patch Changes

- Updated dependencies [[`14f39c3`](https://github.com/gajus/slonik/commit/14f39c396f1a9be3866211b37e79a0ae2d052d42)]:
  - slonik@48.3.0

## 48.2.0

### Patch Changes

- Updated dependencies [[`7b8e200`](https://github.com/gajus/slonik/commit/7b8e2003e3d3d7a0dae25548284a92ee3e94baea)]:
  - slonik@48.2.0

## 48.1.2

### Patch Changes

- Updated dependencies [[`c926df6`](https://github.com/gajus/slonik/commit/c926df636c922984adc431f3f0144eddc219ab88)]:
  - slonik@48.1.2

## 48.1.1

### Patch Changes

- Updated dependencies [[`491a515`](https://github.com/gajus/slonik/commit/491a515d2acb11f2ab0434b1f6adcec7da1379aa)]:
  - slonik@48.1.1

## 48.1.0

### Patch Changes

- Updated dependencies [[`b8e0936`](https://github.com/gajus/slonik/commit/b8e0936cc7c845803d8f20ada3c58bbc1906e125)]:
  - slonik@48.1.0

## 48.0.0

### Major Changes

- [#692](https://github.com/gajus/slonik/pull/692) [`31db3aa`](https://github.com/gajus/slonik/commit/31db3aa0f0f64cd2fadfc854815d2c0e346b75be) Thanks [@gajus](https://github.com/gajus)! - migrate to esm

### Patch Changes

- Updated dependencies [[`363cafb`](https://github.com/gajus/slonik/commit/363cafbffd69a64354ed0e23a56d88ac78af78cf), [`31db3aa`](https://github.com/gajus/slonik/commit/31db3aa0f0f64cd2fadfc854815d2c0e346b75be)]:
  - slonik@48.0.0

## 47.3.2

### Patch Changes

- Updated dependencies [[`ce93282`](https://github.com/gajus/slonik/commit/ce93282ff3da12c77f5e15e2b729a1de58beefd1)]:
  - slonik@47.3.2

## 47.3.1

### Patch Changes

- Updated dependencies [[`b7c9c34`](https://github.com/gajus/slonik/commit/b7c9c34116553c143feec9ae84df09ffe28c5db4)]:
  - slonik@47.3.1

## 47.3.0

### Patch Changes

- Updated dependencies [[`50ebfbe`](https://github.com/gajus/slonik/commit/50ebfbe04bf796519788e515b9092edd2dd1bd83)]:
  - slonik@47.3.0

## 47.2.1

### Patch Changes

- Updated dependencies [[`2225991`](https://github.com/gajus/slonik/commit/2225991d4d368d0b9181ea59def88455a77772ce)]:
  - slonik@47.2.1

## 47.2.0

### Patch Changes

- Updated dependencies [[`dbc7b15`](https://github.com/gajus/slonik/commit/dbc7b15b0f2d21638686777fe76947b4bf216bdf), [`0caecd5`](https://github.com/gajus/slonik/commit/0caecd5e1b2e03869229fc06783d3365eac6143b)]:
  - slonik@47.2.0

## 47.1.0

### Patch Changes

- Updated dependencies [[`8e8e819`](https://github.com/gajus/slonik/commit/8e8e819b029ca1d30a74779def57f49d6700f83f)]:
  - slonik@47.1.0

## 47.0.1

### Patch Changes

- Updated dependencies [[`97d6887`](https://github.com/gajus/slonik/commit/97d6887fd9fa0691c847238317c70a74e4d51895)]:
  - slonik@47.0.1

## 47.0.0

### Patch Changes

- Updated dependencies [[`1b4032c`](https://github.com/gajus/slonik/commit/1b4032c589cc8788a617d651be70720f2f60936a), [`cdd1d9a`](https://github.com/gajus/slonik/commit/cdd1d9a2c8d9b30ac21297ff71c45f52bb0f922c)]:
  - slonik@47.0.0

## 46.8.0

### Patch Changes

- Updated dependencies [[`60613bd`](https://github.com/gajus/slonik/commit/60613bd56bb2ab85c970dd20f35ef68bd09eeb22)]:
  - slonik@46.8.0

## 46.7.0

### Patch Changes

- Updated dependencies [[`ef65a7f`](https://github.com/gajus/slonik/commit/ef65a7fafe4e76c13c4a1a1e60f264ad9558f853)]:
  - slonik@46.7.0

## 46.6.1

### Patch Changes

- Updated dependencies [[`45bff8b`](https://github.com/gajus/slonik/commit/45bff8b901b6bc70d5fb397e38c49ca410bae6b8)]:
  - slonik@46.6.1

## 46.6.0

### Patch Changes

- Updated dependencies []:
  - slonik@46.6.0

## 46.5.0

### Patch Changes

- Updated dependencies []:
  - slonik@46.5.0

## 46.4.0

### Patch Changes

- Updated dependencies [[`a97891b`](https://github.com/gajus/slonik/commit/a97891b7f58cbc9af912654a78cf786a184620bf)]:
  - slonik@46.4.0

## 46.3.0

### Patch Changes

- Updated dependencies [[`960bf89`](https://github.com/gajus/slonik/commit/960bf891f8f280551cc405210ea87e8dca2ff278)]:
  - slonik@46.3.0

## 46.2.0

### Patch Changes

- Updated dependencies [[`c8f9741`](https://github.com/gajus/slonik/commit/c8f9741855d3a564b1709fb539cbf0a09610056e)]:
  - slonik@46.2.0

## 46.1.0

### Patch Changes

- Updated dependencies [[`97924d6`](https://github.com/gajus/slonik/commit/97924d663c8f948c70dc3f3a3248000e298627d7)]:
  - slonik@46.1.0

## 46.0.1

### Patch Changes

- [`a478df5`](https://github.com/gajus/slonik/commit/a478df56482e9f9ee6adc6489d101259c91fa89d) Thanks [@gajus](https://github.com/gajus)! - update lock file

- Updated dependencies [[`a478df5`](https://github.com/gajus/slonik/commit/a478df56482e9f9ee6adc6489d101259c91fa89d)]:
  - slonik@46.0.1

## 46.0.0

### Patch Changes

- Updated dependencies [[`c415b16`](https://github.com/gajus/slonik/commit/c415b16616871073fa0aa11a4965e2ba86db60a0), [`48263cd`](https://github.com/gajus/slonik/commit/48263cd4845aa89539bd7004ae195d1a968bbeb1)]:
  - slonik@46.0.0

## 45.6.0

### Patch Changes

- Updated dependencies [[`2968b32`](https://github.com/gajus/slonik/commit/2968b32bec2e9bd8f2f757dd830a730824bf0e47)]:
  - slonik@45.6.0

## 45.5.0

### Patch Changes

- Updated dependencies []:
  - slonik@45.5.0

## 45.4.1

### Patch Changes

- Updated dependencies []:
  - slonik@45.4.1

## 45.4.0

### Patch Changes

- Updated dependencies []:
  - slonik@45.4.0

## 45.3.0

### Patch Changes

- Updated dependencies []:
  - slonik@45.3.0

## 45.2.1

### Patch Changes

- Updated dependencies []:
  - slonik@45.2.1

## 45.2.0

### Patch Changes

- Updated dependencies []:
  - slonik@45.2.0

## 45.1.0

### Patch Changes

- Updated dependencies []:
  - slonik@45.1.0

## 45.0.0

### Patch Changes

- Updated dependencies [[`5525659`](https://github.com/gajus/slonik/commit/552565961fa65e9951e363a2388538713388c5b5)]:
  - slonik@45.0.0

## 44.0.0

### Patch Changes

- Updated dependencies [[`96db9f0`](https://github.com/gajus/slonik/commit/96db9f08faefb0e7da0cc0d817d9e8fae361e590)]:
  - slonik@44.0.0

## 43.0.8

### Patch Changes

- [`30f1dc4`](https://github.com/gajus/slonik/commit/30f1dc4469fe6065f90651c2e1c501d5374358c7) Thanks [@gajus](https://github.com/gajus)! - remove exports

- Updated dependencies [[`30f1dc4`](https://github.com/gajus/slonik/commit/30f1dc4469fe6065f90651c2e1c501d5374358c7)]:
  - slonik@43.0.8

## 43.0.7

### Patch Changes

- [`dba5be1`](https://github.com/gajus/slonik/commit/dba5be1b34868059c3f64a8dc44e48703625a3b9) Thanks [@gajus](https://github.com/gajus)! - corrects exports; adds more logging about pool state

- Updated dependencies [[`dba5be1`](https://github.com/gajus/slonik/commit/dba5be1b34868059c3f64a8dc44e48703625a3b9)]:
  - slonik@43.0.7

## 43.0.6

### Patch Changes

- [#591](https://github.com/gajus/slonik/pull/591) [`30e89a6`](https://github.com/gajus/slonik/commit/30e89a6f2ab1fc8f9d010bb0157ce41aa4da80e8) Thanks [@gajus](https://github.com/gajus)! - add slonik-interceptor-query-cache to monorepo

- Updated dependencies [[`30e89a6`](https://github.com/gajus/slonik/commit/30e89a6f2ab1fc8f9d010bb0157ce41aa4da80e8), [`30e89a6`](https://github.com/gajus/slonik/commit/30e89a6f2ab1fc8f9d010bb0157ce41aa4da80e8)]:
  - slonik@43.0.6

## 43.0.5

### Patch Changes

- [`d1958fd`](https://github.com/gajus/slonik/commit/d1958fd6acfcd48cc4148811106b63daf28b52a8) Thanks [@gajus](https://github.com/gajus)! - log how long it took to acquire a connection

- Updated dependencies [[`d1958fd`](https://github.com/gajus/slonik/commit/d1958fd6acfcd48cc4148811106b63daf28b52a8)]:
  - slonik@43.0.5

## 43.0.4

### Patch Changes

- [`d0d9a82`](https://github.com/gajus/slonik/commit/d0d9a82dee0980c4768d74e90e20491ada126816) Thanks [@gajus](https://github.com/gajus)! - use $slonik\_ bindings

- Updated dependencies [[`d0d9a82`](https://github.com/gajus/slonik/commit/d0d9a82dee0980c4768d74e90e20491ada126816)]:
  - slonik@43.0.4

## 43.0.3

### Patch Changes

- Updated dependencies [[`c9e261d`](https://github.com/gajus/slonik/commit/c9e261d8af6490ad84b450b6e4b598f662d92203), [`0f072df`](https://github.com/gajus/slonik/commit/0f072df5f3796fc2571c0e5e81405a36000ab9ec)]:
  - slonik@43.0.3

## 43.0.2

### Patch Changes

- Updated dependencies []:
  - slonik@43.0.2

## 43.0.1

### Patch Changes

- [`146a301`](https://github.com/gajus/slonik/commit/146a3011b6b9cbd1a3a5dbc7ce3a13d9cc6bb2ae) Thanks [@gajus](https://github.com/gajus)! - add missing type exports

- Updated dependencies [[`146a301`](https://github.com/gajus/slonik/commit/146a3011b6b9cbd1a3a5dbc7ce3a13d9cc6bb2ae)]:
  - slonik@43.0.1

## 43.0.0

### Patch Changes

- Updated dependencies [[`cb257c5`](https://github.com/gajus/slonik/commit/cb257c55a72ce82364ce1e3bf787e4cc2a517989), [`8c58884`](https://github.com/gajus/slonik/commit/8c588849338dbc626d661a04af9f162a791f3e31)]:
  - slonik@43.0.0

```

### File: packages\errors\CHANGELOG.md
```md
# @slonik/errors

## 48.13.2

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.13.2

## 48.13.1

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.13.1

## 48.13.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.13.0

## 48.12.3

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.12.3

## 48.12.2

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.12.2

## 48.12.1

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.12.1

## 48.12.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.12.0

## 48.11.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.11.0

## 48.10.3

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.10.3

## 48.10.2

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.10.2

## 48.10.1

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.10.1

## 48.10.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.10.0

## 48.9.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.9.0

## 48.8.12

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.8.12

## 48.8.11

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.8.11

## 48.8.10

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.8.10

## 48.8.9

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.8.9

## 48.8.8

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.8.8

## 48.8.7

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.8.7

## 48.8.6

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.8.6

## 48.8.5

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.8.5

## 48.8.4

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.8.4

## 48.8.3

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.8.3

## 48.8.2

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.8.2

## 48.8.1

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.8.1

## 48.8.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.8.0

## 48.7.1

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.7.1

## 48.7.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.7.0

## 48.6.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.6.0

## 48.5.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.5.0

## 48.4.2

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.4.2

## 48.4.1

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.4.1

## 48.4.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.4.0

## 48.3.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.3.0

## 48.2.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.2.0

## 48.1.2

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.1.2

## 48.1.1

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.1.1

## 48.1.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@48.1.0

## 48.0.0

### Major Changes

- [#692](https://github.com/gajus/slonik/pull/692) [`31db3aa`](https://github.com/gajus/slonik/commit/31db3aa0f0f64cd2fadfc854815d2c0e346b75be) Thanks [@gajus](https://github.com/gajus)! - migrate to esm

### Patch Changes

- Updated dependencies [[`31db3aa`](https://github.com/gajus/slonik/commit/31db3aa0f0f64cd2fadfc854815d2c0e346b75be)]:
  - @slonik/types@48.0.0

## 47.3.2

### Patch Changes

- Updated dependencies []:
  - @slonik/types@47.3.2

## 47.3.1

### Patch Changes

- Updated dependencies []:
  - @slonik/types@47.3.1

## 47.3.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@47.3.0

## 47.2.1

### Patch Changes

- Updated dependencies []:
  - @slonik/types@47.2.1

## 47.2.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@47.2.0

## 47.1.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@47.1.0

## 47.0.1

### Patch Changes

- Updated dependencies []:
  - @slonik/types@47.0.1

## 47.0.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@47.0.0

## 46.8.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@46.8.0

## 46.7.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@46.7.0

## 46.6.1

### Patch Changes

- Updated dependencies []:
  - @slonik/types@46.6.1

## 46.6.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@46.6.0

## 46.5.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@46.5.0

## 46.4.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@46.4.0

## 46.3.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@46.3.0

## 46.2.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@46.2.0

## 46.1.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@46.1.0

## 46.0.1

### Patch Changes

- [`a478df5`](https://github.com/gajus/slonik/commit/a478df56482e9f9ee6adc6489d101259c91fa89d) Thanks [@gajus](https://github.com/gajus)! - update lock file

- Updated dependencies [[`a478df5`](https://github.com/gajus/slonik/commit/a478df56482e9f9ee6adc6489d101259c91fa89d)]:
  - @slonik/types@46.0.1

## 46.0.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@46.0.0

## 45.6.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@45.6.0

## 45.5.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@45.5.0

## 45.4.1

### Patch Changes

- Updated dependencies []:
  - @slonik/types@45.4.1

## 45.4.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@45.4.0

## 45.3.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@45.3.0

## 45.2.1

### Patch Changes

- Updated dependencies []:
  - @slonik/types@45.2.1

## 45.2.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@45.2.0

## 45.1.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@45.1.0

## 45.0.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@45.0.0

## 44.0.0

### Patch Changes

- Updated dependencies []:
  - @slonik/types@44.0.0

## 43.0.8

### Patch Changes

- [`30f1dc4`](https://github.com/gajus/slonik/commit/30f1dc4469fe6065f90651c2e1c501d5374358c7) Thanks [@gajus](https://github.com/gajus)! - remove exports

- Updated dependencies [[`30f1dc4`](https://github.com/gajus/slonik/commit/30f1dc4469fe6065f90651c2e1c501d5374358c7)]:
  - @slonik/types@43.0.8

## 43.0.7

### Patch Changes

- [`dba5be1`](https://github.com/gajus/slonik/commit/dba5be1b34868059c3f64a8dc44e48703625a3b9) Thanks [@gajus](https://github.com/gajus)! - corrects exports; adds more logging about pool state

- Updated dependencies [[`dba5be1`](https://github.com/gajus/slonik/commit/dba5be1b34868059c3f64a8dc44e48703625a3b9)]:
  - @slonik/types@43.0.7

## 43.0.6

### Patch Changes

- [#591](https://github.com/gajus/slonik/pull/591) [`30e89a6`](https://github.com/gajus/slonik/commit/30e89a6f2ab1fc8f9d010bb0157ce41aa4da80e8) Thanks [@gajus](https://github.com/gajus)! - add slonik-interceptor-query-cache to monorepo

- Updated dependencies [[`30e89a6`](https://github.com/gajus/slonik/commit/30e89a6f2ab1fc8f9d010bb0157ce41aa4da80e8), [`30e89a6`](https://github.com/gajus/slonik/commit/30e89a6f2ab1fc8f9d010bb0157ce41aa4da80e8)]:
  - @slonik/types@43.0.6

## 43.0.5

### Patch Changes

- [`d1958fd`](https://github.com/gajus/slonik/commit/d1958fd6acfcd48cc4148811106b63daf28b52a8) Thanks [@gajus](https://github.com/gajus)! - log how long it took to acquire a connection

- Updated dependencies [[`d1958fd`](https://github.com/gajus/slonik/commit/d1958fd6acfcd48cc4148811106b63daf28b52a8)]:
  - @slonik/types@43.0.5

## 43.0.4

### Patch Changes

- [`d0d9a82`](https://github.com/gajus/slonik/commit/d0d9a82dee0980c4768d74e90e20491ada126816) Thanks [@gajus](https://github.com/gajus)! - use $slonik\_ bindings

- Updated dependencies [[`d0d9a82`](https://github.com/gajus/slonik/commit/d0d9a82dee0980c4768d74e90e20491ada126816)]:
  - @slonik/types@43.0.4

## 43.0.3

### Patch Changes

- Updated dependencies []:
  - @slonik/types@43.0.3

## 43.0.2

### Patch Changes

- Updated dependencies []:
  - @slonik/types@43.0.2

## 43.0.1

### Patch Changes

- [`146a301`](https://github.com/gajus/slonik/commit/146a3011b6b9cbd1a3a5dbc7ce3a13d9cc6bb2ae) Thanks [@gajus](https://github.com/gajus)! - add missing type exports

- Updated dependencies [[`146a301`](https://github.com/gajus/slonik/commit/146a3011b6b9cbd1a3a5dbc7ce3a13d9cc6bb2ae)]:
  - @slonik/types@43.0.1

## 43.0.0

### Minor Changes

- [`8c58884`](https://github.com/gajus/slonik/commit/8c588849338dbc626d661a04af9f162a791f3e31) Thanks [@gajus](https://github.com/gajus)! - force version bump

### Patch Changes

- [`cb257c5`](https://github.com/gajus/slonik/commit/cb257c55a72ce82364ce1e3bf787e4cc2a517989) Thanks [@gajus](https://github.com/gajus)! - correct createSqlTokenSqlFragment export

- Updated dependencies [[`cb257c5`](https://github.com/gajus/slonik/commit/cb257c55a72ce82364ce1e3bf787e4cc2a517989), [`8c58884`](https://github.com/gajus/slonik/commit/8c588849338dbc626d661a04af9f162a791f3e31)]:
  - @slonik/types@43.0.0

## 41.3.0

### Minor Changes

- [`fb83bd9`](https://github.com/gajus/slonik/commit/fb83bd900b85b5e672db49694a8171b9296c252c) Thanks [@gajus](https://github.com/gajus)! - force update version

### Patch Changes

- Updated dependencies [[`fb83bd9`](https://github.com/gajus/slonik/commit/fb83bd900b85b5e672db49694a8171b9296c252c)]:
  - @slonik/types@41.3.0

## 40.2.5

### Patch Changes

- [`ef802a9`](https://github.com/gajus/slonik/commit/ef802a91be2bc6e69b077c544cc7f9e5a2687433) Thanks [@gajus](https://github.com/gajus)! - force patch bump

- Updated dependencies [[`ef802a9`](https://github.com/gajus/slonik/commit/ef802a91be2bc6e69b077c544cc7f9e5a2687433)]:
  - @slonik/types@40.2.5

## 40.2.4

### Patch Changes

- [`c1064fc`](https://github.com/gajus/slonik/commit/c1064fc3f21f839effc1687737942332a7c05b0d) Thanks [@gajus](https://github.com/gajus)! - update access

- Updated dependencies [[`c1064fc`](https://github.com/gajus/slonik/commit/c1064fc3f21f839effc1687737942332a7c05b0d)]:
  - @slonik/types@40.2.4

## 40.2.3

### Patch Changes

- [#577](https://github.com/gajus/slonik/pull/577) [`4007ab7`](https://github.com/gajus/slonik/commit/4007ab7e07d5b71e8f41e145584979fa36885275) Thanks [@gajus](https://github.com/gajus)! - abstract packages using internal modules

- [#579](https://github.com/gajus/slonik/pull/579) [`2779fd1`](https://github.com/gajus/slonik/commit/2779fd15ddae35b9830f4c156648e444cd793f13) Thanks [@gajus](https://github.com/gajus)! - add slonik-sql-tag-raw

- Updated dependencies [[`4007ab7`](https://github.com/gajus/slonik/commit/4007ab7e07d5b71e8f41e145584979fa36885275), [`2779fd1`](https://github.com/gajus/slonik/commit/2779fd15ddae35b9830f4c156648e444cd793f13)]:
  - @slonik/types@40.2.3

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

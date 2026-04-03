---
id: talyssonoc-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:20.932478
---

# KNOWLEDGE EXTRACT: talyssonoc
> **Extracted on:** 2026-03-30 17:54:14
> **Source:** talyssonoc

---

## File: `node-api-boilerplate.md`
```markdown
# 📦 talyssonoc/node-api-boilerplate [🔖 PENDING/APPROVE]
🔗 https://github.com/talyssonoc/node-api-boilerplate
🌐 https://github.com/talyssonoc/node-api-boilerplate/wiki

## Meta
- **Stars:** ⭐ 3360 | **Forks:** 🍴 533
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
DDD/Clean Architecture inspired boilerplate for Node web APIs

## README (trích đầu)
```
# What is it

This project is a starting point for you to develop a web API in a scalable way with Node and TypeScript, and was implemented following ideas from layered architecture, Clean Architecture, and Domain-Driven Design. While it contains an opinionated design and structure, it was built to be extensible and flexible so you can modify and adapt it according to your team's needs and preferences.

This version of the boilerplate is still in beta, so might contain abstractions that will change or be missing features. Contribution from the community, either through PRs or is welcome.

**Important** This is the documentation for the v3 of the boilerplate. Click here if you want the [docs for the v2.1](https://github.com/talyssonoc/node-api-boilerplate/tree/v2.1).

# Usage

## How to run the server

During development, the project can be run in two different ways.

If you want to just run the application in development mode, use the following command:

```sh
$ yarn dev

```

To run the application in debug mode in a way that the execution will stop when a debugger statement is called, use:

```sh
$ yarn debug
```

## How to run the application console

You can also run the application in console mode, giving you programmatic access to the environment, this can also be done in two different ways.

To run a new instance, isolated from the server, use the following command:

```sh
$ yarn cli
```

For the new instance, you're able to access the dependencies registered in the container using `registry.<dependencyName>` or through the `container` variable.

But if you're already running the server (this is a requirement) and you want to a console connected to the process of the server, giving you access to the current state of it, use:

```sh
$ yarn remote [server address] [REPL port]
```

## Tests

The boilerplate is prepared to run tests using Jest. We usually group the tests in folders called `__tests__` (following Jest convention) for each module of the application. To run the tests use the following command:

```sh
$ yarn test
```

## Docker wrapper

In case you want to use Docker to run it, this project includes a [docker wrapper](https://github.com/brunohcastro/node-base) for development. Any command can be executed by calling the scripts under the `dbin/` folder.

```sh
$ dbin/yarn dev

$ dbin/yarn debug

$ dbin/yarn cli

$ dbin/yarn remote [server address] [REPL port]

$ dbin/yarn test
```

The container runs using host networking, so there's no need to map ports. Keep in mind that environment variables should be added to the docker-compose.yml.

### Wrapper commands

```sh
# Runs the command inside an ephemeral container using the app service described in the docker-compose file as a base (use the --root flag if the command should be run as root)
$ dbin/run [--root] <command>

# Rebuild the image after any changes to the dockerfile
$ dbin/build

# Remove all containers and their volumes (WARNING any cache or files not stored in the filesyst
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


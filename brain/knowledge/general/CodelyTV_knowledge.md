---
id: codelytv-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:08.098954
---

# KNOWLEDGE EXTRACT: CodelyTV
> **Extracted on:** 2026-03-30 17:34:53
> **Source:** CodelyTV

---

## File: `java-ddd-example.md`
```markdown
# 📦 CodelyTV/java-ddd-example [🔖 PENDING/APPROVE]
🔗 https://github.com/CodelyTV/java-ddd-example
🌐 https://pro.codely.tv/library/ddd-en-java/about/

## Meta
- **Stars:** ⭐ 500 | **Forks:** 🍴 217
- **Language:** Java | **License:** Unknown
- **Last updated:** 2026-03-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
♨️ DDD in Java skeleton & examples. Course:

## README (trích đầu)
```
<p align="center">
  <a href="https://codely.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://codely.com/logo/codely_logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://codely.com/logo/codely_logo-light.svg">
      <img alt="Codely logo" src="https://codely.com/logo/codely_logo.svg">
    </picture>
  </a>
</p>

<h1 align="center">
  ☕🚀 Java DDD example: Save the boilerplate in your new projects
</h1>

<p align="center">
    <a href="https://github.com/CodelyTV"><img src="https://img.shields.io/badge/Codely-OS-green.svg?style=flat-square" alt="Codely Open Source projects"/></a>
    <a href="https://pro.codely.com"><img src="https://img.shields.io/badge/Codely-Pro-black.svg?style=flat-square" alt="Codely Pro courses"/></a>
    <a href="https://github.com/CodelyTV/java-ddd-example/actions"><img src="https://github.com/CodelyTV/java-ddd-example/workflows/CI/badge.svg" alt="CI pipeline status"></a>
</p>

> ⚡ Start your Java projects as fast as possible

## ℹ️ Introduction

This is a repository intended to serve as a starting point if you want to bootstrap a Java project with JUnit and Gradle.

Here you have the [course on CodelyTV Pro where we explain step by step all this](https://pro.codely.tv/library/ddd-en-java/about/?utm_source=github&utm_medium=social&utm_campaign=readme) (Spanish)

## 🏁 How To Start

1. Install Java 11: `brew cask install corretto`
2. Set it as your default JVM: `export JAVA_HOME='/Library/Java/JavaVirtualMachines/amazon-corretto-11.jdk/Contents/Home'`
3. Clone this repository: `git clone https://github.com/CodelyTV/java-ddd-example`.
4. Bring up the Docker environment: `make up`.
5. Execute some [Gradle lifecycle tasks](https://docs.gradle.org/current/userguide/java_plugin.html#lifecycle_tasks) in order to check everything is OK:
    1. Create [the project JAR](https://docs.gradle.org/current/userguide/java_plugin.html#sec:jar): `make build`
    2. Run the tests and plugins verification tasks: `make test`
6. Start developing!

## ☝️ How to update dependencies

* Gradle ([releases](https://gradle.org/releases/)): `./gradlew wrapper --gradle-version=WANTED_VERSION --distribution-type=bin`

## 💡 Related repositories

### ☕ Java

* 📂 [Java Basic example](https://github.com/CodelyTV/java-basic-example)
* ⚛ [Java OOP Examples](https://github.com/CodelyTV/java-oop-examples)
* 🧱 [Java SOLID Examples](https://github.com/CodelyTV/java-solid-examples)
* 🥦 [Java DDD Example](https://github.com/CodelyTV/java-ddd-example)

### 🐘 PHP

* 📂 [PHP Basic example](https://github.com/CodelyTV/php-basic-example)
* 🎩 [PHP DDD example](https://github.com/CodelyTV/php-ddd-example)
* 🥦 [PHP DDD Example](https://github.com/CodelyTV/php-ddd-example)

### 🧬 Scala

* 📂 [Scala Basic example](https://github.com/CodelyTV/scala-basic-example)
* ⚡ [Scala Basic example (g8 template)](https://github.com/CodelyTV/scala-basic-example.g8)
* ⚛ [Scala Examples](https://github.com/CodelyTV/scala-examp
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `php-ddd-example.md`
```markdown
# 📦 CodelyTV/php-ddd-example [🔖 PENDING/APPROVE]
🔗 https://github.com/CodelyTV/php-ddd-example
🌐 https://pro.codely.tv/library/ddd-en-php

## Meta
- **Stars:** ⭐ 3135 | **Forks:** 🍴 1090
- **Language:** PHP | **License:** Unknown
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
🐘🎯 Hexagonal Architecture + DDD + CQRS in PHP using Symfony 7

## README (trích đầu)
```
<p align="center">
  <a href="https://codely.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://codely.com/logo/codely_logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://codely.com/logo/codely_logo-light.svg">
      <img alt="Codely logo" src="https://codely.com/logo/codely_logo.svg">
    </picture>
  </a>
</p>

<h1 align="center">
  🐘🎯 Hexagonal Architecture, DDD & CQRS in PHP
</h1>

<p align="center">
    <a href="https://github.com/CodelyTV"><img src="https://img.shields.io/badge/Codely-OS-green.svg?style=flat-square" alt="Codely Open Source projects"/></a>
    <a href="http://pro.codely.tv"><img src="https://img.shields.io/badge/CodelyTV-PRO-black.svg?style=flat-square" alt="CodelyTV Courses"/></a>
    <a href="#"><img src="https://img.shields.io/badge/Symfony-7-purple.svg?style=flat-square&logo=symfony" alt="Symfony 7"/></a>
    <a href="https://shepherd.dev/github/CodelyTV/php-ddd-example"><img src="https://shepherd.dev/github/CodelyTV/php-ddd-example/coverage.svg" alt="Type Coverage"/></a>
    <a href="https://github.com/CodelyTV/php-ddd-example/actions"><img src="https://github.com/CodelyTV/php-ddd-example/workflows/CI/badge.svg?branch=master" alt="CI pipeline status" /></a>
</p>

<p align="center">
  Example of a <strong>PHP application using Domain-Driven Design (DDD) and Command Query Responsibility Segregation
  (CQRS) principles</strong> keeping the code as simple as possible.
  <br />
  <br />
  Take a look, play and have fun with this.
  <a href="https://github.com/CodelyTV/php-ddd-example/stargazers">Stars are welcome 😊</a>
  <br />
  <br />
  <a href="https://www.youtube.com/watch?v=1kaP39W80zQ">View Demo</a>
  ·
  <a href="https://github.com/CodelyTV/php-ddd-example/issues">Report a bug</a>
  ·
  <a href="https://github.com/CodelyTV/php-ddd-example/issues">Request a feature</a>
</p>

## 🚀 Environment Setup

### 🐳 Needed tools

1. [Install Docker](https://www.docker.com/get-started)
2. Clone this project: `git clone https://github.com/CodelyTV/php-ddd-example php-ddd-example`
3. Move to the project folder: `cd php-ddd-example`

### 🛠️ Environment configuration

1. Create a local environment file (`cp .env .env.local`) if you want to modify any parameter

### 🔥 Application execution

1. Install all the dependencies and bring up the project with Docker executing: `make build`
2. Then you'll have 3 apps available (2 APIs and 1 Frontend):
   1. [Mooc Backend](apps/mooc/backend): http://localhost:8030/health-check
   2. [Backoffice Backend](apps/backoffice/backend): http://localhost:8040/health-check
   3. [Backoffice Frontend](apps/backoffice/frontend): http://localhost:8041/health-check

### ✅ Tests execution

1. Install the dependencies if you haven't done it previously: `make deps`
2. Execute PHPUnit and Behat tests: `make test`

## 👩‍💻 Project explanation

This project tries to be a MOOC (Massive Open Online Course) platform. It's decoupled from any framework, b
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `typescript-api-skeleton.md`
```markdown
# 📦 CodelyTV/typescript-api-skeleton [🔖 PENDING/APPROVE]
🔗 https://github.com/CodelyTV/typescript-api-skeleton
🌐 https://pro.codely.tv/library/de-javascript-a-typescript-128106/347481/about/

## Meta
- **Stars:** ⭐ 204 | **Forks:** 🍴 38
- **Language:** TypeScript | **License:** Unknown
- **Last updated:** 2026-03-08
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
🔷🌍 TypeScript API Skeleton: Bootstrap your new HTTP API backend with TypeScript

## README (trích đầu)
```
# TypeScript Express API Bootstrap (base / project starter)

This is a repository intended to serve as a starting point if you want to bootstrap a express API project in TypeScript.

## Features

- [TypeScript](https://www.typescriptlang.org/) (v4)
- [ts-node-dev](https://github.com/wclr/ts-node-dev)
- [Prettier](https://prettier.io/)
- [ESLint](https://eslint.org/) with:
  - [Codely's config](https://github.com/lydell/eslint-plugin-simple-import-sort/) (includes ESLint's recommended rules, Prettier, Import plugin and more)
  - [Jest plugin](https://www.npmjs.com/package/eslint-plugin-jest)
- [Jest](https://jestjs.io) with [DOM Testing Library](https://testing-library.com/brain/knowledge/docs_legacy/dom-testing-library/intro)
- [GitHub Action workflows](https://github.com/features/actions) set up to run tests and linting on push

## Running the app

```
# install dependencies
npm install

# run in dev mode on port 3000
npm run dev

# generate production build
npm run build

# run generated content in dist folder on port 3000
npm run start
```

## Testing

### Jest with supertest

```
npm run test
```

## Linting

```
# run linter
npm run lint

# fix lint issues
npm run lint:fix
```

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `typescript-ddd-example.md`
```markdown
# 📦 CodelyTV/typescript-ddd-example [🔖 PENDING/APPROVE]
🔗 https://github.com/CodelyTV/typescript-ddd-example
🌐 https://pro.codely.tv/library/ddd-typescript/375662/about/

## Meta
- **Stars:** ⭐ 1459 | **Forks:** 🍴 231
- **Language:** TypeScript | **License:** Unknown
- **Last updated:** 2026-03-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
🔷🎯 TypeScript DDD Example: Complete project applying Hexagonal Architecture and Domain-Driven Design patterns

## README (trích đầu)
```
<p align="center">
  <a href="https://codely.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://codely.com/logo/codely_logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://codely.com/logo/codely_logo-light.svg">
      <img alt="Codely logo" src="https://codely.com/logo/codely_logo.svg">
    </picture>
  </a>
</p>

<h1 align="center">
  🐘🎯 Hexagonal Architecture, DDD & CQRS in Typescript
</h1>

<p align="center">
    <a href="https://github.com/CodelyTV"><img src="https://img.shields.io/badge/CodelyTV-OS-green.svg?style=flat-square" alt="codely.tv"/></a>
    <a href="http://pro.codely.tv"><img src="https://img.shields.io/badge/CodelyTV-PRO-black.svg?style=flat-square" alt="CodelyTV Courses"/></a>
</p>

<p align="center">
  Example of a Typescript application following Domain-Driven Design (DDD),
  Command Query Responsibility Segregation (CQRS) and
  Event-Driven Architecture (EDA) principles keeping the code as simple as possible.

</p>

# 🔀 Related utilities and resources

## ☝️ Learning resources

- [🔖 Domain-Driven Design en TypeScript: Modelado y Arquitectura](https://pro.codely.tv/library/ddd-en-typescript-modelado-y-arquitectura-172533/375662/about/) (Spanish - Course)
- [️️🛰️ DDD en TypeScript: Comunicación entre servicios y aplicaciones](https://pro.codely.com/library/comunicacion-entre-microservicios-event-driven-architecture-35834) (Spanish - Course)
- [🏗️ De JavaScript a TypeScript](https://pro.codely.tv/library/de-javascript-a-typescript-128106/347481/about/) (Spanish - Course)
- [📂 DDD en TypeScript: Estructura de carpetas](https://youtu.be/AJJRk7qmVHg) (Spanish - YouTube video)

## 🔷 TypeScript skeletons


- [🌱 TypeScript Basic Skeleton](https://github.com/CodelyTV/typescript-basic-skeleton): Bootstrap your new TypeScript frontend project
- [🌍 TypeScript API Skeleton](https://github.com/CodelyTV/typescript-api-skeleton): Bootstrap your new TypeScript backend project
- [️🗿 TypeScript DDD Skeleton](https://github.com/CodelyTV/typescript-ddd-skeleton): Bootstrap your new TypeScript DDD project

## 🌈 TypeScript Domain-Driven Design repositories

- [✨ TypeScript DDD Skeleton](https://github.com/CodelyTV/typescript-ddd-skeleton): Bootstrap your new TypeScript projects applying Hexagonal Architecture and Domain-Driven Design patterns
- [🔖 TypeScript DDD Course](https://github.com/CodelyTV/typescript-ddd-course): Learn Domain-Driven Design in TS lesson by lesson
- [🎯 TypeScript DDD Example](https://github.com/CodelyTV/typescript-ddd-example): Complete project applying Hexagonal Architecture and Domain-Driven Design patterns

## 🎯 Other languages Domain-Driven Design repositories

- [☕🎯 Java DDD Example](https://github.com/CodelyTV/java-ddd-example)
- [🐘🎯 PHP DDD Example](https://github.com/CodelyTV/php-ddd-example)
- [λ🎯 Scala DDD Example](https://github.com/CodelyTV/scala-ddd-example)
- [🦈✨ C# DDD Skeleton](https://github.com/CodelyTV/csharp-ddd-skeleton)

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `typescript-ddd-skeleton.md`
```markdown
# 📦 CodelyTV/typescript-ddd-skeleton [🔖 PENDING/APPROVE]
🔗 https://github.com/CodelyTV/typescript-ddd-skeleton
🌐 https://pro.codely.tv/library/ddd-typescript/375662/about/

## Meta
- **Stars:** ⭐ 474 | **Forks:** 🍴 54
- **Language:** TypeScript | **License:** Unknown
- **Last updated:** 2026-03-14
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
🔷✨ TypeScript DDD Skeleton: Bootstrap your new TypeScript project applying Hexagonal Architecture and Domain-Driven Design patterns

## README (trích đầu)
```
# TypeScript basic skeleton

For now, you have all the code example available in this other repository: https://github.com/CodelyTV/typescript-ddd-example

The idea is that we'll move the basic parts (folder structure and bare minimum code to serve as skeleton) to this repository (`typescript-ddd-skeleton`) once we completely finish the `typescript-ddd-example` code. Current progress: ~95%

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


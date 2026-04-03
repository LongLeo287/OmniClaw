---
id: sairyss-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:10.582255
---

# KNOWLEDGE EXTRACT: Sairyss
> **Extracted on:** 2026-03-30 17:53:03
> **Source:** Sairyss

---

## File: `backend-best-practices.md`
```markdown
# 📦 Sairyss/backend-best-practices [🔖 PENDING/APPROVE]
🔗 https://github.com/Sairyss/backend-best-practices


## Meta
- **Stars:** ⭐ 2255 | **Forks:** 🍴 177
- **Language:** N/A | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Best practices, tools and guidelines for backend development. Code examples in TypeScript + NodeJS

## README (trích đầu)
```
# Backend best practices

**Check out my other repositories**:

- [Domain-Driven Hexagon](https://github.com/Sairyss/domain-driven-hexagon) - Guide on Domain-Driven Design, software architecture, design patterns, best practices etc.
- [System Design Patterns](https://github.com/Sairyss/system-design-patterns) - list of topics and resources related to distributed systems, system design, microservices, scalability and performance, etc.
- [Full Stack starter template](https://github.com/Sairyss/fullstack-starter-template) - template for full stack applications based on TypeScript, React, Vite, ChakraUI, tRPC, Fastify, Prisma, zod, etc.

---

In this readme are presented some of the best practices, tools and guidelines for backend applications gathered from different sources.

This Readme contains code examples mainly for TypeScript + NodeJS, but practices described here are language agnostic and can be used in any backend project.

---

- [Backend best practices](#backend-best-practices)
  - [Architecture](#architecture)
  - [API Security](#api-security)
    - [Data Validation](#data-validation)
    - [Enforce least privilege](#enforce-least-privilege)
    - [Rate Limiting](#rate-limiting)
  - [Testing](#testing)
    - [White box vs Black box](#white-box-vs-black-box)
    - [Load Testing](#load-testing)
    - [Fuzz Testing](#fuzz-testing)
  - [Documentation](#documentation)
    - [Document APIs](#document-apis)
    - [Use wiki](#use-wiki)
    - [Add Readme](#add-readme)
    - [Write self-documenting code](#write-self-documenting-code)
    - [Prefer statically typed languages](#prefer-statically-typed-languages)
    - [Avoid useless comments](#avoid-useless-comments)
  - [Database Best Practices](#database-best-practices)
    - [Backups](#backups)
    - [Managing Schema Changes](#managing-schema-changes)
    - [Data Seeding](#data-seeding)
  - [Configuration](#configuration)
  - [Logging](#logging)
  - [Monitoring](#monitoring)
    - [Telemetry](#telemetry)
  - [Standardization](#standardization)
  - [Static Code Analysis](#static-code-analysis)
  - [Code formatting](#code-formatting)
  - [Shut down gracefully](#shut-down-gracefully)
  - [Profiling](#profiling)
  - [Benchmarking](#benchmarking)
  - [Make application easy to setup](#make-application-easy-to-setup)
  - [Deployment](#deployment)
    - [Blue-Green Deployment](#blue-green-deployment)
  - [Code Generation](#code-generation)
  - [Version Control](#version-control)
    - [Pre-push/pre-commit hooks](#pre-pushpre-commit-hooks)
    - [Conventional commits](#conventional-commits)
  - [API Versioning](#api-versioning)
- [Additional resources](#additional-resources)
  - [Github Repositories](#github-repositories)

## Architecture

Software architecture is about making fundamental choices of your application structure.

> Architecture serves as a blueprint for a system. It provides an abstraction to manage the system complexity and establish a communication and coordination mechanism among componen
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `domain-driven-hexagon.md`
```markdown
# 📦 Sairyss/domain-driven-hexagon [🔖 PENDING/APPROVE]
🔗 https://github.com/Sairyss/domain-driven-hexagon


## Meta
- **Stars:** ⭐ 14503 | **Forks:** 🍴 1529
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Learn Domain-Driven Design, software architecture, design patterns, best practices. Code examples included

## README (trích đầu)
```
# Domain-Driven Hexagon

**Check out my other repositories**:

- [Backend best practices](https://github.com/Sairyss/backend-best-practices) - Best practices, tools and guidelines for backend development.
- [System Design Patterns](https://github.com/Sairyss/system-design-patterns) - list of topics and resources related to distributed systems, system design, microservices, scalability and performance, etc.
- [Full Stack starter template](https://github.com/Sairyss/fullstack-starter-template) - template for full stack applications based on TypeScript, React, Vite, ChakraUI, tRPC, Fastify, Prisma, zod, etc.

---

The main emphasis of this project is to provide recommendations on how to design software applications. This readme includes techniques, tools, best practices, architectural patterns and guidelines gathered from different sources.

Code examples are written using [NodeJS](https://nodejs.org/en/), [TypeScript](https://www.typescriptlang.org/), [NestJS](https://docs.nestjs.com/) framework and [Slonik](https://github.com/gajus/slonik) for the database access.

Patterns and principles presented here are **framework/language agnostic**. Therefore, the above technologies can be easily replaced with any alternative. No matter what language or framework is used, any application can benefit from principles described below.

**Note**: code examples are adapted to TypeScript and frameworks mentioned above. <br/>
(Implementations in other languages will look differently)

**Everything below is provided as a recommendation, not a rule**. Different projects have different requirements, so any pattern mentioned in this readme should be adjusted to project needs or even skipped entirely if it doesn't fit. In real world production applications, you will most likely only need a fraction of those patterns depending on your use cases. More info in [this](#general-recommendations-on-architectures-best-practices-design-patterns-and-principles) section.

---

- [Domain-Driven Hexagon](#domain-driven-hexagon)
- [Architecture](#architecture)
      - [Pros](#pros)
      - [Cons](#cons)
- [Diagram](#diagram)
- [Modules](#modules)
- [Application Core](#application-core)
- [Application layer](#application-layer)
  - [Application Services](#application-services)
  - [Commands and Queries](#commands-and-queries)
    - [Commands](#commands)
    - [Queries](#queries)
  - [Ports](#ports)
- [Domain Layer](#domain-layer)
  - [Entities](#entities)
  - [Aggregates](#aggregates)
  - [Domain Events](#domain-events)
  - [Integration Events](#integration-events)
  - [Domain Services](#domain-services)
  - [Value objects](#value-objects)
  - [Domain Invariants](#domain-invariants)
    - [Replacing primitives with Value Objects](#replacing-primitives-with-value-objects)
    - [Make illegal states unrepresentable](#make-illegal-states-unrepresentable)
      - [Validation at compile time](#validation-at-compile-time)
      - [Validation at runtime](#validation-at-runtime)
    - [Guard
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `fullstack-starter-template.md`
```markdown
# 📦 Sairyss/fullstack-starter-template [🔖 PENDING/APPROVE]
🔗 https://github.com/Sairyss/fullstack-starter-template


## Meta
- **Stars:** ⭐ 322 | **Forks:** 🍴 71
- **Language:** TypeScript | **License:** Unknown
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Template for full stack applications based on TypeScript, React, Vite, ChakraUI, tRPC, Fastify, Prisma, zod, etc.

## README (trích đầu)
```
# Full stack starter template

Monorepository TypeScript template for full stack applications.

- Maximized for productivity
- Based on cutting edge technologies
- Follows best practices for project structure, architecture, security
- Includes authentication module

## Libraries/frameworks

This template includes a bunch of libraries to get you up and running quickly and improve your developer experience.

### Frontend

- [React](https://reactjs.org/) - main frontend library
- [Vite](https://vitejs.dev/) - modern and fast build tool
- [React Query](https://react-query-v3.tanstack.com/) - react hooks to facilitate fetching/updating/caching data on the server
- [Zustand](https://github.com/pmndrs/zustand) - easy state-management
- [React router](https://reactrouter.com/en/main) - for routing
- [Cypress](https://www.cypress.io/) - end-to-end testing for your frontend
- [Storybook](https://storybook.js.org/) - build your UI web components in isolation

#### Frontend UI

- [ChakraUI](https://chakra-ui.com/) - UI library that lets you create beautiful interfaces quickly
- [Framer Motion](https://www.framer.com/motion/) - create beautiful motion animations ([compatible with ChakraUI](https://chakra-ui.com/getting-started/with-framer))
- [React Icons](https://react-icons.github.io/react-icons/) - icons for your app
- [React-toastify](https://fkhadra.github.io/react-toastify/introduction) - show notifications when something happens

### Backend

- [Fastify](https://www.fastify.io/) - fast web framework for NodeJS
- [Prisma](https://www.prisma.io/) - new generation ORM for working with relational databases
- [Zod](https://github.com/colinhacks/zod) - TypeScript-first schema validation with static type inference
- [dotenv](https://www.npmjs.com/package/dotenv) - to load your configs from an .env file
- [env-var](https://www.npmjs.com/package/env-var) - validate and sanitize your environmental variables

### Shared libraries

- [tRPC](https://trpc.io/) - Remote Procedure Calls for your TypeScript applications. Move faster by removing the need of a traditional API-layer.
- [NX](https://nx.dev/) - build system with first class monorepo support and powerful integrations
- [Jest](https://jestjs.io/) - testing framework
- [Eslint](https://eslint.org/) - static code analysis for identifying problematic patterns found in your code

## Starting the app

- Clone the repository
- Copy `.env.example` and rename to `.env`
- `npm run docker:env` - setup the database (postgresql) in docker
- `npm install` - install dependencies
- `npm run migrate:dev` - run migrations to create tables
- `npm run backend:dev` - run backend
- `npm run frontend:dev` - run frontend

## Scripts

- `npm run frontend:storybook` - start storybook to develop components in isolation
- `npm run dep-graph` - see dependency graph
- For more commands check `package.json`
- To generate new apps in the monorepo, check out [NX documentation](https://nx.dev/packages/nx/documents/generate).

## Check out my
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `system-design-patterns.md`
```markdown
# 📦 Sairyss/system-design-patterns [🔖 PENDING/APPROVE]
🔗 https://github.com/Sairyss/system-design-patterns


## Meta
- **Stars:** ⭐ 1195 | **Forks:** 🍴 141
- **Language:** N/A | **License:** Unknown
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Resources related to distributed systems, system design, microservices, scalability and performance, etc

## README (trích đầu)
```
# System Design Patterns

**This repo is work in progress**

Topics and resources related to distributed systems, system design, microservices, scalability and performance, etc

**Check out my other repositories**:

- [Domain-Driven Hexagon](https://github.com/Sairyss/domain-driven-hexagon) - Guide on Domain-Driven Design, software architecture, design patterns, best practices etc.
- [Backend best practices](https://github.com/Sairyss/backend-best-practices) - Best practices, tools and guidelines for backend development.
- [Full Stack starter template](https://github.com/Sairyss/fullstack-starter-template) - template for full stack applications based on TypeScript, React, Vite, ChakraUI, tRPC, Fastify, Prisma, zod, etc.

---

- [System Design Patterns](#system-design-patterns)
  - [Distributed systems integration](#distributed-systems-integration)
    - [Synchronous communication](#synchronous-communication)
    - [Asynchronous communication](#asynchronous-communication)
    - [Data serialization](#data-serialization)
    - [API Gateway](#api-gateway)
  - [Scalability](#scalability)
    - [Performance and availability](#performance-and-availability)
      - [Creating redundancy](#creating-redundancy)
      - [Autoscaling](#autoscaling)
      - [Load balancing](#load-balancing)
        - [Transport (Layer 4) load balancing](#transport-layer-4-load-balancing)
        - [Application (Layer 7) load balancing](#application-layer-7-load-balancing)
    - [Databases](#databases)
      - [Indexing](#indexing)
      - [Replication](#replication)
      - [Partitioning](#partitioning)
      - [Hot, Warm and Cold data](#hot-warm-and-cold-data)
      - [Database Federation](#database-federation)
      - [Denormalization](#denormalization)
      - [Materialized views](#materialized-views)
      - [Multitenancy](#multitenancy)
      - [SQL vs NoSQL](#sql-vs-nosql)
      - [Identifiers](#identifiers)
      - [Connection pooling](#connection-pooling)
    - [Caching](#caching)
      - [Caching strategies](#caching-strategies)
      - [Distributed caches](#distributed-caches)
      - [CDNs](#cdns)
    - [Coupling](#coupling)
      - [Location coupling](#location-coupling)
        - [Broker pattern](#broker-pattern)
      - [Temporal coupling](#temporal-coupling)
        - [Message queues](#message-queues)
      - [Business data and logic coupling](#business-data-and-logic-coupling)
      - [Shared-nothing architecture](#shared-nothing-architecture)
      - [Selective data replication](#selective-data-replication)
      - [Event-driven architecture](#event-driven-architecture)
        - [Event-driven end-to-end](#event-driven-end-to-end)
        - [Designing around dataflow](#designing-around-dataflow)
  - [Consistency](#consistency)
    - [Different views on data](#different-views-on-data)
    - [Distributed transactions](#distributed-transactions)
      - [Two-phase commit (2PC)](#two-phase-commit-2pc)
      - [Sagas](#sagas)
        - [Orchestration](#orchestratio
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


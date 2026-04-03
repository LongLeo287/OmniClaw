---
id: kgrzybek-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:59.852167
---

# KNOWLEDGE EXTRACT: kgrzybek
> **Extracted on:** 2026-03-30 17:38:16
> **Source:** kgrzybek

---

## File: `modular-monolith-with-ddd.md`
```markdown
# 📦 kgrzybek/modular-monolith-with-ddd [🔖 PENDING/APPROVE]
🔗 https://github.com/kgrzybek/modular-monolith-with-ddd


## Meta
- **Stars:** ⭐ 13526 | **Forks:** 🍴 2137
- **Language:** C# | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Full Modular Monolith application with Domain-Driven Design approach.

## README (trích đầu)
```
# Modular Monolith with DDD

Full Modular Monolith .NET application with Domain-Driven Design approach.

## Announcement

![](docs/Images/glory_to_ukraine.jpg)

Learn, use and benefit from this project only if:

- You **condemn Russia and its military aggression against Ukraine**
- You **recognize that Russia is an occupant that unlawfully invaded a sovereign state**
- You **support Ukraine's territorial integrity, including its claims over temporarily occupied territories of Crimea and Donbas**
- You **reject false narratives perpetuated by Russian state propaganda**

Otherwise, leave this project immediately and educate yourself.

Putin, idi nachuj.

## CI

![](https://github.com/kgrzybek/modular-monolith-with-ddd/workflows/Build%20Pipeline/badge.svg)

## FrontEnd application

FrontEnd application : [Modular Monolith With DDD: FrontEnd React application](https://github.com/kgrzybek/modular-monolith-with-ddd-fe-react)

## Table of contents

[1. Introduction](#1-introduction)

&nbsp;&nbsp;[1.1 Purpose of this Repository](#11-purpose-of-this-repository)

&nbsp;&nbsp;[1.2 Out of Scope](#12-out-of-scope)

&nbsp;&nbsp;[1.3 Reason](#13-reason)

&nbsp;&nbsp;[1.4 Disclaimer](#14-disclaimer)

&nbsp;&nbsp;[1.5 Give a Star](#15-give-a-star)

&nbsp;&nbsp;[1.6 Share It](#16-share-it)

[2. Domain](#2-domain)

&nbsp;&nbsp;[2.1 Description](#21-description)

&nbsp;&nbsp;[2.2 Conceptual Model](#22-conceptual-model)

&nbsp;&nbsp;[2.3 Event Storming](#23-event-storming)

[3. Architecture](#3-architecture)

&nbsp;&nbsp;[3.0 C4 Model](#30-c4-model)

&nbsp;&nbsp;[3.1 High Level View](#31-high-level-view)

&nbsp;&nbsp;[3.2 Module Level View](#32-module-level-view)

&nbsp;&nbsp;[3.3 API and Module Communication](#33-api-and-module-communication)

&nbsp;&nbsp;[3.4 Module Requests Processing via CQRS](#34-module-requests-processing-via-cqrs)

&nbsp;&nbsp;[3.5 Domain Model Principles and Attributes](#35-domain-model-principles-and-attributes)

&nbsp;&nbsp;[3.6 Cross-Cutting Concerns](#36-cross-cutting-concerns)

&nbsp;&nbsp;[3.7 Modules Integration](#37-modules-integration)

&nbsp;&nbsp;[3.8 Internal Processing](#38-internal-processing)

&nbsp;&nbsp;[3.9 Security](#39-security)

&nbsp;&nbsp;[3.10 Unit Tests](#310-unit-tests)

&nbsp;&nbsp;[3.11 Architecture Decision Log](#311-architecture-decision-log)

&nbsp;&nbsp;[3.12 Architecture Unit Tests](#312-architecture-unit-tests)

&nbsp;&nbsp;[3.13 Integration Tests](#313-integration-tests)

&nbsp;&nbsp;[3.14 System Integration Testing](#314-system-integration-testing)

&nbsp;&nbsp;[3.15 Event Sourcing](#315-event-sourcing)

&nbsp;&nbsp;[3.16 Database change management](#316-database-change-management)

&nbsp;&nbsp;[3.17 Continuous Integration](#317-continuous-integration)

&nbsp;&nbsp;[3.18 Static code analysis](#318-static-code-analysis)

&nbsp;&nbsp;[3.19 System Under Test SUT](#319-system-under-test-sut)

&nbsp;&nbsp;[3.20 Mutation Testing](#320-mutation-testing)

[4. Technology](#4-technology)

[5. How to Run](#5-how-to-ru
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `sample-dotnet-core-cqrs-api.md`
```markdown
# 📦 kgrzybek/sample-dotnet-core-cqrs-api [🔖 PENDING/APPROVE]
🔗 https://github.com/kgrzybek/sample-dotnet-core-cqrs-api
🌐 https://www.kamilgrzybek.com/design/simple-cqrs-implementation-with-raw-sql-and-ddd/

## Meta
- **Stars:** ⭐ 3053 | **Forks:** 🍴 675
- **Language:** C# | **License:** MIT
- **Last updated:** 2026-03-22
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Sample .NET Core REST API CQRS implementation with raw SQL and DDD using Clean Architecture.

## README (trích đầu)
```
Sample .NET Core REST API CQRS implementation with raw SQL and DDD using Clean Architecture.
==============================================================

## CI

![](https://github.com/kgrzybek/sample-dotnet-core-cqrs-api/workflows/Build%20Pipeline/badge.svg)

## Give a Star! :star:

If you like this project, learn something or you are using it in your applications, please give it a star. Thanks!

## Description
Sample .NET Core REST API application implemented with basic [CQRS](https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/cqrs) approach and Domain Driven Design.

## Architecture [Clean Architecture](http://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

![projects_dependencies](docs/clean_architecture.jpg)

## CQRS

Read Model - executing raw SQL scripts on database views objects (using [Dapper](https://github.com/StackExchange/Dapper)).

Write Model - Domain Driven Design approach (using Entity Framework Core).

Commands/Queries/Domain Events handling using [MediatR](https://github.com/jbogard/MediatR) library.

## Domain

![projects_dependencies](docs/domain_model_diagram.png)

## Validation
Data validation using [FluentValidation](https://github.com/JeremySkinner/FluentValidation)

Problem Details for HTTP APIs standard implementation using [ProblemDetails](https://github.com/khellang/Middleware/tree/master/src/ProblemDetails)

## Caching
Using Cache-Aside pattern and in-memory cache.

## Integration
Outbox Pattern implementation using [Quartz.NET](https://github.com/quartznet/quartznet)

## Related blog articles

[Simple CQRS implementation with raw SQL and DDD](http://www.kamilgrzybek.com/design/simple-cqrs-implementation-with-raw-sql-and-ddd/)

[Domain Model Encapsulation and PI with Entity Framework 2.2](http://www.kamilgrzybek.com/design/domain-model-encapsulation-and-pi-with-entity-framework-2-2/)

[REST API Data Validation](http://www.kamilgrzybek.com/design/rest-api-data-validation/)

[Domain Model Validation](http://www.kamilgrzybek.com/design/domain-model-validation/)

[How to publish and handle Domain Events](http://www.kamilgrzybek.com/design/how-to-publish-and-handle-domain-events/)

[Handling Domain Events: Missing Part](http://www.kamilgrzybek.com/design/handling-domain-events-missing-part/)

[Cache-Aside Pattern in .NET Core](http://www.kamilgrzybek.com/design/cache-aside-pattern-in-net-core/)

[The Outbox Pattern](http://www.kamilgrzybek.com/design/the-outbox-pattern/)

## How to run application
1. Create empty database.
2. Execute InitializeDatabase.sql script.
2. Set connection string (in appsettings.json or by user secrets mechanism).
3. Run!

## How to run Integration Tests
1. Create empty database.
2. Execute InitializeDatabase.sql script.
3. Set connection string using environment variable named `ASPNETCORE_SampleProject_IntegrationTests_ConnectionString`
- Run tests from project [src/Tests/SampleProject.IntegrationTests](src/Tests/SampleProject.IntegrationTests)
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


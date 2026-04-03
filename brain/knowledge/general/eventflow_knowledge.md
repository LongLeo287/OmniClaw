---
id: eventflow-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:22.804876
---

# KNOWLEDGE EXTRACT: eventflow
> **Extracted on:** 2026-03-30 17:36:29
> **Source:** eventflow

---

## File: `EventFlow.md`
```markdown
# 📦 eventflow/EventFlow [🔖 PENDING/APPROVE]
🔗 https://github.com/eventflow/EventFlow
🌐 https://geteventflow.net

## Meta
- **Stars:** ⭐ 2552 | **Forks:** 🍴 471
- **Language:** C# | **License:** NOASSERTION
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Async/await first CQRS+ES and DDD framework for .NET

## README (trích đầu)
```
# EventFlow

![EventFlow logo](https://raw.githubusercontent.com/eventflow/EventFlow/develop-v1/icon-128.png)

![NuGet downloads](https://img.shields.io/nuget/dt/EventFlow)

```
$ dotnet add package EventFlow
```

EventFlow is a basic CQRS+ES framework designed to be easy to use.

Have a look at our [getting started guide](https://geteventflow.net/getting-started/),
the [do’s and don’ts](https://geteventflow.net/additional/dos-and-donts/) and the
[FAQ](https://geteventflow.net/additional/faq/).

Alternatively, join our [Discord](https://discord.gg/QfgNPs5WxR) server to engage with the community. Its hopefully getting a reboot to kickstart the upcoming release of v1.

## Features

* **Easy to use**: Designed with sensible defaults and implementations that make it
  easy to create an example application
* **Highly configurable and extendable**: EventFlow uses interfaces for every part of
  its core, making it easy to replace or extend existing features with custom
  implementation
* **No use of threads or background workers**
* **MIT licensed** Easy to understand and use license for enterprise

## Versions

Development of version 1.0 has started and is mainly braking changes regarding changes
related to replacing EventFlow types with that of Microsoft extension abstractions,
mainly `IServiceProvider` and `ILogger<>`.

The following list key characteristics of each version as well as its related branches
(not properly configured yet).

* `1.x`

  Represents the next iteration of EventFlow that aligns EventFlow with the standard
  packages for .NET. Releases here will only support .NET Standard, .NET Core
  and .NET versions 6+ going forward.

  - Released
  - Still development
  - Not all projects migrated yet
  
  Read the [migration guide](https://geteventflow.net/migrations/v0-to-v1/) to view the full list of breaking
  changes as well as recommendations on how to migrate.

  ### Documentation
  Version 1.x documentation has been pulled into this repository in order to have
  the code and documentation closer together and have the documentation
  updated in the same pull-requests as any code changes. The compiled version of the
  documentation is available at https://geteventflow.net/.

  ### NuGet package status

  - 🟢 ported
  - 💚 newly added to 1.0
  - 🟠 not yet ported to 1.0
  - 💀 for packages that are removed as part of 1.0 (see the [migration guide](https://geteventflow.net/migrations/v0-to-v1/) for details)

  Projects
    - 🟢 `EventFlow`
    - 🟠 `EventFlow.AspNetCore`
    - 💀 `EventFlow.Autofac`
    - 💀 `EventFlow.DependencyInjection`
    - 🟠 `EventFlow.Elasticsearch`
    - 🟢 `EventFlow.EntityFramework`
    - 🟠 `EventFlow.EventStores.EventStore`
    - 🟢 `EventFlow.Hangfire`
    - 🟢 `EventFlow.MongoDB`
    - 🟢 `EventFlow.MsSql`
    - 💀 `EventFlow.Owin`
    - 🟢 `EventFlow.PostgreSql`
    - 🟠 `EventFlow.Redis`
    - 🟢 `EventFlow.RabbitMQ`
    - 🟢 `EventFlow.Sql`
    - 🟢 `EventFlow.SQLite`
    - 🟢 `EventFlow.TestHelpers`

  ### Branches
  - `
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


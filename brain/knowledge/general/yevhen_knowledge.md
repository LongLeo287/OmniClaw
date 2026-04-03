---
id: yevhen-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:47.536121
---

# KNOWLEDGE EXTRACT: yevhen
> **Extracted on:** 2026-03-30 18:01:25
> **Source:** yevhen

---

## File: `Streamstone.md`
```markdown
# 📦 yevhen/Streamstone [🔖 PENDING/APPROVE]
🔗 https://github.com/yevhen/Streamstone


## Meta
- **Stars:** ⭐ 403 | **Forks:** 🍴 66
- **Language:** C# | **License:** NOASSERTION
- **Last updated:** 2026-03-15
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Event store for Azure Table Storage

## README (trích đầu)
```
<p align="center">
  <img src="https://github.com/yevhen/Streamstone/blob/master/Logo.Wide.png?raw=true" alt="Streamstone's logo"/>
</p>

Streamstone is a tiny embeddable library targeted at building scalable event-sourced applications on top of Azure Table Storage. It has simple, functional style API, heavily inspired by Greg Young's Event Store.

## Features

+ Fully ACID compliant
+ Optimistic concurrency support
+ Duplicate event detection (based on identity)
+ Automatic continuation for both writes and reads (over WATS limits)
+ Custom stream and event properties you can query on
+ Synchronous (inline) projections and snapshots
+ Change tracking support for inline projections
+ Friendly for multi-tenant designs
+ Sharding support (jump consistent hashing)
+ Compatible with .NET Standard 2.0 and .NET Framework 4.6

## Installing from NuGet [![NuGet](https://img.shields.io/nuget/v/Streamstone.svg?style=flat)](https://www.nuget.org/packages/Streamstone/)

To install Streamstone via NuGet, run this command in NuGet package manager console:

    PM> Install-Package Streamstone

## Building from source [![Build status](https://ci.appveyor.com/api/projects/status/3rsmwblor11b6inq/branch/master?svg=true)](https://ci.appveyor.com/project/yevhen/streamstone/branch/master)

To build Streamstone binaries on Windows you will need to have Visual Studio 17 Update 3 or higher and .NET Core SDK 2.0 or higher. To build binaries on Linux use dotnet cli tooling (ie `dotnet build`). 

## Running unit tests

### Windows/Linux/MacOs

Use Azurite [npm](https://www.npmjs.com/package/azurite#npm) package to run tests and example app against an emulated table storage service. 

WARNING: Azurite doesn't fully emulate Azure Table Storage functionality so you may have some of the tests failing.

NOTE: Alternatively, you could run against real Azure by setting storage account connection string to **Streamstone-Test-Storage** user-level environment variable.


## Design

Streamstone is just a thin layer (library, not a server) on top of Windows Azure Table Storage. It implements low-level mechanics for dealing with event streams, and all heavy-weight lifting is done by underlying provider. 

The api is stateless and all exposed objects are immutable, once fully constructed. Streamstone doesn't dictate payload serialization protocol, so you are free to choose any protocol you want.

Optimistic concurrency is implemented by always including stream header entity with every write, making it impossible to append to a stream without first having a latest Etag. Duplicate event detection is done by automatically creating additional entity for every event, with RowKey value set to a unique identifier of a source event (consistent secondary index).     

## Schema

<a href="https://raw.githubusercontent.com/yevhen/Streamstone/master/Doc/Schema.png" target="_blank" title="Click to view full size"><img src="https://raw.githubusercontent.com/yevhen/Streamstone/master/Doc/Schema.png" al
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


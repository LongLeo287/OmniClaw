---
id: hlaueriksson-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:52.322984
---

# KNOWLEDGE EXTRACT: hlaueriksson
> **Extracted on:** 2026-03-30 17:38:07
> **Source:** hlaueriksson

---

## File: `CommandQuery.md`
```markdown
# 📦 hlaueriksson/CommandQuery [🔖 PENDING/APPROVE]
🔗 https://github.com/hlaueriksson/CommandQuery


## Meta
- **Stars:** ⭐ 110 | **Forks:** 🍴 17
- **Language:** C# | **License:** MIT
- **Last updated:** 2026-03-22
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Command Query Separation for 🌐ASP.NET Core ⚡AWS Lambda ⚡Azure Functions ⚡Google Cloud Functions

## README (trích đầu)
```
# CommandQuery<!-- omit in toc -->

[![build](https://github.com/hlaueriksson/CommandQuery/actions/workflows/build.yml/badge.svg)](https://github.com/hlaueriksson/CommandQuery/actions/workflows/build.yml)
[![CodeFactor](https://codefactor.io/repository/github/hlaueriksson/commandquery/badge)](https://codefactor.io/repository/github/hlaueriksson/commandquery)

[![CommandQuery](https://img.shields.io/nuget/v/CommandQuery.svg?label=CommandQuery)](https://www.nuget.org/packages/CommandQuery)
[![CommandQuery.Abstractions](https://img.shields.io/nuget/v/CommandQuery.Abstractions.svg?label=CommandQuery.Abstractions)](https://www.nuget.org/packages/CommandQuery.Abstractions)

[![CommandQuery.AspNetCore](https://img.shields.io/nuget/v/CommandQuery.AspNetCore.svg?label=CommandQuery.AspNetCore)](https://www.nuget.org/packages/CommandQuery.AspNetCore)
[![CommandQuery.AWSLambda](https://img.shields.io/nuget/v/CommandQuery.AWSLambda.svg?label=CommandQuery.AWSLambda)](https://www.nuget.org/packages/CommandQuery.AWSLambda)
[![CommandQuery.AzureFunctions](https://img.shields.io/nuget/v/CommandQuery.AzureFunctions.svg?label=CommandQuery.AzureFunctions)](https://www.nuget.org/packages/CommandQuery.AzureFunctions)
[![CommandQuery.GoogleCloudFunctions](https://img.shields.io/nuget/v/CommandQuery.GoogleCloudFunctions.svg?label=CommandQuery.GoogleCloudFunctions)](https://www.nuget.org/packages/CommandQuery.GoogleCloudFunctions)

[![CommandQuery.Client](https://img.shields.io/nuget/v/CommandQuery.Client.svg?label=CommandQuery.Client)](https://www.nuget.org/packages/CommandQuery.Client)

## Content<!-- omit in toc -->

- [Introduction](#introduction)
- [Packages](#packages)
  - [`CommandQuery` ⚙️](#commandquery-️)
  - [`CommandQuery.AspNetCore` 🌐](#commandqueryaspnetcore-)
  - [`CommandQuery.AWSLambda` ⚡](#commandqueryawslambda-)
  - [`CommandQuery.AzureFunctions` ⚡](#commandqueryazurefunctions-)
  - [`CommandQuery.GoogleCloudFunctions` ⚡](#commandquerygooglecloudfunctions-)
  - [`CommandQuery.Client` 🧰](#commandqueryclient-)
- [Upgrading](#upgrading)
- [Acknowledgements](#acknowledgements)

## Introduction

Command Query Separation (CQS) for .NET and C#

- Build services that separate the responsibility of commands and queries
- Focus on implementing the handlers for commands and queries
- Create APIs with less boilerplate code

Available for:

```txt
🌐 ASP.NET Core
⚡ AWS Lambda
⚡ Azure Functions
⚡ Google Cloud Functions
```

Command Query Separation?

> **Queries**: Return a result and do not change the observable state of the system (are free of side effects).
>
> **Commands**: Change the state of a system but do not return a value.
>
> — <cite>[Martin Fowler](http://martinfowler.com/bliki/CommandQuerySeparation.html)</cite>

In other words:

- Commands
  - Writes (create, update, delete) data
- Queries
  - Reads and returns data

The traditional approach that commands *do not return a value* is a bit inconvenient.

`CommandQuery` has a pragmatic take and supports bot
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


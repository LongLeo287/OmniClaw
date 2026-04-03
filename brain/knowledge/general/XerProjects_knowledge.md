---
id: xerprojects-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:47.255187
---

# KNOWLEDGE EXTRACT: XerProjects
> **Extracted on:** 2026-03-30 18:01:19
> **Source:** XerProjects

---

## File: `Xer.Cqrs.md`
```markdown
# 📦 XerProjects/Xer.Cqrs [🔖 PENDING/APPROVE]
🔗 https://github.com/XerProjects/Xer.Cqrs


## Meta
- **Stars:** ⭐ 103 | **Forks:** 🍴 8
- **Language:** C# | **License:** MIT
- **Last updated:** 2025-12-09
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A lightweight and easy-to-use CQRS + DDD library

## README (trích đầu)
```
# What is Xer.Cqrs?

Xer.Cqrs is a convenience package that contains all packages needed to build a CQRS write side with DDD concepts. It groups together other lightweight XerProjects libraries:
* [Domain Driven](https://github.com/XerProjects/Xer.DomainDriven) - contains Domain Driven Design (DDD) components/concepts.
* [Command Stack](https://github.com/XerProjects/Xer.Cqrs.CommandStack) - contains components for handling commands.
* [Event Stack](https://github.com/XerProjects/Xer.Cqrs.EventStack) - contains components for handling events.

# Build

| Branch | Status |
|--------|--------|
| Master | [![Build status](https://ci.appveyor.com/api/projects/status/jr4h0o8h064m6je2/branch/master?svg=true)](https://ci.appveyor.com/project/XerProjects25246/xer-cqrs-5e3ne/branch/master) |
| Dev | [![Build status](https://ci.appveyor.com/api/projects/status/jr4h0o8h064m6je2/branch/dev?svg=true)](https://ci.appveyor.com/project/XerProjects25246/xer-cqrs-5e3ne/branch/dev) |


# Table of contents
* [Overview](#overview)
* [Features](#features)
* [Installation](#installation)
* [Getting Started](#getting-started)
   * [Command Handling](#command-handling)
   * [Event Handling](#event-handling)

# Overview
Simple CQRS library

This project composes of components for implementing the CQRS pattern (Command Handling, Event Handling) with DDD concepts (Aggregate Roots, Entities, Value Objects, Domain Events). This library was built with simplicity, modularity and pluggability in mind.

## Features
* Send commands to registered command handlers.
* Send events to registered event handlers.
* Provides simple abstraction for hosted command/event handlers which can be registered just like a regular command/event handler.
* Multiple ways of registering command/event handlers:
    * Simple handler registration (no IoC container).
    * IoC container registration
      * achieved by creating implementations of IContainerAdapter or using pre-made extensions pakcages for supported containers.
        * Microsoft.DependencyInjection
          
          [![NuGet](https://img.shields.io/nuget/v/Xer.Cqrs.Extensions.Microsoft.DependencyInjection.svg)](https://www.nuget.org/packages/Xer.Cqrs.Extensions.Microsoft.DependencyInjection/)
          
          See https://github.com/XerProjects/Xer.Cqrs.Extensions.Microsoft.DependencyInjection for source.
          
        * SimpleInjector
          
          [![NuGet](https://img.shields.io/nuget/v/Xer.Cqrs.Extensions.SimpleInjector.svg)](https://www.nuget.org/packages/Xer.Cqrs.Extensions.SimpleInjector/)
          
          See https://github.com/XerProjects/Xer.Cqrs.Extensions.SimpleInjector for source.
                    
        * Autofac
          
          [![NuGet](https://img.shields.io/nuget/v/Xer.Cqrs.Extensions.Autofac.svg)](https://www.nuget.org/packages/Xer.Cqrs.Extensions.Autofac/)
          
          See https://github.com/XerProjects/Xer.Cqrs.Extensions.Autofac for source.
                    
    * Attribute 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


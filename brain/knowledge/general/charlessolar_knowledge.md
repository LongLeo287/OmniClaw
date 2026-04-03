---
id: charlessolar-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:00.683198
---

# KNOWLEDGE EXTRACT: charlessolar
> **Extracted on:** 2026-03-30 17:31:17
> **Source:** charlessolar

---

## File: `Aggregates.NET.md`
```markdown
# 📦 charlessolar/Aggregates.NET [🔖 PENDING/APPROVE]
🔗 https://github.com/charlessolar/Aggregates.NET


## Meta
- **Stars:** ⭐ 441 | **Forks:** 🍴 63
- **Language:** C# | **License:** MIT
- **Last updated:** 2026-02-13
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
.NET event sourced domain driven design model via NServiceBus and GetEventStore

## README (trích đầu)
```
|              |                                                                                                                                                                                    |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Build**    | [![Build status](https://ci.appveyor.com/api/projects/status/r75p0yn5uo6colgk?svg=true&branch=master)](https://ci.appveyor.com/project/charlessolar/aggregates-net)                |
| **Coverage** | [![Coverage Status](https://coveralls.io/repos/github/charlessolar/Aggregates.NET/badge.svg?branch=master)](https://coveralls.io/github/charlessolar/Aggregates.NET?branch=master) |
| **Quality**  | [![GitHub issues](https://img.shields.io/github/issues-raw/charlessolar/aggregates.net.svg)](https://github.com/charlessolar/Aggregates.NET/issues)                                |
| **Nuget**    | [![Nuget](https://buildstats.info/nuget/Aggregates.NET)](http://nuget.org/packages/Aggregates.NET)                                                                                 |

# Aggregates.NET v0.18

Aggregates.NET is a library to facilitate integration between [NServiceBus](https://github.com/Particular/NServiceBus) and [EventStore](https://github.com/EventStore/EventStore). It provides a framework to define entities, value objects, command and event handlers, and many other domain driven design and CQRS principles. The framework should take all the tediousness of dealing with event streams and message queues out of your consideration and give you a solid base to build a solid event sourced application.

#### Note as of v0.17

Aggregates.NET uses Microsoft's standard DI and logging module - and I've removed direct support for StructureMap, SimpleInjector and LibLog which supported many different logging modules. I did this simply to reduce the headache for myself going forward to v1.0 - if you want to use one of these other libraries fear not! Each of them *should* have adaptors for Microsoft's DI and Logging.

All of the samples and examples are Microsoft Hosting setup so likely this won't affect your projects especially if you're new. But if you are upgrading Agg.net something to be aware of!

## What will Aggregates.NET do for you?

Take the following example

```
class Handler :
    IHandleMessages<Send>
{
    public async Task Handle(Send command, IMessageHandlerContext ctx)
    {
        var entity = await ctx.For<EchoEntity>().TryGet("default");
        if (entity == null)
            entity = await ctx.For<EchoEntity>().New("default");

        entity.Echo(command.Message);
    }
} 
```

Users of NSB should immediately notice the `IHandleMessages` convention - everything inside the message handler is provided by Aggregates.NET. The special extension methods are using entity definitions to retreive streams from the eventstore. Once loaded the en
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `eShopOnContainersDDD.md`
```markdown
# 📦 charlessolar/eShopOnContainersDDD [🔖 PENDING/APPROVE]
🔗 https://github.com/charlessolar/eShopOnContainersDDD


## Meta
- **Stars:** ⭐ 322 | **Forks:** 🍴 45
- **Language:** C# | **License:** MIT
- **Last updated:** 2026-02-13
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Fork of dotnet-architecture/eShopOnContainers in full DDD/CQRS design using my own patterns

## README (trích đầu)
```
# eShopOnContainers (Aggregates.Net Edition)

This project is a fork (maybe better a loose copy) of Microsoft's container example [eShopOnContainers](https://github.com/dotnet-architecture/eShopOnContainers).  I implemented many of the same objects using my own DDD, EventSourcing library [Aggregates.NET](https://github.com/volak/Aggregates.NET) and its meant to be an illustrative example of a fully event sourced application.

## Like what you see?

We're hiring developers!  We are currently looking for a couple people to help develop new software for small/medium businesses - remote OK but located around Chicago is ideal.  If you have an interest in learning DDD, CQRS, EventSourcing and making distributed systems less complex send me an email or better yet open a pull request!

### Live Demo

Currently disabled

### Wiki

There are articles in the Wiki about certain features of the app / how certain things are handled and implemented - check them out!

### Disclaimer

This is a project written over the course of a month in my free time.  Its not bug free, its not exploit free, it may not even be very clean in places.  Please don't judge too harsly 🙏 

# Instructions

**Linux Only**

One docker image we require to run (eventstore) doesn't have a windows container - so run `docker-compose` on linux only for now!

**Start**

from the linux-cli directory
```
export SERVICESTACK_LICENSE=<-Your license->
export HOST_SERVER=<-Machine's ip address->
./build.sh
./up.sh
```

**Note**

A NServiceBus license is not required to run this example - but a servicestack license is.
Its also required to supply the host machine's ip - use `localhost` if running localy

### What is EventSourcing?

EventSourcing is a process of representing domain objects (Orders, Invoices, Accounts, etc) as a series of separate events.

Your application ends up being 1 long audit log which records every state-changing event that occurs.  The advantage of this approach is other processes can read this event log and generate models that contain only the information the process cares about.  There is also additional information available that other services perhaps don't record themselves.

Imagine a shoppign cart which fills with items to buy.  The warehouse only cares about the final order of the stuff the customer actually agreed to purchase -

<img src="img/eventsourcing.png" height="400px">

but the marketing team might care more about the items the customer removed from their cart **without** buying.  

Using eventsourcing correctly you can generate models which contain both sets of information to satisfy both departments with only 1 set of data.

### What is CQRS

CQRS stands for **Command and Query Responsibility Segregation**

<img src="img/cqrs-logical.svg" height="400px">

In a nut shell - commands are everything that want to change the application state.  Queries are anything that want to read application state.  **There is no overlap**

Commands do not return any data other
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `TodoMVC-DDD-CQRS-EventSourcing.md`
```markdown
# 📦 charlessolar/TodoMVC-DDD-CQRS-EventSourcing [🔖 PENDING/APPROVE]
🔗 https://github.com/charlessolar/TodoMVC-DDD-CQRS-EventSourcing


## Meta
- **Stars:** ⭐ 257 | **Forks:** 🍴 32
- **Language:** C# | **License:** MIT
- **Last updated:** 2026-02-13
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Implementation of basic Todo app via tastejs/todomvc in C#/Typescript with eventsourcing, cqrs, and domain driven design

## README (trích đầu)
```
# Instructions

**Start**

```
docker compose build
docker compose up
```

# Source Code!

Being this project has such a small domain context there are only a couple source files which contain real logic.  Other files are helpers, extensions, or setup.  

### Important backend files:

* [Domain Command Handler](src/Domain/Todo/Handler.cs)
* [Domain Todo Aggregate](src/Domain/Todo/Todo.cs)
* [Read Model Projector](src/Application/Todo/Handler.cs)
* [Web Request Handler](src/Web/Controllers/TodoController.cs)
* [Domain Handler Tests](src/Test/DomainHandler.cs)
* [Event Handler Tests](src/Test/EventHandler.cs)

Web frontend from [TodoMVC-React](https://github.com/blacksonic/todomvc-react)

### What is EventSourcing?

EventSourcing is a process of representing domain objects (Orders, Invoices, Accounts, etc) as a series of separate events.

Your application ends up being 1 long audit log which records every state-changing event that occurs.  The advantage of this approach is other processes can read this event log and generate models that contain only the information the process cares about.  There is also additional information available that other services perhaps don't record themselves.

Imagine a shoppign cart which fills with items to buy.  The warehouse only cares about the final order of the stuff the customer actually agreed to purchase -

<img src="img/eventsourcing.png" height="400px">

but the marketing team might care more about the items the customer removed from their cart **without** buying.  

Using eventsourcing correctly you can generate models which contain both sets of information to satisfy both departments with only 1 set of data.

### What is CQRS

CQRS stands for **Command and Query Responsibility Segregation**

<img src="img/cqrs-logical.svg" height="400px">

In a nut shell - commands are everything that want to change the application state.  Queries are anything that want to read application state.  **There is no overlap**

Commands do not return any data other than if they were *Accepted* or *Rejected*. Accepted meaning the change was saved and read models will be updated.  Rejected meaning the command failed validation or was not valid to be run at this time.  (One example would be trying to invoice a sales order which has already been invoiced)

## Architecture Overview

<img src="img/overview.png" height="400px">

## Commands Processing

<img src="img/commands.png" height="400px">

### Good reads

* [Microsoft's CQRS architecture guide](https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/cqrs)
* [Microsoft's eventsourcing architecture guide](https://docs.microsoft.com/en-us/azure/architecture/patterns/event-sourcing)

### EventStore Management

{host}:2113

### RabbitMq Management

{host}:15672

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


---
id: younos1986-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:47.596992
---

# KNOWLEDGE EXTRACT: younos1986
> **Extracted on:** 2026-03-30 18:01:25
> **Source:** younos1986

---

## File: `Core.EventStore.md`
```markdown
# 📦 younos1986/Core.EventStore [🔖 PENDING/APPROVE]
🔗 https://github.com/younos1986/Core.EventStore


## Meta
- **Stars:** ⭐ 6 | **Forks:** 🍴 0
- **Language:** C# | **License:** Unknown
- **Last updated:** 2025-12-29
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A library to facilitate communication between CommandService and QueryService. The Idea is when any event occures in commandService, it should be persisted in QueryService in MongoDb, SqlServer, MySql and PostgreSQL

## README (trích đầu)
```
# Core.EventStore

![.NET Core](https://github.com/younos1986/Core.EventStore/workflows/.NET%20Core/badge.svg)
 

A library to facilitate communication between CommandService and QueryService. The Idea is when any event occures in commandService, it should be persisted in QueryService in MongoDb, SqlServer, MySql and PostgreSQL


<img src="https://raw.githubusercontent.com/younos1986/Core.EventStore/master/images/what_it_does.png" />


- CommandService only keeps events in EventStore
- QueryService's Projectors will be triggered when any event is stored in EventStore by CommandService


# Nuget

* <a href="https://www.nuget.org/packages/Core.EventStore/"> Core.EventStore <a/>
 
* <a href="https://www.nuget.org/packages/Core.EventStore.Mongo/"> Core.EventStore.Mongo <a/>
 
* <a href="https://www.nuget.org/packages/Core.EventStore.EFCore.SqlServer/"> Core.EventStore.EFCore.SqlServer <a/>

* <a href="https://www.nuget.org/packages/Core.EventStore.EFCore.MySql"> Core.EventStore.EFCore.MySql <a/>

* PostgreSQL is still in progress

# Features

* Keep track of last event position
* Idempotency
* Define multiple projectors for one event


# Dependencies

.NETStandard 2.1

Autofac (>= 5.1.2)

EventStore.Client (>= 5.0.6)

MediatR (>= 7.0.0)

Microsoft.Extensions.Configuration.Abstractions (>= 3.1.2)

MongoDB.Driver (>= 2.10.0)


# How to use 

In CommandService

```
using Autofac;
using Core.EventStore.Autofac;

namespace CommandService.IoCC.Modules
{
    public class EventStoreModule : Module
    {
        protected override void Load(ContainerBuilder builder)
        {
            builder.RegisterEventStore(initializationConfiguration =>
            {
                initializationConfiguration.Username = "admin";
                initializationConfiguration.PASSWORD='[REDACTED_PASSWORD]';
                initializationConfiguration.DefaultPort = 1113;
                //initializationConfiguration.IsDockerized = true;
                //initializationConfiguration.DockerContainerName = "eventstore";

                initializationConfiguration.IsDockerized = false;
                initializationConfiguration.ConnectionUri = "127.0.0.1";
            });
        }
    }
}


```

In QueryService

```
using Autofac;
using Core.EventStore.Autofac;
using IntegrationEvents;
using QueryService.InvokerPipelines;

namespace QueryService.IoCC.Modules
{
        public class EventStoreModule : Module
        {
            protected override void Load(ContainerBuilder builder)
            {
                builder.RegisterEventStore(initializationConfiguration =>
                {
                    initializationConfiguration.Username = "admin";
                    initializationConfiguration.PASSWORD='[REDACTED_PASSWORD]';
                    initializationConfiguration.DefaultPort = 1113;

                    //initializationConfiguration.IsDockerized = true;
                    //initializationConfiguration.DockerContainerName = "eventstore";

                    initializationCon
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


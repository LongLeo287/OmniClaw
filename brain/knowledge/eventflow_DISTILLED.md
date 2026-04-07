---
id: EventFlow
type: knowledge
owner: OA_Triage
---
# EventFlow
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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
  - `develop-v1`: Development branch, pull requests should be done here
  - `release-v1`: Release branch, merge commits are done to this branch from
    `develop-v1` to create releases. Typically each commit represents a release

* `0.x` (legacy)

  The current stable version of EventFlow and has been the version of EventFlow
  for almost six years. 0.x versions have .NET Framework support and limited
  support to the Microsoft extension packages through extra NuGet packages.

  Feature and bug fix releases will still be done while there's interest in
  the community.

  ### Branches
  - `develop-v0`: Development branch, pull requests should be done here
  - `release-v0`: Release branch, merge commits are done to this branch from
    `develop-v0` to create releases. Typically each commit represents a release

  ### Documentation
  Version 0.x documentation is (although a bit outdated) is live at
  https://docs.geteventflow.net/.


## Talks directly related to EventFlow

- [GOTO Aarhus 2022](https://github.com/rasmus/presentation-goto-2022) by [rasmus](https://github.com/rasmus)
  Practical event sourcing using EventFlow

## Examples

* **[Complete](#complete-example):** Shows a complete example on how to use
  EventFlow with in-memory event store and read models in a relatively few lines
  of code
* **Shipping:** To get a more complete example of how EventFlow _could_ be used,
  have a look at the shipping example found here in the code base. The example
  is based on the shipping example from the book "Domain-Driven Design -
  Tackling Complexity in the Heart of Software" by Eric Evans. Its
  _in-progress_, but should provide inspiration on how to use EventFlow on a
  larger scale. If you have ideas and/or comments, create a pull request or
  an issue
  
### External Examples

List of examples create by different community members. Note that many of these
examples will be using EventFlow 0.x.

*Create a pull request to get your exampled linked from here.*

 * **[Racetimes:](https://github.com/dennisfabri/Eventflow.Example.Racetimes)**
   Shows some features of EventFlow that are not covered in the 
   [complete example](#complete-example). It features entities, a read model for 
   an entity, delete on read models, specifications and snapshots.

   * **[Racetimes for Azure Functions:](https://github.com/craignicol/Eventflow.Example.Racetimes)**
     Extends the above example to support the HTTP access via Azure Functions
     
   * **[Racetimes for Azure Functions and Event Grid:](https://github.com/craignicol/Eventflow.Example.Racetimes/tree/feature/event-grid-as-extension)**
     Further extends the Azure Functions Example to publish to Event Grid, following the RabbitMQ pattern

 * **[.NET Core:](https://github.com/johnny-chan/EventFlowDemo)**
	A Web API running .NET Core 2.2 using the event flow. It uses the pre-defined 
	command/entities/events from the [complete example](#complete-example). There are endpoints to 
	create a new example event, getting a data model and to replay all data models.
	
* **[ElasticSearch/.NET Core:](https://github.com/DureSameen/EventFlowWithElasticSearch)**
	It is configured with EventFlow, ElasticSearch, EventStore, and RabbitMq. See "withRabbitMq" branch for #384.

 * **[Vehicle Tracking:](https://github.com/MongkonEiadon/VehicleTracker)**
	A Microservice on .NET Core 2.2 with docker based, you can up the service with docker-compose, this project using various
  tools to up the services aka. Linux Docker based on .NET Core, RabbitMq, EntityFramework with SQL Server and using EventFlow following CQRS-ES architecture
  and all microservice can access through ApiGateway which using Ocelot

  * **[RestAirline:](https://github.com/twzhangyang/RestAirline)**
	A classic DDD with CQRS-ES, Hypermedia API project based on EventFlow. It's targeted to ASP.NET Core 2.2 and can be deployed to docker and k8s.
	
* **[Full Example:](https://github.com/OKTAYKIR/EventFlow.Example)**
	A console application on .NET Core 2.2. You can up the services using [docker-compose file](https://github.com/OKTAYKIR/EventFlow.Example/blob/master/build/docker-compose.yml). Docker-compose file include EventStore, RabbitMq, MongoDb, and PostgreSQL. It include following EventFlow concepts:
	* Aggregates
	* Command bus and commands
	* Synchronous subscriber
	* Event store ([GES](https://eventstore.com/))
	* In-memory read model.
	* Snapshots ([MongoDb](https://www.mongodb.com/))
	* Sagas
	* Event publising (In-memory, [RabbitMq](https://www.rabbitmq.com/))
	* Metadata
	* Command bus decorator, custom value object, custom execution result, ...
	
### Overview

Here is a list of the EventFlow concepts. Use the links to navigate
to the documentation.

* [**Aggregates:**](https://geteventflow.net/basics/aggregates/)
  Domains object that guarantees the consistency of changes being made within
  each aggregate
* [**Command bus and commands:**](https://geteventflow.net/basics/commands/)
  Entry point for all command/operation execution.
* [**Event store:**](https://geteventflow.net/integration/event-stores/)
  Storage of the event stream for aggregates. Currently there is support for
  these storage types.
  * In-memory - only for test
  * Files - only for test
  * Microsoft SQL Server
  * Entity Framework Core
  * SQLite
  * PostgreSQL
  * EventStore - [home page](https://eventstore.org/)
* [**Subscribers:**](https://geteventflow.net/basics/subscribers/)
  Listeners that act on specific domain events. Useful if an specific action
  needs to be triggered after a domain event has been committed.
* [**Read models:**](https://geteventflow.net/integration/read-stores/)
  Denormalized representation of aggregate events optimized for reading fast.
  Currently there is support for these read model storage types.
  For the SQL storage types the queries are being generated automatically with quoted columns and table names.
  * Elasticsearch
  * In-memory - only for test
  * Microsoft SQL Server
  * Entity Framework Core
  * SQLite
  * PostgreSQL
* [**Snapshots:**](https://geteventflow.net/additional/snapshots/)
  Instead of reading the entire event stream every single time, a snapshot can
  be created every so often that contains the aggregate state. EventFlow
  supports upgrading existing snapshots, which is useful for long-lived
  aggregates. Snapshots in EventFlow are opt-in and EventFlow has support for
  * In-memory - only for test
  * Microsoft SQL Server
  * Entity Framework Core
  * SQLite
  * PostgreSQL
* [**Sagas:**](https://geteventflow.net/basics/sagas/)
  Also known as _process managers_, coordinates and routes messages between
  bounded contexts and aggregates
* [**Queries:**](https://geteventflow.net/basics/queries/)
  Value objects that represent a query without specifying how its executed,
  that is let to a query handler
* [**Jobs:**](https://geteventflow.net/basics/jobs/) Perform scheduled tasks at
  a later time, e.g. publish a command. EventFlow provides support for these
  job schedulers
  * Hangfire - [home page](https://hangfire.io/)
* [**Event upgrade:**](https://geteventflow.net/basics/event-upgrade/)
  As events committed to the event store is never changed, EventFlow uses the
  concept of event upgraders to deprecate events and replace them with new
  during aggregate load.
* **Event publishing:** Sometimes you want other applications or services to
  consume and act on domains. For this EventFlow supports event publishing.
  * RabbitMQ
* [**Metadata:**](https://geteventflow.net/basics/metadata/)
  Additional information for each aggregate event, e.g. the IP of
  the user behind the event being emitted. EventFlow ships with
  several providers ready to use used.
* [**Value objects:**](https://geteventflow.net/additional/value-objects/)
  Data containing classes used to validate and hold domain data, e.g. a
  username or e-mail.

## Complete example
Here's a complete example on how to use the default in-memory event store
along with an in-memory read model.

The example consists of the following classes, each shown below

- `ExampleAggregate`: The aggregate root
- `ExampleId`: Value object representing the identity of the aggregate root
- `ExampleEvent`: Event emitted by the aggregate root
- `ExampleCommand`: Value object defining a command that can be published to the
  aggregate root
- `ExampleCommandHandler`: Command handler which EventFlow resolves using its IoC
  container and defines how the command specific is applied to the aggregate root
- `ExampleReadModel`: In-memory read model providing easy access to the current
  state

**Note:** This example is part of the EventFlow test suite, so checkout the
code and give it a go.

```csharp
[Test]
public async Task Example()
{
  // We wire up EventFlow with all of our classes. Instead of adding events,
  // commands, etc. explicitly, we could have used the the simpler
  // AddDefaults(Assembly) instead.
  var serviceCollection = new ServiceCollection()
    .AddLogging()
    .AddEventFlow(o => o
      .AddEvents(typeof(ExampleEvent))
      .AddCommands(typeof(ExampleCommand))
      .AddCommandHandlers(typeof(ExampleCommandHandler))
      .UseInMemoryReadStoreFor<ExampleReadModel>());

  using (var serviceProvider = serviceCollection.BuildServiceProvider())
  {
    // Create a new identity for our aggregate root
    var exampleId = ExampleId.New;

    // Resolve the command bus and use it to publish a command
    var commandBus = serviceProvider.GetRequiredService<ICommandBus>();
    await commandBus.PublishAsync(
      new ExampleCommand(exampleId, 42), CancellationToken.None);

    // Resolve the query handler and use the built-in query for fetching
    // read models by identity to get our read model representing the
    // state of our aggregate root
    var queryProcessor = serviceProvider.GetRequiredService<IQueryProcessor>();
    var exampleReadModel = await queryProcessor.ProcessAsync(
      new ReadModelByIdQuery<ExampleReadModel>(exampleId), CancellationToken.None);

    // Verify that the read model has the expected magic number
    exampleReadModel.MagicNumber.Should().Be(42);
  }
}
```

```csharp
// The aggregate root
public class ExampleAggregate : AggregateRoot<ExampleAggregate, ExampleId>,
  IEmit<ExampleEvent>
{
  private int? _magicNumber;

  public ExampleAggregate(ExampleId id) : base(id) { }

  // Method invoked by our command
  public void SetMagicNumber(int magicNumber)
  {
    if (_magicNumber.HasValue)
      throw DomainError.With("Magic number already set");

    Emit(new ExampleEvent(magicNumber));
  }

  // We apply the event as part of the event sourcing system. EventFlow
  // provides several different methods for doing this, e.g. state objects,
  // the Apply method is merely the simplest
  public void Apply(ExampleEvent aggregateEvent)
  {
    _magicNumber = aggregateEvent.MagicNumber;
  }
}
```

```csharp
// Represents the aggregate identity (ID)
public class ExampleId : Identity<ExampleId>
{
  public ExampleId(string value) : base(value) { }
}
```

```csharp
// A basic event containing some information
public class ExampleEvent : AggregateEvent<ExampleAggregate, ExampleId>
{
  public ExampleEvent(int magicNumber)
  {
      MagicNumber = magicNumber;
  }

  public int MagicNumber { get; }
}
```

```csharp
// Command for update magic number
public class ExampleCommand : Command<ExampleAggregate, ExampleId>
{
  public ExampleCommand(
    ExampleId aggregateId,
    int magicNumber)
    : base(aggregateId)
  {
    MagicNumber = magicNumber;
  }

  public int MagicNumber { get; }
}
```

```csharp
// Command handler for our command
public class ExampleCommandHandler
  : CommandHandler<ExampleAggregate, ExampleId, ExampleCommand>
{
  public override Task ExecuteAsync(
    ExampleAggregate aggregate,
    ExampleCommand command,
    CancellationToken cancellationToken)
  {
    aggregate.SetMagicNumber(command.MagicNumber);
    return Task.CompletedTask;;
  }
}
```

```csharp
// Read model for 
... [TRUNCATED]
```

### File: requirements.txt
```txt
mkdocs-material
mkdocs-git-committers-plugin-2


```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct, or to ban temporarily or permanently any contributor for other behaviors that they deem inappropriate, threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces when an individual is representing the project or its community. Examples of representing a project or community include using an official project e-mail address, posting via an official social media account, or acting as an appointed representative at an online or offline event. Representation of a project may be further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team at r@smus.nu. The project team will review and investigate all complaints, and will respond in a way that it deems appropriate to the circumstances. The project team is obligated to maintain confidentiality with regard to the reporter of an incident. Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good faith may face temporary or permanent repercussions as determined by other members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4, available at [http://contributor-covenant.org/version/1/4][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/

```

### File: CONTRIBUTING.md
```md
## How to contribute

EventFlow still needs a lot of love and if you want to help out there are
several areas that you could help out with.

* **Features:** If you have a great idea for EventFlow, create a pull request.
   It might be a finished idea or just some basic concepts showing the feature
   outline
* **Pull request feedback:** Typically there are several pull requests marked
   with the `in progress` and feedback is always welcome. Please note that the
   quality of the code here might not be "production ready", especially if
   the pull request is marked with the `prof of concept` label
* **Documentation:** Good documentation is very important for any library and
   is also very hard to do properly, so if spot a spelling error, think up
   a good idea for a guide or just have some comments, then please create
   either a pull request or an issue
* **Information sharing:** Working with CQRS+ES and DDD is hard, so if you come
   across articles that might be relevant for EventFlow, or even better, can
   point to specfic EventFlow functionality that might be done better, then
   please create an issue or ask in the Gitter chat
* **Expand the shipping example:** If you have ideas on how to expand the
  shipping example found in the code base, the please create a pull request
  or create an issue
  * Give a good understanding of how to use EventFlow
  * Give a better understanding of how API changes in EventFlow affect
    existing applications
  * Provide a platform for DDD discussions

```

### File: CONTRIBUTORS.md
```md
# Contributors

List of notable contributors to EventFlow sorted alphabetically. For a
complete list of all contributions to EventFlow, have look at the
[contributors](https://github.com/eventflow/EventFlow/graphs/contributors)
graph.

If you think your name is missing from the list, create a pull-request.

### [Carlos Eduardo Ferrari](https://github.com/ceferrari)

* Converted EventFlow to Visual Studio 2017 project format

### [Christian Ølholm](https://github.com/olholm)

* Created the current logo of EventFlow

### [Edward Wilson](https://github.com/edwardwilson)

* Original MongoDB author

### [Emanuele Curati](https://github.com/ProH4Ck)

* ASP.NET Core 3 
* Docker integration test cleanup

### [Frank Ebersoll](https://github.com/frankebersoll)

* Created following packages
  * `EventFlow.DependencyInjection`
  * `EventFlow.EntityFramework`
* Several key contributions and bug fixes

### [idubnori](https://github.com/idubnori)

* PostgreSQL implementation
* EntityFramework implementation
* Build and integration test improvements

### [Jaco Coetzee](https://github.com/JC008)

* Several key contributions and bug fixes
* Donated Navicat Essentials for SQLite

### [Jan Feyen](https://github.com/janfeyen)

* Key MongoDB contributions

### [Rasmus Mikkelsen](https://github.com/rasmus)

* Original creator and author of EventFlow

### [Rida Messaoudene](https://github.com/rmess)

* PostgreSQL implementation

### [Willem Peters](https://github.com/wgtmpeters)

* MongoDB cleanup and move to main repository

### [Przemysław Andruszewski](https://github.com/przemyslawandruszewski)

* SQL Server and PostgreSQL query generation cleanup

```

### File: global.json
```json
{
  "sdk": {
    "version": "10.0.100",
    "rollForward": "latestFeature"
  }
}

```

### File: RELEASE_NOTES.md
```md
### New in 1.2.4 (not released yet)

### New in 1.2.3 (released 2025-12-06)

- New: Compiled and packaged for .NET 10, which has the dependency on `System.Linq.Async` removed

### New in 1.2.2 (released 2025-10-11)

* Fix: Use the ASP.NET Core shared framework reference for non-`netstandard` targets in `EventFlow.AspNetCore` to avoid redundant package references (thanks @thompson-tomo)
* Fix: Replace FluentAssertions with Shouldly across the solution to simplify assertion usage (thanks @Focus1337)
* Fix: Lean on framework-provided `Microsoft.CSharp` where available to trim redundant package references (fixes #1107, thanks @thompson-tomo)
* Fix: Cleaned up major parts of the documentation hosted on https://geteventflow.net/
* Fix: Resolved Hangfire delayed job scheduling bug by switching to the correct `Schedule` API (fixes #1104)
* Fix: Restore Hangfire job runner backward compatibility with EventFlow 0.x by reintroducing legacy overloads (fixes #1109)

### New in 1.2.1 (released 2025-05-29)

* Fix: Prevent multiple calls of the same async subscribers when dispatching events (by @alexeyfv)
* Fix: Better exception handling and propagation in `ReadModelPopulator`

### New in 1.2.0 (released 2025-03-09)

* New: New NuGet package `EventFlow.SourceGenerators` created by @alexeyfv. See
  [documentation](https://geteventflow.net/additional/source-generation/) for details
* New: NuGet `EventFlow.SQLite` is now released as part of v1 and enables support for SQLite
* New: NuGet `EventFlow.EntityFramework` now ported to v1 (thanks @MMonrad)
* Fix: Upgrade `EventFlow.MongoDB` reference of `MongoDB.Driver` from `2.19.0` to `[3.0.0,4.0)` (thanks @tniessner)
* Fix: Invoking `UseEventPersistence` now removes any previously registered event persistence. This
  fixes a service ordering issue in the following event store configurations
  - MongoDB
  - MSSQL
  - PostgreSQL

*Sorry for the delay.*

### New in 1.1.0 (released 2024-12-16)

* New: More control of event naming by introducing the interface `IEventNamingStrategy`, see the
  updated documentation at https://geteventflow.net/additional/event-naming-strategies/ for more
  information (thanks @SeWaS)

### New in 1.0.5007 (released 2024-11-16)

Read the complete migration guide to get the full list of changes as well as recommendations
on how to do the migration.

https://geteventflow.net/migrations/v0-to-v1/

(If you see any changes you feel ownership of and you want you name there, create an issue
and it will get fixed asap. EventFlow would be where it is today without the grate community
contributions that it have received over the years)

Changes since last 1.x pre-release, `1.0.5003-alpha`

* New: .NET 8 support
* New: Enable `IEventStore` to load events to a given sequence number (thanks @SeWaS)
* New: `EventFlow.Hangfire` now part of the v1 release cycle (thanks @nicolaj-hartmann)
* Fix/breaking: Switch from `System.Data.SqlClient` to `Microsoft.Data.SqlClient` (thanks @janrybka)

Changes since last 1.x pre-release, `1.0.5002-alpha`

* New: Read model rebuilder can be done across multiple read model types. The piping of events
  and applying them are now done concurrently to reduced memory usage and significantly improve
  time to completion (by @kyle-bradley)
* New: Created `EventFlow.Redis` (by @joshua211)
* New: Migrated `EventFlow.RabbitMQ` to v1 (by @kyle-bradley)
* Breaking: Removed old `EventFlow.Shims.Tasks` class that provided a wrapper for `Task.CompletedTask`
  in frameworks that did not have it

Changes since last 1.x pre-release, `1.0.5001-alpha`

* New/breaking: `IEventUpgrader<,>` are now (finally) async. For an easy upgrade experience,
  use the new base class `EventUpgraderNonAsync` for any existing upgraders. Its a `abstract`
  class that implements the updated interface and provides a `abstract` method with the same
  signature as the previous interface
* Fix/breaking: Event upgraders are now used during read model population. As the upgraders
  are re-used across multiple aggregates, there is a high likelihood that some additions are
  needed in any existing upgraders. Upgraders are stored on the new `IEventUpgradeContext`,
  which is created by the new `IEventUpgradeContextFactory`. Replace this if you need addition
  context during event upgrades
* Fix: `SnapshotAggregateRoot` now correctly loads previous source IDs as well
  adds the current source ID that triggered the snapshot. This causes the
  `DuplicateOperationException` to be correctly thrown if a duplicate source
  ID as added before a snapshot was taken
* Fix: Upgrade `Newtonsoft.Json` from `11.0.2` to `13.0.1` to fix DoS
  vulnerability
  - https://github.com/advisories/GHSA-5crp-9r3c-p9vr
  - https://security.snyk.io/vuln/SNYK-DOTNET-NEWTONSOFTJSON-2774678
* Fix: `UseFilesEventPersistence` should no longer throw exception for .NET regarding relative paths

Complete 1.0 change log

* New: Read model rebuilder can be done across multiple read model types. The piping of events
  and applying them are now done concurrently to reduced memory usage and significantly improve
  time to completion (by @kyle-bradley)
* New: Created `EventFlow.Redis` (by @joshua211)
* New/breaking: Replace internal IoC implementation with `Microsoft.Extensions.DependencyInjection`
* New/breaking: Replace internal logging implementation with `Microsoft.Extensions.Logging`
* New/breaking: SQL read models now support different connection strings using the
  `[SqlReadModelConnectionStringName]` attribute. To allow executing queries using different
  connection strings, all methods on `IMsSqlConnection` and `ISqlConnection` now have an
  additional argument, `string connectionStringName` to signify which connection string
  should be used for the query
* New/breaking: SQL connection strings are now fetched from the
  `SqlConfiguration<T>.GetConnectionStringAsync(...)` instead of a property, allowing more
  control of the connection string used at runtime
* New/breaking: `IEventUpgrader<,>` are now (finally) async. For an easy upgrade experience,
  use the new base class `EventUpgraderNonAsync` for any existing upgraders. Its a `abstract`
  class that implements the updated interface and provides a `abstract` method with the same
  signature as the previous interface
* New: Its now possible to change the execution timeout for database migrations using the
  `SetUpgradeExecutionTimeout(...)` on the SQL configuration
* Fix/breaking: Event upgraders are now used during read model population. As the upgraders
  are re-used across multiple aggregates, there is a high likelihood that some additions are
  needed in any existing upgraders. Upgraders are stored on the new `IEventUpgradeContext`,
  which is created by the new `IEventUpgradeContextFactory`. Replace this if you need addition
  context during event upgrades
* Breaking: Removed the following dead and/or confusion MSSQL attributes. The real ones
  are named the same, with with `Sql...` instead of `MsSql...`
  - `MsSqlReadModelIdentityColumn`
  - `MsSqlReadModelIgnoreColumn`
  - `MsSqlReadModelVersionColumn`
* Breaking: Methods on `IMsSqlDatabaseMigrator` and `ISqlDatabaseMigrator` have been
  made async and have an extra `CancellationToken` argument
* Breaking: Remove support for .NET Framework and consolidate on .NET (Core) LTS versions
* Breaking: Replace internal in-memory caching with `Microsoft.Extensions.Caching.Memory`
* Breaking: Removed `IAmAsyncReadModelFor` and made `IAmReadModelFor` async
* Breaking: Removed `EventFlow.Core.AsyncHelper` as well as all async wrapper methods
  that used it
  - `IAggregateStore.Load`
  - `IAggregateStore.Store`
  - `IAggregateStore.Update`
  - `ICommandBus.Publish`
  - `IEventStore.LoadAggregate`
  - `IEventStore.LoadEvents`
  - `IEventStore.LoadAllEvents`
  - `IQueryProcessor.Process`
  - `IReadModelPopulator.Populate`
  - `IReadModelPopulator.Purge`
* Breaking: Removed old `EventFlow.Shims.Tasks` class that provided a wrapper for `Task.CompletedTask`
  in frameworks that did not have it
* Fix: `SnapshotAggregateRoot` now correctly loads previous source IDs as well
  adds the current source ID that triggered the snapshot. This causes the
  `DuplicateOperationException` to be correctly thrown if a duplicate source
  ID as added before a snapshot was taken
* Fix: Upgrade `Newtonsoft.Json` from `11.0.2` to `13.0.1` to fix DoS
  vulnerability
  - https://github.com/advisories/GHSA-5crp-9r3c-p9vr
  - https://security.snyk.io/vuln/SNYK-DOTNET-NEWTONSOFTJSON-2774678
* Version of 0.x included: `0.83.4713`. 0.x changes are merged to 1.x at regular
  intervals, but might be one or two releases behind


### New in 0.83.4713 (released 2021-09-07)

* New: Queue name used by HangfireJobScheduler can be overridden:
  ```csharp
  eventFlowOptions.UseHangfireJobScheduler(o => o.UseQueueName("myqueue"))
  ```
* Fixed: Do not throw `MetadataKeyNotFoundException` if there is no meta data on
  `previous_source_ids` in snapshots

### New in 0.82.4684 (released 2021-08-31)

* Fix: Allow the use of explicitly implemented interfaces in the read model
* New: added extension methods to the `EventFlow.EntityFramework` package that allow
  us to configure [eager loading of related data](https://docs.microsoft.com/en-us/ef/core/querying/related-data/eager). Example usage:
  ```csharp
  public static IEventFlowOptions Configure(this IEventFlowOptions options)
  {
    return options
      .UseEntityFrameworkReadModel<MyEntity, MyDbContext>(
        cfg => cfg.Include(x => x.SomeProperty)
                  .ThenInclude(y => y.SomeOtherProperty)
      );
  }
  ```

### New in 0.82.4659 (released 2021-06-17)

* Fix: Source IDs are now added to snapshots
* Fix: InMemoryReadStore will not break on unmodified update result

### New in 0.81.4483 (released 2020-12-14)

* Breaking: Elasticsearch NEST Nuget Library updated from v6.1.0 to v7.8.2
* New: Now possible to implement error handlers for specific sagas using
  `ISagaErrorHandler<TSaga>`
* Fixed: You can now create `Id : Identity<Id>`

### New in 0.80.4377 (released 2020-10-01)

* Breaking: To support .NET going forward, all EventFlow test have been converted
  from .NET Framework 4.x to .NET Core 3.1. This however, introduced a set of
  breaking changes
  * EntityFramework has been updated from 2.2.6 to 3.1.5 
  * `IHangfireJobRunner.Execute` is now `IHangfireJobRunner.ExecuteAsync`
* Breaking: Merged `AggregateReadStoreManager` and `SingleAggregateReadStoreManager`
  into one class in order to always guarantee in-order event processing
* Breaking: Marked the `UseReadStoreFor<,,,>` configuration methods as obsolete,
  in favor of the simpler overloads with less type parameters (as those automatically
  figure out the AggregateRoot and Id types and configure the more reliable 
  `SingleAggregateReadStoreManager` implementation)
* Obsolete: The class `AsyncHelper` and all non-async methods using it have been
  marked obsolete and will be removed in EventFlow 1.0 (not planned yet). If you rely
  on these non-async methods, then merely copy-paste the `AsyncHelper` from the EventFlow
  code base and continue using it in your transition to async only 
* Fixed: An issue where `EntityFrameworkEventPersistence` could possibly save aggregate 
  events out of order, which would lead to out-of-order application when streaming events
  ordered by GlobalSequenceNumber
* New: `FilesEventPersistence` now uses relative paths
* New: A new set of hook-in interfaces are provided from this release, which should
  make it easier to implement crash resilience (#439) in EventFlow. Please note that
  this new API is experimentational and subject to change as different strategies are
  implemented
  * `IAggregateStoreResilienceStrategy`
  * `IDispatchToReadStoresResilienceStrategy`
  * `IDispatchToSubscriberResilienceStrategy`
  * `ISagaUpdateResilienceStrategy`

### New in 0.79.4216 (released 2020-05-13)

* New: Added .NET Core 3.1 target for the `EventFlow`
  and `EventFlow.EntityFramework` packages
* Added quoting to the SQL query generator for the column names

### New in 0.78.4205 (released 2020-05-11)

* New: Updated LibLog provider to support structured logging with NLog 4.5. 
  Reduced memory allocations for log4net-provider
* New: Made several methods in `AggregateRoot<,>` `virtual` to allow
  easier customization
* Fixed: Added quoting to the SQL query generator for the column names
```sql
  -- query before the fix
    UPDATE [ReadModel-TestAttributes]
    SET UpdatedTime = @UpdatedTime
    WHERE Id = @Id
  
  -- query after the fix
    UPDATE [ReadModel-TestAttributes]
    SET [UpdatedTime] = @UpdatedTime
    WHERE [Id] = @Id
  ```
* Fixed: Do not log about event upgraders if none is found for an event
* Fixed: Add default `null` predicate to `AddCommands` and `AddJobs`

### New in 0.77.4077 (released 2019-12-10)

* New: The `EventFlow.AspNetCore` NuGet package now has ASP.NET Core 3 support

### New in 0.76.4014 (released 2019-10-19)

* New: Mongo DB read model store Queryable:
  ```csharp
  MongoDbReadModelStore readModelStore;
  IQueryable<TReadModel> queryable = readModelStore.AsQueryable();
  ```
* New: Moved publish of messages in `RabbitMqPublisher` to a new virtual
  method to ease reuse and customization
* Fixed: MongoDB read models no longer has the `new()` generic requirement,
  which aligns read model requirements with the rest of EventFlow

### New in 0.75.3970 (released 2019-09-12)

* Fix: When deserializing the JSON value `"null"` into a struct value like
  `int`, the `SingleValueObjectConverter` threw an exception instead of
  merely returning `null` representing an absent `SingleValueObject<int>` value

### New in 0.74.3948 (released 2019-07-01)

* Breaking: Renamed `AspNetCoreEventFlowOptions.AddMetadataProviders()` 
  to `AddDefaultMetadataProviders()` and made `AddUserClaimsMetadata` opt-in
  in order to prevent policy issues. 
* Fix: Allow explicit implementations of `IEmit<>` in aggregate roots
* Fix: Using `.AddAspNetCore()` with defaults now doesn't throw a DI
  exception.

### New in 0.73.3933 (released 2019-06-11)

* New: Configure JSON serialization: 
  ```csharp
  EventFlowOptions.New.
    .ConfigureJson(json => json
      .AddSingleValueObjects()
      .AddConverter<SomeConverter>()
    )
  ```
* New: ASP.NET Core enhancements:
  - New fluent configuration API for ASP.NET Core components:
    `services.AddEventFlow(o => o.AddAspNetCore(c => {...}));` (old syntax
    `AddAspNetCoreMetadataProviders` is now deprecated).
  - `.RunBootstrapperOnHostStartup()` runs bootstrappers together with ASP.NET
    host startup. Previously, this was done in `AddAspNetCoreMetadataProviders`
    and led to some confusion.
  - `.UseMvcJsonOptions()` adds EventFlow JSON configuration (see below) to ASP.NET Core,
    so you can accept and return Single Value Objects as plain strings for example.
  - `.Add{Whatever}Metadata()` configures specific metadata provider.
  - `.AddUserClaimsMetadata(params string claimTyp
... [TRUNCATED]
```

### File: .devcontainer\devcontainer.json
```json
{
  "name": "EventFlow Framework",
  "service": "event-flow-framework",
  "dockerComposeFile": ["./docker-compose.yml"],
  "settings": {},
  "extensions": [
    "ms-dotnettools.csharp",
    "streetsidesoftware.code-spell-checker",    
    "k--kato.docomment",
    "editorconfig.editorconfig",
    "heaths.vscode-guid",
    "jchannon.csharpextensions",
    "aaron-bond.better-comments",
    "kiteco.kite",
    "esbenp.prettier-vscode"
    ],
  "workspaceFolder": "/workspace",
  "remoteUser": "vscode",
  "shutdownAction": "none"
}

```

### File: .github\copilot-instructions.md
```md
# Copilot Instructions for EventFlow

These guidelines govern contributions within the EventFlow code base hosted at https://github.com/eventflow/EventFlow/. Follow them whenever collaborating in this repository to stay aligned with the project’s expectations.

## Architecture snapshot
- EventFlow is a CQRS+ES framework; the core runtime lives in `Source/EventFlow` and exposes aggregates, commands, queries, read stores, sagas, jobs, and snapshots.
- Command flow: clients call `CommandBus` (`Source/EventFlow/CommandBus.cs`) which resolves handlers, invokes aggregates deriving from `AggregateRoot<TAggregate, TIdentity>`, and emits events that pipe through subscribers and read-store dispatchers.
- Aggregates load and persist via `IAggregateStore`/`IEventStore`; defaults use the in-memory persistence registered in `EventFlowOptions`, while integration packages under `Source/EventFlow.*` swap in specific stores.
- Read models implement `IReadModel` plus `IAmReadModelFor<...>`; dispatch logic sits in `ReadStores` and uses metadata to map events to view updates.
- Sagas and jobs live under `Source/EventFlow/Sagas` and `Source/EventFlow/Jobs`, coordinating cross-aggregate workflows and deferred execution.
- Documentation that explains the concepts is checked in under `Documentation/`; updates should travel with code changes.

## Extension & configuration guide
- Dependency injection starts with `services.AddEventFlow(o => { ... })` (`Source/EventFlow/Extensions/ServiceCollectionExtensions.cs`); chain option methods to register events, commands, read models, snapshots, sagas, and custom services.
- Use the fluent helpers in `EventFlowOptions` (`Source/EventFlow/EventFlowOptions.cs`) such as `.AddEvents`, `.AddCommands`, `.UseInMemoryReadStoreFor<TReadModel>()`, `.ConfigureOptimisticConcurrencyRetry(...)`, or `.UseEventPersistence<T>()` to pivot storage/backends.
- Strongly typed IDs must derive from `Identity<T>` (`Source/EventFlow/Core/Identity.cs`); create new IDs via `ExampleId.New` or `Identity<T>.With(Guid)` to honor prefix validation.
- When adding domain objects, follow the naming pattern `ThingyAggregate` + `ThingyId` + `ThingyEvent`; see `EventFlow.TestHelpers/Aggregates/Thingy*` for canonical examples including event emit/apply patterns.
- Integration modules (MongoDB, MsSql, PostgreSql, Redis, SQLite, etc.) expose option extensions in their `Extensions/` folder; replicate those patterns when introducing new infrastructure.
- Prefer using `EventFlow.TestHelpers` base classes and fixtures when authoring tests so categories, logging, and deterministic IDs behave consistently.

## Build, test, and verification
- The solution is organized under `EventFlow.sln`; build with `dotnet build EventFlow.sln` (warnings are treated as errors via `Source/Directory.Build.props`).
- Unit tests target `netcoreapp3.1`, `net6.0`, and `net8.0`; run fast feedback with `dotnet test EventFlow.sln --filter "Category!=integration"` and rely on `EventFlow.TestHelpers.Categories` constants when tagging new suites.
- Integration tests span external services (MongoDB, PostgreSQL, SQL Server, RabbitMQ, Elasticsearch, EventStore); start containers with `docker-compose up` before executing the corresponding `*.Tests` projects or include the `integration` category filter.
- Source generators and analyzers live in `Source/EventFlow.SourceGenerators` and `Source/EventFlow.CodeStyle`; ensure the .NET SDK version supports C# 12 and keep analyzer warnings clean.
- Documentation builds use MkDocs (`requirements.txt`); run `pip install -r requirements.txt` followed by `mkdocs serve` when verifying doc updates.

## Coding conventions & review tips
- Favor async APIs and accept `CancellationToken` parameters throughout—the core dispatchers expect cooperative cancellation (see `CommandBus.PublishAsync` and `AggregateStore` methods).
- New events should inherit `AggregateEvent<TAggregate, TIdentity>`, carry immutable data, and rely on aggregate `Apply` methods to mutate state; never mutate state directly inside command handlers.
- Subscribers and read stores should request dependencies via constructor injection and avoid static singletons; look at `Source/EventFlow/Subscribers` for the expected interface contracts.
- When wiring new persistence, register required DI services before calling `.UseEventPersistence<T>()` to avoid the `RemoveAll<IEventPersistence>()` guard removing your registration.
- Keep public APIs binary compatible where possible; breaking changes require updates in `Documentation/` and `RELEASE_NOTES.md`.
- Mirror existing namespace layout (`EventFlow.{Feature}`) and group files into folders matching their conceptual role to keep source generators and discovery heuristics effective.

## Operational safeguards
- Avoid invoking GitHub management tools that mutate remote state (issues, pull requests, repositories, projects, workflows, labels, security alerts, notifications, etc.) unless the user has granted explicit permission in the current conversation.
- Never run mutating `git` commands (commit, push, merge, rebase, reset, clean, etc.) without explicit user authorization; limit `git` usage to read-only inspection by default.
- If permission is unclear, pause and ask the user before attempting any action that could alter repository or GitHub state.

```

### File: .github\workflows\analyze.yaml
```yaml
name: Perform an issue analysis

on:
  issue_comment:
    types: [created]

permissions:
  issues: write
  checks: read
  contents: read

jobs:
  pipeline:
    uses: rasmus/workflow-review/.github/workflows/analyze.yaml@v2
    with:
      issue_number: ${{ github.event.issue.number }}
      allowlist: "rasmus"
    secrets:
      openai_api_key: ${{ secrets.OPENAI_API_KEY }}

```

### File: .github\workflows\codeql-analysis.yaml
```yaml
name: "CodeQL"

on:
  push:
    branches: [ develop-v1, develop-v*, release-v* ]
  pull_request:
    # The branches below must be a subset of the branches above
    branches: [ develop-v1 ]
  schedule:
    - cron: '30 3 * * 1'

jobs:
  analyze:
    name: Analyze
    runs-on: ubuntu-latest
    permissions:
      actions: read
      contents: read
      security-events: write

    strategy:
      fail-fast: false
      matrix:
        language: [ 'csharp' ]

    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Setup .NET
      uses: actions/setup-dotnet@v4
      with:
        dotnet-version: |
          3.1.x
          6.0.x
          8.0.x

    # Initializes the CodeQL tools for scanning.
    - name: Initialize CodeQL
      uses: github/codeql-action/init@v3
      with:
        languages: ${{ matrix.language }}

    - name: Autobuild
      uses: github/codeql-action/autobuild@v3

    # ℹ️ Command-line programs to run using the OS shell.
    # 📚 https://git.io/JvXDl

    # ✏️ If the Autobuild fails above, remove it and uncomment the following three lines
    #    and modify them (or add more) to build your code if your project
    #    uses a compiled language

    #- run: |
    #   make bootstrap
    #   make release

    - name: Perform CodeQL Analysis
      uses: github/codeql-action/analyze@v3

```

### File: .github\workflows\docs.yaml
```yaml
name: docs 

on:
  push:
    branches:
      - develop-v1

jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v5
        with:
          python-version: 3.x

      - run: pip install -r requirements.txt

      - run: mkdocs gh-deploy --force
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          MKDOCS_GIT_COMMITTERS_APIKEY: ${{ secrets.GITHUB_TOKEN }}

```

### File: .github\workflows\pipeline.yaml
```yaml
name: pipeline

on:
  workflow_call:
    inputs:
      # REQUIRED ============================
      version:
        required: true
        type: string
      # OPTIONAL ============================
      bake-convention:
        required: false
        default: 'default'
        type: string
      bake-version:
        required: false
        type: string
        default: '0.37.51'
      environment:
        required: false
        type: string
        default: 'develop'
    secrets:
      nuget-api-key:
        required: false

jobs:
  build:
    runs-on:
    - ubuntu-22.04

    environment: 
      name: ${{ inputs.environment }}

    env:
      HELPZ_POSTGRESQL_PASS: Password12!
      EVENTFLOW_MSSQL_SERVER: 127.0.0.1,1433
      EVENTFLOW_MSSQL_USER: sa
      EVENTFLOW_MSSQL_PASS: Password12!
      NUGET_APIKEY: ${{ secrets.nuget-api-key }}

    services:
      rabbitmq:
        image: rabbitmq:3-management-alpine
        env:
          RABBITMQ_DEFAULT_USER: guest
          RABBITMQ_DEFAULT_PASS: guest
        ports:
          - 5672:5672
          - 15672:15672

      eventstore:
        image: eventstore/eventstore:release-4.1.3
        ports:
          - "1113:1113"
          - "2113:2113"

      postgres:
        image: postgres:10
        env:
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: Password12!
        ports:
          - "5432:5432"

      mssql:
        image: mcr.microsoft.com/mssql/server:2017-latest
        env:
          ACCEPT_EULA: Y
          SA_PASSWORD: Password12!
        ports:
          - "1433:1433"

    steps:
    - name: Configure sysctl limits for Elasticsearch
      run: |
        sudo swapoff -a
        sudo sysctl -w vm.swappiness=1
        sudo sysctl -w fs.file-max=262144
        sudo sysctl -w vm.max_map_count=262144

    - name: Run Elasticsearch
      uses: elastic/elastic-github-actions/elasticsearch@master
      with:
        stack-version: 6.8.3

    - uses: actions/checkout@v3

    - name: Setup .NET
      uses: actions/setup-dotnet@v4
      with:
        dotnet-version: |
          3.1.x
          6.0.x
          8.0.x

    # Yes, EventFlow has a custom built build tool. If you are reading this
    # you might have a better idea of how to do it alternatively, if so,
    # create a PR for EventFlow.

    # https://github.com/rasmus/Bake
    - name: Install Bake 
      run: dotnet tool install -g --version ${{ inputs.bake-version }} Bake 

    - name: Run Bake
      env:
        MKDOCS_GIT_COMMITTERS_APIKEY: ${{ secrets.GITHUB_TOKEN }}
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      run: |
        bake run \
          --convention=${{ inputs.bake-convention }} \
          --build-version ${{ inputs.version }} \
          --destination="nuget>github,nuget,release>github"

    - name: Upload NuGet packages
      uses: actions/upload-artifact@v4
      if: success()
      with:
        name: packages
        path: "**/*nupkg"
        if-no-files-found: error

    - name: Upload test results
      uses: actions/upload-artifact@v4
      if: success() || failure()
      with:
        name: test-results
        path: "**/*.trx"
        if-no-files-found: error

```

### File: .github\workflows\pull-requests.yaml
```yaml
name: pull-requests

on:
  push:
    branches: [ develop-v1 ]
  pull_request:
    branches: [ develop-v1 ]

permissions:
  contents: read

jobs:
  pipeline:
    uses: ./.github/workflows/pipeline.yaml
    with:
      version: "1.2.3-pr${{ github.event.number }}-b${{ github.run_number }}"

```

### File: .github\workflows\release.yaml
```yaml
name: release

on:
  push:
    branches: [ release-v1 ]

permissions:
  contents: write
  packages: write

jobs:
  pipeline:
    uses: ./.github/workflows/pipeline.yaml
    with:
      bake-convention: 'Release'
      environment: 'release'
      version: "1.2.3"
    secrets:
      nuget-api-key: ${{ secrets.NUGET_APIKEY }}

```

### File: .github\workflows\review.yaml
```yaml
name: Perform a code review

on:
  issue_comment:
    types: [created]

permissions:
  pull-requests: write
  issues: write
  checks: read
  contents: read

jobs:
  pipeline:
    uses: rasmus/workflow-review/.github/workflows/review.yaml@v2
    with:
      pull_request_number: ${{ github.event.issue.number }}
      allow_drafts: "true"
      allow_forks: "true"
      allowlist: "rasmus"
      skip_ci: "true"
    secrets:
      openai_api_key: ${{ secrets.OPENAI_API_KEY }}

```

### File: .github\workflows\stale.yaml
```yaml
name: 'Close stale issues and PRs'

on:
  push:
    branches: [ develop-v1 ]
  schedule:
    - cron: '0 9 * * *'

permissions:
  contents: write
  issues: write
  pull-requests: write

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v8
        with:
          stale-issue-message: |
            Hello there! 

            We hope you are doing well. We noticed that this issue has not seen any activity in the past 90 days.
            We consider this issue to be stale and will be closing it within the next seven days. 

            If you still require assistance with this issue, please feel free to reopen it or create a new issue. 

            Thank you for your understanding and cooperation. 

            Best regards, 
            EventFlow

          close-issue-message: |
            Hello there! 

            This issue has been closed due to inactivity for seven days. If you believe this issue still
            needs attention, please feel free to open a new issue or comment on this one to request its
            reopening. 

            Thank you for your contribution to this repository. 

            Best regards, 
            EventFlow

          stale-pr-message: |
            Hello there! 

            We hope this message finds you well. We wanted to let you know that we have noticed that there has been
            no activity on this pull request for the past 90 days, which makes it a stale pull request. 

            As a result, we will be closing this pull request within the next seven days. If you still
            think this pull request is necessary or relevant, please feel free to update it or leave a
            comment within the next seven days. 

            Thank you for your contributions and understanding.

            Best regards,
            EventFlow

          close-pr-message:
            Hello there! 

            I'm a bot and I wanted to let you know that your pull request has been closed due to inactivity
            after being marked as stale for seven days. 

            If you believe this was done in error, or if you still plan to work on this pull request,
            please don't hesitate to reopen it and let us know. We're always happy to review and
            merge high-quality contributions. 

            Thank you for your interest in our project!

            Best regards,
            EventFlow

          days-before-stale: 90
          days-before-close: 7
          stale-pr-label: stale
          stale-issue-label: stale
          exempt-pr-labels: stale-exempt
          exempt-issue-labels: stale-exempt
          operations-per-run: 1000

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

# Knowledge Dump for Cirqus

## File: changelog.md
```
# d60 Cirqus

## 0.0.5

* Bam!

## 0.0.6

* Changed default behavior of `Load` from within an aggregate root to throw an exception if a root with the specified type/ID does not exist. The behavior can be overridden by setting `createIfNotExists = true` when loading.
* Implemented proper MongoDB-based catch-up view.

## 0.0.15

* Implemented simple SQL server row-based view
* Views get an `IViewContext` now that they can use to load aggregate roots (including the ability to specify which version to load)

## 0.0.16

* Gave event dispatcher the ability to initialize itself

## 0.0.17

* Extended `TestContext` with the ability to dispatch events to views
* Made not-intended-for-others-to-use in-mem versions of some stuff internal

## 0.0.18

* Added serializability check to test context

## 0.0.19

* Added serializability check to all current event stores

## 0.0.20

* Fixed it so that loading an aggregate root during event application will result in loading the correct version of that aggregate root

## 0.0.21

* Made an explicit divide (made it possible, at least) between catch-up and direct-dispatch view managers
* Added LINQ capabilities to MongoDB view manager

## 0.0.22

* Introduced `Created` hook that can be overridden on aggregate roots, e.g. to emit the infamous `YayIWasCreated` event.

## 0.0.23

* Made Entity Framework view manager support LINQ as well and removed the need for that silly global sequence numbers table
* Entity Framework view manager automatically adds index to global sequence number column

## 0.0.27

* Did some repair work and did some more stuff as well.

## 0.0.30

* `Load<TAggregate>
    ` on `AggregateRoot` now loads & caches in the current unit of work, loading & caching the right versions of aggregate roots as well.

    ## 0.0.33

    * Renamed view managers

    ## 0.0.34

    * Divided view manager into push/pull view managers
    * Introduced composite command

    ## 0.0.35

    * Moved event dispatch out of retry loop

    ## 0.1.0

    * Renamed to "Circus" ;)- because when you
say "CQRS" fast enough, that's what it sounds like
    ## 0.1.1
    * Renamed existing e
    vent dispatcher to `ViewManagerEventDispatcher` because it can dispatch events to view managers - that's what makes it special :)
    


   ## 0.1.2
    * Added Azure Service Bus event dispatcher + nuspec
    ## 0.1.3
    * Fixed bug in view managers that could "forget" to upd
    ate `LastGlobalSequenceNumber` on a view - not that will be automatically done
by the `ViewDispatcherHelper`
    ## 0.2.0
    * Renamed to "Cirqus"
- the name that just gets better and better!
    ## 0.2.1
    * Introduced logging + added `ProcessCommand` method to `TestContext`
    ## 0.2.2
    *
    Somemore logging

    

 ## 0.2.3
    * Added NLog integration and added configuration
    option on `Options` to a
llow for configuring logging
    ## 0.2.4
    * Added asynchron
    ous event dispatcher - can be configured by going `.Asynchronous()` on any ordinary dispatcher

## 0.2.5
    * Improved async event dispatcher to use one worker thread per inner dispatcher
    ## 0.3.0

    * Improved `IViewContext` by adding some more context to it (+ ability to load "current" version of an aggregate root - i.e. the global sequence number "roof" is automatically deducted from the domain event currently being han
dled)
    ## 0.4.0
    * Changed `TestContext` to provide a more explicit model for simulating a proper u
    nit of work - can now be accessed by
 going `BeginUnitOfWork` and going all `Commit` and stuff
    ## 0.4.1
    * Fixed bug that would
 result in "forgetting" to invoke the `Created` hook on a new aggregate root when running with the real command processor
    ## 0.4.2
    * Added MongoDB logger factory
    ## 0.4.3
    * Added method to the test conte
    xt that can print the ac
cumulated event history and the emitted events to a text writter, formatted as plain old JSON objects
    ## 0.4.4
    * MIT licensed everything.
    ## 0.5.0
    * Fixed bug that would result in not
 getting a cache hit on 2nd load of the same root from unit of work
    ## 0.6.0
    * Fixed potential odd behavior by having in-mem even
    t store save cloned events instead of the original objects.

    ## 0.6.1

    * Make event stores automatically add event batch ID as a header on all
events  ##
 0.7.0
    * Changed format
    of timestamp metadata to be strings in order to ensure consistent behavior across all event stores + introduced extension method for extracting them

    ## 0.7.1

    * Corrected
spelling in an error message
    ## 0.8.0
    * Changed initialization of async event dispatcher to be async as well
    ## 0.9.0
    * Added Pos
    tgreSQL event store

    ## 0.10.0
    * Changed `TestCon
    text` API so that it can
 return fully hydrated aggregate roots
    ## 0.11.0
    * Made `ProcessCommand` method on `TestC
    ontext` return events th
at were emitted as a result of that command
    ## 0.12.0
    * Removed a lot of generics and reflection
    stuff and made it possible to use the base `Command` to execute logic on arbitrary aggregate roots.

    ## 0.12.1

    * Added `string[]` as a supported property type on `MsSqlViewManager`.  ##
 0.12.2   *
 Allow properties of type `DateTime`, `DateTimeOffset` and `TimeSpan` on `MsSqlViewManager`-managed views
    ## 0.12.3
    * Introduced a fluent configuration
    APIthat will make it easier to discover configuration options + make it harder to end up with e.g. an un-initialized command proce
ssor
    ## 0.13.0
    * Changed logger API to include overloads
    for`Warn` and `Error` that include a real `exception` field
    * Added Serilog integration package

    

 ## 0.14.
    0

    

 * Removed superfluous methods from `ICommandProcessor` interface - it's only ab
    out processing commands n
ow!
    ## 0.14.1
    * Added experimental caching aggregate root repository with a simple in-mem sna
    pshot cache (warning: bet
a!)
    ## 0.15.0
    * Added experimental async-by-default managed views as an alternative to the initial view managers
    ## 0.15.
    1

    

 * Suppor
    t for composite event dispatchers in the configuration API

    ## 0.15.2

    * Added conf
iguration options to Serilog integration
    ## 0.16.0
    * Abi
    lityfor new SQL views to
 have certain propoerties JSON-serialized - just use the `[Json]` attribute on them :)
    * Can now pass
    `ViewManagerWaitHandle` to the new view manager event dispatcher to allow for blocking until certain views have updat
ed
    ## 0.17.0

    * Made `CommandProcessor` and `TestContext` disposable in the hope that someone will dispose them and stop their threads

    ## 0.17.1

    * Comments + more.

    ## 0.17.2
    * Exposed Serilog options on config API
    ## 0.18.0
    * Allow for specifying that certain columns can be `[NotNull]` with the new MsSql vi
    ew manag
er
    ## 0.19.0 * C
hanged `ViewLocator` API to pass the view context, allowing for loading roots during view location
      ##
 0.20.0
    * JSON.NET is now me
    rged into d60.Cirqus, making for an ef
fectively dependency-less core assembly - just how it's supposed to be
    ## 0.20.1
    * Made `Test
    Context` return `CommandProcessingResult` when calling `Save`, so that async views can be blocked until the results are
 visible


    

 ## 0.20.2
    * Fixed bug in `TestContext` that did not correctly serialize the UTC time
    ## 0.20
    .3

    * `NewMsSqlViewManager` can automagically drop & recreate the table when necessary

    ## 0.20.4* Added `HandlerVie
wLocator` that allows for implementing `IGetViewIdsFor<TDomainEvent>
        ` where `TDomainEven
    t` is a domain event or an interface - makes view ID mapping really neat in some situations.


        ## 0.21.0
        This is a big update that completes
    the transition tothe new, vastly improved view managers and makes a load of stuff much more consi
stent.
    * All the ol
d view manager stuff has now been completely replaced by the new view manager.
        * `TestContext` now has an `
    Asynch
ronous` property that can be used to specify that it is to work asynchronously (more realistic with regards to event dispatch).
    *Replaced the `ProcessCommand` method on `TestContext` with one that matched the one on `ICommandProcessor`

    ## 0.22.0

    * Added `InMemoryViewEventDispatcher` which a special in-mem view manager that has events dispatched to it directly - suitable for in-mem, in-process views only (but they're very fast...)

    ## 0.22.1* Fixed bug where loading a nonexistent aggregate root from a view did not throw an exception

    ## 0.22.2

    * Better `ToString` on `CommandProc
essingResult`
        ## 0.23.0
        * Added ability for `MsSqlViewManager`-views to
    "find rest", which is crucial when you
 want to support blocking on a view - a separate table is used to implement this feature
        #
    # 0.24.0* Store current position in separate collection for `MongoDbViewManager` to avoid having to deal with the special position document popping up in query results

    ## 0.24.1
    * Made `InMemoryEventStore` reentrant by serializing access to the inner list of committed event batches

    ## 0.24.2
  * Added experimental TypeScript code generator
        ## 0.24.3
        * Silly `Assembly.LoadFile` must always be called with an
    absolute p
ath
      ##
 0.24.4
        * Map `object` to `any`
        ## 0.25.0
    * Added initial version of an `EventR
eplicator` - can probably be brought to do all kinds of interesting things :)
    * Added `Updated` event to the typed view manager and made all the existing view managers raise the event a<TDomainEvent>
        rVie
        ` where `TDomainEven
        t` i
s a domain event or an interface - makes view ID mapping really neat in some situations.
        ## 0.21.0
        This is a big update that completes the transition to the new, vastly improved view manage
rs and makes a load of stuff much more consistent.
        * Al
        l the old view manager stuff has now been completely replaced by the new view manager.
        * `TestContext` now has an `Asynchronous` property that can be used to specify that it is to work asynchronously (more realistic with regards to event dispatch
).
        * Replaced the `ProcessCommand` method on `TestContext` with
one that matched the one on `ICommandProcessor`
           #
# 0.22.0       * Added `InMemoryViewEventDispatcher` which a special in-mem view manager that has events dispatched to it dire
ctly - suitable for in-mem, in-process views only (but they're very fast...)
        ## 0.22.1
        * Fixed
         bug
 where loading a nonexistent aggregate root from a view did not throw an exception
        ## 0.22.2
        * Better `ToString` on `CommandProcessingResult`
        

      ## 0.23.0
        * Added ability for `MsSqlViewManager`-views to "find rest", which is crucial when you want to support bloc
        king
 on a view - a separate table is used to implement this feature
        ## 0.24.0
        * Store current
        position in separate collection for `MongoDbViewManager` to avoid having to deal with the special position document popping up in query results
        

      ## 0.24.1
        * Made `InMemoryEventStore` reentrant by serializing access to the inner list of committed event batches
        ## 0.24.2
        * Added experimental TypeSc
        ript
 code generator
        ## 0.24.3
        * Silly `Assembly.LoadFile` must always be called with an absolute path       ## 0.24.4

        


       *
        Map
`object` to `any`## 0.25.0* Added initial version of an `
EventReplicator` - can probably be brought to do all kinds of interesting things :)
        * Ad
        ded`Updated` event to the typed view manager and made all the existing view managers raise the event at the right time.
        * Fixed usageof `Nullable<>` on data types like `Guid`, `int`, etc. on `
MsSqlViewManager`
        ## 0.25.1
        * Re-introduced the Entity Framework-based
        view manager - be warned though: it leaves de
referenced child objects in the database with NULL foreign keys
        ## 0.26.0
        * Changed view dispatcher to support polymorphic dispatch - i.e. views can now imp
        lement e.g. `ISubscribeTo<DomainEvent<SomeParticularRoot>>` in order to get everything that happens on `SomeParticularRoot` or `ISubscribeTo<DomainEvent>` to get everything

        ## 0.26.1

        * Changed Entity Framework view manager touse the _sloooow_ OR-mapper-
way of purging data - it's slow, but it cascades to tables with FK constraints and whatnot
## 0.26.2
* Removed annoying log line from `ViewManagerEventDispat
        cher
`
## 0
        .26.3


* Re-publishing because silly NuGet.org failed in the middle of uploading 0.26.2
## 0.27.0
* Moved `TestContext` into cor
        e because it's just easier that way


## 0.28.
        0

        * Remov
ed JSON.NET dependency from MongoDB stuff by merging it in
## 0.29.0
* Validate that collection prop
        erties of Entity Framework views are declared as virtual (otherwise the view might le
ave a trail of non-disconnected should-have-been-orphans in the database)
## 0.30.0
* Added file system-based event store implementat
        ion - thanks [asgerhallas]
        * Added SQLite-bas
ed event store implementation
* Include view positions in timeout exceptio
        n when `TestContext` is waiting for views to catch up


## 0.31.0
* Removed MongoDB dep from nuspec (it didn't actually depend
        on it anyway, since it was merge in)
        
##
 0.32.0
*
        Added cr
ude MongoDB JSON serialization/deserialization mutator hooks
## 0.33.0
* Added simple profiler that can be used
        to record time spent doing various
 core operations
## 0.34.0
* Removed aggregate root repository reference fro
        m aggregate root because it would accidentally avoid decorators and this bypass caching
* Added event dispatch timing to `IProfiler`
## 0.35.0
* Moved file-based event store into core because it has no depend
        encies - thanks [asge
rhallas]
        * Moved SQL Server event store and view manager into core because they too have no dependencie
s
## 0.36.0
* Added an Azure Service Bus Relay-based event store proxy and an `IE
        ventDispatcher` impleme
ntation that is an event store (readonly-)host
## 0.36.1
* Added ability for `EventRepli
        cator`to wait a configurable a
mount of time in the event that an error occurs (chill down, don't spam the logs...)
## 0.36.2
* Fixed bug in configuration API that would always reg
        ister Azure event dispatchers
 as primary
## 0.36.3
* Fixed max message size in ASB relay-based event store proxy
## 0.36.4
* Made `NetTcpRelayBinding` configurable from the outside on ASB relay event store proxy thingie
## 0.40.0
* Huge BREAKING change: Event store abs
        traction does not care about serialization now. It may, however, provide special support for various serialization <DomainEvent<SomeParticularRoot>>` in order to get everything that happens on `SomeParticularRoot` or `ISubscribeTo<DomainEvent>` to get everything

## 0.26.1

* Changed Entity Framework view manager to use the _sloooow_ OR-mapper-way of purging data - it's slow, but it cascades to tables with FK constraints and whatnot

## 0.26.2

* Removed annoying log line from `ViewManagerEventDispatcher`

## 0.26.3

* Re-publishing because silly NuGet.org failed in the middle of uploading 0.26.2

## 0.27.0

* Moved `TestContext` into core because it's just easier that way

## 0.28.0

* Removed JSON.NET dependency from MongoDB stuff by merging it in


## 0.29.0

* Validate that collection properties of Entity Framework views are declared as virtual (otherwise the view might leave a trail of non-disconnected should-have-been-orphans in the database)

## 0.30.0

* Added file system-based event store implementation - thanks [asgerhallas]
* Added SQLite-based event store implementation
* Include view positions in timeout exception when `TestContext` is waiting for views to catch up

## 0.31.0

* Removed MongoDB dep from nuspec (it didn't actually depend on it anyway, since it was merge in)

## 0.32.0

* Added crude MongoDB JSON serialization/deserialization mutator hooks

## 0.33.0

* Added simple profiler that can be used to record time spent doing various core operations

## 0.34.0

* Removed aggregate root repository reference from aggregate root because it would accidentally avoid decorators and this bypass caching
* Added event dispatch timing to `IProfiler`

## 0.35.0

* Moved file-based event store into core because it has no dependencies - thanks [asgerhallas]
* Moved SQL Server event store and view manager into core because they too have no dependencies

## 0.36.0

* Added an Azure Service Bus Relay-based event store proxy and an `IEventDispatcher` implementation that is an event store (readonly-)host

## 0.36.1

* Added ability for `EventReplicator` to wait a configurable amount of time in the event that an error occurs (chill down, don't spam the logs...)

## 0.36.2

* Fixed bug in configuration API that would always register Azure event dispatchers as primary

## 0.36.3

* Fixed max message size in ASB relay-based event store proxy

## 0.36.4

* Made `NetTcpRelayBinding` configurable from the outside on ASB relay event store proxy thingie

## 0.40.0

* Huge BREAKING change: Event store abstraction does not care about serialization now. It may, however, provide special support for various serialization formats if that makes sense (JSON comes to mind, in MongoDB or Postgres).
* Allow for defaulting to `NullEventDispatcher` if no event dispatcher is configured.

## 0.41.0

* Added ability to configure a custom serializer
* Added standard binary formatter-based binary .NET serializer

## 0.41.1

* Better error messages when JSON serialization/deserialization fails
* Fixed some things around the new `Event` class

## 0.42.0

* Add event type to metadata of events. I sincerely hope that this will be the last change to the persistence format of the events.

## 0.43.0

* Changed aggregate root ID to be `string`s instead of `Guid`s - thanks [asgerhallas]

## 0.44.0

* Added `IsNew` property to aggregate root which allows for determining whether an instance is new or not
* Fixed `Created` that would not fire when creating aggregate roots from within another aggregate root - thanks [asgerhallas]
* Removed the `Guid` ctor on `Command<>` because it's in the way when using R# to generate ctor in subclasses

## 0.44.1

* Fixed TS Client generator to generate a command processor proxy without the "process" in the names - i.e. a command `DoWhatever` will now yield a `doWhatever` method on the command processor proxy

## 0.44.2

* Removed some accidental `Console.WriteLine` in `ViewManagerEventDispatcher` and `HandlerViewLocator`

## 0.45.0

* Re-introduced the command mapper concept, making `Command` the ultimate base class of all commands (which must be explicitly mapped using the command mapper API) - use either `ExecutableCommand` or the generic `Command<TAggregateRoot>` to supply the command action as part of the command
* Prettified some code - thanks [ssboisen]
* Introduced `IDomainTypeNameMapper` that allows for customizing names of events and aggregate roots as they go into event metadata
* Split `Load` up into `Create`, `TryLoad`, and `Load` - each with appropriate and more explicit behavior
* Relaxed type constraints on `Load` and `TryLoad` methods, allowing for loading as base classes and interfaces
* Optimized `ViewManagerEventDispatcher` to do direct dispatch of events when possible

## 0.46.0

* Made TestContext's event serializer customizable

## 0.46.1

* Added `IAggregateRootRepository` implementation that allows for letting a factory method create the instance - thanks [kimbirkelund]

## 0.46.2

* Made number of domain events per batch configurable in the config API for `ViewManagerEventDispatcher`

## 0.47.0

* Brought back the aggregate root type in the `IProfiler` interface

## 0.48.0

* Slight change in profiler behavior - actuall aggregate root type is registered if possible, otherwise the queries type is used

## 0.49.0

* Fixed pretty subtle bug in `MongoDbEventStore` that surfaces when caching is introduced
* Finished the simple caching event store with a simple age-based eviction strategy

## 0.50.0

* Better way of skipping the unit of work property when generating aggregate root snapshots with the `Sturdylizer`

## 0.51.0

* Added fluent configuration api for TestContext so all dependencies can be switched out or decorated
* Made shortcuts to registration of services in the configuration api and removed the Registrar-property
* Changed the configuration of view managers to a fluent one instead of the plethora of overloads

## 0.52.0

* Automagically add command type name to emitted events
* Fixed bug where unit of work in some circumstances did not cache aggregate roots under their correct global sequence number, thus leading to bad stuff

## 0.53.0

* Moved the auto-added command type name option to a decorator that can be optionally enabled

## 0.54.0

* Added PostgreSQL view manager
* Added testing tools including xUnit and NUnit integration
* Fixed nuget package for NUnit

## 0.55.0

* Fixed missing file dependency in nuget for xunit and nunit

## 0.55.1

* Fixed internal serializer issue in testing harness

## 0.55.2

* Added implicit ids to Emit/Then methods og the test harness
* Added possibility to configure the test context in the test harness

## 0.56.0

* Metadata from commands now flow to emitted events before they are applied to the aggregate root

## 0.57.0

* Added simple profiler hook to `ViewManagerEventDispatcher` - let's see if it turns out to be useful

## 0.58.0

* Made view manager profiler hook more details - now captures time for individual events

## 0.58.1

* Added `StandardViewManagerProfiler` to make simple profiling of views easy

## 0.58.2

* Added `AggregateRootInfo` that can be used as a helper when you want to implement caching

## 0.59.0

* Changed `StandardViewManagerProfiler` model to include number of events with its trackings

## 0.59.1

* Fixed odd missing delegation to inner unit of work in `DefaultViewContext`

## 0.60.0

* Added `Committed` hook to `IUnitOfWork` - will probably turn out to be useful

## 0.60.1

* Made `Sturdylizer` even more sturdy

## 0.60.2

* Made in-mem event cache simpler and trim itself in the background
* Introduced deserialized domain event serializer cache

## 0.60.3

* Enable batching in `EventReplicator`

## 0.60.4

* Fixed odd behavior that would accidentally replay events agains entire pool of view managers when one of them was behind

## 0.60.5

* Fixed support for inherited aggregate roots - thanks [mhertis]
* Fixed subtle bug that would cause waiting for specific view instances to not work

## 0.60.6

* Added support for overriding id generation in test framework

## 0.60.7

* Added support for manipulating the command before executing it in the test framework

## 0.60.8

* Made test harness generate and store IDs for entities

## 0.60.9

* Fixed storing of IDs for entities

## 0.60.10

* support for manipulating the event before emitting it in the test framework

## 0.61.0

* Added support for dependent views - i.e. views that catch up with other views instead of catching up with the event store

## 0.61.1

* Gradually back off from attempting to catch up in the view manager event dispatchers when an error has occurred

## 0.61.2

* Simplified test context setup to support testing the new dependent view event dispatcher

## 0.61.3

* Changed api for test context setup

## 0.61.4

* Added initial HybridDb view manager support
* Fixed metadata flow bug

## 0.61.5

* Added nuspec for HybridDb view manager

## 0.61.6

* Tiny enhancment of HybridDb view manager configuration

## 0.61.7

* Fixed bug that would result in metadata not being set correctly on events emitted in an overridden `Created` method

## 0.61.8

* Fixing configuration in testing harness - again!

## 0.61.9

* Fixing TestContext to handle dependent view managers

## 0.61.10

* Fixing failing test

## 0.62.0

* Added experimental auto-balacing of views among multiple processes (WARNING: not suitable for production just yet)

## 0.62.1

* More intelligent sign-off in automatic view distributor

## 0.62.2

* Enabled batch dispatch capabilities in MongoDB, Postgres, In-mem, and MSSQL view managers

## 0.62.3

* Added debug logging factory - thanks [SamuelDebruyn]

## 0.62.4

* Made dependent view manager event dispatcher actually use the "max domain events per batch" setting

## 0.62.5

* Fixed bug in `MsSqlViewManager` that caused properties of type `bool` and `bool?` to be stored as `NVARCHAR(MAX)`, leading to invalid cast exceptions on update

## 0.62.6

* Added d60.Cirqus.Identity package and added support for Id<T> in the test tools

## 0.62.7

* Fixed failing test

## 0.62.8

* Fxied a misspell in the nuspec

## 0.62.9

* Build script now supports nuspec with multiple Cirqus-dependencies

## 0.62.10

* Can now add custom view context items to ordinary view manager event dispatcher's context

## 0.62.11

* Can now use batched domain events with entityFramework view manager

## 0.63.0

* Introduced `AggregateRootNotFoundException` to let other exceptions that can potentially occur during hydration bubble up properly when `TryLoad`ing

## 0.63.1

* Fixed a bug where dependantviewdispatcher could be in a state with a invalid default MaxDomainEventsPrBatch - set it to 100

## 0.63.2

* Fixed bug where MSSQL event store could return events for an aggregate root out of order (which was pretty unlikely to happen + aggregate roots guard against thist)

## 0.63.3

* Fixed bug in `PostgreSqlViewManager` that would result in never dispatching the first event to anyone - thanks [pvivera]

## 0.63.4

* Fixed missing line breaks in testing tools output
* Added synchronous event dispatcher for testing views and getting sensible exception output

## 0.63.5

* Changes default ID separator to dash (but with an option for slash) to support using IDs directly in URLs
* Added support for a shorter GUID notation for IDs

## 0.63.6

* Fixed a bug in IDs Get-method that I just introduced in 0.63.5

## 0.63.7

* Fixed bug in `CachingEventStoreDecorator` that could result in having many cache trim operations executed in parallel in the background if the execution time exceeds 30 s

## 0.63.8

* Added support for retrieving the type that an id matches by pre-, in- or postfix
* Added support for a shorter GUID notation by default

## 0.63.9

* Upgraded xunit to 2.1

## 0.63.10

* Same as 0.63.9. There was a disturbance on nuget.org that I thought originated from some deploy gone wrong.

## 0.63.11

* Fixed the xunit output that didn't show up

## 0.63.12

* Makes no sense to have reentrant cache trimming in `CachingDomainEventSerializerDecorator`
* Added view type reflection extension on `IViewManager`

## 0.63.13

* Fixed GetHashCode issue on KeyFormat

## 0.63.14

* Fixed TestingHarness for bug when no event was emitted

## 0.63.15

* Making InMemoryEventStore and InMemoryUnitOfWork testing tools public to ease implementing custom event dispatchers

## 0.64.0

* Fixed `Kind` of `DateTime` retrieved by `MsSqlViewManager` to be UTC because that's what it is. The really short version of the description of this problem is: Use `DateTimeOffset`s instead. They are explicit about the fact that they are just a UTC timestamp.
* Added Sunshine Scenario Aggregate Root Load Caching mechanism in `DefaultViewContext` which can provide a nice acceleration in Sunshine Scenarios.
* Updated internal Newtonsoft JSON serializer to 7.0.1

## 0.64.1

* Clean up of the EventDispatcher interface
* Use the configured DomainEventSerializer in the testing tools

## 0.64.2

* Better logging in the event replicator - will now periodically log stats on how many events have been replicated

## 0.64.3

* Made MongoDB event store less eager to fetch data - basically leaves batching to the driver, while still keeping a tight grip on overall paging of the result set

## 0.64.4

* Added logging in the `Retryer` so it is possible to see how many times commands are retried

## 0.64.5

* Added support for testing events not emitted by an aggregate root

## 0.64.6

* Added IDomainEvent as an interface for DomainEvent to enable subscription by custom interfaces while still having access to Meta and ensuring that we are actually dealing with an event (intersection types ala TypeScript would have solved this so elegantly)
* Added an AfterEmit callback to the test harness and renamed the others to a consistent Before/After naming scheme

## 0.64.7

* fixing api for CirqusTestHarness, so a typed id is not required

## 0.64.8

* fixing error in last change

## 0.64.9

* fixing "then" of testing tools to support testing of non aggregate root streams

## 0.64.10

* Asserting on events without When()-call

## 0.64.11

* Fixing xunit test output to work for xunit 2.0

## 0.64.12

* Asserting on events by type only without When()-call

## 0.64.13

* Exposed event store on test context

## 0.64.14

* Added new experimental aggregate root snapshotting mechanism to MongoDB package (can easily be extended to other storages if it turns out to be good)

## 0.64.15

* Tweaked the new MongoDB snapshotting

## 0.64.16

* Tweaked the new MongoDB snapshotting again

## 0.65.0

* Changed new snapshot configuration API to enable other snapshot storages via the `ISnapshotStore` abstraction

## 0.66.0

* Refined API of `ISnapshotStore` and introduced simple in-mem snapshot store
* Made snapshotter do another snapshot after preparation if the preparation 

## 0.66.1

* Further optimization of fast-track: Avoid serializer roundtrip when possible

## 0.66.2

* Optimization of MSSQL event store with drastically improved write performance + slightly improved read performance
* Better error message when an event can suddenly no longer be applied to an aggregate root

## 0.66.3

* Better error message when MSSQL view instance upsert fails

## 0.66.4

* Access to UnitOfWork from ICommandContext + overload on UnitOfWork to emit events from non-aggregate root stream

## 0.67.0

* Updated HybridDB integration to 0.10.0

## 0.67.1

* Fixed ordering in PostgreSQL when loading events for an aggregate root - thanks [enriquein]

## 0.68.0

* Fixed MSSQL event store - avoid `WITH (NOLOCK)` because it is dangerous and fetch batches of 2000 rows

## 0.68.1

* Defensive hydration by `DefaultViewContext` - always checks if in-mem event bactch has something that needs to be applied, which allows for safely loading aggregate roots local events when running on a replicated event store

## 0.69.0

* Add ability to customize `NpgsqlConnection` after its creation (to e.g. supply certificate validation callback) - thanks [enriquein]


[asgerhallas]: https://github.com/asgerhallas
[enriquein]: https://github.com/enriquein
[kimbirkelund]: https://github.com/kimbirkelund
[mhertis]: https://github.com/mhertis
[pvivera]: https://github.com/pvivera
[SamuelDebruyn]: https://github.com/SamuelDebruyn
[ssboisen]: https://github.com/ssboisen

```

## File: license.md
```
The MIT License (MIT)

Copyright (c) 2014 d60

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: README.md
```
# d60 Cirqus

Simple but powerful event sourcing + CQRS kit. 

Provides a model for creating commands, aggregate roots, events, and views,
tying it all up in one simple and neat `CommandProcessor`.

### How simple?

You do this:

```csharp
var processor = CommandProcessor.With()
    .(...)
    .Create();
```

and let the API guide you through selecting an event store, possibly configuring some more stuff as well, and then you can do this:

```csharp
processor.ProcessCommand(myCommand);
```

and then everything will flow from there. The command processor is reentrant and is meant to be kept around for the duration of your application's lifetime. Remember to

```csharp
processor.Dispose();
```
    
when the application shuts down.

### More docs

Check out [the official documentation wiki](https://github.com/d60/Cirqus/wiki).

### Is Cirqus for you?

It depends ;) to answer that question, it is necessary to think a little bit about your
requirements. Cirqus is not in the _extreme high performance camp_ (if there is such a camp),
although it doesn't mean that Cirqus cannot perform extremely well - it's more that on the
following scale:

    Raw performance                  Polished APIs and general usefulness
    ================================================(+)==================

Cirqus is positioned around the `(+)` - it doesn't mean that you cannot achieve great -
excellent even - performance with Cirqus, it just means that certain choices have probably
been made for your with Cirqus that makes certain things easier, even though it may
sacrifice a little bit of raw performance.

And on this scale:

    Complex event processing        Domain-model-centric event processing
    ================================================(+)==================

Cirqus is again positioned around the `(+)` - it is mostly meant to be used in conjunction
with an event-driven domain model, so if you're content with driving everything directly off
of events, you will probably not benefit as much from using Cirqus.

Again, it's not that Cirqus doesn't do complex event processing - Cirqus' views can
easily be brought to do that - it's just that that is not really the focus (at least not with
the existing implementations).

Lastly, on this scale:

    .NET-centric                                            Interoperable
    =================(+)=================================================

it shows that many things are just made extremely easy for you if you're using Cirqus and .NET.
You can of course easily set up something else to read events since all the existing event
stores are simply using JSON to represent their contents, but from time to time a .NET type name 
might show up in the JSON data - which means that it's easier to use from .NET, but not impossible
to use from something else (e.g. to have node.js-driven projections or whatever).


### Configuration example

This is how you can set up a fully functioning command processor, including a view:

```csharp
// configure one single view manager
var viewManager = new MsSqlViewManager<CounterView>("sqltestdb");

// let's create & initialize the command processor
var processor = CommandProcessor.With()
    .EventStore(e => e.UseSqlServer("sqltestdb", "Events"))
    .EventDispatcher(e => e.UseViewManagerEventDispatcher(viewManager))
    .Create();

// use the command processor, possibly from multiple threads,
// for the entire lifetime of your application....

// and then, when your application shuts down:
processor.Dispose();
```


### Elaborate configuration example

If you're interested in seeing which moving parts are involved in the command processor, here's the equivalent
configuration where all the things are wired together manually. As you can see, it's actually fairly simple
(although the configuration API is much more intuitive and concise).

```csharp
// this is the origin of truth - let's keep it in SQL Server!
var eventStore = new MsSqlEventStore("sqltestdb", "Events", 
                                     automaticallyCreateSchema: true);

// aggregate roots are simply built when needed by replaying events
// for the requested root
var repository = new DefaultAggregateRootRepository(eventStore);

// configure one single view manager in another table in our SQL Server
var viewManager = new MsSqlViewManager<CounterView>("sqltestdb", "CounterView", 
                                                    automaticallyCreateSchema: true);

// Cirqus will deliver emitted events to the event dispatcher when they have
//  been persisted
var eventDispatcher = new ViewManagerEventDispatcher(repository, eventStore, viewManager);

// we can create the processor now
var processor = new CommandProcessor(eventStore, repository, eventDispatcher);

// and then, when your application shuts down:
processor.Dispose();
```


### Code example

This is an example of a command whose purpose it is to instruct the `Counter` aggregate root to increment itself by
some specific value, as indicated by the given `delta` parameter:

```csharp
public class IncrementCounter : Command<Counter>
{
    public IncrementCounter(string aggregateRootId, int delta)
        : base(aggregateRootId)
    {
        Delta = delta;
    }

    public int Delta { get; private set; }

    public override void Execute(Counter aggregateRoot)
    {
        aggregateRoot.Increment(Delta);
    }
}
```

Note how the command indicates the type and ID of the aggregate root to address, as well as an `Execute` method that
will be invoked by the framework. Let's take a look at `Counter` - aggregate roots must be based on the
`AggregateRoot` base class and must of course follow the [_emit/apply_ pattern](https://github.com/d60/Cirqus/wiki/Emit-Apply-Pattern)
 for mutating themselves - it looks like this:

```csharp
public class Counter : AggregateRoot, IEmit<CounterIncremented>
{
    int _currentValue;

    public void Increment(int delta)
    {
        Emit(new CounterIncremented(delta));
    }

    public void Apply(CounterIncremented e)
    {
        _currentValue += e.Delta;
    }

    public int CurrentValue
    {
        get { return _currentValue; }
    }

    public double GetSecretBizValue()
    {
        return CurrentValue%2 == 0
            ? Math.PI
            : CurrentValue;
    }
}
```

As you can see, the command's `Execute` method will invoke the `Increment(delta)` method on the root, which
in turn will emit a `CounterIncremented` event, which simply looks like this:

```csharp
public class CounterIncremented : DomainEvent<Counter>
{
    public CounterIncremented(int delta)
    {
        Delta = delta;
    }

    public int Delta { get; private set; }
}
```

The event is immediately applied (via the root's `Apply` method that comes from implementing
`IEmit<CounterIncremented>`), and this is the place where the root is free
to mutate itself - in this case, we increment the private `_currentValue` variable, which serves to demonstrate
that aggregate roots are free to keep their privates private.

Note also how the aggregate root is capable of calculating a secret business value, which happens to alternate
between the counter's value and π, depending on whether the counter's value is odd or even.

Lastly, we have set up a `MsSqlViewManager` that operates on a `CounterView` that looks like this:

```csharp
public class CounterView : IViewInstance<InstancePerAggregateRootLocator>,
    ISubscribeTo<CounterIncremented>
{
    public CounterView()
    {
        SomeRecentBizValues = new List<double>();
    }

    public string Id { get; set; }

    public long LastGlobalSequenceNumber { get; set; }

    public int CurrentValue { get; set; }

    public double SecretBizValue { get; set; }

    public List<double> SomeRecentBizValues { get; set; }

    public void Handle(IViewContext context, CounterIncremented domainEvent)
    {
        CurrentValue += domainEvent.Delta;

        var id = domainEvent.GetAggregateRootId();
        var version = domainEvent.GetGlobalSequenceNumber();
        var counter = context.Load<Counter>(id, version);

        SecretBizValue = counter.GetSecretBizValue();

        SomeRecentBizValues.Add(SecretBizValue);

        // trim to 10 most recent biz values
        while(SomeRecentBizValues.Count > 10) 
            SomeRecentBizValues.RemoveAt(0);
    }
}
```

Views can define how processed events are mapped to view IDs via the `ViewLocator` implementation that closes the `IViewInstance<>`
interface - in this case, we're using `InstancePerAggregateRootLocator` which means that the aggregate root ID of the processed
event is simply used as the ID of the view, in turn resulting in one instance of the view per aggregate root.

In order to actually get to receive events, the view class must implement one or more `ISubscribeTo<>` interfaces - in this case,
we subscribe to `CounterIncremented` which requires that we implement the `Handle` method.

In addition to the two required properties, `Id` and `LastGLobalSequenceNumber`, we've added a property for the current value
of the counter (`CurrentValue`), a property for the secret business value (`SecretBizValue`), and a list that can contain the 
10 most recent business values (`SomeRecentBizValues`).

Note how the `IViewContext` gives access to a `Load` method that can be used by the view to load aggregate roots if it needs to invoke
domain logic to extract certain values out of the domain (like e.g. our secret business value). 

Note also how an aggregate root must be loaded by specifying a global sequence number which will serve as a "roof" for applied event, 
thus ensuring that the loaded aggregate root has the version that corresponds to the time when the event was emitted, thus allowing for
eternally consistent replay of events. It also allows for peeking back and forth in time, but that's a story for another time... ;)

```

## File: _GIT_INGEST.md
```
# OmniClaw Repo Plow: CIV_FETCHED_Cirqus_133125



================================================
FILE: CHANGELOG.md
================================================
# d60 Cirqus

## 0.0.5

* Bam!

## 0.0.6

* Changed default behavior of `Load` from within an aggregate root to throw an exception if a root with the specified type/ID does not exist. The behavior can be overridden by setting `createIfNotExists = true` when loading.
* Implemented proper MongoDB-based catch-up view.

## 0.0.15

* Implemented simple SQL server row-based view
* Views get an `IViewContext` now that they can use to load aggregate roots (including the ability to specify which version to load)

## 0.0.16

* Gave event dispatcher the ability to initialize itself

## 0.0.17

* Extended `TestContext` with the ability to dispatch events to views
* Made not-intended-for-others-to-use in-mem versions of some stuff internal

## 0.0.18

* Added serializability check to test context

## 0.0.19

* Added serializability check to all current event stores

## 0.0.20

* Fixed it so that loading an aggregate root during event application will result in loading the correct version of that aggregate root

## 0.0.21

* Made an explicit divide (made it possible, at least) between catch-up and direct-dispatch view managers
* Added LINQ capabilities to MongoDB view manager

## 0.0.22

* Introduced `Created` hook that can be overridden on aggregate roots, e.g. to emit the infamous `YayIWasCreated` event.

## 0.0.23

* Made Entity Framework view manager support LINQ as well and removed the need for that silly global sequence numbers table
* Entity Framework view manager automatically adds index to global sequence number column

## 0.0.27

* Did some repair work and did some more stuff as well.

## 0.0.30

* `Load<TAggregate>
    ` on `AggregateRoot` now loads & caches in the current unit of work, loading & caching the right versions of aggregate roots as well.

    ## 0.0.33

    * Renamed view managers

    ## 0.0.34

    * Divided view manager into push/pull view managers
    * Introduced composite command

    ## 0.0.35

    * Moved event dispatch out of retry loop

    ## 0.1.0

    * Renamed to "Circus" ;)- because when you
say "CQRS" fast enough, that's what it sounds like
    ## 0.1.1
    * Renamed existing e
    vent dispatcher to `ViewManagerEventDispatcher` because it can dispatch events to view managers - that's what makes it special :)
    


   ## 0.1.2
    * Added Azure Service Bus event dispatcher + nuspec
    ## 0.1.3
    * Fixed bug in view managers that could "forget" to upd
    ate `LastGlobalSequenceNumber` on a view - not that will be automatically done
by the `ViewDispatcherHelper`
    ## 0.2.0
    * Renamed to "Cirqus"
- the name that just gets better and better!
    ## 0.2.1
    * Introduced logging + added `ProcessCommand` method to `TestContext`
    ## 0.2.2
    *
    Somemore logging

    

 ## 0.2.3
    * Added NLog integration and added configuration
    option on `Options` to a
llow for configuring logging
    ## 0.2.4
    * Added asynchron
    ous event dispatcher - can be configured by going `.Asynchronous()` on any ordinary dispatcher

## 0.2.5
    * Improved async event dispatcher to use one worker thread per inner dispatcher
    ## 0.3.0

    * Improved `IViewContext` by adding some more context to it (+ ability to load "current" version of an aggregate root - i.e. the global sequence number "roof" is automatically deducted from the domain event currently being han
dled)
    ## 0.4.0
    * Changed `TestContext` to provide a more explicit model for simulating a proper u
    nit of work - can now be accessed by
 going `BeginUnitOfWork` and going all `Commit` and stuff
    ## 0.4.1
    * Fixed bug that would
 result in "forgetting" to invoke the `Created` hook on a new aggregate root when running with the real command processor
    ## 0.4.2
    * Added MongoDB logger factory
    ## 0.4.3
    * Added method to the test conte
    xt that can print the ac
cumulated event history and the emitted events to a text writter, formatted as plain old JSON objects
    ## 0.4.4
    * MIT licensed everything.
    ## 0.5.0
    * Fixed bug that would result in not
 getting a cache hit on 2nd load of the same root from unit of work
    ## 0.6.0
    * Fixed potential odd behavior by having in-mem even
    t store save cloned events instead of the original objects.

    ## 0.6.1

    * Make event stores automatically add event batch ID as a header on all
events  ##
 0.7.0
    * Changed format
    of timestamp metadata to be strings in order to ensure consistent behavior across all event stores + introduced extension method for extracting them

    ## 0.7.1

    * Corrected
spelling in an error message
    ## 0.8.0
    * Changed initialization of async event dispatcher to be async as well
    ## 0.9.0
    * Added Pos
    tgreSQL event store

    ## 0.10.0
    * Changed `TestCon
    text` API so that it can
 return fully hydrated aggregate roots
    ## 0.11.0
    * Made `ProcessCommand` method on `TestC
    ontext` return events th
at were emitted as a result of that command
    ## 0.12.0
    * Removed a lot 

================================================
FILE: LICENSE.md
================================================
The MIT License (MIT)

Copyright (c) 2014 d60

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

================================================
FILE: README.md
================================================
# d60 Cirqus

Simple but powerful event sourcing + CQRS kit. 

Provides a model for creating commands, aggregate roots, events, and views,
tying it all up in one simple and neat `CommandProcessor`.

### How simple?

You do this:

```csharp
var processor = CommandProcessor.With()
    .(...)
    .Create();
```

and let the API guide you through selecting an event store, possibly configuring some more stuff as well, and then you can do this:

```csharp
processor.ProcessCommand(myCommand);
```

and then everything will flow from there. The command processor is reentrant and is meant to be kept around for the duration of your application's lifetime. Remember to

```csharp
processor.Dispose();
```
    
when the application shuts down.

### More docs

Check out [the official documentation wiki](https://github.com/d60/Cirqus/wiki).

### Is Cirqus for you?

It depends ;) to answer that question, it is necessary to think a little bit about your
requirements. Cirqus is not in the _extreme high performance camp_ (if there is such a camp),
although it doesn't mean that Cirqus cannot perform extremely well - it's more that on the
following scale:

    Raw performance                  Polished APIs and general usefulness
    ================================================(+)==================

Cirqus is positioned around the `(+)` - it doesn't mean that you cannot achieve great -
excellent even - performance with Cirqus, it just means that certain choices have probably
been made for your with Cirqus that makes certain things easier, even though it may
sacrifice a little bit of raw performance.

And on this scale:

    Complex event processing        Domain-model-centric event processing
    ================================================(+)==================

Cirqus is again positioned around the `(+)` - it is mostly meant to be used in conjunction
with an event-driven domain model, so if you're content with driving everything directly off
of events, you will probably not benefit as much from using Cirqus.

Again, it's not that Cirqus doesn't do complex event processing - Cirqus' views can
easily be brought to do that - it's just that that is not really the focus (at least not with
the existing implementations).

Lastly, on this scale:

    .NET-centric                                            Interoperable
    =================(+)=================================================

it shows that many things are just made extremely easy for you if you're using Cirqus and .NET.
You can of course easily set up something else to read events since all the existing event
stores are simply using JSON to represent their contents, but from time to time a .NET type name 
might show up in the JSON data - which means that it's easier to use from .NET, but not impossible
to use from something else (e.g. to have node.js-driven projections or whatever).


### Configuration example

This is how you can set up a fully functioning command processor, including a view:

```csharp
// configure one single view manager
var viewManager = new MsSqlViewManager<CounterView>("sqltestdb");

// let's create & initialize the command processor
var processor = CommandProcessor.With()
    .EventStore(e => e.UseSqlServer("sqltestdb", "Events"))
    .EventDispatcher(e => e.UseViewManagerEventDispatcher(viewManager))
    .Create();

// use the command processor, possibly from multiple threads,
// for the entire lifetime of your application....

// and then, when your application shuts down:
processor.Dispose();
```


### Elaborate configuration example

If you're interested in seeing which moving parts are involved in the command processor, here's the equivalent
configuration where all the things are wired together manually. As you can see, it's actually fairly simple
(although the configuration API is much more intuitive and concise).

```csharp
// this is the origin of truth - let's keep it in SQL Server!
var eventStore = new MsSqlEventStore("sqltestdb", "Events", 
                                     automaticallyCreateSchema: true);

// aggregate roots are simply built when needed by replaying events
// for the requested root
var repository = new DefaultAggregateRootRepository(eventStore);

// configure one single view manager in another table in our SQL Server
var viewManager = new MsSqlViewManager<CounterView>("sqltestdb", "CounterView", 
                                                    automaticallyCreateSchema: true);

// Cirqus will deliver emitted events to the event dispatcher when they have
//  been persisted
var eventDispatcher = new ViewManagerEventDispatcher(repository, eventStore, viewManager);

// we can create the processor now
var processor = new CommandProcessor(eventStore, repository, eventDispatcher);

// and then, when your application shuts down:
processor.Dispose();
```


### Code example

This is an example of a command whose purpose it is to instruct the `Counter` aggregate root to increment itself by
some specific value, as 

================================================
FILE: d60.Cirqus.SQLite\readme.txt
================================================
﻿Sorry about the readme - but when you're using the SQLite event store with Cirqus, you need to
go and make sure that the appropriate sqlite3.dll is copied to the output directory of your
application.

Here's how to do it:

 * "Add existing item" to the root of your project

 * Browse to where the d60.Cirqus.SQLite NuGet package was included (e.g.)
   <your-solution-folder>/packages/d60.Cirqus.SQLite.<version>

 * Find appropriate sqlite3.dll depending on your platform - can be found either
   in lib/x64 or lib/x86 - and include it in your project

 * Make sure that the build action for sqlite3.dll is "Content", and "Copy to output
   directory" is set to "Copy if newer"

That should be it :)

PS: You don't HAVE to use the include sqlite3.dll - you're free to go to http://sqlite.org
and download a newer version if you like.


================================================
FILE: packages\EntityFramework.6.1.1\tools\about_EntityFramework.help.txt
================================================
TOPIC
    about_EntityFramework

SHORT DESCRIPTION
    Provides information about Entity Framework commands.

LONG DESCRIPTION
    This topic describes the Entity Framework commands. Entity Framework is
    Microsoft's recommended data access technology for new applications.

    The following Entity Framework cmdlets are used with Entity Framework
    Migrations.

        Cmdlet              Description
        -----------------   ---------------------------------------------------
        Enable-Migrations   Enables Code First Migrations in a project.

        Add-Migration       Scaffolds a migration script for any pending model
                            changes.

        Update-Database     Applies any pending migrations to the database.

        Get-Migrations      Displays the migrations that have been applied to
                            the target database.

    The following Entity Framework cmdlets are used by NuGet packages that
    install Entity Framework providers. These commands are not usually used as
    part of normal application development.

        Cmdlet                          Description
        ------------------------------  ---------------------------------------
        Add-EFProvider                  Adds or updates an Entity Framework
                                        provider entry in the project config
                                        file.

        Add-EFDefaultConnectionFactory  Adds or updates an Entity Framework
                                        default connection factory in the
                                        project config file.

        Initialize-EFConfiguration      Initializes the Entity Framework
                                        section in the project config file and
                                        sets defaults.

SEE ALSO
    Enable-Migrations
    Add-Migration
    Update-Database
    Get-Migrations


================================================
FILE: packages\NUnit.2.6.3\license.txt
================================================
Copyright  2002-2013 Charlie Poole
Copyright  2002-2004 James W. Newkirk, Michael C. Two, Alexei A. Vorontsov
Copyright  2000-2002 Philip A. Craig

This software is provided 'as-is', without any express or implied warranty. In no event will the authors be held liable for any damages arising from the use of this software.

Permission is granted to anyone to use this software for any purpose, including commercial applications, and to alter it and redistribute it freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not claim that you wrote the original software. If you use this software in a product, an acknowledgment (see the following) in the product documentation is required.

Portions Copyright  2002-2013 Charlie Poole or Copyright  2002-2004 James W. Newkirk, Michael C. Two, Alexei A. Vorontsov or Copyright  2000-2002 Philip A. Craig

2. Altered source versions must be plainly marked as such, and must not be misrepresented as being the original software.

3. This notice may not be removed or altered from any source distribution.


================================================
FILE: packages\Shouldly.2.5.0\BREAKING CHANGES.txt
================================================
v1.1 -> v2.0 Breaking Changes
    # ShouldBeGreaterThan and ShouldBeLessThan are now constrained to IComparable<T>
        If you are doing something like this `1.ShouldBeLessThan(3f)` then cast one of the types so they are the same type
        i.e `((float)1).ShouldBeLessThan(3f)`
    # Method Grouping on Should.Throw no longer works due to async overloads.
        Change `Should.Throw(service.DoSomething)` to `Should.Throw(() => service.DoSomething)`
    # IEnumerable.ShouldBe(IEnumerable) now uses .Equals to compare
        - This is because of c#'s overload selection, it will always pick the ShouldBe<T>(T, T) overload rather than ShouldBe<T>(IEnumerable<T>, IEnumerable<T>)
        - There are two ways to select the IEnumerable overload:
           - Specify T. i.e new[]{"foo"}.ShouldBe<string>(new[]{"foo"});
           - Specify the `ignoreOrder` parameter. i.e new[]{"foo"}.ShouldBe(new[]{"foo"}, ignoreOrder: false)
           - Make expected value less specific than actual, for instance: `new[]{"foo"}.ShouldBe(new[]{"foo"}.AsEnumerable())`
    # ShouldBeTypeOf<T> renamed to ShouldBeAssignableTo<T>

v1.0 -> v1.1 Breaking Changes
    # Shouldly.Should.Throw<TException> changed to return thrown exception when failed, rather than exception message
        FIX: Any code relying on Throw<T>() to return a string should update to call Message. Eg:
        Should.Throw<SomeException>(() => throw new OtherException()).Message.ShouldBe("Threw other exception"); 
   
    # Rhino Mocks has been deprecated from Shouldly. 
        Won't break build as such, but please bear in mind that plans are to remove this functionality from Shouldly
        This also means the NuGet package has been updated to remove the explicit dependency on Rhino.Mocks.
        
    # The following classes have been marked internal. They shouldn't have been marked public:
        Shouldly.ObjectHelpers
            T As<T>()
        Shouldly.ShouldlyCoreExtentions
            void AssertAwesomely<T>()
        Shouldly.TestEnvironment
        Shouldly.ShouldlyMessage
        Shouldly.ShouldlyMethodsAttribute
        Shouldly.StringHelpers
            string CommaDelimited<T>()
            string DelimitWith<T>()
            string Inspect()

        If you're using these methods, please implement locally before updating to v1.1

====EOF====


================================================
FILE: packages\Shouldly.2.5.0\LICENSE.txt
================================================
Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice,
    this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.
    * Neither the names of the copyright holders nor the names of 
    contributors may be used to endorse or promote products derived from this
    software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

[ http://www.opensource.org/licenses/bsd-license.php ]

================================================
FILE: packages\Shouldly.2.5.0\README.txt
================================================
![Icon](https://raw.github.com/shouldly/shouldly/master/package_icon.png)

Shouldly
========
Shouldly is an assertion framework which focuses on giving great error messages when the assertion fails while being simple and terse.

This is the old *Assert* way: 

    Assert.That(contestant.Points, Is.EqualTo(1337));

For your troubles, you get this message, when it fails:

    Expected 1337 but was 0

How it **Should** be:

    contestant.Points.ShouldBe(1337);

Which is just syntax, so far, but check out the message when it fails:

    contestant.Points should be 1337 but was 0

It might be easy to underestimate how useful this is. Another example, side by side:

    Assert.That(map.IndexOfValue("boo"), Is.EqualTo(2));    // -> Expected 2 but was 1
    map.IndexOfValue("boo").ShouldBe(2);                    // -> map.IndexOfValue("boo") should be 2 but was 1

**Shouldly** uses the code before the *ShouldBe* statement to report on errors, which makes diagnosing easier.

Read more about Shouldly and it's features at [http://docs.shouldly-lib.net/](http://docs.shouldly-lib.net/)

## Contributing
**Getting started with Git and GitHub**

 * [Setting up Git for Windows and connecting to GitHub](http://help.github.com/win-set-up-git/)
 * [Forking a GitHub repository](http://help.github.com/fork-a-repo/)
 * [The simple guide to GIT guide](http://rogerdudler.github.com/git-guide/)
 * [Open an issue](https://github.com/shouldly/shouldly/issues) if you encounter a bug or have a suggestion for improvements/features
 * [Submit documentation improvements](http://docs.shouldly-lib.net) by clicking 'Suggest edit' on any docs

Once you're familiar with Git and GitHub, clone the repository and start contributing.

If you need inspiration for which issue to pick up have a look for the [Jump-In](https://github.com/shouldly/shouldly/labels/Jump-In) label on issues which are put on issues which are ready to be picked up by anyone. 

## Icon
[Star](https://thenounproject.com/term/star/20931/) created by [Luboš Volkov](https://thenounproject.com/Lubo%C5%A1%20Volkov/) from The Noun Project


================================================
FILE: packages\System.Threading.Tasks.Extensions.4.3.0\dotnet_library_license.txt
================================================

MICROSOFT SOFTWARE LICENSE TERMS


MICROSOFT .NET LIBRARY 

These license terms are an agreement between Microsoft Corporation (or based on where you live, one of its affiliates) and you. Please read them. They apply to the software named above, which includes the media on which you received it, if any. The terms also apply to any Microsoft

·         updates,

·         supplements,

·         Internet-based services, and

·         support services

for this software, unless other terms accompany those items. If so, those terms apply.

BY USING THE SOFTWARE, YOU ACCEPT THESE TERMS. IF YOU DO NOT ACCEPT THEM, DO NOT USE THE SOFTWARE.


IF YOU COMPLY WITH THESE LICENSE TERMS, YOU HAVE THE PERPETUAL RIGHTS BELOW.

1.    INSTALLATION AND USE RIGHTS. 

a.    Installation and Use. You may install and use any number of copies of the software to design, develop and test your programs.

b.    Third Party Programs. The software may include third party programs that Microsoft, not the third party, licenses to you under this agreement. Notices, if any, for the third party program are included for your information only.

2.    ADDITIONAL LICENSING REQUIREMENTS AND/OR USE RIGHTS.

a.    DISTRIBUTABLE CODE.  The software is comprised of Distributable Code. “Distributable Code” is code that you are permitted to distribute in programs you develop if you comply with the terms below.

i.      Right to Use and Distribute. 

·         You may copy and distribute the object code form of the software.

·         Third Party Distribution. You may permit distributors of your programs to copy and distribute the Distributable Code as part of those programs.

ii.    Distribution Requirements. For any Distributable Code you distribute, you must

·         add significant primary functionality to it in your programs;

·         require distributors and external end users to agree to terms that protect it at least as much as this agreement;

·         display your valid copyright notice on your programs; and

·         indemnify, defend, and hold harmless Microsoft from any claims, including attorneys’ fees, related to the distribution or use of your programs.

iii.   Distribution Restrictions. You may not

·         alter any copyright, trademark or patent notice in the Distributable Code;

·         use Microsoft’s trademarks in your programs’ names or in a way that suggests your programs come from or are endorsed by Microsoft;

·         include Distributable Code in malicious, deceptive or unlawful programs; or

·         modify or distribute the source code of any Distributable Code so that any part of it becomes subject to an Excluded License. An Excluded License is one that requires, as a condition of use, modification or distribution, that

·         the code be disclosed or distributed in source code form; or

·         others have the right to modify it.

3.    SCOPE OF LICENSE. The software is licensed, not sold. This agreement only gives you some rights to use the software. Microsoft reserves all other rights. Unless applicable law gives you more rights despite this limitation, you may use the software only as expressly permitted in this agreement. In doing so, you must comply with any technical limitations in the software that only allow you to use it in certain ways. You may not

·         work around any technical limitations in the software;

·         reverse engineer, decompile or disassemble the software, except and only to the extent that applicable law expressly permits, despite this limitation;

·         publish the software for others to copy;

·         rent, lease or lend the software;

·         transfer the software or this agreement to any third party; or

·         use the software for commercial software hosting services.

4.    BACKUP COPY. You may make one backup copy of the software. You may use it only to reinstall the software.

5.    DOCUMENTATION. Any person that has valid access to your computer or internal network may copy and use the documentation for your internal, reference purposes.

6.    EXPORT RESTRICTIONS. The software is subject to United States export laws and regulations. You must comply with all domestic and international export laws and regulations that apply to the software. These laws include restrictions on destinations, end users and end use. For additional information, see www.microsoft.com/exporting.

7.    SUPPORT SERVICES. Because this software is “as is,” we may not provide support services for it.

8.    ENTIRE AGREEMENT. This agreement, and the terms for supplements, updates, Internet-based services and support services that you use, are the entire agreement for the software and support services.

9.    APPLICABLE LAW.

a.    United States. If you acquired the software in the United States, Washington state law governs the interpretation of this agreement and applies to claims for breach of it, regardless of conflict of laws principles. The laws of the state where you liv

================================================
FILE: packages\System.Threading.Tasks.Extensions.4.3.0\ThirdPartyNotices.txt
================================================
This Microsoft .NET Library may incorporate components from the projects listed
below. Microsoft licenses these components under the Microsoft .NET Library
software license terms. The original copyright notices and the licenses under
which Microsoft received such components are set forth below for informational
purposes only. Microsoft reserves all rights not expressly granted herein,
whether by implication, estoppel or otherwise.

1.	.NET Core (https://github.com/dotnet/core/)

.NET Core
Copyright (c) .NET Foundation and Contributors

The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: d60.Cirqus.SQLite\readme.txt
```
﻿Sorry about the readme - but when you're using the SQLite event store with Cirqus, you need to
go and make sure that the appropriate sqlite3.dll is copied to the output directory of your
application.

Here's how to do it:

 * "Add existing item" to the root of your project

 * Browse to where the d60.Cirqus.SQLite NuGet package was included (e.g.)
   <your-solution-folder>/packages/d60.Cirqus.SQLite.<version>

 * Find appropriate sqlite3.dll depending on your platform - can be found either
   in lib/x64 or lib/x86 - and include it in your project

 * Make sure that the build action for sqlite3.dll is "Content", and "Copy to output
   directory" is set to "Copy if newer"

That should be it :)

PS: You don't HAVE to use the include sqlite3.dll - you're free to go to http://sqlite.org
and download a newer version if you like.

```

## File: packages\EntityFramework.6.1.1\tools\about_EntityFramework.help.txt
```
TOPIC
    about_EntityFramework

SHORT DESCRIPTION
    Provides information about Entity Framework commands.

LONG DESCRIPTION
    This topic describes the Entity Framework commands. Entity Framework is
    Microsoft's recommended data access technology for new applications.

    The following Entity Framework cmdlets are used with Entity Framework
    Migrations.

        Cmdlet              Description
        -----------------   ---------------------------------------------------
        Enable-Migrations   Enables Code First Migrations in a project.

        Add-Migration       Scaffolds a migration script for any pending model
                            changes.

        Update-Database     Applies any pending migrations to the database.

        Get-Migrations      Displays the migrations that have been applied to
                            the target database.

    The following Entity Framework cmdlets are used by NuGet packages that
    install Entity Framework providers. These commands are not usually used as
    part of normal application development.

        Cmdlet                          Description
        ------------------------------  ---------------------------------------
        Add-EFProvider                  Adds or updates an Entity Framework
                                        provider entry in the project config
                                        file.

        Add-EFDefaultConnectionFactory  Adds or updates an Entity Framework
                                        default connection factory in the
                                        project config file.

        Initialize-EFConfiguration      Initializes the Entity Framework
                                        section in the project config file and
                                        sets defaults.

SEE ALSO
    Enable-Migrations
    Add-Migration
    Update-Database
    Get-Migrations

```

## File: packages\NUnit.2.6.3\license.txt
```
Copyright  2002-2013 Charlie Poole
Copyright  2002-2004 James W. Newkirk, Michael C. Two, Alexei A. Vorontsov
Copyright  2000-2002 Philip A. Craig

This software is provided 'as-is', without any express or implied warranty. In no event will the authors be held liable for any damages arising from the use of this software.

Permission is granted to anyone to use this software for any purpose, including commercial applications, and to alter it and redistribute it freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not claim that you wrote the original software. If you use this software in a product, an acknowledgment (see the following) in the product documentation is required.

Portions Copyright  2002-2013 Charlie Poole or Copyright  2002-2004 James W. Newkirk, Michael C. Two, Alexei A. Vorontsov or Copyright  2000-2002 Philip A. Craig

2. Altered source versions must be plainly marked as such, and must not be misrepresented as being the original software.

3. This notice may not be removed or altered from any source distribution.

```

## File: packages\Shouldly.2.5.0\BREAKING CHANGES.txt
```
v1.1 -> v2.0 Breaking Changes
    # ShouldBeGreaterThan and ShouldBeLessThan are now constrained to IComparable<T>
        If you are doing something like this `1.ShouldBeLessThan(3f)` then cast one of the types so they are the same type
        i.e `((float)1).ShouldBeLessThan(3f)`
    # Method Grouping on Should.Throw no longer works due to async overloads.
        Change `Should.Throw(service.DoSomething)` to `Should.Throw(() => service.DoSomething)`
    # IEnumerable.ShouldBe(IEnumerable) now uses .Equals to compare
        - This is because of c#'s overload selection, it will always pick the ShouldBe<T>(T, T) overload rather than ShouldBe<T>(IEnumerable<T>, IEnumerable<T>)
        - There are two ways to select the IEnumerable overload:
           - Specify T. i.e new[]{"foo"}.ShouldBe<string>(new[]{"foo"});
           - Specify the `ignoreOrder` parameter. i.e new[]{"foo"}.ShouldBe(new[]{"foo"}, ignoreOrder: false)
           - Make expected value less specific than actual, for instance: `new[]{"foo"}.ShouldBe(new[]{"foo"}.AsEnumerable())`
    # ShouldBeTypeOf<T> renamed to ShouldBeAssignableTo<T>

v1.0 -> v1.1 Breaking Changes
    # Shouldly.Should.Throw<TException> changed to return thrown exception when failed, rather than exception message
        FIX: Any code relying on Throw<T>() to return a string should update to call Message. Eg:
        Should.Throw<SomeException>(() => throw new OtherException()).Message.ShouldBe("Threw other exception"); 
   
    # Rhino Mocks has been deprecated from Shouldly. 
        Won't break build as such, but please bear in mind that plans are to remove this functionality from Shouldly
        This also means the NuGet package has been updated to remove the explicit dependency on Rhino.Mocks.
        
    # The following classes have been marked internal. They shouldn't have been marked public:
        Shouldly.ObjectHelpers
            T As<T>()
        Shouldly.ShouldlyCoreExtentions
            void AssertAwesomely<T>()
        Shouldly.TestEnvironment
        Shouldly.ShouldlyMessage
        Shouldly.ShouldlyMethodsAttribute
        Shouldly.StringHelpers
            string CommaDelimited<T>()
            string DelimitWith<T>()
            string Inspect()

        If you're using these methods, please implement locally before updating to v1.1

====EOF====

```

## File: packages\Shouldly.2.5.0\LICENSE.txt
```
Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice,
    this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.
    * Neither the names of the copyright holders nor the names of 
    contributors may be used to endorse or promote products derived from this
    software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

[ http://www.opensource.org/licenses/bsd-license.php ]
```

## File: packages\Shouldly.2.5.0\README.txt
```
![Icon](https://raw.github.com/shouldly/shouldly/master/package_icon.png)

Shouldly
========
Shouldly is an assertion framework which focuses on giving great error messages when the assertion fails while being simple and terse.

This is the old *Assert* way: 

    Assert.That(contestant.Points, Is.EqualTo(1337));

For your troubles, you get this message, when it fails:

    Expected 1337 but was 0

How it **Should** be:

    contestant.Points.ShouldBe(1337);

Which is just syntax, so far, but check out the message when it fails:

    contestant.Points should be 1337 but was 0

It might be easy to underestimate how useful this is. Another example, side by side:

    Assert.That(map.IndexOfValue("boo"), Is.EqualTo(2));    // -> Expected 2 but was 1
    map.IndexOfValue("boo").ShouldBe(2);                    // -> map.IndexOfValue("boo") should be 2 but was 1

**Shouldly** uses the code before the *ShouldBe* statement to report on errors, which makes diagnosing easier.

Read more about Shouldly and it's features at [http://docs.shouldly-lib.net/](http://docs.shouldly-lib.net/)

## Contributing
**Getting started with Git and GitHub**

 * [Setting up Git for Windows and connecting to GitHub](http://help.github.com/win-set-up-git/)
 * [Forking a GitHub repository](http://help.github.com/fork-a-repo/)
 * [The simple guide to GIT guide](http://rogerdudler.github.com/git-guide/)
 * [Open an issue](https://github.com/shouldly/shouldly/issues) if you encounter a bug or have a suggestion for improvements/features
 * [Submit documentation improvements](http://docs.shouldly-lib.net) by clicking 'Suggest edit' on any docs

Once you're familiar with Git and GitHub, clone the repository and start contributing.

If you need inspiration for which issue to pick up have a look for the [Jump-In](https://github.com/shouldly/shouldly/labels/Jump-In) label on issues which are put on issues which are ready to be picked up by anyone. 

## Icon
[Star](https://thenounproject.com/term/star/20931/) created by [Luboš Volkov](https://thenounproject.com/Lubo%C5%A1%20Volkov/) from The Noun Project

```

## File: packages\System.Threading.Tasks.Extensions.4.3.0\dotnet_library_license.txt
```

MICROSOFT SOFTWARE LICENSE TERMS


MICROSOFT .NET LIBRARY 

These license terms are an agreement between Microsoft Corporation (or based on where you live, one of its affiliates) and you. Please read them. They apply to the software named above, which includes the media on which you received it, if any. The terms also apply to any Microsoft

·         updates,

·         supplements,

·         Internet-based services, and

·         support services

for this software, unless other terms accompany those items. If so, those terms apply.

BY USING THE SOFTWARE, YOU ACCEPT THESE TERMS. IF YOU DO NOT ACCEPT THEM, DO NOT USE THE SOFTWARE.


IF YOU COMPLY WITH THESE LICENSE TERMS, YOU HAVE THE PERPETUAL RIGHTS BELOW.

1.    INSTALLATION AND USE RIGHTS. 

a.    Installation and Use. You may install and use any number of copies of the software to design, develop and test your programs.

b.    Third Party Programs. The software may include third party programs that Microsoft, not the third party, licenses to you under this agreement. Notices, if any, for the third party program are included for your information only.

2.    ADDITIONAL LICENSING REQUIREMENTS AND/OR USE RIGHTS.

a.    DISTRIBUTABLE CODE.  The software is comprised of Distributable Code. “Distributable Code” is code that you are permitted to distribute in programs you develop if you comply with the terms below.

i.      Right to Use and Distribute. 

·         You may copy and distribute the object code form of the software.

·         Third Party Distribution. You may permit distributors of your programs to copy and distribute the Distributable Code as part of those programs.

ii.    Distribution Requirements. For any Distributable Code you distribute, you must

·         add significant primary functionality to it in your programs;

·         require distributors and external end users to agree to terms that protect it at least as much as this agreement;

·         display your valid copyright notice on your programs; and

·         indemnify, defend, and hold harmless Microsoft from any claims, including attorneys’ fees, related to the distribution or use of your programs.

iii.   Distribution Restrictions. You may not

·         alter any copyright, trademark or patent notice in the Distributable Code;

·         use Microsoft’s trademarks in your programs’ names or in a way that suggests your programs come from or are endorsed by Microsoft;

·         include Distributable Code in malicious, deceptive or unlawful programs; or

·         modify or distribute the source code of any Distributable Code so that any part of it becomes subject to an Excluded License. An Excluded License is one that requires, as a condition of use, modification or distribution, that

·         the code be disclosed or distributed in source code form; or

·         others have the right to modify it.

3.    SCOPE OF LICENSE. The software is licensed, not sold. This agreement only gives you some rights to use the software. Microsoft reserves all other rights. Unless applicable law gives you more rights despite this limitation, you may use the software only as expressly permitted in this agreement. In doing so, you must comply with any technical limitations in the software that only allow you to use it in certain ways. You may not

·         work around any technical limitations in the software;

·         reverse engineer, decompile or disassemble the software, except and only to the extent that applicable law expressly permits, despite this limitation;

·         publish the software for others to copy;

·         rent, lease or lend the software;

·         transfer the software or this agreement to any third party; or

·         use the software for commercial software hosting services.

4.    BACKUP COPY. You may make one backup copy of the software. You may use it only to reinstall the software.

5.    DOCUMENTATION. Any person that has valid access to your computer or internal network may copy and use the documentation for your internal, reference purposes.

6.    EXPORT RESTRICTIONS. The software is subject to United States export laws and regulations. You must comply with all domestic and international export laws and regulations that apply to the software. These laws include restrictions on destinations, end users and end use. For additional information, see www.microsoft.com/exporting.

7.    SUPPORT SERVICES. Because this software is “as is,” we may not provide support services for it.

8.    ENTIRE AGREEMENT. This agreement, and the terms for supplements, updates, Internet-based services and support services that you use, are the entire agreement for the software and support services.

9.    APPLICABLE LAW.

a.    United States. If you acquired the software in the United States, Washington state law governs the interpretation of this agreement and applies to claims for breach of it, regardless of conflict of laws principles. The laws of the state where you live govern all other claims, including claims under state consumer protection laws, unfair competition laws, and in tort.

b.    Outside the United States. If you acquired the software in any other country, the laws of that country apply.

10.  LEGAL EFFECT. This agreement describes certain legal rights. You may have other rights under the laws of your country. You may also have rights with respect to the party from whom you acquired the software. This agreement does not change your rights under the laws of your country if the laws of your country do not permit it to do so.

11.  DISCLAIMER OF WARRANTY. THE SOFTWARE IS LICENSED “AS-IS.” YOU BEAR THE RISK OF USING IT. MICROSOFT GIVES NO EXPRESS WARRANTIES, GUARANTEES OR CONDITIONS. YOU MAY HAVE ADDITIONAL CONSUMER RIGHTS OR STATUTORY GUARANTEES UNDER YOUR LOCAL LAWS WHICH THIS AGREEMENT CANNOT CHANGE. TO THE EXTENT PERMITTED UNDER YOUR LOCAL LAWS, MICROSOFT EXCLUDES THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.

FOR AUSTRALIA – YOU HAVE STATUTORY GUARANTEES UNDER THE AUSTRALIAN CONSUMER LAW AND NOTHING IN THESE TERMS IS INTENDED TO AFFECT THOSE RIGHTS.

12.  LIMITATION ON AND EXCLUSION OF REMEDIES AND DAMAGES. YOU CAN RECOVER FROM MICROSOFT AND ITS SUPPLIERS ONLY DIRECT DAMAGES UP TO U.S. $5.00. YOU CANNOT RECOVER ANY OTHER DAMAGES, INCLUDING CONSEQUENTIAL, LOST PROFITS, SPECIAL, INDIRECT OR INCIDENTAL DAMAGES.

This limitation applies to

·         anything related to the software, services, content (including code) on third party Internet sites, or third party programs; and

·         claims for breach of contract, breach of warranty, guarantee or condition, strict liability, negligence, or other tort to the extent permitted by applicable law.

It also applies even if Microsoft knew or should have known about the possibility of the damages. The above limitation or exclusion may not apply to you because your country may not allow the exclusion or limitation of incidental, consequential or other damages.

Please note: As this software is distributed in Quebec, Canada, some of the clauses in this agreement are provided below in French.

Remarque : Ce logiciel étant distribué au Québec, Canada, certaines des clauses dans ce contrat sont fournies ci-dessous en français.

EXONÉRATION DE GARANTIE. Le logiciel visé par une licence est offert « tel quel ». Toute utilisation de ce logiciel est à votre seule risque et péril. Microsoft n’accorde aucune autre garantie expresse. Vous pouvez bénéficier de droits additionnels en vertu du droit local sur la protection des consommateurs, que ce contrat ne peut modifier. La ou elles sont permises par le droit locale, les garanties implicites de qualité marchande, d’adéquation à un usage particulier et d’absence de contrefaçon sont exclues.

LIMITATION DES DOMMAGES-INTÉRÊTS ET EXCLUSION DE RESPONSABILITÉ POUR LES DOMMAGES. Vous pouvez obtenir de Microsoft et de ses fournisseurs une indemnisation en cas de dommages directs uniquement à hauteur de 5,00 $ US. Vous ne pouvez prétendre à aucune indemnisation pour les autres dommages, y compris les dommages spéciaux, indirects ou accessoires et pertes de bénéfices.

Cette limitation concerne :

·         tout ce qui est relié au logiciel, aux services ou au contenu (y compris le code) figurant sur des sites Internet tiers ou dans des programmes tiers ; et

·         les réclamations au titre de violation de contrat ou de garantie, ou au titre de responsabilité stricte, de négligence ou d’une autre faute dans la limite autorisée par la loi en vigueur.

Elle s’applique également, même si Microsoft connaissait ou devrait connaître l’éventualité d’un tel dommage. Si votre pays n’autorise pas l’exclusion ou la limitation de responsabilité pour les dommages indirects, accessoires ou de quelque nature que ce soit, il se peut que la limitation ou l’exclusion ci-dessus ne s’appliquera pas à votre égard.

EFFET JURIDIQUE. Le présent contrat décrit certains droits juridiques. Vous pourriez avoir d’autres droits prévus par les lois de votre pays. Le présent contrat ne modifie pas les droits que vous confèrent les lois de votre pays si celles-ci ne le permettent pas.

 

```

## File: packages\System.Threading.Tasks.Extensions.4.3.0\ThirdPartyNotices.txt
```
This Microsoft .NET Library may incorporate components from the projects listed
below. Microsoft licenses these components under the Microsoft .NET Library
software license terms. The original copyright notices and the licenses under
which Microsoft received such components are set forth below for informational
purposes only. Microsoft reserves all rights not expressly granted herein,
whether by implication, estoppel or otherwise.

1.	.NET Core (https://github.com/dotnet/core/)

.NET Core
Copyright (c) .NET Foundation and Contributors

The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```


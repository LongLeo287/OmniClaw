---
id: Cirqus
type: knowledge
owner: OA_Triage
---
# Cirqus
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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

### File: CHANGELOG.md
```md
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
        traction does not care about serialization now. It may, howev
... [TRUNCATED]
```

### File: LICENSE.md
```md
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


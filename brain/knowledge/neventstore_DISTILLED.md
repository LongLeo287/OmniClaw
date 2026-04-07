---
id: neventstore
type: knowledge
owner: OA_Triage
---
# neventstore
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: Readme.md
```md
NEventStore
===

NEventStore is a persistence library used to abstract different storage implementations when using event sourcing as storage mechanism. 

This library is developed with a specific focus on [DDD](http://en.wikipedia.org/wiki/Domain-driven_design)/[CQRS](https://en.wikipedia.org/wiki/Command%E2%80%93query_separation#Command_query_responsibility_segregation) applications.

NEventStore currently supports:

- .net standard 2.0
- .net framework 4.6.2

Starting from Version 6.0.0 NEventStore will use [Semantic Versioning](https://semver.org/) to track the version numbers.

Build Status (AppVeyor)
===

Branches: 

- master [![Build status](https://ci.appveyor.com/api/projects/status/frg36pb2oh1j2ddi/branch/master?svg=true)](https://ci.appveyor.com/project/AGiorgetti/neventstore/branch/master)
- develop [![Build status](https://ci.appveyor.com/api/projects/status/frg36pb2oh1j2ddi/branch/develop?svg=true)](https://ci.appveyor.com/project/AGiorgetti/neventstore/branch/develop)

Main Library Packages
===

- NEventStore - the core library package.
- NEventStore.Serialization.Json - Json serialization to be used with an IDocumentSerializer.
- NEventStore.Serialization.Bson - BSon serialization to be used with an IDocumentSerializer.
- NEventStore.Serialization.MsgPack - Message Pack serialization to be used with an IDocumentSerializer.
- NEventStore.PollingClient - provides an implementation for a PollingClient.

Documentation
===

Please see the [documentation](https://github.com/NEventStore/NEventStore/wiki) to get started and for more information.

ChangeLog can be [found here](https://github.com/NEventStore/NEventStore/blob/master/Changelog.md)

### Developed with:

[![Resharper](http://neventstore.org/images/logo_resharper_small.gif)](http://www.jetbrains.com/resharper/)
[![TeamCity](http://neventstore.org/images/logo_teamcity_small.gif)](http://www.jetbrains.com/teamcity/)
[![dotCover](http://neventstore.org/images/logo_dotcover_small.gif)](http://www.jetbrains.com/dotcover/)
[![dotTrace](http://neventstore.org/images/logo_dottrace_small.gif)](http://www.jetbrains.com/dottrace/)

# How to build (Windows OS)

To build the project locally on a Windows Machine:

- Open a Powershell console in Administrative mode and run the build script `build.ps1` in the root of the repository.

## Versioning

Versioning is done automatically by the build script updating the
AssemblyInfo.cs file (<GenerateAssemblyInfo>false</GenerateAssemblyInfo> in .csproj files) 
before the build starts. The version number is retrieved
from the git repository tags using "gitversion" tool.

Things are handled this way because NEventStore is used a submodule in other projects and it
need to have it's own version number when building other projects.

You should not update the version number manually, not commit the updated AssemblyInfo files.
```

### File: build.ps1
```ps1
$configurationdefault = "Release"
$artifacts = "../../artifacts"

$configuration = Read-Host 'Configuration to build [default: Release] ?'
if ($configuration -eq '') {
    $configuration = $configurationdefault
}
$runtests = Read-Host 'Run Tests (y / n) [default:n] ?'

# Install gitversion tool
dotnet tool restore

# Display minimal restore information
dotnet restore ./src/NEventStore.Core.sln --verbosity m

# GitVersion 
$str = dotnet tool run dotnet-gitversion /updateAssemblyInfo | out-string
$json = convertFrom-json $str
$nugetversion = $json.SemVer

# Build
Write-Host "Building: "$nugetversion
dotnet build ./src/NEventStore.Core.sln -c $configuration --no-restore -p:ContinuousIntegrationBuild=True

# Testing
if ($runtests -eq "y") {
    Write-Host "Executing Tests"
    dotnet test ./src/NEventStore.Core.sln -c $configuration --no-build
    Write-Host "Tests Execution Complated"
}

# NuGet packages
Write-Host "NuGet Packages creation"
dotnet pack ./src/NEventStore/NEventStore.Core.csproj -c $configuration --no-build -o $artifacts /p:PackageVersion=$nugetversion
dotnet pack ./src/NEventStore.PollingClient/NEventStore.PollingClient.csproj -c $configuration --no-build -o $artifacts /p:PackageVersion=$nugetversion
dotnet pack ./src/NEventStore.Serialization.Json/NEventStore.Serialization.Json.Core.csproj -c $configuration --no-build -o $artifacts /p:PackageVersion=$nugetversion
dotnet pack ./src/NEventStore.Serialization.Bson/NEventStore.Serialization.Bson.Core.csproj -c $configuration --no-build -o $artifacts /p:PackageVersion=$nugetversion
dotnet pack ./src/NEventStore.Serialization.MsgPack/NEventStore.Serialization.MsgPack.Core.csproj -c $configuration --no-build -o $artifacts /p:PackageVersion=$nugetversion
dotnet pack ./src/NEventStore.Serialization.Binary/NEventStore.Serialization.Binary.Core.csproj -c $configuration --no-build -o $artifacts /p:PackageVersion=$nugetversion
```

### File: Changelog.md
```md
# NEventStore Versions

## 10.1.1

### BugFix

- Fixed Assemblies Version Numbers (AssemblyInfo files).

## 10.1.0

- Improved `IEventStream` interface: `CommitChanges()` and `CommitChangesAsync()` now return `ICommit` instead of `void`.
- Updated MessagePack serializer to 3.1.3

### Breaking Changes

- `IEventStream.CommitChanges()` and `IEventStream.CommitChangesAsync()` now return `ICommit` instead of `void`.

## 10.0.1

### BugFix

- Async Pipeline Hooks: initialization and PreCommit/PostCommit invocation bugs [#516](https://github.com/NEventStore/NEventStore/issues/516)

## 10.0.0

- Async Methods to read from and write to streams (IStoreEvents, IEventStream, IPersistStreams, IPersistStreamsAsync, ICommitEventsAsync, IAccessSnapshotsAsync). [#513](https://github.com/NEventStore/NEventStore/issues/513)
  - methods that read from a stream in an async way follow the Observer pattern and requires you to pass in an `IAsyncObservable` that will receive data as soon as they are available.
- Async Pipeline Hooks (IPipelineHookAsync). [#515](https://github.com/NEventStore/NEventStore/issues/515)
- AsyncPollingClient: a new polling client implementation that uses Async interfaces. [#505](https://github.com/NEventStore/NEventStore/issues/505)
- Removed the BinarySerializer (BinaryFormatter) from the core package and moved it to its own package [#510](https://github.com/NEventStore/NEventStore/issues/510)
- Improved comments and added more nullability checks.
- Minor performance improvements.
- Updated Testing Packages (NUnit, FluentAssertions, Microsoft.NET.Test and so on...).

### Breaking Changes

- `PersistStreamsExtensions.GetFrom(IPersistStreams, DateTime)` and `PersistStreamsExtensions.GetFromTo(IPersistStreams, DateTime, DateTime)` extension methods have been removed: they had inconsistent behavior with the other GetFrom(checkpointToken) methods, 
  they were getting data from the default bucket only.
- `PipelineHooksAwarePersistanceDecorator` renamed to `PipelineHooksAwarePersistStreamsDecorator`.
- `IPipelineHook.Select` method renamed to `IPipelineHook.SelectCommit`.
- `BinarySerializer` moved to its own package: `NEventStore.Serialization.Binary`.
  - for net8.0+ call `AppContext.SetSwitch("System.Runtime.Serialization.EnableUnsafeBinaryFormatterSerialization", true);` to enable unsafe BinaryFormatter usage.
- Improved many method signature with nullability annotations.
- `Wireup.With()` renamed `Wireup.Register()`.
- `OptimisticEventStream` constructors replaced by initialization functions:
  - `new OptimisticEventStream(string bucketId, string streamId, ICommitEvents persistence, int minRevision, int maxRevision)` -> `new OptimisticEventStream(string bucketId, string streamId, ICommitEvents persistence).Initialize(int minRevision, int maxRevision)`.
  - `new OptimisticEventStream(ISnapshot snapshot, ICommitEvents persistence, int maxRevision)` -> `new OptimisticEventStream(string bucketId, string streamId, ICommitEvents persistence).Initialize(ISnapshot snapshot, int maxRevision)`.

## 9.2.0

- Updated nuget packages to include symbol packages and more information.
- Updated Newtonsoft.Bson 13.0.3
- Added MessagePack serializer, thanks to [@pvagnozzi](https://github.com/pvagnozzi)
- Improved comments and removed some compilation warnings.

## 9.1.1

- Fixed `build.ps1` script to correctly update Assembly Version number before building.
- Updated Readme with how Versioning works.

## 9.1.0

- Support the following Target Frameworks only: netstandard2.0, net462.	
- Updated Newtonsoft.Json 13.0.3

## 9.0.1 

- Added documentation files to NuGet packages (improved intellisense support) [#496](https://github.com/NEventStore/NEventStore/issues/496)

## 9.0.0

- Added support for .net 6 [#493](https://github.com/NEventStore/NEventStore/issues/493).
- Change / Optimization: Commit and CommitAttempt do not create internal read-only collections anymore, it can be useless given that we can change properties of events.
- NEventStore.Serialization.Json: accepts a JsonSerializerSettings to configure the serializer.

## 8.0.0

- Added support for .net 5 [#489](https://github.com/NEventStore/NEventStore/issues/489).
- Added support for .net framework 4.6.1.
- Fixed InMemoryPersistenceEngine.AddSnapshot() behavior: adding multiple snapshots for the same tuple bucketId, streamId, streamRevision is not allowed; the updated snapshot will be ignored [#484](https://github.com/NEventStore/NEventStore/pull/484).
- Logging infrastructure switched to [Microsoft.Extensions.Logging](https://docs.microsoft.com/en-us/dotnet/core/extensions/logging) [#454](https://github.com/NEventStore/NEventStore/issues/454), [#488](https://github.com/NEventStore/NEventStore/pull/488).
- Reviewed Exception (and logging) messages: many of those that refer to a StreamId should also provide BucketId information [#480](https://github.com/NEventStore/NEventStore/issues/480)

### Breaking Changes

- Dropped support for .NET Framework 4.5, only .NET 4.6.1+ will be supported in 8.x. .NET Framework support will be dropped in a future revision.
- Logging switched to Microsoft.Extensions.Logging, old logging code and configuration functions have been removed.

## 7.0.0

- The IPersistStreams interface got some major changes:
	- Added new `GetFromTo(Int64, Int64)` and `GetFromTo(string, Int64, Int64)` methods to the IPersistStreams interface.
	- Extension methods `PersistStreamsExtensions.GetFrom(DateTime)` and `PersistStreamsExtensions.GetFromTo(DateTime, DateTime)` were marked obsolete and will be removed.
	- A new PersistStreamsExtensions.GetCommit(Int64) method was added to retrieve a single commit [#445](https://github.com/NEventStore/NEventStore/issues/445).
- PollingClient was moved to its own NEventStore.PollingClient NuGet package [#467](https://github.com/NEventStore/NEventStore/issues/467).
- Added more information to the DuplicateCommitException error message (StreamId and BucketId), also the information provided by the Persistence providers will be reviewed [#372](https://github.com/NEventStore/NEventStore/issues/372).

### Breaking Changes

- The default value of 0 has been removed from the `IPersistStreams.GetFrom(Int64)` method.
- Removed the almost useless `GetFromStart()` extension method: use `IPersistStream.GetFrom(0)`.
- Bson serializer was moved from NEventStore.Serialization.Json to its own package: `NEventStore.Serialization.Bson`. Closes: [#479](https://github.com/NEventStore/NEventStore/issues/479).
- PollingClient was moved to its own package: add a reference to NEventStore.PollingClient NuGet package. Also the namespace was changed from NEventStore.Client to NEventStorePollingClient.

## 6.1.0

Enlist in ambient transaction has been removed from the mail library and added to the persistence drivers implementations, each driver has its own way to support, enable or disable the feature. As of now this change will mainly impact Microsoft SQL Server users, because all other persistence plugins didn't use transactions at all.

All the transactions (or their suppression) should be explicitly managed by the user.

Minor optimizations were made if no pipeline hooks are used.

### Breaking Changes

- `PipelineHookBase`: changed the way the Dispose pattern was implemented to be compliant with the framework guidelines. Move all the Dispose logic to the overridden Dispose(bool disposing) method of your pipeline hook class.
- `OptimisticPipelineHook` optimization is not configured and enabled by default (if not enlisting in ambient transactions) anymore; it now must be explicitly enabled calling UseOptimisticPipelineHook() when configuring NEventStore. Do not use it if you plan to use transactions. To restore the previous behavior call .UseOptimisticPipelineHook() when configuring NEventStore.
- `EnlistInAmbientTransaction` has been removed from the core NEventStore library. It will be added to specific persistence drivers implementations.

## 6.0.0

__Version 6.x is not backwards compatible with version 5.x.__ Updating to NEventStore 6.x without doing some preparation work will result in problems.

### New Features

- dotnet standard 2.0 , dotnet core 2.0 are now supported for the following projects: NEventStore, NEventStore.Domain, NEventStore.Persistence.Sql, NEventStore.Persistence.MongoDb

### Breaking Changes

- **Removed Dispatcher and dispatching mechanic, use the PollingClient**: it was marked obsolete in the version 5.x, you should dispatch events with other mechanisms, like using a PollingClient.
More information on this topic in the issue: [Race condition in sync and async dispatchers can result in subscribers getting commits / events out of order](https://github.com/NEventStore/NEventStore/issues/360).
- **Removed LongCheckpoint class**: checkpoint now is a plain Int64, there is no need to keep a LongCheckpoint class anymore. 
- **PollingClient was removed because it used to depend on Rx**: you can [read more information here](src/NEventStore/Client/README.MD). The new polling client class is called PollingClient2, this however should be considered as a sample implementation you can use to derive your own.
- **JsonSerializer and BsonSerializer were moved in a separate assembly**: if you need them, you should reference the NEventStore.Serialization.Json assembly or implement your own serializers that depend on the Json.Net version you need.
- **EventMessage** class is now sealed.
- **`OptimisticEventStream` throws exceptions if a null message or a message with null body is added to the stream**. Previously if you called Add with null event message or add with an event message with null body, the add operation was ignored without any warning or error. 

## 6.0.0-rc-1

New features:

- improved logging performances ([#468](https://github.com/NEventStore/NEventStore/issues/468)).

Bug fixed:

- adding events in the middle of a commit should throw ConcurrencyException ([#420](https://github.com/NEventStore/NEventStore/issues/420)).

## 6.0.0-rc-0

__Version 6.x is not backwards compatible with version 5.x.__ Updating to NEventStore 6.x without doing some preparation work will result in problems.

### New Features

- dotnet standard 2.0 , dotnet core 2.0 are now supported for the following projects: NEventStore, NEventStore.Domain, NEventStore.Persistence.Sql, NEventStore.Persistence.MongoDb

### Breaking changes

- **Removed Dispatcher and dispatching mechanic, use the PollingClient**: it was marked obsolete in the version 5.x, you should dispatch events with other mechanisms, like using a PollingClient.
More information on this topic in the issue: [Race condition in sync and async dispatchers can result in subscribers getting commits / events out of order](https://github.com/NEventStore/NEventStore/issues/360).
- **Removed LongCheckpoint class**: checkpoint now is a plain Int64, there is no need to keep a LongCheckpoint class anymore. 
- **PollingClient was removed because it used to depend on Rx**: you can [read more information here](src/NEventStore/Client/README.MD). The new polling client class is called PollingClient2, this however should be considered as a sample implementation you can use to derive your own.
- **JsonSerializer and BsonSerializer were moved in a separate assembly**: if you need them, you should reference the NEventStore.Serialization.Json assembly or implement your own serializers that depend on the Json.Net version you need.
- **EventMessage** class is now sealed.
- **OptimisticEventStream throws exceptions if a null message or a message with null body is added to the stream**. Previously if you called Add with null event message or add with an event message with null body, the add operation was ignored without any warning or error. 

### Other Notes

All persistence providers: 

- [MongoDb](https://github.com/NEventStore/NEventStore.Persistence.MongoDB)
- [Sql](https://github.com/NEventStore/NEventStore.Persistence.SQL) 
- [RavenDb](https://github.com/NEventStore/NEventStore.Persistence.RavenDB) - currently not maintained anymore.

are now hosted in their own project. 

Common Domain is now moved in its [own repository](https://github.com/NEventStore/NEventStore.Domain).

## 5.x.x

Note: Version 5 is not backwards compatible with v4. Updating to v5 without doing some preparation work will result in problems.

### Breaking Changes

1. Underlying schema has changed for all v5 storage engines. In order to migrate a store from v4 to v5 use NEventStore.Migrations
1.The concept of a 'Bucket' has been added as a container for streams allowing multi-tenancy, partitions, multiple-bounded contexts, sagas, etc to be stored in the one store. The API changes have been such that, using extension methods, operations will work on the default bucket, unless a bucket Id has been explicitly supplied. This should mean minimal code changes for the user.
1.Stream Ids are now string based and are limited to 1000 characters.
In the SQL engines the stream Id's are limited to 40 characters and are hashed versions of the actual StreamId.
The hashing function can be overridden during wire-up.

### New Features

#### Polling Client

As an alternative to the dispatcher mechanism and improved replay / catch-up story we have implemented a CheckpointNumber in the stores that guarantees ordering across the streams. This number is guaranteed to increment but not guaranteed to be sequential. This allows you to get all Commits from a specific checkpoint and observe new ones. This implementation is polling based (and thus works for all engines) so it doesn't have the same low-latency attributes of the dispatcher mechanism. You can see how to use it here: [https://gist.github.com/damianh/6370328](https://gist.github.com/damianh/6370328) .In this, instead of the store tracking what has been dispatched, the onus is on the client to track what it has seen. And upon restart, start subscribing from what it last saw.

In the future I'd like to see / implement reactive clients that leverage stores that are observable.

### Other Notes

1. Only SQL and MongoDB persistence engines are supported in this release. RavenDB engine will be shipped later.
1. RavenDB and MongoDB persistence engines are now in their own repositories and will have be shipped independently.

```

### File: license.txt
```txt
The MIT License

Copyright (c) 2013 Jonathan Oliver, Jonathan Matheus, Damian Hickey and contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

### File: .config\dotnet-tools.json
```json
{
  "version": 1,
  "isRoot": true,
  "tools": {
    "gitversion.tool": {
      "version": "6.1.0",
      "commands": [
        "dotnet-gitversion"
      ],
      "rollForward": false
    }
  }
}
```

### File: docs\Testing.md
```md
# Testing And Test Frameworks in NEventStore

While upgrading the solution to support dotnet core, we also tried to migrate the tests to other test frameworks
(because not all of them supported dotnet core correctly when the migration job started).

Several trial and errors were made, but in the end we were able to implement the tests using all the 3 major testing frameworks available in the dotnet world:

- XUnit
- NUnit
- MSTest

We had to write 3 version of the `SpecificationBase` class and adapt the testing attributes to each framework.

I you inspect the code you'll see a lot of `#if NUNIT` (and the like) lines of code.

The actual implementation compiles all the projects to use NUnit.

You can change the behavior following these steps:

- go through all the .csproj files and change the compilation constant from NUNIT to XUNIT or MSTEST.
- in the assemblies that contain tests you need to reference the correct Test Framework assemblies and TestAdapter for the framework you are going to use.

Having more than one test runner might not be a good idea because some CI tools (like Appveyor) might autodetect them and execute the tests for a framework you are not using, and it will surely endup with failures and errors of your build.
```

### File: src\AssemblyInfo.cs
```cs
﻿using System.Reflection;
using System.Runtime.CompilerServices;

[assembly: AssemblyVersion("0.0.0.0")]
[assembly: AssemblyFileVersion("0.0.0.0")]
[assembly: AssemblyInformationalVersion("0.0.0.0")]

```

### File: src\GlobalAssemblyInfo.cs
```cs
//-----------------------------------------------------------------------
// <copyright file="GlobalAssemblyInfo.cs">
//	 Copyright (c) Jonathan Oliver. All rights reserved.
// </copyright>
//-----------------------------------------------------------------------

using System;
using System.Reflection;
using System.Resources;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

[assembly: AssemblyCompany("NEventStore")]
[assembly: AssemblyProduct("NEventStore")]
[assembly: AssemblyCopyright("Copyright © Jonathan Oliver, Jonathan Mathius, Damian Hickey and Contributors 2011")]
[assembly: AssemblyTrademark("")]
[assembly: AssemblyConfiguration("")]
[assembly: AssemblyCulture("")]
[assembly: ComVisible(false)]
[assembly: CLSCompliant(false)]
[assembly: NeutralResourcesLanguage("en-US")]
[assembly: InternalsVisibleTo("NEventStore.Tests")]
[assembly: InternalsVisibleTo("NEventStore.Core.Tests")]

```

### File: src\GlobalSuppressions.cs
```cs
//-----------------------------------------------------------------------
// <copyright file="GlobalSuppressions.cs">
//	 Copyright (c) Jonathan Oliver. All rights reserved.
// </copyright>
//-----------------------------------------------------------------------
```


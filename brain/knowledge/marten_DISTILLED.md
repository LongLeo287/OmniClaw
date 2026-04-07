---
id: marten
type: knowledge
owner: OA_Triage
---
# marten
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "private": true,
  "scripts": {
    "mdsnippets": "mdsnippets",
    "vitepress-dev": "vitepress dev docs --port 5050 --open",
    "vitepress-build": "vitepress build docs",
    "docs": "concurrently --group mdsnippets \"vitepress dev docs --port 5050 --open\"",
    "docs-build": "concurrently --group mdsnippets \"vitepress build docs\"",
    "deploy-preview": "netlify deploy",
    "deploy": "netlify deploy --prod"
  },
  "devDependencies": {
    "concurrently": "^9.1.2",
    "markdown-it-block-embed": "^0.0.3",
    "netlify-cli": "^21.5.0",
    "vitepress": "1.6.3",
    "vitepress-plugin-llms": "^1.5.1",
    "vitepress-plugin-mermaid": "^2.0.17"
  }
}

```

### File: README.md
```md
# Marten

## .NET Transactional Document DB and Event Store on PostgreSQL

[![Discord](https://img.shields.io/discord/1074998995086225460?color=blue&label=Chat%20on%20Discord)](https://discord.gg/WMxrvegf8H)
![Twitter Follow](https://img.shields.io/twitter/follow/marten_lib?logo=Twitter&style=flat-square)
[![Windows Build Status](https://ci.appveyor.com/api/projects/status/va5br63j7sbx74cm/branch/master?svg=true)](https://ci.appveyor.com/project/jasper-ci/marten/branch/master)
[![Linux Build status](https://dev.azure.com/jasperfx-marten/marten/_apis/build/status/marten?branchName=master)](https://dev.azure.com/jasperfx-marten/marten/_build/latest?definitionId=1&branchName=master)
[![Nuget Package](https://badgen.net/nuget/v/marten)](https://www.nuget.org/packages/Marten/)
[![Nuget](https://img.shields.io/nuget/dt/marten)](https://www.nuget.org/packages/Marten/)

<div align="center">
    <img src="https://github.com/user-attachments/assets/f052d5a7-1f49-4aa7-91f6-cba415988d14" alt="marten logo" width="70%">
</div>

The Marten library provides .NET developers with the ability to use the proven [PostgreSQL database engine](http://www.postgresql.org/) and its [fantastic JSON support](https://web.archive.org/web/20230127180328/https://www.compose.com/articles/is-postgresql-your-next-json-database/) as a fully fledged [document database](https://en.wikipedia.org/wiki/Document-oriented_database). The Marten team believes that a document database has far reaching benefits for developer productivity over relational databases with or without an ORM tool.

Marten also provides .NET developers with an ACID-compliant event store with user-defined projections against event streams.

Access docs [here](https://martendb.io/). For any of your queries including the whole of Critter stack, join our [Discord channel](https://discord.gg/WMxrvegf8H) and it is the best way to reach us quickly. You can also raise questions/queries via [GitHub Discussions](https://github.com/JasperFx/marten/discussions) as well.

## Support Plans

<div align="center">
    <img src="https://www.jasperfx.net/logo.png" alt="JasperFx logo" width="70%">
</div>

While Marten is open source, [JasperFx Software offers paid support and consulting contracts](https://jasperfx.net/support-plans/) for Marten.

## Help us keep working on this project 💚

[Become a Sponsor on GitHub](https://github.com/sponsors/JasperFX) by sponsoring monthly or one time.

### Past Sponsors

<p align="left">
    <a href="https://aws.amazon.com/dotnet" target="_blank" rel="noopener noreferrer">
    <picture>
      <source srcset="https://martendb.io/dotnet-aws.png" media="(prefers-color-scheme: dark)" height="72px" alt=".NET on AWS" />
      <img src="https://martendb.io/dotnet-aws.png" height="72px" alt=".NET on AWS" />
    </picture>
  </a>
</p>

## Working with the Code

Before getting started you will need the following in your environment:

### 1. .NET SDK 8.0+

Available [here](https://dotnet.microsoft.com/download)

### 2. PostgreSQL 13 or above database

The fastest possible way to develop with Marten is to run PostgreSQL in a Docker container. Assuming that you have Docker running on your local box, type:
`docker-compose up`
or
`dotnet run --framework net6.0 -- init-db`
at the command line to spin up a Postgresql database withThe default Marten test configuration tries to find this database if no
PostgreSQL database connection string is explicitly configured following the steps below:

### Native Partial Updates/Patching

Marten supports native patching since v7.x. you can refer to [patching api](https://martendb.io/documents/partial-updates-patching.html) for more details.

### PLV8

If you'd like to use [PLV8 Patching Api](https://martendb.io/documents/plv8.html#the-patching-api) you need to enable the PLV8 extension inside of PostgreSQL for running JavaScript stored procedures for the nascent projection support.

Note that PLV8 patching will be deprecated in future versions and native patching is the drop in replacement for it. You can easily migrate to native patching, refer [here](https://martendb.io/documents/partial-updates-patching.html#patching-api) for more details.

Ensure the following:

- The login you are using to connect to your database is a member of the `postgres` role
- An environment variable of `marten_testing_database` is set to the connection string for the database you want to use as a testbed. (See the [Npgsql documentation](http://www.npgsql.org/doc/connection-string-parameters.html) for more information about PostgreSQL connection strings ).

_Help with PSQL/PLV8_

- On Windows, see [this link](http://www.postgresonline.com/journal/archives/360-PLV8-binaries-for-PostgreSQL-9.5-windows-both-32-bit-and-64-bit.html) for pre-built binaries of PLV8
- On *nix, check [marten-local-db](https://github.com/eouw0o83hf/marten-local-db) for a Docker based PostgreSQL instance including PLV8.

### Test Config Customization

Some of our tests are run against a particular PostgreSQL version. If you'd like to run different database versions, you can do it by setting `POSTGRES_IMAGE` env variables, for instance:

```bash
POSTGRES_IMAGE=postgres:15.3-alpine docker compose up
```

Tests explorer should be able to detect database version automatically, but if it's not able to do it, you can enforce it by setting `postgresql_version` to a specific one (e.g.)

```shell
postgresql_version=15.3
```

Once you have the codebase and the connection string file, run the [build command](https://github.com/JasperFx/marten#build-commands) or use the dotnet CLI to restore and build the solution.

You are now ready to contribute to Marten.

See more in [Contribution Guidelines](CONTRIBUTING.md).

### Tooling

* Unit Tests rely on [xUnit](http://xunit.github.io/) and [Shouldly](https://github.com/shouldly/shouldly)
* [Bullseye](https://github.com/adamralph/bullseye) is used for build automation.
* [Node.js](https://nodejs.org/en/) runs our Mocha specs.
* [Storyteller](http://storyteller.github.io) for some of the data intensive automated tests

### Build Commands

| Description                         | Windows Commandline      | PowerShell               | Linux Shell             | DotNet CLI                                                |
|-------------------------------------|--------------------------|--------------------------|-------------------------|-----------------------------------------------------------|
| Run restore, build and test         | `build.cmd`              | `build.ps1`              | `build.sh`              | `dotnet build src\Marten.sln`                             |
| Run all tests including mocha tests | `build.cmd test`         | `build.ps1 test`         | `build.sh test`         | `dotnet run --project build/build.csproj -- test`         |
| Run just mocha tests                | `build.cmd mocha`        | `build.ps1 mocha`        | `build.sh mocha`        | `dotnet run --project build/build.csproj -- mocha`        |
| Run StoryTeller tests               | `build.cmd storyteller`  | `build.ps1 storyteller`  | `build.sh storyteller`  | `dotnet run --project build/build.csproj -- storyteller`  |
| Open StoryTeller editor             | `build.cmd open_st`      | `build.ps1 open_st`      | `build.sh open_st`      | `dotnet run --project build/build.csproj -- open_st`      |
| Run docs website locally            | `build.cmd docs`         | `build.ps1 docs`         | `build.sh docs`         | `dotnet run --project build/build.csproj -- docs`         |
| Publish docs                        | `build.cmd publish-docs` | `build.ps1 publish-docs` | `build.sh publish-docs` | `dotnet run --project build/build.csproj -- publish-docs` |
| Run benchmarks                      | `build.cmd benchmarks`   | `build.ps1 benchmarks`   | `build.sh benchmarks`   | `dotnet run --project build/build.csproj -- benchmarks`   |

> Note: You should have a running Postgres instance while running unit tests or StoryTeller tests.

### xUnit.Net Specs

The tests for the main library are now broken into three testing projects:

1. `CoreTests` -- basic services like retries, schema management basics
1. `DocumentDbTests` -- anything specific to the document database features of Marten
1. `EventSourcingTests` -- anything specific to the event sourcing features of Marten

To aid in integration testing, Marten.Testing has a couple reusable base classes that can be use
to make integration testing through Postgresql be more efficient and allow the xUnit.Net tests
to run in parallel for better throughput.

- `IntegrationContext` -- if most of the tests will use an out of the box configuration
  (i.e., no fluent interface configuration of any document types), use this base type. Warning though,
  this context type will **not** clean out the main `public` database schema between runs,
  but will delete any existing data
- `DestructiveIntegrationContext` -- similar to `IntegrationContext`, but will wipe out any and all
  Postgresql schema objects in the `public` schema between tests. Use this sparingly please.
- `OneOffConfigurationsContext` -- if a test suite will need to frequently re-configure
  the `DocumentStore`, this context is appropriate. You do *not* need to decorate any of these
  test classes with the `[Collection]` attribute. This fixture will use an isolated schema using the name of the
  test fixture type as the schema name
- `BugIntegrationContext` -- the test harnesses for bugs tend to require custom `DocumentStore`
  configuration, and this context is a specialization of `OneOffConfigurationsContext` for
  the *bugs* schema.
- `StoreFixture` and `StoreContext` are helpful if a series of tests use the same custom
  `DocumentStore` configuration. You'd need to write a subclass of `StoreFixture`, then use
  `StoreContext<YourNewStoreFixture>` as the base class to share the `DocumentStore` between
  test runs with xUnit.Net's shared context (`IClassFixture<T>`)

### Mocha Specs

Refer to the build commands section to look up the commands to run Mocha tests. There is also `npm run tdd` to run the mocha specifications
in a watched mode with growl turned on.

> Note: remember to run `npm install`

### Storyteller Specs

Refer to build commands section to look up the commands to open the StoryTeller editor or run the StoryTeller specs.

### Current Build Matrix

| CI              | .NET | Postgres  |        plv8        | Serializer | 
|-----------------|:----:|:---------:|:------------------:|:----------:|
| GitHub Actions  |  8   |   12.8    | :white_check_mark: |    STJ     | 
| GitHub Actions  |  8   | 15-alpine |        :x:         | Newtonsoft | 
| GitHub Actions  |  7   |   12.8    | :white_check_mark: |  JSON.NET  | 
| GitHub Actions  |  7   |  latest   |        :x:         |    STJ     | 
| Azure Pipelines |  6   |   12.8    | :white_check_mark: |  JSON.NET  | 
| Azure Pipelines |  6   |   12.8    | :white_check_mark: |    STJ     | 
| Azure Pipelines |  6   | 15-alpine |        :x:         |    STJ     | 
| Azure Pipelines |  6   |  latest   |        :x:         | Newtonsoft | 

## Documentation

All the documentation is written in Markdown and the docs are published as a static site hosted in Netlify. v4.x and v3.x use different documentation tools hence are detailed below in separate sub-sections.

### v4.x and above

[VitePress](https://vitepress.vuejs.org/) is used as documentation tool. Along with this, [MarkdownSnippets](https://github.com/SimonCropp/MarkdownSnippets) is used for adding code snippets to docs from source code and [Algolia DocSearch](https://docsearch.algolia.com/) is used for searching the docs via the search box.

The documentation content is the Markdown files in the `/docs` directory directly under the project root. To run the docs locally use `npm run docs` with auto-refresh on any changes.

To add code samples/snippets from the tests in docs, follow the steps below:

Use C# named regions to mark a code block as described in the sample below

```csharp
#region sample_my-snippet
// code sample/snippet
// ...
#endregion
```

All code snippet identifier starts with `sample_` as a convention to clearly identify that the region block corresponds to a sample code/snippet used in docs. Recommend to use kebab case for the identifiers with words in lower case.

Use the below to include the code snippet in a docs page

<pre>
&#60;!-- snippet: sample_my-snippet -->
&#60;!-- endSnippet -->
</pre>

Note that when you run the docs locally, the above placeholder block in the Markdown file will get updated inline with the actual code snippet from the source code. Please commit the changes with the auto-generated inline code snippet as-is after you preview the docs page. This helps with easier change tracking when you send PR's.

Few gotchas:

- Any changes to the code snippets will need to done in the source code. Do not edit/update any of the auto-generated inline code snippet directly in the Markdown files.
- The latest snippet are always pulled into the docs while we publish the docs. Hence do not worry about the inline code snippet in Markdown file getting out of sync with the snippet in source code.

### v3.x

[stdocs](https://www.nuget.org/packages/dotnet-stdocs/) is used as documentation tool. The documentation content is the markdown files in the `/documentation` directory directly under the project root. Any updates to v3.x docs will need to done in [3.14 branch](https://github.com/JasperFx/marten/tree/3.14). To run the documentation website locally with auto-refresh, refer to the build commands section above.

If you wish to insert code samples/snippet to a documentation page from the tests, wrap the code you wish to insert with
`// SAMPLE: name-of-sample` and `// ENDSAMPLE`.
Then to insert that code to the documentation, add `<[sample:name-of-sample]>`.

> Note: content is published to the `gh-pages` branch of this repository. Refer to build commands section to lookup the command for publishing docs.

## License

Copyright © Jeremy D. Miller, Babu Annamalai, Oskar Dudycz, Joona-Pekka Kokko and contributors.

Marten is provided as-is under the MIT license. For more information see [LICENSE](LICENSE).

## Code of Conduct

This project has adopted the code of conduct defined by the [Contributor Covenant](http://contributor-covenant.org/) to clarify expected behavior in our community.

```

### File: docs\.vitepress\theme\index.js
```js
import DefaultTheme from 'vitepress/theme'
import './custom.css'
import CustomLayout from './CustomLayout.vue'

export default {
  extends: DefaultTheme,
  Layout: CustomLayout
}

```

### File: .markdownlint.json
```json
{
    "MD024": false,
    "MD013": false,
    "MD026": false,
    "MD031": false,
    "MD033": false,
    "MD046": false
}

```

### File: build.ps1
```ps1
[CmdletBinding()]
Param(
    [Parameter(Position=0,Mandatory=$false,ValueFromRemainingArguments=$true)]
    [string[]]$BuildArguments
)

Write-Output "PowerShell $($PSVersionTable.PSEdition) version $($PSVersionTable.PSVersion)"

Set-StrictMode -Version 2.0; $ErrorActionPreference = "Stop"; $ConfirmPreference = "None"; trap { Write-Error $_ -ErrorAction Continue; exit 1 }
$PSScriptRoot = Split-Path $MyInvocation.MyCommand.Path -Parent

###########################################################################
# CONFIGURATION
###########################################################################

$BuildProjectFile = "$PSScriptRoot\build\build.csproj"
$TempDirectory = "$PSScriptRoot\..\.nuke\temp"

$DotNetGlobalFile = "$PSScriptRoot\..\global.json"
$DotNetInstallUrl = "https://dot.net/v1/dotnet-install.ps1"
$DotNetChannel = "STS"

$env:DOTNET_CLI_TELEMETRY_OPTOUT = 1
$env:DOTNET_NOLOGO = 1

###########################################################################
# EXECUTION
###########################################################################

function ExecSafe([scriptblock] $cmd) {
    & $cmd
    if ($LASTEXITCODE) { exit $LASTEXITCODE }
}

# If dotnet CLI is installed globally and it matches requested version, use for execution
if ($null -ne (Get-Command "dotnet" -ErrorAction SilentlyContinue) -and `
     $(dotnet --version) -and $LASTEXITCODE -eq 0) {
    $env:DOTNET_EXE = (Get-Command "dotnet").Path
}
else {
    # Download install script
    $DotNetInstallFile = "$TempDirectory\dotnet-install.ps1"
    New-Item -ItemType Directory -Path $TempDirectory -Force | Out-Null
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    (New-Object System.Net.WebClient).DownloadFile($DotNetInstallUrl, $DotNetInstallFile)

    # If global.json exists, load expected version
    if (Test-Path $DotNetGlobalFile) {
        $DotNetGlobal = $(Get-Content $DotNetGlobalFile | Out-String | ConvertFrom-Json)
        if ($DotNetGlobal.PSObject.Properties["sdk"] -and $DotNetGlobal.sdk.PSObject.Properties["version"]) {
            $DotNetVersion = $DotNetGlobal.sdk.version
        }
    }

    # Install by channel or version
    $DotNetDirectory = "$TempDirectory\dotnet-win"
    if (!(Test-Path variable:DotNetVersion)) {
        ExecSafe { & powershell $DotNetInstallFile -InstallDir $DotNetDirectory -Channel $DotNetChannel -NoPath }
    } else {
        ExecSafe { & powershell $DotNetInstallFile -InstallDir $DotNetDirectory -Version $DotNetVersion -NoPath }
    }
    $env:DOTNET_EXE = "$DotNetDirectory\dotnet.exe"
    $env:PATH = "$DotNetDirectory;$env:PATH"
}

Write-Output "Microsoft (R) .NET SDK version $(& $env:DOTNET_EXE --version)"

if (Test-Path env:NUKE_ENTERPRISE_TOKEN) {
    & $env:DOTNET_EXE nuget remove source "nuke-enterprise" > $null
    & $env:DOTNET_EXE nuget add source "https://f.feedz.io/nuke/enterprise/nuget" --name "nuke-enterprise" --username "PAT" --password $env:NUKE_ENTERPRISE_TOKEN > $null
}

ExecSafe { & $env:DOTNET_EXE build $BuildProjectFile /nodeReuse:false /p:UseSharedCompilation=false -nologo -clp:NoSummary --verbosity quiet }
ExecSafe { & $env:DOTNET_EXE run --project $BuildProjectFile --no-build -- $BuildArguments }

```

### File: build.sh
```sh
#!/usr/bin/env bash

bash --version 2>&1 | head -n 1

set -eo pipefail
SCRIPT_DIR=$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)

###########################################################################
# CONFIGURATION
###########################################################################

BUILD_PROJECT_FILE="$SCRIPT_DIR/build/build.csproj"
TEMP_DIRECTORY="$SCRIPT_DIR/../.nuke/temp"

DOTNET_GLOBAL_FILE="$SCRIPT_DIR/../global.json"
DOTNET_INSTALL_URL="https://dot.net/v1/dotnet-install.sh"
DOTNET_CHANNEL="STS"

export DOTNET_CLI_TELEMETRY_OPTOUT=1
export DOTNET_NOLOGO=1

###########################################################################
# EXECUTION
###########################################################################

function FirstJsonValue {
    perl -nle 'print $1 if m{"'"$1"'": "([^"]+)",?}' <<< "${@:2}"
}

# If dotnet CLI is installed globally and it matches requested version, use for execution
if [ -x "$(command -v dotnet)" ] && dotnet --version &>/dev/null; then
    export DOTNET_EXE="$(command -v dotnet)"
else
    # Download install script
    DOTNET_INSTALL_FILE="$TEMP_DIRECTORY/dotnet-install.sh"
    mkdir -p "$TEMP_DIRECTORY"
    curl -Lsfo "$DOTNET_INSTALL_FILE" "$DOTNET_INSTALL_URL"
    chmod +x "$DOTNET_INSTALL_FILE"

    # If global.json exists, load expected version
    if [[ -f "$DOTNET_GLOBAL_FILE" ]]; then
        DOTNET_VERSION=$(FirstJsonValue "version" "$(cat "$DOTNET_GLOBAL_FILE")")
        if [[ "$DOTNET_VERSION" == ""  ]]; then
            unset DOTNET_VERSION
        fi
    fi

    # Install by channel or version
    DOTNET_DIRECTORY="$TEMP_DIRECTORY/dotnet-unix"
    if [[ -z ${DOTNET_VERSION+x} ]]; then
        "$DOTNET_INSTALL_FILE" --install-dir "$DOTNET_DIRECTORY" --channel "$DOTNET_CHANNEL" --no-path
    else
        "$DOTNET_INSTALL_FILE" --install-dir "$DOTNET_DIRECTORY" --version "$DOTNET_VERSION" --no-path
    fi
    export DOTNET_EXE="$DOTNET_DIRECTORY/dotnet"
    export PATH="$DOTNET_DIRECTORY:$PATH"
fi

echo "Microsoft (R) .NET SDK version $("$DOTNET_EXE" --version)"

if [[ ! -z ${NUKE_ENTERPRISE_TOKEN+x} && "$NUKE_ENTERPRISE_TOKEN" != "" ]]; then
    "$DOTNET_EXE" nuget remove source "nuke-enterprise" &>/dev/null || true
    "$DOTNET_EXE" nuget add source "https://f.feedz.io/nuke/enterprise/nuget" --name "nuke-enterprise" --username "PAT" --password "$NUKE_ENTERPRISE_TOKEN" --store-password-in-clear-text &>/dev/null || true
fi

"$DOTNET_EXE" build "$BUILD_PROJECT_FILE" /nodeReuse:false /p:UseSharedCompilation=false -nologo -clp:NoSummary --verbosity quiet
"$DOTNET_EXE" run --project "$BUILD_PROJECT_FILE" --no-build -- "$@"

```

### File: centralization-for-marten-9.md
```md
# Centralization Plan for Marten 9: Shared Infrastructure with Polecat via Weasel.Core

## Context

Marten (PostgreSQL) and Polecat (SQL Server 2025) share significant infrastructure patterns. Common base types and interfaces should move to Weasel.Core so both projects can share them without database-specific coupling.

---

## Category 1: Metadata Interfaces — Identical, move to Weasel.Core

These are exact duplicates (modulo namespace and nullability) with zero database-specific logic. They're pure document metadata contracts.

| Interface | Marten (`Marten.Metadata`) | Polecat (`Polecat.Metadata`) | Status |
|-----------|--------|---------|--------|
| `IVersioned` | `Guid Version { get; set; }` | `Guid Version { get; set; }` | **Identical** |
| `ISoftDeleted` | `bool Deleted; DateTimeOffset? DeletedAt` | `bool Deleted; DateTimeOffset? DeletedAt` | **Identical** |
| `IRevisioned` | `int Version { get; set; }` | Does not exist yet | Marten-only; worth putting in Weasel.Core for Polecat to adopt later |
| `ITracked` | Non-nullable `string` members | Nullable `string?` members | **Needs alignment** — Polecat's nullable approach is more correct |

**Action:** Move all four to `Weasel.Core.Metadata` namespace. Align `ITracked` on nullable strings. Both Marten and Polecat type-forward or alias from their own namespaces.

---

## Category 2: Serialization Enums — Already partially shared

| Type | Weasel.Core | Marten | Polecat |
|------|-------------|--------|---------|
| `EnumStorage` | Yes (canonical) | Uses Weasel.Core's | Own copy (duplicate) |
| `Casing` | **No** | Defined in `ISerializer.cs` | Own copy (duplicate) |
| `CollectionStorage` | **No** | Defined in `ISerializer.cs` | Own copy (duplicate) |
| `NonPublicMembersStorage` | **No** | Defined in `ISerializer.cs` | Own copy (duplicate) |

**Action:** Move `Casing`, `CollectionStorage`, and `NonPublicMembersStorage` to Weasel.Core alongside the existing `EnumStorage`. Polecat already duplicates all three and can switch to the Weasel.Core versions.

---

## Category 3: ISerializer Interface — Strong overlap, worth unifying

### Shared surface (present in both Marten and Polecat)

```csharp
EnumStorage EnumStorage { get; }
Casing Casing { get; }
string ToJson(object document);
T FromJson<T>(Stream stream);
T FromJson<T>(DbDataReader reader, int index);
object FromJson(Type type, Stream stream);
object FromJson(Type type, DbDataReader reader, int index);
ValueTask<T> FromJsonAsync<T>(Stream stream, CancellationToken cancellationToken = default);
ValueTask<object> FromJsonAsync(Type type, Stream stream, CancellationToken cancellationToken = default);
```

### Marten-only additions

- `ValueCasting ValueCasting { get; }` — controls LINQ Select() casting behavior
- `string ToCleanJson(object? document)` — serialize without type metadata
- `string ToJsonWithTypes(object document)` — serialize with embedded type info
- `ValueTask<T> FromJsonAsync<T>(DbDataReader reader, int index, CancellationToken)` — async reader deserialization
- `ValueTask<object> FromJsonAsync(Type type, DbDataReader reader, int index, CancellationToken)` — async reader deserialization (non-generic)

### Polecat-only additions

- `T FromJson<T>(string json)` — string-based deserialization
- `object FromJson(Type type, string json)` — string-based deserialization (non-generic)

**Action:** Define a common `ISerializer` interface in Weasel.Core with the shared members. Both Marten and Polecat extend it with project-specific additions via their own derived interfaces.

---

## Category 4: IStorageOperation — Similar but divergent patterns

Both have a storage operation concept with `DocumentType`, `Role`, and `PostprocessAsync(DbDataReader)`, but the interfaces diverge:

| Aspect | Marten | Polecat |
|--------|--------|---------|
| Inheritance | Inherits `IQueryHandler` (LINQ) | Standalone |
| Role | `OperationRole Role()` (method) | `OperationRole Role { get; }` (property) |
| Postprocess | `IList<Exception>` parameter | No exceptions parameter |
| Command setup | Via `IQueryHandler` | `ConfigureCommand(ICommandBuilder)` |
| Document ID | Not on interface | `object? DocumentId` default method |
| Enum values | `Upsert, Insert, Update, Deletion, Patch, Events, Other` | `Upsert, Insert, Update, Delete, Patch` |

**Action:** Extract a minimal common `OperationRole` enum and a slim `IStorageOperation` base to Weasel.Core. Both projects extend with their specific needs. Lower priority since the divergence is larger.

---

## Category 5: Session Interfaces — Too divergent, do not share

`IQuerySession`, `IDocumentSession`, `IDocumentOperations`, `IDocumentStore` are conceptually similar but:

- **Marten** is much larger: `NpgsqlConnection Connection`, full-text search, bulk insert via PostgreSQL COPY, dirty tracking sessions, serializable isolation variants, 65+ members on `IDocumentStore`
- **Polecat** is intentionally minimal: ~10 members on `IDocumentStore`, no dirty tracking, no full-text search

Forcing a common interface would either bloat Polecat or gut Marten.

**Action:** Keep project-specific. No shared base.

---

## Recommended Priority Order

1. **Metadata interfaces** (`IVersioned`, `ISoftDeleted`, `ITracked`, `IRevisioned`) → Weasel.Core
   - Easiest win, zero risk, zero database coupling

2. **Serialization enums** (`Casing`, `CollectionStorage`, `NonPublicMembersStorage`) → Weasel.Core
   - Alongside existing `EnumStorage`. Eliminates Polecat duplicates

3. **ISerializer base interface** → Weasel.Core with shared members
   - Both projects extend for their extras

4. **OperationRole enum + minimal IStorageOperation** → Weasel.Core
   - Lower priority, interfaces diverge more

5. **Session interfaces** → Do not share

```

### File: CLAUDE.md
```md
# Marten

.NET transactional document database and event store on PostgreSQL. Uses PostgreSQL's JSONB support for document storage with ACID guarantees and a full event sourcing implementation with projections.

**Repository:** https://github.com/JasperFx/marten
**Version:** 8.20.0 (`Directory.Build.props:4`)
**License:** MIT

## Tech Stack

- **Language:** C# 13.0, targets net8.0 / net9.0 / net10.0 (`Directory.Build.props:5,12`)
- **Database:** PostgreSQL 13+ (via Npgsql)
- **Key deps:** JasperFx, JasperFx.Events, JasperFx.RuntimeCompiler, Weasel.Postgresql, Newtonsoft.Json (`src/Marten/Marten.csproj:39-46`)
- **Build system:** Nuke (`build/build.cs`)
- **Test framework:** xUnit + Shouldly
- **Docs:** VitePress (`docs/`)

## Project Structure

```
src/
  Marten/                  - Core library (document store, event store, LINQ, sessions)
  Marten.AspNetCore/       - ASP.NET Core integration (streaming endpoints)
  Marten.NodaTime/         - NodaTime date/time support
  Marten.Testing/          - Shared test harness: fixtures, base classes, helpers
  CoreTests/               - Schema management, retries, core services
  DocumentDbTests/         - Document storage features
  EventSourcingTests/      - Event sourcing, projections, daemon
  LinqTests/               - LINQ-to-SQL translation
  MultiTenancyTests/       - Multi-tenancy isolation
  PatchingTests/           - Partial document updates
  ValueTypeTests/          - Strongly-typed ID support
  DaemonTests/             - Async projection daemon
  Marten.CommandLine.Tests/- CLI tool tests
  CommandLineRunner/       - CLI for codegen and DB management
  TestingSupport/          - Shared test infrastructure
build/                     - Nuke build automation
docs/                      - VitePress documentation site
```

### Key Source Directories Within `src/Marten/`

| Directory | Purpose |
|-----------|---------|
| `Events/` | Event sourcing: appenders, projections, aggregation, daemon |
| `Internal/Sessions/` | Session implementations (lightweight, identity map, dirty tracking) |
| `Internal/Storage/` | Document storage variants and providers |
| `Internal/Operations/` | Storage operations (insert, update, upsert, delete) |
| `Internal/CodeGeneration/` | Runtime code generation for storage providers |
| `Linq/` | LINQ query parsing, SQL generation, compiled queries |
| `Schema/` | Document mapping, indexes, DDL generation |
| `Storage/` | Tenancy strategies, database management |
| `Patching/` | Fluent partial-update API |
| `Subscriptions/` | Event subscription processing |
| `Metadata/` | Metadata policies (versioning, soft delete, timestamps) |

## Build & Test

**Prerequisites:** .NET SDK 8.0+, PostgreSQL 13+ (Docker recommended)

```bash
# Start PostgreSQL
docker-compose up -d

# Build
./build.sh compile

# Run all tests
./build.sh test

# Run individual test suites
./build.sh test-core              # CoreTests
./build.sh test-document-db       # DocumentDbTests
./build.sh test-event-sourcing    # EventSourcingTests
./build.sh test-linq              # LinqTests
./build.sh test-multi-tenancy     # MultiTenancyTests
./build.sh test-patching          # PatchingTests
./build.sh test-value-types       # ValueTypeTests
./build.sh test-cli               # Marten.CommandLine.Tests
./build.sh test-base-lib          # Marten.Testing
./build.sh test-code-gen          # Code generation round-trip
./build.sh test-extensions        # NodaTime + AspNetCore

# Docs
npm install && npm run docs
```

Default test connection: `Host=localhost;Port=5432;Database=marten_testing;Username=postgres;password=postgres` (`build/build.cs:28`). Override with `marten_testing_database` env var.

## Test Harness

Base classes in `src/Marten.Testing/Harness/`:

- **`IntegrationContext`** (`IntegrationContext.cs:49`) - Standard integration tests. Shared `DocumentStore`, deletes all data between tests. Uses `[Collection("integration")]`.
- **`DestructiveIntegrationContext`** - Wipes entire public schema between tests.
- **`OneOffConfigurationsContext`** - Creates isolated `DocumentStore` with custom schema per test.
- **`BugIntegrationContext`** - Like `OneOffConfigurationsContext`, for bug regression tests.
- **`StoreFixture` / `StoreContext<T>`** - Share `DocumentStore` across tests via collection fixtures.
- **`SessionTypesAttribute`** (`IntegrationContext.cs:36`) - Theory data source for testing across None/IdentityOnly/DirtyTracking session modes.

## Environment Variables

| Variable | Purpose |
|----------|---------|
| `marten_testing_database` | Override test connection string |
| `DEFAULT_SERIALIZER` | `SystemTextJson` or `Newtonsoft` (default) |
| `DISABLE_TEST_PARALLELIZATION` | `true` to disable parallel test execution |
| `postgresql_version` | Enforce specific PostgreSQL version detection |

## CI

GitHub Actions runs matrix builds across .NET 8/10, PostgreSQL 15/latest, and both serializers. Workflows in `.github/workflows/`. Tests run in Release config with parallelization disabled.

## Additional Documentation

When working on specific areas, check these files for patterns and conventions:

- [Architectural Patterns](.claude/docs/architectural_patterns.md) - Design patterns, DI conventions, session model, code generation, event sourcing patterns, and testing conventions used across the codebase.
- [VitePress Docs](docs/) - User-facing documentation with code samples referenced via `<!-- snippet: sample_* -->` markers tied to `#region sample_*` blocks in source.
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution workflow, PR guidelines, git rebase strategy.

```

### File: CONTRIBUTING.md
```md
# Contributing to Marten

We take Pull Requests!

## Before you send Pull Request

1. Contact the contributors via the [Discord channel](https://discord.gg/WMxrvegf8H) or the [Github Issue](https://github.com/JasperFx/marten/issues/new) to make sure that this is issue or bug should be handled with proposed way. Send details of your case and explain the details of the proposed solution.
2. Once you get approval from one of the maintainers, you can start to work on your code change.
3. After your changes are ready, make sure that you covered your case with automated tests and verify that you have limited the number of breaking changes to a bare minimum.
4. We also highly appreciate any relevant updates to the documentation.
5. Make sure that your code is compiling and all automated tests are passing.

## After you have sent Pull Request

1. Make sure that you applied or answered all the feedback from the maintainers.
2. We're trying to be as much responsive as we can, but if we didn't respond to you, feel free to ping us on the [Discord channel](https://discord.gg/WMxrvegf8H).
3. Pull request will be merged when you get approvals from at least 2 of the maintainers (and no rejection from others). Pull request will be tagged with the target Marten version in which it will be released. We also label the Pull Requests with information about the type of change.

## Setup your work environment

We try to limit the number of necessary setup to a minimum, but few steps are still needed:

**1. .NET Core SDK 6.0+**

Available [here](https://dotnet.microsoft.com/download)

**2. PostgreSQL 12 or above database**

The fastest possible way to develop with Marten is to run PostgreSQL in a Docker container. Assuming that you have Docker running on your local box, type:
`docker-compose up`
or
`dotnet run --framework net6.0 -- init-db`
at the command line to spin up a Postgresql database withThe default Marten test configuration tries to find this database if no
PostgreSQL database connection string is explicitly configured following the steps below:

**PLV8**

If you'd like to use [Patching Api](https://martendb.io/documents/plv8.html#the-patching-api) you need to enable the PLV8 extension inside of PostgreSQL for running JavaScript stored procedures for the nascent projection support.

Ensure the following:

- The login you are using to connect to your database is a member of the `postgres` role
- An environment variable of `marten_testing_database` is set to the connection string for the database you want to use as a testbed. (See the [Npgsql documentation](http://www.npgsql.org/doc/connection-string-parameters.html) for more information about PostgreSQL connection strings ).

_Help with PSQL/PLV8_

- On Windows, see [this link](http://www.postgresonline.com/journal/archives/360-PLV8-binaries-for-PostgreSQL-9.5-windows-both-32-bit-and-64-bit.html) for pre-built binaries of PLV8
- On *nix, check [marten-local-db](https://github.com/eouw0o83hf/marten-local-db) for a Docker based PostgreSQL instance including PLV8.

Once you have the codebase and the connection string file, run the [build command](https://github.com/JasperFx/marten#build-commands) or use the dotnet CLI to restore and build the solution.

You are now ready to contribute to Marten.

**Node.js**

If you want to update or add new documentation, you need to have Node.js installed on your machine. The recommended version is the latest LTS version. You can download it from the [official website](https://nodejs.org/) or using a version manager like [nvm](https://github.com/nvm-sh/nvm).

After installing Node.js, you can install the required packages by running the following command in the root directory of this repository:

```bash
npm install
```

## Working with the Git

1. Fork the repository.
2. Create a feature branch from the `master` branch.
3. We're not squashing the changes and using rebase strategy for our branches (see more in [Git documentation](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)). Having that, we highly recommend using clear commit messages. Commits should also represent the unit of change.
4. Before sending PR to make sure that you rebased the latest `master` branch from the main Marten repository.
5. When you're ready to create the [Pull Request on GitHub](https://github.com/JasperFx/marten/compare).

## Code style

Coding rules are set up in the [.editorconfig file](.editorconfig). This file is supported by all popular IDE (eg. Microsoft Visual Studio, Rider, Visual Studio Code) so if you didn't disable it manually they should be automatically applied after opening the solution. We also recommend turning automatic formatting on saving to have all the rules applied.

## Documentation

If you want to update or add new documentation, you can find the documentation in the `docs` directory.

We're using [MarkdownSnippets](https://github.com/SimonCropp/MarkdownSnippets) to include the C# code examples in the documentation.

If you want to add code examples to the documentation, you have to add a C# file which includes the code example or annotate existing files with a unique C# #region/#endregion pair:

```csharp
#region sample_my_unique_name
// Your code example here
#endregion
```

Then you can refer to the code example in the Markdown file by using the following syntax:

![Referring the code example](assets/mdsnippet-sample.png)

After adding the code example, you can run the following command to update the documentation:

```bash
npm run mdsnippets
```

You can find examples if you search this repository for "sample_" or "snippet:".

## Licensing and legal rights

By contributing to Marten:

1. You assert that contribution is your original work.
2. You assert that you have the right to assign the copyright for the work.
3. You are accepting the [License](LICENSE).

## Code of Conduct

This project has adopted the code of conduct defined by the [Contributor Covenant](http://contributor-covenant.org/) to clarify expected behavior in our community.

```

### File: dcb-concepts.md
```md
# DCB (Dynamic Consistency Boundary) Implementation in Marten

## What is DCB?

DCB is a technique for enforcing consistency in event-driven systems without rigid aggregate-based transactional boundaries. It allows events to be assigned to **multiple domain concepts** via tags, and enforces consistency across them using conditional appends.

**Core spec (https://dcb.events/):**
- **Read**: Filter events by event type (OR) and/or tags (AND within a query item, OR across items)
- **Write**: Atomically persist events, failing if any event matching a query exists after a given global sequence position

## Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Coexistence | DCB coexists with traditional stream-based event sourcing | Purely additive — users tag some events, use streams for others |
| Stream requirement | DCB events always belong to a stream | Keeps existing stream infrastructure intact |
| Condition model | First-class "condition" pattern | Encapsulates query + state + consistency check as a formal concept |
| Append atomicity | Condition check within `SaveChangesAsync()` transaction | True consistency, no check-then-act race |
| Append modes | Both Rich and Quick | Full compatibility |
| Tenancy | Scoped to current tenant by default | Opt-in for cross-tenant queries |
| Portability | Abstractions in JasperFx.Events, PostgreSQL impl in Marten | Maximizes portability |
| Tag extraction | Write-time with backfill tool | Pre-computed for query performance; backfill for migration |
| Schema | Opt-in `tags TEXT[]` column + GIN index on `mt_events` | No impact to existing users |
| Performance target | ~1ms per event at 1M events | Aligned with DCB FAQ benchmarks |

## Storage Approach

### Recommended: `TEXT[]` column with GIN index

When DCB is enabled, add to `mt_events`:

```sql
ALTER TABLE mt_events ADD COLUMN tags TEXT[];
CREATE INDEX ix_mt_events_tags ON mt_events USING GIN (tags);
```

**Why this over alternatives:**
- **vs normalized junction table**: No JOINs, single-table queries, simpler writes
- **vs JSONB headers**: Dedicated column with native array operators, proper GIN indexing, no mixing concerns
- **vs query-time computation**: Pre-computed tags enable indexed conditional append checks — the core DCB performance requirement

### Conditional Append SQL

The append condition check runs within the same transaction as event insertion:

```sql
SELECT EXISTS (
  SELECT 1 FROM mt_events
  WHERE seq_id > @after
  AND (
    -- Query Item 1 (types OR'd, tags AND'd within item)
    (type = ANY(@types1) AND tags @> @tags1)
    OR
    -- Query Item 2
    (type = ANY(@types2) AND tags @> @tags2)
  )
  -- Tenant scoping (default)
  AND tenant_id = @tenantId
)
```

If this returns `true`, the append fails with a concurrency exception.

## API Syntax

### Tag Registration

**Fluent configuration in StoreOptions:**

```csharp
opts.Events.EnableDcb(); // opt-in, triggers schema addition

opts.Events.TagEvent<StudentSubscribedToCourse>(e => new[]
{
    $"student:{e.StudentId}",
    $"course:{e.CourseId}"
});

opts.Events.TagEvent<CourseCapacityChanged>(e => new[]
{
    $"course:{e.CourseId}"
});
```

**Interface on the event (alternative):**

```csharp
public record StudentSubscribedToCourse(Guid StudentId, Guid CourseId) : ITaggedEvent
{
    public IEnumerable<string> GetTags() => [$"student:{StudentId}", $"course:{CourseId}"];
}
```

### Condition Pattern

A "condition" is a first-class concept that encapsulates:
1. **Query**: What event types and tags to look for
2. **State**: Projecting matching events into a decision model
3. **Check**: Whether the append should proceed
4. **Enforcement**: Atomic validation during `SaveChangesAsync()`

```csharp
public class CourseSubscriptionCondition : AppendCondition
{
    public bool CourseExists { get; set; }
    public int Capacity { get; set; }
    public int Subscriptions { get; set; }

    // Define which events this condition queries
    public override void ConfigureQuery(DcbQueryBuilder query, Guid courseId, Guid studentId)
    {
        query
            .Match<CourseDefined>([$"course:{courseId}"])
            .Match<CourseCapacityChanged>([$"course:{courseId}"])
            .Match<StudentSubscribedToCourse>([$"course:{courseId}"])
            .Match<StudentSubscribedToCourse>([$"student:{studentId}"]);
    }

    // Build state from matching events
    public void Apply(CourseDefined e) => CourseExists = true;
    public void Apply(CourseCapacityChanged e) => Capacity = e.NewCapacity;
    public void Apply(StudentSubscribedToCourse e) => Subscriptions++;

    // Evaluate whether append is allowed
    public override bool CanAppend() =>
        CourseExists && Subscriptions < Capacity;
}
```

**Usage:**

```csharp
var condition = await session.Events
    .BuildCondition<CourseSubscriptionCondition>(courseId, studentId);

if (condition.CanAppend())
{
    session.Events.AppendWithCondition(
        streamId,
        condition,
        new StudentSubscribedToCourse(studentId, courseId)
    );
    await session.SaveChangesAsync();
    // ^ condition check + event insert in same transaction
    // throws concurrency exception if condition violated
}
```

### Backfill Tool

For existing events when enabling DCB or adding new tag definitions:

```csharp
await store.Events.BackfillTagsAsync(CancellationToken.None);
```

This reads events in batches, applies registered tag extractors, and updates the `tags` column.

## Architecture Split

### JasperFx.Events (portable)

- `ITaggedEvent` interface
- `AppendCondition` base class / condition model
- `DcbQueryBuilder` — query construction
- `IDcbQuery` / `DcbQueryItem` — query representation
- Tag extraction registration abstractions
- Apply method conventions for condition state

### Marten (PostgreSQL-specific)

- `EnableDcb()` opt-in configuration
- `tags TEXT[]` column addition to `EventsTable`
- GIN index creation
- SQL generation for conditional append check
- Integration with Rich and Quick append paths
- `BackfillTagsAsync()` migration tool
- Tenant scoping in condition queries

## DCB Spec Mapping

| DCB Spec Concept | Marten Implementation |
|---|---|
| Sequence Position | `seq_id` (existing global sequence) |
| Event Type | `type` column (existing) |
| Tags | `tags TEXT[]` column (new, opt-in) |
| Query | `DcbQueryBuilder` → SQL with `type = ANY(...)` and `tags @> ARRAY[...]` |
| Query Item (types OR, tags AND) | Single `WHERE` clause per item, items combined with `OR` |
| Append Condition `failIfEventsMatch` | `SELECT EXISTS(...)` check in `SaveChangesAsync()` transaction |
| Append Condition `after` position | `WHERE seq_id > @after` in the condition query |
| Atomic append | PostgreSQL transaction wrapping condition check + event INSERT |

```

### File: dcb-summary.md
```md
# Marten DCB Implementation Summary

## Shared Types (JasperFx.Events)
- **`EventTag`** — `readonly record struct(Type TagType, object Value)` stored on each event
- **`TagTypeRegistration`** — Wraps a strong-typed ID type (e.g. `StudentId(Guid Value)`) with `ValueTypeInfo`, `TableSuffix`, `SimpleType`, and optional `AggregateType`
- **`EventTagQuery`** — Builds OR'd conditions of `(EventType?, TagType, TagValue)` via fluent `Or<TTag>(value)` API
- **`IEvent.WithTag()`** — Extension methods to attach tags to events; uses `TagValueExtractor` (compiled lambdas) to unwrap inner values

## Schema & Registration
- **`EventGraph`** — Holds `List<TagTypeRegistration>`, exposes `RegisterTagType<T>()`, `FindTagType()`, `TagTypes`
- **`EventTagTable`** — One table per tag type: `mt_event_tag_{suffix}` with composite PK `(value, seq_id)`, FK to `mt_events.seq_id`. Value column type maps from SimpleType (Guid→uuid, string→text, int→integer, etc.)
- **`EventGraph.FeatureSchema`** — Yields `EventTagTable` instances in schema object generation

## Tag Insert Operations (3 paths)
1. **`InsertEventTagOperation`** — Rich mode: direct `INSERT (value, seq_id) VALUES (...)` using pre-assigned sequence
2. **`InsertEventTagByEventIdOperation`** — Quick mode fallback: `INSERT ... SELECT seq_id FROM mt_events WHERE id = @eventId` for individual insert paths (Start/ExpectedVersion)
3. **`QuickAppendEventFunction`** — Quick mode optimized: tag value arrays passed as `varchar[]` parameters to the PL/pgSQL function; tags inserted inline in the same loop using the already-available `seq` variable
- **`EventTagOperations`** — Static helper dispatching to `QueueTagOperations()` (Rich) or `QueueTagOperationsByEventId()` (Quick individual paths)

## Code Generation (Quick Append)
- **`EventDocumentStorageGenerator.buildQuickAppendOperation()`** — Conditionally emits `writeAllTagValues(parameterBuilder)` when `graph.TagTypes.Count > 0`
- **`QuickAppendEventsOperationBase.writeAllTagValues()`** — Builds parallel `string?[]` arrays per tag type from event tags, appends as `NpgsqlDbType.Array | Varchar`
- **`QuickEventAppender`** — Routes: function path skips separate tag ops (handled in-function); Start/ExpectedVersion paths queue `InsertEventTagByEventIdOperation`

## Query & Consistency
- **`EventStore.Dcb.cs`** — Session APIs: `QueryByTagsAsync()`, `AggregateByTagsAsync<T>()`, `FetchForWritingByTags<T>()`. Builds SQL with INNER JOINs to tag tables + OR'd WHERE conditions
- **`AssertDcbConsistency`** — `IStorageOperation` queued at fetch time, runs at `SaveChangesAsync`: `EXISTS` query checks for events with `seq_id > lastSeenSequence` matching the tag query. Throws `DcbConcurrencyException` if violated
- **`IEventBoundary<T>`** / **`EventBoundary<T>`** — Wraps query result: `Aggregate`, `Events`, `LastSeenSequence`. `AppendOne()`/`AppendMany()` route new events to streams by tag values
- **`FetchForWritingByTagsHandler<T>`** — `IQueryHandler` for batch query support; same SQL building + assertion registration

## Batch Querying
- **`IBatchEvents.FetchForWritingByTags<T>()`** — Interface on `IBatchedQuery`
- **`BatchedQuery.Events.cs`** — Delegates to `FetchForWritingByTagsHandler<T>` via `AddItem()`

## Key File Locations

### JasperFx.Events (shared)
| File | Purpose |
|------|---------|
| `JasperFx.Events/EventTag.cs` | Core tag value type |
| `JasperFx.Events/Tags/TagTypeRegistration.cs` | Tag type registration & value extraction |
| `JasperFx.Events/Tags/EventTagQuery.cs` | Query specification with OR'd conditions |
| `JasperFx.Events/IEvent.cs` | `WithTag()` extension methods |
| `JasperFx.Events/Event.cs` | Tag storage on event instances |

### Marten
| File | Purpose |
|------|---------|
| `Marten/Events/EventGraph.cs` | `RegisterTagType<T>()`, tag type list |
| `Marten/Events/EventGraph.FeatureSchema.cs` | Schema generation for tag tables |
| `Marten/Events/Schema/EventTagTable.cs` | Tag table DDL (per tag type) |
| `Marten/Events/Schema/QuickAppendEventFunction.cs` | PL/pgSQL function with inline tag inserts |
| `Marten/Events/Operations/InsertEventTagOperation.cs` | Rich mode tag insert |
| `Marten/Events/Operations/InsertEventTagByEventIdOperation.cs` | Quick mode tag insert (by event ID) |
| `Marten/Events/Operations/EventTagOperations.cs` | Static tag operation dispatcher |
| `Marten/Events/Operations/QuickAppendEventsOperationBase.cs` | `writeAllTagValues()` for function path |
| `Marten/Events/QuickEventAppender.cs` | Append routing (function vs individual) |
| `Marten/Events/CodeGeneration/EventDocumentStorageGenerator.cs` | Conditional tag codegen |
| `Marten/Events/EventStore.Dcb.cs` | Session-level DCB APIs |
| `Marten/Events/Dcb/IEventBoundary.cs` | Public boundary interface |
| `Marten/Events/Dcb/EventBoundary.cs` | Boundary implementation & event routing |
| `Marten/Events/Dcb/AssertDcbConsistency.cs` | Consistency check operation |
| `Marten/Events/Dcb/DcbConcurrencyException.cs` | Concurrency violation exception |
| `Marten/Events/Dcb/FetchForWritingByTagsHandler.cs` | Batch query handler |
| `Marten/Services/BatchQuerying/BatchedQuery.Events.cs` | Batch query integration |

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

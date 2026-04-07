---
id: projac
type: knowledge
owner: OA_Triage
---
# projac
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Projac

Projac is a set of .NET libraries that allow you to author projections targeting various backing stores and is easy to  integrate with existing event stores such as [EventStore](http://www.eventstore.org) and [SQLStreamStore](https://github.com/SQLStreamStore). [![Join the chat at https://gitter.im/yreynhout/Projac](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/yreynhout/Projac?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

- [Projac](https://github.com/BitTacklr/Projac/wiki/projac) allows you to author projections that target any store for which you can bring your own connection (e.g [Redis](http://redis.io), [RavenDB](http://ravendb.net/), [Elasticsearch](http://http://www.elasticsearch.org/), [Microsoft Windows Azure Table Storage](http://azure.microsoft.com/en-us/documentation/services/storage/)). 

- [Projac.Sql, Projac.SqlClient and Projac.SQLite](https://github.com/BitTacklr/Projac/wiki/projac.sql) allow you to author projections that target relational databases. Projac.Sql contains common abstractions across all database providers that use the ADO.NET model. Projac.SqlClient targets [Microsoft SQL Server](http://www.microsoft.com/en-us/server-cloud/products/sql-server-editions/overview.aspx). Projac.SQLite targets [SQLite](http://sqlite.org). We welcome contributions for other database providers that follow a similar recipe.

It's available on both NuGet & MyGet:

- Projac: [NuGet](https://www.nuget.org/packages/Projac/) - [MyGet](https://www.myget.org/feed/projac/package/nuget/Projac)
- Projac.Sql: [NuGet](https://www.nuget.org/packages/Projac,Sql/) - [MyGet](https://www.myget.org/feed/projac/package/nuget/Projac.Sql)
- Projac.SqlClient: [NuGet](https://www.nuget.org/packages/Projac.SqlClient/) - [MyGet](https://www.myget.org/feed/projac/package/nuget/Projac.SqlClient)
- [WIP] Projac.SQLite: [NuGet](https://www.nuget.org/packages/Projac,SQLite/) - [MyGet](https://www.myget.org/feed/projac/package/nuget/Projac.SQLite)

The custom MyGet feed can be found [here](https://www.myget.org/F/projac/api/v3/index.json).

---

**Important Changes**

If you're using a version prior to 0.1.0, not only has your cheese been moved, it probably has been broken in unexpected places. Please check out the [changes made in 0.1.0](https://github.com/BitTacklr/Projac/wiki/Changes0.1.0) as well as the [how do I upgrade to 0.1.0 guide](https://github.com/BitTacklr/Projac/wiki/UpgradeTo0.1.0). If you want to keep your cheese as is, you can always fork this code base and use the `legacy` branch.

---

# Contributions

* Date, DateTime, DateTime2, Money data types in TSql by [@xt0rted](https://github.com/xt0rted)
* The ``positional syntax`` suggestion by [@tojans](https://github.com/tojans).
* Decimal data type in SqlClientSyntax by [@ritasker](https://github.com/ritasker)

```

### File: build.ps1
```ps1
[CmdLetBinding()]
param(
    [Parameter(Mandatory=$false)][string]$NugetApiKey="",
    [Parameter(Mandatory=$false)][string]$MygetApiKey=""
)

# terminate upon any error encountered
$ErrorActionPreference="Stop"

function Say($message)
{
    Write-Host $message -foreground "Blue"
}

Say "nuget-apikey: $NugetApiKey"
Say "myget-apikey: $MygetApiKey"

# install .net core sdk
Say "dotnet-install: installing .net core 2.0 sdk"
.\build\dotnet-install.ps1 -Channel "2.0"
$DotNetVersion = dotnet --version
Say "dotnet-version: running on $DotNetVersion"

# restore and run tooling
Say "dotnet-restore: installing tools"
dotnet restore .\build\tools.csproj --packages .\build\tools --no-dependencies
if($Error.Count -ne 0 -or $LastExitCode -eq 0) {
    Say "gitversion: detecting semantic version"
    $MajorMinorPatch = .\build\tools\gitversion.commandline\3.6.5\tools\GitVersion.exe /output json /showvariable MajorMinorPatch
    $InformationalVersion = .\build\tools\gitversion.commandline\3.6.5\tools\GitVersion.exe /output json /showvariable InformationalVersion
    Say "gitversion: Major.Minor.Patch=$MajorMinorPatch"
    Say "gitversion: InformationalVersion=$InformationalVersion"

    # build, test, pack and push
    Say "dotnet-build: building solution"
    dotnet build .\src\All.sln --configuration Release /p:AssemblyVersion=$MajorMinorPatch /p:FileVersion=$MajorMinorPatch /p:InformationalVersion=$InformationalVersion /p:PackageVersion=$MajorMinorPatch
    if($Error.Count -ne 0 -or $LastExitCode -eq 0) {
        Push-Location
        Set-Location -Path .\src\Projac.Tests
        Say "dotnet-test: running tests"
        dotnet test --no-build --configuration Release
        Set-Location -Path ..\Projac.Sql.Tests
        Say "dotnet-test: running sql tests"
        dotnet test --no-build --configuration Release
        Set-Location -Path ..\Projac.SqlClient.Tests
        Say "dotnet-test: running sqlclient tests"
        dotnet test --no-build --configuration Release
        Set-Location -Path ..\Projac.SQLite.Tests
        Say "dotnet-test: running sqlite tests"
        dotnet test --no-build --configuration Release
        if($Error.Count -ne 0 -or $LastExitCode -eq 0) {
            Pop-Location
            Say "dotnet-pack: packaging"
            dotnet pack .\src\All.sln --no-build --configuration Release /p:AssemblyVersion=$MajorMinorPatch /p:FileVersion=$MajorMinorPatch /p:InformationalVersion=$InformationalVersion /p:PackageVersion=$MajorMinorPatch
            if($LastExitCode -eq 0) {
                if ($NugetApiKey -ne "") {
                    Say "dotnet-nuget-push: pushing projac package to nuget"
                    dotnet nuget push .\src\Projac\bin\Release\Projac.$MajorMinorPatch.nupkg --source https://www.nuget.org/api/v2/package --api-key $NugetApiKey
                    Say "dotnet-nuget-push: pushing projac.sql package to nuget"
                    dotnet nuget push .\src\Projac.Sql\bin\Release\Projac.Sql.$MajorMinorPatch.nupkg --source https://www.nuget.org/api/v2/package --api-key $NugetApiKey
                    Say "dotnet-nuget-push: pushing projac.sqlclient package to nuget"
                    dotnet nuget push .\src\Projac.SqlClient\bin\Release\Projac.SqlClient.$MajorMinorPatch.nupkg --source https://www.nuget.org/api/v2/package --api-key $NugetApiKey
                    Say "dotnet-nuget-push: pushing projac.sqlite package to nuget"
                    dotnet nuget push .\src\Projac.SQLite\bin\Release\Projac.SQLite.$MajorMinorPatch.nupkg --source https://www.nuget.org/api/v2/package --api-key $NugetApiKey
                }
                if ($MygetApiKey -ne "") {
                    Say "dotnet-nuget-push: pushing projac package to myget"
                    dotnet nuget push .\src\Projac\bin\Release\Projac.$MajorMinorPatch.nupkg --source https://www.myget.org/F/projac/api/v2/package --api-key $MygetApiKey
                    Say "dotnet-nuget-push: pushing projac.sql package to myget"
                    dotnet nuget push .\src\Projac.Sql\bin\Release\Projac.Sql.$MajorMinorPatch.nupkg --source https://www.myget.org/F/projac/api/v2/package --api-key $MygetApiKey
                    Say "dotnet-nuget-push: pushing projac.sqlclient package to myget"
                    dotnet nuget push .\src\Projac.SqlClient\bin\Release\Projac.SqlClient.$MajorMinorPatch.nupkg --source https://www.myget.org/F/projac/api/v2/package --api-key $MygetApiKey
                    Say "dotnet-nuget-push: pushing projac.sqlite package to myget"
                    dotnet nuget push .\src\Projac.SQLite\bin\Release\Projac.SQLite.$MajorMinorPatch.nupkg --source https://www.myget.org/F/projac/api/v2/package --api-key $MygetApiKey
                }
            }
        } else {
            Pop-Location
        }
    }
}
```

### File: build.sh
```sh
#!/usr/bin/env bash

# Parameters
# $1 = NugetApiKey
NugetApiKey=$1
# $2 = MygetApiKey
MygetApiKey=$2

# standard output may be used as a return value in the functions
# we need a way to write text on the screen in the functions so that
# it won't interfere with the return value.
# Exposing stream 3 as a pipe to standard output of the script itself
exec 3>&1

# Setup some colors to use. These need to work in fairly limited shells, like the Ubuntu Docker container where there are only 8 colors.
# See if stdout is a terminal
if [ -t 1 ]; then
    # see if it supports colors
    ncolors=$(tput colors)
    if [ -n "$ncolors" ] && [ $ncolors -ge 8 ]; then
        bold="$(tput bold       || echo)"
        normal="$(tput sgr0     || echo)"
        black="$(tput setaf 0   || echo)"
        red="$(tput setaf 1     || echo)"
        green="$(tput setaf 2   || echo)"
        yellow="$(tput setaf 3  || echo)"
        blue="$(tput setaf 4    || echo)"
        magenta="$(tput setaf 5 || echo)"
        cyan="$(tput setaf 6    || echo)"
        white="$(tput setaf 7   || echo)"
    fi
fi

say_err() {
    printf "%b/n" "${red:-}dotnet_install: Error: $1${normal:-}" >&2
}

say() {
    # using stream 3 (defined in the beginning) to not interfere with stdout of functions
    # which may be used as return value
    printf "%b\n" "${cyan:-}$1${normal:-}" >&3
}

say_verbose() {
    if [ "$verbose" = true ]; then
        say "$1"
    fi
}

# install .net core sdk
say "dotnet-install: installing .net core 2.0 sdk"
./build/dotnet-install.sh -channel "2.0"
DotNetVersion=$(dotnet --version)
say "dotnet-version: running on $DotNetVersion"

# restore and run tooling
say "dotnet-restore: installing tools"
dotnet restore ./build/tools.csproj --packages ./build/tools --no-dependencies

say "gitversion: detecting semantic version"
MajorMinorPatch=$(./build/tools/gitversion.commandline/3.6.5/tools/GitVersion.exe /output json /showvariable MajorMinorPatch)
InformationalVersion=$(./build/tools/gitversion.commandline/3.6.5/tools/GitVersion.exe /output json /showvariable InformationalVersion)
say "gitversion: Major.Minor.Patch=$MajorMinorPatch"
say "gitversion: InformationalVersion=$InformationalVersion"

# build
say "dotnet-build: building Projac"
dotnet build ./src/Projac/Projac.csproj --configuration Release /p:AssemblyVersion=$MajorMinorPatch /p:FileVersion=$MajorMinorPatch /p:InformationalVersion=$InformationalVersion /p:PackageVersion=$MajorMinorPatch
say "dotnet-build: building Projac.Sql"
dotnet build ./src/Projac.Sql/Projac.Sql.csproj --configuration Release /p:AssemblyVersion=$MajorMinorPatch /p:FileVersion=$MajorMinorPatch /p:InformationalVersion=$InformationalVersion /p:PackageVersion=$MajorMinorPatch
say "dotnet-build: building Projac.SqlClient"
dotnet build ./src/Projac.SqlClient/Projac.SqlClient.csproj --configuration Release /p:AssemblyVersion=$MajorMinorPatch /p:FileVersion=$MajorMinorPatch /p:InformationalVersion=$InformationalVersion /p:PackageVersion=$MajorMinorPatch

say "dotnet-build: building Projac.Tests"
dotnet build ./src/Projac.Tests/Projac.Tests.csproj --configuration Release /p:AssemblyVersion=$MajorMinorPatch /p:FileVersion=$MajorMinorPatch /p:InformationalVersion=$InformationalVersion /p:PackageVersion=$MajorMinorPatch
say "dotnet-build: building Projac.Sql.Tests"
dotnet build ./src/Projac.Sql.Tests/Projac.Sql.Tests.csproj --configuration Release /p:AssemblyVersion=$MajorMinorPatch /p:FileVersion=$MajorMinorPatch /p:InformationalVersion=$InformationalVersion /p:PackageVersion=$MajorMinorPatch
say "dotnet-build: building Projac.SqlClient.Tests"
dotnet build ./src/Projac.SqlClient.Tests/Projac.SqlClient.Tests.csproj --configuration Release /p:AssemblyVersion=$MajorMinorPatch /p:FileVersion=$MajorMinorPatch /p:InformationalVersion=$InformationalVersion /p:PackageVersion=$MajorMinorPatch

# test
say "dotnet-xunit: running tests"
cd ./src/Projac.Tests
dotnet test --no-build --configuration Release
cd ../..
cd ./src/Projac.Sql.Tests
dotnet test --no-build --configuration Release
cd ../..
cd ./src/Projac.SqlClient.Tests
dotnet test --no-build --configuration Release
cd ../..

# package
say "dotnet-pack: packaging"
dotnet pack ./src/Projac/Projac.csproj --no-build --configuration Release /p:AssemblyVersion=$MajorMinorPatch /p:FileVersion=$MajorMinorPatch /p:InformationalVersion=$InformationalVersion /p:PackageVersion=$MajorMinorPatch
dotnet pack ./src/Projac.Sql/Projac.Sql.csproj --no-build --configuration Release /p:AssemblyVersion=$MajorMinorPatch /p:FileVersion=$MajorMinorPatch /p:InformationalVersion=$InformationalVersion /p:PackageVersion=$MajorMinorPatch
dotnet pack ./src/Projac.SqlClient/Projac.SqlClient.csproj --no-build --configuration Release /p:AssemblyVersion=$MajorMinorPatch /p:FileVersion=$MajorMinorPatch /p:InformationalVersion=$InformationalVersion /p:PackageVersion=$MajorMinorPatch

# push
if [ "$NugetApiKey" != "" ]; then
    say "dotnet-nuget-push: pushing Projac package to nuget"
    dotnet nuget push ./src/Projac/bin/Release/Projac.$MajorMinorPatch.nupkg --source https://www.nuget.org/api/v2/package --api-key $NugetApiKey
    say "dotnet-nuget-push: pushing Projac.Sql package to nuget"
    dotnet nuget push ./src/Projac.Sql/bin/Release/Projac.Sql.$MajorMinorPatch.nupkg --source https://www.nuget.org/api/v2/package --api-key $NugetApiKey
    say "dotnet-nuget-push: pushing Projac.SqlClient package to nuget"
    dotnet nuget push ./src/Projac.SqlClient/bin/Release/Projac.SqlClient.$MajorMinorPatch.nupkg --source https://www.nuget.org/api/v2/package --api-key $NugetApiKey
fi

if [ "$MygetApiKey" != "" ]; then
    say "dotnet-nuget-push: pushing Projac package to myget"
    dotnet nuget push ./src/Projac/bin/Release/Projac.$MajorMinorPatch.nupkg --source https://www.myget.org/F/projac/api/v2/package --api-key $MygetApiKey
    say "dotnet-nuget-push: pushing Projac.Sql package to nuget"
    dotnet nuget push ./src/Projac.Sql/bin/Release/Projac.Sql.$MajorMinorPatch.nupkg --source https://www.myget.org/F/projac/api/v2/package --api-key $MygetApiKey
    say "dotnet-nuget-push: pushing Projac.SqlClient package to nuget"
    dotnet nuget push ./src/Projac.SqlClient/bin/Release/Projac.SqlClient.$MajorMinorPatch.nupkg --source https://www.myget.org/F/projac/api/v2/package --api-key $MygetApiKey
fi
```

### File: global.json
```json
{
    "sdk": {
        "version": "2.0.2"
    }
}
```

### File: LICENSE.txt
```txt
BSD 3-Clause License
====================

Copyright (c) 2013, Yves Reynhout
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
Neither the name of the BitTacklr nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```


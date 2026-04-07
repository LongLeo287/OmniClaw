---
id: xer
type: knowledge
owner: OA_Triage
---
# xer
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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
                    
    * Attribute registration
      * achieved by marking methods with [CommandHandler] or [EventHandler] attributes from the Xer.Cqrs.CommandStack.Extensions.Attributes and Xer.Cqrs.EventStack.Extensions.Attributes packages.
      
        * Xer.Cqrs.CommandStack.Extensions.Attributes
          
          [![NuGet](https://img.shields.io/nuget/v/Xer.Cqrs.CommandStack.Extensions.Attributes.svg)](https://www.nuget.org/packages/Xer.Cqrs.CommandStack.Extensions.Attributes/)
          
          See https://github.com/XerProjects/Xer.Cqrs.CommandStack.Extensions.Attributes/ for source.
        
        * Xer.Cqrs.EventStack.Extensions.Attributes
          
          [![NuGet](https://img.shields.io/nuget/v/Xer.Cqrs.EventStack.Extensions.Attributes.svg)](https://www.nuget.org/packages/Xer.Cqrs.EventStack.Extensions.Attributes/)
         
          See https://github.com/XerProjects/Xer.Cqrs.EventStack.Extensions.Attributes/ for source.

## Installation
You can simply clone this repository, build the source, reference the dll from the project, and code away!

Xer.Cqrs is available as a Nuget package:
* [![NuGet](https://img.shields.io/nuget/v/Xer.Cqrs.svg)](https://www.nuget.org/packages/Xer.Cqrs/)

To install Nuget package:
1. Open command prompt
2. Go to project directory
3. Add the packages to the project:
    ```csharp
    dotnet add package Xer.Cqrs
    ```
4. Restore the packages:
    ```csharp
    dotnet restore
    ```

## Getting Started
(Samples are in ASP.NET Core)

### Command Handling
See https://github.com/XerProjects/Xer.Cqrs.CommandStack/blob/dev/README.md for documentation.

### Event Handling
See https://github.com/XerProjects/Xer.Cqrs.EventStack/blob/dev/README.md for documentation.

```

### File: build.ps1
```ps1
##########################################################################
# This is the Cake bootstrapper script for PowerShell.
# This file was downloaded from https://github.com/cake-build/resources
# Feel free to change this file to fit your needs.
##########################################################################

<#

.SYNOPSIS
This is a Powershell script to bootstrap a Cake build.

.DESCRIPTION
This Powershell script will download NuGet if missing, restore NuGet tools (including Cake)
and execute your Cake build script with the parameters you provide.

.PARAMETER Script
The build script to execute.
.PARAMETER Target
The build script target to run.
.PARAMETER Configuration
The build configuration to use.
.PARAMETER Verbosity
Specifies the amount of information to be displayed.
.PARAMETER ShowDescription
Shows description about tasks.
.PARAMETER DryRun
Performs a dry run.
.PARAMETER Experimental
Uses the nightly builds of the Roslyn script engine.
.PARAMETER Mono
Uses the Mono Compiler rather than the Roslyn script engine.
.PARAMETER SkipToolPackageRestore
Skips restoring of packages.
.PARAMETER ScriptArgs
Remaining arguments are added here.

.LINK
https://cakebuild.net

#>

[CmdletBinding()]
Param(
    [string]$Script = "build.cake",
    [string]$Target,
    [string]$Configuration,
    [ValidateSet("Quiet", "Minimal", "Normal", "Verbose", "Diagnostic")]
    [string]$Verbosity,
    [switch]$ShowDescription,
    [Alias("WhatIf", "Noop")]
    [switch]$DryRun,
    [switch]$Experimental,
    [switch]$Mono,
    [switch]$SkipToolPackageRestore,
    [Parameter(Position=0,Mandatory=$false,ValueFromRemainingArguments=$true)]
    [string[]]$ScriptArgs
)

[Reflection.Assembly]::LoadWithPartialName("System.Security") | Out-Null
function MD5HashFile([string] $filePath)
{
    if ([string]::IsNullOrEmpty($filePath) -or !(Test-Path $filePath -PathType Leaf))
    {
        return $null
    }

    [System.IO.Stream] $file = $null;
    [System.Security.Cryptography.MD5] $md5 = $null;
    try
    {
        $md5 = [System.Security.Cryptography.MD5]::Create()
        $file = [System.IO.File]::OpenRead($filePath)
        return [System.BitConverter]::ToString($md5.ComputeHash($file))
    }
    finally
    {
        if ($file -ne $null)
        {
            $file.Dispose()
        }
    }
}

function GetProxyEnabledWebClient
{
    $wc = New-Object System.Net.WebClient
    $proxy = [System.Net.WebRequest]::GetSystemWebProxy()
    $proxy.Credentials = [System.Net.CredentialCache]::DefaultCredentials        
    $wc.Proxy = $proxy
    return $wc
}

Write-Host "Preparing to run build script..."

if(!$PSScriptRoot){
    $PSScriptRoot = Split-Path $MyInvocation.MyCommand.Path -Parent
}

$TOOLS_DIR = Join-Path $PSScriptRoot "tools"
$ADDINS_DIR = Join-Path $TOOLS_DIR "Addins"
$MODULES_DIR = Join-Path $TOOLS_DIR "Modules"
$NUGET_EXE = Join-Path $TOOLS_DIR "nuget.exe"
$CAKE_EXE = Join-Path $TOOLS_DIR "Cake/Cake.exe"
$NUGET_URL = "https://dist.nuget.org/win-x86-commandline/latest/nuget.exe"
$PACKAGES_CONFIG = Join-Path $TOOLS_DIR "packages.config"
$PACKAGES_CONFIG_MD5 = Join-Path $TOOLS_DIR "packages.config.md5sum"
$ADDINS_PACKAGES_CONFIG = Join-Path $ADDINS_DIR "packages.config"
$MODULES_PACKAGES_CONFIG = Join-Path $MODULES_DIR "packages.config"

# Make sure tools folder exists
if ((Test-Path $PSScriptRoot) -and !(Test-Path $TOOLS_DIR)) {
    Write-Verbose -Message "Creating tools directory..."
    New-Item -Path $TOOLS_DIR -Type directory | out-null
}

# Make sure that packages.config exist.
if (!(Test-Path $PACKAGES_CONFIG)) {
    Write-Verbose -Message "Downloading packages.config..."    
    try {        
        $wc = GetProxyEnabledWebClient
        $wc.DownloadFile("https://cakebuild.net/download/bootstrapper/packages", $PACKAGES_CONFIG) } catch {
        Throw "Could not download packages.config."
    }
}

# Try find NuGet.exe in path if not exists
if (!(Test-Path $NUGET_EXE)) {
    Write-Verbose -Message "Trying to find nuget.exe in PATH..."
    $existingPaths = $Env:Path -Split ';' | Where-Object { (![string]::IsNullOrEmpty($_)) -and (Test-Path $_ -PathType Container) }
    $NUGET_EXE_IN_PATH = Get-ChildItem -Path $existingPaths -Filter "nuget.exe" | Select -First 1
    if ($NUGET_EXE_IN_PATH -ne $null -and (Test-Path $NUGET_EXE_IN_PATH.FullName)) {
        Write-Verbose -Message "Found in PATH at $($NUGET_EXE_IN_PATH.FullName)."
        $NUGET_EXE = $NUGET_EXE_IN_PATH.FullName
    }
}

# Try download NuGet.exe if not exists
if (!(Test-Path $NUGET_EXE)) {
    Write-Verbose -Message "Downloading NuGet.exe..."
    try {
        $wc = GetProxyEnabledWebClient
        $wc.DownloadFile($NUGET_URL, $NUGET_EXE)
    } catch {
        Throw "Could not download NuGet.exe."
    }
}

# Save nuget.exe path to environment to be available to child processed
$ENV:NUGET_EXE = $NUGET_EXE

# Restore tools from NuGet?
if(-Not $SkipToolPackageRestore.IsPresent) {
    Push-Location
    Set-Location $TOOLS_DIR

    # Check for changes in packages.config and remove installed tools if true.
    [string] $md5Hash = MD5HashFile($PACKAGES_CONFIG)
    if((!(Test-Path $PACKAGES_CONFIG_MD5)) -Or
      ($md5Hash -ne (Get-Content $PACKAGES_CONFIG_MD5 ))) {
        Write-Verbose -Message "Missing or changed package.config hash..."
        Get-ChildItem -Exclude packages.config,nuget.exe,Cake.Bakery |
        Remove-Item -Recurse
    }

    Write-Verbose -Message "Restoring tools from NuGet..."
    $NuGetOutput = Invoke-Expression "&`"$NUGET_EXE`" install -ExcludeVersion -OutputDirectory `"$TOOLS_DIR`""

    if ($LASTEXITCODE -ne 0) {
        Throw "An error occurred while restoring NuGet tools."
    }
    else
    {
        $md5Hash | Out-File $PACKAGES_CONFIG_MD5 -Encoding "ASCII"
    }
    Write-Verbose -Message ($NuGetOutput | out-string)

    Pop-Location
}

# Restore addins from NuGet
if (Test-Path $ADDINS_PACKAGES_CONFIG) {
    Push-Location
    Set-Location $ADDINS_DIR

    Write-Verbose -Message "Restoring addins from NuGet..."
    $NuGetOutput = Invoke-Expression "&`"$NUGET_EXE`" install -ExcludeVersion -OutputDirectory `"$ADDINS_DIR`""

    if ($LASTEXITCODE -ne 0) {
        Throw "An error occurred while restoring NuGet addins."
    }

    Write-Verbose -Message ($NuGetOutput | out-string)

    Pop-Location
}

# Restore modules from NuGet
if (Test-Path $MODULES_PACKAGES_CONFIG) {
    Push-Location
    Set-Location $MODULES_DIR

    Write-Verbose -Message "Restoring modules from NuGet..."
    $NuGetOutput = Invoke-Expression "&`"$NUGET_EXE`" install -ExcludeVersion -OutputDirectory `"$MODULES_DIR`""

    if ($LASTEXITCODE -ne 0) {
        Throw "An error occurred while restoring NuGet modules."
    }

    Write-Verbose -Message ($NuGetOutput | out-string)

    Pop-Location
}

# Make sure that Cake has been installed.
if (!(Test-Path $CAKE_EXE)) {
    Throw "Could not find Cake.exe at $CAKE_EXE"
}



# Build Cake arguments
$cakeArguments = @("$Script");
if ($Target) { $cakeArguments += "-target=$Target" }
if ($Configuration) { $cakeArguments += "-configuration=$Configuration" }
if ($Verbosity) { $cakeArguments += "-verbosity=$Verbosity" }
if ($ShowDescription) { $cakeArguments += "-showdescription" }
if ($DryRun) { $cakeArguments += "-dryrun" }
if ($Experimental) { $cakeArguments += "-experimental" }
if ($Mono) { $cakeArguments += "-mono" }
$cakeArguments += $ScriptArgs

# Start Cake
Write-Host "Running build script..."
&$CAKE_EXE $cakeArguments
exit $LASTEXITCODE

```

### File: build.sh
```sh
#!/usr/bin/env bash

##########################################################################
# This is the Cake bootstrapper script for Linux and OS X.
# This file was downloaded from https://github.com/cake-build/resources
# Feel free to change this file to fit your needs.
##########################################################################

# Define directories.
SCRIPT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
TOOLS_DIR=$SCRIPT_DIR/tools
ADDINS_DIR=$TOOLS_DIR/Addins
MODULES_DIR=$TOOLS_DIR/Modules
NUGET_EXE=$TOOLS_DIR/nuget.exe
CAKE_EXE=$TOOLS_DIR/Cake/Cake.exe
PACKAGES_CONFIG=$TOOLS_DIR/packages.config
PACKAGES_CONFIG_MD5=$TOOLS_DIR/packages.config.md5sum
ADDINS_PACKAGES_CONFIG=$ADDINS_DIR/packages.config
MODULES_PACKAGES_CONFIG=$MODULES_DIR/packages.config

# Define md5sum or md5 depending on Linux/OSX
MD5_EXE=
if [[ "$(uname -s)" == "Darwin" ]]; then
    MD5_EXE="md5 -r"
else
    MD5_EXE="md5sum"
fi

# Define default arguments.
SCRIPT="build.cake"
CAKE_ARGUMENTS=()

# Parse arguments.
for i in "$@"; do
    case $1 in
        -s|--script) SCRIPT="$2"; shift ;;
        --) shift; CAKE_ARGUMENTS+=("$@"); break ;;
        *) CAKE_ARGUMENTS+=("$1") ;;
    esac
    shift
done

# Make sure the tools folder exist.
if [ ! -d "$TOOLS_DIR" ]; then
  mkdir "$TOOLS_DIR"
fi

# Make sure that packages.config exist.
if [ ! -f "$TOOLS_DIR/packages.config" ]; then
    echo "Downloading packages.config..."
    curl -Lsfo "$TOOLS_DIR/packages.config" https://cakebuild.net/download/bootstrapper/packages
    if [ $? -ne 0 ]; then
        echo "An error occurred while downloading packages.config."
        exit 1
    fi
fi

# Download NuGet if it does not exist.
if [ ! -f "$NUGET_EXE" ]; then
    echo "Downloading NuGet..."
    curl -Lsfo "$NUGET_EXE" https://dist.nuget.org/win-x86-commandline/latest/nuget.exe
    if [ $? -ne 0 ]; then
        echo "An error occurred while downloading nuget.exe."
        exit 1
    fi
fi

# Restore tools from NuGet.
pushd "$TOOLS_DIR" >/dev/null
if [ ! -f "$PACKAGES_CONFIG_MD5" ] || [ "$( cat "$PACKAGES_CONFIG_MD5" | sed 's/\r$//' )" != "$( $MD5_EXE "$PACKAGES_CONFIG" | awk '{ print $1 }' )" ]; then
    find . -type d ! -name . ! -name 'Cake.Bakery' | xargs rm -rf
fi

mono "$NUGET_EXE" install -ExcludeVersion
if [ $? -ne 0 ]; then
    echo "Could not restore NuGet tools."
    exit 1
fi

$MD5_EXE "$PACKAGES_CONFIG" | awk '{ print $1 }' >| "$PACKAGES_CONFIG_MD5"

popd >/dev/null

# Restore addins from NuGet.
if [ -f "$ADDINS_PACKAGES_CONFIG" ]; then
    pushd "$ADDINS_DIR" >/dev/null

    mono "$NUGET_EXE" install -ExcludeVersion
    if [ $? -ne 0 ]; then
        echo "Could not restore NuGet addins."
        exit 1
    fi

    popd >/dev/null
fi

# Restore modules from NuGet.
if [ -f "$MODULES_PACKAGES_CONFIG" ]; then
    pushd "$MODULES_DIR" >/dev/null

    mono "$NUGET_EXE" install -ExcludeVersion
    if [ $? -ne 0 ]; then
        echo "Could not restore NuGet modules."
        exit 1
    fi

    popd >/dev/null
fi

# Make sure that Cake has been installed.
if [ ! -f "$CAKE_EXE" ]; then
    echo "Could not find Cake.exe at '$CAKE_EXE'."
    exit 1
fi

# Start Cake
exec mono "$CAKE_EXE" $SCRIPT "${CAKE_ARGUMENTS[@]}"

```

### File: Samples\Domain\Product.cs
```cs
using System;
using System.Collections.Generic;
using Domain.DomainEvents;
using Xer.DomainDriven;

namespace Domain
{
    public class Product : AggregateRoot
    {
        public string Name { get; private set; }
        public bool IsActive { get; private set; }

        public Product(Guid id, string name)
            : base(id)
        {
            RegisterDomainEventAppliers();

            ApplyDomainEvent(new ProductRegisteredEvent(id, name));
        }
        
        public void Activate()
        {
            ApplyDomainEvent(new ProductActivatedEvent(Id));
        }

        public void Deactivate()
        {
            ApplyDomainEvent(new ProductDeactivatedEvent(Id));
        }

        private void RegisterDomainEventAppliers()
        {
            RegisterDomainEventApplier<ProductRegisteredEvent>(OnProductRegisteredEvent);
            RegisterDomainEventApplier<ProductActivatedEvent>(OnProductActivatedEvent);
            RegisterDomainEventApplier<ProductDeactivatedEvent>(OnProductDeactivatedEvent);
        }

        private void OnProductRegisteredEvent(ProductRegisteredEvent domainEvent)
        {
            Name = domainEvent.ProductName;
        }

        private void OnProductActivatedEvent(ProductActivatedEvent domainEvent)
        {
            IsActive = true;
        }

        private void OnProductDeactivatedEvent(ProductDeactivatedEvent domainEvent)
        {
            IsActive = false;
        }
    }
}
```

### File: Samples\Domain\Commands\ActivateProductCommand.cs
```cs
using System;
using System.Threading;
using System.Threading.Tasks;
using Domain.Exceptions;
using Xer.Cqrs.CommandStack;
using Xer.DomainDriven.Repositories;
// using Xer.Cqrs.CommandStack.Attributes;

namespace Domain.Commands
{
    public class ActivateProductCommand
    {
        public Guid ProductId { get; }

        public ActivateProductCommand(Guid productId) 
        {
            ProductId = productId; 
        }
    }

    /// <summary>
    /// This handler can be registered either through Container, Basic or Attribute registration.
    /// In real projects, implementing only one of the interfaces or only using the [CommandHandler] attribute should do.
    /// </summary>
    public class ActivateProductCommandHandler : ICommandAsyncHandler<ActivateProductCommand>
    {
        private readonly IAggregateRootRepository<Product> _productRepository;

        public ActivateProductCommandHandler(IAggregateRootRepository<Product> productRepository)
        {
            _productRepository = productRepository;
        }
        
        // [CommandHandler] // To allow this method to be registered through attribute registration.
        public async Task HandleAsync(ActivateProductCommand command, CancellationToken cancellationToken = default(CancellationToken))
        {
            Product product = await _productRepository.GetByIdAsync(command.ProductId);
            if (product == null)
            {
                throw new ProductNotFoundException("Product not found.");
            }

            product.Activate();

            await _productRepository.SaveAsync(product);
        }
    }
}
```

### File: Samples\Domain\Commands\DeactivateProductCommand.cs
```cs
using System;
using System.Threading;
using System.Threading.Tasks;
using Domain.Exceptions;
using Xer.Cqrs.CommandStack;
using Xer.DomainDriven.Repositories;
// using Xer.Cqrs.CommandStack.Attributes;

namespace Domain.Commands
{
    public class DeactivateProductCommand
    {
        public Guid ProductId { get; }

        public DeactivateProductCommand(Guid productId) 
        {
            ProductId = productId; 
        }        
    }

    /// <summary>
    /// This handler can be registered either through Container, Basic or Attribute registration.
    /// In real projects, implementing only one of the interfaces or only using the [CommandHandler] attribute should do.
    /// </summary>
    public class DeactivateProductCommandHandler : ICommandAsyncHandler<DeactivateProductCommand>
    {
        private readonly IAggregateRootRepository<Product> _productRepository;

        public DeactivateProductCommandHandler(IAggregateRootRepository<Product> productRepository)
        {
            _productRepository = productRepository;
        }

        // [CommandHandler] // To allow this method to be registered through attribute registration.
        public async Task HandleAsync(DeactivateProductCommand command, CancellationToken cancellationToken = default(CancellationToken))
        {
            Product product = await _productRepository.GetByIdAsync(command.ProductId);
            if (product == null)
            {
                throw new ProductNotFoundException("Product not found.");
            }

            product.Deactivate();

            await _productRepository.SaveAsync(product);
        }
    }
}
```

### File: Samples\Domain\Commands\RegisterProductCommand.cs
```cs
using System;
using System.Threading;
using System.Threading.Tasks;
using Xer.Cqrs.CommandStack;
using Xer.DomainDriven.Repositories;
// using Xer.Cqrs.CommandStack.Attributes;

namespace Domain.Commands
{
    public class RegisterProductCommand
    {
        public Guid ProductId { get; }
        public string ProductName { get; }
        
        public RegisterProductCommand(Guid productId, string productName) 
        {
            ProductId = productId;
            ProductName = productName;
        }
    }

    /// <summary>
    /// This handler can be registered either through Container, Basic or Attribute registration.
    /// In real projects, implementing only one of the interfaces or only using the [CommandHandler] attribute should do.
    /// </summary>
    public class RegisterProductCommandHandler : ICommandAsyncHandler<RegisterProductCommand>
    {
        private readonly IAggregateRootRepository<Product> _productRepository;

        public RegisterProductCommandHandler(IAggregateRootRepository<Product> productRepository)
        {
            _productRepository = productRepository;
        }

        // [CommandHandler] // To allow this method to be registered through attribute registration.
        public Task HandleAsync(RegisterProductCommand command, CancellationToken cancellationToken = default(CancellationToken))
        {
            return _productRepository.SaveAsync(new Product(command.ProductId, command.ProductName));
        }
    }
}
```

### File: Samples\Domain\Exceptions\ProductNotFoundException.cs
```cs
using System;
using Xer.DomainDriven.Exceptions;

namespace Domain.Exceptions
{
    public class ProductNotFoundException : AggregateRootNotFoundException
    {
        public ProductNotFoundException(string message) : base(message)
        {
        }

        public ProductNotFoundException(string message, Exception innerException) : base(message, innerException)
        {
        }
    }
}
```


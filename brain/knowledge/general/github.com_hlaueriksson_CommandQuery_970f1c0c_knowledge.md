---
id: github.com-hlaueriksson-commandquery-970f1c0c-know
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:07.445215
---

# KNOWLEDGE EXTRACT: github.com_hlaueriksson_CommandQuery_970f1c0c
> **Extracted on:** 2026-04-01 14:39:33
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524035/github.com_hlaueriksson_CommandQuery_970f1c0c

---

## File: `.editorconfig`
```
# editorconfig.org

# top-most EditorConfig file
root = true

# Default settings:
# A newline ending every file
# Use 4 spaces as indentation
[*]
insert_final_newline = true
indent_style = space
indent_size = 4
trim_trailing_whitespace = true
charset = utf-8

[*.json]
indent_size = 2

# C# files
[*.cs]
# New line preferences
csharp_new_line_before_open_brace = all
csharp_new_line_before_else = true
csharp_new_line_before_catch = true
csharp_new_line_before_finally = true
csharp_new_line_before_members_in_object_initializers = true
csharp_new_line_before_members_in_anonymous_types = true
csharp_new_line_between_query_expression_clauses = true

# Indentation preferences
csharp_indent_block_contents = true
csharp_indent_braces = false
csharp_indent_case_contents = true
csharp_indent_case_contents_when_block = true
csharp_indent_switch_labels = true
csharp_indent_labels = one_less_than_current

# Modifier preferences
csharp_preferred_modifier_order = public,private,protected,internal,static,extern,new,virtual,abstract,sealed,override,readonly,unsafe,volatile,async:suggestion

# avoid this. unless absolutely necessary
dotnet_style_qualification_for_field = false:suggestion
dotnet_style_qualification_for_property = false:suggestion
dotnet_style_qualification_for_method = false:suggestion
dotnet_style_qualification_for_event = false:suggestion

# Types: use keywords instead of BCL types, and permit var only when the type is clear
dotnet_style_predefined_type_for_locals_parameters_members = true:suggestion
dotnet_style_predefined_type_for_member_access = true:suggestion

# name all constant fields using PascalCase
dotnet_naming_rule.constant_fields_should_be_pascal_case.severity = suggestion
dotnet_naming_rule.constant_fields_should_be_pascal_case.symbols  = constant_fields
dotnet_naming_rule.constant_fields_should_be_pascal_case.style    = pascal_case_style
dotnet_naming_symbols.constant_fields.applicable_kinds   = field
dotnet_naming_symbols.constant_fields.required_modifiers = const
dotnet_naming_style.pascal_case_style.capitalization = pascal_case

# internal and private fields should be _camelCase
dotnet_naming_rule.camel_case_for_private_internal_fields.severity = suggestion
dotnet_naming_rule.camel_case_for_private_internal_fields.symbols  = private_internal_fields
dotnet_naming_rule.camel_case_for_private_internal_fields.style    = camel_case_underscore_style
dotnet_naming_symbols.private_internal_fields.applicable_kinds = field
dotnet_naming_symbols.private_internal_fields.applicable_accessibilities = private, internal
dotnet_naming_style.camel_case_underscore_style.required_prefix = _
dotnet_naming_style.camel_case_underscore_style.capitalization = camel_case

# Code style defaults
csharp_using_directive_placement = outside_namespace:suggestion
dotnet_sort_system_directives_first = true
csharp_prefer_braces = true:refactoring
csharp_preserve_single_line_blocks = true:none
csharp_preserve_single_line_statements = false:none
csharp_prefer_static_local_function = true:suggestion
csharp_prefer_simple_using_statement = false:none
csharp_style_prefer_switch_expression = true:suggestion

# Code quality
dotnet_style_readonly_field = true:error
dotnet_code_quality_unused_parameters = non_public:suggestion

# Expression-level preferences
dotnet_style_object_initializer = true:suggestion
dotnet_style_collection_initializer = true:suggestion
dotnet_style_explicit_tuple_names = true:suggestion
dotnet_style_coalesce_expression = true:suggestion
dotnet_style_null_propagation = true:suggestion
dotnet_style_prefer_is_null_check_over_reference_equality_method = true:suggestion
dotnet_style_prefer_inferred_tuple_names = true:suggestion
dotnet_style_prefer_inferred_anonymous_type_member_names = true:suggestion
dotnet_style_prefer_auto_properties = true:suggestion
dotnet_style_prefer_conditional_expression_over_assignment = true:refactoring
dotnet_style_prefer_conditional_expression_over_return = true:refactoring
csharp_prefer_simple_default_expression = true:suggestion

# Expression-bodied members
csharp_style_expression_bodied_methods = true:refactoring
csharp_style_expression_bodied_constructors = true:refactoring
csharp_style_expression_bodied_operators = true:refactoring
csharp_style_expression_bodied_properties = true:refactoring
csharp_style_expression_bodied_indexers = true:refactoring
csharp_style_expression_bodied_accessors = true:refactoring
csharp_style_expression_bodied_lambdas = true:refactoring
csharp_style_expression_bodied_local_functions = true:refactoring

# Pattern matching
csharp_style_pattern_matching_over_is_with_cast_check = true:suggestion
csharp_style_pattern_matching_over_as_with_null_check = true:suggestion
csharp_style_inlined_variable_declaration = true:suggestion

# Null checking preferences
csharp_style_throw_expression = true:suggestion
csharp_style_conditional_delegate_call = true:suggestion

# Other features
csharp_style_prefer_index_operator = false:none
csharp_style_prefer_range_operator = false:none
csharp_style_pattern_local_over_anonymous_function = false:none

# Space preferences
csharp_space_after_cast = false
csharp_space_after_colon_in_inheritance_clause = true
csharp_space_after_comma = true
csharp_space_after_dot = false
csharp_space_after_keywords_in_control_flow_statements = true
csharp_space_after_semicolon_in_for_statement = true
csharp_space_around_binary_operators = before_and_after
csharp_space_around_declaration_statements = do_not_ignore
csharp_space_before_colon_in_inheritance_clause = true
csharp_space_before_comma = false
csharp_space_before_dot = false
csharp_space_before_open_square_brackets = false
csharp_space_before_semicolon_in_for_statement = false
csharp_space_between_empty_square_brackets = false
csharp_space_between_method_call_empty_parameter_list_parentheses = false
csharp_space_between_method_call_name_and_opening_parenthesis = false
csharp_space_between_method_call_parameter_list_parentheses = false
csharp_space_between_method_declaration_empty_parameter_list_parentheses = false
csharp_space_between_method_declaration_name_and_open_parenthesis = false
csharp_space_between_method_declaration_parameter_list_parentheses = false
csharp_space_between_parentheses = false
csharp_space_between_square_brackets = false

# Analyzers
dotnet_code_quality.ca1802.api_surface = private, internal

# C++ Files
[*.{cpp,h,in}]
curly_bracket_next_line = true
indent_brace_style = Allman

# Xml project files
[*.{csproj,vbproj,vcxproj,vcxproj.filters,proj,nativeproj,locproj}]
indent_size = 2

# Xml build files
[*.builds]
indent_size = 2

# Xml files
[*.{xml,stylecop,resx,ruleset}]
indent_size = 2

# Xml config files
[*.{props,targets,config,nuspec}]
indent_size = 2

# Shell scripts
[*.sh]
end_of_line = lf
[*.{cmd, bat}]
end_of_line = crlf

[*.cs]
dotnet_diagnostic.CA1014.severity = none
dotnet_diagnostic.CA1031.severity = none
dotnet_diagnostic.CA1040.severity = none
dotnet_diagnostic.CA1054.severity = none
dotnet_diagnostic.CA1848.severity = none
dotnet_diagnostic.SA1101.severity = none
dotnet_diagnostic.SA1309.severity = none
dotnet_diagnostic.SA1402.severity = none
dotnet_diagnostic.SA1623.severity = none
dotnet_diagnostic.SA1625.severity = none
dotnet_diagnostic.SA1633.severity = none
```

## File: `.gcloudignore`
```
# This file tells "gcloud functions deploy" which files and folders
# to ignore. This is important when deploying multi-project functions,
# as otherwise a lot of unnecessary files (particularly in the bin and
# obj directories) may be uploaded.

.gcloudignore

.git/
.github/
.vs/
src/
tests/

bin/
obj/
```

## File: `.gitattributes`
```
# Auto detect text files and perform LF normalization
* text=auto

# Custom for Visual Studio
*.cs     diff=csharp
*.sln    merge=union
*.csproj merge=union
*.vbproj merge=union
*.fsproj merge=union
*.dbproj merge=union

# Standard to msysgit
*.doc	 diff=astextplain
*.DOC	 diff=astextplain
*.docx diff=astextplain
*.DOCX diff=astextplain
*.dot  diff=astextplain
*.DOT  diff=astextplain
*.pdf  diff=astextplain
*.PDF	 diff=astextplain
*.rtf	 diff=astextplain
*.RTF	 diff=astextplain
```

## File: `.gitignore`
```
## Ignore Visual Studio temporary files, build results, and
## files generated by popular Visual Studio add-ons.
##
## Get latest from https://github.com/github/gitignore/blob/main/VisualStudio.gitignore

# User-specific files
*.rsuser
*.suo
*.user
*.userosscache
*.sln.docstates

# User-specific files (MonoDevelop/Xamarin Studio)
*.userprefs

# Mono auto generated files
mono_crash.*

# Build results
[Dd]ebug/
[Dd]ebugPublic/
[Rr]elease/
[Rr]eleases/
x64/
x86/
[Ww][Ii][Nn]32/
[Aa][Rr][Mm]/
[Aa][Rr][Mm]64/
bld/
[Bb]in/
[Oo]bj/
[Ll]og/
[Ll]ogs/

# Visual Studio 2015/2017 cache/options directory
.vs/
# Uncomment if you have tasks that create the project's static files in wwwroot
#wwwroot/

# Visual Studio 2017 auto generated files
Generated\ Files/

# MSTest test Results
[Tt]est[Rr]esult*/
[Bb]uild[Ll]og.*

# NUnit
*.VisualState.xml
TestResult.xml
nunit-*.xml

# Build Results of an ATL Project
[Dd]ebugPS/
[Rr]eleasePS/
dlldata.c

# Benchmark Results
BenchmarkDotNet.Artifacts/

# .NET Core
project.lock.json
project.fragment.lock.json
artifacts/

# ASP.NET Scaffolding
ScaffoldingReadMe.txt

# StyleCop
StyleCopReport.xml

# Files built by Visual Studio
*_i.c
*_p.c
*_h.h
*.ilk
*.meta
*.obj
*.iobj
*.pch
*.pdb
*.ipdb
*.pgc
*.pgd
*.rsp
*.sbr
*.tlb
*.tli
*.tlh
*.tmp
*.tmp_proj
*_wpftmp.csproj
*.log
*.tlog
*.vspscc
*.vssscc
.builds
*.pidb
*.svclog
*.scc

# Chutzpah Test files
_Chutzpah*

# Visual C++ cache files
ipch/
*.aps
*.ncb
*.opendb
*.opensdf
*.sdf
*.cachefile
*.VC.db
*.VC.VC.opendb

# Visual Studio profiler
*.psess
*.vsp
*.vspx
*.sap

# Visual Studio Trace Files
*.e2e

# TFS 2012 Local Workspace
$tf/

# Guidance Automation Toolkit
*.gpState

# ReSharper is a .NET coding add-in
_ReSharper*/
*.[Rr]e[Ss]harper
*.DotSettings.user

# TeamCity is a build add-in
_TeamCity*

# DotCover is a Code Coverage Tool
*.dotCover

# AxoCover is a Code Coverage Tool
.axoCover/*
!.axoCover/settings.json

# Coverlet is a free, cross platform Code Coverage Tool
coverage*.json
coverage*.xml
coverage*.info

# Visual Studio code coverage results
*.coverage
*.coveragexml

# NCrunch
_NCrunch_*
.*crunch*.local.xml
nCrunchTemp_*

# MightyMoose
*.mm.*
AutoTest.Net/

# Web workbench (sass)
.sass-cache/

# Installshield output folder
[Ee]xpress/

# DocProject is a documentation generator add-in
DocProject/buildhelp/
DocProject/Help/*.HxT
DocProject/Help/*.HxC
DocProject/Help/*.hhc
DocProject/Help/*.hhk
DocProject/Help/*.hhp
DocProject/Help/Html2
DocProject/Help/html

# Click-Once directory
publish/

# Publish Web Output
*.[Pp]ublish.xml
*.azurePubxml
# Note: Comment the next line if you want to checkin your web deploy settings,
# but database connection strings (with potential passwords) will be unencrypted
*.pubxml
*.publishproj

# Microsoft Azure Web App publish settings. Comment the next line if you want to
# checkin your Azure Web App publish settings, but sensitive information contained
# in these scripts will be unencrypted
PublishScripts/

# NuGet Packages
*.nupkg
# NuGet Symbol Packages
*.snupkg
# The packages folder can be ignored because of Package Restore
**/[Pp]ackages/*
# except build/, which is used as an MSBuild target.
!**/[Pp]ackages/build/
# Uncomment if necessary however generally it will be regenerated when needed
#!**/[Pp]ackages/repositories.config
# NuGet v3's project.json files produces more ignorable files
*.nuget.props
*.nuget.targets

# Microsoft Azure Build Output
csx/
*.build.csdef

# Microsoft Azure Emulator
ecf/
rcf/

# Windows Store app package directories and files
AppPackages/
BundleArtifacts/
Package.StoreAssociation.xml
_pkginfo.txt
*.appx
*.appxbundle
*.appxupload

# Visual Studio cache files
# files ending in .cache can be ignored
*.[Cc]ache
# but keep track of directories ending in .cache
!?*.[Cc]ache/

# Others
ClientBin/
~$*
*~
*.dbmdl
*.dbproj.schemaview
*.jfm
*.pfx
*.publishsettings
orleans.codegen.cs

# Including strong name files can present a security risk
# (https://github.com/github/gitignore/pull/2483#issue-259490424)
#*.snk

# Since there are multiple workflows, uncomment next line to ignore bower_components
# (https://github.com/github/gitignore/pull/1529#issuecomment-104372622)
#bower_components/

# RIA/Silverlight projects
Generated_Code/

# Backup & report files from converting an old project file
# to a newer Visual Studio version. Backup files are not needed,
# because we have git ;-)
_UpgradeReport_Files/
Backup*/
UpgradeLog*.XML
UpgradeLog*.htm
ServiceFabricBackup/
*.rptproj.bak

# SQL Server files
*.mdf
*.ldf
*.ndf

# Business Intelligence projects
*.rdl.data
*.bim.layout
*.bim_*.settings
*.rptproj.rsuser
*- [Bb]ackup.rdl
*- [Bb]ackup ([0-9]).rdl
*- [Bb]ackup ([0-9][0-9]).rdl

# Microsoft Fakes
FakesAssemblies/

# GhostDoc plugin setting file
*.GhostDoc.xml

# Node.js Tools for Visual Studio
.ntvs_analysis.dat
node_modules/

# Visual Studio 6 build log
*.plg

# Visual Studio 6 workspace options file
*.opt

# Visual Studio 6 auto-generated workspace file (contains which files were open etc.)
*.vbw

# Visual Studio 6 auto-generated project file (contains which files were open etc.)
*.vbp

# Visual Studio 6 workspace and project file (working project files containing files to include in project)
*.dsw
*.dsp

# Visual Studio 6 technical files
*.ncb
*.aps

# Visual Studio LightSwitch build output
**/*.HTMLClient/GeneratedArtifacts
**/*.DesktopClient/GeneratedArtifacts
**/*.DesktopClient/ModelManifest.xml
**/*.Server/GeneratedArtifacts
**/*.Server/ModelManifest.xml
_Pvt_Extensions

# Paket dependency manager
.paket/paket.exe
paket-files/

# FAKE - F# Make
.fake/

# CodeRush personal settings
.cr/personal

# Python Tools for Visual Studio (PTVS)
__pycache__/
*.pyc

# Cake - Uncomment if you are using it
# tools/**
# !tools/packages.config

# Tabs Studio
*.tss

# Telerik's JustMock configuration file
*.jmconfig

# BizTalk build output
*.btp.cs
*.btm.cs
*.odx.cs
*.xsd.cs

# OpenCover UI analysis results
OpenCover/

# Azure Stream Analytics local run output
ASALocalRun/

# MSBuild Binary and Structured Log
*.binlog

# NVidia Nsight GPU debugger configuration file
*.nvuser

# MFractors (Xamarin productivity tool) working folder
.mfractor/

# Local History for Visual Studio
.localhistory/

# Visual Studio History (VSHistory) files
.vshistory/

# BeatPulse healthcheck temp database
healthchecksdb

# Backup folder for Package Reference Convert tool in Visual Studio 2017
MigrationBackup/

# Ionide (cross platform F# VS Code tools) working folder
.ionide/

# Fody - auto-generated XML schema
FodyWeavers.xsd

# VS Code files for those working on multiple tools
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
*.code-workspace

# Local History for Visual Studio Code
.history/

# Windows Installer files from build outputs
*.cab
*.msi
*.msix
*.msm
*.msp

# JetBrains Rider
*.sln.iml
```

## File: `Analyzers.props`
```
<Project>
  <PropertyGroup>
    <RunWithWarnings>true</RunWithWarnings>
    <StyleCopTreatErrorsAsWarnings>false</StyleCopTreatErrorsAsWarnings>
    <TreatWarningsAsErrors>true</TreatWarningsAsErrors>
    <AnalysisMode>AllEnabledByDefault</AnalysisMode>
    <EnablePackageValidation>true</EnablePackageValidation>
  </PropertyGroup>
  <ItemGroup>
    <AdditionalFiles Include="../../stylecop.json">
      <Link>stylecop.json</Link>
    </AdditionalFiles>
  </ItemGroup>
  <ItemGroup>
    <PackageReference Include="Microsoft.VisualStudio.Threading.Analyzers" Version="17.10.48">
      <PrivateAssets>all</PrivateAssets>
      <IncludeAssets>runtime; build; native; contentfiles; analyzers</IncludeAssets>
    </PackageReference>
    <PackageReference Include="Roslynator.Analyzers" Version="4.12.4">
      <PrivateAssets>all</PrivateAssets>
      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
    </PackageReference>
    <PackageReference Include="StyleCop.Analyzers" Version="1.2.0-beta.556">
      <PrivateAssets>all</PrivateAssets>
      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
    </PackageReference>
  </ItemGroup>
</Project>
```

## File: `CommandQuery.AWSLambda.md`
```markdown
# CommandQuery.AWSLambda ⚡

[![build](https://github.com/hlaueriksson/CommandQuery/actions/workflows/build.yml/badge.svg)](https://github.com/hlaueriksson/CommandQuery/actions/workflows/build.yml) [![CodeFactor](https://codefactor.io/repository/github/hlaueriksson/commandquery/badge)](https://codefactor.io/repository/github/hlaueriksson/commandquery)

> Command Query Separation for AWS Lambda

* Provides generic function support for commands and queries with *Amazon API Gateway*
* Enables APIs based on HTTP `POST` and `GET`

## Get Started

0. Install **AWS Toolkit for Visual Studio**
   * [https://aws.amazon.com/visualstudio/](https://aws.amazon.com/visualstudio/)
1. Create a new **AWS Serverless Application (.NET Core)** project
   * [Tutorial](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/lambda-build-test-severless-app.html)
2. Install the `CommandQuery.AWSLambda` package from [NuGet](https://www.nuget.org/packages/CommandQuery.AWSLambda)
   * `PM>` `Install-Package CommandQuery.AWSLambda`
3. Create functions
   * Preferably named `Command` and `Query`
4. Create commands and command handlers
   * Implement `ICommand` and `ICommandHandler<in TCommand>`
   * Or `ICommand<TResult>` and `ICommandHandler<in TCommand, TResult>`
5. Create queries and query handlers
   * Implement `IQuery<TResult>` and `IQueryHandler<in TQuery, TResult>`
6. Configure the serverless template

![New Project - AWS Serverless Application (.NET Core - C#)](https://raw.githubusercontent.com/hlaueriksson/CommandQuery/master/vs-new-project-aws-serverless-application-1.png)

Choose:

* AWS Serverless Application (.NET Core - C#)

![New AWS Serverless Application - Empty Serverless Application](https://raw.githubusercontent.com/hlaueriksson/CommandQuery/master/vs-new-project-aws-serverless-application-2.png)

Choose:

* Empty Serverless Application

## Commands

```cs
using Amazon.Lambda.Annotations;
using Amazon.Lambda.Annotations.APIGateway;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using CommandQuery.AWSLambda;

namespace CommandQuery.Sample.AWSLambda;

public class Command(ICommandFunction commandFunction)
{
    [LambdaFunction(Policies = "AWSLambdaBasicExecutionRole", MemorySize = 256, Timeout = 30)]
    [RestApi(LambdaHttpMethod.Post, "/command/{commandName}")]
    public async Task<APIGatewayProxyResponse> Post(
        APIGatewayProxyRequest request,
        ILambdaContext context,
        string commandName) =>
        await commandFunction.HandleAsync(commandName, request, context.Logger);
}
```

* The function is requested via HTTP `POST` with the Content-Type `application/json` in the header.
* The name of the command is the slug of the URL.
* The command itself is provided as JSON in the body.
* If the command succeeds; the response is empty with the HTTP status code `200`.
* If the command fails; the response is an error message with the HTTP status code `400` or `500`.

Commands with result:

* If the command succeeds; the response is the result as JSON with the HTTP status code `200`.

## Queries

```cs
using Amazon.Lambda.Annotations;
using Amazon.Lambda.Annotations.APIGateway;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using CommandQuery.AWSLambda;

namespace CommandQuery.Sample.AWSLambda
{
    public class Query(IQueryFunction queryFunction)
    {
        [LambdaFunction(Policies = "AWSLambdaBasicExecutionRole", MemorySize = 256, Timeout = 30)]
        [RestApi(LambdaHttpMethod.Get, "/query/{queryName}")]
        public async Task<APIGatewayProxyResponse> Get(
            APIGatewayProxyRequest request,
            ILambdaContext context,
            string queryName) =>
            await queryFunction.HandleAsync(queryName, request, context.Logger);

        [LambdaFunction(Policies = "AWSLambdaBasicExecutionRole", MemorySize = 256, Timeout = 30)]
        [RestApi(LambdaHttpMethod.Post, "/query/{queryName}")]
        public async Task<APIGatewayProxyResponse> Post(
            APIGatewayProxyRequest request,
            ILambdaContext context,
            string queryName) =>
            await queryFunction.HandleAsync(queryName, request, context.Logger);
    }
}
```

* The function is requested via:
  * HTTP `POST` with the Content-Type `application/json` in the header and the query itself as JSON in the body
  * HTTP `GET` and the query itself as query string parameters in the URL
* The name of the query is the slug of the URL.
* If the query succeeds; the response is the result as JSON with the HTTP status code `200`.
* If the query fails; the response is an error message with the HTTP status code `400` or `500`.

## Configuration

Configuration in `Startup.cs`:

```cs
using Amazon.Lambda.Annotations;
using Amazon.Lambda.Core;
using CommandQuery.AWSLambda;
using CommandQuery.Sample.Contracts.Commands;
using CommandQuery.Sample.Contracts.Queries;
using CommandQuery.Sample.Handlers;
using CommandQuery.Sample.Handlers.Commands;
using CommandQuery.Sample.Handlers.Queries;
using Microsoft.Extensions.DependencyInjection;

[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace CommandQuery.Sample.AWSLambda;

[LambdaStartup]
public class Startup
{
    public void ConfigureServices(IServiceCollection services)
    {
        //services.AddSingleton(new JsonSerializerOptions(JsonSerializerDefaults.Web));

        // Add commands and queries
        services.AddCommandFunction(typeof(FooCommandHandler).Assembly, typeof(FooCommand).Assembly);
        services.AddQueryFunction(typeof(BarQueryHandler).Assembly, typeof(BarQuery).Assembly);

        // Add handler dependencies
        services.AddTransient<IDateTimeProxy, DateTimeProxy>();
        services.AddTransient<ICultureService, CultureService>();

        // Validation
        var serviceProvider = services.BuildServiceProvider();
        serviceProvider.GetService<ICommandProcessor>()!.AssertConfigurationIsValid();
        serviceProvider.GetService<IQueryProcessor>()!.AssertConfigurationIsValid();
    }
}
```

The extension methods `AddCommandFunction` and `AddQueryFunction` will add functions and all command/query handlers in the given assemblies to the IoC container.
You can pass in a `params` array of `Assembly` arguments if your handlers are located in different projects.
If you only have one project you can use `typeof(Program).Assembly` as a single argument.

Configuration in `serverless.template`:

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Transform": "AWS::Serverless-2016-10-31",
  "Description": "An AWS Serverless Application. This template is partially managed by Amazon.Lambda.Annotations (v1.5.0.0).",
  "Resources": {
    "CommandQuerySampleAWSLambdaCommandPostGenerated": {
      "Type": "AWS::Serverless::Function",
      "Metadata": {
        "Tool": "Amazon.Lambda.Annotations",
        "SyncedEvents": [
          "RootPost"
        ],
        "SyncedEventProperties": {
          "RootPost": [
            "Path",
            "Method"
          ]
        }
      },
      "Properties": {
        "Architectures": [
          "x86_64"
        ],
        "Handler": "CommandQuery.Sample.AWSLambda::CommandQuery.Sample.AWSLambda.Command_Post_Generated::Post",
        "Runtime": "dotnet8",
        "CodeUri": ".",
        "MemorySize": 256,
        "Timeout": 30,
        "Policies": [
          "AWSLambdaBasicExecutionRole"
        ],
        "PackageType": "Zip",
        "Events": {
          "RootPost": {
            "Type": "Api",
            "Properties": {
              "Path": "/command/{commandName}",
              "Method": "POST"
            }
          }
        }
      }
    },
    "CommandQuerySampleAWSLambdaQueryGetGenerated": {
      "Type": "AWS::Serverless::Function",
      "Metadata": {
        "Tool": "Amazon.Lambda.Annotations",
        "SyncedEvents": [
          "RootGet"
        ],
        "SyncedEventProperties": {
          "RootGet": [
            "Path",
            "Method"
          ]
        }
      },
      "Properties": {
        "Architectures": [
          "x86_64"
        ],
        "Handler": "CommandQuery.Sample.AWSLambda::CommandQuery.Sample.AWSLambda.Query_Get_Generated::Get",
        "Runtime": "dotnet8",
        "CodeUri": ".",
        "MemorySize": 256,
        "Timeout": 30,
        "Policies": [
          "AWSLambdaBasicExecutionRole"
        ],
        "PackageType": "Zip",
        "Events": {
          "RootGet": {
            "Type": "Api",
            "Properties": {
              "Path": "/query/{queryName}",
              "Method": "GET"
            }
          }
        }
      }
    },
    "CommandQuerySampleAWSLambdaQueryPostGenerated": {
      "Type": "AWS::Serverless::Function",
      "Metadata": {
        "Tool": "Amazon.Lambda.Annotations",
        "SyncedEvents": [
          "RootPost"
        ],
        "SyncedEventProperties": {
          "RootPost": [
            "Path",
            "Method"
          ]
        }
      },
      "Properties": {
        "Architectures": [
          "x86_64"
        ],
        "Handler": "CommandQuery.Sample.AWSLambda::CommandQuery.Sample.AWSLambda.Query_Post_Generated::Post",
        "Runtime": "dotnet8",
        "CodeUri": ".",
        "MemorySize": 256,
        "Timeout": 30,
        "Policies": [
          "AWSLambdaBasicExecutionRole"
        ],
        "PackageType": "Zip",
        "Events": {
          "RootPost": {
            "Type": "Api",
            "Properties": {
              "Path": "/query/{queryName}",
              "Method": "POST"
            }
          }
        }
      }
    }
  },
  "Outputs": {
    "ApiURL": {
      "Description": "API endpoint URL for Prod environment",
      "Value": {
        "Fn::Sub": "https://${ServerlessRestApi}.execute-api.${AWS::Region}.amazonaws.com/Prod/"
      }
    }
  }
}
```

## Testing

You can [test](https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.TestUtilities/README.md) your lambdas with the [Amazon.Lambda.TestUtilities](https://www.nuget.org/packages/Amazon.Lambda.TestUtilities) package.

```cs
using System.Text.Json;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.TestUtilities;
using CommandQuery.AWSLambda;
using CommandQuery.Sample.Contracts.Commands;
using FluentAssertions;
using Microsoft.Extensions.DependencyInjection;
using NUnit.Framework;

namespace CommandQuery.Sample.AWSLambda.Tests
{
    public class CommandTests
    {
        [SetUp]
        public void SetUp()
        {
            var serviceCollection = new ServiceCollection();
            new Startup().ConfigureServices(serviceCollection);
            var serviceProvider = serviceCollection.BuildServiceProvider();

            Subject = new Command(serviceProvider.GetRequiredService<ICommandFunction>());
            Context = new TestLambdaContext();
        }

        [Test]
        public async Task should_handle_command()
        {
            var response = await Subject.Post(GetRequest(new FooCommand { Value = "Foo" }), Context, "FooCommand");
            response.StatusCode.Should().Be(200);
        }

        [Test]
        public async Task should_handle_errors()
        {
            var response = await Subject.Post(GetRequest(new FooCommand()), Context, "FooCommand");
            response.ShouldBeError("Value cannot be null or empty");
        }

        static APIGatewayProxyRequest GetRequest(object body) => new() { Body = JsonSerializer.Serialize(body) };

        Command Subject = null!;
        TestLambdaContext Context = null!;
    }
}
```

## Samples

* [CommandQuery.Sample.AWSLambda](https://github.com/hlaueriksson/CommandQuery/tree/master/samples/CommandQuery.Sample.AWSLambda)
* [CommandQuery.Sample.AWSLambda.Tests](https://github.com/hlaueriksson/CommandQuery/tree/master/samples/CommandQuery.Sample.AWSLambda.Tests)
```

## File: `CommandQuery.Abstractions.md`
```markdown
# CommandQuery.Abstractions ⚙️

[![build](https://github.com/hlaueriksson/CommandQuery/actions/workflows/build.yml/badge.svg)](https://github.com/hlaueriksson/CommandQuery/actions/workflows/build.yml) [![CodeFactor](https://codefactor.io/repository/github/hlaueriksson/commandquery/badge)](https://codefactor.io/repository/github/hlaueriksson/commandquery)

> Command Query Separation abstractions for .NET and C#

## Commands

```cs
public interface ICommand;

public interface ICommand<TResult>;
```

```cs
public interface ICommandHandler<in TCommand>
    where TCommand : ICommand
{
    Task HandleAsync(TCommand command, CancellationToken cancellationToken);
}

public interface ICommandHandler<in TCommand, TResult>
    where TCommand : ICommand<TResult>
{
    Task<TResult> HandleAsync(TCommand command, CancellationToken cancellationToken);
}
```

## Queries

```cs
public interface IQuery<TResult>;
```

```cs
public interface IQueryHandler<in TQuery, TResult>
    where TQuery : IQuery<TResult>
{
    Task<TResult> HandleAsync(TQuery query, CancellationToken cancellationToken);
}
```

## Error

```cs
public interface IError
{
    public string? Message { get; }

    public Dictionary<string, object>? Details { get; }
}
```

## Samples

* [CommandQuery.Sample.Contracts](https://github.com/hlaueriksson/CommandQuery/tree/master/samples/CommandQuery.Sample.Contracts)
* [CommandQuery.Sample.Handlers](https://github.com/hlaueriksson/CommandQuery/tree/master/samples/CommandQuery.Sample.Handlers)
```

## File: `CommandQuery.AspNetCore.md`
```markdown
# CommandQuery.AspNetCore 🌐

[![build](https://github.com/hlaueriksson/CommandQuery/actions/workflows/build.yml/badge.svg)](https://github.com/hlaueriksson/CommandQuery/actions/workflows/build.yml) [![CodeFactor](https://codefactor.io/repository/github/hlaueriksson/commandquery/badge)](https://codefactor.io/repository/github/hlaueriksson/commandquery)

> Command Query Separation for ASP.NET Core

* Provides generic actions for handling the execution of commands and queries
* Enables APIs based on HTTP `POST` and `GET`

## Get Started

1. Create a new **ASP.NET Core** project
   * [Tutorial](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-web-api?view=aspnetcore-8.0&tabs=visual-studio)
2. Install the `CommandQuery.AspNetCore` package from [NuGet](https://www.nuget.org/packages/CommandQuery.AspNetCore)
   * `PM>` `Install-Package CommandQuery.AspNetCore`
3. Create commands and command handlers
   * Implement `ICommand` and `ICommandHandler<in TCommand>`
   * Or `ICommand<TResult>` and `ICommandHandler<in TCommand, TResult>`
4. Create queries and query handlers
   * Implement `IQuery<TResult>` and `IQueryHandler<in TQuery, TResult>`
5. Configure services in `Startup.cs`

![Add a new project - ASP.NET Core Web API](https://raw.githubusercontent.com/hlaueriksson/CommandQuery/master/vs-new-project-aspnet-core-web-api.png)

Choose:

* .NET 8.0 (Long Term Support)
* Use controllers

## Configuration

Configuration in `Program.cs`:

```cs
using CommandQuery;
using CommandQuery.AspNetCore;
using CommandQuery.Sample.Contracts.Commands;
using CommandQuery.Sample.Contracts.Queries;
using CommandQuery.Sample.Handlers;
using CommandQuery.Sample.Handlers.Commands;
using CommandQuery.Sample.Handlers.Queries;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// Add commands and queries
builder.Services.AddCommandControllers(typeof(FooCommandHandler).Assembly, typeof(FooCommand).Assembly);
builder.Services.AddQueryControllers(typeof(BarQueryHandler).Assembly, typeof(BarQuery).Assembly);

// Add handler dependencies
builder.Services.AddTransient<IDateTimeProxy, DateTimeProxy>();
builder.Services.AddTransient<ICultureService, CultureService>();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

// Validation
app.Services.GetService<ICommandProcessor>()!.AssertConfigurationIsValid();
app.Services.GetService<IQueryProcessor>()!.AssertConfigurationIsValid();

app.Run();
```

The extension methods `AddCommandControllers` and `AddQueryControllers` will add controllers and all command/query handlers in the given assemblies to the IoC container.
You can pass in a `params` array of `Assembly` arguments if your handlers are located in different projects.
If you only have one project you can use `typeof(Startup).Assembly` as a single argument.

## Commands

The action method from the generated controller will handle commands:

```cs
/// <summary>
/// Handle a command.
/// </summary>
/// <param name="command">The command.</param>
/// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
/// <returns>The result for status code <c>200</c>, or an error for status code <c>400</c> and <c>500</c>.</returns>
[HttpPost]
public async Task<IActionResult> HandleAsync(TCommand command, CancellationToken cancellationToken)
```

* The action is requested via HTTP `POST` with the Content-Type `application/json` in the header
* The name of the command is the slug of the URL
* The command itself is provided as JSON in the body
* If the command succeeds; the response is empty with the HTTP status code `200`
* If the command fails; the response is an error message with the HTTP status code `400` or `500`

Commands with result:

```cs
/// <summary>
/// Handle a command.
/// </summary>
/// <param name="command">The command.</param>
/// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
/// <returns>The result for status code <c>200</c>, or an error for status code <c>400</c> and <c>500</c>.</returns>
[HttpPost]
public async Task<IActionResult> HandleAsync(TCommand command, CancellationToken cancellationToken)
```

* If the command succeeds; the response is the result as JSON with the HTTP status code `200`.
* If the command fails; the response is an error message with the HTTP status code `400` or `500`.

## Queries

The action methods from the generated controller will handle queries:

```cs
/// <summary>
/// Handle a query.
/// </summary>
/// <param name="query">The query.</param>
/// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
/// <returns>The result + 200, 400 or 500.</returns>
[HttpPost]
public async Task<IActionResult> HandlePostAsync(TQuery query, CancellationToken cancellationToken)
```

```cs
/// <summary>
/// Handle a query.
/// </summary>
/// <param name="query">The query.</param>
/// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
/// <returns>The result + 200, 400 or 500.</returns>
[HttpGet]
public async Task<IActionResult> HandleGetAsync([FromQuery] TQuery query, CancellationToken cancellationToken)
```

* The action is requested via:
  * HTTP `POST` with the Content-Type `application/json` in the header and the query itself as JSON in the body
  * HTTP `GET` and the query itself as query string parameters in the URL
* The name of the query is the slug of the URL.
* If the query succeeds; the response is the result as JSON with the HTTP status code `200`.
* If the query fails; the response is an error message with the HTTP status code `400` or `500`.

## Testing

You can [integration test](https://docs.microsoft.com/en-us/aspnet/core/test/integration-tests?view=aspnetcore-6.0) your controllers and command/query handlers with the `Microsoft.AspNetCore.Mvc.Testing` package.

```cs
using System.Net;
using System.Net.Http.Json;
using CommandQuery.Sample.Contracts.Commands;
using FluentAssertions;
using Microsoft.AspNetCore.Mvc.Testing;
using NUnit.Framework;

namespace CommandQuery.Sample.AspNetCore.Tests
{
    public class CommandControllerTests
    {
        [SetUp]
        public void SetUp()
        {
            Factory = new WebApplicationFactory<Program>();
            Client = Factory.CreateClient();
        }

        [TearDown]
        public void TearDown()
        {
            Client.Dispose();
            Factory.Dispose();
        }

        [Test]
        public async Task should_handle_command()
        {
            var response = await Client.PostAsJsonAsync("/api/command/FooCommand", new FooCommand { Value = "Foo" });
            response.StatusCode.Should().Be(HttpStatusCode.OK);
        }

        [Test]
        public async Task should_handle_errors()
        {
            var response = await Client.PostAsJsonAsync("/api/command/FooCommand", new FooCommand { Value = "" });
            await response.ShouldBeErrorAsync("Value cannot be null or empty");
        }

        WebApplicationFactory<Program> Factory = null!;
        HttpClient Client = null!;
    }
}
```

## Samples

* [CommandQuery.Sample.AspNetCore](https://github.com/hlaueriksson/CommandQuery/tree/master/samples/CommandQuery.Sample.AspNetCore)
* [CommandQuery.Sample.AspNetCore.Tests](https://github.com/hlaueriksson/CommandQuery/tree/master/samples/CommandQuery.Sample.AspNetCore.Tests)
```

## File: `CommandQuery.AzureFunctions.md`
```markdown
# CommandQuery.AzureFunctions ⚡

[![build](https://github.com/hlaueriksson/CommandQuery/actions/workflows/build.yml/badge.svg)](https://github.com/hlaueriksson/CommandQuery/actions/workflows/build.yml) [![CodeFactor](https://codefactor.io/repository/github/hlaueriksson/commandquery/badge)](https://codefactor.io/repository/github/hlaueriksson/commandquery)

> Command Query Separation for Azure Functions

* Provides generic function support for commands and queries with *HTTPTriggers*
* Enables APIs based on HTTP `POST` and `GET`

## Get Started

0. Install **Azure development** workload in Visual Studio
   * [Prerequisites](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs?tabs=in-process&pivots=isolated#prerequisites)
1. Create a new **Azure Functions** (_isolated worker process_) project
   * [Tutorial](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide?tabs=windows)
2. Install the `CommandQuery.AzureFunctions` package from [NuGet](https://www.nuget.org/packages/CommandQuery.AzureFunctions/)
   * `PM>` `Install-Package CommandQuery.AzureFunctions`
3. Create functions
   * Preferably named `Command` and `Query`
4. Create commands and command handlers
   * Implement `ICommand` and `ICommandHandler<in TCommand>`
   * Or `ICommand<TResult>` and `ICommandHandler<in TCommand, TResult>`
5. Create queries and query handlers
   * Implement `IQuery<TResult>` and `IQueryHandler<in TQuery, TResult>`
6. Configure services in `Program.cs`

![Add a new project - Azure Functions](https://raw.githubusercontent.com/hlaueriksson/CommandQuery/master/vs-new-project-azure-functions-1.png)

![Create a new Azure Functions Application](https://raw.githubusercontent.com/hlaueriksson/CommandQuery/master/vs-new-project-azure-functions-2.png)

Choose:

* .NET 8.0 Isolated (Long Term Support)
* Http trigger

## Commands

```cs
using CommandQuery.AzureFunctions;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.Functions.Worker;

namespace CommandQuery.Sample.AzureFunctions
{
    public class Command(ICommandFunction commandFunction)
    {
        [Function(nameof(Command))]
        public async Task<IActionResult> Run(
            [HttpTrigger(AuthorizationLevel.Anonymous, "post", Route = "command/{commandName}")] HttpRequest req,
            FunctionContext context,
            string commandName) =>
            await commandFunction.HandleAsync(commandName, req, context.CancellationToken);
    }
}
```

* The function is requested via HTTP `POST` with the Content-Type `application/json` in the header.
* The name of the command is the slug of the URL.
* The command itself is provided as JSON in the body.
* If the command succeeds; the response is empty with the HTTP status code `200`.
* If the command fails; the response is an error message with the HTTP status code `400` or `500`.

Commands with result:

* If the command succeeds; the response is the result as JSON with the HTTP status code `200`.

## Queries

```cs
using CommandQuery.AzureFunctions;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.Functions.Worker;

namespace CommandQuery.Sample.AzureFunctions
{
    public class Query(IQueryFunction queryFunction)
    {
        [Function(nameof(Query))]
        public async Task<IActionResult> Run(
            [HttpTrigger(AuthorizationLevel.Anonymous, "get", "post", Route = "query/{queryName}")] HttpRequest req,
            FunctionContext context,
            string queryName) =>
            await queryFunction.HandleAsync(queryName, req, context.CancellationToken);
    }
}
```

* The function is requested via:
  * HTTP `POST` with the Content-Type `application/json` in the header and the query itself as JSON in the body
  * HTTP `GET` and the query itself as query string parameters in the URL
* The name of the query is the slug of the URL.
* If the query succeeds; the response is the result as JSON with the HTTP status code `200`.
* If the query fails; the response is an error message with the HTTP status code `400` or `500`.

## Configuration

Configuration in `Program.cs`:

```cs
using CommandQuery;
using CommandQuery.AzureFunctions;
using CommandQuery.Sample.Contracts.Commands;
using CommandQuery.Sample.Contracts.Queries;
using CommandQuery.Sample.Handlers;
using CommandQuery.Sample.Handlers.Commands;
using CommandQuery.Sample.Handlers.Queries;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

var host = new HostBuilder()
    .ConfigureFunctionsWebApplication()
    .ConfigureServices(ConfigureServices)
    .Build();

// Validation
host.Services.GetService<ICommandProcessor>()!.AssertConfigurationIsValid();
host.Services.GetService<IQueryProcessor>()!.AssertConfigurationIsValid();

host.Run();

public static partial class Program
{
    public static void ConfigureServices(IServiceCollection services)
    {
        services.AddApplicationInsightsTelemetryWorkerService();
        services.ConfigureFunctionsApplicationInsights();

        services
            //.AddSingleton(new JsonSerializerOptions(JsonSerializerDefaults.Web));

            // Add commands and queries
            .AddCommandFunction(typeof(FooCommandHandler).Assembly, typeof(FooCommand).Assembly)
            .AddQueryFunction(typeof(BarQueryHandler).Assembly, typeof(BarQuery).Assembly)

            // Add handler dependencies
            .AddTransient<IDateTimeProxy, DateTimeProxy>()
            .AddTransient<ICultureService, CultureService>();
    }
}
```

The extension methods `AddCommandFunction` and `AddQueryFunction` will add functions and all command/query handlers in the given assemblies to the IoC container.
You can pass in a `params` array of `Assembly` arguments if your handlers are located in different projects.
If you only have one project you can use `typeof(Program).Assembly` as a single argument.

## Testing

```cs
using System.Text;
using System.Text.Json;
using CommandQuery.AzureFunctions;
using CommandQuery.Sample.Contracts.Commands;
using FluentAssertions;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc.Infrastructure;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.DependencyInjection;
using Moq;
using NUnit.Framework;

namespace CommandQuery.Sample.AzureFunctions.Tests
{
    public class CommandTests
    {
        [SetUp]
        public void SetUp()
        {
            var serviceCollection = new ServiceCollection();
            Program.ConfigureServices(serviceCollection);
            var serviceProvider = serviceCollection.BuildServiceProvider();

            Subject = new Command(serviceProvider.GetRequiredService<ICommandFunction>());

            var context = new Mock<FunctionContext>();
            context.SetupProperty(c => c.InstanceServices, serviceProvider);
            Context = context.Object;
        }

        [Test]
        public async Task should_handle_command()
        {
            var result = await Subject.Run(GetRequest(new FooCommand { Value = "Foo" }), Context, "FooCommand");
            result.As<IStatusCodeActionResult>().StatusCode.Should().Be(200);
        }

        [Test]
        public async Task should_handle_errors()
        {
            var result = await Subject.Run(GetRequest(new FooCommand()), Context, "FooCommand");
            result.ShouldBeError("Value cannot be null or empty");
        }

        HttpRequest GetRequest(object body)
        {
            var request = new Mock<HttpRequest>();
            request.Setup(r => r.Body).Returns(new MemoryStream(Encoding.UTF8.GetBytes(JsonSerializer.Serialize(body))));
            return request.Object;
        }

        Command Subject = null!;
        FunctionContext Context = null!;
    }
}
```

## Samples

* [CommandQuery.Sample.AzureFunctions](https://github.com/hlaueriksson/CommandQuery/tree/master/samples/CommandQuery.Sample.AzureFunctions)
* [CommandQuery.Sample.AzureFunctions.Tests](https://github.com/hlaueriksson/CommandQuery/tree/master/samples/CommandQuery.Sample.AzureFunctions.Tests)
```

## File: `CommandQuery.Client.md`
```markdown
# CommandQuery.Client 🧰

[![build](https://github.com/hlaueriksson/CommandQuery/actions/workflows/build.yml/badge.svg)](https://github.com/hlaueriksson/CommandQuery/actions/workflows/build.yml) [![CodeFactor](https://codefactor.io/repository/github/hlaueriksson/commandquery/badge)](https://codefactor.io/repository/github/hlaueriksson/commandquery)

> Clients for CommandQuery APIs

## Commands

Create a `CommandClient` and invoke `PostAsync`:

```cs
var commandClient = new CommandClient("https://commandquerysampleaspnetcore.azurewebsites.net/api/command/");

await commandClient.PostAsync(new FooCommand { Value = "en-GB" });
```

Commands with result:

```cs
var result = await commandClient.PostAsync(new BazCommand { Value = "en-GB" });
```

## Queries

Create a `QueryClient` and invoke `PostAsync` or `GetAsync`:

```cs
var queryClient = new QueryClient("https://commandquerysampleaspnetcore.azurewebsites.net/api/query/");

var result = await queryClient.PostAsync(new BarQuery { Id = 1 });
result = await queryClient.GetAsync(new BarQuery { Id = 1 });
```

## Samples

* [CommandQuery.Sample.Client](https://github.com/hlaueriksson/CommandQuery/tree/master/samples/CommandQuery.Sample.Client)
```

## File: `CommandQuery.GoogleCloudFunctions.md`
```markdown
# CommandQuery.GoogleCloudFunctions ⚡

[![build](https://github.com/hlaueriksson/CommandQuery/actions/workflows/build.yml/badge.svg)](https://github.com/hlaueriksson/CommandQuery/actions/workflows/build.yml) [![CodeFactor](https://codefactor.io/repository/github/hlaueriksson/commandquery/badge)](https://codefactor.io/repository/github/hlaueriksson/commandquery)

> Command Query Separation for Google Cloud Functions

* Provides generic function support for commands and queries with *HTTP functions*
* Enables APIs based on HTTP `POST` and `GET`

## Get Started

0. Install **Google.Cloud.Functions.Templates**
   * [https://www.nuget.org/packages/Google.Cloud.Functions.Templates/](https://www.nuget.org/packages/Google.Cloud.Functions.Templates/)
1. Create a new **gcf-http** project
   * [Tutorial](https://github.com/GoogleCloudPlatform/functions-framework-dotnet#quickstarts)
2. Install the `CommandQuery.GoogleCloudFunctions` package from [NuGet](https://www.nuget.org/packages/CommandQuery.GoogleCloudFunctions)
   * `PM>` `Install-Package CommandQuery.GoogleCloudFunctions`
3. Create functions
   * Preferably named `Command` and `Query`
4. Create commands and command handlers
   * Implement `ICommand` and `ICommandHandler<in TCommand>`
   * Or `ICommand<TResult>` and `ICommandHandler<in TCommand, TResult>`
5. Create queries and query handlers
   * Implement `IQuery<TResult>` and `IQueryHandler<in TQuery, TResult>`
6. Configure services in `Startup.cs`

## Commands

```cs
using CommandQuery.GoogleCloudFunctions;
using Google.Cloud.Functions.Framework;
using Google.Cloud.Functions.Hosting;
using Microsoft.AspNetCore.Http;

namespace CommandQuery.Sample.GoogleCloudFunctions
{
    [FunctionsStartup(typeof(Startup))]
    public class Command(ICommandFunction commandFunction) : IHttpFunction
    {
        public async Task HandleAsync(HttpContext context)
        {
            var commandName = context.Request.Path.Value!.Substring("/api/command/".Length);
            await commandFunction.HandleAsync(commandName, context, context.RequestAborted);
        }
    }
}
```

* The function is requested via HTTP `POST` with the Content-Type `application/json` in the header.
* The name of the command is the slug of the URL.
* The command itself is provided as JSON in the body.
* If the command succeeds; the response is empty with the HTTP status code `200`.
* If the command fails; the response is an error message with the HTTP status code `400` or `500`.

Commands with result:

* If the command succeeds; the response is the result as JSON with the HTTP status code `200`.

## Queries

```cs
using CommandQuery.GoogleCloudFunctions;
using Google.Cloud.Functions.Framework;
using Google.Cloud.Functions.Hosting;
using Microsoft.AspNetCore.Http;

namespace CommandQuery.Sample.GoogleCloudFunctions
{
    [FunctionsStartup(typeof(Startup))]
    public class Query(IQueryFunction queryFunction) : IHttpFunction
    {
        public async Task HandleAsync(HttpContext context)
        {
            var queryName = context.Request.Path.Value!.Substring("/api/query/".Length);
            await queryFunction.HandleAsync(queryName, context, context.RequestAborted);
        }
    }
}
```

* The function is requested via:
  * HTTP `POST` with the Content-Type `application/json` in the header and the query itself as JSON in the body
  * HTTP `GET` and the query itself as query string parameters in the URL
* The name of the query is the slug of the URL.
* If the query succeeds; the response is the result as JSON with the HTTP status code `200`.
* If the query fails; the response is an error message with the HTTP status code `400` or `500`.

## Configuration

Configuration in `Startup.cs`:

```cs
using CommandQuery.GoogleCloudFunctions;
using CommandQuery.Sample.Contracts.Commands;
using CommandQuery.Sample.Contracts.Queries;
using CommandQuery.Sample.Handlers;
using CommandQuery.Sample.Handlers.Commands;
using CommandQuery.Sample.Handlers.Queries;
using Google.Cloud.Functions.Hosting;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.DependencyInjection;

namespace CommandQuery.Sample.GoogleCloudFunctions
{
    public class Startup : FunctionsStartup
    {
        public override void ConfigureServices(WebHostBuilderContext context, IServiceCollection services) =>
            services
                //.AddSingleton(new JsonSerializerOptions(JsonSerializerDefaults.Web))

                // Add commands and queries
                .AddCommandFunction(typeof(FooCommandHandler).Assembly, typeof(FooCommand).Assembly)
                .AddQueryFunction(typeof(BarQueryHandler).Assembly, typeof(BarQuery).Assembly)

                // Add handler dependencies
                .AddTransient<IDateTimeProxy, DateTimeProxy>()
                .AddTransient<ICultureService, CultureService>();

        public override void Configure(WebHostBuilderContext context, IApplicationBuilder app)
        {
            // Validation
            app.ApplicationServices.GetService<ICommandProcessor>()!.AssertConfigurationIsValid();
            app.ApplicationServices.GetService<IQueryProcessor>()!.AssertConfigurationIsValid();
        }
    }
}
```

The extension methods `AddCommandFunction` and `AddQueryFunction` will add functions and all command/query handlers in the given assemblies to the IoC container.
You can pass in a `params` array of `Assembly` arguments if your handlers are located in different projects.
If you only have one project you can use `typeof(Startup).Assembly` as a single argument.

## Testing

You can [integration test](https://github.com/GoogleCloudPlatform/functions-framework-dotnet/blob/main/docs/testing.md) your functions with the [Google.Cloud.Functions.Testing](https://www.nuget.org/packages/Google.Cloud.Functions.Testing) package.

```cs
using System.Net;
using System.Net.Http.Json;
using CommandQuery.Sample.Contracts.Commands;
using FluentAssertions;
using Google.Cloud.Functions.Testing;
using NUnit.Framework;

namespace CommandQuery.Sample.GoogleCloudFunctions.Tests
{
    public class CommandTests
    {
        [SetUp]
        public void SetUp()
        {
            Server = new FunctionTestServer<Command>();
            Client = Server.CreateClient();
        }

        [TearDown]
        public void TearDown()
        {
            Client.Dispose();
            Server.Dispose();
        }

        [Test]
        public async Task should_handle_command()
        {
            var response = await Client.PostAsJsonAsync("/api/command/FooCommand", new FooCommand { Value = "Foo" });
            response.StatusCode.Should().Be(HttpStatusCode.OK);
        }

        [Test]
        public async Task should_handle_errors()
        {
            var response = await Client.PostAsJsonAsync("/api/command/FooCommand", new FooCommand());
            await response.ShouldBeErrorAsync("Value cannot be null or empty");
        }

        FunctionTestServer<Command> Server = null!;
        HttpClient Client = null!;
    }
}
```

## Samples

* [CommandQuery.Sample.GoogleCloudFunctions](https://github.com/hlaueriksson/CommandQuery/tree/master/samples/CommandQuery.Sample.GoogleCloudFunctions)
* [CommandQuery.Sample.GoogleCloudFunctions.Tests](https://github.com/hlaueriksson/CommandQuery/tree/master/samples/CommandQuery.Sample.GoogleCloudFunctions.Tests)
```

## File: `CommandQuery.Samples.sln`
```
﻿
Microsoft Visual Studio Solution File, Format Version 12.00
# Visual Studio Version 17
VisualStudioVersion = 17.2.32427.441
MinimumVisualStudioVersion = 10.0.40219.1
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.Sample.Contracts", "samples\CommandQuery.Sample.Contracts\CommandQuery.Sample.Contracts.csproj", "{FF932E21-17DE-4BC3-9E25-606502CAE58B}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.Sample.AWSLambda", "samples\CommandQuery.Sample.AWSLambda\CommandQuery.Sample.AWSLambda.csproj", "{6AC1C95D-58A9-4D87-B303-EDF47BD35094}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.Sample.AWSLambda.Tests", "samples\CommandQuery.Sample.AWSLambda.Tests\CommandQuery.Sample.AWSLambda.Tests.csproj", "{B89EE6EB-2672-4355-BA1F-BB6569890287}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.Sample.Client", "samples\CommandQuery.Sample.Client\CommandQuery.Sample.Client.csproj", "{7C6D862F-63DF-4F03-8AC6-D57824C69CF8}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.Sample.Handlers", "samples\CommandQuery.Sample.Handlers\CommandQuery.Sample.Handlers.csproj", "{4A4F9ADD-F1CD-4377-8274-511C5221A87F}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.Sample.GoogleCloudFunctions", "samples\CommandQuery.Sample.GoogleCloudFunctions\CommandQuery.Sample.GoogleCloudFunctions.csproj", "{1DD7928F-24E7-4D21-BE69-39065CDAA5F7}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.Sample.GoogleCloudFunctions.Tests", "samples\CommandQuery.Sample.GoogleCloudFunctions.Tests\CommandQuery.Sample.GoogleCloudFunctions.Tests.csproj", "{20A4BF7B-F8B0-4CD6-BB63-F34338B95CD8}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.Sample.AspNetCore", "samples\CommandQuery.Sample.AspNetCore\CommandQuery.Sample.AspNetCore.csproj", "{C2A0A496-2F46-451F-BFA1-ECDDF9EE4414}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.Sample.AspNetCore.Tests", "samples\CommandQuery.Sample.AspNetCore.Tests\CommandQuery.Sample.AspNetCore.Tests.csproj", "{9499162C-FA52-4625-9628-B86952ED85C5}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.Sample.AzureFunctions", "samples\CommandQuery.Sample.AzureFunctions\CommandQuery.Sample.AzureFunctions.csproj", "{06C6F925-BACD-4F1F-8905-7F787330E980}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.Sample.AzureFunctions.Tests", "samples\CommandQuery.Sample.AzureFunctions.Tests\CommandQuery.Sample.AzureFunctions.Tests.csproj", "{2D223ADD-F2C9-4DB7-A68D-B04965AB2060}"
EndProject
Project("{2150E333-8FDC-42A3-9474-1A3956D46DE8}") = "HttpFiles", "HttpFiles", "{6F3519E3-F0E6-4DFA-86DD-86531529C512}"
	ProjectSection(SolutionItems) = preProject
		samples\HttpFiles\GetBarQuery.http = samples\HttpFiles\GetBarQuery.http
		samples\HttpFiles\GetQuuxQuery.http = samples\HttpFiles\GetQuuxQuery.http
		samples\HttpFiles\GetQuxQuery.http = samples\HttpFiles\GetQuxQuery.http
		samples\HttpFiles\http-client.env.json = samples\HttpFiles\http-client.env.json
		samples\HttpFiles\PostBarQuery.http = samples\HttpFiles\PostBarQuery.http
		samples\HttpFiles\PostBazCommand.http = samples\HttpFiles\PostBazCommand.http
		samples\HttpFiles\PostFooCommand.http = samples\HttpFiles\PostFooCommand.http
		samples\HttpFiles\PostQuuxQuery.http = samples\HttpFiles\PostQuuxQuery.http
		samples\HttpFiles\PostQuxQuery.http = samples\HttpFiles\PostQuxQuery.http
	EndProjectSection
EndProject
Global
	GlobalSection(SolutionConfigurationPlatforms) = preSolution
		Debug|Any CPU = Debug|Any CPU
		Release|Any CPU = Release|Any CPU
	EndGlobalSection
	GlobalSection(ProjectConfigurationPlatforms) = postSolution
		{FF932E21-17DE-4BC3-9E25-606502CAE58B}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{FF932E21-17DE-4BC3-9E25-606502CAE58B}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{FF932E21-17DE-4BC3-9E25-606502CAE58B}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{FF932E21-17DE-4BC3-9E25-606502CAE58B}.Release|Any CPU.Build.0 = Release|Any CPU
		{6AC1C95D-58A9-4D87-B303-EDF47BD35094}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{6AC1C95D-58A9-4D87-B303-EDF47BD35094}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{6AC1C95D-58A9-4D87-B303-EDF47BD35094}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{6AC1C95D-58A9-4D87-B303-EDF47BD35094}.Release|Any CPU.Build.0 = Release|Any CPU
		{B89EE6EB-2672-4355-BA1F-BB6569890287}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{B89EE6EB-2672-4355-BA1F-BB6569890287}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{B89EE6EB-2672-4355-BA1F-BB6569890287}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{B89EE6EB-2672-4355-BA1F-BB6569890287}.Release|Any CPU.Build.0 = Release|Any CPU
		{7C6D862F-63DF-4F03-8AC6-D57824C69CF8}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{7C6D862F-63DF-4F03-8AC6-D57824C69CF8}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{7C6D862F-63DF-4F03-8AC6-D57824C69CF8}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{7C6D862F-63DF-4F03-8AC6-D57824C69CF8}.Release|Any CPU.Build.0 = Release|Any CPU
		{4A4F9ADD-F1CD-4377-8274-511C5221A87F}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{4A4F9ADD-F1CD-4377-8274-511C5221A87F}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{4A4F9ADD-F1CD-4377-8274-511C5221A87F}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{4A4F9ADD-F1CD-4377-8274-511C5221A87F}.Release|Any CPU.Build.0 = Release|Any CPU
		{1DD7928F-24E7-4D21-BE69-39065CDAA5F7}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{1DD7928F-24E7-4D21-BE69-39065CDAA5F7}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{1DD7928F-24E7-4D21-BE69-39065CDAA5F7}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{1DD7928F-24E7-4D21-BE69-39065CDAA5F7}.Release|Any CPU.Build.0 = Release|Any CPU
		{20A4BF7B-F8B0-4CD6-BB63-F34338B95CD8}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{20A4BF7B-F8B0-4CD6-BB63-F34338B95CD8}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{20A4BF7B-F8B0-4CD6-BB63-F34338B95CD8}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{20A4BF7B-F8B0-4CD6-BB63-F34338B95CD8}.Release|Any CPU.Build.0 = Release|Any CPU
		{C2A0A496-2F46-451F-BFA1-ECDDF9EE4414}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{C2A0A496-2F46-451F-BFA1-ECDDF9EE4414}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{C2A0A496-2F46-451F-BFA1-ECDDF9EE4414}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{C2A0A496-2F46-451F-BFA1-ECDDF9EE4414}.Release|Any CPU.Build.0 = Release|Any CPU
		{9499162C-FA52-4625-9628-B86952ED85C5}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{9499162C-FA52-4625-9628-B86952ED85C5}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{9499162C-FA52-4625-9628-B86952ED85C5}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{9499162C-FA52-4625-9628-B86952ED85C5}.Release|Any CPU.Build.0 = Release|Any CPU
		{06C6F925-BACD-4F1F-8905-7F787330E980}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{06C6F925-BACD-4F1F-8905-7F787330E980}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{06C6F925-BACD-4F1F-8905-7F787330E980}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{06C6F925-BACD-4F1F-8905-7F787330E980}.Release|Any CPU.Build.0 = Release|Any CPU
		{2D223ADD-F2C9-4DB7-A68D-B04965AB2060}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{2D223ADD-F2C9-4DB7-A68D-B04965AB2060}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{2D223ADD-F2C9-4DB7-A68D-B04965AB2060}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{2D223ADD-F2C9-4DB7-A68D-B04965AB2060}.Release|Any CPU.Build.0 = Release|Any CPU
	EndGlobalSection
	GlobalSection(SolutionProperties) = preSolution
		HideSolutionNode = FALSE
	EndGlobalSection
	GlobalSection(ExtensibilityGlobals) = postSolution
		SolutionGuid = {FFB4AB08-1F28-416F-BF83-5A8EC1A6A6C6}
	EndGlobalSection
EndGlobal
```

## File: `CommandQuery.md`
```markdown
# CommandQuery ⚙️

[![build](https://github.com/hlaueriksson/CommandQuery/actions/workflows/build.yml/badge.svg)](https://github.com/hlaueriksson/CommandQuery/actions/workflows/build.yml) [![CodeFactor](https://codefactor.io/repository/github/hlaueriksson/commandquery/badge)](https://codefactor.io/repository/github/hlaueriksson/commandquery)

> Command Query Separation for .NET and C#

## Commands

> Commands change the state of a system but _[traditionally]_ do not return a value. They write (create, update, delete) data.

Commands implement the marker interface `ICommand` and command handlers implement `ICommandHandler<in TCommand>`.

```cs
public class FooCommand : ICommand
{
    public string Value { get; set; }
}

public class FooCommandHandler : ICommandHandler<FooCommand>
{
    private readonly ICultureService _cultureService;

    public FooCommandHandler(ICultureService cultureService)
    {
        _cultureService = cultureService;
    }

    public async Task HandleAsync(FooCommand command, CancellationToken cancellationToken)
    {
        if (string.IsNullOrEmpty(command.Value)) throw new FooCommandException("Value cannot be null or empty", 1337, "Try setting the value to 'en-US'");

        _cultureService.SetCurrentCulture(command.Value);

        await Task.CompletedTask;
    }
}
```

Commands can also return a result.

```cs
public class BazCommand : ICommand<Baz>
{
    public string Value { get; set; }
}

public class Baz
{
    public bool Success { get; set; }
}

public class BazCommandHandler : ICommandHandler<BazCommand, Baz>
{
    private readonly ICultureService _cultureService;

    public BazCommandHandler(ICultureService cultureService)
    {
        _cultureService = cultureService;
    }

    public async Task<Baz> HandleAsync(BazCommand command, CancellationToken cancellationToken)
    {
        var result = new Baz();

        try
        {
            _cultureService.SetCurrentCulture(command.Value);

            result.Success = true;
        }
        catch
        {
            // TODO: log
        }

        return await Task.FromResult(result);
    }
}
```

Commands with result implement the marker interface `ICommand<TResult>` and command handlers implement `ICommandHandler<in TCommand, TResult>`.

## Queries

> Queries return a result and do not change the observable state of the system (are free of side effects). They read and return data.

Queries implement the marker interface `IQuery<TResult>` and query handlers implement `IQueryHandler<in TQuery, TResult>`.

```cs
public class BarQuery : IQuery<Bar>
{
    public int Id { get; set; }
}

public class Bar
{
    public int Id { get; set; }

    public string Value { get; set; }
}

public class BarQueryHandler : IQueryHandler<BarQuery, Bar>
{
    private readonly IDateTimeProxy _dateTime;

    public BarQueryHandler(IDateTimeProxy dateTime)
    {
        _dateTime = dateTime;
    }

    public async Task<Bar> HandleAsync(BarQuery query, CancellationToken cancellationToken)
    {
        var result = new Bar { Id = query.Id, Value = _dateTime.Now.ToString("F") };

        return await Task.FromResult(result);
    }
}
```

## Samples

* [CommandQuery.Sample.Contracts](https://github.com/hlaueriksson/CommandQuery/tree/master/samples/CommandQuery.Sample.Contracts)
* [CommandQuery.Sample.Handlers](https://github.com/hlaueriksson/CommandQuery/tree/master/samples/CommandQuery.Sample.Handlers)
```

## File: `CommandQuery.sln`
```
﻿
Microsoft Visual Studio Solution File, Format Version 12.00
# Visual Studio Version 17
VisualStudioVersion = 17.4.33205.214
MinimumVisualStudioVersion = 10.0.40219.1
Project("{2150E333-8FDC-42A3-9474-1A3956D46DE8}") = "src", "src", "{382E6C39-5EF6-453D-88DC-9079E57A240E}"
EndProject
Project("{2150E333-8FDC-42A3-9474-1A3956D46DE8}") = "tests", "tests", "{4875335E-26C1-4D2A-80E9-4362C823DF3B}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery", "src\CommandQuery\CommandQuery.csproj", "{9631F3FE-6AF2-419B-B3F9-E1E6832BEF98}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.AspNetCore", "src\CommandQuery.AspNetCore\CommandQuery.AspNetCore.csproj", "{39AAD843-BC36-4A8E-92A7-6648C3FA7108}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.AzureFunctions", "src\CommandQuery.AzureFunctions\CommandQuery.AzureFunctions.csproj", "{230835A8-7181-4649-87BD-419492FED283}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.AWSLambda", "src\CommandQuery.AWSLambda\CommandQuery.AWSLambda.csproj", "{541A2BF0-A66C-445C-9DBE-2B2FD2513F18}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.Abstractions", "src\CommandQuery.Abstractions\CommandQuery.Abstractions.csproj", "{3AC1D062-7110-460F-AB04-AE77CD3087CC}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.Client", "src\CommandQuery.Client\CommandQuery.Client.csproj", "{321B804D-FE8E-4900-8A8A-C5B9FF52E6A5}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.Tests", "tests\CommandQuery.Tests\CommandQuery.Tests.csproj", "{B4491BED-B1E5-49CB-8138-763F549457D4}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.AspNetCore.Tests", "tests\CommandQuery.AspNetCore.Tests\CommandQuery.AspNetCore.Tests.csproj", "{FB355BA1-6923-4894-9BA2-B471A23EC3F5}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.AWSLambda.Tests", "tests\CommandQuery.AWSLambda.Tests\CommandQuery.AWSLambda.Tests.csproj", "{F81EEC3B-BB3D-456F-942B-6F610F977F53}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.AzureFunctions.Tests", "tests\CommandQuery.AzureFunctions.Tests\CommandQuery.AzureFunctions.Tests.csproj", "{BE082150-6F58-41C6-96F1-00F4FD827F4A}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.SystemTextJson", "src\CommandQuery.SystemTextJson\CommandQuery.SystemTextJson.csproj", "{A9946B7C-FB24-4873-9D56-549716BA51FE}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.Benchmark", "tests\CommandQuery.Benchmark\CommandQuery.Benchmark.csproj", "{55DAA02E-406A-41CC-89D7-CC97D71AA9CC}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.GoogleCloudFunctions", "src\CommandQuery.GoogleCloudFunctions\CommandQuery.GoogleCloudFunctions.csproj", "{361CA3A1-4E20-4C3F-AAE8-F059E533522E}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.GoogleCloudFunctions.Tests", "tests\CommandQuery.GoogleCloudFunctions.Tests\CommandQuery.GoogleCloudFunctions.Tests.csproj", "{292B144F-B56D-4594-9F85-8D8A519E5FD0}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "CommandQuery.Fail", "tests\CommandQuery.Fail\CommandQuery.Fail.csproj", "{AF2041C4-9DB5-4C0E-82C6-BC526C20D8E5}"
EndProject
Global
	GlobalSection(SolutionConfigurationPlatforms) = preSolution
		Debug|Any CPU = Debug|Any CPU
		Release|Any CPU = Release|Any CPU
	EndGlobalSection
	GlobalSection(ProjectConfigurationPlatforms) = postSolution
		{9631F3FE-6AF2-419B-B3F9-E1E6832BEF98}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{9631F3FE-6AF2-419B-B3F9-E1E6832BEF98}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{9631F3FE-6AF2-419B-B3F9-E1E6832BEF98}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{9631F3FE-6AF2-419B-B3F9-E1E6832BEF98}.Release|Any CPU.Build.0 = Release|Any CPU
		{39AAD843-BC36-4A8E-92A7-6648C3FA7108}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{39AAD843-BC36-4A8E-92A7-6648C3FA7108}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{39AAD843-BC36-4A8E-92A7-6648C3FA7108}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{39AAD843-BC36-4A8E-92A7-6648C3FA7108}.Release|Any CPU.Build.0 = Release|Any CPU
		{230835A8-7181-4649-87BD-419492FED283}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{230835A8-7181-4649-87BD-419492FED283}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{230835A8-7181-4649-87BD-419492FED283}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{230835A8-7181-4649-87BD-419492FED283}.Release|Any CPU.Build.0 = Release|Any CPU
		{541A2BF0-A66C-445C-9DBE-2B2FD2513F18}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{541A2BF0-A66C-445C-9DBE-2B2FD2513F18}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{541A2BF0-A66C-445C-9DBE-2B2FD2513F18}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{541A2BF0-A66C-445C-9DBE-2B2FD2513F18}.Release|Any CPU.Build.0 = Release|Any CPU
		{3AC1D062-7110-460F-AB04-AE77CD3087CC}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{3AC1D062-7110-460F-AB04-AE77CD3087CC}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{3AC1D062-7110-460F-AB04-AE77CD3087CC}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{3AC1D062-7110-460F-AB04-AE77CD3087CC}.Release|Any CPU.Build.0 = Release|Any CPU
		{321B804D-FE8E-4900-8A8A-C5B9FF52E6A5}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{321B804D-FE8E-4900-8A8A-C5B9FF52E6A5}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{321B804D-FE8E-4900-8A8A-C5B9FF52E6A5}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{321B804D-FE8E-4900-8A8A-C5B9FF52E6A5}.Release|Any CPU.Build.0 = Release|Any CPU
		{B4491BED-B1E5-49CB-8138-763F549457D4}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{B4491BED-B1E5-49CB-8138-763F549457D4}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{B4491BED-B1E5-49CB-8138-763F549457D4}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{B4491BED-B1E5-49CB-8138-763F549457D4}.Release|Any CPU.Build.0 = Release|Any CPU
		{FB355BA1-6923-4894-9BA2-B471A23EC3F5}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{FB355BA1-6923-4894-9BA2-B471A23EC3F5}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{FB355BA1-6923-4894-9BA2-B471A23EC3F5}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{FB355BA1-6923-4894-9BA2-B471A23EC3F5}.Release|Any CPU.Build.0 = Release|Any CPU
		{F81EEC3B-BB3D-456F-942B-6F610F977F53}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{F81EEC3B-BB3D-456F-942B-6F610F977F53}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{F81EEC3B-BB3D-456F-942B-6F610F977F53}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{F81EEC3B-BB3D-456F-942B-6F610F977F53}.Release|Any CPU.Build.0 = Release|Any CPU
		{BE082150-6F58-41C6-96F1-00F4FD827F4A}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{BE082150-6F58-41C6-96F1-00F4FD827F4A}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{BE082150-6F58-41C6-96F1-00F4FD827F4A}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{BE082150-6F58-41C6-96F1-00F4FD827F4A}.Release|Any CPU.Build.0 = Release|Any CPU
		{A9946B7C-FB24-4873-9D56-549716BA51FE}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{A9946B7C-FB24-4873-9D56-549716BA51FE}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{A9946B7C-FB24-4873-9D56-549716BA51FE}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{A9946B7C-FB24-4873-9D56-549716BA51FE}.Release|Any CPU.Build.0 = Release|Any CPU
		{55DAA02E-406A-41CC-89D7-CC97D71AA9CC}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{55DAA02E-406A-41CC-89D7-CC97D71AA9CC}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{55DAA02E-406A-41CC-89D7-CC97D71AA9CC}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{55DAA02E-406A-41CC-89D7-CC97D71AA9CC}.Release|Any CPU.Build.0 = Release|Any CPU
		{361CA3A1-4E20-4C3F-AAE8-F059E533522E}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{361CA3A1-4E20-4C3F-AAE8-F059E533522E}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{361CA3A1-4E20-4C3F-AAE8-F059E533522E}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{361CA3A1-4E20-4C3F-AAE8-F059E533522E}.Release|Any CPU.Build.0 = Release|Any CPU
		{292B144F-B56D-4594-9F85-8D8A519E5FD0}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{292B144F-B56D-4594-9F85-8D8A519E5FD0}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{292B144F-B56D-4594-9F85-8D8A519E5FD0}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{292B144F-B56D-4594-9F85-8D8A519E5FD0}.Release|Any CPU.Build.0 = Release|Any CPU
		{AF2041C4-9DB5-4C0E-82C6-BC526C20D8E5}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{AF2041C4-9DB5-4C0E-82C6-BC526C20D8E5}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{AF2041C4-9DB5-4C0E-82C6-BC526C20D8E5}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{AF2041C4-9DB5-4C0E-82C6-BC526C20D8E5}.Release|Any CPU.Build.0 = Release|Any CPU
	EndGlobalSection
	GlobalSection(SolutionProperties) = preSolution
		HideSolutionNode = FALSE
	EndGlobalSection
	GlobalSection(NestedProjects) = preSolution
		{9631F3FE-6AF2-419B-B3F9-E1E6832BEF98} = {382E6C39-5EF6-453D-88DC-9079E57A240E}
		{39AAD843-BC36-4A8E-92A7-6648C3FA7108} = {382E6C39-5EF6-453D-88DC-9079E57A240E}
		{230835A8-7181-4649-87BD-419492FED283} = {382E6C39-5EF6-453D-88DC-9079E57A240E}
		{541A2BF0-A66C-445C-9DBE-2B2FD2513F18} = {382E6C39-5EF6-453D-88DC-9079E57A240E}
		{3AC1D062-7110-460F-AB04-AE77CD3087CC} = {382E6C39-5EF6-453D-88DC-9079E57A240E}
		{321B804D-FE8E-4900-8A8A-C5B9FF52E6A5} = {382E6C39-5EF6-453D-88DC-9079E57A240E}
		{B4491BED-B1E5-49CB-8138-763F549457D4} = {4875335E-26C1-4D2A-80E9-4362C823DF3B}
		{FB355BA1-6923-4894-9BA2-B471A23EC3F5} = {4875335E-26C1-4D2A-80E9-4362C823DF3B}
		{F81EEC3B-BB3D-456F-942B-6F610F977F53} = {4875335E-26C1-4D2A-80E9-4362C823DF3B}
		{BE082150-6F58-41C6-96F1-00F4FD827F4A} = {4875335E-26C1-4D2A-80E9-4362C823DF3B}
		{A9946B7C-FB24-4873-9D56-549716BA51FE} = {382E6C39-5EF6-453D-88DC-9079E57A240E}
		{55DAA02E-406A-41CC-89D7-CC97D71AA9CC} = {4875335E-26C1-4D2A-80E9-4362C823DF3B}
		{361CA3A1-4E20-4C3F-AAE8-F059E533522E} = {382E6C39-5EF6-453D-88DC-9079E57A240E}
		{292B144F-B56D-4594-9F85-8D8A519E5FD0} = {4875335E-26C1-4D2A-80E9-4362C823DF3B}
		{AF2041C4-9DB5-4C0E-82C6-BC526C20D8E5} = {4875335E-26C1-4D2A-80E9-4362C823DF3B}
	EndGlobalSection
	GlobalSection(ExtensibilityGlobals) = postSolution
		SolutionGuid = {0D9F3EA4-8F77-4A20-9943-50764DB157AF}
	EndGlobalSection
EndGlobal
```

## File: `Directory.Build.props`
```
<Project>

  <PropertyGroup>
    <LangVersion>preview</LangVersion>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
    <PublishRepositoryUrl>true</PublishRepositoryUrl>
    <EmbedUntrackedSources>true</EmbedUntrackedSources>
    <AllowedOutputExtensionsInPackageBuildOutputFolder>$(AllowedOutputExtensionsInPackageBuildOutputFolder);.pdb</AllowedOutputExtensionsInPackageBuildOutputFolder>
  </PropertyGroup>

  <PropertyGroup Condition="'$(TF_BUILD)' == 'true'">
    <Deterministic>true</Deterministic>
    <ContinuousIntegrationBuild>true</ContinuousIntegrationBuild>
    <GeneratePackageOnBuild>true</GeneratePackageOnBuild>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Microsoft.SourceLink.GitHub" Version="8.0.0" PrivateAssets="All"/>
  </ItemGroup>

</Project>
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2019 Henrik Lau Eriksson

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

## File: `README.md`
```markdown
# CommandQuery<!-- omit in toc -->

[![build](https://github.com/hlaueriksson/CommandQuery/actions/workflows/build.yml/badge.svg)](https://github.com/hlaueriksson/CommandQuery/actions/workflows/build.yml)
[![CodeFactor](https://codefactor.io/repository/github/hlaueriksson/commandquery/badge)](https://codefactor.io/repository/github/hlaueriksson/commandquery)

[![CommandQuery](https://img.shields.io/nuget/v/CommandQuery.svg?label=CommandQuery)](https://www.nuget.org/packages/CommandQuery)
[![CommandQuery.Abstractions](https://img.shields.io/nuget/v/CommandQuery.Abstractions.svg?label=CommandQuery.Abstractions)](https://www.nuget.org/packages/CommandQuery.Abstractions)

[![CommandQuery.AspNetCore](https://img.shields.io/nuget/v/CommandQuery.AspNetCore.svg?label=CommandQuery.AspNetCore)](https://www.nuget.org/packages/CommandQuery.AspNetCore)
[![CommandQuery.AWSLambda](https://img.shields.io/nuget/v/CommandQuery.AWSLambda.svg?label=CommandQuery.AWSLambda)](https://www.nuget.org/packages/CommandQuery.AWSLambda)
[![CommandQuery.AzureFunctions](https://img.shields.io/nuget/v/CommandQuery.AzureFunctions.svg?label=CommandQuery.AzureFunctions)](https://www.nuget.org/packages/CommandQuery.AzureFunctions)
[![CommandQuery.GoogleCloudFunctions](https://img.shields.io/nuget/v/CommandQuery.GoogleCloudFunctions.svg?label=CommandQuery.GoogleCloudFunctions)](https://www.nuget.org/packages/CommandQuery.GoogleCloudFunctions)

[![CommandQuery.Client](https://img.shields.io/nuget/v/CommandQuery.Client.svg?label=CommandQuery.Client)](https://www.nuget.org/packages/CommandQuery.Client)

## Content<!-- omit in toc -->

- [Introduction](#introduction)
- [Packages](#packages)
  - [`CommandQuery` ⚙️](#commandquery-️)
  - [`CommandQuery.AspNetCore` 🌐](#commandqueryaspnetcore-)
  - [`CommandQuery.AWSLambda` ⚡](#commandqueryawslambda-)
  - [`CommandQuery.AzureFunctions` ⚡](#commandqueryazurefunctions-)
  - [`CommandQuery.GoogleCloudFunctions` ⚡](#commandquerygooglecloudfunctions-)
  - [`CommandQuery.Client` 🧰](#commandqueryclient-)
- [Upgrading](#upgrading)
- [Acknowledgements](#acknowledgements)

## Introduction

Command Query Separation (CQS) for .NET and C#

- Build services that separate the responsibility of commands and queries
- Focus on implementing the handlers for commands and queries
- Create APIs with less boilerplate code

Available for:

```txt
🌐 ASP.NET Core
⚡ AWS Lambda
⚡ Azure Functions
⚡ Google Cloud Functions
```

Command Query Separation?

> **Queries**: Return a result and do not change the observable state of the system (are free of side effects).
>
> **Commands**: Change the state of a system but do not return a value.
>
> — <cite>[Martin Fowler](http://martinfowler.com/bliki/CommandQuerySeparation.html)</cite>

In other words:

- Commands
  - Writes (create, update, delete) data
- Queries
  - Reads and returns data

The traditional approach that commands *do not return a value* is a bit inconvenient.

`CommandQuery` has a pragmatic take and supports both commands with and without result 👍

## Packages

### `CommandQuery` ⚙️

[![NuGet](https://img.shields.io/nuget/v/CommandQuery.svg) ![NuGet](https://img.shields.io/nuget/dt/CommandQuery.svg)](https://www.nuget.org/packages/CommandQuery)

> Command Query Separation for .NET

- 📃 README: [CommandQuery.md](../../../vault/archives/archive_legacy/hlaueriksson/CommandQuery.md)
- 💁 Samples:
  - [`CommandQuery.Sample.Contracts`](/samples/CommandQuery.Sample.Contracts)
  - [`CommandQuery.Sample.Handlers`](/samples/CommandQuery.Sample.Handlers)

### `CommandQuery.AspNetCore` 🌐

[![NuGet](https://img.shields.io/nuget/v/CommandQuery.AspNetCore.svg) ![NuGet](https://img.shields.io/nuget/dt/CommandQuery.AspNetCore.svg)](https://www.nuget.org/packages/CommandQuery.AspNetCore)

> Command Query Separation for ASP.NET Core

- 📃 README: [CommandQuery.AspNetCore.md](CommandQuery.AspNetCore.md)
- 💁 Samples:
  - [`CommandQuery.Sample.AspNetCore`](/samples/CommandQuery.Sample.AspNetCore)
  - [`CommandQuery.Sample.AspNetCore.Tests`](/samples/CommandQuery.Sample.AspNetCore.Tests)

### `CommandQuery.AWSLambda` ⚡

[![NuGet](https://img.shields.io/nuget/v/CommandQuery.AWSLambda.svg) ![NuGet](https://img.shields.io/nuget/dt/CommandQuery.AWSLambda.svg)](https://www.nuget.org/packages/CommandQuery.AWSLambda)

> Command Query Separation for AWS Lambda

- 📃 README: [CommandQuery.AWSLambda.md](CommandQuery.AWSLambda.md)
- 💁 Samples:
  - [`CommandQuery.Sample.AWSLambda`](/samples/CommandQuery.Sample.AWSLambda)
  - [`CommandQuery.Sample.AWSLambda.Tests`](/samples/CommandQuery.Sample.AWSLambda.Tests)

### `CommandQuery.AzureFunctions` ⚡

[![NuGet](https://img.shields.io/nuget/v/CommandQuery.AzureFunctions.svg) ![NuGet](https://img.shields.io/nuget/dt/CommandQuery.AzureFunctions.svg)](https://www.nuget.org/packages/CommandQuery.AzureFunctions)

> Command Query Separation for Azure Functions

- 📃 README: [CommandQuery.AzureFunctions.md](CommandQuery.AzureFunctions.md)
- 💁 Samples:
  - [`CommandQuery.Sample.AzureFunctions`](/samples/CommandQuery.Sample.AzureFunctions)
  - [`CommandQuery.Sample.AzureFunctions.Tests`](/samples/CommandQuery.Sample.AzureFunctions.Tests)

### `CommandQuery.GoogleCloudFunctions` ⚡

[![NuGet](https://img.shields.io/nuget/v/CommandQuery.GoogleCloudFunctions.svg) ![NuGet](https://img.shields.io/nuget/dt/CommandQuery.GoogleCloudFunctions.svg)](https://www.nuget.org/packages/CommandQuery.GoogleCloudFunctions)

> Command Query Separation for Google Cloud Functions

- 📃 README: [CommandQuery.GoogleCloudFunctions.md](CommandQuery.GoogleCloudFunctions.md)
- 💁 Samples:
  - [`CommandQuery.Sample.GoogleCloudFunctions`](/samples/CommandQuery.Sample.GoogleCloudFunctions)
  - [`CommandQuery.Sample.GoogleCloudFunctions.Tests`](/samples/CommandQuery.Sample.GoogleCloudFunctions.Tests)

### `CommandQuery.Client` 🧰

[![NuGet](https://img.shields.io/nuget/v/CommandQuery.Client.svg) ![NuGet](https://img.shields.io/nuget/dt/CommandQuery.Client.svg)](https://www.nuget.org/packages/CommandQuery.Client)

> Clients for CommandQuery APIs

- 📃 README: [CommandQuery.Client.md](CommandQuery.Client.md)
- 💁 Samples:
  - [`CommandQuery.Sample.Client`](/samples/CommandQuery.Sample.Client)

## Upgrading

> ⬆️ Upgrading from version `3.0.0` to `4.0.0`

Upgrade AspNetCore:

- Upgrade the project target framework to `net8.0`

Upgrade AWSLambda:

- Upgrade the project target framework to `net8.0`

Upgrade AzureFunctions:

- Upgrade the project target framework to `net8.0`
- Remove the `logger` argument from `HandleAsync`
- Consider to use the `HttpRequest` versions of `HandleAsync`

Upgrade GoogleCloudFunctions:

- Upgrade the project target framework to `net8.0`
- Remove the `logger` argument from `HandleAsync`

## Acknowledgements

Inspired by _Steven van Deursen_ blog posts:

- [Meanwhile... on the command side of my architecture](https://blogs.cuttingedge.it/steven/posts/2011/meanwhile-on-the-command-side-of-my-architecture/)
- [Meanwhile... on the query side of my architecture](https://blogs.cuttingedge.it/steven/posts/2011/meanwhile-on-the-query-side-of-my-architecture/)
```

## File: `coverage.bat`
```
dotnet test CommandQuery.sln --collect "Code Coverage" --settings coverage.runsettings
reportgenerator -reports:"tests\**\coverage.xml" -targetdir:"TestResults\Coverage" -reporttypes:Html -filefilters:"-*DotNetWorker*;-*NUnit*"
```

## File: `coverage.runsettings`
```
<?xml version="1.0" encoding="utf-8"?>
<RunSettings>
  <DataCollectionRunSettings>
    <DataCollectors>
      <DataCollector friendlyName="Code Coverage" uri="datacollector://Microsoft/CodeCoverage/2.0" assemblyQualifiedName="Microsoft.VisualStudio.Coverage.DynamicCoverageDataCollector, Microsoft.VisualStudio.TraceCollector, Version=11.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a">
        <Configuration>
          <CoverageFileName>coverage.xml</CoverageFileName>
          <Format>xml</Format>
          <IncludeTestAssembly>False</IncludeTestAssembly>
          <CodeCoverage>
            <EnableStaticNativeInstrumentation>False</EnableStaticNativeInstrumentation>
            <EnableDynamicNativeInstrumentation>False</EnableDynamicNativeInstrumentation>
          </CodeCoverage>
        </Configuration>
      </DataCollector>
    </DataCollectors>
  </DataCollectionRunSettings>
</RunSettings>
```

## File: `nuget-local.bat`
```
nuget init .\src\CommandQuery\bin\Release\ .\packages
nuget init .\src\CommandQuery.Abstractions\bin\Release\ .\packages
nuget init .\src\CommandQuery.AspNetCore\bin\Release\ .\packages
nuget init .\src\CommandQuery.AWSLambda\bin\Release\ .\packages
nuget init .\src\CommandQuery.AzureFunctions\bin\Release\ .\packages
nuget init .\src\CommandQuery.Client\bin\Release\ .\packages
nuget init .\src\CommandQuery.GoogleCloudFunctions\bin\Release\ .\packages
nuget init .\src\CommandQuery.SystemTextJson\bin\Release\ .\packages
```

## File: `pack.bat`
```
dotnet build CommandQuery.sln -c Release /p:TF_BUILD=true
```

## File: `stylecop.json`
```json
﻿{
  "$schema": "https://raw.githubusercontent.com/DotNetAnalyzers/StyleCopAnalyzers/master/StyleCop.Analyzers/StyleCop.Analyzers/Settings/stylecop.schema.json",
  "settings": {
    "documentationRules": {
      "documentInternalElements": false
    }
  }
}
```

## File: `test.bat`
```
dotnet test .\tests\CommandQuery.AspNetCore.Tests\CommandQuery.AspNetCore.Tests.csproj
dotnet test .\tests\CommandQuery.AWSLambda.Tests\CommandQuery.AWSLambda.Tests.csproj
dotnet test .\tests\CommandQuery.AzureFunctions.Tests\CommandQuery.AzureFunctions.Tests.csproj
dotnet test .\tests\CommandQuery.GoogleCloudFunctions.Tests\CommandQuery.GoogleCloudFunctions.Tests.csproj
dotnet test .\tests\CommandQuery.Tests\CommandQuery.Tests.csproj
```

## File: `samples/README.md`
```markdown
# CommandQuery Sample Code

This code has been written with *Visual Studio 2022*.

The unit tests are using [NUnit](https://github.com/nunit/nunit).

Try out the sample projects via the Postman Workspace:

* <https://www.postman.com/hlaueriksson/workspace/commandquery/overview>

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/30609-f711b607-24cc-4b17-955e-c24e8dbeab99?action=collection%2Ffork&collection-url=entityId%3D30609-f711b607-24cc-4b17-955e-c24e8dbeab99%26entityType%3Dcollection%26workspaceId%3D3787ce92-42c3-4e2f-9534-6ea64eb639b3)

Or via the `.http` files in Visual Studio:

* Open the `CommandQuery.Samples.sln`
* Open a `.http` file in the `HttpFiles` folder
* Select en environment in the HTTP Environments (F6) dropdown:
  * `AspNetCore` | `AWSLambda` | `AzureFunctions` | `GoogleCloudFunctions` | `http://localhost:7071`
* Click the `Send request` link
  * [Send an HTTP request](https://learn.microsoft.com/en-us/aspnet/core/test/http-files?view=aspnetcore-8.0#send-an-http-request)

![Visual Studio - HttpFiles](HttpFiles.png)

## Command + Query + Handlers

Sample code:

* `CommandQuery.Sample.Contracts`
* `CommandQuery.Sample.Handlers`

## ASP.NET Core

Sample code:

* `CommandQuery.Sample.AspNetCore`
* `CommandQuery.Sample.AspNetCore.Tests`

## AWS Lambda

Sample code:

* `CommandQuery.Sample.AWSLambda`
* `CommandQuery.Sample.AWSLambda.Tests`

## Azure Functions

Sample code:

* `CommandQuery.Sample.AzureFunctions`
* `CommandQuery.Sample.AzureFunctions.Tests`

## Google Cloud Functions

Sample code:

* `CommandQuery.Sample.GoogleCloudFunctions`
* `CommandQuery.Sample.GoogleCloudFunctions.Tests`

## Client

Sample code:

* `CommandQuery.Sample.Client`
```

## File: `samples/test.bat`
```
dotnet test .\CommandQuery.Sample.AspNetCore.Tests\CommandQuery.Sample.AspNetCore.Tests.csproj
dotnet test .\CommandQuery.Sample.AWSLambda.Tests\CommandQuery.Sample.AWSLambda.Tests.csproj
dotnet test .\CommandQuery.Sample.AzureFunctions.Tests\CommandQuery.Sample.AzureFunctions.Tests.csproj
dotnet test .\CommandQuery.Sample.GoogleCloudFunctions.Tests\CommandQuery.Sample.GoogleCloudFunctions.Tests.csproj
```

## File: `samples/CommandQuery.Sample.AWSLambda/Command.cs`
```csharp
using Amazon.Lambda.Annotations;
using Amazon.Lambda.Annotations.APIGateway;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using CommandQuery.AWSLambda;

namespace CommandQuery.Sample.AWSLambda;

public class Command(ICommandFunction commandFunction)
{
    [LambdaFunction(Policies = "AWSLambdaBasicExecutionRole", MemorySize = 256, Timeout = 30)]
    [RestApi(LambdaHttpMethod.Post, "/command/{commandName}")]
    public async Task<APIGatewayProxyResponse> Post(
        APIGatewayProxyRequest request,
        ILambdaContext context,
        string commandName) =>
        await commandFunction.HandleAsync(commandName, request, context.Logger);
}
```

## File: `samples/CommandQuery.Sample.AWSLambda/CommandQuery.Sample.AWSLambda.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <GenerateRuntimeConfigurationFiles>true</GenerateRuntimeConfigurationFiles>
    <AWSProjectType>Lambda</AWSProjectType>
    <!-- This property makes the build directory similar to a publish directory and helps the AWS .NET Lambda Mock Test Tool find project dependencies. -->
    <CopyLocalLockFileAssemblies>true</CopyLocalLockFileAssemblies>
    <!-- Generate ready to run images during publishing to improve cold start time. -->
    <PublishReadyToRun>true</PublishReadyToRun>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Amazon.Lambda.Annotations" Version="1.5.0" />
    <PackageReference Include="Amazon.Lambda.Core" Version="2.2.0" />
    <PackageReference Include="Amazon.Lambda.Serialization.SystemTextJson" Version="2.4.3" />
    <PackageReference Include="Amazon.Lambda.APIGatewayEvents" Version="2.7.0" />
    <PackageReference Include="CommandQuery.AWSLambda" Version="4.0.0" />
    <PackageReference Include="Microsoft.Extensions.DependencyInjection" Version="8.0.0" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\CommandQuery.Sample.Contracts\CommandQuery.Sample.Contracts.csproj" />
    <ProjectReference Include="..\CommandQuery.Sample.Handlers\CommandQuery.Sample.Handlers.csproj" />
  </ItemGroup>

</Project>
```

## File: `samples/CommandQuery.Sample.AWSLambda/Query.cs`
```csharp
using Amazon.Lambda.Annotations;
using Amazon.Lambda.Annotations.APIGateway;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using CommandQuery.AWSLambda;

namespace CommandQuery.Sample.AWSLambda
{
    public class Query(IQueryFunction queryFunction)
    {
        [LambdaFunction(Policies = "AWSLambdaBasicExecutionRole", MemorySize = 256, Timeout = 30)]
        [RestApi(LambdaHttpMethod.Get, "/query/{queryName}")]
        public async Task<APIGatewayProxyResponse> Get(
            APIGatewayProxyRequest request,
            ILambdaContext context,
            string queryName) =>
            await queryFunction.HandleAsync(queryName, request, context.Logger);

        [LambdaFunction(Policies = "AWSLambdaBasicExecutionRole", MemorySize = 256, Timeout = 30)]
        [RestApi(LambdaHttpMethod.Post, "/query/{queryName}")]
        public async Task<APIGatewayProxyResponse> Post(
            APIGatewayProxyRequest request,
            ILambdaContext context,
            string queryName) =>
            await queryFunction.HandleAsync(queryName, request, context.Logger);
    }
}
```

## File: `samples/CommandQuery.Sample.AWSLambda/Startup.cs`
```csharp
using Amazon.Lambda.Annotations;
using Amazon.Lambda.Core;
using CommandQuery.AWSLambda;
using CommandQuery.Sample.Contracts.Commands;
using CommandQuery.Sample.Contracts.Queries;
using CommandQuery.Sample.Handlers;
using CommandQuery.Sample.Handlers.Commands;
using CommandQuery.Sample.Handlers.Queries;
using Microsoft.Extensions.DependencyInjection;

[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace CommandQuery.Sample.AWSLambda;

[LambdaStartup]
public class Startup
{
    public void ConfigureServices(IServiceCollection services)
    {
        //services.AddSingleton(new JsonSerializerOptions(JsonSerializerDefaults.Web));

        // Add commands and queries
        services.AddCommandFunction(typeof(FooCommandHandler).Assembly, typeof(FooCommand).Assembly);
        services.AddQueryFunction(typeof(BarQueryHandler).Assembly, typeof(BarQuery).Assembly);

        // Add handler dependencies
        services.AddTransient<IDateTimeProxy, DateTimeProxy>();
        services.AddTransient<ICultureService, CultureService>();

        // Validation
        var serviceProvider = services.BuildServiceProvider();
        serviceProvider.GetService<ICommandProcessor>()!.AssertConfigurationIsValid();
        serviceProvider.GetService<IQueryProcessor>()!.AssertConfigurationIsValid();
    }
}
```

## File: `samples/CommandQuery.Sample.AWSLambda/aws-lambda-tools-defaults.json`
```json

{
    "Information" : [
        "This file provides default values for the deployment wizard inside Visual Studio and the AWS Lambda commands added to the .NET Core CLI.",
        "To learn more about the Lambda commands with the .NET Core CLI execute the following command at the command line in the project root directory.",
        "dotnet lambda help",
        "All the command line options for the Lambda command can be specified in this file."
    ],
    "profile"     : "Henrik Lau Eriksson",
    "region"      : "eu-central-1",
    "configuration" : "Release",
    "framework"     : "net8.0",
    "s3-prefix"     : "CommandQuery.Sample.AWSLambda/",
    "template"      : "serverless.template",
    "template-parameters" : "",
    "s3-bucket"           : "commandquery",
    "stack-name"          : "CommandQuery"
}
```

## File: `samples/CommandQuery.Sample.AWSLambda/serverless.template`
```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Transform": "AWS::Serverless-2016-10-31",
  "Description": "An AWS Serverless Application. This template is partially managed by Amazon.Lambda.Annotations (v1.5.0.0).",
  "Resources": {
    "CommandQuerySampleAWSLambdaCommandPostGenerated": {
      "Type": "AWS::Serverless::Function",
      "Metadata": {
        "Tool": "Amazon.Lambda.Annotations",
        "SyncedEvents": [
          "RootPost"
        ],
        "SyncedEventProperties": {
          "RootPost": [
            "Path",
            "Method"
          ]
        }
      },
      "Properties": {
        "Architectures": [
          "x86_64"
        ],
        "Handler": "CommandQuery.Sample.AWSLambda::CommandQuery.Sample.AWSLambda.Command_Post_Generated::Post",
        "Runtime": "dotnet8",
        "CodeUri": ".",
        "MemorySize": 256,
        "Timeout": 30,
        "Policies": [
          "AWSLambdaBasicExecutionRole"
        ],
        "PackageType": "Zip",
        "Events": {
          "RootPost": {
            "Type": "Api",
            "Properties": {
              "Path": "/command/{commandName}",
              "Method": "POST"
            }
          }
        }
      }
    },
    "CommandQuerySampleAWSLambdaQueryGetGenerated": {
      "Type": "AWS::Serverless::Function",
      "Metadata": {
        "Tool": "Amazon.Lambda.Annotations",
        "SyncedEvents": [
          "RootGet"
        ],
        "SyncedEventProperties": {
          "RootGet": [
            "Path",
            "Method"
          ]
        }
      },
      "Properties": {
        "Architectures": [
          "x86_64"
        ],
        "Handler": "CommandQuery.Sample.AWSLambda::CommandQuery.Sample.AWSLambda.Query_Get_Generated::Get",
        "Runtime": "dotnet8",
        "CodeUri": ".",
        "MemorySize": 256,
        "Timeout": 30,
        "Policies": [
          "AWSLambdaBasicExecutionRole"
        ],
        "PackageType": "Zip",
        "Events": {
          "RootGet": {
            "Type": "Api",
            "Properties": {
              "Path": "/query/{queryName}",
              "Method": "GET"
            }
          }
        }
      }
    },
    "CommandQuerySampleAWSLambdaQueryPostGenerated": {
      "Type": "AWS::Serverless::Function",
      "Metadata": {
        "Tool": "Amazon.Lambda.Annotations",
        "SyncedEvents": [
          "RootPost"
        ],
        "SyncedEventProperties": {
          "RootPost": [
            "Path",
            "Method"
          ]
        }
      },
      "Properties": {
        "Architectures": [
          "x86_64"
        ],
        "Handler": "CommandQuery.Sample.AWSLambda::CommandQuery.Sample.AWSLambda.Query_Post_Generated::Post",
        "Runtime": "dotnet8",
        "CodeUri": ".",
        "MemorySize": 256,
        "Timeout": 30,
        "Policies": [
          "AWSLambdaBasicExecutionRole"
        ],
        "PackageType": "Zip",
        "Events": {
          "RootPost": {
            "Type": "Api",
            "Properties": {
              "Path": "/query/{queryName}",
              "Method": "POST"
            }
          }
        }
      }
    }
  },
  "Outputs": {
    "ApiURL": {
      "Description": "API endpoint URL for Prod environment",
      "Value": {
        "Fn::Sub": "https://${ServerlessRestApi}.execute-api.${AWS::Region}.amazonaws.com/Prod/"
      }
    }
  }
}
```

## File: `samples/CommandQuery.Sample.AWSLambda/Properties/launchSettings.json`
```json
{
  "$schema": "http://json.schemastore.org/launchsettings.json",
  "profiles": {
    "Mock Lambda Test Tool": {
      "commandName": "Executable",
      "commandLineArgs": "--port 7071",
      "workingDirectory": ".\\bin\\$(Configuration)\\net8.0",
      "executablePath": "%USERPROFILE%\\.dotnet\\tools\\dotnet-lambda-test-tool-8.0.exe"
    }
  }
}
```

## File: `samples/CommandQuery.Sample.AWSLambda.Tests/CommandQuery.Sample.AWSLambda.Tests.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <IsTestProject>true</IsTestProject>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Amazon.Lambda.TestUtilities" Version="2.0.0" />
    <PackageReference Include="FluentAssertions" Version="6.12.0" />
    <PackageReference Include="Microsoft.NET.Test.Sdk" Version="17.10.0" />
    <PackageReference Include="NUnit" Version="4.1.0" />
    <PackageReference Include="NUnit3TestAdapter" Version="4.5.0">
      <PrivateAssets>all</PrivateAssets>
      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
    </PackageReference>
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\CommandQuery.Sample.AWSLambda\CommandQuery.Sample.AWSLambda.csproj" />
  </ItemGroup>

</Project>
```

## File: `samples/CommandQuery.Sample.AWSLambda.Tests/CommandTests.cs`
```csharp
using System.Text.Json;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.TestUtilities;
using CommandQuery.AWSLambda;
using CommandQuery.Sample.Contracts.Commands;
using FluentAssertions;
using Microsoft.Extensions.DependencyInjection;
using NUnit.Framework;

namespace CommandQuery.Sample.AWSLambda.Tests
{
    public class CommandTests
    {
        [SetUp]
        public void SetUp()
        {
            var serviceCollection = new ServiceCollection();
            new Startup().ConfigureServices(serviceCollection);
            var serviceProvider = serviceCollection.BuildServiceProvider();

            Subject = new Command(serviceProvider.GetRequiredService<ICommandFunction>());
            Context = new TestLambdaContext();
        }

        [Test]
        public async Task should_handle_command()
        {
            var response = await Subject.Post(GetRequest(new FooCommand { Value = "Foo" }), Context, "FooCommand");
            response.StatusCode.Should().Be(200);
        }

        [Test]
        public async Task should_handle_errors()
        {
            var response = await Subject.Post(GetRequest(new FooCommand()), Context, "FooCommand");
            response.ShouldBeError("Value cannot be null or empty");
        }

        static APIGatewayProxyRequest GetRequest(object body) => new() { Body = JsonSerializer.Serialize(body) };

        Command Subject = null!;
        TestLambdaContext Context = null!;
    }
}
```

## File: `samples/CommandQuery.Sample.AWSLambda.Tests/QueryTests.cs`
```csharp
using System.Text.Json;
using System.Web;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using Amazon.Lambda.TestUtilities;
using CommandQuery.AWSLambda;
using CommandQuery.Sample.Contracts.Queries;
using FluentAssertions;
using Microsoft.Extensions.DependencyInjection;
using NUnit.Framework;

namespace CommandQuery.Sample.AWSLambda.Tests
{
    public class QueryTests
    {
        [SetUp]
        public void SetUp()
        {
            var serviceCollection = new ServiceCollection();
            new Startup().ConfigureServices(serviceCollection);
            var serviceProvider = serviceCollection.BuildServiceProvider();

            Subject = new Query(serviceProvider.GetRequiredService<IQueryFunction>());
            Context = new TestLambdaContext();
        }

        [Test]
        public async Task should_handle_query_via_Post()
        {
            var response = await Subject.Post(GetRequest("POST", new BarQuery { Id = 1 }), Context, "BarQuery");
            var value = response.Body<Bar>()!;
            value.Id.Should().Be(1);
        }

        [Test]
        public async Task should_handle_query_via_Get()
        {
            var response = await Subject.Get(GetRequest("GET", "?Id=1"), Context, "BarQuery");
            var value = response.Body<Bar>()!;
            value.Id.Should().Be(1);
        }

        static APIGatewayProxyRequest GetRequest(string method, object body) => new()
        {
            HttpMethod = method,
            Body = JsonSerializer.Serialize(body),
        };

        static APIGatewayProxyRequest GetRequest(string method, string query)
        {
            var collection = HttpUtility.ParseQueryString(query);
            var parameters = collection.AllKeys.ToDictionary(k => k!, k => collection.GetValues(k)!.ToList() as IList<string>);

            return new()
            {
                HttpMethod = method,
                MultiValueQueryStringParameters = parameters
            };
        }

        Query Subject = null!;
        ILambdaContext Context = null!;
    }
}
```

## File: `samples/CommandQuery.Sample.AWSLambda.Tests/ShouldExtensions.cs`
```csharp
using System.Text.Json;
using Amazon.Lambda.APIGatewayEvents;
using CommandQuery.Sample.Contracts;
using FluentAssertions;

namespace CommandQuery.Sample.AWSLambda.Tests
{
    public static class ShouldExtensions
    {
        public static void ShouldBeError(this APIGatewayProxyResponse result, string message)
        {
            result.Should().NotBeNull();
            result.StatusCode.Should().NotBe(200);
            var value = result.Body<Error>()!;
            value.Should().NotBeNull();
            value.Message.Should().Be(message);
        }

        public static T? Body<T>(this APIGatewayProxyResponse result)
        {
            return JsonSerializer.Deserialize<T>(result.Body);
        }
    }
}
```

## File: `samples/CommandQuery.Sample.AspNetCore/.gitignore`
```
profile.arm.json
*Web Deploy.json
```

## File: `samples/CommandQuery.Sample.AspNetCore/CommandQuery.Sample.AspNetCore.csproj`
```
<Project Sdk="Microsoft.NET.Sdk.Web">

  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="CommandQuery.AspNetCore" Version="4.0.0" />
    <PackageReference Include="Swashbuckle.AspNetCore" Version="6.6.2" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\CommandQuery.Sample.Contracts\CommandQuery.Sample.Contracts.csproj" />
    <ProjectReference Include="..\CommandQuery.Sample.Handlers\CommandQuery.Sample.Handlers.csproj" />
  </ItemGroup>

  <ItemGroup>
    <InternalsVisibleTo Include="CommandQuery.Sample.AspNetCore.Tests" />
  </ItemGroup>

</Project>
```

## File: `samples/CommandQuery.Sample.AspNetCore/Program.cs`
```csharp
using CommandQuery;
using CommandQuery.AspNetCore;
using CommandQuery.Sample.Contracts.Commands;
using CommandQuery.Sample.Contracts.Queries;
using CommandQuery.Sample.Handlers;
using CommandQuery.Sample.Handlers.Commands;
using CommandQuery.Sample.Handlers.Queries;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// Add commands and queries
builder.Services.AddCommandControllers(typeof(FooCommandHandler).Assembly, typeof(FooCommand).Assembly);
builder.Services.AddQueryControllers(typeof(BarQueryHandler).Assembly, typeof(BarQuery).Assembly);

// Add handler dependencies
builder.Services.AddTransient<IDateTimeProxy, DateTimeProxy>();
builder.Services.AddTransient<ICultureService, CultureService>();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

// Validation
app.Services.GetService<ICommandProcessor>()!.AssertConfigurationIsValid();
app.Services.GetService<IQueryProcessor>()!.AssertConfigurationIsValid();

app.Run();
```

## File: `samples/CommandQuery.Sample.AspNetCore/appsettings.Development.json`
```json
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  }
}
```

## File: `samples/CommandQuery.Sample.AspNetCore/appsettings.json`
```json
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*"
}
```

## File: `samples/CommandQuery.Sample.AspNetCore/Properties/launchSettings.json`
```json
{
  "$schema": "http://json.schemastore.org/launchsettings.json",
  "iisSettings": {
    "windowsAuthentication": false,
    "anonymousAuthentication": true,
    "iisExpress": {
      "applicationUrl": "http://localhost:57857",
      "sslPort": 44362
    }
  },
  "profiles": {
    "CommandQuery.Sample.AspNetCore": {
      "commandName": "Project",
      "dotnetRunMessages": true,
      "launchBrowser": true,
      "launchUrl": "swagger",
      "applicationUrl": "https://localhost:7070;http://localhost:7071",
      "environmentVariables": {
        "ASPNETCORE_ENVIRONMENT": "Development"
      }
    },
    "IIS Express": {
      "commandName": "IISExpress",
      "launchBrowser": true,
      "launchUrl": "swagger",
      "environmentVariables": {
        "ASPNETCORE_ENVIRONMENT": "Development"
      }
    }
  }
}
```

## File: `samples/CommandQuery.Sample.AspNetCore/Properties/serviceDependencies.json`
```json
{
  "dependencies": {}
}
```

## File: `samples/CommandQuery.Sample.AspNetCore.Tests/CommandControllerTests.cs`
```csharp
using System.Net;
using System.Net.Http.Json;
using CommandQuery.Sample.Contracts.Commands;
using FluentAssertions;
using Microsoft.AspNetCore.Mvc.Testing;
using NUnit.Framework;

namespace CommandQuery.Sample.AspNetCore.Tests
{
    public class CommandControllerTests
    {
        [SetUp]
        public void SetUp()
        {
            Factory = new WebApplicationFactory<Program>();
            Client = Factory.CreateClient();
        }

        [TearDown]
        public void TearDown()
        {
            Client.Dispose();
            Factory.Dispose();
        }

        [Test]
        public async Task should_handle_command()
        {
            var response = await Client.PostAsJsonAsync("/api/command/FooCommand", new FooCommand { Value = "Foo" });
            response.StatusCode.Should().Be(HttpStatusCode.OK);
        }

        [Test]
        public async Task should_handle_errors()
        {
            var response = await Client.PostAsJsonAsync("/api/command/FooCommand", new FooCommand { Value = "" });
            await response.ShouldBeErrorAsync("Value cannot be null or empty");
        }

        WebApplicationFactory<Program> Factory = null!;
        HttpClient Client = null!;
    }
}
```

## File: `samples/CommandQuery.Sample.AspNetCore.Tests/CommandQuery.Sample.AspNetCore.Tests.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <IsTestProject>true</IsTestProject>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="FluentAssertions" Version="6.12.0" />
    <PackageReference Include="Microsoft.AspNetCore.Mvc.Testing" Version="8.0.7" />
    <PackageReference Include="Microsoft.NET.Test.Sdk" Version="17.10.0" />
    <PackageReference Include="NUnit" Version="4.1.0" />
    <PackageReference Include="NUnit3TestAdapter" Version="4.5.0">
      <PrivateAssets>all</PrivateAssets>
      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
    </PackageReference>
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\CommandQuery.Sample.AspNetCore\CommandQuery.Sample.AspNetCore.csproj" />
  </ItemGroup>

</Project>
```

## File: `samples/CommandQuery.Sample.AspNetCore.Tests/QueryControllerTests.cs`
```csharp
using System.Net.Http.Json;
using CommandQuery.Sample.Contracts.Queries;
using FluentAssertions;
using Microsoft.AspNetCore.Mvc.Testing;
using NUnit.Framework;

namespace CommandQuery.Sample.AspNetCore.Tests
{
    public class QueryControllerTests
    {
        [SetUp]
        public void SetUp()
        {
            Factory = new WebApplicationFactory<Program>();
            Client = Factory.CreateClient();
        }

        [TearDown]
        public void TearDown()
        {
            Client.Dispose();
            Factory.Dispose();
        }

        [Test]
        public async Task should_handle_query_via_Post()
        {
            var response = await Client.PostAsJsonAsync("/api/query/BarQuery", new BarQuery { Id = 1 });
            var value = await response.Content.ReadFromJsonAsync<Bar>();
            value!.Id.Should().Be(1);
        }

        [Test]
        public async Task should_handle_query_via_Get()
        {
            var response = await Client.GetAsync("/api/query/BarQuery?Id=1");
            var value = await response.Content.ReadFromJsonAsync<Bar>();
            value!.Id.Should().Be(1);
        }

        WebApplicationFactory<Program> Factory = null!;
        HttpClient Client = null!;
    }
}
```

## File: `samples/CommandQuery.Sample.AspNetCore.Tests/ShouldExtensions.cs`
```csharp
using System.Net;
using System.Net.Http.Json;
using CommandQuery.Sample.Contracts;
using FluentAssertions;
using Microsoft.AspNetCore.Http;

namespace CommandQuery.Sample.AspNetCore.Tests
{
    public static class ShouldExtensions
    {
        public static async Task ShouldBeErrorAsync(this HttpResponseMessage result, string message)
        {
            result.Should().NotBeNull();
            result.StatusCode.Should().NotBe(HttpStatusCode.OK);
            var value = await result.Content.ReadFromJsonAsync<Error>();
            value.Should().NotBeNull();
            value!.Message.Should().Be(message);
        }
    }
}
```

## File: `samples/CommandQuery.Sample.AzureFunctions/.gitignore`
```
## Ignore Visual Studio temporary files, build results, and
## files generated by popular Visual Studio add-ons.

profile.arm.json
storage1.arm.json
*Zip Deploy.json

# Azure Functions localsettings file
local.settings.json

# User-specific files
*.suo
*.user
*.userosscache
*.sln.docstates

# User-specific files (MonoDevelop/Xamarin Studio)
*.userprefs

# Build results
[Dd]ebug/
[Dd]ebugPublic/
[Rr]elease/
[Rr]eleases/
x64/
x86/
bld/
[Bb]in/
[Oo]bj/
[Ll]og/

# Visual Studio 2015 cache/options directory
.vs/
# Uncomment if you have tasks that create the project's static files in wwwroot
#wwwroot/

# MSTest test Results
[Tt]est[Rr]esult*/
[Bb]uild[Ll]og.*

# NUNIT
*.VisualState.xml
TestResult.xml

# Build Results of an ATL Project
[Dd]ebugPS/
[Rr]eleasePS/
dlldata.c

# DNX
project.lock.json
project.fragment.lock.json
artifacts/

*_i.c
*_p.c
*_i.h
*.ilk
*.meta
*.obj
*.pch
*.pdb
*.pgc
*.pgd
*.rsp
*.sbr
*.tlb
*.tli
*.tlh
*.tmp
*.tmp_proj
*.log
*.vspscc
*.vssscc
.builds
*.pidb
*.svclog
*.scc

# Chutzpah Test files
_Chutzpah*

# Visual C++ cache files
ipch/
*.aps
*.ncb
*.opendb
*.opensdf
*.sdf
*.cachefile
*.VC.db
*.VC.VC.opendb

# Visual Studio profiler
*.psess
*.vsp
*.vspx
*.sap

# TFS 2012 Local Workspace
$tf/

# Guidance Automation Toolkit
*.gpState

# ReSharper is a .NET coding add-in
_ReSharper*/
*.[Rr]e[Ss]harper
*.DotSettings.user

# JustCode is a .NET coding add-in
.JustCode

# TeamCity is a build add-in
_TeamCity*

# DotCover is a Code Coverage Tool
*.dotCover

# NCrunch
_NCrunch_*
.*crunch*.local.xml
nCrunchTemp_*

# MightyMoose
*.mm.*
AutoTest.Net/

# Web workbench (sass)
.sass-cache/

# Installshield output folder
[Ee]xpress/

# DocProject is a documentation generator add-in
DocProject/buildhelp/
DocProject/Help/*.HxT
DocProject/Help/*.HxC
DocProject/Help/*.hhc
DocProject/Help/*.hhk
DocProject/Help/*.hhp
DocProject/Help/Html2
DocProject/Help/html

# Click-Once directory
publish/

# Publish Web Output
*.[Pp]ublish.xml
*.azurePubxml
# TODO: Comment the next line if you want to checkin your web deploy settings
# but database connection strings (with potential passwords) will be unencrypted
#*.pubxml
*.publishproj

# Microsoft Azure Web App publish settings. Comment the next line if you want to
# checkin your Azure Web App publish settings, but sensitive information contained
# in these scripts will be unencrypted
PublishScripts/

# NuGet Packages
*.nupkg
# The packages folder can be ignored because of Package Restore
**/packages/*
# except build/, which is used as an MSBuild target.
!**/packages/build/
# Uncomment if necessary however generally it will be regenerated when needed
#!**/packages/repositories.config
# NuGet v3's project.json files produces more ignoreable files
*.nuget.props
*.nuget.targets

# Microsoft Azure Build Output
csx/
*.build.csdef

# Microsoft Azure Emulator
ecf/
rcf/

# Windows Store app package directories and files
AppPackages/
BundleArtifacts/
Package.StoreAssociation.xml
_pkginfo.txt

# Visual Studio cache files
# files ending in .cache can be ignored
*.[Cc]ache
# but keep track of directories ending in .cache
!*.[Cc]ache/

# Others
ClientBin/
~$*
*~
*.dbmdl
*.dbproj.schemaview
*.jfm
*.pfx
*.publishsettings
node_modules/
orleans.codegen.cs

# Since there are multiple workflows, uncomment next line to ignore bower_components
# (https://github.com/github/gitignore/pull/1529#issuecomment-104372622)
#bower_components/

# RIA/Silverlight projects
Generated_Code/

# Backup & report files from converting an old project file
# to a newer Visual Studio version. Backup files are not needed,
# because we have git ;-)
_UpgradeReport_Files/
Backup*/
UpgradeLog*.XML
UpgradeLog*.htm

# SQL Server files
*.mdf
*.ldf

# Business Intelligence projects
*.rdl.data
*.bim.layout
*.bim_*.settings

# Microsoft Fakes
FakesAssemblies/

# GhostDoc plugin setting file
*.GhostDoc.xml

# Node.js Tools for Visual Studio
.ntvs_analysis.dat

# Visual Studio 6 build log
*.plg

# Visual Studio 6 workspace options file
*.opt

# Visual Studio LightSwitch build output
**/*.HTMLClient/GeneratedArtifacts
**/*.DesktopClient/GeneratedArtifacts
**/*.DesktopClient/ModelManifest.xml
**/*.Server/GeneratedArtifacts
**/*.Server/ModelManifest.xml
_Pvt_Extensions

# Paket dependency manager
.paket/paket.exe
paket-files/

# FAKE - F# Make
.fake/

# JetBrains Rider
.idea/
*.sln.iml

# CodeRush
.cr/

# Python Tools for Visual Studio (PTVS)
__pycache__/
*.pyc
```

## File: `samples/CommandQuery.Sample.AzureFunctions/Command.cs`
```csharp
using CommandQuery.AzureFunctions;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.Functions.Worker;

namespace CommandQuery.Sample.AzureFunctions
{
    public class Command(ICommandFunction commandFunction)
    {
        [Function(nameof(Command))]
        public async Task<IActionResult> Run(
            [HttpTrigger(AuthorizationLevel.Anonymous, "post", Route = "command/{commandName}")] HttpRequest req,
            FunctionContext context,
            string commandName) =>
            await commandFunction.HandleAsync(commandName, req, context.CancellationToken);
    }
}
```

## File: `samples/CommandQuery.Sample.AzureFunctions/CommandQuery.Sample.AzureFunctions.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <AzureFunctionsVersion>v4</AzureFunctionsVersion>
    <OutputType>Exe</OutputType>
  </PropertyGroup>

  <ItemGroup>
    <FrameworkReference Include="Microsoft.AspNetCore.App" />
    <PackageReference Include="CommandQuery.AzureFunctions" Version="4.0.0" />
    <PackageReference Include="Microsoft.Azure.Functions.Worker" Version="1.22.0" />
    <PackageReference Include="Microsoft.Azure.Functions.Worker.Extensions.Http" Version="3.2.0" />
    <PackageReference Include="Microsoft.Azure.Functions.Worker.Extensions.Http.AspNetCore" Version="1.3.2" />
    <PackageReference Include="Microsoft.Azure.Functions.Worker.Sdk" Version="1.17.3" />
    <PackageReference Include="Microsoft.ApplicationInsights.WorkerService" Version="2.22.0" />
    <PackageReference Include="Microsoft.Azure.Functions.Worker.ApplicationInsights" Version="1.2.0" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\CommandQuery.Sample.Contracts\CommandQuery.Sample.Contracts.csproj" />
    <ProjectReference Include="..\CommandQuery.Sample.Handlers\CommandQuery.Sample.Handlers.csproj" />
  </ItemGroup>

  <ItemGroup>
    <None Update="host.json">
      <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
    </None>
    <None Update="local.settings.json">
      <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
      <CopyToPublishDirectory>Never</CopyToPublishDirectory>
    </None>
  </ItemGroup>

  <ItemGroup>
    <Using Include="System.Threading.ExecutionContext" Alias="ExecutionContext" />
  </ItemGroup>

</Project>
```

## File: `samples/CommandQuery.Sample.AzureFunctions/Program.cs`
```csharp
using CommandQuery;
using CommandQuery.AzureFunctions;
using CommandQuery.Sample.Contracts.Commands;
using CommandQuery.Sample.Contracts.Queries;
using CommandQuery.Sample.Handlers;
using CommandQuery.Sample.Handlers.Commands;
using CommandQuery.Sample.Handlers.Queries;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

var host = new HostBuilder()
    .ConfigureFunctionsWebApplication()
    .ConfigureServices(ConfigureServices)
    .Build();

// Validation
host.Services.GetService<ICommandProcessor>()!.AssertConfigurationIsValid();
host.Services.GetService<IQueryProcessor>()!.AssertConfigurationIsValid();

host.Run();

public static partial class Program
{
    public static void ConfigureServices(IServiceCollection services)
    {
        services.AddApplicationInsightsTelemetryWorkerService();
        services.ConfigureFunctionsApplicationInsights();

        services
            //.AddSingleton(new JsonSerializerOptions(JsonSerializerDefaults.Web));

            // Add commands and queries
            .AddCommandFunction(typeof(FooCommandHandler).Assembly, typeof(FooCommand).Assembly)
            .AddQueryFunction(typeof(BarQueryHandler).Assembly, typeof(BarQuery).Assembly)

            // Add handler dependencies
            .AddTransient<IDateTimeProxy, DateTimeProxy>()
            .AddTransient<ICultureService, CultureService>();
    }
}
```

## File: `samples/CommandQuery.Sample.AzureFunctions/Query.cs`
```csharp
using CommandQuery.AzureFunctions;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.Functions.Worker;

namespace CommandQuery.Sample.AzureFunctions
{
    public class Query(IQueryFunction queryFunction)
    {
        [Function(nameof(Query))]
        public async Task<IActionResult> Run(
            [HttpTrigger(AuthorizationLevel.Anonymous, "get", "post", Route = "query/{queryName}")] HttpRequest req,
            FunctionContext context,
            string queryName) =>
            await queryFunction.HandleAsync(queryName, req, context.CancellationToken);
    }
}
```

## File: `samples/CommandQuery.Sample.AzureFunctions/host.json`
```json
{
    "version": "2.0",
    "logging": {
        "applicationInsights": {
            "samplingSettings": {
                "isEnabled": true,
                "excludedTypes": "Request"
            },
            "enableLiveMetricsFilters": true
        }
    }
}
```

## File: `samples/CommandQuery.Sample.AzureFunctions/Properties/launchSettings.json`
```json
{
  "$schema": "http://json.schemastore.org/launchsettings.json",
  "profiles": {
    "CommandQuery.Sample.AzureFunctions": {
      "commandName": "Project",
      "commandLineArgs": "--port 7071",
      "launchBrowser": false
    }
  }
}
```

## File: `samples/CommandQuery.Sample.AzureFunctions/Properties/serviceDependencies.CommandQuerySampleAzureFunctions.json`
```json
{
  "dependencies": {
    "storage1": {
      "resourceId": "/subscriptions/[parameters('subscriptionId')]/resourceGroups/[parameters('resourceGroupName')]/providers/Microsoft.Storage/storageAccounts/commandquery",
      "type": "storage.azure",
      "connectionId": "AzureWebJobsStorage"
    }
  }
}
```

## File: `samples/CommandQuery.Sample.AzureFunctions/Properties/serviceDependencies.json`
```json
{
  "dependencies": {
    "appInsights1": {
      "type": "appInsights"
    },
    "storage1": {
      "type": "storage",
      "connectionId": "AzureWebJobsStorage"
    }
  }
}
```

## File: `samples/CommandQuery.Sample.AzureFunctions/Properties/serviceDependencies.local.json`
```json
{
  "dependencies": {
    "appInsights1": {
      "type": "appInsights.sdk"
    }
  }
}
```

## File: `samples/CommandQuery.Sample.AzureFunctions.Tests/CommandQuery.Sample.AzureFunctions.Tests.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="FluentAssertions" Version="6.12.0" />
    <PackageReference Include="Microsoft.NET.Test.Sdk" Version="17.10.0" />
    <PackageReference Include="Moq" Version="4.20.70" />
    <PackageReference Include="NUnit" Version="4.1.0" />
    <PackageReference Include="NUnit3TestAdapter" Version="4.5.0">
      <PrivateAssets>all</PrivateAssets>
      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
    </PackageReference>
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\CommandQuery.Sample.AzureFunctions\CommandQuery.Sample.AzureFunctions.csproj" />
  </ItemGroup>

</Project>
```

## File: `samples/CommandQuery.Sample.AzureFunctions.Tests/CommandTests.cs`
```csharp
using System.Text;
using System.Text.Json;
using CommandQuery.AzureFunctions;
using CommandQuery.Sample.Contracts.Commands;
using FluentAssertions;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc.Infrastructure;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.DependencyInjection;
using Moq;
using NUnit.Framework;

namespace CommandQuery.Sample.AzureFunctions.Tests
{
    public class CommandTests
    {
        [SetUp]
        public void SetUp()
        {
            var serviceCollection = new ServiceCollection();
            Program.ConfigureServices(serviceCollection);
            var serviceProvider = serviceCollection.BuildServiceProvider();

            Subject = new Command(serviceProvider.GetRequiredService<ICommandFunction>());

            var context = new Mock<FunctionContext>();
            context.SetupProperty(c => c.InstanceServices, serviceProvider);
            Context = context.Object;
        }

        [Test]
        public async Task should_handle_command()
        {
            var result = await Subject.Run(GetRequest(new FooCommand { Value = "Foo" }), Context, "FooCommand");
            result.As<IStatusCodeActionResult>().StatusCode.Should().Be(200);
        }

        [Test]
        public async Task should_handle_errors()
        {
            var result = await Subject.Run(GetRequest(new FooCommand()), Context, "FooCommand");
            result.ShouldBeError("Value cannot be null or empty");
        }

        HttpRequest GetRequest(object body)
        {
            var request = new Mock<HttpRequest>();
            request.Setup(r => r.Body).Returns(new MemoryStream(Encoding.UTF8.GetBytes(JsonSerializer.Serialize(body))));
            return request.Object;
        }

        Command Subject = null!;
        FunctionContext Context = null!;
    }
}
```

## File: `samples/CommandQuery.Sample.AzureFunctions.Tests/QueryTests.cs`
```csharp
using System.Text;
using System.Text.Json;
using System.Web;
using CommandQuery.AzureFunctions;
using CommandQuery.Sample.Contracts.Queries;
using FluentAssertions;
using Microsoft.AspNetCore.Http;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Primitives;
using Moq;
using NUnit.Framework;

namespace CommandQuery.Sample.AzureFunctions.Tests
{
    public class QueryTests
    {
        [SetUp]
        public void SetUp()
        {
            var serviceCollection = new ServiceCollection();
            Program.ConfigureServices(serviceCollection);
            var serviceProvider = serviceCollection.BuildServiceProvider();

            Subject = new Query(serviceProvider.GetRequiredService<IQueryFunction>());

            var context = new Mock<FunctionContext>();
            context.SetupProperty(c => c.InstanceServices, serviceProvider);
            Context = context.Object;
        }

        [Test]
        public async Task should_handle_query_via_Post()
        {
            var result = await Subject.Run(GetRequest("POST", new BarQuery { Id = 1 }), Context, "BarQuery");
            var value = result.Value<Bar>()!;
            value.Id.Should().Be(1);
        }

        [Test]
        public async Task should_handle_query_via_Get()
        {
            var result = await Subject.Run(GetRequest("GET", "?Id=1"), Context, "BarQuery");
            var value = result.Value<Bar>()!;
            value.Id.Should().Be(1);
        }

        static HttpRequest GetRequest(string method, object body)
        {
            var request = new Mock<HttpRequest>();
            request.Setup(r => r.Method).Returns(method);
            request.Setup(r => r.Body).Returns(new MemoryStream(Encoding.UTF8.GetBytes(JsonSerializer.Serialize(body))));
            return request.Object;
        }

        static HttpRequest GetRequest(string method, string query)
        {
            var collection = HttpUtility.ParseQueryString(query);
            var store = collection.AllKeys.ToDictionary(k => k!, k => new StringValues(collection.GetValues(k)));

            var request = new Mock<HttpRequest>();
            request.Setup(r => r.Method).Returns(method);
            request.Setup(r => r.Query).Returns(new QueryCollection(store));
            return request.Object;
        }

        Query Subject = null!;
        FunctionContext Context = null!;
    }
}
```

## File: `samples/CommandQuery.Sample.AzureFunctions.Tests/ShouldExtensions.cs`
```csharp
using FluentAssertions;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Infrastructure;

namespace CommandQuery.Sample.AzureFunctions.Tests
{
    public static class ShouldExtensions
    {
        public static void ShouldBeError(this IActionResult result, string message)
        {
            result.Should().NotBeNull();
            result.As<IStatusCodeActionResult>().StatusCode.Should().NotBe(200);
            var value = result.Value<IError>()!;
            value.Should().NotBeNull();
            value.Message.Should().Be(message);
        }

        public static T As<T>(this IActionResult result)
        {
            return (T)result;
        }

        public static T? Value<T>(this IActionResult result) where T : class
        {
            return result.As<ObjectResult>().Value as T;
        }
    }
}
```

## File: `samples/CommandQuery.Sample.Client/CommandQuery.Sample.Client.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="CommandQuery.Client" Version="4.0.0" />
    <PackageReference Include="Microsoft.Extensions.Http.Polly" Version="8.0.7" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\CommandQuery.Sample.Contracts\CommandQuery.Sample.Contracts.csproj" />
  </ItemGroup>

</Project>
```

## File: `samples/CommandQuery.Sample.Client/LoggingHandler.cs`
```csharp
namespace CommandQuery.Sample.Client
{
    public class LoggingHandler : DelegatingHandler
    {
        protected override async Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
        {
            Console.WriteLine(request.ToString());
            if (request.Content != null) Console.WriteLine(await request.Content.ReadAsStringAsync(cancellationToken));

            var response = await base.SendAsync(request, cancellationToken);

            if (!response.IsSuccessStatusCode) Console.ForegroundColor = ConsoleColor.Red;

            Console.WriteLine(response.ToString());
            Console.WriteLine(await response.Content.ReadAsStringAsync(cancellationToken));
            Console.ResetColor();
            Console.WriteLine();

            return response;
        }
    }
}
```

## File: `samples/CommandQuery.Sample.Client/Program.cs`
```csharp
using CommandQuery.Client;
using CommandQuery.Sample.Contracts.Commands;
using CommandQuery.Sample.Contracts.Queries;
using Microsoft.Extensions.DependencyInjection;
using Polly;
using Polly.Extensions.Http;

namespace CommandQuery.Sample.Client
{
    public class Program
    {
        private static IServiceProvider _serviceProvider = null!;

        public static async Task Main(string[] args)
        {
            ConfigureServices(args.Any() ? args : new[] { "http://localhost:7071/api" });

            var commandClient = _serviceProvider.GetRequiredService<ICommandClient>();
            var queryClient = _serviceProvider.GetRequiredService<IQueryClient>();

            await commandClient.PostAsync(new FooCommand { Value = "en-GB" }); // Command without result
            await commandClient.PostAsync(new BazCommand { Value = "en-GB" }); // Command with result

            await queryClient.PostAsync(new BarQuery { Id = 1 }); // Query via POST
            await queryClient.GetAsync(new BarQuery { Id = 1 }); // Query via GET
            await queryClient.GetAsync(new QuxQuery { Ids = new[] { Guid.NewGuid(), Guid.NewGuid() } }); // Query with enumerable property
            await queryClient.GetAsync(new QuuxQuery { Id = 1, Corge = new Corge { DateTime = DateTime.UtcNow, Grault = new Grault { DayOfWeek = DayOfWeek.Monday } } }); // Query with nested property
        }

        static void ConfigureServices(params string[] baseUrls)
        {
            var commandUrl = baseUrls.Length == 1 ? $"{baseUrls.Single()}/command/" : baseUrls.First();
            var queryUrl = baseUrls.Length == 1 ? $"{baseUrls.Single()}/query/" : baseUrls.Last();

            var services = new ServiceCollection();
            services.AddTransient<LoggingHandler>();
            //services.AddSingleton(new JsonSerializerOptions(JsonSerializerDefaults.Web));
            services.AddHttpClient<ICommandClient, CommandClient>(x =>
                {
                    x.BaseAddress = new Uri(commandUrl);
                    x.Timeout = TimeSpan.FromSeconds(10);
                })
                .AddHttpMessageHandler<LoggingHandler>()
                .AddPolicyHandler(GetRetryPolicy());
            services.AddHttpClient<IQueryClient, QueryClient>(x =>
                {
                    x.BaseAddress = new Uri(queryUrl);
                    x.Timeout = TimeSpan.FromSeconds(10);
                })
                .AddHttpMessageHandler<LoggingHandler>()
                .AddPolicyHandler(GetRetryPolicy());

            _serviceProvider = services.BuildServiceProvider();
        }

        static IAsyncPolicy<HttpResponseMessage> GetRetryPolicy()
        {
            return HttpPolicyExtensions
                .HandleTransientHttpError()
                .OrResult(msg => msg.StatusCode == System.Net.HttpStatusCode.NotFound)
                .WaitAndRetryAsync(6, retryAttempt => TimeSpan.FromSeconds(Math.Pow(2, retryAttempt)));
        }
    }
}
```

## File: `samples/CommandQuery.Sample.Client/run.bat`
```
dotnet run https://commandquerysampleaspnetcore.azurewebsites.net/api
dotnet run https://u3rkew3obh.execute-api.eu-central-1.amazonaws.com/Prod
dotnet run https://commandquerysampleazurefunctions.azurewebsites.net/api
dotnet run https://europe-north1-solid-antler-215713.cloudfunctions.net/commandquery-sample-googlecloudfunctions-command/api/command/ https://europe-north1-solid-antler-215713.cloudfunctions.net/commandquery-sample-googlecloudfunctions-query/api/query/
```

## File: `samples/CommandQuery.Sample.Contracts/.editorconfig`
```
[*.cs]
dotnet_diagnostic.CS8618.severity = none
```

## File: `samples/CommandQuery.Sample.Contracts/CommandQuery.Sample.Contracts.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>netstandard2.0</TargetFramework>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="CommandQuery.Abstractions" Version="4.0.0" />
  </ItemGroup>

</Project>
```

## File: `samples/CommandQuery.Sample.Contracts/Error.cs`
```csharp
namespace CommandQuery.Sample.Contracts
{
    public class Error : IError
    {
        public string Message { get; set; }
        public Dictionary<string, object> Details { get; set; }
    }
}
```

## File: `samples/CommandQuery.Sample.Contracts/Commands/BazCommand.cs`
```csharp
namespace CommandQuery.Sample.Contracts.Commands
{
    public class BazCommand : ICommand<Baz>
    {
        public string Value { get; set; }
    }

    public class Baz
    {
        public bool Success { get; set; }
    }
}
```

## File: `samples/CommandQuery.Sample.Contracts/Commands/FooCommand.cs`
```csharp
namespace CommandQuery.Sample.Contracts.Commands
{
    public class FooCommand : ICommand
    {
        public string Value { get; set; }
    }
}
```

## File: `samples/CommandQuery.Sample.Contracts/Queries/BarQuery.cs`
```csharp
namespace CommandQuery.Sample.Contracts.Queries
{
    public class BarQuery : IQuery<Bar>
    {
        public int Id { get; set; }
    }

    public class Bar
    {
        public int Id { get; set; }

        public string Value { get; set; }
    }
}
```

## File: `samples/CommandQuery.Sample.Contracts/Queries/QuuxQuery.cs`
```csharp
namespace CommandQuery.Sample.Contracts.Queries
{
    public class QuuxQuery : IQuery<Quux>
    {
        public long? Id { get; set; }
        public Corge Corge { get; set; }
    }

    public class Corge
    {
        public DateTime DateTime { get; set; }
        public Grault Grault { get; set; }
    }

    public class Grault
    {
        public DayOfWeek DayOfWeek { get; set; }
    }

    public class Quux
    {
        public long Id { get; set; }
        public Corge Corge { get; set; }
    }
}
```

## File: `samples/CommandQuery.Sample.Contracts/Queries/QuxQuery.cs`
```csharp
namespace CommandQuery.Sample.Contracts.Queries
{
    public class QuxQuery : IQuery<Qux[]>
    {
        public Guid[] Ids { get; set; }
    }

    public class Qux
    {
        public Guid Id { get; set; }

        public string Value { get; set; }
    }
}
```

## File: `samples/CommandQuery.Sample.GoogleCloudFunctions/Command.cs`
```csharp
using CommandQuery.GoogleCloudFunctions;
using Google.Cloud.Functions.Framework;
using Google.Cloud.Functions.Hosting;
using Microsoft.AspNetCore.Http;

namespace CommandQuery.Sample.GoogleCloudFunctions
{
    [FunctionsStartup(typeof(Startup))]
    public class Command(ICommandFunction commandFunction) : IHttpFunction
    {
        public async Task HandleAsync(HttpContext context)
        {
            var commandName = context.Request.Path.Value!.Substring("/api/command/".Length);
            await commandFunction.HandleAsync(commandName, context, context.RequestAborted);
        }
    }
}
```

## File: `samples/CommandQuery.Sample.GoogleCloudFunctions/CommandQuery.Sample.GoogleCloudFunctions.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="CommandQuery.GoogleCloudFunctions" Version="4.0.0" />
    <PackageReference Include="Google.Cloud.Functions.Hosting" Version="2.2.1" />
    <None Include="appsettings*.json" CopyToOutputDirectory="PreserveNewest" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\CommandQuery.Sample.Contracts\CommandQuery.Sample.Contracts.csproj" />
    <ProjectReference Include="..\CommandQuery.Sample.Handlers\CommandQuery.Sample.Handlers.csproj" />
  </ItemGroup>

</Project>
```

## File: `samples/CommandQuery.Sample.GoogleCloudFunctions/Query.cs`
```csharp
using CommandQuery.GoogleCloudFunctions;
using Google.Cloud.Functions.Framework;
using Google.Cloud.Functions.Hosting;
using Microsoft.AspNetCore.Http;

namespace CommandQuery.Sample.GoogleCloudFunctions
{
    [FunctionsStartup(typeof(Startup))]
    public class Query(IQueryFunction queryFunction) : IHttpFunction
    {
        public async Task HandleAsync(HttpContext context)
        {
            var queryName = context.Request.Path.Value!.Substring("/api/query/".Length);
            await queryFunction.HandleAsync(queryName, context, context.RequestAborted);
        }
    }
}
```

## File: `samples/CommandQuery.Sample.GoogleCloudFunctions/Startup.cs`
```csharp
using CommandQuery.GoogleCloudFunctions;
using CommandQuery.Sample.Contracts.Commands;
using CommandQuery.Sample.Contracts.Queries;
using CommandQuery.Sample.Handlers;
using CommandQuery.Sample.Handlers.Commands;
using CommandQuery.Sample.Handlers.Queries;
using Google.Cloud.Functions.Hosting;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.DependencyInjection;

namespace CommandQuery.Sample.GoogleCloudFunctions
{
    public class Startup : FunctionsStartup
    {
        public override void ConfigureServices(WebHostBuilderContext context, IServiceCollection services) =>
            services
                //.AddSingleton(new JsonSerializerOptions(JsonSerializerDefaults.Web))

                // Add commands and queries
                .AddCommandFunction(typeof(FooCommandHandler).Assembly, typeof(FooCommand).Assembly)
                .AddQueryFunction(typeof(BarQueryHandler).Assembly, typeof(BarQuery).Assembly)

                // Add handler dependencies
                .AddTransient<IDateTimeProxy, DateTimeProxy>()
                .AddTransient<ICultureService, CultureService>();

        public override void Configure(WebHostBuilderContext context, IApplicationBuilder app)
        {
            // Validation
            app.ApplicationServices.GetService<ICommandProcessor>()!.AssertConfigurationIsValid();
            app.ApplicationServices.GetService<IQueryProcessor>()!.AssertConfigurationIsValid();
        }
    }
}
```

## File: `samples/CommandQuery.Sample.GoogleCloudFunctions/command.bat`
```
dotnet run --target CommandQuery.Sample.GoogleCloudFunctions.Command --port 7071
```

## File: `samples/CommandQuery.Sample.GoogleCloudFunctions/deploy.bat`
```
:: Deploy from the root directory
cd ..\..

CMD /C gcloud functions deploy commandquery-sample-googlecloudfunctions-command --gen2 --region=europe-north1 --runtime=dotnet8 --trigger-http --entry-point=CommandQuery.Sample.GoogleCloudFunctions.Command --set-build-env-vars=GOOGLE_BUILDABLE=samples/CommandQuery.Sample.GoogleCloudFunctions
CMD /C gcloud functions deploy commandquery-sample-googlecloudfunctions-query --gen2 --region=europe-north1 --runtime=dotnet8 --trigger-http --entry-point=CommandQuery.Sample.GoogleCloudFunctions.Query --set-build-env-vars=GOOGLE_BUILDABLE=samples/CommandQuery.Sample.GoogleCloudFunctions

cd samples\CommandQuery.Sample.GoogleCloudFunctions
```

## File: `samples/CommandQuery.Sample.GoogleCloudFunctions/query.bat`
```
dotnet run --target CommandQuery.Sample.GoogleCloudFunctions.Query --port 7071
```

## File: `samples/CommandQuery.Sample.GoogleCloudFunctions.Tests/CommandQuery.Sample.GoogleCloudFunctions.Tests.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="FluentAssertions" Version="6.12.0" />
    <PackageReference Include="Google.Cloud.Functions.Testing" Version="2.2.1" />
    <PackageReference Include="Microsoft.NET.Test.Sdk" Version="17.10.0" />
    <PackageReference Include="NUnit" Version="4.1.0" />
    <PackageReference Include="NUnit3TestAdapter" Version="4.5.0">
      <PrivateAssets>all</PrivateAssets>
      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
    </PackageReference>
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\CommandQuery.Sample.GoogleCloudFunctions\CommandQuery.Sample.GoogleCloudFunctions.csproj" />
  </ItemGroup>

</Project>
```

## File: `samples/CommandQuery.Sample.GoogleCloudFunctions.Tests/CommandTests.cs`
```csharp
using System.Net;
using System.Net.Http.Json;
using CommandQuery.Sample.Contracts.Commands;
using FluentAssertions;
using Google.Cloud.Functions.Testing;
using NUnit.Framework;

namespace CommandQuery.Sample.GoogleCloudFunctions.Tests
{
    public class CommandTests
    {
        [SetUp]
        public void SetUp()
        {
            Server = new FunctionTestServer<Command>();
            Client = Server.CreateClient();
        }

        [TearDown]
        public void TearDown()
        {
            Client.Dispose();
            Server.Dispose();
        }

        [Test]
        public async Task should_handle_command()
        {
            var response = await Client.PostAsJsonAsync("/api/command/FooCommand", new FooCommand { Value = "Foo" });
            response.StatusCode.Should().Be(HttpStatusCode.OK);
        }

        [Test]
        public async Task should_handle_errors()
        {
            var response = await Client.PostAsJsonAsync("/api/command/FooCommand", new FooCommand());
            await response.ShouldBeErrorAsync("Value cannot be null or empty");
        }

        FunctionTestServer<Command> Server = null!;
        HttpClient Client = null!;
    }
}
```

## File: `samples/CommandQuery.Sample.GoogleCloudFunctions.Tests/QueryTests.cs`
```csharp
using System.Net.Http.Json;
using CommandQuery.Sample.Contracts.Queries;
using FluentAssertions;
using Google.Cloud.Functions.Testing;
using Microsoft.AspNetCore.Http;
using NUnit.Framework;

namespace CommandQuery.Sample.GoogleCloudFunctions.Tests
{
    public class QueryTests
    {
        [SetUp]
        public void SetUp()
        {
            Server = new FunctionTestServer<Query>();
            Client = Server.CreateClient();
        }

        [TearDown]
        public void TearDown()
        {
            Client.Dispose();
            Server.Dispose();
        }

        [Test]
        public async Task should_handle_query_via_Post()
        {
            var response = await Client.PostAsJsonAsync("/api/query/BarQuery", new BarQuery { Id = 1 });
            var value = await response.Content.ReadFromJsonAsync<Bar>();
            value!.Id.Should().Be(1);
        }

        [Test]
        public async Task should_handle_query_via_Get()
        {
            var response = await Client.GetAsync("/api/query/BarQuery?Id=1");
            var value = await response.Content.ReadFromJsonAsync<Bar>();
            value!.Id.Should().Be(1);
        }

        FunctionTestServer<Query> Server = null!;
        HttpClient Client = null!;
    }
}
```

## File: `samples/CommandQuery.Sample.GoogleCloudFunctions.Tests/ShouldExtensions.cs`
```csharp
using System.Net;
using System.Net.Http.Json;
using CommandQuery.Sample.Contracts;
using FluentAssertions;
using Microsoft.AspNetCore.Http;

namespace CommandQuery.Sample.GoogleCloudFunctions.Tests
{
    public static class ShouldExtensions
    {
        public static async Task ShouldBeErrorAsync(this HttpResponseMessage result, string message)
        {
            result.Should().NotBeNull();
            result.StatusCode.Should().NotBe(HttpStatusCode.OK);
            var value = await result.Content.ReadFromJsonAsync<Error>();
            value.Should().NotBeNull();
            value!.Message.Should().Be(message);
        }
    }
}
```

## File: `samples/CommandQuery.Sample.Handlers/CommandQuery.Sample.Handlers.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>netstandard2.0</TargetFramework>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="CommandQuery" Version="4.0.0" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\CommandQuery.Sample.Contracts\CommandQuery.Sample.Contracts.csproj" />
  </ItemGroup>

</Project>
```

## File: `samples/CommandQuery.Sample.Handlers/CultureService.cs`
```csharp
using System.Globalization;

namespace CommandQuery.Sample.Handlers
{
    public interface ICultureService
    {
        void SetCurrentCulture(string name);
    }

    public class CultureService : ICultureService
    {
        public void SetCurrentCulture(string name)
        {
            var culture = CultureInfo.CreateSpecificCulture(name);
            CultureInfo.DefaultThreadCurrentCulture = culture;
            CultureInfo.DefaultThreadCurrentUICulture = culture;
        }
    }
}
```

## File: `samples/CommandQuery.Sample.Handlers/DateTimeProxy.cs`
```csharp
namespace CommandQuery.Sample.Handlers
{
    public interface IDateTimeProxy
    {
        DateTime Now { get; }
    }

    public class DateTimeProxy : IDateTimeProxy
    {
        public DateTime Now => DateTime.Now;
    }
}
```

## File: `samples/CommandQuery.Sample.Handlers/FooCommandException.cs`
```csharp
using CommandQuery.Exceptions;

namespace CommandQuery.Sample.Handlers
{
    public class FooCommandException : CommandException
    {
        public int ErrorCode { get; }
        public string Help { get; }

        public FooCommandException(string message, int errorCode, string help) : base(message)
        {
            ErrorCode = errorCode;
            Help = help;
        }
    }
}
```

## File: `samples/CommandQuery.Sample.Handlers/QuuxQueryException.cs`
```csharp
using CommandQuery.Exceptions;

namespace CommandQuery.Sample.Handlers
{
    public class QuuxQueryException : QueryException
    {
        public bool InvalidCorge { get; set; }
        public bool InvalidGrault { get; set; }

        public QuuxQueryException(string message) : base(message)
        {
        }
    }
}
```

## File: `samples/CommandQuery.Sample.Handlers/Commands/BazCommandHandler.cs`
```csharp
using CommandQuery.Sample.Contracts.Commands;

namespace CommandQuery.Sample.Handlers.Commands
{
    public class BazCommandHandler : ICommandHandler<BazCommand, Baz>
    {
        private readonly ICultureService _cultureService;

        public BazCommandHandler(ICultureService cultureService)
        {
            _cultureService = cultureService;
        }

        public async Task<Baz> HandleAsync(BazCommand command, CancellationToken cancellationToken)
        {
            var result = new Baz();

            try
            {
                _cultureService.SetCurrentCulture(command.Value);

                result.Success = true;
            }
            catch
            {
                // TODO: log
            }

            return await Task.FromResult(result);
        }
    }
}
```

## File: `samples/CommandQuery.Sample.Handlers/Commands/FooCommandHandler.cs`
```csharp
using CommandQuery.Sample.Contracts.Commands;

namespace CommandQuery.Sample.Handlers.Commands
{
    public class FooCommandHandler : ICommandHandler<FooCommand>
    {
        private readonly ICultureService _cultureService;

        public FooCommandHandler(ICultureService cultureService)
        {
            _cultureService = cultureService;
        }

        public async Task HandleAsync(FooCommand command, CancellationToken cancellationToken)
        {
            if (string.IsNullOrEmpty(command.Value)) throw new FooCommandException("Value cannot be null or empty", 1337, "Try setting the value to 'en-US'");

            _cultureService.SetCurrentCulture(command.Value);

            await Task.CompletedTask;
        }
    }
}
```

## File: `samples/CommandQuery.Sample.Handlers/Queries/BarQueryHandler.cs`
```csharp
using CommandQuery.Sample.Contracts.Queries;

namespace CommandQuery.Sample.Handlers.Queries
{
    public class BarQueryHandler : IQueryHandler<BarQuery, Bar>
    {
        private readonly IDateTimeProxy _dateTime;

        public BarQueryHandler(IDateTimeProxy dateTime)
        {
            _dateTime = dateTime;
        }

        public async Task<Bar> HandleAsync(BarQuery query, CancellationToken cancellationToken)
        {
            var result = new Bar { Id = query.Id, Value = _dateTime.Now.ToString("F") };

            return await Task.FromResult(result);
        }
    }
}
```

## File: `samples/CommandQuery.Sample.Handlers/Queries/QuuxQueryHandler.cs`
```csharp
using CommandQuery.Sample.Contracts.Queries;

namespace CommandQuery.Sample.Handlers.Queries
{
    public class QuuxQueryHandler : IQueryHandler<QuuxQuery, Quux>
    {
        public async Task<Quux> HandleAsync(QuuxQuery query, CancellationToken cancellationToken)
        {
            if (query.Corge is null) throw new QuuxQueryException("Corge is null") { InvalidCorge = true };
            if (query.Corge.Grault is null) throw new QuuxQueryException("Grault is null") { InvalidGrault = true };

            var result = new Quux
            {
                Id = query.Id.GetValueOrDefault(1337),
                Corge = new Corge
                {
                    DateTime = query.Corge.DateTime.AddDays(1),
                    Grault = new Grault
                    {
                        DayOfWeek = query.Corge.Grault.DayOfWeek + 1
                    }
                }
            };

            return await Task.FromResult(result);
        }
    }
}
```

## File: `samples/CommandQuery.Sample.Handlers/Queries/QuxQueryHandler.cs`
```csharp
using CommandQuery.Sample.Contracts.Queries;

namespace CommandQuery.Sample.Handlers.Queries
{
    public class QuxQueryHandler : IQueryHandler<QuxQuery, Qux[]>
    {
        private readonly IDateTimeProxy _dateTime;

        public QuxQueryHandler(IDateTimeProxy dateTime)
        {
            _dateTime = dateTime;
        }

        public async Task<Qux[]> HandleAsync(QuxQuery query, CancellationToken cancellationToken)
        {
            var result = query.Ids.Select((x, index) => new Qux { Id = x, Value = _dateTime.Now.AddDays(index).ToString("F") }).ToArray();

            return await Task.FromResult(result);
        }
    }
}
```

## File: `samples/HttpFiles/GetBarQuery.http`
```
@Id = 1

GET {{QueryUrl}}/BarQuery?Id={{Id}}
Content-Type: application/json
```

## File: `samples/HttpFiles/GetQuuxQuery.http`
```
@Id = 1
@DateTime = 2021-07-15T22%3A12%3A41.0000000Z
@DayOfWeek = Monday

GET {{QueryUrl}}/QuuxQuery?Id={{Id}}&Corge.DateTime={{DateTime}}&Corge.Grault.DayOfWeek={{DayOfWeek}}
Content-Type: application/json
```

## File: `samples/HttpFiles/GetQuxQuery.http`
```
@Id1 = 94e4d942-0606-4fba-90df-8604ead81968
@Id2 = e085c54b-44e4-4478-a28a-25ce3eaa79ce

GET {{QueryUrl}}/QuxQuery?Ids={{Id1}}&Ids={{Id2}}
Content-Type: application/json
```

## File: `samples/HttpFiles/PostBarQuery.http`
```

POST {{QueryUrl}}/BarQuery
Content-Type: application/json

{
  "Id": 1
}
```

## File: `samples/HttpFiles/PostBazCommand.http`
```

POST {{CommandUrl}}/BazCommand
Content-Type: application/json

{
  "Value": "sv-SE"
}
```

## File: `samples/HttpFiles/PostFooCommand.http`
```

POST {{CommandUrl}}/FooCommand
Content-Type: application/json

{
  "Value": "sv-SE"
}
```

## File: `samples/HttpFiles/PostQuuxQuery.http`
```

POST {{QueryUrl}}/QuuxQuery
Content-Type: application/json

{
  "Id": 1,
  "Corge": {
    "DateTime": "2021-07-15T22:12:41.0000000Z",
    "Grault": {
      "DayOfWeek": 1
    }
  }
}
```

## File: `samples/HttpFiles/PostQuxQuery.http`
```

POST {{QueryUrl}}/QuxQuery
Content-Type: application/json

{
  "Ids": [
    "94e4d942-0606-4fba-90df-8604ead81968",
    "e085c54b-44e4-4478-a28a-25ce3eaa79ce"
  ]
}
```

## File: `samples/HttpFiles/http-client.env.json`
```json
{
    "AspNetCore": {
        "CommandUrl": "https://commandquerysampleaspnetcore.azurewebsites.net/api/command",
        "QueryUrl": "https://commandquerysampleaspnetcore.azurewebsites.net/api/query"
    },
    "AWSLambda": {
        "CommandUrl": "https://u3rkew3obh.execute-api.eu-central-1.amazonaws.com/Prod/command",
        "QueryUrl": "https://u3rkew3obh.execute-api.eu-central-1.amazonaws.com/Prod/query"
    },
    "AzureFunctions": {
        "CommandUrl": "https://commandquerysampleazurefunctions.azurewebsites.net/api/command",
        "QueryUrl": "https://commandquerysampleazurefunctions.azurewebsites.net/api/query"
    },
    "GoogleCloudFunctions": {
        "CommandUrl": "https://europe-north1-solid-antler-215713.cloudfunctions.net/commandquery-sample-googlecloudfunctions-command/api/command",
        "QueryUrl": "https://europe-north1-solid-antler-215713.cloudfunctions.net/commandquery-sample-googlecloudfunctions-query/api/query"
    },
    "http://localhost:7071": {
        "CommandUrl": "http://localhost:7071/api/command",
        "QueryUrl": "http://localhost:7071/api/query"
    }
}
```

## File: `src/CommandQuery/CommandProcessor.cs`
```csharp
using CommandQuery.Exceptions;

namespace CommandQuery
{
    /// <inheritdoc />
    public class CommandProcessor : ICommandProcessor
    {
        private readonly ICommandTypeProvider _commandTypeProvider;
        private readonly IServiceProvider _serviceProvider;

        /// <summary>
        /// Initializes a new instance of the <see cref="CommandProcessor"/> class.
        /// </summary>
        /// <param name="commandTypeProvider">A provider of supported commands.</param>
        /// <param name="serviceProvider">A service provider with supported command handlers.</param>
        public CommandProcessor(ICommandTypeProvider commandTypeProvider, IServiceProvider serviceProvider)
        {
            _commandTypeProvider = commandTypeProvider;
            _serviceProvider = serviceProvider;
        }

        /// <inheritdoc />
        public async Task ProcessAsync(ICommand command, CancellationToken cancellationToken = default)
        {
            if (command is null)
            {
                throw new ArgumentNullException(nameof(command));
            }

            var handlerType = typeof(ICommandHandler<>).MakeGenericType(command.GetType());

            dynamic? handler = GetService(handlerType);

            if (handler is null)
            {
                throw new CommandProcessorException($"The command handler for '{command}' could not be found.");
            }

            await handler.HandleAsync((dynamic)command, cancellationToken);
        }

        /// <inheritdoc />
        public async Task<TResult> ProcessAsync<TResult>(ICommand<TResult> command, CancellationToken cancellationToken = default)
        {
            if (command is null)
            {
                throw new ArgumentNullException(nameof(command));
            }

            var handlerType = typeof(ICommandHandler<,>).MakeGenericType(command.GetType(), typeof(TResult));

            dynamic? handler = GetService(handlerType);

            if (handler is null)
            {
                throw new CommandProcessorException($"The command handler for '{command}' could not be found.");
            }

            return await handler.HandleAsync((dynamic)command, cancellationToken);
        }

        /// <inheritdoc />
        public Type? GetCommandType(string commandName)
        {
            return _commandTypeProvider.GetCommandType(commandName);
        }

        /// <inheritdoc />
        public IReadOnlyList<Type> GetCommandTypes()
        {
            return _commandTypeProvider.GetCommandTypes();
        }

        /// <inheritdoc />
        public ICommandProcessor AssertConfigurationIsValid()
        {
            var errors = new List<string>();

            foreach (var commandType in GetCommandTypes())
            {
                var handlerType = commandType.IsAssignableToType(typeof(ICommand))
                    ? typeof(ICommandHandler<>).MakeGenericType(commandType)
                    : typeof(ICommandHandler<,>).MakeGenericType(commandType, commandType.GetResultType(typeof(ICommand<>)));

                try
                {
                    if (GetService(handlerType) is null)
                    {
                        errors.Add($"The command handler for '{commandType.AssemblyQualifiedName}' is not registered.");
                    }
                }
                catch (CommandProcessorException)
                {
                    errors.Add($"A single command handler for '{commandType.AssemblyQualifiedName}' could not be retrieved.");
                }
            }

            foreach (var handlerType in _serviceProvider
                .GetAllServiceTypes()
                .Where(x => x.IsGenericType && (x.GetGenericTypeDefinition() == typeof(ICommandHandler<>) || x.GetGenericTypeDefinition() == typeof(ICommandHandler<,>)))
                .ToList())
            {
                var commandType = handlerType.GetGenericArguments()[0];
                var supportedCommandType = _commandTypeProvider.GetCommandType(commandType.Name);

                if (supportedCommandType is null || supportedCommandType != commandType)
                {
                    errors.Add($"The command '{commandType.AssemblyQualifiedName}' is not registered.");
                }
            }

            if (errors.Any())
            {
                throw new CommandTypeException("The CommandProcessor configuration is not valid:" + Environment.NewLine + string.Join(Environment.NewLine, errors));
            }

            return this;
        }

        private object? GetService(Type handlerType)
        {
            try
            {
                return _serviceProvider.GetSingleService(handlerType);
            }
            catch (InvalidOperationException exception)
            {
                throw new CommandProcessorException($"A single command handler for '{handlerType}' could not be retrieved.", exception);
            }
        }
    }
}
```

## File: `src/CommandQuery/CommandQuery.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>netstandard2.0</TargetFramework>
    <Version>4.0.0</Version>
    <PackageReleaseNotes>
- Bump Microsoft.Extensions.DependencyInjection to 8.0.0
    </PackageReleaseNotes>
    <Authors>Henrik Lau Eriksson</Authors>
    <Description>Command Query Separation for .NET Framework and .NET Standard ⚙️

✔️ Build services that separate the responsibility of commands and queries
✔️ Focus on implementing the handlers for commands and queries
✔️ Create APIs with less boilerplate code
📄 https://hlaueriksson.me/CommandQuery/
    </Description>
    <PackageId>CommandQuery</PackageId>
    <PackageProjectUrl>https://github.com/hlaueriksson/CommandQuery</PackageProjectUrl>
    <PackageIcon>icon.png</PackageIcon>
    <PackageReadmeFile>CommandQuery.md</PackageReadmeFile>
    <PackageTags>CommandQuery;Command;Query;CQS</PackageTags>
    <PackageLicenseExpression>MIT</PackageLicenseExpression>
    <GenerateDocumentationFile>true</GenerateDocumentationFile>
  </PropertyGroup>

  <ItemGroup>
    <None Include="..\..\icon.png" Link="icon.png" Pack="true" PackagePath="\" />
    <None Include="..\..\CommandQuery.md" Pack="true" PackagePath="\" />
  </ItemGroup>

  <Import Project="../../Analyzers.props" />

  <ItemGroup>
    <InternalsVisibleTo Include="CommandQuery.AspNetCore" />
    <InternalsVisibleTo Include="CommandQuery.AWSLambda" />
    <InternalsVisibleTo Include="CommandQuery.AzureFunctions" />
    <InternalsVisibleTo Include="CommandQuery.GoogleCloudFunctions" />
    <InternalsVisibleTo Include="CommandQuery.SystemTextJson" />
    <InternalsVisibleTo Include="CommandQuery.Tests" />
  </ItemGroup>

  <ItemGroup>
    <PackageReference Include="Microsoft.CSharp" Version="4.7.0" />
    <PackageReference Include="Microsoft.Extensions.DependencyInjection" Version="8.0.0" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\CommandQuery.Abstractions\CommandQuery.Abstractions.csproj" />
  </ItemGroup>

</Project>
```

## File: `src/CommandQuery/CommandTypeProvider.cs`
```csharp
using System.Reflection;
using CommandQuery.Exceptions;

namespace CommandQuery
{
    /// <inheritdoc cref="ICommandTypeProvider" />
    public class CommandTypeProvider : TypeProvider, ICommandTypeProvider
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="CommandTypeProvider"/> class.
        /// </summary>
        /// <param name="assemblies">The assemblies with commands to support.</param>
        /// <exception cref="CommandTypeException">Multiple commands with the same name was found.</exception>
        public CommandTypeProvider(params Assembly[] assemblies)
            : base([typeof(ICommand), typeof(ICommand<>)], assemblies)
        {
        }

        /// <inheritdoc />
        public Type? GetCommandType(string key) => GetType(key);

        /// <inheritdoc />
        public IReadOnlyList<Type> GetCommandTypes() => GetTypes();

        /// <inheritdoc />
        protected override Exception GetTypeException(Type first, Type second) =>
            new CommandTypeException($"Multiple commands with the same name was found: '{first?.AssemblyQualifiedName}', '{second?.AssemblyQualifiedName}'");
    }
}
```

## File: `src/CommandQuery/ICommandProcessor.cs`
```csharp
using CommandQuery.Exceptions;

namespace CommandQuery
{
    /// <summary>
    /// Process commands by invoking the corresponding handler.
    /// </summary>
    public interface ICommandProcessor
    {
        /// <summary>
        /// Process a command.
        /// </summary>
        /// <param name="command">The command.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>A task that represents the asynchronous operation.</returns>
        /// <exception cref="ArgumentNullException"><paramref name="command"/> is <see langword="null"/>.</exception>
        /// <exception cref="CommandProcessorException">The command handler for <paramref name="command"/> could not be found.</exception>
        Task ProcessAsync(ICommand command, CancellationToken cancellationToken = default);

        /// <summary>
        /// Process a command with result.
        /// </summary>
        /// <typeparam name="TResult">The type of result.</typeparam>
        /// <param name="command">The command.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>The result of the command.</returns>
        /// <exception cref="ArgumentNullException"><paramref name="command"/> is <see langword="null"/>.</exception>
        /// <exception cref="CommandProcessorException">The command handler for <paramref name="command"/> could not be found.</exception>
        Task<TResult> ProcessAsync<TResult>(ICommand<TResult> command, CancellationToken cancellationToken = default);

        /// <summary>
        /// Returns the type of command.
        /// </summary>
        /// <param name="commandName">The name of the command.</param>
        /// <returns>The command type.</returns>
        Type? GetCommandType(string commandName);

        /// <summary>
        /// Returns the types of commands that can be processed.
        /// </summary>
        /// <returns>Supported command types.</returns>
        IReadOnlyList<Type> GetCommandTypes();

        /// <summary>
        /// Validate the command type and handler configuration and throw a <see cref="CommandTypeException"/> for any problems.
        /// </summary>
        /// <returns>The <see cref="ICommandProcessor"/>.</returns>
        ICommandProcessor AssertConfigurationIsValid();
    }
}
```

## File: `src/CommandQuery/ICommandTypeProvider.cs`
```csharp
namespace CommandQuery
{
    /// <summary>
    /// A provider of supported command types.
    /// </summary>
    public interface ICommandTypeProvider
    {
        /// <summary>
        /// Returns the type of command.
        /// </summary>
        /// <param name="key">The type key.</param>
        /// <returns>The type of command.</returns>
        Type? GetCommandType(string key);

        /// <summary>
        /// Returns the types of supported commands.
        /// </summary>
        /// <returns>Supported commands.</returns>
        IReadOnlyList<Type> GetCommandTypes();
    }
}
```

## File: `src/CommandQuery/IQueryProcessor.cs`
```csharp
using CommandQuery.Exceptions;

namespace CommandQuery
{
    /// <summary>
    /// Process queries by invoking the corresponding handler.
    /// </summary>
    public interface IQueryProcessor
    {
        /// <summary>
        /// Process a query.
        /// </summary>
        /// <typeparam name="TResult">The type of result.</typeparam>
        /// <param name="query">The query.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>The result of the query.</returns>
        /// <exception cref="ArgumentNullException"><paramref name="query"/> is <see langword="null"/>.</exception>
        /// <exception cref="QueryProcessorException">The query handler for <paramref name="query"/> could not be found.</exception>
        Task<TResult> ProcessAsync<TResult>(IQuery<TResult> query, CancellationToken cancellationToken = default);

        /// <summary>
        /// Returns the type of query.
        /// </summary>
        /// <param name="queryName">The name of the query.</param>
        /// <returns>The query type.</returns>
        Type? GetQueryType(string queryName);

        /// <summary>
        /// Returns the types of queries that can be processed.
        /// </summary>
        /// <returns>Supported query types.</returns>
        IReadOnlyList<Type> GetQueryTypes();

        /// <summary>
        /// Validate the query type and handler configuration and throw a <see cref="QueryTypeException"/> for any problems.
        /// </summary>
        /// <returns>The <see cref="IQueryProcessor"/>.</returns>
        IQueryProcessor AssertConfigurationIsValid();
    }
}
```

## File: `src/CommandQuery/IQueryTypeProvider.cs`
```csharp
namespace CommandQuery
{
    /// <summary>
    /// A provider of supported query types.
    /// </summary>
    public interface IQueryTypeProvider
    {
        /// <summary>
        /// Returns the type of query.
        /// </summary>
        /// <param name="key">The type key.</param>
        /// <returns>The type of query.</returns>
        Type? GetQueryType(string key);

        /// <summary>
        /// Returns the types of supported queries.
        /// </summary>
        /// <returns>Supported queries.</returns>
        IReadOnlyList<Type> GetQueryTypes();
    }
}
```

## File: `src/CommandQuery/QueryProcessor.cs`
```csharp
using CommandQuery.Exceptions;

namespace CommandQuery
{
    /// <inheritdoc />
    public class QueryProcessor : IQueryProcessor
    {
        private readonly IQueryTypeProvider _queryTypeProvider;
        private readonly IServiceProvider _serviceProvider;

        /// <summary>
        /// Initializes a new instance of the <see cref="QueryProcessor"/> class.
        /// </summary>
        /// <param name="queryTypeProvider">A provider of supported queries.</param>
        /// <param name="serviceProvider">A service provider with supported query handlers.</param>
        public QueryProcessor(IQueryTypeProvider queryTypeProvider, IServiceProvider serviceProvider)
        {
            _queryTypeProvider = queryTypeProvider;
            _serviceProvider = serviceProvider;
        }

        /// <inheritdoc />
        public async Task<TResult> ProcessAsync<TResult>(IQuery<TResult> query, CancellationToken cancellationToken = default)
        {
            if (query is null)
            {
                throw new ArgumentNullException(nameof(query));
            }

            var handlerType = typeof(IQueryHandler<,>).MakeGenericType(query.GetType(), typeof(TResult));

            dynamic? handler = GetService(handlerType);

            if (handler is null)
            {
                throw new QueryProcessorException($"The query handler for '{query}' could not be found.");
            }

            return await handler.HandleAsync((dynamic)query, cancellationToken);
        }

        /// <inheritdoc />
        public Type? GetQueryType(string queryName)
        {
            return _queryTypeProvider.GetQueryType(queryName);
        }

        /// <inheritdoc />
        public IReadOnlyList<Type> GetQueryTypes()
        {
            return _queryTypeProvider.GetQueryTypes();
        }

        /// <inheritdoc />
        public IQueryProcessor AssertConfigurationIsValid()
        {
            var errors = new List<string>();

            foreach (var queryType in GetQueryTypes())
            {
                var handlerType = typeof(IQueryHandler<,>).MakeGenericType(queryType, queryType.GetResultType(typeof(IQuery<>)));

                try
                {
                    if (GetService(handlerType) is null)
                    {
                        errors.Add($"The query handler for '{queryType.AssemblyQualifiedName}' is not registered.");
                    }
                }
                catch (QueryProcessorException)
                {
                    errors.Add($"A single query handler for '{queryType.AssemblyQualifiedName}' could not be retrieved.");
                }
            }

            foreach (var handlerType in _serviceProvider
                .GetAllServiceTypes()
                .Where(x => x.IsGenericType && x.GetGenericTypeDefinition() == typeof(IQueryHandler<,>))
                .ToList())
            {
                var queryType = handlerType.GetGenericArguments()[0];
                var supportedQueryType = _queryTypeProvider.GetQueryType(queryType.Name);

                if (supportedQueryType is null || supportedQueryType != queryType)
                {
                    errors.Add($"The query '{queryType.AssemblyQualifiedName}' is not registered.");
                }
            }

            if (errors.Any())
            {
                throw new QueryTypeException("The QueryProcessor configuration is not valid:" + Environment.NewLine + string.Join(Environment.NewLine, errors));
            }

            return this;
        }

        private object? GetService(Type handlerType)
        {
            try
            {
                return _serviceProvider.GetSingleService(handlerType);
            }
            catch (InvalidOperationException exception)
            {
                throw new QueryProcessorException($"A single query handler for '{handlerType}' could not be retrieved.", exception);
            }
        }
    }
}
```

## File: `src/CommandQuery/QueryTypeProvider.cs`
```csharp
using System.Reflection;
using CommandQuery.Exceptions;

namespace CommandQuery
{
    /// <inheritdoc cref="IQueryTypeProvider" />
    public class QueryTypeProvider : TypeProvider, IQueryTypeProvider
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="QueryTypeProvider"/> class.
        /// </summary>
        /// <param name="assemblies">The assemblies with queries to support.</param>
        /// <exception cref="QueryTypeException">Multiple queries with the same name was found.</exception>
        public QueryTypeProvider(params Assembly[] assemblies)
            : base([typeof(IQuery<>)], assemblies)
        {
        }

        /// <inheritdoc />
        public Type? GetQueryType(string key) => GetType(key);

        /// <inheritdoc />
        public IReadOnlyList<Type> GetQueryTypes() => GetTypes();

        /// <inheritdoc />
        protected override Exception GetTypeException(Type first, Type second) =>
            new QueryTypeException($"Multiple queries with the same name was found: '{first?.AssemblyQualifiedName}', '{second?.AssemblyQualifiedName}'");
    }
}
```

## File: `src/CommandQuery/TypeProvider.cs`
```csharp
using System.Reflection;
using CommandQuery.Exceptions;

namespace CommandQuery
{
    /// <summary>
    /// A provider of supported command or query types.
    /// </summary>
    public abstract class TypeProvider
    {
        private readonly Type[] _baseTypes;
        private readonly Dictionary<string, Type> _types;

        /// <summary>
        /// Initializes a new instance of the <see cref="TypeProvider"/> class.
        /// </summary>
        /// <param name="baseTypes">The base types for commands or queries.</param>
        /// <param name="assemblies">The assemblies with commands or queries to support.</param>
        protected TypeProvider(Type[] baseTypes, params Assembly[] assemblies)
        {
            _baseTypes = baseTypes;
            _types = [];
            LoadTypeCaches(assemblies);
        }

        /// <summary>
        /// Returns the type of command or query.
        /// </summary>
        /// <param name="key">The type key.</param>
        /// <returns>The type of command or query.</returns>
        protected Type? GetType(string key)
        {
            return _types.ContainsKey(key) ? _types[key] : null;
        }

        /// <summary>
        /// Returns the types of supported commands or queries.
        /// </summary>
        /// <returns>Supported commands or queries.</returns>
        protected IReadOnlyList<Type> GetTypes()
        {
            return _types.Values.ToList().AsReadOnly();
        }

        /// <summary>
        /// Returns exception for when multiple types with the same <see cref="MemberInfo.Name"/> were found.
        /// </summary>
        /// <param name="first">The first type.</param>
        /// <param name="second">The second type.</param>
        /// <returns><see cref="CommandTypeException"/> or <see cref="QueryTypeException"/>.</returns>
        protected abstract Exception GetTypeException(Type first, Type second);

        private void LoadTypeCaches(params Assembly[] assemblies)
        {
            foreach (var baseType in _baseTypes)
            {
                foreach (var type in assemblies.SelectMany(assembly => assembly.GetTypesAssignableTo(baseType)).ToList())
                {
                    var key = type.Name;

                    if (_types.ContainsKey(key))
                    {
                        throw GetTypeException(_types[key], type);
                    }

                    _types.Add(key, type);
                }
            }
        }
    }
}
```

## File: `src/CommandQuery/DependencyInjection/CommandExtensions.cs`
```csharp
using System.Reflection;
using Microsoft.Extensions.DependencyInjection;

namespace CommandQuery.DependencyInjection
{
    /// <summary>
    /// Extensions methods for initializing an <see cref="ICommandProcessor"/>.
    /// </summary>
    public static class CommandExtensions
    {
        /// <summary>
        /// Initializes an <see cref="ICommandProcessor"/> from an <see cref="Assembly"/> with commands and handlers.
        /// </summary>
        /// <param name="assembly">An <see cref="Assembly"/> with commands and handlers.</param>
        /// <returns>An <see cref="ICommandProcessor"/>.</returns>
        public static ICommandProcessor GetCommandProcessor(this Assembly assembly)
        {
            return new ServiceCollection().GetCommandProcessor(assembly);
        }

        /// <summary>
        /// Initializes an <see cref="ICommandProcessor"/> from assemblies with commands and handlers.
        /// </summary>
        /// <param name="assemblies">Assemblies with commands and handlers.</param>
        /// <returns>An <see cref="ICommandProcessor"/>.</returns>
        public static ICommandProcessor GetCommandProcessor(this Assembly[] assemblies)
        {
            return new ServiceCollection().GetCommandProcessor(assemblies);
        }

        /// <summary>
        /// Initializes an <see cref="ICommandProcessor"/> from an <see cref="Assembly"/> with commands and handlers.
        /// </summary>
        /// <param name="assembly">An <see cref="Assembly"/> with commands and handlers.</param>
        /// <param name="services">A service collection for command handlers.</param>
        /// <returns>An <see cref="ICommandProcessor"/>.</returns>
        public static ICommandProcessor GetCommandProcessor(this Assembly assembly, IServiceCollection services)
        {
            return services.GetCommandProcessor(assembly);
        }

        /// <summary>
        /// Initializes an <see cref="ICommandProcessor"/> from assemblies with commands and handlers.
        /// </summary>
        /// <param name="assemblies">Assemblies with commands and handlers.</param>
        /// <param name="services">A service collection for command handlers.</param>
        /// <returns>An <see cref="ICommandProcessor"/>.</returns>
        public static ICommandProcessor GetCommandProcessor(this Assembly[] assemblies, IServiceCollection services)
        {
            return services.GetCommandProcessor(assemblies);
        }

        /// <summary>
        /// Initializes an <see cref="ICommandProcessor"/> from assemblies with commands and handlers.
        /// </summary>
        /// <param name="services">A service collection for command handlers.</param>
        /// <param name="assemblies">Assemblies with commands and handlers.</param>
        /// <returns>An <see cref="ICommandProcessor"/>.</returns>
        public static ICommandProcessor GetCommandProcessor(this IServiceCollection services, params Assembly[] assemblies)
        {
            services.AddCommands(assemblies);

            return new CommandProcessor(new CommandTypeProvider(assemblies), services.BuildServiceProvider());
        }
    }
}
```

## File: `src/CommandQuery/DependencyInjection/QueryExtensions.cs`
```csharp
using System.Reflection;
using Microsoft.Extensions.DependencyInjection;

namespace CommandQuery.DependencyInjection
{
    /// <summary>
    /// Extensions methods for initializing an <see cref="IQueryProcessor"/>.
    /// </summary>
    public static class QueryExtensions
    {
        /// <summary>
        /// Initializes an <see cref="IQueryProcessor"/> from an <see cref="Assembly"/> with queries and handlers.
        /// </summary>
        /// <param name="assembly">An <see cref="Assembly"/> with queries and handlers.</param>
        /// <returns>An <see cref="IQueryProcessor"/>.</returns>
        public static IQueryProcessor GetQueryProcessor(this Assembly assembly)
        {
            return new ServiceCollection().GetQueryProcessor(assembly);
        }

        /// <summary>
        /// Initializes an <see cref="IQueryProcessor"/> from assemblies with queries and handlers.
        /// </summary>
        /// <param name="assemblies">Assemblies with queries and handlers.</param>
        /// <returns>An <see cref="IQueryProcessor"/>.</returns>
        public static IQueryProcessor GetQueryProcessor(this Assembly[] assemblies)
        {
            return new ServiceCollection().GetQueryProcessor(assemblies);
        }

        /// <summary>
        /// Initializes an <see cref="IQueryProcessor"/> from an <see cref="Assembly"/> with queries and handlers.
        /// </summary>
        /// <param name="assembly">An <see cref="Assembly"/> with queries and handlers.</param>
        /// <param name="services">A service collection for query handlers.</param>
        /// <returns>An <see cref="IQueryProcessor"/>.</returns>
        public static IQueryProcessor GetQueryProcessor(this Assembly assembly, IServiceCollection services)
        {
            return services.GetQueryProcessor(assembly);
        }

        /// <summary>
        /// Initializes an <see cref="IQueryProcessor"/> from assemblies with queries and handlers.
        /// </summary>
        /// <param name="assemblies">Assemblies with queries and handlers.</param>
        /// <param name="services">A service collection for query handlers.</param>
        /// <returns>An <see cref="IQueryProcessor"/>.</returns>
        public static IQueryProcessor GetQueryProcessor(this Assembly[] assemblies, IServiceCollection services)
        {
            return services.GetQueryProcessor(assemblies);
        }

        /// <summary>
        /// Initializes an <see cref="IQueryProcessor"/> from assemblies with queries and handlers.
        /// </summary>
        /// <param name="services">A service collection for query handlers.</param>
        /// <param name="assemblies">Assemblies with queries and handlers.</param>
        /// <returns>An <see cref="IQueryProcessor"/>.</returns>
        public static IQueryProcessor GetQueryProcessor(this IServiceCollection services, params Assembly[] assemblies)
        {
            services.AddQueries(assemblies);

            return new QueryProcessor(new QueryTypeProvider(assemblies), services.BuildServiceProvider());
        }
    }
}
```

## File: `src/CommandQuery/DependencyInjection/ServiceCollectionExtensions.cs`
```csharp
using System.Reflection;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.DependencyInjection.Extensions;

namespace CommandQuery.DependencyInjection
{
    /// <summary>
    /// Extensions methods for <see cref="IServiceCollection"/>.
    /// </summary>
    public static class ServiceCollectionExtensions
    {
        /// <summary>
        /// Adds command handlers to the <see cref="IServiceCollection"/>.
        /// </summary>
        /// <param name="services">The <see cref="IServiceCollection"/>.</param>
        /// <param name="assemblies">Assemblies with command handlers.</param>
        /// <returns>The <see cref="IServiceCollection"/>.</returns>
        public static IServiceCollection AddCommands(this IServiceCollection services, params Assembly[] assemblies)
        {
            services.AddSingleton<ICommandProcessor, CommandProcessor>();
            services.AddSingleton<ICommandTypeProvider>(_ => new CommandTypeProvider(assemblies));

            services.AddHandlers(typeof(ICommandHandler<>), assemblies);
            services.AddHandlers(typeof(ICommandHandler<,>), assemblies);

            return services;
        }

        /// <summary>
        /// Adds query handlers to the <see cref="IServiceCollection"/>.
        /// </summary>
        /// <param name="services">The <see cref="IServiceCollection"/>.</param>
        /// <param name="assemblies">Assemblies with query handlers.</param>
        /// <returns>The <see cref="IServiceCollection"/>.</returns>
        public static IServiceCollection AddQueries(this IServiceCollection services, params Assembly[] assemblies)
        {
            services.AddSingleton<IQueryProcessor, QueryProcessor>();
            services.AddSingleton<IQueryTypeProvider>(_ => new QueryTypeProvider(assemblies));

            services.AddHandlers(typeof(IQueryHandler<,>), assemblies);

            return services;
        }

        private static void AddHandlers(this IServiceCollection services, Type baseType, params Assembly[] assemblies)
        {
            var handlers = assemblies.GetTypesAssignableTo(baseType);

            foreach (var handler in handlers)
            {
                foreach (var abstraction in handler.GetHandlerInterfaceTypes(baseType))
                {
                    services.TryAddTransient(abstraction, handler);
                }
            }
        }
    }
}
```

## File: `src/CommandQuery/Exceptions/CommandException.cs`
```csharp
namespace CommandQuery.Exceptions
{
    /// <summary>
    /// Represents errors that occur during command processing in a command handler.
    /// Derive custom command exceptions from this class and add public properties to expose more error details.
    /// </summary>
    public class CommandException : Exception
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="CommandException"/> class.
        /// </summary>
        public CommandException()
        {
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="CommandException"/> class with a specified error message.
        /// </summary>
        /// <param name="message">The message that describes the error.</param>
        public CommandException(string message)
            : base(message)
        {
        }

        /// <summary>Initializes a new instance of the <see cref="CommandException"/> class with a specified error message and a reference to the inner exception that is the cause of this exception.</summary>
        /// <param name="message">The error message that explains the reason for the exception.</param>
        /// <param name="innerException">The exception that is the cause of the current exception, or a null reference if no inner exception is specified.</param>
        public CommandException(string message, Exception innerException)
            : base(message, innerException)
        {
        }
    }
}
```

## File: `src/CommandQuery/Exceptions/CommandProcessorException.cs`
```csharp
namespace CommandQuery.Exceptions
{
    /// <summary>
    /// Represents errors that occur during command processing in the <see cref="CommandProcessor"/>.
    /// </summary>
    public sealed class CommandProcessorException : Exception
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="CommandProcessorException"/> class.
        /// </summary>
        public CommandProcessorException()
        {
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="CommandProcessorException"/> class with a specified error message.
        /// </summary>
        /// <param name="message">The message that describes the error.</param>
        public CommandProcessorException(string message)
            : base(message)
        {
        }

        /// <summary>Initializes a new instance of the <see cref="CommandProcessorException"/> class with a specified error message and a reference to the inner exception that is the cause of this exception.</summary>
        /// <param name="message">The error message that explains the reason for the exception.</param>
        /// <param name="innerException">The exception that is the cause of the current exception, or a null reference if no inner exception is specified.</param>
        public CommandProcessorException(string message, Exception innerException)
            : base(message, innerException)
        {
        }
    }
}
```

## File: `src/CommandQuery/Exceptions/CommandTypeException.cs`
```csharp
namespace CommandQuery.Exceptions
{
    /// <summary>
    /// Represents errors that occur during initialization of a <see cref="CommandTypeProvider"/>.
    /// </summary>
    public sealed class CommandTypeException : Exception
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="CommandTypeException"/> class.
        /// </summary>
        public CommandTypeException()
        {
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="CommandTypeException"/> class with a specified error message.
        /// </summary>
        /// <param name="message">The message that describes the error.</param>
        public CommandTypeException(string message)
            : base(message)
        {
        }

        /// <summary>Initializes a new instance of the <see cref="CommandTypeException"/> class with a specified error message and a reference to the inner exception that is the cause of this exception.</summary>
        /// <param name="message">The error message that explains the reason for the exception.</param>
        /// <param name="innerException">The exception that is the cause of the current exception, or a null reference if no inner exception is specified.</param>
        public CommandTypeException(string message, Exception innerException)
            : base(message, innerException)
        {
        }
    }
}
```

## File: `src/CommandQuery/Exceptions/QueryException.cs`
```csharp
namespace CommandQuery.Exceptions
{
    /// <summary>
    /// Represents errors that occur during query processing in a query handler.
    /// Derive custom query exceptions from this class and add public properties to expose more error details.
    /// </summary>
    public class QueryException : Exception
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="QueryException"/> class.
        /// </summary>
        public QueryException()
        {
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="QueryException"/> class with a specified error message.
        /// </summary>
        /// <param name="message">The message that describes the error.</param>
        public QueryException(string message)
            : base(message)
        {
        }

        /// <summary>Initializes a new instance of the <see cref="QueryException"/> class with a specified error message and a reference to the inner exception that is the cause of this exception.</summary>
        /// <param name="message">The error message that explains the reason for the exception.</param>
        /// <param name="innerException">The exception that is the cause of the current exception, or a null reference if no inner exception is specified.</param>
        public QueryException(string message, Exception innerException)
            : base(message, innerException)
        {
        }
    }
}
```

## File: `src/CommandQuery/Exceptions/QueryProcessorException.cs`
```csharp
namespace CommandQuery.Exceptions
{
    /// <summary>
    /// Represents errors that occur during query processing in the <see cref="QueryProcessor"/>.
    /// </summary>
    public sealed class QueryProcessorException : Exception
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="QueryProcessorException"/> class.
        /// </summary>
        public QueryProcessorException()
        {
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="QueryProcessorException"/> class with a specified error message.
        /// </summary>
        /// <param name="message">The message that describes the error.</param>
        public QueryProcessorException(string message)
            : base(message)
        {
        }

        /// <summary>Initializes a new instance of the <see cref="QueryProcessorException"/> class with a specified error message and a reference to the inner exception that is the cause of this exception.</summary>
        /// <param name="message">The error message that explains the reason for the exception.</param>
        /// <param name="innerException">The exception that is the cause of the current exception, or a null reference if no inner exception is specified.</param>
        public QueryProcessorException(string message, Exception innerException)
            : base(message, innerException)
        {
        }
    }
}
```

## File: `src/CommandQuery/Exceptions/QueryTypeException.cs`
```csharp
namespace CommandQuery.Exceptions
{
    /// <summary>
    /// Represents errors that occur during initialization of a <see cref="QueryTypeProvider"/>.
    /// </summary>
    public sealed class QueryTypeException : Exception
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="QueryTypeException"/> class.
        /// </summary>
        public QueryTypeException()
        {
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="QueryTypeException"/> class with a specified error message.
        /// </summary>
        /// <param name="message">The message that describes the error.</param>
        public QueryTypeException(string message)
            : base(message)
        {
        }

        /// <summary>Initializes a new instance of the <see cref="QueryTypeException"/> class with a specified error message and a reference to the inner exception that is the cause of this exception.</summary>
        /// <param name="message">The error message that explains the reason for the exception.</param>
        /// <param name="innerException">The exception that is the cause of the current exception, or a null reference if no inner exception is specified.</param>
        public QueryTypeException(string message, Exception innerException)
            : base(message, innerException)
        {
        }
    }
}
```

## File: `src/CommandQuery/Internal/DictionaryExtensions.cs`
```csharp
using System.Collections;

namespace CommandQuery
{
    internal static class DictionaryExtensions
    {
        internal static Dictionary<string, object>? GetQueryDictionary(this IDictionary<string, IEnumerable<string>>? query, Type type)
        {
            if (query is null)
            {
                return null;
            }

            var properties = type.GetProperties();

            var result = query.ToDictionary(g => g.Key, Token, StringComparer.OrdinalIgnoreCase);

            var nestedKeys = result.Keys.Where(x => x.Contains('.')).ToList();

            foreach (var key in nestedKeys)
            {
                var path = key.Split('.');
                var ancestorCount = key.Count(x => x == '.');

                Dictionary<string, object> parent = result;

                foreach (var ancestor in path.Take(ancestorCount))
                {
                    if (parent!.ContainsKey(ancestor))
                    {
                        parent = (Dictionary<string, object>)parent[ancestor];
                    }
                    else
                    {
                        var temp = new Dictionary<string, object>();
                        parent.Add(ancestor, temp);
                        parent = temp;
                    }
                }

                parent.Add(path.Last(), result[key]);
                result.Remove(key);
            }

            return result;

            object Token(KeyValuePair<string, IEnumerable<string>> kv)
            {
                var property = properties.FirstOrDefault(x => string.Equals(x.Name, kv.Key, StringComparison.OrdinalIgnoreCase));
                var isEnumerable = property?.PropertyType != typeof(string) && typeof(IEnumerable).IsAssignableFrom(property?.PropertyType);

                return (isEnumerable ? kv.Value : kv.Value.FirstOrDefault())!;
            }
        }
    }
}
```

## File: `src/CommandQuery/Internal/Error.cs`
```csharp
namespace CommandQuery
{
    internal class Error : IError
    {
        internal Error(string message)
        {
            Message = message;
        }

        internal Error(string message, Dictionary<string, object>? details)
        {
            Message = message;
            Details = details;
        }

        public string? Message { get; }

        public Dictionary<string, object>? Details { get; }
    }
}
```

## File: `src/CommandQuery/Internal/ExceptionExtensions.cs`
```csharp
using System.Reflection;
using CommandQuery.Exceptions;

namespace CommandQuery
{
    internal static class ExceptionExtensions
    {
        internal static bool IsHandled(this Exception exception)
        {
            return
                exception is CommandProcessorException ||
                exception is CommandException ||
                exception is QueryProcessorException ||
                exception is QueryException;
        }

        internal static IError ToError(this Exception exception)
        {
            return exception switch
            {
                CommandException commandException => commandException.ToError(),
                QueryException queryException => queryException.ToError(),
                _ => new Error(exception.Message),
            };
        }

        internal static IError ToError(this CommandException exception)
        {
            return new Error(exception.Message, GetDetails(exception));
        }

        internal static IError ToError(this QueryException exception)
        {
            return new Error(exception.Message, GetDetails(exception));
        }

        private static Dictionary<string, object>? GetDetails(Exception exception)
        {
            var properties = exception.GetType().GetProperties(BindingFlags.Public | BindingFlags.Instance)
                .Where(x => x.DeclaringType != typeof(Exception) && x.GetValue(exception) != null)
                .ToList();

            return properties.Any() ? properties.ToDictionary(property => property.Name, property => property.GetValue(exception)) : null;
        }
    }
}
```

## File: `src/CommandQuery/Internal/ReflectionExtensions.cs`
```csharp
using System.Reflection;

namespace CommandQuery
{
    internal static class ReflectionExtensions
    {
        internal static IEnumerable<Type> GetTypesAssignableTo(this Assembly[] assemblies, Type baseType)
        {
            return assemblies.SelectMany(x => x.GetTypesAssignableTo(baseType)).ToList();
        }

        internal static IEnumerable<Type> GetTypesAssignableTo(this Assembly assembly, Type baseType)
        {
            return assembly.ExportedTypes.Where(type => type.IsAssignableToType(baseType)).ToList();
        }

        internal static bool IsAssignableToType(this Type type, Type baseType)
        {
            return type.IsClass && (baseType.IsAssignableFrom(type) || IsAssignableToGenericType(type, baseType));
        }

        internal static Type? GetResultType(this Type type, Type baseType)
        {
            return type.GetInterfaces()
                .Where(i => i.IsGenericType && i.GetGenericTypeDefinition() == baseType)
                .Select(i => i.GetGenericArguments()[0])
                .FirstOrDefault();
        }

        internal static IEnumerable<Type> GetHandlerInterfaceTypes(this Type type, Type genericType)
        {
            return type.GetInterfaces().Where(it => it.GetTypeInfo().IsGenericType && it.GetGenericTypeDefinition() == genericType).ToList();
        }

        private static bool IsAssignableToGenericType(this Type type, Type genericType)
        {
            return type.GetInterfaces().Any(it => it.GetTypeInfo().IsGenericType && it.GetGenericTypeDefinition() == genericType)
                   || (type.GetTypeInfo().IsGenericType && type.GetGenericTypeDefinition() == genericType)
                   || (type.GetTypeInfo().BaseType?.IsAssignableToGenericType(genericType) == true);
        }
    }
}
```

## File: `src/CommandQuery/Internal/ServiceProviderExtensions.cs`
```csharp
using System.Reflection;
using Microsoft.Extensions.DependencyInjection;

namespace CommandQuery
{
    internal static class ServiceProviderExtensions
    {
        internal static object? GetSingleService(this IServiceProvider provider, Type serviceType)
        {
            if (provider is null)
            {
                throw new ArgumentNullException(nameof(provider));
            }

            if (serviceType is null)
            {
                throw new ArgumentNullException(nameof(serviceType));
            }

            var enumerableType = typeof(IEnumerable<>).MakeGenericType(serviceType);
            var services = provider.GetService(enumerableType) as IEnumerable<object>;

            return services?.SingleOrDefault();
        }

        internal static IEnumerable<Type> GetAllServiceTypes(this IServiceProvider provider)
        {
            if (provider is not ServiceProvider serviceProvider)
            {
                return [];
            }

            var callSiteFactory = GetPropertyValue(serviceProvider, "CallSiteFactory");
            var descriptors = GetPropertyValue(callSiteFactory, "Descriptors");

            if (descriptors is not ServiceDescriptor[] array)
            {
                return [];
            }

            return array.Select(x => x.ServiceType).ToList();

            static object? GetPropertyValue(object? obj, string name)
            {
                return obj?.GetType().GetProperty(name, BindingFlags.Instance | BindingFlags.NonPublic)?.GetValue(obj, null);
            }
        }
    }
}
```

## File: `src/CommandQuery.AWSLambda/CommandFunction.cs`
```csharp
using System.Net;
using System.Text.Json;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using CommandQuery.SystemTextJson;

namespace CommandQuery.AWSLambda
{
    /// <summary>
    /// Handles commands for the Lambda function.
    /// </summary>
    public class CommandFunction : ICommandFunction
    {
        private readonly ICommandProcessor _commandProcessor;
        private readonly JsonSerializerOptions? _options;

        /// <summary>
        /// Initializes a new instance of the <see cref="CommandFunction"/> class.
        /// </summary>
        /// <param name="commandProcessor">An <see cref="ICommandProcessor"/>.</param>
        /// <param name="options"><see cref="JsonSerializerOptions"/> to control the behavior during deserialization of <see cref="APIGatewayProxyRequest.Body"/> and serialization of <see cref="APIGatewayProxyResponse.Body"/>.</param>
        public CommandFunction(ICommandProcessor commandProcessor, JsonSerializerOptions? options = null)
        {
            _commandProcessor = commandProcessor;
            _options = options;
        }

        /// <inheritdoc />
        public async Task<APIGatewayProxyResponse> HandleAsync(string commandName, APIGatewayProxyRequest request, ILambdaLogger logger)
        {
            logger.LogLine($"Handle {commandName}");

            if (request is null)
            {
                throw new ArgumentNullException(nameof(request));
            }

            try
            {
                var result = await _commandProcessor.ProcessAsync(commandName, request.Body, _options).ConfigureAwait(false);

                if (result == CommandResult.None)
                {
                    return new APIGatewayProxyResponse { StatusCode = (int)HttpStatusCode.OK };
                }

                return request.Ok(result.Value, _options);
            }
            catch (Exception exception)
            {
                logger.LogLine($"Handle command failed: {commandName}, {request.Body}, {exception.Message}");

                return exception.IsHandled() ? request.BadRequest(exception, _options) : request.InternalServerError(exception, _options);
            }
        }

        /// <inheritdoc />
        public async Task<APIGatewayHttpApiV2ProxyResponse> HandleAsync(string commandName, APIGatewayHttpApiV2ProxyRequest request, ILambdaLogger logger)
        {
            logger.LogLine($"Handle {commandName}");

            if (request is null)
            {
                throw new ArgumentNullException(nameof(request));
            }

            try
            {
                var result = await _commandProcessor.ProcessAsync(commandName, request.Body, _options).ConfigureAwait(false);

                if (result == CommandResult.None)
                {
                    return new APIGatewayHttpApiV2ProxyResponse { StatusCode = (int)HttpStatusCode.OK };
                }

                return request.Ok(result.Value, _options);
            }
            catch (Exception exception)
            {
                logger.LogLine($"Handle command failed: {commandName}, {request.Body}, {exception.Message}");

                return exception.IsHandled() ? request.BadRequest(exception, _options) : request.InternalServerError(exception, _options);
            }
        }
    }
}
```

## File: `src/CommandQuery.AWSLambda/CommandQuery.AWSLambda.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>netstandard2.0</TargetFramework>
    <Version>4.0.0</Version>
    <PackageReleaseNotes>
- Bump Amazon.Lambda.Core to 2.2.0
- Bump Amazon.Lambda.APIGatewayEvents to 2.7.0
- Make ILambdaLogger parameter required for HandleAsync
- Add support for APIGatewayHttpApiV2ProxyRequest
    </PackageReleaseNotes>
    <Authors>Henrik Lau Eriksson</Authors>
    <Description>Command Query Separation for AWS Lambda ⚡

✔️ Provides generic function support for commands and queries with Amazon API Gateway
✔️ Enables APIs based on HTTP POST and GET
📄 https://hlaueriksson.me/CommandQuery.AWSLambda/
    </Description>
    <PackageId>CommandQuery.AWSLambda</PackageId>
    <PackageProjectUrl>https://github.com/hlaueriksson/CommandQuery</PackageProjectUrl>
    <PackageIcon>icon.png</PackageIcon>
    <PackageReadmeFile>CommandQuery.AWSLambda.md</PackageReadmeFile>
    <PackageTags>CommandQuery;Command;Query;CQS;AWS;Amazon;Lambda</PackageTags>
    <PackageLicenseExpression>MIT</PackageLicenseExpression>
    <GenerateDocumentationFile>true</GenerateDocumentationFile>
  </PropertyGroup>

  <ItemGroup>
    <None Include="..\..\icon.png" Link="icon.png" Pack="true" PackagePath="\" />
    <None Include="..\..\CommandQuery.AWSLambda.md" Pack="true" PackagePath="\" />
  </ItemGroup>

  <Import Project="../../Analyzers.props" />

  <ItemGroup>
    <InternalsVisibleTo Include="CommandQuery.AWSLambda.Tests" />
  </ItemGroup>

  <ItemGroup>
    <PackageReference Include="Amazon.Lambda.Core" Version="2.2.0" />
    <PackageReference Include="Amazon.Lambda.APIGatewayEvents" Version="2.7.0" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\CommandQuery.SystemTextJson\CommandQuery.SystemTextJson.csproj" />
    <ProjectReference Include="..\CommandQuery\CommandQuery.csproj" />
  </ItemGroup>

</Project>
```

## File: `src/CommandQuery.AWSLambda/ICommandFunction.cs`
```csharp
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;

namespace CommandQuery.AWSLambda
{
    /// <summary>
    /// Handles commands for the Lambda function.
    /// </summary>
    public interface ICommandFunction
    {
        /// <summary>
        /// Handle a command.
        /// </summary>
        /// <param name="commandName">The name of the command.</param>
        /// <param name="request">An <see cref="APIGatewayProxyRequest"/>.</param>
        /// <param name="logger">An <see cref="ILambdaLogger"/>.</param>
        /// <returns>The result for status code <c>200</c>, or an error for status code <c>400</c> and <c>500</c>.</returns>
        /// <exception cref="ArgumentNullException"><paramref name="request"/> is <see langword="null"/>.</exception>
        Task<APIGatewayProxyResponse> HandleAsync(string commandName, APIGatewayProxyRequest request, ILambdaLogger logger);

        /// <summary>
        /// Handle a command.
        /// </summary>
        /// <param name="commandName">The name of the command.</param>
        /// <param name="request">An <see cref="APIGatewayHttpApiV2ProxyRequest"/>.</param>
        /// <param name="logger">An <see cref="ILambdaLogger"/>.</param>
        /// <returns>The result for status code <c>200</c>, or an error for status code <c>400</c> and <c>500</c>.</returns>
        /// <exception cref="ArgumentNullException"><paramref name="request"/> is <see langword="null"/>.</exception>
        Task<APIGatewayHttpApiV2ProxyResponse> HandleAsync(string commandName, APIGatewayHttpApiV2ProxyRequest request, ILambdaLogger logger);
    }
}
```

## File: `src/CommandQuery.AWSLambda/IQueryFunction.cs`
```csharp
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;

namespace CommandQuery.AWSLambda
{
    /// <summary>
    /// Handles queries for the Lambda function.
    /// </summary>
    public interface IQueryFunction
    {
        /// <summary>
        /// Handle a query.
        /// </summary>
        /// <param name="queryName">The name of the query.</param>
        /// <param name="request">An <see cref="APIGatewayProxyRequest"/>.</param>
        /// <param name="logger">An <see cref="ILambdaLogger"/>.</param>
        /// <returns>The result for status code <c>200</c>, or an error for status code <c>400</c> and <c>500</c>.</returns>
        /// <exception cref="ArgumentNullException"><paramref name="request"/> is <see langword="null"/>.</exception>
        Task<APIGatewayProxyResponse> HandleAsync(string queryName, APIGatewayProxyRequest request, ILambdaLogger logger);

        /// <summary>
        /// Handle a query.
        /// </summary>
        /// <param name="queryName">The name of the query.</param>
        /// <param name="request">An <see cref="APIGatewayHttpApiV2ProxyRequest"/>.</param>
        /// <param name="logger">An <see cref="ILambdaLogger"/>.</param>
        /// <returns>The result for status code <c>200</c>, or an error for status code <c>400</c> and <c>500</c>.</returns>
        /// <exception cref="ArgumentNullException"><paramref name="request"/> is <see langword="null"/>.</exception>
        Task<APIGatewayHttpApiV2ProxyResponse> HandleAsync(string queryName, APIGatewayHttpApiV2ProxyRequest request, ILambdaLogger logger);
    }
}
```

## File: `src/CommandQuery.AWSLambda/QueryFunction.cs`
```csharp
using System.Text.Json;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using CommandQuery.SystemTextJson;

namespace CommandQuery.AWSLambda
{
    /// <summary>
    /// Handles queries for the Lambda function.
    /// </summary>
    public class QueryFunction : IQueryFunction
    {
        private readonly IQueryProcessor _queryProcessor;
        private readonly JsonSerializerOptions? _options;

        /// <summary>
        /// Initializes a new instance of the <see cref="QueryFunction"/> class.
        /// </summary>
        /// <param name="queryProcessor">An <see cref="IQueryProcessor"/>.</param>
        /// <param name="options"><see cref="JsonSerializerOptions"/> to control the behavior during deserialization of <see cref="APIGatewayProxyRequest.Body"/> and serialization of <see cref="APIGatewayProxyResponse.Body"/>.</param>
        public QueryFunction(IQueryProcessor queryProcessor, JsonSerializerOptions? options = null)
        {
            _queryProcessor = queryProcessor;
            _options = options;
        }

        /// <inheritdoc />
        public async Task<APIGatewayProxyResponse> HandleAsync(string queryName, APIGatewayProxyRequest request, ILambdaLogger logger)
        {
            logger.LogLine($"Handle {queryName}");

            if (request is null)
            {
                throw new ArgumentNullException(nameof(request));
            }

            try
            {
                var result = request.HttpMethod == "GET"
                    ? await _queryProcessor.ProcessAsync<object>(queryName, Dictionary(request.MultiValueQueryStringParameters)).ConfigureAwait(false)
                    : await _queryProcessor.ProcessAsync<object>(queryName, request.Body, _options).ConfigureAwait(false);

                return request.Ok(result, _options);
            }
            catch (Exception exception)
            {
                var payload = request.HttpMethod == "GET" ? request.Path : request.Body;
                logger.LogLine($"Handle query failed: {queryName}, {payload}, {exception.Message}");

                return exception.IsHandled() ? request.BadRequest(exception, _options) : request.InternalServerError(exception, _options);
            }

            static Dictionary<string, IEnumerable<string>> Dictionary(IDictionary<string, IList<string>> query)
            {
                return query.ToDictionary(kv => kv.Key, kv => kv.Value as IEnumerable<string>, StringComparer.OrdinalIgnoreCase);
            }
        }

        /// <inheritdoc />
        public async Task<APIGatewayHttpApiV2ProxyResponse> HandleAsync(string queryName, APIGatewayHttpApiV2ProxyRequest request, ILambdaLogger logger)
        {
            logger.LogLine($"Handle {queryName}");

            if (request is null)
            {
                throw new ArgumentNullException(nameof(request));
            }

            try
            {
                var result = request.RequestContext.Http.Method == "GET"
                    ? await _queryProcessor.ProcessAsync<object>(queryName, Dictionary(request.QueryStringParameters)).ConfigureAwait(false)
                    : await _queryProcessor.ProcessAsync<object>(queryName, request.Body, _options).ConfigureAwait(false);

                return request.Ok(result, _options);
            }
            catch (Exception exception)
            {
                var payload = request.RequestContext.Http.Method == "GET" ? request.RequestContext.Http.Path : request.Body;
                logger.LogLine($"Handle query failed: {queryName}, {payload}, {exception.Message}");

                return exception.IsHandled() ? request.BadRequest(exception, _options) : request.InternalServerError(exception, _options);
            }

            static Dictionary<string, IEnumerable<string>> Dictionary(IDictionary<string, string> query)
            {
                return query.ToDictionary(kv => kv.Key, kv => kv.Value.Split(',') as IEnumerable<string>, StringComparer.OrdinalIgnoreCase);
            }
        }
    }
}
```

## File: `src/CommandQuery.AWSLambda/ServiceCollectionExtensions.cs`
```csharp
using System.Reflection;
using CommandQuery.DependencyInjection;
using Microsoft.Extensions.DependencyInjection;

namespace CommandQuery.AWSLambda
{
    /// <summary>
    /// Extensions methods for <see cref="IServiceCollection"/>.
    /// </summary>
    public static class ServiceCollectionExtensions
    {
        /// <summary>
        /// Adds function and command handlers to the <see cref="IServiceCollection"/>.
        /// </summary>
        /// <param name="services">The <see cref="IServiceCollection"/>.</param>
        /// <param name="assemblies">Assemblies with command handlers.</param>
        /// <returns>The <see cref="IServiceCollection"/>.</returns>
        public static IServiceCollection AddCommandFunction(this IServiceCollection services, params Assembly[] assemblies)
        {
            services.AddSingleton<ICommandFunction, CommandFunction>();
            services.AddCommands(assemblies);

            return services;
        }

        /// <summary>
        /// Adds function and query handlers to the <see cref="IServiceCollection"/>.
        /// </summary>
        /// <param name="services">The <see cref="IServiceCollection"/>.</param>
        /// <param name="assemblies">Assemblies with query handlers.</param>
        /// <returns>The <see cref="IServiceCollection"/>.</returns>
        public static IServiceCollection AddQueryFunction(this IServiceCollection services, params Assembly[] assemblies)
        {
            services.AddSingleton<IQueryFunction, QueryFunction>();
            services.AddQueries(assemblies);

            return services;
        }
    }
}
```

## File: `src/CommandQuery.AWSLambda/Internal/APIGatewayHttpApiV2ProxyRequestExtensions.cs`
```csharp
using System.Net;
using System.Text.Json;
using Amazon.Lambda.APIGatewayEvents;

namespace CommandQuery.AWSLambda
{
    internal static class APIGatewayHttpApiV2ProxyRequestExtensions
    {
        internal static APIGatewayHttpApiV2ProxyResponse Ok(this APIGatewayHttpApiV2ProxyRequest request, object? result, JsonSerializerOptions? options = null)
        {
            return new()
            {
                StatusCode = (int)HttpStatusCode.OK,
                Body = JsonSerializer.Serialize(result, options),
                Headers = new Dictionary<string, string> { { "Content-Type", "application/json; charset=utf-8" } },
            };
        }

        internal static APIGatewayHttpApiV2ProxyResponse BadRequest(this APIGatewayHttpApiV2ProxyRequest request, Exception exception, JsonSerializerOptions? options = null)
        {
            return new()
            {
                StatusCode = (int)HttpStatusCode.BadRequest,
                Body = JsonSerializer.Serialize(exception.ToError(), options),
                Headers = new Dictionary<string, string> { { "Content-Type", "application/json; charset=utf-8" } },
            };
        }

        internal static APIGatewayHttpApiV2ProxyResponse InternalServerError(this APIGatewayHttpApiV2ProxyRequest request, Exception exception, JsonSerializerOptions? options = null)
        {
            return new()
            {
                StatusCode = (int)HttpStatusCode.InternalServerError,
                Body = JsonSerializer.Serialize(exception.ToError(), options),
                Headers = new Dictionary<string, string> { { "Content-Type", "application/json; charset=utf-8" } },
            };
        }
    }
}
```

## File: `src/CommandQuery.AWSLambda/Internal/APIGatewayProxyRequestExtensions.cs`
```csharp
using System.Net;
using System.Text.Json;
using Amazon.Lambda.APIGatewayEvents;

namespace CommandQuery.AWSLambda
{
    internal static class APIGatewayProxyRequestExtensions
    {
        internal static APIGatewayProxyResponse Ok(this APIGatewayProxyRequest request, object? result, JsonSerializerOptions? options = null)
        {
            return new()
            {
                StatusCode = (int)HttpStatusCode.OK,
                Body = JsonSerializer.Serialize(result, options),
                Headers = new Dictionary<string, string> { { "Content-Type", "application/json; charset=utf-8" } },
            };
        }

        internal static APIGatewayProxyResponse BadRequest(this APIGatewayProxyRequest request, Exception exception, JsonSerializerOptions? options = null)
        {
            return new()
            {
                StatusCode = (int)HttpStatusCode.BadRequest,
                Body = JsonSerializer.Serialize(exception.ToError(), options),
                Headers = new Dictionary<string, string> { { "Content-Type", "application/json; charset=utf-8" } },
            };
        }

        internal static APIGatewayProxyResponse InternalServerError(this APIGatewayProxyRequest request, Exception exception, JsonSerializerOptions? options = null)
        {
            return new()
            {
                StatusCode = (int)HttpStatusCode.InternalServerError,
                Body = JsonSerializer.Serialize(exception.ToError(), options),
                Headers = new Dictionary<string, string> { { "Content-Type", "application/json; charset=utf-8" } },
            };
        }
    }
}
```

## File: `src/CommandQuery.Abstractions/CommandQuery.Abstractions.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>netstandard2.0</TargetFramework>
    <RootNamespace>CommandQuery</RootNamespace>
    <Version>4.0.0</Version>
    <PackageReleaseNotes>
    </PackageReleaseNotes>
    <Authors>Henrik Lau Eriksson</Authors>
    <Description>Interfaces for CommandQuery

✔️ ICommand / ICommandHandler&lt;in TCommand&gt;
✔️ ICommand&lt;TResult&gt; / ICommandHandler&lt;in TCommand, TResult&gt;
✔️ IQuery&lt;TResult&gt; / IQueryHandler&lt;in TQuery, TResult&gt;
📄 https://hlaueriksson.me/CommandQuery/
    </Description>
    <PackageId>CommandQuery.Abstractions</PackageId>
    <PackageProjectUrl>https://github.com/hlaueriksson/CommandQuery</PackageProjectUrl>
    <PackageIcon>icon.png</PackageIcon>
    <PackageReadmeFile>CommandQuery.Abstractions.md</PackageReadmeFile>
    <PackageTags>CommandQuery;Command;Query;CQS</PackageTags>
    <PackageLicenseExpression>MIT</PackageLicenseExpression>
    <GenerateDocumentationFile>true</GenerateDocumentationFile>
  </PropertyGroup>

  <ItemGroup>
    <None Include="..\..\icon.png" Link="icon.png" Pack="true" PackagePath="\" />
    <None Include="..\..\CommandQuery.Abstractions.md" Pack="true" PackagePath="\" />
  </ItemGroup>

  <Import Project="../../Analyzers.props" />

</Project>
```

## File: `src/CommandQuery.Abstractions/ICommand.cs`
```csharp
namespace CommandQuery
{
    /// <summary>
    /// Marker interface to represent a command.
    /// </summary>
    public interface ICommand;

    /// <summary>
    /// Marker interface to represent a command with result.
    /// </summary>
    /// <typeparam name="TResult">Result type.</typeparam>
    public interface ICommand<TResult>;
}
```

## File: `src/CommandQuery.Abstractions/ICommandHandler.cs`
```csharp
namespace CommandQuery
{
    /// <summary>
    /// Defines a handler for a command.
    /// </summary>
    /// <typeparam name="TCommand">The type of command being handled.</typeparam>
    public interface ICommandHandler<in TCommand>
        where TCommand : ICommand
    {
        /// <summary>
        /// Handles a command.
        /// </summary>
        /// <param name="command">The command.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>A task that represents the asynchronous operation.</returns>
        Task HandleAsync(TCommand command, CancellationToken cancellationToken);
    }

    /// <summary>
    /// Defines a handler for a command with result.
    /// </summary>
    /// <typeparam name="TCommand">The type of command being handled.</typeparam>
    /// <typeparam name="TResult">The type of result from the handler.</typeparam>
    public interface ICommandHandler<in TCommand, TResult>
        where TCommand : ICommand<TResult>
    {
        /// <summary>
        /// Handles a command.
        /// </summary>
        /// <param name="command">The command.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>Result from the command.</returns>
        Task<TResult> HandleAsync(TCommand command, CancellationToken cancellationToken);
    }
}
```

## File: `src/CommandQuery.Abstractions/IError.cs`
```csharp
namespace CommandQuery
{
    /// <summary>
    /// Represents an error that occurred during the processing of a command or query.
    /// </summary>
    public interface IError
    {
        /// <summary>
        /// A message that describes the error.
        /// </summary>
        public string? Message { get; }

        /// <summary>
        /// Details about the error.
        /// </summary>
        public Dictionary<string, object>? Details { get; }
    }
}
```

## File: `src/CommandQuery.Abstractions/IQuery.cs`
```csharp
namespace CommandQuery
{
    /// <summary>
    /// Marker interface to represent a query.
    /// </summary>
    /// <typeparam name="TResult">Result type.</typeparam>
    public interface IQuery<TResult>;
}
```

## File: `src/CommandQuery.Abstractions/IQueryHandler.cs`
```csharp
namespace CommandQuery
{
    /// <summary>
    /// Defines a handler for a query.
    /// </summary>
    /// <typeparam name="TQuery">The type of query being handled.</typeparam>
    /// <typeparam name="TResult">The type of result from the handler.</typeparam>
    public interface IQueryHandler<in TQuery, TResult>
        where TQuery : IQuery<TResult>
    {
        /// <summary>
        /// Handles a query.
        /// </summary>
        /// <param name="query">The query.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>Result from the query.</returns>
        Task<TResult> HandleAsync(TQuery query, CancellationToken cancellationToken);
    }
}
```

## File: `src/CommandQuery.AspNetCore/CommandControllerFeatureProvider.cs`
```csharp
using System.Reflection;
using Microsoft.AspNetCore.Mvc.ApplicationParts;
using Microsoft.AspNetCore.Mvc.Controllers;

namespace CommandQuery.AspNetCore
{
    /// <summary>
    /// Populates the list of controller types in an MVC application with controllers for all commands found in the provided assemblies.
    /// </summary>
    public class CommandControllerFeatureProvider : IApplicationFeatureProvider<ControllerFeature>
    {
        private readonly Type[] _types;

        /// <summary>
        /// Initializes a new instance of the <see cref="CommandControllerFeatureProvider"/> class.
        /// </summary>
        /// <param name="assemblies">The assemblies with commands to create controllers for.</param>
        public CommandControllerFeatureProvider(params Assembly[] assemblies)
        {
            _types = assemblies.GetTypesAssignableTo(typeof(ICommand)).Concat(assemblies.GetTypesAssignableTo(typeof(ICommand<>))).ToArray();
        }

        /// <summary>
        /// Populates the list of controller types in an MVC application with controllers for all commands found in the provided assemblies.
        /// </summary>
        /// <param name="parts">The list of <see cref="ApplicationPart"/> instances in the application.
        /// </param>
        /// <param name="feature">The feature instance to populate.</param>
        /// <exception cref="ArgumentNullException"><paramref name="feature"/> is <see langword="null"/>.</exception>
        public void PopulateFeature(IEnumerable<ApplicationPart> parts, ControllerFeature feature)
        {
            ArgumentNullException.ThrowIfNull(feature);

            foreach (var commandType in _types.Where(x => x.IsAssignableToType(typeof(ICommand))))
            {
                var controllerType = typeof(CommandController<>).MakeGenericType(commandType);

                feature.Controllers.Add(controllerType.GetTypeInfo());
            }

            foreach (var commandType in _types.Where(x => x.IsAssignableToType(typeof(ICommand<>))))
            {
                var controllerType = typeof(CommandController<,>).MakeGenericType(commandType, commandType.GetResultType(typeof(ICommand<>))!);

                feature.Controllers.Add(controllerType.GetTypeInfo());
            }
        }
    }
}
```

## File: `src/CommandQuery.AspNetCore/CommandQuery.AspNetCore.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Version>4.0.0</Version>
    <PackageReleaseNotes>
- Change TargetFramework to net8.0
    </PackageReleaseNotes>
    <Authors>Henrik Lau Eriksson</Authors>
    <Description>Command Query Separation for ASP.NET Core 🌐

✔️ Provides generic actions for handling the execution of commands and queries
✔️ Enables APIs based on HTTP POST and GET
📄 https://hlaueriksson.me/CommandQuery.AspNetCore/
    </Description>
    <PackageId>CommandQuery.AspNetCore</PackageId>
    <PackageProjectUrl>https://github.com/hlaueriksson/CommandQuery</PackageProjectUrl>
    <PackageIcon>icon.png</PackageIcon>
    <PackageReadmeFile>CommandQuery.AspNetCore.md</PackageReadmeFile>
    <PackageTags>CommandQuery;Command;Query;CQS;aspnetcore</PackageTags>
    <PackageLicenseExpression>MIT</PackageLicenseExpression>
    <GenerateDocumentationFile>true</GenerateDocumentationFile>
  </PropertyGroup>

  <ItemGroup>
    <None Include="..\..\icon.png" Link="icon.png" Pack="true" PackagePath="\" />
    <None Include="..\..\CommandQuery.AspNetCore.md" Pack="true" PackagePath="\" />
  </ItemGroup>

  <Import Project="../../Analyzers.props" />

  <ItemGroup>
    <InternalsVisibleTo Include="CommandQuery.AspNetCore.Tests" />
    <InternalsVisibleTo Include="DynamicProxyGenAssembly2" />
  </ItemGroup>

  <ItemGroup>
    <FrameworkReference Include="Microsoft.AspNetCore.App" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\CommandQuery\CommandQuery.csproj" />
  </ItemGroup>

</Project>
```

## File: `src/CommandQuery.AspNetCore/CommandQueryControllerModelConvention.cs`
```csharp
using Microsoft.AspNetCore.Mvc.ApplicationModels;

namespace CommandQuery.AspNetCore
{
    /// <summary>
    /// Customizes the name of controllers for commands and queries.
    /// </summary>
    public class CommandQueryControllerModelConvention : IControllerModelConvention
    {
        /// <summary>
        /// Applies the naming convention of controllers for commands and queries.
        /// </summary>
        /// <param name="controller">The <see cref="ControllerModel"/>.</param>
        /// <exception cref="ArgumentNullException"><paramref name="controller"/> is <see langword="null"/>.</exception>
        public void Apply(ControllerModel controller)
        {
            ArgumentNullException.ThrowIfNull(controller);

            if (!controller.ControllerType.IsGenericType)
            {
                return;
            }

            var openControllerType = controller.ControllerType.GetGenericTypeDefinition();

            if (openControllerType != typeof(CommandController<>)
                && openControllerType != typeof(CommandController<,>)
                && openControllerType != typeof(QueryController<,>))
            {
                return;
            }

            controller.ControllerName = controller.ControllerType.GenericTypeArguments[0].Name;
        }
    }
}
```

## File: `src/CommandQuery.AspNetCore/CommandWithResultController.cs`
```csharp
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace CommandQuery.AspNetCore
{
    [ApiController]
    [Route("api/command/[controller]")]
#pragma warning disable SA1649 // File name should match first type name
    internal class CommandController<TCommand, TResult> : ControllerBase
#pragma warning restore SA1649 // File name should match first type name
        where TCommand : ICommand<TResult>
    {
        private readonly ICommandProcessor _commandProcessor;
        private readonly ILogger _logger;

        /// <summary>
        /// Initializes a new instance of the <see cref="CommandController{TCommand,TResult}"/> class.
        /// </summary>
        /// <param name="commandProcessor">An <see cref="ICommandProcessor"/>.</param>
        /// <param name="logger">An <see cref="ILogger"/>.</param>
        public CommandController(ICommandProcessor commandProcessor, ILogger<CommandController<TCommand, TResult>> logger)
        {
            _commandProcessor = commandProcessor;
            _logger = logger;
        }

        /// <summary>
        /// Handle a command.
        /// </summary>
        /// <param name="command">The command.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>The result for status code <c>200</c>, or an error for status code <c>400</c> and <c>500</c>.</returns>
        [HttpPost]
        public async Task<IActionResult> HandleAsync(TCommand command, CancellationToken cancellationToken)
        {
            _logger.LogInformation("Handle {@Command}", command);

            try
            {
                var result = await _commandProcessor.ProcessAsync(command, cancellationToken).ConfigureAwait(false);

                return Ok(result);
            }
            catch (Exception exception)
            {
                _logger.LogError(exception, "Handle command failed: {@Command}", command);

                return exception.IsHandled() ? BadRequest(exception.ToError()) : StatusCode(500, exception.ToError());
            }
        }
    }
}
```

## File: `src/CommandQuery.AspNetCore/CommandWithoutResultController.cs`
```csharp
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace CommandQuery.AspNetCore
{
    [ApiController]
    [Route("api/command/[controller]")]
#pragma warning disable SA1649 // File name should match first type name
    internal class CommandController<TCommand> : ControllerBase
#pragma warning restore SA1649 // File name should match first type name
        where TCommand : ICommand
    {
        private readonly ICommandProcessor _commandProcessor;
        private readonly ILogger _logger;

        /// <summary>
        /// Initializes a new instance of the <see cref="CommandController{TCommand}"/> class.
        /// </summary>
        /// <param name="commandProcessor">An <see cref="ICommandProcessor"/>.</param>
        /// <param name="logger">An <see cref="ILogger"/>.</param>
        public CommandController(ICommandProcessor commandProcessor, ILogger<CommandController<TCommand>> logger)
        {
            _commandProcessor = commandProcessor;
            _logger = logger;
        }

        /// <summary>
        /// Handle a command.
        /// </summary>
        /// <param name="command">The command.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>The result for status code <c>200</c>, or an error for status code <c>400</c> and <c>500</c>.</returns>
        [HttpPost]
        public async Task<IActionResult> HandleAsync(TCommand command, CancellationToken cancellationToken)
        {
            _logger.LogInformation("Handle {@Command}", command);

            try
            {
                await _commandProcessor.ProcessAsync(command, cancellationToken).ConfigureAwait(false);

                return Ok();
            }
            catch (Exception exception)
            {
                _logger.LogError(exception, "Handle command failed: {@Command}", command);

                return exception.IsHandled() ? BadRequest(exception.ToError()) : StatusCode(500, exception.ToError());
            }
        }
    }
}
```

## File: `src/CommandQuery.AspNetCore/QueryController.cs`
```csharp
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace CommandQuery.AspNetCore
{
    /// <summary>
    /// Base class for query controllers.
    /// </summary>
    [ApiController]
    [Route("api/query/[controller]")]
    internal class QueryController<TQuery, TResult> : ControllerBase
        where TQuery : IQuery<TResult>
    {
        private readonly IQueryProcessor _queryProcessor;
        private readonly ILogger _logger;

        /// <summary>
        /// Initializes a new instance of the <see cref="QueryController{TQuery,TResult}"/> class.
        /// </summary>
        /// <param name="queryProcessor">An <see cref="IQueryProcessor"/>.</param>
        /// <param name="logger">An <see cref="ILogger"/>.</param>
        public QueryController(IQueryProcessor queryProcessor, ILogger<QueryController<TQuery, TResult>> logger)
        {
            _queryProcessor = queryProcessor;
            _logger = logger;
        }

        /// <summary>
        /// Handle a query.
        /// </summary>
        /// <param name="query">The query.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>The result + 200, 400 or 500.</returns>
        [HttpPost]
        public async Task<IActionResult> HandlePostAsync(TQuery query, CancellationToken cancellationToken)
        {
            _logger.LogInformation("Handle {@Query}", query);

            try
            {
                var result = await _queryProcessor.ProcessAsync(query, cancellationToken).ConfigureAwait(false);

                return Ok(result);
            }
            catch (Exception exception)
            {
                _logger.LogError(exception, "Handle query failed: {@Query}", query);

                return exception.IsHandled() ? BadRequest(exception.ToError()) : StatusCode(500, exception.ToError());
            }
        }

        /// <summary>
        /// Handle a query.
        /// </summary>
        /// <param name="query">The query.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>The result + 200, 400 or 500.</returns>
        [HttpGet]
        public async Task<IActionResult> HandleGetAsync([FromQuery] TQuery query, CancellationToken cancellationToken)
        {
            _logger.LogInformation("Handle {@Query}", query);

            try
            {
                var result = await _queryProcessor.ProcessAsync(query, cancellationToken).ConfigureAwait(false);

                return Ok(result);
            }
            catch (Exception exception)
            {
                _logger.LogError(exception, "Handle query failed: {@Query}", query);

                return exception.IsHandled() ? BadRequest(exception.ToError()) : StatusCode(500, exception.ToError());
            }
        }
    }
}
```

## File: `src/CommandQuery.AspNetCore/QueryControllerFeatureProvider.cs`
```csharp
using System.Reflection;
using Microsoft.AspNetCore.Mvc.ApplicationParts;
using Microsoft.AspNetCore.Mvc.Controllers;

namespace CommandQuery.AspNetCore
{
    /// <summary>
    /// Populates the list of controller types in an MVC application with controllers for all queries found in the provided assemblies.
    /// </summary>
    public class QueryControllerFeatureProvider : IApplicationFeatureProvider<ControllerFeature>
    {
        private readonly Type[] _types;

        /// <summary>
        /// Initializes a new instance of the <see cref="QueryControllerFeatureProvider"/> class.
        /// </summary>
        /// <param name="assemblies">The assemblies with queries to create controllers for.</param>
        public QueryControllerFeatureProvider(params Assembly[] assemblies)
        {
            _types = assemblies.GetTypesAssignableTo(typeof(IQuery<>)).ToArray();
        }

        /// <summary>
        /// Populates the list of controller types in an MVC application with controllers for all queries found in the provided assemblies.
        /// </summary>
        /// <param name="parts">The list of <see cref="ApplicationPart"/> instances in the application.
        /// </param>
        /// <param name="feature">The feature instance to populate.</param>
        /// <exception cref="ArgumentNullException"><paramref name="feature"/> is <see langword="null"/>.</exception>
        public void PopulateFeature(IEnumerable<ApplicationPart> parts, ControllerFeature feature)
        {
            ArgumentNullException.ThrowIfNull(feature);

            foreach (var queryType in _types)
            {
                var controllerType = typeof(QueryController<,>).MakeGenericType(queryType, queryType.GetResultType(typeof(IQuery<>))!);

                feature.Controllers.Add(controllerType.GetTypeInfo());
            }
        }
    }
}
```

## File: `src/CommandQuery.AspNetCore/ServiceCollectionExtensions.cs`
```csharp
using System.Reflection;
using CommandQuery.DependencyInjection;
using Microsoft.Extensions.DependencyInjection;

namespace CommandQuery.AspNetCore
{
    /// <summary>
    /// Extensions methods for <see cref="IServiceCollection"/>.
    /// </summary>
    public static class ServiceCollectionExtensions
    {
        /// <summary>
        /// Adds controllers and command handlers to the <see cref="IServiceCollection"/>.
        /// </summary>
        /// <param name="services">The <see cref="IServiceCollection"/>.</param>
        /// <param name="assemblies">Assemblies with command handlers.</param>
        /// <returns>The <see cref="IServiceCollection"/>.</returns>
        public static IServiceCollection AddCommandControllers(this IServiceCollection services, params Assembly[] assemblies)
        {
            services
                .AddControllers(options => options.Conventions.Add(new CommandQueryControllerModelConvention()))
                .ConfigureApplicationPartManager(manager => manager.FeatureProviders.Add(new CommandControllerFeatureProvider(assemblies)));
            services.AddCommands(assemblies);

            return services;
        }

        /// <summary>
        /// Adds controllers and query handlers to the <see cref="IServiceCollection"/>.
        /// </summary>
        /// <param name="services">The <see cref="IServiceCollection"/>.</param>
        /// <param name="assemblies">Assemblies with query handlers.</param>
        /// <returns>The <see cref="IServiceCollection"/>.</returns>
        public static IServiceCollection AddQueryControllers(this IServiceCollection services, params Assembly[] assemblies)
        {
            services
                .AddControllers(options => options.Conventions.Add(new CommandQueryControllerModelConvention()))
                .ConfigureApplicationPartManager(manager => manager.FeatureProviders.Add(new QueryControllerFeatureProvider(assemblies)));
            services.AddQueries(assemblies);

            return services;
        }
    }
}
```

## File: `src/CommandQuery.AzureFunctions/CommandFunction.cs`
```csharp
using System.Net;
using System.Text.Json;
using CommandQuery.SystemTextJson;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.Functions.Worker.Http;
using Microsoft.Extensions.Logging;

namespace CommandQuery.AzureFunctions
{
    /// <inheritdoc />
    public class CommandFunction : ICommandFunction
    {
        private readonly ICommandProcessor _commandProcessor;
        private readonly ILogger<CommandFunction> _logger;
        private readonly JsonSerializerOptions? _options;

        /// <summary>
        /// Initializes a new instance of the <see cref="CommandFunction"/> class.
        /// </summary>
        /// <param name="commandProcessor">An <see cref="ICommandProcessor"/>.</param>
        /// <param name="logger">An <see cref="ILogger{T}"/>.</param>
        /// <param name="options"><see cref="JsonSerializerOptions"/> to control the behavior during deserialization of <see cref="HttpRequestData.Body"/> and serialization of <see cref="HttpResponseData.Body"/>.</param>
        public CommandFunction(ICommandProcessor commandProcessor, ILogger<CommandFunction> logger, JsonSerializerOptions? options = null)
        {
            _commandProcessor = commandProcessor;
            _logger = logger;
            _options = options;
        }

        /// <inheritdoc />
        public async Task<HttpResponseData> HandleAsync(string commandName, HttpRequestData req, CancellationToken cancellationToken = default)
        {
            ArgumentNullException.ThrowIfNull(req);

            _logger.LogInformation("Handle {Command}", commandName);

            try
            {
                var result = await _commandProcessor.ProcessAsync(commandName, await req.ReadAsStringAsync().ConfigureAwait(false), _options, cancellationToken).ConfigureAwait(false);

                if (result == CommandResult.None)
                {
                    return req.CreateResponse(HttpStatusCode.OK);
                }

                return await req.OkAsync(result.Value, _options).ConfigureAwait(false);
            }
            catch (Exception exception)
            {
                var payload = await req.ReadAsStringAsync().ConfigureAwait(false);
                _logger.LogError(exception, "Handle command failed: {Command}, {Payload}", commandName, payload);

                return exception.IsHandled()
                    ? await req.BadRequestAsync(exception, _options).ConfigureAwait(false)
                    : await req.InternalServerErrorAsync(exception, _options).ConfigureAwait(false);
            }
        }

        /// <inheritdoc />
        public async Task<IActionResult> HandleAsync(string commandName, HttpRequest req, CancellationToken cancellationToken = default)
        {
            ArgumentNullException.ThrowIfNull(req);

            _logger.LogInformation("Handle {Command}", commandName);

            try
            {
                var result = await _commandProcessor.ProcessAsync(commandName, await req.ReadAsStringAsync().ConfigureAwait(false), _options, cancellationToken).ConfigureAwait(false);

                if (result == CommandResult.None)
                {
                    return new OkResult();
                }

                return new OkObjectResult(result.Value);
            }
            catch (Exception exception)
            {
                var payload = await req.ReadAsStringAsync().ConfigureAwait(false);
                _logger.LogError(exception, "Handle command failed: {Command}, {Payload}", commandName, payload);

                return exception.IsHandled()
                    ? new BadRequestObjectResult(exception.ToError())
                    : new ObjectResult(exception.ToError()) { StatusCode = StatusCodes.Status500InternalServerError };
            }
        }
    }
}
```

## File: `src/CommandQuery.AzureFunctions/CommandQuery.AzureFunctions.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Version>4.0.0</Version>
    <PackageReleaseNotes>
- Change TargetFramework to net8.0
- Bump Microsoft.Azure.Functions.Worker to 1.22.0
- Remove ILogger parameter from HandleAsync
- Add support for HttpRequest
    </PackageReleaseNotes>
    <Authors>Henrik Lau Eriksson</Authors>
    <Description>Command Query Separation for Azure Functions ⚡

✔️ Provides generic function support for commands and queries with HTTPTriggers
✔️ Enables APIs based on HTTP POST and GET
📄 https://hlaueriksson.me/CommandQuery.AzureFunctions/
    </Description>
    <PackageId>CommandQuery.AzureFunctions</PackageId>
    <PackageProjectUrl>https://github.com/hlaueriksson/CommandQuery</PackageProjectUrl>
    <PackageIcon>icon.png</PackageIcon>
    <PackageReadmeFile>CommandQuery.AzureFunctions.md</PackageReadmeFile>
    <PackageTags>CommandQuery;Command;Query;CQS;Microsoft;Azure;AzureFunctions</PackageTags>
    <PackageLicenseExpression>MIT</PackageLicenseExpression>
    <GenerateDocumentationFile>true</GenerateDocumentationFile>
  </PropertyGroup>

  <ItemGroup>
    <None Include="..\..\icon.png" Link="icon.png" Pack="true" PackagePath="\" />
    <None Include="..\..\CommandQuery.AzureFunctions.md" Pack="true" PackagePath="\" />
  </ItemGroup>

  <Import Project="../../Analyzers.props" />

  <ItemGroup>
    <InternalsVisibleTo Include="CommandQuery.AzureFunctions.Tests" />
  </ItemGroup>

  <ItemGroup>
    <FrameworkReference Include="Microsoft.AspNetCore.App" />
    <PackageReference Include="Microsoft.Azure.Functions.Worker" Version="1.22.0" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\CommandQuery.SystemTextJson\CommandQuery.SystemTextJson.csproj" />
    <ProjectReference Include="..\CommandQuery\CommandQuery.csproj" />
  </ItemGroup>

</Project>
```

## File: `src/CommandQuery.AzureFunctions/ICommandFunction.cs`
```csharp
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.Functions.Worker.Http;

namespace CommandQuery.AzureFunctions
{
    /// <summary>
    /// Handles commands for the Azure function.
    /// </summary>
    public interface ICommandFunction
    {
        /// <summary>
        /// Handle a command.
        /// </summary>
        /// <param name="commandName">The name of the command.</param>
        /// <param name="req">A <see cref="HttpRequestData"/>.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>The result for status code <c>200</c>, or an error for status code <c>400</c> and <c>500</c>.</returns>
        /// <exception cref="ArgumentNullException"><paramref name="req"/> is <see langword="null"/>.</exception>
        Task<HttpResponseData> HandleAsync(string commandName, HttpRequestData req, CancellationToken cancellationToken = default);

        /// <summary>
        /// Handle a command.
        /// </summary>
        /// <param name="commandName">The name of the command.</param>
        /// <param name="req">A <see cref="HttpRequest"/>.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>The result for status code <c>200</c>, or an error for status code <c>400</c> and <c>500</c>.</returns>
        /// <exception cref="ArgumentNullException"><paramref name="req"/> is <see langword="null"/>.</exception>
        Task<IActionResult> HandleAsync(string commandName, HttpRequest req, CancellationToken cancellationToken = default);
    }
}
```

## File: `src/CommandQuery.AzureFunctions/IQueryFunction.cs`
```csharp
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.Functions.Worker.Http;

namespace CommandQuery.AzureFunctions
{
    /// <summary>
    /// Handles queries for the Azure function.
    /// </summary>
    public interface IQueryFunction
    {
        /// <summary>
        /// Handle a query.
        /// </summary>
        /// <param name="queryName">The name of the query.</param>
        /// <param name="req">A <see cref="HttpRequestData"/>.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>The result for status code <c>200</c>, or an error for status code <c>400</c> and <c>500</c>.</returns>
        /// <exception cref="ArgumentNullException"><paramref name="req"/> is <see langword="null"/>.</exception>
        Task<HttpResponseData> HandleAsync(string queryName, HttpRequestData req, CancellationToken cancellationToken = default);

        /// <summary>
        /// Handle a query.
        /// </summary>
        /// <param name="queryName">The name of the query.</param>
        /// <param name="req">A <see cref="HttpRequest"/>.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>The result for status code <c>200</c>, or an error for status code <c>400</c> and <c>500</c>.</returns>
        /// <exception cref="ArgumentNullException"><paramref name="req"/> is <see langword="null"/>.</exception>
        Task<IActionResult> HandleAsync(string queryName, HttpRequest req, CancellationToken cancellationToken = default);
    }
}
```

## File: `src/CommandQuery.AzureFunctions/QueryFunction.cs`
```csharp
using System.Text.Json;
using System.Web;
using CommandQuery.SystemTextJson;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Http.Extensions;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.Functions.Worker.Http;
using Microsoft.Extensions.Logging;

namespace CommandQuery.AzureFunctions
{
    /// <inheritdoc />
    public class QueryFunction : IQueryFunction
    {
        private readonly IQueryProcessor _queryProcessor;
        private readonly ILogger<QueryFunction> _logger;
        private readonly JsonSerializerOptions? _options;

        /// <summary>
        /// Initializes a new instance of the <see cref="QueryFunction"/> class.
        /// </summary>
        /// <param name="queryProcessor">An <see cref="IQueryProcessor"/>.</param>
        /// <param name="logger">An <see cref="ILogger{T}"/>.</param>
        /// <param name="options"><see cref="JsonSerializerOptions"/> to control the behavior during deserialization of <see cref="HttpRequestData.Body"/> and serialization of <see cref="HttpResponseData.Body"/>.</param>
        public QueryFunction(IQueryProcessor queryProcessor, ILogger<QueryFunction> logger, JsonSerializerOptions? options = null)
        {
            _queryProcessor = queryProcessor;
            _logger = logger;
            _options = options;
        }

        /// <inheritdoc />
        public async Task<HttpResponseData> HandleAsync(string queryName, HttpRequestData req, CancellationToken cancellationToken = default)
        {
            ArgumentNullException.ThrowIfNull(req);

            _logger.LogInformation("Handle {Query}", queryName);

            try
            {
                var result = req.Method == "GET"
                    ? await _queryProcessor.ProcessAsync<object>(queryName, Dictionary(req.Url), cancellationToken).ConfigureAwait(false)
                    : await _queryProcessor.ProcessAsync<object>(queryName, await req.ReadAsStringAsync().ConfigureAwait(false), _options, cancellationToken).ConfigureAwait(false);

                return await req.OkAsync(result, _options).ConfigureAwait(false);
            }
            catch (Exception exception)
            {
                var payload = req.Method == "GET" ? req.Url.ToString() : await req.ReadAsStringAsync().ConfigureAwait(false);
                _logger.LogError(exception, "Handle query failed: {Query}, {Payload}", queryName, payload);

                return exception.IsHandled()
                    ? await req.BadRequestAsync(exception, _options).ConfigureAwait(false)
                    : await req.InternalServerErrorAsync(exception, _options).ConfigureAwait(false);
            }

            Dictionary<string, IEnumerable<string>> Dictionary(Uri url)
            {
                var query = HttpUtility.ParseQueryString(url.Query);

                return query.AllKeys.ToDictionary<string?, string, IEnumerable<string>>(k => k!, k => query.GetValues(k)!);
            }
        }

        /// <inheritdoc />
        public async Task<IActionResult> HandleAsync(string queryName, HttpRequest req, CancellationToken cancellationToken = default)
        {
            ArgumentNullException.ThrowIfNull(req);

            _logger.LogInformation("Handle {Query}", queryName);

            try
            {
                var result = req.Method == "GET"
                    ? await _queryProcessor.ProcessAsync<object>(queryName, Dictionary(req.Query), cancellationToken).ConfigureAwait(false)
                    : await _queryProcessor.ProcessAsync<object>(queryName, await req.ReadAsStringAsync().ConfigureAwait(false), _options, cancellationToken).ConfigureAwait(false);

                return new OkObjectResult(result);
            }
            catch (Exception exception)
            {
                var payload = req.Method == "GET" ? req.GetDisplayUrl() : await req.ReadAsStringAsync().ConfigureAwait(false);
                _logger.LogError(exception, "Handle query failed: {Query}, {Payload}", queryName, payload);

                return exception.IsHandled()
                    ? new BadRequestObjectResult(exception.ToError())
                    : new ObjectResult(exception.ToError()) { StatusCode = StatusCodes.Status500InternalServerError };
            }

            static Dictionary<string, IEnumerable<string>> Dictionary(IQueryCollection query)
            {
                return query.ToDictionary(kv => kv.Key, kv => kv.Value as IEnumerable<string>, StringComparer.OrdinalIgnoreCase);
            }
        }
    }
}
```

## File: `src/CommandQuery.AzureFunctions/ServiceCollectionExtensions.cs`
```csharp
using System.Reflection;
using CommandQuery.DependencyInjection;
using Microsoft.Extensions.DependencyInjection;

namespace CommandQuery.AzureFunctions
{
    /// <summary>
    /// Extensions methods for <see cref="IServiceCollection"/>.
    /// </summary>
    public static class ServiceCollectionExtensions
    {
        /// <summary>
        /// Adds function and command handlers to the <see cref="IServiceCollection"/>.
        /// </summary>
        /// <param name="services">The <see cref="IServiceCollection"/>.</param>
        /// <param name="assemblies">Assemblies with command handlers.</param>
        /// <returns>The <see cref="IServiceCollection"/>.</returns>
        public static IServiceCollection AddCommandFunction(this IServiceCollection services, params Assembly[] assemblies)
        {
            services.AddSingleton<ICommandFunction, CommandFunction>();
            services.AddCommands(assemblies);

            return services;
        }

        /// <summary>
        /// Adds function and query handlers to the <see cref="IServiceCollection"/>.
        /// </summary>
        /// <param name="services">The <see cref="IServiceCollection"/>.</param>
        /// <param name="assemblies">Assemblies with query handlers.</param>
        /// <returns>The <see cref="IServiceCollection"/>.</returns>
        public static IServiceCollection AddQueryFunction(this IServiceCollection services, params Assembly[] assemblies)
        {
            services.AddSingleton<IQueryFunction, QueryFunction>();
            services.AddQueries(assemblies);

            return services;
        }
    }
}
```

## File: `src/CommandQuery.AzureFunctions/Internal/HttpRequestDataExtensions.cs`
```csharp
using System.Net;
using System.Text.Json;
using Microsoft.Azure.Functions.Worker.Http;

namespace CommandQuery.AzureFunctions
{
    internal static class HttpRequestDataExtensions
    {
        internal static async Task<HttpResponseData> OkAsync(this HttpRequestData req, object? result, JsonSerializerOptions? options)
        {
            var response = req.CreateResponse();
            response.Headers.Add("Content-Type", "application/json; charset=utf-8");
            response.StatusCode = HttpStatusCode.OK;
            await JsonSerializer.SerializeAsync(response.Body, result, options).ConfigureAwait(false);
            return response;
        }

        internal static async Task<HttpResponseData> BadRequestAsync(this HttpRequestData req, Exception exception, JsonSerializerOptions? options)
        {
            var response = req.CreateResponse();
            response.Headers.Add("Content-Type", "application/json; charset=utf-8");
            response.StatusCode = HttpStatusCode.BadRequest;
            await JsonSerializer.SerializeAsync(response.Body, exception.ToError(), options).ConfigureAwait(false);
            return response;
        }

        internal static async Task<HttpResponseData> InternalServerErrorAsync(this HttpRequestData req, Exception exception, JsonSerializerOptions? options)
        {
            var response = req.CreateResponse();
            response.Headers.Add("Content-Type", "application/json; charset=utf-8");
            response.StatusCode = HttpStatusCode.InternalServerError;
            await JsonSerializer.SerializeAsync(response.Body, exception.ToError(), options).ConfigureAwait(false);
            return response;
        }
    }
}
```

## File: `src/CommandQuery.AzureFunctions/Internal/HttpRequestExtensions.cs`
```csharp
using System.Text;
using Microsoft.AspNetCore.Http;

namespace CommandQuery.AzureFunctions
{
    internal static class HttpRequestExtensions
    {
        internal static async Task<string?> ReadAsStringAsync(this HttpRequest req, Encoding? encoding = null)
        {
            ArgumentNullException.ThrowIfNull(req);

            if (req.Body is null)
            {
                return null;
            }

            using (var reader = new StreamReader(req.Body, encoding: encoding ?? Encoding.UTF8, detectEncodingFromByteOrderMarks: true, bufferSize: 1024, leaveOpen: true))
            {
                return await reader.ReadToEndAsync().ConfigureAwait(false);
            }
        }
    }
}
```

## File: `src/CommandQuery.Client/BaseClient.cs`
```csharp
using System.Net.Http.Json;
using System.Text;
using System.Text.Json;

namespace CommandQuery.Client
{
    /// <summary>
    /// Base class for clients to CommandQuery APIs.
    /// </summary>
    public abstract class BaseClient
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="BaseClient"/> class.
        /// </summary>
        /// <param name="baseUrl">The base URL to the API.</param>
        /// <param name="timeoutInSeconds">The timeout for requests.</param>
        protected BaseClient(string baseUrl, int timeoutInSeconds = 10)
        {
            Client.BaseAddress = new Uri(baseUrl);
            Client.Timeout = TimeSpan.FromSeconds(timeoutInSeconds);
            Client.SetDefaultRequestHeaders();
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="BaseClient"/> class.
        /// </summary>
        /// <param name="baseUrl">The base URL to the API.</param>
        /// <param name="configAction">Configuration for the <see cref="HttpClient"/>.</param>
        /// <exception cref="ArgumentNullException"><paramref name="configAction"/> is <see langword="null"/>.</exception>
        protected BaseClient(string baseUrl, Action<HttpClient> configAction)
            : this(baseUrl)
        {
            if (configAction is null)
            {
                throw new ArgumentNullException(nameof(configAction));
            }

            configAction(Client);
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="BaseClient"/> class.
        /// </summary>
        /// <param name="client">A <see cref="HttpClient"/>.</param>
        /// <param name="options"><see cref="JsonSerializerOptions"/> to control the behavior during serialization and deserialization of JSON.</param>
        protected BaseClient(HttpClient client, JsonSerializerOptions? options)
        {
            Client = client;
            Client.SetDefaultRequestHeaders();
            Options = options;
        }

        /// <summary>
        /// Sends HTTP requests and receives HTTP responses.
        /// </summary>
        protected HttpClient Client { get; } = new();

        /// <summary>
        /// Options to control the behavior during serialization and deserialization of JSON.
        /// </summary>
        protected JsonSerializerOptions? Options { get; }

        /// <summary>
        /// Gets a result.
        /// </summary>
        /// <typeparam name="T">The type of result.</typeparam>
        /// <param name="value">A payload.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>A result.</returns>
        /// <exception cref="ArgumentNullException"><paramref name="value"/> is <see langword="null"/>.</exception>
        /// <exception cref="CommandQueryException">The <c>GET</c> request failed.</exception>
        protected async Task<T?> BaseGetAsync<T>(object value, CancellationToken cancellationToken)
        {
            var response = await Client.GetAsync(value.GetRequestUri(), cancellationToken).ConfigureAwait(false);
            await response.EnsureSuccessAsync(cancellationToken).ConfigureAwait(false);
            return await response.Content.ReadFromJsonAsync<T>(Options, cancellationToken).ConfigureAwait(false);
        }

        /// <summary>
        /// Post a payload.
        /// </summary>
        /// <param name="value">A payload.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>A task that represents the asynchronous operation.</returns>
        /// <exception cref="ArgumentNullException"><paramref name="value"/> is <see langword="null"/>.</exception>
        /// <exception cref="CommandQueryException">The <c>POST</c> request failed.</exception>
        protected async Task BasePostAsync(object value, CancellationToken cancellationToken)
        {
            var response = await PostAsJsonAsync(value.GetRequestSlug(), value, cancellationToken).ConfigureAwait(false);
            await response.EnsureSuccessAsync(cancellationToken).ConfigureAwait(false);
        }

        /// <summary>
        /// Post a payload and returns a result.
        /// </summary>
        /// <typeparam name="T">The type of result.</typeparam>
        /// <param name="value">A payload.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>A result.</returns>
        /// <exception cref="ArgumentNullException"><paramref name="value"/> is <see langword="null"/>.</exception>
        /// <exception cref="CommandQueryException">The <c>POST</c> request failed.</exception>
        protected async Task<T?> BasePostAsync<T>(object value, CancellationToken cancellationToken)
        {
            var response = await PostAsJsonAsync(value.GetRequestSlug(), value, cancellationToken).ConfigureAwait(false);
            await response.EnsureSuccessAsync(cancellationToken).ConfigureAwait(false);
            return await response.Content.ReadFromJsonAsync<T>(Options, cancellationToken).ConfigureAwait(false);
        }

        // Fix for Transfer-Encoding: chunked
        private async Task<HttpResponseMessage> PostAsJsonAsync(string? requestUri, object value, CancellationToken cancellationToken)
        {
            using var content = new StringContent(JsonSerializer.Serialize(value, Options), Encoding.UTF8, "application/json");
            await content.LoadIntoBufferAsync().ConfigureAwait(false);
            return await Client.PostAsync(requestUri, content, cancellationToken).ConfigureAwait(false);
        }
    }
}
```

## File: `src/CommandQuery.Client/CommandClient.cs`
```csharp
using System.Text.Json;

namespace CommandQuery.Client
{
    /// <inheritdoc cref="ICommandClient" />
    public class CommandClient : BaseClient, ICommandClient
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="CommandClient"/> class.
        /// </summary>
        /// <param name="baseUrl">The base URL to the API.</param>
        /// <param name="timeoutInSeconds">The timeout for requests.</param>
        public CommandClient(string baseUrl, int timeoutInSeconds = 10)
            : base(baseUrl, timeoutInSeconds)
        {
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="CommandClient"/> class.
        /// </summary>
        /// <param name="baseUrl">The base URL to the API.</param>
        /// <param name="configAction">Configuration for the <see cref="HttpClient"/>.</param>
        public CommandClient(string baseUrl, Action<HttpClient> configAction)
            : base(baseUrl, configAction)
        {
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="CommandClient"/> class.
        /// </summary>
        /// <param name="client">A <see cref="HttpClient"/>.</param>
        /// <param name="options"><see cref="JsonSerializerOptions"/> to control the behavior during serialization and deserialization of JSON.</param>
        public CommandClient(HttpClient client, JsonSerializerOptions? options = null)
            : base(client, options)
        {
        }

        /// <inheritdoc />
        public async Task PostAsync(ICommand command, CancellationToken cancellationToken = default) => await BasePostAsync(command, cancellationToken).ConfigureAwait(false);

        /// <inheritdoc />
        public async Task<TResult?> PostAsync<TResult>(ICommand<TResult> command, CancellationToken cancellationToken = default) => await BasePostAsync<TResult>(command, cancellationToken).ConfigureAwait(false);
    }
}
```

## File: `src/CommandQuery.Client/CommandQuery.Client.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>netstandard2.0</TargetFramework>
    <Version>4.0.0</Version>
    <PackageReleaseNotes>
- Bump System.Net.Http.Json to 8.0.0
    </PackageReleaseNotes>
    <Authors>Henrik Lau Eriksson</Authors>
    <Description>Clients for CommandQuery

✔️ CommandClient
✔️ QueryClient
📄 https://hlaueriksson.me/CommandQuery.Client/
    </Description>
    <PackageId>CommandQuery.Client</PackageId>
    <PackageProjectUrl>https://github.com/hlaueriksson/CommandQuery</PackageProjectUrl>
    <PackageIcon>icon.png</PackageIcon>
    <PackageReadmeFile>CommandQuery.Client.md</PackageReadmeFile>
    <PackageTags>CommandQuery;Command;Query;CQS;HttpClient</PackageTags>
    <PackageLicenseExpression>MIT</PackageLicenseExpression>
    <GenerateDocumentationFile>true</GenerateDocumentationFile>
  </PropertyGroup>

  <ItemGroup>
    <None Include="..\..\icon.png" Link="icon.png" Pack="true" PackagePath="\" />
    <None Include="..\..\CommandQuery.Client.md" Pack="true" PackagePath="\" />
  </ItemGroup>

  <Import Project="../../Analyzers.props" />

  <ItemGroup>
    <InternalsVisibleTo Include="CommandQuery.Tests" />
  </ItemGroup>

  <ItemGroup>
    <PackageReference Include="System.Net.Http.Json" Version="8.0.0" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\CommandQuery.Abstractions\CommandQuery.Abstractions.csproj" />
  </ItemGroup>

</Project>
```

## File: `src/CommandQuery.Client/CommandQueryException.cs`
```csharp
namespace CommandQuery.Client
{
    /// <summary>
    /// Represents errors that occur when receiving HTTP responses in the <see cref="CommandClient"/> and <see cref="QueryClient"/>.
    /// </summary>
    public class CommandQueryException : Exception
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="CommandQueryException"/> class.
        /// </summary>
        public CommandQueryException()
        {
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="CommandQueryException"/> class.
        /// </summary>
        /// <param name="message">The message that describes the error.</param>
        public CommandQueryException(string message)
            : base(message)
        {
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="CommandQueryException"/> class.
        /// </summary>
        /// <param name="message">The error message that explains the reason for the exception.</param>
        /// <param name="innerException">The exception that is the cause of the current exception, or a null reference if no inner exception is specified.</param>
        public CommandQueryException(string message, Exception innerException)
            : base(message, innerException)
        {
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="CommandQueryException"/> class with a specified error message and <see cref="IError"/>.
        /// </summary>
        /// <param name="message">The message that describes the error.</param>
        /// <param name="error">The error that occurred during the processing of a command or query.</param>
        public CommandQueryException(string message, IError? error)
            : base(message)
        {
            Error = error;
        }

        /// <summary>
        /// Represents an error that occurred during the processing of a command or query.
        /// </summary>
        public IError? Error { get; set; }
    }
}
```

## File: `src/CommandQuery.Client/ICommandClient.cs`
```csharp
namespace CommandQuery.Client
{
    /// <summary>
    /// Client for sending commands to CommandQuery APIs over <c>HTTP</c>.
    /// </summary>
    public interface ICommandClient
    {
        /// <summary>
        /// Sends an <see cref="ICommand"/> to the API with <c>POST</c>.
        /// </summary>
        /// <param name="command">The command.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>A task that represents the asynchronous operation.</returns>
        /// <exception cref="ArgumentNullException"><paramref name="command"/> is <see langword="null"/>.</exception>
        /// <exception cref="CommandQueryException">The <see cref="ICommand"/> failed.</exception>
        Task PostAsync(ICommand command, CancellationToken cancellationToken = default);

        /// <summary>
        /// Sends an <see cref="ICommand{TResult}"/> to the API with <c>POST</c>.
        /// </summary>
        /// <typeparam name="TResult">The type of result.</typeparam>
        /// <param name="command">The command.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>A result.</returns>
        /// <exception cref="ArgumentNullException"><paramref name="command"/> is <see langword="null"/>.</exception>
        /// <exception cref="CommandQueryException">The <see cref="ICommand{TResult}"/> failed.</exception>
        Task<TResult?> PostAsync<TResult>(ICommand<TResult> command, CancellationToken cancellationToken = default);
    }
}
```

## File: `src/CommandQuery.Client/IQueryClient.cs`
```csharp
namespace CommandQuery.Client
{
    /// <summary>
    /// Client for sending queries to CommandQuery APIs over <c>HTTP</c>.
    /// </summary>
    public interface IQueryClient
    {
        /// <summary>
        /// Sends an <see cref="IQuery{TResult}"/> to the API with <c>GET</c>.
        /// </summary>
        /// <typeparam name="TResult">The type of result.</typeparam>
        /// <param name="query">The query.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>A result.</returns>
        /// <exception cref="ArgumentNullException"><paramref name="query"/> is <see langword="null"/>.</exception>
        /// <exception cref="CommandQueryException">The <see cref="IQuery{TResult}"/> failed.</exception>
        Task<TResult?> GetAsync<TResult>(IQuery<TResult> query, CancellationToken cancellationToken = default);

        /// <summary>
        /// Sends an <see cref="IQuery{TResult}"/> to the API with <c>POST</c>.
        /// </summary>
        /// <typeparam name="TResult">The type of result.</typeparam>
        /// <param name="query">The query.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>A result.</returns>
        /// <exception cref="ArgumentNullException"><paramref name="query"/> is <see langword="null"/>.</exception>
        /// <exception cref="CommandQueryException">The <see cref="IQuery{TResult}"/> failed.</exception>
        Task<TResult?> PostAsync<TResult>(IQuery<TResult> query, CancellationToken cancellationToken = default);
    }
}
```

## File: `src/CommandQuery.Client/QueryClient.cs`
```csharp
using System.Text.Json;

namespace CommandQuery.Client
{
    /// <inheritdoc cref="IQueryClient" />
    public class QueryClient : BaseClient, IQueryClient
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="QueryClient"/> class.
        /// </summary>
        /// <param name="baseUrl">The base URL to the API.</param>
        /// <param name="timeoutInSeconds">The timeout for requests.</param>
        public QueryClient(string baseUrl, int timeoutInSeconds = 10)
            : base(baseUrl, timeoutInSeconds)
        {
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="QueryClient"/> class.
        /// </summary>
        /// <param name="baseUrl">The base URL to the API.</param>
        /// <param name="configAction">Configuration for the <see cref="HttpClient"/>.</param>
        public QueryClient(string baseUrl, Action<HttpClient> configAction)
            : base(baseUrl, configAction)
        {
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="QueryClient"/> class.
        /// </summary>
        /// <param name="client">A <see cref="HttpClient"/>.</param>
        /// <param name="options"><see cref="JsonSerializerOptions"/> to control the behavior during serialization and deserialization of JSON.</param>
        public QueryClient(HttpClient client, JsonSerializerOptions? options = null)
            : base(client, options)
        {
        }

        /// <inheritdoc />
        public async Task<TResult?> GetAsync<TResult>(IQuery<TResult> query, CancellationToken cancellationToken = default) => await BaseGetAsync<TResult>(query, cancellationToken).ConfigureAwait(false);

        /// <inheritdoc />
        public async Task<TResult?> PostAsync<TResult>(IQuery<TResult> query, CancellationToken cancellationToken = default) => await BasePostAsync<TResult>(query, cancellationToken).ConfigureAwait(false);
    }
}
```

## File: `src/CommandQuery.Client/Internal/DictionaryStringObjectConverter.cs`
```csharp
using System.Text.Json;
using System.Text.Json.Serialization;

namespace CommandQuery.Client
{
    // https://github.com/joseftw/JOS.SystemTextJsonDictionaryStringObjectJsonConverter/blob/develop/src/JOS.SystemTextJsonDictionaryObjectModelBinder/DictionaryStringObjectJsonConverterCustomWrite.cs
    internal sealed class DictionaryStringObjectConverter : JsonConverter<Dictionary<string, object>>
    {
        public override Dictionary<string, object> Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
        {
            var dictionary = new Dictionary<string, object>();
            while (reader.Read())
            {
                if (reader.TokenType == JsonTokenType.EndObject)
                {
                    return dictionary;
                }

                var propertyName = reader.GetString();

                reader.Read();

                dictionary.Add(propertyName!, ReadValue(ref reader, options)!);
            }

            return dictionary;
        }

        public override void Write(Utf8JsonWriter writer, Dictionary<string, object> value, JsonSerializerOptions options)
        {
            writer.WriteStartObject();

            foreach (var key in value.Keys)
            {
                WriteValue(writer, key, value[key]);
            }

            writer.WriteEndObject();
        }

        private static void WriteValue(Utf8JsonWriter writer, string? key, object objectValue)
        {
            if (key != null)
            {
                writer.WritePropertyName(key);
            }

            switch (objectValue)
            {
                case Dictionary<string, object> dict:
                    writer.WriteStartObject();
                    foreach (var item in dict)
                    {
                        WriteValue(writer, item.Key, item.Value);
                    }

                    writer.WriteEndObject();
                    break;
                default:
                    JsonSerializer.Serialize(writer, objectValue);
                    break;
            }
        }

        private object? ReadValue(ref Utf8JsonReader reader, JsonSerializerOptions options)
        {
            switch (reader.TokenType)
            {
                case JsonTokenType.String:
                    if (reader.TryGetDateTime(out var dateTime))
                    {
                        return dateTime;
                    }

                    if (reader.TryGetGuid(out var guid))
                    {
                        return guid;
                    }

                    return reader.GetString();
                case JsonTokenType.False:
                    return false;
                case JsonTokenType.True:
                    return true;
                case JsonTokenType.Null:
                    return null;
                case JsonTokenType.Number:
                    if (reader.TryGetInt64(out var result))
                    {
                        return result;
                    }

                    return reader.GetDecimal();
                case JsonTokenType.StartObject:
                    return Read(ref reader, null!, options);
                case JsonTokenType.StartArray:
                    var list = new List<object>();
                    while (reader.Read() && reader.TokenType != JsonTokenType.EndArray)
                    {
                        list.Add(ReadValue(ref reader, options)!);
                    }

                    return list;
                default:
                    throw new JsonException($"'{reader.TokenType}' is not supported");
            }
        }
    }
}
```

## File: `src/CommandQuery.Client/Internal/Error.cs`
```csharp
namespace CommandQuery.Client
{
    internal class Error : IError
    {
        public string? Message { get; set; }

        public Dictionary<string, object>? Details { get; set; }
    }
}
```

## File: `src/CommandQuery.Client/Internal/HttpClientExtensions.cs`
```csharp
using System.Net.Http.Headers;
using System.Reflection;

namespace CommandQuery.Client
{
    internal static class HttpClientExtensions
    {
        internal static void SetDefaultRequestHeaders(this HttpClient client)
        {
            if (client is null)
            {
                throw new ArgumentNullException(nameof(client));
            }

            client.DefaultRequestHeaders.Accept.Clear();
            client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
            client.DefaultRequestHeaders.Add("User-Agent", $"CommandQuery.Client/{Assembly.GetExecutingAssembly().GetName().Version}");
        }
    }
}
```

## File: `src/CommandQuery.Client/Internal/HttpResponseMessageExtensions.cs`
```csharp
using System.Net.Http.Json;
using System.Text.Json;

namespace CommandQuery.Client
{
    internal static class HttpResponseMessageExtensions
    {
        private static readonly JsonSerializerOptions _options = GetJsonSerializerOptions();

        internal static async Task<HttpResponseMessage> EnsureSuccessAsync(this HttpResponseMessage message, CancellationToken cancellationToken)
        {
            if (message.IsSuccessStatusCode)
            {
                return message;
            }

            var error = await message.Content.ReadFromJsonAsync<Error>(_options, cancellationToken).ConfigureAwait(false);

            throw new CommandQueryException(message.ToString(), error);
        }

        private static JsonSerializerOptions GetJsonSerializerOptions()
        {
            var result = new JsonSerializerOptions();
            result.Converters.Add(new DictionaryStringObjectConverter());

            return result;
        }
    }
}
```

## File: `src/CommandQuery.Client/Internal/QueryExtensions.cs`
```csharp
using System.Collections;
using System.Globalization;
using System.Net;
using System.Reflection;

namespace CommandQuery.Client
{
    internal static class QueryExtensions
    {
        private static readonly Assembly _system = typeof(object).Assembly;

        internal static string GetRequestUri(this object query)
        {
            if (query is null)
            {
                throw new ArgumentNullException(nameof(query));
            }

            return query.GetType().Name + "?" + query.QueryString();
        }

        internal static string GetRequestSlug(this object query)
        {
            if (query is null)
            {
                throw new ArgumentNullException(nameof(query));
            }

            return query.GetType().Name;
        }

        private static string QueryString(this object query)
        {
            var result = new List<string>();

            Parameters(query, string.Empty);

            return string.Join("&", [.. result]);

            void Parameters(object root, string prefix)
            {
                foreach (var p in root.GetType().GetProperties().Where(p => p.GetValue(root, null) != null))
                {
                    var value = p.GetValue(root, null);

                    if (value.GetType().Assembly != _system)
                    {
                        Parameters(value, prefix + p.Name + ".");
                    }
                    else if (value is IEnumerable enumerable and not string)
                    {
                        result.AddRange(from object v in enumerable select Parameter(p, v, prefix));
                    }
                    else
                    {
                        result.Add(Parameter(p, value, prefix));
                    }
                }
            }

            static string Parameter(PropertyInfo property, object value, string prefix)
            {
                return value switch
                {
                    DateTime dateTime => NameValuePair(dateTime.ToString("O")),
                    DateTimeOffset dateTimeOffset => NameValuePair(dateTimeOffset.ToString("O")),
                    _ => NameValuePair(Convert.ToString(value, CultureInfo.InvariantCulture)!),
                };

                string NameValuePair(string value)
                {
                    return $"{prefix}{property.Name}={WebUtility.UrlEncode(value)}";
                }
            }
        }
    }
}
```

## File: `src/CommandQuery.GoogleCloudFunctions/CommandFunction.cs`
```csharp
using System.Text.Json;
using CommandQuery.SystemTextJson;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;

namespace CommandQuery.GoogleCloudFunctions
{
    /// <inheritdoc />
    public class CommandFunction : ICommandFunction
    {
        private readonly ICommandProcessor _commandProcessor;
        private readonly ILogger<CommandFunction> _logger;
        private readonly JsonSerializerOptions? _options;

        /// <summary>
        /// Initializes a new instance of the <see cref="CommandFunction"/> class.
        /// </summary>
        /// <param name="commandProcessor">An <see cref="ICommandProcessor"/>.</param>
        /// <param name="logger">An <see cref="ILogger{T}"/>.</param>
        /// <param name="options"><see cref="JsonSerializerOptions"/> to control the behavior during deserialization of <see cref="HttpRequest.Body"/> and serialization of <see cref="HttpResponse.Body"/>.</param>
        public CommandFunction(ICommandProcessor commandProcessor, ILogger<CommandFunction> logger, JsonSerializerOptions? options = null)
        {
            _commandProcessor = commandProcessor;
            _logger = logger;
            _options = options;
        }

        /// <inheritdoc />
        public async Task HandleAsync(string commandName, HttpContext context, CancellationToken cancellationToken = default)
        {
            _logger.LogInformation("Handle {Command}", commandName);

            if (context is null)
            {
                throw new ArgumentNullException(nameof(context));
            }

            try
            {
                var result = await _commandProcessor.ProcessAsync(commandName, await context.Request.ReadAsStringAsync().ConfigureAwait(false), _options, cancellationToken).ConfigureAwait(false);

                context.Response.StatusCode = StatusCodes.Status200OK;

                if (result == CommandResult.None)
                {
                    return;
                }

                await context.Response.OkAsync(result.Value, _options, cancellationToken).ConfigureAwait(false);
            }
            catch (Exception exception)
            {
                var payload = await context.Request.ReadAsStringAsync().ConfigureAwait(false);
                _logger.LogError(exception, "Handle command failed: {Command}, {Payload}", commandName, payload);

                if (exception.IsHandled())
                {
                    await context.Response.BadRequestAsync(exception, _options, cancellationToken).ConfigureAwait(false);
                    return;
                }

                await context.Response.InternalServerErrorAsync(exception, _options, cancellationToken).ConfigureAwait(false);
            }
        }
    }
}
```

## File: `src/CommandQuery.GoogleCloudFunctions/CommandQuery.GoogleCloudFunctions.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>netstandard2.0</TargetFramework>
    <Version>4.0.0</Version>
    <PackageReleaseNotes>
- Change Microsoft.AspNetCore.Http to 2.1.34
- Bump to Microsoft.Extensions.Logging.Abstractions 6.0.4
- Remove ILogger parameter from HandleAsync
    </PackageReleaseNotes>
    <Authors>Henrik Lau Eriksson</Authors>
    <Description>Command Query Separation for Google Cloud Functions ⚡

✔️ Provides generic function support for commands and queries with HTTP functions
✔️ Enables APIs based on HTTP POST and GET
📄 https://hlaueriksson.me/CommandQuery.GoogleCloudFunctions/
    </Description>
    <PackageId>CommandQuery.GoogleCloudFunctions</PackageId>
    <PackageProjectUrl>https://github.com/hlaueriksson/CommandQuery</PackageProjectUrl>
    <PackageIcon>icon.png</PackageIcon>
    <PackageReadmeFile>CommandQuery.GoogleCloudFunctions.md</PackageReadmeFile>
    <PackageTags>CommandQuery;Command;Query;CQS;google;cloud;functions</PackageTags>
    <PackageLicenseExpression>MIT</PackageLicenseExpression>
    <GenerateDocumentationFile>true</GenerateDocumentationFile>
  </PropertyGroup>

  <ItemGroup>
    <None Include="..\..\icon.png" Link="icon.png" Pack="true" PackagePath="\" />
    <None Include="..\..\CommandQuery.GoogleCloudFunctions.md" Pack="true" PackagePath="\" />
  </ItemGroup>

  <Import Project="../../Analyzers.props" />

  <ItemGroup>
    <InternalsVisibleTo Include="CommandQuery.GoogleCloudFunctions.Tests" />
  </ItemGroup>

  <ItemGroup>
    <PackageReference Include="Microsoft.AspNetCore.Http" Version="2.1.34" />
    <PackageReference Include="Microsoft.Extensions.Logging.Abstractions" Version="6.0.4" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\CommandQuery.SystemTextJson\CommandQuery.SystemTextJson.csproj" />
    <ProjectReference Include="..\CommandQuery\CommandQuery.csproj" />
  </ItemGroup>

</Project>
```

## File: `src/CommandQuery.GoogleCloudFunctions/ICommandFunction.cs`
```csharp
using Microsoft.AspNetCore.Http;

namespace CommandQuery.GoogleCloudFunctions
{
    /// <summary>
    /// Handles commands for the Google Cloud function.
    /// </summary>
    public interface ICommandFunction
    {
        /// <summary>
        /// Handle a command.
        /// </summary>
        /// <param name="commandName">The name of the command.</param>
        /// <param name="context">A <see cref="HttpContext"/>.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>A task that represents the asynchronous operation.</returns>
        /// <exception cref="ArgumentNullException"><paramref name="context"/> is <see langword="null"/>.</exception>
        Task HandleAsync(string commandName, HttpContext context, CancellationToken cancellationToken = default);
    }
}
```

## File: `src/CommandQuery.GoogleCloudFunctions/IQueryFunction.cs`
```csharp
using Microsoft.AspNetCore.Http;

namespace CommandQuery.GoogleCloudFunctions
{
    /// <summary>
    /// Handles queries for the Google Cloud function.
    /// </summary>
    public interface IQueryFunction
    {
        /// <summary>
        /// Handle a query.
        /// </summary>
        /// <param name="queryName">The name of the query.</param>
        /// <param name="context">A <see cref="HttpContext"/>.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>A task that represents the asynchronous operation.</returns>
        /// <exception cref="ArgumentNullException"><paramref name="context"/> is <see langword="null"/>.</exception>
        Task HandleAsync(string queryName, HttpContext context, CancellationToken cancellationToken = default);
    }
}
```

## File: `src/CommandQuery.GoogleCloudFunctions/QueryFunction.cs`
```csharp
using System.Text.Json;
using CommandQuery.SystemTextJson;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;

namespace CommandQuery.GoogleCloudFunctions
{
    /// <inheritdoc />
    public class QueryFunction : IQueryFunction
    {
        private readonly IQueryProcessor _queryProcessor;
        private readonly ILogger<QueryFunction> _logger;
        private readonly JsonSerializerOptions? _options;

        /// <summary>
        /// Initializes a new instance of the <see cref="QueryFunction"/> class.
        /// </summary>
        /// <param name="queryProcessor">An <see cref="IQueryProcessor"/>.</param>
        /// <param name="logger">An <see cref="ILogger{T}"/>.</param>
        /// <param name="options"><see cref="JsonSerializerOptions"/> to control the behavior during deserialization of <see cref="HttpRequest.Body"/> and serialization of <see cref="HttpResponse.Body"/>.</param>
        public QueryFunction(IQueryProcessor queryProcessor, ILogger<QueryFunction> logger, JsonSerializerOptions? options = null)
        {
            _queryProcessor = queryProcessor;
            _logger = logger;
            _options = options;
        }

        /// <inheritdoc />
        public async Task HandleAsync(string queryName, HttpContext context, CancellationToken cancellationToken = default)
        {
            _logger.LogInformation("Handle {Query}", queryName);

            if (context is null)
            {
                throw new ArgumentNullException(nameof(context));
            }

            try
            {
                var result = context.Request.Method == "GET"
                    ? await _queryProcessor.ProcessAsync<object>(queryName, Dictionary(context.Request.Query), cancellationToken).ConfigureAwait(false)
                    : await _queryProcessor.ProcessAsync<object>(queryName, await context.Request.ReadAsStringAsync().ConfigureAwait(false), _options, cancellationToken).ConfigureAwait(false);

                await context.Response.OkAsync(result, _options, cancellationToken).ConfigureAwait(false);
            }
            catch (Exception exception)
            {
                var payload = context.Request.Method == "GET" ? context.Request.QueryString.Value : await context.Request.ReadAsStringAsync().ConfigureAwait(false);
                _logger.LogError(exception, "Handle query failed: {Query}, {Payload}", queryName, payload);

                if (exception.IsHandled())
                {
                    await context.Response.BadRequestAsync(exception, _options, cancellationToken).ConfigureAwait(false);
                    return;
                }

                await context.Response.InternalServerErrorAsync(exception, _options, cancellationToken).ConfigureAwait(false);
            }

            static Dictionary<string, IEnumerable<string>> Dictionary(IQueryCollection query)
            {
                return query.ToDictionary(kv => kv.Key, kv => kv.Value as IEnumerable<string>, StringComparer.OrdinalIgnoreCase);
            }
        }
    }
}
```

## File: `src/CommandQuery.GoogleCloudFunctions/ServiceCollectionExtensions.cs`
```csharp
using System.Reflection;
using CommandQuery.DependencyInjection;
using Microsoft.Extensions.DependencyInjection;

namespace CommandQuery.GoogleCloudFunctions
{
    /// <summary>
    /// Extensions methods for <see cref="IServiceCollection"/>.
    /// </summary>
    public static class ServiceCollectionExtensions
    {
        /// <summary>
        /// Adds function and command handlers to the <see cref="IServiceCollection"/>.
        /// </summary>
        /// <param name="services">The <see cref="IServiceCollection"/>.</param>
        /// <param name="assemblies">Assemblies with command handlers.</param>
        /// <returns>The <see cref="IServiceCollection"/>.</returns>
        public static IServiceCollection AddCommandFunction(this IServiceCollection services, params Assembly[] assemblies)
        {
            services.AddSingleton<ICommandFunction, CommandFunction>();
            services.AddCommands(assemblies);

            return services;
        }

        /// <summary>
        /// Adds function and query handlers to the <see cref="IServiceCollection"/>.
        /// </summary>
        /// <param name="services">The <see cref="IServiceCollection"/>.</param>
        /// <param name="assemblies">Assemblies with query handlers.</param>
        /// <returns>The <see cref="IServiceCollection"/>.</returns>
        public static IServiceCollection AddQueryFunction(this IServiceCollection services, params Assembly[] assemblies)
        {
            services.AddSingleton<IQueryFunction, QueryFunction>();
            services.AddQueries(assemblies);

            return services;
        }
    }
}
```

## File: `src/CommandQuery.GoogleCloudFunctions/Internal/HttpExtensions.cs`
```csharp
using System.Text;
using System.Text.Json;
using Microsoft.AspNetCore.Http;

namespace CommandQuery.GoogleCloudFunctions
{
    internal static class HttpExtensions
    {
        internal static async Task<string?> ReadAsStringAsync(this HttpRequest req, Encoding? encoding = null)
        {
            if (req is null)
            {
                throw new ArgumentNullException(nameof(req));
            }

            if (req.Body is null)
            {
                return null;
            }

            using (var reader = new StreamReader(req.Body, encoding: encoding ?? Encoding.UTF8, detectEncodingFromByteOrderMarks: true, bufferSize: 1024, leaveOpen: true))
            {
                return await reader.ReadToEndAsync().ConfigureAwait(false);
            }
        }

        internal static async Task OkAsync(this HttpResponse response, object? result, JsonSerializerOptions? options, CancellationToken cancellationToken)
        {
            response.ContentType = "application/json; charset=utf-8";
            response.StatusCode = StatusCodes.Status200OK;
            await JsonSerializer.SerializeAsync(response.Body, result, options, cancellationToken).ConfigureAwait(false);
        }

        internal static async Task BadRequestAsync(this HttpResponse response, Exception exception, JsonSerializerOptions? options, CancellationToken cancellationToken)
        {
            response.ContentType = "application/json; charset=utf-8";
            response.StatusCode = StatusCodes.Status400BadRequest;
            await JsonSerializer.SerializeAsync(response.Body, exception.ToError(), options, cancellationToken).ConfigureAwait(false);
        }

        internal static async Task InternalServerErrorAsync(this HttpResponse response, Exception exception, JsonSerializerOptions? options, CancellationToken cancellationToken)
        {
            response.ContentType = "application/json; charset=utf-8";
            response.StatusCode = StatusCodes.Status500InternalServerError;
            await JsonSerializer.SerializeAsync(response.Body, exception.ToError(), options, cancellationToken).ConfigureAwait(false);
        }
    }
}
```

## File: `src/CommandQuery.SystemTextJson/CommandProcessorExtensions.cs`
```csharp
using System.Text.Json;
using CommandQuery.Exceptions;

namespace CommandQuery.SystemTextJson
{
    /// <summary>
    /// Extensions methods for <see cref="ICommandProcessor"/>.
    /// </summary>
    public static class CommandProcessorExtensions
    {
        /// <summary>
        /// Process a command with or without result.
        /// </summary>
        /// <param name="commandProcessor">The command processor.</param>
        /// <param name="commandName">The name of the command.</param>
        /// <param name="json">The JSON representation of the command.</param>
        /// <param name="options"><see cref="JsonSerializerOptions"/> to control the behavior during deserialization of <paramref name="json"/>.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>The result of the command wrapped in a <see cref="CommandResult"/>, or <see cref="CommandResult.None"/>.</returns>
        /// <exception cref="ArgumentNullException"><paramref name="commandProcessor"/> is <see langword="null"/>.</exception>
        /// <exception cref="CommandProcessorException">The process of the command failed.</exception>
        public static async Task<CommandResult> ProcessAsync(this ICommandProcessor commandProcessor, string commandName, string? json, JsonSerializerOptions? options = null, CancellationToken cancellationToken = default)
        {
            if (commandProcessor is null)
            {
                throw new ArgumentNullException(nameof(commandProcessor));
            }

            if (json is null)
            {
                throw new ArgumentNullException(nameof(json));
            }

            var commandType = commandProcessor.GetCommandType(commandName);

            if (commandType is null)
            {
                throw new CommandProcessorException($"The command type '{commandName}' could not be found");
            }

            var command = json.SafeDeserialize(commandType, options);

            switch (command)
            {
                case null:
                    throw new CommandProcessorException("The json string could not be deserialized to an object");
                case ICommand commandWithoutResult:
                    await commandProcessor.ProcessAsync(commandWithoutResult, cancellationToken).ConfigureAwait(false);
                    return CommandResult.None;
                default:
                    var commandWithResult = (dynamic)command;
                    var result = await commandProcessor.ProcessAsync(commandWithResult, cancellationToken).ConfigureAwait(false);
                    return new CommandResult(result);
            }
        }
    }
}
```

## File: `src/CommandQuery.SystemTextJson/CommandQuery.SystemTextJson.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>netstandard2.0</TargetFramework>
    <Version>4.0.0</Version>
    <PackageReleaseNotes>
- Bump System.Text.Json to 8.0.4
- Deserialize JSON with sane defaults
    </PackageReleaseNotes>
    <Authors>Henrik Lau Eriksson</Authors>
    <Description>System.Text.Json extensions for CommandQuery</Description>
    <PackageId>CommandQuery.SystemTextJson</PackageId>
    <PackageProjectUrl>https://github.com/hlaueriksson/CommandQuery</PackageProjectUrl>
    <PackageIcon>icon.png</PackageIcon>
    <PackageTags>CommandQuery;Command;Query;CQS;json</PackageTags>
    <PackageLicenseExpression>MIT</PackageLicenseExpression>
    <GenerateDocumentationFile>true</GenerateDocumentationFile>
  </PropertyGroup>

  <ItemGroup>
    <None Include="..\..\icon.png" Link="icon.png" Pack="true" PackagePath="\" />
  </ItemGroup>

  <Import Project="../../Analyzers.props" />

  <ItemGroup>
    <InternalsVisibleTo Include="CommandQuery.Benchmark" />
    <InternalsVisibleTo Include="CommandQuery.Tests" />
  </ItemGroup>

  <ItemGroup>
    <PackageReference Include="System.Text.Json" Version="8.0.4" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\CommandQuery\CommandQuery.csproj" />
  </ItemGroup>

</Project>
```

## File: `src/CommandQuery.SystemTextJson/CommandResult.cs`
```csharp
namespace CommandQuery.SystemTextJson
{
    /// <summary>
    /// Wraps a command result.
    /// </summary>
    public class CommandResult
    {
        /// <summary>
        /// Represents the result of an <see cref="ICommand"/>.
        /// </summary>
        public static readonly CommandResult None = new();

        /// <summary>
        /// Initializes a new instance of the <see cref="CommandResult"/> class that wraps a command result.
        /// </summary>
        /// <param name="value">The result of an <see cref="ICommand{TResult}"/>.</param>
        public CommandResult(object value)
        {
            Value = value;
        }

        private CommandResult()
        {
        }

        /// <summary>
        /// The result of an <see cref="ICommand{TResult}"/>.
        /// </summary>
        public object? Value { get; }
    }
}
```

## File: `src/CommandQuery.SystemTextJson/QueryProcessorExtensions.cs`
```csharp
using System.Text.Json;
using CommandQuery.Exceptions;

namespace CommandQuery.SystemTextJson
{
    /// <summary>
    /// Extensions methods for <see cref="IQueryProcessor"/>.
    /// </summary>
    public static class QueryProcessorExtensions
    {
        /// <summary>
        /// Process a query.
        /// </summary>
        /// <typeparam name="TResult">The type of result.</typeparam>
        /// <param name="queryProcessor">The query processor.</param>
        /// <param name="queryName">The name of the query.</param>
        /// <param name="json">The JSON representation of the query.</param>
        /// <param name="options"><see cref="JsonSerializerOptions"/> to control the behavior during deserialization of <paramref name="json"/>.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>The result of the query.</returns>
        /// <exception cref="ArgumentNullException"><paramref name="queryProcessor"/> is <see langword="null"/>.</exception>
        /// <exception cref="QueryProcessorException">The process of the query failed.</exception>
        public static async Task<TResult> ProcessAsync<TResult>(this IQueryProcessor queryProcessor, string queryName, string? json, JsonSerializerOptions? options = null, CancellationToken cancellationToken = default)
        {
            if (queryProcessor is null)
            {
                throw new ArgumentNullException(nameof(queryProcessor));
            }

            if (json is null)
            {
                throw new ArgumentNullException(nameof(json));
            }

            var queryType = queryProcessor.GetQueryType(queryName);

            if (queryType is null)
            {
                throw new QueryProcessorException($"The query type '{queryName}' could not be found");
            }

            var query = json.SafeDeserialize(queryType, options);

            if (query is null)
            {
                throw new QueryProcessorException("The json string could not be deserialized to an object");
            }

            return await queryProcessor.ProcessAsync((dynamic)query, cancellationToken);
        }

        /// <summary>
        /// Process a query.
        /// </summary>
        /// <typeparam name="TResult">The type of result.</typeparam>
        /// <param name="queryProcessor">The query processor.</param>
        /// <param name="queryName">The name of the query.</param>
        /// <param name="dictionary">The key/value representation of the query.</param>
        /// <param name="cancellationToken">A cancellation token that can be used by other objects or threads to receive notice of cancellation.</param>
        /// <returns>The result of the query.</returns>
        /// <exception cref="ArgumentNullException"><paramref name="queryProcessor"/> is <see langword="null"/>.</exception>
        /// <exception cref="QueryProcessorException">The process of the query failed.</exception>
        public static async Task<TResult> ProcessAsync<TResult>(this IQueryProcessor queryProcessor, string queryName, IDictionary<string, IEnumerable<string>> dictionary, CancellationToken cancellationToken = default)
        {
            if (queryProcessor is null)
            {
                throw new ArgumentNullException(nameof(queryProcessor));
            }

            var queryType = queryProcessor.GetQueryType(queryName);

            if (queryType is null)
            {
                throw new QueryProcessorException($"The query type '{queryName}' could not be found");
            }

            var query = dictionary.GetQueryDictionary(queryType).SafeDeserialize(queryType);

            if (query is null)
            {
                throw new QueryProcessorException("The dictionary could not be deserialized to an object");
            }

            return await queryProcessor.ProcessAsync((dynamic)query, cancellationToken);
        }
    }
}
```

## File: `src/CommandQuery.SystemTextJson/Internal/BooleanConverter.cs`
```csharp
using System.Text.Json;
using System.Text.Json.Serialization;

namespace CommandQuery.SystemTextJson
{
    internal sealed class BooleanConverter : JsonConverter<bool>
    {
        public override bool Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
        {
            switch (reader.TokenType)
            {
                case JsonTokenType.String:
                    var stringValue = reader.GetString();
                    if (bool.TryParse(stringValue, out bool value))
                    {
                        return value;
                    }

                    break;
                case JsonTokenType.True:
                    return true;
                case JsonTokenType.False:
                    return false;
            }

            throw new JsonException();
        }

        public override void Write(Utf8JsonWriter writer, bool value, JsonSerializerOptions options)
        {
            writer.WriteBooleanValue(value);
        }
    }
}
```

## File: `src/CommandQuery.SystemTextJson/Internal/JsonExtensions.cs`
```csharp
using System.Text.Json;
using System.Text.Json.Serialization;

namespace CommandQuery.SystemTextJson
{
    internal static class JsonExtensions
    {
        private static readonly JsonSerializerOptions _options = GetJsonSerializerOptions();

        internal static object? SafeDeserialize(this string json, Type type, JsonSerializerOptions? options = null)
        {
            try
            {
                return JsonSerializer.Deserialize(json, type, options ?? _options);
            }
            catch
            {
                return null;
            }
        }

        internal static object? SafeDeserialize(this IDictionary<string, object>? dictionary, Type type)
        {
            if (dictionary is null)
            {
                return null;
            }

            try
            {
                return JsonSerializer.Deserialize(JsonSerializer.Serialize(dictionary), type, _options);
            }
            catch
            {
                return null;
            }
        }

        private static JsonSerializerOptions GetJsonSerializerOptions()
        {
            var result = new JsonSerializerOptions
            {
                PropertyNameCaseInsensitive = true,
                NumberHandling = JsonNumberHandling.AllowReadingFromString,
            };
            result.Converters.Add(new JsonStringEnumConverter());
            result.Converters.Add(new BooleanConverter());

            return result;
        }
    }
}
```

## File: `tests/CommandQuery.AWSLambda.Tests/CommandFunctionTests.cs`
```csharp
using System.Text.Json;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using CommandQuery.Exceptions;
using CommandQuery.Tests;
using FluentAssertions;

namespace CommandQuery.AWSLambda.Tests
{
    public class CommandFunctionTests_APIGatewayProxyRequest : LoFuTest<CommandFunction>
    {
        [SetUp]
        public void SetUp()
        {
            Clear();
            Use<JsonSerializerOptions>(null);
            Logger = One<ILambdaLogger>();
            Request = new APIGatewayProxyRequest { Body = "{}" };
        }

        [LoFu, Test]
        public async Task when_handling_the_command()
        {
            CommandName = "FakeCommand";
            Use<Mock<ICommandProcessor>>().Setup(x => x.GetCommandType(CommandName)).Returns(typeof(FakeCommand));

            async Task should_invoke_the_command_processor()
            {
                var result = await Subject.HandleAsync(CommandName, Request, Logger);

                result.StatusCode.Should().Be(200);
                result.Body.Should().BeNull();
            }

            async Task should_throw_when_request_is_null()
            {
                Func<Task> act = () => Subject.HandleAsync(CommandName, (APIGatewayProxyRequest)null, Logger);
                await act.Should().ThrowAsync<ArgumentNullException>();
            }

            async Task should_handle_CommandProcessorException()
            {
                The<Mock<ICommandProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeCommand>(), It.IsAny<CancellationToken>())).Throws(new CommandProcessorException("fail"));

                var result = await Subject.HandleAsync(CommandName, Request, Logger);

                result.ShouldBeError("fail", 400);
            }

            async Task should_handle_CommandException()
            {
                The<Mock<ICommandProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeCommand>(), It.IsAny<CancellationToken>())).Throws(new CommandException("invalid"));

                var result = await Subject.HandleAsync(CommandName, Request, Logger);

                result.ShouldBeError("invalid", 400);
            }

            async Task should_handle_Exception()
            {
                The<Mock<ICommandProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeCommand>(), It.IsAny<CancellationToken>())).Throws(new Exception("fail"));

                var result = await Subject.HandleAsync(CommandName, Request, Logger);

                result.ShouldBeError("fail", 500);
            }
        }

        [LoFu, Test]
        public async Task when_handling_the_command_with_result()
        {
            CommandName = "FakeResultCommand";
            Use<Mock<ICommandProcessor>>().Setup(x => x.GetCommandType(CommandName)).Returns(typeof(FakeResultCommand));

            async Task should_return_the_result_from_the_command_processor()
            {
                var expected = new FakeResult();
                The<Mock<ICommandProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeResultCommand>(), It.IsAny<CancellationToken>())).Returns(Task.FromResult(expected));

                var result = await Subject.HandleAsync(CommandName, Request, Logger);

                result.StatusCode.Should().Be(200);
                result.Body.Should().NotBeNull();
            }
        }

        APIGatewayProxyRequest Request;
        ILambdaLogger Logger;
        string CommandName;
    }

    public class CommandFunctionTests_APIGatewayHttpApiV2ProxyRequest : LoFuTest<CommandFunction>
    {
        [SetUp]
        public void SetUp()
        {
            Clear();
            Use<JsonSerializerOptions>(null);
            Logger = One<ILambdaLogger>();
            Request = new APIGatewayHttpApiV2ProxyRequest { Body = "{}" };
        }

        [LoFu, Test]
        public async Task when_handling_the_command()
        {
            CommandName = "FakeCommand";
            Use<Mock<ICommandProcessor>>().Setup(x => x.GetCommandType(CommandName)).Returns(typeof(FakeCommand));

            async Task should_invoke_the_command_processor()
            {
                var result = await Subject.HandleAsync(CommandName, Request, Logger);

                result.StatusCode.Should().Be(200);
                result.Body.Should().BeNull();
            }

            async Task should_throw_when_request_is_null()
            {
                Func<Task> act = () => Subject.HandleAsync(CommandName, (APIGatewayHttpApiV2ProxyRequest)null, Logger);
                await act.Should().ThrowAsync<ArgumentNullException>();
            }

            async Task should_handle_CommandProcessorException()
            {
                The<Mock<ICommandProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeCommand>(), It.IsAny<CancellationToken>())).Throws(new CommandProcessorException("fail"));

                var result = await Subject.HandleAsync(CommandName, Request, Logger);

                result.ShouldBeError("fail", 400);
            }

            async Task should_handle_CommandException()
            {
                The<Mock<ICommandProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeCommand>(), It.IsAny<CancellationToken>())).Throws(new CommandException("invalid"));

                var result = await Subject.HandleAsync(CommandName, Request, Logger);

                result.ShouldBeError("invalid", 400);
            }

            async Task should_handle_Exception()
            {
                The<Mock<ICommandProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeCommand>(), It.IsAny<CancellationToken>())).Throws(new Exception("fail"));

                var result = await Subject.HandleAsync(CommandName, Request, Logger);

                result.ShouldBeError("fail", 500);
            }
        }

        [LoFu, Test]
        public async Task when_handling_the_command_with_result()
        {
            CommandName = "FakeResultCommand";
            Use<Mock<ICommandProcessor>>().Setup(x => x.GetCommandType(CommandName)).Returns(typeof(FakeResultCommand));

            async Task should_return_the_result_from_the_command_processor()
            {
                var expected = new FakeResult();
                The<Mock<ICommandProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeResultCommand>(), It.IsAny<CancellationToken>())).Returns(Task.FromResult(expected));

                var result = await Subject.HandleAsync(CommandName, Request, Logger);

                result.StatusCode.Should().Be(200);
                result.Body.Should().NotBeNull();
            }
        }

        APIGatewayHttpApiV2ProxyRequest Request;
        ILambdaLogger Logger;
        string CommandName;
    }
}
```

## File: `tests/CommandQuery.AWSLambda.Tests/CommandQuery.AWSLambda.Tests.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>disable</Nullable>
    <IsPackable>false</IsPackable>
    <IsTestProject>true</IsTestProject>
    <NoWarn>$(NoWarn);CS1998;CS8321;NU1603</NoWarn>
  </PropertyGroup>

  <ItemGroup>
    <Compile Include="..\CommandQuery.Tests\Fake.cs" Link="Fake.cs" />
  </ItemGroup>

  <ItemGroup>
    <PackageReference Include="FluentAssertions" Version="6.12.0" />
    <PackageReference Include="LoFuUnit.AutoMoq" Version="4.0.0-preview.1" />
    <PackageReference Include="LoFuUnit.NUnit" Version="4.0.0-preview.1" />
    <PackageReference Include="Microsoft.CodeCoverage" Version="17.10.0" />
    <PackageReference Include="Microsoft.NET.Test.Sdk" Version="17.10.0" />
    <PackageReference Include="NUnit3TestAdapter" Version="4.5.0">
      <PrivateAssets>all</PrivateAssets>
      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
    </PackageReference>
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\..\src\CommandQuery.AWSLambda\CommandQuery.AWSLambda.csproj" />
  </ItemGroup>

</Project>
```

## File: `tests/CommandQuery.AWSLambda.Tests/QueryFunctionTests.cs`
```csharp
using System.Text.Json;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using CommandQuery.Exceptions;
using CommandQuery.Tests;
using FluentAssertions;

namespace CommandQuery.AWSLambda.Tests
{
    public class QueryFunctionTests_APIGatewayProxyRequest : LoFuTest<QueryFunction>
    {
        [SetUp]
        public void SetUp()
        {
            Clear();
            QueryName = "FakeQuery";
            Use<Mock<IQueryProcessor>>().Setup(x => x.GetQueryType(QueryName)).Returns(typeof(FakeQuery));
            Use<JsonSerializerOptions>(null);
            Logger = One<ILambdaLogger>();
        }

        [LoFu, Test]
        public async Task when_handling_the_query_via_Post()
        {
            Request = new APIGatewayProxyRequest { Body = "{}" };

            async Task should_return_the_result_from_the_query_processor()
            {
                var expected = new FakeResult();
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).ReturnsAsync(expected);

                var result = await Subject.HandleAsync(QueryName, Request, Logger);

                result.StatusCode.Should().Be(200);
                result.Body.Should().NotBeEmpty();
            }

            async Task should_throw_when_request_is_null()
            {
                Func<Task> act = () => Subject.HandleAsync(QueryName, (APIGatewayProxyRequest)null, Logger);
                await act.Should().ThrowAsync<ArgumentNullException>();
            }

            async Task should_handle_QueryProcessorException()
            {
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Throws(new QueryProcessorException("fail"));

                var result = await Subject.HandleAsync(QueryName, Request, Logger);

                result.ShouldBeError("fail", 400);
            }

            async Task should_handle_QueryException()
            {
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Throws(new QueryException("invalid"));

                var result = await Subject.HandleAsync(QueryName, Request, Logger);

                result.ShouldBeError("invalid", 400);
            }

            async Task should_handle_Exception()
            {
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Throws(new Exception("fail"));

                var result = await Subject.HandleAsync(QueryName, Request, Logger);

                result.ShouldBeError("fail", 500);
            }
        }

        [LoFu, Test]
        public async Task when_handling_the_query_via_Get()
        {
            Request = new APIGatewayProxyRequest { HttpMethod = "GET", MultiValueQueryStringParameters = new Dictionary<string, IList<string>> { { "foo", new List<string> { "bar" } } } };

            async Task should_return_the_result_from_the_query_processor()
            {
                var expected = new FakeResult();
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).ReturnsAsync(expected);

                var result = await Subject.HandleAsync(QueryName, Request, Logger);

                result.StatusCode.Should().Be(200);
                result.Body.Should().NotBeEmpty();
            }
        }

        APIGatewayProxyRequest Request;
        ILambdaLogger Logger;
        string QueryName;
    }

    public class QueryFunctionTests_APIGatewayHttpApiV2ProxyRequest : LoFuTest<QueryFunction>
    {
        [SetUp]
        public void SetUp()
        {
            Clear();
            QueryName = "FakeQuery";
            Use<Mock<IQueryProcessor>>().Setup(x => x.GetQueryType(QueryName)).Returns(typeof(FakeQuery));
            Use<JsonSerializerOptions>(null);
            Logger = One<ILambdaLogger>();
        }

        [LoFu, Test]
        public async Task when_handling_the_query_via_Post()
        {
            Request = new APIGatewayHttpApiV2ProxyRequest
            {
                RequestContext = new APIGatewayHttpApiV2ProxyRequest.ProxyRequestContext { Http = new APIGatewayHttpApiV2ProxyRequest.HttpDescription { Method = "POST", Path = "" } },
                Body = "{}",
            };

            async Task should_return_the_result_from_the_query_processor()
            {
                var expected = new FakeResult();
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).ReturnsAsync(expected);

                var result = await Subject.HandleAsync(QueryName, Request, Logger);

                result.StatusCode.Should().Be(200);
                result.Body.Should().NotBeEmpty();
            }

            async Task should_throw_when_request_is_null()
            {
                Func<Task> act = () => Subject.HandleAsync(QueryName, (APIGatewayHttpApiV2ProxyRequest)null, Logger);
                await act.Should().ThrowAsync<ArgumentNullException>();
            }

            async Task should_handle_QueryProcessorException()
            {
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Throws(new QueryProcessorException("fail"));

                var result = await Subject.HandleAsync(QueryName, Request, Logger);

                result.ShouldBeError("fail", 400);
            }

            async Task should_handle_QueryException()
            {
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Throws(new QueryException("invalid"));

                var result = await Subject.HandleAsync(QueryName, Request, Logger);

                result.ShouldBeError("invalid", 400);
            }

            async Task should_handle_Exception()
            {
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Throws(new Exception("fail"));

                var result = await Subject.HandleAsync(QueryName, Request, Logger);

                result.ShouldBeError("fail", 500);
            }
        }

        [LoFu, Test]
        public async Task when_handling_the_query_via_Get()
        {
            Request = new APIGatewayHttpApiV2ProxyRequest
            {
                RequestContext = new APIGatewayHttpApiV2ProxyRequest.ProxyRequestContext { Http = new APIGatewayHttpApiV2ProxyRequest.HttpDescription { Method = "GET" } },
                QueryStringParameters = new Dictionary<string, string> { { "foo", "bar" } },
            };

            async Task should_return_the_result_from_the_query_processor()
            {
                var expected = new FakeResult();
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).ReturnsAsync(expected);

                var result = await Subject.HandleAsync(QueryName, Request, Logger);

                result.StatusCode.Should().Be(200);
                result.Body.Should().NotBeEmpty();
            }
        }

        APIGatewayHttpApiV2ProxyRequest Request;
        ILambdaLogger Logger;
        string QueryName;
    }
}
```

## File: `tests/CommandQuery.AWSLambda.Tests/ServiceCollectionExtensionsTests.cs`
```csharp
using CommandQuery.Tests;
using FluentAssertions;
using Microsoft.Extensions.DependencyInjection;

namespace CommandQuery.AWSLambda.Tests
{
    public class ServiceCollectionExtensionsTests
    {
        [Test]
        public void when_AddCommandFunction()
        {
            var assembly = typeof(FakeCommandHandler).Assembly;
            var serviceCollection = new ServiceCollection();

            serviceCollection.AddCommandFunction(assembly);
            var provider = serviceCollection.BuildServiceProvider();

            provider.GetService<ICommandFunction>().Should().NotBeNull();
        }

        [Test]
        public void when_AddQueryFunction()
        {
            var assembly = typeof(FakeQueryHandler).Assembly;
            var serviceCollection = new ServiceCollection();

            serviceCollection.AddQueryFunction(assembly);
            var provider = serviceCollection.BuildServiceProvider();

            provider.GetService<IQueryFunction>().Should().NotBeNull();
        }
    }
}
```

## File: `tests/CommandQuery.AWSLambda.Tests/ShouldExtensions.cs`
```csharp
using System.Text.Json;
using Amazon.Lambda.APIGatewayEvents;
using CommandQuery.Tests;
using FluentAssertions;

namespace CommandQuery.AWSLambda.Tests
{
    public static class ShouldExtensions
    {
        public static void ShouldBeError(this APIGatewayProxyResponse result, string message, int? statusCode = null)
        {
            result.Should().NotBeNull();
            result.StatusCode.Should().NotBe(200);
            if (statusCode.HasValue) result.StatusCode.Should().Be(statusCode);
            var value = JsonSerializer.Deserialize<FakeError>(result.Body);
            value.Should().NotBeNull();
            value.Message.Should().Be(message);
        }

        public static void ShouldBeError(this APIGatewayHttpApiV2ProxyResponse result, string message, int? statusCode = null)
        {
            result.Should().NotBeNull();
            result.StatusCode.Should().NotBe(200);
            if (statusCode.HasValue) result.StatusCode.Should().Be(statusCode);
            var value = JsonSerializer.Deserialize<FakeError>(result.Body);
            value.Should().NotBeNull();
            value.Message.Should().Be(message);
        }
    }
}
```

## File: `tests/CommandQuery.AWSLambda.Tests/Internal/APIGatewayHttpApiV2ProxyRequestExtensionsTests.cs`
```csharp
using Amazon.Lambda.APIGatewayEvents;
using FluentAssertions;

namespace CommandQuery.AWSLambda.Tests.Internal
{
    public class APIGatewayHttpApiV2ProxyRequestExtensionsTests
    {
        private readonly APIGatewayHttpApiV2ProxyRequest _request = null;

        [Test]
        public void Ok()
        {
            var result = _request.Ok(new { Foo = "Bar" });
            result.StatusCode.Should().Be(200);
            result.Body.Should().Be("{\"Foo\":\"Bar\"}");
        }

        [Test]
        public void BadRequest()
        {
            var exception = new CustomCommandException("fail") { Foo = "Bar" };
            var result = _request.BadRequest(exception);
            result.StatusCode.Should().Be(400);
            result.Body.Should().Be("{\"Message\":\"fail\",\"Details\":{\"Foo\":\"Bar\"}}");
        }

        [Test]
        public void InternalServerError()
        {
            var exception = new CustomCommandException("fail") { Foo = "Bar" };
            var result = _request.InternalServerError(exception);
            result.StatusCode.Should().Be(500);
            result.Body.Should().Be("{\"Message\":\"fail\",\"Details\":{\"Foo\":\"Bar\"}}");
        }
    }
}
```

## File: `tests/CommandQuery.AWSLambda.Tests/Internal/APIGatewayProxyRequestExtensionsTests.cs`
```csharp
using Amazon.Lambda.APIGatewayEvents;
using CommandQuery.Exceptions;
using FluentAssertions;

namespace CommandQuery.AWSLambda.Tests.Internal
{
    public class APIGatewayProxyRequestExtensionsTests
    {
        private readonly APIGatewayProxyRequest _request = null;

        [Test]
        public void Ok()
        {
            var result = _request.Ok(new { Foo = "Bar" });
            result.StatusCode.Should().Be(200);
            result.Body.Should().Be("{\"Foo\":\"Bar\"}");
        }

        [Test]
        public void BadRequest()
        {
            var exception = new CustomCommandException("fail") { Foo = "Bar" };
            var result = _request.BadRequest(exception);
            result.StatusCode.Should().Be(400);
            result.Body.Should().Be("{\"Message\":\"fail\",\"Details\":{\"Foo\":\"Bar\"}}");
        }

        [Test]
        public void InternalServerError()
        {
            var exception = new CustomCommandException("fail") { Foo = "Bar" };
            var result = _request.InternalServerError(exception);
            result.StatusCode.Should().Be(500);
            result.Body.Should().Be("{\"Message\":\"fail\",\"Details\":{\"Foo\":\"Bar\"}}");
        }
    }

    public class CustomCommandException : CommandException
    {
        public string Foo { get; set; }

        public CustomCommandException(string message) : base(message)
        {
        }
    }
}
```

## File: `tests/CommandQuery.AspNetCore.Tests/CommandControllerFeatureProviderTests.cs`
```csharp
using System.Reflection;
using CommandQuery.Tests;
using FluentAssertions;
using Microsoft.AspNetCore.Mvc.Controllers;

namespace CommandQuery.AspNetCore.Tests
{
    public class CommandControllerFeatureProviderTests
    {
        [LoFu, Test]
        public async Task when_PopulateFeature()
        {
            Subject = new CommandControllerFeatureProvider(typeof(FakeCommand).Assembly);
            Result = new ControllerFeature();
            Subject.PopulateFeature(null, Result);

            void should_add_CommandControllers_without_result() =>
                Result.Controllers.Should().Contain(typeof(CommandController<FakeCommand>).GetTypeInfo());

            void should_add_CommandControllers_with_result() =>
                Result.Controllers.Should().Contain(typeof(CommandController<FakeResultCommand, FakeResult>).GetTypeInfo());

            void should_throw_when_feature_is_null() =>
                Subject.Invoking(x => x.PopulateFeature(null, null)).Should().Throw<ArgumentNullException>();
        }

        CommandControllerFeatureProvider Subject;
        ControllerFeature Result;
    }
}
```

## File: `tests/CommandQuery.AspNetCore.Tests/CommandControllerWithResultTests.cs`
```csharp
using CommandQuery.Exceptions;
using CommandQuery.Tests;
using FluentAssertions;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace CommandQuery.AspNetCore.Tests
{
    public class CommandControllerWithResultTests
    {
        [SetUp]
        public void SetUp()
        {
            FakeCommandProcessor = new Mock<ICommandProcessor>();
            Subject = new CommandController<FakeResultCommand, FakeResult>(FakeCommandProcessor.Object, new Mock<ILogger<CommandController<FakeResultCommand, FakeResult>>>().Object);
        }

        [LoFu, Test]
        public async Task when_handling_the_command()
        {
            async Task should_return_the_result_from_the_command_processor()
            {
                var expected = new FakeResult();
                FakeCommandProcessor.Setup(x => x.ProcessAsync(It.IsAny<FakeResultCommand>(), It.IsAny<CancellationToken>())).Returns(Task.FromResult(expected));

                var result = await Subject.HandleAsync(new FakeResultCommand(), CancellationToken.None) as OkObjectResult;

                result.StatusCode.Should().Be(200);
                result.Value.Should().Be(expected);
            }

            async Task should_handle_CommandProcessorException()
            {
                FakeCommandProcessor.Setup(x => x.ProcessAsync(It.IsAny<FakeResultCommand>(), It.IsAny<CancellationToken>())).Throws(new CommandProcessorException("fail"));

                var result = await Subject.HandleAsync(new FakeResultCommand(), CancellationToken.None);

                result.ShouldBeError("fail", 400);
            }

            async Task should_handle_CommandException()
            {
                FakeCommandProcessor.Setup(x => x.ProcessAsync(It.IsAny<FakeResultCommand>(), It.IsAny<CancellationToken>())).Throws(new CommandException("invalid"));

                var result = await Subject.HandleAsync(new FakeResultCommand(), CancellationToken.None);

                result.ShouldBeError("invalid", 400);
            }

            async Task should_handle_Exception()
            {
                FakeCommandProcessor.Setup(x => x.ProcessAsync(It.IsAny<FakeResultCommand>(), It.IsAny<CancellationToken>())).Throws(new Exception("fail"));

                var result = await Subject.HandleAsync(new FakeResultCommand(), CancellationToken.None);

                result.ShouldBeError("fail", 500);
            }
        }

        Mock<ICommandProcessor> FakeCommandProcessor;
        private CommandController<FakeResultCommand, FakeResult> Subject;
    }
}
```

## File: `tests/CommandQuery.AspNetCore.Tests/CommandControllerWithoutResultTests.cs`
```csharp
using CommandQuery.Exceptions;
using CommandQuery.Tests;
using FluentAssertions;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace CommandQuery.AspNetCore.Tests
{
    public class CommandControllerWithoutResultTests
    {
        [SetUp]
        public void SetUp()
        {
            FakeCommandProcessor = new Mock<ICommandProcessor>();
            Subject = new CommandController<FakeCommand>(FakeCommandProcessor.Object, new Mock<ILogger<CommandController<FakeCommand>>>().Object);
        }

        [LoFu, Test]
        public async Task when_handling_the_command()
        {
            async Task should_invoke_the_command_processor()
            {
                var result = await Subject.HandleAsync(new FakeCommand(), CancellationToken.None) as OkResult;

                result.StatusCode.Should().Be(200);
            }

            async Task should_handle_CommandProcessorException()
            {
                FakeCommandProcessor.Setup(x => x.ProcessAsync(It.IsAny<FakeCommand>(), It.IsAny<CancellationToken>())).Throws(new CommandProcessorException("fail"));

                var result = await Subject.HandleAsync(new FakeCommand(), CancellationToken.None);

                result.ShouldBeError("fail", 400);
            }

            async Task should_handle_CommandException()
            {
                FakeCommandProcessor.Setup(x => x.ProcessAsync(It.IsAny<FakeCommand>(), It.IsAny<CancellationToken>())).Throws(new CommandException("invalid"));

                var result = await Subject.HandleAsync(new FakeCommand(), CancellationToken.None);

                result.ShouldBeError("invalid", 400);
            }

            async Task should_handle_Exception()
            {
                FakeCommandProcessor.Setup(x => x.ProcessAsync(It.IsAny<FakeCommand>(), It.IsAny<CancellationToken>())).Throws(new Exception("fail"));

                var result = await Subject.HandleAsync(new FakeCommand(), CancellationToken.None);

                result.ShouldBeError("fail", 500);
            }
        }

        Mock<ICommandProcessor> FakeCommandProcessor;
        private CommandController<FakeCommand> Subject;
    }
}
```

## File: `tests/CommandQuery.AspNetCore.Tests/CommandQuery.AspNetCore.Tests.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>disable</Nullable>
    <IsPackable>false</IsPackable>
    <IsTestProject>true</IsTestProject>
    <NoWarn>$(NoWarn);CS1998;CS8321;NU1603</NoWarn>
  </PropertyGroup>

  <ItemGroup>
    <Compile Include="..\CommandQuery.Tests\Fake.cs" Link="Fake.cs" />
  </ItemGroup>

  <ItemGroup>
    <PackageReference Include="FluentAssertions" Version="6.12.0" />
    <PackageReference Include="LoFuUnit.AutoMoq" Version="4.0.0-preview.1" />
    <PackageReference Include="LoFuUnit.NUnit" Version="4.0.0-preview.1" />
    <PackageReference Include="Microsoft.CodeCoverage" Version="17.10.0" />
    <PackageReference Include="Microsoft.NET.Test.Sdk" Version="17.10.0" />
    <PackageReference Include="NUnit3TestAdapter" Version="4.5.0">
      <PrivateAssets>all</PrivateAssets>
      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
    </PackageReference>
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\..\src\CommandQuery.AspNetCore\CommandQuery.AspNetCore.csproj" />
  </ItemGroup>

</Project>
```

## File: `tests/CommandQuery.AspNetCore.Tests/CommandQueryControllerModelConventionTests.cs`
```csharp
using System.Reflection;
using CommandQuery.Tests;
using FluentAssertions;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.ApplicationModels;

namespace CommandQuery.AspNetCore.Tests
{
    public class CommandQueryControllerModelConventionTests
    {
        [LoFu, Test]
        public async Task when_Apply()
        {
            Subject = new CommandQueryControllerModelConvention();

            void should_handle_CommandControllers_without_result()
            {
                var result = new ControllerModel(typeof(CommandController<FakeCommand>).GetTypeInfo(), []);
                Subject.Apply(result);
                result.ControllerName.Should().Be("FakeCommand");
            }

            void should_handle_CommandControllers_with_result()
            {
                var result = new ControllerModel(typeof(CommandController<FakeResultCommand, FakeResult>).GetTypeInfo(), []);
                Subject.Apply(result);
                result.ControllerName.Should().Be("FakeResultCommand");
            }

            void should_handle_QueryControllers()
            {
                var result = new ControllerModel(typeof(QueryController<FakeQuery, FakeResult>).GetTypeInfo(), []);
                Subject.Apply(result);
                result.ControllerName.Should().Be("FakeQuery");
            }

            void should_not_handle_non_generic_controllers()
            {
                var result = new ControllerModel(typeof(ControllerBase).GetTypeInfo(), []);
                Subject.Apply(result);
                result.ControllerName.Should().BeNull();
            }

            void should_not_handle_unknown_controllers()
            {
                var result = new ControllerModel(typeof(FakeController<>).GetTypeInfo(), []);
                Subject.Apply(result);
                result.ControllerName.Should().BeNull();
            }

            void should_throw_when_controller_is_null()
            {
                Subject.Invoking(x => x.Apply(null)).Should().Throw<ArgumentNullException>();
            }
        }

        CommandQueryControllerModelConvention Subject;

        class FakeController<T> : ControllerBase { }
    }
}
```

## File: `tests/CommandQuery.AspNetCore.Tests/QueryControllerFeatureProviderTests.cs`
```csharp
using System.Reflection;
using CommandQuery.Tests;
using FluentAssertions;
using Microsoft.AspNetCore.Mvc.Controllers;

namespace CommandQuery.AspNetCore.Tests
{
    public class QueryControllerFeatureProviderTests
    {
        [LoFu, Test]
        public async Task when_PopulateFeature()
        {
            Subject = new QueryControllerFeatureProvider(typeof(FakeQuery).Assembly);
            Result = new ControllerFeature();
            Subject.PopulateFeature(null, Result);

            void should_add_QueryControllers() =>
                Result.Controllers.Should().Contain(typeof(QueryController<FakeQuery, FakeResult>).GetTypeInfo());

            void should_throw_when_feature_is_null() =>
                Subject.Invoking(x => x.PopulateFeature(null, null)).Should().Throw<ArgumentNullException>();
        }

        QueryControllerFeatureProvider Subject;
        ControllerFeature Result;
    }
}
```

## File: `tests/CommandQuery.AspNetCore.Tests/QueryControllerTests.cs`
```csharp
using CommandQuery.Exceptions;
using CommandQuery.Tests;
using FluentAssertions;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace CommandQuery.AspNetCore.Tests
{
    public class QueryControllerTests
    {
        [SetUp]
        public void SetUp()
        {
            FakeQueryProcessor = new Mock<IQueryProcessor>();
            Subject = new QueryController<FakeQuery, FakeResult>(FakeQueryProcessor.Object, new Mock<ILogger<QueryController<FakeQuery, FakeResult>>>().Object);
        }

        [LoFu, Test]
        public async Task when_handling_the_query_via_Post()
        {
            async Task should_return_the_result_from_the_query_processor()
            {
                var expected = new FakeResult();
                FakeQueryProcessor.Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Returns(Task.FromResult(expected));

                var result = await Subject.HandlePostAsync(new FakeQuery(), CancellationToken.None) as OkObjectResult;

                result.StatusCode.Should().Be(200);
                result.Value.Should().Be(expected);
            }

            async Task should_handle_QueryProcessorException()
            {
                FakeQueryProcessor.Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Throws(new QueryProcessorException("fail"));

                var result = await Subject.HandlePostAsync(new FakeQuery(), CancellationToken.None);

                result.ShouldBeError("fail", 400);
            }

            async Task should_handle_QueryException()
            {
                FakeQueryProcessor.Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Throws(new QueryException("invalid"));

                var result = await Subject.HandlePostAsync(new FakeQuery(), CancellationToken.None);

                result.ShouldBeError("invalid", 400);
            }

            async Task should_handle_Exception()
            {
                FakeQueryProcessor.Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Throws(new Exception("fail"));

                var result = await Subject.HandlePostAsync(new FakeQuery(), CancellationToken.None);

                result.ShouldBeError("fail", 500);
            }
        }

        [LoFu, Test]
        public async Task when_handling_the_query_via_Get()
        {
            async Task should_return_the_result_from_the_query_processor()
            {
                var expected = new FakeResult();
                FakeQueryProcessor.Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Returns(Task.FromResult(expected));

                var result = await Subject.HandleGetAsync(new FakeQuery(), CancellationToken.None) as OkObjectResult;

                result.StatusCode.Should().Be(200);
                result.Value.Should().Be(expected);
            }

            async Task should_handle_QueryProcessorException()
            {
                FakeQueryProcessor.Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Throws(new QueryProcessorException("fail"));

                var result = await Subject.HandleGetAsync(new FakeQuery(), CancellationToken.None);

                result.ShouldBeError("fail", 400);
            }

            async Task should_handle_QueryException()
            {
                FakeQueryProcessor.Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Throws(new QueryException("invalid"));

                var result = await Subject.HandleGetAsync(new FakeQuery(), CancellationToken.None);

                result.ShouldBeError("invalid", 400);
            }

            async Task should_handle_Exception()
            {
                FakeQueryProcessor.Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Throws(new Exception("fail"));

                var result = await Subject.HandleGetAsync(new FakeQuery(), CancellationToken.None);

                result.ShouldBeError("fail", 500);
            }
        }

        Mock<IQueryProcessor> FakeQueryProcessor;
        private QueryController<FakeQuery, FakeResult> Subject;
    }
}
```

## File: `tests/CommandQuery.AspNetCore.Tests/ServiceCollectionExtensionsTests.cs`
```csharp
using System.Reflection;
using CommandQuery.Tests;
using FluentAssertions;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Controllers;
using Microsoft.AspNetCore.Routing;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;

namespace CommandQuery.AspNetCore.Tests
{
    public class ServiceCollectionExtensionsTests
    {
        [Test]
        public void when_AddCommandControllers()
        {
            var assembly = typeof(FakeCommandHandler).Assembly;
            var serviceCollection = new ServiceCollection();

            serviceCollection
                .AddCommandControllers(assembly)
                .AddLogging(logging => logging.AddConsole());
            var provider = serviceCollection.BuildServiceProvider();
            var activator = provider.GetService<IControllerActivator>();

            CreateController(activator, provider, typeof(CommandController<FakeCommand>)).Should().NotBeNull();
            CreateController(activator, provider, typeof(CommandController<FakeResultCommand, FakeResult>)).Should().NotBeNull();
        }

        [Test]
        public void when_AddQueryControllers()
        {
            var assembly = typeof(FakeQueryHandler).Assembly;
            var serviceCollection = new ServiceCollection();

            serviceCollection
                .AddQueryControllers(assembly)
                .AddLogging(logging => logging.AddConsole());
            var provider = serviceCollection.BuildServiceProvider();
            var activator = provider.GetService<IControllerActivator>();

            CreateController(activator, provider, typeof(QueryController<FakeQuery, FakeResult>)).Should().NotBeNull();
        }

        private static object CreateController(IControllerActivator activator, ServiceProvider provider, Type controllerType)
        {
            var actionContext = new ActionContext(
                new DefaultHttpContext
                {
                    RequestServices = provider
                },
                new RouteData(),
                new ControllerActionDescriptor
                {
                    ControllerTypeInfo = controllerType.GetTypeInfo()
                });
            return activator.Create(new ControllerContext(actionContext));
        }
    }
}
```

## File: `tests/CommandQuery.AspNetCore.Tests/ShouldExtensions.cs`
```csharp
using FluentAssertions;
using Microsoft.AspNetCore.Mvc;

namespace CommandQuery.AspNetCore.Tests
{
    public static class ShouldExtensions
    {
        public static void ShouldBeError(this IActionResult result, string message, int? statusCode = null)
        {
            ShouldBeError(result as ObjectResult, message, statusCode);
        }

        public static void ShouldBeError(this ObjectResult result, string message, int? statusCode = null)
        {
            result.Should().NotBeNull();
            result.StatusCode.Should().NotBe(200);
            if (statusCode.HasValue) result.StatusCode.Should().Be(statusCode);
            var value = result.Value as IError;
            value.Should().NotBeNull();
            value.Message.Should().Be(message);
        }
    }
}
```

## File: `tests/CommandQuery.AzureFunctions.Tests/CommandFunctionTests.cs`
```csharp
using System.Net;
using System.Text;
using System.Text.Json;
using CommandQuery.Exceptions;
using CommandQuery.Tests;
using FluentAssertions;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Infrastructure;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Http;

namespace CommandQuery.AzureFunctions.Tests
{
    public class CommandFunctionTests_HttpRequestData : LoFuTest<CommandFunction>
    {
        [SetUp]
        public async Task SetUp()
        {
            Clear();
            Use<JsonSerializerOptions>(null);

            Req = new FakeHttpRequestData(One<FunctionContext>());
            await Req.Body.WriteAsync(Encoding.UTF8.GetBytes("{}"));
        }

        [LoFu, Test]
        public async Task when_handling_the_command()
        {
            CommandName = "FakeCommand";
            Use<Mock<ICommandProcessor>>().Setup(x => x.GetCommandType(CommandName)).Returns(typeof(FakeCommand));

            async Task should_invoke_the_command_processor()
            {
                Req.Body.Position = 0;
                var result = await Subject.HandleAsync(CommandName, Req);
                result.StatusCode.Should().Be(HttpStatusCode.OK);
            }

            async Task should_throw_when_request_is_null()
            {
                Func<Task> act = () => Subject.HandleAsync(CommandName, (HttpRequestData)null);
                await act.Should().ThrowAsync<ArgumentNullException>();
            }

            async Task should_handle_CommandProcessorException()
            {
                Req.Body.Position = 0;
                The<Mock<ICommandProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeCommand>(), It.IsAny<CancellationToken>())).Throws(new CommandProcessorException("fail"));

                var result = await Subject.HandleAsync(CommandName, Req);

                await result.ShouldBeErrorAsync("fail", HttpStatusCode.BadRequest);
            }

            async Task should_handle_CommandException()
            {
                Req.Body.Position = 0;
                The<Mock<ICommandProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeCommand>(), It.IsAny<CancellationToken>())).Throws(new CommandException("invalid"));

                var result = await Subject.HandleAsync(CommandName, Req);

                await result.ShouldBeErrorAsync("invalid", HttpStatusCode.BadRequest);
            }

            async Task should_handle_Exception()
            {
                Req.Body.Position = 0;
                The<Mock<ICommandProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeCommand>(), It.IsAny<CancellationToken>())).Throws(new Exception("fail"));

                var result = await Subject.HandleAsync(CommandName, Req);

                await result.ShouldBeErrorAsync("fail", HttpStatusCode.InternalServerError);
            }
        }

        [LoFu, Test]
        public async Task when_handling_the_command_with_result()
        {
            CommandName = "FakeResultCommand";
            Use<Mock<ICommandProcessor>>().Setup(x => x.GetCommandType(CommandName)).Returns(typeof(FakeResultCommand));

            async Task should_return_the_result_from_the_command_processor()
            {
                Req.Body.Position = 0;
                var expected = new FakeResult();
                The<Mock<ICommandProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeResultCommand>(), It.IsAny<CancellationToken>())).Returns(Task.FromResult(expected));

                var result = await Subject.HandleAsync(CommandName, Req);
                result.Body.Position = 0;

                result.StatusCode.Should().Be(HttpStatusCode.OK);
                result.Body.Length.Should().BeGreaterThan(0);
            }
        }

        HttpRequestData Req;
        string CommandName;
    }

    public class CommandFunctionTests_HttpRequest : LoFuTest<CommandFunction>
    {
        [SetUp]
        public async Task SetUp()
        {
            Clear();
            Use<JsonSerializerOptions>(null);

            var mock = new Mock<HttpRequest>();
            mock.SetupGet(x => x.Body).Returns(new MemoryStream(Encoding.UTF8.GetBytes("{}")));
            Req = mock.Object;
        }

        [LoFu, Test]
        public async Task when_handling_the_command()
        {
            CommandName = "FakeCommand";
            Use<Mock<ICommandProcessor>>().Setup(x => x.GetCommandType(CommandName)).Returns(typeof(FakeCommand));

            async Task should_invoke_the_command_processor()
            {
                Req.Body.Position = 0;
                var result = await Subject.HandleAsync(CommandName, Req) as IStatusCodeActionResult;
                result.StatusCode.Should().Be(200);
            }

            async Task should_throw_when_request_is_null()
            {
                Func<Task> act = () => Subject.HandleAsync(CommandName, (HttpRequest)null);
                await act.Should().ThrowAsync<ArgumentNullException>();
            }

            async Task should_handle_CommandProcessorException()
            {
                Req.Body.Position = 0;
                The<Mock<ICommandProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeCommand>(), It.IsAny<CancellationToken>())).Throws(new CommandProcessorException("fail"));

                var result = await Subject.HandleAsync(CommandName, Req);

                result.ShouldBeError("fail", 400);
            }

            async Task should_handle_CommandException()
            {
                Req.Body.Position = 0;
                The<Mock<ICommandProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeCommand>(), It.IsAny<CancellationToken>())).Throws(new CommandException("invalid"));

                var result = await Subject.HandleAsync(CommandName, Req);

                result.ShouldBeError("invalid", 400);
            }

            async Task should_handle_Exception()
            {
                Req.Body.Position = 0;
                The<Mock<ICommandProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeCommand>(), It.IsAny<CancellationToken>())).Throws(new Exception("fail"));

                var result = await Subject.HandleAsync(CommandName, Req);

                result.ShouldBeError("fail", 500);
            }
        }

        [LoFu, Test]
        public async Task when_handling_the_command_with_result()
        {
            CommandName = "FakeResultCommand";
            Use<Mock<ICommandProcessor>>().Setup(x => x.GetCommandType(CommandName)).Returns(typeof(FakeResultCommand));

            async Task should_return_the_result_from_the_command_processor()
            {
                Req.Body.Position = 0;
                var expected = new FakeResult();
                The<Mock<ICommandProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeResultCommand>(), It.IsAny<CancellationToken>())).Returns(Task.FromResult(expected));

                var result = await Subject.HandleAsync(CommandName, Req);

                (result as IStatusCodeActionResult).StatusCode.Should().Be(200);
                (result as ObjectResult).Value.Should().NotBeNull();
            }
        }

        HttpRequest Req;
        string CommandName;
    }
}
```

## File: `tests/CommandQuery.AzureFunctions.Tests/CommandQuery.AzureFunctions.Tests.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>disable</Nullable>
    <IsPackable>false</IsPackable>
    <IsTestProject>true</IsTestProject>
    <NoWarn>$(NoWarn);CS1998;CS8321;NU1603</NoWarn>
  </PropertyGroup>

  <ItemGroup>
    <Compile Include="..\CommandQuery.Tests\Fake.cs" Link="Fake.cs" />
  </ItemGroup>

  <ItemGroup>
    <PackageReference Include="FluentAssertions" Version="6.12.0" />
    <PackageReference Include="LoFuUnit.AutoMoq" Version="4.0.0-preview.1" />
    <PackageReference Include="LoFuUnit.NUnit" Version="4.0.0-preview.1" />
    <PackageReference Include="Microsoft.CodeCoverage" Version="17.10.0" />
    <PackageReference Include="Microsoft.NET.Test.Sdk" Version="17.10.0" />
    <PackageReference Include="NUnit3TestAdapter" Version="4.5.0">
      <PrivateAssets>all</PrivateAssets>
      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
    </PackageReference>
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\..\src\CommandQuery.AzureFunctions\CommandQuery.AzureFunctions.csproj" />
  </ItemGroup>

</Project>
```

## File: `tests/CommandQuery.AzureFunctions.Tests/FakeHttpData.cs`
```csharp
using System.Net;
using System.Security.Claims;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Http;

namespace CommandQuery.AzureFunctions.Tests
{
    public class FakeHttpRequestData : HttpRequestData
    {
        public FakeHttpRequestData(FunctionContext functionContext, string method = null, Uri url = null) : base(functionContext)
        {
            Method = method;
            Url = url;
        }

        public override Stream Body { get; } = new MemoryStream();

        public override HttpHeadersCollection Headers { get; } = [];

        public override IReadOnlyCollection<IHttpCookie> Cookies { get; }

        public override Uri Url { get; }

        public override IEnumerable<ClaimsIdentity> Identities { get; }

        public override string Method { get; }

        public override HttpResponseData CreateResponse()
        {
            return new FakeHttpResponseData(FunctionContext);
        }
    }

    public class FakeHttpResponseData : HttpResponseData
    {
        public FakeHttpResponseData(FunctionContext functionContext) : base(functionContext)
        {
        }

        public override HttpStatusCode StatusCode { get; set; }
        public override HttpHeadersCollection Headers { get; set; } = [];
        public override Stream Body { get; set; } = new MemoryStream();
        public override HttpCookies Cookies { get; }
    }
}
```

## File: `tests/CommandQuery.AzureFunctions.Tests/QueryFunctionTests.cs`
```csharp
using System.Net;
using System.Text;
using System.Text.Json;
using CommandQuery.Exceptions;
using CommandQuery.Tests;
using FluentAssertions;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Infrastructure;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Http;

namespace CommandQuery.AzureFunctions.Tests
{
    public class QueryFunctionTests_HttpRequestData : LoFuTest<QueryFunction>
    {
        [SetUp]
        public void SetUp()
        {
            Clear();
            QueryName = "FakeQuery";
            Use<Mock<IQueryProcessor>>().Setup(x => x.GetQueryType(QueryName)).Returns(typeof(FakeQuery));
            Use<JsonSerializerOptions>(null);

            Context = One<FunctionContext>();
        }

        [LoFu, Test]
        public async Task when_handling_the_query_via_Post()
        {
            Req = new FakeHttpRequestData(Context, "POST");
            await Req.Body.WriteAsync(Encoding.UTF8.GetBytes("{}"));

            async Task should_return_the_result_from_the_query_processor()
            {
                Req.Body.Position = 0;
                var expected = new FakeResult();
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Returns(Task.FromResult(expected));

                var result = await Subject.HandleAsync(QueryName, Req);

                result.StatusCode.Should().Be(HttpStatusCode.OK);
                result.Body.Length.Should().BeGreaterThan(0);
            }

            async Task should_throw_when_request_is_null()
            {
                Func<Task> act = () => Subject.HandleAsync(QueryName, (HttpRequestData)null);
                await act.Should().ThrowAsync<ArgumentNullException>();
            }

            async Task should_handle_QueryProcessorException()
            {
                Req.Body.Position = 0;
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Throws(new QueryProcessorException("fail"));

                var result = await Subject.HandleAsync(QueryName, Req);

                await result.ShouldBeErrorAsync("fail", HttpStatusCode.BadRequest);
            }

            async Task should_handle_QueryException()
            {
                Req.Body.Position = 0;
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Throws(new QueryException("invalid"));

                var result = await Subject.HandleAsync(QueryName, Req);

                await result.ShouldBeErrorAsync("invalid", HttpStatusCode.BadRequest);
            }

            async Task should_handle_Exception()
            {
                Req.Body.Position = 0;
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Throws(new Exception("fail"));

                var result = await Subject.HandleAsync(QueryName, Req);

                await result.ShouldBeErrorAsync("fail", HttpStatusCode.InternalServerError);
            }
        }

        [LoFu, Test]
        public async Task when_handling_the_query_via_Get()
        {
            Req = new FakeHttpRequestData(Context, "GET", new Uri("http://localhost/api/query/FakeQuery?foo=bar"));

            async Task should_return_the_result_from_the_query_processor()
            {
                var expected = new FakeResult();
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Returns(Task.FromResult(expected));

                var result = await Subject.HandleAsync(QueryName, Req);

                result.StatusCode.Should().Be(HttpStatusCode.OK);
                result.Body.Length.Should().BeGreaterThan(0);
            }
        }

        HttpRequestData Req;
        string QueryName;
        FunctionContext Context;
    }

    public class QueryFunctionTests_HttpRequest : LoFuTest<QueryFunction>
    {
        [SetUp]
        public void SetUp()
        {
            Clear();
            QueryName = "FakeQuery";
            Use<Mock<IQueryProcessor>>().Setup(x => x.GetQueryType(QueryName)).Returns(typeof(FakeQuery));
            Use<JsonSerializerOptions>(null);

            Context = One<FunctionContext>();
        }

        [LoFu, Test]
        public async Task when_handling_the_query_via_Post()
        {
            var mock = new Mock<HttpRequest>();
            mock.Setup(x => x.Method).Returns("POST");
            mock.SetupGet(x => x.Body).Returns(new MemoryStream(Encoding.UTF8.GetBytes("{}")));
            Req = mock.Object;

            async Task should_return_the_result_from_the_query_processor()
            {
                Req.Body.Position = 0;
                var expected = new FakeResult();
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Returns(Task.FromResult(expected));

                var result = await Subject.HandleAsync(QueryName, Req);

                (result as IStatusCodeActionResult).StatusCode.Should().Be(200);
                (result as ObjectResult).Value.Should().NotBeNull();
            }

            async Task should_throw_when_request_is_null()
            {
                Func<Task> act = () => Subject.HandleAsync(QueryName, (HttpRequest)null);
                await act.Should().ThrowAsync<ArgumentNullException>();
            }

            async Task should_handle_QueryProcessorException()
            {
                Req.Body.Position = 0;
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Throws(new QueryProcessorException("fail"));

                var result = await Subject.HandleAsync(QueryName, Req);

                result.ShouldBeError("fail", 400);
            }

            async Task should_handle_QueryException()
            {
                Req.Body.Position = 0;
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Throws(new QueryException("invalid"));

                var result = await Subject.HandleAsync(QueryName, Req);

                result.ShouldBeError("invalid", 400);
            }

            async Task should_handle_Exception()
            {
                Req.Body.Position = 0;
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Throws(new Exception("fail"));

                var result = await Subject.HandleAsync(QueryName, Req);

                result.ShouldBeError("fail", 500);
            }
        }

        [LoFu, Test]
        public async Task when_handling_the_query_via_Get()
        {
            var mock = new Mock<HttpRequest>();
            mock.SetupGet(x => x.Method).Returns("GET");
            mock.SetupGet(x => x.Query).Returns(new QueryCollection());
            Req = mock.Object;

            async Task should_return_the_result_from_the_query_processor()
            {
                var expected = new FakeResult();
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Returns(Task.FromResult(expected));

                var result = await Subject.HandleAsync(QueryName, Req);

                (result as IStatusCodeActionResult).StatusCode.Should().Be(200);
                (result as ObjectResult).Value.Should().NotBeNull();
            }
        }

        HttpRequest Req;
        string QueryName;
        FunctionContext Context;
    }
}
```

## File: `tests/CommandQuery.AzureFunctions.Tests/ServiceCollectionExtensionsTests.cs`
```csharp
using CommandQuery.Tests;
using FluentAssertions;
using Microsoft.Extensions.DependencyInjection;

namespace CommandQuery.AzureFunctions.Tests
{
    public class ServiceCollectionExtensionsTests
    {
        [Test]
        public void when_AddCommandFunction()
        {
            var assembly = typeof(FakeCommandHandler).Assembly;
            var serviceCollection = new ServiceCollection();

            serviceCollection.AddLogging();
            serviceCollection.AddCommandFunction(assembly);
            var provider = serviceCollection.BuildServiceProvider();

            provider.GetService<ICommandFunction>().Should().NotBeNull();
        }

        [Test]
        public void when_AddQueryFunction()
        {
            var assembly = typeof(FakeQueryHandler).Assembly;
            var serviceCollection = new ServiceCollection();

            serviceCollection.AddLogging();
            serviceCollection.AddQueryFunction(assembly);
            var provider = serviceCollection.BuildServiceProvider();

            provider.GetService<IQueryFunction>().Should().NotBeNull();
        }
    }
}
```

## File: `tests/CommandQuery.AzureFunctions.Tests/ShouldExtensions.cs`
```csharp
using System.Net;
using System.Text.Json;
using CommandQuery.Tests;
using FluentAssertions;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Infrastructure;
using Microsoft.Azure.Functions.Worker.Http;

namespace CommandQuery.AzureFunctions.Tests
{
    public static class ShouldExtensions
    {
        public static async Task ShouldBeErrorAsync(this HttpResponseData result, string message, HttpStatusCode? statusCode = null)
        {
            result.Should().NotBeNull();
            result.StatusCode.Should().NotBe(HttpStatusCode.OK);
            if (statusCode.HasValue) result.StatusCode.Should().Be(statusCode);
            result.Body.Position = 0;
            var value = await JsonSerializer.DeserializeAsync<FakeError>(result.Body);
            value.Should().NotBeNull();
            value.Message.Should().Be(message);
        }

        public static void ShouldBeError(this IActionResult result, string message, int? statusCode = null)
        {
            result.Should().NotBeNull();

            var resultWithStatusCode = result as IStatusCodeActionResult;
            resultWithStatusCode.StatusCode.Should().NotBe(200);
            if (statusCode.HasValue) resultWithStatusCode.StatusCode.Should().Be(statusCode);

            var resultWithValue = result as ObjectResult;
            var value = resultWithValue.Value as IError;
            value.Should().NotBeNull();
            value.Message.Should().Be(message);
        }
    }
}
```

## File: `tests/CommandQuery.AzureFunctions.Tests/Internal/HttpRequestDataExtensionsTests.cs`
```csharp
using System.Net;
using CommandQuery.Exceptions;
using FluentAssertions;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Http;

namespace CommandQuery.AzureFunctions.Tests.Internal
{
    public class HttpRequestDataExtensionsTests
    {
        private HttpRequestData Req;

        [SetUp]
        public void SetUp()
        {
            var context = new Mock<FunctionContext>();
            Req = new FakeHttpRequestData(context.Object);
        }

        [Test]
        public async Task OkAsync()
        {
            var response = await Req.OkAsync(new { Foo = "Bar" }, null);
            response.StatusCode.Should().Be(HttpStatusCode.OK);
            response.Body.Position = 0;
            var result = await new StreamReader(response.Body).ReadToEndAsync();
            result.Should().Be("{\"Foo\":\"Bar\"}");
        }

        [Test]
        public async Task BadRequestAsync()
        {
            var exception = new CustomCommandException("fail") { Foo = "Bar" };
            var response = await Req.BadRequestAsync(exception, null);
            response.StatusCode.Should().Be(HttpStatusCode.BadRequest);
            response.Body.Position = 0;
            var result = await new StreamReader(response.Body).ReadToEndAsync();
            result.Should().Be("{\"Message\":\"fail\",\"Details\":{\"Foo\":\"Bar\"}}");
        }

        [Test]
        public async Task InternalServerErrorAsync()
        {
            var exception = new CustomCommandException("fail") { Foo = "Bar" };
            var response = await Req.InternalServerErrorAsync(exception, null);
            response.StatusCode.Should().Be(HttpStatusCode.InternalServerError);
            response.Body.Position = 0;
            var result = await new StreamReader(response.Body).ReadToEndAsync();
            result.Should().Be("{\"Message\":\"fail\",\"Details\":{\"Foo\":\"Bar\"}}");
        }
    }

    public class CustomCommandException : CommandException
    {
        public string Foo { get; set; }

        public CustomCommandException(string message) : base(message)
        {
        }
    }
}
```

## File: `tests/CommandQuery.AzureFunctions.Tests/Internal/HttpRequestExtensionsTests.cs`
```csharp
using System.Text;
using FluentAssertions;
using Microsoft.AspNetCore.Http;

namespace CommandQuery.AzureFunctions.Tests.Internal
{
    public class HttpRequestExtensionsTests
    {
        [LoFu, Test]
        public async Task ReadAsStringAsync()
        {
            async Task should_return_a_string()
            {
                var mock = new Mock<HttpRequest>();
                mock.SetupGet(x => x.Body).Returns(new MemoryStream(Encoding.UTF8.GetBytes("{}")));
                var req = mock.Object;

                var result = await req.ReadAsStringAsync();
                result.Should().Be("{}");
            }

            async Task should_throw_when_request_is_null()
            {
                Func<Task> act = () => ((HttpRequest)null).ReadAsStringAsync();
                await act.Should().ThrowAsync<ArgumentNullException>();
            }

            async Task should_return_null_when_body_is_null()
            {
                var result = await new Mock<HttpRequest>().Object.ReadAsStringAsync();
                result.Should().BeNull();
            }
        }
    }
}
```

## File: `tests/CommandQuery.Benchmark/CommandQuery.Benchmark.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <OutputType>Exe</OutputType>
    <Nullable>disable</Nullable>
  </PropertyGroup>

  <PropertyGroup>
    <PlatformTarget>AnyCPU</PlatformTarget>
    <DebugType>pdbonly</DebugType>
    <DebugSymbols>true</DebugSymbols>
    <AllowUnsafeBlocks>true</AllowUnsafeBlocks>
    <Optimize>true</Optimize>
    <Configuration>Release</Configuration>
    <IsPackable>false</IsPackable>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="BenchmarkDotNet" Version="0.13.12" />
    <PackageReference Include="BenchmarkDotNet.Diagnostics.Windows" Version="0.13.12" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\..\src\CommandQuery.SystemTextJson\CommandQuery.SystemTextJson.csproj" />
  </ItemGroup>

</Project>
```

## File: `tests/CommandQuery.Benchmark/JsonBenchmarks.cs`
```csharp
using BenchmarkDotNet.Attributes;

namespace CommandQuery.Benchmark
{
    public class JsonBenchmarks
    {
        private FakeComplexObject _object;
        private string _systemTextJsonString;
        private Dictionary<string, object> _dictionary;

        [GlobalSetup]
        public void GlobalSetup()
        {
            _object = new FakeComplexObject
            {
                String = "String",
                Int = 1,
                Bool = true,
                DateTime = DateTime.Parse("2021-07-04 20:31:48"),
                Guid = Guid.Parse("b665da2a-60fe-4f2b-baf1-9d766e2542d3"),
                NullableDouble = 2.1,
                Array = [1, 2],
                IEnumerable = [3, 4],
                List = [5, 6]
            };

            _systemTextJsonString = System.Text.Json.JsonSerializer.Serialize(_object);

            _dictionary = new Dictionary<string, object>
            {
                { "String", "String" },
                { "Int", "1" },
                { "Bool", "true" },
                { "DateTime", "2021-07-04 20:31:48" },
                { "Guid", "b665da2a-60fe-4f2b-baf1-9d766e2542d3" },
                { "NullableDouble", "2.1" },
                { "Array", new[] { "1", "2" } },
                { "IEnumerable", new[] { "3", "4" } },
                { "List", new[] { "5", "6" } }
            };
        }

        // SystemTextJson

        [Benchmark]
        public object SystemTextJson_string_SafeDeserialize() => SystemTextJson.JsonExtensions.SafeDeserialize(_systemTextJsonString, typeof(FakeComplexObject), null);

        [Benchmark]
        public object SystemTextJson_Dictionary_SafeDeserialize() => SystemTextJson.JsonExtensions.SafeDeserialize(_dictionary, typeof(FakeComplexObject));
    }

    public class FakeComplexObject
    {
        public string String { get; set; }
        public int Int { get; set; }
        public bool Bool { get; set; }
        public DateTime DateTime { get; set; }
        public Guid Guid { get; set; }
        public double? NullableDouble { get; set; }
        public int[] Array { get; set; }
        public IEnumerable<int> IEnumerable { get; set; }
        public List<int> List { get; set; }
    }
}
```

## File: `tests/CommandQuery.Benchmark/Program.cs`
```csharp
using BenchmarkDotNet.Running;

namespace CommandQuery.Benchmark
{
    public class Program
    {
        public static void Main(string[] args)
        {
            BenchmarkRunner.Run<JsonBenchmarks>();
        }
    }
}
```

## File: `tests/CommandQuery.Benchmark/run.bat`
```
dotnet run --configuration Release
```

## File: `tests/CommandQuery.Fail/CommandQuery.Fail.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>netstandard2.0</TargetFramework>
    <Nullable>disable</Nullable>
    <IsPackable>false</IsPackable>
  </PropertyGroup>

  <ItemGroup>
    <ProjectReference Include="..\..\src\CommandQuery.Abstractions\CommandQuery.Abstractions.csproj" />
  </ItemGroup>

</Project>
```

## File: `tests/CommandQuery.Fail/Dupes.cs`
```csharp
namespace CommandQuery.Fail
{
    public class DupeCommand : ICommand { }

    public class DupeQuery : IQuery<object> { }
}
```

## File: `tests/CommandQuery.Fail/Folder/Dupes.cs`
```csharp
namespace CommandQuery.Fail.Folder
{
    public class DupeCommand : ICommand { }

    public class DupeQuery : IQuery<object> { }
}
```

## File: `tests/CommandQuery.GoogleCloudFunctions.Tests/CommandFunctionTests.cs`
```csharp
using System.Text;
using System.Text.Json;
using CommandQuery.Exceptions;
using CommandQuery.Tests;
using FluentAssertions;
using Microsoft.AspNetCore.Http;

namespace CommandQuery.GoogleCloudFunctions.Tests
{
    public class CommandFunctionTests : LoFuTest<CommandFunction>
    {
        [SetUp]
        public void SetUp()
        {
            Clear();
            Use<JsonSerializerOptions>(null);
            Context = new DefaultHttpContext();
            Context.Request.Body = new MemoryStream(Encoding.UTF8.GetBytes("{}"));
            Context.Response.Body = new MemoryStream();
        }

        [LoFu, Test]
        public async Task when_handling_the_command()
        {
            CommandName = "FakeCommand";
            Use<Mock<ICommandProcessor>>().Setup(x => x.GetCommandType(CommandName)).Returns(typeof(FakeCommand));

            async Task should_invoke_the_command_processor()
            {
                Context.Request.Body.Position = 0;
                Context.Response.Clear();
                await Subject.HandleAsync(CommandName, Context);

                Context.Response.StatusCode.Should().Be(200);
            }

            async Task should_throw_when_request_is_null()
            {
                Func<Task> act = () => Subject.HandleAsync(CommandName, null);
                await act.Should().ThrowAsync<ArgumentNullException>();
            }

            async Task should_handle_CommandProcessorException()
            {
                Context.Request.Body.Position = 0;
                Context.Response.Clear();
                The<Mock<ICommandProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeCommand>(), It.IsAny<CancellationToken>())).Throws(new CommandProcessorException("fail"));

                await Subject.HandleAsync(CommandName, Context);

                await Context.Response.ShouldBeErrorAsync("fail", 400);
            }

            async Task should_handle_CommandException()
            {
                Context.Request.Body.Position = 0;
                Context.Response.Clear();
                The<Mock<ICommandProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeCommand>(), It.IsAny<CancellationToken>())).Throws(new CommandException("invalid"));

                await Subject.HandleAsync(CommandName, Context);

                await Context.Response.ShouldBeErrorAsync("invalid", 400);
            }

            async Task should_handle_Exception()
            {
                Context.Request.Body.Position = 0;
                Context.Response.Clear();
                The<Mock<ICommandProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeCommand>(), It.IsAny<CancellationToken>())).Throws(new Exception("fail"));

                await Subject.HandleAsync(CommandName, Context);

                await Context.Response.ShouldBeErrorAsync("fail", 500);
            }
        }

        [LoFu, Test]
        public async Task when_handling_the_command_with_result()
        {
            CommandName = "FakeResultCommand";
            Use<Mock<ICommandProcessor>>().Setup(x => x.GetCommandType(CommandName)).Returns(typeof(FakeResultCommand));

            async Task should_return_the_result_from_the_command_processor()
            {
                Context.Response.Clear();
                var expected = new FakeResult();
                The<Mock<ICommandProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeResultCommand>(), It.IsAny<CancellationToken>())).Returns(Task.FromResult(expected));

                await Subject.HandleAsync(CommandName, Context);

                Context.Response.StatusCode.Should().Be(200);
                Context.Response.Body.Length.Should().BeGreaterThan(0);
            }
        }

        HttpContext Context;
        string CommandName;
    }
}
```

## File: `tests/CommandQuery.GoogleCloudFunctions.Tests/CommandQuery.GoogleCloudFunctions.Tests.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>disable</Nullable>
    <IsPackable>false</IsPackable>
    <IsTestProject>true</IsTestProject>
    <NoWarn>$(NoWarn);CS1998;CS8321;NU1603</NoWarn>
  </PropertyGroup>

  <ItemGroup>
    <Compile Include="..\CommandQuery.Tests\Fake.cs" Link="Fake.cs" />
  </ItemGroup>

  <ItemGroup>
    <PackageReference Include="FluentAssertions" Version="6.12.0" />
    <PackageReference Include="LoFuUnit.AutoMoq" Version="4.0.0-preview.1" />
    <PackageReference Include="LoFuUnit.NUnit" Version="4.0.0-preview.1" />
    <PackageReference Include="Microsoft.AspNetCore.Http.Extensions" Version="2.1.21" />
    <PackageReference Include="Microsoft.CodeCoverage" Version="17.10.0" />
    <PackageReference Include="Microsoft.Extensions.Logging" Version="8.0.0" />
    <PackageReference Include="Microsoft.NET.Test.Sdk" Version="17.10.0" />
    <PackageReference Include="NUnit3TestAdapter" Version="4.5.0">
      <PrivateAssets>all</PrivateAssets>
      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
    </PackageReference>
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\..\src\CommandQuery.GoogleCloudFunctions\CommandQuery.GoogleCloudFunctions.csproj" />
  </ItemGroup>

</Project>
```

## File: `tests/CommandQuery.GoogleCloudFunctions.Tests/QueryFunctionTests.cs`
```csharp
using System.Text;
using System.Text.Json;
using CommandQuery.Exceptions;
using CommandQuery.Tests;
using FluentAssertions;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Http.Internal;
using Microsoft.Extensions.Primitives;

namespace CommandQuery.GoogleCloudFunctions.Tests
{
    public class QueryFunctionTests : LoFuTest<QueryFunction>
    {
        [SetUp]
        public void SetUp()
        {
            Clear();
            QueryName = "FakeQuery";
            Use<Mock<IQueryProcessor>>().Setup(x => x.GetQueryType(QueryName)).Returns(typeof(FakeQuery));
            Use<JsonSerializerOptions>(null);
        }

        [LoFu, Test]
        public async Task when_handling_the_query_via_Post()
        {
            Context = new DefaultHttpContext();
            Context.Request.Body = new MemoryStream(Encoding.UTF8.GetBytes("{}"));
            Context.Response.Body = new MemoryStream();

            async Task should_return_the_result_from_the_query_processor()
            {
                Context.Request.Body.Position = 0;
                Context.Response.Clear();
                var expected = new FakeResult();
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Returns(Task.FromResult(expected));

                await Subject.HandleAsync(QueryName, Context);

                Context.Response.StatusCode.Should().Be(200);
                Context.Response.Body.Length.Should().BeGreaterThan(0);
            }

            async Task should_throw_when_request_is_null()
            {
                Func<Task> act = () => Subject.HandleAsync(QueryName, null);
                await act.Should().ThrowAsync<ArgumentNullException>();
            }

            async Task should_handle_QueryProcessorException()
            {
                Context.Request.Body.Position = 0;
                Context.Response.Clear();
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Throws(new QueryProcessorException("fail"));

                await Subject.HandleAsync(QueryName, Context);

                await Context.Response.ShouldBeErrorAsync("fail", 400);
            }

            async Task should_handle_QueryException()
            {
                Context.Request.Body.Position = 0;
                Context.Response.Clear();
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Throws(new QueryException("invalid"));

                await Subject.HandleAsync(QueryName, Context);

                await Context.Response.ShouldBeErrorAsync("invalid", 400);
            }

            async Task should_handle_Exception()
            {
                Context.Request.Body.Position = 0;
                Context.Response.Clear();
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Throws(new Exception("fail"));

                await Subject.HandleAsync(QueryName, Context);

                await Context.Response.ShouldBeErrorAsync("fail", 500);
            }
        }

        [LoFu, Test]
        public async Task when_handling_the_query_via_Get()
        {
            Context = new DefaultHttpContext();
            Context.Request.Method = "GET";
            Context.Request.Query = new QueryCollection(new Dictionary<string, StringValues> { { "foo", new StringValues("bar") } });
            Context.Response.Body = new MemoryStream();

            async Task should_return_the_result_from_the_query_processor()
            {
                Context.Response.Clear();
                var expected = new FakeResult();
                The<Mock<IQueryProcessor>>().Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Returns(Task.FromResult(expected));

                await Subject.HandleAsync(QueryName, Context);

                Context.Response.StatusCode.Should().Be(200);
                Context.Response.Body.Length.Should().BeGreaterThan(0);
            }
        }

        HttpContext Context;
        string QueryName;
    }
}
```

## File: `tests/CommandQuery.GoogleCloudFunctions.Tests/ServiceCollectionExtensionsTests.cs`
```csharp
using CommandQuery.Tests;
using FluentAssertions;
using Microsoft.Extensions.DependencyInjection;

namespace CommandQuery.GoogleCloudFunctions.Tests
{
    public class ServiceCollectionExtensionsTests
    {
        [Test]
        public void when_AddCommandFunction()
        {
            var assembly = typeof(FakeCommandHandler).Assembly;
            var serviceCollection = new ServiceCollection();

            serviceCollection.AddLogging();
            serviceCollection.AddCommandFunction(assembly);
            var provider = serviceCollection.BuildServiceProvider();

            provider.GetService<ICommandFunction>().Should().NotBeNull();
        }

        [Test]
        public void when_AddQueryFunction()
        {
            var assembly = typeof(FakeQueryHandler).Assembly;
            var serviceCollection = new ServiceCollection();

            serviceCollection.AddLogging();
            serviceCollection.AddQueryFunction(assembly);
            var provider = serviceCollection.BuildServiceProvider();

            provider.GetService<IQueryFunction>().Should().NotBeNull();
        }
    }
}
```

## File: `tests/CommandQuery.GoogleCloudFunctions.Tests/ShouldExtensions.cs`
```csharp
using System.Text.Json;
using CommandQuery.Tests;
using FluentAssertions;
using Microsoft.AspNetCore.Http;

namespace CommandQuery.GoogleCloudFunctions.Tests
{
    public static class ShouldExtensions
    {
        public static async Task ShouldBeErrorAsync(this HttpResponse response, string message, int? statusCode = null)
        {
            response.Should().NotBeNull();
            response.StatusCode.Should().NotBe(200);
            if (statusCode.HasValue) response.StatusCode.Should().Be(statusCode);
            response.Body.Seek(0, SeekOrigin.Begin);
            var value = await JsonSerializer.DeserializeAsync<FakeError>(response.Body);
            value.Should().NotBeNull();
            value.Message.Should().Be(message);
        }
    }
}
```

## File: `tests/CommandQuery.GoogleCloudFunctions.Tests/Internal/HttpExtensionsTests.cs`
```csharp
using System.Text;
using CommandQuery.Exceptions;
using FluentAssertions;
using Microsoft.AspNetCore.Http;

namespace CommandQuery.GoogleCloudFunctions.Tests.Internal
{
    public class HttpExtensionsTests
    {
        private HttpRequest Request;
        private HttpResponse Response;

        [SetUp]
        public void SetUp()
        {
            var context = new DefaultHttpContext();
            Request = context.Request;
            Request.Body = new MemoryStream(Encoding.UTF8.GetBytes("{}"));
            Response = context.Response;
            Response.Body = new MemoryStream();
        }

        [Test]
        public async Task ReadAsStringAsync()
        {
            var result = await Request.ReadAsStringAsync();
            result.Should().Be("{}");

            Func<Task> act = () => ((HttpRequest)null).ReadAsStringAsync();
            await act.Should().ThrowAsync<ArgumentNullException>();

            result = await new Mock<HttpRequest>().Object.ReadAsStringAsync();
            result.Should().BeNull();
        }

        [Test]
        public async Task OkAsync()
        {
            await Response.OkAsync(new { Foo = "Bar" }, null, CancellationToken.None);
            Response.StatusCode.Should().Be(200);
            Response.Body.Position = 0;
            var result = await new StreamReader(Response.Body).ReadToEndAsync();
            result.Should().Be("{\"Foo\":\"Bar\"}");
        }

        [Test]
        public async Task BadRequestAsync()
        {
            var exception = new CustomCommandException("fail") { Foo = "Bar" };
            await Response.BadRequestAsync(exception, null, CancellationToken.None);
            Response.StatusCode.Should().Be(400);
            Response.Body.Position = 0;
            var result = await new StreamReader(Response.Body).ReadToEndAsync();
            result.Should().Be("{\"Message\":\"fail\",\"Details\":{\"Foo\":\"Bar\"}}");
        }

        [Test]
        public async Task InternalServerErrorAsync()
        {
            var exception = new CustomCommandException("fail") { Foo = "Bar" };
            await Response.InternalServerErrorAsync(exception, null, CancellationToken.None);
            Response.StatusCode.Should().Be(500);
            Response.Body.Position = 0;
            var result = await new StreamReader(Response.Body).ReadToEndAsync();
            result.Should().Be("{\"Message\":\"fail\",\"Details\":{\"Foo\":\"Bar\"}}");
        }
    }

    public class CustomCommandException : CommandException
    {
        public string Foo { get; set; }

        public CustomCommandException(string message) : base(message)
        {
        }
    }
}
```

## File: `tests/CommandQuery.Tests/.editorconfig`
```
# editorconfig.org

# top-most EditorConfig file
root = false

[*.cs]
dotnet_diagnostic.NUnit1032.severity = none
```

## File: `tests/CommandQuery.Tests/CommandProcessorTests.cs`
```csharp
using CommandQuery.DependencyInjection;
using CommandQuery.Exceptions;
using FluentAssertions;
using Microsoft.Extensions.DependencyInjection;

namespace CommandQuery.Tests
{
    public class CommandProcessorTests
    {
        [LoFu, Test]
        public async Task when_processing_the_command()
        {
            FakeCommandTypeProvider = new Mock<ICommandTypeProvider>();
            FakeServiceProvider = new Mock<IServiceProvider>();
            Subject = new CommandProcessor(FakeCommandTypeProvider.Object, FakeServiceProvider.Object);

            async Task should_invoke_the_correct_command_handler()
            {
                FakeCommand expectedCommand = null;
                var fakeCommandHandler = new FakeCommandHandler { Callback = x => expectedCommand = x };
                FakeServiceProvider.Setup(x => x.GetService(typeof(IEnumerable<ICommandHandler<FakeCommand>>))).Returns(new[] { fakeCommandHandler });

                var command = new FakeCommand();
                await Subject.ProcessAsync(command);

                command.Should().Be(expectedCommand);
            }

            async Task should_throw_exception_if_the_command_is_null()
            {
                Func<Task> act = () => Subject.ProcessAsync(null);
                await act.Should().ThrowAsync<ArgumentNullException>();
            }

            async Task should_throw_exception_if_the_command_handler_is_not_found()
            {
                var command = new Mock<ICommand>().Object;

                Func<Task> act = () => Subject.ProcessAsync(command);
                await act.Should().ThrowAsync<CommandProcessorException>()
                    .WithMessage($"The command handler for '{command}' could not be found.");
            }

            async Task should_throw_exception_if_multiple_command_handlers_are_found()
            {
                var handlerType = typeof(ICommandHandler<FakeMultiCommand1>);
                var enumerableType = typeof(IEnumerable<ICommandHandler<FakeMultiCommand1>>);
                FakeServiceProvider.Setup(x => x.GetService(enumerableType)).Returns(new[] { new Mock<ICommandHandler<FakeMultiCommand1>>().Object, new Mock<ICommandHandler<FakeMultiCommand1>>().Object });

                var command = new FakeMultiCommand1();

                Func<Task> act = () => Subject.ProcessAsync(command);
                await act.Should().ThrowAsync<CommandProcessorException>()
                    .WithMessage($"A single command handler for '{handlerType}' could not be retrieved.");
            }
        }

        [LoFu, Test]
        public async Task when_processing_the_command_with_result()
        {
            FakeCommandTypeProvider = new Mock<ICommandTypeProvider>();
            FakeServiceProvider = new Mock<IServiceProvider>();
            Subject = new CommandProcessor(FakeCommandTypeProvider.Object, FakeServiceProvider.Object);

            async Task should_invoke_the_correct_command_handler_and_return_a_result()
            {
                FakeResultCommand expectedCommand = null;
                var expectedResult = new FakeResult();
                var fakeCommandHandler = new FakeResultCommandHandler
                {
                    Callback = x =>
                    {
                        expectedCommand = x;
                        return expectedResult;
                    }
                };
                FakeServiceProvider.Setup(x => x.GetService(typeof(IEnumerable<ICommandHandler<FakeResultCommand, FakeResult>>))).Returns(new[] { fakeCommandHandler });

                var command = new FakeResultCommand();
                var result = await Subject.ProcessAsync(command);

                command.Should().Be(expectedCommand);
                result.Should().Be(expectedResult);
            }

            async Task should_throw_exception_if_the_command_is_null()
            {
                Func<Task> act = () => Subject.ProcessAsync<object>(null);
                await act.Should().ThrowAsync<ArgumentNullException>();
            }

            async Task should_throw_exception_if_the_command_handler_is_not_found()
            {
                var command = new Mock<ICommand<object>>().Object;

                Func<Task> act = () => Subject.ProcessAsync(command);
                await act.Should().ThrowAsync<CommandProcessorException>()
                    .WithMessage($"The command handler for '{command}' could not be found.");
            }

            async Task should_throw_exception_if_multiple_command_handlers_are_found()
            {
                var handlerType = typeof(ICommandHandler<FakeMultiResultCommand1, FakeResult>);
                var enumerableType = typeof(IEnumerable<ICommandHandler<FakeMultiResultCommand1, FakeResult>>);
                FakeServiceProvider.Setup(x => x.GetService(enumerableType)).Returns(new[] { new Mock<ICommandHandler<FakeMultiResultCommand1, FakeResult>>().Object, new Mock<ICommandHandler<FakeMultiResultCommand1, FakeResult>>().Object });

                var command = new FakeMultiResultCommand1();

                Func<Task> act = () => Subject.ProcessAsync(command);
                await act.Should().ThrowAsync<CommandProcessorException>()
                    .WithMessage($"A single command handler for '{handlerType}' could not be retrieved.");
            }
        }

        [LoFu, Test]
        public void when_get_command_types()
        {
            FakeCommandTypeProvider = new Mock<ICommandTypeProvider>();
            Subject = new CommandProcessor(FakeCommandTypeProvider.Object, null);

            void should_get_all_types_from_the_cache()
            {
                Subject.GetCommandTypes();

                FakeCommandTypeProvider.Verify(x => x.GetCommandTypes());
            }
        }

        [LoFu, Test]
        public void when_get_command_type()
        {
            FakeCommandTypeProvider = new Mock<ICommandTypeProvider>();
            Subject = new CommandProcessor(FakeCommandTypeProvider.Object, null);

            void should_get_the_type_from_the_cache()
            {
                var commandName = "name";

                Subject.GetCommandType(commandName);

                FakeCommandTypeProvider.Verify(x => x.GetCommandType(commandName));
            }
        }

        [Test]
        public void AssertConfigurationIsValid()
        {
            var subject = typeof(FakeCommandHandler).Assembly.GetCommandProcessor();

            subject.Invoking(x => x.AssertConfigurationIsValid())
                .Should().Throw<CommandTypeException>()
                .WithMessage("*The command handler for * is not registered.*")
                .WithMessage("*A single command handler for * could not be retrieved.*")
                .WithMessage("*The command * is not registered.*");

            new CommandProcessor(new CommandTypeProvider(), new ServiceCollection().BuildServiceProvider())
                .AssertConfigurationIsValid().Should().NotBeNull();
        }

        Mock<ICommandTypeProvider> FakeCommandTypeProvider;
        Mock<IServiceProvider> FakeServiceProvider;
        CommandProcessor Subject;
    }

    public class DupeCommandHandler : ICommandHandler<Fail.DupeCommand>
    {
        public async Task HandleAsync(Fail.DupeCommand command, CancellationToken cancellationToken) => throw new NotImplementedException();
    }
}
```

## File: `tests/CommandQuery.Tests/CommandQuery.Tests.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>disable</Nullable>
    <IsPackable>false</IsPackable>
    <IsTestProject>true</IsTestProject>
    <NoWarn>$(NoWarn);CS1998;CS8321;NU1603</NoWarn>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="FluentAssertions" Version="6.12.0" />
    <PackageReference Include="LoFuUnit.AutoMoq" Version="4.0.0-preview.1" />
    <PackageReference Include="LoFuUnit.NUnit" Version="4.0.0-preview.1" />
    <PackageReference Include="Microsoft.CodeCoverage" Version="17.10.0" />
    <PackageReference Include="Microsoft.NET.Test.Sdk" Version="17.10.0" />
    <PackageReference Include="NUnit3TestAdapter" Version="4.5.0">
      <PrivateAssets>all</PrivateAssets>
      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
    </PackageReference>
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\..\src\CommandQuery.Client\CommandQuery.Client.csproj" />
    <ProjectReference Include="..\..\src\CommandQuery.SystemTextJson\CommandQuery.SystemTextJson.csproj" />
    <ProjectReference Include="..\..\src\CommandQuery\CommandQuery.csproj" />
    <ProjectReference Include="..\CommandQuery.Fail\CommandQuery.Fail.csproj" />
  </ItemGroup>

  <ItemGroup>
    <Compile Include="..\..\samples\CommandQuery.Sample.Contracts\Commands\*.cs" LinkBase="Client\Contracts\Commands" />
    <Compile Include="..\..\samples\CommandQuery.Sample.Contracts\Queries\*.cs" LinkBase="Client\Contracts\Queries" />
  </ItemGroup>

</Project>
```

## File: `tests/CommandQuery.Tests/CommandTypeProviderTests.cs`
```csharp
using CommandQuery.Exceptions;
using CommandQuery.Fail;
using FluentAssertions;

namespace CommandQuery.Tests
{
    public class CommandTypeProviderTests
    {
        [Test]
        public void Ctor()
        {
            Action act = () => new CommandTypeProvider(typeof(DupeCommand).Assembly);
            act.Should()
                .Throw<CommandTypeException>()
                .WithMessage("Multiple commands with the same name was found*");
        }

        [LoFu, Test]
        public void GetCommandType()
        {
            Subject = new CommandTypeProvider(typeof(FakeCommand).Assembly);

            void should_return_the_type_of_command_if_the_command_name_is_found() => Subject.GetCommandType("FakeCommand").Should().NotBeNull();

            void should_return_null_if_the_command_name_is_not_found() => Subject.GetCommandType("NotFoundCommand").Should().BeNull();
        }

        [LoFu, Test]
        public void GetCommandTypes()
        {
            Subject = new CommandTypeProvider(typeof(FakeCommand).Assembly);

            void should_return_the_types_of_commands_supported() => Subject.GetCommandTypes().Should().NotBeEmpty();
        }

        CommandTypeProvider Subject;
    }
}
```

## File: `tests/CommandQuery.Tests/Fake.cs`
```csharp
namespace CommandQuery.Tests
{
    public class FakeCommand : ICommand
    {
    }

    public class FakeCommandHandler : ICommandHandler<FakeCommand>
    {
        public Action<FakeCommand> Callback { get; set; }

        public async Task HandleAsync(FakeCommand command, CancellationToken cancellationToken)
        {
            Callback(command);

            await Task.CompletedTask;
        }
    }

    public class FakeResultCommand : ICommand<FakeResult>
    {
    }

    public class FakeResultCommandHandler : ICommandHandler<FakeResultCommand, FakeResult>
    {
        public Func<FakeResultCommand, FakeResult> Callback { get; set; }

        public async Task<FakeResult> HandleAsync(FakeResultCommand command, CancellationToken cancellationToken)
        {
            var result = Callback(command);

            return await Task.FromResult(result);
        }
    }

    public class FakeQuery : IQuery<FakeResult>
    {
    }

    public class FakeResult
    {
    }

    public class FakeQueryHandler : IQueryHandler<FakeQuery, FakeResult>
    {
        public Func<FakeQuery, FakeResult> Callback { get; set; }

        public async Task<FakeResult> HandleAsync(FakeQuery query, CancellationToken cancellationToken)
        {
            var result = Callback(query);

            return await Task.FromResult(result);
        }
    }

    // https://github.com/dotnet/runtime/tree/main/src/libraries/System.Text.Json/src/System/Text/Json/Serialization/Converters/Value
    // https://docs.microsoft.com/en-us/dotnet/standard/serialization/system-text-json-supported-collection-types
    public class FakeComplexQuery : IQuery<IEnumerable<FakeResult>>
    {
        public bool Boolean { get; set; }
        public byte Byte { get; set; }
        public char Char { get; set; }
        public DateOnly DateOnly { get; set; }
        public DateTime DateTime { get; set; }
        public DateTimeOffset DateTimeOffset { get; set; }
        public decimal Decimal { get; set; }
        public double Double { get; set; }
        public DayOfWeek Enum { get; set; }
        public Guid Guid { get; set; }
        public short Int16 { get; set; }
        public int Int32 { get; set; }
        public long Int64 { get; set; }
        public sbyte SByte { get; set; }
        public float Single { get; set; }
        public string String { get; set; }
        public TimeOnly TimeOnly { get; set; }
        public TimeSpan TimeSpan { get; set; }
        public ushort UInt16 { get; set; }
        public uint UInt32 { get; set; }
        public ulong UInt64 { get; set; }
        public Uri Uri { get; set; }
        public Version Version { get; set; }

        public int? Nullable { get; set; }
        public (int, int) Tuple { get; set; }

        public int[] Array { get; set; }
        public IDictionary<int, int> IDictionary { get; set; }
        public IEnumerable<int> IEnumerable { get; set; }
        public IList<int> IList { get; set; }
        public IReadOnlyList<int> IReadOnlyList { get; set; }
    }

    public class FakeComplexQueryHandler : IQueryHandler<FakeComplexQuery, IEnumerable<FakeResult>>
    {
        public async Task<IEnumerable<FakeResult>> HandleAsync(FakeComplexQuery query, CancellationToken cancellationToken)
        {
            return await Task.FromResult(new[] { new FakeResult() });
        }
    }

    public class FakeDateTimeQuery : IQuery<FakeResult>
    {
        public DateTime DateTimeUnspecified { get; set; }
        public DateTime DateTimeUtc { get; set; }
        public DateTime DateTimeLocal { get; set; }
        public DateTime[] DateTimeArray { get; set; }
    }

    public class FakeNestedQuery : IQuery<FakeResult>
    {
        public string Foo { get; set; }

        public FakeNestedChild Child { get; set; }
    }

    public class FakeNestedChild
    {
        public string Foo { get; set; }

        public FakeNestedGrandchild Child { get; set; }
    }

    public class FakeNestedGrandchild
    {
        public string Foo { get; set; }
    }

    public class FakeMultiCommand1 : ICommand { }
    public class FakeMultiCommand2 : ICommand { }
    public class FakeMultiResultCommand1 : ICommand<FakeResult> { }
    public class FakeMultiResultCommand2 : ICommand<FakeResult> { }
    public class FakeMultiQuery1 : IQuery<FakeResult> { }
    public class FakeMultiQuery2 : IQuery<FakeResult> { }
    public class FakeMultiHandler :
        ICommandHandler<FakeMultiCommand1>,
        ICommandHandler<FakeMultiCommand2>,
        ICommandHandler<FakeMultiResultCommand1, FakeResult>,
        ICommandHandler<FakeMultiResultCommand2, FakeResult>,
        IQueryHandler<FakeMultiQuery1, FakeResult>,
        IQueryHandler<FakeMultiQuery2, FakeResult>
    {

        public Task HandleAsync(FakeMultiCommand1 command, CancellationToken cancellationToken)
        {
            throw new NotImplementedException();
        }

        public Task HandleAsync(FakeMultiCommand2 command, CancellationToken cancellationToken)
        {
            throw new NotImplementedException();
        }

        public Task<FakeResult> HandleAsync(FakeMultiResultCommand1 command, CancellationToken cancellationToken)
        {
            throw new NotImplementedException();
        }

        public Task<FakeResult> HandleAsync(FakeMultiResultCommand2 command, CancellationToken cancellationToken)
        {
            throw new NotImplementedException();
        }

        public Task<FakeResult> HandleAsync(FakeMultiQuery1 query, CancellationToken cancellationToken)
        {
            throw new NotImplementedException();
        }

        public Task<FakeResult> HandleAsync(FakeMultiQuery2 query, CancellationToken cancellationToken)
        {
            throw new NotImplementedException();
        }
    }

    public class FakeError : IError
    {
        public string Message { get; set; }

        public Dictionary<string, object> Details { get; set; }
    }

    public class BrokenCommand : ICommand
    {
    }

    public class BrokenCommandHandler : ICommandHandler<BrokenCommand>
    {
        public BrokenCommandHandler(object unknownDependency)
        {
        }

        public async Task HandleAsync(BrokenCommand command, CancellationToken cancellationToken)
        {
            await Task.CompletedTask;
        }
    }

    public class BrokenQuery : IQuery<object>
    {
    }

    public class BrokenQueryHandler : IQueryHandler<BrokenQuery, object>
    {
        public BrokenQueryHandler(object unknownDependency)
        {
        }

        public async Task<object> HandleAsync(BrokenQuery query, CancellationToken cancellationToken)
        {
            return await Task.FromResult(new object());
        }
    }
}
```

## File: `tests/CommandQuery.Tests/QueryProcessorTests.cs`
```csharp
using CommandQuery.DependencyInjection;
using CommandQuery.Exceptions;
using FluentAssertions;
using Microsoft.Extensions.DependencyInjection;

namespace CommandQuery.Tests
{
    public class QueryProcessorTests
    {
        [LoFu, Test]
        public async Task when_processing_the_query()
        {
            FakeQueryTypeProvider = new Mock<IQueryTypeProvider>();
            FakeServiceProvider = new Mock<IServiceProvider>();
            Subject = new QueryProcessor(FakeQueryTypeProvider.Object, FakeServiceProvider.Object);

            async Task should_invoke_the_correct_query_handler_and_return_a_result()
            {
                FakeQuery expectedQuery = null;
                var expectedResult = new FakeResult();
                var fakeQueryHandler = new FakeQueryHandler
                {
                    Callback = x =>
                    {
                        expectedQuery = x;
                        return expectedResult;
                    }
                };
                FakeServiceProvider.Setup(x => x.GetService(typeof(IEnumerable<IQueryHandler<FakeQuery, FakeResult>>))).Returns(new[] { fakeQueryHandler });

                var query = new FakeQuery();
                var result = await Subject.ProcessAsync(query);

                query.Should().Be(expectedQuery);
                result.Should().Be(expectedResult);
            }

            async Task should_throw_exception_if_the_query_is_null()
            {
                Func<Task> act = () => Subject.ProcessAsync<object>(null);
                await act.Should().ThrowAsync<ArgumentNullException>();
            }

            async Task should_throw_exception_if_the_query_handler_is_not_found()
            {
                var query = new Mock<IQuery<FakeResult>>().Object;

                Func<Task> act = () => Subject.ProcessAsync(query);
                await act.Should().ThrowAsync<QueryProcessorException>()
                    .WithMessage($"The query handler for '{query}' could not be found.");
            }

            async Task should_throw_exception_if_multiple_query_handlers_are_found()
            {
                var handlerType = typeof(IQueryHandler<FakeMultiQuery1, FakeResult>);
                var enumerableType = typeof(IEnumerable<IQueryHandler<FakeMultiQuery1, FakeResult>>);
                FakeServiceProvider.Setup(x => x.GetService(enumerableType)).Returns(new[] { new Mock<IQueryHandler<FakeMultiQuery1, FakeResult>>().Object, new Mock<IQueryHandler<FakeMultiQuery1, FakeResult>>().Object });

                var query = new FakeMultiQuery1();

                Func<Task> act = () => Subject.ProcessAsync(query);
                await act.Should().ThrowAsync<QueryProcessorException>()
                    .WithMessage($"A single query handler for '{handlerType}' could not be retrieved.");
            }
        }

        [LoFu, Test]
        public void when_get_query_types()
        {
            FakeQueryTypeProvider = new Mock<IQueryTypeProvider>();
            Subject = new QueryProcessor(FakeQueryTypeProvider.Object, null);

            void should_get_all_types_from_the_cache()
            {
                Subject.GetQueryTypes();

                FakeQueryTypeProvider.Verify(x => x.GetQueryTypes());
            }
        }

        [LoFu, Test]
        public void when_get_query_type()
        {
            FakeQueryTypeProvider = new Mock<IQueryTypeProvider>();
            Subject = new QueryProcessor(FakeQueryTypeProvider.Object, null);

            void should_get_the_type_from_the_cache()
            {
                var queryName = "name";

                Subject.GetQueryType(queryName);

                FakeQueryTypeProvider.Verify(x => x.GetQueryType(queryName));
            }
        }

        [Test]
        public void AssertConfigurationIsValid()
        {
            var subject = typeof(FakeQueryHandler).Assembly.GetQueryProcessor();

            subject.Invoking(x => x.AssertConfigurationIsValid())
                .Should().Throw<QueryTypeException>()
                .WithMessage("*The query handler for * is not registered.*")
                .WithMessage("*A single query handler for * could not be retrieved.*")
                .WithMessage("*The query * is not registered.*");

            new QueryProcessor(new QueryTypeProvider(), new ServiceCollection().BuildServiceProvider())
                .AssertConfigurationIsValid().Should().NotBeNull();
        }

        Mock<IQueryTypeProvider> FakeQueryTypeProvider;
        Mock<IServiceProvider> FakeServiceProvider;
        QueryProcessor Subject;
    }

    public class DupeQueryHandler : IQueryHandler<Fail.DupeQuery, object>
    {
        public async Task<object> HandleAsync(Fail.DupeQuery query, CancellationToken cancellationToken) => throw new NotImplementedException();
    }
}
```

## File: `tests/CommandQuery.Tests/QueryTypeProviderTests.cs`
```csharp
using CommandQuery.Exceptions;
using CommandQuery.Fail;
using FluentAssertions;

namespace CommandQuery.Tests
{
    public class QueryTypeProviderTests
    {
        [Test]
        public void Ctor()
        {
            Action act = () => new QueryTypeProvider(typeof(DupeQuery).Assembly);
            act.Should()
                .Throw<QueryTypeException>()
                .WithMessage("Multiple queries with the same name was found*");
        }

        [LoFu, Test]
        public void GetQueryType()
        {
            Subject = new QueryTypeProvider(typeof(FakeQuery).Assembly);

            void should_return_the_type_of_query_if_the_query_name_is_found() => Subject.GetQueryType("FakeQuery").Should().NotBeNull();

            void should_return_null_if_the_query_name_is_not_found() => Subject.GetQueryType("NotFoundQuery").Should().BeNull();
        }

        [LoFu, Test]
        public void GetQueryTypes()
        {
            Subject = new QueryTypeProvider(typeof(FakeQuery).Assembly);

            void should_return_the_types_of_queries_supported() => Subject.GetQueryTypes().Should().NotBeEmpty();
        }

        QueryTypeProvider Subject;
    }
}
```

## File: `tests/CommandQuery.Tests/TestData.cs`
```csharp
namespace CommandQuery.Tests
{
    public static class TestData
    {
        public static readonly FakeComplexQuery FakeComplexQuery = new()
        {
            Boolean = true,
            Byte = 1,
            Char = 'C',
            DateOnly = DateOnly.Parse("2021-07-09"),
            DateTime = DateTime.Parse("2021-07-09T18:37:53.2473503"),
            DateTimeOffset = DateTimeOffset.Parse("2021-07-09T20:39:07.8226113+02:00"),
            Decimal = 2.1M,
            Double = 3.1,
            Enum = DayOfWeek.Friday,
            Guid = Guid.Parse("F8FE9091-DFFD-4E33-8017-221554FE242F"),
            Int16 = 4,
            Int32 = 5,
            Int64 = 6L,
            SByte = 7,
            Single = 8.1f,
            String = "String",
            TimeOnly = TimeOnly.Parse("18:37:53.2473503"),
            TimeSpan = TimeSpan.Parse("1.02:03:04"),
            UInt16 = 9,
            UInt32 = 10U,
            UInt64 = 11UL,
            Uri = new Uri("https://github.com/hlaueriksson/CommandQuery"),
            Version = Version.Parse("1.2.3.4"),

            Nullable = 12,
            //Tuple = (13, 14),

            Array = new[] { 15, 16 },
            //IDictionary = new Dictionary<int, int>() { { 17, 18 } },
            IEnumerable = new[] { 19, 20 },
            IList = new[] { 21, 22 },
            IReadOnlyList = new[] { 23, 24 },
        };

        public static readonly Dictionary<string, object> FakeComplexQuery_As_Dictionary_Of_String_Object = new()
        {
            { "Boolean", "true" },
            { "Byte", "1" },
            { "Char", "C" },
            { "DateOnly", "2021-07-09" },
            { "DateTime", "2021-07-09T18:37:53.2473503" },
            { "DateTimeOffset", "2021-07-09T20:39:07.8226113+02:00" },
            { "Decimal", "2.1" },
            { "Double", "3.1" },
            { "Enum", "Friday" },
            { "Guid", "F8FE9091-DFFD-4E33-8017-221554FE242F" },
            { "Int16", "4" },
            { "Int32", "5" },
            { "Int64", "6" },
            { "SByte", "7" },
            { "Single", "8.1" },
            { "String", "String" },
            { "TimeOnly", "18:37:53.2473503" },
            { "TimeSpan", "1.02:03:04" },
            { "UInt16", "9" },
            { "UInt32", "10" },
            { "UInt64", "11" },
            { "Uri", "https://github.com/hlaueriksson/CommandQuery" },
            { "Version", "1.2.3.4" },

            { "Nullable", "12" },
            //{ "Tuple", (13, 14) },

            { "Array", new[] { "15", "16" } },
            //{ "IDictionary", new Dictionary<int, int> { { 17, 18 } } },
            { "IEnumerable", new[] { "19", "20" } },
            { "IList", new[] { "21", "22" } },
            { "IReadOnlyList", new[] { "23", "24" } },

            { "UndefinedProperty", "should_not_be_used" },
        };

        public static readonly Dictionary<string, IEnumerable<string>> FakeComplexQuery_As_Dictionary_Of_String_IEnumerable_String = new()
        {
            { "Boolean", new[] { "true" } },
            { "Byte", new[] { "1" } },
            { "Char", new[] { "C" } },
            { "DateOnly", new[] { "2021-07-09" } },
            { "DateTime", new[] { "2021-07-09T18:37:53.2473503" } },
            { "DateTimeOffset", new[] { "2021-07-09T20:39:07.8226113+02:00" } },
            { "Decimal", new[] { "2.1" } },
            { "Double", new[] { "3.1" } },
            { "Enum", new[] { "Friday" } },
            { "Guid", new[] { "F8FE9091-DFFD-4E33-8017-221554FE242F" } },
            { "Int16", new[] { "4" } },
            { "Int32", new[] { "5" } },
            { "Int64", new[] { "6" } },
            { "SByte", new[] { "7" } },
            { "Single", new[] { "8.1" } },
            { "String", new[] { "String" } },
            { "TimeOnly", new[] { "18:37:53.2473503" } },
            { "TimeSpan", new[] { "1.02:03:04" } },
            { "UInt16", new[] { "9" } },
            { "UInt32", new[] { "10" } },
            { "UInt64", new[] { "11" } },
            { "Uri", new[] { "https://github.com/hlaueriksson/CommandQuery" } },
            { "Version", new[] { "1.2.3.4" } },

            { "Nullable", new[] { "12" } },
            //{ "Tuple", new[] { "13", "14" } },

            { "Array", new[] { "15", "16" } },
            //{ "IDictionary", new[] { "{\"17\": 18}" } },
            { "IEnumerable", new[] { "19", "20" } },
            { "IList", new[] { "21", "22" } },
            { "IReadOnlyList", new[] { "23", "24" } },

            { "UndefinedProperty", new[] { "should_not_be_used" } },
        };

        public static readonly FakeDateTimeQuery FakeDateTimeQuery = new()
        {
            DateTimeUnspecified = new DateTime(2021, 7, 10, 9, 48, 41, DateTimeKind.Unspecified),
            DateTimeUtc = new DateTime(2021, 7, 10, 9, 48, 41, DateTimeKind.Utc),
            //DateTimeLocal = new DateTime(2021, 7, 10, 9, 48, 41, DateTimeKind.Local),
            DateTimeArray =
            [
                new DateTime(2021, 7, 10, 9, 48, 41, DateTimeKind.Unspecified),
                new DateTime(2021, 7, 10, 9, 48, 41, DateTimeKind.Utc),
                //new DateTime(2021, 7, 10, 9, 48, 41, DateTimeKind.Local),
            ]
        };

        public static readonly Dictionary<string, object> FakeDateTimeQuery_As_Dictionary_Of_String_Object = new()
        {
            { "DateTimeUnspecified", "2021-07-10T09:48:41.0000000" },
            { "DateTimeUtc", "2021-07-10T09:48:41.0000000Z" },
            //{ "DateTimeLocal", "2021-07-10T09:48:41.0000000+02:00" },
            { "DateTimeArray", new[] { "2021-07-10T09:48:41.0000000", "2021-07-10T09:48:41.0000000Z", /*"2021-07-10T09:48:41.0000000+02:00"*/ } },
        };

        public static readonly Dictionary<string, IEnumerable<string>> FakeDateTimeQuery_As_Dictionary_Of_String_IEnumerable_String = new()
        {
            { "DateTimeUnspecified", new[] { "2021-07-10T09:48:41.0000000" } },
            { "DateTimeUtc", new[] { "2021-07-10T09:48:41.0000000Z" } },
            //{ "DateTimeLocal", new[] { "2021-07-10T09:48:41.0000000+02:00" } },
            { "DateTimeArray", new[] { "2021-07-10T09:48:41.0000000", "2021-07-10T09:48:41.0000000Z", /*"2021-07-10T09:48:41.0000000+02:00"*/ } },
        };

        public static readonly FakeNestedQuery FakeNestedQuery = new()
        {
            Foo = "Bar",
            Child = new FakeNestedChild
            {
                Foo = "Bar",
                Child = new FakeNestedGrandchild
                {
                    Foo = "Bar"
                }
            }
        };

        public static readonly Dictionary<string, object> FakeNestedQuery_As_Dictionary_Of_String_Object = new()
        {
            { "Foo", "Bar" },
            { "Child", new Dictionary<string, object>
                {
                    { "Foo", "Bar" },
                    { "Child", new Dictionary<string, object>
                        {
                            { "Foo", "Bar" }
                        }
                    }
                }
            }
        };

        public static readonly Dictionary<string, IEnumerable<string>> FakeNestedQuery_As_Dictionary_Of_String_IEnumerable_String = new()
        {
            { "Foo", new[] { "Bar" } },
            { "Child.Foo", new[] { "Bar" } },
            { "Child.Child.Foo", new[] { "Bar" } },
        };
    }
}
```

## File: `tests/CommandQuery.Tests/Client/CommandClientTests.cs`
```csharp
using System.Text;
using System.Text.Json;
using CommandQuery.Client;
using CommandQuery.Sample.Contracts.Commands;
using FluentAssertions;
using Moq.Protected;

namespace CommandQuery.Tests.Client
{
    public class CommandClientTests
    {
        [SetUp]
        public void SetUp()
        {
            MockHandler = new Mock<HttpMessageHandler>();
            var client = new HttpClient(MockHandler.Object) { BaseAddress = new Uri("https://localhost") };
            Subject = new CommandClient(client);
        }

        [Test]
        public void Ctor()
        {
            new CommandClient("https://example.com", 20).Should().NotBeNull();
            new CommandClient("https://example.com", x => x.Timeout = TimeSpan.FromSeconds(20)).Should().NotBeNull();

            Action act = () => new CommandClient("https://example.com", null);
            act.Should().Throw<ArgumentNullException>();
        }

        [Test]
        public async Task PostAsync()
        {
            var command = new FooCommand { Value = "sv-SE" };

            var httpResponse = new HttpResponseMessage
            {
                StatusCode = System.Net.HttpStatusCode.OK
            };

            MockHandler.Protected().Setup<Task<HttpResponseMessage>>("SendAsync",
                    ItExpr.Is<HttpRequestMessage>(r => r.Method == HttpMethod.Post && r.RequestUri.ToString().Contains(command.GetType().Name)),
                    ItExpr.IsAny<CancellationToken>())
                .ReturnsAsync(httpResponse);

            await Subject.PostAsync(command);
        }

        [Test]
        public async Task PostAsync_with_result()
        {
            var expectation = new Baz { Success = true };
            var command = new BazCommand { Value = "sv-SE" };

            var httpResponse = new HttpResponseMessage
            {
                StatusCode = System.Net.HttpStatusCode.OK,
                Content = new StringContent(JsonSerializer.Serialize(expectation), Encoding.UTF8, "application/json")
            };

            MockHandler.Protected().Setup<Task<HttpResponseMessage>>("SendAsync",
                    ItExpr.Is<HttpRequestMessage>(r => r.Method == HttpMethod.Post && r.RequestUri.ToString().Contains(command.GetType().Name)),
                    ItExpr.IsAny<CancellationToken>())
                .ReturnsAsync(httpResponse);

            var result = await Subject.PostAsync(command);
            result.Should().BeEquivalentTo(expectation);
        }

        CommandClient Subject;
        Mock<HttpMessageHandler> MockHandler;
    }
}
```

## File: `tests/CommandQuery.Tests/Client/QueryClientTests.cs`
```csharp
using System.Text;
using System.Text.Json;
using CommandQuery.Client;
using CommandQuery.Sample.Contracts.Queries;
using FluentAssertions;
using Moq.Protected;

namespace CommandQuery.Tests.Client
{
    public class QueryClientTests
    {
        [SetUp]
        public void SetUp()
        {
            MockHandler = new Mock<HttpMessageHandler>();
            var client = new HttpClient(MockHandler.Object) { BaseAddress = new Uri("https://localhost") };
            Subject = new QueryClient(client);
        }

        [Test]
        public void Ctor()
        {
            new QueryClient("https://example.com", 20).Should().NotBeNull();
            new QueryClient("https://example.com", x => x.Timeout = TimeSpan.FromSeconds(20)).Should().NotBeNull();

            Action act = () => new QueryClient("https://example.com", null);
            act.Should().Throw<ArgumentNullException>();
        }

        [Test]
        public async Task PostAsync()
        {
            var expectation = new Bar { Id = 1, Value = "Value" };
            var query = new BarQuery { Id = 1 };

            var httpResponse = new HttpResponseMessage
            {
                StatusCode = System.Net.HttpStatusCode.OK,
                Content = new StringContent(JsonSerializer.Serialize(expectation), Encoding.UTF8, "application/json")
            };

            MockHandler.Protected().Setup<Task<HttpResponseMessage>>("SendAsync",
                    ItExpr.Is<HttpRequestMessage>(r => r.Method == HttpMethod.Post && r.RequestUri.ToString().Contains(query.GetType().Name)),
                    ItExpr.IsAny<CancellationToken>())
                .ReturnsAsync(httpResponse);

            var result = await Subject.PostAsync(query);
            result.Should().BeEquivalentTo(expectation);
        }

        [Test]
        public async Task GetAsync()
        {
            var expectation = new Bar { Id = 1, Value = "Value" };
            var query = new BarQuery { Id = 1 };

            var httpResponse = new HttpResponseMessage
            {
                StatusCode = System.Net.HttpStatusCode.OK,
                Content = new StringContent(JsonSerializer.Serialize(expectation), Encoding.UTF8, "application/json")
            };

            MockHandler.Protected().Setup<Task<HttpResponseMessage>>("SendAsync",
                    ItExpr.Is<HttpRequestMessage>(r => r.Method == HttpMethod.Get && r.RequestUri.ToString().Contains(query.GetType().Name)),
                    ItExpr.IsAny<CancellationToken>())
                .ReturnsAsync(httpResponse);

            var result = await Subject.GetAsync(query);
            result.Should().BeEquivalentTo(expectation);
        }

        QueryClient Subject;
        Mock<HttpMessageHandler> MockHandler;
    }
}
```

## File: `tests/CommandQuery.Tests/Client/Integration/CommandClientIntegrationTests.cs`
```csharp
using CommandQuery.Client;
using CommandQuery.Sample.Contracts.Commands;
using FluentAssertions;

namespace CommandQuery.Tests.Client.Integration
{
    [Explicit("Integration tests")]
    public class CommandClientIntegrationTests
    {
        [SetUp]
        public void SetUp()
        {
            Subject = new CommandClient("https://commandquery-sample-azurefunctions-vs3.azurewebsites.net/api/command/");
        }

        [Test]
        public async Task when_PostAsync()
        {
            await Subject.PostAsync(new FooCommand { Value = "sv-SE" });

            Func<Task> act = () => Subject.PostAsync(new FooCommand());
            (await act.Should().ThrowAsync<CommandQueryException>())
                .And.Error.GetErrorCode().Should().Be(1337);

            act = () => Subject.PostAsync(new FailCommand());
            await act.Should().ThrowAsync<CommandQueryException>();
        }

        [Test]
        public async Task when_PostAsync_with_result()
        {
            var result = await Subject.PostAsync(new BazCommand { Value = "sv-SE" });
            result.Should().NotBeNull();

            Func<Task> act = () => Subject.PostAsync(new FailResultCommand());
            await act.Should().ThrowAsync<CommandQueryException>();
        }

        [Test]
        public async Task when_configuring_the_client()
        {
            var client = new CommandClient("http://example.com", x => x.BaseAddress = new Uri("https://commandquery-sample-azurefunctions-vs2.azurewebsites.net/api/command/"));
            await client.PostAsync(new FooCommand { Value = "sv-SE" });
        }

        CommandClient Subject;
    }

    public class FailCommand : ICommand { }
    public class FailResultCommand : ICommand<object> { }

    public static class FooCommandExceptionExtensions
    {
        public static long? GetErrorCode(this IError error)
        {
            return error?.Details?["ErrorCode"] as long?;
        }
    }
}
```

## File: `tests/CommandQuery.Tests/Client/Integration/QueryClientIntegrationTests.cs`
```csharp
using CommandQuery.Client;
using CommandQuery.Sample.Contracts.Queries;
using FluentAssertions;

namespace CommandQuery.Tests.Client.Integration
{
    [Explicit("Integration tests")]
    public class QueryClientIntegrationTests
    {
        [SetUp]
        public void SetUp()
        {
            Subject = new QueryClient("https://commandquery-sample-azurefunctions-vs3.azurewebsites.net/api/query/");
        }

        [Test]
        public async Task when_PostAsync()
        {
            var result = await Subject.PostAsync(new BarQuery { Id = 1 });
            result.Should().NotBeNull();

            Func<Task> act = () => Subject.PostAsync(new FailQuery());
            await act.Should().ThrowAsync<CommandQueryException>();
        }

        [Test]
        public async Task when_GetAsync()
        {
            var result = await Subject.GetAsync(new QuxQuery { Ids = [Guid.NewGuid(), Guid.NewGuid()] });
            result.Should().NotBeNull();

            Func<Task> act = () => Subject.GetAsync(new FailQuery());
            await act.Should().ThrowAsync<CommandQueryException>();
        }

        [Test]
        public async Task when_configuring_the_client()
        {
            var client = new QueryClient("http://example.com", x => x.BaseAddress = new Uri("https://commandquery-sample-azurefunctions-vs2.azurewebsites.net/api/query/"));
            await client.PostAsync(new BarQuery { Id = 1 });
        }

        QueryClient Subject;
    }

    public class FailQuery : IQuery<object> { }
}
```

## File: `tests/CommandQuery.Tests/Client/Internal/DictionaryStringObjectConverterTests.cs`
```csharp
using System.Text;
using System.Text.Json;
using CommandQuery.Client;
using FluentAssertions;

namespace CommandQuery.Tests.Client.Internal
{
    public class DictionaryStringObjectConverterTests
    {
        [Test]
        public async Task Read()
        {
            var options = new JsonSerializerOptions
            {
                Converters = { new DictionaryStringObjectConverter() }
            };

            var stream = new MemoryStream(Encoding.UTF8.GetBytes("{}"));
            var result = await JsonSerializer.DeserializeAsync<Dictionary<string, object>>(stream, options, CancellationToken.None);
            result.Should().BeEmpty();

            stream = new MemoryStream(Encoding.UTF8.GetBytes("{\"BooleanTrue\":true,\"BooleanFalse\":false,\"Byte\":1,\"Char\":\"C\",\"DateTime\":\"2021-07-09T18:37:53.2473503\",\"DateTimeOffset\":\"2021-07-09T20:39:07.8226113+02:00\",\"Decimal\":2.1,\"Double\":3.1,\"Enum\":5,\"Guid\":\"f8fe9091-dffd-4e33-8017-221554fe242f\",\"Int16\":4,\"Int32\":5,\"Int64\":6,\"SByte\":7,\"Single\":8.1,\"String\":\"String\",\"UInt16\":9,\"UInt32\":10,\"UInt64\":11,\"Uri\":\"https://github.com/hlaueriksson/CommandQuery\",\"Null\":null,\"Array\":[1,2,3],\"Dictionary\":{\"Array\":[1,2,3]}}"));
            result = await JsonSerializer.DeserializeAsync<Dictionary<string, object>>(stream, options, CancellationToken.None);
            result.Should().BeEquivalentTo(
                new Dictionary<string, object>
                {
                    { "BooleanTrue", true },
                    { "BooleanFalse", false },
                    { "Byte", (byte)1 },
                    { "Char", "C" },
                    { "DateTime", DateTime.Parse("2021-07-09T18:37:53.2473503") },
                    { "DateTimeOffset", DateTime.Parse("2021-07-09T20:39:07.8226113+02:00") },
                    { "Decimal", 2.1M },
                    { "Double", 3.1 },
                    { "Enum", (int)DayOfWeek.Friday },
                    { "Guid", Guid.Parse("F8FE9091-DFFD-4E33-8017-221554FE242F") },
                    { "Int16", (short)4 },
                    { "Int32", 5 },
                    { "Int64", 6L },
                    { "SByte", (sbyte)7 },
                    { "Single", 8.1f },
                    { "String", "String" },
                    //{ "TimeSpan", TimeSpan.Parse("1:02:03:04") },
                    { "UInt16", (ushort)9 },
                    { "UInt32", 10U },
                    { "UInt64", 11UL },
                    { "Uri", "https://github.com/hlaueriksson/CommandQuery" },
                    //{ "Version", new Version("1.2.3.4") },
                    { "Null", null },
                    { "Array", new[] { 1, 2, 3 } },
                    {
                        "Dictionary",
                        new Dictionary<string, object>
                        {
                            { "Array", new[] { 1, 2, 3 } }
                        }
                    }
                });
        }

        [Test]
        public void Write()
        {
            var options = new JsonSerializerOptions
            {
                Converters = { new DictionaryStringObjectConverter() }
            };

            var dict = new Dictionary<string, object>();
            var result = JsonSerializer.Serialize(dict, options);
            result.Should().Be("{}");

            dict = new Dictionary<string, object>
            {
                { "BooleanTrue", true },
                { "BooleanFalse", false },
                { "Byte", (byte)1 },
                { "Char", 'C' },
                { "DateTime", DateTime.Parse("2021-07-09T18:37:53.2473503") },
                { "DateTimeOffset", DateTimeOffset.Parse("2021-07-09T20:39:07.8226113+02:00") },
                { "Decimal", 2.1M },
                { "Double", 3.1 },
                { "Enum", DayOfWeek.Friday },
                { "Guid", Guid.Parse("F8FE9091-DFFD-4E33-8017-221554FE242F") },
                { "Int16", (short)4 },
                { "Int32", 5 },
                { "Int64", 6L },
                { "SByte", (sbyte)7 },
                { "Single", 8.1f },
                { "String", "String" },
                //{ "TimeSpan", TimeSpan.Parse("1:02:03:04") },
                { "UInt16", (ushort)9 },
                { "UInt32", 10U },
                { "UInt64", 11UL },
                { "Uri", "https://github.com/hlaueriksson/CommandQuery" },
                //{ "Version", new Version("1.2.3.4") },
                { "Null", null },
                { "Array", new[] { 1, 2, 3 } },
                {
                    "Dictionary",
                    new Dictionary<string, object>
                    {
                        { "Array", new[] { 1, 2, 3 } }
                    }
                }
            };
            result = JsonSerializer.Serialize(dict, options);
            result.Should().Be("{\"BooleanTrue\":true,\"BooleanFalse\":false,\"Byte\":1,\"Char\":\"C\",\"DateTime\":\"2021-07-09T18:37:53.2473503\",\"DateTimeOffset\":\"2021-07-09T20:39:07.8226113+02:00\",\"Decimal\":2.1,\"Double\":3.1,\"Enum\":5,\"Guid\":\"f8fe9091-dffd-4e33-8017-221554fe242f\",\"Int16\":4,\"Int32\":5,\"Int64\":6,\"SByte\":7,\"Single\":8.1,\"String\":\"String\",\"UInt16\":9,\"UInt32\":10,\"UInt64\":11,\"Uri\":\"https://github.com/hlaueriksson/CommandQuery\",\"Null\":null,\"Array\":[1,2,3],\"Dictionary\":{\"Array\":[1,2,3]}}");
        }
    }
}
```

## File: `tests/CommandQuery.Tests/Client/Internal/ExceptionExtensionsTests.cs`
```csharp
using System.Net;
using System.Text;
using System.Text.Json;
using CommandQuery.Client;
using FluentAssertions;

namespace CommandQuery.Tests.Client.Internal
{
    public class HttpResponseMessageExtensionsTests
    {
        [Test]
        public async Task EnsureSuccessStatusCode()
        {
            (await new HttpResponseMessage(HttpStatusCode.OK).EnsureSuccessAsync(CancellationToken.None)).Should().NotBeNull();

            var error = new Error("fail", new Dictionary<string, object> { { "foo", "bar" } });

            var subject = new HttpResponseMessage
            {
                StatusCode = HttpStatusCode.BadRequest,
                Content = new StringContent(JsonSerializer.Serialize(error), Encoding.UTF8, "application/json")
            };

            Func<Task> act = () => subject.EnsureSuccessAsync(CancellationToken.None);
            (await act.Should().ThrowAsync<CommandQueryException>())
                .WithMessage("StatusCode: 400, ReasonPhrase: 'Bad Request'*")
                .And.Error.Should().BeEquivalentTo(error);
        }
    }
}
```

## File: `tests/CommandQuery.Tests/Client/Internal/HttpClientExtensionsTests.cs`
```csharp
using CommandQuery.Client;
using FluentAssertions;

namespace CommandQuery.Tests.Client.Internal
{
    public class HttpClientExtensionsTests
    {
        [Test]
        public void SetDefaultRequestHeaders()
        {
            var client = new HttpClient();
            client.SetDefaultRequestHeaders();
            client.DefaultRequestHeaders.Accept.Single().MediaType.Should().Be("application/json");
            client.DefaultRequestHeaders.UserAgent.Single().Product.Name.Should().StartWith("CommandQuery.Client");

            Action act = () => ((HttpClient)null).SetDefaultRequestHeaders();
            act.Should().Throw<ArgumentNullException>();
        }
    }
}
```

## File: `tests/CommandQuery.Tests/Client/Internal/QueryExtensionsTests.cs`
```csharp
using CommandQuery.Client;
using FluentAssertions;

namespace CommandQuery.Tests.Client.Internal
{
    public class QueryExtensionsTests
    {
        [Test]
        public void GetRequestUri_with_complex_query()
        {
            var result = TestData.FakeComplexQuery.GetRequestUri();
            result.Should()
                .StartWith("FakeComplexQuery?").And

                .Contain("Boolean=True").And
                .Contain("Byte=1").And
                .Contain("Char=C").And
                .Contain("DateOnly=07%2F09%2F2021").And
                .Contain("DateTime=2021-07-09T18%3A37%3A53.2473503").And
                .Contain("DateTimeOffset=2021-07-09T20%3A39%3A07.8226113%2B02%3A00").And
                .Contain("Decimal=2.1").And
                .Contain("Double=3.1").And
                .Contain("Enum=Friday").And
                .Contain("Guid=f8fe9091-dffd-4e33-8017-221554fe242f").And
                .Contain("Int16=4").And
                .Contain("Int32=5").And
                .Contain("Int64=6").And
                .Contain("SByte=7").And
                .Contain("Single=8").And
                .Contain("String=String").And
                .Contain("TimeOnly=18%3A37").And
                .Contain("TimeSpan=1.02%3A03%3A04").And
                .Contain("UInt16=9").And
                .Contain("UInt32=10").And
                .Contain("UInt64=11").And
                .Contain("Uri=https%3A%2F%2Fgithub.com%2Fhlaueriksson%2FCommandQuery").And
                .Contain("Version=1.2.3.4").And

                .Contain("Nullable=12").And
                //.Contain("Tuple=(13,14)").And

                .Contain("Array=15&Array=16").And
                //.Contain("IDictionary=17:18").And
                .Contain("IEnumerable=19&IEnumerable=20").And
                .Contain("IList=21&IList=22").And
                .Contain("IReadOnlyList=23&IReadOnlyList=24");

            Action act = () => ((object)null).GetRequestUri();
            act.Should().Throw<ArgumentNullException>();
        }

        [Test]
        public void GetRequestUri_with_datetime_query()
        {
            var result = TestData.FakeDateTimeQuery.GetRequestUri();
            result.Should()
                .Contain("DateTimeUnspecified=2021-07-10T09%3A48%3A41.0000000").And
                .Contain("DateTimeUtc=2021-07-10T09%3A48%3A41.0000000Z").And
                //.Contain("DateTimeLocal=2021-07-10T09%3A48%3A41.0000000%2B02%3A00").And
                .Contain("DateTimeArray=2021-07-10T09%3A48%3A41.0000000&DateTimeArray=2021-07-10T09%3A48%3A41.0000000Z"/*&DateTimeArray=2021-07-10T09%3A48%3A41.0000000%2B02%3A00"*/);

            Action act = () => ((object)null).GetRequestUri();
            act.Should().Throw<ArgumentNullException>();
        }

        [Test]
        public void GetRequestUri_with_nested_query()
        {
            var result = TestData.FakeNestedQuery.GetRequestUri();
            result.Should().Be("FakeNestedQuery?Foo=Bar&Child.Foo=Bar&Child.Child.Foo=Bar");
        }

        [Test]
        public void GetRequestSlug()
        {
            new FakeComplexQuery().GetRequestSlug().Should().Be("FakeComplexQuery");

            Action act = () => ((object)null).GetRequestSlug();
            act.Should().Throw<ArgumentNullException>();
        }
    }
}
```

## File: `tests/CommandQuery.Tests/DependencyInjection/CommandExtensionsTests.cs`
```csharp
using System.Reflection;
using CommandQuery.DependencyInjection;
using FluentAssertions;
using Microsoft.Extensions.DependencyInjection;

namespace CommandQuery.Tests.DependencyInjection
{
    public class CommandExtensionsTests
    {
        [LoFu, Test]
        public void when_GetCommandProcessor()
        {
            Assembly = typeof(FakeCommandHandler).Assembly;

            void should_add_commands_from_Assembly()
            {
                var result = Assembly.GetCommandProcessor();

                result.Should().NotBeNull();
                result.GetCommandTypes().Should().Contain(typeof(FakeCommand));
                result.GetCommandTypes().Should().Contain(typeof(FakeResultCommand));
            }

            void should_add_commands_from_Assemblies()
            {
                var result = new[] { Assembly }.GetCommandProcessor();

                result.Should().NotBeNull();
                result.GetCommandTypes().Should().Contain(typeof(FakeCommand));
                result.GetCommandTypes().Should().Contain(typeof(FakeResultCommand));
            }

            void should_add_commands_to_the_given_ServiceCollection()
            {
                Assembly.GetCommandProcessor(new ServiceCollection()).Should().NotBeNull();
                new[] { Assembly }.GetCommandProcessor(new ServiceCollection()).Should().NotBeNull();
                new ServiceCollection().GetCommandProcessor(Assembly).Should().NotBeNull();
            }
        }

        Assembly Assembly;
    }
}
```

## File: `tests/CommandQuery.Tests/DependencyInjection/QueryExtensionsTests.cs`
```csharp
using System.Reflection;
using CommandQuery.DependencyInjection;
using FluentAssertions;
using Microsoft.Extensions.DependencyInjection;

namespace CommandQuery.Tests.DependencyInjection
{
    public class QueryExtensionsTests
    {
        [LoFu, Test]
        public void when_GetQueryProcessor()
        {
            Assembly = typeof(FakeQueryHandler).Assembly;

            void should_add_queries_from_Assembly()
            {
                var result = Assembly.GetQueryProcessor();

                result.Should().NotBeNull();
                result.GetQueryTypes().Should().Contain(typeof(FakeQuery));
            }

            void should_add_queries_from_Assemblies()
            {
                var result = new[] { Assembly }.GetQueryProcessor();

                result.Should().NotBeNull();
                result.GetQueryTypes().Should().Contain(typeof(FakeQuery));
            }

            void should_add_queries_to_the_given_ServiceCollection()
            {
                Assembly.GetQueryProcessor(new ServiceCollection()).Should().NotBeNull();
                new[] { Assembly }.GetQueryProcessor(new ServiceCollection()).Should().NotBeNull();
                new ServiceCollection().GetQueryProcessor(Assembly).Should().NotBeNull();
            }
        }

        Assembly Assembly;
    }
}
```

## File: `tests/CommandQuery.Tests/DependencyInjection/ServiceCollectionExtensionsTests.cs`
```csharp
using System.Reflection;
using CommandQuery.DependencyInjection;
using FluentAssertions;
using Microsoft.Extensions.DependencyInjection;

namespace CommandQuery.Tests.DependencyInjection
{
    public class ServiceCollectionExtensionsTests
    {
        [LoFu, Test]
        public void when_AddCommands()
        {
            Assembly = typeof(FakeCommandHandler).Assembly;

            void should_add_commands_from_Assemblies()
            {
                var serviceCollection = new ServiceCollection();
                serviceCollection.AddCommands(Assembly);
                var provider = serviceCollection.BuildServiceProvider();

                provider.GetService<ICommandHandler<FakeCommand>>().Should().BeOfType<FakeCommandHandler>();
                provider.GetService<ICommandHandler<FakeResultCommand, FakeResult>>().Should().BeOfType<FakeResultCommandHandler>();
            }

            void should_create_a_CommandTypeProvider()
            {
                var serviceCollection = new ServiceCollection();
                serviceCollection.AddCommands(Assembly);
                var provider = serviceCollection.BuildServiceProvider();

                provider.GetService(typeof(ICommandTypeProvider)).Should().NotBeNull();
            }

            void should_add_all_commands_from_handler()
            {
                var serviceCollection = new ServiceCollection();
                serviceCollection.AddCommands(Assembly);
                var provider = serviceCollection.BuildServiceProvider();

                provider.GetService<ICommandHandler<FakeMultiCommand1>>().Should().BeOfType<FakeMultiHandler>();
                provider.GetService<ICommandHandler<FakeMultiCommand2>>().Should().BeOfType<FakeMultiHandler>();
                provider.GetService<ICommandHandler<FakeMultiResultCommand1, FakeResult>>().Should().BeOfType<FakeMultiHandler>();
                provider.GetService<ICommandHandler<FakeMultiResultCommand2, FakeResult>>().Should().BeOfType<FakeMultiHandler>();
            }
        }

        [LoFu, Test]
        public void when_AddQueries()
        {
            Assembly = typeof(FakeQueryHandler).Assembly;

            void should_add_queries_from_Assemblies()
            {
                var serviceCollection = new ServiceCollection();
                serviceCollection.AddQueries(Assembly);
                var provider = serviceCollection.BuildServiceProvider();

                provider.GetService<IQueryHandler<FakeQuery, FakeResult>>().Should().BeOfType<FakeQueryHandler>();
            }

            void should_create_a_QueryTypeProvider()
            {
                var serviceCollection = new ServiceCollection();
                serviceCollection.AddQueries(Assembly);
                var provider = serviceCollection.BuildServiceProvider();

                provider.GetService(typeof(IQueryTypeProvider)).Should().NotBeNull();
            }

            void should_add_all_queries_from_handler()
            {
                var serviceCollection = new ServiceCollection();
                serviceCollection.AddQueries(Assembly);
                var provider = serviceCollection.BuildServiceProvider();

                provider.GetService<IQueryHandler<FakeMultiQuery1, FakeResult>>().Should().BeOfType<FakeMultiHandler>();
                provider.GetService<IQueryHandler<FakeMultiQuery2, FakeResult>>().Should().BeOfType<FakeMultiHandler>();
            }
        }

        Assembly Assembly;
    }
}
```

## File: `tests/CommandQuery.Tests/Internal/DictionaryExtensionsTests.cs`
```csharp
using FluentAssertions;

namespace CommandQuery.Tests.Internal
{
    public class DictionaryExtensionsTests
    {
        [Test]
        public void GetQueryDictionary()
        {
            var query = TestData.FakeComplexQuery_As_Dictionary_Of_String_IEnumerable_String;
            var result = query.GetQueryDictionary(typeof(FakeComplexQuery));
            result.Should().BeEquivalentTo(TestData.FakeComplexQuery_As_Dictionary_Of_String_Object);
        }

        [Test]
        public void GetQueryDictionary_with_nested_query()
        {
            var query = TestData.FakeNestedQuery_As_Dictionary_Of_String_IEnumerable_String;
            var result = query.GetQueryDictionary(typeof(FakeNestedQuery));
            result.Should().BeEquivalentTo(TestData.FakeNestedQuery_As_Dictionary_Of_String_Object);
        }
    }
}
```

## File: `tests/CommandQuery.Tests/Internal/ExceptionExtensionsTests.cs`
```csharp
using CommandQuery.Exceptions;
using FluentAssertions;

namespace CommandQuery.Tests.Internal
{
    public class ExceptionExtensionsTests
    {
        [LoFu, Test]
        public void IsHandled()
        {
            void should_return_true_for_custom_exceptions()
            {
                new CommandException("").IsHandled().Should().BeTrue();
                new CommandProcessorException("").IsHandled().Should().BeTrue();
                new QueryException("").IsHandled().Should().BeTrue();
                new QueryProcessorException("").IsHandled().Should().BeTrue();
            }

            void should_return_false_for_other_exceptions() => new Exception().IsHandled().Should().BeFalse();
        }

        [Test]
        public void when_converting_Exception_to_Error()
        {
            var exception = new Exception("message");

            var result = exception.ToError();

            result.Message.Should().Be(exception.Message);
            result.Details.Should().BeNull();
        }

        [Test]
        public void when_converting_CommandException_to_Error()
        {
            var exception = new FakeCommandException("message")
            {
                String = "Value",
                Int = 1,
                Bool = true,
                DateTime = DateTime.Parse("2018-07-06"),
                Guid = Guid.Parse("3B10C34C-D423-4EC3-8811-DA2E0606E241"),
                NullableDouble = 2.1,
                Array = [1, 2],
                IEnumerable = [3, 4],
                List = [5, 6],
                Enum = FakeEnum.Some
            };

            var result = exception.ToError();

            result.Message.Should().Be(exception.Message);
            result.Details.Should().Contain("String", exception.String);
            result.Details.Should().Contain("Int", exception.Int);
            result.Details.Should().Contain("Bool", exception.Bool);
            result.Details.Should().Contain("DateTime", exception.DateTime);
            result.Details.Should().Contain("Guid", exception.Guid);
            result.Details.Should().Contain("NullableDouble", exception.NullableDouble);
            result.Details.Should().Contain("Array", exception.Array);
            result.Details.Should().Contain("IEnumerable", exception.IEnumerable);
            result.Details.Should().Contain("List", exception.List);
            result.Details.Should().Contain("Enum", exception.Enum);

            new CommandException("").ToError().Details.Should().BeNull();

            ((Exception)exception).ToError().Details.Should().NotBeNull();
        }

        [Test]
        public void when_converting_QueryException_to_Error()
        {
            var exception = new FakeQueryException("message")
            {
                String = "Value",
                Int = 1,
                Bool = true,
                DateTime = DateTime.Parse("2018-07-06"),
                Guid = Guid.Parse("3B10C34C-D423-4EC3-8811-DA2E0606E241"),
                NullableDouble = 2.1,
                Array = [1, 2],
                IEnumerable = [3, 4],
                List = [5, 6],
                Enum = FakeEnum.Some
            };

            var result = exception.ToError();

            result.Message.Should().Be(exception.Message);
            result.Details.Should().Contain("String", exception.String);
            result.Details.Should().Contain("Int", exception.Int);
            result.Details.Should().Contain("Bool", exception.Bool);
            result.Details.Should().Contain("DateTime", exception.DateTime);
            result.Details.Should().Contain("Guid", exception.Guid);
            result.Details.Should().Contain("NullableDouble", exception.NullableDouble);
            result.Details.Should().Contain("Array", exception.Array);
            result.Details.Should().Contain("IEnumerable", exception.IEnumerable);
            result.Details.Should().Contain("List", exception.List);
            result.Details.Should().Contain("Enum", exception.Enum);

            new QueryException("").ToError().Details.Should().BeNull();

            ((Exception)exception).ToError().Details.Should().NotBeNull();
        }
    }

    public class FakeCommandException : CommandException
    {
        public string String { get; set; }
        public int Int { get; set; }
        public bool Bool { get; set; }
        public DateTime DateTime { get; set; }
        public Guid Guid { get; set; }
        public double? NullableDouble { get; set; }
        public int[] Array { get; set; }
        public IEnumerable<int> IEnumerable { get; set; }
        public List<int> List { get; set; }
        public FakeEnum Enum { get; set; }

        public FakeCommandException(string message) : base(message)
        {
        }
    }

    public class FakeQueryException : QueryException
    {
        public string String { get; set; }
        public int Int { get; set; }
        public bool Bool { get; set; }
        public DateTime DateTime { get; set; }
        public Guid Guid { get; set; }
        public double? NullableDouble { get; set; }
        public int[] Array { get; set; }
        public IEnumerable<int> IEnumerable { get; set; }
        public List<int> List { get; set; }
        public FakeEnum Enum { get; set; }

        public FakeQueryException(string message) : base(message)
        {
        }
    }

    public enum FakeEnum
    {
        None,
        Some,
        All
    }
}
```

## File: `tests/CommandQuery.Tests/Internal/ReflectionExtensionsTests.cs`
```csharp
using System.Reflection;
using FluentAssertions;

namespace CommandQuery.Tests.Internal
{
    public class ReflectionExtensionsTests
    {
        [LoFu, Test]
        public void when_GetTypesAssignableTo()
        {
            Assembly = typeof(FakeCommandHandler).Assembly;

            void should_return_handlers_from_Assemblies()
            {
                new[] { Assembly }.GetTypesAssignableTo(typeof(ICommandHandler<>)).Should().Contain(typeof(FakeCommandHandler));
                new[] { Assembly }.GetTypesAssignableTo(typeof(ICommandHandler<,>)).Should().Contain(typeof(FakeResultCommandHandler));
                new[] { Assembly }.GetTypesAssignableTo(typeof(IQueryHandler<,>)).Should().Contain(typeof(FakeQueryHandler));
            }

            void should_return_handlers_from_Assembly()
            {
                Assembly.GetTypesAssignableTo(typeof(ICommandHandler<>)).Should().Contain(typeof(FakeCommandHandler));
                Assembly.GetTypesAssignableTo(typeof(ICommandHandler<,>)).Should().Contain(typeof(FakeResultCommandHandler));
                Assembly.GetTypesAssignableTo(typeof(IQueryHandler<,>)).Should().Contain(typeof(FakeQueryHandler));
            }
        }

        [Test]
        public void when_IsAssignableToType()
        {
            typeof(FakeCommand).IsAssignableToType(typeof(ICommand)).Should().BeTrue();
            typeof(FakeResultCommand).IsAssignableToType(typeof(ICommand<>)).Should().BeTrue();
            typeof(FakeQuery).IsAssignableToType(typeof(IQuery<>)).Should().BeTrue();

            typeof(FakeResult).IsAssignableToType(typeof(IEnumerable<>)).Should().BeFalse();
        }

        [Test]
        public void when_GetReturnType()
        {
            typeof(FakeResultCommand).GetResultType(typeof(ICommand<>)).Should().Be(typeof(FakeResult));
            typeof(FakeCommand).GetResultType(typeof(ICommand)).Should().BeNull();
        }

        [Test]
        public void when_GetHandlerInterfaceTypes()
        {
            typeof(FakeCommandHandler).GetHandlerInterfaceTypes(typeof(ICommandHandler<>)).Should().AllBeEquivalentTo(typeof(ICommandHandler<FakeCommand>));
            typeof(FakeResultCommandHandler).GetHandlerInterfaceTypes(typeof(ICommandHandler<,>)).Should().AllBeEquivalentTo(typeof(ICommandHandler<FakeResultCommand, FakeResult>));
            typeof(FakeQueryHandler).GetHandlerInterfaceTypes(typeof(IQueryHandler<,>)).Should().AllBeEquivalentTo(typeof(IQueryHandler<FakeQuery, FakeResult>));

            typeof(FakeMultiHandler).GetHandlerInterfaceTypes(typeof(ICommandHandler<>)).Count().Should().Be(2);
            typeof(FakeMultiHandler).GetHandlerInterfaceTypes(typeof(ICommandHandler<,>)).Count().Should().Be(2);
            typeof(FakeMultiHandler).GetHandlerInterfaceTypes(typeof(IQueryHandler<,>)).Count().Should().Be(2);
        }

        Assembly Assembly;
    }
}
```

## File: `tests/CommandQuery.Tests/Internal/ServiceProviderExtensionsTests.cs`
```csharp
using FluentAssertions;
using Microsoft.Extensions.DependencyInjection;

namespace CommandQuery.Tests.Internal
{
    public class ServiceProviderExtensionsTests
    {
        [LoFu, Test]
        public void when_GetSingleService()
        {
            var serviceCollection = new ServiceCollection();
            serviceCollection.AddTransient<ICommandHandler<FakeMultiCommand1>, FakeMultiHandler>();
            serviceCollection.AddTransient<IQueryHandler<FakeMultiQuery1, FakeResult>, FakeMultiHandler>();
            serviceCollection.AddTransient<IQueryHandler<FakeMultiQuery1, FakeResult>, FakeMultiHandler>();

            ServiceProvider = serviceCollection.BuildServiceProvider();

            void should_throw_ArgumentNullException_when_IServiceProvider_is_null()
            {
                Action act = () => ((IServiceProvider)null).GetSingleService(typeof(ICommandHandler<FakeMultiCommand1>));
                act.Should().Throw<ArgumentNullException>();
            }

            void should_throw_ArgumentNullException_when_the_service_type_is_null() =>
                ServiceProvider.Invoking(x => x.GetSingleService(null)).Should().Throw<ArgumentNullException>();

            void should_return_the_service_when_only_one_service_is_found() =>
                ServiceProvider.GetSingleService(typeof(ICommandHandler<FakeMultiCommand1>)).Should().BeOfType<FakeMultiHandler>();

            void should_return_null_when_no_service_is_found()
            {
                ServiceProvider.GetSingleService(typeof(ICommandHandler<FakeMultiCommand2>)).Should().BeNull();
                ServiceProvider.GetSingleService(typeof(int)).Should().BeNull();
            }

            void should_throw_InvalidOperationException_when_multiple_services_are_found() =>
                ServiceProvider.Invoking(x => x.GetSingleService(typeof(IQueryHandler<FakeMultiQuery1, FakeResult>))).Should().Throw<InvalidOperationException>();

            void should_throw_NotSupportedException_when_service_type_is_open() =>
                ServiceProvider.Invoking(x => x.GetSingleService(typeof(IEnumerable<>))).Should().Throw<NotSupportedException>();
        }

        [LoFu, Test]
        public void when_GetAllServiceTypes()
        {
            var serviceCollection = new ServiceCollection();
            serviceCollection.AddTransient<ICommandHandler<FakeMultiCommand1>, FakeMultiHandler>();

            ServiceProvider = serviceCollection.BuildServiceProvider();

            void should_return_empty_enumeration_when_IServiceProvider_is_null() =>
                ((IServiceProvider)null).GetAllServiceTypes().Should().BeEmpty();

            void should_return_empty_enumeration_if_IServiceProvider_does_not_have_the_right_private_members()
            {
                var broken = new Mock<IServiceProvider>().Object;
                broken.GetAllServiceTypes().Should().BeEmpty();
            }

            void should_return_all_service_types() =>
                ServiceProvider.GetAllServiceTypes().Should().Contain(typeof(ICommandHandler<FakeMultiCommand1>));
        }

        IServiceProvider ServiceProvider;
    }
}
```

## File: `tests/CommandQuery.Tests/SystemTextJson/CommandProcessorExtensionsTests.cs`
```csharp
using CommandQuery.Exceptions;
using CommandQuery.SystemTextJson;
using FluentAssertions;

namespace CommandQuery.Tests.SystemTextJson
{
    public class CommandProcessorExtensionsTests
    {
        [LoFu, Test]
        public async Task when_processing_the_command_with_or_without_result()
        {
            FakeCommandProcessor = new Mock<ICommandProcessor>();
            Subject = FakeCommandProcessor.Object;

            async Task should_invoke_the_correct_command_handler_for_commands_without_result()
            {
                var expectedCommandType = typeof(FakeCommand);
                FakeCommandProcessor.Setup(x => x.GetCommandType(expectedCommandType.Name)).Returns(expectedCommandType);
                FakeCommandProcessor.Setup(x => x.ProcessAsync(It.IsAny<FakeCommand>(), It.IsAny<CancellationToken>())).Returns(Task.CompletedTask);

                var result = await Subject.ProcessAsync(expectedCommandType.Name, "{}");

                result.Should().Be(CommandResult.None);
                FakeCommandProcessor.Verify(x => x.ProcessAsync(It.IsAny<FakeCommand>(), It.IsAny<CancellationToken>()));
            }

            async Task should_invoke_the_correct_command_handler_for_commands_with_result()
            {
                var expectedResult = new FakeResult();
                var expectedCommandType = typeof(FakeResultCommand);
                FakeCommandProcessor.Setup(x => x.GetCommandType(expectedCommandType.Name)).Returns(expectedCommandType);
                FakeCommandProcessor.Setup(x => x.ProcessAsync(It.IsAny<FakeResultCommand>(), It.IsAny<CancellationToken>())).Returns(Task.FromResult(expectedResult));

                var result = await Subject.ProcessAsync(expectedCommandType.Name, "{}");

                result.Value.Should().Be(expectedResult);
                FakeCommandProcessor.Verify(x => x.ProcessAsync(It.IsAny<FakeResultCommand>(), It.IsAny<CancellationToken>()));
            }

            async Task should_throw_exception_if_the_ICommandProcessor_is_null()
            {
                Func<Task> act = () => ((ICommandProcessor)null).ProcessAsync("", "{}");
                await act.Should().ThrowAsync<ArgumentNullException>();
            }

            async Task should_throw_exception_if_the_command_type_is_not_found()
            {
                var commandName = "NotFoundCommand";

                Func<Task> act = () => Subject.ProcessAsync(commandName, "{}");
                await act.Should().ThrowAsync<CommandProcessorException>()
                    .WithMessage("The command type 'NotFoundCommand' could not be found");
            }

            async Task should_throw_exception_if_the_json_is_invalid()
            {
                var commandName = "FakeCommand";

                Func<Task> act = () => Subject.ProcessAsync(commandName, "<>");
                await act.Should().ThrowAsync<CommandProcessorException>()
                    .WithMessage("The json string could not be deserialized to an object");
            }

            async Task should_throw_exception_if_the_json_is_null()
            {
                var commandName = "FakeCommand";

                Func<Task> act = () => Subject.ProcessAsync(commandName, null);
                await act.Should().ThrowAsync<ArgumentNullException>();
            }
        }

        Mock<ICommandProcessor> FakeCommandProcessor;
        ICommandProcessor Subject;
    }
}
```

## File: `tests/CommandQuery.Tests/SystemTextJson/QueryProcessorExtensionsTests.cs`
```csharp
using CommandQuery.Exceptions;
using CommandQuery.SystemTextJson;
using FluentAssertions;

namespace CommandQuery.Tests.SystemTextJson
{
    public class QueryProcessorExtensionsTests
    {
        [LoFu, Test]
        public async Task when_processing_the_query_from_json()
        {
            FakeQueryProcessor = new Mock<IQueryProcessor>();
            Subject = FakeQueryProcessor.Object;

            async Task should_create_the_query_from_a_json_string()
            {
                var expectedQueryType = typeof(FakeQuery);
                FakeQueryProcessor.Setup(x => x.GetQueryType(expectedQueryType.Name)).Returns(expectedQueryType);
                FakeQueryProcessor.Setup(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>())).Returns(Task.FromResult(new FakeResult()));

                await Subject.ProcessAsync<FakeResult>(expectedQueryType.Name, "{}");

                FakeQueryProcessor.Verify(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>()));
            }

            async Task should_throw_exception_if_the_IQueryProcessor_is_null()
            {
                Func<Task> act = () => ((IQueryProcessor)null).ProcessAsync<object>("", "{}");
                await act.Should().ThrowAsync<ArgumentNullException>();
            }

            async Task should_throw_exception_if_the_query_type_is_not_found_for_the_json()
            {
                var queryName = "NotFoundQuery";

                Func<Task> act = () => Subject.ProcessAsync<object>(queryName, "{}");
                await act.Should().ThrowAsync<QueryProcessorException>()
                    .WithMessage("The query type 'NotFoundQuery' could not be found");
            }

            async Task should_throw_exception_if_the_json_is_null()
            {
                var queryName = "FakeQuery";

                Func<Task> act = () => Subject.ProcessAsync<object>(queryName, (string)null);
                await act.Should().ThrowAsync<ArgumentNullException>()
                    .WithMessage("Value cannot be null*json*");
            }

            async Task should_throw_exception_if_the_json_is_invalid()
            {
                var queryName = "FakeQuery";

                Func<Task> act = () => Subject.ProcessAsync<object>(queryName, "<>");
                await act.Should().ThrowAsync<QueryProcessorException>()
                    .WithMessage("The json string could not be deserialized to an object");
            }
        }

        [LoFu, Test]
        public async Task when_processing_the_query_from_dictionary()
        {
            FakeQueryProcessor = new Mock<IQueryProcessor>();
            Subject = FakeQueryProcessor.Object;

            async Task should_create_the_query_from_a_dictionary()
            {
                var expectedQueryType = typeof(FakeQuery);
                FakeQueryProcessor.Setup(x => x.GetQueryType(expectedQueryType.Name)).Returns(expectedQueryType);

                await Subject.ProcessAsync<FakeResult>(expectedQueryType.Name, new Dictionary<string, IEnumerable<string>>());

                FakeQueryProcessor.Verify(x => x.ProcessAsync(It.IsAny<FakeQuery>(), It.IsAny<CancellationToken>()));
            }

            async Task should_throw_exception_if_the_IQueryProcessor_is_null()
            {
                Func<Task> act = () => ((IQueryProcessor)null).ProcessAsync<object>("", new Dictionary<string, IEnumerable<string>>());
                await act.Should().ThrowAsync<ArgumentNullException>();
            }

            async Task should_throw_exception_if_the_query_type_is_not_found_for_the_dictionary()
            {
                var queryName = "NotFoundQuery";

                Func<Task> act = () => Subject.ProcessAsync<object>(queryName, new Dictionary<string, IEnumerable<string>>());
                await act.Should().ThrowAsync<QueryProcessorException>()
                    .WithMessage("The query type 'NotFoundQuery' could not be found");
            }

            async Task should_create_a_complex_query_from_a_dictionary()
            {
                var expectedQueryType = typeof(FakeComplexQuery);
                FakeQueryProcessor.Setup(x => x.GetQueryType(expectedQueryType.Name)).Returns(expectedQueryType);
                FakeComplexQuery actual = null;
                FakeQueryProcessor
                    .Setup(x => x.ProcessAsync(It.IsAny<FakeComplexQuery>(), It.IsAny<CancellationToken>()))
                    .Returns(Task.FromResult(Enumerable.Empty<FakeResult>()))
                    .Callback<FakeComplexQuery, CancellationToken>((query, _) => actual = query);

                var query = TestData.FakeComplexQuery_As_Dictionary_Of_String_IEnumerable_String;

                await Subject.ProcessAsync<IEnumerable<FakeResult>>(expectedQueryType.Name, query);

                actual.Should().BeEquivalentTo(TestData.FakeComplexQuery);
            }

            async Task should_create_a_query_with_DateTime_kinds_from_a_dictionary()
            {
                var expectedQueryType = typeof(FakeDateTimeQuery);
                FakeQueryProcessor.Setup(x => x.GetQueryType(expectedQueryType.Name)).Returns(expectedQueryType);
                FakeDateTimeQuery actual = null;
                FakeQueryProcessor
                    .Setup(x => x.ProcessAsync(It.IsAny<FakeDateTimeQuery>(), It.IsAny<CancellationToken>()))
                    .Returns(Task.FromResult(new FakeResult()))
                    .Callback<FakeDateTimeQuery, CancellationToken>((query, _) => actual = query);

                var query = TestData.FakeDateTimeQuery_As_Dictionary_Of_String_IEnumerable_String;

                await Subject.ProcessAsync<FakeResult>(expectedQueryType.Name, query);

                actual.Should().BeEquivalentTo(TestData.FakeDateTimeQuery);
            }

            async Task should_not_create_a_query_with_nested_objects_from_a_dictionary()
            {
                var expectedQueryType = typeof(FakeNestedQuery);
                FakeQueryProcessor.Setup(x => x.GetQueryType(expectedQueryType.Name)).Returns(expectedQueryType);
                FakeNestedQuery actual = null;
                FakeQueryProcessor
                    .Setup(x => x.ProcessAsync(It.IsAny<FakeNestedQuery>(), It.IsAny<CancellationToken>()))
                    .Returns(Task.FromResult(new FakeResult()))
                    .Callback<FakeNestedQuery, CancellationToken>((query, _) => actual = query);

                var query = TestData.FakeNestedQuery_As_Dictionary_Of_String_IEnumerable_String;

                await Subject.ProcessAsync<FakeResult>(expectedQueryType.Name, query);

                actual.Should().BeEquivalentTo(TestData.FakeNestedQuery);
            }

            async Task should_throw_exception_if_the_dictionary_is_invalid()
            {
                var queryName = "FakeQuery";

                Func<Task> act = () => Subject.ProcessAsync<object>(queryName, null, CancellationToken.None);
                await act.Should().ThrowAsync<QueryProcessorException>()
                    .WithMessage("The dictionary could not be deserialized to an object");
            }
        }

        Mock<IQueryProcessor> FakeQueryProcessor;
        IQueryProcessor Subject;
    }
}
```

## File: `tests/CommandQuery.Tests/SystemTextJson/Internal/BooleanConverterTests.cs`
```csharp
using System.Text.Json;
using CommandQuery.SystemTextJson;
using FluentAssertions;

namespace CommandQuery.Tests.SystemTextJson.Internal
{
    public class BooleanConverterTests
    {
        [Test]
        public void Read()
        {
            var options = new JsonSerializerOptions();
            options.Converters.Add(new BooleanConverter());

            JsonSerializer.Deserialize<bool>("true", options).Should().BeTrue();
            JsonSerializer.Deserialize<bool>(@"""true""", options).Should().BeTrue();
            JsonSerializer.Deserialize<bool>("false", options).Should().BeFalse();
            JsonSerializer.Deserialize<bool>(@"""false""", options).Should().BeFalse();

            Action act = () => JsonSerializer.Deserialize<bool>("1", options);
            act.Should().Throw<JsonException>();
            act = () => JsonSerializer.Deserialize<bool>(@"""1""", options);
            act.Should().Throw<JsonException>();
        }

        [Test]
        public void Write()
        {
            var options = new JsonSerializerOptions();
            options.Converters.Add(new BooleanConverter());

            JsonSerializer.Serialize(true, options).Should().Be("true");
            JsonSerializer.Serialize(false, options).Should().Be("false");
        }
    }
}
```

## File: `tests/CommandQuery.Tests/SystemTextJson/Internal/JsonExtensionsTests.cs`
```csharp
using System.Text.Json;
using CommandQuery.SystemTextJson;
using FluentAssertions;

namespace CommandQuery.Tests.SystemTextJson.Internal
{
    public class JsonExtensionsTests
    {
        [LoFu, Test]
        public void SafeDeserialize_string()
        {
            void should_return_an_object()
            {
                "{}".SafeDeserialize(typeof(object)).Should().NotBeNull();

                JsonSerializer.Serialize(TestData.FakeComplexQuery)
                    .SafeDeserialize(typeof(FakeComplexQuery))
                    .Should().BeEquivalentTo(TestData.FakeComplexQuery);

                JsonSerializer.Serialize(TestData.FakeDateTimeQuery)
                    .SafeDeserialize(typeof(FakeDateTimeQuery))
                    .Should().BeEquivalentTo(TestData.FakeDateTimeQuery);

                JsonSerializer.Serialize(TestData.FakeNestedQuery)
                    .SafeDeserialize(typeof(FakeNestedQuery))
                    .Should().BeEquivalentTo(TestData.FakeNestedQuery);
            }

            void should_have_sane_defaults()
            {
                var result = "{\"int32\":\"1\"}".SafeDeserialize(typeof(FakeComplexQuery)) as FakeComplexQuery;
                result.Int32.Should().Be(1);
            }

            void should_use_options_when_provided()
            {
                var options = new JsonSerializerOptions(JsonSerializerDefaults.Web);
                var result = "{\"int32\":\"1\"}".SafeDeserialize(typeof(FakeComplexQuery), options) as FakeComplexQuery;
                result.Int32.Should().Be(1);
            }

            void should_return_null_if_deserialization_fails() => ((string)null).SafeDeserialize(typeof(object)).Should().BeNull();
        }

        [LoFu, Test]
        public void SafeDeserialize_Dictionary()
        {
            void should_set_the_property_values()
            {
                var subject = TestData.FakeComplexQuery_As_Dictionary_Of_String_Object;
                var result = subject.SafeDeserialize(typeof(FakeComplexQuery)) as FakeComplexQuery;
                result.Should().BeEquivalentTo(TestData.FakeComplexQuery);

                subject = TestData.FakeComplexQuery_As_Dictionary_Of_String_Object.ToDictionary(x => x.Key.ToLower(), x => x.Value);
                result = subject.SafeDeserialize(typeof(FakeComplexQuery)) as FakeComplexQuery;
                result.Should().BeEquivalentTo(TestData.FakeComplexQuery);
            }

            void should_set_the_property_values_of_DateTime_kinds()
            {
                var subject = TestData.FakeDateTimeQuery_As_Dictionary_Of_String_Object;

                var result = subject.SafeDeserialize(typeof(FakeDateTimeQuery)) as FakeDateTimeQuery;

                result.Should().BeEquivalentTo(TestData.FakeDateTimeQuery);
            }

            void should_not_set_the_property_values_of_nested_objects()
            {
                var subject = TestData.FakeNestedQuery_As_Dictionary_Of_String_Object;

                var result = subject.SafeDeserialize(typeof(FakeNestedQuery)) as FakeNestedQuery;

                result.Should().BeEquivalentTo(TestData.FakeNestedQuery);
            }

            void should_return_null_if_dictionary_is_null()
            {
                IDictionary<string, object> subject = null;

                subject.SafeDeserialize(typeof(FakeComplexQuery)).Should().BeNull();
            }

            void should_return_null_if_conversion_fails()
            {
                var subject = new Dictionary<string, object>
                {
                    { "Guid", "fail" }
                };

                subject.SafeDeserialize(typeof(FakeComplexQuery)).Should().BeNull();
            }
        }
    }
}
```


---
id: github.com-itlibrium-ddd-starter-dotnet-3776c022-k
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:09.316222
---

# KNOWLEDGE EXTRACT: github.com_itlibrium_DDD-starter-dotnet_3776c022
> **Extracted on:** 2026-04-01 09:47:01
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520450/github.com_itlibrium_DDD-starter-dotnet_3776c022

---

## File: `.gitignore`
```
*.swp
*.*~
project.lock.json
.DS_Store
*.pyc
nupkg/

# Visual Studio Code
.vscode

# Rider
.idea

# User-specific files
*.suo
*.user
*.userosscache
*.sln.docstates

# Build results
[Dd]ebug/
[Dd]ebugPublic/
[Rr]elease/
[Rr]eleases/
x64/
x86/
build/
bld/
[Bb]in/
[Oo]bj/
[Oo]ut/
msbuild.log
msbuild.err
msbuild.wrn

# Visual Studio 2015
.vs/

# Nuke
.tmp/
.nuke/
Build/Nuke/Artifacts/
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2019 ITLibrium

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

## File: `MyCompany.Crm.sln.DotSettings`
```
﻿<wpf:ResourceDictionary xml:space="preserve" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" xmlns:s="clr-namespace:System;assembly=mscorlib" xmlns:ss="urn:shemas-jetbrains-com:settings-storage-xaml" xmlns:wpf="http://schemas.microsoft.com/winfx/2006/xaml/presentation">
	<s:Int64 x:Key="/Default/CodeStyle/CodeFormatting/CSharpFormat/BLANK_LINES_AFTER_BLOCK_STATEMENTS/@EntryValue">0</s:Int64>
	<s:String x:Key="/Default/CodeStyle/CodeFormatting/CSharpFormat/EMPTY_BLOCK_STYLE/@EntryValue">TOGETHER_SAME_LINE</s:String>
	<s:Int64 x:Key="/Default/CodeStyle/CodeFormatting/CSharpFormat/KEEP_BLANK_LINES_IN_CODE/@EntryValue">1</s:Int64>
	<s:Int64 x:Key="/Default/CodeStyle/CodeFormatting/CSharpFormat/KEEP_BLANK_LINES_IN_DECLARATIONS/@EntryValue">1</s:Int64>
	<s:String x:Key="/Default/CodeStyle/CodeFormatting/CSharpFormat/PLACE_ACCESSORHOLDER_ATTRIBUTE_ON_SAME_LINE_EX/@EntryValue">NEVER</s:String>
	<s:String x:Key="/Default/CodeStyle/CodeFormatting/CSharpFormat/PLACE_FIELD_ATTRIBUTE_ON_SAME_LINE_EX/@EntryValue">NEVER</s:String>
	<s:String x:Key="/Default/CodeStyle/Naming/CSharpNaming/PredefinedNamingRules/=Interfaces/@EntryIndexedValue">&lt;Policy Inspect="True" Prefix="" Suffix="" Style="AaBb" /&gt;</s:String>
	<s:String x:Key="/Default/CodeStyle/Naming/CSharpNaming/PredefinedNamingRules/=PrivateStaticReadonly/@EntryIndexedValue">&lt;Policy Inspect="True" Prefix="" Suffix="" Style="AaBb_AaBb" /&gt;</s:String>
	<s:String x:Key="/Default/Environment/InlayHints/CSharpTypeNameHintsOptions/ShowMethodReturnTypeNameHints/@EntryValue">Default</s:String>
	<s:String x:Key="/Default/Environment/InlayHints/CSharpTypeNameHintsOptions/ShowTypeNameHintsForImplicitlyTypedVariables/@EntryValue">PushToShowHints</s:String>
	<s:Boolean x:Key="/Default/Environment/SettingsMigration/IsMigratorApplied/=JetBrains_002EReSharper_002EPsi_002ECSharp_002ECodeStyle_002ECSharpKeepExistingMigration/@EntryIndexedValue">True</s:Boolean>
	<s:Boolean x:Key="/Default/Environment/SettingsMigration/IsMigratorApplied/=JetBrains_002EReSharper_002EPsi_002ECSharp_002ECodeStyle_002ECSharpPlaceEmbeddedOnSameLineMigration/@EntryIndexedValue">True</s:Boolean>
	<s:Boolean x:Key="/Default/Environment/SettingsMigration/IsMigratorApplied/=JetBrains_002EReSharper_002EPsi_002ECSharp_002ECodeStyle_002ECSharpUseContinuousIndentInsideBracesMigration/@EntryIndexedValue">True</s:Boolean>
	<s:Boolean x:Key="/Default/Environment/SettingsMigration/IsMigratorApplied/=JetBrains_002EReSharper_002EPsi_002ECSharp_002ECodeStyle_002ESettingsUpgrade_002EMigrateBlankLinesAroundFieldToBlankLinesAroundProperty/@EntryIndexedValue">True</s:Boolean>
	<s:Boolean x:Key="/Default/UserDictionary/Words/=ITLIBRIUM/@EntryIndexedValue">True</s:Boolean>
	<s:Boolean x:Key="/Default/UserDictionary/Words/=Shouldly/@EntryIndexedValue">True</s:Boolean></wpf:ResourceDictionary>
```

## File: `MyCompany.ECommerce.sln`
```
﻿
Microsoft Visual Studio Solution File, Format Version 12.00
Project("{2150E333-8FDC-42A3-9474-1A3956D46DE8}") = "Sales", "Sales", "{B442AF5F-B127-45EF-B835-714A187D3F0A}"
	ProjectSection(SolutionItems) = preProject
		Sources\Sales\SalesDomainModelInfo.json = Sources\Sales\SalesDomainModelInfo.json
	EndProjectSection
EndProject
Project("{2150E333-8FDC-42A3-9474-1A3956D46DE8}") = "Contacts", "Contacts", "{6114F446-78E7-49DC-BA34-C9904FE7838B}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "Contacts", "Sources\Contacts\Contacts\Contacts.csproj", "{9DE86BB4-7D8E-4997-BDCE-C5E7E30968AF}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "Monolith.Startup", "Sources\Monolith.Startup\Monolith.Startup.csproj", "{B064C8A6-79AB-4B7B-98A6-A5F15635ED8D}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "Sales.RestApi", "Sources\Sales\Sales.RestApi\Sales.RestApi.csproj", "{E7E66DCC-7D68-4900-B09D-DE06E89DA534}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "Sales.Adapters", "Sources\Sales\Sales.Adapters\Sales.Adapters.csproj", "{0F36E2E3-EEFC-4C74-88DF-AA281238F768}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "Sales.ProcessModel", "Sources\Sales\Sales.ProcessModel\Sales.ProcessModel.csproj", "{EA9ECA12-F038-4437-8D08-34A61DC2DE50}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "Sales.DeepModel", "Sources\Sales\Sales.DeepModel\Sales.DeepModel.csproj", "{88560531-4322-49A6-BE34-91D70CF8CE5C}"
EndProject
Project("{2150E333-8FDC-42A3-9474-1A3956D46DE8}") = "TechnicalStuff", "TechnicalStuff", "{E9167F5F-E45B-4ABD-ACCD-89E3514BB0AA}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "TechnicalStuff", "Sources\TechnicalStuff\TechnicalStuff\TechnicalStuff.csproj", "{CD120717-6AF0-4A13-A62F-9B86F23DD408}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "Sales.DeepModel.Tests", "Sources\Sales\Sales.DeepModel.Tests\Sales.DeepModel.Tests.csproj", "{AD0D919C-8499-46A7-869E-EEB6456C6BA9}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "Sales.ProcessModel.Tests", "Sources\Sales\Sales.ProcessModel.Tests\Sales.ProcessModel.Tests.csproj", "{44B45E96-A286-44DC-A2F7-0E213005BDBF}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "TechnicalStuff.Crud", "Sources\TechnicalStuff\TechnicalStuff.Crud\TechnicalStuff.Crud.csproj", "{7366E7E8-283D-4772-9807-BDC55917B9F3}"
EndProject
Project("{2150E333-8FDC-42A3-9474-1A3956D46DE8}") = "Sources", "Sources", "{109EBFC9-4414-4331-AD7B-5C19A87CBF8B}"
	ProjectSection(SolutionItems) = preProject
		Sources\DomainVisionStatement.md = Sources\DomainVisionStatement.md
	EndProjectSection
EndProject
Project("{2150E333-8FDC-42A3-9474-1A3956D46DE8}") = "Build", "Build", "{2F88D996-6A05-4BE0-A064-F7748E584090}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "Nuke", "Build\Nuke\Nuke.csproj", "{F98F4F5C-DDF2-4756-A5EA-715DE0D22402}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "Nuke.DockerCompose", "Build\Nuke.DockerCompose\Nuke.DockerCompose.csproj", "{C751FBCB-B7AE-4ECE-BEDE-4A6600EC77D0}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "Sales.IntegrationTests", "Sources\Sales\Sales.IntegrationTests\Sales.IntegrationTests.csproj", "{4B8223B4-1F0C-444C-88CE-B181D8277ACE}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "TechnicalStuff.Marten", "Sources\TechnicalStuff\TechnicalStuff.Marten\TechnicalStuff.Marten.csproj", "{E5526B10-65CB-4619-A5C3-4C29A86D76A9}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "TechnicalStuff.Transactions", "Sources\TechnicalStuff\TechnicalStuff.Transactions\TechnicalStuff.Transactions.csproj", "{9FF8E353-1ACC-407A-A9B8-55183261A8C8}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "TechnicalStuff.ProcessModel", "Sources\TechnicalStuff\TechnicalStuff.ProcessModel\TechnicalStuff.ProcessModel.csproj", "{85E951AA-5333-4181-B5B1-305050405BFE}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "TechnicalStuff.Kafka", "Sources\TechnicalStuff\TechnicalStuff.Kafka\TechnicalStuff.Kafka.csproj", "{E033439A-DE1C-46D1-A33B-FBFA71812901}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "TechnicalStuff.Outbox.Kafka", "Sources\TechnicalStuff\TechnicalStuff.Outbox.Kafka\TechnicalStuff.Outbox.Kafka.csproj", "{D014CF07-21C0-4783-B8BE-A2153289215A}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "TechnicalStuff.Api", "Sources\TechnicalStuff\TechnicalStuff.Api\TechnicalStuff.Api.csproj", "{63F7927D-D6F2-43EF-9E41-1C70C6911434}"
EndProject
Project("{2150E333-8FDC-42A3-9474-1A3956D46DE8}") = "Tests", "Tests", "{5FBC2CAC-E39A-4899-9CC1-94EF0712BDAE}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "TechnicalStuff.Crud.Ef", "Sources\TechnicalStuff\TechnicalStuff.Crud.Ef\TechnicalStuff.Crud.Ef.csproj", "{F453B007-94DB-4F0B-B598-93D50B077C8F}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "TechnicalStuff.Crud.Api", "Sources\TechnicalStuff\TechnicalStuff.Crud.Api\TechnicalStuff.Crud.Api.csproj", "{971A1F55-C6D6-456C-A19A-772182DCE97F}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "TechnicalStuff.Outbox", "Sources\TechnicalStuff\TechnicalStuff.Outbox\TechnicalStuff.Outbox.csproj", "{529DB367-5C6D-4103-B0B5-9D540E84F88B}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "TechnicalStuff.Outbox.Postgres", "Sources\TechnicalStuff\TechnicalStuff.Outbox.Postgres\TechnicalStuff.Outbox.Postgres.csproj", "{077E8C19-C1A4-4073-9BE8-4EE3701B3504}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "TechnicalStuff.Postgres", "Sources\TechnicalStuff\TechnicalStuff.Postgres\TechnicalStuff.Postgres.csproj", "{CB589043-28B4-46FB-9BC3-3591D9FF8C6D}"
EndProject
Project("{2150E333-8FDC-42A3-9474-1A3956D46DE8}") = "Payments", "Payments", "{BFB7ABD8-A1AC-41A9-B40B-C2F9389ABAF0}"
	ProjectSection(SolutionItems) = preProject
		Sources\Payments\PaymentModelInfo.json = Sources\Payments\PaymentModelInfo.json
	EndProjectSection
EndProject
Project("{2150E333-8FDC-42A3-9474-1A3956D46DE8}") = "RiskManagement", "RiskManagement", "{B132FA8E-B99A-420A-919D-5DA77555517C}"
	ProjectSection(SolutionItems) = preProject
		Sources\RiskManagement\RiskManagementModelInfo.json = Sources\RiskManagement\RiskManagementModelInfo.json
	EndProjectSection
EndProject
Project("{2150E333-8FDC-42A3-9474-1A3956D46DE8}") = "ProductsDelivery", "ProductsDelivery", "{A1B88082-6C3F-4A8E-89E7-ABFD08A5A89E}"
	ProjectSection(SolutionItems) = preProject
		Sources\ProductsDelivery\ProductsDeliveryModelInfo.json = Sources\ProductsDelivery\ProductsDeliveryModelInfo.json
	EndProjectSection
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "Payments.ProcessModel", "Sources\Payments\Payments.ProcessModel\Payments.ProcessModel.csproj", "{F0906A93-243B-4BD0-A10F-FD6975F7DF10}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "ProductsDelivery.ProcessModel", "Sources\ProductsDelivery\ProductsDelivery.ProcessModel\ProductsDelivery.ProcessModel.csproj", "{BB564CD2-68E0-4479-8DB1-4BA49901F25E}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "RiskManagement.ProcessModel", "Sources\RiskManagement\RiskManagement.ProcessModel\RiskManagement.ProcessModel.csproj", "{005314CE-7AE5-422D-A90C-E2A4A9F29B02}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "TechnicalStuff.Outbox.Quartz", "Sources\TechnicalStuff\TechnicalStuff.Outbox.Quartz\TechnicalStuff.Outbox.Quartz.csproj", "{22B5AF7D-F6EC-47E1-8255-E17381AEF6F9}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "TechnicalStuff.Ef", "Sources\TechnicalStuff\TechnicalStuff.Ef\TechnicalStuff.Ef.csproj", "{81865144-6255-4828-B920-C494990E1380}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "TechnicalStuff.Json", "Sources\TechnicalStuff\TechnicalStuff.Json\TechnicalStuff.Json.csproj", "{D03CF004-F9F0-4EA4-9DF8-7C5F0F5EEE85}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "Sales.FluentMigrations", "Sources\Sales\Sales.FluentMigrations\Sales.FluentMigrations.csproj", "{E14C64C4-1972-49B4-AEF6-1B826B7E0E1C}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "TechnicalStuff.Persistence", "Sources\TechnicalStuff\TechnicalStuff.Persistence\TechnicalStuff.Persistence.csproj", "{7C31A913-87D2-4A03-A6B4-B6578882DDA1}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "TechnicalStuff.Persistence.RepoDb", "Sources\TechnicalStuff\TechnicalStuff.Persistence.RepoDb\TechnicalStuff.Persistence.RepoDb.csproj", "{767884F2-2324-4E58-BD44-210B6D339AC8}"
EndProject
Project("{2150E333-8FDC-42A3-9474-1A3956D46DE8}") = "Search", "Search", "{77FDB1B2-4CDF-4787-AE38-5090B9101CE5}"
	ProjectSection(SolutionItems) = preProject
		Sources\Search\SearchModelInfo.json = Sources\Search\SearchModelInfo.json
	EndProjectSection
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "Search.Startup", "Sources\Search.Startup\Search.Startup.csproj", "{76F474F0-ABF9-45ED-B4DA-52411E5B7D2B}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "Search.Api", "Sources\Search\Search.Api\Search.Api.csproj", "{A790A9C0-9557-4B01-80C4-3B8127E96C85}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "Search.Infrastructure", "Sources\Search\Search.Infrastructure\Search.Infrastructure.csproj", "{248E00B3-D637-46A0-9A34-50C0B9B15E5E}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "Payments.DeepModel", "Sources\Payments\Payments.DeepModel\Payments.DeepModel.csproj", "{9ACFD89D-1617-4BE5-99CB-0D29F14B1E6D}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "Payments.Adapters.Api", "Sources\Payments\Payments.Adapters.Api\Payments.Adapters.Api.csproj", "{41D6FB86-BB30-4BA0-B571-4FC5F7461BD3}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "Payments.Adapters.Out", "Sources\Payments\Payments.Adapters.Out\Payments.Adapters.Out.csproj", "{0EF67E99-4BF5-40FA-A6D6-DAA6EC8DA8E7}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "RiskManagement.DeepModel", "Sources\RiskManagement\RiskManagement.DeepModel\RiskManagement.DeepModel.csproj", "{9D3F8A61-7FA6-4D05-9FBB-7F2ECFA5669A}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "RiskManagement.Adapters.Api", "Sources\RiskManagement\RiskManagement.Adapters.Api\RiskManagement.Adapters.Api.csproj", "{E75D22ED-2FB4-440B-A343-F697A6D7324B}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "RiskManagement.Adapters.Out", "Sources\RiskManagement\RiskManagement.Adapters.Out\RiskManagement.Adapters.Out.csproj", "{7157262D-FECB-4802-BF55-9629A1D17EC2}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "ProductsDelivery.Adapters.Api", "Sources\ProductsDelivery\ProductsDelivery.Adapters.Api\ProductsDelivery.Adapters.Api.csproj", "{ECDB0505-6712-485E-8983-A20E1EF99239}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "ProductsDelivery.Adapters.Out", "Sources\ProductsDelivery\ProductsDelivery.Adapters.Out\ProductsDelivery.Adapters.Out.csproj", "{FE6E23DC-151B-4D55-BAD5-B97C561ED973}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "ProductsDelivery.DeepModel", "Sources\ProductsDelivery\ProductsDelivery.DeepModel\ProductsDelivery.DeepModel.csproj", "{2EF68AE3-819E-4FE4-8364-CD54375C2A9A}"
EndProject
Global
	GlobalSection(SolutionConfigurationPlatforms) = preSolution
		Debug|Any CPU = Debug|Any CPU
		Release|Any CPU = Release|Any CPU
	EndGlobalSection
	GlobalSection(ProjectConfigurationPlatforms) = postSolution
		{F98F4F5C-DDF2-4756-A5EA-715DE0D22402}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{F98F4F5C-DDF2-4756-A5EA-715DE0D22402}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{9DE86BB4-7D8E-4997-BDCE-C5E7E30968AF}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{9DE86BB4-7D8E-4997-BDCE-C5E7E30968AF}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{9DE86BB4-7D8E-4997-BDCE-C5E7E30968AF}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{9DE86BB4-7D8E-4997-BDCE-C5E7E30968AF}.Release|Any CPU.Build.0 = Release|Any CPU
		{B064C8A6-79AB-4B7B-98A6-A5F15635ED8D}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{B064C8A6-79AB-4B7B-98A6-A5F15635ED8D}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{B064C8A6-79AB-4B7B-98A6-A5F15635ED8D}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{B064C8A6-79AB-4B7B-98A6-A5F15635ED8D}.Release|Any CPU.Build.0 = Release|Any CPU
		{E7E66DCC-7D68-4900-B09D-DE06E89DA534}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{E7E66DCC-7D68-4900-B09D-DE06E89DA534}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{E7E66DCC-7D68-4900-B09D-DE06E89DA534}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{E7E66DCC-7D68-4900-B09D-DE06E89DA534}.Release|Any CPU.Build.0 = Release|Any CPU
		{0F36E2E3-EEFC-4C74-88DF-AA281238F768}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{0F36E2E3-EEFC-4C74-88DF-AA281238F768}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{0F36E2E3-EEFC-4C74-88DF-AA281238F768}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{0F36E2E3-EEFC-4C74-88DF-AA281238F768}.Release|Any CPU.Build.0 = Release|Any CPU
		{EA9ECA12-F038-4437-8D08-34A61DC2DE50}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{EA9ECA12-F038-4437-8D08-34A61DC2DE50}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{EA9ECA12-F038-4437-8D08-34A61DC2DE50}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{EA9ECA12-F038-4437-8D08-34A61DC2DE50}.Release|Any CPU.Build.0 = Release|Any CPU
		{88560531-4322-49A6-BE34-91D70CF8CE5C}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{88560531-4322-49A6-BE34-91D70CF8CE5C}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{88560531-4322-49A6-BE34-91D70CF8CE5C}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{88560531-4322-49A6-BE34-91D70CF8CE5C}.Release|Any CPU.Build.0 = Release|Any CPU
		{CD120717-6AF0-4A13-A62F-9B86F23DD408}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{CD120717-6AF0-4A13-A62F-9B86F23DD408}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{CD120717-6AF0-4A13-A62F-9B86F23DD408}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{CD120717-6AF0-4A13-A62F-9B86F23DD408}.Release|Any CPU.Build.0 = Release|Any CPU
		{AD0D919C-8499-46A7-869E-EEB6456C6BA9}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{AD0D919C-8499-46A7-869E-EEB6456C6BA9}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{AD0D919C-8499-46A7-869E-EEB6456C6BA9}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{AD0D919C-8499-46A7-869E-EEB6456C6BA9}.Release|Any CPU.Build.0 = Release|Any CPU
		{44B45E96-A286-44DC-A2F7-0E213005BDBF}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{44B45E96-A286-44DC-A2F7-0E213005BDBF}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{44B45E96-A286-44DC-A2F7-0E213005BDBF}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{44B45E96-A286-44DC-A2F7-0E213005BDBF}.Release|Any CPU.Build.0 = Release|Any CPU
		{7366E7E8-283D-4772-9807-BDC55917B9F3}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{7366E7E8-283D-4772-9807-BDC55917B9F3}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{7366E7E8-283D-4772-9807-BDC55917B9F3}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{7366E7E8-283D-4772-9807-BDC55917B9F3}.Release|Any CPU.Build.0 = Release|Any CPU
		{C751FBCB-B7AE-4ECE-BEDE-4A6600EC77D0}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{C751FBCB-B7AE-4ECE-BEDE-4A6600EC77D0}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{C751FBCB-B7AE-4ECE-BEDE-4A6600EC77D0}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{C751FBCB-B7AE-4ECE-BEDE-4A6600EC77D0}.Release|Any CPU.Build.0 = Release|Any CPU
		{4B8223B4-1F0C-444C-88CE-B181D8277ACE}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{4B8223B4-1F0C-444C-88CE-B181D8277ACE}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{4B8223B4-1F0C-444C-88CE-B181D8277ACE}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{4B8223B4-1F0C-444C-88CE-B181D8277ACE}.Release|Any CPU.Build.0 = Release|Any CPU
		{E5526B10-65CB-4619-A5C3-4C29A86D76A9}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{E5526B10-65CB-4619-A5C3-4C29A86D76A9}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{E5526B10-65CB-4619-A5C3-4C29A86D76A9}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{E5526B10-65CB-4619-A5C3-4C29A86D76A9}.Release|Any CPU.Build.0 = Release|Any CPU
		{9FF8E353-1ACC-407A-A9B8-55183261A8C8}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{9FF8E353-1ACC-407A-A9B8-55183261A8C8}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{9FF8E353-1ACC-407A-A9B8-55183261A8C8}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{9FF8E353-1ACC-407A-A9B8-55183261A8C8}.Release|Any CPU.Build.0 = Release|Any CPU
		{85E951AA-5333-4181-B5B1-305050405BFE}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{85E951AA-5333-4181-B5B1-305050405BFE}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{85E951AA-5333-4181-B5B1-305050405BFE}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{85E951AA-5333-4181-B5B1-305050405BFE}.Release|Any CPU.Build.0 = Release|Any CPU
		{E033439A-DE1C-46D1-A33B-FBFA71812901}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{E033439A-DE1C-46D1-A33B-FBFA71812901}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{E033439A-DE1C-46D1-A33B-FBFA71812901}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{E033439A-DE1C-46D1-A33B-FBFA71812901}.Release|Any CPU.Build.0 = Release|Any CPU
		{D014CF07-21C0-4783-B8BE-A2153289215A}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{D014CF07-21C0-4783-B8BE-A2153289215A}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{D014CF07-21C0-4783-B8BE-A2153289215A}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{D014CF07-21C0-4783-B8BE-A2153289215A}.Release|Any CPU.Build.0 = Release|Any CPU
		{63F7927D-D6F2-43EF-9E41-1C70C6911434}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{63F7927D-D6F2-43EF-9E41-1C70C6911434}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{63F7927D-D6F2-43EF-9E41-1C70C6911434}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{63F7927D-D6F2-43EF-9E41-1C70C6911434}.Release|Any CPU.Build.0 = Release|Any CPU
		{F453B007-94DB-4F0B-B598-93D50B077C8F}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{F453B007-94DB-4F0B-B598-93D50B077C8F}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{F453B007-94DB-4F0B-B598-93D50B077C8F}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{F453B007-94DB-4F0B-B598-93D50B077C8F}.Release|Any CPU.Build.0 = Release|Any CPU
		{971A1F55-C6D6-456C-A19A-772182DCE97F}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{971A1F55-C6D6-456C-A19A-772182DCE97F}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{971A1F55-C6D6-456C-A19A-772182DCE97F}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{971A1F55-C6D6-456C-A19A-772182DCE97F}.Release|Any CPU.Build.0 = Release|Any CPU
		{529DB367-5C6D-4103-B0B5-9D540E84F88B}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{529DB367-5C6D-4103-B0B5-9D540E84F88B}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{529DB367-5C6D-4103-B0B5-9D540E84F88B}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{529DB367-5C6D-4103-B0B5-9D540E84F88B}.Release|Any CPU.Build.0 = Release|Any CPU
		{077E8C19-C1A4-4073-9BE8-4EE3701B3504}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{077E8C19-C1A4-4073-9BE8-4EE3701B3504}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{077E8C19-C1A4-4073-9BE8-4EE3701B3504}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{077E8C19-C1A4-4073-9BE8-4EE3701B3504}.Release|Any CPU.Build.0 = Release|Any CPU
		{CB589043-28B4-46FB-9BC3-3591D9FF8C6D}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{CB589043-28B4-46FB-9BC3-3591D9FF8C6D}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{CB589043-28B4-46FB-9BC3-3591D9FF8C6D}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{CB589043-28B4-46FB-9BC3-3591D9FF8C6D}.Release|Any CPU.Build.0 = Release|Any CPU
		{F0906A93-243B-4BD0-A10F-FD6975F7DF10}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{F0906A93-243B-4BD0-A10F-FD6975F7DF10}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{F0906A93-243B-4BD0-A10F-FD6975F7DF10}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{F0906A93-243B-4BD0-A10F-FD6975F7DF10}.Release|Any CPU.Build.0 = Release|Any CPU
		{BB564CD2-68E0-4479-8DB1-4BA49901F25E}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{BB564CD2-68E0-4479-8DB1-4BA49901F25E}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{BB564CD2-68E0-4479-8DB1-4BA49901F25E}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{BB564CD2-68E0-4479-8DB1-4BA49901F25E}.Release|Any CPU.Build.0 = Release|Any CPU
		{005314CE-7AE5-422D-A90C-E2A4A9F29B02}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{005314CE-7AE5-422D-A90C-E2A4A9F29B02}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{005314CE-7AE5-422D-A90C-E2A4A9F29B02}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{005314CE-7AE5-422D-A90C-E2A4A9F29B02}.Release|Any CPU.Build.0 = Release|Any CPU
		{22B5AF7D-F6EC-47E1-8255-E17381AEF6F9}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{22B5AF7D-F6EC-47E1-8255-E17381AEF6F9}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{22B5AF7D-F6EC-47E1-8255-E17381AEF6F9}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{22B5AF7D-F6EC-47E1-8255-E17381AEF6F9}.Release|Any CPU.Build.0 = Release|Any CPU
		{81865144-6255-4828-B920-C494990E1380}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{81865144-6255-4828-B920-C494990E1380}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{81865144-6255-4828-B920-C494990E1380}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{81865144-6255-4828-B920-C494990E1380}.Release|Any CPU.Build.0 = Release|Any CPU
		{D03CF004-F9F0-4EA4-9DF8-7C5F0F5EEE85}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{D03CF004-F9F0-4EA4-9DF8-7C5F0F5EEE85}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{D03CF004-F9F0-4EA4-9DF8-7C5F0F5EEE85}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{D03CF004-F9F0-4EA4-9DF8-7C5F0F5EEE85}.Release|Any CPU.Build.0 = Release|Any CPU
		{E14C64C4-1972-49B4-AEF6-1B826B7E0E1C}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{E14C64C4-1972-49B4-AEF6-1B826B7E0E1C}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{E14C64C4-1972-49B4-AEF6-1B826B7E0E1C}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{E14C64C4-1972-49B4-AEF6-1B826B7E0E1C}.Release|Any CPU.Build.0 = Release|Any CPU
		{7C31A913-87D2-4A03-A6B4-B6578882DDA1}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{7C31A913-87D2-4A03-A6B4-B6578882DDA1}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{7C31A913-87D2-4A03-A6B4-B6578882DDA1}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{7C31A913-87D2-4A03-A6B4-B6578882DDA1}.Release|Any CPU.Build.0 = Release|Any CPU
		{767884F2-2324-4E58-BD44-210B6D339AC8}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{767884F2-2324-4E58-BD44-210B6D339AC8}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{767884F2-2324-4E58-BD44-210B6D339AC8}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{767884F2-2324-4E58-BD44-210B6D339AC8}.Release|Any CPU.Build.0 = Release|Any CPU
		{76F474F0-ABF9-45ED-B4DA-52411E5B7D2B}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{76F474F0-ABF9-45ED-B4DA-52411E5B7D2B}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{76F474F0-ABF9-45ED-B4DA-52411E5B7D2B}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{76F474F0-ABF9-45ED-B4DA-52411E5B7D2B}.Release|Any CPU.Build.0 = Release|Any CPU
		{A790A9C0-9557-4B01-80C4-3B8127E96C85}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{A790A9C0-9557-4B01-80C4-3B8127E96C85}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{A790A9C0-9557-4B01-80C4-3B8127E96C85}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{A790A9C0-9557-4B01-80C4-3B8127E96C85}.Release|Any CPU.Build.0 = Release|Any CPU
		{248E00B3-D637-46A0-9A34-50C0B9B15E5E}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{248E00B3-D637-46A0-9A34-50C0B9B15E5E}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{248E00B3-D637-46A0-9A34-50C0B9B15E5E}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{248E00B3-D637-46A0-9A34-50C0B9B15E5E}.Release|Any CPU.Build.0 = Release|Any CPU
		{9ACFD89D-1617-4BE5-99CB-0D29F14B1E6D}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{9ACFD89D-1617-4BE5-99CB-0D29F14B1E6D}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{9ACFD89D-1617-4BE5-99CB-0D29F14B1E6D}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{9ACFD89D-1617-4BE5-99CB-0D29F14B1E6D}.Release|Any CPU.Build.0 = Release|Any CPU
		{41D6FB86-BB30-4BA0-B571-4FC5F7461BD3}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{41D6FB86-BB30-4BA0-B571-4FC5F7461BD3}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{41D6FB86-BB30-4BA0-B571-4FC5F7461BD3}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{41D6FB86-BB30-4BA0-B571-4FC5F7461BD3}.Release|Any CPU.Build.0 = Release|Any CPU
		{0EF67E99-4BF5-40FA-A6D6-DAA6EC8DA8E7}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{0EF67E99-4BF5-40FA-A6D6-DAA6EC8DA8E7}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{0EF67E99-4BF5-40FA-A6D6-DAA6EC8DA8E7}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{0EF67E99-4BF5-40FA-A6D6-DAA6EC8DA8E7}.Release|Any CPU.Build.0 = Release|Any CPU
		{9D3F8A61-7FA6-4D05-9FBB-7F2ECFA5669A}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{9D3F8A61-7FA6-4D05-9FBB-7F2ECFA5669A}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{9D3F8A61-7FA6-4D05-9FBB-7F2ECFA5669A}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{9D3F8A61-7FA6-4D05-9FBB-7F2ECFA5669A}.Release|Any CPU.Build.0 = Release|Any CPU
		{E75D22ED-2FB4-440B-A343-F697A6D7324B}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{E75D22ED-2FB4-440B-A343-F697A6D7324B}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{E75D22ED-2FB4-440B-A343-F697A6D7324B}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{E75D22ED-2FB4-440B-A343-F697A6D7324B}.Release|Any CPU.Build.0 = Release|Any CPU
		{7157262D-FECB-4802-BF55-9629A1D17EC2}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{7157262D-FECB-4802-BF55-9629A1D17EC2}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{7157262D-FECB-4802-BF55-9629A1D17EC2}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{7157262D-FECB-4802-BF55-9629A1D17EC2}.Release|Any CPU.Build.0 = Release|Any CPU
		{ECDB0505-6712-485E-8983-A20E1EF99239}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{ECDB0505-6712-485E-8983-A20E1EF99239}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{ECDB0505-6712-485E-8983-A20E1EF99239}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{ECDB0505-6712-485E-8983-A20E1EF99239}.Release|Any CPU.Build.0 = Release|Any CPU
		{FE6E23DC-151B-4D55-BAD5-B97C561ED973}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{FE6E23DC-151B-4D55-BAD5-B97C561ED973}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{FE6E23DC-151B-4D55-BAD5-B97C561ED973}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{FE6E23DC-151B-4D55-BAD5-B97C561ED973}.Release|Any CPU.Build.0 = Release|Any CPU
		{2EF68AE3-819E-4FE4-8364-CD54375C2A9A}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{2EF68AE3-819E-4FE4-8364-CD54375C2A9A}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{2EF68AE3-819E-4FE4-8364-CD54375C2A9A}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{2EF68AE3-819E-4FE4-8364-CD54375C2A9A}.Release|Any CPU.Build.0 = Release|Any CPU
	EndGlobalSection
	GlobalSection(NestedProjects) = preSolution
		{9DE86BB4-7D8E-4997-BDCE-C5E7E30968AF} = {6114F446-78E7-49DC-BA34-C9904FE7838B}
		{E7E66DCC-7D68-4900-B09D-DE06E89DA534} = {B442AF5F-B127-45EF-B835-714A187D3F0A}
		{0F36E2E3-EEFC-4C74-88DF-AA281238F768} = {B442AF5F-B127-45EF-B835-714A187D3F0A}
		{EA9ECA12-F038-4437-8D08-34A61DC2DE50} = {B442AF5F-B127-45EF-B835-714A187D3F0A}
		{88560531-4322-49A6-BE34-91D70CF8CE5C} = {B442AF5F-B127-45EF-B835-714A187D3F0A}
		{CD120717-6AF0-4A13-A62F-9B86F23DD408} = {E9167F5F-E45B-4ABD-ACCD-89E3514BB0AA}
		{7366E7E8-283D-4772-9807-BDC55917B9F3} = {E9167F5F-E45B-4ABD-ACCD-89E3514BB0AA}
		{6114F446-78E7-49DC-BA34-C9904FE7838B} = {109EBFC9-4414-4331-AD7B-5C19A87CBF8B}
		{B442AF5F-B127-45EF-B835-714A187D3F0A} = {109EBFC9-4414-4331-AD7B-5C19A87CBF8B}
		{E9167F5F-E45B-4ABD-ACCD-89E3514BB0AA} = {109EBFC9-4414-4331-AD7B-5C19A87CBF8B}
		{B064C8A6-79AB-4B7B-98A6-A5F15635ED8D} = {109EBFC9-4414-4331-AD7B-5C19A87CBF8B}
		{F98F4F5C-DDF2-4756-A5EA-715DE0D22402} = {2F88D996-6A05-4BE0-A064-F7748E584090}
		{C751FBCB-B7AE-4ECE-BEDE-4A6600EC77D0} = {2F88D996-6A05-4BE0-A064-F7748E584090}
		{E5526B10-65CB-4619-A5C3-4C29A86D76A9} = {E9167F5F-E45B-4ABD-ACCD-89E3514BB0AA}
		{9FF8E353-1ACC-407A-A9B8-55183261A8C8} = {E9167F5F-E45B-4ABD-ACCD-89E3514BB0AA}
		{85E951AA-5333-4181-B5B1-305050405BFE} = {E9167F5F-E45B-4ABD-ACCD-89E3514BB0AA}
		{E033439A-DE1C-46D1-A33B-FBFA71812901} = {E9167F5F-E45B-4ABD-ACCD-89E3514BB0AA}
		{D014CF07-21C0-4783-B8BE-A2153289215A} = {E9167F5F-E45B-4ABD-ACCD-89E3514BB0AA}
		{63F7927D-D6F2-43EF-9E41-1C70C6911434} = {E9167F5F-E45B-4ABD-ACCD-89E3514BB0AA}
		{5FBC2CAC-E39A-4899-9CC1-94EF0712BDAE} = {B442AF5F-B127-45EF-B835-714A187D3F0A}
		{AD0D919C-8499-46A7-869E-EEB6456C6BA9} = {5FBC2CAC-E39A-4899-9CC1-94EF0712BDAE}
		{4B8223B4-1F0C-444C-88CE-B181D8277ACE} = {5FBC2CAC-E39A-4899-9CC1-94EF0712BDAE}
		{44B45E96-A286-44DC-A2F7-0E213005BDBF} = {5FBC2CAC-E39A-4899-9CC1-94EF0712BDAE}
		{F453B007-94DB-4F0B-B598-93D50B077C8F} = {E9167F5F-E45B-4ABD-ACCD-89E3514BB0AA}
		{971A1F55-C6D6-456C-A19A-772182DCE97F} = {E9167F5F-E45B-4ABD-ACCD-89E3514BB0AA}
		{529DB367-5C6D-4103-B0B5-9D540E84F88B} = {E9167F5F-E45B-4ABD-ACCD-89E3514BB0AA}
		{077E8C19-C1A4-4073-9BE8-4EE3701B3504} = {E9167F5F-E45B-4ABD-ACCD-89E3514BB0AA}
		{CB589043-28B4-46FB-9BC3-3591D9FF8C6D} = {E9167F5F-E45B-4ABD-ACCD-89E3514BB0AA}
		{BFB7ABD8-A1AC-41A9-B40B-C2F9389ABAF0} = {109EBFC9-4414-4331-AD7B-5C19A87CBF8B}
		{B132FA8E-B99A-420A-919D-5DA77555517C} = {109EBFC9-4414-4331-AD7B-5C19A87CBF8B}
		{A1B88082-6C3F-4A8E-89E7-ABFD08A5A89E} = {109EBFC9-4414-4331-AD7B-5C19A87CBF8B}
		{F0906A93-243B-4BD0-A10F-FD6975F7DF10} = {BFB7ABD8-A1AC-41A9-B40B-C2F9389ABAF0}
		{BB564CD2-68E0-4479-8DB1-4BA49901F25E} = {A1B88082-6C3F-4A8E-89E7-ABFD08A5A89E}
		{005314CE-7AE5-422D-A90C-E2A4A9F29B02} = {B132FA8E-B99A-420A-919D-5DA77555517C}
		{22B5AF7D-F6EC-47E1-8255-E17381AEF6F9} = {E9167F5F-E45B-4ABD-ACCD-89E3514BB0AA}
		{81865144-6255-4828-B920-C494990E1380} = {E9167F5F-E45B-4ABD-ACCD-89E3514BB0AA}
		{D03CF004-F9F0-4EA4-9DF8-7C5F0F5EEE85} = {E9167F5F-E45B-4ABD-ACCD-89E3514BB0AA}
		{E14C64C4-1972-49B4-AEF6-1B826B7E0E1C} = {B442AF5F-B127-45EF-B835-714A187D3F0A}
		{7C31A913-87D2-4A03-A6B4-B6578882DDA1} = {E9167F5F-E45B-4ABD-ACCD-89E3514BB0AA}
		{767884F2-2324-4E58-BD44-210B6D339AC8} = {E9167F5F-E45B-4ABD-ACCD-89E3514BB0AA}
		{77FDB1B2-4CDF-4787-AE38-5090B9101CE5} = {109EBFC9-4414-4331-AD7B-5C19A87CBF8B}
		{76F474F0-ABF9-45ED-B4DA-52411E5B7D2B} = {109EBFC9-4414-4331-AD7B-5C19A87CBF8B}
		{A790A9C0-9557-4B01-80C4-3B8127E96C85} = {77FDB1B2-4CDF-4787-AE38-5090B9101CE5}
		{248E00B3-D637-46A0-9A34-50C0B9B15E5E} = {77FDB1B2-4CDF-4787-AE38-5090B9101CE5}
		{9ACFD89D-1617-4BE5-99CB-0D29F14B1E6D} = {BFB7ABD8-A1AC-41A9-B40B-C2F9389ABAF0}
		{41D6FB86-BB30-4BA0-B571-4FC5F7461BD3} = {BFB7ABD8-A1AC-41A9-B40B-C2F9389ABAF0}
		{0EF67E99-4BF5-40FA-A6D6-DAA6EC8DA8E7} = {BFB7ABD8-A1AC-41A9-B40B-C2F9389ABAF0}
		{9D3F8A61-7FA6-4D05-9FBB-7F2ECFA5669A} = {B132FA8E-B99A-420A-919D-5DA77555517C}
		{E75D22ED-2FB4-440B-A343-F697A6D7324B} = {B132FA8E-B99A-420A-919D-5DA77555517C}
		{7157262D-FECB-4802-BF55-9629A1D17EC2} = {B132FA8E-B99A-420A-919D-5DA77555517C}
		{ECDB0505-6712-485E-8983-A20E1EF99239} = {A1B88082-6C3F-4A8E-89E7-ABFD08A5A89E}
		{FE6E23DC-151B-4D55-BAD5-B97C561ED973} = {A1B88082-6C3F-4A8E-89E7-ABFD08A5A89E}
		{2EF68AE3-819E-4FE4-8364-CD54375C2A9A} = {A1B88082-6C3F-4A8E-89E7-ABFD08A5A89E}
	EndGlobalSection
EndGlobal
```

## File: `MyCompany.ECommerce.sln.DotSettings`
```
﻿<wpf:ResourceDictionary xml:space="preserve" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" xmlns:s="clr-namespace:System;assembly=mscorlib" xmlns:ss="urn:shemas-jetbrains-com:settings-storage-xaml" xmlns:wpf="http://schemas.microsoft.com/winfx/2006/xaml/presentation">
	<s:Int64 x:Key="/Default/CodeStyle/CodeFormatting/CSharpFormat/BLANK_LINES_AFTER_BLOCK_STATEMENTS/@EntryValue">0</s:Int64>
	<s:String x:Key="/Default/CodeStyle/CodeFormatting/CSharpFormat/EMPTY_BLOCK_STYLE/@EntryValue">TOGETHER_SAME_LINE</s:String>
	<s:Int64 x:Key="/Default/CodeStyle/CodeFormatting/CSharpFormat/KEEP_BLANK_LINES_IN_CODE/@EntryValue">1</s:Int64>
	<s:Int64 x:Key="/Default/CodeStyle/CodeFormatting/CSharpFormat/KEEP_BLANK_LINES_IN_DECLARATIONS/@EntryValue">1</s:Int64>
	<s:String x:Key="/Default/CodeStyle/CodeFormatting/CSharpFormat/PLACE_ACCESSORHOLDER_ATTRIBUTE_ON_SAME_LINE_EX/@EntryValue">NEVER</s:String>
	<s:String x:Key="/Default/CodeStyle/CodeFormatting/CSharpFormat/PLACE_FIELD_ATTRIBUTE_ON_SAME_LINE_EX/@EntryValue">NEVER</s:String>
	<s:String x:Key="/Default/CodeStyle/Naming/CSharpNaming/Abbreviations/=EF/@EntryIndexedValue">EF</s:String>
	<s:String x:Key="/Default/CodeStyle/Naming/CSharpNaming/PredefinedNamingRules/=Interfaces/@EntryIndexedValue">&lt;Policy Inspect="True" Prefix="" Suffix="" Style="AaBb" /&gt;</s:String>
	<s:String x:Key="/Default/CodeStyle/Naming/CSharpNaming/PredefinedNamingRules/=PrivateStaticReadonly/@EntryIndexedValue">&lt;Policy Inspect="True" Prefix="" Suffix="" Style="AaBb_AaBb" /&gt;</s:String>
	<s:String x:Key="/Default/CodeStyle/Naming/CSharpNaming/UserRules/=15b5b1f1_002D457c_002D4ca6_002Db278_002D5615aedc07d3/@EntryIndexedValue">&lt;Policy&gt;&lt;Descriptor Staticness="Static" AccessRightKinds="Private" Description="Static readonly fields (private)"&gt;&lt;ElementKinds&gt;&lt;Kind Name="READONLY_FIELD" /&gt;&lt;/ElementKinds&gt;&lt;/Descriptor&gt;&lt;Policy Inspect="True" Prefix="" Suffix="" Style="AaBb_AaBb" /&gt;&lt;/Policy&gt;</s:String>
	<s:String x:Key="/Default/CodeStyle/Naming/CSharpNaming/UserRules/=a7a3339e_002D4e89_002D4319_002D9735_002Da9dc4cb74cc7/@EntryIndexedValue">&lt;Policy&gt;&lt;Descriptor Staticness="Any" AccessRightKinds="Any" Description="Interfaces"&gt;&lt;ElementKinds&gt;&lt;Kind Name="INTERFACE" /&gt;&lt;/ElementKinds&gt;&lt;/Descriptor&gt;&lt;Policy Inspect="True" Prefix="" Suffix="" Style="AaBb" /&gt;&lt;/Policy&gt;</s:String>
	<s:String x:Key="/Default/Environment/InlayHints/CSharpTypeNameHintsOptions/ShowMethodReturnTypeNameHints/@EntryValue">Default</s:String>
	<s:String x:Key="/Default/Environment/InlayHints/CSharpTypeNameHintsOptions/ShowTypeNameHintsForImplicitlyTypedVariables/@EntryValue">PushToShowHints</s:String>
	<s:Boolean x:Key="/Default/Environment/SettingsMigration/IsMigratorApplied/=JetBrains_002EReSharper_002EPsi_002ECSharp_002ECodeStyle_002ECSharpKeepExistingMigration/@EntryIndexedValue">True</s:Boolean>
	<s:Boolean x:Key="/Default/Environment/SettingsMigration/IsMigratorApplied/=JetBrains_002EReSharper_002EPsi_002ECSharp_002ECodeStyle_002ECSharpPlaceEmbeddedOnSameLineMigration/@EntryIndexedValue">True</s:Boolean>
	<s:Boolean x:Key="/Default/Environment/SettingsMigration/IsMigratorApplied/=JetBrains_002EReSharper_002EPsi_002ECSharp_002ECodeStyle_002ECSharpUseContinuousIndentInsideBracesMigration/@EntryIndexedValue">True</s:Boolean>
	<s:Boolean x:Key="/Default/Environment/SettingsMigration/IsMigratorApplied/=JetBrains_002EReSharper_002EPsi_002ECSharp_002ECodeStyle_002ESettingsUpgrade_002EMigrateBlankLinesAroundFieldToBlankLinesAroundProperty/@EntryIndexedValue">True</s:Boolean>
	<s:Boolean x:Key="/Default/Environment/SettingsMigration/IsMigratorApplied/=JetBrains_002EReSharper_002EPsi_002ECSharp_002ECodeStyle_002ESettingsUpgrade_002EPredefinedNamingRulesToUserRulesUpgrade/@EntryIndexedValue">True</s:Boolean>
	<s:Boolean x:Key="/Default/UserDictionary/Words/=ITLIBRIUM/@EntryIndexedValue">True</s:Boolean>
	<s:Boolean x:Key="/Default/UserDictionary/Words/=Shouldly/@EntryIndexedValue">True</s:Boolean></wpf:ResourceDictionary>
```

## File: `Projects-and-Namespaces.md`
```markdown
# *Projects* and *Namespaces*

1. All names should be as short as possible and without information noise.
2. Company / product name should be present in: *Solution name* (*MyCompany.Crm*), *Assembly name* (*MyCompany.CRM.Sales.Domain.dll*), *Root namespace* (*MyCompany.CRM.Sales*), but it's better not to add it to the project name (*Sales*).
3. The project name should starts with the *Bounded Context* name (*Sales* or *Sales.Adapters.RestApi*).
4. Projects should reflect architectural divisions (e.g. project per layer). Relations between projects should follow used architectural style.
5. Projects should expose only what is actually needed. By default, *internal* visibility should be used instead of *public*.
6. *Namespaces* should tell a business story, not a technical one. They should starts with the name of the company / product followed by the name of the *Bounded Context*. The rest of the namespace should reflect the hierarchical division into *Modules* (*MyCompany.CRM.Sales.Orders*).
7. *Namespace* **should not** contain names reflecting architectural divisions that are already present in project names (*.Domain*, *.Adapters.Sql*).

Thanks to this approach just a glance at *Solution Explorer* gives us a lot of information about the system and the business. The names of all components are as short as possible, which makes navigation much easier. In addition, each technical element of the code has a clear responsibility and you know what kind of information you can expect from it. The system is divided hierarchically according to the divisions in the business.
```

## File: `README.md`
```markdown
# *DDD* starter for *.net*

## About

**This repository allows to quickly start a *DDD* oriented project in *C#*** selecting a combination of *DDD*-related technologies which is right for your needs. *Hexagonal Architecture*, *BDD*, *CQRS*, *Event Sourcing* - to not overengineer your project you often need only part of them. Here we show you **various implementation options** with **guidelines** which should help you make a smart choice and start coding.

### What *DDD starter* is?

It's a **place to learn** how to implement *DDD*, *CQRS*, *Event Sourcing*, *Hexagonal Architecture*, *BDD*, etc.

It's a **comparison of different implementations styles** that can be used to solve the same requirement.

It's a **set of ready made solutions** that you can adapt in your own projects.

### What *DDD starter* is not?

It's **not a complete study of some domain**. 

It's **not an ilustration of domain exploration** or **modeling process**.

It's **not a complete comparison** of all possible implementation styles.

### The goal

The main goal of this project is to show different implementation options for a *DDD* project and share some best practices for each of them. Which approach is the best and should be chosen? It all depends! ;) Depends on what? Probably on some drivers from the context you operate in. So we also give you here some tips about how the available options match different drivers. We hope it will allow you to quickly make a good choice and get some productivity boost.


### **IMPORTANT DISCLAIMER** 
**Remember that DDD is not about implementation!** It is *"just"* a lightweight technique of creating a model for your software using exactly the same language as your business. This model can be more or less complex depending on the business itself. **There is no point in using a pneumatic drill where a simple hammer will do the job** (even if the pneumatic drill is very shiny). **Do not even try to use all most advanced DDD technologies (like Event Sourcing) without a proper reflection**.

### Our approach

#### Limiting the domain to a minimum

It is impractical to present the process of domain exploration and modeling as well as various approaches to implementation at once. That's why we decided to limit the domain to an absolute minimum so that we could present implementation techniques of particular patterns.

This limitation will mainly concern the number of domain concepts and to a lesser degree their complexity as this is necessary for meaningful use of the presented patterns.

#### Simplicity

The code is read much more often than it is modified. The implementation should therefore primarily be optimized for readability. In addition, the code is usually read by someone other than its author, so it is worth to ensure that the learning curve is as flat as possible.

We will try to make all presented solutions as easy as possible. The different options will of course vary in complexity. This will be an additional illustration of trade-offs between brevity and simplicity: what is gaining and what is lost by choosing more generic / automatic / magical solutions.

Simplicity, however, does not mean simplifications that we will try to avoid at all costs. Simplified solutions are usually not suitable for use in a real projects. They also require additional knowledge to distinguish what is essential from what is merely a simplification.

#### Minimum technical dependencies

Discussed patterns are not strictly related to any technology, therefore the project will not be written from the perspective of a specific set of technologies or cloud provider.

The only limitation is the choice of .net platform and C # language.

Chosen libraries and technologies are optimal choices from the perspective of  authors' experience. All of them can be easily replaced with analogical solutions while maintaining the essence of the implemented patterns.

## Project development

This project is under development so we encourage you to follow:

1. This site - give us a Star
2. Our blog: https://itlibrium.com/blog?tag=DDD-starter
3. Twitter: [ITLIBRIUM](https://twitter.com/itlibrium), [Marcin](https://twitter.com/technites_pl), [Szymon](https://twitter.com/szjanikowski)

## Table of contents

### Screaming architecture

To create this solution we used an architectural approach called *screaming architecture*. This means that the structure of the solution "screams" about the business domain and architectural choices. Bounded Contexts are mapped to solution folders, application architecture layers are in separate projects, namespaces hierarchy follows business divisions.

**Documentation:**

1. [Projects and namespaces conventions](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Projects-and-Namespaces.md)

**Blog:**

1. [How to use c# projects and *namespaces* in a DDD project](https://itlibrium.com/en/blog/how-to-use-csharp-projects-and-namespaces-in-a-ddd-project)

### Hexagonal Architecture

Hexagonal Architecture is used in a part of `Sales` Bounded Context.

This architecture style is best for Deep Model with high business complexity. It's a very rare situation when it's the best choice for the architecture of the whole system. When used for CRUD part of the system it only adds unnecessary, accidental complexity. That's why we used it only in a part of the system. The rest of `Sales` and whole `Contacts` Bounded Context is rather simple with only CRUD operations. For these parts simple single layer architecture was chosen.

**Code:**

1. [`Sales` Bounded Context](https://github.com/itlibrium/DDD-starter-dotnet/tree/master/Sources/Sales)

**Blog:**

1. [[PL] Architektura wspierająca podejście *Domain First*](https://itlibrium.com/architektura-wspierajaca-podejscie-domain-first/)

### DDD Building Blocks

#### Aggregate

**Code:**

1. Complex aggregate: [`Order`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel/Orders/Order.cs)
2. Aggregate's private Value Object: [`PriceAgreement`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel/Orders/Order.PriceAgreement.cs)
3. Aggregate's events: [`Order.Events`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel/Orders/Order.Events.cs)
4. Aggregate's snapshot: [`Order.Snapshot`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel/Orders/Order.Snapshot.cs)

**Blog:**

1. [[PL] Identyfikowanie obiektów domenowych](https://itlibrium.com/identyfikowanie-obiektow-domenowych/)

#### Value Object

**Code:**

1. Identifiers eg: [`OrderId`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel/Orders/OrderId.cs), [`ProductId`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel/Products/ProductId.cs)
2. Simple quantities (often with operators facilitating calculations) eg: [`Amount`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel/Products/Amount.cs), [`ProductAmount`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel/Products/ProductAmount.cs), [`Money`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel/Commons/Money.cs)
3. Complex quantities (often used by Policies) eg: [`Offer`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel/Pricing/Offer.cs), [`Quote`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel/Pricing/Quote.cs)
4. Other domain concepts (often used for communication between other Building Blocks) eg: [`OfferRequest`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel/Pricing/OfferRequest.cs), [`BasePrice`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel/Pricing/PriceLists/BasePrice.cs)

**Blog:**

1. [[PL] Jak zaimplementować Value Object z DDD w C#](https://itlibrium.com/value-object-w-csharp/)

#### Policy

**Code:**

1. Calculations eg: [`OfferModifier`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel/Pricing/OfferModifier.cs), [`ClientLevelDiscount`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel/Pricing/Discounts/ClientLevelDiscounts.cs), [`SpecialOffer`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel/Pricing/SpecialOffers/SpecialOffer.cs)
2. Adjusting Aggregate's rules eg: [`PriceChangesPolicy`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel/Orders/PriceChanges/PriceChangesPolicy.cs), [`AllowPriceChangesIfTotalPriceIsLower`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel/Orders/PriceChanges/AllowPriceChangesIfTotalPriceIsLower.cs)

**Blog:**

1. [[PL] Jak zaimplementować Polityki z DDD w C#](https://itlibrium.com/polityki-z-ddd-w-csharp/)

#### Factory

**Code:**

1. Creating Aggregates and Value Object: factory methods on each type
2. Choosing Policy for given conditions: [`PriceChangesPolicies`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel/Orders/PriceChanges/PriceChangesPolicies.cs), [`OfferModifiers`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel/Pricing/OfferModifiers.cs)

#### Domain Service

**Code:**

1. Domain sub-processes: [`CalculatePrices`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel/Pricing/CalculatePrices.cs)

### Emitting Events from Aggregates

**Code:**

1. List inside Aggregate: [`Order.NewEvents`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel/Orders/Order.Events.cs)

Alternatives that won't be implemented:

1. static event publisher - hard to test Aggregates
2. passing event publisher to aggregate
   1. through constructor - hard to restore Aggregates
   2. through method argument - technical language in business behaviors
3. returning events from Aggregate's methods - harder implementation if method can return not only single Event; Events have to be passed as arguments to Repository methods which in less intuitive than passing Aggregate itself

### Testing domain model

**Code:**

1. [Tests for `Money` Value Object](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel.Tests/Commons/MoneyTests.cs)

**Tools:**

1. [BDD toolkit](https://github.com/itlibrium/BDD-toolkit-dotnet) - our another open source project

### Combining *DDD* and *CRUD*

Even in a single Bounded Context we often find parts with different complexity. Some part of the Bounded Context may require Deep Model and techniques like Hexagonal Architecture and DDD Building Blocks. At the same time, another part may need CRUD model where single or two-layered architecture (using frameworks and libraries as much as possible) is the best fit. 

Using completely separate styles - Hexagonal Architecture for the Deep part and single/two layered architecture for CRUD part - is possible only if there are no use cases where we need to operate on both models. It's only a mater of time when such a use case occurs. What then? Which architecture style should be used?

The solution we propose is to use flexible Hexagonal Architecture, but avoid usage of OOP and Tactical DDD patterns for the CRUD parts. Check out the Sales Bounded Context where we show it in action. You can also check the Contacts Bounded Context where we show sample CRUD model implementation which is kept as simple as possible.

**Code:**

1. CRUD Bounded Context with single layer architecture eg: [`Contacts`](https://github.com/itlibrium/DDD-starter-dotnet/tree/master/Sources/Contacts)
2. Bounded Context with Deep Model and CRUD Model eg: [`Sales`](https://github.com/itlibrium/DDD-starter-dotnet/tree/master/Sources/Sales)
   1. Separation rules (Aggregate) and simple data (Anemic Entity / Data Structure) eg: [`Order`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel/Orders/Order.cs) - [`OrderHeader`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.DeepModel/Orders/OrderHeader.cs)
   2. Saving both Deep Model and CRUD Model in Command Handler (single transaction) eg: , [`PlaceOrderHandler`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.ProcessModel/OnlineSale/OrderPlacement/PlaceOrderHandler.cs), [`CreateOrderHandler`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.ProcessModel/Wholesale/OrderCreation/CreateOrderHandler.cs)
   3. Reading CRUD Model in Command Handler eg: , [`ConfirmOfferHandler`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.ProcessModel/Wholesale/OrderPricing/ConfirmOfferHandler.cs), [`GetOfferHandler`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.ProcessModel/Wholesale/OrderPricing/GetOfferHandler.cs), [`SalesCrudOperations`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.ProcessModel/SalesCrudOperations.cs)
   4. Managing CRUD Model without Command Handler eg: [`WholesalesOrdersHeaderController`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.RestApi/Wholesales/WholesalesOrdersHeaderController.cs), [`WholesalesOrdersHeaderNotesController`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.RestApi/Wholesales/WholesalesOrdersHeaderNotesController.cs), [`SalesCrudOperations`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.Crud.Contracts/SalesCrudOperations.cs)

### Persistence of Aggregates

Domain model can be persisted in a several ways using SQL and noSQL databases. Here we compare various approaches by providing an example implementation for each of them.

**Code:**

1. SQL
   1. Entity Framework: [`OrderSqlRepository.EF`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.Adapters/Orders/OrderSqlRepository.EF.cs)
   2. Raw SQL: [`OrderSqlRepository.Raw`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.Adapters/Orders/OrderSqlRepository.Raw.cs)
   3. Document with Marten: [`OrderSqlRepository.Document`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.Adapters/Orders/OrderSqlRepository.Document.cs)
   4. Event Sourcing with Marten: [`OrderSqlRepository.EventsSourcing`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.Adapters/Orders/OrderSqlRepository.EventsSourcing.cs)
2. Transactions: [`AmbientTransactionDecorator`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/TechnicalStuff/TechnicalStuff.Transactions/AmbientTransactionDecorator.cs), ['ExplicitTransactionDecorator'](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/TechnicalStuff/TechnicalStuff.Transactions/ExplicitTransactionDecorator.cs)

**Blog:**

1. [[PL] 4 sposoby persystencji agregatow DDD](https://itlibrium.com/4-sposoby-persystencji-agregatow-ddd/)

### Publishing Events

**Code:**

1. In a single transaction with domain model using *Outbox Pattern*
   1. Base abstractions: [`TransactionalOutbox`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/TechnicalStuff/TechnicalStuff.Outbox/TransactionalOutbox.cs), [`TransactionalOutboxes`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/TechnicalStuff/TechnicalStuff.Outbox/TransactionalOutboxes.cs)
   2. Integration with Use Case lifetime: [`TransactionalMessageSendingDecorator`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/TechnicalStuff/TechnicalStuff.Outbox/TransactionalMessageSendingDecorator.cs)
   3. Particular Outbox as a Port in Use Cases layer: [`OrderEventsOutbox`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.ProcessModel/OrderEventsOutbox.cs)
   4. Publishing Outbox to Event Broker: coming soon   
2. Post Commit
   1. Base abstractions: [`NonTransactionalOutbox`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/TechnicalStuff/TechnicalStuff.Outbox/NonTransactionalOutbox.cs), [`NonTransactionalOutboxes`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/TechnicalStuff/TechnicalStuff.Outbox/NonTransactionalOutboxes.cs)
   2. Integration with *Use Case* lifetime: [`NonTransactionalMessageSendingDecorator`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/TechnicalStuff/TechnicalStuff.Outbox/NonTransactionalMessageSendingDecorator.cs)
   3. Particular Outbox as a Port in Use Cases layer: coming soon   
3. Pre Commit - In our  opinion it's not very useful approach in real world scenarios.

### Testing integration with infrastructure

**Code:**

1. Integration tests for DDD Repository and SQL database: [`OrderSqlRepositoryTests`](https://github.com/itlibrium/DDD-starter-dotnet/blob/master/Sources/Sales/Sales.IntegrationTests/Orders/OrderSqlRepositoryTests.cs)

### Startup

We prefer to put all the startup code in a separate project. This project *know* about everything but *does* only initialization including:

- parsing and merging configuration
- registering all components in dependency injection container
- composing framework components like `middlewares`

In our opinion it's a better approach compared to putting startup code into the project with API code. It's especially useful in a modular monolith because each of the modules can have its own, separate API and use its own set of dependencies.

**Code:**

1. [Startup project](https://github.com/itlibrium/DDD-starter-dotnet/tree/master/Sources/Startup)

### What's next?

If you thought of something we can implement in this repo to make it even more useful for your projects let us know! We are looking forward for your feedback and ideas for new example implementations. 

Good luck with implementing DDD in your projects!

## License

The project is under [MIT license](https://opensource.org/licenses/MIT).
```

## File: `build.cmd`
```
:; set -eo pipefail
:; SCRIPT_DIR=$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)
:; ${SCRIPT_DIR}/build.sh "$@"
:; exit $?

@ECHO OFF
powershell -ExecutionPolicy ByPass -NoProfile -File "%~dp0build.ps1" %*
```

## File: `build.ps1`
```powershell
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

$BuildProjectFile = "$PSScriptRoot\Build\Nuke\Nuke.csproj"
$TempDirectory = "$PSScriptRoot\\.nuke\temp"

$DotNetGlobalFile = "$PSScriptRoot\\global.json"
$DotNetInstallUrl = "https://dot.net/v1/dotnet-install.ps1"
$DotNetChannel = "Current"

$env:DOTNET_SKIP_FIRST_TIME_EXPERIENCE = 1
$env:DOTNET_CLI_TELEMETRY_OPTOUT = 1
$env:DOTNET_MULTILEVEL_LOOKUP = 0

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
}

Write-Output "Microsoft (R) .NET SDK version $(& $env:DOTNET_EXE --version)"

ExecSafe { & $env:DOTNET_EXE build $BuildProjectFile /nodeReuse:false /p:UseSharedCompilation=false -nologo -clp:NoSummary --verbosity quiet }
ExecSafe { & $env:DOTNET_EXE run --project $BuildProjectFile --no-build -- $BuildArguments }
```

## File: `build.sh`
```bash
#!/usr/bin/env bash

bash --version 2>&1 | head -n 1

set -eo pipefail
SCRIPT_DIR=$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)

###########################################################################
# CONFIGURATION
###########################################################################

BUILD_PROJECT_FILE="$SCRIPT_DIR/Build/Nuke/Nuke.csproj"
TEMP_DIRECTORY="$SCRIPT_DIR//.nuke/temp"

DOTNET_GLOBAL_FILE="$SCRIPT_DIR//global.json"
DOTNET_INSTALL_URL="https://dot.net/v1/dotnet-install.sh"
DOTNET_CHANNEL="Current"

export DOTNET_CLI_TELEMETRY_OPTOUT=1
export DOTNET_SKIP_FIRST_TIME_EXPERIENCE=1
export DOTNET_MULTILEVEL_LOOKUP=0

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
fi

echo "Microsoft (R) .NET SDK version $("$DOTNET_EXE" --version)"

"$DOTNET_EXE" build "$BUILD_PROJECT_FILE" /nodeReuse:false /p:UseSharedCompilation=false -nologo -clp:NoSummary --verbosity quiet
"$DOTNET_EXE" run --project "$BUILD_PROJECT_FILE" --no-build -- "$@"
```

## File: `Build/Nuke/AssemblyInfo.cs`
```csharp
using NoesisVision.Annotations;

[assembly: ExcludeFromDocs]
```

## File: `Build/Nuke/Build.Parameters.cs`
```csharp
using System;
using Nuke.Common;

namespace MyCompany.ECommerce.Nuke;

public partial class Build
{
    [Parameter("Configuration to build - Default is 'Debug' (local) or 'Release' (server)")]
    public static string BuildConfiguration { get; private set; } = IsLocalBuild
        ? "Debug"
        : "Release";

    [Parameter]
    public static string ExecutingUser { get; private set; } = "1000";

    [Parameter]
    public static Environment Environment
    {
        get
        {
            if (!_environment.Equals(Environment.Undefined))
                return _environment;
            if (!AspNetCoreEnvironment.Equals(Environment.Undefined))
                return AspNetCoreEnvironment;
            if (!DotNetEnvironment.Equals(Environment.Undefined))
                return DotNetEnvironment;
            return Environment.Development;
        }
        private set
        {
            if (value.Equals(Environment.Undefined))
                throw new ArgumentException(
                    $"{nameof(Environment)} can not be set to {Environment.Undefined}");
            _environment = value;
        }
    }

    private static Environment _environment = Environment.Undefined;

    [Parameter]
    public static Environment DotNetEnvironment { get; private set; } = Environment.Undefined;

    [Parameter]
    public static Environment AspNetCoreEnvironment { get; private set; } = Environment.Undefined;
}
```

## File: `Build/Nuke/Build.Targets.cs`
```csharp
using JetBrains.Annotations;
using MyCompany.ECommerce.Nuke.Certs;
using MyCompany.ECommerce.Nuke.DockerCompose;
using MyCompany.ECommerce.Nuke.DotNet;
using MyCompany.ECommerce.Nuke.Elastic;
using Nuke.Common;

namespace MyCompany.ECommerce.Nuke;

public partial class Build
{
    [PublicAPI]
    public Target CleanBin => DotNetTargets.CleanBin;

    [PublicAPI]
    public Target Restore => DotNetTargets.Restore;

    [PublicAPI]
    public Target Compile => DotNetTargets.Compile;

    [PublicAPI]
    public Target RunIntegrationTestsOnLocalDockerInfrastructure =>
        DotNetTargets.RunIntegrationTestsOnLocalDockerInfrastructure;

    [PublicAPI]
    public Target ApplyMigrationsOnLocalDockerInfrastructure =>
        EntityFrameworkTargets.ApplyMigrationsOnLocalDockerInfrastructure;

    [PublicAPI]
    public Target StartLocalDockerInfrastructure => DockerComposeTargets.StartLocalDockerInfrastructure;

    [PublicAPI]
    public Target StopLocalDockerInfrastructure => DockerComposeTargets.StopLocalDockerInfrastructure;

    [PublicAPI]
    public Target CleanLocalDockerInfrastructure => DockerComposeTargets.CleanLocalDockerInfrastructure;
        
    [PublicAPI]
    public Target DisplayLocalDockerInfrastructureLogs => DockerComposeTargets.DisplayLocalDockerInfrastructureLogs;
        
    [PublicAPI]
    public Target PrepareCertificates => CertsTargets.PrepareCertificates;

    [PublicAPI]
    public Target CleanCertificates => CertsTargets.CleanCertificates;

    [PublicAPI]
    public Target CreateElasticUsers => ElasticTargets.CreateElasticUsers;

    [PublicAPI]
    public Target CleanElasticUsers => ElasticTargets.CleanElasticUsers;
}
```

## File: `Build/Nuke/Build.cs`
```csharp
using Nuke.Common;
using Nuke.Common.Execution;
using Nuke.Common.ProjectModel;

namespace MyCompany.ECommerce.Nuke;

[UnsetVisualStudioEnvironmentVariables]
public partial class Build : NukeBuild
{
    public static int Main() => Execute<Build>(x => x.Compile);

    [Solution]
    public static Solution Solution { get; private set; }
        
    // [GitRepository] readonly GitRepository GitRepository;
    // [GitVersion] readonly GitVersion GitVersion;
}
```

## File: `Build/Nuke/Environment.cs`
```csharp
using System.ComponentModel;
using Nuke.Common.Tooling;

namespace MyCompany.ECommerce.Nuke;

[TypeConverter(typeof(TypeConverter<Environment>))]
public class Environment : Enumeration
{
    public static Environment Undefined = new() { Value = nameof(Undefined) };
    public static Environment Development = new() { Value = nameof(Development) };
    public static Environment Test = new() { Value = nameof(Test) };
    public static Environment Production = new() { Value = nameof(Production) };

    public static bool EnvironmentIs(Environment environment) => Build.Environment.Equals(environment);
        
    public static implicit operator string(Environment environment) => environment.Value;
}
```

## File: `Build/Nuke/Nuke.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <NoWarn>CS0649;CS0169</NoWarn>
    <UserSecretsId>MyCompanyCrm</UserSecretsId>
    <AssemblyName>MyCompany.ECommerce.Nuke</AssemblyName>
    <RootNamespace>MyCompany.ECommerce.Nuke</RootNamespace>
    <NukeTelemetryVersion>1</NukeTelemetryVersion>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
    <PackageReference Include="Microsoft.EntityFrameworkCore" Version="8.0.5" />
    <PackageReference Include="Microsoft.Extensions.Configuration" Version="8.0.0" />
    <PackageReference Include="Microsoft.Extensions.Configuration.Abstractions" Version="8.0.0" />
    <PackageReference Include="Microsoft.Extensions.Configuration.Binder" Version="8.0.1" />
    <PackageReference Include="Microsoft.Extensions.Configuration.CommandLine" Version="8.0.0" />
    <PackageReference Include="Microsoft.Extensions.Configuration.EnvironmentVariables" Version="8.0.0" />
    <PackageReference Include="Microsoft.Extensions.Configuration.Json" Version="8.0.0" />
    <PackageReference Include="Microsoft.Extensions.Configuration.UserSecrets" Version="8.0.0" />
    <PackageReference Include="Npgsql" Version="8.0.3" />
    <PackageReference Include="Nuke.Common" Version="8.0.0" />
    <PackageDownload Include="GitVersion.Tool" Version="[5.1.1]" />
    <PackageReference Include="Polly" Version="8.4.0" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\Nuke.DockerCompose\Nuke.DockerCompose.csproj" />
  </ItemGroup>

</Project>
```

## File: `Build/Nuke/Nuke.csproj.DotSettings`
```
﻿<wpf:ResourceDictionary xml:space="preserve" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" xmlns:s="clr-namespace:System;assembly=mscorlib" xmlns:ss="urn:shemas-jetbrains-com:settings-storage-xaml" xmlns:wpf="http://schemas.microsoft.com/winfx/2006/xaml/presentation">
	<s:String x:Key="/Default/CodeInspection/CSharpLanguageProject/LanguageLevel/@EntryValue">Experimental</s:String></wpf:ResourceDictionary>
```

## File: `Build/Nuke/Paths.cs`
```csharp
using Nuke.Common;
using Nuke.Common.IO;

namespace MyCompany.ECommerce.Nuke;

public static class Paths
{
    public static readonly AbsolutePath SourcesDirectory = NukeBuild.RootDirectory / "Sources";
    public static readonly AbsolutePath NukeDirectory = NukeBuild.RootDirectory / "Build" / "Nuke";
        
    public static readonly AbsolutePath ArtifactsDirectory = NukeDirectory / "Artifacts";
    public static readonly AbsolutePath BinDirectory = ArtifactsDirectory / "Bin";
        
    public static readonly AbsolutePath StartupProjectFile = SourcesDirectory / "Monolith.Startup" / "Monolith.Startup.csproj";
}
```

## File: `Build/Nuke/Settings.cs`
```csharp
using Microsoft.Extensions.Configuration;
using MyCompany.ECommerce.Nuke.Elastic;
using MyCompany.ECommerce.Nuke.Helpers;
using MyCompany.ECommerce.Nuke.Postgres;
using static MyCompany.ECommerce.Nuke.Paths;

namespace MyCompany.ECommerce.Nuke;

public static class Settings
{
    public static ElasticSettings Elastic { get; }
    public static PostgresSettings Postgres { get; }

    static Settings()
    {
        var configurationRoot = GetConfigurationRoot(Build.Environment);
        Elastic = configurationRoot.GetSection(ElasticSettings.Key).Get<ElasticSettings>();
        Postgres = configurationRoot.GetSection(PostgresSettings.Key).Get<PostgresSettings>();
    }

    private static IConfigurationRoot GetConfigurationRoot(Environment environment)
    {
        const string secretsId = "MyCompanyCrm";
        const string environmentVariablesPrefix = "MYCOMPANY_CRM_";
        var configurationBuilder = new ConfigurationBuilder()
            .AddJsonFile(NukeDirectory / "settings.json", optional: true, reloadOnChange: false)
            .AddJsonFile(NukeDirectory / $"settings.{environment.ValueToLower()}.json", true, false);
        if (environment.Equals(Environment.Development))
            configurationBuilder.AddUserSecrets(secretsId);
        configurationBuilder.AddEnvironmentVariables(environmentVariablesPrefix);
        return configurationBuilder.Build();
    }
}
```

## File: `Build/Nuke/settings.development.json`
```json
{
}
```

## File: `Build/Nuke/settings.json`
```json
{
  "Elastic": {
    "ElasticsearchVersion": "7.7.0",
    "ElasticsearchConfigDirectory": "/usr/share/elasticsearch/config",
    "SuperUserName": "admin",
    "KibanaVersion": "7.7.0",
    "KibanaConfigDirectory": "/usr/share/kibana/config",
    "Kibana01UserName": "kibana01"
  },
  "Postgres": {
    "ConnectionString": "Server=localhost;Port=5432;User Id=postgres;Password=password;Timeout=3;"
  }
}
```

## File: `Build/Nuke/Certs/CertsTargets.cs`
```csharp
using System;
using Nuke.Common;
using Nuke.Common.IO;
using static Nuke.Common.IO.FileSystemTasks;
using static MyCompany.ECommerce.Nuke.Environment;
using static MyCompany.ECommerce.Nuke.Paths;

namespace MyCompany.ECommerce.Nuke.Certs;

public static class CertsTargets
{
    public static readonly AbsolutePath CertsDirectory = ArtifactsDirectory / "Certs";
    private static readonly AbsolutePath DevCertsDirectory = NukeDirectory / "Certs" / "DevCerts";

    public static Target PrepareCertificates => _ => _
        .Executes(() =>
        {
            if (EnvironmentIs(Development))
            {
                if (!CertsDirectory.DirectoryExists())
                    CopyDirectoryRecursively(DevCertsDirectory, CertsDirectory);
            }
            else
            {
                throw new NotImplementedException();
            }
        });
        
    public static Target CleanCertificates => _ => _
        .Executes(() =>
        {
            if (EnvironmentIs(Development))
            {
                if (CertsDirectory.DirectoryExists())
                    DeleteDirectory(CertsDirectory);
            }
            else
            {
                throw new NotImplementedException();
            }
        });
}
```

## File: `Build/Nuke/Certs/DevCerts/CA/ca.crt`
```
-----BEGIN CERTIFICATE-----
MIIFRjCCAy6gAwIBAgIIc3knYDcFy2wwDQYJKoZIhvcNAQENBQAwKDESMBAGA1UE
ChMJTXlDb21wYW55MRIwEAYDVQQDEwlNeUNvbXBhbnkwIBcNMjAwNDI5MDcyNDAw
WhgPMjEyMDA0MjkwNzI0MDBaMCgxEjAQBgNVBAoTCU15Q29tcGFueTESMBAGA1UE
AxMJTXlDb21wYW55MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAxRjB
rVhACvWo/v1LT8pNib5rNyTK19wAMMFG3fpvYHQu5yy4o8CnfKG7oRUwh2Ar+m1/
vCmgbyTJdzu9FAbT7QqfY5Ltrk3+7t1feA2qekJUPDl/y4kqQZU5aZemluWcQoiz
gg8m2sgriIxl92fkKrw8+CytVsl14/KnPwXiVkd/S7nCZVb0/rQVC1WFh09alOdT
PWvGPws79khoEpAYVLXs3EwcgL3DmqT22gcRiwVZUzDiMGmT3vXxnEg49ENFKgNo
ImDnSvNFBhTIUoDFduw6vgEnTpuTZe134c39njRuhO9FyULl0NJCcpkoOEB/k0Gp
nz9bCS7D7MujZ+B/pz2wLMCJ6PP4i43epUjL1aAlGA+vUosTgBD/dv19jvWscVWN
8ayTeqeryA59kASm8+vNYi9HXWTRmdsCB+K2hzJ9rRePZXVYru7sS/FONU1Y4skF
Z/KKd/M4P984OcaHOnaYUmoScvcsQEG9d9U1BVmktApXgzWXQupyHcF08gj1vwR3
83fLPYHxCeHPU46ls0KKcaRdILy+n94cJ+SokWjMqEiTQk4NYDnlFbiasGIGPfXn
ZitV2txflGsmA9M3u7UyT9GBAZctu9JOAXdEj400ZAo3VU/4TJcioKxbFyjfoPVG
FBjG/pqFmn6wYGpwzlXOfAKsW5Tck6ORh7bVNvkCAwEAAaNyMHAwDwYDVR0TAQH/
BAUwAwEB/zAdBgNVHQ4EFgQUGywZIbUfqYGZvdR/3tPVILm+J7kwCwYDVR0PBAQD
AgEGMBEGCWCGSAGG+EIBAQQEAwIABzAeBglghkgBhvhCAQ0EERYPeGNhIGNlcnRp
ZmljYXRlMA0GCSqGSIb3DQEBDQUAA4ICAQBS7hgZjln1vQR0ftQNonOD4rVOu1na
Y1fP+eSxyROIu1E1+rJzfqOuPhjCAgshKw1tM97emFlIRBQqgqTX7sARKFScgFUc
K8nNTZET+oRH7/mn1WiJqotQrRS3qO59V29Cs569h8QmHcnHTxGVFvvkhjys4n/i
LPIb5/RAdet9CB6cUSH8l7gBpJf7KmnCZ/O1La8ILjvXDsV4fFLWDuOjo/D2VazK
wngPo8158UxxeSKQz2ihIXjp/6EcFKOC4EVi78LMh//uK2e9nr1Ck4aHVCu2y2yV
FlQb1Zafp3KWwO+Bcndqx8ER/WAEZIcpAwcje7OZ6vSNoGgaHpoQos+XmmTRGSyO
ezhpNETjAwdrGg7a4SrU5FtUz9jb5r0kuYrL07UVV7b04+5rO/CwmA1WYDvAXWjT
Ks2M2WfP4dCWM4/ADRJKUGcJ7wBlfmGMZXP6hu+w6xxSty2WFHv5UDlS9KX9H2Ef
aXslr8BuXaUzSJVbiYhbtop77OP8gVlbjsQjp6D80Sdce8ejO9rBnx2AY/rFHLv7
5v+C/gpPoAdKvQUStIpAne3IL6WPMhQVkmE1JYYEt+qNbWOakTwkv7WwT2EpPGkB
+c8y45T64iFcTisWAMGe/D/qNl/XhP99PNGWHCOWQWhiWSiZ+dDS7f5icQ6IEcXj
Jm5eT9NDKPNSYg==
-----END CERTIFICATE-----
```

## File: `Build/Nuke/Certs/DevCerts/Elastic/es01.crt`
```
-----BEGIN CERTIFICATE-----
MIIFezCCA2OgAwIBAgIIFD1C9gpep6wwDQYJKoZIhvcNAQENBQAwKDESMBAGA1UE
ChMJTXlDb21wYW55MRIwEAYDVQQDEwlNeUNvbXBhbnkwIBcNMjAwNTI3MTUzMzAw
WhgPMjEyMDA0MjkwNzI0MDBaMCMxEjAQBgNVBAoTCU15Q29tcGFueTENMAsGA1UE
AxMEZXMwMTCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAMQXiJJ/mMay
uhH1LLIEMPvNiC5NKfDI/wMcYIx8NKyfH7lNNSbeqQQbIiB66rp1Yoxuoa+ZKiPA
sFbUlkqkOTXohNvldCeMLKGg6SBL/lpJ2NzYXK2cI5CMJXJftfREwt5rt+U8g3Fu
HLGwsmUsThDkuQDJ7lkyectLEFHaYP/FfOxDkqYBnKhRSQ6E1kX2uqDNYeJ6Ga21
k2SEyXeSnUpxALng2IDZedscqNG3HKuvDOgOvB9ve5kRkJB1ijFpcE+6sc0qeUWG
2Cxve4PwCELKd2OMUiv2MCVOvTUEKSOak9i4YtpfPfDUbry7hhoxwRkzTEmUNjVm
v+lgauAsyN596e0baa5c+cpaAVpyYGJ8R1MR/n10r16+0o24xkhlq2VdpxynqaGp
YrsryxUSERPYN2ihcXRcPBO6iOrPHJi15W5eYCSGW0EgaXpn63HJEiqIQLCeDfBq
4Lf7WfpMZ/TOsBzcILvGsJF5zOq4RMCcmLTyTomNQ0wY0bX7ULhBMdhsOQuhk6gD
Sc3NkEc4wCA4s3yN7wQAfPtWTTYqPdxc9gkGg3SE8F+q59xPXW1GKMX4WZaVYJhv
PYOcugmMppcweu07A1Qn6BHoCm6YlgF9/Jq9PDEBChQOtRagD4SRIQc3dj1F0ddq
NM2WSRi18NITbDoi/7eRt9bAVJlkf+X7AgMBAAGjgaswgagwDAYDVR0TAQH/BAIw
ADAdBgNVHQ4EFgQURAmzhPjy6eE8KgLgZRU+ZqtzrDEwCwYDVR0PBAQDAgPoMB0G
A1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjAaBgNVHREEEzARggRlczAxggls
b2NhbGhvc3QwEQYJYIZIAYb4QgEBBAQDAgbAMB4GCWCGSAGG+EIBDQQRFg94Y2Eg
Y2VydGlmaWNhdGUwDQYJKoZIhvcNAQENBQADggIBAFYjqaolA8PHi84GZPZ1EwO0
RsJuDwlW5UEszR8/743TDRsZn3jdcKzASGVrmiq8lWf4gSbwFqyiHALbfA+yrHw6
PatK8dkAHQDeHLRT2VGr7XQLczGZFSbZOcRPI3TQWirjAh6x2UgcVNuo345UGjtw
3TBa4SfAUZYTyE0kh+rxdPAjBp3RD2R+8r0MPsmU0eCIv5rk/8Mmx//nHs0C4rM5
bSyXBrKxk6CgAMsGl4YaQ6OIVTrIJBeCQaxYMBta/S4kTXX9GMkJeaA2eF3UXwuB
tRpeREgI5/oHkkbvyBNZk4Y0RtFbIiyXT9wb6/S+jiCTTIp/GKWKFBMk3RoAJGxE
OBct6IhhVSJjNgshPQmJFm/Edkf7JArFTpnUvWRdigc0+RbKPYJwAxPOxJyLv8rv
iGIxeZsw0WJhtzX+g2scN9Va4R/xKgt1dR7eEZgWXxrUB2NCzAm+/DhAT2qf7hLC
p1t11jWd2dtCks5+vARKFYlTy0JBvBkhOwgOkbBQx6uQ72Xqk/8sUlOxf7114JK0
ZoiKAfdiR1YLr8tvwJ01JzDq7BM4jlxR473gHFqWPzRQg3dKYdaOHEqpQz/1dx6X
sp1IVP0/+keWqhLFMMfz4ai3eivlY5QDs7N3tTN2fWRCR7J67YqDPW+qiMRnxqAN
kuvZMgNuLcYSv9idxMvl
-----END CERTIFICATE-----
```

## File: `Build/Nuke/Certs/DevCerts/Elastic/es01.pem`
```
-----BEGIN RSA PRIVATE KEY-----
MIIJKQIBAAKCAgEAxBeIkn+YxrK6EfUssgQw+82ILk0p8Mj/AxxgjHw0rJ8fuU01
Jt6pBBsiIHrqunVijG6hr5kqI8CwVtSWSqQ5NeiE2+V0J4wsoaDpIEv+WknY3Nhc
rZwjkIwlcl+19ETC3mu35TyDcW4csbCyZSxOEOS5AMnuWTJ5y0sQUdpg/8V87EOS
pgGcqFFJDoTWRfa6oM1h4noZrbWTZITJd5KdSnEAueDYgNl52xyo0bccq68M6A68
H297mRGQkHWKMWlwT7qxzSp5RYbYLG97g/AIQsp3Y4xSK/YwJU69NQQpI5qT2Lhi
2l898NRuvLuGGjHBGTNMSZQ2NWa/6WBq4CzI3n3p7Rtprlz5yloBWnJgYnxHUxH+
fXSvXr7SjbjGSGWrZV2nHKepoaliuyvLFRIRE9g3aKFxdFw8E7qI6s8cmLXlbl5g
JIZbQSBpemfrcckSKohAsJ4N8Grgt/tZ+kxn9M6wHNwgu8awkXnM6rhEwJyYtPJO
iY1DTBjRtftQuEEx2Gw5C6GTqANJzc2QRzjAIDizfI3vBAB8+1ZNNio93Fz2CQaD
dITwX6rn3E9dbUYoxfhZlpVgmG89g5y6CYymlzB67TsDVCfoEegKbpiWAX38mr08
MQEKFA61FqAPhJEhBzd2PUXR12o0zZZJGLXw0hNsOiL/t5G31sBUmWR/5fsCAwEA
AQKCAgBogqZudgUF+aHECmjs4+D7g1qOWt/8jhOkI86tcVFdo110FFs8wTVRk+iH
aRuLjx6b/Ca+gSJ9dahGTv1fANHhEnElBdD3dvUem7VEWlxQ4MTtR391pB8sXhVj
NPG0I6W8h6q2SZ9AqFAwwB0EYS2mQVD8w6L99TIGkJY9GefSyf2/qnARfBBzgQcv
7sqI9WwYYf5Gh48CDyFkVIVP7ltYnoulhdm+KqqQhmDPjQmB00VMtPW8x10Xgs4K
wCqMFUcfp0A2OenyjWDPpgctlZPBjUk+TD5LYeXdLG8ZP4Nxj2Q3AGbnPhW0MnRm
sIdTlKr29Gk3Wf/eTEoCZznvCs9vHL4S1GnovtaQLyrDoxat+Z90LdyYYnp67tPl
sQdQk646Dtx14Hnn3mBswKVprdW6q42y0ttMLY2OqHUNSKjX30GP8Py+ZtpghEv8
EEfBpsRu+NvMpikCFEMNhMA/Hdq2adeQkI9TH89K69SP5d7LnsiWo8H+Y6XGUjSo
hGH7aCEV7Yy3yQPfW8JOR3N5sQzBLvWdrnN0cXrR5XZS5FHC5buoN4nVJqrWsuAC
h4GEIEUSnN0EpfZXBK66nWdATuOHxuRMZ8Vnbaos6HpjLKTSgFUzlocl92LvS8cu
HecPi+9kDmCxQKdJCI+6YQYcS+yJALSqEEW84fjTAoKAi3C+QQKCAQEA/8SO+3tq
lRpRbryTbYZzBWiUo4wFj6FvkIepXbpbmCSuFwrAv+2fwqNBAtRcRQ4e2LNtX3k8
Pc0f1hOXCQjNdUGvI2KcJCBGtjkBBGRNUcO16DjmkR8C/jQnm1zTIQy/z1JAGr3z
A7obVH6KTGh5OMD4gS8uMlygcvkzZH3IS56V4ilU75n6biicHr20JC8kKxenbGBE
dT3TOS/aWCMl7wYtQWgTj+Y/DFUUAfKlZ+2vcwuW7CdDcA9auoivmR84Cz8wu1bj
wgydQheQe+owiG/p6m/PPkJz684+b1a0fnf7xGr7kE/qTIjxwrGrx3zoSzR1q0Pm
zPtnYUFM+J4GGwKCAQEAxEUbJbkArUfPXGyAu8M+bwoXBiAo/vEmUrg9OsEY5SKH
P0rgGgOU12uo+IYwC1mvwAy53siFVSXBQVQA4/UUtj1z2ne8d7a4jNLA7xzqCMC9
r/N2OE9L9hZgZlZwDpryW1chlSP9h85bvOYZdRFw4ii9/F1LYVH4M3PU4W5cZK58
wAdN/i3UXwGeq1BOG/GLYlmQoeAcJBRhiRuvXkyG+/UMQhkUZKfCmme8P99cZvvp
WgOaoPiug9Fe1R5ZV4lJejT9x2uJtldyMgz2QuZpaWk325Sj2essm+cOzJq5K1hq
sYT/IsJfr7TaHQLpm4CuXsaXpKBM/DDK9hxfIhcdoQKCAQEA+mLUjwEtQDZ5jezy
bwB2Tc8p5EnJj+i8rUMB3Q35aSJPg6M1Oy9HfWYQ2NJIWhoOvJo68oJfJSlQh2S6
MU/6w1XAPOXmcb9fOjjn9AK1Ztwvkt1RarRvW6h3NbNTxUET7cRZmVRnOTjSVI9k
mJSWR6cyIFWt5gOj16p6U2CH2u+vT66ixcV50qnS3I1ecyXrRHxtnL1Jh3U0+QEN
wcb29d6YIzXeILuI8WvAoH+Iygt3/SpVX264qFV/vqjdLwvO88Oy01OmuGtc8Dzd
Z1HGnWriFm3K9upbTXeky56YKE8RnCIXkBmMB8zw0GbbAfoX9reukjFxGy7q79zb
m3AoDQKCAQEAoy714EpOFsRC0wxfiD1P9pCEDhLFIxqrC1GljuknYrNvkZ8WbmqV
4PnhNiiTX4yFBH9QNruvp9jJMiC+0MlfHBpB7d1ptHsWO/eqc+QtbXObAuTAYRcF
CCkYo12ws2P+pxTtlgujaruXKJqDhgMnQNIxC9chqlu1qknfMENKzGcKz7oDDZdb
IFa/bp5JIxCUHARtrTkhDJppcc6z4wprnKbkNzyU6Q9WTHx9VvnF4NYH8VBXywiY
SH7WgwlFrPM3RUUzzw9JI3LXPmfqhDsAX6UczRNrm+7dWw4kDteBp1lO9COo4WSM
nBEY29AlHKZD1Ab34+dnurJyvWdfbX+coQKCAQBtpYFOUz1Q5EoVt0/VdUxAraX1
QBF0XueYEl2ieclYWswW0AmFXcd834gHVEyV0vSFAZ2Y2tOdpOSCSzHeQbPQwTEp
EhpGldBFGkfjzwU97kP6cdACDGJay3M94DQDuh/kqGTQTwa5gJVQdGVHwwzIct4H
G8uKuBPwV2iD4pyLK2/YWIbPfM2ZuMoCOjJAaIbkRlu37iiWvqwWnC2a1aFfc+7T
ppLTeZHrdw2V/z0bX1FdpL7c3bweIoXwAr0J5ZEygaEaS9VZs9W7Pm2lIR/RmHAB
RIk8JGWuVG7NsoGd7YgauM2p2MOUSpsj2blATYcfTbVWNa4R2G3BivJDbj1w
-----END RSA PRIVATE KEY-----
```

## File: `Build/Nuke/Certs/DevCerts/Elastic/es02.crt`
```
-----BEGIN CERTIFICATE-----
MIIFezCCA2OgAwIBAgIIFBMn2O8VG34wDQYJKoZIhvcNAQENBQAwKDESMBAGA1UE
ChMJTXlDb21wYW55MRIwEAYDVQQDEwlNeUNvbXBhbnkwIBcNMjAwNTI3MTUzNTAw
WhgPMjEyMDA0MjkwNzI0MDBaMCMxEjAQBgNVBAoTCU15Q29tcGFueTENMAsGA1UE
AxMEZXMwMjCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAMANm/VcB/yJ
MkOe09ffedRf49Pbd9xcXAcM2Ufnsiht8s+sNPR5xKUnWFKFCAVD1cyg2t5pgUg5
FimmXb4saAXNg0aof15loKxyeS5v5/2a6hGt7VyO8H2y7QH6EUnS2ZhytlQe4lqY
PqrMD99y9Uj0UnnbyTsH/kBZclwwz2BNLKcXa2c8YCN8ynKRUrPj7PaFKznTQfME
zz5gj4jd6kU7QCQTvAo6dLoDtyRvD1KHA/2zXUIIGnJPT6KIN+vzYx2QdY8Ecnjt
4IeEsy7SeAY1rofskYW5Uhp7rVs0dkctGKPRibfY6Q/l8fJItJesa1EK33pwrOB7
ydiAImEopP7TI4LpOsKRsmEcXEF+OPN5R/78MPhWF5EpWkLra5wqPSGrIuCvtTJb
4FNQ+4D4BikJD423Pmiz1DvW3DrZddPAUyHTl6yLpLavbc2NiS1XZNUQzi4lyguR
iArdJFftjC1wGnBY96zZLWF2qGR3FOoIAlbCJN/jM+X8g0IU7hJUiVjIe1MO4D3s
TnV25A8k7p9O7u4ZtwuKdI41O0TfEtPjyYOkLg+s3oaEc01rVguEfcZu+HS7y936
jcpKLH3/OgEifkBcb1EcvfxaWhHo0JYpFYzmJCRhPXvo2xQEHr5DTjd1DEe5LHs8
L9cCLFof3TcXMCfxMWimxEEt7beDPO89AgMBAAGjgaswgagwDAYDVR0TAQH/BAIw
ADAdBgNVHQ4EFgQUTILHlUi4V2XYwE/yNawEBFPqE8YwCwYDVR0PBAQDAgPoMB0G
A1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjAaBgNVHREEEzARggRlczAyggls
b2NhbGhvc3QwEQYJYIZIAYb4QgEBBAQDAgbAMB4GCWCGSAGG+EIBDQQRFg94Y2Eg
Y2VydGlmaWNhdGUwDQYJKoZIhvcNAQENBQADggIBAH7dUiFAzIDouuN5nyHFN5l8
Kj18vrIwOaM1U4h3AFl25R6CrfAC2q2HuULT1KKjNv6H6ORoIpds+u4GeBoIxcKe
AWDQyOBULGh2PdO83wbfoJcRe+rjN8WFgeaDZ6nV15DmFL8jLsnF8sy6kihQagG/
+eAr0yn/xCj5pyqYL8FYMyUFNxH3iu9r4FGekpO4BIZbzOj7UkyO4jYWHL7oo3G4
eCvapqiOWRvHFJSh7FOb3RtMECTADU0VrXX/koUnVqcuvzktH/ynQY2vwXZEXyv5
IlM7gAmSFh7+AyJzsfUpx6mD50DxP/NrvAEOkOEksOXmtHwzopFQsa83tcx7UePa
P7YeatGb223dB2yhgkf3Wuabwu+DCZFhF1xY6eJMTJe4B2MuWMa7cXZmAC435Egx
l7T8u46jR9DS1sktg1JvxE9GT6wSSjgrZi4dRsPFA9xMExSW6HeQRiGc/SXGiwHz
PUkRUWhiF3TvN/97opUeT0oaQraVFpc9DeGnX/jUYazbR00nAxfHqzKFV5Twqt+m
vqKJiTmeGHl2mRGuBQ/C3vjTZu8r3rpSmk+6tXn8CABC/K5Lx72MKHerK/MMoV92
O+R4BFjEfMu+1KN4Xmy0RwAGmBzUqxVxTrujJXthVrcT1NAVKhQ3m2b7vSAnOTg9
tPSZDL/go4NsMGCVIOtl
-----END CERTIFICATE-----
```

## File: `Build/Nuke/Certs/DevCerts/Elastic/es02.pem`
```
-----BEGIN RSA PRIVATE KEY-----
MIIJKQIBAAKCAgEAwA2b9VwH/IkyQ57T19951F/j09t33FxcBwzZR+eyKG3yz6w0
9HnEpSdYUoUIBUPVzKDa3mmBSDkWKaZdvixoBc2DRqh/XmWgrHJ5Lm/n/ZrqEa3t
XI7wfbLtAfoRSdLZmHK2VB7iWpg+qswP33L1SPRSedvJOwf+QFlyXDDPYE0spxdr
ZzxgI3zKcpFSs+Ps9oUrOdNB8wTPPmCPiN3qRTtAJBO8Cjp0ugO3JG8PUocD/bNd
Qggack9Poog36/NjHZB1jwRyeO3gh4SzLtJ4BjWuh+yRhblSGnutWzR2Ry0Yo9GJ
t9jpD+Xx8ki0l6xrUQrfenCs4HvJ2IAiYSik/tMjguk6wpGyYRxcQX4483lH/vww
+FYXkSlaQutrnCo9Iasi4K+1MlvgU1D7gPgGKQkPjbc+aLPUO9bcOtl108BTIdOX
rIuktq9tzY2JLVdk1RDOLiXKC5GICt0kV+2MLXAacFj3rNktYXaoZHcU6ggCVsIk
3+Mz5fyDQhTuElSJWMh7Uw7gPexOdXbkDyTun07u7hm3C4p0jjU7RN8S0+PJg6Qu
D6zehoRzTWtWC4R9xm74dLvL3fqNykosff86ASJ+QFxvURy9/FpaEejQlikVjOYk
JGE9e+jbFAQevkNON3UMR7ksezwv1wIsWh/dNxcwJ/ExaKbEQS3tt4M87z0CAwEA
AQKCAgBF1GzxgJ3yx5u8FILoSfxNKPR4sqLZP8fCVHyodWlE4/1WX0H95kyG1FB7
6Jzq9ShGt/H8zpXQQdl6GWCaZiEIgxoJVfjBxOfv68t+A/hxMKOM/BWDAwIUYjtk
7Zzdn8m4cXU0Duq0kAixJ3NaBr2C4jsezbhUO2rJ0PwQ4zpzxHvI4W4O4lf+b0BY
+df9SpF9bRwzcUnYZ9ZG0us9k5q7w3hl5bsIaQrKG9G6cJs8oZTk6ROuj622BHpr
GWZj52IRfNYRw0cwCyYJgEl6a9JyR5CHIZAj9CcTNAbrU57x8Ea2Qdj2POs4+Z3I
P4FSaMG4fOCW72McWEYi7ywQ8atTzrIul+35oXG2VSOh11yB6Tx04MJYlTS5WWcb
o6T9+W8aBljV+pGS8RbsKYQGPUNGCLHMylTrufgwcrgkscJ9lUtpiB6hLp8xR0Zs
hjuHZbt9lxCgn7ZJ5j4p2iBYezLX6kyK2Q/63x5kov5bj6eo1DVk7kL10EaZII8w
wGuAwkixRI0kYOn8uQHGOZ61Lh3yrbkXkPRnrxr2W4CfGR8kybOgji7saH163k9O
nL2uskAWmD1C9oFcyYD2QexlZ9P81dfpiH+/rlQoR3dfGK+wJpRjHb4G85Hl0kjw
C6cm7heRcFkPHnK7ejXSZJvZyBBv+KS3howxnxV/8gVih5l3rQKCAQEA7I7eXoqB
XkZYX05T0+y/lmb/68pLD3cIFMeMLlw/vFDPtgS/n5Bvvv+Vizj9KrQjCr987mCB
GdJb8jS18ApFko+5GYFOFbEBENIGh1uWwZAT/FXuzf1fapJw8ePm6LcusDBAd3ZT
U4A1XFXrhrQd5UxpBJ5lwfvqEIZ0WzOngpLnxngggtutaX2qJ4bWHIk3R9h6G+P0
Ukyp7MjLKnarBFgIAVWc6iAQTdVkQfo8ptXWHumhzrbS1zp6F1jOnjF0ZMmifDIJ
GxmYkWXHA2lM/rAP95g8WUa14rFXUT32mG+PS0VY+8aglzneNSGOdPEDuwXn9u3u
7yILJfHiRXEzowKCAQEAz9Zd2afedJuuxAQx+zu4PBCpqfkPaMFGWlho8xdxrMUl
PUrGQdBz5qGqSlQ9CI2PIX+hnMpfdvxAW4LLYKg1N26oYq3Kk+ZpEbQn670L2vnA
GKsAcBSBeXSxQsZI3ZrlBKUbSlbh6rwpZDFKmnZX1LvpQNy7x2wo1manNFv2BbJ2
lLpm9mSn2ybVhcd8bUYEUs7uszEZAgvLEw262CgcydLQTi8Qf7Uh/+OXk7wYQ6IF
WCuq0v6DCJ7Z8wFUVrG3S/WIrNdART18GdU6VxcnaFYFZAWhWFimlmSrupbswtqf
WssCjjycl5qSqR0/i3xUyAI9iTn8xVG2PC5y9nB/nwKCAQEAzAO3Qh//zJeslZ2O
7GHtJcB1DRztOUw2Gv2yJzWF/lpPmTJlNS8zQK1agrTGmrK62gUlsMxn6yYiCDRv
iLLDJ9BuGdILzudV/PS1jr1tukgRBHn0N5FCXj4nzGX5+lApougqYR0aZhRXcOfk
9cqXUe9hTwtwxSkGx/O9m/5jhFhALknh+BmPaEBppCdEt12b4ImRXkZtqyDVGBJg
LaIkgd2OIeB9MOowRYA5NDGlZ1lajlR+KTJBij+zljkQERyjvlyrlqLseYPMsfDt
/0IsliavzqBrw68ZJIY/wSBIcVUdZxRK1vGKBIJy4q2rF63Yws4oLS0s+O4KYVJI
DA3CMwKCAQEAn/d0oLQOCl5RM1mvRpl+geypScQC0jQAfEUT8haXTc0njndhBQL2
UgsYUMFpgI3EHppnv5Abzi71MfoHo0uUOigXvmvZQeDT+eZZ253T5CTab6IeYiXG
Sb9BOA35w2cW4m5aBOu+UrekfBNcQmrXy0seiufaN/HNtMep5ijpwRTNJEgcO4TZ
lVncem1CHbEIXtwa6RzfDK4bDX1B1GF7VvPFlIexATpfAt8fqXvaiSPJTUW+40s1
e4sYYWsiiN+cHwDKw42hUCm0vQVbM/EESc/7sjKLLr586cBuVN0ZOhifEniybNvG
AwHb5AI5CJkXgCIJTves0ArGYqe1oGySLQKCAQAIqf8gMwtstiTAeBYdHatyd9Sg
ozg1LYTAjHcv/p1dFmfwI/Rg6acmkOou29U5VO718obwUrZSDO/pEbbBS+v8cIKo
1bOVQJJZ3wn0Pjpfdcr0XHp5A3zcT8rtDUhaTLTvAzQJBUJbpG2xriRg19iW57F2
cnvwvkInq9npcEleUaXdr4CSQFMmklfNVNSoBzygic5yfZnHN/K9ygZGc3AuvHmV
gsRHhWBrxT842IRNtt5Kr3X8NSGr22/E3nXUapJ5edVaQd4XDrGzv51dPJlosfy/
N24a/zAqXXPEOm1vf73EujjVg09FfxXsjPSvtDW2EluEJxA3JQMOiOBC0doD
-----END RSA PRIVATE KEY-----
```

## File: `Build/Nuke/Certs/DevCerts/Elastic/es03.crt`
```
-----BEGIN CERTIFICATE-----
MIIFezCCA2OgAwIBAgIITlE/JHsYw5EwDQYJKoZIhvcNAQENBQAwKDESMBAGA1UE
ChMJTXlDb21wYW55MRIwEAYDVQQDEwlNeUNvbXBhbnkwIBcNMjAwNTI3MTUzNzAw
WhgPMjEyMDA0MjkwNzI0MDBaMCMxEjAQBgNVBAoTCU15Q29tcGFueTENMAsGA1UE
AxMEZXMwMzCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAK02yEq+txSM
aMCugAmYQAIg/rxAm6IbEXoM8oW3a+lqw0TY9rF38xrvJNL6wot0dLbHN8PF0KDY
YteOLfQAaHF+bTrGci1D8OmzjCaSV4DU6v/aS6PJANF5TXTQiu77OrqqXzxPhxvR
GD5kYK1ztkL+7jCsKh/wwQ2NCvi1sVMyqhroC0ubiiBe9CcK0Bgy5geFUPjAaoHr
Kym8iUIi13iOKx1Jm0BBdmKrAZP5+CcJxvG+bh+rN3Mbs9DnxzthaFncb3uuWjv5
lguMJqpkDFHThEYCEmBd1K06USxpe3oFBgctKEVjafDhE/RProxqVMRTCVzT/0vH
GAchf8Dg4/CT3iYriiaqUnmeuTMA/sRMgkPS8wtbJ1zEGrO9Sbmy+h0WNXDJWYjM
8IJzuo6gUEHh8JnwNYaHJmJ6CqcVafbsYhkpdS4P16WSX7hwGU0glJy6hUwg9X2A
bO6elWMGwEJUPZyvHGq/yl+/MLqN/mMDoCL8iS0aUUfDfiuNuyE72EC13t/08rQU
0fyDvMsYEXs68xGGlwC48g1HcS7TuX/l10BaXEyfbT/L7yRllNbhbTnXu6041bW0
lg29qKt9+M8VAXlklXhDvDCN+SEBvBZ63maOQ/GfRzXNOnn7qjgC434lORg61Qr2
SDJBAqT1Tvn0gHwLPXAsJia/PgZZcl2hAgMBAAGjgaswgagwDAYDVR0TAQH/BAIw
ADAdBgNVHQ4EFgQUASdtyYBzDupRs0GZ9x9aYYkQgbUwCwYDVR0PBAQDAgPoMB0G
A1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjAaBgNVHREEEzARggRlczAzggls
b2NhbGhvc3QwEQYJYIZIAYb4QgEBBAQDAgbAMB4GCWCGSAGG+EIBDQQRFg94Y2Eg
Y2VydGlmaWNhdGUwDQYJKoZIhvcNAQENBQADggIBAKNzM1b1J9Cxlff94n92cSJw
7XtzkVC0s8ODaRjmI8AOutfeLEBUvdao70USayCYFsouuKAqAEJdiKHf9lSGEzVg
jP+6933/sbSNOqFczZJp8ogF7um47UT54RVv37xo23kregFX/NYkyRDhKKzyYq0q
QqdYG+0569JnF8Ns62Mqcp2Sxg1AYL7SqrAfuiyO302CbI1jGdP0mcrjpICxPdDu
WnywuE4KVOUholrokSoKUUg4bejvro4Mm2N8w9iK0ylzB+wGHUU78ieedpmumVNi
BFM2pc53dhUibzHBpcAC7ZKdlOmaNduvu/AjoUcZSJ4VS1yfaiH4HlFDegRT8Aqf
/ABVAw0/Lmgk0CLFBFuKtoB5/D+pQYYbOsttNt4JXaYyM7wuzWlxyF/CDxoSpVDt
SXlGcnkrSaEP7i40qTxw4KbcrvrWhy6nQH8Ln32xQTzRyyLul8bwt2MeT1sFkJas
muR1igDDYaZ3YF+QbkrVZqMWxBHXnZJ+WjCnPSLQMmVMMxAzGiNtDCO4NU88y1RO
8t8kuO7LZE5dSN7gqTGg2EjgR9aEfzXTltAq0EhsgHjNbYBc28DFLAmgBujZGkgW
BYZPwC7AMrI53tra1snLbtxVRp4NrApDgom23FrP+sFe+E8x+KNJGsrSU234XMcP
2dj22jVIOGjX/lkb8XOo
-----END CERTIFICATE-----
```

## File: `Build/Nuke/Certs/DevCerts/Elastic/es03.pem`
```
-----BEGIN RSA PRIVATE KEY-----
MIIJKQIBAAKCAgEArTbISr63FIxowK6ACZhAAiD+vECbohsRegzyhbdr6WrDRNj2
sXfzGu8k0vrCi3R0tsc3w8XQoNhi144t9ABocX5tOsZyLUPw6bOMJpJXgNTq/9pL
o8kA0XlNdNCK7vs6uqpfPE+HG9EYPmRgrXO2Qv7uMKwqH/DBDY0K+LWxUzKqGugL
S5uKIF70JwrQGDLmB4VQ+MBqgesrKbyJQiLXeI4rHUmbQEF2YqsBk/n4JwnG8b5u
H6s3cxuz0OfHO2FoWdxve65aO/mWC4wmqmQMUdOERgISYF3UrTpRLGl7egUGBy0o
RWNp8OET9E+ujGpUxFMJXNP/S8cYByF/wODj8JPeJiuKJqpSeZ65MwD+xEyCQ9Lz
C1snXMQas71JubL6HRY1cMlZiMzwgnO6jqBQQeHwmfA1hocmYnoKpxVp9uxiGSl1
Lg/XpZJfuHAZTSCUnLqFTCD1fYBs7p6VYwbAQlQ9nK8car/KX78wuo3+YwOgIvyJ
LRpRR8N+K427ITvYQLXe3/TytBTR/IO8yxgRezrzEYaXALjyDUdxLtO5f+XXQFpc
TJ9tP8vvJGWU1uFtOde7rTjVtbSWDb2oq334zxUBeWSVeEO8MI35IQG8FnreZo5D
8Z9HNc06efuqOALjfiU5GDrVCvZIMkECpPVO+fSAfAs9cCwmJr8+BllyXaECAwEA
AQKCAgB3ceSSros/j0eZP3wpoaTaEvi2xnLMSZA2swD2trKihq3bJyaO4OFyvGCP
YL6RPiBR/nT0+s9Qa4dVj8Uekr1zLjSSqFAJ6OUTs229F4Nh4vGet2Ebs7ttuBFy
sXBtNi+ck2oTA+BujTUDqWKFmdqgvn1wcPinh/UIrC9ZrKl4buKgpU1MuRh6FCCX
X7x6Q3cezo80yjNoHcxo/otEYRRnHNqcWqrFl57UkYoICgNWoEZhY+k6y230YbER
KRPZXeWAuiLijivJWeZfVik/rLhWIN8BC+KyM2I6hpF9Z8vvK9GpVzmDB/gBVKTW
/6+lQpnrvDsjmUlebw+hszcOwcZMeFsF0HC8uitJX+7vkYFEEu+nnNmeIZcPRltb
LR4GOSgbaOiS3KD3RlFiNoCNRulLC08AR8ZqkwHztqVFUUAeLKnNbp4OJvS9tqLt
h0UizW6H17xrKMUIH4W1wV55v+frRXUR23jJnxf3eiU+B2OtaTRS315vgj/8iK17
Cd5WwMq1nRwfmR5/iQU6h6BWOx/VIek3dMyxyCtpLYupfW6MEshtH5/pxZ5bpDzB
UusWa7iqlHGq05AMaETnl5tqrZBVQCR6IhrM+JX0+9UPUyeZ4Bh3LPU8OBVRhzJj
ANeyCvF2H+p/Q2pqfN7hK//WDKvdZziAXXGVsvOyiziqg6NgMQKCAQEA3NCNIf0Z
w6U2ek5GGs6yhcyTlVbW1dKKaCKLaugeTeKRqHuO1GsRtBYGiOYTrAixVkOIukqP
HhqkFPBR7XlW4QhjTZGxdF9I4oYXvjUivrieKyDBopiWCXUyLpizBgvJ9ETxu2JJ
CBaESVvakn+fmGuuXy1F2WZpJC1QGCjzQnO9R71Wj/cLf2XF629KdlGtNFCoaoL5
vru6ynXvYFyphXj3R6DdQ5tDQIKjWNTPhWBQ3inJ2lmZuPKfzOAJ0eqP7RTh0Eoc
i03ED/d0xixdzvugNQx64yFWRBoCc4H1699e+8QTSXzAWEtlqrSsIP7ciWA+4BN1
sWmoaEgmTk1A5QKCAQEAyNCChgnkNQj5gceeMs7Zs4UFU19LPBNilUe4KQASdT1n
URYEwNLpxnJmWOCdd0l8NNCdaRxJPRjTKeKiBYfeD8HzH/OdepftUxPRtC6B3PAR
ccKADX03MkegwQ6zQ24ahwVpTVCMfvCkCvzQo5xT9/Lr4PhH4z6zf+q7Xgs3lKJF
rQJtq6pRIXhFIwMtmm+WRsRYV6bjz/btgus49tIXdfQHjmJm/qX1tbJLXNV0u44T
/b5HsYLvcMH9oDGIVCzRz0IByA1Y+I4Rk6DHbVqGZl413uG6qysJLFR2CnBf8E6c
Wl4K7kPh6rTo2TWEhWIK/bWMdMxexhFHQfR3V9aqDQKCAQEArdHJVzkKf/TcpnhZ
PR76btK0VjlukhDS/Ng8kSI5QKwaZtsketfxrqYr7LXYRHLvTe2JgsPQVy03fngS
tfHvTuMwcE5At0+OayqNJCBlwmZHs8FsS9b7PGSx5PY07ox3JD7lXtEmliRLbAfP
TcUC15PkRm2370Nrfpvg0bPikavUEtXbfyZEObveic8oeW0f/++CM534hIj4qAkg
LuWiWDv5w7vAkUh2LyDm/rU+ykogPlH84FHp7SmoWzj84e5X75OhkjnUsF+996ee
l6UzDw0KdtflIEgMxT0IMu7ZrBxAg8U8PXvjWV24oSDp4mtdJRLLS85ltgtrEvPA
m6C6dQKCAQAIAB6jHnPEFSZzoDNSTOFpgIw0xSAnNZKA5gmVQJZ7q0WZemoYEI8V
w+sF8XT0kq3rIMCUtnbIg1uuWIQh+kbDk/OOu1Lz1mezHqAFMLElzz6yrJATeYCg
dTAXYPGNZy6RYIrQdLwUNpwif+4EBq9lunzhSqL6j73xA7YRShsdxdVGzkj2ROPU
lIkUmwTPGVEAYsQuQczjtS/DPoHXe4lJvr4qUwtNa+k9IuxTt4FeE4wCWPlcPh4x
/NiQ8EhBKkP1oOiXQsjfpjFXE1m+ppOiMnCs/4tDVISaCodlZRK9bTRXeVWwJm4y
vqBkPviXo89SSlBdOuMvuvJ+0zGKA1hlAoIBAQCiWqfBK1An7+twj1WlBx6zaSK1
MzSUhdDCnlkP4yaIg2yXbXTv9i4TqckaWGTKNCisW9AJHLMiBC6lZ23aa685XYnF
W3JftcvYHIsRJSOY34UEy4rbqcnJ32xAqu7t52y1urpJu0WkAPw3/H/ZpvPFrWZ/
sc7vMb1yk1E6QiwnndF1qn06l6Eip2dk9b2eLCxezDm8bP+SddQM2PSH4TCZHf8X
vWJTAvKdZlQxpCWd3UihBb1mt26rhZNKDgV6tEOycsVINCeiTWqzQtyLC4KCEtIv
oYYbGxaxy8ZJY05o4vVMJOLklQ5cATDBZEKU2Noq4tt6jFuaD3K4Jn87jWuU
-----END RSA PRIVATE KEY-----
```

## File: `Build/Nuke/Certs/DevCerts/Elastic/kibana01.crt`
```
-----BEGIN CERTIFICATE-----
MIIFgzCCA2ugAwIBAgIISMJmOpIrtQowDQYJKoZIhvcNAQENBQAwKDESMBAGA1UE
ChMJTXlDb21wYW55MRIwEAYDVQQDEwlNeUNvbXBhbnkwIBcNMjAwNTI2MTMwOTAw
WhgPMjEyMDA0MjkwNzI0MDBaMCcxEjAQBgNVBAoTCU15Q29tcGFueTERMA8GA1UE
AxMIa2liYW5hMDEwggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQC9W51/
e2CQOcqvAgosUqKfrFTeF5dtwTsTZIcKJuEt9SmaCdc6os8jcWgvO5e+2JICkeGT
hy/ECSu1anHL6r1N2Rq47wm4nq8tzke4PE8xl+NOth0IyHDCuDQSFWRnoZ2Jn32h
8AVB/zExw7tXCtYsbST7FMAs6/LAUd6kYUi9doRien89gO1xTMTmvhIWQ2J0g5yD
5M512gJJnnFUvjIGEBatNxTdSTGHGUGWOVXK1IMhTWf2uBegirfM/1RenSX9Iey7
4vlMGymycd6MXQfUa2lsRQ8ZDH8miuTXVCYvSQzwJdD5Z0UQjX8X70zi/6jxjrfO
2+TgqUOsFcGIXb0OWlHRN53qBTgJJyfge6cQlpjU9pJgsH0mmeXM5odTin9pxO6h
Gl9UIl1LFIHlrLC96kxE5b3PeqDQpx2ysyt/24dc0Vu624p59PQXWldgsIpYkStl
dnk2LkOQJjjkEXIO2H3iakCQMA8kfqxh5a7yU3Jpw1zsny4FqYBqEubJexGV2dwl
XqxBj4Tv46nuPoqFb3cq5OeoG+dYkWVwHNHZ6naGMnFt76j/xonvcstxaPiSTsOi
H/H6MvBmuKTXa4RpmBcEYjDCAl8qsBjg577zUVGwGYfH3s+RJT7Np7fIZqQQNcrl
iWBZxHLb4nLGectrW1dcav4apmqWHRvXEao7RwIDAQABo4GvMIGsMAwGA1UdEwEB
/wQCMAAwHQYDVR0OBBYEFIZ572uOuxq7nj9uQZb+sOH8lEeqMAsGA1UdDwQEAwID
6DAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHgYDVR0RBBcwFYIIa2li
YW5hMDGCCWxvY2FsaG9zdDARBglghkgBhvhCAQEEBAMCBsAwHgYJYIZIAYb4QgEN
BBEWD3hjYSBjZXJ0aWZpY2F0ZTANBgkqhkiG9w0BAQ0FAAOCAgEAvq66QQrRxDwu
TO9ekdfiU2uV/+2DPN1eZB3Vo4rAJVrc/uafH6lu+Or+Sogq7wQ9cLhpZWwbDL5Z
tJFR7hCFqmVkMXX8pqvNk4oKi71cBzx4QVAH+HxEkmTikc1oH3z+Kj1JzLcqHQ/O
DCf8iGHAoIeP0p7Bxfm1VzXGaPoxyRP7Ise+VTQnYmw8d84WR34tKAFWEf/B+aZe
iX0XzLS32M247k8U5ellmwQ5iOaSkjtpsocM+BmD4PKGvwTvcmShnHGf5D81dhAU
WvPOeuoouhcw4b+bWTGaZqoQb30aOe+vJDLX2VURTSuMaSIpoxy51qu0ZQNfgcRc
q/dZo+0NLQJwHij6uU5V6rrTwTYsYoHsQkj/kB9+S8KM9AXg7VD/qeVO4kIz7XpD
hb+oJfTjFnN/lNIbkdOpbpieurqFC3RA7yMk26AT+v/120/aVB6IkXn1Vq0kJbE6
oEjhuBbj4c1b2riXrDWICghbHLXWYjKvrCOqn5E2KELDrjkT4b/ZlrWBXeDn4Sd3
GkBK3GLsHZENxiEDAfeWOIEdrni/vHo1I2s6nu5CFCQiphI6mIgDhk19pQTetTS9
38Hy+FnzXlp7FfyTOW2xpJbfYtoi9YE/RcBz21feCMidXFJGBw7gW3pf64UQgsk/
ULR6JtJlskuaaXgZGH19J+uAmG1oOig=
-----END CERTIFICATE-----
```

## File: `Build/Nuke/Certs/DevCerts/Elastic/kibana01.pem`
```
-----BEGIN RSA PRIVATE KEY-----
MIIJKQIBAAKCAgEAvVudf3tgkDnKrwIKLFKin6xU3heXbcE7E2SHCibhLfUpmgnX
OqLPI3FoLzuXvtiSApHhk4cvxAkrtWpxy+q9TdkauO8JuJ6vLc5HuDxPMZfjTrYd
CMhwwrg0EhVkZ6GdiZ99ofAFQf8xMcO7VwrWLG0k+xTALOvywFHepGFIvXaEYnp/
PYDtcUzE5r4SFkNidIOcg+TOddoCSZ5xVL4yBhAWrTcU3UkxhxlBljlVytSDIU1n
9rgXoIq3zP9UXp0l/SHsu+L5TBspsnHejF0H1GtpbEUPGQx/Jork11QmL0kM8CXQ
+WdFEI1/F+9M4v+o8Y63ztvk4KlDrBXBiF29DlpR0Ted6gU4CScn4HunEJaY1PaS
YLB9JpnlzOaHU4p/acTuoRpfVCJdSxSB5aywvepMROW9z3qg0KcdsrMrf9uHXNFb
utuKefT0F1pXYLCKWJErZXZ5Ni5DkCY45BFyDth94mpAkDAPJH6sYeWu8lNyacNc
7J8uBamAahLmyXsRldncJV6sQY+E7+Op7j6KhW93KuTnqBvnWJFlcBzR2ep2hjJx
be+o/8aJ73LLcWj4kk7Doh/x+jLwZrik12uEaZgXBGIwwgJfKrAY4Oe+81FRsBmH
x97PkSU+zae3yGakEDXK5YlgWcRy2+JyxnnLa1tXXGr+GqZqlh0b1xGqO0cCAwEA
AQKCAgEAs6/yXvzG/1W3/iajXLf11iuERVSBwAbzdk2Yz4thd2kD10arVNsWUP3W
7atRLir5MzMXqhVIwHArZ/Xgkq7ogK0abI943BbJCWCMMkoYpGkLrK+oEaOTTVPb
JaXjJ2v3wJb2cur/MkdleWHRrqF756CSzSg9zOMB8no+GiKvEgsbSRARGl3z8+Xz
mzqWk0XScdpKdeZz/OWp8g5GYTIy6gnuWuTACdThCOBwmotB3D2ZScrYcwjycsfv
7roEZ9wcJn9A1HJoO04zXUAs/WlyeqKK4dEOqKhxKDP5QFR7/7cEbgaUrXbP1QtQ
pXfRsD8HJGJYDhYgtQgqTWw/wJWjRg8cAA6hhNFaeLnUj2ZuJKtOscLHoylyaYWq
+KbV2yDmUey7GOIaERtmaXBfM9uQvOG0xZOn4tS3Cl5HYO4Dut2f0krW+5kF7Ntu
AIjoUMFJixficDvfihCekHbFwbQMOyGXPpkE9ZIChXmnUuWFR08T+YPlUtrYW8al
fwbmjDN2X1TDJIfcTPfMT5RR7w5uYOGgl14Go7rT4Efb9vTLqa2XU86n6ltYBqJ2
bfPBD14PMF9b2uz6Djy6xiL1ehAiF6GBGnHyeJg+ibesRv0ZhzCP+BpoUJi5wleY
jf3AQdaGX6+f7/0+Cw+dglPGooT3mxZq6UGWgcjT8gXuy3AxatECggEBAOb5U+oL
qpouzcxkjlPrqyJSfiHfFOxZGMMC6jzOg+2xqWOV4rx7mhs79NAmGYbNlUzPKE4A
njmUXdC6/qemWKA7J4nd/LrBJ+8lBqqKwkBdSEOxrz9hFz2QQox3vX/4oe2U3+W2
U9t6A9ZGX8oyBnBJSWX7wO1J7goS7UkQ5UGi/yV9JA/DD3G1SwJCG+50DhPo7ywf
6j0gZjj1Q8fdOzimuTGkB22zAGNs6th8cuLYF+hz//MwyEKxuCXF2GTmaXg0BChy
N91STs2r/H0AUm0E+un4nWO4WwrI8e3y95QOljv0RZc95OGtXcwD7ck0SFhiefbd
Fxv6CFkib7ZROoMCggEBANHf9LnVtbhpQmJXEg76Tp5a+5SNd2EX5f39fhuhG9qL
RJhjHltPC4CO67kByXPkGGlAt/PqgxxWxSkNcGgSKV/0pvrv4YNFALWqucChxtBL
C8030NBwn8RY988YGH2ss/OFK2JqrUGWyNRGtGkfdXkXfT+GG7sQy0Ru42zwHeUz
EfySNUDYh3MKVqhg8x6DD2bP4tRPkWgo+ovkc0u3O+MdMSGFUVox28+iWvKvEzVc
R5ey65mdCA4G7xAHOdFwz7myn/zVgcsvJhpEyZJ/tkOMfBshwXNEnGx2xhrfw3MC
DvcuQ9DIgvk+p8gaElzJr6cpFQSEc900mUikm64/sO0CggEATlBpiGjOPpryAoRx
0biNfQS1aaym/oAzKiP54gYvq09a3L48c6YBGYzZtB3G9/MK1VFEHDaPb3yD1rsg
jx2S3TlRbaiMAZJuhOJsATUtKf+2+eTsQ7Qa2i/osJIE+bgGx3R7+fo5MqiLVoLk
Bb2yey4OKfsTbiFsCZRjSivlX7zxf/ePW5zKxsYumaRqrg5Bm7SWK8LifDlZD6Tx
h3nWk53MGy2/qw1Pa2bJtf90QL/+Uz3Jod5/eEWj54LOnV+WkUApzMD1eiBnQcs3
v/Z0/Cv9G4nFa8NdcymxBfokwdm0TL3FPsOosHBE5mDKpjcI9JbnPbG3HTBI1lgb
wpiGGwKCAQAarqpiZfUweNFjx0YYeWI9Z7vMax/eTDeFTxEVWio8YrBZ32Ago7AG
rCTz5HJENZ+U4hGBBTOeCroOOhMsaAKynFwOUykMk10/u3DaOLcaDDB36ry1g1wM
jnMS9TFH6QkH0MpvPLjCOfVWZ5bQNpusxXu688XaxovRK3fmhbCHTzLeNYhnsh+m
VI4n4guGuYrfu1ZPP75wy6Tu3CB8Y9NNUIzKgjSRjv0vLKj7aZ67jfvcIXcqlHhN
sDv8ga6sHfeK2FbWwh46QshJVq153prBg77ThDsf+H0anQ8ao5Apsv1MF6mvhY6B
OaIDIq1q9olKa0KszFoeqW1Dewn/4UERAoIBAQDgJeauMHRcpMrp/8jUxOyTrGlQ
U/R4LfbYB0N/zOhUXK0tO60GCfdB4EpXrG0fvhtkQJd5/5WPPBUuZhBIY3jYD1cE
4cV6++sCKXTQcbd6wZKd0Rbe7G22Z076R7FT8X5NJBUdgcsczIxmXw6Lh8w6OE5O
fBLzFlh1mvPwgTdO19umS+qjz3+OSESmL409i5TDWhFz9yM9sz37Dw+U0CpNUgOg
lX9AmKSe/BU1mNYPfi4/O4UR/06aHe1ZLKGnnynzPM+RkoCsGabyvyHoDvP/zSut
hyePVhh8eI/oQENlOgak7qlCGRLnxjEkFHPkke+URSiCwCOxYUchPoTR2jXn
-----END RSA PRIVATE KEY-----
```

## File: `Build/Nuke/DockerCompose/DockerComposeTargets.cs`
```csharp
using System;
using System.Collections.Generic;
using System.Runtime.CompilerServices;
using Nuke.Common;
using Nuke.Common.IO;
using Nuke.Common.Tooling;
using Nuke.Common.Tools.Docker;
using static MyCompany.ECommerce.Nuke.Paths;
using static MyCompany.ECommerce.Nuke.Environment;
using static MyCompany.ECommerce.Nuke.Certs.CertsTargets;
using static MyCompany.ECommerce.Nuke.Elastic.ElasticTargets;

namespace MyCompany.ECommerce.Nuke.DockerCompose;

public static class DockerComposeTargets
{
    private static readonly AbsolutePath ComposeDirectory = NukeDirectory / "DockerCompose";

    public static Target StartLocalDockerInfrastructure => _ => _
        .DependsOn(PrepareCertificates, CreateElasticUsers)
        .Executes(() =>
        {
            DockerComposeTasks.Up(settings => settings
                .SetFile(GetInfrastructureComposeFiles())
                .Apply(upSettings => SetInfrastructureEnvironmentVariables(upSettings))
                .SetDetach(true));
            WriteLogsInfo();
        });

    public static Target StopLocalDockerInfrastructure => _ => _
        .Executes(() =>
        {
            DockerComposeTasks.Down(settings => settings
                .SetFile(GetInfrastructureComposeFiles())
                .Apply(SetInfrastructureEnvironmentVariables)
            );
        });

    public static Target CleanLocalDockerInfrastructure => _ => _
        .DependsOn(
            StopLocalDockerInfrastructure,
            CleanCertificates,
            CleanElasticUsers)
        .Executes(() =>
        {
            DockerTasks.DockerVolumePrune(settings => settings
                .SetForce(true));
        });

    public static Target DisplayLocalDockerInfrastructureLogs => _ => _
        .Executes(() =>
        {
            DockerComposeTasks.Logs(settings => settings
                .SetFile(GetInfrastructureComposeFiles())
                .Apply(SetInfrastructureEnvironmentVariables)
                .SetFollow(true));
        });

    private static IEnumerable<string> GetInfrastructureComposeFiles([CallerMemberName] string targetName = null)
    {
        yield return ComposeDirectory / "infrastructure-compose.yml";
        if (EnvironmentIs(Development))
        {
            var overrideFilePath = GetOverrideFileNameFor(Development);
            if (overrideFilePath.FileExists())
                yield return overrideFilePath;
        }
        else if (EnvironmentIs(Test))
        {
            var overrideFilePath = GetOverrideFileNameFor(Test);
            if (overrideFilePath.FileExists())
                yield return overrideFilePath;
        }
        else
        {
            throw new ArgumentOutOfRangeException(nameof(Environment), Build.Environment,
                $"Environment not supported for: {targetName}");
        }
    }

    private static AbsolutePath GetOverrideFileNameFor(Environment environment) =>
        ComposeDirectory / $"infrastructure-compose.{((string)environment).ToLower()}.yml";

    private static T SetInfrastructureEnvironmentVariables<T>(T settings)
        where T : DockerComposeSettings => settings
        .SetProcessEnvironmentVariable("ES_VERSION", Settings.Elastic.ElasticsearchVersion)
        .SetProcessEnvironmentVariable("ES_CONFIG_DIR", Settings.Elastic.ElasticsearchConfigDirectory)
        .SetProcessEnvironmentVariable("KIBANA_VERSION", Settings.Elastic.KibanaVersion)
        .SetProcessEnvironmentVariable("KIBANA_CONFIG_DIR", Settings.Elastic.KibanaConfigDirectory)
        .SetProcessEnvironmentVariable("ES_KIBANA01_USER", Settings.Elastic.Kibana01UserName)
        .SetProcessEnvironmentVariable("ES_KIBANA01_PASSWORD", Settings.Elastic.Kibana01UserPassword)
        .SetProcessEnvironmentVariable("KIBANA_ENCRYPTIONKEY", Settings.Elastic.KibanaEncryptionKey)
        .SetProcessEnvironmentVariable("ES_USERS_DIR", UsersDirectory)
        .SetProcessEnvironmentVariable("CERTS_DIR", CertsDirectory);

    private static void WriteLogsInfo()
    {
        var previousForegroundColor = Console.ForegroundColor;
        Console.ForegroundColor = ConsoleColor.DarkBlue;
        Console.WriteLine();
        Console.WriteLine("-----------------------");
        Console.WriteLine($"Use \"nuke {nameof(DisplayLocalDockerInfrastructureLogs)}\" to see the logs.");
        Console.WriteLine("-----------------------");
        Console.WriteLine();
        Console.ForegroundColor = previousForegroundColor;
    }
}
```

## File: `Build/Nuke/DockerCompose/infrastructure-compose.development.yml`
```yaml
version: "2.4"
services:  
  postgres:    
    ports:
      - 5432:5432
    environment:
      POSTGRES_PASSWORD: password

  es01:
    volumes:
      - ${CERTS_DIR}/CA/ca.crt:${ES_CONFIG_DIR}/certs/ca.crt:ro
      - ${CERTS_DIR}/Elastic/es01.pem:${ES_CONFIG_DIR}/certs/es01.pem:ro
      - ${CERTS_DIR}/Elastic/es01.crt:${ES_CONFIG_DIR}/certs/es01.crt:ro
    environment:
      - ES_JAVA_OPTS=-Xms512m -Xmx512m     
    ports:
      - 9200:9200
  es02:
    volumes:
      - ${CERTS_DIR}/CA/ca.crt:${ES_CONFIG_DIR}/certs/ca.crt:ro
      - ${CERTS_DIR}/Elastic/es02.pem:${ES_CONFIG_DIR}/certs/es02.pem:ro
      - ${CERTS_DIR}/Elastic/es02.crt:${ES_CONFIG_DIR}/certs/es02.crt:ro
    environment:
      - ES_JAVA_OPTS=-Xms512m -Xmx512m      
    ports:
      - 9201:9200

  es03:
    volumes:      
      - ${CERTS_DIR}/CA/ca.crt:${ES_CONFIG_DIR}/certs/ca.crt:ro
      - ${CERTS_DIR}/Elastic/es03.pem:${ES_CONFIG_DIR}/certs/es03.pem:ro
      - ${CERTS_DIR}/Elastic/es03.crt:${ES_CONFIG_DIR}/certs/es03.crt:ro
    environment:
      - ES_JAVA_OPTS=-Xms512m -Xmx512m
    ports:
      - 9203:9200

  kibana01:
    volumes:
      - ${CERTS_DIR}/CA/ca.crt:${KIBANA_CONFIG_DIR}/certs/ca.crt:ro
      - ${CERTS_DIR}/Elastic/kibana01.pem:${KIBANA_CONFIG_DIR}/certs/kibana01.pem:ro
      - ${CERTS_DIR}/Elastic/kibana01.crt:${KIBANA_CONFIG_DIR}/certs/kibana01.crt:ro
    ports:
      - 5601:5601
```

## File: `Build/Nuke/DockerCompose/infrastructure-compose.yml`
```yaml
version: "2.4"
services:
  postgres:
    image: postgres
    container_name: postgres
    networks:
      - crm
    environment:
      POSTGRES_PASSWORD:
  
  es01:
    image: docker.elastic.co/elasticsearch/elasticsearch:${ES_VERSION}
    container_name: es01    
    volumes:
      - ${ES_USERS_DIR}/users:${ES_CONFIG_DIR}/users:ro
      - ${ES_USERS_DIR}/users_roles:${ES_CONFIG_DIR}/users_roles:ro
    environment:
      - cluster.name=es_cluster
      - node.name=es01
      - discovery.seed_hosts=es02,es03
      - cluster.initial_master_nodes=es01,es02,es03
      - xpack.security.enabled=true
      - xpack.security.transport.ssl.enabled=true
      - xpack.security.transport.ssl.key=${ES_CONFIG_DIR}/certs/es01.pem
      - xpack.security.transport.ssl.certificate=${ES_CONFIG_DIR}/certs/es01.crt
      - xpack.security.transport.ssl.certificate_authorities=${ES_CONFIG_DIR}/certs/ca.crt
      - xpack.security.transport.ssl.verification_mode=certificate
      - xpack.security.transport.ssl.client_authentication=required
      - xpack.security.http.ssl.enabled=true
      - xpack.security.http.ssl.key=${ES_CONFIG_DIR}/certs/es01.pem
      - xpack.security.http.ssl.certificate=${ES_CONFIG_DIR}/certs/es01.crt
      - xpack.security.http.ssl.certificate_authorities=${ES_CONFIG_DIR}/certs/ca.crt
    ulimits:
      memlock:
        soft: -1
        hard: -1
    networks:
      - crm

  es02:
    image: docker.elastic.co/elasticsearch/elasticsearch:${ES_VERSION}
    container_name: es02
    volumes:
      - ${ES_USERS_DIR}/users:${ES_CONFIG_DIR}/users:ro
      - ${ES_USERS_DIR}/users_roles:${ES_CONFIG_DIR}/users_roles:ro
    environment:
      - cluster.name=es_cluster
      - node.name=es02
      - discovery.seed_hosts=es01,es03
      - cluster.initial_master_nodes=es01,es02,es03
      - xpack.security.enabled=true
      - xpack.security.transport.ssl.enabled=true
      - xpack.security.transport.ssl.key=${ES_CONFIG_DIR}/certs/es02.pem
      - xpack.security.transport.ssl.certificate=${ES_CONFIG_DIR}/certs/es02.crt
      - xpack.security.transport.ssl.certificate_authorities=${ES_CONFIG_DIR}/certs/ca.crt
      - xpack.security.transport.ssl.verification_mode=certificate
      - xpack.security.transport.ssl.client_authentication=required
      - xpack.security.http.ssl.enabled=true
      - xpack.security.http.ssl.key=${ES_CONFIG_DIR}/certs/es02.pem
      - xpack.security.http.ssl.certificate=${ES_CONFIG_DIR}/certs/es02.crt
      - xpack.security.http.ssl.certificate_authorities=${ES_CONFIG_DIR}/certs/ca.crt
    ulimits:
      memlock:
        soft: -1
        hard: -1
    networks:
      - crm

  es03:
    image: docker.elastic.co/elasticsearch/elasticsearch:${ES_VERSION}
    container_name: es03
    volumes:
      - ${ES_USERS_DIR}/users:${ES_CONFIG_DIR}/users:ro
      - ${ES_USERS_DIR}/users_roles:${ES_CONFIG_DIR}/users_roles:ro
    environment:
      - cluster.name=es_cluster
      - node.name=es03
      - discovery.seed_hosts=es01,es02
      - cluster.initial_master_nodes=es01,es02,es03
      - xpack.security.enabled=true
      - xpack.security.transport.ssl.enabled=true
      - xpack.security.transport.ssl.key=${ES_CONFIG_DIR}/certs/es03.pem
      - xpack.security.transport.ssl.certificate=${ES_CONFIG_DIR}/certs/es03.crt
      - xpack.security.transport.ssl.certificate_authorities=${ES_CONFIG_DIR}/certs/ca.crt
      - xpack.security.transport.ssl.verification_mode=certificate
      - xpack.security.transport.ssl.client_authentication=required
      - xpack.security.http.ssl.enabled=true
      - xpack.security.http.ssl.key=${ES_CONFIG_DIR}/certs/es03.pem
      - xpack.security.http.ssl.certificate=${ES_CONFIG_DIR}/certs/es03.crt
      - xpack.security.http.ssl.certificate_authorities=${ES_CONFIG_DIR}/certs/ca.crt
    ulimits:
      memlock:
        soft: -1
        hard: -1
    networks:
      - crm

  kibana01:
    image: docker.elastic.co/kibana/kibana:${KIBANA_VERSION}
    container_name: kibana01
    environment:
      - SERVER_NAME=kibana01
      - SERVER_HOST=kibana01
      - ELASTICSEARCH_HOSTS=["https://es01:9200","https://es02:9200","https://es03:9200"]
      - ELASTICSEARCH_SSL_CERTIFICATEAUTHORITIES=${KIBANA_CONFIG_DIR}/certs/ca.crt
      - ELASTICSEARCH_SSL_VERIFICATIONMODE=certificate
      - ELASTICSEARCH_USERNAME=${ES_KIBANA01_USER}
      - ELASTICSEARCH_PASSWORD=${ES_KIBANA01_PASSWORD}
      - XPACK_SECURITY_ENCRYPTIONKEY=${KIBANA_ENCRYPTIONKEY}
      - XPACK_ENCRYPTEDSAVEDOBJECTS_ENCRYPTIONKEY=${KIBANA_ENCRYPTIONKEY}      
      - SERVER_SSL_ENABLED=true
      - SERVER_SSL_KEY=${KIBANA_CONFIG_DIR}/certs/kibana01.pem
      - SERVER_SSL_CERTIFICATE=${KIBANA_CONFIG_DIR}/certs/kibana01.crt
    networks:
      - crm

volumes:
  crm_postgres:
    driver: local  
  crm_es01:
    driver: local
  crm_es02:
    driver: local
  crm_es03:
    driver: local
  crm_kibana01:
    driver: local

networks:
  crm:
    driver: bridge
```

## File: `Build/Nuke/DotNet/DotNetTargets.cs`
```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using Nuke.Common;
using Nuke.Common.IO;
using Nuke.Common.Tools.DotNet;
using Nuke.Common.Utilities.Collections;
using static MyCompany.ECommerce.Nuke.Build;
using static MyCompany.ECommerce.Nuke.Certs.CertsTargets;
using static MyCompany.ECommerce.Nuke.DockerCompose.DockerComposeTargets;
using static Nuke.Common.IO.FileSystemTasks;
using static Nuke.Common.Tools.DotNet.DotNetTasks;
using static MyCompany.ECommerce.Nuke.DotNet.EntityFrameworkTargets;
using static MyCompany.ECommerce.Nuke.Elastic.ElasticTargets;
using static MyCompany.ECommerce.Nuke.Paths;

namespace MyCompany.ECommerce.Nuke.DotNet;

public static class DotNetTargets
{
    private static readonly ISet<string> RootProjects = new HashSet<string>
    {
        "Monolith.Startup",
        "Sales.FluentMigrations"
    };

    public static Target CleanBin => _ => _
        .Before(Restore)
        .Executes(() =>
        {
            SourcesDirectory.GlobDirectories("**/bin", "**/obj").ForEach(DeleteDirectory);
            DeleteDirectory(BinDirectory);
        });

    public static Target Restore => _ => _
        .Executes(() =>
        {
            DotNetRestore(s => s
                .SetProjectFile(Solution));
        });

    public static Target Compile => _ => _
        .DependsOn(Restore)
        .Executes(() =>
        {
            RootProjects.ForEach(projectName =>
            {
                var project = Solution.GetProject(projectName);
                if (project is null)
                    throw new InvalidOperationException($"Compilation root project: {projectName} is missing");
                DotNetBuild(s => s
                    .SetProjectFile(project.Path)
                    .SetConfiguration(BuildConfiguration)
                    .SetOutputDirectory(BinDirectory / project.Name)
                    // .SetAssemblyVersion(GitVersion.AssemblySemVer)
                    // .SetFileVersion(GitVersion.AssemblySemFileVer)
                    // .SetInformationalVersion(GitVersion.InformationalVersion)
                    .EnableNoRestore());
            });
        });

    public static Target RunIntegrationTestsOnLocalDockerInfrastructure => _ => _
        .DependsOn(
            CleanBin,
            Compile,
            StartLocalDockerInfrastructure,
            ApplyMigrationsOnLocalDockerInfrastructure)
        .Triggers(CleanLocalDockerInfrastructure)
        .Before(
            StopLocalDockerInfrastructure,
            CleanCertificates,
            CleanElasticUsers)
        .Executes(() =>
        {
            Solution.AllProjects
                .Where(project => project.Name.EndsWith(".IntegrationTests"))
                .ForEach(project => DotNetTest(settings => settings
                    .SetProjectFile(project.Path)));
        });
}
```

## File: `Build/Nuke/DotNet/EntityFrameworkTargets.cs`
```csharp
using Nuke.Common;
using Nuke.Common.Tooling;
using Nuke.Common.Tools.EntityFramework;
using static MyCompany.ECommerce.Nuke.DockerCompose.DockerComposeTargets;
using static MyCompany.ECommerce.Nuke.Postgres.PostgresTasks;
using static MyCompany.ECommerce.Nuke.Paths;

namespace MyCompany.ECommerce.Nuke.DotNet;

public static class EntityFrameworkTargets
{
    private const string StartupProject = "Monolith.Startup/Monolith.Startup.csproj";
    // TODO: Automatic detecting all projects with DbContexts.
    private static readonly (string Project, string Name)[] DbContexts =
    {
        ("Sales/Sales.Adapters/Sales.Adapters.csproj", "SalesDbContext"),
        ("Contacts/Contacts/Contacts.csproj", "ContactsDbContext")
    };

    public static Target ApplyMigrationsOnLocalDockerInfrastructure => _ => _
        .DependsOn(StartLocalDockerInfrastructure)
        .Executes(() =>
        {
            // TODO: Use connection string from main configuration.
            WaitForDatabase(Settings.Postgres.ConnectionString);
            foreach (var (project, dbContextName) in DbContexts)
            {
                EntityFrameworkTasks.EntityFrameworkDatabaseUpdate(settings => settings
                    .SetProcessWorkingDirectory(SourcesDirectory)
                    .SetStartupProject(StartupProject)
                    .SetProject(project)
                    .SetContext(dbContextName));
            }
        });
}
```

## File: `Build/Nuke/Elastic/ElasticSettings.cs`
```csharp
namespace MyCompany.ECommerce.Nuke.Elastic;

public record ElasticSettings
{
    public const string Key = "Elastic";
        
    public string ElasticsearchVersion { get; set; }
    public string ElasticsearchConfigDirectory { get; set; }
    public string KibanaVersion { get; set; }
    public string KibanaConfigDirectory { get; set; }
    public string SuperUserName { get; set; }
    public string SuperUserPassword { get; set; }
    public string Kibana01UserName { get; set; }
    public string Kibana01UserPassword { get; set; }
    public string KibanaEncryptionKey { get; set; }
}
```

## File: `Build/Nuke/Elastic/ElasticTargets.cs`
```csharp
using Nuke.Common;
using Nuke.Common.IO;
using Nuke.Common.Tools.Docker;
using static Nuke.Common.IO.FileSystemTasks;
using static MyCompany.ECommerce.Nuke.Paths;

namespace MyCompany.ECommerce.Nuke.Elastic;

public static class ElasticTargets
{
    public static readonly AbsolutePath UsersDirectory = ArtifactsDirectory / "Elastic" / "Users";
    private static readonly AbsolutePath ElasticDirectory = NukeDirectory / "Elastic";
    private static readonly AbsolutePath CreateUsersScript = ElasticDirectory / "create_elastic_users.sh";
        
    public static Target CreateElasticUsers => _ => _
        .Executes(() =>
        {
            EnsureExistingDirectory(UsersDirectory);
            return DockerTasks.DockerRun(c => c
                .SetImage($"docker.elastic.co/elasticsearch/elasticsearch:{Settings.Elastic.ElasticsearchVersion}")
                .SetCommand("/bin/bash")
                .SetArgs("/input/script.sh")
                .SetUser(Build.ExecutingUser)
                .SetVolume(
                    $"{CreateUsersScript}:/input/script.sh",
                    $"{UsersDirectory}:/output")
                .SetEnv(
                    $"\"ES_SUPERUSER={Settings.Elastic.SuperUserName}\"",
                    $"\"ES_SUPERUSER_PASSWORD={Settings.Elastic.SuperUserPassword}\"",
                    $"\"ES_KIBANA01_USER={Settings.Elastic.Kibana01UserName}\"",
                    $"\"ES_KIBANA01_PASSWORD={Settings.Elastic.Kibana01UserPassword}\"",
                    $"\"ES_CONFIG_DIR={Settings.Elastic.ElasticsearchConfigDirectory}\"")
                .SetRm(true));
        });

    public static Target CleanElasticUsers => _ => _
        .Executes(() =>
        {
            DeleteDirectory(UsersDirectory);
        });
}
```

## File: `Build/Nuke/Elastic/create_elastic_users.sh`
```bash
bin/elasticsearch-users useradd "${ES_SUPERUSER}" -p "${ES_SUPERUSER_PASSWORD}" -r superuser
bin/elasticsearch-users useradd "${ES_KIBANA01_USER}" -p "${ES_KIBANA01_PASSWORD}" -r kibana_system
cp "${ES_CONFIG_DIR}"/users /output/
cp "${ES_CONFIG_DIR}"/users_roles /output/
```

## File: `Build/Nuke/Helpers/EnumerationExtensions.cs`
```csharp
using Nuke.Common.Tooling;

namespace MyCompany.ECommerce.Nuke.Helpers;

public static class EnumerationExtensions
{
    public static string ValueToLower(this Enumeration enumeration) => enumeration.ToString().ToLower();
}
```

## File: `Build/Nuke/Postgres/PostgresSettings.cs`
```csharp
namespace MyCompany.ECommerce.Nuke.Postgres;

public record PostgresSettings
{
    public const string Key = "Postgres";
        
    public string ConnectionString { get; set; }
}
```

## File: `Build/Nuke/Postgres/PostgresTasks.cs`
```csharp
using System;
using Npgsql;
using Polly;

namespace MyCompany.ECommerce.Nuke.Postgres;

public static class PostgresTasks
{
    private static readonly Policy RetryPolicy = Policy
        .Handle<Exception>()
        .WaitAndRetry(3, attempt => TimeSpan.FromSeconds(attempt));

    public static void WaitForDatabase(string connectionString) => RetryPolicy.Execute(() =>
    {
        using var connection = new NpgsqlConnection(connectionString);
        connection.Open();
    });
}
```

## File: `Build/Nuke.DockerCompose/AssemblyInfo.cs`
```csharp
using NoesisVision.Annotations;

[assembly: ExcludeFromDocs]
```

## File: `Build/Nuke.DockerCompose/DockerComposeDownSettings.cs`
```csharp
using System;
using Nuke.Common.Tooling;

namespace MyCompany.ECommerce.Nuke.DockerCompose;

[Serializable]
public class DockerComposeDownSettings : DockerComposeSettings
{
    protected override Arguments ConfigureProcessArguments(Arguments arguments)
    {
        arguments = base.ConfigureProcessArguments(arguments);
        arguments.Add("down");
        return arguments;
    }
}
```

## File: `Build/Nuke.DockerCompose/DockerComposeLogsSettings.cs`
```csharp
using System;
using Nuke.Common.Tooling;

namespace MyCompany.ECommerce.Nuke.DockerCompose;

[Serializable]
public class DockerComposeLogsSettings : DockerComposeSettings
{
    public bool Follow { get; internal set; }

    public DockerComposeLogsSettings SetFollow(bool follow)
    {
        Follow = follow;
        return this;
    }

    protected override Arguments ConfigureProcessArguments(Arguments arguments)
    {
        arguments = base.ConfigureProcessArguments(arguments);
        arguments.Add("logs")
            .Add("--follow", Follow);
        return arguments;
    }
}
```

## File: `Build/Nuke.DockerCompose/DockerComposeSettings.cs`
```csharp
using System;
using System.Collections.Generic;
using Nuke.Common.Tooling;

namespace MyCompany.ECommerce.Nuke.DockerCompose;

[Serializable]
public class DockerComposeSettings : ToolSettings
{
    public override string ProcessToolPath => DockerComposeTasks.DockerPath;
    public override Action<OutputType, string> ProcessLogger => DockerComposeTasks.CustomLogger;

    internal List<string> FileInternal;
    public IReadOnlyCollection<string> File => FileInternal.AsReadOnly();

    protected override Arguments ConfigureProcessArguments(Arguments arguments)
    {
        arguments.Add("--file {value}", File);
        return base.ConfigureProcessArguments(arguments);
    }
}
```

## File: `Build/Nuke.DockerCompose/DockerComposeSettingsExtensions.cs`
```csharp
using System.Collections.Generic;
using System.Linq;
using JetBrains.Annotations;
using Nuke.Common.Tooling;

namespace MyCompany.ECommerce.Nuke.DockerCompose;

public static class DockerComposeSettingsExtensions
{
    [Pure]
    public static T SetFile<T>(this T settings, params string[] files) where T : DockerComposeSettings => 
        SetFile(settings, (IEnumerable<string>) files);
        
    [Pure]
    public static T SetFile<T>(this T settings, IEnumerable<string> files)
        where T : DockerComposeSettings
    {
        settings = settings.NewInstance();
        settings.FileInternal = files.ToList();
        return settings;
    }
}
```

## File: `Build/Nuke.DockerCompose/DockerComposeTasks.cs`
```csharp
using System;
using System.Collections.Generic;
using JetBrains.Annotations;
using Nuke.Common;
using Nuke.Common.Tooling;

namespace MyCompany.ECommerce.Nuke.DockerCompose;

public static class DockerComposeTasks
{
    internal static string DockerPath => ToolPathResolver.GetPathExecutable("docker-compose");

    internal static void CustomLogger(OutputType type, string output)
    {
        switch (type)
        {
            case OutputType.Std:
                Logger.Normal(output);
                break;
            case OutputType.Err:
            {
                if (output.StartsWith("WARNING!"))
                    Logger.Warn(output);
                else
                    Logger.Normal(output);
                //TODO: logging real errors
                break;
            }
            default:
                throw new ArgumentOutOfRangeException(nameof(type), type, null);
        }
    }

    public static IReadOnlyCollection<Output> Up(Configure<DockerComposeUpSettings> configure) =>
        Up(configure(new DockerComposeUpSettings()));

    public static IReadOnlyCollection<Output> Up(DockerComposeUpSettings settings = null) =>
        StartProcess(settings ?? new DockerComposeUpSettings());

    public static IReadOnlyCollection<Output> Down(Configure<DockerComposeDownSettings> configure) =>
        Down(configure(new DockerComposeDownSettings()));

    public static IReadOnlyCollection<Output> Down(DockerComposeDownSettings settings = null) =>
        StartProcess(settings ?? new DockerComposeDownSettings());

    public static IReadOnlyCollection<Output> Logs(Configure<DockerComposeLogsSettings> configure) =>
        Logs(configure(new DockerComposeLogsSettings()));
        
    public static IReadOnlyCollection<Output> Logs(DockerComposeLogsSettings settings = null) =>
        StartProcess(settings ?? new DockerComposeLogsSettings());

    private static IReadOnlyCollection<Output> StartProcess([NotNull] ToolSettings settings)
    {
        if (settings == null) throw new ArgumentNullException(nameof(settings));
        var process = ProcessTasks.StartProcess(settings);
        process.AssertWaitForExit();
        return process.Output;
    }
}
```

## File: `Build/Nuke.DockerCompose/DockerComposeUpSettings.cs`
```csharp
using System;
using Nuke.Common.Tooling;

namespace MyCompany.ECommerce.Nuke.DockerCompose;

[Serializable]
public class DockerComposeUpSettings : DockerComposeSettings
{
    public bool Detach { get; internal set; }

    public DockerComposeUpSettings SetDetach(bool detach)
    {
        Detach = detach;
        return this;
    }

    protected override Arguments ConfigureProcessArguments(Arguments arguments)
    {
        arguments = base.ConfigureProcessArguments(arguments);
        arguments.Add("up")
            .Add("--detach", Detach);
        return arguments;
    }
}
```

## File: `Build/Nuke.DockerCompose/DockerComposeUpSettingsExtensions.cs`
```csharp
using JetBrains.Annotations;
using Nuke.Common.Tooling;

namespace MyCompany.ECommerce.Nuke.DockerCompose;

public static class DockerComposeUpSettingsExtensions
{
    [Pure]
    public static T SetDetach<T>(this T settings, bool detach)
        where T : DockerComposeUpSettings
    {
        settings = settings.NewInstance();
        settings.Detach = detach;
        return settings;
    }
}
```

## File: `Build/Nuke.DockerCompose/Nuke.DockerCompose.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <AssemblyName>MyCompany.ECommerce.Nuke.DockerCompose</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.Nuke.DockerCompose</RootNamespace>
    </PropertyGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
      <PackageReference Include="Nuke.Common" Version="8.0.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/DomainVisionStatement.md`
```markdown
# Domain Vision Statement

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?
```

## File: `Sources/Contacts/Contacts/Contacts.csproj`
```
﻿<Project Sdk="Microsoft.NET.Sdk.Web">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <AssemblyName>MyCompany.ECommerce.Contacts</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.Contacts</RootNamespace>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
        <OutputType>Library</OutputType>
    </PropertyGroup>
    
    <ItemGroup>
      <ProjectReference Include="..\..\TechnicalStuff\TechnicalStuff.Crud.Api\TechnicalStuff.Crud.Api.csproj" />
      <ProjectReference Include="..\..\TechnicalStuff\TechnicalStuff.Crud.Ef\TechnicalStuff.Crud.Ef.csproj" />
      <ProjectReference Include="..\..\TechnicalStuff\TechnicalStuff.Crud\TechnicalStuff.Crud.csproj" />
    </ItemGroup>
    
    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="Microsoft.AspNetCore.Mvc.Versioning" Version="5.1.0" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
      <PackageReference Include="Npgsql.EntityFrameworkCore.PostgreSQL" Version="8.0.4" />
    </ItemGroup>

</Project>
```

## File: `Sources/Contacts/Contacts/ContactsCrudOperations.cs`
```csharp
using MyCompany.ECommerce.TechnicalStuff.Crud.Operations;

namespace MyCompany.ECommerce.Contacts;

public interface ContactsCrudOperations : CrudOperations { }
```

## File: `Sources/Contacts/Contacts/ContactsEfDao.cs`
```csharp
using System.Diagnostics.CodeAnalysis;
using MyCompany.ECommerce.Contacts.Database;
using MyCompany.ECommerce.TechnicalStuff.Crud.Ef;

namespace MyCompany.ECommerce.Contacts;

[method: SuppressMessage("ReSharper", "SuggestBaseTypeForParameter",
    Justification = "Required by DI container")]
public class ContactsEfDao(ContactsDbContext context) : EfCrudDao(context), ContactsCrudOperations;
```

## File: `Sources/Contacts/Contacts/ContactsModuleInfo.cs`
```csharp
using NoesisVision.Annotations.Domain;
using NoesisVision.Annotations.People;

[assembly: BusinessOwner("Client relations department")]
[assembly: DevelopmentOwner("Supporting team")]
[assembly: DomainModel]
```

## File: `Sources/Contacts/Contacts/Companies/Address.cs`
```csharp
using JetBrains.Annotations;
using Microsoft.AspNetCore.Mvc.ModelBinding;
using Newtonsoft.Json;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Contacts.Companies;

[UsedImplicitly(ImplicitUseTargetFlags.WithMembers)]
[DddEntity]
public class Address
{
    [BindNever]
    [JsonIgnore]
    public Guid CompanyId { get; set; }

    [BindNever]
    [JsonIgnore]
    public Company Company { get; set; }

    public string Street { get; set; }
    public string ZipCode { get; set; }
    public string City { get; set; }
}
```

## File: `Sources/Contacts/Contacts/Companies/Company.cs`
```csharp
using JetBrains.Annotations;
using Microsoft.AspNetCore.Mvc.ModelBinding;
using MyCompany.ECommerce.TechnicalStuff.Crud;
using Newtonsoft.Json;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Contacts.Companies;

[UsedImplicitly(ImplicitUseTargetFlags.WithMembers)]
[DddEntity]
public class Company : CrudEntity
{
    public string Name { get; set; }

    [BindNever]
    public DateTime AddedOn { get; set; }

    [BindNever]
    public Address Address { get; set; }

    public List<Phone> Phones { get; set; }

    [BindNever]
    [JsonIgnore]
    public List<CompanyGroup> Groups { get; set; }

    [BindNever]
    [JsonIgnore]
    public List<CompanyTag> Tags { get; set; }
}
```

## File: `Sources/Contacts/Contacts/Companies/CompanyGroup.cs`
```csharp
using JetBrains.Annotations;
using MyCompany.ECommerce.Contacts.Groups;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Contacts.Companies;

[UsedImplicitly(ImplicitUseTargetFlags.WithMembers)]
[DddEntity]
public class CompanyGroup
{
    public Company Company { get; set; }
    public Guid CompanyId { get; set; }

    public Group Group { get; set; }
    public Guid GroupId { get; set; }
}
```

## File: `Sources/Contacts/Contacts/Companies/CompanyTag.cs`
```csharp
using JetBrains.Annotations;
using MyCompany.ECommerce.Contacts.Tags;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Contacts.Companies;

[UsedImplicitly(ImplicitUseTargetFlags.WithMembers)]
[DddEntity]
public class CompanyTag
{
    public Guid CompanyId { get; set; }
    public Company Company { get; set; }

    public Guid TagId { get; set; }
    public Tag Tag { get; set; }
}
```

## File: `Sources/Contacts/Contacts/Companies/Phone.cs`
```csharp
using JetBrains.Annotations;
using Microsoft.AspNetCore.Mvc.ModelBinding;
using Newtonsoft.Json;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Contacts.Companies;

[UsedImplicitly(ImplicitUseTargetFlags.WithMembers)]
[DddEntity]
public class Phone
{
    [BindNever]
    [JsonIgnore]
    public Guid CompanyId { get; set; }

    [BindRequired]
    public string Number { get; set; }
}
```

## File: `Sources/Contacts/Contacts/Companies/OldApi/CompaniesController.cs`
```csharp
using System.Linq.Expressions;
using JetBrains.Annotations;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using MyCompany.ECommerce.TechnicalStuff.Crud.Api;
using MyCompany.ECommerce.TechnicalStuff.Crud.Operations;

namespace MyCompany.ECommerce.Contacts.Companies.OldApi;

[ApiController]
[Route("/api/companies")]
public class CompaniesController : ControllerBase
{
    private readonly ContactsCrudOperations _operations;

    public CompaniesController(ContactsCrudOperations operations) => _operations = operations;

    [HttpPost("create")]
    public Task<ActionResult<Company>> Create(Company company)
    {
        company.AddedOn = DateTime.UtcNow;
        company.Address = new Address();
        return _operations
            .Create(company)
            .ToOkResult();
    }

    [HttpGet("get")]
    public Task<ActionResult<Company>> Get(Guid id) => _operations
        .Read(id, DefaultIncludes)
        .ToOkResult();

    [HttpGet("search")]
    public IAsyncEnumerable<ListItem> Search(string name = null, int skip = 0, int take = 20) => _operations
        .Read<Company, ListItem>(query => query
            .Apply(ListIncludes)
            .Where(company => name == null || company.Name.Contains(name))
            .Skip(skip)
            .Take(take)
            .Select(ToListItem));

    [HttpPost("update")]
    public Task<ActionResult<Company>> Update(Guid id, Company patch) => _operations
        .Update<Company>(id, DefaultIncludes, company =>
        {
            //Custom action is needed to replace Phones collection.
            //If patch is passed to the ORM then all Phones are treated as new items and inserted to the database.
            //    This behavior does not match the semantics of the PUT request.
            //To merge two collections you can use JSON Patch.
            //To add or remove single entry you can use separate resource (like for Company's Groups or Tags).
            company.Name = patch.Name;
            company.Phones.Clear();
            company.Phones.AddRange(patch.Phones);
            return company;
        })
        .ToOkResult();

    [HttpPost("delete")]
    public Task<OkResult> Delete(Guid id) => _operations
        .Delete<Company>(id, DeletePolicy.Soft)
        .ToOkResult();
        
    [HttpPost("set-address")]
    public Task<ActionResult<Address>> SetAddress(Guid companyId, Address address) => _operations
        .Update<Company, Address>(companyId,
            query => query.Include(c => c.Address),
            company => company.Address = address)
        .ToOkResult();
        
    [HttpPost("add-group")]
    public Task<OkResult> AddGroup(Guid companyId, Guid groupId) => _operations
        .Update<Company>(companyId,
            query => query.Include(company => company.Groups),
            company =>
            {
                if (company.Groups.Any(group => group.GroupId == groupId))
                    return;
                company.Groups.Add(new CompanyGroup
                {
                    CompanyId = companyId,
                    GroupId = groupId
                });
            })
        .ToOkResult();

    [HttpPost("remove-group")]
    public Task<OkResult> RemoveGroup(Guid companyId, Guid groupId) => _operations
        .Update<Company>(companyId,
            query => query.Include(company => company.Groups),
            company =>
            {
                var groupToRemove = company.Groups.FirstOrDefault(group => group.GroupId == groupId);
                if (groupToRemove is null)
                    return;
                company.Groups.Remove(groupToRemove);
            })
        .ToOkResult();
        
    [HttpPost("add-tag")]
    public Task<OkResult> AddTag(Guid companyId, Guid tagId) => _operations
        .Update<Company>(companyId,
            query => query.Include(company => company.Tags),
            company =>
            {
                if (company.Tags.Any(tag => tag.TagId == tagId))
                    return;
                company.Tags.Add(new CompanyTag
                {
                    CompanyId = companyId,
                    TagId = tagId
                });
            })
        .ToOkResult();

    [HttpPost("remove-tag")]
    public Task<OkResult> RemoveTag(Guid companyId, Guid tagId) => _operations
        .Update<Company>(companyId,
            query => query.Include(company => company.Tags),
            company =>
            {
                var tagToRemove = company.Tags.FirstOrDefault(tag => tag.TagId == tagId);
                if (tagToRemove is null)
                    return;
                company.Tags.Remove(tagToRemove);
            })
        .ToOkResult();

    private static readonly QueryConfig<Company> DefaultIncludes = query => query
        .Include(company => company.Phones);

    private static readonly QueryConfig<Company> ListIncludes = query => query
        .Include(company => company.Phones)
        .Include(company => company.Tags)
        .ThenInclude(companyTag => companyTag.Tag);

    private static readonly Expression<Func<Company, ListItem>> ToListItem = company => new ListItem(
        company.Id,
        company.Name,
        company.Phones.Select(phone => phone.Number),
        company.Tags.Select(companyTag => companyTag.Tag.Name));

    [UsedImplicitly(ImplicitUseTargetFlags.WithMembers)]
    public readonly struct ListItem
    {
        public Guid Id { get; }
        public string Name { get; }
        public IEnumerable<string> Phones { get; }
        public IEnumerable<string> Tags { get; }

        public ListItem(Guid id, string name, IEnumerable<string> phones, IEnumerable<string> tags)
        {
            Id = id;
            Name = name;
            Phones = phones;
            Tags = tags;
        }
    }
}
```

## File: `Sources/Contacts/Contacts/Companies/OldApi/NamespaceInfo.cs`
```csharp
using JetBrains.Annotations;
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.Contacts.Companies.OldApi;

[SkipNamespaceInDomainModulesHierarchy(ApplyOnNamespace = true)]
[UsedImplicitly]
public class NamespaceInfo;
```

## File: `Sources/Contacts/Contacts/Companies/RestApi/CompaniesAddressController.cs`
```csharp
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using MyCompany.ECommerce.TechnicalStuff.Crud.Api;

namespace MyCompany.ECommerce.Contacts.Companies.RestApi;

[ApiController]
[Route("/rest/companies/{companyId}/address")]
[ApiVersion("1")]
[ApiVersion("2")]
public class CompaniesAddressController : ControllerBase
{
    private readonly ContactsCrudOperations _operations;

    public CompaniesAddressController(ContactsCrudOperations operations) => _operations = operations;

    [HttpGet]
    [MapToApiVersion("1")]
    public Task<ActionResult<Address>> Read(Guid companyId) => _operations
        .Read<Company, Address>(companyId, query => query
            .Include(c => c.Address)
            .Select(c => c.Address))
        .ToOkResult();

    [HttpPut]
    [MapToApiVersion("1")]
    public Task<ActionResult<Address>> UpdateV1(Guid companyId, AddressV1 addressV1) => _operations
        .Update<Company, Address>(companyId,
            query => query.Include(c => c.Address),
            company => company.Address = MapFrom(addressV1))
        .ToOkResult();

    [HttpPut]
    [MapToApiVersion("2")]
    public Task<ActionResult<Address>> UpdateV2(Guid companyId, Address address) => _operations
        .Update<Company, Address>(companyId,
            query => query.Include(c => c.Address),
            company => company.Address = address)
        .ToOkResult();

    private Address MapFrom(AddressV1 address) => new()
    {
        Street = GetStreetFrom(address),
        ZipCode = address.ZipCode,
        City = address.City
    };

    private static string GetStreetFrom(AddressV1 address)
    {
        if (string.IsNullOrWhiteSpace(address.Street))
            return null;
        if (string.IsNullOrWhiteSpace(address.HouseNo))
            return address.Street;
        if (string.IsNullOrWhiteSpace(address.ApartmentNo))
            return $"{address.Street} {address.HouseNo}";
        return $"{address.Street} {address.HouseNo} {address.ApartmentNo}";
    }

    public class AddressV1
    {
        public string Street { get; set; }
        public string HouseNo { get; set; }
        public string ApartmentNo { get; set; }
        public string ZipCode { get; set; }
        public string City { get; set; }
    }
}
```

## File: `Sources/Contacts/Contacts/Companies/RestApi/CompaniesController.cs`
```csharp
using System.Linq.Expressions;
using JetBrains.Annotations;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using MyCompany.ECommerce.TechnicalStuff.Crud.Api;
using MyCompany.ECommerce.TechnicalStuff.Crud.Operations;

namespace MyCompany.ECommerce.Contacts.Companies.RestApi;

[ApiController]
[Route("rest/companies")]
[ApiVersion("1")]
[ApiVersion("2")]
public class CompaniesController : ControllerBase
{
    private readonly ContactsCrudOperations _operations;

    public CompaniesController(ContactsCrudOperations operations) => _operations = operations;

    [HttpPost]
    [MapToApiVersion("1")]
    public Task<ActionResult<Company>> Create(Company company)
    {
        company.AddedOn = DateTime.UtcNow;
        company.Address = new Address();
        return _operations
            .Create(company)
            .ToCreatedAtActionResult();
    }

    [HttpGet("{id}")]
    [MapToApiVersion("1")]
    public Task<ActionResult<Company>> Read(Guid id) => _operations
        .Read(id, DefaultIncludes)
        .ToOkResult();

    [HttpGet]
    [MapToApiVersion("1")]
    public IAsyncEnumerable<ListItem> SearchV1(string name = null, int skip = 0, int take = 20) => _operations
        .Read<Company, ListItem>(query => query
            .Apply(ListIncludes)
            .Where(company => name == null || company.Name.Contains(name))
            .Skip(skip)
            .Take(take)
            .Select(ToListItem));
        
    [HttpGet]
    [MapToApiVersion("2")]
    public IAsyncEnumerable<ListItem> SearchV2(string query = null, int page = 1, int pageSize = 20)
    {
        // TODO: search using full text search in postgresql
        throw new NotImplementedException();
    }

    [HttpPut("{id}")]
    [MapToApiVersion("1")]
    public Task<ActionResult<Company>> Update(Guid id, Company patch) => _operations
        .Update<Company>(id, DefaultIncludes, company =>
        {
            //Custom action is needed to replace Phones collection.
            //If patch is passed to the ORM then all Phones are treated as new items and inserted to the database.
            //    This behavior does not match the semantics of the PUT request.
            //To merge two collections you can use JSON Patch.
            //To add or remove single entry you can use separate resource (like for Company's Groups or Tags).
            company.Name = patch.Name;
            company.Phones.Clear();
            company.Phones.AddRange(patch.Phones);
            return company;
        })
        .ToOkResult();

    [HttpDelete("{id}")]
    [MapToApiVersion("1")]
    public Task<StatusCodeResult> Delete(Guid id) => _operations
        .Delete<Company>(id, DeletePolicy.Soft)
        .ToStatusCodeResult();

    private static readonly QueryConfig<Company> DefaultIncludes = query => query
        .Include(company => company.Phones);

    private static readonly QueryConfig<Company> ListIncludes = query => query
        .Include(company => company.Phones)
        .Include(company => company.Tags)
        .ThenInclude(companyTag => companyTag.Tag);

    private static readonly Expression<Func<Company, ListItem>> ToListItem = company => new ListItem(
        company.Id,
        company.Name,
        company.Phones.Select(phone => phone.Number),
        company.Tags.Select(companyTag => companyTag.Tag.Name));

    [UsedImplicitly(ImplicitUseTargetFlags.WithMembers)]
    public readonly struct ListItem
    {
        public Guid Id { get; }
        public string Name { get; }
        public IEnumerable<string> Phones { get; }
        public IEnumerable<string> Tags { get; }

        public ListItem(Guid id, string name, IEnumerable<string> phones, IEnumerable<string> tags)
        {
            Id = id;
            Name = name;
            Phones = phones;
            Tags = tags;
        }
    }
}
```

## File: `Sources/Contacts/Contacts/Companies/RestApi/CompaniesGroupsController.cs`
```csharp
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using MyCompany.ECommerce.Contacts.Groups;
using MyCompany.ECommerce.TechnicalStuff.Crud.Api;

namespace MyCompany.ECommerce.Contacts.Companies.RestApi;

[ApiController]
[Route("/rest/companies/{companyId}/groups")]
[ApiVersion("1")]
public class CompaniesGroupsController : ControllerBase
{
    private readonly ContactsCrudOperations _operations;

    public CompaniesGroupsController(ContactsCrudOperations operations) => _operations = operations;

    [HttpGet]
    public IAsyncEnumerable<Group> Read(Guid companyId) => _operations
        .Read<CompanyGroup, Group>(query => query
            .Include(companyGroup => companyGroup.Group)
            .Where(companyGroup => companyGroup.CompanyId == companyId)
            .Select(companyGroup => companyGroup.Group));
        
    [HttpPut("{groupId}")]
    public Task<NoContentResult> Add(Guid companyId, Guid groupId) => _operations
        .Update<Company>(companyId,
            query => query.Include(company => company.Groups),
            company =>
            {
                if (company.Groups.Any(group => group.GroupId == groupId))
                    return;
                company.Groups.Add(new CompanyGroup
                {
                    CompanyId = companyId,
                    GroupId = groupId
                });
            })
        .ToNoContentResult();

    [HttpDelete("{groupId}")]
    public Task<NoContentResult> Remove(Guid companyId, Guid groupId) => _operations
        .Update<Company>(companyId,
            query => query.Include(company => company.Groups),
            company =>
            {
                var groupToRemove = company.Groups.FirstOrDefault(group => group.GroupId == groupId);
                if (groupToRemove is null)
                    return;
                company.Groups.Remove(groupToRemove);
            })
        .ToNoContentResult();
}
```

## File: `Sources/Contacts/Contacts/Companies/RestApi/CompaniesTagsController.cs`
```csharp
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using MyCompany.ECommerce.Contacts.Tags;
using MyCompany.ECommerce.TechnicalStuff.Crud.Api;

namespace MyCompany.ECommerce.Contacts.Companies.RestApi;

[ApiController]
[Route("/rest/companies/{companyId}/tags")]
[ApiVersion("1")]
public class CompaniesTagsController : ControllerBase
{
    private readonly ContactsCrudOperations _operations;

    public CompaniesTagsController(ContactsCrudOperations operations) => _operations = operations;

    [HttpGet]
    public IAsyncEnumerable<Tag> Read(Guid companyId) => _operations
        .Read<CompanyTag, Tag>(query => query
            .Include(companyTag => companyTag.Tag)
            .Where(companyTag => companyTag.CompanyId == companyId)
            .Select(companyTag => companyTag.Tag));

    [HttpPut("{tagId}")]
    public Task<NoContentResult> Add(Guid companyId, Guid tagId) => _operations
        .Update<Company>(companyId,
            query => query.Include(company => company.Tags),
            company =>
            {
                if (company.Tags.Any(tag => tag.TagId == tagId))
                    return;
                company.Tags.Add(new CompanyTag
                {
                    CompanyId = companyId,
                    TagId = tagId
                });
            })
        .ToNoContentResult();

    [HttpDelete("{tagId}")]
    public Task<NoContentResult> Remove(Guid companyId, Guid tagId) => _operations
        .Update<Company>(companyId,
            query => query.Include(company => company.Tags),
            company =>
            {
                var tagToRemove = company.Tags.FirstOrDefault(tag => tag.TagId == tagId);
                if (tagToRemove is null)
                    return;
                company.Tags.Remove(tagToRemove);
            })
        .ToNoContentResult();
}
```

## File: `Sources/Contacts/Contacts/Companies/RestApi/NamespaceInfo.cs`
```csharp
using JetBrains.Annotations;
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.Contacts.Companies.RestApi;

[SkipNamespaceInDomainModulesHierarchy(ApplyOnNamespace = true)]
[UsedImplicitly]
public class NamespaceInfo { }
```

## File: `Sources/Contacts/Contacts/Database/ContactsDbContext.cs`
```csharp
using JetBrains.Annotations;
using Microsoft.EntityFrameworkCore;
using MyCompany.ECommerce.Contacts.Companies;
using MyCompany.ECommerce.Contacts.Groups;
using MyCompany.ECommerce.Contacts.Tags;
using NoesisVision.Annotations.Technology;

namespace MyCompany.ECommerce.Contacts.Database;

[UsedImplicitly(ImplicitUseTargetFlags.Members)]
[Database("Contacts", ServerName = "Postgres")]
public class ContactsDbContext : DbContext
{
    public DbSet<Company> Companies { get; set; }
    public DbSet<Group> Groups { get; set; }
    public DbSet<Tag> Tags { get; set; }

    public ContactsDbContext(DbContextOptions<ContactsDbContext> options) : base(options) { }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        ConfigureContact(modelBuilder);
        ConfigureContactGroup(modelBuilder);
        ConfigureContactTag(modelBuilder);
        ConfigureGroupTag(modelBuilder);
    }

    private static void ConfigureContact(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Company>()
            .OwnsOne(company => company.Address);
        modelBuilder.Entity<Company>()
            .OwnsMany(company => company.Phones, phone =>
            {
                phone.WithOwner().HasForeignKey(nameof(Phone.CompanyId));
                phone.HasKey(nameof(Phone.Number));
            });
    }

    private static void ConfigureContactGroup(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<CompanyGroup>()
            .HasKey(companyGroup => new {companyGroup.CompanyId, companyGroup.GroupId});
        modelBuilder.Entity<CompanyGroup>()
            .HasOne(companyGroup => companyGroup.Company)
            .WithMany(company => company.Groups)
            .HasForeignKey(companyGroup => companyGroup.CompanyId);
        modelBuilder.Entity<CompanyGroup>()
            .HasOne(companyGroup => companyGroup.Group)
            .WithMany(tag => tag.Companies)
            .HasForeignKey(companyTag => companyTag.CompanyId);
    }

    private static void ConfigureContactTag(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<CompanyTag>()
            .HasKey(companyTag => new {companyTag.CompanyId, companyTag.TagId});
        modelBuilder.Entity<CompanyTag>()
            .HasOne(companyTag => companyTag.Company)
            .WithMany(company => company.Tags)
            .HasForeignKey(companyTag => companyTag.CompanyId);
        modelBuilder.Entity<CompanyTag>()
            .HasOne(companyTag => companyTag.Tag)
            .WithMany(tag => tag.Companies)
            .HasForeignKey(companyTag => companyTag.TagId);
    }

    private static void ConfigureGroupTag(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<GroupTag>()
            .HasKey(groupTag => new {groupTag.GroupId, groupTag.TagId});
        modelBuilder.Entity<GroupTag>()
            .HasOne(groupTag => groupTag.Group)
            .WithMany(group => group.Tags)
            .HasForeignKey(groupTag => groupTag.GroupId);
        modelBuilder.Entity<GroupTag>()
            .HasOne(groupTag => groupTag.Tag)
            .WithMany(tag => tag.Groups)
            .HasForeignKey(groupTag => groupTag.TagId);
    }
}
```

## File: `Sources/Contacts/Contacts/Database/NamespaceInfo.cs`
```csharp
using JetBrains.Annotations;
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.Contacts.Database;

[SkipNamespaceInDomainModulesHierarchy(ApplyOnNamespace = true)]
[UsedImplicitly]
public class NamespaceInfo { }
```

## File: `Sources/Contacts/Contacts/Database/Migrations/20220831085231_Initial.Designer.cs`
```csharp
﻿// <auto-generated />
using System;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Migrations;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
using MyCompany.ECommerce.Contacts.Database;
using MyCompany.ECommerce.Contacts.Database;
using Npgsql.EntityFrameworkCore.PostgreSQL.Metadata;

#nullable disable

namespace MyCompany.ECommerce.Contacts.Database.Migrations
{
    [DbContext(typeof(ContactsDbContext))]
    [Migration("20220831085231_Initial")]
    partial class Initial
    {
        protected override void BuildTargetModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder
                .HasAnnotation("ProductVersion", "6.0.8")
                .HasAnnotation("Relational:MaxIdentifierLength", 63);

            NpgsqlModelBuilderExtensions.UseIdentityByDefaultColumns(modelBuilder);

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Companies.Company", b =>
                {
                    b.Property<Guid>("Id")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("uuid");

                    b.Property<DateTime>("AddedOn")
                        .HasColumnType("timestamp with time zone");

                    b.Property<bool>("IsDeleted")
                        .HasColumnType("boolean");

                    b.Property<string>("Name")
                        .HasColumnType("text");

                    b.HasKey("Id");

                    b.ToTable("Companies");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Companies.CompanyGroup", b =>
                {
                    b.Property<Guid>("CompanyId")
                        .HasColumnType("uuid");

                    b.Property<Guid>("GroupId")
                        .HasColumnType("uuid");

                    b.HasKey("CompanyId", "GroupId");

                    b.ToTable("CompanyGroup");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Companies.CompanyTag", b =>
                {
                    b.Property<Guid>("CompanyId")
                        .HasColumnType("uuid");

                    b.Property<Guid>("TagId")
                        .HasColumnType("uuid");

                    b.HasKey("CompanyId", "TagId");

                    b.HasIndex("TagId");

                    b.ToTable("CompanyTag");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Groups.Group", b =>
                {
                    b.Property<Guid>("Id")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("uuid");

                    b.Property<string>("Description")
                        .HasColumnType("text");

                    b.Property<bool>("IsDeleted")
                        .HasColumnType("boolean");

                    b.Property<string>("Name")
                        .HasColumnType("text");

                    b.HasKey("Id");

                    b.ToTable("Groups");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Groups.GroupTag", b =>
                {
                    b.Property<Guid>("GroupId")
                        .HasColumnType("uuid");

                    b.Property<Guid>("TagId")
                        .HasColumnType("uuid");

                    b.HasKey("GroupId", "TagId");

                    b.HasIndex("TagId");

                    b.ToTable("GroupTag");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Tags.Tag", b =>
                {
                    b.Property<Guid>("Id")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("uuid");

                    b.Property<string>("Description")
                        .HasColumnType("text");

                    b.Property<bool>("IsDeleted")
                        .HasColumnType("boolean");

                    b.Property<string>("Name")
                        .HasColumnType("text");

                    b.HasKey("Id");

                    b.ToTable("Tags");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Companies.Company", b =>
                {
                    b.OwnsOne("MyCompany.ECommerce.Contacts.Companies.Address", "Address", b1 =>
                        {
                            b1.Property<Guid>("CompanyId")
                                .HasColumnType("uuid");

                            b1.Property<string>("City")
                                .HasColumnType("text");

                            b1.Property<string>("Street")
                                .HasColumnType("text");

                            b1.Property<string>("ZipCode")
                                .HasColumnType("text");

                            b1.HasKey("CompanyId");

                            b1.ToTable("Companies");

                            b1.WithOwner("Company")
                                .HasForeignKey("CompanyId");

                            b1.Navigation("Company");
                        });

                    b.OwnsMany("MyCompany.ECommerce.Contacts.Companies.Phone", "Phones", b1 =>
                        {
                            b1.Property<string>("Number")
                                .HasColumnType("text");

                            b1.Property<Guid>("CompanyId")
                                .HasColumnType("uuid");

                            b1.HasKey("Number");

                            b1.HasIndex("CompanyId");

                            b1.ToTable("Phone");

                            b1.WithOwner()
                                .HasForeignKey("CompanyId");
                        });

                    b.Navigation("Address");

                    b.Navigation("Phones");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Companies.CompanyGroup", b =>
                {
                    b.HasOne("MyCompany.ECommerce.Contacts.Companies.Company", "Company")
                        .WithMany("Groups")
                        .HasForeignKey("CompanyId")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.HasOne("MyCompany.ECommerce.Contacts.Groups.Group", "Group")
                        .WithMany("Companies")
                        .HasForeignKey("CompanyId")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.Navigation("Company");

                    b.Navigation("Group");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Companies.CompanyTag", b =>
                {
                    b.HasOne("MyCompany.ECommerce.Contacts.Companies.Company", "Company")
                        .WithMany("Tags")
                        .HasForeignKey("CompanyId")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.HasOne("MyCompany.ECommerce.Contacts.Tags.Tag", "Tag")
                        .WithMany("Companies")
                        .HasForeignKey("TagId")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.Navigation("Company");

                    b.Navigation("Tag");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Groups.GroupTag", b =>
                {
                    b.HasOne("MyCompany.ECommerce.Contacts.Groups.Group", "Group")
                        .WithMany("Tags")
                        .HasForeignKey("GroupId")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.HasOne("MyCompany.ECommerce.Contacts.Tags.Tag", "Tag")
                        .WithMany("Groups")
                        .HasForeignKey("TagId")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.Navigation("Group");

                    b.Navigation("Tag");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Companies.Company", b =>
                {
                    b.Navigation("Groups");

                    b.Navigation("Tags");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Groups.Group", b =>
                {
                    b.Navigation("Companies");

                    b.Navigation("Tags");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Tags.Tag", b =>
                {
                    b.Navigation("Companies");

                    b.Navigation("Groups");
                });
#pragma warning restore 612, 618
        }
    }
}
```

## File: `Sources/Contacts/Contacts/Database/Migrations/20220831085231_Initial.cs`
```csharp
﻿using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace MyCompany.ECommerce.Contacts.Database.Migrations
{
    public partial class Initial : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "Companies",
                columns: table => new
                {
                    Id = table.Column<Guid>(type: "uuid", nullable: false),
                    Name = table.Column<string>(type: "text", nullable: true),
                    AddedOn = table.Column<DateTime>(type: "timestamp with time zone", nullable: false),
                    Address_Street = table.Column<string>(type: "text", nullable: true),
                    Address_ZipCode = table.Column<string>(type: "text", nullable: true),
                    Address_City = table.Column<string>(type: "text", nullable: true),
                    IsDeleted = table.Column<bool>(type: "boolean", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Companies", x => x.Id);
                });

            migrationBuilder.CreateTable(
                name: "Groups",
                columns: table => new
                {
                    Id = table.Column<Guid>(type: "uuid", nullable: false),
                    Name = table.Column<string>(type: "text", nullable: true),
                    Description = table.Column<string>(type: "text", nullable: true),
                    IsDeleted = table.Column<bool>(type: "boolean", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Groups", x => x.Id);
                });

            migrationBuilder.CreateTable(
                name: "Tags",
                columns: table => new
                {
                    Id = table.Column<Guid>(type: "uuid", nullable: false),
                    Name = table.Column<string>(type: "text", nullable: true),
                    Description = table.Column<string>(type: "text", nullable: true),
                    IsDeleted = table.Column<bool>(type: "boolean", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Tags", x => x.Id);
                });

            migrationBuilder.CreateTable(
                name: "Phone",
                columns: table => new
                {
                    Number = table.Column<string>(type: "text", nullable: false),
                    CompanyId = table.Column<Guid>(type: "uuid", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Phone", x => x.Number);
                    table.ForeignKey(
                        name: "FK_Phone_Companies_CompanyId",
                        column: x => x.CompanyId,
                        principalTable: "Companies",
                        principalColumn: "Id",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateTable(
                name: "CompanyGroup",
                columns: table => new
                {
                    CompanyId = table.Column<Guid>(type: "uuid", nullable: false),
                    GroupId = table.Column<Guid>(type: "uuid", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_CompanyGroup", x => new { x.CompanyId, x.GroupId });
                    table.ForeignKey(
                        name: "FK_CompanyGroup_Companies_CompanyId",
                        column: x => x.CompanyId,
                        principalTable: "Companies",
                        principalColumn: "Id",
                        onDelete: ReferentialAction.Cascade);
                    table.ForeignKey(
                        name: "FK_CompanyGroup_Groups_CompanyId",
                        column: x => x.CompanyId,
                        principalTable: "Groups",
                        principalColumn: "Id",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateTable(
                name: "CompanyTag",
                columns: table => new
                {
                    CompanyId = table.Column<Guid>(type: "uuid", nullable: false),
                    TagId = table.Column<Guid>(type: "uuid", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_CompanyTag", x => new { x.CompanyId, x.TagId });
                    table.ForeignKey(
                        name: "FK_CompanyTag_Companies_CompanyId",
                        column: x => x.CompanyId,
                        principalTable: "Companies",
                        principalColumn: "Id",
                        onDelete: ReferentialAction.Cascade);
                    table.ForeignKey(
                        name: "FK_CompanyTag_Tags_TagId",
                        column: x => x.TagId,
                        principalTable: "Tags",
                        principalColumn: "Id",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateTable(
                name: "GroupTag",
                columns: table => new
                {
                    GroupId = table.Column<Guid>(type: "uuid", nullable: false),
                    TagId = table.Column<Guid>(type: "uuid", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_GroupTag", x => new { x.GroupId, x.TagId });
                    table.ForeignKey(
                        name: "FK_GroupTag_Groups_GroupId",
                        column: x => x.GroupId,
                        principalTable: "Groups",
                        principalColumn: "Id",
                        onDelete: ReferentialAction.Cascade);
                    table.ForeignKey(
                        name: "FK_GroupTag_Tags_TagId",
                        column: x => x.TagId,
                        principalTable: "Tags",
                        principalColumn: "Id",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateIndex(
                name: "IX_CompanyTag_TagId",
                table: "CompanyTag",
                column: "TagId");

            migrationBuilder.CreateIndex(
                name: "IX_GroupTag_TagId",
                table: "GroupTag",
                column: "TagId");

            migrationBuilder.CreateIndex(
                name: "IX_Phone_CompanyId",
                table: "Phone",
                column: "CompanyId");
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "CompanyGroup");

            migrationBuilder.DropTable(
                name: "CompanyTag");

            migrationBuilder.DropTable(
                name: "GroupTag");

            migrationBuilder.DropTable(
                name: "Phone");

            migrationBuilder.DropTable(
                name: "Groups");

            migrationBuilder.DropTable(
                name: "Tags");

            migrationBuilder.DropTable(
                name: "Companies");
        }
    }
}
```

## File: `Sources/Contacts/Contacts/Database/Migrations/ContactsDbContextModelSnapshot.cs`
```csharp
﻿// <auto-generated />
using System;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
using MyCompany.ECommerce.Contacts.Database;
using MyCompany.ECommerce.Contacts.Database;
using Npgsql.EntityFrameworkCore.PostgreSQL.Metadata;

#nullable disable

namespace MyCompany.ECommerce.Contacts.Database.Migrations
{
    [DbContext(typeof(ContactsDbContext))]
    partial class ContactsDbContextModelSnapshot : ModelSnapshot
    {
        protected override void BuildModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder
                .HasAnnotation("ProductVersion", "6.0.8")
                .HasAnnotation("Relational:MaxIdentifierLength", 63);

            NpgsqlModelBuilderExtensions.UseIdentityByDefaultColumns(modelBuilder);

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Companies.Company", b =>
                {
                    b.Property<Guid>("Id")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("uuid");

                    b.Property<DateTime>("AddedOn")
                        .HasColumnType("timestamp with time zone");

                    b.Property<bool>("IsDeleted")
                        .HasColumnType("boolean");

                    b.Property<string>("Name")
                        .HasColumnType("text");

                    b.HasKey("Id");

                    b.ToTable("Companies");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Companies.CompanyGroup", b =>
                {
                    b.Property<Guid>("CompanyId")
                        .HasColumnType("uuid");

                    b.Property<Guid>("GroupId")
                        .HasColumnType("uuid");

                    b.HasKey("CompanyId", "GroupId");

                    b.ToTable("CompanyGroup");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Companies.CompanyTag", b =>
                {
                    b.Property<Guid>("CompanyId")
                        .HasColumnType("uuid");

                    b.Property<Guid>("TagId")
                        .HasColumnType("uuid");

                    b.HasKey("CompanyId", "TagId");

                    b.HasIndex("TagId");

                    b.ToTable("CompanyTag");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Groups.Group", b =>
                {
                    b.Property<Guid>("Id")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("uuid");

                    b.Property<string>("Description")
                        .HasColumnType("text");

                    b.Property<bool>("IsDeleted")
                        .HasColumnType("boolean");

                    b.Property<string>("Name")
                        .HasColumnType("text");

                    b.HasKey("Id");

                    b.ToTable("Groups");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Groups.GroupTag", b =>
                {
                    b.Property<Guid>("GroupId")
                        .HasColumnType("uuid");

                    b.Property<Guid>("TagId")
                        .HasColumnType("uuid");

                    b.HasKey("GroupId", "TagId");

                    b.HasIndex("TagId");

                    b.ToTable("GroupTag");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Tags.Tag", b =>
                {
                    b.Property<Guid>("Id")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("uuid");

                    b.Property<string>("Description")
                        .HasColumnType("text");

                    b.Property<bool>("IsDeleted")
                        .HasColumnType("boolean");

                    b.Property<string>("Name")
                        .HasColumnType("text");

                    b.HasKey("Id");

                    b.ToTable("Tags");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Companies.Company", b =>
                {
                    b.OwnsOne("MyCompany.ECommerce.Contacts.Companies.Address", "Address", b1 =>
                        {
                            b1.Property<Guid>("CompanyId")
                                .HasColumnType("uuid");

                            b1.Property<string>("City")
                                .HasColumnType("text");

                            b1.Property<string>("Street")
                                .HasColumnType("text");

                            b1.Property<string>("ZipCode")
                                .HasColumnType("text");

                            b1.HasKey("CompanyId");

                            b1.ToTable("Companies");

                            b1.WithOwner("Company")
                                .HasForeignKey("CompanyId");

                            b1.Navigation("Company");
                        });

                    b.OwnsMany("MyCompany.ECommerce.Contacts.Companies.Phone", "Phones", b1 =>
                        {
                            b1.Property<string>("Number")
                                .HasColumnType("text");

                            b1.Property<Guid>("CompanyId")
                                .HasColumnType("uuid");

                            b1.HasKey("Number");

                            b1.HasIndex("CompanyId");

                            b1.ToTable("Phone");

                            b1.WithOwner()
                                .HasForeignKey("CompanyId");
                        });

                    b.Navigation("Address");

                    b.Navigation("Phones");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Companies.CompanyGroup", b =>
                {
                    b.HasOne("MyCompany.ECommerce.Contacts.Companies.Company", "Company")
                        .WithMany("Groups")
                        .HasForeignKey("CompanyId")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.HasOne("MyCompany.ECommerce.Contacts.Groups.Group", "Group")
                        .WithMany("Companies")
                        .HasForeignKey("CompanyId")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.Navigation("Company");

                    b.Navigation("Group");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Companies.CompanyTag", b =>
                {
                    b.HasOne("MyCompany.ECommerce.Contacts.Companies.Company", "Company")
                        .WithMany("Tags")
                        .HasForeignKey("CompanyId")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.HasOne("MyCompany.ECommerce.Contacts.Tags.Tag", "Tag")
                        .WithMany("Companies")
                        .HasForeignKey("TagId")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.Navigation("Company");

                    b.Navigation("Tag");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Groups.GroupTag", b =>
                {
                    b.HasOne("MyCompany.ECommerce.Contacts.Groups.Group", "Group")
                        .WithMany("Tags")
                        .HasForeignKey("GroupId")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.HasOne("MyCompany.ECommerce.Contacts.Tags.Tag", "Tag")
                        .WithMany("Groups")
                        .HasForeignKey("TagId")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.Navigation("Group");

                    b.Navigation("Tag");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Companies.Company", b =>
                {
                    b.Navigation("Groups");

                    b.Navigation("Tags");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Groups.Group", b =>
                {
                    b.Navigation("Companies");

                    b.Navigation("Tags");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Contacts.Tags.Tag", b =>
                {
                    b.Navigation("Companies");

                    b.Navigation("Groups");
                });
#pragma warning restore 612, 618
        }
    }
}
```

## File: `Sources/Contacts/Contacts/Groups/Group.cs`
```csharp
using JetBrains.Annotations;
using Microsoft.AspNetCore.Mvc.ModelBinding;
using MyCompany.ECommerce.Contacts.Companies;
using MyCompany.ECommerce.TechnicalStuff.Crud;
using Newtonsoft.Json;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Contacts.Groups;

[UsedImplicitly(ImplicitUseTargetFlags.WithMembers)]
[DddEntity]
public class Group : CrudEntity
{
    public string Name { get; set; }
    public string Description { get; set; }

    [BindNever]
    [JsonIgnore]
    public List<CompanyGroup> Companies { get; set; }

    [BindNever]
    [JsonIgnore]
    public List<GroupTag> Tags { get; set; }
}
```

## File: `Sources/Contacts/Contacts/Groups/GroupTag.cs`
```csharp
using JetBrains.Annotations;
using MyCompany.ECommerce.Contacts.Tags;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Contacts.Groups;

[UsedImplicitly(ImplicitUseTargetFlags.WithMembers)]
[DddEntity]
public class GroupTag
{
    public Guid GroupId { get; set; }
    public Group Group { get; set; }

    public Guid TagId { get; set; }
    public Tag Tag { get; set; }
}
```

## File: `Sources/Contacts/Contacts/Groups/OldApi/GroupsController.cs`
```csharp
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using MyCompany.ECommerce.TechnicalStuff.Crud.Api;
using MyCompany.ECommerce.TechnicalStuff.Crud.Operations;

namespace MyCompany.ECommerce.Contacts.Groups.OldApi;

[ApiController]
[Route("/api/groups")]
public class GroupsController : ControllerBase
{
    private readonly ContactsCrudOperations _operations;

    public GroupsController(ContactsCrudOperations operations) => _operations = operations;

    [HttpGet("get")]
    public Task<ActionResult<Group>> Get(Guid id) => _operations
        .Read<Group>(id, query => query
            .Include(group => group.Tags))
        .ToOkResult();

    [HttpGet("search")]
    public IAsyncEnumerable<Group> Search(string name = null, int skip = 0, int take = 20) => _operations
        .Read<Group>(query => query
            .Include(group => group.Tags)
            .Where(group => name == null || group.Name.Contains(name))
            .Skip(skip)
            .Take(take));

    [HttpPost("update")]
    public Task<ActionResult<Group>> Update(Guid id, Group group) => _operations
        .Update(id, group)
        .ToOkResult();

    [HttpPost("delete")]
    public Task<OkResult> Delete(Guid id) => _operations
        .Delete<Group>(id, DeletePolicy.Soft)
        .ToOkResult();
        
    [HttpPost("add-tag")]
    public Task<OkResult> AddTag(Guid groupId, Guid tagId) => _operations
        .Update<Group>(groupId,
            query => query.Include(group => group.Tags),
            group =>
            {
                if (group.Tags.Any(tag => tag.TagId == tagId))
                    return;
                group.Tags.Add(new GroupTag
                {
                    GroupId = groupId,
                    TagId = tagId
                });
            })
        .ToOkResult();

    [HttpPost("remove-tag")]
    public Task<OkResult> RemoveTag(Guid groupId, Guid tagId) => _operations
        .Update<Group>(groupId,
            query => query.Include(group => group.Tags),
            group =>
            {
                var tagToRemove = group.Tags.FirstOrDefault(tag => tag.TagId == tagId);
                if (tagToRemove is null)
                    return;
                group.Tags.Remove(tagToRemove);
            })
        .ToOkResult();
}
```

## File: `Sources/Contacts/Contacts/Groups/OldApi/NamespaceInfo.cs`
```csharp
using JetBrains.Annotations;
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.Contacts.Groups.OldApi;

[SkipNamespaceInDomainModulesHierarchy(ApplyOnNamespace = true)]
[UsedImplicitly]
public class NamespaceInfo { }
```

## File: `Sources/Contacts/Contacts/Groups/RestApi/GroupsController.cs`
```csharp
using Microsoft.AspNetCore.Mvc;
using MyCompany.ECommerce.TechnicalStuff.Crud.Api;
using MyCompany.ECommerce.TechnicalStuff.Crud.Operations;

namespace MyCompany.ECommerce.Contacts.Groups.RestApi;

[ApiController]
[Route("/rest/groups")]
[ApiVersion("1")]
public class GroupsController : ControllerBase
{
    private readonly ContactsCrudOperations _operations;

    public GroupsController(ContactsCrudOperations operations) => _operations = operations;

    [HttpPost]
    public Task<ActionResult<Group>> Create(Group group) => _operations
        .Create<Group>(group)
        .ToCreatedAtActionResult();
        
    [HttpGet("{id}")]
    public Task<ActionResult<Group>> Read(Guid id) => _operations
        .Read<Group>(id)
        .ToOkResult();

    [HttpGet]
    public IAsyncEnumerable<Group> Search(string name = null, int skip = 0, int take = 20) => _operations
        .Read<Group>(query => query
            .Where(group => name == null || group.Name.Contains(name))
            .Skip(skip)
            .Take(take));

    [HttpPut("{id}")]
    public Task<ActionResult<Group>> Update(Guid id, Group group) => _operations
        .Update(id, group)
        .ToOkResult();

    [HttpDelete("{id}")]
    public Task<StatusCodeResult> Delete(Guid id) => _operations
        .Delete<Group>(id, DeletePolicy.Soft)
        .ToStatusCodeResult();
}
```

## File: `Sources/Contacts/Contacts/Groups/RestApi/GroupsTagsController.cs`
```csharp
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using MyCompany.ECommerce.Contacts.Tags;
using MyCompany.ECommerce.TechnicalStuff.Crud.Api;

namespace MyCompany.ECommerce.Contacts.Groups.RestApi;

[ApiController]
[Route("/rest/groups/{groupId}/tags")]
[ApiVersion("1")]
public class GroupsTagsController : ControllerBase
{
    private readonly ContactsCrudOperations _operations;

    public GroupsTagsController(ContactsCrudOperations operations) => _operations = operations;

    [HttpGet]
    public IAsyncEnumerable<Tag> Read(Guid groupId) => _operations
        .Read<GroupTag, Tag>(query => query
            .Include(groupTag => groupTag.Tag)
            .Where(groupTag => groupTag.GroupId == groupId)
            .Select(groupTag => groupTag.Tag));
        
    [HttpPut("{tagId}")]
    public Task<NoContentResult> Add(Guid groupId, Guid tagId) => _operations
        .Update<Group>(groupId,
            query => query.Include(group => group.Tags),
            group =>
            {
                if (group.Tags.Any(tag => tag.TagId == tagId))
                    return;
                group.Tags.Add(new GroupTag
                {
                    GroupId = groupId,
                    TagId = tagId
                });
            })
        .ToNoContentResult();

    [HttpDelete("{tagId}")]
    public Task<NoContentResult> Remove(Guid groupId, Guid tagId) => _operations
        .Update<Group>(groupId,
            query => query.Include(group => group.Tags),
            group =>
            {
                var tagToRemove = group.Tags.FirstOrDefault(tag => tag.TagId == tagId);
                if (tagToRemove is null)
                    return;
                group.Tags.Remove(tagToRemove);
            })
        .ToNoContentResult();
}
```

## File: `Sources/Contacts/Contacts/Groups/RestApi/NamespaceInfo.cs`
```csharp
using JetBrains.Annotations;
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.Contacts.Groups.RestApi;

[SkipNamespaceInDomainModulesHierarchy(ApplyOnNamespace = true)]
[UsedImplicitly]
public class NamespaceInfo { }
```

## File: `Sources/Contacts/Contacts/Tags/Tag.cs`
```csharp
using JetBrains.Annotations;
using MyCompany.ECommerce.Contacts.Companies;
using MyCompany.ECommerce.Contacts.Groups;
using MyCompany.ECommerce.TechnicalStuff.Crud;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Contacts.Tags;

[UsedImplicitly(ImplicitUseTargetFlags.WithMembers)]
[DddEntity]
public class Tag : CrudEntity
{
    public string Name { get; set; }
    public string Description { get; set; }
    public List<CompanyTag> Companies { get; set; }
    public List<GroupTag> Groups { get; set; }
}
```

## File: `Sources/Contacts/Contacts/Tags/OldApi/NamespaceInfo.cs`
```csharp
using JetBrains.Annotations;
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.Contacts.Tags.OldApi;

[SkipNamespaceInDomainModulesHierarchy(ApplyOnNamespace = true)]
[UsedImplicitly]
public class NamespaceInfo { }
```

## File: `Sources/Contacts/Contacts/Tags/OldApi/TagsController.cs`
```csharp
using Microsoft.AspNetCore.Mvc;
using MyCompany.ECommerce.TechnicalStuff.Crud.Api;
using MyCompany.ECommerce.TechnicalStuff.Crud.Operations;

namespace MyCompany.ECommerce.Contacts.Tags.OldApi;

[ApiController]
[Route("/api/tags")]
public class TagsController : ControllerBase
{
    private readonly ContactsCrudOperations _operations;

    public TagsController(ContactsCrudOperations operations) => _operations = operations;

    [HttpPost("create")]
    public Task<ActionResult<Tag>> Create(Tag tag) => _operations
        .Create(tag)
        .ToOkResult();
        
    [HttpGet("get")]
    public Task<ActionResult<Tag>> Get(Guid id) => _operations
        .Read<Tag>(id)
        .ToOkResult();

    [HttpGet("search")]
    public IAsyncEnumerable<Tag> Search(string name = null, int skip = 0, int take = 20) => _operations
        .Read<Tag>(query => query
            .Where(tag => name == null || tag.Name.Contains(name))
            .Skip(skip)
            .Take(take));

    [HttpPost("update")]
    public Task<ActionResult<Tag>> Update(Guid id, Tag tag) => _operations
        .Update(id, tag)
        .ToOkResult();

    [HttpPost("delete")]
    public Task<OkResult> Delete(Guid id) => _operations
        .Delete<Tag>(id, DeletePolicy.Hard)
        .ToOkResult();
}
```

## File: `Sources/Contacts/Contacts/Tags/RestApi/NamespaceInfo.cs`
```csharp
using JetBrains.Annotations;
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.Contacts.Tags.RestApi;

[SkipNamespaceInDomainModulesHierarchy(ApplyOnNamespace = true)]
[UsedImplicitly]
public class NamespaceInfo { }
```

## File: `Sources/Contacts/Contacts/Tags/RestApi/TagsController.cs`
```csharp
using Microsoft.AspNetCore.Mvc;
using MyCompany.ECommerce.TechnicalStuff.Crud.Api;
using MyCompany.ECommerce.TechnicalStuff.Crud.Operations;

namespace MyCompany.ECommerce.Contacts.Tags.RestApi;

[ApiController]
[Route("/rets/tags")]
[ApiVersion("1")]
public class TagsController : ControllerBase
{
    private readonly ContactsCrudOperations _operations;

    public TagsController(ContactsCrudOperations operations) => _operations = operations;

    [HttpPost]
    public Task<ActionResult<Tag>> Create(Tag tag) => _operations
        .Create(tag)
        .ToCreatedAtActionResult();
        
    [HttpGet("{id}")]
    public Task<ActionResult<Tag>> Read(Guid id) => _operations
        .Read<Tag>(id)
        .ToOkResult();

    [HttpGet]
    public IAsyncEnumerable<Tag> Search(string name = null, int skip = 0, int take = 20) => _operations
        .Read<Tag>(query => query
            .Where(tag => name == null || tag.Name.Contains(name))
            .Skip(skip)
            .Take(take));

    [HttpPut("{id}")]
    public Task<ActionResult<Tag>> Update(Guid id, Tag tag) => _operations
        .Update(id, tag)
        .ToOkResult();

    [HttpDelete("{id}")]
    public Task<StatusCodeResult> Delete(Guid id) => _operations
        .Delete<Tag>(id, DeletePolicy.Hard)
        .ToStatusCodeResult();
}
```

## File: `Sources/Monolith.Startup/Monolith.Startup.csproj`
```
﻿<Project Sdk="Microsoft.NET.Sdk.Web">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <AssemblyName>MyCompany.ECommerce.Startup</AssemblyName>
        <RootNamespace>MyCompany.ECommerce</RootNamespace>        
        <UserSecretsId>MyCompanyCrm</UserSecretsId>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
    </PropertyGroup>

    <ItemGroup>        
        <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />        
        <PackageReference Include="Microsoft.AspNetCore.Mvc.NewtonsoftJson" Version="8.0.5" />        
        <PackageReference Include="Microsoft.EntityFrameworkCore.Design" Version="8.0.5">
          <PrivateAssets>all</PrivateAssets>
          <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
        </PackageReference>
        <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
        <PackageReference Include="Npgsql.EntityFrameworkCore.PostgreSQL" Version="8.0.4" />
        <PackageReference Include="Scrutor" Version="4.2.2" />
    </ItemGroup>

    <ItemGroup>
      <ProjectReference Include="..\Contacts\Contacts\Contacts.csproj" />
      <ProjectReference Include="..\Payments\Payments.ProcessModel\Payments.ProcessModel.csproj" />
      <ProjectReference Include="..\ProductsDelivery\ProductsDelivery.ProcessModel\ProductsDelivery.ProcessModel.csproj" />
      <ProjectReference Include="..\RiskManagement\RiskManagement.ProcessModel\RiskManagement.ProcessModel.csproj" />
      <ProjectReference Include="..\Sales\Sales.Adapters\Sales.Adapters.csproj" />
      <ProjectReference Include="..\Sales\Sales.DeepModel\Sales.DeepModel.csproj" />
      <ProjectReference Include="..\Sales\Sales.ProcessModel\Sales.ProcessModel.csproj" />
      <ProjectReference Include="..\Sales\Sales.RestApi\Sales.RestApi.csproj" />
      <ProjectReference Include="..\TechnicalStuff\TechnicalStuff.Api\TechnicalStuff.Api.csproj" />
      <ProjectReference Include="..\TechnicalStuff\TechnicalStuff.Json\TechnicalStuff.Json.csproj" />
      <ProjectReference Include="..\TechnicalStuff\TechnicalStuff.Marten\TechnicalStuff.Marten.csproj" />
      <ProjectReference Include="..\TechnicalStuff\TechnicalStuff.Outbox.Quartz\TechnicalStuff.Outbox.Quartz.csproj" />
      <ProjectReference Include="..\TechnicalStuff\TechnicalStuff.ProcessModel\TechnicalStuff.ProcessModel.csproj" />
      <ProjectReference Include="..\TechnicalStuff\TechnicalStuff.Transactions\TechnicalStuff.Transactions.csproj" />
    </ItemGroup>

</Project>
```

## File: `Sources/Monolith.Startup/Program.cs`
```csharp
﻿using System.Text.Json.Serialization;
using Microsoft.AspNetCore.Http.Json;
using MyCompany.ECommerce.DI;
using MyCompany.ECommerce.DI.Modules;
using MyCompany.ECommerce.Infrastructure;
using MyCompany.ECommerce.Sales;
using MyCompany.ECommerce.TechnicalStuff.Api.Versioning;
using MyCompany.ECommerce.TechnicalStuff.Json.Json;
using MyCompany.ECommerce.TechnicalStuff.Persistence;
using NoesisVision.Annotations.Technology;
using NoesisVision.Annotations.Technology.CleanArchitecture;

[assembly: DeployableUnit("ecommerce-monolith")]
[assembly: Tier("Application")]
[assembly: FrameworkLayer]

var builder = WebApplication.CreateBuilder(args);
ConfigureSerialization();
ConfigureApiServices();
ConfigureDatabases();
ConfigureMessagingServices();
ConfigureModulesServices();
ConfigureDecorators();

var app = builder.Build();
app.UseRouting();
app.MapControllers();
app.UseOpenApi();
app.Run();
return;

void ConfigureSerialization()
{
    builder.Services.Configure<JsonOptions>(options =>
    {
        var converters = options.SerializerOptions.Converters;
        options.SerializerOptions.PropertyNameCaseInsensitive = true;
        converters.Add(new JsonStringEnumConverter());
        converters.Add(new ValueObjectJsonConverterFactory());
    });
}

void ConfigureApiServices()
{
    builder.Services.AddControllers();
    // TODO: additional media types in Open API documents

    // Versioning whole API is done by path segment (manually in Route attribute).
    // Each endpoint in each API version can also be versioned independently by query parameter.
    builder.Services.AddEndpointVersioningByQueryParameter();
    builder.Services.AddApiVersionDocument(options =>
    {
        options.PathPrefix = "api";
        options.Title = "Old API";
        options.Description = @"
It's the old API that's supported only for backward compatibility with some clients.
Use REST API instead whenever possible.";
        options.UseEndpointVersioning = false;
    });
    builder.Services.AddApiVersionDocument(options =>
    {
        options.PathPrefix = "rest";
        options.Title = "REST API";
        options.UseEndpointVersioning = true;
    });
}

void ConfigureDatabases()
{
    var connectionString = builder.Configuration.GetConnectionString("Main");
    builder.Services.AddScoped<MainDb>(_ => new MainECommerceDb(connectionString));
}

void ConfigureMessagingServices()
{
    builder.Services.AddOutboxesRegistry();
    builder.Services.AddKafka(builder.Configuration);
    builder.Services.AddSingleton<FakeMessageBroker>();
    builder.Services.AddHostedService<FakeMessageConsumer>();
}

void ConfigureModulesServices()
{
    builder.Services.AddSalesModule(builder.Configuration);
    builder.Services.AddContactsModule(builder.Configuration);
}

void ConfigureDecorators()
{
    builder.Services.DecorateCommandHandlers();
}

namespace MyCompany.ECommerce
{
    public partial class Program { }
}
```

## File: `Sources/Monolith.Startup/app.config`
```
﻿<?xml version="1.0" encoding="utf-8" ?>
<configuration>
  <runtime>
    <gcServer enabled="true"/>
  </runtime>
</configuration>
```

## File: `Sources/Monolith.Startup/appsettings.Development.json`
```json
{
  "ConnectionStrings": {    
    "Main": "Server=localhost;Port=5432;Database=Crm;User Id=postgres;Password=password;"
  },
  "Logging": {
    "LogLevel": {
      "Default": "Debug",
      "System": "Information",
      "Microsoft": "Information"
    }
  },
  "KafkaProducer": {
    "BootstrapServers": "localhost:9092"
  }
}
```

## File: `Sources/Monolith.Startup/appsettings.json`
```json
{
  "Logging": {
    "LogLevel": {
      "Default": "Warning"
    }
  },
  "AllowedHosts": "*" ,
  "KafkaProducer": {
    "Acks": "All",
    "MessageSendMaxRetries": 3,
    "RetryBackoffMs": 1000,
    "EnableIdempotence": true
  }
}
```

## File: `Sources/Monolith.Startup/DI/ConventionBasedRegistrations.cs`
```csharp
using System.Reflection;
using NoesisVision.Annotations.Domain;
using NoesisVision.Annotations.Domain.DDD;
using Scrutor;

namespace MyCompany.ECommerce.DI;

public static class ConventionBasedRegistrations
{
    public static IServiceCollection AddStatelessComponentsFrom(this IServiceCollection services,
        params Assembly[] assemblies) =>
        services.Scan(selector => selector
            .FromAssemblies(assemblies)
            .AddClasses(filter => filter.WithAnyAttribute(
                    typeof(DddRepositoryAttribute),
                    typeof(DddFactoryAttribute),
                    typeof(DddDomainServiceAttribute),
                    typeof(DddApplicationServiceAttribute),
                    typeof(ExternalSystemIntegrationAttribute)),
                false)
            .AsSelfWithInterfaces()
            .WithScopedLifetime());

    private static IImplementationTypeFilter WithAnyAttribute(this IImplementationTypeFilter filter,
        params Type[] attributes) =>
        filter.Where(t => attributes.Any(a => t.HasAttribute(a)));

    private static bool HasAttribute(this Type type, Type attributeType) =>
        type.GetTypeInfo().IsDefined(attributeType, inherit: true);
}
```

## File: `Sources/Monolith.Startup/DI/CrossCuttingConcerns.cs`
```csharp
using System.Reflection;
using MyCompany.ECommerce.TechnicalStuff.Outbox;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;
using MyCompany.ECommerce.TechnicalStuff.Transactions;

namespace MyCompany.ECommerce.DI;

public static class CrossCuttingConcerns
{
    public static IServiceCollection AddOutboxesRegistry(this IServiceCollection services)
    {
        services.AddScoped<TransactionalOutboxes>();
        services.AddScoped<NonTransactionalOutboxes>();
        return services;
    }
        
    public static IServiceCollection AddMessageOutboxes(this IServiceCollection services,
        params Assembly[] assemblies)
    {
        services.Scan(selector => selector
            .FromAssemblies(assemblies)
            .AddClasses(filter => filter
                .AssignableToAny(typeof(TransactionalOutbox), typeof(NonTransactionalOutbox)))
            .AsSelfWithInterfaces()
            .WithScopedLifetime());
        // TODO: registering types
        services.AddSingleton<MessageTypes>();
        return services;
    }

    public static IServiceCollection DecorateCommandHandlers(this IServiceCollection services)
    {
        services.TryDecorate(typeof(CommandHandler<>), typeof(TransactionalMessageSendingDecorator<>));
        services.TryDecorate(typeof(CommandHandler<,>), typeof(TransactionalMessageSendingDecorator<,>));
        services.TryDecorate(typeof(CommandHandler<>), typeof(AmbientTransactionDecorator<>));
        services.TryDecorate(typeof(CommandHandler<,>), typeof(AmbientTransactionDecorator<,>));
        services.TryDecorate(typeof(CommandHandler<>), typeof(NonTransactionalMessageSendingDecorator<>));
        services.TryDecorate(typeof(CommandHandler<,>), typeof(NonTransactionalMessageSendingDecorator<,>));
        return services;
    }
}
```

## File: `Sources/Monolith.Startup/DI/Kafka.cs`
```csharp
using Confluent.Kafka;
using MyCompany.ECommerce.TechnicalStuff.Kafka;

namespace MyCompany.ECommerce.DI;

public static class Kafka
{
    public static IServiceCollection AddKafka(this IServiceCollection services, IConfiguration configuration)
    {
        var producerConfig = configuration.GetSection("KafkaProducer").Get<ProducerConfig>();
        services.AddSingleton(producerConfig);
        services.AddSingleton<KafkaMessageProducer>();
        return services;
    }
}
```

## File: `Sources/Monolith.Startup/DI/Modules/Contacts.cs`
```csharp
using Microsoft.EntityFrameworkCore;
using MyCompany.ECommerce.Contacts;
using MyCompany.ECommerce.Contacts.Database;

namespace MyCompany.ECommerce.DI.Modules;

internal static class ContactsRegistrations
{
    public static IServiceCollection AddContactsModule(this IServiceCollection services,
        IConfiguration configuration)
    {
        services.AddDbContextPool<ContactsDbContext>(options => options
            .UseNpgsql(configuration.GetConnectionString("Main"), npgsqlOptions => npgsqlOptions
                .MigrationsHistoryTable("__Contacts_Migrations")));
        services.AddScoped<ContactsCrudOperations, ContactsEfDao>();
        return services;
    }
}
```

## File: `Sources/Monolith.Startup/DI/Modules/Sales.cs`
```csharp
using System.Reflection;
using System.Text.Json.Serialization;
using Marten;
using Marten.Events;
using Marten.Services;
using Microsoft.EntityFrameworkCore;
using MyCompany.ECommerce.Sales;
using MyCompany.ECommerce.Sales.Database.Sql.EF;
using MyCompany.ECommerce.Sales.Orders;
using MyCompany.ECommerce.Sales.Orders.PriceChanges;
using MyCompany.ECommerce.TechnicalStuff.Json.Json;
using MyCompany.ECommerce.TechnicalStuff.Marten;
using MyCompany.ECommerce.TechnicalStuff.Outbox.Postgres;
using RepoDb;
using DbOrder = MyCompany.ECommerce.Sales.Database.Sql.Documents.DbOrder;

namespace MyCompany.ECommerce.DI.Modules;

internal static class Sales
{
    private static readonly Assembly SalesDeepModel = typeof(SalesDeepModelLayerInfo).Assembly;
    private static readonly Assembly SalesProcessModel = typeof(SalesProcessModelLayerInfo).Assembly;
    private static readonly Assembly SalesAdapters = typeof(SalesAdaptersLayerInfo).Assembly;

    public static IServiceCollection AddSalesModule(this IServiceCollection services,
        IConfiguration configuration)
    {
        var connectionString = configuration.GetConnectionString("Main");
        GlobalConfiguration.Setup().UsePostgreSql();
        // TODO: Same connection provider for all data access libraries (EF, Marten, RepoDB) 
        services.AddDbContextPool<SalesDbContext>(options => options
            .UseNpgsql(connectionString, npgsqlOptions => npgsqlOptions
                .MigrationsHistoryTable("__Sales_Migrations")));
        services.AddMarten(options =>
            {
                options.Connection(connectionString);
                var serializer = new SystemTextJsonSerializer();
                serializer.Customize(serializerOptions =>
                {
                    var converters = serializerOptions.Converters;
                    serializerOptions.PropertyNameCaseInsensitive = true;
                    converters.Add(new JsonStringEnumConverter());
                    converters.Add(new ValueObjectJsonConverterFactory());
                });
                options.Serializer(serializer);
                options.Events.StreamIdentity = StreamIdentity.AsGuid;
                foreach (var (type, name) in OrderSqlRepository.EventsSourcing.Events)
                {
                    options.Events.AddEventType(type);
                    options.Events.MapEventType(type, name);
                }
                options.Schema.For<DbOrder>().UseOptimisticConcurrency(true);
            })
            .BuildSessionsWith<LightweightSessionFactory>()
            .InitializeWith();
        services.AddScoped<SalesCrudOperations, SalesCrudEfDao>();
        services.AddMessageOutboxes(SalesAdapters);
        services.AddScoped<OrderEventsOutbox, FakeOrderEventOutbox>();
        services.AddScoped<PostgresOutboxRepository>();
        services.AddStatelessComponentsFrom(SalesDeepModel, SalesProcessModel, SalesAdapters);
        services.AddScoped<Order.Repository, OrderSqlRepository.Raw>();
        services.AddScoped<AllowAnyPriceChanges>();
        services.AddScoped<AllowPriceChangesIfTotalPriceIsLower>();
        return services;
    }
}
```

## File: `Sources/Monolith.Startup/Infrastructure/FakeMessageConsumer.cs`
```csharp
using MyCompany.ECommerce.Sales;
using MyCompany.ECommerce.TechnicalStuff;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Infrastructure;

public class FakeMessageConsumer(
    FakeMessageBroker broker,
    IServiceScopeFactory scopeFactory,
    ILogger<FakeMessageConsumer> logger)
    : BackgroundService
{
    protected override Task ExecuteAsync(CancellationToken stoppingToken) => Task.WhenAll(
        ConsumeCommand(stoppingToken),
        ConsumeEvent(stoppingToken));

    private async Task ConsumeCommand(CancellationToken cancellationToken)
    {
        while (!cancellationToken.IsCancellationRequested)
        {
            var command = await broker.ReadCommand(cancellationToken);
            logger.LogDebug("Handling command started. Command type: {CommandType}", command.GetType().Name);
            using var scope = scopeFactory.CreateScope();
            var handler = (MessageHandler) scope.ServiceProvider.GetService(CreateCommandHandlerTypeFor(command));
            try
            {
                await handler.Handle(command);
            }
            catch (DomainError e)
            {
                logger.LogError(e, "Domain error");
            }
            logger.LogDebug("Handling command finished. Command type: {CommandType}", command.GetType().Name);
        }
    }

    private static Type CreateCommandHandlerTypeFor(Command command) =>
        typeof(CommandHandler<>).MakeGenericType(command.GetType());

    private async Task ConsumeEvent(CancellationToken cancellationToken)
    {
        while (!cancellationToken.IsCancellationRequested)
        {
            var domainEvent = await broker.ReadEvent(cancellationToken);
            logger.LogDebug("Handling event started. Command type: {EventType}", domainEvent.GetType().Name);
            using var scope = scopeFactory.CreateScope();
            var handler =
                (MessageHandler) scope.ServiceProvider.GetService(CreateEventHandlerTypeFor(domainEvent));
            try
            {
                await handler.Handle(domainEvent);
            }
            catch (DomainError e)
            {
                logger.LogError(e, "Domain error");
            }
            logger.LogDebug("Handling event finished. Command type: {EventType}", domainEvent.GetType().Name);
        }
    }

    private static Type CreateEventHandlerTypeFor(DomainEvent domainEvent) =>
        typeof(DomainEventHandler<>).MakeGenericType(domainEvent.GetType());
}
```

## File: `Sources/Monolith.Startup/Infrastructure/MainECommerceDb.cs`
```csharp
using MyCompany.ECommerce.TechnicalStuff.Persistence;
using MyCompany.ECommerce.TechnicalStuff.Postgres;
using NoesisVision.Annotations.Technology;

namespace MyCompany.ECommerce.Infrastructure;

[Database("Main", ServerName = "Postgres")]
public class MainECommerceDb : PostgresTransactionProvider, MainDb
{
    public MainECommerceDb(string connectionString) : base(connectionString) { }
}
```

## File: `Sources/Monolith.Startup/Properties/launchSettings.json`
```json
﻿{
  "$schema": "http://json.schemastore.org/launchsettings.json",
  "profiles": {    
    "Dev": {
      "commandName": "Project",
      "launchBrowser": false,
      "launchUrl": "",
      "applicationUrl": "http://localhost:5000",
      "environmentVariables": {
        "ASPNETCORE_ENVIRONMENT": "Development"
      }
    }
  }
}
```

## File: `Sources/Payments/PaymentModelInfo.json`
```json
{
  "ModelBoundary": "Payments",
  "BusinessOwner": "Sales department",
  "DevelopmentOwner": "Supporting team"
}
```

## File: `Sources/Payments/Payments.Adapters.Api/Payments.Adapters.Api.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
        <RootNamespace>MyCompany.ECommerce.Payments</RootNamespace>
        <AssemblyName>MyCompany.ECommerce.Payments.Adapters.Api</AssemblyName>        
    </PropertyGroup>

    <ItemGroup>
      <ProjectReference Include="..\Payments.ProcessModel\Payments.ProcessModel.csproj" />
    </ItemGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/Payments/Payments.Adapters.Api/PaymentsAdaptersApiLayerInfo.cs`
```csharp
using System.Reflection;
using JetBrains.Annotations;
using NoesisVision.Annotations.Technology.CleanArchitecture;

[assembly: AdaptersLayer]

namespace MyCompany.ECommerce.Payments;

[UsedImplicitly]
public static class PaymentsAdaptersApiLayerInfo
{
    public static Assembly Assembly => typeof(PaymentsAdaptersApiLayerInfo).Assembly;
}
```

## File: `Sources/Payments/Payments.Adapters.Out/Payments.Adapters.Out.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
        <AssemblyName>MyCompany.ECommerce.Payments.Adapters.Out</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.Payments</RootNamespace>        
    </PropertyGroup>

    <ItemGroup>
      <ProjectReference Include="..\Payments.DeepModel\Payments.DeepModel.csproj" />
      <ProjectReference Include="..\Payments.ProcessModel\Payments.ProcessModel.csproj" />
    </ItemGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/Payments/Payments.Adapters.Out/PaymentsAdaptersOutLayerInfo.cs`
```csharp
using System.Reflection;
using JetBrains.Annotations;
using NoesisVision.Annotations.Technology.CleanArchitecture;

[assembly: AdaptersLayer]

namespace MyCompany.ECommerce.Payments;

[UsedImplicitly]
public static class PaymentsAdaptersOutLayerInfo
{
    public static Assembly Assembly => typeof(PaymentsAdaptersOutLayerInfo).Assembly;
}
```

## File: `Sources/Payments/Payments.DeepModel/Payments.DeepModel.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
        <AssemblyName>MyCompany.ECommerce.Payments.DeepModel</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.Payments</RootNamespace>
    </PropertyGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/Payments/Payments.DeepModel/PaymentsDeepModelLayerInfo.cs`
```csharp
using System.Reflection;
using JetBrains.Annotations;
using NoesisVision.Annotations.Domain;
using NoesisVision.Annotations.Technology.CleanArchitecture;

[assembly: EntitiesLayer]
[assembly: DomainModel]

namespace MyCompany.ECommerce.Payments;

[UsedImplicitly]
public class PaymentsDeepModelLayerInfo
{
    public static Assembly Assembly => typeof(PaymentsDeepModelLayerInfo).Assembly;
}
```

## File: `Sources/Payments/Payments.ProcessModel/PaymentProcess.cs`
```csharp
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.Payments;

[Process(Name, ApplyOnNamespace = true)]
public static class PaymentProcess
{
    public const string Name = "Payment";
}
```

## File: `Sources/Payments/Payments.ProcessModel/Payments.ProcessModel.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <AssemblyName>MyCompany.ECommerce.Payments.ProcessModel</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.Payments</RootNamespace>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
    </PropertyGroup>

    <ItemGroup>
      <ProjectReference Include="..\..\TechnicalStuff\TechnicalStuff.ProcessModel\TechnicalStuff.ProcessModel.csproj" />
      <ProjectReference Include="..\Payments.DeepModel\Payments.DeepModel.csproj" />
    </ItemGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/Payments/Payments.ProcessModel/PaymentsProcessModelLayerInfo.cs`
```csharp
using System.Reflection;
using JetBrains.Annotations;
using NoesisVision.Annotations.Domain;
using NoesisVision.Annotations.Technology.CleanArchitecture;

[assembly: UseCasesLayer]
[assembly: DomainModel]

namespace MyCompany.ECommerce.Payments;

[UsedImplicitly]
public class PaymentsProcessModelLayerInfo
{
    public static Assembly Assembly => typeof(PaymentsProcessModelLayerInfo).Assembly;
}
```

## File: `Sources/Payments/Payments.ProcessModel/Requesting/PaymentRequestFulfilled.cs`
```csharp
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Payments.Requesting;

public class PaymentRequestFulfilled(Guid requestId, DateTime fulfilledOn) : DomainEvent
{
    public Guid RequestId { get; } = requestId;
    public DateTime FulfilledOn { get; } = fulfilledOn;
}
```

## File: `Sources/Payments/Payments.ProcessModel/Requesting/RequestPayment.cs`
```csharp
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Payments.Requesting;

public readonly struct RequestPayment(Guid requestId, Guid clientId, decimal amount, string currencyCode) : Command
{
    public Guid RequestId { get; } = requestId;
    public Guid ClientId { get; } = clientId;
    public decimal Amount { get; } = amount;
    public string CurrencyCode { get; } = currencyCode;
}
```

## File: `Sources/Payments/Payments.ProcessModel/Requesting/RequestPaymentHandler.cs`
```csharp
using JetBrains.Annotations;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.Payments.Requesting;

[UsedImplicitly]
public class RequestPaymentHandler : CommandHandler<RequestPayment>
{
    [EntryPoint(nameof(RequestPayment), Process = PaymentProcess.Name)]
    public Task Handle(RequestPayment command)
    {
        throw new System.NotImplementedException();
    }
}
```

## File: `Sources/ProductsDelivery/ProductsDeliveryModelInfo.json`
```json
{
  "ModelBoundary": "Products Delivery",
  "BusinessOwner": "Inventory department",
  "DevelopmentOwner": "Inventory team"
}
```

## File: `Sources/ProductsDelivery/ProductsDelivery.Adapters.Api/ProductsDelivery.Adapters.Api.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
        <AssemblyName>MyCompany.ECommerce.ProductsDelivery.Adapters.Api</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.ProductsDelivery</RootNamespace>
    </PropertyGroup>

    <ItemGroup>
      <ProjectReference Include="..\ProductsDelivery.ProcessModel\ProductsDelivery.ProcessModel.csproj" />
    </ItemGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/ProductsDelivery/ProductsDelivery.Adapters.Api/ProductsDeliveryAdaptersApiLayerInfo.cs`
```csharp
using System.Reflection;
using JetBrains.Annotations;
using NoesisVision.Annotations.Technology.CleanArchitecture;

[assembly: AdaptersLayer]

namespace MyCompany.ECommerce.ProductsDelivery;

[UsedImplicitly]
public class ProductsDeliveryAdaptersApiLayerInfo
{
    public static Assembly Assembly => typeof(ProductsDeliveryAdaptersApiLayerInfo).Assembly;
}
```

## File: `Sources/ProductsDelivery/ProductsDelivery.Adapters.Out/ProductsDelivery.Adapters.Out.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
        <AssemblyName>MyCompany.ECommerce.ProductsDelivery.Adapters.Out</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.ProductsDelivery</RootNamespace>
    </PropertyGroup>

    <ItemGroup>
      <ProjectReference Include="..\ProductsDelivery.DeepModel\ProductsDelivery.DeepModel.csproj" />
      <ProjectReference Include="..\ProductsDelivery.ProcessModel\ProductsDelivery.ProcessModel.csproj" />
    </ItemGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/ProductsDelivery/ProductsDelivery.Adapters.Out/ProductsDeliveryProcessModelLayerInfo.cs`
```csharp
using System.Reflection;
using JetBrains.Annotations;
using NoesisVision.Annotations.Technology.CleanArchitecture;

[assembly: AdaptersLayer]

namespace MyCompany.ECommerce.ProductsDelivery;

[UsedImplicitly]
public class ProductsDeliveryProcessModelLayerInfo
{
    public static Assembly Assembly => typeof(ProductsDeliveryProcessModelLayerInfo).Assembly;
}
```

## File: `Sources/ProductsDelivery/ProductsDelivery.DeepModel/ProductsDelivery.DeepModel.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
        <AssemblyName>MyCompany.ECommerce.ProductsDelivery.DeepModel</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.ProductsDelivery</RootNamespace>
    </PropertyGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/ProductsDelivery/ProductsDelivery.DeepModel/ProductsDeliveryDeepModelLayerInfo.cs`
```csharp
using System.Reflection;
using JetBrains.Annotations;
using NoesisVision.Annotations.Domain;
using NoesisVision.Annotations.Technology.CleanArchitecture;

[assembly: EntitiesLayer]
[assembly: DomainModel]

namespace MyCompany.ECommerce.ProductsDelivery;

[UsedImplicitly]
public class ProductsDeliveryDeepModelLayerInfo
{
    public static Assembly Assembly => typeof(ProductsDeliveryDeepModelLayerInfo).Assembly;
}
```

## File: `Sources/ProductsDelivery/ProductsDelivery.ProcessModel/ProductsDelivery.ProcessModel.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <AssemblyName>MyCompany.ECommerce.ProductsDelivery.ProcessModel</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.ProductsDelivery</RootNamespace>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
    </PropertyGroup>

    <ItemGroup>
      <Compile Remove="Class1.cs" />
    </ItemGroup>

    <ItemGroup>
      <ProjectReference Include="..\..\TechnicalStuff\TechnicalStuff.ProcessModel\TechnicalStuff.ProcessModel.csproj" />
      <ProjectReference Include="..\ProductsDelivery.DeepModel\ProductsDelivery.DeepModel.csproj" />
    </ItemGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/ProductsDelivery/ProductsDelivery.ProcessModel/ProductsDeliveryProcess.cs`
```csharp
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.ProductsDelivery;

[Process(Name, ApplyOnNamespace = true)]
public static class ProductsDeliveryProcess
{
    public const string Name = "Products delivery";
}
```

## File: `Sources/ProductsDelivery/ProductsDelivery.ProcessModel/ProductsDeliveryProcessModelLayerInfo.cs`
```csharp
using System.Reflection;
using JetBrains.Annotations;
using NoesisVision.Annotations.Domain;
using NoesisVision.Annotations.Technology.CleanArchitecture;

[assembly: UseCasesLayer]
[assembly: DomainModel]

namespace MyCompany.ECommerce.ProductsDelivery;

[UsedImplicitly]
public class ProductsDeliveryProcessModelLayerInfo
{
    public static Assembly Assembly => typeof(ProductsDeliveryProcessModelLayerInfo).Assembly;
}
```

## File: `Sources/ProductsDelivery/ProductsDelivery.ProcessModel/Requesting/RequestDelivery.cs`
```csharp
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.ProductsDelivery.Requesting;

public readonly struct RequestDelivery : Command { }
```

## File: `Sources/ProductsDelivery/ProductsDelivery.ProcessModel/Requesting/RequestDeliveryHandler.cs`
```csharp
using JetBrains.Annotations;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.ProductsDelivery.Requesting;

[UsedImplicitly]
public class RequestDeliveryHandler : CommandHandler<RequestDelivery>
{
    [EntryPoint(nameof(RequestDelivery), Process = ProductsDeliveryProcess.Name)]
    public Task Handle(RequestDelivery command)
    {
        throw new NotImplementedException();
    }
}
```

## File: `Sources/RiskManagement/RiskManagementModelInfo.json`
```json
{
  "ModelBoundary": "Risk Management",
  "BusinessOwner": "Sales department",
  "DevelopmentOwner": "Core team"
}
```

## File: `Sources/RiskManagement/RiskManagement.Adapters.Api/RiskManagement.Adapters.Api.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
        <AssemblyName>MyCompany.ECommerce.RiskManagement.Adapters.Api</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.RiskManagement</RootNamespace>
    </PropertyGroup>

    <ItemGroup>
      <ProjectReference Include="..\RiskManagement.ProcessModel\RiskManagement.ProcessModel.csproj" />
    </ItemGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/RiskManagement/RiskManagement.Adapters.Api/RiskManagementAdaptersApiLayerInfo.cs`
```csharp
using System.Reflection;
using JetBrains.Annotations;
using NoesisVision.Annotations.Technology.CleanArchitecture;

[assembly: AdaptersLayer]

namespace MyCompany.ECommerce.RiskManagement;

[UsedImplicitly]
public class RiskManagementAdaptersApiLayerInfo
{
    public static Assembly Assembly => typeof(RiskManagementAdaptersApiLayerInfo).Assembly;
}
```

## File: `Sources/RiskManagement/RiskManagement.Adapters.Out/RiskManagement.Adapters.Out.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
        <AssemblyName>MyCompany.ECommerce.RiskManagement.Adapters.Out</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.RiskManagement</RootNamespace>
    </PropertyGroup>

    <ItemGroup>
      <ProjectReference Include="..\RiskManagement.DeepModel\RiskManagement.DeepModel.csproj" />
      <ProjectReference Include="..\RiskManagement.ProcessModel\RiskManagement.ProcessModel.csproj" />
    </ItemGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/RiskManagement/RiskManagement.Adapters.Out/RiskManagementAdaptersOutLayerInfo.cs`
```csharp
using System.Reflection;
using JetBrains.Annotations;
using NoesisVision.Annotations.Technology.CleanArchitecture;

[assembly: AdaptersLayer]

namespace MyCompany.ECommerce.RiskManagement;

[UsedImplicitly]
public class RiskManagementAdaptersOutLayerInfo
{
    public static Assembly Assembly => typeof(RiskManagementAdaptersOutLayerInfo).Assembly;
}
```

## File: `Sources/RiskManagement/RiskManagement.DeepModel/RiskManagement.DeepModel.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
        <AssemblyName>MyCompany.ECommerce.RiskManagement.DeepModel</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.RiskManagement</RootNamespace>
    </PropertyGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/RiskManagement/RiskManagement.DeepModel/RiskManagementDeepModelLayerInfo.cs`
```csharp
using System.Reflection;
using JetBrains.Annotations;
using NoesisVision.Annotations.Domain;
using NoesisVision.Annotations.Technology.CleanArchitecture;

[assembly: EntitiesLayer]
[assembly: DomainModel]

namespace MyCompany.ECommerce.RiskManagement;

[UsedImplicitly]
public class RiskManagementDeepModelLayerInfo
{
    public static Assembly Assembly => typeof(RiskManagementDeepModelLayerInfo).Assembly;
}
```

## File: `Sources/RiskManagement/RiskManagement.ProcessModel/GetMaxAmount.cs`
```csharp
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.RiskManagement;

public record GetMaxAmount(string ClientId) : Command;
```

## File: `Sources/RiskManagement/RiskManagement.ProcessModel/RiskManagement.ProcessModel.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <AssemblyName>MyCompany.ECommerce.RiskManagement.ProcessModel</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.RiskManagement</RootNamespace>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
    </PropertyGroup>    

    <ItemGroup>
      <Compile Remove="Class1.cs" />
    </ItemGroup>    

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>    

    <ItemGroup>
      <ProjectReference Include="..\..\TechnicalStuff\TechnicalStuff.ProcessModel\TechnicalStuff.ProcessModel.csproj" />
      <ProjectReference Include="..\RiskManagement.DeepModel\RiskManagement.DeepModel.csproj" />
    </ItemGroup>

</Project>
```

## File: `Sources/RiskManagement/RiskManagement.ProcessModel/RiskManagementProcess.cs`
```csharp
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.RiskManagement;

[Process(Name, ApplyOnNamespace = true)]
public static class RiskManagementProcess
{
    public const string Name = "Risk management";
}
```

## File: `Sources/RiskManagement/RiskManagement.ProcessModel/RiskManagementProcessModelLayerInfo.cs`
```csharp
using System.Reflection;
using JetBrains.Annotations;
using NoesisVision.Annotations.Domain;
using NoesisVision.Annotations.Technology.CleanArchitecture;

[assembly: UseCasesLayer]
[assembly: DomainModel]

namespace MyCompany.ECommerce.RiskManagement;

[UsedImplicitly]
public class RiskManagementProcessModelLayerInfo
{
    public static Assembly Assembly => typeof(RiskManagementProcessModelLayerInfo).Assembly;
}
```

## File: `Sources/RiskManagement/RiskManagement.ProcessModel/Calculation/RiskScoreCalculationProcess.cs`
```csharp
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.RiskManagement.Calculation;

[Process(Name, ApplyOnNamespace = true)]
public static class RiskScoreCalculationProcess
{
    public const string Name = "Risk score calculation";
}
```

## File: `Sources/RiskManagement/RiskManagement.ProcessModel/Publication/GetRiskScore.cs`
```csharp
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.RiskManagement.Publication;

public readonly record struct GetRiskScore(Guid ClientId) : Query;
```

## File: `Sources/RiskManagement/RiskManagement.ProcessModel/Publication/GetRiskScoreHandler.cs`
```csharp
using JetBrains.Annotations;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.RiskManagement.Publication;

[UsedImplicitly]
public class GetRiskScoreHandler : QueryHandler<GetRiskScore, decimal>
{
    [EntryPoint(nameof(GetRiskScore), Process = RiskScorePublicationProcess.Name)]
    public Task<decimal> Handle(GetRiskScore query)
    {
        throw new NotImplementedException();
    }
}
```

## File: `Sources/RiskManagement/RiskManagement.ProcessModel/Publication/RiskScorePublicationProcess.cs`
```csharp
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.RiskManagement.Publication;

[Process(Name, ApplyOnNamespace = true)]
public class RiskScorePublicationProcess
{
    public const string Name = "Risk score publication";
}
```

## File: `Sources/Sales/SalesDomainModelInfo.json`
```json
{
  "ModelBoundary": "Sales",
  "BusinessOwner": "Sales department",
  "DevelopmentOwner": "Core team"
}
```

## File: `Sources/Sales/Sales.Adapters/FakeMessageBroker.cs`
```csharp
using System.Threading.Channels;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Sales;

public class FakeMessageBroker
{
    private readonly Channel<Command> _commands = Channel.CreateUnbounded<Command>(new UnboundedChannelOptions
    {
        SingleWriter = false,
        SingleReader = true,
        AllowSynchronousContinuations = false
    });

    private readonly Channel<DomainEvent> _events = Channel.CreateUnbounded<DomainEvent>(new UnboundedChannelOptions
    {
        SingleWriter = false,
        SingleReader = true,
        AllowSynchronousContinuations = false
    });

    public void Publish(Command command)
    {
        if (!_commands.Writer.TryWrite(command))
            throw new InvalidOperationException();
    }

    public void Publish(DomainEvent domainEvent)
    {
        if (!_events.Writer.TryWrite(domainEvent))
            throw new InvalidOperationException();
    }

    public ValueTask<Command> ReadCommand(CancellationToken cancellationToken) =>
        _commands.Reader.ReadAsync(cancellationToken);

    public ValueTask<DomainEvent> ReadEvent(CancellationToken cancellationToken) =>
        _events.Reader.ReadAsync(cancellationToken);
}
```

## File: `Sources/Sales/Sales.Adapters/Sales.Adapters.csproj`
```
﻿<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <AssemblyName>MyCompany.ECommerce.Sales.Adapters</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.Sales</RootNamespace>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
    </PropertyGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="Marten" Version="7.13.1" />
      <PackageReference Include="Microsoft.EntityFrameworkCore" Version="8.0.5" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
      <PackageReference Include="Npgsql" Version="8.0.3" />
      <PackageReference Include="Npgsql.EntityFrameworkCore.PostgreSQL" Version="8.0.4" />
      <PackageReference Include="RepoDb" Version="1.13.1" />
      <PackageReference Include="RepoDb.PostgreSql" Version="1.13.1" />
    </ItemGroup>

    <ItemGroup>
      <ProjectReference Include="..\..\Payments\Payments.ProcessModel\Payments.ProcessModel.csproj" />
      <ProjectReference Include="..\..\RiskManagement\RiskManagement.ProcessModel\RiskManagement.ProcessModel.csproj" />
      <ProjectReference Include="..\..\TechnicalStuff\TechnicalStuff.Crud.Ef\TechnicalStuff.Crud.Ef.csproj" />
      <ProjectReference Include="..\..\TechnicalStuff\TechnicalStuff.Ef\TechnicalStuff.Ef.csproj" />
      <ProjectReference Include="..\..\TechnicalStuff\TechnicalStuff.Outbox.Kafka\TechnicalStuff.Outbox.Kafka.csproj" />
      <ProjectReference Include="..\..\TechnicalStuff\TechnicalStuff.Outbox.Postgres\TechnicalStuff.Outbox.Postgres.csproj" />
      <ProjectReference Include="..\..\TechnicalStuff\TechnicalStuff.Persistence.RepoDb\TechnicalStuff.Persistence.RepoDb.csproj" />
      <ProjectReference Include="..\..\TechnicalStuff\TechnicalStuff.Persistence\TechnicalStuff.Persistence.csproj" />
      <ProjectReference Include="..\..\TechnicalStuff\TechnicalStuff.Postgres\TechnicalStuff.Postgres.csproj" />
      <ProjectReference Include="..\..\TechnicalStuff\TechnicalStuff.ProcessModel\TechnicalStuff.ProcessModel.csproj" />
      <ProjectReference Include="..\Sales.DeepModel\Sales.DeepModel.csproj" />
      <ProjectReference Include="..\Sales.ProcessModel\Sales.ProcessModel.csproj" />
    </ItemGroup>

</Project>
```

## File: `Sources/Sales/Sales.Adapters/SalesAdaptersLayerInfo.cs`
```csharp
using System.Reflection;
using NoesisVision.Annotations.Technology.CleanArchitecture;

[assembly: AdaptersLayer]

namespace MyCompany.ECommerce.Sales;

public static class SalesAdaptersLayerInfo
{
    public static Assembly Assembly => typeof(SalesAdaptersLayerInfo).Assembly;
}
```

## File: `Sources/Sales/Sales.Adapters/SalesCrudEfDao.cs`
```csharp
using System.Diagnostics.CodeAnalysis;
using MyCompany.ECommerce.Sales.Database.Sql.EF;
using MyCompany.ECommerce.TechnicalStuff.Crud.Ef;

namespace MyCompany.ECommerce.Sales;

[method: SuppressMessage("ReSharper", "SuggestBaseTypeForParameter",
    Justification = "Required by DI container")]
public class SalesCrudEfDao(SalesDbContext context) : EfCrudDao(context), SalesCrudOperations;
```

## File: `Sources/Sales/Sales.Adapters/Clients/ClientSqlRepository.cs`
```csharp
using JetBrains.Annotations;

namespace MyCompany.ECommerce.Sales.Clients;

[UsedImplicitly]
public class ClientSqlRepository : ClientRepository
{
    public Task<ClientStatus> GetStatusFor(ClientId clientId) => throw new System.NotImplementedException();
}
```

## File: `Sources/Sales/Sales.Adapters/Database/Sql/Documents/DbOrder.cs`
```csharp
using JetBrains.Annotations;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Orders;

namespace MyCompany.ECommerce.Sales.Database.Sql.Documents;

[UsedImplicitly(ImplicitUseTargetFlags.WithMembers)]
public class DbOrder : Order.Data
{
    // Marten doesn't support value objects as identifiers.
    OrderId Order.Data.Id => new(Id);
    public Guid Id { get; set; }
    public Money MaxTotalCost { get; set; }
    public bool IsPlaced { get; set; }
    public List<Order.Item> Items { get; set; }

    IReadOnlyCollection<Order.Item> Order.Data.Items => Items;
    public void Add(Order.Item item) => Items.Add(item);
    public void Remove(Order.Item item) => Items.Remove(item);
}
```

## File: `Sources/Sales/Sales.Adapters/Database/Sql/EF/DbOrder.cs`
```csharp
using JetBrains.Annotations;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Orders;

namespace MyCompany.ECommerce.Sales.Database.Sql.EF;

[UsedImplicitly(ImplicitUseTargetFlags.WithMembers)]
public class DbOrder : Order.Data
{
    public OrderId Id { get; set; }
    public Money MaxTotalCost { get; set; }
    public bool IsPlaced { get; set; }
    public int Version { get; set; }
    public List<Order.Item> Items { get; set; }

    IReadOnlyCollection<Order.Item> Order.Data.Items => Items;
    public void Add(Order.Item item) => Items.Add(item);
    public void Remove(Order.Item item) => Items.Remove(item);
}
```

## File: `Sources/Sales/Sales.Adapters/Database/Sql/EF/SalesDbContext.cs`
```csharp
using JetBrains.Annotations;
using Microsoft.EntityFrameworkCore;
using MyCompany.ECommerce.Sales.Orders;
using MyCompany.ECommerce.TechnicalStuff.Ef.ValueConverters;
using MyCompany.ECommerce.TechnicalStuff.ValueObjects;
using NoesisVision.Annotations.Technology;

namespace MyCompany.ECommerce.Sales.Database.Sql.EF;

[UsedImplicitly(ImplicitUseTargetFlags.Members)]
[Database("Main", ServerName = "Postgres")]
public class SalesDbContext(DbContextOptions<SalesDbContext> options) : DbContext(options)
{
    public DbSet<DbOrder> Orders { get; set; }
    public DbSet<OrderHeader> OrderHeaders { get; set; }
    public DbSet<OrderNote> OrderNotes { get; set; }

    protected override void ConfigureConventions(ModelConfigurationBuilder configuration)
    {
        foreach (var (type, valueType) in SalesDeepModelLayerInfo.Assembly.GetValueObjectsMeta())
            configuration.Properties(type)
                .HaveConversion(typeof(ValueObjectConverter<,>).MakeGenericType(type, valueType));
    }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<DbOrder>(order =>
        {
            order.HasKey(o => o.Id);
            order.Property(o => o.Version).IsConcurrencyToken();
            order.OwnsMany(o => o.Items, item =>
            {
                item.ToTable("OrderItems");
                item.WithOwner().HasForeignKey("OrderId");
                item.OwnsOne(i => i.ProductAmount, productAmount =>
                {
                    productAmount.WithOwner();
                    productAmount.OwnsOne(pa => pa.Amount).WithOwner();
                        
                });
                item.OwnsOne(i => i.PriceAgreement, priceAgreement =>
                {
                    priceAgreement.WithOwner();
                    priceAgreement.Property(pa => pa.Type);
                    priceAgreement.Property(pa => pa.ExpiresOn);
                    priceAgreement.OwnsOne(pa => pa.Price).WithOwner();
                });
                item.Ignore(i => i.Id);
            });
        });
        modelBuilder.Entity<OrderHeader>()
            .OwnsOne(orderHeader => orderHeader.InvoicingDetails);
    }
}
```

## File: `Sources/Sales/Sales.Adapters/Database/Sql/EF/Migrations/20221229083720_Initial.Designer.cs`
```csharp
﻿// <auto-generated />
using System;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Migrations;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
using MyCompany.ECommerce.Sales.Database.Sql.EF;
using MyCompany.ECommerce.Sales.Database.Sql.EF;
using Npgsql.EntityFrameworkCore.PostgreSQL.Metadata;

#nullable disable

namespace MyCompany.ECommerce.Sales.Database.Sql.EF.Migrations
{
    [DbContext(typeof(SalesDbContext))]
    [Migration("20221229083720_Initial")]
    partial class Initial
    {
        protected override void BuildTargetModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder
                .HasAnnotation("ProductVersion", "6.0.8")
                .HasAnnotation("Relational:MaxIdentifierLength", 63);

            NpgsqlModelBuilderExtensions.UseIdentityByDefaultColumns(modelBuilder);

            modelBuilder.Entity("MyCompany.ECommerce.Sales.Database.Sql.EF.DbOrder", b =>
                {
                    b.Property<Guid>("Id")
                        .HasColumnType("uuid");

                    b.Property<bool>("IsPlaced")
                        .HasColumnType("boolean");

                    b.Property<int>("Version")
                        .IsConcurrencyToken()
                        .HasColumnType("integer");

                    b.HasKey("Id");

                    b.ToTable("Orders");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Sales.Orders.OrderHeader", b =>
                {
                    b.Property<Guid>("Id")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("uuid");

                    b.Property<Guid>("ClientId")
                        .HasColumnType("uuid");

                    b.Property<bool>("IsDeleted")
                        .HasColumnType("boolean");

                    b.HasKey("Id");

                    b.ToTable("OrderHeaders");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Sales.Orders.OrderNote", b =>
                {
                    b.Property<Guid>("Id")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("uuid");

                    b.Property<DateTime>("AddedOn")
                        .HasColumnType("timestamp with time zone");

                    b.Property<Guid>("AuthorId")
                        .HasColumnType("uuid");

                    b.Property<bool>("IsDeleted")
                        .HasColumnType("boolean");

                    b.Property<Guid?>("OrderHeaderId")
                        .HasColumnType("uuid");

                    b.Property<Guid>("OrderId")
                        .HasColumnType("uuid");

                    b.Property<string>("Text")
                        .IsRequired()
                        .HasColumnType("text");

                    b.HasKey("Id");

                    b.HasIndex("OrderHeaderId");

                    b.ToTable("OrderNotes");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Sales.Database.Sql.EF.DbOrder", b =>
                {
                    b.OwnsMany("MyCompany.ECommerce.Sales.Orders.Order+Item", "Items", b1 =>
                        {
                            b1.Property<Guid>("OrderId")
                                .HasColumnType("uuid");

                            b1.Property<int>("Id1")
                                .ValueGeneratedOnAdd()
                                .HasColumnType("integer");

                            NpgsqlPropertyBuilderExtensions.UseIdentityByDefaultColumn(b1.Property<int>("Id1"));

                            b1.HasKey("OrderId", "Id1");

                            b1.ToTable("OrderItems", (string)null);

                            b1.WithOwner()
                                .HasForeignKey("OrderId");

                            b1.OwnsOne("MyCompany.ECommerce.Sales.Orders.Order+PriceAgreement", "PriceAgreement", b2 =>
                                {
                                    b2.Property<Guid>("ItemOrderId")
                                        .HasColumnType("uuid");

                                    b2.Property<int>("ItemId1")
                                        .HasColumnType("integer");

                                    b2.Property<DateTime?>("ExpiresOn")
                                        .HasColumnType("timestamp with time zone");

                                    b2.Property<byte>("Type")
                                        .HasColumnType("smallint");

                                    b2.HasKey("ItemOrderId", "ItemId1");

                                    b2.ToTable("OrderItems");

                                    b2.WithOwner()
                                        .HasForeignKey("ItemOrderId", "ItemId1");

                                    b2.OwnsOne("MyCompany.ECommerce.Sales.Commons.Money", "Price", b3 =>
                                        {
                                            b3.Property<Guid>("PriceAgreementItemOrderId")
                                                .HasColumnType("uuid");

                                            b3.Property<int>("PriceAgreementItemId1")
                                                .HasColumnType("integer");

                                            b3.Property<int>("Currency")
                                                .HasColumnType("integer");

                                            b3.Property<decimal>("Value")
                                                .HasColumnType("numeric");

                                            b3.HasKey("PriceAgreementItemOrderId", "PriceAgreementItemId1");

                                            b3.ToTable("OrderItems");

                                            b3.WithOwner()
                                                .HasForeignKey("PriceAgreementItemOrderId", "PriceAgreementItemId1");
                                        });

                                    b2.Navigation("Price");
                                });

                            b1.OwnsOne("MyCompany.ECommerce.Sales.Products.ProductAmount", "ProductAmount", b2 =>
                                {
                                    b2.Property<Guid>("ItemOrderId")
                                        .HasColumnType("uuid");

                                    b2.Property<int>("ItemId1")
                                        .HasColumnType("integer");

                                    b2.Property<Guid>("ProductId")
                                        .HasColumnType("uuid");

                                    b2.HasKey("ItemOrderId", "ItemId1");

                                    b2.ToTable("OrderItems");

                                    b2.WithOwner()
                                        .HasForeignKey("ItemOrderId", "ItemId1");

                                    b2.OwnsOne("MyCompany.ECommerce.Sales.Products.Amount", "Amount", b3 =>
                                        {
                                            b3.Property<Guid>("ProductAmountItemOrderId")
                                                .HasColumnType("uuid");

                                            b3.Property<int>("ProductAmountItemId1")
                                                .HasColumnType("integer");

                                            b3.Property<int>("Unit")
                                                .HasColumnType("integer");

                                            b3.Property<int>("Value")
                                                .HasColumnType("integer");

                                            b3.HasKey("ProductAmountItemOrderId", "ProductAmountItemId1");

                                            b3.ToTable("OrderItems");

                                            b3.WithOwner()
                                                .HasForeignKey("ProductAmountItemOrderId", "ProductAmountItemId1");
                                        });

                                    b2.Navigation("Amount")
                                        .IsRequired();
                                });

                            b1.Navigation("PriceAgreement")
                                .IsRequired();

                            b1.Navigation("ProductAmount")
                                .IsRequired();
                        });

                    b.Navigation("Items");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Sales.Orders.OrderHeader", b =>
                {
                    b.OwnsOne("MyCompany.ECommerce.Sales.Orders.InvoicingDetails", "InvoicingDetails", b1 =>
                        {
                            b1.Property<Guid>("OrderHeaderId")
                                .HasColumnType("uuid");

                            b1.Property<string>("Name")
                                .IsRequired()
                                .HasColumnType("text");

                            b1.Property<string>("TaxId")
                                .IsRequired()
                                .HasColumnType("text");

                            b1.HasKey("OrderHeaderId");

                            b1.ToTable("OrderHeaders");

                            b1.WithOwner()
                                .HasForeignKey("OrderHeaderId");
                        });

                    b.Navigation("InvoicingDetails")
                        .IsRequired();
                });

            modelBuilder.Entity("MyCompany.ECommerce.Sales.Orders.OrderNote", b =>
                {
                    b.HasOne("MyCompany.ECommerce.Sales.Orders.OrderHeader", null)
                        .WithMany("Notes")
                        .HasForeignKey("OrderHeaderId");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Sales.Orders.OrderHeader", b =>
                {
                    b.Navigation("Notes");
                });
#pragma warning restore 612, 618
        }
    }
}
```

## File: `Sources/Sales/Sales.Adapters/Database/Sql/EF/Migrations/20221229083720_Initial.cs`
```csharp
﻿using System;
using Microsoft.EntityFrameworkCore.Migrations;
using Npgsql.EntityFrameworkCore.PostgreSQL.Metadata;

#nullable disable

namespace MyCompany.ECommerce.Sales.Database.Sql.EF.Migrations
{
    public partial class Initial : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "OrderHeaders",
                columns: table => new
                {
                    Id = table.Column<Guid>(type: "uuid", nullable: false),
                    ClientId = table.Column<Guid>(type: "uuid", nullable: false),
                    InvoicingDetails_TaxId = table.Column<string>(type: "text", nullable: false),
                    InvoicingDetails_Name = table.Column<string>(type: "text", nullable: false),
                    IsDeleted = table.Column<bool>(type: "boolean", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_OrderHeaders", x => x.Id);
                });

            migrationBuilder.CreateTable(
                name: "Orders",
                columns: table => new
                {
                    Id = table.Column<Guid>(type: "uuid", nullable: false),
                    IsPlaced = table.Column<bool>(type: "boolean", nullable: false),
                    Version = table.Column<int>(type: "integer", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Orders", x => x.Id);
                });

            migrationBuilder.CreateTable(
                name: "OrderNotes",
                columns: table => new
                {
                    Id = table.Column<Guid>(type: "uuid", nullable: false),
                    OrderId = table.Column<Guid>(type: "uuid", nullable: false),
                    AuthorId = table.Column<Guid>(type: "uuid", nullable: false),
                    AddedOn = table.Column<DateTime>(type: "timestamp with time zone", nullable: false),
                    Text = table.Column<string>(type: "text", nullable: false),
                    OrderHeaderId = table.Column<Guid>(type: "uuid", nullable: true),
                    IsDeleted = table.Column<bool>(type: "boolean", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_OrderNotes", x => x.Id);
                    table.ForeignKey(
                        name: "FK_OrderNotes_OrderHeaders_OrderHeaderId",
                        column: x => x.OrderHeaderId,
                        principalTable: "OrderHeaders",
                        principalColumn: "Id");
                });

            migrationBuilder.CreateTable(
                name: "OrderItems",
                columns: table => new
                {
                    OrderId = table.Column<Guid>(type: "uuid", nullable: false),
                    Id1 = table.Column<int>(type: "integer", nullable: false)
                        .Annotation("Npgsql:ValueGenerationStrategy", NpgsqlValueGenerationStrategy.IdentityByDefaultColumn),
                    ProductAmount_ProductId = table.Column<Guid>(type: "uuid", nullable: false),
                    ProductAmount_Amount_Value = table.Column<int>(type: "integer", nullable: false),
                    ProductAmount_Amount_Unit = table.Column<int>(type: "integer", nullable: false),
                    PriceAgreement_Type = table.Column<byte>(type: "smallint", nullable: false),
                    PriceAgreement_Price_Value = table.Column<decimal>(type: "numeric", nullable: true),
                    PriceAgreement_Price_Currency = table.Column<int>(type: "integer", nullable: true),
                    PriceAgreement_ExpiresOn = table.Column<DateTime>(type: "timestamp with time zone", nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_OrderItems", x => new { x.OrderId, x.Id1 });
                    table.ForeignKey(
                        name: "FK_OrderItems_Orders_OrderId",
                        column: x => x.OrderId,
                        principalTable: "Orders",
                        principalColumn: "Id",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateIndex(
                name: "IX_OrderNotes_OrderHeaderId",
                table: "OrderNotes",
                column: "OrderHeaderId");
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "OrderItems");

            migrationBuilder.DropTable(
                name: "OrderNotes");

            migrationBuilder.DropTable(
                name: "Orders");

            migrationBuilder.DropTable(
                name: "OrderHeaders");
        }
    }
}
```

## File: `Sources/Sales/Sales.Adapters/Database/Sql/EF/Migrations/SalesDbContextModelSnapshot.cs`
```csharp
﻿// <auto-generated />
using System;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
using MyCompany.ECommerce.Sales.Database.Sql.EF;
using MyCompany.ECommerce.Sales.Database.Sql.EF;
using Npgsql.EntityFrameworkCore.PostgreSQL.Metadata;

#nullable disable

namespace MyCompany.ECommerce.Sales.Database.Sql.EF.Migrations
{
    [DbContext(typeof(SalesDbContext))]
    partial class SalesDbContextModelSnapshot : ModelSnapshot
    {
        protected override void BuildModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder
                .HasAnnotation("ProductVersion", "6.0.8")
                .HasAnnotation("Relational:MaxIdentifierLength", 63);

            NpgsqlModelBuilderExtensions.UseIdentityByDefaultColumns(modelBuilder);

            modelBuilder.Entity("MyCompany.ECommerce.Sales.Database.Sql.EF.DbOrder", b =>
                {
                    b.Property<Guid>("Id")
                        .HasColumnType("uuid");

                    b.Property<bool>("IsPlaced")
                        .HasColumnType("boolean");

                    b.Property<int>("Version")
                        .IsConcurrencyToken()
                        .HasColumnType("integer");

                    b.HasKey("Id");

                    b.ToTable("Orders");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Sales.Orders.OrderHeader", b =>
                {
                    b.Property<Guid>("Id")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("uuid");

                    b.Property<Guid>("ClientId")
                        .HasColumnType("uuid");

                    b.Property<bool>("IsDeleted")
                        .HasColumnType("boolean");

                    b.HasKey("Id");

                    b.ToTable("OrderHeaders");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Sales.Orders.OrderNote", b =>
                {
                    b.Property<Guid>("Id")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("uuid");

                    b.Property<DateTime>("AddedOn")
                        .HasColumnType("timestamp with time zone");

                    b.Property<Guid>("AuthorId")
                        .HasColumnType("uuid");

                    b.Property<bool>("IsDeleted")
                        .HasColumnType("boolean");

                    b.Property<Guid?>("OrderHeaderId")
                        .HasColumnType("uuid");

                    b.Property<Guid>("OrderId")
                        .HasColumnType("uuid");

                    b.Property<string>("Text")
                        .IsRequired()
                        .HasColumnType("text");

                    b.HasKey("Id");

                    b.HasIndex("OrderHeaderId");

                    b.ToTable("OrderNotes");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Sales.Database.Sql.EF.DbOrder", b =>
                {
                    b.OwnsMany("MyCompany.ECommerce.Sales.Orders.Order+Item", "Items", b1 =>
                        {
                            b1.Property<Guid>("OrderId")
                                .HasColumnType("uuid");

                            b1.Property<int>("Id1")
                                .ValueGeneratedOnAdd()
                                .HasColumnType("integer");

                            NpgsqlPropertyBuilderExtensions.UseIdentityByDefaultColumn(b1.Property<int>("Id1"));

                            b1.HasKey("OrderId", "Id1");

                            b1.ToTable("OrderItems", (string)null);

                            b1.WithOwner()
                                .HasForeignKey("OrderId");

                            b1.OwnsOne("MyCompany.ECommerce.Sales.Orders.Order+PriceAgreement", "PriceAgreement", b2 =>
                                {
                                    b2.Property<Guid>("ItemOrderId")
                                        .HasColumnType("uuid");

                                    b2.Property<int>("ItemId1")
                                        .HasColumnType("integer");

                                    b2.Property<DateTime?>("ExpiresOn")
                                        .HasColumnType("timestamp with time zone");

                                    b2.Property<byte>("Type")
                                        .HasColumnType("smallint");

                                    b2.HasKey("ItemOrderId", "ItemId1");

                                    b2.ToTable("OrderItems");

                                    b2.WithOwner()
                                        .HasForeignKey("ItemOrderId", "ItemId1");

                                    b2.OwnsOne("MyCompany.ECommerce.Sales.Commons.Money", "Price", b3 =>
                                        {
                                            b3.Property<Guid>("PriceAgreementItemOrderId")
                                                .HasColumnType("uuid");

                                            b3.Property<int>("PriceAgreementItemId1")
                                                .HasColumnType("integer");

                                            b3.Property<int>("Currency")
                                                .HasColumnType("integer");

                                            b3.Property<decimal>("Value")
                                                .HasColumnType("numeric");

                                            b3.HasKey("PriceAgreementItemOrderId", "PriceAgreementItemId1");

                                            b3.ToTable("OrderItems");

                                            b3.WithOwner()
                                                .HasForeignKey("PriceAgreementItemOrderId", "PriceAgreementItemId1");
                                        });

                                    b2.Navigation("Price");
                                });

                            b1.OwnsOne("MyCompany.ECommerce.Sales.Products.ProductAmount", "ProductAmount", b2 =>
                                {
                                    b2.Property<Guid>("ItemOrderId")
                                        .HasColumnType("uuid");

                                    b2.Property<int>("ItemId1")
                                        .HasColumnType("integer");

                                    b2.Property<Guid>("ProductId")
                                        .HasColumnType("uuid");

                                    b2.HasKey("ItemOrderId", "ItemId1");

                                    b2.ToTable("OrderItems");

                                    b2.WithOwner()
                                        .HasForeignKey("ItemOrderId", "ItemId1");

                                    b2.OwnsOne("MyCompany.ECommerce.Sales.Products.Amount", "Amount", b3 =>
                                        {
                                            b3.Property<Guid>("ProductAmountItemOrderId")
                                                .HasColumnType("uuid");

                                            b3.Property<int>("ProductAmountItemId1")
                                                .HasColumnType("integer");

                                            b3.Property<int>("Unit")
                                                .HasColumnType("integer");

                                            b3.Property<int>("Value")
                                                .HasColumnType("integer");

                                            b3.HasKey("ProductAmountItemOrderId", "ProductAmountItemId1");

                                            b3.ToTable("OrderItems");

                                            b3.WithOwner()
                                                .HasForeignKey("ProductAmountItemOrderId", "ProductAmountItemId1");
                                        });

                                    b2.Navigation("Amount")
                                        .IsRequired();
                                });

                            b1.Navigation("PriceAgreement")
                                .IsRequired();

                            b1.Navigation("ProductAmount")
                                .IsRequired();
                        });

                    b.Navigation("Items");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Sales.Orders.OrderHeader", b =>
                {
                    b.OwnsOne("MyCompany.ECommerce.Sales.Orders.InvoicingDetails", "InvoicingDetails", b1 =>
                        {
                            b1.Property<Guid>("OrderHeaderId")
                                .HasColumnType("uuid");

                            b1.Property<string>("Name")
                                .IsRequired()
                                .HasColumnType("text");

                            b1.Property<string>("TaxId")
                                .IsRequired()
                                .HasColumnType("text");

                            b1.HasKey("OrderHeaderId");

                            b1.ToTable("OrderHeaders");

                            b1.WithOwner()
                                .HasForeignKey("OrderHeaderId");
                        });

                    b.Navigation("InvoicingDetails")
                        .IsRequired();
                });

            modelBuilder.Entity("MyCompany.ECommerce.Sales.Orders.OrderNote", b =>
                {
                    b.HasOne("MyCompany.ECommerce.Sales.Orders.OrderHeader", null)
                        .WithMany("Notes")
                        .HasForeignKey("OrderHeaderId");
                });

            modelBuilder.Entity("MyCompany.ECommerce.Sales.Orders.OrderHeader", b =>
                {
                    b.Navigation("Notes");
                });
#pragma warning restore 612, 618
        }
    }
}
```

## File: `Sources/Sales/Sales.Adapters/Database/Sql/Raw/DbOrder.cs`
```csharp
using System.ComponentModel.DataAnnotations.Schema;
using MyCompany.ECommerce.TechnicalStuff.Persistence.RepoDb;

namespace MyCompany.ECommerce.Sales.Database.Sql.Raw;

[Table("Sales_RawSql.Orders")]
public record DbOrder(Guid Id, bool IsPlaced, int Version) : DbRootEntity<Guid>;
```

## File: `Sources/Sales/Sales.Adapters/Database/Sql/Raw/DbOrderItem.cs`
```csharp
using System.ComponentModel.DataAnnotations.Schema;

namespace MyCompany.ECommerce.Sales.Database.Sql.Raw;

[Table("Sales_RawSql.OrderItems")]
public record DbOrderItem(Guid OrderId, Guid ProductId, string AmountUnit, int AmountValue, string PriceAgreementType, DateTime? PriceAgreementExpiresOn, decimal? Price, string Currency);
```

## File: `Sources/Sales/Sales.Adapters/Integrations/RiskManagementInMemoryCalls.cs`
```csharp
using MyCompany.ECommerce.RiskManagement;
using MyCompany.ECommerce.Sales.Clients;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Sales.Integrations;

public class RiskManagementInMemoryCalls(CommandHandler<GetMaxAmount> handler) : RiskManagement.RiskManagementIntegration
{
    public Task<Money> GetMaxOrderTotalCostFor(ClientId clientId)
    {
        throw new NotImplementedException();
    }
}
```

## File: `Sources/Sales/Sales.Adapters/Integrations/Forex/ForexViaHttp.cs`
```csharp
using JetBrains.Annotations;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.ExchangeRates;

namespace MyCompany.ECommerce.Sales.Integrations.Forex;

[UsedImplicitly]
public class ForexViaHttp : ExchangeRateProvider
{
    // The only purpose of this fake implementation is to show integration point with external software system.
    public Task<ExchangeRate> GetFor(Currency currency) => Task.FromResult(ExchangeRate.Of(currency, 1));
}
```

## File: `Sources/Sales/Sales.Adapters/Integrations/Payments/PaymentsInMemoryCalls.cs`
```csharp
using JetBrains.Annotations;
using MyCompany.ECommerce.Payments.Requesting;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Orders;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Sales.Integrations.Payments;

[UsedImplicitly]
public class PaymentsInMemoryCalls : PaymentsModule
{
    private readonly CommandHandler<RequestPayment> _handler;
        
    public void AddPaymentRequestFor(OrderId orderId, Money amount)
    {
        // handler.Handle(new RequestPayment)
        throw new System.NotImplementedException();
    }
}

public class PaymentsIHttpCalls : PaymentsModule
{
    // HttpClient
    public void AddPaymentRequestFor(OrderId orderId, Money amount)
    {
        //HttpClient.Post(...)
        throw new System.NotImplementedException();
    }
}
```

## File: `Sources/Sales/Sales.Adapters/Orders/FakeOrderEventOutbox.cs`
```csharp
namespace MyCompany.ECommerce.Sales.Orders;

public class FakeOrderEventOutbox(FakeMessageBroker broker) : OrderEventsOutbox
{
    public void Add(OrderEvent orderEvent) => broker.Publish(orderEvent);
}
```

## File: `Sources/Sales/Sales.Adapters/Orders/InPLaceOrderEventsOutbox.cs`
```csharp
using MyCompany.ECommerce.TechnicalStuff.Outbox;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Sales.Orders;

public class InPlaceOrderEventsOutbox(
    TransactionalOutboxes outboxes,
    TransactionalOutboxRepository repository,
    MessageTypes messageTypes)
    : InPlaceTransactionalOutbox<OrderEvent>(outboxes, repository, messageTypes), OrderEventsOutbox
{
    protected override string GetPartitionKeyFor(OrderEvent message) => message.OrderId.ToString("N");
}
```

## File: `Sources/Sales/Sales.Adapters/Orders/KafkaOrderEventsOutbox.cs`
```csharp
﻿using System.Diagnostics.CodeAnalysis;
using MyCompany.ECommerce.TechnicalStuff.Outbox;
using MyCompany.ECommerce.TechnicalStuff.Outbox.Kafka;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Sales.Orders;

[method: SuppressMessage("ReSharper", "SuggestBaseTypeForParameter", Justification = "Required by DI container")]
public class KafkaOrderEventsOutbox(TransactionalOutboxes outboxes, TransactionalOutboxRepository repository,
    MessageTypes messageTypes) : TransactionalKafkaOutbox<OrderEvent>(outboxes, repository, messageTypes), OrderEventsOutbox
{
    protected override string Topic => "OrderEvents";

    protected override string GetPartitionKeyFor(OrderEvent message) => message.OrderId.ToString("N");
}
```

## File: `Sources/Sales/Sales.Adapters/Orders/OrderDetailsSqlRepository.cs`
```csharp
namespace MyCompany.ECommerce.Sales.Orders;

// TODO: implementation for all persistence options used for OrderRepository
public class OrderDetailsSqlRepository : OnlineOrdering.OrderDetailsFinder,
    WholesaleOrdering.OrderDetailsFinder
{
    Task<OnlineOrdering.OrderDetails> OnlineOrdering.OrderDetailsFinder.GetBy(Guid id) =>
        throw new NotImplementedException();
        
    Task<AllOrderDetails> WholesaleOrdering.OrderDetailsFinder.GetBy(Guid id) =>
        throw new NotImplementedException();
}
```

## File: `Sources/Sales/Sales.Adapters/Orders/OrderSqlRepository.Document.cs`
```csharp
using Marten;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Database.Sql.Documents;
using MyCompany.ECommerce.Sales.Integrations.RiskManagement;
using MyCompany.ECommerce.TechnicalStuff;

namespace MyCompany.ECommerce.Sales.Orders;

public static partial class OrderSqlRepository
{
    public class Document(RiskManagementIntegration riskManagement, IDocumentSession session)
        : Order.Factory(riskManagement), Order.Repository
    {
        private readonly Dictionary<OrderId, (DbOrder OrderData, Guid Version)> _orders = new();

        protected override Order.Data CreateData(OrderId id, Money maxTotalCost)
        {
            var dbOrder = new DbOrder { Id = id.Value, Items = new List<Order.Item>() };
            _orders.Add(id, (dbOrder, Guid.Empty));
            return dbOrder;
        }

        public async Task<Order> GetBy(OrderId id)
        {
            if (_orders.ContainsKey(id))
                throw new DesignError(SameAggregateRestoredMoreThanOnce);
            var orderDoc = await session.LoadAsync<DbOrder>(id.Value);
            if (orderDoc is null)
                throw new DomainError();
            var order = Order.RestoreFrom(orderDoc);
            var metadata = await session.MetadataForAsync(orderDoc);
            _orders.Add(id, (orderDoc, metadata.CurrentVersion));
            return order;
        }

        public Task Save(Order order)
        {
            // TODO: document versioning
            if (!_orders.TryGetValue(order.Id, out var tuple))
                throw new DesignError(SaveOfUnknownAggregate);
            session.UpdateExpectedVersion(tuple.OrderData, tuple.Version);
            return session.SaveChangesAsync();
        }
    }
}
```

## File: `Sources/Sales/Sales.Adapters/Orders/OrderSqlRepository.EF.cs`
```csharp
using JetBrains.Annotations;
using Microsoft.EntityFrameworkCore;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Database.Sql.EF;
using MyCompany.ECommerce.Sales.Integrations.RiskManagement;
using MyCompany.ECommerce.TechnicalStuff;

namespace MyCompany.ECommerce.Sales.Orders;

public static partial class OrderSqlRepository
{
    [UsedImplicitly]
    public class EF(RiskManagementIntegration riskManagement, SalesDbContext dbContext)
        : Order.Factory(riskManagement), Order.Repository
    {
        private readonly Dictionary<OrderId, DbOrder> _orders = new();

        protected override Order.Data CreateData(OrderId id, Money maxTotalCost)
        {
            var dbOrder = new DbOrder
            {
                Id = id,
                MaxTotalCost = maxTotalCost,
                Items = new List<Order.Item>()
            };
            _orders.Add(id, dbOrder);
            dbContext.Orders.Add(dbOrder);
            return dbOrder;
        }

        public async Task<Order> GetBy(OrderId id)
        {
            if (_orders.ContainsKey(id))
                throw new DesignError(SameAggregateRestoredMoreThanOnce);
            var dbOrder = await dbContext.Orders
                .Include(o => o.Items)
                .SingleOrDefaultAsync(o => o.Id.Equals(id));
            if (dbOrder is null) 
                throw new DomainError();
            var order = Order.RestoreFrom(dbOrder);
            _orders.Add(id, dbOrder);
            return order;
        }

        public Task Save(Order order)
        {
            if (!_orders.TryGetValue(order.Id, out var dbOrder))
                throw new DesignError(SaveOfUnknownAggregate);
            dbOrder.Version++;
            return dbContext.SaveChangesAsync();
            // TODO: error when not all tracked orders are explicitly saved
        }
    }
}
```

## File: `Sources/Sales/Sales.Adapters/Orders/OrderSqlRepository.EventsSourcing.Data.cs`
```csharp
using MyCompany.ECommerce.Sales.Commons;

namespace MyCompany.ECommerce.Sales.Orders;

public static partial class OrderSqlRepository
{
    public partial class EventsSourcing
    {
        private class Data : Order.Data
        {
            public OrderId Id { get; init; }
            public Money MaxTotalCost { get; init; }
            public bool IsPlaced { get; set; }
            private List<Order.Item> Items { get; } = new();

            IReadOnlyCollection<Order.Item> Order.Data.Items => Items;
            public void Add(Order.Item item) => Items.Add(item);
            public void Remove(Order.Item item) => Items.Remove(item);
        }
    }
}
```

## File: `Sources/Sales/Sales.Adapters/Orders/OrderSqlRepository.EventsSourcing.cs`
```csharp
using JetBrains.Annotations;
using Marten;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Integrations.RiskManagement;
using MyCompany.ECommerce.TechnicalStuff;

namespace MyCompany.ECommerce.Sales.Orders;

public static partial class OrderSqlRepository
{
    [UsedImplicitly]
    public partial class EventsSourcing(RiskManagementIntegration riskManagement, IDocumentSession session)
        : Order.Factory(riskManagement), Order.Repository
    {
        public static readonly IEnumerable<(Type Type, string Name)> Events = new[]
        {
            (typeof(Order.CreatedFromOffer), "Order.CreatedFromOffer"),
            (typeof(Order.ProductAmountAdded), "Order.ProductAmountAdded"),
            (typeof(Order.PricesConfirmed), "Order.PricesConfirmed"),
            (typeof(Order.Placed), "Order.Placed")
        };

        private readonly Dictionary<OrderId, long> _orderVersions = new();

        protected override Order.Data CreateData(OrderId id, Money maxTotalCost) => new Data { Id = id };

        public async Task<Order> GetBy(OrderId id)
        {
            if (_orderVersions.ContainsKey(id))
                throw new DesignError(SameAggregateRestoredMoreThanOnce);
            var events = await session.Events.FetchStreamAsync(id.Value);
            var version = events.Count > 0 ? events[^1].Version : 0;
            _orderVersions.Add(id, version);
            var orderEvents = events
                .Select(e => e.Data)
                .Cast<Order.Event>();
            var order = Order.RestoreFrom(new Data { Id = id });
            foreach (var orderEvent in orderEvents)
                orderEvent.Apply(order);
            return order;
        }

        public async Task Save(Order order)
        {
            // TODO: event versioning
            session.Events.Append(
                order.Id.Value,
                CalculateExpectedVersionFor(order),
                order.NewEvents);
            await session.SaveChangesAsync();
        }

        private long CalculateExpectedVersionFor(Order order) =>
            (_orderVersions.TryGetValue(order.Id, out var version) ? version : 0) + order.NewEvents.Count;
    }
}
```

## File: `Sources/Sales/Sales.Adapters/Orders/OrderSqlRepository.Raw.Data.cs`
```csharp
using System.Data;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Database.Sql.Raw;
using MyCompany.ECommerce.Sales.Products;
using MyCompany.ECommerce.TechnicalStuff;
using MyCompany.ECommerce.TechnicalStuff.Persistence;
using MyCompany.ECommerce.TechnicalStuff.Persistence.RepoDb;
using RepoDb;

namespace MyCompany.ECommerce.Sales.Orders;

public static partial class OrderSqlRepository
{
    public partial class Raw
    {
        public class Data : RootEntityData<DbOrder, Guid>, Order.Data
        {
            public OrderId Id { get; }
            public Money MaxTotalCost { get; }
            public bool IsPlaced { get; set; }

            private readonly TrackedSet<Order.Item, DbOrderItem> _items;
            public IReadOnlyCollection<Order.Item> Items => _items;

            public Data(DbOrder originalDbOrder, IEnumerable<DbOrderItem> originalDbOrderItems)
                : base(originalDbOrder)
            {
                Id = new OrderId(originalDbOrder.Id);
                IsPlaced = originalDbOrder.IsPlaced;
                _items = CreateItemsSet(originalDbOrder.Id, originalDbOrderItems);
            }

            public Data(OrderId id, Money maxTotalCost)
                : base(null)
            {
                Id = id;
                MaxTotalCost = maxTotalCost;
                IsPlaced = false;
                _items = CreateItemsSet(Id.Value, Enumerable.Empty<DbOrderItem>());
            }

            private static TrackedSet<Order.Item, DbOrderItem> CreateItemsSet(Guid id,
                IEnumerable<DbOrderItem> dbOrderItems) => new(dbOrderItems,
                item => new DbOrderItem(
                     id,
                     item.ProductAmount.ProductId.Value,
                     item.ProductAmount.Amount.Unit.ToString(),
                     item.ProductAmount.Amount.Value,
                     item.PriceAgreement.Type.ToString(),
                     item.PriceAgreement.ExpiresOn,
                     item.PriceAgreement.Price?.Value,
                     item.PriceAgreement.Price?.Currency.ToString()!
                ),
                dbItem => new Order.Item(
                    new ProductAmount(
                        ProductId.From(dbItem.ProductId),
                        Amount.Of(
                            dbItem.AmountValue,
                            dbItem.AmountUnit.ToDomainModel<AmountUnit>())),
                    new Order.PriceAgreement(
                        dbItem.PriceAgreementType.ToDomainModel<PriceAgreementType>(),
                        dbItem.Price.HasValue
                            ? Money.Of(dbItem.Price.Value, dbItem.Currency.ToDomainModel<Currency>())
                            : null,
                        dbItem.PriceAgreementExpiresOn)));

            public void Add(Order.Item item) => _items.Add(item);

            public void Remove(Order.Item item) => _items.Remove(item);

            protected override DbOrder ToDbEntity(int version) => new(Id.Value, IsPlaced, version);

            protected override async Task SaveNestedDbEntities(IDbTransaction transaction)
            {
                var (added, updated, deleted) = _items.GetDiff();
                await transaction.Connection.InsertAllAsync(added, transaction: transaction);
                await transaction.Connection.UpdateAllAsync(updated,
                    qualifiers: i => new { i.OrderId, i.ProductId, i.AmountUnit },
                    transaction: transaction);
                await transaction.Connection.DeleteAllAsync(deleted, transaction: transaction);
            }
        }
    }
}
```

## File: `Sources/Sales/Sales.Adapters/Orders/OrderSqlRepository.Raw.cs`
```csharp
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Database.Sql.Raw;
using MyCompany.ECommerce.Sales.Integrations.RiskManagement;
using MyCompany.ECommerce.TechnicalStuff;
using MyCompany.ECommerce.TechnicalStuff.Persistence;
using RepoDb;

namespace MyCompany.ECommerce.Sales.Orders;

public static partial class OrderSqlRepository
{
    public partial class Raw(RiskManagementIntegration riskManagement, MainDb db) : Order.Factory(riskManagement), Order.Repository
    {
        private readonly Dictionary<OrderId, Data> _orders = new();

        protected override Order.Data CreateData(OrderId id, Money maxTotalCost) => new Data(id, maxTotalCost);

        public async Task<Order> GetBy(OrderId id)
        {
            if (_orders.ContainsKey(id))
                throw new DesignError(SameAggregateRestoredMoreThanOnce);
            var connection = await db.CreateOneOffConnection();
            var (dbOrders, dbOrderItems) = await connection.QueryMultipleAsync<DbOrder, DbOrderItem>(               
                o => o.Id == id.Value,                
                i => i.OrderId == id.Value);
            var dbOrder = dbOrders.FirstOrDefault();
            if (dbOrder is null)
                throw new DomainError();
            var data = new Data(dbOrder, dbOrderItems);
            var order = Order.RestoreFrom(data);
            _orders.Add(id, data);
            return order;
        }

        public async Task Save(Order order)
        {
            if (!_orders.TryGetValue(order.Id, out var data))
                throw new DesignError(SaveOfUnknownAggregate);
            var transaction = db.GetCurrentTransaction();
            await data.Save(transaction);
        }
    }
}
```

## File: `Sources/Sales/Sales.Adapters/Orders/OrderSqlRepository.cs`
```csharp
namespace MyCompany.ECommerce.Sales.Orders;

public static partial class OrderSqlRepository
{
    private const string SameAggregateRestoredMoreThanOnce =
        "Same aggregate is restored from the repository more than once in a single business transaction";

    private const string SaveOfUnknownAggregate =
        $"Attempt to save {nameof(Order)} that wasn't created nor get with {nameof(OrderSqlRepository)}";
}
```

## File: `Sources/Sales/Sales.Adapters/Pricing/PriceListSqlRepository.cs`
```csharp
using System.Collections.Immutable;
using JetBrains.Annotations;
using MyCompany.ECommerce.Sales.Clients;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Pricing.PriceLists;
using MyCompany.ECommerce.Sales.Products;

namespace MyCompany.ECommerce.Sales.Pricing;

[UsedImplicitly]
public class PriceListSqlRepository : PriceListRepository
{
    public Task<Money> GetBasePriceFor(ClientId clientId, ProductAmount productAmount) => 
        throw new System.NotImplementedException();

    public Task<BasePrices> GetBasePricesFor(ClientId clientId, ImmutableArray<ProductAmount> productAmounts) => 
        throw new System.NotImplementedException();
}
```

## File: `Sources/Sales/Sales.Adapters/Pricing/Discounts/DiscountsSqlRepository.cs`
```csharp
using System.Collections.Immutable;
using JetBrains.Annotations;
using MyCompany.ECommerce.Sales.Clients;
using MyCompany.ECommerce.Sales.Products;

namespace MyCompany.ECommerce.Sales.Pricing.Discounts;

[UsedImplicitly]
public class DiscountsSqlRepository : DiscountsRepository
{
    public Task<ClientLevelDiscounts> GetFor(ClientId clientId) =>
        throw new System.NotImplementedException();

    public Task<ProductLevelDiscounts> GetFor(ImmutableArray<ProductAmount> productAmounts) =>
        throw new System.NotImplementedException();
}
```

## File: `Sources/Sales/Sales.Adapters/Time/SystemClock.cs`
```csharp
namespace MyCompany.ECommerce.Sales.Time;

public class SystemClock : Clock
{
    public DateTime Now
    {
        get
        {
            var now = DateTime.UtcNow;
            return new DateTime(now.Year, now.Month, now.Day, now.Hour, now.Minute, now.Second, now.Millisecond,
                DateTimeKind.Utc);
        }
    }
}
```

## File: `Sources/Sales/Sales.DeepModel/Sales.DeepModel.csproj`
```
﻿<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <AssemblyName>MyCompany.ECommerce.Sales.DeepModel</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.Sales</RootNamespace>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
    </PropertyGroup>

    <ItemGroup>
      <ProjectReference Include="..\..\TechnicalStuff\TechnicalStuff.Crud\TechnicalStuff.Crud.csproj" />
      <ProjectReference Include="..\..\TechnicalStuff\TechnicalStuff\TechnicalStuff.csproj" />
    </ItemGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
      <PackageReference Include="System.Collections.Immutable" Version="8.0.0" />
      <PackageReference Include="TaskTupleAwaiter" Version="2.1.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/Sales/Sales.DeepModel/SalesDeepModelLayerInfo.cs`
```csharp
using System.Reflection;
using System.Runtime.CompilerServices;
using NoesisVision.Annotations.Domain;
using NoesisVision.Annotations.Technology.CleanArchitecture;

[assembly: InternalsVisibleTo("MyCompany.ECommerce.Monolith.Startup")]
[assembly: InternalsVisibleTo("MyCompany.ECommerce.Sales.IntegrationTests")]
[assembly: EntitiesLayer]
[assembly: DomainModel]

namespace MyCompany.ECommerce.Sales;

public static class SalesDeepModelLayerInfo
{
    public static Assembly Assembly => typeof(SalesDeepModelLayerInfo).Assembly;
}
```

## File: `Sources/Sales/Sales.DeepModel/Clients/ClientId.cs`
```csharp
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Clients;

[DddValueObject]
public readonly struct ClientId : IEquatable<ClientId>
{
    public Guid Value { get; }

    public static ClientId New() => new(Guid.NewGuid());
    public static ClientId From(Guid value) => new(value);
    private ClientId(Guid value) => Value = value;

    public bool Equals(ClientId other) => Value.Equals(other.Value);
    public override bool Equals(object obj) => obj is ClientId other && Equals(other);
    public override int GetHashCode() => Value.GetHashCode();

    public override string ToString() => $"Client: {Value.ToString()}";
}
```

## File: `Sources/Sales/Sales.DeepModel/Clients/ClientRepository.cs`
```csharp
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Clients;

[DddRepository]
public interface ClientRepository
{
    Task<ClientStatus> GetStatusFor(ClientId clientId);
}
```

## File: `Sources/Sales/Sales.DeepModel/Clients/ClientStatus.cs`
```csharp
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Clients;

[DddValueObject]
public enum ClientStatus
{
    Normal,
    Vip
}
```

## File: `Sources/Sales/Sales.DeepModel/Commons/Currency.cs`
```csharp
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Commons;

[DddValueObject]
public enum Currency
{
    PLN,
    USD,
    EUR
}
```

## File: `Sources/Sales/Sales.DeepModel/Commons/Money.cs`
```csharp
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using MyCompany.ECommerce.TechnicalStuff;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Commons;

[DddValueObject]
public record Money(decimal Value, Currency Currency)
{
    public static Money Zero(Currency currency) => new(0, currency);
    public static Money Of(decimal value, Currency currency) => new(value, currency);

    public static Money operator +(Money x, Money y) => Calculate(x, y, (a, b) => a + b);
    public static Money operator -(Money x, Money y) => Calculate(x, y, (a, b) => a - b);

    private static Money Calculate(Money x, Money y, Func<decimal, decimal, decimal> calculate)
    {
        CheckCurrencies(x, y);
        return new Money(calculate(x.Value, y.Value), x.Currency);
    }

    public static Money operator *(Money x, int y) => Calculate(x, y, (a, b) => a * b);
    public static Money operator /(Money x, int y) => Calculate(x, y, (a, b) => a / b);
    public static Money operator *(Money x, decimal y) => Calculate(x, y, (a, b) => a * b);
    public static Money operator /(Money x, decimal y) => Calculate(x, y, (a, b) => a / b);

    public static Money operator *(Money x, Percentage y) => Calculate(x, y.Fraction, (a, b) => a * b);

    private static Money Calculate<T>(Money x, T y, Func<decimal, T, decimal> calculate) => 
        x with { Value = calculate(x.Value, y) };

    public static Percentage operator /(Money x, Money y)
    {
        CheckCurrencies(x, y);
        return Percentage.Of((int) Math.Round((x.Value / y.Value) * 100, 0));
    }

    public static Money Max(Money x, Money y) => x > y ? x : y;

    public static bool operator >(Money x, Money y) => Compare(x, y, (a, b) => a > b);
    public static bool operator <(Money x, Money y) => Compare(x, y, (a, b) => a < b);
    public static bool operator >=(Money x, Money y) => Compare(x, y, (a, b) => a >= b);
    public static bool operator <=(Money x, Money y) => Compare(x, y, (a, b) => a <= b);

    private static bool Compare(Money x, Money y, Func<decimal, decimal, bool> compare)
    {
        CheckCurrencies(x, y);
        return compare(x.Value, y.Value);
    }

    [SuppressMessage("ReSharper", "ParameterOnlyUsedForPreconditionCheck.Local")]
    private static void CheckCurrencies(Money x, Money y)
    {
        if (x.Currency != y.Currency)
            throw new DomainError();
    }

    public override string ToString() =>
        $"{Value.ToString("F", CultureInfo.InvariantCulture)} {Currency.ToCode()}";
}
```

## File: `Sources/Sales/Sales.DeepModel/Commons/Percentage.cs`
```csharp
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Commons;

[DddValueObject]
public readonly struct Percentage : IEquatable<Percentage>
{
    public int Value { get; }
    public decimal Fraction => (decimal) Value / 100;
        
    public static Percentage Of0 => new(0);
    public static Percentage Of100 => new(100);
    public static Percentage Of(int value) => new(value);

    private Percentage(int value) => Value = value;

    public static Percentage operator +(Percentage x, Percentage y) => new(x.Value + y.Value);
    public static Percentage operator -(Percentage x, Percentage y) => new(x.Value - y.Value);

    public static bool operator ==(Percentage x, Percentage y) => x.Equals(y);
    public static bool operator !=(Percentage x, Percentage y) => !x.Equals(y);
    public static bool operator >(Percentage x, Percentage y) => x.Value > y.Value;
    public static bool operator <(Percentage x, Percentage y) => x.Value < y.Value;
    public static bool operator >=(Percentage x, Percentage y) => x.Value >= y.Value;
    public static bool operator <=(Percentage x, Percentage y) => x.Value <= y.Value;

    public bool Equals(Percentage other) => Value == other.Value;
    public override bool Equals(object obj) => obj is Percentage other && Equals(other);
    public override int GetHashCode() => Value;

    public override string ToString() => $"{Value.ToString()}%";
}
    
public class Percentage2
{
    public int Value { get; }
    public decimal Fraction => (decimal) Value / 100;
        
    public static Percentage2 Of0 => new(0);
    public static Percentage2 Of100 => new(100);
    public static Percentage2 Of(int value) => new(value);

    private Percentage2(int value) => Value = value;

    public static Percentage2 operator +(Percentage2 x, Percentage2 y)
    {
        if (x == null) throw new ArgumentNullException(nameof(x));
        if (y == null) throw new ArgumentNullException(nameof(y));
        return new Percentage2(x.Value + y.Value);
    }
    public static Percentage2 operator -(Percentage2 x, Percentage2 y)
    {
        if (x == null) throw new ArgumentNullException(nameof(x));
        if (y == null) throw new ArgumentNullException(nameof(y));
        return new Percentage2(x.Value - y.Value);
    }

    public static bool operator ==(Percentage2 x, Percentage2 y) => x != null && x.Equals(y);
    public static bool operator !=(Percentage2 x, Percentage2 y) => x == null || !x.Equals(y);
    public static bool operator >(Percentage2 x, Percentage2 y)
    {
        if (x == null) throw new ArgumentNullException(nameof(x));
        if (y == null) throw new ArgumentNullException(nameof(y));
        return x.Value > y.Value;
    }
    public static bool operator <(Percentage2 x, Percentage2 y)
    {
        if (x == null) throw new ArgumentNullException(nameof(x));
        if (y == null) throw new ArgumentNullException(nameof(y));
        return x.Value < y.Value;
    }
    public static bool operator >=(Percentage2 x, Percentage2 y)
    {
        if (x == null) throw new ArgumentNullException(nameof(x));
        if (y == null) throw new ArgumentNullException(nameof(y));
        return x.Value >= y.Value;
    }
    public static bool operator <=(Percentage2 x, Percentage2 y)
    {
        if (x == null) throw new ArgumentNullException(nameof(x));
        if (y == null) throw new ArgumentNullException(nameof(y));
        return x.Value <= y.Value;
    }

    public override bool Equals(object obj) => obj is Percentage2 other && Value == other.Value;
    public override int GetHashCode() => Value;

    public override string ToString() => $"{Value.ToString()}%";
}
```

## File: `Sources/Sales/Sales.DeepModel/Commons/TaxId.cs`
```csharp
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Commons;

[DddValueObject]
public readonly struct TaxId(string value) : IEquatable<TaxId>
{
    public string Value { get; } = value;

    public bool Equals(TaxId other) => Value == other.Value;

    public override bool Equals(object obj) => obj is TaxId other && Equals(other);

    public override int GetHashCode() => Value.GetHashCode();
}
```

## File: `Sources/Sales/Sales.DeepModel/ExchangeRates/ExchangeRate.cs`
```csharp
using System.Globalization;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Pricing;
using MyCompany.ECommerce.TechnicalStuff;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.ExchangeRates;

[DddValueObject]
public struct ExchangeRate : PriceModifier, IEquatable<ExchangeRate>
{
    public Currency Currency { get; }
    public decimal Value { get; }
        
    public static ExchangeRate Of(Currency toCurrency, decimal value) => new(toCurrency, value);
        
    private ExchangeRate(Currency currency, decimal value)
    {
        Currency = currency;
        Value = value;
    }
        
    public Money ApplyOn(Money price)
    {
        if (price.Currency != Currency.PLN) throw new DomainError();
        return Money.Of(price.Value * Value, Currency);
    }

    public static Money operator *(Money money, ExchangeRate exchangeRate) => exchangeRate.ApplyOn(money);

    public bool Equals(ExchangeRate other) => (To: Currency, Value).Equals((other.Currency, other.Value));
    public override bool Equals(object obj) => obj is ExchangeRate other && Equals(other);
    public override int GetHashCode() => (To: Currency, Value).GetHashCode();

    public override string ToString() => 
        $"{Value.ToString(CultureInfo.InvariantCulture)} {Currency.ToCode()}/{Currency.PLN.ToCode()}";
}
```

## File: `Sources/Sales/Sales.DeepModel/ExchangeRates/ExchangeRateProvider.cs`
```csharp
using MyCompany.ECommerce.Sales.Commons;
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.Sales.ExchangeRates;

[ExternalSystemIntegration("Forex")]
public interface ExchangeRateProvider
{
    Task<ExchangeRate> GetFor(Currency currency);
}
```

## File: `Sources/Sales/Sales.DeepModel/Integrations/RiskManagement/RiskManagementIntegration.cs`
```csharp
using MyCompany.ECommerce.Sales.Clients;
using MyCompany.ECommerce.Sales.Commons;

namespace MyCompany.ECommerce.Sales.Integrations.RiskManagement;

public interface RiskManagementIntegration
{
    Task<Money> GetMaxOrderTotalCostFor(ClientId clientId);
}
```

## File: `Sources/Sales/Sales.DeepModel/Orders/AllOrderDetails.cs`
```csharp
﻿using JetBrains.Annotations;
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.Sales.Orders;

[ReadModel]
[UsedImplicitly(ImplicitUseTargetFlags.WithMembers)]
public class AllOrderDetails
{
    //TODO: DomainModel + Raw
    public Guid ClientId { get; set; }
    public string CurrencyCode { get; set; }
    public List<OrderItemDetails> Items { get; set; }
        
    // TODO: invoicing details, notes, etc.
}
```

## File: `Sources/Sales/Sales.DeepModel/Orders/InvoicingDetails.cs`
```csharp
using JetBrains.Annotations;
using Microsoft.AspNetCore.Mvc.ModelBinding;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Orders;

[DddValueObject]
[UsedImplicitly(ImplicitUseTargetFlags.WithMembers)]
public class InvoicingDetails
{
    [BindRequired] public string TaxId { get; set; }
    [BindRequired] public string Name { get; set; }
    //...
}
```

## File: `Sources/Sales/Sales.DeepModel/Orders/Order.Data.cs`
```csharp
using System.Diagnostics.CodeAnalysis;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Products;

namespace MyCompany.ECommerce.Sales.Orders;

public partial class Order
{
    private readonly Data _data;

    private Order(Data data) => _data = data;

    public static Order RestoreFrom(Data data) => new(data);

    public interface Data : IEquatable<Data>
    {
        OrderId Id { get; }
        Money MaxTotalCost { get; }
        bool IsPlaced { get; set; }
        IReadOnlyCollection<Item> Items { get; }
        
        public bool TryGetItem(ProductUnit productUnit, [NotNullWhen(true)] out Item? item)
        {
            item = Items.SingleOrDefault(i => i.ProductAmount.ProductUnit.Equals(productUnit));
            return item != null;
        }

        void Add(Item item);
        void Remove(Item item);

        bool IEquatable<Data>.Equals(Data? other) =>
            other is not null &&
            Id.Equals(other.Id) &&
            IsPlaced == other.IsPlaced &&
            Items.All(item => other.Items.Contains(item));
    }
}
```

## File: `Sources/Sales/Sales.DeepModel/Orders/Order.Events.cs`
```csharp
using System.Collections.Immutable;
using MyCompany.ECommerce.Sales.Pricing;
using MyCompany.ECommerce.Sales.Products;
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.Sales.Orders;

public partial class Order
{
    private readonly List<Event> _newEvents = new();
    public IReadOnlyList<Event> NewEvents => _newEvents.AsReadOnly();

    private void AddAndApply(Event @event)
    {
        @event.Apply(this);
        _newEvents.Add(@event);
    }

    public interface Event
    {
        void Apply(Order order);
    }

    [Event]
    public class CreatedFromOffer(ImmutableArray<Item> items) : Event
    {
        public ImmutableArray<Item> Items { get; } = items;

        public void Apply(Order order)
        {
            foreach (var item in Items)
                order._data.Add(item);
        }
    }

    [Event]
    public class ProductAmountAdded(ProductAmount productAmount) : Event
    {
        public ProductAmount ProductAmount { get; } = productAmount;

        public void Apply(Order order) => order.AddToItem(ProductAmount);
    }

    [Event]
    public class PricesConfirmed : Event
    {
        public ImmutableArray<Quote> Quotes { get; }
        public PriceAgreementType AgreementType { get; }
        public DateTime? AgreementExpiresOn { get; }

        public PricesConfirmed(ImmutableArray<Quote> quotes, PriceAgreementType agreementType, 
            DateTime? agreementExpiresOn)
        {
            switch (agreementType)
            {
                case PriceAgreementType.Non:
                    throw new ArgumentException();
                case PriceAgreementType.Temporary:
                    if (!agreementExpiresOn.HasValue)
                        throw new ArgumentException();
                    break;
                case PriceAgreementType.Final:
                    if (agreementExpiresOn.HasValue)
                        throw new ArgumentException();
                    break;
                default:
                    throw new ArgumentOutOfRangeException(nameof(agreementType), agreementType, null);
            }
            Quotes = quotes;
            AgreementType = agreementType;
            AgreementExpiresOn = agreementExpiresOn;
        }

        public void Apply(Order order) => order.ApplyPriceAgreements(Quotes, AgreementType, AgreementExpiresOn);
    }

    [Event]
    public class Placed : Event
    {
        public void Apply(Order order) => order._data.IsPlaced = true;
    }
}
```

## File: `Sources/Sales/Sales.DeepModel/Orders/Order.Factory.cs`
```csharp
using MyCompany.ECommerce.Sales.Clients;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Integrations.RiskManagement;
using MyCompany.ECommerce.Sales.Pricing;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Orders;

public partial class Order
{
    [DddFactory]
    public abstract class Factory(RiskManagementIntegration riskManagement)
    {
        public async Task<Order> NewWithMaxTotalCostFor(ClientId clientId)
        {
            var maxTotalCost = await riskManagement.GetMaxOrderTotalCostFor(clientId);
            return NewWith(maxTotalCost);
        }
        
        public Order NewWith(Money maxTotalCost)
        {
            var id = OrderId.New();
            var data = CreateData(id, maxTotalCost);
            return new Order(data);
        }

        public Order ImmediatelyPlacedBasedOn(Offer offer)
        {
            var id = OrderId.New();
            var data = CreateData(id, offer.TotalPrice);
            var order = new Order(data);
            foreach (var quote in offer.Quotes)
            {
                var item = Item.For(quote.ProductAmount);
                item.ConfirmPrice(quote.Price);
                order._data.Add(item);
            }
            order._data.IsPlaced = true;
            return order;
        }

        protected abstract Data CreateData(OrderId id, Money maxTotalCost);
    }
}
```

## File: `Sources/Sales/Sales.DeepModel/Orders/Order.Item.cs`
```csharp
using System.Diagnostics.CodeAnalysis;
using System.Text.Json.Serialization;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Products;

namespace MyCompany.ECommerce.Sales.Orders;

public partial class Order
{
    public class Item : IEquatable<Item>
    {
        public ProductUnit Id => ProductAmount.ProductUnit;
        public ProductAmount ProductAmount { get; private set; }
        public PriceAgreement PriceAgreement { get; private set; }

        [JsonConstructor]
        public Item(ProductAmount productAmount, PriceAgreement priceAgreement)
        {
            ProductAmount = productAmount;
            PriceAgreement = priceAgreement;
        }

        [SuppressMessage("ReSharper", "UnusedMember.Local", Justification = "EF")]
        private Item() { }

        public static Item For(ProductAmount productAmount) => new(productAmount, PriceAgreement.Non());

        public void Add(ProductAmount productAmount)
        {
            ProductAmount += productAmount;
            PriceAgreement = PriceAgreement.Non();
        }

        public void ConfirmPrice(Money price) => PriceAgreement = PriceAgreement.Final(price);

        public void ConfirmPrice(Money price, DateTime expiresOn) =>
            PriceAgreement = PriceAgreement.Temporary(price, expiresOn);

        public bool Equals(Item? other) => other is not null && Id.Equals(other.Id);

        public bool HasSameDataAs(Item other) =>
            ProductAmount.Equals(other.ProductAmount) &&
            PriceAgreement.Equals(other.PriceAgreement);
    }
}
```

## File: `Sources/Sales/Sales.DeepModel/Orders/Order.PriceAgreement.cs`
```csharp
using System.Diagnostics.CodeAnalysis;
using System.Text.Json.Serialization;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.TechnicalStuff;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Orders;

public partial class Order
{
    [DddValueObject]
    public class PriceAgreement : IEquatable<PriceAgreement>
    {
        public PriceAgreementType Type { get; }
        public Money? Price { get; }
        public DateTime? ExpiresOn { get; }

        public static PriceAgreement Non() => new(PriceAgreementType.Non, null, default);

        public static PriceAgreement Temporary(Money price, DateTime expiresOn) =>
            new(PriceAgreementType.Temporary, price, expiresOn);

        public static PriceAgreement Final(Money price) => new(PriceAgreementType.Final, price, default);

        [JsonConstructor]
        //https://github.com/dotnet/runtime/issues/44428
        public PriceAgreement(PriceAgreementType type, Money? price, DateTime? expiresOn)
        {
            Type = type;
            Price = price;
            ExpiresOn = expiresOn;
        }

        [SuppressMessage("ReSharper", "UnusedMember.Local", Justification = "EF")]
        private PriceAgreement() { }

        public bool CanChangePrice() => Type switch
        {
            PriceAgreementType.Non => true,
            PriceAgreementType.Temporary => true,
            PriceAgreementType.Final => false,
            _ => throw new ArgumentOutOfRangeException(nameof(Type), Type, null)
        };

        public bool IsValidOn(DateTime date) => Type switch
        {
            PriceAgreementType.Non => false,
            PriceAgreementType.Temporary => ExpiresOn >= date,
            PriceAgreementType.Final => true,
            _ => throw new ArgumentOutOfRangeException(nameof(Type), Type, null)
        };

        public bool Equals(PriceAgreement? other) => other is not null &&
                                                     Type == other.Type &&
                                                     Price == other.Price &&
                                                     ExpiresOn == other.ExpiresOn;

        public override bool Equals(object? obj) => obj is PriceAgreement other && Equals(other);

        public override int GetHashCode() => new HashCode()
            .CombineWith(Type)
            .CombineWith(Price)
            .CombineWith(ExpiresOn)
            .ToHashCode();
    }
}
```

## File: `Sources/Sales/Sales.DeepModel/Orders/Order.Repository.cs`
```csharp
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Orders;

public partial class Order
{
    [DddRepository]
    public interface Repository
    {
        Task<Order> GetBy(OrderId id);
        Task Save(Order order);
    }
}
```

## File: `Sources/Sales/Sales.DeepModel/Orders/Order.cs`
```csharp
using System.Collections.Immutable;
using MyCompany.ECommerce.Sales.Orders.PriceChanges;
using MyCompany.ECommerce.Sales.Pricing;
using MyCompany.ECommerce.Sales.Products;
using MyCompany.ECommerce.TechnicalStuff;
using NoesisVision.Annotations;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Orders;

[DddAggregate]
[ShortDescription("*An order is a request for products.* It is placed by a customer and contains " +
                  "a list of products with their amounts. The order is placed when the customer " +
                  "confirms the prices of the products.")]
public partial class Order : IEquatable<Order>, DataEquals<Order>
{
    public OrderId Id => _data.Id;

    public IEnumerable<ProductAmount> ProductAmounts => _data.Items.Select(item => item.ProductAmount);

    public void Add(ProductAmount productAmount)
    {
            if (_data.IsPlaced)
                throw new DomainError();
            AddAndApply(new ProductAmountAdded(productAmount));

            // Version without events:
            // AddToItem(productAmount);
        }

    private void AddToItem(ProductAmount productAmount)
    {
            var productUnit = productAmount.ProductUnit;
            if (_data.TryGetItem(productUnit, out var item))
                item.Add(productAmount);
            else
                _data.Add(Item.For(productAmount));
    }

    public void ConfirmPrices(Offer offer, PriceChangesPolicy priceChangesPolicy) =>
        ConfirmPrices(offer.Quotes, priceChangesPolicy, PriceAgreementType.Final, default);

    public void ConfirmPrices(Offer offer, PriceChangesPolicy priceChangesPolicy, DateTime agreementExpiresOn) =>
        ConfirmPrices(offer.Quotes, priceChangesPolicy, PriceAgreementType.Temporary, agreementExpiresOn);

    private void ConfirmPrices(ImmutableArray<Quote> newQuotes,
        PriceChangesPolicy priceChangesPolicy,
        PriceAgreementType agreementType,
        DateTime? agreementExpiresOn)
    {
        if (_data.IsPlaced)
            throw new DomainError();
        if (!newQuotes.All(quote => HasMatchingItemFor(quote.ProductAmount)))
            throw new DomainError();
        if (!newQuotes.All(quote => CanChangePriceFor(quote.ProductAmount)))
            throw new DomainError();
        var oldQuotes = _data.Items
            .Where(i => i.PriceAgreement.Type != PriceAgreementType.Non)
            .Select(i => Quote.For(i.ProductAmount, i.PriceAgreement.Price!))
            .ToImmutableArray();
        if (!priceChangesPolicy.CanChangePrices(oldQuotes, newQuotes))
            throw new DomainError();
        AddAndApply(new PricesConfirmed(newQuotes, agreementType, agreementExpiresOn));

        // Version without events:
        // ApplyPriceAgreements(newQuotes, agreementType, agreementExpiresOn);
    }

    private bool HasMatchingItemFor(ProductAmount productAmount) =>
        _data.TryGetItem(productAmount.ProductUnit, out var item) &&
        item.ProductAmount.Equals(productAmount);

    private bool CanChangePriceFor(ProductAmount productAmount) =>
        _data.TryGetItem(productAmount.ProductUnit, out var item) &&
        item.PriceAgreement.CanChangePrice();

    private void ApplyPriceAgreements(ImmutableArray<Quote> quotes, PriceAgreementType agreementType,
        DateTime? agreementExpiresOn)
    {
        foreach (var quote in quotes)
        {
            var productUnit = quote.ProductAmount.ProductUnit;
            if (!_data.TryGetItem(productUnit, out var item))
                throw new CorruptedDataError();
            switch (agreementType)
            {
                case PriceAgreementType.Temporary:
                    item.ConfirmPrice(quote.Price, agreementExpiresOn!.Value);
                    break;
                case PriceAgreementType.Final:
                    item.ConfirmPrice(quote.Price);
                    break;
                case PriceAgreementType.Non:
                    throw new CorruptedDataError();
                default:
                    throw new ArgumentOutOfRangeException();
            }
        }
    }

    public void Place(DateTime now)
    {
        if (_data.IsPlaced) return;
        if (!AllItemsHaveValidPriceAgreementOn(now)) throw new DomainError();
        AddAndApply(new Placed());

        // Version without events:
        // _isPlaced = true;
    }

    private bool AllItemsHaveValidPriceAgreementOn(DateTime date) =>
        _data.Items.All(item => item.PriceAgreement.IsValidOn(date));

    public override bool Equals(object? obj) => obj is Order other && Equals(other);
    public bool Equals(Order? other) => other is not null && Id.Equals(other.Id);
    public override int GetHashCode() => Id.GetHashCode();

    public bool HasSameDataAs(Order other) => _data.Equals(other._data);
}
```

## File: `Sources/Sales/Sales.DeepModel/Orders/Order.md`
```markdown
# Order

## Heading 2

**Lorem ipsum** dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Heading 2

_Sed ut perspiciatis_ unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"

### Heading 3

- list item 1
- list item 2
  - list item 2.1
    - list item 2.1.1
  - list item 2.2
- list item 3
```

## File: `Sources/Sales/Sales.DeepModel/Orders/OrderHeader.cs`
```csharp
using JetBrains.Annotations;
using Microsoft.AspNetCore.Mvc.ModelBinding;
using MyCompany.ECommerce.TechnicalStuff.Crud;
using Newtonsoft.Json;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Orders;

[DddEntity]
[UsedImplicitly(ImplicitUseTargetFlags.WithMembers)]
public class OrderHeader : CrudEntity
{
    [BindRequired]
    public Guid ClientId { get; set; }

    public InvoicingDetails InvoicingDetails { get; set; }

    [BindNever]
    [JsonIgnore]
    public List<OrderNote> Notes { get; set; }
        
    //...
}
```

## File: `Sources/Sales/Sales.DeepModel/Orders/OrderId.cs`
```csharp
using MyCompany.ECommerce.TechnicalStuff.ValueObjects;

namespace MyCompany.ECommerce.Sales.Orders;

public readonly record struct OrderId(Guid Value) : ValueObject<Guid>
{
    public static OrderId New() => new(Guid.NewGuid());
        
    public static OrderId From(Guid value) => new(value);
}
```

## File: `Sources/Sales/Sales.DeepModel/Orders/OrderItemDetails.cs`
```csharp
using JetBrains.Annotations;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Orders;

[DddValueObject]
[UsedImplicitly(ImplicitUseTargetFlags.WithMembers)]
public class OrderItemDetails
{
    public Guid ProductId { get; set; }
    public int Amount { get; set; }
    public string AmountUnit { get; set; }
    public decimal Price { get; set; }
}
```

## File: `Sources/Sales/Sales.DeepModel/Orders/OrderNote.cs`
```csharp
using JetBrains.Annotations;
using Microsoft.AspNetCore.Mvc.ModelBinding;
using MyCompany.ECommerce.TechnicalStuff.Crud;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Orders;

[DddEntity]
[UsedImplicitly(ImplicitUseTargetFlags.WithMembers)]
public class OrderNote : CrudEntity
{
    [BindNever]
    public Guid OrderId { get; set; }

    [BindNever]
    public Guid AuthorId { get; set; }

    [BindNever]
    public DateTime AddedOn { get; set; }

    [BindRequired]
    public string Text { get; set; }
    //...
}
```

## File: `Sources/Sales/Sales.DeepModel/Orders/PriceAgreementType.cs`
```csharp
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Orders;

[DddValueObject]
public enum PriceAgreementType : byte
{
    Non,
    Temporary,
    Final
}
```

## File: `Sources/Sales/Sales.DeepModel/Orders/PriceChanges/AllowAnyPriceChanges.cs`
```csharp
using System.Collections.Immutable;
using MyCompany.ECommerce.Sales.Pricing;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Orders.PriceChanges;

[DddDomainService]
public class AllowAnyPriceChanges : PriceChangesPolicy
{
    public bool CanChangePrices(ImmutableArray<Quote> oldQuotes, ImmutableArray<Quote> newQuotes) => true;
}
```

## File: `Sources/Sales/Sales.DeepModel/Orders/PriceChanges/AllowPriceChangesIfTotalPriceIsLower.cs`
```csharp
using System.Collections.Immutable;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Pricing;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Orders.PriceChanges;

[DddDomainService]
public class AllowPriceChangesIfTotalPriceIsLower : PriceChangesPolicy
{
    public bool CanChangePrices(ImmutableArray<Quote> oldQuotes, ImmutableArray<Quote> newQuotes) =>
        GetTotalPrice(newQuotes) < GetTotalPrice(oldQuotes.Where(q => newQuotes.Contains(q)));

    private static Money GetTotalPrice(IEnumerable<Quote> quotes) => quotes
        .Select(quote => quote.Price)
        .Aggregate((totalPrice, price) => totalPrice + price);
}
```

## File: `Sources/Sales/Sales.DeepModel/Orders/PriceChanges/PriceChangesPolicies.cs`
```csharp
using MyCompany.ECommerce.Sales.Clients;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Orders.PriceChanges;

[DddFactory]
public class PriceChangesPolicies(
    AllowAnyPriceChanges allowAny,
    AllowPriceChangesIfTotalPriceIsLower allowIfTotalPriceIsLower,
    ClientRepository clients)
{
    public async Task<PriceChangesPolicy> ChooseFor(ClientId clientId)
    {
        var clientStatus = await clients.GetStatusFor(clientId);
        return clientStatus switch
        {
            ClientStatus.Normal => allowAny,
            ClientStatus.Vip => allowIfTotalPriceIsLower,
            _ => throw new ArgumentOutOfRangeException(nameof(clientStatus), clientStatus, null)
        };
    }
}
```

## File: `Sources/Sales/Sales.DeepModel/Orders/PriceChanges/PriceChangesPolicy.cs`
```csharp
using System.Collections.Immutable;
using MyCompany.ECommerce.Sales.Pricing;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Orders.PriceChanges;

[DddDomainService]
public interface PriceChangesPolicy
{
    bool CanChangePrices(ImmutableArray<Quote> oldQuotes, ImmutableArray<Quote> newQuotes);
}
```

## File: `Sources/Sales/Sales.DeepModel/Pricing/CalculatePrices.cs`
```csharp
using System.Collections.Immutable;
using MyCompany.ECommerce.Sales.Clients;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.ExchangeRates;
using MyCompany.ECommerce.Sales.Pricing.PriceLists;
using MyCompany.ECommerce.Sales.Products;
using MyCompany.ECommerce.Sales.SalesChannels;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Pricing;

[DddDomainService]
public class CalculatePrices(
    PriceListRepository priceLists,
    OfferModifiers offerModifiers,
    ExchangeRateProvider exchangeRates)
{
    public async Task<Quote> For(ClientId clientId, SalesChannel salesChannel, ProductAmount productAmount,
        Currency currency) =>
        (await For(clientId, salesChannel, ImmutableArray.Create(productAmount), currency))
        .Quotes.Single();

    public Task<Offer> For(ClientId clientId, SalesChannel salesChannel,
        IEnumerable<ProductAmount> productAmounts, Currency currency) =>
        For(clientId, salesChannel, productAmounts.ToImmutableArray(), currency);
        
    public async Task<Offer> For(ClientId clientId, SalesChannel salesChannel,
        ImmutableArray<ProductAmount> productAmounts, Currency currency)
    {
        var offerRequest = OfferRequest.For(clientId, salesChannel, productAmounts);
        var (basePrices, offerModifier, exchangeRate) = await (
            priceLists.GetBasePricesFor(clientId, productAmounts),
            offerModifiers.ChooseFor(offerRequest),
            exchangeRates.GetFor(currency));

        return Offer.WithBasePrices(productAmounts, basePrices)
            .Apply(offerModifier)
            .Apply(exchangeRate);
    }
}
```

## File: `Sources/Sales/Sales.DeepModel/Pricing/IndividualSalesConditions.cs`
```csharp
using MyCompany.ECommerce.Sales.Pricing.Discounts;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Pricing;

[DddDomainService]
internal class IndividualSalesConditions(
    ClientLevelDiscounts clientLevelDiscounts,
    ProductLevelDiscounts productLevelDiscounts)
    : OfferModifier, QuoteModifier
{
    public Offer ApplyOn(Offer offer) => offer.Apply((QuoteModifier)this);

    public Quote ApplyOn(Quote quote)
    {
        var quote1 =clientLevelDiscounts.ApplyOn(quote);
        var quote2 = productLevelDiscounts.ApplyOn(quote);

        return quote1.Price < quote2.Price ? quote1 : quote2;
    }
}
```

## File: `Sources/Sales/Sales.DeepModel/Pricing/Offer.cs`
```csharp
using System.Collections.Immutable;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Pricing.PriceLists;
using MyCompany.ECommerce.Sales.Products;
using MyCompany.ECommerce.TechnicalStuff;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Pricing;

[DddValueObject]
public readonly struct Offer : IEquatable<Offer>
{
    private readonly ImmutableDictionary<ProductUnit, Quote> _items;
        
    public Currency Currency { get; }

    public int Count => _items.Count;
        
    public Money TotalPrice => Quotes.Aggregate(Money.Zero(Currency), (sum, current) => sum + current.Price);
        
    public ImmutableArray<Quote> Quotes => _items.Values.ToImmutableArray();
        
    public ImmutableArray<ProductAmount> ProductAmounts => _items.Values
        .Select(quote => quote.ProductAmount)
        .ToImmutableArray();
        
    public static Offer FromQuotes(Currency currency, params Quote[] quotes) => new(currency, quotes);
    public static Offer FromQuotes(Currency currency, IEnumerable<Quote> quotes) => new(currency, quotes);

    internal static Offer WithBasePrices(ImmutableArray<ProductAmount> productAmounts, BasePrices basePrices) => 
        FromQuotes(Currency.PLN, productAmounts.Select(productAmount => 
            Quote.For(productAmount, basePrices.GetFor(productAmount))));

    private Offer(Currency currency, IEnumerable<Quote> quotes)
    {
        var items = quotes
            .GroupBy(quote => quote.ProductAmount.ProductUnit)
            .Select(grouping => grouping
                .Aggregate((sum, current) => sum + current))
            .ToImmutableDictionary(quote => quote.ProductAmount.ProductUnit);
        if (items.Count == 0) throw new DomainError();
        if (items.Values.Any(quote => quote.Price.Currency != currency)) throw new DomainError();
        _items = items;
        Currency = currency;
    }

    internal Offer Apply(OfferModifier offerModifier) => offerModifier.ApplyOn(this);

    internal Offer Apply(QuoteModifier quoteModifier) =>
        FromQuotes(Currency, Quotes.Select(quote => quote.Apply(quoteModifier)));

    internal Offer Apply<TPriceModifier>(TPriceModifier priceModifier)
        where TPriceModifier : struct, PriceModifier
        => FromQuotes(Currency, Quotes.Select(quote => quote.Apply(priceModifier)));

    public bool Compare(Offer other, Percentage accuracy) => TotalPrice / other.TotalPrice > accuracy;
        
    // TODO: real Equals and GetHashCode
    public bool Equals(Offer other) => Quotes.Equals(other.Quotes);
    public override bool Equals(object obj) => obj is Offer other && Equals(other);
    public override int GetHashCode() => Quotes.GetHashCode();

    public override string ToString() => $"Offer with total price: {TotalPrice.ToString()}";
}
```

## File: `Sources/Sales/Sales.DeepModel/Pricing/OfferModifier.cs`
```csharp
using System.Diagnostics.Contracts;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Pricing;

[DddDomainService]
public interface OfferModifier
{
    [Pure]
    Offer ApplyOn(Offer offer);
}

[DddDomainService]
public delegate Offer OfferModifier2(Offer offer);

public class AggregatedModifier(List<OfferModifier> modifiers) : OfferModifier
{
    public Offer ApplyOn(Offer offer) => modifiers
        .Aggregate(offer, (current, modifier) => modifier.ApplyOn(current));
}
```

## File: `Sources/Sales/Sales.DeepModel/Pricing/OfferModifiers.cs`
```csharp
using MyCompany.ECommerce.Sales.Pricing.Discounts;
using MyCompany.ECommerce.Sales.Pricing.SpecialOffers;
using MyCompany.ECommerce.Sales.SalesChannels;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Pricing;

[DddFactory]
public class OfferModifiers(DiscountsRepository discountsRepository)
{
    public async Task<OfferModifier> ChooseFor(OfferRequest offerRequest) =>
        ThreeForTwo.Or(
            EverySecondBoxForHalfPrice.Or(
                CanApplyIndividualSalesConditions(offerRequest)
                    ? await GetIndividualSalesConditions(offerRequest) 
                    : await GetProductLevelDiscounts(offerRequest)));

    private static bool CanApplyIndividualSalesConditions(OfferRequest offerRequest) =>
        offerRequest.SalesChannel == SalesChannel.Wholesale;
        
    private async Task<OfferModifier> GetIndividualSalesConditions(OfferRequest offerRequest)
    {
        var (clientLevelDiscounts, productLevelDiscounts) = await (
            discountsRepository.GetFor(offerRequest.ClientId),
            discountsRepository.GetFor(offerRequest.ProductAmounts));

        return new IndividualSalesConditions(clientLevelDiscounts, productLevelDiscounts);
    }

    private Task<ProductLevelDiscounts> GetProductLevelDiscounts(OfferRequest offerRequest) => 
        discountsRepository.GetFor(offerRequest.ProductAmounts);
}
```

## File: `Sources/Sales/Sales.DeepModel/Pricing/OfferRequest.cs`
```csharp
using System.Collections.Immutable;
using MyCompany.ECommerce.Sales.Clients;
using MyCompany.ECommerce.Sales.Products;
using MyCompany.ECommerce.Sales.SalesChannels;
using MyCompany.ECommerce.TechnicalStuff;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Pricing;

[DddValueObject]
public readonly struct OfferRequest : IEquatable<OfferRequest>
{
    public ClientId ClientId { get; }
    public SalesChannel SalesChannel { get; }
    public ImmutableArray<ProductAmount> ProductAmounts { get; }

    public static OfferRequest For(ClientId clientId, SalesChannel salesChannel,
        ImmutableArray<ProductAmount> productAmounts) => new(clientId, salesChannel, productAmounts);

    private OfferRequest(ClientId clientId, SalesChannel salesChannel, ImmutableArray<ProductAmount> productAmounts)
    {
        ClientId = clientId;
        SalesChannel = salesChannel;
        ProductAmounts = productAmounts;
    }

    public bool Equals(OfferRequest other) =>
        (ClientId, SalesChannel).Equals((other.ClientId, other.SalesChannel)) &&
        ProductAmounts.SequenceEqual(other.ProductAmounts);
    public override bool Equals(object obj) => obj is OfferRequest other && Equals(other);
    public override int GetHashCode() => (ClientId, SalesChannel).GetHashCode();

    public override string ToString() => $"Offer request for {ClientId.ToString()} and {SalesChannel.ToCode()}";
}
```

## File: `Sources/Sales/Sales.DeepModel/Pricing/PriceModifier.cs`
```csharp
using System.Diagnostics.Contracts;
using MyCompany.ECommerce.Sales.Commons;

namespace MyCompany.ECommerce.Sales.Pricing;

internal interface PriceModifier
{
    [Pure]
    Money ApplyOn(Money price);
}
```

## File: `Sources/Sales/Sales.DeepModel/Pricing/Quote.cs`
```csharp
using System.Text.Json.Serialization;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Products;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Pricing;

[DddValueObject]
[method: JsonConstructor]
public readonly struct Quote(ProductAmount productAmount, Money price) : IEquatable<Quote>
{
    public ProductAmount ProductAmount { get; } = productAmount;
    public Money Price { get; } = price;

    public static Quote For(ProductAmount productAmount, Money price) => new(productAmount, price);

    internal Quote Apply<TPriceModifier>(TPriceModifier priceModifier)
        where TPriceModifier : struct, PriceModifier => new(ProductAmount, priceModifier.ApplyOn(Price));

    internal Quote Apply(QuoteModifier quoteModifier) => quoteModifier.ApplyOn(this);

    public Quote ChangePrice(Money newPrice) => new(ProductAmount, newPrice);

    public static Quote operator +(Quote x, Quote y) => For(x.ProductAmount + y.ProductAmount, x.Price + y.Price);

    public bool Equals(Quote other) => (ProductAmount, Price).Equals((other.ProductAmount, other.Price));
    public override bool Equals(object? obj) => obj is Quote other && Equals(other);
    public override int GetHashCode() => (ProductAmount, Price).GetHashCode();

    public override string ToString() => $"{ProductAmount} - {Price}";
}
```

## File: `Sources/Sales/Sales.DeepModel/Pricing/QuoteModifier.cs`
```csharp
using System.Diagnostics.Contracts;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Pricing;

[DddDomainService]
internal interface QuoteModifier
{
    [Pure]
    Quote ApplyOn(Quote quote);
}
```

## File: `Sources/Sales/Sales.DeepModel/Pricing/README.md`
```markdown
README lorem ipsum
```

## File: `Sources/Sales/Sales.DeepModel/Pricing/Discounts/ClientLevelDiscounts.cs`
```csharp
using System.Collections.Immutable;
using MyCompany.ECommerce.Sales.Products;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Pricing.Discounts;

[DddDomainService]
public class ClientLevelDiscounts(PercentageDiscount baseDiscountValue, 
    IEnumerable<ProductDiscount> productDiscounts) : OfferModifier, QuoteModifier
{
    private readonly PercentageDiscount _baseDiscount = baseDiscountValue;

    private readonly ImmutableDictionary<ProductUnit, Discount> _productDiscounts = productDiscounts.ToImmutableDictionary(
            d => d.ProductUnit, d => d.Discount);

    public Offer ApplyOn(Offer offer) => offer.Apply((QuoteModifier) this);

    public Quote ApplyOn(Quote quote)
    {
        var productAmount = quote.ProductAmount;
        return _productDiscounts.TryGetValue(productAmount.ProductUnit, out var discount)
            ? quote.Apply(discount)
            : quote.Apply(_baseDiscount);
    }
}
```

## File: `Sources/Sales/Sales.DeepModel/Pricing/Discounts/Discount.cs`
```csharp
using MyCompany.ECommerce.Sales.Commons;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Pricing.Discounts;

[DddValueObject]
public readonly struct Discount : PriceModifier, IEquatable<Discount>
{
    private readonly bool _isPercentage;
    private readonly PercentageDiscount _percentageDiscount;
    private readonly ValueDiscount _valueDiscount;

    public static Discount Percentage(Percentage value) => new(true, PercentageDiscount.Of(value), default);
        
    public static Discount Value(Money value) => new(true, default, ValueDiscount.Of(value));

    private Discount(bool isPercentage, PercentageDiscount percentageDiscount, ValueDiscount valueDiscount)
    {
        _isPercentage = isPercentage;
        _percentageDiscount = percentageDiscount;
        _valueDiscount = valueDiscount;
    }

    public Money ApplyOn(Money price) => _isPercentage
        ? _percentageDiscount.ApplyOn(price)
        : _valueDiscount.ApplyOn(price);

    public bool Equals(Discount other) => (_isPercentage, _percentageDiscount, _valueDiscount)
        .Equals((other._isPercentage, other._percentageDiscount, other._valueDiscount));
    public override bool Equals(object? obj) => obj is Discount other && Equals(other);
    public override int GetHashCode() => (_isPercentage, _percentageDiscount, _valueDiscount).GetHashCode();

    public override string ToString() => _isPercentage ? _percentageDiscount.ToString() : _valueDiscount.ToString();
}
```

## File: `Sources/Sales/Sales.DeepModel/Pricing/Discounts/DiscountsRepository.cs`
```csharp
using System.Collections.Immutable;
using MyCompany.ECommerce.Sales.Clients;
using MyCompany.ECommerce.Sales.Products;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Pricing.Discounts;

[DddRepository]
public interface DiscountsRepository
{
    Task<ClientLevelDiscounts> GetFor(ClientId clientId);
    Task<ProductLevelDiscounts> GetFor(ImmutableArray<ProductAmount> productAmounts);
}
```

## File: `Sources/Sales/Sales.DeepModel/Pricing/Discounts/PercentageDiscount.cs`
```csharp
using MyCompany.ECommerce.Sales.Commons;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Pricing.Discounts;

[DddValueObject]
public readonly struct PercentageDiscount : PriceModifier, IEquatable<PercentageDiscount>
{
    private readonly Percentage _value;

    public static PercentageDiscount Of(Percentage value) => new(value);
        
    private PercentageDiscount(Percentage value) => _value = value;

    public Money ApplyOn(Money price) => price * (Percentage.Of100 - _value);

    public bool Equals(PercentageDiscount other) => 
        _value.Equals(other._value);
    public override bool Equals(object? obj) => obj is PercentageDiscount other && Equals(other);
    public override int GetHashCode() => _value.GetHashCode();

    public override string ToString() => $"Discount of {_value.ToString()}";
}
```

## File: `Sources/Sales/Sales.DeepModel/Pricing/Discounts/ProductDiscount.cs`
```csharp
using MyCompany.ECommerce.Sales.Products;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Pricing.Discounts;

[DddValueObject]
public readonly struct ProductDiscount : IEquatable<ProductDiscount>
{
    public ProductUnit ProductUnit { get; }
    public Discount Discount { get; }

    public static ProductDiscount Of(ProductUnit productUnit, Discount discount) => new(productUnit, discount);
        
    private ProductDiscount(ProductUnit productUnit, Discount discount)
    {
        ProductUnit = productUnit;
        Discount = discount;
    }

    public bool Equals(ProductDiscount other) => (ProductUnit, Discount)
        .Equals((other.ProductUnit, other.Discount));
    public override bool Equals(object obj) => obj is ProductDiscount other && Equals(other);
    public override int GetHashCode() => (ProductUnit, Discount).GetHashCode();

    public override string ToString() => $"{Discount.ToString()} for {ProductUnit.ToString()}";
}
```

## File: `Sources/Sales/Sales.DeepModel/Pricing/Discounts/ProductLevelDiscounts.cs`
```csharp
using System.Collections.Immutable;
using MyCompany.ECommerce.Sales.Products;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Pricing.Discounts;

[DddDomainService]
public class ProductLevelDiscounts : OfferModifier, QuoteModifier
{
    private readonly ImmutableDictionary<ProductUnit, Discount> _discounts;

    public static ProductLevelDiscounts Of(IEnumerable<ProductDiscount> discounts) => 
        new(discounts.ToImmutableDictionary(
            d => d.ProductUnit, 
            d => d.Discount));

    private ProductLevelDiscounts(ImmutableDictionary<ProductUnit, Discount> discounts) => 
        _discounts = discounts;

    public Offer ApplyOn(Offer offer) => offer.Apply((QuoteModifier) this);

    public Quote ApplyOn(Quote quote)
    {
        var productAmount = quote.ProductAmount;
        return _discounts.TryGetValue(productAmount.ProductUnit, out var discount)
            ? quote.Apply(discount)
            : quote;
    }
}

public static class ProductLevelDiscounts2
{
    public static OfferModifier2 ProductLevelDiscounts(IEnumerable<ProductDiscount> discounts) =>
        ProductLevelDiscounts(discounts.ToImmutableDictionary(
            d => d.ProductUnit, 
            d => d.Discount));

    private static OfferModifier2 ProductLevelDiscounts(ImmutableDictionary<ProductUnit, Discount> discounts) =>
        offer => Offer.FromQuotes(offer.Currency, offer.Quotes.Select(quote => RecalculateQuote(quote, discounts)));
        
    private static Quote RecalculateQuote(Quote quote, ImmutableDictionary<ProductUnit, Discount> discounts) =>
        discounts.TryGetValue(quote.ProductAmount.ProductUnit, out var discount)
            ? quote.Apply(discount)
            : quote;
}
```

## File: `Sources/Sales/Sales.DeepModel/Pricing/Discounts/ValueDiscount.cs`
```csharp
using MyCompany.ECommerce.Sales.Commons;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Pricing.Discounts;

[DddValueObject]
public readonly struct ValueDiscount : PriceModifier, IEquatable<ValueDiscount>
{
    private readonly Money _value;

    public static ValueDiscount Of(Money value) => new(value);
        
    private ValueDiscount(Money value) => _value = value;

    public Money ApplyOn(Money price) => Money.Max(price - _value, Money.Zero(price.Currency));

    public bool Equals(ValueDiscount other) => _value.Equals(other._value);
    public override bool Equals(object? obj) => obj is ValueDiscount other && Equals(other);
    public override int GetHashCode() => _value.GetHashCode();

    public override string ToString() => $"Discount of {_value}";
}
```

## File: `Sources/Sales/Sales.DeepModel/Pricing/PriceLists/BasePrice.cs`
```csharp
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Products;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Pricing.PriceLists;

[DddValueObject]
public readonly struct BasePrice : IEquatable<BasePrice>
{
    public ProductUnit ProductUnit { get; }
    public Money Price { get; }
        
    public BasePrice Of(ProductUnit productUnit, Money price) => new(productUnit, price);

    private BasePrice(ProductUnit productUnit, Money price)
    {
        ProductUnit = productUnit;
        Price = price;
    }

    public bool Equals(BasePrice other) => (ProductUnit, Price).Equals((other.ProductUnit, other.Price));
    public override bool Equals(object obj) => obj is BasePrice other && Equals(other);
    public override int GetHashCode() => (ProductUnit, Price).GetHashCode();

    public override string ToString() => $"Base price of {ProductUnit.ToString()}: {Price.ToString()}";
}
```

## File: `Sources/Sales/Sales.DeepModel/Pricing/PriceLists/BasePrices.cs`
```csharp
using System.Collections.Immutable;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Products;
using MyCompany.ECommerce.TechnicalStuff;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Pricing.PriceLists;

[DddValueObject]
public readonly struct BasePrices
{
    private readonly ImmutableDictionary<ProductUnit, Money> _prices;

    public static BasePrices Of(IEnumerable<BasePrice> prices) => new(prices);

    private BasePrices(IEnumerable<BasePrice> prices) => 
        _prices = prices.ToImmutableDictionary(
            p => p.ProductUnit, 
            p => p.Price);

    public Money GetFor(ProductAmount productAmount) =>
        _prices.TryGetValue(productAmount.ProductUnit, out var price) 
            ? price * productAmount.Amount.Value
            : throw new DomainError();
}
```

## File: `Sources/Sales/Sales.DeepModel/Pricing/PriceLists/PriceListRepository.cs`
```csharp
using System.Collections.Immutable;
using MyCompany.ECommerce.Sales.Clients;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Products;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Pricing.PriceLists;

[DddRepository]
public interface PriceListRepository
{
    Task<Money> GetBasePriceFor(ClientId clientId, ProductAmount productAmount);
    Task<BasePrices> GetBasePricesFor(ClientId clientId, ImmutableArray<ProductAmount> productAmounts);
}
```

## File: `Sources/Sales/Sales.DeepModel/Pricing/SpecialOffers/EverySecondBoxForHalfPrice.cs`
```csharp
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Pricing.SpecialOffers;

[DddDomainService]
public class EverySecondBoxForHalfPrice : SpecialOffer
{
    public static EverySecondBoxForHalfPrice Or(OfferModifier fallbackModifier) => new(fallbackModifier);

    private EverySecondBoxForHalfPrice(OfferModifier fallbackModifier) : base(fallbackModifier)
    {
    }

    public override Offer ApplyOn(Offer offer)
    {
        // implementation coming soon
        return base.ApplyOn(offer);
    }
}
```

## File: `Sources/Sales/Sales.DeepModel/Pricing/SpecialOffers/SpecialOffer.cs`
```csharp
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Pricing.SpecialOffers;

[DddDomainService]
public class SpecialOffer : OfferModifier
{
    private readonly OfferModifier _fallbackModifier;

    protected SpecialOffer(OfferModifier fallbackModifier) => _fallbackModifier = fallbackModifier;

    public virtual Offer ApplyOn(Offer offer) => _fallbackModifier.ApplyOn(offer);
}
```

## File: `Sources/Sales/Sales.DeepModel/Pricing/SpecialOffers/ThreeForTwo.cs`
```csharp
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Pricing.SpecialOffers;

[DddDomainService]
public class ThreeForTwo : SpecialOffer
{
    public static ThreeForTwo Or(OfferModifier fallbackModifier) => new(fallbackModifier);

    private ThreeForTwo(OfferModifier fallbackModifier) : base(fallbackModifier)
    {
    }

    public override Offer ApplyOn(Offer offer)
    {
        // implementation coming soon
        return base.ApplyOn(offer);
    }
}
```

## File: `Sources/Sales/Sales.DeepModel/Products/Amount.cs`
```csharp
using MyCompany.ECommerce.TechnicalStuff;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Products;

[DddValueObject]
public record Amount(int Value, AmountUnit Unit)
{
    public static Amount Of(int value, AmountUnit unit) => new(value, unit);

    public static Amount operator +(Amount x, Amount y)
    {
        CheckUnits(x, y);
        return new Amount(x.Value + y.Value, x.Unit);
    }
        
    public static Amount operator -(Amount x, Amount y)
    {
        CheckUnits(x, y);
        return new Amount(x.Value - y.Value, x.Unit);
    }

    private static void CheckUnits(Amount x, Amount y)
    {
        if (x.Unit != y.Unit) throw new DomainError();
    }
}
```

## File: `Sources/Sales/Sales.DeepModel/Products/AmountUnit.cs`
```csharp
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Products;

[DddValueObject]
public enum AmountUnit
{
    Unit,
    Box,
    Palette
}
```

## File: `Sources/Sales/Sales.DeepModel/Products/ProductAmount.cs`
```csharp
using System.Diagnostics.CodeAnalysis;
using MyCompany.ECommerce.TechnicalStuff;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Products;

[DddValueObject]
public record ProductAmount(ProductId ProductId, Amount Amount)
{
    public ProductUnit ProductUnit => ProductUnit.Of(ProductId, Amount.Unit);

    public static ProductAmount Of(ProductId productId, int value, AmountUnit unit) =>
        new(productId, Amount.Of(value, unit));
        
    public static ProductAmount Of(ProductId productId, Amount amount) => new(productId, amount);
        
    [SuppressMessage("ReSharper", "UnusedMember.Local", Justification = "EF")]
    private ProductAmount() : this(default, default!) { }

    public static ProductAmount operator +(ProductAmount x, ProductAmount y)
    {
        CheckProductId(x, y);
        return Of(x.ProductId, x.Amount + y.Amount);
    }
        
    public static ProductAmount operator -(ProductAmount x, ProductAmount y)
    {
        CheckProductId(x, y);
        return Of(x.ProductId, x.Amount - y.Amount);
    }

    private static void CheckProductId(ProductAmount x, ProductAmount y)
    {
        if (!x.ProductId.Equals(y.ProductId)) throw new DomainError();
    }
}
```

## File: `Sources/Sales/Sales.DeepModel/Products/ProductId.cs`
```csharp
using MyCompany.ECommerce.TechnicalStuff.ValueObjects;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Products;

[DddValueObject]
public readonly struct ProductId : ValueObject<Guid>, IEquatable<ProductId>
{
    public Guid Value { get; init; }

    public static ProductId New() => new(Guid.NewGuid());
    public static ProductId From(Guid value) => new(value);
    private ProductId(Guid value) => Value = value;

    public override bool Equals(object obj) => obj is ProductId other && Equals(other);
    public bool Equals(ProductId other) => Value.Equals(other.Value);
    public override int GetHashCode() => Value.GetHashCode();

    public override string ToString() => $"Product: {Value.ToString()}";
}
```

## File: `Sources/Sales/Sales.DeepModel/Products/ProductUnit.cs`
```csharp
using MyCompany.ECommerce.TechnicalStuff;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Products;

[DddValueObject]
public readonly struct ProductUnit : IEquatable<ProductUnit>
{
    public ProductId ProductId { get; }
    public AmountUnit Unit { get; }
        
    public static ProductUnit Of(ProductId productId, AmountUnit unit) => new(productId, unit);

    private ProductUnit(ProductId productId, AmountUnit unit)
    {
        ProductId = productId;
        Unit = unit;
    }
        
    public bool Equals(ProductUnit other) => (ProductId, Unit).Equals((other.ProductId, other.Unit));
    public override bool Equals(object obj) => obj is ProductUnit other && Equals(other);
    public override int GetHashCode() => (ProductId, Unit).GetHashCode();
        
    public override string ToString() => $"{Unit.ToCode()} of {ProductId.ToString()}";
}
```

## File: `Sources/Sales/Sales.DeepModel/SalesChannels/SalesChannel.cs`
```csharp
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.SalesChannels;

[DddValueObject]
public enum SalesChannel
{
    OnlineSale,
    Wholesale
}
```

## File: `Sources/Sales/Sales.DeepModel/Time/Clock.cs`
```csharp
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.Time;

[DddDomainService]
public interface Clock
{
    DateTime Now { get; }
}
```

## File: `Sources/Sales/Sales.DeepModel.Tests/Sales.DeepModel.Tests.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <IsPackable>false</IsPackable>
        <RootNamespace>MyCompany.ECommerce.Sales</RootNamespace>
        <AssemblyName>MyCompany.ECommerce.Sales.DeepModel.Tests</AssemblyName>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
    </PropertyGroup>

    <ItemGroup>
        <PackageReference Include="BDD-toolkit-dotnet" Version="2.4.0" />
        <PackageReference Include="FluentAssertions" Version="6.12.0" />
        <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
        <PackageReference Include="Microsoft.NET.Test.Sdk" Version="17.9.0" />
        <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
        <PackageReference Include="xunit" Version="2.8.0" />
        <PackageReference Include="xunit.runner.visualstudio" Version="2.8.0">
          <PrivateAssets>all</PrivateAssets>
          <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
        </PackageReference>
        <PackageReference Include="coverlet.collector" Version="6.0.2">
          <PrivateAssets>all</PrivateAssets>
          <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
        </PackageReference>
    </ItemGroup>

    <ItemGroup>
      <ProjectReference Include="..\Sales.DeepModel\Sales.DeepModel.csproj" />
    </ItemGroup>

</Project>
```

## File: `Sources/Sales/Sales.DeepModel.Tests/Commons/MoneyTests.cs`
```csharp
using FluentAssertions;
using ITLIBRIUM.BddToolkit;
using MyCompany.ECommerce.TechnicalStuff;
using Xunit;

namespace MyCompany.ECommerce.Sales.Commons;

public class MoneyTests
{
    [Fact]
    public void CanAddSameCurrencies() => Bdd.Scenario<Context>()
        .Given(c => c.FirstValueWas(1.01m, Currency.PLN))
        .And(c => c.SecondValueWas(2.02m, Currency.PLN))
        .When(c => c.FirstValueIsAddedToSecondValue())
        .Then(c => c.ResultIs(3.03m, Currency.PLN))
        .Test();
        
    [Fact]
    public void CanNotAddDifferentCurrencies() => Bdd.Scenario<Context>()
        .Given(c => c.FirstValueWas(1, Currency.PLN))
        .And(c => c.SecondValueWas(2, Currency.EUR))
        .When(c => c.FirstValueIsAddedToSecondValue())
        .Then((c, r) => c.ErrorIsReturned(r))
        .Test();
        
    [Fact]
    public void CanSubtractSameCurrencies() => Bdd.Scenario<Context>()
        .Given(c => c.FirstValueWas(1.01m, Currency.PLN))
        .And(c => c.SecondValueWas(3.03m, Currency.PLN))
        .When(c => c.FirstValueIsSubtractedFromSecondValue())
        .Then(c => c.ResultIs(2.02m, Currency.PLN))
        .Test();
        
    [Fact]
    public void CanNotSubtractDifferentCurrencies() => Bdd.Scenario<Context>()
        .Given(c => c.FirstValueWas(1, Currency.PLN))
        .And(c => c.SecondValueWas(2, Currency.EUR))
        .When(c => c.FirstValueIsSubtractedFromSecondValue())
        .Then((c, r) => c.ErrorIsReturned(r))
        .Test();
        
    [Fact]
    public void CanMultiplyByInteger() => Bdd.Scenario<Context>()
        .Given(c => c.FirstValueWas(1.01m, Currency.PLN))
        .And(c => c.MultiplierWas(2))
        .When(c => c.FirstValueIsMultipliedByInt())
        .Then(c => c.ResultIs(2.02m, Currency.PLN))
        .Test();
        
    [Fact]
    public void CanMultiplyByDecimal() => Bdd.Scenario<Context>()
        .Given(c => c.FirstValueWas(1.10m, Currency.PLN))
        .And(c => c.MultiplierWas(2.5m))
        .When(c => c.FirstValueIsMultipliedByDecimal())
        .Then(c => c.ResultIs(2.75m, Currency.PLN))
        .Test();
        
    [Fact]
    public void CanMultiplyByPercentage() => Bdd.Scenario<Context>()
        .Given(c => c.FirstValueWas(1.10m, Currency.PLN))
        .And(c => c.PercentageMultiplierWas(250), "Multiplier is 250%")
        .When(c => c.FirstValueIsMultipliedByPercentage())
        .Then(c => c.ResultIs(2.75m, Currency.PLN))
        .Test();
        
    [Fact]
    public void CanDividedByInteger() => Bdd.Scenario<Context>()
        .Given(c => c.FirstValueWas(2.02m, Currency.PLN))
        .And(c => c.DividerWas(2))
        .When(c => c.FirstValueIsDividedByInt())
        .Then(c => c.ResultIs(1.01m, Currency.PLN))
        .Test();
        
    [Fact]
    public void CanDividedByDecimal() => Bdd.Scenario<Context>()
        .Given(c => c.FirstValueWas(2.75m, Currency.PLN))
        .And(c => c.DividerWas(2.5m))
        .When(c => c.FirstValueIsDividedByDecimal())
        .Then(c => c.ResultIs(1.10m, Currency.PLN))
        .Test();
        
    [Fact]
    public void CanDividedByMoney() => Bdd.Scenario<Context>()
        .Given(c => c.FirstValueWas(2.75m, Currency.PLN))
        .And(c => c.SecondValueWas(2.50m, Currency.PLN))
        .When(c => c.FirstValueIsDividedBySecondValue())
        .Then(c => c.ResultIs(110), "Result is 110%")
        .Test();
        
    [Fact]
    public void CanCalculateMaxValueForSameCurrencies() => Bdd.Scenario<Context>()
        .Given(c => c.FirstValueWas(2.75m, Currency.PLN))
        .And(c => c.SecondValueWas(2.50m, Currency.PLN))
        .When(c => c.MaxValueIsCalculated())
        .Then(c => c.ResultIs(2.75m, Currency.PLN))
        .Test();
        
    [Fact]
    public void CanNotCalculateMaxValueForDifferentCurrencies() => Bdd.Scenario<Context>()
        .Given(c => c.FirstValueWas(2.75m, Currency.PLN))
        .And(c => c.SecondValueWas(2.50m, Currency.EUR))
        .When(c => c.MaxValueIsCalculated())
        .Then((c, r) => c.ErrorIsReturned(r))
        .Test();

    [Theory]
    [InlineData(1.01, 1.01, Comparison.Equal, true)]
    [InlineData(1.01, 1.02, Comparison.Equal, false)]
    [InlineData(1.01, 1.02, Comparison.NotEqual, true)]
    [InlineData(1.01, 1.01, Comparison.NotEqual, false)]
    [InlineData(1.02, 1.01, Comparison.Greater, true)]
    [InlineData(1.01, 1.02, Comparison.Greater, false)]
    [InlineData(1.02, 1.02, Comparison.GreaterOrEqual, true)]
    [InlineData(1.01, 1.02, Comparison.GreaterOrEqual, false)]
    [InlineData(1.01, 1.02, Comparison.Less, true)]
    [InlineData(1.02, 1.01, Comparison.Less, false)]
    [InlineData(1.02, 1.02, Comparison.LessOrEqual, true)]
    [InlineData(1.02, 1.01, Comparison.LessOrEqual, false)]
    public void CanCompareSameCurrencies(decimal firstValue, decimal secondValue, Comparison comparison, 
        bool result) => Bdd.Scenario<Context>()
        .Given(c => c.FirstValueWas(firstValue, Currency.PLN))
        .And(c => c.SecondValueWas(secondValue, Currency.PLN))
        .When(c => c.FirstValueIsComparedToSecondValue(comparison))
        .Then(c => c.ResultIs(result))
        .Test();
        
    [Theory]
    [InlineData(Comparison.Equal, false)]
    [InlineData(Comparison.NotEqual, true)]
    public void ValuesWithDifferentCurrenciesAreNotEqual(Comparison comparison, bool result) => Bdd.Scenario<Context>()
        .Given(c => c.FirstValueWas(1.01m, Currency.PLN))
        .And(c => c.SecondValueWas(1.01m, Currency.EUR))
        .When(c => c.FirstValueIsComparedToSecondValue(comparison))
        .Then(c => c.ResultIs(result))
        .Test();
        
    [Theory]
    [InlineData(Comparison.Greater)]
    [InlineData(Comparison.GreaterOrEqual)]
    [InlineData(Comparison.Less)]
    [InlineData(Comparison.LessOrEqual)]
    public void CanNotCompareDifferentCurrencies(Comparison comparison) => Bdd.Scenario<Context>()
        .Given(c => c.FirstValueWas(1.01m, Currency.PLN))
        .And(c => c.SecondValueWas(1.02m, Currency.EUR))
        .When(c => c.FirstValueIsComparedToSecondValue(comparison))
        .Then((c, r) => c.ErrorIsReturned(r))
        .Test();
        
    [Theory]
    [InlineData(1.01, Currency.PLN, "1.01 PLN")]
    [InlineData(-1.01, Currency.EUR, "-1.01 EUR")]
    [InlineData(1, Currency.PLN, "1.00 PLN")]
    public void ToStringProducesHumanReadableValue(decimal value, Currency currency, string result) => Bdd.Scenario<Context>()
        .Given(c => c.FirstValueWas(value, currency))
        .When(c => c.StringValueIsCreatedForFirstValue())
        .Then(c => c.ResultIs(result))
        .Test();

    public enum Comparison
    {
        Equal,
        NotEqual,
        Greater,
        GreaterOrEqual,
        Less,
        LessOrEqual,
    }
        
    private class Context
    {
        private Money _firstValue;
        private Money _secondValue;
        private int _intMultiplier;
        private decimal _decimalMultiplier;
        private Percentage _percentageMultiplier;
        private int _intDivider;
        private decimal _decimalDivider;
        private Money _moneyResult;
        private Percentage _percentageResult;
        private bool _boolResult;
        private string _stringResult;
            
        public void FirstValueWas(decimal value, Currency currency) => _firstValue = Money.Of(value, currency);

        public void SecondValueWas(decimal value, Currency currency) => _secondValue = Money.Of(value, currency);

        public void MultiplierWas(int multiplier) => _intMultiplier = multiplier;
        public void MultiplierWas(decimal multiplier) => _decimalMultiplier = multiplier;
        public void PercentageMultiplierWas(int multiplier) => _percentageMultiplier = Percentage.Of(multiplier);
            
        public void DividerWas(int divider) => _intDivider = divider;
        public void DividerWas(decimal divider) => _decimalDivider = divider;
            
        public void FirstValueIsAddedToSecondValue() => _moneyResult = _firstValue + _secondValue;
            
        public void FirstValueIsSubtractedFromSecondValue() => _moneyResult = _secondValue - _firstValue;
            
        public void FirstValueIsMultipliedByInt() => _moneyResult = _firstValue * _intMultiplier;
            
        public void FirstValueIsMultipliedByDecimal() => _moneyResult = _firstValue * _decimalMultiplier;
            
        public void FirstValueIsMultipliedByPercentage() => _moneyResult = _firstValue * _percentageMultiplier;
            
        public void FirstValueIsDividedByInt() => _moneyResult = _firstValue / _intDivider;
            
        public void FirstValueIsDividedByDecimal() => _moneyResult = _firstValue / _decimalDivider;
            
        public void FirstValueIsDividedBySecondValue() => _percentageResult = _firstValue / _secondValue;
            
        public void MaxValueIsCalculated() => _moneyResult = Money.Max(_firstValue, _secondValue);

        public void StringValueIsCreatedForFirstValue() => _stringResult = _firstValue.ToString();

        public void FirstValueIsComparedToSecondValue(Comparison comparison) =>
            _boolResult = comparison switch
            {
                Comparison.Equal => (_firstValue == _secondValue),
                Comparison.NotEqual => (_firstValue != _secondValue),
                Comparison.Greater => (_firstValue > _secondValue),
                Comparison.GreaterOrEqual => (_firstValue >= _secondValue),
                Comparison.Less => (_firstValue < _secondValue),
                Comparison.LessOrEqual => (_firstValue <= _secondValue),
                _ => throw new ArgumentOutOfRangeException(nameof(comparison))
            };

        public void ResultIs(decimal value, Currency currency) =>
            _moneyResult.Should().Be(Money.Of(value, currency));
            
        public void ResultIs(int value) => _percentageResult.Should().Be(Percentage.Of(value));
        public void ResultIs(bool result) => _boolResult.Should().Be(result);
            
        public void ResultIs(string result) => _stringResult.Should().Be(result);
            
        // ReSharper disable once MemberCanBeMadeStatic.Local
        public void ErrorIsReturned(Result result)
        {
            result.IsSuccessful.Should().BeFalse();
            result.Exception.Should().BeOfType<DomainError>();
        }
    }
}
```

## File: `Sources/Sales/Sales.FluentMigrations/Program.cs`
```csharp
﻿using FluentMigrator.Runner;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using NoesisVision.Annotations;

[assembly: ExcludeFromDocs]

var environmentName = Environment.GetEnvironmentVariable("ASPNETCORE_ENVIRONMENT");
var configuration = new ConfigurationBuilder()
    .AddJsonFile("appsettings.json", true, false)
    .AddJsonFile($"appsettings.{environmentName}.json", true, false)
    .AddEnvironmentVariables()
    .AddCommandLine(args)
    .Build();
var mainConnectionString = configuration.GetConnectionString("Crm");

var serviceProvider = new ServiceCollection()
    .AddFluentMigratorCore()
    .ConfigureRunner(rb => rb
        .AddPostgres()
        .WithGlobalConnectionString(mainConnectionString)
        .ScanIn(typeof(MyCompany.ECommerce.Sales.FluentMigrations.Program).Assembly).For.Migrations())
    .AddLogging(lb => lb.AddFluentMigratorConsole())
    .BuildServiceProvider(false);

using var scope = serviceProvider.CreateScope();
var runner = serviceProvider.GetRequiredService<IMigrationRunner>();
runner.MigrateUp();

namespace MyCompany.ECommerce.Sales.FluentMigrations
{
    public partial class Program { }
}
```

## File: `Sources/Sales/Sales.FluentMigrations/Sales.FluentMigrations.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <OutputType>Exe</OutputType>
        <TargetFramework>net8.0</TargetFramework>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
        <AssemblyName>MyCompany.ECommerce.Sales.FluentMigrations</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.Sales.FluentMigrations</RootNamespace>
    </PropertyGroup>

    <ItemGroup>
      <Reference Include="Microsoft.Extensions.Configuration">
        <HintPath>..\..\..\..\..\..\.nuget\packages\microsoft.extensions.configuration\6.0.1\lib\netstandard2.0\Microsoft.Extensions.Configuration.dll</HintPath>
      </Reference>
      <Reference Include="Microsoft.Extensions.DependencyInjection.Abstractions">
        <HintPath>..\..\..\..\..\..\.nuget\packages\microsoft.extensions.dependencyinjection.abstractions\7.0.0\lib\net6.0\Microsoft.Extensions.DependencyInjection.Abstractions.dll</HintPath>
      </Reference>
    </ItemGroup>

    <ItemGroup>
      <PackageReference Include="FluentMigrator.Runner" Version="5.2.0" />
      <PackageReference Include="FluentMigrator.Runner.Postgres" Version="5.2.0" />
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="Microsoft.Extensions.Configuration.CommandLine" Version="8.0.0" />
      <PackageReference Include="Microsoft.Extensions.Configuration.EnvironmentVariables" Version="8.0.0" />
      <PackageReference Include="Microsoft.Extensions.Configuration.Json" Version="8.0.0" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
      <PackageReference Include="Npgsql" Version="8.0.3" />
    </ItemGroup>

    <ItemGroup>
      <Content Include="appsettings.Development.json">
        <ExcludeFromSingleFile>true</ExcludeFromSingleFile>
        <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
        <CopyToPublishDirectory>PreserveNewest</CopyToPublishDirectory>
      </Content>
    </ItemGroup>

</Project>
```

## File: `Sources/Sales/Sales.FluentMigrations/appsettings.Development.json`
```json
{
  "ConnectionStrings": {    
    "Main": "Server=localhost;Port=5432;Database=Crm;User Id=postgres;Password=password;"
  }
}
```

## File: `Sources/Sales/Sales.FluentMigrations/Properties/launchSettings.json`
```json
{
  "$schema": "http://json.schemastore.org/launchsettings.json",
  "profiles": {
    "Dev": {
      "commandName": "Project",
      "environmentVariables": {
        "ASPNETCORE_ENVIRONMENT": "Development"
      }
    }
  }
}
```

## File: `Sources/Sales/Sales.FluentMigrations/Raw/2022/AddOrderTables.cs`
```csharp
using FluentMigrator;

namespace MyCompany.ECommerce.Sales.FluentMigrations.Raw._2022;

[Migration(2022_12_01)]
public class AddOrderTables : Migration
{
    private const string SalesSchema = "Sales_RawSql";
    
    public override void Up()
    {
        Create.Schema(SalesSchema);
        Create.Table("Orders")
            .InSchema(SalesSchema)
            .WithColumn("Id").AsGuid().PrimaryKey()
            .WithColumn("Version").AsInt32().NotNullable()
            .WithColumn("IsPlaced").AsBoolean().NotNullable();
        Create.Table("OrderItems")
            .InSchema(SalesSchema)
            .WithColumn("OrderId").AsGuid().NotNullable().ForeignKey("FK_OrderItems_OrderId_Orders_Id", SalesSchema, "Orders", "Id")
            .WithColumn("ProductId").AsGuid().NotNullable()
            .WithColumn("AmountUnit").AsString().NotNullable()
            .WithColumn("AmountValue").AsInt32().NotNullable()
            .WithColumn("PriceAgreementType").AsString().NotNullable()
            .WithColumn("PriceAgreementExpiresOn").AsDateTime().Nullable()
            .WithColumn("Price").AsDecimal(9, 2).Nullable()
            .WithColumn("Currency").AsString().Nullable();
        Create.PrimaryKey()
            .OnTable("OrderItems")
            .WithSchema(SalesSchema)
            .Columns("OrderId", "ProductId", "AmountUnit");
    }

    public override void Down() => throw new NotSupportedException();
}
```

## File: `Sources/Sales/Sales.IntegrationTests/Sales.IntegrationTests.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <IsPackable>false</IsPackable>
        <AssemblyName>MyCompany.ECommerce.Sales.IntegrationTests</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.Sales</RootNamespace>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
    </PropertyGroup>

    <ItemGroup>
        <PackageReference Include="FluentAssertions" Version="6.12.0" />
        <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
        <PackageReference Include="Microsoft.AspNetCore.Mvc.Testing" Version="8.0.5" />
        <PackageReference Include="Microsoft.NET.Test.Sdk" Version="17.9.0" />
        <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
        <PackageReference Include="xunit" Version="2.8.0" />
        <PackageReference Include="xunit.runner.visualstudio" Version="2.8.0">
          <PrivateAssets>all</PrivateAssets>
          <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
        </PackageReference>
        <PackageReference Include="coverlet.collector" Version="6.0.2">
          <PrivateAssets>all</PrivateAssets>
          <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
        </PackageReference>
    </ItemGroup>

    <ItemGroup>
      <ProjectReference Include="..\..\Monolith.Startup\Monolith.Startup.csproj" />
    </ItemGroup>

</Project>
```

## File: `Sources/Sales/Sales.IntegrationTests/Orders/OrderSqlRepositoryTests.cs`
```csharp
using FluentAssertions;
using Marten.Exceptions;
using Microsoft.AspNetCore.Mvc.Testing;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Orders.PriceChanges;
using MyCompany.ECommerce.Sales.Pricing;
using MyCompany.ECommerce.Sales.Products;
using MyCompany.ECommerce.Sales.Time;
using MyCompany.ECommerce.TechnicalStuff.Persistence;
using MyCompany.ECommerce.TechnicalStuff.Postgres;
using Xunit;

namespace MyCompany.ECommerce.Sales.Orders;

public class OrderSqlRepositoryTests : IClassFixture<WebApplicationFactory<Program>>
{
    private readonly PriceChangesPolicy _priceChangesPolicies = new FakePriceChangesPolicy();
    private readonly SystemClock _clock = new();
    private readonly IServiceProvider _serviceProvider;

    private string _repositoryImplementation;
        
    public OrderSqlRepositoryTests(WebApplicationFactory<Program> appFactory) => 
        _serviceProvider = appFactory.Services;
        
    [Theory]
    [InlineData(nameof(OrderSqlRepository.Raw))]
    [InlineData(nameof(OrderSqlRepository.EF))]
    [InlineData(nameof(OrderSqlRepository.Document))]
    [InlineData(nameof(OrderSqlRepository.EventsSourcing))]
    public async Task RestoredOrderIsEqualToOriginal(string repositoryImplementation)
    {
        _repositoryImplementation = repositoryImplementation;
        var (productAmount1, productAmount2, productAmount3) = CreateProductAmounts();
        var offer1 = CreateOfferFor(productAmount1, productAmount2);
        var offer2 = CreateOfferFor(productAmount1, productAmount2, productAmount3);
        var now = _clock.Now;

        var orderId = await TestRestoreForNewOrder();
        await TestRestoreAfter(orderId, order => order.Add(productAmount1));
        await TestRestoreAfter(orderId, order => order.Add(productAmount2));
        await TestRestoreAfter(orderId, order => order.ConfirmPrices(offer1, _priceChangesPolicies, now.AddDays(2)));
        await TestRestoreAfter(orderId, order => order.Add(productAmount3));
        await TestRestoreAfter(orderId, order => order.ConfirmPrices(offer2, _priceChangesPolicies, now.AddDays(3)));
        await TestRestoreAfter(orderId, order => order.Place(now.AddDays(2)));
        await TestRestoreForOrderFromOffer(offer2);
    }

    [Theory]
    [InlineData(nameof(OrderSqlRepository.Raw))]
    [InlineData(nameof(OrderSqlRepository.EF))]
    [InlineData(nameof(OrderSqlRepository.Document))]
    [InlineData(nameof(OrderSqlRepository.EventsSourcing))]
    public async Task CanNotSaveOrderIfVersionHasChangedInDb(string repositoryImplementation)
    {
        _repositoryImplementation = repositoryImplementation;
        using var scope0 = CreateScope();
        var order = scope0.OrderFactory.NewWith(Money.Of(decimal.MaxValue, Currency.PLN));
        await scope0.OrderRepository.Save(order);
        await scope0.TransactionProvider.CommitCurrentTransaction();
            
        using var scope1 = CreateScope();
        using var scope2 = CreateScope();
        var order1 = await scope1.OrderRepository.GetBy(order.Id);
        var order2 = await scope2.OrderRepository.GetBy(order.Id);
        order1.Add(ProductAmount.Of(ProductId.New(), Amount.Of(3, AmountUnit.Box)));
        order2.Add(ProductAmount.Of(ProductId.New(), Amount.Of(7, AmountUnit.Unit)));
        var action1 = async () =>
        {
            await scope1.OrderRepository.Save(order1);
            await scope1.TransactionProvider.CommitCurrentTransaction();
        };
        var action2 = async () =>
        {
            await scope2.OrderRepository.Save(order2);
            await scope2.TransactionProvider.CommitCurrentTransaction();
        };
        await action1.Should().NotThrowAsync();
        switch (repositoryImplementation)
        {
            case nameof(OrderSqlRepository.Raw):
                await action2.Should().ThrowExactlyAsync<OptimisticLockException>();
                break;
            case nameof(OrderSqlRepository.EF):
                await action2.Should().ThrowExactlyAsync<DbUpdateConcurrencyException>();
                break;
            case nameof(OrderSqlRepository.Document):
                await action2.Should().ThrowExactlyAsync<ConcurrencyException>();
                break;
            case nameof(OrderSqlRepository.EventsSourcing):
                await action2.Should().ThrowExactlyAsync<EventStreamUnexpectedMaxEventIdException>();
                break;
            default:
                throw new ArgumentOutOfRangeException(nameof(_repositoryImplementation),
                    repositoryImplementation,
                    null);
        }
    }

    private static (ProductAmount, ProductAmount, ProductAmount) CreateProductAmounts()
    {
        var product1 = ProductId.New();
        var product2 = ProductId.New();
        var productAmount1 = ProductAmount.Of(
            product1,
            Amount.Of(3, AmountUnit.Palette));
        var productAmount2 = ProductAmount.Of(
            product2,
            Amount.Of(5, AmountUnit.Box));
        var productAmount3 = ProductAmount.Of(
            product2,
            Amount.Of(7, AmountUnit.Unit));
        return (productAmount1, productAmount2, productAmount3);
    }

    private static Offer CreateOfferFor(params ProductAmount[] productAmounts) => Offer.FromQuotes(
        Currency.PLN,
        productAmounts.Select((productAmount, index) => Quote.For(
            productAmount,
            Money.Of((index + 1) * 1.23m, Currency.PLN))));

    private async Task<OrderId> TestRestoreForNewOrder()
    {
        using var scope = CreateScope();
        var order = scope.OrderFactory.NewWith(Money.Of(decimal.MaxValue, Currency.PLN));
        await scope.OrderRepository.Save(order);
        await scope.TransactionProvider.CommitCurrentTransaction();
        await TestRestore(order);
        return order.Id;
    }

    private async Task TestRestoreForOrderFromOffer(Offer offer)
    {
        using var scope = CreateScope();
        var order = scope.OrderFactory.ImmediatelyPlacedBasedOn(offer);
        await scope.OrderRepository.Save(order);
        await scope.TransactionProvider.CommitCurrentTransaction();
        await TestRestore(order);
    }

    private async Task TestRestoreAfter(OrderId orderId, Action<Order> action)
    {
        using var scope = CreateScope();
        var order = await scope.OrderRepository.GetBy(orderId);
        action(order);
        await scope.OrderRepository.Save(order);
        await scope.TransactionProvider.CommitCurrentTransaction();
        await TestRestore(order);
    }

    private async Task TestRestore(Order savedOrder)
    {
        using var scope = CreateScope();
        var restoredOrder = await scope.OrderRepository.GetBy(savedOrder.Id);
        restoredOrder.Should().BeEquivalentTo(savedOrder);
    }

    private Scope CreateScope() => new(_serviceProvider, _repositoryImplementation);

    private class Scope : IDisposable
    {
        private readonly IServiceScope _scope;
        public PostgresTransactionProvider TransactionProvider { get; }
        public Order.Repository OrderRepository { get; }
        public Order.Factory OrderFactory { get; }
            
        public Scope(IServiceProvider serviceProvider, string repositoryImplementation)
        {
            _scope = serviceProvider.CreateScope();
            TransactionProvider = _scope.ServiceProvider.GetRequiredService<PostgresTransactionProvider>();
            OrderRepository = CreateRepository(_scope, repositoryImplementation);
            OrderFactory = CreateFactory(_scope, repositoryImplementation);
        }
            
        public void Dispose()
        {
            TransactionProvider.Dispose();
            _scope.Dispose();
        }

        private static Order.Repository CreateRepository(IServiceScope scope, string repositoryImplementation) =>
            repositoryImplementation switch
            {
                nameof(OrderSqlRepository.Raw) => scope.ServiceProvider
                    .GetRequiredService<OrderSqlRepository.Raw>(),
                nameof(OrderSqlRepository.EF) => scope.ServiceProvider
                    .GetRequiredService<OrderSqlRepository.EF>(),
                nameof(OrderSqlRepository.Document) => scope.ServiceProvider
                    .GetRequiredService<OrderSqlRepository.Document>(),
                nameof(OrderSqlRepository.EventsSourcing) => scope.ServiceProvider
                    .GetRequiredService<OrderSqlRepository.EventsSourcing>(),
                _ => throw new ArgumentOutOfRangeException(nameof(_repositoryImplementation),
                    repositoryImplementation,
                    null)
            };
            
        private static Order.Factory CreateFactory(IServiceScope scope, string repositoryImplementation) =>
            repositoryImplementation switch
            {
                nameof(OrderSqlRepository.Raw) => scope.ServiceProvider
                    .GetRequiredService<OrderSqlRepository.Raw>(),
                nameof(OrderSqlRepository.EF) => scope.ServiceProvider
                    .GetRequiredService<OrderSqlRepository.EF>(),
                nameof(OrderSqlRepository.Document) => scope.ServiceProvider
                    .GetRequiredService<OrderSqlRepository.Document>(),
                nameof(OrderSqlRepository.EventsSourcing) => scope.ServiceProvider
                    .GetRequiredService<OrderSqlRepository.EventsSourcing>(),
                _ => throw new ArgumentOutOfRangeException(nameof(_repositoryImplementation),
                    repositoryImplementation,
                    null)
            };
    }
}
```

## File: `Sources/Sales/Sales.IntegrationTests/Orders/PriceChanges/FakePriceChangesPolicy.cs`
```csharp
using System.Collections.Immutable;
using MyCompany.ECommerce.Sales.Pricing;

namespace MyCompany.ECommerce.Sales.Orders.PriceChanges;

public class FakePriceChangesPolicy : PriceChangesPolicy
{
    public bool CanChangePrices(ImmutableArray<Quote> oldQuotes, ImmutableArray<Quote> newQuotes) => true;
}
```

## File: `Sources/Sales/Sales.ProcessModel/Actors.cs`
```csharp
namespace MyCompany.ECommerce.Sales;

public static class Actors
{
    public const string RetailClient = nameof(RetailClient);
    public const string WholesaleClient = nameof(WholesaleClient);
}
```

## File: `Sources/Sales/Sales.ProcessModel/OrderEvent.cs`
```csharp
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Sales;

public interface OrderEvent : DomainEvent
{
    public Guid OrderId { get; }
}
```

## File: `Sources/Sales/Sales.ProcessModel/OrderEventsOutbox.cs`
```csharp
namespace MyCompany.ECommerce.Sales;

public interface OrderEventsOutbox
{
    public void Add(OrderEvent orderEvent);
}
```

## File: `Sources/Sales/Sales.ProcessModel/SaleProcess.cs`
```csharp
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.Sales;

[Process(Name, ApplyOnNamespace = true)]
public static class SaleProcess
{
    public const string Name = "Sale";
}
```

## File: `Sources/Sales/Sales.ProcessModel/Sales.ProcessModel.csproj`
```
﻿<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <AssemblyName>MyCompany.ECommerce.Sales.ProcessModel</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.Sales</RootNamespace>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
    </PropertyGroup>

    <ItemGroup>
      <ProjectReference Include="..\..\TechnicalStuff\TechnicalStuff.ProcessModel\TechnicalStuff.ProcessModel.csproj" />
      <ProjectReference Include="..\Sales.DeepModel\Sales.DeepModel.csproj" />
    </ItemGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
      <PackageReference Include="TaskTupleAwaiter" Version="2.1.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/Sales/Sales.ProcessModel/SalesCrudOperations.cs`
```csharp
using MyCompany.ECommerce.TechnicalStuff.Crud.Operations;

namespace MyCompany.ECommerce.Sales;

public interface SalesCrudOperations : CrudOperations { }
```

## File: `Sources/Sales/Sales.ProcessModel/SalesProcessModelLayerInfo.cs`
```csharp
using System.Reflection;
using NoesisVision.Annotations.Domain;
using NoesisVision.Annotations.Technology.CleanArchitecture;

[assembly: UseCasesLayer]
[assembly: DomainModel]

namespace MyCompany.ECommerce.Sales;

public static class SalesProcessModelLayerInfo
{
    public static Assembly Assembly => typeof(SalesProcessModelLayerInfo).Assembly;
}
```

## File: `Sources/Sales/Sales.ProcessModel/Fulfillment/FulfillmentProcess.cs`
```csharp
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.Sales.Fulfillment;

[Process(Name, ApplyOnNamespace = true)]
public static class FulfillmentProcess
{
    public const string Name = "Order fulfillment";
}
```

## File: `Sources/Sales/Sales.ProcessModel/Fulfillment/OrderPlacedHandler.cs`
```csharp
using JetBrains.Annotations;
using MyCompany.ECommerce.Sales.OnlineOrdering;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.Sales.Fulfillment;

using OnlineOrderPlaced = OrderPlaced;
using WholesaleOrderPlaced = WholesaleOrdering.OrderPlaced;

[UsedImplicitly]
public class OrderPlacedHandler : DomainEventHandler<OnlineOrderPlaced>, DomainEventHandler<WholesaleOrderPlaced>
{
    public Task Handle(Message message) => message switch
    {
        OnlineOrderPlaced onlineOrderPlaced => Handle(onlineOrderPlaced),
        WholesaleOrderPlaced wholesaleOrderPlaced => Handle(wholesaleOrderPlaced),
        _ => throw new ArgumentOutOfRangeException(nameof(message), message, null)
    };

    [EntryPoint(nameof(OnlineOrderPlaced), Process = FulfillmentProcess.Name)]
    public Task Handle(OnlineOrderPlaced domainEvent)
    {
        throw new NotImplementedException();
    }

    [EntryPoint(nameof(WholesaleOrderPlaced), Process = FulfillmentProcess.Name)]
    public Task Handle(WholesaleOrderPlaced domainEvent)
    {
        throw new NotImplementedException();
    }
}
```

## File: `Sources/Sales/Sales.ProcessModel/Fulfillment/RequestOrderAcceptance.cs`
```csharp
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Sales.Fulfillment;

public readonly struct RequestOrderAcceptance : Command
{
    public Guid OrderId { get; }

    public RequestOrderAcceptance(Guid orderId) => OrderId = orderId;
}
```

## File: `Sources/Sales/Sales.ProcessModel/Integrations/Payments/PaymentRequestFulfilled.cs`
```csharp
namespace MyCompany.ECommerce.Sales.Integrations.Payments;

public class PaymentRequestFulfilled : OrderEvent
{
    public Guid OrderId { get; }
}
```

## File: `Sources/Sales/Sales.ProcessModel/Integrations/Payments/PaymentsModule.cs`
```csharp
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Orders;

namespace MyCompany.ECommerce.Sales.Integrations.Payments;

public interface PaymentsModule
{
    void AddPaymentRequestFor(OrderId orderId, Money amount);
}
```

## File: `Sources/Sales/Sales.ProcessModel/Integrations/ProductsDelivery/ProductsDeliveryModule.cs`
```csharp
using MyCompany.ECommerce.Sales.Orders;

namespace MyCompany.ECommerce.Sales.Integrations.ProductsDelivery;

public interface ProductsDeliveryModule
{
    void AddDeliveryRequestFor(AllOrderDetails orderDetails);
}
```

## File: `Sources/Sales/Sales.ProcessModel/OnlineOrdering/CartItemDto.cs`
```csharp
namespace MyCompany.ECommerce.Sales.OnlineOrdering;

public readonly struct CartItemDto(Guid productId, int amount)
{
    public Guid ProductId { get; } = productId;
    public int Amount { get; } = amount;
}
```

## File: `Sources/Sales/Sales.ProcessModel/OnlineOrdering/CartPriced.cs`
```csharp
using System.Collections.Immutable;

namespace MyCompany.ECommerce.Sales.OnlineOrdering;

public readonly struct CartPriced(DateTime pricedOn, Guid clientId, string currency, ImmutableArray<QuoteDto> quotes)
{
    public DateTime PricedOn { get; } = pricedOn;
    public Guid ClientId { get; } = clientId;
    public string Currency { get; } = currency;
    public ImmutableArray<QuoteDto> Quotes { get; } = quotes;
}
```

## File: `Sources/Sales/Sales.ProcessModel/OnlineOrdering/DtoMapping.cs`
```csharp
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Pricing;
using MyCompany.ECommerce.Sales.Products;
using MyCompany.ECommerce.TechnicalStuff;

namespace MyCompany.ECommerce.Sales.OnlineOrdering;

public static class DtoMapping
{
    public static ProductAmount ToDomainModel(this CartItemDto cartItemDto) => ProductAmount.Of(
        ProductId.From(cartItemDto.ProductId),
        cartItemDto.Amount,
        AmountUnit.Unit);
        
    public static Quote ToDomainModel(this QuoteDto quoteDto) => Quote.For(
        ProductAmount.Of(
            ProductId.From(quoteDto.ProductId),
            quoteDto.Amount,
            AmountUnit.Unit),
        Money.Of(
            quoteDto.Price, 
            quoteDto.CurrencyCode.ToDomainModel<Currency>()));
        
    public static QuoteDto ToDto(this Quote quote) => new(
        quote.ProductAmount.ProductId.Value,
        quote.ProductAmount.Amount.Value,
        quote.Price.Value,
        quote.Price.Currency.ToCode());
}
```

## File: `Sources/Sales/Sales.ProcessModel/OnlineOrdering/OnlineOrderingProcess.cs`
```csharp
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.Sales.OnlineOrdering;

[Process(Name, ApplyOnNamespace = true)]
public class OnlineOrderingProcess
{
    public const string Name = "Online ordering";
}
```

## File: `Sources/Sales/Sales.ProcessModel/OnlineOrdering/OrderDetails.cs`
```csharp
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.Sales.OnlineOrdering;

[ReadModel]
public class OrderDetails
{
    // TODO: subset of data from AllAOderDetails
}
```

## File: `Sources/Sales/Sales.ProcessModel/OnlineOrdering/OrderDetailsFinder.cs`
```csharp
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.OnlineOrdering;

[DddRepository]
public interface OrderDetailsFinder
{
    Task<OrderDetails> GetBy(Guid id);
}
```

## File: `Sources/Sales/Sales.ProcessModel/OnlineOrdering/OrderPlaced.cs`
```csharp
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.Sales.OnlineOrdering;

[Event]
public class OrderPlaced(Guid orderId, Guid clientId, DateTime placedOn) : OrderEvent
{
    public Guid OrderId { get; } = orderId;
    public Guid ClientId { get; } = clientId;
    public DateTime PlacedOn { get; } = placedOn;
}
```

## File: `Sources/Sales/Sales.ProcessModel/OnlineOrdering/PlaceOrder.cs`
```csharp
using System.Collections.Immutable;
using MyCompany.ECommerce.Sales.Orders;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.Sales.OnlineOrdering;

[PublicContract]
[Command]
public readonly struct PlaceOrder(
    Guid clientId,
    string currencyCode,
    ImmutableArray<QuoteDto> quotes,
    InvoicingDetails invoicingDetails)
    : Command
{
    public Guid ClientId { get; } = clientId;
    public string CurrencyCode { get; } = currencyCode;
    public ImmutableArray<QuoteDto> Quotes { get; } = quotes;
    public InvoicingDetails InvoicingDetails { get; } = invoicingDetails;
}
```

## File: `Sources/Sales/Sales.ProcessModel/OnlineOrdering/PlaceOrderHandler.cs`
```csharp
using JetBrains.Annotations;
using MyCompany.ECommerce.Sales.Clients;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Orders;
using MyCompany.ECommerce.Sales.Pricing;
using MyCompany.ECommerce.Sales.SalesChannels;
using MyCompany.ECommerce.Sales.Time;
using MyCompany.ECommerce.TechnicalStuff;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;
using NoesisVision.Annotations.Domain;
using NoesisVision.Annotations.People;

namespace MyCompany.ECommerce.Sales.OnlineOrdering;

[UsedImplicitly]
public class PlaceOrderHandler(
    CalculatePrices calculatePrices,
    Order.Repository repository,
    Order.Factory factory,
    SalesCrudOperations crudOperations,
    OrderEventsOutbox eventsOutbox,
    Clock clock)
    : CommandHandler<PlaceOrder, OrderPlaced>
{
    [PublicContract]
    [Actor(Actors.RetailClient)]
    public async Task<OrderPlaced> Handle(PlaceOrder command)
    {
            var (clientId, offer) = CreateDomainModelFrom(command);
            var currentOffer = await calculatePrices.For(clientId,
                SalesChannel.OnlineSale,
                offer.ProductAmounts,
                offer.Currency);
            if (!offer.Equals(currentOffer)) throw new DomainError();
            var order = factory.ImmediatelyPlacedBasedOn(offer);
            var orderHeader = new OrderHeader
            {
                Id = order.Id.Value, 
                ClientId = clientId.Value, 
                InvoicingDetails = command.InvoicingDetails
            };
            await repository.Save(order);
            await crudOperations.Create(orderHeader);
            var orderPlaced = CreateEventFrom(clientId, order, clock.Now);
            eventsOutbox.Add(orderPlaced);
            return orderPlaced;
        }

    private static (ClientId, Offer) CreateDomainModelFrom(PlaceOrder command) => (
        ClientId.From(command.ClientId),
        Offer.FromQuotes(command.CurrencyCode.ToDomainModel<Currency>(),
            command.Quotes.Select(quote => quote.ToDomainModel())));

    private static OrderPlaced CreateEventFrom(ClientId clientId, Order order, DateTime placedOn) =>
        new(order.Id.Value, clientId.Value, placedOn);
}
```

## File: `Sources/Sales/Sales.ProcessModel/OnlineOrdering/PriceCart.cs`
```csharp
using System.Collections.Immutable;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Sales.OnlineOrdering;

public readonly struct PriceCart(Guid clientId, string currency, ImmutableArray<CartItemDto> cartItems)
    : Command
{
    public Guid ClientId { get; } = clientId;
    public string Currency { get; } = currency;
    public ImmutableArray<CartItemDto> CartItems { get; } = cartItems;
}
```

## File: `Sources/Sales/Sales.ProcessModel/OnlineOrdering/PriceCartHandler.cs`
```csharp
using System.Collections.Immutable;
using JetBrains.Annotations;
using MyCompany.ECommerce.Sales.Clients;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Pricing;
using MyCompany.ECommerce.Sales.Products;
using MyCompany.ECommerce.Sales.SalesChannels;
using MyCompany.ECommerce.TechnicalStuff;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;
using NoesisVision.Annotations.People;

namespace MyCompany.ECommerce.Sales.OnlineOrdering;

[UsedImplicitly]
public class PriceCartHandler(CalculatePrices calculatePrices) : CommandHandler<PriceCart, CartPriced>
{
    [Actor(Actors.RetailClient)]
    public async Task<CartPriced> Handle(PriceCart command)
    {
            var (clientId, currency, productAmounts) = CreateDomainModelFrom(command);
            var offer = await calculatePrices.For(clientId, SalesChannel.OnlineSale, productAmounts, currency);
            var cartPriced = CreateEventFrom(clientId, offer);
            return cartPriced;
        }

    private static (ClientId, Currency, ImmutableArray<ProductAmount>) CreateDomainModelFrom(
        PriceCart command) => (
        ClientId.From(command.ClientId),
        command.Currency.ToDomainModel<Currency>(),
        command.CartItems
            .Select(cartItem => cartItem.ToDomainModel())
            .ToImmutableArray());

    private static CartPriced CreateEventFrom(ClientId clientId, Offer offer) => new(
        DateTime.UtcNow,
        clientId.Value,
        offer.Currency.ToCode(),
        offer.Quotes
            .Select(quote => quote.ToDto())
            .ToImmutableArray());
}
```

## File: `Sources/Sales/Sales.ProcessModel/OnlineOrdering/QuoteDto.cs`
```csharp
namespace MyCompany.ECommerce.Sales.OnlineOrdering;

public readonly struct QuoteDto(Guid productId, int amount, decimal price, string currencyCode)
{
    public Guid ProductId { get; } = productId;
    public int Amount { get; } = amount;
    public decimal Price { get; } = price;
    public string CurrencyCode { get; } = currencyCode;
}
```

## File: `Sources/Sales/Sales.ProcessModel/WholesaleOrdering/AddToOrder.cs`
```csharp
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

public readonly struct AddToOrder(Guid orderId, Guid productId, int amount, string unitCode)
    : Command
{
    public Guid OrderId { get; } = orderId;
    public Guid ProductId { get; } = productId;
    public int Amount { get; } = amount;
    public string UnitCode { get; } = unitCode;
}
```

## File: `Sources/Sales/Sales.ProcessModel/WholesaleOrdering/AddToOrderHandler.cs`
```csharp
using JetBrains.Annotations;
using MyCompany.ECommerce.Sales.Orders;
using MyCompany.ECommerce.Sales.Products;
using MyCompany.ECommerce.TechnicalStuff;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;
using NoesisVision.Annotations.People;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

[UsedImplicitly]
public class AddToOrderHandler(Order.Repository orders, OrderEventsOutbox eventsOutbox)
    : CommandHandler<AddToOrder, AddedToOrder>
{
    [Actor(Actors.WholesaleClient)]
    public async Task<AddedToOrder> Handle(AddToOrder command)
    {
            var (orderId, productAmount) = CreateDomainModelFrom(command);
            var order = await orders.GetBy(orderId);
            order.Add(productAmount);
            await orders.Save(order);
            // var allOrderDetails = _readModels.Get(orderId)
            // allOrderDetails.Apply(order.NewEvents)
            // albo
            // allOrderDetails.AddProductAmount(productAmount)
            // _readModels.Save(allOrderDetails)
            var addedToOrder = CreateEventFrom(orderId, productAmount);
            eventsOutbox.Add(addedToOrder);
            return addedToOrder;
        }

    private static (OrderId, ProductAmount) CreateDomainModelFrom(AddToOrder command) => (
        OrderId.From(command.OrderId),
        ProductAmount.Of(
            ProductId.From(command.ProductId),
            command.Amount,
            command.UnitCode.ToDomainModel<AmountUnit>()));

    private static AddedToOrder CreateEventFrom(OrderId orderId, ProductAmount productAmount) =>
        new(orderId.Value,
            productAmount.ProductId.Value,
            productAmount.Amount.Value,
            productAmount.Amount.Unit.ToCode());
}
```

## File: `Sources/Sales/Sales.ProcessModel/WholesaleOrdering/AddedToOrder.cs`
```csharp
namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

public class AddedToOrder(Guid orderId, Guid productId, int amount, string unitCode)
    : OrderEvent
{
    public Guid OrderId { get; } = orderId;
    public Guid ProductId { get; } = productId;
    public int Amount { get; } = amount;
    public string UnitCode { get; } = unitCode;
}
```

## File: `Sources/Sales/Sales.ProcessModel/WholesaleOrdering/ConfirmOffer.cs`
```csharp
using System.Collections.Immutable;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

public readonly struct ConfirmOffer(Guid orderId, string currencyCode, ImmutableArray<QuoteDto> quotes)
    : Command
{
    public Guid OrderId { get; } = orderId;
    public string CurrencyCode { get; } = currencyCode;
    public ImmutableArray<QuoteDto> Quotes { get; } = quotes;
}
```

## File: `Sources/Sales/Sales.ProcessModel/WholesaleOrdering/ConfirmOfferHandler.cs`
```csharp
using System.Collections.Immutable;
using JetBrains.Annotations;
using MyCompany.ECommerce.Sales.Clients;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Orders;
using MyCompany.ECommerce.Sales.Orders.PriceChanges;
using MyCompany.ECommerce.Sales.Pricing;
using MyCompany.ECommerce.Sales.SalesChannels;
using MyCompany.ECommerce.Sales.Time;
using MyCompany.ECommerce.TechnicalStuff;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;
using NoesisVision.Annotations.People;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

[UsedImplicitly]
public class ConfirmOfferHandler(
    Order.Repository orders,
    SalesCrudOperations crudOperations,
    CalculatePrices calculatePrices,
    PriceChangesPolicies priceChangesPolicies,
    OrderEventsOutbox eventsOutbox,
    Clock clock)
    : CommandHandler<ConfirmOffer, OfferConfirmed>
{
    private readonly TimeSpan _offerExpirationTime = TimeSpan.FromHours(24);

    [Actor(Actors.WholesaleClient)]
    public async Task<OfferConfirmed> Handle(ConfirmOffer command)
    {
            var (orderId, offer) = CreateDomainModelFrom(command);
            var order = await orders.GetBy(orderId);
            var clientId = await GetClient(orderId);
            var currentOffer = await calculatePrices.For(clientId,
                SalesChannel.Wholesale,
                offer.ProductAmounts,
                offer.Currency);
            if (!offer.Equals(currentOffer))
                throw new DomainError();
            var priceChangesPolicy = await priceChangesPolicies.ChooseFor(clientId);
            var now = clock.Now;
            order.ConfirmPrices(offer, priceChangesPolicy, now + _offerExpirationTime);
            await orders.Save(order);
            var offerConfirmed = CreateEventFrom(orderId, offer);
            eventsOutbox.Add(offerConfirmed);
            return offerConfirmed;
        }

    private static (OrderId, Offer) CreateDomainModelFrom(ConfirmOffer command) => (
        OrderId.From(command.OrderId),
        Offer.FromQuotes(command.CurrencyCode.ToDomainModel<Currency>(),
            command.Quotes.Select(quote => quote.ToDomainModel())));

    private async Task<ClientId> GetClient(OrderId orderId)
    {
            var orderHeader = await crudOperations.Read<OrderHeader>(orderId.Value);
            return ClientId.From(orderHeader.ClientId);
        }

    private static OfferConfirmed CreateEventFrom(OrderId orderId, Offer offer) => new(
        orderId.Value, offer.Quotes
            .Select(quote => quote.ToDto())
            .ToImmutableArray());
}
```

## File: `Sources/Sales/Sales.ProcessModel/WholesaleOrdering/CreateOrder.cs`
```csharp
using MyCompany.ECommerce.Sales.Clients;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

public readonly struct CreateOrder(ClientId clientId) : Command
{
    public ClientId ClientId { get; } = clientId;
}
```

## File: `Sources/Sales/Sales.ProcessModel/WholesaleOrdering/CreateOrderHandler.cs`
```csharp
using JetBrains.Annotations;
using MyCompany.ECommerce.Sales.Clients;
using MyCompany.ECommerce.Sales.Orders;
using MyCompany.ECommerce.Sales.SalesChannels;
using MyCompany.ECommerce.TechnicalStuff;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;
using NoesisVision.Annotations.People;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

[UsedImplicitly]
public class CreateOrderHandler(
    Order.Repository orders,
    SalesCrudOperations crudOperations,
    OrderEventsOutbox eventsOutbox)
    : CommandHandler<CreateOrder, OrderCreated>
{
    private readonly Order.Factory _orderFactory;

    [Actor(Actors.WholesaleClient)]
    public async Task<OrderCreated> Handle(CreateOrder command)
    {
            var clientId = command.ClientId;
            var order = await _orderFactory.NewWithMaxTotalCostFor(clientId);
            var orderHeader = new OrderHeader {Id = order.Id.Value, ClientId = clientId.Value};
            await orders.Save(order);
            await crudOperations.Create(orderHeader);
            var orderCreated = CreateEventFrom(order, clientId);
            eventsOutbox.Add(orderCreated);
            return orderCreated;
        }

    private static OrderCreated CreateEventFrom(Order order, ClientId clientId) =>
        new(order.Id.Value, clientId.Value, SalesChannel.Wholesale.ToCode());
}
```

## File: `Sources/Sales/Sales.ProcessModel/WholesaleOrdering/DtoMapping.cs`
```csharp
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Pricing;
using MyCompany.ECommerce.Sales.Products;
using MyCompany.ECommerce.TechnicalStuff;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

internal static class DtoExtensions
{
    internal static Quote ToDomainModel(this QuoteDto quoteDto) => Quote.For(
        ProductAmount.Of(
            ProductId.From(quoteDto.ProductId),
            quoteDto.Amount,
            quoteDto.UnitCode.ToDomainModel<AmountUnit>()),
        Money.Of(
            quoteDto.Price, 
            quoteDto.CurrencyCode.ToDomainModel<Currency>()));

    internal static QuoteDto ToDto(this Quote quote) => new(
        quote.ProductAmount.ProductId.Value,
        quote.ProductAmount.Amount.Value,
        quote.ProductAmount.Amount.Unit.ToCode(),
        quote.Price.Value,
        quote.Price.Currency.ToCode()); 
}
```

## File: `Sources/Sales/Sales.ProcessModel/WholesaleOrdering/GetOffer.cs`
```csharp
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

public readonly struct GetOffer(Guid orderId, string currencyCode) : Command
{
    public Guid OrderId { get; } = orderId;
    public string CurrencyCode { get; } = currencyCode;
}
```

## File: `Sources/Sales/Sales.ProcessModel/WholesaleOrdering/GetOfferHandler.cs`
```csharp
using System.Collections.Immutable;
using JetBrains.Annotations;
using MyCompany.ECommerce.Sales.Clients;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Orders;
using MyCompany.ECommerce.Sales.Pricing;
using MyCompany.ECommerce.Sales.SalesChannels;
using MyCompany.ECommerce.TechnicalStuff;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;
using NoesisVision.Annotations.People;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

[UsedImplicitly]
public class GetOfferHandler(
    Order.Repository orders,
    SalesCrudOperations crudOperations,
    CalculatePrices calculatePrices)
    : CommandHandler<GetOffer, OfferCalculated>
{
    [Actor(Actors.WholesaleClient)]
    public async Task<OfferCalculated> Handle(GetOffer command)
    {
            var (orderId, currency) = CreateDomainModelFrom(command);
            var order = await orders.GetBy(orderId);
            var clientId = await GetClient(orderId);
            var offer = await calculatePrices.For(clientId, SalesChannel.Wholesale, order.ProductAmounts, currency);
            return CreateEventFrom(orderId, offer);
        }

    private static (OrderId, Currency) CreateDomainModelFrom(GetOffer command) => (
        OrderId.From(command.OrderId), command.CurrencyCode.ToDomainModel<Currency>());

    private async Task<ClientId> GetClient(OrderId orderId)
    {
            var orderHeader = await crudOperations.Read<OrderHeader>(orderId.Value);
            return ClientId.From(orderHeader.ClientId);
        }

    private static OfferCalculated CreateEventFrom(OrderId orderId, Offer offer) => new(
        orderId.Value, offer.Quotes
            .Select(quote => quote.ToDto())
            .ToImmutableArray());
}
```

## File: `Sources/Sales/Sales.ProcessModel/WholesaleOrdering/GetQuickQuote.cs`
```csharp
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

public readonly struct GetQuickQuote(Guid clientId, Guid productId, int amount, string unitCode, string currencyCode)
    : Command
{
    public Guid ClientId { get; } = clientId;
    public Guid ProductId { get; } = productId;
    public int Amount { get; } = amount;
    public string UnitCode { get; } = unitCode;
    public string CurrencyCode { get; } = currencyCode;
}
```

## File: `Sources/Sales/Sales.ProcessModel/WholesaleOrdering/GetQuickQuoteHandler.cs`
```csharp
using JetBrains.Annotations;
using MyCompany.ECommerce.Sales.Clients;
using MyCompany.ECommerce.Sales.Commons;
using MyCompany.ECommerce.Sales.Pricing;
using MyCompany.ECommerce.Sales.Products;
using MyCompany.ECommerce.Sales.SalesChannels;
using MyCompany.ECommerce.TechnicalStuff;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;
using NoesisVision.Annotations.People;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

[UsedImplicitly]
public class GetQuickQuoteHandler(CalculatePrices calculatePrices) : CommandHandler<GetQuickQuote, QuickQuoteCalculated>
{
    [Actor(Actors.WholesaleClient)]
    public async Task<QuickQuoteCalculated> Handle(GetQuickQuote command)
    {
            var (clientId, productAmount, currency) = CreateDomainModelFrom(command);
            var quote = await calculatePrices.For(clientId, SalesChannel.Wholesale, productAmount, currency);
            return CreateEventFrom(clientId, quote);
        }

    private static (ClientId, ProductAmount, Currency) CreateDomainModelFrom(GetQuickQuote command) => (
        ClientId.From(command.ClientId),
        ProductAmount.Of(
            ProductId.From(command.ProductId),
            command.Amount,
            command.UnitCode.ToDomainModel<AmountUnit>()),
        command.CurrencyCode.ToDomainModel<Currency>());

    private static QuickQuoteCalculated CreateEventFrom(ClientId clientId, Quote quote) =>
        new(clientId.Value, quote.ToDto());
}
```

## File: `Sources/Sales/Sales.ProcessModel/WholesaleOrdering/OfferCalculated.cs`
```csharp
using System.Collections.Immutable;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

public class OfferCalculated(Guid orderId, ImmutableArray<QuoteDto> quotes)
{
    public Guid OrderId { get; } = orderId;
    public ImmutableArray<QuoteDto> Quotes { get; } = quotes;
}
```

## File: `Sources/Sales/Sales.ProcessModel/WholesaleOrdering/OfferConfirmed.cs`
```csharp
using System.Collections.Immutable;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

public class OfferConfirmed(Guid orderId, ImmutableArray<QuoteDto> quotes) : OrderEvent
{
    public Guid OrderId { get; } = orderId;
    public ImmutableArray<QuoteDto> Quotes { get; } = quotes;
}
```

## File: `Sources/Sales/Sales.ProcessModel/WholesaleOrdering/OrderCreated.cs`
```csharp
namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

public class OrderCreated(Guid orderId, Guid clientId, string salesChannel) : OrderEvent
{
    public Guid OrderId { get; } = orderId;
    public Guid ClientId { get; } = clientId;
    public string SalesChannel { get; } = salesChannel;
}
```

## File: `Sources/Sales/Sales.ProcessModel/WholesaleOrdering/OrderDetailsFinder.cs`
```csharp
using MyCompany.ECommerce.Sales.Orders;
using NoesisVision.Annotations.Domain.DDD;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

[DddRepository]
public interface OrderDetailsFinder
{
    Task<AllOrderDetails> GetBy(Guid id);
}
```

## File: `Sources/Sales/Sales.ProcessModel/WholesaleOrdering/OrderPlaced.cs`
```csharp
namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

public class OrderPlaced(Guid orderId, Guid clientId, DateTime placedOn) : OrderEvent
{
    public Guid OrderId { get; } = orderId;
    public Guid ClientId { get; } = clientId;
    public DateTime PlacedOn { get; } = placedOn;
}
```

## File: `Sources/Sales/Sales.ProcessModel/WholesaleOrdering/PlaceOrder.cs`
```csharp
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

public readonly struct PlaceOrder(Guid orderId) : Command
{
    public Guid OrderId { get; } = orderId;
}
```

## File: `Sources/Sales/Sales.ProcessModel/WholesaleOrdering/PlaceOrderHandler.cs`
```csharp
using JetBrains.Annotations;
using MyCompany.ECommerce.Sales.Orders;
using MyCompany.ECommerce.Sales.Time;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;
using NoesisVision.Annotations.People;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

[UsedImplicitly]
public class PlaceOrderHandler(
    Order.Repository orders,
    SalesCrudOperations crudOperations,
    Clock clock,
    OrderEventsOutbox eventsOutbox)
    : CommandHandler<PlaceOrder, OrderPlaced>
{
    [Actor(Actors.WholesaleClient)]
    public async Task<OrderPlaced> Handle(PlaceOrder command)
    {
            var orderId = CreateDomainModelFrom(command);
            var order = await orders.GetBy(orderId);
            var now = clock.Now;
            order.Place(now);
            await orders.Save(order);
            var orderPlaced = await CreateEventFrom(order, now);
            eventsOutbox.Add(orderPlaced);
            return orderPlaced;
        }
        
    private static OrderId CreateDomainModelFrom(PlaceOrder command) => OrderId.From(command.OrderId);

    private async Task<OrderPlaced> CreateEventFrom(Order order, DateTime placedOn)
    {
            var orderHeader = await crudOperations.Read<OrderHeader>(order.Id.Value);
            return new OrderPlaced(order.Id.Value, orderHeader.ClientId, placedOn);
        }
}
```

## File: `Sources/Sales/Sales.ProcessModel/WholesaleOrdering/QuickQuoteCalculated.cs`
```csharp
namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

public class QuickQuoteCalculated(Guid clientId, QuoteDto quote)
{
    public Guid ClientId { get; } = clientId;
    public QuoteDto Quote { get; } = quote;
}
```

## File: `Sources/Sales/Sales.ProcessModel/WholesaleOrdering/QuoteDto.cs`
```csharp
namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

public readonly struct QuoteDto(Guid productId, int amount, string unitCode, decimal price, string currencyCode)
{
    public Guid ProductId { get; } = productId;
    public int Amount { get; } = amount;
    public string UnitCode { get; } = unitCode;
    public decimal Price { get; } = price;
    public string CurrencyCode { get; } = currencyCode;
}
```

## File: `Sources/Sales/Sales.ProcessModel/WholesaleOrdering/WholesaleOrderingProcess.cs`
```csharp
using NoesisVision.Annotations.Domain;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

[Process(Name, ApplyOnNamespace = true)]
public static class WholesaleOrderingProcess
{
    public const string Name = "Wholesale ordering";
}
```

## File: `Sources/Sales/Sales.ProcessModel.Tests/Sales.ProcessModel.Tests.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <IsPackable>false</IsPackable>
        <AssemblyName>MyCompany.ECommerce.Sales.ProcessModel.Tests</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.Sales</RootNamespace>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
    </PropertyGroup>

    <ItemGroup>
        <PackageReference Include="BDD-toolkit-dotnet" Version="2.4.0" />
        <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
        <PackageReference Include="Microsoft.NET.Test.Sdk" Version="17.9.0" />
        <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
        <PackageReference Include="xunit" Version="2.8.0" />
        <PackageReference Include="xunit.runner.visualstudio" Version="2.8.0">
          <PrivateAssets>all</PrivateAssets>
          <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
        </PackageReference>
        <PackageReference Include="coverlet.collector" Version="6.0.2">
          <PrivateAssets>all</PrivateAssets>
          <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
        </PackageReference>
    </ItemGroup>

    <ItemGroup>
      <ProjectReference Include="..\Sales.ProcessModel\Sales.ProcessModel.csproj" />
    </ItemGroup>

</Project>
```

## File: `Sources/Sales/Sales.RestApi/Sales.RestApi.csproj`
```
﻿<Project Sdk="Microsoft.NET.Sdk.Web">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <AssemblyName>MyCompany.ECommerce.Sales.RestApi</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.Sales</RootNamespace>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
        <OutputType>Library</OutputType>
    </PropertyGroup>

    <ItemGroup>
      <ProjectReference Include="..\..\TechnicalStuff\TechnicalStuff.Crud.Api\TechnicalStuff.Crud.Api.csproj" />      
      <ProjectReference Include="..\Sales.ProcessModel\Sales.ProcessModel.csproj" />      
    </ItemGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="Microsoft.AspNetCore.Mvc.Versioning" Version="5.1.0" />
      <PackageReference Include="Microsoft.EntityFrameworkCore" Version="8.0.5" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>    

</Project>
```

## File: `Sources/Sales/Sales.RestApi/SalesRestApiLayerInfo.cs`
```csharp
using System.Reflection;
using JetBrains.Annotations;
using NoesisVision.Annotations.Technology.CleanArchitecture;

[assembly: AdaptersLayer]

namespace MyCompany.ECommerce.Sales;

[UsedImplicitly]
public static class SalesRestApiLayerInfo
{
    public static Assembly Assembly => typeof(SalesRestApiLayerInfo).Assembly;
}
```

## File: `Sources/Sales/Sales.RestApi/OnlineOrdering/OffersController.cs`
```csharp
using Microsoft.AspNetCore.Mvc;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Sales.OnlineOrdering;

[ApiController]
[Route("rest/online-ordering/offer-request")]
[ApiVersion("1")]
public class OffersController : ControllerBase
{
    private readonly CommandHandler<PriceCart, CartPriced> _priceCartHandler;

    public OffersController(CommandHandler<PriceCart, CartPriced> priceCartHandler) =>
        _priceCartHandler = priceCartHandler;

    [HttpPost]
    public async Task<CartPriced> PriceCart(PriceCart priceCart) =>
        await _priceCartHandler.Handle(priceCart);
}
```

## File: `Sources/Sales/Sales.RestApi/OnlineOrdering/OrdersController.cs`
```csharp
using Microsoft.AspNetCore.Mvc;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Sales.OnlineOrdering;

[ApiController]
[Route("rest/online-ordering/orders")]
[ApiVersion("1")]
public class OrdersController : ControllerBase
{
    private readonly CommandHandler<PlaceOrder, WholesaleOrdering.OrderPlaced> _placeOrderHandler;
    private readonly OrderDetailsFinder _orderDetailsFinder;

    public OrdersController(CommandHandler<PlaceOrder, WholesaleOrdering.OrderPlaced> placeOrderHandler,
        OrderDetailsFinder orderDetailsFinder)
    {
        _placeOrderHandler = placeOrderHandler;
        _orderDetailsFinder = orderDetailsFinder;
    }

    [HttpPost]
    public async Task<CreatedAtActionResult> Place(PlaceOrder placeOrder)
    {
        var orderPlaced = await _placeOrderHandler.Handle(placeOrder);
        // Returning value works only if read model is created synchronously.
        // var orderDetails = await _orderDetailsFinder.GetBy(orderPlaced.OrderId);
        return CreatedAtAction("Get", new {id = orderPlaced.OrderId}, null /*orderDetails*/);
    }

    [HttpGet("{id}")]
    public async Task<OrderDetails> Get(Guid id) => await _orderDetailsFinder.GetBy(id);
}
```

## File: `Sources/Sales/Sales.RestApi/WholesaleOrdering/OrdersConfirmedOfferController.cs`
```csharp
using System.Collections.Immutable;
using System.ComponentModel.DataAnnotations;
using JetBrains.Annotations;
using Microsoft.AspNetCore.Mvc;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

[ApiController]
[Route("rest/wholesale-ordering/orders/{id}/confirmed-offer")]
[ApiVersion("1")]
public class OrdersConfirmedOfferController : ControllerBase
{
    private readonly CommandHandler<ConfirmOffer, OfferConfirmed> _confirmOfferHandler;

    public OrdersConfirmedOfferController(
        CommandHandler<ConfirmOffer, OfferConfirmed> confirmOfferHandler) =>
        _confirmOfferHandler = confirmOfferHandler;

    [HttpPut]
    public async Task<NoContentResult> ConfirmOffer(Guid id, ConfirmedOfferDto confirmedOffer)
    {
        await _confirmOfferHandler.Handle(
            new ConfirmOffer(id, confirmedOffer.CurrencyCode, confirmedOffer.Quotes.ToImmutableArray()));
        // TODO: change to SeeOther
        return NoContent();
    }

    [UsedImplicitly(ImplicitUseTargetFlags.WithMembers)]
    public class ConfirmedOfferDto
    {
        [Required]
        public string CurrencyCode { get; set; }

        [Required]
        public List<QuoteDto> Quotes { get; set; }
    }
}
```

## File: `Sources/Sales/Sales.RestApi/WholesaleOrdering/OrdersController.cs`
```csharp
using Microsoft.AspNetCore.Mvc;
using MyCompany.ECommerce.Sales.Orders;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

[ApiController]
[Route("rest/wholesale-ordering/orders")]
[ApiVersion("1")]
public class OrdersController : ControllerBase
{
    private readonly CommandHandler<CreateOrder, OrderCreated> _createOrderHandler;
    private readonly OrderDetailsFinder _orderDetailsFinder;

    public OrdersController(CommandHandler<CreateOrder, OrderCreated> createOrderHandler,
        OrderDetailsFinder orderDetailsFinder)
    {
        _createOrderHandler = createOrderHandler;
        _orderDetailsFinder = orderDetailsFinder;
    }

    [HttpPost]
    public async Task<CreatedAtActionResult> Create(CreateOrder createOrder)
    {
        var orderCreated = await _createOrderHandler.Handle(createOrder);
        // Returning value works only if read model is created synchronously.
        var orderDetails = await _orderDetailsFinder.GetBy(orderCreated.OrderId);
        return CreatedAtAction("Get", new {id = orderCreated.OrderId}, orderDetails);
    }

    [HttpGet("{id}")]
    public async Task<AllOrderDetails> Get(Guid id) => await _orderDetailsFinder.GetBy(id);
}
```

## File: `Sources/Sales/Sales.RestApi/WholesaleOrdering/OrdersCurrentOfferController.cs`
```csharp
using Microsoft.AspNetCore.Mvc;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

[ApiController]
[Route("rest/wholesale-ordering/orders/{id}/current-offer")]
[ApiVersion("1")]
public class OrdersCurrentOfferController : ControllerBase
{
    private readonly CommandHandler<GetOffer, OfferCalculated> _getOfferHandler;

    public OrdersCurrentOfferController(CommandHandler<GetOffer, OfferCalculated> getOfferHandler) =>
        _getOfferHandler = getOfferHandler;

    [HttpGet]
    public async Task<IEnumerable<QuoteDto>> GetOffer(Guid id, string currencyCode)
    {
        var offerCalculated = await _getOfferHandler.Handle(new GetOffer(id, currencyCode));
        return offerCalculated.Quotes;
    }
}
```

## File: `Sources/Sales/Sales.RestApi/WholesaleOrdering/OrdersHeaderController.cs`
```csharp
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using MyCompany.ECommerce.Sales.Orders;
using MyCompany.ECommerce.TechnicalStuff.Crud.Api;
using MyCompany.ECommerce.TechnicalStuff.Crud.Operations;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

[ApiController]
[Route("/rest/wholesale-ordering/orders/{id}/header")]
[ApiVersion("1")]
public class OrdersHeaderController : ControllerBase
{
    private readonly SalesCrudOperations _operations;

    public OrdersHeaderController(SalesCrudOperations operations) => _operations = operations;

    [HttpGet]
    public async Task<ActionResult<OrderHeader>> Read(Guid id) => await _operations
        .Read(id, DefaultIncludes)
        .ToOkResult();

    [HttpPut]
    public Task<ActionResult<OrderHeader>> Update(Guid id, OrderHeader orderHeader) => _operations
        .Update(id, DefaultIncludes, orderHeader)
        .ToOkResult();

    private static readonly QueryConfig<OrderHeader> DefaultIncludes =
        orderHeaders => orderHeaders.Include(i => i.InvoicingDetails);
}
```

## File: `Sources/Sales/Sales.RestApi/WholesaleOrdering/OrdersHeaderNotesController.cs`
```csharp
using Microsoft.AspNetCore.Mvc;
using MyCompany.ECommerce.Sales.Orders;
using MyCompany.ECommerce.TechnicalStuff.Crud;
using MyCompany.ECommerce.TechnicalStuff.Crud.Api;
using MyCompany.ECommerce.TechnicalStuff.Crud.Operations;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

[ApiController]
[Route("/rest/wholesale-ordering/orders/{orderId}/header/notes")]
[ApiVersion("1")]
public class OrdersHeaderNotesController : ControllerBase
{
    private readonly SalesCrudOperations _operations;

    public OrdersHeaderNotesController(SalesCrudOperations operations) => _operations = operations;

    [HttpPost]
    public async Task<ActionResult<OrderNote>> Create(Guid orderId, OrderNote note)
    {
        await CheckIfOrderExists(orderId);
        return await _operations.Create(note).ToCreatedAtActionResult(createdNote => new
        {
            orderId = createdNote.OrderId,
            id = createdNote.Id
        });
    }

    [HttpGet("{id}")]
    public async Task<ActionResult<OrderNote>> Read(Guid orderId, Guid id)
    {
        await CheckIfOrderExists(orderId);
        return await _operations.Read<OrderNote>(id).ToOkResult();
    }

    [HttpPut("{id}")]
    public async Task<ActionResult<OrderNote>> Update(Guid orderId, Guid id, OrderNote note)
    {
        await CheckIfOrderExists(orderId);
        return await _operations.Update(id, note).ToOkResult();
    }

    [HttpDelete("{id}")]
    public async Task<StatusCodeResult> Delete(Guid orderId, Guid id)
    {
        await CheckIfOrderExists(orderId);
        return await _operations.Delete<OrderNote>(id, DeletePolicy.Hard).ToStatusCodeResult();
    }

    private async Task CheckIfOrderExists(Guid orderId)
    {
        if (!await _operations.CheckIfExists<OrderHeader>(orderId))
            throw new CrudEntityNotFound(typeof(OrderHeader), orderId);
    }
}
```

## File: `Sources/Sales/Sales.RestApi/WholesaleOrdering/OrdersItemsController.cs`
```csharp
using System.ComponentModel.DataAnnotations;
using System.Net.NetworkInformation;
using JetBrains.Annotations;
using Microsoft.AspNetCore.Mvc;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

[ApiController]
[Route("rest/wholesale-ordering/orders/{orderId}/items")]
[ApiVersion("1")]
public class OrdersItemsController : ControllerBase
{
    private readonly CommandHandler<AddToOrder, AddedToOrder> _addToOrderHandler;
        
    public OrdersItemsController(CommandHandler<AddToOrder, AddedToOrder> addToOrderHandler) => 
        _addToOrderHandler = addToOrderHandler;

    [HttpPut]
    public async Task<NoContentResult> Add(Guid orderId, OrderItemDto item)
    {
        await _addToOrderHandler.Handle(new AddToOrder(orderId, item.ProductId, item.Amount, item.UnitCode));
        return NoContent();
    }
        
    [HttpDelete]
    public Task<NoContentResult> Remove(Guid orderId, OrderItemDto item)
    {
        // TODO: RemoveOrderItem
        throw new NetworkInformationException();
    }
        
    [UsedImplicitly(ImplicitUseTargetFlags.WithMembers)]
    public class OrderItemDto
    {
        [Required]
        public Guid ProductId { get; set; }
        [Required]
        public int Amount { get; set; }
        [Required]
        public string UnitCode { get; set; }
    }
}
```

## File: `Sources/Sales/Sales.RestApi/WholesaleOrdering/OrdersPlacementController.cs`
```csharp
using Microsoft.AspNetCore.Mvc;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

[ApiController]
[Route("rest/wholesale-ordering/orders/{id}/placement")]
[ApiVersion("1")]
public class OrdersPlacementController : ControllerBase
{
    private readonly CommandHandler<PlaceOrder, OrderPlaced> _placeOrderHandler;

    public OrdersPlacementController(CommandHandler<PlaceOrder, OrderPlaced> placeOrderHandler) =>
        _placeOrderHandler = placeOrderHandler;

    [HttpPut]
    public async Task<NoContentResult> Place(Guid id)
    {
        await _placeOrderHandler.Handle(new PlaceOrder(id));
        // TODO: change to SeeOther
        return NoContent();
    }
}
```

## File: `Sources/Sales/Sales.RestApi/WholesaleOrdering/QuotesController.cs`
```csharp
using Microsoft.AspNetCore.Mvc;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.Sales.WholesaleOrdering;

[ApiController]
[Route("rest/wholesale-ordering/quotes")]
[ApiVersion("1")]
public class QuotesController : ControllerBase
{
    private readonly CommandHandler<GetQuickQuote, QuickQuoteCalculated> _getQuickQuoteHandler;

    public QuotesController(CommandHandler<GetQuickQuote, QuickQuoteCalculated> getQuickQuoteHandler) =>
        _getQuickQuoteHandler = getQuickQuoteHandler;

    [HttpGet]
    public async Task<QuoteDto> GetQuote(Guid clientId, Guid productId, int amount, string unitCode,
        string currencyCode)
    {
        var quoteCalculated = await _getQuickQuoteHandler.Handle(
            new GetQuickQuote(clientId, productId, amount, unitCode, currencyCode));
        return quoteCalculated.Quote;
    }
}
```

## File: `Sources/Search/SearchModelInfo.json`
```json
{
  "ModelBoundary": "Search",
  "BusinessOwner": "Sales department",
  "DevelopmentOwner": "Supporting team"
}
```

## File: `Sources/Search/Search.Api/Search.Api.csproj`
```
<Project Sdk="Microsoft.NET.Sdk.Web">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
        <AssemblyName>MyCompany.ECommerce.Search.Api</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.Search</RootNamespace>
        <OutputType>Library</OutputType>
    </PropertyGroup>

    <ItemGroup>
      <ProjectReference Include="..\Search.Infrastructure\Search.Infrastructure.csproj" />
    </ItemGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/Search/Search.Api/SearchApiLayerInfo.cs`
```csharp
using System.Reflection;
using System.Runtime.CompilerServices;
using NoesisVision.Annotations.Domain;
using NoesisVision.Annotations.Technology;

[assembly: InternalsVisibleTo("MyCompany.ECommerce.Search.Startup")]
[assembly: Layer("Api")]
[assembly: DomainModel]

namespace MyCompany.ECommerce.Search;

public static class SearchApiLayerInfo
{
    public static Assembly Assembly => typeof(SearchApiLayerInfo).Assembly;
}
```

## File: `Sources/Search/Search.Api/Products/SearchProductsApi.cs`
```csharp
﻿namespace MyCompany.ECommerce.Search.Products;

public static class SearchProductsApi
{
    public static void MapSearchProductsApi(this WebApplication app)
    {
        app.MapGet("search/products", GetProducts);
    }

    private static Task<string> GetProducts(ProductRepository repository) => Task.FromResult("test");
}
```

## File: `Sources/Search/Search.Infrastructure/Search.Infrastructure.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
        <AssemblyName>MyCompany.ECommerce.Search.Infrastructure</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.Search</RootNamespace>
    </PropertyGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/Search/Search.Infrastructure/SearchDb.cs`
```csharp
using JetBrains.Annotations;
using NoesisVision.Annotations.Technology;

namespace MyCompany.ECommerce.Search;

[Database("Search", ServerName = "Elastic")]
[UsedImplicitly]
internal class SearchDb
{
    
}
```

## File: `Sources/Search/Search.Infrastructure/SearchInfrastructureLayerInfo.cs`
```csharp
using System.Reflection;
using System.Runtime.CompilerServices;
using NoesisVision.Annotations.Domain;
using NoesisVision.Annotations.Technology;

[assembly: InternalsVisibleTo("MyCompany.ECommerce.Search.Startup")]
[assembly: Layer("Infrastructure")]
[assembly: DomainModel]

namespace MyCompany.ECommerce.Search;

public static class SearchInfrastructureLayerInfo
{
    public static Assembly Assembly => typeof(SearchInfrastructureLayerInfo).Assembly;
}
```

## File: `Sources/Search/Search.Infrastructure/Products/ProductElasticRepository.cs`
```csharp
using JetBrains.Annotations;

namespace MyCompany.ECommerce.Search.Products;

[UsedImplicitly]
internal class ProductElasticRepository(SearchDb db) : ProductRepository
{
    private readonly SearchDb _db = db;
}
```

## File: `Sources/Search/Search.Infrastructure/Products/ProductRepository.cs`
```csharp
﻿namespace MyCompany.ECommerce.Search.Products;

public interface ProductRepository { }
```

## File: `Sources/Search.Startup/Program.cs`
```csharp
using MyCompany.ECommerce.Search;
using MyCompany.ECommerce.Search.Products;
using NoesisVision.Annotations.Technology;
using NoesisVision.Annotations.Technology.CleanArchitecture;

[assembly: DeployableUnit("ecommerce-search")]
[assembly: Tier("Application")]
[assembly: FrameworkLayer]

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddScoped<ProductRepository, ProductElasticRepository>();
builder.Services.AddScoped<SearchDb>();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}
app.MapSearchProductsApi();
app.Run();
```

## File: `Sources/Search.Startup/Search.Startup.csproj`
```
<Project Sdk="Microsoft.NET.Sdk.Web">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
        <AssemblyName>MyCompany.ECommerce.Search.Startup</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.Search</RootNamespace>
    </PropertyGroup>

    <ItemGroup>
        <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
        <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
        <PackageReference Include="Swashbuckle.AspNetCore" Version="6.6.1" />
    </ItemGroup>

    <ItemGroup>
      <ProjectReference Include="..\Search\Search.Api\Search.Api.csproj" />
      <ProjectReference Include="..\Search\Search.Infrastructure\Search.Infrastructure.csproj" />
    </ItemGroup>

</Project>
```

## File: `Sources/Search.Startup/appsettings.Development.json`
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

## File: `Sources/Search.Startup/appsettings.json`
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

## File: `Sources/Search.Startup/Properties/launchSettings.json`
```json
﻿{
  "$schema": "https://json.schemastore.org/launchsettings.json",
  "profiles": {
    "Search.Startup": {
      "commandName": "Project",
      "dotnetRunMessages": true,
      "launchBrowser": false,
      "launchUrl": "swagger",
      "applicationUrl": "http://localhost:5239",
      "environmentVariables": {
        "ASPNETCORE_ENVIRONMENT": "Development"
      }
    }
  }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff/AssemblyInfo.cs`
```csharp
using NoesisVision.Annotations;

[assembly: ExcludeFromDocs]
```

## File: `Sources/TechnicalStuff/TechnicalStuff/CorruptedDataError.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff;

public class CorruptedDataError : Exception{}
```

## File: `Sources/TechnicalStuff/TechnicalStuff/DataEquals.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff;

public interface DataEquals<in T>
{
    bool HasSameDataAs(T other);
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff/DesignError.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff;

public class DesignError : Exception
{
    public DesignError(string message) : base(message) { }
    public DesignError(string message, Exception innerException) : base(message, innerException) { }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff/DomainError.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff;

public class DomainError : Exception
{
        
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff/EnumExtensions.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff;

public static class EnumExtensions
{
    public static string ToCode<T>(this T value) where T : struct, Enum => value.ToString();
        
    public static T ToDomainModel<T>(this string value) where T: struct, Enum => 
        (T) Enum.Parse(typeof(T), value, true);
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff/EqualsExtensions.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff;

public static class EqualsExtensions
{
    public static bool HasSameItemsAs<T>(this IList<T> collection, IList<T> other)
        where T : IEquatable<T>
    {
        if (other.Count != collection.Count) 
            return false;
        var counts = new Dictionary<T, int>(collection.Count);
        for (var i = 0; i < collection.Count; i++)
        {
            var item = collection[i];
            if (counts.ContainsKey(item))
                counts[item]++;
            else
                counts.Add(item, 1);
        }
        for (var i = 0; i < collection.Count; i++)
        {
            var item = other[i];
            if (counts.TryGetValue(item, out var count))
            {
                if (count == 1)
                    counts.Remove(item);
                else
                    counts[item]--;
            }
            else
            {
                return false;
            }
        }
        return counts.Count == 0;
    }
        
    public static bool HasSameItemsAs<TKey, TValue>(this IDictionary<TKey, TValue> dictionary,
        IEnumerable<KeyValuePair<TKey, TValue>> other)
        where TValue : IEquatable<TValue>
    {
        var count = 0;
        foreach (var (key, otherValue) in other)
        {
            if (!dictionary.TryGetValue(key, out var value) || !otherValue.Equals(value))
                return false;
            count++;
        }
        return dictionary.Count == count;
    }
        
    public static bool HasSameItemsAs<TKey, TValue>(this IDictionary<TKey, TValue> dictionary,
        IEnumerable<KeyValuePair<TKey, TValue>> other,
        Func<TValue, TValue, bool> comparer)
    {
        var count = 0;
        foreach (var (key, otherValue) in other)
        {
            if (!dictionary.TryGetValue(key, out var value) || !comparer(value, otherValue))
                return false;
            count++;
        }
        return dictionary.Count == count;
    }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff/HashCodeExtensions.cs`
```csharp
using System.Collections.Immutable;

namespace MyCompany.ECommerce.TechnicalStuff;

public static class HashCodeExtensions
{
    public static HashCode CombineWith<T>(this HashCode hashCode, T value)
    {
        hashCode.Add(value);
        return hashCode;
    }
        
    public static HashCode CombineWith<T>(this HashCode hashCode, ImmutableArray<T> array)
    {
        var length = array.Length;
        for (var i = 0; i < length; i++) hashCode.Add(array[i]);
        return hashCode;
    }
        
    public static HashCode CombineWith<T>(this HashCode hashCode, IEnumerable<T> enumerable)
    {
        foreach (var item in enumerable) hashCode.Add(item);
        return hashCode;
    }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff/InfrastructureError.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff;

public class InfrastructureError : Exception
{
    protected InfrastructureError() { }
        
    protected InfrastructureError(string message) : base(message) { }
        
    protected InfrastructureError(string message, Exception innerException) : base(message, innerException) { }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff/PermanentInfrastructureError.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff;

public class PermanentInfrastructureError : InfrastructureError
{
    public PermanentInfrastructureError() { }

    public PermanentInfrastructureError(string message) : base(message) { }

    public PermanentInfrastructureError(string message, Exception innerException) :
        base(message, innerException) { }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff/TechnicalStuff.csproj`
```
﻿<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>        
        <AssemblyName>MyCompany.ECommerce.TechnicalStuff</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.TechnicalStuff</RootNamespace>
        <LangVersion>default</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
    </PropertyGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/TechnicalStuff/TechnicalStuff/TemporaryInfrastructureError.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff;

public class TemporaryInfrastructureError : InfrastructureError
{
    public TemporaryInfrastructureError() { }
        
    public TemporaryInfrastructureError(string message) : base(message) { }

    public TemporaryInfrastructureError(string message, Exception innerException) :
        base(message, innerException) { }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff/ValueObjects/ValueObject.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.ValueObjects;

public interface ValueObject<T>
{
    T Value { get; init; }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff/ValueObjects/ValueObjectExtensions.cs`
```csharp
using System.Reflection;

namespace MyCompany.ECommerce.TechnicalStuff.ValueObjects;

public static class ValueObjectExtensions
{
    public static IEnumerable<ValueObjectMeta> GetValueObjectsMeta(this Assembly assembly)
    {
        foreach (var type in assembly.GetTypes())
        {
            if (type.IsInterface || (type.IsClass && type.IsAbstract))
                continue;
            if (!type.IsValueObject(out var valueType))
                continue;
            yield return new ValueObjectMeta(type, valueType!);
        }
    }

    public static bool IsValueObject(this Type type, out Type? valueType)
    {
        var valueObjectInterfaces = type.GetInterfaces()
            .Where(i => i.IsGenericType && i.GetGenericTypeDefinition() == typeof(ValueObject<>))
            .ToList();
        switch (valueObjectInterfaces.Count)
        {
            case 0:
                valueType = null;
                return false;
            case 1:
                valueType = valueObjectInterfaces[0].GetGenericArguments()[0];
                return true;
            case > 1:
                throw new NotSupportedException(
                    "Value Object should not implement more than one ValueObject<> interface");
            default:
                throw new ArgumentOutOfRangeException();
        }
    }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff/ValueObjects/ValueObjectMeta.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.ValueObjects;

public readonly record struct ValueObjectMeta(Type Type, Type ValueType);
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Api/AssemblyInfo.cs`
```csharp
using NoesisVision.Annotations;

[assembly: ExcludeFromDocs]
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Api/TechnicalStuff.Api.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <AssemblyName>MyCompany.ECommerce.TechnicalStuff.Api</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.TechnicalStuff.Api</RootNamespace>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
    </PropertyGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="Microsoft.AspNetCore.Mvc.Versioning" Version="5.1.0" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
      <PackageReference Include="NSwag.AspNetCore" Version="14.0.7" />
    </ItemGroup>

    <ItemGroup>
      <ProjectReference Include="..\TechnicalStuff\TechnicalStuff.csproj" />
    </ItemGroup>

</Project>
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Api/Versioning/ApiVersionDocumentOptions.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.Api.Versioning;

public class ApiVersionDocumentOptions
{
    public string PathPrefix { get; set; }
    public string Title { get; set; }
    public string Description { get; set; }
    public bool UseEndpointVersioning { get; set; }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Api/Versioning/EndpointVersioningProcessor.cs`
```csharp
using System.Reflection;
using Microsoft.AspNetCore.Mvc;
using NSwag.Generation.Processors;
using NSwag.Generation.Processors.Contexts;

namespace MyCompany.ECommerce.TechnicalStuff.Api.Versioning;

internal class EndpointVersioningProcessor(string versionParameterName) : IOperationProcessor
{
    public bool Process(OperationProcessorContext context)
    {
        if (OperationIsForSingleVersion(context, out var version))
        {
            SetApiVersionInPath(context, version);
            RemoveApiVersionParameter(context);
            return true;
        }
        return true;
    }

    private static bool OperationIsForSingleVersion(OperationProcessorContext context, out string version)
    {
        var mapToApiVersionAttributes = context.MethodInfo
            .GetCustomAttributes<MapToApiVersionAttribute>()
            .ToArray();
        if (mapToApiVersionAttributes.Length == 1)
        {
            version = mapToApiVersionAttributes[0].Versions[0].ToString();
            return true;
        }
        if (mapToApiVersionAttributes.Length == 0)
        {
            var apiVersionAttributes = context.ControllerType
                .GetCustomAttributes<ApiVersionAttribute>()
                .ToArray();
            if (apiVersionAttributes.Length == 1)
            {
                version = apiVersionAttributes[0].Versions[0].ToString();
                return true;
            }
            if (apiVersionAttributes.Length == 0)
            {
                version = null;
                return false;
            }
        }
        throw new DesignError($"Operation {context.OperationDescription.Path} is mapped to more than one version");
    }

    private void SetApiVersionInPath(OperationProcessorContext context, string version) =>
        context.OperationDescription.Path =
            $"{context.OperationDescription.Path}?{versionParameterName}={version}";

    private void RemoveApiVersionParameter(OperationProcessorContext context)
    {
        var parameters = context.OperationDescription.Operation.Parameters;
        var apiVersionParameter = parameters.FirstOrDefault(
            p => p.Name.Equals(versionParameterName, StringComparison.OrdinalIgnoreCase));
        if (apiVersionParameter != null)
            parameters.Remove(apiVersionParameter);
    }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Api/Versioning/VersioningServiceCollectionExtensions.cs`
```csharp
using Microsoft.AspNetCore.Mvc.Versioning;
using Microsoft.Extensions.DependencyInjection;

namespace MyCompany.ECommerce.TechnicalStuff.Api.Versioning;

public static class VersioningServiceCollectionExtensions
{
    private const string EndpointVersionParameterName = "version";

    public static IServiceCollection AddEndpointVersioningByQueryParameter(this IServiceCollection services) =>
        services.AddApiVersioning(options =>
        {
            options.ApiVersionReader = new QueryStringApiVersionReader(EndpointVersionParameterName);
            options.AssumeDefaultVersionWhenUnspecified = false;
            options.ReportApiVersions = false;
        });

    public static IServiceCollection AddApiVersionDocument(this IServiceCollection services,
        Action<ApiVersionDocumentOptions> configure)
    {
        if (configure is null) throw new ArgumentNullException(nameof(configure));
        var options = new ApiVersionDocumentOptions();
        configure.Invoke(options);
        if (options.PathPrefix is null) throw new ArgumentNullException(nameof(options.PathPrefix));
        services.AddOpenApiDocument(settings =>
        {
            var pathPrefix = options.PathPrefix.Trim('/');
            settings.DocumentName = pathPrefix;
            settings.Version = options.UseEndpointVersioning ? "versioning per endpoint" : "no versioning";
            settings.Title = options.Title ?? pathPrefix;
            settings.Description = options.Description;
            settings.AddOperationFilter(context =>
                context.OperationDescription.Path.StartsWith($"/{pathPrefix}/"));
            if (options.UseEndpointVersioning)
                settings.OperationProcessors.Add(new EndpointVersioningProcessor(EndpointVersionParameterName));
        });
        return services;
        // TODO: better schemas naming - configuration (attributes, fluent api, etc.)
    }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Crud/AssemblyInfo.cs`
```csharp
using NoesisVision.Annotations;

[assembly: ExcludeFromDocs]
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Crud/CrudEntity.cs`
```csharp
using JetBrains.Annotations;
using Microsoft.AspNetCore.Mvc.ModelBinding;

namespace MyCompany.ECommerce.TechnicalStuff.Crud;

[UsedImplicitly(ImplicitUseTargetFlags.WithMembers)]
public class CrudEntity
{
    [BindNever] public Guid Id { get; set; }
    [BindNever] public bool IsDeleted { get; set; }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Crud/CrudEntityNotFound.cs`
```csharp
using JetBrains.Annotations;

namespace MyCompany.ECommerce.TechnicalStuff.Crud;

public class CrudEntityNotFound(Type type, Guid id)
    : Exception($"Entity not found. Type: {type.FullName}, Id: {id.ToString()}")
{
    [PublicAPI] public Type Type { get; } = type;
    [PublicAPI] public Guid Id { get; } = id;
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Crud/TechnicalStuff.Crud.csproj`
```
<Project Sdk="Microsoft.NET.Sdk.Web">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
        <OutputType>Library</OutputType>
        <AssemblyName>MyCompany.ECommerce.TechnicalStuff.Crud</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.TechnicalStuff.Crud</RootNamespace>
    </PropertyGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="Microsoft.AspNetCore.JsonPatch" Version="8.0.5" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>

    <ItemGroup>
      <ProjectReference Include="..\TechnicalStuff\TechnicalStuff.csproj" />
    </ItemGroup>

</Project>
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Crud/Operations/CrudOperations.cs`
```csharp
using JetBrains.Annotations;
using Microsoft.AspNetCore.JsonPatch;
using MyCompany.ECommerce.TechnicalStuff.Crud.Operations.Results;

namespace MyCompany.ECommerce.TechnicalStuff.Crud.Operations;

public interface CrudOperations
{
    [PublicAPI]
    IQueryable<TEntity> Entities<TEntity>()
        where TEntity : class;

    [PublicAPI]
    Task<bool> CheckIfExists<TEntity>(Guid id)
        where TEntity : CrudEntity;

    [PublicAPI]
    Task<Created<TEntity>> Create<TEntity>(TEntity entity)
        where TEntity : CrudEntity;

    [PublicAPI]
    Task<TEntity> Read<TEntity>(Guid id)
        where TEntity : CrudEntity;

    [PublicAPI]
    Task<TEntity> Read<TEntity>(Guid id, QueryConfig<TEntity> queryConfig)
        where TEntity : CrudEntity;

    [PublicAPI]
    Task<TResult> Read<TEntity, TResult>(Guid id, QueryConfig<TEntity, TResult> queryConfig)
        where TEntity : CrudEntity;

    [PublicAPI]
    IAsyncEnumerable<TEntity> Read<TEntity>(QueryConfig<TEntity> queryConfig)
        where TEntity : class;

    [PublicAPI]
    IAsyncEnumerable<TResult> Read<TEntity, TResult>(QueryConfig<TEntity, TResult> queryConfig)
        where TEntity : class;

    [PublicAPI]
    Task<Updated<TEntity>> Update<TEntity>(Guid id, TEntity entity)
        where TEntity : CrudEntity;

    [PublicAPI]
    Task<Updated<TEntity>> Update<TEntity>(Guid id, QueryConfig<TEntity> queryConfig, TEntity entity)
        where TEntity : CrudEntity;

    [PublicAPI]
    Task<Updated<TEntity>> Update<TEntity>(Guid id, JsonPatchDocument<TEntity> patch)
        where TEntity : CrudEntity;

    [PublicAPI]
    Task<Updated<TEntity>> Update<TEntity>(Guid id, QueryConfig<TEntity> queryConfig,
        JsonPatchDocument<TEntity> patch)
        where TEntity : CrudEntity;

    [PublicAPI]
    Task<Updated> Update<TEntity>(Guid id, Action<TEntity> updateEntity)
        where TEntity : CrudEntity;

    [PublicAPI]
    Task<Updated> Update<TEntity>(Guid id, QueryConfig<TEntity> queryConfig, Action<TEntity> updateEntity)
        where TEntity : CrudEntity;

    [PublicAPI]
    Task<Updated<TEntity>> Update<TEntity>(Guid id, Func<TEntity, TEntity> updateEntity)
        where TEntity : CrudEntity;

    [PublicAPI]
    Task<Updated<TEntity>> Update<TEntity>(Guid id, QueryConfig<TEntity> queryConfig,
        Func<TEntity, TEntity> updateEntity)
        where TEntity : CrudEntity;

    [PublicAPI]
    Task<Updated<TResult>> Update<TEntity, TResult>(Guid id, Func<TEntity, TResult> updateEntity)
        where TEntity : CrudEntity
        where TResult : class;

    [PublicAPI]
    Task<Updated<TResult>> Update<TEntity, TResult>(Guid id, QueryConfig<TEntity> queryConfig,
        Func<TEntity, TResult> updateEntity)
        where TEntity : CrudEntity
        where TResult : class;

    [PublicAPI]
    Task<Deleted> Delete<TEntity>(Guid id, DeletePolicy deletePolicy)
        where TEntity : CrudEntity;

    [PublicAPI]
    Task SaveChanges();
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Crud/Operations/DeletePolicy.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.Crud.Operations;

public enum DeletePolicy
{
    Soft,
    Hard
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Crud/Operations/QueryConfig.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.Crud.Operations;

public delegate IQueryable<T> QueryConfig<T>(IQueryable<T> queryable);

public delegate IQueryable<TOut> QueryConfig<in TIn, out TOut>(IQueryable<TIn> queryable);
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Crud/Operations/QueryableExtensions.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.Crud.Operations;

public static class QueryableExtensions
{
    public static IQueryable<T> Apply<T>(this IQueryable<T> queryable, QueryConfig<T> queryConfig) =>
        queryConfig(queryable);

    public static IQueryable<TOut> Apply<TIn, TOut>(this IQueryable<TIn> queryable,
        QueryConfig<TIn, TOut> queryConfig) =>
        queryConfig(queryable);
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Crud/Operations/Results/Created.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.Crud.Operations.Results;

public readonly struct Created<TEntity>(TEntity entity) : IEquatable<Created<TEntity>>
    where TEntity : class
{
    public TEntity Entity { get; } = entity;

    public bool Equals(Created<TEntity> other) => Entity.Equals(other.Entity);

    public override bool Equals(object obj) => obj is Created<TEntity> other && Equals(other);

    public override int GetHashCode() => Entity.GetHashCode();

    public static implicit operator TEntity(Created<TEntity> created) => created.Entity;
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Crud/Operations/Results/CrudResult.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.Crud.Operations.Results;

public static class CrudResult
{
    public static Created<TEntity> Created<TEntity>(TEntity entity) where TEntity : class => new(entity);

    public static Updated Updated(Guid id) => new(id);

    public static Updated<TEntity> Updated<TEntity>(TEntity entity) where TEntity : class => new(entity);

    public static Deleted Deleted(Guid id, bool wasPresent) => new(id, wasPresent);
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Crud/Operations/Results/Deleted.cs`
```csharp
using JetBrains.Annotations;

namespace MyCompany.ECommerce.TechnicalStuff.Crud.Operations.Results;

public readonly struct Deleted(Guid id, bool wasPresent) : IEquatable<Deleted>
{
    [PublicAPI] public Guid Id { get; } = id;
    [PublicAPI] public bool WasPresent { get; } = wasPresent;

    public bool Equals(Deleted other) => (Id, WasPresent).Equals((other.Id, other.WasPresent));

    public override bool Equals(object obj) => obj is Deleted other && Equals(other);

    public override int GetHashCode() => (Id, WasPresent).GetHashCode();
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Crud/Operations/Results/Updated.cs`
```csharp
using JetBrains.Annotations;

namespace MyCompany.ECommerce.TechnicalStuff.Crud.Operations.Results;

public readonly struct Updated(Guid id) : IEquatable<Updated>
{
    [PublicAPI] public Guid Id { get; } = id;

    public bool Equals(Updated other) => Id.Equals(other.Id);

    public override bool Equals(object obj) => obj is Updated other && Equals(other);

    public override int GetHashCode() => Id.GetHashCode();
}

public readonly struct Updated<TEntity>(TEntity entity) : IEquatable<Updated<TEntity>>
    where TEntity : class
{
    [PublicAPI] public TEntity Entity { get; } = entity;

    public bool Equals(Updated<TEntity> other) => Entity.Equals(other.Entity);

    public override bool Equals(object obj) => obj is Updated<TEntity> other && Equals(other);

    public override int GetHashCode() => Entity.GetHashCode();

    public static implicit operator TEntity(Updated<TEntity> created) => created.Entity;
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Crud.Api/AssemblyInfo.cs`
```csharp
using NoesisVision.Annotations;

[assembly: ExcludeFromDocs]
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Crud.Api/CrudControllerExtensions.cs`
```csharp
using JetBrains.Annotations;
using Microsoft.AspNetCore.Mvc;
using MyCompany.ECommerce.TechnicalStuff.Crud.Operations.Results;

namespace MyCompany.ECommerce.TechnicalStuff.Crud.Api;

public static class CrudControllerExtensions
{
    private const string DefaultCreatedAtAction = "Read";
    private const string DefaultCreatedAtController = null;
    private static readonly Func<CrudEntity, object> DefaultRouteValuesFactory = e => new {id = e.Id};

    [PublicAPI]
    public static async Task<ActionResult<TEntity>> ToCreatedAtActionResult<TEntity>(
        this Task<Created<TEntity>> createPromise)
        where TEntity : CrudEntity =>
        ToCreatedAtActionResult(
            await createPromise,
            DefaultCreatedAtAction,
            DefaultCreatedAtController,
            DefaultRouteValuesFactory);

    [PublicAPI]
    public static async Task<ActionResult<TEntity>> ToCreatedAtActionResult<TEntity>(
        this Task<Created<TEntity>> createPromise,
        Func<TEntity, object> routeValuesFactory)
        where TEntity : CrudEntity =>
        ToCreatedAtActionResult(
            await createPromise,
            DefaultCreatedAtAction,
            DefaultCreatedAtController,
            routeValuesFactory);

    [PublicAPI]
    public static async Task<ActionResult<TEntity>> ToCreatedAtActionResult<TEntity>(
        this Task<Created<TEntity>> createPromise,
        string actionName)
        where TEntity : CrudEntity =>
        ToCreatedAtActionResult(
            await createPromise,
            actionName,
            DefaultCreatedAtController,
            DefaultRouteValuesFactory);

    [PublicAPI]
    public static async Task<ActionResult<TEntity>> ToCreatedAtActionResult<TEntity>(
        this Task<Created<TEntity>> createPromise,
        string actionName,
        Func<TEntity, object> routeValuesFactory)
        where TEntity : CrudEntity =>
        ToCreatedAtActionResult(
            await createPromise,
            actionName,
            DefaultCreatedAtController,
            routeValuesFactory);

    [PublicAPI]
    public static async Task<ActionResult<TEntity>> ToCreatedAtActionResult<TEntity>(
        this Task<Created<TEntity>> createPromise,
        string actionName,
        string controllerName,
        Func<TEntity, object> routeValuesFactory)
        where TEntity : CrudEntity =>
        ToCreatedAtActionResult(
            await createPromise,
            actionName,
            controllerName,
            routeValuesFactory);

    private static ActionResult<TEntity> ToCreatedAtActionResult<TEntity>(Created<TEntity> created,
        string actionName,
        string controllerName,
        Func<TEntity, object> routeValuesFactory)
        where TEntity : CrudEntity =>
        new CreatedAtActionResult(
            actionName,
            controllerName,
            routeValuesFactory,
            created.Entity);

    [PublicAPI]
    public static async Task<ActionResult<TEntity>> ToOkResult<TEntity>(this Task<Created<TEntity>> createPromise)
        where TEntity : CrudEntity
    {
        var created = await createPromise;
        return new OkObjectResult(created.Entity);
    }

    [PublicAPI]
    public static async Task<ActionResult<TEntity>> ToOkResult<TEntity>(this Task<TEntity> readPromise) =>
        new(await readPromise);

    [PublicAPI]
    public static async Task<ActionResult<TEntity>> ToOkResult<TEntity>(this Task<Updated<TEntity>> updatePromise)
        where TEntity : class
        => new(await updatePromise);

    [PublicAPI]
    public static async Task<NoContentResult> ToNoContentResult(this Task<Updated> updatePromise)
    {
        await updatePromise;
        return new NoContentResult();
    }

    [PublicAPI]
    public static async Task<OkResult> ToOkResult(this Task<Updated> updatePromise)
    {
        await updatePromise;
        return new OkResult();
    }

    [PublicAPI]
    public static async Task<NoContentResult> ToNoContentResult<TEntity>(this Task<Updated<TEntity>> updatePromise)
        where TEntity : class
    {
        await updatePromise;
        return new NoContentResult();
    }

    [PublicAPI]
    public static async Task<StatusCodeResult> ToStatusCodeResult(this Task<Deleted> deletePromise)
    {
        await deletePromise;
        return new NoContentResult();

        // var deleted = await deletePromise;
        // return deleted.WasPresent ? (StatusCodeResult) new NoContentResult() : new NotFoundResult();
    }

    [PublicAPI]
    public static async Task<OkResult> ToOkResult(this Task<Deleted> deletePromise)
    {
        await deletePromise;
        return new OkResult();
    }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Crud.Api/TechnicalStuff.Crud.Api.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <AssemblyName>MyCompany.ECommerce.TechnicalStuff.Crud.Api</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.TechnicalStuff.Crud.Api</RootNamespace>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
    </PropertyGroup>

    <ItemGroup>
      <ProjectReference Include="..\TechnicalStuff.Crud\TechnicalStuff.Crud.csproj" />
    </ItemGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Crud.Ef/AssemblyInfo.cs`
```csharp
using NoesisVision.Annotations;

[assembly: ExcludeFromDocs]
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Crud.Ef/EfCrudDao.cs`
```csharp
using Microsoft.AspNetCore.JsonPatch;
using Microsoft.EntityFrameworkCore;
using MyCompany.ECommerce.TechnicalStuff.Crud.Operations;
using MyCompany.ECommerce.TechnicalStuff.Crud.Operations.Results;

namespace MyCompany.ECommerce.TechnicalStuff.Crud.Ef;

public class EfCrudDao : CrudOperations
{
    private readonly DbContext _context;

    protected EfCrudDao(DbContext context) => _context = context;

    public IQueryable<TEntity> Entities<TEntity>() where TEntity : class => _context.Set<TEntity>();

    public Task<bool> CheckIfExists<TEntity>(Guid id) where TEntity : CrudEntity =>
        Entities<TEntity>().AnyAsync(e => e.Id == id);

    public async Task<Created<TEntity>> Create<TEntity>(TEntity entity)
        where TEntity : CrudEntity
    {
        if (entity.Id != Guid.Empty)
            throw new InvalidOperationException();
        if (entity.IsDeleted)
            throw new InvalidOperationException();
        entity.Id = Guid.NewGuid();
        await _context.Set<TEntity>().AddAsync(entity);
        await _context.SaveChangesAsync();
        return CrudResult.Created(entity);
    }

    public Task<TEntity> Read<TEntity>(Guid id)
        where TEntity : CrudEntity =>
        Read(id, Config<TEntity>.Empty);

    public Task<TEntity> Read<TEntity>(Guid id, QueryConfig<TEntity> queryConfig)
        where TEntity : CrudEntity =>
        GetById<TEntity>(id, query => query
            .AsNoTracking()
            .Apply(queryConfig));

    public Task<TResult> Read<TEntity, TResult>(Guid id, QueryConfig<TEntity, TResult> queryConfig)
        where TEntity : CrudEntity =>
        GetById<TEntity, TResult>(id, query => query
            .AsNoTracking()
            .Apply(queryConfig));

    public IAsyncEnumerable<TEntity> Read<TEntity>(QueryConfig<TEntity> queryConfig)
        where TEntity : class =>
        Entities<TEntity>()
            .AsNoTracking()
            .Apply(queryConfig)
            .AsAsyncEnumerable();

    public IAsyncEnumerable<TResult> Read<TEntity, TResult>(QueryConfig<TEntity, TResult> queryConfig)
        where TEntity : class =>
        Entities<TEntity>()
            .AsNoTracking()
            .Apply(queryConfig)
            .AsAsyncEnumerable();

    public Task<Updated<TEntity>> Update<TEntity>(Guid id, TEntity entity)
        where TEntity : CrudEntity =>
        Update(id, Config<TEntity>.Empty, entity);

    public async Task<Updated<TEntity>> Update<TEntity>(Guid id, QueryConfig<TEntity> queryConfig, TEntity entity)
        where TEntity : CrudEntity
    {
        entity.Id = id;
        _context.Set<TEntity>().Update(entity);
        await _context.SaveChangesAsync();
        return CrudResult.Updated(entity);
    }

    public Task<Updated<TEntity>> Update<TEntity>(Guid id, JsonPatchDocument<TEntity> patch)
        where TEntity : CrudEntity =>
        Update(id, Config<TEntity>.Empty, patch);

    public async Task<Updated<TEntity>> Update<TEntity>(Guid id, QueryConfig<TEntity> queryConfig,
        JsonPatchDocument<TEntity> patch)
        where TEntity : CrudEntity
    {
        var entity = await GetById(id, queryConfig);
        patch.ApplyTo(entity);
        await _context.SaveChangesAsync();
        return CrudResult.Updated(entity);
    }

    public Task<Updated> Update<TEntity>(Guid id, Action<TEntity> updateEntity)
        where TEntity : CrudEntity =>
        Update(id, Config<TEntity>.Empty, updateEntity);

    public async Task<Updated> Update<TEntity>(Guid id, QueryConfig<TEntity> queryConfig,
        Action<TEntity> updateEntity)
        where TEntity : CrudEntity
    {
        var entity = await GetById(id, queryConfig);
        updateEntity(entity);
        await _context.SaveChangesAsync();
        return CrudResult.Updated(id);
    }

    public Task<Updated<TEntity>> Update<TEntity>(Guid id, Func<TEntity, TEntity> updateEntity)
        where TEntity : CrudEntity =>
        Update<TEntity>(id, Config<TEntity>.Empty, updateEntity);

    public async Task<Updated<TEntity>> Update<TEntity>(Guid id, QueryConfig<TEntity> queryConfig,
        Func<TEntity, TEntity> updateEntity)
        where TEntity : CrudEntity
    {
        var entity = await GetById(id, queryConfig);
        var updatedEntity = updateEntity(entity);
        await _context.SaveChangesAsync();
        return CrudResult.Updated(updatedEntity);
    }

    public Task<Updated<TResult>> Update<TEntity, TResult>(Guid id, Func<TEntity, TResult> updateEntity)
        where TEntity : CrudEntity
        where TResult : class=>
        Update(id, Config<TEntity>.Empty, updateEntity);

    public async Task<Updated<TResult>> Update<TEntity, TResult>(Guid id, QueryConfig<TEntity> queryConfig,
        Func<TEntity, TResult> updateEntity)
        where TEntity : CrudEntity
        where TResult : class
    {
        var entity = await GetById(id, queryConfig);
        var result = updateEntity(entity);
        await _context.SaveChangesAsync();
        return CrudResult.Updated(result);
    }

    public async Task<Deleted> Delete<TEntity>(Guid id, DeletePolicy deletePolicy)
        where TEntity : CrudEntity
    {
        var entity = await Entities<TEntity>().SingleOrDefaultAsync(e => e.Id == id);
        if (entity is null || entity.IsDeleted)
            return new Deleted(id, false);

        switch (deletePolicy)
        {
            case DeletePolicy.Soft:
                entity.IsDeleted = true;
                break;
            case DeletePolicy.Hard:
                _context.Set<TEntity>().Remove(entity);
                break;
            default:
                throw new ArgumentOutOfRangeException(nameof(deletePolicy),
                    deletePolicy,
                    $"Unsupported {nameof(DeletePolicy)}");
        }
        await _context.SaveChangesAsync();
        return CrudResult.Deleted(id, true);
    }

    public Task SaveChanges() => _context.SaveChangesAsync();

    private async Task<TEntity> GetById<TEntity>(Guid id, QueryConfig<TEntity> queryConfig)
        where TEntity : CrudEntity
    {
        var result = await Entities<TEntity>()
            .Apply(queryConfig)
            .SingleOrDefaultAsync(entity => entity.Id == id);
        if (result is null)
            throw new CrudEntityNotFound(typeof(TEntity), id);
        return result;
    }

    private async Task<TResult> GetById<TEntity, TResult>(Guid id, QueryConfig<TEntity, TResult> queryConfig)
        where TEntity : CrudEntity
    {
        var result = await Entities<TEntity>()
            .Where(entity => entity.Id == id)
            .Apply(queryConfig)
            .SingleOrDefaultAsync();
        if (result is null)
            throw new CrudEntityNotFound(typeof(TEntity), id);
        return result;
    }

    private static class Config<T>
    {
        public static QueryConfig<T> Empty { get; } = queryable => queryable;
    }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Crud.Ef/TechnicalStuff.Crud.Ef.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <AssemblyName>MyCompany.ECommerce.TechnicalStuff.Crud.Ef</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.TechnicalStuff.Crud.Ef</RootNamespace>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
    </PropertyGroup>

    <ItemGroup>
      <ProjectReference Include="..\TechnicalStuff.Crud\TechnicalStuff.Crud.csproj" />
    </ItemGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="Microsoft.EntityFrameworkCore" Version="8.0.5" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Ef/AssemblyInfo.cs`
```csharp
using NoesisVision.Annotations;

[assembly: ExcludeFromDocs]
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Ef/TechnicalStuff.Ef.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <AssemblyName>MyCompany.ECommerce.TechnicalStuff.Ef</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.TechnicalStuff.Ef</RootNamespace>
        <LangVersion>default</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
    </PropertyGroup>

    <ItemGroup>
      <ProjectReference Include="..\TechnicalStuff\TechnicalStuff.csproj" />
    </ItemGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="Microsoft.EntityFrameworkCore" Version="8.0.5" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>    

</Project>
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Ef/ValueConverters/ValueObjectConverter.cs`
```csharp
using System.Linq.Expressions;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
using MyCompany.ECommerce.TechnicalStuff.ValueObjects;

namespace MyCompany.ECommerce.TechnicalStuff.Ef.ValueConverters;

public class ValueObjectConverter<TValueObject, TValue> : ValueConverter<TValueObject, TValue>
    where TValueObject : ValueObject<TValue>, new()
{
    public ValueObjectConverter() : base(ToValue, ToValueObject) { }

    private static Expression<Func<TValueObject, TValue>> ToValue => id => id.Value;

    private static Expression<Func<TValue, TValueObject>> ToValueObject => value => new TValueObject { Value = value };
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Json/AssemblyInfo.cs`
```csharp
using NoesisVision.Annotations;

[assembly: ExcludeFromDocs]
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Json/TechnicalStuff.Json.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
        <AssemblyName>MyCompany.ECommerce.TechnicalStuff.Json</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.TechnicalStuff.Json</RootNamespace>
    </PropertyGroup>

    <ItemGroup>
      <ProjectReference Include="..\TechnicalStuff\TechnicalStuff.csproj" />
    </ItemGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Json/Json/DecimalValueObjectJsonConverter.cs`
```csharp
using System.Globalization;
using System.Text.Json;
using System.Text.Json.Serialization;
using MyCompany.ECommerce.TechnicalStuff.ValueObjects;

namespace MyCompany.ECommerce.TechnicalStuff.Json.Json;

public class DecimalValueObjectJsonConverter<TValueObject> : JsonConverter<TValueObject>
    where TValueObject : struct, ValueObject<decimal>
{
    public override TValueObject Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
    {
        if (reader.TokenType is JsonTokenType.Null or JsonTokenType.None)
            throw new InvalidOperationException();
        return new TValueObject { Value = decimal.Parse(reader.GetString()!) };
    }

    public override void Write(Utf8JsonWriter writer, TValueObject valueObject, JsonSerializerOptions options) =>
        writer.WriteStringValue(valueObject.Value.ToString("N2", NumberFormatInfo.InvariantInfo));
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Json/Json/GuidValueObjectJsonConverter.cs`
```csharp
using System.Text.Json;
using System.Text.Json.Serialization;
using MyCompany.ECommerce.TechnicalStuff.ValueObjects;

namespace MyCompany.ECommerce.TechnicalStuff.Json.Json;

public class GuidValueObjectJsonConverter<TValueObject> : JsonConverter<TValueObject>
    where TValueObject : struct, ValueObject<Guid>
{
    public override TValueObject Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
    {
        if (reader.TokenType is JsonTokenType.Null or JsonTokenType.None)
            throw new InvalidOperationException();
        return new TValueObject { Value = Guid.Parse(reader.GetString()!) };
    }

    public override void Write(Utf8JsonWriter writer, TValueObject valueObject, JsonSerializerOptions options) =>
        writer.WriteStringValue(valueObject.Value.ToString("N"));
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Json/Json/LongValueObjectJsonConverter.cs`
```csharp
using System.Text.Json;
using System.Text.Json.Serialization;
using MyCompany.ECommerce.TechnicalStuff.ValueObjects;

namespace MyCompany.ECommerce.TechnicalStuff.Json.Json;

public class LongValueObjectJsonConverter<TValueObject> : JsonConverter<TValueObject>
    where TValueObject : struct, ValueObject<long>
{
    public override TValueObject Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
    {
        if (reader.TokenType is JsonTokenType.Null or JsonTokenType.None)
            throw new InvalidOperationException();
        return new TValueObject { Value = reader.GetInt64() };
    }

    public override void Write(Utf8JsonWriter writer, TValueObject valueObject, JsonSerializerOptions options) =>
        writer.WriteNumberValue(valueObject.Value);
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Json/Json/StringValueObjectJsonConverter.cs`
```csharp
using System.Text.Json;
using System.Text.Json.Serialization;
using MyCompany.ECommerce.TechnicalStuff.ValueObjects;

namespace MyCompany.ECommerce.TechnicalStuff.Json.Json;

public class StringValueObjectJsonConverter<TValueObject> : JsonConverter<TValueObject>
    where TValueObject : struct, ValueObject<string>
{
    public override TValueObject Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
    {
        if (reader.TokenType is JsonTokenType.Null or JsonTokenType.None)
            throw new InvalidOperationException();
        return new TValueObject { Value = reader.GetString()! };
    }

    public override void Write(Utf8JsonWriter writer, TValueObject valueObject, JsonSerializerOptions options) =>
        writer.WriteStringValue(valueObject.Value);
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Json/Json/ValueObjectJsonConverterFactory.cs`
```csharp
using System.Text.Json;
using System.Text.Json.Serialization;
using MyCompany.ECommerce.TechnicalStuff.ValueObjects;

namespace MyCompany.ECommerce.TechnicalStuff.Json.Json;

public class ValueObjectJsonConverterFactory : JsonConverterFactory
{
    public override bool CanConvert(Type typeToConvert) =>
        typeToConvert.IsValueObject(out var valueType) &&
        IsValueTypeSupported(valueType!);

    public override JsonConverter CreateConverter(Type typeToConvert, JsonSerializerOptions options)
    {
        if (!typeToConvert.IsValueType)
            throw new NotSupportedException();
        if (!typeToConvert.IsValueObject(out var valueType))
            throw new NotSupportedException();
        if (valueType == typeof(long))
            return (JsonConverter)Activator.CreateInstance(
                typeof(LongValueObjectJsonConverter<>).MakeGenericType(typeToConvert))!;
        if (valueType == typeof(string))
            return (JsonConverter)Activator.CreateInstance(
                typeof(StringValueObjectJsonConverter<>).MakeGenericType(typeToConvert))!;
        if (valueType == typeof(decimal))
            return (JsonConverter)Activator.CreateInstance(
                typeof(DecimalValueObjectJsonConverter<>).MakeGenericType(typeToConvert))!;
        if (valueType == typeof(Guid))
            return (JsonConverter)Activator.CreateInstance(
                typeof(GuidValueObjectJsonConverter<>).MakeGenericType(typeToConvert))!;
        throw new NotSupportedException();
    }

    

    private static bool IsValueTypeSupported(Type valueType) =>
        valueType == typeof(long) ||
        valueType == typeof(string) ||
        valueType == typeof(decimal) ||
        valueType == typeof(Guid);
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Kafka/AssemblyInfo.cs`
```csharp
using NoesisVision.Annotations;

[assembly: ExcludeFromDocs]
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Kafka/KafkaMessage.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.Kafka;

public class KafkaMessage(string topic, string key, string valueAsJson)
{
    public string Topic { get; } = topic;
    public string Key { get; } = key;
    public string ValueAsJson { get; } = valueAsJson;
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Kafka/KafkaMessageProducer.cs`
```csharp
using System.Collections.Immutable;
using Confluent.Kafka;
using Microsoft.Extensions.Logging;

namespace MyCompany.ECommerce.TechnicalStuff.Kafka;

public class KafkaMessageProducer(ProducerConfig config, ILogger<KafkaMessageProducer> logger)
    : IDisposable
{
    private static readonly ImmutableHashSet<ErrorCode> InvalidMessageErrors = new HashSet<ErrorCode>
    {
        ErrorCode.Local_BadMsg,
        ErrorCode.Local_KeySerialization,
        ErrorCode.Local_ValueSerialization,
        ErrorCode.InvalidMsg,
        ErrorCode.InvalidMsgSize,
        ErrorCode.MsgSizeTooLarge
    }.ToImmutableHashSet();

    private readonly IProducer<string, string> _producer = new ProducerBuilder<string, string>(config).Build();

    public async Task<KafkaProducerResult> Produce(KafkaMessage message, CancellationToken cancellationToken)
    {
        try
        {
            var result = await _producer.ProduceAsync(message.Topic,
                new Message<string, string> {Key = message.Key, Value = message.ValueAsJson},
                cancellationToken);
            return result.Status == PersistenceStatus.Persisted
                ? KafkaProducerResult.NoError
                : KafkaProducerResult.NoAck;
        }
        catch (ProduceException<string, string> e)
        {
            logger.LogError(e, "Kafka producer failed");
            return InvalidMessageErrors.Contains(e.Error.Code)
                ? KafkaProducerResult.InvalidMessage
                : KafkaProducerResult.OtherError;
        }
    }

    public void Dispose() => _producer.Dispose();
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Kafka/KafkaProducerResult.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.Kafka;

public enum KafkaProducerResult
{
    NoError,
    InvalidMessage,
    NoAck,
    OtherError
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Kafka/TechnicalStuff.Kafka.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <AssemblyName>MyCompany.ECommerce.TechnicalStuff.Kafka</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.TechnicalStuff.Kafka</RootNamespace>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
    </PropertyGroup>

    <ItemGroup>
      <PackageReference Include="Confluent.Kafka" Version="2.4.0" />
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="Microsoft.Extensions.Logging.Abstractions" Version="8.0.1" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>

    <ItemGroup>
      <ProjectReference Include="..\TechnicalStuff\TechnicalStuff.csproj" />
    </ItemGroup>

</Project>
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Marten/AssemblyInfo.cs`
```csharp
using NoesisVision.Annotations;

[assembly: ExcludeFromDocs]
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Marten/LightweightSessionFactory.cs`
```csharp
using System.Data;
using JetBrains.Annotations;
using Marten;
using Marten.Services;

namespace MyCompany.ECommerce.TechnicalStuff.Marten;

[UsedImplicitly]
public class LightweightSessionFactory(IDocumentStore store) : ISessionFactory
{
    public IQuerySession QuerySession() => store.QuerySession();

    public IDocumentSession OpenSession() => store.OpenSession(new SessionOptions
    {
        Tracking = DocumentTracking.None,
        IsolationLevel = IsolationLevel.ReadCommitted
    });
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Marten/TechnicalStuff.Marten.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <AssemblyName>MyCompany.ECommerce.TechnicalStuff.Marten</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.TechnicalStuff.Marten</RootNamespace>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
    </PropertyGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="Marten" Version="7.13.1" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
      <PackageReference Include="Npgsql" Version="8.0.3" />
    </ItemGroup>

</Project>
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox/AssemblyInfo.cs`
```csharp
using NoesisVision.Annotations;

[assembly: ExcludeFromDocs]
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox/BatchProcessingResult.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.Outbox;

public enum BatchProcessingResult
{
    NotFullBatchProcessed,
    FullBatchProcessed,
    TemporaryError
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox/InPlaceOutboxMessageProcessor.cs`
```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;
using Newtonsoft.Json;

namespace MyCompany.ECommerce.TechnicalStuff.Outbox;

public class InPlaceOutboxMessageProcessor(
    MessageTypes messageTypes,
    IServiceScopeFactory serviceScopeProvider,
    ILogger<InPlaceOutboxMessageProcessor> logger)
    : OutboxMessageProcessor
{
    public string ProcessorType => OutboxMessageProcessors.InPlace;

    public async Task<MessageProcessingResult> Process(OutboxMessage outboxMessage,
        CancellationToken cancellationToken)
    {
        var messageType = messageTypes.GetMessageTypeFor(outboxMessage.MessageTypeId);
        var handlerType = messageTypes.GetHandlerTypeFor(outboxMessage.MessageTypeId);
        if (!TryDeserializeMessage(outboxMessage.PayloadAsJson, messageType, out var message))
            return MessageProcessingResult.MessageUnprocessable;

        return await TryHandleMessage(message, handlerType);
    }

    private bool TryDeserializeMessage(string json, Type messageType, out Message message)
    {
        try
        {
            message = (Message) JsonConvert.DeserializeObject(json, messageType);
            return true;
        }
        catch (JsonException e)
        {
            logger.LogError(e, "Message deserialization failed");
            message = null;
            return false;
        }
    }

    private async Task<MessageProcessingResult> TryHandleMessage(Message message, Type handlerType)
    {
        using var scope = serviceScopeProvider.CreateScope();
        var handler = (MessageHandler) scope.ServiceProvider.GetService(handlerType);
        try
        {
            await handler.Handle(message);
            return MessageProcessingResult.Processed;
        }
        catch (DomainError e)
        {
            logger.LogError(e, "Domain error");
            return MessageProcessingResult.Processed;
        }
        catch (TemporaryInfrastructureError e)
        {
            logger.LogError(e, "Temporary infrastructure error");
            return MessageProcessingResult.TemporaryError;
        }
        catch (PermanentInfrastructureError e)
        {
            logger.LogCritical(e, "Permanent infrastructure error");
            return MessageProcessingResult.MessageUnprocessable;
        }
    }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox/InPlaceTransactionalOutbox.cs`
```csharp
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;
using Newtonsoft.Json;

namespace MyCompany.ECommerce.TechnicalStuff.Outbox;

public abstract class InPlaceTransactionalOutbox<TMessage>(
    TransactionalOutboxes outboxes,
    TransactionalOutboxRepository repository,
    MessageTypes messageTypes)
    : TransactionalOutbox<TMessage>(outboxes, repository, messageTypes)
    where TMessage : Message
{
    protected override string GetProcessorTypeFor(TMessage message) => OutboxMessageProcessors.InPlace;

    protected override string CreatePayloadFrom(TMessage message) => JsonConvert.SerializeObject(message);
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox/MessageProcessingResult.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.Outbox;

public enum MessageProcessingResult
{
    Processed,
    TemporaryError,
    MessageUnprocessable
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox/NonTransactionalMessageSendingDecorator.cs`
```csharp
﻿using System.Transactions;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.TechnicalStuff.Outbox;

public class NonTransactionalMessageSendingDecorator<TCommand>(
    CommandHandler<TCommand> decorated,
    NonTransactionalOutboxes outboxes)
    : CommandHandler<TCommand>
    where TCommand : struct, Command
{
    public async Task Handle(TCommand command)
    {
        await decorated.Handle(command);
        var transaction = Transaction.Current;
        if (transaction != null && transaction.TransactionInformation.Status != TransactionStatus.Committed)
            throw new DesignError($"{GetType().Name} used within uncommitted transaction");
        await Task.WhenAll(outboxes.ForCurrentUseCase.Select(outbox => outbox.Send()));
    }
}
    
public class NonTransactionalMessageSendingDecorator<TCommand, TResult>(
    CommandHandler<TCommand, TResult> decorated,
    NonTransactionalOutboxes outboxes)
    : CommandHandler<TCommand, TResult>
    where TCommand : struct, Command
{
    public async Task<TResult> Handle(TCommand command)
    {
        var result = await decorated.Handle(command);
        var transaction = Transaction.Current;
        if (transaction != null && transaction.TransactionInformation.Status != TransactionStatus.Committed)
            throw new DesignError($"{GetType().Name} used within uncommitted transaction");
        await Task.WhenAll(outboxes.ForCurrentUseCase.Select(outbox => outbox.Send()));
        return result;
    }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox/NonTransactionalOutbox.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.Outbox;

public abstract class NonTransactionalOutbox
{
    protected NonTransactionalOutbox(NonTransactionalOutboxes outboxes) => outboxes.Register(this);
        
    public abstract Task Send();
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox/NonTransactionalOutboxes.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.Outbox;

public class NonTransactionalOutboxes
{
    private readonly List<NonTransactionalOutbox> _outboxes = new();
    public IReadOnlyList<NonTransactionalOutbox> ForCurrentUseCase => _outboxes.AsReadOnly();

    public void Register(NonTransactionalOutbox outbox) => _outboxes.Add(outbox);
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox/OutboxMessage.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.Outbox;

public class OutboxMessage(
    Guid id,
    string partitionKey,
    string processorType,
    string messageTypeId,
    string payloadAsJson)
{
    public Guid Id { get; } = id;
    public string PartitionKey { get; } = partitionKey;
    public string ProcessorType { get; } = processorType;
    public string MessageTypeId { get; } = messageTypeId;
    public string PayloadAsJson { get; } = payloadAsJson;
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox/OutboxMessageProcessor.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.Outbox;

public interface OutboxMessageProcessor
{
    string ProcessorType { get; }
    Task<MessageProcessingResult> Process(OutboxMessage outboxMessage, CancellationToken cancellationToken);
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox/OutboxMessageProcessors.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.Outbox;

internal static class OutboxMessageProcessors
{
    internal const string InPlace = "InPlace";
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox/TechnicalStuff.Outbox.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <AssemblyName>MyCompany.ECommerce.TechnicalStuff.Outbox</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.TechnicalStuff.Outbox</RootNamespace>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
    </PropertyGroup>

    <ItemGroup>      
      <ProjectReference Include="..\TechnicalStuff.ProcessModel\TechnicalStuff.ProcessModel.csproj" />      
      <ProjectReference Include="..\TechnicalStuff\TechnicalStuff.csproj" />
    </ItemGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="Microsoft.Extensions.DependencyInjection.Abstractions" Version="8.0.1" />
      <PackageReference Include="Microsoft.Extensions.Logging.Abstractions" Version="8.0.1" />
      <PackageReference Include="Newtonsoft.Json" Version="13.0.3" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox/TransactionalMessageSendingDecorator.cs`
```csharp
using System.Transactions;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.TechnicalStuff.Outbox;

public class TransactionalMessageSendingDecorator<TCommand>(
    CommandHandler<TCommand> decorated,
    TransactionalOutboxes outboxes)
    : CommandHandler<TCommand>
    where TCommand : struct, Command
{
    public async Task Handle(TCommand command)
    {
        var transaction = Transaction.Current;
        if (transaction == null || transaction.TransactionInformation.Status != TransactionStatus.Active)
            throw new DesignError($"{GetType().Name} used without active transaction");
        await decorated.Handle(command);
        await Task.WhenAll(outboxes.ForCurrentUseCase.Select(outbox => outbox.Save()));
    }
}
    
public class TransactionalMessageSendingDecorator<TCommand, TResult>(
    CommandHandler<TCommand, TResult> decorated,
    TransactionalOutboxes outboxes)
    : CommandHandler<TCommand, TResult>
    where TCommand : struct, Command
{
    public async Task<TResult> Handle(TCommand command)
    {
        var transaction = Transaction.Current;
        if (transaction == null || transaction.TransactionInformation.Status != TransactionStatus.Active)
            throw new DesignError($"{GetType().Name} used without active transaction");
        var result = await decorated.Handle(command);
        await Task.WhenAll(outboxes.ForCurrentUseCase.Select(outbox => outbox.Save()));
        return result;
    }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox/TransactionalOutbox.cs`
```csharp
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.TechnicalStuff.Outbox;

public class TransactionalOutbox
{
    private readonly List<OutboxMessage> _messages = new();
    private readonly TransactionalOutboxRepository _repository;

    protected TransactionalOutbox(TransactionalOutboxes outboxes, TransactionalOutboxRepository repository)
    {
        outboxes.Register(this);
        _repository = repository;
    }

    public Task Save() => _repository.Save(_messages);

    protected void Add(string partitionKey, string processorType, string messageTypeId, string payload) =>
        _messages.Add(new OutboxMessage(Guid.NewGuid(), partitionKey, processorType, messageTypeId, payload));
}

public abstract class TransactionalOutbox<TMessage>(
    TransactionalOutboxes outboxes,
    TransactionalOutboxRepository repository,
    MessageTypes messageTypes)
    : TransactionalOutbox(outboxes, repository)
    where TMessage : Message
{
    public void Add(TMessage message)
    {
        var partitionKey = GetPartitionKeyFor(message);
        var processorType = GetProcessorTypeFor(message);
        var messageTypeId = messageTypes.GetTypeIdFor(message);
        var payload = CreatePayloadFrom(message);
        Add(partitionKey, processorType, messageTypeId, payload);
    }

    protected abstract string GetPartitionKeyFor(TMessage message);

    protected abstract string GetProcessorTypeFor(TMessage message);

    protected abstract string CreatePayloadFrom(TMessage message);
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox/TransactionalOutboxProcessor.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.Outbox;

public interface TransactionalOutboxProcessor
{
    Task<BatchProcessingResult> ProcessSingleBatch(int partition, CancellationToken cancellationToken);
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox/TransactionalOutboxRepository.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.Outbox;

public interface TransactionalOutboxRepository
{
    Task Save(IEnumerable<OutboxMessage> messages);
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox/TransactionalOutboxes.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.Outbox;

public class TransactionalOutboxes
{
    private readonly List<TransactionalOutbox> _outboxes = new();
    public IReadOnlyList<TransactionalOutbox> ForCurrentUseCase => _outboxes.AsReadOnly();

    public void Register(TransactionalOutbox outbox) => _outboxes.Add(outbox);
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox.Kafka/AssemblyInfo.cs`
```csharp
using NoesisVision.Annotations;

[assembly: ExcludeFromDocs]
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox.Kafka/KafkaOutboxMessageProcessor.cs`
```csharp
using Microsoft.Extensions.Logging;
using MyCompany.ECommerce.TechnicalStuff.Kafka;
using Newtonsoft.Json;

namespace MyCompany.ECommerce.TechnicalStuff.Outbox.Kafka;

public class KafkaOutboxMessageProcessor(
    KafkaMessageProducer kafkaMessageProducer,
    ILogger<KafkaOutboxMessageProcessor> logger)
    : OutboxMessageProcessor
{
    public string ProcessorType => OutboxMessageProcessors.Kafka;

    public async Task<MessageProcessingResult> Process(OutboxMessage outboxMessage,
        CancellationToken cancellationToken)
    {
        if (!CheckProcessorTypeFor(outboxMessage))
            return MessageProcessingResult.MessageUnprocessable;
        if (!TryDeserialize(outboxMessage, out var kafkaMessage))
            return MessageProcessingResult.MessageUnprocessable;
        return await Produce(kafkaMessage, cancellationToken);
    }

    private bool CheckProcessorTypeFor(OutboxMessage outboxMessage)
    {
        if (outboxMessage.ProcessorType == ProcessorType)
            return true;
        logger.LogCritical(
            "Wrong OutboxMessageProcessor. Message {MessageId}, actual processor: {ActualProcessorType}, required processor: {RequiredProcessorType}",
            outboxMessage.Id, ProcessorType, outboxMessage.ProcessorType);
        return false;
    }

    private bool TryDeserialize(OutboxMessage outboxMessage, out KafkaMessage kafkaMessage)
    {
        try
        {
            kafkaMessage = JsonConvert.DeserializeObject<KafkaMessage>(outboxMessage.PayloadAsJson);
            return true;
        }
        catch (JsonException e)
        {
            logger.LogCritical(e, "Message deserialization failed. Message id: {MessageId}", outboxMessage.Id);
            kafkaMessage = null;
            return false;
        }
    }

    private async Task<MessageProcessingResult> Produce(KafkaMessage kafkaMessage,
        CancellationToken cancellationToken)
    {
        var result = await kafkaMessageProducer.Produce(kafkaMessage, cancellationToken);
        return result switch
        {
            KafkaProducerResult.NoError => MessageProcessingResult.Processed,
            KafkaProducerResult.InvalidMessage => MessageProcessingResult.MessageUnprocessable,
            KafkaProducerResult.NoAck => MessageProcessingResult.TemporaryError,
            KafkaProducerResult.OtherError => MessageProcessingResult.TemporaryError,
            _ => throw new ArgumentOutOfRangeException(nameof(result))
        };
    }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox.Kafka/NonTransactionalKafkaOutbox.cs`
```csharp
using MyCompany.ECommerce.TechnicalStuff.Kafka;

namespace MyCompany.ECommerce.TechnicalStuff.Outbox.Kafka;

public abstract class NonTransactionalKafkaOutbox<TMessage>(
    KafkaMessageProducer kafkaMessageProducer,
    NonTransactionalOutboxes outboxes)
    : NonTransactionalOutbox(outboxes)
{
    private readonly List<KafkaMessage> _kafkaMessages = new();

    public void Add(TMessage message)
    {
        var kafkaMessage = ToKafkaMessage(message);
        _kafkaMessages.Add(kafkaMessage);
    }

    protected abstract KafkaMessage ToKafkaMessage(TMessage message);

    public override Task Send()
    {
        foreach (var kafkaMessage in _kafkaMessages)
            kafkaMessageProducer.Produce(kafkaMessage, CancellationToken.None);
        _kafkaMessages.Clear();
        return Task.CompletedTask;
    }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox.Kafka/OutboxMessageProcessors.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.Outbox.Kafka;

internal static class OutboxMessageProcessors
{
    internal const string Kafka = "Kafka";
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox.Kafka/TechnicalStuff.Outbox.Kafka.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <AssemblyName>MyCompany.ECommerce.TechnicalStuff.Outbox.Kafka</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.TechnicalStuff.Outbox.Kafka</RootNamespace>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
    </PropertyGroup>

    <ItemGroup>
      <ProjectReference Include="..\TechnicalStuff.Kafka\TechnicalStuff.Kafka.csproj" />
      <ProjectReference Include="..\TechnicalStuff.Outbox\TechnicalStuff.Outbox.csproj" />
    </ItemGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox.Kafka/TransactionalKafkaOutbox.cs`
```csharp
using MyCompany.ECommerce.TechnicalStuff.Kafka;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;
using Newtonsoft.Json;

namespace MyCompany.ECommerce.TechnicalStuff.Outbox.Kafka;

public abstract class TransactionalKafkaOutbox<TMessage>(
    TransactionalOutboxes outboxes,
    TransactionalOutboxRepository repository,
    MessageTypes messageTypes)
    : TransactionalOutbox<TMessage>(outboxes, repository, messageTypes)
    where TMessage : Message
{
    protected abstract string Topic { get; }

    protected override string GetProcessorTypeFor(TMessage message) => OutboxMessageProcessors.Kafka;

    protected override string CreatePayloadFrom(TMessage message)
    {
        var kafkaMessage = new KafkaMessage(Topic,
            GetPartitionKeyFor(message),
            Serialize(message));
        return Serialize(kafkaMessage);
    }

    // TODO: flexible serialization (json, avro, etc. - Kafka specific)
    private static string Serialize(TMessage message) => JsonConvert.SerializeObject(message);

    private static string Serialize(KafkaMessage kafkaMessage) => JsonConvert.SerializeObject(kafkaMessage);
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox.Postgres/AssemblyInfo.cs`
```csharp
using NoesisVision.Annotations;

[assembly: ExcludeFromDocs]
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox.Postgres/Batch.cs`
```csharp
using System.Collections;

namespace MyCompany.ECommerce.TechnicalStuff.Outbox.Postgres;

public readonly struct Batch(int requestedSize, long startingOffset, IReadOnlyCollection<OutboxMessage> messages)
    : IEnumerable<Batch.Item>
{
    public bool IsFull => messages.Count == requestedSize;

    public bool IsOffsetCommitRequiredFor(Item item, int commitInterval) =>
        IsAtIntervalEnd(item, commitInterval) ||
        IsLast(item);

    private bool IsAtIntervalEnd(Item item, int commitInterval) =>
        (item.Offset - startingOffset + 1) % commitInterval == 0; 
        
    private bool IsLast(Item item) => 
        item.Offset == startingOffset + messages.Count - 1;

    public IEnumerator<Item> GetEnumerator()
    {
        var offset = startingOffset;
        return messages.Select(m => new Item(offset++, m)).GetEnumerator();
    }

    IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();

    public readonly struct Item(long offset, OutboxMessage outboxMessage)
    {
        public long Offset { get; } = offset;
        public OutboxMessage OutboxMessage { get; } = outboxMessage;
    }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox.Postgres/PostgresOutboxProcessor.cs`
```csharp
using JetBrains.Annotations;
using Microsoft.Extensions.Logging;
using MyCompany.ECommerce.TechnicalStuff.Postgres;

namespace MyCompany.ECommerce.TechnicalStuff.Outbox.Postgres;

[UsedImplicitly]
public class PostgresOutboxProcessor<TConnectionFactory> : TransactionalOutboxProcessor
    where TConnectionFactory : PostgresConnectionProvider
{
    private readonly PostgresOutboxRepository _repository;
    private readonly Dictionary<string, OutboxMessageProcessor> _processors;
    private readonly PostgresOutboxProcessorSettings _processorSettings;
    private readonly ILogger<PostgresOutboxProcessor<TConnectionFactory>> _logger;

    protected PostgresOutboxProcessor(
        PostgresOutboxRepository repository,
        IEnumerable<OutboxMessageProcessor> messageProcessors,
        PostgresOutboxProcessorSettings processorSettings,
        ILogger<PostgresOutboxProcessor<TConnectionFactory>> logger)
    {
        _repository = repository;
        _processors = messageProcessors.ToDictionary(p => p.ProcessorType);
        _processorSettings = processorSettings;
        _logger = logger;
    }

    public async Task<BatchProcessingResult> ProcessSingleBatch(int partition, CancellationToken cancellationToken)
    {
        try
        {
            var batch = await _repository.GetUnprocessedMessagesFor(partition, _processorSettings.BatchSize,
                cancellationToken);
            foreach (var item in batch)
            {
                if (cancellationToken.IsCancellationRequested)
                    return BatchProcessingResult.NotFullBatchProcessed;
                var result = await Process(item, cancellationToken);
                if (result == BatchItemProcessingResult.TemporaryError)
                {
                    await _repository.SaveCurrentOffset(partition, item.Offset - 1);
                    return BatchProcessingResult.TemporaryError;
                }
                if (batch.IsOffsetCommitRequiredFor(item, _processorSettings.CommitOffsetInterval))
                    await _repository.SaveCurrentOffset(partition, item.Offset);
            }
            return batch.IsFull
                ? BatchProcessingResult.FullBatchProcessed
                : BatchProcessingResult.NotFullBatchProcessed;
        }
        catch (TemporaryInfrastructureError e)
        {
            _logger.LogError(e, "Temporary infrastructure error");
            return BatchProcessingResult.TemporaryError;
        }
    }

    private async Task<BatchItemProcessingResult> Process(Batch.Item item, CancellationToken cancellationToken)
    {
        var messageProcessingResult = await Process(item.OutboxMessage, cancellationToken);
        switch (messageProcessingResult)
        {
            case MessageProcessingResult.Processed:
                return BatchItemProcessingResult.Processed;
            case MessageProcessingResult.MessageUnprocessable:
                await _repository.MoveToUnprocessableMessages(item.OutboxMessage);
                return BatchItemProcessingResult.Processed;
            case MessageProcessingResult.TemporaryError:
                return BatchItemProcessingResult.TemporaryError;
            default:
                throw new ArgumentOutOfRangeException(nameof(messageProcessingResult));
        }
    }

    private async Task<MessageProcessingResult> Process(OutboxMessage message, CancellationToken cancellationToken)
    {
        if (_processors.TryGetValue(message.ProcessorType, out var processor))
            return await processor.Process(message, cancellationToken);
        _logger.LogCritical("Missing OutboxMessageProcessor of type: {ProcessorType}", message.ProcessorType);
        return MessageProcessingResult.MessageUnprocessable;
    }

    private enum BatchItemProcessingResult
    {
        Processed,
        TemporaryError
    }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox.Postgres/PostgresOutboxProcessorSettings.cs`
```csharp
using JetBrains.Annotations;

namespace MyCompany.ECommerce.TechnicalStuff.Outbox.Postgres;

[UsedImplicitly(ImplicitUseTargetFlags.WithMembers)]
public class PostgresOutboxProcessorSettings
{
    public int BatchSize { get; set; }
    public int CommitOffsetInterval { get; set; }
    public int CleanupThreshold { get; set; }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox.Postgres/PostgresOutboxRepository.cs`
```csharp
﻿using JetBrains.Annotations;
using MyCompany.ECommerce.TechnicalStuff.Persistence;

namespace MyCompany.ECommerce.TechnicalStuff.Outbox.Postgres;

[UsedImplicitly]
public class PostgresOutboxRepository(MainDb db) : TransactionalOutboxRepository
{
    private readonly MainDb _db = db;

    public Task Save(IEnumerable<OutboxMessage> messages)
    {
        throw new NotImplementedException();
    }

    public async Task<Batch> GetUnprocessedMessagesFor(int partition, int batchSize,
        CancellationToken cancellationToken)
    {
        throw new NotImplementedException();
    }

    public async Task SaveCurrentOffset(int partition, long currentOffset)
    {
        throw new NotImplementedException();
    }

    public async Task MoveToUnprocessableMessages(OutboxMessage message)
    {
        throw new NotImplementedException();
    }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox.Postgres/TechnicalStuff.Outbox.Postgres.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <AssemblyName>MyCompany.ECommerce.TechnicalStuff.Outbox.Postgres</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.TechnicalStuff.Outbox.Postgres</RootNamespace>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
    </PropertyGroup>

    <ItemGroup>
      <ProjectReference Include="..\TechnicalStuff.Outbox\TechnicalStuff.Outbox.csproj" />
      <ProjectReference Include="..\TechnicalStuff.Postgres\TechnicalStuff.Postgres.csproj" />
    </ItemGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="Microsoft.Extensions.Logging.Abstractions" Version="8.0.1" />
      <PackageReference Include="Newtonsoft.Json" Version="13.0.3" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
      <PackageReference Include="SqlKata" Version="2.4.0" />
      <PackageReference Include="SqlKata.Execution" Version="2.4.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox.Quartz/AssemblyInfo.cs`
```csharp
using NoesisVision.Annotations;

[assembly: ExcludeFromDocs]
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox.Quartz/OutboxBackgroundServiceSettings.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.Outbox.Quartz;

public class OutboxBackgroundServiceSettings(
    IReadOnlyList<Type> processorTypes,
    int? minDelayBetweenBatches,
    int? delayAfterEmptyBatch)
{
    public IReadOnlyList<Type> ProcessorTypes { get; } = processorTypes;
    public int? MinDelayBetweenBatches { get; } = minDelayBetweenBatches;
    public int? DelayAfterEmptyBatch { get; } = delayAfterEmptyBatch;
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox.Quartz/OutboxJob.cs`
```csharp
using Microsoft.Extensions.Logging;
using Quartz;

namespace MyCompany.ECommerce.TechnicalStuff.Outbox.Quartz;

// TODO: deleting processed messages in separate Job
[DisallowConcurrentExecution]
public class OutboxJob<TProcessor>(int partition, TProcessor processor, ILogger<OutboxJob<TProcessor>> logger)
    : IJob
    where TProcessor : class, TransactionalOutboxProcessor
{
    public async Task Execute(IJobExecutionContext context)
    {
        try
        {
            logger.LogDebug("Outbox processing started. {OutboxProcessorType}, {Partition}",
                processor.GetType().Name, partition);
            while (!context.CancellationToken.IsCancellationRequested)
            {
                var processingResult = await processor.ProcessSingleBatch(partition, context.CancellationToken);
                switch (processingResult)
                {
                    case BatchProcessingResult.FullBatchProcessed:
                        break;
                    case BatchProcessingResult.NotFullBatchProcessed:
                    case BatchProcessingResult.TemporaryError:
                        return;
                    default:
                        throw new ArgumentOutOfRangeException(nameof(processingResult));
                }
            }
            logger.LogDebug("Outbox processing ended. {OutboxProcessorType}, {Partition}",
                processor.GetType().Name, partition);
        }
        catch (Exception e) when (e is not OperationCanceledException)
        {
            logger.LogCritical(e,
                "Unexpected exception in outbox processor: {OutboxProcessorType}",
                processor.GetType().Name);
        }
    }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Outbox.Quartz/TechnicalStuff.Outbox.Quartz.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
        <AssemblyName>MyCompany.ECommerce.TechnicalStuff.Outbox.Quartz</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.TechnicalStuff.Outbox.Quartz</RootNamespace>
    </PropertyGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
      <PackageReference Include="Quartz" Version="3.9.0" />
    </ItemGroup>

    <ItemGroup>
      <ProjectReference Include="..\TechnicalStuff.Outbox\TechnicalStuff.Outbox.csproj" />
    </ItemGroup>

</Project>
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Persistence/AssemblyInfo.cs`
```csharp
using NoesisVision.Annotations;

[assembly: ExcludeFromDocs]
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Persistence/DbConnectionProvider.cs`
```csharp
using System.Data.Common;

namespace MyCompany.ECommerce.TechnicalStuff.Persistence;

public interface DbConnectionProvider
{
    Task<DbConnection> CreateOneOffConnection();
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Persistence/DbTransactionProvider.cs`
```csharp
using System.Data;
using System.Data.Common;

namespace MyCompany.ECommerce.TechnicalStuff.Persistence;

public interface DbTransactionProvider : DbConnectionProvider
{
    DbTransaction GetCurrentTransaction();
    Task BeginTransaction(IsolationLevel level = IsolationLevel.ReadCommitted);
    Task CommitCurrentTransaction();
    Task RollbackCurrentTransaction();
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Persistence/MainDb.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.Persistence;

public interface MainDb : DbTransactionProvider{}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Persistence/OptimisticLockException.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.Persistence;

public class OptimisticLockException : Exception { }
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Persistence/TechnicalStuff.Persistence.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
        <AssemblyName>MyCompany.ECommerce.TechnicalStuff.Persistence</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.TechnicalStuff.Persistence</RootNamespace>
    </PropertyGroup>

    <ItemGroup>
      <ProjectReference Include="..\TechnicalStuff\TechnicalStuff.csproj" />
    </ItemGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Persistence/TrackedSet.cs`
```csharp
using System.Collections;

namespace MyCompany.ECommerce.TechnicalStuff.Persistence;

public class TrackedSet<TItem, TDbItem> : IReadOnlySet<TItem>
    where TItem : IEquatable<TItem>
    where TDbItem : IEquatable<TDbItem>
{
    private readonly Dictionary<TItem, TDbItem> _original = new();
    private readonly HashSet<TItem> _currentItems = new();
    private readonly Func<TItem, TDbItem> _toDbItem;

    private List<TItem>? _added;
    private List<TItem>? _removed;

    public int Count => _currentItems.Count;

    public TrackedSet(IEnumerable<TDbItem> dbItems,
        Func<TItem, TDbItem> toDbItem,
        Func<TDbItem, TItem> toItem)
    {
        foreach (var dbItem in dbItems)
        {
            var item = toItem(dbItem);
            _original.Add(item, dbItem);
            _currentItems.Add(item);
        }
        _toDbItem = toDbItem;
    }

    public void Add(TItem item)
    {
        if (!_currentItems.Add(item))
            return;
        if (_original.ContainsKey(item))
            return;
        _added ??= new List<TItem>();
        _added.Add(item);
    }

    public void Remove(TItem item)
    {
        if (!_currentItems.Remove(item))
            return;
        _removed ??= new List<TItem>();
        _removed.Add(item);
    }

    public Diff GetDiff() => new(Added, Updated, Removed);

    private IEnumerable<TDbItem> Added => _added is null 
        ? Enumerable.Empty<TDbItem>() 
        : _added.Select(_toDbItem);

    private IEnumerable<TDbItem> Updated
    {
        get
        {
            foreach (var currentItem in _currentItems)
            {
                if (!_original.TryGetValue(currentItem, out var originalDbItem))
                    continue;
                var currentDbItem = _toDbItem(currentItem);
                if (!currentDbItem.Equals(originalDbItem))
                    yield return currentDbItem;
            }
        }
    }

    private IEnumerable<TDbItem> Removed => _removed is null 
        ? Enumerable.Empty<TDbItem>() 
        : _removed.Select(item => _original[item]);

    IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();

    public IEnumerator<TItem> GetEnumerator() => _currentItems.GetEnumerator();

    public bool Contains(TItem item) => _currentItems.Contains(item);

    public bool IsProperSubsetOf(IEnumerable<TItem> other) => _currentItems.IsProperSubsetOf(other);

    public bool IsProperSupersetOf(IEnumerable<TItem> other) => _currentItems.IsProperSupersetOf(other);

    public bool IsSubsetOf(IEnumerable<TItem> other) => _currentItems.IsSubsetOf(other);

    public bool IsSupersetOf(IEnumerable<TItem> other) => _currentItems.IsSupersetOf(other);

    public bool Overlaps(IEnumerable<TItem> other) => _currentItems.Overlaps(other);

    public bool SetEquals(IEnumerable<TItem> other) => _currentItems.SetEquals(other);

    public record Diff(IEnumerable<TDbItem> Added,
        IEnumerable<TDbItem> Updated,
        IEnumerable<TDbItem> Removed);
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Persistence.RepoDb/AssemblyInfo.cs`
```csharp
using NoesisVision.Annotations;

[assembly: ExcludeFromDocs]
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Persistence.RepoDb/DbRootEntity.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.Persistence.RepoDb;

public interface DbRootEntity<out TId>
{
    TId Id { get; }
    int Version { get; }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Persistence.RepoDb/RootEntityData.cs`
```csharp
using System.Data;
using RepoDb;

namespace MyCompany.ECommerce.TechnicalStuff.Persistence.RepoDb;

public abstract class RootEntityData<TDbEntity, TId>
    where TDbEntity : class, DbRootEntity<TId>
    where TId : notnull
{
    private readonly TDbEntity? _originalDbEntity;
    private bool _isSaved;
    
    protected RootEntityData(TDbEntity? originalDbEntity) => _originalDbEntity = originalDbEntity;

    public async Task Save(IDbTransaction transaction)
    {
        if (_isSaved)
            throw new DesignError("Can not save root db entity twice");
        if (_originalDbEntity is null)
            await SaveNewEntity(transaction);
        else
            await UpdateExistingEntity(transaction);
        _isSaved = true;
    }

    private async Task SaveNewEntity(IDbTransaction transaction)
    {
        var currentDbEntity = ToDbEntity(0);
        await transaction.Connection.InsertAsync(currentDbEntity, transaction: transaction);
        await SaveNestedDbEntities(transaction);
    }
    
    private async Task UpdateExistingEntity(IDbTransaction transaction)
    {
        var currentDbEntity = ToDbEntity(_originalDbEntity!.Version + 1);
        var rowsAffected = await transaction.Connection.UpdateAsync(currentDbEntity,
            where: new QueryField[]
            {
                new(nameof(DbRootEntity<TId>.Id), _originalDbEntity.Id),
                new(nameof(DbRootEntity<TId>.Version), _originalDbEntity.Version)
            },
            transaction: transaction);
        if (rowsAffected == 0)
            throw new OptimisticLockException();
        if (rowsAffected > 1)
            throw new DesignError("More than one row affected when updating root entity - check where clause");
        await SaveNestedDbEntities(transaction);
    }

    protected abstract TDbEntity ToDbEntity(int version);

    protected abstract Task SaveNestedDbEntities(IDbTransaction transaction);
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Persistence.RepoDb/TechnicalStuff.Persistence.RepoDb.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
        <AssemblyName>MyCompany.ECommerce.TechnicalStuff.Persistence.RepoDb</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.TechnicalStuff.Persistence.RepoDb</RootNamespace>
    </PropertyGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
      <PackageReference Include="RepoDb" Version="1.13.1" />
    </ItemGroup>

    <ItemGroup>
      <ProjectReference Include="..\TechnicalStuff.Persistence\TechnicalStuff.Persistence.csproj" />
      <ProjectReference Include="..\TechnicalStuff\TechnicalStuff.csproj" />
    </ItemGroup>

</Project>
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Postgres/AssemblyInfo.cs`
```csharp
using NoesisVision.Annotations;

[assembly: ExcludeFromDocs]
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Postgres/PostgresConnectionProvider.cs`
```csharp
﻿using System.Data.Common;
using MyCompany.ECommerce.TechnicalStuff.Persistence;
using Npgsql;

namespace MyCompany.ECommerce.TechnicalStuff.Postgres;

// TODO: Upgrade to Npgsql 7.x when possible (now Marten is incompatible) and use NpgsqlDataSource
//  https://www.npgsql.org/doc/basic-usage.html#connections
public class PostgresConnectionProvider : DbConnectionProvider, IDisposable, IAsyncDisposable
{
    protected readonly string _connectionString;
    private List<NpgsqlConnection>? _oneOffConnections;

    protected PostgresConnectionProvider(string connectionString) => _connectionString = connectionString;

    public async Task<DbConnection> CreateOneOffConnection()
    {
        var connection = new NpgsqlConnection(_connectionString);
        await connection.OpenAsync();
        _oneOffConnections ??= new List<NpgsqlConnection>();
        _oneOffConnections.Add(connection);
        return connection;
    }

    public virtual void Dispose()
    {
        if (_oneOffConnections is not null)
            foreach (var connection in _oneOffConnections)
                connection.Dispose();
    }

    public virtual async ValueTask DisposeAsync()
    {
        if (_oneOffConnections is not null)
            foreach (var connection in _oneOffConnections)
                await connection.DisposeAsync();
    }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Postgres/PostgresTransactionProvider.cs`
```csharp
using System.Data;
using System.Data.Common;
using MyCompany.ECommerce.TechnicalStuff.Persistence;
using Npgsql;

namespace MyCompany.ECommerce.TechnicalStuff.Postgres;

public class PostgresTransactionProvider : PostgresConnectionProvider, DbTransactionProvider
{
    private const string NoOpenTransaction =
        $"There are no open transaction - open it using {nameof(BeginTransaction)} method";

    private Stack<NpgsqlTransaction>? _transactions;

    protected PostgresTransactionProvider(string connectionString) : base(connectionString)
    {
    }

    public async Task BeginTransaction(IsolationLevel level = IsolationLevel.ReadCommitted)
    {
        var connection = new NpgsqlConnection(_connectionString);
        await connection.OpenAsync();
        var transaction = await connection.BeginTransactionAsync(level);
        _transactions ??= new Stack<NpgsqlTransaction>();
        _transactions.Push(transaction);
    }

    public DbTransaction GetCurrentTransaction()
    {
        if (_transactions is null)
            throw new DesignError(NoOpenTransaction);
        var transaction = _transactions.Peek();
        if (transaction is null)
            throw new DesignError(NoOpenTransaction);
        return transaction;
    }

    public async Task CommitCurrentTransaction()
    {
        if (_transactions is null)
            throw new DesignError(NoOpenTransaction);
        var transaction = _transactions.Pop();
        if (transaction is null)
            throw new DesignError(NoOpenTransaction);
        await transaction.CommitAsync();
        await transaction.DisposeAsync();
        await transaction.Connection!.DisposeAsync();
    }
        
    public async Task RollbackCurrentTransaction()
    {
        if (_transactions is null)
            throw new DesignError(NoOpenTransaction);
        var transaction = _transactions.Pop();
        if (transaction is null)
            throw new DesignError(NoOpenTransaction);
        await transaction.RollbackAsync();
        await transaction.DisposeAsync();
        await transaction.Connection!.DisposeAsync();
    }
        
    public override void Dispose()
    {
        base.Dispose();
        if (_transactions is not null)
            foreach (var transaction in _transactions)
                transaction.Dispose();
    }

    public override async ValueTask DisposeAsync()
    {
        await base.DisposeAsync();
        if (_transactions is not null)
            foreach (var transaction in _transactions)
                await transaction.DisposeAsync();
    }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Postgres/TechnicalStuff.Postgres.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <AssemblyName>MyCompany.ECommerce.TechnicalStuff.Postgres</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.TechnicalStuff.Postgres</RootNamespace>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
    </PropertyGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
      <PackageReference Include="Npgsql" Version="8.0.3" />
    </ItemGroup>

    <ItemGroup>
      <ProjectReference Include="..\TechnicalStuff.Persistence\TechnicalStuff.Persistence.csproj" />
      <ProjectReference Include="..\TechnicalStuff\TechnicalStuff.csproj" />
    </ItemGroup>

</Project>
```

## File: `Sources/TechnicalStuff/TechnicalStuff.ProcessModel/AssemblyInfo.cs`
```csharp
using NoesisVision.Annotations;

[assembly: ExcludeFromDocs]
```

## File: `Sources/TechnicalStuff/TechnicalStuff.ProcessModel/Command.cs`
```csharp
﻿namespace MyCompany.ECommerce.TechnicalStuff.ProcessModel;

public interface Command : Message { }
```

## File: `Sources/TechnicalStuff/TechnicalStuff.ProcessModel/CommandHandler.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.ProcessModel;

public interface CommandHandler<in TCommand> : MessageHandler
    where TCommand : Command
{
    Task MessageHandler.Handle(Message message)
    {
        if (!(message is TCommand command))
            throw new DesignError($"{message.GetType().Name} in incompatible with {GetType().Name}");
        return Handle(command);
    }

    Task Handle(TCommand command);
}

public interface CommandHandler<in TCommand, TResult> : CommandHandler<TCommand>
    where TCommand : Command
{
    Task CommandHandler<TCommand>.Handle(TCommand command) => Handle(command);

    new Task<TResult> Handle(TCommand command);
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.ProcessModel/DomainEvent.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.ProcessModel;

public interface DomainEvent : Message { }
```

## File: `Sources/TechnicalStuff/TechnicalStuff.ProcessModel/DomainEventHandler.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.ProcessModel;

public interface DomainEventHandler<in TEvent> : MessageHandler
    where TEvent : DomainEvent
{
    Task MessageHandler.Handle(Message message)
    {
        if (!(message is TEvent domainEvent))
            throw new DesignError($"{message.GetType().Name} in incompatible with {GetType().Name}");
        return Handle(domainEvent);
    }
        
    Task Handle(TEvent domainEvent);
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.ProcessModel/Message.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.ProcessModel;

public interface Message { }
```

## File: `Sources/TechnicalStuff/TechnicalStuff.ProcessModel/MessageHandler.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.ProcessModel;

public interface MessageHandler
{
    Task Handle(Message message);
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.ProcessModel/MessageTypes.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.ProcessModel;

public class MessageTypes
{
    private readonly Dictionary<string, Type> _id2Type = new();
    private readonly Dictionary<Type, string> _type2Id = new();

    public void Register<TMessage>(string typeId, IReadOnlyCollection<string> alternativeTypeIds)
        where TMessage : Message
    {
        if (_id2Type.ContainsKey(typeId))
            ThrowDuplicatedTypeId(typeId, typeof(TMessage));
        foreach (var alternativeTypeId in alternativeTypeIds)
        {
            if (_id2Type.ContainsKey(alternativeTypeId))
                ThrowDuplicatedTypeId(alternativeTypeId, typeof(TMessage));
        }
        if (_type2Id.ContainsKey(typeof(TMessage)))
            throw new DesignError($"Duplicated type registration for {typeof(TMessage).Name}");
            
        _id2Type.Add(typeId, typeof(TMessage));
        foreach (var alternativeTypeId in alternativeTypeIds)
            _id2Type.Add(alternativeTypeId, typeof(TMessage));
        _type2Id.Add(typeof(TMessage), typeId);
    }

    private void ThrowDuplicatedTypeId(string typeId, Type typeToRegister)
    {
        var alreadyRegisteredType = _id2Type[typeId];
        throw new DesignError($"Duplicated type id for {typeToRegister.Name} and {alreadyRegisteredType.Name}");
    }

    public string GetTypeIdFor<TMessage>(TMessage message)
    {
        if (!_type2Id.TryGetValue(typeof(TMessage), out var typeId))
            throw new DesignError($"Missing type id for: {typeof(TMessage).Name}");
        return typeId;
    }

    public Type GetMessageTypeFor(string typeId)
    {
        if (!_id2Type.TryGetValue(typeId, out var type))
            throw new DesignError($"Missing type for type id: {typeId}");
        return type;
    }

    public Type GetHandlerTypeFor(string typeId)
    {
        if (!_id2Type.TryGetValue(typeId, out var type))
            throw new DesignError($"Missing handler type for type id: {typeId}");
        return type;
    }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.ProcessModel/Query.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.ProcessModel;

public interface Query { }
```

## File: `Sources/TechnicalStuff/TechnicalStuff.ProcessModel/QueryHandler.cs`
```csharp
namespace MyCompany.ECommerce.TechnicalStuff.ProcessModel;

public interface QueryHandler<in TQuery, TResult>
    where TQuery : Query
{
     Task<TResult> Handle(TQuery query);
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.ProcessModel/TechnicalStuff.ProcessModel.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <AssemblyName>MyCompany.ECommerce.TechnicalStuff.ProcessModel</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.TechnicalStuff.ProcessModel</RootNamespace>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
    </PropertyGroup>

    <ItemGroup>
      <ProjectReference Include="..\TechnicalStuff\TechnicalStuff.csproj" />
    </ItemGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>

</Project>
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Transactions/AmbientTransactionDecorator.cs`
```csharp
using System.Transactions;
using JetBrains.Annotations;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.TechnicalStuff.Transactions;

[PublicAPI]
public class AmbientTransactionDecorator<TCommand>(CommandHandler<TCommand> decorated) : CommandHandler<TCommand>
    where TCommand : struct, Command
{
    public async Task Handle(TCommand command)
    {
        using var scope = new TransactionScope(
            TransactionScopeOption.RequiresNew,
            new TransactionOptions {IsolationLevel = IsolationLevel.ReadCommitted},
            TransactionScopeAsyncFlowOption.Enabled);
        await decorated.Handle(command);
        scope.Complete();
    }
}
    
[PublicAPI]
public class AmbientTransactionDecorator<TCommand, TResult>(CommandHandler<TCommand, TResult> decorated)
    : CommandHandler<TCommand, TResult>
    where TCommand : struct, Command
{
    public async Task<TResult> Handle(TCommand command)
    {
        using var scope = new TransactionScope(
            TransactionScopeOption.RequiresNew,
            new TransactionOptions {IsolationLevel = IsolationLevel.ReadCommitted},
            TransactionScopeAsyncFlowOption.Enabled);
        var result = await decorated.Handle(command);
        scope.Complete();
        return result;
    }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Transactions/AssemblyInfo.cs`
```csharp
using NoesisVision.Annotations;

[assembly: ExcludeFromDocs]
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Transactions/ExplicitTransactionDecorator.cs`
```csharp
using JetBrains.Annotations;
using MyCompany.ECommerce.TechnicalStuff.Persistence;
using MyCompany.ECommerce.TechnicalStuff.ProcessModel;

namespace MyCompany.ECommerce.TechnicalStuff.Transactions;

[PublicAPI]
public class ExplicitTransactionDecorator<TCommand>(CommandHandler<TCommand> decorated, MainDb db)
    : CommandHandler<TCommand>
    where TCommand : struct, Command
{
    public async Task Handle(TCommand command)
    {
        await db.BeginTransaction();
        try
        {
            await decorated.Handle(command);
            await db.CommitCurrentTransaction();
        }
        catch (Exception)
        {
            await db.RollbackCurrentTransaction();
            throw;
        }
    }
}

[PublicAPI]
public class ExplicitTransactionDecorator<TCommand, TResult>(CommandHandler<TCommand, TResult> decorated, MainDb db)
    : CommandHandler<TCommand, TResult>
    where TCommand : struct, Command
{
    public async Task<TResult> Handle(TCommand command)
    {
        await db.BeginTransaction();
        try
        {
            var result = await decorated.Handle(command);
            await db.CommitCurrentTransaction();
            return result;
        }
        catch (Exception)
        {
            await db.RollbackCurrentTransaction();
            throw;
        }
    }
}
```

## File: `Sources/TechnicalStuff/TechnicalStuff.Transactions/TechnicalStuff.Transactions.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <AssemblyName>MyCompany.ECommerce.TechnicalStuff.Transactions</AssemblyName>
        <RootNamespace>MyCompany.ECommerce.TechnicalStuff.Transactions</RootNamespace>
        <LangVersion>latest</LangVersion>
        <Nullable>enable</Nullable>
        <ImplicitUsings>true</ImplicitUsings>
    </PropertyGroup>

    <ItemGroup>
      <PackageReference Include="JetBrains.Annotations" Version="2025.2.2" />
      <PackageReference Include="NoesisVision.Annotations" Version="0.1.0" />
    </ItemGroup>

    <ItemGroup>
      <ProjectReference Include="..\TechnicalStuff.Persistence\TechnicalStuff.Persistence.csproj" />
      <ProjectReference Include="..\TechnicalStuff.ProcessModel\TechnicalStuff.ProcessModel.csproj" />
    </ItemGroup>

</Project>
```


---
id: repo-fetched-bio.cs-040900
type: knowledge
owner: OA
registered_at: 2026-04-05T03:54:41.935022
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_Bio.cs_040900

## Assimilation Report
Auto-cloned repository: FETCHED_Bio.cs_040900

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# BioLib (*Bio.cs*)

A helper library used in most of my C# projects.

The main purpose of this library is speeding up the development of command line applications by providing functions for common tasks, as well as ensuring consistency in terms of UX.

## Installation

Install the package [Bioruebe.BioLib](https://www.nuget.org/packages/Bioruebe.BioLib/) with NuGet.

## Library functions

- Command line interface helpers: prompts, progress display, functions for common tasks
- File I/O:
  - Automatic overwrite prompts
  - Path validation
- Working with binary data and streams: pattern search, copy, split, dump to file
- Logging: pretty console outputs for many file types
```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for bio_cs
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: docs\CHANGELOG.md
```md
# Changelog

## 2.5.0

- Added `FileCreate`, `FileFindBySubDirectory`, `ProgressPartial`, `Repeat`, `RandomByteArray` and `Xor`
- Added `Debug` overload to pretty-print byte arrays
- Added `MISSING_FILE` exitcode
- Added `Read8BitPrefixedString` and `Skip8BitPrefixedString` to `BinaryReaderExtensions`
- Added `RemainingLength`, `Back`, `IsExecutable` and `Matches` to `StreamExtensions`
- Added `Find` overload, which accepts a string pattern, to `StreamExtensions`
- Changed `BytesToString`:
  - Added parameter to specify encoding
  - Added parameter to ignore trailing zero bytes
- Changed `Cout`: added parameter to prevent appending a newline character
- Fixed `Cout`: some messages with a `DEBUG` log severity were printed in release version
- Fixed `Debug` without parameters printing text instead of a raw newline
- Fixed crash in `StreamExtensions.WriteToFileRelative`

## 2.4.0

- Added `BytesToString`, `PathAppendSeparator`, `PathRemoveLeadingSeparator` and `PathRemoveTrailingSeparator`
- Added `IsAtStart`, `IsAtEnd`, `FindAll` and `ToUtf8String` to `StreamExtensions`
- Added `StringExtensions` class
- Changed `CreateFile`: made `promptId` optional
- Changed `PrintNumbers`: if the array is empty, `<empty>` is now displayed
- Changed `HexDump` to display a message, if the end of the stream was reached
- Changed `StreamExtensions.WriteToFile` to always write the whole stream to file, ignoring the current position; added `WriteToFileRelative` to save the content from the current position
- Fixed `PathReplaceInvalidChars` and `PathReplaceInvalidFileNameChars`: control characters are now removed
- Fixed `PathGetDirectory` not working correctly for relative paths

## 2.3.2

- Fixed crash in `FileSetTimes` if the file path is invalid

## 2.3.1

- Fixed crash if file names contain certain special characters
- Fixed crash in `Progress` and `Cout` functions if message contains certain special characters

## 2.3.0

- Added `CreateFile` and `FileSetTimes`
- Added `Concatenate` overload accepting an array of streams to `StreamExtensions`
- Changed `Tout`: the function can now be called without parameters

## 2.2.0

- Added options `CoutPrintTime` and `CoutKeepLog` to allow global console output configuration
- Added `RandomInt`, `HexToBytes`, `PrintTime` and `CoutGetLog` functions to main class
- Added I/O helper functions `PathContainsInvalidChars`, `PathExists`, `PathGetDirectory`, `FileDelete`, `CreateDirectoryStructure` and `IsDirectory`

## 2.1.0

- Added `ConcatenatedStream` and `OffsetStream` classes
- Added `Concatenate` and `ToByteArray` functions to `StreamExtensions`
- Added `Tout` (`Cout` with prepended timestamp)
- Added `Debug` overload which allows a dynamic amount of parameters
- Fixed RNG initialization in `RandomArray` (affects `RandomStream` as well)
- Fixed `StreamExtensions.Copy` not copying the whole stream if the position is not zero
- Fixed `StreamExtensions.Copy` returning `Stream` instead of `MemoryStream`

## 2.0.0

[Breaking changes](UPGRADE_V1_V2.md)

- Added many new extension methods for `Stream` and `BinaryReader` classes (namespace `BioLib.Streams`)
- Added file/path helper functions:
  - `GetSafeOutputPath`
  - `PathRemoveRelativeParts`
  - `FileOpen`
  - `FileMove`
  - `DirectoryIsEmpty`
- Added `HexDump` helper function and overloads for `Cout` to pretty-print streams and byte arrays automatically
- Added `RandomStream` function
- Added `ProgressWithoutDuplicates`
- Added support for .NET Framework 4.0
- Fixed `FileReplaceInvalidChars`: invalid characters in file names (such as `?`) were not replaced

## 1.0.0

Initial release
```

### File: docs\UPGRADE_V1_V2.md
```md
# Upgrade guide 1.x to 2.x

## Breaking changes
##### Bio.FileReplaceInvalidChars

...has been renamed to `PathReplaceInvalidChars`.

A third parameter `isDirectory` is now required, which decides whether or not to replace characters that are only invalid in file names, but allowed in paths (such as `:` or `?`).

See `GetSafeOutputPath` for another way to ensure valid paths.


##### Bio.CopyStream

Removed. Use the extension method instead:

```C#
using BioLib.Streams;
myStream.Copy(otherStream);
```

The parameter `keepPosition` has been removed to keep function complexity low. Use a closure instead:

``` c#
myStream.KeepPosition(() => myStream.Copy(otherStream));
```


##### Bio.Seperator

Renamed. Use the correctly spelled Bio.Separator instead.


##### Public constants

Removed. Prompt-related constants have been moved to `PromptInput` class.
```


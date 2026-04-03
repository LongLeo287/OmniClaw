---
id: icsharpcode-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:53.038226
---

# KNOWLEDGE EXTRACT: icsharpcode
> **Extracted on:** 2026-03-30 17:38:09
> **Source:** icsharpcode

---

## File: `SharpZipLib.md`
```markdown
# 📦 icsharpcode/SharpZipLib [🔖 PENDING/APPROVE]
🔗 https://github.com/icsharpcode/SharpZipLib
🌐 http://icsharpcode.github.io/SharpZipLib/

## Meta
- **Stars:** ⭐ 3911 | **Forks:** 🍴 1005
- **Language:** C# | **License:** MIT
- **Last updated:** 2026-03-20
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
#ziplib is a Zip, GZip, Tar and BZip2 library written entirely in C# for the .NET platform.

## README (trích đầu)
```
# SharpZipLib [![Build Status](https://github.com/icsharpcode/SharpZipLib/actions/workflows/build-test.yml/badge.svg?branch=master)](https://github.com/icsharpcode/SharpZipLib/actions/workflows/build-test.yml) [![NuGet Version](https://img.shields.io/nuget/v/SharpZipLib.svg)](https://www.nuget.org/packages/SharpZipLib/) [![openupm](https://img.shields.io/npm/v/org.icsharpcode.sharpziplib?label=openupm&registry_uri=https://package.openupm.com)](https://openupm.com/packages/org.icsharpcode.sharpziplib/)

Introduction
------------

SharpZipLib (\#ziplib, formerly NZipLib) is a compression library that supports Zip files using both stored and deflate compression methods, PKZIP 2.0 style and AES encryption, tar with GNU long filename extensions, GZip, zlib and raw deflate, as well as BZip2. Zip64 is supported while Deflate64 is not yet supported. It is implemented as an assembly (installable in the GAC), and thus can easily be incorporated into other projects (in any .NET language). The creator of SharpZipLib put it this way: "I've ported the zip library over to C\# because I needed gzip/zip compression and I didn't want to use libzip.dll or something like this. I want all in pure C\#."

SharpZipLib was originally ported from the [GNU Classpath](http://www.gnu.org/software/classpath/) java.util.zip library for use with [SharpDevelop](http://www.icsharpcode.net/OpenSource/SD), which needed gzip/zip compression. bzip2 compression and tar archiving were added later due to popular demand.

The [SharpZipLib homepage](http://icsharpcode.github.io/SharpZipLib/) has precompiled libraries available for download, [API documentation](https://icsharpcode.github.io/SharpZipLib/help/api/index.html), [release history](https://github.com/icsharpcode/SharpZipLib/wiki/Release-History), samples and more.

License
-------

This software is now released under the [MIT License](https://opensource.org/licenses/MIT). Please see [issue #103](https://github.com/icsharpcode/SharpZipLib/issues/103) for more information on the relicensing effort.

Previous versions were released under the [GNU General Public License, version 2](http://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html) with an [exception](http://www.gnu.org/software/classpath/license.html) which allowed linking with non-GPL programs.

Namespace layout
----------------

| Module | Namespace |
|:----------------:|:-----------------------------|
|BZip2 implementation|ICSharpCode.SharpZipLib.BZip2.\*|
|Checksum implementation|ICSharpCode.SharpZipLib.Checksum.\*|
|Core utilities / interfaces|ICSharpCode.SharpZipLib.Core.\*|
|Encryption implementation|ICSharpCode.SharpZipLib.Encryption.\*|
|GZip implementation|ICSharpCode.SharpZipLib.GZip.\*|
|LZW implementation|ICSharpCode.SharpZipLib.Lzw.\*|
|Tar implementation|ICSharpCode.SharpZipLib.Tar.\*|
|ZIP implementation|ICSharpCode.SharpZipLib.Zip.\*|
|Inflater/Deflater|ICSharpCode.SharpZipLib.Zip.Compression.\*|
|Inflater/Deflater streams|ICSharpCode.SharpZipLib.Zip.Compress
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


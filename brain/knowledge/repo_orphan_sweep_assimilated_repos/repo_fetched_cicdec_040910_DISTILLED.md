---
id: repo-fetched-cicdec-040910
type: knowledge
owner: OA
registered_at: 2026-04-05T04:13:21.641111
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_cicdec_040910

## Assimilation Report
Auto-cloned repository: FETCHED_cicdec_040910

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# cicdec
Extract files from installers made with Clickteam Install Creator.

### Usage

`cicdec [<options>...] <installer> [<output_directory>]`

If no output directory is specified, all files are extracted to a subdirectory named after the input file.

##### Options

| Switch       | Description                                                  |
| ------------ | ------------------------------------------------------------ |
| -v <version> | Extract as installer version <version>. Auto-detection might not always work correctly, so it is possible to explicitly set the installer version. Possible values are `20`, `24`, `30`, `35`, `40` |
| -db        | Dump blocks. Save additional installer data like registry changes, license files and the uninstaller. This is considered raw data and might not be readable or usable. |
| -dfb       | Dump file block. This is raw binary data containing all files in compressed form and only useful for debugging purposes. |
| -si          | Simulate extraction without writing files to disk. Useful for debugging. |



### Limitations

- Installers, which contain multiple product versions, are not supported
	- This includes official Clickteam products, such as the Install Creator and Patch Maker installers themselves
- Encrypted installers are not supported
- Installer versions below 2.0.0.20 are untested and might not be supported. Please open an issue if you encounter an installer, which fails to extract
```

### File: changelog.txt
```txt
3.0.1
  Updated BioLib to 2.5.0

3.0.0
  Added support for another installer version
  Added '-dfb' command line parameter to extract file data block
  Changed '-db' command line parameter to not extract the file block per default
  Fixed crash if the installer contains unknown data blocks
  Fixed crash when using the '-si' command line option
  Improved installer version detection
  Updated BioLib to 2.3.2
  Updated SharpZipLib to 1.3.3

2.3.0
  Added support for installers containing files bigger than ~2 GB
  Fixed extraction for installers with more than one data file
  Reduced memory usage during extraction
  Updated BioLib to 2.3.0

2.2.0
  Added support for another installer version, thanks to sjkorvin
  Updated BioLib to 2.2.0

2.1.2
  Fixed extraction failure of some installers with data files

2.1.1
  Fixed version detection for some installers
  Updated BioLib to 2.0.0

2.1.0
  Added 'Overwrite file?' prompt if output file already exists
  Moved common functions to separate dll

2.0.0
  Added support for installer version 2.0.0.20
  Added command line parameter to explicitly set the installer version instead of auto-detecting it
  Fixed files being skipped if their names contain certain non-ASCII characters
  Fixed extraction for installers with big external data files
  Improved detetion of installer version

1.1.0
  Added support for installers with external data files

1.0.1
  Fixed crash if the installer contains dummy files

1.0.0
  Initial release
```

### File: cicdec\FileInfo.cs
```cs
﻿using System;
using BioLib;

namespace cicdec {
	public class FileInfo {
		public long nodeStart;
		public uint nodeSize;
		public long nodeEnd;
		public ushort type;
		public uint compressedSize;
		public uint offset;
		public uint unknown32;
		public uint uncompressedSize;
		public uint index;
		public string path;
		public DateTime modified;
		public DateTime accessed;
		public DateTime created;

		public FileInfo(long nodeStart, uint nodeSize, ushort type) {
			SetNodeInfos(nodeStart, nodeSize);
			this.type = type;
		}

		public FileInfo(ushort type, uint offset, uint compressedSize, uint unknown32, uint uncompressedSize) {
			this.type = type;
			this.compressedSize = compressedSize;
			this.offset = offset;
			this.unknown32 = unknown32;
			this.uncompressedSize = uncompressedSize;
		}

		public void SetFileInfos(uint offset, uint compressedSize, uint unknown32, uint uncompressedSize) {
			this.compressedSize = compressedSize;
			this.offset = offset;
			this.unknown32 = unknown32;
			this.uncompressedSize = uncompressedSize;
		}

		public void SetNodeInfos(long startPos, uint size) {
			nodeStart = startPos;
			nodeSize = size;
			nodeEnd = nodeStart + nodeSize;
		}

		public void SetFileTimes(long modified, long accessed, long created) {
			try {
				this.modified = DateTime.FromFileTime(modified);
				this.accessed = DateTime.FromFileTime(accessed);
				this.created = DateTime.FromFileTime(created);
			}
			catch (Exception) {
				Bio.Debug("Failed to parse file time");
			}
		}

		public bool IsValid(long fileStreamLength) {
			if (offset > fileStreamLength
			|| (compressedSize == 0 && uncompressedSize > 3000000000)
			|| (uncompressedSize > 10 && compressedSize > 10 && compressedSize > uncompressedSize * 5)
			|| index > 1000000000
			|| Bio.PathContainsInvalidChars(path)) return false;

			return true;
		}

		public override string ToString() {
			return string.Format("File {0}, type: {1:x} at {2}: {3} -> {4}, path: {5}", index, type, offset,
				compressedSize, uncompressedSize, path);
		}
	}
}
```

### File: cicdec\Program.cs
```cs
﻿using System;
using System.Collections.Generic;
using System.IO;
using System.IO.Compression;
using System.Linq;
using System.Text;
using ICSharpCode.SharpZipLib;
using ICSharpCode.SharpZipLib.BZip2;
using BioLib;
using BioLib.Streams;

namespace cicdec {
	class Program {
		private const string VERSION = "3.0.1";
		private const string PROMPT_ID = "cicdec_overwrite";

		private const int BLOCK_HEADER_SIZE = 16 + 16 + 32;
		private static readonly byte[] DATA_SECTION_SIGNATURE = {0x77, 0x77, 0x67, 0x54, 0x29, 0x48};

		private static string inputFile;
		private static string outputDirectory;
		private static bool dumpBlocks;
		private static bool dumpFileBlock;
		private static bool simulate;
		private static int installerVersion = -1;

		private static Stream fileListStream;
		private static List<FileInfo> filesInfos;
		private static long dataBlockStartPosition = -1;
		private static int failedExtractions = 0;

		static void Main(string[] args) {
			const string USAGE = "[<options>...] <installer> [<output_directory>]\n\n" + 
								 "<options>:\n" + 
								 "  -v <version>\tExtract as installer version <version>. Auto-detection might not always work correctly, so it is possible to explicitly set the installer version.\n\n" + 
								 "  -db\tDump blocks. Save additional installer data like registry changes, license files and the uninstaller. This is considered raw data and might not be readable or usable.\n\n" + 
								 "  -dfb\tDump file block. This is raw binary data containing all files in compressed form and only useful for debugging purposes.\n\n" + 
								 "  -si\tSimulate extraction without writing files to disk.";
			Bio.Header("cicdec - A Clickteam Install Creator unpacker", VERSION, "2019-2021", "Extracts files from installers made with Clickteam Install Creator", USAGE);
			
			inputFile = ParseCommandLine(args);
			var inputStream = File.OpenRead(inputFile);
			var binaryReader = new BinaryReader(inputStream);
			var inputStreamLength = inputStream.Length;

			// First we need to find the data section. The simplest way to do so
			// is searching for the signature 0x77, 0x77, 0x67, 0x54, 0x29, 0x48
			if (!inputStream.Find(DATA_SECTION_SIGNATURE)) Bio.Error("Failed to find overlay signature.", Bio.EXITCODE.INVALID_INPUT);
			inputStream.Skip(DATA_SECTION_SIGNATURE.Length);

			Bio.Cout("Starting extraction at offset " + inputStream.Position + "\n");

			// The data section consists of a varying number of data blocks,
			// whose headers give information about the type of data contained inside.
			while (inputStream.Position + BLOCK_HEADER_SIZE <= inputStreamLength) {
				var blockId = binaryReader.ReadUInt16();
				inputStream.Skip(2); // unknown
				var blockSize = binaryReader.ReadUInt32();
				var blockType = (BLOCK_TYPE) blockId;
				var nextBlockPos = inputStream.Position + blockSize;
				Bio.Cout(string.Format("Reading block 0x{0:X} {1,-16} with size {2}", blockId, (BLOCK_TYPE) blockId, blockSize));
				var outputFileName = string.Format("Block 0x{0:X} {1}.bin", blockId, (BLOCK_TYPE) blockId);

				if (blockType == BLOCK_TYPE.FILE_DATA) {
					// Data block should always be last, but better be safe and parse all other blocks before
					dataBlockStartPosition = inputStream.Position;
					
					if (dumpFileBlock) {
						using (var ms = inputStream.Extract((int)blockSize)) {
							SaveToFile(ms, outputFileName);
						}
					}

					continue;
				}
				else if (blockType == BLOCK_TYPE.FILE_LIST) {
					fileListStream = UnpackStream(binaryReader, blockSize);
					if (fileListStream == null) Bio.Error("Failed to decompress file list", Bio.EXITCODE.RUNTIME_ERROR);

					if (dumpBlocks) SaveToFile(fileListStream, outputFileName);

					fileListStream.MoveToStart();
				}
				else if (dumpBlocks) {
					using (var decompressedStream = UnpackStream(binaryReader, blockSize)) {
						SaveToFile(decompressedStream, outputFileName);
					}
				}

				Bio.Debug("Pos: " + inputStream.Position + ", expected: " + nextBlockPos);
				inputStream.Position = nextBlockPos;
			}

			if (fileListStream == null) Bio.Error("File list could not be read. Please send a bug report if you want the file to be supported in a future version.", Bio.EXITCODE.NOT_SUPPORTED);

			// Install Creator supports external data files, instead of integrating 
			// the files into the executable. This actually means the data block is
			// saved as a separate file, which we just need to read.
			var dataFiles = FindDataFiles();
			if (dataFiles.Count > 0) {
				using (var concatenatedStream = inputStream.Concatenate(dataFiles)) {
					Bio.Debug($"{dataFiles.Count - 1} data files read. Total length: {concatenatedStream.Length}");

					ParseFileList(fileListStream, concatenatedStream.Length);
					using (var concatenatedStreamBinaryReader = new BinaryReader(concatenatedStream)) {
						ExtractFiles(concatenatedStream, concatenatedStreamBinaryReader);
					}
				}
			}
			else if (dataBlockStartPosition < 0) {
				Bio.Error("Could not find data block in installer and there is no external data file. The installer is likely corrupt.", Bio.EXITCODE.RUNTIME_ERROR);
			}
			else {
				ParseFileList(fileListStream, inputStreamLength);
				ExtractFiles(inputStream, binaryReader);
			}

			if (failedExtractions > 0) {
				if (failedExtractions == filesInfos.Count) Bio.Error("Extraction failed. The installer is either encrypted or a version, which is currently not supported.", Bio.EXITCODE.NOT_SUPPORTED);
				Bio.Warn(failedExtractions + " files failed to extract.");
			}
			else {
				Bio.Cout("All OK");
			}

			Bio.Pause();
		}

		static List<Stream> FindDataFiles() {
			var directory = Path.GetDirectoryName(inputFile);
			var baseFileName = Path.GetFileNameWithoutExtension(inputFile);

			var i = 1;
			var dataFiles = new List<Stream>();

			while (true) {
				var dataFile = baseFileName + $".D{i:00}";
				var dataFilePath = Path.Combine(directory, dataFile);

				if (!File.Exists(dataFilePath)) break;

				Bio.Debug("Found data file " + dataFile);
				var dataFileStream = File.OpenRead(dataFilePath);
				var offsetStream = new OffsetStream(dataFileStream, 4);
				dataFiles.Add(offsetStream);

				i++;
			}

			return dataFiles;
		}

		static string ParseCommandLine(string[] args) {
			var count = args.Length - 1;
			if (count < 0) Bio.Error("No input file specified.", Bio.EXITCODE.INVALID_INPUT);

			var path = args[count];
			string inputFile;

			if (File.Exists(path)) {
				inputFile = path;
				outputDirectory = Path.Combine(Path.GetDirectoryName(path), Path.GetFileNameWithoutExtension(path));
			}
			else {
				outputDirectory = path;
				count--;
				if (count < 0) Bio.Error("Invalid input file specified.", Bio.EXITCODE.INVALID_INPUT);
				inputFile = args[count];
			}

			if (!File.Exists(inputFile)) Bio.Error("Invalid input file specified.", Bio.EXITCODE.IO_ERROR);

			for (var i = 0; i < count; i++) {
				var arg = args[i];
				Bio.Debug("Argument: " + arg);
				switch (arg) {
					case "--dump-blocks":
					case "-db":
						dumpBlocks = true;
						break;
					case "--dump-file-block":
					case "-dfb":
						dumpFileBlock = true;
						break;
					case "--simulate":
					case "-si":
						simulate = true;
						break;
					case "--version":
					case "-v":
						i++;
						if (i >= args.Length) Bio.Error("No installer version specified.", Bio.EXITCODE.INVALID_PARAMETER);

						try {
							installerVersion = Convert.ToInt32(args[i]);
						}
						catch (FormatException) {
							Bio.Error("Invalid installer version specified.", Bio.EXITCODE.INVALID_PARAMETER);
						}

						break;
					default:
						Bio.Warn("Unknown command line option: " + arg);
						break;
				}
			}

			Bio.Debug("Input file: " + inputFile);
			Bio.Debug("Output directory: " + outputDirectory);
			Bio.Debug("Dump blocks: " + dumpBlocks);

			return inputFile;
		}

		static int GetInstallerVersion(Stream decompressedStream, BinaryReader binaryReader, ushort fileNumber, long dataStreamLength) {
			if (installerVersion > -1) return installerVersion;

			if (TestInstallerVersion(40, TryParse40, decompressedStream, binaryReader, fileNumber, dataStreamLength)) return 40;
			if (TestInstallerVersion(35, TryParse35, decompressedStream, binaryReader, fileNumber, dataStreamLength)) return 35;
			if (TestInstallerVersion(30, TryParse30, decompressedStream, binaryReader, fileNumber, dataStreamLength)) return 30;
			if (TestInstallerVersion(24, TryParse24, decompressedStream, binaryReader, fileNumber, dataStreamLength)) return 24;
			if (TestInstallerVersion(20, TryParse20, decompressedStream, binaryReader, fileNumber, dataStreamLength)) return 20;

			Bio.Error($"Failed to determine installer version. Please send a bug report if you want the file to be supported in a future version.", Bio.EXITCODE.NOT_SUPPORTED);
			return -1;
		}

		static bool TestInstallerVersion(int version, Func<Stream, BinaryReader, FileInfo> parsingFunction, Stream decompressedStream, BinaryReader binaryReader, int fileNumber, long dataStreamLength) {
			Bio.Debug($"\nTesting installer version {version}\n");
			var pos = decompressedStream.Position;

			for (var i = 0; i < fileNumber; i++) {
				try {
					var fileInfo = parsingFunction(decompressedStream, binaryReader);

					Bio.Debug(string.Format("Node {0} at offset {1}, size: {2}, end: {3}", i, fileInfo.nodeStart, fileInfo.nodeSize, fileInfo.nodeEnd));

					if (!fileInfo.IsValid(dataStreamLength)) {
						Bio.Debug(fileInfo);
						Bio.Debug("Invalid file info");
						decompressedStream.Position = pos;
						return false;
					}

					if (fileInfo.type != 0) decompressedStream.Position = fileInfo.nodeEnd;
				}
				catch (EndOfStreamException) {
					Bio.Debug("End of Stream reached while parsing file list");
					decompressedStream.Position = pos;
					return false;
				}
			}

			decompressedStream.Position = pos;
			return true;
		}

		static Stream UnpackStream(BinaryReader binaryReader, uint blockSize, uint decompressedSize = 0, Stream decompressedStream = null) {
			if (decompressedSize == 0) decompressedSize = binaryReader.ReadUInt32();
			var compressionMethod = (COMPRESSION) binaryReader.ReadByte();
			Bio.Debug("Decompressing " + blockSize + " bytes @ " + binaryReader.BaseStream.Position);
			Bio.Debug(string.Format("\tCompression: {0:X}, decompressed size: {1}", compressionMethod, decompressedSize));
			blockSize -= 5;

			if (decompressedStream == null) {
				if (decompressedSize > int.MaxValue) {
					Bio.Warn("Block size exceeds limit. Skipping block.");
					binaryReader.BaseStream.Skip(blockSize);
					return null;
				}

				decompressedStream = new MemoryStream((int)decompressedSize);
			}

			switch (compressionMethod) {
				case COMPRESSION.NONE:
					binaryReader.BaseStream.Copy(decompressedStream, (int) blockSize);
					break;
				case COMPRESSION.DEFLATE:
					binaryReader.BaseStream.Skip(2);
					using (var deflateStream = new DeflateStream(binaryReader.BaseStream, CompressionMode.Decompress, true)) {
						deflateStream.Copy(decompressedStream, decompressedSize);
					}
					break;
				case COMPRESSION.BZ2:
					using (var bzip2Stream = new BZip2InputStream(binaryReader.BaseStream)) {
						bzip2Stream.IsStreamOwner = false;
						bzip2Stream.Copy(decompressedStream, decompressedSize);
					}
					break;
				default:
					Bio.Warn("Unknown compression method, data might be encrypted and cannot be unpacked. Skipping block.");
					decompressedStream.Dispose();
					binaryReader.BaseStream.Skip(blockSize);
					return null;
			}

			//binaryReader.BaseStream.Skip(blockSize);
			return decompressedStream;
		}

		static bool UnpackStreamToFile(string filePath, BinaryReader binaryReader, uint blockSize, uint decompressedSize = 0) {
			if (simulate) return true;

			using (var fileStream = Bio.CreateFile(filePath, PROMPT_ID)) {
				if (fileStream == null) return true;
				UnpackStream(binaryReader, blockSize, decompressedSize, fileStream);
			}

			return true;
		}

		static bool SaveToFile(Stream stream, string fileName, FileInfo fileInfo = null) {
			if (stream == null) {
				Bio.Warn("Failed to save stream to file. Stream is null");
				return false;
			}

			if (simulate) return true;

			stream.MoveToStart();
			var filePath = Bio.GetSafeOutputPath(outputDirectory, fileName);
			//Bio.Cout("Saving decompressed block to " + filePath);

			try {
				if (!stream.WriteToFile(filePath, PROMPT_ID)) return true;

				SetFileAttributes(filePath, fileInfo);
			}
			catch (Exception e) {
				Bio.Warn("Failed to create file: " + e.Message);
				return false;
			}

			return true;
		}

		static bool SetFileAttributes(string path, FileInfo fileInfo) {
			if (fileInfo == null || simulate) return false;

			Bio.FileSetTimes(path, fileInfo.created, fileInfo.accessed, fileInfo.modified);
			return true;
		}

		static void ParseFileList(Stream decompressedStream, long dataStreamLength) {
			var binaryReader  = new BinaryReader(decompressedStream);
			var fileNumber = binaryReader.ReadUInt16();
			filesInfos = new List<FileInfo>();
			decompressedStream.Skip(2); // Unknown. Maybe fileNumber is 4 bytes?
			Bio.Cout("\n" + fileNumber + " files in installer\n");

			installerVersion = GetInstallerVersion(decompressedStream, binaryReader, fileNumber, dataStreamLength);
			Func<Stream, BinaryReader, FileInfo> parsingFunction = null;
			if (installerVersion >= 40) {
				parsingFunction = TryParse40;
			}
			else if (installerVersion >= 35) {
				parsingFunction = TryParse35;
			}
			else if (installerVersion >= 30) {
				parsingFunction = TryParse30;
			}
			else if (installerVersion >= 24) {
				parsingFunction = TryParse24;
			}
			else if (installerVersion >= 20) {
				parsingFunction = TryParse20;
			}
			else {
				Bio.Error($"Unsupported installer version {installerVersion}. Please send a bug report if you want the file to be supported in a future version.", Bio.EXITCODE.NOT_SUPPORTED);
			}

			Bio.Cout($"\nStarting extraction as installer version {installerVersion}\n");
			for (var i = 0; i < fileNumber; i++) {
				var fileInfo = parsingFunction(decompressedStream, binaryReader);
				Bio.Debug(string.Format("Node {0} at offset {1}, size: {2}, end: {3}", i, fileInfo.nodeStart, fileInfo.nodeSize, fileInfo.nodeEnd));

				if (!fileInfo.IsValid(dataStreamLength)) {
					Bio.Debug(fileInfo);
					Bio.Error($"The file could not be extracted as installer version {installerVersion}. Please try to manually set the correct version using the command line switch -v.", Bio.EXITCODE.RUNTIME_ERROR);
				}

#if DEBUG
				if (dumpBlocks) {
					using (var ms = new MemoryStream((int) fileInfo.nodeSize)) {
						decompressedStream.Position = fileInfo.nodeStart;
						decompressedStream.Copy(ms, (int) fileInfo.nodeSize);
						decompressedStream.Position = fileInfo.nodeEnd;
						SaveToFile(ms, "FileMeta" + i + ".bin");
					}
				}
#endif

				if (fileInfo.type != 0) {
					decompressedStream.Position = fileInfo.nodeEnd;
					continue;
	
... [TRUNCATED]
```

### File: cicdec\Properties\AssemblyInfo.cs
```cs
﻿using System.Resources;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

// Allgemeine Informationen über eine Assembly werden über die folgenden
// Attribute gesteuert. Ändern Sie diese Attributwerte, um die Informationen zu ändern,
// die einer Assembly zugeordnet sind.
[assembly: AssemblyTitle("cicdec")]
[assembly: AssemblyDescription("Extract files from installers made with Clickteam Install Creator")]
[assembly: AssemblyConfiguration("")]
[assembly: AssemblyCompany("Bioruebe")]
[assembly: AssemblyProduct("cicdec")]
[assembly: AssemblyCopyright("Copyright © 2019-2023 William Engelmann")]
[assembly: AssemblyTrademark("")]
[assembly: AssemblyCulture("")]

// Durch Festlegen von ComVisible auf FALSE werden die Typen in dieser Assembly
// für COM-Komponenten unsichtbar.  Wenn Sie auf einen Typ in dieser Assembly von
// COM aus zugreifen müssen, sollten Sie das ComVisible-Attribut für diesen Typ auf "True" festlegen.
[assembly: ComVisible(false)]

// Die folgende GUID bestimmt die ID der Typbibliothek, wenn dieses Projekt für COM verfügbar gemacht wird
[assembly: Guid("da16b24d-57c6-48c3-ace3-94af36325ced")]

// Versionsinformationen für eine Assembly bestehen aus den folgenden vier Werten:
//
//      Hauptversion
//      Nebenversion
//      Buildnummer
//      Revision
//
// Sie können alle Werte angeben oder Standardwerte für die Build- und Revisionsnummern verwenden,
// übernehmen, indem Sie "*" eingeben:
// [assembly: AssemblyVersion("1.0.*")]
[assembly: AssemblyVersion("3.0.1.0")]
[assembly: AssemblyFileVersion("3.0.1.0")]
[assembly: NeutralResourcesLanguage("en")]

```


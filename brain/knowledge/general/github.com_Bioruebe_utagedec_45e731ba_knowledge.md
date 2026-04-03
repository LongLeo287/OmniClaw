---
id: github.com-bioruebe-utagedec-45e731ba-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:34.271068
---

# KNOWLEDGE EXTRACT: github.com_Bioruebe_utagedec_45e731ba
> **Extracted on:** 2026-04-01 13:09:09
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007522308/github.com_Bioruebe_utagedec_45e731ba

---

## File: `.gitignore`
```
/bin
```

## File: `LICENSE`
```
BSD 3-Clause License

Copyright (c) 2017, William Engelmann
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

## File: `Package.bat`
```
@echo off
cd bin
echo Creating standalone command line executable...
nekotools boot utagedec.n
pause
```

## File: `README.md`
```markdown
# utagedec
A simple decryptor for utage encrypted files (.utage)

### Usage
`utagedec <input_file>|<input_dir> [<output_dir>] [-k <decryption_key>]`

- Utagedec supports either a single file or a whole folder as input. In folder mode only files with one of 3 the allowed extensions is processed. Subdirectories are ++ignored++.
- The encryption/decryption key is needed to extract any file. Automatic detection is not supported yet. (I don't have enough sample games to test.) If no key is provided the engine's standard key is used to decrypt the files - this may or may not work for your game.

### Technical details

UTAGE encrypts assets using a modified XOR algorithm: if the input byte is either zero or the same as the next byte of the key, it is not touched (to prevent leaking the key in files with sequences of zero bytes). Otherwise, the byte is XOR-ed.
There are also functions to compress assets before encrypting and the possibility to overwrite the encryption code with a custom algorithm. Both are currently not supported by utagedec.

### Limitations

- UTAGE also supports compression of asset files, utagedec doesn't at the moment. So if the output is not useful, it may have been compressed (or the decryption key was wrong).
- The decryption key cannot be determined automatically yet.
- Games made with UTAGE can use a custom encryption algorithm. This may be different for each game, and is also not supported by utagedec.
- If you found a game, which is not supported, feel free to open an issue and send me a sample file.

### Remarks
This is the result of analysing the file type itself, no reverse engineering has been used to write this tool.

I released it as a helper for artists to search games for unlicensed use of their assets. It is not meant to encourage extraction with the sole purpose of using assets in your own products without permission of the copyright holder.

Remember: don't steal assets from other people's games. Respect copyrights. And don't protect your own games - it's unnecessary effort.
```

## File: `Run.bat`
```
@echo off
cd bin
neko utagedec.n
pause
```

## File: `utagedec.hxproj`
```
﻿<?xml version="1.0" encoding="utf-8"?>
<project version="2">
  <!-- Output SWF options -->
  <output>
    <movie outputType="Application" />
    <movie input="" />
    <movie path="bin\utagedec.n" />
    <movie fps="0" />
    <movie width="0" />
    <movie height="0" />
    <movie version="0" />
    <movie minorVersion="0" />
    <movie platform="Neko" />
    <movie background="#FFFFFF" />
  </output>
  <!-- Other classes to be compiled into your SWF -->
  <classpaths>
    <class path="src" />
  </classpaths>
  <!-- Build options -->
  <build>
    <option directives="" />
    <option flashStrict="False" />
    <option noInlineOnDebug="False" />
    <option mainClass="Main" />
    <option enabledebug="False" />
    <option additional="" />
  </build>
  <!-- haxelib libraries -->
  <haxelib>
    <library name="Bio" />
  </haxelib>
  <!-- Class files to compile (other referenced classes will automatically be included) -->
  <compileTargets>
    <compile path="src\Main.hx" />
  </compileTargets>
  <!-- Paths to exclude from the Project Explorer tree -->
  <hiddenPaths>
    <hidden path="obj" />
  </hiddenPaths>
  <!-- Executed before build -->
  <preBuildCommand />
  <!-- Executed after build -->
  <postBuildCommand alwaysRun="False" />
  <!-- Other project options -->
  <options>
    <option showHiddenPaths="False" />
    <option testMovie="Custom" />
    <option testMovieCommand="run.bat" />
  </options>
  <!-- Plugin storage -->
  <storage />
</project>
```

## File: `src/Main.hx`
```
package;

import haxe.Json;
import haxe.io.Bytes;
import sys.FileSystem;
import sys.io.File;

/**
 * ...
 * @author Bioruebe
 */
class Main {
	private static var files:Array<String>;
	
	static function main() {
		Bio.Header("utagedec", "1.0.0", "2017", "A simple decrypter for utage encrypted files (.utage)", "<input_file>|<input_dir> [<output_dir>] [-k <decrytion_key>]");
		Bio.Seperator();
		
		var args = Sys.args();
		if (args.length < 1) Bio.Error("Please specify an input path. This can either be a file or a directory containing .utage files.", 1);
		
		files = readInputFileArgument(args[0]);
		var keyArgPos = args.indexOf("-k");
		var outdir = args.length > 1 && args[1] != "-k"? Bio.PathAppendSeperator(args[1]): null;
		var encryptionKeyString = keyArgPos > 0? args[keyArgPos + 1]: "InputOriginalKey";
		var encryptionKey = Bytes.ofString(encryptionKeyString);
		Bio.Cout("Using decryption key " + encryptionKey.toHex());
		
		for (i in 0...files.length) {
			try {
				if (FileSystem.isDirectory(files[i])) continue;
				
				var fileParts = Bio.FileGetParts(files[i]);
				if (fileParts.extension != "utage"){
					Bio.Cout("Invalid extension '" + fileParts.extension + "' for file " + fileParts.name);
					continue;
				}
				
				var outFile = (outdir == null? fileParts.directory: outdir) + fileParts.name;
				if (FileSystem.exists(outFile) && !Bio.Prompt("The file " + fileParts.name + " already exists. Overwrite?", "OutOverwrite")) {
					Bio.Cout("Skipped file " + fileParts.fullName);
					continue;
				}
				
				var bytes = File.getBytes(files[i]);
				decryptXor(bytes, encryptionKey);
				
				File.saveBytes(outFile, bytes);
				Bio.Cout('${i + 1}/${files.length}\t${fileParts.name}');
			} catch (e:Dynamic) {
				Bio.Cout('${i + 1}/${files.length}\tFailed to read file', Bio.LogSeverity.ERROR);
			}
		}
		
		Bio.Cout("All OK");
	}
	
	private static function readInputFileArgument(file:String){
		if (!FileSystem.exists(file)) {
			Bio.Error("The input file " + file + " does not exist.", 1);
			return null;
		}
		else if (FileSystem.isDirectory(file)) {
			return FileSystem.readDirectory(file).map(function(s:String) {
				return Bio.PathAppendSeperator(file) + s;
			});
		}
		else {
			return [file];
		}
	}
	
	private static function decryptXor(data:Bytes, key:Bytes) {
		if (key == null || key.length <= 0) return;
		var keyLength = key.length;
		for (i in 0...data.length) {
			var k = key.get(i % keyLength);
			var d = data.get(i);
			if (d == 0 || d == k) continue;
			data.set(i, d ^ k);
			//trace('$d ^ $k = ${data.get(i)}');
		}
	}
}
```


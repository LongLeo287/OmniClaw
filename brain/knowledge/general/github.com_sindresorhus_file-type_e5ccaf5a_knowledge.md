---
id: github.com-sindresorhus-file-type-e5ccaf5a-knowled
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:22.682908
---

# KNOWLEDGE EXTRACT: github.com_sindresorhus_file-type_e5ccaf5a
> **Extracted on:** 2026-04-01 11:02:15
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007521180/github.com_sindresorhus_file-type_e5ccaf5a

---

## File: `.editorconfig`
```
root = true

[*]
indent_style = tab
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.yml]
indent_style = space
indent_size = 2
```

## File: `.gitattributes`
```
* text=auto eol=lf
```

## File: `.gitignore`
```
node_modules
yarn.lock
```

## File: `.npmrc`
```
package-lock=false
```

## File: `contributing.md`
```markdown
# Contributing

If you're adding support for a new file type, [please follow these steps](pull_request_template.md).
```

## File: `license`
```
MIT License

Copyright (c) Sindre Sorhus <sindresorhus@gmail.com> (https://sindresorhus.com)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `package.json`
```json
{
	"name": "file-type",
	"version": "22.0.0",
	"description": "Detect the file type of a file, stream, or data",
	"license": "MIT",
	"repository": "sindresorhus/file-type",
	"funding": "https://github.com/sindresorhus/file-type?sponsor=1",
	"author": {
		"name": "Sindre Sorhus",
		"email": "sindresorhus@gmail.com",
		"url": "https://sindresorhus.com"
	},
	"type": "module",
	"exports": {
		"types": "./source/index.d.ts",
		"default": "./source/index.js"
	},
	"sideEffects": false,
	"engines": {
		"node": ">=22"
	},
	"scripts": {
		"test": "xo && ava && tsd --typings source/index.d.ts --files source/index.test-d.ts"
	},
	"files": [
		"source"
	],
	"keywords": [
		"mime",
		"file",
		"type",
		"magic",
		"archive",
		"image",
		"img",
		"pic",
		"picture",
		"flash",
		"photo",
		"video",
		"detect",
		"check",
		"is",
		"exif",
		"elf",
		"macho",
		"exe",
		"binary",
		"buffer",
		"uint8array",
		"jpg",
		"png",
		"apng",
		"gif",
		"webp",
		"flif",
		"xcf",
		"cr2",
		"cr3",
		"orf",
		"arw",
		"dng",
		"nef",
		"rw2",
		"raf",
		"tif",
		"bmp",
		"icns",
		"jxr",
		"psd",
		"indd",
		"zip",
		"tar",
		"rar",
		"gz",
		"bz2",
		"7z",
		"dmg",
		"mp4",
		"mid",
		"mkv",
		"webm",
		"mov",
		"avi",
		"mpg",
		"mp2",
		"mp3",
		"m4a",
		"ogg",
		"opus",
		"flac",
		"wav",
		"amr",
		"pdf",
		"epub",
		"mobi",
		"swf",
		"rtf",
		"woff",
		"woff2",
		"eot",
		"ttf",
		"otf",
		"ttc",
		"ico",
		"flv",
		"ps",
		"xz",
		"sqlite",
		"xpi",
		"cab",
		"deb",
		"ar",
		"rpm",
		"Z",
		"lz",
		"cfb",
		"mxf",
		"mts",
		"wasm",
		"webassembly",
		"blend",
		"bpg",
		"docx",
		"pptx",
		"xlsx",
		"3gp",
		"j2c",
		"jp2",
		"jpm",
		"jpx",
		"mj2",
		"aif",
		"odt",
		"ods",
		"odp",
		"xml",
		"heic",
		"ics",
		"glb",
		"pcap",
		"dsf",
		"lnk",
		"alias",
		"voc",
		"ac3",
		"3g2",
		"m4b",
		"m4p",
		"m4v",
		"f4a",
		"f4b",
		"f4p",
		"f4v",
		"mie",
		"qcp",
		"asf",
		"ogv",
		"ogm",
		"oga",
		"spx",
		"ogx",
		"ape",
		"wv",
		"cur",
		"nes",
		"crx",
		"ktx",
		"dcm",
		"mpc",
		"arrow",
		"shp",
		"aac",
		"mp1",
		"it",
		"s3m",
		"xm",
		"skp",
		"avif",
		"eps",
		"lzh",
		"pgp",
		"asar",
		"stl",
		"chm",
		"3mf",
		"zst",
		"jxl",
		"vcf",
		"jls",
		"pst",
		"dwg",
		"parquet",
		"class",
		"arj",
		"cpio",
		"ace",
		"avro",
		"icc",
		"fbx",
		"vsdx",
		"vtt",
		"apk",
		"drc",
		"lz4",
		"potx",
		"xltx",
		"dotx",
		"xltm",
		"ots",
		"odg",
		"otg",
		"otp",
		"ott",
		"xlsm",
		"docm",
		"dotm",
		"potm",
		"pptm",
		"jar",
		"jmp",
		"rm",
		"sav",
		"ppsm",
		"ppsx",
		"tar.gz",
		"reg",
		"dat",
		"key",
		"numbers",
		"pages"
	],
	"dependencies": {
		"@tokenizer/inflate": "^0.4.1",
		"strtok3": "^10.3.5",
		"token-types": "^6.1.2",
		"uint8array-extras": "^1.5.0"
	},
	"devDependencies": {
		"@tokenizer/token": "^0.3.0",
		"@types/node": "^25.5.0",
		"ava": "^7.0.0",
		"commonmark": "^0.31.2",
		"get-stream": "^9.0.1",
		"tsd": "^0.33.0",
		"xo": "^2.0.2"
	},
	"xo": [
		{
			"ignores": [
				"fixture/**"
			]
		},
		{
			"rules": {
				"no-inner-declarations": "warn",
				"no-await-in-loop": "warn",
				"no-bitwise": "off",
				"@typescript-eslint/no-unsafe-assignment": "off",
				"unicorn/text-encoding-identifier-case": "off",
				"unicorn/switch-case-braces": "off",
				"unicorn/prefer-top-level-await": "off",
				"n/prefer-global/buffer": "off",
				"@stylistic/curly-newline": "off",
				"ava/no-useless-t-pass": "off",
				"ava/no-conditional-assertion": "off"
			}
		}
	],
	"ava": {
		"serial": true
	}
}
```

## File: `readme.md`
```markdown
<h1 align="center" title="file-type">
	<img src="media/logo.jpg" alt="file-type logo">
</h1>

> Detect the file type of a file, stream, or data

The file type is detected by checking the [magic number](https://en.wikipedia.org/wiki/Magic_number_(programming)#Magic_numbers_in_files) of the buffer.

This package is for detecting binary-based file formats, not text-based formats like `.txt`, `.csv`, `.svg`, etc.

We accept contributions for commonly used modern file formats, not historical or obscure ones. Open an issue first for discussion.

## Install

```sh
npm install file-type
```

**This package is an ESM package. Your project needs to be ESM too. [Read more](https://gist.github.com/sindresorhus/a39789f98801d908bbc7ff3ecc99d99c). For TypeScript + CommonJS, see [`load-esm`](https://github.com/Borewit/load-esm).** If you use it with Webpack, you need the latest Webpack version and ensure you configure it correctly for ESM.

> [!IMPORTANT]
> File type detection is based on binary signatures (magic numbers) and is a best-effort hint. It does not guarantee the file is actually of that type or that the file is valid/not malformed.
>
> Robustness against malformed input is best-effort. When processing untrusted files on a server, enforce a reasonable file size limit and use a worker thread with a timeout (e.g., [`make-asynchronous`](https://github.com/sindresorhus/make-asynchronous)). These are not considered security issues in this package.

## Usage

### Node.js

Determine file type from a file:

```js
import {fileTypeFromFile} from 'file-type';

console.log(await fileTypeFromFile('Unicorn.png'));
//=> {ext: 'png', mime: 'image/png'}
```

Determine file type from a Uint8Array/ArrayBuffer, which may be a portion of the beginning of a file:

```js
import {fileTypeFromBuffer} from 'file-type';
import {readChunk} from 'read-chunk';

const buffer = await readChunk('Unicorn.png', {length: 4100});

console.log(await fileTypeFromBuffer(buffer));
//=> {ext: 'png', mime: 'image/png'}
```

Determine file type from a stream:

```js
import {fileTypeFromStream} from 'file-type';

const url = 'https://upload.wikimedia.org/wikipedia/en/a/a9/Example.jpg';

const response = await fetch(url);
const fileType = await fileTypeFromStream(response.body);

console.log(fileType);
//=> {ext: 'jpg', mime: 'image/jpeg'}
```

## API

### fileTypeFromBuffer(buffer, options)

Detect the file type of a `Uint8Array` or `ArrayBuffer`.

The file type is detected by checking the [magic number](https://en.wikipedia.org/wiki/Magic_number_(programming)#Magic_numbers_in_files) of the buffer.

If file access is available, it is recommended to use `fileTypeFromFile()` instead.

Returns a `Promise` for an object with the detected file type:

- `ext` - One of the [supported file types](#supported-file-types)
- `mime` - The [MIME type](https://en.wikipedia.org/wiki/Internet_media_type)

Or `undefined` when there is no match.

#### buffer

Type: `Uint8Array | ArrayBuffer`

A buffer representing file data. It works best if the buffer contains the entire file. It may work with a smaller portion as well.

### fileTypeFromFile(filePath, options)

Detect the file type of a file path.

Only available in environments where `node:fs` is available, such as Node.js. To read from a [`File`](https://developer.mozilla.org/docs/Web/API/File), see [`fileTypeFromBlob()`](#filetypefromblobblob-options).

The file type is detected by checking the [magic number](https://en.wikipedia.org/wiki/Magic_number_(programming)#Magic_numbers_in_files) of the file.

Returns a `Promise` for an object with the detected file type:

- `ext` - One of the [supported file types](#supported-file-types)
- `mime` - The [MIME type](https://en.wikipedia.org/wiki/Internet_media_type)

Or `undefined` when there is no match.

#### filePath

Type: `string`

The file path to parse.

### fileTypeFromStream(stream, options)

Detect the file type of a [web `ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream).

The file type is detected by checking the [magic number](https://en.wikipedia.org/wiki/Magic_number_(programming)#Magic_numbers_in_files) of the buffer.

Returns a `Promise` for an object with the detected file type:

- `ext` - One of the [supported file types](#supported-file-types)
- `mime` - The [MIME type](https://en.wikipedia.org/wiki/Internet_media_type)

Or `undefined` when there is no match.

#### stream

Type: [Web `ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream)

A readable stream representing file data.

> [!TIP]
> If you have a Node.js `stream.Readable`, convert it with [`Readable.toWeb()`](https://nodejs.org/api/stream.html#streamreadabletowebstreamreadable-options).

### fileTypeFromBlob(blob, options)

Detect the file type of a [`Blob`](https://developer.mozilla.org/docs/Web/API/Blob).

> [!TIP]
> A [`File` object](https://developer.mozilla.org/docs/Web/API/File) is a `Blob` and can be passed in here.

It will **stream** the underlying Blob.

The file type is detected by checking the [magic number](https://en.wikipedia.org/wiki/Magic_number_(programming)#Magic_numbers_in_files) of the blob.

Returns a `Promise` for an object with the detected file type:

- `ext` - One of the [supported file types](#supported-file-types)
- `mime` - The [MIME type](https://en.wikipedia.org/wiki/Internet_media_type)

Or `undefined` when there is no match.

```js
import {fileTypeFromBlob} from 'file-type';

const blob = new Blob(['<?xml version="1.0" encoding="ISO-8859-1" ?>'], {
	type: 'text/plain',
	endings: 'native'
});

console.log(await fileTypeFromBlob(blob));
//=> {ext: 'txt', mime: 'text/plain'}
```

#### blob

Type: [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob)

### fileTypeFromTokenizer(tokenizer, options)

Detect the file type from an `ITokenizer` source.

This method is used internally, but can also be used for a special "tokenizer" reader.

A tokenizer propagates the internal read functions, allowing alternative transport mechanisms, to access files, to be implemented and used.

Returns a `Promise` for an object with the detected file type:

- `ext` - One of the [supported file types](#supported-file-types)
- `mime` - The [MIME type](https://en.wikipedia.org/wiki/Internet_media_type)

Or `undefined` when there is no match.

An example is [`@tokenizer/http`](https://github.com/Borewit/tokenizer-http), which requests data using [HTTP-range-requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Range_requests). A difference with a conventional stream and the [*tokenizer*](https://github.com/Borewit/strtok3#tokenizer), is that it can *ignore* (seek, fast-forward) in the stream. For example, you may only need and read the first 6 bytes, and the last 128 bytes, which may be an advantage in case reading the entire file would take longer.

```js
import {makeTokenizer} from '@tokenizer/http';
import {fileTypeFromTokenizer} from 'file-type';

const audioTrackUrl = 'https://test-audio.netlify.com/Various%20Artists%20-%202009%20-%20netBloc%20Vol%2024_%20tiuqottigeloot%20%5BMP3-V2%5D/01%20-%20Diablo%20Swing%20Orchestra%20-%20Heroines.mp3';

const httpTokenizer = await makeTokenizer(audioTrackUrl);
const fileType = await fileTypeFromTokenizer(httpTokenizer);

console.log(fileType);
//=> {ext: 'mp3', mime: 'audio/mpeg'}
```

Or use [`@tokenizer/s3`](https://github.com/Borewit/tokenizer-s3) to determine the file type of a file stored on [Amazon S3](https://aws.amazon.com/s3):

```js
import {S3Client} from '@aws-sdk/client-s3';
import {makeChunkedTokenizerFromS3} from '@tokenizer/s3';
import {fileTypeFromTokenizer} from 'file-type';

// Initialize S3 client
const s3 = new S3Client();

// Initialize the S3 tokenizer.
const s3Tokenizer = await makeChunkedTokenizerFromS3(s3, {
	Bucket: 'affectlab',
	Key: '1min_35sec.mp4'
});

// Figure out what kind of file it is.
const fileType = await fileTypeFromTokenizer(s3Tokenizer);
console.log(fileType);
```

Note that only the minimum amount of data required to determine the file type is read (okay, just a bit extra to prevent too many fragmented reads).

#### tokenizer

Type: [`ITokenizer`](https://github.com/Borewit/strtok3#tokenizer)

A file source implementing the [tokenizer interface](https://github.com/Borewit/strtok3#tokenizer).

### fileTypeStream(webStream, options?)

Returns a `Promise` which resolves to the original readable stream argument, but with an added `fileType` property, which is an object like the one returned from `fileTypeFromFile()`.

This method can be handy to put in a stream pipeline, but it comes with a price.
Internally `stream()` builds up a buffer of `sampleSize` bytes, used as a sample, to determine the file type.
The sample size impacts the file detection resolution.
A smaller sample size will result in lower probability of the best file type detection.

#### webStream

Type: [Web `ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream)

The input stream.

#### options

Type: `object`

Supports the following options in addition to the [general options](#options):

##### sampleSize

Type: `number`\
Default: `4100`

The sample size in bytes.

#### Example

```js
import {fileTypeStream} from 'file-type';

const url = 'https://upload.wikimedia.org/wikipedia/en/a/a9/Example.jpg';

const response = await fetch(url);
const stream = await fileTypeStream(response.body, {sampleSize: 1024});

if (stream.fileType?.mime === 'image/jpeg') {
	// stream can be used to stream the JPEG image (from the very beginning of the stream)
}
```

### supportedExtensions

Returns a `Set<string>` of supported file extensions.

### supportedMimeTypes

Returns a `Set<string>` of supported MIME types.

### Options

#### customDetectors

Array of custom file type detectors to run before default detectors.

For example:

```js
import {fileTypeFromFile} from 'file-type';
import {detectXml} from '@file-type/xml';

const fileType = await fileTypeFromFile('sample.kml', {customDetectors: [detectXml]});
console.log(fileType);
```

#### mpegOffsetTolerance

Default: `0`

Specifies the byte tolerance for locating the first MPEG audio frame (e.g. `.mp1`, `.mp2`, `.mp3`, `.aac`).

Allows detection to handle slight sync offsets between the expected and actual frame start. Common in malformed or incorrectly muxed files, which, while technically invalid, do occur in the wild.

A tolerance of 10 bytes covers most cases.

## Custom detectors

Custom file type detectors are plugins designed to extend the default detection capabilities.
They allow support for uncommon file types, non-binary formats, or customized detection behavior.

Detectors can be added via the constructor options or by directly modifying `FileTypeParser#detectors`.
Detectors provided through the constructor are executed before the default ones.

### Example adding a detector

```js
import {FileTypeParser} from 'file-type';
import {detectXml} from '@file-type/xml';

const parser = new FileTypeParser({customDetectors: [detectXml]});
const fileType = await parser.fromFile('sample.kml');
console.log(fileType);
```

### Available third-party file-type detectors

- [@file-type/av](https://github.com/Borewit/file-type-av): Improves detection of audio and video file formats, with accurate differentiation between the two
- [@file-type/cfbf](https://github.com/Borewit/file-type-cfbf): Detects Compound File Binary Format (CFBF) based formats, such as Office 97–2003 documents and `.msi`.
- [@file-type/pdf](https://github.com/Borewit/file-type-pdf): Detects PDF based file types, such as Adobe Illustrator
- [@file-type/xml](https://github.com/Borewit/file-type-xml): Detects common XML file types, such as GLM, KML, MusicXML, RSS, SVG, and XHTML

### Detector execution flow

If a detector returns `undefined`, the following rules apply:

1. **No Tokenizer Interaction**: If the detector does not modify the tokenizer's position, the next detector in the sequence is executed.
2. **Tokenizer Interaction**: If the detector modifies the tokenizer's position (`tokenizer.position` is advanced), no further detectors are executed. In this case, the file type remains `undefined`, as subsequent detectors cannot evaluate the content. This is an exceptional scenario, as it prevents any other detectors from determining the file type.

### Writing your own custom detector

Below is an example of a custom detector. This can be passed to the `FileTypeParser` via the `customDetectors` option.

```js
import {FileTypeParser} from 'file-type';

const unicornDetector = {
	id: 'unicorn', // May be used to recognize the detector in the detector list
	async detect(tokenizer) {
		const unicornHeader = [85, 78, 73, 67, 79, 82, 78]; // "UNICORN" in ASCII decimal

		const buffer = new Uint8Array(unicornHeader.length);
		await tokenizer.peekBuffer(buffer, {length: unicornHeader.length, mayBeLess: true});
		if (unicornHeader.every((value, index) => value === buffer[index])) {
			return {ext: 'unicorn', mime: 'application/unicorn'};
		}

		return undefined;
	}
}

const buffer = new Uint8Array([85, 78, 73, 67, 79, 82, 78]);
const parser = new FileTypeParser({customDetectors: [unicornDetector]});
const fileType = await parser.fromBuffer(buffer);
console.log(fileType); // {ext: 'unicorn', mime: 'application/unicorn'}
```

```ts
/**
@param tokenizer - The [tokenizer](https://github.com/Borewit/strtok3#tokenizer) used to read file content.
@param fileType - The file type detected by standard or previous custom detectors, or `undefined` if no match is found.
@returns The detected file type, or `undefined` if no match is found.
*/
export type Detector = {
	id: string;
	detect: (tokenizer: ITokenizer, fileType?: FileTypeResult) => Promise<FileTypeResult | undefined>;
};
```

## Abort signal

Some async operations can be aborted by passing an [`AbortSignal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) to the `FileTypeParser` constructor.

```js
import {FileTypeParser} from 'file-type';

const abortController = new AbortController();

const parser = new FileTypeParser({signal: abortController.signal});

const promise = parser.fromStream(blob.stream());

abortController.abort(); // Abort file-type reading from the Blob stream.
```

## Supported file types

MIME media subtypes prefixed with `x-ft-` are custom and defined by us. They are neither formally registered with IANA nor based on any informal conventions.

- [`3g2`](https://en.wikipedia.org/wiki/3GP_and_3G2#3G2) - Multimedia container format defined by the 3GPP2 for 3G CDMA2000 multimedia services
- [`3gp`](https://en.wikipedia.org/wiki/3GP_and_3G2#3GP) - Multimedia container format defined by the Third Generation Partnership Project (3GPP) for 3G UMTS multimedia services
- [`3mf`](https://en.wikipedia.org/wiki/3D_Manufacturing_Format) - 3D Manufacturing Format
- [`7z`](https://en.wikipedia.org/wiki/7z) - 7-Zip archive
- [`Z`](https://fileinfo.com/extension/z) - Unix Compressed File
- [`aac`](https://en.wikipedia.org/wiki/Advanced_Audio_Coding) - Advanced Audio Coding
- [`ac3`](https://www.atsc.org/standard/a522012-digital-audio-compression-ac-3-e-ac-3-standard-12172012/) - ATSC A/52 Audio File
- [`ace`](https://en.wikipedia.org/wiki/ACE_(compressed_file_format)) - ACE archive
- [`aif`](https://en.wikipedia.org/wiki/Audio_Interchange_File_Format) - Audio Interchange file
- [`alias`](https://en.wikipedia.org/wiki/Alias_%28Mac_OS%29) - macOS Alias file
- [`amr`](https://en.wikipedia.org/wiki/Adaptive_Multi-Rate_audio_codec) - Adaptive Multi-Rate audio codec
- [`ape`](https://en.wikipedia.org/wiki/Monkey%27s_Audio) - Monkey's Audio
- [`apk`](https://en.wikipedia.org/wiki/Apk_(file_format)) - Android package format
- [`apng`](https://en.wikipedia.org/wiki/APNG) - Animated Portable Network Graphics
- [`ar`](https://en.wikipedia.org/wiki/Ar_(Unix)) - Archive file
- [`arj`](https://en.wikipedia.org/wiki/ARJ) - Archive file
- [`arrow`](https://arrow.apache.org) - Columnar format for tables of data
- [`arw`](https://en.wikipedia.org/wiki/Raw_image_format#ARW) - Sony Alpha Raw image file
- [`asar`](https://github.com/electron/asar#format) - Archive format primarily used to enclose Electron applications
- [`asf`](https://en.wikipedia.org/wiki/Advanced_Systems_Format) - Advanced Systems Format
- [`avi`](https://en.wikipedia.org/wiki/Audio_Video_Interleave) - Audio Video Interleave file
- [`avif`](https://en.wikipedia.org/wiki/AV1#AV1_Image_File_Format_(AVIF)) - AV1 Image File Format
- [`avro`](https://en.wikipedia.org/wiki/Apache_Avro#Avro_Object_Container_File) - Object container file developed by Apache Avro
- [`blend`](https://wiki.blender.org/index.php/Dev:Source/Architecture/File_Format) - Blender project
- [`bmp`](https://en.wikipedia.org/wiki/BMP_file_format) - Bitmap image file
- [`bpg`](https://bellard.org/bpg/) - Better Portable Graphics file
- [`bz2`](https://en.wikipedia.org/wiki/Bzip2) - Archive file
- [`cab`](https://en.wikipedia.org/wiki/Cabinet_(file_format)) - Cabinet file
- [`cfb`](https://en.wikipedia.org/wiki/Compound_File_Binary_Format) - Compound File Binary Format
- [`chm`](https://en.wikipedia.org/wiki/Microsoft_Compiled_HTML_Help) - Microsoft Compiled HTML Help
- [`class`](https://en.wikipedia.org/wiki/Java_class_file) - Java class file
- [`cpio`](https://en.wikipedia.org/wiki/Cpio) - Cpio archive
- [`cr2`](https://fileinfo.com/extension/cr2) - Canon Raw image file (v2)
- [`cr3`](https://fileinfo.com/extension/cr3) - Canon Raw image file (v3)
- [`crx`](https://developer.chrome.com/extensions/crx) - Google Chrome extension
- [`cur`](https://en.wikipedia.org/wiki/ICO_(file_format)) - Icon file
- [`dat`](https://en.wikipedia.org/wiki/Windows_Registry) - Windows registry hive file
- [`dcm`](https://en.wikipedia.org/wiki/DICOM#Data_format) - DICOM Image File
- [`deb`](https://en.wikipedia.org/wiki/Deb_(file_format)) - Debian package
- [`dmg`](https://en.wikipedia.org/wiki/Apple_Disk_Image) - Apple Disk Image
- [`dng`](https://en.wikipedia.org/wiki/Digital_Negative) - Adobe Digital Negative image file
- [`docm`](https://en.wikipedia.org/wiki/List_of_Microsoft_Office_filename_extensions) - Microsoft Word macro-enabled document
- [`docx`](https://en.wikipedia.org/wiki/Office_Open_XML) - Microsoft Word document
- [`dotm`](https://en.wikipedia.org/wiki/List_of_Microsoft_Office_filename_extensions) - Microsoft Word macro-enabled template
- [`dotx`](https://en.wikipedia.org/wiki/List_of_Microsoft_Office_filename_extensions) - Microsoft Word template
- [`drc`](https://en.wikipedia.org/wiki/Zstandard) - Google's Draco 3D Data Compression
- [`dsf`](https://dsd-guide.com/sites/default/files/white-papers/DSFFileFormatSpec_E.pdf) - Sony DSD Stream File (DSF)
- [`dwg`](https://en.wikipedia.org/wiki/.dwg) - Autodesk CAD file
- [`elf`](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format) - Unix Executable and Linkable Format
- [`eot`](https://en.wikipedia.org/wiki/Embedded_OpenType) - Embedded OpenType font
- [`eps`](https://en.wikipedia.org/wiki/Encapsulated_PostScript) - Encapsulated PostScript
- [`epub`](https://en.wikipedia.org/wiki/EPUB) - E-book file
- [`exe`](https://en.wikipedia.org/wiki/.exe) - Executable file
- [`f4a`](https://en.wikipedia.org/wiki/Flash_Video) - Audio-only ISO base media file format used by Adobe Flash Player
- [`f4b`](https://en.wikipedia.org/wiki/Flash_Video) - Audiobook and podcast ISO base media file format used by Adobe Flash Player
- [`f4p`](https://en.wikipedia.org/wiki/Flash_Video) - ISO base media file format protected by Adobe Access DRM used by Adobe Flash Player
- [`f4v`](https://en.wikipedia.org/wiki/Flash_Video) - ISO base media file format used by Adobe Flash Player
- [`fbx`](https://en.wikipedia.org/wiki/FBX) - Filmbox is a proprietary file format used to provide interoperability between digital content creation apps.
- [`flac`](https://en.wikipedia.org/wiki/FLAC) - Free Lossless Audio Codec
- [`flif`](https://en.wikipedia.org/wiki/Free_Lossless_Image_Format) - Free Lossless Image Format
- [`flv`](https://en.wikipedia.org/wiki/Flash_Video) - Flash video
- [`gif`](https://en.wikipedia.org/wiki/GIF) - Graphics Interchange Format
- [`glb`](https://github.com/KhronosGroup/glTF) - GL Transmission Format
- [`gz`](https://en.wikipedia.org/wiki/Gzip) - Archive file
- [`heic`](https://nokiatech.github.io/heif/technical.html) - High Efficiency Image File Format
- [`icc`](https://en.wikipedia.org/wiki/ICC_profile) - ICC Profile
- [`icns`](https://en.wikipedia.org/wiki/Apple_Icon_Image_format) - Apple Icon image
- [`ico`](https://en.wikipedia.org/wiki/ICO_(file_format)) - Windows icon file
- [`ics`](https://en.wikipedia.org/wiki/ICalendar#Data_format) - iCalendar
- [`indd`](https://en.wikipedia.org/wiki/Adobe_InDesign#File_format) - Adobe InDesign document
- [`it`](https://wiki.openmpt.org/Manual:_Module_formats#The_Impulse_Tracker_format_.28.it.29) - Audio module format: Impulse Tracker
- [`j2c`](https://en.wikipedia.org/wiki/JPEG_2000) - JPEG 2000
- [`jar`](https://en.wikipedia.org/wiki/JAR_(file_format)) - Java archive
- [`jls`](https://en.wikipedia.org/wiki/Lossless_JPEG#JPEG-LS) - Lossless/near-lossless compression standard for continuous-tone images
- [`jmp`](https://en.wikipedia.org/wiki/JMP_(statistical_software)) - JMP data file format by SAS Institute
- [`jp2`](https://en.wikipedia.org/wiki/JPEG_2000) - JPEG 2000
- [`jpg`](https://en.wikipedia.org/wiki/JPEG) - Joint Photographic Experts Group image
- [`jpm`](https://en.wikipedia.org/wiki/JPEG_2000) - JPEG 2000
- [`jpx`](https://en.wikipedia.org/wiki/JPEG_2000) - JPEG 2000
- [`jxl`](https://en.wikipedia.org/wiki/JPEG_XL) - JPEG XL image format
- [`jxr`](https://en.wikipedia.org/wiki/JPEG_XR) - Joint Photographic Experts Group extended range
- [`key`](https://en.wikipedia.org/wiki/Keynote_(presentation_software)) - Apple Keynote presentation
- [`ktx`](https://www.khronos.org/opengles/sdk/tools/KTX/file_format_spec/) - OpenGL and OpenGL ES textures
- [`lnk`](https://en.wikipedia.org/wiki/Shortcut_%28computing%29#Microsoft_Windows) - Microsoft Windows file shortcut
- [`lz`](https://en.wikipedia.org/wiki/Lzip) - Archive file
- [`lz4`](https://en.wikipedia.org/wiki/LZ4_(compression_algorithm)) - Compressed archive created by one of a variety of LZ4 compression utilities
- [`lzh`](https://en.wikipedia.org/wiki/LHA_(file_format)) - LZH archive
- [`m4a`](https://en.wikipedia.org/wiki/M4A) - Audio-only MPEG-4 files
- [`m4b`](https://en.wikipedia.org/wiki/M4B) - Audiobook and podcast MPEG-4 files, which also contain metadata including chapter markers, images, and hyperlinks
- [`m4p`](https://en.wikipedia.org/wiki/MPEG-4_Part_14#Filename_extensions) - MPEG-4 files with audio streams encrypted by FairPlay Digital Rights Management as were sold through the iTunes Store
- [`m4v`](https://en.wikipedia.org/wiki/M4V) - Video container format developed by Apple, which is very similar to the MP4 format
- [`macho`](https://en.wikipedia.org/wiki/Mach-O) - Mach-O binary format
- [`mid`](https://en.wikipedia.org/wiki/MIDI) - Musical Instrument Digital Interface file
- [`mie`](https://en.wikipedia.org/wiki/Sidecar_file) - Dedicated meta information format which supports storage of binary as well as textual meta information
- [`mj2`](https://en.wikipedia.org/wiki/Motion_JPEG_2000) - Motion JPEG 2000
- [`mkv`](https://en.wikipedia.org/wiki/Matroska) - Matroska video file
- [`mobi`](https://en.wikipedia.org/wiki/Mobipocket) - Mobipocket
- [`mov`](https://en.wikipedia.org/wiki/QuickTime_File_Format) - QuickTime video file
- [`mp1`](https://en.wikipedia.org/wiki/MPEG-1_Audio_Layer_I) - MPEG-1 Audio Layer I
- [`mp2`](https://en.wikipedia.org/wiki/MPEG-1_Audio_Layer_II) - MPEG-1 Audio Layer II
- [`mp3`](https://en.wikipedia.org/wiki/MP3) - Audio file
- [`mp4`](https://en.wikipedia.org/wiki/MPEG-4_Part_14#Filename_extensions) - MPEG-4 Part 14 video file
- [`mpc`](https://en.wikipedia.org/wiki/Musepack) - Musepack (SV7 & SV8)
- [`mpg`](https://en.wikipedia.org/wiki/MPEG-1) - MPEG-1 file
- [`mts`](https://en.wikipedia.org/wiki/.m2ts) - MPEG-2 Transport Stream, both raw and Blu-ray Disc Audio-Video (BDAV) versions
- [`mxf`](https://en.wikipedia.org/wiki/Material_Exchange_Format) - Material Exchange Format
- [`nef`](https://www.nikonusa.com/en/learn-and-explore/a/products-and-innovation/nikon-electronic-format-nef.html) - Nikon Electronic Format image file
- [`nes`](https://fileinfo.com/extension/nes) - Nintendo NES ROM
- [`numbers`](https://en.wikipedia.org/wiki/Numbers_(spreadsheet)) - Apple Numbers spreadsheet
- [`odg`](https://en.wikipedia.org/wiki/OpenDocument) - OpenDocument for drawing
- [`odp`](https://en.wikipedia.org/wiki/OpenDocument) - OpenDocument for presentations
- [`ods`](https://en.wikipedia.org/wiki/OpenDocument) - OpenDocument for spreadsheets
- [`odt`](https://en.wikipedia.org/wiki/OpenDocument) - OpenDocument for word processing
- [`oga`](https://en.wikipedia.org/wiki/Ogg) - Audio file
- [`ogg`](https://en.wikipedia.org/wiki/Ogg) - Audio file
- [`ogm`](https://en.wikipedia.org/wiki/Ogg) - Audio file
- [`ogv`](https://en.wikipedia.org/wiki/Ogg) - Audio file
- [`ogx`](https://en.wikipedia.org/wiki/Ogg) - Audio file
- [`opus`](https://en.wikipedia.org/wiki/Opus_(audio_format)) - Audio file
- [`orf`](https://en.wikipedia.org/wiki/ORF_format) - Olympus Raw image file
- [`otf`](https://en.wikipedia.org/wiki/OpenType) - OpenType font
- [`otg`](https://en.wikipedia.org/wiki/OpenDocument_technical_specification#Templates) - OpenDocument template for drawing
- [`otp`](https://en.wikipedia.org/wiki/OpenDocument_technical_specification#Templates) - OpenDocument template for presentations
- [`ots`](https://en.wikipedia.org/wiki/OpenDocument_technical_specification#Templates) - OpenDocument template for spreadsheets
- [`ott`](https://en.wikipedia.org/wiki/OpenDocument_technical_specification#Templates) - OpenDocument template for word processing
- [`pages`](https://en.wikipedia.org/wiki/Pages_(word_processor)) - Apple Pages document
- [`parquet`](https://en.wikipedia.org/wiki/Apache_Parquet) - Apache Parquet
- [`pcap`](https://wiki.wireshark.org/Development/LibpcapFileFormat) - Libpcap File Format
- [`pdf`](https://en.wikipedia.org/wiki/Portable_Document_Format) - Portable Document Format
- [`pgp`](https://en.wikipedia.org/wiki/Pretty_Good_Privacy) - Pretty Good Privacy
- [`png`](https://en.wikipedia.org/wiki/Portable_Network_Graphics) - Portable Network Graphics
- [`potm`](https://en.wikipedia.org/wiki/List_of_Microsoft_Office_filename_extensions) - Microsoft PowerPoint macro-enabled template
- [`potx`](https://en.wikipedia.org/wiki/List_of_Microsoft_Office_filename_extensions) - Microsoft PowerPoint template
- [`ppsm`](https://en.wikipedia.org/wiki/List_of_Microsoft_Office_filename_extensions#PowerPoint) - Office PowerPoint 2007 macro-enabled slide show
- [`ppsx`](https://en.wikipedia.org/wiki/List_of_Microsoft_Office_filename_extensions#PowerPoint) - Office PowerPoint 2007 slide show
- [`pptm`](https://en.wikipedia.org/wiki/List_of_Microsoft_Office_filename_extensions) - Microsoft PowerPoint macro-enabled document
- [`pptx`](https://en.wikipedia.org/wiki/Office_Open_XML) - Microsoft PowerPoint document
- [`ps`](https://en.wikipedia.org/wiki/Postscript) - PostScript
- [`psd`](https://en.wikipedia.org/wiki/Adobe_Photoshop#File_format) - Adobe Photoshop document
- [`pst`](https://en.wikipedia.org/wiki/Personal_Storage_Table) - Personal Storage Table file
- [`qcp`](https://en.wikipedia.org/wiki/QCP) - Tagged and chunked data
- [`raf`](https://en.wikipedia.org/wiki/Raw_image_format) - Fujifilm RAW image file
- [`rar`](https://en.wikipedia.org/wiki/RAR_(file_format)) - Archive file
- [`reg`](https://en.wikipedia.org/wiki/Windows_Registry) - Windows registry (entries) file format
- [`rm`](https://en.wikipedia.org/wiki/RealMedia) - RealMedia
- [`rpm`](https://fileinfo.com/extension/rpm) - Red Hat Package Manager file
- [`rtf`](https://en.wikipedia.org/wiki/Rich_Text_Format) - Rich Text Format
- [`rw2`](https://en.wikipedia.org/wiki/Raw_image_format) - Panasonic RAW image file
- [`s3m`](https://wiki.openmpt.org/Manual:_Module_formats#The_ScreamTracker_3_format_.28.s3m.29) - Audio module format: ScreamTracker 3
- [`sav`](https://en.wikipedia.org/wiki/SPSS) - SPSS Statistical Data File
- [`shp`](https://en.wikipedia.org/wiki/Shapefile) - Geospatial vector data format
- [`skp`](https://en.wikipedia.org/wiki/SketchUp) - SketchUp
- [`spx`](https://en.wikipedia.org/wiki/Ogg) - Audio file
- [`sqlite`](https://www.sqlite.org/fileformat2.html) - SQLite file
- [`stl`](https://en.wikipedia.org/wiki/STL_(file_format)) - Standard Tessellated Geometry File Format (ASCII only)
- [`swf`](https://en.wikipedia.org/wiki/SWF) - Adobe Flash Player file
- [`tar`](https://en.wikipedia.org/wiki/Tar_(computing)#File_format) - Tape archive or tarball
- [`tar.gz`](https://en.wikipedia.org/wiki/Gzip) - Gzipped tape archive (tarball)
- [`tif`](https://en.wikipedia.org/wiki/Tagged_Image_File_Format) - Tagged Image file
- [`ttc`](https://en.wikipedia.org/wiki/TrueType#TrueType_Collection) - TrueType Collection font
- [`ttf`](https://en.wikipedia.org/wiki/TrueType) - TrueType font
- [`vcf`](https://en.wikipedia.org/wiki/VCard) - vCard
- [`voc`](https://wiki.multimedia.cx/index.php/Creative_Voice) - Creative Voice File
- [`vsdx`](https://en.wikipedia.org/wiki/Microsoft_Visio) - Microsoft Visio File
- [`vtt`](https://en.wikipedia.org/wiki/WebVTT) - WebVTT File (for video captions)
- [`wasm`](https://en.wikipedia.org/wiki/WebAssembly) - WebAssembly intermediate compiled format
- [`wav`](https://en.wikipedia.org/wiki/WAV) - Waveform Audio file
- [`webm`](https://en.wikipedia.org/wiki/WebM) - Web video file
- [`webp`](https://en.wikipedia.org/wiki/WebP) - Web Picture format
- [`woff`](https://en.wikipedia.org/wiki/Web_Open_Font_Format) - Web Open Font Format
- [`woff2`](https://en.wikipedia.org/wiki/Web_Open_Font_Format) - Web Open Font Format
- [`wv`](https://en.wikipedia.org/wiki/WavPack) - WavPack
- [`xcf`](https://en.wikipedia.org/wiki/XCF_(file_format)) - eXperimental Computing Facility
- [`xlsm`](https://en.wikipedia.org/wiki/List_of_Microsoft_Office_filename_extensions) - Microsoft Excel macro-enabled document
- [`xlsx`](https://en.wikipedia.org/wiki/Office_Open_XML) - Microsoft Excel document
- [`xltm`](https://en.wikipedia.org/wiki/List_of_Microsoft_Office_filename_extensions) - Microsoft Excel macro-enabled template
- [`xltx`](https://en.wikipedia.org/wiki/List_of_Microsoft_Office_filename_extensions) - Microsoft Excel template
- [`xm`](https://wiki.openmpt.org/Manual:_Module_formats#The_FastTracker_2_format_.28.xm.29) - Audio module format: FastTracker 2
- [`xml`](https://en.wikipedia.org/wiki/XML) - eXtensible Markup Language
- [`xpi`](https://en.wikipedia.org/wiki/XPInstall) - XPInstall file
- [`xz`](https://en.wikipedia.org/wiki/Xz) - Compressed file
- [`zip`](https://en.wikipedia.org/wiki/Zip_(file_format)) - Archive file
- [`zst`](https://en.wikipedia.org/wiki/Zstandard) - Archive file

*[Pull requests](pull_request_template.md) are welcome for additional commonly used file types.*

The following file types will not be accepted, but most of them are supported by [third-party detectors](#available-third-party-file-type-detectors).
- [MS-CFB: Microsoft Compound File Binary File Format based formats](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-cfb/53989ce4-7b05-4f8d-829b-d08d6148375b)
	- `.doc` - Microsoft Word 97-2003 Document
	- `.xls` - Microsoft Excel 97-2003 Document
	- `.ppt` - Microsoft PowerPoint 97-2003 Document
	- `.msi` - Microsoft Windows Installer
- `.csv` - [Reason.](https://github.com/sindresorhus/file-type/issues/264#issuecomment-568439196)
- `.svg`

## Related

- [file-type-cli](https://github.com/sindresorhus/file-type-cli) - CLI for this module
- [image-dimensions](https://github.com/sindresorhus/image-dimensions) - Get the dimensions of an image

## Maintainers

- [Sindre Sorhus](https://github.com/sindresorhus)
- [Borewit](https://github.com/Borewit)
```

## File: `test.js`
```javascript
import process from 'node:process';
import os from 'node:os';
import path from 'node:path';
import http from 'node:http';
import {spawnSync} from 'node:child_process';
import fs from 'node:fs';
import {readFile} from 'node:fs/promises';
import {deflateRawSync, gzipSync} from 'node:zlib';
import test from 'ava';
import {Parser as ReadmeParser} from 'commonmark';
import {fromFile} from 'strtok3';
import * as strtok3 from 'strtok3/core';
import {areUint8ArraysEqual} from 'uint8array-extras';
import {getStreamAsArrayBuffer} from 'get-stream';
import {stringToBytes} from './source/tokens.js';
import {
	fileTypeFromBuffer,
	fileTypeFromStream,
	fileTypeFromFile,
	fileTypeFromBlob,
	fileTypeFromTokenizer,
	fileTypeStream,
	supportedExtensions,
	supportedMimeTypes,
	FileTypeParser,
} from './source/index.js';

const __dirname = import.meta.dirname;

const missingTests = new Set();

const reasonableDetectionSizeInBytes = 4100;
const maximumZipTextEntrySizeInBytes = 1024 * 1024;
const maximumStreamPayloadProbeSizeInBytes = 1024 * 1024;
const maximumUntrustedSkipSizeInBytes = 16 * 1024 * 1024;
const legacyOversizedZipTextEntrySizeInBytes = 16 * 1024 * 1024;

const types = [...supportedExtensions].filter(extension => !missingTests.has(extension));

// Define an entry here only if the fixture has a different
// name than `fixture` or if you want multiple fixtures
const names = {
	aac: [
		'fixture-adts-mpeg2',
		'fixture-adts-mpeg4',
		'fixture-adts-mpeg4-2',
		'fixture-id3v2',
	],
	asar: [
		'fixture',
		'fixture2',
	],
	arw: [
		'fixture-sony-zv-e10',
	],
	cr3: [
		'fixture',
	],
	dng: [
		'fixture-Leica-M10',
	],
	drc: [
		'fixture-cube_pc',
	],
	epub: [
		'fixture',
		'fixture-crlf',
	],
	nef: [
		'fixture',
		'fixture2',
		'fixture3',
		'fixture4',
	],
	'3gp': [
		'fixture',
		'fixture2',
	],
	woff2: [
		'fixture',
		'fixture-otto',
	],
	woff: [
		'fixture',
		'fixture-otto',
	],
	eot: [
		'fixture',
		'fixture-0x20001',
	],
	mov: [
		'fixture',
		'fixture-mjpeg',
		'fixture-moov',
	],
	mp2: [
		'fixture',
		'fixture-mpa',
	],
	mp3: [
		'fixture',
		'fixture-mp2l3',
		'fixture-ffe3',
	],
	mp4: [
		'fixture-imovie',
		'fixture-isom',
		'fixture-isomv2',
		'fixture-mp4v2',
		'fixture-dash',
	],
	mts: [
		'fixture-raw',
		'fixture-bdav',
	],
	tif: [
		'fixture-big-endian',
		'fixture-little-endian',
		'fixture-bali',
	],
	gz: [
		'fixture',
	],
	xz: [
		'fixture.tar',
	],
	lz: [
		'fixture.tar',
	],
	Z: [
		'fixture.tar',
	],
	zst: [
		'fixture.tar',
	],
	mkv: [
		'fixture',
		'fixture2',
	],
	mpg: [
		'fixture',
		'fixture2',
		'fixture.ps',
		'fixture.sub',
	],
	heic: [
		'fixture-mif1',
		'fixture-msf1',
		'fixture-heic',
	],
	ape: [
		'fixture-monkeysaudio',
	],
	mpc: [
		'fixture-sv7',
		'fixture-sv8',
	],
	pcap: [
		'fixture-big-endian',
		'fixture-little-endian',
	],
	png: [
		'fixture',
		'fixture-itxt',
	],
	tar: [
		'fixture',
		'fixture-v7',
		'fixture-spaces',
		'fixture-pax',
	],
	mie: [
		'fixture-big-endian',
		'fixture-little-endian',
	],
	m4a: [
		'fixture-babys-songbook.m4b', // Actually it's an `.m4b`
	],
	m4v: [
		'fixture',
		'fixture-2', // Previously named as `fixture.mp4`
	],
	flac: [
		'fixture',
		'fixture-id3v2', // FLAC prefixed with ID3v2 header
	],
	docx: [
		'fixture',
		'fixture2',
		'fixture-office365',
	],
	pptx: [
		'fixture',
		'fixture2',
		'fixture-office365',
	],
	xlsx: [
		'fixture',
		'fixture2',
		'fixture-office365',
	],
	ogx: [
		'fixture-unknown-ogg', // Manipulated fixture to unrecognized Ogg based file
	],
	avif: [
		'fixture-yuv420-8bit', // Multiple bit-depths and/or subsamplings
		'fixture-sequence',
	],
	eps: [
		'fixture',
		'fixture2',
	],
	cfb: [
		'fixture.msi',
		'fixture.xls',
		'fixture.doc',
		'fixture.ppt',
		'fixture-2.doc',
	],
	asf: [
		'fixture',
		'fixture.wma',
		'fixture.wmv',
	],
	jxl: [
		'fixture', // Image data stored within JXL container
		'fixture2', // Bare image data with no container
	],
	pdf: [
		'fixture',
		'fixture-adobe-illustrator', // PDF saved from Adobe Illustrator, using the default "[Illustrator Default]" preset
		'fixture-smallest', // PDF saved from Adobe Illustrator, using the preset "smallest PDF"
		'fixture-fast-web', // PDF saved from Adobe Illustrator, using the default "[Illustrator Default"] preset, but enabling "Optimize for Fast Web View"
		'fixture-printed', // PDF printed from Adobe Illustrator, but with a PDF printer.
		'fixture-minimal', // PDF written to be as small as the spec allows
	],
	webm: [
		'fixture-null', // EBML DocType with trailing null character
	],
	xml: [
		'fixture',
		'fixture-utf8-bom', // UTF-8 with BOM
		'fixture-utf16-be-bom', // UTF-16 little endian encoded XML, with BOM
		'fixture-utf16-le-bom', // UTF-16 big endian encoded XML, with BOM
	],
	jls: [
		'fixture-normal',
		'fixture-hp1',
		'fixture-hp2',
		'fixture-hp3',
	],
	pst: [
		'fixture-sample',
	],
	dwg: [
		'fixture-line-weights',
	],
	j2c: [
		'fixture',
	],
	cpio: [
		'fixture-bin',
		'fixture-ascii',
	],
	vsdx: [
		'fixture-vsdx',
		'fixture-vstx',
	],
	vtt: [
		'fixture-vtt-linebreak',
		'fixture-vtt-space',
		'fixture-vtt-tab',
		'fixture-vtt-eof',
	],
	lz4: [
		'fixture',
	],
	rm: [
		'fixture-realmedia-audio',
		'fixture-realmedia-video',
	],
	ppsx: [
		'fixture',
	],
	ppsm: [
		'fixture',
	],
	'tar.gz': [
		'fixture',
	],
	reg: [
		'fixture-win2000',
		'fixture-win95',
	],
	dat: [
		'fixture-unicode-tests',
	],
	zip: [
		'fixture',
		'fixture2',
	],
	macho: [
		'fixture-arm64',
		'fixture-x86_64',
		'fixture-i386',
		'fixture-ppc7400',
		'fixture-fat-binary',
	],
};

// Define an entry here only if the file type has potential
// for false-positives
const falsePositives = {
	png: [
		'fixture-corrupt',
	],
	webp: [
		'fixture-json',
	],
};

// Known failing fixture
const failingFixture = new Set([
	'fixture-password-protected.xls', // Excel / MS-OSHARED / Compound-File-Binary-Format
]);

/**
 @returns {Array<Object>} An array of fixture objects.
 Each object contains the following properties:
 - `path` {string}: The full path to the fixture file.
 - `filename` {string}: The name of the fixture file.
 - `type` {string}: The type/extension of the fixture.
 */
function getFixtures() {
	const paths = [];
	for (const type of types) {
		if (Object.hasOwn(names, type)) {
			for (const suffix of names[type]) {
				const filename = `${(suffix ?? 'fixture')}.${type}`;
				paths.push({
					path: path.join(__dirname, 'fixture', filename),
					filename,
					type,
				});
			}
		} else {
			const filename = `fixture.${type}`;
			paths.push({
				path: path.join(__dirname, 'fixture', filename),
				filename,
				type,
			});
		}
	}

	return paths;
}

async function checkBufferLike(t, expectedExtension, bufferLike) {
	const {ext, mime} = await fileTypeFromBuffer(bufferLike) ?? {};
	t.is(ext, expectedExtension);
	t.is(typeof mime, 'string');
}

async function checkBlobLike(t, expectedExtension, bufferLike) {
	const blob = new Blob([bufferLike]);
	const {ext, mime} = await fileTypeFromBlob(blob) ?? {};
	t.is(ext, expectedExtension);
	t.is(typeof mime, 'string');
}

async function testFromFile(t, expectedExtension, filePath) {
	const {ext, mime} = await fileTypeFromFile(filePath) ?? {};
	t.is(ext, expectedExtension);
	t.is(typeof mime, 'string');
}

async function testFromBuffer(t, expectedExtension, path) {
	const chunk = fs.readFileSync(path);
	await checkBufferLike(t, expectedExtension, chunk);
	await checkBufferLike(t, expectedExtension, new Uint8Array(chunk));

	if (path.includes('fixture2.zip')) {
		await checkBufferLike(t, expectedExtension, chunk.buffer.slice(0, Math.floor(chunk.byteLength / 2)));
	}

	await checkBufferLike(t, expectedExtension, chunk.buffer.slice(chunk.byteOffset, chunk.byteOffset + chunk.byteLength));
}

async function testFromBlob(t, expectedExtension, path) {
	const chunk = fs.readFileSync(path);
	await checkBlobLike(t, expectedExtension, chunk);
}

async function testFalsePositive(t, filePath) {
	await t.is(await fileTypeFromFile(filePath), undefined);

	const chunk = fs.readFileSync(filePath);
	t.is(await fileTypeFromBuffer(chunk), undefined);
	t.is(await fileTypeFromBuffer(new Uint8Array(chunk)), undefined);
	t.is(await fileTypeFromBuffer(chunk.buffer), undefined);
}

async function getStreamAsUint8Array(stream) {
	return new Uint8Array(await getStreamAsArrayBuffer(stream));
}

async function testStreamWithWebStream(t, expectedExtension, path) {
	// Read the file into a buffer
	const fileBuffer = await readFile(path);
	// Create a Blob from the buffer
	const blob = new Blob([fileBuffer]);
	const webStream = await fileTypeStream(blob.stream());
	t.false(webStream.locked);
	const webStreamResult = await getStreamAsUint8Array(webStream);
	t.false(webStream.locked, 'Ensure web-stream is released');
	t.true(areUint8ArraysEqual(fileBuffer, webStreamResult));
}

let i = 0;
for (const fixture of getFixtures()) {
	const _test = failingFixture.has(fixture.filename) ? test.failing : test;

	_test(`${fixture.filename} ${i++} .fileTypeFromFile() method - same fileType`, testFromFile, fixture.type, fixture.path);
	_test(`${fixture.filename} ${i++} .fileTypeFromBuffer() method - same fileType`, testFromBuffer, fixture.type, fixture.path);
	_test(`${fixture.filename} ${i++} .fileTypeFromBlob() method - same fileType`, testFromBlob, fixture.type, fixture.path);
	test(`${fixture.filename} ${i++} .fileTypeStream() - identical Web Streams`, testStreamWithWebStream, fixture.type, fixture.path);

	if (Object.hasOwn(falsePositives, fixture.filename)) {
		for (const falsePositiveFile of falsePositives[fixture.filename]) {
			test(`false positive - ${fixture.filename} ${i++}`, testFalsePositive, fixture.filename, falsePositiveFile);
		}
	}
}

test('.fileTypeStream() method - empty stream', async t => {
	const newStream = await fileTypeStream(new ReadableStream({
		start(controller) {
			controller.close();
		},
	}));
	t.is(newStream.fileType, undefined);
});

test('.fileTypeStream() method - short stream', async t => {
	const bufferA = new Uint8Array([0, 1, 0, 1]);
	const shortStream = new ReadableStream({
		start(controller) {
			controller.enqueue(bufferA);
			controller.close();
		},
	});

	// Test filetype detection
	const newStream = await fileTypeStream(shortStream);
	t.is(newStream.fileType, undefined);

	// Test usability of returned stream
	const bufferB = await getStreamAsUint8Array(newStream);
	t.deepEqual(bufferA, bufferB);
});

test('.fileTypeStream() method - no end-of-stream errors', async t => {
	const file = path.join(__dirname, 'fixture', 'fixture.ogm');
	const stream = await fileTypeStream(new Blob([fs.readFileSync(file)]).stream(), {sampleSize: 30});
	t.is(stream.fileType, undefined);
});

test('.fileTypeStream() method - error event', async t => {
	const errorMessage = 'Fixture';

	const readableStream = new ReadableStream({
		pull() {
			throw new Error(errorMessage);
		},
	});

	await t.throwsAsync(fileTypeStream(readableStream), {message: errorMessage});
});

test('.fileTypeStream() method - sampleSize option', async t => {
	const file = path.join(__dirname, 'fixture', 'fixture.ogm');
	let stream = await fileTypeStream(new Blob([fs.readFileSync(file)]).stream(), {sampleSize: 30});
	t.is(typeof (stream.fileType), 'undefined', 'file-type cannot be determined with a sampleSize of 30');

	stream = await fileTypeStream(new Blob([fs.readFileSync(file)]).stream(), {sampleSize: 4100});
	t.is(typeof (stream.fileType), 'object', 'file-type can be determined with a sampleSize of 4100');
	t.is(stream.fileType.mime, 'video/ogg');
});

test('.fileTypeStream() preserves large caller-provided sampleSize values', async t => {
	const id3HeaderLength = 2 * 1024 * 1024;
	const id3Header = Uint8Array.from([
		0x49,
		0x44,
		0x33,
		0x04,
		0x00,
		0x00,
		...toSyncSafeInteger(id3HeaderLength),
	]);
	const mpegFrame = Uint8Array.from([0xFF, 0xFB, 0x90, 0x64, 0x00, 0x00, 0x00, 0x00]);
	const payload = Buffer.concat([Buffer.from(id3Header), Buffer.alloc(id3HeaderLength), Buffer.from(mpegFrame)]);
	const sampleSize = payload.length;

	let detectionStream = await fileTypeStream(createBufferedWebStream(payload, 64 * 1024), {sampleSize});
	t.deepEqual(detectionStream.fileType, {
		ext: 'mp3',
		mime: 'audio/mpeg',
	});

	detectionStream = await fileTypeStream(new Blob([payload]).stream(), {sampleSize});
	t.deepEqual(detectionStream.fileType, {
		ext: 'mp3',
		mime: 'audio/mpeg',
	});
});

test('.fileTypeFromStream() method - be able to abort operation', async t => {
	const abortController = new AbortController();
	const stalledStream = new ReadableStream({
		pull() {
			return new Promise((_resolve, reject) => {
				if (abortController.signal.aborted) {
					reject(abortController.signal.reason);
					return;
				}

				abortController.signal.addEventListener('abort', () => {
					reject(abortController.signal.reason);
				});
			});
		},
	});

	const parser = new FileTypeParser({signal: abortController.signal});
	const timeoutMilliseconds = 500;
	const promiseFileType = Promise.race([
		parser.fromStream(stalledStream),
		new Promise((_resolve, reject) => {
			setTimeout(() => {
				reject(new Error(`Timed out after ${timeoutMilliseconds} ms`));
			}, timeoutMilliseconds);
		}),
	]);
	abortController.abort();
	// The parser should resolve or reject quickly after abort, not time out
	const result = await promiseFileType;
	t.is(result, undefined);
});

test('.fileTypeFromStream() method - rejects immediately when the signal is already aborted', async t => {
	const stalledStream = new ReadableStream({
		pull() {
			return new Promise(() => {});
		},
	});
	const abortController = new AbortController();
	const timeoutMilliseconds = 200;
	abortController.abort();
	const error = await t.throwsAsync(Promise.race([
		fileTypeFromStream(stalledStream, {signal: abortController.signal}),
		new Promise((_resolve, reject) => {
			setTimeout(() => {
				reject(new Error(`Timed out after ${timeoutMilliseconds} ms`));
			}, timeoutMilliseconds);
		}),
	]));
	t.is(error.name, 'AbortError');
});

test('Does not falsely detect DWG for non-digit version strings like scientific notation', async t => {
	const buffer = Buffer.from('AC1e+3<html><script>alert(1)</script>');
	t.is(await fileTypeFromBuffer(buffer), undefined);
});

test('ID3 sync-safe integer masks MSBs on all bytes to prevent type confusion', async t => {
	// Byte 2 has MSB set (0x80), making the buggy parser compute 16384 instead of 0.
	// JPEG magic at offset 16394 would fool the old parser into detecting JPEG.
	const buffer = new Uint8Array(17_000);
	// ID3 header: "ID3" + version 3.0 + no flags + size [0x00, 0x00, 0x80, 0x00]
	buffer.set([0x49, 0x44, 0x33, 0x03, 0x00, 0x00, 0x00, 0x00, 0x80, 0x00]);
	// Place JPEG magic at position 16394 (where the buggy parser would look)
	buffer[16_394] = 0xFF;
	buffer[16_395] = 0xD8;
	buffer[16_396] = 0xFF;
	// With the fix, the parser sees size=0 and detects at position 10 (no JPEG there).
	const result = await fileTypeFromBuffer(buffer);
	t.not(result?.mime, 'image/jpeg');
});

test('.fileTypeFromStream() cancels a Web byte stream after successful detection', async t => {
	const jpegHeader = Buffer.from([0xFF, 0xD8, 0xFF, 0xDB]);
	const filler = Buffer.alloc(64 * 1024);
	const totalBytes = 4 * 1024 * 1024;
	let bodyBytesSent = 0;
	let responseClosed = false;
	let interval;

	const server = http.createServer((request, response) => {
		response.on('close', () => {
			responseClosed = true;
			clearInterval(interval);
		});
		response.writeHead(200, {
			'Content-Type': 'image/jpeg',
			'Content-Length': String(totalBytes),
		});
		response.write(jpegHeader);
		let sent = jpegHeader.length;
		interval = setInterval(() => {
			if (sent >= totalBytes) {
				clearInterval(interval);
				response.end();
				return;
			}

			const chunkLength = Math.min(filler.length, totalBytes - sent);
			sent += chunkLength;
			bodyBytesSent += chunkLength;
			response.write(filler.subarray(0, chunkLength));
		}, 10);
		interval.unref?.();
	});

	await new Promise(resolve => {
		server.listen(0, '127.0.0.1', resolve);
	});

	try {
		const {port} = server.address();
		const response = await fetch(`http://127.0.0.1:${port}/image.jpg`);
		const fileType = await fileTypeFromStream(response.body);
		t.deepEqual(fileType, {
			ext: 'jpg',
			mime: 'image/jpeg',
		});
		await new Promise(resolve => {
			setTimeout(resolve, 80);
		});

		t.true(responseClosed);
		t.true(bodyBytesSent < 128 * 1024);
	} finally {
		clearInterval(interval);
		server.closeAllConnections?.();
		server.close();
	}
});

test('.fileTypeStream() method - be able to abort stalled stream detection', async t => {
	const abortController = new AbortController();
	const stalledStream = new ReadableStream({
		pull() {
			return new Promise((_resolve, reject) => {
				abortController.signal.addEventListener('abort', () => {
					reject(abortController.signal.reason);
				});
			});
		},
	});
	const timeoutMilliseconds = 400;
	setTimeout(() => {
		abortController.abort();
	}, 50);
	const error = await t.throwsAsync(Promise.race([
		fileTypeStream(stalledStream, {signal: abortController.signal}),
		new Promise((_resolve, reject) => {
			setTimeout(() => {
				reject(new Error(`Timed out after ${timeoutMilliseconds} ms`));
			}, timeoutMilliseconds);
		}),
	]));
	t.is(error.name, 'AbortError');
});

test('.fileTypeFromStream() returns gzip for a stalled unknown-size gzip stream', async t => {
	const gzipPrefix = Uint8Array.from([31, 139, 8, 8, 137, 83, 29, 82, 0, 11]);
	const timeoutMilliseconds = 300;
	const stalledStream = new ReadableStream({
		pull(controller) {
			if (this.sent) {
				return new Promise(() => {});
			}

			this.sent = true;
			controller.enqueue(gzipPrefix);
			return new Promise(() => {});
		},
	});

	const type = await Promise.race([
		new FileTypeParser().fromStream(stalledStream),
		new Promise((_resolve, reject) => {
			setTimeout(() => {
				reject(new Error(`Timed out after ${timeoutMilliseconds} ms`));
			}, timeoutMilliseconds);
		}),
	]);
	assertGzipFileType(t, type);
});

test('supportedExtensions.has', t => {
	t.true(supportedExtensions.has('jpg'));
	t.false(supportedExtensions.has('blah'));
});

test('supportedMimeTypes.has', t => {
	t.true(supportedMimeTypes.has('video/mpeg'));
	t.false(supportedMimeTypes.has('video/blah'));
});

test('validate the input argument type', async t => {
	await t.throwsAsync(fileTypeFromBuffer('x'), {
		message: /Expected the `input` argument to be of type `Uint8Array`/v,
	});

	await t.notThrowsAsync(fileTypeFromBuffer(new Uint8Array()));

	await t.notThrowsAsync(fileTypeFromBuffer(new ArrayBuffer()));
});

test('validate the repo has all extensions and mimes in sync', t => {
	// File: source/*.js (base truth)
	function readIndexJS() {
		const sourceFiles = ['source/index.js', 'source/detectors/zip.js', 'source/detectors/ebml.js', 'source/detectors/png.js', 'source/detectors/asf.js'];
		const extensions = new Set();
		const mimes = new Set();
		for (const file of sourceFiles) {
			const content = fs.readFileSync(file, {encoding: 'utf8'});
			for (const extension of content.match(/(?<=ext:\s')(.*)(?=',)/gv) ?? []) {
				extensions.add(extension);
			}

			for (const mime of content.match(/(?<=mime:\s')(.*)(?=')/gv) ?? []) {
				mimes.add(mime);
			}
		}

		return {
			exts: extensions,
			mimes,
		};
	}

	// File: package.json
	function readPackageJSON() {
		const packageJson = fs.readFileSync('package.json', {encoding: 'utf8'});
		const {keywords} = JSON.parse(packageJson);

		const allowedExtras = new Set([
			'mime',
			'file',
			'type',
			'magic',
			'archive',
			'image',
			'img',
			'pic',
			'picture',
			'flash',
			'photo',
			'video',
			'detect',
			'check',
			'is',
			'exif',
			'binary',
			'buffer',
			'uint8array',
			'webassembly',
		]);

		const extensionArray = keywords.filter(keyword => !allowedExtras.has(keyword));
		return extensionArray;
	}

	// File: readme.md
	function readReadmeMD() {
		const index = fs.readFileSync('readme.md', {encoding: 'utf8'});
		const extensionArray = index.match(/(?<=-\s\[`)(.*)(?=`)/gv);
		return extensionArray;
	}

	// Helpers
	// Find extensions/mimes that are defined twice in a file
	function findDuplicates(input) {
		// TODO: Fix this.
		// eslint-disable-next-line unicorn/no-array-reduce
		return input.reduce((accumulator, element, index, array) => {
			if (array.indexOf(element) !== index && !accumulator.includes(element)) {
				accumulator.push(element);
			}

			return accumulator;
		}, []);
	}

	// Find extensions/mimes that are in another file but not in `index.js`
	function findExtras(array, set) {
		return array.filter(element => !set.has(element));
	}

	// Find extensions/mimes that are in `index.js` but missing from another file
	function findMissing(array, set) {
		const missing = [];
		const other = new Set(array);
		for (const elemenet of set) {
			if (!other.has(elemenet)) {
				missing.push(elemenet);
			}
		}

		return missing;
	}

	// Test runner
	function validate(found, baseTruth, filename, extensionOrMime) {
		const duplicates = findDuplicates(found);
		const extras = findExtras(found, baseTruth);
		const missing = findMissing(found, baseTruth);
		t.is(duplicates.length, 0, `Found duplicate ${extensionOrMime}: ${duplicates} in ${filename}.`);
		t.is(extras.length, 0, `Extra ${extensionOrMime}: ${extras} in ${filename}.`);
		t.is(missing.length, 0, `Missing ${extensionOrMime}: ${missing} in ${filename}.`);
	}

	// Get the base truth of extensions and mimes supported from core.js
	const {exts} = readIndexJS();

	// Validate all extensions
	const filesWithExtensions = {
		'supported.js': [...supportedExtensions],
		'package.json': readPackageJSON(),
		'readme.md': readReadmeMD(),
	};

	for (const filename in filesWithExtensions) {
		if (filesWithExtensions[filename]) {
			const foundExtensions = filesWithExtensions[filename];
			validate(foundExtensions, exts, filename, 'extensions');
		}
	}
});

function createBufferedWebStream(buffer, chunkSize = buffer.length) {
	let offset = 0;
	return new ReadableStream({
		pull(controller) {
			if (offset >= buffer.length) {
				controller.close();
				return;
			}

			const chunk = buffer.subarray(offset, offset + chunkSize);
			offset += chunk.length;
			controller.enqueue(chunk);
		},
	});
}

const hostileChunkPatterns = [
	[1],
	[2],
	[3],
	[5],
	[8],
	[13],
	[1, 2, 3, 5],
	[8, 1, 4, 2],
];

function createPatternWebStream(buffer, chunkPattern, {byteStream = false} = {}) {
	let offset = 0;
	let patternIndex = 0;
	const state = {
		emittedBytes: 0,
	};

	return {
		state,
		stream: new ReadableStream({
			...(byteStream && {type: 'bytes'}),
			pull(controller) {
				if (offset >= buffer.length) {
					controller.close();
					return;
				}

				const chunkSize = chunkPattern[patternIndex % chunkPattern.length];
				patternIndex++;
				const chunk = buffer.subarray(offset, offset + chunkSize);
				offset += chunk.length;
				state.emittedBytes += chunk.length;
				controller.enqueue(chunk);
			},
		}),
	};
}

async function assertUndefinedTypeFromBuffer(t, bytes) {
	const type = await fileTypeFromBuffer(bytes);
	t.is(type, undefined);
}

async function assertUndefinedTypeFromChunkedStream(t, bytes) {
	const type = await fileTypeFromStream(createBufferedWebStream(bytes, 8));
	t.is(type, undefined);
}

async function assertUndefinedTypeFromHostileStreams(t, bytes, description) {
	for (const chunkPattern of hostileChunkPatterns) {
		const type = await fileTypeFromStream(createPatternWebStream(bytes, chunkPattern).stream);
		t.is(type, undefined, `${description} with chunk pattern ${chunkPattern.join(',')}`);
	}
}

function assertZipFileType(t, type) {
	t.deepEqual(type, {
		ext: 'zip',
		mime: 'application/zip',
	});
}

function assertGzipFileType(t, type) {
	t.deepEqual(type, {
		ext: 'gz',
		mime: 'application/gzip',
	});
}

function assertTarGzipFileType(t, type) {
	t.deepEqual(type, {
		ext: 'tar.gz',
		mime: 'application/gzip',
	});
}

async function assertZipTypeFromBuffer(t, bytes) {
	const type = await fileTypeFromBuffer(bytes);
	assertZipFileType(t, type);
}

async function assertZipTypeFromBlob(t, bytes) {
	const type = await fileTypeFromBlob(new Blob([bytes]));
	assertZipFileType(t, type);
}

async function assertZipTypeFromChunkedStream(t, bytes) {
	const type = await fileTypeFromStream(createBufferedWebStream(bytes, 8));
	assertZipFileType(t, type);
}

async function assertZipTypeFromWebStream(t, bytes, chunkPattern = [8]) {
	const {stream} = createPatternWebStream(bytes, chunkPattern);
	const type = await new FileTypeParser().fromStream(stream);
	assertZipFileType(t, type);
}

async function assertFileTypeStreamChunkedResult(t, bytes, expectedFileType, options = {}) {
	const {
		chunkSize = 64 * 1024,
		sampleSize,
	} = options;
	const detectionStream = await fileTypeStream(createBufferedWebStream(bytes, chunkSize), {sampleSize});
	t.deepEqual(detectionStream.fileType, expectedFileType);
	t.true(areUint8ArraysEqual(await getStreamAsUint8Array(detectionStream), bytes));
}

async function assertFileTypeStreamWebResult(t, bytes, expectedFileType, options = {}) {
	const detectionStream = await fileTypeStream(new Blob([bytes]).stream(), options);
	t.deepEqual(detectionStream.fileType, expectedFileType);
	t.true(areUint8ArraysEqual(await getStreamAsUint8Array(detectionStream), bytes));
}

async function assertZipTypeFromFile(t, bytes) {
	const filePath = await createTemporaryTestFile(t, bytes);
	assertZipFileType(t, await fileTypeFromFile(filePath));
}

async function assertZipTypeFromKnownSizeInputs(t, bytes) {
	await assertZipTypeFromBuffer(t, bytes);
	await assertZipTypeFromBlob(t, bytes);
	await assertZipTypeFromFile(t, bytes);
}

async function assertZipTypeFromBufferAndChunkedStream(t, bytes) {
	await assertZipTypeFromBuffer(t, bytes);
	await assertZipTypeFromChunkedStream(t, bytes);
}

async function assertZipTypeFromAllDirectInputs(t, bytes) {
	await assertZipTypeFromBuffer(t, bytes);
	await assertZipTypeFromBlob(t, bytes);
	await assertZipTypeFromFile(t, bytes);
	await assertZipTypeFromChunkedStream(t, bytes);
}

async function assertFileTypeStreamFallsBackToZipWithLargeSampleSize(t, bytes) {
	await assertFileTypeStreamChunkedResult(t, bytes, {
		ext: 'zip',
		mime: 'application/zip',
	}, {sampleSize: bytes.length});
	await assertFileTypeStreamWebResult(t, bytes, {
		ext: 'zip',
		mime: 'application/zip',
	}, {sampleSize: bytes.length});
}

async function createTemporaryTestFile(t, bytes, extension = 'zip') {
	const temporaryDirectory = path.join(__dirname, '.ai-temporary');
	await fs.promises.mkdir(temporaryDirectory, {recursive: true});
	const filePath = path.join(temporaryDirectory, `file-type-${process.pid}-${Date.now()}-${Math.random().toString(16).slice(2)}.${extension}`);
	await fs.promises.writeFile(filePath, bytes);
	t.teardown(async () => {
		await fs.promises.unlink(filePath).catch(() => {});
	});
	return filePath;
}

async function createSparseTemporaryTestFile(t, bytes, size, extension = 'zip') {
	const filePath = await createTemporaryTestFile(t, bytes, extension);
	await fs.promises.truncate(filePath, size);
	return filePath;
}

async function createTemporaryDirectory(t) {
	const temporaryDirectory = await fs.promises.mkdtemp(path.join(os.tmpdir(), 'file-type-'));
	t.teardown(async () => {
		await fs.promises.rm(temporaryDirectory, {recursive: true, force: true}).catch(() => {});
	});

	return temporaryDirectory;
}

async function createTemporaryFifo(t) {
	const temporaryDirectory = await createTemporaryDirectory(t);
	const filePath = path.join(temporaryDirectory, 'test.fifo');
	const result = spawnSync('mkfifo', [filePath]);
	if (result.status !== 0) {
		throw new Error(`mkfifo failed: ${result.stderr.toString()}`);
	}

	return filePath;
}

function createZipLocalFile({
	filename,
	generalPurposeBitFlag = 0,
	compressedMethod = 0,
	compressedData = new Uint8Array(0),
	compressedSize = compressedData.length,
	uncompressedSize = compressedData.length,
}) {
	const filenameBytes = new TextEncoder().encode(filename);
	const header = new Uint8Array(30 + filenameBytes.length);
	const view = new DataView(header.buffer);
	view.setUint32(0, 0x04_03_4B_50, true);
	view.setUint16(4, 20, true);
	view.setUint16(6, generalPurposeBitFlag, true);
	view.setUint16(8, compressedMethod, true);
	view.setUint16(10, 0, true);
	view.setUint16(12, 0, true);
	view.setUint32(14, 0, true);
	view.setUint32(18, compressedSize, true);
	view.setUint32(22, uncompressedSize, true);
	view.setUint16(26, filenameBytes.length, true);
	view.setUint16(28, 0, true);
	header.set(filenameBytes, 30);

	return Buffer.concat([Buffer.from(header), Buffer.from(compressedData)]);
}

function createZipDataDescriptor({compressedSize = 0, uncompressedSize = compressedSize, crc32 = 0} = {}) {
	const descriptor = new Uint8Array(16);
	const view = new DataView(descriptor.buffer);
	view.setUint32(0, 0x08_07_4B_50, true);
	view.setUint32(4, crc32, true);
	view.setUint32(8, compressedSize, true);
	view.setUint32(12, uncompressedSize, true);
	return descriptor;
}

function createZipDataDescriptorFile({filename, compressedMethod = 0, compressedData = new Uint8Array(0), uncompressedSize = compressedData.length, descriptor = createZipDataDescriptor({compressedSize: compressedData.length, uncompressedSize})} = {}) {
	return Buffer.concat([
		createZipLocalFile({
			filename,
			generalPurposeBitFlag: 0x08,
			compressedMethod,
			compressedData,
			compressedSize: 0,
			uncompressedSize: 0,
		}),
		Buffer.from(descriptor),
	]);
}

const descriptorBoundaryEpubFileType = {
	ext: 'epub',
	mime: 'application/epub+zip',
};

const descriptorBoundaryDocmFileType = {
	ext: 'docm',
	mime: 'application/vnd.ms-word.document.macroenabled.12',
};

const descriptorBoundaryContentTypesXml = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';

function createZipWithLeadingDescriptorEntry(descriptorSize, trailingEntries) {
	const irrelevantDescriptorEntry = createZipDataDescriptorFile({
		filename: 'irrelevant.bin',
		compressedData: Buffer.alloc(descriptorSize),
	});

	return Buffer.concat([irrelevantDescriptorEntry, ...trailingEntries]);
}

function createZipWithRepeatedDescriptorEntries(entryCount, descriptorSize, trailingEntries) {
	const entries = [];

	for (let index = 0; index < entryCount; index++) {
		entries.push(createZipDataDescriptorFile({
			filename: `irrelevant-${index}.bin`,
			compressedData: Buffer.alloc(descriptorSize),
		}));
	}

	return Buffer.concat([...entries, ...trailingEntries]);
}

function createZipWithRepeatedDescriptorEntriesAtKnownSizeBudget(trailingEntries, exceededBytes = 0) {
	const filenames = ['irrelevant-0.bin', 'irrelevant-1.bin'];
	const firstPayloadSize = Math.floor(maximumZipTextEntrySizeInBytes / 4);
	const secondPayloadSize = (maximumZipTextEntrySizeInBytes - firstPayloadSize) + exceededBytes;

	return Buffer.concat([
		createZipDataDescriptorFile({
			filename: filenames[0],
			compressedData: Buffer.alloc(firstPayloadSize),
		}),
		createZipDataDescriptorFile({
			filename: filenames[1],
			compressedData: Buffer.alloc(secondPayloadSize),
		}),
		...trailingEntries,
	]);
}

function createZipWithLeadingDescriptorMimetype(descriptorSize) {
	return createZipWithLeadingDescriptorEntry(descriptorSize, [
		createZipLocalFile({
			filename: 'mimetype',
			compressedData: new TextEncoder().encode('application/epub+zip'),
		}),
	]);
}

function createZipWithRepeatedDescriptorMimetype(entryCount, descriptorSize) {
	return createZipWithRepeatedDescriptorEntries(entryCount, descriptorSize, [
		createZipLocalFile({
			filename: 'mimetype',
			compressedData: new TextEncoder().encode('application/epub+zip'),
		}),
	]);
}

function createZipWithRepeatedDescriptorMimetypeAtKnownSizeBudget(exceededBytes = 0) {
	return createZipWithRepeatedDescriptorEntriesAtKnownSizeBudget([
		createZipLocalFile({
			filename: 'mimetype',
			compressedData: new TextEncoder().encode('application/epub+zip'),
		}),
	], exceededBytes);
}

function createZipWithLeadingDescriptorContentTypes(descriptorSize) {
	return createZipWithLeadingDescriptorEntry(descriptorSize, [
		createZipLocalFile({
			filename: 'word/document.xml',
			compressedData: new TextEncoder().encode('<w:document/>'),
		}),
		createZipLocalFile({
			filename: '[Content_Types].xml',
			compressedData: new TextEncoder().encode(descriptorBoundaryContentTypesXml),
		}),
	]);
}

function createZipWithRepeatedDescriptorContentTypes(entryCount, descriptorSize) {
	return createZipWithRepeatedDescriptorEntries(entryCount, descriptorSize, [
		createZipLocalFile({
			filename: 'word/document.xml',
			compressedData: new TextEncoder().encode('<w:document/>'),
		}),
		createZipLocalFile({
			filename: '[Content_Types].xml',
			compressedData: new TextEncoder().encode(descriptorBoundaryContentTypesXml),
		}),
	]);
}

function createZipWithRepeatedDescriptorContentTypesAtKnownSizeBudget(exceededBytes = 0) {
	return createZipWithRepeatedDescriptorEntriesAtKnownSizeBudget([
		createZipLocalFile({
			filename: 'word/document.xml',
			compressedData: new TextEncoder().encode('<w:document/>'),
		}),
		createZipLocalFile({
			filename: '[Content_Types].xml',
			compressedData: new TextEncoder().encode(descriptorBoundaryContentTypesXml),
		}),
	], exceededBytes);
}

function createZipWithLeadingStoredEntry(entrySize, trailingEntries) {
	const irrelevantStoredEntry = createZipLocalFile({
		filename: 'irrelevant.bin',
		compressedData: Buffer.alloc(entrySize),
	});

	return Buffer.concat([irrelevantStoredEntry, ...trailingEntries]);
}

function createZipWithRepeatedStoredEntries(entryCount, entrySize, trailingEntries) {
	const entries = [];

	for (let index = 0; index < entryCount; index++) {
		entries.push(createZipLocalFile({
			filename: `irrelevant-${index}.bin`,
			compressedData: Buffer.alloc(entrySize),
		}));
	}

	return Buffer.concat([...entries, ...trailingEntries]);
}

function createZipWithRepeatedStoredEntriesAtCumulativeLimit(trailingEntries) {
	const entries = [];
	let consumedBytes = 0;

	for (let index = 0; consumedBytes < maximumUntrustedSkipSizeInBytes; index++) {
		const filename = `irrelevant-${index}.bin`;
		const headerSize = 30 + new TextEncoder().encode(filename).length;
		const remainingBytes = maximumUntrustedSkipSizeInBytes - consumedBytes;
		const entrySize = Math.min(maximumZipTextEntrySizeInBytes, remainingBytes - headerSize);

		entries.push(createZipLocalFile({
			filename,
			compressedData: Buffer.alloc(entrySize),
		}));
		consumedBytes += headerSize + entrySize;
	}

	return Buffer.concat([...entries, ...trailingEntries]);
}

function createZipWithLeadingStoredMimetype(entrySize) {
	return createZipWithLeadingStoredEntry(entrySize, [
		createZipLocalFile({
			filename: 'mimetype',
			compressedData: new TextEncoder().encode('application/epub+zip'),
		}),
	]);
}

function createZipWithLeadingStoredContentTypes(entrySize) {
	return createZipWithLeadingStoredEntry(entrySize, [
		createZipLocalFile({
			filename: 'word/document.xml',
			compressedData: new TextEncoder().encode('<w:document/>'),
		}),
		createZipLocalFile({
			filename: '[Content_Types].xml',
			compressedData: new TextEncoder().encode(descriptorBoundaryContentTypesXml),
		}),
	]);
}

function createZipWithLeadingStoredDescriptorMimetype(entrySize) {
	return createZipWithLeadingStoredEntry(entrySize, [
		createZipDataDescriptorFile({
			filename: 'mimetype',
			compressedData: new TextEncoder().encode('application/epub+zip'),
		}),
	]);
}

function createZipWithLeadingStoredDescriptorContentTypes(entrySize) {
	return createZipWithLeadingStoredEntry(entrySize, [
		createZipLocalFile({
			filename: 'word/document.xml',
			compressedData: new TextEncoder().encode('<w:document/>'),
		}),
		createZipDataDescriptorFile({
			filename: '[Content_Types].xml',
			compressedData: new TextEncoder().encode(descriptorBoundaryContentTypesXml),
		}),
	]);
}

function createZipWithRepeatedStoredMimetype(entryCount, entrySize) {
	return createZipWithRepeatedStoredEntries(entryCount, entrySize, [
		createZipLocalFile({
			filename: 'mimetype',
			compressedData: new TextEncoder().encode('application/epub+zip'),
		}),
	]);
}

function createZipWithRepeatedStoredMimetypeAtCumulativeLimit() {
	return createZipWithRepeatedStoredEntriesAtCumulativeLimit([
		createZipLocalFile({
			filename: 'mimetype',
			compressedData: new TextEncoder().encode('application/epub+zip'),
		}),
	]);
}

function createZipWithRepeatedStoredContentTypes(entryCount, entrySize) {
	return createZipWithRepeatedStoredEntries(entryCount, entrySize, [
		createZipLocalFile({
			filename: 'word/document.xml',
			compressedData: new TextEncoder().encode('<w:document/>'),
		}),
		createZipLocalFile({
			filename: '[Content_Types].xml',
			compressedData: new TextEncoder().encode(descriptorBoundaryContentTypesXml),
		}),
	]);
}

function createZipWithRepeatedStoredContentTypesAtCumulativeLimit() {
	return createZipWithRepeatedStoredEntriesAtCumulativeLimit([
		createZipLocalFile({
			filename: 'word/document.xml',
			compressedData: new TextEncoder().encode('<w:document/>'),
		}),
		createZipLocalFile({
			filename: '[Content_Types].xml',
			compressedData: new TextEncoder().encode(descriptorBoundaryContentTypesXml),
		}),
	]);
}

function createZipTextEntryExceedingProbeLimit(text) {
	return text + ' '.repeat((maximumZipTextEntrySizeInBytes + 1) - text.length);
}

function createDeflatedZipWithUnderstatedMimetypeSize() {
	const mimetype = createZipTextEntryExceedingProbeLimit('application/epub+zip');
	return createZipLocalFile({
		filename: 'mimetype',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(mimetype)),
		uncompressedSize: 1,
	});
}

function createDeflatedZipWithUnderstatedContentTypesSize() {
	const contentTypesXml = createZipTextEntryExceedingProbeLimit(descriptorBoundaryContentTypesXml);
	return Buffer.concat([
		createZipLocalFile({
			filename: 'word/document.xml',
			compressedData: new TextEncoder().encode('<w:document/>'),
		}),
		createZipLocalFile({
			filename: '[Content_Types].xml',
			compressedMethod: 8,
			compressedData: deflateRawSync(Buffer.from(contentTypesXml)),
			uncompressedSize: 1,
		}),
	]);
}

function createZipArchive(entries) {
	const localFiles = [];
	const centralDirectoryEntries = [];
	let offset = 0;

	for (const entry of entries) {
		const {
			filename,
			generalPurposeBitFlag = 0,
			compressedMethod = 0,
			compressedData = new Uint8Array(0),
			compressedSize = compressedData.length,
			uncompressedSize = compressedData.length,
		} = entry;
		const filenameBytes = new TextEncoder().encode(filename);
		const localFile = createZipLocalFile({
			filename,
			generalPurposeBitFlag,
			compressedMethod,
			compressedData,
			compressedSize,
			uncompressedSize,
		});
		localFiles.push(localFile);

		const centralDirectoryEntry = new Uint8Array(46 + filenameBytes.length);
		const view = new DataView(centralDirectoryEntry.buffer);
		view.setUint32(0, 0x02_01_4B_50, true);
		view.setUint16(4, 20, true);
		view.setUint16(6, 20, true);
		view.setUint16(8, generalPurposeBitFlag, true);
		view.setUint16(10, compressedMethod, true);
		view.setUint16(12, 0, true);
		view.setUint16(14, 0, true);
		view.setUint32(16, 0, true);
		view.setUint32(20, compressedSize, true);
		view.setUint32(24, uncompressedSize, true);
		view.setUint16(28, filenameBytes.length, true);
		view.setUint16(30, 0, true);
		view.setUint16(32, 0, true);
		view.setUint16(34, 0, true);
		view.setUint16(36, 0, true);
		view.setUint32(38, 0, true);
		view.setUint32(42, offset, true);
		centralDirectoryEntry.set(filenameBytes, 46);
		centralDirectoryEntries.push(Buffer.from(centralDirectoryEntry));
		offset += localFile.length;
	}

	const centralDirectory = Buffer.concat(centralDirectoryEntries);
	const endOfCentralDirectory = new Uint8Array(22);
	const view = new DataView(endOfCentralDirectory.buffer);
	view.setUint32(0, 0x06_05_4B_50, true);
	view.setUint16(4, 0, true);
	view.setUint16(6, 0, true);
	view.setUint16(8, entries.length, true);
	view.setUint16(10, entries.length, true);
	view.setUint32(12, centralDirectory.length, true);
	view.setUint32(16, offset, true);
	view.setUint16(20, 0, true);

	return Buffer.concat([...localFiles, centralDirectory, Buffer.from(endOfCentralDirectory)]);
}

function createZipArchiveWithEntryAtIndex(entryCount, entryIndex, entry) {
	const entries = [];
	for (let index = 0; index < entryCount; ++index) {
		if (index === entryIndex) {
			entries.push(entry);
			continue;
		}

		entries.push({
			filename: `entry-${String(index).padStart(4, '0')}.txt`,
		});
	}

	return createZipArchive(entries);
}

function toSyncSafeInteger(value) {
	return Uint8Array.from([
		(value >> 21) & 0x7F,
		(value >> 14) & 0x7F,
		(value >> 7) & 0x7F,
		value & 0x7F,
	]);
}

function createRepeatedId3Payload(repetitions, payloadSizeInBytes) {
	const header = new Uint8Array(10);
	header[0] = 0x49;
	header[1] = 0x44;
	header[2] = 0x33;
	header.set(toSyncSafeInteger(payloadSizeInBytes), 6);

	const segment = new Uint8Array(10 + payloadSizeInBytes);
	segment.set(header, 0);

	const output = new Uint8Array(segment.length * repetitions);
	for (let index = 0; index < repetitions; index++) {
		output.set(segment, index * segment.length);
	}

	return output;
}

function encodeEbmlVariableSizeInteger(value) {
	for (let length = 1; length <= 8; length++) {
		const maximumValue = (2 ** (7 * length)) - 2;
		if (value <= maximumValue) {
			const bytes = new Uint8Array(length);
			let remaining = value;
			for (let index = length - 1; index >= 0; index--) {
				bytes[index] = remaining & 0xFF;
				remaining = Math.floor(remaining / 256);
			}

			bytes[0] |= 1 << (8 - length);
			return bytes;
		}
	}

	throw new RangeError(`Unsupported EBML size ${value}`);
}

function createEbmlElement(idBytes, payload = new Uint8Array(0)) {
	return Buffer.concat([
		Buffer.from(idBytes),
		Buffer.from(encodeEbmlVariableSizeInteger(payload.length)),
		Buffer.from(payload),
	]);
}

function createEbmlWithRepeatedUnknownChildren(childCount, childPayloadSizeInBytes, documentType) {
	const children = [];

	for (let index = 0; index < childCount; index++) {
		children.push(createEbmlElement([0x81], new Uint8Array(childPayloadSizeInBytes)));
	}

	if (documentType) {
		children.push(createEbmlElement([0x42, 0x82], new TextEncoder().encode(documentType)));
	}

	const rootPayload = Buffer.concat(children);
	return createEbmlElement([0x1A, 0x45, 0xDF, 0xA3], rootPayload);
}

function createEbmlWithUnknownPayloadBeforeDocumentType(payloadSizeInBytes, documentType) {
	return createEbmlElement([0x1A, 0x45, 0xDF, 0xA3], Buffer.concat([
		createEbmlElement([0x81], new Uint8Array(payloadSizeInBytes)),
		createEbmlElement([0x42, 0x82], new TextEncoder().encode(documentType)),
	]));
}

function createNestedGzip(buffer, depth) {
	let output = buffer;
	for (let index = 0; index < depth; index++) {
		output = gzipSync(output);
	}

	return output;
}

function createOversizedZipMimetypeEntry() {
	// Force declared sizes to the 32-bit max to verify detection stays bounded even when metadata is attacker-controlled.
	return createZipLocalFile({
		filename: 'mimetype',
		compressedSize: 0xFF_FF_FF_FF,
		uncompressedSize: 0xFF_FF_FF_FF,
	});
}

function createAsfObject(id, payload = new Uint8Array(0)) {
	const object = new Uint8Array(24 + payload.length);
	const view = new DataView(object.buffer);
	object.set(id, 0);
	view.setBigUint64(16, BigInt(object.length), true);
	object.set(payload, 24);
	return object;
}

function createAsfHeader(objects) {
	const header = new Uint8Array(30);
	header.set([0x30, 0x26, 0xB2, 0x75, 0x8E, 0x66, 0xCF, 0x11, 0xA6, 0xD9], 0);
	return Buffer.concat([Buffer.from(header), ...objects.map(object => Buffer.from(object))]);
}

function createAsfStreamHeaderWithMetadataObjects(metadataObjectCount, streamTypeId) {
	const metadataObjectId = Uint8Array.from([0xA1, 0xDC, 0xAB, 0x8C, 0x47, 0xA9, 0xCF, 0x11, 0x8E, 0xE4, 0x00, 0xC0, 0x0C, 0x20, 0x53, 0x65]);
	const metadataObjects = [];

	for (let index = 0; index < metadataObjectCount; index++) {
		metadataObjects.push(createAsfObject(metadataObjectId));
	}

	const streamPropertiesObject = createAsfObject(
		Uint8Array.from([0x91, 0x07, 0xDC, 0xB7, 0xB7, 0xA9, 0xCF, 0x11, 0x8E, 0xE6, 0x00, 0xC0, 0x0C, 0x20, 0x53, 0x65]),
		streamTypeId,
	);

	return createAsfHeader([...metadataObjects, streamPropertiesObject]);
}

function createAsfAudioHeaderWithMetadataObjects(metadataObjectCount) {
	return createAsfStreamHeaderWithMetadataObjects(metadataObjectCount, Uint8Array.from([0x40, 0x9E, 0x69, 0xF8, 0x4D, 0x5B, 0xCF, 0x11, 0xA8, 0xFD, 0x00, 0x80, 0x5F, 0x5C, 0x44, 0x2B]));
}

function createAsfVideoHeaderWithMetadataObjects(metadataObjectCount) {
	return createAsfStreamHeaderWithMetadataObjects(metadataObjectCount, Uint8Array.from([0xC0, 0xEF, 0x19, 0xBC, 0x4D, 0x5B, 0xCF, 0x11, 0xA8, 0xFD, 0x00, 0x80, 0x5F, 0x5C, 0x44, 0x2B]));
}

function createAsfUnknownStreamHeaderWithMetadataObjects(metadataObjectCount) {
	return createAsfStreamHeaderWithMetadataObjects(metadataObjectCount, Uint8Array.from([0x00, 0x01, 0x02, 0x03, 0x4D, 0x5B, 0xCF, 0x11, 0xA8, 0xFD, 0x00, 0x80, 0x5F, 0x5C, 0x44, 0x2B]));
}

function createAsfAudioHeaderWithUnknownPayload(payloadSize) {
	const metadataObjectId = Uint8Array.from([0xA1, 0xDC, 0xAB, 0x8C, 0x47, 0xA9, 0xCF, 0x11, 0x8E, 0xE4, 0x00, 0xC0, 0x0C, 0x20, 0x53, 0x65]);
	const metadataObject = createAsfObject(metadataObjectId, new Uint8Array(payloadSize));
	const streamPropertiesObject = createAsfObject(
		Uint8Array.from([0x91, 0x07, 0xDC, 0xB7, 0xB7, 0xA9, 0xCF, 0x11, 0x8E, 0xE6, 0x00, 0xC0, 0x0C, 0x20, 0x53, 0x65]),
		Uint8Array.from([0x40, 0x9E, 0x69, 0xF8, 0x4D, 0x5B, 0xCF, 0x11, 0xA8, 0xFD, 0x00, 0x80, 0x5F, 0x5C, 0x44, 0x2B]),
	);

	return createAsfHeader([metadataObject, streamPropertiesObject]);
}

function createAsfAudioHeaderWithHeaderExtensionPayload(payloadSize) {
	const headerExtensionObjectId = Uint8Array.from([0xB5, 0x03, 0xBF, 0x5F, 0x2E, 0xA9, 0xCF, 0x11, 0x8E, 0xE3, 0x00, 0xC0, 0x0C, 0x20, 0x53, 0x65]);
	const headerExtensionObject = createAsfObject(headerExtensionObjectId, new Uint8Array(payloadSize));
	const streamPropertiesObject = createAsfObject(
		Uint8Array.from([0x91, 0x07, 0xDC, 0xB7, 0xB7, 0xA9, 0xCF, 0x11, 0x8E, 0xE6, 0x00, 0xC0, 0x0C, 0x20, 0x53, 0x65]),
		Uint8Array.from([0x40, 0x9E, 0x69, 0xF8, 0x4D, 0x5B, 0xCF, 0x11, 0xA8, 0xFD, 0x00, 0x80, 0x5F, 0x5C, 0x44, 0x2B]),
	);

	return createAsfHeader([headerExtensionObject, streamPropertiesObject]);
}

function createPngChunk(type, data = new Uint8Array(0)) {
	const chunk = new Uint8Array(12 + data.length);
	const view = new DataView(chunk.buffer);
	view.setUint32(0, data.length);
	chunk.set(new TextEncoder().encode(type), 4);
	chunk.set(data, 8);
	return chunk;
}

function createPngWithAncillaryChunks(ancillaryChunkCount, ancillaryChunkData = new Uint8Array(0)) {
	const signature = Uint8Array.from([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]);
	const ihdrData = Uint8Array.from([0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0x08, 0x02, 0x00, 0x00, 0x00]);
	const chunks = [Buffer.from(createPngChunk('IHDR', ihdrData))];

	for (let index = 0; index < ancillaryChunkCount; index++) {
		chunks.push(Buffer.from(createPngChunk('tEXt', ancillaryChunkData)));
	}

	chunks.push(Buffer.from(createPngChunk('IDAT')));
	return Buffer.concat([Buffer.from(signature), ...chunks]);
}

function createPngWithAncillaryChunksAndAnimationControl(ancillaryChunkCount, ancillaryChunkData = new Uint8Array(0)) {
	const signature = Uint8Array.from([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]);
	const ihdrData = Uint8Array.from([0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0x08, 0x02, 0x00, 0x00, 0x00]);
	const animationControlData = Uint8Array.from([0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00]);
	const chunks = [Buffer.from(createPngChunk('IHDR', ihdrData))];

	for (let index = 0; index < ancillaryChunkCount; index++) {
		chunks.push(Buffer.from(createPngChunk('tEXt', ancillaryChunkData)));
	}

	chunks.push(
		Buffer.from(createPngChunk('acTL', animationControlData)),
		Buffer.from(createPngChunk('IDAT')),
	);
	return Buffer.concat([Buffer.from(signature), ...chunks]);
}

function createPngWithAncillaryPayloadBeforeIdat(payloadSize) {
	const signature = Uint8Array.from([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]);
	const ihdrData = Uint8Array.from([0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0x08, 0x02, 0x00, 0x00, 0x00]);
	return Buffer.concat([
		Buffer.from(signature),
		Buffer.from(createPngChunk('IHDR', ihdrData)),
		Buffer.from(createPngChunk('tEXt', new Uint8Array(payloadSize))),
		Buffer.from(createPngChunk('IDAT')),
	]);
}

function createPngWithAncillaryPayloadBeforeAnimationControl(payloadSize) {
	const signature = Uint8Array.from([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]);
	const ihdrData = Uint8Array.from([0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0x08, 0x02, 0x00, 0x00, 0x00]);
	const animationControlData = Uint8Array.from([0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00]);
	return Buffer.concat([
		Buffer.from(signature),
		Buffer.from(createPngChunk('IHDR', ihdrData)),
		Buffer.from(createPngChunk('tEXt', new Uint8Array(payloadSize))),
		Buffer.from(createPngChunk('acTL', animationControlData)),
		Buffer.from(createPngChunk('IDAT')),
	]);
}

function createPngWithCriticalPayloadBeforeIdat(type, payloadSize) {
	const signature = Uint8Array.from([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]);
	const ihdrData = Uint8Array.from([0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0x08, 0x02, 0x00, 0x00, 0x00]);
	return Buffer.concat([
		Buffer.from(signature),
		Buffer.from(createPngChunk('IHDR', ihdrData)),
		Buffer.from(createPngChunk(type, new Uint8Array(payloadSize))),
		Buffer.from(createPngChunk('IDAT')),
	]);
}

function createPngWithLeadingCgbiChunk() {
	const signature = Uint8Array.from([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]);
	const ihdrData = Uint8Array.from([0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0x08, 0x02, 0x00, 0x00, 0x00]);
	return Buffer.concat([
		Buffer.from(signature),
		Buffer.from(createPngChunk('CgBI')),
		Buffer.from(createPngChunk('IHDR', ihdrData)),
		Buffer.from(createPngChunk('IDAT')),
	]);
}

function createTiffWithTagIds(tagIds, bigEndian = false, ifdOffset = 8) {
	const buffer = new Uint8Array(ifdOffset + 2 + (tagIds.length * 12) + 4);
	const view = new DataView(buffer.buffer);
	buffer.set(bigEndian ? [0x4D, 0x4D, 0x00, 0x2A] : [0x49, 0x49, 0x2A, 0x00], 0);
	view.setUint32(4, ifdOffset, !bigEndian);
	view.setUint16(ifdOffset, tagIds.length, !bigEndian);

	let offset = ifdOffset + 2;
	for (const tagId of tagIds) {
		view.setUint16(offset, tagId, !bigEndian);
		offset += 12;
	}

	return buffer;
}

function createLittleEndianTiffWithTagIds(tagIds) {
	return createTiffWithTagIds(tagIds);
}

function createLittleEndianTiffWithTagIdsAtOffset(tagIds, ifdOffset) {
	return createTiffWithTagIds(tagIds, false, ifdOffset);
}

function createLittleEndianTiffWithTagIdAtIndex(tagCount, tagIndex, tagId) {
	const tagIds = Array.from({length: tagCount}, () => 0);
	tagIds[tagIndex] = tagId;
	return createLittleEndianTiffWithTagIds(tagIds);
}

function createBigEndianTiffWithTagIdAtIndex(tagCount, tagIndex, tagId) {
	const tagIds = Array.from({length: tagCount}, () => 0);
	tagIds[tagIndex] = tagId;
	return createTiffWithTagIds(tagIds, true);
}

test('odd file sizes', async t => {
	const oddFileSizes = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 255, 256, 257, 511, 512, 513];

	for (const size of oddFileSizes) {
		const buffer = new Uint8Array(size);
		await t.notThrowsAsync(fileTypeFromBuffer(buffer), `fromBuffer: File size: ${size} bytes`);
	}

	for (const size of oddFileSizes) {
		const buffer = new Uint8Array(size);
		const stream = createBufferedWebStream(buffer);
		await t.notThrowsAsync(fileTypeFromStream(stream), `fromStream: File size: ${size} bytes`);
	}
});

test('supported files types are listed alphabetically', async t => {
	const readme = await fs.promises.readFile('readme.md', {encoding: 'utf8'});
	let currentNode = new ReadmeParser().parse(readme).firstChild;

	while (currentNode) {
		if (currentNode.type === 'heading' && currentNode.firstChild.literal === 'Supported file types') {
			// Header → (skip non-list nodes) → List → First list item
			currentNode = currentNode.next;
			while (currentNode && currentNode.type !== 'list') {
				currentNode = currentNode.next;
			}

			currentNode = currentNode.firstChild;
			break;
		}

		currentNode = currentNode.next;
	}

	let previousFileType;

	while (currentNode) {
		// List item → Paragraph → Link → Inline code → Text
		const currentFileType = currentNode.firstChild.firstChild.firstChild.literal;

		t.true(!previousFileType || currentFileType > previousFileType, `${currentFileType} should be listed before ${previousFileType}`);

		previousFileType = currentFileType;
		currentNode = currentNode.next;
	}
});

// TODO: Replace with `Set.symmetricDifference` when targeting Node.js 22.
function symmetricDifference(setA, setB) {
	const diff = new Set();
	for (const item of setA) {
		if (!setB.has(item)) {
			diff.add(item);
		}
	}

	for (const item of setB) {
		if (!setA.has(item)) {
			diff.add(item);
		}
	}

	return diff;
}

test('implemented MIME types and extensions match the list of supported ones', async t => {
	const mimeTypesWithoutUnitTest = [
		'application/vnd.ms-asf',
		'image/heic-sequence',
	];

	const implementedMimeTypes = new Set(mimeTypesWithoutUnitTest);
	const implementedExtensions = new Set();

	for (const {path} of getFixtures()) {
		const fileType = await fileTypeFromFile(path);
		if (fileType) {
			implementedMimeTypes.add(fileType.mime);
			implementedExtensions.add(fileType.ext);
		}
	}

	const differencesInMimeTypes = symmetricDifference(supportedMimeTypes, implementedMimeTypes);

	for (const difference of differencesInMimeTypes) {
		if (implementedMimeTypes.has(difference)) {
			t.fail(`MIME-type ${difference} is implemented, but not declared as a supported MIME-type`);
		} else {
			t.fail(`MIME-type ${difference} declared as a supported MIME-type, but not found as an implemented MIME-type`);
		}
	}

	t.is(differencesInMimeTypes.size, 0);

	const differencesInExtensions = symmetricDifference(supportedExtensions, implementedExtensions);
	for (const difference of differencesInExtensions) {
		if (implementedMimeTypes.has(difference)) {
			t.fail(`Extension ${difference} is implemented, but not declared as a supported extension`);
		} else {
			t.fail(`Extension ${difference} declared as a supported extension, but not found as an implemented extension`);
		}
	}

	t.is(differencesInExtensions.size, 0);
});

test('corrupt MKV returns undefined', async t => {
	const filePath = path.join(__dirname, 'fixture/fixture-corrupt.mkv');
	const type = await fileTypeFromFile(filePath);
	t.is(type, undefined);
});

// Create a custom detector for the just made up "unicorn" file type
const unicornDetector = {
	id: 'mock.unicorn',
	async detect(tokenizer) {
		const unicornHeader = [85, 78, 73, 67, 79, 82, 78]; // "UNICORN" as decimal string
		const buffer = new Uint8Array(7);
		await tokenizer.peekBuffer(buffer, {length: unicornHeader.length, mayBeLess: true});
		if (unicornHeader.every((value, index) => value === buffer[index])) {
			return {ext: 'unicorn', mime: 'application/unicorn'};
		}

		return undefined;
	},
};

const mockPngDetector = {
	id: 'mock.png',
	detect: () => ({ext: 'mockPng', mime: 'image/mockPng'}),
};

const tokenizerPositionChanger = {
	id: 'mock.dirtyTokenizer',
	detect(tokenizer) {
		const buffer = new Uint8Array(1);
		tokenizer.readBuffer(buffer, {length: 1, mayBeLess: true});
	},
};

test('fileTypeFromBlob should detect custom file type "unicorn" using custom detectors', async t => {
	// Set up the "unicorn" file content
	const header = 'UNICORN FILE\n';
	const blob = new Blob([header]);

	const customDetectors = [unicornDetector];
	const parser = new FileTypeParser({customDetectors});

	const result = await parser.fromBlob(blob);
	t.deepEqual(result, {ext: 'unicorn', mime: 'application/unicorn'});
});

test('fileTypeFromBlob should keep detecting default file types when no custom detector matches', async t => {
	const file = path.join(__dirname, 'fixture', 'fixture.png');
	const chunk = fs.readFileSync(file);
	const blob = new Blob([chunk]);

	const customDetectors = [unicornDetector];
	const parser = new FileTypeParser({customDetectors});

	const result = await parser.fromBlob(blob);
	t.deepEqual(result, {ext: 'png', mime: 'image/png'});
});

test('fileTypeFromBlob should allow overriding default file type detectors', async t => {
	const file = path.join(__dirname, 'fixture', 'fixture.png');
	const chunk = fs.readFileSync(file);
	const blob = new Blob([chunk]);

	const customDetectors = [mockPngDetector];
	const parser = new FileTypeParser({customDetectors});

	const result = await parser.fromBlob(blob);
	t.deepEqual(result, {ext: 'mockPng', mime: 'image/mockPng'});
});

test('fileTypeFromBuffer should detect custom file type "unicorn" using custom detectors', async t => {
	const header = 'UNICORN FILE\n';
	const uint8ArrayContent = new TextEncoder().encode(header);

	const customDetectors = [unicornDetector];
	const parser = new FileTypeParser({customDetectors});

	const result = await parser.fromBuffer(uint8ArrayContent);
	t.deepEqual(result, {ext: 'unicorn', mime: 'application/unicorn'});
});

test('fileTypeFromBuffer should keep detecting default file types when no custom detector matches', async t => {
	const file = path.join(__dirname, 'fixture', 'fixture.png');
	const uint8ArrayContent = fs.readFileSync(file);

	const customDetectors = [unicornDetector];
	const parser = new FileTypeParser({customDetectors});

	const result = await parser.fromBuffer(uint8ArrayContent);
	t.deepEqual(result, {ext: 'png', mime: 'image/png'});
});

test('fileTypeFromBuffer should allow overriding default file type detectors', async t => {
	const file = path.join(__dirname, 'fixture', 'fixture.png');
	const uint8ArrayContent = fs.readFileSync(file);

	const customDetectors = [mockPngDetector];
	const parser = new FileTypeParser({customDetectors});

	const result = await parser.fromBuffer(uint8ArrayContent);
	t.deepEqual(result, {ext: 'mockPng', mime: 'image/mockPng'});
});

test('fileTypeFromBuffer keeps detecting MP3 from a sampled prefix with ID3 data', async t => {
	const file = path.join(__dirname, 'fixture', 'fixture.mp3');
	const prefix = fs.readFileSync(file).subarray(0, 32);

	const result = await fileTypeFromBuffer(prefix);
	t.deepEqual(result, {ext: 'mp3', mime: 'audio/mpeg'});
});

test('fileTypeFromBuffer keeps detecting PNG from a short valid prefix', async t => {
	const file = path.join(__dirname, 'fixture', 'fixture.png');
	const prefix = fs.readFileSync(file).subarray(0, 16);

	const result = await fileTypeFromBuffer(prefix);
	t.deepEqual(result, {ext: 'png', mime: 'image/png'});
});

test('fileTypeFromBuffer falls back to generic ASF for a short valid prefix', async t => {
	const file = path.join(__dirname, 'fixture', 'fixture.asf');
	const prefix = fs.readFileSync(file).subarray(0, 64);

	const result = await fileTypeFromBuffer(prefix);
	t.deepEqual(result, {ext: 'asf', mime: 'application/vnd.ms-asf'});
});

function createCustomReadableStream() {
	return new ReadableStream({
		start(controller) {
			controller.enqueue(new TextEncoder().encode('UNICORN'));
			controller.close();
		},
	});
}

test('fileTypeFromStream should detect custom file type "unicorn" using custom detectors', async t => {
	const readableStream = createCustomReadableStream();

	const customDetectors = [unicornDetector];
	const parser = new FileTypeParser({customDetectors});

	const result = await parser.fromStream(readableStream);
	t.deepEqual(result, {ext: 'unicorn', mime: 'application/unicorn'});
});

test('fileTypeFromStream should keep detecting default file types when no custom detector matches', async t => {
	const file = path.join(__dirname, 'fixture', 'fixture.png');
	const readableStream = new Blob([fs.readFileSync(file)]).stream();

	const customDetectors = [unicornDetector];
	const parser = new FileTypeParser({customDetectors});

	const result = await parser.fromStream(readableStream);
	t.deepEqual(result, {ext: 'png', mime: 'image/png'});
});

test('fileTypeFromStream should allow overriding default file type detectors', async t => {
	const file = path.join(__dirname, 'fixture', 'fixture.png');
	const readableStream = new Blob([fs.readFileSync(file)]).stream();

	const customDetectors = [mockPngDetector];
	const parser = new FileTypeParser({customDetectors});

	const result = await parser.fromStream(readableStream);
	t.deepEqual(result, {ext: 'mockPng', mime: 'image/mockPng'});
});

test('fileTypeFromStream should return undefined on malformed object-mode stream input', async t => {
	// This payload deterministically triggered `RangeError: offset is out of bounds` before hardening.
	const malformedChunk = Buffer.from('969c0e7833211bc4d4db0530eab780406fe889490c1e212bb1e4948f39bc4b4b8d', 'hex');
	const readableStream = new ReadableStream({
		start(controller) {
			controller.enqueue(malformedChunk.subarray(0, 16));
			controller.enqueue(malformedChunk.subarray(16));
			controller.close();
		},
	});

	const result = await fileTypeFromStream(readableStream);
	t.is(result, undefined);
});

test('fileTypeFromFile should detect custom file type "unicorn" using custom detectors', async t => {
	const file = path.join(__dirname, 'fixture', 'fixture.unicorn');

	const customDetectors = [unicornDetector];

	const result = await fileTypeFromFile(file, {customDetectors});
	t.deepEqual(result, {ext: 'unicorn', mime: 'application/unicorn'});
});

test('fileTypeFromFile should keep detecting default file types when no custom detector matches', async t => {
	const file = path.join(__dirname, 'fixture', 'fixture.png');

	const customDetectors = [unicornDetector];

	const result = await fileTypeFromFile(file, {customDetectors});
	t.deepEqual(result, {ext: 'png', mime: 'image/png'});
});

test('fileTypeFromFile should allow overriding default file type detectors', async t => {
	const file = path.join(__dirname, 'fixture', 'fixture.png');

	const customDetectors = [mockPngDetector];

	const result = await fileTypeFromFile(file, {customDetectors});
	t.deepEqual(result, {ext: 'mockPng', mime: 'image/mockPng'});
});

test('fileTypeFromTokenizer should return undefined when a custom detector changes the tokenizer position and does not return a file type', async t => {
	const header = 'UNICORN FILE\n';
	const uint8ArrayContent = new TextEncoder().encode(header);

	// Include the unicornDetector here to verify it's not used after the tokenizer.position changed
	const customDetectors = [tokenizerPositionChanger, unicornDetector];
	const parser = new FileTypeParser({customDetectors});

	const result = await parser.fromTokenizer(strtok3.fromBuffer(uint8ArrayContent));
	t.is(result, undefined);
});

test('fileTypeFromTokenizer should close the tokenizer it consumes', async t => {
	const tokenizer = await fromFile(path.join(__dirname, 'fixture', 'fixture.jpg'));

	const result = await fileTypeFromTokenizer(tokenizer);

	t.deepEqual(result, {
		ext: 'jpg',
		mime: 'image/jpeg',
	});
	t.is(tokenizer.fileHandle.fd, -1);
});

test('FileTypeParser.fromTokenizer should close the tokenizer it consumes', async t => {
	const tokenizer = await fromFile(path.join(__dirname, 'fixture', 'fixture.jpg'));

	const result = await new FileTypeParser().fromTokenizer(tokenizer);

	t.deepEqual(result, {
		ext: 'jpg',
		mime: 'image/jpeg',
	});
	t.is(tokenizer.fileHandle.fd, -1);
});

test('should detect MPEG frame which is out of sync with the mpegOffsetTolerance option', async t => {
	const badOffset1Path = path.join(__dirname, 'fixture', 'fixture-bad-offset.mp3');
	const badOffset10Path = path.join(__dirname, 'fixture', 'fixture-bad-offset-10.mp3');

	let result = await fileTypeFromFile(badOffset1Path);
	t.is(result, undefined, 'does not detect an MP3 which 1 byte out-sync, with default value mpegOffsetTolerance=0');

	result = await fileTypeFromFile(badOffset1Path, {mpegOffsetTolerance: 1});
	t.deepEqual(result, {ext: 'mp3', mime: 'audio/mpeg'}, 'detect an MP3 which 1 byte out of sync');

	result = await fileTypeFromFile(badOffset10Path);
	t.is(result, undefined, 'does not detect an MP3 which 10 bytes out of sync, with default value mpegOffsetTolerance=0');

	result = await fileTypeFromFile(badOffset10Path, {mpegOffsetTolerance: 10});
	t.deepEqual(result, {ext: 'mp3', mime: 'audio/mpeg'}, 'detect an MP3 which 1 byte out of sync');
});

test('FileTypeParser clamps mpegOffsetTolerance to a safe value', t => {
	const parser = new FileTypeParser({mpegOffsetTolerance: Number.MAX_SAFE_INTEGER});
	t.is(parser.options.mpegOffsetTolerance, 4098);
});

function loopEncoding(t, stringValue, encoding) {
	t.deepEqual(new TextDecoder(encoding).decode(new Uint8Array(stringToBytes(stringValue, encoding))), stringValue, `Ensure consistency with TextDecoder with encoding ${encoding}`);
}

test('stringToBytes encodes correctly for selected characters and encodings', t => {
	// Default encoding: basic ASCII
	t.deepEqual(
		stringToBytes('ABC'),
		[65, 66, 67],
		'should encode ASCII correctly using default encoding',
	);

	// UTF-16LE with character above 0xFF
	t.deepEqual(
		stringToBytes('ꟻ', 'utf-16le'),
		[0xFB, 0xA7],
		'should encode U+A7FB correctly in utf-16le',
	);

	// UTF-16BE with character above 0xFF
	t.deepEqual(
		stringToBytes('ꟻ', 'utf-16be'),
		[0xA7, 0xFB],
		'should encode U+A7FB correctly in utf-16be',
	);

	// UTF-16LE with surrogate pair (🦄)
	t.deepEqual(
		stringToBytes('🦄', 'utf-16le'),
		[0x3E, 0xD8, 0x84, 0xDD],
		'should encode 🦄 (U+1F984) correctly in utf-16le',
	);

	// UTF-16BE with surrogate pair (🦄)
	t.deepEqual(
		stringToBytes('🦄', 'utf-16be'),
		[0xD8, 0x3E, 0xDD, 0x84],
		'should encode 🦄 (U+1F984) correctly in utf-16be',
	);

	loopEncoding(t, '🦄', 'utf-16le');
	loopEncoding(t, '🦄', 'utf-16be');

	t.is(new TextDecoder('utf-16be').decode(new Uint8Array(stringToBytes('🦄', 'utf-16be'))), '🦄', 'Decoded value should match original value');
});

test('Does not hang on crafted ASF file with zero-size sub-header', async t => {
	const buffer = Buffer.from('3026b2758e66cf11a6d9000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', 'hex');
	await assertUndefinedTypeFromBuffer(t, buffer);
});

test('Does not throw on malformed ASF stream with zero-size sub-header', async t => {
	const buffer = Buffer.from('3026b2758e66cf11a6d9000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', 'hex');
	await assertUndefinedTypeFromChunkedStream(t, buffer);
});

test('Does not throw on malformed ASF stream with oversized sub-header', async t => {
	const buffer = Buffer.alloc(80);
	buffer.set([0x30, 0x26, 0xB2, 0x75, 0x8E, 0x66, 0xCF, 0x11, 0xA6, 0xD9]);
	buffer.fill(0xFF, 46, 54);
	await assertUndefinedTypeFromChunkedStream(t, buffer);
});

test('Does not classify malformed ASF streams with non-zero oversized sub-header objects', async t => {
	const buffer = Buffer.alloc(80);
	buffer.set([0x30, 0x26, 0xB2, 0x75, 0x8E, 0x66, 0xCF, 0x11, 0xA6, 0xD9]);
	buffer.set([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10], 30);
	buffer.fill(0xFF, 46, 54);
	await assertUndefinedTypeFromChunkedStream(t, buffer);
});

test('Does not classify malformed PNG streams with invalid IHDR before an oversized ancillary chunk', async t => {
	const buffer = Buffer.concat([
		Buffer.from([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]),
		Buffer.from(createPngChunk('IHDR')),
		Buffer.from(createPngChunk('tEXt', new Uint8Array(maximumStreamPayloadProbeSizeInBytes + 1))),
	]);
	await assertUndefinedTypeFromChunkedStream(t, buffer);
});

test('Malformed hardening corpus stays stable under hostile stream chunking', async t => {
	const malformedAsfZeroSize = Buffer.from('3026b2758e66cf11a6d9000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', 'hex');
	const malformedAsfOversized = Buffer.alloc(80);
	malformedAsfOversized.set([0x30, 0x26, 0xB2, 0x75, 0x8E, 0x66, 0xCF, 0x11, 0xA6, 0xD9]);
	malformedAsfOversized.fill(0xFF, 46, 54);
	const malformedAsfNonZeroOversized = Buffer.alloc(80);
	malformedAsfNonZeroOversized.set([0x30, 0x26, 0xB2, 0x75, 0x8E, 0x66, 0xCF, 0x11, 0xA6, 0xD9]);
	malformedAsfNonZeroOversized.set([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10], 30);
	malformedAsfNonZeroOversized.fill(0xFF, 46, 54);
	const malformedId3 = Uint8Array.from([0x49, 0x44, 0x33, 0x04, 0x00, 0x00, 0x7F, 0x7F, 0x7F, 0x7F]);
	const malformedPng = Uint8Array.from([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A, 0x7F, 0xFF, 0xFF, 0xFF, 0x7A, 0x7A, 0x7A, 0x7A]);
	const malformedPngInvalidIhdr = Buffer.concat([
		Buffer.from([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]),
		Buffer.from(createPngChunk('IHDR')),
		Buffer.from(createPngChunk('tEXt', new Uint8Array(maximumStreamPayloadProbeSizeInBytes + 1))),
	]);
	const malformedTiff = Uint8Array.from([0x49, 0x49, 0x2A, 0x00, 0xFF, 0xFF, 0xFF, 0xFF]);
	const malformedEbml = Uint8Array.from([0x1A, 0x45, 0xDF, 0xA3, 0x8A, 0x42, 0x83, 0x01, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]);

	await assertUndefinedTypeFromHostileStreams(t, malformedAsfZeroSize, 'malformed ASF zero-size sub-header');
	await assertUndefinedTypeFromHostileStreams(t, malformedAsfOversized, 'malformed ASF oversized sub-header');
	await assertUndefinedTypeFromHostileStreams(t, malformedAsfNonZeroOversized, 'malformed ASF non-zero oversized sub-header');
	await assertUndefinedTypeFromHostileStreams(t, malformedId3, 'malformed ID3 oversized header');
	await assertUndefinedTypeFromHostileStreams(t, malformedPng, 'malformed PNG oversized chunk');
	await assertUndefinedTypeFromHostileStreams(t, malformedPngInvalidIhdr, 'malformed PNG invalid IHDR before oversized chunk');
	await assertUndefinedTypeFromHostileStreams(t, malformedEbml, 'malformed EBML oversized child');

	for (const chunkPattern of hostileChunkPatterns) {
		const type = await fileTypeFromStream(createPatternWebStream(malformedTiff, chunkPattern).stream);
		t.deepEqual(type, {
			ext: 'tif',
			mime: 'image/tiff',
		}, `malformed TIFF oversized offset with chunk pattern ${chunkPattern.join(',')}`);
	}
});

test('Keeps UTF-8 BOM re-entry bounded', async t => {
	const maximumDetectionReentryCount = 256;
	const bom = Buffer.from([0xEF, 0xBB, 0xBF]);
	const xml = Buffer.from('<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg"></svg>');
	const supportedPayload = Buffer.concat([
		...Array.from({length: maximumDetectionReentryCount}, () => bom),
		xml,
	]);
	const excessivePayload = Buffer.concat([
		...Array.from({length: maximumDetectionReentryCount + 1}, () => bom),
		xml,
	]);

	t.deepEqual(await fileTypeFromBuffer(supportedPayload), {
		ext: 'xml',
		mime: 'application/xml',
	});
	t.is(await fileTypeFromBuffer(excessivePayload), undefined);
});

test('Keeps zero-length ID3 re-entry bounded', async t => {
	const maximumDetectionReentryCount = 256;
	const zeroLengthId3Header = Buffer.from([0x49, 0x44, 0x33, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]);
	const mpegFrame = Buffer.from([0xFF, 0xFB, 0x90, 0x64, 0x00, 0x00, 0x00, 0x00]);
	const supportedPayload = Buffer.concat([
		...Array.from({length: maximumDetectionReentryCount}, () => zeroLengthId3Header),
		mpegFrame,
	]);
	const excessivePayload = Buffer.concat([
		...Array.from({length: maximumDetectionReentryCount + 1}, () => zeroLengthId3Header),
		mpegFrame,
	]);

	t.deepEqual(await fileTypeFromBuffer(supportedPayload), {
		ext: 'mp3',
		mime: 'audio/mpeg',
	});
	t.is(await fileTypeFromBuffer(excessivePayload), undefined);
});

test('Keeps UTF-8 BOM stream re-entry bounded', async t => {
	const maximumDetectionReentryCount = 256;
	const bom = Buffer.from([0xEF, 0xBB, 0xBF]);
	const xml = Buffer.from('<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg"></svg>');
	const excessivePayload = Buffer.concat([
		...Array.from({length: maximumDetectionReentryCount + 1}, () => bom),
		xml,
	]);
	const {state, stream} = createPatternWebStream(excessivePayload, [1]);

	const type = await new FileTypeParser().fromStream(stream);
	t.is(type, undefined);
	t.true(state.emittedBytes <= ((maximumDetectionReentryCount + 1) * bom.length) + 32);
});

test('Keeps zero-length ID3 stream re-entry bounded', async t => {
	const maximumDetectionReentryCount = 256;
	const zeroLengthId3Header = Buffer.from([0x49, 0x44, 0x33, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]);
	const mpegFrame = Buffer.from([0xFF, 0xFB, 0x90, 0x64, 0x00, 0x00, 0x00, 0x00]);
	const excessivePayload = Buffer.concat([
		...Array.from({length: maximumDetectionReentryCount + 1}, () => zeroLengthId3Header),
		mpegFrame,
	]);
	const {state, stream} = createPatternWebStream(excessivePayload, [1]);

	const type = await new FileTypeParser().fromStream(stream);
	t.is(type, undefined);
	t.true(state.emittedBytes <= ((maximumDetectionReentryCount + 1) * zeroLengthId3Header.length) + 32);
});

test('FileTypeParser resets re-entry count between calls', async t => {
	const maximumDetectionReentryCount = 256;
	const parser = new FileTypeParser();
	const bom = Buffer.from([0xEF, 0xBB, 0xBF]);
	const xml = Buffer.from('<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg"></svg>');
	const excessiveBomPayload = Buffer.concat([
		...Array.from({length: maximumDetectionReentryCount + 1}, () => bom),
		xml,
	]);
	const zeroLengthId3Header = Buffer.from([0x49, 0x44, 0x33, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]);
	const mpegFrame = Buffer.from([0xFF, 0xFB, 0x90, 0x64, 0x00, 0x00, 0x00, 0x00]);
	const excessiveId3Payload = Buffer.concat([
		...Array.from({length: maximumDetectionReentryCount + 1}, () => zeroLengthId3Header),
		mpegFrame,
	]);

	t.is(await parser.fromBuffer(excessiveBomPayload), undefined);
	t.deepEqual(await parser.fromBuffer(xml), {
		ext: 'xml',
		mime: 'application/xml',
	});
	t.is(await parser.fromBuffer(excessiveId3Payload), undefined);
	t.deepEqual(await parser.fromBuffer(mpegFrame), {
		ext: 'mp3',
		mime: 'audio/mpeg',
	});
});

test('Scans known-size ASF buffers beyond the stream safety window', async t => {
	const metadataObject = createAsfObject(
		Uint8Array.from([0xA1, 0xDC, 0xAB, 0x8C, 0x47, 0xA9, 0xCF, 0x11, 0x8E, 0xE4, 0x00, 0xC0, 0x0C, 0x20, 0x53, 0x65]),
		new Uint8Array(1400),
	);
	const streamPropertiesObject = createAsfObject(
		Uint8Array.from([0x91, 0x07, 0xDC, 0xB7, 0xB7, 0xA9, 0xCF, 0x11, 0x8E, 0xE6, 0x00, 0xC0, 0x0C, 0x20, 0x53, 0x65]),
		Uint8Array.from([0x40, 0x9E, 0x69, 0xF8, 0x4D, 0x5B, 0xCF, 0x11, 0xA8, 0xFD, 0x00, 0x80, 0x5F, 0x5C, 0x44, 0x2B]),
	);
	const buffer = createAsfHeader([metadataObject, streamPropertiesObject]);

	const type = await fileTypeFromBuffer(buffer);
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'audio/x-ms-asf',
	});

	const streamType = await fileTypeFromStream(createBufferedWebStream(buffer, 32));
	t.deepEqual(streamType, {
		ext: 'asf',
		mime: 'audio/x-ms-asf',
	});
});

test('Scans many ASF header objects for known-size buffers', async t => {
	const metadataObjectId = Uint8Array.from([0xA1, 0xDC, 0xAB, 0x8C, 0x47, 0xA9, 0xCF, 0x11, 0x8E, 0xE4, 0x00, 0xC0, 0x0C, 0x20, 0x53, 0x65]);
	const fillerObjects = [];

	for (let index = 0; index < 257; index++) {
		fillerObjects.push(createAsfObject(metadataObjectId));
	}

	const streamPropertiesObject = createAsfObject(
		Uint8Array.from([0x91, 0x07, 0xDC, 0xB7, 0xB7, 0xA9, 0xCF, 0x11, 0x8E, 0xE6, 0x00, 0xC0, 0x0C, 0x20, 0x53, 0x65]),
		Uint8Array.from([0x40, 0x9E, 0x69, 0xF8, 0x4D, 0x5B, 0xCF, 0x11, 0xA8, 0xFD, 0x00, 0x80, 0x5F, 0x5C, 0x44, 0x2B]),
	);
	const buffer = createAsfHeader([...fillerObjects, streamPropertiesObject]);

	const type = await fileTypeFromBuffer(buffer);
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'audio/x-ms-asf',
	});
});

test('Scans ASF stream properties at the header object limit', async t => {
	const type = await fileTypeFromBuffer(createAsfAudioHeaderWithMetadataObjects(511));
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'audio/x-ms-asf',
	});
});

test('fileTypeFromFile scans ASF stream properties at the header object limit', async t => {
	const filePath = await createTemporaryTestFile(t, createAsfAudioHeaderWithMetadataObjects(511), 'asf');

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'asf',
		mime: 'audio/x-ms-asf',
	});
});

test('fileTypeFromBlob scans ASF stream properties at the header object limit', async t => {
	const type = await fileTypeFromBlob(new Blob([createAsfAudioHeaderWithMetadataObjects(511)]));
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'audio/x-ms-asf',
	});
});

test('Detects ASF video when stream properties appear at the header object limit', async t => {
	const type = await fileTypeFromBuffer(createAsfVideoHeaderWithMetadataObjects(511));
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'video/x-ms-asf',
	});
});

test('fileTypeFromFile detects ASF video when stream properties appear at the header object limit', async t => {
	const filePath = await createTemporaryTestFile(t, createAsfVideoHeaderWithMetadataObjects(511), 'asf');

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'asf',
		mime: 'video/x-ms-asf',
	});
});

test('fileTypeFromBlob detects ASF video when stream properties appear at the header object limit', async t => {
	const type = await fileTypeFromBlob(new Blob([createAsfVideoHeaderWithMetadataObjects(511)]));
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'video/x-ms-asf',
	});
});

test('Falls back to generic ASF when an unknown stream type appears at the header object limit', async t => {
	const type = await fileTypeFromBuffer(createAsfUnknownStreamHeaderWithMetadataObjects(511));
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'application/vnd.ms-asf',
	});
});

test('fileTypeFromFile falls back to generic ASF when an unknown stream type appears at the header object limit', async t => {
	const filePath = await createTemporaryTestFile(t, createAsfUnknownStreamHeaderWithMetadataObjects(511), 'asf');

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'asf',
		mime: 'application/vnd.ms-asf',
	});
});

test('fileTypeFromBlob falls back to generic ASF when an unknown stream type appears at the header object limit', async t => {
	const type = await fileTypeFromBlob(new Blob([createAsfUnknownStreamHeaderWithMetadataObjects(511)]));
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'application/vnd.ms-asf',
	});
});

test('Falls back to generic ASF when stream properties appear after the header object limit', async t => {
	const type = await fileTypeFromBuffer(createAsfAudioHeaderWithMetadataObjects(512));
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'application/vnd.ms-asf',
	});
});

test('fileTypeFromFile falls back to generic ASF when stream properties appear after the header object limit', async t => {
	const filePath = await createTemporaryTestFile(t, createAsfAudioHeaderWithMetadataObjects(512), 'asf');

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'asf',
		mime: 'application/vnd.ms-asf',
	});
});

test('fileTypeFromBlob falls back to generic ASF when stream properties appear after the header object limit', async t => {
	const type = await fileTypeFromBlob(new Blob([createAsfAudioHeaderWithMetadataObjects(512)]));
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'application/vnd.ms-asf',
	});
});

test('Streamed ASF detection keeps scanning at the header object limit', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createAsfAudioHeaderWithMetadataObjects(511), 17));
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'audio/x-ms-asf',
	});
});

test('Streamed ASF detection keeps scanning at the header object limit with small chunks', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createAsfAudioHeaderWithMetadataObjects(511), 1));
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'audio/x-ms-asf',
	});
});

test('Web Stream ASF detection keeps scanning at the header object limit', async t => {
	const {stream} = createPatternWebStream(createAsfAudioHeaderWithMetadataObjects(511), [3, 5, 2, 7]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'audio/x-ms-asf',
	});
});

test('Web Stream ASF detection keeps scanning at the header object limit with small chunks', async t => {
	const {stream} = createPatternWebStream(createAsfAudioHeaderWithMetadataObjects(511), [1]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'audio/x-ms-asf',
	});
});

test('Streamed ASF video detection keeps scanning at the header object limit', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createAsfVideoHeaderWithMetadataObjects(511), 17));
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'video/x-ms-asf',
	});
});

test('Streamed ASF video detection keeps scanning at the header object limit with small chunks', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createAsfVideoHeaderWithMetadataObjects(511), 1));
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'video/x-ms-asf',
	});
});

test('Web Stream ASF video detection keeps scanning at the header object limit', async t => {
	const {stream} = createPatternWebStream(createAsfVideoHeaderWithMetadataObjects(511), [3, 5, 2, 7]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'video/x-ms-asf',
	});
});

test('Web Stream ASF video detection keeps scanning at the header object limit with small chunks', async t => {
	const {stream} = createPatternWebStream(createAsfVideoHeaderWithMetadataObjects(511), [1]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'video/x-ms-asf',
	});
});

test('Streamed ASF detection falls back to generic ASF for an unknown stream type at the header object limit', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createAsfUnknownStreamHeaderWithMetadataObjects(511), 17));
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'application/vnd.ms-asf',
	});
});

test('Streamed ASF detection falls back to generic ASF for an unknown stream type at the header object limit with small chunks', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createAsfUnknownStreamHeaderWithMetadataObjects(511), 1));
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'application/vnd.ms-asf',
	});
});

test('Web Stream ASF detection falls back to generic ASF for an unknown stream type at the header object limit', async t => {
	const {stream} = createPatternWebStream(createAsfUnknownStreamHeaderWithMetadataObjects(511), [3, 5, 2, 7]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'application/vnd.ms-asf',
	});
});

test('Web Stream ASF detection falls back to generic ASF for an unknown stream type at the header object limit with small chunks', async t => {
	const {stream} = createPatternWebStream(createAsfUnknownStreamHeaderWithMetadataObjects(511), [1]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'application/vnd.ms-asf',
	});
});

test('Streamed ASF detection falls back after the header object limit', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createAsfAudioHeaderWithMetadataObjects(512), 17));
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'application/vnd.ms-asf',
	});
});

test('Streamed ASF detection falls back after the header object limit with small chunks', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createAsfAudioHeaderWithMetadataObjects(512), 1));
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'application/vnd.ms-asf',
	});
});

test('Web Stream ASF detection falls back after the header object limit', async t => {
	const {stream} = createPatternWebStream(createAsfAudioHeaderWithMetadataObjects(512), [3, 5, 2, 7]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'application/vnd.ms-asf',
	});
});

test('Web Stream ASF detection falls back after the header object limit with small chunks', async t => {
	const {stream} = createPatternWebStream(createAsfAudioHeaderWithMetadataObjects(512), [1]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'application/vnd.ms-asf',
	});
});

test('Scans many ASF header objects for streamed inputs', async t => {
	const metadataObjectId = Uint8Array.from([0xA1, 0xDC, 0xAB, 0x8C, 0x47, 0xA9, 0xCF, 0x11, 0x8E, 0xE4, 0x00, 0xC0, 0x0C, 0x20, 0x53, 0x65]);
	const fillerObjects = [];

	for (let index = 0; index < 257; index++) {
		fillerObjects.push(createAsfObject(metadataObjectId));
	}

	const streamPropertiesObject = createAsfObject(
		Uint8Array.from([0x91, 0x07, 0xDC, 0xB7, 0xB7, 0xA9, 0xCF, 0x11, 0x8E, 0xE6, 0x00, 0xC0, 0x0C, 0x20, 0x53, 0x65]),
		Uint8Array.from([0x40, 0x9E, 0x69, 0xF8, 0x4D, 0x5B, 0xCF, 0x11, 0xA8, 0xFD, 0x00, 0x80, 0x5F, 0x5C, 0x44, 0x2B]),
	);
	const buffer = createAsfHeader([...fillerObjects, streamPropertiesObject]);

	const type = await fileTypeFromStream(createBufferedWebStream(buffer, 32));
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'audio/x-ms-asf',
	});
});

test('fileTypeFromBuffer still detects ASF when header payload exceeds the stream payload probe limit', async t => {
	const type = await fileTypeFromBuffer(createAsfAudioHeaderWithUnknownPayload(maximumStreamPayloadProbeSizeInBytes + 1));
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'audio/x-ms-asf',
	});
});

test('Streamed ASF detection keeps scanning when header payload is exactly at the stream payload probe limit', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createAsfAudioHeaderWithUnknownPayload(maximumStreamPayloadProbeSizeInBytes), 1024));
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'audio/x-ms-asf',
	});
});

test('Web Stream ASF detection keeps scanning when header payload is exactly at the stream payload probe limit', async t => {
	const {stream} = createPatternWebStream(createAsfAudioHeaderWithUnknownPayload(maximumStreamPayloadProbeSizeInBytes), [1024]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'asf',
		mime: 'audio/x-ms-asf',
	});
});

test('Streamed ASF detection stays undefined when header payload exceeds the stream payload probe limit', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createAsfAudioHeaderWithUnknownPayload(maximumStreamPayloadProbeSizeInBytes + 1), 1024));
	t.is(type, undefined);
});

test('Web Stream ASF detection stays undefined when header payload exceeds the stream payload probe limit', async t => {
	const {stream} = createPatternWebStream(createAsfAudioHeaderWithUnknownPayload(maximumStreamPayloadProbeSizeInBytes + 1), [1024]);
	const type = await new FileTypeParser().fromStream(stream);
	t.is(type, undefined);
});

test('Streamed ASF detection stays undefined when a header extension payload exceeds the stream payload probe limit', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createAsfAudioHeaderWithHeaderExtensionPayload(maximumStreamPayloadProbeSizeInBytes + 1), 1024));
	t.is(type, undefined);
});

test('Web Stream ASF detection stays undefined when a header extension payload exceeds the stream payload probe limit', async t => {
	const {stream} = createPatternWebStream(createAsfAudioHeaderWithHeaderExtensionPayload(maximumStreamPayloadProbeSizeInBytes + 1), [1024]);
	const type = await new FileTypeParser().fromStream(stream);
	t.is(type, undefined);
});

test('Does not throw on malformed ID3 stream with oversized header length', async t => {
	const buffer = Uint8Array.from([0x49, 0x44, 0x33, 0x04, 0x00, 0x00, 0x7F, 0x7F, 0x7F, 0x7F]);
	await assertUndefinedTypeFromChunkedStream(t, buffer);
});

test('Allows large ID3 headers for known-size buffers but keeps stream probing bounded', async t => {
	const id3HeaderLength = (16 * 1024 * 1024) + 1;
	const id3Header = Uint8Array.from([
		0x49,
		0x44,
		0x33,
		0x04,
		0x00,
		0x00,
		...toSyncSafeInteger(id3HeaderLength),
	]);
	const mpegFrame = Uint8Array.from([0xFF, 0xFB, 0x90, 0x64, 0x00, 0x00, 0x00, 0x00]);
	const payload = Buffer.concat([Buffer.from(id3Header), Buffer.alloc(id3HeaderLength), Buffer.from(mpegFrame)]);

	const bufferType = await fileTypeFromBuffer(payload);
	t.deepEqual(bufferType, {
		ext: 'mp3',
		mime: 'audio/mpeg',
	});

	await assertUndefinedTypeFromChunkedStream(t, payload);
});

test('Oversized ID3 web stream keeps hostile reads bounded', async t => {
	const id3HeaderLength = (16 * 1024 * 1024) + 1;
	const id3Header = Uint8Array.from([
		0x49,
		0x44,
		0x33,
		0x04,
		0x00,
		0x00,
		...toSyncSafeInteger(id3HeaderLength),
	]);
	const payload = Buffer.concat([Buffer.from(id3Header), Buffer.alloc(1024)]);
	const {state, stream} = createPatternWebStream(payload, [1, 2, 1, 3]);

	const type = await new FileTypeParser().fromStream(stream);
	t.is(type, undefined);
	t.true(state.emittedBytes <= 40);
});

test('Repeated non-zero ID3 chunked stream probing stays cumulatively bounded', async t => {
	const maximumId3HeaderSizeInBytes = 16 * 1024 * 1024;
	const chunkSize = 64 * 1024;
	const payload = createRepeatedId3Payload(80, 256 * 1024);
	const {state, stream} = createPatternWebStream(payload, [chunkSize]);

	const type = await fileTypeFromStream(stream);
	t.is(type, undefined);
	t.true(state.emittedBytes <= maximumId3HeaderSizeInBytes + chunkSize);
});

test('Repeated non-zero ID3 Web stream probing stays cumulatively bounded', async t => {
	const maximumId3HeaderSizeInBytes = 16 * 1024 * 1024;
	const chunkSize = 64 * 1024;
	const payload = createRepeatedId3Payload(80, 256 * 1024);
	const {state, stream} = createPatternWebStream(payload, [chunkSize]);

	const type = await new FileTypeParser().fromStream(stream);
	t.is(type, undefined);
	t.true(state.emittedBytes <= maximumId3HeaderSizeInBytes + chunkSize);
});

test('Repeated non-zero ID3 chunked streams still detect MP3 below the cumulative limit', async t => {
	const payload = Buffer.concat([
		Buffer.from(createRepeatedId3Payload(8, 64 * 1024)),
		Buffer.from([0xFF, 0xFB, 0x90, 0x64, 0x00, 0x00, 0x00, 0x00]),
	]);
	const type = await fileTypeFromStream(createBufferedWebStream(payload, 1024));

	t.deepEqual(type, {
		ext: 'mp3',
		mime: 'audio/mpeg',
	});
});

test('Repeated non-zero ID3 Web streams still detect MP3 below the cumulative limit', async t => {
	const payload = Buffer.concat([
		Buffer.from(createRepeatedId3Payload(8, 64 * 1024)),
		Buffer.from([0xFF, 0xFB, 0x90, 0x64, 0x00, 0x00, 0x00, 0x00]),
	]);
	const {stream} = createPatternWebStream(payload, [1024]);
	const type = await new FileTypeParser().fromStream(stream);

	t.deepEqual(type, {
		ext: 'mp3',
		mime: 'audio/mpeg',
	});
});

test('Repeated unknown EBML chunked stream probing stays cumulatively bounded', async t => {
	const maximumEbmlScanBudgetInBytes = 16 * 1024 * 1024;
	const chunkSize = 64 * 1024;
	const payload = createEbmlWithRepeatedUnknownChildren(17, 1024 * 1024);
	const {state, stream} = createPatternWebStream(payload, [chunkSize]);

	const type = await fileTypeFromStream(stream);
	t.is(type, undefined);
	t.true(state.emittedBytes <= maximumEbmlScanBudgetInBytes + (5 * chunkSize));
});

test('Repeated unknown EBML Web stream probing stays cumulatively bounded', async t => {
	const maximumEbmlScanBudgetInBytes = 16 * 1024 * 1024;
	const chunkSize = 64 * 1024;
	const payload = createEbmlWithRepeatedUnknownChildren(17, 1024 * 1024);
	const {state, stream} = createPatternWebStream(payload, [chunkSize]);

	const type = await new FileTypeParser().fromStream(stream);
	t.is(type, undefined);
	t.true(state.emittedBytes <= maximumEbmlScanBudgetInBytes + (5 * chunkSize));
});

test('Repeated unknown EBML chunked streams still detect WebM below the cumulative limit', async t => {
	const payload = createEbmlWithRepeatedUnknownChildren(8, 64 * 1024, 'webm');
	const type = await fileTypeFromStream(createBufferedWebStream(payload, 1024));

	t.deepEqual(type, {
		ext: 'webm',
		mime: 'video/webm',
	});
});

test('Repeated unknown EBML Web streams still detect WebM below the cumulative limit', async t => {
	const payload = createEbmlWithRepeatedUnknownChildren(8, 64 * 1024, 'webm');
	const {stream} = createPatternWebStream(payload, [1024]);
	const type = await new FileTypeParser().fromStream(stream);

	t.deepEqual(type, {
		ext: 'webm',
		mime: 'video/webm',
	});
});

test('EBML chunked streams still detect WebM when document type is exactly at the stream payload probe limit', async t => {
	const payload = createEbmlWithUnknownPayloadBeforeDocumentType(maximumStreamPayloadProbeSizeInBytes, 'webm');
	const type = await fileTypeFromStream(createBufferedWebStream(payload, 1024));

	t.deepEqual(type, {
		ext: 'webm',
		mime: 'video/webm',
	});
});

test('EBML Web streams still detect WebM when document type is exactly at the stream payload probe limit', async t => {
	const payload = createEbmlWithUnknownPayloadBeforeDocumentType(maximumStreamPayloadProbeSizeInBytes, 'webm');
	const {stream} = createPatternWebStream(payload, [1024]);
	const type = await new FileTypeParser().fromStream(stream);

	t.deepEqual(type, {
		ext: 'webm',
		mime: 'video/webm',
	});
});

test('EBML chunked streams stop before document type when it first appears after the stream payload probe limit', async t => {
	const payload = createEbmlWithUnknownPayloadBeforeDocumentType(maximumStreamPayloadProbeSizeInBytes + 1, 'webm');
	const type = await fileTypeFromStream(createBufferedWebStream(payload, 1024));

	t.is(type, undefined);
});

test('EBML Web streams stop before document type when it first appears after the stream payload probe limit', async t => {
	const payload = createEbmlWithUnknownPayloadBeforeDocumentType(maximumStreamPayloadProbeSizeInBytes + 1, 'webm');
	const {stream} = createPatternWebStream(payload, [1024]);
	const type = await new FileTypeParser().fromStream(stream);

	t.is(type, undefined);
});

test('EBML chunked streams with small chunks still detect Matroska when document type is exactly at the stream payload probe limit', async t => {
	const payload = createEbmlWithUnknownPayloadBeforeDocumentType(maximumStreamPayloadProbeSizeInBytes, 'matroska');
	const type = await fileTypeFromStream(createBufferedWebStream(payload, 1));

	t.deepEqual(type, {
		ext: 'mkv',
		mime: 'video/matroska',
	});
});

test('EBML Web streams with small chunks still detect Matroska when document type is exactly at the stream payload probe limit', async t => {
	const payload = createEbmlWithUnknownPayloadBeforeDocumentType(maximumStreamPayloadProbeSizeInBytes, 'matroska');
	const {stream} = createPatternWebStream(payload, [1]);
	const type = await new FileTypeParser().fromStream(stream);

	t.deepEqual(type, {
		ext: 'mkv',
		mime: 'video/matroska',
	});
});

test('EBML chunked streams with small chunks stop before Matroska when document type first appears after the stream payload probe limit', async t => {
	const payload = createEbmlWithUnknownPayloadBeforeDocumentType(maximumStreamPayloadProbeSizeInBytes + 1, 'matroska');
	const type = await fileTypeFromStream(createBufferedWebStream(payload, 1));

	t.is(type, undefined);
});

test('EBML Web streams with small chunks stop before Matroska when document type first appears after the stream payload probe limit', async t => {
	const payload = createEbmlWithUnknownPayloadBeforeDocumentType(maximumStreamPayloadProbeSizeInBytes + 1, 'matroska');
	const {stream} = createPatternWebStream(payload, [1]);
	const type = await new FileTypeParser().fromStream(stream);

	t.is(type, undefined);
});

test('.fileTypeStream() detects WebM when the EBML document type is exactly at the stream payload probe limit for chunked streams with a large sampleSize', async t => {
	const payload = createEbmlWithUnknownPayloadBeforeDocumentType(maximumStreamPayloadProbeSizeInBytes, 'webm');

	await assertFileTypeStreamChunkedResult(t, payload, {
		ext: 'webm',
		mime: 'video/webm',
	}, {sampleSize: payload.length});
});

test('.fileTypeStream() detects WebM when the EBML document type is exactly at the stream payload probe limit for Web Streams with a large sampleSize', async t => {
	const payload = createEbmlWithUnknownPayloadBeforeDocumentType(maximumStreamPayloadProbeSizeInBytes, 'webm');

	await assertFileTypeStreamWebResult(t, payload, {
		ext: 'webm',
		mime: 'video/webm',
	}, {sampleSize: payload.length});
});

test('.fileTypeStream() falls back when the EBML document type appears after the default sampleSize for chunked streams', async t => {
	const payload = createEbmlWithUnknownPayloadBeforeDocumentType(maximumStreamPayloadProbeSizeInBytes + 1, 'webm');

	await assertFileTypeStreamChunkedResult(t, payload, undefined);
});

test('.fileTypeStream() falls back when the EBML document type appears after the default sampleSize for Web Streams', async t => {
	const payload = createEbmlWithUnknownPayloadBeforeDocumentType(maximumStreamPayloadProbeSizeInBytes + 1, 'webm');

	await assertFileTypeStreamWebResult(t, payload, undefined);
});

test('.fileTypeStream() detects Matroska when the EBML document type is exactly at the stream payload probe limit for chunked streams with small chunks and a large sampleSize', async t => {
	const payload = createEbmlWithUnknownPayloadBeforeDocumentType(maximumStreamPayloadProbeSizeInBytes, 'matroska');

	await assertFileTypeStreamChunkedResult(t, payload, {
		ext: 'mkv',
		mime: 'video/matroska',
	}, {
		chunkSize: 256,
		sampleSize: payload.length,
	});
});

test('.fileTypeStream() detects Matroska when the EBML document type is exactly at the stream payload probe limit for Web Streams with a large sampleSize', async t => {
	const payload = createEbmlWithUnknownPayloadBeforeDocumentType(maximumStreamPayloadProbeSizeInBytes, 'matroska');

	await assertFileTypeStreamWebResult(t, payload, {
		ext: 'mkv',
		mime: 'video/matroska',
	}, {sampleSize: payload.length});
});

test('.fileTypeStream() falls back when the Matroska document type appears after the default sampleSize for chunked streams', async t => {
	const payload = createEbmlWithUnknownPayloadBeforeDocumentType(maximumStreamPayloadProbeSizeInBytes + 1, 'matroska');

	await assertFileTypeStreamChunkedResult(t, payload, undefined);
});

test('.fileTypeStream() falls back when the Matroska document type appears after the default sampleSize for Web Streams', async t => {
	const payload = createEbmlWithUnknownPayloadBeforeDocumentType(maximumStreamPayloadProbeSizeInBytes + 1, 'matroska');

	await assertFileTypeStreamWebResult(t, payload, undefined);
});

test('fileTypeFromBuffer still detects WebM when the EBML document type appears after the stream payload probe limit', async t => {
	const payload = createEbmlWithUnknownPayloadBeforeDocumentType(maximumStreamPayloadProbeSizeInBytes + 1, 'webm');
	const type = await fileTypeFromBuffer(payload);

	t.deepEqual(type, {
		ext: 'webm',
		mime: 'video/webm',
	});
});

test('fileTypeFromBlob still detects WebM when the EBML document type appears after the stream payload probe limit', async t => {
	const payload = createEbmlWithUnknownPayloadBeforeDocumentType(maximumStreamPayloadProbeSizeInBytes + 1, 'webm');
	const type = await fileTypeFromBlob(new Blob([payload]));

	t.deepEqual(type, {
		ext: 'webm',
		mime: 'video/webm',
	});
});

test('fileTypeFromFile still detects Matroska when the EBML document type appears after the stream payload probe limit', async t => {
	const payload = createEbmlWithUnknownPayloadBeforeDocumentType(maximumStreamPayloadProbeSizeInBytes + 1, 'matroska');
	const filePath = await createTemporaryTestFile(t, payload);
	const type = await fileTypeFromFile(filePath);

	t.deepEqual(type, {
		ext: 'mkv',
		mime: 'video/matroska',
	});
});

test('fileTypeFromBuffer still detects Matroska when the EBML document type appears after the stream payload probe limit', async t => {
	const payload = createEbmlWithUnknownPayloadBeforeDocumentType(maximumStreamPayloadProbeSizeInBytes + 1, 'matroska');
	const type = await fileTypeFromBuffer(payload);

	t.deepEqual(type, {
		ext: 'mkv',
		mime: 'video/matroska',
	});
});

test('fileTypeFromFile returns undefined for FIFOs without blocking', async t => {
	if (process.platform === 'win32') {
		t.pass();
		return;
	}

	const filePath = await createTemporaryFifo(t);
	const script = `
		import {fileTypeFromFile} from ${JSON.stringify(new URL('source/index.js', import.meta.url).href)};
		const type = await fileTypeFromFile(${JSON.stringify(filePath)});
		console.log(JSON.stringify(type));
	`;
	const result = spawnSync(process.execPath, ['--input-type=module', '-e', script], {
		cwd: __dirname,
		encoding: 'utf8',
		timeout: 1500,
	});

	t.is(result.signal, null);
	t.is(result.status, 0);
	t.is(result.stdout.trim(), 'undefined');
});

test('fileTypeFromFile returns undefined when the path becomes a FIFO before open', async t => {
	if (process.platform === 'win32') {
		t.pass();
		return;
	}

	const temporaryDirectory = await createTemporaryDirectory(t);
	const regularPath = path.join(temporaryDirectory, 'regular.jpg');
	const fifoPath = path.join(temporaryDirectory, 'fifo');
	const linkPath = path.join(temporaryDirectory, 'link');
	await fs.promises.writeFile(regularPath, Buffer.from([0xFF, 0xD8, 0xFF, 0x00]));
	const mkfifoResult = spawnSync('mkfifo', [fifoPath]);
	if (mkfifoResult.status !== 0) {
		throw new Error(`mkfifo failed: ${mkfifoResult.stderr.toString()}`);
	}

	await fs.promises.symlink(regularPath, linkPath);
	const script = `
		import fs from 'node:fs/promises';
		const originalOpen = fs.open.bind(fs);
		const linkPath = ${JSON.stringify(linkPath)};
		const fifoPath = ${JSON.stringify(fifoPath)};
		fs.open = async (...arguments_) => {
			await fs.unlink(linkPath);
			await fs.symlink(fifoPath, linkPath);
			return originalOpen(...arguments_);
		};
		const {fileTypeFromFile} = await import(${JSON.stringify(new URL('source/index.js', import.meta.url).href)});
		const type = await fileTypeFromFile(linkPath);
		console.log(JSON.stringify(type));
	`;
	const result = spawnSync(process.execPath, ['--input-type=module', '-e', script], {
		cwd: __dirname,
		encoding: 'utf8',
		timeout: 1500,
	});

	t.is(result.signal, null);
	t.is(result.status, 0);
	t.is(result.stdout.trim(), 'undefined');
});

test('Does not throw on malformed PNG stream with oversized chunk length', async t => {
	const bytes = Uint8Array.from([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A, 0x7F, 0xFF, 0xFF, 0xFF, 0x7A, 0x7A, 0x7A, 0x7A]);
	await assertUndefinedTypeFromChunkedStream(t, bytes);
});

test('Does not throw on malformed TIFF with oversized IFD offset', async t => {
	const bytes = Uint8Array.from([0x49, 0x49, 0x2A, 0x00, 0xFF, 0xFF, 0xFF, 0xFF]);
	await assertUndefinedTypeFromBuffer(t, bytes);
});

test('Does not throw on malformed TIFF stream with oversized IFD offset', async t => {
	const bytes = Uint8Array.from([0x49, 0x49, 0x2A, 0x00, 0xFF, 0xFF, 0xFF, 0xFF]);
	const type = await fileTypeFromStream(createBufferedWebStream(bytes, 8));
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('Does not crash or hang if provided with a partial gunzip file', async t => {
	const buffer = Uint8Array.from([31, 139, 8, 8, 137, 83, 29, 82, 0, 11]);
	const type = await fileTypeFromBuffer(buffer);

	t.deepEqual(type, {
		ext: 'gz',
		mime: 'application/gzip',
	});
});

test('OOXML type detection is not affected by ZIP entry order', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode('<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>'),
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	const bufferType = await fileTypeFromBuffer(orderedZip);
	t.deepEqual(bufferType, {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});

	const streamType = await fileTypeFromStream(createBufferedWebStream(orderedZip, 16));
	t.deepEqual(streamType, {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('OOXML directory heuristic detects docx when [Content_Types].xml is beyond the stream sample', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new Uint8Array(reasonableDetectionSizeInBytes),
	});
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode('<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/></Types>'),
	});
	const zip = Buffer.concat([wordEntry, contentTypesEntry]);

	// Full buffer: [Content_Types].xml is reachable, gives precise type
	const bufferType = await fileTypeFromBuffer(zip);
	t.deepEqual(bufferType, {
		ext: 'docx',
		mime: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
	});

	// Truncated stream: [Content_Types].xml is beyond the sample, falls back to directory heuristic
	await assertFileTypeStreamChunkedResult(t, zip, {
		ext: 'docx',
		mime: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
	});
	await assertFileTypeStreamWebResult(t, zip, {
		ext: 'docx',
		mime: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
	});
});

test('OOXML directory heuristic detects pptx when [Content_Types].xml is beyond the stream sample', async t => {
	const pptEntry = createZipLocalFile({
		filename: 'ppt/presentation.xml',
		compressedData: new Uint8Array(reasonableDetectionSizeInBytes),
	});
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode('<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/></Types>'),
	});
	const zip = Buffer.concat([pptEntry, contentTypesEntry]);

	await assertFileTypeStreamChunkedResult(t, zip, {
		ext: 'pptx',
		mime: 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
	});
	await assertFileTypeStreamWebResult(t, zip, {
		ext: 'pptx',
		mime: 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
	});
});

test('OOXML directory heuristic detects xlsx when [Content_Types].xml is beyond the stream sample', async t => {
	const xlEntry = createZipLocalFile({
		filename: 'xl/workbook.xml',
		compressedData: new Uint8Array(reasonableDetectionSizeInBytes),
	});
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode('<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/></Types>'),
	});
	const zip = Buffer.concat([xlEntry, contentTypesEntry]);

	await assertFileTypeStreamChunkedResult(t, zip, {
		ext: 'xlsx',
		mime: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
	});
	await assertFileTypeStreamWebResult(t, zip, {
		ext: 'xlsx',
		mime: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
	});
});

test('OOXML directory heuristic detects 3mf when [Content_Types].xml is beyond the stream sample', async t => {
	const modelEntry = createZipLocalFile({
		filename: '3D/3dmodel.model',
		compressedData: new Uint8Array(reasonableDetectionSizeInBytes),
	});
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode('<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/></Types>'),
	});
	const zip = Buffer.concat([modelEntry, contentTypesEntry]);

	await assertFileTypeStreamChunkedResult(t, zip, {
		ext: '3mf',
		mime: 'model/3mf',
	});
	await assertFileTypeStreamWebResult(t, zip, {
		ext: '3mf',
		mime: 'model/3mf',
	});
});

test('iWork: detects Keynote (.key)', async t => {
	const expected = {ext: 'key', mime: 'application/vnd.apple.keynote'};
	const zip = Buffer.concat([
		createZipLocalFile({filename: 'Index/Document.iwa'}),
		createZipLocalFile({filename: 'Index/MasterSlide.iwa'}),
	]);
	t.deepEqual(await fileTypeFromBuffer(zip), expected);
	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(zip, 8)), expected);
});

test('iWork: detects Keynote (.key) with numbered MasterSlide', async t => {
	const expected = {ext: 'key', mime: 'application/vnd.apple.keynote'};
	const zip = Buffer.concat([
		createZipLocalFile({filename: 'Index/Document.iwa'}),
		createZipLocalFile({filename: 'Index/MasterSlide-2.iwa'}),
	]);
	t.deepEqual(await fileTypeFromBuffer(zip), expected);
	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(zip, 8)), expected);
});

test('iWork: streamed detection falls back to zip when only Index/Document.iwa is visible within the default sample size', async t => {
	const expected = {ext: 'key', mime: 'application/vnd.apple.keynote'};
	const zip = createZipArchive([
		{
			filename: 'Index/Document.iwa',
			compressedData: new Uint8Array(5000),
		},
		{
			filename: 'Index/MasterSlide.iwa',
		},
	]);

	t.deepEqual(await fileTypeFromBuffer(zip), expected);
	t.deepEqual(await fileTypeFromFile(await createTemporaryTestFile(t, zip)), expected);
	await assertFileTypeStreamChunkedResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	});
	await assertFileTypeStreamWebResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('iWork: streamed detection falls back to zip when a non-diagnostic entry appears before the real Keynote marker', async t => {
	const expected = {ext: 'key', mime: 'application/vnd.apple.keynote'};
	const zip = createZipArchive([
		{filename: 'Index/Document.iwa'},
		{filename: 'Metadata/DocumentIdentifier'},
		{
			filename: 'Index/SharedStrings.iwa',
			compressedData: new Uint8Array(5000),
		},
		{filename: 'Index/MasterSlide.iwa'},
	]);

	t.deepEqual(await fileTypeFromBuffer(zip), expected);
	t.deepEqual(await fileTypeFromFile(await createTemporaryTestFile(t, zip)), expected);
	await assertFileTypeStreamChunkedResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	});
	await assertFileTypeStreamWebResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('iWork: detects Numbers (.numbers)', async t => {
	const expected = {ext: 'numbers', mime: 'application/vnd.apple.numbers'};
	const zip = Buffer.concat([
		createZipLocalFile({filename: 'Index/Document.iwa'}),
		createZipLocalFile({filename: 'Index/Tables/Table-1.iwa'}),
	]);
	t.deepEqual(await fileTypeFromBuffer(zip), expected);
	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(zip, 8)), expected);
});

test('iWork: detects Pages (.pages)', async t => {
	const expected = {ext: 'pages', mime: 'application/vnd.apple.pages'};
	const zip = Buffer.concat([
		createZipLocalFile({filename: 'Index/Document.iwa'}),
	]);
	t.deepEqual(await fileTypeFromBuffer(zip), expected);
	t.deepEqual(await fileTypeFromBlob(new Blob([zip])), expected);
	t.deepEqual(await fileTypeFromFile(await createTemporaryTestFile(t, zip)), expected);
});

test('iWork: detects Pages (.pages) with CalculationEngine marker', async t => {
	const expected = {ext: 'pages', mime: 'application/vnd.apple.pages'};
	const zip = Buffer.concat([
		createZipLocalFile({filename: 'Index/Document.iwa'}),
		createZipLocalFile({filename: 'Index/CalculationEngine.iwa'}),
	]);
	t.deepEqual(await fileTypeFromBuffer(zip), expected);
	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(zip, 8)), expected);
});

test('.fileTypeStream() detects Pages when the stream ends exactly at sampleSize', async t => {
	const expected = {ext: 'pages', mime: 'application/vnd.apple.pages'};
	const zip = Buffer.concat([
		createZipLocalFile({filename: 'Index/Document.iwa'}),
	]);

	await assertFileTypeStreamChunkedResult(t, zip, expected, {sampleSize: zip.length});
	await assertFileTypeStreamWebResult(t, zip, expected, {sampleSize: zip.length});
});

test('iWork: detects Numbers (.numbers) with multiple table entries', async t => {
	const expected = {ext: 'numbers', mime: 'application/vnd.apple.numbers'};
	const zip = Buffer.concat([
		createZipLocalFile({filename: 'Index/Document.iwa'}),
		createZipLocalFile({filename: 'Index/Tables/Table-1.iwa'}),
		createZipLocalFile({filename: 'Index/Tables/Tile-1.iwa'}),
		createZipLocalFile({filename: 'Metadata/DocumentIdentifier'}),
	]);
	t.deepEqual(await fileTypeFromBuffer(zip), expected);
	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(zip, 8)), expected);
});

test('iWork: Keynote takes priority when both MasterSlide and Tables entries exist', async t => {
	const expected = {ext: 'key', mime: 'application/vnd.apple.keynote'};
	const zip = Buffer.concat([
		createZipLocalFile({filename: 'Index/Document.iwa'}),
		createZipLocalFile({filename: 'Index/MasterSlide.iwa'}),
		createZipLocalFile({filename: 'Index/Tables/Table-1.iwa'}),
	]);
	t.deepEqual(await fileTypeFromBuffer(zip), expected);
	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(zip, 8)), expected);
});

test('iWork: does not detect iWork without Index/Document.iwa', async t => {
	const zip = Buffer.concat([
		createZipLocalFile({filename: 'Index/MasterSlide.iwa'}),
	]);
	await assertZipTypeFromBufferAndChunkedStream(t, zip);
});

test('Does not use OOXML directory fallback when [Content_Types].xml parses but remains unresolved', async t => {
	const spreadsheetEntry = createZipLocalFile({
		filename: 'xl/workbook.bin',
		compressedData: new TextEncoder().encode('<workbook/>'),
	});
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode('<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-excel.sheet.binary.macroEnabled.main"/></Types>'),
	});
	const orderedZip = Buffer.concat([spreadsheetEntry, contentTypesEntry]);
	await assertZipTypeFromBufferAndChunkedStream(t, orderedZip);
});

test('Does not use OOXML directory fallback when unresolved [Content_Types].xml appears before spreadsheet entries', async t => {
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode('<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-excel.sheet.binary.macroEnabled.main"/></Types>'),
	});
	const spreadsheetEntry = createZipLocalFile({
		filename: 'xl/workbook.bin',
		compressedData: new TextEncoder().encode('<workbook/>'),
	});
	const orderedZip = Buffer.concat([contentTypesEntry, spreadsheetEntry]);
	await assertZipTypeFromBufferAndChunkedStream(t, orderedZip);
});

test('Does not use directory fallback when [Content_Types].xml cannot be read', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const unreadableContentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedMethod: 99,
		compressedData: new TextEncoder().encode('<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>'),
	});
	const orderedZip = Buffer.concat([wordEntry, unreadableContentTypesEntry]);
	await assertZipTypeFromBufferAndChunkedStream(t, orderedZip);
});

test('Falls back to zip for malformed [Content_Types].xml entries that overstate their size', async t => {
	const malformedZip = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedSize: 1024,
		uncompressedSize: 1024,
	});

	await assertZipTypeFromBuffer(t, malformedZip);
	await assertZipTypeFromBlob(t, malformedZip);
	await assertZipTypeFromFile(t, malformedZip);
});

test('Does not classify partial [Content_Types].xml data when its declared size is larger than the bytes present', async t => {
	const xml = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const malformedZip = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode(xml),
		compressedSize: xml.length + 1,
		uncompressedSize: xml.length + 1,
	});

	await assertZipTypeFromBuffer(t, malformedZip);
	await assertZipTypeFromBlob(t, malformedZip);
	await assertZipTypeFromChunkedStream(t, malformedZip);
	await assertZipTypeFromFile(t, malformedZip);
});

test('Does not classify partial deflated [Content_Types].xml data when its declared size is larger than the bytes present', async t => {
	const xml = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const compressed = deflateRawSync(Buffer.from(xml));
	const malformedZip = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedMethod: 8,
		compressedData: compressed,
		compressedSize: compressed.length + 1,
		uncompressedSize: xml.length,
	});

	await assertZipTypeFromBuffer(t, malformedZip);
	await assertZipTypeFromBlob(t, malformedZip);
	await assertZipTypeFromChunkedStream(t, malformedZip);
	await assertZipTypeFromFile(t, malformedZip);
});

test('Does not use directory fallback when malformed oversized [Content_Types].xml appears after a Word entry', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const malformedContentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedSize: 1024,
		uncompressedSize: 1024,
	});
	const orderedZip = Buffer.concat([wordEntry, malformedContentTypesEntry]);

	await assertZipTypeFromBuffer(t, orderedZip);
	await assertZipTypeFromBlob(t, orderedZip);
	await assertZipTypeFromChunkedStream(t, orderedZip);
	await assertZipTypeFromFile(t, orderedZip);
});

test('fileTypeFromFile does not abort on malformed [Content_Types].xml entries larger than Int32 reads', async t => {
	const malformedZip = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedSize: 0x80_00_00_00,
		uncompressedSize: 0x80_00_00_00,
	});
	const filePath = await createTemporaryTestFile(t, malformedZip);
	const script = `import {fileTypeFromFile} from './source/index.js'; console.log(JSON.stringify(await fileTypeFromFile(${JSON.stringify(filePath)})));`;
	const result = spawnSync(process.execPath, ['--input-type=module', '-e', script], {
		cwd: __dirname,
		encoding: 'utf8',
	});

	t.is(result.signal, null);
	t.is(result.status, 0);
	t.deepEqual(JSON.parse(result.stdout.trim()), {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('fileTypeFromFile does not throw on sparse [Content_Types].xml entries beyond the ZIP text probe limit', async t => {
	const compressedSize = 512 * 1024 * 1024;
	const malformedZip = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedSize,
		uncompressedSize: compressedSize,
	});
	const filePath = await createSparseTemporaryTestFile(t, malformedZip, malformedZip.length + compressedSize);
	const script = `import {fileTypeFromFile} from './source/index.js'; console.log(JSON.stringify(await fileTypeFromFile(${JSON.stringify(filePath)})));`;
	const result = spawnSync(process.execPath, ['--input-type=module', '-e', script], {
		cwd: __dirname,
		encoding: 'utf8',
	});

	t.is(result.signal, null);
	t.is(result.status, 0);
	t.deepEqual(JSON.parse(result.stdout.trim()), {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('Falls back to zip for malformed [Content_Types].xml entries larger than Int32 reads on buffer and blob inputs', async t => {
	const malformedZip = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedSize: 0x80_00_00_00,
		uncompressedSize: 0x80_00_00_00,
	});

	await assertZipTypeFromBuffer(t, malformedZip);
	await assertZipTypeFromBlob(t, malformedZip);
});

test('Allows known-size [Content_Types].xml entries below the ZIP text probe limit', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const contentTypesXml = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>' + ' '.repeat((maximumZipTextEntrySizeInBytes / 2) - 128);
	const oversizedContentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode(contentTypesXml),
	});
	const orderedZip = Buffer.concat([wordEntry, oversizedContentTypesEntry]);
	const bufferType = await fileTypeFromBuffer(orderedZip);
	t.deepEqual(bufferType, {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('fileTypeFromFile allows known-size [Content_Types].xml entries below the ZIP text probe limit', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const contentTypesXml = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>' + ' '.repeat((maximumZipTextEntrySizeInBytes / 2) - 128);
	const oversizedContentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode(contentTypesXml),
	});
	const orderedZip = Buffer.concat([wordEntry, oversizedContentTypesEntry]);
	const filePath = await createTemporaryTestFile(t, orderedZip);

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('fileTypeFromBlob allows known-size [Content_Types].xml entries below the ZIP text probe limit', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const contentTypesXml = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>' + ' '.repeat((maximumZipTextEntrySizeInBytes / 2) - 128);
	const oversizedContentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode(contentTypesXml),
	});
	const orderedZip = Buffer.concat([wordEntry, oversizedContentTypesEntry]);

	t.deepEqual(await fileTypeFromBlob(new Blob([orderedZip])), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('Detects [Content_Types].xml entries at the ZIP text probe limit', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat(maximumZipTextEntrySizeInBytes - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode(contentTypesXml),
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	t.deepEqual(await fileTypeFromBuffer(orderedZip), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
	t.deepEqual(await fileTypeFromBlob(new Blob([orderedZip])), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('fileTypeFromFile detects [Content_Types].xml entries at the ZIP text probe limit', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat(maximumZipTextEntrySizeInBytes - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode(contentTypesXml),
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);
	const filePath = await createTemporaryTestFile(t, orderedZip);

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('Streamed detection keeps [Content_Types].xml scanning at the ZIP text probe limit with small chunks', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat(maximumZipTextEntrySizeInBytes - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode(contentTypesXml),
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(orderedZip, 1)), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('Web Stream detection keeps [Content_Types].xml scanning at the ZIP text probe limit with small chunks', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat(maximumZipTextEntrySizeInBytes - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode(contentTypesXml),
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);
	const {stream} = createPatternWebStream(orderedZip, [1]);

	t.deepEqual(await new FileTypeParser().fromStream(stream), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('Falls back to zip when [Content_Types].xml entries exceed the ZIP text probe limit', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat((maximumZipTextEntrySizeInBytes + 1) - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode(contentTypesXml),
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	await assertZipTypeFromBuffer(t, orderedZip);
	await assertZipTypeFromBlob(t, orderedZip);
	await assertZipTypeFromFile(t, orderedZip);
	await assertZipTypeFromChunkedStream(t, orderedZip);
});

test('Web Stream detection falls back when [Content_Types].xml entries exceed the ZIP text probe limit', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat((maximumZipTextEntrySizeInBytes + 1) - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode(contentTypesXml),
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	await assertZipTypeFromWebStream(t, orderedZip, [1]);
});

test('.fileTypeStream() detects [Content_Types].xml entries at the ZIP text probe limit for Web Streams with a large sampleSize', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat(maximumZipTextEntrySizeInBytes - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode(contentTypesXml),
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	await assertFileTypeStreamWebResult(t, orderedZip, {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	}, {sampleSize: orderedZip.length});
});

test('.fileTypeStream() detects [Content_Types].xml entries at the ZIP text probe limit for chunked streams with a large sampleSize', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat(maximumZipTextEntrySizeInBytes - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode(contentTypesXml),
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	await assertFileTypeStreamChunkedResult(t, orderedZip, {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	}, {sampleSize: orderedZip.length});
});

test('.fileTypeStream() falls back to zip for stored [Content_Types].xml entries at the ZIP text probe limit with the default sampleSize for chunked streams', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat(maximumZipTextEntrySizeInBytes - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode(contentTypesXml),
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	await assertFileTypeStreamChunkedResult(t, orderedZip, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('.fileTypeStream() falls back to zip for stored [Content_Types].xml entries at the ZIP text probe limit with the default sampleSize for Web Streams', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat(maximumZipTextEntrySizeInBytes - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode(contentTypesXml),
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	await assertFileTypeStreamWebResult(t, orderedZip, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('.fileTypeStream() detects deflated [Content_Types].xml entries at the ZIP text probe limit with the default sampleSize for chunked streams', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat(maximumZipTextEntrySizeInBytes - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(contentTypesXml)),
		uncompressedSize: contentTypesXml.length,
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	await assertFileTypeStreamChunkedResult(t, orderedZip, {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('.fileTypeStream() detects deflated [Content_Types].xml entries at the ZIP text probe limit with the default sampleSize for Web Streams', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat(maximumZipTextEntrySizeInBytes - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(contentTypesXml)),
		uncompressedSize: contentTypesXml.length,
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	await assertFileTypeStreamWebResult(t, orderedZip, {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('.fileTypeStream() falls back to zip for deflated [Content_Types].xml entries at the previous ZIP text probe limit with the default sampleSize for chunked streams', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat(legacyOversizedZipTextEntrySizeInBytes - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(contentTypesXml)),
		uncompressedSize: contentTypesXml.length,
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	await assertFileTypeStreamChunkedResult(t, orderedZip, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('.fileTypeStream() falls back to zip for deflated [Content_Types].xml entries at the previous ZIP text probe limit with the default sampleSize for Web Streams', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat(legacyOversizedZipTextEntrySizeInBytes - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(contentTypesXml)),
		uncompressedSize: contentTypesXml.length,
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	await assertFileTypeStreamWebResult(t, orderedZip, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('.fileTypeStream() falls back when [Content_Types].xml entries exceed the ZIP text probe limit for Web Streams with a large sampleSize', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat((maximumZipTextEntrySizeInBytes + 1) - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode(contentTypesXml),
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	await assertFileTypeStreamWebResult(t, orderedZip, {
		ext: 'zip',
		mime: 'application/zip',
	}, {sampleSize: orderedZip.length});
});

test('.fileTypeStream() falls back when [Content_Types].xml entries exceed the ZIP text probe limit for chunked streams with a large sampleSize', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat((maximumZipTextEntrySizeInBytes + 1) - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode(contentTypesXml),
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	await assertFileTypeStreamChunkedResult(t, orderedZip, {
		ext: 'zip',
		mime: 'application/zip',
	}, {sampleSize: orderedZip.length});
});

test('.fileTypeStream() falls back for [Content_Types].xml entries at the previous ZIP text probe limit for chunked streams with a large sampleSize', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat(legacyOversizedZipTextEntrySizeInBytes - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode(contentTypesXml),
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	await assertFileTypeStreamChunkedResult(t, orderedZip, {
		ext: 'zip',
		mime: 'application/zip',
	}, {sampleSize: orderedZip.length});
});

test('.fileTypeStream() falls back for [Content_Types].xml entries at the previous ZIP text probe limit for Web Streams with a large sampleSize', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat(legacyOversizedZipTextEntrySizeInBytes - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode(contentTypesXml),
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	await assertFileTypeStreamWebResult(t, orderedZip, {
		ext: 'zip',
		mime: 'application/zip',
	}, {sampleSize: orderedZip.length});
});

test('.fileTypeStream() detects deflated [Content_Types].xml entries at the ZIP text probe limit for Web Streams with a large sampleSize', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat(maximumZipTextEntrySizeInBytes - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(contentTypesXml)),
		uncompressedSize: contentTypesXml.length,
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	await assertFileTypeStreamWebResult(t, orderedZip, {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	}, {sampleSize: orderedZip.length});
});

test('.fileTypeStream() detects deflated [Content_Types].xml entries at the ZIP text probe limit for chunked streams with a large sampleSize', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat(maximumZipTextEntrySizeInBytes - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(contentTypesXml)),
		uncompressedSize: contentTypesXml.length,
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	await assertFileTypeStreamChunkedResult(t, orderedZip, {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	}, {sampleSize: orderedZip.length});
});

test('.fileTypeStream() falls back when deflated [Content_Types].xml entries exceed the ZIP text probe limit for Web Streams with a large sampleSize', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat((maximumZipTextEntrySizeInBytes + 1) - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(contentTypesXml)),
		uncompressedSize: contentTypesXml.length,
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	await assertFileTypeStreamWebResult(t, orderedZip, {
		ext: 'zip',
		mime: 'application/zip',
	}, {sampleSize: orderedZip.length});
});

test('.fileTypeStream() falls back when deflated [Content_Types].xml entries exceed the ZIP text probe limit for chunked streams with a large sampleSize', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat((maximumZipTextEntrySizeInBytes + 1) - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(contentTypesXml)),
		uncompressedSize: contentTypesXml.length,
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	await assertFileTypeStreamChunkedResult(t, orderedZip, {
		ext: 'zip',
		mime: 'application/zip',
	}, {sampleSize: orderedZip.length});
});

test('.fileTypeStream() falls back for deflated [Content_Types].xml entries at the previous ZIP text probe limit for chunked streams with a large sampleSize', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat(legacyOversizedZipTextEntrySizeInBytes - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(contentTypesXml)),
		uncompressedSize: contentTypesXml.length,
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	await assertFileTypeStreamChunkedResult(t, orderedZip, {
		ext: 'zip',
		mime: 'application/zip',
	}, {sampleSize: orderedZip.length});
});

test('.fileTypeStream() falls back for deflated [Content_Types].xml entries at the previous ZIP text probe limit for Web Streams with a large sampleSize', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat(legacyOversizedZipTextEntrySizeInBytes - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(contentTypesXml)),
		uncompressedSize: contentTypesXml.length,
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	await assertFileTypeStreamWebResult(t, orderedZip, {
		ext: 'zip',
		mime: 'application/zip',
	}, {sampleSize: orderedZip.length});
});

test('Falls back to zip for deflated [Content_Types].xml entries at the previous ZIP text probe limit', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat(legacyOversizedZipTextEntrySizeInBytes - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(contentTypesXml)),
		uncompressedSize: contentTypesXml.length,
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	await assertZipTypeFromBuffer(t, orderedZip);
	await assertZipTypeFromBlob(t, orderedZip);
	await assertZipTypeFromFile(t, orderedZip);
});

test('All APIs detect deflated [Content_Types].xml entries at the ZIP text probe limit', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat(maximumZipTextEntrySizeInBytes - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(contentTypesXml)),
		uncompressedSize: contentTypesXml.length,
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);
	const filePath = await createTemporaryTestFile(t, orderedZip);

	t.deepEqual(await fileTypeFromBuffer(orderedZip), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
	t.deepEqual(await fileTypeFromBlob(new Blob([orderedZip])), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(orderedZip, 1)), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('Web Stream detection keeps deflated [Content_Types].xml scanning at the ZIP text probe limit', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat(maximumZipTextEntrySizeInBytes - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(contentTypesXml)),
		uncompressedSize: contentTypesXml.length,
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	t.deepEqual(await new FileTypeParser().fromStream(createPatternWebStream(orderedZip, [1]).stream), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('Falls back to zip when deflated [Content_Types].xml entries exceed the ZIP text probe limit', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat((maximumZipTextEntrySizeInBytes + 1) - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(contentTypesXml)),
		uncompressedSize: contentTypesXml.length,
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	await assertZipTypeFromBuffer(t, orderedZip);
	await assertZipTypeFromBlob(t, orderedZip);
	await assertZipTypeFromFile(t, orderedZip);
	await assertZipTypeFromChunkedStream(t, orderedZip);
});

test('Web Stream detection falls back when deflated [Content_Types].xml entries exceed the ZIP text probe limit', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = xmlPrefix + ' '.repeat((maximumZipTextEntrySizeInBytes + 1) - xmlPrefix.length);
	const contentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(contentTypesXml)),
		uncompressedSize: contentTypesXml.length,
	});
	const orderedZip = Buffer.concat([wordEntry, contentTypesEntry]);

	await assertZipTypeFromWebStream(t, orderedZip, [1]);
});

test('Allows many pre-IDAT PNG chunks for known-size buffers', async t => {
	const buffer = createPngWithAncillaryChunks(257);
	const type = await fileTypeFromBuffer(buffer);
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('Allows many pre-IDAT PNG chunks for streamed inputs', async t => {
	const buffer = createPngWithAncillaryChunks(257);
	const type = await fileTypeFromStream(createBufferedWebStream(buffer, 16));
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('Detects PNG when IDAT appears at the PNG chunk scan limit', async t => {
	const buffer = createPngWithAncillaryChunks(510);
	const type = await fileTypeFromBuffer(buffer);
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('fileTypeFromFile detects PNG when IDAT appears at the PNG chunk scan limit', async t => {
	const filePath = await createTemporaryTestFile(t, createPngWithAncillaryChunks(510), 'png');

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'png',
		mime: 'image/png',
	});
});

test('fileTypeFromBlob detects PNG when IDAT appears at the PNG chunk scan limit', async t => {
	const type = await fileTypeFromBlob(new Blob([createPngWithAncillaryChunks(510)]));
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('Streamed PNG detection keeps scanning at the PNG chunk limit', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createPngWithAncillaryChunks(510), 9));
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('Streamed PNG detection keeps scanning at the PNG chunk limit with small chunks', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createPngWithAncillaryChunks(510), 1));
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('Web Stream PNG detection keeps scanning at the PNG chunk limit', async t => {
	const {stream} = createPatternWebStream(createPngWithAncillaryChunks(510), [1, 2, 1, 3]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('Web Stream PNG detection keeps scanning at the PNG chunk limit with small chunks', async t => {
	const {stream} = createPatternWebStream(createPngWithAncillaryChunks(510), [1]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('Falls back to PNG when IDAT appears after the PNG chunk scan limit', async t => {
	const type = await fileTypeFromBuffer(createPngWithAncillaryChunks(511));
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('fileTypeFromFile falls back to PNG when IDAT appears after the PNG chunk scan limit', async t => {
	const filePath = await createTemporaryTestFile(t, createPngWithAncillaryChunks(511), 'png');

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'png',
		mime: 'image/png',
	});
});

test('fileTypeFromBlob falls back to PNG when IDAT appears after the PNG chunk scan limit', async t => {
	const type = await fileTypeFromBlob(new Blob([createPngWithAncillaryChunks(511)]));
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('Streamed PNG detection falls back after the PNG chunk limit', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createPngWithAncillaryChunks(511), 9));
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('Streamed PNG detection falls back after the PNG chunk limit with small chunks', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createPngWithAncillaryChunks(511), 1));
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('Web Stream PNG detection falls back after the PNG chunk limit', async t => {
	const {stream} = createPatternWebStream(createPngWithAncillaryChunks(511), [1, 2, 1, 3]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('Web Stream PNG detection falls back after the PNG chunk limit with small chunks', async t => {
	const {stream} = createPatternWebStream(createPngWithAncillaryChunks(511), [1]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('Detects APNG when acTL appears at the PNG chunk scan limit', async t => {
	const buffer = createPngWithAncillaryChunksAndAnimationControl(510);
	const type = await fileTypeFromBuffer(buffer);
	t.deepEqual(type, {
		ext: 'apng',
		mime: 'image/apng',
	});
});

test('fileTypeFromFile detects APNG when acTL appears at the PNG chunk scan limit', async t => {
	const filePath = await createTemporaryTestFile(t, createPngWithAncillaryChunksAndAnimationControl(510), 'png');

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'apng',
		mime: 'image/apng',
	});
});

test('fileTypeFromBlob detects APNG when acTL appears at the PNG chunk scan limit', async t => {
	const type = await fileTypeFromBlob(new Blob([createPngWithAncillaryChunksAndAnimationControl(510)]));
	t.deepEqual(type, {
		ext: 'apng',
		mime: 'image/apng',
	});
});

test('Falls back to PNG when acTL appears after the PNG chunk scan limit', async t => {
	const buffer = createPngWithAncillaryChunksAndAnimationControl(511);
	const type = await fileTypeFromBuffer(buffer);
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('fileTypeFromFile falls back to PNG when acTL appears after the PNG chunk scan limit', async t => {
	const filePath = await createTemporaryTestFile(t, createPngWithAncillaryChunksAndAnimationControl(511), 'png');

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'png',
		mime: 'image/png',
	});
});

test('fileTypeFromBlob falls back to PNG when acTL appears after the PNG chunk scan limit', async t => {
	const type = await fileTypeFromBlob(new Blob([createPngWithAncillaryChunksAndAnimationControl(511)]));
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('Streamed APNG detection keeps scanning at the PNG chunk limit', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createPngWithAncillaryChunksAndAnimationControl(510), 9));
	t.deepEqual(type, {
		ext: 'apng',
		mime: 'image/apng',
	});
});

test('Streamed APNG detection keeps scanning at the PNG chunk limit with small chunks', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createPngWithAncillaryChunksAndAnimationControl(510), 1));
	t.deepEqual(type, {
		ext: 'apng',
		mime: 'image/apng',
	});
});

test('Web Stream APNG detection keeps scanning at the PNG chunk limit', async t => {
	const {stream} = createPatternWebStream(createPngWithAncillaryChunksAndAnimationControl(510), [1, 2, 1, 3]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'apng',
		mime: 'image/apng',
	});
});

test('fileTypeFromBuffer still detects PNG when ancillary payload exceeds the stream payload probe limit', async t => {
	const type = await fileTypeFromBuffer(createPngWithAncillaryPayloadBeforeIdat(maximumStreamPayloadProbeSizeInBytes + 1));
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('fileTypeFromBuffer still detects PNG with a leading CgBI chunk', async t => {
	const type = await fileTypeFromBuffer(createPngWithLeadingCgbiChunk());
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('fileTypeFromBuffer still detects APNG when ancillary payload exceeds the stream payload probe limit', async t => {
	const type = await fileTypeFromBuffer(createPngWithAncillaryPayloadBeforeAnimationControl(maximumStreamPayloadProbeSizeInBytes + 1));
	t.deepEqual(type, {
		ext: 'apng',
		mime: 'image/apng',
	});
});

test('Streamed PNG detection keeps scanning when ancillary payload is exactly at the stream payload probe limit', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createPngWithAncillaryPayloadBeforeIdat(maximumStreamPayloadProbeSizeInBytes), 1024));
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('Web Stream PNG detection keeps scanning when ancillary payload is exactly at the stream payload probe limit', async t => {
	const {stream} = createPatternWebStream(createPngWithAncillaryPayloadBeforeIdat(maximumStreamPayloadProbeSizeInBytes), [1024]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('Streamed PNG detection falls back to PNG when ancillary payload exceeds the stream payload probe limit', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createPngWithAncillaryPayloadBeforeIdat(maximumStreamPayloadProbeSizeInBytes + 1), 1024));
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('Web Stream PNG detection falls back to PNG when ancillary payload exceeds the stream payload probe limit', async t => {
	const {stream} = createPatternWebStream(createPngWithAncillaryPayloadBeforeIdat(maximumStreamPayloadProbeSizeInBytes + 1), [1024]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('Streamed PNG detection does not classify oversized critical chunks as PNG', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createPngWithCriticalPayloadBeforeIdat('PLTE', maximumStreamPayloadProbeSizeInBytes + 1), 1024));
	t.is(type, undefined);
});

test('Web Stream PNG detection does not classify oversized critical chunks as PNG', async t => {
	const {stream} = createPatternWebStream(createPngWithCriticalPayloadBeforeIdat('PLTE', maximumStreamPayloadProbeSizeInBytes + 1), [1024]);
	const type = await new FileTypeParser().fromStream(stream);
	t.is(type, undefined);
});

test('Streamed APNG detection keeps scanning when ancillary payload is exactly at the stream payload probe limit', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createPngWithAncillaryPayloadBeforeAnimationControl(maximumStreamPayloadProbeSizeInBytes), 1024));
	t.deepEqual(type, {
		ext: 'apng',
		mime: 'image/apng',
	});
});

test('Web Stream APNG detection keeps scanning when ancillary payload is exactly at the stream payload probe limit', async t => {
	const {stream} = createPatternWebStream(createPngWithAncillaryPayloadBeforeAnimationControl(maximumStreamPayloadProbeSizeInBytes), [1024]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'apng',
		mime: 'image/apng',
	});
});

test('Streamed APNG detection falls back to PNG when ancillary payload exceeds the stream payload probe limit', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createPngWithAncillaryPayloadBeforeAnimationControl(maximumStreamPayloadProbeSizeInBytes + 1), 1024));
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('Web Stream APNG detection falls back to PNG when ancillary payload exceeds the stream payload probe limit', async t => {
	const {stream} = createPatternWebStream(createPngWithAncillaryPayloadBeforeAnimationControl(maximumStreamPayloadProbeSizeInBytes + 1), [1024]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('Streamed APNG detection still detects APNG when small ancillary chunks cumulatively exceed the stream payload probe limit', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createPngWithAncillaryChunksAndAnimationControl(5, new Uint8Array(256 * 1024)), 1024));
	t.deepEqual(type, {
		ext: 'apng',
		mime: 'image/apng',
	});
});

test('Web Stream APNG detection still detects APNG when small ancillary chunks cumulatively exceed the stream payload probe limit', async t => {
	const {stream} = createPatternWebStream(createPngWithAncillaryChunksAndAnimationControl(5, new Uint8Array(256 * 1024)), [1024]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'apng',
		mime: 'image/apng',
	});
});

test('Web Stream APNG detection keeps scanning at the PNG chunk limit with small chunks', async t => {
	const {stream} = createPatternWebStream(createPngWithAncillaryChunksAndAnimationControl(510), [1]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'apng',
		mime: 'image/apng',
	});
});

test('Streamed APNG detection falls back after the PNG chunk limit', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createPngWithAncillaryChunksAndAnimationControl(511), 9));
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('Streamed APNG detection falls back after the PNG chunk limit with small chunks', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createPngWithAncillaryChunksAndAnimationControl(511), 1));
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('Web Stream APNG detection falls back after the PNG chunk limit', async t => {
	const {stream} = createPatternWebStream(createPngWithAncillaryChunksAndAnimationControl(511), [1, 2, 1, 3]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('Web Stream APNG detection falls back after the PNG chunk limit with small chunks', async t => {
	const {stream} = createPatternWebStream(createPngWithAncillaryChunksAndAnimationControl(511), [1]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('Allows many TIFF tags for known-size buffers', async t => {
	const tagIds = Array.from({length: 257}, () => 0);
	tagIds[256] = 50_706;
	const buffer = createLittleEndianTiffWithTagIds(tagIds);
	const type = await fileTypeFromBuffer(buffer);
	t.deepEqual(type, {
		ext: 'dng',
		mime: 'image/x-adobe-dng',
	});
});

test('Allows many TIFF tags for streamed inputs', async t => {
	const tagIds = Array.from({length: 257}, () => 0);
	tagIds[256] = 50_706;
	const buffer = createLittleEndianTiffWithTagIds(tagIds);
	const type = await fileTypeFromStream(createBufferedWebStream(buffer, 16));
	t.deepEqual(type, {
		ext: 'dng',
		mime: 'image/x-adobe-dng',
	});
});

test('Detects TIFF tags at the TIFF tag scan limit', async t => {
	const type = await fileTypeFromBuffer(createLittleEndianTiffWithTagIdAtIndex(512, 511, 50_706));
	t.deepEqual(type, {
		ext: 'dng',
		mime: 'image/x-adobe-dng',
	});
});

test('fileTypeFromFile detects TIFF tags at the TIFF tag scan limit', async t => {
	const filePath = await createTemporaryTestFile(t, createLittleEndianTiffWithTagIdAtIndex(512, 511, 50_706), 'tif');

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'dng',
		mime: 'image/x-adobe-dng',
	});
});

test('fileTypeFromBlob detects TIFF tags at the TIFF tag scan limit', async t => {
	const type = await fileTypeFromBlob(new Blob([createLittleEndianTiffWithTagIdAtIndex(512, 511, 50_706)]));
	t.deepEqual(type, {
		ext: 'dng',
		mime: 'image/x-adobe-dng',
	});
});

test('Streamed TIFF detection keeps scanning at the TIFF tag limit', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createLittleEndianTiffWithTagIdAtIndex(512, 511, 50_706), 16));
	t.deepEqual(type, {
		ext: 'dng',
		mime: 'image/x-adobe-dng',
	});
});

test('Streamed TIFF detection keeps scanning at the TIFF tag limit with small chunks', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createLittleEndianTiffWithTagIdAtIndex(512, 511, 50_706), 1));
	t.deepEqual(type, {
		ext: 'dng',
		mime: 'image/x-adobe-dng',
	});
});

test('Web Stream TIFF detection keeps scanning at the TIFF tag limit', async t => {
	const {stream} = createPatternWebStream(createLittleEndianTiffWithTagIdAtIndex(512, 511, 50_706), [3, 5, 2, 7]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'dng',
		mime: 'image/x-adobe-dng',
	});
});

test('Web Stream TIFF detection keeps scanning at the TIFF tag limit with small chunks', async t => {
	const {stream} = createPatternWebStream(createLittleEndianTiffWithTagIdAtIndex(512, 511, 50_706), [1]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'dng',
		mime: 'image/x-adobe-dng',
	});
});

test('Detects big-endian TIFF tags at the TIFF tag scan limit', async t => {
	const type = await fileTypeFromBuffer(createBigEndianTiffWithTagIdAtIndex(512, 511, 50_706));
	t.deepEqual(type, {
		ext: 'dng',
		mime: 'image/x-adobe-dng',
	});
});

test('fileTypeFromFile detects big-endian TIFF tags at the TIFF tag scan limit', async t => {
	const filePath = await createTemporaryTestFile(t, createBigEndianTiffWithTagIdAtIndex(512, 511, 50_706), 'tif');

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'dng',
		mime: 'image/x-adobe-dng',
	});
});

test('fileTypeFromBlob detects big-endian TIFF tags at the TIFF tag scan limit', async t => {
	const type = await fileTypeFromBlob(new Blob([createBigEndianTiffWithTagIdAtIndex(512, 511, 50_706)]));
	t.deepEqual(type, {
		ext: 'dng',
		mime: 'image/x-adobe-dng',
	});
});

test('Big-endian streamed TIFF detection keeps scanning at the TIFF tag limit with small chunks', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createBigEndianTiffWithTagIdAtIndex(512, 511, 50_706), 1));
	t.deepEqual(type, {
		ext: 'dng',
		mime: 'image/x-adobe-dng',
	});
});

test('Big-endian Web Stream TIFF detection keeps scanning at the TIFF tag limit with small chunks', async t => {
	const {stream} = createPatternWebStream(createBigEndianTiffWithTagIdAtIndex(512, 511, 50_706), [1]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'dng',
		mime: 'image/x-adobe-dng',
	});
});

test('Detects ARW when its TIFF tag appears at the TIFF tag scan limit', async t => {
	const type = await fileTypeFromBuffer(createLittleEndianTiffWithTagIdAtIndex(512, 511, 50_341));
	t.deepEqual(type, {
		ext: 'arw',
		mime: 'image/x-sony-arw',
	});
});

test('fileTypeFromFile detects ARW when its TIFF tag appears at the TIFF tag scan limit', async t => {
	const filePath = await createTemporaryTestFile(t, createLittleEndianTiffWithTagIdAtIndex(512, 511, 50_341), 'tif');

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'arw',
		mime: 'image/x-sony-arw',
	});
});

test('fileTypeFromBlob detects ARW when its TIFF tag appears at the TIFF tag scan limit', async t => {
	const type = await fileTypeFromBlob(new Blob([createLittleEndianTiffWithTagIdAtIndex(512, 511, 50_341)]));
	t.deepEqual(type, {
		ext: 'arw',
		mime: 'image/x-sony-arw',
	});
});

test('Web Stream ARW detection keeps scanning at the TIFF tag limit with small chunks', async t => {
	const {stream} = createPatternWebStream(createLittleEndianTiffWithTagIdAtIndex(512, 511, 50_341), [1]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'arw',
		mime: 'image/x-sony-arw',
	});
});

test('Detects big-endian ARW when its TIFF tag appears at the TIFF tag scan limit', async t => {
	const type = await fileTypeFromBuffer(createBigEndianTiffWithTagIdAtIndex(512, 511, 50_341));
	t.deepEqual(type, {
		ext: 'arw',
		mime: 'image/x-sony-arw',
	});
});

test('fileTypeFromFile detects big-endian ARW when its TIFF tag appears at the TIFF tag scan limit', async t => {
	const filePath = await createTemporaryTestFile(t, createBigEndianTiffWithTagIdAtIndex(512, 511, 50_341), 'tif');

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'arw',
		mime: 'image/x-sony-arw',
	});
});

test('fileTypeFromBlob detects big-endian ARW when its TIFF tag appears at the TIFF tag scan limit', async t => {
	const type = await fileTypeFromBlob(new Blob([createBigEndianTiffWithTagIdAtIndex(512, 511, 50_341)]));
	t.deepEqual(type, {
		ext: 'arw',
		mime: 'image/x-sony-arw',
	});
});

test('Big-endian streamed ARW detection keeps scanning at the TIFF tag limit with small chunks', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createBigEndianTiffWithTagIdAtIndex(512, 511, 50_341), 1));
	t.deepEqual(type, {
		ext: 'arw',
		mime: 'image/x-sony-arw',
	});
});

test('Big-endian Web Stream ARW detection keeps scanning at the TIFF tag limit with small chunks', async t => {
	const {stream} = createPatternWebStream(createBigEndianTiffWithTagIdAtIndex(512, 511, 50_341), [1]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'arw',
		mime: 'image/x-sony-arw',
	});
});

test('Returns generic TIFF when no recognized TIFF tag appears at the TIFF tag scan limit', async t => {
	const type = await fileTypeFromBuffer(createLittleEndianTiffWithTagIdAtIndex(512, 511, 0));
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('fileTypeFromFile returns generic TIFF when no recognized TIFF tag appears at the TIFF tag scan limit', async t => {
	const filePath = await createTemporaryTestFile(t, createLittleEndianTiffWithTagIdAtIndex(512, 511, 0), 'tif');

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('fileTypeFromBlob returns generic TIFF when no recognized TIFF tag appears at the TIFF tag scan limit', async t => {
	const type = await fileTypeFromBlob(new Blob([createLittleEndianTiffWithTagIdAtIndex(512, 511, 0)]));
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('Returns generic big-endian TIFF when no recognized TIFF tag appears at the TIFF tag scan limit', async t => {
	const type = await fileTypeFromBuffer(createBigEndianTiffWithTagIdAtIndex(512, 511, 0));
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('fileTypeFromFile returns generic big-endian TIFF when no recognized TIFF tag appears at the TIFF tag scan limit', async t => {
	const filePath = await createTemporaryTestFile(t, createBigEndianTiffWithTagIdAtIndex(512, 511, 0), 'tif');

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('fileTypeFromBlob returns generic big-endian TIFF when no recognized TIFF tag appears at the TIFF tag scan limit', async t => {
	const type = await fileTypeFromBlob(new Blob([createBigEndianTiffWithTagIdAtIndex(512, 511, 0)]));
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('Streamed TIFF detection returns generic TIFF after scanning the full tag limit with small chunks', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createLittleEndianTiffWithTagIdAtIndex(512, 511, 0), 1));
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('Web Stream TIFF detection returns generic TIFF after scanning the full tag limit with small chunks', async t => {
	const {stream} = createPatternWebStream(createLittleEndianTiffWithTagIdAtIndex(512, 511, 0), [1]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('Web Stream TIFF detection returns generic big-endian TIFF after scanning the full tag limit with small chunks', async t => {
	const {stream} = createPatternWebStream(createBigEndianTiffWithTagIdAtIndex(512, 511, 0), [1]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('Falls back to generic TIFF when tags appear after the TIFF tag scan limit', async t => {
	const type = await fileTypeFromBuffer(createLittleEndianTiffWithTagIdAtIndex(513, 512, 50_706));
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('Falls back to generic TIFF when the DNG tag appears before the TIFF tag scan limit but the IFD is too large', async t => {
	const type = await fileTypeFromBuffer(createLittleEndianTiffWithTagIdAtIndex(513, 0, 50_706));
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('Falls back to generic big-endian TIFF when tags appear after the TIFF tag scan limit', async t => {
	const type = await fileTypeFromBuffer(createBigEndianTiffWithTagIdAtIndex(513, 512, 50_706));
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('fileTypeFromFile falls back to generic big-endian TIFF when tags appear after the TIFF tag scan limit', async t => {
	const filePath = await createTemporaryTestFile(t, createBigEndianTiffWithTagIdAtIndex(513, 512, 50_706), 'tif');

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('fileTypeFromBlob falls back to generic big-endian TIFF when tags appear after the TIFF tag scan limit', async t => {
	const type = await fileTypeFromBlob(new Blob([createBigEndianTiffWithTagIdAtIndex(513, 512, 50_706)]));
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('Falls back to generic big-endian TIFF when the DNG tag appears before the TIFF tag scan limit but the IFD is too large', async t => {
	const type = await fileTypeFromBuffer(createBigEndianTiffWithTagIdAtIndex(513, 0, 50_706));
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('fileTypeFromFile falls back to generic TIFF when tags appear after the TIFF tag scan limit', async t => {
	const filePath = await createTemporaryTestFile(t, createLittleEndianTiffWithTagIdAtIndex(513, 512, 50_706), 'tif');

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('fileTypeFromBlob falls back to generic TIFF when tags appear after the TIFF tag scan limit', async t => {
	const type = await fileTypeFromBlob(new Blob([createLittleEndianTiffWithTagIdAtIndex(513, 512, 50_706)]));
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('Streamed TIFF detection falls back after the TIFF tag limit', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createLittleEndianTiffWithTagIdAtIndex(513, 512, 50_706), 16));
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('Streamed TIFF detection falls back after the TIFF tag limit with small chunks', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createLittleEndianTiffWithTagIdAtIndex(513, 512, 50_706), 1));
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('Big-endian streamed TIFF detection falls back after the TIFF tag limit with small chunks', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createBigEndianTiffWithTagIdAtIndex(513, 512, 50_706), 1));
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('Big-endian Web Stream TIFF detection falls back after the TIFF tag limit with small chunks', async t => {
	const {stream} = createPatternWebStream(createBigEndianTiffWithTagIdAtIndex(513, 512, 50_706), [1]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('Falls back to generic TIFF when the ARW tag appears after the TIFF tag scan limit', async t => {
	const type = await fileTypeFromBuffer(createLittleEndianTiffWithTagIdAtIndex(513, 512, 50_341));
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('Falls back to generic TIFF when the ARW tag appears before the TIFF tag scan limit but the IFD is too large', async t => {
	const type = await fileTypeFromBuffer(createLittleEndianTiffWithTagIdAtIndex(513, 0, 50_341));
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('Falls back to generic big-endian TIFF when the ARW tag appears before the TIFF tag scan limit but the IFD is too large', async t => {
	const type = await fileTypeFromBuffer(createBigEndianTiffWithTagIdAtIndex(513, 0, 50_341));
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('Web Stream TIFF detection falls back after the TIFF tag limit', async t => {
	const {stream} = createPatternWebStream(createLittleEndianTiffWithTagIdAtIndex(513, 512, 50_706), [3, 5, 2, 7]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('Web Stream TIFF detection falls back after the TIFF tag limit with small chunks', async t => {
	const {stream} = createPatternWebStream(createLittleEndianTiffWithTagIdAtIndex(513, 512, 50_706), [1]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('Streamed TIFF detection falls back when the DNG tag appears before the TIFF tag scan limit but the IFD is too large', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createLittleEndianTiffWithTagIdAtIndex(513, 0, 50_706), 1));
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('Web Stream TIFF detection falls back when the big-endian DNG tag appears before the TIFF tag scan limit but the IFD is too large', async t => {
	const {stream} = createPatternWebStream(createBigEndianTiffWithTagIdAtIndex(513, 0, 50_706), [1]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('fileTypeFromBuffer still detects DNG when the TIFF IFD offset exceeds the stream probe limit', async t => {
	const type = await fileTypeFromBuffer(createLittleEndianTiffWithTagIdsAtOffset([50_706], maximumStreamPayloadProbeSizeInBytes + 8));
	t.deepEqual(type, {
		ext: 'dng',
		mime: 'image/x-adobe-dng',
	});
});

test('Streamed TIFF detection falls back to generic TIFF when the IFD offset exceeds the stream probe limit', async t => {
	const type = await fileTypeFromStream(createBufferedWebStream(createLittleEndianTiffWithTagIdsAtOffset([50_706], maximumStreamPayloadProbeSizeInBytes + 8), 1));
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('Web Stream TIFF detection falls back to generic TIFF when the IFD offset exceeds the stream probe limit', async t => {
	const {stream} = createPatternWebStream(createLittleEndianTiffWithTagIdsAtOffset([50_706], maximumStreamPayloadProbeSizeInBytes + 8), [1]);
	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'tif',
		mime: 'image/tiff',
	});
});

test('Does not scan unbounded inflated gzip payload while probing for tar.gz', async t => {
	const repeatedId3Payload = createRepeatedId3Payload(3, 8 * 1024 * 1024);
	const tarFixture = await readFile(path.join(__dirname, 'fixture', 'fixture.tar'));
	const gzipPayload = gzipSync(Buffer.concat([Buffer.from(repeatedId3Payload), tarFixture]));
	const bufferType = await fileTypeFromBuffer(gzipPayload);
	assertGzipFileType(t, bufferType);

	const streamType = await fileTypeFromStream(createBufferedWebStream(gzipPayload, 128));
	assertGzipFileType(t, streamType);
});

test('Still detects tar.gz with a single gzip layer', async t => {
	const tarFixture = await readFile(path.join(__dirname, 'fixture', 'fixture.tar'));
	const gzipPayload = createNestedGzip(tarFixture, 1);

	assertTarGzipFileType(t, await fileTypeFromBuffer(gzipPayload));
	assertTarGzipFileType(t, await fileTypeFromBlob(new Blob([gzipPayload])));

	const filePath = await createTemporaryTestFile(t, gzipPayload, 'gz');
	assertTarGzipFileType(t, await fileTypeFromFile(filePath));
	assertTarGzipFileType(t, await fileTypeFromStream(createBufferedWebStream(gzipPayload, 1)));

	const {stream} = createPatternWebStream(gzipPayload, [1]);
	assertTarGzipFileType(t, await new FileTypeParser().fromStream(stream));
});

test('Stops nested gzip probing after one layer', async t => {
	const tarFixture = await readFile(path.join(__dirname, 'fixture', 'fixture.tar'));
	const nestedGzipPayload = createNestedGzip(tarFixture, 2);

	assertGzipFileType(t, await fileTypeFromBuffer(nestedGzipPayload));
	assertGzipFileType(t, await fileTypeFromBlob(new Blob([nestedGzipPayload])));

	const filePath = await createTemporaryTestFile(t, nestedGzipPayload, 'gz');
	assertGzipFileType(t, await fileTypeFromFile(filePath));
	assertGzipFileType(t, await fileTypeFromStream(createBufferedWebStream(nestedGzipPayload, 1)));

	const {stream} = createPatternWebStream(nestedGzipPayload, [1]);
	assertGzipFileType(t, await new FileTypeParser().fromStream(stream));
});

test('.fileTypeStream() reports nested gzip as plain gzip and preserves the original bytes', async t => {
	const tarFixture = await readFile(path.join(__dirname, 'fixture', 'fixture.tar'));
	const nestedGzipPayload = createNestedGzip(tarFixture, 2);
	const detectionStream = await fileTypeStream(createBufferedWebStream(nestedGzipPayload, 1));
	assertGzipFileType(t, detectionStream.fileType);

	try {
		const streamBytes = await getStreamAsUint8Array(detectionStream);
		t.true(areUint8ArraysEqual(streamBytes, nestedGzipPayload));
	} finally {
		detectionStream.cancel();
	}
});

test('.fileTypeStream() reports nested gzip as plain gzip and preserves the original bytes for Web Streams', async t => {
	const tarFixture = await readFile(path.join(__dirname, 'fixture', 'fixture.tar'));
	const nestedGzipPayload = createNestedGzip(tarFixture, 2);
	const detectionStream = await fileTypeStream(new Blob([nestedGzipPayload]).stream());
	assertGzipFileType(t, detectionStream.fileType);

	const streamBytes = await getStreamAsUint8Array(detectionStream);
	t.true(areUint8ArraysEqual(streamBytes, nestedGzipPayload));
});

test('Reused FileTypeParser resets gzip probe depth after nested gzip fallback', async t => {
	const tarFixture = await readFile(path.join(__dirname, 'fixture', 'fixture.tar'));
	const nestedGzipPayload = createNestedGzip(tarFixture, 2);
	const singleLayerGzipPayload = createNestedGzip(tarFixture, 1);
	const parser = new FileTypeParser();

	assertGzipFileType(t, await parser.fromBuffer(nestedGzipPayload));
	assertTarGzipFileType(t, await parser.fromBuffer(singleLayerGzipPayload));

	const {stream: nestedWebStream} = createPatternWebStream(nestedGzipPayload, [1]);
	assertGzipFileType(t, await parser.fromStream(nestedWebStream));

	const {stream: tarWebStream} = createPatternWebStream(singleLayerGzipPayload, [1]);
	assertTarGzipFileType(t, await parser.fromStream(tarWebStream));
});

test('Reused FileTypeParser resets gzip probe depth after a malformed gzip probe', async t => {
	const malformedGzip = Uint8Array.from([31, 139, 8, 8, 137, 83, 29, 82, 0, 11]);
	const tarFixture = await readFile(path.join(__dirname, 'fixture', 'fixture.tar'));
	const singleLayerGzipPayload = createNestedGzip(tarFixture, 1);
	const parser = new FileTypeParser();

	assertGzipFileType(t, await parser.fromBuffer(malformedGzip));
	assertTarGzipFileType(t, await parser.fromBuffer(singleLayerGzipPayload));

	const {stream: malformedStream} = createPatternWebStream(malformedGzip, [1]);
	assertGzipFileType(t, await parser.fromStream(malformedStream));

	const {stream: tarWebStream} = createPatternWebStream(singleLayerGzipPayload, [1]);
	assertTarGzipFileType(t, await parser.fromStream(tarWebStream));
});

test('Reused FileTypeParser resets gzip probe depth after an aborted nested gzip probe', async t => {
	const tarFixture = await readFile(path.join(__dirname, 'fixture', 'fixture.tar'));
	const nestedGzipPayload = createNestedGzip(tarFixture, 2);
	const singleLayerGzipPayload = createNestedGzip(tarFixture, 1);

	function createAbortStream(buffer) {
		return new ReadableStream({
			pull(controller) {
				controller.enqueue(buffer.subarray(0, 16));
				const error = new Error('aborted nested gzip probe');
				error.name = 'AbortError';
				controller.error(error);
			},
		});
	}

	const parser = new FileTypeParser();
	const error = await t.throwsAsync(parser.fromStream(createAbortStream(nestedGzipPayload)));
	t.is(error.name, 'AbortError');
	assertTarGzipFileType(t, await parser.fromBuffer(singleLayerGzipPayload));
});

test('Reused FileTypeParser resets gzip probe depth across blob and file inputs', async t => {
	const tarFixture = await readFile(path.join(__dirname, 'fixture', 'fixture.tar'));
	const nestedGzipPayload = createNestedGzip(tarFixture, 2);
	const singleLayerGzipPayload = createNestedGzip(tarFixture, 1);
	const parser = new FileTypeParser();
	const filePath = await createTemporaryTestFile(t, singleLayerGzipPayload, 'gz');

	assertGzipFileType(t, await parser.fromBlob(new Blob([nestedGzipPayload])));
	assertTarGzipFileType(t, await parser.fromFile(filePath));
});

test('Reused FileTypeParser handles repeated nested gzip fallbacks before detecting tar.gz', async t => {
	const tarFixture = await readFile(path.join(__dirname, 'fixture', 'fixture.tar'));
	const nestedGzipPayload = createNestedGzip(tarFixture, 2);
	const singleLayerGzipPayload = createNestedGzip(tarFixture, 1);
	const parser = new FileTypeParser();

	assertGzipFileType(t, await parser.fromBuffer(nestedGzipPayload));
	assertGzipFileType(t, await parser.fromBlob(new Blob([nestedGzipPayload])));

	const {stream: nestedWebStream} = createPatternWebStream(nestedGzipPayload, [1]);
	assertGzipFileType(t, await parser.fromStream(nestedWebStream));

	assertTarGzipFileType(t, await parser.fromBuffer(singleLayerGzipPayload));
});

test('Reused FileTypeParser isolates tokenizer options across chunked stream, blob, Web Stream, and file inputs', async t => {
	const tarFixture = await readFile(path.join(__dirname, 'fixture', 'fixture.tar'));
	const nestedGzipPayload = createNestedGzip(tarFixture, 2);
	const singleLayerGzipPayload = createNestedGzip(tarFixture, 1);
	const parser = new FileTypeParser();
	const filePath = await createTemporaryTestFile(t, singleLayerGzipPayload, 'gz');

	assertGzipFileType(t, await parser.fromStream(createBufferedWebStream(nestedGzipPayload, 1)));
	assertTarGzipFileType(t, await parser.fromBlob(new Blob([singleLayerGzipPayload])));

	const {stream: nestedWebStream} = createPatternWebStream(nestedGzipPayload, [1]);
	assertGzipFileType(t, await parser.fromStream(nestedWebStream));
	assertTarGzipFileType(t, await parser.fromFile(filePath));
});

test('Reused FileTypeParser handles repeated nested gzip blob probes before detecting tar.gz from blob input', async t => {
	const tarFixture = await readFile(path.join(__dirname, 'fixture', 'fixture.tar'));
	const nestedGzipPayload = createNestedGzip(tarFixture, 2);
	const singleLayerGzipPayload = createNestedGzip(tarFixture, 1);
	const parser = new FileTypeParser();

	assertGzipFileType(t, await parser.fromBlob(new Blob([nestedGzipPayload])));
	assertGzipFileType(t, await parser.fromBlob(new Blob([nestedGzipPayload])));
	assertTarGzipFileType(t, await parser.fromBlob(new Blob([singleLayerGzipPayload])));
});

test('Reused FileTypeParser handles tokenizer-backed inputs after an aborted nested gzip stream probe', async t => {
	const tarFixture = await readFile(path.join(__dirname, 'fixture', 'fixture.tar'));
	const nestedGzipPayload = createNestedGzip(tarFixture, 2);
	const singleLayerGzipPayload = createNestedGzip(tarFixture, 1);
	const filePath = await createTemporaryTestFile(t, singleLayerGzipPayload, 'gz');

	function createAbortStream(buffer) {
		return new ReadableStream({
			pull(controller) {
				controller.enqueue(buffer.subarray(0, 16));
				const error = new Error('aborted nested gzip stream before tokenizer-backed reuse');
				error.name = 'AbortError';
				controller.error(error);
			},
		});
	}

	const parser = new FileTypeParser();
	const error = await t.throwsAsync(parser.fromStream(createAbortStream(nestedGzipPayload)));
	t.is(error.name, 'AbortError');
	assertTarGzipFileType(t, await parser.fromBlob(new Blob([singleLayerGzipPayload])));
	assertTarGzipFileType(t, await parser.fromFile(filePath));
});

test('Does not allocate huge memory for oversized ZIP mimetype entries', async t => {
	const buffer = createOversizedZipMimetypeEntry();

	const type = await fileTypeFromBuffer(buffer);
	t.deepEqual(type, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('Does not allocate huge memory for oversized ZIP mimetype entries from blob input', async t => {
	const buffer = createOversizedZipMimetypeEntry();
	await assertZipTypeFromBlob(t, buffer);
});

test('Does not allocate huge memory for oversized ZIP mimetype entries in stream mode', async t => {
	const buffer = createOversizedZipMimetypeEntry();
	await assertZipTypeFromChunkedStream(t, buffer);
});

test('Falls back to zip for malformed ZIP mimetype entries that overstate their size from file input', async t => {
	const malformedZip = createZipLocalFile({
		filename: 'mimetype',
		compressedSize: 1024,
		uncompressedSize: 1024,
	});
	await assertZipTypeFromFile(t, malformedZip);
});

test('Does not classify partial ZIP mimetype data when its declared size is larger than the bytes present', async t => {
	const mimeType = 'application/epub+zip';
	const malformedZip = createZipLocalFile({
		filename: 'mimetype',
		compressedData: new TextEncoder().encode(mimeType),
		compressedSize: mimeType.length + 1,
		uncompressedSize: mimeType.length + 1,
	});

	await assertZipTypeFromBuffer(t, malformedZip);
	await assertZipTypeFromBlob(t, malformedZip);
	await assertZipTypeFromChunkedStream(t, malformedZip);
	await assertZipTypeFromFile(t, malformedZip);
});

test('Does not classify partial deflated ZIP mimetype data when its declared size is larger than the bytes present', async t => {
	const mimeType = 'application/epub+zip';
	const compressed = deflateRawSync(Buffer.from(mimeType));
	const malformedZip = createZipLocalFile({
		filename: 'mimetype',
		compressedMethod: 8,
		compressedData: compressed,
		compressedSize: compressed.length + 1,
		uncompressedSize: mimeType.length,
	});

	await assertZipTypeFromBuffer(t, malformedZip);
	await assertZipTypeFromBlob(t, malformedZip);
	await assertZipTypeFromChunkedStream(t, malformedZip);
	await assertZipTypeFromFile(t, malformedZip);
});

test('fileTypeFromFile does not abort on malformed ZIP mimetype entries larger than Int32 reads', async t => {
	const malformedZip = createOversizedZipMimetypeEntry();
	const filePath = await createTemporaryTestFile(t, malformedZip);
	const script = `import {fileTypeFromFile} from './source/index.js'; console.log(JSON.stringify(await fileTypeFromFile(${JSON.stringify(filePath)})));`;
	const result = spawnSync(process.execPath, ['--input-type=module', '-e', script], {
		cwd: __dirname,
		encoding: 'utf8',
	});

	t.is(result.signal, null);
	t.is(result.status, 0);
	t.deepEqual(JSON.parse(result.stdout.trim()), {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('fileTypeFromFile does not throw on sparse ZIP mimetype entries beyond the ZIP text probe limit', async t => {
	const compressedSize = 512 * 1024 * 1024;
	const malformedZip = createZipLocalFile({
		filename: 'mimetype',
		compressedSize,
		uncompressedSize: compressedSize,
	});
	const filePath = await createSparseTemporaryTestFile(t, malformedZip, malformedZip.length + compressedSize);
	const script = `import {fileTypeFromFile} from './source/index.js'; console.log(JSON.stringify(await fileTypeFromFile(${JSON.stringify(filePath)})));`;
	const result = spawnSync(process.execPath, ['--input-type=module', '-e', script], {
		cwd: __dirname,
		encoding: 'utf8',
	});

	t.is(result.signal, null);
	t.is(result.status, 0);
	t.deepEqual(JSON.parse(result.stdout.trim()), {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('Detects ZIP mimetype entries at the ZIP text probe limit', async t => {
	const mimeType = 'application/epub+zip';
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedData: new TextEncoder().encode(mimeType + ' '.repeat(maximumZipTextEntrySizeInBytes - mimeType.length)),
	});

	t.deepEqual(await fileTypeFromBuffer(mimetypeEntry), {
		ext: 'epub',
		mime: 'application/epub+zip',
	});
	t.deepEqual(await fileTypeFromBlob(new Blob([mimetypeEntry])), {
		ext: 'epub',
		mime: 'application/epub+zip',
	});
});

test('fileTypeFromFile detects ZIP mimetype entries at the ZIP text probe limit', async t => {
	const mimeType = 'application/epub+zip';
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedData: new TextEncoder().encode(mimeType + ' '.repeat(maximumZipTextEntrySizeInBytes - mimeType.length)),
	});
	const filePath = await createTemporaryTestFile(t, mimetypeEntry);

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'epub',
		mime: 'application/epub+zip',
	});
});

test('Streamed detection keeps ZIP mimetype scanning at the ZIP text probe limit with small chunks', async t => {
	const mimeType = 'application/epub+zip';
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedData: new TextEncoder().encode(mimeType + ' '.repeat(maximumZipTextEntrySizeInBytes - mimeType.length)),
	});

	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(mimetypeEntry, 1)), {
		ext: 'epub',
		mime: 'application/epub+zip',
	});
});

test('Web Stream detection keeps ZIP mimetype scanning at the ZIP text probe limit with small chunks', async t => {
	const mimeType = 'application/epub+zip';
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedData: new TextEncoder().encode(mimeType + ' '.repeat(maximumZipTextEntrySizeInBytes - mimeType.length)),
	});
	const {stream} = createPatternWebStream(mimetypeEntry, [1]);

	t.deepEqual(await new FileTypeParser().fromStream(stream), {
		ext: 'epub',
		mime: 'application/epub+zip',
	});
});

test('Falls back to zip when ZIP mimetype entries exceed the ZIP text probe limit', async t => {
	const mimeType = 'application/epub+zip';
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedData: new TextEncoder().encode(mimeType + ' '.repeat((maximumZipTextEntrySizeInBytes + 1) - mimeType.length)),
	});

	await assertZipTypeFromBuffer(t, mimetypeEntry);
	await assertZipTypeFromBlob(t, mimetypeEntry);
	await assertZipTypeFromFile(t, mimetypeEntry);
	await assertZipTypeFromChunkedStream(t, mimetypeEntry);
});

test('Web Stream detection falls back when ZIP mimetype entries exceed the ZIP text probe limit', async t => {
	const mimeType = 'application/epub+zip';
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedData: new TextEncoder().encode(mimeType + ' '.repeat((maximumZipTextEntrySizeInBytes + 1) - mimeType.length)),
	});

	await assertZipTypeFromWebStream(t, mimetypeEntry, [1]);
});

test('.fileTypeStream() detects ZIP mimetype entries at the ZIP text probe limit for chunked streams with a large sampleSize', async t => {
	const mimeType = 'application/epub+zip';
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedData: new TextEncoder().encode(mimeType + ' '.repeat(maximumZipTextEntrySizeInBytes - mimeType.length)),
	});

	await assertFileTypeStreamChunkedResult(t, mimetypeEntry, {
		ext: 'epub',
		mime: 'application/epub+zip',
	}, {sampleSize: mimetypeEntry.length});
});

test('.fileTypeStream() detects ZIP mimetype entries at the ZIP text probe limit for Web Streams with a large sampleSize', async t => {
	const mimeType = 'application/epub+zip';
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedData: new TextEncoder().encode(mimeType + ' '.repeat(maximumZipTextEntrySizeInBytes - mimeType.length)),
	});

	await assertFileTypeStreamWebResult(t, mimetypeEntry, {
		ext: 'epub',
		mime: 'application/epub+zip',
	}, {sampleSize: mimetypeEntry.length});
});

test('.fileTypeStream() falls back when ZIP mimetype entries exceed the ZIP text probe limit for chunked streams with a large sampleSize', async t => {
	const mimeType = 'application/epub+zip';
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedData: new TextEncoder().encode(mimeType + ' '.repeat((maximumZipTextEntrySizeInBytes + 1) - mimeType.length)),
	});

	await assertFileTypeStreamChunkedResult(t, mimetypeEntry, {
		ext: 'zip',
		mime: 'application/zip',
	}, {sampleSize: mimetypeEntry.length});
});

test('.fileTypeStream() falls back when ZIP mimetype entries exceed the ZIP text probe limit for Web Streams with a large sampleSize', async t => {
	const mimeType = 'application/epub+zip';
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedData: new TextEncoder().encode(mimeType + ' '.repeat((maximumZipTextEntrySizeInBytes + 1) - mimeType.length)),
	});

	await assertFileTypeStreamWebResult(t, mimetypeEntry, {
		ext: 'zip',
		mime: 'application/zip',
	}, {sampleSize: mimetypeEntry.length});
});

test('.fileTypeStream() falls back for ZIP mimetype entries at the previous ZIP text probe limit for Web Streams with a large sampleSize', async t => {
	const mimeType = 'application/epub+zip';
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedData: new TextEncoder().encode(mimeType + ' '.repeat(legacyOversizedZipTextEntrySizeInBytes - mimeType.length)),
	});

	await assertFileTypeStreamWebResult(t, mimetypeEntry, {
		ext: 'zip',
		mime: 'application/zip',
	}, {sampleSize: mimetypeEntry.length});
});

test('.fileTypeStream() falls back for ZIP mimetype entries at the previous ZIP text probe limit for chunked streams with a large sampleSize', async t => {
	const mimeType = 'application/epub+zip';
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedData: new TextEncoder().encode(mimeType + ' '.repeat(legacyOversizedZipTextEntrySizeInBytes - mimeType.length)),
	});

	await assertFileTypeStreamChunkedResult(t, mimetypeEntry, {
		ext: 'zip',
		mime: 'application/zip',
	}, {sampleSize: mimetypeEntry.length});
});

test('.fileTypeStream() detects deflated ZIP mimetype entries at the ZIP text probe limit for chunked streams with a large sampleSize', async t => {
	const mimeType = 'application/epub+zip';
	const mimetype = mimeType + ' '.repeat(maximumZipTextEntrySizeInBytes - mimeType.length);
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(mimetype)),
		uncompressedSize: mimetype.length,
	});

	await assertFileTypeStreamChunkedResult(t, mimetypeEntry, {
		ext: 'epub',
		mime: 'application/epub+zip',
	}, {sampleSize: mimetypeEntry.length});
});

test('.fileTypeStream() detects deflated ZIP mimetype entries at the ZIP text probe limit for Web Streams with a large sampleSize', async t => {
	const mimeType = 'application/epub+zip';
	const mimetype = mimeType + ' '.repeat(maximumZipTextEntrySizeInBytes - mimeType.length);
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(mimetype)),
		uncompressedSize: mimetype.length,
	});

	await assertFileTypeStreamWebResult(t, mimetypeEntry, {
		ext: 'epub',
		mime: 'application/epub+zip',
	}, {sampleSize: mimetypeEntry.length});
});

test('.fileTypeStream() falls back to zip for stored ZIP mimetype entries at the ZIP text probe limit with the default sampleSize for chunked streams', async t => {
	const mimeType = 'application/epub+zip';
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedData: new TextEncoder().encode(mimeType + ' '.repeat(maximumZipTextEntrySizeInBytes - mimeType.length)),
	});

	await assertFileTypeStreamChunkedResult(t, mimetypeEntry, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('.fileTypeStream() falls back to zip for stored ZIP mimetype entries at the ZIP text probe limit with the default sampleSize for Web Streams', async t => {
	const mimeType = 'application/epub+zip';
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedData: new TextEncoder().encode(mimeType + ' '.repeat(maximumZipTextEntrySizeInBytes - mimeType.length)),
	});

	await assertFileTypeStreamWebResult(t, mimetypeEntry, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('.fileTypeStream() detects deflated ZIP mimetype entries at the ZIP text probe limit with the default sampleSize for chunked streams', async t => {
	const mimeType = 'application/epub+zip';
	const mimetype = mimeType + ' '.repeat(maximumZipTextEntrySizeInBytes - mimeType.length);
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(mimetype)),
		uncompressedSize: mimetype.length,
	});

	await assertFileTypeStreamChunkedResult(t, mimetypeEntry, {
		ext: 'epub',
		mime: 'application/epub+zip',
	});
});

test('.fileTypeStream() detects deflated ZIP mimetype entries at the ZIP text probe limit with the default sampleSize for Web Streams', async t => {
	const mimeType = 'application/epub+zip';
	const mimetype = mimeType + ' '.repeat(maximumZipTextEntrySizeInBytes - mimeType.length);
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(mimetype)),
		uncompressedSize: mimetype.length,
	});

	await assertFileTypeStreamWebResult(t, mimetypeEntry, {
		ext: 'epub',
		mime: 'application/epub+zip',
	});
});

test('.fileTypeStream() falls back to zip for deflated ZIP mimetype entries at the previous ZIP text probe limit with the default sampleSize for chunked streams', async t => {
	const mimeType = 'application/epub+zip';
	const mimetype = mimeType + ' '.repeat(legacyOversizedZipTextEntrySizeInBytes - mimeType.length);
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(mimetype)),
		uncompressedSize: mimetype.length,
	});

	await assertFileTypeStreamChunkedResult(t, mimetypeEntry, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('.fileTypeStream() falls back to zip for deflated ZIP mimetype entries at the previous ZIP text probe limit with the default sampleSize for Web Streams', async t => {
	const mimeType = 'application/epub+zip';
	const mimetype = mimeType + ' '.repeat(legacyOversizedZipTextEntrySizeInBytes - mimeType.length);
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(mimetype)),
		uncompressedSize: mimetype.length,
	});

	await assertFileTypeStreamWebResult(t, mimetypeEntry, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('.fileTypeStream() falls back when deflated ZIP mimetype entries exceed the ZIP text probe limit for chunked streams with a large sampleSize', async t => {
	const mimeType = 'application/epub+zip';
	const mimetype = mimeType + ' '.repeat((maximumZipTextEntrySizeInBytes + 1) - mimeType.length);
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(mimetype)),
		uncompressedSize: mimetype.length,
	});

	await assertFileTypeStreamChunkedResult(t, mimetypeEntry, {
		ext: 'zip',
		mime: 'application/zip',
	}, {sampleSize: mimetypeEntry.length});
});

test('.fileTypeStream() falls back when deflated ZIP mimetype entries exceed the ZIP text probe limit for Web Streams with a large sampleSize', async t => {
	const mimeType = 'application/epub+zip';
	const mimetype = mimeType + ' '.repeat((maximumZipTextEntrySizeInBytes + 1) - mimeType.length);
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(mimetype)),
		uncompressedSize: mimetype.length,
	});

	await assertFileTypeStreamWebResult(t, mimetypeEntry, {
		ext: 'zip',
		mime: 'application/zip',
	}, {sampleSize: mimetypeEntry.length});
});

test('.fileTypeStream() falls back for deflated ZIP mimetype entries at the previous ZIP text probe limit for Web Streams with a large sampleSize', async t => {
	const mimeType = 'application/epub+zip';
	const mimetype = mimeType + ' '.repeat(legacyOversizedZipTextEntrySizeInBytes - mimeType.length);
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(mimetype)),
		uncompressedSize: mimetype.length,
	});

	await assertFileTypeStreamWebResult(t, mimetypeEntry, {
		ext: 'zip',
		mime: 'application/zip',
	}, {sampleSize: mimetypeEntry.length});
});

test('.fileTypeStream() falls back for deflated ZIP mimetype entries at the previous ZIP text probe limit for chunked streams with a large sampleSize', async t => {
	const mimeType = 'application/epub+zip';
	const mimetype = mimeType + ' '.repeat(legacyOversizedZipTextEntrySizeInBytes - mimeType.length);
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(mimetype)),
		uncompressedSize: mimetype.length,
	});

	await assertFileTypeStreamChunkedResult(t, mimetypeEntry, {
		ext: 'zip',
		mime: 'application/zip',
	}, {sampleSize: mimetypeEntry.length});
});

test('Falls back to zip for deflated ZIP mimetype entries at the previous ZIP text probe limit', async t => {
	const mimeType = 'application/epub+zip';
	const mimetype = mimeType + ' '.repeat(legacyOversizedZipTextEntrySizeInBytes - mimeType.length);
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(mimetype)),
		uncompressedSize: mimetype.length,
	});

	await assertZipTypeFromBuffer(t, mimetypeEntry);
	await assertZipTypeFromBlob(t, mimetypeEntry);
	await assertZipTypeFromFile(t, mimetypeEntry);
});

test('All APIs detect deflated ZIP mimetype entries at the ZIP text probe limit', async t => {
	const mimeType = 'application/epub+zip';
	const mimetype = mimeType + ' '.repeat(maximumZipTextEntrySizeInBytes - mimeType.length);
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(mimetype)),
		uncompressedSize: mimetype.length,
	});
	const filePath = await createTemporaryTestFile(t, mimetypeEntry);

	t.deepEqual(await fileTypeFromBuffer(mimetypeEntry), {
		ext: 'epub',
		mime: 'application/epub+zip',
	});
	t.deepEqual(await fileTypeFromBlob(new Blob([mimetypeEntry])), {
		ext: 'epub',
		mime: 'application/epub+zip',
	});
	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'epub',
		mime: 'application/epub+zip',
	});
	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(mimetypeEntry, 1)), {
		ext: 'epub',
		mime: 'application/epub+zip',
	});
});

test('Web Stream detection keeps deflated ZIP mimetype scanning at the ZIP text probe limit', async t => {
	const mimeType = 'application/epub+zip';
	const mimetype = mimeType + ' '.repeat(maximumZipTextEntrySizeInBytes - mimeType.length);
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(mimetype)),
		uncompressedSize: mimetype.length,
	});

	t.deepEqual(await new FileTypeParser().fromStream(createPatternWebStream(mimetypeEntry, [1]).stream), {
		ext: 'epub',
		mime: 'application/epub+zip',
	});
});

test('Falls back to zip when deflated ZIP mimetype entries exceed the ZIP text probe limit', async t => {
	const mimeType = 'application/epub+zip';
	const mimetype = mimeType + ' '.repeat((maximumZipTextEntrySizeInBytes + 1) - mimeType.length);
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(mimetype)),
		uncompressedSize: mimetype.length,
	});

	await assertZipTypeFromBuffer(t, mimetypeEntry);
	await assertZipTypeFromBlob(t, mimetypeEntry);
	await assertZipTypeFromFile(t, mimetypeEntry);
	await assertZipTypeFromChunkedStream(t, mimetypeEntry);
});

test('Web Stream detection falls back when deflated ZIP mimetype entries exceed the ZIP text probe limit', async t => {
	const mimeType = 'application/epub+zip';
	const mimetype = mimeType + ' '.repeat((maximumZipTextEntrySizeInBytes + 1) - mimeType.length);
	const mimetypeEntry = createZipLocalFile({
		filename: 'mimetype',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(mimetype)),
		uncompressedSize: mimetype.length,
	});

	await assertZipTypeFromWebStream(t, mimetypeEntry, [1]);
});

test('Falls back to zip for malformed deflated ZIP mimetype entries that overstate compressed size', async t => {
	const malformedZip = createZipLocalFile({
		filename: 'mimetype',
		compressedMethod: 8,
		compressedData: Uint8Array.from([0x00, 0x00, 0x00, 0x00, 0x00]),
		compressedSize: 1024,
		uncompressedSize: 20,
	});

	await assertZipTypeFromBuffer(t, malformedZip);
	await assertZipTypeFromBlob(t, malformedZip);
	await assertZipTypeFromChunkedStream(t, malformedZip);
	await assertZipTypeFromFile(t, malformedZip);
});

test('Falls back to zip for deflated ZIP mimetype entries that understate uncompressed size', async t => {
	const mimetypeEntry = createDeflatedZipWithUnderstatedMimetypeSize();

	await assertZipTypeFromAllDirectInputs(t, mimetypeEntry);
});

test('.fileTypeStream() falls back for deflated ZIP mimetype entries that understate uncompressed size with a large sampleSize', async t => {
	const mimetypeEntry = createDeflatedZipWithUnderstatedMimetypeSize();

	await assertFileTypeStreamFallsBackToZipWithLargeSampleSize(t, mimetypeEntry);
});

test('Does not throw on malformed ZIP with unexpected follow-up signature', async t => {
	const zipLocalFile = createZipLocalFile({
		filename: 'a',
		compressedMethod: 0,
		compressedData: Uint8Array.from([0x41]),
	});
	const malformedZip = Buffer.concat([zipLocalFile, Buffer.from([0, 0, 0, 0])]);
	await assertZipTypeFromBufferAndChunkedStream(t, malformedZip);
});

test('Does not throw on malformed ZIP deflate entry in [Content_Types].xml', async t => {
	const malformedDeflatePayload = Uint8Array.from([0x00, 0x00, 0x00, 0x00, 0x00]);
	const malformedZip = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedMethod: 8,
		compressedData: malformedDeflatePayload,
		uncompressedSize: 20,
	});
	await assertZipTypeFromBufferAndChunkedStream(t, malformedZip);
});

test('Falls back to zip for malformed deflated [Content_Types].xml entries that overstate compressed size', async t => {
	const malformedZip = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedMethod: 8,
		compressedData: Uint8Array.from([0x00, 0x00, 0x00, 0x00, 0x00]),
		compressedSize: 1024,
		uncompressedSize: 20,
	});

	await assertZipTypeFromBuffer(t, malformedZip);
	await assertZipTypeFromBlob(t, malformedZip);
	await assertZipTypeFromChunkedStream(t, malformedZip);
	await assertZipTypeFromFile(t, malformedZip);
});

test('Falls back to zip for deflated [Content_Types].xml entries that understate uncompressed size', async t => {
	const zip = createDeflatedZipWithUnderstatedContentTypesSize();

	await assertZipTypeFromAllDirectInputs(t, zip);
});

test('.fileTypeStream() falls back for deflated [Content_Types].xml entries that understate uncompressed size with a large sampleSize', async t => {
	const zip = createDeflatedZipWithUnderstatedContentTypesSize();

	await assertFileTypeStreamFallsBackToZipWithLargeSampleSize(t, zip);
});

test('Does not use directory fallback when malformed deflated oversized [Content_Types].xml appears after a Word entry', async t => {
	const wordEntry = createZipLocalFile({
		filename: 'word/document.xml',
		compressedData: new TextEncoder().encode('<w:document/>'),
	});
	const malformedContentTypesEntry = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedMethod: 8,
		compressedData: Uint8Array.from([0x00, 0x00, 0x00, 0x00, 0x00]),
		compressedSize: 1024,
		uncompressedSize: 20,
	});
	const orderedZip = Buffer.concat([wordEntry, malformedContentTypesEntry]);

	await assertZipTypeFromBuffer(t, orderedZip);
	await assertZipTypeFromBlob(t, orderedZip);
	await assertZipTypeFromChunkedStream(t, orderedZip);
	await assertZipTypeFromFile(t, orderedZip);
});

test('Keeps ZIP [Content_Types].xml inflate probing bounded for streams', async t => {
	const mimeMarker = 'ContentType="application/vnd.ms-word.document.macroenabled.main+xml"';
	const oversizedXml = mimeMarker + 'A'.repeat((2 * 1024 * 1024) - mimeMarker.length);
	const compressed = deflateRawSync(Buffer.from(oversizedXml, 'utf8'));
	const zip = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedMethod: 8,
		compressedData: compressed,
		uncompressedSize: 1,
	});
	await assertZipTypeFromChunkedStream(t, zip);
});

test('Allows deflated known-size [Content_Types].xml entries below the ZIP text probe limit', async t => {
	const contentTypesXml = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>' + ' '.repeat((maximumZipTextEntrySizeInBytes / 2) - 128);
	const compressed = deflateRawSync(Buffer.from(contentTypesXml, 'utf8'));
	const zip = Buffer.concat([
		createZipLocalFile({
			filename: 'word/document.xml',
			compressedData: new TextEncoder().encode('<w:document/>'),
		}),
		createZipLocalFile({
			filename: '[Content_Types].xml',
			compressedMethod: 8,
			compressedData: compressed,
			uncompressedSize: Buffer.byteLength(contentTypesXml),
		}),
	]);
	const type = await fileTypeFromBuffer(zip);
	t.deepEqual(type, {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('fileTypeFromFile allows deflated known-size [Content_Types].xml entries below the ZIP text probe limit', async t => {
	const contentTypesXml = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>' + ' '.repeat((maximumZipTextEntrySizeInBytes / 2) - 128);
	const compressed = deflateRawSync(Buffer.from(contentTypesXml, 'utf8'));
	const zip = Buffer.concat([
		createZipLocalFile({
			filename: 'word/document.xml',
			compressedData: new TextEncoder().encode('<w:document/>'),
		}),
		createZipLocalFile({
			filename: '[Content_Types].xml',
			compressedMethod: 8,
			compressedData: compressed,
			uncompressedSize: Buffer.byteLength(contentTypesXml),
		}),
	]);
	const filePath = await createTemporaryTestFile(t, zip);

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('fileTypeFromBlob allows deflated known-size [Content_Types].xml entries below the ZIP text probe limit', async t => {
	const contentTypesXml = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>' + ' '.repeat((maximumZipTextEntrySizeInBytes / 2) - 128);
	const compressed = deflateRawSync(Buffer.from(contentTypesXml, 'utf8'));
	const zip = Buffer.concat([
		createZipLocalFile({
			filename: 'word/document.xml',
			compressedData: new TextEncoder().encode('<w:document/>'),
		}),
		createZipLocalFile({
			filename: '[Content_Types].xml',
			compressedMethod: 8,
			compressedData: compressed,
			uncompressedSize: Buffer.byteLength(contentTypesXml),
		}),
	]);

	t.deepEqual(await fileTypeFromBlob(new Blob([zip])), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('Does not throw on ZIP with unsupported compression method in [Content_Types].xml', async t => {
	const malformedZip = createZipLocalFile({
		filename: '[Content_Types].xml',
		compressedMethod: 99,
		compressedData: Uint8Array.from([0x01, 0x02, 0x03, 0x04]),
		uncompressedSize: 4,
	});
	await assertZipTypeFromBufferAndChunkedStream(t, malformedZip);
});

test('Does not throw on ZIP with streamed [Content_Types].xml entry without descriptor data', async t => {
	const malformedZip = createZipLocalFile({
		filename: '[Content_Types].xml',
		generalPurposeBitFlag: 0x08,
		compressedMethod: 8,
		compressedData: Uint8Array.from([0x41, 0x42, 0x43]),
		compressedSize: 0,
		uncompressedSize: 0,
	});
	await assertZipTypeFromBufferAndChunkedStream(t, malformedZip);
});

test('Detects small ZIP mimetype descriptor entries', async t => {
	const streamedZip = createZipDataDescriptorFile({
		filename: 'mimetype',
		compressedData: new TextEncoder().encode('application/epub+zip'),
	});

	const bufferType = await fileTypeFromBuffer(streamedZip);
	t.deepEqual(bufferType, {
		ext: 'epub',
		mime: 'application/epub+zip',
	});

	const streamType = await fileTypeFromStream(createBufferedWebStream(streamedZip, 8));
	t.deepEqual(streamType, {
		ext: 'epub',
		mime: 'application/epub+zip',
	});
});

test('fileTypeFromFile detects small ZIP mimetype descriptor entries', async t => {
	const filePath = await createTemporaryTestFile(t, createZipDataDescriptorFile({
		filename: 'mimetype',
		compressedData: new TextEncoder().encode('application/epub+zip'),
	}));

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'epub',
		mime: 'application/epub+zip',
	});
});

test('Detects small ZIP mimetype descriptor entries with one-byte stream chunks', async t => {
	const streamedZip = createZipDataDescriptorFile({
		filename: 'mimetype',
		compressedData: new TextEncoder().encode('application/epub+zip'),
	});
	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(streamedZip, 1)), {
		ext: 'epub',
		mime: 'application/epub+zip',
	});
});

test('Detects small ZIP [Content_Types].xml descriptor entries', async t => {
	const streamedZip = createZipDataDescriptorFile({
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode('<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>'),
	});

	const bufferType = await fileTypeFromBuffer(streamedZip);
	t.deepEqual(bufferType, {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});

	const streamType = await fileTypeFromStream(createBufferedWebStream(streamedZip, 8));
	t.deepEqual(streamType, {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('Detects small deflated ZIP [Content_Types].xml descriptor entries', async t => {
	const contentTypesXml = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const streamedZip = createZipDataDescriptorFile({
		filename: '[Content_Types].xml',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(contentTypesXml)),
		uncompressedSize: Buffer.byteLength(contentTypesXml),
	});

	const bufferType = await fileTypeFromBuffer(streamedZip);
	t.deepEqual(bufferType, {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});

	const streamType = await fileTypeFromStream(createBufferedWebStream(streamedZip, 8));
	t.deepEqual(streamType, {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('Ignores ZIP descriptor signature bytes inside descriptor-backed [Content_Types].xml entries', async t => {
	const contentTypesXml = Buffer.concat([
		Buffer.from('<?xml version="1.0" encoding="UTF-8"?><Types>'),
		Buffer.from([0x50, 0x4B, 0x07, 0x08]),
		Buffer.from('<Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>'),
	]);
	const streamedZip = createZipDataDescriptorFile({
		filename: '[Content_Types].xml',
		compressedData: contentTypesXml,
	});
	const filePath = await createTemporaryTestFile(t, streamedZip);

	t.deepEqual(await fileTypeFromBuffer(streamedZip), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(streamedZip, 1)), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('fileTypeFromFile detects small deflated ZIP [Content_Types].xml descriptor entries', async t => {
	const contentTypesXml = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const filePath = await createTemporaryTestFile(t, createZipDataDescriptorFile({
		filename: '[Content_Types].xml',
		compressedMethod: 8,
		compressedData: deflateRawSync(Buffer.from(contentTypesXml)),
		uncompressedSize: Buffer.byteLength(contentTypesXml),
	}));

	const type = await fileTypeFromFile(filePath);
	t.deepEqual(type, {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('Allows streamed ZIP [Content_Types].xml descriptor probing at the exact size limit', async t => {
	const maximumZipEntrySizeInBytes = 1024 * 1024;
	const contentTypesPrefix = '<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>';
	const contentTypesXml = new TextEncoder().encode(contentTypesPrefix + 'A'.repeat(maximumZipEntrySizeInBytes - Buffer.byteLength(contentTypesPrefix)));
	const streamedZip = createZipDataDescriptorFile({
		filename: '[Content_Types].xml',
		compressedData: contentTypesXml,
	});

	t.deepEqual(await fileTypeFromBuffer(streamedZip), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(streamedZip, 8)), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
	t.deepEqual(await fileTypeFromFile(await createTemporaryTestFile(t, streamedZip)), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('Keeps unknown-size ZIP [Content_Types].xml descriptor probing bounded', async t => {
	const contentTypesXml = new TextEncoder().encode('<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>' + 'A'.repeat((1024 * 1024) + 1));
	const streamedZip = createZipDataDescriptorFile({
		filename: '[Content_Types].xml',
		compressedData: contentTypesXml,
	});

	await assertZipTypeFromBufferAndChunkedStream(t, streamedZip);
});

test('fileTypeFromFile keeps unknown-size ZIP [Content_Types].xml descriptor probing bounded', async t => {
	const contentTypesXml = new TextEncoder().encode('<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>' + 'A'.repeat((1024 * 1024) + 1));
	const streamedZip = createZipDataDescriptorFile({
		filename: '[Content_Types].xml',
		compressedData: contentTypesXml,
	});

	await assertZipTypeFromFile(t, streamedZip);
});

test('Keeps unknown-size ZIP mimetype descriptor probing bounded', async t => {
	const streamedZip = createZipDataDescriptorFile({
		filename: 'mimetype',
		compressedData: new TextEncoder().encode('application/epub+zip' + 'A'.repeat((1024 * 1024) + 1)),
	});

	await assertZipTypeFromBufferAndChunkedStream(t, streamedZip);
});

test('fileTypeFromFile keeps unknown-size ZIP mimetype descriptor probing bounded', async t => {
	const streamedZip = createZipDataDescriptorFile({
		filename: 'mimetype',
		compressedData: new TextEncoder().encode('application/epub+zip' + 'A'.repeat((1024 * 1024) + 1)),
	});

	await assertZipTypeFromFile(t, streamedZip);
});

test('Known-size APIs still detect EPUB when a descriptor-backed entry before ZIP mimetype detection is at the scan limit', async t => {
	const zip = createZipWithLeadingDescriptorMimetype(maximumZipTextEntrySizeInBytes);

	t.deepEqual(await fileTypeFromBuffer(zip), descriptorBoundaryEpubFileType);
	t.deepEqual(await fileTypeFromBlob(new Blob([zip])), descriptorBoundaryEpubFileType);
	t.deepEqual(await fileTypeFromFile(await createTemporaryTestFile(t, zip)), descriptorBoundaryEpubFileType);
	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(zip, 1)), descriptorBoundaryEpubFileType);
});

test('Web Stream detection keeps ZIP mimetype detection when a descriptor-backed entry before it is at the scan limit', async t => {
	const zip = createZipWithLeadingDescriptorMimetype(maximumZipTextEntrySizeInBytes);

	t.deepEqual(await new FileTypeParser().fromStream(createPatternWebStream(zip, [1]).stream), descriptorBoundaryEpubFileType);
});

test('.fileTypeStream() detects ZIP mimetype when a descriptor-backed entry before it is at the scan limit for chunked streams with a large sampleSize', async t => {
	const zip = createZipWithLeadingDescriptorMimetype(maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamChunkedResult(t, zip, descriptorBoundaryEpubFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() falls back when an oversized descriptor-backed entry precedes ZIP mimetype detection for chunked streams with a large sampleSize', async t => {
	const zip = createZipWithLeadingDescriptorMimetype(maximumZipTextEntrySizeInBytes + 1);

	await assertFileTypeStreamChunkedResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	}, {sampleSize: zip.length});
});

test('.fileTypeStream() detects ZIP mimetype when a descriptor-backed entry before it is at the scan limit for chunked streams with small chunks and a large sampleSize', async t => {
	const zip = createZipWithLeadingDescriptorMimetype(maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamChunkedResult(t, zip, descriptorBoundaryEpubFileType, {
		chunkSize: 256,
		sampleSize: zip.length,
	});
});

test('.fileTypeStream() falls back when an oversized descriptor-backed entry precedes ZIP mimetype detection for chunked streams with small chunks and a large sampleSize', async t => {
	const zip = createZipWithLeadingDescriptorMimetype(maximumZipTextEntrySizeInBytes + 1);

	await assertFileTypeStreamChunkedResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	}, {
		chunkSize: 256,
		sampleSize: zip.length,
	});
});

test('.fileTypeStream() falls back when a descriptor-backed entry before ZIP mimetype detection is at the scan limit for chunked streams with the default sampleSize', async t => {
	const zip = createZipWithLeadingDescriptorMimetype(maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamChunkedResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('.fileTypeStream() falls back when an oversized descriptor-backed entry precedes ZIP mimetype detection for chunked streams with the default sampleSize', async t => {
	const zip = createZipWithLeadingDescriptorMimetype(maximumZipTextEntrySizeInBytes + 1);

	await assertFileTypeStreamChunkedResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('.fileTypeStream() detects ZIP mimetype when a descriptor-backed entry before it is at the scan limit for Web Streams with a large sampleSize', async t => {
	const zip = createZipWithLeadingDescriptorMimetype(maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamWebResult(t, zip, descriptorBoundaryEpubFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() falls back when an oversized descriptor-backed entry precedes ZIP mimetype detection for Web Streams with a large sampleSize', async t => {
	const zip = createZipWithLeadingDescriptorMimetype(maximumZipTextEntrySizeInBytes + 1);

	await assertFileTypeStreamWebResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	}, {sampleSize: zip.length});
});

test('.fileTypeStream() falls back when a descriptor-backed entry before ZIP mimetype detection is at the scan limit for Web Streams with the default sampleSize', async t => {
	const zip = createZipWithLeadingDescriptorMimetype(maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamWebResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('Falls back to zip when an oversized descriptor-backed entry precedes ZIP mimetype detection', async t => {
	const zip = createZipWithLeadingDescriptorMimetype(maximumZipTextEntrySizeInBytes + 1);

	await assertZipTypeFromBuffer(t, zip);
	await assertZipTypeFromBlob(t, zip);
	await assertZipTypeFromFile(t, zip);
	await assertZipTypeFromChunkedStream(t, zip);
});

test('Web Stream detection falls back when an oversized descriptor-backed entry precedes ZIP mimetype detection', async t => {
	const zip = createZipWithLeadingDescriptorMimetype(maximumZipTextEntrySizeInBytes + 1);

	await assertZipTypeFromWebStream(t, zip, [1]);
});

test('Known-size APIs fall back to zip when repeated descriptor-backed entries consume the cumulative limit before ZIP mimetype detection', async t => {
	const zip = createZipWithRepeatedDescriptorMimetype(15, maximumZipTextEntrySizeInBytes);

	await assertZipTypeFromKnownSizeInputs(t, zip);
});

test('Known-size APIs still detect EPUB when repeated small descriptor-backed entries stay below the known-size ZIP scan budget', async t => {
	const zip = createZipWithRepeatedDescriptorMimetype(4, maximumZipTextEntrySizeInBytes / 8);

	t.deepEqual(await fileTypeFromBuffer(zip), descriptorBoundaryEpubFileType);
	t.deepEqual(await fileTypeFromBlob(new Blob([zip])), descriptorBoundaryEpubFileType);
	t.deepEqual(await fileTypeFromFile(await createTemporaryTestFile(t, zip)), descriptorBoundaryEpubFileType);
});

test('Known-size APIs still detect EPUB when repeated descriptor-backed entries are exactly at the known-size ZIP scan budget', async t => {
	const zip = createZipWithRepeatedDescriptorMimetypeAtKnownSizeBudget();

	t.deepEqual(await fileTypeFromBuffer(zip), descriptorBoundaryEpubFileType);
	t.deepEqual(await fileTypeFromBlob(new Blob([zip])), descriptorBoundaryEpubFileType);
	t.deepEqual(await fileTypeFromFile(await createTemporaryTestFile(t, zip)), descriptorBoundaryEpubFileType);
});

test('.fileTypeStream() still detects EPUB when repeated small descriptor-backed entries stay below the known-size ZIP scan budget for chunked streams with a large sampleSize', async t => {
	const zip = createZipWithRepeatedDescriptorMimetype(4, maximumZipTextEntrySizeInBytes / 8);

	await assertFileTypeStreamChunkedResult(t, zip, descriptorBoundaryEpubFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() still detects EPUB when repeated small descriptor-backed entries stay below the known-size ZIP scan budget for Web Streams with a large sampleSize', async t => {
	const zip = createZipWithRepeatedDescriptorMimetype(4, maximumZipTextEntrySizeInBytes / 8);

	await assertFileTypeStreamWebResult(t, zip, descriptorBoundaryEpubFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() still detects EPUB when repeated descriptor-backed entries are exactly at the known-size ZIP scan budget for chunked streams with a large sampleSize', async t => {
	const zip = createZipWithRepeatedDescriptorMimetypeAtKnownSizeBudget();

	await assertFileTypeStreamChunkedResult(t, zip, descriptorBoundaryEpubFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() still detects EPUB when repeated descriptor-backed entries are exactly at the known-size ZIP scan budget for Web Streams with a large sampleSize', async t => {
	const zip = createZipWithRepeatedDescriptorMimetypeAtKnownSizeBudget();

	await assertFileTypeStreamWebResult(t, zip, descriptorBoundaryEpubFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() still detects EPUB when repeated descriptor-backed ZIP mimetype entries are exactly at the known-size ZIP scan budget for chunked streams with hostile mixed chunking and a large sampleSize', async t => {
	const zip = createZipWithRepeatedDescriptorMimetypeAtKnownSizeBudget();

	await assertFileTypeStreamChunkedResult(t, zip, descriptorBoundaryEpubFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() still detects EPUB when repeated descriptor-backed ZIP mimetype entries are exactly at the known-size ZIP scan budget for Web Streams with hostile mixed chunking and a large sampleSize', async t => {
	const zip = createZipWithRepeatedDescriptorMimetypeAtKnownSizeBudget();

	await assertFileTypeStreamWebResult(t, zip, descriptorBoundaryEpubFileType, {sampleSize: zip.length});
});

test('Known-size APIs fall back to zip when repeated descriptor-backed entries exceed the known-size ZIP scan budget by one byte before ZIP mimetype detection', async t => {
	const zip = createZipWithRepeatedDescriptorMimetypeAtKnownSizeBudget(1);

	await assertZipTypeFromKnownSizeInputs(t, zip);
});

test('Known-size APIs fall back to zip when repeated descriptor-backed entries exceed the cumulative limit before ZIP mimetype detection', async t => {
	const zip = createZipWithRepeatedDescriptorMimetype(17, maximumZipTextEntrySizeInBytes);

	await assertZipTypeFromBuffer(t, zip);
	await assertZipTypeFromBlob(t, zip);
	await assertZipTypeFromFile(t, zip);
});

test('Streamed ZIP detection still detects EPUB when a stored entry before it is at the scan limit', async t => {
	const zip = createZipWithLeadingStoredMimetype(maximumZipTextEntrySizeInBytes);

	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(zip, 1)), descriptorBoundaryEpubFileType);
});

test('Web Stream detection still detects EPUB when a stored entry before it is at the scan limit', async t => {
	const zip = createZipWithLeadingStoredMimetype(maximumZipTextEntrySizeInBytes);

	t.deepEqual(await new FileTypeParser().fromStream(createPatternWebStream(zip, [1]).stream), descriptorBoundaryEpubFileType);
});

test('Streamed ZIP detection keeps stored-entry probing bounded when an oversized entry precedes ZIP mimetype detection', async t => {
	const chunkSize = 64 * 1024;
	const zip = createZipWithLeadingStoredMimetype(maximumZipTextEntrySizeInBytes + 1);
	const {state, stream} = createPatternWebStream(zip, [chunkSize]);

	const type = await fileTypeFromStream(stream);
	t.deepEqual(type, {
		ext: 'zip',
		mime: 'application/zip',
	});
	t.true(state.emittedBytes <= maximumZipTextEntrySizeInBytes + (3 * chunkSize));
});

test('Web Stream detection keeps stored-entry probing bounded when an oversized entry precedes ZIP mimetype detection', async t => {
	const chunkSize = 64 * 1024;
	const zip = createZipWithLeadingStoredMimetype(maximumZipTextEntrySizeInBytes + 1);
	const {state, stream} = createPatternWebStream(zip, [chunkSize]);

	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'zip',
		mime: 'application/zip',
	});
	t.true(state.emittedBytes <= maximumZipTextEntrySizeInBytes + (3 * chunkSize));
});

test('Streamed ZIP detection still detects EPUB when repeated stored entries stay below the cumulative limit', async t => {
	const zip = createZipWithRepeatedStoredMimetype(15, maximumZipTextEntrySizeInBytes);

	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(zip, 64 * 1024)), descriptorBoundaryEpubFileType);
});

test('Web Stream detection still detects EPUB when repeated stored entries stay below the cumulative limit', async t => {
	const zip = createZipWithRepeatedStoredMimetype(15, maximumZipTextEntrySizeInBytes);

	t.deepEqual(await new FileTypeParser().fromStream(createPatternWebStream(zip, [64 * 1024]).stream), descriptorBoundaryEpubFileType);
});

test('Streamed ZIP detection still detects EPUB when repeated stored entries are exactly at the cumulative limit', async t => {
	const zip = createZipWithRepeatedStoredMimetypeAtCumulativeLimit();

	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(zip, 64 * 1024)), descriptorBoundaryEpubFileType);
});

test('Web Stream detection still detects EPUB when repeated stored entries are exactly at the cumulative limit', async t => {
	const zip = createZipWithRepeatedStoredMimetypeAtCumulativeLimit();

	t.deepEqual(await new FileTypeParser().fromStream(createPatternWebStream(zip, [64 * 1024]).stream), descriptorBoundaryEpubFileType);
});

test('Streamed ZIP detection keeps repeated stored-entry probing cumulatively bounded when ZIP mimetype detection is beyond the limit', async t => {
	const chunkSize = 64 * 1024;
	const zip = createZipWithRepeatedStoredMimetype(17, maximumZipTextEntrySizeInBytes);
	const {state, stream} = createPatternWebStream(zip, [chunkSize]);

	const type = await fileTypeFromStream(stream);
	t.deepEqual(type, {
		ext: 'zip',
		mime: 'application/zip',
	});
	t.true(state.emittedBytes <= maximumUntrustedSkipSizeInBytes + (6 * chunkSize));
});

test('Web Stream detection keeps repeated stored-entry probing cumulatively bounded when ZIP mimetype detection is beyond the limit', async t => {
	const chunkSize = 64 * 1024;
	const zip = createZipWithRepeatedStoredMimetype(17, maximumZipTextEntrySizeInBytes);
	const {state, stream} = createPatternWebStream(zip, [chunkSize]);

	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'zip',
		mime: 'application/zip',
	});
	t.true(state.emittedBytes <= maximumUntrustedSkipSizeInBytes + (6 * chunkSize));
});

test('.fileTypeStream() detects ZIP mimetype when a stored entry before it is at the scan limit for chunked streams with a large sampleSize', async t => {
	const zip = createZipWithLeadingStoredMimetype(maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamChunkedResult(t, zip, descriptorBoundaryEpubFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() detects ZIP mimetype when a stored entry before it is at the scan limit for Web Streams with a large sampleSize', async t => {
	const zip = createZipWithLeadingStoredMimetype(maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamWebResult(t, zip, descriptorBoundaryEpubFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() detects ZIP mimetype when a stored entry before it is at the scan limit for chunked streams with small chunks and a large sampleSize', async t => {
	const zip = createZipWithLeadingStoredMimetype(maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamChunkedResult(t, zip, descriptorBoundaryEpubFileType, {
		chunkSize: 256,
		sampleSize: zip.length,
	});
});

test('.fileTypeStream() falls back when a stored entry before ZIP mimetype detection is at the scan limit for chunked streams with the default sampleSize', async t => {
	const zip = createZipWithLeadingStoredMimetype(maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamChunkedResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('.fileTypeStream() falls back when a stored entry before ZIP mimetype detection is at the scan limit for Web Streams with the default sampleSize', async t => {
	const zip = createZipWithLeadingStoredMimetype(maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamWebResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('.fileTypeStream() still detects ZIP mimetype when an oversized stored entry precedes it for chunked streams with a large sampleSize', async t => {
	const zip = createZipWithLeadingStoredMimetype(maximumZipTextEntrySizeInBytes + 1);

	await assertFileTypeStreamChunkedResult(t, zip, descriptorBoundaryEpubFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() still detects ZIP mimetype when an oversized stored entry precedes it for Web Streams with a large sampleSize', async t => {
	const zip = createZipWithLeadingStoredMimetype(maximumZipTextEntrySizeInBytes + 1);

	await assertFileTypeStreamWebResult(t, zip, descriptorBoundaryEpubFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() still detects ZIP mimetype when an oversized stored entry precedes it for chunked streams with small chunks and a large sampleSize', async t => {
	const zip = createZipWithLeadingStoredMimetype(maximumZipTextEntrySizeInBytes + 1);

	await assertFileTypeStreamChunkedResult(t, zip, descriptorBoundaryEpubFileType, {
		chunkSize: 256,
		sampleSize: zip.length,
	});
});

test('Known-size APIs still detect EPUB when a stored entry appears before it beyond the stream scan limit', async t => {
	const zip = createZipWithLeadingStoredMimetype(maximumZipTextEntrySizeInBytes + 1);
	const filePath = await createTemporaryTestFile(t, zip);

	t.deepEqual(await fileTypeFromBuffer(zip), descriptorBoundaryEpubFileType);
	t.deepEqual(await fileTypeFromBlob(new Blob([zip])), descriptorBoundaryEpubFileType);
	t.deepEqual(await fileTypeFromFile(filePath), descriptorBoundaryEpubFileType);
});

test('Known-size APIs still detect EPUB when a large stored entry appears before a small descriptor-backed mimetype entry', async t => {
	const zip = createZipWithLeadingStoredDescriptorMimetype(maximumZipTextEntrySizeInBytes + 1);
	const filePath = await createTemporaryTestFile(t, zip);

	t.deepEqual(await fileTypeFromBuffer(zip), descriptorBoundaryEpubFileType);
	t.deepEqual(await fileTypeFromBlob(new Blob([zip])), descriptorBoundaryEpubFileType);
	t.deepEqual(await fileTypeFromFile(filePath), descriptorBoundaryEpubFileType);
});

test('.fileTypeStream() falls back when repeated stored entries stay below the cumulative limit for chunked streams with the default sampleSize', async t => {
	const zip = createZipWithRepeatedStoredMimetype(15, maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamChunkedResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('.fileTypeStream() falls back when repeated stored entries stay below the cumulative limit for Web Streams with the default sampleSize', async t => {
	const zip = createZipWithRepeatedStoredMimetype(15, maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamWebResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('.fileTypeStream() falls back when repeated stored entries stay below the cumulative limit for chunked streams with hostile mixed chunking and the default sampleSize', async t => {
	const zip = createZipWithRepeatedStoredMimetype(15, maximumZipTextEntrySizeInBytes);
	const detectionStream = await fileTypeStream(createPatternWebStream(zip, [1, 64 * 1024]).stream);

	try {
		t.deepEqual(detectionStream.fileType, {
			ext: 'zip',
			mime: 'application/zip',
		});
		t.true(areUint8ArraysEqual(await getStreamAsUint8Array(detectionStream), zip));
	} finally {
		detectionStream.cancel();
	}
});

test('.fileTypeStream() still detects ZIP when repeated stored entries stay below the cumulative limit for Web Streams with hostile mixed chunking and the default sampleSize', async t => {
	const zip = createZipWithRepeatedStoredMimetype(15, maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamWebResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('.fileTypeStream() still detects ZIP mimetype when repeated stored entries exceed the stream cumulative limit for chunked streams with a large sampleSize', async t => {
	const zip = createZipWithRepeatedStoredMimetype(17, maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamChunkedResult(t, zip, descriptorBoundaryEpubFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() still detects ZIP mimetype when repeated stored entries exceed the stream cumulative limit for Web Streams with a large sampleSize', async t => {
	const zip = createZipWithRepeatedStoredMimetype(17, maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamWebResult(t, zip, descriptorBoundaryEpubFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() still detects EPUB when repeated stored entries exceed the stream cumulative limit for chunked streams with hostile mixed chunking and a large sampleSize', async t => {
	const zip = createZipWithRepeatedStoredMimetype(17, maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamChunkedResult(t, zip, descriptorBoundaryEpubFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() still detects EPUB when repeated stored entries exceed the stream cumulative limit for Web Streams with hostile mixed chunking and a large sampleSize', async t => {
	const zip = createZipWithRepeatedStoredMimetype(17, maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamWebResult(t, zip, descriptorBoundaryEpubFileType, {sampleSize: zip.length});
});

test('Known-size APIs still detect DOCM when a descriptor-backed entry before ZIP [Content_Types].xml detection is at the scan limit', async t => {
	const zip = createZipWithLeadingDescriptorContentTypes(maximumZipTextEntrySizeInBytes);

	t.deepEqual(await fileTypeFromBuffer(zip), descriptorBoundaryDocmFileType);
	t.deepEqual(await fileTypeFromBlob(new Blob([zip])), descriptorBoundaryDocmFileType);
	t.deepEqual(await fileTypeFromFile(await createTemporaryTestFile(t, zip)), descriptorBoundaryDocmFileType);
	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(zip, 1)), descriptorBoundaryDocmFileType);
});

test('Web Stream detection keeps ZIP [Content_Types].xml detection when a descriptor-backed entry before it is at the scan limit', async t => {
	const zip = createZipWithLeadingDescriptorContentTypes(maximumZipTextEntrySizeInBytes);

	t.deepEqual(await new FileTypeParser().fromStream(createPatternWebStream(zip, [1]).stream), descriptorBoundaryDocmFileType);
});

test('.fileTypeStream() detects ZIP [Content_Types].xml when a descriptor-backed entry before it is at the scan limit for Web Streams with a large sampleSize', async t => {
	const zip = createZipWithLeadingDescriptorContentTypes(maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamWebResult(t, zip, descriptorBoundaryDocmFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() falls back when an oversized descriptor-backed entry precedes ZIP [Content_Types].xml detection for Web Streams with a large sampleSize', async t => {
	const zip = createZipWithLeadingDescriptorContentTypes(maximumZipTextEntrySizeInBytes + 1);

	await assertFileTypeStreamWebResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	}, {sampleSize: zip.length});
});

test('.fileTypeStream() falls back when a descriptor-backed entry before ZIP [Content_Types].xml detection is at the scan limit for chunked streams with the default sampleSize', async t => {
	const zip = createZipWithLeadingDescriptorContentTypes(maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamChunkedResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('.fileTypeStream() falls back when an oversized descriptor-backed entry precedes ZIP [Content_Types].xml detection for chunked streams with the default sampleSize', async t => {
	const zip = createZipWithLeadingDescriptorContentTypes(maximumZipTextEntrySizeInBytes + 1);

	await assertFileTypeStreamChunkedResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('.fileTypeStream() detects ZIP [Content_Types].xml when a descriptor-backed entry before it is at the scan limit for chunked streams with small chunks and a large sampleSize', async t => {
	const zip = createZipWithLeadingDescriptorContentTypes(maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamChunkedResult(t, zip, descriptorBoundaryDocmFileType, {
		chunkSize: 256,
		sampleSize: zip.length,
	});
});

test('.fileTypeStream() falls back when an oversized descriptor-backed entry precedes ZIP [Content_Types].xml detection for chunked streams with small chunks and a large sampleSize', async t => {
	const zip = createZipWithLeadingDescriptorContentTypes(maximumZipTextEntrySizeInBytes + 1);

	await assertFileTypeStreamChunkedResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	}, {
		chunkSize: 256,
		sampleSize: zip.length,
	});
});

test('.fileTypeStream() detects ZIP [Content_Types].xml when a descriptor-backed entry before it is at the scan limit for chunked streams with a large sampleSize', async t => {
	const zip = createZipWithLeadingDescriptorContentTypes(maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamChunkedResult(t, zip, descriptorBoundaryDocmFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() falls back when an oversized descriptor-backed entry precedes ZIP [Content_Types].xml detection for chunked streams with a large sampleSize', async t => {
	const zip = createZipWithLeadingDescriptorContentTypes(maximumZipTextEntrySizeInBytes + 1);

	await assertFileTypeStreamChunkedResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	}, {sampleSize: zip.length});
});

test('.fileTypeStream() falls back when a descriptor-backed entry before ZIP [Content_Types].xml detection is at the scan limit for Web Streams with the default sampleSize', async t => {
	const zip = createZipWithLeadingDescriptorContentTypes(maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamWebResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('Falls back to zip when an oversized descriptor-backed entry precedes ZIP [Content_Types].xml detection', async t => {
	const zip = createZipWithLeadingDescriptorContentTypes(maximumZipTextEntrySizeInBytes + 1);

	await assertZipTypeFromBuffer(t, zip);
	await assertZipTypeFromBlob(t, zip);
	await assertZipTypeFromFile(t, zip);
	await assertZipTypeFromChunkedStream(t, zip);
});

test('Web Stream detection falls back when an oversized descriptor-backed entry precedes ZIP [Content_Types].xml detection', async t => {
	const zip = createZipWithLeadingDescriptorContentTypes(maximumZipTextEntrySizeInBytes + 1);

	await assertZipTypeFromWebStream(t, zip, [1]);
});

test('Known-size APIs fall back to zip when repeated descriptor-backed entries consume the cumulative limit before ZIP [Content_Types].xml detection', async t => {
	const zip = createZipWithRepeatedDescriptorContentTypes(15, maximumZipTextEntrySizeInBytes);

	await assertZipTypeFromKnownSizeInputs(t, zip);
});

test('Known-size APIs still detect DOCM when repeated small descriptor-backed entries stay below the known-size ZIP scan budget', async t => {
	const zip = createZipWithRepeatedDescriptorContentTypes(4, maximumZipTextEntrySizeInBytes / 8);

	t.deepEqual(await fileTypeFromBuffer(zip), descriptorBoundaryDocmFileType);
	t.deepEqual(await fileTypeFromBlob(new Blob([zip])), descriptorBoundaryDocmFileType);
	t.deepEqual(await fileTypeFromFile(await createTemporaryTestFile(t, zip)), descriptorBoundaryDocmFileType);
});

test('Known-size APIs still detect DOCM when repeated descriptor-backed entries are exactly at the known-size ZIP scan budget', async t => {
	const zip = createZipWithRepeatedDescriptorContentTypesAtKnownSizeBudget();

	t.deepEqual(await fileTypeFromBuffer(zip), descriptorBoundaryDocmFileType);
	t.deepEqual(await fileTypeFromBlob(new Blob([zip])), descriptorBoundaryDocmFileType);
	t.deepEqual(await fileTypeFromFile(await createTemporaryTestFile(t, zip)), descriptorBoundaryDocmFileType);
});

test('.fileTypeStream() still detects ZIP [Content_Types].xml when repeated small descriptor-backed entries stay below the known-size ZIP scan budget for chunked streams with a large sampleSize', async t => {
	const zip = createZipWithRepeatedDescriptorContentTypes(4, maximumZipTextEntrySizeInBytes / 8);

	await assertFileTypeStreamChunkedResult(t, zip, descriptorBoundaryDocmFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() still detects ZIP [Content_Types].xml when repeated small descriptor-backed entries stay below the known-size ZIP scan budget for Web Streams with a large sampleSize', async t => {
	const zip = createZipWithRepeatedDescriptorContentTypes(4, maximumZipTextEntrySizeInBytes / 8);

	await assertFileTypeStreamWebResult(t, zip, descriptorBoundaryDocmFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() still detects ZIP [Content_Types].xml when repeated descriptor-backed entries are exactly at the known-size ZIP scan budget for chunked streams with a large sampleSize', async t => {
	const zip = createZipWithRepeatedDescriptorContentTypesAtKnownSizeBudget();

	await assertFileTypeStreamChunkedResult(t, zip, descriptorBoundaryDocmFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() still detects ZIP [Content_Types].xml when repeated descriptor-backed entries are exactly at the known-size ZIP scan budget for Web Streams with a large sampleSize', async t => {
	const zip = createZipWithRepeatedDescriptorContentTypesAtKnownSizeBudget();

	await assertFileTypeStreamWebResult(t, zip, descriptorBoundaryDocmFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() still detects DOCM when repeated descriptor-backed ZIP [Content_Types].xml entries are exactly at the known-size ZIP scan budget for chunked streams with hostile mixed chunking and a large sampleSize', async t => {
	const zip = createZipWithRepeatedDescriptorContentTypesAtKnownSizeBudget();

	await assertFileTypeStreamChunkedResult(t, zip, descriptorBoundaryDocmFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() still detects DOCM when repeated descriptor-backed ZIP [Content_Types].xml entries are exactly at the known-size ZIP scan budget for Web Streams with hostile mixed chunking and a large sampleSize', async t => {
	const zip = createZipWithRepeatedDescriptorContentTypesAtKnownSizeBudget();

	await assertFileTypeStreamWebResult(t, zip, descriptorBoundaryDocmFileType, {sampleSize: zip.length});
});

test('Known-size APIs fall back to zip when repeated descriptor-backed entries exceed the known-size ZIP scan budget by one byte before ZIP [Content_Types].xml detection', async t => {
	const zip = createZipWithRepeatedDescriptorContentTypesAtKnownSizeBudget(1);

	await assertZipTypeFromKnownSizeInputs(t, zip);
});

test('Known-size APIs fall back to zip when repeated descriptor-backed entries exceed the cumulative limit before ZIP [Content_Types].xml detection', async t => {
	const zip = createZipWithRepeatedDescriptorContentTypes(17, maximumZipTextEntrySizeInBytes);

	await assertZipTypeFromBuffer(t, zip);
	await assertZipTypeFromBlob(t, zip);
	await assertZipTypeFromFile(t, zip);
});

test('Streamed ZIP detection still detects DOCM when a stored entry before it is at the scan limit', async t => {
	const zip = createZipWithLeadingStoredContentTypes(maximumZipTextEntrySizeInBytes);

	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(zip, 1)), descriptorBoundaryDocmFileType);
});

test('Web Stream detection still detects DOCM when a stored entry before it is at the scan limit', async t => {
	const zip = createZipWithLeadingStoredContentTypes(maximumZipTextEntrySizeInBytes);

	t.deepEqual(await new FileTypeParser().fromStream(createPatternWebStream(zip, [1]).stream), descriptorBoundaryDocmFileType);
});

test('Streamed ZIP detection keeps stored-entry probing bounded when an oversized entry precedes ZIP [Content_Types].xml detection', async t => {
	const chunkSize = 64 * 1024;
	const zip = createZipWithLeadingStoredContentTypes(maximumZipTextEntrySizeInBytes + 1);
	const {state, stream} = createPatternWebStream(zip, [chunkSize]);

	const type = await fileTypeFromStream(stream);
	t.deepEqual(type, {
		ext: 'zip',
		mime: 'application/zip',
	});
	t.true(state.emittedBytes <= maximumZipTextEntrySizeInBytes + (3 * chunkSize));
});

test('Web Stream detection keeps stored-entry probing bounded when an oversized entry precedes ZIP [Content_Types].xml detection', async t => {
	const chunkSize = 64 * 1024;
	const zip = createZipWithLeadingStoredContentTypes(maximumZipTextEntrySizeInBytes + 1);
	const {state, stream} = createPatternWebStream(zip, [chunkSize]);

	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'zip',
		mime: 'application/zip',
	});
	t.true(state.emittedBytes <= maximumZipTextEntrySizeInBytes + (3 * chunkSize));
});

test('Streamed ZIP detection still detects DOCM when repeated stored entries stay below the cumulative limit', async t => {
	const zip = createZipWithRepeatedStoredContentTypes(15, maximumZipTextEntrySizeInBytes);

	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(zip, 64 * 1024)), descriptorBoundaryDocmFileType);
});

test('Web Stream detection still detects DOCM when repeated stored entries stay below the cumulative limit', async t => {
	const zip = createZipWithRepeatedStoredContentTypes(15, maximumZipTextEntrySizeInBytes);

	t.deepEqual(await new FileTypeParser().fromStream(createPatternWebStream(zip, [64 * 1024]).stream), descriptorBoundaryDocmFileType);
});

test('Streamed ZIP detection falls back when repeated stored entries are exactly at the cumulative limit before ZIP [Content_Types].xml detection', async t => {
	const zip = createZipWithRepeatedStoredContentTypesAtCumulativeLimit();

	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(zip, 64 * 1024)), {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('Web Stream detection falls back when repeated stored entries are exactly at the cumulative limit before ZIP [Content_Types].xml detection', async t => {
	const zip = createZipWithRepeatedStoredContentTypesAtCumulativeLimit();

	t.deepEqual(await new FileTypeParser().fromStream(createPatternWebStream(zip, [64 * 1024]).stream), {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('Streamed ZIP detection keeps repeated stored-entry probing cumulatively bounded when ZIP [Content_Types].xml detection is beyond the limit', async t => {
	const chunkSize = 64 * 1024;
	const zip = createZipWithRepeatedStoredContentTypes(17, maximumZipTextEntrySizeInBytes);
	const {state, stream} = createPatternWebStream(zip, [chunkSize]);

	const type = await fileTypeFromStream(stream);
	t.deepEqual(type, {
		ext: 'zip',
		mime: 'application/zip',
	});
	t.true(state.emittedBytes <= maximumUntrustedSkipSizeInBytes + (6 * chunkSize));
});

test('Web Stream detection keeps repeated stored-entry probing cumulatively bounded when ZIP [Content_Types].xml detection is beyond the limit', async t => {
	const chunkSize = 64 * 1024;
	const zip = createZipWithRepeatedStoredContentTypes(17, maximumZipTextEntrySizeInBytes);
	const {state, stream} = createPatternWebStream(zip, [chunkSize]);

	const type = await new FileTypeParser().fromStream(stream);
	t.deepEqual(type, {
		ext: 'zip',
		mime: 'application/zip',
	});
	t.true(state.emittedBytes <= maximumUntrustedSkipSizeInBytes + (6 * chunkSize));
});

test('.fileTypeStream() detects ZIP [Content_Types].xml when a stored entry before it is at the scan limit for chunked streams with a large sampleSize', async t => {
	const zip = createZipWithLeadingStoredContentTypes(maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamChunkedResult(t, zip, descriptorBoundaryDocmFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() detects ZIP [Content_Types].xml when a stored entry before it is at the scan limit for Web Streams with a large sampleSize', async t => {
	const zip = createZipWithLeadingStoredContentTypes(maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamWebResult(t, zip, descriptorBoundaryDocmFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() detects ZIP [Content_Types].xml when a stored entry before it is at the scan limit for chunked streams with small chunks and a large sampleSize', async t => {
	const zip = createZipWithLeadingStoredContentTypes(maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamChunkedResult(t, zip, descriptorBoundaryDocmFileType, {
		chunkSize: 256,
		sampleSize: zip.length,
	});
});

test('.fileTypeStream() falls back when a stored entry before ZIP [Content_Types].xml detection is at the scan limit for chunked streams with the default sampleSize', async t => {
	const zip = createZipWithLeadingStoredContentTypes(maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamChunkedResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('.fileTypeStream() falls back when a stored entry before ZIP [Content_Types].xml detection is at the scan limit for Web Streams with the default sampleSize', async t => {
	const zip = createZipWithLeadingStoredContentTypes(maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamWebResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('.fileTypeStream() still detects ZIP [Content_Types].xml when an oversized stored entry precedes it for chunked streams with a large sampleSize', async t => {
	const zip = createZipWithLeadingStoredContentTypes(maximumZipTextEntrySizeInBytes + 1);

	await assertFileTypeStreamChunkedResult(t, zip, descriptorBoundaryDocmFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() still detects ZIP [Content_Types].xml when an oversized stored entry precedes it for Web Streams with a large sampleSize', async t => {
	const zip = createZipWithLeadingStoredContentTypes(maximumZipTextEntrySizeInBytes + 1);

	await assertFileTypeStreamWebResult(t, zip, descriptorBoundaryDocmFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() still detects ZIP [Content_Types].xml when an oversized stored entry precedes it for chunked streams with small chunks and a large sampleSize', async t => {
	const zip = createZipWithLeadingStoredContentTypes(maximumZipTextEntrySizeInBytes + 1);

	await assertFileTypeStreamChunkedResult(t, zip, descriptorBoundaryDocmFileType, {
		chunkSize: 256,
		sampleSize: zip.length,
	});
});

test('Known-size APIs still detect DOCM when a stored entry appears before it beyond the stream scan limit', async t => {
	const zip = createZipWithLeadingStoredContentTypes(maximumZipTextEntrySizeInBytes + 1);
	const filePath = await createTemporaryTestFile(t, zip);

	t.deepEqual(await fileTypeFromBuffer(zip), descriptorBoundaryDocmFileType);
	t.deepEqual(await fileTypeFromBlob(new Blob([zip])), descriptorBoundaryDocmFileType);
	t.deepEqual(await fileTypeFromFile(filePath), descriptorBoundaryDocmFileType);
});

test('Known-size APIs still detect DOCM when a large stored entry appears before a small descriptor-backed [Content_Types].xml entry', async t => {
	const zip = createZipWithLeadingStoredDescriptorContentTypes(maximumZipTextEntrySizeInBytes + 1);
	const filePath = await createTemporaryTestFile(t, zip);

	t.deepEqual(await fileTypeFromBuffer(zip), descriptorBoundaryDocmFileType);
	t.deepEqual(await fileTypeFromBlob(new Blob([zip])), descriptorBoundaryDocmFileType);
	t.deepEqual(await fileTypeFromFile(filePath), descriptorBoundaryDocmFileType);
});

test('.fileTypeStream() falls back when repeated stored ZIP [Content_Types].xml entries stay below the cumulative limit for chunked streams with the default sampleSize', async t => {
	const zip = createZipWithRepeatedStoredContentTypes(15, maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamChunkedResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('.fileTypeStream() falls back when repeated stored ZIP [Content_Types].xml entries stay below the cumulative limit for Web Streams with the default sampleSize', async t => {
	const zip = createZipWithRepeatedStoredContentTypes(15, maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamWebResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('.fileTypeStream() falls back when repeated stored ZIP [Content_Types].xml entries stay below the cumulative limit for chunked streams with hostile mixed chunking and the default sampleSize', async t => {
	const zip = createZipWithRepeatedStoredContentTypes(15, maximumZipTextEntrySizeInBytes);
	const detectionStream = await fileTypeStream(createPatternWebStream(zip, [1, 64 * 1024]).stream);

	try {
		t.deepEqual(detectionStream.fileType, {
			ext: 'zip',
			mime: 'application/zip',
		});
		t.true(areUint8ArraysEqual(await getStreamAsUint8Array(detectionStream), zip));
	} finally {
		detectionStream.cancel();
	}
});

test('.fileTypeStream() still detects ZIP when repeated stored ZIP [Content_Types].xml entries stay below the cumulative limit for Web Streams with hostile mixed chunking and the default sampleSize', async t => {
	const zip = createZipWithRepeatedStoredContentTypes(15, maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamWebResult(t, zip, {
		ext: 'zip',
		mime: 'application/zip',
	});
});

test('.fileTypeStream() still detects ZIP [Content_Types].xml when repeated stored entries exceed the stream cumulative limit for chunked streams with a large sampleSize', async t => {
	const zip = createZipWithRepeatedStoredContentTypes(17, maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamChunkedResult(t, zip, descriptorBoundaryDocmFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() still detects ZIP [Content_Types].xml when repeated stored entries exceed the stream cumulative limit for Web Streams with a large sampleSize', async t => {
	const zip = createZipWithRepeatedStoredContentTypes(17, maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamWebResult(t, zip, descriptorBoundaryDocmFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() still detects DOCM when repeated stored ZIP [Content_Types].xml entries exceed the stream cumulative limit for chunked streams with hostile mixed chunking and a large sampleSize', async t => {
	const zip = createZipWithRepeatedStoredContentTypes(17, maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamChunkedResult(t, zip, descriptorBoundaryDocmFileType, {sampleSize: zip.length});
});

test('.fileTypeStream() still detects DOCM when repeated stored ZIP [Content_Types].xml entries exceed the stream cumulative limit for Web Streams with hostile mixed chunking and a large sampleSize', async t => {
	const zip = createZipWithRepeatedStoredContentTypes(17, maximumZipTextEntrySizeInBytes);

	await assertFileTypeStreamWebResult(t, zip, descriptorBoundaryDocmFileType, {sampleSize: zip.length});
});

test('Falls back to zip on invalid ZIP descriptor signature', async t => {
	const streamedZip = createZipDataDescriptorFile({
		filename: 'mimetype',
		compressedData: new TextEncoder().encode('application/epub+zip'),
		descriptor: new Uint8Array(16),
	});

	await assertZipTypeFromBufferAndChunkedStream(t, streamedZip);
});

test('fileTypeFromFile falls back to zip on invalid ZIP descriptor signature', async t => {
	const filePath = await createTemporaryTestFile(t, createZipDataDescriptorFile({
		filename: 'mimetype',
		compressedData: new TextEncoder().encode('application/epub+zip'),
		descriptor: new Uint8Array(16),
	}));

	assertZipFileType(t, await fileTypeFromFile(filePath));
});

test('Known-size inputs fall back to zip when ZIP descriptor scanning finds a false positive', async t => {
	const zip = fs.readFileSync(path.join(__dirname, 'fixture', 'fixture.3mf')).subarray(0, 322);
	zip[250] = 28;

	await assertZipTypeFromKnownSizeInputs(t, zip);
});

test('Detects EPUB when the ZIP entry count is at the limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1024, 1023, {
		filename: 'mimetype',
		compressedData: new TextEncoder().encode('application/epub+zip'),
	});

	t.deepEqual(await fileTypeFromBuffer(zip), {
		ext: 'epub',
		mime: 'application/epub+zip',
	});
});

test('fileTypeFromFile detects EPUB when the ZIP entry count is at the limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1024, 1023, {
		filename: 'mimetype',
		compressedData: new TextEncoder().encode('application/epub+zip'),
	});
	const filePath = await createTemporaryTestFile(t, zip);

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'epub',
		mime: 'application/epub+zip',
	});
});

test('fileTypeFromBlob detects EPUB when the ZIP entry count is at the limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1024, 1023, {
		filename: 'mimetype',
		compressedData: new TextEncoder().encode('application/epub+zip'),
	});

	t.deepEqual(await fileTypeFromBlob(new Blob([zip])), {
		ext: 'epub',
		mime: 'application/epub+zip',
	});
});

test('Streamed ZIP detection still detects EPUB when the ZIP entry count is at the limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1024, 1023, {
		filename: 'mimetype',
		compressedData: new TextEncoder().encode('application/epub+zip'),
	});

	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(zip, 8)), {
		ext: 'epub',
		mime: 'application/epub+zip',
	});
});

test('Falls back to zip when the ZIP entry count exceeds the limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1025, 1024, {
		filename: 'mimetype',
		compressedData: new TextEncoder().encode('application/epub+zip'),
	});

	await assertZipTypeFromBuffer(t, zip);
});

test('fileTypeFromFile falls back to zip when the ZIP entry count exceeds the limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1025, 1024, {
		filename: 'mimetype',
		compressedData: new TextEncoder().encode('application/epub+zip'),
	});

	await assertZipTypeFromFile(t, zip);
});

test('fileTypeFromBlob falls back to zip when the ZIP entry count exceeds the limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1025, 1024, {
		filename: 'mimetype',
		compressedData: new TextEncoder().encode('application/epub+zip'),
	});

	assertZipFileType(t, await fileTypeFromBlob(new Blob([zip])));
});

test('Streamed ZIP detection falls back to zip when the entry count exceeds the limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1025, 1024, {
		filename: 'mimetype',
		compressedData: new TextEncoder().encode('application/epub+zip'),
	});

	await assertZipTypeFromChunkedStream(t, zip);
});

test('Detects DOCM when [Content_Types].xml appears at the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1024, 1023, {
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode('<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>'),
	});

	t.deepEqual(await fileTypeFromBuffer(zip), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('fileTypeFromFile detects DOCM when [Content_Types].xml appears at the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1024, 1023, {
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode('<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>'),
	});
	const filePath = await createTemporaryTestFile(t, zip);

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('fileTypeFromBlob detects DOCM when [Content_Types].xml appears at the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1024, 1023, {
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode('<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>'),
	});

	t.deepEqual(await fileTypeFromBlob(new Blob([zip])), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('Streamed ZIP detection still detects DOCM when [Content_Types].xml appears at the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1024, 1023, {
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode('<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>'),
	});

	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(zip, 8)), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('Falls back to zip when [Content_Types].xml first appears after the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1025, 1024, {
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode('<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>'),
	});

	await assertZipTypeFromBuffer(t, zip);
});

test('Still detects DOCM in over-limit ZIP archives when [Content_Types].xml appears before the entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1025, 0, {
		filename: '[Content_Types].xml',
		compressedData: new TextEncoder().encode('<?xml version="1.0" encoding="UTF-8"?><Types><Override ContentType="application/vnd.ms-word.document.macroenabled.main+xml"/></Types>'),
	});

	t.deepEqual(await fileTypeFromBuffer(zip), {
		ext: 'docm',
		mime: 'application/vnd.ms-word.document.macroenabled.12',
	});
});

test('Still detects EPUB in over-limit ZIP archives when the mimetype entry appears before the entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1025, 0, {
		filename: 'mimetype',
		compressedData: new TextEncoder().encode('application/epub+zip'),
	});

	t.deepEqual(await fileTypeFromBuffer(zip), {
		ext: 'epub',
		mime: 'application/epub+zip',
	});
});

test('Detects JAR when META-INF/MANIFEST.MF appears at the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1024, 1023, {
		filename: 'META-INF/MANIFEST.MF',
		compressedData: new TextEncoder().encode('Manifest-Version: 1.0\n'),
	});

	t.deepEqual(await fileTypeFromBuffer(zip), {
		ext: 'jar',
		mime: 'application/java-archive',
	});
});

test('fileTypeFromFile detects JAR when META-INF/MANIFEST.MF appears at the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1024, 1023, {
		filename: 'META-INF/MANIFEST.MF',
		compressedData: new TextEncoder().encode('Manifest-Version: 1.0\n'),
	});
	const filePath = await createTemporaryTestFile(t, zip);

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'jar',
		mime: 'application/java-archive',
	});
});

test('fileTypeFromBlob detects JAR when META-INF/MANIFEST.MF appears at the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1024, 1023, {
		filename: 'META-INF/MANIFEST.MF',
		compressedData: new TextEncoder().encode('Manifest-Version: 1.0\n'),
	});

	t.deepEqual(await fileTypeFromBlob(new Blob([zip])), {
		ext: 'jar',
		mime: 'application/java-archive',
	});
});

test('Streamed ZIP detection still detects JAR when META-INF/MANIFEST.MF appears at the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1024, 1023, {
		filename: 'META-INF/MANIFEST.MF',
		compressedData: new TextEncoder().encode('Manifest-Version: 1.0\n'),
	});

	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(zip, 8)), {
		ext: 'jar',
		mime: 'application/java-archive',
	});
});

test('Still detects JAR in over-limit ZIP archives when META-INF/MANIFEST.MF appears before the entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1025, 0, {
		filename: 'META-INF/MANIFEST.MF',
		compressedData: new TextEncoder().encode('Manifest-Version: 1.0\n'),
	});

	t.deepEqual(await fileTypeFromBuffer(zip), {
		ext: 'jar',
		mime: 'application/java-archive',
	});
});

test('Falls back to zip when META-INF/MANIFEST.MF first appears after the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1025, 1024, {
		filename: 'META-INF/MANIFEST.MF',
		compressedData: new TextEncoder().encode('Manifest-Version: 1.0\n'),
	});

	await assertZipTypeFromBuffer(t, zip);
});

test('fileTypeFromFile falls back to zip when META-INF/MANIFEST.MF first appears after the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1025, 1024, {
		filename: 'META-INF/MANIFEST.MF',
		compressedData: new TextEncoder().encode('Manifest-Version: 1.0\n'),
	});

	await assertZipTypeFromFile(t, zip);
});

test('fileTypeFromBlob falls back to zip when META-INF/MANIFEST.MF first appears after the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1025, 1024, {
		filename: 'META-INF/MANIFEST.MF',
		compressedData: new TextEncoder().encode('Manifest-Version: 1.0\n'),
	});

	assertZipFileType(t, await fileTypeFromBlob(new Blob([zip])));
});

test('Streamed ZIP detection falls back to zip when META-INF/MANIFEST.MF first appears after the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1025, 1024, {
		filename: 'META-INF/MANIFEST.MF',
		compressedData: new TextEncoder().encode('Manifest-Version: 1.0\n'),
	});

	await assertZipTypeFromChunkedStream(t, zip);
});

test('Detects XPI when META-INF/mozilla.rsa appears at the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1024, 1023, {
		filename: 'META-INF/mozilla.rsa',
		compressedData: new Uint8Array(0),
	});

	t.deepEqual(await fileTypeFromBuffer(zip), {
		ext: 'xpi',
		mime: 'application/x-xpinstall',
	});
});

test('fileTypeFromFile detects XPI when META-INF/mozilla.rsa appears at the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1024, 1023, {
		filename: 'META-INF/mozilla.rsa',
		compressedData: new Uint8Array(0),
	});
	const filePath = await createTemporaryTestFile(t, zip);

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'xpi',
		mime: 'application/x-xpinstall',
	});
});

test('fileTypeFromBlob detects XPI when META-INF/mozilla.rsa appears at the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1024, 1023, {
		filename: 'META-INF/mozilla.rsa',
		compressedData: new Uint8Array(0),
	});

	t.deepEqual(await fileTypeFromBlob(new Blob([zip])), {
		ext: 'xpi',
		mime: 'application/x-xpinstall',
	});
});

test('Streamed ZIP detection still detects XPI when META-INF/mozilla.rsa appears at the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1024, 1023, {
		filename: 'META-INF/mozilla.rsa',
		compressedData: new Uint8Array(0),
	});

	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(zip, 8)), {
		ext: 'xpi',
		mime: 'application/x-xpinstall',
	});
});

test('Still detects XPI in over-limit ZIP archives when META-INF/mozilla.rsa appears before the entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1025, 0, {
		filename: 'META-INF/mozilla.rsa',
		compressedData: new Uint8Array(0),
	});

	t.deepEqual(await fileTypeFromBuffer(zip), {
		ext: 'xpi',
		mime: 'application/x-xpinstall',
	});
});

test('Falls back to zip when META-INF/mozilla.rsa first appears after the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1025, 1024, {
		filename: 'META-INF/mozilla.rsa',
		compressedData: new Uint8Array(0),
	});

	await assertZipTypeFromBuffer(t, zip);
});

test('fileTypeFromFile falls back to zip when META-INF/mozilla.rsa first appears after the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1025, 1024, {
		filename: 'META-INF/mozilla.rsa',
		compressedData: new Uint8Array(0),
	});

	await assertZipTypeFromFile(t, zip);
});

test('fileTypeFromBlob falls back to zip when META-INF/mozilla.rsa first appears after the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1025, 1024, {
		filename: 'META-INF/mozilla.rsa',
		compressedData: new Uint8Array(0),
	});

	assertZipFileType(t, await fileTypeFromBlob(new Blob([zip])));
});

test('Streamed ZIP detection falls back to zip when META-INF/mozilla.rsa first appears after the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1025, 1024, {
		filename: 'META-INF/mozilla.rsa',
		compressedData: new Uint8Array(0),
	});

	await assertZipTypeFromChunkedStream(t, zip);
});

test('Detects APK when classes.dex appears at the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1024, 1023, {
		filename: 'classes.dex',
		compressedData: new TextEncoder().encode('dex\n035\0'),
	});

	t.deepEqual(await fileTypeFromBuffer(zip), {
		ext: 'apk',
		mime: 'application/vnd.android.package-archive',
	});
});

test('fileTypeFromFile detects APK when classes.dex appears at the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1024, 1023, {
		filename: 'classes.dex',
		compressedData: new TextEncoder().encode('dex\n035\0'),
	});
	const filePath = await createTemporaryTestFile(t, zip);

	t.deepEqual(await fileTypeFromFile(filePath), {
		ext: 'apk',
		mime: 'application/vnd.android.package-archive',
	});
});

test('fileTypeFromBlob detects APK when classes.dex appears at the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1024, 1023, {
		filename: 'classes.dex',
		compressedData: new TextEncoder().encode('dex\n035\0'),
	});

	t.deepEqual(await fileTypeFromBlob(new Blob([zip])), {
		ext: 'apk',
		mime: 'application/vnd.android.package-archive',
	});
});

test('Streamed ZIP detection still detects APK when classes.dex appears at the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1024, 1023, {
		filename: 'classes.dex',
		compressedData: new TextEncoder().encode('dex\n035\0'),
	});

	t.deepEqual(await fileTypeFromStream(createBufferedWebStream(zip, 8)), {
		ext: 'apk',
		mime: 'application/vnd.android.package-archive',
	});
});

test('Still detects APK in over-limit ZIP archives when classes.dex appears before the entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1025, 0, {
		filename: 'classes.dex',
		compressedData: new TextEncoder().encode('dex\n035\0'),
	});

	t.deepEqual(await fileTypeFromBuffer(zip), {
		ext: 'apk',
		mime: 'application/vnd.android.package-archive',
	});
});

test('Falls back to zip when classes.dex first appears after the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1025, 1024, {
		filename: 'classes.dex',
		compressedData: new TextEncoder().encode('dex\n035\0'),
	});

	await assertZipTypeFromBuffer(t, zip);
});

test('fileTypeFromFile falls back to zip when classes.dex first appears after the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1025, 1024, {
		filename: 'classes.dex',
		compressedData: new TextEncoder().encode('dex\n035\0'),
	});

	await assertZipTypeFromFile(t, zip);
});

test('fileTypeFromBlob falls back to zip when classes.dex first appears after the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1025, 1024, {
		filename: 'classes.dex',
		compressedData: new TextEncoder().encode('dex\n035\0'),
	});

	assertZipFileType(t, await fileTypeFromBlob(new Blob([zip])));
});

test('Streamed ZIP detection falls back to zip when classes.dex first appears after the ZIP entry count limit', async t => {
	const zip = createZipArchiveWithEntryAtIndex(1025, 1024, {
		filename: 'classes.dex',
		compressedData: new TextEncoder().encode('dex\n035\0'),
	});

	await assertZipTypeFromChunkedStream(t, zip);
});

test('.fileTypeStream() clamps invalid sampleSize values', async t => {
	const file = path.join(__dirname, 'fixture', 'fixture.png');
	const blob = new Blob([await readFile(file)]);
	const stream = await fileTypeStream(blob.stream(), {sampleSize: Number.POSITIVE_INFINITY});
	t.deepEqual(stream.fileType, {
		ext: 'png',
		mime: 'image/png',
	});
});

test('Does not allocate huge memory on malformed EBML DocType length', async t => {
	const bytes = Uint8Array.from([0x1A, 0x45, 0xDF, 0xA3, 0x81, 0x42, 0x82, 0x01, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]);
	const type = await fileTypeFromBuffer(bytes);

	t.is(type, undefined);
});

test('Does not throw on malformed EBML stream child with oversized payload length', async t => {
	const bytes = Uint8Array.from([0x1A, 0x45, 0xDF, 0xA3, 0x8A, 0x42, 0x83, 0x01, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]);
	const type = await fileTypeFromStream(createBufferedWebStream(bytes, 8));

	t.is(type, undefined);
});
```

## File: `type.js`
```javascript
#!/usr/bin/node
import process from 'node:process';
import {fileTypeFromFile} from './source/index.js';

const [file] = process.argv.slice(2);

if (!file) {
	console.error('Expected path of the file to examine');
	process.exit();
}

const fileType = await fileTypeFromFile(file);

if (fileType) {
	console.log(`MIME-type: ${fileType.mime}`);
	console.log(`Extension: ${fileType.ext}`);
} else {
	console.log('Could not determine file type');
}
```

## File: `fixture/.gitattributes`
```
fixture-win2000.reg binary
fixture-win95.reg text eol=crlf
```

## File: `fixture/fixture-ascii.cpio`
```
0707070000475347511006440017500017500000010000001441141455100000600000000006small small
0707070000000000000000000000000000000000010000000000000000000001300000000000TRAILER!!!                                                                                                                                                                                                                                                                                                                                                  
```

## File: `fixture/fixture-minimal.pdf`
```
%PDF-1.1
%¥±ë

1 0 obj
  << /Type /Catalog
     /Pages 2 0 R
  >>
endobj

2 0 obj
  << /Type /Pages
     /Kids [3 0 R]
     /Count 1
     /MediaBox [0 0 300 144]
  >>
endobj

3 0 obj
  <<  /Type /Page
      /Parent 2 0 R
      /Resources
       << /Font
           << /F1
               << /Type /Font
                  /Subtype /Type1
                  /BaseFont /Times-Roman
               >>
           >>
       >>
      /Contents 4 0 R
  >>
endobj

4 0 obj
  << /Length 55 >>
stream
  BT
    /F1 18 Tf
    0 0 Td
    (Hello World) Tj
  ET
endstream
endobj

xref
0 5
0000000000 65535 f 
0000000018 00000 n 
0000000077 00000 n 
0000000178 00000 n 
0000000457 00000 n 
trailer
  <<  /Root 1 0 R
      /Size 5
  >>
startxref
565
%%EOF
```

## File: `fixture/fixture-utf8-bom.xml`
```xml
﻿<?xml version="1.0" encoding="UTF-16"?>
<FileType>
	<encoding>UTF-8 with BOM</encoding>
</FileType>
```

## File: `fixture/fixture-vtt-eof.vtt`
```
WEBVTT
```

## File: `fixture/fixture-vtt-linebreak.vtt`
```
WEBVTT

00:11.000 --> 00:13.000
<v Speaker Name>Test WEBVTT prefix followed by a line break
```

## File: `fixture/fixture-vtt-space.vtt`
```
WEBVTT 00:11.000 --> 00:13.000
<v Speaker Name>Test WEBVTT prefix followed by a space
```

## File: `fixture/fixture-vtt-tab.vtt`
```
WEBVTT	00:11.000 --> 00:13.000
<v Speaker Name>Test WEBVTT prefix followed by a tab
```

## File: `fixture/fixture-win95.reg`
```
REGEDIT4

[HKEY_CURRENT_USER\Software\Test]
"TestVal"="Succeeded"
```

## File: `fixture/fixture.3g2`
```
   ftyp3g2a
```

## File: `fixture/fixture.asar`
```
   <   8   1   {"files":{"sample.txt":{"size":11,"offset":"0"}}}   helloworld
```

## File: `fixture/fixture.f4a`
```
   ftypF4A 
```

## File: `fixture/fixture.f4b`
```
   ftypF4B 
```

## File: `fixture/fixture.f4p`
```
   ftypF4P 
```

## File: `fixture/fixture.f4v`
```
   ftypF4V 
```

## File: `fixture/fixture.ics`
```
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//hacksw/handcal//NONSGML v1.0//EN
BEGIN:VEVENT
UID:19970610T172345Z-AF23B2@example.com
DTSTAMP:19970610T172345Z
DTSTART:19970714T170000Z
DTEND:19970715T040000Z
SUMMARY:Bastille Day Party
END:VEVENT
END:VCALENDAR
```

## File: `fixture/fixture.key`
```
PK                        Index/Document.iwaPK                        Index/MasterSlide.iwa
```

## File: `fixture/fixture.m4b`
```
   ftypM4B 
```

## File: `fixture/fixture.m4p`
```
   ftypM4P 
```

## File: `fixture/fixture.numbers`
```
PK                        Index/Document.iwaPK                        Index/Tables/Table-1.iwa
```

## File: `fixture/fixture.pages`
```
PK                        Index/Document.iwaPK                        Index/CalculationEngine.iwa
```

## File: `fixture/fixture.pgp`
```
-----BEGIN PGP MESSAGE-----
Version: OpenPGP.js v3.0.9
Comment: https://openpgpjs.org

wcBMA5C5XtMJioU5AQf/VlCbKDYaUD2UaAVVM4jJqktfYkNjxfGAzzJps+0e
mfkkG4Ax5GJWHC0q5I3PKXlqSESpqooARa5bYZ1wt5iqEYPbUkt1csbsnXlZ
X1EHwZb9YYmQBEJSjOyA49jwpeetaEt//VvIlFPHp4a7QnYePSa3gH1DsKkM
NG/cZjZoh/ik5yAPD56w1/Ym+RP0y11lwpWxbpfq0iyu5RbUekD9cgXAnCvP
G29Sqt8H3C299v2dbp3utRSf+bS/ERra6XVipWjjxfkD2tgrruFIERSAGQX1
FPvS6ztH0301hUEXeA7cA4OuGK5sgbBeiRoSHE/DdbTeLiRIxbW01rqIXxzz
ItJRAby+866YRBJnl/vvauszUFNz9JpV2ZS5c+weELrkPBlUuaV0CieLkwIn
T318njOQ+cnW1cpxWPaiK/qSCBaIc6sOiVhLL4wRePu2FRe47mC4
=Gp87
-----END PGP MESSAGE-----
```

## File: `fixture/fixture.ps`
```
%!PS

/Courier             % name the desired font
20 selectfont        % choose the size in points and establish
                     % the font as the current one
72 500 moveto        % position the current point at
                     % coordinates 72, 500 (the origin is at the
                     % lower-left corner of the page)
(Hello world!) show  % stroke the text in parentheses
showpage             % print all on the page
```

## File: `fixture/fixture.rtf`
```
{\rtf1\ansi\ansicpg1252\cocoartf1265\cocoasubrtf210
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural

\f0\fs24 \cf0 Test RTF file}
```

## File: `fixture/fixture.stl`
```
solid SQUARE
  facet normal  0.0   0.0  1.0    
    outer loop
      vertex    1.0   0.0   0.0    
      vertex    0.5   0.5   0.0    
      vertex    0.0   0.0   0.0    
    endloop
  endfacet
  facet normal  0.0   0.0  1.0    
    outer loop
      vertex    0.0   0.0   0.0 
      vertex    0.5   0.5   0.0    
      vertex    0.0   1.0   0.0    
    endloop
  endfacet
  facet normal  0.0   0.0   1.0    
    outer loop
      vertex    1.0   0.0   0.0
      vertex    1.0   1.0   0.0
      vertex    0.0   1.0   0.0
    endloop
  endfacet
endsolid SQUARE
```

## File: `fixture/fixture.ttc`
```
ttcf 
```

## File: `fixture/fixture.unicorn`
```
UNICORN FILE CONTENT
```

## File: `fixture/fixture.vcf`
```
BEGIN:VCARD
VERSION:3.0
N:Gump;Forrest;;Mr.,;
FN:Forrest Gump
ORG:Bubba Gump Shrimp Co.
TITLE:Shrimp Man
PHOTO;VALUE=URI;TYPE=GIF:http://www.example.com/dir_photos/my_photo.gif
TEL;TYPE=WORK,VOICE:(111) 555-1212
TEL;TYPE=HOME,VOICE:(404) 555-1212
ADR;TYPE=WORK,PREF:;;100 Waters Edge;Baytown;LA;30314;United States of America
LABEL;TYPE=WORK,PREF:100 Waters Edge\nBaytown\, LA 30314\nUnited States of America
ADR;TYPE=HOME:;;42 Plantation St.;Baytown;LA;30314;United States of America
LABEL;TYPE=HOME:42 Plantation St.\nBaytown\, LA 30314\nUnited States of America
EMAIL:forrestgump@example.com
REV:2008-04-24T19:52:43Z
END:VCARD
```

## File: `fixture/fixture.voc`
```
Creative Voice File 
)
```

## File: `fixture/fixture.wasm`
```
 asm
   ` 
addTwo  
	    j
```

## File: `fixture/fixture.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<doc>

</doc>
```

## File: `fixture/fixture2.eps`
```
%!PS-Adobe-2.0 EPSF-1.2
%%Creator: Adobe Illustrator 88(TM) 1.6
%%For: (Timothy A. Tedder) ()
%%Title: (earth)
%%CreationDate: (10/19/88) (2:29 PM)
%%DocumentProcSets: Adobe_packedarray 0 0
%%DocumentSuppliedProcSets: Adobe_packedarray 0 0
%%DocumentProcSets: Adobe_cmykcolor 0 0
%%DocumentSuppliedProcSets: Adobe_cmykcolor 0 0
%%DocumentProcSets: Adobe_cshow 0 0
%%DocumentSuppliedProcSets: Adobe_cshow 0 0
%%DocumentProcSets: Adobe_customcolor 0 0
%%DocumentSuppliedProcSets: Adobe_customcolor 0 0
%%DocumentProcSets: Adobe_Illustrator_881 0 0
%%DocumentSuppliedProcSets: Adobe_Illustrator_881 0 0
%%ColorUsage: Black&White
%%DocumentProcessColors: Black
%%BoundingBox:119 246 394 521
%%TemplateBox:288 360 288 360
%%TileBox:-552 730 0 1460
%%EndComments
%%BeginProcSet: Adobe_packedarray 0 0
% packedarray Operators
% Version 1.0 5/9/1988
% Copyright (C) 1987, 1988
% Adobe Systems Incorporated
% All Rights Reserved
userdict /Adobe_packedarray 5 dict dup begin put
/initialize			% - initialize -
{
/packedarray where
	{
	pop
	}
	{
	Adobe_packedarray begin
	Adobe_packedarray
		{
		dup xcheck
			{
			bind
			} if
		userdict 3 1 roll put
		} forall
	end
	} ifelse
} def
/terminate			% - terminate -
{
} def
/packedarray		% arguments count packedarray array
{
array astore readonly
} def
/setpacking			% boolean setpacking -
{
pop
} def
/currentpacking		% - setpacking boolean
{
false
} def
currentdict readonly pop end
%%EndProcSet
Adobe_packedarray /initialize get exec
%%BeginProcSet:Adobe_cmykcolor 0 0
% cmykcolor Operators
% Version 1.0 5/9/1988
% Copyright (C) 1987, 1988
% Adobe Systems Incorporated
% All Rights Reserved
currentpacking true setpacking
userdict /Adobe_cmykcolor 4 dict dup begin put
/initialize			% - initialize -
{
/setcmykcolor where
	{
	pop
	}
	{
	userdict /Adobe_cmykcolor_vars 2 dict dup begin put
	/_setrgbcolor
		/setrgbcolor load def
	/_currentrgbcolor
		/currentrgbcolor load def
	Adobe_cmykcolor begin
	Adobe_cmykcolor
		{
		dup xcheck
			{
			bind
			} if
		pop pop
		} forall
	end
	end
	Adobe_cmykcolor begin
	} ifelse
} def
/terminate			% - terminate -
{
currentdict Adobe_cmykcolor eq
	{
	end
	} if
} def
/setcmykcolor		% cyan magenta yellow black setcmykcolor -
{
1 sub 4 1 roll
3
	{
	3 index add neg dup 0 lt
		{
		pop 0
		} if
	3 1 roll
	} repeat
Adobe_cmykcolor_vars /_setrgbcolor get exec
pop
} def 
/currentcmykcolor	% - currentcmykcolor cyan magenta yellow black
{
Adobe_cmykcolor_vars /_currentrgbcolor get exec
3
	{
	1 sub neg 3 1 roll
	} repeat
0
} def
currentdict readonly pop end
setpacking
%%EndProcSet
%%BeginProcSet: Adobe_cshow 0 0
% cshow Operator
% Version 1.0 5/9/1988
% Copyright (C) 1987, 1988
% Adobe Systems Incorporated
% All Rights Reserved
currentpacking true setpacking
userdict /Adobe_cshow 3 dict dup begin put
/initialize			% - initialize -
{
/cshow where
	{
	pop
	}
	{
	userdict /Adobe_cshow_vars 1 dict dup begin put
	/_cshow		% - _cshow proc
		{} def
	Adobe_cshow begin
	Adobe_cshow
		{
		dup xcheck
			{
			bind
			} if
		userdict 3 1 roll put
		} forall
	end
	end
	} ifelse
} def
/terminate			% - terminate -
{
} def
/cshow				% string proc cshow -
{
Adobe_cshow_vars
	exch /_cshow
	exch put
	{
	0 0 Adobe_cshow_vars /_cshow get exec
	} forall
} def
currentdict readonly pop end
setpacking
%%EndProcSet
%%BeginProcSet: Adobe_customcolor 0 0
% Custom Color Operators
% Version 1.0 5/9/1988
% Copyright (C) 1987, 1988
% Adobe Systems Incorporated
% All Rights Reserved
currentpacking true setpacking
userdict /Adobe_customcolor 5 dict dup begin put
/initialize			% - initialize -
{
/setcustomcolor where
	{
	pop
	}
	{
	Adobe_customcolor begin
	Adobe_customcolor
		{
		dup xcheck
			{
			bind
			} if
		pop pop
		} forall
	end
	Adobe_customcolor begin
	} ifelse
} def
/terminate			% - terminate -
{
currentdict Adobe_customcolor eq
	{
	end
	} if
} def
/findcmykcustomcolor	% cyan magenta yellow black name findcmykcustomcolor object
{
5 packedarray
}  def
/setcustomcolor		% object tint setcustomcolor -
{
exch
aload pop pop
4
	{
	4 index mul 4 1 roll
	} repeat
5 -1 roll pop
setcmykcolor
} def
/setoverprint		% boolean setoverprint -
{
pop
} def
currentdict readonly pop end
setpacking
%%EndProcSet
%%BeginProcSet: Adobe_Illustrator881 0 0
% Adobe Illustrator (TM) Prolog
% Version 1.0 5/9/1988
% Copyright (C) 1987, 1988
% Adobe Systems Incorporated
% All Rights Reserved
currentpacking true setpacking
userdict /Adobe_Illustrator881 72 dict dup begin put
% initialization
/initialize				% - initialize -
{
userdict /Adobe_Illustrator881_vars 29 dict dup begin put
% paint operands
/_lp /none def
/_pf {} def
/_ps {} def
/_psf {} def
/_pss {} def
% text operands
/_a null def
/_as null def
/_tt 2 array def
/_tl 2 array def
/_tm matrix def
/t {} def
% color operands
/_gf null def
/_cf 4 array def
/_if null def
/_of false def
/_fc {} def
/_gs null def
/_cs 4 array def
/_is null def
/_os false def
/_sc {} def
/_i null def
Adobe_Illustrator881 begin
Adobe_Illustrator881
	{
	dup xcheck
		{
		bind
		} if
	pop pop
	} forall
end
end
Adobe_Illustrator881 begin
Adobe_Illustrator881_vars begin
newpath
} def
/terminate				% - terminate -
{
end
end
} def
% definition operators
/_					% - _ null
null def
/ddef				% key value ddef -
{
Adobe_Illustrator881_vars 3 1 roll put
} def
/xput				% key value literal xput -
{
dup load dup length exch maxlength eq
	{
	dup dup load dup
	length 2 mul dict copy def
	} if
load begin def end
} def
/npop				% integer npop -
{
	{
	pop
	} repeat
} def
% marking operators
/sw					% ax ay length string sw x y
{
stringwidth
exch 5 -1 roll 3 index 1 sub mul add
4 1 roll 3 1 roll 1 sub mul add
} def
/ss					% ax ay length string matrix ss -
{
3 -1 roll pop
4 1 roll
	{
	2 npop (0) exch
	2 copy 0 exch put pop
	gsave
	false charpath
	currentpoint
	4 index setmatrix
	stroke
	grestore
	moveto
	2 copy rmoveto
	} cshow
3 npop
} def
% path operators
/sp					% ax ay length string sp -
{
exch pop
	{
	2 npop (0) exch
	2 copy 0 exch put pop
	false charpath
	2 copy rmoveto
	} cshow
2 npop
} def
% path construction operators
/pl					% x y pl x y
{
transform
0.25 sub round 0.25 add exch
0.25 sub round 0.25 add exch
itransform
} def
/setstrokeadjust where
{
pop true setstrokeadjust
/c				% x1 y1 x2 y2 x3 y3 c -
{
curveto
} def
/C
/c load def
/v				% x2 y2 x3 y3 v -
{
currentpoint 6 2 roll curveto
} def
/V
/v load def
/y				% x1 y1 x2 y2 y -
{
2 copy curveto
} def
/Y
/y load def
/l				% x y l -
{
lineto
} def
/L
/l load def
/m				% x y m -
{
moveto
} def
}
{
/c
{
pl curveto
} def
/C
/c load def
/v
{
currentpoint 6 2 roll pl curveto
} def
/V
/v load def
/y
{
pl 2 copy curveto
} def
/Y
/y load def
/l
{
pl lineto
} def
/L
/l load def
/m
{
pl moveto
} def
} ifelse
% graphic state operators
/d					% array phase d -
{
setdash
} def
/cf					% - cf flatness
currentflat def
/i					% flatness i -
{
dup 0 eq
	{
	pop cf
	} if
setflat
} def
/j					% linejoin j -
{
setlinejoin
} def
/J					% linecap J -
{
setlinecap
} def
/M					% miterlimit M -
{
setmiterlimit
} def
/w					% linewidth w -
{
setlinewidth
} def
% path painting operators
/H					% - H -
{} def
/h					% - h -
{
closepath
} def
/N					% - N -
{
newpath
} def
/n					% - n -
/N load def
/F					% - F -
{
_pf
} def
/f					% - f -
{
closepath
F
} def
/S					% - S -
{
_ps
} def
/s					% - s -
{
closepath
S
} def
/B					% - B -
{
gsave F grestore
S
} def
/b					% - b -
{
closepath
B
} def
/W					% - W -
{
clip
} def
% text painting operators
/ta					% length string ta ax ay length string
{
_as moveto
_tt aload pop 4 -2 roll
} def
/tl					% - tl -
{
_tl aload pop translate
} def
/as					% - as array
{
{
0 0
}
{
2 copy _tt aload pop 4 -2 roll sw
exch neg 2 div exch neg 2 div
}
{
2 copy _tt aload pop 4 -2 roll sw
exch neg exch neg
}
{
0 0
}
} cvlit def
/z					% literal size leading tracking align z -
{
/_a exch ddef
/_as as _a get ddef
_a 2 le
	{
	0 _tt astore pop
	0 exch neg _tl astore pop
	}
	{
	0 exch neg _tt astore pop
	neg 0 _tl astore pop
	} ifelse
exch findfont exch scalefont setfont
} def
/tm					% matrix tm -
{
_tm currentmatrix pop
concat
} def
/I					% matrix I -
{
tm
/t
	{
	ta sp
	tl
	} ddef
} def
/o					% matrix o -
{
tm
/t
	{
	ta 4 npop
	tl
	newpath
	} ddef
} def
/e					% matrix e -
{
tm
/t
	{
	ta _psf
	tl
	newpath
	} ddef
} def
/r					% matrix r -
{
tm
/t
	{
	ta _tm _pss
	tl
	newpath
	} ddef
} def
/a					% matrix a -
{
tm
/t
	{
	2 copy
	ta _psf
	newpath
	ta _tm _pss
	tl
	newpath
	} ddef
} def
/T					% - T -
{
_tm setmatrix
} def
% font operators
/Z					% array literal literal direction Z -
{
pop
findfont begin
currentdict dup length 1 add dict begin
	{
	1 index /FID ne
		{
		def
		}
		{
		2 npop
		} ifelse
	} forall
/FontName exch def dup length 0 ne
	{
	/Encoding Encoding 256 array copy def
	0 exch
		{
		dup type /nametype eq
			{
			Encoding 2 index 2 index put pop
			1 add
			}
			{
			exch pop
			} ifelse
		} forall
	} if pop
currentdict dup end end
/FontName get exch definefont pop
} def
% group operators
/u					% - u -
{} def
/U					% - U -
{} def
/q					% - q -
{
gsave
} def
/Q					% - Q -
{
grestore
} def
% place operators
/`					% matrix llx lly urx ury string ` -
{
/_i save ddef
6 1 roll 4 npop
concat
userdict begin
/showpage {} def
false setoverprint
pop
} def
/~					% - ~ -
{
end
_i restore
} def
% color operators
/O					% flag O -
{
0 ne
/_of exch ddef
/_lp /none ddef
} def
/R					% flag R -
{
0 ne
/_os exch ddef
/_lp /none ddef
} def
/g					% gray g -
{
/_gf exch ddef
/_fc
{
_lp /fill ne
	{
	_of setoverprint
	_gf setgray
	/_lp /fill ddef
	} if
} ddef
/_pf
{
_fc
fill
} ddef
/_psf
{
_fc
exch pop
ashow
} ddef
/_lp /none ddef
} def
/G					% gray G -
{
/_gs exch ddef
/_sc
{
_lp /stroke ne
	{
	_os setoverprint
	_gs setgray
	/_lp /stroke ddef
	} if
} ddef
/_ps
{
_sc
stroke
} ddef
/_pss
{
_sc
ss
} ddef
/_lp /none ddef
} def
/k					% cyan magenta yellow black k -
{
_cf astore pop
/_fc
{
_lp /fill ne
	{
	_of setoverprint
	_cf aload pop setcmykcolor
	/_lp /fill ddef
	} if
} ddef
/_pf
{
_fc
fill
} ddef
/_psf
{
_fc
exch pop
ashow
} ddef
/_lp /none ddef
} def
/K					% cyan magenta yellow black K -
{
_cs astore pop
/_sc
{
_lp /stroke ne
	{
	_os setoverprint
	_cs aload pop setcmykcolor
	/_lp /stroke ddef
	} if
} ddef
/_ps
{
_sc
stroke
} ddef
/_pss
{
_sc
ss
} ddef
/_lp /none ddef
} def
/x					% cyan magenta yellow black name gray x -
{
/_gf exch ddef
findcmykcustomcolor
/_if exch ddef
/_fc
{
_lp /fill ne
	{
	_of setoverprint
	_if _gf 1 exch sub setcustomcolor
	/_lp /fill ddef
	} if
} ddef
/_pf
{
_fc
fill
} ddef
/_psf
{
_fc
exch pop
ashow
} ddef
/_lp /none ddef
} def
/X					% cyan magenta yellow black name gray X -
{
/_gs exch ddef
findcmykcustomcolor
/_is exch ddef
/_sc
{
_lp /stroke ne
	{
	_os setoverprint
	_is _gs 1 exch sub setcustomcolor
	/_lp /stroke ddef
	} if
} ddef
/_ps
{
_sc
stroke
} ddef
/_pss
{
_sc
ss
} ddef
/_lp /none ddef
} def
% locked object operators
/A					% value A -
{
pop
} def
currentdict readonly pop end
setpacking
%%EndProcSet
%%EndProlog
%%BeginSetup

Adobe_cmykcolor /initialize get exec
Adobe_cshow /initialize get exec
Adobe_customcolor /initialize get exec
Adobe_Illustrator881 /initialize get exec
%%EndSetup
0 A
u
q
0 O
0 g
0 R
0 G
0 i 0 J 0 j 1 w 4 M []0 d
%%Note:
289.7483 499.934 m
323.3996 489.1332 350.8221 464.5488 364.8541 432.0545 c
390.3671 372.9737 360.4601 299.753 300.8926 274.7434 c
241.5687 249.836 167.9347 279.1117 143.7827 339.0235 c
134.3854 362.3347 131.6141 386.862 137.3373 411.8925 c
145.5155 447.6591 157.8251 467.6706 191.9297 487.7602 c
222.0044 505.476 256.5007 510.6053 289.7483 499.934 c
h
W
n
0.2 g
120.6329 385.5208 m
120.6329 459.3289 180.4681 519.164 254.2761 519.164 c
328.0841 519.164 387.9193 459.3289 387.9193 385.5208 c
387.9193 311.7128 328.0841 251.8777 254.2761 251.8777 c
180.4681 251.8777 120.6329 311.7128 120.6329 385.5208 c
f
u
0.2227 g
132.0236 388.6477 m
132.0236 457.0886 187.5077 512.5727 255.9486 512.5727 c
324.3895 512.5727 379.8736 457.0886 379.8736 388.6477 c
379.8736 320.2068 324.3895 264.7227 255.9486 264.7227 c
187.5077 264.7227 132.0236 320.2068 132.0236 388.6477 c
f
0.2454 g
143.4163 391.7751 m
143.4163 454.8479 194.5486 505.9802 257.6214 505.9802 c
320.6943 505.9802 371.8265 454.8479 371.8265 391.7751 c
371.8265 328.7022 320.6943 277.5699 257.6214 277.5699 c
194.5486 277.5699 143.4163 328.7022 143.4163 391.7751 c
f
0.2682 g
154.8089 394.9025 m
154.8089 452.6072 201.5894 499.3878 259.2942 499.3878 c
316.999 499.3878 363.7795 452.6072 363.7795 394.9025 c
363.7795 337.1977 316.999 290.4172 259.2942 290.4172 c
201.5894 290.4172 154.8089 337.1977 154.8089 394.9025 c
f
0.2909 g
166.2015 398.0298 m
166.2015 450.3666 208.6302 492.7953 260.967 492.7953 c
313.3037 492.7953 355.7324 450.3666 355.7324 398.0298 c
355.7324 345.6931 313.3037 303.2644 260.967 303.2644 c
208.6302 303.2644 166.2015 345.6931 166.2015 398.0298 c
f
0.3136 g
177.5941 401.1572 m
177.5941 448.1259 215.671 486.2028 262.6398 486.2028 c
309.6085 486.2028 347.6854 448.1259 347.6854 401.1572 c
347.6854 354.1885 309.6085 316.1116 262.6398 316.1116 c
215.671 316.1116 177.5941 354.1885 177.5941 401.1572 c
f
0.3364 g
188.9868 404.2846 m
188.9868 445.8853 222.7119 479.6104 264.3125 479.6104 c
305.9132 479.6104 339.6383 445.8853 339.6383 404.2846 c
339.6383 362.6839 305.9132 328.9588 264.3125 328.9588 c
222.7119 328.9588 188.9868 362.6839 188.9868 404.2846 c
f
0.3591 g
200.3794 407.412 m
200.3794 443.6446 229.7527 473.0179 265.9853 473.0179 c
302.218 473.0179 331.5913 443.6446 331.5913 407.412 c
331.5913 371.1793 302.218 341.806 265.9853 341.806 c
229.7527 341.806 200.3794 371.1793 200.3794 407.412 c
f
0.3818 g
211.772 410.5393 m
211.772 441.404 236.7935 466.4255 267.6581 466.4255 c
298.5227 466.4255 323.5442 441.404 323.5442 410.5393 c
323.5442 379.6748 298.5227 354.6532 267.6581 354.6532 c
236.7935 354.6532 211.772 379.6748 211.772 410.5393 c
f
0.4045 g
223.1646 413.6667 m
223.1646 439.1633 243.8343 459.833 269.3309 459.833 c
294.8274 459.833 315.4972 439.1633 315.4972 413.6667 c
315.4972 388.1702 294.8274 367.5005 269.3309 367.5005 c
243.8343 367.5005 223.1646 388.1702 223.1646 413.6667 c
f
0.4273 g
234.5573 416.7941 m
234.5573 436.9226 250.8752 453.2405 271.0037 453.2405 c
291.1322 453.2405 307.4501 436.9226 307.4501 416.7941 c
307.4501 396.6656 291.1322 380.3477 271.0037 380.3477 c
250.8752 380.3477 234.5573 396.6656 234.5573 416.7941 c
f
U
0.45 g
245.948 419.921 m
245.948 434.6824 257.9148 446.6492 272.6762 446.6492 c
287.4376 446.6492 299.4044 434.6824 299.4044 419.921 c
299.4044 405.1596 287.4376 393.1927 272.6762 393.1927 c
257.9148 393.1927 245.948 405.1596 245.948 419.921 c
f
Q
0 O
0 g
0 R
0 G
0 i 0 J 0 j 1 w 4 M []0 d
%%Note:
289.7483 499.934 m
323.3996 489.1332 350.8221 464.5488 364.8541 432.0545 c
390.3671 372.9737 360.4601 299.753 300.8926 274.7434 c
241.5687 249.836 167.9347 279.1117 143.7827 339.0235 c
134.3854 362.3347 131.6141 386.862 137.3373 411.8925 c
145.5155 447.6591 157.8251 467.6706 191.9297 487.7602 c
222.0044 505.476 256.5007 510.6053 289.7483 499.934 c
s
1 g
0.5 w
262.9362 494.878 m
263.9038 495.9616 264.029 497.0776 263.6135 497.9427 c
262.428 500.4107 259.8451 498.5589 258.7761 497.0208 C
258.1363 498.4351 256.8504 498.1583 255.8006 497.9151 c
255.004 497.7306 254.317 496.9224 254.8631 496.077 c
255.6469 494.8637 256.6282 493.6156 257.8426 493.2309 c
259.3329 492.7589 260.7498 492.4297 262.9362 494.878 c
b
246.261 490.0954 m
247.0191 495.3287 247.1764 499.5381 251.6501 503.1758 c
252.3093 503.7118 251.5041 504.8194 250.7648 504.878 c
246.1479 505.2436 237.1615 504.8332 235.8237 502.4362 c
233.7228 498.6722 235.8776 491.4663 241.0037 488.4015 c
242.3837 487.5763 245.7645 486.6679 246.261 490.0954 c
b
221.7933 487.0311 m
222.2423 486.2785 222.8567 485.611 223.7408 486.0865 c
226.5326 487.588 222.6996 489.3542 223.7761 491.0208 C
225.1099 489.6871 226.4425 488.3545 227.7761 487.0208 C
231.1632 492.2806 223.8779 497.3235 220.359 499.2646 c
216.5141 501.3856 212.9676 494.4472 210.7761 492.0208 C
214.6938 490.2114 219.1382 491.4814 221.7933 487.0311 c
b
219.4496 475.1803 m
217.2548 480.8589 214.9571 485.8608 209.5444 487.2241 c
208.3401 487.5274 205.9487 484.81 204.9404 482.783 c
202.4377 477.752 209.3265 475.0647 207.878 471.2099 c
206.695 468.0619 206.5051 464.2489 204.3433 461.1545 c
203.4441 459.8674 201.5381 461.562 200.8447 462.9608 c
200.1052 464.4525 201.7189 466.7855 199.6509 467.7631 c
195.4009 469.7723 187.4771 470.989 188.3149 476.8093 c
188.9238 481.0387 195.1368 482.9055 195.5333 487.9101 c
195.5857 488.5717 194.6187 489.3568 193.776 488.8036 c
182.5886 481.4583 171.3027 475.5423 163.0261 465.3958 c
147.0595 445.8222 132.091 418.4364 140.7136 391.8958 C
144.2369 398.2317 136.3142 404.56 140.7136 410.8958 C
143.3919 402.1176 145.3569 393.5363 152.2552 386.4497 c
152.8715 385.8166 150.907 382.7934 151.947 381.0338 c
155.1274 375.6534 161.797 374.5592 167.7136 374.8958 C
167.2928 371.7261 170.0157 369.9832 171.8688 369.3494 c
180.6928 366.3307 187.049 360.8411 194.8662 356.1501 c
196.9756 354.8843 196.2676 358.8141 197.6913 358.672 c
205.2502 357.9173 205.856 350.0908 207.0701 343.9665 c
207.3868 342.3684 210.0023 341.4284 210.3812 339.8177 c
211.3784 335.5789 209.4697 330.6396 211.3356 327.2369 c
216.4342 317.9387 231.7717 315.7572 234.4636 306.6458 c
237.7136 295.6458 237.5532 281.9055 241.9621 269.9878 c
242.5616 268.3672 244.1946 266.5581 245.7822 266.2557 c
248.9949 265.6439 260.1357 265.6306 262.4584 266.5446 c
268.1426 268.7815 275.9636 274.3958 276.6494 278.1308 c
279.1081 291.5213 288.3125 290.4866 292.0735 297.2517 c
293.3588 299.5637 293.0046 303.4012 292.2678 307.009 c
291.3356 311.5736 296.06 314.2964 298.3463 318.1157 c
299.4239 319.916 301.023 323.1725 299.3826 324.4808 c
291.6107 330.6793 282.2473 333.5366 272.7136 329.8958 C
271.679 333.3266 275.1378 336.3038 273.0433 340.0788 c
272.4035 341.232 273.1099 343.5575 273.085 344.8841 c
272.927 353.3242 268.3777 361.9687 257.7574 362.615 c
254.4437 362.8166 254.3365 368.8336 250.6923 370.8573 c
242.0101 375.6786 234.0391 370.1833 225.7136 367.8958 C
225.6417 368.9832 226.1112 370.7205 224.7233 370.6631 c
217.2654 370.354 208.1444 366.1258 207.7136 357.8958 C
205.0878 359.1552 203.941 362.5496 200.7082 362.8338 c
198.3213 363.0437 196.072 360.9694 193.7825 362.0426 c
192.5648 362.6134 191.3771 363.7481 190.8861 364.9654 c
189.7628 367.7501 192.5051 371.6355 189.5049 373.5725 c
187.0301 375.1703 182.2637 372.1887 181.3511 375.0959 c
180.5628 377.607 186.6741 382.6222 183.457 384.4423 c
180.6287 386.0426 177.4147 384.1035 174.3916 382.5047 c
167.5434 378.883 161.5311 387.4385 160.3434 394.0097 c
159.1788 400.4532 161.181 408.6551 167.8732 411.5235 c
171.8335 413.221 176.6781 409.4493 180.5016 411.3275 c
182.4996 412.309 184.905 413.7755 186.4141 412.5323 c
189.4681 410.016 193.6844 409.3116 195.5327 405.8006 c
196.6171 403.7409 194.2784 400.8098 196.8082 399.0303 c
196.8784 398.9809 197.3786 399.5608 197.7136 399.8958 C
197.1685 396.2387 199.6003 393.3354 200.7136 389.8958 C
201.7147 390.8969 203.155 391.7468 203.481 392.9585 c
205.4984 400.456 199.5463 408.4574 202.7416 414.3372 c
206.2251 420.7472 209.5076 426.8985 213.018 433.7397 c
214.4742 436.5776 217.1338 438.6911 219.7963 440.791 c
220.5525 441.3875 221.0831 440.4498 221.7747 439.987 c
222.6111 439.4272 223.6213 440.2459 223.5098 440.8587 c
223.3982 441.4718 222.2018 442.341 222.8303 442.6783 c
226.2465 444.5119 228.1605 447.4301 230.7136 449.8958 C
226.2239 453.2582 220.035 448.8928 216.7136 444.8958 C
222.8849 449.8136 225.1703 460.8635 234.7136 456.8958 C
235.8882 460.7527 241.8715 459.8852 241.7252 461.8211 c
241.1125 469.9232 231.998 474.5171 226.7136 480.8958 C
225.5663 479.0559 225.4812 476.7725 224.4154 475.0841 c
223.5966 473.7867 221.5572 469.7268 219.4496 475.1803 c
b
249.7922 448.0593 m
250.7217 447.6692 251.505 448.2479 251.6604 449.0434 c
252.5609 453.653 247.2679 453.2509 245.7761 456.0208 C
245.4394 455.6842 245.1038 455.1253 244.78 455.1363 c
243.1977 455.1898 244.2984 458.0949 242.829 457.7765 c
239.4154 457.037 241.9164 452.8662 239.7761 451.0208 C
243.0007 449.6536 246.5276 449.4293 249.7922 448.0593 c
b
298.6886 481.156 m
301.8026 483.1714 298.3354 486.4673 296.7543 486.539 c
294.9557 486.6204 295.7592 483.6663 295.958 482.0431 c
296.1208 480.7135 297.7139 480.5252 298.6886 481.156 c
b
304.3822 481.1275 m
304.1183 480.1533 303.6413 479.0982 303.8806 478.0446 c
304.229 476.5104 306.2117 476.7436 306.4942 477.1966 c
308.2003 479.9326 310.5241 479.3387 311.3297 482.1488 c
312.842 487.4244 305.5648 486.3447 302.9461 489.1779 c
302.4362 489.7297 302.9557 491.0518 302.6863 491.9952 c
302.4607 492.7855 301.5234 493.5389 300.8982 492.9012 c
296.0264 487.9319 305.7106 486.0319 304.3822 481.1275 c
b
315.7649 478.9803 m
313.119 479.7079 312.3219 477.2227 310.7761 476.0208 C
311.4426 475.3543 312.0104 474.3835 312.8164 474.182 c
314.7507 473.6985 316.9925 474.5319 318.6585 473.7653 c
322.1959 472.1373 323.7502 467.5142 323.1033 464.1502 c
321.9755 458.2864 315.0336 460.6195 309.8228 459.7433 c
308.6534 459.5467 307.5293 458.1711 306.9075 456.9537 c
306.0205 455.2169 308.1732 454.2713 308.4612 452.9521 c
309.2362 449.4015 308.3715 443.9141 311.8068 443.7742 c
315.7832 443.6122 318.925 447.4477 323.7822 447.3605 c
324.7653 447.3429 326.4761 449.0554 326.4241 450.0014 c
326.1186 455.55 325.1462 461.5031 330.0952 464.4926 c
333.6101 466.6157 339.2649 466.0933 342.948 463.2429 c
343.1583 463.0802 344.2775 464.2138 343.6656 464.9259 c
336.0389 473.8014 327.6993 480.4107 317.7184 486.9325 c
316.8765 487.4826 315.8357 486.6016 315.9922 486.0865 c
316.3608 484.8728 318.0582 484.1698 318.6295 482.9521 c
319.4335 481.2381 318.7872 478.1492 315.7649 478.9803 c
b
335.8932 456.9075 m
335.2636 456.2568 336.0755 455.1817 336.7759 455.1825 c
337.4766 455.1833 338.2894 456.2566 337.6589 456.9072 c
337.3285 457.2481 336.2223 457.2475 335.8932 456.9075 c
b
345.6561 451.1443 m
346.2943 451.7646 345.4771 452.5368 344.7761 453.0208 C
344.3766 451.4521 341.669 452.4946 342.0344 451.0879 c
342.6272 448.8055 344.6541 450.1703 345.6561 451.1443 c
b
345.6136 457.008 m
345.744 455.354 347.2075 455.0874 347.7761 454.0208 C
350.6015 457.253 347.6156 462.2134 344.7464 462.3383 c
342.1785 462.45 345.4673 458.8636 345.6136 457.008 c
b
339.8964 387.445 m
345.2477 385.9283 353.2441 390.7796 354.3547 382.961 c
355.0814 377.8452 356.0482 373.4821 358.2538 368.776 c
360.6779 363.604 357.6652 357.669 356.2543 352.1543 c
355.3741 348.714 352.6667 345.7619 350.041 342.7871 c
348.0474 340.5285 348.6645 336.9477 348.2582 333.9554 c
347.6854 329.7359 351.5231 321.3322 353.7612 323.2225 c
364.6913 332.4542 372.0321 360.5778 373.424 375.0547 c
375.4573 396.2029 372.3386 420.5833 360.2041 439.6551 c
357.2261 444.3356 350.7969 441.895 345.8619 443.3183 c
344.246 443.7844 343.3053 446.2304 341.6876 446.74 c
335.3839 448.7257 329.5215 444.5618 324.3494 440.5743 c
322.3254 439.0138 320.0442 443.219 316.7913 441.9809 c
314.5552 441.1297 314.6569 438.6022 314.1122 436.9125 c
313.0832 433.7205 314.2317 430.3247 315.3881 426.8902 c
316.3586 424.0074 313.5326 421.4991 312.2302 418.8016 c
308.5155 411.1074 311.2912 402.3222 311.2242 394.0172 c
311.2136 392.6942 313.2467 390.9395 314.8687 390.2336 c
319.5544 388.1944 324.6825 388.2089 329.8298 387.3384 c
333.0988 386.7855 336.136 388.5107 339.8964 387.445 c
b
U
%%Trailer
Adobe_Illustrator881 /terminate get exec
Adobe_customcolor /terminate get exec
Adobe_cshow /terminate get exec
Adobe_cmykcolor /terminate get exec

```

## File: `source/index.d.ts`
```typescript
/**
Typings for primary entry point.
*/

import type {ReadableStream as WebReadableStream} from 'node:stream/web';
import type {ITokenizer} from 'strtok3';

/**
Either the Node.js ReadableStream or the `lib.dom.d.ts` ReadableStream.
Related issue: https://github.com/DefinitelyTyped/DefinitelyTyped/pull/60377
*/
export type AnyWebReadableStream<G> = WebReadableStream<G> | ReadableStream<G>;

export type FileTypeResult = {
	/**
	One of the supported [file types](https://github.com/sindresorhus/file-type#supported-file-types).
	*/
	readonly ext: string;

	/**
	The detected [MIME type](https://en.wikipedia.org/wiki/Internet_media_type).
	*/
	readonly mime: string;
};

/**
Detect the file type of a `Uint8Array` or `ArrayBuffer`.

The file type is detected by checking the [magic number](https://en.wikipedia.org/wiki/Magic_number_(programming)#Magic_numbers_in_files) of the buffer.

In Node.js, it is recommended to use `fileTypeFromFile()` instead when reading from a file path.

@param buffer - A Uint8Array or ArrayBuffer representing file data. It works best if the buffer contains the entire file. It may work with a smaller portion as well.
@param options - Options to override default behavior.
@returns The detected file type, or `undefined` when there is no match.
*/
export function fileTypeFromBuffer(buffer: Uint8Array | ArrayBuffer, options?: FileTypeOptions): Promise<FileTypeResult | undefined>;

/**
Detect the file type of a [web `ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream).

The file type is detected by checking the [magic number](https://en.wikipedia.org/wiki/Magic_number_(programming)#Magic_numbers_in_files) of the buffer.

If you have a Node.js `stream.Readable`, convert it with [`Readable.toWeb()`](https://nodejs.org/api/stream.html#streamreadabletowebstreamreadable-options).

@param stream - A [web `ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream) streaming a file to examine.
@param options - Options to override default behavior.
@returns A `Promise` for an object with the detected file type, or `undefined` when there is no match.
*/
export function fileTypeFromStream(stream: AnyWebReadableStream<Uint8Array>, options?: FileTypeOptions): Promise<FileTypeResult | undefined>;

/**
Detect the file type from an [`ITokenizer`](https://github.com/Borewit/strtok3#tokenizer) source.

This method is used internally, but can also be used for a special "tokenizer" reader.

A tokenizer propagates the internal read functions, allowing alternative transport mechanisms, to access files, to be implemented and used.

@param tokenizer - File source implementing the tokenizer interface.
@param options - Options to override default behavior.
@returns The detected file type, or `undefined` when there is no match.

An example is [`@tokenizer/http`](https://github.com/Borewit/tokenizer-http), which requests data using [HTTP-range-requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Range_requests). A difference with a conventional stream and the [*tokenizer*](https://github.com/Borewit/strtok3#tokenizer), is that it can *ignore* (seek, fast-forward) in the stream. For example, you may only need and read the first 6 bytes, and the last 128 bytes, which may be an advantage in case reading the entire file would take longer.

@example
```
import {makeTokenizer} from '@tokenizer/http';
import {fileTypeFromTokenizer} from 'file-type';

const audioTrackUrl = 'https://test-audio.netlify.com/Various%20Artists%20-%202009%20-%20netBloc%20Vol%2024_%20tiuqottigeloot%20%5BMP3-V2%5D/01%20-%20Diablo%20Swing%20Orchestra%20-%20Heroines.mp3';

const httpTokenizer = await makeTokenizer(audioTrackUrl);
const fileType = await fileTypeFromTokenizer(httpTokenizer);

console.log(fileType);
//=> {ext: 'mp3', mime: 'audio/mpeg'}
```
*/
export function fileTypeFromTokenizer(tokenizer: ITokenizer, options?: FileTypeOptions): Promise<FileTypeResult | undefined>;

/**
Supported file extensions.
*/
export const supportedExtensions: ReadonlySet<string>;

/**
Supported MIME types.
*/
export const supportedMimeTypes: ReadonlySet<string>;

export type StreamOptions = {
	/**
	The default sample size in bytes.

	@default 4100
	*/
	readonly sampleSize?: number;
};

/**
Detect the file type of a [`Blob`](https://nodejs.org/api/buffer.html#class-blob) or [`File`](https://developer.mozilla.org/en-US/docs/Web/API/File).

@param blob - The [`Blob`](https://nodejs.org/api/buffer.html#class-blob) used for file detection.
@param options - Options to override default behavior.
@returns The detected file type, or `undefined` when there is no match.

@example
```
import {fileTypeFromBlob} from 'file-type';

const blob = new Blob(['<?xml version="1.0" encoding="ISO-8859-1" ?>'], {
	type: 'text/plain',
	endings: 'native'
});

console.log(await fileTypeFromBlob(blob));
//=> {ext: 'txt', mime: 'text/plain'}
```
*/
export declare function fileTypeFromBlob(blob: Blob, options?: FileTypeOptions): Promise<FileTypeResult | undefined>;

/**
A custom file type detector.

Custom file type detectors are plugins designed to extend the default detection capabilities.
They allow support for uncommon file types, non-binary formats, or customized detection behavior.

Detectors can be added via the constructor options or by directly modifying `FileTypeParser#detectors`.
Detectors provided through the constructor are executed before the default ones.

### Example adding a detector

```js
import {FileTypeParser} from 'file-type';
import {detectXml} from '@file-type/xml';

const parser = new FileTypeParser({customDetectors: [detectXml]});
const fileType = await parser.fromFile('sample.kml');
console.log(fileType);
```

### Available third-party file-type detectors

- [@file-type/av](https://github.com/Borewit/file-type-av): Improves detection of audio and video file formats, with accurate differentiation between the two
- [@file-type/cfbf](https://github.com/Borewit/file-type-cfbf): Detects Compound File Binary Format (CFBF) based formats, such as Office 97–2003 documents and `.msi`.
- [@file-type/pdf](https://github.com/Borewit/file-type-pdf): Detects PDF based file types, such as Adobe Illustrator
- [@file-type/xml](https://github.com/Borewit/file-type-xml): Detects common XML file types, such as GLM, KML, MusicXML, RSS, SVG, and XHTML

### Detector execution flow

If a detector returns `undefined`, the following rules apply:

1. **No Tokenizer Interaction**: If the detector does not modify the tokenizer's position, the next detector in the sequence is executed.
2. **Tokenizer Interaction**: If the detector modifies the tokenizer's position (`tokenizer.position` is advanced), no further detectors are executed. In this case, the file type remains `undefined`, as subsequent detectors cannot evaluate the content. This is an exceptional scenario, as it prevents any other detectors from determining the file type.

### Example writing a custom detector

Below is an example of a custom detector. This can be passed to the `FileTypeParser` via the `customDetectors` option.

```
import {FileTypeParser} from 'file-type';

const unicornDetector = {
	id: 'unicorn',
	async detect(tokenizer) {
		const unicornHeader = [85, 78, 73, 67, 79, 82, 78]; // "UNICORN" in ASCII decimal

		const buffer = new Uint8Array(unicornHeader.length);
		await tokenizer.peekBuffer(buffer, {length: unicornHeader.length, mayBeLess: true});
		if (unicornHeader.every((value, index) => value === buffer[index])) {
			return {ext: 'unicorn', mime: 'application/unicorn'};
		}

		return undefined;
	}
};

const buffer = new Uint8Array([85, 78, 73, 67, 79, 82, 78]);
const parser = new FileTypeParser({customDetectors: [unicornDetector]});
const fileType = await parser.fromBuffer(buffer);
console.log(fileType); // {ext: 'unicorn', mime: 'application/unicorn'}
```

@param tokenizer - The [tokenizer](https://github.com/Borewit/strtok3#tokenizer) used to read file content.
@param fileType - The file type detected by standard or previous custom detectors, or `undefined` if no match is found.
@returns The detected file type, or `undefined` if no match is found.
*/
export type Detector = {
	id: string;
	detect: (tokenizer: ITokenizer, fileType?: FileTypeResult) => Promise<FileTypeResult | undefined>;
};

export type FileTypeOptions = {
	customDetectors?: Iterable<Detector>;

	/**
	An `AbortSignal` to cancel the detection.
	*/
	signal?: AbortSignal;

	/**
	Specifies the byte tolerance for locating the first MPEG audio frame (e.g. `.mp1`, `.mp2`, `.mp3`, `.aac`).

	Allows detection to handle slight sync offsets between the expected and actual frame start. Common in malformed or incorrectly muxed files, which, while technically invalid, do occur in the wild.

	A tolerance of 10 bytes covers most cases.

	@default 0
	*/
	mpegOffsetTolerance?: number;
};

export declare class TokenizerPositionError extends Error {
	constructor(message?: string);
}

export type AnyWebReadableByteStreamWithFileType = AnyWebReadableStream<Uint8Array> & {
	readonly fileType?: FileTypeResult;
};

/**
Detect the file type of a file path.

The file type is detected by checking the [magic number](https://en.wikipedia.org/wiki/Magic_number_(programming)#Magic_numbers_in_files) of the file.

Only available in environments where `node:fs` is available, such as Node.js. To read from a [`File`](https://developer.mozilla.org/docs/Web/API/File), see `fileTypeFromBlob()`.

@param filePath - The file path to examine.
@param options - Options to override default behavior.
@returns The detected file type and MIME type or `undefined` when there is no match.
*/
export function fileTypeFromFile(filePath: string, options?: FileTypeOptions): Promise<FileTypeResult | undefined>;

/**
Returns a `Promise` which resolves to the original readable stream argument, but with an added `fileType` property, which is an object like the one returned from `fileTypeFromFile()`.

This method can be handy to put in a stream pipeline, but it comes with a price. Internally `stream()` builds up a buffer of `sampleSize` bytes, used as a sample, to determine the file type. The sample size impacts the file detection resolution. A smaller sample size will result in lower probability of the best file type detection.
*/
export function fileTypeStream(webStream: AnyWebReadableStream<Uint8Array>, options?: StreamOptions & FileTypeOptions): Promise<AnyWebReadableByteStreamWithFileType>;

export declare class FileTypeParser {
	/**
	File type detectors.

	Initialized with a single entry holding the built-in detector function.
	*/
	detectors: Detector[];

	constructor(options?: FileTypeOptions);

	/**
	Works the same way as {@link fileTypeFromBuffer}, additionally taking into account custom detectors (if any were provided to the constructor).
	*/
	fromBuffer(buffer: Uint8Array | ArrayBuffer): Promise<FileTypeResult | undefined>;

	/**
	Works the same way as {@link fileTypeFromTokenizer}, additionally taking into account custom detectors (if any were provided to the constructor).
	*/
	fromTokenizer(tokenizer: ITokenizer): Promise<FileTypeResult | undefined>;

	/**
	Works the same way as {@link fileTypeFromBlob}, additionally taking into account custom detectors (if any were provided to the constructor).
	*/
	fromBlob(blob: Blob): Promise<FileTypeResult | undefined>;

	/**
	Works the same way as {@link fileTypeFromStream}, additionally taking into account custom detectors (if any were provided to the constructor).
	*/
	fromStream(stream: AnyWebReadableStream<Uint8Array>): Promise<FileTypeResult | undefined>;

	/**
	Works the same way as {@link fileTypeFromFile}, additionally taking into account custom detectors (if any were provided to the constructor). Only available where `node:fs` is available.
	*/
	fromFile(filePath: string): Promise<FileTypeResult | undefined>;

	/**
	Works the same way as {@link fileTypeStream}, additionally taking into account custom detectors (if any were provided to the constructor).
	*/
	toDetectionStream(webStream: AnyWebReadableStream<Uint8Array>, options?: StreamOptions & FileTypeOptions): Promise<AnyWebReadableByteStreamWithFileType>;
}
```

## File: `source/index.js`
```javascript
/**
Primary entry point, Node.js specific entry point is index.js
*/

import * as Token from 'token-types';
import * as strtok3 from 'strtok3/core';
import {GzipHandler} from '@tokenizer/inflate';
import {concatUint8Arrays} from 'uint8array-extras';
import {
	stringToBytes,
	tarHeaderChecksumMatches,
	uint32SyncSafeToken,
} from './tokens.js';
import {extensions, mimeTypes} from './supported.js';
import {
	maximumUntrustedSkipSizeInBytes,
	ParserHardLimitError,
	safeIgnore,
	checkBytes,
	hasUnknownFileSize,
} from './parser.js';
import {detectZip} from './detectors/zip.js';
import {detectEbml} from './detectors/ebml.js';
import {detectPng} from './detectors/png.js';
import {detectAsf} from './detectors/asf.js';

export const reasonableDetectionSizeInBytes = 4100; // A fair amount of file-types are detectable within this range.
const maximumMpegOffsetTolerance = reasonableDetectionSizeInBytes - 2;
const maximumNestedGzipDetectionSizeInBytes = maximumUntrustedSkipSizeInBytes;
const maximumNestedGzipProbeDepth = 1;
const unknownSizeGzipProbeTimeoutInMilliseconds = 100;
const maximumId3HeaderSizeInBytes = maximumUntrustedSkipSizeInBytes;
const maximumTiffTagCount = 512;
const maximumDetectionReentryCount = 256;
const maximumTiffStreamIfdOffsetInBytes = 1024 * 1024;
const maximumTiffIfdOffsetInBytes = maximumUntrustedSkipSizeInBytes;

export function normalizeSampleSize(sampleSize) {
	// `sampleSize` is an explicit caller-controlled tuning knob, not untrusted file input.
	// Preserve valid caller-requested probe depth here; applications must bound attacker-derived option values themselves.
	if (!Number.isFinite(sampleSize)) {
		return reasonableDetectionSizeInBytes;
	}

	return Math.max(1, Math.trunc(sampleSize));
}

function normalizeMpegOffsetTolerance(mpegOffsetTolerance) {
	// This value controls scan depth and therefore worst-case CPU work.
	if (!Number.isFinite(mpegOffsetTolerance)) {
		return 0;
	}

	return Math.max(0, Math.min(maximumMpegOffsetTolerance, Math.trunc(mpegOffsetTolerance)));
}

function getKnownFileSizeOrMaximum(fileSize) {
	if (!Number.isFinite(fileSize)) {
		return Number.MAX_SAFE_INTEGER;
	}

	return Math.max(0, fileSize);
}

// Wrap stream in an identity TransformStream to avoid BYOB readers.
// Node.js has a bug where calling controller.close() inside a BYOB stream's
// pull() callback does not resolve pending reader.read() calls, causing
// permanent hangs on streams shorter than the requested read size.
// Using a default (non-BYOB) reader via TransformStream avoids this.
function toDefaultStream(stream) {
	return stream.pipeThrough(new TransformStream());
}

function readWithSignal(reader, signal) {
	if (signal === undefined) {
		return reader.read();
	}

	signal.throwIfAborted();

	return Promise.race([
		reader.read(),
		new Promise((_resolve, reject) => {
			signal.addEventListener('abort', () => {
				reject(signal.reason);
				reader.cancel(signal.reason).catch(() => {});
			}, {once: true});
		}),
	]);
}

function createByteLimitedReadableStream(stream, maximumBytes) {
	const reader = stream.getReader();
	let emittedBytes = 0;
	let sourceDone = false;
	let sourceCanceled = false;

	const cancelSource = async reason => {
		if (
			sourceDone
			|| sourceCanceled
		) {
			return;
		}

		sourceCanceled = true;
		await reader.cancel(reason);
	};

	return new ReadableStream({
		async pull(controller) {
			if (emittedBytes >= maximumBytes) {
				controller.close();
				await cancelSource();
				return;
			}

			const {done, value} = await reader.read();
			if (
				done
				|| !value
			) {
				sourceDone = true;
				controller.close();
				return;
			}

			const remainingBytes = maximumBytes - emittedBytes;
			if (value.length > remainingBytes) {
				controller.enqueue(value.subarray(0, remainingBytes));
				emittedBytes += remainingBytes;
				controller.close();
				await cancelSource();
				return;
			}

			controller.enqueue(value);
			emittedBytes += value.length;
		},
		async cancel(reason) {
			await cancelSource(reason);
		},
	});
}

export async function fileTypeFromStream(stream, options) {
	return new FileTypeParser(options).fromStream(stream);
}

export async function fileTypeFromBuffer(input, options) {
	return new FileTypeParser(options).fromBuffer(input);
}

export async function fileTypeFromBlob(blob, options) {
	return new FileTypeParser(options).fromBlob(blob);
}

export async function fileTypeFromTokenizer(tokenizer, options) {
	return new FileTypeParser(options).fromTokenizer(tokenizer);
}

export async function fileTypeStream(webStream, options) {
	return new FileTypeParser(options).toDetectionStream(webStream, options);
}

export class FileTypeParser {
	constructor(options) {
		const normalizedMpegOffsetTolerance = normalizeMpegOffsetTolerance(options?.mpegOffsetTolerance);
		this.options = {
			...options,
			mpegOffsetTolerance: normalizedMpegOffsetTolerance,
		};

		this.detectors = [...(this.options.customDetectors ?? []),
			{id: 'core', detect: this.detectConfident},
			{id: 'core.imprecise', detect: this.detectImprecise}];
		this.tokenizerOptions = {
			abortSignal: this.options.signal,
		};
		this.gzipProbeDepth = 0;
	}

	getTokenizerOptions() {
		return {
			...this.tokenizerOptions,
		};
	}

	createTokenizerFromWebStream(stream) {
		return strtok3.fromWebStream(toDefaultStream(stream), this.getTokenizerOptions());
	}

	async parseTokenizer(tokenizer, detectionReentryCount = 0) {
		this.detectionReentryCount = detectionReentryCount;
		const initialPosition = tokenizer.position;
		// Iterate through all file-type detectors
		for (const detector of this.detectors) {
			let fileType;
			try {
				fileType = await detector.detect(tokenizer);
			} catch (error) {
				if (error instanceof strtok3.EndOfStreamError) {
					return;
				}

				if (error instanceof ParserHardLimitError) {
					return;
				}

				throw error;
			}

			if (fileType) {
				return fileType;
			}

			if (initialPosition !== tokenizer.position) {
				return undefined; // Cannot proceed scanning of the tokenizer is at an arbitrary position
			}
		}
	}

	async fromTokenizer(tokenizer) {
		try {
			return await this.parseTokenizer(tokenizer);
		} finally {
			await tokenizer.close();
		}
	}

	async fromBuffer(input) {
		if (!(input instanceof Uint8Array || input instanceof ArrayBuffer)) {
			throw new TypeError(`Expected the \`input\` argument to be of type \`Uint8Array\` or \`ArrayBuffer\`, got \`${typeof input}\``);
		}

		const buffer = input instanceof Uint8Array ? input : new Uint8Array(input);

		if (!(buffer?.length > 1)) {
			return;
		}

		return this.fromTokenizer(strtok3.fromBuffer(buffer, this.getTokenizerOptions()));
	}

	async fromBlob(blob) {
		this.options.signal?.throwIfAborted();
		const tokenizer = strtok3.fromBlob(blob, this.getTokenizerOptions());
		return this.fromTokenizer(tokenizer);
	}

	async fromStream(stream) {
		this.options.signal?.throwIfAborted();
		const tokenizer = this.createTokenizerFromWebStream(stream);
		return this.fromTokenizer(tokenizer);
	}

	async fromFile(path) {
		this.options.signal?.throwIfAborted();
		// TODO: Remove this when `strtok3.fromFile()` safely rejects non-regular filesystem objects without a pathname race.
		const [{default: fsPromises}, {FileTokenizer}] = await Promise.all([
			import('node:fs/promises'),
			import('strtok3'),
		]);
		const fileHandle = await fsPromises.open(path, fsPromises.constants.O_RDONLY | fsPromises.constants.O_NONBLOCK);
		const fileStat = await fileHandle.stat();
		if (!fileStat.isFile()) {
			await fileHandle.close();
			return;
		}

		const tokenizer = new FileTokenizer(fileHandle, {
			...this.getTokenizerOptions(),
			fileInfo: {path, size: fileStat.size},
		});
		return this.fromTokenizer(tokenizer);
	}

	async toDetectionStream(stream, options) {
		this.options.signal?.throwIfAborted();
		const sampleSize = normalizeSampleSize(options?.sampleSize ?? reasonableDetectionSizeInBytes);
		let detectedFileType;
		let streamEnded = false;

		const reader = stream.getReader();
		const chunks = [];
		let totalSize = 0;

		try {
			while (totalSize < sampleSize) {
				const {value, done} = await readWithSignal(reader, this.options.signal);
				if (done || !value) {
					streamEnded = true;
					break;
				}

				chunks.push(value);
				totalSize += value.length;
			}

			if (
				!streamEnded
				&& totalSize === sampleSize
			) {
				const {value, done} = await readWithSignal(reader, this.options.signal);
				if (done || !value) {
					streamEnded = true;
				} else {
					chunks.push(value);
					totalSize += value.length;
				}
			}
		} finally {
			reader.releaseLock();
		}

		if (totalSize > 0) {
			const sample = chunks.length === 1 ? chunks[0] : concatUint8Arrays(chunks);
			try {
				detectedFileType = await this.fromBuffer(sample.subarray(0, sampleSize));
			} catch (error) {
				if (!(error instanceof strtok3.EndOfStreamError)) {
					throw error;
				}

				detectedFileType = undefined;
			}

			if (
				!streamEnded
				&& detectedFileType?.ext === 'pages'
			) {
				detectedFileType = {
					ext: 'zip',
					mime: 'application/zip',
				};
			}
		}

		// Prepend collected chunks and pipe the rest through
		const transformStream = new TransformStream({
			start(controller) {
				for (const chunk of chunks) {
					controller.enqueue(chunk);
				}
			},
			transform(chunk, controller) {
				controller.enqueue(chunk);
			},
		});

		const newStream = stream.pipeThrough(transformStream);
		newStream.fileType = detectedFileType;

		return newStream;
	}

	async detectGzip(tokenizer) {
		if (this.gzipProbeDepth >= maximumNestedGzipProbeDepth) {
			return {
				ext: 'gz',
				mime: 'application/gzip',
			};
		}

		const gzipHandler = new GzipHandler(tokenizer);
		const limitedInflatedStream = createByteLimitedReadableStream(gzipHandler.inflate(), maximumNestedGzipDetectionSizeInBytes);
		const hasUnknownSize = hasUnknownFileSize(tokenizer);
		let timeout;
		let probeSignal;
		let probeParser;
		let compressedFileType;

		if (hasUnknownSize) {
			const timeoutController = new AbortController();
			timeout = setTimeout(() => {
				timeoutController.abort(new DOMException(`Operation timed out after ${unknownSizeGzipProbeTimeoutInMilliseconds} ms`, 'TimeoutError'));
			}, unknownSizeGzipProbeTimeoutInMilliseconds);
			probeSignal = this.options.signal === undefined
				? timeoutController.signal
				: AbortSignal.any([this.options.signal, timeoutController.signal]);
			probeParser = new FileTypeParser({
				...this.options,
				signal: probeSignal,
			});
			probeParser.gzipProbeDepth = this.gzipProbeDepth + 1;
		} else {
			this.gzipProbeDepth++;
		}

		try {
			compressedFileType = await (probeParser ?? this).fromStream(limitedInflatedStream);
		} catch (error) {
			if (
				error?.name === 'AbortError'
				&& probeSignal?.reason?.name !== 'TimeoutError'
			) {
				throw error;
			}

			// Timeout, decompression, or inner-detection failures are expected for non-tar gzip files.
		} finally {
			clearTimeout(timeout);
			if (!hasUnknownSize) {
				this.gzipProbeDepth--;
			}
		}

		if (compressedFileType?.ext === 'tar') {
			return {
				ext: 'tar.gz',
				mime: 'application/gzip',
			};
		}

		return {
			ext: 'gz',
			mime: 'application/gzip',
		};
	}

	check(header, options) {
		return checkBytes(this.buffer, header, options);
	}

	checkString(header, options) {
		return this.check(stringToBytes(header, options?.encoding), options);
	}

	// Detections with a high degree of certainty in identifying the correct file type
	detectConfident = async tokenizer => {
		this.buffer = new Uint8Array(reasonableDetectionSizeInBytes);

		// Keep reading until EOF if the file size is unknown.
		if (tokenizer.fileInfo.size === undefined) {
			tokenizer.fileInfo.size = Number.MAX_SAFE_INTEGER;
		}

		this.tokenizer = tokenizer;

		if (hasUnknownFileSize(tokenizer)) {
			await tokenizer.peekBuffer(this.buffer, {length: 3, mayBeLess: true});
			if (this.check([0x1F, 0x8B, 0x8])) {
				return this.detectGzip(tokenizer);
			}
		}

		await tokenizer.peekBuffer(this.buffer, {length: 32, mayBeLess: true});

		// -- 2-byte signatures --

		if (this.check([0x42, 0x4D])) {
			return {
				ext: 'bmp',
				mime: 'image/bmp',
			};
		}

		if (this.check([0x0B, 0x77])) {
			return {
				ext: 'ac3',
				mime: 'audio/vnd.dolby.dd-raw',
			};
		}

		if (this.check([0x78, 0x01])) {
			return {
				ext: 'dmg',
				mime: 'application/x-apple-diskimage',
			};
		}

		if (this.check([0x4D, 0x5A])) {
			return {
				ext: 'exe',
				mime: 'application/x-msdownload',
			};
		}

		if (this.check([0x25, 0x21])) {
			await tokenizer.peekBuffer(this.buffer, {length: 24, mayBeLess: true});

			if (
				this.checkString('PS-Adobe-', {offset: 2})
				&& this.checkString(' EPSF-', {offset: 14})
			) {
				return {
					ext: 'eps',
					mime: 'application/eps',
				};
			}

			return {
				ext: 'ps',
				mime: 'application/postscript',
			};
		}

		if (
			this.check([0x1F, 0xA0])
			|| this.check([0x1F, 0x9D])
		) {
			return {
				ext: 'Z',
				mime: 'application/x-compress',
			};
		}

		if (this.check([0xC7, 0x71])) {
			return {
				ext: 'cpio',
				mime: 'application/x-cpio',
			};
		}

		if (this.check([0x60, 0xEA])) {
			return {
				ext: 'arj',
				mime: 'application/x-arj',
			};
		}

		// -- 3-byte signatures --

		if (this.check([0xEF, 0xBB, 0xBF])) { // UTF-8-BOM
			if (this.detectionReentryCount >= maximumDetectionReentryCount) {
				return;
			}

			this.detectionReentryCount++;
			// Strip off UTF-8-BOM
			await this.tokenizer.ignore(3);
			return this.detectConfident(tokenizer);
		}

		if (this.check([0x47, 0x49, 0x46])) {
			return {
				ext: 'gif',
				mime: 'image/gif',
			};
		}

		if (this.check([0x49, 0x49, 0xBC])) {
			return {
				ext: 'jxr',
				mime: 'image/vnd.ms-photo',
			};
		}

		if (this.check([0x1F, 0x8B, 0x8])) {
			return this.detectGzip(tokenizer);
		}

		if (this.check([0x42, 0x5A, 0x68])) {
			return {
				ext: 'bz2',
				mime: 'application/x-bzip2',
			};
		}

		if (this.checkString('ID3')) {
			await safeIgnore(tokenizer, 6, {
				maximumLength: 6,
				reason: 'ID3 header prefix',
			}); // Skip ID3 header until the header size
			const id3HeaderLength = await tokenizer.readToken(uint32SyncSafeToken);
			const isUnknownFileSize = hasUnknownFileSize(tokenizer);
			if (
				!Number.isFinite(id3HeaderLength)
				|| id3HeaderLength < 0
				// Keep ID3 probing bounded for unknown-size streams to avoid attacker-controlled large skips.
				|| (
					isUnknownFileSize
					&& (
						id3HeaderLength > maximumId3HeaderSizeInBytes
						|| (tokenizer.position + id3HeaderLength) > maximumId3HeaderSizeInBytes
					)
				)
			) {
				return;
			}

			if (tokenizer.position + id3HeaderLength > tokenizer.fileInfo.size) {
				if (isUnknownFileSize) {
					return;
				}

				return {
					ext: 'mp3',
					mime: 'audio/mpeg',
				};
			}

			try {
				await safeIgnore(tokenizer, id3HeaderLength, {
					maximumLength: isUnknownFileSize ? maximumId3HeaderSizeInBytes : tokenizer.fileInfo.size,
					reason: 'ID3 payload',
				});
			} catch (error) {
				if (error instanceof strtok3.EndOfStreamError) {
					return;
				}

				throw error;
			}

			if (this.detectionReentryCount >= maximumDetectionReentryCount) {
				return;
			}

			this.detectionReentryCount++;
			return this.parseTokenizer(tokenizer, this.detectionReentryCount); // Skip ID3 header, recursion
		}

		// Musepack, SV7
		if (this.checkString('MP+')) {
			return {
				ext: 'mpc',
				mime: 'audio/x-musepack',
			};
		}

		if (
			(this.buffer[0] === 0x43 || this.buffer[0] === 0x46)
			&& this.check([0x57, 0x53], {offset: 1})
		) {
			return {
				ext: 'swf',
				mime: 'application/x-shockwave-flash',
			};
		}

		// -- 4-byte signatures --

		// Requires a sample size of 4 bytes
		if (this.check([0xFF, 0xD8, 0xFF])) {
			if (this.check([0xF7], {offset: 3})) { // JPG7/SOF55, indicating a ISO/IEC 14495 / JPEG-LS file
				return {
					ext: 'jls',
					mime: 'image/jls',
				};
			}

			return {
				ext: 'jpg',
				mime: 'image/jpeg',
			};
		}

		if (this.check([0x4F, 0x62, 0x6A, 0x01])) {
			return {
				ext: 'avro',
				mime: 'application/avro',
			};
		}

		if (this.checkString('FLIF')) {
			return {
				ext: 'flif',
				mime: 'image/flif',
			};
		}

		if (this.checkString('8BPS')) {
			return {
				ext: 'psd',
				mime: 'image/vnd.adobe.photoshop',
			};
		}

		// Musepack, SV8
		if (this.checkString('MPCK')) {
			return {
				ext: 'mpc',
				mime: 'audio/x-musepack',
			};
		}

		if (this.checkString('FORM')) {
			return {
				ext: 'aif',
				mime: 'audio/aiff',
			};
		}

		if (this.checkString('icns', {offset: 0})) {
			return {
				ext: 'icns',
				mime: 'image/icns',
			};
		}

		// Zip-based file formats
		// Need to be before the `zip` check
		if (this.check([0x50, 0x4B, 0x3, 0x4])) { // Local file header signature
			return detectZip(tokenizer);
		}

		if (this.checkString('OggS')) {
			// This is an OGG container
			await tokenizer.ignore(28);
			const type = new Uint8Array(8);
			await tokenizer.readBuffer(type);

			// Needs to be before `ogg` check
			if (checkBytes(type, [0x4F, 0x70, 0x75, 0x73, 0x48, 0x65, 0x61, 0x64])) {
				return {
					ext: 'opus',
					mime: 'audio/ogg; codecs=opus',
				};
			}

			// If ' theora' in header.
			if (checkBytes(type, [0x80, 0x74, 0x68, 0x65, 0x6F, 0x72, 0x61])) {
				return {
					ext: 'ogv',
					mime: 'video/ogg',
				};
			}

			// If '\x01video' in header.
			if (checkBytes(type, [0x01, 0x76, 0x69, 0x64, 0x65, 0x6F, 0x00])) {
				return {
					ext: 'ogm',
					mime: 'video/ogg',
				};
			}

			// If ' FLAC' in header  https://xiph.org/flac/faq.html
			if (checkBytes(type, [0x7F, 0x46, 0x4C, 0x41, 0x43])) {
				return {
					ext: 'oga',
					mime: 'audio/ogg',
				};
			}

			// 'Speex  ' in header https://en.wikipedia.org/wiki/Speex
			if (checkBytes(type, [0x53, 0x70, 0x65, 0x65, 0x78, 0x20, 0x20])) {
				return {
					ext: 'spx',
					mime: 'audio/ogg',
				};
			}

			// If '\x01vorbis' in header
			if (checkBytes(type, [0x01, 0x76, 0x6F, 0x72, 0x62, 0x69, 0x73])) {
				return {
					ext: 'ogg',
					mime: 'audio/ogg',
				};
			}

			// Default OGG container https://www.iana.org/assignments/media-types/application/ogg
			return {
				ext: 'ogx',
				mime: 'application/ogg',
			};
		}

		if (
			this.check([0x50, 0x4B])
			&& (this.buffer[2] === 0x3 || this.buffer[2] === 0x5 || this.buffer[2] === 0x7)
			&& (this.buffer[3] === 0x4 || this.buffer[3] === 0x6 || this.buffer[3] === 0x8)
		) {
			return {
				ext: 'zip',
				mime: 'application/zip',
			};
		}

		if (this.checkString('MThd')) {
			return {
				ext: 'mid',
				mime: 'audio/midi',
			};
		}

		if (
			this.checkString('wOFF')
			&& (
				this.check([0x00, 0x01, 0x00, 0x00], {offset: 4})
				|| this.checkString('OTTO', {offset: 4})
			)
		) {
			return {
				ext: 'woff',
				mime: 'font/woff',
			};
		}

		if (
			this.checkString('wOF2')
			&& (
				this.check([0x00, 0x01, 0x00, 0x00], {offset: 4})
				|| this.checkString('OTTO', {offset: 4})
			)
		) {
			return {
				ext: 'woff2',
				mime: 'font/woff2',
			};
		}

		if (this.check([0xD4, 0xC3, 0xB2, 0xA1]) || this.check([0xA1, 0xB2, 0xC3, 0xD4])) {
			return {
				ext: 'pcap',
				mime: 'application/vnd.tcpdump.pcap',
			};
		}

		// Sony DSD Stream File (DSF)
		if (this.checkString('DSD ')) {
			return {
				ext: 'dsf',
				mime: 'audio/x-dsf', // Non-standard
			};
		}

		if (this.checkString('LZIP')) {
			return {
				ext: 'lz',
				mime: 'application/lzip',
			};
		}

		if (this.checkString('fLaC')) {
			return {
				ext: 'flac',
				mime: 'audio/flac',
			};
		}

		if (this.check([0x42, 0x50, 0x47, 0xFB])) {
			return {
				ext: 'bpg',
				mime: 'image/bpg',
			};
		}

		if (this.checkString('wvpk')) {
			return {
				ext: 'wv',
				mime: 'audio/wavpack',
			};
		}

		if (this.checkString('%PDF')) {
			// Assume this is just a normal PDF
			return {
				ext: 'pdf',
				mime: 'application/pdf',
			};
		}

		if (this.check([0x00, 0x61, 0x73, 0x6D])) {
			return {
				ext: 'wasm',
				mime: 'application/wasm',
			};
		}

		// TIFF, little-endian type
		if (this.check([0x49, 0x49])) {
			const fileType = await this.readTiffHeader(false);
			if (fileType) {
				return fileType;
			}
		}

		// TIFF, big-endian type
		if (this.check([0x4D, 0x4D])) {
			const fileType = await this.readTiffHeader(true);
			if (fileType) {
				return fileType;
			}
		}

		if (this.checkString('MAC ')) {
			return {
				ext: 'ape',
				mime: 'audio/ape',
			};
		}

		// https://github.com/file/file/blob/master/magic/Magdir/matroska
		if (this.check([0x1A, 0x45, 0xDF, 0xA3])) { // Root element: EBML
			return detectEbml(tokenizer);
		}

		if (this.checkString('SQLi')) {
			return {
				ext: 'sqlite',
				mime: 'application/x-sqlite3',
			};
		}

		if (this.check([0x4E, 0x45, 0x53, 0x1A])) {
			return {
				ext: 'nes',
				mime: 'application/x-nintendo-nes-rom',
			};
		}

		if (this.checkString('Cr24')) {
			return {
				ext: 'crx',
				mime: 'application/x-google-chrome-extension',
			};
		}

		if (
			this.checkString('MSCF')
			|| this.checkString('ISc(')
		) {
			return {
				ext: 'cab',
				mime: 'application/vnd.ms-cab-compressed',
			};
		}

		if (this.check([0xED, 0xAB, 0xEE, 0xDB])) {
			return {
				ext: 'rpm',
				mime: 'application/x-rpm',
			};
		}

		if (this.check([0xC5, 0xD0, 0xD3, 0xC6])) {
			return {
				ext: 'eps',
				mime: 'application/eps',
			};
		}

		if (this.check([0x28, 0xB5, 0x2F, 0xFD])) {
			return {
				ext: 'zst',
				mime: 'application/zstd',
			};
		}

		if (this.check([0x7F, 0x45, 0x4C, 0x46])) {
			return {
				ext: 'elf',
				mime: 'application/x-elf',
			};
		}

		if (this.check([0x21, 0x42, 0x44, 0x4E])) {
			return {
				ext: 'pst',
				mime: 'application/vnd.ms-outlook',
			};
		}

		if (this.checkString('PAR1') || this.checkString('PARE')) {
			return {
				ext: 'parquet',
				mime: 'application/vnd.apache.parquet',
			};
		}

		if (this.checkString('ttcf')) {
			return {
				ext: 'ttc',
				mime: 'font/collection',
			};
		}

		if (
			this.check([0xFE, 0xED, 0xFA, 0xCE]) // 32-bit, big-endian
			|| this.check([0xFE, 0xED, 0xFA, 0xCF]) // 64-bit, big-endian
			|| this.check([0xCE, 0xFA, 0xED, 0xFE]) // 32-bit, little-endian
			|| this.check([0xCF, 0xFA, 0xED, 0xFE]) // 64-bit, little-endian
		) {
			return {
				ext: 'macho',
				mime: 'application/x-mach-binary',
			};
		}

		if (this.check([0x04, 0x22, 0x4D, 0x18])) {
			return {
				ext: 'lz4',
				mime: 'application/x-lz4', // Informal, used by freedesktop.org shared-mime-info
			};
		}

		if (this.checkString('regf')) {
			return {
				ext: 'dat',
				mime: 'application/x-ft-windows-registry-hive',
			};
		}

		// SPSS Statistical Data File
		if (this.checkString('$FL2') || this.checkString('$FL3')) {
			return {
				ext: 'sav',
				mime: 'application/x-spss-sav',
			};
		}

		// -- 5-byte signatures --

		if (this.check([0x4F, 0x54, 0x54, 0x4F, 0x00])) {
			return {
				ext: 'otf',
				mime: 'font/otf',
			};
		}

		if (this.checkString('#!AMR')) {
			return {
				ext: 'amr',
				mime: 'audio/amr',
			};
		}

		if (this.checkString(String.raw`{\rtf`)) {
			return {
				ext: 'rtf',
				mime: 'application/rtf',
			};
		}

		if (this.check([0x46, 0x4C, 0x56, 0x01])) {
			return {
				ext: 'flv',
				mime: 'video/x-flv',
			};
		}

		if (this.checkString('IMPM')) {
			return {
				ext: 'it',
				mime: 'audio/x-it',
			};
		}

		if (
			this.checkString('-lh0-', {offset: 2})
			|| this.checkString('-lh1-', {offset: 2})
			|| this.checkString('-lh2-', {offset: 2})
			|| this.checkString('-lh3-', {offset: 2})
			|| this.checkString('-lh4-', {offset: 2})
			|| this.checkString('-lh5-', {offset: 2})
			|| this.checkString('-lh6-', {offset: 2})
			|| this.checkString('-lh7-', {offset: 2})
			|| this.checkString('-lzs-', {offset: 2})
			|| this.checkString('-lz4-', {offset: 2})
			|| this.checkString('-lz5-', {offset: 2})
			|| this.checkString('-lhd-', {offset: 2})
		) {
			return {
				ext: 'lzh',
				mime: 'application/x-lzh-compressed',
			};
		}

		// MPEG program stream (PS or MPEG-PS)
		if (this.check([0x00, 0x00, 0x01, 0xBA])) {
			//  MPEG-PS, MPEG-1 Part 1
			if (this.check([0x21], {offset: 4, mask: [0xF1]})) {
				return {
					ext: 'mpg', // May also be .ps, .mpeg
					mime: 'video/MP1S',
				};
			}

			// MPEG-PS, MPEG-2 Part 1
			if (this.check([0x44], {offset: 4, mask: [0xC4]})) {
				return {
					ext: 'mpg', // May also be .mpg, .m2p, .vob or .sub
					mime: 'video/MP2P',
				};
			}
		}

		if (this.checkString('ITSF')) {
			return {
				ext: 'chm',
				mime: 'application/vnd.ms-htmlhelp',
			};
		}

		if (this.check([0xCA, 0xFE, 0xBA, 0xBE])) {
			// Java bytecode and Mach-O universal binaries have the same magic number.
			// We disambiguate based on the next 4 bytes, as done by `file`.
			// See https://github.com/file/file/blob/master/magic/Magdir/cafebabe
			const machOArchitectureCount = Token.UINT32_BE.get(this.buffer, 4);
			const javaClassFileMajorVersion = Token.UINT16_BE.get(this.buffer, 6);

			if (machOArchitectureCount > 0 && machOArchitectureCount <= 30) {
				return {
					ext: 'macho',
					mime: 'application/x-mach-binary',
				};
			}

			if (javaClassFileMajorVersion > 30) {
				return {
					ext: 'class',
					mime: 'application/java-vm',
				};
			}
		}

		if (this.checkString('.RMF')) {
			return {
				ext: 'rm',
				mime: 'application/vnd.rn-realmedia',
			};
		}

		// -- 5-byte signatures --

		if (this.checkString('DRACO')) {
			return {
				ext: 'drc',
				mime: 'application/x-ft-draco',
			};
		}

		// -- 6-byte signatures --

		if (this.check([0xFD, 0x37, 0x7A, 0x58, 0x5A, 0x00])) {
			return {
				ext: 'xz',
				mime: 'application/x-xz',
			};
		}

		if (this.checkString('<?xml ')) {
			return {
				ext: 'xml',
				mime: 'application/xml',
			};
		}

		if (this.check([0x37, 0x7A, 0xBC, 0xAF, 0x27, 0x1C])) {
			return {
				ext: '7z',
				mime: 'application/x-7z-compressed',
			};
		}

		if (
			this.check([0x52, 0x61, 0x72, 0x21, 0x1A, 0x7])
			&& (this.buffer[6] === 0x0 || this.buffer[6] === 0x1)
		) {
			return {
				ext: 'rar',
				mime: 'application/x-rar-compressed',
			};
		}

		if (this.checkString('solid ')) {
			return {
				ext: 'stl',
				mime: 'model/stl',
			};
		}

		if (this.checkString('AC')) {
			const version = new Token.StringType(4, 'latin1').get(this.buffer, 2);
			if (/^\d+$/v.test(version) && version >= 1000 && version <= 1050) {
				return {
					ext: 'dwg',
					mime: 'image/vnd.dwg',
				};
			}
		}

		if (this.checkString('070707')) {
			return {
				ext: 'cpio',
				mime: 'application/x-cpio',
			};
		}

		// -- 7-byte signatures --

		if (this.checkString('BLENDER')) {
			return {
				ext: 'blend',
				mime: 'application/x-blender',
			};
		}

		if (this.checkString('!<arch>')) {
			await tokenizer.ignore(8);
			const string = await tokenizer.readToken(new Token.StringType(13, 'ascii'));
			if (string === 'debian-binary') {
				return {
					ext: 'deb',
					mime: 'application/x-deb',
				};
			}

			return {
				ext: 'ar',
				mime: 'application/x-unix-archive',
			};
		}

		if (
			this.checkString('WEBVTT')
			&&	(
				// One of LF, CR, tab, space, or end of file must follow "WEBVTT" per the spec (see `fixture/fixture-vtt-*.vtt` for examples). Note that `\0` is technically the null character (there is no such thing as an EOF character). However, checking for `\0` gives us the same result as checking for the end of the stream.
				(['\n', '\r', '\t', ' ', '\0'].some(char7 => this.checkString(char7, {offset: 6}))))
		) {
			return {
				ext: 'vtt',
				mime: 'text/vtt',
			};
		}

		// -- 8-byte signatures --

		if (this.check([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])) {
			return detectPng(tokenizer);
		}

		if (this.check([0x41, 0x52, 0x52, 0x4F, 0x57, 0x31, 0x00, 0x00])) {
			return {
				ext: 'arrow',
				mime: 'application/vnd.apache.arrow.file',
			};
		}

		if (this.check([0x67, 0x6C, 0x54, 0x46, 0x02, 0x00, 0x00, 0x00])) {
			return {
				ext: 'glb',
				mime: 'model/gltf-binary',
			};
		}

		// `mov` format variants
		if (
			this.check([0x66, 0x72, 0x65, 0x65], {offset: 4}) // `free`
			|| this.check([0x6D, 0x64, 0x61, 0x74], {offset: 4}) // `mdat` MJPEG
			|| this.check([0x6D, 0x6F, 0x6F, 0x76], {offset: 4}) // `moov`
			|| this.check([0x77, 0x69, 0x64, 0x65], {offset: 4}) // `wide`
		) {
			return {
				ext: 'mov',
				mime: 'video/quicktime',
			};
		}

		// -- 9-byte signatures --

		if (this.check([0x49, 0x49, 0x52, 0x4F, 0x08, 0x00, 0x00, 0x00, 0x18])) {
			return {
				ext: 'orf',
				mime: 'image/x-olympus-orf',
			};
		}

		if (this.checkString('gimp xcf ')) {
			return {
				ext: 'xcf',
				mime: 'image/x-xcf',
			};
		}

		// File Type Box (https://en.wikipedia.org/wiki/ISO_base_media_file_format)
		// It's not required to be first, but it's recommended to be. Almost all ISO base media files start with `ftyp` box.
		// `ftyp` box must contain a brand major identifier, which must consist of ISO 8859-1 printable characters.
		// Here we check for 8859-1 printable characters (for simplicity, it's a mask which also catches one non-printable character).
		if (
			this.checkString('ftyp', {offset: 4})
			&& (this.buffer[8] & 0x60) !== 0x00 // Brand major, first character ASCII?
		) {
			// They all can have MIME `video/mp4` except `application/mp4` special-case which is hard to detect.
			// For some cases, we're specific, everything else falls to `video/mp4` with `mp4` extension.
			const brandMajor = new Token.StringType(4, 'latin1').get(this.buffer, 8).replace('\0', ' ').trim();
			switch (brandMajor) {
				case 'avif':
				case 'avis':
					return {ext: 'avif', mime: 'image/avif'};
				case 'mif1':
					return {ext: 'heic', mime: 'image/heif'};
				case 'msf1':
					return {ext: 'heic', mime: 'image/heif-sequence'};
				case 'heic':
				case 'heix':
					return {ext: 'heic', mime: 'image/heic'};
				case 'hevc':
				case 'hevx':
					return {ext: 'heic', mime: 'image/heic-sequence'};
				case 'qt':
					return {ext: 'mov', mime: 'video/quicktime'};
				case 'M4V':
				case 'M4VH':
				case 'M4VP':
					return {ext: 'm4v', mime: 'video/x-m4v'};
				case 'M4P':
					return {ext: 'm4p', mime: 'video/mp4'};
				case 'M4B':
					return {ext: 'm4b', mime: 'audio/mp4'};
				case 'M4A':
					return {ext: 'm4a', mime: 'audio/x-m4a'};
				case 'F4V':
					return {ext: 'f4v', mime: 'video/mp4'};
				case 'F4P':
					return {ext: 'f4p', mime: 'video/mp4'};
				case 'F4A':
					return {ext: 'f4a', mime: 'audio/mp4'};
				case 'F4B':
					return {ext: 'f4b', mime: 'audio/mp4'};
				case 'crx':
					return {ext: 'cr3', mime: 'image/x-canon-cr3'};
				default:
					if (brandMajor.startsWith('3g')) {
						if (brandMajor.startsWith('3g2')) {
							return {ext: '3g2', mime: 'video/3gpp2'};
						}

						return {ext: '3gp', mime: 'video/3gpp'};
					}

					return {ext: 'mp4', mime: 'video/mp4'};
			}
		}

		// -- 10-byte signatures --

		if (this.checkString('REGEDIT4\r\n')) {
			return {
				ext: 'reg',
				mime: 'application/x-ms-regedit',
			};
		}

		// -- 12-byte signatures --

		// RIFF file format which might be AVI, WAV, QCP, etc
		if (this.check([0x52, 0x49, 0x46, 0x46])) {
			if (this.checkString('WEBP', {offset: 8})) {
				return {
					ext: 'webp',
					mime: 'image/webp',
				};
			}

			if (this.check([0x41, 0x56, 0x49], {offset: 8})) {
				return {
					ext: 'avi',
					mime: 'video/vnd.avi',
				};
			}

			if (this.check([0x57, 0x41, 0x56, 0x45], {offset: 8})) {
				return {
					ext: 'wav',
					mime: 'audio/wav',
				};
			}

			// QLCM, QCP file
			if (this.check([0x51, 0x4C, 0x43, 0x4D], {offset: 8})) {
				return {
					ext: 'qcp',
					mime: 'audio/qcelp',
				};
			}
		}

		if (this.check([0x49, 0x49, 0x55, 0x00, 0x18, 0x00, 0x00, 0x00, 0x88, 0xE7, 0x74, 0xD8])) {
			return {
				ext: 'rw2',
				mime: 'image/x-panasonic-rw2',
			};
		}

		// ASF_Header_Object first 80 bytes
		if (this.check([0x30, 0x26, 0xB2, 0x75, 0x8E, 0x66, 0xCF, 0x11, 0xA6, 0xD9])) {
			return detectAsf(tokenizer);
		}

		if (this.check([0xAB, 0x4B, 0x54, 0x58, 0x20, 0x31, 0x31, 0xBB, 0x0D, 0x0A, 0x1A, 0x0A])) {
			return {
				ext: 'ktx',
				mime: 'image/ktx',
			};
		}

		if ((this.check([0x7E, 0x10, 0x04]) || this.check([0x7E, 0x18, 0x04])) && this.check([0x30, 0x4D, 0x49, 0x45], {offset: 4})) {
			return {
				ext: 'mie',
				mime: 'application/x-mie',
			};
		}

		if (this.check([0x27, 0x0A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], {offset: 2})) {
			return {
				ext: 'shp',
				mime: 'application/x-esri-shape',
			};
		}

		if (this.check([0xFF, 0x4F, 0xFF, 0x51])) {
			return {
				ext: 'j2c',
				mime: 'image/j2c',
			};
		}

		if (this.check([0x00, 0x00, 0x00, 0x0C, 0x6A, 0x50, 0x20, 0x20, 0x0D, 0x0A, 0x87, 0x0A])) {
			// JPEG-2000 family

			await tokenizer.ignore(20);
			const type = await tokenizer.readToken(new Token.StringType(4, 'ascii'));
			switch (type) {
				case 'jp2 ':
					return {
						ext: 'jp2',
						mime: 'image/jp2',
					};
				case 'jpx ':
					return {
						ext: 'jpx',
						mime: 'image/jpx',
					};
				case 'jpm ':
					return {
						ext: 'jpm',
						mime: 'image/jpm',
					};
				case 'mjp2':
					return {
						ext: 'mj2',
						mime: 'image/mj2',
					};
				default:
					return;
			}
		}

		if (
			this.check([0xFF, 0x0A])
			|| this.check([0x00, 0x00, 0x00, 0x0C, 0x4A, 0x58, 0x4C, 0x20, 0x0D, 0x0A, 0x87, 0x0A])
		) {
			return {
				ext: 'jxl',
				mime: 'image/jxl',
			};
		}

		if (this.check([0xFE, 0xFF])) { // UTF-16-BOM-BE
			if (this.checkString('<?xml ', {offset: 2, encoding: 'utf-16be'})) {
				return {
					ext: 'xml',
					mime: 'application/xml',
				};
			}

			return undefined; // Some unknown text based format
		}

		if (this.check([0xD0, 0xCF, 0x11, 0xE0, 0xA1, 0xB1, 0x1A, 0xE1])) {
			// Detected Microsoft Compound File Binary File (MS-CFB) Format.
			return {
				ext: 'cfb',
				mime: 'application/x-cfb',
			};
		}

		// Increase sample size from 32 to 256.
		await tokenizer.peekBuffer(this.buffer, {length: Math.min(256, tokenizer.fileInfo.size), mayBeLess: true});

		if (this.check([0x61, 0x63, 0x73, 0x70], {offset: 36})) {
			return {
				ext: 'icc',
				mime: 'application/vnd.iccprofile',
			};
		}

		// ACE: requires 14 bytes in the buffer
		if (this.checkString('**ACE', {offset: 7}) && this.checkString('**', {offset: 12})) {
			return {
				ext: 'ace',
				mime: 'application/x-ace-compressed',
			};
		}

		// -- 15-byte signatures --

		if (this.checkString('BEGIN:')) {
			if (this.checkString('VCARD', {offset: 6})) {
				return {
					ext: 'vcf',
					mime: 'text/vcard',
				};
			}

			if (this.checkString('VCALENDAR', {offset: 6})) {
				return {
					ext: 'ics',
					mime: 'text/calendar',
				};
			}
		}

		// `raf` is here just to keep all the raw image detectors together.
		if (this.checkString('FUJIFILMCCD-RAW')) {
			return {
				ext: 'raf',
				mime: 'image/x-fujifilm-raf',
			};
		}

		if (this.checkString('Extended Module:')) {
			return {
				ext: 'xm',
				mime: 'audio/x-xm',
			};
		}

		if (this.checkString('Creative Voice File')) {
			return {
				ext: 'voc',
				mime: 'audio/x-voc',
			};
		}

		if (this.check([0x04, 0x00, 0x00, 0x00]) && this.buffer.length >= 16) { // Rough & quick check Pickle/ASAR
			const jsonSize = new DataView(this.buffer.buffer).getUint32(12, true);

			if (jsonSize > 12 && this.buffer.length >= jsonSize + 16) {
				try {
					const header = new TextDecoder().decode(this.buffer.subarray(16, jsonSize + 16));
					const json = JSON.parse(header);
					// Check if Pickle is ASAR
					if (json.files) { // Final check, assuring Pickle/ASAR format
						return {
							ext: 'asar',
							mime: 'application/x-asar',
						};
					}
				} catch {}
			}
		}

		if (this.check([0x06, 0x0E, 0x2B, 0x34, 0x02, 0x05, 0x01, 0x01, 0x0D, 0x01, 0x02, 0x01, 0x01, 0x02])) {
			return {
				ext: 'mxf',
				mime: 'application/mxf',
			};
		}

		if (this.checkString('SCRM', {offset: 44})) {
			return {
				ext: 's3m',
				mime: 'audio/x-s3m',
			};
		}

		// Raw MPEG-2 transport stream (188-byte packets)
		if (this.check([0x47]) && this.check([0x47], {offset: 188})) {
			return {
				ext: 'mts',
				mime: 'video/mp2t',
			};
		}

		// Blu-ray Disc Audio-Video (BDAV) MPEG-2 transport stream has 4-byte TP_extra_header before each 188-byte packet
		if (this.check([0x47], {offset: 4}) && this.check([0x47], {offset: 196})) {
			return {
				ext: 'mts',
				mime: 'video/mp2t',
			};
		}

		if (this.check([0x42, 0x4F, 0x4F, 0x4B, 0x4D, 0x4F, 0x42, 0x49], {offset: 60})) {
			return {
				ext: 'mobi',
				mime: 'application/x-mobipocket-ebook',
			};
		}

		if (this.check([0x44, 0x49, 0x43, 0x4D], {offset: 128})) {
			return {
				ext: 'dcm',
				mime: 'application/dicom',
			};
		}

		if (this.check([0x4C, 0x00, 0x00, 0x00, 0x01, 0x14, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0xC0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x46])) {
			return {
				ext: 'lnk',
				mime: 'application/x-ms-shortcut', // Informal, used by freedesktop.org shared-mime-info
			};
		}

		if (this.check([0x62, 0x6F, 0x6F, 0x6B, 0x00, 0x00, 0x00, 0x00, 0x6D, 0x61, 0x72, 0x6B, 0x00, 0x00, 0x00, 0x00])) {
			return {
				ext: 'alias',
				mime: 'application/x-ft-apple.alias',
			};
		}

		if (this.checkString('Kaydara FBX Binary  \u0000')) {
			return {
				ext: 'fbx',
				mime: 'application/x-ft-fbx',
			};
		}

		if (
			this.check([0x4C, 0x50], {offset: 34})
			&& (
				this.check([0x00, 0x00, 0x01], {offset: 8})
				|| this.check([0x01, 0x00, 0x02], {offset: 8})
				|| this.check([0x02, 0x00, 0x02], {offset: 8})
			)
		) {
			return {
				ext: 'eot',
				mime: 'application/vnd.ms-fontobject',
			};
		}

		if (this.check([0x06, 0x06, 0xED, 0xF5, 0xD8, 0x1D, 0x46, 0xE5, 0xBD, 0x31, 0xEF, 0xE7, 0xFE, 0x74, 0xB7, 0x1D])) {
			return {
				ext: 'indd',
				mime: 'application/x-indesign',
			};
		}

		// -- 16-byte signatures --

		// JMP files - check for both Little Endian and Big Endian signatures
		if (this.check([0xFF, 0xFF, 0x00, 0x00, 0x07, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x01, 0x00, 0x01, 0x00])
			|| this.check([0x00, 0x00, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x07, 0x00, 0x00, 0x00, 0x04, 0x00, 0x01, 0x00, 0x01])) {
			return {
				ext: 'jmp',
				mime: 'application/x-jmp-data',
			};
		}

		// Increase sample size from 256 to 512
		await tokenizer.peekBuffer(this.buffer, {length: Math.min(512, tokenizer.fileInfo.size), mayBeLess: true});

		// Requires a buffer size of 512 bytes
		if ((this.checkString('ustar', {offset: 257}) && (this.checkString('\0', {offset: 262}) || this.checkString(' ', {offset: 262})))
			|| (this.check([0, 0, 0, 0, 0, 0], {offset: 257}) && tarHeaderChecksumMatches(this.buffer))) {
			return {
				ext: 'tar',
				mime: 'application/x-tar',
			};
		}

		if (this.check([0xFF, 0xFE])) { // UTF-16-BOM-LE
			const encoding = 'utf-16le';
			if (this.checkString('<?xml ', {offset: 2, encoding})) {
				return {
					ext: 'xml',
					mime: 'application/xml',
				};
			}

			if (this.check([0xFF, 0x0E], {offset: 2}) && this.checkString('SketchUp Model', {offset: 4, encoding})) {
				return {
					ext: 'skp',
					mime: 'application/vnd.sketchup.skp',
				};
			}

			if (this.checkString('Windows Registry Editor Version 5.00\r\n', {offset: 2, encoding})) {
				return {
					ext: 'reg',
					mime: 'application/x-ms-regedit',
				};
			}

			return undefined; // Some text based format
		}

		if (this.checkString('-----BEGIN PGP MESSAGE-----')) {
			return {
				ext: 'pgp',
				mime: 'application/pgp-encrypted',
			};
		}
	};
	// Detections with limited supporting data, resulting in a higher likelihood of false positives
	detectImprecise = async tokenizer => {
		this.buffer = new Uint8Array(reasonableDetectionSizeInBytes);
		const fileSize = getKnownFileSizeOrMaximum(tokenizer.fileInfo.size);

		// Read initial sample size of 8 bytes
		await tokenizer.peekBuffer(this.buffer, {length: Math.min(8, fileSize), mayBeLess: true});

		if (
			this.check([0x0, 0x0, 0x1, 0xBA])
			|| this.check([0x0, 0x0, 0x1, 0xB3])
		) {
			return {
				ext: 'mpg',
				mime: 'video/mpeg',
			};
		}

		if (this.check([0x00, 0x01, 0x00, 0x00, 0x00])) {
			return {
				ext: 'ttf',
				mime: 'font/ttf',
			};
		}

		if (this.check([0x00, 0x00, 0x01, 0x00])) {
			return {
				ext: 'ico',
				mime: 'image/x-icon',
			};
		}

		if (this.check([0x00, 0x00, 0x02, 0x00])) {
			return {
				ext: 'cur',
				mime: 'image/x-icon',
			};
		}

		// Adjust buffer to `mpegOffsetTolerance`
		await tokenizer.peekBuffer(this.buffer, {length: Math.min(2 + this.options.mpegOffsetTolerance, fileSize), mayBeLess: true});

		// Check MPEG 1 or 2 Layer 3 header, or 'layer 0' for ADTS (MPEG sync-word 0xFFE)
		if (this.buffer.length >= (2 + this.options.mpegOffsetTolerance)) {
			for (let depth = 0; depth <= this.options.mpegOffsetTolerance; ++depth) {
				const type = this.scanMpeg(depth);
				if (type) {
					return type;
				}
			}
		}
	};

	async readTiffTag(bigEndian) {
		const tagId = await this.tokenizer.readToken(bigEndian ? Token.UINT16_BE : Token.UINT16_LE);
		await this.tokenizer.ignore(10);
		switch (tagId) {
			case 50_341:
				return {
					ext: 'arw',
					mime: 'image/x-sony-arw',
				};
			case 50_706:
				return {
					ext: 'dng',
					mime: 'image/x-adobe-dng',
				};
			default:
		}
	}

	async readTiffIFD(bigEndian) {
		const numberOfTags = await this.tokenizer.readToken(bigEndian ? Token.UINT16_BE : Token.UINT16_LE);
		if (numberOfTags > maximumTiffTagCount) {
			return;
		}

		if (
			hasUnknownFileSize(this.tokenizer)
			&& (2 + (numberOfTags * 12)) > maximumTiffIfdOffsetInBytes
		) {
			return;
		}

		for (let n = 0; n < numberOfTags; ++n) {
			const fileType = await this.readTiffTag(bigEndian);
			if (fileType) {
				return fileType;
			}
		}
	}

	async readTiffHeader(bigEndian) {
		const tiffFileType = {
			ext: 'tif',
			mime: 'image/tiff',
		};

		const version = (bigEndian ? Token.UINT16_BE : Token.UINT16_LE).get(this.buffer, 2);
		const ifdOffset = (bigEndian ? Token.UINT32_BE : Token.UINT32_LE).get(this.buffer, 4);

		if (version === 42) {
			// TIFF file header
			if (ifdOffset >= 6) {
				if (this.checkString('CR', {offset: 8})) {
					return {
						ext: 'cr2',
						mime: 'image/x-canon-cr2',
					};
				}

				if (ifdOffset >= 8) {
					const someId1 = (bigEndian ? Token.UINT16_BE : Token.UINT16_LE).get(this.buffer, 8);
					const someId2 = (bigEndian ? Token.UINT16_BE : Token.UINT16_LE).get(this.buffer, 10);

					if (
						(someId1 === 0x1C && someId2 === 0xFE)
						|| (someId1 === 0x1F && someId2 === 0x0B)) {
						return {
							ext: 'nef',
							mime: 'image/x-nikon-nef',
						};
					}
				}
			}

			if (
				hasUnknownFileSize(this.tokenizer)
				&& ifdOffset > maximumTiffStreamIfdOffsetInBytes
			) {
				return tiffFileType;
			}

			const maximumTiffOffset = hasUnknownFileSize(this.tokenizer) ? maximumTiffIfdOffsetInBytes : this.tokenizer.fileInfo.size;

			try {
				await safeIgnore(this.tokenizer, ifdOffset, {
					maximumLength: maximumTiffOffset,
					reason: 'TIFF IFD offset',
				});
			} catch (error) {
				if (error instanceof strtok3.EndOfStreamError) {
					return;
				}

				throw error;
			}

			let fileType;
			try {
				fileType = await this.readTiffIFD(bigEndian);
			} catch (error) {
				if (error instanceof strtok3.EndOfStreamError) {
					return;
				}

				throw error;
			}

			return fileType ?? tiffFileType;
		}

		if (version === 43) {	// Big TIFF file header
			return tiffFileType;
		}
	}

	/**
	Scan check MPEG 1 or 2 Layer 3 header, or 'layer 0' for ADTS (MPEG sync-word 0xFFE).

	@param offset - Offset to scan for sync-preamble.
	@returns {{ext: string, mime: string}}
	*/
	scanMpeg(offset) {
		if (this.check([0xFF, 0xE0], {offset, mask: [0xFF, 0xE0]})) {
			if (this.check([0x10], {offset: offset + 1, mask: [0x16]})) {
				// Check for (ADTS) MPEG-2
				if (this.check([0x08], {offset: offset + 1, mask: [0x08]})) {
					return {
						ext: 'aac',
						mime: 'audio/aac',
					};
				}

				// Must be (ADTS) MPEG-4
				return {
					ext: 'aac',
					mime: 'audio/aac',
				};
			}

			// MPEG 1 or 2 Layer 3 header
			// Check for MPEG layer 3
			if (this.check([0x02], {offset: offset + 1, mask: [0x06]})) {
				return {
					ext: 'mp3',
					mime: 'audio/mpeg',
				};
			}

			// Check for MPEG layer 2
			if (this.check([0x04], {offset: offset + 1, mask: [0x06]})) {
				return {
					ext: 'mp2',
					mime: 'audio/mpeg',
				};
			}

			// Check for MPEG layer 1
			if (this.check([0x06], {offset: offset + 1, mask: [0x06]})) {
				return {
					ext: 'mp1',
					mime: 'audio/mpeg',
				};
			}
		}
	}
}

export const supportedExtensions = new Set(extensions);
export const supportedMimeTypes = new Set(mimeTypes);

export async function fileTypeFromFile(path, options) {
	return (new FileTypeParser(options)).fromFile(path);
}
```

## File: `source/index.test-d.ts`
```typescript
import {ReadableStream as NodeReadableStream} from 'node:stream/web';
import {expectType} from 'tsd';
import {
	type FileTypeResult,
	type FileTypeResult as FileTypeResultBrowser,
	type AnyWebReadableByteStreamWithFileType,
	fileTypeFromBlob,
	fileTypeFromBuffer,
	fileTypeFromFile,
	fileTypeFromStream,
	fileTypeStream,
	FileTypeParser,
} from './index.js';

// `fileTypeStream`: accepts StreamOptions & FileTypeOptions
(async () => {
	const webStream = new ReadableStream<Uint8Array>();
	expectType<AnyWebReadableByteStreamWithFileType>(await fileTypeStream(webStream, {sampleSize: 256}));
	expectType<AnyWebReadableByteStreamWithFileType>(await fileTypeStream(webStream, {sampleSize: 256, customDetectors: []}));
	expectType<AnyWebReadableByteStreamWithFileType>(await fileTypeStream(webStream, {signal: AbortSignal.timeout(1000)}));
})();

// `FileTypeParser`: tests generic input types and options
(async () => {
	const fileTypeParser = new FileTypeParser({customDetectors: [], signal: AbortSignal.timeout(1000)});
	const fileTypeParserWithMpeg = new FileTypeParser({mpegOffsetTolerance: 10});
	const webStream = new ReadableStream<Uint8Array>();
	const nodeWebStream = new NodeReadableStream<Uint8Array>();

	expectType<FileTypeResult | undefined>(await fileTypeParser.fromStream(webStream));
	expectType<FileTypeResult | undefined>(await fileTypeParser.fromStream(nodeWebStream));

	expectType<AnyWebReadableByteStreamWithFileType>(await fileTypeParser.toDetectionStream(webStream, {sampleSize: 256}));
})();

// `fileTypeFromStream`: accepts FileTypeOptions
(async () => {
	const webStream = new ReadableStream<Uint8Array>();
	expectType<FileTypeResult | undefined>(await fileTypeFromStream(webStream, {signal: AbortSignal.timeout(1000)}));
})();

// Test that Blob overload returns browser-specific result
expectType<Promise<FileTypeResultBrowser | undefined>>(fileTypeFromBlob(new Blob([])));

// `fileTypeFromFile`: accepts a file path and options
expectType<Promise<FileTypeResult | undefined>>(fileTypeFromFile('file.bin'));
expectType<Promise<FileTypeResult | undefined>>(fileTypeFromFile('file.bin', {signal: AbortSignal.timeout(1000)}));

// `FileTypeParser#fromFile`: accepts a file path
(async () => {
	const fileTypeParser = new FileTypeParser();
	expectType<Promise<FileTypeResult | undefined>>(fileTypeParser.fromFile('file.bin'));
})();
```

## File: `source/parser.js`
```javascript
export const maximumUntrustedSkipSizeInBytes = 16 * 1024 * 1024;

export class ParserHardLimitError extends Error {}

export function getSafeBound(value, maximum, reason) {
	if (
		!Number.isFinite(value)
		|| value < 0
		|| value > maximum
	) {
		throw new ParserHardLimitError(`${reason} has invalid size ${value} (maximum ${maximum} bytes)`);
	}

	return value;
}

export async function safeIgnore(tokenizer, length, {maximumLength = maximumUntrustedSkipSizeInBytes, reason = 'skip'} = {}) {
	const safeLength = getSafeBound(length, maximumLength, reason);
	await tokenizer.ignore(safeLength);
}

export async function safeReadBuffer(tokenizer, buffer, options, {maximumLength = buffer.length, reason = 'read'} = {}) {
	const length = options?.length ?? buffer.length;
	const safeLength = getSafeBound(length, maximumLength, reason);
	return tokenizer.readBuffer(buffer, {
		...options,
		length: safeLength,
	});
}

export function checkBytes(buffer, headers, options) {
	options = {
		offset: 0,
		...options,
	};

	for (const [index, header] of headers.entries()) {
		// If a bitmask is set
		if (options.mask) {
			// If header doesn't equal `buf` with bits masked off
			if (header !== (options.mask[index] & buffer[index + options.offset])) {
				return false;
			}
		} else if (header !== buffer[index + options.offset]) {
			return false;
		}
	}

	return true;
}

export function hasUnknownFileSize(tokenizer) {
	const fileSize = tokenizer.fileInfo.size;
	return (
		!Number.isFinite(fileSize)
		|| fileSize === Number.MAX_SAFE_INTEGER
	);
}

export function hasExceededUnknownSizeScanBudget(tokenizer, startOffset, maximumBytes) {
	return (
		hasUnknownFileSize(tokenizer)
		&& tokenizer.position - startOffset > maximumBytes
	);
}
```

## File: `source/supported.js`
```javascript
// MIME media subtypes prefixed with `x-ft-` are custom and defined by us. They are neither formally registered with IANA nor based on any informal conventions.

export const extensions = [
	'jpg',
	'png',
	'apng',
	'gif',
	'webp',
	'flif',
	'xcf',
	'cr2',
	'cr3',
	'orf',
	'arw',
	'dng',
	'nef',
	'rw2',
	'raf',
	'tif',
	'bmp',
	'icns',
	'jxr',
	'psd',
	'indd',
	'zip',
	'tar',
	'rar',
	'gz',
	'bz2',
	'7z',
	'dmg',
	'mp4',
	'mid',
	'mkv',
	'webm',
	'mov',
	'avi',
	'mpg',
	'mp2',
	'mp3',
	'm4a',
	'oga',
	'ogg',
	'ogv',
	'opus',
	'flac',
	'wav',
	'spx',
	'amr',
	'pdf',
	'epub',
	'elf',
	'macho',
	'exe',
	'swf',
	'rtf',
	'wasm',
	'woff',
	'woff2',
	'eot',
	'ttf',
	'otf',
	'ttc',
	'ico',
	'flv',
	'ps',
	'xz',
	'sqlite',
	'nes',
	'crx',
	'xpi',
	'cab',
	'deb',
	'ar',
	'rpm',
	'Z',
	'lz',
	'cfb',
	'mxf',
	'mts',
	'blend',
	'bpg',
	'docx',
	'pptx',
	'xlsx',
	'3gp',
	'3g2',
	'j2c',
	'jp2',
	'jpm',
	'jpx',
	'mj2',
	'aif',
	'qcp',
	'odt',
	'ods',
	'odp',
	'xml',
	'mobi',
	'heic',
	'cur',
	'ktx',
	'ape',
	'wv',
	'dcm',
	'ics',
	'glb',
	'pcap',
	'dsf',
	'lnk',
	'alias',
	'voc',
	'ac3',
	'm4v',
	'm4p',
	'm4b',
	'f4v',
	'f4p',
	'f4b',
	'f4a',
	'mie',
	'asf',
	'ogm',
	'ogx',
	'mpc',
	'arrow',
	'shp',
	'aac',
	'mp1',
	'it',
	's3m',
	'xm',
	'skp',
	'avif',
	'eps',
	'lzh',
	'pgp',
	'asar',
	'stl',
	'chm',
	'3mf',
	'zst',
	'jxl',
	'vcf',
	'jls',
	'pst',
	'dwg',
	'parquet',
	'class',
	'arj',
	'cpio',
	'ace',
	'avro',
	'icc',
	'fbx',
	'vsdx',
	'vtt',
	'apk',
	'drc',
	'lz4',
	'potx',
	'xltx',
	'dotx',
	'xltm',
	'ott',
	'ots',
	'otp',
	'odg',
	'otg',
	'xlsm',
	'docm',
	'dotm',
	'potm',
	'pptm',
	'jar',
	'jmp',
	'rm',
	'sav',
	'ppsm',
	'ppsx',
	'tar.gz',
	'reg',
	'dat',
	'key',
	'numbers',
	'pages',
];

export const mimeTypes = [
	'image/jpeg',
	'image/png',
	'image/gif',
	'image/webp',
	'image/flif',
	'image/x-xcf',
	'image/x-canon-cr2',
	'image/x-canon-cr3',
	'image/tiff',
	'image/bmp',
	'image/vnd.ms-photo',
	'image/vnd.adobe.photoshop',
	'application/x-indesign',
	'application/epub+zip',
	'application/x-xpinstall',
	'application/vnd.ms-powerpoint.slideshow.macroenabled.12',
	'application/vnd.oasis.opendocument.text',
	'application/vnd.oasis.opendocument.spreadsheet',
	'application/vnd.oasis.opendocument.presentation',
	'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
	'application/vnd.openxmlformats-officedocument.presentationml.presentation',
	'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
	'application/vnd.openxmlformats-officedocument.presentationml.slideshow',
	'application/zip',
	'application/x-tar',
	'application/x-rar-compressed',
	'application/gzip',
	'application/x-bzip2',
	'application/x-7z-compressed',
	'application/x-apple-diskimage',
	'application/vnd.apache.arrow.file',
	'video/mp4',
	'audio/midi',
	'video/matroska',
	'video/webm',
	'video/quicktime',
	'video/vnd.avi',
	'audio/wav',
	'audio/qcelp',
	'audio/x-ms-asf',
	'video/x-ms-asf',
	'application/vnd.ms-asf',
	'video/mpeg',
	'video/3gpp',
	'audio/mpeg',
	'audio/mp4', // RFC 4337
	'video/ogg',
	'audio/ogg',
	'audio/ogg; codecs=opus',
	'application/ogg',
	'audio/flac',
	'audio/ape',
	'audio/wavpack',
	'audio/amr',
	'application/pdf',
	'application/x-elf',
	'application/x-mach-binary',
	'application/x-msdownload',
	'application/x-shockwave-flash',
	'application/rtf',
	'application/wasm',
	'font/woff',
	'font/woff2',
	'application/vnd.ms-fontobject',
	'font/ttf',
	'font/otf',
	'font/collection',
	'image/x-icon',
	'video/x-flv',
	'application/postscript',
	'application/eps',
	'application/x-xz',
	'application/x-sqlite3',
	'application/x-nintendo-nes-rom',
	'application/x-google-chrome-extension',
	'application/vnd.ms-cab-compressed',
	'application/x-deb',
	'application/x-unix-archive',
	'application/x-rpm',
	'application/x-compress',
	'application/lzip',
	'application/x-cfb',
	'application/x-mie',
	'application/mxf',
	'video/mp2t',
	'application/x-blender',
	'image/bpg',
	'image/j2c',
	'image/jp2',
	'image/jpx',
	'image/jpm',
	'image/mj2',
	'audio/aiff',
	'application/xml',
	'application/x-mobipocket-ebook',
	'image/heif',
	'image/heif-sequence',
	'image/heic',
	'image/heic-sequence',
	'image/icns',
	'image/ktx',
	'application/dicom',
	'audio/x-musepack',
	'text/calendar',
	'text/vcard',
	'text/vtt',
	'model/gltf-binary',
	'application/vnd.tcpdump.pcap',
	'audio/x-dsf', // Non-standard
	'application/x-ms-shortcut', // Informal, used by freedesktop.org shared-mime-info
	'application/x-ft-apple.alias',
	'audio/x-voc',
	'audio/vnd.dolby.dd-raw',
	'audio/x-m4a',
	'image/apng',
	'image/x-olympus-orf',
	'image/x-sony-arw',
	'image/x-adobe-dng',
	'image/x-nikon-nef',
	'image/x-panasonic-rw2',
	'image/x-fujifilm-raf',
	'video/x-m4v',
	'video/3gpp2',
	'application/x-esri-shape',
	'audio/aac',
	'audio/x-it',
	'audio/x-s3m',
	'audio/x-xm',
	'video/MP1S',
	'video/MP2P',
	'application/vnd.sketchup.skp',
	'image/avif',
	'application/x-lzh-compressed',
	'application/pgp-encrypted',
	'application/x-asar',
	'model/stl',
	'application/vnd.ms-htmlhelp',
	'model/3mf',
	'image/jxl',
	'application/zstd',
	'image/jls',
	'application/vnd.ms-outlook',
	'image/vnd.dwg',
	'application/vnd.apache.parquet',
	'application/java-vm',
	'application/x-arj',
	'application/x-cpio',
	'application/x-ace-compressed',
	'application/avro',
	'application/vnd.iccprofile',
	'application/x-ft-fbx',
	'application/vnd.visio',
	'application/vnd.android.package-archive',
	'application/x-ft-draco',
	'application/x-lz4', // Informal, used by freedesktop.org shared-mime-info
	'application/vnd.openxmlformats-officedocument.presentationml.template',
	'application/vnd.openxmlformats-officedocument.spreadsheetml.template',
	'application/vnd.openxmlformats-officedocument.wordprocessingml.template',
	'application/vnd.ms-excel.template.macroenabled.12',
	'application/vnd.oasis.opendocument.text-template',
	'application/vnd.oasis.opendocument.spreadsheet-template',
	'application/vnd.oasis.opendocument.presentation-template',
	'application/vnd.oasis.opendocument.graphics',
	'application/vnd.oasis.opendocument.graphics-template',
	'application/vnd.ms-excel.sheet.macroenabled.12',
	'application/vnd.ms-word.document.macroenabled.12',
	'application/vnd.ms-word.template.macroenabled.12',
	'application/vnd.ms-powerpoint.template.macroenabled.12',
	'application/vnd.ms-powerpoint.presentation.macroenabled.12',
	'application/java-archive',
	'application/vnd.rn-realmedia',
	'application/x-spss-sav',
	'application/x-ms-regedit',
	'application/x-ft-windows-registry-hive',
	'application/x-jmp-data',
	'application/vnd.apple.keynote',
	'application/vnd.apple.numbers',
	'application/vnd.apple.pages',
];
```

## File: `source/tokens.js`
```javascript
import {StringType} from 'token-types';

export function stringToBytes(string, encoding) {
	if (encoding === 'utf-16le') {
		const bytes = [];
		for (let index = 0; index < string.length; index++) {
			const code = string.charCodeAt(index); // eslint-disable-line unicorn/prefer-code-point
			bytes.push(code & 0xFF, (code >> 8) & 0xFF); // High byte
		}

		return bytes;
	}

	if (encoding === 'utf-16be') {
		const bytes = [];
		for (let index = 0; index < string.length; index++) {
			const code = string.charCodeAt(index); // eslint-disable-line unicorn/prefer-code-point
			bytes.push((code >> 8) & 0xFF, code & 0xFF); // Low byte
		}

		return bytes;
	}

	return [...string].map(character => character.charCodeAt(0)); // eslint-disable-line unicorn/prefer-code-point
}

/**
Checks whether the TAR checksum is valid.

@param {Uint8Array} arrayBuffer - The TAR header `[offset ... offset + 512]`.
@param {number} offset - TAR header offset.
@returns {boolean} `true` if the TAR checksum is valid, otherwise `false`.
*/
export function tarHeaderChecksumMatches(arrayBuffer, offset = 0) {
	const readSum = Number.parseInt(new StringType(6).get(arrayBuffer, 148).replace(/\0.*$/v, '').trim(), 8); // Read sum in header
	if (Number.isNaN(readSum)) {
		return false;
	}

	let sum = 8 * 0x20; // Initialize signed bit sum

	for (let index = offset; index < offset + 148; index++) {
		sum += arrayBuffer[index];
	}

	for (let index = offset + 156; index < offset + 512; index++) {
		sum += arrayBuffer[index];
	}

	return readSum === sum;
}

/**
ID3 UINT32 sync-safe tokenizer token.
28 bits (representing up to 256MB) integer, the msb is 0 to avoid "false syncsignals".
*/
export const uint32SyncSafeToken = {
	get: (buffer, offset) => (buffer[offset + 3] & 0x7F) | ((buffer[offset + 2] & 0x7F) << 7) | ((buffer[offset + 1] & 0x7F) << 14) | ((buffer[offset] & 0x7F) << 21),
	len: 4,
};
```

## File: `source/detectors/asf.js`
```javascript
import * as Token from 'token-types';
import * as strtok3 from 'strtok3/core';
import {
	maximumUntrustedSkipSizeInBytes,
	ParserHardLimitError,
	checkBytes,
	safeReadBuffer,
	safeIgnore,
	hasUnknownFileSize,
	hasExceededUnknownSizeScanBudget,
} from '../parser.js';

const maximumAsfHeaderObjectCount = 512;
const maximumAsfHeaderPayloadSizeInBytes = 1024 * 1024;

export async function detectAsf(tokenizer) {
	let isMalformedAsf = false;
	try {
		async function readHeader() {
			const guid = new Uint8Array(16);
			await safeReadBuffer(tokenizer, guid, undefined, {
				maximumLength: guid.length,
				reason: 'ASF header GUID',
			});
			return {
				id: guid,
				size: Number(await tokenizer.readToken(Token.UINT64_LE)),
			};
		}

		await safeIgnore(tokenizer, 30, {
			maximumLength: 30,
			reason: 'ASF header prelude',
		});
		const isUnknownFileSize = hasUnknownFileSize(tokenizer);
		const asfHeaderScanStart = tokenizer.position;
		let asfHeaderObjectCount = 0;
		while (tokenizer.position + 24 < tokenizer.fileInfo.size) {
			asfHeaderObjectCount++;
			if (asfHeaderObjectCount > maximumAsfHeaderObjectCount) {
				break;
			}

			if (hasExceededUnknownSizeScanBudget(tokenizer, asfHeaderScanStart, maximumUntrustedSkipSizeInBytes)) {
				break;
			}

			const previousPosition = tokenizer.position;
			const header = await readHeader();
			let payload = header.size - 24;
			if (
				!Number.isFinite(payload)
				|| payload < 0
			) {
				isMalformedAsf = true;
				break;
			}

			if (checkBytes(header.id, [0x91, 0x07, 0xDC, 0xB7, 0xB7, 0xA9, 0xCF, 0x11, 0x8E, 0xE6, 0x00, 0xC0, 0x0C, 0x20, 0x53, 0x65])) {
				// Sync on Stream-Properties-Object (B7DC0791-A9B7-11CF-8EE6-00C00C205365)
				const typeId = new Uint8Array(16);
				payload -= await safeReadBuffer(tokenizer, typeId, undefined, {
					maximumLength: typeId.length,
					reason: 'ASF stream type GUID',
				});

				if (checkBytes(typeId, [0x40, 0x9E, 0x69, 0xF8, 0x4D, 0x5B, 0xCF, 0x11, 0xA8, 0xFD, 0x00, 0x80, 0x5F, 0x5C, 0x44, 0x2B])) {
					// Found audio:
					return {
						ext: 'asf',
						mime: 'audio/x-ms-asf',
					};
				}

				if (checkBytes(typeId, [0xC0, 0xEF, 0x19, 0xBC, 0x4D, 0x5B, 0xCF, 0x11, 0xA8, 0xFD, 0x00, 0x80, 0x5F, 0x5C, 0x44, 0x2B])) {
					// Found video:
					return {
						ext: 'asf',
						mime: 'video/x-ms-asf',
					};
				}

				break;
			}

			if (
				isUnknownFileSize
				&& payload > maximumAsfHeaderPayloadSizeInBytes
			) {
				isMalformedAsf = true;
				break;
			}

			await safeIgnore(tokenizer, payload, {
				maximumLength: isUnknownFileSize ? maximumAsfHeaderPayloadSizeInBytes : tokenizer.fileInfo.size,
				reason: 'ASF header payload',
			});

			// Safeguard against malformed files: break if the position did not advance.
			if (tokenizer.position <= previousPosition) {
				isMalformedAsf = true;
				break;
			}
		}
	} catch (error) {
		if (
			error instanceof strtok3.EndOfStreamError
			|| error instanceof ParserHardLimitError
		) {
			if (hasUnknownFileSize(tokenizer)) {
				isMalformedAsf = true;
			}
		} else {
			throw error;
		}
	}

	if (isMalformedAsf) {
		return;
	}

	// Default to ASF generic extension
	return {
		ext: 'asf',
		mime: 'application/vnd.ms-asf',
	};
}
```

## File: `source/detectors/ebml.js`
```javascript
import * as Token from 'token-types';
import {getUintBE} from 'uint8array-extras';
import {
	maximumUntrustedSkipSizeInBytes,
	getSafeBound,
	safeReadBuffer,
	safeIgnore,
	hasUnknownFileSize,
	hasExceededUnknownSizeScanBudget,
} from '../parser.js';

const maximumEbmlDocumentTypeSizeInBytes = 64;
const maximumEbmlElementPayloadSizeInBytes = 1024 * 1024;
const maximumEbmlElementCount = 256;

export async function detectEbml(tokenizer) {
	async function readField() {
		const msb = await tokenizer.peekNumber(Token.UINT8);
		let mask = 0x80;
		let ic = 0; // 0 = A, 1 = B, 2 = C, 3 = D

		while ((msb & mask) === 0 && mask !== 0) {
			++ic;
			mask >>= 1;
		}

		const id = new Uint8Array(ic + 1);
		await safeReadBuffer(tokenizer, id, undefined, {
			maximumLength: id.length,
			reason: 'EBML field',
		});
		return id;
	}

	async function readElement() {
		const idField = await readField();
		const lengthField = await readField();

		lengthField[0] ^= 0x80 >> (lengthField.length - 1);
		const nrLength = Math.min(6, lengthField.length); // JavaScript can max read 6 bytes integer

		const idView = new DataView(idField.buffer);
		const lengthView = new DataView(lengthField.buffer, lengthField.length - nrLength, nrLength);

		return {
			id: getUintBE(idView),
			len: getUintBE(lengthView),
		};
	}

	async function readChildren(children) {
		let ebmlElementCount = 0;
		while (children > 0) {
			ebmlElementCount++;
			if (ebmlElementCount > maximumEbmlElementCount) {
				return;
			}

			if (hasExceededUnknownSizeScanBudget(tokenizer, ebmlScanStart, maximumUntrustedSkipSizeInBytes)) {
				return;
			}

			const previousPosition = tokenizer.position;
			const element = await readElement();

			if (element.id === 0x42_82) {
				// `DocType` is a short string ("webm", "matroska", ...), reject implausible lengths to avoid large allocations.
				if (element.len > maximumEbmlDocumentTypeSizeInBytes) {
					return;
				}

				const documentTypeLength = getSafeBound(element.len, maximumEbmlDocumentTypeSizeInBytes, 'EBML DocType');
				const rawValue = await tokenizer.readToken(new Token.StringType(documentTypeLength));
				return rawValue.replaceAll(/\0.*$/gv, ''); // Return DocType
			}

			if (
				hasUnknownFileSize(tokenizer)
				&& (
					!Number.isFinite(element.len)
					|| element.len < 0
					|| element.len > maximumEbmlElementPayloadSizeInBytes
				)
			) {
				return;
			}

			await safeIgnore(tokenizer, element.len, {
				maximumLength: hasUnknownFileSize(tokenizer) ? maximumEbmlElementPayloadSizeInBytes : tokenizer.fileInfo.size,
				reason: 'EBML payload',
			}); // ignore payload
			--children;

			// Safeguard against malformed files: bail if the position did not advance.
			if (tokenizer.position <= previousPosition) {
				return;
			}
		}
	}

	const rootElement = await readElement();
	const ebmlScanStart = tokenizer.position;
	const documentType = await readChildren(rootElement.len);

	switch (documentType) {
		case 'webm':
			return {
				ext: 'webm',
				mime: 'video/webm',
			};

		case 'matroska':
			return {
				ext: 'mkv',
				mime: 'video/matroska',
			};

		default:
	}
}
```

## File: `source/detectors/png.js`
```javascript
import * as Token from 'token-types';
import * as strtok3 from 'strtok3/core';
import {
	ParserHardLimitError,
	safeIgnore,
	hasUnknownFileSize,
	hasExceededUnknownSizeScanBudget,
} from '../parser.js';

const maximumPngChunkCount = 512;
const maximumPngStreamScanBudgetInBytes = 16 * 1024 * 1024;
const maximumPngChunkSizeInBytes = 1024 * 1024;

function isPngAncillaryChunk(type) {
	return (type.codePointAt(0) & 0x20) !== 0;
}

export async function detectPng(tokenizer) {
	const pngFileType = {
		ext: 'png',
		mime: 'image/png',
	};

	const apngFileType = {
		ext: 'apng',
		mime: 'image/apng',
	};

	// APNG format (https://wiki.mozilla.org/APNG_Specification)
	// 1. Find the first IDAT (image data) chunk (49 44 41 54)
	// 2. Check if there is an "acTL" chunk before the IDAT one (61 63 54 4C)

	// Offset calculated as follows:
	// - 8 bytes: PNG signature
	// - 4 (length) + 4 (chunk type) + 13 (chunk data) + 4 (CRC): IHDR chunk

	await tokenizer.ignore(8); // ignore PNG signature

	async function readChunkHeader() {
		return {
			length: await tokenizer.readToken(Token.INT32_BE),
			type: await tokenizer.readToken(new Token.StringType(4, 'latin1')),
		};
	}

	const isUnknownPngStream = hasUnknownFileSize(tokenizer);
	const pngScanStart = tokenizer.position;
	let pngChunkCount = 0;
	let hasSeenImageHeader = false;
	do {
		pngChunkCount++;
		if (pngChunkCount > maximumPngChunkCount) {
			break;
		}

		if (hasExceededUnknownSizeScanBudget(tokenizer, pngScanStart, maximumPngStreamScanBudgetInBytes)) {
			break;
		}

		const previousPosition = tokenizer.position;
		const chunk = await readChunkHeader();
		if (chunk.length < 0) {
			return; // Invalid chunk length
		}

		if (chunk.type === 'IHDR') {
			// PNG requires the first real image header to be a 13-byte IHDR chunk.
			if (chunk.length !== 13) {
				return;
			}

			hasSeenImageHeader = true;
		}

		switch (chunk.type) {
			case 'IDAT':
				return pngFileType;
			case 'acTL':
				return apngFileType;
			default:
				if (
					!hasSeenImageHeader
					&& chunk.type !== 'CgBI'
				) {
					return;
				}

				if (
					isUnknownPngStream
					&& chunk.length > maximumPngChunkSizeInBytes
				) {
					// Avoid huge attacker-controlled skips when probing unknown-size streams.
					return hasSeenImageHeader && isPngAncillaryChunk(chunk.type) ? pngFileType : undefined;
				}

				try {
					await safeIgnore(tokenizer, chunk.length + 4, {
						maximumLength: isUnknownPngStream ? maximumPngChunkSizeInBytes + 4 : tokenizer.fileInfo.size,
						reason: 'PNG chunk payload',
					}); // Ignore chunk-data + CRC
				} catch (error) {
					if (
						!isUnknownPngStream
						&& (
							error instanceof ParserHardLimitError
							|| error instanceof strtok3.EndOfStreamError
						)
					) {
						return pngFileType;
					}

					throw error;
				}
		}

		// Safeguard against malformed files: bail if the position did not advance.
		if (tokenizer.position <= previousPosition) {
			break;
		}
	} while (tokenizer.position + 8 < tokenizer.fileInfo.size);

	return pngFileType;
}
```

## File: `source/detectors/zip.js`
```javascript
import * as Token from 'token-types';
import * as strtok3 from 'strtok3/core';
import {ZipHandler} from '@tokenizer/inflate';
import {
	maximumUntrustedSkipSizeInBytes,
	ParserHardLimitError,
	safeIgnore,
	hasUnknownFileSize,
	hasExceededUnknownSizeScanBudget,
} from '../parser.js';

const maximumZipEntrySizeInBytes = 1024 * 1024;
const maximumZipEntryCount = 1024;
const maximumZipBufferedReadSizeInBytes = (2 ** 31) - 1;
const maximumZipTextEntrySizeInBytes = maximumZipEntrySizeInBytes;

const recoverableZipErrorMessages = new Set([
	'Unexpected signature',
	'Encrypted ZIP',
	'Expected Central-File-Header signature',
]);
const recoverableZipErrorMessagePrefixes = [
	'ZIP entry count exceeds ',
	'Unsupported ZIP compression method:',
	'ZIP entry compressed data exceeds ',
	'ZIP entry decompressed data exceeds ',
	'Expected data-descriptor-signature at position ',
];
const recoverableZipErrorCodes = new Set([
	'Z_BUF_ERROR',
	'Z_DATA_ERROR',
	'ERR_INVALID_STATE',
]);

async function decompressDeflateRawWithLimit(data, {maximumLength = maximumZipEntrySizeInBytes} = {}) {
	const input = new ReadableStream({
		start(controller) {
			controller.enqueue(data);
			controller.close();
		},
	});
	const output = input.pipeThrough(new DecompressionStream('deflate-raw'));
	const reader = output.getReader();
	const chunks = [];
	let totalLength = 0;

	try {
		for (;;) {
			const {done, value} = await reader.read();
			if (done) {
				break;
			}

			totalLength += value.length;
			if (totalLength > maximumLength) {
				await reader.cancel();
				throw new Error(`ZIP entry decompressed data exceeds ${maximumLength} bytes`);
			}

			chunks.push(value);
		}
	} finally {
		reader.releaseLock();
	}

	const uncompressedData = new Uint8Array(totalLength);
	let offset = 0;
	for (const chunk of chunks) {
		uncompressedData.set(chunk, offset);
		offset += chunk.length;
	}

	return uncompressedData;
}

function mergeByteChunks(chunks, totalLength) {
	const merged = new Uint8Array(totalLength);
	let offset = 0;

	for (const chunk of chunks) {
		merged.set(chunk, offset);
		offset += chunk.length;
	}

	return merged;
}

function getMaximumZipBufferedReadLength(tokenizer) {
	const fileSize = tokenizer.fileInfo.size;
	const remainingBytes = Number.isFinite(fileSize)
		? Math.max(0, fileSize - tokenizer.position)
		: Number.MAX_SAFE_INTEGER;

	return Math.min(remainingBytes, maximumZipBufferedReadSizeInBytes);
}

function isRecoverableZipError(error) {
	if (error instanceof strtok3.EndOfStreamError) {
		return true;
	}

	if (error instanceof ParserHardLimitError) {
		return true;
	}

	if (!(error instanceof Error)) {
		return false;
	}

	if (recoverableZipErrorMessages.has(error.message)) {
		return true;
	}

	if (recoverableZipErrorCodes.has(error.code)) {
		return true;
	}

	for (const prefix of recoverableZipErrorMessagePrefixes) {
		if (error.message.startsWith(prefix)) {
			return true;
		}
	}

	return false;
}

function canReadZipEntryForDetection(zipHeader, maximumSize = maximumZipEntrySizeInBytes) {
	const sizes = [zipHeader.compressedSize, zipHeader.uncompressedSize];
	for (const size of sizes) {
		if (
			!Number.isFinite(size)
			|| size < 0
			|| size > maximumSize
		) {
			return false;
		}
	}

	return true;
}

// -- iWork helpers --

function createIWorkZipDetectionState() {
	return {
		hasDocumentEntry: false,
		hasMasterSlideEntry: false,
		hasTablesEntry: false,
		hasCalculationEngineEntry: false,
	};
}

function updateIWorkZipDetectionStateFromFilename(iWorkState, filename) {
	if (filename === 'Index/Document.iwa') {
		iWorkState.hasDocumentEntry = true;
	}

	if (filename.startsWith('Index/MasterSlide')) {
		iWorkState.hasMasterSlideEntry = true;
	}

	if (filename.startsWith('Index/Tables/')) {
		iWorkState.hasTablesEntry = true;
	}

	if (filename === 'Index/CalculationEngine.iwa') {
		iWorkState.hasCalculationEngineEntry = true;
	}
}

function getIWorkFileTypeFromZipEntries(iWorkState) {
	if (!iWorkState.hasDocumentEntry) {
		return;
	}

	if (iWorkState.hasMasterSlideEntry) {
		return {ext: 'key', mime: 'application/vnd.apple.keynote'};
	}

	if (iWorkState.hasTablesEntry) {
		return {ext: 'numbers', mime: 'application/vnd.apple.numbers'};
	}

	return {ext: 'pages', mime: 'application/vnd.apple.pages'};
}

// -- OpenXML helpers --

function getFileTypeFromMimeType(mimeType) {
	mimeType = mimeType.toLowerCase();
	switch (mimeType) {
		case 'application/epub+zip':
			return {ext: 'epub', mime: mimeType};
		case 'application/vnd.oasis.opendocument.text':
			return {ext: 'odt', mime: mimeType};
		case 'application/vnd.oasis.opendocument.text-template':
			return {ext: 'ott', mime: mimeType};
		case 'application/vnd.oasis.opendocument.spreadsheet':
			return {ext: 'ods', mime: mimeType};
		case 'application/vnd.oasis.opendocument.spreadsheet-template':
			return {ext: 'ots', mime: mimeType};
		case 'application/vnd.oasis.opendocument.presentation':
			return {ext: 'odp', mime: mimeType};
		case 'application/vnd.oasis.opendocument.presentation-template':
			return {ext: 'otp', mime: mimeType};
		case 'application/vnd.oasis.opendocument.graphics':
			return {ext: 'odg', mime: mimeType};
		case 'application/vnd.oasis.opendocument.graphics-template':
			return {ext: 'otg', mime: mimeType};
		case 'application/vnd.openxmlformats-officedocument.presentationml.slideshow':
			return {ext: 'ppsx', mime: mimeType};
		case 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
			return {ext: 'xlsx', mime: mimeType};
		case 'application/vnd.ms-excel.sheet.macroenabled':
			return {ext: 'xlsm', mime: 'application/vnd.ms-excel.sheet.macroenabled.12'};
		case 'application/vnd.openxmlformats-officedocument.spreadsheetml.template':
			return {ext: 'xltx', mime: mimeType};
		case 'application/vnd.ms-excel.template.macroenabled':
			return {ext: 'xltm', mime: 'application/vnd.ms-excel.template.macroenabled.12'};
		case 'application/vnd.ms-powerpoint.slideshow.macroenabled':
			return {ext: 'ppsm', mime: 'application/vnd.ms-powerpoint.slideshow.macroenabled.12'};
		case 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
			return {ext: 'docx', mime: mimeType};
		case 'application/vnd.ms-word.document.macroenabled':
			return {ext: 'docm', mime: 'application/vnd.ms-word.document.macroenabled.12'};
		case 'application/vnd.openxmlformats-officedocument.wordprocessingml.template':
			return {ext: 'dotx', mime: mimeType};
		case 'application/vnd.ms-word.template.macroenabledtemplate':
			return {ext: 'dotm', mime: 'application/vnd.ms-word.template.macroenabled.12'};
		case 'application/vnd.openxmlformats-officedocument.presentationml.template':
			return {ext: 'potx', mime: mimeType};
		case 'application/vnd.ms-powerpoint.template.macroenabled':
			return {ext: 'potm', mime: 'application/vnd.ms-powerpoint.template.macroenabled.12'};
		case 'application/vnd.openxmlformats-officedocument.presentationml.presentation':
			return {ext: 'pptx', mime: mimeType};
		case 'application/vnd.ms-powerpoint.presentation.macroenabled':
			return {ext: 'pptm', mime: 'application/vnd.ms-powerpoint.presentation.macroenabled.12'};
		case 'application/vnd.ms-visio.drawing':
			return {ext: 'vsdx', mime: 'application/vnd.visio'};
		case 'application/vnd.ms-package.3dmanufacturing-3dmodel+xml':
			return {ext: '3mf', mime: 'model/3mf'};
		default:
	}
}

function createOpenXmlZipDetectionState() {
	return {
		hasContentTypesEntry: false,
		hasParsedContentTypesEntry: false,
		isParsingContentTypes: false,
		hasUnparseableContentTypes: false,
		hasWordDirectory: false,
		hasPresentationDirectory: false,
		hasSpreadsheetDirectory: false,
		hasThreeDimensionalModelEntry: false,
	};
}

function updateOpenXmlZipDetectionStateFromFilename(openXmlState, filename) {
	if (filename.startsWith('word/')) {
		openXmlState.hasWordDirectory = true;
	}

	if (filename.startsWith('ppt/')) {
		openXmlState.hasPresentationDirectory = true;
	}

	if (filename.startsWith('xl/')) {
		openXmlState.hasSpreadsheetDirectory = true;
	}

	if (
		filename.startsWith('3D/')
		&& filename.endsWith('.model')
	) {
		openXmlState.hasThreeDimensionalModelEntry = true;
	}
}

function getOpenXmlFileTypeFromDirectoryNames(openXmlState) {
	if (openXmlState.hasWordDirectory) {
		return {
			ext: 'docx',
			mime: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
		};
	}

	if (openXmlState.hasPresentationDirectory) {
		return {
			ext: 'pptx',
			mime: 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
		};
	}

	if (openXmlState.hasSpreadsheetDirectory) {
		return {
			ext: 'xlsx',
			mime: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
		};
	}

	if (openXmlState.hasThreeDimensionalModelEntry) {
		return {
			ext: '3mf',
			mime: 'model/3mf',
		};
	}
}

function getOpenXmlFileTypeFromZipEntries(openXmlState) {
	// Only use directory-name heuristic when [Content_Types].xml was present in the archive
	// but its handler was skipped (not invoked, not currently running, and not already resolved).
	// This avoids guessing from directory names when content-type parsing already gave a definitive answer or failed.
	if (
		!openXmlState.hasContentTypesEntry
		|| openXmlState.hasUnparseableContentTypes
		|| openXmlState.isParsingContentTypes
		|| openXmlState.hasParsedContentTypesEntry
	) {
		return;
	}

	return getOpenXmlFileTypeFromDirectoryNames(openXmlState);
}

function getOpenXmlMimeTypeFromContentTypesXml(xmlContent) {
	// We only need the `ContentType="...main+xml"` value, so a small string scan is enough and avoids full XML parsing.
	const endPosition = xmlContent.indexOf('.main+xml"');
	if (endPosition === -1) {
		const mimeType = 'application/vnd.ms-package.3dmanufacturing-3dmodel+xml';
		if (xmlContent.includes(`ContentType="${mimeType}"`)) {
			return mimeType;
		}

		return;
	}

	const truncatedContent = xmlContent.slice(0, endPosition);
	const firstQuotePosition = truncatedContent.lastIndexOf('"');
	// If no quote is found, `lastIndexOf` returns -1 and this intentionally falls back to the full truncated prefix.
	return truncatedContent.slice(firstQuotePosition + 1);
}

const zipDataDescriptorSignature = 0x08_07_4B_50;
const zipDataDescriptorLengthInBytes = 16;
const zipDataDescriptorOverlapLengthInBytes = zipDataDescriptorLengthInBytes - 1;

function findZipDataDescriptorOffset(buffer, bytesConsumed) {
	if (buffer.length < zipDataDescriptorLengthInBytes) {
		return -1;
	}

	const lastPossibleDescriptorOffset = buffer.length - zipDataDescriptorLengthInBytes;
	for (let index = 0; index <= lastPossibleDescriptorOffset; index++) {
		if (
			Token.UINT32_LE.get(buffer, index) === zipDataDescriptorSignature
			&& Token.UINT32_LE.get(buffer, index + 8) === bytesConsumed + index
		) {
			return index;
		}
	}

	return -1;
}

async function readZipDataDescriptorEntryWithLimit(zipHandler, {shouldBuffer, maximumLength = maximumZipEntrySizeInBytes} = {}) {
	const {syncBuffer} = zipHandler;
	const {length: syncBufferLength} = syncBuffer;
	const chunks = [];
	let bytesConsumed = 0;

	for (;;) {
		const length = await zipHandler.tokenizer.peekBuffer(syncBuffer, {mayBeLess: true});
		const dataDescriptorOffset = findZipDataDescriptorOffset(syncBuffer.subarray(0, length), bytesConsumed);
		const retainedLength = dataDescriptorOffset >= 0
			? 0
			: (
				length === syncBufferLength
					? Math.min(zipDataDescriptorOverlapLengthInBytes, length - 1)
					: 0
			);
		const chunkLength = dataDescriptorOffset >= 0 ? dataDescriptorOffset : length - retainedLength;

		if (chunkLength === 0) {
			break;
		}

		bytesConsumed += chunkLength;
		if (bytesConsumed > maximumLength) {
			throw new Error(`ZIP entry compressed data exceeds ${maximumLength} bytes`);
		}

		if (shouldBuffer) {
			const data = new Uint8Array(chunkLength);
			await zipHandler.tokenizer.readBuffer(data);
			chunks.push(data);
		} else {
			await zipHandler.tokenizer.ignore(chunkLength);
		}

		if (dataDescriptorOffset >= 0) {
			break;
		}
	}

	if (!hasUnknownFileSize(zipHandler.tokenizer)) {
		zipHandler.knownSizeDescriptorScannedBytes += bytesConsumed;
	}

	if (!shouldBuffer) {
		return;
	}

	return mergeByteChunks(chunks, bytesConsumed);
}

function getRemainingZipScanBudget(zipHandler, startOffset) {
	if (hasUnknownFileSize(zipHandler.tokenizer)) {
		return Math.max(0, maximumUntrustedSkipSizeInBytes - (zipHandler.tokenizer.position - startOffset));
	}

	return Math.max(0, maximumZipEntrySizeInBytes - zipHandler.knownSizeDescriptorScannedBytes);
}

async function readZipEntryData(zipHandler, zipHeader, {shouldBuffer, maximumDescriptorLength = maximumZipEntrySizeInBytes} = {}) {
	if (
		zipHeader.dataDescriptor
		&& zipHeader.compressedSize === 0
	) {
		return readZipDataDescriptorEntryWithLimit(zipHandler, {
			shouldBuffer,
			maximumLength: maximumDescriptorLength,
		});
	}

	if (!shouldBuffer) {
		await safeIgnore(zipHandler.tokenizer, zipHeader.compressedSize, {
			maximumLength: hasUnknownFileSize(zipHandler.tokenizer) ? maximumZipEntrySizeInBytes : zipHandler.tokenizer.fileInfo.size,
			reason: 'ZIP entry compressed data',
		});
		return;
	}

	const maximumLength = getMaximumZipBufferedReadLength(zipHandler.tokenizer);
	if (
		!Number.isFinite(zipHeader.compressedSize)
		|| zipHeader.compressedSize < 0
		|| zipHeader.compressedSize > maximumLength
	) {
		throw new Error(`ZIP entry compressed data exceeds ${maximumLength} bytes`);
	}

	const fileData = new Uint8Array(zipHeader.compressedSize);
	await zipHandler.tokenizer.readBuffer(fileData);
	return fileData;
}

// Override the default inflate to enforce decompression size limits, since @tokenizer/inflate does not expose a configuration hook for this.
ZipHandler.prototype.inflate = async function (zipHeader, fileData, callback) {
	if (zipHeader.compressedMethod === 0) {
		return callback(fileData);
	}

	if (zipHeader.compressedMethod !== 8) {
		throw new Error(`Unsupported ZIP compression method: ${zipHeader.compressedMethod}`);
	}

	const uncompressedData = await decompressDeflateRawWithLimit(fileData, {maximumLength: maximumZipEntrySizeInBytes});
	return callback(uncompressedData);
};

ZipHandler.prototype.unzip = async function (fileCallback) {
	let stop = false;
	let zipEntryCount = 0;
	const zipScanStart = this.tokenizer.position;
	this.knownSizeDescriptorScannedBytes = 0;
	do {
		if (hasExceededUnknownSizeScanBudget(this.tokenizer, zipScanStart, maximumUntrustedSkipSizeInBytes)) {
			throw new ParserHardLimitError(`ZIP stream probing exceeds ${maximumUntrustedSkipSizeInBytes} bytes`);
		}

		const zipHeader = await this.readLocalFileHeader();
		if (!zipHeader) {
			break;
		}

		zipEntryCount++;
		if (zipEntryCount > maximumZipEntryCount) {
			throw new Error(`ZIP entry count exceeds ${maximumZipEntryCount}`);
		}

		const next = fileCallback(zipHeader);
		stop = Boolean(next.stop);
		await this.tokenizer.ignore(zipHeader.extraFieldLength);
		const fileData = await readZipEntryData(this, zipHeader, {
			shouldBuffer: Boolean(next.handler),
			maximumDescriptorLength: Math.min(maximumZipEntrySizeInBytes, getRemainingZipScanBudget(this, zipScanStart)),
		});

		if (next.handler) {
			await this.inflate(zipHeader, fileData, next.handler);
		}

		if (zipHeader.dataDescriptor) {
			const dataDescriptor = new Uint8Array(zipDataDescriptorLengthInBytes);
			await this.tokenizer.readBuffer(dataDescriptor);
			if (Token.UINT32_LE.get(dataDescriptor, 0) !== zipDataDescriptorSignature) {
				throw new Error(`Expected data-descriptor-signature at position ${this.tokenizer.position - dataDescriptor.length}`);
			}
		}

		if (hasExceededUnknownSizeScanBudget(this.tokenizer, zipScanStart, maximumUntrustedSkipSizeInBytes)) {
			throw new ParserHardLimitError(`ZIP stream probing exceeds ${maximumUntrustedSkipSizeInBytes} bytes`);
		}
	} while (!stop);
};

export async function detectZip(tokenizer) {
	let fileType;
	const openXmlState = createOpenXmlZipDetectionState();
	const iWorkState = createIWorkZipDetectionState();

	try {
		await new ZipHandler(tokenizer).unzip(zipHeader => {
			updateOpenXmlZipDetectionStateFromFilename(openXmlState, zipHeader.filename);
			updateIWorkZipDetectionStateFromFilename(iWorkState, zipHeader.filename);

			// Early exit for Keynote or Numbers when markers are definitive
			if (iWorkState.hasDocumentEntry && (iWorkState.hasMasterSlideEntry || iWorkState.hasTablesEntry)) {
				fileType = getIWorkFileTypeFromZipEntries(iWorkState);
				return {stop: true};
			}

			const isOpenXmlContentTypesEntry = zipHeader.filename === '[Content_Types].xml';
			const openXmlFileTypeFromEntries = getOpenXmlFileTypeFromZipEntries(openXmlState);
			if (
				!isOpenXmlContentTypesEntry
				&& openXmlFileTypeFromEntries
			) {
				fileType = openXmlFileTypeFromEntries;
				return {
					stop: true,
				};
			}

			switch (zipHeader.filename) {
				case 'META-INF/mozilla.rsa':
					fileType = {
						ext: 'xpi',
						mime: 'application/x-xpinstall',
					};
					return {
						stop: true,
					};
				case 'META-INF/MANIFEST.MF':
					fileType = {
						ext: 'jar',
						mime: 'application/java-archive',
					};
					return {
						stop: true,
					};
				case 'mimetype':
					if (!canReadZipEntryForDetection(zipHeader, maximumZipTextEntrySizeInBytes)) {
						return {};
					}

					return {
						async handler(fileData) {
							// Use TextDecoder to decode the UTF-8 encoded data
							const mimeType = new TextDecoder('utf-8').decode(fileData).trim();
							fileType = getFileTypeFromMimeType(mimeType);
						},
						stop: true,
					};

				case '[Content_Types].xml': {
					openXmlState.hasContentTypesEntry = true;

					if (!canReadZipEntryForDetection(zipHeader, maximumZipTextEntrySizeInBytes)) {
						openXmlState.hasUnparseableContentTypes = true;
						return {};
					}

					openXmlState.isParsingContentTypes = true;
					return {
						async handler(fileData) {
							// Use TextDecoder to decode the UTF-8 encoded data
							const xmlContent = new TextDecoder('utf-8').decode(fileData);
							const mimeType = getOpenXmlMimeTypeFromContentTypesXml(xmlContent);
							if (mimeType) {
								fileType = getFileTypeFromMimeType(mimeType);
							}

							openXmlState.hasParsedContentTypesEntry = true;
							openXmlState.isParsingContentTypes = false;
						},
						stop: true,
					};
				}

				default:
					if (/classes\d*\.dex/v.test(zipHeader.filename)) {
						fileType = {
							ext: 'apk',
							mime: 'application/vnd.android.package-archive',
						};
						return {stop: true};
					}

					return {};
			}
		});
	} catch (error) {
		if (!isRecoverableZipError(error)) {
			throw error;
		}

		if (openXmlState.isParsingContentTypes) {
			openXmlState.isParsingContentTypes = false;
			openXmlState.hasUnparseableContentTypes = true;
		}

		// When the stream was truncated before reaching [Content_Types].xml, use directory names as a fallback.
		// This handles LibreOffice-created OOXML files where [Content_Types].xml appears after content entries.
		if (!fileType && error instanceof strtok3.EndOfStreamError && !openXmlState.hasContentTypesEntry) {
			fileType = getOpenXmlFileTypeFromDirectoryNames(openXmlState);
		}
	}

	const iWorkFileType = hasUnknownFileSize(tokenizer)
		&& iWorkState.hasDocumentEntry
		&& !iWorkState.hasMasterSlideEntry
		&& !iWorkState.hasTablesEntry
		&& !iWorkState.hasCalculationEngineEntry
		? undefined
		: getIWorkFileTypeFromZipEntries(iWorkState);

	return fileType ?? getOpenXmlFileTypeFromZipEntries(openXmlState) ?? iWorkFileType ?? {
		ext: 'zip',
		mime: 'application/zip',
	};
}
```


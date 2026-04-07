---
id: gm
type: knowledge
owner: OA_Triage
---
# gm
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: index.js
```js

/**
 * Module dependencies.
 */

var Stream = require('stream').Stream;
var EventEmitter = require('events').EventEmitter;
var util = require('util');

util.inherits(gm, EventEmitter);

/**
 * Constructor.
 *
 * @param {String|Number} path - path to img source or ReadableStream or width of img to create
 * @param {Number} [height] - optional filename of ReadableStream or height of img to create
 * @param {String} [color] - optional hex background color of created img
 */

function gm (source, height, color) {
  var width;

  if (!(this instanceof gm)) {
    return new gm(source, height, color);
  }

  EventEmitter.call(this);

  this._options = {};
  this.options(this.__proto__._options);

  this.data = {};
  this._in = [];
  this._out = [];
  this._outputFormat = null;
  this._subCommand = 'convert';

  if (source instanceof Stream) {
    this.sourceStream = source;
    source = height || 'unknown.jpg';
  } else if (Buffer.isBuffer(source)) {
    this.sourceBuffer = source;
    source = height || 'unknown.jpg';
  } else if (height) {
    // new images
    width = source;
    source = "";

    this.in("-size", width + "x" + height);

    if (color) {
      this.in("xc:"+ color);
    }
  }

  if (typeof source === "string") {
    // then source is a path

    // parse out gif frame brackets from filename
    // since stream doesn't use source path
    // eg. "filename.gif[0]"
    var frames = source.match(/(\[.+\])$/);
    if (frames) {
      this.sourceFrames = source.substr(frames.index, frames[0].length);
      source = source.substr(0, frames.index);
    }
  }

  this.source = source;

  this.addSrcFormatter(function (src) {
    // must be first source formatter

    var inputFromStdin = this.sourceStream || this.sourceBuffer;
    var ret = inputFromStdin ? '-' : this.source;

    const fileNameProvied = typeof height === 'string';
    if (inputFromStdin && fileNameProvied && /\.ico$/i.test(this.source)) {
      ret = `ico:-`;
    }

    if (ret && this.sourceFrames) ret += this.sourceFrames;

    src.length = 0;
    src[0] = ret;
  });
}

/**
 * Subclasses the gm constructor with custom options.
 *
 * @param {options} options
 * @return {gm} the subclasses gm constructor
 */

var parent = gm;
gm.subClass = function subClass (options) {
  function gm (source, height, color) {
    if (!(this instanceof parent)) {
      return new gm(source, height, color);
    }

    parent.call(this, source, height, color);
  }

  gm.prototype.__proto__ = parent.prototype;
  gm.prototype._options = {};
  gm.prototype.options(options);

  return gm;
}

/**
 * Augment the prototype.
 */

require("./lib/options")(gm.prototype);
require("./lib/getters")(gm);
require("./lib/args")(gm.prototype);
require("./lib/drawing")(gm.prototype);
require("./lib/convenience")(gm.prototype);
require("./lib/command")(gm.prototype);
require("./lib/compare")(gm.prototype);
require("./lib/composite")(gm.prototype);
require("./lib/montage")(gm.prototype);

/**
 * Expose.
 */

module.exports = exports = gm;
module.exports.utils = require('./lib/utils');
module.exports.compare = require('./lib/compare')();
module.exports.version = require('./package.json').version;

```

### File: package.json
```json
{
  "name": "gm",
  "description": "GraphicsMagick and ImageMagick for node.js",
  "version": "1.25.1",
  "author": "Aaron Heckmann <aaron.heckmann+github@gmail.com>",
  "keywords": [
    "graphics",
    "magick",
    "image",
    "graphicsmagick",
    "imagemagick",
    "gm",
    "convert",
    "identify",
    "compare"
  ],
  "engines": {
    "node": ">=14"
  },
  "bugs": {
    "url": "http://github.com/aheckmann/gm/issues"
  },
  "licenses": [
    {
      "type": "MIT",
      "url": "http://www.opensource.org/licenses/mit-license.php"
    }
  ],
  "main": "./index",
  "scripts": {
    "security": "npm audit",
    "test": "npm run security && npm run test-integration",
    "test-integration": "node test/ --integration",
    "test-unit": "node test/"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/aheckmann/gm.git"
  },
  "license": "MIT",
  "devDependencies": {
    "async": "~0.9.0"
  },
  "dependencies": {
    "array-parallel": "~0.1.3",
    "array-series": "~0.1.5",
    "cross-spawn": "^7.0.5",
    "debug": "^3.1.0"
  }
}

```

### File: README.md
```md
# 2025-02-24 This project is not maintained

Instead of using this project, execute the `gm` or `magick` binaries using
[`cross-spawn`](https://www.npmjs.com/package/cross-spawn) directly.

Nearly [15 years ago](https://github.com/aheckmann/gm/commit/defc7360d70d87f7a13da4f6e2ef0104594776b9) I started this project as part of my start up which I sold later that year (2010). Having not used this project in over a decade and with no contributors for years, it's time to officially sunset `gm`.

No further Issues will be addressed. No Pull Requests will be merged. No new commits or npm releases will be made.

---

😍 _Massive **thank you** to [everyone](https://github.com/aheckmann/gm/graphs/contributors) who contributed to this project over the years._ 😍

---

## I want to continue using gm. What do I do?

All past `gm` releases published to the npm registry will continue to be available for install. However, you should **prioritize moving off of this project to an alternative** because the risk of unpatched vulnerabilities in this project will continue to _increase_ over time. No new commits will land and no new releases will be published.

The most obvious alternative to `gm` I see is installing [cross-spawn](https://www.npmjs.com/package/cross-spawn) and executing the GraphicsMagick or ImageMagick binaries directly, after all, that's pretty much all this project did. There may be other `gm` alternatives on npm but I don't what they are offhand so you'll need to search for something suitable yourself.

---


# gm [![Build Status](https://travis-ci.org/aheckmann/gm.png?branch=master)](https://travis-ci.org/aheckmann/gm)  [![NPM Version](https://img.shields.io/npm/v/gm.svg?style=flat)](https://www.npmjs.org/package/gm)

GraphicsMagick and ImageMagick for node

## Bug Reports

When reporting bugs please include the version of graphicsmagick/imagemagick you're using (gm -version/convert -version) as well as the version of this module and copies of any images you're having problems with.

## Getting started
First download and install [GraphicsMagick](http://www.graphicsmagick.org/) or [ImageMagick](http://www.imagemagick.org/). In Mac OS X, you can simply use [Homebrew](http://mxcl.github.io/homebrew/) and do:

    brew install imagemagick
    brew install graphicsmagick

then either use npm:

    npm install gm

or clone the repo:

    git clone git://github.com/aheckmann/gm.git


## Use ImageMagick instead of gm

Subclass `gm` to enable [ImageMagick 7+](https://imagemagick.org/script/porting.php)

```js
const fs = require('fs')
const gm = require('gm').subClass({ imageMagick: '7+' });
```

Or, to enable ImageMagick legacy mode (for ImageMagick version < 7)

```js
const fs = require('fs')
const gm = require('gm').subClass({ imageMagick: true });
```

## Specify the executable path

Optionally specify the path to the executable.

```js
const fs = require('fs')
const gm = require('gm').subClass({
  appPath: String.raw`C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe`
});
```

## Basic Usage

```js
var fs = require('fs')
  , gm = require('gm');

// resize and remove EXIF profile data
gm('/path/to/my/img.jpg')
.resize(240, 240)
.noProfile()
.write('/path/to/resize.png', function (err) {
  if (!err) console.log('done');
});

// some files would not be resized appropriately
// http://stackoverflow.com/questions/5870466/imagemagick-incorrect-dimensions
// you have two options:
// use the '!' flag to ignore aspect ratio
gm('/path/to/my/img.jpg')
.resize(240, 240, '!')
.write('/path/to/resize.png', function (err) {
  if (!err) console.log('done');
});

// use the .resizeExact with only width and/or height arguments
gm('/path/to/my/img.jpg')
.resizeExact(240, 240)
.write('/path/to/resize.png', function (err) {
  if (!err) console.log('done');
});

// obtain the size of an image
gm('/path/to/my/img.jpg')
.size(function (err, size) {
  if (!err)
    console.log(size.width > size.height ? 'wider' : 'taller than you');
});

// output all available image properties
gm('/path/to/img.png')
.identify(function (err, data) {
  if (!err) console.log(data)
});

// pull out the first frame of an animated gif and save as png
gm('/path/to/animated.gif[0]')
.write('/path/to/firstframe.png', function (err) {
  if (err) console.log('aaw, shucks');
});

// auto-orient an image
gm('/path/to/img.jpg')
.autoOrient()
.write('/path/to/oriented.jpg', function (err) {
  if (err) ...
})

// crazytown
gm('/path/to/my/img.jpg')
.flip()
.magnify()
.rotate('green', 45)
.blur(7, 3)
.crop(300, 300, 150, 130)
.edge(3)
.write('/path/to/crazy.jpg', function (err) {
  if (!err) console.log('crazytown has arrived');
})

// annotate an image
gm('/path/to/my/img.jpg')
.stroke("#ffffff")
.drawCircle(10, 10, 20, 10)
.font("Helvetica.ttf", 12)
.drawText(30, 20, "GMagick!")
.write("/path/to/drawing.png", function (err) {
  if (!err) console.log('done');
});

// creating an image
gm(200, 400, "#ddff99f3")
.drawText(10, 50, "from scratch")
.write("/path/to/brandNewImg.jpg", function (err) {
  // ...
});
```

## Streams

```js
// passing a stream
var readStream = fs.createReadStream('/path/to/my/img.jpg');
gm(readStream, 'img.jpg')
.write('/path/to/reformat.png', function (err) {
  if (!err) console.log('done');
});


// passing a downloadable image by url

var request = require('request');
var url = "www.abc.com/pic.jpg"

gm(request(url))
.write('/path/to/reformat.png', function (err) {
  if (!err) console.log('done');
});


// can also stream output to a ReadableStream
// (can be piped to a local file or remote server)
gm('/path/to/my/img.jpg')
.resize('200', '200')
.stream(function (err, stdout, stderr) {
  var writeStream = fs.createWriteStream('/path/to/my/resized.jpg');
  stdout.pipe(writeStream);
});

// without a callback, .stream() returns a stream
// this is just a convenience wrapper for above.
var writeStream = fs.createWriteStream('/path/to/my/resized.jpg');
gm('/path/to/my/img.jpg')
.resize('200', '200')
.stream()
.pipe(writeStream);

// pass a format or filename to stream() and
// gm will provide image data in that format
gm('/path/to/my/img.jpg')
.stream('png', function (err, stdout, stderr) {
  var writeStream = fs.createWriteStream('/path/to/my/reformatted.png');
  stdout.pipe(writeStream);
});

// or without the callback
var writeStream = fs.createWriteStream('/path/to/my/reformatted.png');
gm('/path/to/my/img.jpg')
.stream('png')
.pipe(writeStream);

// combine the two for true streaming image processing
var readStream = fs.createReadStream('/path/to/my/img.jpg');
gm(readStream)
.resize('200', '200')
.stream(function (err, stdout, stderr) {
  var writeStream = fs.createWriteStream('/path/to/my/resized.jpg');
  stdout.pipe(writeStream);
});

// GOTCHA:
// when working with input streams and any 'identify'
// operation (size, format, etc), you must pass "{bufferStream: true}" if
// you also need to convert (write() or stream()) the image afterwards
// NOTE: this buffers the readStream in memory!
var readStream = fs.createReadStream('/path/to/my/img.jpg');
gm(readStream)
.size({bufferStream: true}, function(err, size) {
  this.resize(size.width / 2, size.height / 2)
  this.write('/path/to/resized.jpg', function (err) {
    if (!err) console.log('done');
  });
});

```

## Buffers

```js
// A buffer can be passed instead of a filepath as well
var buf = require('fs').readFileSync('/path/to/image.jpg');

gm(buf, 'image.jpg')
.noise('laplacian')
.write('/path/to/out.jpg', function (err) {
  if (err) return handle(err);
  console.log('Created an image from a Buffer!');
});

/*
A buffer can also be returned instead of a stream
The first argument to toBuffer is optional, it specifies the image format
*/
gm('img.jpg')
.resize(100, 100)
.toBuffer('PNG',function (err, buffer) {
  if (err) return handle(err);
  console.log('done!');
})
```

## Custom Arguments

If `gm` does not supply you with a method you need or does not work as you'd like, you can simply use `gm().in()` or `gm().out()` to set your own arguments.

- `gm().command()` - Custom command such as `identify` or `convert`
- `gm().in()` - Custom input arguments
- `gm().out()` - Custom output arguments

The command will be formatted in the following order:

1. `command` - ie `convert`
2. `in` - the input arguments
3. `source` - stdin or an image file
4. `out` - the output arguments
5. `output` - stdout or the image file to write to

For example, suppose you want the following command:

```bash
gm "convert" "label:Offline" "PNG:-"
```

However, using `gm().label()` may not work as intended for you:

```js
gm()
.label('Offline')
.stream();
```

would yield:

```bash
gm "convert" "-label" "\"Offline\"" "PNG:-"
```

Instead, you can use `gm().out()`:

```js
gm()
.out('label:Offline')
.stream();
```

which correctly yields:

```bash
gm "convert" "label:Offline" "PNG:-"
```

### Custom Identify Format String

When identifying an image, you may want to use a custom formatting string instead of using `-verbose`, which is quite slow.
You can use your own [formatting string](http://www.imagemagick.org/script/escape.php) when using `gm().identify(format, callback)`.
For example,

```js
gm('img.png').format(function (err, format) {

})

// is equivalent to

gm('img.png').identify('%m', function (err, format) {

})
```

since `%m` is the format option for getting the image file format.

## Platform differences

Please document and refer to any [platform or ImageMagick/GraphicsMagick issues/differences here](https://github.com/aheckmann/gm/wiki/GraphicsMagick-and-ImageMagick-versions).

## Examples:

  Check out the [examples](http://github.com/aheckmann/gm/tree/master/examples/) directory to play around.
  Also take a look at the [extending gm](http://wiki.github.com/aheckmann/gm/extending-gm)
  page to see how to customize gm to your own needs.

## Constructor:

  There are a few ways you can use the `gm` image constructor.

  - 1) `gm(path)` When you pass a string as the first argument it is interpreted as the path to an image you intend to manipulate.
  - 2) `gm(stream || buffer, [filename])` You may also pass a ReadableStream or Buffer as the first argument, with an optional file name for format inference.
  - 3) `gm(width, height, [color])` When you pass two integer arguments, gm will create a new image on the fly with the provided dimensions and an optional background color. And you can still chain just like you do with pre-existing images too. See [here](http://github.com/aheckmann/gm/blob/master/examples/new.js) for an example.

The links below refer to an older version of gm but everything should still work, if anyone feels like updating them please make a PR

## Methods

  - getters
    - [size](http://aheckmann.github.io/gm/docs.html#getters) - returns the size (WxH) of the image
    - [orientation](http://aheckmann.github.io/gm/docs.html#getters) - returns the EXIF orientation of the image
    - [format](http://aheckmann.github.io/gm/docs.html#getters) - returns the image format (gif, jpeg, png, etc)
    - [depth](http://aheckmann.github.io/gm/docs.html#getters) - returns the image color depth
    - [color](http://aheckmann.github.io/gm/docs.html#getters) - returns the number of colors
    - [res](http://aheckmann.github.io/gm/docs.html#getters)   - returns the image resolution
    - [filesize](http://aheckmann.github.io/gm/docs.html#getters) - returns image filesize
    - [identify](http://aheckmann.github.io/gm/docs.html#getters) - returns all image data available. Takes an optional format string.

  - manipulation
    - [adjoin](http://aheckmann.github.io/gm/docs.html#adjoin)
    - [affine](http://aheckmann.github.io/gm/docs.html#affine)
    - [antialias](http://aheckmann.github.io/gm/docs.html#antialias)
    - [append](http://aheckmann.github.io/gm/docs.html#append)
    - [authenticate](http://aheckmann.github.io/gm/docs.html#authenticate)
    - [autoOrient](http://aheckmann.github.io/gm/docs.html#autoOrient)
    - [average](http://aheckmann.github.io/gm/docs.html#average)
    - [backdrop](http://aheckmann.github.io/gm/docs.html#backdrop)
    - [bitdepth](http://aheckmann.github.io/gm/docs.html#bitdepth)
    - [blackThreshold](http://aheckmann.github.io/gm/docs.html#blackThreshold)
    - [bluePrimary](http://aheckmann.github.io/gm/docs.html#bluePrimary)
    - [blur](http://aheckmann.github.io/gm/docs.html#blur)
    - [border](http://aheckmann.github.io/gm/docs.html#border)
    - [borderColor](http://aheckmann.github.io/gm/docs.html#borderColor)
    - [box](http://aheckmann.github.io/gm/docs.html#box)
    - [channel](http://aheckmann.github.io/gm/docs.html#channel)
    - [charcoal](http://aheckmann.github.io/gm/docs.html#charcoal)
    - [chop](http://aheckmann.github.io/gm/docs.html#chop)
    - [clip](http://aheckmann.github.io/gm/docs.html#clip)
    - [coalesce](http://aheckmann.github.io/gm/docs.html#coalesce)
    - [colors](http://aheckmann.github.io/gm/docs.html#colors)
    - [colorize](http://aheckmann.github.io/gm/docs.html#colorize)
    - [colorMap](http://aheckmann.github.io/gm/docs.html#colorMap)
    - [colorspace](http://aheckmann.github.io/gm/docs.html#colorspace)
    - [comment](http://aheckmann.github.io/gm/docs.html#comment)
    - [compose](http://aheckmann.github.io/gm/docs.html#compose)
    - [compress](http://aheckmann.github.io/gm/docs.html#compress)
    - [contrast](http://aheckmann.github.io/gm/docs.html#contrast)
    - [convolve](http://aheckmann.github.io/gm/docs.html#convolve)
    - [createDirectories](http://aheckmann.github.io/gm/docs.html#createDirectories)
    - [crop](http://aheckmann.github.io/gm/docs.html#crop)
    - [cycle](http://aheckmann.github.io/gm/docs.html#cycle)
    - [deconstruct](http://aheckmann.github.io/gm/docs.html#deconstruct)
    - [delay](http://aheckmann.github.io/gm/docs.html#delay)
    - [define](http://aheckmann.github.io/gm/docs.html#define)
    - [density](http://aheckmann.github.io/gm/docs.html#density)
    - [despeckle](http://aheckmann.github.io/gm/docs.html#despeckle)
    - [dither](http://aheckmann.github.io/gm/docs.html#dither)
    - [displace](http://aheckmann.github.io/gm/docs.html#dither)
    - [display](http://aheckmann.github.io/gm/docs.html#display)
    - [dispose](http://aheckmann.github.io/gm/docs.html#dispose)
    - [dissolve](http://aheckmann.github.io/gm/docs.html#dissolve)
    - [edge](http://aheckmann.github.io/gm/docs.html#edge)
    - [emboss](http://aheckmann.github.io/gm/docs.html#emboss)
    - [encoding](http://aheckmann.github.io/gm/docs.html#encoding)
    - [enhance](http://aheckmann.github.io/gm/docs.html#enhance)
    - [endian](http://aheckmann.github.io/gm/docs.html#endian)
    - [equalize](http://aheckmann.github.io/gm/docs.html#equalize)
    - [extent](http://aheckmann.github.io/gm/docs.html#extent)
    - [file](http://aheckmann.github.io/gm/docs.html#file)
    - [filter](http://aheckmann.github.io/gm/docs.html#filter)
    - [flatten](http://aheckmann.github.io/gm/docs.html#flatten)
    - [flip](http://aheckmann.github
... [TRUNCATED]
```

### File: test\index.js
```js
const cp = require('child_process');
const path = require('path');
const Async = require('async');
const dir = path.join(__dirname, '..', 'examples', 'imgs');
const gm = require('..');
const fs = require('fs');
const os = require('os');

const only = process.argv.slice(2);
gm.integration = !! ~process.argv.indexOf('--integration');
if (gm.integration) only.shift();

let files = fs.readdirSync(__dirname).filter(filter);
if (files.length === 0) {
  console.log('No tests found matching', only);
}

function filter (file) {
  if (!/\.js$/.test(file)) return false;
  if ('index.js' === file) return false;
  if (only.length && !~only.indexOf(file)) return false;

  var filename = path.join(__dirname, file);
  if (!fs.statSync(filename).isFile()) return false;
  return true;
}

const originalPathName = path.join(dir, 'original.jpg');

function test (imageMagick) {
  return gm(originalPathName).options({ imageMagick });
}

function finish (filename) {
  return function (err) {
    if (err) {
      console.error('\n\nError occured with file: ' + filename);
      throw err;
    }
  }
}

function isGraphicsMagickInstalled() {
  try {
    cp.execSync('gm -version');
    return true;
  } catch (_) {
    return false;
  }
}

function isConvertInstalled() {
  try {
    cp.execSync('convert -version');
    return true;
  } catch (_) {
    return false;
  }
}

function isMagickInstalled() {
  try {
    cp.execSync('magick -version');
    return true;
  } catch (_) {
    return false;
  }
}

const isWindows = () => os.platform() === 'win32';

var q = Async.queue(function (task, callback) {
  var filename = task.filename;
  var im = task.imagemagick;

  console.log(`Testing ${filename} ..`);
  require(filename)(test(im), dir, function (err) {
    finish(filename)(err);
    callback();
  }, gm, im);
}, 1);

q.drain = function(){
  console.log("\n\u001B[32mAll tests passed\u001B[0m");
};

files = files.map(function (file) {
  return path.join(__dirname, file);
});

if (isGraphicsMagickInstalled()) {
  console.log('gm is installed');
  files.forEach(function (filename) {
    q.push({
      imagemagick: false,
      filename
    })
  });
}

if (!isWindows() && isConvertInstalled()) {
  // windows has a different convert binary

  console.log('convert is installed');
  files.forEach(function (filename) {
    q.push({
      imagemagick: true,
      filename
    })
  });
}

if (isMagickInstalled()) {
  console.log('magick is installed');

  files.forEach(function (filename) {
    q.push({
      imagemagick: '7+',
      filename
    })
  });
}
```

### File: History.md
```md
1.25.1 / 2025-02-24

* deps: bump cross-spawn [talyuk](https://github.com/talyuk)

1.25.0 / 2022-09-21

* fixed: windows support #846, #774, #594, #524, #528, #559, #652, #682 [piotr-cz](https://github.com/piotr-cz)
* docs; improvements from #821 [agokhale](https://github.com/agokhale)
* docs; improvements #801 [aarongarciah](https://github.com/aarongarciah)

1.24.0 / 2022-09-18

* fixed: infering format of buffered or streamed ico files #429 freund17
* fixed; preserve color info duing autoOrient() #714, #844 reco
* tests; switch to Github Actions
* docs; fix links #834 delesseps
* docs; clarify install directions #689 PatrykMiszczak
* refactor; clean up compare.js #788 LongTengDao

1.23.1 / 2017-12-27

 * fixed: use debug > 2.6.9 because of security issue #685 danez
 * tests; add nsp check
 * tests; get tests passing on OSX

1.23.0 / 2016-08-03

 * fixed; webpack support #547 sean-shirazi
 * fixed; windows support - use cross-spawn to spawn processes #537 bdukes
 * added; allow thumbnail to accept the same options as resize #527 Sebmaster
 * added; dispose support #487 dlwr
 * docs; add example of loading image from URL #544 wahengchang
 * docs; Fix a link in README.md #532 clbn
 * travis; update travis versions #551 amilajack

1.22.0 / 2016-04-07

 * fixed; identity parser: support multi-value keys by creating an array #508 #509 [emaniacs](https://github.com/emaniacs)
 * fixed; error handling if gm is not installed #499 [aeo3](https://github.com/aeo3)
 * fixed; highlightColor typo in compare #504 [DanielHudson](https://github.com/DanielHudson)
 * docs; Fix typo #475 [rodrigoalviani](https://github.com/rodrigoalviani)

1.21.1 / 2015-10-26

* fixed: Fixed #465 hard coded gm binary, also fixed issues with compare and fixed tests so they will fail on subsequent runs when they should do [rwky](https://github.com/rwky)

1.21.0 / 2015-10-26 **contains security fix**

* fixed: gm.compare fails to escape arguments properly (Reported by Brendan Scarvell) [rwky](https://github.com/rwky)

1.20.0 / 2015-09-23

* changed: Reverted "Add format inference from filename for buffers/streams" due to errors #448

1.19.0 / 2015-09-16

* changed: Added error to notify about image magick not supporting minify [encima](https://github.com/encima)
* changed: Refactored orientation getter to use faster identify call [lbeschastny](https://github.com/lbeschastny)
* added: resizeExact function [DanMMX](https://github.com/DanMMX)
* added: thumbExact function [DanMMX](https://github.com/DanMMX)
* added: Add format inference from filename for buffers/streams [adurrive](https://github.com/adurrive)
* fixed: Hex values when passed to compare aren't quoted automatically [DanMMX](https://github.com/DanMMX)
* fixed: identify returning last frame size instead of the larges on animated gifs [preynal](https://github.com/preynal)
* docs: Updated docs [laurilehmijoki](https://github.com/laurilehmijoki)

1.18.1 / 2015-05-18

* changed: Added io.js support [rwky](https://github.com/rwky)

1.18.0 / 2015-05-18

* changed: Removed support for node 0.8 and added support for 0.12 [rwky](https://github.com/rwky)
* changed: Listen to stdin error event for spawn errors [kapouer](https://github.com/kapouer)
* changed: Improved error handling when gm isn't installed [FreshXOpenSource](https://github.com/FreshXOpenSource)
* changed: Allow append method to use an array of arguments [emohacker](https://github.com/emohacker)
* changed: appPath option now specifies full path to gm binary John Borkowski
* changed: Ignore warning messages for identify [asrail](https://github.com/asrail)
* added: Montage method [donaldpcook](https://github.com/donaldpcook)
* added: Progressive option to thumb [mohebifar](https://github.com/mohebifar)
* added: Native gm auto-orient for use with gm >= 1.3.18 [bog](https://github.com/bog)
* added: Timeout support by passing the timeout option in milliseconds [marcbachmann](https://github.com/marcbachmann)
* fixed: density when using ImageMagick [syzer](https://github.com/syzer)
* fixed: resize behaviour for falsy values [adius](https://github.com/adius)


1.17.0 / 2014-10-28
==================

 * changed: extended compare callback also returns the file names #297 [mastix](https://github.com/mastix)
 * changed: pass spawn crash to callback #306 [medikoo](https://github.com/medikoo)
 * changed: geometry supports arbitary string as first argument #330 [jdiez17](https://github.com/jdiez17)
 * added: support for repage+ option #275 [desigens](https://github.com/desigens)
 * added: added the dissolve command #300 [microadm](https://github.com/microadam)
 * added: composite method #332 [jdiez17](https://github.com/jdiez17)
 * fixed: cannot set tolerance to 0 #302 [rwky](https://github.com/rwky)
 * fixed: handle empty buffers #330 [alcidesv](https://github.com/alcidesv)

1.16.0 / 2014-05-09
==================

 * fixed; dropped "+" when 0 passed as vertical roll amt #267 [dwtkns](https://github.com/dwtkns)
 * added; highlight-style support #272 [fdecampredon](https://github.com/fdecampredon)

1.15.0 / 2014-05-03
===================

 * changed; gm.compare logic to always run the mse comparison as expected #258 [Vokkim](https://github.com/Vokkim)
 * added; `tolerance` to gm.compare options object #258 [Vokkim](https://github.com/Vokkim)
 * added; option to set ImageMagick application path explicitly #250 (akreitals)
 * fixed; gm.compare: support values like 9.51582e-05 #260 [normanrz](https://github.com/normanrz)
 * README: add call for maintainers

1.14.2 / 2013-12-24
===================

* fixed; background is now a setting #246 (PEM--)

1.14.1 / 2013-12-09
===================

* fixed; identify -verbose colon behavior #240 ludow

1.14.0 / 2013-12-04
===================

* added; compare method for imagemagick (longlho)

1.13.3 / 2013-10-22
===================

* fixed; escape diffOptions.file in compare (dwabyick)

1.13.2 / 2013-10-18
===================

* fixed; density is a setting not an operator

1.13.1 / 2013-09-15
===================

* added; boolean for % crop

1.13.0 / 2013-09-07
===================

* added; morph more than two images (overra)

1.12.2 / 2013-08-29
===================

* fixed; fallback to through in node 0.8

1.12.1 / 2013-08-29 (unpublished)
===================

* refactor; replace through with stream.PassThrough

1.12.0 / 2013-08-27
===================

* added; diff image output file (chenglou)

1.11.1 / 2013-08-17
===================

* added; proto.selectFrame(#)
* fixed; getters should not ignore frame selection

1.11.0 / 2013-07-23
===================

* added; optional formatting string for gm().identify(format, callback) (tornillo)
* removed; error messages when gm/im binary is not installed

1.10.0 / 2013-06-27
===================

* refactor; use native `-auto-orient` for imagemagick

1.9.2 / 2013-06-12
==================

  * refactor; move `streamToBuffer` to a separate module
  * fixed; .stream(format) without a callback

1.9.1 / 2013-05-07
==================

  * fixed; gm().resize(width) always only resizes width
  * fixed; gm('img.gif').format() returns the format of the first frame

1.9.0 / 2013-04-21
==================

  * added; node v0.10 support
  * removed; node < v0.8 support - `Buffer.concat()`
  * tests; all tests now run on Travis
  * added; gm().stream() returns a stream when no callback is present
  * added; gm().toBuffer(callback)
  * fixed; gm().size() only returns the size of the first frame of a GIF

1.8.2 / 2013-03-07
==================

  * include source path in identify data #126 [soupdiver](https://github.com/soupdiver)

1.8.1 / 2012-12-21
==================

  * Avoid losing already set arguments on identify #105 #113 #109 [JNissi](https://github.com/JNissi)
  * tests; add autoOrient + thumb() test
  * tests; add test case for #113
  * tests; added test for #109
  * tests; add resize on buffer test

1.8.0 / 2012-12-14
==================

  * added; geometry support to scale() #98
  * removed; incorrect/broken dissolve() method (never worked)
  * fixed; handle child_proc error when using Buffer input #109
  * fixed; use of Buffers with identify() #109
  * fixed; no longer include -size arg with resize() #98
  * fixed; remove -size arg from extent() #103
  * fixed; magnify support
  * fixed; autoOrient to work with all types of exif orientations [dambalah](https://github.com/dambalah) #108
  * tests; npm test runs unit only (now compatible with travis)
  * tests; fix magnify test on imagemagick
  * tests; added for cmd line args

1.7.0 / 2012-12-06
==================

  * added; gm.compare support
  * added; passing Buffers directly [danmilon](https://github.com/danmilon)

1.6.1 / 2012-11-13
==================

  * fixed regression; only pass additional params on error #96

1.6.0 / 2012-11-10
==================

  * changed; rename internal buffer to _buffer #88 [kof](https://github.com/kof)
  * changed; optimized identify getters (format, depth, size, color, filesize). #83 please read this for details: https://github.com/aheckmann/gm/commit/8fcf3f8f84a02cc2001da874cbebb89bf7084409
  * added; visionmedia/debug support
  * added; `gm convert -thumbnail` support. _differs from thumb()._ [danmilon](https://github.com/danmilon)
  * fixed; -rotate 0 support #90
  * fixed; multi-execution of same gm instance arguments corruption
  * fixed; gracefully handle parser errors #94 [eldilibra](https://github.com/eldilibra)

1.5.1 / 2012-10-02
==================

  * fixed; passing multiple paths to append() #77

1.5.0 / 2012-09-15
==================

  * fixed; callback scope
  * fixed; append() usage #77

1.4.2 / 2012-08-17
==================

  * fixed; identify parsing for ImageMagick exif data (#58)
  * fixed; when in imageMagick mode, complain about missing imageMagick [bcherry](https://github.com/bcherry) (#73)
  * added; tests

1.4.1 / 2012-07-31
==================

  * fixed; scenes() args
  * fixed; accept the left-to-right arg of append()
  * added; _subCommand

## v1.4 - 07/28/2012

  * added; adjoin() [Math-]
  * added; affine() [Math-]
  * added; append() [Math-]
  * added; authenticate() [Math-]
  * added; average() [Math-]
  * added; backdrop() [Math-]
  * added; blackThreshold() [Math-]
  * added; bluePrimary() [Math-]
  * added; border() [Math-]
  * added; borderColor() [Math-]
  * added; box() [Math-]
  * added; channel() [Math-]
  * added; clip() [Math-]
  * added; coalesce() [Math-]
  * added; colorMap() [Math-]
  * added; compose() [Math-]
  * added; compress() [Math-]
  * added; convolve() [Math-]
  * added; createDirectories() [Math-]
  * added; deconstruct() [Math-]
  * added; delay() [Math-]
  * added; define() [Math-]
  * added; displace() [Math-]
  * added; display() [Math-]
  * added; dispose() [Math-]
  * added; disolve() [Math-]
  * added; encoding() [Math-]
  * added; endian() [Math-]
  * added; file() [Math-]
  * added; flatten() [Math-]
  * added; foreground() [Math-]
  * added; frame() [Math-]
  * added; fuzz() [Math-]
  * added; gaussian() [Math-]
  * added; geometry() [Math-]
  * added; greenPrimary() [Math-]
  * added; highlightColor() [Math-]
  * added; highlightStyle() [Math-]
  * added; iconGeometry() [Math-]
  * added; intent() [Math-]
  * added; lat() [Math-]
  * added; level() [Math-]
  * added; list() [Math-]
  * added; log() [Math-]
  * added; map() [Math-]
  * added; matte() [Math-]
  * added; matteColor() [Math-]
  * added; mask() [Math-]
  * added; maximumError() [Math-]
  * added; mode() [Math-]
  * added; monitor() [Math-]
  * added; mosaic() [Math-]
  * added; motionBlur() [Math-]
  * added; name() [Math-]
  * added; noop() [Math-]
  * added; normalize() [Math-]
  * added; opaque() [Math-]
  * added; operator() [Math-]
  * added; orderedDither() [Math-]
  * added; outputDirectory() [Math-]
  * added; page() [Math-]
  * added; pause() [Math-]
  * added; pen() [Math-]
  * added; ping() [Math-]
  * added; pointSize() [Math-]
  * added; preview() [Math-]
  * added; process() [Math-]
  * added; profile() [Math-]
  * added; progress() [Math-]
  * added; rawSize() [Math-]
  * added; randomThreshold() [Math-]
  * added; recolor() [Math-]
  * added; redPrimary() [Math-]
  * added; remote() [Math-]
  * added; render() [Math-]
  * added; repage() [Math-]
  * added; sample() [Math-]
  * added; samplingFactor() [Math-]
  * added; scene() [Math-]
  * added; scenes() [Math-]
  * added; screen() [Math-]
  * added; segment() [Math-]
  * added; set() [Math-]
  * added; shade() [Math-]
  * added; shadow() [Math-]
  * added; sharedMemory() [Math-]
  * added; shave() [Math-]
  * added; shear() [Math-]
  * added; silent() [Math-]
  * added; snaps() [Math-]
  * added; stagano() [Math-]
  * added; stereo() [Math-]
  * added; textFont() [Math-]
  * added; texture() [Math-]
  * added; threshold() [Math-]
  * added; tile() [Math-]
  * added; transform() [Math-]
  * added; transparent() [Math-]
  * added; treeDepth() [Math-]
  * added; update() [Math-]
  * added; units() [Math-]
  * added; unsharp() [Math-]
  * added; usePixmap() [Math-]
  * added; view() [Math-]
  * added; virtualPixel() [Math-]
  * added; visual() [Math-]
  * added; watermark() [Math-]
  * added; wave() [Math-]
  * added; whitePoint() [Math-]
  * added; whiteThreshold() [Math-]
  * added; window() [Math-]
  * added; windowGroup() [Math-]

## v1.3.2 - 06/22/2012

  * added; node >= 0.7/0.8 compat

## v1.3.1 - 06/06/2012

  * fixed; thumb() alignment and cropping [thomaschaaf]
  * added; hint when graphicsmagick is not installed (#62)
  * fixed; minify() (#59)

## v1.3.0 - 04/11/2012

  * added; flatten support [jwarchol]
  * added; background support [jwarchol]
  * fixed; identify parser error [chriso]

## v1.2.0 - 03/30/2012

  * added; extent and gravity support [jwarchol]

## v1.1.0 - 03/15/2012

  * added; filter() support [travisbeck]
  * added; density() [travisbeck]
  * fixed; permit either width or height in resize [dambalah]
  * updated; docs

## v1.0.5 - 02/15/2012

  * added; strip() support [Math-]
  * added; interlace() support [Math-]
  * added; setFormat() support [Math-]
  * fixed; regexps for image types [Math-]

## v1.0.4 - 02/09/2012

  * expose utils

## v1.0.3 - 01/27/2012

  * removed; console.log

## v1.0.2 - 01/24/2012

  * added; debugging info on parser errors
  * fixed; exports.version

## v1.0.1 - 01/12/2012

  * fixed; use of reserved keyword `super` for node v0.5+

## v1.0.0 - 01/12/2012

  * added; autoOrient support [kainosnoema] (#21)
  * added; orientation support [kainosnoema] (#21)
  * fixed; identify parser now properly JSON formats all data output by `gm identify` such as IPTC, GPS, Make, etc (#20)
  * added; support for running as imagemagick (#23, #29)
  * added; subclassing support; useful for setting default constructor options like one constructor for ImageMagick, the other for GM
  * added; more tests
  * changed; remove redundant `orientation`, `resolution`, and `filesize` from `this.data` in `indentify()`. Use their uppercase equivalents.

## v0.6.0 - 12/14/2
... [TRUNCATED]
```

### File: examples\append.js
```js
var gm = require('../')
  , dir = __dirname + '/imgs'
  , imgs = 'lost.png original.jpg'.split(' ').map(function (img) {
      return dir + '/' + img
    })
  , out = dir + '/append.jpg'

gm(imgs[0])
.append(imgs[1])
.append()
.background('#222')
.write(out, function (err) {
  if (err) return console.dir(arguments)
  console.log(this.outname + " created  ::  " + arguments[3])
  require('child_process').exec('open ' + out)
});


```

### File: examples\background.js
```js
var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + "/original.jpg")
  .crop(140,100)
  .background("#FF0000")
  .extent(340,300)
  .write(dir + '/background.jpg', function (err) {
    if (err) return console.dir(arguments)
    console.log(this.outname + " created  ::  " + arguments[3])
});


```

### File: examples\bitdepth.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.png')
  .bitdepth(2)
  .write(dir + '/bitdepth.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + ' created :: ' + arguments[3])
  }
) 

```

### File: examples\blur.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.png')
  .blur(19, 10)
  .write(dir + '/blur.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + ' created  :: ' + arguments[3])
  }
) 

```

### File: examples\changeFormat.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'
  
gm(dir + '/original.png')
  .write(dir + '/original.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + " created  ::  " + arguments[3])
  }
) 

```

### File: examples\charcoal.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.png')
  .charcoal(1)
  .write(dir + '/charcoal.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + ' created  :: ' + arguments[3])
  }
) 

```

### File: examples\chop.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'
  
gm(dir + '/original.png')
  .chop(54, 1, 307, 1)
  .write(dir + "/chop.jpg", function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + " created  ::  " + arguments[3])
  }
) 

```

### File: examples\colorize.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.png')
  .colorize(80, 0, 30)
  .write(dir + '/colorize.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + ' created  :: ' + arguments[3])
  }
) 

```

### File: examples\colors.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.png')
  .colors(16)
  .write(dir + '/colors.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + ' created  :: ' + arguments[3])
  }
) 

```

### File: examples\comment.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.png')
  .comment("%m:%f %wx%h")
  .write(dir + '/comment.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + ' created  :: ' + arguments[3])
  }
) 

```

### File: examples\compare.js
```js
var gm = require('../')
  , dir = __dirname + '/imgs'
  , imgs = 'bitdepth.png original.jpg'.split(' ').map(function (img) {
      return dir + '/' + img
    })
  , out = dir + '/compare.jpg'

gm.compare(imgs[0], imgs[1], { highlightColor: "#fff", file: out }, function (err) {
  if (err) return console.dir(arguments)
  console.log('The images are equal: %s', arguments[1]);
  console.log('Actual equality: %d', arguments[2]);
  console.log(this.outname + " created  ::  " + arguments[3]);
  require('child_process').exec('open ' + out);
});


```

### File: examples\contrast.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.png')
  .contrast(2)
  .write(dir + '/contrast.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + ' created :: ' + arguments[3])
  }
) 

```

### File: examples\crop.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'
  
gm(dir + '/original.png')
  .crop(200, 155, 300, 0)
  .write(dir + "/crop.jpg", function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + " created  ::  " + arguments[3])
  }
) 

```

### File: examples\cycle.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.png')
  .cycle(4)
  .write(dir + '/cycle.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + ' created :: ' + arguments[3])
  }
) 

```

### File: examples\despeckle.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.png')
  .despeckle()
  .write(dir + '/despeckle.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + ' created :: ' + arguments[3])
  }
) 

```

### File: examples\dither.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.png')
  .monochrome()
  .dither()
  .write(dir + '/dither.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + ' created :: ' + arguments[3])
  }
) 

```

### File: examples\drawing.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.png')
  .blur(8, 4)
  .stroke("red", 7)
  .fill("#ffffffbb")
  .drawLine(20, 10, 50, 40)
  .fill("#2c2")
  .stroke("blue", 1)
  .drawRectangle(40, 10, 50, 20)
  .drawRectangle(60, 10, 70, 20, 3)
  .drawArc(80, 10, 90, 20, 0, 180)
  .drawEllipse(105, 15, 3, 5)
  .drawCircle(125, 15, 120, 15)
  .drawPolyline([140, 10], [143, 13], [145, 13], [147, 15], [145, 17], [143, 19])
  .drawPolygon([160, 10], [163, 13], [165, 13], [167, 15], [165, 17], [163, 19])
  .drawBezier([180, 10], [183, 13], [185, 13], [187, 15], [185, 17], [183, 19])
  .fontSize(68)
  .stroke("#efe", 2)
  .fill("#888")
  .drawText(-20, 98, "graphics magick")
  .write(dir + '/drawing.png', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + ' created  :: ' + arguments[3])
  }
) 

```

### File: examples\edge.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.png')
  .edge(2)
  .write(dir + '/edge.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + ' created :: ' + arguments[3])
  }
) 

```

### File: examples\emboss.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.png')
  .emboss(2)
  .write(dir + '/emboss.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + ' created :: ' + arguments[3])
  }
) 

```

### File: examples\enhance.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.png')
  .enhance()
  .write(dir + '/enhance.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + ' created :: ' + arguments[3])
  }
) 

```

### File: examples\equalize.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.png')
  .equalize()
  .write(dir + '/equalize.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + ' created :: ' + arguments[3])
  }
) 

```

### File: examples\extent.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.jpg')
  .resize(200,100)
  .extent(300, 300)
  .write(dir + '/extent.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + " created  ::  " + arguments[3])
  }
)

```

### File: examples\flatten.js
```js
// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/layers.psd')
  .flatten()
  .write(dir + "/unlayered.jpg", function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + " created  ::  " + arguments[3])
  }
)

```

### File: examples\flip.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.png')
  .flip()
  .write(dir + '/flip.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + " created :: " + arguments[3])
  }
) 

```

### File: examples\flop.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.png')
  .flop()
  .write(dir + '/flop.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + " created :: " + arguments[3])
  }
) 

```

### File: examples\gamma.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.png')
  .gamma(1.7, 2.3, 1.3)
  .write(dir + '/gamma.png', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + ' created :: ' + arguments[3])
  }
) 

```

### File: examples\getters.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

var methods = 
[ "size"
, "identify"
, "format"
, "depth"
, "color"
, "res"
, "filesize"
]

var image = gm(dir + '/original.png')
methods.forEach(function(method){
  image[method](function(err, result){
    console.log(method + " result:")
    console.dir(result)
  })
})


```

### File: examples\gravity.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.jpg')
  .resize(200,100)
  .gravity("South") // Be sure to use gravity BEFORE extent
  .extent(300, 300)
  .write(dir + '/gravity.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + " created  ::  " + arguments[3])
  }
)

```

### File: examples\implode.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.png')
  .implode(0.8)
  .write(dir + '/implode.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + ' created :: ' + arguments[3])
  }
) 

```

### File: examples\label.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.png')
  .label("%m:%f %wx%h")
  .write(dir + '/label.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + ' created  :: ' + arguments[3])
  }
) 

```

### File: examples\limit.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.png')
  .limit("memory", "32MB")
  .limit("map", "64MB")
  .write(dir + '/limit.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + ' created  :: ' + arguments[3])
  }
) 

```

### File: examples\lower.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.png')
  .lower(10, 14)
  .write(dir + '/lower.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + ' created :: ' + arguments[3])
  }
) 

```

### File: examples\magnify.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'
  
gm(dir + '/original.png')
  .magnify()
  .write(dir + '/magnify.png', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + " created  ::  " + arguments[3])
  }
) 

```

### File: examples\median.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.png')
  .median(4)
  .write(dir + '/median.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + ' created :: ' + arguments[3])
  }
) 

```

### File: examples\minify.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs' 
gm(dir + '/original.png')
  .minify()
  .write(dir + '/minify.png', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + " created  ::  " + arguments[3])
  }
) 
```

### File: examples\modulate.js
```js

// gm - Copyright Aaron Heckmann <aaron.heckmann+github@gmail.com> (MIT Licensed)

var gm = require('../')
  , dir = __dirname + '/imgs'

gm(dir + '/original.png')
  .modulate(120, 100, 80)
  .write(dir + '/modulate.jpg', function(err){
    if (err) return console.dir(arguments)
    console.log(this.outname + ' created  :: ' + arguments[3])
  }
) 

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

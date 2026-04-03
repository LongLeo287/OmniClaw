---
id: github.com-jhuckaby-pixl-logger-d603e49b-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:15.368511
---

# KNOWLEDGE EXTRACT: github.com_jhuckaby_pixl-logger_d603e49b
> **Extracted on:** 2026-04-01 17:05:44
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007525494/github.com_jhuckaby_pixl-logger_d603e49b

---

## File: `.npmignore`
```
.gitignore
node_modules/
```

## File: `README.md`
```markdown
<details><summary>Table of Contents</summary>

<!-- toc -->
- [Overview](#overview)
- [Usage](#usage)
	* [Constructor Args](#constructor-args)
	* [Data Cleansing](#data-cleansing)
	* [Shortcut Methods](#shortcut-methods)
		+ [debug](#debug)
			- [shouldLog](#shouldlog)
		+ [error](#error)
		+ [transaction](#transaction)
	* [Echo to Console](#echo-to-console)
		+ [Colored Logs](#colored-logs)
	* [Last Line Logged](#last-line-logged)
	* [Special Column Names](#special-column-names)
		+ [epoch](#epoch)
		+ [hires_epoch](#hires_epoch)
		+ [date](#date)
		+ [hostname](#hostname)
		+ [pid](#pid)
		+ [data](#data)
		+ [category](#category)
	* [Special Hooks](#special-hooks)
		+ [pather](#pather)
		+ [filter](#filter)
		+ [serializer](#serializer)
		+ [echoer](#echoer)
	* [Rotating Logs](#rotating-logs)
	* [Archiving Logs](#archiving-logs)
	* [Sync or Async](#sync-or-async)
	* [Buffering](#buffering)
	* [Approximate Time](#approximate-time)
- [License](#license)

</details>

# Overview

This module provides a simple logging class, which appends to a text log file with bracket-delimited columns.  You can define any number of columns you want, or use some of the built-in auto-populated columns.  You can populate columns by name, or by using one of the shortcut methods described below.

# Usage

Use [npm](https://www.npmjs.com/) to install the module:

```sh
npm install pixl-logger
```

Then use `require()` to load it in your code:

```js
const Logger = require('pixl-logger');
```

To use the module, instantiate an object, and start logging:

```js
let columns = ['hires_epoch', 'date', 'hostname', 'component', 'category', 'code', 'msg', 'data'];
let logger = new Logger( 'logs/debug.log', columns );
logger.set('hostname', 'myserver.com');

logger.print({
	category: 'debug',
	component: 'main',
	code: 1,
	msg: "Hello log!"
});
```

This would append the following like to `logs/debug.log`:

```
[1423462332.437][2015-02-08 22:12:12][myserver.com][main][debug][1][Hello log!][]
```

Some column names are special or automatically populated (see [Special Column Names](#special-column-names)), but the rest are free-form.  You can include any number of columns you like, and name them however you want.

All the log "columns" are basically just key/value pairs stored in an `args` property in the class, which don't have to be specified on every call to `print()`.  Meaning, you can set some of them once, and only have to set them again when they change.  Example:

```js
logger.set('component', 'main');
logger.set('category', 'debug');

logger.print({
	code: 1,
	msg: "Hello log!"
});
```

Note that when you pass arguments to `print()` they are not saved for subsequent calls.  They are only used for that one log row.  You need to call `set()` to make them stick.

You can also fetch arg values using `get()`.  Pass in a key to fetch one arg, or omit to get the entire `args` object back.

## Constructor Args

You can specify one or more args in the constructor, by passing in an object after the log columns.  Example:

```js
let logger = new Logger( log_file, log_columns, {
	hostname: 'myhost.com',
	custom_column: 1234,
	sync: false
} );
```

These properties can include your own custom column keys, and also built-in args like `sync`, `echo` and `color`.

## Data Cleansing

In order to protect the log format and syntax, all column values are "cleansed" before being written.  Specifically, any newlines are converted to single spaces, and the character sequence `][` is stripped (as it would corrupt the log column layout).  All other characters are allowed.  Example:

```js
logger.debug( 1, "This won't go well\n[Hi][There]\r\nGoodbye.\n" );
```

This would be logged as:

```
[1423466726.159][2015-02-08 23:25:26][myserver.com][main][debug][1][This won't go well [HiThere]  Goodbye. ]
```

## Shortcut Methods

The logger library provides the following three shortcut methods, which accept a list of common arguments instead of a hash:

### debug

The `debug()` method is designed to assist with writing to a debug log.  It automatically sets the `category` column to `debug`.  It requires two arguments, which are values for the `code` (debug level) and `msg` columns, with the 3rd argument being an optional `data` object, if you want.  Examples:

```js
logger.debug( 1, "Logged at debug level 1" );
logger.debug( 2, "Logged at debug level 2", {some:"data"} );
```

An extra feature with the `debug()` call is that you can set a `debugLevel` arg on your class instance, and it'll only log entries if they have an *equal or lower level* (a.k.a. code).  So imagine this setup:

```js
logger.set( 'debugLevel', 2 );

logger.debug( 1, "Logged at debug level 1" );
logger.debug( 2, "Logged at debug level 2" );
logger.debug( 3, "This won't be logged at all!" );
```

In this case we set the `debugLevel` arg to 2, so only the first two calls will be logged.  The third call, which is logged at a higher (more verbose) level than the `debugLevel` value, will be silently skipped.

#### shouldLog

If you need to see if a particular debug level would be logged, you can call the `shouldLog()` method and pass in a level to query.  If the current `debugLevel` is *equal to or higher than* the level number passed in, it returns `true`, otherwise it returns `false`.  Example:

```js
if (logger.shouldLog(9)) {
	// do something here like serializing complex data into a string
	logger.debug(9, "Complex data here: " + complex_data);
}
```

The idea is that entire code block wouldn't even be executed if the `debugLevel` was less than 9, saving you the CPU time of serializing the complex data to be logged.

Keep in mind that you can simply pass an Object to `debug()` as an optional 3rd argument, and it'll automatically be serialized to JSON and logged if the debug level is acceptable.

### error

The `error()` method is designed to assist with logging errors.  It automatically sets the `category` column to `error`.  It requires two arguments, which are values for the `code` and `msg` columns, with the 3rd argument being an optional `data` object, if you want.  Example:

```js
logger.error( 1005, "An error of type 1005 occurred!" );
```

This would be equivalent to calling `print()` with the following:

```js
logger.print({
	category: 'error',
	code: 1005,
	msg: "An error of type 1005 occurred!"
});
```

### transaction

The `transaction()` method is designed to assist with logging transactions.  A "transaction" is whatever action you define in your app as something you want logged, for audit or replay purposes.  It automatically sets the `category` column to `transaction`.  It requires two arguments, which are values for the `code` and `msg` columns, with the 3rd argument being an optional `data` object, if you want.  Example:

```js
logger.transaction( "user_update", "User jhuckaby was updated", {username:"jhuckaby"} );
```

This would be equivalent to calling `print()` with the following:

```js
logger.print({
	category: 'transaction',
	code: "user_update",
	msg: "User jhuckaby was updated",
	data: {username:"jhuckaby"}
});
```

## Echo to Console

If you set the `echo` arg to any true value, the logger will echo all log entries to [process.stdout](https://nodejs.org/api/process.html#processstdout), in addition to the log file.  This is useful for running CLI scripts or your app in debug mode.  Example:

```js
logger.set( 'echo', true );
logger.debug( 1, "This will be logged and echoed to the console!" );
```

### Colored Logs

If you set the `color` arg to any true value, the logger will echo all log entries in color (assuming you have a terminal that supports color), using the [chalk](https://www.npmjs.com/package/chalk) module.  The color sequence is `gray`, `red`, `green`, `yellow`, `blue`, `magenta` and `cyan`.  If your log has more than 7 columns, the colors repeat.  The bracket dividers are printed in `dim`.  Here is a screenshot:

![Colored Log Example](https://pixlcore.com/software/pixl-logger/colored-log-example.png)

Example:

```js
logger.set( 'echo', true );
logger.set( 'color', true );
logger.debug( 1, "This will be colored in the console!" );
```

Note that the color only affects the local echo in your terminal.  The log file itself is still written in plain text.

## Last Line Logged

To grab the last line logged by the logger, pull the `lastRow` property off the class instance.  It is the fully formatted line, including an EOL.  Example:

```js
let line = logger.lastRow;
```

## Special Column Names

Several column names are special, in that they are automatically populated, or have special behavior.  Here they are:

### epoch

Any column named `epoch` will automatically be populated with the current local server time, represented in integer Epoch seconds.  Example:

```
[1423433821]
```

### hires_epoch

Any column named `hires_epoch` will automatically be populated with the current local server time, represented in high precision floating point Epoch seconds, with up to 3 digits after the decimal.  Example:

```
[1423433807.277]
```

### date

Any column named `date` will automatically be populated with a human-friendly version of the current local server time, in `YYYY-MM-DD HH:MI:SS` format.  Example:

```
[2015-02-08 14:16:58]
```

### hostname

Any column named `hostname` will automatically be populated with the server's hostname, obtained by calling [os.hostname()](https://nodejs.org/api/os.html#oshostname) once at construction.  Example:

```
[host01.mydomain.com]
```

### pid

Any column named `pid` will automatically be populated with the current Process ID (PID), obtained by calling [process.pid](https://nodejs.org/api/process.html#processpid) once at construction.  Example:

```
[13702]
```

### data

The `data` column is special, in that if it contains an object, it will be serialized to JSON.  Example:

```
[{"code":0,"description":"Success"}]
```

### category

The `category` column is only special in that the shortcut methods `debug()`, `error()` and `transaction()` automatically populate it to match their names.

## Special Hooks

There are a number of optional hooks available for you to customize your logs even further.  These can be specified in the `args` object passed to the constructor, by calling `set()`, or simply by setting them on an instance object.

### pather

The `pather` hook allows you to intercept and alter the log path on disk per each log row, and generate your own path based on the current `args` passed to the logger.  Using this you can change the log file per each log row.  Your hook function is passed the current path, and the current `args` object containing all the column keys/values.  Example:

```js
logger.pather = function(path, args) {
	return '/let/log/MyApp-' + args.category + '.log';
};
```

In this example the `category` column is used to dynamically construct the log filename.  So if the `category` column was set to `debug`, the log path would be `/let/log/MyApp-debug.log`.  This is a great way to generate multiple logs based on any criteria you want.

### filter

The `filter` hook allows you to intercept each log column value as it is being added to the columns array for serialization.  This is typically where column values are stripped of any illegal characters, and whitespace compressed.  If you specify this hook, the default cleansing operation does not take place, and your function is expected to do all the filtering necessary.  Your hook function is called *for each column* in each row, so keep that in mind for performance purposes, and passed the current column value, and its array index.  Example:

```js
logger.filter = function(value, idx) {
	if (typeof(value) == 'object') value = JSON.stringify(value);
	return value.toString().replace(/[\r\n]/g, ' ').replace(/\]\[/g, '');
};
```

Note that it is up to your filter function to convert objects into strings here, if you are trying to log any raw objects.

### serializer

The `serializer` hook allows you to intercept the log columns just as they are being serialized into a string for appending to your log file.  Using this you can completely change how your log file is formatted.  The default format is `[bracket][delimited][rows]` but you can serialize columns into any format of string you want.  Your function is passed the current columns array (filtered) and the `args` object.  For example, here is how to produce a CSV (comma-separated) log:

```js
logger.serializer = function(cols, args) {
	return cols.join(',') + "\n";
};
```

Your serializer function is expected to return a full formatted log row (line) ending in a EOL character.  However, it can also return boolean `false`, in which case the line will not be logged at all.

### echoer

The `echoer` hook allows you to control exactly how your log is echoed to the console, if [Echo to Console](#echo-to-console) mode is enabled.  The default behavior is to simply reprint the formatted log line to STDOUT, in addition to appending it to your log file.  However, if you specify the `echoer` hook, this no longer happens, and instead your function is expected to do the echoing.  The function is passed the formatted log line string (already appended to the log file), the array of columns that were serialized (these are filtered), and the current `args` object.  Example:

```js
logger.echoer = function(line, cols, args) {
	console.log( args.category + ": " + args.msg );
	if (args.data) console.dir(args.data);
};
```

In this example we are only echoing certain columns to the console (just `category` and `msg`) using the `args` object, and allowing Node.js to serialize the data column via [console.dir()](https://nodejs.org/api/console.html#consoledirobj-options).  This way if you are using a debugger, it may be navigable.

If you specify a filesystem path as the `echoer` instead of a function, it will be appended to.  Using this technique you can have the logger append to two different log files at once (the primary log and the echoer log).  This file append honors the `sync` flag as well.

Note that your `echoer` hook is only ever called if [Echo to Console](#echo-to-console) mode is enabled.

## Rotating Logs

To rotate a log file, call the `rotate()` method, passing in a destination filesystem path and a callback.  This will atomically move the file to the destination directory/filename, attempting a rename, and falling back to a "copy to temp file + rename" strategy.  Example:

```js
logger.rotate( '/logs/pickup/myapp.log', function(err) {
	if (err) throw err;
} );
```

If you omit a filename on the destination path and leave a trailing slash, the source log filename will be appended to it.

You can actually rotate any log file you want by specifying three arguments, with the custom source log file path as the first argument.  Example:

```js
logger.rotate( '/path/to/logfile.log', '/logs/pickup/otherapp.log', function(err) {
	if (err) throw err;
} );
```

## Archiving Logs

You can also "archive" logs using the `archive()` method.  Archiving differs from rotation in that the log file is atomically copied to a custom location which may contain date/time directories (all auto-created as needed), and then the file is compressed using gzip.  You can archive any number of logs at once by using [filesystem glob syntax](https://en.wikipedia.org/wiki/Glob_%28programming%29).  Example:

```js
let src_spec = '/logs/myapp/*.log';
let dest_path = '/archives/myapp/[yyyy]/[mm]/[dd]/[filename]-[hh].log.gz';
let epoch = ((new Date()).getTime() / 1000) - 1800; // 30 minutes ago

logger.archive( src_spec, dest_path, epoch, function(err) {
	if (err) throw err;
} );
```

This example would find all the log files found in the `/logs/myapp/` directory that end in `.log`, and archive them to destination directory `/archives/myapp/[yyyy]/[mm]/[dd]/`, with a destination filename pattern of `[filename]-[hh].log.gz`.  All the bracket-delimited placeholders are expanded using the timestamp provided in the `epoch` variable.  The special `[filename]` placeholder expands to the source log filename, sans extension.  All directories are created as needed.

## Sync or Async

By default, the logger will append to your log files asynchronously.  This has the benefit of not blocking your main thread, and can help if your log drive is suffering lag or high I/O wait.  But it *may* cause issues with log entries appearing out of order for extremely high traffic apps, and also some final log entries may be lost if `process.exit()` is called *immediately* after.

To get around these potential issues, you can write log entries synchronously.  Just set the `sync` arg to true:

```js
logger.set( 'sync', true );
logger.debug( 1, "This will be logged synchronously, even if we exit right NOW!" );
process.exit(0);
```

## Buffering

For high traffic applications, calling out to the filesystem to print each log row can become a bottleneck, even in async mode.  To solve this problem, you can enable buffering.  This accumulates N lines (default 100) in RAM before flushing them to disk all at once, using a single filesystem call.  The logger will also automatically flush the buffer at preset intervals (default 100ms), to handle sudden low traffic situations.  The flush operation itself is async (using [fs.appendFile](https://nodejs.org/api/fs.html#filehandleappendfiledata-options)) so it will not block the main thread, but it also ensures only one flush operation happens at a time.

To enable buffering, set the `useBuffer` property in the constructor like this:

```js
let logger = new Logger( log_file, log_columns, {
	useBuffer: true
} );
```

Or you can enable it anytime after construction by calling the `enableBuffer()` method.  Example:

```js
let logger = new Logger( log_file, log_columns );
logger.enableBuffer();
```

You can set the following properties to configure the buffering system (either as constructor args or by calling `set()`):

| Property | Type | Description |
|----------|------|-------------|
| `bufferMaxLines` | Integer | The number of lines to buffer before flushing.  Defaults to `100` (lines). |
| `flushInterval` | Integer | The auto-flush interval in milliseconds.  Defaults to `100` (ms). |
| `flushOnShutdown` | Boolean | Automatically flush on shutdown (see below).  Defaults to `true` (enabled). |

The flush interval requires a timer, and this may keep the Node.js process alive.  We do not use [unref()](https://nodejs.org/en/docs/guides/timers-in-node/#leaving-timeouts-behind) on the timer because too many of these can cause performance issues.  So, our timer must be cleared on shutdown.  The logger can do this automatically if you leave `flushOnShutdown` enabled.  This hooks `SIGTERM`, `SIGINT`, `SIGQUIT` and `uncaughtException`, flushes the buffer and disables further buffering.  It also enables `sync` mode so any last minute log prints will be sync-written.

If you don't want to use `flushOnShutdown` and instead handle things yourself, set it to `false`, then simply call `shutdown()` on the logger instance when you are done using it.  This will flush the buffer and disable further buffering (you can still log of course -- it'll just be immediate).

The final shutdown flush is performed using [fs.appendFileSync](https://nodejs.org/api/fs.html#fsappendfilesyncpath-data-options) so it is guaranteed to be written, even in a crash situation (we use the cooperative [uncatch](https://github.com/jhuckaby/uncatch) module to hook unhandled exceptions).

Note that buffering only affects writing to the log file itself, and not the [echo](#echo-to-console) system.  If you echo log rows to the console, those lines are printed immediately.

## Approximate Time

High traffic applications may also suffer due to the logger fetching the system clock time (i.e. via [Date.now()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/now)) for every log row.  To assist with this, you can enable "approximate" time which only fetches the system clock time once every 50 milliseconds.  For log rows printed in between system clock calls, the time is approximated.

To enable this feature, set the `approximateTime` property to `true` (either as constructor args or by calling `set()`):

```js
let logger = new Logger( log_file, log_columns, {
	approximateTime: true
} );
```

The approximate time feature uses the [approximate-now](https://github.com/gajus/approximate-now) module.  Note that this **does** utilize an `unref()` interval timer, so use with care.

# License

The MIT License

Copyright (c) 2015 - 2021 Joseph Huckaby

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

## File: `logger.js`
```javascript
// Generic Logger Class for Node.JS
// Copyright (c) 2012 - 2021 Joseph Huckaby and PixlCore.com
// Released under the MIT License

const fs = require('fs');
const zlib = require('zlib');
const Path = require('path');
const os = require('os');
const chalk = require('chalk');
const whenever = require('approximate-now');
const Uncatch = require('uncatch');

const Class = require("class-plus");
const Tools = require("pixl-tools");

const async = Tools.async;
const mkdirp = Tools.mkdirp;
const glob = Tools.glob;

module.exports = Class({
	
	__events: true,
	
	columnColors: ['gray', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'],
	dividerColor: 'dim',
	
	internalArgs: ['pather', 'filter', 'serializer', 'echoer', 'useBuffer', 'bufferMaxLines', 'flushInterval', 'flushOnShutdown', 'approximateTime'],
	
	pather: null,
	filter: null,
	serializer: null,
	echoer: null,
	
	useBuffer: false,
	bufferMaxLines: 100,
	flushInterval: 100,
	flushOnShutdown: true,
	approximateTime: false
	
},
class Logger {
	
	constructor(path, columns, args) {
		// create new logger instance
		var self = this;
		
		this.path = path;
		this.columns = columns;
		this.args = args ? Tools.copyHash(args, true) : {};
		
		if (!this.args.debugLevel) this.args.debugLevel = 1;
		if (!this.args.hostname) {
			this.args.hostname = os.hostname().toLowerCase();
		}
		if (!this.args.pid) this.args.pid = process.pid;
		
		// pass hooks in args
		this.internalArgs.forEach( function(key) {
			if (self.args[key]) {
				self[key] = self.args[key];
				delete self.args[key];
			}
		});
		
		// setup buffer system
		if (this.useBuffer) this.enableBuffer();
	}
	
	enableBuffer() {
		// setup flush interval
		this.useBuffer = true;
		this.bufferLines = [];
		this.flushTimer = setInterval( this.flushBuffer.bind(this), this.flushInterval );
		
		if (this.flushOnShutdown) {
			process.on('SIGTERM', this.shutdown.bind(this));
			process.on('SIGINT', this.shutdown.bind(this));
			process.on('SIGQUIT', this.shutdown.bind(this));
			Uncatch.on('uncaughtException', this.shutdown.bind(this));
		}
	}
	
	bufferAppendLine(line) {
		// append line to buffer, flush if full
		this.bufferLines.push(line);
		if (this.bufferLines.length >= this.bufferMaxLines) this.flushBuffer();
	}
	
	flushBuffer() {
		// flush all buffered lines to disk
		// only allow one libuv I/O thread at a time
		// if FS is busy, buffer continues to grow, and will flush on next print or flush interval
		var self = this;
		if (!this.useBuffer || !this.bufferLines.length || this.flushInProgress) return;
		this.flushInProgress = true;
		
		var payload = this.bufferLines.join("");
		this.bufferLines = [];
		
		if (this.args.sync) {
			fs.appendFileSync( this.lastPath, payload );
			this.flushInProgress = false;
			this.emit('bufferFlushed', payload);
		}
		else {
			fs.appendFile( this.lastPath, payload, function() {
				self.flushInProgress = false;
				self.emit('bufferFlushed', payload);
			});
		}
	}
	
	shutdown() {
		// shut down buffer and disable async too (called on shutdown / crash)
		if (!this.useBuffer) return;
		
		if (this.flushTimer) {
			clearInterval( this.flushTimer );
			delete this.flushTimer;
		}
		
		// force shutdown flush in sync mode
		if (this.bufferLines.length) {
			fs.appendFileSync( this.lastPath, this.bufferLines.join("") );
			this.bufferLines = [];
		}
		
		this.useBuffer = false;
		this.args.sync = true;
	}
	
	get(key) {
		// get one arg, or all of them
		return key ? this.args[key] : this.args;
	}
	
	set() {
		// set one or more args, pass in key,value or args obj
		if (arguments.length == 2) {
			if (arguments[0].toString().match(/^(pather|filter|serializer|echoer|useBuffer|bufferMaxLines|flushInterval|flushOnShutdown)$/)) {
				this[arguments[0]] = arguments[1];
			}
			else this.args[ arguments[0] ] = arguments[1];
		}
		else if (arguments.length == 1) {
			for (var key in arguments[0]) this.set(key, arguments[0][key]);
		}
	}
	
	clone(args) {
		// make copy of ourself with optional overrides
		var self = this;
		var clone = new module.exports( this.path, this.columns, this.args );
		
		this.internalArgs.forEach( function(key) {
			if (self[key]) clone[key] = self[key];
		});
		
		if (args) clone.set(args);
		
		return clone;
	}
	
	print(in_args) {
		// setup date/time stuff
		
		// copy args object, never modify user object
		var args = Tools.copyHash(in_args);
		
		var now = 0;
		if (args.now) {
			// now was passed in (expects hires-epoch)
			now = args.now * 1000;
			delete args.now;
		}
		else if (this.approximateTime) {
			// use approximate-time (~50ms precision)
			now = whenever.approximateTime.now;
		}
		else {
			// call system time
			now = Date.now();
		}
		
		var hires_epoch = now / 1000;
		var epoch = Math.floor( hires_epoch );
		
		// only compute local date/time string for unique seconds, for performance
		var date_str = '';
		if (this.lastEpoch && (epoch == this.lastEpoch)) {
			date_str = this.lastDateStr;
		}
		else {
			date_str = Tools.formatDate( epoch, '[yyyy]-[mm]-[dd] [hh]:[mi]:[ss]' );
			this.lastDateStr = date_str;
			this.lastEpoch = epoch;
		}
		
		// import args into object
		for (var key in this.args) {
			if (!(key in args)) args[key] = this.args[key];
		}
		
		// set automatic column values
		args.hires_epoch = hires_epoch;
		args.epoch = epoch;
		args.date = date_str;
		
		// populate columns
		var cols = [];
		for (var idx = 0, len = this.columns.length; idx < len; idx++) {
			var col = this.columns[idx];
			var val = args[col];
			
			if ((typeof(val) == 'undefined') || (val === null) || !val.toString) val = '';
			
			if (this.filter) {
				cols.push( this.filter(val, idx) );
			}
			else {
				if (typeof(val) == 'object') val = JSON.stringify(val);
				cols.push( val.toString().replace(/[\r\n]/g, ' ').replace(/\]\[/g, '') );
			}
		}
		
		// compose log row
		var line = this.serializer ? this.serializer(cols, args) : ('[' + cols.join('][') + "]" + os.EOL);
		if (line === false) return; // do not log anything
		this.lastRow = line;
		
		// file path may have placeholders, expand these if necessary
		var path = this.path;
		if (this.pather) {
			path = this.pather( path, args );
		}
		else if (path.indexOf('[') > -1) {
			path = Tools.substitute( path, args );
		}
		this.lastPath = path;
		
		// append to log
		if (this.useBuffer) this.bufferAppendLine(line);
		else if (args.sync) fs.appendFileSync(path, line);
		else fs.appendFile(path, line, function() {});
		
		// echo to console if desired
		if (args.echo) {
			if (this.echoer) {
				if (typeof(this.echoer) == 'function') {
					this.echoer( line, cols, args );
				}
				else if (typeof(this.echoer) == 'string') {
					if (args.sync) fs.appendFileSync(this.echoer, line);
					else fs.appendFile(this.echoer, line, function() {});
				}
			}
			else if (args.color) {
				// print in color (ignores custom serializer)
				process.stdout.write( this.colorize(cols) + os.EOL );
			}
			else {
				// print plain
				process.stdout.write( line );
			}
		}
		
		// emit row as an event
		this.emit( 'row', line, cols, args );
	}
	
	colorize(cols) {
		// colorize one row (bracket format)
		var ccols = [];
		var nclrs = this.columnColors.length;
		var dclr = chalk[ this.dividerColor ];
		
		for (var idx = 0, len = cols.length; idx < len; idx++) {
			ccols.push( chalk[ this.columnColors[idx % nclrs] ]( cols[idx] ) );
		}
		
		return dclr('[') + ccols.join( dclr('][') ) + dclr(']');
	}
	
	debug(level, msg, data) {
		// simple debug log implementation, expects 'code' and 'msg' named columns in log
		// only logs if level is less than or equal to current debugLevel arg
		if (level <= this.args.debugLevel) {
			this.print({ 
				category: 'debug', 
				code: level, 
				msg: msg, 
				data: data 
			});
		}
	}
	
	error(code, msg, data) {
		// simple error log implementation, expects 'code' and 'msg' named columns in log
		this.print({ 
			category: 'error', 
			code: code, 
			msg: msg, 
			data: data 
		});
	}
	
	transaction(code, msg, data) {
		// simple debug log implementation, expects 'code' and 'msg' named columns in log
		this.print({ 
			category: 'transaction', 
			code: code, 
			msg: msg, 
			data: data 
		});
	}
	
	rotate() {
		// rotate any log file atomically (defaults to our own file)
		// 2 arg convention: dest_path, callback
		// 3 arg convention: log_file, dest_path, callback
		var log_file = '';
		var dest_path = '';
		var callback = null;
		
		if (arguments.length == 3) {
			log_file = arguments[0];
			dest_path = arguments[1];
			callback = arguments[2];
		}
		else if (arguments.length == 2) {
			dest_path = arguments[0];
			callback = arguments[1];
		}
		else throw new Error("Wrong number of arguments to rotate()");
		
		if (!log_file) log_file = this.path;
		if (log_file.indexOf('[') > -1) {
			log_file = Tools.substitute( log_file, this.args );
		}
		
		// if dest path ends with a slash, add src filename + date/time stamp
		if (dest_path.match(/\/$/)) {
			var dargs = Tools.getDateArgs( Tools.timeNow() );
			dest_path += Path.basename(log_file);
			dest_path += '.' + (dargs.yyyy_mm_dd + '-' + dargs.hh_mi_ss).replace(/\W+/g, '-');
			dest_path += '.' + Tools.generateUniqueID(16) + Path.extname(log_file);
		}
		
		// try fs.rename first
		fs.rename(log_file, dest_path, function(err) {
			if (err && (err.code == 'EXDEV')) {
				// dest path crosses fs boundary, gotta rename + copy + rename + delete
				
				// first, perform local rename in source log directory
				var src_temp_file = log_file + '.' + Tools.generateUniqueID(32) + '.tmp';
				fs.rename(log_file, src_temp_file, function(err) {
					if (err) {
						if (callback) callback(err);
						return;
					}
					
					// copy src temp to dest temp file, then rename it
					var dest_temp_file = dest_path + '.' + Tools.generateUniqueID(32) + '.tmp';
					var inp = fs.createReadStream(src_temp_file);
					var outp = fs.createWriteStream(dest_temp_file);
					
					if (callback) inp.on('error', callback );
					if (callback) outp.on('error', callback );
					
					outp.on('finish', function() {
						// final rename
						fs.rename(dest_temp_file, dest_path, function(err) {
							if (err) {
								if (callback) callback(err);
								return;
							}
							
							// all done, delete src temp file
							fs.unlink(src_temp_file, function(err) {
								if (callback) callback(err);
							});
						});
					} );
					
					inp.pipe( outp );
				} ); // src rename
			} // EXDEV
			else {
				// rename worked, or other error
				if (callback) callback(err);
			}
		} ); // fs.rename
	}
	
	archive(src_spec, dest_path, epoch, callback) {
		// archive one or more log files, can use glob spec (defaults to our file).
		// dest path may use placeholders: [yyyy], [mm], [dd], [hh], [filename], [hostname], etc.
		// creates dest dirs as needed.
		// if dest path ends in .gz, archives will be compressed.
		var self = this;
		if (!src_spec) src_spec = this.path;
		if (!callback) callback = function() {};
		
		// fill date/time placeholders
		var dargs = Tools.getDateArgs( epoch );
		for (var key in dargs) self.args[key] = dargs[key];
		
		glob(src_spec, {}, function (err, files) {
			// got files
			if (err) return callback(err);
			
			if (files && files.length) {
				async.eachSeries( files, function(src_file, callback) {
					// foreach file
					
					// add filename to args
					self.args.filename = Path.basename(src_file).replace(/\.\w+$/, '');
					
					// construct final path
					var dest_file = Tools.substitute( dest_path, self.args );
					
					// rename local log first
					var src_temp_file = src_file + '.' + Tools.generateUniqueID(32) + '.tmp';
					
					fs.rename(src_file, src_temp_file, function(err) {
						if (err) {
							return callback( new Error("Failed to rename: " + src_file + " to: " + src_temp_file + ": " + err) );
						}
						
						// create dest dirs as necessary
						mkdirp(Path.dirname(dest_file), function (err) {
							if (err) {
								return callback( new Error("Failed to make directories for: " + dest_file + ": " + err) );
							}
							
							if (dest_file.match(/\.gz$/i)) {
								// gzip the log archive
								var gzip = zlib.createGzip();
								var inp = fs.createReadStream( src_temp_file );
								var outp = fs.createWriteStream( dest_file, {flags: 'a'} );
								
								inp.on('error', callback);
								outp.on('error', callback);
								
								outp.on('finish', function() {
									// all done, delete temp file
									fs.unlink( src_temp_file, callback );
								} );
								
								inp.pipe(gzip).pipe(outp);
							} // gzip
							else {
								// straight copy (no compress)
								var inp = fs.createReadStream( src_temp_file );
								var outp = fs.createWriteStream( dest_file, {flags: 'a'} );
								
								inp.on('error', callback);
								outp.on('error', callback);
								
								outp.on('finish', function() {
									// all done, delete temp file
									fs.unlink( src_temp_file, callback );
								} );
								
								inp.pipe( outp );
							} // copy
						} ); // mkdirp
					} ); // fs.rename
				}, callback ); // eachSeries
			} // got files
			else {
				callback( err || new Error("No files found matching: " + src_spec) );
			}
		} ); // glob
	}
	
	shouldLog(level) {
		// // check if we're logging at or above the requested level
		return( this.get('debugLevel') >= level );
	}

});
```

## File: `package.json`
```json
{
  "name": "pixl-logger",
  "version": "2.0.4",
  "description": "A simple logging class which generates [bracket][delimited] log columns.",
  "author": "Joseph Huckaby <jhuckaby@gmail.com>",
  "homepage": "https://github.com/jhuckaby/pixl-logger",
  "license": "MIT",
  "main": "logger.js",
  "scripts": {
	  "test": "pixl-unit test.js"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/jhuckaby/pixl-logger"
  },
  "bugs": {
    "url": "https://github.com/jhuckaby/pixl-logger/issues"
  },
  "keywords": [
    "logging",
    "clear"
  ],
  "dependencies": {
    "chalk": "2.4.1",
    "class-plus": "^1.0.0",
	"pixl-tools": "^2.0.2",
	"uncatch": "^1.0.0",
	"approximate-now": "1.0.0"
  },
  "devDependencies": {
	  "pixl-unit": "^1.0.0"
  }
}
```

## File: `test.js`
```javascript
// Unit tests for pixl-logger
// Copyright (c) 2021 Joseph Huckaby
// Released under the MIT License

var os = require('os');
var fs = require('fs');
var Path = require('path');
var Tools = require('pixl-tools');
var Logger = require('./logger.js');

process.chdir( __dirname );

var log_file = Path.join( os.tmpdir(), 'pixl-logger-unit-tests.log' );
var log_columns = ['hires_epoch', 'date', 'hostname', 'pid', 'component', 'category', 'code', 'msg', 'data'];

if (fs.existsSync(log_file)) fs.unlinkSync(log_file);

// Unit Tests

module.exports = {
	setUp: function (callback) {
		callback();
	},
	
	beforeEach: function(test) {
		
	},
	
	afterEach: function(test) {
		
	},
	
	onAssertFailure: function(test, msg, data) {
		
	},
	
	tests: [
		
		function testBasicSync(test) {
			var logger = new Logger( log_file, log_columns, { 
				sync: true 
			} );
			
			logger.once('row', function(line, cols, args) {
				test.ok( "Row event fired");
				test.debug( line );
			});
			
			logger.print({
				category: 'debug',
				component: 'main',
				code: 1,
				msg: "Hello log!",
				data: { foo: "bar" }
			});
			
			var payload = fs.readFileSync(log_file, 'utf8');
			
			test.ok( payload.match(/\[main\]\[debug\]\[1\]\[Hello log\!\]\[\{\"foo\"\:\"bar\"\}\]/), "Basic log content not found in file." );
			test.done();
		},
		
		function testBasicAsync(test) {
			var logger = new Logger( log_file, log_columns, {
				sync: false
			} );
			
			logger.print({
				category: 'debug',
				component: 'main',
				code: 1,
				msg: "This was async!"
			});
			
			setTimeout( function() {
				test.ok( fs.readFileSync(log_file, 'utf8').match(/This was async/), "Async log content not found in file." );
				test.done();
			}, 50 );
		},
		
		function testApproxTime(test) {
			if (fs.existsSync(log_file)) fs.unlinkSync(log_file);
			
			var logger = new Logger( log_file, log_columns, {
				sync: false,
				approximateTime: true
			} );
			
			var epochs = [];
			
			logger.on('row', function(line, cols, args) {
				epochs.push( cols[0] );
			});
			
			for (var idx = 0; idx < 10; idx++) {
				logger.print({ category: 'debug', component: 'main', code: 1, msg: "Test" });
			}
			
			test.ok( epochs.length == 10, "Wrong number of rows logged: " + epochs.length );
			
			for (var idx = 1; idx < 10; idx++) {
				test.ok( epochs[idx] > epochs[idx - 1], "Epoch did not increment on sequential print calls." );
			}
			
			test.done();
		},
		
		function testBuffer(test) {
			if (fs.existsSync(log_file)) fs.unlinkSync(log_file);
			
			var logger = new Logger( log_file, log_columns, {
				sync: false,
				useBuffer: true,
				bufferMaxLines: 10,
				flushInterval: 100,
				flushOnShutdown: false
			} );
			
			logger.once('bufferFlushed', function() {
				var lines = fs.readFileSync(log_file, 'utf8').trim().split(/\n/);
				test.ok( lines.length == 10, "Wrong number of lines logged in buffer flush.");
				
				logger.shutdown();
				test.ok( logger.useBuffer === false, "Buffer was not disabled on shutdown.");
				test.ok( logger.args.sync === true, "Sync was not enabled on shutdown.");
				
				test.done();
			});
			
			for (var idx = 0; idx < 10; idx++) {
				logger.print({ category: 'debug', component: 'main', code: 1, msg: "TestBuffer" });
			}
		},
		
		function testBufferIntervalFlush(test) {
			if (fs.existsSync(log_file)) fs.unlinkSync(log_file);
			
			var logger = new Logger( log_file, log_columns, {
				sync: false,
				useBuffer: true,
				bufferMaxLines: 10,
				flushInterval: 100,
				flushOnShutdown: false
			} );
			
			logger.once('bufferFlushed', function() {
				var lines = fs.readFileSync(log_file, 'utf8').trim().split(/\n/);
				test.ok( lines.length == 9, "Wrong number of lines logged in buffer flush.");
				logger.shutdown();
				test.done();
			});
			
			for (var idx = 0; idx < 9; idx++) {
				logger.print({ category: 'debug', component: 'main', code: 1, msg: "TestBuffer" });
			}
		}
		
	],
	
	tearDown: function (callback) {
		// clean up
		if (fs.existsSync(log_file)) fs.unlinkSync(log_file);
		callback();
	}
};
```


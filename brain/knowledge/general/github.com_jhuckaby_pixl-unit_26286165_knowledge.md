---
id: github.com-jhuckaby-pixl-unit-26286165-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:15.525033
---

# KNOWLEDGE EXTRACT: github.com_jhuckaby_pixl-unit_26286165
> **Extracted on:** 2026-04-01 14:00:29
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007523603/github.com_jhuckaby_pixl-unit_26286165

---

## File: `.npmignore`
```
.gitignore
node_modules/
```

## File: `README.md`
```markdown
# Overview

This module is a very simple unit test runner.

# Usage

Use [npm](https://www.npmjs.com/) to install the module as a command-line executable:

```
sudo npm install -g pixl-unit
```

Then call it using `pixl-unit` and specify a path to your unit test file or directory:

```
pixl-unit /path/to/your/unit/tests.js
```

You may specify multiple files and/or directories, separated by spaces.  If you specify directories, the script will scan the contents and execute all JS files within (one level deep only).

```
pixl-unit /path/to/your/unit/test/dir/
```

## Command-Line Arguments

Specify command-line arguments using the format `--key value` and do this *after* any and all unit test files / directories.  The following command-line switches are supported:

| Argument | Default Value | Description |
| -------- | ------------- | ----------- |
| `threads` | 1 | The total number of threads to use when executing tests.  See warning below. | 
| `verbose` | 0 | Set this to `1` to enable verbose output to the console. | 
| `quiet` | 0 | Set this to `1` to suppress all output to the console. | 
| `color` | 1 | Enables or disables color output using the chalk module. | 
| `fatal` | 0 | Set this to `1` to exit immediately after the first assertion failure (includes stack trace). | 
| `output` | "" | Set this to a file path to emit a JSON report (works with quiet mode). | 
| `delay` | 0 | Insert a delay between each test by setting this to the desired number of seconds. |
| `times` | 1 | Run the tests a specified number of times. |

Here is an example, which runs all the tests in `tests.js`, enables quiet mode, and generates a JSON report file:

```
pixl-unit /path/to/tests.js --quiet --output /var/tmp/unit-results.json
```

Please be careful when increasing the `--threads` setting, beyond the default value of `1`.  This will cause multiple tests to run simultaneously.  If any of your tests rely on previous tests completing, this will not go well.

## Use in Modules

To use `pixl-unit` in your own npm module, first declare it in your `package.json` in the `devDependencies` section:

```javascript
"devDependencies": {
	"pixl-unit": "*"
}
```

Then add a test script command to your `scripts` section:

```javascript
"scripts": {
	"test": "pixl-unit test/*.js"
}
```

This example assumes you have a `test/` directory in your module containing one or more JS files containing unit tests compatible with `pixl-unit`.

Then you can simply type `npm test` to run your module's unit tests.

## Sample Output

`pixl-unit` outputs to the console by default, using the [chalk](https://www.npmjs.com/package/chalk) module for ANSI color.  Stats are summarized at the bottom.  You can also suppress this output and/or generate a JSON report file (see below).

```
Simple Unit Test Runner v1.0
Sat Mar 07 2015 12:50:11 GMT-0800 (PST)

Args: {"threads":1,"verbose":0,"quiet":0,"color":1,"fatal":0,"output":""}
Suites: ["/Users/jhuckaby/node_modules/pixl-unit/test.js"]

Suite: /Users/jhuckaby/node_modules/pixl-unit/test.js

✓ OK - All tests passed

Tests passed: 3 of 3 (100%)
Tests failed: 0 of 3 (0%)
Assertions:   5
Test Suites:  1
Time Elapsed: 0 seconds
```

Assertion failures are highlighted in bold + red, and include the test name, assertion failure message, and any additional data if provided.  Example:

```
Suite: /Users/jhuckaby/node_modules/pixl-unit/test.js

Assert Failed: /Users/jhuckaby/node_modules/pixl-unit/test.js: testExpect: Assertion 2 of 3
Data: {"additional_data":12345}       
X testExpect                          
                                       
X - Errors occurred

Tests passed: 2 of 3 (66%)
Tests failed: 1 of 3 (33%)
Assertions:   5
Test Suites:  1
Time Elapsed: 0.11 seconds
```

You can also get a full stack trace by enabling verbose mode (`--verbose`) or fatal mode, which also exits at the first failure (`--fatal`).  This will give you the exact line number where the assertion failed.

Here is example JSON report (activate by including `--output MYREPORT.json` on the CLI):

```javascript
{
    "args": {
        "color": 1,
        "fatal": 0,
        "output": "/var/tmp/joe.json",
        "quiet": true,
        "threads": 1,
        "verbose": 0
    },
    "asserts": 5,
    "elapsed": 0.108,
    "failed": 0,
    "files": [
        "/Users/jhuckaby/node_modules/pixl-unit/test.js"
    ],
    "passed": 3,
    "suites": 1,
    "tests": 3,
    "time_end": 1425762119.48,
    "time_start": 1425762119.372,
    "errors": []
}
```

## Test Modules

Your test modules should be simple JS files containing tests, and optionally setup and teardown functions (described below).  Feel free to require any other modules you need at the top of your JS file.

You declare unit tests in your modules by exporting a `tests` array of functions.  The functions are executed in order from top to bottom, and support async tests by using a promise object.

```javascript
exports.tests = [
	// function test1...
	// function test2...
];
```

Each test function should have a name, and accept a single argument which works sort of like a promise:

```javascript
function testTrue(test) {
	test.ok(true == true, 'Testing for true');
	test.done();
}
```

The `test` object has an assertion method called `ok()` (`assert()` is also acceptable).  This expects a boolean `true` for success, `false` for failure, and optionally accepts a message to be displayed upon failure.

Calling `test.done()` indicates that all the asserts have been called, and the test is complete.  This is useful because tests may be asynchronous, and finish in another thread.  Example:

```javascript
function testTimeout(test) {
	setTimeout( function() {
		test.ok(true == true, 'Testing 100ms later');
		test.done();
	}, 100 );
}
```

If you know exactly how many asserts will be called for a given test, you can call `expect()` at the beginning of the test, which sets an expectation for the assertion count.  If you then call `done()` without completing the asserts (or called too many) an error is raised.  Example use:

```javascript
function testExpect(test) {
	// test the expect feature
	test.expect(3);
	test.ok( true, "Assertion 1 of 3" );
	test.ok( true, "Assertion 2 of 3" );
	test.ok( true, "Assertion 3 of 3" );
	test.done();
}
```

You can also provide true async functions which are handled properly.  You do not need to call `test.done()` in these cases (it's a no-op).  Example:

```js
async function testAsync(test) {
	// true async function
	// test harness will wait for promise to resolve
	// no need to call test.done()
	await sleep(100);
}
```

Feel free to use Node's built-in `assert` library for async tests, as exceptions will be caught correctly:

```js
async function testMath(test) {
	assert.strictEqual(1, 0); // will fail
}
```

However, note that pixl-unit's own "assertion counter" stat (`asserts`) doesn't increment for these calls.

## setUp and tearDown

You can optionally export `setUp()` and/or `tearDown()` functions from your module, which are called when the test is starting up, and shutting down, respectively.  These functions are passed a single callback which must be invoked to indicate that have finished their operations.

```javascript
exports.setUp = function(callback) {
	// do some setup here
	callback();
};

exports.tearDown = function(callback) {
	// do some shutdown stuff here
	callback();
};
```

## beforeEach and afterEach

You can optionally export `beforeEach()` and/or `afterEach()` functions from your module, which are called when each test is about to start, and after it completes, respectively.  These functions are passed the test object as a single argument, and there is no callback.

```javascript
exports.beforeEach = function(test) {
	// test is about to start
	console.log("Starting test: " + test.name);
};

exports.afterEach = function(test) {
	// test has just completed
	console.log("Completed test: " + test.name);
	console.log("Failed asserts: " + test.failed);
};
```

## timeout

You can optionally set a maximum elapsed time for a test.  If this time limit is exceeded, an assertion is force-failed on the test.  To do this, call `timeout()` at the start of your test, and specify the timeout value in milliseconds.  Example use:

```js
function testTimeout(test) {
	test.timeout( 200 ); // 200ms max time
	
	setTimeout( function() {
		test.ok(true == true, 'Testing 100ms later');
		test.done();
	}, 100 );
}
```

## Debug Logging

There are two ways to include additional debugging data with your unit test output.  First, you can include a 3rd argument to `ok()` or `assert()` which will be logged *only if the assertion fails*.  It can be any JavaScript primitive type (string, number, etc.) or an object, and will be JSON serialized and emitted in gray (if color is enabled).  Example:

```javascript
function testSomething(test) {
	test.ok(true == false, 'Testing for true', { additional: "data" } );
	test.done();
}
```

In this case, when the assertion fails, the console output will include:

```
Assert Failed: test.js: testSomething: Testing for true
Data: {"additional":"data"}
```

The other thing you can do is call `test.debug()` at any time, and pass in a debug message and an optional data object.  This will *only* emit if pixl-unit is running in verbose mode (i.e. via the `--verbose` command-line switch).  Otherwise it will be suppressed.  Example:

```js
test.debug( "This will only be printed in verbose mode", { additional: "data" } );
```

# License

The MIT License

Copyright (c) 2015 - 2026 Joseph Huckaby.

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

## File: `package.json`
```json
{
  "name": "pixl-unit",
  "version": "2.0.1",
  "description": "A very simple unit test runner for Node.js.",
  "author": "Joseph Huckaby <jhuckaby@gmail.com>",
  "homepage": "https://github.com/jhuckaby/pixl-unit",
  "license": "MIT",
  "main": "unit.js",
  "bin": "unit.js",
  "scripts": {
    "test": "pixl-unit test.js"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/jhuckaby/pixl-unit"
  },
  "bugs": {
    "url": "https://github.com/jhuckaby/pixl-unit/issues"
  },
  "keywords": [
    "unit",
    "test"
  ],
  "dependencies": {
    "async": "2.6.4",
    "chalk": "2.4.1",
    "pixl-args": "^1.0.0",
    "pixl-tools": "^2.0.2",
    "pixl-cli": "^1.0.0"
  },
  "devDependencies": {}
}
```

## File: `test.js`
```javascript
// Sample unit tests for pixl-unit
// Copyright (c) 2015 Joseph Huckaby
// Released under the MIT License

const assert = require('node:assert/strict');

function sleep(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
};

module.exports = {
	setUp: function (callback) {
		// always called before tests start
		callback();
	},
	
	tests: [
		
		function testTrue(test) {
			test.ok(true == true, 'Testing for true');
			test.done();
		},
		
		function testTimeout(test) {
			setTimeout( function() {
				test.ok(true == true, 'Testing 100ms later');
				test.done();
			}, 100 );
		},
		
		function testTimeout(test) {
			test.timeout( 200 ); // 200ms max time
			
			setTimeout( function() {
				test.ok(true == true, 'Testing 100ms later');
				test.done();
			}, 100 );
		},
		
		function testExpect(test) {
			// test the expect feature
			test.expect(3);
			test.ok( true, "Assertion 1 of 3" );
			test.ok( true, "Assertion 2 of 3", { additional_data: 12345 } );
			test.ok( true, "Assertion 3 of 3" );
			test.done();
		},
		
		async function testAsync(test) {
			// true async function
			// pixl-unit will wait for promise to resolve
			// no need to call test.done(), and we can also use node's assert here
			await sleep(100);
			assert.strictEqual(1, 1);
		}
		
	], // tests array
	
	tearDown: function (callback) {
		// always called right before shutdown
		callback();
	}
};
```

## File: `unit.js`
```javascript
#!/usr/bin/env node

// Simple Unit Test Runner
// Copyright (c) 2015 - 2018 Joseph Huckaby
// Released under the MIT License

var fs = require("fs");
var path = require("path");
var util = require("util");

var async = require("async");
var chalk = require("chalk");
var Args = require("pixl-args");
var Tools = require("pixl-tools");
var cli = require('pixl-cli');
var pkg = require('./package.json');

// shift files off beginning of arg array
var argv = JSON.parse( JSON.stringify(process.argv.slice(2)) );
var paths = [];
while (argv.length && !argv[0].match(/^\-/)) {
	paths.push( path.resolve( argv.shift() ) );
}

// now parse rest of cmdline args, if any
var args = new Args( argv, {
	threads: 1,
	verbose: 0,
	quiet: 0,
	color: 1,
	fatal: 0,
	output: ''
} );
args = args.get(); // simple hash

// color support?
if (!args.color) chalk.enabled = false;

// resolve dirs to files
var files = [];
for (var idx = 0, len = paths.length; idx < len; idx++) {
	var p = paths[idx].replace(/\/$/, '');
	var stats = fs.statSync( p );
	if (stats.isFile()) files.push( p );
	else if (stats.isDirectory()) {
		var filenames = fs.readdirSync( p );
		for (var idy = 0, ley = filenames.length; idy < ley; idy++) {
			var filename = filenames[idy];
			if (filename.match(/\.js$/i)) files.push( p + '/' + filename );
		}
	} // dir
} // foreach path

// setup progress bar
var progress = {
	active: false,
	
	start: function() {
		if (args.verbose) return;
		cli.progress.start();
		this.active = true;
	},
	update: function(amount) {
		if (!this.active || args.verbose) return;
		cli.progress.update( amount );
	},
	hide: function() {
		if (!this.active || args.verbose) return;
		cli.progress.erase();
	},
	show: function() {
		if (!this.active || args.verbose) return;
		cli.progress.draw();
	},
	end: function() {
		if (!this.active || args.verbose) return;
		cli.progress.end();
		this.active = false;
	}
};

var print = function(msg) {
	// print message to console
	if (!args.quiet) {
		progress.hide();
		process.stdout.write(msg);
		progress.show();
	}
};
var verbose = function(msg) {
	// print only in verbose mode
	if (args.verbose) print(msg);
};
var pct = function(amount, total) {
	// printable percent number
	if (!amount) amount = 0;
	if (!total) total = 1;
	return '' + Math.floor( (amount / total) * 100 ) + '%';
};

print("\n" + chalk.bold.magenta("Simple Unit Test Runner v" + pkg.version) + "\n");
print( chalk.gray((new Date()).toLocaleString()) + "\n" );

print("\n" + chalk.gray("Args: " + JSON.stringify(args)) + "\n");
print( chalk.gray("Suites: " + JSON.stringify(files)) + "\n");

var stats = {
	tests: 0,
	asserts: 0,
	passed: 0,
	failed: 0,
	errors: [],
	time_start: Tools.timeNow()
};

// iterate over files
async.eachSeries( files, 
	function(file, callback) {
		// run each suite
		print("\n" + chalk.bold.yellow("Suite: " + file) + "\n");
		
		// load js file and grab tests
		var suite = require( path.resolve(file) );
		suite.args = args;
		suite.stats = stats;
		
		// stub out setUp and tearDown if not defined
		if (!suite.setUp) suite.setUp = function(callback) { callback(); };
		if (!suite.tearDown) suite.tearDown = function(callback) { callback(); };
		
		// setUp
		suite.setUp( function() {
			
			// start progress tracking
			progress.start({
				catchInt: true,
				catchTerm: true,
				catchCrash: true,
				exitOnSig: true
			});
			
			// execute tests N times (usually 1)
			async.timesSeries( args.times || 1, function(tidx, callback) {
				async.eachLimit( suite.tests, args.threads, 
					function(test_func, callback) {
						// execute single test
						stats.tests++;
						var test_name = test_func.testName || test_func.name || ("UnnamedTest" + stats.tests);
						
						var test = {
							file: file,
							name: test_name,
							expected: 0,
							asserted: 0,
							passed: 0,
							failed: 0,
							completed: false,
							
							expect: function(num) {
								this.expected = num;
							},
							assert: function(fact, msg, data) {
								this.asserted++;
								if (fact) {
									this.passed++;
									verbose('.');
								}
								else {
									this.failed++;
									verbose("F\n");
									if (!msg) msg = "(No message)";
									print( "\n" + chalk.bold.red("Assert Failed: " + file + ": " + test_name + ": " + msg) + "\n" );
									if (typeof(data) != 'undefined') {
										print( chalk.gray( chalk.bold("Data: ") + JSON.stringify(data)) + "\n" );
									}
									stats.errors.push( "Assert Failed: " + file + ": " + test_name + ": " + msg );
									if (args.verbose || args.fatal) {
										print( "\n" + (new Error("Stack Trace:")).stack + "\n\n" );
									}
									if (suite.onAssertFailure) {
										suite.onAssertFailure( test, msg, data );
									}
									if (args.fatal) {
										progress.end();
										if (args.die) process.exit(1); // die without tearDown
										suite.tearDown( function() { process.exit(1); } );
									}
								}
							},
							done: function() {
								if (this.timer) clearTimeout( this.timer );
								if (this.completed) {
									var msg = "Error: test.done() called twice: " + file + ": " + test_name;
									print( chalk.bold.red(msg) + "\n" );
									stats.errors.push( msg );
									if (args.fatal) {
										progress.end();
										if (args.die) process.exit(1); // die without tearDown
										suite.tearDown( function() { process.exit(1); } );
										return;
									}
								}
								this.completed = true;
								
								progress.update( stats.tests / (suite.tests.length * (args.times || 1)) );
								stats.asserts += this.asserted;
								
								if (this.expected && (this.asserted != this.expected)) {
									// wrong number of assertions
									this.failed++;
									verbose("F\n");
									var msg = "Error: Wrong number of assertions: " + file + ": " + test_name + ": " + 
										"Expected " + this.expected + ", Got " + this.asserted + ".";
									print( chalk.bold.red(msg) + "\n" );
									stats.errors.push( msg );
									if (args.fatal) {
										progress.end();
										if (args.die) process.exit(1); // die without tearDown
										suite.tearDown( function() { process.exit(1); } );
										return;
									}
								}
								if (!this.failed) {
									// test passed
									stats.passed++;
									verbose( chalk.bold.green("✓ " + test_name) + "\n" );
								}
								else {
									// test failed
									stats.failed++;
									print( chalk.bold.red("X " + test_name) + "\n" );
								}
								
								if (suite.afterEach) suite.afterEach(this);
								// callback();
								process.nextTick( callback );
							}, // done
							verbose: function(msg, data) {
								// log verbose message and data
								verbose( chalk.bold.gray(msg) + "\n" );
								if (typeof(data) != 'undefined') {
									verbose( chalk.gray(JSON.stringify(data)) + "\n" );
								}
							},
							fatal: function(msg, data) {
								// force a fatal error and immediate shutdown
								args.fatal = true;
								args.verbose = true;
								this.verbose( msg, data );
								this.assert( false, msg );
							},
							timeout: function(msec) {
								// set a timeout for the test to complete
								var self = this;
								this.timer = setTimeout( function() {
									delete self.timer;
									self.ok( false, "Error: Maximum time exceeded for test (" + msec + " ms)" );
									self.done();
								}, msec );
							}
						}; // test object
						
						// convenience, to better simulate nodeunit and others
						test.ok = test.assert;
						test.debug = test.verbose;
						
						// invoke test
						var runTest = function() {
							verbose("Running test: " + test.name + "...\n");
							if (suite.beforeEach) suite.beforeEach(test);
							
							var result;
							try { 
								result = test_func.apply( suite, [test] ); 
							}
							catch (err) {
								// sync throw
								test.assert(false, err && err.message ? err.message : String(err), {
									stack: err && err.stack
								});
								return test.done();
							}
							
							// sniff out a promise and handle separately
							if (result && (typeof(result.then) === 'function')) {
								var orig_done = test.done;
								test.done = function() {}; // no-op in case user does both
								
								result.then(
									function() {
										// promise resolved happily
										orig_done.call(test);
									},
									function(err) {
										// async throw
										test.assert(false, err && err.message ? err.message : String(err), {
											stack: err && err.stack
										});
										orig_done.call(test);
									}
								);
							} // promise
						};
						
						if (args.delay) {
							setTimeout( runTest, parseFloat(args.delay) * 1000 );
						}
						else runTest();
					},
					function(err) {
						// all tests complete in suite
						// if user code reset args.times and we're in a non-zero iteration, abort timesSeries
						if ((tidx > 0) && !args.times) callback("ABORT");
						else callback();
					} // all tests complete
				); // each test
			},
			function() {
				// end of timesSeries
				progress.end();
				
				suite.tearDown( function() {
					callback();
				} ); // tearDown
			} ); // async.timesSeries
			
		} ); // setUp
	},
	function(err) {
		// all suites complete
		stats.time_end = Tools.timeNow();
		stats.elapsed = stats.time_end - stats.time_start;
		stats.suites = files.length;
		stats.files = files;
		stats.args = args;
		
		print("\n");
		
		if (!stats.failed) {
			// all tests passed
			print( chalk.bold.green("✓ OK - All tests passed") + "\n" );
		}
		else {
			print( chalk.bold.red("X - Errors occurred") + "\n" );
			process.exitCode = 1;
		}
		
		// more stats
		var pass_color = stats.failed ? chalk.bold.yellow : chalk.bold.green;
		var fail_color = stats.failed ? chalk.bold.red : chalk.bold.gray;
		
		print("\n");
		print( pass_color("Tests passed: " + Tools.commify(stats.passed) + " of " + Tools.commify(stats.tests) + " (" + pct(stats.passed, stats.tests) + ")") + "\n" );
		print( fail_color("Tests failed: " + Tools.commify(stats.failed) + " of " + Tools.commify(stats.tests) + " (" + pct(stats.failed, stats.tests) + ")") + "\n" );
		print( chalk.gray("Assertions:   " + Tools.commify(stats.asserts)) + "\n" );
		print( chalk.gray("Test Suites:  " + Tools.commify(stats.suites)) + "\n" );
		if (args.times && (args.times > 1)) print( chalk.gray("Iterations:  " + Tools.commify(args.times)) + "\n" );
		
		if (stats.elapsed >= 61.0) {
			// 1 minute 1 second
			print( chalk.gray("Time Elapsed: " + Tools.getTextFromSeconds(stats.elapsed)) + "\n" );
		}
		else {
			// 60.999 seconds
			print( chalk.gray("Time Elapsed: " + Tools.shortFloat(stats.elapsed) + " seconds") + "\n" );
		}
		
		print("\n");
		
		// json file output
		if (args.output) {
			fs.writeFileSync( args.output, JSON.stringify(stats) );
		}
	}
);
```


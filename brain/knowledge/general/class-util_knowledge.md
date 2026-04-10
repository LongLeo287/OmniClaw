# Knowledge Dump for class-util

## File: index.js
```
// Simple class helper utilities
// Copyright (c) 2024 Joseph Huckaby
// Released under the MIT License

class HookHelper {
	
	registerHook(name, handler) {
		// register a hook, called by plugins
		// hooks are different than event listeners, as they are called in async sequence
		if (!this.hooks) this.hooks = {};
		if (!this.hooks[name]) this.hooks[name] = [];
		this.hooks[name].push( handler );
	}
	
	removeHook(name, handler) {
		// remove single hook listener or all of them
		if (!this.hooks) this.hooks = {};
		if (handler) {
			if (this.hooks[name]) {
				let idx = this.hooks[name].indexOf(handler);
				if (idx > -1) this.hooks[name].splice( idx, 1 );
				if (!this.hooks[name].length) delete this.hooks[name];
			}
		}
		else delete this.hooks[name];
	}
	
	fireHook(name, thingy, callback) {
		// fire all listeners for a given hook
		// calls both sync and async listeners
		let self = this;
		if (!this.hooks) this.hooks = {};
		
		// now do the normal async dance
		if (!this.hooks[name] || !this.hooks[name].length) {
			process.nextTick( callback );
			return;
		}
		
		// fire hooks in async series
		let idx = 0;
		let iterator = function() {
			let handler = self.hooks[name][idx++];
			if (!handler) return callback();
			
			if (handler.constructor.name === "AsyncFunction") {
				// async style
				handler.call( self, thingy ).then( iterator, callback );
			}
			else {
				// callback-style
				let nextThread = 0;
				handler.call( self, thingy, function(err) {
					if (err) return callback(err);
					
					// ensure async, to prevent call stack overflow
					if (nextThread) iterator();
					else process.nextTick( iterator );
				} );
				nextThread++;
			}
		};
		iterator();
	}
	
} // HookHelper

const asyncifyMethod = function(origFunc, argNames) {
	// asyncify a single class method
	// resolution will be array of callback arguments (err, results, etc.)
	// also supports classic callback calling convention
	return async function(...args) {
		let self = this;
		
		// sniff for classic callback style
		if (typeof(args[ args.length - 1 ]) == 'function') return origFunc.call(self, ...args);
		
		// promise/async style
		return new Promise( (resolve, reject) => {
			origFunc.call(self, ...args, function(...results) {
				let err = results.shift();
				if (err) reject(err);
				else if (argNames) {
					let resultsObj = {};
					argNames.forEach( function(name, idx) {
						resultsObj[name] = results[idx];
					} );
					resolve( resultsObj );
				}
				else resolve( (results.length > 1) ? results : results[0] );
			});
		});
	};
}; // asyncifyMethod

/** 
 * Helper functions for classes.
 * @module ClassUtil
 */
const ClassUtil = module.exports = {
	
	/** 
	 * Convert one or more callback-style functions to async.
	 * @param {Function} obj - The class to convert functions in.
	 * @param {(Object|RegExp)} methods - The set of modules to convert.
	 */
	asyncify(obj, methods) {
		// asyncify one or more methods in class
		let proto = obj.prototype;
		if (typeof(methods) == 'string') methods = [ methods ];
		
		if (Array.isArray(methods)) {
			// specific set of methods to asyncify
			methods.forEach( function(key) {
				if (proto[key] && !proto[key].__async && (proto[key].constructor.name !== "AsyncFunction")) {
					proto[key] = asyncifyMethod( proto[key] );
					proto[key].__async = true;
				}
			} );
		}
		else if (methods instanceof RegExp) {
			// regular expression to match against method names
			Object.getOwnPropertyNames(proto).forEach( function(key) { 
				if (!key.match(/^(__name|constructor|prototype)$/) && (typeof(proto[key]) == 'function') && key.match(methods) && !proto[key].__async && (proto[key].constructor.name !== "AsyncFunction")) { 
					proto[key] = asyncifyMethod( proto[key] ); 
					proto[key].__async = true;
				} 
			}); 
		}
		else {
			// hash to define callback arg names for each async func
			for (let key in methods) {
				if (proto[key] && !proto[key].__async && (proto[key].constructor.name !== "AsyncFunction")) {
					proto[key] = asyncifyMethod( proto[key], methods[key] );
					proto[key].__async = true;
				}
			}
		}
	},
	
	/** 
	 * Mixin one or more classes into a target class.
	 * @param {Function} obj - The target class to mix mixins into.
	 * @param {Object} mixers - The array of classes to mixin.
	 * @param {boolean} [force=false] - Overwrite existing methods and static properties.
	 */
	mixin(obj, mixers, force) {
		// mix-in an external class
		let proto = obj.prototype;
		if (!Array.isArray(mixers)) mixers = [ mixers ];
		
		for (let idx = 0, len = mixers.length; idx < len; idx++) {
			let class_obj = mixers[idx];
			let class_proto = class_obj.prototype;
			if (!class_proto) throw new Error("All mixins must be classes.");
			let class_inst = new class_obj();
			
			// prototype methods
			Object.getOwnPropertyNames(class_proto).forEach( function(key) {
				if (!key.match(/^(__name|constructor|prototype)$/) && (!(key in proto) || force)) {
					proto[key] = class_proto[key];
				}
			});
			
			// public class fields
			Object.getOwnPropertyNames(class_inst).forEach( function(key) {
				if (!key.match(/^(__name|constructor|prototype)$/) && (!(key in proto) || force)) {
					proto[key] = class_inst[key];
				}
			});
			
			// static members
			Object.getOwnPropertyNames(class_obj).forEach( function(key) {
				if (!key.match(/^(name|length|prototype)$/) && (!(key in obj) || force)) {
					obj[key] = class_obj[key];
				}
			});
		} // foreach mixin
	},
	
	/** 
	 * Add event listener and emitter support to a class.
	 * @param {Function} obj - The target class to add event support into.
	 */
	eventify(obj) {
		ClassUtil.mixin(obj, require("events").EventEmitter);
	},
	
	/** 
	 * Add hook support to a class.
	 * @param {Function} obj - The target class to add hook support into.
	 */
	hookify(obj) {
		ClassUtil.mixin(obj, HookHelper);
	}
	
}; // ClassUtil

// asyncify fireHook
ClassUtil.asyncify( HookHelper, ['fireHook'] );

```

## File: package.json
```
{
  "name": "pixl-class-util",
  "version": "1.0.1",
  "description": "Helper functions for extending classes with mixins and more.",
  "author": "Joseph Huckaby <jhuckaby@gmail.com>",
  "homepage": "https://github.com/pixlcore/class-util",
  "license": "MIT",
  "main": "index.js",
  "scripts": {
    "test": "pixl-unit test.js --verbose"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/pixlcore/class-util"
  },
  "bugs": {
    "url": "https://github.com/pixlcore/class-util/issues"
  },
  "keywords": [
    "oop",
    "class",
    "mixins",
    "async",
	"await"
  ],
  "dependencies": {},
  "devDependencies": {
    "pixl-unit": "^1.0.0"
  }
}

```

## File: README.md
```
# Overview

`class-util` is a simple class utility module, which can do things like asyncify methods, mix-in other classes, add event support, and more.  It does this by providing custom helper functions that augment an ES2015 class.

## Features

- Provide an easy API to augment classes with additional features.
- Support for multiple mix-ins, will merge methods from multiple classes.
- Optional easy way to mix-in the Node.js [EventEmitter](https://nodejs.org/api/events.html#events_class_eventemitter) class.
- Optional hook system (async event emitters).
- Optional conversion of callback methods to async ones.
- No dependencies.

# Usage

Use [npm](https://www.npmjs.com/) to install the module:

```
npm install pixl-class-util
```

Then use `require()` to load it in your code:

```js
const { asyncify, mixin, eventify, hookify } = require('pixl-class-util');
```

Then call one of the following helper functions:

## asyncify

```
VOID asyncify( CLASS, METHODS )
```

Node.js version 8 introduced native support for the [async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)/[await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await) pattern.  If your class has callback-based methods that you want to auto-convert into async/await, simply call `asyncify()` and specify your list of callback methods:

```js
class Sleeper {
	sleep(milliseconds, callback) {
		// sleep for N milliseconds, then fire callback
		setTimeout( function() { callback(); }, milliseconds );
	}
}
asyncify( Sleeper, ['sleep'] );
```

This will convert the `sleep()` method to async, making it instantly ready for async/await (but still supporting callbacks simultaneously).  Example usage:

```js
let snooze = new Sleeper();

(async function() {
	await snooze.sleep( 1000 ); // waits for 1 second here
	console.log("This happened 1 second later!");
})();
```

If you only want *some* of your methods to be asyncified, specify a [regular expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions), to match against all of your class method names.  If the pattern matches, the function will be converted.  Example:

```js
asyncify( Sleeper, /^(sleep|someOtherFunction)$/ );
```

Note that in order for your methods to be async-compatible, they must accept a callback as the final argument, and that callback must be called using the standard Node.js convention (i.e. `(err)` or `(err, result)`).  The error *must* be the first argument sent to the callback (or false/undefined on success), and a result, if any, must be the second argument.

### Async Return Values

If your method's callback is fired using the typical `(err, result)` arguments, such as this:

```js
class Soda {
	pour(callback) {
		setTimeout( function() {
			callback( null, "8oz" );
		}, 250 );
	}
}
asyncify( Soda, ['pour'] );
```

Then you can access the result using async in this way:

```js
let drink = new Soda();

try {
	let result = await drink.pour();
	console.log(result);
}
catch (err) {
	throw err;
}
```

However, if your callback has *multiple result arguments*, like this:

```js
class Soda {
	pour(callback) {
		setTimeout( function() {
			callback( null, 8, "oz" );
		}, 250 );
	}
}
asyncify( Soda, ['pour'] );
```

They will be returned in an array which you can destruct like this:

```js
let drink = new Soda();

try {
	let [amount, units] = await drink.pour();
	console.log(amount, units);
}
catch (err) {
	throw err;
}
```

Finally, for ultimate control over the async conversion, you can pre-declare the names of your callback arguments in the call to `asyncify()`, by setting it to an object containing the function names as keys, and the argument names as array items.  Then, the result can be awaited as a destructed object with named keys.  Here is how to set this up:

```js
class Soda {
	pour(callback) {
		setTimeout( function() {
			callback( null, 8, "oz" ); // fire callback as usual
		}, 250 );
	}
}
asyncify( Soda, {
	pour: ['amount', 'units'] // declare pour() callback arg names here
} );
```

And here is how to await the named arguments:

```js
let drink = new Soda();

try {
	let { amount, units } = await drink.pour();
	console.log(amount, units);
}
catch (err) {
	throw err;
}
```

The idea here is that the calling code can select *which of the arguments it wants*.  For example, we can omit `units` and only fetch `amount`:

```js
let { amount } = await drink.pour();
```

## mixin

```
VOID mixin( CLASS, MIXINS, [FORCE] )
```

Using class-util you can simply merge in one or more "mix-in" classes using the `mixin()` function.  This will import all the public methods, fields and static members from the specified classes, excluding constructors and private properties.  Example:

```js
class Liquid {
	flavor = 'sweet';
}

class Glass {
	size = 8;
}

class Soda {
	drink() {
		console.log("Yum, " + this.size + " oz of " + this.flavor + " drink!");
	}
}

mixin( Soda, [Liquid, Glass] );
```

In the above example we are importing all the fields of the `Liquid` and `Glass` classes into our `Soda` class.  Then, they are accessible using the normal `this` keyword, as if they were defined in the `Soda` class.

I often use mix-ins to spread my larger classes across multiple source files, like this:

```js
mixin( Soda, [ 
	require('./liquid.js'), 
	require('./glass.js') 
] );
```

Then in each of those files (`liquid.js` and `glass.js`) I would export the entire class using `module.exports`.

Note that mix-in methods, fields and static properties will *only* be imported if they aren't already defined in your class.  Meaning, they will not clobber any existing class members.  This is designed to emulate the behavior of multiple inheritance.  You can override this behavior by passing `true` as the 3rd argument to `mixin()`, which will overwrite everything.

If the mix-in classes you are importing have their own parent classes, those should be explicitly listed in the array passed to `mixin()`.  Meaning, the prototype chain of the mix-ins themselves is not automatically imported -- only the top-level methods and static properties on the specified class are merged in.  You'll need to specify mix-in parent classes if you want those merged in as well.

**Note:** Mix-in classes should *not* have a constructor.

## eventify

```
VOID eventify( CLASS )
```

I find myself frequently inheriting from Node's [EventEmitter](http://nodejs.org/api/events.html#events_class_events_eventemitter) in my classes, so I added a shortcut for it in class-util.  Simply call `eventify()`, and your class will magically become an EventEmitter.  Example:

```js
class Party {
	start() {
		console.log("Let's get this party started!");
		this.emit('dance');
	}
}
eventify( Party );

let birthday = new Party();
birthday.on('dance', function() {
	console.log("I'm dancing!");
} );
birthday.start();
```

## hookify

```
VOID hookify( CLASS )
```

Taking event listeners one step further, class-util introduces an optional "hook" system for use in your classes, where custom events can be hooked, and you can run *asynchronous* operations in each listener.  If multiple listeners are registered on a given hook, they are all fired in sequence.  If any listener returns an error, the sequence is aborted, and the error passed to the original caller.

Your listeners can be either callback based, or native [async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function) functions.  To enable hooks in your class, simply call `hoofify()`.  Example:

```js
class Party {
	start() { console.log("The party has finally started."); }
}
hookify( Party );

let birthday = new Party();

birthday.registerHook( 'prestart', function(item, callback) {
	// delay the party by 100ms
	setTimeout( function() { callback(); }, 100 );
} );

birthday.fireHook( 'prestart', "Get ready!", function(err) {
	// all prestart hooks completed, let's go
	// this will run about 100ms later
	birthday.start();
});
```

The idea here is similar with events, where one or more listeners can be registered, but in this case the hooks fire in an asynchronous manner, each with a callback to advance to the next listener, or to complete the hook sequence.  In fact, the whole system can be used with native [async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function) functions (in Node 8+).  Example:

```js
class Party {
	start() { console.log("The party has finally started."); }
}
hookify( Party );

// simple async sleep helper function
const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay));

(async function() {
	let birthday = new Party();

	birthday.registerHook( 'prestart', async function(item) {
		// do something async here
		await sleep(100);
	} );
	
	await birthday.fireHook( 'prestart', "Get ready!");
	
	// all async prestart hooks completed, let's go
	birthday.start();
})();
```

# License

**The MIT License**

*Copyright (c) 2024 Joseph Huckaby*

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

## File: test.js
```
// Unit tests for class-util

const { asyncify, mixin, eventify, hookify } = require('./index.js');

class GenericBaseClass {
	base() { return "BASE"; }
}

exports.tests = [

	function testMixins(test) {
		// mixin base class and another class
		let MyOtherClass = class Other {
			prop1 = "hello";
			static noise = "fzzz";
			bar() { return "baz"; }
		};
		
		let MyClass = class Foo {
			foo() { return "bar"; }
		};
		
		mixin( MyClass, [ GenericBaseClass, MyOtherClass ] );
		
		let instance = new MyClass();
		test.ok( instance.foo() === "bar", "Foo.foo() does not equal bar" );
		test.ok( instance.bar() === "baz", "Foo.bar() does not equal baz" );
		test.ok( instance.base() === "BASE", "Foo.base() does not equal BASE" );
		test.ok( instance.prop1 === "hello", "Property missing from instance" );
		test.ok( MyClass.noise === "fzzz", "Static property missing from instance" );
		test.done();
	},
	
	function testEvents(test) {
		test.expect( 2 );
		
		let MyClass = class Foo {
			foo() { return "bar"; }
		};
		eventify( MyClass );
		
		let instance = new MyClass();
		test.ok( instance.foo() === "bar", "Foo does not equal bar" );
		
		instance.on('party', function() {
			test.ok( true, "Went to party" );
		});
		instance.emit( 'party' );
		
		test.done();
	},
	
	function testHooks(test) {
		let MyClass = class Foo {
			foo() { return "bar"; }
		};
		hookify( MyClass );
		
		let instance = new MyClass();
		test.ok( instance.foo() === "bar", "Foo does not equal bar" );
		
		let went_to_party = false;
		instance.registerHook( 'party', function (thingy, callback) {
			test.ok( true, "Went to party" );
			test.ok( thingy === "present", "Received a present" );
			went_to_party = true;
			setTimeout( function() { callback(); }, 100 ); // delay completion of hook
		});
		
		let went_home = false;
		instance.registerHook( 'party', function(thingy, callback) {
			test.ok( true, "Went home" );
			went_home = true;
			callback(); // same thread
		});
		
		instance.fireHook( 'party', "present", function(err) {
			test.ok( !err, "Unexpected error from party hook: " + err );
			test.ok( went_to_party, "Party hook was not fired" );
			test.ok( went_home, "Second party hook was not fired" );
			test.done();
		} );
	},
	
	function testAsyncify(test) {
		let MyClass = class Foo {
			foo() { return "bar"; }
			
			sleep(ms, callback) {
				setTimeout( function() { callback(); }, ms );
			}
		};
		asyncify( MyClass, 'sleep' );
		
		let instance = new MyClass();
		test.ok( instance.foo() === "bar", "Foo does not equal bar" );
		
		(async function() {
			let before = Date.now();
			await instance.sleep( 100 );
			let elapsed = Date.now() - before;
			// allowing for some error here, as clock corrections do happen
			test.ok( elapsed > 95, "Unexpected elapsed time for await sleep test: " + elapsed );
			test.done();
		})();
	},
	
	function testAsyncifyWithError(test) {
		test.expect(2);
		
		let MyClass = class Foo {
			foo() { return "bar"; }
			
			pour(callback) {
				callback( new Error("frogs") );
			}
		};
		asyncify( MyClass, 'pour' );
		
		let instance = new MyClass();
		test.ok( instance.foo() === "bar", "Foo does not equal bar" );
		
		(async function() {
			try {
				let result = await instance.pour();
			}
			catch(err) {
				test.ok( err.message === 'frogs', "Unexpected error message: " + err.message );
			}
			test.done();
		})();
	},
	
	function testAsyncifyWithSingleArg(test) {
		let MyClass = class Foo {
			foo() { return "bar"; }
			
			pour(callback) {
				callback(null, "8oz");
			}
		};
		asyncify( MyClass, 'pour' );
		
		let instance = new MyClass();
		test.ok( instance.foo() === "bar", "Foo does not equal bar" );
		
		(async function() {
			let result = await instance.pour();
			test.ok( result === "8oz", "Unexpected result: " + result );
			test.done();
		})();
	},
	
	function testAsyncifyWithMultiArgs(test) {
		let MyClass = class Foo {
			foo() { return "bar"; }
			
			pour(callback) {
				callback(null, 8, "oz");
			}
		};
		asyncify( MyClass, 'pour' );
		
		let instance = new MyClass();
		test.ok( instance.foo() === "bar", "Foo does not equal bar" );
		
		(async function() {
			let [amount, units] = await instance.pour();
			test.ok( amount === 8, "Unexpected amount: " + amount );
			test.ok( units === "oz", "Unexpected units: " + units );
			test.done();
		})();
	},
	
	function testAsyncifyWithNamedArgs(test) {
		let MyClass = class Foo {
			foo() { return "bar"; }
			
			pour(callback) {
				callback(null, 8, "oz");
			}
		};
		asyncify( MyClass, { pour: ['amount', 'units'] } );
		
		let instance = new MyClass();
		test.ok( instance.foo() === "bar", "Foo does not equal bar" );
		
		(async function() {
			let {amount, units} = await instance.pour();
			test.ok( amount === 8, "Unexpected amount: " + amount );
			test.ok( units === "oz", "Unexpected units: " + units );
			test.done();
		})();
	},
	
	function testAsyncifyWithNamedArgsSelective(test) {
		let MyClass = class Foo {
			foo() { return "bar"; }
			
			pour(callback) {
				callback(null, 8, "oz");
			}
		};
		asyncify( MyClass, { pour: ['amount', 'units'] } );
		
		let instance = new MyClass();
		test.ok( instance.foo() === "bar", "Foo does not equal bar" );
		
		(async function() {
			let {amount} = await instance.pour();
			test.ok( amount === 8, "Unexpected amount: " + amount );
			test.done();
		})();
	},
	
	function testAsyncHooks(test) {
		let MyClass = class Foo {
			foo() { return "bar"; }
			
			sleep(ms, callback) {
				setTimeout( function() { callback(); }, ms );
			}
		};
		asyncify( MyClass, 'sleep' );
		hookify( MyClass );
		
		let instance = new MyClass();
		test.ok( instance.foo() === "bar", "Foo does not equal bar" );
		
		let went_to_party = false;
		instance.registerHook( 'party', async function (thingy) {
			test.ok( true, "Went to party" );
			test.ok( thingy === "present", "Received a present" );
			went_to_party = true;
			await this.sleep(100);
		});
		
		(async function() {
			let before = Date.now();
			await instance.fireHook( 'party', "present" );
			let elapsed = Date.now() - before;
			// allowing for some error here, as clock corrections do happen
			test.ok( elapsed > 95, "Unexpected elapsed time for async hook test: " + elapsed );
			test.done();
		})();
	}
	
];

```

## File: _GIT_INGEST.md
```
# OmniClaw Repo Plow: CIV_FETCHED_class-util_191517



================================================
FILE: index.js
================================================
// Simple class helper utilities
// Copyright (c) 2024 Joseph Huckaby
// Released under the MIT License

class HookHelper {
	
	registerHook(name, handler) {
		// register a hook, called by plugins
		// hooks are different than event listeners, as they are called in async sequence
		if (!this.hooks) this.hooks = {};
		if (!this.hooks[name]) this.hooks[name] = [];
		this.hooks[name].push( handler );
	}
	
	removeHook(name, handler) {
		// remove single hook listener or all of them
		if (!this.hooks) this.hooks = {};
		if (handler) {
			if (this.hooks[name]) {
				let idx = this.hooks[name].indexOf(handler);
				if (idx > -1) this.hooks[name].splice( idx, 1 );
				if (!this.hooks[name].length) delete this.hooks[name];
			}
		}
		else delete this.hooks[name];
	}
	
	fireHook(name, thingy, callback) {
		// fire all listeners for a given hook
		// calls both sync and async listeners
		let self = this;
		if (!this.hooks) this.hooks = {};
		
		// now do the normal async dance
		if (!this.hooks[name] || !this.hooks[name].length) {
			process.nextTick( callback );
			return;
		}
		
		// fire hooks in async series
		let idx = 0;
		let iterator = function() {
			let handler = self.hooks[name][idx++];
			if (!handler) return callback();
			
			if (handler.constructor.name === "AsyncFunction") {
				// async style
				handler.call( self, thingy ).then( iterator, callback );
			}
			else {
				// callback-style
				let nextThread = 0;
				handler.call( self, thingy, function(err) {
					if (err) return callback(err);
					
					// ensure async, to prevent call stack overflow
					if (nextThread) iterator();
					else process.nextTick( iterator );
				} );
				nextThread++;
			}
		};
		iterator();
	}
	
} // HookHelper

const asyncifyMethod = function(origFunc, argNames) {
	// asyncify a single class method
	// resolution will be array of callback arguments (err, results, etc.)
	// also supports classic callback calling convention
	return async function(...args) {
		let self = this;
		
		// sniff for classic callback style
		if (typeof(args[ args.length - 1 ]) == 'function') return origFunc.call(self, ...args);
		
		// promise/async style
		return new Promise( (resolve, reject) => {
			origFunc.call(self, ...args, function(...results) {
				let err = results.shift();
				if (err) reject(err);
				else if (argNames) {
					let resultsObj = {};
					argNames.forEach( function(name, idx) {
						resultsObj[name] = results[idx];
					} );
					resolve( resultsObj );
				}
				else resolve( (results.length > 1) ? results : results[0] );
			});
		});
	};
}; // asyncifyMethod

/** 
 * Helper functions for classes.
 * @module ClassUtil
 */
const ClassUtil = module.exports = {
	
	/** 
	 * Convert one or more callback-style functions to async.
	 * @param {Function} obj - The class to convert functions in.
	 * @param {(Object|RegExp)} methods - The set of modules to convert.
	 */
	asyncify(obj, methods) {
		// asyncify one or more methods in class
		let proto = obj.prototype;
		if (typeof(methods) == 'string') methods = [ methods ];
		
		if (Array.isArray(methods)) {
			// specific set of methods to asyncify
			methods.forEach( function(key) {
				if (proto[key] && !proto[key].__async && (proto[key].constructor.name !== "AsyncFunction")) {
					proto[key] = asyncifyMethod( proto[key] );
					proto[key].__async = true;
				}
			} );
		}
		else if (methods instanceof RegExp) {
			// regular expression to match against method names
			Object.getOwnPropertyNames(proto).forEach( function(key) { 
				if (!key.match(/^(__name|constructor|prototype)$/) && (typeof(proto[key]) == 'function') && key.match(methods) && !proto[key].__async && (proto[key].constructor.name !== "AsyncFunction")) { 
					proto[key] = asyncifyMethod( proto[key] ); 
					proto[key].__async = true;
				} 
			}); 
		}
		else {
			// hash to define callback arg names for each async func
			for (let key in methods) {
				if (proto[key] && !proto[key].__async && (proto[key].constructor.name !== "AsyncFunction")) {
					proto[key] = asyncifyMethod( proto[key], methods[key] );
					proto[key].__async = true;
				}
			}
		}
	},
	
	/** 
	 * Mixin one or more classes into a target class.
	 * @param {Function} obj - The target class to mix mixins into.
	 * @param {Object} mixers - The array of classes to mixin.
	 * @param {boolean} [force=false] - Overwrite existing methods and static properties.
	 */
	mixin(obj, mixers, force) {
		// mix-in an external class
		let proto = obj.prototype;
		if (!Array.isArray(mixers)) mixers = [ mixers ];
		
		for (let idx = 0, len = mixers.length; idx < len; idx++) {
			let class_obj = mixers[idx];
			let class_proto = class_obj.prototype;
			if (!class_proto) throw new Error("All mixins must be classes.");
			let class_inst = new class_obj();
			
			// prototype methods
			Object.getOwnPropertyNames(class_proto).forEach( function(key) {
				if (!key.match(/^(__name|constructor|prototype)$/) && (!(key in proto) || force)) {
					proto[key] = class_pr

================================================
FILE: package.json
================================================
{
  "name": "pixl-class-util",
  "version": "1.0.1",
  "description": "Helper functions for extending classes with mixins and more.",
  "author": "Joseph Huckaby <jhuckaby@gmail.com>",
  "homepage": "https://github.com/pixlcore/class-util",
  "license": "MIT",
  "main": "index.js",
  "scripts": {
    "test": "pixl-unit test.js --verbose"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/pixlcore/class-util"
  },
  "bugs": {
    "url": "https://github.com/pixlcore/class-util/issues"
  },
  "keywords": [
    "oop",
    "class",
    "mixins",
    "async",
	"await"
  ],
  "dependencies": {},
  "devDependencies": {
    "pixl-unit": "^1.0.0"
  }
}


================================================
FILE: README.md
================================================
# Overview

`class-util` is a simple class utility module, which can do things like asyncify methods, mix-in other classes, add event support, and more.  It does this by providing custom helper functions that augment an ES2015 class.

## Features

- Provide an easy API to augment classes with additional features.
- Support for multiple mix-ins, will merge methods from multiple classes.
- Optional easy way to mix-in the Node.js [EventEmitter](https://nodejs.org/api/events.html#events_class_eventemitter) class.
- Optional hook system (async event emitters).
- Optional conversion of callback methods to async ones.
- No dependencies.

# Usage

Use [npm](https://www.npmjs.com/) to install the module:

```
npm install pixl-class-util
```

Then use `require()` to load it in your code:

```js
const { asyncify, mixin, eventify, hookify } = require('pixl-class-util');
```

Then call one of the following helper functions:

## asyncify

```
VOID asyncify( CLASS, METHODS )
```

Node.js version 8 introduced native support for the [async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)/[await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await) pattern.  If your class has callback-based methods that you want to auto-convert into async/await, simply call `asyncify()` and specify your list of callback methods:

```js
class Sleeper {
	sleep(milliseconds, callback) {
		// sleep for N milliseconds, then fire callback
		setTimeout( function() { callback(); }, milliseconds );
	}
}
asyncify( Sleeper, ['sleep'] );
```

This will convert the `sleep()` method to async, making it instantly ready for async/await (but still supporting callbacks simultaneously).  Example usage:

```js
let snooze = new Sleeper();

(async function() {
	await snooze.sleep( 1000 ); // waits for 1 second here
	console.log("This happened 1 second later!");
})();
```

If you only want *some* of your methods to be asyncified, specify a [regular expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions), to match against all of your class method names.  If the pattern matches, the function will be converted.  Example:

```js
asyncify( Sleeper, /^(sleep|someOtherFunction)$/ );
```

Note that in order for your methods to be async-compatible, they must accept a callback as the final argument, and that callback must be called using the standard Node.js convention (i.e. `(err)` or `(err, result)`).  The error *must* be the first argument sent to the callback (or false/undefined on success), and a result, if any, must be the second argument.

### Async Return Values

If your method's callback is fired using the typical `(err, result)` arguments, such as this:

```js
class Soda {
	pour(callback) {
		setTimeout( function() {
			callback( null, "8oz" );
		}, 250 );
	}
}
asyncify( Soda, ['pour'] );
```

Then you can access the result using async in this way:

```js
let drink = new Soda();

try {
	let result = await drink.pour();
	console.log(result);
}
catch (err) {
	throw err;
}
```

However, if your callback has *multiple result arguments*, like this:

```js
class Soda {
	pour(callback) {
		setTimeout( function() {
			callback( null, 8, "oz" );
		}, 250 );
	}
}
asyncify( Soda, ['pour'] );
```

They will be returned in an array which you can destruct like this:

```js
let drink = new Soda();

try {
	let [amount, units] = await drink.pour();
	console.log(amount, units);
}
catch (err) {
	throw err;
}
```

Finally, for ultimate control over the async conversion, you can pre-declare the names of your callback arguments in the call to `asyncify()`, by setting it to an object containing the function names as keys, and the argument names as array items.  Then, the result can be awaited as a destructed object with named keys.  Here is how to set this up:

```js
class Soda {
	pour(callback) {
		setTimeout( function() {
			callback( null, 8, "oz" ); // fire callback as usual
		}, 250 );
	}
}
asyncify( Soda, {
	pour: ['amount', 'units'] // declare pour() callback arg names here
} );
```

And here is how to await the named arguments:

```js
let drink = new Soda();

try {
	let { amount, units } = await drink.pour();
	console.log(amount, units);
}
catch (err) {
	throw err;
}
```

The idea here is that the calling code can select *which of the arguments it wants*.  For example, we can omit `units` and only fetch `amount`:

```js
let { amount } = await drink.pour();
```

## mixin

```
VOID mixin( CLASS, MIXINS, [FORCE] )
```

Using class-util you can simply merge in one or more "mix-in" classes using the `mixin()` function.  This will import all the public methods, fields and static members from the specified classes, excluding constructors and private properties.  Example:

```js
class Liquid {
	flavor = 'sweet';
}

class Glass {
	size = 8;
}

class Soda {
	drink() {
		console.log("Yum, " + this.size + " oz of " + this.flavor + " drink!");
	}
}

mixin( Soda, [Liquid, Glass] )

================================================
FILE: test.js
================================================
// Unit tests for class-util

const { asyncify, mixin, eventify, hookify } = require('./index.js');

class GenericBaseClass {
	base() { return "BASE"; }
}

exports.tests = [

	function testMixins(test) {
		// mixin base class and another class
		let MyOtherClass = class Other {
			prop1 = "hello";
			static noise = "fzzz";
			bar() { return "baz"; }
		};
		
		let MyClass = class Foo {
			foo() { return "bar"; }
		};
		
		mixin( MyClass, [ GenericBaseClass, MyOtherClass ] );
		
		let instance = new MyClass();
		test.ok( instance.foo() === "bar", "Foo.foo() does not equal bar" );
		test.ok( instance.bar() === "baz", "Foo.bar() does not equal baz" );
		test.ok( instance.base() === "BASE", "Foo.base() does not equal BASE" );
		test.ok( instance.prop1 === "hello", "Property missing from instance" );
		test.ok( MyClass.noise === "fzzz", "Static property missing from instance" );
		test.done();
	},
	
	function testEvents(test) {
		test.expect( 2 );
		
		let MyClass = class Foo {
			foo() { return "bar"; }
		};
		eventify( MyClass );
		
		let instance = new MyClass();
		test.ok( instance.foo() === "bar", "Foo does not equal bar" );
		
		instance.on('party', function() {
			test.ok( true, "Went to party" );
		});
		instance.emit( 'party' );
		
		test.done();
	},
	
	function testHooks(test) {
		let MyClass = class Foo {
			foo() { return "bar"; }
		};
		hookify( MyClass );
		
		let instance = new MyClass();
		test.ok( instance.foo() === "bar", "Foo does not equal bar" );
		
		let went_to_party = false;
		instance.registerHook( 'party', function (thingy, callback) {
			test.ok( true, "Went to party" );
			test.ok( thingy === "present", "Received a present" );
			went_to_party = true;
			setTimeout( function() { callback(); }, 100 ); // delay completion of hook
		});
		
		let went_home = false;
		instance.registerHook( 'party', function(thingy, callback) {
			test.ok( true, "Went home" );
			went_home = true;
			callback(); // same thread
		});
		
		instance.fireHook( 'party', "present", function(err) {
			test.ok( !err, "Unexpected error from party hook: " + err );
			test.ok( went_to_party, "Party hook was not fired" );
			test.ok( went_home, "Second party hook was not fired" );
			test.done();
		} );
	},
	
	function testAsyncify(test) {
		let MyClass = class Foo {
			foo() { return "bar"; }
			
			sleep(ms, callback) {
				setTimeout( function() { callback(); }, ms );
			}
		};
		asyncify( MyClass, 'sleep' );
		
		let instance = new MyClass();
		test.ok( instance.foo() === "bar", "Foo does not equal bar" );
		
		(async function() {
			let before = Date.now();
			await instance.sleep( 100 );
			let elapsed = Date.now() - before;
			// allowing for some error here, as clock corrections do happen
			test.ok( elapsed > 95, "Unexpected elapsed time for await sleep test: " + elapsed );
			test.done();
		})();
	},
	
	function testAsyncifyWithError(test) {
		test.expect(2);
		
		let MyClass = class Foo {
			foo() { return "bar"; }
			
			pour(callback) {
				callback( new Error("frogs") );
			}
		};
		asyncify( MyClass, 'pour' );
		
		let instance = new MyClass();
		test.ok( instance.foo() === "bar", "Foo does not equal bar" );
		
		(async function() {
			try {
				let result = await instance.pour();
			}
			catch(err) {
				test.ok( err.message === 'frogs', "Unexpected error message: " + err.message );
			}
			test.done();
		})();
	},
	
	function testAsyncifyWithSingleArg(test) {
		let MyClass = class Foo {
			foo() { return "bar"; }
			
			pour(callback) {
				callback(null, "8oz");
			}
		};
		asyncify( MyClass, 'pour' );
		
		let instance = new MyClass();
		test.ok( instance.foo() === "bar", "Foo does not equal bar" );
		
		(async function() {
			let result = await instance.pour();
			test.ok( result === "8oz", "Unexpected result: " + result );
			test.done();
		})();
	},
	
	function testAsyncifyWithMultiArgs(test) {
		let MyClass = class Foo {
			foo() { return "bar"; }
			
			pour(callback) {
				callback(null, 8, "oz");
			}
		};
		asyncify( MyClass, 'pour' );
		
		let instance = new MyClass();
		test.ok( instance.foo() === "bar", "Foo does not equal bar" );
		
		(async function() {
			let [amount, units] = await instance.pour();
			test.ok( amount === 8, "Unexpected amount: " + amount );
			test.ok( units === "oz", "Unexpected units: " + units );
			test.done();
		})();
	},
	
	function testAsyncifyWithNamedArgs(test) {
		let MyClass = class Foo {
			foo() { return "bar"; }
			
			pour(callback) {
				callback(null, 8, "oz");
			}
		};
		asyncify( MyClass, { pour: ['amount', 'units'] } );
		
		let instance = new MyClass();
		test.ok( instance.foo() === "bar", "Foo does not equal bar" );
		
		(async function() {
			let {amount, units} = await instance.pour();
			test.ok( amount === 8, "Unexpected amount: " + amount );
			test.ok( units === "oz", "Unexpected units: " + units );
			test.done();
		})();
	},
	
	function testAsyncifyWithNamedArgsSelective(test) {
		let MyClass = class Foo {
			foo() { return "bar"; }
			
	
```


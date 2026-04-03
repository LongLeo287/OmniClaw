---
id: github.com-thenativeweb-node-cqrs-saga-71da9e36-kn
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:27.692832
---

# KNOWLEDGE EXTRACT: github.com_thenativeweb_node-cqrs-saga_71da9e36
> **Extracted on:** 2026-04-01 12:49:57
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007522042/github.com_thenativeweb_node-cqrs-saga_71da9e36

---

## File: `.editorconfig`
```
# EditorConfig is awesome: http://EditorConfig.org
root = true

[*.{js,jsx,json}]
end_of_line = lf
insert_final_newline = true
charset = utf-8
indent_style = space
indent_size = 2
```

## File: `.eslintignore`
```
test/*
```

## File: `.eslintrc`
```
---

env:
  node: true

globals:
  __resourceQuery: false
  describe: false
  describeSaga: false
  describeEvent: false
  describeCommand: false
  before: false
  it: false
  xit: false
  window : false
  beforeEach : false
  afterEach : false
  after : false
  before : false
  beforeEachChapter: false
  describeScenario: false
  describeChapter: false
  describeStep: false
  document : false
  window: false
  File : false
  FormData: false
  QCodeDecoder: false
  $: false
  L: false
  btoa: false
  escape: false
  angular: false
  jQuery: false

rules:
  # ERRORS
  no-unused-vars: [2, {vars: all, args: none}]
  curly: [2, "multi-line"]

  # WARNINGS
  semi-spacing: 1
  no-empty: 1
  handle-callback-err: 1
  eqeqeq: 1
  quotes: [1, 'single']
  no-unused-expressions: 1
  no-throw-literal: 1
  semi: 1
  block-scoped-var: 1
  no-alert: 1
  no-console: 1
  new-cap: 1

  # DISABLED
  space-after-keywords: 0
  dot-notation: 0
  consistent-return: 0
  brace-style: 0
  no-multi-spaces: 0
  no-underscore-dangle: 0
  key-spacing: 0
  comma-spacing: 0
  no-shadow: 0
  no-mixed-requires: 0
  space-infix-ops: 0
  strict: 0
  camelcase: 0
  no-wrap-func: 0
  comma-dangle: 0
  no-extra-semi: 0
  no-use-before-define: [0, "nofunc"]

  # AUTOMATED BY EDITORCONFIG
  eol-last: 0
  no-trailing-spaces: 0
  indent: 0
```

## File: `.gitignore`
```
$ cat .gitignore

# Can ignore specific files
.settings.xml
.monitor

# Use wildcards as well
*~
#*.swp

# Can also ignore all directories and files in a directory.
node_modules
node_modules/**/*

package-lock.json

.idea

.DS_Store

*.tingo
*.db

dump.rdb
```

## File: `.npmignore`
```
test
*.tingo
*.db
*.yml
.editorconfig
.eslintrc
.DS_Store

dump.rdb

.idea
```

## File: `.travis.yml`
```yaml
sudo: false
services:
  - redis-server
  - mongodb
  - couchdb

language: node_js
node_js:
  - "10"
  - "12"
  - "14"

branches:
  only:
    - master

notifications:
  email:
    - adriano@raiano.ch
```

## File: `README.md`
```markdown
# ⚠️ IMPORTANT NEWS! 📰

I’ve been dealing with CQRS, event-sourcing and DDD long enough now that I don’t need working with it anymore unfortunately, so at least for now this my formal farewell!

I want to thank everyone who has contributed in one way or another.
Especially...

- [Jan](https://github.com/jamuhl), who introduced me to this topic.
- [Dimitar](https://github.com/nanov), one of the last bigger contributors and maintainer.
- My last employer, who gave me the possibility to use all these CQRS modules in a big Cloud-System.
- My family and friends, who very often came up short.

Finally, I would like to thank [Golo Roden](https://github.com/goloroden), who was there very early at the beginning of my CQRS/ES/DDD journey and is now here again to take over these modules.

Golo Roden is the founder, CTO and managing director of [the native web](https://www.thenativeweb.io/), a company specializing in native web technologies. Among other things, he also teaches CQRS/ES/DDD etc. and based on his vast knowledge, he brought wolkenkit to life.
[wolkenkit](https://wolkenkit.io) is a CQRS and event-sourcing framework based on Node.js. It empowers you to build and run scalable distributed web and cloud services that process and store streams of domain events.

With this step, I can focus more on [i18next](https://www.i18next.com), [locize](https://locize.com) and [localistars](https://localistars.com). I'm happy about that. 😊

So, there is no end, but the start of a new phase for my CQRS modules. 😉

I wish you all good luck on your journey.

Who knows, maybe we'll meet again in a github issue or PR at [i18next](https://github.com/i18next/i18next) 😉


[Adriano Raiano](https://twitter.com/adrirai)

---

# Introduction

[![travis](https://img.shields.io/travis/adrai/node-cqrs-saga.svg)](https://travis-ci.org/adrai/node-cqrs-saga) [![npm](https://img.shields.io/npm/v/cqrs-saga.svg)](https://npmjs.org/package/cqrs-saga)

Node-cqrs-saga is a node.js module that helps to implement the sagas in cqrs.
It can be very useful as domain component if you work with (d)ddd, cqrs, eventdenormalizer, host, etc.

# Installation

    $ npm install cqrs-saga


# Usage

	var pm = require('cqrs-saga')({
	  // the path to the "working directory"
	  // can be structured like
	  // [set 1](https://github.com/adrai/node-cqrs-saga/tree/master/test/integration/fixture)
	  sagaPath: '/path/to/my/files',

	  // optional, default is 800
	  // if using in scaled systems and not guaranteeing that each event for a saga "instance"
	  // dispatches to the same worker process, this module tries to catch the concurrency issues and
	  // retries to handle the event after a timeout between 0 and the defined value
	  retryOnConcurrencyTimeout: 1000,

	  // optional, default is in-memory
	  // currently supports: mongodb, redis, azuretable and inmemory
	  // hint settings like: [eventstore](https://github.com/adrai/node-eventstore#provide-implementation-for-storage)
	  // mongodb:
	  sagaStore: {
	    type: 'mongodb',
	    host: 'localhost',                          // optional
	    port: 27017,                                // optional
	    dbName: 'domain',                           // optional
	    collectionName: 'sagas',                    // optional
	    timeout: 10000                              // optional
      // authSource: 'authedicationDatabase',        // optional
	    // username: 'technicalDbUser',                // optional
	    // password: 'secret'                          // optional
      // url: 'mongodb://user:pass@host:port/db?opts // optional
	  },
	  // or redis:
	  sagaStore: {
	    type: 'redis',
	    host: 'localhost',                          // optional
	    port: 6379,                                 // optional
	    db: 0,                                      // optional
	    prefix: 'domain_saga',                      // optional
	    timeout: 10000                              // optional
	    // password: 'secret'                          // optional
	  },

	  // optional, default is in-memory
	  // the revisionguard only works if aggregateId and revision are defined in event definition
	  // currently supports: mongodb, redis, tingodb, azuretable and inmemory
	  // hint settings like: [eventstore](https://github.com/adrai/node-eventstore#provide-implementation-for-storage)
	  revisionGuard: {
	  	queueTimeout: 1000,                         // optional, timeout for non-handled events in the internal in-memory queue
	  	queueTimeoutMaxLoops: 3,                    // optional, maximal loop count for non-handled event in the internal in-memory queue
      startRevisionNumber: 1,			                // optional, if defined the denormaizer waits for an event with that revision to be used as first event

	  	type: 'redis',
	  	host: 'localhost',                          // optional
	  	port: 6379,                                 // optional
	  	db: 0,                                      // optional
	  	prefix: 'saga_revision',               			// optional
	  	timeout: 10000                              // optional
	  	// password: 'secret'                       // optional
	  }
		// or, if you don't like to guard revisions ( managed externally ? )
		revisionGuard: false // note has to be set explicitly false
	});


## Catch connect ad disconnect events

	// sagaStore
	pm.sagaStore.on('connect', function() {
	  console.log('sagaStore connected');
	});

	pm.sagaStore.on('disconnect', function() {
	  console.log('sagaStore disconnected');
	});

	// revisionGuardStore
	pm.revisionGuardStore.on('connect', function() {
	  console.log('revisionGuardStore connected');
	});

	pm.revisionGuardStore.on('disconnect', function() {
	  console.log('revisionGuardStore disconnected');
	});


	// anything (sagaStore or revisionGuardStore)
	pm.on('connect', function() {
	  console.log('something connected');
	});

	pm.on('disconnect', function() {
	  console.log('something disconnected');
	});


## Define the event structure
The values describes the path to that property in the event message.

	pm.defineEvent({
	  // optional, default is 'name'
	  name: 'name',

	  // optional, only makes sense if contexts are defined in the 'domainPath' structure
	  context: 'context.name',

	  // optional, only makes sense if aggregates with names are defined in the 'domainPath' structure
	  aggregate: 'aggregate.name',

	  // optional, default is 'aggregate.id'
	  aggregateId: 'aggregate.id',

	  // optional, default is 'revision'
	  // will represent the aggregate revision, can be used in next command
	  revision: 'revision',

	  // optional
	  version: 'version',

	  // optional, if defined theses values will be copied to the command (can be used to transport information like userId, etc..)
	  meta: 'meta'
	});


## Define the command structure
The values describes the path to that property in the command message.

	pm.defineCommand({
	  // optional, default is 'id'
	  id: 'id',

	  // optional, if defined the values of the event will be copied to the command (can be used to transport information like userId, etc..)
	  meta: 'meta'
	});


## Define the id generator function [optional]
### you can define a synchronous function

	pm.idGenerator(function () {
	  var id = require('uuid').v4().toString();
	  return id;
	});

### or you can define an asynchronous function

	pm.idGenerator(function (callback) {
	  setTimeout(function () {
	    var id = require('uuid').v4().toString();
	    callback(null, id);
	  }, 50);
	});


## Wire up commands [optional]
### you can define a synchronous function

	// pass commands to bus
	pm.onCommand(function (cmd) {
	  bus.emit('command', cmd);
	});

### or you can define an asynchronous function

	// pass commands to bus
	pm.onCommand(function (cmd, callback) {
	  bus.emit('command', cmd, function ack () {
	    callback();
	  });
	});


## Wire up event missing [optional]

	pm.onEventMissing(function (info, evt) {

		// grab the missing events, depending from info values...
		// info.aggregateId
		// info.aggregateRevision
		// info.aggregate
		// info.context
		// info.guardRevision
		// and call handle...
		pm.handle(missingEvent, function (err) {
			if (err) { console.log(err); }
		});

	});

you can get the last guarded event:

	pm.getLastEvent(function (err, evt) {

	  if (event.occurredAt < Date.now()) {
	  	// ...
	  }

	});

## Using custom structure loader function
The built-in structure loader can be replaced with one adapted to your needs.
To do that, you need to include a loading method in the options object passed to the domain constructor.

	// options will contain sagaPath as well as the as well as a definition object containing all the constructors of the saga components  ( Saga )
	function structureLoader(options) {

		return [
			new options.definitions.Saga({
				name: 'myEvt'
			}, function (evt, saga, callback) {
				// handle
			}),
			new options.definitions.Saga({
				name: 'myOtherEvt'
			}, function (evt, saga, callback) {
				// handle
			}),
		];
		// or more probably
		return myExternalLoader(options.sagaPath, options.definitions);
	}

	var pm = require('cqrs-saga')({
	  sagaPath: '/path/to/my/files',
		structureLoader: structureLoader
	});

## Initialization

	pm.init(function (err, warnings) {
	  // this callback is called when all is ready...
	  // warnings: if no warnings warnings is null, else it's an array containing errors during require of files
	});

	// or

	pm.init(); // callback is optional


## Handling an event

	pm.handle({
	  id: 'b80ade36-dd05-4340-8a8b-846eea6e286f',
	  name: 'orderCreated',
	  aggregate: {
	    id: '3b4d44b0-34fb-4ceb-b212-68fe7a7c2f70',
	    name: 'order'
	  },
	  context: {
	    name: 'sale'
	  },
	  payload: {
      totalCosts: 520,
      seats: ['4f', '8a']
	  },
	  revision: 0,
	  version: 1,
	  meta: {
	    userId: 'ccd65819-4da4-4df9-9f24-5b10bf89ef89'
	  }
	}); // callback is optional

### or

	pm.handle({
	  id: 'b80ade36-dd05-4340-8a8b-846eea6e286f',
	  name: 'orderCreated',
    aggregate: {
      id: '3b4d44b0-34fb-4ceb-b212-68fe7a7c2f70',
      name: 'order'
    },
    context: {
      name: 'sale'
    },
    payload: {
      totalCosts: 520,
      seats: ['4f', '8a']
    },
	  revision: 0,
	  version: 1,
	  meta: {
	    userId: 'ccd65819-4da4-4df9-9f24-5b10bf89ef89'
	  }
	}, function (errs, cmds) {
	  // this callback is called when event is handled successfully or unsuccessfully
	  // errs can be of type:
	  // - null
	  // - Array of Errors
	  //
	  // cmds: same as passed in 'onCommand' function
	});

### more infos, can be useful if testing

	pm.handle({
	  id: 'b80ade36-dd05-4340-8a8b-846eea6e286f',
	  name: 'orderCreated',
    aggregate: {
      id: '3b4d44b0-34fb-4ceb-b212-68fe7a7c2f70',
      name: 'order'
    },
    context: {
      name: 'sale'
    },
    payload: {
      totalCosts: 520,
      seats: ['4f', '8a']
    },
	  meta: {
	    userId: 'ccd65819-4da4-4df9-9f24-5b10bf89ef89'
	  }
	}, function (errs, cmds, sagaModels) {
	  // this callback is called when event is handled successfully or unsuccessfully
	  // errs: is the same as described before

	  // cmds: same as passed in 'onCommand' function
	  // cmds: in case of no error or in case of error here is the array of all commands that should be published

	  // sagaModels: represents the saga data after have handled the event
	});


## Request saga information

After the initialization you can request the saga information:

	pm.init(function (err) {
	  pm.getInfo();
	  // ==>
	  // {
	  //   "sagas": [
	  //     {
	  //       "name": "orderConfirmed",
	  //       "aggregate": "order",
	  //       "context": "sale",
	  //       "version": 0
	  //     },
	  //     {
	  //       "name": "orderCreated",
	  //       "aggregate": "order",
	  //       "context": "sale",
	  //       "version": 0
	  //     },
	  //     {
	  //       "name": "paymentAccepted",
	  //       "aggregate": "payment",
	  //       "context": "sale",
	  //       "version": 2
	  //     },
	  //     {
	  //       "name": "seatsReserved",
	  //       "aggregate": "reservation",
	  //       "context": "sale",
	  //       "version": 0
	  //     }
	  //   ]
	  // }
	});


# Components definition

## Saga

	module.exports = require('cqrs-saga').defineSaga({
	  // optional, default is file name without extension
	  name: 'orderCreated',

	  // optional
	  aggregate: 'order',

	  // optional
	  context: 'sale',

	  // optional, default 0
	  version: 1,

	  // optional, default false
	  // if true it will check if there is already a saga in the db and only if there is something it will continue...
	  existing: false,

	  // optional, will catch the event only if it contains the defined properties
	  containingProperties: ['aggregate.id', 'payload.totalCosts', 'payload.seats'],

	  // optional, if not defined it will pass the whole event...
	  payload: 'payload',

	  // optional, if not defined it will generate a new id
	  // it will try to load the saga from the db by this id
	  id: 'aggregate.id',

	  // optional, default Infinity, all sagas will be sorted by this value
	  priority: 1
	}, function (evt, saga, callback) {

	  // if you have multiple concurrent events that targets the same saga, you can catch it like this:
	  if (saga.actionOnCommit === 'create') {
	  	return this.retry();
	  	// or
	  	//return this.retry(100); // retries to handle again in 0-100ms
	  	// or
	  	//return this.retry({ from: 500, to: 8000 }); // retries to handle again in 500-8000ms
	  }

	  saga.set('orderId', evt.aggregate.id);
	  saga.set('totalCosts', evt.payload.totalCosts);
	  // or
	  // saga.set({ orderId: evt.aggregate.id, totalCosts: evt.payload.totalCosts });

	  var cmd = {

	    // if you don't pass an id it will generate a new one
	    id: 'my own command id',
	    name: 'makeReservation',
	    aggregate: {
	      name: 'reservation'
	    },
	    context: {
	      name: 'sale'
	    },
	    payload: {
	      transactionId: saga.id,
	      seats: saga.has('seats') ? saga.get('seats') : evt.payload.seats
	    },

	    // to transport meta infos (like userId)...
	    // if not defined, it will use the meta value of the event
	    meta: evt.meta
	  };

	  saga.addCommandToSend(cmd);

	  // optionally define a timeout
	  // this can be useful if you have an other process that will fetch timeouted sagas
	  var tomorrow = new Date();
	  tomorrow.setDate((new Date()).getDate() + 1);
	  var timeoutCmd = {

	    // if you don't pass an id it will generate a new one
	    id: 'my own command id',
	    name: 'cancelOrder',
	    aggregate: {
	      name: 'order',
	      id: evt.aggregate.id
	    },
	    context: {
	      name: 'sale'
	    },
	    payload: {
	      transactionId: saga.id
	    },

	    // to transport meta infos (like userId)...
	    // if not defined, it will use the meta value of the event
	    meta: evt.meta
	  };
	  saga.defineTimeout(tomorrow, [timeoutCmd]);
	  // or
	  // saga.defineTimeout(tomorrow, timeoutCmd);
	  // or
	  // saga.defineTimeout(tomorrow);

	  saga.commit(callback);
	});
	// optional define a function to that returns an id that will be used as saga id
	//.useAsId(function (evt) {
	//  return 'newId';
	//});
	// or
	//.useAsId(function (evt, callback) {
	//  callback(null, 'newId');
	//});
	//
	// optional define a function that checks if an event should be handled ( before saga is loaded )
	//.defineShouldHandleEvent(function (evt) {
	//  return true;
	//});
	// or
	//.defineShouldHandleEvent(function (evt, callback) {
	//  callback(null, true');
	//});
	//
	// optional define a function that checks if an event should be handled ( after saga is loaded )
	//.defineShouldHandle(function (evt, saga) {
	//  return true;
	//});
	// or
	//.defineShouldHandle(function (evt, saga, callback) {
	//  callback(null, true');
	//});


# Persistence functions

## getTimoutedSagas
Use this function to get all timeouted sagas.

	pm.getTimeoutedSagas(function (err, sagas) {
	  if (err) { return console.log('ohh!'); }

	  sagas.forEach(function (saga) {
	    // saga.id...
	    // saga.getTimeoutAt();
	    var cmds = saga.getTimeoutCommands();

	    cmds.forEach(function (cmd) {
	    	saga.addCommandToSend(cmd);
	    });

	    saga.commit(function (err) {
        // if you have registered the pm.onCommand handler it will be automatically executed,
        // if you have not registered the pm.onCommand handler you need to publish and set the command to dispatched on your own!
	    	cmds.forEach(function (cmd) {
	    		// publish cmd...
	    		// msgBus.send(cmd);
	    		// ... and set to dispatched...
	    		pm.setCommandToDispatched(cmd.id, saga.id, function (err) {});
	    	});
	    });

	    // or if saga does not clean itself after timouted and/or no commands are defined, then:
	    // pm.removeSaga(saga || saga.id, function (err) {});
	    // or
	    // saga.destroy();
	    // saga.commit(function (err) {});
	  });
	});

## getOlderSagas
Use this function to get all sagas that are older then the passed date.

	pm.getOlderSagas(new Date(2010, 2, 4), function (err, sagas) {
	  if (err) { return console.log('ohh!'); }

	  sagas.forEach(function (saga) {
	    // saga.id...
	    // saga.getTimeoutAt();
	    // saga.getTimeoutCommands();

	    // if saga does not clean itself after timouted and/or no commands are defined, then:
	    pm.removeSaga(saga || saga.id, function (err) {});
	    // or
	    // saga.destroy();
	    // saga.commit(function (err) {});
	  });
	});

## getUndispatchedCommands | setCommandToDispatched
Use getUndispatchedCommands to get all undispatched commands.

Use setCommandToDispatched to mark a command as dispatched. (will remove it from the db)

	pm.getUndispatchedCommands(function (err, cmds) {
	  if (err) { return console.log('ohh!'); }

	  cmds.forEach(function (cmd) {
	    // cmd is: { sagaId: 'the id of the saga', commandId: 'the id of the command', commitStamp: 'a date', command: { /* the command */ } }

	    pm.setCommandToDispatched(cmd.commandId, cmd.sagaId, function (err) {});
	  });
	});


## ES6 default exports
Importing ES6 style default exports is supported for all definitions where you also use `module.exports`:
```
module.exports = defineSaga({...});
```
works as well as 
```
exports.default = defineSaga({...});
```
as well as (must be transpiled by babel or tsc to be runnable in node)
```
export default defineSaga({...});
```
Exports other than the default export are then ignored by this package's structure loader.

[Release notes](https://github.com/adrai/node-cqrs-saga/blob/master/releasenotes.md)

# License

Copyright (c) 2018 Adriano Raiano

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

## File: `index.js`
```javascript
var ProcessManagement = require('./lib/pm'),
  _ = require('lodash'),
  fs = require('fs'),
  path = require('path');

function pm (options) {
  return new ProcessManagement(options);
}

/**
 * Calls the constructor.
 * @param  {Object} klass Constructor function.
 * @param  {Array}  args  Arguments for the constructor function.
 * @return {Object}       The new object.
 */
function construct(klass, args) {
  function T() {
    klass.apply(this, arguments[0]);
  }
  T.prototype = klass.prototype;
  return new T(args);
}

var files = fs.readdirSync(path.join(__dirname, 'lib/definitions'));

files.forEach(function (file) {
  var name = path.basename(file, '.js');
  var nameCap = name.charAt(0).toUpperCase() + name.slice(1);
  pm['define' + nameCap] = function () {
    return construct(require('./lib/definitions/' + name), _.toArray(arguments));
  };
});

module.exports = pm;
```

## File: `licence`
```
Copyright (c) 2018 Adriano Raiano

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
  "author": "adrai",
  "name": "cqrs-saga",
  "version": "1.11.14",
  "private": false,
  "main": "index.js",
  "engines": {
    "node": ">=0.8.0"
  },
  "directories": {
    "lib": "./lib"
  },
  "dependencies": {
    "async": "1.5.2",
    "debug": "3.1.0",
    "dotty": "0.0.2",
    "jsondate": "0.0.1",
    "lodash": "4.17.19",
    "parent-require": "1.0.0",
    "tolerance": "1.0.0",
    "uuid": "3.3.2"
  },
  "devDependencies": {
    "azure-storage": ">=0.3.0",
    "cradle": ">=0.6.7",
    "eslint": ">=1.0.0",
    "expect.js": ">= 0.1.2",
    "mocha": "3.x.x",
    "mongodb": "2.1.x",
    "redis": ">= 0.10.1",
    "tingodb": ">= 0.0.1"
  },
  "description": "Node-cqrs-saga is a node.js module that helps to implement the sagas in cqrs. It can be very useful as domain component if you work with (d)ddd, cqrs, eventdenormalizer, host, etc.",
  "keywords": [
    "cqrs",
    "saga",
    "eventsourcing",
    "ddd",
    "dddd",
    "command",
    "event",
    "eventdenormalizer",
    "domain"
  ],
  "homepage": "https://github.com/adrai/node-cqrs-saga",
  "repository": {
    "type": "git",
    "url": "git@github.com:adrai/node-cqrs-saga.git"
  },
  "bugs": {
    "url": "https://github.com/adrai/node-cqrs-saga/issues"
  },
  "licenses": [
    {
      "type": "MIT",
      "url": "https://raw.github.com/adrai/node-cqrs-saga/master/licence"
    }
  ],
  "scripts": {
    "test": "mocha test/unit && mocha test/integration"
  }
}
```

## File: `releasenotes.md`
```markdown
## [v1.11.14](https://github.com/adrai/node-cqrs-saga/compare/v1.11.13...v1.11.14)
- mongodb: useUnifiedTopology

## [v1.11.13](https://github.com/adrai/node-cqrs-saga/compare/v1.11.12...v1.11.13)
- add option not to use the revisionGuardStore

## [v1.11.12](https://github.com/adrai/node-cqrs-saga/compare/v1.11.11...v1.11.12)
- replace additional deprecated mongo methods

## [v1.11.11](https://github.com/adrai/node-cqrs-saga/compare/v1.11.1...v1.11.11)
- remove debug forgotten console messages

## [v1.11.1](https://github.com/adrai/node-cqrs-saga/compare/v1.11.0...v1.11.1)
- replace deprecated mongo methods ( ensureIndex, insert, remove, update )
- add optional shouldHandleEvent function, to filter events before loading saga

## [v1.11.0](https://github.com/adrai/node-cqrs-saga/compare/v1.10.2...v1.11.0)
- add option to add custom structureLoader implementation

## [v1.10.2](https://github.com/adrai/node-cqrs-saga/compare/v1.10.1...v1.10.2)
- remove deprecated option max_attempts from redis options

## [v1.10.1](https://github.com/adrai/node-cqrs-saga/compare/v1.9.1...v1.10.1)
- compatibility with new mongodb version (3.x)

## [v1.9.1](https://github.com/adrai/node-cqrs-saga/compare/v1.9.0...v1.9.1)
- add possibility to call removeTimeout after getTimeoutSagas and getOlderSagas [#42](https://github.com/adrai/node-cqrs-saga/issues/#42) thanks to [edro](https://github.com/edro)

## [v1.9.0](https://github.com/adrai/node-cqrs-saga/compare/v1.8.0...v1.9.0)
- optional pagination for getTimeoutedSagas and getUndispatchedCommands

## [v1.8.0](https://github.com/adrai/node-cqrs-saga/compare/v1.7.3...v1.8.0)
- Support default exports [#40](https://github.com/adrai/node-cqrs-saga/pull/#40) thanks to [IRT-fbachmann](https://github.com/IRT-fbachmann)

## [v1.7.3](https://github.com/adrai/node-cqrs-saga/compare/v1.7.2...v1.7.3)
- fix saga callback on retry [#39](https://github.com/adrai/node-cqrs-saga/pull/#39) thanks to [nanov](https://github.com/nanov)

## [v1.7.2](https://github.com/adrai/node-cqrs-saga/compare/v1.7.1...v1.7.2)
- optimize handling for commandRejected

## [v1.7.1](https://github.com/adrai/node-cqrs-saga/compare/v1.6.27...v1.7.1)
- for getTimeoutedSagas handling: if the pm.onCommand handler is registered it will be automatically executed

## [v1.6.27](https://github.com/adrai/node-cqrs-saga/compare/v1.6.25...v1.6.27)
- fix for new mongodb driver

## [v1.6.25](https://github.com/adrai/node-cqrs-saga/compare/v1.6.24...v1.6.25)
- update deps

## [v1.6.24](https://github.com/adrai/node-cqrs-saga/compare/v1.6.23...v1.6.24)
- edgecase in revisionGuard

## [v1.6.23](https://github.com/adrai/node-cqrs-saga/compare/v1.6.22...v1.6.23)
- redis, mongodb: call disconnect on ping error

## [v1.6.22](https://github.com/adrai/node-cqrs-saga/compare/v1.6.21...v1.6.22)
- Fix events getting lost at high concurrency [#33](https://github.com/adrai/node-cqrs-saga/pull/#33) thanks to [hilkeheremans](https://github.com/hilkeheremans)

## [v1.6.21](https://github.com/adrai/node-cqrs-saga/compare/v1.6.20...v1.6.21)
- Support mongo connection string

## [v1.6.20](https://github.com/adrai/node-cqrs-saga/compare/v1.6.19...v1.6.20)
- redis, mongodb: call disconnect on ping error

## [v1.6.19](https://github.com/adrai/node-cqrs-saga/compare/v1.6.17...v1.6.19)
- revisionGuard: optional startRevisionNumber

## [v1.6.17](https://github.com/adrai/node-cqrs-saga/compare/v1.6.16...v1.6.17)
- redis: added optional heartbeat

## [v1.6.16](https://github.com/adrai/node-cqrs-saga/compare/v1.6.15...v1.6.16)
- fix defineShouldHandle

## [v1.6.15](https://github.com/adrai/node-cqrs-saga/compare/v1.6.14...v1.6.15)
- revisionGuard fix

## [v1.6.14](https://github.com/adrai/node-cqrs-saga/compare/v1.6.13...v1.6.14)
- redis: fix for new redis lib

## [v1.6.13](https://github.com/adrai/node-cqrs-saga/compare/v1.6.12...v1.6.13)
- mongodb: added optional heartbeat

## [v1.6.12](https://github.com/adrai/node-cqrs-saga/compare/v1.6.11...v1.6.12)
- redis: fix wrong multi response handling

## [v1.6.11](https://github.com/adrai/node-cqrs-saga/compare/v1.6.10...v1.6.11)
- optimize handling of guarding the first events

## [v1.6.10](https://github.com/adrai/node-cqrs-saga/compare/v1.6.9...v1.6.10)
- remove trycatch dependency due to memory leaks

## [v1.6.9](https://github.com/adrai/node-cqrs-saga/compare/v1.6.8...v1.6.9)
- give possibility to use mongodb with authSource

## [v1.6.8](https://github.com/adrai/node-cqrs-saga/compare/v1.6.7...v1.6.8)
- updated dep

## [v1.6.7](https://github.com/adrai/node-cqrs-saga/compare/v1.6.6...v1.6.7)
- optimization for `npm link`'ed development

## [v1.6.6](https://github.com/adrai/node-cqrs-saga/compare/v1.6.4...v1.6.6)
- catch throwing errors when calling callback

## [v1.6.4](https://github.com/adrai/node-cqrs-saga/compare/v1.6.3...v1.6.4)
- expose warnings during initialization

## [v1.6.3](https://github.com/adrai/node-cqrs-saga/compare/v1.6.2...v1.6.3)
- better catch for userland errors

## [v1.6.2](https://github.com/adrai/node-cqrs-saga/compare/v1.6.1...v1.6.2)
- fix alreadyInQueue check

## [v1.6.1](https://github.com/adrai/node-cqrs-saga/compare/v1.6.0...v1.6.1)
- redis: replace .keys() calls with .scan() calls => scales better

## [v1.6.0](https://github.com/adrai/node-cqrs-saga/compare/v1.5.0...v1.6.0)
- introduce possibility to define a shouldHandle function

## [v1.5.0](https://github.com/adrai/node-cqrs-saga/compare/v1.4.0...v1.5.0)
- when using revisionGuard, always save the last event
- when using revisionGuard, added possibility to fetch the last handled event

## [v1.4.0](https://github.com/adrai/node-cqrs-saga/compare/v1.3.0...v1.4.0)
- add retry mechanism for saga

## [v1.3.0](https://github.com/adrai/node-cqrs-saga/compare/v1.2.9...v1.3.0)
- fix revisionGuard when handling duplicate events at the same time

## [v1.2.9](https://github.com/adrai/node-cqrs-saga/compare/v1.2.8...v1.2.9)
- fixed mongodb indexes

## [v1.2.8](https://github.com/adrai/node-cqrs-saga/compare/v1.2.7...v1.2.8)
- added mongodb driver 2.x support

## [v1.2.7](https://github.com/adrai/node-cqrs-saga/compare/v1.2.4...v1.2.7)
- optimize structureParser

## [v1.2.4](https://github.com/adrai/node-cqrs-saga/compare/v1.2.3...v1.2.4)
- added convenience information on sagaModel (actionOnCommit)

## [v1.2.3](https://github.com/adrai/node-cqrs-saga/compare/v1.2.1...v1.2.3)
- fix usage with own db implementation

## [v1.2.1](https://github.com/adrai/node-cqrs-saga/compare/v1.2.0...v1.2.1)
- generate command id if not set even if destroying the saga

## [v1.2.0](https://github.com/adrai/node-cqrs-saga/compare/v1.1.3...v1.2.0)
- added getInfo function

## [v1.1.3](https://github.com/adrai/node-cqrs-saga/compare/v1.1.2...v1.1.3)
- added commitstamp to getUndispatchedcommands
- added possibility to addCommandToSend for timeoutedSagas

## [v1.1.2](https://github.com/adrai/node-cqrs-saga/compare/v1.1.1...v1.1.2)
- handle case of same aggregateId in different contexts or aggregates

## [v1.1.1](https://github.com/adrai/node-cqrs-saga/compare/v1.1.0...v1.1.1)
- added azure-table support [#2](https://github.com/adrai/node-cqrs-saga/pull/#2) thanks to [sbiaudet](https://github.com/sbiaudet) and [rvin100](https://github.com/rvin100)

## [v1.1.0](https://github.com/adrai/node-cqrs-saga/compare/v1.0.2...v1.1.0)
- introduce revisionGuard

## v1.0.2
- saga: optional define a function to that returns an id that will be used as saga id

## v1.0.1
- make redis commit transactional

## v1.0.0
- first stable release
```

## File: `lib/definitionBase.js`
```javascript
var _ = require('lodash');

/**
 * Definition constructor
 * @param {Object} meta meta infos like: { name: 'name' }
 * @constructor
 */
function Definition (meta) {
  if (!this.name && meta && meta.name) {
    this.name = meta.name;
  }

  this.options = {};

  this.definitions = {
    command: {
      id: 'id'
////      name: 'name',                   // optional
////      aggregateId: 'aggregate.id',    // optional
////      context: 'context.name',        // optional
////      aggregate: 'aggregate.name',    // optional
////      payload: 'payload',             // optional
////      revision: 'revision',           // optional
////      version: 'version',             // optional
//      meta: 'meta'                    // optional (will be passed directly to corresponding event(s))
    },
    event: {
////      correlationId: 'correlationId', // optional
////      id: 'id',                       // optional
      name: 'name'
////      aggregateId: 'aggregate.id',    // optional
//      context: 'context.name',        // optional
//      aggregate: 'aggregate.name',    // optional
////      payload: 'payload',             // optional
////      revision: 'revision'            // optional
//      version: 'version',             // optional
//      meta: 'meta'                    // optional (will be passed directly from corresponding command)
    }
  };
}

/**
 * Inject definition for command structure.
 * @param   {Object} definition the definition to be injected
 */
Definition.prototype.defineCommand = function (definition) {
  if (!_.isObject(definition)) {
    throw new Error('Please pass in an object');
  }
  this.definitions.command = _.defaults(definition, this.definitions.command);
};

/**
 * Inject definition for event structure.
 * @param   {Object} definition the definition to be injected
 */
Definition.prototype.defineEvent = function (definition) {
  if (!_.isObject(definition)) {
    throw new Error('Please pass in an object');
  }
  this.definitions.event = _.defaults(definition, this.definitions.event);
  return this;
};

/**
 * Inject options.
 * @param   {Object} options the options to be injected
 */
Definition.prototype.defineOptions = function (options) {
  if (!_.isObject(options)) {
    throw new Error('Please pass in an object');
  }
  this.options = options;
  return this;
};

module.exports = Definition;
```

## File: `lib/eventDispatcher.js`
```javascript
var debug = require('debug')('saga:eventDispatcher'),
  _ = require('lodash'),
  async = require('async'),
  dotty = require('dotty');

/**
 * EventDispatcher constructor
 * @param {Object} structureSearcher The tree object.
 * @param {Object} definition        The definition object.
 * @constructor
 */
function EventDispatcher (structureSearcher, definition) {
  if (!structureSearcher || !_.isObject(structureSearcher) || !_.isFunction(structureSearcher.getSagas)) {
    var err = new Error('Please pass a valid tree!');
    debug(err);
    throw err;
  }

  if (!definition || !_.isObject(definition)) {
    var err = new Error('Please pass a valid command definition!');
    debug(err);
    throw err;
  }

  this.structureSearcher = structureSearcher;
  this.definition = definition;
}

EventDispatcher.prototype = {

  /**
   * Returns the target information of this event.
   * @param {Object} evt The passed event.
   * @returns {{name: 'eventName', aggregateId: 'aggregateId', version: 0, aggregate: 'aggregateName', context: 'contextName'}}
   */
  getTargetInformation: function (evt) {
    if (!evt || !_.isObject(evt)) {
      var err = new Error('Please pass a valid event!');
      debug(err);
      throw err;
    }

    var name = dotty.get(evt, this.definition.name);

    var version = 0;
    if (dotty.exists(evt, this.definition.version)) {
      version = dotty.get(evt, this.definition.version);
    } else {
      debug('no version found, handling as version: 0');
    }

    var aggregate = null;
    if (dotty.exists(evt, this.definition.aggregate)) {
      aggregate = dotty.get(evt, this.definition.aggregate);
    } else {
      debug('no aggregate found');
    }

    var context = null;
    if (dotty.exists(evt, this.definition.context)) {
      context = dotty.get(evt, this.definition.context);
    } else {
      debug('no aggregateName found');
    }

    return {
      name: name,
      version: version,
      aggregate: aggregate,
      context: context
    };
  },

  /**
   * Dispatches an event.
   * @param {Object}   evt      The passed event.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err, sagaModels){}`
   */
  dispatch: function (evt, callback) {
    if (!evt || !_.isObject(evt)) {
      var err = new Error('Please pass a valid event!');
      debug(err);
      throw err;
    }

    if (!callback || !_.isFunction(callback)) {
      var err = new Error('Please pass a valid callback!');
      debug(err);
      throw err;
    }

    var target = this.getTargetInformation(evt);

    var sagas = this.structureSearcher.getSagas(target);

    if (!sagas) {
      debug('no saga found for ' + target.name);
      return callback(null, []);
    }

    var errs = [];
    var sagaModels = [];
    async.each(sagas, function (saga, callback) {
      saga.handle(evt, function (err, sagaModel) {
        if (err) {
          debug(err);
          errs.push(err);
        }

        if (sagaModel) {
          sagaModels.push(sagaModel);
        }
        callback(null);
      });
    }, function () {
      if (errs.length === 0) {
        errs = null;
      }
      callback(errs, sagaModels);
    });
  }

};

module.exports = EventDispatcher;
```

## File: `lib/orderQueue.js`
```javascript
var debug = require('debug')('saga:orderQueue'),
  _ = require('lodash'),
  AlreadyHandlingError = require('./errors/alreadyHandlingError');

/**
 * Queue constructor
 * @param {Object} options The options object. Like: { queueTimeout: 3000 }
 * @constructor
 */
function Queue (options) {
  this.queue = {};
  this.retries = {};
  this.options = options || { queueTimeout: 3000 };
}

Queue.prototype = {

  /**
   * Pushes a new item in the queue.
   * @param {String}   id     The aggregate id.
   * @param {String}   objId  The event id.
   * @param {Object}   object The event.
   * @param {Function} clb    The callback function for the event handle.
   * @param {Function} fn     The timeout function handle.
   */
  push: function (id, objId, object, clb, fn) {
    this.queue[id] = this.queue[id] || [];

    var alreadyInQueue = _.find(this.queue[id], function (o) {
      return o.id === objId;
    });

    if (alreadyInQueue) {
      debug('event already handling [concatenatedId]=' + id + ', [evtId]=' + objId);
      clb(new AlreadyHandlingError('Event: [id]=' + objId + ', [evtId]=' + objId + ' already handling!'), function (done) {
        done(null);
      });
      return;
    }

    this.queue[id].push({ id: objId, payload: object, callback: clb });

    this.retries[id] = this.retries[id] || {};

    this.retries[id][objId] = this.retries[id][objId] || 0;

    if (fn) {
      var self = this;
      (function wait () {
        debug('wait called [concatenatedId]=' + id + ', [evtId]=' + objId);
        setTimeout(function () {
          var found = _.find(self.queue[id], function (o) {
            return o.id === objId;
          });
          if (found) {
            var loopCount = self.retries[id][objId]++;
            fn(loopCount, wait);
          }
        }, self.options.queueTimeout);
      })();
    }
  },

  /**
   * Returns the pending events for an aggregate.
   * @param {String} id The aggregate id.
   * @returns {Array}
   */
  get: function (id) {
    if (!this.queue[id] || this.queue[id].length === 0) {
      return null;
    }
    return this.queue[id];
  },

  /**
   * Removes an event from the queue.
   * @param {String} id    The aggregate id.
   * @param {String} objId The event id.
   */
  remove: function (id, objId) {
    if (this.queue[id]) {
      _.remove(this.queue[id], function (o) {
        return o.id === objId;
      });
    }

    if (objId && this.retries[id] && this.retries[id][objId]) {
      this.retries[id][objId] = 0;
    }
  },

  /**
   * NEVER USE THIS FUNCTION!!! ONLY FOR TESTS!
   * clears the complete queue...
   */
  clear: function() {
    this.queue = {};
    this.retries = {};
  }

};

module.exports = Queue;
```

## File: `lib/pm.js`
```javascript
var debug = require('debug')('saga'),
  async = require('async'),
  util = require('util'),
  EventEmitter = require('events').EventEmitter,
  _ = require('lodash'),
  EventDispatcher = require('./eventDispatcher'),
  sagastore = require('./store'),
  uuid = require('uuid').v4,
  dotty = require('dotty'),
  RevisionGuard = require('./revisionGuard'),
  revisionGuardStore = require('./revisionGuardStore'),
  SagaModel = require('./sagaModel'),
  customLoader = require('./structure/customLoader'),
  structureLoader = require('./structure/structureLoader'),
  attachLookupFunctions = require('./structure/structureSearcher');


function createStructureLoader (options) {
  if (options) {
    if (!_.isFunction(options)) {
      var err = new Error('"options.structureLoader" is not a valid structure loader method');
      debug(err);
      throw err;
    };
    return customLoader(options);
  }
  return structureLoader;
}
  
/**
 * ProcessManagement constructor
 * @param {Object} options The options.
 * @constructor
 */
function ProcessManagement(options) {
  EventEmitter.call(this);

  options = options || {};

  if (!options.sagaPath && options.sagaPath !== '') {
    var err = new Error('Please provide sagaPath in options');
    debug(err);
    throw err;
  }

  var defaults = {
    commandRejectedEventName: 'commandRejected'
  };

  _.defaults(options, defaults);

  this.structureLoader = createStructureLoader(options.structureLoader);
  this.sagaStore = sagastore.create(options.sagaStore);

  options.retryOnConcurrencyTimeout = options.retryOnConcurrencyTimeout || 800;

  var defaultRevOpt = {
    queueTimeout: 1000,
    queueTimeoutMaxLoops: 3//,
    // startRevisionNumber: 1
  };

  if (options.revisionGuard !== false) {
    options.revisionGuard = options.revisionGuard || {};
    _.defaults(options.revisionGuard, defaultRevOpt);
    this.revisionGuardStore = revisionGuardStore.create(options.revisionGuard);
  }

  this.options = options;

  this.definitions = {
    command: {
      id: 'id'
////      name: 'name',                   // optional
////      aggregateId: 'aggregate.id',    // optional
////      context: 'context.name',        // optional
////      aggregate: 'aggregate.name',    // optional
////      payload: 'payload',             // optional
////      revision: 'revision',           // optional
////      version: 'version',             // optional
//      meta: 'meta'                    // optional (will be passed directly to corresponding event(s))
    },
    event: {
////      correlationId: 'correlationId', // optional
////      id: 'id',                       //optional
      name: 'name'
////      aggregateId: 'aggregate.id',    // optional
//      context: 'context.name',        // optional
//      aggregate: 'aggregate.name',    // optional
////      payload: 'payload',             // optional
////      revision: 'revision'            // optional
//      version: 'version',             // optional
//      meta: 'meta'                    // optional (will be passed directly from corresponding command)
    }
  };

  this.idGenerator(function () {
    return uuid().toString();
  });

  // DO not register a "dummy" onCommand handler because of getTimeoutedSagas handling
  // this.onCommand(function (cmd) {
  //   debug('emit:', cmd);
  // });

  this.onEventMissing(function (info, evt) {
    debug('missing events: ', info, evt);
  });
}

util.inherits(ProcessManagement, EventEmitter);

_.extend(ProcessManagement.prototype, {

  /**
   * Inject definition for command structure.
   * @param   {Object} definition the definition to be injected
   * @returns {ProcessManagement} to be able to chain...
   */
  defineCommand: function (definition) {
    if (!definition || !_.isObject(definition)) {
      var err = new Error('Please pass a valid definition!');
      debug(err);
      throw err;
    }

    this.definitions.command = _.defaults(definition, this.definitions.command);
    return this;
  },

  /**
   * Inject definition for event structure.
   * @param   {Object} definition the definition to be injected
   * @returns {ProcessManagement} to be able to chain...
   */
  defineEvent: function (definition) {
    if (!definition || !_.isObject(definition)) {
      var err = new Error('Please pass a valid definition!');
      debug(err);
      throw err;
    }

    this.definitions.event = _.defaults(definition, this.definitions.event);
    return this;
  },

  /**
   * Inject idGenerator function.
   * @param   {Function}  fn      The function to be injected.
   * @returns {ProcessManagement} to be able to chain...
   */
  idGenerator: function (fn) {
    if (!fn || !_.isFunction(fn)) {
      var err = new Error('Please pass a valid function!');
      debug(err);
      throw err;
    }

    if (fn.length === 1) {
      this.getNewId = fn;
      return this;
    }

    this.getNewId = function (callback) {
      callback(null, fn());
    };

    return this;
  },

  /**
   * Inject function for for event notification.
   * @param   {Function} fn       the function to be injected
   * @returns {ProcessManagement} to be able to chain...
   */
  onCommand: function (fn) {
    if (!fn || !_.isFunction(fn)) {
      var err = new Error('Please pass a valid function!');
      debug(err);
      throw err;
    }

    if (fn.length === 1) {
      fn = _.wrap(fn, function(func, cmd, callback) {
        func(cmd);
        callback(null);
      });
    }

    this.onCommandHandle = fn;

    return this;
  },

  /**
   * Inject function for event missing handle.
   * @param   {Function} fn       the function to be injected
   * @returns {ProcessManager} to be able to chain...
   */
  onEventMissing: function (fn) {
    if (!fn || !_.isFunction(fn)) {
      var err = new Error('Please pass a valid function!');
      debug(err);
      throw err;
    }

    this.onEventMissingHandle = fn;

    return this;
  },

  /**
   * Call this function to initialize the saga.
   * @param {Function} callback the function that will be called when this action has finished [optional]
   *                            `function(err){}`
   */
  init: function (callback) {

    var self = this;

    var warnings = null;

    async.series([
      // load saga files...
      function (callback) {
        if (self.options.sagaPath === '') {
          self.sagas = {};
          debug('empty sagaPath defined so no sagas will be loaded...');
          return callback(null);
        }
        debug('load saga files...');
        self.structureLoader(self.options.sagaPath, function (err, sagas, warns) {
          if (err) {
            return callback(err);
          }
          warnings = warns;
          self.sagas = attachLookupFunctions(sagas);
          callback(null);
        });
      },

      // prepare infrastructure...
      function (callback) {
        debug('prepare infrastructure...');
        async.parallel([

          // prepare sagaStore...
          function (callback) {
            debug('prepare sagaStore...');

            self.sagaStore.on('connect', function () {
              self.emit('connect');
            });

            self.sagaStore.on('disconnect', function () {
              self.emit('disconnect');
            });

            self.sagaStore.connect(callback);
          },

          // prepare revisionGuard...
          function (callback) {
            debug('prepare revisionGuard...');
            if (!self.revisionGuardStore) {
              return callback(null);
            }

            self.revisionGuardStore.on('connect', function () {
              self.emit('connect');
            });

            self.revisionGuardStore.on('disconnect', function () {
              self.emit('disconnect');
            });

            self.revisionGuardStore.connect(callback);
          }
        ], callback);
      },

      // inject all needed dependencies...
      function (callback) {
        debug('inject all needed dependencies...');

        if (self.revisionGuardStore) {
          self.revisionGuard = new RevisionGuard(self.revisionGuardStore, self.options.revisionGuard);
          self.revisionGuard.onEventMissing(function (info, evt) {
            self.onEventMissingHandle(info, evt);
          });
        }

        if (self.options.sagaPath !== '') {
          self.eventDispatcher = new EventDispatcher(self.sagas, self.definitions.event);
          self.sagas.defineOptions({}) // options???
            .defineCommand(self.definitions.command)
            .defineEvent(self.definitions.event)
            .idGenerator(self.getNewId)
            .useSagaStore(self.sagaStore);
        }

        if (self.revisionGuardStore) {
          self.revisionGuard.defineEvent(self.definitions.event);
        }

        callback(null);
      }
    ], function (err) {
      if (err) {
        debug(err);
      }
      if (callback) { callback(err, warnings); }
    });
  },

  /**
   * Returns the saga information.
   * @returns {Object}
   */
  getInfo: function () {
    if (!this.sagas) {
      var err = new Error('Not initialized!');
      debug(err);
      throw err;
    }

    return this.sagas.getInfo();
  },

  /**
   * Call this function to forward it to the dispatcher.
   * @param {Object}   evt      The event object
   * @param {Function} callback The function that will be called when this action has finished [optional]
   *                            `function(errs, evt, notifications){}` notifications is of type Array
   */
  dispatch: function (evt, callback) {
    var self = this;

    this.eventDispatcher.dispatch(evt, function (errs, sagaModels) {
      var cmds = [];

      if (!sagaModels || sagaModels.length === 0) {
        if (callback) {
          callback(errs, cmds, []);
        }
        return;
      }

      async.each(sagaModels, function (sagaModel, callback) {

        var cmdsToSend = sagaModel.getUndispatchedCommands();

        function setCommandToDispatched (c, clb) {
          debug('set command to dispatched');
          self.setCommandToDispatched(dotty.get(c, self.definitions.command.id), sagaModel.id, function (err) {
            if (err) {
              return clb(err);
            }
            cmds.push(c);
            sagaModel.removeUnsentCommand(c);
            clb(null);
          });
        }

        async.each(cmdsToSend, function (cmd, callback) {

          if (self.onCommandHandle) {
            debug('publish a command');
            self.onCommandHandle(cmd, function (err) {
              if (err) {
                debug(err);
                return callback(err);
              }
              setCommandToDispatched(cmd, callback);
            });
          } else {
            setCommandToDispatched(cmd, callback);
          }

        }, callback);

      }, function (err) {
        if (err) {
          if (!errs) {
            errs = [err];
          } else if (_.isArray(errs)) {
            errs.unshift(err);
          }
          debug(err);
        }
        if (callback) {
          try {
            callback(errs, cmds, sagaModels);
          } catch (e) {
            debug(e);
            console.log(e.stack);
            process.emit('uncaughtException', e);
          }
        }
      });

    });
  },

  /**
   * Call this function to let the saga handle it.
   * @param {Object}   evt      The event object
   * @param {Function} callback The function that will be called when this action has finished [optional]
   *                            `function(err, cmds, sagaModels){}` cmds and sagaModels are of type Array
   */
  handle: function (evt, callback) {
    if (!evt || !_.isObject(evt)) {
      var err = new Error('Please pass a valid event!');
      debug(err);
      throw err;
    }

    var self = this;

    var workWithRevisionGuard = false;
    if (
      this.revisionGuard &&
      !!this.definitions.event.revision && dotty.exists(evt, this.definitions.event.revision) &&
      !!this.definitions.event.aggregateId && dotty.exists(evt, this.definitions.event.aggregateId)
    ) {
      workWithRevisionGuard = true;
    }

    if (dotty.get(evt, this.definitions.event.name) === this.options.commandRejectedEventName) {
      workWithRevisionGuard = false;
    }

    if (!workWithRevisionGuard) {
      return this.dispatch(evt, callback);
    }

    this.revisionGuard.guard(evt, function (err, done) {
      if (err) {
        debug(err);
        if (callback) {
          callback([err]);
        }
        return;
      }

      self.dispatch(evt, function (errs, cmds, sagaModels) {
        if (errs) {
          debug(errs);
          if (callback) {
            callback(errs, cmds, sagaModels);
          }
          return;
        }

        done(function (err) {
          if (err) {
            if (!errs) {
              errs = [err];
            } else if (_.isArray(errs)) {
              errs.unshift(err);
            }
            debug(err);
          }

          if (callback) {
            callback(errs, cmds, sagaModels);
          }
        });
      });

    });

  },

  /**
   * Use this function to get all timeouted sagas.
   * @param  {Function} callback The function, that will be called when this action is completed.
   *                             `function(err, sagas){}` saga is of type Array.
   */
  getTimeoutedSagas: function (options, callback) {
    if (!callback) {
      callback = options;
      options = {};
    }

    var self = this;

    this.sagaStore.getTimeoutedSagas(options, function (err, sagas) {
      if (err) {
        debug(err);
        return callback(err);
      }

      var sagaModels = [];
      sagas.forEach(function (s) {
        var sagaModel = new SagaModel(s.id);
        sagaModel.set(s);
        sagaModel.actionOnCommit = 'update';

        var calledAddCommandToSend = false;
        sagaModel.addCommandToSend = function (cmd) {
          calledAddCommandToSend = true;
          sagaModel.addUnsentCommand(cmd);
        };
        var calledRemoveTimeout = false;
        var orgRemoveTimeout = sagaModel.removeTimeout;
        sagaModel.removeTimeout = function () {
          calledRemoveTimeout = true;
          orgRemoveTimeout.bind(sagaModel)();
        };
        sagaModel.commit = function (clb) {
          var cmds = calledAddCommandToSend ? sagaModel.getUndispatchedCommands() : [];

          function onAfterCommit(err) {
            if (err) return clb(err);

            function setCommandToDispatched (c, cb) {
              debug('set command to dispatched');
              self.setCommandToDispatched(dotty.get(c, self.definitions.command.id), sagaModel.id, function (err) {
                if (err) {
                  return cb(err);
                }
                sagaModel.removeUnsentCommand(c);
                cb(null);
              });
            }

            if (!self.onCommandHandle) return clb(null);

            async.each(sagaModel.getUndispatchedCommands(), function (cmd, callback) {
              debug('publish a command');
              self.onCommandHandle(cmd, function (err) {
                if (err) {
                  debug(err);
                  return callback(err);
                }
                setCommandToDispatched(cmd, callback);
              });
            }, clb);
          }

          async.each(cmds, function (cmd, fn) {
            if (dotty.exists(cmd, self.definitions.command.id)) {
              return fn(null);
            }

            self.getNewId(function (err, id) {
              if (err) {
                debug(err);
                return fn(err);
              }
              dotty.put(cmd, self.definitions.command.id, id);
              fn(null);
            });
          }, function (err) {
            if (err) {
              debug(err);
              return callback(err);
            }

            if (sagaModel.isDestroyed()) {
              self.removeSaga(sagaModel, onAfterCommit);
            } else if (calledAddCommandToSend) {
              sagaModel.setCommitStamp(new Date());
              var undispCmds = _.map(sagaModel.getUndispatchedCommands(), function (c) {
                return { id: dotty.get(c, self.definitions.command.id), payload: c };
              });
              self.sagaStore.save(sagaModel.toJSON(), undispCmds, onAfterCommit);
            } else if (calledRemoveTimeout) {
              sagaModel.setCommitStamp(new Date());
              self.sagaStore.save(sagaModel.toJSON(), [], onAfterCommit);
            } else {
              var err = new Error('Use commit only to remove a saga or to addCommandToSend!');
              debug(err);
              if (clb) { return clb(err); }
              throw err;
            }
          });
        };
        sagaModels.push(sagaModel);
      });

      callback(null, sagaModels);
    });
  },

  /**
   * Use this function to get all sagas that are older then the passed date.
   * @param {Date}     date     The date
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err, sagas){}` saga is of type Array.
   */
  getOlderSagas: function (date, callback) {
    var self = this;

    this.sagaStore.getOlderSagas(date, function (err, sagas) {
      if (err) {
        debug(err);
        return callback(err);
      }
      var sagaModels = [];
      sagas.forEach(function (s) {
        var sagaModel = new SagaModel(s.id);
        sagaModel.set(s);
        sagaModel.actionOnCommit = 'update';
        var calledRemoveTimeout = false;
        var orgRemoveTimeout = sagaModel.removeTimeout;
        sagaModel.removeTimeout = function () {
          calledRemoveTimeout = true;
          orgRemoveTimeout.bind(sagaModel)();
        };
        sagaModel.commit = function (clb) {
          if (sagaModel.isDestroyed()) {
            self.removeSaga(sagaModel, clb);
          } else if (calledRemoveTimeout) {
            sagaModel.setCommitStamp(new Date());
            self.sagaStore.save(sagaModel.toJSON(), [], clb);
          } else {
            var err = new Error('Use commit only to remove a saga!');
            debug(err);
            if (clb) { return clb(err); }
            throw err;
          }
        };
        sagaModels.push(sagaModel);
      });

      callback(null, sagaModels);
    });
  },

  /**
   * Use this function to get all undispatched commands.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err, cmdsSagaMap){}` cmdsSagaMap is of type Array.
   */
  getUndispatchedCommands: function (options, callback) {
    if (!callback) {
      callback = options;
      options = {};
    }
    this.sagaStore.getUndispatchedCommands(options, callback);
  },

  /**
   * Use this function to mark a command as dispatched. (will remove it from the db)
   * @param {String}   cmdId    The command id
   * @param {String}   sagaId   The saga id
   * @param {Function} callback The function, that will be called when this action is completed. [optional]
   *                            `function(err){}`
   */
  setCommandToDispatched: function (cmdId, sagaId, callback) {
    this.sagaStore.setCommandToDispatched(cmdId, sagaId, callback);
  },

  /**
   * Use this function to remove the matched saga.
   * @param {String}   saga     The id of the saga or the saga itself
   * @param {Function} callback The function, that will be called when this action is completed. [optional]
   *                             `function(err){}`
   */
  removeSaga: function (saga, callback) {
    var sagaId = saga.id || saga;
    this.sagaStore.remove(sagaId, callback);
  },

  /**
   * Gets the last event.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err, evt){}` evt is of type Object.
   */
  getLastEvent: function (callback) {
    if (!this.revisionGuardStore)
      return callback(null, null);
    this.revisionGuardStore.getLastEvent(callback);
  }

});

module.exports = ProcessManagement;
```

## File: `lib/revisionGuard.js`
```javascript
var debug = require('debug')('saga:revisionGuard'),
  _ = require('lodash'),
  Queue = require('./orderQueue'),
  ConcurrencyError = require('./errors/concurrencyError'),
  AlreadyHandledError = require('./errors/alreadyHandledError'),
  AlreadyHandlingError = require('./errors/alreadyHandlingError'),
  dotty = require('dotty');

/**
 * RevisionGuard constructor
 * @param {Object} store   The store object.
 * @param {Object} options The options object.
 * @constructor
 */
function RevisionGuard (store, options) {
  options = options || {};

  var defaults = {
    queueTimeout: 1000,
    queueTimeoutMaxLoops: 3//,
    // startRevisionNumber: 1
  };

  _.defaults(options, defaults);

  this.options = options;

  if (!store || !_.isObject(store)) {
    var err = new Error('store not injected!');
    debug(err);
    throw err;
  }

  this.store = store;

  this.definition = {
    correlationId: 'correlationId', // optional
    id: 'id',                       // optional
    name: 'name',                   // optional
//    aggregateId: 'aggregate.id',    // optional
//    context: 'context.name',        // optional
//    aggregate: 'aggregate.name',    // optional
    payload: 'payload'              // optional
//    revision: 'revision'            // optional
//    version: 'version',             // optional
//    meta: 'meta'                    // optional, if defined theses values will be copied to the notification (can be used to transport information like userId, etc..)
  };

  this.queue = new Queue({ queueTimeout: this.options.queueTimeout });

  this.currentHandlingRevisions = {};

  this.onEventMissing(function (info, evt) {
    debug('missing events: ', info, evt);
  });
}

/**
 * Returns a random number between passed values of min and max.
 * @param {Number} min The minimum value of the resulting random number.
 * @param {Number} max The maximum value of the resulting random number.
 * @returns {Number}
 */
function randomBetween(min, max) {
  return Math.round(min + Math.random() * (max - min));
}

RevisionGuard.prototype = {

  /**
   * Inject definition for event structure.
   * @param   {Object} definition the definition to be injected
   */
  defineEvent: function (definition) {
    if (!_.isObject(definition)) {
      throw new Error('Please pass in an object');
    }
    this.definition = _.defaults(definition, this.definition);
    return this;
  },

  /**
   * Inject function for event missing handle.
   * @param   {Function} fn       the function to be injected
   * @returns {RevisionGuard} to be able to chain...
   */
  onEventMissing: function (fn) {
    if (!fn || !_.isFunction(fn)) {
      var err = new Error('Please pass a valid function!');
      debug(err);
      throw err;
    }

    if (fn.length === 1) {
      fn = _.wrap(fn, function(func, info, evt, callback) {
        func(info, evt);
        callback(null);
      });
    }

    this.onEventMissingHandle = fn;

    return this;
  },

  /**
   * Returns the concatenated id (more unique)
   * @param {Object}   evt The passed eventt.
   * @returns {string}
   */
  getConcatenatedId: function (evt) {
    var aggregateId = '';
    if (dotty.exists(evt, this.definition.aggregateId)) {
      aggregateId = dotty.get(evt, this.definition.aggregateId);
    }

    var aggregate = '';
    if (dotty.exists(evt, this.definition.aggregate)) {
      aggregate = dotty.get(evt, this.definition.aggregate);
    }

    var context = '';
    if (dotty.exists(evt, this.definition.context)) {
      context = dotty.get(evt, this.definition.context);
    }

    return context + aggregate + aggregateId;
  },

  /**
   * Queues an event with its callback by aggregateId
   * @param {Object}   evt      The event object.
   * @param {Function} callback The event callback.
   */
  queueEvent: function (evt, callback) {
    var self = this;
    var evtId = dotty.get(evt, this.definition.id);
    var revInEvt = dotty.get(evt, this.definition.revision);
    var aggId = dotty.get(evt, this.definition.aggregateId);

    var concatenatedId = this.getConcatenatedId(evt);

    // just to make sure callback gets not called twice...
    callback = _.once(callback);

    this.queue.push(concatenatedId, evtId, evt, callback, function (loopCount, waitAgain) {
      self.store.get(concatenatedId, function (err, revInStore) {
        if (err) {
          debug(err);
          self.store.remove(concatenatedId, evtId);
          return callback(err);
        }

        if (revInEvt === revInStore) {
          debug('revision match [concatenatedId]=' + concatenatedId + ', [revInStore]=' + revInStore + ', [revInEvt]=' + revInEvt);
          return self.guard(evt, callback);
        }

        if (loopCount < self.options.queueTimeoutMaxLoops) {
          debug('revision mismatch => try/wait again... [concatenatedId]=' + concatenatedId + ', [revInStore]=' + revInStore + ', [revInEvt]=' + revInEvt);
          return waitAgain();
        }

        debug('event timeouted [concatenatedId]=' + concatenatedId + ', [revInStore]=' + revInStore + ', [revInEvt]=' + revInEvt);
        // try to replay depending from id and evt...
        var info = {
          aggregateId: aggId,
          aggregateRevision: !!self.definition.revision ? dotty.get(evt, self.definition.revision) : undefined,
          aggregate: !!self.definition.aggregate ? dotty.get(evt, self.definition.aggregate) : undefined,
          context: !!self.definition.context ? dotty.get(evt, self.definition.context) : undefined,
          guardRevision: revInStore || self.options.startRevisionNumber
        };
        self.onEventMissingHandle(info, evt);
      });
    });
  },

  /**
   * Finishes the guard stuff and save the new revision to store.
   * @param {Object}   evt        The event object.
   * @param {Number}   revInStore The actual revision number in store.
   * @param {Function} callback   The function, that will be called when this action is completed.
   *                              `function(err){}`
   */
  finishGuard: function (evt, revInStore, callback) {
    var evtId = dotty.get(evt, this.definition.id);
    var revInEvt = dotty.get(evt, this.definition.revision);

    var self = this;

    var concatenatedId = this.getConcatenatedId(evt);

    this.store.set(concatenatedId, revInEvt + 1, revInStore, function (err) {
      if (err) {
        debug(err);
        if (err instanceof ConcurrencyError) {
          var retryIn = randomBetween(0, self.options.retryOnConcurrencyTimeout || 800);
          debug('retry in ' + retryIn + 'ms for [concatenatedId]=' + concatenatedId + ', [revInStore]=' + (revInStore || 'null') + ', [revInEvt]=' + revInEvt);
          setTimeout(function() {
            self.guard(evt, callback);
          }, retryIn);
          return;
        }

        return callback(err);
      }

      self.store.saveLastEvent(evt, function (err) {
        if (err) {
          debug('error while saving last event');
          debug(err);
        }
      });

      self.queue.remove(concatenatedId, evtId);
      callback(null);

      var pendingEvents = self.queue.get(concatenatedId);
      if (!pendingEvents || pendingEvents.length === 0) return debug('no other pending event found [concatenatedId]=' + concatenatedId + ', [revInStore]=' + (revInStore || 'null') + ', [revInEvt]=' + revInEvt);

      var nextEvent = _.find(pendingEvents, function (e) {
        var revInNextEvt = dotty.get(e.payload, self.definition.revision);
        return revInNextEvt === revInEvt + 1;
      });

      if (!nextEvent) return debug('no next pending event found [concatenatedId]=' + concatenatedId + ', [revInStore]=' + (revInStore || 'null') + ', [revInEvt]=' + revInEvt);

      debug('found next pending event => guard [concatenatedId]=' + concatenatedId + ', [revInStore]=' + (revInStore || 'null') + ', [revInEvt]=' + revInEvt);
      self.guard(nextEvent.payload, nextEvent.callback);
    });
  },

  /**
   * Guard this event. Check for order and check if missing events...
   * @param {Object} evt The event object.
   * @param {Function} callback The event callback.
   */
  guard: function (evt, callback) {
    if (!this.definition.aggregateId || !dotty.exists(evt, this.definition.aggregateId) ||
        !this.definition.revision || !dotty.exists(evt, this.definition.revision)) {
      var err = new Error('Please define an aggregateId!');
      debug(err);
      return callback(err);
    }

    var self = this;

    var revInEvt = dotty.get(evt, this.definition.revision);

    var concatenatedId = this.getConcatenatedId(evt);

    function proceed (revInStore) {
      if (!revInStore && !self.currentHandlingRevisions[concatenatedId] && (self.options.startRevisionNumber === undefined || self.options.startRevisionNumber === null)) {
        self.currentHandlingRevisions[concatenatedId] = revInEvt;
        debug('first revision to store [concatenatedId]=' + concatenatedId + ', [revInStore]=' + (revInStore || 'null') + ', [revInEvt]=' + revInEvt);
        callback(null, function (clb) {
          self.finishGuard(evt, revInStore, clb);
        });
        return;
      }

      if (revInStore && revInEvt < revInStore) {
        debug('event already handled [concatenatedId]=' + concatenatedId + ', [revInStore]=' + revInStore + ', [revInEvt]=' + revInEvt);
        callback(new AlreadyHandledError('Event: [id]=' + dotty.get(evt, self.definition.id) + ', [revision]=' + revInEvt + ', [concatenatedId]=' + concatenatedId + ' already handled!'), function (clb) {
          clb(null);
        });
        return;
      }

      if (revInStore && revInEvt > revInStore) {
        debug('queue event [concatenatedId]=' + concatenatedId + ', [revInStore]=' + revInStore + ', [revInEvt]=' + revInEvt);
        self.queueEvent(evt, callback);
        return;
      }

      if (!revInStore && self.options.startRevisionNumber >= 0 && revInEvt > self.options.startRevisionNumber) {
        debug('queue event (startRevisionNumber is set) [concatenatedId]=' + concatenatedId + ', [startRevisionNumber]=' + self.options.startRevisionNumber + ', [revInEvt]=' + revInEvt);
        self.queueEvent(evt, callback);
        return;
      }

      if (!revInStore && self.currentHandlingRevisions[concatenatedId] >= 0 && revInEvt > self.currentHandlingRevisions[concatenatedId]) {
        debug('queue event [concatenatedId]=' + concatenatedId + ', [currentlyHandling]=' + self.currentHandlingRevisions[concatenatedId] + ', [revInEvt]=' + revInEvt);
        self.queueEvent(evt, callback);
        return;
      }

      if (self.currentHandlingRevisions[concatenatedId] >= revInEvt) {
        debug('event already handling [concatenatedId]=' + concatenatedId + ', [revInStore]=' + revInStore + ', [revInEvt]=' + revInEvt);
        callback(new AlreadyHandlingError('Event: [id]=' + dotty.get(evt, self.definition.id) + ', [revision]=' + revInEvt + ', [concatenatedId]=' + concatenatedId + ' already handling!'), function (clb) {
          clb(null);
        });
        return;
      }

      self.currentHandlingRevisions[concatenatedId] = revInEvt;

      debug('event is in correct order => go for it! [concatenatedId]=' + concatenatedId + ', [revInStore]=' + revInStore + ', [revInEvt]=' + revInEvt);
      callback(null, function (clb) {
        self.finishGuard(evt, revInStore, clb);
      });
    }

    function retry (max, loop) {
      setTimeout(function () {
        self.store.get(concatenatedId, function(err, revInStore) {
          if (err) {
            debug(err);
            return callback(err);
          }

          if (loop <= 0) {
            debug('finished loops for retry => proceed [concatenatedId]=' + concatenatedId + ', [revInStore]=' + revInStore + ', [revInEvt]=' + revInEvt);
            return proceed(revInStore);
          }

          if (!revInStore && revInEvt !== 1) {
            debug('no revision in store => retry [concatenatedId]=' + concatenatedId + ', [revInStore]=' + revInStore + ', [revInEvt]=' + revInEvt);
            retry(max, --loop);
            return;
          }

          debug('revision in store existing => proceed [concatenatedId]=' + concatenatedId + ', [revInStore]=' + revInStore + ', [revInEvt]=' + revInEvt);
          proceed(revInStore);
        });
      }, randomBetween(max / 5, max));
    }

    process.nextTick(function () {
      self.store.get(concatenatedId, function (err, revInStore) {
        if (err) {
          debug(err);
          return callback(err);
        }

        if (!revInStore && revInEvt !== (self.options.startRevisionNumber || 1) && !self.currentHandlingRevisions[concatenatedId]) {
          var max = (self.options.queueTimeout * self.options.queueTimeoutMaxLoops) / 3;
          max = max < 10 ? 10 : max;
          retry(max, self.options.queueTimeoutMaxLoops);
          return;
        }

        proceed(revInStore);
      });
    });
  }

};

module.exports = RevisionGuard;
```

## File: `lib/sagaModel.js`
```javascript
var debug = require('debug')('saga:sagaModel'),
  dotty = require('dotty'),
  _ = require('lodash'),
  jsondate = require('jsondate');

/**
 * SagaModel constructor
 * @param {String} id The saga id.
 * @constructor
 */
function SagaModel (id) {
  if (!id || !_.isString(id)) {
    var err = new Error('No id injected!');
    debug(err);
    throw err;
  }

  this.attributes = {};

  this.id = id;

  this.destroyed = false;

  this.commandsToSend = [];

  this.actionOnCommit = 'create';
}

SagaModel.prototype = {

  /**
   * Gets the id of this saga.
   * @returns {String}
   */
  get id (){
    return this.attributes.id;
  },

  /**
   * Sets the id for this saga.
   * @param {String} val The saga id
   */
  set id (val){
    this.attributes.id = val;
  },

  /**
   * Defines the commit date.
   * @param {Date} date The commit date.
   */
  setCommitStamp: function (date) {
    this.set('_commitStamp', date);
  },

  /**
   * Returns the commit date.
   * @returns {Date}
   */
  getCommitStamp: function () {
    return this.get('_commitStamp');
  },

  /**
   * Defines a timeout date and optional timeout commands, and adds them to this model.
   * Will be called by the attached function 'defineTimeout'.
   * @param {Date}  date The timeout date.
   * @param {Array} cmds The array of commands.
   */
  addTimeout: function (date, cmds) {
    this.set('_timeoutAt', date);
    this.set('_timeoutCommands', cmds);
  },

  /**
   * Returns the timeout date.
   * @returns {Date}
   */
  getTimeoutAt: function () {
    return this.get('_timeoutAt');
  },

  /**
   * Returns the commands that should be handled when timeouted.
   * @returns {Array}
   */
  getTimeoutCommands: function () {
    return this.get('_timeoutCommands');
  },

  /**
   * Removes the timoutAt and the timeoutCommands values.
   */
  removeTimeout: function () {
    this.set('_timeoutAt', undefined);
    this.set('_timeoutCommands', undefined);
  },

  /**
   * Adds the passed command to this model.
   * Will be called by the attached function 'addCommandToSend'.
   * @param {Object} cmd The command that should be sent.
   */
  addUnsentCommand: function (cmd) {
    this.commandsToSend.push(cmd);
  },

  /**
   * Removes the passed command from this model.
   * @param {Object} cmd The command that should not be sent anymore.
   */
  removeUnsentCommand: function (cmd) {
    this.commandsToSend.splice(this.commandsToSend.indexOf(cmd), 1);
  },

  /**
   * Returns the commands that should be sent.
   * @returns {Array}
   */
  getUndispatchedCommands: function () {
    return [].concat(this.commandsToSend);
  },

  /**
   * Defines a timeout date and optional timeout commands, and adds them to this model.
   * Will be attached by saga handle.
   * @param {Date}  date The timeout date.
   * @param {Array} cmds The array of commands.
   */
  defineTimeout: function (date, cmds) {
    throw new Error('Attach defineTimeout function!!!');
  },

  /**
   * Adds the passed command to this model.
   * Will be attached by saga handle.
   * @param {Object} cmd The command that should be sent.
   */
  addCommandToSend: function (cmd) {
    throw new Error('Attach addCommandToSend function!!!');
  },

  /**
   * Commits the saga data and its commands.
   * Will be attached by saga handle.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err){}`
   */
  commit: function (callback) {
    throw new Error('Attach commit function!!!');
  },

  /**
   * Marks this saga as destroyed.
   */
  destroy: function () {
    this.destroyed = true;
    this.actionOnCommit = 'delete';
  },

  /**
   * Returns true if this saga is destroyed.
   * @returns {boolean}
   */
  isDestroyed: function () {
    return this.destroyed;
  },

  /**
   * The toJSON function will be called when JSON.stringify().
   * @return {Object} A clean Javascript object containing all attributes.
   */
  toJSON: function () {
    return jsondate.parse(JSON.stringify(this.attributes));
  },

  /**
   * Sets attributes for the saga.
   *
   * @example:
   *     saga.set('firstname', 'Jack');
   *     // or
   *     saga.set({
   *          firstname: 'Jack',
   *          lastname: 'X-Man'
   *     });
   */
  set: function (data) {
    if (arguments.length === 2) {
      dotty.put(this.attributes, arguments[0], arguments[1]);
    } else if (_.isObject(data)) {
      for (var m in data) {
        dotty.put(this.attributes, m, data[m]);
      }
    }
  },

  /**
   * Gets an attribute of the vm.
   * @param  {String} attr The attribute name.
   * @return {Object}      The result value.
   *
   * @example:
   *     saga.get('firstname'); // returns 'Jack'
   */
  get: function (attr) {
    return dotty.get(this.attributes, attr);
  },

  /**
   * Returns `true` if the attribute contains a value that is not null
   * or undefined.
   * @param  {String} attr The attribute name.
   * @return {Boolean}     The result value.
   *
   * @example:
   *     saga.has('firstname'); // returns true or false
   */
  has: function (attr) {
    return (this.get(attr) !== null && this.get(attr) !== undefined);
  }

};

module.exports = SagaModel;
```

## File: `lib/definitions/saga.js`
```javascript
var Definition = require('../definitionBase'),
  SagaModel = require('../sagaModel'),
  ConcurrencyError = require('../errors/concurrencyError'),
  util = require('util'),
  _ = require('lodash'),
  dotty = require('dotty'),
  async = require('async'),
  uuid = require('uuid').v4,
  debug = require('debug')('saga:handle');

/**
 * Saga constructor
 * @param {Object}   meta Meta infos like: { name: 'name', version: 1, payload: 'some.path', id: 'some.path', containingProperties: ['some.path'] }
 * @param {Function} fn   Function handle
 *                        `function(evtData, sagaModel, callback){}`
 * @constructor
 */
function Saga (meta, fn) {
  Definition.call(this, meta);

  meta = meta || {};

  if (!fn || !_.isFunction(fn)) {
    var err = new Error('Saga function not injected!');
    debug(err);
    throw err;
  }

  this.aggregate = meta.aggregate || null;
  this.context = meta.context || null;
  this.existing = meta.existing || false;
  this.version = meta.version || 0;
  this.payload = meta.payload || '';
  this.id = meta.id || null;
  this.containingProperties = meta.containingProperties || [];
  this.priority = meta.priority || Infinity;

  this.sagaFn = function (evt, saga, clb) {
    var wrappedCallback = function () {
      try {
        clb.apply(this, _.toArray(arguments));
      } catch (e) {
        debug(e);
        process.emit('uncaughtException', e);
      }
    };

    try {
      fn.call(this, evt, saga, wrappedCallback);
    } catch (e) {
      debug(e);
      process.emit('uncaughtException', e);
    }
  };

  this.idGenerator(function () {
    return uuid().toString();
  });

  this.defineShouldHandle(function (evt, saga) {
    return true;
  });  

  this.defineShouldHandleEvent(function (evt) {
    return true;
  });  
}

util.inherits(Saga, Definition);

/**
 * Returns a random number between passed values of min and max.
 * @param {Number} min The minimum value of the resulting random number.
 * @param {Number} max The maximum value of the resulting random number.
 * @returns {Number}
 */
function randomBetween(min, max) {
  return Math.round(min + Math.random() * (max - min));
}

_.extend(Saga.prototype, {

  /**
   * Inject idGenerator function.
   * @param   {Function}  fn The function to be injected.
   * @returns {Saga}    to be able to chain...
   */
  idGenerator: function (fn) {
    if (fn.length === 0) {
      fn = _.wrap(fn, function(func, callback) {
        callback(null, func());
      });
    }

    this.getNewId = fn;

    return this;
  },

  /**
   * Injects the needed sagaStore.
   * @param {Object} sagaStore The sagaStore object to inject.
   */
  useSagaStore: function (sagaStore) {
    if (!sagaStore || !_.isObject(sagaStore)) {
      var err = new Error('Please pass a valid sagaStore!');
      debug(err);
      throw err;
    }
    this.sagaStore = sagaStore;
  },

  /**
   * Returns the requested payload of the passed command.
   * @param {Object} evt The passed event.
   * @returns {Object}
   */
  getPayload: function (evt) {
    if (!this.payload || this.payload === '') {
      return evt;
    }
    return dotty.get(evt, this.payload);
  },

  /**
   * Checks if the passed commands have a command id. If not it will generate a new one and extend the command with it.
   * @param {Array}    cmds     The passed commands array.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err){}`
   */
  checkForId: function (cmds, callback) {
    if (!cmds || cmds.length === 0) {
      return callback(null);
    }

    var self = this;
    async.each(cmds, function (cmd, fn) {
      if (dotty.exists(cmd, self.definitions.command.id)) {
        return fn(null);
      }

      self.getNewId(function (err, id) {
        if (err) {
          debug(err);
          return fn(err);
        }
        dotty.put(cmd, self.definitions.command.id, id);
        fn(null);
      });
    }, callback);
  },

  /**
   * Returns true if the passed event contains all requested properties.
   * @param {Object} evt The passed event.
   * @returns {boolean}
   */
  doesContainProperties: function (evt) {
    for (var i = 0, len = this.containingProperties.length; i < len; i++) {
      var prop = this.containingProperties[i];
      if (!dotty.exists(evt, prop)) {
        return false;
      }
    }
    return true;
  },

  /**
   * Handles the passed event.
   * @param {Object}   evt      The passed event.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err, sagaModel){}`
   */
  handle: function (evt, callback) {

    if (!this.doesContainProperties(evt)) {
      debug('does not match the containing properties check');
      return callback(null, null);
    }

    var self = this;

    //        self.shouldHandle(evt, sagaModel, function (err, doHandle) {
    this.shouldHandleEvent(evt, function (err, doHandle) {
      if (err) {
        return callback(err);
      }

      if (!doHandle) {
        return callback(null, null);
      }

      function retry (retryIn) {
        if (_.isNumber(retryIn)) {
          retryIn = randomBetween(0, retryIn);
        }

        if (_.isObject(retryIn) && _.isNumber(retryIn.from) && _.isNumber(retryIn.to)) {
          retryIn = randomBetween(retryIn.from, retryIn.to);
        }

        if (!_.isNumber(retryIn) || retryIn === 0) {
          retryIn = randomBetween(0, self.options ? self.options.retryOnConcurrencyTimeout : 800);
        }

        debug('retry in ' + retryIn + 'ms');
        setTimeout(function() {
          self.handle(evt, callback);
        }, retryIn);
      }

      async.waterfall([

        function (callb) {
          if (!self.id || !dotty.exists(evt, self.id)) {
            debug('has no id, generate new one');

            if (!self.getNewIdForThisSaga) {
              return self.sagaStore.getNewId(callb);
            }

            self.getNewIdForThisSaga(evt, callb);
          } else {
            debug('already has an id');
            callb(null, dotty.get(evt, self.id));
          }
        },

        function (id, callb) {
          self.sagaStore.get(id, function (err, data) {
            if (err) {
              return callb(err);
            }

            if (!data && self.existing) {
              debug('this saga only wants to be executed, if already existing');
              return callback(null, null);
            }

            var sagaModel = new SagaModel(id);
            if (data) {
              sagaModel.set(data);
              sagaModel.actionOnCommit = 'update';
            }
            callb(null, sagaModel);
          });
        },

        function (sagaModel, callb) {

          // attach commit function
          debug('attach commit function');

          /**
           * Commits the saga data and its commands.
           * @param {Function} clb The function, that will be called when this action is completed.
           *                       `function(err){}`
           */
          sagaModel.commit = function (clb) {
            async.parallel([
              function (callback) {
                self.checkForId(sagaModel.getUndispatchedCommands(), callback);
              },
              function (callback) {
                self.checkForId(sagaModel.getTimeoutCommands(), callback);
              }
            ], function (err) {
              if (err) {
                debug(err);
                return callback(err);
              }
              if (sagaModel.isDestroyed()) {
                self.sagaStore.remove(sagaModel.id, clb);
              } else {
                sagaModel.setCommitStamp(new Date());

                var undispCmds = _.map(sagaModel.getUndispatchedCommands(), function (c) {
                  return { id: dotty.get(c, self.definitions.command.id), payload: c };
                });

                self.sagaStore.save(sagaModel.toJSON(), undispCmds, function (err) {
                  if (err instanceof ConcurrencyError) {
                    retry(clb);
                    return;
                  }
                  clb(err);
                });
              }
            });
          };

          // attach addCommandToSend function
          debug('attach addCommandToSend function');
          /**
           * Adds the passed command to this model.
           * @param {Object} cmd The command that should be sent.
           */
          sagaModel.addCommandToSend = function (cmd) {
            if (!dotty.exists(cmd, self.definitions.command.meta) && dotty.exists(evt, self.definitions.event.meta) &&
              !!self.definitions.command.meta && !!self.definitions.event.meta) {
              dotty.put(cmd, self.definitions.command.meta, dotty.get(evt, self.definitions.event.meta));
            }

            sagaModel.addUnsentCommand(cmd);
          };

          // attach defineTimeout function
          debug('attach defineTimeout function');
          /**
           * Defines a timeout date and optional timeout commands, and adds them to this model.
           * @param {Date}  date The timeout date.
           * @param {Array} cmds The array of commands.
           */
          sagaModel.defineTimeout = function (date, cmds) {
            cmds = cmds || [];
            if (!_.isArray(cmds)) {
              cmds = [cmds];
            }

            cmds.forEach(function (cmd) {
              if (!dotty.exists(cmd, self.definitions.command.meta) && dotty.exists(evt, self.definitions.event.meta) &&
                !!self.definitions.command.meta && !!self.definitions.event.meta) {
                dotty.put(cmd, self.definitions.command.meta, dotty.get(evt, self.definitions.event.meta));
              }
            });

            sagaModel.addTimeout(date, cmds);
          };

          callb(null, sagaModel);
        },

        function (sagaModel, callb) {
          var sagaThis = {
            retry: function () {
              if (arguments.length === 0) {
                return retry();
              }

              return retry(arguments[0]);
            }
          };

          self.shouldHandle(evt, sagaModel, function (err, doHandle) {
            if (err) {
              return callb(err);
            }

            if (!doHandle) {
              return callb(null, sagaModel);
            }

            self.sagaFn.call(sagaThis, self.getPayload(evt), sagaModel, function (err) {
              if (err) {
                return callb(err);
              }
              callb(null, sagaModel);
            });
          });
        },

        function (sagaModel, callb) {
          // detach commit function
          debug('detach commit function');
          if (sagaModel.commit) {
            delete sagaModel.commit;
          }

          // detach addCommandToSend function
          debug('detach addCommandToSend function');
          if (sagaModel.addCommandToSend) {
            delete sagaModel.addCommandToSend;
          }

          // detach defineTimeout function
          debug('detach defineTimeout function');
          if (sagaModel.defineTimeout) {
            delete sagaModel.defineTimeout;
          }
          callb(null, sagaModel);
        }

      ], callback);
    });
  },

  /**
   * Inject idGenerator function if no id found.
   * @param   {Function}  fn      The function to be injected.
   * @returns {Saga} to be able to chain...
   */
  useAsId: function (fn) {
    if (!fn || !_.isFunction(fn)) {
      var err = new Error('Please pass a valid function!');
      debug(err);
      throw err;
    }

    if (fn.length === 2) {
      this.getNewIdForThisSaga = fn;
      return this;
    }

    this.getNewIdForThisSaga = function (evt, callback) {
      callback(null, fn(evt));
    };

    return this;
  },

  /**
   * Inject shouldHandle function.
   * @param   {Function}  fn      The function to be injected.
   * @returns {Saga} to be able to chain...
   */
  defineShouldHandle: function (fn) {
    if (!fn || !_.isFunction(fn)) {
      var err = new Error('Please pass a valid function!');
      debug(err);
      throw err;
    }

    if (fn.length === 3) {
      this.shouldHandle = fn;
      return this;
    }

    this.shouldHandle = function (evt, saga, callback) {
      callback(null, fn(evt, saga));
    };

    var unwrappedShouldHandle = this.shouldHandle;

    this.shouldHandle = function (evt, saga, clb) {
      var wrappedCallback = function () {
        try {
          clb.apply(this, _.toArray(arguments));
        } catch (e) {
          debug(e);
          process.emit('uncaughtException', e);
        }
      };

      try {
        unwrappedShouldHandle.call(this, evt, saga, wrappedCallback);
      } catch (e) {
        debug(e);
        process.emit('uncaughtException', e);
      }
    };

    return this;
  },

  /**
   * Inject shouldHandleEvent function.
   * @param   {Function}  fn      The function to be injected.
   * @returns {Saga} to be able to chain...
   */
  defineShouldHandleEvent: function (fn) {
    if (!fn || !_.isFunction(fn)) {
      var err = new Error('Please pass a valid function!');
      debug(err);
      throw err;
    }

    if (fn.length === 2) {
      this.shouldHandleEvent = fn;
      return this;
    }

    this.shouldHandleEvent = function (evt, callback) {
      callback(null, fn(evt));
    };

    var unwrappedShouldHandleEvent = this.shouldHandleEvent;

    this.shouldHandleEvent = function (evt, clb) {
      var wrappedCallback = function () {
        try {
          clb.apply(this, _.toArray(arguments));
        } catch (e) {
          debug(e);
          process.emit('uncaughtException', e);
        }
      };

      try {
        unwrappedShouldHandleEvent.call(this, evt, wrappedCallback);
      } catch (e) {
        debug(e);
        process.emit('uncaughtException', e);
      }
    };

    return this;
  }

});

module.exports = Saga;
```

## File: `lib/errors/alreadyHandledError.js`
```javascript
// Grab the util module that's bundled with Node
var util = require('util');

// Create a new custom Error constructor
function AlreadyHandledError(msg) {
  // Pass the constructor to V8's
  // captureStackTrace to clean up the output
  Error.captureStackTrace(this, AlreadyHandledError);

  // If defined, store a custom error message
  if (msg) {
    this.message = msg;
  }
}

// Extend our custom Error from Error
util.inherits(AlreadyHandledError, Error);

// Give our custom error a name property. Helpful for logging the error later.
AlreadyHandledError.prototype.name = AlreadyHandledError.name;

module.exports = AlreadyHandledError;
```

## File: `lib/errors/alreadyHandlingError.js`
```javascript
// Grab the util module that's bundled with Node
var util = require('util');

// Create a new custom Error constructor
function AlreadyHandlingError(msg) {
    // Pass the constructor to V8's
    // captureStackTrace to clean up the output
    Error.captureStackTrace(this, AlreadyHandlingError);

    // If defined, store a custom error message
    if (msg) {
        this.message = msg;
    }
}

// Extend our custom Error from Error
util.inherits(AlreadyHandlingError, Error);

// Give our custom error a name property. Helpful for logging the error later.
AlreadyHandlingError.prototype.name = AlreadyHandlingError.name;

module.exports = AlreadyHandlingError;
```

## File: `lib/errors/concurrencyError.js`
```javascript
// Grab the util module that's bundled with Node
var util = require('util');

// Create a new custom Error constructor
function ConcurrencyError(msg) {
  // Pass the constructor to V8's
  // captureStackTrace to clean up the output
  Error.captureStackTrace(this, ConcurrencyError);

  // If defined, store a custom error message
  if (msg) {
    this.message = msg;
  }
}

// Extend our custom Error from Error
util.inherits(ConcurrencyError, Error);

// Give our custom error a name property. Helpful for logging the error later.
ConcurrencyError.prototype.name = ConcurrencyError.name;

module.exports = ConcurrencyError;
```

## File: `lib/revisionGuardStore/base.js`
```javascript
var util = require('util'),
  EventEmitter = require('events').EventEmitter,
  prequire = require('parent-require'),
  _ = require('lodash'),
  uuid = require('uuid').v4;

/**
 * Guard constructor
 * @param {Object} options The options can have information like host, port, etc. [optional]
 */
function Guard(options) {
  options = options || {};

  EventEmitter.call(this);
}

util.inherits(Guard, EventEmitter);

function implementError (callback) {
  var err = new Error('Please implement this function!');
  if (callback) callback(err);
  throw err;
}

_.extend(Guard.prototype, {

  /**
   * Initiate communication with the lock.
   * @param  {Function} callback The function, that will be called when this action is completed. [optional]
   *                             `function(err, queue){}`
   */
  connect: implementError,

  /**
   * Terminate communication with the lock.
   * @param  {Function} callback The function, that will be called when this action is completed. [optional]
   *                             `function(err){}`
   */
  disconnect: implementError,

  /**
   * Use this function to obtain a new id.
   * @param  {Function} callback The function, that will be called when this action is completed.
   *                             `function(err, id){}` id is of type String.
   */
  getNewId: function (callback) {
    var id = uuid().toString();
    if (callback) callback(null, id);
  },

  /**
   * Use this function to obtain the revision by id.
   * @param {String}   id       The aggregate id.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                             `function(err, revision){}` id is of type String.
   */
  get: function (id, callback) {
    implementError(callback);
  },

  /**
   * Updates the revision number.
   * @param {String}   id          The aggregate id.
   * @param {Number}   revision    The new revision number.
   * @param {Number}   oldRevision The old revision number.
   * @param {Function} callback    The function, that will be called when this action is completed.
   *                               `function(err, revision){}` id is of type String.
   */
  set: function (id, revision, oldRevision, callback) {
    implementError(callback);
  },

  /**
   * Saves the last event.
   * @param {Object}   evt      The event that should be saved.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err){}`
   */
  saveLastEvent: function (evt, callback) {
    implementError(callback);
  },

  /**
   * Gets the last event.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err, evt){}` evt is of type Object.
   */
  getLastEvent: function (callback) {
    implementError(callback);
  },

  /**
   * NEVER USE THIS FUNCTION!!! ONLY FOR TESTS!
   * clears the complete store...
   * @param {Function} callback the function that will be called when this action has finished [optional]
   */
  clear: function (callback) {
    implementError(callback);
  }

});

Guard.use = function (toRequire) {
  var required;
  try {
    required = require(toRequire);
  } catch (e) {
    // workaround when `npm link`'ed for development
    required = prequire(toRequire);
  }
  return required;
};

module.exports = Guard;
```

## File: `lib/revisionGuardStore/index.js`
```javascript
var tolerate = require('tolerance'),
  _ = require('lodash'),
  Base = require('./base');

function exists(toCheck) {
  var _exists = require('fs').existsSync || require('path').existsSync;
  if (require('fs').accessSync) {
    _exists = function (toCheck) {
      try {
        require('fs').accessSync(toCheck);
        return true;
      } catch (e) {
        return false;
      }
    };
  }
  return _exists(toCheck);
}

function getSpecificDbImplementation(options) {
  options = options || {};

  options.type = options.type || 'inmemory';

  if (_.isFunction(options.type)) {
    return options.type;
  }

  options.type = options.type.toLowerCase();

  var dbPath = __dirname + "/databases/" + options.type + ".js";

  if (!exists(dbPath)) {
    var errMsg = 'Implementation for db "' + options.type + '" does not exist!';
    console.log(errMsg);
    throw new Error(errMsg);
  }

  try {
    var db = require(dbPath);
    return db;
  } catch (err) {

    if (err.message.indexOf('Cannot find module') >= 0 &&
      err.message.indexOf("'") > 0 &&
      err.message.lastIndexOf("'") !== err.message.indexOf("'")) {

      var moduleName = err.message.substring(err.message.indexOf("'") + 1, err.message.lastIndexOf("'"));
      console.log('Please install module "' + moduleName +
        '" to work with db implementation "' + options.type + '"!');
    }

    throw err;
  }
}

module.exports = {
  Store: Base,

  create: function(options, callback) {
    if (typeof options === 'function') {
      callback = options;
      options = {};
    }

    options = options || {};

    var Store;

    try {
      Store = getSpecificDbImplementation(options);
    } catch (err) {
      if (callback) callback(err);
      throw err;
    }

    var store = new Store(options);
    if (callback) {
      process.nextTick(function () {
        tolerate(function (callback) {
          store.connect(callback);
        }, options.timeout || 0, callback || function () {
        });
      });
    }
    return store;
  }
};
```

## File: `lib/revisionGuardStore/databases/azureTable.js`
```javascript
var util = require('util'),
  Store = require('../base'),
  debug = require('debug')('saga:azuretable'),
  ConcurrencyError = require('../../errors/concurrencyError'),
  _ = require('lodash'),
  async = Store.use('async'),
  azure = Store.use('azure-storage'),
  eg = azure.TableUtilities.entityGenerator,
  jsondate = require('jsondate');

function AzureTable(options) {

  var azureConf = {
    storageAccount: 'nodecqrs',
    storageAccessKey: 'StXScH574p1krnkjbxjkHkMkrtbIMQpYMbH1D1uYVqS4ny/DpXVkL4ld02xeKupCQnIIN+v0KVmdLLSVA/cxTQ==',
    storageTableHost: 'https://nodecqrs.table.core.windows.net/'
  };

  this.options = _.defaults(options, azureConf);

  var defaults = {
    revisionTableName: 'saga'
  };

  this.options = _.defaults(this.options, defaults);
}

util.inherits(AzureTable, Store);

_.extend(AzureTable.prototype, {

  connect: function (callback) {
    var self = this;
    var retryOperations = new azure.ExponentialRetryPolicyFilter();

    this.client = azure.createTableService(this.options.storageAccount, this.options.storageAccessKey, this.options.storageTableHost).withFilter(retryOperations);

    this.client.createTableIfNotExists(this.options.revisionTableName, function (err) {
      if (err) {
        if (callback) callback(err);
      } else {
        self.emit('connect');
        if (callback) callback(null, self);
      }
    });

  },

  disconnect: function (callback) {
    this.emit('disconnect');
    if (callback) callback(null);
  },

  get: function (id, callback) {

    if (!id || !_.isString(id)) {
      var err = new Error('Please pass a valid id!');
      debug(err);
      return callback(err);
    }

    this.client.retrieveEntity(this.options.revisionTableName,
      id,
      id,
      function (err, revision) {
        if (err && err.code != 'ResourceNotFound') {
          if (callback) return callback(err);
        }

        if (!revision) {
          return callback(null, null);
        }

        callback(null, revision.revision._);
      }
    );
  },

  set: function (id, revision, oldRevision, callback) {

    var self = this;

    if (!id || !_.isString(id)) {
      var err = new Error('Please pass a valid id!');
      debug(err);
      return callback(err);
    }

    if (!revision || !_.isNumber(revision)) {
      var err = new Error('Please pass a valid revision!');
      debug(err);
      return callback(err);
    }

    this.client.retrieveEntity(this.options.revisionTableName,
      id,
      id,
      null,
      function (err, rev) {
        if (err && err.code != 'ResourceNotFound') {
          if (callback) return callback(err);
        }

        if (rev && rev.revision._ != oldRevision) {
          return callback(new ConcurrencyError());
        }

        self.client.insertOrReplaceEntity(self.options.revisionTableName, {
          PartitionKey: eg.String(id),
          RowKey: eg.String(id),
          revision: eg.Int64(revision)
        }, function(err){
          callback(err);
        })
      }
    );
  },

  clear: function (callback) {

    var self = this;
    var query = new azure.TableQuery();

    this.client.queryEntities(self.options.revisionTableName, query, null, function (err, entities) {
        if (!err) {
          async.each(entities.entries, function (entity, callback) {
              self.client.deleteEntity(self.options.revisionTableName, entity, function (error, response) {
                callback(error);
              });
            },
            function (error) {
              if (callback) callback(error);
            });
        }
      }
    );
  }

});

module.exports = AzureTable;
```

## File: `lib/revisionGuardStore/databases/inmemory.js`
```javascript
var util = require('util'),
    Store = require('../base'),
    debug = require('debug')('saga:revisionGuardStore:inmemory'),
    ConcurrencyError = require('../../errors/concurrencyError'),
    _ = require('lodash');

function InMemory(options) {
  Store.call(this, options);
  this.store = {};
  this.lastEvent = null;
}

util.inherits(InMemory, Store);

_.extend(InMemory.prototype, {

  connect: function (callback) {
    this.emit('connect');
    if (callback) callback(null, this);
  },

  disconnect: function (callback) {
    this.emit('disconnect');
    if (callback) callback(null);
  },

  get: function (id, callback) {
    if (!id || !_.isString(id)) {
      var err = new Error('Please pass a valid id!');
      debug(err);
      return callback(err);
    }

    callback(null, this.store[id] || null);
  },

  set: function (id, revision, oldRevision, callback) {
    if (!id || !_.isString(id)) {
      var err = new Error('Please pass a valid id!');
      debug(err);
      return callback(err);
    }
    if (!revision || !_.isNumber(revision)) {
      var err = new Error('Please pass a valid revision!');
      debug(err);
      return callback(err);
    }

    if (this.store[id] && this.store[id] !== oldRevision) {
      return callback(new ConcurrencyError());
    }

    this.store[id] = revision;

    callback(null);
  },

  saveLastEvent: function (evt, callback) {
    this.lastEvent = evt;
    if (callback) callback(null);
  },

  getLastEvent: function (callback) {
    callback(null, this.lastEvent);
  },

  clear: function (callback) {
    this.store = {};
    this.lastEvent = null;
    if (callback) callback(null);
  }

});

module.exports = InMemory;
```

## File: `lib/revisionGuardStore/databases/mongodb.js`
```javascript
var util = require('util'),
    Store = require('../base'),
    _ = require('lodash'),
    debug = require('debug')('saga:revisionGuardStore:mongodb'),
    ConcurrencyError = require('../../errors/concurrencyError'),
    mongo = Store.use('mongodb'),
    mongoVersion = Store.use('mongodb/package.json').version,
    isNew = mongoVersion.indexOf('1.') !== 0,
    ObjectID = isNew ? mongo.ObjectID : mongo.BSONPure.ObjectID;

function Mongo(options) {
  Store.call(this, options);

  var defaults = {
    host: 'localhost',
    port: 27017,
    dbName: 'readmodel',
    collectionName: 'revision'//,
    // heartbeat: 60 * 1000
  };

  _.defaults(options, defaults);

  var defaultOpt = {
    ssl: false
  };

  options.options = options.options || {};

  if (isNew) {
    defaultOpt.autoReconnect = false;
    defaultOpt.useNewUrlParser = true;
    defaultOpt.useUnifiedTopology = true;
    _.defaults(options.options, defaultOpt);
  } else {
    defaultOpt.auto_reconnect = false;
    _.defaults(options.options, defaultOpt);
  }

  this.options = options;
}

util.inherits(Mongo, Store);

_.extend(Mongo.prototype, {

  connect: function (callback) {
    var self = this;

    var options = this.options;

    var connectionUrl;

    if (options.url) {
      connectionUrl = options.url;
    } else {
      var members = options.servers
        ? options.servers
        : [{host: options.host, port: options.port}];

      var memberString = _(members).map(function(m) { return m.host + ':' + m.port; });
      var authString = options.username && options.password
        ? options.username + ':' + options.password + '@'
        : '';
      var optionsString = options.authSource
        ? '?authSource=' + options.authSource
        : '';

      connectionUrl = 'mongodb://' + authString + memberString + '/' + options.dbName + optionsString;
    }

    var client;

    if (mongo.MongoClient.length === 2) {
      client = new mongo.MongoClient(connectionUrl, options.options);
      client.connect(function(err, cl) {
        if (err) {
          debug(err);
          if (callback) callback(err);
          return;
        }

        self.db = cl.db(cl.s.options.dbName);
        if (!self.db.close) {
          self.db.close = cl.close.bind(cl);
        }
        initDb();
      });
    } else {
      client = new mongo.MongoClient();
      client.connect(connectionUrl, options.options, function(err, db) {
        if (err) {
          debug(err);
          if (callback) callback(err);
          return;
        }

        self.db = db;
        initDb();
      });
    }

    function initDb() {
      self.db.on('close', function() {
        self.emit('disconnect');
        self.stopHeartbeat();
      });

      var finish = function (err) {
        self.store = self.db.collection(options.collectionName);
//        self.store.ensureIndex({ 'aggregateId': 1, date: 1 }, function() {});
        if (!err) {
          self.emit('connect');

          if (self.options.heartbeat) {
            self.startHeartbeat();
          }
        }
        if (callback) callback(err, self);
      };

      finish();
    }
  },

  stopHeartbeat: function () {
    if (this.heartbeatInterval) {
      clearInterval(this.heartbeatInterval);
      delete this.heartbeatInterval;
    }
  },

  startHeartbeat: function () {
    var self = this;

    var gracePeriod = Math.round(this.options.heartbeat / 2);
    this.heartbeatInterval = setInterval(function () {
      var graceTimer = setTimeout(function () {
        if (self.heartbeatInterval) {
          console.error((new Error ('Heartbeat timeouted after ' + gracePeriod + 'ms (mongodb)')).stack);
          self.disconnect();
        }
      }, gracePeriod);

      self.db.command({ ping: 1 }, function (err) {
        if (graceTimer) clearTimeout(graceTimer);
        if (err) {
          console.error(err.stack || err);
          self.disconnect();
        }
      });
    }, this.options.heartbeat);
  },

  disconnect: function (callback) {
    this.stopHeartbeat();

    if (!this.db) {
      if (callback) callback(null);
      return;
    }

    this.db.close(callback || function () {});
  },

  getNewId: function(callback) {
    callback(null, new ObjectID().toString());
  },

  get: function (id, callback) {
    if (!id || !_.isString(id)) {
      var err = new Error('Please pass a valid id!');
      debug(err);
      return callback(err);
    }

    this.store.findOne({ _id: id }, function (err, entry) {
      if (err) {
        return callback(err);
      }

      if (!entry) {
        return callback(null, null);
      }

      callback(null, entry.revision || null);
    });
  },

  set: function (id, revision, oldRevision, callback) {
    if (!id || !_.isString(id)) {
      var err = new Error('Please pass a valid id!');
      debug(err);
      return callback(err);
    }
    if (!revision || !_.isNumber(revision)) {
      var err = new Error('Please pass a valid revision!');
      debug(err);
      return callback(err);
    }

    this.store.update({ _id: id, revision: oldRevision }, { _id: id, revision: revision }, { safe: true, upsert: true }, function (err, modifiedCount) {
      if (isNew) {
        if (modifiedCount && modifiedCount.result && modifiedCount.result.n === 0) {
          err = new ConcurrencyError();
          debug(err);
          if (callback) {
            callback(err);
          }
          return;
        }
      } else {
        if (modifiedCount === 0) {
          err = new ConcurrencyError();
          debug(err);
          if (callback) {
            callback(err);
          }
          return;
        }
      }
      if (err && err.message && err.message.match(/duplicate key/i)) {
        debug(err);
        err = new ConcurrencyError();
        debug(err);
        if (callback) {
          callback(err);
        }
        return;
      }
      if (callback) { callback(err); }
    });
  },

  saveLastEvent: function (evt, callback) {
    this.store.save({ _id: 'THE_LAST_SEEN_EVENT', event: evt }, { safe: true }, function (err) {
      if (callback) { callback(err); }
    });
  },

  getLastEvent: function (callback) {
    this.store.findOne({ _id: 'THE_LAST_SEEN_EVENT' }, function (err, entry) {
      if (err) {
        return callback(err);
      }

      if (!entry) {
        return callback(null, null);
      }

      callback(null, entry.event || null);
    });
  },

  clear: function (callback) {
    this.store.remove({}, { safe: true }, callback);
  }

});

module.exports = Mongo;
```

## File: `lib/revisionGuardStore/databases/redis.js`
```javascript
var util = require('util'),
    Store = require('../base'),
    _ = require('lodash'),
    debug = require('debug')('saga:revisionGuardStore:redis'),
    ConcurrencyError = require('../../errors/concurrencyError'),
    jsondate = require('jsondate'),
    async = require('async'),
    redis = Store.use('redis');

function Redis(options) {
  Store.call(this, options);

  var defaults = {
    host: 'localhost',
    port: 6379,
    prefix: 'readmodel_revision',
    retry_strategy: function (options) {
      return undefined;
    }//,
    // heartbeat: 60 * 1000
  };

  _.defaults(options, defaults);

  if (options.url) {
    var url = require('url').parse(options.url);
    if (url.protocol === 'redis:') {
      if (url.auth) {
        var userparts = url.auth.split(':');
        options.user = userparts[0];
        if (userparts.length === 2) {
          options.password = userparts[1];
        }
      }
      options.host = url.hostname;
      options.port = url.port;
      if (url.pathname) {
        options.db = url.pathname.replace('/', '', 1);
      }
    }
  }

  this.options = options;
}

util.inherits(Redis, Store);

_.extend(Redis.prototype, {

  connect: function (callback) {
    var self = this;

    var options = this.options;

    this.client = new redis.createClient(options.port || options.socket, options.host, _.omit(options, 'prefix'));

    this.prefix = options.prefix;

    var calledBack = false;

    if (options.password) {
      this.client.auth(options.password, function(err) {
        if (err && !calledBack && callback) {
          calledBack = true;
          if (callback) callback(err, self);
          return;
        }
        if (err) throw err;
      });
    }

    if (options.db) {
      this.client.select(options.db);
    }

    this.client.on('end', function () {
      self.disconnect();
      self.stopHeartbeat();
    });

    this.client.on('error', function (err) {
      console.log(err);

      if (calledBack) return;
      calledBack = true;
      if (callback) callback(null, self);
    });

    this.client.on('connect', function () {
      if (options.db) {
        self.client.send_anyways = true;
        self.client.select(options.db);
        self.client.send_anyways = false;
      }

      self.emit('connect');

      if (self.options.heartbeat) {
        self.startHeartbeat();
      }

      if (calledBack) return;
      calledBack = true;
      if (callback) callback(null, self);
    });
  },

  stopHeartbeat: function () {
    if (this.heartbeatInterval) {
      clearInterval(this.heartbeatInterval);
      delete this.heartbeatInterval;
    }
  },

  startHeartbeat: function () {
    var self = this;

    var gracePeriod = Math.round(this.options.heartbeat / 2);
    this.heartbeatInterval = setInterval(function () {
      var graceTimer = setTimeout(function () {
        if (self.heartbeatInterval) {
          console.error((new Error ('Heartbeat timeouted after ' + gracePeriod + 'ms (redis)')).stack);
          self.disconnect();
        }
      }, gracePeriod);

      self.client.ping(function (err) {
        if (graceTimer) clearTimeout(graceTimer);
        if (err) {
          console.error(err.stack || err);
          self.disconnect();
        }
      });
    }, this.options.heartbeat);
  },

  disconnect: function (callback) {
    this.stopHeartbeat();

    if (this.client) {
      this.client.end(true);
    }
    this.emit('disconnect');
    if (callback) callback(null, this);
  },

  getNewId: function(callback) {
    this.client.incr('nextItemId:' + this.prefix, function(err, id) {
      if (err) {
        return callback(err);
      }
      callback(null, id.toString());
    });
  },

  get: function (id, callback) {
    if (!id || !_.isString(id)) {
      var err = new Error('Please pass a valid id!');
      debug(err);
      return callback(err);
    }

    this.client.get(this.options.prefix + ':' + id, function (err, entry) {
      if (err) {
        return callback(err);
      }

      if (!entry) {
        return callback(null, null);
      }

      try {
        entry = jsondate.parse(entry.toString());
      } catch (error) {
        if (callback) callback(error);
        return;
      }

      callback(null, entry.revision || null);
    });
  },

  set: function (id, revision, oldRevision, callback) {
    if (!id || !_.isString(id)) {
      var err = new Error('Please pass a valid id!');
      debug(err);
      return callback(err);
    }
    if (!revision || !_.isNumber(revision)) {
      var err = new Error('Please pass a valid revision!');
      debug(err);
      return callback(err);
    }

    var key = this.options.prefix + ':' + id;

    var self = this;

    this.client.watch(key, function (err) {
      if (err) {
        return callback(err);
      }

      self.get(id, function (err, rev) {
        if (err) {
          debug(err);
          if (callback) callback(err);
          return;
        }

        if (rev && rev !== oldRevision) {
          self.client.unwatch(function (err) {
            if (err) {
              debug(err);
            }

            err = new ConcurrencyError();
            debug(err);
            if (callback) {
              callback(err);
            }
          });
          return;
        }

        self.client.multi([['set'].concat([key, JSON.stringify({ revision: revision })])]).exec(function (err, replies) {
          if (err) {
            debug(err);
            if (callback) {
              callback(err);
            }
            return;
          }
          if (!replies || replies.length === 0 || _.find(replies, function (r) {
                return (r !== 'OK' && r !== 1);
              })) {
            var err = new ConcurrencyError();
            debug(err);
            if (callback) {
              callback(err);
            }
            return;
          }
          if (callback) {
            callback(null);
          }
        });
      });
    });
  },

  saveLastEvent: function (evt, callback) {
    var key = this.options.prefix + ':THE_LAST_SEEN_EVENT';

    this.client.set(key, JSON.stringify({ event: evt }), function (err) {
      if (callback) { callback(err); }
    });
  },

  getLastEvent: function (callback) {
    this.client.get(this.options.prefix + ':THE_LAST_SEEN_EVENT', function (err, entry) {
      if (err) {
        return callback(err);
      }

      if (!entry) {
        return callback(null, null);
      }

      try {
        entry = jsondate.parse(entry.toString());
      } catch (error) {
        if (callback) callback(error);
        return;
      }

      callback(null, entry.event || null);
    });
  },

  clear: function (callback) {
    var self = this;
    async.parallel([
      function (callback) {
        self.client.del('nextItemId:' + self.options.prefix, callback);
      },
      function (callback) {
        self.client.keys(self.options.prefix + ':*', function(err, keys) {
          if (err) {
            return callback(err);
          }
          async.each(keys, function (key, callback) {
            self.client.del(key, callback);
          }, callback);
        });
      }
    ], function (err) {
      if (err) {
        debug(err);
      }
      if (callback) callback(err);
    });
  }

});

module.exports = Redis;
```

## File: `lib/revisionGuardStore/databases/tingodb.js`
```javascript
var util = require('util'),
    Store = require('../base'),
    _ = require('lodash'),
    debug = require('debug')('saga:revisionGuardStore:tingodb'),
    ConcurrencyError = require('../../errors/concurrencyError'),
    tingodb = Store.use('tingodb')(),
    ObjectID = tingodb.ObjectID;

function Tingo(options) {
  Store.call(this, options);

  var defaults = {
    dbPath: require('path').join(__dirname, '/../../../'),
    collectionName: 'revision'
  };

  _.defaults(options, defaults);

  this.options = options;
}

util.inherits(Tingo, Store);

_.extend(Tingo.prototype, {

  connect: function (callback) {
    var self = this;

    var options = this.options;

    this.db = new tingodb.Db(options.dbPath, {});
    // this.db.on('close', function() {
    //   self.emit('disconnect');
    // });
    this.store = this.db.collection(options.collectionName + '.tingo');
//    this.store.ensureIndex({ 'aggregateId': 1, date: 1 }, function() {});

    this.emit('connect');
    if (callback) callback(null, this);
  },

  disconnect: function (callback) {
    if (!this.db) {
      if (callback) callback(null);
      return;
    }

    this.emit('disconnect');
    this.db.close(callback || function () {});
  },

  getNewId: function(callback) {
    callback(null, new ObjectID().toString());
  },

  get: function (id, callback) {
    if (!id || !_.isString(id)) {
      var err = new Error('Please pass a valid id!');
      debug(err);
      return callback(err);
    }

    this.store.findOne({ _id: id }, function (err, entry) {
      if (err) {
        return callback(err);
      }

      if (!entry) {
        return callback(null, null);
      }

      callback(null, entry.revision || null);
    });
  },

  set: function (id, revision, oldRevision, callback) {
    if (!id || !_.isString(id)) {
      var err = new Error('Please pass a valid id!');
      debug(err);
      return callback(err);
    }
    if (!revision || !_.isNumber(revision)) {
      var err = new Error('Please pass a valid revision!');
      debug(err);
      return callback(err);
    }

    this.store.update({ _id: id, revision: oldRevision }, { _id: id, revision: revision }, { safe: true, upsert: true }, function (err, modifiedCount) {
      if (modifiedCount === 0) {
        err = new ConcurrencyError();
        debug(err);
        if (callback) {
          callback(err);
        }
        return;
      }
      if (err && err.message && err.message.match(/duplicate key/i)) {
        debug(err);
        err = new ConcurrencyError();
        debug(err);
        if (callback) {
          callback(err);
        }
        return;
      }
      if (callback) { callback(err); }
    });
  },

  saveLastEvent: function (evt, callback) {
    this.store.save({ _id: 'THE_LAST_SEEN_EVENT', event: evt }, { safe: true }, function (err) {
      if (callback) { callback(err); }
    });
  },

  getLastEvent: function (callback) {
    this.store.findOne({ _id: 'THE_LAST_SEEN_EVENT' }, function (err, entry) {
      if (err) {
        return callback(err);
      }

      if (!entry) {
        return callback(null, null);
      }

      callback(null, entry.event || null);
    });
  },

  clear: function (callback) {
    this.store.remove({}, { safe: true }, callback);
  }

});

module.exports = Tingo;
```

## File: `lib/store/base.js`
```javascript
var util = require('util'),
  EventEmitter = require('events').EventEmitter,
  prequire = require('parent-require'),
  _ = require('lodash'),
  uuid = require('uuid').v4;

/**
 * Store constructor
 * @param {Object} options The options can have information like host, port, etc. [optional]
 */
function Store(options) {
  options = options || {};

  EventEmitter.call(this);
}

util.inherits(Store, EventEmitter);

function implementError (callback) {
  var err = new Error('Please implement this function!');
  if (callback) callback(err);
  throw err;
}

_.extend(Store.prototype, {

  /**
   * Initiate communication with the lock.
   * @param {Function} callback The function, that will be called when this action is completed. [optional]
   *                             `function(err, queue){}`
   */
  connect: implementError,

  /**
   * Terminate communication with the lock.
   * @param {Function} callback The function, that will be called when this action is completed. [optional]
   *                             `function(err){}`
   */
  disconnect: implementError,

  /**
   * Use this function to obtain a new id.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                             `function(err, id){}` id is of type String.
   */
  getNewId: function (callback) {
    var id = uuid().toString();
    if (callback) callback(null, id);
  },

  /**
   * Use this function to obtain the requested saga data.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                             `function(err, data){}` data is of type Object.
   */
  get: function (id, callback) {
    implementError(callback);
  },

  /**
   * Use this function to remove the matched saga.
   * @param {String}   id       The id of the saga
   * @param {Function} callback The function, that will be called when this action is completed. [optional]
   *                             `function(err){}`
   */
  remove: function (id, callback) {
    implementError(callback);
  },

  /**
   * Use this function to save the saga and the optional commands.
   * @param {Object}   saga     The saga object
   * @param {Array}    cmds     The commands array (can be empty)
   * @param {Function} callback The function, that will be called when this action is completed. [optional]
   *                            `function(err){}`
   */
  save: function (saga, cmds, callback) {
    implementError(callback);
  },

  /**
   * Use this function to get all timeouted sagas.
   * @param  {Function} callback The function, that will be called when this action is completed.
   *                             `function(err, sagas){}` saga is of type Array.
   */
  getTimeoutedSagas: function (options, callback) {
    implementError(callback || options);
  },

  /**
   * Use this function to get all sagas that are older then the passed date.
   * @param {Date}     date     The date
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err, sagas){}` saga is of type Array.
   */
  getOlderSagas: function (date, callback) {
    implementError(callback);
  },

  /**
   * Use this function to get all undispatched commands.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err, cmdsSagaMap){}` cmdsSagaMap is of type Array.
   */
  getUndispatchedCommands: function (options, callback) {
    implementError(callback || options);
  },

  /**
   * Use this function mark a command as dispatched. (will remove it from the db)
   * @param {String}   cmdId    The command id
   * @param {String}   sagaId   The saga id
   * @param {Function} callback The function, that will be called when this action is completed. [optional]
   *                            `function(err){}`
   */
  setCommandToDispatched: function (cmdId, sagaId, callback) {
    implementError(callback);
  },

  /**
   * NEVER USE THIS FUNCTION!!! ONLY FOR TESTS!
   * clears the complete store...
   * @param {Function} callback the function that will be called when this action has finished [optional]
   */
  clear: function (callback) {
    implementError(callback);
  }

});

Store.use = function (toRequire) {
  var required;
  try {
    required = require(toRequire);
  } catch (e) {
    // workaround when `npm link`'ed for development
    required = prequire(toRequire);
  }
  return required;
};

module.exports = Store;
```

## File: `lib/store/index.js`
```javascript
var tolerate = require('tolerance'),
  _ = require('lodash'),
  Base = require('./base');

function exists(toCheck) {
  var _exists = require('fs').existsSync || require('path').existsSync;
  if (require('fs').accessSync) {
    _exists = function (toCheck) {
      try {
        require('fs').accessSync(toCheck);
        return true;
      } catch (e) {
        return false;
      }
    };
  }
  return _exists(toCheck);
}

function getSpecificDbImplementation(options) {
  options = options || {};

  options.type = options.type || 'inmemory';

  if (_.isFunction(options.type)) {
    return options.type;
  }

  options.type = options.type.toLowerCase();

  var dbPath = __dirname + "/databases/" + options.type + ".js";

  if (!exists(dbPath)) {
    var errMsg = 'Implementation for db "' + options.type + '" does not exist!';
    console.log(errMsg);
    throw new Error(errMsg);
  }

  try {
    var db = require(dbPath);
    return db;
  } catch (err) {

    if (err.message.indexOf('Cannot find module') >= 0 &&
      err.message.indexOf("'") > 0 &&
      err.message.lastIndexOf("'") !== err.message.indexOf("'")) {

      var moduleName = err.message.substring(err.message.indexOf("'") + 1, err.message.lastIndexOf("'"));
      console.log('Please install module "' + moduleName +
        '" to work with db implementation "' + options.type + '"!');
    }

    throw err;
  }
}

module.exports = {
  Store: Base,

  create: function(options, callback) {
    if (typeof options === 'function') {
      callback = options;
      options = {};
    }

    options = options || {};

    var Store;

    try {
      Store = getSpecificDbImplementation(options);
    } catch (err) {
      if (callback) callback(err);
      throw err;
    }

    var store = new Store(options);
    if (callback) {
      process.nextTick(function () {
        tolerate(function (callback) {
          store.connect(callback);
        }, options.timeout || 0, callback || function () {
        });
      });
    }
    return store;
  }
};
```

## File: `lib/store/databases/azuretable.js`
```javascript
var util = require('util'),
  Store = require('../base'),
  debug = require('debug')('saga:azuretable'),
  ConcurrencyError = require('../../errors/concurrencyError'),
  _ = require('lodash'),
  async = Store.use('async'),
  azure = Store.use('azure-storage'),
  eg = azure.TableUtilities.entityGenerator,
  jsondate = require('jsondate');


function AzureTable(options) {
  var azureConf = {
    storageAccount: 'nodecqrs',
    storageAccessKey: 'StXScH574p1krnkjbxjkHkMkrtbIMQpYMbH1D1uYVqS4ny/DpXVkL4ld02xeKupCQnIIN+v0KVmdLLSVA/cxTQ==',
    storageTableHost: 'https://nodecqrs.table.core.windows.net/'
  };

  this.options = _.defaults(options, azureConf);

  var defaults = {
    sagaTableName: 'saga',
    commandTableName: 'sagaCommand',
    undispatchedCommandtableName: 'sagaUndispatchedCommand'
  };

  this.options = _.defaults(this.options, defaults);
}

util.inherits(AzureTable, Store);

_.extend(AzureTable.prototype, {

  connect: function (callback) {
    var retryOperations = new azure.ExponentialRetryPolicyFilter();

    var self = this;

    this.client = azure.createTableService(this.options.storageAccount, this.options.storageAccessKey, this.options.storageTableHost).withFilter(retryOperations);

    var createSagaTable = function (callback) {
      self.client.createTableIfNotExists(self.options.sagaTableName, callback);
    };

    var createCommandTable = function (callback) {
      self.client.createTableIfNotExists(self.options.commandTableName, callback);
    };

    var createUndispatchedCommandTable = function (callback) {
      self.client.createTableIfNotExists(self.options.undispatchedCommandtableName, callback);
    };

    async.parallel([
      createSagaTable,
      createCommandTable,
      createUndispatchedCommandTable
    ], function (err) {
      if (err) {
        if (callback) callback(err);
      } else {
        self.emit('connect');
        if (callback) callback(null, self);
      }
    });
  },

  disconnect: function (callback) {
    this.emit('disconnect');
    if (callback) callback(null);
  },

  get: function (id, callback) {

    var queryOptions = {
      entityResolver: sagaResolver
    };

    if (!id || !_.isString(id)) {
      var err = new Error('Please pass a valid id!');
      debug(err);
      return callback(err);
    }

    this.client.retrieveEntity(this.options.sagaTableName,
      id,
      id,
      queryOptions,
      function (err, saga) {
        if (err && err.code != 'ResourceNotFound') {
          if (callback) return callback(err);
        }

        if (!saga) {
          return callback(null, null);
        }

        callback(null, saga);
      }
    );
  },

  remove: function (id, callback) {

    var self = this;
    var query = new azure.TableQuery();
    query.where('PartitionKey eq ?', id);

    if (!id || !_.isString(id)) {
      var err = new Error('Please pass a valid id!');
      debug(err);
      return callback(err);
    }

    var objDescriptor = {
      PartitionKey: eg.String(id),
      RowKey: eg.String(id)
    };


    var removeSaga = function (callback) {
      self.client.deleteEntity(self.options.sagaTableName, objDescriptor, function (err) {
        if (err && err.code != 'ResourceNotFound') {
          debug(err);
          return callback(err);
        }
        callback(null);
      });
    };

    var removeCommands = function (callback) {
      self.client.queryEntities(self.options.commandTableName, query, null, function (err, entities) {
          if (!err) {
            async.each(entities.entries, function (entity, callback) {
                self.client.deleteEntity(self.options.commandTableName, entity, function (error, response) {
                  callback(error);
                });
              },
              function (error) {
                callback(error);
              });
          }
        }
      );
    };

    var removeUndispatchedCommands = function (callback) {
      self.client.queryEntities(self.options.undispatchedCommandtableName, query, null, function (err, entities) {
          if (!err) {
            async.each(entities.entries, function (entity, callback) {
                self.client.deleteEntity(self.options.undispatchedCommandtableName, entity, function (error, response) {
                  callback(error);
                });
              },
              function (error) {
                callback(error);
              });
          }
        }
      );
    };

    async.parallel([
      removeSaga,
      removeCommands,
      removeUndispatchedCommands
    ], function (err) {
      callback(err);
    });
  },

  save: function (saga, cmds, callback) {

    var self = this;
    var commandBatch = new azure.TableBatch();
    var undispatchedCommandBatch = new azure.TableBatch();

    if (!saga || !_.isObject(saga) || !_.isString(saga.id) || !_.isDate(saga._commitStamp)) {
      var err = new Error('Please pass a valid saga!');
      debug(err);
      return callback(err);
    }

    if (!cmds || !_.isArray(cmds)) {
      var err = new Error('Please pass a valid saga!');
      debug(err);
      return callback(err);
    }

    if (cmds.length > 0) {
      for (var c in cmds) {
        var cmd = cmds[c];
        if (!cmd.id || !_.isString(cmd.id) || !cmd.payload) {
          var err = new Error('Please pass a valid commands array!');
          debug(err);
          return callback(err);
        }

        var entity = {
          PartitionKey: eg.String(saga.id),
          RowKey: eg.String(cmd.id),
          payload: eg.String(JSON.stringify(cmd)),
          commitStamp: eg.DateTime(saga._commitStamp)
        };

        commandBatch.insertOrReplaceEntity(entity);
        undispatchedCommandBatch.insertOrReplaceEntity(entity);
      }
    }

    async.parallel([
      function (callback) {
        if (!saga._etag) {
          self.client.insertEntity(self.options.sagaTableName,
            {
              PartitionKey: eg.String(saga.id),
              RowKey: eg.String(saga.id),
              commitStamp: eg.DateTime(saga._commitStamp),
              timeoutAt: eg.DateTime(saga._timeoutAt),
              payload: eg.String(JSON.stringify(saga))
            }, function (err) {
              if (err && err.code == 'EntityAlreadyExists')
                return callback(new ConcurrencyError());

              callback(err);
            });
        } else {
          var etag = saga._etag;
          delete saga._etag;
          self.client.updateEntity(self.options.sagaTableName,
            {
              '.metadata': {
                etag: etag
              },
              PartitionKey: eg.String(saga.id),
              RowKey: eg.String(saga.id),
              commitStamp: eg.DateTime(saga._commitStamp),
              timeoutAt: eg.DateTime(saga._timeoutAt),
              payload: eg.String(JSON.stringify(saga))
            }, function (err) {
              if (err && err.code == 'UpdateConditionNotSatisfied' && err.statusCode == 412)
                return callback(new ConcurrencyError());

              callback(err);
            });
        }
      },
      function (callback) {
        if (commandBatch.size() > 0) {
          self.client.executeBatch(self.options.commandTableName, commandBatch, function (err) {
            if (err && err.code == 'EntityAlreadyExists')
              return callback(new ConcurrencyError());

            callback(err);
          });
        } else {
          callback();
        }
      },
      function (callback) {
        if (undispatchedCommandBatch.size() > 0) {
          self.client.executeBatch(self.options.undispatchedCommandtableName, undispatchedCommandBatch, function (err) {
            if (err && err.code == 'EntityAlreadyExists')
              return callback(new ConcurrencyError());

            callback(err);
          });
        } else {
          callback();
        }
      }
    ], function (err) {
      callback(err);
    });

  },

  getTimeoutedSagas: function (options, callback) {
    if (!callback) {
      callback = options;
      options = {};
    }
    var entities = [];
    var self = this;
    var continuationToken = null;

    var queryOptions = {
      entityResolver: sagaResolver
    };

    var tableQuery = new azure.TableQuery();
    tableQuery.where('timeoutAt <= ?', new Date());

    async.doWhilst(function (end) {
      // retrieve entities
      self.client.queryEntities(self.options.sagaTableName, tableQuery, continuationToken, queryOptions, function (err, results) {
        if (err) {
          debug(err);
          return end(err);
        }
        continuationToken = results.continuationToken;
        entities = entities.concat(results.entries);
        end(null);
      });
    }, function () {
      // test if we need to load more
      return continuationToken !== null;
    }, function (err) {
      // return results
      if (err) {
        debug(err);
        return callback(err);
      }

      return callback(null, entities);
    });

  },

  getOlderSagas: function (date, callback) {

    var queryOptions = {
      entityResolver: sagaResolver
    };

    if (!date || !_.isDate(date)) {
      var err = new Error('Please pass a valid date object!');
      debug(err);
      return callback(err);
    }

    var entities = [];
    var self = this;
    var continuationToken = null;

    var tableQuery = new azure.TableQuery();
    tableQuery.where('commitStamp <= ?', date);

    async.doWhilst(function (end) {
      // retrieve entities
      self.client.queryEntities(self.options.sagaTableName, tableQuery, continuationToken, queryOptions, function (err, results) {
        if (err) {
          debug(err);
          return end(err);
        }
        continuationToken = results.continuationToken;
        entities = entities.concat(results.entries);
        end(null);
      });
    }, function () {
      // test if we need to load more
      return continuationToken !== null;
    }, function (err) {
      // return results
      if (err) {
        debug(err);
        return callback(err);
      }

      return callback(null, entities);
    });

  },

  getUndispatchedCommands: function (options, callback) {
    if (!callback) {
      callback = options;
      options = {};
    }
    var entities = [];
    var self = this;
    var continuationToken = null;

    var tableQuery = new azure.TableQuery();

    async.doWhilst(function (end) {
      // retrieve entities
      self.client.queryEntities(self.options.undispatchedCommandtableName, tableQuery, continuationToken, function (err, results) {
        if (err) {
          debug(err);
          return end(err);
        }
        continuationToken = results.continuationToken;
        entities = entities.concat(results.entries);
        end(null);
      });
    }, function () {
      // test if we need to load more
      return continuationToken !== null;
    }, function (err) {
      // return results
      if (err) {
        debug(err);
        return callback(err);
      }

      entities = entities.map(function (entity) {
        var data = jsondate.parse(entity.payload._);

        return {sagaId: entity.PartitionKey._, commandId: entity.RowKey._, command: data.payload, commitStamp: entity.commitStamp._};
      });

      return callback(null, entities);
    });

  },

  setCommandToDispatched: function (cmdId, sagaId, callback) {
    var self = this;

    if (!cmdId || !_.isString(cmdId)) {
      var err = new Error('Please pass a valid command id!');
      debug(err);
      return callback(err);
    }

    if (!sagaId || !_.isString(sagaId)) {
      var err = new Error('Please pass a valid saga id!');
      debug(err);
      return callback(err);
    }

    var objDescriptor = {
      PartitionKey: eg.String(sagaId),
      RowKey: eg.String(cmdId)
    };

    self.client.deleteEntity(self.options.undispatchedCommandtableName, objDescriptor, null,
      function (err) {
        if (err && err.code != 'ResourceNotFound') {
          debug(err);
          return callback(err);
        }
        callback(null);
      });

  },

  clear: function (callback) {

    var self = this;
    var query = new azure.TableQuery();

    var clearSagaTable = function (callback) {
      self.client.queryEntities(self.options.sagaTableName, query, null, function (err, entities) {
          if (!err) {
            async.each(entities.entries, function (entity, callback) {
                self.client.deleteEntity(self.options.sagaTableName, entity, function (error, response) {
                  callback(error);
                });
              },
              function (error) {
                callback(error);
              });
          }
        }
      );
    };

    var clearCommandTable = function (callback) {
      self.client.queryEntities(self.options.commandTableName, query, null, function (err, entities) {
          if (!err) {
            async.each(entities.entries, function (entity, callback) {
                self.client.deleteEntity(self.options.commandTableName, entity, function (error, response) {
                  callback(error);
                });
              },
              function (error) {
                callback(error);
              });
          }
        }
      );
    };

    var clearUndispatchedCommandTable = function (callback) {
      self.client.queryEntities(self.options.undispatchedCommandtableName, query, null, function (err, entities) {
          if (!err) {
            async.each(entities.entries, function (entity, callback) {
                self.client.deleteEntity(self.options.undispatchedCommandtableName, entity, function (error, response) {
                  callback(error);
                });
              },
              function (error) {
                callback(error);
              });
          }
        }
      );
    }

    async.parallel([
      clearSagaTable,
      clearCommandTable,
      clearUndispatchedCommandTable
    ], callback);
  }
});

function sagaResolver(entity) {
  var res = jsondate.parse(entity.payload._);
  res._etag = entity['.metadata']['etag'];
  return res;
}


module.exports = AzureTable;
```

## File: `lib/store/databases/inmemory.js`
```javascript
var util = require('util'),
  Store = require('../base'),
  debug = require('debug')('saga:inmemory'),
  uuid = require('uuid').v4,
  ConcurrencyError = require('../../errors/concurrencyError'),
  _ = require('lodash');

function InMemory(options) {
  Store.call(this, options);
  this.store = {};
  this.cmds = {};
}

util.inherits(InMemory, Store);

_.extend(InMemory.prototype, {

  connect: function (callback) {
    this.emit('connect');
    if (callback) callback(null, this);
  },

  disconnect: function (callback) {
    this.emit('disconnect');
    if (callback) callback(null);
  },

  get: function (id, callback) {
    if (!id || !_.isString(id)) {
      var err = new Error('Please pass a valid id!');
      debug(err);
      return callback(err);
    }

    callback(null, this.store[id] || null);
  },

  remove: function (id, callback) {
    if (!id || !_.isString(id)) {
      var err = new Error('Please pass a valid id!');
      debug(err);
      return callback(err);
    }

    if (this.store[id]) {
      delete this.store[id];
    }

    if (this.cmds[id]) {
      delete this.cmds[id];
    }

    if (callback) { callback(null); }
  },

  save: function (saga, cmds, callback) {
    if (!saga || !_.isObject(saga) || !_.isString(saga.id) || !_.isDate(saga._commitStamp)) {
      var err = new Error('Please pass a valid saga!');
      debug(err);
      return callback(err);
    }

    if (!cmds || !_.isArray(cmds)) {
      var err = new Error('Please pass a valid saga!');
      debug(err);
      return callback(err);
    }

    if (cmds.length > 0) {
      for (var c in cmds) {
        var cmd = cmds[c];
        if (!cmd.id || !_.isString(cmd.id) || !cmd.payload) {
          var err = new Error('Please pass a valid commands array!');
          debug(err);
          return callback(err);
        }
      }
    }

    if ((this.store[saga.id] && saga._hash && saga._hash !== this.store[saga.id]._hash) ||
        (!this.store[saga.id] && saga._hash) ||
        (this.store[saga.id] && this.store[saga.id]._hash && !saga._hash)) {
      var err = new ConcurrencyError();
      debug(err);
      if (callback) { callback(err); }
      return;
    }

    saga._hash = uuid().toString();

    this.store[saga.id] = saga;
    this.cmds[saga.id] = this.cmds[saga.id] || {};

    var self = this;
    cmds.forEach(function (cmd) {
      self.cmds[saga.id][cmd.id] = cmd.payload;
    });

    if (callback) { callback(null); }
  },

  getTimeoutedSagas: function (options, callback) {
    if (!callback) {
      callback = options;
      options = {};
    }
    options = options || {};

    options.limit = options.limit || -1;
    options.skip = options.skip || 0;

    var res = _.filter(_.values(this.store), function (s) {
      return s._timeoutAt && s._timeoutAt.getTime() <= (new Date()).getTime();
    });

    if (options.limit === -1) {
      return callback(null, res.slice(options.skip));
    }

    if (res.length <= options.skip) {
      return callback(null, []);
    }

    callback(null, res.slice(options.skip, options.skip + options.limit));
  },

  getOlderSagas: function (date, callback) {
    if (!date || !_.isDate(date)) {
      var err = new Error('Please pass a valid date object!');
      debug(err);
      return callback(err);
    }

    var res = _.filter(_.values(this.store), function (s) {
      return s._commitStamp.getTime() <= (date).getTime();
    });

    callback(null, res);
  },

  getUndispatchedCommands: function (options, callback) {
    if (!callback) {
      callback = options;
      options = {};
    }
    options = options || {};

    options.limit = options.limit || -1;
    options.skip = options.skip || 0;

    var res = [];
    for (var sagaId in this.cmds) {
      for (var cmdId in this.cmds[sagaId]) {
        res.push({ sagaId: sagaId, commandId: cmdId, command: this.cmds[sagaId][cmdId], commitStamp: this.store[sagaId]._commitStamp });
      }
    }

    if (options.limit === -1) {
      return callback(null, res.slice(options.skip));
    }

    if (res.length <= options.skip) {
      return callback(null, []);
    }

    callback(null, res.slice(options.skip, options.skip + options.limit));
  },

  setCommandToDispatched: function (cmdId, sagaId, callback) {
    if (!cmdId || !_.isString(cmdId)) {
      var err = new Error('Please pass a valid command id!');
      debug(err);
      return callback(err);
    }

    if (!sagaId || !_.isString(sagaId)) {
      var err = new Error('Please pass a valid saga id!');
      debug(err);
      return callback(err);
    }

    if (!this.cmds[sagaId] || !this.cmds[sagaId][cmdId]) {
      if (callback) { callback(null); }
      return;
    }

    delete this.cmds[sagaId][cmdId];

    callback(null);
  },

  clear: function (callback) {
    this.store = {};
    this.cmds = {};
    if (callback) callback(null);
  }

});

module.exports = InMemory;
```

## File: `lib/store/databases/mongodb.js`
```javascript
var util = require('util'),
  Store = require('../base'),
  _ = require('lodash'),
  debug = require('debug')('saga:mongodb'),
  ConcurrencyError = require('../../errors/concurrencyError'),
  mongo = Store.use('mongodb'),
  mongoVersion = Store.use('mongodb/package.json').version,
  isNew = mongoVersion.indexOf('1.') !== 0,
  isNew = mongoVersion.indexOf('1.') !== 0,
  ObjectID = isNew ? mongo.ObjectID : mongo.BSONPure.ObjectID;

function Mongo(options) {
  Store.call(this, options);

  var defaults = {
    host: 'localhost',
    port: 27017,
    dbName: 'domain',
    collectionName: 'saga'//,
    // heartbeat: 60 * 1000
  };

  _.defaults(options, defaults);

  var defaultOpt = {
    ssl: false
  };

  options.options = options.options || {};

  if (isNew) {
    defaultOpt.autoReconnect = false;
    defaultOpt.useNewUrlParser = true;
    defaultOpt.useUnifiedTopology = true;
    _.defaults(options.options, defaultOpt);
  } else {
    defaultOpt.auto_reconnect = false;
    _.defaults(options.options, defaultOpt);
  }

  this.options = options;
}

util.inherits(Mongo, Store);

_.extend(Mongo.prototype, {

  connect: function (callback) {
    var self = this;

    var options = this.options;

    var connectionUrl;

    if (options.url) {
      connectionUrl = options.url;
    } else {
      var members = options.servers
        ? options.servers
        : [{host: options.host, port: options.port}];

      var memberString = _(members).map(function(m) { return m.host + ':' + m.port; });
      var authString = options.username && options.password
        ? options.username + ':' + options.password + '@'
        : '';
      var optionsString = options.authSource
        ? '?authSource=' + options.authSource
        : '';

      connectionUrl = 'mongodb://' + authString + memberString + '/' + options.dbName + optionsString;
    }

    var client;

    if (mongo.MongoClient.length === 2) {
      client = new mongo.MongoClient(connectionUrl, options.options);
      client.connect(function(err, cl) {
        if (err) {
          debug(err);
          if (callback) callback(err);
          return;
        }

        self.db = cl.db(cl.s.options.dbName);
        if (!self.db.close) {
          self.db.close = cl.close.bind(cl);
        }
        initDb();
      });
    } else {
      client = new mongo.MongoClient();
      client.connect(connectionUrl, options.options, function(err, db) {
        if (err) {
          debug(err);
          if (callback) callback(err);
          return;
        }

        self.db = db;
        initDb();
      });
    }

    function initDb() {
      self.db.on('close', function() {
        self.emit('disconnect');
        self.stopHeartbeat();
      });

      var finish = function (err) {
        self.store = self.db.collection(options.collectionName);
        self.store.createIndex({ '_commands.id': 1}, function() {});
        self.store.createIndex({ '_timeoutAt': 1}, function() {});
        self.store.createIndex({ '_commitStamp': 1}, function() {});

        if (!err) {
          self.emit('connect');

          if (self.options.heartbeat) {
            self.startHeartbeat();
          }
        }
        if (callback) callback(err, self);
      };

      finish();
    }
  },

  stopHeartbeat: function () {
    if (this.heartbeatInterval) {
      clearInterval(this.heartbeatInterval);
      delete this.heartbeatInterval;
    }
  },

  startHeartbeat: function () {
    var self = this;

    var gracePeriod = Math.round(this.options.heartbeat / 2);
    this.heartbeatInterval = setInterval(function () {
      var graceTimer = setTimeout(function () {
        if (self.heartbeatInterval) {
          console.error((new Error ('Heartbeat timeouted after ' + gracePeriod + 'ms (mongodb)')).stack);
          self.disconnect();
        }
      }, gracePeriod);

      self.db.command({ ping: 1 }, function (err) {
        if (graceTimer) clearTimeout(graceTimer);
        if (err) {
          console.error(err.stack || err);
          self.disconnect();
        }
      });
    }, this.options.heartbeat);
  },

  disconnect: function (callback) {
    this.stopHeartbeat();

    if (!this.db) {
      if (callback) callback(null);
      return;
    }

    this.db.close(callback || function () {});
  },

  getNewId: function(callback) {
    callback(null, new ObjectID().toString());
  },

  save: function (saga, cmds, callback) {
    if (!saga || !_.isObject(saga) || !_.isString(saga.id) || !_.isDate(saga._commitStamp)) {
      var err = new Error('Please pass a valid saga!');
      debug(err);
      return callback(err);
    }

    if (!cmds || !_.isArray(cmds)) {
      var err = new Error('Please pass a valid saga!');
      debug(err);
      return callback(err);
    }

    if (cmds.length > 0) {
      for (var c in cmds) {
        var cmd = cmds[c];
        if (!cmd.id || !_.isString(cmd.id) || !cmd.payload) {
          var err = new Error('Please pass a valid commands array!');
          debug(err);
          return callback(err);
        }
      }
    }

    saga._id = saga.id;
    saga._commands = cmds;

    if (!saga._hash) {
      saga._hash = new ObjectID().toString();
      this.store.insertOne(saga, { safe: true, w: 1 }, function (err) {
        if (err && err.message && err.message.indexOf('duplicate key') >= 0) {
          return callback(new ConcurrencyError());
        }
        if (callback) { callback(err); }
      });
    } else {
      var currentHash = saga._hash;
      saga._hash = new ObjectID().toString();
      this.store.updateOne({ _id: saga._id, _hash: currentHash }, { $set: saga }, { safe: true }, function(err, modifiedCount) {
        if (isNew) {
          if (modifiedCount && modifiedCount.result && modifiedCount.result.n === 0) {
            return callback(new ConcurrencyError());
          }
        } else {
          if (modifiedCount === 0) {
            return callback(new ConcurrencyError());
          }
        }
        if (callback) { callback(err); }
      });
    }
  },

  get: function (id, callback) {
    if (!id || !_.isString(id)) {
      var err = new Error('Please pass a valid id!');
      debug(err);
      return callback(err);
    }

    this.store.findOne({ _id: id }, function (err, saga) {
      if (err) {
        return callback(err);
      }

      if (!saga) {
        return callback(null, null);
      }

      if (saga._commands) {
        delete saga._commands;
      }

      callback(null, saga);
    });
  },

  remove: function (id, callback) {
    if (!id || !_.isString(id)) {
      var err = new Error('Please pass a valid id!');
      debug(err);
      return callback(err);
    }

    this.store.deleteOne({ _id: id }, { safe: true, w: 1 }, function (err) {
      if (callback) callback(err);
    });
  },

  getTimeoutedSagas: function (options, callback) {
    if (!callback) {
      callback = options;
      options = {};
    }
    options = options || {};
    // options.limit = options.limit || -1;
    // options.skip = options.skip || 0;
    options.sort = [['_timeoutAt', 'asc']];
    this.store.find({
      _timeoutAt: { '$lte': new Date() }
    }, options).toArray(function (err, sagas) {
      if (err) {
        return callback(err);
      }

      sagas.forEach(function (s) {
        if (s._commands) {
          delete s._commands;
        }
      });

      callback(null, sagas);
    });
  },

  getOlderSagas: function (date, callback) {
    if (!date || !_.isDate(date)) {
      var err = new Error('Please pass a valid date object!');
      debug(err);
      return callback(err);
    }

    this.store.find({
      _commitStamp: { '$lte': date }
    }).toArray(function (err, sagas) {
      if (err) {
        return callback(err);
      }

      sagas.forEach(function (s) {
        if (s._commands) {
          delete s._commands;
        }
      });

      callback(null, sagas);
    });
  },

  getUndispatchedCommands: function (options, callback) {
    if (!callback) {
      callback = options;
      options = {};
    }
    options = options || {};
    // options.limit = options.limit || -1;
    // options.skip = options.skip || 0;
    options.sort = [['_commitStamp', 'asc']];

    var res = [];

    this.store.find({
      '_commands.0': {$exists: true}
    }, options).toArray(function (err, sagas) {
      if (err) {
        return callback(err);
      }

      sagas.forEach(function (s) {
        if (s._commands && s._commands.length > 0) {
          s._commands.forEach(function (c) {
            res.push({ sagaId: s._id, commandId: c.id, command: c.payload, commitStamp: s._commitStamp });
          });
        }
      });

      callback(null, res);
    });
  },

  setCommandToDispatched: function (cmdId, sagaId, callback) {
    if (!cmdId || !_.isString(cmdId)) {
      var err = new Error('Please pass a valid command id!');
      debug(err);
      return callback(err);
    }

    if (!sagaId || !_.isString(sagaId)) {
      var err = new Error('Please pass a valid saga id!');
      debug(err);
      return callback(err);
    }

    this.store.updateOne({ _id: sagaId, '_commands.id': cmdId }, { $pull: { '_commands': { id: cmdId } } }, { safe: true }, function (err) {
      if (callback) callback(err);
    });
  },

  clear: function (callback) {
    this.store.deleteMany({}, { safe: true }, callback);
  }

});

module.exports = Mongo;
```

## File: `lib/store/databases/redis.js`
```javascript
var util = require('util'),
  Store = require('../base'),
  _ = require('lodash'),
  debug = require('debug')('saga:redis'),
  uuid = require('uuid').v4,
  ConcurrencyError = require('../../errors/concurrencyError'),
  jsondate = require('jsondate'),
  async = require('async'),
  redis = Store.use('redis');

function Redis(options) {
  Store.call(this, options);

  var defaults = {
    host: 'localhost',
    port: 6379,
    prefix: 'saga',
    retry_strategy: function (options) {
      return undefined;
    }//,
    // heartbeat: 60 * 1000
  };

  _.defaults(options, defaults);

  if (options.url) {
    var url = require('url').parse(options.url);
    if (url.protocol === 'redis:') {
      if (url.auth) {
        var userparts = url.auth.split(':');
        options.user = userparts[0];
        if (userparts.length === 2) {
          options.password = userparts[1];
        }
      }
      options.host = url.hostname;
      options.port = url.port;
      if (url.pathname) {
        options.db = url.pathname.replace('/', '', 1);
      }
    }
  }

  this.options = options;
}

util.inherits(Redis, Store);

_.extend(Redis.prototype, {

  connect: function (callback) {
    var self = this;

    var options = this.options;

    this.client = new redis.createClient(options.port || options.socket, options.host, _.omit(options, 'prefix'));

    this.prefix = options.prefix;

    var calledBack = false;

    if (options.password) {
      this.client.auth(options.password, function(err) {
        if (err && !calledBack && callback) {
          calledBack = true;
          if (callback) callback(err, self);
          return;
        }
        if (err) throw err;
      });
    }

    if (options.db) {
      this.client.select(options.db);
    }

    this.client.on('end', function () {
      self.disconnect();
      self.stopHeartbeat();
    });

    this.client.on('error', function (err) {
      console.log(err);

      if (calledBack) return;
      calledBack = true;
      if (callback) callback(null, self);
    });

    this.client.on('connect', function () {
      if (options.db) {
        self.client.send_anyways = true;
        self.client.select(options.db);
        self.client.send_anyways = false;
      }

      self.emit('connect');

      if (self.options.heartbeat) {
        self.startHeartbeat();
      }

      if (calledBack) return;
      calledBack = true;
      if (callback) callback(null, self);
    });
  },

  stopHeartbeat: function () {
    if (this.heartbeatInterval) {
      clearInterval(this.heartbeatInterval);
      delete this.heartbeatInterval;
    }
  },

  startHeartbeat: function () {
    var self = this;

    var gracePeriod = Math.round(this.options.heartbeat / 2);
    this.heartbeatInterval = setInterval(function () {
      var graceTimer = setTimeout(function () {
        if (self.heartbeatInterval) {
          console.error((new Error ('Heartbeat timeouted after ' + gracePeriod + 'ms (redis)')).stack);
          self.disconnect();
        }
      }, gracePeriod);

      self.client.ping(function (err) {
        if (graceTimer) clearTimeout(graceTimer);
        if (err) {
          console.error(err.stack || err);
          self.disconnect();
        }
      });
    }, this.options.heartbeat);
  },

  disconnect: function (callback) {
    this.stopHeartbeat();

    if (this.client) {
      this.client.end(true);
    }
    this.emit('disconnect');
    if (callback) callback(null, this);
  },

  getNewId: function(callback) {
    this.client.incr('nextItemId:' + this.prefix, function(err, id) {
      if (err) {
        return callback(err);
      }
      callback(null, id.toString());
    });
  },

  save: function (saga, cmds, callback) {
    if (!saga || !_.isObject(saga) || !_.isString(saga.id) || !_.isDate(saga._commitStamp)) {
      var err = new Error('Please pass a valid saga!');
      debug(err);
      return callback(err);
    }

    if (!cmds || !_.isArray(cmds)) {
      var err = new Error('Please pass a valid saga!');
      debug(err);
      return callback(err);
    }

    if (cmds.length > 0) {
      for (var c in cmds) {
        var cmd = cmds[c];
        if (!cmd.id || !_.isString(cmd.id) || !cmd.payload) {
          var err = new Error('Please pass a valid commands array!');
          debug(err);
          return callback(err);
        }
      }
    }

    var self = this;

    var sagaKey;
    if (saga._timeoutAt) {
      sagaKey = this.options.prefix + '_saga' + ':' +  saga._commitStamp.getTime() + ':' + saga._timeoutAt.getTime() + ':' + saga.id;
    } else {
      sagaKey = this.options.prefix + '_saga' + ':' +  saga._commitStamp.getTime() + ':Infinity:' + saga.id;
    }

    var cmdMap = [];

    _.each(cmds, function (cmd) {
      cmd.payload._sagaId = saga.id;
      cmd.payload._commandId = cmd.id;
      cmd.payload._commitStamp = saga._commitStamp;
      cmdMap.push(self.options.prefix + '_command' + ':' + cmd.payload._sagaId+ ':' + cmd.payload._commandId);
      cmdMap.push(JSON.stringify(cmd.payload));
    });

    this.client.watch(sagaKey, function (err) {
      if (err) {
        return callback(err);
      }

      self.get(saga.id, function (err, s) {
        if (err) {
          debug(err);
          if (callback) callback(err);
          return;
        }

        if ((s && saga._hash && saga._hash !== s._hash) ||
          (!s && saga._hash) ||
          (s && s._hash && !saga._hash)) {
          self.client.unwatch(function (err) {
            if (err) {
              debug(err);
            }

            err = new ConcurrencyError();
            debug(err);
            if (callback) {
              callback(err);
            }
          });
          return;
        }

        saga._hash = uuid().toString();

        var args = [sagaKey, JSON.stringify(saga)].concat(cmdMap);

        self.client.multi([['mset'].concat(args)]).exec(function (err, replies) {
          if (err) {
            debug(err);
            if (callback) {
              callback(err);
            }
            return;
          }
          if (!replies || replies.length === 0 || _.find(replies, function (r) { return (r !== 'OK' && r !== 1); })) {
            var err = new ConcurrencyError();
            debug(err);
            if (callback) {
              callback(err);
            }
            return;
          }
          if (callback) {
            callback(null);
          }
        });
      });
    });
  },

  scan: function (key, cursor, handleKeys, callback) {
    var self = this;

    if (!callback) {
      callback = handleKeys;
      handleKeys = cursor;
      cursor = 0;
    }

    (function scanRecursive (curs) {
      self.client.scan(curs, 'match', key, function (err, res) {
        if (err) {
          return callback(err);
        }

        function next () {
          if (res[0] === '0') {
            callback(null);
          } else {
            scanRecursive(res[0]);
          }
        }

        if (res[1].length === 0) {
          return next();
        }

        handleKeys(res[1], function (err) {
          if (err) {
            return callback(err);
          }
          next();
        });
      });
    })(cursor);
  },

  get: function (id, callback) {
    if (!id || !_.isString(id)) {
      var err = new Error('Please pass a valid id!');
      debug(err);
      return callback(err);
    }

    var self = this;

    var allKeys = [];

    this.scan(this.options.prefix + '_saga:*:*:' + id,
      function (keys, fn) {
        allKeys = allKeys.concat(keys);
        fn();
      }, function (err) {
        if (err) {
          debug(err);
          if (callback) callback(err);
          return;
        }

        if (allKeys.length === 0) {
          if (callback) callback(null, null);
          return;
        }

        allKeys = _.sortBy(allKeys, function (s) {
          return s;
        });

        self.client.get(allKeys[0], function (err, saga) {
          if (err) {
            return callback(err);
          }

          if (!saga) {
            return callback(null, null);
          }

          try {
            saga = jsondate.parse(saga.toString());
          } catch (error) {
            if (callback) callback(err);
            return;
          }

          callback(null, saga);
        });
      }
    );
  },

  remove: function (id, callback) {
    if (!id || !_.isString(id)) {
      var err = new Error('Please pass a valid id!');
      debug(err);
      return callback(err);
    }

    var self = this;

    async.parallel([
      function (callback) {
        self.scan(self.options.prefix + '_saga:*:*:' + id,
          function (keys, fn) {
            async.each(keys, function (key, callback) {
              self.client.del(key, callback);
            }, fn);
          }, callback
        );
      },

      function (callback) {
        self.scan(self.options.prefix + '_command:' + id + ':*',
          function (keys, fn) {
            async.each(keys, function (key, callback) {
              self.client.del(key, callback);
            }, fn);
          }, callback
        );
      }
    ], function (err) {
      if (err) {
        debug(err);
      }
      if (callback) callback(err);
    });
  },

  getTimeoutedSagas: function (options, callback) {
    if (!callback) {
      callback = options;
      options = {};
    }
    options = options || {};
    options.limit = options.limit || -1;
    options.skip = options.skip || 0;

    var res = [];
    var self = this;

    var allKeys = [];

    this.scan(this.options.prefix + '_saga:*:*:*',
      function (keys, fn) {
        allKeys = allKeys.concat(keys);
        fn();
      }, function (err) {
        if (err) {
          debug(err);
          if (callback) callback(err);
          return;
        }

        if (allKeys.length === 0) {
          return callback(null, res);
        }

        allKeys = _.sortBy(allKeys, function (s) {
          return s;
        });

        if (options.limit === -1) {
          allKeys = allKeys.slice(options.skip);
        }
        else {
          allKeys = allKeys.slice(options.skip, options.skip + options.limit);
        }

        if (allKeys.length === 0) {
          return callback(null, []);
        }

        async.each(allKeys, function (key, callback) {
          var parts = key.split(':');
          var prefix = parts[0];
          var commitStampMs = parts[1];
          var timeoutAtMs = parts[2];
          var sagaId = parts[3];

          if (commitStampMs === 'Infinity') {
            commitStampMs = Infinity;
          }
          if (_.isString(commitStampMs)) {
            commitStampMs = parseInt(commitStampMs, 10);
          }

          if (timeoutAtMs === 'Infinity') {
            timeoutAtMs = Infinity;
          }
          if (_.isString(timeoutAtMs)) {
            timeoutAtMs = parseInt(timeoutAtMs, 10);
          }

          if (timeoutAtMs > (new Date()).getTime()) {
            return callback(null);
          }

          self.get(sagaId, function (err, saga) {
            if (err) {
              return callback(err);
            }
            if (saga) {
              res.push(saga);
            }
            callback(null);
          });

        }, function (err) {
          if (err) {
            return callback(err);
          }
          callback(null, res);
        });
      }
    );
  },

  getOlderSagas: function (date, callback) {
    if (!date || !_.isDate(date)) {
      var err = new Error('Please pass a valid date object!');
      debug(err);
      return callback(err);
    }

    var res = [];
    var self = this;

    var allKeys = [];

    this.scan(this.options.prefix + '_saga:*:*:*',
      function (keys, fn) {
        allKeys = allKeys.concat(keys);
        fn();
      }, function (err) {
        if (err) {
          debug(err);
          if (callback) callback(err);
          return;
        }

        if (allKeys.length === 0) {
          return callback(null, res);
        }

        allKeys = _.sortBy(allKeys, function (s) {
          return s;
        });

        async.each(allKeys, function (key, callback) {
          var parts = key.split(':');
          var prefix = parts[0];
          var commitStampMs = parts[1];
          var timeoutAtMs = parts[2];
          var sagaId = parts[3];

          if (commitStampMs === 'Infinity') {
            commitStampMs = Infinity;
          }
          if (_.isString(commitStampMs)) {
            commitStampMs = parseInt(commitStampMs, 10);
          }

          if (timeoutAtMs === 'Infinity') {
            timeoutAtMs = Infinity;
          }
          if (_.isString(timeoutAtMs)) {
            timeoutAtMs = parseInt(timeoutAtMs, 10);
          }

          if (commitStampMs > date.getTime()) {
            return callback(null);
          }

          self.get(sagaId, function (err, saga) {
            if (err) {
              return callback(err);
            }
            if (saga) {
              res.push(saga);
            }
            callback(null);
          });

        }, function (err) {
          if (err) {
            return callback(err);
          }
          callback(null, res);
        });
      }
    );
  },

  getUndispatchedCommands: function (options, callback) {
    if (!callback) {
      callback = options;
      options = {};
    }
    options = options || {};
    options.limit = options.limit || -1;
    options.skip = options.skip || 0;

    var res = [];
    var self = this;

    var allKeys = [];

    this.scan(this.options.prefix + '_command:*:*',
      function (keys, fn) {
        allKeys = allKeys.concat(keys);
        fn();
      }, function (err) {
        if (err) {
          debug(err);
          if (callback) callback(err);
          return;
        }

        allKeys = _.sortBy(allKeys, function (s) {
          return s;
        });

        if (options.limit === -1) {
          allKeys = allKeys.slice(options.skip);
        }
        else {
          allKeys = allKeys.slice(options.skip, options.skip + options.limit);
        }

        if (allKeys.length === 0) {
          return callback(null, []);
        }

        async.each(allKeys, function (key, callback) {
          self.client.get(key, function (err, data) {
            if (err) {
              return callback(err);
            }

            if (!data) {
              return callback(null);
            }

            try {
              data = jsondate.parse(data.toString());
            } catch (error) {
              return callback(err);
            }

            res.push({ sagaId: data._sagaId, commandId: data._commandId, command: data, commitStamp: data._commitStamp });
            callback(null);
          });
        }, function (err) {
          if (err) {
            debug(err);
          }
          if (callback) callback(err, res);
        });
      }
    );
  },

  setCommandToDispatched: function (cmdId, sagaId, callback) {
    if (!cmdId || !_.isString(cmdId)) {
      var err = new Error('Please pass a valid command id!');
      debug(err);
      return callback(err);
    }

    if (!sagaId || !_.isString(sagaId)) {
      var err = new Error('Please pass a valid saga id!');
      debug(err);
      return callback(err);
    }

    this.client.del(this.options.prefix + '_command:' + sagaId + ':' + cmdId, function (err) {
      if (callback) callback(err);
    });
  },

  clear: function (callback) {
    var self = this;
    async.parallel([
      function (callback) {
        self.client.del('nextItemId:' + self.options.prefix, callback);
      },
      function (callback) {
        self.client.keys(self.options.prefix + '_saga:*', function(err, keys) {
          if (err) {
            return callback(err);
          }
          async.each(keys, function (key, callback) {
            self.client.del(key, callback);
          }, callback);
        });
      },
      function (callback) {
        self.client.keys(self.options.prefix + '_command:*', function(err, keys) {
          if (err) {
            return callback(err);
          }
          async.each(keys, function (key, callback) {
            self.client.del(key, callback);
          }, callback);
        });
      }
    ], function (err) {
      if (err) {
        debug(err);
      }
      if (callback) callback(err);
    });
  }

});

module.exports = Redis;
```

## File: `lib/structure/customLoader.js`
```javascript
var definitions = {
  Saga: require('./../definitions/saga')
};

module.exports = function (loader) {
  return function(sagaPath, callback) {
    var options = {
      sagaPath: sagaPath,
      definitions: definitions,
    };

    var tree;
    try {
      var tree = loader(options);
    } catch(e) {
      return callback(e);
    }

    return callback(null, tree);
  }
}
```

## File: `lib/structure/structureLoader.js`
```javascript
var debug = require('debug')('saga:structureLoader'),
  path = require('path'),
  _ = require('lodash'),
  structureParser = require('./structureParser'),
  Saga = require('./../definitions/saga');

function isSaga (item) {
  if (item.fileType !== 'js') {
    return false;
  }

  return item.value instanceof Saga;
}

function defineName (item) {
  var name = item.value.name;

  function defineNameByDir () {
    if (!name) {
      var splits = item.dottiedBase.split('.');
      name = splits[splits.length - 1];
    }
  }

  function defineNameByFileName () {
    if (!name) {
      name = item.fileName.substring(0, item.fileName.lastIndexOf('.'));
    }
  }

  defineNameByFileName();
  defineNameByDir();

  item.name = name;
}

function scan (items) {
  var res = [];

  items.forEach(function (item) {
    if (isSaga(item)) {
      debug('found saga at: ' + item.path);
      defineName(item);
      item.value.name = item.name;
      res.push(item.value);
      res = _.sortBy(res, function(s) {
        return s.priority;
      });
    }
  });

  return res;
}

function analyze (dir, callback) {
  structureParser(dir, function (items) {
    return _.filter(items, function (i) {
      return isSaga(i);
    });
  }, function (err, items, warns) {
    if (err) {
      return callback(err);
    }

    var res = scan(items);

    callback(null, res, warns);
  });
}

function load (dir, callback) {
  analyze(dir, function (err, sagas, warns) {
    if (err) {
      return callback(err);
    }

    callback(err, sagas, warns);
  });
}

module.exports = load;
```

## File: `lib/structure/structureParser.js`
```javascript
var debug = require('debug')('saga:structureParser'),
  _ = require('lodash'),
  fs = require('fs'),
  path = require('path');

var validFileTypes = ['js'];

function isValidFileType(fileName) {
  var index = fileName.lastIndexOf('.');
  if (index < 0) {
    return false;
  }
  var fileType = fileName.substring(index + 1);
  index = validFileTypes.indexOf(fileType);
  if (index < 0) {
    return false;
  }
  return validFileTypes[index];
}

function loadPaths (dir, callback) {
  dir = path.resolve(dir);

  var results = [];
  fs.readdir(dir, function (err, list) {
    if (err) {
      debug(err);
      return callback(err);
    }

    var pending = list.length;

    if (pending === 0) return callback(null, results);

    list.forEach(function (file) {
      var pathFull = path.join(dir, file);
      fs.stat(pathFull, function(err, stat) {
        if (err) {
          return debug(err);
        }

        // if directory, go deep...
        if (stat && stat.isDirectory()) {
          loadPaths(pathFull, function (err, res) {
            results = results.concat(res);
            if (!--pending) callback(null, results);
          });
          return;
        }

        // if a file we are looking for
        if (isValidFileType(pathFull)) {
          results.push(pathFull);
        }

        // of just an other file, skip...
        if (!--pending) callback(null, results);
      });
    });
  });
}

function pathToJson (root, paths, addWarning) {
  root = path.resolve(root);
  var res = [];

  paths.forEach(function (p) {
    if (p.indexOf(root) >= 0) {
      var part = p.substring(root.length);
      if (part.indexOf(path.sep) === 0) {
        part = part.substring(path.sep.length);
      }

      var splits = part.split(path.sep);
      var withoutFileName = splits;
      withoutFileName.splice(splits.length - 1);
      var fileName = path.basename(part);

      var dottiedBase = '';
      withoutFileName.forEach(function (s, i) {
        if (i + 1 < withoutFileName.length) {
          dottiedBase += s + '.';
        } else {
          dottiedBase += s;
        }
      });

      try {
        var required = require(p);

//        // clean cache, fixes multiple loading of same aggregates, commands, etc...
//        if (require.cache[require.resolve(p)]) {
//          delete require.cache[require.resolve(p)];
//        }

        if (!required || _.isEmpty(required)) {
          return;
        }

        if (typeof required === 'object' && typeof required.default !== 'undefined') {
          required = required.default;
        }

        if (_.isArray(required)) {
          _.each(required, function (req) {
            res.push({
              path: p,
              dottiedBase: dottiedBase,
              fileName: fileName,
              value: req,
              fileType: path.extname(p).substring(1)
            });
          });
        } else {
          res.push({
            path: p,
            dottiedBase: dottiedBase,
            fileName: fileName,
            value: required,
            fileType: path.extname(p).substring(1)
          });
        }
      } catch (err) {
        debug(err);
        if (addWarning) {
          addWarning(err);
        }
      }
    } else {
      debug('path is not a subpath from root');
    }
  });

  return res;
}

function parse (dir, filter, callback) {
  if (!callback) {
    callback = filter;
    filter = function (r) {
      return r;
    };
  }

  dir = path.resolve(dir);
  loadPaths(dir, function (err, paths) {
    if (err) {
      return callback(err);
    }

    var warns = [];
    function addWarning (e) {
      warns.push(e);
    }

    var res = filter(pathToJson(dir, paths, addWarning));

    var dottiesParts = [];

    res.forEach(function (r) {
      var parts = r.dottiedBase.split('.');
      parts.forEach(function (p, i) {
        if (!dottiesParts[i]) {
          return dottiesParts[i] = [p];
        }

        if (dottiesParts[i].indexOf(p) < 0) {
          dottiesParts[i].push(p);
        }
      });
    });

    var toRemove = '';

    for (var pi = 0, plen = dottiesParts.length; pi < plen; pi++) {
      if (dottiesParts[pi].length === 1) {
        toRemove += dottiesParts[pi][0];
      } else {
        break;
      }
    }

    if (toRemove.length > 0) {
      res.forEach(function (r) {
        if (r.dottiedBase === toRemove) {
          r.dottiedBase = '';
        } else {
          r.dottiedBase = r.dottiedBase.substring(toRemove.length + 1);
        }
      });
    }

    if (warns.length === 0) {
      warns = null;
    }

    callback(null, res, warns);
  });
}

module.exports = parse;
```

## File: `lib/structure/structureSearcher.js`
```javascript
var debug = require('debug')('saga:structureSearcher'),
  _ = require('lodash');

module.exports = function (sagas) {

  if (!sagas || _.isEmpty(sagas)) {
    debug('no sagas injected');
  }

  return {

    getInfo: function () {
      if (!sagas || _.isEmpty(sagas)) {
        debug('no sagas injected');
        return null;
      }

      var info = {
        sagas: []
      };

      sagas.forEach(function (s) {
        info.sagas.push({
          name: s.name,
          aggregate: s.aggregate,
          context: s.context,
          version: s.version
        });
      });

      return info;
    },

    getSagas: function (query) {
      if (!sagas || _.isEmpty(sagas)) {
        debug('no sagas injected');
        return null;
      }

      var res = _.filter(sagas, function (s) {
        var isNameEqual = s.name === query.name;
        var isVersionEqual = s.version === query.version;
        var isAggregateEqual = s.aggregate === query.aggregate;
        var isContextEqual = s.context === query.context;

        return isNameEqual && isVersionEqual && isAggregateEqual && isContextEqual;
      });

      return res;
    },

    defineOptions: function (options) {
      if (!sagas || _.isEmpty(sagas)) {
        debug('no sagas injected');
        return this;
      }

      sagas.forEach(function (s) {
        s.defineOptions(options);
      });

      return this;
    },

    defineCommand: function (definition) {
      if (!sagas || _.isEmpty(sagas)) {
        debug('no sagas injected');
        return this;
      }

      sagas.forEach(function (s) {
        s.defineCommand(definition);
      });

      return this;
    },

    defineEvent: function (definition) {
      if (!sagas || _.isEmpty(sagas)) {
        debug('no sagas injected');
        return this;
      }

      sagas.forEach(function (s) {
        s.defineEvent(definition);
      });

      return this;
    },

    useSagaStore: function (sagaStore) {
      if (!sagaStore || _.isEmpty(sagaStore)) {
        debug('no sagaStore injected');
        return this;
      }

      sagas.forEach(function (s) {
        s.useSagaStore(sagaStore);
      });
      return this;
    },

    idGenerator: function (getNewId) {
      if (!getNewId || !_.isFunction(getNewId)) {
        var err = new Error('Please pass a valid function!');
        debug(err);
        throw err;
      }

      if (!sagas || _.isEmpty(sagas)) {
        debug('no sagas injected');
        return this;
      }

      sagas.forEach(function (s) {
        s.idGenerator(getNewId);
      });

      return this;
    }

  };

};
```

## File: `test/.eslintrc`
```
{
  "env": {
    "browser": false,
    "node": true
  },
  "rules": {
    "no-underscore-dangle": 0,
    "camelcase": 1,
    "no-global-strict": 2,
    "strict": 0,
    "quotes": [2, "single"],
    "if-curly-formatting": 0,
    "no-console": 0,
    "no-undef": 1,
    "no-mixed-requires": 0
  },
  "globals": {
    "describe": false,
    "it": false,
    "before": false,
    "beforeEach": false,
    "afterEach": false
  }
}
```

## File: `test/mocha.opts`
```
-R spec -t 10000
```

## File: `test/integration/integrationTest.js`
```javascript
var expect = require('expect.js'),
  api = require('../../index');

describe('integration', function () {

  var pm;

  before(function (done) {
    pm = api({ sagaPath: __dirname + '/fixture' });
    pm.defineCommand({
      id: 'id',
      meta: 'meta'
    });
    pm.defineEvent({
      name: 'name',
      context: 'context.name',
      aggregate: 'aggregate.name',
      aggregateId: 'aggregate.id',
      revision: 'aggregate.revision',
      version: 'version',
      meta: 'meta'
    });

    expect(function () {
      pm.getInfo();
    }).to.throwError('/init');

    pm.init(function (err, warns) {
      expect(warns).not.to.be.ok();
      done(err);
    });
  });

  describe('requesting information', function () {

    it('it should return the expected information', function () {

      var info = pm.getInfo();
      expect(info.sagas.length).to.eql(4);
      expect(info.sagas[0].name).to.eql('orderConfirmed');
      expect(info.sagas[0].aggregate).to.eql('order');
      expect(info.sagas[0].context).to.eql('sale');
      expect(info.sagas[0].version).to.eql(0);
      expect(info.sagas[1].name).to.eql('orderCreated');
      expect(info.sagas[1].aggregate).to.eql('order');
      expect(info.sagas[1].context).to.eql('sale');
      expect(info.sagas[1].version).to.eql(0);
      expect(info.sagas[2].name).to.eql('paymentAccepted');
      expect(info.sagas[2].aggregate).to.eql('payment');
      expect(info.sagas[2].context).to.eql('sale');
      expect(info.sagas[2].version).to.eql(2);
      expect(info.sagas[3].name).to.eql('seatsReserved');
      expect(info.sagas[3].aggregate).to.eql('reservation');
      expect(info.sagas[3].context).to.eql('sale');
      expect(info.sagas[3].version).to.eql(0);

    });

  });

  describe('handling an event that will not be handled', function () {

    it('it should not publish any command and it should callback without an error and without commands', function (done) {

      var publishedCommands = [];

      pm.onCommand(function (cmd) {
        publishedCommands.push(cmd);
      });

      var evt = {
        name: 'evtName',
        aggregate: {
          name: 'aggregate'
        },
        context: {
          name: 'context'
        },
        version: 0,
        meta: {
          userId: 'userId'
        }
      };

      pm.handle(evt, function (err, cmds, sagaModels) {
        expect(err).not.to.be.ok();
        expect(cmds).to.be.an('array');
        expect(cmds.length).to.eql(0);
        expect(sagaModels).to.be.an('array');
        expect(sagaModels.length).to.eql(0);
        expect(publishedCommands.length).to.eql(0);

        done();
      });

    });

  });

  describe('handling an event that will be handled but will use only an already existing saga', function () {

    it('it should not publish any command and it should callback without an error and without commands', function (done) {

      var publishedCommands = [];

      pm.onCommand(function (cmd) {
        publishedCommands.push(cmd);
      });

      var evt = {
        name: 'paymentAccepted',
        aggregate: {
          name: 'payment'
        },
        context: {
          name: 'sale'
        },
        version: 2,
        payload: {
          transactionId: 'not_existing_64412467'
        },
        meta: {
          userId: 'userId'
        }
      };

      pm.handle(evt, function (err, cmds, sagaModels) {
        expect(err).not.to.be.ok();
        expect(cmds).to.be.an('array');
        expect(cmds.length).to.eql(0);
        expect(sagaModels).to.be.an('array');
        expect(sagaModels.length).to.eql(0);
        expect(publishedCommands.length).to.eql(0);

        done();
      });

    });

  });

  describe('handling an event that will start a new saga', function () {

    var transactionId;

    it('it should publish a command and it should callback without an error and with commands', function (done) {

      var publishedCommands = [];

      pm.onCommand(function (cmd) {
        publishedCommands.push(cmd);
      });

      var evt = {
        name: 'orderCreated',
        aggregate: {
          name: 'order',
          id: 'orderAggId',
          revision: 1
        },
        context: {
          name: 'sale'
        },
        version: 0,
        payload: {
          totalCosts: 520,
          seats: ['4f', '8a']
        },
        meta: {
          userId: 'userId'
        }
      };

      pm.handle(evt, function (err, cmds, sagaModels) {
        expect(err).not.to.be.ok();
        expect(cmds).to.be.an('array');
        expect(cmds.length).to.eql(1);
        expect(cmds[0].id).to.be.a('string');
        expect(cmds[0].name).to.eql('makeReservation');
        expect(cmds[0].payload.seats).to.eql(evt.payload.seats);
        expect(cmds[0].payload.transactionId).to.be.a('string');

        transactionId = cmds[0].payload.transactionId;

        expect(cmds[0].meta).to.eql(evt.meta);
        expect(sagaModels).to.be.an('array');
        expect(sagaModels.length).to.eql(1);
        expect(sagaModels[0].getTimeoutAt()).to.be.a(Date);
        expect(sagaModels[0].getTimeoutCommands()).to.be.an('array');
        expect(sagaModels[0].getTimeoutCommands().length).to.eql(1);
        expect(sagaModels[0].getTimeoutCommands()[0].id).to.be.a('string');
        expect(sagaModels[0].getTimeoutCommands()[0].name).to.eql('cancelOrder');
        expect(sagaModels[0].getTimeoutCommands()[0].payload.transactionId).to.eql(cmds[0].payload.transactionId);
        expect(sagaModels[0].getTimeoutCommands()[0].meta).to.eql(evt.meta);
        expect(publishedCommands.length).to.eql(1);
        expect(publishedCommands[0].id).to.be.a('string');
        expect(publishedCommands[0].name).to.eql('makeReservation');
        expect(publishedCommands[0].payload.seats).to.eql(evt.payload.seats);
        expect(publishedCommands[0].payload.transactionId).to.be.a('string');
        expect(publishedCommands[0].meta).to.eql(evt.meta);

        done();
      });

    });

    describe('continue with the next step', function () {

      it('it should publish a command and it should callback without an error and with commands', function (done) {

        var publishedCommands = [];

        pm.onCommand(function (cmd) {
          publishedCommands.push(cmd);
        });

        var evt = {
          name: 'seatsReserved',
          aggregate: {
            name: 'reservation',
            id: 'seatsAggId',
            revision: 1
          },
          context: {
            name: 'sale'
          },
          version: 0,
          payload: {
            transactionId: transactionId
          },
          meta: {
            userId: 'userId'
          }
        };

        pm.handle(evt, function (err, cmds, sagaModels) {
          expect(err).not.to.be.ok();
          expect(cmds).to.be.an('array');
          expect(cmds.length).to.eql(1);
          expect(cmds[0].id).to.be.a('string');
          expect(cmds[0].name).to.eql('makePayment');
          expect(cmds[0].payload.costs).to.eql(520);
          expect(cmds[0].payload.transactionId).to.be.a('string');
          expect(cmds[0].meta).to.eql(evt.meta);
          expect(sagaModels).to.be.an('array');
          expect(sagaModels.length).to.eql(1);
          expect(sagaModels[0].getTimeoutAt()).to.be.a(Date);
          expect(sagaModels[0].getTimeoutCommands()).to.be.an('array');
          expect(sagaModels[0].getTimeoutCommands().length).to.eql(1);
          expect(sagaModels[0].getTimeoutCommands()[0].id).to.be.a('string');
          expect(sagaModels[0].getTimeoutCommands()[0].name).to.eql('cancelOrder');
          expect(sagaModels[0].getTimeoutCommands()[0].payload.transactionId).to.eql(cmds[0].payload.transactionId);
          expect(sagaModels[0].getTimeoutCommands()[0].meta).to.eql(evt.meta);
          expect(publishedCommands.length).to.eql(1);
          expect(publishedCommands[0].id).to.be.a('string');
          expect(publishedCommands[0].name).to.eql('makePayment');
          expect(publishedCommands[0].payload.costs).to.eql(520);
          expect(publishedCommands[0].payload.transactionId).to.be.a('string');
          expect(publishedCommands[0].meta).to.eql(evt.meta);

          done();
        });

      });

      describe('continue with the next step that will remove the timeout', function () {

        it('it should publish a command and it should callback without an error and with commands', function (done) {

          var publishedCommands = [];

          pm.onCommand(function (cmd) {
            publishedCommands.push(cmd);
          });

          var evt = {
            name: 'paymentAccepted',
            aggregate: {
              name: 'payment',
              id: 'payAggId',
              revision: 1
            },
            context: {
              name: 'sale'
            },
            version: 2,
            payload: {
              transactionId: transactionId
            },
            meta: {
              userId: 'userId'
            }
          };

          pm.handle(evt, function (err, cmds, sagaModels) {
            expect(err).not.to.be.ok();
            expect(cmds).to.be.an('array');
            expect(cmds.length).to.eql(1);
            expect(cmds[0].id).to.be.a('string');
            expect(cmds[0].name).to.eql('confirmOrder');
            expect(cmds[0].aggregate.id).to.eql('orderAggId');
            expect(cmds[0].payload.transactionId).to.be.a('string');
            expect(cmds[0].meta).to.eql(evt.meta);
            expect(sagaModels).to.be.an('array');
            expect(sagaModels.length).to.eql(1);
            expect(sagaModels[0].getTimeoutAt()).to.eql(undefined);
            expect(sagaModels[0].getTimeoutCommands()).to.eql(undefined);
            expect(publishedCommands.length).to.eql(1);
            expect(publishedCommands[0].id).to.be.a('string');
            expect(publishedCommands[0].name).to.eql('confirmOrder');
            expect(publishedCommands[0].aggregate.id).to.eql('orderAggId');
            expect(publishedCommands[0].payload.transactionId).to.be.a('string');
            expect(publishedCommands[0].meta).to.eql(evt.meta);

            done();
          });

        });

        describe('continue with the last step', function () {

          it('it should not publish any command and it should callback without an error and without commands', function (done) {

            var publishedCommands = [];

            pm.onCommand(function (cmd) {
              publishedCommands.push(cmd);
            });

            var evt = {
              name: 'orderConfirmed',
              aggregate: {
                name: 'order',
                id: 'orderAggId',
                revision: 2
              },
              context: {
                name: 'sale'
              },
              version: 0,
              payload: {
                transactionId: transactionId
              },
              meta: {
                userId: 'userId'
              }
            };

            pm.handle(evt, function (err, cmds, sagaModels) {
              expect(err).not.to.be.ok();
              expect(cmds).to.be.an('array');
              expect(cmds.length).to.eql(0);
              expect(sagaModels).to.be.an('array');
              expect(sagaModels.length).to.eql(1);
              expect(sagaModels[0].isDestroyed()).to.eql(true);
              expect(sagaModels[0].getTimeoutAt()).to.eql(undefined);
              expect(sagaModels[0].getTimeoutCommands()).to.eql(undefined);
              expect(publishedCommands.length).to.eql(0);

              done();
            });

          });

          describe('handling an event that was already handled', function () {

            it('it should not publish anything and callback with an error', function (done) {

              var publishedCommands = [];

              pm.onCommand(function (cmd) {
                publishedCommands.push(cmd);
              });

              var evt = {
                name: 'seatsReserved',
                aggregate: {
                  name: 'reservation',
                  id: 'seatsAggId',
                  revision: 1
                },
                context: {
                  name: 'sale'
                },
                version: 0,
                payload: {
                  transactionId: transactionId
                },
                meta: {
                  userId: 'userId'
                }
              };

              pm.handle(evt, function (errs, cmds, sagaModels) {
                expect(errs).to.be.ok();
                expect(errs.length).to.eql(1);
                expect(errs[0].name).to.eql('AlreadyHandledError');
                expect(cmds).not.to.be.ok();
                expect(sagaModels).not.to.be.ok();

                expect(publishedCommands.length).to.eql(0);

                pm.getLastEvent(function (err, evt) {
                  expect(err).not.be.ok();
                  expect(evt.aggregate.revision).to.eql(2);
                  done();
                });
              });

            });

          });

        });

      });

    });

  });

});
```

## File: `test/integration/mocha.opts`
```
-R spec
```

## File: `test/integration/fixture/order/orderConfirmed.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-saga').defineSaga({// event to match..
module.exports = require('../../../../').defineSaga({// event to match...
  name: 'orderConfirmed', // optional, default is file name without extension
  aggregate: 'order',
  context: 'sale',
  containingProperties: ['payload.transactionId'],
  id: 'payload.transactionId',
  existing: true, // if true it will check if there is already a saga in the db and only if there is something it will continue...
  // payload: 'payload' // if not defined it will pass the whole event...
  priority: 1 // optional, default Infinity, all sagas will be sorted by this value
}, function (evt, saga, callback) {

  saga.destroy();
  saga.commit(callback);

});
```

## File: `test/integration/fixture/order/orderCreated.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-saga').defineSaga({// event to match..
module.exports = require('../../../../').defineSaga({// event to match...
//  name: 'orderCreated', // optional, default is file name without extension
  aggregate: 'order',
  context: 'sale',
  existing: false, // if true it will check if there is already a saga in the db and only if there is something it will continue...
  containingProperties: ['aggregate.id', 'payload.totalCosts', 'payload.seats'],
  // payload: 'payload' // if not defined it will pass the whole event...
  // id: 'aggregate.id' // if not defined it will generate an id
  priority: 2 // optional, default Infinity, all sagas will be sorted by this value
}, function (evt, saga, callback) {

  // saga.id or saga.get('id') is a generated id...

  saga.set('orderId', evt.aggregate.id);
  saga.set('totalCosts', evt.payload.totalCosts);

  var cmd = {
    // id: 'my own command id', // if you don't pass an id it will generate one, when emitting the command...
    name: 'makeReservation',
    aggregate: {
      name: 'reservation'
    },
    context: {
      name: 'sale'
    },
    payload: {
      transactionId: saga.id,
      seats: evt.payload.seats
    }//,
//    meta: evt.meta // to transport userId...   if not defined in cmd, it will defaultly use it from event
  };

  saga.addCommandToSend(cmd);

  // timeout stuff  (optional)
  var tomorrow = new Date();
  tomorrow.setDate((new Date()).getDate() + 1);
  var timeoutCmd = {
    // id: 'my own command id', // if you don't pass an id it will generate one, when emitting the command...
    name: 'cancelOrder',
    aggregate: {
      name: 'order',
      id: evt.aggregate.id
    },
    context: {
      name: 'sale'
    },
    payload: {
      transactionId: saga.id
    }//,
//    meta: evt.meta // to transport userId...   if not defined in cmd, it will defaultly use it from event
  };
  saga.defineTimeout(tomorrow, [timeoutCmd]); // pass in array of commands or a command object

  saga.commit(callback);
});
```

## File: `test/integration/fixture/order/paymentAccepted.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-saga').defineSaga({// event to match..
module.exports = require('../../../../').defineSaga({// event to match...
  name: 'paymentAccepted', // optional, default is file name without extension
  aggregate: 'payment',
  context: 'sale',
  version: 2, // default is 0
  containingProperties: ['payload.transactionId'],
  id: 'payload.transactionId',
  existing: true, // if true it will check if there is already a saga in the db and only if there is something it will continue...
  // payload: 'payload' // if not defined it will pass the whole event...
  priority: 3 // optional, default Infinity, all sagas will be sorted by this value
}, function (evt, saga, callback) {

  var cmd = {
    // id: 'my own command id', // if you don't pass an id it will generate one, when emitting the command...
    name: 'confirmOrder',
    aggregate: {
      name: 'order',
      id: saga.get('orderId')
    },
    context: {
      name: 'sale'
    },
    payload: {
      transactionId: saga.id
    },
    meta: evt.meta // to transport userId...   if not defined in cmd, it will defaultly use it from event
  };

  saga.removeTimeout();

  saga.addCommandToSend(cmd);

  saga.commit(callback);
});
```

## File: `test/integration/fixture/order/seatsReserved.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-saga').defineSaga({// event to match..
module.exports = require('../../../../').defineSaga({// event to match...
  name: 'seatsReserved', // optional, default is file name without extension
  aggregate: 'reservation',
  context: 'sale',
  containingProperties: ['payload.transactionId'],
  id: 'payload.transactionId',
  existing: true, // if true it will check if there is already a saga in the db and only if there is something it will continue...
  // payload: 'payload' // if not defined it will pass the whole event...
  priority: 4 // optional, default Infinity, all sagas will be sorted by this value
}, function (evt, saga, callback) {

  var cmd = {
    // id: 'my own command id', // if you don't pass an id it will generate one, when emitting the command...
    name: 'makePayment',
    aggregate: {
      name: 'payment'
    },
    context: {
      name: 'sale'
    },
    payload: {
      transactionId: saga.id,
      costs: saga.get('totalCosts')
    },
    meta: evt.meta // to transport userId...   if not defined in cmd, it will defaultly use it from event
  };

  saga.addCommandToSend(cmd);

  saga.commit(callback);
});
```

## File: `test/unit/eventDispatcherTest.js`
```javascript
var expect = require('expect.js'),
  EventDispatcher = require('../../lib/eventDispatcher');

describe('eventDispatcher', function () {

  describe('creating a new instance', function () {

    describe('without tree argument', function () {

      it('it should throw an error', function () {

        expect(function () {
          new EventDispatcher();
        }).to.throwError(/tree/);

      });

    });

    describe('without definition argument', function () {

      it('it should throw an error', function () {

        expect(function () {
          new EventDispatcher({ getSagas: function () {} });
        }).to.throwError(/definition/);

      });

    });

    describe('with all correct arguments', function () {

      it('it should not throw an error', function () {

        expect(function () {
          new EventDispatcher({ getSagas: function () {} }, {});
        }).not.to.throwError();

      });

      describe('calling getTargetInformation', function () {

        describe('without event argument', function () {

          it('it should throw an error', function () {

            var evtDisp = new EventDispatcher({ getSagas: function () {} }, {});
            expect(function () {
              evtDisp.getTargetInformation();
            }).to.throwError(/event/);

          });

        });

        describe('with event argument', function () {

          it('it should not throw an error', function () {

            var evtDisp = new EventDispatcher({ getSagas: function () {} }, {});
            expect(function () {
              evtDisp.getTargetInformation({});
            }).not.to.throwError();

          });

          describe('passing a definition with all infos', function () {

            it('it should return the correct target infos', function () {

              var evtDisp = new EventDispatcher({ getSagas: function () {} }, { name: 'evtName', version: 'v', aggregate: 'agg', context: 'ctx' });
              var target = evtDisp.getTargetInformation({ evtName: 'evtNameSpec', v: 3, agg: 'aggName', ctx: 'myCtx' });
              expect(target.name).to.eql('evtNameSpec');
              expect(target.version).to.eql(3);
              expect(target.aggregate).to.eql('aggName');
              expect(target.context).to.eql('myCtx');

            });

          });

          describe('passing a definition with less infos', function () {

            it('it should return the correct target infos', function () {

              var evtDisp = new EventDispatcher({ getSagas: function () {} }, { name: 'evtName' });
              var target = evtDisp.getTargetInformation({ evtName: 'evtNameSpec' });
              expect(target.name).to.eql('evtNameSpec');
              expect(target.version).to.eql(0);

            });

          });

        });

      });

      describe('calling dispatch', function () {

        describe('with no matching saga', function () {

          it('it should callback without an error', function (done) {

            var evtDisp = new EventDispatcher({ getSagas: function () {
              return null;
            }}, { name: 'evtName' });
            evtDisp.dispatch({ evtName: 'evtNameSpec' }, function (err, sagaModels) {
              expect(err).not.to.be.ok();
              expect(sagaModels).to.be.an('array');
              expect(sagaModels.length).to.eql(0);
              done();
            });

          });

        });

        describe('with matching saga', function () {

          it('it should call his handle function', function (done) {

            var calledBack1 = false;
            var calledBack2 = false;
            var evtDisp = new EventDispatcher({ getSagas: function () {
              return [{ handle: function (evt, clb) {
                expect(evt.evtName).to.eql('evtNameSpec');
                expect(clb).to.be.a('function');
                calledBack1 = true;
                clb(null);
              }},
              { handle: function (evt, clb) {
                expect(evt.evtName).to.eql('evtNameSpec');
                expect(clb).to.be.a('function');
                calledBack2 = true;
                clb(null);
              }}];
            }}, { name: 'evtName' });

            evtDisp.dispatch({ evtName: 'evtNameSpec' }, function (err) {
              expect(err).not.to.be.ok();
              expect(calledBack1).to.eql(true);
              expect(calledBack2).to.eql(true);
              done();
            });

          });

        });

      });

    });

  });

});
```

## File: `test/unit/mocha.opts`
```
-R spec
--recursive
```

## File: `test/unit/orderQueueTest.js`
```javascript
var expect = require('expect.js'),
  OrderQueue = require('../../lib/orderQueue');

describe('orderQueue', function () {

  describe('creating a new instance', function () {
    
    var queue;

    it('it should not throw an error', function () {

      expect(function () {
        queue = new OrderQueue({ queueTimeout: 50 });
        expect(queue.options.queueTimeout).to.eql(50);
      }).not.to.throwError();

    });

    describe('having a clean queue', function() {

      before(function () {
        queue.clear();
      });

      describe('calling get', function () {

        it('it should return null', function () {

          expect(function () {
            var res = queue.get('aggId1324234');
            expect(res).to.eql(null);
          }).not.to.throwError();

        });

      });

      describe('calling remove', function () {

        it('it should not throw an error', function () {

          expect(function () {
            queue.remove('aggId123', 'objId1234');
          }).not.to.throwError();

        });

      });

      describe('calling push', function () {

        it('it should work as expected', function () {

          expect(function () {
            function evtClb () {}
            function timeoutFn () {}
            queue.push('aggId5132', 'objId151452', { ev: 'ent' }, evtClb, timeoutFn);
            
            var res = queue.get('aggId5132');
            expect(res).to.be.an('array');
            expect(res.length).to.eql(1);
            expect(res[0].payload.ev).to.eql('ent');
            expect(res[0].callback).to.eql(evtClb);
            expect(res[0].id).to.eql('objId151452');
            
            queue.remove('aggId5132', 'wrong');
            var res = queue.get('aggId5132');
            expect(res).to.be.an('array');
            expect(res.length).to.eql(1);
            expect(res[0].payload.ev).to.eql('ent');
            expect(res[0].callback).to.eql(evtClb);
            expect(res[0].id).to.eql('objId151452');
            
            queue.remove('aggId5132', 'objId151452');
            var res = queue.get('aggId5132');
            expect(res).to.eql(null);  
          }).not.to.throwError();

        });
        
        describe('waiting too long before remove it', function () {
          
          it('it should work as expected', function (done) {

            function evtClb () {}
            var loopCounts = [];
            function timeoutFn (loopCount, wait) {
              loopCounts.push(loopCount);
              wait();
            }
            queue.push('aggId5132', 'objId151452', { ev: 'ent' }, evtClb, timeoutFn);
            setTimeout(function () {
              queue.remove('aggId5132', 'objId151452');
              
              setTimeout(function () {
                expect(loopCounts.length).to.eql(3);
                expect(loopCounts[0]).to.eql(1);
                expect(loopCounts[1]).to.eql(2);
                expect(loopCounts[2]).to.eql(3);
                done();
              }, 60);
            }, 160);
            
          });
          
        });

      });

    });

  });

});
```

## File: `test/unit/pmTest.js`
```javascript
var expect = require('expect.js'),
  api = require('../../index'),
  async = require('async'),
  _ = require('lodash');

describe('power management', function () {

  it('it should be a function', function () {

    expect(api).to.be.a('function');

  });

  it('it should have the correct api', function () {

    expect(api.defineSaga).to.be.a('function');

  });

  describe('calling that function', function () {

    describe('without options', function () {

      it('it should throw an error', function () {

        expect(api).to.throwError('/sagaPath/');

      });

    });

    describe('with all mandatory options', function () {

      it('it should return as expected', function () {

        var pm = api({ sagaPath: __dirname });
        expect(pm).to.be.a('object');
        expect(pm.on).to.be.a('function');
        expect(pm.structureLoader).to.be.a('function');        
        expect(pm.sagaStore).to.be.an('object');
        expect(pm.sagaStore.on).to.be.a('function');
        expect(pm.revisionGuardStore).to.be.an('object');
        expect(pm.revisionGuardStore.on).to.be.a('function');
        expect(pm.defineCommand).to.be.a('function');
        expect(pm.defineEvent).to.be.a('function');
        expect(pm.idGenerator).to.be.a('function');
        expect(pm.onCommand).to.be.a('function');
        expect(pm.onEventMissing).to.be.a('function');
        expect(pm.init).to.be.a('function');
        expect(pm.handle).to.be.a('function');
        expect(pm.getLastEvent).to.be.a('function');

        expect(pm.getTimeoutedSagas).to.be.a('function');
        expect(pm.getOlderSagas).to.be.a('function');
        expect(pm.getUndispatchedCommands).to.be.a('function');
        expect(pm.setCommandToDispatched).to.be.a('function');
        expect(pm.removeSaga).to.be.a('function');

        expect(pm.options.retryOnConcurrencyTimeout).to.eql(800);
        expect(pm.options.revisionGuard.queueTimeout).to.eql(1000);
        expect(pm.options.revisionGuard.queueTimeoutMaxLoops).to.eql(3);
      });

    });

    describe('with custom "structureLoader" method', function () {

      describe('creating an object of the wrong interface', function () {

        it('it should throw an error', function () {

          expect(function () {
            api({
              sagaPath: __dirname,
              structureLoader: {
              },
            })
          }).to.throwError('/structureLoader/');

        });
      });

      describe('creating an object of the right interface', function () {

        it('it should return as expected', function () {
          var pm = api({ 
            sagaPath: __dirname,
            structureLoader: function() {
            }
          });

          expect(pm).to.be.a('object');
          expect(pm.on).to.be.a('function');
          expect(pm.structureLoader).to.be.a('function');        
          expect(pm.sagaStore).to.be.an('object');
          expect(pm.sagaStore.on).to.be.a('function');
          expect(pm.revisionGuardStore).to.be.an('object');
          expect(pm.revisionGuardStore.on).to.be.a('function');
          expect(pm.defineCommand).to.be.a('function');
          expect(pm.defineEvent).to.be.a('function');
          expect(pm.idGenerator).to.be.a('function');
          expect(pm.onCommand).to.be.a('function');
          expect(pm.onEventMissing).to.be.a('function');
          expect(pm.init).to.be.a('function');
          expect(pm.handle).to.be.a('function');
          expect(pm.getLastEvent).to.be.a('function');
  
          expect(pm.getTimeoutedSagas).to.be.a('function');
          expect(pm.getOlderSagas).to.be.a('function');
          expect(pm.getUndispatchedCommands).to.be.a('function');
          expect(pm.setCommandToDispatched).to.be.a('function');
          expect(pm.removeSaga).to.be.a('function');
  
          expect(pm.options.retryOnConcurrencyTimeout).to.eql(800);
          expect(pm.options.revisionGuard.queueTimeout).to.eql(1000);
          expect(pm.options.revisionGuard.queueTimeoutMaxLoops).to.eql(3);
        });
      });
    });
    
    describe('defining an id generator function', function() {

      var pm;

      beforeEach(function () {
        pm = api({ sagaPath: __dirname });
        pm.getNewId = null;
      });

      describe('in a synchronous way', function() {

        it('it should be transformed internally to an asynchronous way', function(done) {

          pm.idGenerator(function () {
            var id = require('uuid').v4().toString();
            return id;
          });

          pm.getNewId(function (err, id) {
            expect(id).to.be.a('string');
            done();
          });

        });

      });

      describe('in an synchronous way', function() {

        it('it should be taken as it is', function(done) {

          pm.idGenerator(function (callback) {
            setTimeout(function () {
              var id = require('uuid').v4().toString();
              callback(null, id);
            }, 10);
          });

          pm.getNewId(function (err, id) {
            expect(id).to.be.a('string');
            done();
          });

        });

      });

    });

    describe('defining the command structure', function() {

      var domain;

      beforeEach(function () {
        domain = api({ sagaPath: __dirname });
      });

      describe('using the defaults', function () {

        it('it should apply the defaults', function() {

          var defaults = _.cloneDeep(domain.definitions.command);

          domain.defineCommand({
            meta: 'pass'
          });

          expect(defaults.id).to.eql(domain.definitions.command.id);
          expect(domain.definitions.command.meta).to.eql('pass');
          expect(defaults.meta).not.to.eql(domain.definitions.command.meta);

        });

      });

      describe('overwriting the defaults', function () {

        it('it should apply them correctly', function() {

          var defaults = _.cloneDeep(domain.definitions.command);

          domain.defineCommand({
            id: 'commandId',
            meta: 'pass'
          });

          expect(domain.definitions.command.id).to.eql('commandId');
          expect(defaults.id).not.to.eql(domain.definitions.command.id);
          expect(domain.definitions.command.meta).to.eql('pass');
          expect(defaults.meta).not.to.eql(domain.definitions.command.meta);

        });

      });

    });

    describe('defining the event structure', function() {

      var domain;

      beforeEach(function () {
        domain = api({ sagaPath: __dirname });
      });

      describe('using the defaults', function () {

        it('it should apply the defaults', function() {

          var defaults = _.cloneDeep(domain.definitions.event);

          domain.defineEvent({
            aggregate: 'aggName',
            context: 'ctx.Name',
            version: 'v.',
            meta: 'pass'
          });

          expect(defaults.id).to.eql(domain.definitions.event.id);
          expect(defaults.name).to.eql(domain.definitions.event.name);
          expect(domain.definitions.event.aggregate).to.eql('aggName');
          expect(defaults.aggregate).not.to.eql(domain.definitions.event.aggregate);
          expect(domain.definitions.event.context).to.eql('ctx.Name');
          expect(defaults.context).not.to.eql(domain.definitions.event.context);
          expect(domain.definitions.event.version).to.eql('v.');
          expect(defaults.version).not.to.eql(domain.definitions.event.version);
          expect(domain.definitions.event.meta).to.eql('pass');
          expect(defaults.meta).not.to.eql(domain.definitions.event.meta);

        });

      });

      describe('overwriting the defaults', function () {

        it('it should apply them correctly', function() {

          var defaults = _.cloneDeep(domain.definitions.event);

          domain.defineEvent({
            id: 'eventId',
            name: 'defName',
            aggregate: 'aggName',
            context: 'ctx.Name',
            version: 'v.',
            meta: 'pass'
          });


          expect(domain.definitions.event.id).to.eql('eventId');
          expect(defaults.id).not.to.eql(domain.definitions.event.id);
          expect(domain.definitions.event.name).to.eql('defName');
          expect(defaults.name).not.to.eql(domain.definitions.event.name);
          expect(domain.definitions.event.aggregate).to.eql('aggName');
          expect(defaults.aggregate).not.to.eql(domain.definitions.event.aggregate);
          expect(domain.definitions.event.context).to.eql('ctx.Name');
          expect(defaults.context).not.to.eql(domain.definitions.event.context);
          expect(domain.definitions.event.version).to.eql('v.');
          expect(defaults.version).not.to.eql(domain.definitions.event.version);
          expect(domain.definitions.event.meta).to.eql('pass');
          expect(defaults.meta).not.to.eql(domain.definitions.event.meta);

        });

      });

    });

    describe('defining onCommand handler', function () {

      var pm;

      beforeEach(function () {
        pm = api({ sagaPath: __dirname });
        pm.onCommandHandle = null;
      });

      describe('in a synchronous way', function() {

        it('it should be transformed internally to an asynchronous way', function(done) {

          var called = false;
          pm.onCommand(function (cmd) {
            expect(cmd.my).to.eql('cmd');
            called = true;
          });

          pm.onCommandHandle({ my: 'cmd' }, function (err) {
            expect(err).not.to.be.ok();
            expect(called).to.eql(true);
            done();
          });

        });

      });

      describe('in an synchronous way', function() {

        it('it should be taken as it is', function(done) {

          var called = false;
          pm.onCommand(function (cmd, callback) {
            setTimeout(function () {
              expect(cmd.my).to.eql('cmd');
              called = true;
              callback(null);
            }, 10);
          });

          pm.onCommandHandle({ my: 'cmd' }, function (err) {
            expect(err).not.to.be.ok();
            expect(called).to.eql(true);
            done();
          });

        });

      });

    });

    describe('defining onEventMissing handler', function () {

      var pm;

      beforeEach(function () {
        pm = api({ sagaPath: __dirname });
        pm.onEventMissingHandle = null;
      });

      it('it should work as expected', function() {

        var called = false;
        pm.onEventMissing(function (info, evt) {
          expect(info.in).to.eql('fo');
          expect(evt.my).to.eql('evt');
          called = true;
        });

        pm.onEventMissingHandle({ in: 'fo' }, { my: 'evt' });
        expect(called).to.eql(true);

      });

    });

    describe('initializing', function () {

      var pm;

      beforeEach(function () {
        pm = api({ sagaPath: __dirname });
        pm.defineCommand({
          id: 'i',
          meta: 'm'
        });
        pm.defineEvent({
          id: 'i',
          name: 'n',
          context: 'c',
          aggregate: 'a',
          version: 'v',
          meta: 'm'
        });
      });

      describe('with a callback', function () {

        it('it should work as expected', function (done) {

          var called = 0;
          pm.sagaStore.once('connect', function () {
            called++;
          });
          pm.revisionGuardStore.once('connect', function () {
            called++;
          });
          pm.once('connect', function () {
            called++;
          });

          pm.init(function (err) {
            expect(err).not.to.be.ok();
            expect(called).to.eql(3);
            done();
          });

        });

      });

      describe('without a callback', function () {

        it('it should work as expected', function (done) {

          var called = 0;

          function check () {
            called++;
            if (called >= 3) {
              done();
            }
          }

          pm.sagaStore.once('connect', function () {
            check();
          });
          pm.revisionGuardStore.once('connect', function () {
            check();
          });
          pm.once('connect', function () {
            check();
          });

          pm.init();

        });

      });

      describe('with custom structureLoader', function() {
        it('it should return as expected', function(done) {
          pm = api({
            sagaPath: __dirname,
            denormalizerPath: __dirname,
            structureLoader: function(options) {
              return [
                new options.definitions.Saga({
                  name: 'mySaga'
                }, function() {})
              ]
            },
          });
    
          pm.init(function() {
            var sagas = pm.getInfo().sagas;
            expect(sagas.length).to.eql(1);
            expect(sagas[0].name).to.eql('mySaga');
            done();
          });
                
        });
      });
            

    });

    describe('handling an event', function () {

      describe('not working with revisions', function () {

        var pm;

        beforeEach(function () {
          pm = api({sagaPath: __dirname});
          pm.defineCommand({
            id: 'i',
            meta: 'm'
          });
          pm.defineEvent({
            name: 'n',
            context: 'c',
            aggregate: 'a',
            version: 'v',
            meta: 'm'
          });
        });

        describe('with a callback', function () {

          it('it should work as expected', function (done) {

            var evt = {
              i: 'evtId',
              n: 'evtName',
              ai: 'aggregateId',
              c: 'context',
              p: 'payload',
              r: 'revision',
              v: 'version',
              m: 'meta'
            };
            var dispatchCalled = false;
            var sagastoreCalled = [];
            var onCommandCalled = [];

            pm.onCommand(function (c) {
              onCommandCalled.push(c);
            });

            pm.init(function (err) {
              expect(err).not.to.be.ok();

              pm.eventDispatcher.dispatch = function (e, clb) {
                dispatchCalled = true;
                var s1Ret = [{i: '1'}, {i: '2'}];
                var s2Ret = [{i: '3'}];
                clb(null, [{
                  id: 's1',
                  getUndispatchedCommands: function () {
                    return [].concat(s1Ret);
                  },
                  removeUnsentCommand: function (c) {
                    s1Ret.splice(s1Ret.indexOf(c), 1);
                  },
                  toJSON: function () {
                    return {id: 's1'};
                  },
                  isDestroyed: function () {
                    return false;
                  }
                },
                  {
                    id: 's2',
                    getUndispatchedCommands: function () {
                      return [].concat(s2Ret);
                    },
                    removeUnsentCommand: function (c) {
                      s2Ret.splice(s2Ret.indexOf(c), 1);
                    },
                    toJSON: function () {
                      return {id: 's2'};
                    },
                    isDestroyed: function () {
                      return false;
                    }
                  }]);
              };

              pm.sagaStore.setCommandToDispatched = function (cId, sId, clb) {
                sagastoreCalled.push({sagaId: sId, commandId: cId});
                clb(null);
              };

              var guardCalled = false;
              var guardDoneCalled = false;
              pm.revisionGuard = {
                guard: function (evt, clb) {
                  guardCalled = true;
                  clb(null, function (c) {
                    guardDoneCalled = true;
                    c(null);
                  });
                }
              };

              pm.handle(evt, function (err, cmds, sagaModels) {
                expect(err).not.to.be.ok();
                expect(dispatchCalled).to.eql(true);
                expect(sagastoreCalled.length).to.eql(3);
                expect(sagastoreCalled[0].sagaId).to.eql('s1');
                expect(sagastoreCalled[0].commandId).to.eql('1');
                expect(sagastoreCalled[1].sagaId).to.eql('s1');
                expect(sagastoreCalled[1].commandId).to.eql('2');
                expect(sagastoreCalled[2].sagaId).to.eql('s2');
                expect(sagastoreCalled[2].commandId).to.eql('3');
                expect(onCommandCalled.length).to.eql(3);
                expect(onCommandCalled[0].i).to.eql('1');
                expect(onCommandCalled[1].i).to.eql('2');
                expect(onCommandCalled[2].i).to.eql('3');
                expect(cmds.length).to.eql(3);
                expect(cmds[0].i).to.eql('1');
                expect(cmds[1].i).to.eql('2');
                expect(cmds[2].i).to.eql('3');
                expect(sagaModels.length).to.eql(2);
                expect(sagaModels[0].id).to.eql('s1');
                expect(sagaModels[1].id).to.eql('s2');

                expect(guardCalled).to.eql(false);
                expect(guardDoneCalled).to.eql(false);

                done();
              });
            });

          });

        });

        describe('without a callback', function () {

          it('it should work as expected', function (done) {

            var evt = {
              i: 'evtId',
              n: 'evtName',
              ai: 'aggregateId',
              c: 'context',
              p: 'payload',
              r: 'revision',
              v: 'version',
              m: 'meta'
            };
            var dispatchCalled = false;
            var sagastoreCalled = [];
            var onCommandCalled = [];

            pm.onCommand(function (c) {
              onCommandCalled.push(c);
            });

            pm.init(function (err) {
              expect(err).not.to.be.ok();

              pm.eventDispatcher.dispatch = function (e, clb) {
                dispatchCalled = true;
                var s1Ret = [{i: '1'}, {i: '2'}];
                var s2Ret = [{i: '3'}];
                clb(null, [{
                  id: 's1',
                  getUndispatchedCommands: function () {
                    return [].concat(s1Ret);
                  },
                  removeUnsentCommand: function (c) {
                    s1Ret.splice(s1Ret.indexOf(c), 1);
                  }
                },
                  {
                    id: 's2',
                    getUndispatchedCommands: function () {
                      return [].concat(s2Ret);
                    },
                    removeUnsentCommand: function (c) {
                      s2Ret.splice(s2Ret.indexOf(c), 1);
                    }
                  }]);
              };

              pm.sagaStore.setCommandToDispatched = function (cId, sId, clb) {
                sagastoreCalled.push({sagaId: sId, commandId: cId});
                clb(null);

                if (sagastoreCalled.length === 3) {
                  expect(dispatchCalled).to.eql(true);
                  expect(sagastoreCalled.length).to.eql(3);
                  expect(sagastoreCalled[0].sagaId).to.eql('s1');
                  expect(sagastoreCalled[0].commandId).to.eql('1');
                  expect(sagastoreCalled[1].sagaId).to.eql('s1');
                  expect(sagastoreCalled[1].commandId).to.eql('2');
                  expect(sagastoreCalled[2].sagaId).to.eql('s2');
                  expect(sagastoreCalled[2].commandId).to.eql('3');
                  expect(onCommandCalled.length).to.eql(3);
                  expect(onCommandCalled[0].i).to.eql('1');
                  expect(onCommandCalled[1].i).to.eql('2');
                  expect(onCommandCalled[2].i).to.eql('3');

                  expect(guardCalled).to.eql(false);
                  expect(guardDoneCalled).to.eql(false);

                  done();
                }
              };

              var guardCalled = false;
              var guardDoneCalled = false;
              pm.revisionGuard = {
                guard: function (evt, clb) {
                  guardCalled = true;
                  clb(null, function (c) {
                    guardDoneCalled = true;
                    c(null);
                  });
                }
              };

              pm.handle(evt);
            });

          });

        });

      });

      describe('working with revisions', function () {

        var pm;

        beforeEach(function () {
          pm = api({sagaPath: __dirname});
          pm.defineCommand({
            id: 'i',
            meta: 'm'
          });
          pm.defineEvent({
            name: 'n',
            context: 'c',
            aggregate: 'a',
            aggregateId: 'ai',
            revision: 'r',
            version: 'v',
            meta: 'm'
          });
        });

        describe('with a callback', function () {

          it('it should work as expected', function (done) {

            var evt = {
              i: 'evtId',
              n: 'evtName',
              ai: 'aggregateId',
              c: 'context',
              p: 'payload',
              r: 'revision',
              v: 'version',
              m: 'meta'
            };
            var dispatchCalled = false;
            var sagastoreCalled = [];
            var onCommandCalled = [];

            pm.onCommand(function (c) {
              onCommandCalled.push(c);
            });

            pm.init(function (err) {
              expect(err).not.to.be.ok();

              pm.eventDispatcher.dispatch = function (e, clb) {
                dispatchCalled = true;
                var s1Ret = [{i: '1'}, {i: '2'}];
                var s2Ret = [{i: '3'}];
                clb(null, [{
                  id: 's1',
                  getUndispatchedCommands: function () {
                    return [].concat(s1Ret);
                  },
                  removeUnsentCommand: function (c) {
                    s1Ret.splice(s1Ret.indexOf(c), 1);
                  },
                  toJSON: function () {
                    return {id: 's1'};
                  },
                  isDestroyed: function () {
                    return false;
                  }
                },
                  {
                    id: 's2',
                    getUndispatchedCommands: function () {
                      return [].concat(s2Ret);
                    },
                    removeUnsentCommand: function (c) {
                      s2Ret.splice(s2Ret.indexOf(c), 1);
                    },
                    toJSON: function () {
                      return {id: 's2'};
                    },
                    isDestroyed: function () {
                      return false;
                    }
                  }]);
              };

              pm.sagaStore.setCommandToDispatched = function (cId, sId, clb) {
                sagastoreCalled.push({sagaId: sId, commandId: cId});
                clb(null);
              };

              var guardCalled = false;
              var guardDoneCalled = false;
              pm.revisionGuard = {
                guard: function (evt, clb) {
                  expect(evt.n).to.eql('evtName');
                  guardCalled = true;
                  clb(null, function (c) {
                    guardDoneCalled = true;
                    c(null);
                  });
                }
              };

              pm.handle(evt, function (err, cmds, sagaModels) {
                expect(err).not.to.be.ok();
                expect(dispatchCalled).to.eql(true);
                expect(sagastoreCalled.length).to.eql(3);
                expect(sagastoreCalled[0].sagaId).to.eql('s1');
                expect(sagastoreCalled[0].commandId).to.eql('1');
                expect(sagastoreCalled[1].sagaId).to.eql('s1');
                expect(sagastoreCalled[1].commandId).to.eql('2');
                expect(sagastoreCalled[2].sagaId).to.eql('s2');
                expect(sagastoreCalled[2].commandId).to.eql('3');
                expect(onCommandCalled.length).to.eql(3);
                expect(onCommandCalled[0].i).to.eql('1');
                expect(onCommandCalled[1].i).to.eql('2');
                expect(onCommandCalled[2].i).to.eql('3');
                expect(cmds.length).to.eql(3);
                expect(cmds[0].i).to.eql('1');
                expect(cmds[1].i).to.eql('2');
                expect(cmds[2].i).to.eql('3');
                expect(sagaModels.length).to.eql(2);
                expect(sagaModels[0].id).to.eql('s1');
                expect(sagaModels[1].id).to.eql('s2');

                expect(guardCalled).to.eql(true);
                expect(guardDoneCalled).to.eql(true);

                done();
              });
            });

          });

        });

        describe('without a callback', function () {

          it('it should work as expected', function (done) {

            var evt = {
              i: 'evtId',
              n: 'evtName',
              ai: 'aggregateId',
              c: 'context',
              p: 'payload',
              r: 'revision',
              v: 'version',
              m: 'meta'
            };
            var dispatchCalled = false;
            var sagastoreCalled = [];
            var onCommandCalled = [];

            pm.onCommand(function (c) {
              onCommandCalled.push(c);
            });

            pm.init(function (err) {
              expect(err).not.to.be.ok();

              pm.eventDispatcher.dispatch = function (e, clb) {
                dispatchCalled = true;
                var s1Ret = [{i: '1'}, {i: '2'}];
                var s2Ret = [{i: '3'}];
                clb(null, [{
                  id: 's1',
                  getUndispatchedCommands: function () {
                    return [].concat(s1Ret);
                  },
                  removeUnsentCommand: function (c) {
                    s1Ret.splice(s1Ret.indexOf(c), 1);
                  }
                },
                  {
                    id: 's2',
                    getUndispatchedCommands: function () {
                      return [].concat(s2Ret);
                    },
                    removeUnsentCommand: function (c) {
                      s2Ret.splice(s2Ret.indexOf(c), 1);
                    }
                  }]);
              };

              pm.sagaStore.setCommandToDispatched = function (cId, sId, clb) {
                sagastoreCalled.push({sagaId: sId, commandId: cId});
                clb(null);

                if (sagastoreCalled.length === 3) {
                  expect(dispatchCalled).to.eql(true);
                  expect(sagastoreCalled.length).to.eql(3);
                  expect(sagastoreCalled[0].sagaId).to.eql('s1');
                  expect(sagastoreCalled[0].commandId).to.eql('1');
                  expect(sagastoreCalled[1].sagaId).to.eql('s1');
                  expect(sagastoreCalled[1].commandId).to.eql('2');
                  expect(sagastoreCalled[2].sagaId).to.eql('s2');
                  expect(sagastoreCalled[2].commandId).to.eql('3');
                  expect(onCommandCalled.length).to.eql(3);
                  expect(onCommandCalled[0].i).to.eql('1');
                  expect(onCommandCalled[1].i).to.eql('2');
                  expect(onCommandCalled[2].i).to.eql('3');

                  setTimeout(function () {
                    expect(guardDoneCalled).to.eql(true);
                    expect(guardCalled).to.eql(true);

                    done();
                  }, 500);
                }
              };

              var guardCalled = false;
              var guardDoneCalled = false;
              pm.revisionGuard = {
                guard: function (evt, clb) {
                  expect(evt.n).to.eql('evtName');
                  guardCalled = true;
                  clb(null, function (c) {
                    guardDoneCalled = true;
                    c(null);
                  });
                }
              };

              pm.handle(evt);
            });

          });

        });

      });

      describe('working with revisions but no guard store', function () {

        var pm;

        beforeEach(function () {
          pm = api({sagaPath: __dirname, revisionGuard: false });
          pm.defineCommand({
            id: 'i',
            meta: 'm'
          });
          pm.defineEvent({
            name: 'n',
            context: 'c',
            aggregate: 'a',
            revision: 'r',
            version: 'v',
            meta: 'm'
          });
        });

        describe('with a callback', function () {

          it('it should work as expected', function (done) {

            var evt = {
              i: 'evtId',
              n: 'evtName',
              ai: 'aggregateId',
              c: 'context',
              p: 'payload',
              r: 'revision',
              v: 'version',
              m: 'meta'
            };
            var dispatchCalled = false;
            var sagastoreCalled = [];
            var onCommandCalled = [];

            pm.onCommand(function (c) {
              onCommandCalled.push(c);
            });

            pm.init(function (err) {
              expect(err).not.to.be.ok();

              pm.eventDispatcher.dispatch = function (e, clb) {
                dispatchCalled = true;
                var s1Ret = [{i: '1'}, {i: '2'}];
                var s2Ret = [{i: '3'}];
                clb(null, [{
                  id: 's1',
                  getUndispatchedCommands: function () {
                    return [].concat(s1Ret);
                  },
                  removeUnsentCommand: function (c) {
                    s1Ret.splice(s1Ret.indexOf(c), 1);
                  },
                  toJSON: function () {
                    return {id: 's1'};
                  },
                  isDestroyed: function () {
                    return false;
                  }
                },
                  {
                    id: 's2',
                    getUndispatchedCommands: function () {
                      return [].concat(s2Ret);
                    },
                    removeUnsentCommand: function (c) {
                      s2Ret.splice(s2Ret.indexOf(c), 1);
                    },
                    toJSON: function () {
                      return {id: 's2'};
                    },
                    isDestroyed: function () {
                      return false;
                    }
                  }]);
              };

              pm.sagaStore.setCommandToDispatched = function (cId, sId, clb) {
                sagastoreCalled.push({sagaId: sId, commandId: cId});
                clb(null);
              };

              var guardCalled = false;
              var guardDoneCalled = false;
              pm.revisionGuard = {
                guard: function (evt, clb) {
                  guardCalled = true;
                  clb(null, function (c) {
                    guardDoneCalled = true;
                    c(null);
                  });
                }
              };

              pm.handle(evt, function (err, cmds, sagaModels) {
                expect(err).not.to.be.ok();
                expect(dispatchCalled).to.eql(true);
                expect(sagastoreCalled.length).to.eql(3);
                expect(sagastoreCalled[0].sagaId).to.eql('s1');
                expect(sagastoreCalled[0].commandId).to.eql('1');
                expect(sagastoreCalled[1].sagaId).to.eql('s1');
                expect(sagastoreCalled[1].commandId).to.eql('2');
                expect(sagastoreCalled[2].sagaId).to.eql('s2');
                expect(sagastoreCalled[2].commandId).to.eql('3');
                expect(onCommandCalled.length).to.eql(3);
                expect(onCommandCalled[0].i).to.eql('1');
                expect(onCommandCalled[1].i).to.eql('2');
                expect(onCommandCalled[2].i).to.eql('3');
                expect(cmds.length).to.eql(3);
                expect(cmds[0].i).to.eql('1');
                expect(cmds[1].i).to.eql('2');
                expect(cmds[2].i).to.eql('3');
                expect(sagaModels.length).to.eql(2);
                expect(sagaModels[0].id).to.eql('s1');
                expect(sagaModels[1].id).to.eql('s2');

                expect(guardCalled).to.eql(false);
                expect(guardDoneCalled).to.eql(false);

                done();
              });
            });

          });

        });

        describe('without a callback', function () {

          it('it should work as expected', function (done) {

            var evt = {
              i: 'evtId',
              n: 'evtName',
              ai: 'aggregateId',
              c: 'context',
              p: 'payload',
              r: 'revision',
              v: 'version',
              m: 'meta'
            };
            var dispatchCalled = false;
            var sagastoreCalled = [];
            var onCommandCalled = [];

            pm.onCommand(function (c) {
              onCommandCalled.push(c);
            });

            pm.init(function (err) {
              expect(err).not.to.be.ok();

              pm.eventDispatcher.dispatch = function (e, clb) {
                dispatchCalled = true;
                var s1Ret = [{i: '1'}, {i: '2'}];
                var s2Ret = [{i: '3'}];
                clb(null, [{
                  id: 's1',
                  getUndispatchedCommands: function () {
                    return [].concat(s1Ret);
                  },
                  removeUnsentCommand: function (c) {
                    s1Ret.splice(s1Ret.indexOf(c), 1);
                  }
                },
                  {
                    id: 's2',
                    getUndispatchedCommands: function () {
                      return [].concat(s2Ret);
                    },
                    removeUnsentCommand: function (c) {
                      s2Ret.splice(s2Ret.indexOf(c), 1);
                    }
                  }]);
              };

              pm.sagaStore.setCommandToDispatched = function (cId, sId, clb) {
                sagastoreCalled.push({sagaId: sId, commandId: cId});
                clb(null);

                if (sagastoreCalled.length === 3) {
                  expect(dispatchCalled).to.eql(true);
                  expect(sagastoreCalled.length).to.eql(3);
                  expect(sagastoreCalled[0].sagaId).to.eql('s1');
                  expect(sagastoreCalled[0].commandId).to.eql('1');
                  expect(sagastoreCalled[1].sagaId).to.eql('s1');
                  expect(sagastoreCalled[1].commandId).to.eql('2');
                  expect(sagastoreCalled[2].sagaId).to.eql('s2');
                  expect(sagastoreCalled[2].commandId).to.eql('3');
                  expect(onCommandCalled.length).to.eql(3);
                  expect(onCommandCalled[0].i).to.eql('1');
                  expect(onCommandCalled[1].i).to.eql('2');
                  expect(onCommandCalled[2].i).to.eql('3');

                  expect(guardCalled).to.eql(false);
                  expect(guardDoneCalled).to.eql(false);

                  done();
                }
              };

              var guardCalled = false;
              var guardDoneCalled = false;
              pm.revisionGuard = {
                guard: function (evt, clb) {
                  guardCalled = true;
                  clb(null, function (c) {
                    guardDoneCalled = true;
                    c(null);
                  });
                }
              };

              pm.handle(evt);
            });

          });

        });

      });


    });

    describe('having nothing in the saga store', function () {

      var pm;

      before(function (done) {
        pm = api({ sagaPath: __dirname });
        pm.init(done);
      });

      describe('calling getTimeoutedSagas', function () {

        it('it should work as expected', function (done) {

          pm.getTimeoutedSagas(function(err, sagas) {
            expect(err).not.to.be.ok();
            expect(sagas).to.be.an('array');
            expect(sagas).to.have.length(0);
            done();
          });

        });

      });

      describe('calling getOlderSagas', function() {

        describe('without a valid date object', function () {

          it('it should callback with an error', function (done) {

            pm.getOlderSagas({}, function(err, sagas) {
              expect(err).to.be.ok();
              expect(err.message).to.match(/date/);
              expect(sagas).not.to.be.ok();
              done();
            });

          });

        });

        describe('with a valid date object', function () {

          it('it should callback without an error', function (done) {

            pm.getOlderSagas(new Date(), function(err, sagas) {
              expect(err).not.to.be.ok();
              expect(sagas).to.be.an('array');
              expect(sagas).to.have.length(0);
              done();
            });

          });

        });

      });

      describe('calling getUndispatchedCommands', function() {

        it('it should callback with an empty array', function(done) {

          pm.getUndispatchedCommands(function(err, cmds) {
            expect(err).not.to.be.ok();
            expect(cmds).to.be.an('array');
            expect(cmds).to.have.length(0);
            done();
          });

        });

      });

      describe('calling setCommandToDispatched', function() {

        describe('without a valid commandId', function () {

          it('it should callback with an error', function (done) {

            pm.setCommandToDispatched({}, true, function(err) {
              expect(err).to.be.ok();
              expect(err.message).to.match(/command id/);
              done();
            });

          });

        });

        describe('without a valid sagaId', function () {

          it('it should callback with an error', function (done) {

            pm.setCommandToDispatched('123', true, function(err) {
              expect(err).to.be.ok();
              expect(err.message).to.match(/saga id/);
              done();
            });

          });

        });

        describe('with valid arguments', function () {

          it('it should callback without an error', function (done) {

            pm.setCommandToDispatched('1234', '4356', function(err, nothing) {
              expect(err).not.to.be.ok();
              expect(nothing).to.eql(undefined);
              done();
            });

          });

        });

        describe('calling removeSaga', function() {

          describe('without a valid id object', function () {

            it('it should callback with an error', function (done) {

              pm.removeSaga({}, function(err) {
                expect(err).to.be.ok();
                expect(err.message).to.match(/id/);
                done();
              });

            });

          });

          describe('with a valid id string', function () {

            it('it should callback without an error', function (done) {

              pm.removeSaga('123', function(err) {
                expect(err).not.to.be.ok();
                done();
              });

            });

          });

        });

      });

    });

    describe('having some data in the saga store', function () {

      var pm;

      before(function (done) {
        pm = api({ sagaPath: __dirname });
        pm.init(done);
      });

      var saga1;
      var cmds1;

      var saga2;
      var cmds2;

      var saga3;
      var cmds3;

      var saga4;
      var cmds4;

      beforeEach(function (done) {
        saga1 = { id: 'sagaId1', _commitStamp: new Date(2014, 3, 1), _timeoutAt: new Date(2214, 3, 17), data: 'sagaData1' };
        cmds1 = [{ id: 'cmdId1', payload: { id: 'cmdId1', data: 'cmdData1' } }];

        saga2 = { id: 'sagaId2', _commitStamp: new Date(2014, 3, 2), _timeoutAt: new Date(2014, 3, 15), data: 'sagaData2' };
        cmds2 = [{ id: 'cmdId2', payload: { id: 'cmdId2', data: 'cmdData2' } }, { id: 'cmdId22', payload: { id: 'cmdId22', data: 'cmdData22' } }];

        saga3 = { id: 'sagaId3', _commitStamp: new Date(2014, 3, 5), data: 'sagaData3' };
        cmds3 = [{ id: 'cmdId3', payload: { id: 'cmdId3', data: 'cmdData3' } }];

        saga4 = { id: 'sagaId4', _commitStamp: new Date(2014, 3, 7), data: 'sagaData4' };
        cmds4 = [];

        pm.sagaStore.clear(function () {
          async.series([
            function (callback) {
              pm.sagaStore.save(saga1, cmds1, callback);
            },
            function (callback) {
              pm.sagaStore.save(saga2, cmds2, callback);
            },
            function (callback) {
              pm.sagaStore.save(saga3, cmds3, callback);
            },
            function (callback) {
              pm.sagaStore.save(saga4, cmds4, callback);
            }
          ], done);
        });
      });

      describe('calling getTimeoutedSagas', function () {

        it('it should callback all the timeouted sagas', function (done) {

          pm.getTimeoutedSagas(function (err, sagas) {
            expect(err).not.to.be.ok();
            expect(sagas).to.be.an('array');
            expect(sagas.length).to.eql(1);
            expect(sagas[0].id).to.eql(saga2.id);
            expect(sagas[0].getCommitStamp().getTime()).to.eql(saga2._commitStamp.getTime());
            expect(sagas[0].getTimeoutAt().getTime()).to.eql(saga2._timeoutAt.getTime());
            expect(sagas[0].get('data')).to.eql(saga2.data);
            done();
          });

        });

        describe('calling commit on a saga object', function () {

          describe('with a callback', function () {

            it('it should callback with an error', function (done) {

              pm.getTimeoutedSagas(function (err, sagas) {
                expect(err).not.to.be.ok();
                expect(sagas).to.be.an('array');
                expect(sagas.length).to.eql(1);
                sagas[0].commit(function (err) {
                  expect(err.message).to.match(/remove/);
                  done();
                });
              });

            });

          });

          describe('without a callback', function () {

            it('it should throw an error', function (done) {

              pm.getTimeoutedSagas(function (err, sagas) {
                expect(err).not.to.be.ok();
                expect(sagas).to.be.an('array');
                expect(sagas.length).to.eql(1);
                expect(function() {
                  sagas[0].commit();
                }).to.throwError(/remove/);
                done();
              });

            });

          });

          describe('having added commands to send', function () {

            it('it should work as expected', function (done) {

              pm.getUndispatchedCommands(function (err, cmds) {
                expect(cmds.length).to.eql(4);

                pm.getTimeoutedSagas(function (err, sagas) {
                  expect(err).not.to.be.ok();
                  expect(sagas).to.be.an('array');
                  expect(sagas.length).to.eql(1);
                  sagas[0].addCommandToSend({ id: 'newId', name: 'newCommand' });
                  sagas[0].commit(function (err) {
                    expect(err).not.to.be.ok();

                    pm.getTimeoutedSagas(function (err, sagas) {
                      expect(err).not.to.be.ok();
                      expect(sagas).to.be.an('array');
                      expect(sagas.length).to.eql(1);
                      pm.getUndispatchedCommands(function (err, cmds) {
                        expect(cmds.length).to.eql(5);
                        var cmd = cmds[3];
                        expect(cmd.sagaId).to.eql('sagaId2');
                        expect(cmd.commandId).to.eql('newId');
                        expect(cmd.commitStamp).to.be.ok();
                        expect(cmd.command.id).to.eql('newId');
                        expect(cmd.command.name).to.eql('newCommand');

                        pm.getTimeoutedSagas(function (err, sagas) {
                          expect(err).not.to.be.ok();
                          expect(sagas).to.be.an('array');
                          expect(sagas.length).to.eql(1);

                          sagas[0].removeTimeout();
                          sagas[0].commit(function (err) {
                            expect(err).not.to.be.ok();
                            pm.getTimeoutedSagas(function (err, sagas) {
                              expect(err).not.to.be.ok();
                              expect(sagas).to.be.an('array');
                              expect(sagas.length).to.eql(0);
                              done();
                            });
                          });
                        });

                      });
                    });
                  });
                });
              });

            });

            describe('having added commands to send and having registered an onCommand handle', function () {

              it('it should work as expected', function (done) {

                pm.onCommand(function (cmd) {
                  expect(cmd.id).to.eql('newId');
                  expect(cmd.name).to.eql('newCommand');
                });

                pm.getUndispatchedCommands(function (err, cmds) {
                  expect(cmds.length).to.eql(4);

                  pm.getTimeoutedSagas(function (err, sagas) {
                    expect(err).not.to.be.ok();
                    expect(sagas).to.be.an('array');
                    expect(sagas.length).to.eql(1);
                    sagas[0].addCommandToSend({ id: 'newId', name: 'newCommand' });
                    sagas[0].commit(function (err) {
                      expect(err).not.to.be.ok();

                      pm.getTimeoutedSagas(function (err, sagas) {
                        expect(err).not.to.be.ok();
                        expect(sagas).to.be.an('array');
                        expect(sagas.length).to.eql(1);
                        pm.getUndispatchedCommands(function (err, cmds) {
                          expect(cmds.length).to.eql(4);
                          var cmd = cmds[3];
                          expect(cmd.sagaId).to.eql('sagaId3');
                          expect(cmd.commandId).to.eql('cmdId3');
                          expect(cmd.commitStamp).to.be.ok();
                          expect(cmd.command.id).to.eql('cmdId3');
                          expect(cmd.command.data).to.eql('cmdData3');
                          done();
                        });
                      });
                    });
                  });
                });

              });

            });

          });

          describe('having marked the saga as destroyed', function () {

            it('it should work as expected', function (done) {

              pm.getTimeoutedSagas(function (err, sagas) {
                expect(err).not.to.be.ok();
                expect(sagas).to.be.an('array');
                expect(sagas.length).to.eql(1);
                sagas[0].destroy();
                sagas[0].commit(function (err) {
                  expect(err).not.to.be.ok();

                  pm.getTimeoutedSagas(function (err, sagas) {
                    expect(err).not.to.be.ok();
                    expect(sagas).to.be.an('array');
                    expect(sagas.length).to.eql(0);
                    done();
                  });
                });
              });

            });

          });

        });

      });

      describe('calling getOlderSagas', function () {

        it('it should callback the expected sagas', function (done) {

          pm.getOlderSagas(new Date(2014, 3, 3), function (err, sagas) {
            expect(err).not.to.be.ok();
            expect(sagas).to.be.an('array');
            expect(sagas.length).to.eql(2);
            expect(sagas[0].id).to.eql(saga1.id);
            expect(sagas[0].getCommitStamp().getTime()).to.eql(saga1._commitStamp.getTime());
            expect(sagas[0].getTimeoutAt().getTime()).to.eql(saga1._timeoutAt.getTime());
            expect(sagas[0].get('data')).to.eql(saga1.data);
            expect(sagas[1].id).to.eql(saga2.id);
            expect(sagas[1].getCommitStamp().getTime()).to.eql(saga2._commitStamp.getTime());
            expect(sagas[1].getTimeoutAt().getTime()).to.eql(saga2._timeoutAt.getTime());
            expect(sagas[1].get('data')).to.eql(saga2.data);

            done();
          });

        });

        describe('calling commit on a saga object', function () {

          describe('with a callback', function () {

            it('it should callback with an error', function (done) {

              pm.getOlderSagas(new Date(2014, 3, 3), function (err, sagas) {
                expect(err).not.to.be.ok();
                expect(sagas).to.be.an('array');
                expect(sagas.length).to.eql(2);
                sagas[0].commit(function (err) {
                  expect(err.message).to.match(/remove/);
                  done();
                });
              });

            });

          });

          describe('without a callback', function () {

            it('it should throw an error', function (done) {

              pm.getOlderSagas(new Date(2014, 3, 3), function (err, sagas) {
                expect(err).not.to.be.ok();
                expect(sagas).to.be.an('array');
                expect(sagas.length).to.eql(2);
                expect(function() {
                  sagas[0].commit();
                }).to.throwError(/remove/);
                done();
              });

            });

          });

          describe('having marked the saga as destroyed', function () {

            it('it should work as expected', function (done) {

              pm.getOlderSagas(new Date(2014, 3, 3), function (err, sagas) {
                expect(err).not.to.be.ok();
                expect(sagas).to.be.an('array');
                expect(sagas.length).to.eql(2);
                sagas[0].destroy();
                sagas[0].commit(function (err) {
                  expect(err).not.to.be.ok();

                  pm.getOlderSagas(new Date(2014, 3, 3), function (err, sagas) {
                    expect(err).not.to.be.ok();
                    expect(sagas).to.be.an('array');
                    expect(sagas.length).to.eql(1);
                    expect(sagas[0].id).to.eql(saga2.id);
                    expect(sagas[0].getCommitStamp().getTime()).to.eql(saga2._commitStamp.getTime());
                    expect(sagas[0].getTimeoutAt().getTime()).to.eql(saga2._timeoutAt.getTime());
                    expect(sagas[0].get('data')).to.eql(saga2.data);

                    sagas[0].removeTimeout();
                    sagas[0].commit(function (err) {
                      expect(err).not.to.be.ok();

                      pm.getOlderSagas(new Date(2014, 3, 3), function (err, sagas) {
                        expect(err).not.to.be.ok();
                        expect(sagas).to.be.an('array');
                        expect(sagas.length).to.eql(0);

                        done();
                      });
                    });
                  });
                });
              });

            });

          });

        });

      });

      describe('calling getUndispatchedCommands', function () {

        it('it should callback with the expected commands', function (done) {

          pm.getUndispatchedCommands(function (err, cmds) {
            expect(err).not.to.be.ok();
            expect(cmds).to.be.an('array');
            expect(cmds.length).to.eql(4);
            expect(cmds[0].sagaId).to.eql(saga1.id);
            expect(cmds[0].commandId).to.eql(cmds1[0].id);
            expect(cmds[0].command.id).to.eql(cmds1[0].payload.id);
            expect(cmds[0].command.data).to.eql(cmds1[0].payload.data);
            expect(cmds[1].sagaId).to.eql(saga2.id);
            expect(cmds[1].commandId).to.eql(cmds2[0].id);
            expect(cmds[1].command.id).to.eql(cmds2[0].payload.id);
            expect(cmds[1].command.data).to.eql(cmds2[0].payload.data);
            expect(cmds[2].sagaId).to.eql(saga2.id);
            expect(cmds[2].commandId).to.eql(cmds2[1].id);
            expect(cmds[2].command.id).to.eql(cmds2[1].payload.id);
            expect(cmds[2].command.data).to.eql(cmds2[1].payload.data);
            expect(cmds[3].sagaId).to.eql(saga3.id);
            expect(cmds[3].commandId).to.eql(cmds3[0].id);
            expect(cmds[3].command.id).to.eql(cmds3[0].payload.id);
            expect(cmds[3].command.data).to.eql(cmds3[0].payload.data);

            done();
          });

        });

      });

      describe('calling setCommandToDispatched', function () {

        it('it should remove this command from store', function (done) {

          pm.setCommandToDispatched('cmdId2', 'sagaId2', function (err) {
            expect(err).not.to.be.ok();

            pm.getUndispatchedCommands(function (err, cmds) {
              expect(err).not.to.be.ok();
              expect(cmds).to.be.an('array');
              expect(cmds.length).to.eql(3);
              expect(cmds[0].sagaId).to.eql(saga1.id);
              expect(cmds[0].commandId).to.eql(cmds1[0].id);
              expect(cmds[0].command.id).to.eql(cmds1[0].payload.id);
              expect(cmds[0].command.data).to.eql(cmds1[0].payload.data);
              expect(cmds[1].sagaId).to.eql(saga2.id);
              expect(cmds[1].commandId).to.eql(cmds2[1].id);
              expect(cmds[1].command.id).to.eql(cmds2[1].payload.id);
              expect(cmds[1].command.data).to.eql(cmds2[1].payload.data);
              expect(cmds[2].sagaId).to.eql(saga3.id);
              expect(cmds[2].commandId).to.eql(cmds3[0].id);
              expect(cmds[2].command.id).to.eql(cmds3[0].payload.id);
              expect(cmds[2].command.data).to.eql(cmds3[0].payload.data);

              done();
            });
          });

        });

      });

      describe('calling removeSaga', function () {

        it('it should remove the requesting saga and its commands', function (done) {

          pm.removeSaga('sagaId2', function (err) {
            expect(err).not.to.be.ok();

            pm.getTimeoutedSagas(function (err, sagas) {
              expect(err).not.to.be.ok();
              expect(sagas).to.be.an('array');
              expect(sagas.length).to.eql(0);

              pm.getOlderSagas(new Date(2314, 3, 17), function (err, sagas) {
                expect(err).not.to.be.ok();
                expect(sagas).to.be.an('array');
                expect(sagas.length).to.eql(3);
                expect(sagas[0].id).to.eql(saga1.id);
                expect(sagas[0].getCommitStamp().getTime()).to.eql(saga1._commitStamp.getTime());
                expect(sagas[0].getTimeoutAt().getTime()).to.eql(saga1._timeoutAt.getTime());
                expect(sagas[0].get('data')).to.eql(saga1.data);
                expect(sagas[1].id).to.eql(saga3.id);
                expect(sagas[1].getCommitStamp().getTime()).to.eql(saga3._commitStamp.getTime());
                expect(sagas[1].get('data')).to.eql(saga3.data);
                expect(sagas[2].id).to.eql(saga4.id);
                expect(sagas[2].getCommitStamp().getTime()).to.eql(saga4._commitStamp.getTime());
                expect(sagas[2].get('data')).to.eql(saga4.data);

                pm.getUndispatchedCommands(function (err, cmds) {
                  expect(err).not.to.be.ok();
                  expect(cmds).to.be.an('array');
                  expect(cmds.length).to.eql(2);
                  expect(cmds[0].sagaId).to.eql(saga1.id);
                  expect(cmds[0].commandId).to.eql(cmds1[0].id);
                  expect(cmds[0].command.id).to.eql(cmds1[0].payload.id);
                  expect(cmds[0].command.data).to.eql(cmds1[0].payload.data);
                  expect(cmds[1].sagaId).to.eql(saga3.id);
                  expect(cmds[1].commandId).to.eql(cmds3[0].id);
                  expect(cmds[1].command.id).to.eql(cmds3[0].payload.id);
                  expect(cmds[1].command.data).to.eql(cmds3[0].payload.data);

                  done();
                });
              });
            });
          });

        });

      });


    });

  });

});
```

## File: `test/unit/revisionGuardStoreTest.js`
```javascript
var expect = require('expect.js'),
  async = require('async'),
  revisionGuardStore = require('../../lib/revisionGuardStore'),
  Base = require('../../lib/revisionGuardStore/base'),
  InMemory = require('../../lib/revisionGuardStore/databases/inmemory');

describe('revisionGuardStore', function() {

  it('it should have the correct interface', function() {

    expect(revisionGuardStore).to.be.an('object');
    expect(revisionGuardStore.create).to.be.a('function');
    expect(revisionGuardStore.Store).to.eql(Base);

  });

  describe('calling create', function() {

    describe('without options', function() {

      it('it should return with the in memory store', function() {

        var store = revisionGuardStore.create();
        expect(store).to.be.a('object');

      });

      describe('but with a callback', function() {

        it('it should callback with store object', function(done) {

          revisionGuardStore.create(function(err, store) {
            expect(err).not.to.be.ok();
            expect(store).to.be.a('object');
            done();
          });

        });

      });

    });

    describe('with options of a non existing db implementation', function() {

      it('it should throw an error', function() {

        expect(function() {
          revisionGuardStore.create({ type: 'strangeDb' });
        }).to.throwError();

      });

      it('it should callback with an error', function(done) {

        expect(function() {
          revisionGuardStore.create({ type: 'strangeDb' }, function(err) {
            expect(err).to.be.ok();
            done();
          });
        }).to.throwError();

      });

    });

    describe('with options of an own db implementation', function() {

      it('it should return with the an instance of that implementation', function() {

        var store = revisionGuardStore.create({ type: InMemory });
        expect(store).to.be.a(InMemory);

      });

    });

    describe('with options containing a type property with the value of', function() {

      var types = ['inmemory', 'mongodb', 'tingodb', 'redis'/*, 'azuretable'*/];

      types.forEach(function(type) {

        describe('"' + type + '"', function() {

          var store;

          describe('without callback', function() {

            afterEach(function(done) {
              store.disconnect(done);
            });

            it('it should return with the correct store', function() {

              store = revisionGuardStore.create({ type: type });
              expect(store).to.be.a('object');
              expect(store).to.be.a(Base);
              expect(store.connect).to.be.a('function');
              expect(store.disconnect).to.be.a('function');
              expect(store.getNewId).to.be.a('function');
              expect(store.get).to.be.a('function');
              expect(store.set).to.be.a('function');
              expect(store.saveLastEvent).to.be.a('function');
              expect(store.getLastEvent).to.be.a('function');

            });

          });

          describe('with callback', function() {

            afterEach(function(done) {
              store.disconnect(done);
            });

            it('it should return with the correct store', function(done) {

              revisionGuardStore.create({ type: type }, function(err, resS) {
                expect(err).not.to.be.ok();
                store = resS;
                expect(store).to.be.a('object');
                done();
              });

            });

          });

          describe('calling connect', function () {

            afterEach(function(done) {
              store.disconnect(done);
            });

            describe('with a callback', function () {

              it('it should callback successfully', function(done) {

                store = revisionGuardStore.create({ type: type });
                store.connect(function (err) {
                  expect(err).not.to.be.ok();
                  done();
                });

              });

            });

            describe('without a callback', function () {

              it('it should emit connect', function(done) {

                store = revisionGuardStore.create({ type: type });
                store.once('connect', done);
                store.connect();

              });

            });

          });

          describe('having connected', function() {

            describe('calling disconnect', function() {

              beforeEach(function(done) {
                store = revisionGuardStore.create({ type: type });
                store.connect(done);
              });

              it('it should callback successfully', function(done) {

                store.disconnect(function(err) {
                  expect(err).not.to.be.ok();
                  done();
                });

              });

              it('it should emit disconnect', function(done) {

                store.once('disconnect', done);
                store.disconnect();

              });

            });

            describe('using the store', function() {

              before(function(done) {
                store = revisionGuardStore.create({ type: type });
                store.connect(done);
              });

              describe('calling getNewId', function() {

                it('it should callback with a new Id as string', function(done) {

                  store.getNewId(function(err, id) {
                    expect(err).not.to.be.ok();
                    expect(id).to.be.a('string');
                    done();
                  });

                });

              });

              describe('having no entries', function() {

                before(function(done) {
                  store.clear(done);
                });

                describe('calling get', function() {

                  it('it should callback with an empty revision', function(done) {

                    store.get('23', function (err, rev) {
                      expect(err).not.to.be.ok();
                      expect(rev).not.to.be.ok();
                      done();
                    });

                  });

                });

                describe('calling set', function() {

                  it('it should work as expected', function(done) {

                    store.set('23', 5, 4, function (err) {
                      expect(err).not.to.be.ok();

                      store.get('23', function (err, rev) {
                        expect(err).not.to.be.ok();
                        expect(rev).to.eql(5);

                        done();
                      });
                    });

                  });

                  describe('with a current revision that is less than expected', function () {

                    it('it should callback with a ConcurrencyError', function(done) {

                      store.set('23', 6, 4, function (err) {
                        expect(err).to.be.ok();
                        expect(err.name).to.eql('ConcurrencyError');

                        store.get('23', function (err, rev) {
                          expect(err).not.to.be.ok();
                          expect(rev).to.eql(5);

                          done();
                        });
                      });

                    });

                  });

                  describe('with a current revision that is greater than expected', function () {

                    it('it should callback with a ConcurrencyError', function(done) {

                      store.set('23', 6, 7, function (err) {
                        expect(err).to.be.ok();
                        expect(err.name).to.eql('ConcurrencyError');

                        store.get('23', function (err, rev) {
                          expect(err).not.to.be.ok();
                          expect(rev).to.eql(5);

                          done();
                        });
                      });

                    });

                  });

                  describe('with a current revision that is equal than expected', function () {

                    it('it should callback with a ConcurrencyError', function(done) {

                      store.set('23', 6, 6, function (err) {
                        expect(err).to.be.ok();
                        expect(err.name).to.eql('ConcurrencyError');

                        store.get('23', function (err, rev) {
                          expect(err).not.to.be.ok();
                          expect(rev).to.eql(5);

                          done();
                        });
                      });

                    });

                  });

                  describe('with a current revision that is null', function () {

                    it('it should callback without an error', function(done) {

                      store.set('2345', 2, null, function (err) {
                        expect(err).not.to.be.ok();

                        store.get('2345', function (err, rev) {
                          expect(err).not.to.be.ok();
                          expect(rev).to.eql(2);

                          done();
                        });
                      });

                    });

                  });

                  describe('with a current revision that is correct', function () {

                    it('it should callback without an error', function(done) {

                      store.set('23', 6, 5, function (err) {
                        expect(err).not.to.be.ok();

                        store.get('23', function (err, rev) {
                          expect(err).not.to.be.ok();
                          expect(rev).to.eql(6);

                          done();
                        });
                      });

                    });

                  });

                });

                describe('saving the last event', function() {

                  it('it should work as expected', function (done) {

                    store.getLastEvent(function (err, evt) {
                      expect(err).not.to.be.ok();
                      expect(evt).not.to.be.ok();

                      store.saveLastEvent({ my: 'evt' }, function (err) {
                        expect(err).not.to.be.ok();

                        store.getLastEvent(function (err, evt) {
                          expect(err).not.to.be.ok();
                          expect(evt.my).to.eql('evt');

                          store.clear(function (err) {
                            expect(err).not.to.be.ok();

                            store.getLastEvent(function (err, evt) {
                              expect(err).not.to.be.ok();
                              expect(evt).not.to.be.ok();

                              done();
                            });
                          });
                        });
                      });

                    });

                  });

                });

              });

            });

          });

        });

      });

    });

  });

});
```

## File: `test/unit/revisionGuardTest.js`
```javascript
var expect = require('expect.js'),
  _ = require('lodash'),
  RevisionGuard = require('../../lib/revisionGuard'),
  revGuardStore = require('../../lib/revisionGuardStore');

describe('revisionGuard', function () {

  var store;

  before(function (done) {
    revGuardStore.create(function (err, s) {
      store = s;
      done();
    });
  });

  describe('creating a new guard', function () {

    it('it should not throw an error', function () {

      expect(function () {
        new RevisionGuard(store);
      }).not.to.throwError();

    });

    it('it should return a correct object', function () {

      var guard = new RevisionGuard(store);
      expect(guard.definition).to.be.an('object');
      expect(guard.defineEvent).to.be.a('function');
      expect(guard.onEventMissing).to.be.a('function');

    });

    describe('defining the event structure', function() {

      var guard;

      beforeEach(function () {
        guard = new RevisionGuard(store);
      });

      describe('using the defaults', function () {

        it('it should apply the defaults', function() {

          var defaults = _.cloneDeep(guard.definition);

          guard.defineEvent({
            payload: 'data',
            aggregate: 'aggName',
            context: 'ctx.Name',
            revision: 'rev',
            version: 'v.',
            meta: 'pass'
          });

          expect(defaults.correlationId).to.eql(guard.definition.correlationId);
          expect(defaults.id).to.eql(guard.definition.id);
          expect(guard.definition.payload).to.eql('data');
          expect(defaults.payload).not.to.eql(guard.definition.payload);
          expect(defaults.name).to.eql(guard.definition.name);
          expect(defaults.aggregateId).to.eql(guard.definition.aggregateId);
          expect(guard.definition.aggregate).to.eql('aggName');
          expect(defaults.aggregate).not.to.eql(guard.definition.aggregate);
          expect(guard.definition.context).to.eql('ctx.Name');
          expect(defaults.context).not.to.eql(guard.definition.context);
          expect(guard.definition.revision).to.eql('rev');
          expect(defaults.revision).not.to.eql(guard.definition.revision);
          expect(guard.definition.version).to.eql('v.');
          expect(defaults.version).not.to.eql(guard.definition.version);
          expect(guard.definition.meta).to.eql('pass');
          expect(defaults.meta).not.to.eql(guard.definition.meta);

        });

      });

      describe('overwriting the defaults', function () {

        it('it should apply them correctly', function() {

          var defaults = _.cloneDeep(guard.definition);

          guard.defineEvent({
            correlationId: 'cmdId',
            id: 'eventId',
            payload: 'data',
            name: 'defName',
            aggregateId: 'path.to.aggId',
            aggregate: 'aggName',
            context: 'ctx.Name',
            revision: 'rev',
            version: 'v.',
            meta: 'pass'
          });

          expect(guard.definition.correlationId).to.eql('cmdId');
          expect(defaults.correlationId).not.to.eql(guard.definition.correlationId);
          expect(guard.definition.id).to.eql('eventId');
          expect(defaults.id).not.to.eql(guard.definition.id);
          expect(guard.definition.payload).to.eql('data');
          expect(defaults.payload).not.to.eql(guard.definition.payload);
          expect(guard.definition.name).to.eql('defName');
          expect(defaults.name).not.to.eql(guard.definition.name);
          expect(guard.definition.aggregateId).to.eql('path.to.aggId');
          expect(defaults.aggregateId).not.to.eql(guard.definition.aggregateId);
          expect(guard.definition.aggregate).to.eql('aggName');
          expect(defaults.aggregate).not.to.eql(guard.definition.aggregate);
          expect(guard.definition.context).to.eql('ctx.Name');
          expect(defaults.context).not.to.eql(guard.definition.context);
          expect(guard.definition.revision).to.eql('rev');
          expect(defaults.revision).not.to.eql(guard.definition.revision);
          expect(guard.definition.version).to.eql('v.');
          expect(defaults.version).not.to.eql(guard.definition.version);
          expect(guard.definition.meta).to.eql('pass');
          expect(defaults.meta).not.to.eql(guard.definition.meta);

        });

      });

    });

    describe('guarding an event', function () {

      var guard;

      var evt1 = {
        id: 'evtId1',
        aggregate: {
          id: 'aggId1',
          name: 'agg'
        },
        context: {
          name: 'ctx'
        },
        revision: 1
      };

      var evt2 = {
        id: 'evtId2',
        aggregate: {
          id: 'aggId1',
          name: 'agg'
        },
        context: {
          name: 'ctx'
        },
        revision: 2
      };

      var evt3 = {
        id: 'evtId3',
        aggregate: {
          id: 'aggId1',
          name: 'agg'
        },
        context: {
          name: 'ctx'
        },
        revision: 3
      };

      before(function () {
        guard = new RevisionGuard(store, { queueTimeout: 200 });
        guard.defineEvent({
          correlationId: 'correlationId',
          id: 'id',
          payload: 'payload',
          name: 'name',
          aggregateId: 'aggregate.id',
          aggregate: 'aggregate.name',
          context: 'context.name',
          revision: 'revision',
          version: 'version',
          meta: 'meta'
        });
      });

      beforeEach(function (done) {
        guard.currentHandlingRevisions = {};
        store.clear(done);
      });

      describe('in correct order', function () {

        it('it should work as expected', function (done) {

          var guarded = 0;

          function check () {
            guarded++;

            if (guarded === 3) {
              done();
            }
          }

          guard.guard(evt1, function (err, finish) {
            expect(err).not.to.be.ok();

            finish(function (err) {
              expect(err).not.to.be.ok();
              expect(guarded).to.eql(0);
              check();
            });
          });

          setTimeout(function () {
            guard.guard(evt2, function (err, finish) {
              expect(err).not.to.be.ok();

              finish(function (err) {
                expect(err).not.to.be.ok();
                expect(guarded).to.eql(1);
                check();
              });
            });
          }, 10);

          setTimeout(function () {
            guard.guard(evt3, function (err, finish) {
              expect(err).not.to.be.ok();

              finish(function (err) {
                expect(err).not.to.be.ok();
                expect(guarded).to.eql(2);
                check();
              });
            });
          }, 20);

        });

        describe('but with slow beginning events', function () {

          var specialGuard;

          before(function () {
            specialGuard = new RevisionGuard(store, { queueTimeout: 2000, queueTimeoutMaxLoops: 15 });
            specialGuard.defineEvent({
              correlationId: 'correlationId',
              id: 'id',
              payload: 'payload',
              name: 'name',
              aggregateId: 'aggregate.id',
              aggregate: 'aggregate.name',
              context: 'context.name',
              revision: 'revision',
              version: 'version',
              meta: 'meta'
            });
          });

          beforeEach(function (done) {
            specialGuard.currentHandlingRevisions = {};
            store.clear(done);
          });

          it('it should work as expected', function (done) {

            var guarded = 0;

            function check () {
              guarded++;

              if (guarded === 3) {
                done();
              }
            }

            var start1 = Date.now();
            specialGuard.guard(evt1, function (err, finish1) {
              var diff1 = Date.now() - start1;
              console.log('guarded 1: ' + diff1);
              expect(err).not.to.be.ok();

              setTimeout(function () {
                start1 = Date.now();
                finish1(function (err) {
                  diff1 = Date.now() - start1;
                  console.log('finished 1: ' + diff1);
                  expect(err).not.to.be.ok();
                  expect(guarded).to.eql(0);
                  check();
                });
              }, 250);
            });

            var start2 = Date.now();
            specialGuard.guard(evt2, function (err, finish2) {
              var diff2 = Date.now() - start2;
              console.log('guarded 2: ' + diff2);
              expect(err).not.to.be.ok();

              start2 = Date.now();
              finish2(function (err) {
                diff2 = Date.now() - start2;
                console.log('finished 2: ' + diff2);
                expect(err).not.to.be.ok();
                expect(guarded).to.eql(1);
                check();
              });
            });

            var start3 = Date.now();
            specialGuard.guard(evt3, function (err, finish3) {
              var diff3 = Date.now() - start3;
              console.log('guarded 3: ' + diff3);
              expect(err).not.to.be.ok();

              start3 = Date.now();
              finish3(function (err) {
                diff3 = Date.now() - start3;
                console.log('finished 3: ' + diff3);
                expect(err).not.to.be.ok();
                expect(guarded).to.eql(2);
                check();
              });
            });

          });

        });

        describe('but having a startRevisionNumber', function () {

          var specialGuard;

          beforeEach(function (done) {
            specialGuard = new RevisionGuard(store, { queueTimeout: 200, queueTimeoutMaxLoops: 3, startRevisionNumber: 1 });
            specialGuard.defineEvent({
              correlationId: 'correlationId',
              id: 'id',
              payload: 'payload',
              name: 'name',
              aggregateId: 'aggregate.id',
              aggregate: 'aggregate.name',
              context: 'context.name',
              revision: 'revision',
              version: 'version',
              meta: 'meta'
            });
            specialGuard.currentHandlingRevisions = {};
            store.clear(done);
          });

          it('and guarding an event with revision greater than expected, it should emit an eventMissing event', function (done) {

            specialGuard.onEventMissing(function (info, e) {
              expect(info.aggregateId).to.equal(evt2.aggregate.id);
              expect(info.aggregateRevision).to.equal(evt2.revision);
              expect(info.guardRevision).to.equal(1);
              expect(e).to.equal(evt2);
              done();
            });

            specialGuard.guard(evt2, function (err, finish) {});

          });

          it('and guarding an event with revision like expected, it should work normally', function (done) {

            specialGuard.guard(evt1, function (err, finish) {
              expect(err).not.to.be.ok();
              finish(function (err) {
                expect(err).not.to.be.ok();
                done();
              });
            });

          });

          it('and guarding an event with revision smaller than expected, it work normally', function (done) {

            var evt0 = _.cloneDeep(evt1);
            evt0.revision = 0;

            specialGuard.guard(evt0, function (err, finish) {
              expect(err).not.to.be.ok();
              finish(function (err) {
                expect(err).not.to.be.ok();
                done();
              });
            });

          });

        });

      });

      describe('in wrong order', function () {

        it('it should work as expected', function (done) {

          var guarded = 0;

          function check () {
            guarded++;

//            if (guarded === 3) {
//              done();
//            }
          }

          guard.guard(evt1, function (err, finish) {
            expect(err).not.to.be.ok();

            finish(function (err) {
              expect(err).not.to.be.ok();
              expect(guarded).to.eql(0);
              check();
            });
          });

          setTimeout(function () {
            guard.guard(evt2, function (err, finish) {
              expect(err).not.to.be.ok();

              finish(function (err) {
                expect(err).not.to.be.ok();
                expect(guarded).to.eql(1);
                check();
              });
            });
          }, 30);

          setTimeout(function () {
            guard.guard(evt3, function (err, finish) {
              expect(err).not.to.be.ok();

              finish(function (err) {
                expect(err).not.to.be.ok();
                expect(guarded).to.eql(2);
                check();
              });
            });
            guard.guard(evt3, function (err, finish) {
              expect(err).to.be.ok();
              expect(err.name).to.eql('AlreadyHandlingError');
            });
          }, 10);

          setTimeout(function () {
            guard.guard(evt2, function (err) {
              expect(err).to.be.ok();
              expect(err.name).to.eql('AlreadyHandledError');
              expect(guarded).to.eql(3);

              guard.guard(evt3, function (err) {
                expect(err).to.be.ok();
                expect(err.name).to.eql('AlreadyHandledError');
                expect(guarded).to.eql(3);

                store.getLastEvent(function (err, evt) {
                  expect(err).not.to.be.ok();
                  expect(evt.id).to.eql(evt3.id);
                  done();
                });
              });
            });
          }, 300);

        });

      });

      describe('and missing something', function () {

        it('it should work as expected', function (done) {

          var guarded = 0;

          function check () {
            guarded++;

//            if (guarded === 3) {
//              done();
//            }
          }

          guard.onEventMissing(function (info, evt) {
            expect(guarded).to.eql(1);
            expect(evt).to.eql(evt3);
            expect(info.aggregateId).to.eql('aggId1');
            expect(info.aggregateRevision).to.eql(3);
            expect(info.guardRevision).to.eql(2);
            expect(info.aggregate).to.eql('agg');
            expect(info.context).to.eql('ctx');
            done();
          });

          guard.guard(evt1, function (err, finish) {
            expect(err).not.to.be.ok();

            finish(function (err) {
              expect(err).not.to.be.ok();
              expect(guarded).to.eql(0);
              check();
            });
          });

          setTimeout(function () {
            guard.guard(evt3, function (err, finish) {
              expect(err).not.to.be.ok();

              finish(function (err) {
                expect(err).not.to.be.ok();
                expect(guarded).to.eql(2);
                check();
              });
            });
          }, 20);

        });

      });

    });

  });

});
```

## File: `test/unit/sagaModelTest.js`
```javascript
var expect = require('expect.js'),
  SagaModel = require('../../lib/sagaModel');

describe('saga model', function () {

  describe('creating a new instance', function () {

    describe('without any arguments', function () {

      it('it should throw an error', function () {

        expect(function () {
          new SagaModel();
        }).to.throwError(/id/);

      });

    });

    describe('with an id as number', function () {

      it('it should throw an error', function () {

        expect(function () {
          new SagaModel(1234);
        }).to.throwError(/id/);

      });

    });

    describe('with an id as string', function () {

      it('it should not throw an error', function () {

        expect(function () {
          new SagaModel('12345');
        }).not.to.throwError();

      });

      it('it should return a correct object', function() {

        var saga = new SagaModel('1234');

        expect(saga).to.be.an('object');
        expect(saga.set).to.be.a('function');
        expect(saga.get).to.be.a('function');
        expect(saga.has).to.be.a('function');
        expect(saga.toJSON).to.be.a('function');
        expect(saga.destroy).to.be.a('function');
        expect(saga.isDestroyed).to.be.a('function');
        expect(saga.setCommitStamp).to.be.a('function');
        expect(saga.getCommitStamp).to.be.a('function');
        expect(saga.addTimeout).to.be.a('function');
        expect(saga.removeTimeout).to.be.a('function');
        expect(saga.getTimeoutAt).to.be.a('function');
        expect(saga.getTimeoutCommands).to.be.a('function');
        expect(saga.addUnsentCommand).to.be.a('function');
        expect(saga.removeUnsentCommand).to.be.a('function');
        expect(saga.getUndispatchedCommands).to.be.a('function');

        expect(saga.id).to.eql('1234');
        expect(saga.get('id')).to.eql('1234');

      });

    });
    
    describe('setting a new id', function () {
      
      it('it should update its attribute value too', function () {

        var saga = new SagaModel('1234');

        expect(saga.id).to.eql('1234');
        expect(saga.get('id')).to.eql('1234');
        expect(saga.attributes.id).to.eql('1234');

        saga.id = '8372';
        
        expect(saga.id).to.eql('8372');
        expect(saga.get('id')).to.eql('8372');
        expect(saga.attributes.id).to.eql('8372');

        saga.set('id', '9163');

        expect(saga.id).to.eql('9163');
        expect(saga.get('id')).to.eql('9163');
        expect(saga.attributes.id).to.eql('9163');

        saga.set({ id: '6391' });

        expect(saga.id).to.eql('6391');
        expect(saga.get('id')).to.eql('6391');
        expect(saga.attributes.id).to.eql('6391');
        
      });
      
    });

    describe('calling has', function() {

      describe('of an attribute that does exist', function() {

        it('it should return true', function() {

          var saga = new SagaModel('123456');
          saga.set('a', 'b');

          expect(saga.has('id')).to.eql(true);
          expect(saga.has('a')).to.eql(true);

        });

      });

      describe('of an attribute that does not exist', function() {

        it('it should return false', function() {

          var saga = new SagaModel('123456');

          expect(saga.has('data222')).to.eql(false);

        });

      });

    });

    describe('calling get', function() {

      describe('of an attribute that does exist', function() {

        it('it should return that value', function() {

          var saga = new SagaModel('123456');
          saga.set('my', 'data');

          expect(saga.get('my')).to.eql('data');

        });

      });

      describe('of an attribute that does not exist', function() {

        it('it should return undefined', function() {

          var saga = new SagaModel('123456');

          expect(saga.get('data222')).to.eql(undefined);

        });

      });

      describe('of an attribute that is deep', function() {

        it('it should return that value', function() {

          var saga = new SagaModel('123456');
          saga.set('deep', { data: 'other stuff' });

          expect(saga.get('deep.data')).to.eql('other stuff');

        });

      });

    });

    describe('calling set', function() {

      describe('with a simple key', function() {

        it('it should set it correctly', function() {

          var saga = new SagaModel('123456');

          saga.set('data', 'a');
          expect(saga.get('data')).to.eql('a');

        });

      });

      describe('with a path as key', function() {

        it('it should set it correctly', function() {

          var saga = new SagaModel('123456');

          saga.set('path.sub', 'b');
          expect(saga.get('path.sub')).to.eql('b');

        });

      });

      describe('with an object', function() {

        it('it should set it correctly', function() {

          var saga = new SagaModel('123456');

          saga.set({ tree: 'a', bee: { oh: '3' } });
          expect(saga.get('tree')).to.eql('a');
          expect(saga.get('bee.oh')).to.eql('3');

        });

      });

    });

    describe('calling toJSON', function() {

      it('it should return all attributes as Javascript object', function() {

        var saga = new SagaModel('123456');
        saga.set('data', 'other stuff');
        saga.set('deeper', { a: 'b' });
        
        saga.setCommitStamp(new Date(2014, 3, 17));
        saga.addTimeout(new Date(2014, 3, 2), [{ id: '321' }, { id: '432' }]);
        
        var json = saga.toJSON();

        expect(json.id).to.eql('123456');
        expect(json.data).to.eql('other stuff');
        expect(json.deeper.a).to.eql('b');
        expect(json._commitStamp.getTime()).to.eql((new Date(2014, 3, 17)).getTime());
        expect(json._timeoutAt.getTime()).to.eql((new Date(2014, 3, 2)).getTime());
        expect(json._timeoutCommands).to.be.an('array');
        expect(json._timeoutCommands.length).to.eql(2);
        expect(json._timeoutCommands[0].id).to.eql('321');
        expect(json._timeoutCommands[1].id).to.eql('432');

      });

    });

    describe('calling destroy', function() {

      it('it should mark the vm as to be deleted', function() {

        var saga = new SagaModel('123456');

        expect(saga.isDestroyed()).to.eql(false);

        saga.destroy();

        expect(saga.isDestroyed()).to.eql(true);

      });

    });

    describe('mark saga as destroyed', function () {

      it('it should work as expected', function () {

        var saga = new SagaModel('1234456745');

        expect(saga.isDestroyed()).to.eql(false);

        saga.destroy();

        expect(saga.isDestroyed()).to.eql(true);

      });

    });
    
    describe('working with unsent commands', function () {
      
      it('it should work as expected', function () {
        
        var saga = new SagaModel('1234');
        var cmds = saga.getUndispatchedCommands();
        
        expect(cmds).to.be.an('array');
        expect(cmds.length).to.eql(0);
        
        var first = { id: '13334' };
        saga.addUnsentCommand(first);
        saga.addUnsentCommand({ id: '22114' });
        cmds = saga.getUndispatchedCommands();

        expect(cmds).to.be.an('array');
        expect(cmds.length).to.eql(2);
        expect(cmds[0].id).to.eql('13334');
        expect(cmds[1].id).to.eql('22114');
        
        saga.removeUnsentCommand(first);
        cmds = saga.getUndispatchedCommands();

        expect(cmds).to.be.an('array');
        expect(cmds.length).to.eql(1);
        expect(cmds[0].id).to.eql('22114');
        
      });
      
    });

    describe('working with commitStamp', function () {

      it('it should work as expected', function () {

        var saga = new SagaModel('1234');
        var stamp = saga.getCommitStamp();

        expect(stamp).not.to.be.ok();
        
        saga.setCommitStamp(new Date(2014, 2, 5));
        
        stamp = saga.getCommitStamp();

        expect(stamp.getTime()).to.eql((new Date(2014, 2, 5)).getTime());

      });

    });

    describe('working with timeout', function () {

      it('it should work as expected', function () {

        var saga = new SagaModel('1234');
        var timeout = saga.getTimeoutAt();
        var cmds = saga.getTimeoutCommands();

        expect(timeout).not.to.be.ok();
        expect(cmds).not.to.be.ok();

        saga.addTimeout(new Date(2014, 1, 15), [{ id: '111' }, { id: '222' }]);
        timeout = saga.getTimeoutAt();
        cmds = saga.getTimeoutCommands();

        expect(timeout.getTime()).to.eql((new Date(2014, 1, 15)).getTime());
        expect(cmds).to.be.an('array');
        expect(cmds.length).to.eql(2);
        expect(cmds[0].id).to.eql('111');
        expect(cmds[1].id).to.eql('222');
        
        saga.removeTimeout();
        
        expect(saga.getTimeoutAt()).to.eql(undefined);
        expect(saga.getTimeoutCommands()).to.eql(undefined);

      });

    });

  });

});
```

## File: `test/unit/sagaStoreTest.js`
```javascript
var expect = require('expect.js'),
  async = require('async'),
  _ = require('lodash'),
  sagastore = require('../../lib/store'),
  ConcurrencyError = require('../../lib/errors/concurrencyError'),
  Base = require('../../lib/store/base'),
  InMemory = require('../../lib/store/databases/inmemory');

describe('sagaStore', function() {

  it('it should have the correct interface', function() {

    expect(sagastore).to.be.an('object');
    expect(sagastore.create).to.be.a('function');
    expect(sagastore.Store).to.eql(Base);

  });

  describe('calling create', function() {

    describe('without options', function() {

      it('it should return with the in memory queue', function() {

        var lock = sagastore.create();
        expect(lock).to.be.a('object');

      });

      describe('but with a callback', function() {

        it('it should callback with lock object', function(done) {

          sagastore.create(function(err, lock) {
            expect(err).not.to.be.ok();
            expect(lock).to.be.a('object');
            done();
          });

        });

      });

    });

    describe('with options of a non existing db implementation', function() {

      it('it should throw an error', function() {

        expect(function() {
          sagastore.create({ type: 'strangeDb' });
        }).to.throwError();

      });

      it('it should callback with an error', function(done) {

        expect(function() {
          sagastore.create({ type: 'strangeDb' }, function(err) {
            expect(err).to.be.ok();
            done();
          });
        }).to.throwError();

      });

    });

    describe('with options of an own db implementation', function() {

      it('it should return with the an instance of that implementation', function() {

        var store = sagastore.create({ type: InMemory });
        expect(store).to.be.a(InMemory);

      });

    });

    describe('with options containing a type property with the value of', function() {

      var types = ['inmemory', 'mongodb', 'redis'/*, 'azuretable'*/];

      types.forEach(function(type) {

        describe('"' + type + '"', function() {

          var store;

          describe('without callback', function() {

            afterEach(function(done) {
              store.disconnect(done);
            });

            it('it should return with the correct lock', function() {

              store = sagastore.create({ type: type });
              expect(store).to.be.a('object');
              expect(store).to.be.a(Base);
              expect(store.connect).to.be.a('function');
              expect(store.disconnect).to.be.a('function');
              expect(store.getNewId).to.be.a('function');
              expect(store.remove).to.be.a('function');
              expect(store.save).to.be.a('function');
              expect(store.getTimeoutedSagas).to.be.a('function');
              expect(store.getOlderSagas).to.be.a('function');
              expect(store.getUndispatchedCommands).to.be.a('function');
              expect(store.setCommandToDispatched).to.be.a('function');

            });

          });

          describe('with callback', function() {

            afterEach(function(done) {
              store.disconnect(done);
            });

            it('it should return with the correct lock', function(done) {

              sagastore.create({ type: type }, function(err, resS) {
                expect(err).not.to.be.ok();
                store = resS;
                expect(store).to.be.a('object');
                done();
              });

            });

          });

          describe('calling connect', function () {

            afterEach(function(done) {
              store.disconnect(done);
            });

            describe('with a callback', function () {

              it('it should callback successfully', function(done) {

                store = sagastore.create({ type: type });
                store.connect(function (err) {
                  expect(err).not.to.be.ok();
                  done();
                });

              });

            });

            describe('without a callback', function () {

              it('it should emit connect', function(done) {

                store = sagastore.create({ type: type });
                store.once('connect', done);
                store.connect();

              });

            });

          });

          describe('having connected', function() {

            describe('calling disconnect', function() {

              beforeEach(function(done) {
                store = sagastore.create({ type: type });
                store.connect(done);
              });

              it('it should callback successfully', function(done) {

                store.disconnect(function(err) {
                  expect(err).not.to.be.ok();
                  done();
                });

              });

              it('it should emit disconnect', function(done) {

                store.once('disconnect', done);
                store.disconnect();

              });

            });

            describe('using the lock', function() {

              before(function(done) {
                store = sagastore.create({ type: type });
                store.connect(done);
              });

              describe('calling getNewId', function() {

                it('it should callback with a new Id as string', function(done) {

                  store.getNewId(function(err, id) {
                    expect(err).not.to.be.ok();
                    expect(id).to.be.a('string');
                    done();
                  });

                });

              });

              describe('having no entries', function() {

                before(function(done) {
                  store.clear(done);
                });

                describe('calling get', function() {

                  describe('without a valid id', function () {

                    it('it should callback with an error', function (done) {

                      store.get({}, function(err) {
                        expect(err).to.be.ok();
                        expect(err.message).to.match(/id/);
                        done();
                      });

                    });

                  });

                  describe('with a valid id', function () {

                    it('it should callback without an error', function (done) {

                      store.get('123', function(err, saga) {
                        expect(err).not.to.be.ok();
                        expect(saga).to.eql(null);
                        done();
                      });

                    });

                  });

                });

                describe('calling getTimeoutedSagas', function() {

                  it('it should callback with an empty array', function(done) {

                    store.getTimeoutedSagas(function(err, sagas) {
                      expect(err).not.to.be.ok();
                      expect(sagas).to.be.an('array');
                      expect(sagas).to.have.length(0);
                      done();
                    });

                  });

                });

                describe('calling getUndispatchedCommands', function() {

                  it('it should callback with an empty array', function(done) {

                    store.getUndispatchedCommands(function(err, cmds) {
                      expect(err).not.to.be.ok();
                      expect(cmds).to.be.an('array');
                      expect(cmds).to.have.length(0);
                      done();
                    });

                  });

                });

                describe('calling getOlderSagas', function() {

                  describe('without a valid date object', function () {

                    it('it should callback with an error', function (done) {

                      store.getOlderSagas({}, function(err, sagas) {
                        expect(err).to.be.ok();
                        expect(err.message).to.match(/date/);
                        expect(sagas).not.to.be.ok();
                        done();
                      });

                    });

                  });

                  describe('with a valid date object', function () {

                    it('it should callback without an error', function (done) {

                      store.getOlderSagas(new Date(), function(err, sagas) {
                        expect(err).not.to.be.ok();
                        expect(sagas).to.be.an('array');
                        expect(sagas).to.have.length(0);
                        done();
                      });

                    });

                  });

                });

                describe('calling remove', function() {

                  describe('without a valid id object', function () {

                    it('it should callback with an error', function (done) {

                      store.remove({}, function(err) {
                        expect(err).to.be.ok();
                        expect(err.message).to.match(/id/);
                        done();
                      });

                    });

                  });

                  describe('with a valid id string', function () {

                    it('it should callback without an error', function (done) {

                      store.remove('123', function(err) {
                        expect(err).not.to.be.ok();
                        done();
                      });

                    });

                  });

                });

                describe('calling save', function() {

                  describe('without a valid saga object', function () {

                    it('it should callback with an error', function (done) {

                      store.save({}, true, function(err) {
                        expect(err).to.be.ok();
                        expect(err.message).to.match(/id/);
                        done();
                      });

                    });

                  });

                  describe('without a valid commands object', function () {

                    it('it should callback with an error', function (done) {

                      store.save({ id: '1234', _commitStamp: new Date() }, [{}], function(err) {
                        expect(err).to.be.ok();
                        expect(err.message).to.match(/command/);
                        done();
                      });

                    });

                  });

                  describe('with valid arguments', function () {

                    it('it should callback without an error', function (done) {

                      store.save({ id: '1234', _commitStamp: new Date() }, [{ id: '234', payload: { id: '234' } }], function(err, nothing) {
                      expect(err).not.to.be.ok();
                      expect(nothing).to.eql(undefined);
                        done();
                      });

                    });

                  });

                });

                describe('calling setCommandToDispatched', function() {

                  describe('without a valid commandId', function () {

                    it('it should callback with an error', function (done) {

                      store.setCommandToDispatched({}, true, function(err) {
                        expect(err).to.be.ok();
                        expect(err.message).to.match(/command id/);
                        done();
                      });

                    });

                  });

                  describe('without a valid sagaId', function () {

                    it('it should callback with an error', function (done) {

                      store.setCommandToDispatched('123', true, function(err) {
                        expect(err).to.be.ok();
                        expect(err.message).to.match(/saga id/);
                        done();
                      });

                    });

                  });

                  describe('with valid arguments', function () {

                    it('it should callback without an error', function (done) {

                      store.setCommandToDispatched('1234', '4356', function(err, nothing) {
                      expect(err).not.to.be.ok();
                      expect(nothing).to.eql(undefined);
                        done();
                      });

                    });

                  });

                });

              });

              describe('having some saved sagas', function() {

                var saga1;
                var cmds1;

                var saga2;
                var cmds2;

                var saga3;
                var cmds3;

                var saga4;
                var cmds4;

                beforeEach(function (done) {
                  saga1 = { id: 'sagaId1', _commitStamp: new Date(2014, 3, 1), _timeoutAt: new Date(2214, 3, 17), data: 'sagaData1' };
                  cmds1 = [{ id: 'cmdId1', payload: { id: 'cmdId1', data: 'cmdData1' } }];

                  saga2 = { id: 'sagaId2', _commitStamp: new Date(2014, 3, 2), _timeoutAt: new Date(2014, 3, 15), data: 'sagaData2' };
                  cmds2 = [{ id: 'cmdId2', payload: { id: 'cmdId2', data: 'cmdData2' } }, { id: 'cmdId22', payload: { id: 'cmdId22', data: 'cmdData22' } }];

                  saga3 = { id: 'sagaId3', _commitStamp: new Date(2014, 3, 5), data: 'sagaData3' };
                  cmds3 = [{ id: 'cmdId3', payload: { id: 'cmdId3', data: 'cmdData3' } }];

                  saga4 = { id: 'sagaId4', _commitStamp: new Date(2014, 3, 7), data: 'sagaData4' };
                  cmds4 = [];

                  store.clear(function () {
                    async.series([
                      function (callback) {
                        store.save(saga1, cmds1, callback);
                      },
                      function (callback) {
                        store.save(saga2, cmds2, callback);
                      },
                      function (callback) {
                        store.save(saga3, cmds3, callback);
                      },
                      function (callback) {
                        store.save(saga4, cmds4, callback);
                      }
                    ], done);
                  });
                });

                describe('calling get', function () {

                  it('it should callback the requested saga object', function (done) {

                    store.get('sagaId1', function (err, saga) {
                      expect(err).not.to.be.ok();
                      expect(saga).to.be.an('object');
                      expect(saga.id).to.eql(saga1.id);
                      expect(saga._commitStamp.getTime()).to.eql(saga1._commitStamp.getTime());
                      expect(saga._timeoutAt.getTime()).to.eql(saga1._timeoutAt.getTime());
                      expect(saga.data).to.eql(saga1.data);
                      done();
                    });

                  });

                });

                describe('calling getTimeoutedSagas', function () {

                  it('it should callback all the timeouted sagas', function (done) {

                    store.getTimeoutedSagas(function (err, sagas) {
                      expect(err).not.to.be.ok();
                      expect(sagas).to.be.an('array');
                      expect(sagas.length).to.eql(1);
                      expect(sagas[0].id).to.eql(saga2.id);
                      expect(sagas[0]._commitStamp.getTime()).to.eql(saga2._commitStamp.getTime());
                      expect(sagas[0]._timeoutAt.getTime()).to.eql(saga2._timeoutAt.getTime());
                      expect(sagas[0].data).to.eql(saga2.data);
                      done();
                    });

                  });

                });

                describe('calling getUndispatchedCommands', function () {

                  it('it should callback with the expected commands', function (done) {

                    store.getUndispatchedCommands(function (err, cmds) {
                      expect(err).not.to.be.ok();
                      expect(cmds).to.be.an('array');
                      expect(cmds.length).to.eql(4);
                      expect(cmds[0].sagaId).to.eql(saga1.id);
                      expect(cmds[0].commandId).to.eql(cmds1[0].id);
                      expect(cmds[0].commitStamp.getTime()).to.eql(saga1._commitStamp.getTime());
                      expect(cmds[0].command.id).to.eql(cmds1[0].payload.id);
                      expect(cmds[0].command.data).to.eql(cmds1[0].payload.data);
                      expect(cmds[1].sagaId).to.eql(saga2.id);
                      expect(cmds[1].commandId).to.eql(cmds2[0].id);
                      expect(cmds[1].commitStamp.getTime()).to.eql(saga2._commitStamp.getTime());
                      expect(cmds[1].command.id).to.eql(cmds2[0].payload.id);
                      expect(cmds[1].command.data).to.eql(cmds2[0].payload.data);
                      expect(cmds[2].sagaId).to.eql(saga2.id);
                      expect(cmds[2].commandId).to.eql(cmds2[1].id);
                      expect(cmds[2].commitStamp.getTime()).to.eql(saga2._commitStamp.getTime());
                      expect(cmds[2].command.id).to.eql(cmds2[1].payload.id);
                      expect(cmds[2].command.data).to.eql(cmds2[1].payload.data);
                      expect(cmds[3].sagaId).to.eql(saga3.id);
                      expect(cmds[3].commandId).to.eql(cmds3[0].id);
                      expect(cmds[3].commitStamp.getTime()).to.eql(saga3._commitStamp.getTime());
                      expect(cmds[3].command.id).to.eql(cmds3[0].payload.id);
                      expect(cmds[3].command.data).to.eql(cmds3[0].payload.data);

                      if (type === 'azuretable') return done();

                      store.getUndispatchedCommands({ skip: 1, limit: 2 }, function (err, cmds) {
                        expect(err).not.to.be.ok();
                        expect(cmds).to.be.an('array');
                        if (type === 'mongodb') {
                          expect(cmds.length).to.eql(3);
                        } else {
                          expect(cmds.length).to.eql(2);
                        }

                        expect(cmds[0].sagaId).to.eql(saga2.id);
                        expect(cmds[0].commandId).to.eql(cmds2[0].id);
                        expect(cmds[0].commitStamp.getTime()).to.eql(saga2._commitStamp.getTime());
                        expect(cmds[0].command.id).to.eql(cmds2[0].payload.id);
                        expect(cmds[0].command.data).to.eql(cmds2[0].payload.data);
                        expect(cmds[1].sagaId).to.eql(saga2.id);
                        expect(cmds[1].commandId).to.eql(cmds2[1].id);
                        expect(cmds[1].commitStamp.getTime()).to.eql(saga2._commitStamp.getTime());
                        expect(cmds[1].command.id).to.eql(cmds2[1].payload.id);
                        expect(cmds[1].command.data).to.eql(cmds2[1].payload.data);

                        if (type === 'mongodb') {
                          expect(cmds[2].sagaId).to.eql(saga3.id);
                          expect(cmds[2].commandId).to.eql(cmds3[0].id);
                          expect(cmds[2].commitStamp.getTime()).to.eql(saga3._commitStamp.getTime());
                          expect(cmds[2].command.id).to.eql(cmds3[0].payload.id);
                          expect(cmds[2].command.data).to.eql(cmds3[0].payload.data);
                        }

                        done();
                      });
                    });

                  });

                });

                describe('calling getOlderSagas', function () {

                  it('it should callback the expected sagas', function (done) {

                    store.getOlderSagas(new Date(2014, 3, 3), function (err, sagas) {
                      expect(err).not.to.be.ok();
                      expect(sagas).to.be.an('array');
                      expect(sagas.length).to.eql(2);
                      expect(sagas[0].id).to.eql(saga1.id);
                      expect(sagas[0]._commitStamp.getTime()).to.eql(saga1._commitStamp.getTime());
                      expect(sagas[0]._timeoutAt.getTime()).to.eql(saga1._timeoutAt.getTime());
                      expect(sagas[0].data).to.eql(saga1.data);
                      expect(sagas[1].id).to.eql(saga2.id);
                      expect(sagas[1]._commitStamp.getTime()).to.eql(saga2._commitStamp.getTime());
                      expect(sagas[1]._timeoutAt.getTime()).to.eql(saga2._timeoutAt.getTime());
                      expect(sagas[1].data).to.eql(saga2.data);

                      done();
                    });

                  });

                });

                describe('calling setCommandToDispatched', function () {

                  it('it should remove this command from store', function (done) {

                    store.setCommandToDispatched('cmdId2', 'sagaId2', function (err) {
                      expect(err).not.to.be.ok();

                      store.getUndispatchedCommands(function (err, cmds) {
                        expect(err).not.to.be.ok();
                        expect(cmds).to.be.an('array');
                        expect(cmds.length).to.eql(3);
                        expect(cmds[0].sagaId).to.eql(saga1.id);
                        expect(cmds[0].commandId).to.eql(cmds1[0].id);
                        expect(cmds[0].command.id).to.eql(cmds1[0].payload.id);
                        expect(cmds[0].command.data).to.eql(cmds1[0].payload.data);
                        expect(cmds[1].sagaId).to.eql(saga2.id);
                        expect(cmds[1].commandId).to.eql(cmds2[1].id);
                        expect(cmds[1].command.id).to.eql(cmds2[1].payload.id);
                        expect(cmds[1].command.data).to.eql(cmds2[1].payload.data);
                        expect(cmds[2].sagaId).to.eql(saga3.id);
                        expect(cmds[2].commandId).to.eql(cmds3[0].id);
                        expect(cmds[2].command.id).to.eql(cmds3[0].payload.id);
                        expect(cmds[2].command.data).to.eql(cmds3[0].payload.data);

                        done();
                      });
                    });

                  });

                });

                describe('calling remove', function () {

                  it('it should remove the requesting saga and its commands', function (done) {

                    store.remove('sagaId2', function (err) {
                      expect(err).not.to.be.ok();

                      store.get('sagaId2', function (err, saga) {
                        expect(err).not.to.be.ok();
                        expect(saga).to.eql(null);

                        store.getTimeoutedSagas(function (err, sagas) {
                          expect(err).not.to.be.ok();
                          expect(sagas).to.be.an('array');
                          expect(sagas.length).to.eql(0);

                          store.getOlderSagas(new Date(2314, 3, 17), function (err, sagas) {
                            expect(err).not.to.be.ok();
                            expect(sagas).to.be.an('array');
                            expect(sagas.length).to.eql(3);
                            expect(sagas[0].id).to.eql(saga1.id);
                            expect(sagas[0]._commitStamp.getTime()).to.eql(saga1._commitStamp.getTime());
                            expect(sagas[0]._timeoutAt.getTime()).to.eql(saga1._timeoutAt.getTime());
                            expect(sagas[0].data).to.eql(saga1.data);
                            expect(sagas[1].id).to.eql(saga3.id);
                            expect(sagas[1]._commitStamp.getTime()).to.eql(saga3._commitStamp.getTime());
                            expect(sagas[1].data).to.eql(saga3.data);
                            expect(sagas[2].id).to.eql(saga4.id);
                            expect(sagas[2]._commitStamp.getTime()).to.eql(saga4._commitStamp.getTime());
                            expect(sagas[2].data).to.eql(saga4.data);

                            store.getUndispatchedCommands(function (err, cmds) {
                              expect(err).not.to.be.ok();
                              expect(cmds).to.be.an('array');
                              expect(cmds.length).to.eql(2);
                              expect(cmds[0].sagaId).to.eql(saga1.id);
                              expect(cmds[0].commandId).to.eql(cmds1[0].id);
                              expect(cmds[0].command.id).to.eql(cmds1[0].payload.id);
                              expect(cmds[0].command.data).to.eql(cmds1[0].payload.data);
                              expect(cmds[1].sagaId).to.eql(saga3.id);
                              expect(cmds[1].commandId).to.eql(cmds3[0].id);
                              expect(cmds[1].command.id).to.eql(cmds3[0].payload.id);
                              expect(cmds[1].command.data).to.eql(cmds3[0].payload.data);

                              done();
                            });
                          });
                        });
                      });
                    });

                  });

                });

                describe('calling save', function () {

                  describe('but beeing updated by someone else in the meantime', function () {

                    it('it should callback with a concurrency error', function (done) {

                      store.get('sagaId4', function (err, saga) {
                        expect(err).not.to.be.ok();
                        var org = _.cloneDeep(saga);

                        saga.n = 'new';

                        store.save(saga, [], function (err) {
                          expect(err).not.to.be.ok();
                          org.n = 'other';
                          store.save(org, [], function (err) {
                            expect(err).to.be.a(ConcurrencyError);

                            done();
                          });
                        });
                      });

                    });

                  });

                  describe('but beeing updated by someone else in the meantime and creating with the same id', function() {

                    it('it should callback with a concurrency error', function (done) {

                      var s1 = { id: 'mySagaId', _commitStamp: new Date(2014, 3, 7), data: 'bla' };
                      var s2 = { id: 'mySagaId', _commitStamp: new Date(2014, 3, 7), data: 'bla2' };

                      store.save(s1, [], function (err) {
                        expect(err).not.to.be.ok();
                        store.save(s2, [], function (err) {
                          expect(err).to.be.a(ConcurrencyError);
                          done();
                        });
                      });

                    });

                  });

                });

              });

            });

          });

        });

      });

    });

  });

});
```

## File: `test/unit/definitions/definitionBaseTest.js`
```javascript
var expect = require('expect.js'),
  _ = require('lodash'),
  DefinitionBase = require('../../../lib/definitionBase');

describe('base definition', function () {

  describe('creating a new definition', function () {

    it('it should not throw an error', function () {

      expect(function () {
        new DefinitionBase();
      }).not.to.throwError();

    });

    it('it should return a correct object', function () {

      var def = new DefinitionBase();
      expect(def.definitions).to.be.an('object');
      expect(def.definitions.command).to.be.an('object');
      expect(def.definitions.event).to.be.an('object');
      expect(def.defineCommand).to.be.a('function');
      expect(def.defineEvent).to.be.a('function');
      expect(def.defineOptions).to.be.a('function');

    });

    describe('passing a name in meta infos', function () {

      it('it should return a correct object', function () {

        var def = new DefinitionBase({ name: 'myName' });
        expect(def.name).to.eql('myName');
        expect(def.definitions).to.be.an('object');
        expect(def.definitions.command).to.be.an('object');
        expect(def.definitions.event).to.be.an('object');
        expect(def.defineCommand).to.be.a('function');
        expect(def.defineEvent).to.be.a('function');
        expect(def.defineOptions).to.be.a('function');

      });

    });

    describe('defining options', function() {

      var def;

      beforeEach(function () {
        def = new DefinitionBase({ name: 'myName' });
      });

      it('it should work as expected', function() {

        def.defineOptions({
          my: 'options',
          of: {
            some: 'deep'
          }
        });

        expect(def.options.my).to.eql('options');
        expect(def.options.of.some).to.eql('deep');

      });

    });

    describe('defining the command structure', function() {

      var def;

      beforeEach(function () {
        def = new DefinitionBase({ name: 'myName' });
      });

      describe('using the defaults', function () {

        it('it should apply the defaults', function() {

          var defaults = _.cloneDeep(def.definitions.command);

          def.defineCommand({
            meta: 'pass'
          });

          expect(defaults.id).to.eql(def.definitions.command.id);
          expect(def.definitions.command.meta).to.eql('pass');
          expect(defaults.meta).not.to.eql(def.definitions.command.meta);

        });

      });

      describe('overwriting the defaults', function () {

        it('it should apply them correctly', function() {

          var defaults = _.cloneDeep(def.definitions.command);

          def.defineCommand({
            id: 'commandId',
            meta: 'pass'
          });

          expect(def.definitions.command.id).to.eql('commandId');
          expect(defaults.id).not.to.eql(def.definitions.command.id);
          expect(def.definitions.command.meta).to.eql('pass');
          expect(defaults.meta).not.to.eql(def.definitions.command.meta);

        });

      });

    });

    describe('defining the event structure', function() {

      var def;

      beforeEach(function () {
        def = new DefinitionBase({ name: 'myName' });
      });

      describe('using the defaults', function () {

        it('it should apply the defaults', function() {

          var defaults = _.cloneDeep(def.definitions.event);

          def.defineEvent({
            aggregate: 'aggName',
            context: 'ctx.Name',
            version: 'v.',
            meta: 'pass'
          });

          expect(defaults.name).to.eql(def.definitions.event.name);
          expect(def.definitions.event.aggregate).to.eql('aggName');
          expect(defaults.aggregate).not.to.eql(def.definitions.event.aggregate);
          expect(def.definitions.event.context).to.eql('ctx.Name');
          expect(defaults.context).not.to.eql(def.definitions.event.context);
          expect(def.definitions.event.version).to.eql('v.');
          expect(defaults.version).not.to.eql(def.definitions.event.version);
          expect(def.definitions.event.meta).to.eql('pass');
          expect(defaults.meta).not.to.eql(def.definitions.event.meta);

        });

      });

      describe('overwriting the defaults', function () {

        it('it should apply them correctly', function() {

          var defaults = _.cloneDeep(def.definitions.event);

          def.defineEvent({
            id: 'eventId',
            name: 'defName',
            aggregate: 'aggName',
            context: 'ctx.Name',
            version: 'v.',
            meta: 'pass'
          });

          expect(def.definitions.event.name).to.eql('defName');
          expect(defaults.name).not.to.eql(def.definitions.event.name);
          expect(def.definitions.event.aggregate).to.eql('aggName');
          expect(defaults.aggregate).not.to.eql(def.definitions.event.aggregate);
          expect(def.definitions.event.context).to.eql('ctx.Name');
          expect(defaults.context).not.to.eql(def.definitions.event.context);
          expect(def.definitions.event.version).to.eql('v.');
          expect(defaults.version).not.to.eql(def.definitions.event.version);
          expect(def.definitions.event.meta).to.eql('pass');
          expect(defaults.meta).not.to.eql(def.definitions.event.meta);

        });

      });

    });

  });

});
```

## File: `test/unit/definitions/sagaTest.js`
```javascript
var expect = require('expect.js'),
  _ = require('lodash'),
  DefinitionBase = require('../../../lib/definitionBase'),
  Saga = require('../../../lib/definitions/saga'),
  sagaStore = require('../../../lib/store').create(),
  api = require('../../../');

describe('saga definition', function () {

  describe('creating a new saga definition', function () {

    describe('without any arguments', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.defineSaga();
        }).to.throwError(/function/);

      });

    });

    describe('without saga function', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.defineSaga(null);
        }).to.throwError(/function/);

      });

    });

    describe('with a wrong saga function', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.defineSaga(null, 'not a function');
        }).to.throwError(/function/);

      });

    });

    describe('with a correct saga function', function () {

      it('it should not throw an error', function () {

        expect(function () {
          api.defineSaga(null, function () {});
        }).not.to.throwError();

      });

      it('it should return a correct object', function () {

        var sagaFn = function () {};
        var saga = api.defineSaga(null, sagaFn);
        expect(saga).to.be.a(DefinitionBase);
        expect(saga).to.be.a(Saga);
        expect(saga.sagaFn).to.be.a('function');
        expect(saga.definitions).to.be.an('object');
        expect(saga.definitions.command).to.be.an('object');
        expect(saga.definitions.event).to.be.an('object');
        expect(saga.defineCommand).to.be.a('function');
        expect(saga.defineEvent).to.be.a('function');
        expect(saga.defineOptions).to.be.a('function');

        expect(saga.handle).to.be.a('function');
        expect(saga.useAsId).to.be.a('function');

      });

    });

    describe('with some meta infos and a correct saga function', function () {

      it('it should not throw an error', function () {

        expect(function () {
          api.defineSaga({ name: 'eventName', version: 3 }, function () {});
        }).not.to.throwError();

      });

      it('it should return a correct object', function () {

        var sagaFn = function () {};
        var saga = api.defineSaga({ name: 'commandName', version: 3 }, sagaFn);
        expect(saga).to.be.a(DefinitionBase);
        expect(saga).to.be.a(Saga);
        expect(saga.sagaFn).to.be.a('function');
        expect(saga.definitions).to.be.an('object');
        expect(saga.definitions.command).to.be.an('object');
        expect(saga.definitions.event).to.be.an('object');
        expect(saga.defineCommand).to.be.a('function');
        expect(saga.defineEvent).to.be.a('function');
        expect(saga.defineOptions).to.be.a('function');

        expect(saga.idGenerator).to.be.a('function');
        expect(saga.handle).to.be.a('function');
        expect(saga.useSagaStore).to.be.a('function');

      });

    });

    describe('defining an id generator function', function() {

      var saga;

      beforeEach(function () {
        var sagaFn = function () {};
        saga = api.defineSaga({ name: 'eventName', version: 3 }, sagaFn);
        saga.getNewId = null;
      });

      describe('in a synchronous way', function() {

        it('it should be transformed internally to an asynchronous way', function(done) {

          saga.idGenerator(function () {
            var id = require('uuid').v4().toString();
            return id;
          });

          saga.getNewId(function (err, id) {
            expect(id).to.be.a('string');
            done();
          });

        });

      });

      describe('in an synchronous way', function() {

        it('it should be taken as it is', function(done) {

          saga.idGenerator(function (callback) {
            setTimeout(function () {
              var id = require('uuid').v4().toString();
              callback(null, id);
            }, 10);
          });

          saga.getNewId(function (err, id) {
            expect(id).to.be.a('string');
            done();
          });

        });

      });

    });

    describe('defining an use as id function', function() {

      var saga;

      beforeEach(function () {
        var sagaFn = function () {};
        saga = api.defineSaga({ name: 'eventName', version: 3 }, sagaFn);
        saga.getNewIdForThisSaga = null;
      });

      describe('in a synchronous way', function() {

        it('it should be transformed internally to an asynchronous way', function(done) {

          saga.useAsId(function (evt) {
            expect(evt.my).to.eql('evt');
            var id = require('uuid').v4().toString();
            return id;
          });

          saga.getNewIdForThisSaga({ my: 'evt' }, function (err, id) {
            expect(id).to.be.a('string');
            done();
          });

        });

      });

      describe('in an synchronous way', function() {

        it('it should be taken as it is', function(done) {

          saga.useAsId(function (evt, callback) {
            expect(evt.my).to.eql('evt');
            setTimeout(function () {
              var id = require('uuid').v4().toString();
              callback(null, id);
            }, 10);
          });

          saga.getNewIdForThisSaga({ my: 'evt' }, function (err, id) {
            expect(id).to.be.a('string');
            done();
          });

        });

      });

    });

    describe('handling an event', function () {

      var saga;

      before(function (done) {
        sagaStore.connect(done);
      });

      describe('in a saga', function () {

        describe('that defines containsProperties', function () {

          describe('not matching', function () {

            it('it should work as expected', function (done) {
              var sagaFn = function () {
                expect(this.retry).to.be.a('function');
              };
              saga = api.defineSaga({
                name: 'eventName',
                version: 3,
                payload: 'p',
                containingProperties: ['aggId']
              }, sagaFn);

              saga.useSagaStore(sagaStore);

              saga.handle({}, function (err, sagaModel) {
                expect(err).not.to.be.ok();
                expect(sagaModel).not.to.be.ok();
                done();
              });
            });

          });

          describe('matching', function () {

            it('it should work as expected', function (done) {

              var fnCalled = false;
              var sagaId = null;
              var sagaFn = function (e, s, clb) {
                expect(this.retry).to.be.a('function');
                expect(e.aggId).to.eql('123');
                expect(s.id).to.be.a('string');
                sagaId = s.id;
                fnCalled = true;
                clb(null);
              };
              saga = api.defineSaga({
                name: 'eventName',
                version: 3,
                containingProperties: ['aggId']
              }, sagaFn);

              saga.useSagaStore(sagaStore);

              saga.handle({ aggId: '123' }, function (err, sagaModel) {
                expect(err).not.to.be.ok();
                expect(sagaModel.id).to.eql(sagaId);
                expect(fnCalled).to.eql(true);
                done();
              });
            });

          });

        });

        describe('that does not define containProperties', function () {

          describe('having defined an id', function () {

            it('it should it as saga id', function (done) {

              var fnCalled = false;
              var sagaFn = function (e, s, clb) {
                expect(this.retry).to.be.a('function');
                expect(e.aggId).to.eql('123');
                expect(s.id).to.eql('123');
                fnCalled = true;
                clb(null);
              };
              saga = api.defineSaga({
                name: 'eventName',
                version: 3,
                id: 'aggId'
              }, sagaFn);

              saga.useSagaStore(sagaStore);

              saga.handle({ aggId: '123' }, function (err, sagaModel) {
                expect(err).not.to.be.ok();
                expect(sagaModel.id).to.eql('123');
                expect(fnCalled).to.eql(true);
                done();
              });
            });

          });

          describe('having an existing saga', function () {

            before(function (done) {
              sagaStore.save({ id: '5647', _commitStamp: new Date(), my: 'data' }, [], done);
            });

            it('it should use the existing data in the saga', function (done) {

              var fnCalled = false;
              var sagaFn = function (e, s, clb) {
                expect(this.retry).to.be.a('function');
                expect(e.aggId).to.eql('5647');
                expect(s.id).to.eql('5647');
                expect(s.get('my')).to.eql('data');
                s.set('new', 'value');
                fnCalled = true;
                clb(null);
              };
              saga = api.defineSaga({
                name: 'eventName',
                version: 3,
                id: 'aggId'
              }, sagaFn);

              saga.useSagaStore(sagaStore);

              saga.handle({ aggId: '5647' }, function (err, sagaModel) {
                expect(err).not.to.be.ok();
                expect(sagaModel.id).to.eql('5647');
                expect(sagaModel.get('my')).to.eql('data');
                expect(sagaModel.get('new')).to.eql('value');
                expect(fnCalled).to.eql(true);
                done();
              });
            });

          });

          describe('calling saga.addCommandToSend in the handle function', function () {

            it('it should work as expected', function (done) {

              var fnCalled = false;
              var sagaFn = function (e, s, clb) {
                expect(this.retry).to.be.a('function');
                expect(e.aggId).to.eql('5647');
                expect(s.id).to.eql('5647');
                s.addCommandToSend({ c: 'data1' });
                s.addCommandToSend({ c: 'data2', meta: 'm' });
                fnCalled = true;
                clb(null);
              };
              saga = api.defineSaga({
                name: 'eventName',
                version: 3,
                id: 'aggId'
              }, sagaFn);
              saga.defineCommand({
                id: 'id',
                meta: 'meta'
              });
              saga.defineEvent({
                id: 'id',
                meta: 'meta'
              });

              saga.useSagaStore(sagaStore);

              saga.handle({ aggId: '5647', meta: 'evtMeta' }, function (err, sagaModel) {
                expect(err).not.to.be.ok();
                expect(sagaModel.id).to.eql('5647');
                var cmds = sagaModel.getUndispatchedCommands();
                expect(cmds.length).to.eql(2);
                expect(cmds[0].c).to.eql('data1');
                expect(cmds[0].meta).to.eql('evtMeta');
                expect(cmds[1].c).to.eql('data2');
                expect(cmds[1].meta).to.eql('m');
                expect(fnCalled).to.eql(true);
                done();
              });
            });

          });

          describe('calling saga.defineTimeout in the handle function', function () {

            describe('without command', function () {

              it('it should work as expected', function (done) {

                var fnCalled = false;
                var sagaFn = function (e, s, clb) {
                  expect(this.retry).to.be.a('function');
                  expect(e.aggId).to.eql('5647');
                  expect(s.id).to.eql('5647');
                  s.defineTimeout(new Date(2034, 8, 25));
                  fnCalled = true;
                  clb(null);
                };
                saga = api.defineSaga({
                  name: 'eventName',
                  version: 3,
                  id: 'aggId'
                }, sagaFn);
                saga.defineCommand({
                  id: 'id',
                  meta: 'meta'
                });
                saga.defineEvent({
                  id: 'id',
                  meta: 'meta'
                });

                saga.useSagaStore(sagaStore);

                saga.handle({ aggId: '5647', meta: 'evtMeta' }, function (err, sagaModel) {
                  expect(err).not.to.be.ok();
                  expect(sagaModel.id).to.eql('5647');
                  var cmds = sagaModel.getTimeoutCommands();
                  expect(cmds.length).to.eql(0);
                  var timeout = sagaModel.getTimeoutAt();
                  expect(timeout.getTime()).to.eql((new Date(2034, 8, 25)).getTime());
                  expect(fnCalled).to.eql(true);
                  done();
                });
              });

            });

            describe('with one command', function () {

              it('it should work as expected', function (done) {

                var fnCalled = false;
                var sagaFn = function (e, s, clb) {
                  expect(this.retry).to.be.a('function');
                  expect(e.aggId).to.eql('5647');
                  expect(s.id).to.eql('5647');
                  s.defineTimeout(new Date(2034, 8, 23), { c: 'data1' });
                  fnCalled = true;
                  clb(null);
                };
                saga = api.defineSaga({
                  name: 'eventName',
                  version: 3,
                  id: 'aggId'
                }, sagaFn);
                saga.defineCommand({
                  id: 'id',
                  meta: 'meta'
                });
                saga.defineEvent({
                  id: 'id',
                  meta: 'meta'
                });

                saga.useSagaStore(sagaStore);

                saga.handle({ aggId: '5647', meta: 'evtMeta' }, function (err, sagaModel) {
                  expect(err).not.to.be.ok();
                  expect(sagaModel.id).to.eql('5647');
                  var cmds = sagaModel.getTimeoutCommands();
                  expect(cmds.length).to.eql(1);
                  expect(cmds[0].c).to.eql('data1');
                  expect(cmds[0].meta).to.eql('evtMeta');
                  var timeout = sagaModel.getTimeoutAt();
                  expect(timeout.getTime()).to.eql((new Date(2034, 8, 23)).getTime());
                  expect(fnCalled).to.eql(true);
                  done();
                });
              });

            });

            describe('with mutliple commands', function () {

              it('it should work as expected', function (done) {

                var fnCalled = false;
                var sagaFn = function (e, s, clb) {
                  expect(this.retry).to.be.a('function');
                  expect(e.aggId).to.eql('5647');
                  expect(s.id).to.eql('5647');
                  s.defineTimeout(new Date(2034, 8, 27), [{ c: 'data1' }, { c: 'data2', meta: 'm' }]);
                  fnCalled = true;
                  clb(null);
                };
                saga = api.defineSaga({
                  name: 'eventName',
                  version: 3,
                  id: 'aggId'
                }, sagaFn);
                saga.defineCommand({
                  id: 'id',
                  meta: 'meta'
                });
                saga.defineEvent({
                  id: 'id',
                  meta: 'meta'
                });

                saga.useSagaStore(sagaStore);

                saga.handle({ aggId: '5647', meta: 'evtMeta' }, function (err, sagaModel) {
                  expect(err).not.to.be.ok();
                  expect(sagaModel.id).to.eql('5647');
                  var cmds = sagaModel.getTimeoutCommands();
                  expect(cmds.length).to.eql(2);
                  expect(cmds[0].c).to.eql('data1');
                  expect(cmds[0].meta).to.eql('evtMeta');
                  expect(cmds[1].c).to.eql('data2');
                  expect(cmds[1].meta).to.eql('m');
                  var timeout = sagaModel.getTimeoutAt();
                  expect(timeout.getTime()).to.eql((new Date(2034, 8, 27)).getTime());
                  expect(fnCalled).to.eql(true);
                  done();
                });
              });

            });

          });

          describe('calling saga.commit in the handle function', function () {

            describe('having destroyed the saga', function () {

              before(function (done) {
                sagaStore.save({ id: '9361', _commitStamp: new Date(), my: 'data' }, [], done);
              });

              it('it should work as expected', function (done) {

                var fnCalled = false;
                var sagaFn = function (e, s, clb) {
                  expect(this.retry).to.be.a('function');
                  expect(e.aggId).to.eql('9361');
                  expect(s.id).to.eql('9361');
                  s.destroy();
                  fnCalled = true;
                  s.commit(clb);
                };
                saga = api.defineSaga({
                  name: 'eventName',
                  version: 3,
                  id: 'aggId'
                }, sagaFn);

                saga.useSagaStore(sagaStore);

                saga.handle({ aggId: '9361', meta: 'evtMeta' }, function (err, sagaModel) {
                  expect(err).not.to.be.ok();
                  expect(sagaModel.id).to.eql('9361');
                  expect(sagaModel.isDestroyed()).to.eql(true);
                  expect(fnCalled).to.eql(true);

                  sagaStore.get('9361', function (err, saga) {
                    expect(err).not.to.be.ok();
                    expect(saga).not.to.be.ok();
                    done();
                  });
                });
              });

            });

            describe('with some commands and data and timeout stuff', function () {

              it('it should work as expected', function (done) {

                var sagaId;
                var fnCalled = false;
                var sagaFn = function (e, s, clb) {
                  expect(this.retry).to.be.a('function');
                  expect(e.aggId).to.eql('5647');
                  expect(s.id).to.be.a('string');
                  sagaId = s.id;
                  s.addCommandToSend({ cS: 'data1S' });
                  s.addCommandToSend({ cS: 'data2S', meta: 'mS' });
                  s.defineTimeout(new Date(2034, 8, 27), [{ c: 'data1' }, { c: 'data2', meta: 'm' }]);
                  fnCalled = true;
                  s.commit(clb);
                };
                saga = api.defineSaga({
                  name: 'eventName',
                  version: 3
                }, sagaFn);
                saga.defineCommand({
                  id: 'id',
                  meta: 'meta'
                });
                saga.defineEvent({
                  id: 'id',
                  meta: 'meta'
                });

                saga.useSagaStore(sagaStore);

                saga.handle({ aggId: '5647', meta: 'evtMeta' }, function (err, sagaModel) {
                  expect(err).not.to.be.ok();
                  expect(sagaModel.id).to.eql(sagaId);
                  var cmdsT = sagaModel.getTimeoutCommands();
                  expect(cmdsT.length).to.eql(2);
                  expect(cmdsT[0].c).to.eql('data1');
                  expect(cmdsT[0].meta).to.eql('evtMeta');
                  expect(cmdsT[1].c).to.eql('data2');
                  expect(cmdsT[1].meta).to.eql('m');
                  var timeout = sagaModel.getTimeoutAt();
                  expect(timeout.getTime()).to.eql((new Date(2034, 8, 27)).getTime());

                  var cmds = sagaModel.getUndispatchedCommands();
                  expect(cmds.length).to.eql(2);
                  expect(cmds[0].cS).to.eql('data1S');
                  expect(cmds[0].meta).to.eql('evtMeta');
                  expect(cmds[1].cS).to.eql('data2S');
                  expect(cmds[1].meta).to.eql('mS');

                  expect(fnCalled).to.eql(true);

                  sagaStore.get(sagaId, function (err, saga) {
                    expect(err).not.to.be.ok();
                    expect(saga).to.be.an('object');
                    expect(saga.id).to.eql(sagaId);
                    var cmdsT = saga._timeoutCommands;
                    expect(cmdsT.length).to.eql(2);
                    expect(cmdsT[0].c).to.eql('data1');
                    expect(cmdsT[0].meta).to.eql('evtMeta');
                    expect(cmdsT[1].c).to.eql('data2');
                    expect(cmdsT[1].meta).to.eql('m');
                    var timeout = saga._timeoutAt;
                    expect(timeout.getTime()).to.eql((new Date(2034, 8, 27)).getTime());

                    done();
                  });
                });
              });

            });

          });

          describe('defining a payload', function () {

            it('it should work as expected', function (done) {

              var fnCalled = false;
              var sagaFn = function (e, s, clb) {
                expect(this.retry).to.be.a('function');
                expect(e).to.eql('abc');
                expect(s.id).to.be.a('string');
                fnCalled = true;
                clb(null);
              };
              saga = api.defineSaga({
                name: 'eventName',
                version: 3,
                payload: 'path'
              }, sagaFn);

              saga.useSagaStore(sagaStore);

              saga.handle({ aggId: '213', meta: 'evtMeta', path: 'abc' }, function (err, sagaModel) {
                expect(err).not.to.be.ok();
                expect(sagaModel.id).to.be.a('string');
                expect(fnCalled).to.eql(true);
                done();
              });
            });

          });

          describe('defining existing true', function () {

            describe('not having an existing', function () {

              it('it should work as expected', function (done) {

                var fnCalled = false;
                var sagaFn = function (e, s, clb) {
                  expect(this.retry).to.be.a('function');
                  expect(e).to.eql('abc');
                  expect(s.id).to.be.a('string');
                  fnCalled = true;
                  clb(null);
                };
                saga = api.defineSaga({
                  name: 'eventName',
                  version: 3,
                  payload: 'path',
                  existing: true,
                  id: 'aggId'
                }, sagaFn);

                saga.useSagaStore(sagaStore);

                saga.handle({ aggId: '9876', meta: 'evtMeta', path: 'abc' }, function (err, sagaModel) {
                  expect(err).not.to.be.ok();
                  expect(fnCalled).to.eql(false);
                  expect(sagaModel).not.to.be.ok();
                  done();
                });
              });

            });

            describe('having an existing', function () {

              before(function (done) {
                sagaStore.save({ id: '182734', _commitStamp: new Date() }, [], done);
              });

              it('it should work as expected', function (done) {

                var fnCalled = false;
                var sagaFn = function (e, s, clb) {
                  expect(this.retry).to.be.a('function');
                  expect(e).to.eql('abc');
                  expect(s.id).to.be.a('string');
                  fnCalled = true;
                  clb(null);
                };
                saga = api.defineSaga({
                  name: 'eventName',
                  version: 3,
                  payload: 'path',
                  existing: true,
                  id: 'aggId'
                }, sagaFn);

                saga.useSagaStore(sagaStore);

                saga.handle({ aggId: '182734', meta: 'evtMeta', path: 'abc' }, function (err, sagaModel) {
                  expect(err).not.to.be.ok();
                  expect(fnCalled).to.eql(true);
                  expect(sagaModel.id).to.eql('182734');
                  done();
                });
              });

            });

          });

          describe('calling retry during the handling', function () {

            it('it should work as expected', function (done) {

              var runs = 0;
              var fnCalled = false;
              var sagaFn = function (e, s, clb) {
                runs++;
                expect(this.retry).to.be.a('function');
                if (runs <= 3) {
                  return this.retry(1);
                }

                expect(e).to.eql('abc');
                expect(s.id).to.be.a('string');
                fnCalled = true;
                clb(null);
              };
              saga = api.defineSaga({
                name: 'eventName',
                version: 3,
                payload: 'path'
              }, sagaFn);

              saga.useSagaStore(sagaStore);

              saga.handle({ aggId: '213', meta: 'evtMeta', path: 'abc' }, function (err, sagaModel) {
                expect(err).not.to.be.ok();
                expect(sagaModel.id).to.be.a('string');
                expect(fnCalled).to.eql(true);

                expect(runs).to.eql(4);
                done();
              });
            });

          });

        });

        describe('that defines shouldHandleEvent', function () {

          describe('not matching', function () {

            it('it should work as expected', function (done) {
              var sagaFn = function () {
                expect(this.retry).to.be.a('function');
              };
              saga = api.defineSaga({
                name: 'eventName',
                version: 3,
                payload: 'p',
              }, sagaFn).defineShouldHandleEvent(function (evt) {                
                return evt.match;
              });

              saga.useSagaStore(sagaStore);

              saga.handle({ match: false }, function (err, sagaModel) {
                expect(err).not.to.be.ok();
                expect(sagaModel).not.to.be.ok();
                done();
              });
            });

          });

          describe('matching', function () {

            it('it should work as expected', function (done) {

              var fnCalled = false;
              var sagaId = null;
              var sagaFn = function (e, s, clb) {
                expect(this.retry).to.be.a('function');
                expect(e.aggId).to.eql('123');
                expect(s.id).to.be.a('string');
                sagaId = s.id;
                fnCalled = true;
                clb(null);
              };
              saga = api.defineSaga({
                name: 'eventName',
                version: 3,
              }, sagaFn).defineShouldHandleEvent(function (evt) {
                return evt.aggId === '123';
              })

              saga.useSagaStore(sagaStore);

              saga.handle({ aggId: '123' }, function (err, sagaModel) {
                expect(err).not.to.be.ok();
                expect(sagaModel.id).to.eql(sagaId);
                expect(fnCalled).to.eql(true);
                done();
              });
            });

          });

        });

      });

    });

  });

});
```


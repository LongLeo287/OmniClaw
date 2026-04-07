---
id: node
type: knowledge
owner: OA_Triage
---
# node
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: index.js
```js
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

### File: package.json
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

### File: README.md
```md
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

... [TRUNCATED]
```

### File: lib\store\index.js
```js
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

### File: releasenotes.md
```md
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

### File: lib\aggregateModel.js
```js
var debug = require('debug')('domain:aggregate'),
  dotty = require('dotty'),
  _ = require('lodash'),
  jsondate = require('jsondate');

/**
 * Aggregate constructor
 * @param {String} id              The aggregate id.
 * @param {Object} modelInitValues Initialization values for model like: { emails: [] } [optional]
 * @constructor
 */
function AggregateModel (id, modelInitValues) {
  if (!id || !_.isString(id)) {
    var err = new Error('No id injected!');
    debug(err);
    throw err;
  }

  this.id = id;

  if (modelInitValues instanceof AggregateModel) {
    this.attributes = modelInitValues.toJSON();
  } else {
    this.attributes = _.cloneDeep(modelInitValues || {});
  }

  this.attributes.id = this.id;
  this.attributes._destroyed = this.attributes._destroyed || false;
  this.attributes._revisions = this.attributes._revisions || {};
  this.attributes._revision = this.attributes._revision || 0;

  this.uncommittedEvents = [];
}

AggregateModel.prototype = {

  /**
   * Marks this aggregate as destroyed.
   */
  destroy: function () {
    this.set('_destroyed', true);
  },

  /**
   * Returns true if this aggregate is destroyed.
   * @returns {boolean}
   */
  isDestroyed: function () {
    return !!this.get('_destroyed');
  },

  /**
   * Sets the revision for this aggregate.
   * @param {Object} streamInfo The stream info.
   * @param {Number} rev        The revision number.
   */
  setRevision: function (streamInfo, rev) {
    this.set('_revision', rev);
    streamInfo.context = streamInfo.context || '_general';
    this.get('_revisions')[streamInfo.context + '_' + streamInfo.aggregate + '_' + streamInfo.aggregateId] = rev;
  },

  /**
   * Returns the revision of this aggregate.
   * @param {Object} streamInfo The stream info.
   * @returns {Number}
   */
  getRevision: function (streamInfo) {
    if (!streamInfo) {
      return this.get('_revision');
    }
    streamInfo.context = streamInfo.context || '_general';
    return this.get('_revisions')[streamInfo.context + '_' + streamInfo.aggregate + '_' + streamInfo.aggregateId] || 0;
  },

  /**
   * Returns all uncommitted events.
   * @returns {Array}
   */
  getUncommittedEvents: function () {
    return this.uncommittedEvents;
  },

  /**
   * Adds/Saves an uncommitted event.
   * @param {Object} evt The event object.
   */
  addUncommittedEvent: function (evt) {
    this.uncommittedEvents.push(evt);
  },

  /**
   * Clears the internal uncomitted event list.
   */
  clearUncommittedEvents: function () {
    this.uncommittedEvents = [];
  },

  /**
   * The toJSON function will be called when JSON.stringify().
   * @return {Object} A clean Javascript object containing all attributes.
   */
  toJSON: function () {
    return jsondate.parse(JSON.stringify(this.attributes));
    // return _.cloneDeep(this.attributes);
  },

  /**
   * Sets attributes for the aggregate.
   *
   * @example:
   *     aggregate.set('firstname', 'Jack');
   *     // or
   *     aggregate.set({
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
   *     aggregate.get('firstname'); // returns 'Jack'
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
   *     aggregate.has('firstname'); // returns true or false
   */
  has: function (attr) {
    return (this.get(attr) !== null && this.get(attr) !== undefined);
  },

  /**
   * Resets the attributes for the aggregate.
   */
  reset: function (data) {
    if (data instanceof AggregateModel) {
      this.attributes = data.toJSON();
    } else {
      this.attributes = _.cloneDeep(data || {});
    }

    this.attributes.id = this.id;
    this.attributes._destroyed = this.attributes._destroyed || false;
    this.attributes._revision = this.attributes._revision || 0;
  }

};

module.exports = AggregateModel;

```

### File: lib\commandDispatcher.js
```js
var debug = require('debug')('domain:commandDispatcher'),
  _ = require('lodash'),
  dotty = require('dotty'),
  DuplicateCommandError = require('./errors/duplicateCommandError');

/**
 * CommandDispatcher constructor
 * @param {Object} tree          The tree object.
 * @param {Object} definition    The definition object.
 * @param {Object} commandBunper The commandBumper object. [optional]
 * @constructor
 */
function CommandDispatcher (tree, definition, commandBumper) {
  if (!tree || !_.isObject(tree) || !_.isFunction(tree.getCommandHandler)) {
    var err = new Error('Please pass a valid tree!');
    debug(err);
    throw err;
  }

  if (!definition || !_.isObject(definition)) {
    var err = new Error('Please pass a valid command definition!');
    debug(err);
    throw err;
  }

  this.tree = tree;
  this.definition = definition;

  this.commandBumper = commandBumper;
}

CommandDispatcher.prototype = {

  /**
   * Returns the target information of this command.
   * @param {Object} cmd The passed command.
   * @returns {{name: 'commandName', aggregateId: 'aggregateId', version: 0, aggregate: 'aggregateName', context: 'contextName'}}
   */
  getTargetInformation: function (cmd) {
    if (!cmd || !_.isObject(cmd)) {
      var err = new Error('Please pass a valid command!');
      debug(err);
      throw err;
    }

    var aggregateId = null;
    if (dotty.exists(cmd, this.definition.aggregateId)) {
      aggregateId = dotty.get(cmd, this.definition.aggregateId);
    } else {
      debug('no aggregateId found, seems to be for a new aggregate');
    }

    var name = dotty.get(cmd, this.definition.name);

    var version = 0;
    if (dotty.exists(cmd, this.definition.version)) {
      version = dotty.get(cmd, this.definition.version);
    } else {
      debug('no version found, handling as version: 0');
    }

    var aggregate = null;
    if (dotty.exists(cmd, this.definition.aggregate)) {
      aggregate = dotty.get(cmd, this.definition.aggregate);
    } else {
      debug('no aggregate found, will lookup in all aggregates');
    }

    var context = null;
    if (dotty.exists(cmd, this.definition.context)) {
      context = dotty.get(cmd, this.definition.context);
    } else {
      debug('no aggregateName found, will lookup in all contexts');
    }

    return {
      name: name,
      aggregateId: aggregateId,
      version: version,
      aggregate: aggregate,
      context: context
    };
  },

  /**
   * Dispatches a command.
   * @param {Object}   cmd      The passed command.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err, evts){}`
   */
  dispatch: function (cmd, callback) {
    if (!cmd || !_.isObject(cmd)) {
      var err = new Error('Please pass a valid command!');
      debug(err);
      throw err;
    }

    if (!callback || !_.isFunction(callback)) {
      var err = new Error('Please pass a valid callback!');
      debug(err);
      throw err;
    }

    var target = this.getTargetInformation(cmd);

    var commandHandler = this.tree.getCommandHandler(target);

    // if (!commandHandler) {
    //   commandHandler = this.tree.getCommandHandlerByOldTarget(target);
    // }

    if (!commandHandler) {
      var err = new Error('No command handler found for ' + target.name);
      debug(err);
      return callback(err);
    }

    if (!this.commandBumper) {
      return commandHandler.handle(cmd, callback);
    }

    var key = target.context + target.aggregate + target.aggregateId + dotty.get(cmd, this.definition.id);

    this.commandBumper.add(key, function (err, added) {
      if (err) {
        return callback(err);
      }

      if (!added) {
        return callback(new DuplicateCommandError('Command already seen!'));
      }

      commandHandler.handle(cmd, callback);
    });
  }

};

module.exports = CommandDispatcher;

```

### File: lib\defaultCommandHandler.js
```js
var Definition = require('./definitionBase'),
  util = require('util'),
  _ = require('lodash'),
  debug = require('debug')('domain:defaultCommandHandler'),
  dotty = require('dotty'),
  async = require('async'),
  uuid = require('uuid').v4,
  ConcurrencyError = require('./errors/concurrencyError'),
  AggregateDestroyedError = require('./errors/aggregateDestroyedError'),
  AggregateConcurrencyError = require('./errors/aggregateConcurrencyError'),
  EventFromEventStore = require('eventstore/lib/event');

/**
 * Returns a random number between passed values of min and max.
 * @param {Number} min The minimum value of the resulting random number.
 * @param {Number} max The maximum value of the resulting random number.
 * @returns {Number}
 */
function randomBetween(min, max) {
  return Math.round(min + Math.random() * (max - min));
}

/**
 * DefaultCommandHandler constructor
 * @param {Object}   meta  Meta infos like: { name: 'name', version: 1 }
 * @constructor
 */
function DefaultCommandHandler (meta) {
  Definition.call(this, meta);

  this.id = uuid().toString();
  this.queue = {};
}

util.inherits(DefaultCommandHandler, Definition);

_.extend(DefaultCommandHandler.prototype, {

  /**
   * Injects the needed aggregate.
   * @param {Aggregate} aggregate The aggregate object to inject.
   */
  useAggregate: function (aggregate) {
    if (!aggregate || !_.isObject(aggregate)) {
      var err = new Error('Please pass a valid aggregate!');
      debug(err);
      throw err;
    }
    this.aggregate = aggregate;
  },

  /**
   * Injects the needed eventStore.
   * @param {Object} eventStore The eventStore object to inject.
   */
  useEventStore: function (eventStore) {
    if (!eventStore || !_.isObject(eventStore)) {
      var err = new Error('Please pass a valid eventStore!');
      debug(err);
      throw err;
    }
    this.eventStore = eventStore;
  },

  /**
   * Injects the needed aggregateLock.
   * @param {Object} aggregateLock The aggregateLock object to inject.
   */
  useAggregateLock: function (aggregateLock) {
    if (!aggregateLock || !_.isObject(aggregateLock)) {
      var err = new Error('Please pass a valid aggregateLock!');
      debug(err);
      throw err;
    }
    this.aggregateLock = aggregateLock;
  },

  /**
   * Queues the passed command and its callback.
   * @param {String}   aggId The passed aggregate id.
   * @param {Object}   cmd   The command to be queued.
   * @param {Function} clb   The callback of this command.
   */
  queueCommand: function (aggId, cmd, clb) {
    if (!aggId || !_.isString(aggId)) {
      var err = new Error('Please pass a valid aggregate id!');
      debug(err);
      throw err;
    }
    if (!cmd || !_.isObject(cmd)) {
      var err = new Error('Please pass a valid command!');
      debug(err);
      throw err;
    }
    if (!clb || !_.isFunction(clb)) {
      var err = new Error('Please pass a valid callback!');
      debug(err);
      throw err;
    }

    this.queue[aggId] = this.queue[aggId] || [];
    this.queue[aggId].push({ command: cmd, callback: clb })
  },

  /**
   * Returns next command in the queue
   * @param {String} aggId The passed aggregate id.
   * @returns {Object}
   */
  getNextCommandInQueue: function (aggId) {
    if (!aggId || !_.isString(aggId)) {
      var err = new Error('Please pass a valid aggregate id!');
      debug(err);
      throw err;
    }

    if (this.queue[aggId] && this.queue[aggId].length > 0) {
      var nextCmd = this.queue[aggId][0];
      return nextCmd;
    }

    return null;
  },

  /**
   * Removes the passed command from the queue.
   * @param {String} aggId The passed aggregate id.
   * @param {Object} cmd   The command to be queued.
   */
  removeCommandFromQueue: function (aggId, cmd) {
    if (!aggId || !_.isString(aggId)) {
      var err = new Error('Please pass a valid aggregate id!');
      debug(err);
      throw err;
    }

    _.remove(this.queue[aggId], function (c) {
      return c.command === cmd;
    });
  },

  /**
   * Locks the aggregate.
   * @param {String}   aggregateId The passed aggregateId.
   * @param {Function} callback    The function, that will be called when this action is completed.
   *                               `function(err){}`
   */
  lockAggregate: function (aggregateId, callback) {
    if (!aggregateId || !_.isString(aggregateId)) {
      var err = new Error('Please pass a valid aggregateId!');
      debug(err);
      throw err;
    }
    if (!callback || !_.isFunction(callback)) {
      var err = new Error('Please pass a valid callback!');
      debug(err);
      throw err;
    }
    this.aggregateLock.reserve(this.id, aggregateId, callback);
  },


  /**
   * Loads the aggregate.
   * @param {Object}   cmd         The command to be queued.
   * @param {String}   aggregateId The passed aggregateId (default).
   * @param {Function} callback    The function, that will be called when this action is completed.
   *                               `function(err, aggregate, stream, isNewSnapshotNeeded){}`
   */
  loadAggregate: function (cmd, aggregateId, callback) {
    if (!cmd || !_.isObject(cmd)) {
      var err = new Error('Please pass a valid command!');
      debug(err);
      throw err;
    }
    if (!aggregateId || !_.isString(aggregateId)) {
      var err = new Error('Please pass a valid aggregateId!');
      debug(err);
      throw err;
    }
    if (!callback || !_.isFunction(callback)) {
      var err = new Error('Please pass a valid callback!');
      debug(err);
      throw err;
    }

    var hasAggregateName = !!this.definitions.command.aggregate;
    var hasContextName = !!this.definitions.command.context;

    var toLoad = this.aggregate.getLoadInfo(cmd);

    var self = this;

    var firstToLoad = toLoad.shift();
    firstToLoad.aggregateId = firstToLoad.aggregateId || aggregateId;

    var aggregate = this.aggregate.create(aggregateId);

    var streams = [];

    var isNewSnapShotNeeded = false;

    if (this.aggregate.skipHistory) {
      debug('skip history for ', firstToLoad);
      if (this.aggregate.disablePersistence) {
        debug('persistency is disabled for ', firstToLoad);
        return callback(null, aggregate, streams);
      }
      var startLoadingOne = Date.now();
      // load aggregate with every stream
      this.eventStore.getLastEventAsStream(firstToLoad, function(err, stream) {
        if (err) {
          return callback(err);
        }

        var lastStreamRevInLoop = null;
        var events = _.map(stream.events, function (streamEvent) {
          if (lastStreamRevInLoop !== null && lastStreamRevInLoop + 1 !== streamEvent.streamRevision) {
            var msg = 'WARNING!!! Inconsistent event stream! Event with id (' + streamEvent.id + ') has a streamRevision of ' + streamEvent.streamRevision + ', but streamRevision in last event was ' + lastStreamRevInLoop + '!';
            var e = new Error(msg);
            debug(e);
            console.log(msg);
          }
          lastStreamRevInLoop = streamEvent.streamRevision;
          return streamEvent.payload;
        });

        var loadingTime = Date.now() - startLoadingOne;
        debug('needed ' + loadingTime + 'ms to load last event from the eventstore for: ', firstToLoad);

        streams.push(stream);

        async.map(events, function (evt, clb) {
          var evtName = dotty.get(evt, self.definitions.event.name);
          if (!evtName) {
            var err = new Error('event has no event name in ' + self.definitions.event.name);
            debug(err);
            throw err;
          }

          var version = 0;
          if (!!self.definitions.event.version) {
            version = dotty.get(evt, self.definitions.event.version);
          }

          var evtTransformer = self.aggregate.getLoadingEventTransformer(evtName, version) || { transform: function (e, cb) { cb(null, e); } };
          evtTransformer.transform(evt, clb);
        }, function (err, events) {
          if (err) return callback(err);

          self.aggregate.loadFromHistory(aggregate, null, events, loadingTime, stream, streams);

          // callback with the aggregate and the streams
          callback(null, aggregate, streams);
        });
      });
      return;
    }

    function regularLoad (callback) {
      if (!hasAggregateName) {
        delete firstToLoad.aggregate;
      }

      if (!hasContextName) {
        delete firstToLoad.context;
      }

      var startLoading = Date.now();

      // load aggregate with every stream
      self.eventStore.getFromSnapshot(firstToLoad, function(err, snapshot, stream) {
        if (err) {
          return callback(err);
        }

        var ignoreSnapshot = false;

        if (snapshot) ignoreSnapshot = self.aggregate.shouldIgnoreSnapshot(snapshot);

        if (!ignoreSnapshot) {
          var lastStreamRevInLoop = null;
          var events = _.map(stream.events, function (streamEvent) {
            if (lastStreamRevInLoop !== null && lastStreamRevInLoop + 1 !== streamEvent.streamRevision) {
              var msg = 'WARNING!!! Inconsistent event stream! Event with id (' + streamEvent.id + ') has a streamRevision of ' + streamEvent.streamRevision + ', but streamRevision in last event was ' + lastStreamRevInLoop + '!';
              var e = new Error(msg);
              debug(e);
              console.log(msg);
            }
            lastStreamRevInLoop = streamEvent.streamRevision;
            return streamEvent.payload;
          });

          var loadingTime = Date.now() - startLoading;
          var addon = '';
          if (snapshot) {
            addon = ' and snapshot';
          }
          debug('needed ' + loadingTime + 'ms to load events' + addon + ' from the eventstore for: ', firstToLoad);

          if (!snapshot) {
            isNewSnapShotNeeded = self.aggregate.loadFromHistory(aggregate, snapshot, [], loadingTime, stream);

            streams.push(stream);

            callback(null, events, stream, startLoading);
            return;
          }

          var transformer = self.aggregate.loadingSnapshotTransformers[self.aggregate.context.name + '.' + self.aggregate.name + '.' + self.aggregate.version] || function (sn, cb) { cb(null, sn); };
          transformer(snapshot.data, function (err, snapData) {
            if (err) return callback(err);

            snapshot.data = snapData;

            isNewSnapShotNeeded = self.aggregate.loadFromHistory(aggregate, snapshot, [], loadingTime, stream);

            streams.push(stream);

            callback(null, events, stream, startLoading);
          });
          return;
        }

        debug('skipping snapshot, and load whole event stream');

        startLoading = Date.now();
        self.eventStore.getEventStream(firstToLoad, function(err, stream) {
          if (err) {
            return callback(err);
          }

          var lastStreamRevInLoop = null;
          var events = _.map(stream.events, function (streamEvent) {
            if (lastStreamRevInLoop !== null && lastStreamRevInLoop + 1 !== streamEvent.streamRevision) {
              var msg = 'WARNING!!! Inconsistent event stream! Event with id (' + streamEvent.id + ') has a streamRevision of ' + streamEvent.streamRevision + ', but streamRevision in last event was ' + lastStreamRevInLoop + '!';
              var e = new Error(msg);
              debug(e);
              console.log(msg);
            }
            lastStreamRevInLoop = streamEvent.streamRevision;
            return streamEvent.payload;
          });

          loadingTime = Date.now() - startLoading;

          debug('needed ' + loadingTime + 'ms to load events from the eventstore');

          async.map(events, function (evt, clb) {
            var evtName = dotty.get(evt, self.definitions.event.name);
            if (!evtName) {
              var err = new Error('event has no event name in ' + self.definitions.event.name);
              debug(err);
              throw err;
            }

            var version = 0;
            if (!!self.definitions.event.version) {
              version = dotty.get(evt, self.definitions.event.version);
            }

            var evtTransformer = self.aggregate.getLoadingEventTransformer(evtName, version) || { transform: function (e, cb) { cb(null, e); } };
            evtTransformer.transform(evt, clb);
          }, function (err, events) {
            if (err) return callback(err);

            isNewSnapShotNeeded = self.aggregate.loadFromHistory(aggregate, null, events, loadingTime, stream);

            streams.push(stream);

            callback(null, events, stream, startLoading);
          });
        });
      });
    }

    regularLoad(function (err, events, stream, totalLoadingTime) {
      if (err) {
        return callback(err);
      }

      async.eachSeries(toLoad, function (loadInfo, callback) {
        loadInfo.aggregateId = loadInfo.aggregateId || aggregateId;

        if (!hasAggregateName) {
          delete loadInfo.aggregate;
        }

        if (!hasContextName) {
          delete loadInfo.context;
        }

        var rev = aggregate.getRevision(loadInfo);

        var startLoading = Date.now();

        // load aggregate with every stream
        self.eventStore.getEventStream(loadInfo, rev, function(err, str) {
          if (err) {
            return callback(err);
          }

          var lastStreamRevInLoop = null;
          var evts = _.map(str.events, function (streamEvent) {
            if (lastStreamRevInLoop !== null && lastStreamRevInLoop + 1 !== streamEvent.streamRevision) {
              var msg = 'WARNING!!! Inconsistent event stream! Event with id (' + streamEvent.id + ') has a streamRevision of ' + streamEvent.streamRevision + ', but streamRevision in last event was ' + lastStreamRevInLoop + '!';
              var e = new Error(msg);
              debug(e);
              console.log(msg);
            }
            lastStreamRevInLoop = streamEvent.streamRevision;
            return streamEvent.payload;
          });

          var loadingTime = Date.now() - startLoading;
          debug('needed ' + loadingTime + 'ms to load events from the eventstore for: ', loadInfo);

          var notSameOrigin = loadInfo.aggregate && loadInfo.aggregate !== self.aggregate.name ||
                              loadInfo.context && loadInfo.context !== self.aggregate.context.name;

          async.map(evts, function (evt, clb) {
            var evtName = dotty.get(evt, self.definitions.event.name);
            if (!evtName) {
              var err = new Error('event has no event name in ' + self.definitions.event.name);
              debug(err);
              throw err;
            }

            var version = 0;
            if (!!self.definitions.event.version) {
              version = dotty.get(evt, self.definitions.event.version);
            }

            var evtTransformer = self.aggregate.getLoadingEventTransformer(evtName, version) || { transform: function (e, cb
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

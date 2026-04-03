---
id: github.com-thenativeweb-node-cqrs-domain-de6c8aa0-
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:27.477557
---

# KNOWLEDGE EXTRACT: github.com_thenativeweb_node-cqrs-domain_de6c8aa0
> **Extracted on:** 2026-04-01 15:42:26
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524704/github.com_thenativeweb_node-cqrs-domain_de6c8aa0

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

.idea

.DS_Store

*.tingo
*.db

dump.rdb

npm-debug.log
package-lock.json
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

before_install:
  - wget http://dynamodb-local.s3-website-us-west-2.amazonaws.com/dynamodb_local_latest.tar.gz -O /tmp/dynamodb_local_latest.tar.gz
  - tar -xzf /tmp/dynamodb_local_latest.tar.gz -C /tmp
  - java -Djava.library.path=/tmp/DynamoDBLocal_lib -jar /tmp/DynamoDBLocal.jar -inMemory &
  - sleep 2
  
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

env:
  global:
    - AWS_ACCESS_KEY_ID=AKID
    - AWS_SECRET_ACCESS_KEY=SECRET
    - AWS_REGION=us-east-1
    - AWS_DYNAMODB_ENDPOINT=http://localhost:8000
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

[![travis](https://img.shields.io/travis/adrai/node-cqrs-domain.svg)](https://travis-ci.org/adrai/node-cqrs-domain) [![npm](https://img.shields.io/npm/v/cqrs-domain.svg)](https://npmjs.org/package/cqrs-domain)

Node-cqrs-domain is a node.js module based on [node-eventstore](http://adrai.github.com/node-eventstore/).
It can be very useful as domain component if you work with (d)ddd, cqrs, eventdenormalizer, host, etc.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Workflow](#workflow)
- [Installation](#installation)
- [Usage](#usage)
  - [Using factory methods for event store or / and aggregate lock in domain definition](#using-factory-methods-for-event-store-or--and-aggregate-lock-in-domain-definition)
  - [Exposed errors](#exposed-errors)
  - [Catch connect ad disconnect events](#catch-connect-ad-disconnect-events)
  - [Define the command structure](#define-the-command-structure)
  - [Define the event structure](#define-the-event-structure)
  - [Define the id generator function [optional]](#define-the-id-generator-function-optional)
    - [you can define a synchronous function](#you-can-define-a-synchronous-function)
    - [or you can define an asynchronous function](#or-you-can-define-an-asynchronous-function)
  - [Define the aggregate id generator function [optional]](#define-the-aggregate-id-generator-function-optional)
    - [you can define a synchronous function](#you-can-define-a-synchronous-function-1)
    - [or you can define an asynchronous function](#or-you-can-define-an-asynchronous-function-1)
  - [Wire up events [optional]](#wire-up-events-optional)
    - [you can define a synchronous function](#you-can-define-a-synchronous-function-2)
    - [or you can define an asynchronous function](#or-you-can-define-an-asynchronous-function-2)
  - [Initialization](#initialization)
  - [Handling a command](#handling-a-command)
    - [or](#or)
    - [more infos, can be useful if testing](#more-infos-can-be-useful-if-testing)
  - [Request domain information](#request-domain-information)
- [Components definition](#components-definition)
  - [Context](#context)
  - [Aggregate](#aggregate)
  - [Command validation](#command-validation)
  - [Pre-Load-Condition](#pre-load-condition)
  - [Pre-Condition](#pre-condition)
  - [Command](#command)
  - [Event](#event)
  - [Business Rule](#business-rule)
  - [Command Handler (Be careful!!!)](#command-handler-be-careful)
- [License](#license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
# Workflow

```

        │
       cmd
        │
        ∨
  ╔════════════╗
  ║ validation ║─────────> "rejected"
  ╚════════════╝
        │
       cmd
        │
        ∨
╔═════════════════════╗
║ pre-load-conditions ║─────> "rejected"
╚═════════════════════╝
        │
       cmd
        │
        ∨
╔════════════════╗
║ pre-conditions ║─────> "rejected"
╚════════════════╝
        │
       cmd
        │
        ∨
  ╔════════════╗
  ║ handle cmd ║
  ╚════════════╝
        │
       evt
        │
        ∨
  ╔═══════════╗
  ║ apply evt ║
  ╚═══════════╝
        │
        │
        │
        ∨
╔════════════════╗
║ business rules ║─────> "rejected"
╚════════════════╝
        │
        │
        │
        ∨
   ╔════════╗
   ║ commit ║
   ╚════════╝

```

# Installation

    npm install cqrs-domain

# Usage

	var domain = require('cqrs-domain')({
	  // the path to the "working directory"
	  // can be structured like
	  // [set 1](https://github.com/adrai/node-cqrs-domain/tree/master/test/integration/fixture/set1) or
	  // [set 2](https://github.com/adrai/node-cqrs-domain/tree/master/test/integration/fixture/set2)
	  domainPath: '/path/to/my/files',

	  // optional, default is 'commandRejected'
	  // will be used if an error occurs and an event should be generated
	  commandRejectedEventName: 'rejectedCommand',

	  // optional, default is 800
	  // if using in scaled systems and not guaranteeing that each command for an aggregate instance
	  // dispatches to the same worker process, this module tries to catch the concurrency issues and
	  // retries to handle the command after a timeout between 0 and the defined value
	  retryOnConcurrencyTimeout: 1000,

	  // optional, default is 100
	  // global snapshot threshold value for all aggregates
	  // defines the amount of loaded events, if there are more events to load, it will do a snapshot, so next loading is faster
	  // an individual snapshot threshold defining algorithm can be defined per aggregate (scroll down)
	  snapshotThreshold: 1000,

	  // optional, default is in-memory
	  // currently supports: mongodb, redis, tingodb, azuretable and inmemory
	  // hint: [eventstore](https://github.com/adrai/node-eventstore#provide-implementation-for-storage)
	  eventStore: {
	    type: 'mongodb',
	    host: 'localhost',                          // optional
	    port: 27017,                                // optional
	    dbName: 'domain',                           // optional
	    eventsCollectionName: 'events',             // optional
	    snapshotsCollectionName: 'snapshots',       // optional
	    transactionsCollectionName: 'transactions', // optional
	    timeout: 10000                              // optional
      // authSource: 'authedicationDatabase',        // optional
	    // username: 'technicalDbUser',                // optional
	    // password: 'secret'                          // optional
      // url: 'mongodb://user:pass@host:port/db?opts // optional
	  },

	  // optional, default is in-memory
	  // currently supports: mongodb, redis, tingodb, couchdb, azuretable, dynamodb and inmemory
	  // hint settings like: [eventstore](https://github.com/adrai/node-eventstore#provide-implementation-for-storage)
	  aggregateLock: {
	    type: 'redis',
	    host: 'localhost',                          // optional
	    port: 6379,                                 // optional
	    db: 0,                                      // optional
	    prefix: 'domain_aggregate_lock',            // optional
	    timeout: 10000                              // optional
	    // password: 'secret'                          // optional
	  },

	  // optional, default is not set
	  // checks if command was already seen in the last time -> ttl
	  // currently supports: mongodb, redis, tingodb and inmemory
	  // hint settings like: [eventstore](https://github.com/adrai/node-eventstore#provide-implementation-for-storage)
	  deduplication: {
			type: 'redis',
			ttl: 1000 * 60 * 60 * 1, // 1 hour          // optional
			host: 'localhost',                          // optional
			port: 6379,                                 // optional
			db: 0,                                      // optional
			prefix: 'domain_aggregate_lock',            // optional
			timeout: 10000                              // optional
			// password: 'secret'                          // optional
	  },

	  // optional, default false
	  // resolves valid file types from loader extensions instead of default values while parsing definition files
	  useLoaderExtensions: true
	});

## Using factory methods for event store or / and aggregate lock in domain definition
You can replace the framework-provided implementation of event store or / and aggregate lock with the one of your own.
To do that, you need to include a factory method in the options object passed to the domain constructor.
Using the factory methods, the example above might become:


	var myGetEventStore = require('./getEventStore.js');
	var myLock = require('./myLock.js');

	var domain = require('cqrs-domain')({
	  domainPath: '/path/to/my/files',
	  commandRejectedEventName: 'rejectedCommand',
	  retryOnConcurrencyTimeout: 1000,
	  snapshotThreshold: 1000,

	  eventStore: function () {
	    return myGetEventStore({
	      host: '127.0.0.1',
	      port: 2113,
	      username: 'admin',
	      password: 'changeit'
	    });
	  },

	  aggregateLock: : function () {
	    return myLock({
	       // ....
	    });
	  },

	  deduplication: : function () {
			return myCommandBumper({
			   // ....
			});
	  }
	});

When using factory methods, the objects they return are required to implement the following public interfaces:

	Event Store:

	  f:  init(function(err));
	  f:  getNewId(function (err, id));
	  f:  on(evtName, function (err));
	  f:  getFromSnapshot(query, revMax, function(err, snapshot, stream));
	  f:  createSnapshot(obj, function (err));
	  f:  setEventToDispatched(evt, function (err));

	Event Stream (returned by getFromSnapshot through the callback):

	  p:  events
	  p:  lastRevision
	  p:  eventsToDispatch
	  f:  addEvents(evts)
	  f:  commit(function (err, stream));

	Aggregate Lock:

	  f: connect(function(err, lock))
	  f: disconnect(function(err))
	  f: getNewId(function(err, id))
	  f: reserve(workerId, aggregateId, function(err))
	  f: getAll(aggregateId, function(err, workerIds))
	  f: resolve(aggregateId, function(err))

	Command Bumper:

	  f: connect(function(err, lock))
	  f: disconnect(function(err))
	  f: getNewId(function(err, id))
	  f: add(key, ttl, function(err, added))

	where:

	  f: function
	  p: property


## Using custom structure loader function
You can also replace the built-in structure loader with one that suits your needs.
To do that, you need to include a loading method in the options object passed to the domain constructor.

	// options will contain a the domainPath, validatorExtension, and useLoaderExtensions options passed to the constructor
	// as well as a definition object containing all the constructors of the domain components  ( Context, Aggregate etc. ) and error constructors ( inside errors )
	function myCustomLoader(options) {
		return {
			myContext:  new Context({ name: 'myContext' }).addAggregate(new Aggregate({ name : 'agg' }, function(){}).addCommand({ name: 'cmd' }, function(){}))
		}
		// or, more probably 
		return myExternalCoolLoader(options.domainPath, options.definitions);
	}
	// or async
	function myCustomLoaderAsync(options, callback) {
		callback(null, myExternalCoolLoader(options.domainPath, options.definitions));
	}

	var domain = require('cqrs-domain')({
	  domainPath: '/path/to/my/files',
		structureLoader: myCustomLoader
	});

## Exposed errors
You can use this for example in you custom command handlers.

	require('cqrs-domain').errors.ValidationError
	require('cqrs-domain').errors.BusinessRuleError
	require('cqrs-domain').errors.AggregateDestroyedError
	require('cqrs-domain').errors.AggregateConcurrencyError
	require('cqrs-domain').errors.ConcurrencyError
	require('cqrs-domain').errors.DuplicateCommandError


## Catch connect and disconnect events

	// eventStore
	domain.eventStore.on('connect', function() {
	  console.log('eventStore connected');
	});

	domain.eventStore.on('disconnect', function() {
	  console.log('eventStore disconnected');
	});

	// aggregateLock
	domain.aggregateLock.on('connect', function() {
	  console.log('aggregateLock connected');
	});

	domain.aggregateLock.on('disconnect', function() {
	  console.log('aggregateLock disconnected');
	});

	// commandBumper
	domain.commandBumper.on('connect', function() {
	  console.log('commandBumper connected');
	});

	domain.commandBumper.on('disconnect', function() {
	  console.log('commandBumper disconnected');
	});


	// anything (eventStore or aggregateLock or commandBumper)
	domain.on('connect', function() {
	  console.log('something connected');
	});

	domain.on('disconnect', function() {
	  console.log('something disconnected');
	});


## Define the command structure
The values describes the path to that property in the command message.

	domain.defineCommand({
	  // optional, default is 'id'
	  id: 'id',

	  // optional, default is 'name'
	  name: 'name',

	  // optional, default is 'aggregate.id'
	  // if an aggregate id is not defined in the command, the command handler will create a new aggregate instance
	  aggregateId: 'aggregate.id',

	  // optional, only makes sense if contexts are defined in the 'domainPath' structure
	  context: 'context.name',

	  // optional, only makes sense if aggregates with names are defined in the 'domainPath' structure
	  aggregate: 'aggregate.name',

	  // optional, but recommended
	  payload: 'payload',

	  // optional, if defined the command handler will check if the command can be handled
	  // if you want the command to be handled in a secure/transactional way pass a revision value that matches the current aggregate revision
	  revision: 'revision',

	  // optional, if defined the command handler will search for a handle that matches command name and version number
	  version: 'version',

	  // optional, if defined theses values will be copied to the event (can be used to transport information like userId, etc..)
	  meta: 'meta'
	});


## Define the event structure
The values describes the path to that property in the event message.

	domain.defineEvent({
	  // optional, default is 'correlationId'
	  // will use the command id as correlationId, so you can match it in the sender
	  correlationId: 'correlationId',

	  // optional, default is 'id'
	  id: 'id',

	  // optional, default is 'name'
	  name: 'name',

	  // optional, default is 'aggregate.id'
	  aggregateId: 'aggregate.id',

	  // optional, only makes sense if contexts are defined in the 'domainPath' structure
	  context: 'context.name',

	  // optional, only makes sense if aggregates with names are defined in the 'domainPath' structure
	  aggregate: 'aggregate.name',

	  // optional, default is 'payload'
	  payload: 'payload',

	  // optional, default is 'revision'
	  // will represent the aggregate revision, can be used in next command
	  revision: 'revision',

	  // optional
	  version: 'version',

	  // optional, if defined the values of the command will be copied to the event (can be used to transport information like userId, etc..)
	  meta: 'meta',

	  // optional, if defined the commit date of the eventstore will be saved in this value
	  commitStamp: 'commitStamp',

	  // optional, if defined and the eventstore db implemntation supports this the position of the event in the eventstore will be saved in this value
	  position: 'position'
	});


## Define the id generator function [optional]
### you can define a synchronous function

	domain.idGenerator(function () {
	  var id = require('uuid').v4().toString();
	  return id;
	});

### or you can define an asynchronous function

	domain.idGenerator(function (callback) {
	  setTimeout(function () {
	    var id = require('uuid').v4().toString();
	    callback(null, id);
	  }, 50);
	});


## Define the aggregate id generator function [optional]
### you can define a synchronous function

	domain.aggregateIdGenerator(function () {
	  var id = require('uuid').v4().toString();
	  return id;
	});

### or you can define an asynchronous function

	domain.aggregateIdGenerator(function (callback) {
	  setTimeout(function () {
	    var id = require('uuid').v4().toString();
	    callback(null, id);
	  }, 50);
	});


## Wire up events [optional]
### you can define a synchronous function

	// pass events to bus
	domain.onEvent(function (evt) {
	  bus.emit('event', evt);
	});

### or you can define an asynchronous function

	// pass events to bus
	domain.onEvent(function (evt, callback) {
	  bus.emit('event', evt, function ack () {
	    callback();
	  });
	});


## Initialization

	domain.init(function (err, warnings) {
	  // this callback is called when all is ready...
	  // warnings: if no warnings warnings is null, else it's an array containing errors during require of files
	});

	// or

	domain.init(); // callback is optional


## Handling a command

	domain.handle({
	  id: 'b80ade36-dd05-4340-8a8b-846eea6e286f',
	  name: 'enterNewPerson',
	  aggregate: {
	    id: '3b4d44b0-34fb-4ceb-b212-68fe7a7c2f70',
	    name: 'person'
	  },
	  context: {
	    name: 'hr'
	  },
	  payload: {
	    firstname: 'Jack',
	    lastname: 'Huston'
	  },
	  revision: 0,
	  version: 1,
	  meta: {
	    userId: 'ccd65819-4da4-4df9-9f24-5b10bf89ef89'
	  }
	}); // callback is optional

### or

	domain.handle({
	  id: 'b80ade36-dd05-4340-8a8b-846eea6e286f',
	  name: 'renamePerson',
	  aggregate: {
	    id: '3b4d44b0-34fb-4ceb-b212-68fe7a7c2f70',
	    name: 'person'
	  },
	  context: {
	    name: 'hr'
	  },
	  payload: {
	    firstname: 'Jack',
	    lastname: 'Huston'
	  },
	  revision: 0,
	  version: 1,
	  meta: {
	    userId: 'ccd65819-4da4-4df9-9f24-5b10bf89ef89'
	  }
	}, function (err) {
	  // this callback is called when command is handled successfully or unsuccessfully
	  // err can be of type:
	  // - null
	  // - Error
	  //   {
	  //     name: 'Error',
	  //     message: 'optional message'
	  //   }
	  // - ValidationError
	  //   {
	  //     name: 'ValidationError',
	  //     message: 'some message',
	  //     more: { /* more infos */ }
	  //   }
	  // - BusinessRuleError
	  //   {
	  //     name: 'BusinessRuleError',
	  //     message: 'some message',
	  //     more: { /* more infos */ }
	  //   }
	  // - AggregateDestroyedError
	  //   {
	  //     name: 'AggregateDestroyedError',
	  //     message: 'Aggregate has already been destroyed!',
	  //     more: {
	  //       aggregateId: 'ad10d2c0-6509-4cb0-86d2-76312d930001',
	  //       aggregateRevision: 6
	  //     }
	  //   }
	  // - AggregateConcurrencyError
	  //   {
	  //     name: 'AggregateConcurrencyError',
	  //     message: 'Actual revision in command is "3", but expected is "2"!',
	  //     more: {
	  //       aggregateId: 'ad10d2c0-6509-4cb0-86d2-76312d930001',
	  //       aggregateRevision: 2,
	  //       commandRevision: 3
	  //     }
	  //   }
	});

### more infos, can be useful if testing

	domain.handle({
	  id: 'b80ade36-dd05-4340-8a8b-846eea6e286f',
	  name: 'renamePerson',
	  aggregate: {
	    id: '3b4d44b0-34fb-4ceb-b212-68fe7a7c2f70',
	    name: 'person'
	  },
	  context: {
	    name: 'hr'
	  },
	  payload: {
	    firstname: 'Jack',
	    lastname: 'Huston'
	  },
	  revision: 0,
	  version: 1,
	  meta: {
	    userId: 'ccd65819-4da4-4df9-9f24-5b10bf89ef89'
	  }
	}, function (err, events, aggregateData, metaInfos) {
	  // this callback is called when command is handled successfully or unsuccessfully
	  // err: is the same as described before

	  // events: same as passed in 'onEvent' function
	  // events: in case of no error here is the array of all events that should be published
	  // events: in case of error are the one of these Errors (ValidationError, BusinessRuleError, AggregateDestroyedError, AggregateConcurrencyError)
	  // converted in an event with the event name defined in the options (default is 'commandRejected')

	  // aggregateData: represents the aggregateData after applying the resulting events

	  // metaInfos: { aggregateId: '3b4d44b0-34fb-4ceb-b212-68fe7a7c2f70', aggregate: 'person', context: 'context' }
	});


## Request domain information

After the initialization you can request the domain information:

	domain.init(function (err) {
	  domain.getInfo();
	  // ==>
	  // { contexts: [
	  //   {
	  //      "name": "hr",
	  //      "aggregates": [
	  //        {
	  //          "name": "person",
	  //          "version": 3,
	  //          "commands": [
	  //            {
	  //              "name": "enterNewPerson",
	  //              "version": 0,
	  //							"preconditions": [...]
	  //            },
	  //            {
	  //              "name": "unregisterAllContactInformation",
	  //              "version": 2,
	  //							"preconditions": [...]
	  //            },
	  //            {
	  //              "name": "unregisterAllContactInformation",
	  //              "version": 1,
	  //							"preconditions": [...]
	  //            }
	  //          ],
	  //          "events": [
	  //            {
	  //              "name": "enteredNewPerson",
	  //              "version": 3
	  //            },
	  //            {
	  //              "name": "enteredNewPerson",
	  //              "version": 0
	  //            },
	  //            {
	  //              "name": "enteredNewPerson",
	  //              "version": 2
	  //            },
	  //            {
	  //              "name": "unregisteredEMailAddress",
	  //              "version": 0
	  //            },
	  //            {
	  //              "name": "unregisteredPhoneNumber",
	  //              "version": 0
	  //            }
	  //          ],
	  //          "businessRules": [
	  //            {
	  //              "name": "atLeast1EMail",
	  //              "description": "at least one character should be in email address"
	  //            },
	  //            {
	  //              "name": "nameEquality",
	  //              "description": "firstname should never be equal lastname"
	  //            }
	  //          ]
	  //        }
	  //      ]
	  //   }
	  //]}
	});


# Components definition

## Context

	module.exports = require('cqrs-domain').defineContext({
	  // optional, default is the directory name
	  name: 'hr'
	});

### Externally loaded context ( self-loaded ) 

	A special option to define a context with all its aggregates, commands, events and rules exists by adding the externallyLoaded option to the context :

	module.exports = require('cqrs-domain').defineContext({
	  // optional, default is the directory name
	  name: 'hr',
	  externallyLoaded: true
	});

	When doing so the context will be added 'as-is' to the domain, this means it won't go trough the normal tree loading and parsing process.
	This option is aimed mainly at plugin developers, as it leaves the responsibility of structuring the domain right in the hand of the one defining the context ( most-probably a plug-in ).

## Aggregate

	module.exports = require('cqrs-domain').defineAggregate({
	  // optional, default is last part of path name
	  name: 'person',

	  // optional, default 0
	  version: 3,

	  // optional, default ''
	  defaultCommandPayload: 'payload',

	  // optional, default ''
	  defaultEventPayload: 'payload',

	  // optional, default ''
	  defaultPreConditionPayload: 'payload',

	  // optional, default false
	  // by skipping the history, only the last event will be loaded and defaultly not applyed (just to ensure the revision number increment)
	  skipHistory: true,

	  // optional, default false
	  // only optionally needed when skipHistory is set to true, only the last event will be loaded and applyed
	  applyLastEvent: true,

	  // optional, default false
	  // will publish the events but will not commit them to the eventstore
	  disablePersistence: false
	},

	// optionally, define some initialization data...
	{
	  emails: ['default@mycomp.org'],
	  phoneNumbers: []
	})

	// optionally, define snapshot need algorithm...
	.defineSnapshotNeed(function (loadingTime, events, aggregateData) {
	  // loadingTime is the loading time in ms of the eventstore data
	  // events are all loaded events in an array
	  // aggregateData represents the aggregateData after applying the resulting events
	  return events.length >= 200;
	})

	// optionally, define if snapshot should be ignored
	// if true, the whole event stream will be loaded
	.defineIgnoreSnapshot({
	  version: 0
	}, function (data) {
	  return true;
	})
	//.defineIgnoreSnapshot({
	//  version: 0
	//}, true)
	//.defineIgnoreSnapshot({
	//  version: 0
	//}) // default true

	// optionally, define conversion algorithm for older snapshots
	// always convert directly to newest version...
	// when loaded a snapshot and it's an older snapshot, a new snapshot with same revision but with newer aggregate version will be created
	.defineSnapshotConversion({
	  version: 1
	}, function (data, aggregate) {
	  // data is the snapshot data
	  // aggregate is the aggregate object

	  aggregate.set('emails', data.emails);
	  aggregate.set('phoneNumbers', data.phoneNumbers);

	  var names = data.name.split(' ');
	  aggregate.set('firstname', names[0]);
	  aggregate.set('lastname', names[1]);
	})
    // optionally, define committingSnapshotTransformer (i.e. for GDPR: to encrypt data in storage)
  	.defineCommittingSnapshotTransformer({
	  version: 1
	}, function (data) {
	  // data is the snapshot data
	  data.firstname = encrypt(data.firstname);
    return data;
	})
    // or async
	.defineCommittingSnapshotTransformer({
	  version: 1
	}, function (data, callback) {
	  // data is the snapshot data
	  encrypt(data.firstname, function (err, encrypted) {
      data.firstname = encrypted;
      callback(err, data);
    });
	})
    // optionally, define loadingSnapshotTransformer (i.e. for GDPR: to decrypt stored data)
	.defineLoadingSnapshotTransformer({
	  version: 1
	}, function (data) {
	  // data is the snapshot data
	  data.firstname = decrypt(data.firstname);
    return data;
	})
    // or async
	.defineLoadingSnapshotTransformer({
	  version: 1
	}, function (data, callback) {
	  // data is the snapshot data
	  decrypt(data.firstname, function (err, decrypted) {
      data.firstname = decrypted;
      callback(err, data);
    });
	})
	// optionally, define idGenerator function for new aggregate ids
	// sync
	.defineAggregateIdGenerator(function () {
	  return require('uuid').v4().toString();
	});
	// or async
	.defineAggregateIdGenerator(function (callback) {
	  setTimeout(function () {
	    var id = require('uuid').v4().toString();
	    callback(null, id);
	  }, 50);
	})
    // optionally, define idGenerator function for new aggregate ids that are command aware
    // if you define it that way, the normal defineAggregateIdGenerator function will be replaced
    // sync
  	.defineCommandAwareAggregateIdGenerator(function (cmd) {
  	  return cmd.id + require('uuid').v4().toString();
  	});
  	// or async
  	.defineCommandAwareAggregateIdGenerator(function (cmd, callback) {
  	  setTimeout(function () {
  	    var id = cmd.id + require('uuid').v4().toString();
  	    callback(null, id);
  	  }, 50);
  	});


## Command validation
All command schemas are json schemas. Hint [http://jsonary.com/documentation/json-schema/](http://jsonary.com/documentation/json-schema/)

Internally the [tv4](http://geraintluff.github.io/tv4/) module is used for validation. Additionaly you can extend the tv4 instance with other functionality like [tv4-formats](https://github.com/ikr/tv4-formats), so you can easily use format constraints (i.e. 'email') for your 'string'-types.
To extend tv4 just catch the validator before having initialized the domain:


    domain.extendValidator(function (validator) {

      // own formats
      validator.addFormat(require('tv4-formats'));
      validator.addFormat('mySpecialFormat', function (data) {
        if (data === 'special') {
          return null;
        }
        return 'wrong format for special';
      });

      // or other schemas
      validator.addSchema({ 'mySharedSchema': { /* the schema json */ } });
      validator.addSchema('myOtherSharedSchema', { /* the schema json */ });

      // or replace the core valitator
      validator.validator(function (options, schema) {
        // options.schemas => all schemas
        // options.formats => all formats

        // sync        
        return function (cmdDataToValidate) {
          if (everythingIsOk) {
            return null;
          } else {
            return new require('cqrs-domain').errors.ValidationError('command not valid', { 'because': 'of this' });
          }
        };
        // or async
        return function (cmdDataToValidate, callback) {
          externalAsyncValidator(cmdDataToValidate, function(errors){
            if (!error) {
                callback();
            } else {
                callback(new require('cqrs-domain').errors.ValidationError('command not valid', { 'because': 'of this' }));
            }
          });
        };

      });

    });


Each command schema title should match the command name. Example: [enterNewPerson.json](https://github.com/adrai/node-cqrs-domain/blob/1.0/test/integration/fixture/set1/hr/person/validationRules/enterNewPerson.json)

To support multiple versions look at: [unregisterAllContactInformation.json](https://github.com/adrai/node-cqrs-domain/blob/v2.1.5/test/integration/fixture/set1/hr/person/validationRules/unregisterAllContactInformation.json#L10)

or: [unregisterAllContactInformation_v1.json](https://github.com/adrai/node-cqrs-domain/blob/v2.2.0/test/integration/fixture/set1/hr/person/validationRules/unregisterAllContactInformation_v1.json#L3)
[unregisterAllContactInformation_v2.json](https://github.com/adrai/node-cqrs-domain/blob/v2.2.0/test/integration/fixture/set1/hr/person/validationRules/unregisterAllContactInformation_v2.json#L3)


You can also have an hierarchical command extension look at:

- [command](https://github.com/adrai/node-cqrs-domain/blob/1.0/test/integration/fixture/set1/hr/person/validationRules/enterNewPerson.json)
- [aggregate](https://github.com/adrai/node-cqrs-domain/blob/1.0/test/integration/fixture/set1/hr/person/command.json)
- [context](https://github.com/adrai/node-cqrs-domain/blob/1.0/test/integration/fixture/set1/hr/command.json)
- [general](https://github.com/adrai/node-cqrs-domain/blob/1.0/test/integration/fixture/set1/command.json)

## Pre-Load-Condition
Can be used to perform some business rules before handling the command. Contrary to Pre-Conditions, these rules are applied BEFORE the aggregate is loaded.

This allows you to (for example) run checks against external information by using closures.

> **Tip:** Pre-load conditions are especially useful when you have checks that you want to run on an aggregate, but when it is OK for those checks to run on potentially stale data (eg a view model). By doing these checks before the aggregate is locked, you avoid creating a locking bottleneck at the aggregate level, and can keep your aggregate smaller because the information for those checks is externalized to the domain. This helps for performance if the domain you are in is performance critical, and helps you keep focus on the real, strongly consistent invariants in your domain.

A Command can have multiple pre-load-conditions.

    var externalDataLoader = require('some_file');

	module.exports = require('cqrs-domain').definePreLoadCondition({
	  // the command name
	  // optional, default is file name without extension,
	  // if name is '' it will handle all commands that matches the appropriate aggregate
	  // if name is an array of strings it will handle all commands that matches the appropriate name
	  name: 'checkSomeViewModel',

	  // optional, default 0
	  version: 2,

	  // optional, if not defined it will use what is defined as default in aggregate or pass the whole command
	  payload: 'payload',

	  // optional
	  description: 'firstname should always be set',

	  // optional, default Infinity, all pre-conditions will be sorted by this value
	  priority: 1
	}, function (data, callback) {
	  // data is the command data
	  // callback is optional, if not defined as function argument you can throw errors or return errors here (sync way)

      if (externalDataLoader.get(data.id) !== data.value) {
        return callback('not allowed');
        // or
        // return callback(new Error('not allowed'));
        // or
        // return callback(new Error()); // if no error message is defined then the description will be taken
        // or
        // return callback(new require('cqrs-domain').BusinessRuleError('not allowed', { /* more infos */ }));
      }

	  callback(null);

	  // or if callback is not defined as function argument
	  // if (externalDataLoader.get(data.id) !== data.value)
    //   return 'not allowed';
    //   // or
    //   // return new Error('not allowed');
    //   // or
    //   // return new Error(); // if no error message is defined then the description will be taken
    //   // or
    //   // throw new Error(); // if no error message is defined then the description will be taken
    //   // or
    //   // throw new Error('not allowed');
    //   // or
    //   // throw new require('cqrs-domain').BusinessRuleError('not allowed', { /* more infos */ });
    // }
	});


## Pre-Condition
Can be used to perform some business rules before handling the command. The aggregate is locked and loaded before the pre-condition is applied.

A Command can have multiple pre-conditions.

	module.exports = require('cqrs-domain').definePreCondition({
	  // the command name
	  // optional, default is file name without extension,
	  // if name is '' it will handle all commands that matches the appropriate aggregate
	  // if name is an array of strings it will handle all commands that matches the appropriate name
	  name: 'unregisterAllContactInformation',

	  // optional, default 0
	  version: 2,

	  // optional, if not defined it will use what is defined as default in aggregate or pass the whole command
	  payload: 'payload',

	  // optional
	  description: 'firstname should always be set',

	  // optional, default Infinity, all pre-conditions will be sorted by this value
	  priority: 1
	}, function (data, aggregate, callback) {
	  // data is the command data
	  // aggregate is the aggregate object
	  // callback is optional, if not defined as function argument you can throw errors or return errors here (sync way)

	  if (!agg.has('firstname')) {
	    return callback('not personalized');
	    // or
	    // return callback(new Error('not personalized'));
	    // or
	    // return callback(new Error()); // if no error message is defined then the description will be taken
	    // or
	    // return callback(new require('cqrs-domain').BusinessRuleError('not personalized', { /* more infos */ }));
	  }
	  callback(null);

	  // or if callback is not defined as function argument
	  // if (!agg.has('firstname')) {
    //   return 'not personalized';
    //   // or
    //   // return new Error('not personalized');
    //   // or
    //   // return new Error(); // if no error message is defined then the description will be taken
    //   // or
    //   // throw new Error(); // if no error message is defined then the description will be taken
    //   // or
    //   // throw new Error('not personalized');
    //   // or
    //   // throw new require('cqrs-domain').BusinessRuleError('not personalized', { /* more infos */ });
    // }
	});


## Command
Collect all needed infos from aggregate to generate your event(s).

Move checks out of here, the correct places are "business rules", "pre-conditions" or "pre-load consitions"!

Do NOT manipulate the aggregate here!

	module.exports = require('cqrs-domain').defineCommand({
	  // optional, default is file name without extension
	  name: 'enterNewPerson',

	  // optional, default 0
	  version: 1,

	  // optional, if not defined it will use what is defined as default in aggregate or pass the whole command
	  payload: 'payload',

	  // optional, default undefined
	  // if true, ensures the aggregate to exists already before this command was handled
	  // if false, ensures the aggregate to not exists already before this command was handled
	  existing: true
	}, function (data, aggregate) {
	  // data is the command data
	  // aggregate is the aggregate object

	  // if (aggregate.get('someAttr') === 'someValue' && aggregate.has('special')) { ... }

	  aggregate.apply('enteredNewPerson', data);
	  // or
	  // aggregate.apply('enteredNewPerson', data, version);
	  // or
	  // aggregate.apply({
	  //   event: 'enteredNewPerson',
	  //   payload: data
	  // });
	})

	// if defined it will load all the requested event streams
	// useful if making bigger redesigns in domain and you need to handle a command on a new aggregate
	.defineEventStreamsToLoad(function (cmd) {
	  return [{ // order is new to old
	    context: 'hr',
	    aggregate: 'mails',
	    aggregateId: cmd.meta.newAggId
	  },{
	    context: 'hr',
	    aggregate: 'persons',
	    aggregateId: cmd.aggregate.id
	  }];
	});

## Event
This is the place where you should manipulate your aggregate.

	module.exports = require('cqrs-domain').defineEvent({
	  // optional, default is file name without extension
	  name: 'enteredNewPerson',

	  // optional, default 0
	  version: 3,

	  // optional, if not defined it will use what is defined as default in aggregate or pass the whole event...
	  payload: 'payload'
	},
	// passing a function is optional
	function (data, aggregate) {
	  // data is the event data
	  // aggregate is the aggregate object

	  aggregate.set('firstname', data.firstname);
	  aggregate.set('lastname', data.lastname);
	  // or
	  // aggregate.set(data);
	});


## Business Rule

	module.exports = require('cqrs-domain').defineBusinessRule({
	  // optional, default is file name without extension
	  name: 'nameEquality',

	  // optional
	  description: 'firstname should never be equal lastname',

	  // optional, default Infinity, all business rules will be sorted by this value
	  priority: 1
	}, function (changed, previous, events, command, callback) {
	  // changed is the new aggregate object
	  // previous is the old aggregate object
	  // events is the array with the resulting events
	  // command the handling command
	  // callback is optional, if not defined as function argument you can throw errors or return errors here (sync way)

	  if (changed.get('firstname') === changed.get('lastname')) {
	    return callback('names not valid');
	    // or
	    // return callback(new Error('names not valid'));
	    // or
	    // return callback(new Error()); // if no error message is defined then the description will be taken
	    // or
	    // return callback(new require('cqrs-domain').BusinessRuleError('names not valid', { /* more infos */ }));
	  }
	  callback(null);

	  // or if callback is not defined as function argument
	  // if (changed.get('firstname') === changed.get('lastname')) {
    //   return 'names not valid';
    //   // or
    //   // return new Error('names not valid');
    //   // or
    //   // return new Error(); // if no error message is defined then the description will be taken
    //   // or
    //   // throw new Error(); // if no error message is defined then the description will be taken
    //   // or
    //   // throw new Error('names not valid');
    //   // or
    //   // throw new require('cqrs-domain').BusinessRuleError('names not valid', { /* more infos */ });
    // }
	});


## EventTransformer
i.e. useful for GDPR relevant data... to have your data encrypted in the eventstore

  // i.e. encrypt
  module.exports = require('cqrs-domain').defineCommittingEventTransformer({
	  // optional, default is file name without extension
	  name: 'enteredNewPerson',

	  // optional, default 0
	  version: 3
	},
	// passing a function is optional
	function (evt) {
	  evt.payload.firstname = encrypt(evt.payload.firstname);
    return evt;
	});
  // or async
  module.exports = require('cqrs-domain').defineCommittingEventTransformer({
	  // optional, default is file name without extension
	  name: 'enteredNewPerson',

	  // optional, default 0
	  version: 3
	},
	// passing a function is optional
	function (evt, callback) {
	  encrypt(evt.payload.firstname, function (err, encrypted) {
      evt.payload.firstname = encrypted;
      callback(err, evt);
    });
	});

  // i.e decrypt
	module.exports = require('cqrs-domain').defineLoadingEventTransformer({
	  // optional, default is file name without extension
	  name: 'enteredNewPerson',

	  // optional, default 0
	  version: 3
	},
	// passing a function is optional
	function (evt) {
	  evt.payload.firstname = decrypt(evt.payload.firstname);
    return evt;
	});
  // or async
  module.exports = require('cqrs-domain').defineLoadingEventTransformer({
	  // optional, default is file name without extension
	  name: 'enteredNewPerson',

	  // optional, default 0
	  version: 3
	},
	// passing a function is optional
	function (evt, callback) {
	  decrypt(evt.payload.firstname, function (err, decrypted) {
      evt.payload.firstname = decrypted;
      callback(err, evt);
    });
	});


## Command Handler (Be careful!!!)
Is your use case not solvable without a custom command handling? Sagas? Micro-Services?

	module.exports = require('cqrs-domain').defineCommandHandler({
	  // optional, default is file name without extension
	  name: 'enterNewSpecialPerson',

	  // optional, default 0
	  version: 1,

	  // optional, if not defined it will pass the whole command...
	  payload: 'payload'
	}, function (aggId, cmd, commandHandler, callback) {
	  // aggId is the aggregate id
	  // cmd is the command data

	  commandHandler.loadAggregate(aggId, function (err, aggregate, stream) {
	    if (err) {
	      return callback(err);
	    }

	    callback(null, [{ my: 'special', ev: 'ent' }]);

	//    // check if destroyed, check revision, validate command
	//    var err = commandHandler.verifyAggregate(aggregate, cmd);
	//    if (err) {
	//      return callback(err);
	//    }
	//
	//    // call api or emit a command or whatever...
	//    // and at the end perhaps you call: commandHandler.handle(cmd, callback);
	  });
	});

## ES6 default exports
Importing ES6 style default exports is supported for all definitions where you also use `module.exports`:
```
module.exports = defineContext({...});
```
works as well as
```
exports.default = defineContext({...});
```
as well as (must be transpiled by babel or tsc to be runnable in node)
```
export default defineContext({...});
```

Also:
```
exports.default = defineAggregate({...});
exports.default = defineCommand({...});
exports.default = defineEvent({...});
// etc...
```
Exports other than the default export are then ignored by this package's structure loader.

[Release notes](https://github.com/adrai/node-cqrs-domain/blob/master/releasenotes.md)

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
var Domain = require('./lib/domain'),
  ValidationError = require('./lib/errors/validationError'),
  BusinessRuleError = require('./lib/errors/businessRuleError'),
  AggregateConcurrencyError = require('./lib/errors/aggregateConcurrencyError'),
  AggregateDestroyedError = require('./lib/errors/aggregateDestroyedError'),
  ConcurrencyError = require('./lib/errors/concurrencyError'),
  DuplicateCommandError = require('./lib/errors/duplicateCommandError'),
  _ = require('lodash'),
  fs = require('fs'),
  path = require('path');

function domain (options) {
  return new Domain(options);
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
  domain['define' + nameCap] = function () {
    return construct(require('./lib/definitions/' + name), _.toArray(arguments));
  };
});

domain.errors = {
  ValidationError: ValidationError,
  BusinessRuleError: BusinessRuleError,
  AggregateConcurrencyError: AggregateConcurrencyError,
  AggregateDestroyedError: AggregateDestroyedError,
  ConcurrencyError: ConcurrencyError,
  DuplicateCommandError: DuplicateCommandError
};

module.exports = domain;
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
  "name": "cqrs-domain",
  "version": "2.14.79",
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
    "debug": "3.2.6",
    "dotty": "0.1.0",
    "eventstore": "1.15.3",
    "jsondate": "0.0.1",
    "lodash": "4.17.19",
    "parent-require": "1.0.0",
    "tolerance": "1.0.0",
    "tv4": "1.3.0",
    "uuid": "3.3.3"
  },
  "devDependencies": {
    "aws-sdk": ">=2.96.0",
    "azure-storage": ">=0.10.0",
    "cradle": ">=0.6.7",
    "eslint": ">=1.0.0",
    "expect.js": ">= 0.1.2",
    "mocha": "3.x.x",
    "mongodb": "2.1.x",
    "redis": ">= 0.10.1",
    "tingodb": ">= 0.0.1",
    "tv4-formats": ">=1.0.0"
  },
  "description": "Node-cqrs-domain is a node.js module based on node-eventstore. It can be very useful as domain component if you work with (d)ddd, cqrs, eventdenormalizer, host, etc.",
  "keywords": [
    "cqrs",
    "eventsourcing",
    "ddd",
    "dddd",
    "command",
    "event",
    "eventdenormalizer",
    "domain"
  ],
  "homepage": "https://github.com/adrai/node-cqrs-domain",
  "repository": {
    "type": "git",
    "url": "git@github.com:adrai/node-cqrs-domain.git"
  },
  "bugs": {
    "url": "https://github.com/adrai/node-cqrs-domain/issues"
  },
  "licenses": [
    {
      "type": "MIT",
      "url": "https://raw.github.com/adrai/node-cqrs-domain/master/licence"
    }
  ],
  "scripts": {
    "test": "mocha test/unit && mocha test/integration"
  }
}
```

## File: `releasenotes.md`
```markdown
## [v2.14.79](https://github.com/adrai/node-cqrs-domain/compare/v2.14.78...v2.14.79)
- mongodb: useUnifiedTopology

## [v2.14.78](https://github.com/adrai/node-cqrs-domain/compare/v2.14.77...v2.14.78)
- catch throwing errors during command handling

## [v2.14.77](https://github.com/adrai/node-cqrs-domain/compare/v2.14.76...v2.14.77)
- Fix for validation error(s) swallowing thanks to [ssipos90](https://github.com/ssipos90)

## [v2.14.76](https://github.com/adrai/node-cqrs-domain/compare/v2.14.75...v2.14.76)
- update eventstore

## [v2.14.75](https://github.com/adrai/node-cqrs-domain/compare/v2.14.74...v2.14.75)
- update eventstore

## [v2.14.74](https://github.com/adrai/node-cqrs-domain/compare/v2.14.73...v2.14.74)
- update deps and eventstore

## [v2.14.73](https://github.com/adrai/node-cqrs-domain/compare/v2.14.72...v2.14.73)
- add edge case error handling on main command handler

## [v2.14.72](https://github.com/adrai/node-cqrs-domain/compare/v2.14.71...v2.14.72)
- update deps and eventstore

## [v2.14.71](https://github.com/adrai/node-cqrs-domain/compare/v2.14.7...v2.14.71)
- update eventstore

## [v2.14.7](https://github.com/adrai/node-cqrs-domain/compare/v2.14.6...v2.14.7)
- prepare previousModel before evaluating preConditions in order to prevent model mutation inside them 

## [v2.14.6](https://github.com/adrai/node-cqrs-domain/compare/v2.14.5...v2.14.6)
- updated node-eventstore and added optional position property to event

## [v2.14.5](https://github.com/adrai/node-cqrs-domain/compare/v2.14.4...v2.14.5)
- updated node-eventstore and lodash dependencies

## [v2.14.4](https://github.com/adrai/node-cqrs-domain/compare/v2.14.3...v2.14.4)
- pass error constructors to customLoader

## [v2.14.3](https://github.com/adrai/node-cqrs-domain/compare/v2.14.2...v2.14.3)
- update node-eventstore dependency

## [v2.14.2](https://github.com/adrai/node-cqrs-domain/compare/v2.14.0...v2.14.1)
- add option for asynchronous custom structureLoader thank to [nanov](https://github.com/nanov)

## [v2.14.1](https://github.com/adrai/node-cqrs-domain/compare/v2.14.0...v2.14.1)
- Schema validation rules structure loader bug fix [#127](https://github.com/adrai/node-cqrs-domain/pull/127) thanks to [OrH](https://github.com/OrH)

## [v2.14.0](https://github.com/adrai/node-cqrs-domain/compare/v2.13.1...v2.14.0)
- add option to add custom structureLoader implementation [#125](https://github.com/adrai/node-cqrs-domain/pull/125) thanks to [nanov](https://github.com/nanov)

## [v2.13.1](https://github.com/adrai/node-cqrs-domain/compare/v2.12.3...v2.13.1)
- Introduce externallyLoaded option to context, and load those separately [#121](https://github.com/adrai/node-cqrs-domain/pull/121) thanks to [nanov](https://github.com/nanov)

## [v2.12.3](https://github.com/adrai/node-cqrs-domain/compare/v2.12.2...v2.12.3)
- update eventstore

## [v2.12.2](https://github.com/adrai/node-cqrs-domain/compare/v2.12.1...v2.12.2)
- generated rejectedCommand for AggregateDestroyedError now contains revision information (if provided)

## [v2.12.1](https://github.com/adrai/node-cqrs-domain/compare/v2.12.0...v2.12.1)
- Do not set revision when persistence is disabled [#120](https://github.com/adrai/node-cqrs-domain/pull/120) thanks to [nanov](https://github.com/nanov)

## [v2.12.0](https://github.com/adrai/node-cqrs-domain/compare/v2.11.4...v2.12.0)
- introduce event transformers; to give possibility to be GDPR compliant

## [v2.11.4](https://github.com/adrai/node-cqrs-domain/compare/v2.11.2...v2.11.4)
- remove deprecated option max_attempts from redis options

## [v2.11.2](https://github.com/adrai/node-cqrs-domain/compare/v2.11.1...v2.11.2)
- update eventstore

## [v2.11.1](https://github.com/adrai/node-cqrs-domain/compare/v2.11.0...v2.11.1)
- update eventstore

## [v2.11.0](https://github.com/adrai/node-cqrs-domain/compare/v2.10.0...v2.11.0)
- compatibility with new mongodb version (3.x)

## [v2.10.0](https://github.com/adrai/node-cqrs-domain/compare/v2.9.8...v2.10.0)
- Use of node loader extensions for valid file types of parsing definition sources [#113](https://github.com/adrai/node-cqrs-domain/pull/113) thanks to [repkins](https://github.com/repkins)

## [v2.9.8](https://github.com/adrai/node-cqrs-domain/compare/v2.9.7...v2.9.8)
- do not verify the revision when disablePersistence is set to true [#112](https://github.com/adrai/node-cqrs-domain/issues/112) thanks to [repkins](https://github.com/repkins)

## [v2.9.7](https://github.com/adrai/node-cqrs-domain/compare/v2.9.6...v2.9.7)
- update eventstore

## [v2.9.6](https://github.com/adrai/node-cqrs-domain/compare/v2.9.5...v2.9.6)
- fixing definePreLoadCondition handing commands with version [#111](https://github.com/adrai/node-cqrs-domain/issues/111) thanks to [repkins](https://github.com/repkins)

## [v2.9.5](https://github.com/adrai/node-cqrs-domain/compare/v2.9.4...v2.9.5)
- update eventstore

## [v2.9.4](https://github.com/adrai/node-cqrs-domain/compare/v2.9.3...v2.9.4)
- update eventstore

## [v2.9.3](https://github.com/adrai/node-cqrs-domain/compare/v2.9.2...v2.9.3)
- update eventstore

## [v2.9.2](https://github.com/adrai/node-cqrs-domain/compare/v2.9.1...v2.9.2)
- update eventstore

## [v2.9.1](https://github.com/adrai/node-cqrs-domain/compare/v2.9.0...v2.9.1)
- fixing dynamodb DocumentClient initialization [#105](https://github.com/adrai/node-cqrs-domain/pull/105) thanks to [Glockenbeat](https://github.com/Glockenbeat)

## [v2.9.0](https://github.com/adrai/node-cqrs-domain/compare/v2.8.1...v2.9.0)
- Support default exports [#104](https://github.com/adrai/node-cqrs-domain/pull/#104) thanks to [IRT-fbachmann](https://github.com/IRT-fbachmann)

## [v2.8.1](https://github.com/adrai/node-cqrs-domain/compare/v2.8.0...v2.8.1)
- fix aggregateLock [#103](https://github.com/adrai/node-cqrs-domain/pull/#103) thanks to [emmkong](https://github.com/emmkong)

## [v2.8.0](https://github.com/adrai/node-cqrs-domain/compare/v2.7.0...v2.8.0)
- dynamodb aggregateLock implementation [#100](https://github.com/adrai/node-cqrs-domain/pull/#100) thanks to [emmkong](https://github.com/emmkong)

## [v2.7.0](https://github.com/adrai/node-cqrs-domain/compare/v2.6.0...v2.7.0)
- Added non-breaking option for asynchronous command validation. [#99](https://github.com/adrai/node-cqrs-domain/pull/#99) thanks to [velislav-bankov](https://github.com/velislav-bankov)

## [v2.6.0](https://github.com/adrai/node-cqrs-domain/compare/v2.5.10...v2.6.0)
- Added non breaking commandAwareAggregateIdGenerator [#93](https://github.com/adrai/node-cqrs-domain/pull/#93) thanks to the idea of [nanov](https://github.com/nanov)

## [v2.5.10](https://github.com/adrai/node-cqrs-domain/compare/v2.5.9...v2.5.10)
- correct resolve revision for commands that have no aggregate or context specified [#92](https://github.com/adrai/node-cqrs-domain/pull/#92) thanks to [velislav-bankov](https://github.com/velislav-bankov)

## [v2.5.9](https://github.com/adrai/node-cqrs-domain/compare/v2.5.8...v2.5.9)
- update eventstore

## [v2.5.7](https://github.com/adrai/node-cqrs-domain/compare/v2.5.5...v2.5.7)
- fix for new mongodb driver

## [v2.5.5](https://github.com/adrai/node-cqrs-domain/compare/v2.5.2...v2.5.5)
- make command handling faster for some use cases

## [v2.5.2](https://github.com/adrai/node-cqrs-domain/compare/v2.5.1...v2.5.2)
- fix for defining ignoring snapshots

## [v2.5.1](https://github.com/adrai/node-cqrs-domain/compare/v2.5.0...v2.5.1)
- update eventstore

## [v2.5.0](https://github.com/adrai/node-cqrs-domain/compare/v2.4.8...v2.5.0)
- reactivate ignoring snapshots

## [v2.4.8](https://github.com/adrai/node-cqrs-domain/compare/v2.4.7...v2.4.8)
- fix preLoadConditions check

## [v2.4.7](https://github.com/adrai/node-cqrs-domain/compare/v2.4.6...v2.4.7)
- update eventstore

## [v2.4.6](https://github.com/adrai/node-cqrs-domain/compare/v2.4.5...v2.4.6)
- possibility to set payload to '' if there is a defaultPayload in handlers

## [v2.4.5](https://github.com/adrai/node-cqrs-domain/compare/v2.4.4...v2.4.5)
- update deps

## [v2.4.4](https://github.com/adrai/node-cqrs-domain/compare/v2.3.21...v2.4.4)
- possibility to disable persistence on an aggregate

## [v2.3.21](https://github.com/adrai/node-cqrs-domain/compare/v2.3.20...v2.3.21)
- update deps

## [v2.3.20](https://github.com/adrai/node-cqrs-domain/compare/v2.3.19...v2.3.20)
- update eventstore

## [v2.3.19](https://github.com/adrai/node-cqrs-domain/compare/v2.3.18...v2.3.19)
- Do not overwrite user-provided meta properties [#85](https://github.com/adrai/node-cqrs-domain/pull/#85) thanks to [jwoudenberg](https://github.com/jwoudenberg)

## [v2.3.18](https://github.com/adrai/node-cqrs-domain/compare/v2.3.17...v2.3.18)
- update eventstore

## [v2.3.17](https://github.com/adrai/node-cqrs-domain/compare/v2.3.16...v2.3.17)
- update eventstore

## [v2.3.16](https://github.com/adrai/node-cqrs-domain/compare/v2.3.15...v2.3.16)
- update eventstore

## [v2.3.15](https://github.com/adrai/node-cqrs-domain/compare/v2.3.14...v2.3.15)
- update eventstore

## [v2.3.14](https://github.com/adrai/node-cqrs-domain/compare/v2.3.13...v2.3.14)
- update eventstore

## [v2.3.13](https://github.com/adrai/node-cqrs-domain/compare/v2.3.12...v2.3.13)
- update eventstore

## [v2.3.12](https://github.com/adrai/node-cqrs-domain/compare/v2.3.9...v2.3.12)
- update eventstore

## [v2.3.9](https://github.com/adrai/node-cqrs-domain/compare/v2.3.8...v2.3.9)
- introduce applyLastEvent in combination with skipHistory on aggregate

## [v2.3.8](https://github.com/adrai/node-cqrs-domain/compare/v2.3.4...v2.3.8)
- update eventstore

## [v2.3.4](https://github.com/adrai/node-cqrs-domain/compare/v2.3.3...v2.3.4)
- update eventstore
- redis, mongodb: call disconnect on ping error

## [v2.3.3](https://github.com/adrai/node-cqrs-domain/compare/v2.3.2...v2.3.3)
- update eventstore
- Support mongo connection string

## [v2.3.2](https://github.com/adrai/node-cqrs-domain/compare/v2.3.1...v2.3.2)
- update eventstore
- redis, mongodb: call disconnect on ping error

## [v2.3.1](https://github.com/adrai/node-cqrs-domain/compare/v2.3.0...v2.3.1)
- update eventstore

## [v2.3.0](https://github.com/adrai/node-cqrs-domain/compare/v2.2.3...v2.3.0)
- Support for custom conditions before aggregates are locked [#76](https://github.com/adrai/node-cqrs-domain/pull/#76) thanks to [hilkeheremans](https://github.com/hilkeheremans)

## [v2.2.3](https://github.com/adrai/node-cqrs-domain/compare/v2.2.2...v2.2.3)
- update eventstore

## [v2.2.2](https://github.com/adrai/node-cqrs-domain/compare/v2.2.1...v2.2.2)
- redis: added optional heartbeat

## [v2.2.1](https://github.com/adrai/node-cqrs-domain/compare/v2.2.0...v2.2.1)
- update eventstore
- fix version handling for command validation

## [v2.2.0](https://github.com/adrai/node-cqrs-domain/compare/v2.1.5...v2.2.0)
- version property for command validation rules

## [v2.1.5](https://github.com/adrai/node-cqrs-domain/compare/v2.1.4...v2.1.5)
- updated eventstore

## [v2.1.4](https://github.com/adrai/node-cqrs-domain/compare/v2.1.2...v2.1.4)
- introduce skipHistory on aggregate

## [v2.1.2](https://github.com/adrai/node-cqrs-domain/compare/v2.1.1...v2.1.2)
- little optimization for old folder structure in structureLoader

## [v2.1.1](https://github.com/adrai/node-cqrs-domain/compare/v2.1.0...v2.1.1)
- little optimization for structureLoader

## [v2.1.0](https://github.com/adrai/node-cqrs-domain/compare/v2.0.5...v2.1.0)
- fix snapshot mongodb usage (ATTENTION: this could break if you have existing snapshots)

## [v2.0.5](https://github.com/adrai/node-cqrs-domain/compare/v2.0.4...v2.0.5)
- fix for usage without an aggregate name

## [v2.0.4](https://github.com/adrai/node-cqrs-domain/compare/v2.0.3...v2.0.4)
- redis: fix for new redis lib

## [v2.0.3](https://github.com/adrai/node-cqrs-domain/compare/v2.0.2...v2.0.3)
- mongodb: added optional heartbeat

## [v2.0.2](https://github.com/adrai/node-cqrs-domain/compare/v2.0.1...v2.0.2)
- fix initialization of generalContext

## [v2.0.1](https://github.com/adrai/node-cqrs-domain/compare/v2.0.0...v2.0.1)
- fix event check before setting the event to undispatched

## [v2.0.0](https://github.com/adrai/node-cqrs-domain/compare/v1.10.9...v2.0.0)
- IMPORTANT: extending the validator (tv4) is done differently, getTv4() not working anymore
- added migration api: defineEventStreamsToLoad for command to ensure business rules

## [v1.10.9](https://github.com/adrai/node-cqrs-domain/compare/v1.10.8...v1.10.9)
- give possibility to use mongodb with authSource

## [v1.10.8](https://github.com/adrai/node-cqrs-domain/compare/v1.10.7...v1.10.8)
- update eventstore

## [v1.10.7](https://github.com/adrai/node-cqrs-domain/compare/v1.10.6...v1.10.7)
- optimization for `npm link`'ed development

## [v1.10.6](https://github.com/adrai/node-cqrs-domain/compare/v1.10.4...v1.10.6)
- improved a little bit the performance whan applying a lot of history events

## [v1.10.4](https://github.com/adrai/node-cqrs-domain/compare/v1.10.2...v1.10.4)
- catch throwing errors when calling callback

## [v1.10.2](https://github.com/adrai/node-cqrs-domain/compare/v1.10.1...v1.10.2)
- expose warnings during initialization

## [v1.10.1](https://github.com/adrai/node-cqrs-domain/compare/v1.10.0...v1.10.1)
- update eventstore

## [v1.10.0](https://github.com/adrai/node-cqrs-domain/compare/v1.9.0...v1.10.0)
- introduce defineIgnoreSnapshot function on aggregate

## [v1.9.0](https://github.com/adrai/node-cqrs-domain/compare/v1.8.3...v1.9.0)
- added optional command de-duplication

## [v1.8.3](https://github.com/adrai/node-cqrs-domain/compare/v1.8.2...v1.8.3)
- fix calculation of snapshots

## [v1.8.2](https://github.com/adrai/node-cqrs-domain/compare/v1.8.1...v1.8.2)
- added possibility to use real BusinessRuleError object in pre-conditions and business rules

## [v1.8.1](https://github.com/adrai/node-cqrs-domain/compare/v1.8.0...v1.8.1)
- update eventstore and make use of its commitStamp functionality

## [v1.8.0](https://github.com/adrai/node-cqrs-domain/compare/v1.7.3...v1.8.0)
- added more detailed infos for some ValidationErrors

## [v1.7.3](https://github.com/adrai/node-cqrs-domain/compare/v1.7.2...v1.7.3)
- refactored reorderValidationRules

## [v1.7.2](https://github.com/adrai/node-cqrs-domain/compare/v1.7.1...v1.7.2)
- extend apply function to pass version

## [v1.7.1](https://github.com/adrai/node-cqrs-domain/compare/v1.7.0...v1.7.1)
- little fix in structureLoader, general preConditions

## [v1.7.0](https://github.com/adrai/node-cqrs-domain/compare/v1.6.1...v1.7.0)
- added aggregateIdGenerator

## [v1.6.1](https://github.com/adrai/node-cqrs-domain/compare/v1.5.3...v1.6.1)
- added defineAggregateIdGenerator
- update eventstore

## [v1.5.3](https://github.com/adrai/node-cqrs-domain/compare/v1.5.2...v1.5.3)
- update eventstore

## [v1.5.2](https://github.com/adrai/node-cqrs-domain/compare/v1.5.1...v1.5.2)
- made some performance improvements

## [v1.5.1](https://github.com/adrai/node-cqrs-domain/compare/v1.5.0...v1.5.1)
- update eventstore

## [v1.5.0](https://github.com/adrai/node-cqrs-domain/compare/v1.4.10...v1.5.0)
- attach aggregate preConditions to all commands [#28](https://github.com/adrai/node-cqrs-domain/issues/#28)
- fix priority of preConditions

## [v1.4.10](https://github.com/adrai/node-cqrs-domain/compare/v1.4.9...v1.4.10)
- factory methods for event store and aggregate lock [#35](https://github.com/adrai/node-cqrs-domain/pull/#35) thanks to [nizachon](https://github.com/nizachon)

## [v1.4.9](https://github.com/adrai/node-cqrs-domain/compare/v1.4.6...v1.4.9)
- optimize structureParser
- allow setting values on aggregateModel only in event handle function

## [v1.4.6](https://github.com/adrai/node-cqrs-domain/compare/v1.4.5...v1.4.6)
- fix handling when command does not generate any event

## [v1.4.5](https://github.com/adrai/node-cqrs-domain/compare/v1.4.4...v1.4.5)
- update eventstore

## [v1.4.4](https://github.com/adrai/node-cqrs-domain/compare/v1.4.2...v1.4.4)
- fix usage with own db implementation

## [v1.4.2](https://github.com/adrai/node-cqrs-domain/compare/v1.4.1...v1.4.2)
- catch thrown errors in validation workflow

## [v1.4.1](https://github.com/adrai/node-cqrs-domain/compare/v1.4.0...v1.4.1)
- expose error prototypes

## [v1.4.0](https://github.com/adrai/node-cqrs-domain/compare/v1.3.2...v1.4.0)
- added getInfo function

## [v1.3.2](https://github.com/adrai/node-cqrs-domain/compare/v1.3.1...v1.3.2)
- fix snapshot creation call

## [v1.3.1](https://github.com/adrai/node-cqrs-domain/compare/v1.3.0...v1.3.1)
- optimized catching of thrown error in businessRules and preConditions

## [v1.3.0](https://github.com/adrai/node-cqrs-domain/compare/v1.2.10...v1.3.0)
- expose tv4 instance
- IMPORTANT: removed tv4-formats

## [v1.2.10](https://github.com/adrai/node-cqrs-domain/compare/v1.2.8...v1.2.10)
- introduce existing flag in command

## [v1.2.8](https://github.com/adrai/node-cqrs-domain/compare/v1.2.7...v1.2.8)
- update some dependencies

## [v1.2.7](https://github.com/adrai/node-cqrs-domain/compare/v1.2.6...v1.2.7)
- handle case of same aggregateId in different contexts or aggregates

## [v1.2.6](https://github.com/adrai/node-cqrs-domain/compare/v1.2.5...v1.2.6)
- added possibility to define pre-conditions for all commands of an aggregate

## [v1.2.5](https://github.com/adrai/node-cqrs-domain/compare/v1.2.4...v1.2.5)
- update eventstore dependency

## [v1.2.4](https://github.com/adrai/node-cqrs-domain/compare/v1.2.3...v1.2.4)
- address [#27](https://github.com/adrai/node-cqrs-domain/issues/27)

## [v1.2.3](https://github.com/adrai/node-cqrs-domain/compare/v1.2.2...v1.2.3)
- add possibility to define multiple pre-conditions per command

## [v1.2.2](https://github.com/adrai/node-cqrs-domain/compare/v1.2.1...v1.2.2)
- fix pre-conditions

## [v1.2.1](https://github.com/adrai/node-cqrs-domain/compare/v1.2.0...v1.2.1)
- added azure-table support [#25](https://github.com/adrai/node-cqrs-domain/pull/#25) thanks to [sbiaudet](https://github.com/sbiaudet)

## v1.2.0
- introduced pre-conditions

## v1.1.8
- update eventstore dependency

## v1.1.7
- update eventstore dependency

## v1.1.6
- update eventstore dependency

## v1.1.5
- clone command and event payload before passing to handle function

## v1.1.4
- fixes a major bug for concurrent command handling of same aggregate instance

## v1.1.3
- fixes [#22](https://github.com/adrai/node-cqrs-domain/pull/22) thanks to [zauberpony](https://github.com/zauberpony)

## v1.1.2
- optimize structureLoader (case if directory starts with same name)

## v1.1.1
- do not extend the command if no aggregateId is presented

## v1.1.0
- add possibility to define defaultCommandPayload and defaultEventPayload in aggragate
- add additional validation formats for tv4 [#21](https://github.com/adrai/node-cqrs-domain/pull/21) thanks to [zauberpony](https://github.com/zauberpony)

## v1.0.7
- use new version of eventstore

## v1.0.6
- fix for fallback for file and directory names

## v1.0.5
- allow to not pass an event function in defining an event

## v1.0.4
- do not try-catch errors in domain handle

## v1.0.3
- fix some callback arguments of aggregateLock

## v1.0.2
- fix handling of command without command validation
- fix multiple adding of same definition
- remove debug in redis

## v1.0.0
- refactored whole module
- added possibility to define aggregateId, aggregate and context
- generic message structure for commands and events
- command validation changed, now based on [tv4](https://github.com/geraintluff/tv4)
- added a lot of tests
- stabilized everything
- optimized performance
- IMPORTANT: changed API!!!

## v0.8.2
- do not use newer eventstore version

## v0.8.1
- do not use newer viewmodel version

## v0.8.0
- updated node-queue

## v0.7.9
- send commandRejected event with better reason

## v0.7.8
- added optional callback on commandhandler defaultHandle

## v0.7.7
- optimization for npm module naming

## v0.7.6
- updated eventstore

## v0.7.5
- introduce versioned messages and snapshots

## v0.7.4
- fixed naming of handleUndispatchedEvents option

## v0.7.3
- updated eventstore

## v0.7.2
- update dependencies

## v0.7.1
- load sagas always from db

## v0.7.0
- introduced commandLock for distributed domain (handling same aggregate instance on multiple machines)

## v0.6.1
- buffer commands by aggregate id

## v0.6.0
- don't publish in eventstore but publish in domain
- removed flags: publishingInterval, forkEventDispatching
- added handleUpdispatchedEvents flag

## v0.5.3
- fix for async business rules (issue [#13](https://github.com/adrai/node-cqrs-domain/issues/13))

## v0.5.2
- fix commandDispatcher if no commandqueue is used

## v0.5.0
- a complete change of validation rules (see new [rule-validator](https://github.com/adrai/rule-validator))

## v0.4.4
- added disableQueuing flag

## v0.4.3
- strip .js file extensions to enable loading of .coffee scripts too

## v0.4.2
- added forcedQueuing flag

## v0.4.1
- added optional snapshotThreshold on aggregate

## v0.4.0
- asynchronous api for saga

## v0.3.9
- optimized performance a little

## v0.3.8
- updated eventstore package
- optimized initialization
```

## File: `lib/aggregateModel.js`
```javascript
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

## File: `lib/commandDispatcher.js`
```javascript
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

## File: `lib/defaultCommandHandler.js`
```javascript
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

            var evtTransformer = self.aggregate.getLoadingEventTransformer(evtName, version) || { transform: function (e, cb) { cb(null, e); } };
            evtTransformer.transform(evt, clb);
          }, function (err, evts) {
            if (err) return callback(err);

            var snapNeed = self.aggregate.loadFromHistory(aggregate, null, evts, loadingTime, str, null, notSameOrigin);

            if (!isNewSnapShotNeeded) {
              isNewSnapShotNeeded = snapNeed;
            }

            streams.push(str);

            callback(null);
          });
        });
      }, function (err) {
        if (err) {
          return callback(err);
        }

        var loadingTime = Date.now() - totalLoadingTime;

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

          var snapNeed = self.aggregate.loadFromHistory(aggregate, null, events, loadingTime, stream, streams);

          if (!isNewSnapShotNeeded) {
            isNewSnapShotNeeded = snapNeed;
          }

          debug('check if new snapshot is needed');
          if (isNewSnapShotNeeded) {
            self.createSnapshot(aggregate, stream);
          }

          // callback with the aggregate and the streams
          callback(null, aggregate, streams);
        });
      });
    });
  },

  /**
   * Creates a new snapshot.
   * @param {AggregateModel} aggregate The passed aggregate.
   * @param {Object}         stream    The event stream.
   * @param {Function}       callback  The function, that will be called when this action is completed. [optional]
   *                                   `function(err){}`
   */
  createSnapshot: function (aggregate, stream, callback) {
    if (!aggregate || !_.isObject(aggregate)) {
      var err = new Error('Please pass a valid aggregate!');
      debug(err);
      throw err;
    }
    if (!stream || !_.isObject(stream)) {
      var err = new Error('Please pass a valid aggregate!');
      debug(err);
      throw err;
    }

    var hasAggregateName = !!this.definitions.command.aggregate;
    var hasContextName = !!this.definitions.command.context;

    var query = {
      aggregateId: aggregate.id
    };

    if (hasAggregateName) {
      query.aggregate = this.aggregate.name;
    }

    if (hasContextName) {
      query.context = this.aggregate.context.name;
    }

    query.data = aggregate.toJSON();
    query.revision = stream.lastRevision;
    query.version = this.aggregate.version;

    var self = this;

    process.nextTick(function() {
      var transformer = self.aggregate.committingSnapshotTransformers[self.aggregate.context.name + '.' + self.aggregate.name + '.' + self.aggregate.version] || function (sn, cb) { cb(null, sn); };
      transformer(query.data, function (err, snapData) {
        if (err) {
          debug(err);
          if (callback) callback(err);
          return;
        }

        query.data = snapData;

        debug('cerate new snapshot');
        self.eventStore.createSnapshot(query, function (err) {
          if (err) {
            debug(err);
            if (callback) callback(err);
            return;
          }
          debug('snapshot created');
          if (callback) callback(null);
        });
      });
    });
  },

  /**
   * Returns an error if the aggregate is destroyed.
   * @param {AggregateModel} aggregate The passed aggregate.
   * @param {Object}         cmd       The command.
   * @returns {AggregateDestroyedError}
   */
  isAggregateDestroyed: function (aggregate, cmd) {
    if (!aggregate || !_.isObject(aggregate)) {
      var err = new Error('Please pass a valid aggregate!');
      debug(err);
      throw err;
    }
    if (!cmd || !_.isObject(cmd)) {
      var err = new Error('Please pass a valid command!');
      debug(err);
      throw err;
    }

    var contextName, aggregateName, aggregateId;

    if (!!this.definitions.command.context) {
      contextName = dotty.get(cmd, this.definitions.command.context);
    }

    if (!!this.definitions.command.aggregate) {
      aggregateName = dotty.get(cmd, this.definitions.command.aggregate);
    }

    if (!!this.definitions.command.aggregateId) {
      aggregateId = dotty.get(cmd, this.definitions.command.aggregateId);
    }

    var streamInfo = {
      context: contextName,
      aggregate: aggregateName,
      aggregateId: aggregateId
    };

    if (aggregate.isDestroyed()) {
      return new AggregateDestroyedError('Aggregate has already been destroyed!', {
        aggregateId: aggregate.id,
        aggregateRevision: aggregate.getRevision(streamInfo)
      });
    }

    return null;
  },

  /**
   * Returns an error if the revision does not match.
   * @param {AggregateModel} aggregate The passed aggregate.
   * @param {Object}         cmd       The command.
   * @returns {AggregateConcurrencyError}
   */
  isRevisionWrong: function (aggregate, cmd) {
    if (!aggregate || !_.isObject(aggregate)) {
      var err = new Error('Please pass a valid aggregate!');
      debug(err);
      throw err;
    }
    if (!cmd || !_.isObject(cmd)) {
      var err = new Error('Please pass a valid command!');
      debug(err);
      throw err;
    }

    var hasRevision = !!this.definitions.command.revision;

    if (!hasRevision) {
      return null;
    }

    var revisionInCommand = dotty.get(cmd, this.definitions.command.revision);
    if (revisionInCommand === null || revisionInCommand === undefined) {
      return null;
    }

    var contextName, aggregateName, aggregateId;

    if (!!this.definitions.command.context) {
      contextName = dotty.get(cmd, this.definitions.command.context);
    }

    if (!!this.definitions.command.aggregate) {
      aggregateName = dotty.get(cmd, this.definitions.command.aggregate);
    }

    if (!!this.definitions.command.aggregateId) {
      aggregateId = dotty.get(cmd, this.definitions.command.aggregateId);
    }

    var streamInfo = {
      context: contextName,
      aggregate: aggregateName,
      aggregateId: aggregateId
    };

    if (revisionInCommand === aggregate.getRevision(streamInfo)) {
      return null;
    }

    return new AggregateConcurrencyError('Actual revision in command is "' + revisionInCommand + '", but expected is "' + aggregate.getRevision(streamInfo) + '"!', {
      aggregateId: aggregate.id,
      aggregateRevision: aggregate.getRevision(streamInfo),
      commandRevision: revisionInCommand
    });
  },

  /**
   * Returns an error if the command is not valid.
   * @param {Object} cmd The command.
   * @returns {ValidationError}
   */
  validateCommand: function (cmd, callback) {
    if (!cmd || !_.isObject(cmd)) {
      debug(err);
      return callback(new Error('Please pass a valid command!'), null);
    }
    return this.aggregate.validateCommand(cmd, callback);
  },

  checkPreLoadConditions: function (cmd, clb) {
    this.aggregate.checkPreLoadConditions(cmd, clb);
  },

  /**
   * Returns an error if verification fails.
   * @param {AggregateModel} aggregate The passed aggregate.
   * @param {Object}         cmd       The command.
   * @returns {Error}
   */
  verifyAggregate: function (aggregate, cmd) {
    if (!aggregate || !_.isObject(aggregate)) {
      var err = new Error('Please pass a valid aggregate!');
      debug(err);
      throw err;
    }
    if (!cmd || !_.isObject(cmd)) {
      var err = new Error('Please pass a valid command!');
      debug(err);
      throw err;
    }

    var reason = this.isAggregateDestroyed(aggregate, cmd);
    if (reason) {
      return reason;
    }

    if (this.aggregate.disablePersistence) return;

    reason = this.isRevisionWrong(aggregate, cmd);
    if (reason) {
      return reason;
    }
  },

  /**
   * Handles the command by passing it to the handle function of the aggregate.
   * @param {AggregateModel} aggregate The passed aggregate.
   * @param {Object}         cmd       The command.
   * @param {Function}       callback  The function, that will be called when this action is completed.
   *                                   `function(err){}`
   */
  letHandleCommandByAggregate: function (aggregate, cmd, callback) {
    if (!aggregate || !_.isObject(aggregate)) {
      var err = new Error('Please pass a valid aggregate!');
      debug(err);
      throw err;
    }
    if (!cmd || !_.isObject(cmd)) {
      var err = new Error('Please pass a valid command!');
      debug(err);
      throw err;
    }
    if (!callback || !_.isFunction(callback)) {
      var err = new Error('Please pass a valid function!');
      debug(err);
      throw err;
    }

    this.aggregate.handle(aggregate, cmd, callback);
  },

  /**
   * Checks if the aggregate lock is ok.
   * @param {String}   aggregateId The passed aggregateId.
   * @param {Function} callback    The function, that will be called when this action is completed.
   *                               `function(err){}`
   */
  checkAggregateLock: function (aggregateId, callback) {
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

    var self = this;

    this.aggregateLock.getAll(aggregateId, function (err, workerIds) {
      if (err) {
        return callback(err);
      }

      if (workerIds.length === 1 && workerIds[0] === self.id) {
        return callback(null);
      }

      var err = new ConcurrencyError('Aggregate is locked by an other command handler!');
      debug(err);
      callback(err);
    });
  },

  /**
   * Resolves if the aggregate lock.
   * @param {String}   aggregateId The passed aggregateId.
   * @param {Function} callback    The function, that will be called when this action is completed.
   *                               `function(err){}`
   */
  resolveAggregateLock: function (aggregateId, callback) {
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

    this.aggregateLock.resolve(aggregateId, callback);
  },

  /**
   * Saves the uncommitted events of an aggregate in the eventstore.
   * @param {AggregateModel} aggregate The passed aggregate.
   * @param {Array}          streams   The event streams.
   * @param {Function}       callback  The function, that will be called when this action is completed.
   *                                   `function(err, eventsToDispatch){}`
   */
  commit: function (aggregate, streams, callback) {
    if (!aggregate || !_.isObject(aggregate)) {
      var err = new Error('Please pass a valid aggregate!');
      debug(err);
      throw err;
    }
    if (!streams || !_.isArray(streams)) {
      var err = new Error('Please pass valid streams!');
      debug(err);
      throw err;
    }
    if (!callback || !_.isFunction(callback)) {
      var err = new Error('Please pass a valid callback!');
      debug(err);
      throw err;
    }

    var uncommitedEvents = aggregate.getUncommittedEvents();

    if (uncommitedEvents.length === 0) {
      debug('no events generated');
      return callback(null, []);
    }

    var self = this;

    var evtsToDispatch = [];
    var fakeEventStream = {
      aggregateId: dotty.get(uncommitedEvents[0], self.definitions.event.aggregateId),
      aggregate: dotty.get(uncommitedEvents[0], self.definitions.event.aggregate),
      context: dotty.get(uncommitedEvents[0], self.definitions.event.context),
      uncommittedEvents: []
    };

    for (var e in uncommitedEvents) {
      var evt = uncommitedEvents[e];

      var stream = _.find(streams, function (s) {
        return s.context === dotty.get(evt, self.definitions.event.context) &&
          s.aggregate === dotty.get(evt, self.definitions.event.aggregate) &&
          s.aggregateId === dotty.get(evt, self.definitions.event.aggregateId);
      });

      if (!stream && !self.aggregate.disablePersistence) {
        debug('no stream found for:', evt);
        return callback(new Error('No event stream found for evt with id:' + dotty.get(evt, self.definitions.event.id)));
      }

      if (stream) stream.addEvent(evt);

      if (!stream && self.aggregate.disablePersistence) {
        var eventStoreEvent = new EventFromEventStore(fakeEventStream, evt, self.eventStore.eventMappings);
        eventStoreEvent.disablePersistence = true;
        eventStoreEvent.id = uuid().toString();
        evtsToDispatch.push(eventStoreEvent);
      }
    }

    async.each(streams, function (stream, callback) {
      if (self.aggregate.disablePersistence) {
        for (var ie = 0, evtLength = stream.uncommittedEvents.length; ie < evtLength; ie++) {
          stream.uncommittedEvents[ie].disablePersistence = true;
          stream.uncommittedEvents[ie].id = uuid().toString();
          evtsToDispatch.push(stream.uncommittedEvents[ie]);
        }
        return callback(null);
      }

      async.each(stream.uncommittedEvents, function (streamEvent, clb) {
        var evt = streamEvent.payload;
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

        var evtTransformer = self.aggregate.getCommittingEventTransformer(evtName, version) || { transform: function (e, cb) { cb(null, e); } };
        evtTransformer.transform(evt, function (err, evt) {
          if (err) return clb(err);
          streamEvent.payload = evt;
          clb(null);
        });
      }, function (err) {
        if (err) return callback(err);
        stream.commit(function (err, stream) {
          if (err) return callback(err);
          evtsToDispatch = evtsToDispatch.concat(stream.eventsToDispatch);
          callback(null);
        });
      });
    }, function (err) {
      if (err) return callback(err);

      async.map(evtsToDispatch, function (streamEvent, clb) {
        var evt = streamEvent.payload;
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
        evtTransformer.transform(evt, function (err, evt) {
          if (err) return clb(err);
          var clonedStreamEvent = _.clone(streamEvent);
          clonedStreamEvent.payload = evt;
          clb(null, clonedStreamEvent);
        });
      }, function (err, evtsToDispatch) {
        if (err) return callback(err);
        callback(null, evtsToDispatch);
      });
    });
  },

  /**
   * Executes the default workflow to handle a command.
   * @param {String}   aggId    The passed aggregate id.
   * @param {Object}   cmd      The passed command.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err, eventsToDispatch){}`
   */
  workflow: function (aggId, cmd, callback) {
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
    if (!callback || !_.isFunction(callback)) {
      var err = new Error('Please pass a valid callback!');
      debug(err);
      throw err;
    }

    var self = this;

    var agg = null;
    var meta = {
      aggregateId: aggId,
      aggregate: this.aggregate ? this.aggregate.name : undefined,
      context: this.aggregate && this.aggregate.context ? this.aggregate.context.name : undefined
    };

    var concatenatedId = this.getConcatenatedId(aggId, cmd);

    var hadNoAggregateId = !dotty.exists(cmd, this.definitions.command.aggregateId);

    async.waterfall([

      // validate command
      function (clb) {
        debug('validate command');
        self.validateCommand(cmd, clb);
      },

//      // check aggregate lock
//      function (clb) {
//        if (hadNoAggregateId) return clb(null);
//        debug('check aggregate lock');
//        self.checkAggregateLock(aggId, clb);
//      },

      // check the pre-load conditions: this is run before the aggregate is locked to allow non-(b)locking checks
      function (clb) {
        debug('check the pre-load conditions');
        self.checkPreLoadConditions(cmd, clb);
      },

      // lock aggregate
      function (clb) {
        if (hadNoAggregateId) return clb(null);
        debug('lock aggregate');
        self.lockAggregate(concatenatedId, clb);
      },

      // load aggregate
      function (clb) {
        debug('load aggregate');
        self.loadAggregate(cmd, aggId, clb);
      },

      // verify aggregate
      function (aggregate, streams, clb) {
        agg = aggregate; // save it temporary so we can use it in the callback

        debug('verify aggregate');
        var err = self.verifyAggregate(aggregate, cmd);
        if (err) {
          return clb(err);
        }
        clb(null, aggregate, streams);
      },

      // handle command and check business rules
      function (aggregate, streams, clb) {
        debug('handle command');
        self.letHandleCommandByAggregate(aggregate, cmd, function (err) { // err is a business rule error
          if (err) {
            return clb(err);
          }
          clb(null, aggregate, streams);
        });
      },

      // check aggregate lock
      function (aggregate, streams, clb) {
        if (hadNoAggregateId) return clb(null, aggregate, streams);
        debug('check aggregate lock');
        self.checkAggregateLock(concatenatedId, function (err) {
          clb(err, aggregate, streams);
        });
      },

      // commit new aggregate events
      function (aggregate, streams, clb) {
        debug('commit new aggregate events');
        self.commit(aggregate, streams, clb);
      }

    ], function (err, eventsToDispatch) {
      if (agg && agg.getRevision() === 0) {
        agg = null;
      }

      if (hadNoAggregateId) {
        if (callback.length > 2) {
          return callback(err, eventsToDispatch || null, agg ? agg.toJSON() : null, meta);
        }

        return callback(err, eventsToDispatch || null);
      }

      // unlock...
      debug('unlock aggregate');

      self.resolveAggregateLock(concatenatedId, function (errLock) {
        if (errLock) {
          debug(errLock);
          return callback(errLock);
        }

        if (err) {
          debug(err);

          if (err instanceof ConcurrencyError) {
            var retryIn = randomBetween(0, self.options.retryOnConcurrencyTimeout); // could be overwritten in a custom commandHandler?
            debug('retry in ' + retryIn + 'ms');
            setTimeout(function() {
              self.workflow(aggId, cmd, callback);
            }, retryIn);
            return;
          }

          if (callback.length > 2) {
            return callback(err, null, agg ? agg.toJSON() : null, meta);
          }

          return callback(err, null);
        }

        if (callback.length > 2) {
          return callback(null, eventsToDispatch || null, agg ? agg.toJSON() : null, meta);
        }

        callback(null, eventsToDispatch || null);
      });
    });
  },

  /**
   * Returns the concatenated id (more unique)
   * @param {String}   aggId The passed aggregate id.
   * @param {Object}   cmd   The passed command.
   * @returns {string}
   */
  getConcatenatedId: function (aggId, cmd) {
    var aggregate = '';
    if (dotty.exists(cmd, this.definitions.command.aggregate)) {
      aggregate = dotty.get(cmd, this.definitions.command.aggregate);
    }

    var context = '';
    if (dotty.exists(cmd, this.definitions.command.context)) {
      context = dotty.get(cmd, this.definitions.command.context);
    }

    return context + aggregate + aggId;
  },

  /**
   * Handles the passed command
   * @param {Object}   cmd      The passed command
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err, evts){}`
   */
  handle: function (cmd, callback) {
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

    var self = this;

    function _handle (aggId) {
      var concatenatedId = self.getConcatenatedId(aggId, cmd);

      var isFirst = !self.getNextCommandInQueue(concatenatedId);

      self.queueCommand(concatenatedId, cmd, callback);

      if (!isFirst) {
        return;
      }

      (function handleNext (aggregateId, c) {
        var concId = self.getConcatenatedId(aggregateId, c);
        var cmdEntry = self.getNextCommandInQueue(concId);
        if (cmdEntry) {
          if (cmdEntry.callback.length > 2) {
            self.workflow(aggregateId, cmdEntry.command, function (err, evts, aggData, meta) {
              self.removeCommandFromQueue(concId, cmdEntry.command);
              handleNext(aggregateId, cmdEntry.command);
              cmdEntry.callback(err, evts, aggData, meta);
            });
            return;
          }
          self.workflow(aggregateId, cmdEntry.command, function (err, evts) {
            self.removeCommandFromQueue(concId, cmdEntry.command);
            handleNext(aggregateId, cmdEntry.command);
            cmdEntry.callback(err, evts);
          });
        }
      })(aggId, cmd);
    }

    if (dotty.exists(cmd, this.definitions.command.aggregateId)) {
      return _handle(dotty.get(cmd, this.definitions.command.aggregateId));
    }

    debug('no aggregateId in command, so generate a new one');

    this.getNewAggregateId(cmd, function (err, id) {
      if (err) {
        debug(err);
        return callback(err);
      }

      return _handle(id);
    });
  },

  /**
   * Inject idGenerator function for aggregate id.
   * @param   {Function} fn           The function to be injected.
   * @returns {DefaultCommandHandler} to be able to chain...
   */
  aggregateIdGenerator: function (fn) {
    if (fn.length === 0) {
      fn = _.wrap(fn, function(func, callback) {
        callback(null, func());
      });
    }

    this.getNewAggregateIdFn = fn;

    return this;
  },

  /**
   * IdGenerator function for aggregate id.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err, newId){}`
   */
  getNewAggregateId: function (cmd, callback) {
    var getNewIdFn = this.eventStore.getNewId.bind(this.eventStore);
    if (this.aggregate && this.aggregate.getNewAggregateId) {
      getNewIdFn = this.aggregate.getNewAggregateId.bind(this.aggregate);
    } else if (this.getNewAggregateIdFn) {
      getNewIdFn = this.getNewAggregateIdFn.bind(this);
    }

    if (getNewIdFn.length === 2) {
      return getNewIdFn(cmd, callback);
    }

    getNewIdFn(callback);
  }

});

module.exports = DefaultCommandHandler;
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
  if (!this.name && meta) {
    this.name = meta.name;
  }

  this.options = {};

  this.definitions = {
    command: {
      id: 'id',
      name: 'name',
      aggregateId: 'aggregate.id'
//      context: 'context.name',        // optional
//      aggregate: 'aggregate.name',    // optional
//      payload: 'payload',             // optional
//      revision: 'revision',           // optional
//      version: 'version',             // optional
//      meta: 'meta'                    // optional (will be passed directly to corresponding event(s))
    },
    event: {
      correlationId: 'correlationId',
      id: 'id',
      name: 'name',
      aggregateId: 'aggregate.id',
//      context: 'context.name',        // optional
//      aggregate: 'aggregate.name',    // optional
      payload: 'payload',               // optional
      revision: 'revision'              // optional
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

## File: `lib/domain.js`
```javascript
var debug = require('debug')('domain'),
  async = require('async'),
  util = require('util'),
  EventEmitter = require('events').EventEmitter,
  _ = require('lodash'),
  eventstore = require('eventstore'),
  aggregatelock = require('./lock'),
  commandBumper = require('./bumper'),
  customLoader = require('./structure/customLoader'),
  structureLoader = require('./structure/structureLoader'),
  attachLookupFunctions = require('./structure/treeExtender'),
  ValidationError = require('./errors/validationError'),
  BusinessRuleError = require('./errors/businessRuleError'),
  AggregateConcurrencyError = require('./errors/aggregateConcurrencyError'),
  AggregateDestroyedError = require('./errors/aggregateDestroyedError'),
  DuplicateCommandError = require('./errors/duplicateCommandError'),
  CommandDispatcher = require('./commandDispatcher'),
  uuid = require('uuid').v4,
  dotty = require('dotty');

function isValidEventStore (obj) {
  // TODO: check each method's signature?
  return !!obj && _.every([
    obj.init, obj.on, obj.getNewId, obj.getFromSnapshot,
    obj.createSnapshot, obj.setEventToDispatched],
    function (o) {
      return _.isFunction(o);
    }
  );
}

function createEventStore (options) {
  if ( _.isFunction(options)) {
    // This is a factory method.
    var eventStore = options();
    if (!isValidEventStore(eventStore)) {
      var err = new Error('"options.eventStore" is not a valid event store factory');
      debug(err);
      throw err;
    }
    return eventStore;
  }
  return eventstore(options);
}

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

function isValidAggregateLock (obj) {
  // TODO: check each method's signature?
  return !!obj && _.every([
    obj.connect, obj.disconnect, obj.on, obj.getNewId,
    obj.reserve, obj.getAll, obj.resolve],
    function (o) {
      return _.isFunction(o);
    }
  );
}

function isValidCommandBumper (obj) {
  // TODO: check each method's signature?
  return !!obj && _.every([
        obj.connect, obj.disconnect, obj.on, obj.getNewId,
        obj.add],
      function (o) {
        return _.isFunction(o);
      }
    );
}

function createAggregateLock (options) {
  if (_.isFunction(options)) {
    // This is a factory method.
    var lock = options();
    if (!isValidAggregateLock(lock)) {
      var err = new Error('"options.aggregateLock" is not a valid aggregate lock factory');
      debug(err);
      throw err;
    }
  }
  return aggregatelock.create(options);
}

function createCommandBumper (options) {
  if (_.isFunction(options)) {
    // This is a factory method.
    var bumper = options();
    if (!isValidCommandBumper(bumper)) {
      var err = new Error('"options.deduplication" is not a valid deduplication store factory');
      debug(err);
      throw err;
    }
  }
  return commandBumper.create(options);
}

/**
 * Domain constructor
 * @param {Object} options The options.
 * @constructor
 */
function Domain(options) {
  EventEmitter.call(this);

  options = options || {};

  if (!options.domainPath) {
    var err = new Error('Please provide domainPath or domainLoader in options');
    debug(err);
    throw err;
  }

  options.retryOnConcurrencyTimeout = options.retryOnConcurrencyTimeout || 800;

  options.commandRejectedEventName = options.commandRejectedEventName || 'commandRejected';

  options.snapshotThreshold = options.snapshotThreshold || 100;

  options.useLoaderExtensions = options.useLoaderExtensions || false;

  this.structureLoader = createStructureLoader(options.structureLoader);

  this.eventStore = createEventStore(options.eventStore);

  this.aggregateLock = createAggregateLock(options.aggregateLock);

  if (options.deduplication) {
    this.commandBumper = createCommandBumper(options.deduplication);
  }

  this.options = options;

  this.definitions = {
    command: {
      id: 'id',
      name: 'name',
      aggregateId: 'aggregate.id'
//      context: 'context.name',        // optional
//      aggregate: 'aggregate.name',    // optional
//      payload: 'payload',             // optional
//      revision: 'revision',           // optional
//      version: 'version',             // optional
//      meta: 'meta'                    // optional (will be passed directly to corresponding event(s))
    },
    event: {
      correlationId: 'correlationId',
      id: 'id',
      name: 'name',
      aggregateId: 'aggregate.id',
//      context: 'context.name',        // optional
//      aggregate: 'aggregate.name',    // optional
      payload: 'payload',               // optional
      revision: 'revision'              // optional
//      version: 'version',             // optional
//      meta: 'meta'                    // optional (will be passed directly from corresponding command)
    }
  };

  this.idGenerator(function () {
    return uuid().toString();
  });

  this.onEvent(function (evt) {
    debug('emit:', evt);
  });

  this.extendValidator(function (validator) {
    debug('no validator extension defined');
  });
}

util.inherits(Domain, EventEmitter);

_.extend(Domain.prototype, {



  /**
   * Inject definition for command structure.
   * @param   {Object} definition the definition to be injected
   * @returns {Domain}            to be able to chain...
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
   * @returns {Domain}            to be able to chain...
   */
  defineEvent: function (definition) {
    if (!definition || !_.isObject(definition)) {
      var err = new Error('Please pass a valid definition!');
      debug(err);
      throw err;
    }

    this.definitions.event = _.defaults(definition, this.definitions.event);

    if (this.definitions.event.commitStamp || this.definitions.event.position) {
      var mappings = {};
      if (this.definitions.event.commitStamp) {
        mappings.commitStamp = this.definitions.event.commitStamp;
      }

      if (this.definitions.event.position) {
        mappings.position = this.definitions.event.position;
      }

      this.eventStore.defineEventMappings(mappings);
    }
    return this;
  },

  /**
   * Inject idGenerator function.
   * @param   {Function}  fn The function to be injected.
   * @returns {Domain}       to be able to chain...
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
   * Inject idGenerator function for aggregate id.
   * @param   {Function}  fn The function to be injected.
   * @returns {Domain}       to be able to chain...
   */
  aggregateIdGenerator: function (fn) {
    if (!fn || !_.isFunction(fn)) {
      var err = new Error('Please pass a valid function!');
      debug(err);
      throw err;
    }

    if (fn.length === 1) {
      this.getNewAggregateId = fn;
      return this;
    }

    this.getNewAggregateId = function (callback) {
      callback(null, fn());
    };

    return this;
  },

  /**
   * Inject custom structure loader function
   * @param   {Function} fn The function to be injected.
   * @returns {Domain}            to be able to chain...
   */
  defineStructureLoader: function (fn) {
    if (!fn || !_.isFunction(fn)) {
      var err = new Error('Please pass a valid function!');
      debug(err);
      throw err;
    }

    this.structureLoader = customLoader(fn);

    return this;
  },


  /**
   * Inject function for for event notification.
   * @param   {Function} fn the function to be injected
   * @returns {Domain}      to be able to chain...
   */
  onEvent: function (fn) {
    if (!fn || !_.isFunction(fn)) {
      var err = new Error('Please pass a valid function!');
      debug(err);
      throw err;
    }

    if (fn.length === 1) {
      fn = _.wrap(fn, function(func, evt, callback) {
        func(evt);
        callback(null);
      });
    }

    this.onEventHandle = fn;

    return this;
  },

  /**
   * Converts an error to the commandRejected event
   * @param {Object} cmd The command that was handled.
   * @param {Error}  err The error that occurs.
   * @returns {Object} The resulting event.
   */
  createCommandRejectedEvent: function (cmd, err) {
    if (!cmd || !_.isObject(cmd)) {
      var err = new Error('Please pass a valid command!');
      debug(err);
      throw err;
    }
    if (!err || !_.isObject(err)) {
      var err = new Error('Please pass a valid error!');
      debug(err);
      throw err;
    }

    var evt = {};

    if (!!this.definitions.command.meta && !!this.definitions.event.meta) {
      dotty.put(evt, this.definitions.event.meta, dotty.get(cmd, this.definitions.command.meta));
    }

    dotty.put(evt, this.definitions.event.correlationId, dotty.get(cmd, this.definitions.command.id));
    dotty.put(evt, this.definitions.event.name, this.options.commandRejectedEventName);
    dotty.put(evt, this.definitions.event.id, dotty.get(cmd, this.definitions.command.id) + '_rejected');
    dotty.put(evt, this.definitions.event.aggregateId, dotty.get(cmd, this.definitions.command.aggregateId));

    if (!!this.definitions.command.aggregate && !!this.definitions.event.aggregate) {
      dotty.put(evt, this.definitions.event.aggregate, dotty.get(cmd, this.definitions.command.aggregate));
    }

    if (!!this.definitions.command.context && !!this.definitions.event.context) {
      dotty.put(evt, this.definitions.event.context, dotty.get(cmd, this.definitions.command.context));
    }

    if (err instanceof ValidationError || err instanceof BusinessRuleError ||
        err instanceof AggregateDestroyedError || err instanceof AggregateConcurrencyError ||
        err instanceof DuplicateCommandError) {
      dotty.put(evt, this.definitions.event.payload, {
        command: cmd,
        reason: {
          name: err.name,
          message: err.message,
          more: err.more
        }
      });

      if (!!this.definitions.event.revision && dotty.get(evt, this.definitions.event.revision) === undefined && err.more && err.more.aggregateRevision > -1) {
        dotty.put(evt, this.definitions.event.revision, err.more.aggregateRevision);
      }
    } else {
      evt = null;
    }

    return evt;
  },

  /**
   * Returns the domain information.
   * @returns {Object}
   */
  getInfo: function () {
    if (!this.tree) {
      var err = new Error('Not initialized!');
      debug(err);
      throw err;
    }

    return this.tree.getInfo();
  },

  /**
   * Extends the validator instance.
   * @param   {Function} fn the function to be injected
   * @returns {Domain}      to be able to chain...
   */
  extendValidator: function (fn) {
    if (!fn || !_.isFunction(fn) || fn.length !== 1) {
      var err = new Error('Please pass a valid function!');
      debug(err);
      throw err;
    }

    this.validatorExtension = fn;

    return this;
  },

  /**
   * Call this function to initialize the domain.
   * @param {Function} callback the function that will be called when this action has finished [optional]
   *                            `function(err, warnings){}`
   */
  init: function (callback) {

    var self = this;

    var warnings = null;


    async.series([
      // load domain files...
      function (callback) {
        debug('load domain files..');
        self.structureLoader(self.options.domainPath, self.validatorExtension, self.options.useLoaderExtensions, function (err, tree, warns) {
          if (err) {
            return callback(err);
          }
          warnings = warns;

          if (!tree || _.isEmpty(tree)) return callback(new Error('No structure loaded for ' + self.options.domainPath + '!'));

          self.tree = attachLookupFunctions(tree);
          callback(null);
        });
      },

      // prepare infrastructure...
      function (callback) {
        debug('prepare infrastructure...');
        async.parallel([

          // prepare eventStore...
          function (callback) {
            debug('prepare eventStore...');

            self.eventStore.on('connect', function () {
              self.emit('connect');
            });

            self.eventStore.on('disconnect', function () {
              self.emit('disconnect');
            });

            self.eventStore.init(callback);
          },

          // prepare aggregateLock...
          function (callback) {
            debug('prepare aggregateLock...');

            self.aggregateLock.on('connect', function () {
              self.emit('connect');
            });

            self.aggregateLock.on('disconnect', function () {
              self.emit('disconnect');
            });

            self.aggregateLock.connect(callback);
          },

          // prepare commandBumper...
          function (callback) {
            if (!self.commandBumper) {
              return callback(null);
            }
            debug('prepare commandBumper...');

            self.commandBumper.on('connect', function () {
              self.emit('connect');
            });

            self.commandBumper.on('disconnect', function () {
              self.emit('disconnect');
            });

            self.commandBumper.connect(callback);
          }
        ], callback);
      },

      // inject all needed dependencies...
      function (callback) {
        debug('inject all needed dependencies...');

        self.commandDispatcher = new CommandDispatcher(self.tree, self.definitions.command, self.commandBumper);
        self.tree.defineOptions({
            retryOnConcurrencyTimeout: self.options.retryOnConcurrencyTimeout,
            snapshotThreshold: self.options.snapshotThreshold,
            snapshotThresholdMs: self.options.snapshotThresholdMs
          })
          .defineCommand(self.definitions.command)
          .defineEvent(self.definitions.event)
          .idGenerator(self.getNewId)
          .useEventStore(self.eventStore)
          .useAggregateLock(self.aggregateLock);

        if (self.getNewAggregateId) {
          self.tree.aggregateIdGenerator(self.getNewAggregateId);
        }

        callback(null);
      }
    ], function (err) {
      if (err) {
        debug(err);
      } else {
        debug('domain inited');
      }
      if (callback) callback(err, warnings);
    });
  },

  /**
   * Is called when dispatched a command.
   * @param {Object}   cmd              the command object
   * @param {Error}    err              the error
   * @param {Array}    eventsToDispatch the events to dispatch
   * @param {Object}   aggregateData    the aggregate data
   * @param {Object}   meta             the meta infos
   * @param {Function} callback         the function that will be called when this action has finished [optional]
   *                                    `function(err, evts, aggregateData, meta){}` evts is of type Array, aggregateData and meta are an object
   */
  onDispatched: function (cmd, err, eventsToDispatch, aggregateData, meta, callback) {
    var self = this;

    if (err) {
      debug(err);
      var cmdRejEvt = this.createCommandRejectedEvent(cmd, err);
      if (cmdRejEvt) {
        this.onEventHandle(cmdRejEvt, function (err) { if (err) { debug(err); } });

        if (callback) {
          try {
            callback(err, [cmdRejEvt], aggregateData || null, meta || null);
          } catch (e) {
            debug(e);
            console.log(e.stack);
            process.emit('uncaughtException', e);
          }
        }
        return;
      }

      if (callback) {
        try {
          callback(err, null, aggregateData, meta);
        } catch (e) {
          debug(e);
          console.log(e.stack);
          process.emit('uncaughtException', e);
        }
      }
      return;
    }

    var evts = [];
    if (!eventsToDispatch || !_.isArray(eventsToDispatch)) {
      debug('seams to be something from a custom command handler');
      if (callback) {
        try {
          callback.apply(callback, _.toArray(arguments));
        } catch (e) {
          debug(e);
          console.log(e.stack);
          process.emit('uncaughtException', e);
        }
      }
      return;
    }

    async.each(eventsToDispatch, function (evt, callback) {
      function setEventToDispatched (e, clb) {
        if (!e.payload || !e.id || e.disablePersistence) {
          evts.push(e.payload || e);
          return callback(null);
        }
        debug('set event to dispatched');
        self.eventStore.setEventToDispatched(e, function (err) {
          if (err) {
            return callback(err);
          }
          evts.push(e.payload);
          clb(null);
        });
      }

      if (self.onEventHandle) {
        debug('publish an event');
        if (evt.payload && evt.id) {
          self.onEventHandle(evt.payload, function (err) {
            if (err) {
              debug(err);
              return callback(err);
            }
            setEventToDispatched(evt, function (err) {
              if (err) {
                return callback(err);
              }
              callback(null);
            });
          });
        } else {
          // seams that custom command handler has done some strange stuff!!!
          self.onEventHandle(evt, function (err) {
            if (err) {
              debug(err);
              return callback(err);
            }
            evts.push(evt);
            callback(null);
          });
        }
      } else {
        setEventToDispatched(evt, callback);
      }
    }, function (err) {
      if (err) {
        debug(err);
      }

      if (callback) {
        try {
          callback(err, evts, aggregateData, meta);
        } catch (e) {
          debug(e);
          console.log(e.stack);
          process.emit('uncaughtException', e);
        }
      }
    });
  },

  /**
   * Call this function to let the domain handle it.
   * @param {Object}   cmd      the command object
   * @param {Function} callback the function that will be called when this action has finished [optional]
   *                            `function(err, evts, aggregateData, meta){}` evts is of type Array, aggregateData and meta are an object
   */
  handle: function (cmd, callback) {
    if (!cmd || !_.isObject(cmd) || !dotty.exists(cmd, this.definitions.command.name)) {
      var err = new Error('Please pass a valid command!');
      debug(err);
      if (callback) callback(err);
      return;
    }

    var self = this;
    process.nextTick(function () {
      try {
        if (callback && callback.length > 2) {
          self.commandDispatcher.dispatch(cmd, function (err, eventsToDispatch, aggregateData, meta) {
            self.onDispatched(cmd, err, eventsToDispatch, aggregateData, meta, callback);
          });
          return;
        }
        self.commandDispatcher.dispatch(cmd, function (err, eventsToDispatch) {
          self.onDispatched(cmd, err, eventsToDispatch, null, null, callback);
        });
      } catch (e) {
        if (callback)
          callback(e);
      }
    });
  }

});

module.exports = Domain;
```

## File: `lib/validator.js`
```javascript
var debug = require('debug')('domain:validator'),
  _ = require('lodash'),
  tv4Module = require('tv4'),
  ValidationError = require('./errors/validationError');

/**
 * Returns a validator function.
 * @param {Object} options The options object.
 * @param {Object} schema  The schema object.
 * @returns {Function}
 */
function getValidator (options, schema) {
  options = options || {};
  options.schemas = options.schemas || {};
  options.formats = options.formats || {};

  if (!schema || !_.isObject(schema)) {
    var err = new Error('Please pass a valid schema!');
    debug(err);
    throw err;
  }

  var tv4 = tv4Module.freshApi();

  _.each(options.schemas, function (v, k) {
    tv4.addSchema(k, v);
  });

  tv4.addFormat(options.formats);

  return function (data) {
    var validation = tv4.validateMultiple(data, schema);

    if (validation.missing.length > 0) {
      var missingString = validation.missing[0];

      for (var m = 1, lenM = validation.missing.length; m < lenM; m++) {
        missingString += ', ' + validation.missing[m];
      }

      var err = new Error('Validation schema(s) "' + missingString + '" missing!');
      debug(err);
      return err;
    }

    if (!validation.valid) {
      var errors = validation.errors.map(function (error) {
        if (error.message.indexOf('not match any schemas') >= 0 && error.subErrors && error.subErrors.length > 0) {
          return error.subErrors[0];
        } else {
          return error;
        }
      });
      var firstError = errors[0];

      return new ValidationError(firstError.dataPath + ' => ' + firstError.message, errors);
    }

    return null;
  };
}

module.exports = getValidator;
```

## File: `lib/bumper/base.js`
```javascript
var util = require('util'),
  EventEmitter = require('events').EventEmitter,
  prequire = require('parent-require'),
  _ = require('lodash'),
  uuid = require('uuid').v4;

/**
 * Bumper constructor
 * @param {Object} options The options can have information like host, port, etc. [optional]
 */
function Bumper(options) {
  options = options || {};

  EventEmitter.call(this);
}

util.inherits(Bumper, EventEmitter);

function implementError (callback) {
  var err = new Error('Please implement this function!');
  if (callback) callback(err);
  throw err;
}

_.extend(Bumper.prototype, {

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
   * Use this function to add a key with expiration.
   * @param  {String}   key      The key
   * @param  {Number}   ttl      The time to live in ms
   * @param  {Function} callback The function, that will be called when this action is completed. [optional]
   *                             `function(err, added){}`
   */
  add: function (key, ttl, callback) {
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

Bumper.use = function (toRequire) {
  var required;
  try {
    required = require(toRequire);
  } catch (e) {
    // workaround when `npm link`'ed for development
    required = prequire(toRequire);
  }
  return required;
};

module.exports = Bumper;
```

## File: `lib/bumper/index.js`
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
  Bumper: Base,

  create: function(options, callback) {
    if (typeof options === 'function') {
      callback = options;
      options = {};
    }

    options = options || {};

    var Bumper;

    try {
      Bumper = getSpecificDbImplementation(options);
    } catch (err) {
      if (callback) callback(err);
      throw err;
    }

    var bumper = new Bumper(options);
    if (callback) {
      process.nextTick(function () {
        tolerate(function (callback) {
          bumper.connect(callback);
        }, options.timeout || 0, callback || function () {
        });
      });
    }
    return bumper;
  }
};
```

## File: `lib/bumper/databases/inmemory.js`
```javascript
var util = require('util'),
  Bumper = require('../base'),
  _ = require('lodash');

function InMemory(options) {
  Bumper.call(this, options);
  this.store = [];
  this.options = options;
  this.options.ttl = 1000 * 60 * 60 * 1; // 1 hour
}

util.inherits(InMemory, Bumper);

_.extend(InMemory.prototype, {

  connect: function (callback) {
    this.emit('connect');
    if (callback) callback(null, this);
  },

  disconnect: function (callback) {
    this.emit('disconnect');
    if (callback) callback(null);
  },

  add: function(key, ttl, callback) {
    if (!callback) {
      callback = ttl;
      ttl = this.options.ttl;
    }

    if (this.store.indexOf(key) >= 0) {
      return callback(null, false);
    }

    this.store.push(key);

    var self = this;
    setTimeout(function () {
      self.store = _.remove(self.store, key);
    }, ttl);

    if (callback) callback(null, true);
  },

  clear: function (callback) {
    this.store = [];
    if (callback) callback(null);
  }

});

module.exports = InMemory;
```

## File: `lib/bumper/databases/mongodb.js`
```javascript
var util = require('util'),
  Bumper = require('../base'),
  _ = require('lodash'),
  mongo = Bumper.use('mongodb'),
  mongoVersion = Bumper.use('mongodb/package.json').version,
  isNew = mongoVersion.indexOf('1.') !== 0,
  ObjectID = isNew ? mongo.ObjectID : mongo.BSONPure.ObjectID;

function Mongo(options) {
  Bumper.call(this, options);

  var defaults = {
    host: 'localhost',
    port: 27017,
    dbName: 'domain',
    collectionName: 'commandbumper',
    // heartbeat: 60 * 1000
    ttl:  1000 * 60 * 60 * 1 // 1 hour
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

util.inherits(Mongo, Bumper);

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
        self.bumper = self.db.collection(options.collectionName);
        self.bumper.ensureIndex({ expires: 1 }, { expireAfterSeconds: 0 }, function() {});
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

  add: function(key, ttl, callback) {
    if (!callback) {
      callback = ttl;
      ttl = this.options.ttl;
    }

    var self = this;
    var exp = new Date(Date.now() + ttl);
    this.bumper.insert({ _id: key, expires: exp }, { safe: true }, function(err) {
      if (err && err.message && err.message.indexOf('duplicate key') >= 0) {
        return callback(null, false);
      }
      if (err) {
        return callback(err);
      }

      // mongodb is not so fast in removing expired documents
      setTimeout(function () {
        self.bumper.remove({ _id: key }, { safe: true }, function () {});
      }, ttl);

      return callback(null, true);
    });
  },

  clear: function (callback) {
    this.bumper.remove({}, { safe: true }, callback);
  }

});

module.exports = Mongo;
```

## File: `lib/bumper/databases/redis.js`
```javascript
var util = require('util'),
  Bumper = require('../base'),
  _ = require('lodash'),
  async = require('async'),
  redis = Bumper.use('redis');

function Redis(options) {
  Bumper.call(this, options);

  var defaults = {
    host: 'localhost',
    port: 6379,
    prefix: 'commandbumper',
    retry_strategy: function (options) {
      return undefined;
    },
    ttl:  1000 * 60 * 60 * 1 // 1 hour,
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

util.inherits(Redis, Bumper);

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

  add: function(key, ttl, callback) {
    if (!callback) {
      callback = ttl;
      ttl = this.options.ttl;
    }

    var self = this;
    ttl = Math.round(ttl / 1000);
    if (ttl < 1) {
      ttl = 1;
    }
    this.client.setnx(self.options.prefix + ':' + key, ttl, function (err, res) {
      if (err) {
        return callback(err);
      }

      if (!res) {
        return callback(null, false);
      }

      self.client.expire(self.options.prefix + ':' + key, ttl, function (err) {
        if (err) {
          return callback(err);
        }

        callback(null, true);
      });
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
      if (callback) callback(err);
    });
  }

});

module.exports = Redis;
```

## File: `lib/bumper/databases/tingodb.js`
```javascript
var util = require('util'),
  Bumper = require('../base'),
  _ = require('lodash'),
  tingodb = Bumper.use('tingodb')(),
  ObjectID = tingodb.ObjectID;

function Tingo(options) {
  Bumper.call(this, options);

  var defaults = {
    dbPath: require('path').join(__dirname, '/../../../'),
    collectionName: 'commandbumper',
    ttl:  1000 * 60 * 60 * 1 // 1 hour'
  };

  _.defaults(options, defaults);

  this.options = options;
}

util.inherits(Tingo, Bumper);

_.extend(Tingo.prototype, {

  connect: function (callback) {
    var self = this;

    var options = this.options;

    this.db = new tingodb.Db(options.dbPath, {});
    // this.db.on('close', function() {
    //   self.emit('disconnect');
    // });
    this.bumper = this.db.collection(options.collectionName + '.tingo');
    this.bumper.ensureIndex({ expires: 1 }, { expireAfterSeconds: 0 }, function() {});

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

  add: function(key, ttl, callback) {
    if (!callback) {
      callback = ttl;
      ttl = this.options.ttl;
    }

    var self = this;
    var exp = new Date(Date.now() + ttl);
    this.bumper.insert({ _id: key, expires: exp }, { safe: true }, function(err) {
      if (err && err.message && err.message.indexOf('duplicate key') >= 0) {
        return callback(null, false);
      }
      if (err) {
        return callback(err);
      }

      // tingodb is not so fast in removing expired documents
      setTimeout(function () {
        self.bumper.remove({ _id: key }, { safe: true }, function () {});
      }, ttl);

      return callback(null, true);
    });
  },

  clear: function (callback) {
    this.bumper.remove({}, { safe: true }, callback);
  }

});

module.exports = Tingo;
```

## File: `lib/definitions/aggregate.js`
```javascript
var Definition = require('../definitionBase'),
  util = require('util'),
  _ = require('lodash'),
  debug = require('debug')('domain:aggregate'),
  AggregateModel = require('../aggregateModel'),
  dotty = require('dotty'),
  DefaultCommandHandler = require('../defaultCommandHandler'),
  uuid = require('uuid').v4,
  async = require('async');

/**
 * Aggregate constructor
 * @param {Object} meta            Meta infos like: { name: 'name', version: 1 }
 * @param {Object} modelInitValues Initialization values for model like: { emails: [] } [optional]
 * @constructor
 */
function Aggregate (meta, modelInitValues) {
  Definition.call(this, meta);

  meta = meta || {};

  this.version = meta.version || 0;

  this.defaultCommandPayload = meta.defaultCommandPayload || '';
  this.defaultEventPayload = meta.defaultEventPayload || '';
  this.defaultPreConditionPayload = meta.defaultPreConditionPayload || '';
  this.defaultPreLoadConditionPayload = meta.defaultPreLoadConditionPayload || '';
  this.skipHistory = meta.skipHistory || false;
  this.applyLastEvent = meta.applyLastEvent || false;
  this.disablePersistence = meta.disablePersistence || false;

  this.commands = [];
  this.events = [];
  this.businessRules = [];
  this.commandHandlers = [];

  this.loadingEventTransformers = [];
  this.committingEventTransformers = [];

  this.snapshotConversions = {};
  this.snapshotIgnores = {};

  this.loadingSnapshotTransformers = {};
  this.committingSnapshotTransformers = {};

  this.idGenerator(function () {
    return uuid().toString();
  });

  this.modelInitValues = modelInitValues || {};

  this.defaultCommandHandler = new DefaultCommandHandler(this);
  this.defaultCommandHandler.useAggregate(this);

  this.snapshotConversionRegistrations = [];

  this.loadingSnapshotTransformerRegistrations = [];
  this.committingSnapshotTransformerRegistrations = [];
}

util.inherits(Aggregate, Definition);

/**
 * Returns the apply function for the AggregateModel.
 * @param {Aggregate}      aggregate      The aggregate object.
 * @param {AggregateModel} aggregateModel The aggregateModel object.
 * @param {Command}        cmd            The command object that caused this.
 * @returns {Function}
 */
function applyHelper (aggregate, aggregateModel, cmd) {
  return function (name, payload, version) {
    aggregateModel.set = function () {
      AggregateModel.prototype.set.apply(aggregateModel, _.toArray(arguments));
    };

    var evt;

    if (!payload) {
      if (_.isString(name)) {
        evt = {};
        dotty.put(evt, aggregate.definitions.event.name, name);
      } else if (_.isObject(name)) {
        evt = name;
      }
    } else {
      evt = {};
      dotty.put(evt, aggregate.definitions.event.name, name);
      dotty.put(evt, aggregate.definitions.event.payload, payload);
    }

    if (!!aggregate.definitions.event.meta && !!aggregate.definitions.command.meta) {
      var commandMeta = dotty.get(cmd, aggregate.definitions.command.meta);
      var userAddedMeta = dotty.get(evt, aggregate.definitions.event.meta);
      var meta = (commandMeta || userAddedMeta) && _.extend({}, commandMeta, userAddedMeta);
      dotty.put(evt, aggregate.definitions.event.meta, meta);
    }

    dotty.put(evt, aggregate.definitions.event.aggregateId, aggregateModel.id);
    dotty.put(evt, aggregate.definitions.event.correlationId, dotty.get(cmd, aggregate.definitions.command.id));

    if (!!aggregate.definitions.event.version) {
      if (_.isNumber(version)) {
        dotty.put(evt, aggregate.definitions.event.version, version);
      }

      if (!dotty.exists(evt, aggregate.definitions.event.version)) {
        // if version is not defined in event, search the latest version number...
        var evtName = dotty.get(evt, aggregate.definitions.event.name);
        var maxVersion = _.reduce(aggregate.getEvents(), function (res, e) {
          if (e.name !== evtName) {
            return res;
          }

          var v = e.version || 0;
          if (v > res) {
            return v;
          }
          return res;
        }, 0);
        dotty.put(evt, aggregate.definitions.event.version, maxVersion);
      }
    }

    var aggName, ctxName;

    if (!!aggregate.definitions.event.aggregate && !!aggregate.definitions.command.aggregate) {
      aggName = dotty.get(cmd, aggregate.definitions.command.aggregate) || aggregate.name;
      dotty.put(evt, aggregate.definitions.event.aggregate, aggName);
    }

    if (!!aggregate.definitions.event.context && !!aggregate.definitions.command.context) {
      ctxName = dotty.get(cmd, aggregate.definitions.command.context) || aggregate.context.name;
      dotty.put(evt, aggregate.definitions.event.context, ctxName);
    }

    var aggregateId;

    if (!!aggregate.definitions.event.aggregateId) {
      aggregateId = dotty.get(evt, aggregate.definitions.event.aggregateId);
    }

    var streamInfo = {
      context: ctxName,// || aggregate.context.name,
      aggregate: aggName,// || aggregate.name,
      aggregateId: aggregateId || aggregateModel.id
    };
    if (!aggregate.disablePersistence) {
      var revision = aggregateModel.getRevision(streamInfo) + 1;
      aggregateModel.setRevision(streamInfo, revision);
      dotty.put(evt, aggregate.definitions.event.revision, revision);
    }

    aggregateModel.addUncommittedEvent(evt);

    // apply the event
    debug('apply the event');
    aggregate.apply(_.cloneDeep(evt), aggregateModel);

    aggregateModel.set = function () {
      throw new Error('You are not allowed to set a value in this step!');
    };
  };

}

_.extend(Aggregate.prototype, {

  /**
   * Inject idGenerator function.
   * @param   {Function}  fn The function to be injected.
   * @returns {Aggregate}    to be able to chain...
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
   * Inject the context module.
   * @param {Context} context The context module to be injected.
   */
  defineContext: function (context) {
    if (!context || !_.isObject(context)) {
      var err = new Error('Please inject a valid context object!');
      debug(err);
      throw err;
    }

    this.context = context;

    for (var r in this.snapshotConversionRegistrations) {
      var reg = this.snapshotConversionRegistrations[r];
      var meta = reg.meta;
      var fn = reg.fn;

      meta.context = meta.context || this.context.name;
      meta.aggregate = meta.aggregate || this.name;

      this.snapshotConversions[meta.context + '.' + meta.aggregate + '.' + meta.version] = fn;
    }

    for (var r in this.loadingSnapshotTransformerRegistrations) {
      var reg = this.loadingSnapshotTransformerRegistrations[r];
      var meta = reg.meta;
      var fn = reg.fn;

      meta.context = meta.context || this.context.name;
      meta.aggregate = meta.aggregate || this.name;

      this.loadingSnapshotTransformers[meta.context + '.' + meta.aggregate + '.' + meta.version] = fn;
    }

    for (var r in this.committingSnapshotTransformerRegistrations) {
      var reg = this.committingSnapshotTransformerRegistrations[r];
      var meta = reg.meta;
      var fn = reg.fn;

      meta.context = meta.context || this.context.name;
      meta.aggregate = meta.aggregate || this.name;

      this.committingSnapshotTransformers[meta.context + '.' + meta.aggregate + '.' + meta.version] = fn;
    }
  },

  /**
   * Add command module.
   * @param {Command} command The command module to be injected.
   */
  addCommand: function (command) {
    if (!command || !_.isObject(command)) {
      var err = new Error('Please inject a valid command object!');
      debug(err);
      throw err;
    }

    if (!command.payload && command.payload !== '') {
      command.payload = this.defaultCommandPayload;
    }

    command.defineAggregate(this);

    if (this.commands.indexOf(command) < 0) {
      this.commands.push(command);
    }
  },

  /**
   * Add event module.
   * @param {Event} event The event module to be injected.
   */
  addEvent: function (event) {
    if (!event || !_.isObject(event)) {
      var err = new Error('Please inject a valid event object!');
      debug(err);
      throw err;
    }

    if (!event.payload && event.payload !== '') {
      event.payload = this.defaultEventPayload;
    }

    if (this.events.indexOf(event) < 0) {
      this.events.push(event);
    }
  },

  /**
   * Add businessRule module.
   * @param {BusinessRule} businessRule The businessRule module to be injected.
   */
  addBusinessRule: function (businessRule) {
    if (!businessRule || !_.isObject(businessRule)) {
      var err = new Error('Please inject a valid businessRule object!');
      debug(err);
      throw err;
    }

    if (this.businessRules.indexOf(businessRule) < 0) {
      businessRule.defineAggregate(this);
      this.businessRules.push(businessRule);
      this.businessRules = _.sortBy(this.businessRules, function(br) {
        return br.priority;
      });
    }
  },

  /**
   * Add loadingEventTransformer module.
   * @param {LoadingEventTransformer} loadingEventTransformer The loadingEventTransformer module to be injected.
   */
  addLoadingEventTransformer: function (loadingEventTransformer) {
    if (!loadingEventTransformer || !_.isObject(loadingEventTransformer)) {
      var err = new Error('Please inject a valid loadingEventTransformer object!');
      debug(err);
      throw err;
    }

    if (this.loadingEventTransformers.indexOf(loadingEventTransformer) < 0) {
      this.loadingEventTransformers.push(loadingEventTransformer);
    }
  },

  /**
   * Add committingEventTransformer module.
   * @param {CommittingEventTransformer} committingEventTransformer The committingEventTransformer module to be injected.
   */
  addCommittingEventTransformer: function (committingEventTransformer) {
    if (!committingEventTransformer || !_.isObject(committingEventTransformer)) {
      var err = new Error('Please inject a valid committingEventTransformer object!');
      debug(err);
      throw err;
    }

    if (this.committingEventTransformers.indexOf(committingEventTransformer) < 0) {
      this.committingEventTransformers.push(committingEventTransformer);
    }
  },

  /**
   * Add commandHandler module.
   * @param {CommandHandler} commandHandler The commandHandler module to be injected.
   */
  addCommandHandler: function (commandHandler) {
    if (!commandHandler || !_.isObject(commandHandler) || !_.isFunction(commandHandler.useAggregate)) {
      var err = new Error('Please inject a valid commandHandler object!');
      debug(err);
      throw err;
    }

    commandHandler.useAggregate(this);

    if (this.commandHandlers.indexOf(commandHandler) < 0) {
      this.commandHandlers.push(commandHandler);
    }
  },

  /**
   * Returns the command modules by command name.
   * @param {String} name The command name.
   * @returns {Array}
   */
  getCommandsByName: function (name) {
    if (!name || !_.isString(name)) {
      var err = new Error('Please pass a valid string as name!');
      debug(err);
      throw err;
    }

    return _.filter(this.commands, function (cmd) {
      return cmd.name === name;
    });
  },

  /**
   * Returns the command module by command name and command version.
   * @param {String} name    The command name.
   * @param {Number} version The command version. [optional; default 0]
   * @returns {Command}
   */
  getCommand: function (name, version) {
    if (!name || !_.isString(name)) {
      var err = new Error('Please pass a valid string as name!');
      debug(err);
      throw err;
    }

    version = version || 0;

    if (!_.isNumber(version)) {
      var err = new Error('Please pass a valid number as version!');
      debug(err);
      throw err;
    }

    return _.find(this.commands, function (cmd) {
      return cmd.name === name && cmd.version === version;
    });
  },

  /**
   * Returns all command modules.
   * @returns {Array}
   */
  getCommands: function () {
    return this.commands;
  },

  /**
   * Returns the event module by event name and event version.
   * @param {String} name    The event name.
   * @param {Number} version The event version. [optional; default 0]
   * @returns {Event}
   */
  getEvent: function (name, version) {
    if (!name || !_.isString(name)) {
      var err = new Error('Please pass a valid string as name!');
      debug(err);
      throw err;
    }

    version = version || 0;

    if (!_.isNumber(version)) {
      var err = new Error('Please pass a valid number as version!');
      debug(err);
      throw err;
    }

    return _.find(this.events, function (evt) {
      return evt.name === name && evt.version === version;
    });
  },

  /**
   * Returns all event modules.
   * @returns {Array}
   */
  getEvents: function () {
    return this.events;
  },

  /**
   * Returns all business rule modules.
   * @returns {Array}
   */
  getBusinessRules: function () {
    return this.businessRules;
  },

  /**
   * Returns all commandHandler modules.
   * @returns {Array}
   */
  getCommandHandlers: function () {
    return this.commandHandlers;
  },

  /**
   * Returns the commandHandler module by command name and command version.
   * @param {String} name    The command name.
   * @param {Number} version The command version. [optional; default 0]
   * @returns {CommandHandler}
   */
  getCommandHandler: function (name, version) {
    if (!name || !_.isString(name)) {
      var err = new Error('Please pass a valid string as name!');
      debug(err);
      throw err;
    }

    version = version || 0;

    if (!_.isNumber(version)) {
      var err = new Error('Please pass a valid number as version!');
      debug(err);
      throw err;
    }

    var handler =  _.find(this.commandHandlers, function (cmdHnd) {
      return cmdHnd.name === name && cmdHnd.version === version;
    });

    if (handler) {
      return handler;
    }

    if (!this.getCommand(name, version)) {
      return null;
    }

    return this.defaultCommandHandler;
  },

  /**
   * Returns the loadingEventTransformer module by event name and event version.
   * @param {String} name    The event name.
   * @param {Number} version The event version. [optional; default 0]
   * @returns {Event}
   */
  getLoadingEventTransformer: function (name, version) {
    if (!name || !_.isString(name)) {
      var err = new Error('Please pass a valid string as name!');
      debug(err);
      throw err;
    }

    version = version || 0;

    if (!_.isNumber(version)) {
      var err = new Error('Please pass a valid number as version!');
      debug(err);
      throw err;
    }

    var found = _.find(this.loadingEventTransformers, function (evt) {
      return evt.name === name && evt.version === version;
    });

    if (found) return found;

    return _.find(this.loadingEventTransformers, function (evt) {
      return evt.name === name && (evt.version === null || evt.version === undefined);
    });
  },

  /**
   * Returns the committingEventTransformer module by event name and event version.
   * @param {String} name    The event name.
   * @param {Number} version The event version. [optional; default 0]
   * @returns {Event}
   */
  getCommittingEventTransformer: function (name, version) {
    if (!name || !_.isString(name)) {
      var err = new Error('Please pass a valid string as name!');
      debug(err);
      throw err;
    }

    version = version || 0;

    if (!_.isNumber(version)) {
      var err = new Error('Please pass a valid number as version!');
      debug(err);
      throw err;
    }

    var found = _.find(this.committingEventTransformers, function (evt) {
      return evt.name === name && evt.version === version;
    });

    if (found) return found;

    return _.find(this.committingEventTransformers, function (evt) {
      return evt.name === name && (evt.version === null || evt.version === undefined);
    });
  },

  /**
   * Returns a new aggregate model, to be used in the command and event functions.
   * @param {String} id The aggregate id.
   * @returns {AggregateModel}
   */
  create: function (id) {
    if (!id || !_.isString(id)) {
      var err = new Error('Please pass a valid string as id!');
      debug(err);
      throw err;
    }

    return new AggregateModel(id, this.modelInitValues);
  },

  /**
   * Validates the requested command.
   * @param {Object} cmd The command object
   * @returns {ValidationError}
   */
  validateCommand: function (cmd, callback) {
    var cmdName = dotty.get(cmd, this.definitions.command.name);

    var err;
    if (!cmdName) {
      err = new Error('command has no command name in ' + this.definitions.command.name);
      debug(err);
      return callback(err);
    }

    var version = 0;
    if (!!this.definitions.command.version) {
      version = dotty.get(cmd, this.definitions.command.version);
    }

    var command = this.getCommand(cmdName, version);
    if (!command) {
      err = new Error('Command "' + cmdName + '" not found!');
      debug(err);
      return callback(err);
    }

    if (command.validate.length >= 2) {
      return command.validate(cmd, callback);
    }

    try {
      callback(command.validate(cmd));
    } catch (e) {
      callback(e);
    }
  },
  /**
   * Checks for pre-load-conditions. This check will be done BEFORE the aggregate is locked and loaded.
   * @param {Object}         cmd            The command that was handled.
   * @param {Function}       callback       The function, that will be called when this action is completed.
   *                                        `function(err){}`
   */
  checkPreLoadConditions: function (cmd, callback) {
    var cmdName = dotty.get(cmd, this.definitions.command.name);

    if (!cmdName) {
      var err = new Error('command has no command name in ' + this.definitions.command.name);
      debug(err);
      throw err;
    }

    var version = 0;
    if (!!this.definitions.command.version) {
      version = dotty.get(cmd, this.definitions.command.version);
    }

    var command = this.getCommand(cmdName, version);
    if (!command) {
      var err = new Error('Command "' + cmdName + '" not found!');
      debug(err);
      throw err;
    }

    command.checkPreLoadConditions(cmd, callback);
  },

  /**
   * Checks for pre-conditions.
   * @param {Object}         cmd            The command that was handled.
   * @param {AggregateModel} aggregateModel The aggregate values.
   * @param {Function}       callback       The function, that will be called when this action is completed.
   *                                        `function(err){}`
   */
  checkPreConditions: function (cmd, aggregateModel, callback) {
    var cmdName = dotty.get(cmd, this.definitions.command.name);

    if (!cmdName) {
      var err = new Error('command has no command name in ' + this.definitions.command.name);
      debug(err);
      throw err;
    }

    var version = 0;
    if (!!this.definitions.command.version) {
      version = dotty.get(cmd, this.definitions.command.version);
    }

    var command = this.getCommand(cmdName, version);
    if (!command) {
      var err = new Error('Command "' + cmdName + '" not found!');
      debug(err);
      throw err;
    }

    command.checkPreConditions(cmd, aggregateModel, callback);
  },

  /**
   * Checks business rules.
   * @param {Object}   changed  The new aggregate values.
   * @param {Object}   previous The previous aggregate values.
   * @param {Array}    events   All new generated events.
   * @param {Object}   command  The command that was handled.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err){}`
   */
  checkBusinessRules: function (changed, previous, events, command, callback) {
    async.eachSeries(this.getBusinessRules(), function (rule, callback) {
      rule.check(changed, previous, events, command, callback);
    }, callback);
  },

  /**
   * Get infos to load correct stream.
   * @param {Object} cmd The command object.
   * @returns {Array}
   */
  getLoadInfo: function (cmd) {
    var cmdName = dotty.get(cmd, this.definitions.command.name);

    if (!cmdName) {
      var err = new Error('command has no command name in ' + this.definitions.command.name);
      debug(err);
      throw err;
    }

    var version = 0;
    if (!!this.definitions.command.version) {
      version = dotty.get(cmd, this.definitions.command.version);
    }

    var command = this.getCommand(cmdName, version);
    if (!command) {
      var aggregateId = dotty.get(cmd, this.definitions.command.aggregateId);
      var aggregateName = this.name;
      var contextName = this.context.name;

      return [{
        context: contextName,
        aggregate: aggregateName,
        aggregateId: aggregateId
      }];
    }

    return command.getLoadInfo(cmd);
  },

  /**
   * Handles the passed command and checks the business rules.
   * @param {AggregateModel}  aggregateModel The aggregateModel that should be used.
   * @param {Object}          cmd            The command that was handled.
   * @param {Function}        callback       The function, that will be called when this action is completed.
   *                                         `function(err){}`
   */
  handle: function (aggregateModel, cmd, callback) {
    var cmdName = dotty.get(cmd, this.definitions.command.name);
    if (!cmdName) {
      var err = new Error('command has no command name in ' + this.definitions.command.name);
      debug(err);
      return callback(err);
    }

    var version = 0;
    if (!!this.definitions.command.version) {
      version = dotty.get(cmd, this.definitions.command.version);
    }

    var command = this.getCommand(cmdName, version);
    if (!command) {
      var err = new Error('Command "' + cmdName + '" not found!');
      debug(err);
      return callback(err);
    }

    var self = this;

    aggregateModel.set = function () {
      throw new Error('You are not allowed to set a value in this step!');
    };

    var previousModel = new AggregateModel(aggregateModel.id, aggregateModel);

    this.checkPreConditions(cmd, aggregateModel, function (err) {
      if (err) {
        return callback(err);
      }

      // attach apply function
      aggregateModel.apply = applyHelper(self, aggregateModel, cmd);

      debug('handle command');
      try {
        command.handle(cmd, aggregateModel);
      } catch (e) {
        return callback(e);
      }

      // remove apply function
      delete aggregateModel.apply;

      var uncommittedEvents = aggregateModel.getUncommittedEvents();

      async.each(uncommittedEvents, function (evt, callback) {
        var isEvtIdDefined = !!dotty.get(evt, self.definitions.event.id);
        if (isEvtIdDefined) {
          debug('event id already defined');
          return callback(null);
        }

        // generate new id for event
        debug('generate new id for event');
        self.getNewId(function (err, id) {
          if (err) {
            return callback(err);
          }

          dotty.put(evt, self.definitions.event.id, id);
          callback(null);
        });
      }, function (err) {
        if (err) {
          return callback(err);
        }

        // check business rules
        debug('check business rules');
        self.checkBusinessRules(aggregateModel, previousModel, uncommittedEvents, cmd, function (err) {
          if (!err) {
            return callback(null);
          }

          // clean up...
          aggregateModel.reset(previousModel);
          aggregateModel.clearUncommittedEvents();
          callback(err);
        });
      });
    });
  },

  /**
   * Applies the passed events to the passed aggregateModel.
   * @param {Array || Object} events         The events that should be applied.
   * @param {AggregateModel}  aggregateModel The aggregateModel that should be used.
   * @param {boolean}         notSameOrigin  If true it's an indication to not throw if event handler not found.
   */
  apply: function (events, aggregateModel, notSameOrigin) {
    if (!events) {
      return;
    }

    if (!_.isArray(events)) {
      events = [events];
    }

    var self = this;

    events.forEach(function (evt) {
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

      var event = self.getEvent(evtName, version);

      if (!event) {
        if (notSameOrigin) {
          debug('You don\'t want to handle event "' + evtName + '" of other event stream');
          return;
        }
        var err = new Error('Event "' + evtName + '" not found!');
        debug(err);
        throw err;
      }

      event.apply(evt, aggregateModel);
    });
  },

  /**
   * Loads the aggregateModel with the data of the snapshot and the events.
   * And returns true if a new snapshot should be done.
   * @param {AggregateModel}  aggregateModel The aggregateModel that should be used.
   * @param {Object}          snapshot       The snapshot object.
   * @param {Array}           events         The events that should be applied.
   * @param {Number}          loadingTime    The loading time in ms of the eventstore data.
   * @param {Object}          stream         The eventstream.
   * @param {Array}           streams        All loaded eventstreams for this aggregate.
   * @param {boolean}         notSameOrigin  If true it's an indication to not throw if event handler not found.
   * @returns {boolean}
   */
  loadFromHistory: function (aggregateModel, snapshot, events, loadingTime, stream, streams, notSameOrigin) {
    var self = this;

    var isSnapshotNeeded = false;

    if (snapshot) {
      // load snapshot
      debug('load snapshot ' + snapshot.id + ' from history', _.pick(snapshot, ['context', 'aggregate', 'version']), {
        context: this.context.name,
        aggregate: this.name,
        version: this.version
      });
      if ((snapshot.context === this.context.name || !snapshot.context && this.context.name === '_general') &&
          (snapshot.aggregate === this.name || !snapshot.aggregate) &&
          snapshot.version === this.version) {
        aggregateModel.set(snapshot.data);
      } else {
        if (!this.snapshotConversions[snapshot.context + '.' + snapshot.aggregate + '.' + snapshot.version]) {
          var err = new Error('No snapshot conversion defined!');
          debug(err);
          throw err;
        }
        debug('convert snapshot from history');
        this.snapshotConversions[snapshot.context + '.' + snapshot.aggregate + '.' + snapshot.version](snapshot.data, aggregateModel);
        isSnapshotNeeded = true;
      }
      aggregateModel.setRevision({
        context: stream.context,
        aggregate: stream.aggregate,
        aggregateId: stream.aggregateId
      }, snapshot.revision + 1);
    }

    if (events && events.length > 0) {
      // load events
      debug('load events from history');
      var maxRevision = _.reduce(events, function (res, evt) {
        var rev = dotty.get(evt, self.definitions.event.revision);
        if (rev > res) {
          return rev;
        }
        return res;
      }, 0);

      if (!this.skipHistory || (this.skipHistory && this.applyLastEvent)) {
        this.apply(events, aggregateModel, notSameOrigin);
      }

      aggregateModel.setRevision({
        context: stream.context,
        aggregate: stream.aggregate,
        aggregateId: stream.aggregateId
      }, maxRevision);

      if (!isSnapshotNeeded) {
        if (this.isSnapshotNeeded.length > 2) {
          isSnapshotNeeded = this.isSnapshotNeeded(loadingTime, events, aggregateModel.toJSON(), streams);
        } else {
          isSnapshotNeeded = this.isSnapshotNeeded(loadingTime, events);
        }
      }
    }

    return isSnapshotNeeded;
  },

  /**
   * Defines a new loading transform function for snapshot.
   * @param {Object}   meta Meta infos like: { version: 10 }
   * @param {Function} fn   Function containing the transform function
   *                        `function(snapshotData, callback){}`
   * @returns {Aggregate}
   */
  defineLoadingSnapshotTransformer: function (meta, fn) {
    if (!_.isObject(meta) || meta.version === undefined || meta.version === null || !_.isNumber(meta.version)) {
      throw new Error('Please pass in a version');
    }
    if (!_.isFunction(fn)) {
      throw new Error('Please pass in a function');
    }

    var wrappedFn;
    if (fn.length === 1) {
      wrappedFn = function (s, cb) {
        try {
          cb(null, fn(s));
        } catch (err) {
          cb(err);
        }
      };
    } else {
      wrappedFn = fn;
    }

    this.loadingSnapshotTransformerRegistrations.push({ meta: meta, fn: wrappedFn });
    return this;
  },

  /**
   * Defines a new committing transform function for snapshot.
   * @param {Object}   meta Meta infos like: { version: 10 }
   * @param {Function} fn   Function containing the transform function
   *                        `function(snapshotData, callback){}`
   * @returns {Aggregate}
   */
  defineCommittingSnapshotTransformer: function (meta, fn) {
    if (!_.isObject(meta) || meta.version === undefined || meta.version === null || !_.isNumber(meta.version)) {
      throw new Error('Please pass in a version');
    }
    if (!_.isFunction(fn)) {
      throw new Error('Please pass in a function');
    }

    var wrappedFn;
    if (fn.length === 1) {
      wrappedFn = function (s, cb) {
        try {
          cb(null, fn(s));
        } catch (err) {
          cb(err);
        }
      };
    } else {
      wrappedFn = fn;
    }

    this.committingSnapshotTransformerRegistrations.push({ meta: meta, fn: wrappedFn });
    return this;
  },

  /**
   * Returns true if a new snapshot should be done.
   * @param {Number} loadingTime    The loading time in ms of the eventstore data.
   * @param {Array}  events         The loaded events.
   * @param {Object} aggregateModel The aggregate json object. [could be used for other algorithms]
   * @param {Array}  streams        All loaded eventstreams for this aggregate.
   * @returns {boolean}
   */
  isSnapshotNeeded: function (loadingTime, events) {
    var snapshotThreshold = 100;
    if (this.options.snapshotThreshold) {
      snapshotThreshold = this.options.snapshotThreshold;
    }

    if (this.options.snapshotThresholdMs) {
      return loadingTime >= this.options.snapshotThresholdMs;
    }

    return events.length >= snapshotThreshold;
  },

  /**
   * Checks if a snapshot should be ignored.
   * @param {Object} snapshot       The the snapshot.
   * @returns {boolean}
   */
  shouldIgnoreSnapshot: function (snapshot) {
    if (!this.snapshotIgnores[snapshot.version]) {
      return false;
    }

    return this.snapshotIgnores[snapshot.version](snapshot.data);
  },

  /**
   * Defines the algorithm to identify if a snapshot is needed to be done.
   * @param {Function} fn Function containing the algorithm. Should return true or false.
   *                      `function(loadingTime, events, aggregateModel){}`
   */
  defineSnapshotNeed: function (fn) {
    if (!_.isFunction(fn)) {
      throw new Error('Please pass in a function');
    }

    this.isSnapshotNeeded = fn;
    return this;
  },

  /**
   * Defines a new conversion function for older snapshot versions.
   * @param {Object}   meta Meta infos like: { version: 10 }
   * @param {Function} fn   Function containing the conversion rule
   *                        `function(snapshotData, aggregateModel){}`
   * @returns {Aggregate}
   */
  defineSnapshotConversion: function (meta, fn) {
    if (!_.isObject(meta) || meta.version === undefined || meta.version === null || !_.isNumber(meta.version)) {
      throw new Error('Please pass in a version');
    }
    if (!_.isFunction(fn)) {
      throw new Error('Please pass in a function');
    }

    this.snapshotConversionRegistrations.push({ meta: meta, fn: fn });
    return this;
  },

  /**
   * Defines a if a snapshot should be ignored. -> if true it will loads all events
   * @param {Object}   meta Meta infos like: { version: 10 }
   * @param {Function} fn   Function containing the check function [optional], default return true
   *                        `function(snapshotData){ return true; }`
   * @returns {Aggregate}
   */
  defineIgnoreSnapshot: function (meta, fn) {
    if (!_.isObject(meta) || meta.version === undefined || meta.version === null || !_.isNumber(meta.version)) {
      throw new Error('Please pass in a version');
    }

    if (!fn) {
      this.snapshotIgnores[meta.version] = function () {
        return true;
      };
      return this;
    }

    if (_.isBoolean(fn)) {
      this.snapshotIgnores[meta.version] = function () {
        return fn;
      };
      return this;
    }

    this.snapshotIgnores[meta.version] = fn;
    return this;
  },

  /**
   * Inject idGenerator function for aggregate id.
   * @param   {Function}  fn The function to be injected.
   * @returns {Aggregate}    to be able to chain...
   */
  defineAggregateIdGenerator: function (fn) {
    if (fn.length === 0) {
      var orgFn = fn;
      fn = function(callback) {
        callback(null, orgFn());
      };
    }

    this.getNewAggregateId = fn;

    return this;
  },

  /**
   * Inject idGenerator function for aggregate id that is command aware.
   * @param   {Function}  fn The function to be injected.
   * @returns {Aggregate}    to be able to chain...
   */
  defineCommandAwareAggregateIdGenerator: function (fn) {
    if (fn.length === 0) throw new Error('Please define your function to accept the command!');
    if (fn.length === 1) {
      var orgFn = fn;
      fn = function(cmd, callback) {
        callback(null, orgFn(cmd));
      };
    }

    this.getNewAggregateId = fn;

    return this;
  }

});

module.exports = Aggregate;
```

## File: `lib/definitions/businessRule.js`
```javascript
var Definition = require('../definitionBase'),
  util = require('util'),
  _ = require('lodash'),
  debug = require('debug')('domain:businessRule'),
  BusinessRuleError = require('../errors/businessRuleError');

/**
 * BusinessRule constructor
 * @param {Object}   meta           Meta infos like: { name: 'name', priority: 1, description: 'bla bla' }
 * @param {Function} businessRuleFn Function handle
 *                                  `function(changed, previous, events, command, callback){}`
 * @constructor
 */
function BusinessRule (meta, businessRuleFn) {
  Definition.call(this, meta);

  meta = meta || {};

  if (!businessRuleFn || !_.isFunction(businessRuleFn)) {
    var err = new Error('Business rule function not injected!');
    debug(err);
    throw err;
  }

  this.description = meta.description;
  this.priority = meta.priority || Infinity;

  this.businessRuleFn = businessRuleFn;
}

util.inherits(BusinessRule, Definition);

_.extend(BusinessRule.prototype, {

  /**
   * Inject the aggregate module.
   * @param {Aggregate} aggregate The context module to be injected.
   */
  defineAggregate: function (aggregate) {
    if (!aggregate || !_.isObject(aggregate)) {
      var err = new Error('Please inject a valid aggregate object!');
      debug(err);
      throw err;
    }

    this.aggregate = aggregate;
  },

  /**
   * Checks this business rule.
   * @param {Object}   changed  The new aggregate values.
   * @param {Object}   previous The previous aggregate values.
   * @param {Array}    events   All new generated events.
   * @param {Object}   command  The command that was handled.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err){}`
   */
  check: function (changed, previous, events, command, callback) {

    var self = this;
    var callbacked = false;

    function handleError (err) {
      debug(err);

      if (_.isString(err)) {
        if (_.isEmpty(err)) {
          err = self.description;
        }
        err = new BusinessRuleError(err);
      } else if (err instanceof BusinessRuleError) {
        // do nothing
      } else {
        err = new BusinessRuleError(err.message || self.description);
      }

      callbacked = true;
      callback(err);
    }

    try {
      if (this.businessRuleFn.length === 5) {
        this.businessRuleFn(changed, previous, events, command, function (err) {
          if (err) {
            return handleError(err);
          }
          callbacked = true;
          callback(null);
        });
      } else {
        var err = this.businessRuleFn(changed, previous, events, command);
        if (err) {
          return handleError(err);
        }
        callbacked = true;
        callback(null);
      }
    } catch (err) {
      if (!callbacked) {
        return handleError(err);
      }
      throw err;
    }
  }

});

module.exports = BusinessRule;
```

## File: `lib/definitions/command.js`
```javascript
var Definition = require('../definitionBase'),
  util = require('util'),
  _ = require('lodash'),
  dotty = require('dotty'),
  async = require('async'),
  debug = require('debug')('domain:command'),
  BusinessRuleError = require('../errors/businessRuleError');

/**
 * Command constructor
 * @param {Object}   meta  Meta infos like: { name: 'name', version: 1, payload: 'some.path' }
 * @param {Function} cmdFn Function handle
 *                         `function(cmd, aggregateModel){}`
 * @constructor
 */
function Command (meta, cmdFn) {
  Definition.call(this, meta);

  meta = meta || {};

  if (!cmdFn || !_.isFunction(cmdFn)) {
    var err = new Error('Command function not injected!');
    debug(err);
    throw err;
  }

  // this.source = meta.source || {};

  this.version = meta.version || 0;
  this.payload = meta.payload === '' ? meta.payload : (meta.payload || null);
  if (meta.existing) {
    this.existing = true;
  } else if (meta.existing === false) {
    this.existing = false;
  } else {
    this.existing = undefined;
  }

  this.cmdFn = cmdFn;

  this.preConditions = [];
  this.preLoadConditions = [];
}

util.inherits(Command, Definition);

_.extend(Command.prototype, {

  /**
   * Inject the aggregate module.
   * @param {Aggregate} aggregate The context module to be injected.
   */
  defineAggregate: function (aggregate) {
    if (!aggregate || !_.isObject(aggregate)) {
      var err = new Error('Please inject a valid aggregate object!');
      debug(err);
      throw err;
    }

    this.aggregate = aggregate;
  },

  /**
   * Injects the pre-condition function.
   * @param {Function} preCond The pre-condition function that should be injected
   */
  addPreCondition: function (preCond) {
    if (!preCond || !_.isObject(preCond)) {
      var err = new Error('Please inject a valid preCondition object!');
      debug(err);
      throw err;
    }

    if (!preCond.payload && preCond.payload !== '') {
      preCond.payload = this.aggregate.defaultPreConditionPayload;
    }

    if (this.preConditions.indexOf(preCond) < 0) {
      preCond.defineAggregate(this.aggregate);
      this.preConditions.push(preCond);
      this.preConditions = _.sortBy(this.preConditions, function(pc) {
        return pc.priority;
      });
    }
  },

  /**
   * Injects the pre-load-condition function.
   * @param {Function} preLoadCond The pre-load-condition function that should be injected
   */
  addPreLoadCondition: function (preLoadCond) {
    if (!preLoadCond || !_.isObject(preLoadCond)) {
      var err = new Error('Please inject a valid preCondition object!');
      debug(err);
      throw err;
    }

    if (!preLoadCond.payload) {
      preLoadCond.payload = this.aggregate.defaultPreLoadConditionPayload;
    }

    if (this.preLoadConditions.indexOf(preLoadCond) < 0) {
      preLoadCond.defineAggregate(this.aggregate);
      this.preLoadConditions.push(preLoadCond);
      this.preLoadConditions = _.sortBy(this.preLoadConditions, function(pc) {
        return pc.priority;
      });
    }
  },

  /**
   * Injects the validator function.
   * @param {Function} validator The validator function that should be injected
   */
  defineValidation: function (validator) {
    if (!_.isFunction(validator)) {
      var err = new Error('Please pass in a function');
      debug(err);
      throw err;
    }
    if (validator.length == 2) {
      return this.validator = validator;
    }

    this.validator = function (data, callback) {
      callback(validator(data));
    };

    return this.validator;
  },

  /**
   * Validates the requested command.
   * @param {Object} cmd The command object
   * @returns {ValidationError}
   */
  validate: function (cmd, callback) {
    if (!this.validator) {
      debug('no validation rule for ' + this.name);
      return callback();
    }
    return this.validator(cmd, callback);
  },

  /**
   * Checks for pre-load conditions
   * @param {Object}         cmd            The command object.
   * @param {Function}       callback       The function, that will be called when this action is completed.
   *                                        `function(err){}`
   */
  checkPreLoadConditions: function (cmd, callback) {
    if (this.preLoadConditions.length === 0) {
      debug('no pre-load-condition for ' + this.name);
      return callback(null);
    }

    var self = this;
    async.eachSeries(this.preLoadConditions, function (preLoadCondition, callback) {
      if (preLoadCondition.version === undefined || preLoadCondition.version === null || preLoadCondition.version === self.version) {
        return preLoadCondition.check(cmd, callback);
      }
      callback(null);
    }, callback);
  },

  /**
   * Checks for pre-conditions
   * @param {Object}         cmd            The command object.
   * @param {AggregateModel} aggregateModel The aggregate object.
   * @param {Function}       callback       The function, that will be called when this action is completed.
   *                                        `function(err){}`
   */
  checkPreConditions: function (cmd, aggregateModel, callback) {
    if (this.existing === true && aggregateModel.get('_revision') === 0) {
      var err = new BusinessRuleError('This command only wants to be handled, if aggregate already existing!', {
        type: 'AggregateNotExisting',
        aggregateId: aggregateModel.id,
        aggregateRevision: aggregateModel.get('_revision')
      });
      debug(err);
      return callback(err);
    }

    if (this.existing === false && aggregateModel.get('_revision') !== 0) {
      var err = new BusinessRuleError('This command only wants to be handled, if aggregate not existing!', {
        type: 'AggregateAlreadyExisting',
        aggregateId: aggregateModel.id,
        aggregateRevision: aggregateModel.get('_revision')
      });
      debug(err);
      return callback(err);
    }

    if (this.preConditions.length === 0) {
      debug('no pre-condition for ' + this.name);
      return callback(null);
    }

    var self = this;
    async.eachSeries(this.preConditions, function (preCondition, callback) {
      if (preCondition.version === undefined || preCondition.version === null || preCondition.version === self.version) {
        return preCondition.check(cmd, aggregateModel, callback);
      }
      callback(null);
    }, callback);
  },

  /**
   * Get infos to load correct stream.
   * @param {Object} cmd The command object.
   * @returns {Array}
   */
  getLoadInfo: function (cmd) {
    var aggregateId = dotty.get(cmd, this.definitions.command.aggregateId);
    var aggregateName = this.aggregate.name;
    var contextName = this.aggregate.context.name;

    var toLoad = [{
      context: contextName,
      aggregate: aggregateName,
      aggregateId: aggregateId
    }];

    if (_.isFunction(this.getStreamsInfo)) {
      toLoad = this.getStreamsInfo(cmd);
      if (!_.isArray(toLoad)) {
        toLoad = [toLoad];
      }
      toLoad.forEach(function (l) {
        l.aggregateId = l.aggregateId || aggregateId;
      });
    }

    if (toLoad[0].context !== contextName || toLoad[0].aggregate !== aggregateName) {
      throw new Error('First stream to load has to be the new one!');
    }

    return toLoad;
  },

  /**
   * Handles the passed command
   * @param {Object}         cmd            The command object.
   * @param {AggregateModel} aggregateModel The aggregate object.
   */
  handle: function (cmd, aggregateModel) {
    if (!this.payload || this.payload === '') {
      this.cmdFn(_.cloneDeep(cmd), aggregateModel);
      return;
    }

    var payload = dotty.get(cmd, this.payload);
    this.cmdFn(_.cloneDeep(payload), aggregateModel);
  },

  /**
   * Defines which event streams should be loaded before handling this event.
   * @param {Function} fn Function containing the algorithm. Should return an array of infos.
   *                      `function(cmd){}`
   */
  defineEventStreamsToLoad: function (fn) {
    if (!_.isFunction(fn)) {
      throw new Error('Please pass in a function');
    }

    this.getStreamsInfo = fn;
    return this;
  }

});

module.exports = Command;
```

## File: `lib/definitions/commandHandler.js`
```javascript
var DefaultCommandHandler = require('../defaultCommandHandler'),
  util = require('util'),
  _ = require('lodash'),
  dotty = require('dotty'),
  debug = require('debug')('domain:commandHandler');

/**
 * CommandHandler constructor
 * @param {Object}   meta      Meta infos like: { name: 'name', version: 1 }
 * @param {Function} cmdHndlFn Function handle
 *                             `function(aggId, cmd, commandHandler, callback){}`
 * @constructor
 */
function CommandHandler (meta, cmdHndlFn) {
  DefaultCommandHandler.call(this, meta);

  console.log('Is your use case not solvable without a custom command handling? Sagas? Micro-Services?');

  meta = meta || {};

  this.version = meta.version || 0;

  if (!cmdHndlFn || !_.isFunction(cmdHndlFn)) {
    var err = new Error('CommandHandler function not injected!');
    debug(err);
    throw err;
  }

  this.cmdHndlFn = cmdHndlFn;
}

util.inherits(CommandHandler, DefaultCommandHandler);

_.extend(CommandHandler.prototype, {

  /**
   * Handles the passed command
   * @param {Object}   cmd      The passed command
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err, evts){}`
   */
  handle: function (cmd, callback) {
    debug('called a custom command handler');
    console.log('Is your use case not solvable without a custom command handling? Sagas? Micro-Services?');

    var self = this;

    function _handle (aggId) {
      var concatenatedId = self.getConcatenatedId(aggId, cmd);

      var isFirst = !self.getNextCommandInQueue(concatenatedId);

      self.queueCommand(concatenatedId, cmd, callback);

      if (!isFirst) {
        return;
      }

      (function handleNext (aggregateId, c) {
        var concId = self.getConcatenatedId(aggregateId, c);
        var cmdEntry = self.getNextCommandInQueue(concId);
        if (cmdEntry) {
          if (cmdEntry.callback.length > 2) {
            self.cmdHndlFn(aggregateId, cmdEntry.command, self, function (err, evts, aggData, meta) {
              self.removeCommandFromQueue(concId, cmdEntry.command);
              handleNext(aggregateId, cmdEntry.command);
              cmdEntry.callback(err, evts, aggData, meta);
            });
            return;
          }
          self.cmdHndlFn(aggregateId, cmdEntry.command, self, function (err, evts) {
            self.removeCommandFromQueue(concId, cmdEntry.command);
            handleNext(aggregateId, cmdEntry.command);
            cmdEntry.callback(err, evts);
          });
        }
      })(aggId, cmd);
    }

    if (dotty.exists(cmd, this.definitions.command.aggregateId)) {
      return _handle(dotty.get(cmd, this.definitions.command.aggregateId));
    }

    debug('no aggregateId in command, so generate a new one');

    this.getNewAggregateId(cmd, function (err, id) {
      if (err) {
        debug(err);
        return callback(err);
      }

      return _handle(id);
    });
  }

});

module.exports = CommandHandler;
```

## File: `lib/definitions/committingEventTransformer.js`
```javascript
var Definition = require('../definitionBase'),
  util = require('util'),
  _ = require('lodash'),
  debug = require('debug')('domain:committingEventTransformer');

/**
 * CommittingEventTransformer constructor
 * @param {Object}   meta  Meta infos like: { name: 'name', version: 1 }
 * @param {Function} transformFn Fuction handle
 *                         `function(evt, clb){}`
 * @constructor
 */
function CommittingEventTransformer (meta, transformFn) {
  Definition.call(this, meta);

  meta = meta || {};

  if (transformFn && !_.isFunction(transformFn)) {
    var err = new Error('Transform function not injected!');
    debug(err);
    throw err;
  }

  this.version = meta.version;

  this.transformFn = transformFn;
}

util.inherits(CommittingEventTransformer, Definition);

_.extend(CommittingEventTransformer.prototype, {

  /**
   * transform an CommittingEventTransformer.
   * @param {Object}   evt      The CommittingEventTransformer object.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err, evt){}`
   */
  transform: function (evt, callback) {
    var self = this;
    var callbacked = false;

    function handleError (err) {
      debug(err);
      callbacked = true;
      callback(err);
    }

    try {
      if (this.transformFn.length === 2) {
        this.transformFn(_.cloneDeep(evt), function (err, newEvt) {
          if (err) return handleError(err);
          callbacked = true;
          callback(null, newEvt);
        });
      } else {
        var newEvt = this.transformFn(_.cloneDeep(evt));
        callback(null, newEvt);
      }
    } catch (err) {
      if (!callbacked) {
        return handleError(err);
      }
      throw err;
    }
  }

});

module.exports = CommittingEventTransformer;
```

## File: `lib/definitions/context.js`
```javascript
var Definition = require('../definitionBase'),
  util = require('util'),
  _ = require('lodash'),
  debug = require('debug')('domain:context'),
  Aggregate = require('./aggregate');

/**
 * Context constructor
 * @param {Object} meta meta infos like: { name: 'name' }
 * @constructor
 */
function Context (meta) {
  Definition.call(this, meta);

  meta = meta || {};

  this.externallyLoaded = meta.externallyLoaded || false;

  this.aggregates = [];
}

util.inherits(Context, Definition);

_.extend(Context.prototype, {

  /**
   * Adds an aggregate to this context.
   * @param {Aggregate} aggregate the aggregate that should be added
   */
  addAggregate: function (aggregate) {
    if (!aggregate || !(aggregate instanceof Aggregate)) {
      throw new Error('Passed object should be an Aggregate');
    }

    aggregate.defineContext(this);

    if (this.aggregates.indexOf(aggregate) < 0) {
      this.aggregates.push(aggregate);
    }
  },

  /**
   * Returns the aggregate with the requested name.
   * @param {String} name command name
   * @returns {Aggregate}
   */
  getAggregate: function (name) {
    if (!name || !_.isString(name)) {
      throw new Error('Please pass in an aggregate name!');
    }

    return _.find(this.aggregates, function (agg) {
      return agg.name === name;
    });
  },

  /**
   * Return the aggregate that handles the requested command.
   * @param {String} name    command name
   * @param {Number} version command version
   * @returns {Aggregate}
   */
  getAggregateForCommand: function (name, version) {
    if (!name || !_.isString(name)) {
      throw new Error('Please pass in a command name!');
    }

    for (var a in this.aggregates) {
      var aggr = this.aggregates[a];
      var cmd = aggr.getCommand(name, version);
      if (cmd) {
        return aggr;
      }
    }

    for (var a in this.aggregates) {
      var aggr = this.aggregates[a];
      var cmdHndl = aggr.getCommandHandler(name, version);
      if (cmdHndl && cmdHndl !== aggr.defaultCommandHandler) {
        return aggr;
      }
    }

    debug('no matching aggregate found for command ' + name);

    return null;
  },

  // /**
  //  * Return the aggregate that handles the requested command.
  //  * @param {Object} query the query object
  //  * @returns {Aggregate}
  //  */
  // getAggregateForCommandByOldTarget: function (query) {
  //   if (!query) {
  //     throw new Error('Please pass in a query object!');
  //   }
  //
  //   for (var a in this.aggregates) {
  //     var aggr = this.aggregates[a];
  //     var cmd = aggr.getCommand(query.name, query.version);
  //     if (cmd && cmd.source && cmd.source.context === query.context && cmd.source.aggregate === query.aggregate) {
  //       return aggr;
  //     }
  //   }
  //
  //   for (var a in this.aggregates) {
  //     var aggr = this.aggregates[a];
  //     var cmdHndl = aggr.getCommandHandler(query.name, query.version);
  //     if (cmdHndl && cmdHndl !== aggr.defaultCommandHandler && cmdHndl.source && cmdHndl.source.context === query.context && cmdHndl.source.aggregate === query.aggregate) {
  //       return aggr;
  //     }
  //   }
  //
  //   debug('no matching aggregate found for command ' + query.name);
  //
  //   return null;
  // },

  /**
   * Return all aggregates.
   * @returns {Array}
   */
  getAggregates: function () {
    return this.aggregates;
  }

});

module.exports = Context;
```

## File: `lib/definitions/event.js`
```javascript
var Definition = require('../definitionBase'),
  util = require('util'),
  _ = require('lodash'),
  dotty = require('dotty'),
  debug = require('debug')('domain:event');

/**
 * Event constructor
 * @param {Object}   meta  Meta infos like: { name: 'name', version: 1, payload: 'some.path' }
 * @param {Function} evtFn Fuction handle
 *                         `function(evtData, aggregateModel){}`
 * @constructor
 */
function Event (meta, evtFn) {
  Definition.call(this, meta);

  meta = meta || {};

  if (evtFn && !_.isFunction(evtFn)) {
    var err = new Error('Event function not injected!');
    debug(err);
    throw err;
  }

  this.version = meta.version || 0;
  this.payload = meta.payload === '' ? meta.payload : (meta.payload || null);

  this.evtFn = evtFn;
}

util.inherits(Event, Definition);

_.extend(Event.prototype, {

  /**
   * Apply an event.
   * @param {Object}         evt            The event object.
   * @param {AggregateModel} aggregateModel The aggregate object.
   */
  apply: function (evt, aggregateModel) {
    if (!this.evtFn) {
      return;
    }

    if (!this.payload || this.payload === '') {
      this.evtFn(evt, aggregateModel);
      return;
    }

    var payload = dotty.get(evt, this.payload);
    this.evtFn(payload, aggregateModel);
  }

});

module.exports = Event;
```

## File: `lib/definitions/loadingEventTransformer.js`
```javascript
var Definition = require('../definitionBase'),
  util = require('util'),
  _ = require('lodash'),
  debug = require('debug')('domain:loadingEventTransformer');

/**
 * LoadingEventTransformer constructor
 * @param {Object}   meta  Meta infos like: { name: 'name', version: 1 }
 * @param {Function} transformFn Fuction handle
 *                         `function(evt, clb){}`
 * @constructor
 */
function LoadingEventTransformer (meta, transformFn) {
  Definition.call(this, meta);

  meta = meta || {};

  if (transformFn && !_.isFunction(transformFn)) {
    var err = new Error('Transform function not injected!');
    debug(err);
    throw err;
  }

  this.version = meta.version;

  this.transformFn = transformFn;
}

util.inherits(LoadingEventTransformer, Definition);

_.extend(LoadingEventTransformer.prototype, {

  /**
   * transform an LoadingEventTransformer.
   * @param {Object}   evt      The LoadingEventTransformer object.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err, evt){}`
   */
  transform: function (evt, callback) {
    var self = this;
    var callbacked = false;

    function handleError (err) {
      debug(err);
      callbacked = true;
      callback(err);
    }

    try {
      if (this.transformFn.length === 2) {
        this.transformFn(_.cloneDeep(evt), function (err, newEvt) {
          if (err) return handleError(err);
          callbacked = true;
          callback(null, newEvt);
        });
      } else {
        var newEvt = this.transformFn(_.cloneDeep(evt));
        callback(null, newEvt);
      }
    } catch (err) {
      if (!callbacked) {
        return handleError(err);
      }
      throw err;
    }
  }

});

module.exports = LoadingEventTransformer;
```

## File: `lib/definitions/preCondition.js`
```javascript
var Definition = require('../definitionBase'),
  util = require('util'),
  _ = require('lodash'),
  dotty = require('dotty'),
  debug = require('debug')('domain:preCondition'),
  BusinessRuleError = require('../errors/businessRuleError');

/**
 * PreCondition constructor
 * @param {Object}   meta           Meta infos like: { name: 'name', version: 1, priority: 1, payload: 'some.path', description: 'bla bla' }
 * @param {Function} preConditionFn Function handle
 *                                  `function(command, aggData, callback){}`
 * @constructor
 */
function PreCondition (meta, preConditionFn) {
  Definition.call(this, meta);

  meta = meta || {};

  if (!preConditionFn || !_.isFunction(preConditionFn)) {
    var err = new Error('Pre-condition function not injected!');
    debug(err);
    throw err;
  }

  this.description = meta.description;
  this.version = meta.version;
  this.payload = meta.payload === '' ? meta.payload : (meta.payload || null);
  this.priority = meta.priority || Infinity;

  this.preConditionFn = preConditionFn;
}

util.inherits(PreCondition, Definition);

_.extend(PreCondition.prototype, {

  /**
   * Inject the aggregate module.
   * @param {Aggregate} aggregate The context module to be injected.
   */
  defineAggregate: function (aggregate) {
    if (!aggregate || !_.isObject(aggregate)) {
      var err = new Error('Please inject a valid aggregate object!');
      debug(err);
      throw err;
    }

    this.aggregate = aggregate;
  },

  /**
   * Checks this business rule.
   * @param {Object}   command  The command that was handled.
   * @param {Object}   aggData  The aggregate values.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err){}`
   */
  check: function (command, aggData, callback) {

    var self = this;
    var callbacked = false;

    function handleError (err) {
      debug(err);

      if (_.isString(err)) {
        if (_.isEmpty(err)) {
          err = self.description;
        }
        err = new BusinessRuleError(err);
      } else if (err instanceof BusinessRuleError) {
        // do nothing
      } else {
        err = new BusinessRuleError(err.message || self.description);
      }

      callbacked = true;
      callback(err);
    }

    var payload;
    if (!this.payload || this.payload === '') {
      payload = command;
    } else {
      payload = dotty.get(command, this.payload);
    }

    try {
      if (this.preConditionFn.length === 3) {
        this.preConditionFn(_.cloneDeep(payload), aggData, function (err) {
          if (err) {
            return handleError(err);
          }
          callbacked = true;
          callback(null);
        });
      } else {
        var err = this.preConditionFn(_.cloneDeep(payload), aggData);
        if (err) {
          return handleError(err);
        }
        callbacked = true;
        callback(null);
      }
    } catch (err) {
      if (!callbacked) {
        return handleError(err);
      }
      throw err;
    }
  }

});

module.exports = PreCondition;
```

## File: `lib/definitions/preLoadCondition.js`
```javascript
var Definition = require('../definitionBase'),
  util = require('util'),
  _ = require('lodash'),
  dotty = require('dotty'),
  debug = require('debug')('domain:preLoadCondition'),
  BusinessRuleError = require('../errors/businessRuleError');

/**
 * PreLoadCondition constructor
 * @param {Object}   meta  Meta infos like: { name: 'name', version: 1, priority: 1, payload: 'some.path', description: 'bla bla' }
 * @param {Function} preLoadConditionFn Function handle
 *                                  `function(command, aggData, callback){}`
 * @constructor
 */
function PreLoadCondition (meta, preLoadConditionFn) {
  Definition.call(this, meta);

  meta = meta || {};

  if (!preLoadConditionFn || !_.isFunction(preLoadConditionFn)) {
    var err = new Error('Pre-load-condition function not injected!');
    debug(err);
    throw err;
  }

  this.description = meta.description;
  this.version = meta.version;
  this.payload = meta.payload || null;
  this.priority = meta.priority || Infinity;

  this.preLoadConditionFn = preLoadConditionFn;
}

util.inherits(PreLoadCondition, Definition);

_.extend(PreLoadCondition.prototype, {

  /**
   * Inject the aggregate module.
   * @param {Aggregate} aggregate The context module to be injected.
   */
  defineAggregate: function (aggregate) {
    if (!aggregate || !_.isObject(aggregate)) {
      var err = new Error('Please inject a valid aggregate object!');
      debug(err);
      throw err;
    }

    this.aggregate = aggregate;
  },

  /**
   * Checks this business rule.
   * @param {Object}   command  The command that was handled.
   * @param {Object}   aggData  The aggregate values.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err){}`
   */
  check: function (command, callback) {

    var self = this;
    var callbacked = false;

    function handleError (err) {
      debug(err);

      if (_.isString(err)) {
        if (_.isEmpty(err)) {
          err = self.description;
        }
        err = new BusinessRuleError(err);
      } else if (err instanceof BusinessRuleError) {
        // do nothing
      } else {
        err = new BusinessRuleError(err.message || self.description);
      }

      callbacked = true;
      callback(err);
    }

    var payload;
    if (!this.payload || this.payload === '') {
      payload = command;
    } else {
      payload = dotty.get(command, this.payload);
    }

    try {
      if (this.preLoadConditionFn.length === 2) {
        this.preLoadConditionFn(_.cloneDeep(payload), function (err) {
          if (err) {
            return handleError(err);
          }
          callbacked = true;
          callback(null);
        });
      } else {
        var err = this.preLoadConditionFn(_.cloneDeep(payload));
        if (err) {
          return handleError(err);
        }
        callbacked = true;
        callback(null);
      }
    } catch (err) {
      if (!callbacked) {
        return handleError(err);
      }
      throw err;
    }
  }

});

module.exports = PreLoadCondition;
```

## File: `lib/errors/aggregateConcurrencyError.js`
```javascript
// Grab the util module that's bundled with Node
var util = require('util');

// Create a new custom Error constructor
function AggregateConcurrencyError(msg, more) {
  // Pass the constructor to V8's
  // captureStackTrace to clean up the output
  Error.captureStackTrace(this, AggregateConcurrencyError);

  // If defined, store a custom error message
  if (msg) {
    this.message = msg;
  }

  // If defined, store more infos
  if (more) {
    this.more = more;
  }
}

// Extend our custom Error from Error
util.inherits(AggregateConcurrencyError, Error);

// Give our custom error a name property. Helpful for logging the error later.
AggregateConcurrencyError.prototype.name = AggregateConcurrencyError.name;

module.exports = AggregateConcurrencyError;
```

## File: `lib/errors/aggregateDestroyedError.js`
```javascript
// Grab the util module that's bundled with Node
var util = require('util');

// Create a new custom Error constructor
function AggregateDestroyedError(msg, more) {
  // Pass the constructor to V8's
  // captureStackTrace to clean up the output
  Error.captureStackTrace(this, AggregateDestroyedError);

  // If defined, store a custom error message
  if (msg) {
    this.message = msg;
  }

  // If defined, store more infos
  if (more) {
    this.more = more;
  }
}

// Extend our custom Error from Error
util.inherits(AggregateDestroyedError, Error);

// Give our custom error a name property. Helpful for logging the error later.
AggregateDestroyedError.prototype.name = AggregateDestroyedError.name;

module.exports = AggregateDestroyedError;
```

## File: `lib/errors/businessRuleError.js`
```javascript
// Grab the util module that's bundled with Node
var util = require('util');

// Create a new custom Error constructor
function BusinessRuleError(msg, more) {
  // Pass the constructor to V8's
  // captureStackTrace to clean up the output
  Error.captureStackTrace(this, BusinessRuleError);

  // If defined, store a custom error message
  if (msg) {
    this.message = msg;
  }

  // If defined, store more infos
  if (more) {
    this.more = more;
  }
}

// Extend our custom Error from Error
util.inherits(BusinessRuleError, Error);

// Give our custom error a name property. Helpful for logging the error later.
BusinessRuleError.prototype.name = BusinessRuleError.name;

module.exports = BusinessRuleError;
```

## File: `lib/errors/concurrencyError.js`
```javascript
// Grab the util module that's bundled with Node
var util = require('util');

// Create a new custom Error constructor
function ConcurrencyError(msg, more) {
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

## File: `lib/errors/duplicateCommandError.js`
```javascript
// Grab the util module that's bundled with Node
var util = require('util');

// Create a new custom Error constructor
function DuplicateCommandError(msg, more) {
  // Pass the constructor to V8's
  // captureStackTrace to clean up the output
  Error.captureStackTrace(this, DuplicateCommandError);

  // If defined, store a custom error message
  if (msg) {
    this.message = msg;
  }

  // If defined, store more infos
  if (more) {
    this.more = more;
  }
}

// Extend our custom Error from Error
util.inherits(DuplicateCommandError, Error);

// Give our custom error a name property. Helpful for logging the error later.
DuplicateCommandError.prototype.name = DuplicateCommandError.name;

module.exports = DuplicateCommandError;
```

## File: `lib/errors/validationError.js`
```javascript
// Grab the util module that's bundled with Node
var util = require('util');

// Create a new custom Error constructor
function ValidationError(msg, more) {
  // Pass the constructor to V8's
  // captureStackTrace to clean up the output
  Error.captureStackTrace(this, ValidationError);

  // If defined, store a custom error message
  if (msg) {
    this.message = msg;
  }

  // If defined, store more infos
  if (more) {
    this.more = more;
  }
}

// Extend our custom Error from Error
util.inherits(ValidationError, Error);

// Give our custom error a name property. Helpful for logging the error later.
ValidationError.prototype.name = ValidationError.name;

module.exports = ValidationError;
```

## File: `lib/lock/base.js`
```javascript
var util = require('util'),
  EventEmitter = require('events').EventEmitter,
  prequire = require('parent-require'),
  _ = require('lodash'),
  uuid = require('uuid').v4;

/**
 * Lock constructor
 * @param {Object} options The options can have information like host, port, etc. [optional]
 */
function Lock(options) {
  options = options || {};

  EventEmitter.call(this);
}

util.inherits(Lock, EventEmitter);

function implementError (callback) {
  var err = new Error('Please implement this function!');
  if (callback) callback(err);
  throw err;
}

_.extend(Lock.prototype, {

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
   * Use this function to reserve an aggregate.
   * @param  {String}   workerId    The id of the worker.
   * @param  {String}   aggregateId The id of the aggregate
   * @param  {Function} callback    The function, that will be called when this action is completed. [optional]
   *                                `function(err){}`
   */
  reserve: function (workerId, aggregateId, callback) {
    implementError(callback);
  },

  /**
   * Use this function to get get all the worker that reserve an aggregate.
   * @param  {String}   aggregateId The id of the aggregate
   * @param  {Function} callback    The function, that will be called when this action is completed.
   *                                `function(err, workerIds){}` workerIds is of type Array.
   */
  getAll: function (aggregateId, callback) {
    implementError(callback);
  },

  /**
   * Use this function to remove all reservation of an aggregate.
   * @param  {String}   aggregateId The id of the aggregate
   * @param  {Function} callback    The function, that will be called when this action is completed. [optional]
   *                                `function(err){}`
   */
  resolve: function (aggregateId, callback) {
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

Lock.use = function (toRequire) {
  var required;
  try {
    required = require(toRequire);
  } catch (e) {
    // workaround when `npm link`'ed for development
    required = prequire(toRequire);
  }
  return required;
};

module.exports = Lock;
```

## File: `lib/lock/index.js`
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
  Lock: Base,

  create: function(options, callback) {
    if (typeof options === 'function') {
      callback = options;
      options = {};
    }

    options = options || {};

    var Lock;

    try {
      Lock = getSpecificDbImplementation(options);
    } catch (err) {
      if (callback) callback(err);
      throw err;
    }

    var lock = new Lock(options);
    if (callback) {
      process.nextTick(function () {
        tolerate(function (callback) {
          lock.connect(callback);
        }, options.timeout || 0, callback || function () {
        });
      });
    }
    return lock;
  }
};
```

## File: `lib/lock/databases/azuretable.js`
```javascript
var util = require('util'),
  Lock = require('../base'),
  _ = require('lodash'),
  async = require('async'),
  azure = Lock.use('azure-storage'),
  eg = azure.TableUtilities.entityGenerator;

function AzureTable(options) {
  Lock.call(this, options);

  var azureConf = {
    storageAccount: 'nodecqrs',
    storageAccessKey: 'StXScH574p1krnkjbxjkHkMkrtbIMQpYMbH1D1uYVqS4ny/DpXVkL4ld02xeKupCQnIIN+v0KVmdLLSVA/cxTQ==',
    storageTableHost: 'https://nodecqrs.table.core.windows.net/'
  };

  this.options = _.defaults(options, azureConf);

  var defaults = {
    lockTableName: 'aggregatelock'
  };

  this.options = _.defaults(this.options, defaults);
}

util.inherits(AzureTable, Lock);

_.extend(AzureTable.prototype, {

  connect: function (callback) {
    var retryOperations = new azure.ExponentialRetryPolicyFilter();

    var self = this;

    this.client = azure.createTableService(this.options.storageAccount, this.options.storageAccessKey, this.options.storageTableHost).withFilter(retryOperations);

    this.client.createTableIfNotExists(this.options.lockTableName, function (err) {
      if (err) {
        if (callback) callback(err);
        return;
      }

      self.emit('connect');
      if (callback) callback(null, self);
    });
  },

  disconnect: function (callback) {
    this.emit('disconnect');
    if (callback) callback(null);
  },

  reserve: function (workerId, aggregateId, callback) {
    var entity = {
      PartitionKey: eg.String(aggregateId),
      RowKey: eg.String(workerId),
      workerId: eg.String(workerId),
      aggregateId: eg.String(aggregateId),
      date: eg.DateTime(new Date())
    };

    this.client.insertEntity(this.options.lockTableName, entity, function (err) {
      if (callback) callback(err);
    });
  },

  getAll: function (aggregateId, callback) {
    var query = new azure.TableQuery();

    var options = {
      autoResolveProperties: true,
      entityResolver: function (entity) {
        return entity.workerId._;
      }
    };
    query.select('workerId');
    query.where('PartitionKey eq ?', aggregateId);

    this.client.queryEntities(this.options.lockTableName, query, null, options, function (err, result) {
      var res = [];

      if (err) {
        return callback(err);
      }

      res = _.sortBy(result.entries, "date");

      callback(null, res);
    });
  },

  resolve: function (aggregateId, callback) {

    var self = this;

    var query = new azure.TableQuery();
    query.where('PartitionKey eq ?', aggregateId);

    this.client.queryEntities(this.options.lockTableName, query, null, function (err, result) {
      if (err) {
        if (callback) callback(err);
        return;
      }

      async.each(result.entries, function (entity, callback) {
        self.client.deleteEntity(self.options.lockTableName, entity, function (err, response) {
          callback(err);
        });
      },
      function (err) {
        if (callback) callback(err);
      });
    });
  },

  clear: function (callback) {
    var self = this;

    this.client.queryEntities(this.options.lockTableName, null, null, function (err, entities) {
      if (err) {
        return callback(err);
      }

      async.each(entities.entries, function (entity, callback) {
        self.client.deleteEntity(self.options.lockTableName, entity, function (err, response) {
          callback(err);
        });
      },
      function (err) {
        if (callback) callback(err);
      });
    });
  }
});

module.exports = AzureTable;
```

## File: `lib/lock/databases/couchdb.js`
```javascript
var util = require('util'),
  Lock = require('../base'),
  _ = require('lodash'),
  async = require('async'),
  cradle = Lock.use('cradle');

function Couch(options) {
  Lock.call(this, options);

  var defaults = {
    host: 'http://localhost',
    port: 5984,
    dbName: 'domain',
    collectionName: 'aggregatelock'
  };

  _.defaults(options, defaults);

  var defaultOpt = {
    cache: true,
    raw: false,
    forceSave: true//,
    // secure: true,
    // auth: { username: 'login', password: 'pwd' }
  };

  options.options = options.options || {};

  _.defaults(options.options, defaultOpt);

  this.options = options;

  this.collectionName = options.collectionName;
}

util.inherits(Couch, Lock);

_.extend(Couch.prototype, {

  connect: function (callback) {
    var self = this;

    var options = this.options;

    var client = new (cradle.Connection)(options.host, options.port, options.options);
    var db = client.database(options.dbName);
    db.exists(function (err, exists) {

      function finish() {
        self.client = client;
        self.db = db;

        db.get('_design/aggregatelock', function (err, obj) {

          var view = {
            views: {
              findAll: {
                map: function (doc) {
                  emit(doc.collectionName, doc);
                }
              },
              findByAggregateId: {
                map: function (doc) {
                  emit({ collectionName: doc.collectionName, aggregateId: doc.aggregateId}, doc);
                }
              }
            }
          };

          if (err && err.error === 'not_found') {
            db.save('_design/aggregatelock', view, function (err) {
              if (!err) {
                self.emit('connect');
              }
              if (callback) callback(err, self);
            });
            return;
          }
          if (!err) {
            self.emit('connect');
          }
          if (callback) callback(err, self);
        });
      }

      if (err) {
        if (callback) callback(err);
        return;
      }

      if (!exists) {
        db.create(function (err) {
          if (err) {
            if (callback) callback(err);
            return;
          }
          finish();
        });
        return;
      }

      finish();
    });
  },

  disconnect: function(callback) {
    if (!this.client) {
      if (callback) callback(null);
      return;
    }

    // this.client.close();
    this.emit('disconnect');
    if (callback) callback(null);
  },

  getNewId: function(callback) {
    this.client.uuids(function(err, uuids) {
      if (err) {
        return callback(err);
      }
      callback(null, uuids[0].toString());
    });
  },

  reserve: function(workerId, aggregateId, callback) {
    this.db.save(workerId, { _id: workerId, aggregateId: aggregateId, collectionName: this.collectionName }, function (err) {
      if (callback) callback(err);
    });
  },

  getAll: function(aggregateId, callback) {
    this.db.view('aggregatelock/findByAggregateId', { key: { collectionName: this.collectionName, aggregateId: aggregateId } }, function (err, docs) {
      var res = [];

      if (!docs || docs.length === 0) {
        return callback(null, res);
      }

      for (var i = 0, len = docs.length; i < len; i++) {
        var id = docs[i].value._id;
        var found = _.find(res, function (r) {
          return r === id;
        });

        if (!found) {
          res.push(id);
        }
      }

      if (callback) callback(err, res);
    });
  },

  resolve: function(aggregateId, callback) {
    var self = this;

    this.db.view('aggregatelock/findByAggregateId', { key: { collectionName: this.collectionName, aggregateId: aggregateId } }, function (err, res) {
      if (err) {
        return callback(err);
      }

      async.each(res, function (r, callback) {
        self.db.remove(r._id, r._rev, callback);
      }, function (err) {
        if (callback) callback(err);
      });

    });
  },

  clear: function (callback) {
    var self = this;

    this.db.view('aggregatelock/findAll', { key: this.collectionName }, function (err, res) {
      if (err) {
        return callback(err);
      }

      async.each(res, function (r, callback) {
        self.db.remove(r._id, r._rev, callback);
      }, callback || function () {});

    });
  }

});

module.exports = Couch;
```

## File: `lib/lock/databases/dynamodb.js`
```javascript
var util = require('util'),
  Lock = require('../base'),
  _ = require('lodash'),
  async = require('async'),
  aws = Lock.use('aws-sdk');

function DynamoDB(options) {
  var awsConf = {
    region: 'ap-southeast-2',
    endpointConf: {}
  };

  if (process.env['AWS_DYNAMODB_ENDPOINT']) {
    awsConf.endpointConf = { endpoint: process.env['AWS_DYNAMODB_ENDPOINT'] };
  }

  this.options = _.defaults(options, awsConf);

  var defaults = {
    lockTableName: 'aggregatelock',
    ReadCapacityUnits: 1,
    WriteCapacityUnits: 3
  };

  this.options = _.defaults(this.options, defaults);
}

util.inherits(DynamoDB, Lock);

_.extend(DynamoDB.prototype, {
  connect: function(callback) {
    var self = this;
    self.client = new aws.DynamoDB(self.options.endpointConf);
    self.documentClient = new aws.DynamoDB.DocumentClient({ service: self.client });
    self.isConnected = true;

    var createAggregatelockTable = function(done) {
      createTableIfNotExists(
        self.client,
        AggregatelockTableDefinition(self.options),
        done
      );
    };

    createAggregatelockTable(function(err) {
      if (err) {
        if (callback) callback(err);
      } else {
        self.emit('connect');
        if (callback) callback(null, self);
      }
    });
  },

  disconnect: function(callback) {
    this.emit('disconnect');
    if (callback) callback(null);
  },

  reserve: function(workerId, aggregateId, callback) {
    var self = this;

    var params = {
      TableName: self.options.lockTableName,
      Item: {
        aggregateId: aggregateId,
        workerId: workerId,
        timeStamp: new Date().getTime()
      }
    };
    self.documentClient.put(params, function(err, data) {
      if (callback) callback(err);
    });
  },

  getAll: function(aggregateId, callback) {
    var self = this;

    if (callback) {
      var params = {
        TableName: self.options.lockTableName,
        KeyConditionExpression: '#aggrId = :a',
        ExpressionAttributeNames: {
          '#aggrId': 'aggregateId'
        },
        ExpressionAttributeValues: {
          ':a': aggregateId
        }
      };
      self.documentClient.query(params, function(err, data) {
        var res = [];
        if (err) {
          if (callback) callback(err);
          return;
        }
        res = _.sortBy(data.Items, 'timeStamp');
        if (callback) callback(null, _.map(res, function(r){ return r.workerId}));
      });
    }
  },

  resolve: function(aggregateId, callback) {
    var self = this;

    var queryParams = {
      TableName: self.options.lockTableName,
      KeyConditionExpression: '#aggrId = :a',
      ExpressionAttributeNames: {
        '#aggrId': 'aggregateId'
      },
      ExpressionAttributeValues: {
        ':a': aggregateId
      }
    };

    self.documentClient.query(queryParams, function(err, data) {
      if (err) {
        if (callback) callback(err);
        return;
      }
      async.each(
        data.Items,
        function(item, deleteCallback) {
          var params = {
            TableName: self.options.lockTableName,
            Key: { aggregateId: item.aggregateId, workerId: item.workerId }
          };
          self.documentClient.delete(params, function(deleteErr, data) {
            if (deleteErr) {
              return deleteCallback(deleteErr);
            }
            deleteCallback(null, data);
          });
        },
        function(err) {
          if (callback) callback(err);
        }
      );
    });
  },

  clear: function(callback) {
    var self = this;
    var query = {
      TableName: self.options.lockTableName
    };
    self.documentClient.scan(query, function(err, data) {
      if (err) {
        if (callback) callback(err);
        return;
      }
      async.each(
        data.Items,
        function(item, callback) {
          var params = {
            TableName: self.options.lockTableName,
            Key: { aggregateId: item.aggregateId, workerId: item.workerId }
          };
          self.documentClient.delete(params, function(error, response) {
            callback(error);
          });
        },
        function(error) {
          if (callback) callback(error);
        }
      );
    });
  }
});

function AggregatelockTableDefinition(opts) {
  var def = {
    TableName: opts.lockTableName,
    KeySchema: [
      { AttributeName: 'aggregateId', KeyType: 'HASH' },
      { AttributeName: 'workerId', KeyType: 'RANGE' }
    ],
    AttributeDefinitions: [
      { AttributeName: 'aggregateId', AttributeType: 'S' },
      { AttributeName: 'workerId', AttributeType: 'S' }
    ],
    ProvisionedThroughput: {
      ReadCapacityUnits: opts.ReadCapacityUnits,
      WriteCapacityUnits: opts.WriteCapacityUnits
    }
  };

  return def;
}

var createTableIfNotExists = function(client, params, callback) {
  var exists = function(p, cbExists) {
    client.describeTable({ TableName: p.TableName }, function(err, data) {
      if (err) {
        if (err.code === 'ResourceNotFoundException') {
          cbExists(null, { exists: false, definition: p });
        } else {
          cbExists(err);
        }
      } else {
        cbExists(null, { exists: true, description: data });
      }
    });
  };

  var create = function(r, cbCreate) {
    if (!r.exists) {
      client.createTable(r.definition, function(err, data) {
        if (err) {
          cbCreate(err);
        } else {
          cbCreate(null, {
            Table: {
              TableName: data.TableDescription.TableName,
              TableStatus: data.TableDescription.TableStatus
            }
          });
        }
      });
    } else {
      cbCreate(null, r.description);
    }
  };

  var active = function(d, cbActive) {
    var status = d.Table.TableStatus;
    async.until(
      function() {
        return status === 'ACTIVE';
      },
      function(cbUntil) {
        client.describeTable({ TableName: d.Table.TableName }, function(
          err,
          data
        ) {
          if (err) {
            cbUntil(err);
          } else {
            status = data.Table.TableStatus;
            setTimeout(cbUntil, 1000);
          }
        });
      },
      function(err, r) {
        if (err) {
          return cbActive(err);
        }
        cbActive(null, r);
      }
    );
  };

  async.compose(active, create, exists)(params, function(err, result) {
    if (err) callback(err);
    else callback(null, result);
  });
};

module.exports = DynamoDB;
```

## File: `lib/lock/databases/inmemory.js`
```javascript
var util = require('util'),
  Lock = require('../base'),
  _ = require('lodash');

function InMemory(options) {
  Lock.call(this, options);
  this.store = {};
}

util.inherits(InMemory, Lock);

_.extend(InMemory.prototype, {

  connect: function (callback) {
    this.emit('connect');
    if (callback) callback(null, this);
  },

  disconnect: function (callback) {
    this.emit('disconnect');
    if (callback) callback(null);
  },

  reserve: function(workerId, aggregateId, callback) {
    this.store[aggregateId] = this.store[aggregateId] || [];
    this.store[aggregateId].push(workerId);
    if (callback) callback(null);
  },

  getAll: function(aggregateId, callback) {
    if (callback) callback(null, this.store[aggregateId] || []);
  },

  resolve: function(aggregateId, callback) {
    if (this.store[aggregateId] !== undefined) delete this.store[aggregateId];
    if (callback) callback(null);
  },

  clear: function (callback) {
    this.store = {};
    if (callback) callback(null);
  }

});

module.exports = InMemory;
```

## File: `lib/lock/databases/mongodb.js`
```javascript
var util = require('util'),
  Lock = require('../base'),
  _ = require('lodash'),
  mongo = Lock.use('mongodb'),
  mongoVersion = Lock.use('mongodb/package.json').version,
  isNew = mongoVersion.indexOf('1.') !== 0,
  ObjectID = isNew ? mongo.ObjectID : mongo.BSONPure.ObjectID;

function Mongo(options) {
  Lock.call(this, options);

  var defaults = {
    host: 'localhost',
    port: 27017,
    dbName: 'domain',
    collectionName: 'aggregatelock'//,
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

util.inherits(Mongo, Lock);

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
        self.lock = self.db.collection(options.collectionName);
        self.lock.ensureIndex({ 'aggregateId': 1, date: 1 }, function() {});
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

  reserve: function(workerId, aggregateId, callback) {
    this.lock.save({ _id: workerId, aggregateId: aggregateId, date: new Date() }, { safe: true }, function (err) {
      if (callback) callback(err);
    });
  },

  getAll: function(aggregateId, callback) {
    this.lock.find({ aggregateId: aggregateId }, { sort: { date: 1 } }).toArray(function (err, res) {
      if (err) {
        return callback(err);
      }
      callback(null, _.map(res, function (entry) { return entry._id; }));
    });
  },

  resolve: function(aggregateId, callback) {
    this.lock.remove({ aggregateId: aggregateId }, { safe: true }, function (err) {
      if (callback) callback(err);
    });
  },

  clear: function (callback) {
    this.lock.remove({}, { safe: true }, callback);
  }

});

module.exports = Mongo;
```

## File: `lib/lock/databases/redis.js`
```javascript
var util = require('util'),
  Lock = require('../base'),
  _ = require('lodash'),
  async = require('async'),
  redis = Lock.use('redis');

function Redis(options) {
  Lock.call(this, options);

  var defaults = {
    host: 'localhost',
    port: 6379,
    prefix: 'aggregatelock',
    retry_strategy: function (options) {
      return undefined;
    }
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

util.inherits(Redis, Lock);

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

  reserve: function(workerId, aggregateId, callback) {
    var prefixedId = this.prefix + ':' + aggregateId;

    this.client.rpush(prefixedId, workerId, function (err) {
      if (callback) callback(err);
    });
  },

  getAll: function(aggregateId, callback) {
    var prefixedId = this.prefix + ':' + aggregateId;

    this.client.lrange(prefixedId, 0, -1, callback);
  },

  resolve: function(aggregateId, callback) {
    var prefixedId = this.prefix + ':' + aggregateId;

    this.client.del(prefixedId, function (err) {
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
      if (callback) callback(err);
    });
  }

});

module.exports = Redis;
```

## File: `lib/lock/databases/tingodb.js`
```javascript
var util = require('util'),
  Lock = require('../base'),
  _ = require('lodash'),
  tingodb = Lock.use('tingodb')(),
  ObjectID = tingodb.ObjectID;

function Tingo(options) {
  Lock.call(this, options);

  var defaults = {
    dbPath: require('path').join(__dirname, '/../../../'),
    collectionName: 'aggregatelock'
  };

  _.defaults(options, defaults);

  this.options = options;
}

util.inherits(Tingo, Lock);

_.extend(Tingo.prototype, {

  connect: function (callback) {
    var self = this;

    var options = this.options;

    this.db = new tingodb.Db(options.dbPath, {});
    // this.db.on('close', function() {
    //   self.emit('disconnect');
    // });
    this.lock = this.db.collection(options.collectionName + '.tingo');
    this.lock.ensureIndex({ 'aggregateId': 1, date: 1 }, function() {});

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

  reserve: function(workerId, aggregateId, callback) {
    this.lock.save({ _id: workerId, aggregateId: aggregateId, date: new Date() }, { safe: true }, function (err) {
      if (callback) callback(err);
    });
  },

  getAll: function(aggregateId, callback) {
    this.lock.find({ aggregateId: aggregateId }, { sort: { date: 1 } }).toArray(function (err, res) {
      if (err) {
        return callback(err);
      }
      callback(null, _.map(res, function (entry) { return entry._id; }));
    });
  },

  resolve: function(aggregateId, callback) {
    this.lock.remove({ aggregateId: aggregateId }, { safe: true }, function (err) {
      if (callback) callback(err);
    });
  },

  clear: function (callback) {
    this.lock.remove({}, { safe: true }, callback);
  }

});

module.exports = Tingo;
```

## File: `lib/structure/customLoader.js`
```javascript
var definitions = {
  Context: require('./../definitions/context'),
  Aggregate: require('./../definitions/aggregate'),
  Command: require('./../definitions/command'),
  Event: require('./../definitions/event'),
  BusinessRule: require('./../definitions/businessRule'),
  PreCondition: require('./../definitions/preCondition'),
  PreLoadCondition: require('./../definitions/preLoadCondition'),
  LoadingEventTransformer: require('./../definitions/loadingEventTransformer'),
  CommittingEventTransformer: require('./../definitions/committingEventTransformer'),
  CommandHandler: require('./../definitions/commandHandler'),
  errors: {
    BusinessRuleError: require('../errors/businessRuleError'),
    ValidationError: require('../errors/validationError'),
  }
}

module.exports = function (loader) {
  return function(domainPath, validatorExtension, useLoaderExtensions, callback) {
    var options = {
      domainPath: domainPath,
      definitions: definitions,
      validatorExtension: validatorExtension,
      useLoaderExtensions: useLoaderExtensions,
    };
    var tree;

    // async
    if (loader.length > 1) {
      return loader(options, callback);
    }

    // sync
    try {
      tree = loader(options);
    } catch(e) {
      return callback(e);
    }
    callback(null, tree);
  };
}
```

## File: `lib/structure/structureLoader.js`
```javascript
var debug = require('debug')('domain:structureLoader'),
  _ = require('lodash'),
  path = require('path'),
  structureParser = require('./structureParser'),
  Context = require('./../definitions/context'),
  Aggregate = require('./../definitions/aggregate'),
  Command = require('./../definitions/command'),
  Event = require('./../definitions/event'),
  BusinessRule = require('./../definitions/businessRule'),
  PreCondition = require('./../definitions/preCondition'),
  PreLoadCondition = require('./../definitions/preLoadCondition'),
  LoadingEventTransformer = require('./../definitions/loadingEventTransformer'),
  CommittingEventTransformer = require('./../definitions/committingEventTransformer'),
  CommandHandler = require('./../definitions/commandHandler');

function isSchema (item) {
  return item.fileType === 'json' && item.value.title;
}

function isContext (item) {
  if (item.fileType === 'json') {
    return false;
  }

  return item.value instanceof Context;
}

function isAggregate (item) {
  if (item.fileType === 'json') {
    return false;
  }

  return item.value instanceof Aggregate;
}

function isCommand (item) {
  if (item.fileType === 'json') {
    return false;
  }

  return item.value instanceof Command;
}

function isEvent (item) {
  if (item.fileType === 'json') {
    return false;
  }

  return item.value instanceof Event;
}

function isPreCondition (item) {
  if (item.fileType === 'json') {
    return false;
  }

  return item.value instanceof PreCondition;
}

function isPreLoadCondition (item) {
  if (item.fileType === 'json') {
    return false;
  }

  return item.value instanceof PreLoadCondition;
}

function isLoadingEventTransformer (item) {
  if (item.fileType === 'json') {
    return false;
  }

  return item.value instanceof LoadingEventTransformer;
}

function isCommittingEventTransformer (item) {
  if (item.fileType === 'json') {
    return false;
  }

  return item.value instanceof CommittingEventTransformer;
}

function isBusinessRule (item) {
  if (item.fileType === 'json') {
    return false;
  }

  return item.value instanceof BusinessRule;
}

function isCommandHandler (item) {
  if (item.fileType === 'json') {
    return false;
  }

  return item.value instanceof CommandHandler;
}

function defineNameOfSchema (item) {
  var name = item.value.title;
  if (!name) {
    var splits = item.dottiedBase.split('.');
    name = splits[splits.length - 1];
  }
  item.name = name;
}

function defineName (item, invert) {
  var name = item.value.name;

  if (name === '') {
    item.name = name;
    return;
  }

  function defineNameByDir () {
    if (!name) {
      var splits = item.dottiedBase.split('.');
      name = splits[splits.length - 1];
    }

    if (!name) {
      var tmp = item.path.substring(0, item.path.lastIndexOf(path.sep + item.fileName));
      name = tmp.substring(tmp.lastIndexOf(path.sep) + 1);
    }
  }

  function defineNameByFileName () {
    if (!name) {
      name = item.fileName.substring(0, item.fileName.lastIndexOf('.'));
    }
  }

  if (invert) {
    defineNameByDir();
    defineNameByFileName();
  } else {
    defineNameByFileName();
    defineNameByDir();
  }

  item.name = name;
}

function scan (items) {
  var res = {
    schemas: [],
    contexts: [],
    aggregates: [],
    commands: [],
    events: [],
    preConditions: [],
    preLoadConditions: [],
    businessRules: [],
    loadingEventTransformers: [],
    committingEventTransformers: [],
    commandHandlers: []
  };

  items.forEach(function (item) {
    if (isSchema(item)) {
      debug('found schema at: ' + item.path);
      defineNameOfSchema(item);
      res.schemas.push(item);
      return;
    }

    if (isContext(item)) {
      debug('found context at: ' + item.path);
      defineName(item, true);
      item.value.name = item.name;
      res.contexts.push(item);
      return;
    }

    if (isAggregate(item)) {
      debug('found aggregate at: ' + item.path);
      defineName(item, true);
      item.value.name = item.name;
      res.aggregates.push(item);
      return;
    }

    if (isCommand(item)) {
      debug('found command at: ' + item.path);
      defineName(item);
      item.value.name = item.name;
      res.commands.push(item);
      return;
    }

    if (isEvent(item)) {
      debug('found event at: ' + item.path);
      defineName(item);
      item.value.name = item.name;
      res.events.push(item);
      return;
    }

    if (isBusinessRule(item)) {
      debug('found businessRule at: ' + item.path);
      defineName(item);
      item.value.name = item.name;
      res.businessRules.push(item);
      return;
    }

    if (isLoadingEventTransformer(item)) {
      debug('found loadingEventTransformer at: ' + item.path);
      defineName(item);
      item.value.name = item.name;
      res.loadingEventTransformers.push(item);
      return;
    }

    if (isCommittingEventTransformer(item)) {
      debug('found committingEventTransformer at: ' + item.path);
      defineName(item);
      item.value.name = item.name;
      res.committingEventTransformers.push(item);
      return;
    }

    if (isPreCondition(item)) {
      debug('found preCondition at: ' + item.path);
      defineName(item);
      if (!_.isArray(item.name)) {
        item.name = [item.name];
      }
      item.value.name = item.name;
      res.preConditions.push(item);
      return;
    }

    if (isCommandHandler(item)) {
      debug('found commandHandler at: ' + item.path);
      defineName(item);
      item.value.name = item.name;
      res.commandHandlers.push(item);
      return;
    }

    if (isPreLoadCondition(item)) {
      debug('found preLoadCondition at: ' + item.path);
      defineName(item);
      if (!_.isArray(item.name)) {
        item.name = [item.name];
      }
      item.value.name = item.name;
      res.preLoadConditions.push(item);
      return;
    }
  });



  return res;
}

function analyze (dir, useLoaderExtensions, callback) {
  structureParser(dir, useLoaderExtensions, function (items) {
    return _.filter(items, function (i) {
      return isSchema(i) || isContext(i) || isAggregate(i) || isCommand(i) || isEvent(i) || isBusinessRule(i) || isPreCondition(i) || isPreLoadCondition(i) || isCommandHandler(i) || isLoadingEventTransformer(i) || isCommittingEventTransformer(i);
    });
  }, function (err, items, warns) {
    if (err) {
      return callback(err);
    }

    var res = scan(items);

    callback(null, res, warns);
  });
}

function reorderExternallyLoadedContexts (obj, ordered) {
  obj.contexts.forEach(function (ctxItem) {
    if (!ctxItem.value.externallyLoaded)
      return;
      ordered[ctxItem.name] = ctxItem.value;
  });
}

function reorderAggregates (obj, ordered) {
  var generalContext = new Context({ name: '_general' });

  obj.aggregates.forEach(function (aggItem) {
    var foundCtx = _.find(obj.contexts, function (ctx) {
      if (ctx.value.externallyLoaded) {
        return false;
      }
      if (aggItem.dottiedBase.indexOf('.') >= 0) {
        return aggItem.dottiedBase.indexOf(ctx.dottiedBase + '.') === 0;
      } else {
        return aggItem.dottiedBase === ctx.dottiedBase;
      }
    });

    if (!foundCtx) {
      foundCtx = _.find(obj.contexts, function (ctx) {
        if (ctx.value.externallyLoaded) {
          return false;
        }
        return ctx.dottiedBase === '';
      });
    }

    var ctxName = '_general';
    if (foundCtx) {
      ctxName = foundCtx.name;
      ordered[ctxName] = ordered[ctxName] || foundCtx.value;
    } else {
      ordered[ctxName] = ordered[ctxName] || generalContext;
    }
    ordered[ctxName].addAggregate(aggItem.value);

    // mark context for aggregate
    aggItem.context = ctxName;
  });
}

function reorderDefault (obj, ordered, what) {
  obj[what + 's'].forEach(function (objItem) {
    var foundAggr = _.find(obj.aggregates, function (aggr) {
      if (objItem.dottiedBase.indexOf('.') >= 0) {
        return objItem.dottiedBase.indexOf(aggr.dottiedBase + '.') === 0;
      } else {
        return objItem.dottiedBase === aggr.dottiedBase;
      }
    });

    if (!foundAggr) {
      return;
    }

    var whatCap = what.charAt(0).toUpperCase() + what.slice(1);

    var agg = ordered[foundAggr.context].getAggregate(foundAggr.name);

    agg['add' + whatCap].call(agg, objItem.value);

    // mark context and aggregate
    objItem.context = foundAggr.context;
    objItem.aggregate = foundAggr.name;
  });
}

function reorderCommands (obj, ordered) {
  reorderDefault(obj, ordered, 'command');
}

function reorderEvents (obj, ordered) {
  reorderDefault(obj, ordered, 'event');
}

function reorderBusinessRules (obj, ordered) {
  reorderDefault(obj, ordered, 'businessRule');
}

function reorderCommandHandlers (obj, ordered) {
  reorderDefault(obj, ordered, 'commandHandler');
}

function reorderLoadingEventTransformers (obj, ordered) {
  reorderDefault(obj, ordered, 'loadingEventTransformer');
}

function reorderCommittingEventTransformers (obj, ordered) {
  reorderDefault(obj, ordered, 'committingEventTransformer');
}

function preorderPreConditions (obj, ordered) {
  obj.preConditions.forEach(function (objItem) {
    var foundAggr = _.find(obj.aggregates, function (aggr) {
      if (objItem.dottiedBase.indexOf('.') >= 0) {
        return objItem.dottiedBase.indexOf(aggr.dottiedBase + '.') === 0;
      } else {
        return objItem.dottiedBase === aggr.dottiedBase;
      }
    });

    if (!foundAggr) {
      return;
    }

    // mark context and aggregate
    objItem.context = foundAggr.context;
    objItem.aggregate = foundAggr.name;
  });
}

function reorderPreConditions (obj, ordered) {
  preorderPreConditions(obj, ordered);

  obj.preConditions.forEach(function (pc) {

    var foundCmds = _.filter(obj.commands, function (cmd) {
      return pc.context === cmd.context &&
             pc.aggregate === cmd.aggregate &&
            (pc.name.indexOf(cmd.name) >= 0 || pc.name.indexOf('') >= 0) &&
            (pc.name.indexOf('') >= 0 || pc.version === cmd.version);
    });

    if (!foundCmds || foundCmds.length === 0) {
      if (pc.name.length > 0) {
        debug('no cmd found for ',  pc.name);
        return;
      }
      return;
    }

    foundCmds.forEach(function (foundCmd) {
      foundCmd.value.addPreCondition(pc.value);
    });
  });
}

function preorderPreLoadConditions (obj, ordered) {
  obj.preLoadConditions.forEach(function (objItem) {
    var foundAggr = _.find(obj.aggregates, function (aggr) {
      if (objItem.dottiedBase.indexOf('.') >= 0) {
        return objItem.dottiedBase.indexOf(aggr.dottiedBase + '.') === 0;
      } else {
        return objItem.dottiedBase === aggr.dottiedBase;
      }
    });

    if (!foundAggr) {
      return;
    }

    // mark context and aggregate
    objItem.context = foundAggr.context;
    objItem.aggregate = foundAggr.name;
  });
}

function reorderPreLoadConditions (obj, ordered) {
  preorderPreLoadConditions(obj, ordered);

  obj.preLoadConditions.forEach(function (plc) {

    var foundCmds = _.filter(obj.commands, function (cmd) {
      return plc.context === cmd.context &&
        plc.aggregate === cmd.aggregate &&
        (plc.name.indexOf(cmd.name) >= 0 || plc.name.indexOf('') >= 0) &&
        (plc.name.indexOf('') >= 0 || plc.version === cmd.version);
    });

    if (!foundCmds || foundCmds.length === 0) {
      if (plc.name.length > 0) {
        debug('no cmd found for ',  plc.name);
        return;
      }
      return;
    }

    foundCmds.forEach(function (foundCmd) {
      foundCmd.value.addPreLoadCondition(plc.value);
    });
  });
}

function reorderValidationRules (obj, ordered, validatorExtension) {
  var allSchemas = {};
  var cmdSchemas = [];

  obj.schemas.forEach(function (schemaItem) {

    allSchemas['/' + schemaItem.name] = schemaItem.value;

    var foundCtx = _.find(obj.contexts, function (ctx) {
      return schemaItem.dottiedBase.indexOf(ctx.dottiedBase) === 0;
    });
    if (foundCtx) {
      schemaItem.context = foundCtx.name;
    } else {
      schemaItem.context = '_general';
    }

    var foundAggr = _.find(obj.aggregates, function (aggr) {
      if (schemaItem.dottiedBase.indexOf('.') >= 0) {
        return schemaItem.dottiedBase.indexOf(aggr.dottiedBase + '.') === 0;
      } else {
        return schemaItem.dottiedBase === aggr.dottiedBase;
      }
    });

    if (foundAggr) {
      schemaItem.aggregate = foundAggr.name;
    }

    if (!schemaItem.context || (schemaItem.context === '_general' && schemaItem.dottiedBase === '' && !schemaItem.aggregate)) {
      // it's a general schema
      return;
    }

    if (foundCtx && foundCtx.dottiedBase === schemaItem.dottiedBase && schemaItem.context !== '_general') {
      // it's a context schema
      return;
    }

    if (!schemaItem.aggregate) {
      debug('no aggregate found for schema: ' + schemaItem.path);
      // skip
      return;
    }

    if (foundAggr.dottiedBase === schemaItem.dottiedBase) {
      var foundPossibleCommand = _.find(foundAggr.value.commands, 'name', schemaItem.value.title);
      if (!foundPossibleCommand) {
        // it's an aggregate schema
        return;
      }
    }

    cmdSchemas.push(schemaItem);
  });

  var formats = {};

  var getValidatorFn = require('./../validator');

  var validator = {
    addFormat: function (key, value) {
      if (!key) {
        var err = new Error('Please pass valid arguments!');
        debug(err);
        throw err;
      }

      if (!value) {
        _.forOwn(key, function (v, k) {
          formats[k] = v;
        });
      } else {
        formats[key] = value;
      }
    },
    addSchema: function (key, value) {
      if (!key) {
        var err = new Error('Please pass valid arguments!');
        debug(err);
        throw err;
      }

      if (!value) {
        _.forOwn(key, function (v, k) {
          allSchemas[k] = v;
        });
      } else {
        allSchemas[key] = value;
      }
    },
    validator: function (fn) {
      if (!fn || !_.isFunction(fn)) {
        var err = new Error('Please pass a valid function!');
        debug(err);
        throw err;
      }

      getValidatorFn = fn;
    }
  };

  validatorExtension(validator);

  cmdSchemas.forEach(function (schemaItem) {
    // check for all commands, if nothing found continue...
    obj.commands.forEach(function (cmdItem) {
      if (cmdItem.name === schemaItem.name &&
        cmdItem.aggregate === schemaItem.aggregate &&
        cmdItem.context === schemaItem.context &&
        ((schemaItem.value.version === undefined || schemaItem.value.version === null) || cmdItem.value.version === schemaItem.value.version)) {
        var cmd = ordered[schemaItem.context].getAggregate(schemaItem.aggregate).getCommand(schemaItem.name, schemaItem.value.version);
        // it's a command schema
        cmd.defineValidation(getValidatorFn({ schemas: allSchemas, formats: formats }, schemaItem.value));
      }
    });
  });
}

function reorder (obj, validatorExtension) {
  var ordered = {};

  reorderExternallyLoadedContexts(obj, ordered);

  reorderAggregates(obj, ordered);

  reorderCommands(obj, ordered);

  reorderEvents(obj, ordered);

  reorderBusinessRules(obj, ordered);

  reorderCommandHandlers(obj, ordered);

  reorderValidationRules(obj, ordered, validatorExtension);

  reorderPreLoadConditions(obj, ordered);

  reorderPreConditions(obj, ordered);

  reorderLoadingEventTransformers(obj, ordered);

  reorderCommittingEventTransformers(obj, ordered);

  if (!ordered || _.isEmpty(ordered)) {
    debug('analyzed: ', obj);
    debug('ordered: ', ordered);
  }

  return ordered;
}

function load (dir, validatorExtension, useLoaderExtensions, callback) {
  analyze(dir, useLoaderExtensions, function (err, dividedByTypes, warns) {
    if (err) {
      return callback(err);
    }

    var structured = reorder(dividedByTypes, validatorExtension);

    callback(err, structured, warns);
  });
}

module.exports = load;
```

## File: `lib/structure/structureParser.js`
```javascript
var debug = require('debug')('domain:structureParser'),
  _ = require('lodash'),
  fs = require('fs'),
  path = require('path');

var validFileTypes = ['js', 'json'];

function isValidFileType(fileName) {
  var index = fileName.lastIndexOf('.');
  if (index < 0) {
    return false;
  }
  var fileType = fileName.substring(index + 1);
  var index = validFileTypes.indexOf(fileType);
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

function parse (dir, useLoaderExtensions, filter, callback) {
  if (!callback) {
    callback = filter;
    filter = function (r) {
      return r;
    };
  }

  if (useLoaderExtensions) {
    validFileTypes = Object.keys(require.extensions)
      .map(function (ext) {
        return ext.substr(1);
      });

    debug('Using valid file types from loader extensions');
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

## File: `lib/structure/treeExtender.js`
```javascript
var debug = require('debug')('domain:treeExtender'),
  _ = require('lodash'),
  Context = require('../definitions/context');

function getCommandHandler (ctx, query) {
  var aggr;
  if (query.aggregate) {
    aggr = ctx.getAggregate(query.aggregate);
  } else {
    aggr = ctx.getAggregateForCommand(query.name, query.version);
  }

  if (!aggr) {
    return null;
  }

  return aggr.getCommandHandler(query.name, query.version);
}

// function getCommandHandlerByOldTarget (ctx, query) {
//   var aggr = ctx.getAggregateForCommandByOldTarget(query);
//
//   if (!aggr) {
//     return null;
//   }
//
//   return aggr.getCommandHandler(query.name, query.version);
// }

module.exports = function (tree) {

  if (!tree || _.isEmpty(tree)) {
    debug('no tree injected');
  }

  return {

    getInfo: function () {
      if (!tree || _.isEmpty(tree)) {
        debug('no tree injected');
        return null;
      }

      var ctxs = this.getContexts();

      var info = {
        contexts: []
      };

      ctxs.forEach(function (ctx) {
        var c = { name: ctx.name, aggregates: [] };

        ctx.aggregates.forEach(function (aggr) {
          var a = { name: aggr.name, version: aggr.version, commands: [], events: [], businessRules: [] };

          aggr.commands.forEach(function (command) {
            var cmd = { name: command.name, version: command.version, preConditions: [], preLoadConditions: [] };
            // if (command.source && command.source.aggregate) {
            //   cmd.source = command.source;
            // }
            command.preConditions.forEach(function (pc) {
              var n = pc.name.join(', ');
              cmd.preConditions.push({ name: n, description: pc.description, priority: pc.priority });
            });

            command.preLoadConditions.forEach(function (pc) {
              var n = pc.name.join(', ');
              cmd.preLoadConditions.push({ name: n, description: pc.description, priority: pc.priority });
            });

            a.commands.push(cmd);
          });

          aggr.events.forEach(function (event) {
            a.events.push({ name: event.name, version: event.version });
          });

          aggr.businessRules.forEach(function (businessRule) {
            a.businessRules.push({ name: businessRule.name, description: businessRule.description, priority: businessRule.priority });
          });

          c.aggregates.push(a);
        });

        info.contexts.push(c);
      });

      return info;
    },

    getContexts: function () {
      if (!tree || _.isEmpty(tree)) {
        debug('no tree injected');
        return null;
      }

      var ctxs = [];
      for (var c in tree) {
        var ctx = tree[c];
        if (ctx instanceof Context) {
          ctxs.push(ctx);
        }
      }
      return ctxs;
    },

    getContext: function (name) {
      if (!tree || _.isEmpty(tree)) {
        debug('no tree injected');
        return null;
      }

      var ctx = tree[name];
      if (ctx instanceof Context) {
        return ctx;
      }
      return null;
    },

    getCommandHandler: function (query) {
      if (!tree || _.isEmpty(tree)) {
        debug('no tree injected');
        return null;
      }

      var ctx;
      if (query.context) {
        ctx = this.getContext(query.context);
        if (!ctx) {
          debug('no context found with name ' + query.context);
          return null;
        }
        return getCommandHandler(ctx, query);
      } else {
        var ctxs = this.getContexts();
        for (var c in ctxs) {
          ctx = ctxs[c];
          var handler = getCommandHandler(ctx, query);
          if (handler) {
            return handler;
          }
        }
      }
      return null;
    },

    // getCommandHandlerByOldTarget: function (query) {
    //   if (!tree || _.isEmpty(tree)) {
    //     debug('no tree injected');
    //     return null;
    //   }
    //
    //   var ctx;
    //   var ctxs = this.getContexts();
    //   for (var c in ctxs) {
    //     ctx = ctxs[c];
    //     var handler = getCommandHandlerByOldTarget(ctx, query);
    //     if (handler) {
    //       return handler;
    //     }
    //   }
    //   return null;
    // },

    defineOptions: function (options) {
      if (!tree || _.isEmpty(tree)) {
        debug('no tree injected');
        return this;
      }

      this.getContexts().forEach(function (ctx) {
        ctx.defineOptions(options);

        ctx.getAggregates().forEach(function (aggr) {
          aggr.defineOptions(options);

          if (aggr.defaultCommandHandler) {
            aggr.defaultCommandHandler.defineOptions(options);
          }

          aggr.getCommands().forEach(function (cmd) {
            cmd.defineOptions(options);

            if (cmd.preCondition) {
              cmd.preCondition.defineOptions(options);
            }

            if (cmd.preLoadCondition) {
              cmd.preLoadCondition.defineOptions(options);
            }
          });

          aggr.getEvents().forEach(function (evt) {
            evt.defineOptions(options);
          });

          aggr.getCommandHandlers().forEach(function (cmdHndl) {
            cmdHndl.defineOptions(options);
          });

          aggr.getBusinessRules().forEach(function (buRu) {
            buRu.defineOptions(options);
          });
        });
      });
      return this;
    },

    defineCommand: function (definition) {
      if (!tree || _.isEmpty(tree)) {
        debug('no tree injected');
        return this;
      }

      this.getContexts().forEach(function (ctx) {
        ctx.defineCommand(definition);

        ctx.getAggregates().forEach(function (aggr) {
          aggr.defineCommand(definition);

          if (aggr.defaultCommandHandler) {
            aggr.defaultCommandHandler.defineCommand(definition);
          }

          aggr.getCommands().forEach(function (cmd) {
            cmd.defineCommand(definition);
          });

          aggr.getEvents().forEach(function (evt) {
            evt.defineCommand(definition);
          });

          aggr.getCommandHandlers().forEach(function (cmdHndl) {
            cmdHndl.defineCommand(definition);
          });

          aggr.getBusinessRules().forEach(function (buRu) {
            buRu.defineCommand(definition);
          });
        });
      });
      return this;
    },

    defineEvent: function (definition) {
      if (!tree || _.isEmpty(tree)) {
        debug('no tree injected');
        return this;
      }

      this.getContexts().forEach(function (ctx) {
        ctx.defineEvent(definition);

        ctx.getAggregates().forEach(function (aggr) {
          aggr.defineEvent(definition);

          if (aggr.defaultCommandHandler) {
            aggr.defaultCommandHandler.defineEvent(definition);
          }

          aggr.getCommands().forEach(function (cmd) {
            cmd.defineEvent(definition);

            if (cmd.preCondition) {
              cmd.preCondition.defineEvent(definition);
            }

            if (cmd.preLoadCondition) {
              cmd.preLoadCondition.defineEvent(definition);
            }
          });

          aggr.getEvents().forEach(function (evt) {
            evt.defineEvent(definition);
          });

          aggr.getCommandHandlers().forEach(function (cmdHndl) {
            cmdHndl.defineEvent(definition);
          });

          aggr.getBusinessRules().forEach(function (buRu) {
            buRu.defineEvent(definition);
          });
        });
      });
      return this;
    },

    useEventStore: function (eventStore) {
      if (!tree || _.isEmpty(tree)) {
        debug('no tree injected');
        return this;
      }

      this.getContexts().forEach(function (ctx) {
        ctx.getAggregates().forEach(function (aggr) {
          if (aggr.defaultCommandHandler) {
            aggr.defaultCommandHandler.useEventStore(eventStore);
          }
          aggr.getCommandHandlers().forEach(function (cmdHndl) {
            cmdHndl.useEventStore(eventStore);
          });
        });
      });
      return this;
    },

    useAggregateLock: function (aggregateLock) {
      if (!tree || _.isEmpty(tree)) {
        debug('no tree injected');
        return this;
      }

      this.getContexts().forEach(function (ctx) {
        ctx.getAggregates().forEach(function (aggr) {
          if (aggr.defaultCommandHandler) {
            aggr.defaultCommandHandler.useAggregateLock(aggregateLock);
          }
          aggr.getCommandHandlers().forEach(function (cmdHndl) {
            cmdHndl.useAggregateLock(aggregateLock);
          });
        });
      });
      return this;
    },

    idGenerator: function (getNewId) {
      if (!getNewId || !_.isFunction(getNewId)) {
        var err = new Error('Please pass a valid function!');
        debug(err);
        throw err;
      }

      if (!tree || _.isEmpty(tree)) {
        debug('no tree injected');
        return this;
      }

      this.getContexts().forEach(function (ctx) {
        ctx.getAggregates().forEach(function (aggr) {
          aggr.idGenerator(getNewId);
        });
      });
      return this;
    },

    aggregateIdGenerator: function (getNewId) {
      if (!getNewId || !_.isFunction(getNewId)) {
        var err = new Error('Please pass a valid function!');
        debug(err);
        throw err;
      }

      if (!tree || _.isEmpty(tree)) {
        debug('no tree injected');
        return this;
      }

      this.getContexts().forEach(function (ctx) {
        ctx.getAggregates().forEach(function (aggr) {
          if (aggr.defaultCommandHandler) {
            aggr.defaultCommandHandler.aggregateIdGenerator(getNewId);
          }
          aggr.getCommandHandlers().forEach(function (cmdHndl) {
            cmdHndl.aggregateIdGenerator(getNewId);
          });
        });
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
-R spec -t 20000
```

## File: `test/integration/integrationTest.js`
```javascript
var expect = require('expect.js'),
  uuid = require('uuid').v4,
  api = require('../../index');

describe('integration', function () {

  describe('set 1', function () {

    describe('format 1', function () {

      var domain;

      before(function (done) {
        domain = api({ domainPath: __dirname + '/fixture/set1', commandRejectedEventName: 'rejectedCommand', deduplication: {} });
        domain.defineCommand({
          id: 'id',
          name: 'name',
          aggregateId: 'aggregate.id',
          context: 'context.name',
          aggregate: 'aggregate.name',
          payload: 'payload',
          revision: 'revision',
          version: 'version',
          meta: 'meta'
        });
        domain.defineEvent({
          correlationId: 'correlationId',
          id: 'id',
          name: 'name',
          aggregateId: 'aggregate.id',
          context: 'context.name',
          aggregate: 'aggregate.name',
          payload: 'payload',
          revision: 'revision',
          version: 'version',
          meta: 'meta'
        });

        expect(function () {
          domain.getInfo();
        }).to.throwError('/init');

        expect(function () {
          domain.extendValidator(function () {});
        }).to.throwError();

        domain.extendValidator(function (validator) {
          // expect(validator.addFormat('mySpecialFormat', function (data) {
          //   return data === 'special';
          // }));
          expect(validator.addFormat('mySpecialFormat', function (data) {
           if (data === 'special') {
             return null;
           }
           return 'wrong format for special';
          }));
        });

        domain.init(function (err, warns) {
          expect(warns).not.to.be.ok();
          done(err);
        });
      });

      describe('requesting information', function () {

        it('it should return the expected information', function () {

          var info = domain.getInfo();
          expect(info.contexts.length).to.eql(2);
          expect(info.contexts[0].name).to.eql('_general');
          expect(info.contexts[0].aggregates.length).to.eql(1);
          expect(info.contexts[0].aggregates[0].name).to.eql('cart');
          expect(info.contexts[0].aggregates[0].version).to.eql(0);
          expect(info.contexts[0].aggregates[0].commands.length).to.eql(1);
          expect(info.contexts[0].aggregates[0].commands[0].name).to.eql('enterNewPerson');
          expect(info.contexts[0].aggregates[0].commands[0].version).to.eql(0);
          expect(info.contexts[0].aggregates[0].events.length).to.eql(1);
          expect(info.contexts[0].aggregates[0].events[0].name).to.eql('enteredNewPerson');
          expect(info.contexts[0].aggregates[0].events[0].version).to.eql(3);
          expect(info.contexts[0].aggregates[0].businessRules.length).to.eql(0);

          expect(info.contexts[1].name).to.eql('hr');
          expect(info.contexts[1].aggregates.length).to.eql(1);
          expect(info.contexts[1].aggregates[0].name).to.eql('person');
          expect(info.contexts[1].aggregates[0].version).to.eql(3);
          expect(info.contexts[1].aggregates[0].commands.length).to.eql(3);
          expect(info.contexts[1].aggregates[0].commands[0].name).to.eql('enterNewPerson');
          expect(info.contexts[1].aggregates[0].commands[0].version).to.eql(0);
          expect(info.contexts[1].aggregates[0].commands[0].preConditions.length).to.eql(2);
          expect(info.contexts[1].aggregates[0].commands[0].preConditions[0].name).to.eql('');
          expect(info.contexts[1].aggregates[0].commands[0].preConditions[0].description).to.eql('authorization');
          expect(info.contexts[1].aggregates[0].commands[0].preConditions[0].priority).to.eql(1);
          expect(info.contexts[1].aggregates[0].commands[0].preConditions[1].name).to.eql('');
          expect(info.contexts[1].aggregates[0].commands[0].preConditions[1].description).to.eql('Fails if firstname is rumpelstilz');
          expect(info.contexts[1].aggregates[0].commands[0].preConditions[1].priority).to.eql(1);
          expect(info.contexts[1].aggregates[0].commands[0].preLoadConditions.length).to.eql(1);
          expect(info.contexts[1].aggregates[0].commands[0].preLoadConditions[0].name).to.eql('');
          expect(info.contexts[1].aggregates[0].commands[0].preLoadConditions[0].description).to.eql('just a nice little test');
          expect(info.contexts[1].aggregates[0].commands[0].preLoadConditions[0].priority).to.eql(1);
          expect(info.contexts[1].aggregates[0].commands[1].name).to.eql('unregisterAllContactInformation');
          expect(info.contexts[1].aggregates[0].commands[1].version).to.eql(2);
          expect(info.contexts[1].aggregates[0].commands[1].preConditions.length).to.eql(3);
          expect(info.contexts[1].aggregates[0].commands[1].preConditions[0].name).to.eql('');
          expect(info.contexts[1].aggregates[0].commands[1].preConditions[0].description).to.eql('authorization');
          expect(info.contexts[1].aggregates[0].commands[1].preConditions[0].priority).to.eql(1);
          expect(info.contexts[1].aggregates[0].commands[1].preConditions[1].name).to.eql('');
          expect(info.contexts[1].aggregates[0].commands[1].preConditions[1].description).to.eql('Fails if firstname is rumpelstilz');
          expect(info.contexts[1].aggregates[0].commands[1].preConditions[1].priority).to.eql(1);
          expect(info.contexts[1].aggregates[0].commands[1].preConditions[2].name).to.eql('unregisterAllContactInformation');
          expect(info.contexts[1].aggregates[0].commands[1].preConditions[2].description).to.eql('firstname should always be set');
          expect(info.contexts[1].aggregates[0].commands[1].preConditions[2].priority).to.eql(2);
          expect(info.contexts[1].aggregates[0].commands[1].preLoadConditions.length).to.eql(1);
          expect(info.contexts[1].aggregates[0].commands[1].preLoadConditions[0].name).to.eql('');
          expect(info.contexts[1].aggregates[0].commands[1].preLoadConditions[0].description).to.eql('just a nice little test');
          expect(info.contexts[1].aggregates[0].commands[1].preLoadConditions[0].priority).to.eql(1);
          expect(info.contexts[1].aggregates[0].commands[2].name).to.eql('unregisterAllContactInformation');
          expect(info.contexts[1].aggregates[0].commands[2].version).to.eql(1);
          expect(info.contexts[1].aggregates[0].commands[2].preConditions.length).to.eql(3);
          expect(info.contexts[1].aggregates[0].commands[2].preConditions[0].name).to.eql('');
          expect(info.contexts[1].aggregates[0].commands[2].preConditions[0].description).to.eql('authorization');
          expect(info.contexts[1].aggregates[0].commands[2].preConditions[0].priority).to.eql(1);
          expect(info.contexts[1].aggregates[0].commands[2].preConditions[1].name).to.eql('');
          expect(info.contexts[1].aggregates[0].commands[2].preConditions[1].description).to.eql('Fails if firstname is rumpelstilz');
          expect(info.contexts[1].aggregates[0].commands[2].preConditions[1].priority).to.eql(1);
          expect(info.contexts[1].aggregates[0].commands[2].preConditions[2].name).to.eql('unregisterAllContactInformation');
          expect(info.contexts[1].aggregates[0].commands[2].preConditions[2].description).to.eql('firstname should always be set');
          expect(info.contexts[1].aggregates[0].commands[2].preConditions[2].priority).to.eql(2);
          expect(info.contexts[1].aggregates[0].commands[2].preLoadConditions.length).to.eql(1);
          expect(info.contexts[1].aggregates[0].commands[2].preLoadConditions[0].name).to.eql('');
          expect(info.contexts[1].aggregates[0].commands[2].preLoadConditions[0].description).to.eql('just a nice little test');
          expect(info.contexts[1].aggregates[0].commands[2].preLoadConditions[0].priority).to.eql(1);
          expect(info.contexts[1].aggregates[0].events.length).to.eql(5);
          expect(info.contexts[1].aggregates[0].events[0].name).to.eql('enteredNewPerson');
          expect(info.contexts[1].aggregates[0].events[0].version).to.eql(3);
          expect(info.contexts[1].aggregates[0].events[1].name).to.eql('enteredNewPerson');
          expect(info.contexts[1].aggregates[0].events[1].version).to.eql(0);
          expect(info.contexts[1].aggregates[0].events[2].name).to.eql('enteredNewPerson');
          expect(info.contexts[1].aggregates[0].events[2].version).to.eql(2);
          expect(info.contexts[1].aggregates[0].events[3].name).to.eql('unregisteredEMailAddress');
          expect(info.contexts[1].aggregates[0].events[3].version).to.eql(0);
          expect(info.contexts[1].aggregates[0].events[4].name).to.eql('unregisteredPhoneNumber');
          expect(info.contexts[1].aggregates[0].events[4].version).to.eql(0);
          expect(info.contexts[1].aggregates[0].businessRules.length).to.eql(2);
          expect(info.contexts[1].aggregates[0].businessRules[0].name).to.eql('atLeast1EMail');
          expect(info.contexts[1].aggregates[0].businessRules[0].description).to.eql('at least one character should be in email address');
          expect(info.contexts[1].aggregates[0].businessRules[1].name).to.eql('nameEquality');
          expect(info.contexts[1].aggregates[0].businessRules[1].description).to.eql('firstname should never be equal lastname');

        });

      });

      describe('handling a command that is not a json object', function () {

        it('it should not publish any event and it should callback with an error and without events', function (done) {

          var publishedEvents = [];

          domain.onEvent(function (evt) {
            publishedEvents.push(evt);
          });

          domain.handle('crappy', function (err, evts) {
            expect(err).to.be.ok();
            expect(err.message).to.match(/valid/i);
            expect(evts).not.to.be.ok();
            expect(publishedEvents.length).to.eql(0);

            done();
          });

        });

      });

      describe('handling a command that has no name', function () {

        it('it should not publish any event and it should callback with an error and without events', function (done) {

          var publishedEvents = [];

          domain.onEvent(function (evt) {
            publishedEvents.push(evt);
          });

          var cmd = {
            id: uuid().toString(),
//            name: 'cmdName',
            aggregate: {
              id: 'aggregateId',
              name: 'aggregate'
            },
            context: {
              name: 'context'
            },
            payload: 'payload',
            revision: 0,
            version: 0,
            meta: {
              userId: 'userId'
            }
          };

          domain.handle(cmd, function (err, evts) {
            expect(err).to.be.ok();
            expect(err.message).to.match(/valid/i);
            expect(evts).not.to.be.ok();
            expect(publishedEvents.length).to.eql(0);

            done();
          });

        });

      });

      describe('handling a command that will not be handled', function () {

        it('it should not publish any event and it should callback with an error and without events', function (done) {

          var publishedEvents = [];

          domain.onEvent(function (evt) {
            publishedEvents.push(evt);
          });

          var cmd = {
            id: uuid().toString(),
            name: 'cmdName',
            aggregate: {
              id: 'aggregateId',
              name: 'aggregate'
            },
            context: {
              name: 'context'
            },
            payload: 'payload',
            revision: 0,
            version: 0,
            meta: {
              userId: 'userId'
            }
          };

          domain.handle(cmd, function (err, evts) {
            expect(err).to.be.ok();
            expect(err.message).to.match(/found/i);
            expect(evts).not.to.be.ok();
            expect(publishedEvents.length).to.eql(0);

            done();
          });

        });

      });

      describe('handling a command with correct command name but wrong aggregate and context', function () {

        it('it should not publish any event and it should callback with an error and without events', function (done) {

          var publishedEvents = [];

          domain.onEvent(function (evt) {
            publishedEvents.push(evt);
          });

          var cmd = {
            id: uuid().toString(),
            name: 'enterNewPerson',
            aggregate: {
              id: 'aggregateId',
              name: 'aggregate'
            },
            context: {
              name: 'context'
            },
            payload: 'payload',
            revision: 0,
            version: 0,
            meta: {
              userId: 'userId'
            }
          };

          domain.handle(cmd, function (err, evts) {
            expect(err).to.be.ok();
            expect(err.message).to.match(/found/i);
            expect(evts).not.to.be.ok();
            expect(publishedEvents.length).to.eql(0);

            done();
          });

        });

      });

      describe('handling a command with correct command name and correct aggregate but wrong context', function () {

        it('it should not publish any event and it should callback with an error and without events', function (done) {

          var publishedEvents = [];

          domain.onEvent(function (evt) {
            publishedEvents.push(evt);
          });

          var cmd = {
            id: uuid().toString(),
            name: 'enterNewPerson',
            aggregate: {
              id: 'aggregateId',
              name: 'person'
            },
            context: {
              name: 'context'
            },
            payload: 'payload',
            revision: 0,
            version: 0,
            meta: {
              userId: 'userId'
            }
          };

          domain.handle(cmd, function (err, evts) {
            expect(err).to.be.ok();
            expect(err.message).to.match(/found/i);
            expect(evts).not.to.be.ok();
            expect(publishedEvents.length).to.eql(0);

            done();
          });

        });

      });

      describe('handling a command', function () {

        describe('that does fails on the validation rules of a parent schema', function () {

          it('it should publish a command rejected event and it should callback with an error and without events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              idd: 'cmdId',
              name: 'enterNewPerson',
              aggregate: {
                id: 'aggregateId',
                name: 'person'
              },
              context: {
                name: 'hr'
              },
              payload: {
                firstname: 'jack',
                lastname: 'doe',
                email: 'jack'
              },
              revision: 0,
              version: 0,
              meta: {
                userId: 'userId'
              }
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).to.be.ok();
              expect(err.name).to.eql('ValidationError');
              expect(evts).to.be.an('array');
              expect(evts.length).to.eql(1);
              expect(evts[0].name).to.eql('rejectedCommand');
              expect(evts[0].payload.reason.name).to.eql('ValidationError');
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].name).to.eql('rejectedCommand');
              expect(publishedEvents[0].payload.reason.name).to.eql('ValidationError');

              expect(aggData).to.eql(null);
              expect(meta.aggregateId).to.eql('aggregateId');
              expect(meta.aggregate).to.eql('person');
              expect(meta.context).to.eql('hr');

              done();
            });

          });

        });

        describe('that fails on the validation rules of a custom format', function () {

          it('it should publish a command rejected event and it should callback with an error and without events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              id: uuid().toString(),
              name: 'enterNewPerson',
              aggregate: {
                id: 'aggregateId',
                name: 'person'
              },
              context: {
                name: 'hr'
              },
              special: 'spec',
              payload: {
                firstname: 'jack',
                lastname: 'jack',
                email: 'jack'
              },
              revision: 0,
              version: 0,
              meta: {
                userId: 'userId'
              }
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).to.be.ok();
              expect(err.name).to.eql('ValidationError');
              expect(evts).to.be.an('array');
              expect(evts.length).to.eql(1);
              expect(evts[0].name).to.eql('rejectedCommand');
              expect(evts[0].payload.reason.name).to.eql('ValidationError');
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].name).to.eql('rejectedCommand');
              expect(publishedEvents[0].payload.reason.name).to.eql('ValidationError');

              expect(aggData).to.eql(null);
              expect(meta.aggregateId).to.eql('aggregateId');
              expect(meta.aggregate).to.eql('person');
              expect(meta.context).to.eql('hr');

              done();
            });

          });

        });

        describe('that fails on the validation rules', function () {

          it('it should publish a command rejected event and it should callback with an error and without events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              id: uuid().toString(),
              name: 'enterNewPerson',
              aggregate: {
                id: 'aggregateId',
                name: 'person'
              },
              context: {
                name: 'hr'
              },
              payload: 'payload',
              revision: 0,
              version: 0,
              meta: {
                userId: 'userId'
              }
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).to.be.ok();
              expect(err.name).to.eql('ValidationError');
              expect(evts).to.be.an('array');
              expect(evts.length).to.eql(1);
              expect(evts[0].name).to.eql('rejectedCommand');
              expect(evts[0].payload.reason.name).to.eql('ValidationError');
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].name).to.eql('rejectedCommand');
              expect(publishedEvents[0].payload.reason.name).to.eql('ValidationError');

              expect(aggData).to.eql(null);
              expect(meta.aggregateId).to.eql('aggregateId');
              expect(meta.aggregate).to.eql('person');
              expect(meta.context).to.eql('hr');

              done();
            });

          });

        });

        describe('that fails on a pre-load-condition', function () {

          it('it should publish a command rejected event and it should callback with an error and without events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              id: uuid().toString(),
              name: 'unregisterAllContactInformation',
              aggregate: {
                id: 'aggregateIdNew',
                name: 'person'
              },
              context: {
                name: 'hr'
              },
              payload: {
              },
              revision: 0,
              version: 2,
              meta: {
                userId: 'userId'
              },
              failPreLoadCondition: true
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).to.be.ok();
              expect(err.name).to.eql('BusinessRuleError');
              expect(err.message).to.eql('precondition failed!');
              expect(evts).to.be.an('array');
              expect(evts.length).to.eql(1);
              expect(evts[0].name).to.eql('rejectedCommand');
              expect(evts[0].payload.reason.name).to.eql('BusinessRuleError');
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].name).to.eql('rejectedCommand');
              expect(publishedEvents[0].payload.reason.name).to.eql('BusinessRuleError');

              expect(aggData).to.eql(null);
              expect(meta.aggregateId).to.eql('aggregateIdNew');
              expect(meta.aggregate).to.eql('person');
              expect(meta.context).to.eql('hr');

              done();
            });

          });

        });

        describe('that fails on a pre-condition', function () {

          it('it should publish a command rejected event and it should callback with an error and without events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              id: uuid().toString(),
              name: 'unregisterAllContactInformation',
              aggregate: {
                id: 'aggregateIdNew',
                name: 'person'
              },
              context: {
                name: 'hr'
              },
              payload: {
              },
              revision: 0,
              version: 2,
              meta: {
                userId: 'userId'
              }
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).to.be.ok();
              expect(err.name).to.eql('BusinessRuleError');
              expect(err.message).to.eql('not personalized');
              expect(evts).to.be.an('array');
              expect(evts.length).to.eql(1);
              expect(evts[0].name).to.eql('rejectedCommand');
              expect(evts[0].payload.reason.name).to.eql('BusinessRuleError');
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].name).to.eql('rejectedCommand');
              expect(publishedEvents[0].payload.reason.name).to.eql('BusinessRuleError');

              expect(aggData).to.eql(null);
              expect(meta.aggregateId).to.eql('aggregateIdNew');
              expect(meta.aggregate).to.eql('person');
              expect(meta.context).to.eql('hr');

              done();
            });

          });

        });

        describe('that fails on a pre-condition of an aggregate', function () {

          it('it should publish a command rejected event and it should callback with an error and without events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              id: uuid().toString(),
              name: 'unregisterAllContactInformation',
              aggregate: {
                id: 'aggregateIdNew',
                name: 'person'
              },
              context: {
                name: 'hr'
              },
              payload: {
              },
              revision: 0,
              version: 2,
              meta: {
                userId: 'userId'
              },
              notAuthorized: true
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).to.be.ok();
              expect(err.name).to.eql('BusinessRuleError');
              expect(err.message).to.eql('not authorized');
              expect(evts).to.be.an('array');
              expect(evts.length).to.eql(1);
              expect(evts[0].name).to.eql('rejectedCommand');
              expect(evts[0].payload.reason.name).to.eql('BusinessRuleError');
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].name).to.eql('rejectedCommand');
              expect(publishedEvents[0].payload.reason.name).to.eql('BusinessRuleError');

              expect(aggData).to.eql(null);
              expect(meta.aggregateId).to.eql('aggregateIdNew');
              expect(meta.aggregate).to.eql('person');
              expect(meta.context).to.eql('hr');

              done();
            });

          });

        });

        describe('that fails on a business rule', function () {

          it('it should publish a command rejected event and it should callback with an error and without events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              id: uuid().toString(),
              name: 'enterNewPerson',
              aggregate: {
                id: 'aggregateId',
                name: 'person'
              },
              context: {
                name: 'hr'
              },
              payload: {
                firstname: 'jack',
                lastname: 'jack',
                email: 'jack'
              },
              revision: 0,
              version: 0,
              meta: {
                userId: 'userId'
              }
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).to.be.ok();
              expect(err.name).to.eql('BusinessRuleError');
              expect(evts).to.be.an('array');
              expect(evts.length).to.eql(1);
              expect(evts[0].name).to.eql('rejectedCommand');
              expect(evts[0].payload.reason.name).to.eql('BusinessRuleError');
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].name).to.eql('rejectedCommand');
              expect(publishedEvents[0].payload.reason.name).to.eql('BusinessRuleError');

              expect(aggData).to.eql(null);
              expect(meta.aggregateId).to.eql('aggregateId');
              expect(meta.aggregate).to.eql('person');
              expect(meta.context).to.eql('hr');

              done();
            });

          });

        });

        describe('that fails because already seen', function () {

          it('it should publish a command rejected event and it should callback with an error and without events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              id: 'cmdIdForDuplication',
              name: 'enterNewPerson',
              aggregate: {
                id: 'aggregateIdForDuplication',
                name: 'person'
              },
              context: {
                name: 'hr'
              },
              payload: {
                firstname: 'jack',
                lastname: 'doe',
                email: 'jack'
              },
              revision: 0,
              version: 0,
              meta: {
                userId: 'userId'
              }
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).not.to.be.ok();
              expect(evts.length).to.eql(1);
              expect(evts[0].name).to.eql('enteredNewPerson');
              expect(evts[0].payload).to.eql(cmd.payload);
              expect(evts[0].meta).to.eql(cmd.meta);
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].name).to.eql('enteredNewPerson');
              expect(publishedEvents[0].payload).to.eql(cmd.payload);
              expect(publishedEvents[0].meta).to.eql(cmd.meta);

              expect(aggData.lastname).to.eql('doe');
              expect(meta.aggregateId).to.eql('aggregateIdForDuplication');
              expect(meta.aggregate).to.eql('person');
              expect(meta.context).to.eql('hr');

              domain.handle(cmd, function (err, evts, aggData, meta) {
                expect(err).to.be.ok();
                expect(err.name).to.eql('DuplicateCommandError');
                expect(evts).to.be.an('array');
                expect(evts.length).to.eql(1);
                expect(evts[0].name).to.eql('rejectedCommand');
                expect(evts[0].payload.reason.name).to.eql('DuplicateCommandError');
                expect(publishedEvents.length).to.eql(2);
                expect(publishedEvents[0].name).to.eql('enteredNewPerson');
                expect(publishedEvents[0].payload).to.eql(cmd.payload);
                expect(publishedEvents[0].meta).to.eql(cmd.meta);
                expect(publishedEvents[1].name).to.eql('rejectedCommand');
                expect(publishedEvents[1].payload.reason.name).to.eql('DuplicateCommandError');

                expect(aggData).to.eql(null);
                expect(meta).to.eql(null);

                done();
              });
            });

          });

        });

        describe('that is completely valid but with usage of defineCommandAwareAggregateIdGenerator', function () {

          it('it should publish a the resulting event and it should callback without an error and with events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              id: 'mySpecialCommandId' + uuid().toString(),
              name: 'enterNewPerson',
              aggregate: {
                name: 'person'
              },
              context: {
                name: 'hr'
              },
              payload: {
                firstname: 'jack',
                lastname: 'doe',
                email: 'jack'
              },
              revision: 0,
              version: 0,
              meta: {
                userId: 'userId'
              }
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).not.to.be.ok();
              expect(evts.length).to.eql(1);
              expect(evts[0].name).to.eql('enteredNewPerson');
              expect(evts[0].payload).to.eql(cmd.payload);
              expect(evts[0].meta).to.eql(cmd.meta);
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].name).to.eql('enteredNewPerson');
              expect(publishedEvents[0].payload).to.eql(cmd.payload);
              expect(publishedEvents[0].meta).to.eql(cmd.meta);

              expect(aggData.lastname).to.eql('doe');
              expect(meta.aggregateId.indexOf('mySpecialCommandId')).to.eql(0);
              expect(meta.aggregate).to.eql('person');
              expect(meta.context).to.eql('hr');

              done();
            });

          });

        });

        describe('that is completely valid', function () {

          it('it should publish a the resulting event and it should callback without an error and with events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              id: uuid().toString(),
              name: 'enterNewPerson',
              aggregate: {
                id: 'aggregateId',
                name: 'person'
              },
              context: {
                name: 'hr'
              },
              payload: {
                firstname: 'jack',
                lastname: 'doe',
                email: 'jack'
              },
              revision: 0,
              version: 0,
              meta: {
                userId: 'userId'
              }
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).not.to.be.ok();
              expect(evts.length).to.eql(1);
              expect(evts[0].name).to.eql('enteredNewPerson');
              expect(evts[0].payload).to.eql(cmd.payload);
              expect(evts[0].meta).to.eql(cmd.meta);
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].name).to.eql('enteredNewPerson');
              expect(publishedEvents[0].payload).to.eql(cmd.payload);
              expect(publishedEvents[0].meta).to.eql(cmd.meta);

              expect(aggData.lastname).to.eql('doe');
              expect(meta.aggregateId).to.eql('aggregateId');
              expect(meta.aggregate).to.eql('person');
              expect(meta.context).to.eql('hr');

              done();
            });

          });

        });

        describe('that generates 2 events', function () {

          it('it should publish a the resulting events and it should callback without an error and with events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              id: uuid().toString(),
              name: 'unregisterAllContactInformation',
              aggregate: {
                id: 'aggregateId',
                name: 'person'
              },
              context: {
                name: 'hr'
              },
              payload: {
              },
              revision: 1,
              version: 2,
              meta: {
                userId: 'userId'
              }
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).not.to.be.ok();
              expect(evts.length).to.eql(2);
              expect(evts[0].name).to.eql('unregisteredEMailAddress');
              expect(evts[0].payload.email).to.eql('default@mycomp.org');
              expect(evts[0].meta).to.eql(cmd.meta);
              expect(evts[1].name).to.eql('unregisteredEMailAddress');
              expect(evts[1].payload.email).to.eql('jack');
              expect(evts[1].meta).to.eql(cmd.meta);
              expect(publishedEvents.length).to.eql(2);
              expect(publishedEvents[0].name).to.eql('unregisteredEMailAddress');
              expect(publishedEvents[0].payload.email).to.eql('default@mycomp.org');
              expect(publishedEvents[0].meta).to.eql(cmd.meta);
              expect(publishedEvents[1].name).to.eql('unregisteredEMailAddress');
              expect(publishedEvents[1].payload.email).to.eql('jack');
              expect(publishedEvents[1].meta).to.eql(cmd.meta);

              expect(aggData.emails.length).to.eql(0);
              expect(meta.aggregateId).to.eql('aggregateId');
              expect(meta.aggregate).to.eql('person');
              expect(meta.context).to.eql('hr');

              done();
            });

          });

        });

        describe('that has a custom command handler', function () {

          it('it use that handler', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              id: uuid().toString(),
              name: 'enterNewSpecialPerson',
              aggregate: {
                id: 'aggregateId',
                name: 'person'
              },
              context: {
                name: 'hr'
              },
              payload: {
              },
              revision: 1,
              version: 0,
              meta: {
                userId: 'userId'
              }
            };

            domain.handle(cmd, function (err, evts) {
              expect(err).not.to.be.ok();
              expect(evts.length).to.eql(1);
              expect(evts[0].my).to.eql('special');
              expect(evts[0].ev).to.eql('ent');
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].my).to.eql('special');
              expect(publishedEvents[0].ev).to.eql('ent');

              done();
            });

          });

        });

      });

      describe('pre-condition ordering with priority', function () {

        it('should evaluate precondition with priority 1 first', function (done) {

          var cmd = {
            id: uuid().toString(),
            name: 'enterNewPerson',
            aggregate: {
              id: 'aggregateId1234',
              name: 'person'
            },
            context: {
              name: 'hr'
            },
            payload: {
              firstname: 'rumpelstilz', // triggers test precondition error
              lastname: 'some',
              email: 'test@rumpestilz.org'
            },
            revision: 0,
            version: 0,
            meta: {
              userId: 'userId'
            }
          };

          domain.handle(cmd, function (err) {
            expect(err).to.be.ok();
            expect(err.message).to.be('Precondition with prio 1 failed (all commands)');
            done();
          });
        });

      });

    });

    describe('format 2', function () {

      var domain;

      before(function (done) {
        domain = api({ domainPath: __dirname + '/fixture/set1', commandRejectedEventName: 'rejectedCommand' });
        domain.defineCommand({
          id: 'id',
          name: 'command',
          aggregateId: 'payload.id',
          payload: 'payload',
          revision: 'head.revision'
        });
        domain.defineEvent({
          correlationId: 'commandId',
          id: 'id',
          name: 'event',
          aggregateId: 'payload.id',
          payload: 'payload',
          revision: 'head.revision'
        });

        domain.init(done);
      });

      describe('handling a command that will not be handled', function () {

        it('it should not publish any event and it should callback with an error and without events', function (done) {

          var publishedEvents = [];

          domain.onEvent(function (evt) {
            publishedEvents.push(evt);
          });

          var cmd = {
            id: uuid().toString(),
            command: 'cmdName',
            payload: {
              id: 'aggregateId',
              data: 'data'
            },
            head: {
              userId: 'userId',
              revision: 0
            }
          };

          domain.handle(cmd, function (err, evts) {
            expect(err).to.be.ok();
            expect(err.message).to.match(/found/i);
            expect(evts).not.to.be.ok();
            expect(publishedEvents.length).to.eql(0);

            done();
          });

        });

      });

      describe('handling a command', function () {

        describe('that does fails on the validation rules of a parent schema', function () {

          it('it should publish a command rejected event and it should callback with an error and without events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              idd: 'cmdId',
              command: 'enterNewPerson',
              payload: {
                id: 'aggregateId',
                firstname: 'jack',
                lastname: 'doe',
                email: 'jack'
              },
              head: {
                userId: 'userId',
                revision: 0
              }
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(meta.aggregateId).to.eql('aggregateId');
              expect(meta.aggregate).to.eql('cart');
              expect(meta.context).to.eql('_general');

              done();
            });

          });

        });

        describe('that has a custom command handler', function () {

          it('it use that handler', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              idd: 'cmdId',
              command: 'enterNewSpecialPerson',
              payload: {
                id: 'aggregateId'
              },
              head: {
                userId: 'userId',
                revision: 0
              }
            };

            domain.handle(cmd, function (err, evts) {
              expect(err).not.to.be.ok();
              expect(evts.length).to.eql(1);
              expect(evts[0].my).to.eql('special');
              expect(evts[0].ev).to.eql('ent');
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].my).to.eql('special');
              expect(publishedEvents[0].ev).to.eql('ent');

              done();
            });

          });

        });

      });

    });

  });

  describe('set 2', function () {

    describe('format 2', function () {

      var domain;

      before(function (done) {
        domain = api({ domainPath: __dirname + '/fixture/set2', commandRejectedEventName: 'rejectedCommand' });
        domain.defineCommand({
          id: 'id',
          name: 'command',
          aggregateId: 'payload.id',
          payload: 'payload',
          revision: 'head.revision'
        });
        domain.defineEvent({
          correlationId: 'commandId',
          id: 'id',
          name: 'event',
          aggregateId: 'payload.id',
          payload: 'payload',
          revision: 'head.revision'
        });

        domain.init(done);
      });

      describe('handling a command that will not be handled', function () {

        it('it should not publish any event and it should callback with an error and without events', function (done) {

          var publishedEvents = [];

          domain.onEvent(function (evt) {
            publishedEvents.push(evt);
          });

          var cmd = {
            id: uuid().toString(),
            command: 'cmdName',
            payload: {
              id: 'aggregateId',
              data: 'data'
            },
            head: {
              userId: 'userId',
              revision: 0
            }
          };

          domain.handle(cmd, function (err, evts) {
            expect(err).to.be.ok();
            expect(err.message).to.match(/found/i);
            expect(evts).not.to.be.ok();
            expect(publishedEvents.length).to.eql(0);

            done();
          });

        });

      });

      describe('handling a command', function () {

        describe('that does fails on the validation rules of a parent schema', function () {

          it('it should publish a command rejected event and it should callback with an error and without events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              idd: 'cmdId',
              command: 'enterNewPerson',
              payload: {
                id: 'aggregateId',
                firstname: 'jack',
                lastname: 'doe',
                email: 'jack'
              },
              head: {
                userId: 'userId',
                revision: 0
              }
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).to.be.ok();
              expect(err.name).to.eql('ValidationError');
              expect(evts).to.be.an('array');
              expect(evts.length).to.eql(1);
              expect(evts[0].event).to.eql('rejectedCommand');
              expect(evts[0].payload.reason.name).to.eql('ValidationError');
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].event).to.eql('rejectedCommand');
              expect(publishedEvents[0].payload.reason.name).to.eql('ValidationError');

              expect(aggData).to.eql(null);
              expect(meta.aggregateId).to.eql('aggregateId');
              expect(meta.aggregate).to.eql('person');

              done();
            });

          });

        });

        describe('that fails on the validation rules', function () {

          it('it should publish a command rejected event and it should callback with an error and without events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              idd: 'cmdId',
              command: 'enterNewPerson',
              payload: {
                id: 'aggregateId'
              },
              head: {
                userId: 'userId',
                revision: 0
              }
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).to.be.ok();
              expect(err.name).to.eql('ValidationError');
              expect(evts).to.be.an('array');
              expect(evts.length).to.eql(1);
              expect(evts[0].event).to.eql('rejectedCommand');
              expect(evts[0].payload.reason.name).to.eql('ValidationError');
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].event).to.eql('rejectedCommand');
              expect(publishedEvents[0].payload.reason.name).to.eql('ValidationError');

              expect(aggData).to.eql(null);
              expect(meta.aggregateId).to.eql('aggregateId');
              expect(meta.aggregate).to.eql('person');

              done();
            });

          });

        });

        describe('that fails on a pre-condition', function () {

          it('it should publish a command rejected event and it should callback with an error and without events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              id: uuid().toString(),
              command: 'unregisterAllContactInformation',
              payload: {
                id: 'aggregateIdNew'
              },
              head: {
                userId: 'userId',
                revision: 0
              }
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).to.be.ok();
              expect(err.name).to.eql('BusinessRuleError');
              expect(err.message).to.eql('not personalized');
              expect(evts).to.be.an('array');
              expect(evts.length).to.eql(1);
              expect(evts[0].event).to.eql('rejectedCommand');
              expect(evts[0].payload.reason.name).to.eql('BusinessRuleError');
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].event).to.eql('rejectedCommand');
              expect(publishedEvents[0].payload.reason.name).to.eql('BusinessRuleError');

              expect(aggData).to.eql(null);
              expect(meta.aggregateId).to.eql('aggregateIdNew');
              expect(meta.aggregate).to.eql('person');

              done();
            });

          });

        });

        describe('that fails on a business rule', function () {

          it('it should publish a command rejected event and it should callback with an error and without events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              id: uuid().toString(),
              command: 'enterNewPerson',
              payload: {
                id: 'aggregateId',
                firstname: 'jack',
                lastname: 'jack',
                email: 'jack'
              },
              head: {
                userId: 'userId',
                revision: 0
              }
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).to.be.ok();
              expect(err.name).to.eql('BusinessRuleError');
              expect(evts).to.be.an('array');
              expect(evts.length).to.eql(1);
              expect(evts[0].event).to.eql('rejectedCommand');
              expect(evts[0].payload.reason.name).to.eql('BusinessRuleError');
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].event).to.eql('rejectedCommand');
              expect(publishedEvents[0].payload.reason.name).to.eql('BusinessRuleError');

              expect(aggData).to.eql(null);
              expect(meta.aggregateId).to.eql('aggregateId');
              expect(meta.aggregate).to.eql('person');

              done();
            });

          });

        });

        describe('that is completely valid', function () {

          it('it should publish a the resulting event and it should callback without an error and with events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              id: uuid().toString(),
              command: 'enterNewPerson',
              payload: {
                id: 'aggregateId',
                firstname: 'jack',
                lastname: 'doe',
                email: 'jack'
              },
              head: {
                userId: 'userId',
                revision: 0
              }
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).not.to.be.ok();
              expect(evts.length).to.eql(1);
              expect(evts[0].event).to.eql('enteredNewPerson');
              expect(evts[0].payload).to.eql(cmd.payload);
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].event).to.eql('enteredNewPerson');
              expect(publishedEvents[0].payload).to.eql(cmd.payload);

              expect(aggData.lastname).to.eql('doe');
              expect(meta.aggregateId).to.eql('aggregateId');
              expect(meta.aggregate).to.eql('person');

              done();
            });

          });

        });

        describe('that generates 2 events', function () {

          it('it should publish a the resulting events and it should callback without an error and with events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              id: uuid().toString(),
              command: 'unregisterAllContactInformation',
              payload: {
                id: 'aggregateId'
              },
              head: {
                userId: 'userId',
                revision: 1
              }
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).not.to.be.ok();
              expect(evts.length).to.eql(2);
              expect(evts[0].event).to.eql('unregisteredEMailAddress');
              expect(evts[0].payload.email).to.eql('default@mycomp.org');
              expect(evts[1].event).to.eql('unregisteredEMailAddress');
              expect(evts[1].payload.email).to.eql('jack');
              expect(publishedEvents.length).to.eql(2);
              expect(publishedEvents[0].event).to.eql('unregisteredEMailAddress');
              expect(publishedEvents[0].payload.email).to.eql('default@mycomp.org');
              expect(publishedEvents[1].event).to.eql('unregisteredEMailAddress');
              expect(publishedEvents[1].payload.email).to.eql('jack');

              expect(aggData.emails.length).to.eql(0);
              expect(meta.aggregateId).to.eql('aggregateId');
              expect(meta.aggregate).to.eql('person');

              done();
            });

          });

        });

        describe('that has a custom command handler', function () {

          it('it use that handler', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              idd: 'cmdId',
              command: 'enterNewSpecialPerson',
              payload: {
                id: 'aggregateId'
              },
              head: {
                userId: 'userId',
                revision: 0
              }
            };

            domain.handle(cmd, function (err, evts) {
              expect(err).not.to.be.ok();
              expect(evts.length).to.eql(1);
              expect(evts[0].my).to.eql('special');
              expect(evts[0].ev).to.eql('ent');
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].my).to.eql('special');
              expect(publishedEvents[0].ev).to.eql('ent');

              done();
            });

          });

        });

      });

    });

    describe('format 1', function () {

      var domain;

      before(function (done) {
        domain = api({ domainPath: __dirname + '/fixture/set2', commandRejectedEventName: 'rejectedCommand' });
        domain.defineCommand({
          id: 'id',
          name: 'name',
          aggregateId: 'aggregate.id',
          context: 'context.name',
          aggregate: 'aggregate.name',
          payload: 'payload',
          revision: 'revision',
          version: 'version',
          meta: 'meta'
        });
        domain.defineEvent({
          correlationId: 'correlationId',
          id: 'id',
          name: 'name',
          aggregateId: 'aggregate.id',
          context: 'context.name',
          aggregate: 'aggregate.name',
          payload: 'payload',
          revision: 'revision',
          version: 'version',
          meta: 'meta'
        });

        domain.init(done);
      });

      describe('handling a command that will not be handled', function () {

        it('it should not publish any event and it should callback with an error and without events', function (done) {

          var publishedEvents = [];

          domain.onEvent(function (evt) {
            publishedEvents.push(evt);
          });

          var cmd = {
            id: uuid().toString(),
            name: 'cmdName',
            aggregate: {
              id: 'aggregateId',
              name: 'aggregate'
            },
            context: {
              name: 'context'
            },
            payload: 'payload',
            revision: 0,
            version: 0,
            meta: {
              userId: 'userId'
            }
          };

          domain.handle(cmd, function (err, evts) {
            expect(err).to.be.ok();
            expect(err.message).to.match(/found/i);
            expect(evts).not.to.be.ok();
            expect(publishedEvents.length).to.eql(0);

            done();
          });

        });

      });

      describe('handling a command with correct command name but wrong aggregate and context', function () {

        it('it should not publish any event and it should callback with an error and without events', function (done) {

          var publishedEvents = [];

          domain.onEvent(function (evt) {
            publishedEvents.push(evt);
          });

          var cmd = {
            id: uuid().toString(),
            name: 'enterNewPerson',
            aggregate: {
              id: 'aggregateId',
              name: 'aggregate'
            },
            context: {
              name: 'context'
            },
            payload: 'payload',
            revision: 0,
            version: 0,
            meta: {
              userId: 'userId'
            }
          };

          domain.handle(cmd, function (err, evts) {
            expect(err).to.be.ok();
            expect(err.message).to.match(/found/i);
            expect(evts).not.to.be.ok();
            expect(publishedEvents.length).to.eql(0);

            done();
          });

        });

      });

      describe('handling a command with correct command name and correct aggregate but wrong context', function () {

        it('it should not publish any event and it should callback with an error and without events', function (done) {

          var publishedEvents = [];

          domain.onEvent(function (evt) {
            publishedEvents.push(evt);
          });

          var cmd = {
            id: uuid().toString(),
            name: 'enterNewPerson',
            aggregate: {
              id: 'aggregateId',
              name: 'person'
            },
            context: {
              name: 'context'
            },
            payload: 'payload',
            revision: 0,
            version: 0,
            meta: {
              userId: 'userId'
            }
          };

          domain.handle(cmd, function (err, evts) {
            expect(err).to.be.ok();
            expect(err.message).to.match(/found/i);
            expect(evts).not.to.be.ok();
            expect(publishedEvents.length).to.eql(0);

            done();
          });

        });

      });

      describe('handling a command', function () {

        describe('that does fails on the validation rules of a parent schema', function () {

          it('it should publish a command rejected event and it should callback with an error and without events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              idd: 'cmdId',
              name: 'enterNewPerson',
              aggregate: {
                id: 'aggregateId',
                name: 'person'
              },
//              context: {
//                name: 'hr'
//              },
              payload: {
                firstname: 'jack',
                lastname: 'doe',
                email: 'jack'
              },
              revision: 0,
              version: 0,
              meta: {
                userId: 'userId'
              }
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).to.be.ok();
              expect(err.name).to.eql('ValidationError');
              expect(evts).to.be.an('array');
              expect(evts.length).to.eql(1);
              expect(evts[0].name).to.eql('rejectedCommand');
              expect(evts[0].payload.reason.name).to.eql('ValidationError');
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].name).to.eql('rejectedCommand');
              expect(publishedEvents[0].payload.reason.name).to.eql('ValidationError');

              expect(aggData).to.eql(null);
              expect(meta.aggregateId).to.eql('aggregateId');
              expect(meta.aggregate).to.eql('person');

              done();
            });

          });

        });

        describe('that has a custom command handler', function () {

          it('it use that handler', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              id: uuid().toString(),
              name: 'enterNewSpecialPerson',
              aggregate: {
                id: 'aggregateId',
                name: 'person'
              },
//              context: {
//                name: 'hr'
//              },
              payload: {
              },
              revision: 1,
              version: 0,
              meta: {
                userId: 'userId'
              }
            };

            domain.handle(cmd, function (err, evts) {
              expect(err).not.to.be.ok();
              expect(evts.length).to.eql(1);
              expect(evts[0].my).to.eql('special');
              expect(evts[0].ev).to.eql('ent');
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].my).to.eql('special');
              expect(publishedEvents[0].ev).to.eql('ent');

              done();
            });

          });

        });

      });

    });

  });

  describe('set 3', function () {

    describe('format 3', function () {

      var domain;

      before(function (done) {
        domain = api({ domainPath: __dirname + '/fixture/set2', commandRejectedEventName: 'rejectedCommand' });
        domain.defineCommand({
          id: 'id',
          name: 'command',
          aggregateId: 'payload.id',
          aggregate: 'agg',
          payload: 'payload',
          revision: 'head.revision'
        });
        domain.defineEvent({
          correlationId: 'commandId',
          id: 'id',
          name: 'event',
          aggregateId: 'payload.id',
          aggregate: 'agg',
          payload: 'payload',
          revision: 'head.revision'
        });

        domain.init(done);
      });

      describe('handling a command that will not be handled', function () {

        it('it should not publish any event and it should callback with an error and without events', function (done) {

          var publishedEvents = [];

          domain.onEvent(function (evt) {
            publishedEvents.push(evt);
          });

          var cmd = {
            id: uuid().toString(),
            command: 'cmdName',
            agg: 'aggName',
            payload: {
              id: 'aggregateId',
              data: 'data'
            },
            head: {
              userId: 'userId',
              revision: 0
            }
          };

          domain.handle(cmd, function (err, evts) {
            expect(err).to.be.ok();
            expect(err.message).to.match(/found/i);
            expect(evts).not.to.be.ok();
            expect(publishedEvents.length).to.eql(0);

            done();
          });

        });

      });

      describe('handling a command', function () {

        describe('that does fails on the validation rules of a parent schema', function () {

          it('it should publish a command rejected event and it should callback with an error and without events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              idd: 'cmdId',
              command: 'enterNewPerson',
              agg: 'person',
              payload: {
                id: 'aggregateId',
                firstname: 'jack',
                lastname: 'doe',
                email: 'jack'
              },
              head: {
                userId: 'userId',
                revision: 0
              }
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).to.be.ok();
              expect(err.name).to.eql('ValidationError');
              expect(evts).to.be.an('array');
              expect(evts.length).to.eql(1);
              expect(evts[0].event).to.eql('rejectedCommand');
              expect(evts[0].payload.reason.name).to.eql('ValidationError');
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].event).to.eql('rejectedCommand');
              expect(publishedEvents[0].payload.reason.name).to.eql('ValidationError');

              expect(aggData).to.eql(null);
              expect(meta.aggregateId).to.eql('aggregateId');
              expect(meta.aggregate).to.eql('person');

              done();
            });

          });

        });

        describe('that fails on the validation rules', function () {

          it('it should publish a command rejected event and it should callback with an error and without events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              idd: 'cmdId',
              command: 'enterNewPerson',
              agg: 'person',
              payload: {
                id: 'aggregateId'
              },
              head: {
                userId: 'userId',
                revision: 0
              }
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).to.be.ok();
              expect(err.name).to.eql('ValidationError');
              expect(evts).to.be.an('array');
              expect(evts.length).to.eql(1);
              expect(evts[0].event).to.eql('rejectedCommand');
              expect(evts[0].payload.reason.name).to.eql('ValidationError');
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].event).to.eql('rejectedCommand');
              expect(publishedEvents[0].payload.reason.name).to.eql('ValidationError');

              expect(aggData).to.eql(null);
              expect(meta.aggregateId).to.eql('aggregateId');
              expect(meta.aggregate).to.eql('person');

              done();
            });

          });

        });

        describe('that fails on a business rule', function () {

          it('it should publish a command rejected event and it should callback with an error and without events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              id: uuid().toString(),
              command: 'enterNewPerson',
              agg: 'person',
              payload: {
                id: 'aggregateId',
                firstname: 'jack',
                lastname: 'jack',
                email: 'jack'
              },
              head: {
                userId: 'userId',
                revision: 0
              }
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).to.be.ok();
              expect(err.name).to.eql('BusinessRuleError');
              expect(evts).to.be.an('array');
              expect(evts.length).to.eql(1);
              expect(evts[0].event).to.eql('rejectedCommand');
              expect(evts[0].payload.reason.name).to.eql('BusinessRuleError');
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].event).to.eql('rejectedCommand');
              expect(publishedEvents[0].payload.reason.name).to.eql('BusinessRuleError');

              expect(aggData).to.eql(null);
              expect(meta.aggregateId).to.eql('aggregateId');
              expect(meta.aggregate).to.eql('person');

              done();
            });

          });

        });

        describe('that is completely valid', function () {

          it('it should publish a the resulting event and it should callback without an error and with events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              id: uuid().toString(),
              command: 'enterNewPerson',
              agg: 'person',
              payload: {
                id: 'aggregateId',
                firstname: 'jack',
                lastname: 'doe',
                email: 'jack'
              },
              head: {
                userId: 'userId',
                revision: 0
              }
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).not.to.be.ok();
              expect(evts.length).to.eql(1);
              expect(evts[0].event).to.eql('enteredNewPerson');
              expect(evts[0].payload).to.eql(cmd.payload);
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].event).to.eql('enteredNewPerson');
              expect(publishedEvents[0].payload).to.eql(cmd.payload);

              expect(aggData.lastname).to.eql('doe');
              expect(meta.aggregateId).to.eql('aggregateId');
              expect(meta.aggregate).to.eql('person');

              done();
            });

          });

        });

        describe('that generates 2 events', function () {

          it('it should publish a the resulting events and it should callback without an error and with events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              id: uuid().toString(),
              command: 'unregisterAllContactInformation',
              agg: 'person',
              payload: {
                id: 'aggregateId'
              },
              head: {
                userId: 'userId',
                revision: 1
              }
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).not.to.be.ok();
              expect(evts.length).to.eql(2);
              expect(evts[0].event).to.eql('unregisteredEMailAddress');
              expect(evts[0].payload.email).to.eql('default@mycomp.org');
              expect(evts[1].event).to.eql('unregisteredEMailAddress');
              expect(evts[1].payload.email).to.eql('jack');
              expect(publishedEvents.length).to.eql(2);
              expect(publishedEvents[0].event).to.eql('unregisteredEMailAddress');
              expect(publishedEvents[0].payload.email).to.eql('default@mycomp.org');
              expect(publishedEvents[1].event).to.eql('unregisteredEMailAddress');
              expect(publishedEvents[1].payload.email).to.eql('jack');

              expect(aggData.emails.length).to.eql(0);
              expect(meta.aggregateId).to.eql('aggregateId');
              expect(meta.aggregate).to.eql('person');

              done();
            });

          });

        });

        describe('that has a custom command handler', function () {

          it('it use that handler', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              idd: 'cmdId',
              command: 'enterNewSpecialPerson',
              agg: 'person',
              payload: {
                id: 'aggregateId'
              },
              head: {
                userId: 'userId',
                revision: 0
              }
            };

            domain.handle(cmd, function (err, evts) {
              expect(err).not.to.be.ok();
              expect(evts.length).to.eql(1);
              expect(evts[0].my).to.eql('special');
              expect(evts[0].ev).to.eql('ent');
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].my).to.eql('special');
              expect(publishedEvents[0].ev).to.eql('ent');

              done();
            });

          });

        });

      });

    });

    describe('format 1', function () {

      var domain;

      before(function (done) {
        domain = api({ domainPath: __dirname + '/fixture/set2', commandRejectedEventName: 'rejectedCommand' });
        domain.defineCommand({
          id: 'id',
          name: 'name',
          aggregateId: 'aggregate.id',
          context: 'context.name',
          aggregate: 'aggregate.name',
          payload: 'payload',
          revision: 'revision',
          version: 'version',
          meta: 'meta'
        });
        domain.defineEvent({
          correlationId: 'correlationId',
          id: 'id',
          name: 'name',
          aggregateId: 'aggregate.id',
          context: 'context.name',
          aggregate: 'aggregate.name',
          payload: 'payload',
          revision: 'revision',
          version: 'version',
          meta: 'meta'
        });

        domain.init(done);
      });

      describe('handling a command that will not be handled', function () {

        it('it should not publish any event and it should callback with an error and without events', function (done) {

          var publishedEvents = [];

          domain.onEvent(function (evt) {
            publishedEvents.push(evt);
          });

          var cmd = {
            id: uuid().toString(),
            name: 'cmdName',
            aggregate: {
              id: 'aggregateId',
              name: 'aggregate'
            },
            context: {
              name: 'context'
            },
            payload: 'payload',
            revision: 0,
            version: 0,
            meta: {
              userId: 'userId'
            }
          };

          domain.handle(cmd, function (err, evts) {
            expect(err).to.be.ok();
            expect(err.message).to.match(/found/i);
            expect(evts).not.to.be.ok();
            expect(publishedEvents.length).to.eql(0);

            done();
          });

        });

      });

      describe('handling a command with correct command name but wrong aggregate and context', function () {

        it('it should not publish any event and it should callback with an error and without events', function (done) {

          var publishedEvents = [];

          domain.onEvent(function (evt) {
            publishedEvents.push(evt);
          });

          var cmd = {
            id: uuid().toString(),
            name: 'enterNewPerson',
            aggregate: {
              id: 'aggregateId',
              name: 'aggregate'
            },
            context: {
              name: 'context'
            },
            payload: 'payload',
            revision: 0,
            version: 0,
            meta: {
              userId: 'userId'
            }
          };

          domain.handle(cmd, function (err, evts) {
            expect(err).to.be.ok();
            expect(err.message).to.match(/found/i);
            expect(evts).not.to.be.ok();
            expect(publishedEvents.length).to.eql(0);

            done();
          });

        });

      });

      describe('handling a command with correct command name and correct aggregate but wrong context', function () {

        it('it should not publish any event and it should callback with an error and without events', function (done) {

          var publishedEvents = [];

          domain.onEvent(function (evt) {
            publishedEvents.push(evt);
          });

          var cmd = {
            id: uuid().toString(),
            name: 'enterNewPerson',
            aggregate: {
              id: 'aggregateId',
              name: 'person'
            },
            context: {
              name: 'context'
            },
            payload: 'payload',
            revision: 0,
            version: 0,
            meta: {
              userId: 'userId'
            }
          };

          domain.handle(cmd, function (err, evts) {
            expect(err).to.be.ok();
            expect(err.message).to.match(/found/i);
            expect(evts).not.to.be.ok();
            expect(publishedEvents.length).to.eql(0);

            done();
          });

        });

      });

      describe('handling a command', function () {

        describe('that does fails on the validation rules of a parent schema', function () {

          it('it should publish a command rejected event and it should callback with an error and without events', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              idd: 'cmdId',
              name: 'enterNewPerson',
              aggregate: {
                id: 'aggregateId',
                name: 'person'
              },
//              context: {
//                name: 'hr'
//              },
              payload: {
                firstname: 'jack',
                lastname: 'doe',
                email: 'jack'
              },
              revision: 0,
              version: 0,
              meta: {
                userId: 'userId'
              }
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).to.be.ok();
              expect(err.name).to.eql('ValidationError');
              expect(evts).to.be.an('array');
              expect(evts.length).to.eql(1);
              expect(evts[0].name).to.eql('rejectedCommand');
              expect(evts[0].payload.reason.name).to.eql('ValidationError');
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].name).to.eql('rejectedCommand');
              expect(publishedEvents[0].payload.reason.name).to.eql('ValidationError');

              expect(aggData).to.eql(null);
              expect(meta.aggregateId).to.eql('aggregateId');
              expect(meta.aggregate).to.eql('person');

              done();
            });

          });

        });

        describe('that has a custom command handler', function () {

          it('it use that handler', function (done) {

            var publishedEvents = [];

            domain.onEvent(function (evt) {
              publishedEvents.push(evt);
            });

            var cmd = {
              id: uuid().toString(),
              name: 'enterNewSpecialPerson',
              aggregate: {
                id: 'aggregateId',
                name: 'person'
              },
//              context: {
//                name: 'hr'
//              },
              payload: {
              },
              revision: 1,
              version: 0,
              meta: {
                userId: 'userId'
              }
            };

            domain.handle(cmd, function (err, evts) {
              expect(err).not.to.be.ok();
              expect(evts.length).to.eql(1);
              expect(evts[0].my).to.eql('special');
              expect(evts[0].ev).to.eql('ent');
              expect(publishedEvents.length).to.eql(1);
              expect(publishedEvents[0].my).to.eql('special');
              expect(publishedEvents[0].ev).to.eql('ent');

              done();
            });

          });

        });

      });

    });

  });

});
```

## File: `test/integration/migrationTest.js`
```javascript
var expect = require('expect.js'),
  assert = require('assert'),
  api = require('../../index'),
  async = require('async'),
  _ = require('lodash'),
  uuid = require('uuid').v4;

describe('migration of domain', function () {

  var oldEventStore;

  var personsAggregateId = uuid().toString();

  var mailsAggregateId = uuid().toString();

  var v1Events = [];

  var v1Commands = [
    {
      id: uuid().toString(),
      name: 'enterNewPerson',
      aggregate: {
        id: personsAggregateId,
        name: 'persons'
      },
      context: {
        name: 'hr'
      },
      payload: {
        firstname: 'jack',
        lastname: 'doe',
        email: 'jack@doe.com'
      },
      revision: 0,
      version: 0,
      meta: {
        userId: 'userId'
      }
    },
    {
      id: uuid().toString(),
      name: 'enterNewPerson',
      aggregate: {
        id: personsAggregateId,
        name: 'persons'
      },
      context: {
        name: 'hr'
      },
      payload: {
        firstname: 'fitz',
        lastname: 'gerald',
        email: 'fitz@gerald.com'
      },
      revision: 1,
      version: 0,
      meta: {
        userId: 'userId'
      }
    },
    {
      id: uuid().toString(),
      name: 'enterNewPerson',
      aggregate: {
        id: personsAggregateId,
        name: 'persons'
      },
      context: {
        name: 'hr'
      },
      payload: {
        firstname: 'pablo',
        lastname: 'picasso',
        email: 'pablo@picasso.com'
      },
      revision: 2,
      version: 0,
      meta: {
        userId: 'userId'
      }
    },
    {
      id: uuid().toString(),
      name: 'enterNewPerson',
      aggregate: {
        id: personsAggregateId,
        name: 'persons'
      },
      context: {
        name: 'hr'
      },
      payload: {
        firstname: 'steve',
        lastname: 'jobs',
        email: 'steve@jobs.com'
      },
      revision: 3,
      version: 0,
      meta: {
        userId: 'userId'
      }
    },
    {
      id: uuid().toString(),
      name: 'enterNewPerson',
      aggregate: {
        id: personsAggregateId,
        name: 'persons'
      },
      context: {
        name: 'hr'
      },
      payload: {
        firstname: 'mister',
        lastname: 't',
        email: 'fitz@gerald.com'
      },
      revision: 4,
      version: 0,
      meta: {
        userId: 'userId',
        shouldFail: true
      }
    },
    {
      id: uuid().toString(),
      name: 'enterNewPerson',
      aggregate: {
        id: personsAggregateId,
        name: 'persons'
      },
      context: {
        name: 'hr'
      },
      payload: {
        firstname: 'mister',
        lastname: 't',
        email: 'mister@t.com'
      },
      revision: 4,
      version: 0,
      meta: {
        userId: 'userId'
      }
    }
  ];

  var v1CommandsForV2 = [
    {
      id: uuid().toString(),
      name: 'enterNewPerson',
      aggregate: {
        id: personsAggregateId,
        name: 'persons'
      },
      context: {
        name: 'hr'
      },
      payload: {
        firstname: 'already',
        lastname: 'in old stream',
        email: 'mister@t.com'
      },
      revision: 5,
      version: 0,
      meta: {
        userId: 'userId',
        shouldFail: true
      }
    },
    {
      id: uuid().toString(),
      name: 'enterNewPerson',
      aggregate: {
        id: personsAggregateId,
        name: 'persons'
      },
      context: {
        name: 'hr'
      },
      payload: {
        firstname: 'new',
        lastname: 'for old version',
        email: 'newForOld@version.com'
      },
      revision: 5,
      version: 0,
      meta: {
        userId: 'userId'
      }
    }
  ];

  var v2Commands = [
    {
      id: uuid().toString(),
      name: 'addEmail',
      aggregate: {
        id: mailsAggregateId,
        name: 'mails'
      },
      context: {
        name: 'hr'
      },
      payload: {
        firstname: 'already',
        lastname: 'in old stream',
        email: 'mister@t.com'
      },
      revision: 0,
      version: 0,
      meta: {
        userId: 'userId',
        oldAggId: personsAggregateId,
        shouldFail: true
      }
    },
    {
      id: uuid().toString(),
      name: 'addEmail',
      aggregate: {
        id: mailsAggregateId,
        name: 'mails'
      },
      context: {
        name: 'hr'
      },
      payload: {
        firstname: 'new',
        lastname: 'for new version',
        email: 'newForNew@version.com'
      },
      revision: 0,
      version: 0,
      meta: {
        userId: 'userId',
        oldAggId: personsAggregateId
      }
    },
    {
      id: uuid().toString(),
      name: 'addEmail',
      aggregate: {
        id: mailsAggregateId,
        name: 'mails'
      },
      context: {
        name: 'hr'
      },
      payload: {
        firstname: 'another new',
        lastname: 'for new version',
        email: 'newForNew2@version.com'
      },
      revision: 1,
      version: 0,
      meta: {
        userId: 'userId',
        oldAggId: personsAggregateId
      }
    },
    {
      id: uuid().toString(),
      name: 'enterNewPerson',
      aggregate: {
        id: personsAggregateId,
        name: 'persons'
      },
      context: {
        name: 'hr'
      },
      payload: {
        firstname: 'another new',
        lastname: 'for new version',
        email: 'newForNew2@version.com'
      },
      revision: 5,
      version: 0,
      meta: {
        userId: 'userId',
        newAggId: mailsAggregateId,
        shouldFail: true
      }
    },
    {
      id: uuid().toString(),
      name: 'enterNewPerson',
      aggregate: {
        id: personsAggregateId,
        name: 'persons'
      },
      context: {
        name: 'hr'
      },
      payload: {
        firstname: 'another new old',
        lastname: 'for old version'
      },
      revision: 5,
      version: 1,
      meta: {
        userId: 'userId',
        newAggId: mailsAggregateId,
        isLastOfPersons: true
      }
    },
    {
      id: uuid().toString(),
      name: 'addEmail',
      aggregate: {
        id: mailsAggregateId,
        name: 'mails'
      },
      context: {
        name: 'hr'
      },
      payload: {
        firstname: 'another new',
        lastname: 'for new version',
        email: 'newForNew3@version.com'
      },
      revision: 2,
      version: 0,
      meta: {
        userId: 'userId',
        oldAggId: personsAggregateId
      }
    }
  ];

  describe('v1', function () {

    var domain;

    before(function (done) {
      domain = api({ domainPath: __dirname + '/fixture/migration/v1' });
      domain.defineCommand({
        id: 'id',
        name: 'name',
        aggregateId: 'aggregate.id',
        context: 'context.name',
        aggregate: 'aggregate.name',
        payload: 'payload',
        revision: 'revision',
        version: 'version',
        meta: 'meta'
      });
      domain.defineEvent({
        correlationId: 'correlationId',
        id: 'id',
        name: 'name',
        aggregateId: 'aggregate.id',
        context: 'context.name',
        aggregate: 'aggregate.name',
        payload: 'payload',
        revision: 'revision',
        version: 'version',
        meta: 'meta'
      });

      domain.init(function (err) {
        oldEventStore = domain.eventStore;
        done(err);
      });
    });

    describe('handling a set of commands', function () {

      it('it should work as expected', function (done) {

        async.eachSeries(v1Commands, function (cmd, callback) {
          domain.handle(cmd, function (err, evts, aggData, meta) {

            if (cmd.meta.shouldFail) {
              expect(err).to.be.ok();
              expect(err.name).to.eql('BusinessRuleError');
              expect(err.message).to.eql('email already used');

              return callback();
            }

            expect(err).not.to.be.ok();
            expect(evts.length).to.eql(1);
            expect(evts[0].name).to.eql('enteredNewPerson');
            expect(evts[0].payload).to.eql(cmd.payload);
            expect(evts[0].meta).to.eql(cmd.meta);
            expect(evts[0].revision).to.eql(cmd.revision + 1);

            expect(meta.aggregateId).to.eql(cmd.aggregate.id);
            expect(meta.aggregate).to.eql(cmd.aggregate.name);
            expect(meta.context).to.eql(cmd.context.name);

            v1Events.push(evts[0]);

            callback();
          });
        }, done);

      });

    });

  });

  describe('v2', function () {

    describe('handling the same set of commands as v1', function () {

      var domain;

      before(function (done) {
        domain = api({ domainPath: __dirname + '/fixture/migration/v2' });
        domain.defineCommand({
          id: 'id',
          name: 'name',
          aggregateId: 'aggregate.id',
          context: 'context.name',
          aggregate: 'aggregate.name',
          payload: 'payload',
          revision: 'revision',
          version: 'version',
          meta: 'meta'
        });
        domain.defineEvent({
          correlationId: 'correlationId',
          id: 'id',
          name: 'name',
          aggregateId: 'aggregate.id',
          context: 'context.name',
          aggregate: 'aggregate.name',
          payload: 'payload',
          revision: 'revision',
          version: 'version',
          meta: 'meta'
        });

        domain.init(done);
      });

      it('it should work as expected', function (done) {

        var i = 0;

        async.eachSeries(v1Commands, function (cmd, callback) {
          domain.handle(cmd, function (err, evts, aggData, meta) {

            if (cmd.name === 'enterNewPerson') {
              expect(err).to.be.ok();
              expect(err.message).to.contain('found');

              return callback();
            }

            if (cmd.meta.shouldFail) {
              expect(err).to.be.ok();
              expect(err.name).to.eql('BusinessRuleError');
              expect(err.message).to.eql('email already used');

              return callback();
            }

            expect(err).not.to.be.ok();
            expect(evts.length).to.eql(1);
            expect(evts[0].name).to.eql('enteredNewPerson');
            expect(evts[0].payload).to.eql(cmd.payload);
            expect(evts[0].meta).to.eql(cmd.meta);
            expect(evts[0].revision).to.eql(cmd.revision + 1);

            expect(meta.aggregateId).to.eql(cmd.aggregate.id);
            expect(meta.aggregate).to.eql('mails');
            expect(meta.context).to.eql('hr');

            assert.deepEqual(_.omit(evts[0], 'id'), _.omit(v1Events[i], 'id'));

            i++;
            callback();
          });
        }, done);

      });

    });

    describe('having an existing eventstore created at v1', function () {

      var domain;

      before(function (done) {
        domain = api({ domainPath: __dirname + '/fixture/migration/v2' });
        domain.defineCommand({
          id: 'id',
          name: 'name',
          aggregateId: 'aggregate.id',
          context: 'context.name',
          aggregate: 'aggregate.name',
          payload: 'payload',
          revision: 'revision',
          version: 'version',
          meta: 'meta'
        });
        domain.defineEvent({
          correlationId: 'correlationId',
          id: 'id',
          name: 'name',
          aggregateId: 'aggregate.id',
          context: 'context.name',
          aggregate: 'aggregate.name',
          payload: 'payload',
          revision: 'revision',
          version: 'version',
          meta: 'meta'
        });

        domain.init(function (err) {
          domain.eventStore = oldEventStore;
          domain.tree.useEventStore(domain.eventStore);
          done(err);
        });
      });

      describe('and continuing with the v2 domain', function () {

        describe('sending old commands', function () {

          it('it should work as expected', function (done) {

            async.eachSeries(v1CommandsForV2, function (cmd, callback) {
              domain.handle(cmd, function (err, evts, aggData, meta) {

                if (cmd.name === 'enterNewPerson') {
                  expect(err).to.be.ok();
                  expect(err.message).to.contain('found');

                  return callback();
                }

                if (cmd.meta.shouldFail) {
                  expect(err).to.be.ok();
                  expect(err.name).to.eql('BusinessRuleError');
                  expect(err.message).to.eql('email already used');

                  return callback();
                }

                expect(aggData.persons).not.to.be.ok();
                expect(aggData.mails).to.be.ok();

                expect(err).not.to.be.ok();
                expect(evts.length).to.eql(1);
                expect(evts[0].name).to.eql('enteredNewPerson');
                expect(evts[0].payload).to.eql(cmd.payload);
                expect(evts[0].meta).to.eql(cmd.meta);
                expect(evts[0].revision).to.eql(cmd.revision + 1);

                expect(meta.aggregateId).to.eql(cmd.aggregate.id);
                expect(meta.aggregate).to.eql('mails');
                expect(meta.context).to.eql('hr');

                callback();
              });
            }, done);

          });

          describe('and then new commands', function () {

            it('it should work as expected', function (done) {

              async.eachSeries(v2Commands, function (cmd, callback) {
                domain.handle(cmd, function (err, evts, aggData, meta) {

                  if (cmd.name === 'enterNewPerson' && cmd.version === 0) {
                    expect(err).to.be.ok();
                    expect(err.message).to.contain('found');

                    return callback();
                  }

                  if (cmd.meta.shouldFail) {
                    expect(err).to.be.ok();
                    expect(err.name).to.eql('BusinessRuleError');
                    expect(err.message).to.eql('email already used');

                    return callback();
                  }

                  if (cmd.name === 'enterNewPerson') {
                    expect(aggData.persons).to.be.ok();
                    expect(aggData.mails).not.to.be.ok();
                  } else {
                    expect(aggData.persons).not.to.be.ok();
                    expect(aggData.mails).to.be.ok();
                  }

                  expect(err).not.to.be.ok();
                  expect(evts.length).to.eql(1);
                  if (cmd.name === 'enterNewPerson') {
                    expect(evts[0].name).to.eql('enteredNewPerson');
                  } else {
                    expect(evts[0].name).to.eql('emailAdded');
                  }
                  expect(evts[0].payload).to.eql(cmd.payload);
                  expect(evts[0].meta).to.eql(cmd.meta);
                  expect(evts[0].revision).to.eql(cmd.revision + 1);

                  expect(meta.aggregateId).to.eql(cmd.aggregate.id);
                  if (cmd.name === 'enterNewPerson') {
                    expect(meta.aggregate).to.eql('persons');
                  } else {
                    expect(meta.aggregate).to.eql('mails');
                  }
                  expect(meta.context).to.eql(cmd.context.name);

                  if (cmd.meta.isLastOfPersons) {
                    expect(aggData.persons.length).to.eql(6);
                  }

                  callback();
                });
              }, done);

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

## File: `test/integration/fixture/migration/v1/command.json`
```json
{
  "title": "command",
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "context": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        }
      },
      "required": ["name"]
    },
    "aggregate": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        }
      },
      "required": ["name"]
    },
    "name": {
      "type": "string"
    },
    "payload": {
      "type": "object",
      "properties": {
      },
      "required": []
    },
    "meta": {
      "type": "object",
      "properties": {
        "userId": {
          "type": "string"
        }
      },
      "required": []
    },
    "revision": {
      "type": "integer",
      "minimum": 0
    },
    "version": {
      "type": "integer",
      "minimum": 0
    }
  },
  "required": ["id", "context", "aggregate", "name"]
}
```

## File: `test/integration/fixture/migration/v1/hr/command.json`
```json
{
  "title": "command/hr",
  "allOf": [
    { "$ref": "/command" },
    {
      "properties": {
        "context": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "pattern": "hr"
            }
          }
        }
      }
    }
  ]
}
```

## File: `test/integration/fixture/migration/v1/hr/context.js`
```javascript
//module.exports = require('cqrs-domain').defineContext({
module.exports = require('../../../../../../').defineContext({
  name: 'hr'
});
```

## File: `test/integration/fixture/migration/v1/hr/persons/aggregate.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineAggregate({
module.exports = require('../../../../../../../').defineAggregate({
  name: 'persons', // optional, default is last part of path name
  version: 0, // optional, default 0
  defaultCommandPayload: 'payload',
  defaultEventPayload: 'payload',
  defaultPreConditionPayload: 'payload'
},
{
  persons: []
})
.defineSnapshotNeed(function (loadingTime, events, aggregate) {
  return events.length >= 2;
})
.defineLoadingSnapshotTransformer({
  version: 0
}, function (snap) {
  if (snap.persons) {
    for (var i = 0; i < snap.persons.length; i++) {
      if (snap.persons[i].firstname.indexOf('_encrypted_') < 0) throw new Error('Encrypted prop not found!\nThis should not happen!');
      snap.persons[i].firstname = snap.persons[i].firstname.replace('_encrypted_', '');
    }
  }
  return snap;
})
.defineCommittingSnapshotTransformer({
  version: 0
}, function (snap) {
  if (snap.persons) {
    for (var i = 0; i < snap.persons.length; i++) {
      if (snap.persons[i].firstname.indexOf('_encrypted_') === 0) throw new Error('Encrypted prop found!\nThis should not happen!');
      snap.persons[i].firstname = '_encrypted_' + snap.persons[i].firstname;
    }
  }
  return snap;
});
```

## File: `test/integration/fixture/migration/v1/hr/persons/command.json`
```json
{
  "title": "command/hr/persons",
  "allOf": [
    { "$ref": "/command/hr" },
    {
      "properties": {
        "aggregate": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "pattern": "persons"
            }
          }
        }
      }
    }
  ]
}
```

## File: `test/integration/fixture/migration/v1/hr/persons/commands/enterNewPerson.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineCommand({
module.exports = require('../../../../../../../../').defineCommand({
  name: 'enterNewPerson',
  version: 0
}, function (data, aggregate) {
  aggregate.apply('enteredNewPerson', data);
});
```

## File: `test/integration/fixture/migration/v1/hr/persons/eventTransformers/enteredNewPerson.js`
```javascript
//module.exports = require('cqrs-domain').defineEvent({
module.exports = [
  require('../../../../../../../../').defineLoadingEventTransformer({
    name: 'enteredNewPerson', // optional, default is file name without extension
    version: 0
  }, function (evt) {
    if (evt.payload.firstname) {
      if (evt.payload.firstname.indexOf('_encrypted_') < 0) throw new Error('Encrypted prop not found!\nThis should not happen!');
      evt.payload.firstname = evt.payload.firstname.replace('_encrypted_', '');
    }
    return evt;
  }),
  require('../../../../../../../../').defineCommittingEventTransformer({
    name: 'enteredNewPerson', // optional, default is file name without extension
    version: 0
  }, function (evt) {
    if (evt.payload.firstname) {
      if (evt.payload.firstname.indexOf('_encrypted_') === 0) throw new Error('Encrypted prop found!\nThis should not happen!');
      evt.payload.firstname = '_encrypted_' + evt.payload.firstname;
    }
    return evt;
  })
];
```

## File: `test/integration/fixture/migration/v1/hr/persons/events/enteredNewPerson.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineEvent({
module.exports = require('../../../../../../../../').defineEvent({
  name: 'enteredNewPerson',
  version: 0
}, function (data, aggregate) {
  aggregate.get('persons').push(data);
});
```

## File: `test/integration/fixture/migration/v1/hr/persons/preConditions/unique.js`
```javascript
var _ = require('lodash');

module.exports = require('../../../../../../../../').definePreCondition({
  name: 'enterNewPerson',
  version: 0,
  description: 'unique mail address'
}, function (data, agg) {
  var found = _.find(agg.get('persons'), function (person) {
    return person.email === data.email;
  });
  if (found) {
    throw new Error('email already used');
  }
});
```

## File: `test/integration/fixture/migration/v1/hr/persons/validationRules/enterNewPerson.json`
```json
{
  "title": "enterNewPerson",
  "allOf": [
    { "$ref": "/command/hr/persons" },
    {
      "properties": {
        "name": {
          "type": "string",
          "pattern": "enterNewPerson"
        },
        "payload": {
          "type": "object",
          "properties": {
            "firstname": {
              "type": "string"
            },
            "lastname": {
              "type": "string"
            },
            "email": {
              "type": "string"
            }
          },
          "required": ["firstname", "lastname", "email"]
        }
      },
      "required": ["payload"]
    }
  ]
}
```

## File: `test/integration/fixture/migration/v2/command.json`
```json
{
  "title": "command",
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "context": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        }
      },
      "required": ["name"]
    },
    "aggregate": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        }
      },
      "required": ["name"]
    },
    "name": {
      "type": "string"
    },
    "payload": {
      "type": "object",
      "properties": {
      },
      "required": []
    },
    "meta": {
      "type": "object",
      "properties": {
        "userId": {
          "type": "string"
        }
      },
      "required": []
    },
    "revision": {
      "type": "integer",
      "minimum": 0
    },
    "version": {
      "type": "integer",
      "minimum": 0
    }
  },
  "required": ["id", "context", "aggregate", "name"]
}
```

## File: `test/integration/fixture/migration/v2/hr/command.json`
```json
{
  "title": "command/hr",
  "allOf": [
    { "$ref": "/command" },
    {
      "properties": {
        "context": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "pattern": "hr"
            }
          }
        }
      }
    }
  ]
}
```

## File: `test/integration/fixture/migration/v2/hr/context.js`
```javascript
//module.exports = require('cqrs-domain').defineContext({
module.exports = require('../../../../../../').defineContext({
  name: 'hr'
});
```

## File: `test/integration/fixture/migration/v2/hr/mails/aggregate.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineAggregate({
module.exports = require('../../../../../../../').defineAggregate({
  name: 'mails', // optional, default is last part of path name
  version: 0, // optional, default 0
  defaultCommandPayload: 'payload',
  defaultEventPayload: 'payload',
  defaultPreConditionPayload: 'payload'
},
{
  mails: []
})
.defineSnapshotNeed(function (loadingTime, events, aggregate) {
  return events.length >= 2;
});
```

## File: `test/integration/fixture/migration/v2/hr/mails/command.json`
```json
{
  "title": "command/hr/mails",
  "allOf": [
    { "$ref": "/command/hr" },
    {
      "properties": {
        "aggregate": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "pattern": "mails"
            }
          }
        }
      }
    }
  ]
}
```

## File: `test/integration/fixture/migration/v2/hr/mails/businessRules/unique.js`
```javascript
var _ = require('lodash');

module.exports = require('../../../../../../../../').defineBusinessRule({
  name: 'uniqueEmails',
  description: 'unique mail address'
}, function (changed, previous, events, command) {

  if (_.uniq(changed.get('mails')).length !== changed.get('mails').length) {
    throw new Error('email already used');
  }

});
```

## File: `test/integration/fixture/migration/v2/hr/mails/commands/addEmail.js`
```javascript
module.exports = require('../../../../../../../../').defineCommand({
  name: 'addEmail',
  version: 0
}, function (data, aggregate) {
  aggregate.apply('emailAdded', data);
})
.defineEventStreamsToLoad(function (cmd) {
  return [{ // order is new to old
    context: 'hr',
    aggregate: 'mails',
    aggregateId: cmd.aggregate.id
  },{
    context: 'hr',
    aggregate: 'persons',
    aggregateId: cmd.meta.oldAggId
  }];
});
```

## File: `test/integration/fixture/migration/v2/hr/mails/commands/enterNewPerson_v0.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineCommand({
module.exports = require('../../../../../../../../').defineCommand({
  name: 'enterNewPerson',
  version: 0,
  source: {
    aggregate: 'persons', // old command location
    context: 'hr'         // old command location
  }
}, function (data, aggregate) {
  aggregate.apply('enteredNewPerson', data, 0);
})
.defineEventStreamsToLoad(function (cmd) {
  return [{
    context: 'hr',
    aggregate: 'mails',
    aggregateId: cmd.meta.newAggId
  },{
    context: 'hr',
    aggregate: 'persons',
    aggregateId: cmd.aggregate.id
  }];
});
```

## File: `test/integration/fixture/migration/v2/hr/mails/events/emailAdded.js`
```javascript
module.exports = require('../../../../../../../../').defineEvent({
  name: 'emailAdded',
  version: 0
}, function (data, aggregate) {
  aggregate.get('mails').push(data.email);
});
```

## File: `test/integration/fixture/migration/v2/hr/mails/events/enteredNewPerson_v0.js`
```javascript
module.exports = require('../../../../../../../../').defineEvent({
  name: 'enteredNewPerson',
  version: 0
}, function (data, aggregate) {
  aggregate.get('mails').push(data.email);
});
```

## File: `test/integration/fixture/migration/v2/hr/mails/validationRules/addEmail.json`
```json
{
  "title": "addEmail",
  "allOf": [
  { "$ref": "/command/hr/mails" },
  {
    "properties": {
      "version": {
        "type": "integer",
        "minimum": 0,
        "maximum": 0
      },
      "name": {
        "type": "string",
        "pattern": "addEmail"
      },
      "payload": {
        "type": "object",
        "properties": {
          "email": {
            "type": "string"
          }
        },
        "required": ["firstname", "lastname", "email"]
      }
    },
    "required": ["payload"]
  }
]
}
```

## File: `test/integration/fixture/migration/v2/hr/mails/validationRules/enterNewPerson_v0.json`
```json
{
  "title": "enterNewPerson",
  "version": 0,
  "allOf": [
    { "$ref": "/command/hr/persons" },
    {
      "properties": {
        "version": {
          "type": "integer",
          "minimum": 0,
          "maximum": 0
        },
        "name": {
          "type": "string",
          "pattern": "enterNewPerson"
        },
        "payload": {
          "type": "object",
          "properties": {
            "firstname": {
              "type": "string"
            },
            "lastname": {
              "type": "string"
            },
            "email": {
              "type": "string"
            }
          },
          "required": ["firstname", "lastname", "email"]
        }
      },
      "required": ["payload"]
    }
  ]
}
```

## File: `test/integration/fixture/migration/v2/hr/persons/aggregate.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineAggregate({
module.exports = require('../../../../../../../').defineAggregate({
  name: 'persons', // optional, default is last part of path name
  version: 0, // optional, default 0
  defaultCommandPayload: 'payload',
  defaultEventPayload: 'payload',
  defaultPreConditionPayload: 'payload'
},
{
  persons: []
})
.defineSnapshotNeed(function (loadingTime, events, aggregate) {
  return events.length >= 2;
});
```

## File: `test/integration/fixture/migration/v2/hr/persons/command.json`
```json
{
  "title": "command/hr/persons",
  "allOf": [
    { "$ref": "/command/hr" },
    {
      "properties": {
        "aggregate": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "pattern": "persons"
            }
          }
        }
      }
    }
  ]
}
```

## File: `test/integration/fixture/migration/v2/hr/persons/commands/enterNewPerson_v1.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineCommand({
module.exports = require('../../../../../../../../').defineCommand({
  name: 'enterNewPerson',
  version: 1
}, function (data, aggregate) {
  aggregate.apply('enteredNewPerson', data, 1);
});
```

## File: `test/integration/fixture/migration/v2/hr/persons/events/enteredNewPerson_v0.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineEvent({
module.exports = require('../../../../../../../../').defineEvent({
  name: 'enteredNewPerson',
  version: 0
}, function (data, aggregate) {
  // console.log('OOOOLLLLLDDDDDDD');
  aggregate.get('persons').push(data);
});
```

## File: `test/integration/fixture/migration/v2/hr/persons/events/enteredNewPerson_v1.js`
```javascript
module.exports = require('../../../../../../../../').defineEvent({
  name: 'enteredNewPerson',
  version: 1
}, function (data, aggregate) {
  // console.log('NNNNEEEEEWWWWWWW');
  aggregate.get('persons').push(data);
});
```

## File: `test/integration/fixture/migration/v2/hr/persons/validationRules/enterNewPerson_v1.json`
```json
{
  "title": "enterNewPerson",
  "version": 0,
  "allOf": [
    { "$ref": "/command/hr/persons" },
    {
      "properties": {
        "version": {
          "type": "integer",
          "minimum": 1,
          "maximum": 1
        },
        "name": {
          "type": "string",
          "pattern": "enterNewPerson"
        },
        "payload": {
          "type": "object",
          "properties": {
            "firstname": {
              "type": "string"
            },
            "lastname": {
              "type": "string"
            }
          },
          "required": ["firstname", "lastname"],
          "additionalProperties": false
        }
      },
      "required": ["payload"]
    }
  ]
}
```

## File: `test/integration/fixture/set1/command.json`
```json
{
  "title": "command",
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "context": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        }
      },
      "required": ["name"]
    },
    "aggregate": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        }
      },
      "required": ["name"]
    },
    "name": {
      "type": "string"
    },
    "payload": {
      "type": "object",
      "properties": {
      },
      "required": []
    },
    "meta": {
      "type": "object",
      "properties": {
        "userId": {
          "type": "string"
        }
      },
      "required": []
    },
    "revision": {
      "type": "integer",
      "minimum": 0
    },
    "version": {
      "type": "integer",
      "minimum": 0
    }
  },
  "required": ["id", "context", "aggregate", "name"]
}
```

## File: `test/integration/fixture/set1/cart/aggregate.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineAggregate({
module.exports = require('../../../../../').defineAggregate({
    name: 'cart'//, // optional, default is last part of path name
//    version: 1//, // optional, default 1
  }
);
```

## File: `test/integration/fixture/set1/cart/enterNewPerson.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineCommand({
module.exports = require('../../../../../').defineCommand({
  name: 'enterNewPerson',  // optional, default is file name without extension
  // version: 1, // optional, default 0
  payload: 'payload' // if not defined it will pass the whole command...
}, function (data, aggregate) {
  aggregate.apply('enteredNewPerson', data);
  // or
  // aggregate.apply({
  //   event: 'enteredNewPerson',
  //   payload: data
  // });
});
```

## File: `test/integration/fixture/set1/cart/enteredNewPerson.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineEvent({
module.exports = require('../../../../../').defineEvent({
  name: 'enteredNewPerson', // optional, default is file name without extension
  version: 3, // optional, default 0
  payload: 'payload' // if not defined it will pass the whole event...
}, function (data, aggregate) {
  aggregate.set('personId', data.personId);
});
```

## File: `test/integration/fixture/set1/hr/command.json`
```json
{
  "title": "command/hr",
  "allOf": [
    { "$ref": "/command" },
    {
      "properties": {
        "context": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "pattern": "hr"
            }
          }
        }
      }
    }
  ]
}
```

## File: `test/integration/fixture/set1/hr/context.js`
```javascript
//module.exports = require('cqrs-domain').defineContext({
module.exports = require('../../../../../').defineContext({
  name: 'hr'
});
```

## File: `test/integration/fixture/set1/hr/contract/command.json`
```json
{
  "title": "command/hr/contract",
  "allOf": [
    { "$ref": "/command/hr" },
    {
      "properties": {
        "aggregate": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "pattern": "contract"
            }
          }
        }
      }
    }
  ]
}
```

## File: `test/integration/fixture/set1/hr/person/aggregate.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineAggregate({
module.exports = require('../../../../../../').defineAggregate({
  name: 'person', // optional, default is last part of path name
  version: 3, // optional, default 0
  defaultCommandPayload: 'payload'//,
//  defaultEventPayload: 'payload'
},
// optionally, define some initialization data...
{
  emails: ['default@mycomp.org'],
  phoneNumbers: []
})
.defineCommandAwareAggregateIdGenerator(function (cmd) {
  return cmd.id + require('uuid').v4().toString();
})
// define snapshot need algorithm...
.defineSnapshotNeed(function (loadingTime, events, aggregate) {
  return events.length >= 20;
})
.defineIgnoreSnapshot({
  version: 0
}, function (data) {
  return true;
})
//.defineIgnoreSnapshot({
//  version: 0
//}, true)
//.defineIgnoreSnapshot({
//  version: 0
//}) // default true
// always convert directly to newest version...
.defineSnapshotConversion({
  version: 2
}, function (data, aggregate) {
  aggregate.set('emails', data.emails);
  aggregate.set('phoneNumbers', data.phoneNumbers);

  aggregate.set('firstname', data.firstName);
  aggregate.set('lastname', data.lastName);
})
// always convert directly to newest version...
.defineSnapshotConversion({
  version: 1
}, function (data, aggregate) {
  aggregate.set('emails', data.emails);
  aggregate.set('phoneNumbers', data.phoneNumbers);

  var names = data.name.split(' ');
  aggregate.set('firstname', names[0]);
  aggregate.set('lastname', names[1]);
});
// info to me: when loaded a snapshot create a new snapshot with same revision with newer version
```

## File: `test/integration/fixture/set1/hr/person/command.json`
```json
{
  "title": "command/hr/person",
  "allOf": [
    { "$ref": "/command/hr" },
    {
      "properties": {
        "aggregate": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "pattern": "person"
            }
          }
        }
      }
    }
  ]
}
```

## File: `test/integration/fixture/set1/hr/person/personProperties.json`
```json
{
  "title": "command/hr/person/personProperties",
  "type": "object",
  "properties": {
    "firstname": {
      "type": "string"
    },
    "lastname": {
      "type": "string"
    },
    "email": {
      "type": "string"
    }
  },
  "required": ["firstname", "lastname", "email"]
}
```

## File: `test/integration/fixture/set1/hr/person/businessRules/atLeast1EMail.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineBusinessRule({
module.exports = require('../../../../../../../').defineBusinessRule({
  name: 'atLeast1EMail', // optional, default is file name without extension
  description: 'at least one character should be in email address', // optional
  priority: 1 // optional, default Infinity, all business rules will be sorted by this value
}, function (changed, previous, events, command) {
  
  for (var i = 0, len = changed.get('emails').length; i < len; i++) {
    var email = changed.get('emails')[i];
    if (email.length < 1) {
      // throw new Error('an email address is needed');
      // or
      throw new Error(); // if no error message is defined then the description will be taken
    }
  }

});
```

## File: `test/integration/fixture/set1/hr/person/businessRules/nameEquality.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineBusinessRule({
module.exports = require('../../../../../../../').defineBusinessRule({
  name: 'nameEquality', // optional, default is file name without extension
  description: 'firstname should never be equal lastname'
  // priority: 1 // optional, default Infinity, all business rules will be sorted by this value
}, function (changed, previous, events, command, callback) {
  if (changed.get('firstname') === changed.get('lastname')) {
    return callback('names not valid');
    // or
    // return callback(new Error('names not valid'));
    // or
    // return callback(new Error()); // if no error message is defined then the description will be taken
  }
  callback(null);
});
```

## File: `test/integration/fixture/set1/hr/person/commandHandlers/enterNewSpecialPerson.js`
```javascript
// Is your use case not solvable without a custom command handling? Sagas? Micro-Services?

// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineCommandHandler({
module.exports = require('../../../../../../../').defineCommandHandler({
  name: 'enterNewSpecialPerson'//,  // optional, default is file name without extension
  // version: 1, // optional, default 0
  // payload: 'payload' // if not defined it will pass the whole command...
}, function (aggId, cmd, commandHandler, callback) {
  
  commandHandler.loadAggregate(cmd, aggId, function (err, aggregate, stream) {
    if (err) {
      return callback(err);
    }
    
    callback(null, [{ my: 'special', ev: 'ent' }]);

//    // check if destroyed, check revision, validate command
//    var err = commandHandler.verifyAggregate(aggregate, cmd);
//    if (err) {
//      return callback(err);
//    }
//
//    // call api or emit a command or whatever...
//    // and at the end perhaps you call: commandHandler.handle(cmd, callback);
  });
});
```

## File: `test/integration/fixture/set1/hr/person/commands/enterNewPerson.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineCommand({
module.exports = require('../../../../../../../').defineCommand({
//  name: 'enterNewPerson',  // optional, default is file name without extension
  // version: 1, // optional, default 0
//  payload: 'payload' // if not defined it will use what is defined as default in aggregate or pass the whole command...
}, function (data, aggregate) {
  aggregate.apply('enteredNewPerson', data);
  // or
  // aggregate.apply({
  //   event: 'enteredNewPerson',
  //   payload: data
  // });
});
```

## File: `test/integration/fixture/set1/hr/person/commands/unregisterAllContactInformation.js`
```javascript
var _ = require('lodash');

// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineCommand({
module.exports = require('../../../../../../../').defineCommand({
  name: 'unregisterAllContactInformation',  // optional, default is file name without extension
  version: 2, // optional, default 0
  payload: '' // if not defined it will use what is defined as default in aggregate or pass the whole command...
}, function (cmd, aggregate) {

  _.each(aggregate.get('phoneNumbers'), function(number) {
    aggregate.apply('unregisteredPhoneNumber', {
      number: number
    });
    // or
    // aggregate.apply({
    //   event: 'unregisteredPhoneNumber',
    //   payload: {
    //     number: number
    //   }
    // });
  });

  _.each(aggregate.get('emails'), function(mail) {
    aggregate.apply('unregisteredEMailAddress', {
      email: mail
    });
    // or
    // aggregate.apply(aggregate.toEvent({
    //   event: 'unregisteredEMailAddress',
    //   payload: {
    //     email: mail
    //   }
    // });
  });
});
```

## File: `test/integration/fixture/set1/hr/person/commands/unregisterAllContactInformation_v1.js`
```javascript
var _ = require('lodash');

// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineCommand({
module.exports = require('../../../../../../../').defineCommand({
  name: 'unregisterAllContactInformation', // optional, default is file name without extension
  version: 1, // optional, default 0
  payload: '' // if not defined it will use what is defined as default in aggregate or pass the whole command...
}, function (cmd, aggregate) {

  if (cmd.payload.indexOf('phoneNumbers') >= 0)  {
    _.each(aggregate.get('phoneNumbers'), function(number) {
      aggregate.apply('unregisteredPhoneNumber', {
        number: number
      });
      // or
      // aggregate.apply({
      //   event: 'unregisteredPhoneNumber',
      //   payload: {
      //     number: number
      //   }
      // });
    });
  }

  if (cmd.payload.indexOf('emails') >= 0) {
    _.each(aggregate.get('emails'), function(mail) {
      aggregate.apply('unregisteredEMailAddress', {
        mail: mail
      });
      // or
      // aggregate.apply({
      //   event: 'unregisteredEMailAddress',
      //   payload: {
      //     mail: mail
      //   }
      // });
    });
  }
});
```

## File: `test/integration/fixture/set1/hr/person/eventTransformers/enteredNewPerson_v3.js`
```javascript
//module.exports = require('cqrs-domain').defineEvent({
module.exports = [
  require('../../../../../../../').defineLoadingEventTransformer({
    name: 'enteredNewPerson', // optional, default is file name without extension
    version: 3
  }, function (evt) {
    if (evt.payload.firstname) {
      if (evt.payload.firstname.indexOf('_encrypted_') < 0) throw new Error('Encrypted prop not found!\nThis should not happen!');
      evt.payload.firstname = evt.payload.firstname.replace('_encrypted_', '');
    }
    return evt;
  }),
  require('../../../../../../../').defineCommittingEventTransformer({
    name: 'enteredNewPerson', // optional, default is file name without extension
    version: 3
  }, function (evt) {
    if (evt.payload.firstname) {
      if (evt.payload.firstname.indexOf('_encrypted_') === 0) throw new Error('Encrypted prop found!\nThis should not happen!');
      evt.payload.firstname = '_encrypted_' + evt.payload.firstname;
    }
    return evt;
  })
];
```

## File: `test/integration/fixture/set1/hr/person/events/enteredNewPerson.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineEvent({
module.exports = require('../../../../../../../').defineEvent({
  name: 'enteredNewPerson', // optional, default is file name without extension
  version: 3, // optional, default 0
  payload: 'payload' // if not defined it will pass the whole event...
}, function (data, aggregate) {
  aggregate.set('firstname', data.firstname);
  aggregate.set('lastname', data.lastname);
  aggregate.get('emails').push(data.email);
});
```

## File: `test/integration/fixture/set1/hr/person/events/enteredNewPerson_v1.js`
```javascript
//module.exports = require('cqrs-domain').defineEvent({
module.exports = require('../../../../../../../').defineEvent({
  name: 'enteredNewPerson', // optional, default is file name without extension
  payload: 'payload' // if not defined it will pass the whole event...
}, function (data, aggregate) {
  var names = data.name.split(' ');
  aggregate.set('firstname', names[0]);
  aggregate.set('lastname', names[1]);
});
```

## File: `test/integration/fixture/set1/hr/person/events/enteredNewPerson_v2.js`
```javascript
//module.exports = require('cqrs-domain').defineEvent({
module.exports = require('../../../../../../../').defineEvent({
  name: 'enteredNewPerson', // optional, default is file name without extension
  version: 2,
  payload: 'payload' // if not defined it will pass the whole event...
}, function (data, aggregate) {
  aggregate.set('firstname', data.firstName);
  aggregate.set('lastname', data.lastName);
});
```

## File: `test/integration/fixture/set1/hr/person/events/unregisteredEMailAddress.js`
```javascript
var _ = require('lodash');

// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineEvent({
module.exports = require('../../../../../../../').defineEvent({
  name: 'unregisteredEMailAddress', // optional, default is file name without extension
  // version: 1, // optional, default 0
  payload: 'payload' // if not defined it will pass the whole event...
}, function (data, aggregate) {
  aggregate.set('emails', _.without(aggregate.get('emails'), data.email));
});
```

## File: `test/integration/fixture/set1/hr/person/events/unregisteredPhoneNumber.js`
```javascript
var _ = require('lodash');

// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineEvent({
module.exports = require('../../../../../../../').defineEvent({
  name: 'unregisteredPhoneNumber'//,  // optional, default is file name without extension
  // version: 1, // optional, default 0
  // payload: 'payload' // if not defined it will pass the whole event...
}, function (cmd, aggregate) {
  aggregate.set('phoneNumbers', _.without(aggregate.get('phoneNumbers'), cmd.payload.number));
});
```

## File: `test/integration/fixture/set1/hr/person/preConditions/firstnameSet.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineBusinessRule({
module.exports = require('../../../../../../../').definePreCondition({
  name: ['unregisterAllContactInformation'],  // optional, default is file name without extension
  version: 2, // optional, default 0
  payload: '', // if not defined it will use what is defined as default in aggregate or pass the whole command...
  description: 'firstname should always be set',
  priority: 2 // optional, default Infinity, all pre-conditions will be sorted by this value
}, function (command, agg, callback) {
  if (!agg.has('firstname')) {
    return callback('not personalized');
    // or
    // return callback(new Error('not personalized'));
    // or
    // return callback(new Error()); // if no error message is defined then the description will be taken
  }
  callback(null);
});
```

## File: `test/integration/fixture/set1/hr/person/preConditions/isAuthorized.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineBusinessRule({
module.exports = require('../../../../../../../').definePreCondition({
  name: '',  // optional, default is file name without extension
  payload: '', // if not defined it will use what is defined as default in aggregate or pass the whole command...
  description: 'authorization',
  priority: 1 // optional, default Infinity, all pre-conditions will be sorted by this value
}, function (command, agg, callback) {
  if (command.notAuthorized) {
    return callback('not authorized');
    // or
    // return callback(new Error('not authorized'));
    // or
    // return callback(new Error()); // if no error message is defined then the description will be taken
  }
  callback(null);
});
```

## File: `test/integration/fixture/set1/hr/person/preConditions/prio1PreconditionAllCommands.js`
```javascript
module.exports = require('../../../../../../../').definePreCondition({
  name: '',
  description: 'Fails if firstname is rumpelstilz',
  priority: 1
}, function (command) {
  if (command.payload.firstname === 'rumpelstilz') {
    throw new Error('Precondition with prio 1 failed (all commands)');
  }
});
```

## File: `test/integration/fixture/set1/hr/person/preConditions/prio2PreconditionSpecificCommand.js`
```javascript
module.exports = require('../../../../../../../').definePreCondition({
  name: 'enterNewPerson2',
  description: 'Fails if firstname is rumpelstilz',
  priority: 2
}, function (command) {
  if (command.payload.firstname === 'rumpelstilz1') {
    throw new Error('Precondition with prio 2 failed (specific command)');
  }
});
```

## File: `test/integration/fixture/set1/hr/person/preLoadConditions/preLoadConditionTest.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineBusinessRule({
module.exports = require('../../../../../../../').definePreLoadCondition({
  name: '',  // optional, default is file name without extension
  payload: '', // if not defined it will use what is defined as default in aggregate or pass the whole command...
  description: 'just a nice little test',
  priority: 1 // optional, default Infinity, all pre-conditions will be sorted by this value
}, function (command, callback) {
  if (command.failPreLoadCondition) {
    return callback('precondition failed!');
    // or
    // return callback(new Error('not authorized'));
    // or
    // return callback(new Error()); // if no error message is defined then the description will be taken
  }
  callback(null);
});
```

## File: `test/integration/fixture/set1/hr/person/validationRules/enterNewPerson_v0.json`
```json
{
  "title": "enterNewPerson",
  "version": 0,
  "allOf": [
    { "$ref": "/command/hr/person" },
    {
      "properties": {
        "name": {
          "type": "string",
          "pattern": "enterNewPerson"
        },
        "special": {
          "format": "mySpecialFormat"
        },
        "payload": {
          "$ref": "/command/hr/person/personProperties"
        }
      },
      "required": ["payload"]
    }
  ]
}
```

## File: `test/integration/fixture/set1/hr/person/validationRules/unregisterAllContactInformation_v1.json`
```json
{
  "title": "unregisterAllContactInformation",
  "version": 1,
  "allOf": [
    { "$ref": "/command/hr/person" },
    {
      "version": {
        "type": "integer",
        "minimum": 1,
        "maximum": 1
      },
      "properties": {
        "name": {
          "type": "string",
          "pattern": "unregisterAllContactInformation"
        },
        "payload": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "phoneNumbers",
              "mails"
            ]
          }
        }
      },
      "required": ["version", "payload"]
    }
  ]
}
```

## File: `test/integration/fixture/set1/hr/person/validationRules/unregisterAllContactInformation_v2.json`
```json
{
  "title": "unregisterAllContactInformation",
  "version": 2,
  "allOf": [
    { "$ref": "/command/hr/person" },
    {
      "version": {
        "type": "integer",
        "minimum": 2,
        "maximum": 2
      },
      "properties": {
        "name": {
          "type": "string",
          "pattern": "unregisterAllContactInformation"
        }
      },
      "required": ["version"]
    }
  ]
}
```

## File: `test/integration/fixture/set1/manufactoring/command.json`
```json
{
  "title": "command/manufactoring",
  "allOf": [
    { "$ref": "/command" },
    {
      "properties": {
        "context": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "pattern": "manufactoring"
            }
          }
        }
      }
    }
  ]
}
```

## File: `test/integration/fixture/set1/manufactoring/context.js`
```javascript
//module.exports = require('cqrs-domain').defineContext({
module.exports = require('../../../../../').defineContext({
});
```

## File: `test/integration/fixture/set1/manufactoring/customer/command.json`
```json
{
  "title": "command/manufactoring/customer",
  "allOf": [
    { "$ref": "/command/manufactoring" },
    {
      "properties": {
        "aggregate": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "pattern": "customer"
            }
          }
        }
      }
    }
  ]
}
```

## File: `test/integration/fixture/set1/manufactoring/order/command.json`
```json
{
  "title": "command/manufactoring/order",
  "allOf": [
    { "$ref": "/command/manufactoring" },
    {
      "properties": {
        "aggregate": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "pattern": "order"
            }
          }
        }
      }
    }
  ]
}
```

## File: `test/integration/fixture/set2/command.json`
```json
{
  "title": "command",
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "command": {
      "type": "string"
    },
    "payload": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        }
      },
      "required": []
    },
    "head": {
      "type": "object",
      "properties": {
        "revision": {
          "type": "integer",
          "minimum": 0
        },
        "userId": {
          "type": "string"
        }
      },
      "required": []
    }
  },
  "required": ["id", "command"]
}
```

## File: `test/integration/fixture/set2/cart/cart.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineAggregate({
module.exports = require('../../../../../').defineAggregate({
    name: 'cart'//, // optional, default is last part of path name
//    version: 1//, // optional, default 1
  }
);
```

## File: `test/integration/fixture/set2/person/person.js`
```javascript
var _ = require('lodash');

// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineEvent({
module.exports = [

  // aggregate
  require('../../../../../').defineAggregate({
    name: 'person'//, // optional, default is last part of path name
    // versionPath: 'version', // can be defined globally, but can be overwritten here...
    },
    // optionally, define some initialization data...
    {
      emails: ['default@mycomp.org'],
      phoneNumbers: []
    })
    // define snapshot need algorithm...
    .defineSnapshotNeed(function (loadingTime, events, aggregate) {
      return events.length >= 20;
    }
  ),

  // commands
  require('../../../../../').defineCommand({
    name: 'enterNewPerson',  // optional, default is file name without extenstion and without _vx
    // version: 1, // optional, default 0
    payload: 'payload' // if not defined it will pass the whole command...
  }, function (data, aggregate) {
    aggregate.apply('enteredNewPerson', data);
    // or
    // aggregate.apply({
    //   event: 'enteredNewPerson',
    //   payload: data
    // });
  }),

  require('../../../../../').defineCommand({
    name: 'unregisterAllContactInformation'//,  // optional, default is file name without extenstion and without _vx
    // payload: 'payload' // if not defined it will pass the whole command...
  }, function (cmd, aggregate) {

    _.each(aggregate.get('phoneNumbers'), function(number) {
      aggregate.apply('unregisteredPhoneNumber', {
        number: number
      });
      // or
      // aggregate.apply({
      //   event: 'unregisteredPhoneNumber',
      //   payload: {
      //     number: number
      //   }
      // });
    });

    _.each(aggregate.get('emails'), function(mail) {
      aggregate.apply('unregisteredEMailAddress', {
        email: mail
      });
      // or
      // aggregate.apply(aggregate.toEvent({
      //   event: 'unregisteredEMailAddress',
      //   payload: {
      //     email: mail
      //   }
      // });
    });
  }),
  

  // events

  require('../../../../../').defineEvent({
    name: 'enteredNewPerson', // optional, default is file name without extension
    payload: 'payload' // if not defined it will pass the whole event...
  }, function (data, aggregate) {
    aggregate.set('firstname', data.firstname);
    aggregate.set('lastname', data.lastname);
    aggregate.get('emails').push(data.email);
  }),

  require('../../../../../').defineEvent({
    name: 'unregisteredEMailAddress', // optional, default is file name without extenstion and without _vx
    // version: 1, // optional, default 0
    payload: 'payload' // if not defined it will pass the whole event...
  }, function (data, aggregate) {
    aggregate.set('emails', _.without(aggregate.get('emails'), data.email));
  }),

  require('../../../../../').defineEvent({
    name: 'unregisteredPhoneNumber'//,  // optional, default is file name without extenstion and without _vx
    // version: 1, // optional, default 0
    // payload: 'payload' // if not defined it will pass the whole event...
  }, function (cmd, aggregate) {
    aggregate.set('phoneNumbers', _.without(aggregate.get('phoneNumbers'), cmd.payload.number));
  })

];
```

## File: `test/integration/fixture/set2/person/businessRules/rules.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineBusinessRule({
module.exports = [

  require('../../../../../../').definePreCondition({
    name: 'unregisterAllContactInformation',  // optional, default is file name without extension
    payload: '', // if not defined it will use what is defined as default in aggregate or pass the whole command...
    description: 'firstname should always be set'
  }, function (command, agg) {
    if (!agg.has('firstname')) {
      throw new Error('not personalized');
    }
  }),

  require('../../../../../../').defineBusinessRule({
    name: 'nameEquality', // optional, default is file name without extenstion
    description: 'firstname should never be equal lastname'//,
    // priority: 1 // optional, default Infinity, all business rules will be sorted by this value
  }, function (changed, previous, events, command, callback) {
    if (changed.get('firstname') === changed.get('lastname')) {
      return callback('names not valid');
      // or
      // return callback(new Error('names not valid'));
      // or
      // return callback(new Error()); // if no error message is defined then the description will be taken
    }
    callback(null);
  }),

  require('../../../../../../').defineBusinessRule({
    name: 'atLeast1EMail', // optional, default is file name without extenstion
    description: 'at least one character should be in email address', // optional
    priority: 1 // optional, default Infinity, all business rules will be sorted by this value
  }, function (changed, previous, events, command) {

    for (var i = 0, len = changed.get('emails').length; i < len; i++) {
      var email = changed.get('emails')[i];
      if (email.length < 1) {
        // throw new Error('an email address is needed');
        // or
        throw new Error(); // if no error message is defined then the description will be taken
      }
    }

  })
  
];
```

## File: `test/integration/fixture/set2/person/commandHandlers/enterNewSpecialPerson.js`
```javascript
// Is your use case not solvable without a custom command handling? Sagas? Micro-Services?

// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineCommandHandler({
module.exports = require('../../../../../../').defineCommandHandler({
  name: 'enterNewSpecialPerson'//,  // optional, default is file name without extension and without _vx
  // payload: 'payload' // if not defined it will pass the whole command...
}, function (aggId, cmd, commandHandler, callback) {
  commandHandler.loadAggregate(cmd, aggId, function (err, aggregate, stream) {
    if (err) {
      return callback(err);
    }
    
    callback(null, [{ my: 'special', ev: 'ent' }]);

//    // check if destroyed, check revision, validate command
//    var err = commandHandler.verifyAggregate(aggregate, cmd);
//    if (err) {
//      return callback(err);
//    }
//
//    // call api or emit a command or whatever...
//    // and at the end perhaps you call: commandHandler.handle(cmd, callback);
  });
});
```

## File: `test/integration/fixture/set2/person/validationRules/enterNewPerson.json`
```json
{
  "title": "enterNewPerson",
  "allOf": [
    { "$ref": "/command" },
    {
      "properties": {
        "command": {
          "type": "string",
          "pattern": "enterNewPerson"
        },
        "payload": {
          "type": "object",
          "properties": {
            "firstname": {
              "type": "string"
            },
            "lastname": {
              "type": "string"
            },
            "email": {
              "type": "string"
            }
          },
          "required": ["firstname", "lastname", "email"]
        }
      },
      "required": ["command", "payload"]
    }
  ]
}
```

## File: `test/integration/fixture/set2/person/validationRules/unregisterAllContactInformation.json`
```json
{
  "title": "unregisterAllContactInformation",
  "allOf": [
    { "$ref": "/command" },
    {
      "properties": {
        "command": {
          "type": "string",
          "pattern": "unregisterAllContactInformation"
        }
      },
      "required": ["command"]
    }
  ]
}
```

## File: `test/integration/fixture/set3/command.json`
```json
{
  "title": "command",
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "command": {
      "type": "string"
    },
    "payload": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        }
      },
      "required": []
    },
    "head": {
      "type": "object",
      "properties": {
        "revision": {
          "type": "integer",
          "minimum": 0
        },
        "userId": {
          "type": "string"
        }
      },
      "required": []
    }
  },
  "required": ["id", "command"]
}
```

## File: `test/integration/fixture/set3/cart/cart.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineAggregate({
module.exports = require('../../../../../').defineAggregate({
    name: 'cart'//, // optional, default is last part of path name
//    version: 1//, // optional, default 1
  }
);
```

## File: `test/integration/fixture/set3/cart/enterNewPerson.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineCommand({
module.exports = require('../../../../../').defineCommand({
  name: 'enterNewPerson',  // optional, default is file name without extension
  // version: 1, // optional, default 0
  payload: 'payload' // if not defined it will pass the whole command...
}, function (data, aggregate) {
  aggregate.apply('enteredNewPerson', data);
  // or
  // aggregate.apply({
  //   event: 'enteredNewPerson',
  //   payload: data
  // });
});
```

## File: `test/integration/fixture/set3/cart/enteredNewPerson.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineEvent({
module.exports = require('../../../../../').defineEvent({
  name: 'enteredNewPerson', // optional, default is file name without extension
  version: 3, // optional, default 0
  payload: 'payload' // if not defined it will pass the whole event...
}, function (data, aggregate) {
  aggregate.set('personId', data.personId);
});
```

## File: `test/integration/fixture/set3/person/person.js`
```javascript
var _ = require('lodash');

// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineEvent({
module.exports = [

  // aggregate
  require('../../../../../').defineAggregate({
    name: 'person'//, // optional, default is last part of path name
    // versionPath: 'version', // can be defined globally, but can be overwritten here...
    },
    // optionally, define some initialization data...
    {
      emails: ['default@mycomp.org'],
      phoneNumbers: []
    })
    // define snapshot need algorithm...
    .defineSnapshotNeed(function (loadingTime, events, aggregate) {
      return events.length >= 20;
    }
  ),

  // commands
  require('../../../../../').defineCommand({
    name: 'enterNewPerson',  // optional, default is file name without extenstion and without _vx
    // version: 1, // optional, default 0
    payload: 'payload' // if not defined it will pass the whole command...
  }, function (data, aggregate) {
    aggregate.apply('enteredNewPerson', data);
    // or
    // aggregate.apply({
    //   event: 'enteredNewPerson',
    //   payload: data
    // });
  }),

  require('../../../../../').defineCommand({
    name: 'unregisterAllContactInformation'//,  // optional, default is file name without extenstion and without _vx
    // payload: 'payload' // if not defined it will pass the whole command...
  }, function (cmd, aggregate) {

    _.each(aggregate.get('phoneNumbers'), function(number) {
      aggregate.apply('unregisteredPhoneNumber', {
        number: number
      });
      // or
      // aggregate.apply({
      //   event: 'unregisteredPhoneNumber',
      //   payload: {
      //     number: number
      //   }
      // });
    });

    _.each(aggregate.get('emails'), function(mail) {
      aggregate.apply('unregisteredEMailAddress', {
        email: mail
      });
      // or
      // aggregate.apply(aggregate.toEvent({
      //   event: 'unregisteredEMailAddress',
      //   payload: {
      //     email: mail
      //   }
      // });
    });
  }),
  

  // events

  require('../../../../../').defineEvent({
    name: 'enteredNewPerson', // optional, default is file name without extension
    payload: 'payload' // if not defined it will pass the whole event...
  }, function (data, aggregate) {
    aggregate.set('firstname', data.firstname);
    aggregate.set('lastname', data.lastname);
    aggregate.get('emails').push(data.email);
  }),

  require('../../../../../').defineEvent({
    name: 'unregisteredEMailAddress', // optional, default is file name without extenstion and without _vx
    // version: 1, // optional, default 0
    payload: 'payload' // if not defined it will pass the whole event...
  }, function (data, aggregate) {
    aggregate.set('emails', _.without(aggregate.get('emails'), data.email));
  }),

  require('../../../../../').defineEvent({
    name: 'unregisteredPhoneNumber'//,  // optional, default is file name without extenstion and without _vx
    // version: 1, // optional, default 0
    // payload: 'payload' // if not defined it will pass the whole event...
  }, function (cmd, aggregate) {
    aggregate.set('phoneNumbers', _.without(aggregate.get('phoneNumbers'), cmd.payload.number));
  })

];
```

## File: `test/integration/fixture/set3/person/businessRules/rules.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineBusinessRule({
module.exports = [
  
  require('../../../../../../').defineBusinessRule({
    name: 'nameEquality', // optional, default is file name without extenstion
    description: 'firstname should never be equal lastname'//,
    // priority: 1 // optional, default Infinity, all business rules will be sorted by this value
  }, function (changed, previous, events, command, callback) {
    if (changed.get('firstname') === changed.get('lastname')) {
      return callback('names not valid');
      // or
      // return callback(new Error('names not valid'));
      // or
      // return callback(new Error()); // if no error message is defined then the description will be taken
    }
    callback(null);
  }),

  require('../../../../../../').defineBusinessRule({
    name: 'atLeast1EMail', // optional, default is file name without extenstion
    description: 'at least one character should be in email address', // optional
    priority: 1 // optional, default Infinity, all business rules will be sorted by this value
  }, function (changed, previous, events, command) {

    for (var i = 0, len = changed.get('emails').length; i < len; i++) {
      var email = changed.get('emails')[i];
      if (email.length < 1) {
        // throw new Error('an email address is needed');
        // or
        throw new Error(); // if no error message is defined then the description will be taken
      }
    }

  })
  
];
```

## File: `test/integration/fixture/set3/person/commandHandlers/enterNewSpecialPerson.js`
```javascript
// Is your use case not solvable without a custom command handling? Sagas? Micro-Services?

// if exports is an array, it will be the same like loading multiple files...
//module.exports = require('cqrs-domain').defineCommandHandler({
module.exports = require('../../../../../../').defineCommandHandler({
  name: 'enterNewSpecialPerson'//,  // optional, default is file name without extension and without _vx
  // payload: 'payload' // if not defined it will pass the whole command...
}, function (cmd, commandHandler, callback) {
  // if cmd was sent without aggregateId, now in cmd there is a generated aggregateId...

  var id = cmd.aggregate && cmd.aggregate.id ? cmd.aggregate.id : cmd.payload.id;
  
  commandHandler.loadAggregate(cmd, id, function (err, aggregate, stream) {
    if (err) {
      return callback(err);
    }
    
    callback(null, [{ my: 'special', ev: 'ent' }]);

//    // check if destroyed, check revision, validate command
//    var err = commandHandler.verifyAggregate(aggregate, cmd);
//    if (err) {
//      return callback(err);
//    }
//
//    // call api or emit a command or whatever...
//    // and at the end perhaps you call: commandHandler.handle(cmd, callback);
  });
});
```

## File: `test/integration/fixture/set3/person/validationRules/enterNewPerson.json`
```json
{
  "title": "enterNewPerson",
  "allOf": [
    { "$ref": "/command" },
    {
      "properties": {
        "command": {
          "type": "string",
          "pattern": "enterNewPerson"
        },
        "payload": {
          "type": "object",
          "properties": {
            "firstname": {
              "type": "string"
            },
            "lastname": {
              "type": "string"
            },
            "email": {
              "type": "string"
            }
          },
          "required": ["firstname", "lastname", "email"]
        }
      },
      "required": ["command", "payload"]
    }
  ]
}
```

## File: `test/integration/fixture/set3/person/validationRules/unregisterAllContactInformation.json`
```json
{
  "title": "unregisterAllContactInformation",
  "allOf": [
    { "$ref": "/command" },
    {
      "properties": {
        "command": {
          "type": "string",
          "pattern": "unregisterAllContactInformation"
        }
      },
      "required": ["command"]
    }
  ]
}
```

## File: `test/unit/aggregateLockTest.js`
```javascript
var expect = require('expect.js'),
  async = require('async'),
  aggregatelock = require('../../lib/lock'),
  Base = require('../../lib/lock/base'),
  InMemory = require('../../lib/lock/databases/inmemory');

describe('AggregateLock', function() {

  it('it should have the correct interface', function() {

    expect(aggregatelock).to.be.an('object');
    expect(aggregatelock.create).to.be.a('function');
    expect(aggregatelock.Lock).to.eql(Base);

  });

  describe('calling create', function() {

    describe('without options', function() {

      it('it should return with the in memory queue', function() {

        var lock = aggregatelock.create();
        expect(lock).to.be.a('object');

      });

      describe('but with a callback', function() {

        it('it should callback with lock object', function(done) {

          aggregatelock.create(function(err, lock) {
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
          aggregatelock.create({ type: 'strangeDb' });
        }).to.throwError();

      });

      it('it should callback with an error', function(done) {

        expect(function() {
          aggregatelock.create({ type: 'strangeDb' }, function(err) {
            expect(err).to.be.ok();
            done();
          });
        }).to.throwError();

      });

    });

    describe('with options of an own db implementation', function() {

      it('it should return with the an instance of that implementation', function() {

        var lock = aggregatelock.create({ type: InMemory });
        expect(lock).to.be.a(InMemory);

      });

    });

    describe('with options containing a type property with the value of', function() {

      var types = ['inmemory', 'mongodb', 'tingodb', 'redis', 'dynamodb'/*, 'couchdb', 'azuretable'*/];

      types.forEach(function(type) {

        describe('"' + type + '"', function() {

          var lock;

          describe('without callback', function() {

            afterEach(function(done) {
              lock.disconnect(done);
            });

            it('it should return with the correct lock', function() {

              lock = aggregatelock.create({ type: type });
              expect(lock).to.be.a('object');
              expect(lock).to.be.a(Base);
              expect(lock.connect).to.be.a('function');
              expect(lock.disconnect).to.be.a('function');
              expect(lock.getNewId).to.be.a('function');
              expect(lock.reserve).to.be.a('function');
              expect(lock.getAll).to.be.a('function');
              expect(lock.resolve).to.be.a('function');

            });

          });

          describe('with callback', function() {

            afterEach(function(done) {
              lock.disconnect(done);
            });

            it('it should return with the correct lock', function(done) {

              aggregatelock.create({ type: type }, function(err, resL) {
                expect(err).not.to.be.ok();
                lock = resL;
                expect(lock).to.be.a('object');
                done();
              });

            });

          });

          describe('calling connect', function () {

            afterEach(function(done) {
              lock.disconnect(done);
            });

            describe('with a callback', function () {

              it('it should callback successfully', function(done) {

                lock = aggregatelock.create({ type: type });
                lock.connect(function (err) {
                  expect(err).not.to.be.ok();
                  done();
                })

              });

            });

            describe('without a callback', function () {

              it('it should emit connect', function(done) {

                lock = aggregatelock.create({ type: type });
                lock.once('connect', done);
                lock.connect()

              });

            });

          });

          describe('having connected', function() {

            describe('calling disconnect', function() {

              beforeEach(function(done) {
                lock = aggregatelock.create({ type: type });
                lock.connect(done);
              });

              it('it should callback successfully', function(done) {

                lock.disconnect(function(err) {
                  expect(err).not.to.be.ok();
                  done();
                });

              });

              it('it should emit disconnect', function(done) {

                lock.once('disconnect', done);
                lock.disconnect();

              });

            });

            describe('using the lock', function() {

              before(function(done) {
                lock = aggregatelock.create({ type: type });
                lock.connect(done);
              });

              describe('calling getNewId', function() {

                it('it should callback with a new Id as string', function(done) {

                  lock.getNewId(function(err, id) {
                    expect(err).not.to.be.ok();
                    expect(id).to.be.a('string');
                    done();
                  });

                });

              });

              describe('having no entries', function() {

                before(function(done) {
                  lock.clear(done);
                });

                describe('calling getAll', function() {

                  it('it should callback with an empty array', function(done) {

                    lock.getAll('23', function(err, items) {
                      expect(err).not.to.be.ok();
                      expect(items).to.be.an('array');
                      expect(items).to.have.length(0);
                      done();
                    });

                  });

                });

                describe('calling resolve', function(done) {

                  it('it should callback correctly', function(done) {

                    lock.resolve('23', function(err, nothing) {
                      expect(err).not.to.be.ok();
                      expect(nothing).to.eql(undefined);
                      done();
                    });

                  });

                });

                describe('calling reserve', function(done) {

                  it('it should callback with no error', function(done) {

                    lock.reserve('workerId1', 'aggregateId1', function(err, nothing) {
                      expect(err).not.to.be.ok();
                      expect(nothing).to.eql(undefined);
                      done();
                    });

                  });

                  describe('verifying if the reservation is ok, by calling getAll', function () {

                    it('it should callback the correct items', function (done) {

                      lock.getAll('aggregateId1', function (err, workerIds) {
                        expect(err).not.to.be.ok();
                        expect(workerIds).to.be.an('array');
                        expect(workerIds.length).to.eql(1);
                        expect(workerIds[0]).to.eql('workerId1');
                        done();
                      });

                    });

                  });

                });

              });

              describe('having 3 reservations for an aggregate and 2 reservations with an other aggregate', function() {

                beforeEach(function (done) {
                  lock.clear(function () {
                    async.series([
                      function (callback) {
                        setTimeout(function () {
                          lock.reserve('workerId111', 'aggregateId111', callback);
                        }, 1);
                      },
                      function (callback) {
                        setTimeout(function () {
                          lock.reserve('workerId222', 'aggregateId111', callback);
                        }, 2);
                      },
                      function (callback) {
                        setTimeout(function () {
                          lock.reserve('workerId333', 'aggregateId111', callback);
                        }, 3);
                      },
                      function (callback) {
                        setTimeout(function () {
                          lock.reserve('workerIdFirst', 'aggregateIdSecond', callback);
                        }, 4);
                      },
                      function (callback) {
                        setTimeout(function () {
                          lock.reserve('workerIdSecond', 'aggregateIdSecond', callback);
                        }, 5);
                      }
                    ], done);
                  });
                });

                describe('calling getAll of the first aggregate', function () {

                  it('it should callback with the correct amount of workers', function (done) {

                    lock.getAll('aggregateId111', function (err, workerIds) {
                      expect(err).not.to.be.ok();
                      expect(workerIds).to.be.an('array');
                      expect(workerIds.length).to.eql(3);
                      expect(workerIds[0]).to.eql('workerId111');
                      expect(workerIds[1]).to.eql('workerId222');
                      expect(workerIds[2]).to.eql('workerId333');
                      done();
                    });
                  });

                });

                describe('calling getAll of the second aggregate', function () {

                  it('it should callback with the correct amount of workers', function (done) {

                    lock.getAll('aggregateIdSecond', function (err, workerIds) {
                      expect(err).not.to.be.ok();
                      expect(workerIds).to.be.an('array');
                      expect(workerIds.length).to.eql(2);
                      expect(workerIds[0]).to.eql('workerIdFirst');
                      expect(workerIds[1]).to.eql('workerIdSecond');
                      done();
                    });
                  });

                });

                describe('calling resolve of the first aggregate', function() {

                  it('it should have removed all reservation for this aggregate', function (done) {

                    lock.resolve('aggregateId111', function (err, nothing) {
                      expect(err).not.to.be.ok();
                      expect(nothing).to.eql(undefined);

                      lock.getAll('aggregateId111', function (err, workerIds) {
                        expect(err).not.to.be.ok();
                        expect(workerIds).to.be.an('array');
                        expect(workerIds.length).to.eql(0);
                        done();
                      })
                    })

                  });

                  it('it should not have removed any reservation for the other aggregate', function (done) {

                    lock.resolve('aggregateId111', function (err, nothing) {
                      expect(err).not.to.be.ok();
                      expect(nothing).to.eql(undefined);

                      lock.getAll('aggregateIdSecond', function (err, workerIds) {
                        expect(err).not.to.be.ok();
                        expect(workerIds).to.be.an('array');
                        expect(workerIds.length).to.eql(2);
                        expect(workerIds[0]).to.eql('workerIdFirst');
                        expect(workerIds[1]).to.eql('workerIdSecond');
                        done();
                      })
                    })

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

## File: `test/unit/aggregateModelTest.js`
```javascript
var expect = require('expect.js'),
  AggregateModel = require('../../lib/aggregateModel');

describe('aggregate model', function () {

  describe('creating a new instance', function () {

    describe('without any arguments', function () {

      it('it should throw an error', function () {

        expect(function () {
          new AggregateModel();
        }).to.throwError(/id/);

      });

    });

    describe('with an id as number', function () {

      it('it should throw an error', function () {

        expect(function () {
          new AggregateModel(1234);
        }).to.throwError(/id/);

      });

    });

    describe('with an id as string', function () {

      it('it should not throw an error', function () {

        expect(function () {
          new AggregateModel('12345');
        }).not.to.throwError();

      });

      it('it should return a correct object', function() {

        var agg = new AggregateModel('1234');

        expect(agg).to.be.an('object');
        expect(agg.set).to.be.a('function');
        expect(agg.get).to.be.a('function');
        expect(agg.has).to.be.a('function');
        expect(agg.toJSON).to.be.a('function');
        expect(agg.destroy).to.be.a('function');
        expect(agg.isDestroyed).to.be.a('function');
        expect(agg.setRevision).to.be.a('function');
        expect(agg.getRevision).to.be.a('function');
        expect(agg.getUncommittedEvents).to.be.a('function');
        expect(agg.addUncommittedEvent).to.be.a('function');
        expect(agg.clearUncommittedEvents).to.be.a('function');
        expect(agg.reset).to.be.a('function');

        expect(agg.id).to.eql('1234');
        expect(agg.get('id')).to.eql('1234');

      });

    });

    describe('calling has', function() {

      describe('of an attribute that does exist', function() {

        it('it should return true', function() {

          var agg = new AggregateModel('123456');
          agg.set('a', 'b');

          expect(agg.has('id')).to.eql(true);
          expect(agg.has('a')).to.eql(true);

        });

      });

      describe('of an attribute that does not exist', function() {

        it('it should return false', function() {

          var agg = new AggregateModel('123456');

          expect(agg.has('data222')).to.eql(false);

        });

      });

    });

    describe('calling get', function() {

      describe('of an attribute that does exist', function() {

        it('it should return that value', function() {

          var agg = new AggregateModel('123456');
          agg.set('my', 'data');

          expect(agg.get('my')).to.eql('data');

        });

      });

      describe('of an attribute that does not exist', function() {

        it('it should return undefined', function() {

          var agg = new AggregateModel('123456');

          expect(agg.get('data222')).to.eql(undefined);

        });

      });

      describe('of an attribute that is deep', function() {

        it('it should return that value', function() {

          var agg = new AggregateModel('123456');
          agg.set('deep', { data: 'other stuff' });

          expect(agg.get('deep.data')).to.eql('other stuff');

        });

      });

    });

    describe('calling set', function() {

      describe('with a simple key', function() {

        it('it should set it correctly', function() {

          var agg = new AggregateModel('123456');

          agg.set('data', 'a');
          expect(agg.get('data')).to.eql('a');

        });

      });

      describe('with a path as key', function() {

        it('it should set it correctly', function() {

          var agg = new AggregateModel('123456');

          agg.set('path.sub', 'b');
          expect(agg.get('path.sub')).to.eql('b');

        });

      });

      describe('with an object', function() {

        it('it should set it correctly', function() {

          var agg = new AggregateModel('123456');

          agg.set({ tree: 'a', bee: { oh: '3' } });
          expect(agg.get('tree')).to.eql('a');
          expect(agg.get('bee.oh')).to.eql('3');

        });

      });

    });

    describe('calling destroy', function() {

      it('it should mark the vm as to be deleted', function() {

        var agg = new AggregateModel('123456');

        expect(agg.isDestroyed()).to.eql(false);

        agg.destroy();

        expect(agg.isDestroyed()).to.eql(true);

      });

    });

    describe('calling toJSON', function() {

      it('it should return all attributes as Javascript object', function() {

        var agg = new AggregateModel('123456');
        agg.set('data', 'other stuff');
        agg.set('deeper', { a: 'b' });
        var json = agg.toJSON();

        expect(json.id).to.eql('123456');
        expect(json.data).to.eql('other stuff');
        expect(json.deeper.a).to.eql('b');

        expect(json._revision).to.eql(0);
        expect(json._destroyed).to.eql(false);

      });

      describe('having set a revision and having destroyed the aggregate', function () {

        it('it should return all attributes as Javascript object', function() {

          var agg = new AggregateModel('123456');
          agg.setRevision({ context: 'c', aggregate: 'a', aggregateId: 'id' }, 3);

          agg.set('data', 'other stuff');
          agg.set('deeper', { a: 'b' });

          agg.destroy();

          var json = agg.toJSON();

          expect(json.id).to.eql('123456');
          expect(json.data).to.eql('other stuff');
          expect(json.deeper.a).to.eql('b');

          expect(json._revision).to.eql(3);
          expect(json._revisions['c_a_id']).to.eql(3);
          expect(json._destroyed).to.eql(true);

        });

      });

    });

    describe('setting a revision', function () {

      it('it should work as expected', function () {

        var agg = new AggregateModel('1234456745');

        expect(agg.getRevision()).to.eql(0);

        agg.setRevision({ context: 'c', aggregate: 'a', aggregateId: 'id' }, 8);

        expect(agg.getRevision({ context: 'c', aggregate: 'a', aggregateId: 'id' })).to.eql(8);

      });

    });

    describe('mark aggregate as destroyed', function () {

      it('it should work as expected', function () {

        var agg = new AggregateModel('1234456745');

        expect(agg.isDestroyed()).to.eql(false);

        agg.destroy();

        expect(agg.isDestroyed()).to.eql(true);

      });

    });

    describe('adding uncommitted events', function () {

      it('it should work as expected', function () {

        var agg = new AggregateModel('1234456745');
        var evts = agg.getUncommittedEvents();

        expect(evts).to.be.an('array');
        expect(evts.length).to.eql(0);

        agg.addUncommittedEvent({ my: 'evt' });
        agg.addUncommittedEvent({ my2: 'evt2' });

        evts = agg.getUncommittedEvents();

        expect(evts).to.be.an('array');
        expect(evts.length).to.eql(2);
        expect(evts[0].my).to.eql('evt');
        expect(evts[1].my2).to.eql('evt2');

      });

    });

    describe('clearing uncommitted events', function () {

      it('it should work as expected', function () {

        var agg = new AggregateModel('1234456745');
        var evts = agg.getUncommittedEvents();

        expect(evts).to.be.an('array');
        expect(evts.length).to.eql(0);

        agg.addUncommittedEvent({ my: 'evt' });
        agg.addUncommittedEvent({ my2: 'evt2' });

        evts = agg.getUncommittedEvents();

        expect(evts).to.be.an('array');
        expect(evts.length).to.eql(2);
        expect(evts[0].my).to.eql('evt');
        expect(evts[1].my2).to.eql('evt2');

        agg.clearUncommittedEvents();

        evts = agg.getUncommittedEvents();

        expect(evts).to.be.an('array');
        expect(evts.length).to.eql(0);

      });

    });

    describe('calling reset', function () {

      it('it should work as expected', function () {

        var agg = new AggregateModel('1234456745');

        agg.set('my', 'value');

        agg.setRevision({ context: 'c', aggregate: 'a', aggregateId: 'id' }, 8);

        agg.reset({ other: 'value', _revision: 8, _revisions: { 'c_a_id': 8 } });

        expect(agg.getRevision({ context: 'c', aggregate: 'a', aggregateId: 'id' })).to.eql(8);

        expect(agg.get('my')).not.to.be.ok();
        expect(agg.get('other')).to.eql('value');

      });

    });

  });

});
```

## File: `test/unit/commandBumperTest.js`
```javascript
var expect = require('expect.js'),
  async = require('async'),
  commandBumper = require('../../lib/bumper'),
  Base = require('../../lib/bumper/base'),
  InMemory = require('../../lib/bumper/databases/inmemory');

describe('CommandBumper', function() {

  it('it should have the correct interface', function() {

    expect(commandBumper).to.be.an('object');
    expect(commandBumper.create).to.be.a('function');
    expect(commandBumper.Bumper).to.eql(Base);

  });

  describe('calling create', function() {

    describe('without options', function() {

      it('it should return with the in memory queue', function() {

        var lock = commandBumper.create();
        expect(lock).to.be.a('object');

      });

      describe('but with a callback', function() {

        it('it should callback with lock object', function(done) {

          commandBumper.create(function(err, lock) {
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
          commandBumper.create({ type: 'strangeDb' });
        }).to.throwError();

      });

      it('it should callback with an error', function(done) {

        expect(function() {
          commandBumper.create({ type: 'strangeDb' }, function(err) {
            expect(err).to.be.ok();
            done();
          });
        }).to.throwError();

      });

    });

    describe('with options of an own db implementation', function() {

      it('it should return with the an instance of that implementation', function() {

        var bumper = commandBumper.create({ type: InMemory });
        expect(bumper).to.be.a(InMemory);

      });

    });

    describe('with options containing a type property with the value of', function() {

      var types = ['inmemory', 'mongodb', 'tingodb', 'redis'];

      types.forEach(function(type) {

        describe('"' + type + '"', function() {

          var bumper;

          describe('without callback', function() {

            afterEach(function(done) {
              bumper.disconnect(done);
            });

            it('it should return with the correct lock', function() {

              bumper = commandBumper.create({ type: type });
              expect(bumper).to.be.a('object');
              expect(bumper).to.be.a(Base);
              expect(bumper.connect).to.be.a('function');
              expect(bumper.disconnect).to.be.a('function');
              expect(bumper.getNewId).to.be.a('function');
              expect(bumper.add).to.be.a('function');

            });

          });

          describe('with callback', function() {

            afterEach(function(done) {
              bumper.disconnect(done);
            });

            it('it should return with the correct lock', function(done) {

              commandBumper.create({ type: type }, function(err, resL) {
                expect(err).not.to.be.ok();
                bumper = resL;
                expect(bumper).to.be.a('object');
                done();
              });

            });

          });

          describe('calling connect', function () {

            afterEach(function(done) {
              bumper.disconnect(done);
            });

            describe('with a callback', function () {

              it('it should callback successfully', function(done) {

                bumper = commandBumper.create({ type: type });
                bumper.connect(function (err) {
                  expect(err).not.to.be.ok();
                  done();
                })

              });

            });

            describe('without a callback', function () {

              it('it should emit connect', function(done) {

                bumper = commandBumper.create({ type: type });
                bumper.once('connect', done);
                bumper.connect()

              });

            });

          });

          describe('having connected', function() {

            describe('calling disconnect', function() {

              beforeEach(function(done) {
                bumper = commandBumper.create({ type: type });
                bumper.connect(done);
              });

              it('it should callback successfully', function(done) {

                bumper.disconnect(function(err) {
                  expect(err).not.to.be.ok();
                  done();
                });

              });

              it('it should emit disconnect', function(done) {

                bumper.once('disconnect', done);
                bumper.disconnect();

              });

            });

            describe('using the lock', function() {

              before(function(done) {
                bumper = commandBumper.create({ type: type, ttl: 1100 });
                bumper.connect(done);
              });

              describe('calling getNewId', function() {

                it('it should callback with a new Id as string', function(done) {

                  bumper.getNewId(function(err, id) {
                    expect(err).not.to.be.ok();
                    expect(id).to.be.a('string');
                    done();
                  });

                });

              });

              describe('having no entries', function() {

                before(function(done) {
                  bumper.clear(done);
                });

                describe('calling add', function() {

                  it('it should callback correctly', function(done) {

                    bumper.add('key1', 100, function(err, added) {
                      expect(err).not.to.be.ok();
                      expect(added).to.eql(true);
                      done();
                    });

                  });

                });

                describe('calling add with the an already added key', function() {

                  it('it should callback correctly', function(done) {

                    bumper.add('key2', 100, function(err, added) {
                      expect(err).not.to.be.ok();
                      expect(added).to.eql(true);

                      bumper.add('key2', 100, function(err, added) {
                        expect(err).not.to.be.ok();
                        expect(added).to.eql(false);
                        done();
                      });
                    });

                  });

                  describe('but waiting the expiration', function() {

                    it('it should callback correctly', function(done) {

                      bumper.add('key3', 50, function(err, added) {
                        expect(err).not.to.be.ok();
                        expect(added).to.eql(true);

                        setTimeout(function () {
                          bumper.add('key3', 50, function(err, added) {
                            expect(err).not.to.be.ok();
                            expect(added).to.eql(true);
                            done();
                          });
                        }, 1001);

                      });

                    });

                  });

                });

                describe('without passing a ttl calling add with the an already added key', function() {

                  it('it should callback correctly', function(done) {

                    bumper.add('key22', function(err, added) {
                      expect(err).not.to.be.ok();
                      expect(added).to.eql(true);

                      bumper.add('key22', function(err, added) {
                        expect(err).not.to.be.ok();
                        expect(added).to.eql(false);
                        done();
                      });
                    });

                  });

                  describe('but waiting the expiration', function() {

                    it('it should callback correctly', function(done) {

                      bumper.add('key23', function(err, added) {
                        expect(err).not.to.be.ok();
                        expect(added).to.eql(true);

                        setTimeout(function () {
                          bumper.add('key23', function(err, added) {
                            expect(err).not.to.be.ok();
                            expect(added).to.eql(true);
                            done();
                          });
                        }, 1501);

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

## File: `test/unit/commandDispatcherTest.js`
```javascript
var expect = require('expect.js'),
  CommandDispatcher = require('../../lib/commandDispatcher');

describe('commandDispatcher', function () {

  describe('creating a new instance', function () {
    
    describe('without tree argument', function () {

      it('it should throw an error', function () {

        expect(function () {
          new CommandDispatcher();
        }).to.throwError(/tree/);

      });
      
    });

    describe('without definition argument', function () {

      it('it should throw an error', function () {

        expect(function () {
          new CommandDispatcher({ getCommandHandler: function () {} });
        }).to.throwError(/definition/);

      });

    });

    describe('with all correct arguments', function () {

      it('it should not throw an error', function () {

        expect(function () {
          new CommandDispatcher({ getCommandHandler: function () {} }, {});
        }).not.to.throwError();

      });
      
      describe('calling getTargetInformation', function () {

        describe('without command argument', function () {

          it('it should throw an error', function () {

            var cmdDisp = new CommandDispatcher({ getCommandHandler: function () {} }, {});
            expect(function () {
              cmdDisp.getTargetInformation();
            }).to.throwError(/command/);

          });

        });

        describe('with command argument', function () {

          it('it should not throw an error', function () {

            var cmdDisp = new CommandDispatcher({ getCommandHandler: function () {} }, {});
            expect(function () {
              cmdDisp.getTargetInformation({});
            }).not.to.throwError();

          });
          
          describe('passing a definition with all infos', function () {

            it('it should return the correct target infos', function () {

              var cmdDisp = new CommandDispatcher({ getCommandHandler: function () {} }, { name: 'cmdName', aggregateId: 'aggId', version: 'v', aggregate: 'agg', context: 'ctx' });
              var target = cmdDisp.getTargetInformation({ cmdName: 'cmdNameSpec', aggId: 'aggIdSpec', v: 3, agg: 'aggName', ctx: 'myCtx' });
              expect(target.name).to.eql('cmdNameSpec');
              expect(target.aggregateId).to.eql('aggIdSpec');
              expect(target.version).to.eql(3);
              expect(target.aggregate).to.eql('aggName');
              expect(target.context).to.eql('myCtx');

            });
            
          });

          describe('passing a definition with less infos', function () {

            it('it should return the correct target infos', function () {

              var cmdDisp = new CommandDispatcher({ getCommandHandler: function () {} }, { name: 'cmdName', aggregateId: 'aggId' });
              var target = cmdDisp.getTargetInformation({ cmdName: 'cmdNameSpec', aggId: 'aggIdSpec' });
              expect(target.name).to.eql('cmdNameSpec');
              expect(target.aggregateId).to.eql('aggIdSpec');
              expect(target.version).to.eql(0);

            });

          });

        });
        
      });
      
      describe('calling dispatch', function () {

        describe('with no matching commandHandler', function () {

          it('it should callback with an error', function (done) {

            var cmdDisp = new CommandDispatcher({ getCommandHandler: function () {
              return null;
            }, getCommandHandlerByOldTarget: function () { return null;}}, { name: 'cmdName', aggregateId: 'aggId' });
            cmdDisp.dispatch({ cmdName: 'cmdNameSpec', aggId: 'aggIdSpec' }, function (err) {
              expect(err).to.be.ok();
              expect(err.message).to.match(/no command/i);
              done();
            });
            
          });

        });
        
        describe('with matching commandHandler', function () {

          it('it should call his handle function', function (done) {

            var calledBack = false;
            var cmdDisp = new CommandDispatcher({ getCommandHandler: function () {
              return { handle: function (cmd, clb) {
                expect(cmd.cmdName).to.eql('cmdNameSpec');
                expect(clb).to.be.a('function');
                calledBack = true;
                clb(null);
              }};
            }}, { name: 'cmdName', aggregateId: 'aggId' });
            
            cmdDisp.dispatch({ cmdName: 'cmdNameSpec', aggId: 'aggIdSpec' }, function (err) {
              expect(err).not.to.be.ok();
              expect(calledBack).to.eql(true);
              done();
            });

          });
          
        });
        
      });

    });
    
  });

});
```

## File: `test/unit/defaultCommandHandlerTest.js`
```javascript
var expect = require('expect.js'),
  DefaultCommandHandler = require('../../lib/defaultCommandHandler'),
  DefinitionBase = require('../../lib/definitionBase'),
  ConcurrencyError = require('../../lib/errors/concurrencyError');

describe('defaultCommandHandler', function () {

  describe('creating a new instance', function () {

    var cmdHnd;

    beforeEach(function () {
      cmdHnd = new DefaultCommandHandler();
    });

    it('it should return a correct object', function () {

      expect(cmdHnd).to.be.a(DefinitionBase);
      expect(cmdHnd.id).to.be.a('string');
      expect(cmdHnd.definitions).to.be.an('object');
      expect(cmdHnd.definitions.command).to.be.an('object');
      expect(cmdHnd.definitions.event).to.be.an('object');
      expect(cmdHnd.defineCommand).to.be.a('function');
      expect(cmdHnd.defineEvent).to.be.a('function');
      expect(cmdHnd.defineOptions).to.be.a('function');

      expect(cmdHnd.useAggregate).to.be.a('function');
      expect(cmdHnd.useEventStore).to.be.a('function');
      expect(cmdHnd.useAggregateLock).to.be.a('function');
      expect(cmdHnd.queueCommand).to.be.a('function');
      expect(cmdHnd.getNextCommandInQueue).to.be.a('function');
      expect(cmdHnd.lockAggregate).to.be.a('function');
      expect(cmdHnd.loadAggregate).to.be.a('function');
      expect(cmdHnd.createSnapshot).to.be.a('function');
      expect(cmdHnd.isAggregateDestroyed).to.be.a('function');
      expect(cmdHnd.isRevisionWrong).to.be.a('function');
      expect(cmdHnd.validateCommand).to.be.a('function');
      expect(cmdHnd.checkPreLoadConditions).to.be.a('function');
      expect(cmdHnd.verifyAggregate).to.be.a('function');
      expect(cmdHnd.letHandleCommandByAggregate).to.be.a('function');
      expect(cmdHnd.checkAggregateLock).to.be.a('function');
      expect(cmdHnd.resolveAggregateLock).to.be.a('function');
      expect(cmdHnd.commit).to.be.a('function');
      expect(cmdHnd.workflow).to.be.a('function');
      expect(cmdHnd.handle).to.be.a('function');

    });

    describe('calling useAggregate', function () {

      it('it should work as expected', function () {

        var aggregate = { agg: 'regate' };
        cmdHnd.useAggregate(aggregate);
        expect(cmdHnd.aggregate).to.eql(aggregate);

      });

    });

    describe('calling useEventStore', function () {

      it('it should work as expected', function () {

        var eventstore = { event: 'store' };
        cmdHnd.useEventStore(eventstore);
        expect(cmdHnd.eventStore).to.eql(eventstore);

      });

    });

    describe('calling useEventStore', function () {

      it('it should work as expected', function () {

        var aggLock = { agg: 'lock' };
        cmdHnd.useAggregateLock(aggLock);
        expect(cmdHnd.aggregateLock).to.eql(aggLock);

      });

    });

    describe('calling queueCommand', function () {

      it('it should work as expected', function () {

        cmdHnd.defineCommand({
          aggregateId: 'aggId'
        });
        var cmd = { my: 'cmd', aggId: '123' };
        var clb = function () {};
        cmdHnd.queueCommand('123', cmd, clb);
        var cmd2 = { my: 'cmd2', aggId: '12345' };
        var clb2 = function () {};
        cmdHnd.queueCommand('12345', cmd2, clb2);
        var cmd3 = { my: 'cmd3', aggId: '123' };
        var clb3 = function () {};
        cmdHnd.queueCommand('123', cmd3, clb3);
        expect(cmdHnd.queue['123']).to.be.an('array');
        expect(cmdHnd.queue['123'].length).to.eql(2);
        expect(cmdHnd.queue['123'][0].command).to.eql(cmd);
        expect(cmdHnd.queue['123'][0].callback).to.eql(clb);
        expect(cmdHnd.queue['123'][1].command).to.eql(cmd3);
        expect(cmdHnd.queue['123'][1].callback).to.eql(clb3);
        expect(cmdHnd.queue['12345']).to.be.an('array');
        expect(cmdHnd.queue['12345'].length).to.eql(1);
        expect(cmdHnd.queue['12345'][0].command).to.eql(cmd2);
        expect(cmdHnd.queue['12345'][0].callback).to.eql(clb2);

      });

    });

    describe('calling getNextCommandInQueue', function () {

      it('it should work as expected', function () {

        cmdHnd.defineCommand({
          aggregateId: 'aggId'
        });
        var cmd = { my: 'cmd', aggId: '123' };
        var clb = function () {};
        cmdHnd.queueCommand('123', cmd, clb);
        var cmd2 = { my: 'cmd2', aggId: '12345' };
        var clb2 = function () {};
        cmdHnd.queueCommand('12345', cmd2, clb2);
        var cmd3 = { my: 'cmd3', aggId: '123' };
        var clb3 = function () {};
        cmdHnd.queueCommand('123', cmd3, clb3);

        var next = cmdHnd.getNextCommandInQueue('123');

        expect(cmdHnd.queue['123']).to.be.an('array');
        expect(cmdHnd.queue['123'].length).to.eql(2);
        expect(next.command).to.eql(cmd);
        expect(next.callback).to.eql(clb);
        expect(cmdHnd.queue['123'][0].command).to.eql(cmd);
        expect(cmdHnd.queue['123'][0].callback).to.eql(clb);
        expect(cmdHnd.queue['123'][1].command).to.eql(cmd3);
        expect(cmdHnd.queue['123'][1].callback).to.eql(clb3);
        expect(cmdHnd.queue['12345']).to.be.an('array');
        expect(cmdHnd.queue['12345'].length).to.eql(1);
        expect(cmdHnd.queue['12345'][0].command).to.eql(cmd2);
        expect(cmdHnd.queue['12345'][0].callback).to.eql(clb2);

      });

    });

    describe('calling removeCommandFromQueue', function () {

      it('it should work as expected', function () {

        cmdHnd.defineCommand({
          aggregateId: 'aggId'
        });
        var cmd = { my: 'cmd', aggId: '123' };
        var clb = function () {};
        cmdHnd.queueCommand('123', cmd, clb);
        var cmd2 = { my: 'cmd2', aggId: '12345' };
        var clb2 = function () {};
        cmdHnd.queueCommand('12345', cmd2, clb2);
        var cmd3 = { my: 'cmd3', aggId: '123' };
        var clb3 = function () {};
        cmdHnd.queueCommand('123', cmd3, clb3);

        cmdHnd.removeCommandFromQueue('123', cmd);

        expect(cmdHnd.queue['123']).to.be.an('array');
        expect(cmdHnd.queue['123'].length).to.eql(1);
        expect(cmdHnd.queue['123'][0].command).to.eql(cmd3);
        expect(cmdHnd.queue['123'][0].callback).to.eql(clb3);
        expect(cmdHnd.queue['12345']).to.be.an('array');
        expect(cmdHnd.queue['12345'].length).to.eql(1);
        expect(cmdHnd.queue['12345'][0].command).to.eql(cmd2);
        expect(cmdHnd.queue['12345'][0].callback).to.eql(clb2);

      });

    });

    describe('calling lockAggregate', function () {

      it('it should work as expected', function (done) {

        var calledBack = false;
        var aggLock = {
          reserve: function (workerId, aggregateId, callback) {
            expect(workerId).to.be.a('string');
            expect(workerId).to.eql(cmdHnd.id);
            expect(aggregateId).to.eql('myAggId');
            calledBack = true;
            callback(null);
          }
        };
        cmdHnd.useAggregateLock(aggLock);

        cmdHnd.lockAggregate('myAggId', function (err) {
          expect(err).not.to.be.ok();
          expect(calledBack).to.eql(true);
          done();
        });

      });

    });

    describe('calling loadAggregate', function () {

      it('it should work as expected', function (done) {

        var snap = { version: 2, data: 'my data' };
        var stream = { events: [ { payload: { name: 'my-name', the: 'event' } } ] };
        var calledBackSnap = false;
        var calledLoad = false;
        var eventStore = {
          getFromSnapshot: function (query, callback) {
            setTimeout(function () {
              expect(query.aggregateId).to.eql('myAggId');
              expect(query.aggregate).to.eql('aggName');
              expect(query.context).to.eql('ctx');
              calledBackSnap = true;
              callback(null, snap, stream);
            }, 6);
          }
        };
        cmdHnd.defineCommand({
          aggregate: 'agg',
          context: 'c'
        });

        var firstTime = true;
        cmdHnd.useEventStore(eventStore);
        cmdHnd.useAggregate({ name: 'aggName',
          context: { name: 'ctx' },
          loadingSnapshotTransformers: {},
          getLoadingEventTransformer: function () {},
          create: function (id) { return { id: id }; },
          loadFromHistory: function (aggregate, snapshot, events, time) {
            if (firstTime) {
              expect(aggregate.id).to.eql('myAggId');
              expect(snapshot.data).to.eql('my data');
              expect(events.length).to.eql(0);
              expect(time).to.be.greaterThan(5);

              firstTime = false;
            } else {
              expect(aggregate.id).to.eql('myAggId');
              expect(snapshot).not.to.be.ok();
              expect(events.length).to.eql(1);
              expect(events[0]).to.eql(stream.events[0].payload);
              expect(time).to.be.greaterThan(5);
            }

            calledLoad = true;
            return false;
          },
          shouldIgnoreSnapshot: function (snapshot) {
            expect(snapshot.data).to.eql('my data');
            return false;
          },
          getLoadInfo: function (cmd) {
            return [{ context: 'ctx', aggregate: 'aggName' }];
          }
        });

        cmdHnd.loadAggregate({}, 'myAggId', function (err) {
          expect(err).not.to.be.ok();
          expect(calledBackSnap).to.eql(true);
          expect(calledLoad).to.eql(true);
          done();
        });

      });

      describe('ignoring loading of snapshot', function () {

        it('it should work as expected', function (done) {

          var snap = { version: 2, data: 'my data' };
          var stream = { events: [ { payload: { name: 'my-event', the: 'event' }, streamRevision: 1, id: 'id2' } ] };
          var streamAll = { events: [ { payload: { name: 'my-event',  the: 'eventOld' }, streamRevision: 0, id: 'id1' }, { payload: { name: 'my-event',  the: 'event' }, streamRevision: 1, id: 'id2' } ] };
          var calledBackSnap = false;
          var calledLoad = false;
          var eventStore = {
            getFromSnapshot: function (query, callback) {
              setTimeout(function () {
                expect(query.aggregateId).to.eql('myAggId');
                expect(query.aggregate).to.eql('aggName');
                expect(query.context).to.eql('ctx');
                calledBackSnap = true;
                callback(null, snap, stream);
              }, 6);
            },
            getEventStream: function (query, callback) {
              setTimeout(function () {
                expect(query.aggregateId).to.eql('myAggId');
                expect(query.aggregate).to.eql('aggName');
                expect(query.context).to.eql('ctx');
                calledBackSnap = true;
                callback(null, streamAll);
              }, 10);
            }
          };
          cmdHnd.defineCommand({
            aggregate: 'agg',
            context: 'c'
          });

          var firstTime = true;
          cmdHnd.useEventStore(eventStore);
          cmdHnd.useAggregate({ name: 'aggName',
            context: { name: 'ctx' },
            loadingSnapshotTransformers: {},
            getLoadingEventTransformer: function () {},
            create: function (id) { return { id: id }; },
            loadFromHistory: function (aggregate, snapshot, events, time) {
            if (firstTime) {
              expect(aggregate.id).to.eql('myAggId');
              expect(snapshot).not.to.be.ok();
              expect(events.length).to.eql(2);
              expect(time).to.be.greaterThan(5);

              firstTime = false;
            } else {
              expect(aggregate.id).to.eql('myAggId');
              expect(snapshot).not.to.be.ok();
              expect(events.length).to.eql(2);
              expect(events[1]).to.eql(stream.events[0].payload);
              expect(time).to.be.greaterThan(5);
            }

            calledLoad = true;
            return false;
          },
          getLoadInfo: function (cmd) {
            return [{ context: 'ctx', aggregate: 'aggName' }];
          },
            shouldIgnoreSnapshot: function (snapshot) {
              expect(snapshot.data).to.eql('my data');
              return true;
            }
          });

          cmdHnd.loadAggregate({}, 'myAggId', function (err) {
            expect(err).not.to.be.ok();
            expect(calledBackSnap).to.eql(true);
            expect(calledLoad).to.eql(true);
            done();
          });

        });

      });

    });

    describe('calling createSnapshot', function () {

      it('it should work as expected', function (done) {

        var aggr = {
          id: 'myAggId',
          toJSON: function () {
            return { a: 'b' };
          }
        };
        var stream = { lastRevision: 3, events: [ { payload: { the: 'event' } } ] };
        var calledBackSnap = false;
        var eventStore = {
          createSnapshot: function (query, callback) {
            expect(query.aggregateId).to.eql('myAggId');
            expect(query.aggregate).to.eql('aggName');
            expect(query.context).to.eql('ctx');
            expect(query.data.a).to.eql('b');
            expect(query.revision).to.eql(3);
            expect(query.version).to.eql(2);
            calledBackSnap = true;
            callback(null);
          }
        };
        cmdHnd.defineCommand({
          aggregate: 'agg',
          context: 'c'
        });
        cmdHnd.useEventStore(eventStore);
        cmdHnd.useAggregate({ name: 'aggName',
          context: { name: 'ctx' },
          version: 2,
          committingSnapshotTransformers: {}
        });

        cmdHnd.createSnapshot(aggr, stream, function (err) {
          expect(err).not.to.be.ok();
          expect(calledBackSnap).to.eql(true);
          done();
        });

      });

    });

    describe('calling isAggregateDestroyed', function () {

      describe('if false', function () {

        it('it should work as expected', function () {

          var aggr = {
            isDestroyed: function () {
              return false;
            }
          };

          var res = cmdHnd.isAggregateDestroyed(aggr, {});
          expect(res).to.eql(null);

        });

      });

      describe('if true', function () {

        it('it should work as expected', function () {

          var aggr = {
            id: '234',
            getRevision: function () {
              return 4;
            },
            isDestroyed: function () {
              return true;
            }
          };

          var res = cmdHnd.isAggregateDestroyed(aggr, {});
          expect(res.name).to.eql('AggregateDestroyedError');
          expect(res.more.aggregateId).to.eql('234');
          expect(res.more.aggregateRevision).to.eql(4);

        });

      });

    });

    describe('calling isRevisionWrong', function () {

      describe('without having defined a revision', function () {

        it('it should work as expected', function () {

          var aggr = {};
          var cmd = {};
          var res = cmdHnd.isRevisionWrong(aggr, cmd);
          expect(res).to.eql(null);

        });

      });

      describe('with a command revision is less then the aggregate revision', function () {

        it('it should work as expected', function () {

          var aggr = { id: '332', getRevision: function () { return 3; } };
          var cmd = { r: 2 };

          cmdHnd.defineCommand({
            revision: 'r'
          });

          var res = cmdHnd.isRevisionWrong(aggr, cmd);
          expect(res.name).to.eql('AggregateConcurrencyError');
          expect(res.more.aggregateId).to.eql('332');
          expect(res.more.aggregateRevision).to.eql(3);
          expect(res.more.commandRevision).to.eql(2);

        });

      });

      describe('with a command revision is greater then the aggregate revision', function () {

        it('it should work as expected', function () {

          var aggr = { id: '332', getRevision: function () { return 2; } };
          var cmd = { r: 3 };

          cmdHnd.defineCommand({
            revision: 'r'
          });

          var res = cmdHnd.isRevisionWrong(aggr, cmd);
          expect(res.name).to.eql('AggregateConcurrencyError');
          expect(res.more.aggregateId).to.eql('332');
          expect(res.more.aggregateRevision).to.eql(2);
          expect(res.more.commandRevision).to.eql(3);

        });

      });

      describe('with a command revision matching the aggregate revision', function () {

        it('it should work as expected', function () {

          var aggr = { id: '332', getRevision: function () { return 3; } };
          var cmd = { r: 3 };

          cmdHnd.defineCommand({
            revision: 'r'
          });

          var res = cmdHnd.isRevisionWrong(aggr, cmd);
          expect(res).to.eql(null);

        });

      });

    });

    describe('calling validateCommand', function () {

      it('it should work as expected', function (done) {

        var cmd = { my: 'cmd' };
        var aggr = {
          validateCommand: function (c, clb) {
            expect(c).to.eql(cmd);
            clb();
          }
        };
        cmdHnd.useAggregate(aggr);
        cmdHnd.validateCommand(cmd, function (error, result){ done() });

      });

    });

    describe('calling verifyAggregate', function () {

      it('it should work as expected', function () {

        var cmd = { my: 'cmd' };
        var aggr = { my: 'aggr' };

        cmdHnd.useAggregate({});

        cmdHnd.isAggregateDestroyed = function (a) {
          expect(a).to.eql(aggr);
          return null;
        };

        cmdHnd.isRevisionWrong = function (a, c) {
          expect(a).to.eql(aggr);
          expect(c).to.eql(cmd);
          return null;
        };

        cmdHnd.verifyAggregate(aggr, cmd);

      });

    });

    describe('calling letHandleCommandByAggregate', function () {

      it('it should work as expected', function (done) {

        var cmd = { my: 'cmd' };
        var aggr = { my: 'aggr' };
        var called = false;

        cmdHnd.useAggregate({
          handle: function (a, c, clb) {
            expect(a).to.eql(aggr);
            expect(c).to.eql(cmd);
            called = true;
            clb(null);
          }
        });
        cmdHnd.letHandleCommandByAggregate(aggr, cmd, function (err) {
          expect(err).not.to.be.ok();
          expect(called).to.eql(true);
          done();
        });

      });

    });

    describe('calling checkAggregateLock', function () {

      describe('having an error', function () {

        it('it should work as expected', function (done) {

          var called = false;

          cmdHnd.useAggregateLock({
            getAll: function (aggId, clb) {
              expect(aggId).to.eql('1234');
              called = true;
              clb('err');
            }
          });
          cmdHnd.checkAggregateLock('1234', function (err) {
            expect(err).to.eql('err');
            expect(called).to.eql(true);
            done();
          });

        });

      });

      describe('having more workers as expected', function () {

        it('it should work as expected', function (done) {

          var called = false;

          cmdHnd.useAggregateLock({
            getAll: function (aggId, clb) {
              expect(aggId).to.eql('1234');
              called = true;
              clb(null, [cmdHnd.id, '1111']);
            }
          });
          cmdHnd.checkAggregateLock('1234', function (err) {
            expect(err).to.be.a(ConcurrencyError);
            expect(called).to.eql(true);
            done();
          });

        });

      });

      describe('having exactly my worker', function () {

        it('it should work as expected', function (done) {

          var called = false;

          cmdHnd.useAggregateLock({
            getAll: function (aggId, clb) {
              expect(aggId).to.eql('1234');
              called = true;
              clb(null, [cmdHnd.id]);
            }
          });
          cmdHnd.checkAggregateLock('1234', function (err) {
            expect(err).not.to.be.ok();
            expect(called).to.eql(true);
            done();
          });

        });

      });

    });

    describe('calling resolveAggregateLock', function () {

      it('it should work as expected', function (done) {

        var called = false;

        cmdHnd.useAggregateLock({
          resolve: function (aggId, clb) {
            expect(aggId).to.eql('1234');
            called = true;
            clb(null);
          }
        });
        cmdHnd.resolveAggregateLock('1234', function (err) {
          expect(err).not.to.be.ok();
          expect(called).to.eql(true);
          done();
        });

      });

    });

    describe('calling commit', function () {

      it('it should work as expected', function (done) {

        var called = false;
        var evts = [{ payload: { name: 'my-event' }, my: 'first', context: 'c', aggregate: 'a', aggregateId: 'aId' }, { payload: { name: 'my-event' }, my: 'second', context: 'c', aggregate: 'a', aggregateId: 'aId' }];
        var agg = { getUncommittedEvents: function () { return evts; } };
        var stream = {
          eventsToDispatch: [],
          addEvents: function (u) {
            this.eventsToDispatch = u;
          },
          addEvent: function (u) {
            this.eventsToDispatch.push(u);
          },
          commit: function (clb) {
            called = true;
            clb(null, this);
          },
          context: 'c',
          aggregate: 'a',
          aggregateId: 'aId'
        };

        cmdHnd.useAggregate({ name: 'aggName', context: { name: 'ctxName' }, getLoadingEventTransformer: function () {} });

        cmdHnd.defineEvent({
          context: 'context',
          aggregate: 'aggregate',
          aggregateId: 'aggregateId'
        });

        cmdHnd.commit(agg, [stream], function (err, uncommitedEvts) {
          expect(err).not.to.be.ok();
          expect(uncommitedEvts).to.eql(evts);
          expect(called).to.eql(true);
          done();
        });

      });

    });

    describe('calling workflow', function () {

      it('it should work as expected', function (done) {

        var cmd = { my: 'cmd', aggId: '8931' };

        cmdHnd.defineCommand({
          aggregateId: 'aggId'
        });

        cmdHnd.useAggregate({ name: 'aggName', context: { name: 'ctxName' } });

        var step = 1;

        cmdHnd.validateCommand = function (c, clb) {
          expect(c).to.eql(cmd);
          expect(step).to.eql(1);
          step++;
          clb();
        };

        cmdHnd.checkPreLoadConditions = function (a, clb) {
          expect(step).to.eql(2);
          step++;
          clb(null);
        };

        cmdHnd.lockAggregate = function (a, clb) {
          expect(a).to.eql('8931');
          expect(step).to.eql(3);
          step++;
          clb(null);
        };

        cmdHnd.loadAggregate = function (cmd, a, clb) {
          expect(a).to.eql('8931');
          expect(step).to.eql(4);
          step++;
          clb(null, { my: 'aggregate', toJSON: function() { return 'aggregateAsJSON'; }, getRevision: function () { return 1; } }, ['stream']);
        };

        cmdHnd.verifyAggregate = function (a, c) {
          expect(a.my).to.eql('aggregate');
          expect(c).to.eql(cmd);
          expect(step).to.eql(5);
          step++;
        };

        cmdHnd.letHandleCommandByAggregate = function (a, c, clb) {
          expect(a.my).to.eql('aggregate');
          expect(c).to.eql(cmd);
          expect(step).to.eql(6);
          step++;
          clb(null, a, 'stream');
        };

        cmdHnd.checkAggregateLock = function (a, clb) {
          expect(a).to.eql('8931');
          expect(step).to.eql(7);
          step++;
          clb(null, { my: 'aggregate', toJSON: function() { return 'aggregateAsJSON'; }, getRevision: function () { return 1; } }, 'stream');
        };

        cmdHnd.commit = function (a, s, clb) {
          expect(a.my).to.eql('aggregate');
          expect(s).to.eql(['stream']);
          expect(step).to.eql(8);
          step++;
          clb(null, [{ evt1: 'one' }, { evt2: 'two' }]);
        };

        cmdHnd.resolveAggregateLock = function (a, clb) {
          expect(a).to.eql('8931');
          expect(step).to.eql(9);
          step++;
          clb(null, [{ evt1: 'one' }, { evt2: 'two' }]);
        };


        cmdHnd.workflow('8931', cmd, function (err, evts, aggData, meta) {
          expect(err).not.to.be.ok();
          expect(step).to.eql(10);
          expect(evts).to.be.an('array');
          expect(evts.length).to.eql(2);
          expect(evts[0].evt1).to.eql('one');
          expect(evts[1].evt2).to.eql('two');
          expect(aggData).to.eql('aggregateAsJSON');
          expect(meta.aggregateId).to.eql('8931');
          expect(meta.aggregate).to.eql('aggName');
          expect(meta.context).to.eql('ctxName');
          done();
        });

      });

    });

    describe('calling handle', function () {

      describe('with a command without aggregate id', function () {

        it('it should work as expected', function (done) {

          var cmd = { my: 'cmd' };
          var queueCalled = false;
          var nextCalled = false;
          var removeCalled = false;
          var workflowCalled = false;
          var aggregateId;

          cmdHnd.defineCommand({
            aggregateId: 'aggId'
          });

          cmdHnd.useEventStore({
            getNewId: function (clb) {
              clb(null, 'newId');
            }
          });

          var queued;

          cmdHnd.queueCommand = function (aggId, c, clb) {
            expect(aggId).to.eql('newId');
            expect(c).to.eql(cmd);
            queueCalled = true;
            queued = { command: c, callback: clb };
          };

          var removed = false;
          cmdHnd.getNextCommandInQueue = function (aggId) {
            expect(aggId).to.eql('newId');
            if (removed) {
              return null;
            }
            nextCalled = true;
            return queued;
          };

          cmdHnd.removeCommandFromQueue = function (aggId, c) {
            expect(aggId).to.eql('newId');
            expect(c).to.eql(cmd);
            removed = true;
            removeCalled = true;
          };

          cmdHnd.workflow = function (aggId, c, clb) {
            expect(c).to.eql(cmd);
            workflowCalled = true;
            clb(null, 'evts', 'aggData', 'meta');
          };

          cmdHnd.handle(cmd, function (err, evts, aggData, meta) {
            expect(err).not.to.be.ok();
            expect(evts).to.eql('evts');
            expect(aggData).to.eql('aggData');
            expect(meta).to.eql('meta');
            expect(cmd.aggId).not.to.be.ok();
            expect(queueCalled).to.eql(true);
            expect(nextCalled).to.eql(true);
            expect(removeCalled).to.eql(true);
            expect(workflowCalled).to.eql(true);
            done();
          });

        });

        describe('having a commandHandler that has defined a getNewAggregateId function', function () {

          it('it should work as expected', function (done) {

            var cmd = { my: 'cmd' };
            var queueCalled = false;
            var nextCalled = false;
            var removeCalled = false;
            var workflowCalled = false;
            var aggregateId;

            cmdHnd.defineCommand({
              aggregateId: 'aggId'
            });

            cmdHnd.useEventStore({
              getNewId: function (clb) {
                clb(null, 'newIdFromStore');
              }
            });

            cmdHnd.aggregateIdGenerator(function (clb) {
              clb(null, 'newIdFromCmdHandler');
            });

            cmdHnd.useAggregate({
              //getNewAggregateId: function (clb) {
              //  clb(null, 'newIdFromAggregate');
              //}
            });

            var queued;

            cmdHnd.queueCommand = function (aggId, c, clb) {
              expect(aggId).to.eql('newIdFromCmdHandler');
              expect(c).to.eql(cmd);
              queueCalled = true;
              queued = { command: c, callback: clb };
            };

            var removed = false;
            cmdHnd.getNextCommandInQueue = function (aggId) {
              expect(aggId).to.eql('newIdFromCmdHandler');
              if (removed) {
                return null;
              }
              nextCalled = true;
              return queued;
            };

            cmdHnd.removeCommandFromQueue = function (aggId, c) {
              expect(aggId).to.eql('newIdFromCmdHandler');
              expect(c).to.eql(cmd);
              removed = true;
              removeCalled = true;
            };

            cmdHnd.workflow = function (aggId, c, clb) {
              expect(c).to.eql(cmd);
              workflowCalled = true;
              clb(null, 'evts', 'aggData', 'meta');
            };

            cmdHnd.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).not.to.be.ok();
              expect(evts).to.eql('evts');
              expect(aggData).to.eql('aggData');
              expect(meta).to.eql('meta');
              expect(cmd.aggId).not.to.be.ok();
              expect(queueCalled).to.eql(true);
              expect(nextCalled).to.eql(true);
              expect(removeCalled).to.eql(true);
              expect(workflowCalled).to.eql(true);
              done();
            });

          });

        });

        describe('having an aggregate that has defined a getNewAggregateId function', function () {

          it('it should work as expected', function (done) {

            var cmd = { my: 'cmd' };
            var queueCalled = false;
            var nextCalled = false;
            var removeCalled = false;
            var workflowCalled = false;
            var aggregateId;

            cmdHnd.defineCommand({
              aggregateId: 'aggId'
            });

            cmdHnd.useEventStore({
              getNewId: function (clb) {
                clb(null, 'newIdFromStore');
              }
            });

            cmdHnd.aggregateIdGenerator(function (clb) {
              clb(null, 'newIdFromCmdHandler');
            });

            cmdHnd.useAggregate({
              getNewAggregateId: function (clb) {
                clb(null, 'newIdFromAggregate');
              }
            });

            var queued;

            cmdHnd.queueCommand = function (aggId, c, clb) {
              expect(aggId).to.eql('newIdFromAggregate');
              expect(c).to.eql(cmd);
              queueCalled = true;
              queued = { command: c, callback: clb };
            };

            var removed = false;
            cmdHnd.getNextCommandInQueue = function (aggId) {
              expect(aggId).to.eql('newIdFromAggregate');
              if (removed) {
                return null;
              }
              nextCalled = true;
              return queued;
            };

            cmdHnd.removeCommandFromQueue = function (aggId, c) {
              expect(aggId).to.eql('newIdFromAggregate');
              expect(c).to.eql(cmd);
              removed = true;
              removeCalled = true;
            };

            cmdHnd.workflow = function (aggId, c, clb) {
              expect(c).to.eql(cmd);
              workflowCalled = true;
              clb(null, 'evts', 'aggData', 'meta');
            };

            cmdHnd.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).not.to.be.ok();
              expect(evts).to.eql('evts');
              expect(aggData).to.eql('aggData');
              expect(meta).to.eql('meta');
              expect(cmd.aggId).not.to.be.ok();
              expect(queueCalled).to.eql(true);
              expect(nextCalled).to.eql(true);
              expect(removeCalled).to.eql(true);
              expect(workflowCalled).to.eql(true);
              done();
            });

          });

        });

        describe('having an aggregate that has defined a getNewAggregateId command aware function', function () {

          it('it should work as expected', function (done) {

            var cmd = { my: 'cmd', id: 'cmdId' };
            var queueCalled = false;
            var nextCalled = false;
            var removeCalled = false;
            var workflowCalled = false;
            var aggregateId;

            cmdHnd.defineCommand({
              aggregateId: 'aggId'
            });

            cmdHnd.useEventStore({
              getNewId: function (clb) {
                clb(null, 'newIdFromStore');
              }
            });

            cmdHnd.aggregateIdGenerator(function (cmd, clb) {
              clb(null, cmd.id + 'newIdFromCmdHandler');
            });

            cmdHnd.useAggregate({
              getNewAggregateId: function (cmd, clb) {
                clb(null, cmd.id + 'newIdFromAggregate');
              }
            });

            var queued;

            cmdHnd.queueCommand = function (aggId, c, clb) {
              expect(aggId).to.eql('cmdIdnewIdFromAggregate');
              expect(c).to.eql(cmd);
              queueCalled = true;
              queued = { command: c, callback: clb };
            };

            var removed = false;
            cmdHnd.getNextCommandInQueue = function (aggId) {
              expect(aggId).to.eql('cmdIdnewIdFromAggregate');
              if (removed) {
                return null;
              }
              nextCalled = true;
              return queued;
            };

            cmdHnd.removeCommandFromQueue = function (aggId, c) {
              expect(aggId).to.eql('cmdIdnewIdFromAggregate');
              expect(c).to.eql(cmd);
              removed = true;
              removeCalled = true;
            };

            cmdHnd.workflow = function (aggId, c, clb) {
              expect(c).to.eql(cmd);
              workflowCalled = true;
              clb(null, 'evts', 'aggData', 'meta');
            };

            cmdHnd.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).not.to.be.ok();
              expect(evts).to.eql('evts');
              expect(aggData).to.eql('aggData');
              expect(meta).to.eql('meta');
              expect(cmd.aggId).not.to.be.ok();
              expect(queueCalled).to.eql(true);
              expect(nextCalled).to.eql(true);
              expect(removeCalled).to.eql(true);
              expect(workflowCalled).to.eql(true);
              done();
            });

          });

        });

      });

      describe('with a command with aggregate id', function () {

        it('it should work as expected', function (done) {

          var cmd = { my: 'cmd', aggId: '1421' };
          var queueCalled = false;
          var nextCalled = false;
          var removeCalled = false;
          var workflowCalled = false;

          cmdHnd.defineCommand({
            aggregateId: 'aggId'
          });

          cmdHnd.useEventStore({
            getNewId: function (clb) {
              clb(null, 'newId');
            }
          });

          var queued;

          cmdHnd.queueCommand = function (aggId, c, clb) {
            expect(aggId).to.eql('1421');
            expect(c).to.eql(cmd);
            queueCalled = true;
            queued = { command: c, callback: clb };
          };

          var removed = false;
          cmdHnd.getNextCommandInQueue = function (aggId) {
            expect(aggId).to.eql('1421');
            if (removed) {
              return null;
            }
            nextCalled = true;
            return queued;
          };

          cmdHnd.removeCommandFromQueue = function (aggId, c) {
            expect(aggId).to.eql('1421');
            expect(c).to.eql(cmd);
            removed = true;
            removeCalled = true;
          };

          cmdHnd.workflow = function (aggId, c, clb) {
            expect(aggId).to.eql('1421');
            expect(c).to.eql(cmd);
            workflowCalled = true;
            clb(null, 'evts', 'aggData', 'meta');
          };

          cmdHnd.handle(cmd, function (err, evts, aggData, meta) {
            expect(err).not.to.be.ok();
            expect(evts).to.eql('evts');
            expect(aggData).to.eql('aggData');
            expect(meta).to.eql('meta');
            expect(cmd.aggId).to.eql('1421');
            expect(queueCalled).to.eql(true);
            expect(nextCalled).to.eql(true);
            expect(removeCalled).to.eql(true);
            expect(workflowCalled).to.eql(true);
            done();
          });

        });

      });

      describe('with a command with aggregate id, an aggregate and a context', function () {

        it('it should work as expected', function (done) {

          var cmd = { my: 'cmd', aggId: '1421', aggr: 'a', ctx: 'c' };
          var queueCalled = false;
          var nextCalled = false;
          var removeCalled = false;
          var workflowCalled = false;

          cmdHnd.defineCommand({
            aggregateId: 'aggId',
            aggregate: 'aggr',
            context: 'ctx'
          });

          cmdHnd.useEventStore({
            getNewId: function (clb) {
              clb(null, 'newId');
            }
          });

          var queued;

          cmdHnd.queueCommand = function (aggId, c, clb) {
            expect(aggId).to.eql('ca1421');
            expect(c).to.eql(cmd);
            queueCalled = true;
            queued = { command: c, callback: clb };
          };

          var removed = false;
          cmdHnd.getNextCommandInQueue = function (aggId) {
            expect(aggId).to.eql('ca1421');
            if (removed) {
              return null;
            }
            nextCalled = true;
            return queued;
          };

          cmdHnd.removeCommandFromQueue = function (aggId, c) {
            expect(aggId).to.eql('ca1421');
            expect(c).to.eql(cmd);
            removed = true;
            removeCalled = true;
          };

          cmdHnd.workflow = function (aggId, c, clb) {
            expect(aggId).to.eql('1421');
            expect(c).to.eql(cmd);
            workflowCalled = true;
            clb(null, 'evts', 'aggData', 'meta');
          };

          cmdHnd.handle(cmd, function (err, evts, aggData, meta) {
            expect(err).not.to.be.ok();
            expect(evts).to.eql('evts');
            expect(aggData).to.eql('aggData');
            expect(meta).to.eql('meta');
            expect(cmd.aggId).to.eql('1421');
            expect(queueCalled).to.eql(true);
            expect(nextCalled).to.eql(true);
            expect(removeCalled).to.eql(true);
            expect(workflowCalled).to.eql(true);
            done();
          });

        });

      });

    });

  });

});
```

## File: `test/unit/domainTest.js`
```javascript
var expect = require('expect.js'),
  api = require('../../index'),
  ValidationError = require('../../lib/errors/validationError'),
  BusinessRuleError = require('../../lib/errors/businessRuleError'),
  AggregateDestroyedError = require('../../lib/errors/aggregateDestroyedError'),
  AggregateConcurrencyError = require('../../lib/errors/aggregateConcurrencyError'),
  ConcurrencyError = require('../../lib/errors/concurrencyError'),
  _ = require('lodash');

describe('domain', function () {

  it('it should be a function', function () {

    expect(api).to.be.a('function');

  });

  it('it should expose all domain errors', function () {

    expect(api.errors.ValidationError).to.eql(ValidationError);
    expect(api.errors.BusinessRuleError).to.eql(BusinessRuleError);
    expect(api.errors.AggregateDestroyedError).to.eql(AggregateDestroyedError);
    expect(api.errors.AggregateConcurrencyError).to.eql(AggregateConcurrencyError);
    expect(api.errors.ConcurrencyError).to.eql(ConcurrencyError);

  });

  it('it should have the correct api', function () {

    expect(api.defineContext).to.be.a('function');
    expect(api.defineAggregate).to.be.a('function');
    expect(api.defineCommand).to.be.a('function');
    expect(api.defineEvent).to.be.a('function');
    expect(api.defineBusinessRule).to.be.a('function');
    expect(api.definePreCondition).to.be.a('function');
    expect(api.definePreLoadCondition).to.be.a('function');
    expect(api.defineCommandHandler).to.be.a('function');

  });

  describe('calling that function', function () {

    describe('without options', function () {

      it('it should throw an error', function () {

        expect(api).to.throwError('/domainPath/');

      });

    });

    describe('with all mandatory options', function () {

      it('it should return as expected', function () {

        var domain = api({ domainPath: __dirname + '/../integration/fixture/set1' });
        expect(domain).to.be.a('object');
        expect(domain.on).to.be.a('function');
        expect(domain.eventStore).to.be.an('object');
        expect(domain.eventStore.on).to.be.a('function');
        expect(domain.aggregateLock).to.be.an('object');
        expect(domain.aggregateLock.on).to.be.a('function');
        expect(domain.defineCommand).to.be.a('function');
        expect(domain.defineEvent).to.be.a('function');
        expect(domain.idGenerator).to.be.a('function');
        expect(domain.aggregateIdGenerator).to.be.a('function');
        expect(domain.onEvent).to.be.a('function');
        expect(domain.init).to.be.a('function');
        expect(domain.handle).to.be.a('function');

        expect(domain.options.retryOnConcurrencyTimeout).to.eql(800);
        expect(domain.options.commandRejectedEventName).to.eql('commandRejected');
        expect(domain.options.snapshotThreshold).to.eql(100);

      });

    });

    describe('with custom "structureLoader" method', function () {

      describe('creating an object of the wrong interface', function () {

        it('it should throw an error', function () {

          expect(function () {
            api({
              domainPath: __dirname + '/../integration/fixture/set1',
              structureLoader: {
              },
            })
          }).to.throwError('/structureLoader/');

        });
      });

      describe('creating an object of the right interface', function () {

        it('it should return as expected', function () {

          var domain = api({
            domainPath: __dirname + '/../integration/fixture/set1',
            structureLoader: function() {
            }});
          expect(domain).to.be.a('object');
          expect(domain.on).to.be.a('function');
          expect(domain.eventStore).to.be.an('object');
          expect(domain.structureLoader).to.be.an('function');
          expect(domain.eventStore.on).to.be.a('function');
          expect(domain.aggregateLock).to.be.an('object');
          expect(domain.aggregateLock.on).to.be.a('function');
          expect(domain.defineCommand).to.be.a('function');
          expect(domain.defineEvent).to.be.a('function');
          expect(domain.idGenerator).to.be.a('function');
          expect(domain.aggregateIdGenerator).to.be.a('function');
          expect(domain.onEvent).to.be.a('function');
          expect(domain.init).to.be.a('function');
          expect(domain.handle).to.be.a('function');

          expect(domain.options.retryOnConcurrencyTimeout).to.eql(800);
          expect(domain.options.commandRejectedEventName).to.eql('commandRejected');
          expect(domain.options.snapshotThreshold).to.eql(100);

        });
      });
    });


    describe('with "eventStore" factory method', function () {

      describe('creating an object of the wrong interface', function () {

        it('it should throw an error', function () {

          expect(function () {
            api({
              domainPath: __dirname + '/../integration/fixture/set1',
              eventStore: function () {
                return {
                  init: function (callback) { },
                  getNewId: function (callback) { },
                  on: 4,  // not a function
                  createSnapshot: function (obj, callback) { },
                  getFromSnapshot: function (query, revMax, callback) { },
                  setEventToDispatched: function (evt, callback) { }
                }
              }
            })
          }).to.throwError('/eventStore/');

        });
      });

      describe('creating an object of the right interface', function () {

        it('it should return as expected', function () {

          var domain = api({
            domainPath: __dirname + '/../integration/fixture/set1',
            eventStore: function () {
              return {
                init: function (callback) {

                },
                getNewId: function (callback) {

                },
                on: function (evtName, callback) {

                },
                createSnapshot: function (obj, callback) {

                },
                getFromSnapshot: function (query, revMax, callback) {

                },
                setEventToDispatched: function (evt, callback) {

                }
              }
            }});
          expect(domain).to.be.a('object');
          expect(domain.on).to.be.a('function');
          expect(domain.eventStore).to.be.an('object');
          expect(domain.eventStore.on).to.be.a('function');
          expect(domain.aggregateLock).to.be.an('object');
          expect(domain.aggregateLock.on).to.be.a('function');
          expect(domain.defineCommand).to.be.a('function');
          expect(domain.defineEvent).to.be.a('function');
          expect(domain.idGenerator).to.be.a('function');
          expect(domain.aggregateIdGenerator).to.be.a('function');
          expect(domain.onEvent).to.be.a('function');
          expect(domain.init).to.be.a('function');
          expect(domain.handle).to.be.a('function');

          expect(domain.options.retryOnConcurrencyTimeout).to.eql(800);
          expect(domain.options.commandRejectedEventName).to.eql('commandRejected');
          expect(domain.options.snapshotThreshold).to.eql(100);

        });
      });

    });

    describe('with "aggregateLock" factory method', function () {

      describe('creating an object of the wrong interface', function () {

        it('it should throw an error', function () {

          expect(function () {
            api({
              domainPath: __dirname + '/../integration/fixture/set1',
              aggregateLock: function () {
                return {
                  connect: function (callback) { },
                  disconnect: function (callback) { },
                  getNewId: function (callback) { },
                  reserve: 4,  // not a function
                  getAll: function (aggregateId, callback) { },
                  resolve: function (aggregateId, callback) { }
                }
              }
            })
          }).to.throwError('/aggregateLock/');

        });

      });

      describe('creating an object of the right interface', function () {

        it('it should return as expected', function () {

          var domain = api({
            domainPath: __dirname + '/../integration/fixture/set1',
            aggregateLock: function () {
              return {
                connect: function (callback) { },
                disconnect: function (callback) { },
                getNewId: function (callback) { },
                reserve: function (workerId, aggregateId, callback) { },
                getAll: function (aggregateId, callback) { },
                resolve: function (aggregateId, callback) { },
                on: function (evtName, callback) { }
              }
            }
          });

          expect(domain).to.be.a('object');
          expect(domain.on).to.be.a('function');
          expect(domain.eventStore).to.be.an('object');
          expect(domain.eventStore.on).to.be.a('function');
          expect(domain.aggregateLock).to.be.an('object');
          expect(domain.aggregateLock.on).to.be.a('function');
          expect(domain.defineCommand).to.be.a('function');
          expect(domain.defineEvent).to.be.a('function');
          expect(domain.idGenerator).to.be.a('function');
          expect(domain.aggregateIdGenerator).to.be.a('function');
          expect(domain.onEvent).to.be.a('function');
          expect(domain.init).to.be.a('function');
          expect(domain.handle).to.be.a('function');

          expect(domain.options.retryOnConcurrencyTimeout).to.eql(800);
          expect(domain.options.commandRejectedEventName).to.eql('commandRejected');
          expect(domain.options.snapshotThreshold).to.eql(100);
        });

      });

    });

    describe('defining an aggregagte id generator function', function() {

      var domain;

      beforeEach(function () {
        domain = api({ domainPath: __dirname + '/../integration/fixture/set1' });
        domain.getNewAggregateId = null;
      });

      describe('in a synchronous way', function() {

        it('it should be transformed internally to an asynchronous way', function(done) {

          domain.aggregateIdGenerator(function () {
            var id = require('uuid').v4().toString();
            return id;
          });

          domain.getNewAggregateId(function (err, id) {
            expect(id).to.be.a('string');
            done();
          });

        });

      });

      describe('in an synchronous way', function() {

        it('it should be taken as it is', function(done) {

          domain.aggregateIdGenerator(function (callback) {
            setTimeout(function () {
              var id = require('uuid').v4().toString();
              callback(null, id);
            }, 10);
          });

          domain.getNewAggregateId(function (err, id) {
            expect(id).to.be.a('string');
            done();
          });

        });

      });

    });

    describe('defining an id generator function', function() {

      var domain;

      beforeEach(function () {
        domain = api({ domainPath: __dirname + '/../integration/fixture/set1' });
        domain.getNewId = null;
      });

      describe('in a synchronous way', function() {

        it('it should be transformed internally to an asynchronous way', function(done) {

          domain.idGenerator(function () {
            var id = require('uuid').v4().toString();
            return id;
          });

          domain.getNewId(function (err, id) {
            expect(id).to.be.a('string');
            done();
          });

        });

      });

      describe('in an synchronous way', function() {

        it('it should be taken as it is', function(done) {

          domain.idGenerator(function (callback) {
            setTimeout(function () {
              var id = require('uuid').v4().toString();
              callback(null, id);
            }, 10);
          });

          domain.getNewId(function (err, id) {
            expect(id).to.be.a('string');
            done();
          });

        });

      });

    });

    describe('defining the command structure', function() {

      var domain;

      beforeEach(function () {
        domain = api({ domainPath: __dirname + '/../integration/fixture/set1' });
      });

      describe('using the defaults', function () {

        it('it should apply the defaults', function() {

          var defaults = _.cloneDeep(domain.definitions.command);

          domain.defineCommand({
            payload: 'data',
            aggregate: 'aggName',
            context: 'ctx.Name',
            revision: 'rev',
            version: 'v.',
            meta: 'pass'
          });

          expect(defaults.id).to.eql(domain.definitions.command.id);
          expect(domain.definitions.command.payload).to.eql('data');
          expect(defaults.payload).not.to.eql(domain.definitions.command.payload);
          expect(defaults.name).to.eql(domain.definitions.command.name);
          expect(defaults.aggregateId).to.eql(domain.definitions.command.aggregateId);
          expect(domain.definitions.command.aggregate).to.eql('aggName');
          expect(defaults.aggregate).not.to.eql(domain.definitions.command.aggregate);
          expect(domain.definitions.command.context).to.eql('ctx.Name');
          expect(defaults.context).not.to.eql(domain.definitions.command.context);
          expect(domain.definitions.command.revision).to.eql('rev');
          expect(defaults.revision).not.to.eql(domain.definitions.command.revision);
          expect(domain.definitions.command.version).to.eql('v.');
          expect(defaults.version).not.to.eql(domain.definitions.command.version);
          expect(domain.definitions.command.meta).to.eql('pass');
          expect(defaults.meta).not.to.eql(domain.definitions.command.meta);

        });

      });

      describe('overwriting the defaults', function () {

        it('it should apply them correctly', function() {

          var defaults = _.cloneDeep(domain.definitions.command);

          domain.defineCommand({
            id: 'commandId',
            payload: 'data',
            name: 'cmdName',
            aggregateId: 'path.to.aggId',
            aggregate: 'aggName',
            context: 'ctx.Name',
            revision: 'rev',
            version: 'v.',
            meta: 'pass'
          });

          expect(domain.definitions.command.id).to.eql('commandId');
          expect(defaults.id).not.to.eql(domain.definitions.command.id);
          expect(domain.definitions.command.payload).to.eql('data');
          expect(defaults.payload).not.to.eql(domain.definitions.command.payload);
          expect(domain.definitions.command.name).to.eql('cmdName');
          expect(defaults.name).not.to.eql(domain.definitions.command.name);
          expect(domain.definitions.command.aggregateId).to.eql('path.to.aggId');
          expect(defaults.aggregateId).not.to.eql(domain.definitions.command.aggregateId);
          expect(domain.definitions.command.aggregate).to.eql('aggName');
          expect(defaults.aggregate).not.to.eql(domain.definitions.command.aggregate);
          expect(domain.definitions.command.context).to.eql('ctx.Name');
          expect(defaults.context).not.to.eql(domain.definitions.command.context);
          expect(domain.definitions.command.revision).to.eql('rev');
          expect(defaults.revision).not.to.eql(domain.definitions.command.revision);
          expect(domain.definitions.command.version).to.eql('v.');
          expect(defaults.version).not.to.eql(domain.definitions.command.version);
          expect(domain.definitions.command.meta).to.eql('pass');
          expect(defaults.meta).not.to.eql(domain.definitions.command.meta);

        });

      });

    });

    describe('defining the event structure', function() {

      var domain;

      beforeEach(function () {
        domain = api({ domainPath: __dirname + '/../integration/fixture/set1' });
      });

      describe('using the defaults', function () {

        it('it should apply the defaults', function() {

          var defaults = _.cloneDeep(domain.definitions.event);

          domain.defineEvent({
            payload: 'data',
            aggregate: 'aggName',
            context: 'ctx.Name',
            revision: 'rev',
            version: 'v.',
            meta: 'pass'
          });

          expect(defaults.correlationId).to.eql(domain.definitions.event.correlationId);
          expect(defaults.id).to.eql(domain.definitions.event.id);
          expect(domain.definitions.event.payload).to.eql('data');
          expect(defaults.payload).not.to.eql(domain.definitions.event.payload);
          expect(defaults.name).to.eql(domain.definitions.event.name);
          expect(defaults.aggregateId).to.eql(domain.definitions.event.aggregateId);
          expect(domain.definitions.event.aggregate).to.eql('aggName');
          expect(defaults.aggregate).not.to.eql(domain.definitions.event.aggregate);
          expect(domain.definitions.event.context).to.eql('ctx.Name');
          expect(defaults.context).not.to.eql(domain.definitions.event.context);
          expect(domain.definitions.event.revision).to.eql('rev');
          expect(defaults.revision).not.to.eql(domain.definitions.event.revision);
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


          expect(domain.definitions.event.correlationId).to.eql('cmdId');
          expect(defaults.correlationId).not.to.eql(domain.definitions.event.correlationId);
          expect(domain.definitions.event.id).to.eql('eventId');
          expect(defaults.id).not.to.eql(domain.definitions.event.id);
          expect(domain.definitions.event.payload).to.eql('data');
          expect(defaults.payload).not.to.eql(domain.definitions.event.payload);
          expect(domain.definitions.event.name).to.eql('defName');
          expect(defaults.name).not.to.eql(domain.definitions.event.name);
          expect(domain.definitions.event.aggregateId).to.eql('path.to.aggId');
          expect(defaults.aggregateId).not.to.eql(domain.definitions.event.aggregateId);
          expect(domain.definitions.event.aggregate).to.eql('aggName');
          expect(defaults.aggregate).not.to.eql(domain.definitions.event.aggregate);
          expect(domain.definitions.event.context).to.eql('ctx.Name');
          expect(defaults.context).not.to.eql(domain.definitions.event.context);
          expect(domain.definitions.event.revision).to.eql('rev');
          expect(defaults.revision).not.to.eql(domain.definitions.event.revision);
          expect(domain.definitions.event.version).to.eql('v.');
          expect(defaults.version).not.to.eql(domain.definitions.event.version);
          expect(domain.definitions.event.meta).to.eql('pass');
          expect(defaults.meta).not.to.eql(domain.definitions.event.meta);

        });

      });

    });

    describe('defining onEvent handler', function () {

      var domain;

      beforeEach(function () {
        domain = api({ domainPath: __dirname + '/../integration/fixture/set1' });
        domain.onEventHandle = null;
      });

      describe('in a synchronous way', function() {

        it('it should be transformed internally to an asynchronous way', function(done) {

          var called = false;
          domain.onEvent(function (evt) {
            expect(evt.my).to.eql('evt');
            called = true;
          });

          domain.onEventHandle({ my: 'evt' }, function (err) {
            expect(err).not.to.be.ok();
            expect(called).to.eql(true);
            done();
          });

        });

      });

      describe('in an synchronous way', function() {

        it('it should be taken as it is', function(done) {

          var called = false;
          domain.onEvent(function (evt, callback) {
            setTimeout(function () {
              expect(evt.my).to.eql('evt');
              called = true;
              callback(null);
            }, 10);
          });

          domain.onEventHandle({ my: 'evt' }, function (err) {
            expect(err).not.to.be.ok();
            expect(called).to.eql(true);
            done();
          });

        });

      });

    });

    describe('calling createCommandRejectedEvent', function () {

      var domain;

      beforeEach(function () {
        domain = api({ domainPath: __dirname + '/../integration/fixture/set1', commandRejectedEventName: 'cmdRej' });
        domain.defineCommand({
          id: 'i',
          name: 'n',
          aggregateId: 'ai',
          context: 'c',
          aggregate: 'a',
          payload: 'p',
          revision: 'r',
          version: 'v',
          meta: 'm'
        });
        domain.defineEvent({
          correlationId: 'corr',
          id: 'i',
          name: 'n',
          aggregateId: 'ai',
          context: 'c',
          aggregate: 'a',
          payload: 'p',
          revision: 'r',
          version: 'v',
          meta: 'm'
        });
      });

//      describe('with an error as object', function () {
//
//        it('it should return an event as expected', function () {
//
//          var cmd = { i: 'cmdId', n: 'cmdName', ai: 'aggregateId', c: 'context', p: 'payload', r: 'revision', v: 'version', m: 'meta' };
//          var err = { my: 'err' };
//
//          var evt = domain.createCommandRejectedEvent(cmd, err);
//
//          expect(evt.corr).to.eql(cmd.i);
//          expect(evt.i).to.eql(cmd.i + '_rejected');
//          expect(evt.n).to.eql('cmdRej');
//          expect(evt.ai).to.eql(cmd.ai);
//          expect(evt.c).to.eql(cmd.c);
//          expect(evt.a).to.eql(cmd.a);
//          expect(evt.r).not.to.be.ok();
//          expect(evt.v).not.to.be.ok();
//          expect(evt.m).to.eql(cmd.m);
//          expect(evt.p.command).to.eql(cmd);
//          expect(evt.p.reason).to.eql(err);
//
//        });
//
//      });
//
//      describe('with an error as Error', function () {
//
//        it('it should return an event as expected', function () {
//
//          var cmd = { i: 'cmdId', n: 'cmdName', ai: 'aggregateId', c: 'context', p: 'payload', r: 'revision', v: 'version', m: 'meta' };
//          var err = new Error('my err');
//
//          var evt = domain.createCommandRejectedEvent(cmd, err);
//
//          expect(evt.corr).to.eql(cmd.i);
//          expect(evt.i).to.eql(cmd.i + '_rejected');
//          expect(evt.n).to.eql('cmdRej');
//          expect(evt.ai).to.eql(cmd.ai);
//          expect(evt.c).to.eql(cmd.c);
//          expect(evt.a).to.eql(cmd.a);
//          expect(evt.r).not.to.be.ok();
//          expect(evt.v).not.to.be.ok();
//          expect(evt.m).to.eql(cmd.m);
//          expect(evt.p.command).to.eql(cmd);
//          expect(evt.p.reason.name).to.eql('Error');
//          expect(evt.p.reason.message).to.eql('my err');
//
//        });
//
//      });

      describe('with an error as ValidationError', function () {

        it('it should return an event as expected', function () {

          var cmd = { i: 'cmdId', n: 'cmdName', ai: 'aggregateId', c: 'context', p: 'payload', r: 'revision', v: 'version', m: 'meta' };
          var err = new ValidationError('my err', { mo: 're' });

          var evt = domain.createCommandRejectedEvent(cmd, err);

          expect(evt.corr).to.eql(cmd.i);
          expect(evt.i).to.eql(cmd.i + '_rejected');
          expect(evt.n).to.eql('cmdRej');
          expect(evt.ai).to.eql(cmd.ai);
          expect(evt.c).to.eql(cmd.c);
          expect(evt.a).to.eql(cmd.a);
          expect(evt.r).not.to.be.ok();
          expect(evt.v).not.to.be.ok();
          expect(evt.m).to.eql(cmd.m);
          expect(evt.p.command).to.eql(cmd);
          expect(evt.p.reason.name).to.eql('ValidationError');
          expect(evt.p.reason.message).to.eql('my err');
          expect(evt.p.reason.more.mo).to.eql('re');

        });

      });

      describe('with an error as BusinessRuleError', function () {

        it('it should return an event as expected', function () {

          var cmd = { i: 'cmdId', n: 'cmdName', ai: 'aggregateId', c: 'context', p: 'payload', r: 'revision', v: 'version', m: 'meta' };
          var err = new BusinessRuleError('my err');

          var evt = domain.createCommandRejectedEvent(cmd, err);

          expect(evt.corr).to.eql(cmd.i);
          expect(evt.i).to.eql(cmd.i + '_rejected');
          expect(evt.n).to.eql('cmdRej');
          expect(evt.ai).to.eql(cmd.ai);
          expect(evt.c).to.eql(cmd.c);
          expect(evt.a).to.eql(cmd.a);
          expect(evt.r).not.to.be.ok();
          expect(evt.v).not.to.be.ok();
          expect(evt.m).to.eql(cmd.m);
          expect(evt.p.command).to.eql(cmd);
          expect(evt.p.reason.name).to.eql('BusinessRuleError');
          expect(evt.p.reason.message).to.eql('my err');

        });

      });

      describe('with an error as AggregateDestroyedError', function () {

        it('it should return an event as expected', function () {

          var cmd = { i: 'cmdId', n: 'cmdName', ai: 'aggregateId', c: 'context', p: 'payload', r: 'revision', v: 'version', m: 'meta' };
          var err = new AggregateDestroyedError('my err', { mo: 're', aggregateRevision: 3 });

          var evt = domain.createCommandRejectedEvent(cmd, err);

          expect(evt.corr).to.eql(cmd.i);
          expect(evt.i).to.eql(cmd.i + '_rejected');
          expect(evt.n).to.eql('cmdRej');
          expect(evt.ai).to.eql(cmd.ai);
          expect(evt.c).to.eql(cmd.c);
          expect(evt.a).to.eql(cmd.a);
          expect(evt.r).to.eql(3);
          expect(evt.v).not.to.be.ok();
          expect(evt.m).to.eql(cmd.m);
          expect(evt.p.command).to.eql(cmd);
          expect(evt.p.reason.name).to.eql('AggregateDestroyedError');
          expect(evt.p.reason.message).to.eql('my err');
          expect(evt.p.reason.more.mo).to.eql('re');

        });

      });

      describe('with an error as AggregateConcurrencyError', function () {

        it('it should return an event as expected', function () {

          var cmd = { i: 'cmdId', n: 'cmdName', ai: 'aggregateId', c: 'context', p: 'payload', r: 'revision', v: 'version', m: 'meta' };
          var err = new AggregateConcurrencyError('my err', { mo: 're' });

          var evt = domain.createCommandRejectedEvent(cmd, err);

          expect(evt.corr).to.eql(cmd.i);
          expect(evt.i).to.eql(cmd.i + '_rejected');
          expect(evt.n).to.eql('cmdRej');
          expect(evt.ai).to.eql(cmd.ai);
          expect(evt.c).to.eql(cmd.c);
          expect(evt.a).to.eql(cmd.a);
          expect(evt.r).not.to.be.ok();
          expect(evt.v).not.to.be.ok();
          expect(evt.m).to.eql(cmd.m);
          expect(evt.p.command).to.eql(cmd);
          expect(evt.p.reason.name).to.eql('AggregateConcurrencyError');
          expect(evt.p.reason.message).to.eql('my err');
          expect(evt.p.reason.more.mo).to.eql('re');

        });

      });

    });

    describe('initializing', function () {

      var domain;

      beforeEach(function () {
        domain = api({ domainPath: __dirname + '/../integration/fixture/set1' });
        domain.defineCommand({
          id: 'i',
          name: 'n',
          aggregateId: 'ai',
          context: 'c',
          aggregate: 'a',
          payload: 'p',
          revision: 'r',
          version: 'v',
          meta: 'm'
        });
        domain.defineEvent({
          correlationId: 'corr',
          id: 'i',
          name: 'n',
          aggregateId: 'ai',
          context: 'c',
          aggregate: 'a',
          payload: 'p',
          revision: 'r',
          version: 'v',
          meta: 'm'
        });
      });

      describe('with a callback', function () {

        it('it should work as expected', function (done) {

          var called = 0;
          domain.eventStore.once('connect', function () {
            called++;
          });
          domain.aggregateLock.once('connect', function () {
            called++;
          });
          domain.once('connect', function () {
            called++;
          });

          domain.init(function (err) {
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

          domain.eventStore.once('connect', function () {
            check();
          });
          domain.aggregateLock.once('connect', function () {
            check();
          });
          domain.once('connect', function () {
            check();
          });

          domain.init();

        });

      });
    });

    describe('loading custom structure', function() {
      describe('in a synchronous way', function() {
        it('it should return as expected', function(done) {
          var domain = api({
            domainPath: __dirname + '/../integration/fixture/set1',
            structureLoader: function(options) {
              var context = new options.definitions.Context({
                name: 'ctx',
              });
              var aggregate = new options.definitions.Aggregate({
                name: 'agg'
              }, function() {});
              context.addAggregate(aggregate);
              var command = new options.definitions.Command({
                name: 'cmd'
              }, function() {});
              var event = new options.definitions.Event({
                name: 'evt'
              }, function() {});
              aggregate.addCommand(command);
              aggregate.addEvent(event);
              return {
                ctx: context
              }
            }
          });

          domain.init(function(){
            var contexts = domain.getInfo().contexts;
            expect(contexts.length).to.eql(1);
            expect(contexts[0].name).to.eql('ctx');
            expect(contexts[0].aggregates.length).to.eql(1);
            expect(contexts[0].aggregates[0].name).to.eql('agg');
            expect(contexts[0].aggregates[0].commands.length).to.eql(1);
            expect(contexts[0].aggregates[0].commands[0].name).to.eql('cmd');
            expect(contexts[0].aggregates[0].events.length).to.eql(1);
            expect(contexts[0].aggregates[0].events[0].name).to.eql('evt');
            done();
          })

        });
      });
      describe('in a asynchronous way', function() {
        it('it should return as expected', function(done) {
          var domain = api({
            domainPath: __dirname + '/../integration/fixture/set1',
            structureLoader: function(options, callback) {
              var context = new options.definitions.Context({
                name: 'ctx',
              });
              var aggregate = new options.definitions.Aggregate({
                name: 'agg'
              }, function() {});
              context.addAggregate(aggregate);
              var command = new options.definitions.Command({
                name: 'cmd'
              }, function() {});
              var event = new options.definitions.Event({
                name: 'evt'
              }, function() {});
              aggregate.addCommand(command);
              aggregate.addEvent(event);
              callback(null, { ctx: context });
            }
          });

          domain.init(function(){
            var contexts = domain.getInfo().contexts;
            expect(contexts.length).to.eql(1);
            expect(contexts[0].name).to.eql('ctx');
            expect(contexts[0].aggregates.length).to.eql(1);
            expect(contexts[0].aggregates[0].name).to.eql('agg');
            expect(contexts[0].aggregates[0].commands.length).to.eql(1);
            expect(contexts[0].aggregates[0].commands[0].name).to.eql('cmd');
            expect(contexts[0].aggregates[0].events.length).to.eql(1);
            expect(contexts[0].aggregates[0].events[0].name).to.eql('evt');
            done();
          })

        });
      });
    });

    describe('handling a command', function () {

      var domain;

      beforeEach(function () {
        domain = api({ domainPath: __dirname + '/../integration/fixture/set1' });
        domain.defineCommand({
          id: 'i',
          name: 'n',
          aggregateId: 'ai',
          context: 'c',
          aggregate: 'a',
          payload: 'p',
          revision: 'r',
          version: 'v',
          meta: 'm'
        });
        domain.defineEvent({
          correlationId: 'corr',
          id: 'i',
          name: 'n',
          aggregateId: 'ai',
          context: 'c',
          aggregate: 'a',
          payload: 'p',
          revision: 'r',
          version: 'v',
          meta: 'm'
        });
      });

      describe('with a callback', function () {

        it('it should work as expected', function (done) {

          var cmd = { i: 'cmdId', n: 'cmdName', ai: 'aggregateId', c: 'context', p: 'payload', r: 'revision', v: 'version', m: 'meta' };
          var dispatchCalled = false;
          var eventstoreCalled = [];
          var onEventCalled = [];

          domain.onEvent(function (e) {
            onEventCalled.push(e);
          });

          domain.init(function (err) {
            expect(err).not.to.be.ok();

            domain.commandDispatcher.dispatch = function (c, clb) {
              dispatchCalled = true;
              clb(null, [{ id: '1', my1: 'evt1', payload: '1' }, { id: '2', my2: 'evt2', payload: '2' }], 'aggData', 'meta');
            };

            domain.eventStore.setEventToDispatched = function (e, clb) {
              eventstoreCalled.push(e);
              clb(null);
            };

            domain.handle(cmd, function (err, evts, aggData, meta) {
              expect(err).not.to.be.ok();
              expect(dispatchCalled).to.eql(true);
              expect(aggData).to.eql('aggData');
              expect(meta).to.eql('meta');
              expect(eventstoreCalled.length).to.eql(2);
              expect(eventstoreCalled[0].my1).to.eql('evt1');
              expect(eventstoreCalled[1].my2).to.eql('evt2');
              expect(onEventCalled.length).to.eql(2);
              expect(onEventCalled[0]).to.eql('1');
              expect(onEventCalled[1]).to.eql('2');
              expect(evts.length).to.eql(2);
              expect(evts[0]).to.eql('1');
              expect(evts[1]).to.eql('2');

              done();
            });
          });

        });

      });

      describe('without a callback', function () {

        it('it should work as expected', function (done) {

          var cmd = { i: 'cmdId', n: 'cmdName', ai: 'aggregateId', c: 'context', p: 'payload', r: 'revision', v: 'version', m: 'meta' };
          var dispatchCalled = false;
          var eventstoreCalled = [];
          var onEventCalled = [];

          domain.onEvent(function (e) {
            onEventCalled.push(e);
          });

          domain.init(function (err) {
            expect(err).not.to.be.ok();

            domain.commandDispatcher.dispatch = function (c, clb) {
              dispatchCalled = true;
              clb(null, [{ id: '1', my1: 'evt1', payload: '1' }, { id: '2', my2: 'evt2', payload: '2' }], 'aggData', 'meta');
            };

            domain.eventStore.setEventToDispatched = function (e, clb) {
              eventstoreCalled.push(e);
              clb(null);

              if (eventstoreCalled.length === 2) {
                expect(dispatchCalled).to.eql(true);
                expect(eventstoreCalled.length).to.eql(2);
                expect(eventstoreCalled[0].my1).to.eql('evt1');
                expect(eventstoreCalled[1].my2).to.eql('evt2');
                expect(onEventCalled.length).to.eql(2);
                expect(onEventCalled[0]).to.eql('1');
                expect(onEventCalled[1]).to.eql('2');
                // eventstoreCalled = []; // just to be sure to exit

                done();
              }
            };

            domain.handle(cmd);
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

## File: `test/unit/validatorTest.js`
```javascript
var expect = require('expect.js'),
  validator = require('../../lib/validator');

describe('validator', function () {

  describe('executing', function () {

    describe('without any arguments', function () {

      it('it should throw an error', function () {

        expect(function () {
          validator();
        }).to.throwError(/schema/);

      });

    });

    describe('with wrong tv4 argument', function () {

      it('it should throw an error', function () {

        expect(function () {
          validator({});
        }).to.throwError(/schema/);

      });

    });

    describe('with all correct arguments', function () {

      describe('validating', function () {

        var val = validator({}, {
          "type": "object",
          "properties": {
            "firstName": {
              "title": "First name",
              "type": "string"
            },
            "lastName": {
              "title": "Last name",
              "type": "string"
            }
          },
          "required": ["firstName"]
        });

        describe('a correct object', function () {

          it('it should return null', function () {

            var res = val({ firstName: 'First', lastName: 'Name' });
            expect(res).to.eql(null);

          });

        });

        describe('a wrong object', function () {

          it('it should return a valiation error', function () {

            var res = val({ lastName: 4 });
            expect(res.name).to.eql('ValidationError');
            expect(res.message).to.match(/missing/i);
            expect(res.more).to.be.an('array');
            expect(res.more.length).to.eql(2);
            expect(res.more[1].message).to.match(/invalid/i);
            expect(res.more[1].dataPath).to.match(/lastName/);

          });

        });

      });

    });

    describe('with additional tv4 formats', function() {

      var formats = require('tv4-formats');

      describe('validating an email address with format property', function() {
        var emailValidation = validator({ formats: formats }, {
          type: 'object',
          properties: {
            email: {
              type: 'string',
              format: 'email'
            }
          }
        });

        it('should reject invalid email addresses', function() {
          var result = emailValidation({ email: 'test@example'});

          expect(result.name).to.eql('ValidationError');
        });

        it('should accept valid email addresses', function() {
          var result = emailValidation({ email: 'test-address+extension@example.com' });

          expect(result).to.eql(null);
        });
      });
    });
  });

});
```

## File: `test/unit/definitions/aggregateTest.js`
```javascript
var expect = require('expect.js'),
  _ = require('lodash'),
  DefinitionBase = require('../../../lib/definitionBase'),
  Aggregate = require('../../../lib/definitions/aggregate'),
  DefaultCommandHandler = require('../../../lib/defaultCommandHandler'),
  AggregateModel = require('../../../lib/aggregateModel'),
  api = require('../../../');

describe('aggregate definition', function () {

  describe('creating a new aggregate definition', function () {

    it('it should not throw an error', function () {

      expect(function () {
        api.defineAggregate();
      }).not.to.throwError();

    });

    it('it should return a correct object', function () {

      var aggr = api.defineAggregate();
      expect(aggr).to.be.a(DefinitionBase);
      expect(aggr).to.be.an(Aggregate);
      expect(aggr.definitions).to.be.an('object');
      expect(aggr.definitions.command).to.be.an('object');
      expect(aggr.definitions.event).to.be.an('object');
      expect(aggr.defineCommand).to.be.a('function');
      expect(aggr.defineEvent).to.be.a('function');
      expect(aggr.defineOptions).to.be.a('function');

      expect(aggr.defineSnapshotConversion).to.be.a('function');
      expect(aggr.defineSnapshotNeed).to.be.a('function');

      expect(aggr.idGenerator).to.be.a('function');
      expect(aggr.defineAggregateIdGenerator).to.be.a('function');
      expect(aggr.defineCommandAwareAggregateIdGenerator).to.be.a('function');
      expect(aggr.defineContext).to.be.a('function');
      expect(aggr.addCommand).to.be.a('function');
      expect(aggr.addEvent).to.be.a('function');
      expect(aggr.addBusinessRule).to.be.a('function');
      expect(aggr.addCommandHandler).to.be.a('function');
      expect(aggr.getCommandsByName).to.be.a('function');
      expect(aggr.getCommand).to.be.a('function');
      expect(aggr.getCommands).to.be.a('function');
      expect(aggr.getEvent).to.be.a('function');
      expect(aggr.getEvents).to.be.a('function');
      expect(aggr.getBusinessRules).to.be.a('function');
      expect(aggr.getCommandHandlers).to.be.a('function');
      expect(aggr.getCommandHandler).to.be.a('function');
      expect(aggr.create).to.be.a('function');
      expect(aggr.validateCommand).to.be.a('function');
      expect(aggr.checkBusinessRules).to.be.a('function');
      expect(aggr.handle).to.be.a('function');
      expect(aggr.apply).to.be.a('function');
      expect(aggr.loadFromHistory).to.be.a('function');
      expect(aggr.isSnapshotNeeded).to.be.a('function');

    });

    describe('defining snapshot conversions', function () {

      describe('by passing no version', function () {

        it('it should throw an error', function () {

          var aggr = api.defineAggregate();

          expect(function () {
            aggr.defineSnapshotConversion();
          }).to.throwError(/version/);

        });

      });

      describe('by passing no function', function () {

        it('it should throw an error', function () {

          var aggr = api.defineAggregate();

          expect(function () {
            aggr.defineSnapshotConversion({ version: 3 });
          }).to.throwError(/function/);

        });

      });

      describe('by passing all valid arguments', function () {

        it('it should save them as expected', function () {

          var aggr = api.defineAggregate({ name: 'a' });
          var fn1 = function () {};
          var fn2 = function () {};
          aggr.defineSnapshotConversion({ version: 2 }, fn1);
          aggr.defineSnapshotConversion({ version: 3 }, fn2);
          aggr.defineContext({ name: 'c' });
          expect(aggr.snapshotConversions['c.a.2']).to.eql(fn1);
          expect(aggr.snapshotConversions['c.a.3']).to.eql(fn2);

        });

      });

    });

    describe('defining snapshot need', function () {

      describe('by passing no function', function () {

        it('it should throw an error', function () {

          var aggr = api.defineAggregate();

          expect(function () {
            aggr.defineSnapshotNeed();
          }).to.throwError(/function/);

        });

      });

      describe('by passing all valid arguments', function () {

        it('it should save them as expected', function () {

          var aggr = api.defineAggregate();
          var fn = function () {};
          aggr.defineSnapshotNeed(fn);
          expect(aggr.isSnapshotNeeded).to.eql(fn);

        });

      });

    });

    describe('defining an id generator function', function() {

      var aggr;

      beforeEach(function () {
        aggr = api.defineAggregate();
        aggr.getNewId = null;
      });

      describe('in a synchronous way', function() {

        it('it should be transformed internally to an asynchronous way', function(done) {

          aggr.idGenerator(function () {
            var id = require('uuid').v4().toString();
            return id;
          });

          aggr.getNewId(function (err, id) {
            expect(id).to.be.a('string');
            done();
          });

        });

      });

      describe('in an synchronous way', function() {

        it('it should be taken as it is', function(done) {

          aggr.idGenerator(function (callback) {
            setTimeout(function () {
              var id = require('uuid').v4().toString();
              callback(null, id);
            }, 10);
          });

          aggr.getNewId(function (err, id) {
            expect(id).to.be.a('string');
            done();
          });

        });

      });

    });

    describe('defining an id generator function for aggregate id', function() {

      var aggr;

      beforeEach(function () {
        aggr = api.defineAggregate();
        aggr.getNewAggregateId = null;
      });

      describe('in a synchronous way', function() {

        it('it should be transformed internally to an asynchronous way', function(done) {

          aggr.defineAggregateIdGenerator(function () {
            var id = require('uuid').v4().toString();
            return id;
          });

          aggr.getNewAggregateId(function (err, id) {
            expect(id).to.be.a('string');
            done();
          });

        });

      });

      describe('in a synchronous way command aware', function() {

        it('it should be transformed internally to an asynchronous way', function(done) {

          aggr.defineCommandAwareAggregateIdGenerator(function (cmd) {
            var id = cmd.id + require('uuid').v4().toString();
            return id;
          });

          aggr.getNewAggregateId({ id: 'cmdId' }, function (err, id) {
            expect(id).to.be.a('string');
            expect(id.indexOf('cmdId')).to.eql(0);
            done();
          });

        });

      });

      describe('in an asynchronous way', function() {

        it('it should be taken as it is', function(done) {

          aggr.defineAggregateIdGenerator(function (callback) {
            setTimeout(function () {
              var id = require('uuid').v4().toString();
              callback(null, id);
            }, 10);
          });

          aggr.getNewAggregateId(function (err, id) {
            expect(id).to.be.a('string');
            done();
          });

        });

      });

      describe('in an asynchronous way command aware', function() {

        it('it should be taken as it is', function(done) {

          aggr.defineCommandAwareAggregateIdGenerator(function (cmd, callback) {
            setTimeout(function () {
              var id = cmd.id + require('uuid').v4().toString();
              callback(null, id);
            }, 10);
          });

          aggr.getNewAggregateId({ id: 'cmdId' }, function (err, id) {
            expect(id).to.be.a('string');
            expect(id.indexOf('cmdId')).to.eql(0);
            done();
          });

        });

      });

    });

    describe('calling defineContext', function () {

      describe('with a wrong object', function () {

        it('it should throw an error', function () {

          var aggr = api.defineAggregate();

          expect(function () {
            aggr.defineContext();
          }).to.throwError(/context/);

        });

      });

      describe('with a correct object', function () {

        it('it should work as expected', function () {

          var aggr = api.defineAggregate();

          aggr.defineContext({ name: 'contextName' });

          expect(aggr.context.name).to.eql('contextName');

        });

      });

    });

    describe('calling addCommand', function () {

      describe('with a wrong object', function () {

        it('it should throw an error', function () {

          var aggr = api.defineAggregate();

          expect(function () {
            aggr.addCommand();
          }).to.throwError(/command/);

        });

      });

      describe('with a correct object', function () {

        it('it should work as expected', function () {

          var aggr = api.defineAggregate();

          var defineAggregateCalled = false;
          aggr.addCommand({ name: 'myCommand', defineAggregate: function (a) {
            expect(a).to.eql(aggr);
            defineAggregateCalled = true;
          }});

          expect(aggr.commands.length).to.eql(1);
          expect(aggr.commands[0].name).to.eql('myCommand');
          expect(defineAggregateCalled).to.eql(true);

        });

      });

      describe('having not defined a default payload for commands', function () {

        describe('having not defined a payload in the command', function () {

          it('it should work as expected', function () {

            var aggr = api.defineAggregate();

            var defineAggregateCalled = false;
            aggr.addCommand({ name: 'myCommand', payload: null, defineAggregate: function (a) {
              expect(a).to.eql(aggr);
              defineAggregateCalled = true;
            }});

            expect(aggr.commands.length).to.eql(1);
            expect(aggr.commands[0].payload).to.eql('');
            expect(defineAggregateCalled).to.eql(true);

          });

        });

        describe('having defined a payload in the command', function () {

          it('it should work as expected', function () {

            var aggr = api.defineAggregate();

            var defineAggregateCalled = false;
            aggr.addCommand({ name: 'myCommand', payload: 'maPay', defineAggregate: function (a) {
              expect(a).to.eql(aggr);
              defineAggregateCalled = true;
            }});

            expect(aggr.commands.length).to.eql(1);
            expect(aggr.commands[0].payload).to.eql('maPay');
            expect(defineAggregateCalled).to.eql(true);

          });

        });

      });

      describe('having defined a default payload for commands', function () {

        describe('having not defined a payload in the command', function () {

          it('it should work as expected', function () {

            var aggr = api.defineAggregate({ defaultCommandPayload: 'def'});

            var defineAggregateCalled = false;
            aggr.addCommand({ name: 'myCommand', payload: null, defineAggregate: function (a) {
              expect(a).to.eql(aggr);
              defineAggregateCalled = true;
            } });

            expect(aggr.commands.length).to.eql(1);
            expect(aggr.commands[0].payload).to.eql('def');
            expect(defineAggregateCalled).to.eql(true);

          });

        });

        describe('having defined a payload in the command', function () {

          it('it should work as expected', function () {

            var aggr = api.defineAggregate({ defaultCommandPayload: 'def'});

            var defineAggregateCalled = false;
            aggr.addCommand({ name: 'myCommand', payload: 'maPay', defineAggregate: function (a) {
              expect(a).to.eql(aggr);
              defineAggregateCalled = true;
            }});

            expect(aggr.commands.length).to.eql(1);
            expect(aggr.commands[0].payload).to.eql('maPay');
            expect(defineAggregateCalled).to.eql(true);

          });

        });

      });

    });

    describe('calling addEvent', function () {

      describe('with a wrong object', function () {

        it('it should throw an error', function () {

          var aggr = api.defineAggregate();

          expect(function () {
            aggr.addEvent();
          }).to.throwError(/event/);

        });

      });

      describe('with a correct object', function () {

        it('it should work as expected', function () {

          var aggr = api.defineAggregate();

          aggr.addEvent({ name: 'myEvent' });

          expect(aggr.events.length).to.eql(1);
          expect(aggr.events[0].name).to.eql('myEvent');

        });

      });

      describe('having not defined a default payload for events', function () {

        describe('having not defined a payload in the event', function () {

          it('it should work as expected', function () {

            var aggr = api.defineAggregate();

            aggr.addEvent({ name: 'myEvent', payload: null });

            expect(aggr.events.length).to.eql(1);
            expect(aggr.events[0].payload).to.eql('');

          });

        });

        describe('having defined a payload in the event', function () {

          it('it should work as expected', function () {

            var aggr = api.defineAggregate();

            aggr.addEvent({ name: 'myEvent', payload: 'maPay' });

            expect(aggr.events.length).to.eql(1);
            expect(aggr.events[0].payload).to.eql('maPay');

          });

        });

      });

      describe('having defined a default payload for events', function () {

        describe('having not defined a payload in the event', function () {

          it('it should work as expected', function () {

            var aggr = api.defineAggregate({ defaultEventPayload: 'def' });

            aggr.addEvent({ name: 'myEvent', payload: null });

            expect(aggr.events.length).to.eql(1);
            expect(aggr.events[0].payload).to.eql('def');

          });

        });

        describe('having defined a payload in the command', function () {

          it('it should work as expected', function () {

            var aggr = api.defineAggregate({ defaultEventPayload: 'def' });

            aggr.addEvent({ name: 'myEvent', payload: 'maPay' });

            expect(aggr.events.length).to.eql(1);
            expect(aggr.events[0].payload).to.eql('maPay');

          });

        });

      });

    });

    describe('calling addBusinessRule', function () {

      describe('with a wrong object', function () {

        it('it should throw an error', function () {

          var aggr = api.defineAggregate();

          expect(function () {
            aggr.addBusinessRule();
          }).to.throwError(/businessRule/);

        });

      });

      describe('with a correct object', function () {

        it('it should work as expected', function () {

          var aggr = api.defineAggregate();

          aggr.addBusinessRule({ name: 'myRule', defineAggregate: function (a) { expect(a).to.eql(aggr); } });

          expect(aggr.businessRules.length).to.eql(1);
          expect(aggr.businessRules[0].name).to.eql('myRule');

        });

      });

      describe('working with priority', function () {

        it('it should order it correctly', function () {

          var aggr = api.defineAggregate();

          aggr.addBusinessRule({ name: 'myRule2', priority: 3, defineAggregate: function (a) { expect(a).to.eql(aggr); } });
          aggr.addBusinessRule({ name: 'myRule4', priority: Infinity, defineAggregate: function (a) { expect(a).to.eql(aggr); } });
          aggr.addBusinessRule({ name: 'myRule1', priority: 1, defineAggregate: function (a) { expect(a).to.eql(aggr); } });
          aggr.addBusinessRule({ name: 'myRule3', priority: 5, defineAggregate: function (a) { expect(a).to.eql(aggr); } });

          expect(aggr.businessRules.length).to.eql(4);
          expect(aggr.businessRules[0].name).to.eql('myRule1');
          expect(aggr.businessRules[1].name).to.eql('myRule2');
          expect(aggr.businessRules[2].name).to.eql('myRule3');
          expect(aggr.businessRules[3].name).to.eql('myRule4');

        });

      });

    });

    describe('calling addCommandHandler', function () {

      describe('with a wrong object', function () {

        it('it should throw an error', function () {

          var aggr = api.defineAggregate();

          expect(function () {
            aggr.addCommandHandler();
          }).to.throwError(/commandHandler/);

          expect(function () {
            aggr.addCommandHandler({ name: 'myCmdHndlName' });
          }).to.throwError(/commandHandler/);

        });

      });

      describe('with a correct object', function () {

        it('it should work as expected', function () {

          var aggr = api.defineAggregate();

          var cmdHndl = {
            name: 'myCommandHandler',
            useAggregate: function(agg) {
              expect(agg).to.eql(aggr);
            }
          };

          aggr.addCommandHandler(cmdHndl);

          expect(aggr.commandHandlers.length).to.eql(1);
          expect(aggr.commandHandlers[0]).to.eql(cmdHndl);

        });

      });

    });

    describe('having added some commands', function () {

      var aggr;

      beforeEach(function () {
        aggr = api.defineAggregate();
        aggr.addCommand({ name: 'cmd1', version: 0, defineAggregate: function () {} });
        aggr.addCommand({ name: 'cmd2', version: 0, defineAggregate: function () {} });
        aggr.addCommand({ name: 'cmd2', version: 1, defineAggregate: function () {} });
        aggr.addCommand({ name: 'cmd2', version: 2, defineAggregate: function () {} });
        aggr.addCommand({ name: 'cmd3', version: 0, defineAggregate: function () {} });
      });

      describe('calling getCommands', function () {

        it('it should return all commands', function () {

          var cmds = aggr.getCommands();
          expect(cmds.length).to.eql(5);
          expect(cmds[0].name).to.eql('cmd1');
          expect(cmds[0].version).to.eql(0);
          expect(cmds[1].name).to.eql('cmd2');
          expect(cmds[1].version).to.eql(0);
          expect(cmds[2].name).to.eql('cmd2');
          expect(cmds[2].version).to.eql(1);
          expect(cmds[3].name).to.eql('cmd2');
          expect(cmds[3].version).to.eql(2);
          expect(cmds[4].name).to.eql('cmd3');
          expect(cmds[4].version).to.eql(0);

        });

      });

      describe('calling getCommandsByName', function () {

        it('it should work as expected', function () {

          var ex0 = aggr.getCommandsByName('someCmdName');
          expect(ex0.length).to.eql(0);

          var ex1 = aggr.getCommandsByName('cmd1');
          expect(ex1.length).to.eql(1);
          expect(ex1[0].name).to.eql('cmd1');
          expect(ex1[0].version).to.eql(0);

          var ex2 = aggr.getCommandsByName('cmd2');
          expect(ex2.length).to.eql(3);
          expect(ex2[0].name).to.eql('cmd2');
          expect(ex2[0].version).to.eql(0);
          expect(ex2[1].name).to.eql('cmd2');
          expect(ex2[1].version).to.eql(1);
          expect(ex2[2].name).to.eql('cmd2');
          expect(ex2[2].version).to.eql(2);

          var ex3 = aggr.getCommandsByName('cmd3');
          expect(ex3.length).to.eql(1);
          expect(ex3[0].name).to.eql('cmd3');
          expect(ex3[0].version).to.eql(0);

        });

      });

      describe('calling getCommand', function () {

        it('it should work as expected', function () {

          var ex0 = aggr.getCommand('someCmd', 0);
          expect(ex0).not.to.be.ok();

          var ex1 = aggr.getCommand('cmd1', 3);
          expect(ex1).not.to.be.ok();

          var ex2 = aggr.getCommand('cmd1', 0);
          expect(ex2.name).to.eql('cmd1');
          expect(ex2.version).to.eql(0);

          var ex3 = aggr.getCommand('cmd2', 0);
          expect(ex3.name).to.eql('cmd2');
          expect(ex3.version).to.eql(0);

          var ex4 = aggr.getCommand('cmd2', 1);
          expect(ex4.name).to.eql('cmd2');
          expect(ex4.version).to.eql(1);

          var ex5 = aggr.getCommand('cmd2', 2);
          expect(ex5.name).to.eql('cmd2');
          expect(ex5.version).to.eql(2);

          var ex6 = aggr.getCommand('cmd3', 0);
          expect(ex6.name).to.eql('cmd3');
          expect(ex6.version).to.eql(0);

          var ex7 = aggr.getCommand('cmd3');
          expect(ex7.name).to.eql('cmd3');
          expect(ex7.version).to.eql(0);

          var ex8 = aggr.getCommand('cmd2');
          expect(ex8.name).to.eql('cmd2');
          expect(ex8.version).to.eql(0);

        });

      });

    });

    describe('having added some events', function () {

      var aggr;

      beforeEach(function () {
        aggr = api.defineAggregate();
        aggr.addEvent({ name: 'evt1', version: 0 });
        aggr.addEvent({ name: 'evt2', version: 0 });
        aggr.addEvent({ name: 'evt2', version: 1 });
        aggr.addEvent({ name: 'evt2', version: 2 });
        aggr.addEvent({ name: 'evt3', version: 0 });
      });

      describe('calling getEvents', function () {

        it('it should return all events', function () {

          var evts = aggr.getEvents();
          expect(evts.length).to.eql(5);
          expect(evts[0].name).to.eql('evt1');
          expect(evts[0].version).to.eql(0);
          expect(evts[1].name).to.eql('evt2');
          expect(evts[1].version).to.eql(0);
          expect(evts[2].name).to.eql('evt2');
          expect(evts[2].version).to.eql(1);
          expect(evts[3].name).to.eql('evt2');
          expect(evts[3].version).to.eql(2);
          expect(evts[4].name).to.eql('evt3');
          expect(evts[4].version).to.eql(0);

        });

      });

      describe('calling getEvent', function () {

        it('it should work as expected', function () {

          var ex0 = aggr.getEvent('someEvt', 0);
          expect(ex0).not.to.be.ok();

          var ex1 = aggr.getEvent('evt1', 3);
          expect(ex1).not.to.be.ok();

          var ex2 = aggr.getEvent('evt1', 0);
          expect(ex2.name).to.eql('evt1');
          expect(ex2.version).to.eql(0);

          var ex3 = aggr.getEvent('evt2', 0);
          expect(ex3.name).to.eql('evt2');
          expect(ex3.version).to.eql(0);

          var ex4 = aggr.getEvent('evt2', 1);
          expect(ex4.name).to.eql('evt2');
          expect(ex4.version).to.eql(1);

          var ex5 = aggr.getEvent('evt2', 2);
          expect(ex5.name).to.eql('evt2');
          expect(ex5.version).to.eql(2);

          var ex6 = aggr.getEvent('evt3', 0);
          expect(ex6.name).to.eql('evt3');
          expect(ex6.version).to.eql(0);

          var ex7 = aggr.getEvent('evt3');
          expect(ex7.name).to.eql('evt3');
          expect(ex7.version).to.eql(0);

          var ex8 = aggr.getEvent('evt2');
          expect(ex8.name).to.eql('evt2');
          expect(ex8.version).to.eql(0);

        });

      });

    });

    describe('having added some command handlers', function () {

      var aggr;

      beforeEach(function () {
        aggr = api.defineAggregate();
        aggr.addCommand({ name: 'someCmdHndl', version: 0, defineAggregate: function () {} });
        aggr.addCommand({ name: 'cmdHndl1', version: 0, defineAggregate: function () {} });
        aggr.addCommand({ name: 'cmdHndl2', version: 0, defineAggregate: function () {} });
        aggr.addCommand({ name: 'cmdHndl2', version: 1, defineAggregate: function () {} });
        aggr.addCommand({ name: 'cmdHndl2', version: 2, defineAggregate: function () {} });
        aggr.addCommand({ name: 'cmdHndl3', version: 0, defineAggregate: function () {} });
        aggr.addCommandHandler({ name: 'cmdHndl1', version: 0, useAggregate: function () {} });
        aggr.addCommandHandler({ name: 'cmdHndl2', version: 0, useAggregate: function () {} });
        aggr.addCommandHandler({ name: 'cmdHndl2', version: 1, useAggregate: function () {} });
        aggr.addCommandHandler({ name: 'cmdHndl2', version: 2, useAggregate: function () {} });
        aggr.addCommandHandler({ name: 'cmdHndl3', version: 0, useAggregate: function () {} });
      });

      describe('calling getCommandHandlers', function () {

        it('it should return all commandHandlers', function () {

          var cmdHndls = aggr.getCommandHandlers();
          expect(cmdHndls.length).to.eql(5);
          expect(cmdHndls[0].name).to.eql('cmdHndl1');
          expect(cmdHndls[0].version).to.eql(0);
          expect(cmdHndls[1].name).to.eql('cmdHndl2');
          expect(cmdHndls[1].version).to.eql(0);
          expect(cmdHndls[2].name).to.eql('cmdHndl2');
          expect(cmdHndls[2].version).to.eql(1);
          expect(cmdHndls[3].name).to.eql('cmdHndl2');
          expect(cmdHndls[3].version).to.eql(2);
          expect(cmdHndls[4].name).to.eql('cmdHndl3');
          expect(cmdHndls[4].version).to.eql(0);

        });

      });

      describe('calling getCommandHandler', function () {

        it('it should work as expected', function () {

          var ex0 = aggr.getCommandHandler('someCmdHndl', 0);
          expect(ex0).to.be.a(DefaultCommandHandler);
          expect(ex0).to.eql(aggr.defaultCommandHandler);

          var ex1 = aggr.getCommandHandler('cmdHndl1', 3);
          expect(ex0).to.be.a(DefaultCommandHandler);
          expect(ex0).to.eql(aggr.defaultCommandHandler);

          var ex2 = aggr.getCommandHandler('cmdHndl1', 0);
          expect(ex2.name).to.eql('cmdHndl1');
          expect(ex2.version).to.eql(0);

          var ex3 = aggr.getCommandHandler('cmdHndl2', 0);
          expect(ex3.name).to.eql('cmdHndl2');
          expect(ex3.version).to.eql(0);

          var ex4 = aggr.getCommandHandler('cmdHndl2', 1);
          expect(ex4.name).to.eql('cmdHndl2');
          expect(ex4.version).to.eql(1);

          var ex5 = aggr.getCommandHandler('cmdHndl2', 2);
          expect(ex5.name).to.eql('cmdHndl2');
          expect(ex5.version).to.eql(2);

          var ex6 = aggr.getCommandHandler('cmdHndl3', 0);
          expect(ex6.name).to.eql('cmdHndl3');
          expect(ex6.version).to.eql(0);

          var ex7 = aggr.getCommandHandler('cmdHndl3');
          expect(ex7.name).to.eql('cmdHndl3');
          expect(ex7.version).to.eql(0);

          var ex8 = aggr.getCommandHandler('cmdHndl2');
          expect(ex8.name).to.eql('cmdHndl2');
          expect(ex8.version).to.eql(0);

        });

      });

    });

    describe('calling create', function () {

      describe('with a wrong id', function () {

        it('it should throw an error', function () {

          var aggr = api.defineAggregate();

          expect(function () {
            aggr.create(123);
          }).to.throwError(/id/);

        });

      });

      describe('with a correct id', function () {

        it('it should not throw an error', function () {

          var aggr = api.defineAggregate();

          expect(function () {
            aggr.create('123');
          }).not.to.throwError();

        });

        it('it should return a correct object', function () {

          var aggr = api.defineAggregate();
          var agg = aggr.create('123');
          expect(agg).to.be.a(AggregateModel);
          expect(agg.set).to.be.a('function');
          expect(agg.get).to.be.a('function');
          expect(agg.has).to.be.a('function');
          expect(agg.setRevision).to.be.a('function');
          expect(agg.getRevision).to.be.a('function');
          expect(agg.destroy).to.be.a('function');
          expect(agg.isDestroyed).to.be.a('function');
          expect(agg.getUncommittedEvents).to.be.a('function');
          expect(agg.addUncommittedEvent).to.be.a('function');
          expect(agg.clearUncommittedEvents).to.be.a('function');
          expect(agg.toJSON).to.be.a('function');

        });

      });

      describe('having defined initialization values', function () {

        it('it should work as expected', function () {

          var aggr = api.defineAggregate(null, { stuff: [] });
          var agg = aggr.create('123');
          expect(agg).to.be.a(AggregateModel);
          expect(agg.set).to.be.a('function');
          expect(agg.get).to.be.a('function');
          expect(agg.has).to.be.a('function');
          expect(agg.setRevision).to.be.a('function');
          expect(agg.getRevision).to.be.a('function');
          expect(agg.destroy).to.be.a('function');
          expect(agg.isDestroyed).to.be.a('function');
          expect(agg.getUncommittedEvents).to.be.a('function');
          expect(agg.addUncommittedEvent).to.be.a('function');
          expect(agg.clearUncommittedEvents).to.be.a('function');
          expect(agg.toJSON).to.be.a('function');

          expect(agg.get('stuff')).to.be.an('array');
          expect(agg.get('stuff').length).to.eql(0);

        });

      });

    });

    describe('calling validateCommand', function () {

      describe('passing a command object that not have a name', function () {

        it('it should throw an Error', function (done) {

          var aggr = api.defineAggregate();

          aggr.defineCommand({
            name: 'cmdName'
          });

          aggr.validateCommand({ my: 'cmd', with: 'payload' }, function(err){
            expect(err).to.be.an(Error);
            done();
          });

        });

      });

      describe('passing a command object that not matches an existing command', function () {

        it('it should throw an Error', function (done) {

          var aggr = api.defineAggregate();

          aggr.defineCommand({
            name: 'cmdName'
          });

          aggr.validateCommand({cmdName: 'cmd', with: 'payload'}, function (err) {
            expect(err).to.be.an(Error);
            done();
          });
        });


      });

      describe('passing a command object that matches an existing command', function () {

        it('it should not throw an Error', function (done) {

          var aggr = api.defineAggregate();

          aggr.defineCommand({
            name: 'cmdName',
            version: 'v'
          });

          aggr.addCommand({ name: 'cmd', version: 2, validate: function () { return null; }, defineAggregate: function () {} });

          aggr.validateCommand({ cmdName: 'cmd', v: 2, with: 'payload' }, function(error){
            expect(error).to.be.null;
            done();
          });

        });

        it('it should return what the command validation function returns', function (done) {

          var aggr = api.defineAggregate();

          aggr.defineCommand({
            name: 'cmdName',
            version: 'v'
          });

          aggr.addCommand({ name: 'cmd', version: 2, validate: function () { return 'myValidationRes'; }, defineAggregate: function () {} });

          aggr.validateCommand({ cmdName: 'cmd', v: 2, with: 'payload' }, function(err) {
            expect(err).to.eql('myValidationRes');
            done();
          });
        });

      });

    });

    describe('calling checkBusinessRules', function () {

      it('it should call the check function on the business rule objects', function (done) {

        var aggr = api.defineAggregate();

        var ch = 'changed';
        var pr = 'previous';
        var evt = 'events';
        var cmd = 'command';

        var called = 0;

        var br1 = {
          check: function (changed, previous, events, command, callback) {
            expect(changed).to.eql(ch);
            expect(previous).to.eql(pr);
            expect(events).to.eql(evt);
            expect(command).to.eql(cmd);
            called++;
            callback(null);
          }, defineAggregate: function (a) { expect(a).to.eql(aggr); }
        };

        var br2 = {
          check: function (changed, previous, events, command, callback) {
            expect(changed).to.eql(ch);
            expect(previous).to.eql(pr);
            expect(events).to.eql(evt);
            expect(command).to.eql(cmd);
            called++;
            callback(null);
          }, defineAggregate: function (a) { expect(a).to.eql(aggr); }
        };

        aggr.addBusinessRule(br1);
        aggr.addBusinessRule(br2);

        aggr.checkBusinessRules(ch, pr, evt, cmd, done);

      });

    });

    describe('calling isSnapshotNeeded', function () {

      describe('passing more events than threshold', function () {

        it('it should work as expected', function () {

          var aggr = api.defineAggregate();
          aggr.defineSnapshotNeed(function (time, evts, model) {
            return evts.length >= 2;
          });

          var res = aggr.isSnapshotNeeded(null, [1, 2, 3, 4]);

          expect(res).to.eql(true);

        });

      });

      describe('passing less events than threshold', function () {

        it('it should work as expected', function () {

          var aggr = api.defineAggregate();

          var res = aggr.isSnapshotNeeded(null, [1, 2, 3, 4]);

          expect(res).to.eql(false);

        });

      });

    });

    describe('calling apply', function () {

      describe('with no matching event name', function () {

        it('it should throw an error', function () {

          var aggr = api.defineAggregate();

          aggr.defineEvent({
            name: 'evtName'
          });

          aggr.addEvent({ name: 'evt1', version: 0, apply: function () {} });
          aggr.addEvent({ name: 'evt2', version: 0, apply: function () {} });
          aggr.addEvent({ name: 'evt2', version: 1, apply: function () {} });
          aggr.addEvent({ name: 'evt2', version: 2, apply: function () {} });
          aggr.addEvent({ name: 'evt3', version: 0, apply: function () {} });

          expect(function () {
            aggr.apply([{ name: 'evt1' }]);
          }).to.throwError(/name/);

        });

      });

      describe('without having defined an event that handles it', function () {

        it('it should throw an error', function () {

          var aggr = api.defineAggregate();

          aggr.defineEvent({
            name: 'evtName'
          });

          aggr.addEvent({ name: 'evt1', version: 0, apply: function () {} });
          aggr.addEvent({ name: 'evt2', version: 0, apply: function () {} });
          aggr.addEvent({ name: 'evt2', version: 1, apply: function () {} });
          aggr.addEvent({ name: 'evt2', version: 2, apply: function () {} });
          aggr.addEvent({ name: 'evt3', version: 0, apply: function () {} });

          expect(function () {
            aggr.apply([{ evtName: 'evt1NotExisting' }]);
          }).to.throwError(/not found/);

        });

      });

      describe('having defined an event that handles it', function () {

        it('it should not throw an error', function () {

          var aggr = api.defineAggregate();

          aggr.defineEvent({
            name: 'evtName'
          });

          aggr.addEvent({ name: 'evt1', version: 0, apply: function () {} });
          aggr.addEvent({ name: 'evt2', version: 0, apply: function () {} });
          aggr.addEvent({ name: 'evt2', version: 1, apply: function () {} });
          aggr.addEvent({ name: 'evt2', version: 2, apply: function () {} });
          aggr.addEvent({ name: 'evt3', version: 0, apply: function () {} });

          expect(function () {
            aggr.apply([{ evtName: 'evt2' }]);
          }).not.to.throwError();

        });

        it('it should not throw an error', function (done) {

          var aggr = api.defineAggregate();

          aggr.defineEvent({
            name: 'evtName',
            version: 'v'
          });

          var checked = 0;

          function check () {
            checked++;
            if (checked === 2) {
              done();
            }
          }

          aggr.addEvent({ name: 'evt1', version: 0, apply: function () {} });
          aggr.addEvent({ name: 'evt2', version: 0, apply: function () {} });
          aggr.addEvent({ name: 'evt2', version: 1, apply: function (evt, aggModel) {
            expect(evt.evtName).to.eql('evt2');
            expect(evt.v).to.eql(1);
            expect(aggModel).to.eql('model');
            check();
          } });
          aggr.addEvent({ name: 'evt2', version: 2, apply: function () {} });
          aggr.addEvent({ name: 'evt3', version: 0, apply: function (evt, aggModel) {
            expect(evt.evtName).to.eql('evt3');
            expect(evt.v).to.eql(0);
            expect(aggModel).to.eql('model');
            check();
          } });

          aggr.apply([{ evtName: 'evt2', v: 1 }, { evtName: 'evt3', v: 0 }], 'model');

        });

      });

    });

    describe('calling loadFromHistory', function () {

      describe('passing more events than threshold', function () {

        it('it should work as expected', function () {

          var evts = [{ evtName: 'evt1' }, { evtName: 'evt2' }, { evtName: 'evt3' }];
          var aggModel = {
            set: function () {},
            setRevision: function () {},
            toJSON: function () { return 'json'; }
          };

          var aggr = api.defineAggregate();
          aggr.defineSnapshotNeed(function (time, evts, model) {
            return evts.length >= 2;
          });

          aggr.apply = function (events, aggregateModel) { // mock
            expect(events).to.eql(evts);
            expect(aggregateModel).to.eql(aggModel);
          };

          aggr.defineEvent({
            name: 'evtName'
          });

          var res = aggr.loadFromHistory(aggModel, null, evts, 4, {});

          expect(res).to.eql(true);

        });

      });

      describe('passing less events than threshold', function () {

        it('it should work as expected', function () {

          var evts = [{ evtName: 'evt1' }, { evtName: 'evt2' }, { evtName: 'evt3' }];
          var aggModel = {
            set: function () {},
            setRevision: function () {},
            toJSON: function () { return 'json'; }
          };

          var aggr = api.defineAggregate();

          aggr.apply = function (events, aggregateModel) { // mock
            expect(events).to.eql(evts);
            expect(aggregateModel).to.eql(aggModel);
          };

          aggr.defineEvent({
            name: 'evtName'
          });

          var res = aggr.loadFromHistory(aggModel, null, evts, 4, {});

          expect(res).to.eql(false);

        });

      });

      describe('passing a snapshot', function () {

        describe('with actual version', function () {

          it('it should work as expected', function () {

            var snap = {
              version: 4,
              revision: 5,
              data: {
                my: { da: 'ta' }
              }
            };

            var aggModel = {
              set: function (d) {
                expect(d).to.eql(snap.data);
              },
              setRevision: function (info, r) {
                expect(r).to.eql(6);
              }
            };

            var aggr = api.defineAggregate({ version: 4 });
            aggr.context = { name: undefined };

            aggr.defineSnapshotNeed(function (time, evts, model) {
              return evts.length >= 2;
            });

            var res = aggr.loadFromHistory(aggModel, snap, null, 4, {});

            expect(res).to.eql(false);

          });

        });

        describe('with older version', function () {

          it('it should work as expected', function () {

            var snap = {
              version: 1,
              revision: 5,
              data: {
                my: { da: 'ta' }
              }
            };

            var aggModel = {
              set: function () {
              },
              setRevision: function (info, r) {
                expect(r).to.eql(6);
              }
            };

            var aggr = api.defineAggregate({ version: 4 });

            aggr.defineSnapshotConversion({ version: 1 }, function (data, aggregateModel) {
              expect(data).to.eql(snap.data);
              expect(aggregateModel).to.eql(aggModel);
            });

            aggr.defineSnapshotNeed(function (time, evts, model) {
              return evts.length >= 2;
            });
            aggr.defineContext({ name: undefined });

            var res = aggr.loadFromHistory(aggModel, snap, null, 4, {});

            expect(res).to.eql(true);

          });

        });

      });

      describe('passing some events', function () {

        it('it should actualize the aggregateModel correctly', function () {

          var evts = [{ evtName: 'evt1', r: 3 }, { evtName: 'evt2', r: 1 }, { evtName: 'evt3', r: 2 }];
          var rev;
          var aggModel = {
            set: function () {},
            setRevision: function (info, r) { rev = r;},
            toJSON: function () { return 'json'; }
          };

          var aggr = api.defineAggregate();

          aggr.apply = function (events, aggregateModel) { // mock
            expect(events).to.eql(evts);
            expect(aggregateModel).to.eql(aggModel);
            expect(aggregateModel).to.eql(aggModel);
          };
          aggr.defineSnapshotNeed(function (time, evts, model) {
            return evts.length >= 2;
          });

          aggr.defineEvent({
            name: 'evtName',
            revision: 'r'
          });
          aggr.context = { name: undefined };

          aggr.loadFromHistory(aggModel, null, evts, 4, {});

          expect(rev).to.eql(3);

        });

        it('it should not set revision when persistance is disabled', function () {

          var evts = [{ evtName: 'nonPersistant'}];
          var rev = null;
          var aggModel = {
            set: function () {},
            setRevision: function (info, r) { rev = r;},
            toJSON: function () { return 'json'; }
          };

          var aggr = api.defineAggregate({
            skipHistory: true,
            applyLastEvent: true,
            disablePersistence: true
          });

          aggr.apply = function (evts, aggregateModel) { // mock
            expect(events).to.eql(evts);
            expect(aggregateModel).to.eql(aggModel);
            expect(aggregateModel).to.eql(aggModel);
          };

          expect(rev).to.eql(null);

        });

    });
    
      describe('passing a snapshot and some events', function () {

        it('it should actualize the aggregateModel correctly', function () {

          var evts = [{ evtName: 'evt1', r: 6 }, { evtName: 'evt2', r: 7 }, { evtName: 'evt3', r: 8 }];
          var snap = {
            version: 1,
            revision: 5,
            data: {
              my: { da: 'ta' }
            }
          };

          var rev;
          var aggModel = {
            set: function () {
            },
            setRevision: function (info, r) {
              rev = r;
            },
            toJSON: function () { return 'json'; }
          };

          var aggr = api.defineAggregate({ version: 4 });

          aggr.defineSnapshotConversion({ version: 1 }, function (data, aggregateModel) {
            expect(data).to.eql(snap.data);
            expect(aggregateModel).to.eql(aggModel);
          });
          aggr.defineSnapshotNeed(function (time, evts, model) {
            return evts.length >= 2;
          });

          aggr.apply = function (events, aggregateModel) { // mock
            expect(events).to.eql(evts);
            expect(aggregateModel).to.eql(aggModel);
            expect(aggregateModel).to.eql(aggModel);
          };

          aggr.defineEvent({
            name: 'evtName',
            revision: 'r'
          });

          aggr.defineContext({ name: undefined });

          aggr.loadFromHistory(aggModel, null, evts, 4, {});

          expect(rev).to.eql(8);

        });

      });

    });

    describe('calling handle', function () {

      describe('passing a command object that not have a name', function () {

        it('it should callback with an Error', function () {

          var aggModel = {
            get: function () {
            }
          };

          var aggr = api.defineAggregate();

          aggr.defineCommand({
            name: 'cmdName'
          });

          aggr.handle(aggModel, { my: 'cmd', with: 'payload' }, function (err) {
            expect(err).to.be.ok();
            expect(err.message).to.match(/name/);
          });

        });

      });

      describe('passing a command object that not matches an existing command', function () {

        it('it should callback with an Error', function () {

          var aggModel = {
            get: function () {
            }
          };

          var aggr = api.defineAggregate();

          aggr.defineCommand({
            name: 'cmdName'
          });

          aggr.handle(aggModel, { cmdName: 'cmd', with: 'payload' }, function (err) {
            expect(err).to.be.ok();
            expect(err.message).to.match(/not found/);
          });

        });

      });

      describe('passing a command object that matches an existing command', function () {

        it('it should not callback with an Error', function (done) {

          var rev = 0;
          var uncommittedEvts = [];
          var applyCalled = false;
          var aggModel = {
            id: 'aggId',
            set: function (k, v) {
              expect(k).to.eql('applied');
              expect(v).to.eql(true);
            },
            get: function () {
            },
            setRevision: function (info, r) { rev = r; },
            getRevision: function () { return rev; },
            toJSON: function () {},
            addUncommittedEvent: function (e) { uncommittedEvts.push(e); },
            getUncommittedEvents: function () { return uncommittedEvts; }
          };

          var cmdToUse = { cmdName: 'cmd', v: 2, with: 'payload' };

          var aggr = api.defineAggregate();

          aggr.defineCommand({
            name: 'cmdName',
            version: 'v'
          });

          aggr.defineEvent({
            name: 'evtName',
            version: 'v'
          });
          aggr.defineContext({ name: undefined });

          var pcCalled = false;
          var checkPreConditions = function (cmd, aggregateModel, clb) {
            expect(cmd).to.eql(cmdToUse);
            expect(aggregateModel).to.eql(aggModel);
            expect(aggregateModel.apply).not.to.be.ok();
            pcCalled = true;
            clb(null);
          };

          var handle = function (cmd, aggregateModel) {
            expect(cmd).to.eql(cmdToUse);
            expect(aggregateModel).to.eql(aggModel);
            expect(function () {
              aggregateModel.set();
            }).to.throwError();
            aggregateModel.apply({ evtName: 'evt', with: 'payloadOfEvt' });
          };

          aggr.addCommand({ name: 'cmd', version: 2, defineAggregate: function () {}, validate: function () { return null; }, handle: handle, checkPreConditions: checkPreConditions });

          aggr.addEvent({ name: 'evt', version: 0, apply: function (e, a) {
            a.set('applied', true);
            applyCalled = true;
          }});

          aggr.handle(aggModel, cmdToUse, function (err) {
            expect(err).not.to.be.ok();
            expect(rev).to.eql(1);
            expect(pcCalled).to.eql(true);
            expect(applyCalled).to.eql(true);

            done();
          });
        });

        it('it should work as expected', function () {

          var evts = [];
          var rev = 3;

          var aggModel = {
            id: 'myAggId',
            toJSON: function () {},
            getRevision: function () {
              return rev;
            },
            setRevision: function (i, r) {
              rev = r;
            },
            addUncommittedEvent: function (e) { evts.push(e); },
            getUncommittedEvents: function () { return evts; }
          };

          var cmdToUse = { cmdId: '111222333', cmdName: 'cmd', v: 2, with: 'payload', head: { m: 'mmm' } };

          var aggr = api.defineAggregate({ name: 'aggName' });

          aggr.defineContext({ name: 'ctxName' });

          aggr.defineCommand({
            name: 'cmdName',
            id: 'cmdId',
            version: 'v',
            aggregate: 'aName',
            context: 'c',
            meta: 'head.m'
          });

          aggr.defineEvent({
            name: 'evtName',
            version: 'v',
            id: 'iii',
            correlationId: 'commandId',
            revision: 'r',
            payload: 'p',
            aggregateId: 'a',
            aggregate: 'aName',
            context: 'c',
            meta: 'p.m'
          });

          var pcCalled = false;
          var checkPreConditions = function (cmd, aggregateModel, clb) {
            expect(cmd).to.eql(cmdToUse);
            expect(aggregateModel).to.eql(aggModel);
            expect(aggregateModel.apply).not.to.be.ok();
            pcCalled = true;
            clb(null);
          };

          var handleCalled = false;
          var handle = function (cmd, aggregateModel) {
            expect(cmd).to.eql(cmdToUse);
            expect(aggregateModel).to.eql(aggModel);
            aggregateModel.apply('evt1', { value: 'data1' });
            aggregateModel.apply({ evtName: 'evt2', p: { value: 'data2' } });
            aggregateModel.apply('evt3');
            aggregateModel.apply('evt4', { value: 'data4' }, 3);
            handleCalled = true;
          };

          var checkBRCalled = false;
          var tmpFn = aggr.checkBusinessRules;
          aggr.checkBusinessRules = function (changed, previous, events, command, callback) { // mock
            checkBRCalled = true;
            tmpFn.call(aggr, changed, previous, events, command, callback);
          };

          aggr.addCommand({ name: 'cmd', version: 2, defineAggregate: function () {}, validate: function () { return null; }, handle: handle, checkPreConditions: checkPreConditions });
          aggr.addEvent({ name: 'evt1', version: 0, apply: function (e, a) {}});
          aggr.addEvent({ name: 'evt2', version: 0, apply: function (e, a) {}});
          aggr.addEvent({ name: 'evt3', version: 0, apply: function (e, a) {}});
          aggr.addEvent({ name: 'evt4', version: 0, apply: function (e, a) {}});
          aggr.addEvent({ name: 'evt4', version: 3, apply: function (e, a) {}});
          aggr.addEvent({ name: 'evt4', version: 4, apply: function (e, a) {}});

          aggr.handle(aggModel, cmdToUse, function (err) {
            expect(err).not.to.be.ok();
            expect(pcCalled).to.eql(true);
            expect(handleCalled).to.eql(true);

            expect(evts[0].evtName).to.eql('evt1');
            expect(evts[0].iii).to.be.a('string');
            expect(evts[0].v).to.eql(0);
            expect(evts[0].r).to.eql(4);
            expect(evts[0].p.value).to.eql('data1');
            expect(evts[0].commandId).to.eql(cmdToUse.cmdId);
            expect(evts[0].a).to.eql('myAggId');
            expect(evts[0].aName).to.eql('aggName');
            expect(evts[0].c).to.eql('ctxName');
            expect(evts[0].p.m).to.eql('mmm');

            expect(evts[1].evtName).to.eql('evt2');
            expect(evts[1].iii).to.be.a('string');
            expect(evts[1].iii).not.to.eql(evts[0].iii);
            expect(evts[1].v).to.eql(0);
            expect(evts[1].r).to.eql(5);
            expect(evts[1].p.value).to.eql('data2');
            expect(evts[1].commandId).to.eql(cmdToUse.cmdId);
            expect(evts[1].a).to.eql('myAggId');
            expect(evts[1].aName).to.eql('aggName');
            expect(evts[1].c).to.eql('ctxName');
            expect(evts[1].p.m).to.eql('mmm');

            expect(evts[2].evtName).to.eql('evt3');
            expect(evts[2].iii).to.be.a('string');
            expect(evts[2].iii).not.to.eql(evts[1].iii);
            expect(evts[2].v).to.eql(0);
            expect(evts[2].r).to.eql(6);
            expect(evts[2].commandId).to.eql(cmdToUse.cmdId);
            expect(evts[2].a).to.eql('myAggId');
            expect(evts[2].aName).to.eql('aggName');
            expect(evts[2].c).to.eql('ctxName');
            expect(evts[2].p.m).to.eql('mmm');

            expect(evts[3].evtName).to.eql('evt4');
            expect(evts[3].iii).to.be.a('string');
            expect(evts[3].v).to.eql(3);
            expect(evts[3].r).to.eql(7);
            expect(evts[3].p.value).to.eql('data4');
            expect(evts[3].commandId).to.eql(cmdToUse.cmdId);
            expect(evts[3].a).to.eql('myAggId');
            expect(evts[3].aName).to.eql('aggName');
            expect(evts[3].c).to.eql('ctxName');
            expect(evts[3].p.m).to.eql('mmm');

            expect(rev).to.eql(7);

            expect(checkBRCalled).to.eql(true);
          });

        });

        describe('if business rules fails', function () {

          it('it should work as expected', function () {

            var evts = [];
            var prevValues = { '_revision': 3 };

            var aggModel = new AggregateModel('myAggId', prevValues);
            aggModel.reset = function (r) {
              if (r.attributes) {
                prevValues = r.attributes;
              } else {
                prevValues = r;
              }
            };
            aggModel.set = function (v) {
              prevValues = v;
            };
            aggModel.toJSON = function () {
              return _.cloneDeep(prevValues);
            };
            aggModel.getRevision = function () {
              return prevValues['_revision'];
            };
            aggModel.setRevision = function (r) {
              prevValues['_revision'] = r;
            };
            aggModel.addUncommittedEvent = function (e) { evts.push(e); };
            aggModel.getUncommittedEvents = function () { return evts; };
            aggModel.clearUncommittedEvents = function () { evts = []; };

            var cmdToUse = { cmdId: '111222333', cmdName: 'cmd', v: 2, with: 'payload', head: { m: 'mmm' } };

            var aggr = api.defineAggregate({ name: 'aggName', defaultPreConditionPayload: 'with' });

            aggr.defineContext({ name: 'ctxName' });

            aggr.defineCommand({
              name: 'cmdName',
              id: 'cmdId',
              version: 'v',
              aggregate: 'aName',
              context: 'c',
              meta: 'head.m'
            });

            aggr.defineEvent({
              name: 'evtName',
              version: 'v',
              id: 'iii',
              correlationId: 'commandId',
              revision: 'r',
              payload: 'p',
              aggregateId: 'a',
              aggregate: 'aName',
              context: 'c',
              meta: 'p.m'
            });

            var pcCalled = false;
            var checkPreConditions = function (cmd, aggregateModel, clb) {
              expect(cmd).to.eql(cmdToUse);
              expect(aggregateModel).to.eql(aggModel);
              expect(aggregateModel.apply).not.to.be.ok();
              pcCalled = true;
              clb(null);
            };

            var handleCalled = false;
            var handle = function (cmd, aggregateModel) {
              expect(cmd).to.eql(cmdToUse);
              expect(aggregateModel).to.eql(aggModel);
              aggregateModel.apply('evt1', { value: 'data1' });
              aggregateModel.apply({ evtName: 'evt2', p: { value: 'data2' } });
              aggregateModel.apply('evt3');
              handleCalled = true;
            };

            var checkBRCalled = false;
            var tmpFn = aggr.checkBusinessRules;
            aggr.checkBusinessRules = function (changed, previous, events, command, callback) { // mock
              checkBRCalled = true;
              callback('err');
            };

            var defineAggregateCalled = false;
            var defineAggregate = function (a) {
              expect(a).to.eql(aggr);
              defineAggregateCalled = true;
            };

            aggr.addCommand({ name: 'cmd', version: 2, validate: function () { return null; }, handle: handle, checkPreConditions: checkPreConditions, defineAggregate: defineAggregate });
            aggr.addEvent({ name: 'evt1', version: 0, apply: function (e, a) {}});
            aggr.addEvent({ name: 'evt2', version: 0, apply: function (e, a) {}});
            aggr.addEvent({ name: 'evt3', version: 0, apply: function (e, a) {}});

            aggr.handle(aggModel, cmdToUse, function (err) {
              expect(err).to.be.ok();
              expect(err).to.eql('err');

              expect(defineAggregateCalled).to.eql(true);
              expect(pcCalled).to.eql(true);
              expect(handleCalled).to.eql(true);
              expect(prevValues._revision).to.eql(3);
              expect(evts.length).to.eql(0);
              expect(checkBRCalled).to.eql(true);
            });

          });

        });

      });

    });

  });

});
```

## File: `test/unit/definitions/businessRuleTest.js`
```javascript
var expect = require('expect.js'),
  _ = require('lodash'),
  DefinitionBase = require('../../../lib/definitionBase'),
  BusinessRule = require('../../../lib/definitions/businessRule'),
  BusinessRuleError = require('../../../lib/errors/businessRuleError'),
  api = require('../../../');

describe('business rule definition', function () {

  describe('creating a new business rule definition', function () {

    describe('without any arguments', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.defineBusinessRule();
        }).to.throwError(/function/);

      });

    });

    describe('without business rule function', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.defineBusinessRule(null);
        }).to.throwError(/function/);

      });

    });

    describe('with a wrong business rule function', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.defineBusinessRule(null, 'not a function');
        }).to.throwError(/function/);

      });

    });

    describe('with a correct business rule function', function () {

      it('it should not throw an error', function () {

        expect(function () {
          api.defineBusinessRule(null, function () {});
        }).not.to.throwError();

      });

      it('it should return a correct object', function () {

        var brFn = function () {};
        var br = api.defineBusinessRule(null, brFn);
        expect(br).to.be.a(DefinitionBase);
        expect(br).to.be.a(BusinessRule);
        expect(br.businessRuleFn).to.eql(brFn);
        expect(br.description).to.eql(undefined);
        expect(br.priority).to.eql(Infinity);
        expect(br.definitions).to.be.an('object');
        expect(br.definitions.command).to.be.an('object');
        expect(br.definitions.event).to.be.an('object');
        expect(br.defineCommand).to.be.a('function');
        expect(br.defineEvent).to.be.a('function');
        expect(br.defineOptions).to.be.a('function');

        expect(br.check).to.be.a('function');

      });

    });

    describe('with some meta infos and a correct business rule function', function () {

      it('it should not throw an error', function () {

        expect(function () {
          api.defineBusinessRule({ priority: 3, description: 'bla bla bla' }, function () {});
        }).not.to.throwError();

      });

      it('it should return a correct object', function () {

        var brFn = function () {};
        var br = api.defineBusinessRule({ priority: 3, description: 'bla bla bla' }, brFn);
        expect(br).to.be.a(DefinitionBase);
        expect(br).to.be.a(BusinessRule);
        expect(br.businessRuleFn).to.eql(brFn);
        expect(br.description).to.eql('bla bla bla');
        expect(br.priority).to.eql(3);
        expect(br.definitions).to.be.an('object');
        expect(br.definitions.command).to.be.an('object');
        expect(br.definitions.event).to.be.an('object');
        expect(br.defineCommand).to.be.a('function');
        expect(br.defineEvent).to.be.a('function');
        expect(br.defineOptions).to.be.a('function');

        expect(br.check).to.be.a('function');

      });

    });
    
    describe('calling check', function () {
      
      describe('having defined a business rule function that', function () {
        
        describe('does not use a callback', function () {
          
          describe('having no error', function () {

            it('it should callback as expected', function (done) {

              var brFn = function (changed, previous, events, command) {};
              var br = api.defineBusinessRule({ priority: 3, description: 'bla bla bla' }, brFn);

              br.check({ changed: 'changed' }, { previous: 'previous' }, [{ evt: 'evt1' }], { cmd: 'cmd1' }, function (err) {
                expect(err).not.to.be.ok();
                done();
              });

            });

          });
          
          describe('but throws an error with message', function () {

            it('it should callback as expected', function (done) {

              var brFn = function (changed, previous, events, command) {
                throw new Error('errorMsg');
              };
              var br = api.defineBusinessRule({ priority: 3, description: 'bla bla bla' }, brFn);

              br.check({ changed: 'changed' }, { previous: 'previous' }, [{ evt: 'evt1' }], { cmd: 'cmd1' }, function (err) {
                expect(err).to.be.a(BusinessRuleError);
                expect(err.message).to.eql('errorMsg');
                done();
              });

            });

          });
          
          describe('but throws an error without message', function () {

            it('it should callback as expected', function (done) {

              var brFn = function (changed, previous, events, command) {
                throw new Error();
              };
              var br = api.defineBusinessRule({ priority: 3, description: 'bla bla bla' }, brFn);

              br.check({ changed: 'changed' }, { previous: 'previous' }, [{ evt: 'evt1' }], { cmd: 'cmd1' }, function (err) {
                expect(err).to.be.a(BusinessRuleError);
                expect(err.message).to.eql('bla bla bla');
                done();
              });

            });
            
          });

          describe('but throws an BusinessRuleRrror with more infos', function () {

            it('it should callback as expected', function (done) {

              var brFn = function (changed, previous, events, command) {
                throw new BusinessRuleError('my message', 'more stuff');
              };
              var br = api.defineBusinessRule({ priority: 3, description: 'bla bla bla' }, brFn);

              br.check({ changed: 'changed' }, { previous: 'previous' }, [{ evt: 'evt1' }], { cmd: 'cmd1' }, function (err) {
                expect(err).to.be.a(BusinessRuleError);
                expect(err.message).to.eql('my message');
                expect(err.more).to.eql('more stuff');
                done();
              });

            });

          });

          describe('but returns an error', function () {
            
            describe('as error with message', function () {

              it('it should callback as expected', function (done) {

                var brFn = function (changed, previous, events, command) {
                  return new Error('errorMsg');
                };
                var br = api.defineBusinessRule({ priority: 3, description: 'bla bla bla' }, brFn);

                br.check({ changed: 'changed' }, { previous: 'previous' }, [{ evt: 'evt1' }], { cmd: 'cmd1' }, function (err) {
                  expect(err).to.be.a(BusinessRuleError);
                  expect(err.message).to.eql('errorMsg');
                  done();
                });

              });

            });

            describe('as error without message', function () {

              it('it should callback as expected', function (done) {

                var brFn = function (changed, previous, events, command) {
                  return new Error();
                };
                var br = api.defineBusinessRule({ priority: 3, description: 'bla bla bla' }, brFn);

                br.check({ changed: 'changed' }, { previous: 'previous' }, [{ evt: 'evt1' }], { cmd: 'cmd1' }, function (err) {
                  expect(err).to.be.a(BusinessRuleError);
                  expect(err.message).to.eql('bla bla bla');
                  done();
                });

              });

            });

            describe('as string', function () {
              
              it('it should callback as expected', function (done) {

                var brFn = function (changed, previous, events, command) {
                  return 'errorMsg'
                };
                var br = api.defineBusinessRule({ priority: 3, description: 'bla bla bla' }, brFn);

                br.check({ changed: 'changed' }, { previous: 'previous' }, [{ evt: 'evt1' }], { cmd: 'cmd1' }, function (err) {
                  expect(err).to.be.a(BusinessRuleError);
                  expect(err.message).to.eql('errorMsg');
                  done();
                });
                
              });
              
            });
            
          });
          
        });

        describe('uses a callback', function () {

          describe('having no error', function () {

            it('it should callback as expected', function (done) {

              var brFn = function (changed, previous, events, command, callback) { callback(null); };
              var br = api.defineBusinessRule({ priority: 3, description: 'bla bla bla' }, brFn);

              br.check({ changed: 'changed' }, { previous: 'previous' }, [{ evt: 'evt1' }], { cmd: 'cmd1' }, function (err) {
                expect(err).not.to.be.ok();
                done();
              });

            });

          });

          describe('that callbacks with', function () {

            describe('as error with message', function () {

              it('it should callback as expected', function (done) {

                var brFn = function (changed, previous, events, command, callback) {
                  callback(new Error('errorMsg'));
                };
                var br = api.defineBusinessRule({ priority: 3, description: 'bla bla bla' }, brFn);

                br.check({ changed: 'changed' }, { previous: 'previous' }, [{ evt: 'evt1' }], { cmd: 'cmd1' }, function (err) {
                  expect(err).to.be.a(BusinessRuleError);
                  expect(err.message).to.eql('errorMsg');
                  done();
                });

              });

            });

            describe('as BusinessRuleError with more', function () {

              it('it should callback as expected', function (done) {

                var brFn = function (changed, previous, events, command, callback) {
                  callback(new BusinessRuleError('errorMsg', 'moreStuff'));
                };
                var br = api.defineBusinessRule({ priority: 3, description: 'bla bla bla' }, brFn);

                br.check({ changed: 'changed' }, { previous: 'previous' }, [{ evt: 'evt1' }], { cmd: 'cmd1' }, function (err) {
                  expect(err).to.be.a(BusinessRuleError);
                  expect(err.message).to.eql('errorMsg');
                  expect(err.more).to.eql('moreStuff');
                  done();
                });

              });

            });

            describe('as error without message', function () {

              it('it should callback as expected', function (done) {

                var brFn = function (changed, previous, events, command, callback) {
                  callback(new Error());
                };
                var br = api.defineBusinessRule({ priority: 3, description: 'bla bla bla' }, brFn);

                br.check({ changed: 'changed' }, { previous: 'previous' }, [{ evt: 'evt1' }], { cmd: 'cmd1' }, function (err) {
                  expect(err).to.be.a(BusinessRuleError);
                  expect(err.message).to.eql('bla bla bla');
                  done();
                });

              });

            });

            describe('as string', function () {

              it('it should callback as expected', function (done) {

                var brFn = function (changed, previous, events, command, callback) {
                  callback('errorMsg');
                };
                var br = api.defineBusinessRule({ priority: 3, description: 'bla bla bla' }, brFn);

                br.check({ changed: 'changed' }, { previous: 'previous' }, [{ evt: 'evt1' }], { cmd: 'cmd1' }, function (err) {
                  expect(err).to.be.a(BusinessRuleError);
                  expect(err.message).to.eql('errorMsg');
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

## File: `test/unit/definitions/commandHandlerTest.js`
```javascript
var expect = require('expect.js'),
  _ = require('lodash'),
  DefinitionBase = require('../../../lib/definitionBase'),
  CommandHandler = require('../../../lib/definitions/commandHandler'),
  DefaultCommandHandler = require('../../../lib/defaultCommandHandler'),
  Aggregate = require('../../../lib/definitions/aggregate'),
  eventStore = require('eventstore')(),
  aggregateLock = require('../../../lib/lock').create(),
  api = require('../../../');

describe('commandHandler definition', function () {

  describe('creating a new commandHandler definition', function () {

    describe('without any arguments', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.defineCommandHandler();
        }).to.throwError(/function/);

      });

    });

    describe('without commandHandler function', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.defineCommandHandler(null);
        }).to.throwError(/function/);

      });

    });

    describe('with a wrong commandHandler function', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.defineCommandHandler(null, 'not a function');
        }).to.throwError(/function/);

      });

    });

    describe('with a correct commandHandler function', function () {

      it('it should not throw an error', function () {

        expect(function () {
          api.defineCommandHandler(null, function () {});
        }).not.to.throwError();

      });

      it('it should return a correct object', function () {

        var cmdHndFn = function () {};
        var cmdHnd = api.defineCommandHandler(null, cmdHndFn);
        expect(cmdHnd).to.be.a(DefinitionBase);
        expect(cmdHnd).to.be.a(DefaultCommandHandler);
        expect(cmdHnd).to.be.a(CommandHandler);
        expect(cmdHnd.id).to.be.a('string');
        expect(cmdHnd.cmdHndlFn).to.eql(cmdHndFn);
        expect(cmdHnd.definitions).to.be.an('object');
        expect(cmdHnd.definitions.command).to.be.an('object');
        expect(cmdHnd.definitions.event).to.be.an('object');
        expect(cmdHnd.defineCommand).to.be.a('function');
        expect(cmdHnd.defineEvent).to.be.a('function');
        expect(cmdHnd.defineOptions).to.be.a('function');

        expect(cmdHnd.handle).to.be.a('function');

      });

    });

    describe('with some meta infos and a correct commandHandler function', function () {

      it('it should not throw an error', function () {

        expect(function () {
          api.defineCommandHandler({ name: 'commandName', version: 3 }, function () {});
        }).not.to.throwError();

      });

      it('it should return a correct object', function () {

        var cmdHndFn = function () {};
        var cmdHnd = api.defineCommandHandler({ name: 'commandName', version: 3 }, cmdHndFn);
        expect(cmdHnd).to.be.a(DefinitionBase);
        expect(cmdHnd).to.be.a(DefaultCommandHandler);
        expect(cmdHnd).to.be.a(CommandHandler);
        expect(cmdHnd.id).to.be.a('string');
        expect(cmdHnd.cmdHndlFn).to.eql(cmdHndFn);
        expect(cmdHnd.definitions).to.be.an('object');
        expect(cmdHnd.definitions.command).to.be.an('object');
        expect(cmdHnd.definitions.event).to.be.an('object');
        expect(cmdHnd.defineCommand).to.be.a('function');
        expect(cmdHnd.defineEvent).to.be.a('function');
        expect(cmdHnd.defineOptions).to.be.a('function');

        expect(cmdHnd.handle).to.be.a('function');

      });

    });

    describe('handling a command', function () {

      it('it should work as expected', function (done) {
        var cmdObj = { my: 'command', with: { deep: 'value' }, aggregate: { id: '1234' } };
        var clb = function () {};

        var cmdHndFn = function (aggId, cmd, commandHandler, callback) {
          expect(aggId).to.eql('1234');
          expect(cmd).to.eql(cmdObj);
          expect(commandHandler).to.eql(cmdHnd);
          expect(clb).to.be.a('function');
          done();
        };

        var cmdHnd = api.defineCommandHandler({ name: 'commandName', version: 3 }, cmdHndFn);
        
        // dummy / mock stuff...
        var agg = new Aggregate();
        agg.validateCommand = function (cmd) {
          return null;
        };
        cmdHnd.useAggregate(agg);
        cmdHnd.useEventStore(eventStore);
        cmdHnd.useAggregateLock(aggregateLock);
        
        cmdHnd.handle(cmdObj, clb);
      });

    });

  });

});
```

## File: `test/unit/definitions/commandTest.js`
```javascript
var expect = require('expect.js'),
  _ = require('lodash'),
  DefinitionBase = require('../../../lib/definitionBase'),
  Command = require('../../../lib/definitions/command'),
  BusinessRuleError = require('../../../lib/errors/businessRuleError'),
  api = require('../../../');

describe('command definition', function () {

  describe('creating a new command definition', function () {

    describe('without any arguments', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.defineCommand();
        }).to.throwError(/function/);

      });

    });

    describe('without command function', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.defineCommand(null);
        }).to.throwError(/function/);

      });

    });

    describe('with a wrong command function', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.defineCommand(null, 'not a function');
        }).to.throwError(/function/);

      });

    });

    describe('with a correct command function', function () {

      it('it should not throw an error', function () {

        expect(function () {
          api.defineCommand(null, function () {});
        }).not.to.throwError();

      });

      it('it should return a correct object', function () {

        var cmdFn = function () {};
        var cmd = api.defineCommand(null, cmdFn);
        expect(cmd).to.be.a(DefinitionBase);
        expect(cmd).to.be.a(Command);
        expect(cmd.cmdFn).to.eql(cmdFn);
        expect(cmd.version).to.eql(0);
        expect(cmd.payload).to.eql(null);
        expect(cmd.definitions).to.be.an('object');
        expect(cmd.definitions.command).to.be.an('object');
        expect(cmd.definitions.event).to.be.an('object');
        expect(cmd.defineCommand).to.be.a('function');
        expect(cmd.defineEvent).to.be.a('function');
        expect(cmd.defineOptions).to.be.a('function');

        expect(cmd.defineAggregate).to.be.a('function');
        expect(cmd.defineValidation).to.be.a('function');
        expect(cmd.validate).to.be.a('function');
        expect(cmd.handle).to.be.a('function');

      });

    });

    describe('with some meta infos and a correct command function', function () {

      it('it should not throw an error', function () {

        expect(function () {
          api.defineCommand({ version: 3, payload: 'some.path' }, function () {});
        }).not.to.throwError();

      });

      it('it should return a correct object', function () {

        var cmdFn = function () {};
        var cmd = api.defineCommand({ version: 3, payload: 'some.path' }, cmdFn);
        expect(cmd).to.be.a(DefinitionBase);
        expect(cmd).to.be.a(Command);
        expect(cmd.cmdFn).to.eql(cmdFn);
        expect(cmd.version).to.eql(3);
        expect(cmd.payload).to.eql('some.path');
        expect(cmd.options).to.be.an('object');
        expect(cmd.definitions).to.be.an('object');
        expect(cmd.definitions.command).to.be.an('object');
        expect(cmd.definitions.event).to.be.an('object');
        expect(cmd.defineCommand).to.be.a('function');
        expect(cmd.defineEvent).to.be.a('function');
        expect(cmd.defineOptions).to.be.a('function');

        expect(cmd.defineAggregate).to.be.a('function');
        expect(cmd.defineValidation).to.be.a('function');
        expect(cmd.validate).to.be.a('function');
        expect(cmd.handle).to.be.a('function');

      });

    });

    describe('calling defineAggregate', function () {

      describe('with a wrong object', function () {

        it('it should throw an error', function () {

          var cmd = api.defineCommand(null, function () {});

          expect(function () {
            cmd.defineAggregate();
          }).to.throwError(/aggregate/);

        });

      });

      describe('with a correct object', function () {

        it('it should work as expected', function () {

          var cmd = api.defineCommand(null, function () {});

          cmd.defineAggregate({ name: 'aggrName' });

          expect(cmd.aggregate.name).to.eql('aggrName');

        });

      });

    });

    describe('calling defineValidation', function () {

      describe('without arguments', function () {

        it('it should throw an error', function () {

          var cmdFn = function () {};
          var cmd = api.defineCommand({ version: 3, payload: 'some.path' }, cmdFn);

          expect(function () {
            cmd.defineValidation();
          }).to.throwError('function');

        });

      });

      describe('with wrong argument', function () {

        it('it should throw an error', function () {

          var cmdFn = function () {};
          var cmd = api.defineCommand({ version: 3, payload: 'some.path' }, cmdFn);

          expect(function () {
            cmd.defineValidation(3);
          }).to.throwError('function');

        });

      });

      describe('with correct argument', function () {

        it('it should not throw an error', function () {

          var cmdFn = function () {};
          var cmd = api.defineCommand({ version: 3, payload: 'some.path' }, cmdFn);

          expect(function () {
            cmd.defineValidation(function () {});
          }).not.to.throwError();

        });

        // it('it should work as expected', function () {
        //
        //   var cmdFn = function () {};
        //   var cmd = api.defineCommand({ version: 3, payload: 'some.path' }, cmdFn);
        //
        //   var valFn = function () {};
        //   cmd.defineValidation(valFn);
        //   expect(cmd.validator).to.eql(valFn);
        //
        // });

      });

    });

    describe('calling validate', function () {

      it('it should call the injected validator function', function (done) {

        var cmdFn = function () {};
        var cmd = api.defineCommand({ version: 3, payload: 'some.path' }, cmdFn);
        var cmdObj = { my: 'command' };

        var valFn = function (cmd) {
          expect(cmd).to.eql(cmdObj);
          done();
        };
        cmd.defineValidation(valFn);
        cmd.validate(cmdObj);

      });

    });

    describe('working with priority', function () {

      it('it should order it correctly', function () {

        var cmdFn = function () {};
        var cmd = api.defineCommand({ version: 3, payload: 'some.path' }, cmdFn);
        var aggr = { name: 'myAggr', defaultPreConditionPayload: 'fromAggr' };
        cmd.defineAggregate(aggr);

        cmd.addPreCondition({ name: 'myRule2', priority: 3, defineAggregate: function (a) { expect(a).to.eql(aggr); } });
        cmd.addPreCondition({ name: 'myRule4', priority: Infinity, defineAggregate: function (a) { expect(a).to.eql(aggr); } });
        cmd.addPreCondition({ name: 'myRule1', priority: 1, payload: 'mySpec', defineAggregate: function (a) { expect(a).to.eql(aggr); } });
        cmd.addPreCondition({ name: 'myRule3', priority: 5, defineAggregate: function (a) { expect(a).to.eql(aggr); } });

        expect(cmd.preConditions.length).to.eql(4);
        expect(cmd.preConditions[0].name).to.eql('myRule1');
        expect(cmd.preConditions[0].payload).to.eql('mySpec');
        expect(cmd.preConditions[1].name).to.eql('myRule2');
        expect(cmd.preConditions[1].payload).to.eql('fromAggr');
        expect(cmd.preConditions[2].name).to.eql('myRule3');
        expect(cmd.preConditions[2].payload).to.eql('fromAggr');
        expect(cmd.preConditions[3].name).to.eql('myRule4');
        expect(cmd.preConditions[3].payload).to.eql('fromAggr');

      });

    });

    describe('checking pre-condition', function () {

      it('it should work as expected', function (done) {
        var cmdObj = { my: 'command', with: { deep: 'value' } };
        var aggregateObj = { get: function () {}, has: function () {} };

        var calledPc1 = false;
        var calledPc2 = false;
        var calledPc3 = false;

        var pc = api.definePreCondition({}, function (cmd, aggregateModel, callback) {
          expect(cmd).to.eql(cmdObj);
          expect(aggregateModel).to.eql(aggregateObj);
          calledPc1 = true;
          callback();
        });

        var pc2 = api.definePreCondition({}, function (cmd, aggregateModel, callback) {
          expect(cmd).to.eql(cmdObj);
          expect(aggregateModel).to.eql(aggregateObj);
          calledPc2 = true;
          callback();
        });

        var pc3 = api.definePreCondition({ version: 1 }, function (cmd, aggregateModel, callback) {
          calledPc3 = true;
          callback();
        });

        var cmd = api.defineCommand({}, function () {});

        cmd.defineAggregate({ name: 'myAggr' });

        cmd.addPreCondition(pc);

        cmd.addPreCondition(pc2);

        cmd.addPreCondition(pc3);

        cmd.checkPreConditions(cmdObj, aggregateObj, function (err) {
          expect(err).not.to.be.ok();
          expect(calledPc1).to.eql(true);
          expect(calledPc2).to.eql(true);
          expect(calledPc3).to.eql(false);
          done();
        });
      });

    });

    describe('checking existing flag [true]', function () {

      it('it should work as expected', function (done) {
        var cmdObj = { my: 'command', with: { deep: 'value' } };
        var aggregateObj = { id: 'myId', get: function () { return 0; }, has: function () {} };


        var cmd = api.defineCommand({ existing: true }, function () {});

        cmd.defineAggregate({ name: 'myAggr' });

        cmd.checkPreConditions(cmdObj, aggregateObj, function (err) {
          expect(err).to.be.ok();
          expect(err).to.be.a(BusinessRuleError);
          expect(err.message).to.match(/already existing/);
          expect(err.more.aggregateId).to.eql('myId');
          expect(err.more.aggregateRevision).to.eql(0);
          expect(err.more.type).to.eql('AggregateNotExisting');
          done();
        });
      });

    });

    describe('checking existing flag [false]', function () {

      it('it should work as expected', function (done) {
        var cmdObj = { my: 'command', with: { deep: 'value' } };
        var aggregateObj = { id: 'myId', get: function () { return 1; }, has: function () {} };


        var cmd = api.defineCommand({ existing: false }, function () {});

        cmd.defineAggregate({ name: 'myAggr' });

        cmd.checkPreConditions(cmdObj, aggregateObj, function (err) {
          expect(err).to.be.ok();
          expect(err).to.be.a(BusinessRuleError);
          expect(err.message).to.match(/not existing/);
          expect(err.more.aggregateId).to.eql('myId');
          expect(err.more.aggregateRevision).to.eql(1);
          expect(err.more.type).to.eql('AggregateAlreadyExisting');
          done();
        });
      });

    });

    describe('handling a command', function () {

      describe('with default payload', function () {

        it('it should work as expected', function (done) {
          var cmdObj = { my: 'command', with: { deep: 'value' } };
          var aggregateObj = { get: function () {}, has: function () {} };

          var cmdFn = function (cmd, aggregateModel) {
            expect(cmd).to.eql(cmdObj);
            expect(aggregateModel).to.eql(aggregateObj);
            done();
          };

          var cmd = api.defineCommand({}, cmdFn);

          cmd.handle(cmdObj, aggregateObj);
        });

      });

      describe('with custom payload', function () {

        it('it should work as expected', function (done) {
          var cmdObj = { my: 'command', with: { deep: 'value' } };
          var aggregateObj = { get: function () {}, has: function () {} };

          var cmdFn = function (cmd, aggregateModel) {
            expect(cmd).to.eql(cmdObj.with);
            expect(aggregateModel).to.eql(aggregateObj);
            cmd.deep = 'duup';
            done();
          };

          var cmd = api.defineCommand({ payload: 'with' }, cmdFn);

          cmd.handle(cmdObj, aggregateObj);

          expect(cmdObj.with.deep).to.eql('value');
        });

      });

    });

  });

});
```

## File: `test/unit/definitions/contextTest.js`
```javascript
var expect = require('expect.js'),
  _ = require('lodash'),
  DefinitionBase = require('../../../lib/definitionBase'),
  Context = require('../../../lib/definitions/context'),
  Aggregate = require('../../../lib/definitions/aggregate'),
  api = require('../../../');

describe('context definition', function () {

  describe('creating a new context definition', function () {

    it('it should not throw an error', function () {

      expect(function () {
        api.defineContext();
      }).not.to.throwError();

    });

    it('it should return a correct object', function () {

      var ctx = api.defineContext();
      expect(ctx).to.be.a(DefinitionBase);
      expect(ctx).to.be.a(Context);
      expect(ctx.definitions).to.be.an('object');
      expect(ctx.definitions.command).to.be.an('object');
      expect(ctx.definitions.event).to.be.an('object');
      expect(ctx.defineCommand).to.be.a('function');
      expect(ctx.defineEvent).to.be.a('function');
      expect(ctx.defineOptions).to.be.a('function');

      expect(ctx.addAggregate).to.be.a('function');
      expect(ctx.getAggregate).to.be.a('function');
      expect(ctx.getAggregateForCommand).to.be.a('function');
      expect(ctx.getAggregates).to.be.a('function');

    });
    
    describe('having not added anything', function () {
      
      var ctx = api.defineContext();

      describe('calling getAggregates', function () {
        
        it('it should return an empty array', function () {
          
          var aggs = ctx.getAggregates();
          expect(aggs).to.be.an('array');
          expect(aggs.length).to.eql(0);
          
        });
        
      });

      describe('calling getAggregate with any name', function () {

        it('it should return an empty array', function () {

          var agg = ctx.getAggregate('blabla');
          expect(agg).not.to.be.ok();

        });

      });

      describe('calling getAggregate with a non-string name', function () {

        it('it should return an empty array', function () {

          expect(function () {
            ctx.getAggregate(3);
          }).to.throwError(/name/);

        });

      });

      describe('calling getAggregate without name', function () {

        it('it should return an empty array', function () {

          expect(function () {
            ctx.getAggregate();
          }).to.throwError(/name/);

        });

      });

      describe('calling getAggregateForCommand without name', function () {

        it('it should return an empty array', function () {

          expect(function () {
            ctx.getAggregateForCommand();
          }).to.throwError(/name/);

        });

      });

      describe('calling getAggregateForCommand with a non-string name', function () {

        it('it should return an empty array', function () {

          expect(function () {
            ctx.getAggregateForCommand(1);
          }).to.throwError(/name/);

        });

      });

      describe('calling getAggregateForCommand with any name but without version', function () {

        it('it should return an empty array', function () {

          var agg = ctx.getAggregateForCommand('blablaCmd');
          expect(agg).not.to.be.ok();

        });

      });

      describe('calling getAggregateForCommand with any name and version', function () {

        it('it should return an empty array', function () {

          var agg = ctx.getAggregateForCommand('blablaCmd', 0);
          expect(agg).not.to.be.ok();

        });

      });
      
    });

    describe('adding an aggregate', function () {
      
      describe('without passing an object', function () {

        it('it should throw an error', function () {

          var ctx = api.defineContext();
          
          expect(function () {
            ctx.addAggregate();
          }).to.throwError(/Aggregate/);

        });
        
      });

      describe('with a wrong object', function () {

        it('it should throw an error', function () {

          var ctx = api.defineContext();

          expect(function () {
            ctx.addAggregate({ some: 'obj' });
          }).to.throwError(/Aggregate/);

        });

      });

      describe('with a correct object', function () {

        it('it should not throw an error', function () {

          var ctx = api.defineContext();

          expect(function () {
            ctx.addAggregate(new Aggregate());
          }).not.to.throwError();

        });

        describe('and call getAggregates', function () {

          var ctx, agg1, agg2;

          beforeEach(function () {
            ctx = api.defineContext();

            agg1 = new Aggregate({ name: 'agg1' });
            agg2 = new Aggregate({ name: 'agg2' });

            ctx.addAggregate(agg1);
            ctx.addAggregate(agg2);
          });

          it('it should work as expected', function () {

            var aggs = ctx.getAggregates();
            
            expect(aggs).to.be.an('array');
            expect(aggs.length).to.eql(2);
            expect(aggs[0].name).to.eql(agg1.name);
            expect(aggs[1].name).to.eql(agg2.name);

          });
          
        });

        describe('and call getAggregate', function () {

          var ctx, agg1, agg2;

          beforeEach(function () {
            ctx = api.defineContext();

            agg1 = new Aggregate({ name: 'agg1' });
            agg2 = new Aggregate({ name: 'agg2' });

            ctx.addAggregate(agg1);
            ctx.addAggregate(agg2);
          });

          it('it should work as expected', function () {

            var aggFirst = ctx.getAggregate('agg1');
            expect(aggFirst.name).to.eql(agg1.name);

            var aggSecond = ctx.getAggregate('agg2');
            expect(aggSecond.name).to.eql(agg2.name);

          });

        });

        describe('and call getAggregateForCommand', function () {

          var ctx, agg1, agg2;

          beforeEach(function () {
            ctx = api.defineContext();

            agg1 = new Aggregate({ name: 'agg1' });
            agg1.getCommand = function (name, version) {
              if (name !== 'cmd1') {
                return null;
              }
              return { name: name, version: version};
            };
            
            agg2 = new Aggregate({ name: 'agg2' });
            agg2.getCommand = function (name, version) {
              if (name !== 'cmd2' || version !== 3) {
                return null;
              }
              return { name: name, version: version};
            };

            ctx.addAggregate(agg1);
            ctx.addAggregate(agg2);
          });

          it('it should work as expected', function () {

            var aggFirst = ctx.getAggregateForCommand('cmd1');
            expect(aggFirst.name).to.eql(agg1.name);

            var aggSecond = ctx.getAggregateForCommand('cmd2', 3);
            expect(aggSecond.name).to.eql(agg2.name);

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
            payload: 'data',
            aggregate: 'aggName',
            context: 'ctx.Name',
            revision: 'rev',
            version: 'v.',
            meta: 'pass'
          });

          expect(defaults.id).to.eql(def.definitions.command.id);
          expect(def.definitions.command.payload).to.eql('data');
          expect(defaults.payload).not.to.eql(def.definitions.command.payload);
          expect(defaults.name).to.eql(def.definitions.command.name);
          expect(defaults.aggregateId).to.eql(def.definitions.command.aggregateId);
          expect(def.definitions.command.aggregate).to.eql('aggName');
          expect(defaults.aggregate).not.to.eql(def.definitions.command.aggregate);
          expect(def.definitions.command.context).to.eql('ctx.Name');
          expect(defaults.context).not.to.eql(def.definitions.command.context);
          expect(def.definitions.command.revision).to.eql('rev');
          expect(defaults.revision).not.to.eql(def.definitions.command.revision);
          expect(def.definitions.command.version).to.eql('v.');
          expect(defaults.version).not.to.eql(def.definitions.command.version);
          expect(def.definitions.command.meta).to.eql('pass');
          expect(defaults.meta).not.to.eql(def.definitions.command.meta);

        });

      });

      describe('overwriting the defaults', function () {

        it('it should apply them correctly', function() {

          var defaults = _.cloneDeep(def.definitions.command);

          def.defineCommand({
            id: 'commandId',
            payload: 'data',
            name: 'cmdName',
            aggregateId: 'path.to.aggId',
            aggregate: 'aggName',
            context: 'ctx.Name',
            revision: 'rev',
            version: 'v.',
            meta: 'pass'
          });

          expect(def.definitions.command.id).to.eql('commandId');
          expect(defaults.id).not.to.eql(def.definitions.command.id);
          expect(def.definitions.command.payload).to.eql('data');
          expect(defaults.payload).not.to.eql(def.definitions.command.payload);
          expect(def.definitions.command.name).to.eql('cmdName');
          expect(defaults.name).not.to.eql(def.definitions.command.name);
          expect(def.definitions.command.aggregateId).to.eql('path.to.aggId');
          expect(defaults.aggregateId).not.to.eql(def.definitions.command.aggregateId);
          expect(def.definitions.command.aggregate).to.eql('aggName');
          expect(defaults.aggregate).not.to.eql(def.definitions.command.aggregate);
          expect(def.definitions.command.context).to.eql('ctx.Name');
          expect(defaults.context).not.to.eql(def.definitions.command.context);
          expect(def.definitions.command.revision).to.eql('rev');
          expect(defaults.revision).not.to.eql(def.definitions.command.revision);
          expect(def.definitions.command.version).to.eql('v.');
          expect(defaults.version).not.to.eql(def.definitions.command.version);
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
            payload: 'data',
            aggregate: 'aggName',
            context: 'ctx.Name',
            revision: 'rev',
            version: 'v.',
            meta: 'pass'
          });

          expect(defaults.correlationId).to.eql(def.definitions.event.correlationId);
          expect(defaults.id).to.eql(def.definitions.event.id);
          expect(def.definitions.event.payload).to.eql('data');
          expect(defaults.payload).not.to.eql(def.definitions.event.payload);
          expect(defaults.name).to.eql(def.definitions.event.name);
          expect(defaults.aggregateId).to.eql(def.definitions.event.aggregateId);
          expect(def.definitions.event.aggregate).to.eql('aggName');
          expect(defaults.aggregate).not.to.eql(def.definitions.event.aggregate);
          expect(def.definitions.event.context).to.eql('ctx.Name');
          expect(defaults.context).not.to.eql(def.definitions.event.context);
          expect(def.definitions.event.revision).to.eql('rev');
          expect(defaults.revision).not.to.eql(def.definitions.event.revision);
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


          expect(def.definitions.event.correlationId).to.eql('cmdId');
          expect(defaults.correlationId).not.to.eql(def.definitions.event.correlationId);
          expect(def.definitions.event.id).to.eql('eventId');
          expect(defaults.id).not.to.eql(def.definitions.event.id);
          expect(def.definitions.event.payload).to.eql('data');
          expect(defaults.payload).not.to.eql(def.definitions.event.payload);
          expect(def.definitions.event.name).to.eql('defName');
          expect(defaults.name).not.to.eql(def.definitions.event.name);
          expect(def.definitions.event.aggregateId).to.eql('path.to.aggId');
          expect(defaults.aggregateId).not.to.eql(def.definitions.event.aggregateId);
          expect(def.definitions.event.aggregate).to.eql('aggName');
          expect(defaults.aggregate).not.to.eql(def.definitions.event.aggregate);
          expect(def.definitions.event.context).to.eql('ctx.Name');
          expect(defaults.context).not.to.eql(def.definitions.event.context);
          expect(def.definitions.event.revision).to.eql('rev');
          expect(defaults.revision).not.to.eql(def.definitions.event.revision);
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

## File: `test/unit/definitions/eventTest.js`
```javascript
var expect = require('expect.js'),
  _ = require('lodash'),
  DefinitionBase = require('../../../lib/definitionBase'),
  Event = require('../../../lib/definitions/event'),
  api = require('../../../');

describe('event definition', function () {

  describe('creating a new event definition', function () {

    describe('without any arguments', function () {

      it('it should not throw an error', function () {

        expect(function () {
          api.defineEvent();
        }).not.to.throwError();

      });

    });

    describe('without event function', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.defineEvent(null);
        }).not.to.throwError();

      });

    });

    describe('with a wrong event function', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.defineEvent(null, 'not a function');
        }).to.throwError(/function/);

      });

    });

    describe('with a correct event function', function () {

      it('it should not throw an error', function () {

        expect(function () {
          api.defineEvent(null, function () {});
        }).not.to.throwError();

      });

      it('it should return a correct object', function () {

        var evtFn = function () {};
        var evt = api.defineEvent(null, evtFn);
        expect(evt).to.be.a(DefinitionBase);
        expect(evt).to.be.an(Event);
        expect(evt.evtFn).to.eql(evtFn);
        expect(evt.version).to.eql(0);
        expect(evt.payload).to.eql(null);
        expect(evt.definitions).to.be.an('object');
        expect(evt.definitions.command).to.be.an('object');
        expect(evt.definitions.event).to.be.an('object');
        expect(evt.defineCommand).to.be.a('function');
        expect(evt.defineEvent).to.be.a('function');
        expect(evt.defineOptions).to.be.a('function');

        expect(evt.apply).to.be.a('function');

      });

    });

    describe('with some meta infos and a correct event function', function () {

      it('it should not throw an error', function () {

        expect(function () {
          api.defineEvent({ version: 3, payload: 'some.path' }, function () {});
        }).not.to.throwError();

      });

      it('it should return a correct object', function () {

        var evtFn = function () {};
        var evt = api.defineEvent({ version: 3, payload: 'some.path' }, evtFn);
        expect(evt).to.be.a(DefinitionBase);
        expect(evt).to.be.an(Event);
        expect(evt.evtFn).to.eql(evtFn);
        expect(evt.version).to.eql(3);
        expect(evt.payload).to.eql('some.path');
        expect(evt.options).to.be.an('object');
        expect(evt.definitions).to.be.an('object');
        expect(evt.definitions.command).to.be.an('object');
        expect(evt.definitions.event).to.be.an('object');
        expect(evt.defineCommand).to.be.a('function');
        expect(evt.defineEvent).to.be.a('function');
        expect(evt.defineOptions).to.be.a('function');

        expect(evt.apply).to.be.a('function');

      });

    });

    describe('applying an event', function () {

      describe('with default payload', function () {

        it('it should work as expected', function (done) {
          var evtObj = { my: 'event', with: { deep: 'value' } };
          var aggregateObj = { get: function () {}, has: function () {} };

          var evtFn = function (evt, aggregateModel) {
            expect(evt).to.eql(evtObj);
            expect(aggregateModel).to.eql(aggregateObj);
            done();
          };

          var evt = api.defineEvent({}, evtFn);

          evt.apply(evtObj, aggregateObj);
        });

      });

      describe('with custom payload', function () {

        it('it should work as expected', function (done) {
          var evtObj = { my: 'event', with: { deep: 'value' } };
          var aggregateObj = { get: function () {}, has: function () {} };

          var evtFn = function (evt, aggregateModel) {
            expect(evt).to.eql(evtObj.with);
            expect(aggregateModel).to.eql(aggregateObj);
            done();
          };

          var evt = api.defineEvent({ payload: 'with' }, evtFn);

          evt.apply(evtObj, aggregateObj);
        });

      });

    });

  });

});
```

## File: `test/unit/definitions/preConditionTest.js`
```javascript
var expect = require('expect.js'),
  _ = require('lodash'),
  DefinitionBase = require('../../../lib/definitionBase'),
  PreCondition = require('../../../lib/definitions/preCondition'),
  BusinessRuleError = require('../../../lib/errors/businessRuleError'),
  api = require('../../../');

describe('pre-condition definition', function () {

  describe('creating a new pre-condition definition', function () {

    describe('without any arguments', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.definePreCondition();
        }).to.throwError(/function/);

      });

    });

    describe('without pre-condition function', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.definePreCondition(null);
        }).to.throwError(/function/);

      });

    });

    describe('with a wrong pre-condition function', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.definePreCondition(null, 'not a function');
        }).to.throwError(/function/);

      });

    });

    describe('with a correct pre-condition function', function () {

      it('it should not throw an error', function () {

        expect(function () {
          api.definePreCondition(null, function () {});
        }).not.to.throwError();

      });

      it('it should return a correct object', function () {

        var pcFn = function () {};
        var pc = api.definePreCondition(null, pcFn);
        expect(pc).to.be.a(DefinitionBase);
        expect(pc).to.be.a(PreCondition);
        expect(pc.preConditionFn).to.eql(pcFn);
        expect(pc.description).to.eql(undefined);
        expect(pc.version).to.eql(undefined);
        expect(pc.priority).to.eql(Infinity);
        expect(pc.payload).to.eql(null);
        expect(pc.definitions).to.be.an('object');
        expect(pc.definitions.command).to.be.an('object');
        expect(pc.definitions.event).to.be.an('object');
        expect(pc.defineCommand).to.be.a('function');
        expect(pc.defineEvent).to.be.a('function');
        expect(pc.defineOptions).to.be.a('function');

        expect(pc.check).to.be.a('function');

      });

      describe('with a defined version', function () {

        it('it should return a correct object', function () {

          var pcFn = function () {};
          var pc = api.definePreCondition({
            version: 0
          }, pcFn);
          expect(pc).to.be.a(DefinitionBase);
          expect(pc).to.be.a(PreCondition);
          expect(pc.preConditionFn).to.eql(pcFn);
          expect(pc.description).to.eql(undefined);
          expect(pc.version).to.eql(0);
          expect(pc.priority).to.eql(Infinity);
          expect(pc.payload).to.eql(null);
          expect(pc.definitions).to.be.an('object');
          expect(pc.definitions.command).to.be.an('object');
          expect(pc.definitions.event).to.be.an('object');
          expect(pc.defineCommand).to.be.a('function');
          expect(pc.defineEvent).to.be.a('function');
          expect(pc.defineOptions).to.be.a('function');

          expect(pc.check).to.be.a('function');

        });

      });

    });

    describe('with some meta infos and a correct pre-condition function', function () {

      it('it should not throw an error', function () {

        expect(function () {
          api.definePreCondition({ priority: 3, description: 'bla bla bla' }, function () {});
        }).not.to.throwError();

      });

      it('it should return a correct object', function () {

        var pcFn = function () {};
        var pc = api.definePreCondition({ priority: 3, description: 'bla bla bla' }, pcFn);
        expect(pc).to.be.a(DefinitionBase);
        expect(pc).to.be.a(PreCondition);
        expect(pc.preConditionFn).to.eql(pcFn);
        expect(pc.description).to.eql('bla bla bla');
        expect(pc.version).to.eql(undefined);
        expect(pc.priority).to.eql(3);
        expect(pc.payload).to.eql(null);
        expect(pc.definitions).to.be.an('object');
        expect(pc.definitions.command).to.be.an('object');
        expect(pc.definitions.event).to.be.an('object');
        expect(pc.defineCommand).to.be.a('function');
        expect(pc.defineEvent).to.be.a('function');
        expect(pc.defineOptions).to.be.a('function');

        expect(pc.check).to.be.a('function');

      });

    });

    describe('calling check', function () {

      describe('having defined a pre-condition function that', function () {

        describe('does not use a callback', function () {

          describe('having no error', function () {

            it('it should callback as expected', function (done) {

              var cmdOk = false;
              var pcFn = function (command, agg) {
                cmdOk = command.changed === 'changed';
                expect(command.changed, 'changed');
              };
              var pc = api.definePreCondition({ priority: 3, description: 'bla bla bla' }, pcFn);

              pc.check({ changed: 'changed' }, { cmd: 'cmd1' }, function (err) {
                expect(err).not.to.be.ok();
                expect(cmdOk).to.eql(true);
                done();
              });

            });

          });

          describe('but throws an error with message', function () {

            it('it should callback as expected', function (done) {

              var cmdOk = false;
              var pcFn = function (command, agg) {
                cmdOk = command.changed === 'changed';
                throw new Error('errorMsg');
              };
              var pc = api.definePreCondition({ priority: 3, description: 'bla bla bla', payload: 'deep' }, pcFn);

              pc.check({ deep: { changed: 'changed' } }, { cmd: 'cmd1' }, function (err) {
                expect(err).to.be.a(BusinessRuleError);
                expect(err.message).to.eql('errorMsg');
                expect(cmdOk).to.eql(true);
                done();
              });

            });

          });

          describe('but throws an error without message', function () {

            it('it should callback as expected', function (done) {

              var pcFn = function (agg, command) {
                throw new Error();
              };
              var pc = api.definePreCondition({ priority: 3, description: 'bla bla bla' }, pcFn);

              pc.check({ changed: 'changed' }, { cmd: 'cmd1' }, function (err) {
                expect(err).to.be.a(BusinessRuleError);
                expect(err.message).to.eql('bla bla bla');
                done();
              });

            });

          });

          describe('but throws a BusinessRuleError with more', function () {

            it('it should callback as expected', function (done) {

              var pcFn = function (agg, command) {
                throw new BusinessRuleError('my message', 'more stuff');
              };
              var pc = api.definePreCondition({ priority: 3, description: 'bla bla bla' }, pcFn);

              pc.check({ changed: 'changed' }, { cmd: 'cmd1' }, function (err) {
                expect(err).to.be.a(BusinessRuleError);
                expect(err.message).to.eql('my message');
                expect(err.more).to.eql('more stuff');
                done();
              });

            });

          });

          describe('but returns an error', function () {

            describe('as error with message', function () {

              it('it should callback as expected', function (done) {

                var pcFn = function (agg, command) {
                  return new Error('errorMsg');
                };
                var pc = api.definePreCondition({ priority: 3, description: 'bla bla bla' }, pcFn);

                pc.check({ changed: 'changed' }, { cmd: 'cmd1' }, function (err) {
                  expect(err).to.be.a(BusinessRuleError);
                  expect(err.message).to.eql('errorMsg');
                  done();
                });

              });

            });

            describe('as error without message', function () {

              it('it should callback as expected', function (done) {

                var pcFn = function (agg, command) {
                  return new Error();
                };
                var pc = api.definePreCondition({ priority: 3, description: 'bla bla bla' }, pcFn);

                pc.check({ changed: 'changed' }, { cmd: 'cmd1' }, function (err) {
                  expect(err).to.be.a(BusinessRuleError);
                  expect(err.message).to.eql('bla bla bla');
                  done();
                });

              });

            });

            describe('as string', function () {

              it('it should callback as expected', function (done) {

                var pcFn = function (agg, command) {
                  return 'errorMsg'
                };
                var pc = api.definePreCondition({ priority: 3, description: 'bla bla bla' }, pcFn);

                pc.check({ changed: 'changed' }, { cmd: 'cmd1' }, function (err) {
                  expect(err).to.be.a(BusinessRuleError);
                  expect(err.message).to.eql('errorMsg');
                  done();
                });

              });

            });

          });

        });

        describe('uses a callback', function () {

          describe('having no error', function () {

            it('it should callback as expected', function (done) {

              var pcFn = function (agg, command, callback) { callback(null); };
              var pc = api.definePreCondition({ priority: 3, description: 'bla bla bla' }, pcFn);

              pc.check({ changed: 'changed' }, { cmd: 'cmd1' }, function (err) {
                expect(err).not.to.be.ok();
                done();
              });

            });

          });

          describe('that callbacks with', function () {

            describe('as error with message', function () {

              it('it should callback as expected', function (done) {

                var pcFn = function (agg, command, callback) {
                  callback(new Error('errorMsg'));
                };
                var pc = api.definePreCondition({ priority: 3, description: 'bla bla bla' }, pcFn);

                pc.check({ changed: 'changed' }, { cmd: 'cmd1' }, function (err) {
                  expect(err).to.be.a(BusinessRuleError);
                  expect(err.message).to.eql('errorMsg');
                  done();
                });

              });

            });

            describe('as BusinessRuleError with more', function () {

              it('it should callback as expected', function (done) {

                var pcFn = function (agg, command, callback) {
                  callback(new BusinessRuleError('errorMsg', 'moreStuff'));
                };
                var pc = api.definePreCondition({ priority: 3, description: 'bla bla bla' }, pcFn);

                pc.check({ changed: 'changed' }, { cmd: 'cmd1' }, function (err) {
                  expect(err).to.be.a(BusinessRuleError);
                  expect(err.message).to.eql('errorMsg');
                  expect(err.more).to.eql('moreStuff');
                  done();
                });

              });

            });

            describe('as error without message', function () {

              it('it should callback as expected', function (done) {

                var pcFn = function (agg, command, callback) {
                  callback(new Error());
                };
                var pc = api.definePreCondition({ priority: 3, description: 'bla bla bla' }, pcFn);

                pc.check({ changed: 'changed' }, { cmd: 'cmd1' }, function (err) {
                  expect(err).to.be.a(BusinessRuleError);
                  expect(err.message).to.eql('bla bla bla');
                  done();
                });

              });

            });

            describe('as string', function () {

              it('it should callback as expected', function (done) {

                var pcFn = function (agg, command, callback) {
                  callback('errorMsg');
                };
                var pc = api.definePreCondition({ priority: 3, description: 'bla bla bla' }, pcFn);

                pc.check({ changed: 'changed' }, { cmd: 'cmd1' }, function (err) {
                  expect(err).to.be.a(BusinessRuleError);
                  expect(err.message).to.eql('errorMsg');
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

## File: `test/unit/definitions/preLoadConditionTest.js`
```javascript
var expect = require('expect.js'),
  _ = require('lodash'),
  DefinitionBase = require('../../../lib/definitionBase'),
  PreLoadCondition = require('../../../lib/definitions/preLoadCondition'),
  BusinessRuleError = require('../../../lib/errors/businessRuleError'),
  api = require('../../../');

describe('pre-load-condition definition', function () {

  describe('creating a new pre-load-condition definition', function () {

    describe('without any arguments', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.definePreLoadCondition();
        }).to.throwError(/function/);

      });

    });

    describe('without pre-load-condition function', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.definePreLoadCondition(null);
        }).to.throwError(/function/);

      });

    });

    describe('with a wrong pre-load-condition function', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.definePreLoadCondition(null, 'not a function');
        }).to.throwError(/function/);

      });

    });

    describe('with a correct pre-load-condition function', function () {

      it('it should not throw an error', function () {

        expect(function () {
          api.definePreLoadCondition(null, function () {});
        }).not.to.throwError();

      });

      it('it should return a correct object', function () {

        var pcFn = function () {};
        var pc = api.definePreLoadCondition(null, pcFn);
        expect(pc).to.be.a(DefinitionBase);
        expect(pc).to.be.a(PreLoadCondition);
        expect(pc.preLoadConditionFn).to.eql(pcFn);
        expect(pc.description).to.eql(undefined);
        expect(pc.version).to.eql(undefined);
        expect(pc.priority).to.eql(Infinity);
        expect(pc.payload).to.eql(null);
        expect(pc.definitions).to.be.an('object');
        expect(pc.definitions.command).to.be.an('object');
        expect(pc.definitions.event).to.be.an('object');
        expect(pc.defineCommand).to.be.a('function');
        expect(pc.defineEvent).to.be.a('function');
        expect(pc.defineOptions).to.be.a('function');

        expect(pc.check).to.be.a('function');

      });

      describe('with a defined version', function () {

        it('it should return a correct object', function () {

          var pcFn = function () {};
          var pc = api.definePreLoadCondition({ version: 0 }, pcFn);
          expect(pc).to.be.a(DefinitionBase);
          expect(pc).to.be.a(PreLoadCondition);
          expect(pc.preLoadConditionFn).to.eql(pcFn);
          expect(pc.description).to.eql(undefined);
          expect(pc.version).to.eql(0);
          expect(pc.priority).to.eql(Infinity);
          expect(pc.payload).to.eql(null);
          expect(pc.definitions).to.be.an('object');
          expect(pc.definitions.command).to.be.an('object');
          expect(pc.definitions.event).to.be.an('object');
          expect(pc.defineCommand).to.be.a('function');
          expect(pc.defineEvent).to.be.a('function');
          expect(pc.defineOptions).to.be.a('function');

          expect(pc.check).to.be.a('function');

        });

      });

    });

    describe('with some meta infos and a correct pre-load-condition function', function () {

      it('it should not throw an error', function () {

        expect(function () {
          api.definePreLoadCondition({ priority: 3, description: 'bla bla bla' }, function () {});
        }).not.to.throwError();

      });

      it('it should return a correct object', function () {

        var pcFn = function () {};
        var pc = api.definePreLoadCondition({ priority: 3, description: 'bla bla bla' }, pcFn);
        expect(pc).to.be.a(DefinitionBase);
        expect(pc).to.be.a(PreLoadCondition);
        expect(pc.preLoadConditionFn).to.eql(pcFn);
        expect(pc.description).to.eql('bla bla bla');
        expect(pc.version).to.eql(undefined);
        expect(pc.priority).to.eql(3);
        expect(pc.payload).to.eql(null);
        expect(pc.definitions).to.be.an('object');
        expect(pc.definitions.command).to.be.an('object');
        expect(pc.definitions.event).to.be.an('object');
        expect(pc.defineCommand).to.be.a('function');
        expect(pc.defineEvent).to.be.a('function');
        expect(pc.defineOptions).to.be.a('function');

        expect(pc.check).to.be.a('function');

      });

    });

    describe('calling check', function () {

      describe('having defined a pre-load-condition function that', function () {

        describe('does not use a callback', function () {

          describe('having no error', function () {

            it('it should callback as expected', function (done) {

              var cmdOk = false;
              var pcFn = function (command) {
                cmdOk = command.cmd === 'cmd1'
              };
              var pc = api.definePreLoadCondition({ priority: 3, description: 'bla bla bla' }, pcFn);

              pc.check({ cmd: 'cmd1' }, function (err) {
                expect(err).not.to.be.ok();
                expect(cmdOk).to.eql(true);
                done();
              });

            });

          });

          describe('but throws an error with message', function () {

            it('it should callback as expected', function (done) {

              var cmdOk = false;
              var pcFn = function (command) {
                cmdOk = command.test === 'payload'
                throw new Error('errorMsg');
              };
              var pc = api.definePreLoadCondition({ priority: 3, description: 'bla bla bla', payload: 'deep' }, pcFn);

              pc.check({ cmd: 'cmd1', deep: {test: 'payload'} }, function (err) {
                expect(err).to.be.a(BusinessRuleError);
                expect(err.message).to.eql('errorMsg');
                expect(cmdOk).to.eql(true);
                done();
              });

            });

          });

          describe('but throws an error without message', function () {

            it('it should callback as expected', function (done) {

              var pcFn = function (command) {
                throw new Error();
              };
              var pc = api.definePreLoadCondition({ priority: 3, description: 'bla bla bla' }, pcFn);

              pc.check({ cmd: 'cmd1' }, function (err) {
                expect(err).to.be.a(BusinessRuleError);
                expect(err.message).to.eql('bla bla bla');
                done();
              });

            });

          });

          describe('but throws a BusinessRuleError with more', function () {

            it('it should callback as expected', function (done) {

              var pcFn = function (command) {
                throw new BusinessRuleError('my message', 'more stuff');
              };
              var pc = api.definePreLoadCondition({ priority: 3, description: 'bla bla bla' }, pcFn);

              pc.check({ cmd: 'cmd1' }, function (err) {
                expect(err).to.be.a(BusinessRuleError);
                expect(err.message).to.eql('my message');
                expect(err.more).to.eql('more stuff');
                done();
              });

            });

          });

          describe('but returns an error', function () {

            describe('as error with message', function () {

              it('it should callback as expected', function (done) {

                var pcFn = function (command) {
                  return new Error('errorMsg');
                };
                var pc = api.definePreLoadCondition({ priority: 3, description: 'bla bla bla' }, pcFn);

                pc.check({ cmd: 'cmd1' }, function (err) {
                  expect(err).to.be.a(BusinessRuleError);
                  expect(err.message).to.eql('errorMsg');
                  done();
                });

              });

            });

            describe('as error without message', function () {

              it('it should callback as expected', function (done) {

                var pcFn = function (command) {
                  return new Error();
                };
                var pc = api.definePreLoadCondition({ priority: 3, description: 'bla bla bla' }, pcFn);

                pc.check({ cmd: 'cmd1' }, function (err) {
                  expect(err).to.be.a(BusinessRuleError);
                  expect(err.message).to.eql('bla bla bla');
                  done();
                });

              });

            });

            describe('as string', function () {

              it('it should callback as expected', function (done) {

                var pcFn = function (command) {
                  return 'errorMsg'
                };
                var pc = api.definePreLoadCondition({ priority: 3, description: 'bla bla bla' }, pcFn);

                pc.check({ cmd: 'cmd1' }, function (err) {
                  expect(err).to.be.a(BusinessRuleError);
                  expect(err.message).to.eql('errorMsg');
                  done();
                });

              });

            });

          });

        });

        describe('uses a callback', function () {

          describe('having no error', function () {

            it('it should callback as expected', function (done) {

              var pcFn = function (command, callback) { callback(null); };
              var pc = api.definePreLoadCondition({ priority: 3, description: 'bla bla bla' }, pcFn);

              pc.check({ cmd: 'cmd1' }, function (err) {
                expect(err).not.to.be.ok();
                done();
              });

            });

          });

          describe('that callbacks with', function () {

            describe('as error with message', function () {

              it('it should callback as expected', function (done) {

                var pcFn = function (command, callback) {
                  callback(new Error('errorMsg'));
                };
                var pc = api.definePreLoadCondition({ priority: 3, description: 'bla bla bla' }, pcFn);

                pc.check({ cmd: 'cmd1' }, function (err) {
                  expect(err).to.be.a(BusinessRuleError);
                  expect(err.message).to.eql('errorMsg');
                  done();
                });

              });

            });

            describe('as BusinessRuleError with more', function () {

              it('it should callback as expected', function (done) {

                var pcFn = function (command, callback) {
                  callback(new BusinessRuleError('errorMsg', 'moreStuff'));
                };
                var pc = api.definePreLoadCondition({ priority: 3, description: 'bla bla bla' }, pcFn);

                pc.check({ cmd: 'cmd1' }, function (err) {
                  expect(err).to.be.a(BusinessRuleError);
                  expect(err.message).to.eql('errorMsg');
                  expect(err.more).to.eql('moreStuff');
                  done();
                });

              });

            });

            describe('as error without message', function () {

              it('it should callback as expected', function (done) {

                var pcFn = function (command, callback) {
                  callback(new Error());
                };
                var pc = api.definePreLoadCondition({ priority: 3, description: 'bla bla bla' }, pcFn);

                pc.check({ cmd: 'cmd1' }, function (err) {
                  expect(err).to.be.a(BusinessRuleError);
                  expect(err.message).to.eql('bla bla bla');
                  done();
                });

              });

            });

            describe('as string', function () {

              it('it should callback as expected', function (done) {

                var pcFn = function (command, callback) {
                  callback('errorMsg');
                };
                var pc = api.definePreLoadCondition({ priority: 3, description: 'bla bla bla' }, pcFn);

                pc.check({ cmd: 'cmd1' }, function (err) {
                  expect(err).to.be.a(BusinessRuleError);
                  expect(err.message).to.eql('errorMsg');
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


---
id: github.com-thenativeweb-node-cqrs-eventdenormalize
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:27.590661
---

# KNOWLEDGE EXTRACT: github.com_thenativeweb_node-cqrs-eventdenormalizer_d58e923c
> **Extracted on:** 2026-04-01 15:46:59
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524767/github.com_thenativeweb_node-cqrs-eventdenormalizer_d58e923c

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

.idea

.DS_Store

*.tingo
*.db

dump.rdb

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

## File: `.tachikoma.yml`
```yaml
#.tachikoma.yml
strategy: 'david'
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

[![travis](https://img.shields.io/travis/adrai/node-cqrs-eventdenormalizer.svg)](https://travis-ci.org/adrai/node-cqrs-eventdenormalizer) [![npm](https://img.shields.io/npm/v/cqrs-eventdenormalizer.svg)](https://npmjs.org/package/cqrs-eventdenormalizer)

Node-cqrs-eventdenormalizer is a node.js module that implements the cqrs pattern.
It can be very useful as eventdenormalizer component if you work with (d)ddd, cqrs, domain, host, etc.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [Catch connect ad disconnect events](#catch-connect-ad-disconnect-events)
  - [Define the event structure](#define-the-event-structure)
  - [Define the notification structure](#define-the-notification-structure)
  - [Define the id generator function [optional]](#define-the-id-generator-function-optional)
    - [you can define a synchronous function](#you-can-define-a-synchronous-function)
    - [or you can define an asynchronous function](#or-you-can-define-an-asynchronous-function)
  - [Wire up events [optional]](#wire-up-events-optional)
    - [you can define a synchronous function](#you-can-define-a-synchronous-function-1)
    - [or you can define an asynchronous function](#or-you-can-define-an-asynchronous-function-1)
  - [Wire up notifications [optional]](#wire-up-notifications-optional)
    - [you can define a synchronous function](#you-can-define-a-synchronous-function-2)
    - [or you can define an asynchronous function](#or-you-can-define-an-asynchronous-function-2)
  - [Wire up event missing [optional]](#wire-up-event-missing-optional)
    - [you can define a synchronous function](#you-can-define-a-synchronous-function-3)
  - [Define default event extension [optional]](#define-default-event-extension-optional)
    - [you can define a synchronous function](#you-can-define-a-synchronous-function-4)
    - [or you can define an asynchronous function](#or-you-can-define-an-asynchronous-function-3)
  - [Initialization](#initialization)
  - [Handling an event](#handling-an-event)
    - [or](#or)
  - [Request denormalizer information](#request-denormalizer-information)
- [Components definition](#components-definition)
  - [Collection](#collection)
  - [ViewBuilder](#viewbuilder)
    - [ViewBuilder for multiple viewmodels in a collection](#viewbuilder-for-multiple-viewmodels-in-a-collection)
  - [EventExtender](#eventextender)
    - [for a collection (in a collection folder)](#for-a-collection-in-a-collection-folder)
    - [not for a collection](#not-for-a-collection)
  - [Replay events](#replay-events)
    - [streamed](#streamed)
    - [if you want to clear the readModel before replaying...](#if-you-want-to-clear-the-readmodel-before-replaying)
- [License](#license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Installation

    npm install cqrs-eventdenormalizer

# Usage

	var denormalizer = require('cqrs-eventdenormalizer')({
	  // the path to the "working directory"
	  // can be structured like
	  // [set 1](https://github.com/adrai/node-cqrs-eventdenormalizer/tree/master/test/integration/fixture/set1) or
	  // [set 2](https://github.com/adrai/node-cqrs-eventdenormalizer/tree/master/test/integration/fixture/set2)
	  denormalizerPath: '/path/to/my/files',

	  // optional, default is 'commandRejected'
	  // will be used to catch AggregateDestroyedError from cqrs-domain
	  commandRejectedEventName: 'rejectedCommand',

	  // optional, default is 800
	  // if using in scaled systems, this module tries to catch the concurrency issues and
	  // retries to handle the event after a timeout between 0 and the defined value
	  retryOnConcurrencyTimeout: 1000,

	  // optional, default is in-memory
	  // currently supports: mongodb, redis, tingodb, couchdb, azuretable, dynamodb and inmemory
	  // hint: [viewmodel](https://github.com/adrai/node-viewmodel#connecting-to-any-repository-mongodb-in-the-example--modewrite)
	  // hint settings like: [eventstore](https://github.com/adrai/node-eventstore#provide-implementation-for-storage)
	  repository: {
	    type: 'mongodb',
	    host: 'localhost',                          // optional
	    port: 27017,                                // optional
	    dbName: 'readmodel',                        // optional
	    timeout: 10000                              // optional
      // authSource: 'authedicationDatabase',        // optional
	    // username: 'technicalDbUser',                // optional
	    // password: 'secret'                          // optional
      // url: 'mongodb://user:pass@host:port/db?opts // optional
	  },

	  // optional, default is in-memory
	  // currently supports: mongodb, redis, tingodb, dynamodb and inmemory
	  // hint settings like: [eventstore](https://github.com/adrai/node-eventstore#provide-implementation-for-storage)
	  revisionGuard: {
	    queueTimeout: 1000,                         // optional, timeout for non-handled events in the internal in-memory queue
	    queueTimeoutMaxLoops: 3,                    // optional, maximal loop count for non-handled event in the internal in-memory queue
	    startRevisionNumber: 1,			// optional, if defined the denormaizer waits for an event with that revision to be used as first event

	    type: 'redis',
	    host: 'localhost',                          // optional
	    port: 6379,                                 // optional
	    db: 0,                                      // optional
	    prefix: 'readmodel_revision',               // optional
	    timeout: 10000                              // optional
	    // password: 'secret'                          // optional
	  },
	  skipExtendEvent: false,						// optional
	  skipOnEventMissing: false,					// optional
	  skipOnEvent: false,							// optional
	  skipOnNotification: false,					// optional
	});


## Catch connect ad disconnect events

	// repository
	denormalizer.repository.on('connect', function() {
	  console.log('repository connected');
	});

	denormalizer.repository.on('disconnect', function() {
	  console.log('repository disconnected');
	});

	// revisionGuardStore
	denormalizer.revisionGuardStore.on('connect', function() {
	  console.log('revisionGuardStore connected');
	});

	denormalizer.revisionGuardStore.on('disconnect', function() {
	  console.log('revisionGuardStore disconnected');
	});


	// anything (repository or revisionGuardStore)
	denormalizer.on('connect', function() {
	  console.log('something connected');
	});

	denormalizer.on('disconnect', function() {
	  console.log('something disconnected');
	});


## Define the event structure
The values describes the path to that property in the event message.

	denormalizer.defineEvent({
	  // optional, default is 'correlationId'
	  // will use the command id as correlationId, so you can match it in the sender
	  // will be used to copy the correlationId to the notification
	  correlationId: 'correlationId',

	  // optional, default is 'id'
	  id: 'id',

	  // optional, default is 'name'
	  name: 'name',

	  // optional, default is 'aggregate.id'
	  aggregateId: 'aggregate.id',

	  // optional
	  context: 'context.name',

	  // optional
	  aggregate: 'aggregate.name',

	  // optional, default is 'payload'
	  payload: 'payload',

	  // optional, default is 'revision'
	  // will represent the aggregate revision, can be used in next command
	  revision: 'revision',

	  // optional
	  version: 'version',

	  // optional, if defined the values of the command will be copied to the event (can be used to transport information like userId, etc..)
	  meta: 'meta'
	});


## Define the notification structure
The values describes the path to that property in the notification message.

	denormalizer.defineNotification({
	  // optional, default is 'correlationId'
	  // will use the command id as correlationId, so you can match it in the sender
	  // will be used to copy the correlationId from the event
	  correlationId: 'correlationId',

	  // optional, default is 'id'
	  id: 'id',

	  // optional, default is 'name'
	  action: 'name',

	  // optional, default is 'collection'
	  collection: 'collection',

	  // optional, default is 'payload'
	  payload: 'payload',

	  // optional, will be copied from event
	  aggregateId: 'meta.aggregate.id',

	  // optional, will be copied from event
	  context: 'meta.context.name',

	  // optional, will be copied from event
	  aggregate: 'meta.aggregate.name',

	  // optional, will be copied from event
	  // will represent the aggregate revision, can be used in next command
	  revision: 'meta.aggregate.revision',

	  // optional, will be copied from event
	  eventId: 'meta.event.id',

	  // optional, will be copied from event
	  event: 'meta.event.name',

	  // optional, if defined the values of the event will be copied to the notification (can be used to transport information like userId, etc..)
	  meta: 'meta'
	});


## Define the id generator function [optional]
### you can define a synchronous function

	denormalizer.idGenerator(function () {
	  var id = require('uuid').v4().toString();
	  return id;
	});

### or you can define an asynchronous function

	denormalizer.idGenerator(function (callback) {
	  setTimeout(function () {
	    var id = require('uuid').v4().toString();
	    callback(null, id);
	  }, 50);
	});


## Wire up events [optional]
### you can define a synchronous function

	// pass events to bus
	denormalizer.onEvent(function (evt) {
	  bus.emit('event', evt);
	});


### or you can define an asynchronous function

	// pass events to bus
	denormalizer.onEvent(function (evt, callback) {
	  bus.emit('event', evt, function ack () {
	    callback();
	  });
	});

### skip onEvent if provided
	You can skip onEvent from being called, by adding the `skipOnEvent` option to the denormalizer. Checkout the usage section for more information.


## Wire up notifications [optional]
### you can define a synchronous function

	// pass notifications to bus
	denormalizer.onNotification(function (noti) {
	  bus.emit('event', evt);
	});

### or you can define an asynchronous function

	// pass notifications to bus
	denormalizer.onNotification(function (noti, callback) {
	  bus.emit('notification', noti, function ack () {
	    callback();
	  });
	});

### skip onNotification if provided

	You can skip onNotification from being called, by addding the `skipOnNotification` option to the denormalizer. Checkout the usage section for more information.



## Wire up event missing [optional]
### you can define a synchronous function

	denormalizer.onEventMissing(function (info, evt) {
	  console.log(info);
	  console.log(evt);
	});

### skip onEventMissing if provided
	You can skip onEventMissing from being called, by adding the `skipOnEventMissing` option to the denormalizer. Checkout the usage section more information.


## Define default event extension [optional]
### you can define a synchronous function

	denormalizer.defaultEventExtension(function (evt) {
	  evt.receiver = [evt.meta.userId];
	  return evt;
	});

### or you can define an asynchronous function

	denormalizer.defaultEventExtension(function (evt, callback) {
	  evt.receiver = [evt.meta.userId];
	  callback(null, evt);
	});

### skip default event extensions 
	You can skip all event extenders and the default extensions from being executed by adding the option `skipExtendEvent` to the denormalizer. Checkout the usage section for more information.




## Using custom structure loader function
The built-in structure loader can be replaced with one adapted to your needs.
To do that, you need to include a loading method in the options object passed to the domain constructor.

	// options will contain denormalizerPath as well as the as well as a definition object containing all the constructors of the denormalizer components  ( Collection, ViewBuilder etc. )
	function structureLoader(options) {
		const collection = new options.definitions.Collection({
			name: 'col'
		});
		collection.addViewBuilder(new options.definitions.ViewBuilder({
			name: 'evt',
			aggregate: 'agg',
			context: 'ctx'              
		}, function() {}));
		return {
			collections: [
				collection
			]
		};
		// or more probably
		return myExternalLoader(options.denormalizerPath, options.definitions);
	}

	require('cqrs-eventdenormalizer')({
			denormalizerPath: '/path/to/my/files',
			structureLoader: structureLoader
	});

## Initialization

	denormalizer.init(function (err, warnings) {
	  // this callback is called when all is ready...
	  // warnings: if no warnings warnings is null, else it's an array containing errors during require of files
	});

	// or

	denormalizer.init(); // callback is optional


## Handling an event

	denormalizer.handle({
	  id: 'b80ade36-dd05-4340-8a8b-846eea6e286f',
	  correlationId: 'c80ada33-dd05-4340-8a8b-846eea6e151d',
	  name: 'enteredNewPerson',
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
	  revision: 1,
	  version: 0,
	  meta: {
	    userId: 'ccd65819-4da4-4df9-9f24-5b10bf89ef89'
	  }
	}); // callback is optional

### or

	denormalizer.handle({
	  id: 'b80ade36-dd05-4340-8a8b-846eea6e286f',
	  correlationId: 'c80ada33-dd05-4340-8a8b-846eea6e151d',
	  name: 'enteredNewPerson',
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
	  revision: 1,
	  version: 0,
	  meta: {
	    userId: 'ccd65819-4da4-4df9-9f24-5b10bf89ef89'
	  }
	}, function (errs, evt, notifications) {
	  // this callback is called when event is handled successfully or unsuccessfully
	  // errs can be of type:
	  // - null
	  // - Array of Errors
	  //
	  // evt: same as passed in 'onEvent' function
	  //
	  // notifications: Array of viewmodel changes
	});


## Request denormalizer information

After the initialization you can request the denormalizer information:

	denorm.init(function (err) {
	  denorm.getInfo();
	  // ==>
	  // {
	  //   "collections": [
	  //     {
	  //       "name": "person",
	  //       "viewBuilders": [
	  //         {
	  //           "name": "enteredNewPerson",
	  //           "aggregate": "person",
	  //           "context": "hr",
	  //           "version": 2,
      //           "priority": 223
	  //         },
	  //         {
	  //           "name": "registeredEMailAddress",
	  //           "aggregate": "person",
	  //           "context": "hr",
	  //           "version": 2,
      //           "priority": 312
	  //         }
	  //       ],
	  //       "eventExtenders": [
	  //         {
	  //           "name": "enteredNewPerson",
	  //           "aggregate": "person",
	  //           "context": "hr",
	  //           "version": 2
	  //         }
	  //       ],
	  //       "preEventExtenders": [
	  //         {
	  //           "name": "enteredNewPerson",
	  //           "aggregate": "person",
	  //           "context": "hr",
	  //           "version": 2
	  //         }
	  //       ]
	  //     },
	  //     {
	  //       "name": "personDetail",
	  //       "viewBuilders": [
	  //         {
	  //           "name": "enteredNewPerson",
	  //           "aggregate": "person",
	  //           "context": "hr",
	  //           "version": 2,
      //           "priority": 110
	  //         },
	  //         {
	  //           "name": "registeredEMailAddress",
	  //           "aggregate": "person",
	  //           "context": "hr",
	  //           "version": 2,
      //           "priority": Infinity
	  //         }
	  //       ],
	  //       "eventExtenders": [],
	  //       "preEventExtenders": []
	  //     }
	  //   ],
	  //   "generalEventExtenders": [
	  //     {
	  //       "name": "",
	  //       "aggregate": null,
	  //       "context": null,
	  //       "version": -1
	  //     }
	  //   ],
	  //   "generalPreEventExtenders": []
	  // }
	});


# Components definition

## Collection

	module.exports = require('cqrs-eventdenormalizer').defineCollection({
	  // optional, default is folder name
	  name: 'personDetail',

	  // optional, default ''
	  defaultPayload: 'payload',

	  // optional, default false
	  noReplay: false,

	  // indexes: [ // for mongodb
	  //   'profileId',
	  //   // or:
	  //   { profileId: 1 },
	  //   // or:
	  //   { index: { profileId: 1 }, options: {} },
	  // ],

	  // repositorySettings: { // optional
	  //   mongodb: { // for mongo db
	  //     indexes: [ // same as above
	  //       'profileId',
	  //       // or:
	  //       { profileId: 1 },
	  //       // or:
	  //       { index: { profileId: 1 }, options: {} },
	  //     ],
	  //   },
	  //   elasticsearch6: { // for elasticsearch 5.x and 6.x ( elasticsearch6 type / implementation / driver )
	  //     refresh: 'wait_for', // refresh behaviour on index, default is true ( ie. force index refresh ) https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-refresh.html
	  //     waitForActiveShards: 2, // optional, defaults to 1 ( ie. wait only for primary ) https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-create-index.html#create-index-wait-for-active-shards
	  //     index: { // optional applied on index create, https://www.elastic.co/guide/en/elasticsearch/reference/6.x/indices-create-index.html
	  //       settings: { // will be merged with the default ones,
	  //         number_of_shards: 3, // optional, otherwise taken from type settings, defaults to 1,
	  //         number_of_replicas: 1, // optional otherwise taken from type settings, defaults to 0,
	  //       },
	  //       mappings: { // optiona will be merged with the default ones,
	  //         properties: { // specific properties to not be handled by dynamic mapper
	  //           title: {
	  //             type: 'text',
	  //           },
	  //         },
	  //       },
	  //     },
	  //   },
	  // },
	},

	  // optionally, define some initialization data for new view models...
	{
	  emails: ['default@mycomp.org'],
	  phoneNumbers: [],
	});


If you need an information from an other collection while denormalizing an event, you can require such a collection and make some lookups.
for example

	col.findViewModels({ my: 'value' }, function (err, vms) {});

or

	col.loadViewModel('id', function (err, vm) {});

or

	col.loadViewModelIfExists('id', function (err, vm) {});

But be careful with this!

## ViewBuilder
Each viewBuilder is dedicated to a specific event. It reacts on an event and denormalizes that event in an appropriate collection.

Viewbuilders are structured by collection (not by context).

	module.exports = require('cqrs-eventdenormalizer').defineViewBuilder({
	  // optional, default is file name without extension,
	  // if name is '' it will handle all events that matches
	  name: 'enteredNewPerson',

	  // optional
	  aggregate: 'person',

	  // optional
	  context: 'hr',

	  // optional, default is 0
	  version: 2,

	  // optional, if not defined or not found it will generate a new viewmodel with new id
	  id: 'aggregate.id',

	  // optional, suppresses auto-creation of new view model if none matching the id can be found, default is true
      autoCreate: true,

	  // optional, if not defined it will pass the whole event...
	  payload: 'payload',

	  // optional, default Infinity, all view-builders will be sorted by this value
      priority: 1
	}, function (data, vm) { // instead of function you can define
	                         // a string with default handling ('create', 'update', 'delete')
	                         // or function that expects a callback (i.e. function (data, vm, callback) {})

	  // if you have multiple concurrent events that targets the same vm, you can catch it like this:
	  // during a replay the denormalization finishes and the retry does not happen
	  if (vm.actionOnCommit === 'create') {
	  	return this.retry(); // hint: do not use arrow function in this scope when using this.retry()
	  	// or
	  	//return this.retry(100); // retries to denormalize again in 0-100ms
	  	// or
	  	//return this.retry({ from: 500, to: 8000 }); // retries to denormalize again in 500-8000ms
	  }

	  vm.set('firstname', data.firstname);
	  vm.set('lastname', data.lastname);
	});

### ViewBuilder for multiple viewmodels in a collection

Be careful with the query!

A lot of viewmodels can slow down the denormalization process!

	module.exports = require('cqrs-eventdenormalizer').defineViewBuilder({
	  // optional, default is file name without extension,
	  // if name is '' it will handle all events that matches
	  name: 'enteredNewPerson',

	  // optional
	  aggregate: 'person',

	  // optional
	  context: 'hr',

	  // optional, default is 0
	  version: 2,

	  // optional, if not defined or not found it will generate a new viewmodel with new id
	  query: { group: 'admins' },

	  // optional, if not defined it will pass the whole event...
	  payload: 'payload',

	  // optional, default Infinity, all view-builders will be sorted by this value
	  priority: 1
	}, function (data, vm) { // instead of function you can define
	                         // a string with default handling ('create', 'update', 'delete')
	                         // or function that expects a callback (i.e. function (data, vm, callback) {})handling ('create', 'update', 'delete')
	  vm.set('firstname', data.firstname);
	  vm.set('lastname', data.lastname);
	  //this.remindMe({ that: 'important value' });
	  //this.retry();
	});
	// optional define a function to that returns an id that will be used as viewmodel id when id not specified in options or found
	//.useAsId(function (evt) {
	//  return 'newId';
	//});
	// or
	//.useAsId(function (evt, callback) {
	//  callback(null, 'newId');
	//});	
	// optional define a function that returns a query that will be used as query to find the viewmodels (but do not define the query in the options)
	//.useAsQuery(function (evt) {
	//  return { my: evt.payload.my };
	//});
	// or async
	//.useAsQuery(function (evt, callback) {
	//  callback(null, { my: evt.payload.my });
	//});
	// optional define a function that returns a list of items, for each the viewbuilder will run.
	//.executeForEach(function (evt) {
	//  return [{ init: 'value1' }, { init: 'value2' }];
	//});
	// or async
	//.executeForEach(function (evt, callback) {
	//  callback(null, [{ init: 'value1' }, { init: 'value2' }]);
	//});
	//
	// optional define a function that checks if an event should be handled ( before vm is loaded )
	//.defineShouldHandleEvent(function (evt) {
	//  return true;
	//});
	// or
	//.defineShouldHandleEvent(function (evt, callback) {
	//  callback(null, true');
	//});
	//
	// optional define a function that checks if an event should be handled ( after vm is loaded )
	//.defineShouldHandle(function (evt, vm) {
	//  return true;
	//});
	// or
	//.defineShouldHandle(function (evt, vm, callback) {
	//  callback(null, true');
	//});
	//
	// optional define a function that checks if an event should be handled
	//.onAfterCommit(function (evt, vm) {
	//  //var memories = this.getReminder();
	//  //console.log(memories.that); // 'important value'
	//  //doSomethingStrange()
	//});
	// or
	//.onAfterCommit(function (evt, vm, callback) {
	//  var memories = this.getReminder();
	//  //console.log(memories.that); // 'important value'
	//  // doSomethingStrange(callback)
	//  callback(memories.that === 'important value' ? null : new Error('important value not set'));
	//});

## EventExtender

### for a collection (in a collection folder)

	module.exports = require('cqrs-eventdenormalizer').defineEventExtender({
  // module.exports = require('cqrs-eventdenormalizer').definePreEventExtender({ // same api as normal EventExtenders but executed before viewBuilder so the extended event can be used
	  // optional, default is file name without extension,
	  // if name is '' it will handle all events that matches
	  name: 'enteredNewPerson',

	  // optional
	  aggregate: 'person',

	  // optional
	  context: 'hr',

	  // optional, default is 0
	  // if set to -1, it will ignore the version
	  version: 2//,

	  // optional, if not defined it will pass the whole event...
	  // payload: 'payload'
	}, function (evt, col, callback) {
	  // col.loadViewModel()... or from somewhere else... (col.findViewModels( /* see https://github.com/adrai/node-viewmodel#find */ ))
	  evt.extended = true;
	  callback(null, evt);
	});

	// or

	module.exports = require('cqrs-eventdenormalizer').defineEventExtender({
	  // optional, default is file name without extension,
	  // if name is '' it will handle all events that matches
	  name: 'enteredNewPerson',

	  // optional
	  aggregate: 'person',

	  // optional
	  context: 'hr',

	  // optional, default is 0
	  // if set to -1, it will ignore the version
	  version: 2,

	  // if defined it will load the viewmodel
	  id: 'payload.id'//,

	  // optional, if not defined it will pass the whole event...
	  // payload: 'payload'
	},
	function (evt, vm) {
	  evt.extended = vm.get('myValue');
	  return evt;
	});

	// or

	module.exports = require('cqrs-eventdenormalizer').defineEventExtender({
	  // optional, default is file name without extension,
	  // if name is '' it will handle all events that matches
	  name: 'enteredNewPerson',

	  // optional
	  aggregate: 'person',

	  // optional
	  context: 'hr',

	  // optional, default is 0
	  // if set to -1, it will ignore the version
	  version: 2,

	  // if defined it will load the viewmodel
	  id: 'payload.id'//,

	  // optional, if not defined it will pass the whole event...
	  // payload: 'payload'
	},
	function (evt, vm, callback) {
	  evt.extended = vm.get('myValue');
	  callback(null, evt);
	});
	// optional define a function to that returns an id that will be used as viewmodel id when id not specified in options or found
	//.useAsId(function (evt) {
	//  return 'newId';
	//});
	// or
	//.useAsId(function (evt, callback) {
	//  callback(null, 'newId');
	//});	
	

### not for a collection

	module.exports = require('cqrs-eventdenormalizer').defineEventExtender({
	  // optional, default is file name without extension,
	  // if name is '' it will handle all events that matches
	  name: 'enteredNewPerson',

	  // optional
	  aggregate: 'person',

	  // optional
	  context: 'hr',

	  // optional, default is 0
	  // if set to -1, it will ignore the version
	  version: 2//,

	  // optional, if not defined it will pass the whole event...
	  // payload: 'payload'
	}, function (evt) {
	  evt.extended = true;
	  return evt;
	});

	// or

	module.exports = require('cqrs-eventdenormalizer').defineEventExtender({
	  // optional, default is file name without extension,
	  // if name is '' it will handle all events that matches
	  name: 'enteredNewPerson',

	  // optional
	  aggregate: 'person',

	  // optional
	  context: 'hr',

	  // optional, default is 0
	  // if set to -1, it will ignore the version
	  version: 2//,

	  // optional, if not defined it will pass the whole event...
	  // payload: 'payload'
	}, function (evt, callback) {
	  evt.extended = true;
	  callback(null, evt);
	});


## Replay events

Replay whenever you want...

	denormalizer.replay([/* ordered array of events */], function (err) {
	  if (err) { console.log(err); }
	});

or when catching some events:

	denormalizer.onEventMissing(function (info, evt) {

	  // grab the missing events, depending from info values...
	  // info.aggregateId
	  // info.aggregateRevision
	  // info.aggregate
	  // info.context
	  // info.guardRevision
	  // and call handle...
	  denormalizer.handle(missingEvent, function (err) {
	    if (err) { console.log(err); }
	  });

	});

	you can skip onEventMissing from being called, if provided, by adding the option `skipOnEventMissing` to the denormalizer. Checkout the usage section for more information.

or depending on the last guarded event:

	denormalizer.getLastEvent(function (err, evt) {

	  if (event.occurredAt < Date.now()) {
	  	// ...
	  }

	});

### streamed

	denormalizer.replayStreamed(function (replay, done) {

	  replay(evt1);
	  replay(evt2);
	  replay(evt3);

	  done(function (err) {
	    if (err) { console.log(err); }
	  });

	});

### if you want to clear the readModel before replaying...

	denormalizer.clear(function (err) {
	});

## ES6 default exports
Importing ES6 style default exports is supported for all definitions where you also use `module.exports`:
```
module.exports = defineCollection({...});
```
works as well as 
```
exports.default = defineCollection({...});
```
as well as (must be transpiled by babel or tsc to be runnable in node)
```
export default defineCollection({...});
```

Also: 
```
exports.default = defineViewBuilder({...});
exports.default = defineEventExtender({...});
// etc...
```
Exports other than the default export are then ignored by this package's structure loader.

[Release notes](https://github.com/adrai/node-cqrs-eventdenormalizer/blob/master/releasenotes.md)


# License

Copyright (c) 2019 Adriano Raiano

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
var Denormalizer = require('./lib/denormalizer'),
  _ = require('lodash'),
  fs = require('fs'),
  path = require('path');

function denormalizer (options) {
  return new Denormalizer(options);
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
  denormalizer['define' + nameCap] = function () {
    return construct(require('./lib/definitions/' + name), _.toArray(arguments));
  };
});

module.exports = denormalizer;
```

## File: `licence`
```
Copyright (c) 2019 Adriano Raiano

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
  "name": "cqrs-eventdenormalizer",
  "version": "1.17.1",
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
    "flat": "4.0.0",
    "jsondate": "0.0.1",
    "lodash": "4.17.19",
    "parent-require": "1.0.0",
    "sift": "5.0.0",
    "tolerance": "1.0.0",
    "uuid": "3.1.0",
    "viewmodel": "1.11.1"
  },
  "devDependencies": {
    "aws-sdk": ">=2.104.0",
    "cradle": ">=0.6.7",
    "eslint": ">=1.0.0",
    "expect.js": ">= 0.1.2",
    "mocha": "3.x.x",
    "mongodb": "2.2.x",
    "redis": ">= 0.10.1",
    "tingodb": ">= 0.0.1"
  },
  "description": "Node-cqrs-eventdenormalizer is a node.js module that implements the cqrs pattern. It can be very useful as eventdenormalizer component if you work with (d)ddd, cqrs, domain, host, etc.",
  "keywords": [
    "cqrs",
    "cqs",
    "ddd",
    "dddd",
    "command",
    "event",
    "eventdenormalizer",
    "domain"
  ],
  "homepage": "https://github.com/adrai/node-cqrs-eventdenormalizer",
  "repository": {
    "type": "git",
    "url": "git@github.com:adrai/node-cqrs-eventdenormalizer.git"
  },
  "bugs": {
    "url": "https://github.com/adrai/node-cqrs-eventdenormalizer/issues"
  },
  "licenses": [
    {
      "type": "MIT",
      "url": "https://raw.github.com/adrai/node-cqrs-eventdenormalizer/master/licence"
    }
  ],
  "scripts": {
    "test": "mocha test/unit && mocha test/integration"
  }
}
```

## File: `releasenotes.md`
```markdown
## [v1.17.1](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.17.0...v1.17.1)
- mongodb: useUnifiedTopology

## [v1.17.0](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.16.57...v1.17.0)
- introduce skip steps [#89](https://github.com/adrai/node-cqrs-eventdenormalizer/pull/89) thanks to [Robin Fehr](https://github.com/robinfehr)

## [v1.16.57](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.16.56...v1.16.57)
- skipAfterCommit [#88](https://github.com/adrai/node-cqrs-eventdenormalizer/pull/88) thanks to [Robin Fehr](https://github.com/robinfehr)

## [v1.16.56](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.16.55...v1.16.56)
- refactoring of findViewModel - only one loop [#85](https://github.com/adrai/node-cqrs-eventdenormalizer/pull/85) thanks to [Robin Fehr](https://github.com/robinfehr)

## [v1.16.55](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.16.54...v1.16.55)
- fix edge case during replay whe using query

## [v1.16.54](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.16.52...v1.16.54)
- update viewmodel

## [v1.16.52](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.16.51...v1.16.52)
- isCommandRejected: do not go to revisionStore if evtPayload.reason.aggregateId is not defined

## [v1.16.51](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.16.5...v1.16.51)
- update viewmodel

## [v1.16.5](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.16.4...v1.16.5)
- add shouldHandleEvent option on the viewbuilder

## [v1.16.4](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.16.2...v1.16.4)
- Increase DynamoDB performance [#80](https://github.com/adrai/node-cqrs-eventdenormalizer/pull/80) thanks to [Peter Schramm](https://github.com/Glockenbeat)

## [v1.16.2](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.16.1...v1.16.2)
- Fix preExtendEvent callback errs param in dispatch func [#79](https://github.com/adrai/node-cqrs-eventdenormalizer/pull/79) thanks to [shazichuanshuo](https://github.com/shazichuanshuo)

## [v1.16.1](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.16.0...v1.16.1)
- Allow to set dynamo DB document client options [#77](https://github.com/adrai/node-cqrs-eventdenormalizer/pull/77) thanks to [wrobel](https://github.com/wrobel)

## [v1.16.0](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.15.0...v1.16.0)
- add option to add custom structureLoader implementation

## [v1.15.0](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.14.12...v1.15.0)
- add useAsId methods to ViewModel and EventExtender [#75](https://github.com/adrai/node-cqrs-eventdenormalizer/pull/75) thanks to [nanov](https://github.com/nanov)

## [v1.14.12](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.14.11...v1.14.12)
- update viewmodel

## [v1.14.11](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.14.10...v1.14.11)
- update viewmodel

## [v1.14.10](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.14.9...v1.14.10)
- update viewmodel

## [v1.14.9](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.14.8...v1.14.9)
- replayHandler: make sure to not handle old events (duplicates) by checking the eventId

## [v1.14.8](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.14.7...v1.14.8)
- replayHandler: make sure to not handle old events (duplicates)

## [v1.14.7](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.14.6...v1.14.7)
- update viewmodel

## [v1.14.6](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.14.5...v1.14.6)
- update viewmodel

## [v1.14.5](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.14.4...v1.14.5)
- update viewmodel

## [v1.14.4](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.14.3...v1.14.4)
- update viewmodel

## [v1.14.3](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.14.2...v1.14.3)
- update viewmodel

## [v1.14.2](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.14.1...v1.14.2)
- update viewmodel

## [v1.14.1](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.14.0...v1.14.1)
- update viewmodel

## [v1.14.0](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.13.1...v1.14.0)
- make use of optional bulkCommit for replay

## [v1.13.1](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.13.0...v1.13.1)
- remove deprecated option max_attempts from redis options

## [v1.13.0](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.12.5...v1.13.0)
- compatibility with new mongodb version (3.x)

## [v1.12.5](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.12.4...v1.12.5)
- Fix callback on retry [#65](https://github.com/adrai/node-cqrs-eventdenormalizer/pull/65) thanks to [nanov](https://github.com/nanov)

## [v1.12.4](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.12.3...v1.12.4)
- [optimization] skip to load vm if viewbuilder has not requested it via shouldHandle function

## [v1.12.3](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.12.2...v1.12.3)
- update viewmodel

## [v1.12.2](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.12.1...v1.12.2)
- update viewmodel

## [v1.12.1](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.12.0...v1.12.1)
- fixing dynamodb DocumentClient initialization [#60](https://github.com/adrai/node-cqrs-eventdenormalizer/pull/60) thanks to [Glockenbeat](https://github.com/Glockenbeat)

## [v1.12.0](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.11.0...v1.12.0)
- Support default exports [#58](https://github.com/adrai/node-cqrs-eventdenormalizer/pull/59) thanks to [IRT-fbachmann](https://github.com/IRT-fbachmann)

## [v1.11.0](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.10.5...v1.11.0)
- dynamodb revisionGuardStore implementation [#58](https://github.com/adrai/node-cqrs-eventdenormalizer/pull/58) thanks to [emmkong](https://github.com/emmkong)

## [v1.10.5](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.10.4...v1.10.5)
- update viewmodel

## [v1.10.4](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.10.3...v1.10.4)
- update viewmodel

## [v1.10.3](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.10.2...v1.10.3)
- update viewmodel

## [v1.10.2](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.10.1...v1.10.2)
- Added non-breaking db implementation specific settings support to collection definition. [#56](https://github.com/adrai/node-cqrs-eventdenormalizer/pull/56) thanks to [nanov](https://github.com/nanov) and his company [eCollect](https://github.com/eCollect) which enabled him to work also during working hours

## [v1.10.1](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.10.0...v1.10.1)
- respect preEventExtenders in replayHandler

## [v1.10.0](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.46...v1.10.0)
- introduced preEventExtenders

## [v1.9.46](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.45...v1.9.46)
- optimize handling for commandRejected

## [v1.9.45](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.43...v1.9.45)
- fix for new mongodb driver

## [v1.9.43](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.41...v1.9.43)
- set proper this context

## [v1.9.41](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.40...v1.9.41)
- update deps

## [v1.9.40](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.39...v1.9.40)
- downgrade async to 1.5.2 because of RangeError: Maximum call stack size exceeded when rebuilding a lot of events

## [v1.9.39](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.38...v1.9.39)
- filter falsable notifications

## [v1.9.38](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.37...v1.9.38)
- update viewmodel

## [v1.9.37](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.36...v1.9.37)
- edgecase in revisionGuard

## [v1.9.36](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.35...v1.9.36)
- redis, mongodb: call disconnect on ping error

## [v1.9.35](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.34...v1.9.35)
- Fix events getting lost at high concurrency

## [v1.9.34](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.31...v1.9.34)
- Support mongo connection string

## [v1.9.31](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.30...v1.9.31)
- fix replay race condition when deleting and creating multiple times

## [v1.9.30](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.29...v1.9.30)
- updated viewmodel

## [v1.9.29](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.28...v1.9.29)
- redis, mongodb: call disconnect on ping error

## [v1.9.28](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.26...v1.9.28)
- fix replay race condition when deleting multiple times
- do abort/finish denormalization handling when calling this.retry() wile replaying

## [v1.9.26](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.24...v1.9.26)
- revisionGuard: optional startRevisionNumber

## [v1.9.24](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.23...v1.9.24)
- redis: added optional heartbeat

## [v1.9.23](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.22...v1.9.23)
- updated viewmodel

## [v1.9.22](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.21...v1.9.22)
- if event is not extended return the original event

## [v1.9.21](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.20...v1.9.21)
- revisionGuard fix

## [v1.9.20](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.19...v1.9.20)
- redis: fix for new redis lib

## [v1.9.19](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.18...v1.9.19)
- mongodb: added optional heartbeat

## [v1.9.18](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.15...v1.9.18)
- fix a replay inmemory issue

## [v1.9.15](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.14...v1.9.15)
- update viewmodel

## [v1.9.14](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.12...v1.9.14)
- optimize loader

## [v1.9.12](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.11...v1.9.12)
- collection added loadViewModelIfExists function

## [v1.9.11](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.10...v1.9.11)
- update viewmodel

## [v1.9.10](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.9...v1.9.10)
- optimize handling of guarding the first events

## [v1.9.9](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.8...v1.9.9)
- do not call onAfterCommit during replay

## [v1.9.8](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.7...v1.9.8)
- optimize performance while replaying

## [v1.9.7](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.6...v1.9.7)
- remove trycatch dependency due to memory leaks

## [v1.9.6](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.5...v1.9.6)
- optimize performance while replaying

## [v1.9.5](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.4...v1.9.5)
- fix replay behaviour
- give possibility to use mongodb with authSource

## [v1.9.4](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.3...v1.9.4)
- warn log when async try catch

## [v1.9.3](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.2...v1.9.3)
- update some deps

## [v1.9.2](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.1...v1.9.2)
- fix replay handling when fetching by query

## [v1.9.1](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.9.0...v1.9.1)
- update viewmodel dependency

## [v1.9.0](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.8.5...v1.9.0)
- viewbuilder: introduce onAfterCommit function

## [v1.8.5](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.8.4...v1.8.5)
- fix defaultPayload stuff for viewbuilder

## [v1.8.4](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.8.3...v1.8.4)
- optimization for `npm link`'ed development
- viewbuilder for multiple events [#24](https://github.com/adrai/node-cqrs-eventdenormalizer/issues/24) thanks to [TomKaltz](https://github.com/TomKaltz)

## [v1.8.3](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.8.0...v1.8.3)
- update viewmodel dependency

## [v1.8.0](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.7.12...v1.8.0)
- introduce priority for viewBuilder

## [v1.7.12](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.7.11...v1.7.12)
- do not use defaultPayload of collection for event extenders

## [v1.7.11](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.7.9...v1.7.11)
- catch throwing errors when calling callback

## [v1.7.9](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.7.7...v1.7.9)
- update viewmodel dependency

## [v1.7.7](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.7.6...v1.7.7)
- expose warnings during initialization

## [v1.7.6](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.7.5...v1.7.6)
- better catch for userland errors

## [v1.7.5](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.7.4...v1.7.5)
- fix alreadyInQueue check

## [v1.7.4](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.7.3...v1.7.4)
- update viewmodel dependency

## [v1.7.3](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.7.2...v1.7.3)
- because of shouldHandle, return all possible viewBuilders (not just one)

## [v1.7.2](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.7.1...v1.7.2)
- filter null notifications

## [v1.7.1](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.7.0...v1.7.1)
- fix replay handling caused by introduction of shouldHandle

## [v1.7.0](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.6.0...v1.7.0)
- introduce possibility to define a shouldHandle function

## [v1.6.0](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.5.1...v1.6.0)
- when using revisionGuard, always save the last event
- when using revisionGuard, added possibility to fetch the last denormalized event

## [v1.5.1](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.5.0...v1.5.1)
- little fix

## [v1.5.0](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.4.0...v1.5.0)
- add retry mechanism for viewBuilder

## [v1.4.0](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.3.11...v1.4.0)
- fix revisionGuard when handling duplicate events at the same time

## [v1.3.11](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.3.10...v1.3.11)
- update viewmodel dependency

## [v1.3.10](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.3.9...v1.3.10)
- correct actionOnCommit handling during replay

## [v1.3.9](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.3.8...v1.3.9)
- update viewmodel dependency
- added mongodb driver 2.x support

## [v1.3.8](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.3.7...v1.3.8)
- update viewmodel dependency
- add autoCreate option to view builder thanks to [#9](https://github.com/adrai/node-cqrs-eventdenormalizer/pull/9) thanks to [andywer](https://github.com/andywer)
- added mongodb driver 2.x support

## [v1.3.7](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.3.6...v1.3.7)
- update viewmodel dependency

## [v1.3.6](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.3.2...v1.3.6)
- optimize structureParser

## [v1.3.2](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.3.1...v1.3.2)
- introduce noReplay flag on collection

## [v1.3.1](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.3.0...v1.3.1)
- cloneDeep init values of executeForEach

## [v1.3.0](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.2.5...v1.3.0)
- added executeForEach function for viewBuilders

## [v1.2.5](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.2.4...v1.2.5)
- added payload functionality for eventExtenders

## [v1.2.4](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.2.3...v1.2.4)
- update viewmodel dependency

## [v1.2.3](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.2.1...v1.2.3)
- fix usage with own db implementation

## [v1.2.1](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.2.0...v1.2.1)
- fix revisionGuard in replay

## [v1.2.0](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.1.11...v1.2.0)
- added getInfo function

## [v1.1.11](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.1.10...v1.1.11)
- fix deepClone issue in collection
- added clear function to be used for rebuilding the readmodel

## [v1.1.10](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.1.9...v1.1.10)
- update viewmodel dependency

## [v1.1.9](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.1.8...v1.1.9)
- update viewmodel dependency

## [v1.1.8](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.1.7...v1.1.8)
- prevent events being denormalized out of order during replayStreamed thanks to [#6](https://github.com/adrai/node-cqrs-eventdenormalizer/pull/6) thanks to [andywer](https://github.com/andywer)

## [v1.1.7](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.1.6...v1.1.7)
- added possibility to denormalize multiple viewmodels in same collection with intelligent queries in an async way

## [v1.1.6](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.1.5...v1.1.6)
- added possibility to denormalize multiple viewmodels in same collection with intelligent queries

## [v1.1.5](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.1.4...v1.1.5)
- async viewBuilders

## [v1.1.4](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.1.3...v1.1.4)
- update viewmodel dependency

## [v1.1.3](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.1.2...v1.1.3)
- handle case of same aggregateId in different contexts or aggregates

## [v1.1.2](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.1.1...v1.1.2)
- update viewmodel dependency

## [v1.1.1](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.1.0...v1.1.1)
- little optimization for replay

## [v1.1.0](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.0.10...v1.1.0)
- added possibility to denormalize multiple viewmodels in same collection

## [v1.0.10](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.0.6...v1.0.10)
- fixed replay handling

## [v1.0.6](https://github.com/adrai/node-cqrs-eventdenormalizer/compare/v1.0.4...v1.0.6)
- update viewmodel dependency

## v1.0.4
- handle crappy events with an error

## v1.0.2
- update viewmodel dependency

## v1.0.1
- clone event payload before passing to handle function

## v1.0.0
- refactored whole module
- added possibility to define aggregateId, aggregate and context
- generic message structure for events
- added a lot of tests
- stabilized everything
- optimized performance
- added notification feature
- IMPORTANT: changed API!!!

## v0.4.1
- do not use newer viewmodel version

## v0.4.0
- updated node-queue

## v0.3.6
- make use of viewmodel indexes

## v0.3.5
- emit missingEvent if commandRejected and revision not in sync

## v0.3.4
- handle versioned events

## v0.3.3
- little fix in replay streamed

## v0.3.2
- introduced optional revisionStart (default = 1)

## v0.3.1
- optimized guard for first event for a new denormalized aggregate id

## v0.3.0 (BREAKING CHANGES!!!)
- introduction of revisionGuard
- contextEventDenormalizer is now eventDenormalizer
- eventMissing notification (for atomic replay)
- eventDenormalizer.replay to replay (from scratch)
- eventDenormalizerBase is now viewBuilderBase
- viewBuilderBase new signature (see documentation or tests)

## v0.2.6
- use new concurrency feature of viewmodel

## v0.2.4
- added disableQueuing and ignoreRevision flag
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
    event: {
      correlationId: 'correlationId', // optional
      id: 'id',                       // optional
      name: 'name',                   // optional
//      aggregateId: 'aggregate.id',    // optional
//      context: 'context.name',        // optional
//      aggregate: 'aggregate.name',    // optional
      payload: 'payload'              // optional
//      revision: 'revision'            // optional
//      version: 'version',             // optional
//      meta: 'meta'                    // optional, if defined theses values will be copied to the notification (can be used to transport information like userId, etc..)
    },
    notification: {
      correlationId: 'correlationId',      // optional, the command Id
      id: 'id',                            // optional
      action: 'name',                      // optional
      collection: 'collection',            // optional
      payload: 'payload'                   // optional
//      context: 'meta.context.name',        // optional, if defined theses values will be copied from the event
//      aggregate: 'meta.aggregate.name',    // optional, if defined theses values will be copied from the event
//      aggregateId: 'meta.aggregate.id',    // optional, if defined theses values will be copied from the event
//      revision: 'meta.aggregate.revision', // optional, if defined theses values will be copied from the event
//      eventId: 'meta.event.id',            // optional, if defined theses values will be copied from the event
//      event: 'meta.event.name',            // optional, if defined theses values will be copied from the event
//      meta: 'meta'                         // optional, if defined theses values will be copied from the event (can be used to transport information like userId, etc..)
    }
  };
}

/**
 * Inject definition for notification structure.
 * @param   {Object} definition the definition to be injected
 */
Definition.prototype.defineNotification = function (definition) {
  if (!_.isObject(definition)) {
    throw new Error('Please pass in an object');
  }
  this.definitions.notification = _.defaults(definition, this.definitions.notification);
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

## File: `lib/denormalizer.js`
```javascript
var debug = require('debug')('denormalizer'),
  async = require('async'),
  dotty = require('dotty'),
  util = require('util'),
  EventEmitter = require('events').EventEmitter,
  _ = require('lodash'),
  uuid = require('uuid').v4,
  customLoader = require('./structure/customLoader'),
  structureLoader = require('./structure/structureLoader'),
  attachLookupFunctions = require('./structure/treeExtender'),
  EventDispatcher = require('./eventDispatcher'),
  ReplayHandler = require('./replayHandler'),
  RevisionGuard = require('./revisionGuard'),
  revisionGuardStore = require('./revisionGuardStore'),
  viewmodel = require('viewmodel');

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
 * Denormalizer constructor
 * @param {Object} options The options.
 * @constructor
 */
function Denormalizer(options) {
  EventEmitter.call(this);

  options = options || {};

  if (!options.denormalizerPath) {
    var err = new Error('Please provide denormalizerPath in options');
    debug(err);
    throw err;
  }

  var defaults = {
    retryOnConcurrencyTimeout: 800,
    commandRejectedEventName: 'commandRejected',
    callOnAfterCommitDuringReplay: false,
    skipAfterCommit: false
  };

  _.defaults(options, defaults);

  this.structureLoader = createStructureLoader(options.structureLoader);

  this.repository = viewmodel.write(options.repository);

  var defaultRevOpt = {
    queueTimeout: 1000,
    queueTimeoutMaxLoops: 3//,
    // startRevisionNumber: 1
  };

  options.revisionGuard = options.revisionGuard || {};

  _.defaults(options.revisionGuard, defaultRevOpt);

  this.revisionGuardStore = revisionGuardStore.create(options.revisionGuard);

  this.options = options;

  this.definitions = {
    event: {
      correlationId: 'correlationId', // optional
      id: 'id',                       // optional
      name: 'name',                   // optional
//      aggregateId: 'aggregate.id',    // optional
//      context: 'context.name',        // optional
//      aggregate: 'aggregate.name',    // optional
      payload: 'payload'              // optional
//      revision: 'revision'            // optional
//      version: 'version',             // optional
//      meta: 'meta'                    // optional, if defined theses values will be copied to the notification (can be used to transport information like userId, etc..)
    },
    notification: {
      correlationId: 'correlationId',      // optional, the command Id
      id: 'id',                            // optional
      action: 'name',                      // optional
      collection: 'collection',            // optional
      payload: 'payload'                   // optional
//      context: 'meta.context.name',        // optional, if defined theses values will be copied from the event
//      aggregate: 'meta.aggregate.name',    // optional, if defined theses values will be copied from the event
//      aggregateId: 'meta.aggregate.id',    // optional, if defined theses values will be copied from the event
//      revision: 'meta.aggregate.revision', // optional, if defined theses values will be copied from the event
//      eventId: 'meta.event.id',            // optional, if defined theses values will be copied from the event
//      event: 'meta.event.name',            // optional, if defined theses values will be copied from the event
//      meta: 'meta'                         // optional, if defined theses values will be copied from the event (can be used to transport information like userId, etc..)
    }
  };

  this.idGenerator(function () {
    return uuid().toString();
  });

  this.onEvent(function (evt) {
    debug('emit event:', evt);
  });

  this.onNotification(function (noti) {
    debug('emit notification:', noti);
  });

  this.onEventMissing(function (info, evt) {
    debug('missing events: ', info, evt);
  });

  this.defaultEventExtension(function (evt) {
    return evt;
  });
}

util.inherits(Denormalizer, EventEmitter);

_.extend(Denormalizer.prototype, {

  /**
   * Inject definition for event structure.
   * @param   {Object} definition the definition to be injected
   * @returns {Denormalizer} to be able to chain...
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
   * Inject definition for notification structure.
   * @param   {Object} definition the definition to be injected
   * @returns {Denormalizer} to be able to chain...
   */
  defineNotification: function (definition) {
    if (!definition || !_.isObject(definition)) {
      var err = new Error('Please pass a valid definition!');
      debug(err);
      throw err;
    }

    this.definitions.notification = _.defaults(definition, this.definitions.notification);
    return this;
  },

  /**
   * Inject idGenerator function.
   * @param   {Function}  fn      The function to be injected.
   * @returns {Denormalizer} to be able to chain...
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
   * Inject function for event notification.
   * @param   {Function} fn       the function to be injected
   * @returns {Denormalizer} to be able to chain...
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

    if (this.options.skipOnEvent) {
      fn = function(evt, callback) { callback (null); };
    }

    this.onEventHandle = fn;

    return this;
  },

  /**
   * Inject function for data notification.
   * @param   {Function} fn       the function to be injected
   * @returns {Denormalizer} to be able to chain...
   */
  onNotification: function (fn) {
    if (!fn || !_.isFunction(fn)) {
      var err = new Error('Please pass a valid function!');
      debug(err);
      throw err;
    }

    if (fn.length === 1) {
      fn = _.wrap(fn, function(func, notification, callback) {
        func(notification);
        callback(null);
      });
    }

    if (this.options.skipOnNotification) {
      fn = function(notification, callback) { callback(null); };
    }

    this.onNotificationHandle = fn;

    return this;
  },

  /**
   * Inject function for event missing handle.
   * @param   {Function} fn       the function to be injected
   * @returns {Denormalizer} to be able to chain...
   */
  onEventMissing: function (fn) {
    if (!fn || !_.isFunction(fn)) {
      var err = new Error('Please pass a valid function!');
      debug(err);
      throw err;
    }

    if (this.options.skipOnEventMissing) {
      fn = function(info, evt) {};
    }

    this.onEventMissingHandle = fn;

    return this;
  },

  /**
   * Inject default event extension function.
   * @param   {Function}  fn      The function to be injected.
   * @returns {Denormalizer} to be able to chain...
   */
  defaultEventExtension: function (fn) {
    if (!fn || !_.isFunction(fn)) {
      var err = new Error('Please pass a valid function!');
      debug(err);
      throw err;
    }

    if (fn.length === 1) {
      fn = _.wrap(fn, function(func, evt, callback) {
        callback(null, func(evt));
      });
    }

    // In case we skip the event extenders, we also have to skip the default extender.
    if (this.options.skipExtendEvent) {
      fn = function (evt, callback) { callback(null, evt); };
    }

    this.extendEventHandle = fn;

    return this;
  },

  /**
   * Call this function to initialize the denormalizer.
   * @param {Function} callback the function that will be called when this action has finished [optional]
   *                            `function(err){}`
   */
  init: function (callback) {

    var self = this;

    var warnings = null;

    async.series([
      // load domain files...
      function (callback) {
        debug('load denormalizer files..');
        self.structureLoader(self.options.denormalizerPath, function (err, tree, warns) {
          if (err) {
            return callback(err);
          }
          warnings = warns;
          self.tree = attachLookupFunctions(tree);
          callback(null);
        });
      },

      // prepare infrastructure...
      function (callback) {
        debug('prepare infrastructure...');
        async.parallel([

          // prepare repository...
          function (callback) {
            debug('prepare repository...');

            self.repository.on('connect', function () {
              self.emit('connect');
            });

            self.repository.on('disconnect', function () {
              self.emit('disconnect');
            });

            self.repository.connect(callback);
          },

          // prepare revisionGuard...
          function (callback) {
            debug('prepare revisionGuard...');

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

        self.revisionGuard = new RevisionGuard(self.revisionGuardStore, self.options.revisionGuard);
        self.revisionGuard.onEventMissing(function (info, evt) {
          self.onEventMissingHandle(info, evt);
        });

        self.eventDispatcher = new EventDispatcher(self.tree, self.definitions.event);
        self.tree.defineOptions(self.options)
          .defineEvent(self.definitions.event)
          .defineNotification(self.definitions.notification)
          .idGenerator(self.getNewId)
          .useRepository(self.repository);

        self.revisionGuard.defineEvent(self.definitions.event);

        self.replayHandler = new ReplayHandler(self.eventDispatcher, self.revisionGuardStore, self.definitions.event, self.options);

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
   * Returns the denormalizer information.
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
   * Call this function to extend the passed event.
   * @param {Object}   evt      The event object
   * @param {Function} callback The function that will be called when this action has finished [optional]
   *                            `function(errs, extendedEvent){}`
   */
  extendEvent: function (evt, callback) {
    var self = this;

    var extendedEvent = evt;

    this.extendEventHandle(evt, function (err, extEvt) {
      if (err) {
        debug(err);
      }

      extendedEvent = extEvt || extendedEvent;

      var eventExtender = self.tree.getEventExtender(self.eventDispatcher.getTargetInformation(evt));

      if (!eventExtender || self.options.skipExtendEvent) {
        return callback(err, extendedEvent);
      }

      eventExtender.extend(extendedEvent, function (err, extEvt) {
        if (err) {
          debug(err);
        }
        extendedEvent = extEvt || extendedEvent;
        callback(err, extendedEvent);
      });

    });
  },

  /**
   * Call this function to pre extend the passed event.
   * @param {Object}   evt      The event object
   * @param {Function} callback The function that will be called when this action has finished [optional]
   *                            `function(errs, preExtendedEvent){}`
   */
  preExtendEvent: function (evt, callback) {
    var self = this;

    var extendedEvent = evt;

    var eventExtender = self.tree.getPreEventExtender(self.eventDispatcher.getTargetInformation(evt));

    if (!eventExtender) {
      return callback(null, extendedEvent);
    }

    eventExtender.extend(extendedEvent, function (err, extEvt) {
      if (err) {
        debug(err);
      }
      extendedEvent = extEvt || extendedEvent;
      callback(err, extendedEvent);
    });
  },

  /**
   * Returns true if the passed event is a command rejected event. Callbacks on its own!
   * @param {Object}   evt      The event object
   * @param {Function} callback The function that will be called when this action has finished [optional]
   *                            `function(errs, evt, notifications){}` notifications is of type Array
   * @returns {boolean}
   */
  isCommandRejected: function (evt, callback) {
    if (!evt || !_.isObject(evt)) {
      var err = new Error('Please pass a valid event!');
      debug(err);
      throw err;
    }

    var res = false;

    var self = this;

    var evtName = dotty.get(evt, this.definitions.event.name);
    var evtPayload = dotty.get(evt, this.definitions.event.payload);

    if (evtName === this.options.commandRejectedEventName &&
      evtPayload && evtPayload.reason &&
      evtPayload.reason.name === 'AggregateDestroyedError') {

      res = true;

      var info = {
        aggregateId: evtPayload.reason.aggregateId,
        aggregateRevision: evtPayload.reason.aggregateRevision,
        aggregate: !!this.definitions.event.aggregate ? dotty.get(evt, this.definitions.event.aggregate) : undefined,
        context: !!this.definitions.event.context ? dotty.get(evt, this.definitions.event.context) : undefined
      };

      if (!this.definitions.event.revision || !dotty.exists(evt, this.definitions.event.revision) || !evtPayload.reason.aggregateId || (typeof evtPayload.reason.aggregateId !== 'string' && typeof evtPayload.reason.aggregateId !== 'number')) {
        this.onEventMissingHandle(info, evt);
        if (callback) {
          callback(null, evt, []);
        }
        return res;
      }

      this.revisionGuardStore.get(evtPayload.reason.aggregateId, function (err, rev) {
        if (err) {
          debug(err);
          if (callback) {
            callback([err])
          }
          return;
        }

        debug('revision in store is "' + rev + '" but domain says: "' + evtPayload.reason.aggregateRevision + '"')
        if (rev - 1 < evtPayload.reason.aggregateRevision) {
          info.guardRevision = rev;
          self.onEventMissingHandle(info, evt);
        } else if (rev - 1 > evtPayload.reason.aggregateRevision) {
          debug('strange: revision in store greater than revision in domain, replay?')
        }

        if (callback) {
          callback(null, evt, []);
        }
      });
      return res;
    }

    return res;
  },

  /**
   * Call this function to forward it to the dispatcher.
   * @param {Object}   evt      The event object
   * @param {Function} callback The function that will be called when this action has finished [optional]
   *                            `function(errs, evt, notifications){}` notifications is of type Array
   */
  dispatch: function (evt, callback) {
    var self = this;

    this.preExtendEvent(evt, function (err, preExtEvt) {
      evt = preExtEvt || evt;;

      if (err) {
        debug(err);
        if (callback) callback([err], evt, []);
        return;
      }

      self.eventDispatcher.dispatch(evt, function (errs, notifications) {

        var extendedEvent;

        notifications = notifications || [];

        async.series([

          function (callback) {
            self.extendEvent(evt, function (err, extEvt) {
              extendedEvent = extEvt;
              callback(err);
            });
          },

          function (callback) {
            async.parallel([
              function (callback) {
                async.each(notifications, function (n, callback) {
                  if (self.onNotificationHandle) {
                    debug('publish a notification');
                    self.onNotificationHandle(n, function (err) {
                      if (err) {
                        debug(err);
                      }
                      callback(err);
                    });
                  } else {
                    callback(null);
                  }

                }, callback);
              },

              function (callback) {
                if (self.onEventHandle) {
                  debug('publish an event');
                  self.onEventHandle(extendedEvent, function (err) {
                    if (err) {
                      debug(err);
                    }
                    callback(err);
                  });
                } else {
                  callback(null);
                }
              }
            ], callback);
          }
        ], function (err) {
          if (err) {
            if (!errs) {
              errs = [err];
            } else if (_.isArray(errs)) {
              errs.unshift(err);
            }
            debug(err);
          }
          if (callback) {
            callback(errs, extendedEvent, notifications);
          }
        });
      });
    });
  },

  /**
   * Call this function to let the denormalizer handle it.
   * @param {Object}   evt      The event object
   * @param {Function} callback The function that will be called when this action has finished [optional]
   *                            `function(errs, evt, notifications){}` notifications is of type Array
   */
  handle: function (evt, callback) {
    if (!evt || !_.isObject(evt) || !dotty.exists(evt, this.definitions.event.name)) {
      var err = new Error('Please pass a valid event!');
      debug(err);
      if (callback) callback([err]);
      return;
    }

    var self = this;

    if (this.isCommandRejected(evt, callback)) {
      return;
    }

    var workWithRevisionGuard = false;
    if (!!this.definitions.event.revision && dotty.exists(evt, this.definitions.event.revision) &&
        !!this.definitions.event.aggregateId && dotty.exists(evt, this.definitions.event.aggregateId)) {
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
          try {
            callback([err]);
          } catch (e) {
            debug(e);
            process.emit('uncaughtException', e);
          }
        }
        return;
      }

      self.dispatch(evt, function (errs, extendedEvt, notifications) {
        if (errs) {
          debug(errs);
          if (callback) {
            try {
              callback(errs, extendedEvt, notifications);
            } catch (e) {
              debug(e);
              process.emit('uncaughtException', e);
            }
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
            try {
              callback(errs, extendedEvt, notifications);
            } catch (e) {
              debug(e);
              process.emit('uncaughtException', e);
            }
          }
        });
      });
    });
  },

  /**
   * Replays all passed events.
   * @param {Array}    evts     The passed array of events.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err){}`
   */
  replay: function (evts, callback) {
    this.replayHandler.replay(evts, callback);
  },

  /**
   * Replays in a streamed way.
   * @param {Function} fn The function that will be called with the replay function and the done function.
   *                      `function(replay, done){}`
   */
  replayStreamed: function (fn) {
    this.replayHandler.replayStreamed(fn);
  },

  /**
   * Gets the last event.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err, evt){}` evt is of type Object.
   */
  getLastEvent: function (callback) {
    this.revisionGuardStore.getLastEvent(callback);
  },

  /**
   * Clears all collections and the revisionGuardStore.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err){}`
   */
  clear: function (callback) {
    this.revisionGuard.currentHandlingRevisions = {};
    this.replayHandler.clear(callback);
  }

});

module.exports = Denormalizer;
```

## File: `lib/eventDispatcher.js`
```javascript
var debug = require('debug')('denormalizer:eventDispatcher'),
  _ = require('lodash'),
  async = require('async'),
  dotty = require('dotty');

/**
 * EventDispatcher constructor
 * @param {Object} tree       The tree object.
 * @param {Object} definition The definition object.
 * @constructor
 */
function EventDispatcher (tree, definition) {
  if (!tree || !_.isObject(tree) || !_.isFunction(tree.getViewBuilders)) {
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

  this.definition = {
    correlationId: 'correlationId', // optional
    id: 'id',                       // optional
    name: 'name',                   // optional
//      aggregateId: 'aggregate.id',    // optional
//      context: 'context.name',        // optional
//      aggregate: 'aggregate.name',    // optional
    payload: 'payload'              // optional
//      revision: 'revision'            // optional
//      version: 'version',             // optional
//      meta: 'meta'                    // optional, if defined theses values will be copied to the notification (can be used to transport information like userId, etc..)
  };

  this.definition = _.defaults(definition, this.definition);
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

    var name = dotty.get(evt, this.definition.name) || '';

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
      debug('no context found');
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
   *                            `function(errs, notifications){}`
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

    var viewBuilders = this.tree.getViewBuilders(target);

    var errs = [];
    var notifications = [];

    var foundPrioSet = _.find(viewBuilders, function (vb) {
      return vb.priority < Infinity;
    });

    var eachMethod = 'each';
    if (foundPrioSet) {
      eachMethod = 'eachSeries';
    }

    async[eachMethod].call(async, viewBuilders, function (viewBuilder, callback) {
      viewBuilder.denormalize(evt, function (err, notis) {
        if (err) {
          debug(err);
          if (!errs.push) {
            var warn = new Error('ATTENTION! Already called back!');
            debug(warn);
            console.log(warn.stack);
            return;
          }
          errs.push(err);
        }

        if (notis && notis.length > 0) {
          notifications = notifications.concat(notis);
        }
        callback(null);
      });
    }, function () {
      if (errs.length === 0) {
        errs = null;
      }
      callback(errs, _.filter(notifications, function (n) { return !!n; }));
    });
  }

};

module.exports = EventDispatcher;
```

## File: `lib/orderQueue.js`
```javascript
var debug = require('debug')('denormalizer:orderQueue'),
  _ = require('lodash'),
  AlreadyDenormalizingError = require('./errors/alreadyDenormalizingError');

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
      debug('event already denormalizing [concatenatedId]=' + id + ', [evtId]=' + objId);
      clb(new AlreadyDenormalizingError('Event: [id]=' + objId + ', [evtId]=' + objId + ' already denormalizing!'), function (done) {
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

## File: `lib/replayHandler.js`
```javascript
var debug = require('debug')('denormalizer:replayHandler'),
  _ = require('lodash'),
  async = require('async'),
  dotty = require('dotty');

/**
 * ReplayHandler constructor
 * @param {Object} disp    The dispatcher object.
 * @param {Object} store   The store object.
 * @param {Object} def     The definition object.
 * @param {Object} options The options object.
 * @constructor
 */
function ReplayHandler (disp, store, def, options) {
  this.dispatcher = disp;

  this.store = store;

  def = def || {};

  this.definition = {
    correlationId: 'correlationId', // optional
    id: 'id',                       // optional
    name: 'name',                   // optional
//      aggregateId: 'aggregate.id',    // optional
//      context: 'context.name',        // optional
//      aggregate: 'aggregate.name',    // optional
    payload: 'payload'              // optional
//      revision: 'revision'            // optional
//      version: 'version',             // optional
//      meta: 'meta'                    // optional, if defined theses values will be copied to the notification (can be used to transport information like userId, etc..)
  };

  this.definition = _.defaults(def, this.definition);

  options = options || {};

  this.options = options;
}

ReplayHandler.prototype = {

  /**
   * Clears all collections and the revisionGuardStore.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err){}`
   */
  clear: function (callback) {
    var self = this;
    async.parallel([
      function (callback) {
        async.each(self.dispatcher.tree.getCollections(), function (col, callback) {
          if (col.noReplay) {
            return callback(null);
          }
          col.repository.clear(callback);
        }, callback);
      },
      function (callback) {
        self.store.clear(callback);
      }
    ], callback);
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
   * Updates the revision in the store.
   * @param {Object}   revisionMap The revision map.
   * @param {Function} callback    The function, that will be called when this action is completed.
   *                               `function(err){}`
   */
  updateRevision: function (revisionMap, callback) {
    var self = this;
    var ids = _.keys(revisionMap);
    async.each(ids, function (id, callback) {
      self.store.get(id, function (err, rev) {
        if (err) {
          return callback(err);
        }
        self.store.set(id, revisionMap[id] + 1, rev, callback);
      });
    }, callback);
  },

  /**
   * Replays all passed events.
   * @param {Array}    evts     The passed array of events.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err){}`
   */
  replay: function (evts, callback) {
    this.replayStreamed(function (replay, done) {
      evts.forEach(function (evt) {
        replay(evt);
      });
      done(callback);
    });
  },

  /**
   * Replays in a streamed way.
   * @param {Function} fn The function that will be called with the replay function and the done function.
   *                      `function(replay, done){}`
   */
  replayStreamed: function (fn) {
    var self = this;

    var evtCount = 0;
    var eventQueue = [];
    var eventQueueHandling = false;

    var errs = [];
    var doneCalled = false;
    var doneClb = null;

    var revisionMap = {};
    var collections = {};

    var lastEvent;

    var seenEvents = {};

    var replay = function (evt) {
      var evtId = dotty.get(evt, self.definition.id);
      lastEvent = evt;
      var concatenatedId;
      if (!!self.definition.revision && dotty.exists(evt, self.definition.revision) &&
        !!self.definition.aggregateId && dotty.exists(evt, self.definition.aggregateId)) {
        concatenatedId = self.getConcatenatedId(evt);
        revisionMap[concatenatedId] = dotty.get(evt, self.definition.revision);
      }

      var concatenatedWithEventId = evtId;
      if (concatenatedId) concatenatedWithEventId = concatenatedId + ':' + evtId;
      if (seenEvents[concatenatedWithEventId]) return;
      seenEvents[concatenatedWithEventId] = true;

      var target = self.dispatcher.getTargetInformation(evt);

      var viewBuilders = [], foundPrioSet = false;

      _.each(self.dispatcher.tree.getViewBuilders(target), function (vb) {
        if (!vb.collection.noReplay) {
          viewBuilders.push(vb);

          if (!foundPrioSet && vb.priority < Infinity) {
            foundPrioSet = true;
          }

          if (!collections[vb.collection.workerId]) {
            vb.collection.isReplaying = true;
            collections[vb.collection.workerId] = vb.collection;
          }
        }
      });

      if (foundPrioSet) {
        _.each(viewBuilders, function (vb) {
          eventQueue.push({event: evt, viewBuilders: [vb]});
          evtCount++;
        });
      } else {
        eventQueue.push({event: evt, viewBuilders: viewBuilders});
        evtCount += viewBuilders.length;
      }

      function handleNext () {
        if (evtCount <= 0 && doneCalled) {
          doneLater();
          return;
        }

        if (eventQueue.length > 0) {
          var task = eventQueue.shift();
          var e = task.event, vbs = task.viewBuilders;

          async.series([
            function (clb) {
              var preEventExtender = self.dispatcher.tree.getPreEventExtender(self.dispatcher.getTargetInformation(e));
              if (!preEventExtender) return clb(null);
              preEventExtender.extend(e, function (err, extEvt) {
                if (err) return clb(err);
                e = extEvt || e;
                clb(null);
              });
            },
            function (clb) {
              async.each(vbs, function (vb, callback) {
                vb.denormalize(e, function (err) {
                  --evtCount;
                  if (err) {
                    debug(err);
                    errs.push(err);
                  }

                  callback();
                });
              }, clb);
            }
          ], function () {
            handleNext();
          });
        } else if (eventQueueHandling) {
          eventQueueHandling = false;
        }
      }

      if (!eventQueueHandling) {
        eventQueueHandling = true;
        process.nextTick(handleNext);
      }
    };

    function doneLater() {
      if (doneCalled) {
        done(doneClb);
      }
    }

    var done = function (callback) {
      if (evtCount > 0) {
        doneCalled = true;
        doneClb = callback;
        return;
      }

      async.parallel([
        function (callback) {
          async.each(_.values(collections), function (col, callback) {
            col.saveReplayingVms(callback);
          }, callback);
        },
        function (callback) {
          self.updateRevision(revisionMap, callback);
        },
        function (callback) {
          self.store.saveLastEvent(lastEvent, callback);
        }
      ], function (err) {
        seenEvents = {};

        if (err) {
          debug(err);
          errs.push(err);
        }

        if (errs.length === 0) {
          if (callback) {
            callback(null);
          }
          return;
        }

        if (callback) {
          callback(errs);
        }
      });
    };

    fn(replay, done);
  }

};

module.exports = ReplayHandler;
```

## File: `lib/revisionGuard.js`
```javascript
var debug = require('debug')('denormalizer:revisionGuard'),
  _ = require('lodash'),
  Queue = require('./orderQueue'),
  ConcurrencyError = require('./errors/concurrencyError'),
  AlreadyDenormalizedError = require('./errors/alreadyDenormalizedError'),
  AlreadyDenormalizingError = require('./errors/alreadyDenormalizingError'),
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
        debug('event already denormalized [concatenatedId]=' + concatenatedId + ', [revInStore]=' + revInStore + ', [revInEvt]=' + revInEvt);
        callback(new AlreadyDenormalizedError('Event: [id]=' + dotty.get(evt, self.definition.id) + ', [revision]=' + revInEvt + ', [concatenatedId]=' + concatenatedId + ' already denormalized!'), function (clb) {
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
        debug('event already denormalizing [concatenatedId]=' + concatenatedId + ', [revInStore]=' + revInStore + ', [revInEvt]=' + revInEvt);
        callback(new AlreadyDenormalizingError('Event: [id]=' + dotty.get(evt, self.definition.id) + ', [revision]=' + revInEvt + ', [concatenatedId]=' + concatenatedId + ' already denormalizing!'), function (clb) {
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

## File: `lib/definitions/collection.js`
```javascript
var Definition = require('../definitionBase'),
  util = require('util'),
  _ = require('lodash'),
  uuid = require('uuid').v4,
  async = require('async'),
  viewmodel = require('viewmodel'),
  sift = require('sift'),
  flatten = require('flat'),
  debug = require('debug')('denormalizer:collection');
/**
 * Collection constructor
 * @param {Object} meta            Meta infos like: { name: 'name' }
 * @param {Object} modelInitValues Initialization values for model like: { emails: [] } [optional]
 * @constructor
 */
function Collection (meta, modelInitValues) {
  Definition.call(this, meta);
  // used for replay...
  this.workerId = uuid().toString();
  this.isReplaying = false;
  this.replayingVms = {};
  this.replayingVmsToDelete = {};
  meta = meta || {};
  this.repositorySettings = meta.repositorySettings || {};
  this.defaultPayload = meta.defaultPayload || '';
  this.indexes = meta.indexes || [];
  this.noReplay = !!meta.noReplay || false;
  this.modelInitValues = modelInitValues || {};
  this.viewBuilders = [];
  this.eventExtenders = [];
  this.preEventExtenders = [];
}
util.inherits(Collection, Definition);
_.extend(Collection.prototype, {
  /**
   * Injects the needed repository.
   * @param {Object} repository The repository object to inject.
   */
  useRepository: function (repository) {
    if (!repository || !_.isObject(repository)) {
      var err = new Error('Please pass a valid repository!');
      debug(err);
      throw err;
    }

    var extendObject = {
      collectionName: this.name,
      indexes: this.indexes,
    };

    if (repository.repositoryType && this.repositorySettings[repository.repositoryType]) {
      extendObject.repositorySettings = {};
      extendObject.repositorySettings[repository.repositoryType] = this.repositorySettings[repository.repositoryType];
    }

    this.repository = repository.extend(extendObject);
  },
  /**
   * Add viewBuilder module.
   * @param {ViewBuilder} viewBuilder The viewBuilder module to be injected.
   */
  addViewBuilder: function (viewBuilder) {
    if (!viewBuilder || !_.isObject(viewBuilder)) {
      var err = new Error('Please inject a valid view builder object!');
      debug(err);
      throw err;
    }
    if (viewBuilder.payload === null || viewBuilder.payload === undefined) {
      viewBuilder.payload = this.defaultPayload;
    }
    if (this.viewBuilders.indexOf(viewBuilder) < 0) {
      viewBuilder.useCollection(this);
      this.viewBuilders.push(viewBuilder);
    }
  },
  /**
   * Add eventExtender module.
   * @param {EventExtender} eventExtender The eventExtender module to be injected.
   */
  addEventExtender: function (eventExtender) {
    if (!eventExtender || !_.isObject(eventExtender)) {
      var err = new Error('Please inject a valid event extender object!');
      debug(err);
      throw err;
    }
    if (this.eventExtenders.indexOf(eventExtender) < 0) {
      eventExtender.useCollection(this);
      this.eventExtenders.push(eventExtender);
    }
  },
  /**
   * Add preEventExtender module.
   * @param {PreEventExtender} preEventExtender The preEventExtender module to be injected.
   */
  addPreEventExtender: function (preEventExtender) {
    if (!preEventExtender || !_.isObject(preEventExtender)) {
      var err = new Error('Please inject a valid event extender object!');
      debug(err);
      throw err;
    }
    if (this.preEventExtenders.indexOf(preEventExtender) < 0) {
      preEventExtender.useCollection(this);
      this.preEventExtenders.push(preEventExtender);
    }
  },
  /**
   * Returns the viewBuilder module by query.
   * @param {Object} query The query object. [optional] If not passed, all viewBuilders will be returned.
   * @returns {Array}
   */
  getViewBuilders: function (query) {
    if (!query || !_.isObject(query)) {
      return this.viewBuilders;
    }
    query.name = query.name || '';
    query.version = query.version || 0;
    query.aggregate = query.aggregate || null;
    query.context = query.context || null;
    var found = _.filter(this.viewBuilders, function (vB) {
      return vB.name === query.name &&
            (vB.version === query.version || vB.version === -1) &&
            (vB.aggregate === query.aggregate) &&
            (vB.context === query.context);
    });
    if (found.length !== 0) {
      return found;
    }
    found = _.filter(this.viewBuilders, function (vB) {
      return vB.name === query.name &&
        (vB.version === query.version || vB.version === -1) &&
        (vB.aggregate === query.aggregate) &&
        (vB.context === query.context || !query.context);
    });
    if (found.length !== 0) {
      return found;
    }
    found = _.filter(this.viewBuilders, function (vB) {
      return vB.name === query.name &&
        (vB.version === query.version || vB.version === -1) &&
        (vB.aggregate === query.aggregate || !query.aggregate) &&
        (vB.context === query.context || !query.context);
    });
    if (found.length !== 0) {
      return found;
    }
    return _.filter(this.viewBuilders, function (vB) {
      return vB.name === '' &&
        (vB.version === query.version || vB.version === -1) &&
        (vB.aggregate === query.aggregate || !query.aggregate) &&
        (vB.context === query.context || !query.context);
    });
  },
  /**
   * Returns the eventExtender module by query.
   * @param {Object} query The query object.
   * @returns {EventExtender}
   */
  getEventExtender: function (query) {
    if (!query || !_.isObject(query)) {
      var err = new Error('Please pass a valid query object!');
      debug(err);
      throw err;
    }
    query.name = query.name || '';
    query.version = query.version || 0;
    query.aggregate = query.aggregate || null;
    query.context = query.context || null;
    var found = _.find(this.eventExtenders, function (evExt) {
      return evExt.name === query.name &&
        (evExt.version === query.version || evExt.version === -1) &&
        (evExt.aggregate === query.aggregate) &&
        (evExt.context === query.context);
    });
    if (found) {
      return found;
    }
    found = _.find(this.eventExtenders, function (evExt) {
      return evExt.name === query.name &&
        (evExt.version === query.version || evExt.version === -1) &&
        (evExt.aggregate === query.aggregate || !query.aggregate || !evExt.aggregate) &&
        (evExt.context === query.context);
    });
    if (found) {
      return found;
    }
    found = _.find(this.eventExtenders, function (evExt) {
      return evExt.name === query.name &&
        (evExt.version === query.version || evExt.version === -1) &&
        (evExt.aggregate === query.aggregate || !query.aggregate || !evExt.aggregate) &&
        (evExt.context === query.context || !query.context || !evExt.context);
    });
    if (found) {
      return found;
    }
    return _.find(this.eventExtenders, function (evExt) {
      return evExt.name === '' &&
        (evExt.version === query.version || evExt.version === -1) &&
        (evExt.aggregate === query.aggregate || !query.aggregate || !evExt.aggregate) &&
        (evExt.context === query.context || !query.context || !evExt.context);
    });
  },
  /**
   * Returns the preEventExtender module by query.
   * @param {Object} query The query object.
   * @returns {PreEventExtender}
   */
  getPreEventExtender: function (query) {
    if (!query || !_.isObject(query)) {
      var err = new Error('Please pass a valid query object!');
      debug(err);
      throw err;
    }
    query.name = query.name || '';
    query.version = query.version || 0;
    query.aggregate = query.aggregate || null;
    query.context = query.context || null;
    var found = _.find(this.preEventExtenders, function (evExt) {
      return evExt.name === query.name &&
        (evExt.version === query.version || evExt.version === -1) &&
        (evExt.aggregate === query.aggregate) &&
        (evExt.context === query.context);
    });
    if (found) {
      return found;
    }
    found = _.find(this.preEventExtenders, function (evExt) {
      return evExt.name === query.name &&
        (evExt.version === query.version || evExt.version === -1) &&
        (evExt.aggregate === query.aggregate || !query.aggregate || !evExt.aggregate) &&
        (evExt.context === query.context);
    });
    if (found) {
      return found;
    }
    found = _.find(this.preEventExtenders, function (evExt) {
      return evExt.name === query.name &&
        (evExt.version === query.version || evExt.version === -1) &&
        (evExt.aggregate === query.aggregate || !query.aggregate || !evExt.aggregate) &&
        (evExt.context === query.context || !query.context || !evExt.context);
    });
    if (found) {
      return found;
    }
    return _.find(this.preEventExtenders, function (evExt) {
      return evExt.name === '' &&
        (evExt.version === query.version || evExt.version === -1) &&
        (evExt.aggregate === query.aggregate || !query.aggregate || !evExt.aggregate) &&
        (evExt.context === query.context || !query.context || !evExt.context);
    });
  },
  /**
   * Returns all eventExtender modules.
   * @returns {Array}
   */
  getEventExtenders: function () {
    return this.eventExtenders;
  },
  /**
   * Returns all preEventExtender modules.
   * @returns {Array}
   */
  getPreEventExtenders: function () {
    return this.preEventExtenders;
  },
  /**
   * Use this function to obtain a new id.
   * @param {Function} callback The function, that will be called when the this action is completed.
   *                            `function(err, id){}` id is of type String.
   */
  getNewId: function (callback) {
    this.repository.getNewId(function(err, newId) {
      if (err) {
        debug(err);
        return callback(err);
      }
      callback(null, newId);
    });
  },
  /**
   * Save the passed viewModel object in the read model.
   * @param {Object}   vm       The viewModel object.
   * @param {Function} callback The function, that will be called when the this action is completed. [optional]
   *                            `function(err){}`
   */
  saveViewModel: function (vm, callback) {
    if (this.isReplaying) {
      vm.actionOnCommitForReplay = vm.actionOnCommit;
      // Clone the values to be sure no reference mistakes happen!
      if (vm.attributes) {
        var flatAttr = flatten(vm.attributes);
        var undefines = [];
        _.each(flatAttr, function (v, k) {
          if (v === undefined) {
            undefines.push(k);
          }
        });
        vm.attributes = vm.toJSON();
        _.each(undefines, function (k) {
          vm.set(k, undefined);
        });
      }

      this.replayingVms[vm.id] = vm;
      if (vm.actionOnCommit === 'delete') {
        delete this.replayingVms[vm.id];
        if (!this.replayingVmsToDelete[vm.id]) this.replayingVmsToDelete[vm.id] = vm;
      }
      if (vm.actionOnCommit === 'create') {
        vm.actionOnCommit = 'update';
      }
      return callback(null);
    }
    this.repository.commit(vm, callback);
  },
  /**
   * Loads a viewModel object by id.
   * @param {String}   id       The viewModel id.
   * @param {Function} callback The function, that will be called when the this action is completed.
   *                            `function(err, vm){}` vm is of type Object
   */
  loadViewModel: function (id, callback) {
    if (this.isReplaying) {
      if (this.replayingVms[id]) {
        return callback(null, this.replayingVms[id]);
      }
      if (this.replayingVmsToDelete[id]) {
        var vm = new viewmodel.ViewModel({ id: id }, this.repository);
        var clonedInitValues = _.cloneDeep(this.modelInitValues);
        for (var prop in clonedInitValues) {
          if (!vm.has(prop)) {
            vm.set(prop, clonedInitValues[prop]);
          }
        }
        this.replayingVms[vm.id] = vm;
        return callback(null, this.replayingVms[id]);
      }
    }
    var self = this;
    this.repository.get(id, function(err, vm) {
      if (err) {
        debug(err);
        return callback(err);
      }
      if (!vm) {
        err = new Error('No vm object returned!');
        debug(err);
        return callback(err);
      }
      var clonedInitValues = _.cloneDeep(self.modelInitValues);
      for (var prop in clonedInitValues) {
        if (!vm.has(prop)) {
          vm.set(prop, clonedInitValues[prop]);
        }
      }
      if (self.isReplaying) {
        if (!self.replayingVms[vm.id]) {
          self.replayingVms[vm.id] = vm;
        }
        return callback(null, self.replayingVms[vm.id]);
      }
      callback(null, vm);
    });
  },
  /**
   * Loads a viewModel object by id if exists.
   * @param {String}   id       The viewModel id.
   * @param {Function} callback The function, that will be called when the this action is completed.
   *                            `function(err, vm){}` vm is of type Object or null
   */
  loadViewModelIfExists: function (id, callback) {
    this.loadViewModel(id, function (err, vm) {
      if (err) {
        return callback(err);
      }

      if (!vm || vm.actionOnCommit === 'create') {
        return callback(null, null);
      }

      callback(null, vm);
    });
  },
  /**
   * Loads a viewModel array by optional query and query options.
   * @param {Object}   query        The query to find the viewModels. (mongodb style) [optional]
   * @param {Object}   queryOptions The query options. (mongodb style) [optional]
   * @param {Function} callback     The function, that will be called when the this action is completed.
   *                                `function(err, vms){}` vms is of type Array.
   */
  findViewModels: function (query, queryOptions, callback) {
    if (typeof query === 'function') {
      callback = query;
      query = {};
      queryOptions = {};
    }
    if (typeof queryOptions === 'function') {
      callback = queryOptions;
      queryOptions = {};
    }
    var self = this;

    var localFoundVmsDict = {}; // Dictionary to have O(1) lookups
    var localFoundVms = [];
    if (this.isReplaying) {
      localFoundVms = _.reduce(this.replayingVms, function (result, vm) {
        // if (sift(query, [vm.toJSON()]).length > 0) { // We just read, so this is ok and faster!
        if (sift(query, [vm.attributes]).length > 0) {
          var newLen = result.push(vm);
          localFoundVmsDict[vm.id] = newLen - 1;
        }
        return result;
      }, []);
    }

    this.repository.find(query, queryOptions, function (err, serverVms) {
      if (err) {
        debug(err);
        return callback(err);
      }

      // We will now enhance the local replayingVms whith the results from the server
      // while keeping the local vms if it already exists.
      if (self.isReplaying) {
        // We preffer the local vms but add the server vm if no local available.
        var localAndServerVms = localFoundVms.concat(serverVms);  // The order of this concat matters since we preffer the local ones.
        var resultDict = {}; // Dictionary to have O(1) lookups within the reduce loop.

        var uniqueLocalPrefferedVms = _.reduce(localAndServerVms, function (result, vm) {
          var isDeleted = !!self.replayingVmsToDelete[vm.id];
          var alreadyInResult = !!resultDict[vm.id];
          var localVm = null;
          var resultVm = null;
          if (isDeleted || alreadyInResult) return result;

          // No result found for query wihtin replayingVm since changes have been applied to the
          // replayingVm's already but from the server we retrieve a result.
          if (!localFoundVmsDict[vm.id] && self.replayingVms[vm.id]) {
            localVm = self.replayingVms[vm.id];
          }

          // Preffer local vm if available
          localVm = localVm || localFoundVms[localFoundVmsDict[vm.id]];
          if (localVm) {
            resultVm = localVm;
          } else {
            // Enhance server vm with initial values if not yet available
            var clonedInitValues = _.cloneDeep(self.modelInitValues);
            for (var prop in clonedInitValues) {
              if (!vm.has(prop)) {
                vm.set(prop, clonedInitValues[prop]);
              }
            }
            resultVm = vm;
          }

          result.push(resultVm);
          resultDict[resultVm.id] = true;
          if (!self.replayingVms[vm.id]) {
            self.replayingVms[vm.id] = resultVm;
          }

          return result;
        }, []);

        return callback(null, uniqueLocalPrefferedVms);
      }
      callback(null, serverVms);
    });
  },
  /**
   * Saves all replaying viewmodels.
   * @param {Function} callback The function, that will be called when the this action is completed.
   *                             `function(err){}`
   */
  saveReplayingVms: function (callback) {
    if (!this.isReplaying) {
      var err = new Error('Not in replay mode!');
      debug(err);
      return callback(err);
    }
    var replVms = _.values(this.replayingVms);
    var replVmsToDelete = _.values(this.replayingVmsToDelete);
    var self = this;

    function commit (vm, callback) {
      if (!vm.actionOnCommitForReplay) {
        return callback(null);
      }
      vm.actionOnCommit = vm.actionOnCommitForReplay;
      delete vm.actionOnCommitForReplay;
      self.repository.commit(vm, function (err) {
        if (err) {
          debug(err);
          debug(vm);
        }
        callback(err);
      });
    }

    function prepareVmsForBulkCommit (vms) {
      return _.map(_.filter(vms, function(vm) { return vm.actionOnCommitForReplay; }), function (vm) {
        vm.actionOnCommit = vm.actionOnCommitForReplay;
        delete vm.actionOnCommitForReplay;
        return vm;
      });
    }

    function bulkCommit (vms, callback) {
      if (vms.length === 0) return callback(null);
      self.repository.bulkCommit(prepareVmsForBulkCommit(vms), function (err) {
        if (err) {
          debug(err);
        }
        callback(err);
      });
    }

    async.series([
      function (callback) {
        if (self.repository.bulkCommit) {
          return bulkCommit(replVmsToDelete, callback);
        }
        async.each(replVmsToDelete, commit, callback);
      },
      function (callback) {
        if (self.repository.bulkCommit) {
          return bulkCommit(replVms, callback);
        }
        async.each(replVms, commit, callback);
      }
    ], function (err) {
      if (err) {
        debug(err);
      }
      self.replayingVms = {};
      self.replayingVmsToDelete = {};
      self.isReplaying = false;
      callback(err);
    });
  }
});
module.exports = Collection;
```

## File: `lib/definitions/eventExtender.js`
```javascript
var Definition = require('../definitionBase'),
  util = require('util'),
  _ = require('lodash'),
  dotty = require('dotty'),
  debug = require('debug')('denormalizer:eventExtender');

/**
 * EventExtender constructor
 * @param {Object}             meta     Meta infos like: { name: 'name', version: 1, payload: 'some.path' }
 * @param {Function || String} evtExtFn Function handle
 *                                      `function(evt, col, callback){}`
 * @constructor
 */
function EventExtender (meta, evtExtFn) {
  Definition.call(this, meta);

  meta = meta || {};

  if (!evtExtFn || !(_.isFunction(evtExtFn))) {
    var err = new Error('extender function not injected!');
    debug(err);
    throw err;
  }

  this.version = meta.version || 0;
  this.aggregate = meta.aggregate || null;
  this.context = meta.context || null;
  this.payload = meta.payload || null;
  this.id = meta.id || null;

  this.evtExtFn = evtExtFn;
}

util.inherits(EventExtender, Definition);

_.extend(EventExtender.prototype, {

  /**
   * Injects the needed collection.
   * @param {Object} collection The collection object to inject.
   */
  useCollection: function (collection) {
    if (!collection || !_.isObject(collection)) {
      var err = new Error('Please pass a valid collection!');
      debug(err);
      throw err;
    }

    this.collection = collection;
  },

  /**
   * Loads the appropriate viewmodel by id.
   * @param {String}   id       The viewmodel id.
   * @param {Function} callback The function that will be called when this action has finished
   *                            `function(err, vm){}`
   */
  loadViewModel: function (id, callback) {
    this.collection.loadViewModel(id, callback);
  },

  /**
   * Loads a viewModel array by optional query and query options.
   * @param {Object}   query        The query to find the viewModels. (mongodb style) [optional]
   * @param {Object}   queryOptions The query options. (mongodb style) [optional]
   * @param {Function} callback     The function, that will be called when the this action is completed.
   *                                `function(err, vms){}` vms is of type Array.
   */
  findViewModels: function (query, queryOptions, callback) {
    if (typeof query === 'function') {
      callback = query;
      query = {};
      queryOptions = {};
    }
    if (typeof queryOptions === 'function') {
      callback = queryOptions;
      queryOptions = {};
    }

    this.collection.findViewModels(query, queryOptions, callback);
  },

  /**
   * Extracts the id from the event or generates a new one.
   * @param {Object}   evt      The event object.
   * @param {Function} callback The function that will be called when this action has finished
   *                            `function(err, id){}`
   */
  extractId: function (evt, callback) {
    if (this.id && dotty.exists(evt, this.id)) {
      debug('found viewmodel id in event');
      return callback(null, dotty.get(evt, this.id));
    }

    if (this.getNewIdForThisEventExtender) {
      debug('[' + this.name + '] found eventextender id getter in event');
      return this.getNewIdForThisEventExtender(evt, callback);
    }
    
    debug('not found viewmodel id in event, generate new id');
    this.collection.getNewId(callback);
  },

  /**
   * Extends the event.
   * @param {Object}   evt      The event object.
   * @param {Function} callback The function that will be called when this action has finished
   *                            `function(err, extendedEvent){}`
   */
  extend: function (evt, callback) {
    var self = this;
    var payload = evt;

    if (self.payload && self.payload !== '') {
      payload = dotty.get(evt, self.payload);
    }

    if (self.evtExtFn.length === 3) {
      if (self.id) {
        self.extractId(evt, function (err, id) {
          if (err) {
            debug(err);
            return callback(err);
          }

          self.loadViewModel(id, function (err, vm) {
            if (err) {
              debug(err);
              return callback(err);
            }

            try {
              self.evtExtFn(_.cloneDeep(payload), vm, function () {
                try {
                  callback.apply(this, _.toArray(arguments));
                } catch (e) {
                  debug(e);
                  process.emit('uncaughtException', e);
                }
              });
            } catch (e) {
              debug(e);
              process.emit('uncaughtException', e);
            }
          });
        });
        return;
      }

      try {
        self.evtExtFn(_.cloneDeep(payload), self.collection, function () {
          try {
            callback.apply(this, _.toArray(arguments));
          } catch (e) {
            debug(e);
            process.emit('uncaughtException', e);
          }
        });
      } catch (e) {
        debug(e);
        process.emit('uncaughtException', e);
      }
      return;
    }

    if (self.evtExtFn.length === 1) {
      try {
        var res = self.evtExtFn(evt);
        try {
          callback(null, res);
        } catch (e) {
          debug(e);
          process.emit('uncaughtException', e);
        }
      } catch (e) {
        debug(e);
        process.emit('uncaughtException', e);
      }
      return;
    }

    if (self.evtExtFn.length === 2) {
      if (!self.collection || !self.id) {
        try {
          self.evtExtFn(evt, function () {
            try {
              callback.apply(this, _.toArray(arguments));
            } catch (e) {
              debug(e);
              process.emit('uncaughtException', e);
            }
          });
        } catch (e) {
          debug(e);
          process.emit('uncaughtException', e);
        }
        return;
      }

      self.extractId(evt, function (err, id) {
        if (err) {
          debug(err);
          return callback(err);
        }

        self.loadViewModel(id, function (err, vm) {
          if (err) {
            debug(err);
            return callback(err);
          }

          try {
            var res = self.evtExtFn(_.cloneDeep(payload), vm);
            try {
              callback(null, res);
            } catch (e) {
              debug(e);
              process.emit('uncaughtException', e);
            }
          } catch (e) {
            debug(e);
            process.emit('uncaughtException', e);
          }
        });
      });
    }
  },

  /**
   * Inject idGenerator for eventextender function if no id found.
   * @param   {Function}  fn      The function to be injected.
   * @returns {EventExtender} to be able to chain...
   */
  useAsId: function (fn) {
    if (!fn || !_.isFunction(fn)) {
      var err = new Error('Please pass a valid function!');
      debug(err);
      throw err;
    }


    if (fn.length === 2) {
      this.getNewIdForThisEventExtender = fn;
      return this;
    }

    this.getNewIdForThisEventExtender = function (evt, callback) {
      callback(null, fn(evt));
    };

    return this;
  },
  

});

module.exports = EventExtender;
```

## File: `lib/definitions/preEventExtender.js`
```javascript
var EventExtender = require('./eventExtender'),
  util = require('util'),
  _ = require('lodash');

/**
 * PreEventExtender constructor
 * @param {Object}             meta     Meta infos like: { name: 'name', version: 1, payload: 'some.path' }
 * @param {Function || String} evtExtFn Function handle
 *                                      `function(evt, col, callback){}`
 * @constructor
 */
function PreEventExtender (meta, evtExtFn) {
  EventExtender.call(this, meta, evtExtFn);
}

util.inherits(PreEventExtender, EventExtender);

_.extend(PreEventExtender.prototype, {});

module.exports = PreEventExtender;
```

## File: `lib/definitions/viewBuilder.js`
```javascript
var Definition = require('../definitionBase'),
  util = require('util'),
  _ = require('lodash'),
  async = require('async'),
  dotty = require('dotty'),
  uuid = require('uuid').v4,
  ConcurrencyError = require('viewmodel').ConcurrencyError,
  debug = require('debug')('denormalizer:viewBuilder');

function truthyShouldHandle (evt, vm, clb) {
  clb(null, true);
}

function truthyShouldHandleEvent (evt, clb) {
  clb(null, true);
}

/**
 * ViewBuilder constructor
 * @param {Object}             meta     Meta infos like: { name: 'name', version: 1, payload: 'some.path' }
 * @param {Function || String} denormFn Function handle
 *                                      `function(evtData, vm){}`
 * @constructor
 */
function ViewBuilder (meta, denormFn) {
  Definition.call(this, meta);

  // used for replay...
  this.workerId = uuid().toString();

  meta = meta || {};

  if (!denormFn || (!_.isFunction(denormFn) && !_.isString(denormFn))) {
    var err = new Error('denormalizer function not injected!');
    debug(err);
    throw err;
  }

  if (_.isString(denormFn) && denormFn !== 'update' && denormFn !== 'create' && denormFn !== 'delete') {
    var err = new Error('denormalizer function "' + denormFn + '" not available! Use "create", "update" or "delete"!');
    debug(err);
    throw err;
  }

  this.version = meta.version || 0;
  this.payload = meta.payload === '' ? meta.payload : (meta.payload || null);
  this.aggregate = meta.aggregate || null;
  this.context = meta.context || null;
  this.id = meta.id || null;
  this.query = meta.query || null;
  this.autoCreate = meta.autoCreate === undefined || meta.autoCreate === null ? true : meta.autoCreate;
  this.priority = meta.priority || Infinity;

  if (_.isString(denormFn)) {
    if (denormFn === 'delete') {
      denormFn = function (evtData, vm) {
        vm.destroy();
      };
    } else {
      denormFn = function (evtData, vm) {
        vm.set(evtData);
      };
    }
  }

  this.denormFn = denormFn;

  if (denormFn.length === 2) {
    this.denormFn = function (evtData, vm, clb) {
      denormFn.call(this, evtData, vm);
      if (this.retryCalled) {
        return;
      }
      clb(null);
    };
  }

  var unwrappedDenormFn = this.denormFn;

  this.denormFn = function (evtData, vm, clb) {
    var wrappedCallback = function () {
      try {
        clb.apply(this, _.toArray(arguments));
      } catch (e) {
        debug(e);
        process.emit('uncaughtException', e);
      }
    };

    try {
      unwrappedDenormFn.call(this, evtData, vm, wrappedCallback.bind(this));
    } catch (e) {
      debug(e);
      process.emit('uncaughtException', e);
    }
  };

  this.idGenerator(function () {
    return uuid().toString();
  });

  this.defineShouldHandle(truthyShouldHandle);

  this.defineShouldHandleEvent(truthyShouldHandleEvent);

  this.onAfterCommit(function (evt, vm) {});
}

util.inherits(ViewBuilder, Definition);

/**
 * Returns a random number between passed values of min and max.
 * @param {Number} min The minimum value of the resulting random number.
 * @param {Number} max The maximum value of the resulting random number.
 * @returns {Number}
 */
function randomBetween(min, max) {
  return Math.round(min + Math.random() * (max - min));
}

_.extend(ViewBuilder.prototype, {

  /**
   * Inject idGenerator function.
   * @param   {Function}  fn The function to be injected.
   * @returns {ViewBuilder}  to be able to chain...
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
   * Injects the needed collection.
   * @param {Object} collection The collection object to inject.
   */
  useCollection: function (collection) {
    if (!collection || !_.isObject(collection)) {
      var err = new Error('Please pass a valid collection!');
      debug(err);
      throw err;
    }

    this.collection = collection;
  },

  /**
   * Loads a viewModel object by id.
   * @param {String}   id       The viewModel id.
   * @param {Function} callback The function, that will be called when the this action is completed.
   *                            `function(err, vm){}` vm is of type Object
   */
  loadViewModel: function (id, callback) {
    this.collection.loadViewModel(id, callback);
  },

  /**
   * Save the passed viewModel object in the read model.
   * @param {Object}   vm       The viewModel object.
   * @param {Function} callback The function, that will be called when the this action is completed. [optional]
   *                            `function(err){}`
   */
  saveViewModel: function (vm, callback) {
    this.collection.saveViewModel(vm, callback);
  },

  /**
   * Loads a viewModel array by optional query and query options.
   * @param {Object}   query        The query to find the viewModels. (mongodb style) [optional]
   * @param {Object}   queryOptions The query options. (mongodb style) [optional]
   * @param {Function} callback     The function, that will be called when the this action is completed.
   *                                `function(err, vms){}` vms is of type Array.
   */
  findViewModels: function (query, queryOptions, callback) {
    if (typeof query === 'function') {
      callback = query;
      query = {};
      queryOptions = {};
    }
    if (typeof queryOptions === 'function') {
      callback = queryOptions;
      queryOptions = {};
    }

    this.collection.findViewModels(query, queryOptions, callback);
  },

  /**
   * Extracts the id from the passed event or generates a new one from read model.
   * @param {Object}   evt      The event object.
   * @param {Function} callback The function, that will be called when the this action is completed.
   *                            `function(err, id){}`
   */
  extractId: function (evt, callback) {
    if (this.id && dotty.exists(evt, this.id)) {
      debug('[' + this.name + '] found viewmodel id in event');
      return callback(null, dotty.get(evt, this.id));
    }

    if (this.getNewIdForThisViewBuilder) {
      debug('[' + this.name + '] found viewmodel id getter in event');
      return this.getNewIdForThisViewBuilder(evt, callback);
    }

    debug('[' + this.name + '] not found viewmodel id in event, generate new id');
    this.collection.getNewId(callback);
  },

  /**
   * Generates a notification from event and viewModel.
   * @param {Object} evt The event object.
   * @param {Object} vm  The viewModel.
   * @returns {Object}
   */
  generateNotification: function (evt, vm) {
    var notification = {};

    // event
    if (!!this.definitions.notification.meta && !!this.definitions.event.meta) {
      dotty.put(notification, this.definitions.notification.meta, _.cloneDeep(dotty.get(evt, this.definitions.event.meta)));
    }
    if (!!this.definitions.notification.eventId && !!this.definitions.event.id) {
      dotty.put(notification, this.definitions.notification.eventId, dotty.get(evt, this.definitions.event.id));
    }
    if (!!this.definitions.notification.event && !!this.definitions.event.name) {
      dotty.put(notification, this.definitions.notification.event, dotty.get(evt, this.definitions.event.name));
    }
    if (!!this.definitions.notification.aggregateId && !!this.definitions.event.aggregateId) {
      dotty.put(notification, this.definitions.notification.aggregateId, dotty.get(evt, this.definitions.event.aggregateId));
    }
    if (!!this.definitions.notification.aggregate && !!this.definitions.event.aggregate) {
      dotty.put(notification, this.definitions.notification.aggregate, dotty.get(evt, this.definitions.event.aggregate));
    }
    if (!!this.definitions.notification.context && !!this.definitions.event.context) {
      dotty.put(notification, this.definitions.notification.context, dotty.get(evt, this.definitions.event.context));
    }
    if (!!this.definitions.notification.revision && !!this.definitions.event.revision) {
      dotty.put(notification, this.definitions.notification.revision, dotty.get(evt, this.definitions.event.revision));
    }
    dotty.put(notification, this.definitions.notification.correlationId, dotty.get(evt, this.definitions.event.correlationId));

    // vm
    dotty.put(notification, this.definitions.notification.payload, vm.toJSON());
    dotty.put(notification, this.definitions.notification.collection, this.collection.name);
    dotty.put(notification, this.definitions.notification.action, vm.actionOnCommit);

    return notification;
  },

  /**
   * Handles denormalization for 1 viewmodel.
   * @param {Object}   vm         The viewModel.
   * @param {Object}   evt        The passed event.
   * @param {Object}   initValues The vm init values. [optional]
   * @param {Function} callback   The function, that will be called when this action is completed.
   *                              `function(err, notification){}`
   */
  handleOne: function (vm, evt, initValues, callback) {
    var self = this;

    if (!callback) {
      callback = initValues;
      initValues = null;
    }

    var payload = evt;

    if (this.payload && this.payload !== '') {
      payload = dotty.get(evt, this.payload);
    }

    if (initValues) {
      vm.set(_.cloneDeep(initValues));
    }

    var evtId = dotty.get(evt, this.definitions.event.id);

    var debugOutPut = evtId ? (', [eventId]=' + evtId) : '';
    debug('[' + this.name + ']' + debugOutPut + ' call denormalizer function');

    function retry (retryIn) {
      if (self.collection.isReplaying) {
        var debugMsg = '[' + self.name + ']' + debugOutPut + ' finishing denormalization because is replaying!';
        debug(debugMsg);
        console.log(debugMsg);
        return callback(null);
      }

      if (_.isNumber(retryIn)) {
        retryIn = randomBetween(0, retryIn);
      }

      if (_.isObject(retryIn) && _.isNumber(retryIn.from) && _.isNumber(retryIn.to)) {
        retryIn = randomBetween(retryIn.from, retryIn.to);
      }

      if (!_.isNumber(retryIn) || retryIn === 0) {
        retryIn = randomBetween(0, self.options.retryOnConcurrencyTimeout || 800);
      }

      debug('[' + self.name + ']' + debugOutPut + ' retry in ' + retryIn + 'ms');
      setTimeout(function() {
        self.loadViewModel(vm.id, function (err, vm) {
          if (err) {
            debug(err);
            return callback(err);
          }

          self.handleOne(vm, evt, initValues, callback);
        });
      }, retryIn);
    }

    var shouldBeHandled = function (cb) {
      // if (self.shouldHandleRequestsOnlyEvent) return cb(null, true);
      self.shouldHandle(evt, vm, cb);
    };

    shouldBeHandled(function (err, doHandle) {
      if (err) {
        return callback(err);
      }

      if (!doHandle) {
        return callback(null, null);
      }

      var denormThis = {
        retryCalled: false,

        retry: function () {
          denormThis.retryCalled = true;

          if (arguments.length === 0) {
            return retry();
          }

          if (arguments.length === 1) {
            if (!_.isFunction(arguments[0])) {
              return retry(arguments[0]);
            }
            return retry();
          }

          retry(arguments[0]);
        },

        toRemember: null,

        remindMe: function (memories) {
          denormThis.toRemember = memories;
        },

        getReminder: function (memories) {
          return denormThis.toRemember;
        }
      };

      self.denormFn.call(denormThis, _.cloneDeep(payload), vm, function (err) {
        if (err) {
          debug(err);
          return callback(err);
        }

        var notification = self.generateNotification(evt, vm);

        debug('[' + self.name + ']' + debugOutPut + ' generate new id for notification');
        self.getNewId(function (err, newId) {
          if (err) {
            debug(err);
            return callback(err);
          }

          dotty.put(notification, self.definitions.notification.id, newId);

          self.saveViewModel(vm, function (err) {
            if (err) {
              debug(err);

              if (err instanceof ConcurrencyError) {
                retry(callback);
                return;
              }

              return callback(err);
            }

            if ((!self.options.callOnAfterCommitDuringReplay && self.collection.isReplaying) || self.options.skipAfterCommit) {
              return callback(null, notification);
            }

            self.handleAfterCommit.call(denormThis, evt, vm, function (err) {
              if (err) {
                debug(err);
                return callback(err);
              }
              callback(null, notification);
            });
          });
        });
      });
    });
  },

  /**
   * Handles denormalization with a query instead of an id.
   * @param {Object}   evt      The event object.
   * @param {Object}   query    The query object.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err, notification){}`
   */
  handleQuery: function (evt, query, callback) {
    var self = this;
    this.findViewModels(query, function (err, vms) {
      if (err) {
        debug(err);
        return callback(err);
      }

      async.map(vms, function (vm, callback) {
        self.handleOne(vm, evt, function (err, notification) {
          if (err) {
            debug(err);
            return callback(err);
          }

          callback(null, notification);
        });
      }, function (err, notifications) {
        if (err) {
          debug(err);
          return callback(err);
        }

        notifications = _.filter(notifications, function (n) {
          return !!n;
        });

        callback(null, notifications);
      });
    });
  },

  /**
   * Denormalizes an event for each item passed in executeForEach function.
   * @param {Object}   evt      The passed event.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err, notifications){}`
   */
  denormalizeForEach: function (evt, callback) {
    var self = this;

    this.executeDenormFnForEach(evt, function (err, res) {
      if (err) {
        debug(err);
        return callback(err);
      }

      async.each(res, function (item, callback) {
        if (item.id) {
          return callback(null);
        }
        self.collection.getNewId(function (err, newId) {
          if (err) {
            return callback(err);
          }
          item.id = newId;
          callback(null);
        });
      }, function (err) {
        if (err) {
          debug(err);
          return callback(err);
        }

        async.map(res, function (item, callback) {
          self.loadViewModel(item.id, function (err, vm) {
            if (err) {
              return callback(err);
            }

            self.handleOne(vm, evt, item, function (err, notification) {
              if (err) {
                return callback(err);
              }

              callback(null, notification);
            });
          });
        }, function (err, notis) {
          if (err) {
            debug(err);
            return callback(err);
          }

          callback(null, notis);
        });
      });
    });
  },

  /**
   * Denormalizes an event.
   * @param {Object}   evt      The passed event.
   * @param {Function} callback The function, that will be called when this action is completed.
   *                            `function(err, notifications){}`
   */
  denormalize: function (evt, callback) {
    var self = this;

    function denorm() {
      if (self.executeDenormFnForEach) {
        return self.denormalizeForEach(evt, callback);
      }

      if (self.query) {
        return self.handleQuery(evt, self.query, callback);
      }

      if (!self.query && self.getQueryForThisViewBuilder) {
        self.getQueryForThisViewBuilder(evt, function (err, query) {
          if (err) {
            debug(err);
            return callback(err);
          }
          self.handleQuery(evt, query, callback);
        });
        return;
      }

      self.extractId(evt, function (err, id) {
        if (err) {
          debug(err);
          return callback(err);
        }

        self.loadViewModel(id, function (err, vm) {
          if (err) {
            debug(err);
            return callback(err);
          }

          if (vm.actionOnCommit === 'create' && !self.autoCreate) {
            return callback(null, []);
          }

          self.handleOne(vm, evt, function (err, notification) {
            if (err) {
              debug(err);
              return callback(err);
            }

            var notis = [];
            if (notification) {
              notis.push(notification);
            }

            callback(null, notis);
          });
        });
      });
    }

    // if (this.shouldHandleRequestsOnlyEvent) {
    this.shouldHandleEvent(evt, function (err, doHandle) {
      if (err) {
        return callback(err);
      }

      if (!doHandle) {
        return callback(null, []);
      }

      denorm();
    });
    // } else {
      // denorm();
    // }
  },

  /**
   * Inject idGenerator function if no id found.
   * @param   {Function}  fn      The function to be injected.
   * @returns {ViewBuilder} to be able to chain...
   */
  useAsId: function (fn) {
    if (!fn || !_.isFunction(fn)) {
      var err = new Error('Please pass a valid function!');
      debug(err);
      throw err;
    }


    if (fn.length === 2) {
      this.getNewIdForThisViewBuilder = fn;
      return this;
    }

    this.getNewIdForThisViewBuilder = function (evt, callback) {
      callback(null, fn(evt));
    };

    return this;
  },


  /**
   * Inject useAsQuery function if no query and no id found.
   * @param   {Function}  fn      The function to be injected.
   * @returns {ViewBuilder} to be able to chain...
   */
  useAsQuery: function (fn) {
    if (!fn || !_.isFunction(fn)) {
      var err = new Error('Please pass a valid function!');
      debug(err);
      throw err;
    }

    if (fn.length === 2) {
      this.getQueryForThisViewBuilder = fn;
      return this;
    }

    this.getQueryForThisViewBuilder = function (evt, callback) {
      callback(null, fn(evt));
    };

    var unwrappedFn = this.getQueryForThisViewBuilder;

    this.getQueryForThisViewBuilder = function (evt, clb) {
      var wrappedCallback = function () {
        try {
          clb.apply(this, _.toArray(arguments));
        } catch (e) {
          debug(e);
          process.emit('uncaughtException', e);
        }
      };

      try {
        unwrappedFn.call(this, evt, wrappedCallback);
      } catch (e) {
        debug(e);
        process.emit('uncaughtException', e);
      }
    };

    return this;
  },

  /**
   * Inject executeForEach function that will execute denormFn for all resulting objects.
   * @param   {Function}  fn      The function to be injected.
   * @returns {ViewBuilder} to be able to chain...
   */
  executeForEach: function (fn) {
    if (!fn || !_.isFunction(fn)) {
      var err = new Error('Please pass a valid function!');
      debug(err);
      throw err;
    }

    if (fn.length === 2) {
      this.executeDenormFnForEach = fn;
      return this;
    }

    this.executeDenormFnForEach = function (evt, callback) {
      callback(null, fn(evt));
    };

    var unwrappedFn = this.executeDenormFnForEach;

    this.executeDenormFnForEach = function (evt, clb) {
      var wrappedCallback = function () {
        try {
          clb.apply(this, _.toArray(arguments));
        } catch (e) {
          debug(e);
          process.emit('uncaughtException', e);
        }
      };

      try {
        unwrappedFn.call(this, evt, wrappedCallback);
      } catch (e) {
        debug(e);
        process.emit('uncaughtException', e);
      }
    };

    return this;
  },

  /**
   * Inject shouldHandle function.
   * @param   {Function}  fn      The function to be injected.
   * @returns {ViewBuilder} to be able to chain...
   */
  defineShouldHandle: function (fn) {
    if (!fn || !_.isFunction(fn)) {
      var err = new Error('Please pass a valid function!');
      debug(err);
      throw err;
    }

    // only event
    if (fn.length === 1)
      return this.defineShouldHandleEvent(fn);
    // this.shouldHandleRequestsOnlyEvent = fn.length === 1;

    if (fn.length === 3) {
      this.shouldHandle = fn;
      return this;
    }

    this.shouldHandle = function (evt, vm, callback) {
      callback(null, fn(evt, vm));
    };

    var unwrappedShouldHandle = this.shouldHandle;

    var self = this;

    this.shouldHandle = function (evt, vm, clb) {
      var wrappedCallback = function () {
        try {
          clb.apply(self, _.toArray(arguments));
        } catch (e) {
          debug(e);
          process.emit('uncaughtException', e);
        }
      };

      try {
        unwrappedShouldHandle.call(self, evt, vm, wrappedCallback);
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
   * @returns {SagViewBuildera} to be able to chain...
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
  },

  /**
   * Inject onAfterCommit function.
   * @param   {Function}  fn      The function to be injected.
   * @returns {ViewBuilder} to be able to chain...
   */
  onAfterCommit: function (fn) {
    if (!fn || !_.isFunction(fn)) {
      var err = new Error('Please pass a valid function!');
      debug(err);
      throw err;
    }

    if (fn.length === 3) {
      this.handleAfterCommit = fn;
      return this;
    }

    this.handleAfterCommit = function (evt, vm, callback) {
      callback(null, fn(evt, vm));
    };

    var unwrappedHandleAfterCommit = this.handleAfterCommit;

    this.handleAfterCommit = function (evt, vm, clb) {
      var wrappedCallback = function () {
        try {
          clb.apply(this, _.toArray(arguments));
        } catch (e) {
          debug(e);
          process.emit('uncaughtException', e);
        }
      };

      try {
        unwrappedHandleAfterCommit.call(this, evt, vm, wrappedCallback);
      } catch (e) {
        debug(e);
        process.emit('uncaughtException', e);
      }
    };

    return this;
  }

});

module.exports = ViewBuilder;
```

## File: `lib/errors/alreadyDenormalizedError.js`
```javascript
// Grab the util module that's bundled with Node
var util = require('util');

// Create a new custom Error constructor
function AlreadyDenormalizedError(msg) {
  // Pass the constructor to V8's
  // captureStackTrace to clean up the output
  Error.captureStackTrace(this, AlreadyDenormalizedError);

  // If defined, store a custom error message
  if (msg) {
    this.message = msg;
  }
}

// Extend our custom Error from Error
util.inherits(AlreadyDenormalizedError, Error);

// Give our custom error a name property. Helpful for logging the error later.
AlreadyDenormalizedError.prototype.name = AlreadyDenormalizedError.name;

module.exports = AlreadyDenormalizedError;
```

## File: `lib/errors/alreadyDenormalizingError.js`
```javascript
// Grab the util module that's bundled with Node
var util = require('util');

// Create a new custom Error constructor
function AlreadyDenormalizingError(msg) {
    // Pass the constructor to V8's
    // captureStackTrace to clean up the output
    Error.captureStackTrace(this, AlreadyDenormalizingError);

    // If defined, store a custom error message
    if (msg) {
        this.message = msg;
    }
}

// Extend our custom Error from Error
util.inherits(AlreadyDenormalizingError, Error);

// Give our custom error a name property. Helpful for logging the error later.
AlreadyDenormalizingError.prototype.name = AlreadyDenormalizingError.name;

module.exports = AlreadyDenormalizingError;
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
   *                               `function(err, revision){}` revision is of type Number.
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

## File: `lib/revisionGuardStore/databases/dynamodb.js`
```javascript
var util = require('util'),
  Store = require('../base'),
  debug = require('debug')('denormalizer:revisionGuardStore:dynamodb'),
  ConcurrencyError = require('../../errors/concurrencyError'),
  async = require('async'),
  _ = require('lodash'),
  uuid = require('uuid').v4,
  aws = Store.use('aws-sdk'),
  collections = [];

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
    tableName: 'revision',
    ReadCapacityUnits: 1,
    WriteCapacityUnits: 3
  };

  this.options = _.defaults(this.options, defaults);
  this.store = {};
  this.lastEvent = null;
}
util.inherits(DynamoDB, Store);

_.extend(DynamoDB.prototype, {

  connect: function(callback) {
    var self = this;
    self.client = new aws.DynamoDB(self.options.endpointConf);
    var clientDefaults = { service: self.client }
    var clientOptions = _.defaults(this.options.clientConf, clientDefaults);
    self.documentClient = new aws.DynamoDB.DocumentClient(clientOptions);
    self.isConnected = true;
    self.emit('connect');
    if (callback) callback(null, self);
  },

  disconnect: function(callback) {
    this.emit('disconnect');
    if (callback) callback(null);
  },

  get: function(id, callback) {
    var self = this;

    if (_.isFunction(id)) {
      callback = id;
      id = null;
    } 

    if (!id) {
      id = uuid().toString();
    }
    self.checkConnection(function(err) {
      if (err) {
        return callback(err);
      }

      var params = {
        TableName: self.options.tableName,
        Key: {
          HashKey: id,
          RangeKey: id
        }
      };

      self.documentClient.get(params, function(err, data) {
        if (err) {
          if (callback) callback(err);
          return;
        } else {
          if (!data || !data.Item) {
            return callback(null, null)  ;
          }
          callback(null, data.Item.Revision);
        }
      });
    });
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

    self.checkConnection(function(err) {
      if (err) {
        return callback(err);
      }
      var entity = {
        TableName: self.options.tableName,
        Item: { 
          HashKey: id, 
          RangeKey: id, 
          Revision: revision 
        },
        ConditionExpression: 'attribute_not_exists(HashKey) OR Revision = :oldRevision',
        ExpressionAttributeValues: {
          ':oldRevision': oldRevision
        }
      };
      self.documentClient.put(entity, function(err, data) {
        if (err) {
          if (err.code == 'ConditionalCheckFailedException')
            err = new ConcurrencyError();
          return callback(err);
        }
        return callback(err);
      });
    });
  },

  saveLastEvent: function (evt, callback) {
    var self = this;
    self.checkConnection(function(err) {
      if (err) {
        return callback(err);
      }
      var entity = {
        TableName: self.options.tableName,
        Item: { 
          HashKey: "THE_LAST_SEEN_EVENT", 
          RangeKey: "THE_LAST_SEEN_EVENT", 
          event: evt  
        }
      };

      self.documentClient.put(entity, function(err, data) {
        if (err) {
          if (err.code == 'ConditionalCheckFailedException')
            err = new ConcurrencyError();
          return callback(err);
        }
        return callback(err);
      });
    });
  },

  getLastEvent: function (callback) {
    var self = this;
    self.checkConnection(function(err) {
      if (err) {
        return callback(err);
      }
      var params = {
        TableName: self.options.tableName,
        Key: {
          HashKey: "THE_LAST_SEEN_EVENT",
          RangeKey: "THE_LAST_SEEN_EVENT"
        }
      };

      self.documentClient.get(params, function(err, data) {
        if (err) {
          if (callback) callback(err);
          return;
        } else {
          if (!data || !data.Item) {
            return callback(null, null)  ;
          }
          callback(null, data.Item.event);
        }
      });
    });
  },

  checkConnection: function(callback) {
    var self = this;

    if (collections.indexOf(self.collectionName) >= 0) {
      if (callback) callback(null);
      return;
    }

    createTableIfNotExists(
      self.client, 
      RevisionTableDefinition(self.options.tableName, self.options), 
      function(err){
        if (err) {
          // ignore ResourceInUseException 
          // as there could be multiple requests attempt to create table concurrently
          if (err.code === 'ResourceInUseException') {
            return callback(null);
          }

          return callback(err);
        }

        if (collections.indexOf(self.collectionName) < 0) {
          collections.push(self.collectionName);
        }

        return callback(null);
      }
    );
  },
  clear: function(callback) {
    var self = this;
    self.checkConnection(function(err) {
      if (err) {
        return callback(err);
      }

      var query = {
        TableName: self.options.tableName
      };
      self.documentClient.scan(query, function(err, entities) {
        if (err) {
          return callback(err);
        }
        async.each(
          entities.Items,
          function(entity, callback) {
            var params = {
              TableName: self.options.tableName,
              Key: { HashKey: entity.HashKey, RangeKey: entity.RangeKey }
            };
            self.documentClient.delete(params, function(error, response) {
              callback(error);
            });
          },
          function(error) {
            callback(error);
          }
        );
      });
    });
  }
});

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

function RevisionTableDefinition(tableName, opts) {
  var def = {
    TableName: tableName,
    KeySchema: [
      { AttributeName: 'HashKey', KeyType: 'HASH' },
      { AttributeName: 'RangeKey', KeyType: 'RANGE' }
    ],
    AttributeDefinitions: [
      { AttributeName: 'HashKey', AttributeType: 'S' },
      { AttributeName: 'RangeKey', AttributeType: 'S' }
    ],
    ProvisionedThroughput: {
      ReadCapacityUnits: opts.ReadCapacityUnits,
      WriteCapacityUnits: opts.WriteCapacityUnits
    }
  };

  return def;
}

module.exports = DynamoDB;
```

## File: `lib/revisionGuardStore/databases/inmemory.js`
```javascript
var util = require('util'),
  Store = require('../base'),
  debug = require('debug')('denormalizer:revisionGuardStore:inmemory'),
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
  debug = require('debug')('denormalizer:revisionGuardStore:mongodb'),
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
  debug = require('debug')('denormalizer:revisionGuardStore:redis'),
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
        var userparts = url.auth.split(":");
        options.user = userparts[0];
        if (userparts.length === 2) {
          options.password = userparts[1];
        }
      }
      options.host = url.hostname;
      options.port = url.port;
      if (url.pathname) {
        options.db   = url.pathname.replace("/", "", 1);
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
            return (r !== 'OK' && r !== 1)
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
  debug = require('debug')('denormalizer:revisionGuardStore:tingodb'),
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

## File: `lib/structure/customLoader.js`
```javascript
var definitions = {
  ViewBuilder: require('./../definitions/viewBuilder'),
  EventExtender: require('./../definitions/eventExtender'),
  PreEventExtender: require('./../definitions/preEventExtender'),
  Collection: require('./../definitions/collection')
};

module.exports = function (loader) {
  return function(denormalizerPath, callback) {
    var options = {
      denormalizerPath: denormalizerPath,
      definitions: definitions,
    };

    var tree;
    try {
      var loadedTree = loader(options);
      var tree = {
        generalPreEventExtenders: loadedTree.preEventExtenders || [],
        collections: loadedTree.collections,
        generalEventExtenders: loadedTree.eventExtenders || []
      };
    } catch(e) {
      return callback(e);
    }

    return callback(null, tree);
  }
}
```

## File: `lib/structure/structureLoader.js`
```javascript
var debug = require('debug')('denormalizer:structureLoader'),
  _ = require('lodash'),
  path = require('path'),
  structureParser = require('./structureParser'),
  ViewBuilder = require('./../definitions/viewBuilder'),
  EventExtender = require('./../definitions/eventExtender'),
  PreEventExtender = require('./../definitions/preEventExtender'),
  Collection = require('./../definitions/collection');


function isViewBuilder (item) {
  if (item.fileType !== 'js') {
    return false;
  }

  return item.value instanceof ViewBuilder;
}

function isEventExtender (item) {
  if (item.fileType !== 'js') {
    return false;
  }

  return item.value instanceof EventExtender && !(item.value instanceof PreEventExtender);
}

function isPreEventExtender (item) {
  if (item.fileType !== 'js') {
    return false;
  }

  return item.value instanceof PreEventExtender;
}

function isCollection (item) {
  if (item.fileType !== 'js') {
    return false;
  }

  return item.value instanceof Collection;
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
    viewBuilders: [],
    eventExtenders: [],
    preEventExtenders: [],
    collections: []
  };

  items.forEach(function (item) {
    if (isViewBuilder(item)) {
      debug('found viewBuilder at: ' + item.path);
      defineName(item);
      item.value.name = item.name;
      res.viewBuilders.push(item);
      return;
    }

    if (isEventExtender(item)) {
      debug('found eventExtender at: ' + item.path);
      defineName(item);
      item.value.name = item.name;
      res.eventExtenders.push(item);
      return;
    }

    if (isPreEventExtender(item)) {
      debug('found preEventExtender at: ' + item.path);
      defineName(item);
      item.value.name = item.name;
      res.preEventExtenders.push(item);
      return;
    }

    if (isCollection(item)) {
      debug('found collection at: ' + item.path);
      defineName(item, true);
      item.value.name = item.name;
      res.collections.push(item);
      return;
    }
  });

  return res;
}

function analyze (dir, callback) {
  structureParser(dir, function (items) {
    return _.filter(items, function (i) {
      return isViewBuilder(i) || isEventExtender(i) || isPreEventExtender(i) || isCollection(i);
    });
  }, function (err, items, warns) {
    if (err) {
      return callback(err);
    }

    var res = scan(items);

    callback(null, res, warns);
  });
}

function reorderViewBuilders (obj) {
  obj.viewBuilders.forEach(function (objItem) {
    var foundCol = _.find(obj.collections, function (col) {
      if (objItem.dottiedBase.indexOf('.') >= 0) {
        return objItem.dottiedBase === col.dottiedBase || objItem.dottiedBase.indexOf(col.dottiedBase + '.') === 0;
      } else {
        return objItem.dottiedBase === col.dottiedBase;
      }
    });

    if (!foundCol) {
      return;
    }

    foundCol.value.addViewBuilder(objItem.value);
  });
}

function reorderEventExtenders (obj, ordered) {
  obj.eventExtenders.forEach(function (objItem) {
    var foundCol = _.find(obj.collections, function (col) {
      if (objItem.dottiedBase.indexOf('.') >= 0) {
        return objItem.dottiedBase === col.dottiedBase || objItem.dottiedBase.indexOf(col.dottiedBase + '.') === 0;
      } else {
        return objItem.dottiedBase === col.dottiedBase;
      }
    });

    if (!foundCol) {
      ordered.generalEventExtenders.push(objItem.value);
      return;
    }

    foundCol.value.addEventExtender(objItem.value);
  });
}

function reorderPreEventExtenders (obj, ordered) {
  obj.preEventExtenders.forEach(function (objItem) {
    var foundCol = _.find(obj.collections, function (col) {
      if (objItem.dottiedBase.indexOf('.') >= 0) {
        return objItem.dottiedBase === col.dottiedBase || objItem.dottiedBase.indexOf(col.dottiedBase + '.') === 0;
      } else {
        return objItem.dottiedBase === col.dottiedBase;
      }
    });

    if (!foundCol) {
      ordered.generalPreEventExtenders.push(objItem.value);
      return;
    }

    foundCol.value.addPreEventExtender(objItem.value);
  });
}

function reorder (obj) {
  var ordered = {
    collections: _.map(obj.collections, function (c) { return c.value; }),
    generalEventExtenders: [],
    generalPreEventExtenders: []
  };

  reorderViewBuilders(obj);

  reorderEventExtenders(obj, ordered);

  reorderPreEventExtenders(obj, ordered);

  return ordered;
}

function load (dir, callback) {
  analyze(dir, function (err, dividedByTypes, warns) {
    if (err) {
      return callback(err);
    }

    var structured = reorder(dividedByTypes);

    callback(err, structured, warns);
  });
}

module.exports = load;
```

## File: `lib/structure/structureParser.js`
```javascript
var debug = require('debug')('denormalizer:structureParser'),
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

## File: `lib/structure/treeExtender.js`
```javascript
var debug = require('debug')('denormalizer:treeExtender'),
  _ = require('lodash');

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

      var info = {
        collections: [],
        generalEventExtenders: [],
        generalPreEventExtenders: []
      };

      tree.collections.forEach(function (col) {
        var c = { name: col.name, viewBuilders: [], eventExtenders: [], preEventExtenders: [] };

        col.viewBuilders.forEach(function (vB) {
          c.viewBuilders.push({
            name: vB.name,
            aggregate: vB.aggregate,
            context: vB.context,
            version: vB.version,
            priority: vB.priority
          });
        });

        col.eventExtenders.forEach(function (evtExt) {
          c.eventExtenders.push({
            name: evtExt.name,
            aggregate: evtExt.aggregate,
            context: evtExt.context,
            version: evtExt.version
          });
        });

        col.preEventExtenders.forEach(function (evtExt) {
          c.preEventExtenders.push({
            name: evtExt.name,
            aggregate: evtExt.aggregate,
            context: evtExt.context,
            version: evtExt.version
          });
        });

        info.collections.push(c);
      });

      tree.generalEventExtenders.forEach(function (evtExt) {
        info.generalEventExtenders.push({
          name: evtExt.name,
          aggregate: evtExt.aggregate,
          context: evtExt.context,
          version: evtExt.version
        });
      });

      tree.generalPreEventExtenders.forEach(function (evtExt) {
        info.generalPreEventExtenders.push({
          name: evtExt.name,
          aggregate: evtExt.aggregate,
          context: evtExt.context,
          version: evtExt.version
        });
      });

      return info;
    },

    getViewBuilders: function (query) {
      if (!tree || _.isEmpty(tree)) {
        debug('no tree injected');
        return null;
      }

      var res = [];

      tree.collections.forEach(function (col) {
        var vBs = col.getViewBuilders(query);
        res = res.concat(vBs);
      });

      res = _.sortBy(res, function(vb) {
        return vb.priority;
      });

      return res;
    },

    getCollections: function () {
      if (!tree || _.isEmpty(tree)) {
        debug('no tree injected');
        return null;
      }

      return tree.collections;
    },

    getEventExtender: function (query) {
      if (!tree || _.isEmpty(tree)) {
        debug('no tree injected');
        return null;
      }

      var evtExt;

      for (var i = 0, len = tree.collections.length; i < len; i++) {
        var col = tree.collections[i];
        evtExt = col.getEventExtender(query);
        if (evtExt) {
          return evtExt;
        }
      }

      for (var j = 0, lenJ = tree.generalEventExtenders.length; j < lenJ; j++) {
        evtExt = tree.generalEventExtenders[j];
        if (evtExt &&
            evtExt.name === query.name &&
            (evtExt.version === query.version || evtExt.version === -1) &&
            (evtExt.aggregate === query.aggregate || !query.aggregate || ! evtExt.aggregate) &&
            (evtExt.context === query.context || !query.context || ! evtExt.context)) {
          return evtExt;
        }
      }

      for (var k = 0, lenK = tree.generalEventExtenders.length; k < lenK; k++) {
        evtExt = tree.generalEventExtenders[k];
        if (evtExt &&
            evtExt.name === '' &&
            (evtExt.version === query.version || evtExt.version === -1) &&
            (evtExt.aggregate === query.aggregate || !query.aggregate || ! evtExt.aggregate) &&
            (evtExt.context === query.context)) {
          return evtExt;
        }
      }

      for (var l = 0, lenL = tree.generalEventExtenders.length; l < lenL; l++) {
        evtExt = tree.generalEventExtenders[l];
        if (evtExt &&
          evtExt.name === '' &&
          (evtExt.version === query.version || evtExt.version === -1) &&
          (evtExt.aggregate === query.aggregate || !query.aggregate || ! evtExt.aggregate) &&
          (evtExt.context === query.context || !query.context || ! evtExt.context)) {
          return evtExt;
        }
      }

      return null;
    },

    getPreEventExtender: function (query) {
      if (!tree || _.isEmpty(tree)) {
        debug('no tree injected');
        return null;
      }

      var evtExt;

      for (var i = 0, len = tree.collections.length; i < len; i++) {
        var col = tree.collections[i];
        evtExt = col.getPreEventExtender(query);
        if (evtExt) {
          return evtExt;
        }
      }

      for (var j = 0, lenJ = tree.generalPreEventExtenders.length; j < lenJ; j++) {
        evtExt = tree.generalPreEventExtenders[j];
        if (evtExt &&
            evtExt.name === query.name &&
            (evtExt.version === query.version || evtExt.version === -1) &&
            (evtExt.aggregate === query.aggregate || !query.aggregate || ! evtExt.aggregate) &&
            (evtExt.context === query.context || !query.context || ! evtExt.context)) {
          return evtExt;
        }
      }

      for (var k = 0, lenK = tree.generalPreEventExtenders.length; k < lenK; k++) {
        evtExt = tree.generalPreEventExtenders[k];
        if (evtExt &&
            evtExt.name === '' &&
            (evtExt.version === query.version || evtExt.version === -1) &&
            (evtExt.aggregate === query.aggregate || !query.aggregate || ! evtExt.aggregate) &&
            (evtExt.context === query.context)) {
          return evtExt;
        }
      }

      for (var l = 0, lenL = tree.generalPreEventExtenders.length; l < lenL; l++) {
        evtExt = tree.generalPreEventExtenders[l];
        if (evtExt &&
          evtExt.name === '' &&
          (evtExt.version === query.version || evtExt.version === -1) &&
          (evtExt.aggregate === query.aggregate || !query.aggregate || ! evtExt.aggregate) &&
          (evtExt.context === query.context || !query.context || ! evtExt.context)) {
          return evtExt;
        }
      }

      return null;
    },

    defineOptions: function (options) {
      if (!tree || _.isEmpty(tree)) {
        debug('no tree injected');
        return this;
      }

      tree.collections.forEach(function (col) {
        col.defineOptions(options);

        col.getViewBuilders().forEach(function (vB) {
          vB.defineOptions(options);
        });

        col.getEventExtenders().forEach(function (eExt) {
          eExt.defineOptions(options);
        });

        col.getPreEventExtenders().forEach(function (eExt) {
          eExt.defineOptions(options);
        });
      });

      tree.generalEventExtenders.forEach(function (eExt) {
        eExt.defineOptions(options);
      });

      tree.generalPreEventExtenders.forEach(function (eExt) {
        eExt.defineOptions(options);
      });

      return this;
    },

    defineNotification: function (definition) {
      if (!tree || _.isEmpty(tree)) {
        debug('no tree injected');
        return this;
      }

      tree.collections.forEach(function (col) {
        col.defineNotification(definition);

        col.getViewBuilders().forEach(function (vB) {
          vB.defineNotification(definition);
        });

        col.getEventExtenders().forEach(function (eExt) {
          eExt.defineNotification(definition);
        });

        col.getPreEventExtenders().forEach(function (eExt) {
          eExt.defineNotification(definition);
        });
      });

      tree.generalEventExtenders.forEach(function (eExt) {
        eExt.defineNotification(definition);
      });

      tree.generalPreEventExtenders.forEach(function (eExt) {
        eExt.defineNotification(definition);
      });

      return this;
    },

    defineEvent: function (definition) {
      if (!tree || _.isEmpty(tree)) {
        debug('no tree injected');
        return this;
      }

      tree.collections.forEach(function (col) {
        col.defineEvent(definition);

        col.getViewBuilders().forEach(function (vB) {
          vB.defineEvent(definition);
        });

        col.getEventExtenders().forEach(function (eExt) {
          eExt.defineEvent(definition);
        });

        col.getPreEventExtenders().forEach(function (eExt) {
          eExt.defineEvent(definition);
        });
      });

      tree.generalEventExtenders.forEach(function (eExt) {
        eExt.defineEvent(definition);
      });

      tree.generalPreEventExtenders.forEach(function (eExt) {
        eExt.defineEvent(definition);
      });
      return this;
    },

    useRepository: function (repository) {
      if (!tree || _.isEmpty(tree)) {
        debug('no tree injected');
        return this;
      }

      tree.collections.forEach(function (col) {
        col.useRepository(repository);
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

      tree.collections.forEach(function (col) {
        col.getViewBuilders().forEach(function (vB) {
          vB.idGenerator(getNewId);
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
-R spec -t 6000
```

## File: `test/integration/integrationTest.js`
```javascript
var expect = require('expect.js'),
  _ = require('lodash'),
  api = require('../../index');

describe('integration', function () {

  describe('format 1', function () {

    var denorm;

    before(function (done) {
      denorm = api({ denormalizerPath: __dirname + '/fixture/set1', commandRejectedEventName: 'rejectedCommand', revisionGuard: { queueTimeout: 200, queueTimeoutMaxLoops: 2 } });
      denorm.defineEvent({
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

      denorm.defineNotification({
        id: 'id',
        action: 'name',
        collection: 'collection',
        payload: 'payload',
        context: 'meta.context.name',
        aggregate: 'meta.aggregate.name',
        aggregateId: 'meta.aggregate.id',
        revision: 'meta.aggregate.revision',
        eventId: 'meta.event.id',
        event: 'meta.event.name',
        meta: 'meta'
      });

      denorm.defaultEventExtension(function (evt) {
        evt.defForAllExt = true;
        return evt;
      });

      expect(function () {
        denorm.getInfo();
      }).to.throwError('/init');

      denorm.init(function (err, warns) {
        expect(warns).not.to.be.ok();
        done(err);
      });
    });

    describe('requesting information', function () {

      it('it should return the expected information', function () {

        function expectInNamedArray(col, name, test) {
          var obj = _.find(col, function(v) { return v.name === name; });
          expect(obj).to.be.an('object');
          test(obj);
        }

        var info = denorm.getInfo();
        expect(info.collections.length).to.eql(2);

        var found = _.find(info.collections, function (col) {
          return col.name === 'person';
        });

        var viewBuilders = found.viewBuilders;

        expect(found.name).to.eql('person');
        expect(viewBuilders.length).to.eql(3);

        expectInNamedArray(viewBuilders, 'enteredNewPerson', function(vb) {
          expect(vb.name).to.eql('enteredNewPerson');
          expect(vb.aggregate).to.eql('person');
          expect(vb.context).to.eql('hr');
          expect(vb.version).to.eql(2);
        });

        expectInNamedArray(viewBuilders, 'personLeaved', function(vb) {
          expect(vb.aggregate).to.eql('person');
          expect(vb.context).to.eql('hr');
          expect(vb.version).to.eql(0);
        });

        expectInNamedArray(viewBuilders, 'registeredEMailAddress', function(vb) {
          expect(vb.aggregate).to.eql('person');
          expect(vb.context).to.eql('hr');
          expect(vb.version).to.eql(2);
        });

        expect(found.eventExtenders.length).to.eql(1);
        expect(found.eventExtenders[0].name).to.eql('enteredNewPerson');
        expect(found.eventExtenders[0].aggregate).to.eql('person');
        expect(found.eventExtenders[0].context).to.eql('hr');
        expect(found.eventExtenders[0].version).to.eql(2);
        expect(found.preEventExtenders.length).to.eql(1);
        expect(found.preEventExtenders[0].name).to.eql('enteredNewPerson');
        expect(found.preEventExtenders[0].aggregate).to.eql('person');
        expect(found.preEventExtenders[0].context).to.eql('hr');
        expect(found.preEventExtenders[0].version).to.eql(2);

        var found = _.find(info.collections, function (col) {
          return col.name === 'personDetail';
        });
        expect(found.name).to.eql('personDetail');
        expect(found.viewBuilders.length).to.eql(4);
        expect(found.viewBuilders[1].name).to.eql('enteredNewPerson');
        expect(found.viewBuilders[1].aggregate).to.eql('person');
        expect(found.viewBuilders[1].context).to.eql('hr');
        expect(found.viewBuilders[1].version).to.eql(2);
        expect(found.viewBuilders[3].name).to.eql('registeredEMailAddress');
        expect(found.viewBuilders[3].aggregate).to.eql('person');
        expect(found.viewBuilders[3].context).to.eql('hr');
        expect(found.viewBuilders[3].version).to.eql(2);
        expect(found.eventExtenders.length).to.eql(0);
        expect(found.preEventExtenders.length).to.eql(0);

        expect(info.generalEventExtenders.length).to.eql(1);
        expect(info.generalEventExtenders[0].name).to.eql('');
        expect(info.generalEventExtenders[0].aggregate).to.eql(null);
        expect(info.generalEventExtenders[0].context).to.eql(null);
        expect(info.generalEventExtenders[0].version).to.eql(-1);

        expect(info.generalPreEventExtenders.length).to.eql(0);

      });

    });

    describe('handling an event that is not a json object', function () {

      it('it should not publish any notification and it should callback with an error and without event', function (done) {

        var publishedEvents = [];
        denorm.onEvent(function (evt) {
          publishedEvents.push(evt);
        });

        var publishedNotis = [];
        denorm.onNotification(function (noti) {
          publishedNotis.push(noti);
        });

        denorm.handle('crappy', function (errs, e, notis) {
          expect(errs).to.be.ok();
          expect(errs.length).to.eql(1);
          expect(errs[0].message).to.match(/valid/i);
          expect(e).not.to.be.ok();
          expect(notis).not.to.be.ok();

          expect(publishedEvents.length).to.eql(0);
          expect(publishedNotis.length).to.eql(0);

          done();
        });

      });

    });

    describe('handling an event that has no name', function () {

      it('it should not publish any notification and it should callback with an error and without event', function (done) {

        var publishedEvents = [];
        denorm.onEvent(function (evt) {
          publishedEvents.push(evt);
        });

        var publishedNotis = [];
        denorm.onNotification(function (noti) {
          publishedNotis.push(noti);
        });

        var evt = {
          correlationId: 'cmdId',
          id: 'evtId',
//          name: 'evtName',
          aggregate: {
            id: 'aggregateId',
            name: 'aggregate'
          },
          context: {
            name: 'context'
          },
          payload: 'payload',
          revision: 1,
          version: 0,
          meta: {
            userId: 'userId'
          }
        };

        denorm.handle(evt, function (errs, e, notis) {
          expect(errs).to.be.ok();
          expect(errs.length).to.eql(1);
          expect(errs[0].message).to.match(/valid/i);
          expect(e).not.to.be.ok();
          expect(notis).not.to.be.ok();

          expect(publishedEvents.length).to.eql(0);
          expect(publishedNotis.length).to.eql(0);

          done();
        });

      });

    });

    describe('handling an event that will not be handled by any viewBuilder or any specific eventExtender', function () {

      it('it should not publish any notification and it should callback without an error but with same event', function (done) {

        var publishedEvents = [];
        denorm.onEvent(function (evt) {
          publishedEvents.push(evt);
        });

        var publishedNotis = [];
        denorm.onNotification(function (noti) {
          publishedNotis.push(noti);
        });

        var evt = {
          correlationId: 'cmdId',
          id: 'evtId',
          name: 'evtName',
          aggregate: {
            id: 'aggregateId',
            name: 'aggregate'
          },
          context: {
            name: 'context'
          },
          payload: 'payload',
          revision: 1,
          version: 0,
          meta: {
            userId: 'userId'
          }
        };

        denorm.handle(evt, function (err, e, notis) {
          expect(err).not.to.be.ok();
          expect(e).to.eql(evt);
          expect(e.defForAllExt).to.eql(true);
          expect(e.extended).not.to.be.ok();
          expect(e.extendedDefault).to.eql(true);
          expect(notis).to.be.an('array');
          expect(notis.length).to.eql(0);

          expect(publishedEvents.length).to.eql(1);
          expect(publishedEvents[0]).to.eql(evt);
          expect(publishedEvents[0].defForAllExt).to.eql(true);
          expect(publishedEvents[0].extended).not.to.be.ok();
          expect(publishedEvents[0].extendedDefault).to.eql(true);
          expect(publishedNotis.length).to.eql(0);

          done();
        });

      });

    });

    describe('handling an event that will be handled by 2 viewBuilders and a specific eventExtender', function () {

      it('it should publish 2 notifications and it should callback without an error but with an extended event', function (done) {

        var publishedEvents = [];
        denorm.onEvent(function (evt) {
          publishedEvents.push(evt);
        });

        var publishedNotis = [];
        denorm.onNotification(function (noti) {
          publishedNotis.push(noti);
        });

        var evt = {
          id: 'evtId',
          correlationId: 'cmdId',
          name: 'enteredNewPerson',
          aggregate: {
            id: '1234',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            firstname: 'Jack',
            lastname: 'Joe',
            email: 'a@b.c'
          },
          revision: 1,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        denorm.handle(evt, function (errs, e, notis) {
          expect(errs).not.to.be.ok();
          for (var m in evt) {
            expect(e[m]).to.eql(evt[m]);
          }
          expect(e.defForAllExt).to.eql(true);
          expect(e.extended).to.eql(true);
          expect(e.extendedDefault).not.to.be.ok();
          expect(notis).to.be.an('array');
          expect(notis.length).to.eql(2);

          var personIndex = 0;
          var personDetailIndex = 1;
          if (notis[0].collection !== 'person') {
            personIndex = 1;
            personDetailIndex = 0;
          }

          expect(notis[personIndex].name).to.eql('create');
          expect(notis[personIndex].collection).to.eql('person');
          expect(notis[personIndex].payload.id).to.eql('1234');
          expect(notis[personIndex].payload.firstname).to.eql('Jack');
          expect(notis[personIndex].payload.lastname).to.eql('Joe');
          expect(notis[personIndex].payload.email).not.to.be.ok();
          expect(notis[personIndex].id).to.be.a('string');
          expect(notis[personIndex].correlationId).to.eql('cmdId');
          expect(notis[personIndex].meta.event.id).to.eql('evtId');
          expect(notis[personIndex].meta.event.name).to.eql('enteredNewPerson');
          expect(notis[personIndex].meta.userId).to.eql('userId');
          expect(notis[personIndex].meta.aggregate.id).to.eql('1234');
          expect(notis[personIndex].meta.aggregate.name).to.eql('person');
          expect(notis[personIndex].meta.aggregate.revision).to.eql(1);
          expect(notis[personIndex].meta.context.name).to.eql('hr');
          expect(notis[personDetailIndex].name).to.eql('create');
          expect(notis[personDetailIndex].collection).to.eql('personDetail');
          expect(notis[personDetailIndex].payload.id).to.eql('1234');
          expect(notis[personDetailIndex].payload.firstname).to.eql('Jack');
          expect(notis[personDetailIndex].payload.lastname).to.eql('Joe');
          expect(notis[personDetailIndex].payload.email).to.eql('a@b.c');
          expect(notis[personDetailIndex].id).to.be.a('string');
          expect(notis[personDetailIndex].correlationId).to.eql('cmdId');
          expect(notis[personDetailIndex].meta.event.id).to.eql('evtId');
          expect(notis[personDetailIndex].meta.event.name).to.eql('enteredNewPerson');
          expect(notis[personDetailIndex].meta.userId).to.eql('userId');
          expect(notis[personDetailIndex].meta.aggregate.id).to.eql('1234');
          expect(notis[personDetailIndex].meta.aggregate.name).to.eql('person');
          expect(notis[personDetailIndex].meta.aggregate.revision).to.eql(1);
          expect(notis[personDetailIndex].meta.context.name).to.eql('hr');

          expect(publishedEvents.length).to.eql(1);
          for (var m in evt) {
            expect(publishedEvents[0][m]).to.eql(evt[m]);
          }
          expect(publishedEvents[0].defForAllExt).to.eql(true);
          expect(publishedEvents[0].extended).to.eql(true);
          expect(publishedEvents[0].extendedDefault).not.to.be.ok();
          expect(publishedNotis.length).to.eql(2);
          expect(publishedNotis[personIndex].name).to.eql('create');
          expect(publishedNotis[personIndex].collection).to.eql('person');
          expect(publishedNotis[personIndex].payload.id).to.eql('1234');
          expect(publishedNotis[personIndex].payload.firstname).to.eql('Jack');
          expect(publishedNotis[personIndex].payload.lastname).to.eql('Joe');
          expect(publishedNotis[personIndex].payload.email).not.to.be.ok();
          expect(publishedNotis[personIndex].id).to.be.a('string');
          expect(publishedNotis[personIndex].correlationId).to.eql('cmdId');
          expect(publishedNotis[personIndex].meta.event.id).to.eql('evtId');
          expect(publishedNotis[personIndex].meta.event.name).to.eql('enteredNewPerson');
          expect(publishedNotis[personIndex].meta.userId).to.eql('userId');
          expect(publishedNotis[personIndex].meta.aggregate.id).to.eql('1234');
          expect(publishedNotis[personIndex].meta.aggregate.name).to.eql('person');
          expect(publishedNotis[personIndex].meta.aggregate.revision).to.eql(1);
          expect(publishedNotis[personIndex].meta.context.name).to.eql('hr');
          expect(publishedNotis[personDetailIndex].name).to.eql('create');
          expect(publishedNotis[personDetailIndex].collection).to.eql('personDetail');
          expect(publishedNotis[personDetailIndex].payload.id).to.eql('1234');
          expect(publishedNotis[personDetailIndex].payload.firstname).to.eql('Jack');
          expect(publishedNotis[personDetailIndex].payload.lastname).to.eql('Joe');
          expect(publishedNotis[personDetailIndex].payload.email).to.eql('a@b.c');
          expect(publishedNotis[personDetailIndex].id).to.be.a('string');
          expect(publishedNotis[personDetailIndex].correlationId).to.eql('cmdId');
          expect(publishedNotis[personDetailIndex].meta.event.id).to.eql('evtId');
          expect(publishedNotis[personDetailIndex].meta.event.name).to.eql('enteredNewPerson');
          expect(publishedNotis[personDetailIndex].meta.userId).to.eql('userId');
          expect(publishedNotis[personDetailIndex].meta.aggregate.id).to.eql('1234');
          expect(publishedNotis[personDetailIndex].meta.aggregate.name).to.eql('person');
          expect(publishedNotis[personDetailIndex].meta.aggregate.revision).to.eql(1);
          expect(publishedNotis[personDetailIndex].meta.context.name).to.eql('hr');

          done();
        });

      });

    });

    describe('handling an event that will be handled by 2 viewBuilder and a generic eventExtender', function () {

      it('it should publish 2 notification and it should callback without an error but with an extended event', function (done) {

        var publishedEvents = [];
        denorm.onEvent(function (evt) {
          publishedEvents.push(evt);
        });

        var publishedNotis = [];
        denorm.onNotification(function (noti) {
          publishedNotis.push(noti);
        });

        var evt = {
          id: 'evtId',
          correlationId: 'cmdId',
          name: 'registeredEMailAddress',
          aggregate: {
            id: '1234',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            email: 'xyz@r.f'
          },
          revision: 2,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        denorm.handle(evt, function (errs, e, notis) {
          expect(errs).not.to.be.ok();
          expect(e).to.eql(evt);
          expect(e.defForAllExt).to.eql(true);
          expect(e.extended).not.to.be.ok();
          expect(e.extendedDefault).to.eql(true);
          expect(notis).to.be.an('array');
          expect(notis.length).to.eql(2);
          expect(notis[0].name).to.eql('update');
          expect(notis[0].collection).to.eql('person');
          expect(notis[0].payload.id).to.eql('1234');
          expect(notis[0].payload.firstname).to.eql('Jack');
          expect(notis[0].payload.lastname).to.eql('Joe');
          expect(notis[0].payload.email).not.to.be.ok();
          expect(notis[0].payload.generalEmail).to.eql('xyz@r.f');
          expect(notis[0].id).to.be.a('string');
          expect(notis[0].correlationId).to.eql('cmdId');
          expect(notis[0].meta.event.id).to.eql('evtId');
          expect(notis[0].meta.event.name).to.eql('registeredEMailAddress');
          expect(notis[0].meta.userId).to.eql('userId');
          expect(notis[0].meta.aggregate.id).to.eql('1234');
          expect(notis[0].meta.aggregate.name).to.eql('person');
          expect(notis[0].meta.aggregate.revision).to.eql(2);
          expect(notis[0].meta.context.name).to.eql('hr');
          expect(notis[1].name).to.eql('update');
          expect(notis[1].collection).to.eql('personDetail');
          expect(notis[1].payload.id).to.eql('1234');
          expect(notis[1].payload.firstname).to.eql('Jack');
          expect(notis[1].payload.lastname).to.eql('Joe');
          expect(notis[1].payload.email).to.eql('xyz@r.f');
          expect(notis[1].id).to.be.a('string');
          expect(notis[1].correlationId).to.eql('cmdId');
          expect(notis[1].meta.event.id).to.eql('evtId');
          expect(notis[1].meta.event.name).to.eql('registeredEMailAddress');
          expect(notis[1].meta.userId).to.eql('userId');
          expect(notis[1].meta.aggregate.id).to.eql('1234');
          expect(notis[1].meta.aggregate.name).to.eql('person');
          expect(notis[1].meta.aggregate.revision).to.eql(2);
          expect(notis[1].meta.context.name).to.eql('hr');

          expect(publishedEvents.length).to.eql(1);
          expect(publishedEvents[0]).to.eql(evt);
          expect(publishedEvents[0].defForAllExt).to.eql(true);
          expect(publishedEvents[0].extended).not.to.be.ok();
          expect(publishedEvents[0].extendedDefault).to.eql(true);
          expect(publishedNotis.length).to.eql(2);
          expect(publishedNotis[0].name).to.eql('update');
          expect(publishedNotis[0].collection).to.eql('person');
          expect(publishedNotis[0].payload.id).to.eql('1234');
          expect(publishedNotis[0].payload.firstname).to.eql('Jack');
          expect(publishedNotis[0].payload.lastname).to.eql('Joe');
          expect(publishedNotis[0].payload.email).not.to.be.ok();
          expect(publishedNotis[0].payload.generalEmail).to.eql('xyz@r.f');
          expect(publishedNotis[0].id).to.be.a('string');
          expect(publishedNotis[0].correlationId).to.eql('cmdId');
          expect(publishedNotis[0].meta.event.id).to.eql('evtId');
          expect(publishedNotis[0].meta.event.name).to.eql('registeredEMailAddress');
          expect(publishedNotis[0].meta.userId).to.eql('userId');
          expect(publishedNotis[0].meta.aggregate.id).to.eql('1234');
          expect(publishedNotis[0].meta.aggregate.name).to.eql('person');
          expect(publishedNotis[0].meta.aggregate.revision).to.eql(2);
          expect(publishedNotis[0].meta.context.name).to.eql('hr');
          expect(publishedNotis[1].name).to.eql('update');
          expect(publishedNotis[1].collection).to.eql('personDetail');
          expect(publishedNotis[1].payload.id).to.eql('1234');
          expect(publishedNotis[1].payload.firstname).to.eql('Jack');
          expect(publishedNotis[1].payload.lastname).to.eql('Joe');
          expect(publishedNotis[1].payload.email).to.eql('xyz@r.f');
          expect(publishedNotis[1].id).to.be.a('string');
          expect(publishedNotis[1].correlationId).to.eql('cmdId');
          expect(publishedNotis[1].meta.event.id).to.eql('evtId');
          expect(publishedNotis[1].meta.event.name).to.eql('registeredEMailAddress');
          expect(publishedNotis[1].meta.userId).to.eql('userId');
          expect(publishedNotis[1].meta.aggregate.id).to.eql('1234');
          expect(publishedNotis[1].meta.aggregate.name).to.eql('person');
          expect(publishedNotis[1].meta.aggregate.revision).to.eql(2);
          expect(publishedNotis[1].meta.context.name).to.eql('hr');

          done();
        });

      });

    });

    describe('handling an event that will be handled by 2 viewBuilder and a generic eventExtender and a generic preEventExtender', function () {

      it('it should publish 2 notification and it should callback without an error but with an extended event', function (done) {

        var publishedEvents = [];
        denorm.onEvent(function (evt) {
          publishedEvents.push(evt);
        });

        var publishedNotis = [];
        denorm.onNotification(function (noti) {
          publishedNotis.push(noti);
        });

        var evt = {
          id: 'evtIdaranew',
          correlationId: 'cmdId',
          name: 'enteredNewPerson',
          aggregate: {
            id: '12345678aranew',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            firstname: 'Jack',
            lastname: 'Joe',
            email: 'a@b.c'
          },
          revision: 1,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        denorm.handle(evt, function (errs, e, notis) {
          expect(errs).not.to.be.ok();
          for (var m in evt) {
            expect(e[m]).to.eql(evt[m]);
          }
          expect(e.defForAllExt).to.eql(true);
          expect(e.extended).to.eql(true);
          expect(e.preExtended).to.eql(true);
          expect(notis).to.be.an('array');
          expect(notis.length).to.eql(2);
          expect(notis[0].name).to.eql('create');
          expect(notis[0].collection).to.eql('person');
          expect(notis[0].payload.id).to.eql('12345678aranew');
          expect(notis[0].payload.firstname).to.eql('Jack');
          expect(notis[0].payload.lastname).to.eql('Joe');
          expect(notis[0].payload.email).not.to.be.ok();
          expect(notis[0].id).to.be.a('string');
          expect(notis[0].correlationId).to.eql('cmdId');
          expect(notis[0].meta.event.id).to.eql('evtIdaranew');
          expect(notis[0].meta.event.name).to.eql('enteredNewPerson');
          expect(notis[0].meta.userId).to.eql('userId');
          expect(notis[0].meta.aggregate.id).to.eql('12345678aranew');
          expect(notis[0].meta.aggregate.name).to.eql('person');
          expect(notis[0].meta.aggregate.revision).to.eql(1);
          expect(notis[0].meta.context.name).to.eql('hr');
          expect(notis[1].name).to.eql('create');
          expect(notis[1].collection).to.eql('personDetail');
          expect(notis[1].payload.id).to.eql('12345678aranew');
          expect(notis[1].payload.firstname).to.eql('Jack');
          expect(notis[1].payload.lastname).to.eql('Joe');
          expect(notis[1].payload.email).to.eql('a@b.c');
          expect(notis[1].id).to.be.a('string');
          expect(notis[1].correlationId).to.eql('cmdId');
          expect(notis[1].meta.event.id).to.eql('evtIdaranew');
          expect(notis[1].meta.event.name).to.eql('enteredNewPerson');
          expect(notis[1].meta.userId).to.eql('userId');
          expect(notis[1].meta.aggregate.id).to.eql('12345678aranew');
          expect(notis[1].meta.aggregate.name).to.eql('person');
          expect(notis[1].meta.aggregate.revision).to.eql(1);
          expect(notis[1].meta.context.name).to.eql('hr');

          expect(publishedEvents.length).to.eql(1);
          for (var m in evt) {
            expect(publishedEvents[0][m]).to.eql(evt[m]);
          }
          expect(publishedEvents[0].defForAllExt).to.eql(true);
          expect(publishedEvents[0].extended).to.eql(true);
          expect(publishedEvents[0].preExtended).to.eql(true);
          expect(publishedNotis.length).to.eql(2);
          expect(publishedNotis[0].name).to.eql('create');
          expect(publishedNotis[0].collection).to.eql('person');
          expect(publishedNotis[0].payload.id).to.eql('12345678aranew');
          expect(publishedNotis[0].payload.firstname).to.eql('Jack');
          expect(publishedNotis[0].payload.lastname).to.eql('Joe');
          expect(publishedNotis[0].payload.email).not.to.be.ok();
          expect(publishedNotis[0].payload.wasExtendedByPreExtender).to.eql(true);
          expect(publishedNotis[0].id).to.be.a('string');
          expect(publishedNotis[0].correlationId).to.eql('cmdId');
          expect(publishedNotis[0].meta.event.id).to.eql('evtIdaranew');
          expect(publishedNotis[0].meta.event.name).to.eql('enteredNewPerson');
          expect(publishedNotis[0].meta.userId).to.eql('userId');
          expect(publishedNotis[0].meta.aggregate.id).to.eql('12345678aranew');
          expect(publishedNotis[0].meta.aggregate.name).to.eql('person');
          expect(publishedNotis[0].meta.aggregate.revision).to.eql(1);
          expect(publishedNotis[0].meta.context.name).to.eql('hr');
          expect(publishedNotis[1].name).to.eql('create');
          expect(publishedNotis[1].collection).to.eql('personDetail');
          expect(publishedNotis[1].payload.id).to.eql('12345678aranew');
          expect(publishedNotis[1].payload.firstname).to.eql('Jack');
          expect(publishedNotis[1].payload.lastname).to.eql('Joe');
          expect(publishedNotis[1].payload.email).to.eql('a@b.c');
          expect(publishedNotis[1].payload.wasExtendedByPreExtender).not.to.be.ok();
          expect(publishedNotis[1].id).to.be.a('string');
          expect(publishedNotis[1].correlationId).to.eql('cmdId');
          expect(publishedNotis[1].meta.event.id).to.eql('evtIdaranew');
          expect(publishedNotis[1].meta.event.name).to.eql('enteredNewPerson');
          expect(publishedNotis[1].meta.userId).to.eql('userId');
          expect(publishedNotis[1].meta.aggregate.id).to.eql('12345678aranew');
          expect(publishedNotis[1].meta.aggregate.name).to.eql('person');
          expect(publishedNotis[1].meta.aggregate.revision).to.eql(1);
          expect(publishedNotis[1].meta.context.name).to.eql('hr');

          done();
        });

      });

    });

    describe('handling an event that will be handled by 2 viewBuilder and a generic eventExtender', function () {

      it('it should publish 3 notification and it should callback without an error but with an extended event', function (done) {

        var publishedEvents = [];
        denorm.onEvent(function (evt) {
          publishedEvents.push(evt);
        });

        var publishedNotis = [];
        denorm.onNotification(function (noti) {
          publishedNotis.push(noti);
        });

        var evt = {
          id: 'evtId',
          correlationId: 'cmdId',
          name: 'registeredEMailAddress',
          aggregate: {
            id: '1234'
//            name: 'person'
          },
          context: {
//            name: 'hr'
          },
          payload: {
            email: 'abc@d.e'
          },
          revision: 3,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        denorm.handle(evt, function (errs, e, notis) {
          expect(errs).not.to.be.ok();
          expect(e).to.eql(evt);
          expect(e.defForAllExt).to.eql(true);
          expect(e.extended).not.to.be.ok();
          expect(e.extendedDefault).to.eql(true);
          expect(notis).to.be.an('array');
          expect(notis.length).to.eql(3);
          expect(notis[0].name).to.eql('update');
          expect(notis[0].collection).to.eql('person');
          expect(notis[0].payload.id).to.eql('1234');
          expect(notis[0].payload.firstname).to.eql('Jack');
          expect(notis[0].payload.lastname).to.eql('Joe');
          expect(notis[0].payload.email).not.to.be.ok();
          expect(notis[0].payload.generalEmail).to.eql('abc@d.e');
          expect(notis[0].id).to.be.a('string');
          expect(notis[0].correlationId).to.eql('cmdId');
          expect(notis[0].meta.event.id).to.eql('evtId');
          expect(notis[0].meta.event.name).to.eql('registeredEMailAddress');
          expect(notis[0].meta.userId).to.eql('userId');
          expect(notis[0].meta.aggregate.id).to.eql('1234');
          expect(notis[0].meta.aggregate.name).not.to.be.ok();
          expect(notis[0].meta.aggregate.revision).to.eql(3);
          expect(notis[0].meta.context.name).not.to.be.ok();
          expect(notis[1].name).to.eql('update');
          expect(notis[1].collection).to.eql('person');
          expect(notis[1].payload.id).to.eql('12345678aranew');
          expect(notis[1].payload.firstname).to.eql('Jack');
          expect(notis[1].payload.lastname).to.eql('Joe');
          expect(notis[1].payload.email).not.to.be.ok();
          expect(notis[1].payload.generalEmail).to.eql('abc@d.e');
          expect(notis[1].id).to.be.a('string');
          expect(notis[1].correlationId).to.eql('cmdId');
          expect(notis[1].meta.event.id).to.eql('evtId');
          expect(notis[1].meta.event.name).to.eql('registeredEMailAddress');
          expect(notis[1].meta.userId).to.eql('userId');
          expect(notis[1].meta.aggregate.id).to.eql('1234');
          expect(notis[1].meta.aggregate.name).not.to.be.ok();
          expect(notis[1].meta.aggregate.revision).to.eql(3);
          expect(notis[1].meta.context.name).not.to.be.ok();
          expect(notis[2].name).to.eql('update');
          expect(notis[2].collection).to.eql('personDetail');
          expect(notis[2].payload.id).to.eql('1234');
          expect(notis[2].payload.firstname).to.eql('Jack');
          expect(notis[2].payload.lastname).to.eql('Joe');
          expect(notis[2].payload.email).to.eql('abc@d.e');
          expect(notis[2].id).to.be.a('string');
          expect(notis[2].correlationId).to.eql('cmdId');
          expect(notis[2].meta.event.id).to.eql('evtId');
          expect(notis[2].meta.event.name).to.eql('registeredEMailAddress');
          expect(notis[2].meta.userId).to.eql('userId');
          expect(notis[2].meta.aggregate.id).to.eql('1234');
          expect(notis[2].meta.aggregate.name).not.to.be.ok();
          expect(notis[2].meta.aggregate.revision).to.eql(3);
          expect(notis[2].meta.context.name).not.to.be.ok();

          expect(publishedEvents.length).to.eql(1);
          expect(publishedEvents[0]).to.eql(evt);
          expect(publishedEvents[0].defForAllExt).to.eql(true);
          expect(publishedEvents[0].extended).not.to.be.ok();
          expect(publishedEvents[0].extendedDefault).to.eql(true);
          expect(publishedNotis.length).to.eql(3);
          expect(publishedNotis[0].name).to.eql('update');
          expect(publishedNotis[0].collection).to.eql('person');
          expect(publishedNotis[0].payload.id).to.eql('1234');
          expect(publishedNotis[0].payload.firstname).to.eql('Jack');
          expect(publishedNotis[0].payload.lastname).to.eql('Joe');
          expect(publishedNotis[0].payload.email).not.to.be.ok();
          expect(publishedNotis[0].payload.generalEmail).to.eql('abc@d.e');
          expect(publishedNotis[0].id).to.be.a('string');
          expect(publishedNotis[0].correlationId).to.eql('cmdId');
          expect(publishedNotis[0].meta.event.id).to.eql('evtId');
          expect(publishedNotis[0].meta.event.name).to.eql('registeredEMailAddress');
          expect(publishedNotis[0].meta.userId).to.eql('userId');
          expect(publishedNotis[0].meta.aggregate.id).to.eql('1234');
          expect(publishedNotis[0].meta.aggregate.name).not.to.be.ok();
          expect(publishedNotis[0].meta.aggregate.revision).to.eql(3);
          expect(publishedNotis[0].meta.context.name).not.to.be.ok();
          expect(publishedNotis[1].name).to.eql('update');
          expect(publishedNotis[1].collection).to.eql('person');
          expect(publishedNotis[1].payload.id).to.eql('12345678aranew');
          expect(publishedNotis[1].payload.firstname).to.eql('Jack');
          expect(publishedNotis[1].payload.lastname).to.eql('Joe');
          expect(publishedNotis[1].payload.email).not.to.be.ok();
          expect(publishedNotis[1].payload.generalEmail).to.eql('abc@d.e');
          expect(publishedNotis[1].id).to.be.a('string');
          expect(publishedNotis[1].correlationId).to.eql('cmdId');
          expect(publishedNotis[1].meta.event.id).to.eql('evtId');
          expect(publishedNotis[1].meta.event.name).to.eql('registeredEMailAddress');
          expect(publishedNotis[1].meta.userId).to.eql('userId');
          expect(publishedNotis[1].meta.aggregate.id).to.eql('1234');
          expect(publishedNotis[1].meta.aggregate.name).not.to.be.ok();
          expect(publishedNotis[1].meta.aggregate.revision).to.eql(3);
          expect(publishedNotis[1].meta.context.name).not.to.be.ok();
          expect(publishedNotis[2].name).to.eql('update');
          expect(publishedNotis[2].collection).to.eql('personDetail');
          expect(publishedNotis[2].payload.id).to.eql('1234');
          expect(publishedNotis[2].payload.firstname).to.eql('Jack');
          expect(publishedNotis[2].payload.lastname).to.eql('Joe');
          expect(publishedNotis[2].payload.email).to.eql('abc@d.e');
          expect(publishedNotis[2].id).to.be.a('string');
          expect(publishedNotis[2].correlationId).to.eql('cmdId');
          expect(publishedNotis[2].meta.event.id).to.eql('evtId');
          expect(publishedNotis[2].meta.event.name).to.eql('registeredEMailAddress');
          expect(publishedNotis[2].meta.userId).to.eql('userId');
          expect(publishedNotis[2].meta.aggregate.id).to.eql('1234');
          expect(publishedNotis[2].meta.aggregate.name).not.to.be.ok();
          expect(publishedNotis[2].meta.aggregate.revision).to.eql(3);
          expect(publishedNotis[2].meta.context.name).not.to.be.ok();

          done();
        });

      });

    });

    describe('handling an event that was already handled', function () {

      it('it should not publish anything and callback with an error', function (done) {

        var publishedEvents = [];
        denorm.onEvent(function (evt) {
          publishedEvents.push(evt);
        });

        var publishedNotis = [];
        denorm.onNotification(function (noti) {
          publishedNotis.push(noti);
        });

        var evt = {
          id: 'evtId',
          correlationId: 'cmdId',
          name: 'registeredEMailAddress',
          aggregate: {
            id: '1234'//,
            //name: 'person'
          },
          context: {
            //name: 'hr'
          },
          payload: {
            email: 'abc@d.e'
          },
          revision: 3,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        denorm.handle(evt, function (errs, e, notis) {
          expect(errs).to.be.ok();
          expect(errs.length).to.eql(1);
          expect(errs[0].name).to.eql('AlreadyDenormalizedError');
          expect(e).not.to.be.ok();
          expect(notis).not.to.be.ok();

          expect(publishedEvents.length).to.eql(0);
          expect(publishedNotis.length).to.eql(0);

          done();
        });

      });

    });

    describe('handling an event that has a bigger revision than expected', function () {

      it('it should fire an eventMissing event', function (done) {

        var publishedEvents = [];
        denorm.onEvent(function (evt) {
          publishedEvents.push(evt);
        });

        var publishedNotis = [];
        denorm.onNotification(function (noti) {
          publishedNotis.push(noti);
        });

        var evt = {
          id: 'evtId',
          correlationId: 'cmdId',
          name: 'registeredEMailAddress',
          aggregate: {
            id: '1234',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            email: 'abc@d.e'
          },
          revision: 7,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        denorm.onEventMissing(function (info, e) {
          expect(info.aggregate).to.eql('person');
          expect(info.aggregateId).to.eql('1234');
          expect(info.context).to.eql('hr');
          expect(info.aggregateRevision).to.eql(7);
          expect(info.guardRevision).to.eql(3);
          expect(e).to.eql(evt);

          expect(publishedEvents.length).to.eql(0);
          expect(publishedNotis.length).to.eql(0);

          done();
        });

        denorm.handle(evt, function (errs, e, notis) {});

      });

    });

    describe('handling an command rejected event', function () {

      it('it should work as expected', function (done) {

        var publishedEvents = [];
        denorm.onEvent(function (evt) {
          publishedEvents.push(evt);
        });

        var publishedNotis = [];
        denorm.onNotification(function (noti) {
          publishedNotis.push(noti);
        });

        var evt = {
          id: 'evtId',
          correlationId: 'cmdId',
          name: 'rejectedCommand',
          aggregate: {
            id: '1234',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            reason: {
              name: 'AggregateDestroyedError',
              aggregateId: '1234',
              aggregateRevision: 6
            }
          },
          revision: 6,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        var eventMissingCalled = false;
        denorm.onEventMissing(function (info, e) {
          expect(info.aggregate).to.eql('person');
          expect(info.aggregateId).to.eql('1234');
          expect(info.context).to.eql('hr');
          expect(info.aggregateRevision).to.eql(6);
          expect(info.guardRevision).to.eql(4);
          expect(e).to.eql(evt);
          eventMissingCalled = true;
        });

        denorm.handle(evt, function (errs, e, notis) {
          expect(errs).not.to.be.ok();
          expect(e).to.eql(evt);
          expect(notis.length).to.eql(0);

          expect(publishedEvents.length).to.eql(0);
          expect(publishedNotis.length).to.eql(0);

          expect(eventMissingCalled).to.eql(true);

          done();
        });

      });

    });

    describe('handling some events multiple times', function () {

      before(function (done) {
        denorm.clear(done);
      });

      it('it should work as expected', function (done) {

        var publishedEvents = [];
        denorm.onEvent(function (evt) {
          publishedEvents.push(evt);
        });

        var publishedNotis = [];
        denorm.onNotification(function (noti) {
          publishedNotis.push(noti);
        });

        var evt1 = {
          id: 'evtIdb',
          correlationId: 'cmdIdb',
          name: 'enteredNewPerson',
          aggregate: {
            id: '12345678b',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            firstname: 'Jack',
            lastname: 'Joe',
            email: 'a@b.c'
          },
          revision: 1,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        var evt2 = {
          id: 'evtId2b',
          correlationId: 'cmdId2b',
          name: 'registeredEMailAddress',
          aggregate: {
            id: '12345678b',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            email: 'd@e.f'
          },
          revision: 2,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        var evt3 = {
          id: 'evtId3b',
          correlationId: 'cmdId3b',
          name: 'registeredEMailAddress',
          aggregate: {
            id: '12345678b',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            email: 'g@h.i'
          },
          revision: 3,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        var evt4 = {
          id: 'evtId4b',
          correlationId: 'cmdId4b',
          name: 'registeredEMailAddress',
          aggregate: {
            id: '12345678b',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            email: 'g@h.i'
          },
          revision: 4,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        denorm.handle(evt1, function (errs, e, notis) {
          var count = 1;

          function check () {
            count++;

            if (count >= 10) {
              denorm.getLastEvent(function (err, evt) {
                expect(err).not.be.ok();

                expect(evt.revision).to.eql(4);

                done();
              });
            }
          }
          denorm.handle(evt4, function (errs, e, notis) {
            check();
          });
          denorm.handle(evt3, function (errs, e, notis) {
            check();
          });
          denorm.handle(evt2, function (errs, e, notis) {
            check();
          });
          denorm.handle(evt2, function (errs, e, notis) {
            check();
          });
          denorm.handle(evt2, function (errs, e, notis) {
            check();
          });
          denorm.handle(evt4, function (errs, e, notis) {
            check();
          });

          denorm.handle(evt2, function (errs, e, notis) {
            check();
          });
          denorm.handle(evt3, function (errs, e, notis) {
            check();
          });
          denorm.handle(evt4, function (errs, e, notis) {
            check();
          });

        });

      });

    });

    describe('replaying some events', function () {

      before(function (done) {
        denorm.clear(done);
      });

      it('it should work as expected', function (done) {

        var publishedEvents = [];
        denorm.onEvent(function (evt) {
          publishedEvents.push(evt);
        });

        var publishedNotis = [];
        denorm.onNotification(function (noti) {
          publishedNotis.push(noti);
        });

        var evt1 = {
          id: 'evtId',
          correlationId: 'cmdId',
          name: 'enteredNewPerson',
          aggregate: {
            id: '12345678',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            firstname: 'Jack',
            lastname: 'Joe',
            email: 'a@b.c'
          },
          revision: 1,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        var evt2 = {
          id: 'evtId2',
          correlationId: 'cmdId2',
          name: 'registeredEMailAddress',
          aggregate: {
            id: '12345678',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            email: 'd@e.f'
          },
          revision: 2,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        var evt3 = {
          id: 'evtId3',
          correlationId: 'cmdId3',
          name: 'registeredEMailAddress',
          aggregate: {
            id: '12345678',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            email: 'g@h.i'
          },
          revision: 3,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        denorm.replay([evt1, evt2, evt2], function (err) {
          expect(err).not.to.be.ok();

          denorm.handle(evt3, function (errs, e, notis) {
            expect(errs).not.to.be.ok();
            expect(e).to.eql(evt3);
            expect(e.defForAllExt).to.eql(true);
            expect(e.extended).not.to.be.ok();
            expect(e.extendedDefault).to.eql(true);
            expect(notis).to.be.an('array');
            expect(notis.length).to.eql(2);
            expect(notis[0].name).to.eql('update');
            expect(notis[0].collection).to.eql('person');
            expect(notis[0].payload.id).to.eql('12345678');
            expect(notis[0].payload.firstname).to.eql('Jack');
            expect(notis[0].payload.lastname).to.eql('Joe');
            expect(notis[0].payload.email).not.to.be.ok();
            expect(notis[0].payload.generalEmail).to.eql('g@h.i');
            expect(notis[0].payload.incr).to.eql(2);
            expect(notis[0].payload.ref.obj.added).not.to.be.ok();
            expect(notis[0].id).to.be.a('string');
            expect(notis[0].correlationId).to.eql('cmdId3');
            expect(notis[0].meta.event.id).to.eql('evtId3');
            expect(notis[0].meta.event.name).to.eql('registeredEMailAddress');
            expect(notis[0].meta.userId).to.eql('userId');
            expect(notis[0].meta.aggregate.id).to.eql('12345678');
            expect(notis[0].meta.aggregate.name).to.eql('person');
            expect(notis[0].meta.aggregate.revision).to.eql(3);
            expect(notis[0].meta.context.name).to.eql('hr');
            expect(notis[1].name).to.eql('update');
            expect(notis[1].collection).to.eql('personDetail');
            expect(notis[1].payload.id).to.eql('12345678');
            expect(notis[1].payload.firstname).to.eql('Jack');
            expect(notis[1].payload.lastname).to.eql('Joe');
            expect(notis[1].payload.email).to.eql('g@h.i');
            expect(notis[1].id).to.be.a('string');
            expect(notis[1].correlationId).to.eql('cmdId3');
            expect(notis[1].meta.event.id).to.eql('evtId3');
            expect(notis[1].meta.event.name).to.eql('registeredEMailAddress');
            expect(notis[1].meta.userId).to.eql('userId');
            expect(notis[1].meta.aggregate.id).to.eql('12345678');
            expect(notis[1].meta.aggregate.name).to.eql('person');
            expect(notis[1].meta.aggregate.revision).to.eql(3);
            expect(notis[1].meta.context.name).to.eql('hr');

            expect(publishedEvents.length).to.eql(1);
            expect(publishedEvents[0]).to.eql(evt3);
            expect(publishedEvents[0].defForAllExt).to.eql(true);
            expect(publishedEvents[0].extended).not.to.be.ok();
            expect(publishedEvents[0].extendedDefault).to.eql(true);
            expect(publishedNotis.length).to.eql(2);
            expect(publishedNotis[0].name).to.eql('update');
            expect(publishedNotis[0].collection).to.eql('person');
            expect(publishedNotis[0].payload.id).to.eql('12345678');
            expect(publishedNotis[0].payload.firstname).to.eql('Jack');
            expect(publishedNotis[0].payload.lastname).to.eql('Joe');
            expect(publishedNotis[0].payload.email).not.to.be.ok();
            expect(publishedNotis[0].payload.generalEmail).to.eql('g@h.i');
            expect(publishedNotis[0].id).to.be.a('string');
            expect(publishedNotis[0].correlationId).to.eql('cmdId3');
            expect(publishedNotis[0].meta.event.id).to.eql('evtId3');
            expect(publishedNotis[0].meta.event.name).to.eql('registeredEMailAddress');
            expect(publishedNotis[0].meta.userId).to.eql('userId');
            expect(publishedNotis[0].meta.aggregate.id).to.eql('12345678');
            expect(publishedNotis[0].meta.aggregate.name).to.eql('person');
            expect(publishedNotis[0].meta.aggregate.revision).to.eql(3);
            expect(publishedNotis[0].meta.context.name).to.eql('hr');
            expect(publishedNotis[1].name).to.eql('update');
            expect(publishedNotis[1].collection).to.eql('personDetail');
            expect(publishedNotis[1].payload.id).to.eql('12345678');
            expect(publishedNotis[1].payload.firstname).to.eql('Jack');
            expect(publishedNotis[1].payload.lastname).to.eql('Joe');
            expect(publishedNotis[1].payload.email).to.eql('g@h.i');
            expect(publishedNotis[1].id).to.be.a('string');
            expect(publishedNotis[1].correlationId).to.eql('cmdId3');
            expect(publishedNotis[1].meta.event.id).to.eql('evtId3');
            expect(publishedNotis[1].meta.event.name).to.eql('registeredEMailAddress');
            expect(publishedNotis[1].meta.userId).to.eql('userId');
            expect(publishedNotis[1].meta.aggregate.id).to.eql('12345678');
            expect(publishedNotis[1].meta.aggregate.name).to.eql('person');
            expect(publishedNotis[1].meta.aggregate.revision).to.eql(3);
            expect(publishedNotis[1].meta.context.name).to.eql('hr');

            done();
          });
        });

      });

    });

    describe('replaying some events in parts', function () {

      before(function (done) {
        denorm.clear(done);
      });

      it('it should work as expected', function (done) {

        var publishedEvents = [];
        denorm.onEvent(function (evt) {
          publishedEvents.push(evt);
        });

        var publishedNotis = [];
        denorm.onNotification(function (noti) {
          publishedNotis.push(noti);
        });

        var evt1 = {
          id: 'evtIdp',
          correlationId: 'cmdIdp',
          name: 'enteredNewPerson',
          aggregate: {
            id: '12345678p',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            firstname: 'Jack',
            lastname: 'Joe',
            email: 'a@b.c'
          },
          revision: 1,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        var evt2 = {
          id: 'evtId2p',
          correlationId: 'cmdId2p',
          name: 'registeredEMailAddress',
          aggregate: {
            id: '12345678p',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            email: 'd@e.f'
          },
          revision: 2,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        var evt3 = {
          id: 'evtId3p',
          correlationId: 'cmdId3p',
          name: 'registeredEMailAddress',
          aggregate: {
            id: '12345678p',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            email: 'g@h.i'
          },
          revision: 3,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        var evt4 = {
          id: 'evtId4p',
          correlationId: 'cmdId4p',
          name: 'registeredEMailAddress',
          aggregate: {
            id: '12345678p',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            email: 'g@h.i2'
          },
          revision: 4,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        var evt5 = {
          id: 'evtId5p',
          correlationId: 'cmdId5p',
          name: 'registeredEMailAddress',
          aggregate: {
            id: '12345678p',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            email: 'g@h.i3'
          },
          revision: 5,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        var evt6 = {
          id: 'evtId6p',
          correlationId: 'cmdId6p',
          name: 'enteredNewPerson',
          aggregate: {
            id: '32145876',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            firstname: 'Jane',
            lastname: 'Jonson',
            email: 'a@b.com'
          },
          revision: 0,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        var evt7 = {
          id: 'evtId7p',
          correlationId: 'cmdId7p',
          name: 'blockedEmail',
          aggregate: {
            id: 'dont-care',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            email: 'g@h.i3'
          },
          revision: 0,
          version: 0,
          meta: {
            userId: 'userId'
          }
        };

        var evt8 = {
          id: 'evtId8p',
          correlationId: 'cmdId8p',
          name: 'exitedPerson',
          aggregate: {
            id: '12345678p',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {},
          revision: 7,
          version: 0,
          meta: {
            userId: 'userId'
          }
        };

        var evt9 = {
          id: 'evtId9p',
          correlationId: 'cmdId9p',
          name: 'blockedEmail',
          aggregate: {
            id: 'dont-care-2',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            email: 'a@b.com'
          },
          revision: 0,
          version: 0,
          meta: {
            userId: 'userId'
          }
        };

        denorm.replayStreamed(function (replay, finished) {

          replay(evt1);
          replay(evt2);

          process.nextTick(function () {
            finished(function (err) {
              expect(err).not.to.be.ok();

              denorm.replayStreamed(function (replay, finished) {

                replay(evt3);

                finished(function (err) {
                  expect(err).not.to.be.ok();

                  denorm.handle(evt4, function (errs, e, notis) {
                    expect(errs).not.to.be.ok();
                    expect(e).to.eql(evt4);
                    expect(e.defForAllExt).to.eql(true);
                    expect(e.extended).not.to.be.ok();
                    expect(e.extendedDefault).to.eql(true);
                    expect(notis).to.be.an('array');
                    expect(notis.length).to.eql(2);
                    expect(notis[0].name).to.eql('update');
                    expect(notis[0].collection).to.eql('person');
                    expect(notis[0].payload.id).to.eql('12345678p');
                    expect(notis[0].payload.firstname).to.eql('Jack');
                    expect(notis[0].payload.lastname).to.eql('Joe');
                    expect(notis[0].payload.email).not.to.be.ok();
                    expect(notis[0].payload.generalEmail).to.eql('g@h.i2');
                    expect(notis[0].id).to.be.a('string');
                    expect(notis[0].correlationId).to.eql('cmdId4p');
                    expect(notis[0].meta.event.id).to.eql('evtId4p');
                    expect(notis[0].meta.event.name).to.eql('registeredEMailAddress');
                    expect(notis[0].meta.userId).to.eql('userId');
                    expect(notis[0].meta.aggregate.id).to.eql('12345678p');
                    expect(notis[0].meta.aggregate.name).to.eql('person');
                    expect(notis[0].meta.aggregate.revision).to.eql(4);
                    expect(notis[0].meta.context.name).to.eql('hr');
                    expect(notis[1].name).to.eql('update');
                    expect(notis[1].collection).to.eql('personDetail');
                    expect(notis[1].payload.id).to.eql('12345678p');
                    expect(notis[1].payload.firstname).to.eql('Jack');
                    expect(notis[1].payload.lastname).to.eql('Joe');
                    expect(notis[1].payload.email).to.eql('g@h.i2');
                    expect(notis[1].id).to.be.a('string');
                    expect(notis[1].correlationId).to.eql('cmdId4p');
                    expect(notis[1].meta.event.id).to.eql('evtId4p');
                    expect(notis[1].meta.event.name).to.eql('registeredEMailAddress');
                    expect(notis[1].meta.userId).to.eql('userId');
                    expect(notis[1].meta.aggregate.id).to.eql('12345678p');
                    expect(notis[1].meta.aggregate.name).to.eql('person');
                    expect(notis[1].meta.aggregate.revision).to.eql(4);
                    expect(notis[1].meta.context.name).to.eql('hr');

                    expect(publishedEvents.length).to.eql(1);
                    expect(publishedEvents[0]).to.eql(evt4);
                    expect(publishedEvents[0].defForAllExt).to.eql(true);
                    expect(publishedEvents[0].extended).not.to.be.ok();
                    expect(publishedEvents[0].extendedDefault).to.eql(true);
                    expect(publishedNotis.length).to.eql(2);
                    expect(publishedNotis[0].name).to.eql('update');
                    expect(publishedNotis[0].collection).to.eql('person');
                    expect(publishedNotis[0].payload.id).to.eql('12345678p');
                    expect(publishedNotis[0].payload.firstname).to.eql('Jack');
                    expect(publishedNotis[0].payload.lastname).to.eql('Joe');
                    expect(publishedNotis[0].payload.email).not.to.be.ok();
                    expect(publishedNotis[0].payload.generalEmail).to.eql('g@h.i2');
                    expect(publishedNotis[0].id).to.be.a('string');
                    expect(publishedNotis[0].correlationId).to.eql('cmdId4p');
                    expect(publishedNotis[0].meta.event.id).to.eql('evtId4p');
                    expect(publishedNotis[0].meta.event.name).to.eql('registeredEMailAddress');
                    expect(publishedNotis[0].meta.userId).to.eql('userId');
                    expect(publishedNotis[0].meta.aggregate.id).to.eql('12345678p');
                    expect(publishedNotis[0].meta.aggregate.name).to.eql('person');
                    expect(publishedNotis[0].meta.aggregate.revision).to.eql(4);
                    expect(publishedNotis[0].meta.context.name).to.eql('hr');
                    expect(publishedNotis[1].name).to.eql('update');
                    expect(publishedNotis[1].collection).to.eql('personDetail');
                    expect(publishedNotis[1].payload.id).to.eql('12345678p');
                    expect(publishedNotis[1].payload.firstname).to.eql('Jack');
                    expect(publishedNotis[1].payload.lastname).to.eql('Joe');
                    expect(publishedNotis[1].payload.email).to.eql('g@h.i2');
                    expect(publishedNotis[1].id).to.be.a('string');
                    expect(publishedNotis[1].correlationId).to.eql('cmdId4p');
                    expect(publishedNotis[1].meta.event.id).to.eql('evtId4p');
                    expect(publishedNotis[1].meta.event.name).to.eql('registeredEMailAddress');
                    expect(publishedNotis[1].meta.userId).to.eql('userId');
                    expect(publishedNotis[1].meta.aggregate.id).to.eql('12345678p');
                    expect(publishedNotis[1].meta.aggregate.name).to.eql('person');
                    expect(publishedNotis[1].meta.aggregate.revision).to.eql(4);
                    expect(publishedNotis[1].meta.context.name).to.eql('hr');

                    denorm.replayStreamed(function (replay, finished) {
                      replay(evt5);
                      replay(evt6);
                      replay(evt7);
                      replay(evt8);

                      finished(function (err) {
                        expect(err).not.to.be.ok();

                        denorm.handle(evt9, function (errs, e, notis) {
                          expect(errs).not.to.be.ok();
                          expect(e).to.eql(evt9);
                          expect(notis).to.be.an('array');
                          expect(notis.length).to.eql(1);
                          expect(notis[0].name).to.eql('update');
                          expect(notis[0].collection).to.eql('personDetail');
                          expect(notis[0].payload.id).to.eql('32145876');
                          expect(notis[0].payload.firstname).to.eql('Jane');
                          expect(notis[0].payload.lastname).to.eql('Jonson');
                          expect(notis[0].payload.email).to.eql('a@b.com');
                          expect(notis[0].payload.blocked).to.eql(true);

                          expect(notis[0].id).to.be.a('string');
                          expect(notis[0].correlationId).to.eql('cmdId9p');
                          expect(notis[0].meta.event.id).to.eql('evtId9p');
                          expect(notis[0].meta.event.name).to.eql('blockedEmail');
                          expect(notis[0].meta.userId).to.eql('userId');
                          expect(notis[0].meta.aggregate.id).to.eql('dont-care-2');
                          expect(notis[0].meta.aggregate.name).to.eql('person');
                          expect(notis[0].meta.aggregate.revision).to.eql(0);
                          expect(notis[0].meta.context.name).to.eql('hr');

                          expect(publishedEvents.length).to.eql(2);
                          expect(publishedEvents[1]).to.eql(evt9);
                          expect(publishedEvents[1].defForAllExt).to.eql(true);
                          expect(publishedEvents[1].extended).not.to.be.ok();
                          expect(publishedEvents[1].extendedDefault).to.eql(true);
                          expect(publishedNotis.length).to.eql(3);
                          expect(publishedNotis[2].name).to.eql('update');
                          expect(publishedNotis[2].collection).to.eql('personDetail');
                          expect(publishedNotis[2].payload.id).to.eql('32145876');
                          expect(publishedNotis[2].payload.firstname).to.eql('Jane');
                          expect(publishedNotis[2].payload.lastname).to.eql('Jonson');
                          expect(publishedNotis[2].payload.email).to.eql('a@b.com');
                          expect(publishedNotis[2].payload.blocked).to.eql(true);
                          expect(publishedNotis[2].id).to.be.a('string');
                          expect(publishedNotis[2].correlationId).to.eql('cmdId9p');
                          expect(publishedNotis[2].meta.event.id).to.eql('evtId9p');
                          expect(publishedNotis[2].meta.event.name).to.eql('blockedEmail');
                          expect(publishedNotis[2].meta.userId).to.eql('userId');
                          expect(publishedNotis[2].meta.aggregate.id).to.eql('dont-care-2');
                          expect(publishedNotis[2].meta.aggregate.name).to.eql('person');
                          expect(publishedNotis[2].meta.aggregate.revision).to.eql(0);
                          expect(publishedNotis[2].meta.context.name).to.eql('hr');

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

    describe('handling an event that denormalizes multiple viewmodels in same collection', function () {

      before(function (done) {
        denorm.clear(done);
      });

      it('it should publish 2 notification and it should callback without an error but with an extended event', function (done) {

        var publishedEvents = [];
        denorm.onEvent(function (evt) {
          publishedEvents.push(evt);
        });

        var publishedNotis = [];
        denorm.onNotification(function (noti) {
          publishedNotis.push(noti);
        });

        var evt11 = {
          id: 'evtId',
          correlationId: 'cmdId',
          name: 'enteredNewPerson',
          aggregate: {
            id: '71632',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            firstname: 'Jack',
            lastname: 'Joe',
            email: 'a@b.c'
          },
          revision: 1,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        var evt12 = {
          id: 'evtId2',
          correlationId: 'cmdId2',
          name: 'registeredEMailAddress',
          aggregate: {
            id: '71632',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            email: 'd@e.f'
          },
          revision: 2,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        var evt21 = {
          id: 'evtId3',
          correlationId: 'cmdId',
          name: 'enteredNewPerson',
          aggregate: {
            id: '14123',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            firstname: 'Jack',
            lastname: 'Joe',
            email: 'a@b.c'
          },
          revision: 1,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        var evt22 = {
          id: 'evtId4',
          correlationId: 'cmdId2',
          name: 'registeredEMailAddress',
          aggregate: {
            id: '14123',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            email: 'd@e.f'
          },
          revision: 2,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        denorm.handle(evt11, function (errs, e, notis) {
          expect(errs).not.to.be.ok();

          denorm.handle(evt12, function (errs, e, notis) {
            expect(errs).not.to.be.ok();

            denorm.handle(evt21, function (errs, e, notis) {
              expect(errs).not.to.be.ok();

              denorm.handle(evt22, function (errs, e, notis) {
                expect(errs).not.to.be.ok();

                expect(publishedEvents.length).to.eql(4);
                for (var m in evt11) {
                  expect(publishedEvents[0][m]).to.eql(evt11[m]);
                }
                for (var m in evt11) {
                  expect(publishedEvents[1][m]).to.eql(evt12[m]);
                }
                for (var m in evt11) {
                  expect(publishedEvents[2][m]).to.eql(evt21[m]);
                }
                for (var m in evt11) {
                  expect(publishedEvents[3][m]).to.eql(evt22[m]);
                }

                expect(publishedNotis.length).to.eql(9);
                expect(publishedNotis[0].name).to.eql('create');
                expect(publishedNotis[0].collection).to.eql('person');
                expect(publishedNotis[0].payload.id).to.eql('71632');
                expect(publishedNotis[1].name).to.eql('create');
                expect(publishedNotis[1].collection).to.eql('personDetail');
                expect(publishedNotis[1].payload.id).to.eql('71632');
                expect(publishedNotis[2].name).to.eql('update');
                expect(publishedNotis[2].collection).to.eql('person');
                expect(publishedNotis[2].payload.id).to.eql('71632');
                expect(publishedNotis[3].name).to.eql('update');
                expect(publishedNotis[3].collection).to.eql('personDetail');
                expect(publishedNotis[3].payload.id).to.eql('71632');
                expect(publishedNotis[4].name).to.eql('create');
                expect(publishedNotis[4].collection).to.eql('person');
                expect(publishedNotis[4].payload.id).to.eql('14123');
                expect(publishedNotis[5].name).to.eql('create');
                expect(publishedNotis[5].collection).to.eql('personDetail');
                expect(publishedNotis[5].payload.id).to.eql('14123');
                expect(publishedNotis[6].name).to.eql('update');
                expect(publishedNotis[6].collection).to.eql('person');
                expect(publishedNotis[6].payload.id).to.eql('14123');
                expect(publishedNotis[7].name).to.eql('update');
                expect(publishedNotis[7].collection).to.eql('person');
                expect(publishedNotis[7].payload.id).to.eql('71632');
                expect(publishedNotis[8].name).to.eql('update');
                expect(publishedNotis[8].collection).to.eql('personDetail');
                expect(publishedNotis[8].payload.id).to.eql('14123');

                done();
              });
            });
          });
        });

      });

    });

    describe('handling an event that will be handled by 1 viewBuilder and an onAfterCommit function', function () {

      it('it should publish 1 notification and it should callback without an error', function (done) {

        var publishedEvents = [];
        denorm.onEvent(function (evt) {
          publishedEvents.push(evt);
        });

        var publishedNotis = [];
        denorm.onNotification(function (noti) {
          publishedNotis.push(noti);
        });

        var evt = {
          id: 'evtId',
          correlationId: 'cmdId',
          name: 'personLeaved',
          aggregate: {
            id: '1234special'
//            name: 'person'
          },
          context: {
//            name: 'hr'
          },
          payload: {
            special: 'important value'
          },
          revision: 1,
          version: 0,
          meta: {
            userId: 'userId'
          }
        };

        denorm.handle(evt, function (errs, e, notis) {
          expect(errs).not.to.be.ok();
          expect(e).to.eql(evt);
          expect(notis).to.be.an('array');
          expect(notis.length).to.eql(1);
          expect(notis[0].name).to.eql('create');
          expect(notis[0].collection).to.eql('person');
          expect(notis[0].payload.sp).to.eql('important value');
          expect(notis[0].id).to.be.a('string');
          expect(notis[0].correlationId).to.eql('cmdId');
          expect(notis[0].meta.event.id).to.eql('evtId');
          expect(notis[0].meta.event.name).to.eql('personLeaved');
          expect(notis[0].meta.userId).to.eql('userId');
          expect(notis[0].meta.aggregate.id).to.eql('1234special');
          expect(notis[0].meta.aggregate.name).not.to.be.ok();
          expect(notis[0].meta.aggregate.revision).to.eql(1);
          expect(notis[0].meta.context.name).not.to.be.ok();

          expect(publishedEvents.length).to.eql(1);
          expect(publishedEvents[0]).to.eql(evt);
          expect(publishedNotis.length).to.eql(1);
          expect(publishedNotis[0].name).to.eql('create');
          expect(publishedNotis[0].collection).to.eql('person');
          expect(publishedNotis[0].payload.sp).to.eql('important value');
          expect(publishedNotis[0].id).to.be.a('string');
          expect(publishedNotis[0].correlationId).to.eql('cmdId');
          expect(publishedNotis[0].meta.event.id).to.eql('evtId');
          expect(publishedNotis[0].meta.event.name).to.eql('personLeaved');
          expect(publishedNotis[0].meta.userId).to.eql('userId');
          expect(publishedNotis[0].meta.aggregate.id).to.eql('1234special');
          expect(publishedNotis[0].meta.aggregate.name).not.to.be.ok();
          expect(publishedNotis[0].meta.aggregate.revision).to.eql(1);
          expect(publishedNotis[0].meta.context.name).not.to.be.ok();

          done();
        });

      });

    });

    describe('skip event extender - handling an event that will be handled by 2 viewBuilder and a generic eventExtender and a generic preEventExtender', function () {

      before(function (done) {
        denorm = api({
          denormalizerPath: __dirname + '/fixture/set1',
          commandRejectedEventName: 'rejectedCommand',
          revisionGuard: { queueTimeout: 200, queueTimeoutMaxLoops: 2 },
          skipOnNotification: true, // has to be set
          skipExtendEvent: true, // has to be set
          skipOnEvent: true // has to be set
        });
        denorm.defineEvent({
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

        denorm.defineNotification({
          id: 'id',
          action: 'name',
          collection: 'collection',
          payload: 'payload',
          context: 'meta.context.name',
          aggregate: 'meta.aggregate.name',
          aggregateId: 'meta.aggregate.id',
          revision: 'meta.aggregate.revision',
          eventId: 'meta.event.id',
          event: 'meta.event.name',
          meta: 'meta'
        });

        denorm.defaultEventExtension(function (evt) {
          evt.defForAllExt = true;
          return evt;
        });

        expect(function () {
          denorm.getInfo();
        }).to.throwError('/init');

        denorm.init(function (err, warns) {
          expect(warns).not.to.be.ok();
          done(err);
        });

      })

      it('it should not publish notifications, the event shall not be extended, the event shall not be published', function (done) {
        var publishedEvents = [];
        denorm.onEvent(function (evt) {
          publishedEvents.push(evt);
        });

        var publishedNotis = [];
        denorm.onNotification(function (noti) {
          publishedNotis.push(noti);
        });

        var evt = {
          id: 'evtIdaranew',
          correlationId: 'cmdId',
          name: 'enteredNewPerson',
          aggregate: {
            id: '12345678aranew',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            firstname: 'Jack',
            lastname: 'Joe',
            email: 'a@b.c'
          },
          revision: 1,
          version: 2,
          meta: {
            userId: 'userId'
          }
        };

        denorm.handle(evt, function (errs, e, notis) {
          expect(errs).not.to.be.ok();
          for (var m in evt) {
            expect(e[m]).to.eql(evt[m]);
          }
          expect(e.defForAllExt).to.eql(undefined);
          expect(e.extended).to.eql(undefined);
          expect(e.extendedDefault).to.eql(undefined);
          expect(e.preExtended).to.eql(true);
          expect(notis).to.be.an('array');
          expect(notis.length).to.eql(2);
          expect(publishedEvents.length).to.eql(0);
          expect(publishedNotis.length).to.eql(0);
          done();
        });

      });

    });

  });

  describe('format 2', function () {

    var denorm;

    before(function (done) {
      denorm = api({ denormalizerPath: __dirname + '/fixture/set2', commandRejectedEventName: 'commandRejected', revisionGuard: { queueTimeout: 200, queueTimeoutMaxLoops: 2 } });
      denorm.defineEvent({
        correlationId: 'commandId',
        id: 'id',
        name: 'event',
        aggregateId: 'payload.id',
        payload: 'payload',
        revision: 'head.revision',
        version: 'head.version',
        meta: 'head'
      });

      denorm.defineNotification({
        id: 'id',
        action: 'name',
        collection: 'collection',
        payload: 'payload',
        aggregateId: 'meta.aggregate.id',
        revision: 'meta.aggregate.revision',
        eventId: 'meta.event.id',
        event: 'meta.event.name',
        meta: 'meta'
      });

      denorm.defaultEventExtension(function (evt) {
        evt.defForAllExt = true;
        return evt;
      });

      denorm.init(done);
    });

    describe('handling an event that will not be handled by any viewBuilder or any specific eventExtender', function () {

      it('it should not publish any notification and it should callback without an error but with same event', function (done) {

        var publishedEvents = [];
        denorm.onEvent(function (evt) {
          publishedEvents.push(evt);
        });

        var publishedNotis = [];
        denorm.onNotification(function (noti) {
          publishedNotis.push(noti);
        });

        var evt = {
          id: 'evtId',
          commandId: 'cmdId',
          event: 'evtName',
          payload: {
            id: 'aggregateId2',
            data: 'payload'
          },
          head: {
            revision: 1,
            version: 0,
            userId: 'userId'
          }
        };

        denorm.handle(evt, function (err, e, notis) {
          expect(err).not.to.be.ok();
          expect(e).to.eql(evt);
          expect(e.defForAllExt).to.eql(true);
          expect(e.extended).not.to.be.ok();
          expect(e.extendedDefault).to.eql(true);
          expect(notis).to.be.an('array');
          expect(notis.length).to.eql(0);

          expect(publishedEvents.length).to.eql(1);
          expect(publishedEvents[0]).to.eql(evt);
          expect(publishedEvents[0].defForAllExt).to.eql(true);
          expect(publishedEvents[0].extended).not.to.be.ok();
          expect(publishedEvents[0].extendedDefault).to.eql(true);
          expect(publishedNotis.length).to.eql(0);

          done();
        });

      });

    });

    describe('handling an event that will be handled by 2 viewBuilders and a specific eventExtender', function () {

      it('it should publish 2 notifications and it should callback without an error but with an extended event', function (done) {

        var publishedEvents = [];
        denorm.onEvent(function (evt) {
          publishedEvents.push(evt);
        });

        var publishedNotis = [];
        denorm.onNotification(function (noti) {
          publishedNotis.push(noti);
        });

        var evt = {
          id: 'evtId',
          commandId: 'cmdId',
          event: 'enteredNewPerson',
          payload: {
            id: '12342',
            firstname: 'Jack',
            lastname: 'Joe',
            email: 'a@b.c'
          },
          head: {
            revision: 1,
            version: 2,
            userId: 'userId'
          }
        };

        denorm.handle(evt, function (errs, e, notis) {
          expect(errs).not.to.be.ok();

          for (var m in evt) {
            expect(e[m]).to.eql(evt[m]);
          }
          expect(e.defForAllExt).to.eql(true);
          expect(e.extended).to.eql(true);
          expect(e.extendedDefault).not.to.be.ok();
          expect(notis).to.be.an('array');
          expect(notis.length).to.eql(2);

          var personIndex = 0;
          var personDetailIndex = 1;
          if (notis[0].collection !== 'person') {
            personIndex = 1;
            personDetailIndex = 0;
          }

          expect(notis[personIndex].name).to.eql('create');
          expect(notis[personIndex].collection).to.eql('person');
          expect(notis[personIndex].payload.id).to.eql('12342');
          expect(notis[personIndex].payload.firstname).to.eql('Jack');
          expect(notis[personIndex].payload.lastname).to.eql('Joe');
          expect(notis[personIndex].payload.email).not.to.be.ok();
          expect(notis[personIndex].id).to.be.a('string');
          expect(notis[personIndex].correlationId).to.eql('cmdId');
          expect(notis[personIndex].meta.event.id).to.eql('evtId');
          expect(notis[personIndex].meta.event.name).to.eql('enteredNewPerson');
          expect(notis[personIndex].meta.userId).to.eql('userId');
          expect(notis[personIndex].meta.aggregate.id).to.eql('12342');
          expect(notis[personIndex].meta.aggregate.name).not.to.be.ok();
          expect(notis[personIndex].meta.aggregate.revision).to.eql(1);
          expect(notis[personIndex].meta.context).not.to.be.ok();
          expect(notis[personDetailIndex].name).to.eql('create');
          expect(notis[personDetailIndex].collection).to.eql('personDetail');
          expect(notis[personDetailIndex].payload.id).to.eql('12342');
          expect(notis[personDetailIndex].payload.firstname).to.eql('Jack');
          expect(notis[personDetailIndex].payload.lastname).to.eql('Joe');
          expect(notis[personDetailIndex].payload.email).to.eql('a@b.c');
          expect(notis[personDetailIndex].id).to.be.a('string');
          expect(notis[personDetailIndex].correlationId).to.eql('cmdId');
          expect(notis[personDetailIndex].meta.event.id).to.eql('evtId');
          expect(notis[personDetailIndex].meta.event.name).to.eql('enteredNewPerson');
          expect(notis[personDetailIndex].meta.userId).to.eql('userId');
          expect(notis[personDetailIndex].meta.aggregate.id).to.eql('12342');
          expect(notis[personDetailIndex].meta.aggregate.name).not.to.be.ok();
          expect(notis[personDetailIndex].meta.aggregate.revision).to.eql(1);
          expect(notis[personDetailIndex].meta.context).not.to.be.ok();

          expect(publishedEvents.length).to.eql(1);
          for (var m in evt) {
            expect(publishedEvents[0][m]).to.eql(evt[m]);
          }
          expect(publishedEvents[0].defForAllExt).to.eql(true);
          expect(publishedEvents[0].extended).to.eql(true);
          expect(publishedEvents[0].extendedDefault).not.to.be.ok();
          expect(publishedNotis.length).to.eql(2);
          expect(publishedNotis[personIndex].name).to.eql('create');
          expect(publishedNotis[personIndex].collection).to.eql('person');
          expect(publishedNotis[personIndex].payload.id).to.eql('12342');
          expect(publishedNotis[personIndex].payload.firstname).to.eql('Jack');
          expect(publishedNotis[personIndex].payload.lastname).to.eql('Joe');
          expect(publishedNotis[personIndex].payload.email).not.to.be.ok();
          expect(publishedNotis[personIndex].id).to.be.a('string');
          expect(publishedNotis[personIndex].correlationId).to.eql('cmdId');
          expect(publishedNotis[personIndex].meta.event.id).to.eql('evtId');
          expect(publishedNotis[personIndex].meta.event.name).to.eql('enteredNewPerson');
          expect(publishedNotis[personIndex].meta.userId).to.eql('userId');
          expect(publishedNotis[personIndex].meta.aggregate.id).to.eql('12342');
          expect(publishedNotis[personIndex].meta.aggregate.name).not.to.be.ok();
          expect(publishedNotis[personIndex].meta.aggregate.revision).to.eql(1);
          expect(publishedNotis[personIndex].meta.context).not.to.be.ok();
          expect(publishedNotis[personDetailIndex].name).to.eql('create');
          expect(publishedNotis[personDetailIndex].collection).to.eql('personDetail');
          expect(publishedNotis[personDetailIndex].payload.id).to.eql('12342');
          expect(publishedNotis[personDetailIndex].payload.firstname).to.eql('Jack');
          expect(publishedNotis[personDetailIndex].payload.lastname).to.eql('Joe');
          expect(publishedNotis[personDetailIndex].payload.email).to.eql('a@b.c');
          expect(publishedNotis[personDetailIndex].id).to.be.a('string');
          expect(publishedNotis[personDetailIndex].correlationId).to.eql('cmdId');
          expect(publishedNotis[personDetailIndex].meta.event.id).to.eql('evtId');
          expect(publishedNotis[personDetailIndex].meta.event.name).to.eql('enteredNewPerson');
          expect(publishedNotis[personDetailIndex].meta.userId).to.eql('userId');
          expect(publishedNotis[personDetailIndex].meta.aggregate.id).to.eql('12342');
          expect(publishedNotis[personDetailIndex].meta.aggregate.name).not.to.be.ok();
          expect(publishedNotis[personDetailIndex].meta.aggregate.revision).to.eql(1);
          expect(publishedNotis[personDetailIndex].meta.context).not.to.be.ok();

          done();
        });

      });

    });

    describe('handling an event that will be handled by 1 viewBuilder and a generic eventExtender', function () {

      it('it should publish 1 notification and it should callback without an error but with an extended event', function (done) {

        var publishedEvents = [];
        denorm.onEvent(function (evt) {
          publishedEvents.push(evt);
        });

        var publishedNotis = [];
        denorm.onNotification(function (noti) {
          publishedNotis.push(noti);
        });

        var evt = {
          id: 'evtId',
          commandId: 'cmdId',
          event: 'registeredEMailAddress',
          payload: {
            id: '12342',
            email: 'xyz@r.f'
          },
          head: {
            revision: 2,
            version: 2,
            userId: 'userId'
          }
        };

        denorm.handle(evt, function (errs, e, notis) {
          expect(errs).not.to.be.ok();
          expect(e).to.eql(evt);
          expect(e.defForAllExt).to.eql(true);
          expect(e.extended).not.to.be.ok();
          expect(e.extendedDefault).to.eql(true);
          expect(notis).to.be.an('array');
          expect(notis.length).to.eql(1);
          expect(notis[0].name).to.eql('update');
          expect(notis[0].collection).to.eql('personDetail');
          expect(notis[0].payload.id).to.eql('12342');
          expect(notis[0].payload.firstname).to.eql('Jack');
          expect(notis[0].payload.lastname).to.eql('Joe');
          expect(notis[0].payload.email).to.eql('xyz@r.f');
          expect(notis[0].id).to.be.a('string');
          expect(notis[0].correlationId).to.eql('cmdId');
          expect(notis[0].meta.event.id).to.eql('evtId');
          expect(notis[0].meta.event.name).to.eql('registeredEMailAddress');
          expect(notis[0].meta.userId).to.eql('userId');
          expect(notis[0].meta.aggregate.id).to.eql('12342');
          expect(notis[0].meta.aggregate.name).not.to.be.ok();
          expect(notis[0].meta.aggregate.revision).to.eql(2);
          expect(notis[0].meta.context).not.to.be.ok();

          expect(publishedEvents.length).to.eql(1);
          expect(publishedEvents[0]).to.eql(evt);
          expect(publishedEvents[0].defForAllExt).to.eql(true);
          expect(publishedEvents[0].extended).not.to.be.ok();
          expect(publishedEvents[0].extendedDefault).to.eql(true);
          expect(publishedNotis.length).to.eql(1);
          expect(publishedNotis[0].name).to.eql('update');
          expect(publishedNotis[0].collection).to.eql('personDetail');
          expect(publishedNotis[0].payload.id).to.eql('12342');
          expect(publishedNotis[0].payload.firstname).to.eql('Jack');
          expect(publishedNotis[0].payload.lastname).to.eql('Joe');
          expect(publishedNotis[0].payload.email).to.eql('xyz@r.f');
          expect(publishedNotis[0].id).to.be.a('string');
          expect(publishedNotis[0].correlationId).to.eql('cmdId');
          expect(publishedNotis[0].meta.event.id).to.eql('evtId');
          expect(publishedNotis[0].meta.event.name).to.eql('registeredEMailAddress');
          expect(publishedNotis[0].meta.userId).to.eql('userId');
          expect(publishedNotis[0].meta.aggregate.id).to.eql('12342');
          expect(publishedNotis[0].meta.aggregate.name).not.to.be.ok();
          expect(publishedNotis[0].meta.aggregate.revision).to.eql(2);
          expect(publishedNotis[0].meta.context).not.to.be.ok();

          done();
        });

      });

    });

    describe('handling an event that will be handled by 1 viewBuilder and a generic eventExtender', function () {

      it('it should publish 1 notification and it should callback without an error but with an extended event', function (done) {

        var publishedEvents = [];
        denorm.onEvent(function (evt) {
          publishedEvents.push(evt);
        });

        var publishedNotis = [];
        denorm.onNotification(function (noti) {
          publishedNotis.push(noti);
        });

        var evt = {
          id: 'evtId',
          commandId: 'cmdId',
          event: 'registeredEMailAddress',
          payload: {
            id: '12342',
            email: 'abc@d.e'
          },
          head: {
            revision: 3,
            version: 2,
            userId: 'userId'
          }
        };

        denorm.handle(evt, function (errs, e, notis) {
          expect(errs).not.to.be.ok();
          expect(e).to.eql(evt);
          expect(e.defForAllExt).to.eql(true);
          expect(e.extended).not.to.be.ok();
          expect(e.extendedDefault).to.eql(true);
          expect(notis).to.be.an('array');
          expect(notis.length).to.eql(1);
          expect(notis[0].name).to.eql('update');
          expect(notis[0].collection).to.eql('personDetail');
          expect(notis[0].payload.id).to.eql('12342');
          expect(notis[0].payload.firstname).to.eql('Jack');
          expect(notis[0].payload.lastname).to.eql('Joe');
          expect(notis[0].payload.email).to.eql('abc@d.e');
          expect(notis[0].id).to.be.a('string');
          expect(notis[0].correlationId).to.eql('cmdId');
          expect(notis[0].meta.event.id).to.eql('evtId');
          expect(notis[0].meta.event.name).to.eql('registeredEMailAddress');
          expect(notis[0].meta.userId).to.eql('userId');
          expect(notis[0].meta.aggregate.id).to.eql('12342');
          expect(notis[0].meta.aggregate.name).not.to.be.ok();
          expect(notis[0].meta.aggregate.revision).to.eql(3);
          expect(notis[0].meta.context).not.to.be.ok();

          expect(publishedEvents.length).to.eql(1);
          expect(publishedEvents[0]).to.eql(evt);
          expect(publishedEvents[0].defForAllExt).to.eql(true);
          expect(publishedEvents[0].extended).not.to.be.ok();
          expect(publishedEvents[0].extendedDefault).to.eql(true);
          expect(publishedNotis.length).to.eql(1);
          expect(publishedNotis[0].name).to.eql('update');
          expect(publishedNotis[0].collection).to.eql('personDetail');
          expect(publishedNotis[0].payload.id).to.eql('12342');
          expect(publishedNotis[0].payload.firstname).to.eql('Jack');
          expect(publishedNotis[0].payload.lastname).to.eql('Joe');
          expect(publishedNotis[0].payload.email).to.eql('abc@d.e');
          expect(publishedNotis[0].id).to.be.a('string');
          expect(publishedNotis[0].correlationId).to.eql('cmdId');
          expect(publishedNotis[0].meta.event.id).to.eql('evtId');
          expect(publishedNotis[0].meta.event.name).to.eql('registeredEMailAddress');
          expect(publishedNotis[0].meta.userId).to.eql('userId');
          expect(publishedNotis[0].meta.aggregate.id).to.eql('12342');
          expect(publishedNotis[0].meta.aggregate.name).not.to.be.ok();
          expect(publishedNotis[0].meta.aggregate.revision).to.eql(3);
          expect(publishedNotis[0].meta.context).not.to.be.ok();

          done();
        });

      });

    });

    describe('handling an event that was already handled', function () {

      it('it should not publish anything and callback with an error', function (done) {

        var publishedEvents = [];
        denorm.onEvent(function (evt) {
          publishedEvents.push(evt);
        });

        var publishedNotis = [];
        denorm.onNotification(function (noti) {
          publishedNotis.push(noti);
        });

        var evt = {
          id: 'evtId',
          commandId: 'cmdId',
          event: 'registeredEMailAddress',
          payload: {
            id: '12342',
            email: 'abc@d.e'
          },
          head: {
            revision: 3,
            version: 2,
            userId: 'userId'
          }
        };

        denorm.handle(evt, function (errs, e, notis) {
          expect(errs).to.be.ok();
          expect(errs.length).to.eql(1);
          expect(errs[0].name).to.eql('AlreadyDenormalizedError');
          expect(e).not.to.be.ok();
          expect(notis).not.to.be.ok();

          expect(publishedEvents.length).to.eql(0);
          expect(publishedNotis.length).to.eql(0);

          done();
        });

      });

    });

    describe('handling an event that has a bigger revision than expected', function () {

      it('it should fire an eventMissing event', function (done) {

        var publishedEvents = [];
        denorm.onEvent(function (evt) {
          publishedEvents.push(evt);
        });

        var publishedNotis = [];
        denorm.onNotification(function (noti) {
          publishedNotis.push(noti);
        });

        var evt = {
          id: 'evtId',
          commandId: 'cmdId',
          event: 'registeredEMailAddress',
          payload: {
            id: '12342',
            email: 'abc@d.e'
          },
          head: {
            revision: 7,
            version: 2,
            userId: 'userId'
          }
        };

        denorm.onEventMissing(function (info, e) {
          expect(info.aggregate).not.to.be.ok();
          expect(info.aggregateId).to.eql('12342');
          expect(info.context).not.to.be.ok();
          expect(info.aggregateRevision).to.eql(7);
          expect(info.guardRevision).to.eql(4);
          expect(e).to.eql(evt);

          expect(publishedEvents.length).to.eql(0);
          expect(publishedNotis.length).to.eql(0);

          done();
        });

        denorm.handle(evt, function (errs, e, notis) {});

      });

    });

    describe('handling an command rejected event', function () {

      it('it should work as expected', function (done) {

        var publishedEvents = [];
        denorm.onEvent(function (evt) {
          publishedEvents.push(evt);
        });

        var publishedNotis = [];
        denorm.onNotification(function (noti) {
          publishedNotis.push(noti);
        });

        var evt = {
          id: 'evtId',
          commandId: 'cmdId',
          event: 'commandRejected',
          payload: {
            id: '12342',
            reason: {
              name: 'AggregateDestroyedError',
              aggregateId: '12342',
              aggregateRevision: 6
            }
          },
          head: {
            revision: 6,
            version: 2,
            userId: 'userId'
          }
        };

        var eventMissingCalled = false;
        denorm.onEventMissing(function (info, e) {
          expect(info.aggregate).not.to.be.ok();
          expect(info.aggregateId).to.eql('12342');
          expect(info.context).not.to.be.ok();
          expect(info.aggregateRevision).to.eql(6);
          expect(info.guardRevision).to.eql(4);
          expect(e).to.eql(evt);
          eventMissingCalled = true;
        });

        denorm.handle(evt, function (errs, e, notis) {
          expect(errs).not.to.be.ok();
          expect(e).to.eql(evt);
          expect(notis.length).to.eql(0);

          expect(publishedEvents.length).to.eql(0);
          expect(publishedNotis.length).to.eql(0);

          expect(eventMissingCalled).to.eql(true);

          done();
        });

      });

    });

    describe('handling an command rejected event', function () {
      before(function (done) {
        denorm = api({
          denormalizerPath: __dirname + '/fixture/set2',
          commandRejectedEventName: 'commandRejected',
          revisionGuard: { queueTimeout: 200, queueTimeoutMaxLoops: 2 },
          skipOnEventMissing: true // has to be set
        });
        denorm.defineEvent({
          correlationId: 'commandId',
          id: 'id',
          name: 'event',
          aggregateId: 'payload.id',
          payload: 'payload',
          revision: 'head.revision',
          version: 'head.version',
          meta: 'head'
        });
        denorm.defineNotification({
          id: 'id',
          action: 'name',
          collection: 'collection',
          payload: 'payload',
          aggregateId: 'meta.aggregate.id',
          revision: 'meta.aggregate.revision',
          eventId: 'meta.event.id',
          event: 'meta.event.name',
          meta: 'meta'
        });
        denorm.defaultEventExtension(function (evt) {
          evt.defForAllExt = true;
          return evt;
        });
        denorm.init(done);

      })

      it('it should not fire an eventMissing event', function (done) {
        var publishedEvents = [];
        denorm.onEvent(function (evt) {
          publishedEvents.push(evt);
        });

        var publishedNotis = [];
        denorm.onNotification(function (noti) {
          publishedNotis.push(noti);
        });

        var evt = {
          id: 'evtId',
          commandId: 'cmdId',
          event: 'commandRejected',
          payload: {
            id: '12342',
            reason: {
              name: 'AggregateDestroyedError',
              aggregateId: '12342',
              aggregateRevision: 6
            }
          },
          head: {
            revision: 6,
            version: 2,
            userId: 'userId'
          }
        };

        var eventMissingCalled = false;
        denorm.onEventMissing(function (info, e) {
          eventMissingCalled = true;
        });

        denorm.handle(evt, function (errs, e, notis) {
          expect(errs).not.to.be.ok();
          expect(e).to.eql(evt);
          expect(notis.length).to.eql(0);
          expect(publishedEvents.length).to.eql(0);
          expect(publishedNotis.length).to.eql(0);
          expect(eventMissingCalled).to.eql(false);
          done();
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

## File: `test/integration/fixture/set1/eventExtender.js`
```javascript
// or only with callback (async) (this event extender could be saved collection independent)
module.exports = require('../../../../index').defineEventExtender({
//module.exports = require('cqrs-eventdenormalizer').defineEventExtender({
  name: '', // optional, default is file name without extension, if name is '' it will handle all events that matches
//  aggregate: 'employee', // optional
//  context: 'hr',         // optional
  version: -1 // optional, default is 0, if -1 every version is accepted
}, function (evt, callback) {
  evt.extendedDefault = true;
  callback(null, evt);
});
```

## File: `test/integration/fixture/set1/person/collection.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
module.exports = require('../../../../../index').defineCollection({
//module.exports = require('cqrs-eventdenormalizer').defineCollection({
    name: 'person' // optional, default is folder name
//  defaultPayload: 'payload',
//    indexes: [ // for mongodb
//      'profileId',
//      // or:
//      { profileId: 1 },
//      // or:
//      { index: {profileId: 1}, options: {} }
//    ]
  }//,

// optionally, define some initialization data for new view models...
//  {
//    emails: ['default@mycomp.org'],
//    phoneNumbers: []
//  }
);
```

## File: `test/integration/fixture/set1/person/eventExtenders/enteredNewPerson.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
module.exports = require('../../../../../../index').defineEventExtender({
//module.exports = require('cqrs-eventdenormalizer').defineEventExtender({
  name: 'enteredNewPerson', // optional, default is file name without extension, if name is '' it will handle all events that matches
  aggregate: 'person', // optional
  context: 'hr',         // optional
  version: 2 // optional, default is 0
}, function (evt, col, callback) {
  // col.loadViewModel()... or from somewhere else... (col.findViewModels())
  evt.extended = true;
  callback(null, evt);
});
```

## File: `test/integration/fixture/set1/person/eventExtenders/enteredNewPerson_preExt.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
module.exports = require('../../../../../../index').definePreEventExtender({
//module.exports = require('cqrs-eventdenormalizer').defineEventExtender({
  name: 'enteredNewPerson', // optional, default is file name without extension, if name is '' it will handle all events that matches
  aggregate: 'person', // optional
  context: 'hr',         // optional
  version: 2 // optional, default is 0
}, function (evt, col, callback) {
  // col.loadViewModel()... or from somewhere else... (col.findViewModels())
  evt.preExtended = true;
  callback(null, evt);
});
```

## File: `test/integration/fixture/set1/person/viewBuilders/enteredNewPerson.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
module.exports = require('../../../../../../index').defineViewBuilder({
//module.exports = require('cqrs-eventdenormalizer').defineViewBuilder({
  name: 'enteredNewPerson', // optional, default is file name without extension, if name is '' it will handle all events that matches
  aggregate: 'person', // optional
  context: 'hr',         // optional
  version: 2, // optional, default is 0
  id: 'aggregate.id', // if not defined or not found it will generate a new viewmodel with new id
  payload: '', // optional, if not defined it will pass the whole event...
  priority: 10 // optional, default Infinity
}, function (evt, vm) { // instead of function you can define a string with default handling ('create', 'update', 'delete')
  vm.set('firstname', evt.payload.firstname);
  vm.set('lastname', evt.payload.lastname);
  var ho = { obj: { test: 'a' } };
  vm.set('ref', ho);
  vm.set('abc', undefined);
  vm.set('deeper.two', undefined);
  vm.set('copy', ho.obj);
  if (evt.preExtended) {
    vm.set('wasExtendedByPreExtender', true);
  }
});
```

## File: `test/integration/fixture/set1/person/viewBuilders/personLeaved.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
module.exports = require('../../../../../../index').defineViewBuilder({
//module.exports = require('cqrs-eventdenormalizer').defineViewBuilder({
//  name: 'personLeaved', // optional, default is file name without extension, if name is '' it will handle all events that matches
  aggregate: 'person', // optional
  context: 'hr',         // optional
  // version: 2, // optional, default is 0
  id: 'aggregate.id', // if not defined or not found it will generate a new viewmodel with new id
  payload: 'payload', // optional, if not defined it will pass the whole event...
  priority: 1000 // optional, default Infinity
}, function (data, vm) {
  vm.set('sp', data.special);
  this.remindMe({ that: data.special });
//}).onAfterCommit(function (evt, vm) {
  //var memories = this.getReminder();
  //console.log(memories.that); // 'important value'
  //doSomethingStrange()
//});
// or
}).onAfterCommit(function (evt, vm, callback) {
  var memories = this.getReminder();
  //console.log(memories.that); // 'important value'
  // doSomethingStrange(callback)
  callback(memories.that === 'important value' ? null : new Error('important value not set'));
});
```

## File: `test/integration/fixture/set1/person/viewBuilders/registeredEMailAddress.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
module.exports = require('../../../../../../index').defineViewBuilder({
//module.exports = require('cqrs-eventdenormalizer').defineViewBuilder({
//  name: 'registeredEMailAddress', // optional, default is file name without extension, if name is '' it will handle all events that matches
  aggregate: 'person', // optional
  context: 'hr',         // optional
  version: 2, // optional, default is 0
  query: {},
  payload: 'payload', // optional, if not defined it will pass the whole event...
  priority: 100 // optional, default Infinity
}, function (data, vm) {
  vm.set('generalEmail', data.email);
  vm.get('copy').added = 'new';
  var incr = vm.get('incr') || 0;
  incr++;
  vm.set('incr', incr);
});
```

## File: `test/integration/fixture/set1/personDetail/collection.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
module.exports = require('../../../../../index').defineCollection({
//module.exports = require('cqrs-eventdenormalizer').defineCollection({
//  name: 'personDetail' // optional, default is folder name
//  defaultPayload: 'payload',
//    indexes: [ // for mongodb
//      'profileId',
//      // or:
//      { profileId: 1 },
//      // or:
//      { index: {profileId: 1}, options: {} }
//    ]
},

// optionally, define some initialization data for new view models...
{
  emails: ['default@mycomp.org'],
  phoneNumbers: []
});
```

## File: `test/integration/fixture/set1/personDetail/viewBuilders/blockedEmail.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
module.exports = require('../../../../../../index').defineViewBuilder({
  //module.exports = require('cqrs-eventdenormalizer').defineViewBuilder({
    name: 'blockedEmail', // optional, default is file name without extension, if name is '' it will handle all events that matches
    aggregate: 'person', // optional
    context: 'hr',         // optional
    version: 0, // optional, default is 0
    payload: 'payload' // optional, if not defined it will pass the whole event...
  }, function (data, vm) {
    vm.set('blocked', true);
  }).useAsQuery(function (evt) {
    return { email: evt.payload.email };
  });
  
```

## File: `test/integration/fixture/set1/personDetail/viewBuilders/enteredNewPerson.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
module.exports = require('../../../../../../index').defineViewBuilder({
//module.exports = require('cqrs-eventdenormalizer').defineViewBuilder({
  name: 'enteredNewPerson', // optional, default is file name without extension, if name is '' it will handle all events that matches
  aggregate: 'person', // optional
  context: 'hr',         // optional
  version: 2, // optional, default is 0
  id: 'aggregate.id', // if not defined or not found it will generate a new viewmodel with new id
  payload: 'payload', // optional, if not defined it will pass the whole event...
  priority: 20 // optional, default Infinity
}, 'create');
```

## File: `test/integration/fixture/set1/personDetail/viewBuilders/exitedPerson.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
module.exports = require('../../../../../../index').defineViewBuilder({
  //module.exports = require('cqrs-eventdenormalizer').defineViewBuilder({
    name: 'exitedPerson', // optional, default is file name without extension, if name is '' it will handle all events that matches
    aggregate: 'person', // optional
    context: 'hr',         // optional
    version: 0, // optional, default is 0
    id: 'aggregate.id', // if not defined or not found it will generate a new viewmodel with new id
    payload: 'payload', // optional, if not defined it will pass the whole event...
    priority: 20 // optional, default Infinity
  }, 'delete');
  
```

## File: `test/integration/fixture/set1/personDetail/viewBuilders/registeredEMailAddress.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
module.exports = require('../../../../../../index').defineViewBuilder({
//module.exports = require('cqrs-eventdenormalizer').defineViewBuilder({
//  name: 'registeredEMailAddress', // optional, default is file name without extension, if name is '' it will handle all events that matches
  aggregate: 'person', // optional
  context: 'hr',         // optional
  version: 2, // optional, default is 0
  id: 'aggregate.id', // if not defined or not found it will generate a new viewmodel with new id
  payload: 'payload', // optional, if not defined it will pass the whole event...
  priority: 200 // optional, default Infinity
}, function (data, vm, callback) {
  if (vm.actionOnCommit === 'create') {
    return callback(new Error('should not happen!'));
  }

  vm.set(data);
  callback();
});
```

## File: `test/integration/fixture/set2/eventExtender.js`
```javascript
// or only with callback (async) (this event extender could be saved collection independent)
module.exports = require('../../../../index').defineEventExtender({
//module.exports = require('cqrs-eventdenormalizer').defineEventExtender({
  name: '', // optional, default is file name without extension, if name is '' it will handle all events that matches
//  aggregate: 'employee', // optional
//  context: 'hr',         // optional
  version: -1 // optional, default is 0, if -1 every version is accepted
}, function (evt, callback) {
  evt.extendedDefault = true;
  callback(null, evt);
});
```

## File: `test/integration/fixture/set2/person/collection.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
module.exports = require('../../../../../index').defineCollection({
//module.exports = require('cqrs-eventdenormalizer').defineCollection({
    name: 'person' // optional, default is folder name
//  defaultPayload: 'payload',
//    indexes: [ // for mongodb
//      'profileId',
//      // or:
//      { profileId: 1 },
//      // or:
//      { index: {profileId: 1}, options: {} }
//    ]
  }//,

// optionally, define some initialization data for new view models...
//  {
//    emails: ['default@mycomp.org'],
//    phoneNumbers: []
//  }
);
```

## File: `test/integration/fixture/set2/person/eventExtenders/enteredNewPerson.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
module.exports = require('../../../../../../index').defineEventExtender({
//module.exports = require('cqrs-eventdenormalizer').defineEventExtender({
  name: 'enteredNewPerson', // optional, default is file name without extension, if name is '' it will handle all events that matches
//  aggregate: 'person', // optional
//  context: 'hr',         // optional
  version: 2 // optional, default is 0
}, function (evt, col, callback) {
  // col.loadViewModel()... or from somewhere else... (col.findViewModels())
  evt.extended = true;
  callback(null, evt);
});
```

## File: `test/integration/fixture/set2/person/viewBuilders/enteredNewPerson.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
module.exports = require('../../../../../../index').defineViewBuilder({
//module.exports = require('cqrs-eventdenormalizer').defineViewBuilder({
  name: 'enteredNewPerson', // optional, default is file name without extension, if name is '' it will handle all events that matches
//  aggregate: 'person', // optional
//  context: 'hr',         // optional
  version: 2, // optional, default is 0
  id: 'payload.id', // if not defined or not found it will generate a new viewmodel with new id
  payload: 'payload', // optional, if not defined it will pass the whole event...
  priority: 10 // optional, default Infinity
}, function (data, vm) { // instead of function you can define a string with default handling ('create', 'update', 'delete')
  vm.set('firstname', data.firstname);
  vm.set('lastname', data.lastname);
});
```

## File: `test/integration/fixture/set2/personDetail/collection.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
module.exports = require('../../../../../index').defineCollection({
//module.exports = require('cqrs-eventdenormalizer').defineCollection({
//  name: 'personDetail' // optional, default is folder name
//  defaultPayload: 'payload',
//    indexes: [ // for mongodb
//      'profileId',
//      // or:
//      { profileId: 1 },
//      // or:
//      { index: {profileId: 1}, options: {} }
//    ]
},

// optionally, define some initialization data for new view models...
{
  emails: ['default@mycomp.org'],
  phoneNumbers: []
});
```

## File: `test/integration/fixture/set2/personDetail/viewBuilders/enteredNewPerson.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
module.exports = require('../../../../../../index').defineViewBuilder({
//module.exports = require('cqrs-eventdenormalizer').defineViewBuilder({
  name: 'enteredNewPerson', // optional, default is file name without extension, if name is '' it will handle all events that matches
//  aggregate: 'person', // optional
//  context: 'hr',         // optional
  version: 2, // optional, default is 0
  id: 'payload.id', // if not defined or not found it will generate a new viewmodel with new id
  payload: 'payload', // optional, if not defined it will pass the whole event...
  priority: 11 // optional, default Infinity
}, 'create');
```

## File: `test/integration/fixture/set2/personDetail/viewBuilders/registeredEMailAddress.js`
```javascript
// if exports is an array, it will be the same like loading multiple files...
module.exports = require('../../../../../../index').defineViewBuilder({
//module.exports = require('cqrs-eventdenormalizer').defineViewBuilder({
//  name: 'registeredEMailAddress', // optional, default is file name without extension, if name is '' it will handle all events that matches
//  aggregate: 'person', // optional
//  context: 'hr',         // optional
  version: 2, // optional, default is 0
  id: 'payload.id', // if not defined or not found it will generate a new viewmodel with new id
  payload: 'payload' // optional, if not defined it will pass the whole event...
}, 'update');
```

## File: `test/unit/denormalizerTest.js`
```javascript
var expect = require('expect.js'),
  api = require('../../index'),
  EventExtender = require('../../lib/definitions/eventExtender');
  _ = require('lodash');

describe('denormalizer', function () {

  it('it should be a function', function () {

    expect(api).to.be.a('function');

  });

  it('it should have the correct api', function () {

    expect(api.defineViewBuilder).to.be.a('function');
    expect(api.defineEventExtender).to.be.a('function');
    expect(api.defineCollection).to.be.a('function');

  });

  describe('calling that function', function () {

    describe('without options', function () {

      it('it should throw an error', function () {

        expect(api).to.throwError('/denormalizerPath/');

      });

    });

    describe('with all mandatory options', function () {

      it('it should return as expected', function () {

        var denorm = api({ denormalizerPath: __dirname });
        expect(denorm).to.be.a('object');
        expect(denorm.on).to.be.a('function');
        expect(denorm.structureLoader).to.be.a('function');
        expect(denorm.revisionGuardStore).to.be.an('object');
        expect(denorm.revisionGuardStore.on).to.be.a('function');
        expect(denorm.repository).to.be.an('object');
        expect(denorm.repository.on).to.be.a('function');
        expect(denorm.defineNotification).to.be.a('function');
        expect(denorm.defineEvent).to.be.a('function');
        expect(denorm.idGenerator).to.be.a('function');
        expect(denorm.onEvent).to.be.a('function');
        expect(denorm.onNotification).to.be.a('function');
        expect(denorm.onEventMissing).to.be.a('function');
        expect(denorm.defaultEventExtension).to.be.a('function');
        expect(denorm.init).to.be.a('function');
        expect(denorm.handle).to.be.a('function');
        expect(denorm.getLastEvent).to.be.a('function');

        expect(denorm.options.retryOnConcurrencyTimeout).to.eql(800);
        expect(denorm.options.commandRejectedEventName).to.eql('commandRejected');
        expect(denorm.options.revisionGuard.queueTimeout).to.eql(1000);
        expect(denorm.options.revisionGuard.queueTimeoutMaxLoops).to.eql(3);

      });

    });

    describe('with custom "structureLoader" method', function () {

      describe('creating an object of the wrong interface', function () {

        it('it should throw an error', function () {

          expect(function () {
            api({
              domainPath: __dirname,
              structureLoader: {
              },
            })
          }).to.throwError('/structureLoader/');

        });
      });

      describe('creating an object of the right interface', function () {

        it('it should return as expected', function () {

          var denorm = api({
            denormalizerPath: __dirname,
            structureLoader: function() {
            }
          });

          expect(denorm).to.be.a('object');
          expect(denorm.on).to.be.a('function');
          expect(denorm.structureLoader).to.be.a('function');
          expect(denorm.revisionGuardStore).to.be.an('object');
          expect(denorm.revisionGuardStore.on).to.be.a('function');
          expect(denorm.repository).to.be.an('object');
          expect(denorm.repository.on).to.be.a('function');
          expect(denorm.defineNotification).to.be.a('function');
          expect(denorm.defineEvent).to.be.a('function');
          expect(denorm.idGenerator).to.be.a('function');
          expect(denorm.onEvent).to.be.a('function');
          expect(denorm.onNotification).to.be.a('function');
          expect(denorm.onEventMissing).to.be.a('function');
          expect(denorm.defaultEventExtension).to.be.a('function');
          expect(denorm.init).to.be.a('function');
          expect(denorm.handle).to.be.a('function');
          expect(denorm.getLastEvent).to.be.a('function');

          expect(denorm.options.retryOnConcurrencyTimeout).to.eql(800);
          expect(denorm.options.commandRejectedEventName).to.eql('commandRejected');
          expect(denorm.options.revisionGuard.queueTimeout).to.eql(1000);
          expect(denorm.options.revisionGuard.queueTimeoutMaxLoops).to.eql(3);
        });
      });
    });

    describe('defining an id generator function', function () {

      var denorm;

      beforeEach(function () {
        denorm = api({ denormalizerPath: __dirname });
        denorm.getNewId = null;
      });

      describe('in a synchronous way', function () {

        it('it should be transformed internally to an asynchronous way', function (done) {

          denorm.idGenerator(function () {
            var id = require('uuid').v4().toString();
            return id;
          });

          denorm.getNewId(function (err, id) {
            expect(id).to.be.a('string');
            done();
          });

        });

      });

      describe('in an synchronous way', function () {

        it('it should be taken as it is', function (done) {

          denorm.idGenerator(function (callback) {
            setTimeout(function () {
              var id = require('uuid').v4().toString();
              callback(null, id);
            }, 10);
          });

          denorm.getNewId(function (err, id) {
            expect(id).to.be.a('string');
            done();
          });

        });

      });

    });

    describe('defining the event structure', function() {

      var denorm;

      beforeEach(function () {
        denorm = api({ denormalizerPath: __dirname });
      });

      describe('using the defaults', function () {

        it('it should apply the defaults', function() {

          var defaults = _.cloneDeep(denorm.definitions.event);

          denorm.defineEvent({
            payload: 'data',
            aggregate: 'aggName',
            context: 'ctx.Name',
            revision: 'rev',
            version: 'v.',
            meta: 'pass'
          });

          expect(defaults.correlationId).to.eql(denorm.definitions.event.correlationId);
          expect(defaults.id).to.eql(denorm.definitions.event.id);
          expect(denorm.definitions.event.payload).to.eql('data');
          expect(defaults.payload).not.to.eql(denorm.definitions.event.payload);
          expect(defaults.name).to.eql(denorm.definitions.event.name);
          expect(defaults.aggregateId).to.eql(denorm.definitions.event.aggregateId);
          expect(denorm.definitions.event.aggregate).to.eql('aggName');
          expect(defaults.aggregate).not.to.eql(denorm.definitions.event.aggregate);
          expect(denorm.definitions.event.context).to.eql('ctx.Name');
          expect(defaults.context).not.to.eql(denorm.definitions.event.context);
          expect(denorm.definitions.event.revision).to.eql('rev');
          expect(defaults.revision).not.to.eql(denorm.definitions.event.revision);
          expect(denorm.definitions.event.version).to.eql('v.');
          expect(defaults.version).not.to.eql(denorm.definitions.event.version);
          expect(denorm.definitions.event.meta).to.eql('pass');
          expect(defaults.meta).not.to.eql(denorm.definitions.event.meta);

        });

      });

      describe('overwriting the defaults', function () {

        it('it should apply them correctly', function() {

          var defaults = _.cloneDeep(denorm.definitions.event);

          denorm.defineEvent({
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


          expect(denorm.definitions.event.correlationId).to.eql('cmdId');
          expect(defaults.correlationId).not.to.eql(denorm.definitions.event.correlationId);
          expect(denorm.definitions.event.id).to.eql('eventId');
          expect(defaults.id).not.to.eql(denorm.definitions.event.id);
          expect(denorm.definitions.event.payload).to.eql('data');
          expect(defaults.payload).not.to.eql(denorm.definitions.event.payload);
          expect(denorm.definitions.event.name).to.eql('defName');
          expect(defaults.name).not.to.eql(denorm.definitions.event.name);
          expect(denorm.definitions.event.aggregateId).to.eql('path.to.aggId');
          expect(defaults.aggregateId).not.to.eql(denorm.definitions.event.aggregateId);
          expect(denorm.definitions.event.aggregate).to.eql('aggName');
          expect(defaults.aggregate).not.to.eql(denorm.definitions.event.aggregate);
          expect(denorm.definitions.event.context).to.eql('ctx.Name');
          expect(defaults.context).not.to.eql(denorm.definitions.event.context);
          expect(denorm.definitions.event.revision).to.eql('rev');
          expect(defaults.revision).not.to.eql(denorm.definitions.event.revision);
          expect(denorm.definitions.event.version).to.eql('v.');
          expect(defaults.version).not.to.eql(denorm.definitions.event.version);
          expect(denorm.definitions.event.meta).to.eql('pass');
          expect(defaults.meta).not.to.eql(denorm.definitions.event.meta);

        });

      });

    });

    describe('defining the notification structure', function() {

      var denorm;

      beforeEach(function () {
        denorm = api({ denormalizerPath: __dirname });
      });

      describe('using the defaults', function () {

        it('it should apply the defaults', function() {

          var defaults = _.cloneDeep(denorm.definitions.notification);

          denorm.defineNotification({
            collection: 'col',
            payload: 'data',
            context: 'meta.context.name',
            aggregate: 'meta.aggregate.name'
          });

          expect(defaults.correlationId).to.eql(denorm.definitions.notification.correlationId);
          expect(defaults.id).to.eql(denorm.definitions.notification.id);
          expect(denorm.definitions.notification.payload).to.eql('data');
          expect(defaults.payload).not.to.eql(denorm.definitions.notification.payload);
          expect(denorm.definitions.notification.collection).to.eql('col');
          expect(defaults.collection).not.to.eql(denorm.definitions.notification.collection);
          expect(denorm.definitions.notification.context).to.eql('meta.context.name');
          expect(defaults.context).not.to.eql(denorm.definitions.notification.context);
          expect(denorm.definitions.notification.aggregate).to.eql('meta.aggregate.name');
          expect(defaults.aggregate).not.to.eql(denorm.definitions.notification.aggregate);
          expect(defaults.action).to.eql(denorm.definitions.notification.action);
          expect(defaults.meta).to.eql(denorm.definitions.notification.meta);

        });

      });

      describe('overwriting the defaults', function () {

        it('it should apply them correctly', function() {

          var defaults = _.cloneDeep(denorm.definitions.notification);

          denorm.defineNotification({
            correlationId: 'corrId',
            id: 'notId',
            action: 'n',
            collection: 'c',
            payload: 'p',
            context: 'ctx',
            aggregate: 'agg',
            aggregateId: 'aggId',
            revision: 'rev',
            eventId: 'evtId',
            event: 'evtName',
            meta: 'm'
          });

          expect(denorm.definitions.notification.correlationId).to.eql('corrId');
          expect(defaults.correlationId).not.to.eql(denorm.definitions.notification.correlationId);
          expect(denorm.definitions.notification.id).to.eql('notId');
          expect(defaults.id).not.to.eql(denorm.definitions.notification.id);
          expect(denorm.definitions.notification.action).to.eql('n');
          expect(defaults.action).not.to.eql(denorm.definitions.notification.action);
          expect(denorm.definitions.notification.collection).to.eql('c');
          expect(defaults.collection).not.to.eql(denorm.definitions.notification.collection);
          expect(denorm.definitions.notification.payload).to.eql('p');
          expect(defaults.payload).not.to.eql(denorm.definitions.notification.payload);
          expect(denorm.definitions.notification.context).to.eql('ctx');
          expect(defaults.context).not.to.eql(denorm.definitions.notification.context);
          expect(denorm.definitions.notification.aggregate).to.eql('agg');
          expect(defaults.aggregate).not.to.eql(denorm.definitions.notification.aggregate);
          expect(denorm.definitions.notification.aggregateId).to.eql('aggId');
          expect(defaults.aggregateId).not.to.eql(denorm.definitions.notification.aggregateId);
          expect(denorm.definitions.notification.revision).to.eql('rev');
          expect(defaults.revision).not.to.eql(denorm.definitions.notification.revision);
          expect(denorm.definitions.notification.eventId).to.eql('evtId');
          expect(defaults.eventId).not.to.eql(denorm.definitions.notification.eventId);
          expect(denorm.definitions.notification.event).to.eql('evtName');
          expect(defaults.event).not.to.eql(denorm.definitions.notification.event);
          expect(denorm.definitions.notification.meta).to.eql('m');
          expect(defaults.meta).not.to.eql(denorm.definitions.notification.meta);

        });

      });

    });

    describe('defining onEvent handler', function () {

      var denorm;

      describe('in a synchronous way', function() {

        it('it should be transformed internally to an asynchronous way', function(done) {
          denorm = api({ denormalizerPath: __dirname });
          denorm.onEventHandle = null;

          var called = false;
          denorm.onEvent(function (evt) {
            expect(evt.my).to.eql('evt');
            called = true;
          });

          denorm.onEventHandle({ my: 'evt' }, function (err) {
            expect(err).not.to.be.ok();
            expect(called).to.eql(true);
            done();
          });

        });

      });

      describe('in an synchronous way', function() {

        it('it should be taken as it is', function(done) {
          denorm = api({ denormalizerPath: __dirname });
          denorm.onEventHandle = null;

          var called = false;
          denorm.onEvent(function (evt, callback) {
            setTimeout(function () {
              expect(evt.my).to.eql('evt');
              called = true;
              callback(null);
            }, 10);
          });

          denorm.onEventHandle({ my: 'evt' }, function (err) {
            expect(err).not.to.be.ok();
            expect(called).to.eql(true);
            done();
          });

        });

      });

      describe('in an synchronous way', function() {

        it('it should not be called beause we want to skip it', function(done) {
          denorm = api({ denormalizerPath: __dirname, skipOnEvent: true });
          denorm.onEventHandle = null;

          var called = false;
          denorm.onEvent(function (evt, callback) {
            called = true;
            callback(null);
          });

          denorm.onEventHandle({ my: 'evt' }, function (err) {
            expect(err).not.to.be.ok();
            expect(called).to.eql(false);
            done();
          });

        });

      });

    });

    describe('defining onNotification handler', function () {

      var denorm;

      describe('in a synchronous way', function() {

        it('it should be transformed internally to an asynchronous way', function(done) {
          denorm = api({ denormalizerPath: __dirname });
          denorm.onNotificationHandle = null;

          var called = false;
          denorm.onNotification(function (noti) {
            expect(noti.my).to.eql('n');
            called = true;
          });

          denorm.onNotificationHandle({ my: 'n' }, function (err) {
            expect(err).not.to.be.ok();
            expect(called).to.eql(true);
            done();
          });

        });

      });

      describe('in an synchronous way', function() {

        it('it should be taken as it is', function(done) {
          denorm = api({ denormalizerPath: __dirname });
          denorm.onNotificationHandle = null;

          var called = false;
          denorm.onNotification(function (noti, callback) {
            setTimeout(function () {
              expect(noti.my).to.eql('n');
              called = true;
              callback(null);
            }, 10);
          });

          denorm.onNotificationHandle({ my: 'n' }, function (err) {
            expect(err).not.to.be.ok();
            expect(called).to.eql(true);
            done();
          });

        });

      });

      describe('in an synchronous way', function() {

        it('it should not be called becuase we want to skip it', function(done) {
          denorm = api({ denormalizerPath: __dirname, skipOnNotification: true });
          denorm.onNotificationHandle = null;

          var called = false;
          denorm.onNotification(function (noti, callback) {
            called = true;
            callback(null);
          });

          denorm.onNotificationHandle({ my: 'n' }, function (err) {
            expect(err).not.to.be.ok();
            expect(called).to.eql(false);
            done();
          });

        });

      });

    });

    describe('defining onEventMissing handler', function () {

      var denorm;

      describe('without skipping the onEventMissing handler', function () {
        it('it should work as expected', function() {
          denorm = api({ denormalizerPath: __dirname });
          denorm.onEventMissingHandle = null;

          var called = false;
          denorm.onEventMissing(function (info, evt) {
            expect(info.in).to.eql('fo');
            expect(evt.my).to.eql('evt');
            called = true;
          });

          denorm.onEventMissingHandle({ in: 'fo' }, { my: 'evt' });
          expect(called).to.eql(true);

        });
      })

      describe('with skipping the onEventMissing handler', function() {
        it('it should work as expected', function() {
          denorm = api({ denormalizerPath: __dirname, skipOnEventMissing: true });
          denorm.onEventMissingHandle = null;

          var called = false;
          denorm.onEventMissing(function (info, evt) {
            called = true;
          });

          denorm.onEventMissingHandle({ in: 'fo' }, { my: 'evt' });
          expect(called).to.eql(false);

        });
      })

    });

    describe('defining defaultEventExtension handler', function () {

      var denorm;


      describe('in a synchronous way', function() {

        it('it should be transformed internally to an asynchronous way', function(done) {
          denorm = api({ denormalizerPath: __dirname });
          denorm.extendEventHandle = null;

          var called = false;
          denorm.defaultEventExtension(function (evt) {
            expect(evt.my).to.eql('evt');
            called = true;
          });

          denorm.extendEventHandle({ my: 'evt' }, function (err) {
            expect(err).not.to.be.ok();
            expect(called).to.eql(true);
            done();
          });

        });

      });

      describe('in an synchronous way', function() {

        it('it should be taken as it is', function(done) {
          denorm = api({ denormalizerPath: __dirname });
          denorm.extendEventHandle = null;

          var called = false;
          denorm.defaultEventExtension(function (evt, callback) {
            setTimeout(function () {
              expect(evt.my).to.eql('evt');
              called = true;
              callback(null);
            }, 10);
          });

          denorm.extendEventHandle({ my: 'evt' }, function (err) {
            expect(err).not.to.be.ok();
            expect(called).to.eql(true);
            done();
          });

        });

      });

      describe('in a synchronous way', function() {

        it('it should be skipped', function(done) {
          denorm = api({ denormalizerPath: __dirname, skipExtendEvent: true });
          denorm.extendEventHandle = null;

          var called = false;
          denorm.defaultEventExtension(function (evt) {
            called = true;
          });

          denorm.extendEventHandle({ my: 'evt' }, function (err) {
            expect(err).not.to.be.ok();
            expect(called).to.eql(false);
            done();
          });

        });

      });


    });

    describe('initializing', function () {

      var denorm;

      beforeEach(function () {
        denorm = api({ denormalizerPath: __dirname });
        denorm.defineNotification({
          correlationId: 'corrId',
          id: 'notId',
          action: 'n',
          collection: 'c',
          payload: 'p',
          context: 'ctx',
          aggregate: 'agg',
          aggregateId: 'aggId',
          revision: 'rev',
          eventId: 'evtId',
          event: 'evtName',
          meta: 'm'
        });
        denorm.defineEvent({
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
          denorm.revisionGuardStore.once('connect', function () {
            called++;
          });
          denorm.repository.once('connect', function () {
            called++;
          });
          denorm.once('connect', function () {
            called++;
          });

          denorm.init(function (err) {
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

          denorm.revisionGuardStore.once('connect', function () {
            check();
          });
          denorm.repository.once('connect', function () {
            check();
          });
          denorm.once('connect', function () {
            check();
          });

          denorm.init();

        });

      });

    });

    describe('calling extendEvent', function () {

      var denorm;

      describe('having found only the default event extender', function () {

        it('it should work as expected', function (done) {
          denorm = api({ denormalizerPath: __dirname });

          denorm.defaultEventExtension(function (evt) {
            evt.ext++;
            return evt;
          });

          denorm.eventDispatcher = {
            getTargetInformation: function (e) {
              expect(e.ext).to.eql(1);
              return 'target';
            }
          };

          denorm.tree = {
            getEventExtender: function (t) {
              expect(t).to.eql('target');

              return null;
            }
          };

          denorm.extendEvent({ ext: 0 }, function (err, extEvt) {
            expect(err).not.to.be.ok();
            expect(extEvt.ext).to.eql(1);
            done();
          });

        });

      });

      describe('having found the default event extender and an other one', function () {

        it('it should work as expected', function (done) {
          denorm = api({ denormalizerPath: __dirname });

          denorm.defaultEventExtension(function (evt) {
            evt.ext++;
            return evt;
          });

          denorm.eventDispatcher = {
            getTargetInformation: function (e) {
              expect(e.ext).to.eql(1);
              return 'target';
            }
          };

          denorm.tree = {
            getEventExtender: function (t) {
              expect(t).to.eql('target');

              return {
                extend: function (e, clb) {
                  expect(e.ext).to.eql(1);
                  e.ext++;
                  clb(null, e);
                }
              };
            }
          };

          denorm.extendEvent({ ext: 0 }, function (err, extEvt) {
            expect(err).not.to.be.ok();
            expect(extEvt.ext).to.eql(2);
            done();
          });

        });

      });

      describe('having found the default event extender and an other one that that should be skipped', function () {

        it('it should skip the default event extender and the extender', function (done) {
          denorm = api({ denormalizerPath: __dirname, skipExtendEvent: true });

          denorm.defaultEventExtension(function (evt) {
            evt.ext++;
            return evt;
          });

          denorm.eventDispatcher = {
            getTargetInformation: function (e) {
              expect(e.ext).to.eql(0);
              return 'target';
            }
          };

          denorm.tree = {
            getEventExtender: function (t) {
              expect(t).to.eql('target');

              function extendEvtFn(evt) {
                evt.ext++;
              }

              return new EventExtender(null, extendEvtFn);
            }
          };

          denorm.extendEvent({ ext: 0 }, function (err, extEvt) {
            expect(err).not.to.be.ok();
            expect(extEvt.ext).to.eql(0);
            done();
          });

        });

      });

    });

    describe('calling isCommandRejected', function () {

      var denorm;

      beforeEach(function () {
        denorm = api({ denormalizerPath: __dirname, commandRejectedEventName: 'reji' });
      });

      describe('with a normal event', function () {

        it('it should work as expected', function (done) {

          var calledClb = false;
          var res = denorm.isCommandRejected({ name: 'normal' }, function (err, evt, notifications) {
            calledClb = true;
          });

          expect(res).to.eql(false);

          setTimeout(function () {
            expect(calledClb).to.eql(false);
            done();
          }, 40);

        });

      });

      describe('with a command rejected event', function () {

        describe('not having defined a revision', function () {

          it('it should work as expected', function (done) {

            denorm.defineEvent({
              aggregate: 'aggregate.name',
              context: 'context.name'
            });

            var calledMissing = false;

            denorm.onEventMissing(function (info, evt) {
              expect(info.aggregateId).to.eql('aggId');
              expect(info.aggregateRevision).to.eql(5);
              expect(info.aggregate).to.eql('agg');
              expect(info.context).to.eql('ctx');
              expect(info.guardRevision).not.to.be.ok();
              expect(evt.name).to.eql('reji');
              calledMissing = true;
            });

            var res = denorm.isCommandRejected({
              name: 'reji',
              payload: {
                reason: {
                  name: 'AggregateDestroyedError',
                  aggregateId: 'aggId',
                  aggregateRevision: 5
                }
              },
              aggregate: {
                name: 'agg'
              },
              context: {
                name: 'ctx'
              }
            }, function (err, evt, notifications) {
              expect(err).not.to.be.ok();
              expect(evt.name).to.eql('reji');
              expect(notifications).to.be.an('array');
              expect(notifications.length).to.eql(0);
              expect(calledMissing).to.eql(true);

              done();
            });

            expect(res).to.eql(true);

          });

        });

        describe('having defined a revision', function () {

          describe('and the revisionGuardStore has missed some event', function () {

            it('it should work as expected', function (done) {

              denorm.defineEvent({
                aggregate: 'aggregate.name',
                context: 'context.name',
                revision: 'aggregate.revision'
              });

              var calledMissing = false;

              denorm.onEventMissing(function (info, evt) {
                expect(info.aggregateId).to.eql('aggId');
                expect(info.aggregateRevision).to.eql(5);
                expect(info.aggregate).to.eql('agg');
                expect(info.context).to.eql('ctx');
                expect(info.guardRevision).to.eql(4);
                expect(evt.name).to.eql('reji');
                calledMissing = true;
              });

              var calledStore = false;

              denorm.revisionGuardStore = {
                get: function (aggId, clb) {
                  expect(aggId).to.eql('aggId');
                  calledStore = true;

                  clb(null, 4)
                }
              };

              var res = denorm.isCommandRejected({
                name: 'reji',
                payload: {
                  reason: {
                    name: 'AggregateDestroyedError',
                    aggregateId: 'aggId',
                    aggregateRevision: 5
                  }
                },
                aggregate: {
                  name: 'agg',
                  revision: 2
                },
                context: {
                  name: 'ctx'
                }
              }, function (err, evt, notifications) {
                expect(err).not.to.be.ok();
                expect(evt.name).to.eql('reji');
                expect(notifications).to.be.an('array');
                expect(notifications.length).to.eql(0);
                expect(calledMissing).to.eql(true);
                expect(calledStore).to.eql(true);

                done();
              });

              expect(res).to.eql(true);

            });

          });

          describe('and the revisionGuardStore has not missed anything', function () {

            it('it should work as expected', function (done) {

              denorm.defineEvent({
                aggregate: 'aggregate.name',
                context: 'context.name',
                revision: 'aggregate.revision'
              });

              var calledMissing = false;

              denorm.onEventMissing(function (info, evt) {
                calledMissing = true;
              });

              var calledStore = false;

              denorm.revisionGuardStore = {
                get: function (aggId, clb) {
                  expect(aggId).to.eql('aggId');
                  calledStore = true;

                  clb(null, 6)
                }
              };

              var res = denorm.isCommandRejected({
                name: 'reji',
                payload: {
                  reason: {
                    name: 'AggregateDestroyedError',
                    aggregateId: 'aggId',
                    aggregateRevision: 5
                  }
                },
                aggregate: {
                  name: 'agg',
                  revision: 2
                },
                context: {
                  name: 'ctx'
                }
              }, function (err, evt, notifications) {
                expect(err).not.to.be.ok();
                expect(evt.name).to.eql('reji');
                expect(notifications).to.be.an('array');
                expect(notifications.length).to.eql(0);
                expect(calledMissing).to.eql(false);
                expect(calledStore).to.eql(true);

                done();
              });

              expect(res).to.eql(true);

            });

          });

        });

      });

    });

    describe('calling dispatch', function () {

      var denorm;

      beforeEach(function () {
        denorm = api({ denormalizerPath: __dirname });
      });

      it('it should work as expected', function (done) {

        var calledDispatch = false;
        denorm.eventDispatcher = {
          dispatch: function (evt, clb) {
            expect(evt.my).to.eql('evt');
            calledDispatch = true;
            clb(null, [{ noti: '1'}, { noti: '2'}]);
          }
        };

        var calledExtend = false;
        denorm.extendEvent = function (evt, clb) {
          evt.ext++;
          calledExtend = true;
          clb(null, evt);
        };

        var calledPreExtend = false;
        denorm.preExtendEvent = function (evt, clb) {
          evt.ext++;
          calledPreExtend = true;
          clb(null, evt);
        };

        var notiCalled = [];
        denorm.onNotification(function (noti) {
          notiCalled.push(noti);
        });

        var evtCalled = [];
        denorm.onEvent(function (evt) {
          evtCalled.push(evt);
        });

        denorm.dispatch({ my: 'evt', ext: 0 }, function (err, extEvt, notis) {
          expect(err).not.to.be.ok();
          expect(extEvt.ext).to.eql(2);
          expect(notis).to.be.an('array');
          expect(notis.length).to.eql(2);
          expect(notis[0].noti).to.eql(1);
          expect(notis[1].noti).to.eql(2);

          expect(notiCalled.length).to.eql(2);
          expect(notiCalled[0].noti).to.eql(1);
          expect(notiCalled[1].noti).to.eql(2);
          expect(evtCalled.length).to.eql(1);
          expect(evtCalled[0].ext).to.eql(2);

          expect(calledDispatch).to.eql(true);
          expect(calledExtend).to.eql(true);
          expect(calledPreExtend).to.eql(true);
          done();
        });

      });

      it('it should work as expected if pre event extender callback with error', function (done) {

        var calledDispatch = false;
        denorm.eventDispatcher = {
          dispatch: function (evt, clb) {
            expect(evt.my).to.eql('evt');
            calledDispatch = true;
            clb(null, [{ noti: '1'}, { noti: '2'}]);
          }
        };

        var calledPreExtend = false;
        denorm.preExtendEvent = function (evt, clb) {
          evt.ext++;
          calledPreExtend = true;
          clb(new Error('This is an error'), evt);
        };

        var notiCalled = [];
        denorm.onNotification(function (noti) {
          notiCalled.push(noti);
        });

        var evtCalled = [];
        denorm.onEvent(function (evt) {
          evtCalled.push(evt);
        });

        denorm.dispatch({ my: 'evt', ext: 0 }, function (errs, extEvt, notis) {
          expect(errs).to.be.an('array');
          expect(errs.length).to.eql(1);
          expect(errs[0].message).to.eql('This is an error');
          expect(extEvt.ext).to.eql(1);
          expect(notis).to.be.an('array');
          expect(notis.length).to.eql(0);

          expect(notiCalled.length).to.eql(0);

          expect(calledDispatch).to.eql(false);
          expect(calledPreExtend).to.eql(true);
          done();
        });

      });

    });

    describe('calling handle', function () {

      var denorm;

      beforeEach(function () {
        denorm = api({ denormalizerPath: __dirname });
      });

      describe('not working with revisions', function () {

        it('it should work as expected', function (done) {

          denorm.defineEvent({
            name: 'my'
          });

          var cmdRejCalled = false;
          denorm.isCommandRejected = function (evt, clb) {
            expect(evt.my).to.eql('evt');
            cmdRejCalled = true;
            return false;
          };

          var dispCalled = false;
          denorm.dispatch = function (evt, clb) {
            expect(evt.my).to.eql('evt');
            dispCalled = true;
            clb(null, evt, [{ noti: 1 }]);
          };

          var guardCalled = false;
          var guardDoneCalled = false;
          denorm.revisionGuard = {
            guard: function (evt, clb) {
              guardCalled = true;
              clb(null, function (c) {
                guardDoneCalled = true;
                c(null);
              });
            }
          };

          denorm.handle({ my: 'evt' }, function (err, extEvt, notis) {
            expect(err).not.be.ok();
            expect(extEvt.my).to.eql('evt');
            expect(notis).to.be.an('array');
            expect(notis.length).to.eql(1);
            expect(notis[0].noti).to.eql(1);

            expect(cmdRejCalled).to.eql(true);
            expect(dispCalled).to.eql(true);
            expect(guardCalled).to.eql(false);
            expect(guardDoneCalled).to.eql(false);

            done();
          });

        });

      });

      describe('working with revisions', function () {

        it('it should work as expected', function (done) {

          denorm.defineEvent({
            name: 'my',
            aggregate: 'aggregate.name',
            aggregateId: 'aggregate.id',
            revision: 'aggregate.revision'
          });

          var cmdRejCalled = false;
          denorm.isCommandRejected = function (evt, clb) {
            expect(evt.my).to.eql('evt');
            cmdRejCalled = true;
            return false;
          };

          var dispCalled = false;
          denorm.dispatch = function (evt, clb) {
            expect(evt.my).to.eql('evt');
            dispCalled = true;
            clb(null, evt, [{ noti: 1 }]);
          };

          var guardCalled = false;
          var guardDoneCalled = false;
          denorm.revisionGuard = {
            guard: function (evt, clb) {
              expect(evt.my).to.eql('evt');
              guardCalled = true;
              clb(null, function (c) {
                guardDoneCalled = true;
                c(null);
              });
            }
          };

          denorm.handle({ my: 'evt', aggregate: { id: 'aggId', name: 'agg', revision: 4 } }, function (err, extEvt, notis) {
            expect(err).not.be.ok();
            expect(extEvt.my).to.eql('evt');
            expect(notis).to.be.an('array');
            expect(notis.length).to.eql(1);
            expect(notis[0].noti).to.eql(1);

            expect(cmdRejCalled).to.eql(true);
            expect(dispCalled).to.eql(true);
            expect(guardCalled).to.eql(true);
            expect(guardDoneCalled).to.eql(true);

            done();
          });

        });

      });

    });

    describe('calling replay', function () {

      var denorm;

      beforeEach(function () {
        denorm = api({ denormalizerPath: __dirname });
      });

      it('it should work as expected', function (done) {

        var events = [{ evt: 1 }, { evt: 2 }];
        var callback = function () {
        };

        denorm.replayHandler = {
          replay: function (evts, clb) {
            expect(evts).to.eql(events);
            expect(clb).to.eql(callback);
            done();
          }
        };

        denorm.replay(events, callback);

      });

    });

    describe('calling replayStreamed', function () {

      var denorm;

      beforeEach(function () {
        denorm = api({ denormalizerPath: __dirname });
      });

      it('it should work as expected', function (done) {

        var replFn = function () {
        };

        denorm.replayHandler = {
          replayStreamed: function (fn) {
            expect(fn).to.eql(replFn);
            done();
          }
        };

        denorm.replayStreamed(replFn);

      });

    });

  });

  describe('loading custom structure', function() {
    it('it should return as expected', function(done) {
      var denorm = api({
        denormalizerPath: __dirname,
        structureLoader: function(options) {
          const collection = new options.definitions.Collection({
            name: 'col'
          });
          collection.addViewBuilder(new options.definitions.ViewBuilder({
            name: 'evt',
            aggregate: 'agg',
            context: 'ctx'
          }, function() {}));

          return {
            collections: [
              collection
            ]
          }
        },
      });

      denorm.init(function() {
        var collections = denorm.getInfo().collections;
        expect(collections.length).to.eql(1);
        expect(collections[0].name).to.eql('col');
        expect(collections[0].viewBuilders.length).to.eql(1);
        expect(collections[0].viewBuilders[0].name).to.eql('evt');
        done();
      });

    });
  });
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
          new EventDispatcher({ getViewBuilders: function () {} });
        }).to.throwError(/definition/);

      });

    });

    describe('with all correct arguments', function () {

      it('it should not throw an error', function () {

        expect(function () {
          new EventDispatcher({ getViewBuilders: function () {} }, {});
        }).not.to.throwError();

      });

      describe('calling getTargetInformation', function () {

        describe('without event argument', function () {

          it('it should throw an error', function () {

            var evtDisp = new EventDispatcher({ getViewBuilders: function () {} }, {});
            expect(function () {
              evtDisp.getTargetInformation();
            }).to.throwError(/event/);

          });

        });

        describe('with event argument', function () {

          it('it should not throw an error', function () {

            var evtDisp = new EventDispatcher({ getViewBuilders: function () {} }, {});
            expect(function () {
              evtDisp.getTargetInformation({});
            }).not.to.throwError();

          });

          describe('passing a definition with all infos', function () {

            it('it should return the correct target infos', function () {

              var evtDisp = new EventDispatcher({ getViewBuilders: function () {} }, { name: 'evtName', version: 'v', aggregate: 'agg', context: 'ctx' });
              var target = evtDisp.getTargetInformation({ evtName: 'evtNameSpec', v: 3, agg: 'aggName', ctx: 'myCtx' });
              expect(target.name).to.eql('evtNameSpec');
              expect(target.version).to.eql(3);
              expect(target.aggregate).to.eql('aggName');
              expect(target.context).to.eql('myCtx');

            });

          });

          describe('passing a definition with less infos', function () {

            it('it should return the correct target infos', function () {

              var evtDisp = new EventDispatcher({ getViewBuilders: function () {} }, { name: 'evtName' });
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

            var evtDisp = new EventDispatcher({ getViewBuilders: function () {
              return [];
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
            var evtDisp = new EventDispatcher({ getViewBuilders: function () {
              return [{ denormalize: function (evt, clb) {
                expect(evt.evtName).to.eql('evtNameSpec');
                expect(clb).to.be.a('function');
                calledBack1 = true;
                clb(null);
              }},
                { denormalize: function (evt, clb) {
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

## File: `test/unit/replayHandlerTest.js`
```javascript
var expect = require('expect.js'),
  _ = require('lodash'),
  EventDispatcher = require('../../lib/eventDispatcher'),
  ReplayHandler = require('../../lib/replayHandler'),
  revGuardStore = require('../../lib/revisionGuardStore');

describe('replayHandler', function () {

  var store;

  before(function (done) {
    revGuardStore.create(function (err, s) {
      store = s;
      done();
    })
  });

  describe('creating a new guard', function () {

    it('it should not throw an error', function () {

      expect(function () {
        new ReplayHandler({}, store);
      }).not.to.throwError();

    });

    it('it should return a correct object', function () {

      var repl = new ReplayHandler({}, store);
      expect(repl.definition).to.be.an('object');
      expect(repl.replay).to.be.a('function');
      expect(repl.replayStreamed).to.be.a('function');

    });

    describe('replaying', function () {

      var repl;

      var evt1 = {
        id: 'evtId1',
        aggregate: {
          id: 'aggId1',
          name: 'agg1'
        },
        revision: 1
      };

      var evt2 = {
        id: 'evtId2',
        aggregate: {
          id: 'aggId1',
          name: 'agg1'
        },
        revision: 2
      };

      var evt3 = {
        id: 'evtId3',
        aggregate: {
          id: 'aggId2',
          name: 'agg2'
        },
        context: {
          name: 'ctx'
        },
        revision: 4
      };

      var evt4 = {
        id: 'evtId4',
        aggregate: {
          id: 'aggId1',
          name: 'agg1'
        },
        context: {
          name: 'ctx'
        },
        revision: 3
      };

      var evt5 = {
        id: 'evtId5',
        aggregate: {
          id: 'aggId2',
          name: 'agg2'
        },
        context: {
          name: 'ctx'
        },
        revision: 5
      };

      var evts = [evt1, evt2, evt3, evt4, evt5];

      var disp;

      var def;

      beforeEach(function () {
        def = {
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
        };
      });

      beforeEach(function (done) {
        store.clear(done);
      });

      describe('normally', function () {

        describe('having defined a revision', function () {

          it('it should work as expected', function (done) {

            var called1 = false;
            var called2 = false;
            var called3 = false;
            var called4 = false;

            var evts1 = [];
            var evts2 = [];
            var evts3 = [];
            var evts4 = [];

            var saveRvmsCalled1 = false;
            var saveRvmsCalled2 = false;
            var saveRvmsCalled3 = false;
            var saveRvmsCalled4 = false;

            disp = new EventDispatcher({
              getPreEventExtender: function (query) {
                return null;
              },
              getViewBuilders: function (query) {
                if (query.aggregate === 'agg1') {
                  return [{
                    collection: { workerId: '11', saveReplayingVms: function (clb) {saveRvmsCalled1 = true; clb(null);} },
                    workerId: '1',
                    denormalize: function (evt, callback) {
                      evts1.push(evt);
                      called1 = true;
                      callback(null);
                    }
                  }];
                } else if (query.aggregate === 'agg2') {
                  return [{
                    collection: { workerId: '22', saveReplayingVms: function (clb) {saveRvmsCalled2 = true; clb(null);} },
                    workerId: '2',
                    denormalize: function (evt, callback) {
                      evts2.push(evt);
                      called2 = true;
                      callback(null);
                    }
                  },{
                    collection: { workerId: '11', saveReplayingVms: function (clb) {saveRvmsCalled3 = true; clb(null);} },
                    workerId: '3',
                    denormalize: function (evt, callback) {
                      evts3.push(evt);
                      called3 = true;
                      callback(null);
                    }
                  },{
                    collection: { noReplay: true, workerId: '33', saveReplayingVms: function (clb) {saveRvmsCalled4 = true; clb(null);} },
                    workerId: '4',
                    denormalize: function (evt, callback) {
                      evts4.push(evt);
                      called4 = true;
                      callback(null);
                    }
                  }];
                }
              }
            }, def);

            repl = new ReplayHandler(disp, store, def);

            repl.replay(evts, function (err) {
              expect(err).not.to.be.ok();
              expect(called1).to.eql(true);
              expect(called2).to.eql(true);
              expect(called3).to.eql(true);
              expect(called4).to.eql(false);

              expect(evts1[0]).to.eql(evt1);
              expect(evts1[1]).to.eql(evt2);
              expect(evts1[2]).to.eql(evt4);
              expect(evts2[0]).to.eql(evt3);
              expect(evts2[1]).to.eql(evt5);
              expect(evts3[0]).to.eql(evt3);
              expect(evts3[1]).to.eql(evt5);
              expect(evts4.length).to.eql(0);

              expect(saveRvmsCalled1).to.eql(true);
              expect(saveRvmsCalled2).to.eql(true);
              expect(saveRvmsCalled3).to.eql(false);
              expect(saveRvmsCalled4).to.eql(false);

              store.get('ctxagg1aggId1', function (err, rev) {
                expect(err).not.to.be.ok();
                expect(rev).to.eql(4);

                store.get('ctxagg2aggId2', function (err, rev) {
                  expect(err).not.to.be.ok();
                  expect(rev).to.eql(6);

                  done();
                });
              });
            });

          });

        });

        describe('not having defined a revision', function () {

          it('it should work as expected', function (done) {

            delete def.revision;

            var called1 = false;
            var called2 = false;
            var called3 = false;

            var evts1 = [];
            var evts2 = [];
            var evts3 = [];

            var saveRvmsCalled1 = false;
            var saveRvmsCalled2 = false;
            var saveRvmsCalled3 = false;

            disp = new EventDispatcher({
              getPreEventExtender: function (query) {
                return null;
              },
              getViewBuilders: function (query) {
                if (query.aggregate === 'agg1') {
                  return [{
                    collection: { workerId: '11', saveReplayingVms: function (clb) {saveRvmsCalled1 = true; clb(null);} },
                    workerId: '1',
                    denormalize: function (evt, callback) {
                      evts1.push(evt);
                      called1 = true;
                      callback(null);
                    }
                  }];
                } else if (query.aggregate === 'agg2') {
                  return [{
                    collection: { workerId: '22', saveReplayingVms: function (clb) {saveRvmsCalled2 = true; clb(null);} },
                    workerId: '2',
                    denormalize: function (evt, callback) {
                      evts2.push(evt);
                      called2 = true;
                      callback(null);
                    }
                  },{
                    collection: { workerId: '11', saveReplayingVms: function (clb) {saveRvmsCalled3 = true; clb(null);} },
                    workerId: '3',
                    denormalize: function (evt, callback) {
                      evts3.push(evt);
                      called3 = true;
                      callback(null);
                    }
                  }];
                }
              }
            }, def);

            repl = new ReplayHandler(disp, store, def);

            repl.replay(evts, function (err) {
              expect(err).not.to.be.ok();
              expect(called1).to.eql(true);
              expect(called2).to.eql(true);
              expect(called3).to.eql(true);

              expect(evts1[0]).to.eql(evt1);
              expect(evts1[1]).to.eql(evt2);
              expect(evts1[2]).to.eql(evt4);
              expect(evts2[0]).to.eql(evt3);
              expect(evts2[1]).to.eql(evt5);
              expect(evts3[0]).to.eql(evt3);
              expect(evts3[1]).to.eql(evt5);

              expect(saveRvmsCalled1).to.eql(true);
              expect(saveRvmsCalled2).to.eql(true);
              expect(saveRvmsCalled3).to.eql(false);

              store.get('aggId1', function (err, rev) {
                expect(err).not.to.be.ok();
                expect(rev).not.to.be.ok();

                store.get('aggId2', function (err, rev) {
                  expect(err).not.to.be.ok();
                  expect(rev).not.to.be.ok();

                  done();
                });
              });
            });

          });

        });

        describe('having defined a preEventExtender', function () {

          it('it should work as expected', function (done) {

            var calledExt1 = false;
            var called1 = false;
            var called2 = false;
            var called3 = false;
            var called4 = false;

            var extendedEvt1 = [];
            var evts1 = [];
            var evts2 = [];
            var evts3 = [];
            var evts4 = [];

            var saveRvmsCalled1 = false;
            var saveRvmsCalled2 = false;
            var saveRvmsCalled3 = false;
            var saveRvmsCalled4 = false;

            disp = new EventDispatcher({
              getPreEventExtender: function (query) {
                if (query.aggregate === 'agg1') {
                  return {
                    extend: function (evt, callback) {
                      extendedEvt1.push(evt);
                      calledExt1 = true;
                      evt.extended = true;
                      callback(null, evt);
                    }
                  };
                }
                return null;
              },
              getViewBuilders: function (query) {
                if (query.aggregate === 'agg1') {
                  return [{
                    collection: { workerId: '11', saveReplayingVms: function (clb) {saveRvmsCalled1 = true; clb(null);} },
                    workerId: '1',
                    denormalize: function (evt, callback) {
                      evts1.push(evt);
                      called1 = true;
                      callback(null);
                    }
                  }];
                } else if (query.aggregate === 'agg2') {
                  return [{
                    collection: { workerId: '22', saveReplayingVms: function (clb) {saveRvmsCalled2 = true; clb(null);} },
                    workerId: '2',
                    denormalize: function (evt, callback) {
                      evts2.push(evt);
                      called2 = true;
                      callback(null);
                    }
                  },{
                    collection: { workerId: '11', saveReplayingVms: function (clb) {saveRvmsCalled3 = true; clb(null);} },
                    workerId: '3',
                    denormalize: function (evt, callback) {
                      evts3.push(evt);
                      called3 = true;
                      callback(null);
                    }
                  },{
                    collection: { noReplay: true, workerId: '33', saveReplayingVms: function (clb) {saveRvmsCalled4 = true; clb(null);} },
                    workerId: '4',
                    denormalize: function (evt, callback) {
                      evts4.push(evt);
                      called4 = true;
                      callback(null);
                    }
                  }];
                }
              }
            }, def);

            repl = new ReplayHandler(disp, store, def);

            repl.replay(evts, function (err) {
              expect(err).not.to.be.ok();
              expect(calledExt1).to.eql(true);
              expect(called1).to.eql(true);
              expect(called2).to.eql(true);
              expect(called3).to.eql(true);
              expect(called4).to.eql(false);

              expect(evts1[0].extended).to.eql(true);
              expect(evts1[1].extended).to.eql(true);
              expect(evts1[2].extended).to.eql(true);
              expect(evts3[1].extended).not.to.be.ok();
              expect(extendedEvt1[0].extended).to.eql(true);
              expect(extendedEvt1[0]).to.eql(evt1);
              expect(evts1[0]).to.eql(evt1);
              expect(evts1[1]).to.eql(evt2);
              expect(evts1[2]).to.eql(evt4);
              expect(evts2[0]).to.eql(evt3);
              expect(evts2[1]).to.eql(evt5);
              expect(evts3[0]).to.eql(evt3);
              expect(evts3[1]).to.eql(evt5);
              expect(evts4.length).to.eql(0);

              expect(saveRvmsCalled1).to.eql(true);
              expect(saveRvmsCalled2).to.eql(true);
              expect(saveRvmsCalled3).to.eql(false);
              expect(saveRvmsCalled4).to.eql(false);

              store.get('ctxagg1aggId1', function (err, rev) {
                expect(err).not.to.be.ok();
                expect(rev).to.eql(4);

                store.get('ctxagg2aggId2', function (err, rev) {
                  expect(err).not.to.be.ok();
                  expect(rev).to.eql(6);

                  done();
                });
              });
            });

          });

        });

      });

      describe('streamed', function () {

        describe('having defined a revision', function () {

          it('it should work as expected', function (done) {

            var called1 = false;
            var called2 = false;
            var called3 = false;

            var evts1 = [];
            var evts2 = [];
            var evts3 = [];

            var saveRvmsCalled1 = false;
            var saveRvmsCalled2 = false;
            var saveRvmsCalled3 = false;

            disp = new EventDispatcher({
              getPreEventExtender: function (query) {
                return null;
              },
              getViewBuilders: function (query) {
                if (query.aggregate === 'agg1') {
                  return [{
                    collection: { workerId: '11', saveReplayingVms: function (clb) {saveRvmsCalled1 = true; clb(null);} },
                    workerId: '1',
                    denormalize: function (evt, callback) {
                      evts1.push(evt);
                      called1 = true;
                      callback(null);
                    }
                  }];
                } else if (query.aggregate === 'agg2') {
                  return [{
                    collection: { workerId: '22', saveReplayingVms: function (clb) {saveRvmsCalled2 = true; clb(null);} },
                    workerId: '2',
                    denormalize: function (evt, callback) {
                      evts2.push(evt);
                      called2 = true;
                      callback(null);
                    }
                  },{
                    collection: { workerId: '11', saveReplayingVms: function (clb) {saveRvmsCalled3 = true; clb(null);} },
                    workerId: '3',
                    denormalize: function (evt, callback) {
                      evts3.push(evt);
                      called3 = true;
                      callback(null);
                    }
                  }];
                }
              }
            }, def);

            repl = new ReplayHandler(disp, store, def);

            repl.replayStreamed(function (replay, finished) {

              _.each(evts, function (e) {
                replay(e);
              });

              finished(function (err) {
                expect(err).not.to.be.ok();
                expect(called1).to.eql(true);
                expect(called2).to.eql(true);
                expect(called3).to.eql(true);

                expect(evts1[0]).to.eql(evt1);
                expect(evts1[1]).to.eql(evt2);
                expect(evts1[2]).to.eql(evt4);
                expect(evts2[0]).to.eql(evt3);
                expect(evts2[1]).to.eql(evt5);
                expect(evts3[0]).to.eql(evt3);
                expect(evts3[1]).to.eql(evt5);

                expect(saveRvmsCalled1).to.eql(true);
                expect(saveRvmsCalled2).to.eql(true);
                expect(saveRvmsCalled3).to.eql(false);

                store.get('ctxagg1aggId1', function (err, rev) {
                  expect(err).not.to.be.ok();
                  expect(rev).to.eql(4);

                  store.get('ctxagg2aggId2', function (err, rev) {
                    expect(err).not.to.be.ok();
                    expect(rev).to.eql(6);

                    done();
                  });
                });
              });

            });

          });

          describe('replaying in parts', function () {

            it('it should work as expected', function (done) {

              var called1 = false;
              var called2 = false;
              var called3 = false;

              var evts1 = [];
              var evts2 = [];
              var evts3 = [];

              var saveRvmsCalled1 = false;
              var saveRvmsCalled2 = false;
              var saveRvmsCalled3 = false;

              disp = new EventDispatcher({
                getPreEventExtender: function (query) {
                  return null;
                },
                getViewBuilders: function (query) {
                  if (query.aggregate === 'agg1') {
                    return [{
                      collection: { workerId: '11', saveReplayingVms: function (clb) {saveRvmsCalled1 = true; clb(null);} },
                      workerId: '1',
                      denormalize: function (evt, callback) {
                        evts1.push(evt);
                        called1 = true;
                        callback(null);
                      }
                    }];
                  } else if (query.aggregate === 'agg2') {
                    return [{
                      collection: { workerId: '22', saveReplayingVms: function (clb) {saveRvmsCalled2 = true; clb(null);} },
                      workerId: '2',
                      denormalize: function (evt, callback) {
                        evts2.push(evt);
                        called2 = true;
                        callback(null);
                      }
                    },{
                      collection: { workerId: '11', saveReplayingVms: function (clb) {saveRvmsCalled3 = true; clb(null);} },
                      workerId: '3',
                      denormalize: function (evt, callback) {
                        evts3.push(evt);
                        called3 = true;
                        callback(null);
                      }
                    }];
                  }
                }
              }, def);

              repl = new ReplayHandler(disp, store, def);

              repl.replayStreamed(function (replay, finished) {

                _.each([evt1, evt2, evt3], function (e) {
                  replay(e);
                });

                finished(function (err) {
                  expect(err).not.to.be.ok();
                  expect(called1).to.eql(true);
                  expect(called2).to.eql(true);
                  expect(called3).to.eql(true);

                  expect(evts1[0]).to.eql(evt1);
                  expect(evts1[1]).to.eql(evt2);
                  // expect(evts1[2]).to.eql(evt4);
                  expect(evts2[0]).to.eql(evt3);
                  // expect(evts2[1]).to.eql(evt5);
                  expect(evts3[0]).to.eql(evt3);
                  // expect(evts3[1]).to.eql(evt5);

                  expect(saveRvmsCalled1).to.eql(true);
                  expect(saveRvmsCalled2).to.eql(true);
                  expect(saveRvmsCalled3).to.eql(false);


                  repl.replayStreamed(function (replay, finished) {

                    _.each([evt4, evt5], function (e) {
                      replay(e);
                    });

                    finished(function (err) {
                      expect(err).not.to.be.ok();
                      expect(called1).to.eql(true);
                      expect(called2).to.eql(true);
                      expect(called3).to.eql(true);

                      // expect(evts1[0]).to.eql(evt1);
                      // expect(evts1[1]).to.eql(evt2);
                      expect(evts1[2]).to.eql(evt4);
                      // expect(evts2[0]).to.eql(evt3);
                      expect(evts2[1]).to.eql(evt5);
                      // expect(evts3[0]).to.eql(evt3);
                      expect(evts3[1]).to.eql(evt5);

                      expect(saveRvmsCalled1).to.eql(true);
                      expect(saveRvmsCalled2).to.eql(true);
                      expect(saveRvmsCalled3).to.eql(false);

                      store.get('ctxagg1aggId1', function (err, rev) {
                        expect(err).not.to.be.ok();
                        expect(rev).to.eql(4);

                        store.get('ctxagg2aggId2', function (err, rev) {
                          expect(err).not.to.be.ok();
                          expect(rev).to.eql(6);

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

        describe('not having defined a revision', function () {

          it('it should work as expected', function (done) {

            delete def.revision;

            var called1 = false;
            var called2 = false;
            var called3 = false;

            var evts1 = [];
            var evts2 = [];
            var evts3 = [];

            var saveRvmsCalled1 = false;
            var saveRvmsCalled2 = false;
            var saveRvmsCalled3 = false;

            disp = new EventDispatcher({
              getPreEventExtender: function (query) {
                return null;
              },
              getViewBuilders: function (query) {
                if (query.aggregate === 'agg1') {
                  return [{
                    collection: { workerId: '11', saveReplayingVms: function (clb) {saveRvmsCalled1 = true; clb(null);} },
                    workerId: '1',
                    denormalize: function (evt, callback) {
                      evts1.push(evt);
                      called1 = true;
                      callback(null);
                    }
                  }];
                } else if (query.aggregate === 'agg2') {
                  return [{
                    collection: { workerId: '22', saveReplayingVms: function (clb) {saveRvmsCalled2 = true; clb(null);} },
                    workerId: '2',
                    denormalize: function (evt, callback) {
                      evts2.push(evt);
                      called2 = true;
                      callback(null);
                    }
                  },{
                    collection: { workerId: '11', saveReplayingVms: function (clb) {saveRvmsCalled3 = true; clb(null);} },
                    workerId: '3',
                    denormalize: function (evt, callback) {
                      evts3.push(evt);
                      called3 = true;
                      callback(null);
                    }
                  }];
                }
              }
            }, def);

            repl = new ReplayHandler(disp, store, def);

            repl.replayStreamed(function (replay, finished) {

              _.each(evts, function (e) {
                replay(e);
              });

              finished(function (err) {
                expect(err).not.to.be.ok();
                expect(called1).to.eql(true);
                expect(called2).to.eql(true);
                expect(called3).to.eql(true);

                expect(evts1[0]).to.eql(evt1);
                expect(evts1[1]).to.eql(evt2);
                expect(evts1[2]).to.eql(evt4);
                expect(evts2[0]).to.eql(evt3);
                expect(evts2[1]).to.eql(evt5);
                expect(evts3[0]).to.eql(evt3);
                expect(evts3[1]).to.eql(evt5);

                expect(saveRvmsCalled1).to.eql(true);
                expect(saveRvmsCalled2).to.eql(true);
                expect(saveRvmsCalled3).to.eql(false);

                store.get('aggId1', function (err, rev) {
                  expect(err).not.to.be.ok();
                  expect(rev).not.to.be.ok();

                  store.get('aggId2', function (err, rev) {
                    expect(err).not.to.be.ok();
                    expect(rev).not.to.be.ok();

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

      var types = ['inmemory', 'mongodb', 'tingodb', 'redis', 'dynamodb'/*, 'couchdb'*/];

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
              expect(err.name).to.eql('AlreadyDenormalizingError');
            });
          }, 10);

          setTimeout(function () {
            guard.guard(evt2, function (err) {
              expect(err).to.be.ok();
              expect(err.name).to.eql('AlreadyDenormalizedError');
              expect(guarded).to.eql(3);

              guard.guard(evt3, function (err) {
                expect(err).to.be.ok();
                expect(err.name).to.eql('AlreadyDenormalizedError');
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

## File: `test/unit/definitions/collectionTest.js`
```javascript
var expect = require('expect.js'),
  _ = require('lodash'),
  async = require('async'),
  viewmodel = require('viewmodel'),
  DefinitionBase = require('../../../lib/definitionBase'),
  Collection = require('../../../lib/definitions/collection'),
  api = require('../../../');

describe('collection definition', function () {

  describe('creating a new collection definition', function () {

    it('it should not throw an error', function () {

      expect(function () {
        api.defineCollection();
      }).not.to.throwError();

    });

    it('it should return a correct object', function () {

      var col = api.defineCollection(null);
      expect(col).to.be.a(DefinitionBase);
      expect(col).to.be.a(Collection);
      expect(col.definitions).to.be.an('object');
      expect(col.definitions.notification).to.be.an('object');
      expect(col.definitions.event).to.be.an('object');
      expect(col.defineNotification).to.be.a('function');
      expect(col.defineEvent).to.be.a('function');
      expect(col.defineOptions).to.be.a('function');

      expect(col.useRepository).to.be.a('function');
      expect(col.addViewBuilder).to.be.a('function');
      expect(col.addEventExtender).to.be.a('function');
      expect(col.getViewBuilders).to.be.a('function');
      expect(col.getEventExtender).to.be.a('function');
      expect(col.getEventExtenders).to.be.a('function');
      expect(col.getNewId).to.be.a('function');
      expect(col.saveViewModel).to.be.a('function');
      expect(col.loadViewModel).to.be.a('function');
      expect(col.findViewModels).to.be.a('function');
      expect(col.saveReplayingVms).to.be.a('function');

    });

    describe('calling addViewBuilder', function () {

      describe('with a wrong object', function () {

        it('it should throw an error', function () {

          var col = api.defineCollection();

          expect(function () {
            col.addViewBuilder();
          }).to.throwError(/builder/);

        });

      });

      describe('with a correct object', function () {

        it('it should work as expected', function () {

          var col = api.defineCollection();

          col.addViewBuilder({ name: 'myEvent', useCollection: function (c) {
            expect(c).to.eql(col);
          }});

          expect(col.viewBuilders.length).to.eql(1);
          expect(col.viewBuilders[0].name).to.eql('myEvent');

        });

      });

      describe('having not defined a default payload for viewBuilders', function () {

        describe('having not defined a payload in the viewBuilder', function () {

          it('it should work as expected', function () {

            var col = api.defineCollection();

            col.addViewBuilder({ name: 'myEvent', payload: null, useCollection: function (c) {
              expect(c).to.eql(col);
            }});

            expect(col.viewBuilders.length).to.eql(1);
            expect(col.viewBuilders[0].payload).to.eql('');

          });

        });

        describe('having defined a payload in the command', function () {

          it('it should work as expected', function () {

            var col = api.defineCollection();

            col.addViewBuilder({ name: 'myEvent', payload: 'maPay', useCollection: function (c) {
              expect(c).to.eql(col);
            }});

            expect(col.viewBuilders.length).to.eql(1);
            expect(col.viewBuilders[0].payload).to.eql('maPay');

          });

        });

      });

      describe('having defined a default payload for commands', function () {

        describe('having not defined a payload in the command', function () {

          it('it should work as expected', function () {

            var col = api.defineCollection({ defaultPayload: 'def' });

            col.addViewBuilder({ name: 'myEvent', payload: null, useCollection: function (c) {
              expect(c).to.eql(col);
            }});

            expect(col.viewBuilders.length).to.eql(1);
            expect(col.viewBuilders[0].payload).to.eql('def');

          });

        });

        describe('having defined a payload in the command', function () {

          it('it should work as expected', function () {

            var col = api.defineCollection({ defaultPayload: 'def' });

            col.addViewBuilder({ name: 'myEvent', payload: 'maPay', useCollection: function (c) {
              expect(c).to.eql(col);
            }});

            expect(col.viewBuilders.length).to.eql(1);
            expect(col.viewBuilders[0].payload).to.eql('maPay');

          });

        });

      });

    });

    describe('calling addEventExtender', function () {

      describe('with a wrong object', function () {

        it('it should throw an error', function () {

          var col = api.defineCollection();

          expect(function () {
            col.addEventExtender();
          }).to.throwError(/extender/);

        });

      });

      describe('with a correct object', function () {

        it('it should work as expected', function () {

          var col = api.defineCollection();

          col.addEventExtender({ name: 'myEvent', useCollection: function (c) {
            expect(c).to.eql(col);
          }});

          expect(col.eventExtenders.length).to.eql(1);
          expect(col.eventExtenders[0].name).to.eql('myEvent');

        });

      });

    });

    describe('calling addPreEventExtender', function () {

      describe('with a wrong object', function () {

        it('it should throw an error', function () {

          var col = api.defineCollection();

          expect(function () {
            col.addPreEventExtender();
          }).to.throwError(/extender/);

        });

      });

      describe('with a correct object', function () {

        it('it should work as expected', function () {

          var col = api.defineCollection();

          col.addPreEventExtender({ name: 'myEvent', useCollection: function (c) {
            expect(c).to.eql(col);
          }});

          expect(col.preEventExtenders.length).to.eql(1);
          expect(col.preEventExtenders[0].name).to.eql('myEvent');

        });

      });

    });

    describe('having added some viewBuilders', function () {

      var col;

      beforeEach(function () {
        col = api.defineCollection();
        col.addViewBuilder({ name: 'evt1', version: 0, aggregate: null, context: null, useCollection: function () {} });
        col.addViewBuilder({ name: 'evt2', version: 0, aggregate: null, context: null, useCollection: function () {} });
        col.addViewBuilder({ name: 'evt2', version: 1, aggregate: null, context: null, useCollection: function () {} });
        col.addViewBuilder({ name: 'evt2', version: 2, aggregate: null, context: null, useCollection: function () {} });
        col.addViewBuilder({ name: 'evt3', version: 0, aggregate: null, context: null, useCollection: function () {} });
        col.addViewBuilder({ name: 'evt3', version: 0, aggregate: 'agg', context: null, useCollection: function () {} });
        col.addViewBuilder({ name: 'evt3', version: 0, aggregate: 'agg', context: 'ctx', useCollection: function () {} });
        col.addViewBuilder({ name: '', version: 0, aggregate: 'aggOnly', context: null, useCollection: function () {} });
      });

      describe('calling getViewBuilders', function () {

        it('it should return all viewBuilders', function () {

          var viewBuilders = col.getViewBuilders();
          expect(viewBuilders.length).to.eql(8);
          expect(viewBuilders[0].name).to.eql('evt1');
          expect(viewBuilders[0].version).to.eql(0);
          expect(viewBuilders[1].name).to.eql('evt2');
          expect(viewBuilders[1].version).to.eql(0);
          expect(viewBuilders[2].name).to.eql('evt2');
          expect(viewBuilders[2].version).to.eql(1);
          expect(viewBuilders[3].name).to.eql('evt2');
          expect(viewBuilders[3].version).to.eql(2);
          expect(viewBuilders[4].name).to.eql('evt3');
          expect(viewBuilders[4].version).to.eql(0);
          expect(viewBuilders[5].name).to.eql('evt3');
          expect(viewBuilders[5].aggregate).to.eql('agg');
          expect(viewBuilders[5].version).to.eql(0);
          expect(viewBuilders[6].name).to.eql('evt3');
          expect(viewBuilders[6].aggregate).to.eql('agg');
          expect(viewBuilders[6].context).to.eql('ctx');
          expect(viewBuilders[6].version).to.eql(0);
          expect(viewBuilders[7].name).to.eql('');
          expect(viewBuilders[7].aggregate).to.eql('aggOnly');
          expect(viewBuilders[7].version).to.eql(0);

        });

      });

      describe('calling getViewBuilder', function () {

        it('it should work as expected', function () {

          var ex0 = col.getViewBuilders({ name: 'someEvtName', aggregate: 'wrong' });
          expect(ex0.length).to.eql(0);

          var ex1 = col.getViewBuilders({ name: 'evt1', version: 3 });
          expect(ex1.length).to.eql(0);

          var ex2 = col.getViewBuilders({ name: 'evt1', version: 0 });
          expect(ex2.length).to.eql(1);
          expect(ex2[0].name).to.eql('evt1');
          expect(ex2[0].version).to.eql(0);

          var ex3 = col.getViewBuilders({ name: 'evt2', version: 0 });
          expect(ex3[0].name).to.eql('evt2');
          expect(ex3[0].version).to.eql(0);

          var ex4 = col.getViewBuilders({ name: 'evt2', version: 1 });
          expect(ex4[0].name).to.eql('evt2');
          expect(ex4[0].version).to.eql(1);

          var ex5 = col.getViewBuilders({ name: 'evt2', version: 2 });
          expect(ex5[0].name).to.eql('evt2');
          expect(ex5[0].version).to.eql(2);

          var ex6 = col.getViewBuilders({ name: 'evt3', version: 0 });
          expect(ex6[0].name).to.eql('evt3');
          expect(ex6[0].aggregate).not.to.be.ok();
          expect(ex6[0].context).not.to.be.ok();
          expect(ex6[0].version).to.eql(0);

          var ex7 = col.getViewBuilders({ name: 'evt3' });
          expect(ex7[0].name).to.eql('evt3');
          expect(ex7[0].aggregate).not.to.be.ok();
          expect(ex7[0].context).not.to.be.ok();
          expect(ex7[0].version).to.eql(0);

          var ex8 = col.getViewBuilders({ name: 'evt2' });
          expect(ex8[0].name).to.eql('evt2');
          expect(ex8[0].version).to.eql(0);

          var ex9 = col.getViewBuilders({ name: 'evt3', aggregate: 'agg' });
          expect(ex9[0].name).to.eql('evt3');
          expect(ex9[0].aggregate).to.eql('agg');
          expect(ex9[0].context).not.to.be.ok();
          expect(ex9[0].version).to.eql(0);

          var ex10 = col.getViewBuilders({ name: 'evt3', aggregate: 'agg', context: 'ctx' });
          expect(ex10[0].name).to.eql('evt3');
          expect(ex10[0].aggregate).to.eql('agg');
          expect(ex10[0].context).to.eql('ctx');
          expect(ex10[0].version).to.eql(0);

          var ex11 = col.getViewBuilders({ name: 'evt3', context: 'ctx' });
          expect(ex11[0].name).to.eql('evt3');
          expect(ex11[0].aggregate).to.eql('agg');
          expect(ex11[0].context).to.eql('ctx');
          expect(ex11[0].version).to.eql(0);

          var ex12 = col.getViewBuilders({ name: 'evt3', aggregate: 'aggOnly' });
          expect(ex12[0].name).to.eql('');
          expect(ex12[0].aggregate).to.eql('aggOnly');
          expect(ex12[0].context).not.to.be.ok();
          expect(ex12[0].version).to.eql(0);

          var ex13 = col.getViewBuilders({ name: 'someEvtName' });
          expect(ex13.length).to.eql(1);
          expect(ex13[0].name).to.eql('');
          expect(ex13[0].aggregate).to.eql('aggOnly');
          expect(ex13[0].context).not.to.be.ok();
          expect(ex13[0].version).to.eql(0);

        });

      });

    });

    describe('having added some eventExtenders', function () {

      var col;

      beforeEach(function () {
        col = api.defineCollection();
        col.addEventExtender({ name: 'evt1', version: 0, aggregate: null, context: null, useCollection: function () {} });
        col.addEventExtender({ name: 'evt2', version: 0, aggregate: null, context: null, useCollection: function () {} });
        col.addEventExtender({ name: 'evt2', version: 1, aggregate: null, context: null, useCollection: function () {} });
        col.addEventExtender({ name: 'evt2', version: 2, aggregate: null, context: null, useCollection: function () {} });
        col.addEventExtender({ name: 'evt3', version: 0, aggregate: null, context: null, useCollection: function () {} });
        col.addEventExtender({ name: 'evt3', version: 0, aggregate: 'agg', context: null, useCollection: function () {} });
        col.addEventExtender({ name: 'evt3', version: 0, aggregate: 'agg', context: 'ctx', useCollection: function () {} });
      });

      describe('calling getEventExtenders', function () {

        it('it should return all eventExtenders', function () {

          var eventExtenders = col.getEventExtenders();
          expect(eventExtenders.length).to.eql(7);
          expect(eventExtenders[0].name).to.eql('evt1');
          expect(eventExtenders[0].version).to.eql(0);
          expect(eventExtenders[1].name).to.eql('evt2');
          expect(eventExtenders[1].version).to.eql(0);
          expect(eventExtenders[2].name).to.eql('evt2');
          expect(eventExtenders[2].version).to.eql(1);
          expect(eventExtenders[3].name).to.eql('evt2');
          expect(eventExtenders[3].version).to.eql(2);
          expect(eventExtenders[4].name).to.eql('evt3');
          expect(eventExtenders[4].version).to.eql(0);
          expect(eventExtenders[5].name).to.eql('evt3');
          expect(eventExtenders[5].aggregate).to.eql('agg');
          expect(eventExtenders[5].version).to.eql(0);
          expect(eventExtenders[6].name).to.eql('evt3');
          expect(eventExtenders[6].aggregate).to.eql('agg');
          expect(eventExtenders[6].context).to.eql('ctx');
          expect(eventExtenders[6].version).to.eql(0);

        });

      });

      describe('calling getEventExtender', function () {

        it('it should work as expected', function () {

          var ex0 = col.getEventExtender({ name: 'someEvtName' });
          expect(ex0).not.to.be.ok();

          var ex1 = col.getEventExtender({ name: 'evt1', version: 3 });
          expect(ex1).not.to.be.ok();

          var ex2 = col.getEventExtender({ name: 'evt1', version: 0 });
          expect(ex2.name).to.eql('evt1');
          expect(ex2.version).to.eql(0);

          var ex3 = col.getEventExtender({ name: 'evt2', version: 0 });
          expect(ex3.name).to.eql('evt2');
          expect(ex3.version).to.eql(0);

          var ex4 = col.getEventExtender({ name: 'evt2', version: 1 });
          expect(ex4.name).to.eql('evt2');
          expect(ex4.version).to.eql(1);

          var ex5 = col.getEventExtender({ name: 'evt2', version: 2 });
          expect(ex5.name).to.eql('evt2');
          expect(ex5.version).to.eql(2);

          var ex6 = col.getEventExtender({ name: 'evt3', version: 0 });
          expect(ex6.name).to.eql('evt3');
          expect(ex6.aggregate).not.to.be.ok();
          expect(ex6.context).not.to.be.ok();
          expect(ex6.version).to.eql(0);

          var ex7 = col.getEventExtender({ name: 'evt3' });
          expect(ex7.name).to.eql('evt3');
          expect(ex7.aggregate).not.to.be.ok();
          expect(ex7.context).not.to.be.ok();
          expect(ex7.version).to.eql(0);

          var ex8 = col.getEventExtender({ name: 'evt2' });
          expect(ex8.name).to.eql('evt2');
          expect(ex8.version).to.eql(0);

          var ex9 = col.getEventExtender({ name: 'evt3', aggregate: 'agg' });
          expect(ex9.name).to.eql('evt3');
          expect(ex9.aggregate).to.eql('agg');
          expect(ex9.context).not.to.be.ok();
          expect(ex9.version).to.eql(0);

          var ex10 = col.getEventExtender({ name: 'evt3', aggregate: 'agg', context: 'ctx' });
          expect(ex10.name).to.eql('evt3');
          expect(ex10.aggregate).to.eql('agg');
          expect(ex10.context).to.eql('ctx');
          expect(ex10.version).to.eql(0);

          var ex11 = col.getEventExtender({ name: 'evt3', context: 'ctx' });
          expect(ex11.name).to.eql('evt3');
          expect(ex11.aggregate).to.eql('agg');
          expect(ex11.context).to.eql('ctx');
          expect(ex11.version).to.eql(0);

        });

      });

    });

    describe('having added some preEventExtenders', function () {

      var col;

      beforeEach(function () {
        col = api.defineCollection();
        col.addPreEventExtender({ name: 'evt1', version: 0, aggregate: null, context: null, useCollection: function () {} });
        col.addPreEventExtender({ name: 'evt2', version: 0, aggregate: null, context: null, useCollection: function () {} });
        col.addPreEventExtender({ name: 'evt2', version: 1, aggregate: null, context: null, useCollection: function () {} });
        col.addPreEventExtender({ name: 'evt2', version: 2, aggregate: null, context: null, useCollection: function () {} });
        col.addPreEventExtender({ name: 'evt3', version: 0, aggregate: null, context: null, useCollection: function () {} });
        col.addPreEventExtender({ name: 'evt3', version: 0, aggregate: 'agg', context: null, useCollection: function () {} });
        col.addPreEventExtender({ name: 'evt3', version: 0, aggregate: 'agg', context: 'ctx', useCollection: function () {} });
      });

      describe('calling getPreEventExtenders', function () {

        it('it should return all preEventExtenders', function () {

          var preEventExtenders = col.getPreEventExtenders();
          expect(preEventExtenders.length).to.eql(7);
          expect(preEventExtenders[0].name).to.eql('evt1');
          expect(preEventExtenders[0].version).to.eql(0);
          expect(preEventExtenders[1].name).to.eql('evt2');
          expect(preEventExtenders[1].version).to.eql(0);
          expect(preEventExtenders[2].name).to.eql('evt2');
          expect(preEventExtenders[2].version).to.eql(1);
          expect(preEventExtenders[3].name).to.eql('evt2');
          expect(preEventExtenders[3].version).to.eql(2);
          expect(preEventExtenders[4].name).to.eql('evt3');
          expect(preEventExtenders[4].version).to.eql(0);
          expect(preEventExtenders[5].name).to.eql('evt3');
          expect(preEventExtenders[5].aggregate).to.eql('agg');
          expect(preEventExtenders[5].version).to.eql(0);
          expect(preEventExtenders[6].name).to.eql('evt3');
          expect(preEventExtenders[6].aggregate).to.eql('agg');
          expect(preEventExtenders[6].context).to.eql('ctx');
          expect(preEventExtenders[6].version).to.eql(0);

        });

      });

      describe('calling getPreEventExtender', function () {

        it('it should work as expected', function () {

          var ex0 = col.getPreEventExtender({ name: 'someEvtName' });
          expect(ex0).not.to.be.ok();

          var ex1 = col.getPreEventExtender({ name: 'evt1', version: 3 });
          expect(ex1).not.to.be.ok();

          var ex2 = col.getPreEventExtender({ name: 'evt1', version: 0 });
          expect(ex2.name).to.eql('evt1');
          expect(ex2.version).to.eql(0);

          var ex3 = col.getPreEventExtender({ name: 'evt2', version: 0 });
          expect(ex3.name).to.eql('evt2');
          expect(ex3.version).to.eql(0);

          var ex4 = col.getPreEventExtender({ name: 'evt2', version: 1 });
          expect(ex4.name).to.eql('evt2');
          expect(ex4.version).to.eql(1);

          var ex5 = col.getPreEventExtender({ name: 'evt2', version: 2 });
          expect(ex5.name).to.eql('evt2');
          expect(ex5.version).to.eql(2);

          var ex6 = col.getPreEventExtender({ name: 'evt3', version: 0 });
          expect(ex6.name).to.eql('evt3');
          expect(ex6.aggregate).not.to.be.ok();
          expect(ex6.context).not.to.be.ok();
          expect(ex6.version).to.eql(0);

          var ex7 = col.getPreEventExtender({ name: 'evt3' });
          expect(ex7.name).to.eql('evt3');
          expect(ex7.aggregate).not.to.be.ok();
          expect(ex7.context).not.to.be.ok();
          expect(ex7.version).to.eql(0);

          var ex8 = col.getPreEventExtender({ name: 'evt2' });
          expect(ex8.name).to.eql('evt2');
          expect(ex8.version).to.eql(0);

          var ex9 = col.getPreEventExtender({ name: 'evt3', aggregate: 'agg' });
          expect(ex9.name).to.eql('evt3');
          expect(ex9.aggregate).to.eql('agg');
          expect(ex9.context).not.to.be.ok();
          expect(ex9.version).to.eql(0);

          var ex10 = col.getPreEventExtender({ name: 'evt3', aggregate: 'agg', context: 'ctx' });
          expect(ex10.name).to.eql('evt3');
          expect(ex10.aggregate).to.eql('agg');
          expect(ex10.context).to.eql('ctx');
          expect(ex10.version).to.eql(0);

          var ex11 = col.getPreEventExtender({ name: 'evt3', context: 'ctx' });
          expect(ex11.name).to.eql('evt3');
          expect(ex11.aggregate).to.eql('agg');
          expect(ex11.context).to.eql('ctx');
          expect(ex11.version).to.eql(0);

        });

      });

    });

    describe('using a repository', function () {

      var col;

      before(function (done) {
        viewmodel.write(function (err, repository) {
          col = api.defineCollection({ name: 'dummy' }, { my: { def: 'data' } });
          col.useRepository(repository);
          done();
        })
      });

      describe('calling getNewId', function() {

        it('it should callback with a new id as string', function (done) {

          col.getNewId(function (err, id) {
            expect(err).not.to.be.ok();
            expect(id).to.be.a('string');
            done();
          });

        });

      });

      describe('calling loadViewModel', function () {

        describe('in normal mode', function () {

          it('it should work as expected', function (done) {

            var orgRepo = col.repository;
            col.repository = {
              get: function (id, clb) {
                clb(null, {theId: id, has: function () { return true }});
              }
            };

            col.loadViewModel('423', function (err, vm) {
              expect(err).not.to.be.ok();
              expect(vm.theId).to.eql('423');

              col.repository = orgRepo;
              col.isReplaying = false;
              done();
            });

          });

        });

        describe('in replay mode', function () {

          describe('not having a cached vm', function () {

            it('it should work as expected', function (done) {

              var orgRepo = col.repository;
              col.repository = {
                get: function (id, clb) {
                  clb(null, {theId: id, has: function () { return true }});
                }
              };
              col.isReplaying = true;
//              col.replayingVms['423'] = { id: '423', cached: true };
              col.loadViewModel('423', function (err, vm) {
                expect(err).not.to.be.ok();
                expect(vm.theId).to.eql('423');

                col.repository = orgRepo;
                col.isReplaying = false;
                done();
              });

            });

          });

          describe('having a cached vm', function () {

            it('it should work as expected', function (done) {

              var orgRepo = col.repository;
              col.repository = {
                get: function (id, clb) {
                  clb(null, {theId: id, has: function () { return true }, toJSON: function () { return { theId: id }; }});
                }
              };
              col.isReplaying = true;
              col.replayingVms['423'] = { id: '423', cached: true };
              col.loadViewModel('423', function (err, vm) {
                expect(err).not.to.be.ok();
                expect(vm.id).to.eql('423');
                expect(vm.cached).to.eql(true);

                col.repository = orgRepo;
                col.isReplaying = false;
                col.replayingVms = {};
                done();
              });

            });

          });

          describe('having a cached deleted vm', function () {

            it('it should work as expected', function (done) {

              var orgRepo = col.repository;
              col.repository = {
                get: function (id, clb) {
                  clb(null, {theId: id, has: function () { return true }, toJSON: function () { return { theId: id }; }});
                }
              };
              col.isReplaying = true;
              col.replayingVmsToDelete['423'] = { id: '423', cached: true };
              col.loadViewModel('423', function (err, vm) {
                expect(err).not.to.be.ok();
                expect(vm.id).to.eql('423');
                expect(vm.cached).not.to.eql(true);

                col.repository = orgRepo;
                col.isReplaying = false;
                col.replayingVms = {};
                col.replayingVmsToDelete = {};
                done();
              });

            });

          });

        });

      });

      describe('calling findViewModels', function () {

        describe('in normal mode', function () {

          it('it should work as expected', function (done) {

            var orgRepo = col.repository;
            col.repository = {
              find: function (query, queryOpt, clb) {
                expect(query.id).to.eql('8372');
                clb(null, [{id: '8372', has: function () { return true }}]);
              }
            };

            col.findViewModels({ id: '8372' }, function (err, vms) {
              expect(err).not.to.be.ok();
              expect(vms.length).to.eql(1);
              expect(vms[0].id).to.eql('8372');

              col.repository = orgRepo;
              col.isReplaying = false;
              done();
            });

          });

        });

        describe('in replay mode', function () {

          describe('not having a cached vm', function () {

            it('it should work as expected', function (done) {

              var orgRepo = col.repository;
              col.repository = {
                find: function (query, queryOpt, clb) {
                  expect(query.id).to.eql('8372');
                  clb(null, [{id: '8372', has: function () { return true }}]);
                }
              };
              col.isReplaying = true;
//              col.replayingVms['423'] = { id: '423', cached: true };
              col.findViewModels({ id: '8372' }, function (err, vms) {
                expect(err).not.to.be.ok();
                expect(vms.length).to.eql(1);
                expect(vms[0].id).to.eql('8372');

                col.repository = orgRepo;
                col.isReplaying = false;
                done();
              });

            });

          });

          describe('having a cached vm', function () {

            it('it should work as expected', function (done) {

              var orgRepo = col.repository;
              col.repository = {
                find: function (query, queryOpt, clb) {
                  expect(query.id).to.eql('8372');
                  clb(null, [{id: '8372', has: function () { return true }, toJSON: function () { return { id: '8372' }; }}]);
                }
              };
              col.isReplaying = true;
              col.replayingVms['8372'] = { id: '8372', cached: true, attributes: { id: '8372', cached: true }, toJSON: function () { return this.attributes; } };
              col.findViewModels({ id: '8372' }, function (err, vms) {
                expect(err).not.to.be.ok();
                expect(vms.length).to.eql(1);
                expect(vms[0].id).to.eql('8372');
                expect(vms[0].cached).to.eql(true);

                col.repository = orgRepo;
                col.isReplaying = false;
                col.replayingVms = {};
                done();
              });

            });

          });

          describe('having a cached deleted vm', function () {

            it('it should work as expected', function (done) {

              var orgRepo = col.repository;
              col.repository = {
                find: function (query, queryOpt, clb) {
                  expect(query.id).to.eql('8372');
                  clb(null, [{id: '8372', has: function () { return true }}]);
                }
              };
              col.isReplaying = true;
              col.replayingVmsToDelete['8372'] = { id: '8372', cached: true };
              col.findViewModels({ id: '8372' }, function (err, vms) {
                expect(err).not.to.be.ok();
                expect(vms.length).to.eql(0);

                col.repository = orgRepo;
                col.isReplaying = false;
                col.replayingVms = {};
                col.replayingVmsToDelete = {};
                done();
              });

            });

          });

        });

      });

      describe('calling saveViewModel', function () {

        describe('in normal mode', function () {

          it('it should work as expected', function (done) {

            var orgRepo = col.repository;
            col.repository = {
              commit: function (vm, clb) {
                expect(vm.id).to.eql('423');
                called = true;
                clb(null);
              }
            };

            var called = false;
            col.saveViewModel({ id: '423' }, function (err) {
              expect(err).not.to.be.ok();
              expect(called).to.eql(true);

              col.repository = orgRepo;
              col.isReplaying = false;
              done();
            });

          });

        });

        describe('in replay mode', function () {

          it('it should work as expected', function (done) {

            var orgRepo = col.repository;
            col.repository = {
              commit: function (vm, clb) {
                expect(vm.id).to.eql('423');
                called = true;
                clb(null);
              }
            };

            var called = false;
            col.isReplaying = true;
            col.saveViewModel({ id: '423', toJSON: function () { return { id: '423' }; } }, function (err) {
              expect(err).not.to.be.ok();
              expect(called).to.eql(false);
              expect(col.replayingVms['423'].id).to.eql('423');

              col.repository = orgRepo;
              col.isReplaying = false;
              done();
            });

          });

          describe('having a deleted vm', function () {

            it('it should work as expected', function (done) {

              var orgRepo = col.repository;
              col.repository = {
                commit: function (vm, clb) {
                  expect(vm.id).to.eql('423');
                  called = true;
                  clb(null);
                }
              };

              var called = false;
              col.isReplaying = true;
              col.saveViewModel({ id: '423', actionOnCommit: 'delete', toJSON: function () { return { id: '756' }; } }, function (err) {
                expect(err).not.to.be.ok();
                expect(called).to.eql(false);
                expect(col.replayingVms['423']).not.to.be.ok();
                expect(col.replayingVmsToDelete['423'].id).to.eql('423');

                col.repository = orgRepo;
                col.isReplaying = false;
                col.replayingVmsToDelete = {};
                done();
              });

            });

          });

        });

      });

      describe('calling saveReplayingVms', function () {

        describe('in normal mode', function () {

          it('it callback with an error', function (done) {

            var orgRepo = col.repository;
            col.repository = {
              commit: function (vm, clb) {
                called = true;
                clb(null);
              }
            };

            var called = false;
            col.saveReplayingVms(function (err) {
              expect(err).to.be.ok();
              expect(err.message).to.match(/replay/);
              expect(called).to.eql(false);

              col.repository = orgRepo;
              col.isReplaying = false;
              done();
            });

          });

        });

        describe('in replay mode', function () {

          it('it should work as expected', function (done) {

            var commitCalled = [];

            var orgRepo = col.repository;
            col.repository = {
              commit: function (vm, clb) {
                commitCalled.push(vm);
                clb(null);
              }
            };

            col.isReplaying = true;
            col.replayingVms['423'] = { id: '423', cached: true, actionOnCommitForReplay: 'create' };
            col.replayingVmsToDelete['5123'] = { id: '5123', cached: true, actionOnCommitForReplay: 'delete' };
            col.saveReplayingVms(function (err) {
              expect(err).not.to.be.ok();
              expect(commitCalled.length).to.eql(2);
              expect(commitCalled[0].id).to.eql('5123');
              expect(commitCalled[1].id).to.eql('423');

              col.repository = orgRepo;
              col.isReplaying = false;
              col.replayingVms = {};
              col.replayingVmsToDelete = {};
              done();
            });

          });

        });

        describe('in replay mode with bulkCommit repository', function () {

          it('it should work as expected', function (done) {

            var commitCalled = [];

            var orgRepo = col.repository;
            col.repository = {
              bulkCommit: function (vms, clb) {
                _.each(vms, function(vm) {
                  commitCalled.push(vm);
                });
                clb(null);
              },
              commit: function (vm, clb) {
                // commitCalled.push(vm);
                clb(null);
              }
            };

            col.isReplaying = true;
            col.replayingVms['423'] = { id: '423', cached: true, actionOnCommitForReplay: 'create' };
            col.replayingVmsToDelete['5123'] = { id: '5123', cached: true, actionOnCommitForReplay: 'delete' };
            col.saveReplayingVms(function (err) {
              expect(err).not.to.be.ok();
              expect(commitCalled.length).to.eql(2);
              expect(commitCalled[0].id).to.eql('5123');
              expect(commitCalled[1].id).to.eql('423');

              col.repository = orgRepo;
              col.isReplaying = false;
              col.replayingVms = {};
              col.replayingVmsToDelete = {};
              done();
            });

          });

        });

      });

      describe('having an empty read model', function () {

        beforeEach(function (done) {
          col.findViewModels(function (err, vms) {
            async.each(vms, function (vm, callback) {
              vm.destroy();
              col.saveViewModel(vm, callback);
            }, done)
          });
        });

        describe('calling loadViewModel', function() {

          it('it should callback with a new view model', function (done) {

            col.loadViewModel('vmId', function (err, vm) {
              expect(err).not.to.be.ok();
              expect(vm).to.be.an('object');
              expect(vm.get('my.def')).to.eql('data');
              done();
            });

          });

        });

        describe('calling findViewModels', function() {

          it('it should callback with an empty array', function (done) {

            col.findViewModels(function (err, vms) {
              expect(err).not.to.be.ok();
              expect(vms).to.be.an('array');
              expect(vms.length).to.eql(0);
              done();
            });

          });

        });

        describe('calling commit', function() {

          it('it should work as expected', function (done) {

            col.loadViewModel('vmId', function (err, vm) {
              expect(err).not.to.be.ok();
              expect(vm).to.be.an('object');
              expect(vm.get('my.def')).to.eql('data');

              vm.set('new', 'value');
              col.saveViewModel(vm, function (err) {
                expect(err).not.to.be.ok();

                col.loadViewModel('vmId', function (err, vm) {
                  expect(err).not.to.be.ok();
                  expect(vm).to.be.an('object');
                  expect(vm.get('my.def')).to.eql('data');
                  expect(vm.get('new')).to.eql('value');
                  expect(vm.toJSON().my.def).to.eql('data');
                  expect(vm.toJSON().new).to.eql('value');

                  col.findViewModels(function (err, vms) {
                    expect(err).not.to.be.ok();
                    expect(vms).to.be.an('array');
                    expect(vms.length).to.eql(1);
                    expect(vms[0].get('my.def')).to.eql('data');
                    expect(vms[0].get('new')).to.eql('value');

                    done();
                  });
                });
              });
            });

          });

        });

      });

      describe('having some viewmodels in the read model', function () {

        beforeEach(function (done) {
          col.findViewModels(function (err, vms) {
            async.each(vms, function (vm, callback) {
              vm.destroy();
              col.saveViewModel(vm, callback);
            }, function () {
              col.loadViewModel('4567', function (err, vm) {
                col.saveViewModel(vm, function (err) {
                  col.loadViewModel('4568', function (err, vm) {
                    col.saveViewModel(vm, done);
                  });
                });
              });
            })
          });
        });

        it('it should return all records within an array', function(done) {

          col.loadViewModel('4567', function (err, vm1) {
            col.loadViewModel('4568', function (err, vm2) {
              col.findViewModels(function (err, results) {
                expect(results).to.have.length(2);
                expect(results.toJSON).to.be.a('function');
                expect(results[0].id === vm1.id || results[1].id === vm1.id);
                expect(results[0].id === vm2.id || results[1].id === vm2.id);
                done();
              });
            });
          });

        });

        describe('calling toJSON on a result array', function() {

          it('it should return the correct data', function (done) {

            col.loadViewModel('4567', function (err, vm1) {
              vm1.set('my', 'data');
              col.saveViewModel(vm1, function (err) {
                col.loadViewModel('4568', function (err, vm2) {
                  col.findViewModels(function (err, results) {
                    var res = results.toJSON();
                    expect(res[0].id === vm1.id || res[1].id === vm1.id);
                    expect(res[0].id === vm2.id || res[1].id === vm2.id);
                    expect(res[0].my === 'data' || res[1].my === 'data');
                    done();
                  });
                });
              });
            });

          });

        });

        it('the containing objects should have an actionOnCommit property', function(done) {

          col.loadViewModel('4567', function (err, vm1) {
            col.loadViewModel('4568', function (err, vm2) {
              col.findViewModels(function (err, results) {
                expect(results[0]).to.be.an('object');
                expect(results[1]).to.be.an('object');
                done();
              });
            });
          });

        });

        it('the containing objects should have a set and a get and a destroy and a commit function', function(done) {

          col.loadViewModel('4567', function (err, vm1) {
            col.loadViewModel('4568', function (err, vm2) {
              col.findViewModels(function (err, results) {
                expect(results[0]).to.be.an('object');
                expect(results[1]).to.be.an('object');
                done();
              });
            });
          });

        });

        describe('with a query object', function() {

          describe('having no records', function() {

            beforeEach(function (done) {
              col.findViewModels(function (err, vms) {
                async.each(vms, function (vm, callback) {
                  vm.destroy();
                  col.saveViewModel(vm, callback);
                }, done)
              });
            });

            it('it should return an empty array', function(done) {

              col.findViewModels({}, function (err, results) {
                expect(results).to.be.an('array');
                expect(results).to.have.length(0);
                done();
              });

            });

          });

          describe('having any records', function() {

            beforeEach(function(done) {

              col.findViewModels(function (err, vms) {
                async.each(vms, function (vm, callback) {
                  vm.destroy();
                  col.saveViewModel(vm, callback);
                }, function () {
                  col.loadViewModel('4567', function (err, vm) {
                    vm.set('foo', 'bar');

                    col.saveViewModel(vm, function (err) {
                      col.loadViewModel('4568', function (err, vm2) {
                        vm2.set('foo', 'wat');
                        col.saveViewModel(vm2, done);
                      });
                    });
                  });
                })
              });

            });

            describe('not matching the query object', function() {

              it('it should return an empty array', function(done) {

                col.findViewModels({ foo: 'bas' }, function(err, results) {
                  expect(results).to.be.an('array');
                  expect(results).to.have.length(0);
                  done();
                });

              });

            });


            describe('matching the query object', function() {

              it('it should return all matching records within an array', function(done) {

                col.findViewModels({ foo: 'bar' }, function(err, results) {
                  expect(results).to.be.an('array');
                  expect(results).to.have.length(1);
                  done();
                });

              });

            });

            describe('matching the query object, that queries an array', function() {

              beforeEach(function(done) {

                col.loadViewModel('4567', function (err, vm) {
                  vm.set('foos', [ { foo: 'bar' } ]);
                  col.saveViewModel(vm, done);
                });

              });

              it('it should return all matching records within an array', function(done) {

                col.findViewModels({ 'foos.foo': 'bar' }, function(err, results) {
                  expect(results).to.be.an('array');
                  expect(results).to.have.length(1);
                  done();
                });

              });

            });

          });

        });

        describe('with query options', function () {

          beforeEach(function(done) {

            col.findViewModels(function (err, vms) {
              async.each(vms, function (vm, callback) {
                vm.destroy();
                col.saveViewModel(vm, callback);
              }, function () {
                col.loadViewModel('4567', function (err, vm) {
                  vm.set('foo', 'bar');

                  col.saveViewModel(vm, function (err) {
                    col.loadViewModel('4568', function (err, vm2) {
                      vm2.set('foo', 'wat');
                      col.saveViewModel(vm2, function(err) {
                        col.loadViewModel('4569', function(err, vm3) {

                          vm3.set('foo', 'bit');
                          col.saveViewModel(vm3, done);
                        });
                      });
                    });
                  });
                });
              })
            });

          });

          describe('for paging limit: 2, skip: 1', function () {

            it('it should work as expected', function (done) {

              col.findViewModels({}, {
                limit: 2,
                skip: 1
              }, function (err, results) {
                expect(results).to.be.an('array');
                expect(results.length).to.eql(2);
                expect(results.toJSON).to.be.a('function');
                expect(results[0].get('foo') === 'wat' || results[1].get('foo') === 'wat');
                expect(results[0].get('foo') === 'bit' || results[1].get('foo') === 'bit');

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
      expect(def.definitions.notification).to.be.an('object');
      expect(def.definitions.event).to.be.an('object');
      expect(def.defineNotification).to.be.a('function');
      expect(def.defineEvent).to.be.a('function');
      expect(def.defineOptions).to.be.a('function');

    });

    describe('passing a name in meta infos', function () {

      it('it should return a correct object', function () {

        var def = new DefinitionBase({ name: 'myName' });
        expect(def.name).to.eql('myName');
        expect(def.definitions).to.be.an('object');
        expect(def.definitions.notification).to.be.an('object');
        expect(def.definitions.event).to.be.an('object');
        expect(def.defineNotification).to.be.a('function');
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

    describe('defining the notification structure', function() {

      var def;

      beforeEach(function () {
        def = new DefinitionBase({ name: 'myName' });
      });

      describe('using the defaults', function () {

        it('it should apply the defaults', function() {

          var defaults = _.cloneDeep(def.definitions.notification);

          def.defineNotification({
            collection: 'col',
            payload: 'data',
            context: 'meta.context.name',
            aggregate: 'meta.aggregate.name'
          });

          expect(defaults.correlationId).to.eql(def.definitions.notification.correlationId);
          expect(defaults.id).to.eql(def.definitions.notification.id);
          expect(def.definitions.notification.payload).to.eql('data');
          expect(defaults.payload).not.to.eql(def.definitions.notification.payload);
          expect(def.definitions.notification.collection).to.eql('col');
          expect(defaults.collection).not.to.eql(def.definitions.notification.collection);
          expect(def.definitions.notification.context).to.eql('meta.context.name');
          expect(defaults.context).not.to.eql(def.definitions.notification.context);
          expect(def.definitions.notification.aggregate).to.eql('meta.aggregate.name');
          expect(defaults.aggregate).not.to.eql(def.definitions.notification.aggregate);
          expect(defaults.action).to.eql(def.definitions.notification.action);
          expect(defaults.meta).to.eql(def.definitions.notification.meta);

        });

      });

      describe('overwriting the defaults', function () {

        it('it should apply them correctly', function() {

          var defaults = _.cloneDeep(def.definitions.notification);

          def.defineNotification({
            correlationId: 'corrId',
            id: 'notId',
            action: 'n',
            collection: 'c',
            payload: 'p',
            context: 'ctx',
            aggregate: 'agg',
            aggregateId: 'aggId',
            revision: 'rev',
            eventId: 'evtId',
            event: 'evtName',
            meta: 'm'
          });

          expect(def.definitions.notification.correlationId).to.eql('corrId');
          expect(defaults.correlationId).not.to.eql(def.definitions.notification.correlationId);
          expect(def.definitions.notification.id).to.eql('notId');
          expect(defaults.id).not.to.eql(def.definitions.notification.id);
          expect(def.definitions.notification.action).to.eql('n');
          expect(defaults.action).not.to.eql(def.definitions.notification.action);
          expect(def.definitions.notification.collection).to.eql('c');
          expect(defaults.collection).not.to.eql(def.definitions.notification.collection);
          expect(def.definitions.notification.payload).to.eql('p');
          expect(defaults.payload).not.to.eql(def.definitions.notification.payload);
          expect(def.definitions.notification.context).to.eql('ctx');
          expect(defaults.context).not.to.eql(def.definitions.notification.context);
          expect(def.definitions.notification.aggregate).to.eql('agg');
          expect(defaults.aggregate).not.to.eql(def.definitions.notification.aggregate);
          expect(def.definitions.notification.aggregateId).to.eql('aggId');
          expect(defaults.aggregateId).not.to.eql(def.definitions.notification.aggregateId);
          expect(def.definitions.notification.revision).to.eql('rev');
          expect(defaults.revision).not.to.eql(def.definitions.notification.revision);
          expect(def.definitions.notification.eventId).to.eql('evtId');
          expect(defaults.eventId).not.to.eql(def.definitions.notification.eventId);
          expect(def.definitions.notification.event).to.eql('evtName');
          expect(defaults.event).not.to.eql(def.definitions.notification.event);
          expect(def.definitions.notification.meta).to.eql('m');
          expect(defaults.meta).not.to.eql(def.definitions.notification.meta);

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

## File: `test/unit/definitions/eventExtenderTest.js`
```javascript
var expect = require('expect.js'),
  _ = require('lodash'),
  DefinitionBase = require('../../../lib/definitionBase'),
  EventExtender = require('../../../lib/definitions/eventExtender'),
  api = require('../../../');

describe('eventExtender definition', function () {

  describe('creating a new eventExtender definition', function () {

    describe('without any arguments', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.defineEventExtender();
        }).to.throwError(/function/);

      });

    });

    describe('without eventExtender function', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.defineEventExtender(null);
        }).to.throwError(/function/);

      });

    });

    describe('with a wrong eventExtender function', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.defineEventExtender(null, 'not a function');
        }).to.throwError(/function/);

      });

    });

    describe('with a correct eventExtender function', function () {

      it('it should not throw an error', function () {

        expect(function () {
          api.defineEventExtender(null, function () {
          });
        }).not.to.throwError();

      });

      it('it should return a correct object', function () {

        var evtExtFn = function () {
        };
        var evtExt = api.defineEventExtender(null, evtExtFn);
        expect(evtExt).to.be.a(DefinitionBase);
        expect(evtExt).to.be.a(EventExtender);
        expect(evtExt.evtExtFn).to.eql(evtExtFn);
        expect(evtExt.definitions).to.be.an('object');
        expect(evtExt.definitions.notification).to.be.an('object');
        expect(evtExt.definitions.event).to.be.an('object');
        expect(evtExt.defineNotification).to.be.a('function');
        expect(evtExt.defineEvent).to.be.a('function');
        expect(evtExt.defineOptions).to.be.a('function');

        expect(evtExt.extend).to.be.a('function');
        expect(evtExt.useCollection).to.be.a('function');

      });

    });

    describe('with some meta infos and a correct eventExtender function', function () {

      it('it should not throw an error', function () {

        expect(function () {
          api.defineEventExtender({ name: 'eventName', version: 3 }, function () {
          });
        }).not.to.throwError();

      });

      it('it should return a correct object', function () {

        var evtExtFn = function () {
        };
        var evtExt = api.defineEventExtender({ name: 'eventName', version: 3 }, evtExtFn);
        expect(evtExt).to.be.a(DefinitionBase);
        expect(evtExt).to.be.a(EventExtender);
        expect(evtExt.evtExtFn).to.eql(evtExtFn);
        expect(evtExt.definitions).to.be.an('object');
        expect(evtExt.definitions.notification).to.be.an('object');
        expect(evtExt.definitions.event).to.be.an('object');
        expect(evtExt.defineNotification).to.be.a('function');
        expect(evtExt.defineEvent).to.be.a('function');
        expect(evtExt.defineOptions).to.be.a('function');

        expect(evtExt.extend).to.be.a('function');
        expect(evtExt.useCollection).to.be.a('function');

      });

    });

    describe('extending an event', function () {

      var evtExt;

      describe('having an event extender function that wants expects 3 arguments', function () {

        describe('not defining an id', function () {

          it('it should work as expected', function (done) {
            var extendedEvt = { ext: 'evt' };
            var evtExtFn = function (evt, col, callback) {
              expect(evt.my).to.eql('evt');
              expect(col.name).to.eql('myCol');
              callback(null, extendedEvt);
            };
            evtExt = api.defineEventExtender({
              name: 'eventName',
              version: 3
            }, evtExtFn);

            evtExt.useCollection({
              name: 'myCol'
            });

            evtExt.extend({ my: 'evt' }, function (err, eEvt) {
              expect(err).not.to.be.ok();
              expect(eEvt).to.eql(extendedEvt);
              done();
            });
          });

        });

        describe('defining an id', function () {

          it('it should work as expected', function (done) {
            var viewM = { my: 'view' };
            var extendedEvt = { ext: 'evt', myId: '1234' };
            var evtExtFn = function (evt, vm, callback) {
              expect(evt.my).to.eql('evt');
              expect(vm.id).to.eql('1234');
              callback(null, extendedEvt);
            };
            evtExt = api.defineEventExtender({
              name: 'eventName',
              version: 3,
              id: 'myId'
            }, evtExtFn);

            evtExt.useCollection({
              name: 'myCol',
              getNewId: function (callback) { callback(null, 'newId'); },
              loadViewModel: function (id, callback) { viewM.id = id; callback(null, viewM); }
            });

            evtExt.extend({ my: 'evt', myId: '1234' }, function (err, eEvt) {
              expect(err).not.to.be.ok();
              expect(eEvt).to.eql(extendedEvt);
              done();
            });
          });

        });

      });

      describe('having an event extender function that wants expects 1 argument', function () {

        it('it should work as expected', function (done) {
          var extendedEvt = { ext: 'evt' };
          var evtExtFn = function (evt) {
            expect(evt.my).to.eql('evt');
            return extendedEvt;
          };
          evtExt = api.defineEventExtender({
            name: 'eventName',
            version: 3
          }, evtExtFn);

          evtExt.useCollection({
            name: 'myCol'
          });

          evtExt.extend({ my: 'evt' }, function (err, eEvt) {
            expect(err).not.to.be.ok();
            expect(eEvt).to.eql(extendedEvt);
            done();
          });
        });

      });

      describe('having an event extender function that wants expects 2 argument', function () {

        describe('not defining an id', function () {

          it('it should work as expected', function (done) {
            var extendedEvt = { ext: 'evt' };
            var evtExtFn = function (evt, callback) {
              expect(evt.my).to.eql('evt');
              callback(null, extendedEvt);
            };
            evtExt = api.defineEventExtender({
              name: 'eventName',
              version: 3
            }, evtExtFn);

            evtExt.useCollection({
              name: 'myCol'
            });

            evtExt.extend({ my: 'evt' }, function (err, eEvt) {
              expect(err).not.to.be.ok();
              expect(eEvt).to.eql(extendedEvt);
              done();
            });
          });

        });

        describe('defining an id', function () {

          describe('but not passing it in the event', function () {

            it('it should work as expected', function (done) {
              var extendedEvt = { ext: 'evt' };
              var viewM = { my: 'view' };
              var evtExtFn = function (evt, vm) {
                expect(evt.my).to.eql('evt');
                expect(vm).to.eql(viewM);
                expect(vm.id).to.eql('newId');
                return extendedEvt;
              };
              evtExt = api.defineEventExtender({
                name: 'eventName',
                version: 3,
                id: 'id'
              }, evtExtFn);

              evtExt.useCollection({
                name: 'myCol',
                getNewId: function (callback) { callback(null, 'newId'); },
                loadViewModel: function (id, callback) { viewM.id = id; callback(null, viewM); }
              });

              evtExt.extend({ my: 'evt' }, function (err, eEvt) {
                expect(err).not.to.be.ok();
                expect(eEvt).to.eql(extendedEvt);
                done();
              });
            });

          });

          describe('and passing it in the event', function () {

            it('it should work as expected', function (done) {
              var extendedEvt = { ext: 'evt' };
              var viewM = { my: 'view' };
              var evtExtFn = function (evt, vm) {
                expect(evt.my).to.eql('evt');
                expect(vm).to.eql(viewM);
                expect(vm.id).to.eql('idInEvt');
                return extendedEvt;
              };
              evtExt = api.defineEventExtender({
                name: 'eventName',
                version: 3,
                id: 'id'
              }, evtExtFn);

              evtExt.useCollection({
                name: 'myCol',
                getNewId: function (callback) { callback(null, 'newId'); },
                loadViewModel: function (id, callback) { viewM.id = id; callback(null, viewM); }
              });

              evtExt.extend({ my: 'evt', id: 'idInEvt' }, function (err, eEvt) {
                expect(err).not.to.be.ok();
                expect(eEvt).to.eql(extendedEvt);
                done();
              });
            });

          });

        });

      });

    });

    describe('defining an use as id function', function() {
      var evtExt;

      beforeEach(function () {
        evtExt = api.defineEventExtender({ name: 'eventName' }, function () {});
        evtExt.getNewIdForThisEventExtender = null;
      });

      describe('in a synchronous way', function() {
        it('it should be transformed internally to an asynchronous way', function(done) {
          evtExt.useAsId(function(evt) {
            expect(evt.my).to.eql('evt');
            return 'freshly-generated';
          });

          evtExt.extractId({ my: 'evt' }, function(err,id) {
            expect(id).to.eql('freshly-generated');
            done();
          });
        });
      });

      describe('in an asynchronous way', function() {

        it('it should be taken as it is', function(done) {
          evtExt.useAsId(function(evt, callback) {
            expect(evt.my).to.eql('evt');
            callback(null, 'freshly-generated');
          });

          evtExt.extractId({ my: 'evt' }, function(err, id) {
            expect(id).to.eql('freshly-generated');
            done();
          });
        });
      });      
      
    });    
    

  });

});
```

## File: `test/unit/definitions/preEventExtenderTest.js`
```javascript
var expect = require('expect.js'),
  _ = require('lodash'),
  DefinitionBase = require('../../../lib/definitionBase'),
  PreEventExtender = require('../../../lib/definitions/preEventExtender'),
  api = require('../../../');

describe('preEventExtender definition', function () {

  describe('creating a new preEventExtender definition', function () {

    describe('without any arguments', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.definePreEventExtender();
        }).to.throwError(/function/);

      });

    });

    describe('without preEventExtender function', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.definePreEventExtender(null);
        }).to.throwError(/function/);

      });

    });

    describe('with a wrong preEventExtender function', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.definePreEventExtender(null, 'not a function');
        }).to.throwError(/function/);

      });

    });

    describe('with a correct preEventExtender function', function () {

      it('it should not throw an error', function () {

        expect(function () {
          api.definePreEventExtender(null, function () {
          });
        }).not.to.throwError();

      });

      it('it should return a correct object', function () {

        var evtExtFn = function () {
        };
        var evtExt = api.definePreEventExtender(null, evtExtFn);
        expect(evtExt).to.be.a(DefinitionBase);
        expect(evtExt).to.be.a(PreEventExtender);
        expect(evtExt.evtExtFn).to.eql(evtExtFn);
        expect(evtExt.definitions).to.be.an('object');
        expect(evtExt.definitions.notification).to.be.an('object');
        expect(evtExt.definitions.event).to.be.an('object');
        expect(evtExt.defineNotification).to.be.a('function');
        expect(evtExt.defineEvent).to.be.a('function');
        expect(evtExt.defineOptions).to.be.a('function');

        expect(evtExt.extend).to.be.a('function');
        expect(evtExt.useCollection).to.be.a('function');

      });

    });

    describe('with some meta infos and a correct preEventExtender function', function () {

      it('it should not throw an error', function () {

        expect(function () {
          api.definePreEventExtender({ name: 'eventName', version: 3 }, function () {
          });
        }).not.to.throwError();

      });

      it('it should return a correct object', function () {

        var evtExtFn = function () {
        };
        var evtExt = api.definePreEventExtender({ name: 'eventName', version: 3 }, evtExtFn);
        expect(evtExt).to.be.a(DefinitionBase);
        expect(evtExt).to.be.a(PreEventExtender);
        expect(evtExt.evtExtFn).to.eql(evtExtFn);
        expect(evtExt.definitions).to.be.an('object');
        expect(evtExt.definitions.notification).to.be.an('object');
        expect(evtExt.definitions.event).to.be.an('object');
        expect(evtExt.defineNotification).to.be.a('function');
        expect(evtExt.defineEvent).to.be.a('function');
        expect(evtExt.defineOptions).to.be.a('function');

        expect(evtExt.extend).to.be.a('function');
        expect(evtExt.useCollection).to.be.a('function');

      });

    });

    describe('extending an event', function () {

      var evtExt;

      describe('having an event extender function that wants expects 3 arguments', function () {

        describe('not defining an id', function () {

          it('it should work as expected', function (done) {
            var extendedEvt = { ext: 'evt' };
            var evtExtFn = function (evt, col, callback) {
              expect(evt.my).to.eql('evt');
              expect(col.name).to.eql('myCol');
              callback(null, extendedEvt);
            };
            evtExt = api.definePreEventExtender({
              name: 'eventName',
              version: 3
            }, evtExtFn);

            evtExt.useCollection({
              name: 'myCol'
            });

            evtExt.extend({ my: 'evt' }, function (err, eEvt) {
              expect(err).not.to.be.ok();
              expect(eEvt).to.eql(extendedEvt);
              done();
            });
          });

        });

        describe('defining an id', function () {

          it('it should work as expected', function (done) {
            var viewM = { my: 'view' };
            var extendedEvt = { ext: 'evt', myId: '1234' };
            var evtExtFn = function (evt, vm, callback) {
              expect(evt.my).to.eql('evt');
              expect(vm.id).to.eql('1234');
              callback(null, extendedEvt);
            };
            evtExt = api.definePreEventExtender({
              name: 'eventName',
              version: 3,
              id: 'myId'
            }, evtExtFn);

            evtExt.useCollection({
              name: 'myCol',
              getNewId: function (callback) { callback(null, 'newId'); },
              loadViewModel: function (id, callback) { viewM.id = id; callback(null, viewM); }
            });

            evtExt.extend({ my: 'evt', myId: '1234' }, function (err, eEvt) {
              expect(err).not.to.be.ok();
              expect(eEvt).to.eql(extendedEvt);
              done();
            });
          });

        });

      });

      describe('having an event extender function that wants expects 1 argument', function () {

        it('it should work as expected', function (done) {
          var extendedEvt = { ext: 'evt' };
          var evtExtFn = function (evt) {
            expect(evt.my).to.eql('evt');
            return extendedEvt;
          };
          evtExt = api.definePreEventExtender({
            name: 'eventName',
            version: 3
          }, evtExtFn);

          evtExt.useCollection({
            name: 'myCol'
          });

          evtExt.extend({ my: 'evt' }, function (err, eEvt) {
            expect(err).not.to.be.ok();
            expect(eEvt).to.eql(extendedEvt);
            done();
          });
        });

      });

      describe('having an event extender function that wants expects 2 argument', function () {

        describe('not defining an id', function () {

          it('it should work as expected', function (done) {
            var extendedEvt = { ext: 'evt' };
            var evtExtFn = function (evt, callback) {
              expect(evt.my).to.eql('evt');
              callback(null, extendedEvt);
            };
            evtExt = api.definePreEventExtender({
              name: 'eventName',
              version: 3
            }, evtExtFn);

            evtExt.useCollection({
              name: 'myCol'
            });

            evtExt.extend({ my: 'evt' }, function (err, eEvt) {
              expect(err).not.to.be.ok();
              expect(eEvt).to.eql(extendedEvt);
              done();
            });
          });

        });

        describe('defining an id', function () {

          describe('but not passing it in the event', function () {

            it('it should work as expected', function (done) {
              var extendedEvt = { ext: 'evt' };
              var viewM = { my: 'view' };
              var evtExtFn = function (evt, vm) {
                expect(evt.my).to.eql('evt');
                expect(vm).to.eql(viewM);
                expect(vm.id).to.eql('newId');
                return extendedEvt;
              };
              evtExt = api.definePreEventExtender({
                name: 'eventName',
                version: 3,
                id: 'id'
              }, evtExtFn);

              evtExt.useCollection({
                name: 'myCol',
                getNewId: function (callback) { callback(null, 'newId'); },
                loadViewModel: function (id, callback) { viewM.id = id; callback(null, viewM); }
              });

              evtExt.extend({ my: 'evt' }, function (err, eEvt) {
                expect(err).not.to.be.ok();
                expect(eEvt).to.eql(extendedEvt);
                done();
              });
            });

          });

          describe('and passing it in the event', function () {

            it('it should work as expected', function (done) {
              var extendedEvt = { ext: 'evt' };
              var viewM = { my: 'view' };
              var evtExtFn = function (evt, vm) {
                expect(evt.my).to.eql('evt');
                expect(vm).to.eql(viewM);
                expect(vm.id).to.eql('idInEvt');
                return extendedEvt;
              };
              evtExt = api.definePreEventExtender({
                name: 'eventName',
                version: 3,
                id: 'id'
              }, evtExtFn);

              evtExt.useCollection({
                name: 'myCol',
                getNewId: function (callback) { callback(null, 'newId'); },
                loadViewModel: function (id, callback) { viewM.id = id; callback(null, viewM); }
              });

              evtExt.extend({ my: 'evt', id: 'idInEvt' }, function (err, eEvt) {
                expect(err).not.to.be.ok();
                expect(eEvt).to.eql(extendedEvt);
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

## File: `test/unit/definitions/viewBuilderTest.js`
```javascript
var expect = require('expect.js'),
  _ = require('lodash'),
  DefinitionBase = require('../../../lib/definitionBase'),
  ViewBuilder = require('../../../lib/definitions/viewBuilder'),
  api = require('../../../');

describe('viewBuilder definition', function () {

  describe('creating a new viewBuilder definition', function () {

    describe('without any arguments', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.defineViewBuilder();
        }).to.throwError(/function/);

      });

    });

    describe('without denorm function', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.defineViewBuilder(null);
        }).to.throwError(/function/);

      });

    });

    describe('with a wrong denorm function', function () {

      it('it should throw an error', function () {

        expect(function () {
          api.defineViewBuilder(null, 2);
        }).to.throwError(/function/);

      });

    });

    describe('with a correct denorm function', function () {

      describe('like a function', function () {

        it('it should not throw an error', function () {

          expect(function () {
            api.defineViewBuilder(null, function () {
            });
          }).not.to.throwError();

        });

        it('it should return a correct object', function () {

          var denormFn = function () {
          };
          var vb = api.defineViewBuilder(null, denormFn);
          expect(vb).to.be.a(DefinitionBase);
          expect(vb).to.be.a(ViewBuilder);
          expect(vb.denormFn).to.be.a('function');
          expect(vb.definitions).to.be.an('object');
          expect(vb.definitions.notification).to.be.an('object');
          expect(vb.definitions.event).to.be.an('object');
          expect(vb.defineNotification).to.be.a('function');
          expect(vb.defineEvent).to.be.a('function');
          expect(vb.defineOptions).to.be.a('function');

          expect(vb.idGenerator).to.be.a('function');
          expect(vb.useCollection).to.be.a('function');
          expect(vb.loadViewModel).to.be.a('function');
          expect(vb.saveViewModel).to.be.a('function');
          expect(vb.extractId).to.be.a('function');
          expect(vb.generateNotification).to.be.a('function');
          expect(vb.denormalize).to.be.a('function');

        });

      });

      describe('like a function string', function () {

        it('it should not throw an error', function () {

          expect(function () {
            api.defineViewBuilder(null, 'update');
          }).not.to.throwError();

        });

        it('it should return a correct object', function () {

          var vb = api.defineViewBuilder(null, 'delete');
          expect(vb).to.be.a(DefinitionBase);
          expect(vb).to.be.a(ViewBuilder);
          expect(vb.denormFn).to.be.a('function');
          expect(vb.definitions).to.be.an('object');
          expect(vb.definitions.notification).to.be.an('object');
          expect(vb.definitions.event).to.be.an('object');
          expect(vb.defineNotification).to.be.a('function');
          expect(vb.defineEvent).to.be.a('function');
          expect(vb.defineOptions).to.be.a('function');

          expect(vb.idGenerator).to.be.a('function');
          expect(vb.useCollection).to.be.a('function');
          expect(vb.findViewModels).to.be.a('function');
          expect(vb.loadViewModel).to.be.a('function');
          expect(vb.saveViewModel).to.be.a('function');
          expect(vb.extractId).to.be.a('function');
          expect(vb.generateNotification).to.be.a('function');
          expect(vb.denormalize).to.be.a('function');

        });

      });

    });

    describe('defining an use as id function', function() {
      var vb;

      beforeEach(function () {
        vb = api.defineViewBuilder({ name: 'eventName', version: 4 }, 'create');
        vb.getNewIdForThisViewModel = null;
      });

      describe('in a synchronous way', function() {
        it('it should be transformed internally to an asynchronous way', function(done) {
          vb.useAsId(function(evt) {
            expect(evt.my).to.eql('evt');
            return 'freshly-generated';
          });

          vb.extractId({ my: 'evt' }, function(err,id) {
            expect(id).to.eql('freshly-generated');
            done();
          });
        });
      });

      describe('in an asynchronous way', function() {

        it('it should be taken as it is', function(done) {
          vb.useAsId(function(evt, callback) {
            expect(evt.my).to.eql('evt');
            callback(null, 'freshly-generated');
          });

          vb.extractId({ my: 'evt' }, function(err, id) {
            expect(id).to.eql('freshly-generated');
            done();
          });
        });
      });      
      
    });    

    describe('defining an id generator function', function () {

      var vb;

      beforeEach(function () {
        vb = api.defineViewBuilder({ name: 'eventName', version: 3 }, 'create');
        vb.getNewId = null;
      });

      describe('in a synchronous way', function () {

        it('it should be transformed internally to an asynchronous way', function (done) {

          vb.idGenerator(function () {
            var id = require('uuid').v4().toString();
            return id;
          });

          vb.getNewId(function (err, id) {
            expect(id).to.be.a('string');
            done();
          });

        });

      });

      describe('in an synchronous way', function () {

        it('it should be taken as it is', function (done) {

          vb.idGenerator(function (callback) {
            setTimeout(function () {
              var id = require('uuid').v4().toString();
              callback(null, id);
            }, 10);
          });

          vb.getNewId(function (err, id) {
            expect(id).to.be.a('string');
            done();
          });

        });

      });

    });

    describe('calling useCollection', function () {

      var vb;

      before(function () {
        vb = api.defineViewBuilder(null, 'update');
      });

      it('it should work as expected', function () {

        var col = { name: 'dummy' };
        vb.useCollection(col);
        expect(vb.collection).to.eql(col);

      });

    });

    describe('calling loadViewModel', function () {

      var vb;

      beforeEach(function () {
        vb = api.defineViewBuilder(null, 'update');
      });

      it('it should work as expected', function (done) {

        var col = { name: 'dummy', loadViewModel: function (id, callback) {
          callback(null, { id: id });
        }};
        vb.useCollection(col);
        vb.loadViewModel('423', function (err, vm) {
          expect(err).not.to.be.ok();
          expect(vm.id).to.eql('423');
          done();
        });

      });

    });

    describe('calling saveViewModel', function () {

      var vb;

      beforeEach(function () {
        vb = api.defineViewBuilder(null, 'update');
      });

      it('it should work as expected', function (done) {

        var called = false;
        var col = { name: 'dummy', saveViewModel: function (vm, callback) {
          expect(vm.id).to.eql('423');
          called = true;
          callback(null);
        }};
        vb.useCollection(col);
        vb.saveViewModel({ id: '423' }, function (err) {
          expect(err).not.to.be.ok();
          expect(called).to.eql(true);
          done();
        });

      });

    });

    describe('calling extractId', function () {

      var vb;

      beforeEach(function () {
        vb = api.defineViewBuilder({ id: 'myId' }, 'update');
      });

      describe('not passing that id', function () {

        it('it should work as expected', function (done) {

          var col = { name: 'dummy', getNewId: function (callback) {
            callback(null, 'newId');
          }};
          vb.useCollection(col);
          vb.extractId({ id: '423' }, function (err, id) {
            expect(err).not.to.be.ok();
            expect(id).to.eql('newId');
            done();
          });

        });

      });

      describe('passing that id', function () {

        it('it should work as expected', function (done) {

          var col = { name: 'dummy', getNewId: function (callback) {
            callback(null, 'newId');
          }};
          vb.useCollection(col);
          vb.extractId({ myId: '423' }, function (err, id) {
            expect(err).not.to.be.ok();
            expect(id).to.eql('423');
            done();
          });

        });

      });

    });

    describe('calling generateNotification', function () {

      var vb;

      beforeEach(function () {
        vb = api.defineViewBuilder(null, 'update');
      });

      it('it should work as expected', function () {

        vb.defineEvent({
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

        vb.defineNotification({
          correlationId: 'correlationId',
          id: 'id',
          action: 'name',
          collection: 'collection',
          payload: 'payload',
          context: 'meta.context.name',
          aggregate: 'meta.aggregate.name',
          aggregateId: 'meta.aggregate.id',
          revision: 'meta.aggregate.revision',
          eventId: 'meta.event.id',
          event: 'meta.event.name',
          meta: 'meta'
        });

        var col = { name: 'dummy' };
        vb.useCollection(col);

        var evt = {
          correlationId: 'cmdId',
          id: 'evtId',
          name: 'enteredNewPerson',
          aggregate: {
            id: 'aggId',
            name: 'person'
          },
          context: {
            name: 'hr'
          },
          payload: {
            firstname: 'Jack',
            lastname: 'Joe'
          },
          revision: 1,
          version: 4,
          meta: {
            userId: 'usrId'
          }
        };

        var vm = {
          actionOnCommit: 'update',
          toJSON: function () {
            return { vmAs: 'json' };
          }
        };

        var noti = vb.generateNotification(evt, vm);

        expect(noti.meta.userId).to.eql('usrId');
        expect(noti.meta.event.id).to.eql('evtId');
        expect(noti.meta.event.name).to.eql('enteredNewPerson');
        expect(noti.meta.aggregate.id).to.eql('aggId');
        expect(noti.meta.aggregate.name).to.eql('person');
        expect(noti.meta.aggregate.revision).to.eql(1);
        expect(noti.meta.context.name).to.eql('hr');
        expect(noti.correlationId).to.eql('cmdId');
        expect(noti.payload.vmAs).to.eql('json');
        expect(noti.collection).to.eql('dummy');
        expect(noti.name).to.eql('update');

      });

    });

    describe('denormalizing an event', function () {

      describe('defining a payload', function () {

        it('it should work as expected', function (done) {

          var vb = api.defineViewBuilder({ payload: 'payload' }, 'update');

          vb.defineEvent({
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

          vb.defineNotification({
            correlationId: 'correlationId',
            id: 'id',
            action: 'name',
            collection: 'collection',
            payload: 'payload',
            context: 'meta.context.name',
            aggregate: 'meta.aggregate.name',
            aggregateId: 'meta.aggregate.id',
            revision: 'meta.aggregate.revision',
            eventId: 'meta.event.id',
            event: 'meta.event.name',
            meta: 'meta'
          });

          var vm = {
            actionOnCommit: 'update',
            set: function (data) {
              this.attr = data;
            },
            toJSON: function () {
              return this.attr;
            }
          };

          var col = { name: 'dummy',
            getNewId: function (callback) { callback(null, 'newId'); },
            loadViewModel: function (id, callback) {
              vm.id = id;
              callback(null, vm);
            },
            saveViewModel: function (vm, callback) {
              expect(vm.attr.firstname).to.eql('Jack');
              expect(vm.attr.lastname).to.eql('Joe');
              callback(null);
            }
          };
          vb.useCollection(col);

          var evt = {
            correlationId: 'cmdId',
            id: 'evtId',
            name: 'enteredNewPerson',
            aggregate: {
              id: 'aggId',
              name: 'person'
            },
            context: {
              name: 'hr'
            },
            payload: {
              firstname: 'Jack',
              lastname: 'Joe'
            },
            revision: 1,
            version: 4,
            meta: {
              userId: 'usrId'
            }
          };

          vb.denormalize(evt, function (err, notis) {
            expect(err).not.to.be.ok();
            expect(notis.length).to.eql(1);
            expect(notis[0].payload.firstname).to.eql('Jack');
            expect(notis[0].payload.lastname).to.eql('Joe');
            done();
          });

        });

      });

      describe('not defining a payload', function () {

        it('it should work as expected', function (done) {

          var vb = api.defineViewBuilder({}, function (evt, vm) {
            expect(this.retry).to.be.a('function');
            evt.deep = 'duup';
            vm.set(evt.payload);
          });

          vb.defineEvent({
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

          vb.defineNotification({
            correlationId: 'correlationId',
            id: 'id',
            action: 'name',
            collection: 'collection',
            payload: 'payload',
            context: 'meta.context.name',
            aggregate: 'meta.aggregate.name',
            aggregateId: 'meta.aggregate.id',
            revision: 'meta.aggregate.revision',
            eventId: 'meta.event.id',
            event: 'meta.event.name',
            meta: 'meta'
          });

          var vm = {
            actionOnCommit: 'update',
            set: function (data) {
              this.attr = data;
            },
            toJSON: function () {
              return this.attr;
            }
          };

          var col = { name: 'dummy',
            getNewId: function (callback) { callback(null, 'newId'); },
            loadViewModel: function (id, callback) {
              vm.id = id;
              callback(null, vm);
            },
            saveViewModel: function (vm, callback) {
              expect(vm.attr.firstname).to.eql('Jack');
              expect(vm.attr.lastname).to.eql('Joe');
              callback(null);
            }
          };
          vb.useCollection(col);

          var evt = {
            correlationId: 'cmdId',
            id: 'evtId',
            name: 'enteredNewPerson',
            aggregate: {
              id: 'aggId',
              name: 'person'
            },
            context: {
              name: 'hr'
            },
            payload: {
              firstname: 'Jack',
              lastname: 'Joe'
            },
            revision: 1,
            version: 4,
            meta: {
              userId: 'usrId'
            }
          };

          vb.denormalize(evt, function (err, notis) {
            expect(err).not.to.be.ok();
            expect(notis.length).to.eql(1);
            expect(notis[0].payload.firstname).to.eql('Jack');
            expect(notis[0].payload.lastname).to.eql('Joe');

            expect(evt.deep).not.to.be.ok();
            done();
          });

        });

      });

      describe('defining a query', function () {

        describe('as json object', function () {

          it('it should work as expected', function (done) {

            var counter = 0;

            var vb = api.defineViewBuilder({ query: { my: 'query' } }, function (evt, vm) {
              vm.set({ index: counter++ });
            });

            vb.defineEvent({
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

            vb.defineNotification({
              correlationId: 'correlationId',
              id: 'id',
              action: 'name',
              collection: 'collection',
              payload: 'payload',
              context: 'meta.context.name',
              aggregate: 'meta.aggregate.name',
              aggregateId: 'meta.aggregate.id',
              revision: 'meta.aggregate.revision',
              eventId: 'meta.event.id',
              event: 'meta.event.name',
              meta: 'meta'
            });

            var vm1 = {
              actionOnCommit: 'update',
              set: function (data) {
                this.attr = data;
              },
              toJSON: function () {
                return this.attr;
              }
            };

            var vm2 = {
              actionOnCommit: 'update',
              set: function (data) {
                this.attr = data;
              },
              toJSON: function () {
                return this.attr;
              }
            };

            var col = { name: 'dummy',
              getNewId: function (callback) { callback(null, 'newId'); },
              saveViewModel: function (vm, callback) {
                if (counter === 1) {
                  expect(vm.attr.index).to.eql(0);
                } else {
                  expect(vm.attr.index).to.eql(1);
                }
                callback(null);
              },
              findViewModels: function (query, queryOptions, callback) {
                expect(query.my).to.eql('query');
                callback(null, [vm1, vm2]);
              }
            };
            vb.useCollection(col);

            var evt = {
              correlationId: 'cmdId',
              id: 'evtId',
              name: 'enteredNewPerson',
              aggregate: {
                id: 'aggId',
                name: 'person'
              },
              context: {
                name: 'hr'
              },
              payload: {
                firstname: 'Jack',
                lastname: 'Joe'
              },
              revision: 1,
              version: 4,
              meta: {
                userId: 'usrId'
              }
            };

            vb.denormalize(evt, function (err, notis) {
              expect(err).not.to.be.ok();
              expect(notis.length).to.eql(2);
              expect(notis[0].payload.index).to.eql(0);
              expect(notis[1].payload.index).to.eql(1);

              expect(evt.deep).not.to.be.ok();
              done();
            });

          });

        });

        describe('as function', function () {

          it('it should work as expected', function (done) {

            var counter = 0;

            var vb = api.defineViewBuilder({  }, function (evt, vm) {
              vm.set({ index: counter++ });
            }).useAsQuery(function (evt) {
              return { my: evt.payload.firstname };
            });

            vb.defineEvent({
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

            vb.defineNotification({
              correlationId: 'correlationId',
              id: 'id',
              action: 'name',
              collection: 'collection',
              payload: 'payload',
              context: 'meta.context.name',
              aggregate: 'meta.aggregate.name',
              aggregateId: 'meta.aggregate.id',
              revision: 'meta.aggregate.revision',
              eventId: 'meta.event.id',
              event: 'meta.event.name',
              meta: 'meta'
            });

            var vm1 = {
              actionOnCommit: 'update',
              set: function (data) {
                this.attr = data;
              },
              toJSON: function () {
                return this.attr;
              }
            };

            var vm2 = {
              actionOnCommit: 'update',
              set: function (data) {
                this.attr = data;
              },
              toJSON: function () {
                return this.attr;
              }
            };

            var col = { name: 'dummy',
              getNewId: function (callback) { callback(null, 'newId'); },
              saveViewModel: function (vm, callback) {
                if (counter === 1) {
                  expect(vm.attr.index).to.eql(0);
                } else {
                  expect(vm.attr.index).to.eql(1);
                }
                callback(null);
              },
              findViewModels: function (query, queryOptions, callback) {
                expect(query.my).to.eql('Jack');
                callback(null, [vm1, vm2]);
              }
            };
            vb.useCollection(col);

            var evt = {
              correlationId: 'cmdId',
              id: 'evtId',
              name: 'enteredNewPerson',
              aggregate: {
                id: 'aggId',
                name: 'person'
              },
              context: {
                name: 'hr'
              },
              payload: {
                firstname: 'Jack',
                lastname: 'Joe'
              },
              revision: 1,
              version: 4,
              meta: {
                userId: 'usrId'
              }
            };

            vb.denormalize(evt, function (err, notis) {
              expect(err).not.to.be.ok();
              expect(notis.length).to.eql(2);
              expect(notis[0].payload.index).to.eql(0);
              expect(notis[1].payload.index).to.eql(1);

              expect(evt.deep).not.to.be.ok();
              done();
            });

          });

        });

        describe('as async function', function () {

          it('it should work as expected', function (done) {

            var counter = 0;

            var vb = api.defineViewBuilder({  }, function (evt, vm) {
              vm.set({ index: counter++ });
            }).useAsQuery(function (evt, callback) {
              callback(null, { my: evt.payload.firstname });
            });

            vb.defineEvent({
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

            vb.defineNotification({
              correlationId: 'correlationId',
              id: 'id',
              action: 'name',
              collection: 'collection',
              payload: 'payload',
              context: 'meta.context.name',
              aggregate: 'meta.aggregate.name',
              aggregateId: 'meta.aggregate.id',
              revision: 'meta.aggregate.revision',
              eventId: 'meta.event.id',
              event: 'meta.event.name',
              meta: 'meta'
            });

            var vm1 = {
              actionOnCommit: 'update',
              set: function (data) {
                this.attr = data;
              },
              toJSON: function () {
                return this.attr;
              }
            };

            var vm2 = {
              actionOnCommit: 'update',
              set: function (data) {
                this.attr = data;
              },
              toJSON: function () {
                return this.attr;
              }
            };

            var col = { name: 'dummy',
              getNewId: function (callback) { callback(null, 'newId'); },
              saveViewModel: function (vm, callback) {
                if (counter === 1) {
                  expect(vm.attr.index).to.eql(0);
                } else {
                  expect(vm.attr.index).to.eql(1);
                }
                callback(null);
              },
              findViewModels: function (query, queryOptions, callback) {
                expect(query.my).to.eql('Jack');
                callback(null, [vm1, vm2]);
              }
            };
            vb.useCollection(col);

            var evt = {
              correlationId: 'cmdId',
              id: 'evtId',
              name: 'enteredNewPerson',
              aggregate: {
                id: 'aggId',
                name: 'person'
              },
              context: {
                name: 'hr'
              },
              payload: {
                firstname: 'Jack',
                lastname: 'Joe'
              },
              revision: 1,
              version: 4,
              meta: {
                userId: 'usrId'
              }
            };

            vb.denormalize(evt, function (err, notis) {
              expect(err).not.to.be.ok();
              expect(notis.length).to.eql(2);
              expect(notis[0].payload.index).to.eql(0);
              expect(notis[1].payload.index).to.eql(1);

              expect(evt.deep).not.to.be.ok();
              done();
            });

          });

        });

      });

      describe('defining a function with a callback', function () {

        it('it should work as expected', function (done) {

          var vb = api.defineViewBuilder({}, function (evt, vm, clb) {
            expect(this.retry).to.be.a('function');
            expect(this.remindMe).to.be.a('function');
            expect(this.getReminder).to.be.a('function');
            var self = this;
            setTimeout(function () {
              expect(self.retry).to.be.a('function');
              expect(self.remindMe).to.be.a('function');
              expect(self.getReminder).to.be.a('function');
              evt.deep = 'duup';
              vm.set(evt.payload);
              clb();
            });
          });

          vb.defineEvent({
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

          vb.defineNotification({
            correlationId: 'correlationId',
            id: 'id',
            action: 'name',
            collection: 'collection',
            payload: 'payload',
            context: 'meta.context.name',
            aggregate: 'meta.aggregate.name',
            aggregateId: 'meta.aggregate.id',
            revision: 'meta.aggregate.revision',
            eventId: 'meta.event.id',
            event: 'meta.event.name',
            meta: 'meta'
          });

          var vm = {
            actionOnCommit: 'update',
            set: function (data) {
              this.attr = data;
            },
            toJSON: function () {
              return this.attr;
            }
          };

          var col = { name: 'dummy',
            getNewId: function (callback) { callback(null, 'newId'); },
            loadViewModel: function (id, callback) {
              vm.id = id;
              callback(null, vm);
            },
            saveViewModel: function (vm, callback) {
              expect(vm.attr.firstname).to.eql('Jack');
              expect(vm.attr.lastname).to.eql('Joe');
              callback(null);
            }
          };
          vb.useCollection(col);

          var evt = {
            correlationId: 'cmdId',
            id: 'evtId',
            name: 'enteredNewPerson',
            aggregate: {
              id: 'aggId',
              name: 'person'
            },
            context: {
              name: 'hr'
            },
            payload: {
              firstname: 'Jack',
              lastname: 'Joe'
            },
            revision: 1,
            version: 4,
            meta: {
              userId: 'usrId'
            }
          };

          vb.denormalize(evt, function (err, notis) {
            expect(err).not.to.be.ok();
            expect(notis.length).to.eql(1);
            expect(notis[0].payload.firstname).to.eql('Jack');
            expect(notis[0].payload.lastname).to.eql('Joe');

            expect(evt.deep).not.to.be.ok();
            done();
          });

        });

      });

      describe('defining an executeForEach function', function () {

        describe('sync', function () {

          it('it should work as expected', function (done) {

            var counter = 0;

            var vb = api.defineViewBuilder({  }, function (evt, vm) {
              var data = vm.toJSON();
              data.index = counter++;
              vm.set(data);
            }).executeForEach(function (evt) {
              return [{ my: evt.payload.firstname }, { id: '1234', my: evt.payload.firstname + 2 }];
            });

            vb.defineEvent({
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

            vb.defineNotification({
              correlationId: 'correlationId',
              id: 'id',
              action: 'name',
              collection: 'collection',
              payload: 'payload',
              context: 'meta.context.name',
              aggregate: 'meta.aggregate.name',
              aggregateId: 'meta.aggregate.id',
              revision: 'meta.aggregate.revision',
              eventId: 'meta.event.id',
              event: 'meta.event.name',
              meta: 'meta'
            });

            var vm = {
              actionOnCommit: 'update',
              set: function (data) {
                this.attr = data;
              },
              toJSON: function () {
                return this.attr;
              }
            };

            var col = { name: 'dummy',
              getNewId: function (callback) { callback(null, 'newId'); },
              loadViewModel: function (id, callback) {
                vm.id = id;
                callback(null, vm);
              },
              saveViewModel: function (vm, callback) {
                callback(null);
              }
            };
            vb.useCollection(col);

            var evt = {
              correlationId: 'cmdId',
              id: 'evtId',
              name: 'enteredNewPerson',
              aggregate: {
                id: 'aggId',
                name: 'person'
              },
              context: {
                name: 'hr'
              },
              payload: {
                firstname: 'Jack',
                lastname: 'Joe'
              },
              revision: 1,
              version: 4,
              meta: {
                userId: 'usrId'
              }
            };

            vb.denormalize(evt, function (err, notis) {
              expect(err).not.to.be.ok();
              expect(notis.length).to.eql(2);
              expect(notis[0].payload.my).to.eql('Jack');
              expect(notis[1].payload.my).to.eql('Jack2');
              expect(notis[0].payload.id).to.eql('newId');
              expect(notis[1].payload.id).to.eql('1234');
              expect(notis[0].payload.index).to.eql(0);
              expect(notis[1].payload.index).to.eql(1);

              expect(evt.deep).not.to.be.ok();
              done();
            });

          });

        });

        describe('async', function () {

          var counter = 0;

          it('it should work as expected', function (done) {

            var vb = api.defineViewBuilder({  }, function (evt, vm) {
              var data = vm.toJSON();
              data.index = counter++;
              vm.set(data);
            }).executeForEach(function (evt, callback) {
              callback(null, [{ my: evt.payload.firstname }, { id: '1234', my: evt.payload.firstname + 2 }]);
            });

            vb.defineEvent({
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

            vb.defineNotification({
              correlationId: 'correlationId',
              id: 'id',
              action: 'name',
              collection: 'collection',
              payload: 'payload',
              context: 'meta.context.name',
              aggregate: 'meta.aggregate.name',
              aggregateId: 'meta.aggregate.id',
              revision: 'meta.aggregate.revision',
              eventId: 'meta.event.id',
              event: 'meta.event.name',
              meta: 'meta'
            });

            var vm = {
              actionOnCommit: 'update',
              set: function (data) {
                this.attr = data;
              },
              toJSON: function () {
                return this.attr;
              }
            };

            var col = { name: 'dummy',
              getNewId: function (callback) { callback(null, 'newId'); },
              loadViewModel: function (id, callback) {
                vm.id = id;
                callback(null, vm);
              },
              saveViewModel: function (vm, callback) {
                callback(null);
              }
            };
            vb.useCollection(col);

            var evt = {
              correlationId: 'cmdId',
              id: 'evtId',
              name: 'enteredNewPerson',
              aggregate: {
                id: 'aggId',
                name: 'person'
              },
              context: {
                name: 'hr'
              },
              payload: {
                firstname: 'Jack',
                lastname: 'Joe'
              },
              revision: 1,
              version: 4,
              meta: {
                userId: 'usrId'
              }
            };

            vb.denormalize(evt, function (err, notis) {
              expect(err).not.to.be.ok();
              expect(notis.length).to.eql(2);
              expect(notis.length).to.eql(2);
              expect(notis[0].payload.my).to.eql('Jack');
              expect(notis[1].payload.my).to.eql('Jack2');
              expect(notis[0].payload.id).to.eql('newId');
              expect(notis[1].payload.id).to.eql('1234');
              expect(notis[0].payload.index).to.eql(0);
              expect(notis[1].payload.index).to.eql(1);

              expect(evt.deep).not.to.be.ok();
              done();
            });

          });

        });

      });

      describe('calling retry during denormalization', function () {

        describe('defining a function without a callback', function () {

          it('it should work as expected', function (done) {

            var runs = 0;
            var vb = api.defineViewBuilder({}, function (evt, vm) {
              runs++;
              expect(this.retry).to.be.a('function');
              if (runs <= 3) {
                return this.retry(1);
              }

              evt.deep = 'duup';
              vm.set(evt.payload);
            });

            vb.defineEvent({
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

            vb.defineNotification({
              correlationId: 'correlationId',
              id: 'id',
              action: 'name',
              collection: 'collection',
              payload: 'payload',
              context: 'meta.context.name',
              aggregate: 'meta.aggregate.name',
              aggregateId: 'meta.aggregate.id',
              revision: 'meta.aggregate.revision',
              eventId: 'meta.event.id',
              event: 'meta.event.name',
              meta: 'meta'
            });

            var vm = {
              actionOnCommit: 'update',
              set: function (data) {
                this.attr = data;
              },
              toJSON: function () {
                return this.attr;
              }
            };

            var col = { name: 'dummy',
              getNewId: function (callback) { callback(null, 'newId'); },
              loadViewModel: function (id, callback) {
                vm.id = id;
                callback(null, vm);
              },
              saveViewModel: function (vm, callback) {
                expect(vm.attr.firstname).to.eql('Jack');
                expect(vm.attr.lastname).to.eql('Joe');
                callback(null);
              }
            };
            vb.useCollection(col);

            var evt = {
              correlationId: 'cmdId',
              id: 'evtId',
              name: 'enteredNewPerson',
              aggregate: {
                id: 'aggId',
                name: 'person'
              },
              context: {
                name: 'hr'
              },
              payload: {
                firstname: 'Jack',
                lastname: 'Joe'
              },
              revision: 1,
              version: 4,
              meta: {
                userId: 'usrId'
              }
            };

            vb.denormalize(evt, function (err, notis) {
              expect(err).not.to.be.ok();
              expect(notis.length).to.eql(1);
              expect(notis[0].payload.firstname).to.eql('Jack');
              expect(notis[0].payload.lastname).to.eql('Joe');

              expect(evt.deep).not.to.be.ok();

              expect(runs).to.eql(4);
              done();
            });

          });

        });

        describe('defining a function with a callback', function () {

          it('it should work as expected', function (done) {

            var runs = 0;
            var vb = api.defineViewBuilder({}, function (evt, vm, clb) {
              expect(this.retry).to.be.a('function');
              var self = this;
              setTimeout(function () {
                runs++;
                expect(self.retry).to.be.a('function');
                if (runs <= 3) {
                  return self.retry(1, clb);
                }

                evt.deep = 'duup';
                vm.set(evt.payload);
                clb();
              });
            });

            vb.defineEvent({
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

            vb.defineNotification({
              correlationId: 'correlationId',
              id: 'id',
              action: 'name',
              collection: 'collection',
              payload: 'payload',
              context: 'meta.context.name',
              aggregate: 'meta.aggregate.name',
              aggregateId: 'meta.aggregate.id',
              revision: 'meta.aggregate.revision',
              eventId: 'meta.event.id',
              event: 'meta.event.name',
              meta: 'meta'
            });

            var vm = {
              actionOnCommit: 'update',
              set: function (data) {
                this.attr = data;
              },
              toJSON: function () {
                return this.attr;
              }
            };

            var col = { name: 'dummy',
              getNewId: function (callback) { callback(null, 'newId'); },
              loadViewModel: function (id, callback) {
                vm.id = id;
                callback(null, vm);
              },
              saveViewModel: function (vm, callback) {
                expect(vm.attr.firstname).to.eql('Jack');
                expect(vm.attr.lastname).to.eql('Joe');
                callback(null);
              }
            };
            vb.useCollection(col);

            var evt = {
              correlationId: 'cmdId',
              id: 'evtId',
              name: 'enteredNewPerson',
              aggregate: {
                id: 'aggId',
                name: 'person'
              },
              context: {
                name: 'hr'
              },
              payload: {
                firstname: 'Jack',
                lastname: 'Joe'
              },
              revision: 1,
              version: 4,
              meta: {
                userId: 'usrId'
              }
            };

            vb.denormalize(evt, function (err, notis) {
              expect(err).not.to.be.ok();
              expect(notis.length).to.eql(1);
              expect(notis[0].payload.firstname).to.eql('Jack');
              expect(notis[0].payload.lastname).to.eql('Joe');

              expect(evt.deep).not.to.be.ok();

              expect(runs).to.eql(4);
              done();
            });

          });

        });

      });

    });

  });

});
```


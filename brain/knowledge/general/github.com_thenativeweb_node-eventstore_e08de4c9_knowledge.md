---
id: github.com-thenativeweb-node-eventstore-e08de4c9-k
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:27.740048
---

# KNOWLEDGE EXTRACT: github.com_thenativeweb_node-eventstore_e08de4c9
> **Extracted on:** 2026-04-01 16:45:28
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007525285/github.com_thenativeweb_node-eventstore_e08de4c9

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
  browser: true
  node: true
  es6: true

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
docker-compose.yml

.idea
.vscode

# Use wildcards as well
*~
#*.swp

node_modules
node_modules/**/*

package-lock.json

*.tingo
*.rdb
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
  - mongodb
  - redis-server
  - elasticsearch
#   - couchdb

language: node_js
node_js:
  - "4"
  - "6"
  - "8"
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

[![JS.ORG](https://img.shields.io/badge/js.org-eventstore-ffb400.svg?style=flat-square)](http://js.org)
[![travis](https://img.shields.io/travis/adrai/node-eventstore.svg)](https://travis-ci.org/adrai/node-eventstore) [![npm](https://img.shields.io/npm/v/eventstore.svg)](https://npmjs.org/package/eventstore)

The project goal is to provide an eventstore implementation for node.js:

- load and store events via EventStream object
- event dispatching to your publisher (optional)
- supported Dbs (inmemory, mongodb, redis, tingodb, elasticsearch, azuretable, dynamodb)
- snapshot support
- query your events

# Consumers

- [cqrs-domain](https://github.com/adrai/node-cqrs-domain)
- [cqrs](https://github.com/leogiese/cqrs)

# Installation

    npm install eventstore

# Usage

## Require the module and init the eventstore:
```javascript
var eventstore = require('eventstore');

var es = eventstore();
```

By default the eventstore will use an inmemory Storage.

### Logging

For logging and debugging you can use [debug](https://github.com/visionmedia/debug) by [TJ Holowaychuk](https://github.com/visionmedia)

simply run your process with

    DEBUG=eventstore* node app.js

## Provide implementation for storage

example with mongodb:

```javascript
var es = require('eventstore')({
  type: 'mongodb',
  host: 'localhost',                             // optional
  port: 27017,                                   // optional
  dbName: 'eventstore',                          // optional
  eventsCollectionName: 'events',                // optional
  snapshotsCollectionName: 'snapshots',          // optional
  transactionsCollectionName: 'transactions',    // optional
  timeout: 10000,                                // optional
  // emitStoreEvents: true                       // optional, by default no store events are emitted
  // maxSnapshotsCount: 3                        // optional, defaultly will keep all snapshots
  // authSource: 'authedicationDatabase'         // optional
  // username: 'technicalDbUser'                 // optional
  // password: 'secret'                          // optional
  // url: 'mongodb://user:pass@host:port/db?opts // optional
  // positionsCollectionName: 'positions'        // optional, defaultly wont keep position
});
```

example with redis:
```javascript
var es = require('eventstore')({
  type: 'redis',
  host: 'localhost',                          // optional
  port: 6379,                                 // optional
  db: 0,                                      // optional
  prefix: 'eventstore',                       // optional
  eventsCollectionName: 'events',             // optional
  snapshotsCollectionName: 'snapshots',       // optional
  timeout: 10000                              // optional
  // emitStoreEvents: true,                   // optional, by default no store events are emitted
  // maxSnapshotsCount: 3                     // optional, defaultly will keep all snapshots
  // password: 'secret'                       // optional
});
```

example with tingodb:
```javascript
var es = require('eventstore')({
  type: 'tingodb',
  dbPath: '/path/to/my/db/file',              // optional
  eventsCollectionName: 'events',             // optional
  snapshotsCollectionName: 'snapshots',       // optional
  transactionsCollectionName: 'transactions', // optional
  timeout: 10000,                             // optional
  // emitStoreEvents: true,                   // optional, by default no store events are emitted
  // maxSnapshotsCount: 3                     // optional, defaultly will keep all snapshots
});
```

example with elasticsearch:
```javascript
var es = require('eventstore')({
  type: 'elasticsearch',
  host: 'localhost:9200',                     // optional
  indexName: 'eventstore',                    // optional
  eventsTypeName: 'events',                   // optional
  snapshotsTypeName: 'snapshots',             // optional
  log: 'warning',                             // optional
  maxSearchResults: 10000,                    // optional
  // emitStoreEvents: true,                   // optional, by default no store events are emitted
  // maxSnapshotsCount: 3                     // optional, defaultly will keep all snapshots
});
```

example with custom elasticsearch client (e.g. with AWS ElasticSearch client. Note ``` http-aws-es ``` package usage in this example):
```javascript
var elasticsearch = require('elasticsearch');

var esClient = = new elasticsearch.Client({
  hosts: 'SOMETHING.es.amazonaws.com',
  connectionClass: require('http-aws-es'),
  amazonES: {
    region: 'us-east-1',
    accessKey: 'REPLACE_AWS_accessKey',
    secretKey: 'REPLACE_AWS_secretKey'
  }
});

var es = require('eventstore')({
  type: 'elasticsearch',
  client: esClient,
  indexName: 'eventstore',
  eventsTypeName: 'events',
  snapshotsTypeName: 'snapshots',
  log: 'warning',
  maxSearchResults: 10000
});
```

example with azuretable:
```javascript
var es = require('eventstore')({
  type: 'azuretable',
  storageAccount: 'nodeeventstore',
  storageAccessKey: 'aXJaod96t980AbNwG9Vh6T3ewPQnvMWAn289Wft9RTv+heXQBxLsY3Z4w66CI7NN12+1HUnHM8S3sUbcI5zctg==',
  storageTableHost: 'https://nodeeventstore.table.core.windows.net/',
  eventsTableName: 'events',               // optional
  snapshotsTableName: 'snapshots',         // optional
  timeout: 10000,                          // optional
  emitStoreEvents: true                    // optional, by default no store events are emitted
});
```

example with dynamodb:
```javascript
var es = require('eventstore')({
    type: 'dynamodb',
    eventsTableName: 'events',                  // optional
    snapshotsTableName: 'snapshots',            // optional
    undispatchedEventsTableName: 'undispatched' // optional
    EventsReadCapacityUnits: 1,                 // optional
    EventsWriteCapacityUnits: 3,                // optional
    SnapshotReadCapacityUnits: 1,               // optional
    SnapshotWriteCapacityUnits: 3,              // optional
    UndispatchedEventsReadCapacityUnits: 1,     // optional
    UndispatchedEventsReadCapacityUnits: 1,     // optional
    useUndispatchedEventsTable: true            // optional
    eventsTableStreamEnabled: false             // optional
    eventsTableStreamViewType: 'NEW_IMAGE',     // optional
    emitStoreEvents: true                       // optional, by default no store events are emitted
});
```

DynamoDB credentials are obtained by eventstore either from environment vars or credentials file. For setup see [AWS Javascript SDK](http://docs.aws.amazon.com/AWSJavaScriptSDK/guide/node-configuring.html).

DynamoDB provider supports [DynamoDB local](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html) for local development via the AWS SDK `endpoint` option. Just set the `$AWS_DYNAMODB_ENDPOINT` (or `%AWS_DYNAMODB_ENDPOINT%` in Windows) environment variable to point to your running instance of Dynamodb local like this:

    $ export AWS_DYNAMODB_ENDPOINT=http://localhost:8000

Or on Windows:

    > set AWS_DYNAMODB_ENDPOINT=http://localhost:8000

The **useUndispatchedEventsTable** option to available for those who prefer to use DyanmoDB.Streams to pull events from the store instead of the UndispatchedEvents table. The default is true. Setting this option to false will result in the UndispatchedEvents table not being created at all, the getUndispatchedEvents method will always return an empty array, and the setEventToDispatched will effectively do nothing.

Refer to [StreamViewType](http://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_StreamSpecification.html#DDB-Type-StreamSpecification-StreamViewType) for a description of the **eventsTableStreamViewType** option

## Built-in event publisher (optional)

if defined the eventstore will try to publish AND set event do dispatched on its own...

### sync interface
```javascript
es.useEventPublisher(function(evt) {
  // bus.emit('event', evt);
});
```

### async interface

```javascript
es.useEventPublisher(function(evt, callback) {
  // bus.sendAndWaitForAck('event', evt, callback);
});
```

## catch connect and disconnect events

```javascript
es.on('connect', function() {
  console.log('storage connected');
});

es.on('disconnect', function() {
  console.log('connection to storage is gone');
});
```

## define event mappings [optional]

Define which values should be mapped/copied to the payload event.

```javascript
es.defineEventMappings({
  id: 'id',
  commitId: 'commitId',
  commitSequence: 'commitSequence',
  commitStamp: 'commitStamp',
  streamRevision: 'streamRevision'
});
```

## initialize
```javascript
es.init(function (err) {
  // this callback is called when all is ready...
});

// or

es.init(); // callback is optional
```

## working with the eventstore

### get the eventhistory (of an aggregate)

```javascript
es.getEventStream('streamId', function(err, stream) {
  var history = stream.events; // the original event will be in events[i].payload

  // myAggregate.loadFromHistory(history);
});
```

or

```javascript
es.getEventStream({
  aggregateId: 'myAggregateId',
  aggregate: 'person',          // optional
  context: 'hr'                 // optional
}, function(err, stream) {
  var history = stream.events; // the original event will be in events[i].payload

  // myAggregate.loadFromHistory(history);
});
```

'streamId' and 'aggregateId' are the same...
In ddd terms aggregate and context are just to be more precise in language.
For example you can have a 'person' aggregate in the context 'human ressources' and a 'person' aggregate in the context of 'business contracts'...
So you can have 2 complete different aggregate instances of 2 complete different aggregates (but perhaps with same name) in 2 complete different contexts

you can request an eventstream even by limit the query with a 'minimum revision number' and a 'maximum revision number'

```javascript
var revMin = 5,
    revMax = 8; // if you omit revMax or you define it as -1 it will retrieve until the end

es.getEventStream('streamId' || {/* query */}, revMin, revMax, function(err, stream) {
  var history = stream.events; // the original event will be in events[i].payload

  // myAggregate.loadFromHistory(history);
});
```

store a new event and commit it to store

```javascript
es.getEventStream('streamId', function(err, stream) {
  stream.addEvent({ my: 'event' });
  stream.addEvents([{ my: 'event2' }]);

  stream.commit();

  // or

  stream.commit(function(err, stream) {
    console.log(stream.eventsToDispatch); // this is an array containing all added events in this commit.
  });
});
```

if you defined an event publisher function the committed event will be dispatched to the provided publisher

if you just want to load the last event as stream you can call getLastEventAsStream instead of ´getEventStream´.

## working with snapshotting

get snapshot and eventhistory from the snapshot point

```javascript
es.getFromSnapshot('streamId', function(err, snapshot, stream) {
  var snap = snapshot.data;
  var history = stream.events; // events history from given snapshot

  // myAggregate.loadSnapshot(snap);
  // myAggregate.loadFromHistory(history);
});
```

or

```javascript
es.getFromSnapshot({
  aggregateId: 'myAggregateId',
  aggregate: 'person',          // optional
  context: 'hr'                 // optional
}, function(err, snapshot, stream) {
  var snap = snapshot.data;
  var history = stream.events; // events history from given snapshot

  // myAggregate.loadSnapshot(snap);
  // myAggregate.loadFromHistory(history);
});
```

you can request a snapshot and an eventstream even by limit the query with a 'maximum revision number'

```javascript
var revMax = 8; // if you omit revMax or you define it as -1 it will retrieve until the end

es.getFromSnapshot('streamId' || {/* query */}, revMax, function(err, snapshot, stream) {
  var snap = snapshot.data;
  var history = stream.events; // events history from given snapshot

  // myAggregate.loadSnapshot(snap);
  // myAggregate.loadFromHistory(history);
});
```


create a snapshot point

```javascript
es.getFromSnapshot('streamId', function(err, snapshot, stream) {

  var snap = snapshot.data;
  var history = stream.events; // events history from given snapshot

  // myAggregate.loadSnapshot(snap);
  // myAggregate.loadFromHistory(history);

  // create a new snapshot depending on your rules
  if (history.length > myLimit) {
    es.createSnapshot({
      streamId: 'streamId',
      data: myAggregate.getSnap(),
      revision: stream.lastRevision,
      version: 1 // optional
    }, function(err) {
      // snapshot saved
    });

    // or

    es.createSnapshot({
      aggregateId: 'myAggregateId',
      aggregate: 'person',          // optional
      context: 'hr'                 // optional
      data: myAggregate.getSnap(),
      revision: stream.lastRevision,
      version: 1 // optional
    }, function(err) {
      // snapshot saved
    });
  }

  // go on: store new event and commit it
  // stream.addEvents...

});
```

You can automatically clean older snapshots by configuring the number of snapshots to keep with `maxSnapshotsCount` in `eventstore` options.

## own event dispatching (no event publisher function defined)

```javascript
es.getUndispatchedEvents(function(err, evts) {
  // or es.getUndispatchedEvents('streamId', function(err, evts) {
  // or es.getUndispatchedEvents({ // free choice (all, only context, only aggregate, only aggregateId...)
  //                                context: 'hr',
  //                                aggregate: 'person',
  //                                aggregateId: 'uuid'
  //                              }, function(err, evts) {

  // all undispatched events
  console.log(evts);

  // dispatch it and set the event as dispatched

  for (var e in evts) {
    var evt = evts[r];
    es.setEventToDispatched(evt, function(err) {});
    // or
    es.setEventToDispatched(evt.id, function(err) {});
  }

});
```

## query your events

for replaying your events or for rebuilding a viewmodel or just for fun...

skip, limit always optional
```javascript
var skip = 0,
    limit = 100; // if you omit limit or you define it as -1 it will retrieve until the end

es.getEvents(skip, limit, function(err, evts) {
  // if (events.length === amount) {
  //   events.next(function (err, nextEvts) {}); // just call next to retrieve the next page...
  // } else {
  //   // finished...
  // }
});

// or

es.getEvents('streamId', skip, limit, function(err, evts) {
  // if (events.length === amount) {
  //   events.next(function (err, nextEvts) {}); // just call next to retrieve the next page...
  // } else {
  //   // finished...
  // }
});

// or

es.getEvents({ // free choice (all, only context, only aggregate, only aggregateId...)
  context: 'hr',
  aggregate: 'person',
  aggregateId: 'uuid'
}, skip, limit, function(err, evts) {
  // if (events.length === amount) {
  //   events.next(function (err, nextEvts) {}); // just call next to retrieve the next page...
  // } else {
  //   // finished...
  // }
});
```

by revision

revMin, revMax always optional

```javascript
var revMin = 5,
    revMax = 8; // if you omit revMax or you define it as -1 it will retrieve until the end

es.getEventsByRevision('streamId', revMin, revMax, function(err, evts) {});

// or

es.getEventsByRevision({
  aggregateId: 'myAggregateId',
  aggregate: 'person',          // optional
  context: 'hr'                 // optional
}, revMin, revMax, function(err, evts) {});
```
by commitStamp

skip, limit always optional

```javascript
var skip = 0,
    limit = 100; // if you omit limit or you define it as -1 it will retrieve until the end

es.getEventsSince(new Date(2015, 5, 23), skip, limit, function(err, evts) {
  // if (events.length === amount) {
  //   events.next(function (err, nextEvts) {}); // just call next to retrieve the next page...
  // } else {
  //   // finished...
  // }
});

// or

es.getEventsSince(new Date(2015, 5, 23), limit, function(err, evts) {
  // if (events.length === amount) {
  //   events.next(function (err, nextEvts) {}); // just call next to retrieve the next page...
  // } else {
  //   // finished...
  // }
});

// or

es.getEventsSince(new Date(2015, 5, 23), function(err, evts) {
  // if (events.length === amount) {
  //   events.next(function (err, nextEvts) {}); // just call next to retrieve the next page...
  // } else {
  //   // finished...
  // }
});
```

## streaming your events
Some databases support streaming your events, the api is similar to the query one

skip, limit always optional

```javascript
var skip = 0,
    limit = 100; // if you omit limit or you define it as -1 it will retrieve until the end

var stream = es.streamEvents(skip, limit);
// or
var stream = es.streamEvents('streamId', skip, limit);
// or by commitstamp
var stream = es.streamEventsSince(new Date(2015, 5, 23), skip, limit);
// or by revision
var stream = es.streamEventsByRevision({
  aggregateId: 'myAggregateId',
  aggregate: 'person',
  context: 'hr',
});

stream.on('data', function(e) {
  doSomethingWithEvent(e);
});

stream.on('end', function() {
  console.log('no more evets');
});

// or even better
stream.pipe(myWritableStream);
```

currently supported by:

1. mongodb

## get the last event
for example to obtain the last revision nr
```javascript
es.getLastEvent('streamId', function(err, evt) {
});

// or

es.getLastEvent({ // free choice (all, only context, only aggregate, only aggregateId...)
  context: 'hr',
  aggregate: 'person',
  aggregateId: 'uuid'
} function(err, evt) {
});
```

## obtain a new id

```javascript
es.getNewId(function(err, newId) {
  if(err) {
    console.log('ohhh :-(');
    return;
  }

  console.log('the new id is: ' + newId);
});
```

## position of event in store

some db implementations support writing the position of the event in the whole store additional to the streamRevision.

currently those implementations support this:

1. inmemory ( by setting ```trackPosition`` option )
1. mongodb ( by setting ```positionsCollectionName``` option)

## special scaling handling with mongodb

Inserting multiple events (documents) in mongodb, is not atomic.
For the eventstore tries to repair itself when calling `getEventsByRevision`.
But if you want you can trigger this from outside:

```javascript
es.store.getPendingTransactions(function(err, txs) {
  if(err) {
    console.log('ohhh :-(');
    return;
  }

  // txs is an array of objects like:
  // {
  //   _id: '/* the commitId of the committed event stream */',
  //   events: [ /* all events of the committed event stream */ ],
  //   aggregateId: 'aggregateId',
  //   aggregate: 'aggregate', // optional
  //   context: 'context'      // optional
  // }

  es.store.getLastEvent({
    aggregateId: txs[0].aggregateId,
    aggregate: txs[0].aggregate, // optional
    context: txs[0].context      // optional
  }, function (err, lastEvent) {
    if(err) {
      console.log('ohhh :-(');
      return;
    }

    es.store.repairFailedTransaction(lastEvent, function (err) {
      if(err) {
        console.log('ohhh :-(');
        return;
      }

      console.log('everything is fine');
    });
  });
});
```
## Catch before and after eventstore events
Optionally the eventstore can emit brefore and after events, to enable this feature set the `emitStoreEvents` to true.

```javascript
var eventstore = require('eventstore');
var es = eventstore({
  emitStoreEvents: true,
});

es.on('before-clear', function({milliseconds}) {});
es.on('after-clear', function({milliseconds}) {});

es.on('before-get-next-positions', function({milliseconds, arguments: [positions]}) {});
es.on('after-get-next-positions', function({milliseconds, arguments: [positions]}) {});

es.on('before-add-events', function({milliseconds, arguments: [events]}) {});
es.on('after-add-events', function(milliseconds, arguments: [events]) {});

es.on('before-get-events', function({milliseconds, arguments: [query, skip, limit]}) {});
es.on('after-get-events', function({milliseconds, arguments: [query, skip, limit]}) {});

es.on('before-get-events-since', function({milliseconds, arguments: [milliseconds, date, skip, limit]}) {});
es.on('after-get-events-since', function({milliseconds, arguments: [date, skip, limit]}) {});

es.on('before-get-events-by-revision', function({milliseconds, arguments: [query, revMin, revMax]}) {});
es.on('after-get-events-by-revision', function({milliseconds, arguments, [query, revMin, revMax]}) {});

es.on('before-get-last-event', function({milliseconds, arguments: [query]}) {});
es.on('after-get-last-event', function({milliseconds, arguments: [query]}) {});

es.on('before-get-undispatched-events', function({milliseconds, arguments: [query]}) {});
es.on('after-get-undispatched-events', function({milliseconds, arguments: [query]}) {});

es.on('before-set-event-to-dispatched', function({milliseconds, arguments: [id]}) {});
es.on('after-set-event-to-dispatched', function({milliseconds, arguments: [id]}) {});

es.on('before-add-snapshot', function({milliseconds, arguments: [snap]}) {});
es.on('after-add-snapshot', function({milliseconds, arguments: [snap]}) {});

es.on('before-clean-snapshots', function({milliseconds, arguments: [query]}) {});
es.on('after-clean-snapshots', function({milliseconds, arguments: [query]}) {});

es.on('before-get-snapshot', function({milliseconds, arguments: [query, revMax]}) {});
es.on('after-get-snapshot', function({milliseconds, arguments: [query, revMax]}) {});

es.on('before-remove-transactions', function({milliseconds}, arguments: [event]) {});
es.on('after-remove-transactions', function({milliseconds}, arguments: [event]) {});

es.on('before-get-pending-transactions', function({milliseconds}) {});
es.on('after-get-pending-transactions', function({milliseconds}) {});

es.on('before-repair-failed-transactions', function({milliseconds, arguments: [lastEvt]}) {});
es.on('after-repair-failed-transactions', function({milliseconds, arguments: [lastEvt]}) {});

es.on('before-remove-tables', function({milliseconds}) {});
es.on('after-remove-tables', function({milliseconds}) {});

es.on('before-stream-events', function({milliseconds, arguments: [query, skip, limit]}) {});
es.on('after-stream-events', function({milliseconds, arguments: [query, skip, limit]}) {});

es.on('before-stream-events-since', function({milliseconds, arguments: [date, skip, limit]}) {});
es.on('after-stream-events-since', function({milliseconds, arguments: [date, skip, limit]}) {});

es.on('before-get-event-stream', function({milliseconds, arguments: [query, revMin, revMax]}) {});
es.on('after-get-event-stream', function({milliseconds, arguments: [query, revMin, revMax]}) {});

es.on('before-get-from-snapshot', function({milliseconds, arguments: [query, revMax]}) {});
es.on('after-get-from-snapshot', function({milliseconds, arguments: [query, revMax]}) {});

es.on('before-create-snapshot', function({milliseconds, arguments: [obj]}) {});
es.on('after-create-snapshot', function({milliseconds, arguments: [obj]}) {});

es.on('before-commit', function({milliseconds, arguments: [eventstream]}) {});
es.on('after-commit', function({milliseconds, arguments: [eventstream]}) {});

es.on('before-get-last-event-as-stream', function({milliseconds, arguments: [query]}) {});
es.on('after-get-last-event-as-stream', function({milliseconds, arguments: [query]}) {});
```

# Sample Integration

- [nodeCQRS](https://github.com/jamuhl/nodeCQRS) A CQRS sample integrating eventstore

# Inspiration

- Jonathan Oliver's [EventStore](https://github.com/joliver/EventStore) for .net.

# [Release notes](https://github.com/adrai/node-eventstore/blob/master/releasenotes.md)

# Database Support

Currently these databases are supported:

1. inmemory
2. mongodb ([node-mongodb-native](https://github.com/mongodb/node-mongodb-native))
3. redis ([redis](https://github.com/mranney/node_redis))
4. tingodb ([tingodb](https://github.com/sergeyksv/tingodb))
5. azuretable ([azure-storage](https://github.com/Azure/azure-storage-node))
6. dynamodb ([aws-sdk](https://github.com/aws/aws-sdk-js))

## own db implementation

You can use your own db implementation by extending this...

```javascript
var Store = require('eventstore').Store,
    util = require('util'),
    _ = require('lodash');

function MyDB(options) {
  options = options || {};
  Store.call(this, options);
}

util.inherits(MyDB, Store);

_.extend(MyDB.prototype, {

  // ...

});

module.exports = MyDB;
```

and you can use it in this way

```javascript
var es = require('eventstore')({
  type: MyDB
});
// es.init...
```

# License

Copyright (c) 2018 Adriano Raiano, Jan Muehlemann

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
var Eventstore = require('./lib/eventstore'),
  Base = require('./lib/base'),
  _ = require('lodash'),
  debug = require('debug')('eventstore'),
  StoreEventEmitter = require('./lib/storeEventEmitter');

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

function getSpecificStore(options) {
  options = options || {};

  options.type = options.type || 'inmemory';

  if (_.isFunction(options.type)) {
    return options.type;
  }

  options.type = options.type.toLowerCase();

  var dbPath = __dirname + "/lib/databases/" + options.type + ".js";

  if (!exists(dbPath)) {
    var errMsg = 'Implementation for db "' + options.type + '" does not exist!';
    console.log(errMsg);
    debug(errMsg);
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
      var msg = 'Please install module "' + moduleName +
        '" to work with db implementation "' + options.type + '"!';
      console.log(msg);
      debug(msg);
    }

    throw err;
  }
}

module.exports = function(options) {
  options = options || {};

  var Store;

  try {
    Store = getSpecificStore(options);
  } catch (err) {
    throw err;
  }

  var eventstore = new Eventstore(options, new Store(options));

  if (options.emitStoreEvents) {
    var storeEventEmitter = new StoreEventEmitter(eventstore);
    storeEventEmitter.addEventEmitter();
  }

  return eventstore;
};

module.exports.Store = Base;
```

## File: `license`
```
Copyright (c) 2018 Adriano Raiano, Jan Muehlemann

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
  "name": "eventstore",
  "version": "1.15.5",
  "contributors": [
    {
      "name": "Adriano Raiano",
      "email": "adriano@raiano.ch"
    },
    {
      "name": "Jan Muehlemann",
      "email": "jan.muehlemann@gmail.com"
    }
  ],
  "private": false,
  "repository": {
    "type": "git",
    "url": "git@github.com:adrai/node-eventstore.git"
  },
  "description": "Node-eventstore is a node.js module for multiple databases. It can be very useful as eventstore if you work with (d)ddd, cqrs, eventsourcing, commands and events, etc.",
  "keywords": [
    "cqrs",
    "eventstore",
    "ddd",
    "(d)ddd",
    "eventsourcing",
    "mongodb",
    "redis",
    "tingodb",
    "azure",
    "azuretable",
    "inmemory",
    "elasticsearch"
  ],
  "main": "./index.js",
  "directories": {
    "lib": "./lib"
  },
  "engines": {
    "node": ">=0.8.0"
  },
  "dependencies": {
    "async": "2.6.2",
    "debug": "3.1.0",
    "dotty": "0.0.2",
    "jsondate": "0.0.1",
    "lodash": "4.17.19",
    "parent-require": "1.0.0",
    "tolerance": "1.0.0",
    "uuid": "3.3.3"
  },
  "devDependencies": {
    "aws-sdk": ">=2.4.9",
    "azure-storage": ">=0.10.0",
    "cradle": ">=0.7.1",
    "elasticsearch": ">=10.0.0",
    "eslint": ">=1.0.0",
    "expect.js": ">=0.1.2",
    "mocha": "3.x.x",
    "mongodb": "2.1.x",
    "redis": ">=0.10.1",
    "tingodb": ">=0.0.1"
  },
  "scripts": {
    "test": "mocha"
  }
}
```

## File: `releasenotes.md`
```markdown
#### [v1.15.5](https://github.com/adrai/node-eventstore/compare/v1.15.4...v1.15.5)
- Fixing omitting & duplication issue on mongoDB streamEventsByRevision [#169](https://github.com/adrai/node-eventstore/pull/169) thanks to [ScripterSugar](https://github.com/ScripterSugar)

#### [v1.15.4](https://github.com/adrai/node-eventstore/compare/v1.15.3...v1.15.4)
- make sure revision is of correct type [#167](https://github.com/adrai/node-eventstore/pull/167) thanks to [ScripterSugar](https://github.com/ScripterSugar)

#### [v1.15.3](https://github.com/adrai/node-eventstore/compare/v1.15.2...v1.15.3)
- mongodb: useUnifiedTopology [#162](https://github.com/adrai/node-eventstore/pull/162) thanks to [odin16](https://github.com/odin16)

#### [v1.15.2](https://github.com/adrai/node-eventstore/compare/v1.15.1...v1.15.2)
- tingodb: use default implementation for getNewId

#### [v1.15.1](https://github.com/adrai/node-eventstore/compare/v1.15.0...v1.15.1)
- Bugfix/emit eventstore event without callback [#151](https://github.com/adrai/node-eventstore/pull/151) thanks to [DaNautilus](https://github.com/DaNautilus)

#### [v1.15.0](https://github.com/adrai/node-eventstore/compare/v1.14.42...v1.15.0)
- Feature: optionally emit eventstore before and after events [#149](https://github.com/adrai/node-eventstore/pull/149) thanks to [DaNautilus](https://github.com/DaNautilus)

#### [v1.14.42](https://github.com/adrai/node-eventstore/compare/v1.14.41...v1.14.42)
- mongodb: speedup getLastEvent by adding a new index [#147](https://github.com/adrai/node-eventstore/pull/147) thanks to [robinfehr](https://github.com/robinfehr)

#### [v1.14.41](https://github.com/adrai/node-eventstore/compare/v1.14.40...v1.14.41)
- update deps

#### [v1.14.4](https://github.com/adrai/node-eventstore/compare/v1.40.4...v1.14.3)
- replace deprecated mongodb methods with suggested replacements

#### [v1.14.3](https://github.com/adrai/node-eventstore/compare/v1.40.3...v1.14.2)
- revisit the position option, to make it mappable to payload and part of the commit flow

#### [v1.14.2](https://github.com/adrai/node-eventstore/compare/v1.40.1...v1.14.2)
- add non-breaking, optional position in store option for mongodb and inmemory implementations

#### [v1.14.1](https://github.com/adrai/node-eventstore/compare/v1.40.0...v1.14.1)
- add streamEventsByRevision method to the streaming api thanks to [nanov](https://github.com/nanov)

#### [v1.14.0](https://github.com/adrai/node-eventstore/compare/v1.13.4...v1.14.0)
- Introduce stream API for getEvents and getEventsSince and add mongodb implementation thanks to [nanov](https://github.com/nanov)

#### [v1.13.4](https://github.com/adrai/node-eventstore/compare/v1.13.3...v1.13.4)
- Fix store.cleanSnapshots for redis implementation [#127](https://github.com/adrai/node-eventstore/pull/127) thanks to [TyGuy](https://github.com/TyGuy)

#### [v1.13.3](https://github.com/adrai/node-eventstore/compare/v1.13.2...v1.13.3)
- remove deprecated option max_attempts from redis options

#### [v1.13.2](https://github.com/adrai/node-eventstore/compare/v1.13.0...v1.13.2)
- Fix concurrency issue in createTableIfNotExists (DynamoDB) [#118](https://github.com/adrai/node-eventstore/pull/118) thanks to [DannyRyman](https://github.com/DannyRyman)

#### [v1.13.0](https://github.com/adrai/node-eventstore/compare/v1.12.9...v1.13.0)
- compatibility with new mongodb version (3.x)

#### [v1.12.9](https://github.com/adrai/node-eventstore/compare/v1.12.8...v1.12.9)
- fixing [#116](https://github.com/adrai/node-eventstore/pull/116) correctly thanks to [wrobel](https://github.com/wrobel)

#### [v1.12.8](https://github.com/adrai/node-eventstore/compare/v1.12.7...v1.12.8)
- Fix sort key/range key ordering in dynamodb events table [#115](https://github.com/adrai/node-eventstore/pull/115) thanks to [chriscosgriff](https://github.com/chriscosgriff)

#### [v1.12.7](https://github.com/adrai/node-eventstore/compare/v1.12.6...v1.12.7)
- Optionally enable dynamodb stream on the events table [#113](https://github.com/adrai/node-eventstore/pull/113) thanks to [chriscosgriff](https://github.com/chriscosgriff)

#### [v1.12.6](https://github.com/adrai/node-eventstore/compare/v1.12.5...v1.12.6)
- try to fix memory leak when calling next page [#112](https://github.com/adrai/node-eventstore/issues/112) thanks to [repkins](https://github.com/repkins)

#### [v1.12.5](https://github.com/adrai/node-eventstore/compare/v1.12.4...v1.12.5)
- fix DynamoDB concurrency [#110](https://github.com/adrai/node-eventstore/pull/110) thanks to [DannyRyman](https://github.com/DannyRyman)

#### [v1.12.4](https://github.com/adrai/node-eventstore/compare/v1.12.3...v1.12.4)
- fixing dynamodb DocumentClient initialization [#109](https://github.com/adrai/node-eventstore/pull/109) thanks to [Glockenbeat](https://github.com/Glockenbeat)

#### [v1.12.3](https://github.com/adrai/node-eventstore/compare/v1.12.2...v1.12.3)
- dynamodb: Fixed TypeError [#107](https://github.com/adrai/node-eventstore/pull/107) thanks to [jrutley](https://github.com/jrutley)

#### [v1.12.2](https://github.com/adrai/node-eventstore/compare/v1.12.0...v1.12.2)
- fix for new mongodb driver

#### [v1.12.0](https://github.com/adrai/node-eventstore/compare/v1.11.1...v1.12.0)
- Clean snapshots automatically whenever activated [#101](https://github.com/adrai/node-eventstore/pull/101) thanks to [rehia](https://github.com/rehia)

#### [v1.11.1](https://github.com/adrai/node-eventstore/compare/v1.11.0...v1.11.1)
- loop fix for node 0.12.x [#99](https://github.com/adrai/node-eventstore/pull/99) thanks to [pingchen](https://github.com/pingchen)

#### [v1.11.0](https://github.com/adrai/node-eventstore/compare/v1.10.3...v1.11.0)
- Fix empty array conversion due to Lua json decode [#97](https://github.com/adrai/node-eventstore/pull/97) thanks to [rehia](https://github.com/rehia)

#### [v1.10.3](https://github.com/adrai/node-eventstore/compare/v1.10.2...v1.10.3)
- update deps

#### [v1.10.2](https://github.com/adrai/node-eventstore/compare/v1.10.1...v1.10.2)
- dynamodb: changed addEvents to use sequential async methods instead of parallel [#93](https://github.com/adrai/node-eventstore/pull/93) thanks to [developmentalmadness](https://github.com/developmentalmadness)

#### [v1.10.1](https://github.com/adrai/node-eventstore/compare/v1.10.0...v1.10.1)
- fix calculated streamRevision for redis to avoid events sorting issues [#92](https://github.com/adrai/node-eventstore/pull/92) thanks to [rehia](https://github.com/rehia)

#### [v1.10.0](https://github.com/adrai/node-eventstore/compare/v1.9.0...v1.10.0)
- improve event revision accuracy in redis, to avoid revisions duplications for an aggregate [#91](https://github.com/adrai/node-eventstore/pull/91) thanks to [rehia](https://github.com/rehia)

#### [v1.9.0](https://github.com/adrai/node-eventstore/compare/v1.8.4...v1.9.0)
- ability to use custom elasticsearch client in the elasticsearch storage  [#88](https://github.com/adrai/node-eventstore/pull/88) thanks to [evereq](https://github.com/evereq)
- redis snapshots are retrieved recursively to match 'max revision' option  [#89](https://github.com/adrai/node-eventstore/pull/89) thanks to [rehia](https://github.com/rehia)

#### [v1.8.4](https://github.com/adrai/node-eventstore/compare/v1.8.3...v1.8.4)
- Ensuring concurrency for dynamodb  [#87](https://github.com/adrai/node-eventstore/pull/87) thanks to [developmentalmadness](https://github.com/developmentalmadness)

#### [v1.8.3](https://github.com/adrai/node-eventstore/compare/v1.8.2...v1.8.3)
- Optional dispatch table for dynamodb  [#86](https://github.com/adrai/node-eventstore/pull/86) thanks to [developmentalmadness](https://github.com/developmentalmadness)

#### [v1.8.2](https://github.com/adrai/node-eventstore/compare/v1.8.1...v1.8.2)
- Prevent uncommittedEvents to be overwritten accidentally [#84](https://github.com/adrai/node-eventstore/issues/84), [#85](https://github.com/adrai/node-eventstore/pull/85) thanks to [albe](https://github.com/albe)

#### [v1.8.1](https://github.com/adrai/node-eventstore/compare/v1.8.0...v1.8.1)
- Early abort when events were fetched without limit and calling next [#81](https://github.com/adrai/node-eventstore/pull/81) thanks to [johanneslumpe](https://github.com/johanneslumpe)

#### [v1.8.0](https://github.com/adrai/node-eventstore/compare/v1.7.11...v1.8.0)
- dynamodb store implementation [#75](https://github.com/adrai/node-eventstore/pull/75) and [#78](https://github.com/adrai/node-eventstore/pull/78) thanks to [developmentalmadness](https://github.com/developmentalmadness)

#### [v1.7.11](https://github.com/adrai/node-eventstore/compare/v1.7.8...v1.7.11)
- This resolves an issue where the maximum call stack size could be hit when processing 1000s of undispatched events on startup [#74](https://github.com/adrai/node-eventstore/pull/74) thanks to [ben-moore](https://github.com/ben-moore)

#### [v1.7.8](https://github.com/adrai/node-eventstore/compare/v1.7.7...v1.7.8)
- redis, mongodb: call disconnect on ping error

#### [v1.7.7](https://github.com/adrai/node-eventstore/compare/v1.7.6...v1.7.7)
- Support mongo connection string [#70](https://github.com/adrai/node-eventstore/pull/70) [#68](https://github.com/adrai/node-eventstore/issues/68) thanks to [danwkennedy](https://github.com/danwkennedy) and [mmmdreg](https://github.com/mmmdreg)

#### [v1.7.6](https://github.com/adrai/node-eventstore/compare/v1.7.5...v1.7.6)
- redis, mongodb: call disconnect on ping error

#### [v1.7.5](https://github.com/adrai/node-eventstore/compare/v1.7.4...v1.7.5)
- inmemory: keep events immutable [#67](https://github.com/adrai/node-eventstore/pull/67) thanks to [hilkeheremans](https://github.com/hilkeheremans)

#### [v1.7.4](https://github.com/adrai/node-eventstore/compare/v1.7.3...v1.7.4)
- MongoDb: Add index used when querying for all events for an aggregate type [#64](https://github.com/adrai/node-eventstore/pull/65) thanks to [HCanber](https://github.com/HCanber)

#### [v1.7.3](https://github.com/adrai/node-eventstore/compare/v1.7.2...v1.7.3)
- redis: added optional heartbeat

#### [v1.7.2](https://github.com/adrai/node-eventstore/compare/v1.7.1...v1.7.2)
- update azure dependencies
- Adding getLastEvent support in azure table provider [#64](https://github.com/adrai/node-eventstore/pull/64) thanks to [sbiaudet](https://github.com/sbiaudet)

#### [v1.7.1](https://github.com/adrai/node-eventstore/compare/v1.7.0...v1.7.1)
- Fix eventmappings when value is empty or 0 [#61](https://github.com/adrai/node-eventstore/pull/61) thanks to [rehia](https://github.com/rehia)

#### [v1.7.0](https://github.com/adrai/node-eventstore/compare/v1.6.2...v1.7.0)
- added Elasticsearch support [#59](https://github.com/adrai/node-eventstore/pull/59) thanks to [gerbenmeyer](https://github.com/gerbenmeyer)

#### [v1.6.2](https://github.com/adrai/node-eventstore/compare/v1.5.3...v1.6.2)
- added getLastEvent and getLastEventAsStream function

#### [v1.5.3](https://github.com/adrai/node-eventstore/compare/v1.5.2...v1.5.3)
- redis: fix for new redis lib

#### [v1.5.1](https://github.com/adrai/node-eventstore/compare/v1.5.0...v1.5.1)
- give possibility to use mongodb with authSource

#### [v1.5.0](https://github.com/adrai/node-eventstore/compare/v1.4.2...v1.5.0)
- added possibility to getUndispatchedEvents by query

#### [v1.4.2](https://github.com/adrai/node-eventstore/compare/v1.4.1...v1.4.2)
- optimization for `npm link`'ed development

#### [v1.4.1](https://github.com/adrai/node-eventstore/compare/v1.4.0...v1.4.1)
- redis: replace .keys() calls with .scan() calls => scales better

#### [v1.4.0](https://github.com/adrai/node-eventstore/compare/v1.3.1...v1.4.0)
- added possibility to map/copy some values of the raw-event to the real event
- added possibility to fetch all events since a date
- IMPORTANT for redis: the keys have a new format

#### [v1.3.1](https://github.com/adrai/node-eventstore/compare/v1.2.0...v1.3.1)
- mongodb: added possibility to repair failed transaction (insert of multiple events) from outside

#### [v1.2.0](https://github.com/adrai/node-eventstore/compare/v1.1.7...v1.2.0)
- performance improvements in inmemory and mongodb store [#31](https://github.com/adrai/node-eventstore/pull/31) thanks to [surlemur](https://github.com/surlemur)
- IMPORTANT for mongodb: removed data compatibility for events older v1.0.0

#### [v1.1.7](https://github.com/adrai/node-eventstore/compare/v1.1.6...v1.1.7)
- performance improvements in inmemory store

#### [v1.1.6](https://github.com/adrai/node-eventstore/compare/v1.1.5...v1.1.6)
- fix inmemory store

#### [v1.1.5](https://github.com/adrai/node-eventstore/compare/v1.1.4...v1.1.5)
- fix usage with own db implementation [#29](https://github.com/adrai/node-eventstore/pull/29)

#### [v1.1.4](https://github.com/adrai/node-eventstore/compare/v1.1.2...v1.1.4)
- fix usage with own db implementation [#27](https://github.com/adrai/node-eventstore/issues/27)

#### [v1.1.2](https://github.com/adrai/node-eventstore/compare/v1.1.1...v1.1.2)
- azure-table: fix issue in getEvents [#23](https://github.com/adrai/node-eventstore/pull/23) thanks to [rvin100](https://github.com/rvin100)

#### [v1.1.1](https://github.com/adrai/node-eventstore/compare/v1.1.0...v1.1.1)
- azure-table storage optimization [#22](https://github.com/adrai/node-eventstore/pull/22) thanks to [sbiaudet](https://github.com/sbiaudet) and [rvin100](https://github.com/rvin100)

#### [v1.1.0](https://github.com/adrai/node-eventstore/compare/v1.0.5...v1.1.0)
- added azure-table support [#21](https://github.com/adrai/node-eventstore/pull/21) thanks to [sbiaudet](https://github.com/sbiaudet)

#### v1.0.5
- mongodb get all events fix [#20](https://github.com/adrai/node-eventstore/pull/20) thanks to [nikolaylukyanchuk](https://github.com/nikolaylukyanchuk)

#### v1.0.4
- mongodb get all events fix [#20](https://github.com/adrai/node-eventstore/pull/20) thanks to [nikolaylukyanchuk](https://github.com/nikolaylukyanchuk)

#### v1.0.3
- little fix for redis

#### v1.0.2
- optimized indexes

#### v1.0.1
- optimized getSnapshot when using versioning of same revision

#### v1.0.0
- refactored whole module
- added possibility to define aggregateId, aggregate and context
- added a lot of tests
- stabilized everything
- optimized performance
- mongodb legacy data should be usable to (so you can update from eventstore.mongodb to eventstore) without migrating data
- IMPORTANT: changed API!!!

#### v0.7.0
- make using of eventDispatcher configurable
- map getUndispatchedEvents and setEventToDispatched to eventstore

#### v0.6.2
- optimized storage initialization

#### v0.6.1
- forking of event dispatching is configurable now

#### v0.6.0
- removed couchDb implementation
- rewritten tests in mocha and expect.js
- updated to node.js 0.6.15

#### v0.5.0
- simplified API for storage usage
- if possible fork dispatching to own childprocess
- optimized lastRevision handling

#### v0.3.0
- eventstreams
- snapshoting
- get all events with paging for replay
- console.logger
- db implementations for mongoDb, couchDb, redis
```

## File: `lib/base.js`
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

function silentWarning(callback) {
  console.warn('Snapshot cleaning is not implemented for this kind of store');
  callback();
}

_.extend(Store.prototype, {

  /**
   * Initiate communication with the queue.
   * @param  {Function} callback The function, that will be called when the this action is completed. [optional]
   *                             `function(err, queue){}`
   */
  connect: implementError,

  /**
   * Terminate communication with the queue.
   * @param  {Function} callback The function, that will be called when the this action is completed. [optional]
   *                             `function(err){}`
   */
  disconnect: implementError,

  /**
   * Use this function to obtain a new id.
   * @param  {Function} callback The function, that will be called when the this action is completed.
   *                             `function(err, id){}` id is of type String.
   */
  getNewId: function (callback) {
    var id = uuid().toString();
    if (callback) callback(null, id);
  },

  /**
   * Use this function to an array containing the next position numbers
   * @param  {number} positins Number of positions to provide.
   * @param  {Function} callback The function, that will be called when the this action is completed.
   *                             `function(err, positions){}` positions is either undefined if option is not enabled/supported or array with positions
   */
  getNextPositions: function(positions, callback) {
    callback(null);
  },

  /**
   * loads the events
   * @param {Object}   query    the query object
   * @param {Number}   skip     how many events should be skipped?
   * @param {Number}   limit    how many events do you want in the result?
   * @param {Function} callback the function that will be called when this action has finished
   *                            `function(err, events){}`
   */
  getEvents: function (query, skip, limit, callback) {
    implementError(callback);
  },

  /**
   * loads all the events since passed commitStamp
   * @param {Date}     commitStamp the date object
   * @param {Number}   skip        how many events should be skipped? [optional]
   * @param {Number}   limit       how many events do you want in the result? [optional]
   * @param {Function} callback    the function that will be called when this action has finished
   *                               `function(err, events){}`
   */
  getEventsSince: function (commitStamp, skip, limit, callback) {
    implementError(callback);
  },

  /**
   * loads the events
   * @param {Object}   query    the query object
   * @param {Number}   revMin   revision start point
   * @param {Number}   revMax   revision end point (hint: -1 = to end)
   * @param {Function} callback the function that will be called when this action has finished
   *                            `function(err, events){}`
   */
  getEventsByRevision: function (query, revMin, revMax, callback) {
    implementError(callback);
  },

  /**
   * loads the next snapshot back from given max revision
   * @param {Object}   query    the query object
   * @param {Number}   revMax   revision end point (hint: -1 = to end)
   * @param {Function} callback the function that will be called when this action has finished
   *                            `function(err, snapshot){}`
   */
  getSnapshot: function (query, revMax, callback) {
    implementError(callback);
  },

  /**
   * stores a new snapshot
   * @param {Object}   snap     the snapshot data
   * @param {Function} callback the function that will be called when this action has finished [optional]
   */
  addSnapshot: function(snap, callback) {
    implementError(callback);
  },

  /**
   * stores a new snapshot
   * @param {Object}   query    the query object
   * @param {Function} callback the function that will be called when this action has finished [optional]
   */
  cleanSnapshots: function(query, callback) {
    silentWarning(callback);
  },

  /**
   * stores the passed events
   * @param {Array}    evts     the events
   * @param {Function} callback the function that will be called when this action has finished [optional]
   */
  addEvents: function (evts, callback) {
    implementError(callback);
  },

  /**
   * loads the last event
   * @param {Object}   query    the query object [optional]
   * @param {Function} callback the function that will be called when this action has finished
   *                            `function(err, event){}`
   */
  getLastEvent: function (query, callback) {
    implementError(callback);
  },

  /**
   * loads all undispatched events
   * @param {Object}   query    the query object [optional]
   * @param {Function} callback the function that will be called when this action has finished
   *                            `function(err, events){}`
   */
  getUndispatchedEvents: function (query, callback) {
    implementError(callback);
  },

  /**
   * Sets the given event to dispatched.
   * @param {String}   id       the event id
   * @param {Function} callback the function that will be called when this action has finished [optional]
   */
  setEventToDispatched: function (id, callback) {
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

## File: `lib/event.js`
```javascript
var debug = require('debug')('eventstore:event'),
  dotty = require('dotty'),
  _ = require('lodash');

/**
 * Event constructor
 * @param {EventStream} eventstream the corresponding event stream object
 * @param {Object}      event       the event object
 * @constructor
 */
function Event (eventstream, event, eventMappings) {
  if (!eventstream) {
    var errStreamMsg = 'eventstream not injected!';
    debug(errStreamMsg);
    throw new Error(errStreamMsg);
  }

  if (!event) {
    var errEvtMsg = 'event not injected!';
    debug(errEvtMsg);
    throw new Error(errEvtMsg);
  }

  if (!eventstream.aggregateId) {
    var errAggIdMsg = 'eventstream.aggregateId not injected!';
    debug(errAggIdMsg);
    throw new Error(errAggIdMsg);
  }

  if (!_.isArray(eventstream.uncommittedEvents)) {
    var errAggIdMsg = 'eventstream.uncommittedEvents not injected!';
    debug(errAggIdMsg);
    throw new Error(errAggIdMsg);
  }

  eventMappings = eventMappings || {};

  this.streamId = eventstream.aggregateId;
  this.aggregateId = eventstream.aggregateId;
  this.aggregate = eventstream.aggregate;
  this.context = eventstream.context;
  this.streamRevision = null;
  this.commitId = null;
  this.commitSequence = null;
  this.commitStamp = null;
  this.payload = event || null;
  this.position = null;

  this.applyMappings = function applyMappings() {
    _.keys(eventMappings).forEach(function (key) {
      if (this[key] !== undefined && this[key] !== null) {
        dotty.put(this.payload, eventMappings[key], this[key]);
      }
    }.bind(this));
  };

  eventstream.uncommittedEvents.push(this);
}

module.exports = Event;
```

## File: `lib/eventDispatcher.js`
```javascript
var debug = require('debug')('eventstore:eventdispatcher');

/**
 * Eventstore constructor
 * @param {Object} options The options.
 * @param publisher the publisher that should be injected
 * @param store the store that should be injected
 * @constructor
 */
function EventDispatcher(publisher, store) {
  this.publisher = publisher;
  this.store = store;
  this.undispatchedEventsQueue = [];
}

/**
 * Triggers to publish all events in undispatchedEventsQueue.
 */
function trigger (dispatcher) {
  var queue = dispatcher.undispatchedEventsQueue || []
  var event;

  // if the last loop is still in progress leave this loop
  if (dispatcher.isRunning) return;

  dispatcher.isRunning = true;

  (function next (e) {

    // dipatch one event in queue and call the _next_ callback, which
    // will call _process_ for the next undispatched event in queue.
    function process (event, nxt) {

      // Publish it now...
      debug('publish event...');
      dispatcher.publisher(event.payload, function(err) {
        if (err) {
          return debug(err);
        }
        // ...and set the published event to dispatched.
        debug('set event to dispatched...');
        dispatcher.store.setEventToDispatched(event, function(err) {
          if (err) {
            debug(err);
          } else {
            debug('event set to dispatched');
          }
        });
      });

      nxt();
    }

    // serial process all events in queue
    if (!e && queue.length) {
      process(queue.shift(), next)
    } else {
      debug(e);
    }
  })();

  dispatcher.isRunning = false;
}

EventDispatcher.prototype = {

  /**
   * Queues the passed in events for dispatching.
   * @param events
   */
  addUndispatchedEvents: function(events) {
    var self = this;
    events.forEach(function(event) {
      self.undispatchedEventsQueue.push(event);
    });
    trigger(this);
  },

  /**
   * Starts the instance to publish all undispatched events.
   * @param callback the function that will be called when this action has finished
   */
  start: function(callback) {

    if (typeof this.publisher !== 'function') {
      var pubErrMsg = 'publisher not injected!';
      debug(pubErrMsg);
      if (callback) callback(new Error(pubErrMsg));
      return;
    }

    if (!this.store || typeof this.store.getUndispatchedEvents !== 'function'
                    || typeof this.store.setEventToDispatched !== 'function') {
      var storeErrMsg = 'store not injected!';
      debug(storeErrMsg);
      if (callback) callback(new Error(storeErrMsg))
      return;
    }

    var self = this;

    // Get all undispatched events from store and queue them
    // before all other events passed in by the addUndispatchedEvents function.
    this.store.getUndispatchedEvents(function(err, events) {

      if (err) {
        debug(err);
        if (callback) callback(err);
        return;
      }

      var triggered = false;
      if (events) {
        for (var i = 0, len = events.length; i < len; i++) {
          self.undispatchedEventsQueue.push(events[i]);
          // If there are a lot of events then we can hit issues with the call stack size when processing in one go
          triggered = false;
          if (i % 1000 === 0){
            triggered = true;
            trigger(self);
          }
        }
      }

      if (!triggered) {
        trigger(self);
      }

      if (callback) callback(null);
    });
  }
};

module.exports = EventDispatcher;
```

## File: `lib/eventStream.js`
```javascript
var debug = require('debug')('eventstore:eventstream'),
  _ = require('lodash'),
  Event = require('./event');

/**
 * EventStream constructor
 * The eventstream is one of the main objects to interagate with the eventstore.
 * @param {Object} eventstore the eventstore that should be injected
 * @param {Object} query the query object
 * @param {Array} events the events (from store)
 * @constructor
 */
function EventStream (eventstore, query, events) {
  if (!eventstore) {
    var errESMsg = 'eventstore not injected!';
    debug(errESMsg);
    throw new Error(errESMsg);
  }

  if (typeof eventstore.commit !== 'function') {
    var errESfnMsg = 'eventstore.commit not injected!';
    debug(errESfnMsg);
    throw new Error(errESfnMsg);
  }

  if (!query) {
    var errQryMsg = 'query not injected!';
    debug(errQryMsg);
    throw new Error(errQryMsg);
  }

  if (!query.aggregateId) {
    var errAggIdMsg = 'query.aggregateId not injected!';
    debug(errAggIdMsg);
    throw new Error(errAggIdMsg);
  }

  if (events) {
    if (!_.isArray(events)) {
      var errEvtsArrMsg = 'events should be an array!';
      debug(errEvtsArrMsg);
      throw new Error(errEvtsArrMsg);
    }

    for (var i = 0, len = events.length; i < len; i++) {
      var evt = events[i];
      if (evt.streamRevision === undefined || evt.streamRevision === null) {
        var errEvtMsg = 'The events passed should all have a streamRevision!';
        debug(errEvtMsg);
        throw new Error(errEvtMsg);
      }
    }
  }

  this.eventstore = eventstore;
  this.streamId = query.aggregateId;
  this.aggregateId = query.aggregateId;
  this.aggregate = query.aggregate;
  this.context = query.context;
  this.events = events || [];
  this.uncommittedEvents = [];
  this.lastRevision = -1;

  this.events = _.sortBy(this.events, 'streamRevision');

  // to update lastRevision...
  this.currentRevision();
}

EventStream.prototype = {

  /**
   * This helper function calculates and returns the current stream revision.
   * @returns {Number} lastRevision
   */
  currentRevision: function() {
    for (var i = 0, len = this.events.length; i < len; i++) {
      if (this.events[i].streamRevision > this.lastRevision) {
        this.lastRevision = this.events[i].streamRevision;
      }
    }

    return this.lastRevision;
  },

  /**
   * adds an event to the uncommittedEvents array
   * @param {Object} event
   */
  addEvent: function(event) {
    new Event(this, event, this.eventstore.eventMappings);
  },

  /**
   * adds an array of events to the uncommittedEvents array
   * @param {Array} events
   */
  addEvents: function(events) {
    if (!_.isArray(events)) {
      var errEvtsArrMsg = 'events should be an array!';
      debug(errEvtsArrMsg);
      throw new Error(errEvtsArrMsg);
    }
    var self = this;
    _.each(events, function(evt) {
      self.addEvent(evt);
    });
  },

  /**
   * commits all uncommittedEvents
   * @param {Function} callback the function that will be called when this action has finished [optional]
   */
  commit: function(callback) {
    this.eventstore.commit(this, callback);
  }
};

module.exports = EventStream;
```

## File: `lib/eventstore.js`
```javascript
var debug = require('debug')('eventstore'),
  util = require('util'),
  EventEmitter = require('events').EventEmitter,
  _ = require('lodash'),
  async = require('async'),
  tolerate = require('tolerance'),
  EventDispatcher = require('./eventDispatcher'),
  EventStream = require('./eventStream'),
  Snapshot = require('./snapshot');

/**
 * Eventstore constructor
 * @param {Object} options The options.
 * @param {Store}  store   The db implementation.
 * @constructor
 */
function Eventstore(options, store) {
  this.options = options || {};
  this.store = store;

  this.eventMappings = {};

  EventEmitter.call(this);
}

util.inherits(Eventstore, EventEmitter);

_.extend(Eventstore.prototype, {

  /**
   * Inject function for event publishing.
   * @param {Function} fn the function to be injected
   * @returns {Eventstore}  to be able to chain...
   */
  useEventPublisher: function (fn) {
    if (fn.length === 1) {
      fn = _.wrap(fn, function(func, evt, callback) {
        func(evt);
        callback(null);
      });
    }

    this.publisher = fn;

    return this;
  },

  /**
   * Define which values should be mapped/copied to the payload event. [optional]
   * @param {Object} mappings the mappings in dotty notation
   *                          {
   *                            id: 'id',
   *                            commitId: 'commitId',
   *                            commitSequence: 'commitSequence',
   *                            commitStamp: 'commitStamp',
   *                            streamRevision: 'streamRevision'
   *                          }
   * @returns {Eventstore}  to be able to chain...
   */
  defineEventMappings: function (mappings) {
    if (!mappings || !_.isObject(mappings)) {
      var err = new Error('Please pass a valid mapping values!');
      debug(err);
      throw err;
    }

    this.eventMappings = mappings;

    return this;
  },

  /**
   * Call this function to initialize the eventstore.
   * If an event publisher function was injected it will additionally initialize an event dispatcher.
   * @param {Function} callback the function that will be called when this action has finished [optional]
   */
  init: function (callback) {
    var self = this;

    function initDispatcher() {
      debug('init event dispatcher');
      self.dispatcher = new EventDispatcher(self.publisher, self);
      self.dispatcher.start(callback);
    }

    this.store.on('connect', function () {
      self.emit('connect');
    });

    this.store.on('disconnect', function () {
      self.emit('disconnect');
    });

    process.nextTick(function() {
      tolerate(function(callback) {
        self.store.connect(callback);
      }, self.options.timeout || 0, function (err) {
        if (err) {
          debug(err);
          if (callback) callback(err);
          return;
        }
        if (!self.publisher) {
          debug('no publisher defined');
          if (callback) callback(null);
          return;
        }
        initDispatcher();
      });
    });
  },


  // streaming api

  /**
   * streams the events
   * @param {Object || String} query    the query object [optional]
   * @param {Number}           skip     how many events should be skipped? [optional]
   * @param {Number}           limit    how many events do you want in the result? [optional]
   * @returns {Stream} a stream with the events
   */
  streamEvents: function (query, skip, limit) {
    if (!this.store.streamEvents) {
      throw new Error('Streaming API is not suppoted by '+(this.options.type || 'inmemory') +' db implementation.');
    }

    if (typeof query === 'number') {
      limit = skip;
      skip = query;
      query = {};      
    };

    if (typeof query === 'string') {
      query = { aggregateId: query };
    }

    return this.store.streamEvents(query, skip, limit);
  },

  /**
   * streams all the events since passed commitStamp
   * @param {Date}     commitStamp the date object
   * @param {Number}   skip        how many events should be skipped? [optional]
   * @param {Number}   limit       how many events do you want in the result? [optional]
   * @returns {Stream} a stream with the events
   */
  streamEventsSince: function (commitStamp, skip, limit) {
    if (!this.store.streamEvents) {
      throw new Error('Streaming API is not suppoted by '+(this.options.type || 'inmemory') +' db implementation.');
    }

    if (!commitStamp) {
      var err = new Error('Please pass in a date object!');
      debug(err);
      throw err;
    }

    var self = this;
    commitStamp = new Date(commitStamp);

    return this.store.streamEventsSince(commitStamp, skip, limit);
  },


  /**
   * stream events by revision
   * @param {Object || String} query    the query object
   * @param {Number}           revMin   revision start point [optional]
   * @param {Number}           revMax   revision end point (hint: -1 = to end) [optional]
   * @returns {Stream} a stream with the events
   */
  streamEventsByRevision: function (query, revMin, revMax) {
    if (typeof query === 'string') {
      query = { aggregateId: query };
    }

    if (!query.aggregateId) {
      var err = new Error('An aggregateId should be passed!');
      debug(err);
      if (callback) callback(err);
      return;
    }

    return this.store.streamEventsByRevision(query, revMin, revMax);
  },

  /**
   * loads the events
   * @param {Object || String} query    the query object [optional]
   * @param {Number}           skip     how many events should be skipped? [optional]
   * @param {Number}           limit    how many events do you want in the result? [optional]
   * @param {Function}         callback the function that will be called when this action has finished
   *                                    `function(err, events){}`
   */
  getEvents: function (query, skip, limit, callback) {
    if (typeof query === 'function') {
      callback = query;
      skip = 0;
      limit = -1;
      query = {};
    } else if (typeof skip === 'function') {
      callback = skip;
      skip = 0;
      limit = -1;
      if (typeof query === 'number') {
        skip = query;
        query = {};
      }
    } else if (typeof limit === 'function') {
      callback = limit;
      limit = -1;
      if (typeof query === 'number') {
        limit = skip;
        skip = query;
        query = {};
      }
    }

    if (typeof query === 'string') {
      query = { aggregateId: query };
    }

    var self = this;

    function nextFn(callback) {
      if (limit < 0) {
        var resEvts = [];
        resEvts.next = nextFn;
        return process.nextTick(function () { callback(null, resEvts) });
      }
      skip += limit;
      _getEvents(query, skip, limit, callback);
    }

    function _getEvents(query, skip, limit, callback) {
      self.store.getEvents(query, skip, limit, function (err, evts) {
        if (err) return callback(err);
        evts.next = nextFn;
        callback(null, evts);
      });
    }

    _getEvents(query, skip, limit, callback);
  },

  /**
   * loads all the events since passed commitStamp
   * @param {Date}     commitStamp the date object
   * @param {Number}   skip        how many events should be skipped? [optional]
   * @param {Number}   limit       how many events do you want in the result? [optional]
   * @param {Function} callback    the function that will be called when this action has finished
   *                               `function(err, events){}`
   */
  getEventsSince: function (commitStamp, skip, limit, callback) {
    if (!commitStamp) {
      var err = new Error('Please pass in a date object!');
      debug(err);
      throw err;
    }

    if (typeof skip === 'function') {
      callback = skip;
      skip = 0;
      limit = -1;
    } else if (typeof limit === 'function') {
      callback = limit;
      limit = -1;
    }

    var self = this;

    function nextFn(callback) {
      if (limit < 0) {
        var resEvts = [];
        resEvts.next = nextFn;
        return process.nextTick(function () { callback(null, resEvts) });
      }
      skip += limit;
      _getEventsSince(commitStamp, skip, limit, callback);
    }

    commitStamp = new Date(commitStamp);

    function _getEventsSince(commitStamp, skip, limit, callback) {
      self.store.getEventsSince(commitStamp, skip, limit, function (err, evts) {
        if (err) return callback(err);
        evts.next = nextFn;
        callback(null, evts);
      });
    }

    _getEventsSince(commitStamp, skip, limit, callback);
  },

  /**
   * loads the events
   * @param {Object || String} query    the query object
   * @param {Number}           revMin   revision start point [optional]
   * @param {Number}           revMax   revision end point (hint: -1 = to end) [optional]
   * @param {Function}         callback the function that will be called when this action has finished
   *                                    `function(err, events){}`
   */
  getEventsByRevision: function (query, revMin, revMax, callback) {
    if (typeof revMin === 'function') {
      callback = revMin;
      revMin = 0;
      revMax = -1;
    } else if (typeof revMax === 'function') {
      callback = revMax;
      revMax = -1;
    }

    if (typeof query === 'string') {
      query = { aggregateId: query };
    }

    if (!query.aggregateId) {
      var err = new Error('An aggregateId should be passed!');
      debug(err);
      if (callback) callback(err);
      return;
    }

    this.store.getEventsByRevision(query, revMin, revMax, callback);
  },

  /**
   * loads the event stream
   * @param {Object || String} query    the query object
   * @param {Number}           revMin   revision start point [optional]
   * @param {Number}           revMax   revision end point (hint: -1 = to end) [optional]
   * @param {Function}         callback the function that will be called when this action has finished
   *                                    `function(err, eventstream){}`
   */
  getEventStream: function (query, revMin, revMax, callback) {
    if (typeof revMin === 'function') {
      callback = revMin;
      revMin = 0;
      revMax = -1;
    } else if (typeof revMax === 'function') {
      callback = revMax;
      revMax = -1;
    }

    if (typeof query === 'string') {
      query = { aggregateId: query };
    }

    if (!query.aggregateId) {
      var err = new Error('An aggregateId should be passed!');
      debug(err);
      if (callback) callback(err);
      return;
    }

    var self = this;

    this.getEventsByRevision(query, revMin, revMax, function(err, evts) {
      if (err) {
        return callback(err);
      }
      callback(null, new EventStream(self, query, evts));
    });
  },

  /**
   * loads the next snapshot back from given max revision
   * @param {Object || String} query    the query object
   * @param {Number}           revMax   revision end point (hint: -1 = to end) [optional]
   * @param {Function}         callback the function that will be called when this action has finished
   *                                    `function(err, snapshot, eventstream){}`
   */
  getFromSnapshot: function (query, revMax, callback) {
    if (typeof revMax === 'function') {
      callback = revMax;
      revMax = -1;
    }

    if (typeof query === 'string') {
      query = { aggregateId: query };
    }

    if (!query.aggregateId) {
      var err = new Error('An aggregateId should be passed!');
      debug(err);
      if (callback) callback(err);
      return;
    }

    var self = this;

    async.waterfall([

      function getSnapshot(callback) {
        self.store.getSnapshot(query, revMax, callback);
      },

      function getEventStream(snap, callback) {
        var rev = 0;

        if (snap && (snap.revision !== undefined && snap.revision !== null)) {
          rev = snap.revision + 1;
        }

        self.getEventStream(query, rev, revMax, function(err, stream) {
          if (err) {
            return callback(err);
          }

          if (rev > 0 && stream.lastRevision == -1) {
            stream.lastRevision = snap.revision;
          }

          callback(null, snap, stream);
        });
      }],

      callback
    );
  },

  /**
   * stores a new snapshot
   * @param {Object}   obj      the snapshot data
   * @param {Function} callback the function that will be called when this action has finished [optional]
   */
  createSnapshot: function(obj, callback) {
    if (obj.streamId && !obj.aggregateId) {
      obj.aggregateId = obj.streamId;
    }

    if (!obj.aggregateId) {
      var err = new Error('An aggregateId should be passed!');
      debug(err);
      if (callback) callback(err);
      return;
    }

    obj.streamId = obj.aggregateId;

    if (obj.revision) {
      if (typeof (obj.revision) === 'string') {
        const castedRevision = parseFloat(obj.revision);

        if (castedRevision && castedRevision.toString() === obj.revision) { // Determines if the revision was parsed correctly, for the cases where user using custom typed revisions that's not in valid float format like: obj.revision = '1,2,3'
          obj.revision = castedRevision;
        }
      }
    }

    var self = this;

    async.waterfall([
        function getNewIdFromStorage(callback) {
          self.getNewId(callback);
        },
        function commit(id, callback) {
          try {
            var snap = new Snapshot(id, obj);
            snap.commitStamp = new Date();
          } catch (err) {
            return callback(err);
          }

          self.store.addSnapshot(snap, function(error) {
            if (self.options.maxSnapshotsCount) {
              self.store.cleanSnapshots(_.pick(obj, 'aggregateId', 'aggregate', 'context'), callback);
            } else {
              callback(error);
            }
          });
        }],
      callback
    );
  },

  /**
   * commits all uncommittedEvents in the eventstream
   * @param eventstream the eventstream that should be saved (hint: directly use the commit function on eventstream)
   * @param {Function}  callback the function that will be called when this action has finished
   *                             `function(err, eventstream){}` (hint: eventstream.eventsToDispatch)
   */
  commit: function(eventstream, callback) {

    var self = this;

    async.waterfall([

      function getNewCommitId(callback) {
        self.getNewId(callback);
      },

      function commitEvents(id, callback) {
        // start committing.
        var event,
          currentRevision = eventstream.currentRevision(),
          uncommittedEvents = [].concat(eventstream.uncommittedEvents);
        eventstream.uncommittedEvents = [];

        self.store.getNextPositions(uncommittedEvents.length, function(err, positions) {
          if (err)
            return callback(err)

          for (var i = 0, len = uncommittedEvents.length; i < len; i++) {
            event = uncommittedEvents[i];
            event.id = id + i.toString();
            event.commitId = id;
            event.commitSequence = i;
            event.restInCommitStream = len - 1 - i;
            event.commitStamp = new Date();
            currentRevision++;
            event.streamRevision = currentRevision;
            if (positions)
              event.position = positions[i];

            event.applyMappings();
          }

          self.store.addEvents(uncommittedEvents, function(err) {
            if (err) {
              // add uncommitted events back to eventstream
              eventstream.uncommittedEvents = uncommittedEvents.concat(eventstream.uncommittedEvents);
              return callback(err);
            }

            if (self.publisher && self.dispatcher) {
              // push to undispatchedQueue
              self.dispatcher.addUndispatchedEvents(uncommittedEvents);
            } else {
              eventstream.eventsToDispatch = [].concat(uncommittedEvents);
            }

            // move uncommitted events to events
            eventstream.events = eventstream.events.concat(uncommittedEvents);
            eventstream.currentRevision();

            callback(null, eventstream);
          });
        });
      }],

      callback
    );
  },

  /**
   * loads all undispatched events
   * @param {Object || String} query    the query object [optional]
   * @param {Function}         callback the function that will be called when this action has finished
   *                                    `function(err, events){}`
   */
  getUndispatchedEvents: function (query, callback) {
    if (!callback) {
      callback = query;
      query = null;
    }

    if (typeof query === 'string') {
      query = { aggregateId: query };
    }

    this.store.getUndispatchedEvents(query, callback);
  },

  /**
   * loads the last event
   * @param {Object || String} query    the query object [optional]
   * @param {Function}         callback the function that will be called when this action has finished
   *                                    `function(err, event){}`
   */
  getLastEvent: function (query, callback) {
    if (!callback) {
      callback = query;
      query = null;
    }

    if (typeof query === 'string') {
      query = { aggregateId: query };
    }

    this.store.getLastEvent(query, callback);
  },

  /**
   * loads the last event in a stream
   * @param {Object || String} query    the query object [optional]
   * @param {Function}         callback the function that will be called when this action has finished
   *                                    `function(err, eventstream){}`
   */
  getLastEventAsStream: function (query, callback) {
    if (!callback) {
      callback = query;
      query = null;
    }

    if (typeof query === 'string') {
      query = { aggregateId: query };
    }

    var self = this;

    this.store.getLastEvent(query, function (err, evt) {
      if (err) return callback(err);

      callback(null, new EventStream(self, query, evt ? [evt] : []));
    });
  },

  /**
   * Sets the given event to dispatched.
   * @param {Object || String} evtOrId  the event object or its id
   * @param {Function}         callback the function that will be called when this action has finished [optional]
   */
  setEventToDispatched: function (evtOrId, callback) {
    if (typeof evtOrId === 'object') {
      evtOrId = evtOrId.id;
    }
    this.store.setEventToDispatched(evtOrId, callback);
  },

  /**
   * loads a new id from store
   * @param {Function} callback the function that will be called when this action has finished
   */
  getNewId: function (callback) {
    this.store.getNewId(callback);
  }

});

module.exports = Eventstore;
```

## File: `lib/snapshot.js`
```javascript
var debug = require('debug')('eventstore:snapshot');

/**
 * Snapshot constructor
 * The snapshot object will be persisted to the store.
 * @param {String} id  the id of the snapshot
 * @param {Object} obj the snapshot object infos
 * @constructor
 */
function Snapshot (id, obj) {
  if (!id) {
    var errIdMsg = 'id not injected!';
    debug(errIdMsg);
    throw new Error(errIdMsg);
  }

  if (!obj) {
    var errObjMsg = 'object not injected!';
    debug(errObjMsg);
    throw new Error(errObjMsg);
  }

  if (!obj.aggregateId) {
    var errAggIdMsg = 'object.aggregateId not injected!';
    debug(errAggIdMsg);
    throw new Error(errAggIdMsg);
  }

  if (!obj.data) {
    var errDataMsg = 'object.data not injected!';
    debug(errDataMsg);
    throw new Error(errDataMsg);
  }

  this.id = id;
  this.streamId = obj.aggregateId;
  this.aggregateId = obj.aggregateId;
  this.aggregate = obj.aggregate || null;
  this.context = obj.context || null;
  this.commitStamp = null;
  this.revision = obj.revision;
  this.version = obj.version;
  this.data = obj.data;
}

module.exports = Snapshot;
```

## File: `lib/storeEventEmitter.js`
```javascript
var _ = require('lodash');
var Eventstore = require('./eventstore');

/**
 * Emit events before and after execution of eventstore methods.
 * @param {Function} eventstore - eventstore store instance
 */
function StoreEventEmitter(eventstore) {
  if (!eventstore || !(eventstore instanceof Eventstore)) {
    throw new Error('Provided eventstore must be instance of Eventstore');
  }

  var self = this;
  self.eventstore = eventstore;
  self.store = self.eventstore.store;

  /**
   * Get arguments which are emitted
   * @param {Array} args - arguments from original implementation except callback
   */
  function getEmitArguments(args) {
    return {
      milliseconds: Date.now(),
      arguments: args
    };
  }

  /**
   * Enhance original callback to emit an event
   * @param {string} name - name which will be used to emit
   * @param {Function} callback - callback function from original implementation
   * @param {Array} args - arguments from original implementation except callback
   */
  function enhanceCallback(name, callback, args) {
    var originalCallback = callback;

    callback = function () {
      self.eventstore.emit.call(self.eventstore, 'after-' + name, getEmitArguments(args));

      if (originalCallback) {
        return originalCallback.apply(this, arguments);
      }

      return;
    };

    return callback;
  }

  /**
   * add event emitter advice to eventstore method
   * @param {string} name - name which will be used to emit
   * @param {Function} eventstore - eventstore store instance
   * @param {Function} originalMethod  - original implementation which will be extended
   * @param {Array} args - arguments from original implementation except callback
   * @param {Function} callback - callback function from original implementation
   */
  function addEventEmitterToMethod(name, originalMethod, args, callback) {
    args = _.without(args, undefined, null);

    callback = enhanceCallback(name, callback, args);

    self.eventstore.emit.call(self.eventstore, 'before-' + name, getEmitArguments(args));
    return originalMethod.apply(this, _.concat(args, callback || []));
  };

  /**
   * Add event emitter to eventstore methods
   */
  StoreEventEmitter.prototype.addEventEmitter = function () {
    /**
     * add event emitter as an around advice to database methods
     */
    if (this.store.clear) {
      var originalClear = this.store.clear;
      this.store.clear = function (callback) {
        return addEventEmitterToMethod.call(this, 'clear', originalClear, [], callback);
      };
    }

    if (this.store.getNextPositions) {
      var originalGetNextPositions = this.store.getNextPositions;
      this.store.getNextPositions = function (positions, callback) {
        return addEventEmitterToMethod.call(this, 'get-next-positions', originalGetNextPositions, [positions], callback);
      };
    }

    if (this.store.addEvents) {
      var originalAddEvents = this.store.addEvents;
      this.store.addEvents = function (events, callback) {
        return addEventEmitterToMethod.call(this, 'add-events', originalAddEvents, [events], callback);
      };
    }

    if (this.eventstore.getEvents) {
      var originalGetEvents = this.eventstore.getEvents;

      this.eventstore.getEvents = function (query, skip, limit, callback) {
        if (typeof query === 'function') {
          callback = query;
          query = undefined;
        } else if (typeof skip === 'function') {
          callback = skip;
          skip = undefined;
        } else if (typeof limit === 'function') {
          callback = limit;
          limit = undefined;
        }

        return addEventEmitterToMethod.call(this, 'get-events', originalGetEvents, [query, skip, limit], callback);
      };
    }

    if (this.eventstore.getEventsSince) {
      var originalGetEventsSince = this.eventstore.getEventsSince;
      this.eventstore.getEventsSince = function (date, skip, limit, callback) {
        if (typeof skip === 'function') {
          callback = skip;
          skip = undefined;
        } else if (typeof limit === 'function') {
          callback = limit;
          limit = undefined;
        }

        return addEventEmitterToMethod.call(this, 'get-events-since', originalGetEventsSince, [date, skip, limit], callback);
      };
    }

    if (this.eventstore.getEventsByRevision) {
      var originalGetEventsByRevision = this.eventstore.getEventsByRevision;
      this.eventstore.getEventsByRevision = function (query, revMin, revMax, callback) {
        if (typeof revMin === 'function') {
          callback = revMin;
          revMin = undefined;
        } else if (typeof revMax === 'function') {
          callback = revMax;
          revMax = undefined;
        }

        return addEventEmitterToMethod.call(this, 'get-events-by-revision', originalGetEventsByRevision, [query, revMin, revMax], callback);
      };
    }

    if (this.eventstore.getLastEvent) {
      var originalGetLastEvent = this.eventstore.getLastEvent;
      this.eventstore.getLastEvent = function (query, callback) {
        return addEventEmitterToMethod.call(this, 'get-last-event', originalGetLastEvent, [query], callback);
      };
    }

    if (this.eventstore.getUndispatchedEvents) {
      var originalGetUndispatchedEvents = this.eventstore.getUndispatchedEvents;
      this.eventstore.getUndispatchedEvents = function (query, callback) {
        if (!callback) {
          callback = query;
          query = undefined;
        }

        return addEventEmitterToMethod.call(this, 'get-undispatched-events', originalGetUndispatchedEvents, [query], callback);
      };
    }

    if (this.eventstore.setEventToDispatched) {
      var originalSetEventToDispatched = this.eventstore.setEventToDispatched;
      this.eventstore.setEventToDispatched = function (id, callback) {
        return addEventEmitterToMethod.call(this, 'set-event-to-dispatched', originalSetEventToDispatched, [id], callback);
      };
    }

    if (this.store.addSnapshot) {
      var originalAddSnapshots = this.store.addSnapshot;
      this.store.addSnapshot = function (snap, callback) {
        return addEventEmitterToMethod.call(this, 'add-snapshot', originalAddSnapshots, [snap], callback);
      };
    }

    if (this.store.cleanSnapshots) {
      var originalCleanSnapshots = this.store.cleanSnapshots;
      this.store.cleanSnapshots = function (query, callback) {
        return addEventEmitterToMethod.call(this, 'clean-snapshots', originalCleanSnapshots, [query], callback);
      };
    }

    if (this.store.getSnapshot) {
      var originalGetSnapshot = this.store.getSnapshot;
      this.store.getSnapshot = function (query, revMax, callback) {
        return addEventEmitterToMethod.call(this, 'get-snapshot', originalGetSnapshot, [query, revMax], callback);
      };
    }

    if (this.store.removeTransactions) {
      var originalRemoveTransactions = this.store.removeTransactions;
      this.store.removeTransactions = function (evt, callback) {
        return addEventEmitterToMethod.call(this, 'remove-transactions', originalRemoveTransactions, [evt], callback);
      };
    }

    if (this.store.getPendingTransactions) {
      var originalGetPendingTransactions = this.store.getPendingTransactions;
      this.store.getPendingTransactions = function (callback) {
        return addEventEmitterToMethod.call(this, 'get-pending-transactions', originalGetPendingTransactions, [], callback);
      };
    }

    if (this.store.repairFailedTransaction) {
      var originalRepairFailedTransaction = this.store.repairFailedTransaction;
      this.store.repairFailedTransaction = function (lastEvt, callback) {
        return addEventEmitterToMethod.call(this, 'repair-failed-transactions', originalRepairFailedTransaction, [lastEvt], callback);
      };
    }

    if (this.store.removeTables) {
      var originalRemoveTables = this.store.removeTables;
      this.store.removeTables = function (callback) {
        return addEventEmitterToMethod.call(this, 'remove-tables', originalRemoveTables, [], callback);
      };
    }

    if (this.eventstore.streamEvents) {
      var originalStreamEvents = this.eventstore.streamEvents;
      this.eventstore.streamEvents = function (query, skip, limit) {
        return addEventEmitterToMethod.call(this, 'stream-events', originalStreamEvents, [query, skip, limit]);
      };
    }

    if (this.eventstore.streamEventsSince) {
      var originalStreamEventsSince = this.eventstore.streamEventsSince;
      this.eventstore.streamEventsSince = function (date, skip, limit) {
        return addEventEmitterToMethod.call(this, 'stream-events-since', originalStreamEventsSince, [date, skip, limit]);
      };
    }

    if (this.eventstore.streamEventsByRevision) {
      var originalStreamEventsByRevision = this.eventstore.streamEventsByRevision;
      this.eventstore.streamEventsByRevision = function (query, revMin, revMax) {
        return addEventEmitterToMethod.call(this, 'stream-events-by-revision', originalStreamEventsByRevision, [query, revMin, revMax]);
      };
    }

    if (this.eventstore.getEventStream) {
      var originalGetEventStream = this.eventstore.getEventStream;
      this.eventstore.getEventStream = function (query, revMin, revMax, callback) {
        if (typeof revMin === 'function') {
          callback = revMin;
          revMin = undefined;
        } else if (typeof revMax === 'function') {
          callback = revMax;
          revMax = undefined;
        }

        return addEventEmitterToMethod.call(this, 'get-event-stream', originalGetEventStream, [query, revMin, revMax], callback);
      };
    }

    if (this.eventstore.getFromSnapshot) {
      var originalGetFromSnapshot = this.eventstore.getFromSnapshot;
      this.eventstore.getFromSnapshot = function (query, revMax, callback) {
        if (typeof revMax === 'function') {
          callback = revMax;
          revMax = undefined;
        }

        return addEventEmitterToMethod.call(this, 'get-from-snapshot', originalGetFromSnapshot, [query, revMax], callback);
      };
    }

    if (this.eventstore.createSnapshot) {
      var originalCreateSnapshot = this.eventstore.createSnapshot;
      this.eventstore.createSnapshot = function (obj, callback) {
        return addEventEmitterToMethod.call(this, 'create-snapshot', originalCreateSnapshot, [obj], callback);
      };
    }

    if (this.eventstore.commit) {
      var originalCommit = this.eventstore.commit;
      this.eventstore.commit = function (eventstream, callback) {
        return addEventEmitterToMethod.call(this, 'commit', originalCommit, [eventstream], callback);
      };
    }

    if (this.eventstore.getLastEventAsStream) {
      var originalGetLastEventAsStream = this.eventstore.getLastEventAsStream;
      this.eventstore.getLastEventAsStream = function (query, callback) {
        return addEventEmitterToMethod.call(this, 'get-last-event-as-stream', originalGetLastEventAsStream, [query], callback);
      };
    }
  };
}

module.exports = StoreEventEmitter;
```

## File: `lib/databases/azuretable.js`
```javascript
var util = require('util'),
  Store = require('../base'),
  _ = require('lodash'),
  async = require('async'),
  azure = Store.use('azure-storage'),
  eg = azure.TableUtilities.entityGenerator,
  debug = require('debug')('eventstore:store:azuretable');

function AzureTable(options) {

  options = options || {};

  var azureConf = {
    storageAccount: 'nodeeventstore',
    storageAccessKey: 'aXJaod96t980AbNwG9Vh6T3ewPQnvMWAn289Wft9RTv+heXQBxLsY3Z4w66CI7NN12+1HUnHM8S3sUbcI5zctg==',
    storageTableHost: 'https://nodeeventstore.table.core.windows.net/'
  };

  this.options = _.defaults(options, azureConf);

  var defaults = {
    eventsTableName: 'events',
    undispatchedEventsTableName: 'undispatchedevents',
    snapshotsTableName: 'snapshots'
  };

  this.options = _.defaults(this.options, defaults);
}

util.inherits(AzureTable, Store);

_.extend(AzureTable.prototype, {

  connect: function (callback) {
    var self = this;
    var retryOperations = new azure.ExponentialRetryPolicyFilter();
    var server = azure.createTableService(this.options.storageAccount, this.options.storageAccessKey, this.options.storageTableHost).withFilter(retryOperations);

    self.client = server;
    self.isConnected = true;

    var createEventsTable = function (callback) {
      self.client.createTableIfNotExists(self.options.eventsTableName, callback);
    };

    var createSnapshotTable = function (callback) {
      self.client.createTableIfNotExists(self.options.snapshotsTableName, callback);
    };

    var createUndispatchedEventsTable = function (done) {
      self.client.createTableIfNotExists(self.options.undispatchedEventsTableName, done)
    };

    async.parallel([
      createEventsTable,
      createSnapshotTable,
      createUndispatchedEventsTable
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

  clear: function (done) {
    var self = this;
    var query = new azure.TableQuery();

    var clearEventsTable = function (callback) {
      self.client.queryEntities(self.options.eventsTableName, query, null, function (err, entities) {
        if (err) {
          return callback(err);
        }

        async.each(entities.entries, function (entity, callback) {
            self.client.deleteEntity(self.options.eventsTableName, entity, function (error, response) {
              callback(error);
            });
          },
          callback);
      });
    };

    var clearSnapshotsTable = function (callback) {
      self.client.queryEntities(self.options.snapshotsTableName, query, null, function (err, entities) {
        if (err) {
          return callback(err);
        }
        async.each(entities.entries, function (entity, callback) {
            self.client.deleteEntity(self.options.snapshotsTableName, entity, function (error, response) {
              callback(error);
            });
          },
          callback);
      });
    };

    var clearUndispatchedEventsTable = function (callback) {
      self.client.queryEntities(self.options.undispatchedEventsTableName, query, null, function (err, entities) {
        if (err) {
          return callback(err);
        }
        async.each(entities.entries, function (entity, callback) {
            self.client.deleteEntity(self.options.undispatchedEventsTableName, entity, function (error, response) {
              callback(error);
            });
          },
          callback);
      });
    };

    async.parallel([
      clearEventsTable,
      clearSnapshotsTable,
      clearUndispatchedEventsTable
    ], function (err) {
      if (err) {
        debug(err);
        if (done) done(err);
//        if (done) done(null); // strange on azure...
        return;
      }
      if (done) done(null, self);
    });
  },

  addEvents: function (events, callback) {
    var self = this;
    var batch = new azure.TableBatch();

    var noAggId = _.every(events, function (event) {
      return !event.aggregateId
    });

    if (noAggId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    async.concat(events,
      function (event, callback) {

        var results = [
          function (callback) {
            var storedEvent = new StoredEvent(event);
            self.client.insertEntity(self.options.eventsTableName, storedEvent, callback);
          },
          function (callback) {
            var storedUndispatchedEvent = new StoredUndispatchedEvent(event);
            self.client.insertEntity(self.options.undispatchedEventsTableName, storedUndispatchedEvent, callback);
          }
        ]

        callback(null, results);
      },
      function (err, results) {
        async.parallel(results, callback);
      }
    );
  },

  getEvents: function (query, skip, limit, callback) {
    var self = this;
    var tableQuery = new azure.TableQuery();
    var continuationToken = null;
    var entities = [];

    var pageSize = skip + limit;

    tableQuery = _(query)
      .pick(['aggregate', 'context', 'aggregateId'])
      .reduce(function (result, val, key) {
        key = key === 'aggregateId' ? 'PartitionKey' : key;
        if (result._where.length === 0) return tableQuery.where(key + ' eq ?', val);
        return result.and(key + ' eq ?', val)
      }, tableQuery);


    if (limit !== -1) {
      tableQuery = tableQuery.top(pageSize);
    }

    async.doWhilst(function (end) {
      // retrieve entities
      self.client.queryEntities(self.options.eventsTableName, tableQuery, continuationToken, function (err, results) {
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
      return (entities.length < pageSize || pageSize == -1) ? continuationToken !== null : false;
    }, function (err) {
      // return results
      if (err) {
        debug(err);
        return callback(err);
      }

      entities = entities.map(MapStoredEventToEvent);

      entities = _.sortBy(entities, function (e) {
        return e.commitStamp.getTime();
      });

      if (limit === -1) {
        entities = entities.slice(skip);
      } else {
        entities = entities.slice(skip, skip + limit);
      }

      callback(null, entities);
    });
  },

  getEventsSince: function (date, skip, limit, callback) {
    var self = this;
    var tableQuery = new azure.TableQuery();
    var continuationToken = null;
    var entities = [];

    var pageSize = skip + limit;

    tableQuery.where('commitStamp >= ?', date);

    async.doWhilst(function (end) {
      // retrieve entities
      self.client.queryEntities(self.options.eventsTableName, tableQuery, continuationToken, function (err, results) {
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
      return (entities.length < pageSize || pageSize == -1) ? continuationToken !== null : false;
    }, function (err) {
      // return results
      if (err) {
        debug(err);
        return callback(err);
      }

      entities = entities.map(MapStoredEventToEvent);

      entities = _.sortBy(entities, function (e) {
        return e.commitStamp.getTime();
      });

      if (limit === -1) {
        entities = entities.slice(skip);
      } else {
        entities = entities.slice(skip, pageSize);
      }

      callback(null, entities);
    });
  },

  getEventsByRevision: function (query, revMin, revMax, callback) {

    var self = this;
    var tableQuery = new azure.TableQuery();
    var continuationToken = null;
    var entities = [];

    if (!query.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    tableQuery = _(query)
      .pick(['aggregate', 'context', 'aggregateId'])
      .reduce(function (result, val, key) {
        key = key === 'aggregateId' ? 'PartitionKey' : key;
        if (result._where.length === 0) return tableQuery.where(key + ' eq ?', val);
        return result.and(key + ' eq ?', val)
      }, tableQuery);


    tableQuery = tableQuery.and('streamRevision >= ?', revMin);
    if (revMax != -1) tableQuery = tableQuery.and('streamRevision < ?', revMax);

    async.doWhilst(function (end) {
      // retrieve entities
      self.client.queryEntities(self.options.eventsTableName, tableQuery, continuationToken, function (err, results) {
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

      entities = entities.map(MapStoredEventToEvent);

      entities = _.sortBy(entities, function (e) {
        return e.commitStamp.getTime();
      });

      callback(null, entities);
    });
  },

  getUndispatchedEvents: function (query, callback) {

    var self = this;
    var tableQuery = new azure.TableQuery();
    var continuationToken = null;
    var entities = [];

    if (query && query.aggregate) tableQuery.where('aggregate eq ?', query.aggregate);
    if (query && query.context) tableQuery.where('context eq ?', query.context);
    if (query && query.aggregateId) tableQuery.where('aggregateId eq ?', query.aggregateId);

    async.doWhilst(function (end) {
      // retrieve entities
      self.client.queryEntities(self.options.undispatchedEventsTableName, tableQuery, continuationToken, function (err, results) {
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

      entities = entities.map(MapStoredEventToEvent);

      entities = _.sortBy(entities, function (e) {
        return e.commitStamp.getTime();
      });

      callback(null, entities);
    });
  },

  getLastEvent: function (query, callback) {

    var self = this;
    var tableQuery = new azure.TableQuery();
    var continuationToken = null;
    var entities = [];


    tableQuery = _(query)
      .pick(['aggregate', 'context', 'aggregateId'])
      .reduce(function (result, val, key) {
        key = key === 'aggregateId' ? 'PartitionKey' : key;
        if (result._where.length === 0) return tableQuery.where(key + ' eq ?', val);
        return result.and(key + ' eq ?', val)
      }, tableQuery);

    async.doWhilst(function (end) {
      // retrieve entities
      self.client.queryEntities(self.options.eventsTableName, tableQuery, continuationToken, function (err, results) {
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
      return  continuationToken !== null;
    }, function (err) {
      // return results
      if (err) {
        debug(err);
        return callback(err);
      }

      entities = entities.map(MapStoredEventToEvent);

      entities = _.sortBy(entities, function (e) {
        return [e.commitStamp.getTime(),
                e.streamRevision,
                e.commitSequence];
      }).reverse();

      callback(null, entities[0]);
    });
    //this.events.findOne(findStatement, {sort: [['commitStamp', 'desc'], ['streamRevision', 'desc'], ['commitSequence', 'desc']]}, callback);
  },

  setEventToDispatched: function (id, callback) {
    var self = this;

    var objDescriptor = {
      PartitionKey: eg.String(id),
      RowKey: eg.String(id)
    };

    self.client.deleteEntity(self.options.undispatchedEventsTableName, objDescriptor, null, callback);
  },

  addSnapshot: function (snap, callback) {
    var self = this;

    if (!snap.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    self.client.insertEntity(self.options.snapshotsTableName, new StoredSnapshot(snap), callback);
  },

  getSnapshot: function (query, revMax, callback) {

    var self = this;
    var tableQuery = new azure.TableQuery();
    var continuationToken = null;
    var entities = [];

    if (!query.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    tableQuery = _(query)
      .pick(['aggregate', 'context', 'aggregateId'])
      .reduce(function (result, val, key) {
        key = key === 'aggregateId' ? 'PartitionKey' : key;
        if (result._where.length === 0) return tableQuery.where(key + ' eq ?', val);
        return result.and(key + ' eq ?', val)
      }, tableQuery);


    if (revMax != -1) tableQuery = tableQuery.and('revision le ?', revMax);

    async.doWhilst(function (end) {
      // retrieve entities
      self.client.queryEntities(self.options.snapshotsTableName, tableQuery, continuationToken, function (err, results) {
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

      entities = entities.map(MapStoredSnapshotToSnapshot);

      entities = _.sortBy(entities, function (e) {
        return -e.commitStamp.getTime();
      });

      callback(null, entities[0]);
    });

  }

});

var StoredEvent = function (event) {
  this.PartitionKey = eg.EntityProperty(event.aggregateId);
  this.RowKey = eg.EntityProperty(event.id);
  this.aggregateId = eg.EntityProperty(event.aggregateId);
  this.id = eg.EntityProperty(event.id);
  this.context = eg.EntityProperty(event.context);
  this.aggregate = eg.EntityProperty(event.aggregate);
  this.streamRevision = eg.EntityProperty(event.streamRevision);
  this.commitId = eg.EntityProperty(event.commitId);
  this.commitSequence = eg.EntityProperty(event.commitSequence);
  this.commitStamp = eg.EntityProperty(event.commitStamp);
  this.header = eg.EntityProperty(event.header);
  this.dispatched = eg.EntityProperty(event.dispatched || false);
  this.payload = eg.EntityProperty(JSON.stringify(event.payload));
};

function MapStoredEventToEvent(storedEvent) {
  var event = {
    aggregateId: getEntityProperty(storedEvent.aggregateId),
    id: getEntityProperty(storedEvent.id),
    context: getEntityProperty(storedEvent.context),
    aggregate: getEntityProperty(storedEvent.aggregate),
    streamRevision: getEntityProperty(storedEvent.streamRevision),
    commitId: getEntityProperty(storedEvent.commitId),
    commitSequence: getEntityProperty(storedEvent.commitSequence),
    commitStamp: getEntityProperty(storedEvent.commitStamp) || null,
    header: getEntityProperty(storedEvent.header) || null,
    dispatched: getEntityProperty(storedEvent.dispatched),
    payload: JSON.parse(getEntityProperty(storedEvent.payload)) || null
  };

  return event;
}

var StoredUndispatchedEvent = function (event) {
  this.PartitionKey = eg.EntityProperty(event.id);
  this.RowKey = eg.EntityProperty(event.id);
  this.aggregateId = eg.EntityProperty(event.aggregateId);
  this.id = eg.EntityProperty(event.id);
  this.context = eg.EntityProperty(event.context);
  this.aggregate = eg.EntityProperty(event.aggregate);
  this.streamRevision = eg.EntityProperty(event.streamRevision);
  this.commitId = eg.EntityProperty(event.commitId);
  this.commitSequence = eg.EntityProperty(event.commitSequence);
  this.commitStamp = eg.EntityProperty(event.commitStamp);
  this.header = eg.EntityProperty(event.header);
  this.dispatched = eg.EntityProperty(event.dispatched || false);
  this.payload = eg.EntityProperty(JSON.stringify(event.payload));
};

var StoredSnapshot = function (snapshot) {
  this.PartitionKey = eg.EntityProperty(snapshot.aggregateId);
  this.RowKey = eg.EntityProperty(snapshot.id);
  this.id = eg.EntityProperty(snapshot.id);
  this.aggregateId = eg.EntityProperty(snapshot.aggregateId);
  this.aggregate = eg.EntityProperty(snapshot.aggregate) || undefined;
  this.context = eg.EntityProperty(snapshot.context) || undefined;
  this.revision = eg.EntityProperty(snapshot.revision);
  this.version = eg.EntityProperty(snapshot.version);
  this.commitStamp = eg.EntityProperty(snapshot.commitStamp);
  this.data = eg.EntityProperty(JSON.stringify(snapshot.data));
};

function MapStoredSnapshotToSnapshot(storedSnapshot) {
  var snapshot = {
    id: getEntityProperty(storedSnapshot.id),
    aggregateId: getEntityProperty(storedSnapshot.PartitionKey),
    aggregate: getEntityProperty(storedSnapshot.aggregate) || undefined,
    context: getEntityProperty(storedSnapshot.context) || undefined,
    revision: getEntityProperty(storedSnapshot.revision),
    version: getEntityProperty(storedSnapshot.version),
    commitStamp: getEntityProperty(storedSnapshot.commitStamp),
    data: JSON.parse(getEntityProperty(storedSnapshot.data)) || null
  };

  return snapshot;
}

var getEntityProperty = function (propertyField) {
  if (propertyField != null) {
    return propertyField['_'];
  } else {
    return null;
  }
};

module.exports = AzureTable;
```

## File: `lib/databases/dynamodb.js`
```javascript
var util = require('util'),
  Store = require('../base'),
  _ = require('lodash'),
  async = require('async'),
  aws = Store.use('aws-sdk'),
  dbg = require('debug');

var debug = dbg('eventstore:store:dynamodb'),
  error = dbg("eventstore:store:dynamodb:error");

/*
for information on optimizing access patterns see: https://medium.com/building-timehop/one-year-of-dynamodb-at-timehop-f761d9fe5fa1
  - query when possible
  - scan when you will really be visiting all items (or almost all, ex: clear, or undispatched)
  - secondary index when you need only a subset (instead of scan) and it will still be cheaper to run SELECT N+1 query (get partition keys from 2ndary then get full item using getItem(key) )
*/
function DynamoDB(options) {

  options = options || {};

  var awsConf = {
    // don't put AWS credentials in files. Use IAM, ~/.aws/credentials with $AWS_PROFILE, or env vars
    // see: http://docs.aws.amazon.com/AWSJavaScriptSDK/guide/node-configuring.html
    // example using credentials file with $AWS_PROFILE:
    // $ AWS_PROFILE=my-non-default-profile npm test
    region: "us-west-2",
    endpointConf: {}
  };

  // support setting a specific endpoint for dynamodb (ex: DynamoDB local)
  // examples usage for testing:
  // $ AWS_DYNAMODB_ENDPOINT=http://localhost:8000 npm test
  if (process.env["AWS_DYNAMODB_ENDPOINT"]) {
    awsConf.endpointConf = { endpoint: process.env["AWS_DYNAMODB_ENDPOINT"] };
  }

  this.options = _.defaults(options, awsConf);

  var defaults = {
    eventsTableName: 'events',
    undispatchedEventsTableName: 'undispatchedevents',
    snapshotsTableName: 'snapshots',
    // 3 write units / 1 read unit for events & undispatched is just low enough
    // to trigger throttling w/o hitting the 20 test timeout. Takes about 5 minutes to run storeTest.js.
    UndispatchedEventsReadCapacityUnits: 1,
    UndispatchedEventsWriteCapacityUnits: 3,
    EventsReadCapacityUnits: 1,
    EventsWriteCapacityUnits: 3,
    SnapshotReadCapacityUnits: 1,
    SnapshotWriteCapacityUnits: 1,
    useUndispatchedEventsTable: true,
    eventsTableStreamEnabled: false,
    eventsTableStreamViewType: "NEW_IMAGE"
  };

  this.options = _.defaults(this.options, defaults);
}

util.inherits(DynamoDB, Store);

_.extend(DynamoDB.prototype, {

  connect: function (callback) {
    var self = this;
    self.client = new aws.DynamoDB(self.options.endpointConf);
    self.documentClient = new aws.DynamoDB.DocumentClient({ service: self.client });
    self.isConnected = true;

    var createEventsTable = function (callback) {
      createTableIfNotExists(self.client, EventsTableDefinition(self.options), callback);
    };

    var createSnapshotTable = function (callback) {
      createTableIfNotExists(self.client, SnapshotTableDefinition(self.options), callback);
    };

    var createUndispatchedEventsTable = function (done) {
      if (self.options.useUndispatchedEventsTable) {
        createTableIfNotExists(self.client, UndispatchedEventsTableDefinition(self.options), done)
      } else {
        done();
      }
    };

    async.parallel([
      createEventsTable,
      createSnapshotTable,
      createUndispatchedEventsTable
    ], function (err) {
      if (err) {
        error("connect error: " + err);
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

  removeTables: function (done) {
    var self = this;
    // AWS has a limit on the number of DynamoDB tables for an account. Let's clean up when we're done
    debug("remove all tables created for testing");
    deleteAllTempTables(self.client, self.options, function (err, result) {
      if (err) {
        error("removeTables error: " + err);
        return done(err);
      }
      return done(null, result);
    });
  },

  clear: function (done) {
    var self = this;

    var clearEvents = function (callback) {
      clearEventTables(self.options, self.documentClient, function (err) {
        if (err) {
          error("clearEventTables error: " + err);
          return callback(err);
        }

        callback(null, "events");
      });
    };

    var clearSnapshots = function (callback) {
      clearSnapshotsTable(self.options, self.documentClient, function (err) {
        if (err) {
          error("clearSnapshotsTable error: " + err);
          return callback(err);
        }

        callback(null, "snapshots");
      });
    };

    async.parallel([
      clearEvents,
      clearSnapshots
    ], function (err, data) {
      if (err) {
        error("removeTables error: " + err);
        if (done) done(err);
        return;
      }
      if (done) done(null, self);
    });
  },

  addEvents: function (events, callback) {
    var self = this;

    var noAggId = _.every(events, function (event) {
      return !event.aggregateId
    });

    if (noAggId) {
      var errMsg = 'aggregateId not defined!';
      error(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    async.concatSeries(events,
      function (event, callback) {

        var results = [
          function (callback) {
            var storedEvent = {
              TableName: self.options.eventsTableName,
              Item: new StoredEvent(event),
              ExpressionAttributeNames: {
                "#name": "aggregate"
              },
              ConditionExpression: "attribute_not_exists(aggregateId) and attribute_not_exists(streamRevision) and attribute_not_exists(context) and attribute_not_exists(#name)"
            };

            debug("Saving event to events table: " + JSON.stringify(storedEvent, null, 2));
            self.documentClient.put(storedEvent, function (err, data) {
              if (err) {
                error("dynamodb.addEvents error: " + JSON.stringify(err));
                return callback(err);
              } else {
                debug("event saved");
                callback(null, data);
              }
            });
          }];

        if (self.options.useUndispatchedEventsTable) {
          debug("using undispatchedevents table");
          results.push(function (callback) {
            var storedEvent = {
              TableName: self.options.undispatchedEventsTableName,
              Item: new StoredEvent(event),
              ConditionExpression: "attribute_not_exists(id)"
            };

            debug("Saving event to undispatchedevents table " + JSON.stringify(storedEvent, null, 2));
            self.documentClient.put(storedEvent, function (err, data) {
              if (err) {
                error("dynamodb.addUndispatchedEvents error: " + JSON.stringify(err));
                return callback(err);
              } else {
                debug("undispatched event saved");
                callback(null, data);
              }
            });
          });
        }

        callback(null, results);
      },
      function (err, results) {
        if (err) {
          error("addEvents error: " + JSON.stringify(err));
        }
        async.series(results, callback);
      }
    );
  },

  getEvents: function (query, skip, limit, callback) {
    var self = this;
    var client = new aws.DynamoDB.DocumentClient(self.options.endpointConf);
    var exclusiveStartKey = null;
    var entities = [];

    var tableQuery = {
      TableName: self.options.eventsTableName
    };

    var vals = {};

    if (query && query.aggregateId) {
      vals[":a"] = query.aggregateId;
      tableQuery.KeyConditionExpression = "aggregateId = :a";
    }

    if (query && query.aggregate) {
      vals[":name"] = query.aggregate;
      tableQuery.FilterExpression = "#name = :name";
      tableQuery.ExpressionAttributeNames = {
        "#name": "aggregate"
      };
    }

    if (query && query.context) {
      vals[":c"] = query.context;
      if (tableQuery.FilterExpression && tableQuery.FilterExpression.length !== 0)
        tableQuery.FilterExpression += " and context = :c";
      else
        tableQuery.FilterExpression = "context = :c";
    }

    if (Object.keys(vals).length !== 0) {
      tableQuery.ExpressionAttributeValues = vals;
    }

    var pageSize = skip + limit;
    if (limit !== -1) {
      tableQuery.Limit = pageSize;
    }

    async.doWhilst(function (end) {
      if (exclusiveStartKey) tableQuery.ExclusiveStartKey = exclusiveStartKey;

      if (tableQuery.KeyConditionExpression) {
        client.query(tableQuery, function (err, results) {
          if (err) {
            error("getEvents query error: " + err);
            return end(err);
          }
          exclusiveStartKey = results.LastEvaluatedKey || null;
          entities = entities.concat(results.Items);
          end(null);
        });
      } else {
        // no great 2ndary index possibilities here - avoid calling getItems w/o aggregateId
        client.scan(tableQuery, function (err, results) {
          if (err) {
            error("getEvents scan error: " + err);
            return end(err);
          }

          exclusiveStartKey = results.LastEvaluatedKey || null;
          entities = entities.concat(results.Items);
          end(null);
        })
      }
    }, function () {
      return (entities.length < pageSize || pageSize == -1) ? exclusiveStartKey !== null : false;
    }, function (err) {
      if (err) {
        error("getEvents error: " + err);
        return callback(err);
      }

      entities = entities.map(MapStoredEventToEvent);

      entities = _.sortBy(entities, function (e) {
        return [new Date(e.commitStamp).getTime(), e.streamRevision];
      });

      if (limit === -1) {
        entities = entities.slice(skip);
      } else {
        entities = entities.slice(skip, skip + limit);
      }

      callback(null, entities);
    });
  },

  getEventsSince: function (date, skip, limit, callback) {
    var self = this;
    var client = new aws.DynamoDB.DocumentClient(self.options.endpointConf);
    var exclusiveStartKey = null;
    var entities = [];

    var tableQuery = {
      TableName: self.options.eventsTableName,
      FilterExpression: "commitStamp >= :date",
      ExpressionAttributeValues: { ":date": date.getTime() }
    };

    var pageSize = skip + limit;
    if (limit !== -1) {
      tableQuery.Limit = pageSize;
    }

    async.doWhilst(function (end) {
      if (exclusiveStartKey) tableQuery.ExclusiveStartKey = exclusiveStartKey;

      // scan is just really inefficient but if you need to do it often a query on a 2ndary IDX *might* help
      client.scan(tableQuery, function (err, results) {
        if (err) {
          error("getEventsSince scan error: " + err);
          return end(err);
        }

        exclusiveStartKey = results.LastEvaluatedKey || null;
        entities = entities.concat(results.Items);
        end(null);
      });
    }, function () {
      return (entities.length < pageSize || pageSize == -1) ? exclusiveStartKey !== null : false;
    }, function (err) {
      if (err) {
        error("getEventsSince error: " + err);
        return callback(err);
      }

      entities = entities.map(MapStoredEventToEvent);

      entities = _.sortBy(entities, function (e) {
        return e.commitStamp.getTime();
      });

      if (limit === -1) {
        entities = entities.slice(skip);
      } else {
        entities = entities.slice(skip, pageSize);
      }

      callback(null, entities);
    });
  },

  getEventsByRevision: function (query, revMin, revMax, callback) {

    var self = this;
    var client = new aws.DynamoDB.DocumentClient(self.options.endpointConf);
    var exclusiveStartKey = null;
    var entities = [];

    if (!query.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      error(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var tableQuery = {
      TableName: self.options.eventsTableName,
      KeyConditionExpression: "aggregateId = :a",
      FilterExpression: "streamRevision >= :rmin",
      ExpressionAttributeValues: {
        ":a": query.aggregateId,
        ":rmin": revMin
      }
    };

    if (revMax !== -1) {
      tableQuery.FilterExpression = "streamRevision BETWEEN :rmin AND :rmax";
      tableQuery.ExpressionAttributeValues[":rmax"] = revMax;
    }

    if (query && query.aggregate) {
      tableQuery.FilterExpression += " AND #name = :name";
      tableQuery.ExpressionAttributeValues[":name"] = query.aggregate;
      tableQuery.ExpressionAttributeNames = { "#name": "aggregate" };
    }

    if (query && query.context) {
      tableQuery.FilterExpression += " AND context = :ctx";
      tableQuery.ExpressionAttributeValues[":ctx"] = query.context;
    }

    async.doWhilst(function (end) {
      if (exclusiveStartKey) tableQuery.ExclusiveStartKey = exclusiveStartKey;

      client.query(tableQuery, function (err, results) {
        if (err) {
          error("getEventsByRevision query error: " + err);
          return end(err);
        }
        exclusiveStartKey = results.LastEvaluatedKey || null;
        entities = entities.concat(results.Items);
        end(null);
      });
    }, function () {
      return exclusiveStartKey !== null;
    }, function (err) {
      if (err) {
        error("getEventsByRevision error: " + err);
        return callback(err);
      }

      entities = entities.map(MapStoredEventToEvent);

      entities = _.sortBy(entities, function (e) {
        return new Date(e.commitStamp).getTime();
      });

      callback(null, entities);
    });
  },

  getUndispatchedEvents: function (query, callback) {
    var self = this;
    var client = new aws.DynamoDB.DocumentClient(self.options.endpointConf);
    var exclusiveStartKey = null;
    var entities = [];

    if (!self.options.useUndispatchedEventsTable) return entities;

    // TODO: use DynamoDB Streams instead
    var tableQuery = {
      TableName: self.options.undispatchedEventsTableName
    };

    if (query && query.aggregateId) {
      tableQuery.ExpressionAttributeValues = { ":a": query.aggregateId };
      tableQuery.FilterExpression = "aggregateId = :a";
    }

    if (query && query.context) {
      if (tableQuery.FilterExpression && tableQuery.FilterExpression.length !== 0) {
        tableQuery.ExpressionAttributeValues[":ctx"] = query.context;
        tableQuery.FilterExpression += " and context = :ctx";
      } else {
        tableQuery.ExpressionAttributeValues = { ":ctx": query.context };
        tableQuery.FilterExpression = "context = :ctx";
      }
    }

    if (query && query.aggregate) {
      tableQuery.ExpressionAttributeNames = { "#name": "aggregate" };
      if (tableQuery.FilterExpression && tableQuery.FilterExpression.length !== 0) {
        tableQuery.ExpressionAttributeValues[":name"] = query.aggregate;
        tableQuery.FilterExpression += " AND #name = :name";
      } else {
        tableQuery.ExpressionAttributeValues = { ":name": query.aggregate };
        tableQuery.FilterExpression = "#name = :name";
      }
    }

    async.doWhilst(function (end) {
      if (exclusiveStartKey) tableQuery.ExclusiveStartKey = exclusiveStartKey;

      client.scan(tableQuery, function (err, results) {
        if (err) {
          error("getUndispatchedEvents scan error: " + err);
          return end(err);
        }

        exclusiveStartKey = results.LastEvaluatedKey || null;
        entities = entities.concat(results.Items);
        end(null);
      });
    }, function () {
      return exclusiveStartKey !== null;
    }, function (err) {
      if (err) {
        error("getUndispatchedEvents error: " + err);
        return callback(err);
      }

      entities = entities.map(MapStoredEventToEvent);

      entities = _.sortBy(entities, [function (e) {
        return new Date(e.commitStamp).getTime();
      }, 'id']);

      callback(null, entities);
    });
  },

  getLastEvent: function (query, callback) {

    var self = this;
    var client = new aws.DynamoDB.DocumentClient(self.options.endpointConf);
    var exclusiveStartKey = null;
    var entities = [];

    if (!query.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      error(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var tableQuery = {
      TableName: self.options.eventsTableName,
      KeyConditionExpression: "aggregateId = :a",
      ExpressionAttributeValues: {
        ":a": query.aggregateId
      }
    };

    async.doWhilst(function (end) {
      if (exclusiveStartKey) tableQuery.ExclusiveStartKey = exclusiveStartKey;

      client.query(tableQuery, function (err, results) {
        if (err) {
          error("getLastEvent query error: " + err);
          return end(err);
        }
        exclusiveStartKey = results.LastEvaluatedKey || null;
        entities = entities.concat(results.Items);
        end(null);
      });
    }, function () {
      return exclusiveStartKey !== null;
    }, function (err) {
      if (err) {
        error("getLastEvent error: " + err);
        return callback(err);
      }

      entities = entities.map(MapStoredEventToEvent);

      entities = _.sortBy(entities, function (e) {
        return [new Date(e.commitStamp).getTime(),
          e.streamRevision,
          e.commitSequence];
      }).reverse();

      callback(null, entities[0]);
    });
  },

  setEventToDispatched: function (id, callback) {
    var self = this;
    var client = new aws.DynamoDB.DocumentClient(self.options.endpointConf);

    if (!self.options.useUndispatchedEventsTable) return callback();

    var objDescriptor = {
      TableName: self.options.undispatchedEventsTableName,
      Key: {
        id: id
      }
    };

    client.delete(objDescriptor, callback);
  },

  addSnapshot: function (snap, callback) {
    var self = this;
    var client = new aws.DynamoDB.DocumentClient(self.options.endpointConf);

    if (!snap.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      error(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var snapshot = {
      TableName: self.options.snapshotsTableName,
      Item: new StoredSnapshot(snap),
      ConditionExpression: "attribute_not_exists(aggregateId) and attribute_not_exists(id)"
    }
    client.put(snapshot, function (err, data) {
      if (err) {
        error("addSnapshot error: " + err);
        return callback(err);
      }
      callback(null, data);
    });
  },

  getSnapshot: function (query, revMax, callback) {

    var self = this;
    var client = new aws.DynamoDB.DocumentClient(self.options.endpointConf);
    var exclusiveStartKey = null;
    var entities = [];

    if (!query.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      if (callback) callback(new Error(errMsg));
      return;
    }

    var tableQuery = {
      TableName: self.options.snapshotsTableName,
      KeyConditionExpression: "aggregateId = :a",
      ExpressionAttributeValues: {
        ":a": query.aggregateId
      }
    };

    if (query && query.aggregate) {
      tableQuery.ExpressionAttributeNames = { "#name": "aggregate" };
      tableQuery.ExpressionAttributeValues[":name"] = query.aggregate;
      tableQuery.FilterExpression = "#name = :name";
    }

    if (query && query.context) {
      tableQuery.ExpressionAttributeValues[":ctx"] = query.context;
      if (tableQuery.FilterExpression && tableQuery.FilterExpression.length !== 0)
        tableQuery.FilterExpression += " AND context = :ctx";
      else
        tableQuery.FilterExpression = "context = :ctx";
    }

    if (revMax != -1) {
      if (tableQuery.FilterExpression && tableQuery.FilterExpression.length !== 0)
        tableQuery.FilterExpression += " AND revision <= :rmax";
      else
        tableQuery.FilterExpression = "revision <= :rmax";
      tableQuery.ExpressionAttributeValues[":rmax"] = revMax;
    }

    async.doWhilst(function (end) {
      if (exclusiveStartKey) tableQuery.ExclusiveStartKey = exclusiveStartKey;

      client.query(tableQuery, function (err, results) {
        if (err) {
          debug("getSnapshot query error: " + err);
          return end(err);
        }
        exclusiveStartKey = results.LastEvaluatedKey || null;
        entities = entities.concat(results.Items);
        end(null);
      });
    }, function () {
      return exclusiveStartKey !== null;
    }, function (err) {
      if (err) {
        error("getSnapshot error: " + err);
        return callback(err);
      }

      entities = entities.map(MapStoredSnapshotToSnapshot);

      entities = _.sortBy(entities, function (e) {
        return - new Date(e.commitStamp).getTime();
      });

      callback(null, entities[0]);
    });
  }
});

var StoredEvent = function (event) {
  debug("Converting event to StoredEvent: " + JSON.stringify(event, null, 2));
  this.aggregateId = event.aggregateId;
  this.rowKey = (event.context || "") + ":" + (event.aggregate || "") + ":" + _.padStart(event.streamRevision, 16, '0');
  this.id = event.id;
  this.context = event.context;
  this.aggregate = event.aggregate;
  this.streamRevision = event.streamRevision;
  this.commitId = event.commitId;
  this.commitSequence = event.commitSequence;
  this.commitStamp = new Date(event.commitStamp).getTime();
  this.header = event.header;
  this.dispatched = event.dispatched || false;
  this.payload = JSON.stringify(event.payload);
  debug("Event converted to StoredEvent: " + JSON.stringify(this, null, 2));
};

function MapStoredEventToEvent(storedEvent) {
  var event = {
    aggregateId: storedEvent.aggregateId,
    id: storedEvent.id,
    context: storedEvent.context,
    aggregate: storedEvent.aggregate,
    streamRevision: storedEvent.streamRevision,
    commitId: storedEvent.commitId,
    commitSequence: storedEvent.commitSequence,
    commitStamp: new Date(storedEvent.commitStamp) || null,
    header: storedEvent.header || null,
    dispatched: storedEvent.dispatched,
    payload: JSON.parse(storedEvent.payload) || null
  };

  return event;
}

var StoredSnapshot = function (snapshot) {
  this.id = snapshot.id;
  this.aggregateId = snapshot.aggregateId;
  this.aggregate = snapshot.aggregate || undefined;
  this.context = snapshot.context || undefined;
  this.revision = snapshot.revision;
  this.version = snapshot.version;
  this.commitStamp = new Date(snapshot.commitStamp).getTime();
  this.data = JSON.stringify(snapshot.data);
};

function MapStoredSnapshotToSnapshot(storedSnapshot) {
  var snapshot = {
    id: storedSnapshot.id,
    aggregateId: storedSnapshot.aggregateId,
    aggregate: storedSnapshot.aggregate || undefined,
    context: storedSnapshot.context || undefined,
    revision: storedSnapshot.revision,
    version: storedSnapshot.version,
    commitStamp: new Date(storedSnapshot.commitStamp) || null,
    data: JSON.parse(storedSnapshot.data) || null
  };

  return snapshot;
}

function EventsTableDefinition(opts) {
  var def = {
    TableName: opts.eventsTableName,
    KeySchema: [
      { AttributeName: "aggregateId", KeyType: "HASH" },
      { AttributeName: "rowKey", KeyType: "RANGE" }
    ],
    AttributeDefinitions: [
      { AttributeName: "aggregateId", AttributeType: "S" },
      { AttributeName: "rowKey", AttributeType: "S" }
    ],
    ProvisionedThroughput: {
      ReadCapacityUnits: opts.EventsReadCapacityUnits,
      WriteCapacityUnits: opts.EventsWriteCapacityUnits
    }
  };

  if(opts.eventsTableStreamEnabled) {
    _.assign(def, {
      StreamSpecification: {
        StreamEnabled: true,
        StreamViewType: opts.eventsTableStreamViewType
      }
    })
  };

  return def;
}

function SnapshotTableDefinition(opts) {
  var def = {
    TableName: opts.snapshotsTableName,
    KeySchema: [
      { AttributeName: "aggregateId", KeyType: "HASH" },
      { AttributeName: "id", KeyType: "RANGE" }
    ],
    AttributeDefinitions: [
      { AttributeName: "aggregateId", AttributeType: "S" },
      { AttributeName: "id", AttributeType: "S" }
    ],
    ProvisionedThroughput: {
      ReadCapacityUnits: opts.SnapshotReadCapacityUnits,
      WriteCapacityUnits: opts.SnapshotWriteCapacityUnits
    }
  };

  return def;
}

function UndispatchedEventsTableDefinition(opts) {
  var def = {
    TableName: opts.undispatchedEventsTableName,
    KeySchema: [
      { AttributeName: "id", KeyType: "HASH" }
    ],
    AttributeDefinitions: [
      { AttributeName: "id", AttributeType: "S" }
    ],
    ProvisionedThroughput: {
      ReadCapacityUnits: opts.UndispatchedEventsReadCapacityUnits,
      WriteCapacityUnits: opts.UndispatchedEventsWriteCapacityUnits
    }
  };

  return def;
}

function isTableAlreadyExistsError (err) {
  return err.code === "ResourceInUseException" && err.message === "Cannot create preexisting table";
}

var createTableIfNotExists = function (client, params, callback) {
  var exists = function (p, cbExists) {
    client.describeTable({ TableName: p.TableName }, function (err, data) {
      if (err) {
        if (err.code === "ResourceNotFoundException") {
          debug("Table " + p.TableName + " doesn't exist yet: " + JSON.stringify(p, null, 2));
          cbExists(null, { exists: false, definition: p });
        } else {
          error("Table " + p.TableName + " doesn't exist yet but describeTable: " + JSON.stringify(err, null, 2));
          cbExists(err);
        }
      } else {
        debug("Table " + p.TableName + " already exists.");
        cbExists(null, { exists: true, description: data });
      }
    });
  };

  var create = function (r, cbCreate) {
    if (!r.exists) {
      debug("Creating " + r.definition.TableName);
      client.createTable(r.definition, function (err, data) {
        if (err && !isTableAlreadyExistsError(err)) {
          error("Error while creating " + r.definition.TableName + ": " + JSON.stringify(err, null, 2));
          cbCreate(err);
        } else {
          debug(params.TableName + " created. Waiting for activiation.");
          cbCreate(null, { Table: { TableName: params.TableName, TableStatus: data ? data.TableDescription.TableStatus : "UNKNOWN"} });
        }
      });
    } else {
      cbCreate(null, r.description);
    }
  };

  var active = function (d, cbActive) {
    var status = d.Table.TableStatus;
    async.until(
      function () { return status === "ACTIVE" },
      function (cbUntil) {
        debug("checking " + d.Table.TableName + " status.");
        client.describeTable({ TableName: d.Table.TableName }, function (err, data) {
          if (err) {
            error("There was an error checking " + d.Table.TableName + " status: " + JSON.stringify(err, null, 2));
            cbUntil(err);
          } else {
            status = data.Table.TableStatus;
            setTimeout(cbUntil, 1000);
          }
        });
      },
      function (err, r) {
        if (err) {
          error("connect create table error: " + err);
          return cbActive(err);
        }
        debug("Table " + d.Table.TableName + " is active.");
        cbActive(null, r);
      });
  };

  async.compose(active, create, exists)(params, function (err, result) {
    if (err) callback(err);
    else callback(null, result);
  });
};

var deleteTableIfExists = function (client, tableName, callback) {
  var exists = function (name, cbExists) {
    client.describeTable({ TableName: name }, function (err, data) {
      if (err) {
        if (err.code === "ResourceNotFoundException") {
          cbExists(null, { exists: false, definition: { TableName: name } });
        } else {
          error("deleteTableIfExists - describeTable error: " + JSON.stringify(err, null, 2));
          cbExists(err);
        }
      } else {
        cbExists(null, { exists: true, description: { TableName: data.Table.TableName } });
      }
    });
  };

  var deleteTable = function (r, cbDelete) {
    if (r.exists) {
      client.deleteTable(r.description, function (err, data) {
        if (err) {
          error("Error deleting '" + r.description.TableName + "': " + JSON.stringify(err, null, 2));
          cbDelete(err);
        } else {
          cbDelete(null, { Table: { TableName: data.TableDescription.TableName, TableStatus: data.TableDescription.TableStatus } });
        }
      });
    } else {
      cbDelete(null, r.description);
    }
  };

  var active = function (d, cbActive) {
    var status = d.Table.TableStatus;
    async.until(
      function () { return status === "DELETED" },
      function (cbUntil) {
        client.describeTable({ TableName: d.Table.TableName }, function (err, data) {
          if (err) {
            if (err.code === "ResourceNotFoundException") {
              status = "DELETED";
              return cbUntil(null, d.Table.TableName);
            }
            error("Error calling describeTable for '" + d.Table.TableName + "'");
            cbUntil(err);
          } else {
            setTimeout(cbUntil, 1000);
          }
        });
      },
      function (err, r) {
        if (err) {
          error("connect delete table error: " + err);
          return cbActive(err);
        }
        cbActive(null, r);
      });
  };

  async.compose(active, deleteTable, exists)(tableName, function (err, result) {
    if (err) callback(err);
    else callback(null, result);
  });
};

var clearEventTables = function (opts, documentClient, cleared) {
  var exclusiveStartKey = null;
  var retryCount = 0;

  debug("clearning events tables");
  var maps = [
    {
      TableName: opts.eventsTableName,
      keyMap: function (n) {
        return { DeleteRequest: { Key: { aggregateId: n.aggregateId, rowKey: n.rowKey } } };
      }
    },
  ];

  if (opts.useUndispatchedEventsTable) {
    maps.push({
      TableName: opts.undispatchedEventsTableName,
      keyMap: function (n) {
        return { DeleteRequest: { Key: { id: n.id } } };
      }
    });
  }

  var read = function (task, callback) {
    documentClient.scan(task.params, function (err, page) {
      if (err) {
        error("clearEventTables scan error: " + err);
        return callback(err);
      }

      retryCount = 0;
      exclusiveStartKey = page.LastEvaluatedKey || null;

      if (page.Count == 0) {
        return callback(null, {});
      }

      var batch = {
        RequestItems: {},
        ReturnConsumedCapacity: "INDEXES",
        ReturnItemCollectionMetrics: "SIZE"
      };

      _.forEach(task.maps, function (m) {
        var keys = _.map(page.Items, m.keyMap);
        batch.RequestItems[m.TableName] = keys;
      });

      callback(null, batch);
    });
  };

  var write = function (batch, callback) {
    if (batch && batch.RequestItems) {
      debug("Clear: calling batchWrite: " + JSON.stringify(batch, null, 2));
      documentClient.batchWrite(batch, function (err, result) {
        if (err) {
          error("Clear (batchWrite) error): " + JSON.stringify(batch, null, 2));
          return callback(err);
        }

        if (Object.keys(result.UnprocessedItems).length !== 0) {
          retryCount++;
          var retry = {
            RequestItems: result.UnprocessedItems,
            ReturnConsumedCapacity: "INDEXES",
            ReturnItemCollectionMetrics: "SIZE"
          };
          debug("Clear batchWrite throttling: " + JSON.stringify(retry, null, 2));
          // retry with exponential backoff
          var delay = retryCount > 0 ? (50 * Math.pow(2, retryCount - 1)) : 0;
          setTimeout(write, delay, retry, callback);
          return;
        }

        callback(null, result);
      });
    } else {
      callback(null);
    }
  };

  var tasks = [
    {
      params: {
        TableName: opts.eventsTableName,
        ProjectionExpression: "aggregateId,rowKey,id",
        Limit: 25, // max 25 per batchWrite call
        ConsistentRead: false,
        ReturnConsumedCapacity: "TOTAL"
      },
      maps: [maps[0]]
    }
  ];

  if (opts.useUndispatchedEventsTable) {
    tasks.splice(0, 0, {
      params: {
        TableName: opts.undispatchedEventsTableName,
        ProjectionExpression: "aggregateId,rowKey,id",
        Limit: 12, // max 25 per batchWrite call divided by 2 tables
        ConsistentRead: false,
        ReturnConsumedCapacity: "TOTAL"
      },
      maps: maps
    });
  }

  async.eachSeries(tasks, function (t, afterEach) {

    async.doWhilst(function (next) {

      if (exclusiveStartKey)
        t.params.ExclusiveStartKey = exclusiveStartKey;

      async.seq(read, write)(t, function (err, result) {
        if (err) next(err);
        else next(null, result);
      });

    }, function () {
      return exclusiveStartKey !== null;
    }, function (err, r) {
      if (err) {
        error("clearEvents error: " + err);
        return afterEach(err);
      }
      return afterEach();
    });

  }, function (err) {
    if (err) {
      error("Error while clearning events tables: " + JSON.stringify(err, null, 2));
      return cleared(err);
    }
    debug("Events tables successfully cleared.");
    return cleared();
  });

};

var clearSnapshotsTable = function (opts, documentClient, cleared) {
  var exclusiveStartKey = null;

  var query = {
    TableName: opts.snapshotsTableName,
    ProjectionExpression: "aggregateId,id",
    Limit: 25, // max 25 per batchWrite call
    ConsistentRead: false,
    ReturnConsumedCapacity: "TOTAL"
  };

  async.doWhilst(function (end) {
    if (exclusiveStartKey)
      query.ExclusiveStartKey = exclusiveStartKey;

    documentClient.scan(query, function (err, page) {
      if (err) {
        error("clearSnapshotsTable scan error: " + err);
        return end(err);
      }

      exclusiveStartKey = page.LastEvaluatedKey || null;

      if (page.Count === 0) {
        return end(err);
      }

      var keys = _.map(page.Items, function (n) {
        return { DeleteRequest: { Key: n } }
      });

      var batch = {
        RequestItems: {},
        ReturnConsumedCapacity: "TOTAL",
        ReturnItemCollectionMetrics: "SIZE"
      };
      batch.RequestItems[opts.snapshotsTableName] = keys;

      documentClient.batchWrite(batch, function (err2, data) {
        error("clearSnapshotsTable batchWrite error: " + err2);
        return end(err2);
      });
    });
  }, function () {
    return exclusiveStartKey !== null;
  }, function (err, r) {
    if (err) {
      error("clearSnapshotsTable error: " + err);
      return cleared(error);
    }
    return cleared(null);;
  });
};

var deleteAllTempTables = function (client, opts, done) {
  var exclusiveStartTableName = null;

  var read = function (query, callback) {
    if (exclusiveStartTableName)
      query.ExclusiveStartTableName = exclusiveStartTableName;

    client.listTables(query, function (err, list) {
      if (err) {
        error("deleteAllTempTables listTables error: " + err);
        return callback(err);
      }

      exclusiveStartTableName = list.LastEvaluatedTableName || null;
      var targets = _.filter(list.TableNames, function (t) {
        return t === opts.eventsTableName ||
          t === opts.undispatchedEventsTableName ||
          t === opts.snapshotsTableName;
      });

      callback(null, targets);
    });
  };

  var drop = function (targets, callback) {
    async.each(targets, function (t, deleted) {
      deleteTableIfExists(client, t, deleted);
    }, function (err) {
      if (err) {
        error("deleteAllTempTables drop error: " + err);
        return callback(err);
      }
      return callback(null);
    });
  };

  async.doWhilst(function (next) {
    async.compose(drop, read)({}, function (err, result) {
      if (err) next(err);
      else next(null, result);
    });
  }, function () {
    return exclusiveStartTableName !== null;
  }, function (err, result) {
    if (err) {
      error("deleteAllTempTables error: " + err);
      return done(err);
    }
    done(null, result);
  });
};

module.exports = DynamoDB;
```

## File: `lib/databases/elasticsearch.js`
```javascript
var util = require('util'),
  Store = require('../base'),
  _ = require('lodash'),
  uuid = require('uuid'),
  elasticsearch = Store.use('elasticsearch'),
  elasticsearchVersion = Store.use('elasticsearch/package.json').version,
  debug = require('debug')('eventstore:store:elasticsearch');

function Elastic(options) {
  options = options || {};

  Store.call(this, options);

  var defaults = {
    host: 'localhost:9200',
    indexName: 'eventstore',
    eventsTypeName: 'events',
    snapshotsTypeName: 'snapshots',
    log: 'warning',
    maxSearchResults: 10000
  };

  _.defaults(options, defaults);

  var defaultOpt = {
    auto_reconnect: false,
    ssl: false
  };

  options.options = options.options || {};

  _.defaults(options.options, defaultOpt);

  this.options = options;
}

util.inherits(Elastic, Store);

_.extend(Elastic.prototype, {

  connect: function (callback) {
    var options = this.options;
    if (options.client) {
  		this.client = options.client;
  	} else {
  		this.client = new elasticsearch.Client({host: options.host, log: options.log});
  	}
    this.emit('connect');
    if (callback) callback(null);
  },

  disconnect: function (callback) {
    this.client = null;
    this.emit('disconnect');
    if (callback) callback(null);
  },

  clear: function (callback) {
    var self = this;
    var options = this.options;
    this.client.indices.exists({index: options.indexName}, function (err, result) {
      if (result){
        self.client.indices.delete({index: options.indexName}, function (err) {
          if (callback) callback(err);
        });
      } else {
        if (callback) callback(err);
      }
    });
  },

  getNewId: function(callback) {
    callback(null, uuid.v4());
  },

  addEvents: function (events, callback) {
    var options = this.options;

    if (events.length === 0) {
      if (callback) callback(null);
      return;
    }

    var noAggId = false;
    var bulkMap = [];

    _.forEach(events, function (evt) {
      if (!evt.aggregateId) {
        noAggId = true;
      }
      evt.dispatched = false;
      bulkMap.push({create: {_index: options.indexName, _type: options.eventsTypeName, _id: evt.id}});
      bulkMap.push(evt);
    });

    if (noAggId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }
    this.client.bulk({body: bulkMap, refresh: true}, function(error, response){
      if (callback) callback(error);
    });
  },

  _buildQuery: function(type, find, sort, skip, limit) {
    var query = {
      index: this.options.indexName,
      type: type,
      defaultOperator: 'AND',
      from: (!skip ? 0 : skip),
      size: (!limit || limit === -1 ? this.options.maxSearchResults - (skip || 0) : limit)
    };
    if (find && find.length) query.q = find.join(' AND ');
    if (sort && sort.length) query.sort = sort;
    return query;
  },

  _search: function (type, find, sort, skip, limit, callback) {
    var options = this.options;
    var searchOptions = this._buildQuery(type, find, sort, skip, limit);

    this.client.search(searchOptions, function (error, response) {
      var dataList = [];
      if (response) {
        if (response.error) {
          var error = new Error(response.error.root_cause ? response.error.root_cause[0].reason : response.error);
          debug(error.message);
          return callback(error);
        }
        if (response.hits && response.hits.hits && response.hits.hits.length) {
          if (response.hits.hits.length >= options.maxSearchResults){
            var errMsg = 'reached maximum of ' + options.maxSearchResults + ' search results!';
            debug(errMsg);
            if (callback) callback(new Error(errMsg));
            return;
          }
          dataList = response.hits.hits.map(function (data) {
            data._source.commitStamp = new Date(data._source.commitStamp);
            return data._source;
          });
        }
      }

      callback(null, dataList);
    });
  },

  _searchEvents: function(find, skip, limit, callback) {
    this._search(this.options.eventsTypeName, find, ['commitStamp:asc', 'streamRevision:asc', 'commitSequence:asc'], skip, limit, callback);
  },

  _searchSnapshots: function(find, skip, limit, callback) {
    this._search(this.options.snapshotsTypeName, find, ['revision:desc', 'version:desc', 'commitStamp:desc'], skip, limit, callback);
  },

  getEvents: function (query, skip, limit, callback) {
    var findStatement = [];
    if (query.aggregate) findStatement.push('aggregate:' + query.aggregate);
    if (query.context) findStatement.push('context:' + query.context);
    if (query.aggregateId) findStatement.push('aggregateId:' + query.aggregateId);

    this._searchEvents(findStatement, skip, limit, callback);
  },

  getLastEvent: function (query, callback) {
    if (!query.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var findStatement = [ 'aggregateId:' + query.aggregateId ];
    if (query.aggregate) findStatement.push('aggregate:' + query.aggregate);
    if (query.context) findStatement.push('context:' + query.context);

    this._search(this.options.eventsTypeName, findStatement, ['commitStamp:desc', 'streamRevision:desc', 'commitSequence:desc'], 0, 1,  function(error, response){
      var event = response && response.length ? response[0] : null;
      if (callback) callback(null, event);
    });
  },

  getEventsSince: function (date, skip, limit, callback) {
    var findStatement = ['commitStamp:[' + date.toJSON() + ' TO *]'];

    this._searchEvents(findStatement, skip, limit, callback);
  },

  getEventsByRevision: function (query, revMin, revMax, callback) {
    if (!query.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var findStatement = [];
    if (revMax === -1) {
      findStatement.push('streamRevision:[' + revMin + ' TO *]');
    } else {
      findStatement.push('streamRevision:[' + revMin + ' TO ' + revMax + '}');
    }
    findStatement.push('aggregateId:' + query.aggregateId);
    if (query.aggregate) findStatement.push('aggregate:' + query.aggregate);
    if (query.context) findStatement.push('context:' + query.context);

    this._searchEvents(findStatement, null, null, callback);
  },

  getUndispatchedEvents: function (query, callback) {
    var findStatement = ['dispatched:false'];
    if (query && query.aggregate) findStatement.push('aggregate:' + query.aggregate);
    if (query && query.context) findStatement.push('context:' + query.context);
    if (query && query.aggregateId) findStatement.push('aggregateId:' + query.aggregateId);

    this._searchEvents(findStatement, null, null, callback);
  },

  setEventToDispatched: function (id, callback) {
    this.client.update({
      index: this.options.indexName,
      type: this.options.eventsTypeName,
      id: id,
      body: {
        doc: {
          dispatched: true
        }
      },
      refresh: true
    }, function (error, response) {
      if (callback) callback(error);
    });
  },

  addSnapshot: function(snap, callback) {
    if (!snap.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    this.client.create({
      index: this.options.indexName,
      type: this.options.snapshotsTypeName,
      id: snap.id,
      body: snap,
      refresh: true
    }, function (error, response) {
      if (callback) callback(error);
    });
  },

  cleanSnapshots: function (query, callback) {
    if (!query.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var findStatement = ['aggregateId:' + query.aggregateId];

    if (query.aggregate) findStatement.push('aggregate:' + query.aggregate);
    if (query.context) findStatement.push('context:' + query.context);

    var self = this;
    this._searchSnapshots(findStatement, this.options.maxSnapshotsCount, -1, function (error, response) {
      if (error) {
        return callback(error);
      }
      self._bulkDelete(self.options.snapshotsTypeName, response, callback);
    });
  },

  _bulkDelete: function (type, items, callback) {
    var index = this.options.indexName;
    var deleteStatements = items.map(function(item) {
      return {
        delete: {
          _index: index,
          _type: type,
          _id: item.id
        }
      };
    });
    this.client.bulk({
      body: deleteStatements
    }, function(error, response) {
      callback(error, response ? response.items.length : 0);
    });
  },

  getSnapshot: function (query, revMax, callback) {
    if (!query.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var findStatement = ['aggregateId:' + query.aggregateId];

    if (query.aggregate) findStatement.push('aggregate:' + query.aggregate);
    if (query.context) findStatement.push('context:' + query.context);
    if (revMax > -1) findStatement.push('revision:[* TO ' + revMax + ']');

    this._searchSnapshots(findStatement, 0, 1, function(error, response){
      var snap = response && response.length ? response[0] : null;
      if (callback) callback(null, snap);
    });
  }

});

module.exports = Elastic;
```

## File: `lib/databases/inmemory.js`
```javascript
var util = require('util'),
  Store = require('../base'),
  _ = require('lodash'),
  jsondate = require('jsondate'),
  debug = require('debug')('eventstore:store:inmemory');

function InMemory(options) {
  Store.call(this, options);
  this.store = {};
  this.snapshots = {};
  this.undispatchedEvents = { _direct: {} };
  this.options = options;
  if (options.trackPosition)
    this.position = 0;    
}

util.inherits(InMemory, Store);

function deepFind (obj, pattern) {
  var found;

  if (pattern) {
    var parts = pattern.split('.');

    found = obj;
    for (var i in parts) {
      found = found[parts[i]];
      if (_.isArray(found)) {
        found = _.filter(found, function (item) {
          var deepFound = deepFind(item, parts.slice(i + 1).join('.'));
          return !!deepFound;

        });
        break;
      }

      if (!found) {
        break;
      }
    }
  }

  return found;
}

_.extend(InMemory.prototype, {

  connect: function (callback) {
    this.emit('connect');
    if (callback) callback(null, this);
  },

  disconnect: function (callback) {
    this.emit('disconnect');
    if (callback) callback(null);
  },

  clear: function (callback) {
    this.store = {};
    this.snapshots = {};
    this.undispatchedEvents = { _direct: {} };
    this.position = 0;
    if (callback) callback(null);
  },

  getNextPositions: function(positions, callback) {
    if (!this.options.trackPosition) {
      return callback(null);
    }
    
    var range = [];
    for(var i=0; i<positions; i++) {
      range.push(++this.position);
    }
    callback(null, range);
  },

  addEvents: function (events, callback) {
    if (!events || events.length === 0) {
      callback(null);
      return;
    }

    var found = _.find(events, function(evt) {
      return !evt.aggregateId;
    });

    if (found) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var aggregateId = events[0].aggregateId;
    var aggregate = events[0].aggregate || '_general';
    var context = events[0].context || '_general';

    this.store[context] = this.store[context] || {};
    this.store[context][aggregate] = this.store[context][aggregate] || {};
    this.store[context][aggregate][aggregateId] = this.store[context][aggregate][aggregateId] || [];
    this.store[context][aggregate][aggregateId] = this.store[context][aggregate][aggregateId].concat(events);

    this.undispatchedEvents[context] = this.undispatchedEvents[context] || {};
    this.undispatchedEvents[context][aggregate] = this.undispatchedEvents[context][aggregate] || {};
    this.undispatchedEvents[context][aggregate][aggregateId] = this.undispatchedEvents[context][aggregate][aggregateId] || [];
    this.undispatchedEvents[context][aggregate][aggregateId] = this.undispatchedEvents[context][aggregate][aggregateId].concat(events);

    var self = this;
    _.forEach(events, function(evt) {
      self.undispatchedEvents._direct[evt.id] = evt;
    });

    callback(null);
  },

  getEvents: function (query, skip, limit, callback) {
    var res = [];
    for (var s in this.store) {
      for (var ss in this.store[s]) {
        for (var sss in this.store[s][ss]) {
          res = res.concat(this.store[s][ss][sss]);
        }
      }
    }

    res = _.sortBy(res, function (e) {
      return e.commitStamp.getTime();
    });

    if (!_.isEmpty(query)) {
      res = _.filter(res, function(e) {
        var keys = _.keys(query);
        var values = _.values(query);
        var found = false;
        for (var i in keys) {
          var key = keys[i];
          var deepFound = deepFind(e, key);
          if (_.isArray(deepFound) && deepFound.length > 0) {
            found = true;
          } else if (deepFound === values[i]) {
            found = true;
          } else {
            found = false;
            break;
          }
        }
        return found;
      });
    }

    if (limit === -1) {
      return callback(null, _.cloneDeep(res.slice(skip)));
    }

    if (res.length <= skip) {
      return callback(null, []);
    }

    callback(null, _.cloneDeep(res.slice(skip, skip + limit)));
  },

  getEventsSince: function (date, skip, limit, callback) {
    var res = [];
    for (var s in this.store) {
      for (var ss in this.store[s]) {
        for (var sss in this.store[s][ss]) {
          res = res.concat(this.store[s][ss][sss]);
        }
      }
    }

    res = _.sortBy(res, function (e) {
      return e.commitStamp.getTime();
    });

    res = _.filter(res, function(e) {
      return e.commitStamp.getTime() >= date.getTime();
    });

    if (limit === -1) {
      return callback(null, _.cloneDeep(res.slice(skip)));
    }

    if (res.length <= skip) {
      return callback(null, []);
    }

    callback(null, _.cloneDeep(res.slice(skip, skip + limit)));
  },

  getEventsByRevision: function (query, revMin, revMax, callback) {
    var res = [];

    if (!query.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    if (query.context && query.aggregate) {
      this.store[query.context] = this.store[query.context] || {};
      this.store[query.context][query.aggregate] = this.store[query.context][query.aggregate] || {};

      if (!this.store[query.context][query.aggregate][query.aggregateId]) {
        return callback(null, _.cloneDeep(res));
      }
      else {
        if (revMax === -1) {
          res = res.concat(this.store[query.context][query.aggregate][query.aggregateId].slice(revMin));
        }
        else {
          res = res.concat(this.store[query.context][query.aggregate][query.aggregateId].slice(revMin, revMax));
        }
      }
      return callback(null, _.cloneDeep(res));
    }

    if (!query.context && query.aggregate) {
      for (var s in this.store) {
        var c = this.store[s];
        if (c[query.aggregate] && c[query.aggregate][query.aggregateId]) {
          if (revMax === -1) {
            res = res.concat(c[query.aggregate][query.aggregateId].slice(revMin));
          }
          else {
            res = res.concat(c[query.aggregate][query.aggregateId].slice(revMin, revMax));
          }
        }
      }
      return callback(null, _.cloneDeep(res));
    }

    if (query.context && !query.aggregate) {
      var cc = this.store[query.context] || {};
      for (var ss in cc) {
        var a = cc[ss];
        if (a[query.aggregateId]) {
          if (revMax === -1) {
            res = res.concat(a[query.aggregateId].slice(revMin));
          }
          else {
            res = res.concat(a[query.aggregateId].slice(revMin, revMax));
          }
        }
      }
      return callback(null, _.cloneDeep(res));
    }

    if (!query.context && !query.aggregate) {
      for (var sc in this.store) {
        var cont = this.store[sc];
        for (var sa in cont) {
          var agg = cont[sa];
          if (agg[query.aggregateId]) {
            if (revMax === -1) {
              res = res.concat(agg[query.aggregateId].slice(revMin));
            }
            else {
              res = res.concat(agg[query.aggregateId].slice(revMin, revMax));
            }
          }
        }
      }
      return callback(null, _.cloneDeep(res));
    }
  },

  getLastEvent: function (query, callback) {
    if (!query.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var res = [];
    for (var s in this.store) {
      for (var ss in this.store[s]) {
        for (var sss in this.store[s][ss]) {
          res = res.concat(this.store[s][ss][sss]);
        }
      }
    }

    res = _.sortBy(res, function (e) {
      return e.commitStamp.getTime();
    });

    if (!_.isEmpty(query)) {
      res = _.filter(res, function(e) {
        var keys = _.keys(query);
        var values = _.values(query);
        var found = false;
        for (var i in keys) {
          var key = keys[i];
          var deepFound = deepFind(e, key);
          if (_.isArray(deepFound) && deepFound.length > 0) {
            found = true;
          } else if (deepFound === values[i]) {
            found = true;
          } else {
            found = false;
            break;
          }
        }
        return found;
      });
    }

    callback(null, res[res.length - 1]);
  },

  getUndispatchedEvents: function (query, callback) {
    var res = [];
    for (var s in this.undispatchedEvents) {
      if (s === '_direct') continue;
      for (var ss in this.undispatchedEvents[s]) {
        for (var sss in this.undispatchedEvents[s][ss]) {
          res = res.concat(this.undispatchedEvents[s][ss][sss]);
        }
      }
    }

    res = _.sortBy(res, function (e) {
      return e.commitStamp.getTime();
    });

    if (!_.isEmpty(query)) {
      res = _.filter(res, function(e) {
        var keys = _.keys(query);
        var values = _.values(query);
        var found = false;
        for (var i in keys) {
          var key = keys[i];
          var deepFound = deepFind(e, key);
          if (_.isArray(deepFound) && deepFound.length > 0) {
            found = true;
          } else if (deepFound === values[i]) {
            found = true;
          } else {
            found = false;
            break;
          }
        }
        return found;
      });
    }

    callback(null, res);
  },

  setEventToDispatched: function (id, callback) {
    var evt = this.undispatchedEvents._direct[id];
    var aggregateId = evt.aggregateId;
    var aggregate = evt.aggregate || '_general';
    var context = evt.context || '_general';

    this.undispatchedEvents[context][aggregate][aggregateId] = _.reject(this.undispatchedEvents[context][aggregate][aggregateId], evt);
    delete this.undispatchedEvents._direct[id];
    callback(null);
  },

  addSnapshot: function(snap, callback) {
    var aggregateId = snap.aggregateId;
    var aggregate = snap.aggregate || '_general';
    var context = snap.context || '_general';

    if (!snap.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    this.snapshots[context] = this.snapshots[context] || {};
    this.snapshots[context][aggregate] = this.snapshots[context][aggregate] || {};
    this.snapshots[context][aggregate][aggregateId] = this.snapshots[context][aggregate][aggregateId] || [];

    this.snapshots[context][aggregate][aggregateId].push(snap);
    callback(null);
  },

  getSnapshot: function (query, revMax, callback) {

    if (!query.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var all = [];
    for (var s in this.snapshots) {
      for (var ss in this.snapshots[s]) {
        for (var sss in this.snapshots[s][ss]) {
          all = all.concat(this.snapshots[s][ss][sss]);
        }
      }
    }

//    all = _.sortBy(all, function (s) {
//      return [(-s.revision), (-s.version)].join('_');
//    });

    all = _.sortBy(all, function (s) {
      return (-s.commitStamp.getTime());
    });

    if (!_.isEmpty(query)) {
      all = _.filter(all, function(a) {
        var keys = _.keys(query);
        var values = _.values(query);
        var found = false;
        for (var i in keys) {
          var key = keys[i];
          var deepFound = deepFind(a, key);
          if (_.isArray(deepFound) && deepFound.length > 0) {
            found = true;
          } else if (deepFound === values[i]) {
            found = true;
          } else {
            found = false;
            break;
          }
        }
        return found;
      });
    }

    if (revMax === -1) {
      return callback(null, all[0] ? jsondate.parse(JSON.stringify(all[0])) : null);
    }
    else {
      for (var i = all.length - 1; i >= 0; i--) {
        if (all[i].revision <= revMax) {
          return callback(null, jsondate.parse(JSON.stringify(all[i])));
        }
      }
    }
    callback(null, null);
  },

  cleanSnapshots: function(query, callback) {
    var aggregateId = query.aggregateId;
    var aggregate = query.aggregate || '_general';
    var context = query.context || '_general';

    if (!aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var snapshots = this.snapshots[context][aggregate][aggregateId] || [];
    var length = snapshots.length;
    snapshots = snapshots.slice(-1 * this.options.maxSnapshotsCount);
    this.snapshots[context][aggregate][aggregateId] = snapshots;

    callback(null, length - snapshots.length);
  }

});

module.exports = InMemory;
```

## File: `lib/databases/mongodb.js`
```javascript
var util = require('util'),
  Store = require('../base'),
  _ = require('lodash'),
  async = require('async'),
  stream = require('stream'),
  mongo = Store.use('mongodb'),
  mongoVersion = Store.use('mongodb/package.json').version,
  isNew = mongoVersion.indexOf('1.') !== 0,
  ObjectID = isNew ? mongo.ObjectID : mongo.BSONPure.ObjectID,
  debug = require('debug')('eventstore:store:mongodb');

function streamEventsByRevision(self, findStatement, revMin, revMax, resultStream, lastEvent) {

  findStatement.streamRevision = (revMax === -1) ? { '$gte': revMin } : { '$gte': revMin, '$lt': revMax };

  var mongoStream = self.events.find(findStatement, { sort: [['commitStamp', 'asc'], ['streamRevision', 'asc'], ['commitSequence', 'asc']] });

  async.during(function(clb) {
    mongoStream.hasNext(clb);
  },
  function(clb) {
      mongoStream.next(function(error, e) {
      if (error)
        return clb(error);

      if (!lastEvent) {
        lastEvent = e;
        return resultStream.write(lastEvent, clb); // Should write the event to resultStream as if there's no lastEvent when there's an event in stream, the event must be first entry of this query.
      }

      // if for some reason we have written this event alredy
      if ((e.streamRevision === lastEvent.streamRevision && e.restInCommitStream <= lastEvent.restInCommitStream) ||
          (e.streamRevision <= lastEvent.streamRevision)) {
          return clb();
      }

      lastEvent = e;
      resultStream.write(lastEvent, clb);
    });
  },
  function (error) {
    if (error) {
      return resultStream.destroy(error);
    }

    if (!lastEvent) {
      return resultStream.end();
    }

    var txOk = (revMax === -1 && !lastEvent.restInCommitStream) ||
                (revMax !== -1 && (lastEvent.streamRevision === revMax - 1 || !lastEvent.restInCommitStream));

    if (txOk) {
      // the following is usually unnecessary
      self.removeTransactions(lastEvent);
      resultStream.end(); // lastEvent was keep duplicated from this line. We should not re-write last event into the stream when ending it. thus end() rather then end(lastEvent).
    }

    self.repairFailedTransaction(lastEvent, function (err) {
      if (err) {
        if (err.message.indexOf('missing tx entry') >= 0) {
          return resultStream.end(lastEvent); // Maybe we should check on this line too?
        }
        debug(err);
        return resultStream.destroy(error);
      }

      streamEventsByRevision(self, findStatement, lastEvent.revMin, revMax, resultStream, lastEvent);
    });
  });
};
  
function Mongo(options) {
  options = options || {};

  Store.call(this, options);

  var defaults = {
    host: 'localhost',
    port: 27017,
    dbName: 'eventstore',
    eventsCollectionName: 'events',
    snapshotsCollectionName: 'snapshots',
    transactionsCollectionName: 'transactions'//,
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
    var ensureIndex = 'ensureIndex';

    if (mongo.MongoClient.length === 2) {
      ensureIndex = 'createIndex';
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


      function finish (err) {
        if (err) {
          debug(err);
          if (callback) callback(err);
          return;
        }

        self.events = self.db.collection(options.eventsCollectionName);
        self.events[ensureIndex]({ aggregateId: 1, streamRevision: 1 },
          function (err) { if (err) { debug(err); } });
        self.events[ensureIndex]({ commitStamp: 1 },
          function (err) { if (err) { debug(err); } });
        self.events[ensureIndex]({ dispatched: 1 }, { sparse: true },
          function (err) { if (err) { debug(err); } });
        self.events[ensureIndex]({ commitStamp: 1, streamRevision: 1, commitSequence: 1 },
          function (err) { if (err) { debug(err); } });
  
        self.snapshots = self.db.collection(options.snapshotsCollectionName);
        self.snapshots[ensureIndex]({ aggregateId: 1, revision: -1 },
          function (err) { if (err) { debug(err); } });

        self.transactions = self.db.collection(options.transactionsCollectionName);
        self.transactions[ensureIndex]({ aggregateId: 1, 'events.streamRevision': 1 },
          function (err) { if (err) { debug(err); } });
        self.events[ensureIndex]({ aggregate: 1, aggregateId: 1, commitStamp: -1, streamRevision: -1, commitSequence: -1 },
          function (err) { if (err) { debug(err); } });

        if (options.positionsCollectionName) {
          self.positions = self.db.collection(options.positionsCollectionName);
          self.positionsCounterId = options.eventsCollectionName;
        }

        self.emit('connect');
        if (self.options.heartbeat) {
          self.startHeartbeat();
        }
        if (callback) callback(null, self);
      }

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

    this.db.close(function (err) {
      if (err) {
        debug(err);
      }
      if (callback) callback(err);
    });
  },

  clear: function (callback) {
    var self = this;
    async.parallel([
      function (callback) {
        self.events.deleteMany({}, callback);
      },
      function (callback) {
        self.snapshots.deleteMany({}, callback);
      },
      function (callback) {
        self.transactions.deleteMany({}, callback);
      },
      function (callback) {
        if (!self.positions)
          return callback(null);
        self.positions.deleteMany({}, callback);
      }
    ], function (err) {
      if (err) {
        debug(err);
      }
      if (callback) callback(err);
    });
  },

  getNewId: function(callback) {
    callback(null, new ObjectID().toString());
  },

  getNextPositions: function(positions, callback) {
    if (!this.positions)
      return callback(null);

    this.positions.findOneAndUpdate({ _id: this.positionsCounterId }, { $inc: { position: positions } }, { returnOriginal: false, upsert: true }, function (err, pos) {
      if (err)
        return callback(err);

      pos.value.position += 1;

      callback(null, _.range(pos.value.position - positions, pos.value.position));
    });
  },

  addEvents: function (events, callback) {
    if (events.length === 0) {
      if (callback) { callback(null); }
      return;
    }

    var commitId = events[0].commitId;

    var noAggregateId = false,
      invalidCommitId = false;

    var self = this;
    // this.getNextPositions(events.length, function(err, positions) {
      /*
      if (err) {
        debug(err);
        if (callback) callback(err);
        return;
      }
      */

      _.forEach(events, function (evt, index) {
        if (!evt.aggregateId) {
          noAggregateId = true;
        }

        if (!evt.commitId || evt.commitId !== commitId) {
          invalidCommitId = true;
        }

        evt._id = evt.id;
        evt.dispatched = false;
      });

      if (noAggregateId) {
        var errMsg = 'aggregateId not defined!';
        debug(errMsg);
        if (callback) callback(new Error(errMsg));
        return;
      }

      if (invalidCommitId) {
        var errMsg = 'commitId not defined or different!';
        debug(errMsg);
        if (callback) callback(new Error(errMsg));
        return;
      }

      if (events.length === 1) {
        return self.events.insertOne(events[0], callback);
      }

      var tx = {
        _id: commitId,
        events: events,
        aggregateId: events[0].aggregateId,
        aggregate: events[0].aggregate,
        context: events[0].context
      };

      self.transactions.insertOne(tx, function (err) {
        if (err) {
          debug(err);
          if (callback) callback(err);
          return;
        }

        self.events.insertMany(events, function (err) {
          if (err) {
            debug(err);
            if (callback) callback(err);
            return;
          }

          self.removeTransactions(events[events.length - 1], callback);
        });
      });
    // });
  },

  // streaming API
  streamEvents: function (query, skip, limit) {
    var findStatement = {};

    if (query.aggregate) {
      findStatement.aggregate = query.aggregate;
    }

    if (query.context) {
      findStatement.context = query.context;
    }

    if (query.aggregateId) {
      findStatement.aggregateId = query.aggregateId;
    }

    var query = this.events.find(findStatement, { sort: [['commitStamp', 'asc'], ['streamRevision', 'asc'], ['commitSequence', 'asc']] });

    if (skip) {
      query.skip(skip);
    }
    
    if (limit && limit > 0) {
      query.limit(limit);
    }

    return query;
  },

  streamEventsSince: function (date, skip, limit) {
    var findStatement = { commitStamp: { '$gte': date } };

    var query = this.events.find(findStatement, { sort: [['commitStamp', 'asc'], ['streamRevision', 'asc'], ['commitSequence', 'asc']] });

    if (skip)
      query.skip(skip);
    
    if (limit && limit > 0)
      query.limit(limit);
    
    return query;
  },

  streamEventsByRevision: function (query, revMin, revMax) {
    if (!query.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var findStatement = {
      aggregateId: query.aggregateId,
    };

    if (query.aggregate) {
      findStatement.aggregate = query.aggregate;
    }

    if (query.context) {
      findStatement.context = query.context;
    }

    var self = this;

    var resultStream = new stream.PassThrough({ objectMode: true, highWaterMark: 1 });
    streamEventsByRevision(self, findStatement, revMin, revMax, resultStream);
    return resultStream;
  },

  getEvents: function (query, skip, limit, callback) {
    this.streamEvents(query, skip, limit).toArray(callback);
  },

  getEventsSince: function (date, skip, limit, callback) {
    this.streamEventsSince(date, skip, limit).toArray(callback);
  },

  getEventsByRevision: function (query, revMin, revMax, callback) {
    if (!query.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var streamRevOptions = { '$gte': revMin, '$lt': revMax };
    if (revMax === -1) {
      streamRevOptions = { '$gte': revMin };
    }

    var findStatement = {
      aggregateId: query.aggregateId,
      streamRevision: streamRevOptions
    };

    if (query.aggregate) {
      findStatement.aggregate = query.aggregate;
    }

    if (query.context) {
      findStatement.context = query.context;
    }

    var self = this;

    this.events.find(findStatement, { sort: [['commitStamp', 'asc'], ['streamRevision', 'asc'], ['commitSequence', 'asc']] }).toArray(function (err, res) {
      if (err) {
        debug(err);
        return callback(err);
      }

      if (!res || res.length === 0) {
        return callback(null, []);
      }

      var lastEvt = res[res.length - 1];

      var txOk = (revMax === -1 && !lastEvt.restInCommitStream) ||
                 (revMax !== -1 && (lastEvt.streamRevision === revMax - 1 || !lastEvt.restInCommitStream));

      if (txOk) {
        // the following is usually unnecessary
        self.removeTransactions(lastEvt);

        return callback(null, res);
      }

      self.repairFailedTransaction(lastEvt, function (err) {
        if (err) {
          if (err.message.indexOf('missing tx entry') >= 0) {
            return callback(null, res);
          }
          debug(err);
          return callback(err);
        }

        self.getEventsByRevision(query, revMin, revMax, callback);
      });
    });
  },

  getUndispatchedEvents: function (query, callback) {
    var findStatement = {
      dispatched: false
    };

    if (query && query.aggregate) {
      findStatement.aggregate = query.aggregate;
    }

    if (query && query.context) {
      findStatement.context = query.context;
    }

    if (query && query.aggregateId) {
      findStatement.aggregateId = query.aggregateId;
    }

    this.events.find(findStatement, { sort: [['commitStamp', 'asc'], ['streamRevision', 'asc'], ['commitSequence', 'asc']] }).toArray(callback);
  },

  setEventToDispatched: function (id, callback) {
    var updateCommand = { '$unset' : { 'dispatched': null } };
    this.events.updateOne({'_id' : id}, updateCommand, callback);
  },

  addSnapshot: function(snap, callback) {
    if (!snap.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    snap._id = snap.id;
    this.snapshots.insertOne(snap, callback);
  },

  cleanSnapshots: function (query, callback) {
    if (!query.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var findStatement = {
      aggregateId: query.aggregateId
    };

    if (query.aggregate) {
      findStatement.aggregate = query.aggregate;
    }

    if (query.context) {
      findStatement.context = query.context;
    }

    this.snapshots.find(findStatement, {
      sort: [['revision', 'desc'], ['version', 'desc'], ['commitStamp', 'desc']]
    })
      .skip(this.options.maxSnapshotsCount)
      .toArray(removeElements(this.snapshots, callback));
  },

  getSnapshot: function (query, revMax, callback) {
    if (!query.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var findStatement = {
      aggregateId: query.aggregateId
    };

    if (query.aggregate) {
      findStatement.aggregate = query.aggregate;
    }

    if (query.context) {
      findStatement.context = query.context;
    }

    if (revMax > -1) {
      findStatement.revision = { '$lte': revMax };
    }

    this.snapshots.findOne(findStatement, { sort: [['revision', 'desc'], ['version', 'desc'], ['commitStamp', 'desc']] }, callback);
  },

  removeTransactions: function (evt, callback) {
    if (!evt.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var findStatement = { aggregateId: evt.aggregateId };

    if (evt.aggregate) {
      findStatement.aggregate = evt.aggregate;
    }

    if (evt.context) {
      findStatement.context = evt.context;
    }

    // the following is usually unnecessary
    this.transactions.deleteMany(findStatement, function (err) {
      if (err) {
        debug(err);
      }
      if (callback) { callback(err); }
    });
  },

  getPendingTransactions: function (callback) {
    var self = this;
    this.transactions.find({}).toArray(function (err, txs) {
      if (err) {
        debug(err);
        return callback(err);
      }

      if (txs.length === 0) {
        return callback(null, txs);
      }

      var goodTxs = [];

      async.map(txs, function (tx, clb) {
        var findStatement = { commitId: tx._id, aggregateId: tx.aggregateId };

        if (tx.aggregate) {
          findStatement.aggregate = tx.aggregate;
        }

        if (tx.context) {
          findStatement.context = tx.context;
        }

        self.events.findOne(findStatement, function (err, evt) {
          if (err) {
            return clb(err);
          }

          if (evt) {
            goodTxs.push(evt);
            return clb(null);
          }
          
          self.transactions.deleteOne({ _id: tx._id }, clb);
        });
      }, function (err) {
        if (err) {
          debug(err);
          return callback(err);
        }

        callback(null, goodTxs);
      })
    });
  },

  getLastEvent: function (query, callback) {
    if (!query.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var findStatement = { aggregateId: query.aggregateId };

    if (query.aggregate) {
      findStatement.aggregate = query.aggregate;
    }

    if (query.context) {
      findStatement.context = query.context;
    }

    this.events.findOne(findStatement, { sort: [['commitStamp', 'desc'], ['streamRevision', 'desc'], ['commitSequence', 'desc']] }, callback);
  },

  repairFailedTransaction: function (lastEvt, callback) {
    var self = this;

    //var findStatement = {
    //  aggregateId: lastEvt.aggregateId,
    //  'events.streamRevision': lastEvt.streamRevision + 1
    //};
    //
    //if (lastEvt.aggregate) {
    //  findStatement.aggregate = lastEvt.aggregate;
    //}
    //
    //if (lastEvt.context) {
    //  findStatement.context = lastEvt.context;
    //}

    //this.transactions.findOne(findStatement, function (err, tx) {
    this.transactions.findOne({ _id: lastEvt.commitId }, function (err, tx) {
      if (err) {
        debug(err);
        return callback(err);
      }

      if (!tx) {
        var err = new Error('missing tx entry for aggregate ' + lastEvt.aggregateId);
        debug(err);
        return callback(err);
      }

      var missingEvts = tx.events.slice(tx.events.length - lastEvt.restInCommitStream);

      self.events.insertMany(missingEvts, function (err) {
        if (err) {
          debug(err);
          return callback(err);
        }

        self.removeTransactions(lastEvt);

        callback(null);
      });
    });
  }

});

function removeElements(collection, callback) {
  return function (error, elements) {
    if (error) {
      debug(error);
      return callback(error);
    }
    async.each(elements, function (element, callback) {
      try {
        collection.deleteOne({_id: element._id});
        callback();
      } catch (error) {
        callback(error);
      }
    }, function(error) {
      callback(error, elements.length);
    });
  }
}

module.exports = Mongo;
```

## File: `lib/databases/redis.js`
```javascript
var util = require('util'),
  fs = require('fs'),
  Store = require('../base'),
  _ = require('lodash'),
  async = require('async'),
  redis = Store.use('redis'),
  jsondate = require('jsondate'),
  debug = require('debug')('eventstore:store:redis');

function Redis(options) {
  options = options || {};

  Store.call(this, options);

  var defaults = {
    host: 'localhost',
    port: 6379,
    prefix: 'eventstore',
    eventsCollectionName: 'events',
    snapshotsCollectionName: 'snapshots',
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

// helpers
function handleResultSet(err, res, callback) {
  if (err) {
    debug(err);
    return callback(err);
  }

  if (!res || res.length === 0) {
    return callback(null, []);
  }
  var arr = [];

  res.forEach(function (item) {
    arr.push(jsondate.parse(item));
  });

  callback(null, arr);
}

_.extend(Redis.prototype, {

  connect: function (callback) {
    var self = this;

    var options = this.options;

    this.client = new redis.createClient(options.port || options.socket, options.host, _.omit(options, 'prefix'));

    var calledBack = false;

    if (options.password) {
      this.client.auth(options.password, function (err) {
        if (err && !calledBack && callback) {
          calledBack = true;
          if (callback) callback(err, self);
          return;
        }

        if (err) {
          debug(err);
        }
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
      debug(err);

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
          console.error((new Error('Heartbeat timeouted after ' + gracePeriod + 'ms (redis)')).stack);
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

  clear: function (callback) {
    var self = this;
    async.parallel([
      function (callback) {
        self.client.del('nextItemId:' + self.options.prefix, callback);
      },
      function (callback) {
        self.client.keys(self.options.prefix + ':*', function (err, keys) {
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
  },

  getNewId: function (callback) {
    this.client.incr('nextItemId:' + this.options.prefix, function (err, id) {
      if (err) {
        debug(err);
        return callback(err);
      }
      callback(null, id.toString());
    });
  },

  addEvents: function (events, callback) {

    var self = this;

    var aggregateId = events[0].aggregateId;
    var aggregate = events[0].aggregate || '_general';
    var context = events[0].context || '_general';

    var noAggId = events.filter(function (event) {
      return !event.aggregateId
    }).length > 0;

    if (noAggId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    if (!events || events.length === 0) {
      return callback(null);
    }

    function eventKey(event) {
      return event.commitStamp.getTime() + ':' + event.commitSequence.toString() + ':' + context + ':' + aggregate + ':' + aggregateId + ':' + event.id;
    }

    var prefix = self.options.prefix + ':' + self.options.eventsCollectionName;
    var revisionKey = prefix + ':' + context + ':' + aggregate + ':' + aggregateId + ':revision';
    var multi = events.reduce(function (multi) {
      return multi.incr(revisionKey);
    }, this.client.multi());

    multi.exec(function (error, revisions) {
      if (error) {
        debug(error);
        return callback(error);
      }

      var errors = revisions.filter(function (reply) {
        return reply instanceof Error;
      });

      if (errors.length) {
        var message = 'error while adding events for aggregate ' + aggregate + ' ' + aggregateId;
        return callback(new Error(message + '\n' + errors.join('\n')));
      }

      var savedKeysAndEvents = events.map(function(event, index) {
        var key = prefix + ':' + eventKey(event);
        event.streamRevision = parseInt(revisions[index], 10) - 1;
        event.applyMappings();
        return [key, JSON.stringify(event)];
      });

      var undispatchedKeysAndEvents = events.map(function (event) {
        var key = self.options.prefix + ':undispatched_' + self.options.eventsCollectionName + ':' + eventKey(event);
        return [key, JSON.stringify(event)];
      });

      var args = _.flatten(savedKeysAndEvents)
        .concat(_.flatten(undispatchedKeysAndEvents))
        .concat(callback);
      self.client.mset.apply(self.client, args);
    });
  },

  scan: function (key, cursor, handleKeys, callback) {
    var self = this;

    if (!callback) {
      callback = handleKeys;
      handleKeys = cursor;
      cursor = 0;
    }

    (function scanRecursive(curs) {
      self.client.scan(curs, 'match', key, function (err, res) {
        if (err) {
          return callback(err);
        }

        function next() {
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

  getEvents: function (query, skip, limit, callback) {
    var aggregateId = query.aggregateId || '*';
    var aggregate = query.aggregate || '*';
    var context = query.context || '*';

    var self = this;

    var allKeys = [];

    this.scan(this.options.prefix + ':' + this.options.eventsCollectionName + ':*:*:' + context + ':' + aggregate + ':' + aggregateId + ':*',
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

        if (limit === -1) {
          allKeys = allKeys.slice(skip);
        }
        else {
          allKeys = allKeys.slice(skip, skip + limit);
        }

        if (allKeys.length === 0) {
          return callback(null, []);
        }

        var args = allKeys.concat(function (err, res) {
          handleResultSet(err, res, callback);
        });

        self.client.mget.apply(self.client, args);
      }
    );
  },

  getEventsSince: function (date, skip, limit, callback) {
    var self = this;

    var allKeys = [];

    this.scan(this.options.prefix + ':' + this.options.eventsCollectionName + ':*:*:*:*:*:*',
      function (keys, fn) {
        keys = _.filter(keys, function (s) {
          var parts = s.split(':');
          var timePart = parseInt(parts[2], 10);
          return timePart >= date.getTime();
        });

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

        if (limit === -1) {
          allKeys = allKeys.slice(skip);
        }
        else {
          allKeys = allKeys.slice(skip, skip + limit);
        }

        if (allKeys.length === 0) {
          return callback(null, []);
        }

        var args = allKeys.concat(function (err, res) {
          handleResultSet(err, res, callback);
        });

        self.client.mget.apply(self.client, args);
      }
    );
  },

  getEventsByRevision: function (query, revMin, revMax, callback) {
    if (!query.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var aggregateId = query.aggregateId;
    var aggregate = query.aggregate || '*';
    var context = query.context || '*';

    var self = this;

    var allKeys = [];

    this.scan(this.options.prefix + ':' + this.options.eventsCollectionName + ':*:*:' + context + ':' + aggregate + ':' + aggregateId + ':*',
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

        if (revMax === -1) {
          allKeys = allKeys.slice(revMin);
        }
        else {
          allKeys = allKeys.slice(revMin, revMax);
        }

        if (allKeys.length === 0) {
          return callback(null, []);
        }

        var args = allKeys.concat(function (err, res) {
          handleResultSet(err, res, callback);
        });

        self.client.mget.apply(self.client, args);
      }
    );
  },

  getLastEvent: function (query, callback) {
    if (!query.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var aggregateId = query.aggregateId || '*';
    var aggregate = query.aggregate || '*';
    var context = query.context || '*';

    var self = this;

    var allKeys = [];

    this.scan(this.options.prefix + ':' + this.options.eventsCollectionName + ':*:*:' + context + ':' + aggregate + ':' + aggregateId + ':*',
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

        if (allKeys.length === 0) {
          return callback(null, null);
        }

        var args = allKeys.concat(function (err, res) {
          handleResultSet(err, res, function (err, evts) {
            if (err) return callback(err);
            if (evts.length === 0) return callback(null, null);
            callback(null, evts[evts.length - 1])
          });
        });

        self.client.mget.apply(self.client, args);
      }
    );
  },

  getUndispatchedEvents: function (query, callback) {
    var self = this;

    var aggregateId = '*';
    var aggregate = '*';
    var context = '*';

    if (query) {
      aggregateId = query.aggregateId || '*';
      aggregate = query.aggregate || '*';
      context = query.context || '*';
    }

    var evts = [];

    this.scan(this.options.prefix + ':undispatched_' + this.options.eventsCollectionName + ':*:*:' + context + ':' + aggregate + ':' + aggregateId + ':*',
      function (keys, fn) {
        var args = keys.concat(function (err, res) {
          handleResultSet(err, res, function (err, events) {
            if (err) {
              return fn(err);
            }

            evts = evts.concat(events);
            fn();
          });
        });

        self.client.mget.apply(self.client, args);
      }, function (err) {
        if (err) {
          debug(err);
          if (callback) callback(err);
          return;
        }

        evts = _.sortBy(evts, function (s) {
          return s.commitStamp.getTime() + ':' + s.commitSequence.toString();
        });

        callback(null, evts);
      }
    );
  },

  setEventToDispatched: function (id, callback) {
    var self = this;

    this.scan(this.options.prefix + ':undispatched_' + this.options.eventsCollectionName + ':*:*:*:*:*:' + id,
      function (keys, fn) {
        var args = keys.concat(fn);
        self.client.del.apply(self.client, args);
      }, function (err) {
        if (err) {
          debug(err);
          if (callback) callback(err);
          return;
        }

        if (callback) callback(null);
      }
    );
  },

  addSnapshot: function (snap, callback) {
    if (!snap.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var aggregateId = snap.aggregateId;
    var aggregate = snap.aggregate || '_general';
    var context = snap.context || '_general';

    this.client.set(this.options.prefix + ':' + this.options.snapshotsCollectionName + ':' + snap.commitStamp.getTime() + ':' + context + ':' + aggregate + ':' + aggregateId + ':' + snap.id, JSON.stringify(snap), function (err) {
      if (callback) callback(err);
    });
  },

  cleanSnapshots: function (query, callback) {
    var self = this;

    this.scanSnapshots(query, function(error, keys) {
      if (error) {
        debug(error);
        if (callback) callback(error);
        return;
      }

      var keysToDelete = keys
        .sort()
        .slice(0, -1 * self.options.maxSnapshotsCount)

      if (keysToDelete.length === 0) {
        if (callback) callback(null, 0);
        return;
      }

      var delArgs = keysToDelete.concat(callback);

      self.client.del.apply(self.client, delArgs);
    });
  },

  scanSnapshots: function (query, callback) {
    if (!query.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var aggregateId = query.aggregateId;
    var aggregate = query.aggregate || '*';
    var context = query.context || '*';

    var allKeys = [];

    this.scan(this.options.prefix + ':' + this.options.snapshotsCollectionName + ':*:' + context + ':' + aggregate + ':' + aggregateId + ':*',
      function (keys, fn) {
        allKeys = allKeys.concat(keys);
        fn();
      }, function (error) {
        callback(error, allKeys);
      }
    );
  },

  getSnapshot: function (query, revMax, callback) {
    var self = this;

    this.scanSnapshots(query, function (err, allKeys) {
      if (err) {
        debug(err);
        if (callback) callback(err);
        return;
      }

      allKeys = _.sortBy(allKeys, function (s) {
        return s;
      }).reverse();

      if (revMax === -1) { // by default the last snapshot is kept
        allKeys = allKeys.slice(0, 1);
      }

      if (allKeys.length === 0) {
        return callback(null, null);
      }

      // iterating recursively over snapshots, from latest to oldest
      (function nextSnapshot(key) {
        self.client.get(key, function (err, res) {
          if (err) {
            debug(err);
            return callback(err);
          }

          var snapshot = jsondate.parse(res);
          if (revMax > -1 && snapshot.revision > revMax) {
            if (allKeys.length > 0) {
              nextSnapshot(allKeys.shift());
            } else {
              callback(null, null);
            }
          } else {
            callback(null, snapshot);
          }
        });
      })(allKeys.shift());
    })
  }

});

module.exports = Redis;
```

## File: `lib/databases/tingodb.js`
```javascript
var util = require('util'),
  Store = require('../base'),
  _ = require('lodash'),
  async = require('async'),
  tingodb = Store.use('tingodb')(),
  ObjectID = tingodb.ObjectID,
  debug = require('debug')('eventstore:store:tingodb');

function Tingo(options) {
  options = options || {};

  Store.call(this, options);

  var defaults = {
    dbPath: require('path').join(__dirname, '../../'),
    eventsCollectionName: 'events',
    snapshotsCollectionName: 'snapshots',
    transactionsCollectionName: 'transactions'
  };

  _.defaults(options, defaults);

  this.options = options;
}

util.inherits(Tingo, Store);

_.extend(Tingo.prototype, {

  connect: function (callback) {
    var options = this.options;

    this.db = new tingodb.Db(options.dbPath, {});
    // this.db.on('close', function() {
    //   self.emit('disconnect');
    // });
    this.events = this.db.collection(options.eventsCollectionName + '.tingo');
    this.events.ensureIndex({ aggregateId: 1, streamRevision: 1 },
      function (err) { if (err) { debug(err); } });
    this.events.ensureIndex({ commitStamp: 1 },
        function (err) { if (err) { debug(err); } });
    this.events.ensureIndex({ dispatched: 1 }, { sparse: true },
      function (err) { if (err) { debug(err); } });
    this.events.ensureIndex({ commitStamp: 1, streamRevision: 1, commitSequence: 1 },
      function (err) { if (err) { debug(err); } });
    this.events.ensureIndex({ aggregate: 1, aggregateId: 1, commitStamp: -1, streamRevision: -1, commitSequence: -1 },
      function (err) { if (err) { debug(err); } });

    this.snapshots = this.db.collection(options.snapshotsCollectionName + '.tingo');
    this.snapshots.ensureIndex({ aggregateId: 1, revision: -1 },
      function (err) { if (err) { debug(err); } });

    this.transactions = this.db.collection(options.transactionsCollectionName + '.tingo');
    this.transactions.ensureIndex({ aggregateId: 1, 'events.streamRevision': 1 },
      function (err) { if (err) { debug(err); } });

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

  clear: function (callback) {
    var self = this;
    async.parallel([
      function (callback) {
        self.events.remove({}, callback);
      },
      function (callback) {
        self.snapshots.remove({}, callback);
      },
      function (callback) {
        self.transactions.remove({}, callback);
      }
    ], function (err) {
      if (err) {
        debug(err);
      }
      if (callback) callback(err);
    });
  },

  // getNewId: function(callback) {
  //   callback(null, new ObjectID().toString());
  // },

  addEvents: function (events, callback) {
    var noAggId = false;

    _.each(events, function (evt) {
      if (!evt.aggregateId) {
        noAggId = true;
      }

      evt._id = evt.id;
      evt.dispatched = false;
    });

    if (noAggId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var self = this;

    if (events.length === 1) {
      return this.events.insert(events, callback);
    }

    var tx = {
      _id: events[0].commitId,
      events: events,
      aggregateId: events[0].aggregateId,
      aggregate: events[0].aggregate,
      context: events[0].context
    };

    this.transactions.insert(tx, function (err) {
      if (err) {
        debug(err);
        if (callback) callback(err);
        return;
      }

      self.events.insert(events, function (err) {
        if (err) {
          debug(err);
          if (callback) callback(err);
          return;
        }

        self.removeTransactions(events[events.length - 1]);

        if (callback) { callback(null); }
      });
    });
  },

  getEvents: function (query, skip, limit, callback) {
    var findStatement = {};

    if (query.aggregate) {
      findStatement.aggregate = query.aggregate;
    }

    if (query.context) {
      findStatement.context = query.context;
    }

    if (query.aggregateId) {
      findStatement['$or'] = [
        { aggregateId: query.aggregateId },
        { streamId: query.aggregateId } // just for compatability of < 1.0.0
      ];
    }

    if (limit === -1) {
      return this.events.find(findStatement, { sort: [['commitStamp', 'asc'], ['streamRevision', 'asc'], ['commitSequence', 'asc']] }).skip(skip).toArray(callback);
    }

    this.events.find(findStatement, { sort: [['commitStamp', 'asc'], ['streamRevision', 'asc'], ['commitSequence', 'asc']] }).skip(skip).limit(limit).toArray(callback);
  },

  getEventsSince: function (date, skip, limit, callback) {
    var findStatement = { commitStamp: { '$gte': date } };

    if (limit === -1) {
      return this.events.find(findStatement, { sort: [['commitStamp', 'asc'], ['streamRevision', 'asc'], ['commitSequence', 'asc']] }).skip(skip).toArray(callback);
    }

    this.events.find(findStatement, { sort: [['commitStamp', 'asc'], ['streamRevision', 'asc'], ['commitSequence', 'asc']] }).skip(skip).limit(limit).toArray(callback);
  },

  getEventsByRevision: function (query, revMin, revMax, callback) {
    if (!query.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var streamRevOptions = { '$gte': revMin, '$lt': revMax };
    if (revMax == -1) {
      streamRevOptions = { '$gte': revMin };
    }

    var findStatement = {
      '$or': [
        { aggregateId: query.aggregateId },
        { streamId: query.aggregateId } // just for compatability of < 1.0.0
      ],
      streamRevision: streamRevOptions
    };

    if (query.aggregate) {
      findStatement.aggregate = query.aggregate;
    }

    if (query.context) {
      findStatement.context = query.context;
    }

    var self = this;

    this.events.find(findStatement, { sort: [['commitStamp', 'asc'], ['streamRevision', 'asc'], ['commitSequence', 'asc']] }).toArray(function (err, res) {
      if (err) {
        debug(err);
        return callback(err);
      }

      if (!res || res.length === 0) {
        return callback(null, []);
      }

      var lastEvt = res[res.length - 1];

      var txOk = (revMax === -1 && !lastEvt.restInCommitStream) ||
                 (revMax !== -1 && (lastEvt.streamRevision === revMax - 1 || !lastEvt.restInCommitStream));

      if (txOk) {
        // the following is usually unnecessary
        self.removeTransactions(lastEvt);

        return callback(null, res);
      }

      self.repairFailedTransaction(lastEvt, function (err) {
        if (err) {
          if (err.message.indexOf('missing tx entry') >= 0) {
            return callback(null, res);
          }
          debug(err);
          return callback(err);
        }

        self.getEventsByRevision(query, revMin, revMax, callback);
      });
    });
  },

  getUndispatchedEvents: function (query, callback) {
    var findStatement = {
      dispatched: false
    };

    if (query && query.aggregate) {
      findStatement.aggregate = query.aggregate;
    }

    if (query && query.context) {
      findStatement.context = query.context;
    }

    if (query && query.aggregateId) {
      findStatement.aggregateId = query.aggregateId;
    }

    this.events.find(findStatement, { sort: [['commitStamp', 'asc'], ['streamRevision', 'asc'], ['commitSequence', 'asc']] }).toArray(callback);
  },

  setEventToDispatched: function (id, callback) {
    var updateCommand = { '$unset' : { 'dispatched': null } };
    this.events.update({'_id' : id}, updateCommand, callback);
  },

  addSnapshot: function(snap, callback) {
    if (!snap.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    snap._id = snap.id;
    this.snapshots.insert(snap, callback);
  },

  cleanSnapshots: function (query, callback) {
    if (!query.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var findStatement = {
      '$or': [
        { aggregateId: query.aggregateId },
        { streamId: query.aggregateId } // just for compatability of < 1.0.0
      ]
    };

    if (query.aggregate) {
      findStatement.aggregate = query.aggregate;
    }

    if (query.context) {
      findStatement.context = query.context;
    }

    this.snapshots.find(findStatement, {
      sort: [['revision', 'desc'], ['version', 'desc'], ['commitStamp', 'desc']]
    })
      .skip(this.options.maxSnapshotsCount)
      .toArray(removeElements(this.snapshots, callback));
  },

  getSnapshot: function (query, revMax, callback) {
    if (!query.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var findStatement = {
      '$or': [
        { aggregateId: query.aggregateId },
        { streamId: query.aggregateId } // just for compatability of < 1.0.0
      ]
    };

    if (query.aggregate) {
      findStatement.aggregate = query.aggregate;
    }

    if (query.context) {
      findStatement.context = query.context;
    }

    if (revMax > -1) {
      findStatement.revision = { '$lte': revMax };
    }

    this.snapshots.findOne(findStatement, { sort: [['revision', 'desc'], ['version', 'desc'], ['commitStamp', 'desc']] }, callback);
  },

  removeTransactions: function (evt, callback) {
    if (!evt.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var findStatement = { aggregateId: evt.aggregateId };

    if (evt.aggregate) {
      findStatement.aggregate = evt.aggregate;
    }

    if (evt.context) {
      findStatement.context = evt.context;
    }

    // the following is usually unnecessary
    this.transactions.remove(findStatement, function (err) {
      if (err) {
        debug(err);
      }
      if (callback) { callback(err); }
    });
  },

  getPendingTransactions: function (callback) {
    var self = this;
    this.transactions.find({}).toArray(function (err, txs) {
      if (err) {
        debug(err);
        return callback(err);
      }

      if (txs.length === 0) {
        return callback(null, txs);
      }

      var goodTxs = [];

      async.map(txs, function (tx, clb) {
        var findStatement = { commitId: tx._id, aggregateId: tx.aggregateId };

        if (tx.aggregate) {
          findStatement.aggregate = tx.aggregate;
        }

        if (tx.context) {
          findStatement.context = tx.context;
        }

        self.events.findOne(findStatement, function (err, evt) {
          if (err) {
            return clb(err);
          }

          if (evt) {
            goodTxs.push(evt);
          } else {
            self.transactions.remove({ _id: tx._id }, function (err) {
              if (err) {
                debug(err);
              }
            });
          }

          clb(null);
        });
      }, function (err) {
        if (err) {
          debug(err);
          return callback(err);
        }

        callback(null, goodTxs);
      })
    });
  },

  getLastEvent: function (query, callback) {
    if (!query.aggregateId) {
      var errMsg = 'aggregateId not defined!';
      debug(errMsg);
      if (callback) callback(new Error(errMsg));
      return;
    }

    var findStatement = { aggregateId: query.aggregateId };

    if (query.aggregate) {
      findStatement.aggregate = query.aggregate;
    }

    if (query.context) {
      findStatement.context = query.context;
    }

    this.events.findOne(findStatement, { sort: [['commitStamp', 'desc'], ['streamRevision', 'desc'], ['commitSequence', 'desc']] }, callback);
  },

  repairFailedTransaction: function (lastEvt, callback) {
    var self = this;

    //var findStatement = {
    //  aggregateId: lastEvt.aggregateId,
    //  'events.streamRevision': lastEvt.streamRevision + 1
    //};
    //
    //if (lastEvt.aggregate) {
    //  findStatement.aggregate = lastEvt.aggregate;
    //}
    //
    //if (lastEvt.context) {
    //  findStatement.context = lastEvt.context;
    //}

    //this.transactions.findOne(findStatement, function (err, tx) {
    this.transactions.findOne({ _id: lastEvt.commitId }, function (err, tx) {
      if (err) {
        debug(err);
        return callback(err);
      }

      if (!tx) {
        var err = new Error('missing tx entry for aggregate ' + lastEvt.aggregateId);
        debug(err);
        return callback(err);
      }

      var missingEvts = tx.events.slice(tx.events.length - lastEvt.restInCommitStream);

      self.events.insert(missingEvts, function (err) {
        if (err) {
          debug(err);
          return callback(err);
        }

        self.removeTransactions(lastEvt);

        callback(null);
      });
    });
  }

});

function removeElements(collection, callback) {
  return function (error, elements) {
    if (error) {
      debug(error);
      return callback(error);
    }
    async.each(elements, function (element, callback) {
      try {
        collection.remove({_id: element._id});
        callback();
      } catch (error) {
        callback(error);
      }
    }, function(error) {
      callback(error, elements.length);
    });
  }
}

module.exports = Tingo;
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

## File: `test/eventDispatcherTest.js`
```javascript
var expect = require('expect.js'),
  EventDispatcher = require('../lib/eventDispatcher');

describe('EventDispatcher', function () {

  describe('creating an instance', function () {

    describe('without passing a publisher function', function () {
      
      describe('and calling start', function () {

        it('it should callback with an error', function (done) {

          var eventDispatcher = new EventDispatcher();
          eventDispatcher.start(function(err) {
            expect(err).to.be.ok();
            expect(err.message).to.match(/publisher/);
            done();
          });

        });
        
      });

    });

    describe('without passing a store', function () {

      describe('and calling start', function () {

        it('it should callback with an error', function (done) {

          var eventDispatcher = new EventDispatcher(function () {}, { getUndispatchedEvents: function () {} });
          expect(eventDispatcher.undispatchedEventsQueue.length).to.eql(0);
          eventDispatcher.start(function(err) {
            expect(err).to.be.ok();
            expect(err.message).to.match(/store/);
            done();
          });

        });

      });

    });

  });

  describe('starting it', function () {

    describe('while having some undispatched events in the store', function () {

      it('it should publish that events', function (done) {
        
        var eventsInStore = [{
          payload: {
            one: 'event1'
          }
        }, {
          payload: {
            two: 'event2'
          }
        }];

        function getUndispatchedEvents (callback) {
          callback(null, eventsInStore);
        }
        
        var publishedEvents = [];
        
        function publisher (evt) {
          publishedEvents.push(evt);
          check();
        }
        
        function check () {
          if (publishedEvents.length === 2) {
            expect(publishedEvents[0]).to.eql(eventsInStore[0].payload);
            expect(publishedEvents[1]).to.eql(eventsInStore[1].payload);
            done();
          }
        }

        var eventDispatcher = new EventDispatcher(publisher, {
                                    getUndispatchedEvents: getUndispatchedEvents,
                                    setEventToDispatched: function (evt, callback) { callback(null); }});
        expect(eventDispatcher.undispatchedEventsQueue.length).to.eql(0);
        
        eventDispatcher.start(function(err) {
          expect(err).not.to.be.ok();
        });

      });

      it('should not crash when there are lots of pending events', function (done) {
        
        var eventsInStore = [];

        for(var i = 0; i < 10000; i++){
          eventsInStore.push({
            payload: {
              index: i
            }
          });
        }

        function getUndispatchedEvents (callback) {
          callback(null, eventsInStore);
        }
        
        var publishedEvents = [];
        
        function publisher (evt) {
          publishedEvents.push(evt);
          check();
        }
        
        function check () {
          if (publishedEvents.length === eventsInStore.length) {
            done();
          }
        }

        var eventDispatcher = new EventDispatcher(publisher, {
                                    getUndispatchedEvents: getUndispatchedEvents,
                                    setEventToDispatched: function (evt, callback) { callback(null); }});
        expect(eventDispatcher.undispatchedEventsQueue.length).to.eql(0);
        
        eventDispatcher.start(function(err) {
          expect(err).not.to.be.ok();
        });

      });

    });

    describe('and calling addUndispatchedEvents', function () {

      it('it should publish that events', function (done) {

        var eventsInStore = [];

        var eventsToBePublished = [{
          payload: {
            one: 'event1'
          }
        }, {
          payload: {
            two: 'event2'
          }
        }];

        function getUndispatchedEvents (callback) {
          callback(null, eventsInStore);
        }

        var publishedEvents = [];

        function publisher (evt) {
          publishedEvents.push(evt);
          check();
        }

        function check () {
          if (publishedEvents.length === 2) {
            expect(publishedEvents[0]).to.eql(eventsToBePublished[0].payload);
            expect(publishedEvents[1]).to.eql(eventsToBePublished[1].payload);
            done();
          }
        }

        var eventDispatcher = new EventDispatcher(publisher, {
          getUndispatchedEvents: getUndispatchedEvents,
          setEventToDispatched: function (evt, callback) { callback(null); }});
        expect(eventDispatcher.undispatchedEventsQueue.length).to.eql(0);

        eventDispatcher.start(function(err) {
          expect(err).not.to.be.ok();
        });
        
        eventDispatcher.addUndispatchedEvents(eventsToBePublished);

      });

    });

  });

});
```

## File: `test/eventStreamTest.js`
```javascript
var expect = require('expect.js'),
  EventStream = require('../lib/eventStream');

describe('EventStream', function () {

  describe('creating an instance', function () {

    describe('without passing an eventstore', function () {

      it('it should throw an error', function () {

        expect(function() {
          new EventStream({});
        }).to.throwError(/eventstore/);

      });

    });

    describe('without passing a query object', function () {

      it('it should throw an error', function () {

        expect(function() {
          new EventStream({ commit: function(){} });
        }).to.throwError(/query/);

      });

    });

    describe('without passing an aggregateId in the query object', function () {

      it('it should throw an error', function () {

        expect(function() {
          new EventStream({ commit: function(){} }, {});
        }).to.throwError(/query.aggregateId/);

      });

    });

    describe('without passing an aggregateId in the query object', function () {

      it('it should throw an error', function () {

        expect(function() {
          new EventStream({ commit: function(){} }, { aggregateId: 'myAggId' }, [{ streamRevision: 0 }, {}]);
        }).to.throwError(/streamRevision/);

      });

    });

    describe('passing all needed values', function () {

      it('it should return a valid object', function () {

        function commit () {}
        var stream = null;

        expect(function() {
          stream = new EventStream({ commit: commit }, { aggregateId: 'myAggId' });
        }).not.to.throwError();

        expect(stream.eventstore.commit).to.eql(commit);
        expect(stream.aggregateId).to.eql('myAggId');
        expect(stream.streamId).to.eql('myAggId');
        expect(stream.events).to.be.an('array');
        expect(stream.events.length).to.eql(0);
        expect(stream.uncommittedEvents).to.be.an('array');
        expect(stream.uncommittedEvents.length).to.eql(0);
        expect(stream.lastRevision).to.eql(-1);
        expect(stream.eventstore.commit).to.eql(commit);

      });

    });

    describe('passing all values', function () {

      it('it should return a valid object', function () {

        function commit () {}
        var stream = null;

        expect(function() {
          stream = new EventStream({ commit: commit }, { aggregateId: 'myAggId', aggregate: 'myAgg', context: 'myCont' },
                                    [{ one: 'event', streamRevision: 5 }]);
        }).not.to.throwError();

        expect(stream.eventstore.commit).to.eql(commit);
        expect(stream.aggregateId).to.eql('myAggId');
        expect(stream.streamId).to.eql('myAggId');
        expect(stream.aggregate).to.eql('myAgg');
        expect(stream.context).to.eql('myCont');
        expect(stream.events).to.be.an('array');
        expect(stream.events.length).to.eql(1);
        expect(stream.events[0].one).to.eql('event');
        expect(stream.uncommittedEvents).to.be.an('array');
        expect(stream.uncommittedEvents.length).to.eql(0);
        expect(stream.lastRevision).to.eql(5);
        expect(stream.eventstore.commit).to.eql(commit);

      });

    });
    
    describe('with some events', function () {

      function commit () {}
      var evts = [{ one: 'event', streamRevision: 0 }, { one: 'three', streamRevision: 2 }, { one: 'two', streamRevision: 1 }];
      
      it('it should return a valid object', function () {

        var stream = new EventStream({ commit: commit }, { aggregateId: 'myAggId', aggregate: 'myAgg', context: 'myCont' },
          evts);
        
        expect(stream.lastRevision).to.eql(2);
        expect(stream.events).to.be.an('array');
        expect(stream.events.length).to.eql(3);
        expect(stream.events[0]).to.eql(evts[0]);
        expect(stream.events[1]).to.eql(evts[2]);
        expect(stream.events[2]).to.eql(evts[1]);
        
      });
      
      describe('calling currentRevision', function () {
        
        it('it should return the correct revision', function () {

          var stream = new EventStream({ commit: commit }, { aggregateId: 'myAggId', aggregate: 'myAgg', context: 'myCont' },
            evts);

          expect(stream.lastRevision).to.eql(2);
          expect(stream.currentRevision()).to.eql(2);
          expect(stream.lastRevision).to.eql(2);
          
        });
        
      });
      
      describe('calling addEvent', function () {
        
        var stream;
        
        before(function () {
          stream = new EventStream({ commit: commit }, { aggregateId: 'myAggId', aggregate: 'myAgg', context: 'myCont' },
            evts);
        });
        
        it('it should add the passed event to the uncommitted event array', function () {

          stream.addEvent({ 'new': 'event' });
          
          expect(stream.events.length).to.eql(3);
          expect(stream.uncommittedEvents.length).to.eql(1);
          expect(stream.uncommittedEvents[0].payload['new']).to.eql('event');
          
        });
        
      });

      describe('calling addEvents', function () {

        var stream;

        beforeEach(function () {
          stream = new EventStream({ commit: commit }, { aggregateId: 'myAggId', aggregate: 'myAgg', context: 'myCont' },
            evts);
        });

        it('it should add the passed events to the uncommitted event array', function () {

          stream.addEvents([{ 'new1': 'event1' }, { 'new2': 'event2' }]);

          expect(stream.events.length).to.eql(3);
          expect(stream.uncommittedEvents.length).to.eql(2);
          expect(stream.uncommittedEvents[0].payload['new1']).to.eql('event1');
          expect(stream.uncommittedEvents[1].payload['new2']).to.eql('event2');

        });
        
        describe('with a non array', function () {

          it('it should add the passed events to the uncommitted event array', function () {

            expect(function() {
              stream.addEvents({});
            }).to.throwError(/array/);

          });
          
        });

      });
      
      describe('calling commit', function () {

        var commitCalledArg;
        function commitCheck (str, clb) {
          commitCalledArg = str;
          clb(null);
        }
        var stream;

        beforeEach(function () {
          commitCalledArg = null;
          stream = new EventStream({ commit: commitCheck }, { aggregateId: 'myAggId', aggregate: 'myAgg', context: 'myCont' },
            evts);
        });

        it('it should add the passed events to the uncommitted event array', function (done) {

          stream.addEvents([{ 'new1': 'event1' }, { 'new2': 'event2' }]);

          stream.commit(function(err) {
            expect(err).not.to.be.ok();
            expect(commitCalledArg).to.eql(stream);
            
            done();
          })

        });
        
      });
      
    });

  });

});
```

## File: `test/eventTest.js`
```javascript
var expect = require('expect.js'),
  Event = require('../lib/event');

describe('Event', function () {
  
  describe('creating an instance', function () {
    
    describe('without passing an eventstream', function () {
      
      it('it should throw an error', function () {
        
        expect(function() {
          new Event();
        }).to.throwError(/eventstream/);
        
      });
      
    });

    describe('without passing an event', function () {

      it('it should throw an error', function () {

        expect(function() {
          new Event({});
        }).to.throwError(/event/);

      });

    });

    describe('without passing an aggregateId in the eventstream', function () {

      it('it should throw an error', function () {

        expect(function() {
          new Event({}, {});
        }).to.throwError(/eventstream.aggregateId/);

      });

    });

    describe('without passing in the eventstream with its uncommittedEvents property', function () {

      it('it should throw an error', function () {

        expect(function() {
          new Event({ aggregateId: 'myAggId' }, {});
        }).to.throwError(/eventstream.uncommittedEvents/);

      });

    });
    
    describe('passing all needed values', function () {
      
      it('it should return a valid object', function () {

        var uncommitedEvents = [];
        var evt = null;
        
        expect(function() {
          evt = new Event({ aggregateId: 'myAggId', uncommittedEvents: uncommitedEvents }, { data: 'event'});
        }).not.to.throwError();

        expect(evt.aggregateId).to.eql('myAggId');
        expect(evt.streamId).to.eql('myAggId');
        expect(evt.payload.data).to.eql('event');
        expect(uncommitedEvents.length).to.eql(1);
        expect(uncommitedEvents[0]).to.eql(evt);
        
      });
      
    });

    describe('passing all values', function () {

      it('it should return a valid object', function () {

        var uncommitedEvents = [];
        var evt = null;
        
        expect(function() {
          evt = new Event({ aggregateId: 'myAggId', uncommittedEvents: uncommitedEvents, aggregate: 'myAgg', context: 'myCont' }, { data: 'event'});
        }).not.to.throwError();

        expect(evt.aggregateId).to.eql('myAggId');
        expect(evt.streamId).to.eql('myAggId');
        expect(evt.payload.data).to.eql('event');
        expect(evt.aggregate).to.eql('myAgg');
        expect(evt.context).to.eql('myCont');
        expect(uncommitedEvents.length).to.eql(1);
        expect(uncommitedEvents[0]).to.eql(evt);

      });

    });
    
  });
  
});
```

## File: `test/eventstoreTest.js`
```javascript
var expect = require('expect.js'),
  eventstore = require('../'),
  InMemory = require('../lib/databases/inmemory'),
  Base = require('../lib/base'),
  crypto = require('crypto');

describe('eventstore', function () {

  it('it should be a function', function () {

    expect(eventstore).to.be.a('function');

  });

  it('it should exposed the Base for the Store implementation', function () {

    expect(eventstore.Store).to.eql(Base);

  });

  describe('calling that function', function() {

    describe('without options', function () {

      it('it should return as expected', function () {

        var es = eventstore();
        expect(es).to.be.a('object');
        expect(es.useEventPublisher).to.be.a('function');
        expect(es.init).to.be.a('function');
        expect(es.streamEvents).to.be.a('function');
        expect(es.streamEventsSince).to.be.a('function');
        expect(es.streamEventsByRevision).to.be.a('function');
        expect(es.getEvents).to.be.a('function');
        expect(es.getEventsSince).to.be.a('function');
        expect(es.getEventsByRevision).to.be.a('function');
        expect(es.getEventStream).to.be.a('function');
        expect(es.getFromSnapshot).to.be.a('function');
        expect(es.createSnapshot).to.be.a('function');
        expect(es.commit).to.be.a('function');
        expect(es.getUndispatchedEvents).to.be.a('function');
        expect(es.setEventToDispatched).to.be.a('function');
        expect(es.getNewId).to.be.a('function');

        expect(es.store).to.be.a(InMemory);

      });

    });

    describe('with options of a non existing db implementation', function () {

      it('it should throw an error', function () {

        expect(function () {
          eventstore({ type: 'strangeDb' });
        }).to.throwError();

      });

    });

    describe('with options of an own db implementation', function () {

      it('it should return with the an instance of that implementation', function () {

        var es = eventstore({ type: InMemory });
        expect(es).to.be.a('object');
        expect(es.useEventPublisher).to.be.a('function');
        expect(es.init).to.be.a('function');
        expect(es.streamEvents).to.be.a('function');
        expect(es.getEvents).to.be.a('function');
        expect(es.getEventsByRevision).to.be.a('function');
        expect(es.getEventStream).to.be.a('function');
        expect(es.getFromSnapshot).to.be.a('function');
        expect(es.createSnapshot).to.be.a('function');
        expect(es.commit).to.be.a('function');
        expect(es.getUndispatchedEvents).to.be.a('function');
        expect(es.setEventToDispatched).to.be.a('function');
        expect(es.getNewId).to.be.a('function');

        expect(es.store).to.be.a(InMemory);

      });

    });

    describe('and checking the api function by calling', function () {

      describe('getEvents', function () {

        var es = eventstore(),
          orgFunc = es.store.getEvents;

        before(function (done) {
          es.init(done);
        });

        after(function () {
          es.store.getEvents = orgFunc;
        });

        describe('with nice arguments', function () {

          it('it should pass them correctly', function (done) {

            var given = {
              query: { aggregateId: 'myAggId', aggregate: 'myAgg', context: 'myCont' },
              skip: 2,
              limit: 32,
              callback: function () {}
            };

            es.store.getEvents = function (query, skip, limit, callback) {
              expect(query).to.eql(given.query);
              expect(skip).to.eql(given.skip);
              expect(limit).to.eql(given.limit);
              expect(callback).to.be.a('function');

              done();
            };

            es.getEvents(given.query, given.skip, given.limit, given.callback);

          });

        });

        describe('with only the callback', function () {

          it('it should pass them correctly', function (done) {

            var given = {
              callback: function () {}
            };

            es.store.getEvents = function (query, skip, limit, callback) {
              expect(query).to.be.an('object');
              expect(query).to.empty();
              expect(skip).to.eql(0);
              expect(limit).to.eql(-1);
              expect(callback).to.be.a('function');

              done();
            };

            es.getEvents(given.callback);

          });

        });

        describe('with query and callback', function () {

          it('it should pass them correctly', function (done) {

            var given = {
              query: { aggregateId: 'myAggId', aggregate: 'myAgg', context: 'myCont' },
              callback: function () {}
            };

            es.store.getEvents = function (query, skip, limit, callback) {
              expect(query).to.eql(given.query);
              expect(skip).to.eql(0);
              expect(limit).to.eql(-1);
              expect(callback).to.be.a('function');

              done();
            };

            es.getEvents(given.query, given.callback);

          });

        });

        describe('with skip and callback', function () {

          it('it should pass them correctly', function (done) {

            var given = {
              skip: 3,
              callback: function () {}
            };

            es.store.getEvents = function (query, skip, limit, callback) {
              expect(query).to.be.an('object');
              expect(query).to.empty();
              expect(skip).to.eql(given.skip);
              expect(limit).to.eql(-1);
              expect(callback).to.be.a('function');

              done();
            };

            es.getEvents(given.skip, given.callback);

          });

        });

        describe('with query, skip and callback', function () {

          it('it should pass them correctly', function (done) {

            var given = {
              query: { aggregateId: 'myAggId', aggregate: 'myAgg', context: 'myCont' },
              skip: 3,
              callback: function () {}
            };

            es.store.getEvents = function (query, skip, limit, callback) {
              expect(query).to.eql(given.query);
              expect(skip).to.eql(given.skip);
              expect(limit).to.eql(-1);
              expect(callback).to.be.a('function');

              done();
            };

            es.getEvents(given.query, given.skip, given.callback);

          });

        });

        describe('with skip, limit and callback', function () {

          it('it should pass them correctly', function (done) {

            var given = {
              skip: 3,
              limit: 50,
              callback: function () {}
            };

            es.store.getEvents = function (query, skip, limit, callback) {
              expect(query).to.be.an('object');
              expect(query).to.empty();
              expect(skip).to.eql(given.skip);
              expect(limit).to.eql(given.limit);
              expect(callback).to.be.a('function');

              done();
            };

            es.getEvents(given.skip, given.limit, given.callback);

          });

        });

        describe('with query as string,  skip, limit and callback', function () {

          it('it should pass them correctly', function (done) {

            var given = {
              query: 'myAggId',
              skip: 3,
              limit: 50,
              callback: function () {}
            };

            es.store.getEvents = function (query, skip, limit, callback) {
              expect(query).to.be.an('object');
              expect(query.aggregateId).to.eql('myAggId');
              expect(skip).to.eql(given.skip);
              expect(limit).to.eql(given.limit);
              expect(callback).to.be.a('function');

              done();
            };

            es.getEvents(given.query, given.skip, given.limit, given.callback);

          });

        });

      });

      describe('getEventsByRevision', function () {

        var es = eventstore(),
          orgFunc = es.store.getEventsByRevision;

        before(function (done) {
          es.init(done);
        });

        after(function () {
          es.store.getEventsByRevision = orgFunc;
        });

        describe('with nice arguments', function () {

          it('it should pass them correctly', function (done) {

            var given = {
              query: { aggregateId: 'myAggId', aggregate: 'myAgg', context: 'myCont' },
              revMin: 2,
              revMax: 32,
              callback: function () {}
            };

            es.store.getEventsByRevision = function (query, revMin, revMax, callback) {
              expect(query).to.eql(given.query);
              expect(revMin).to.eql(given.revMin);
              expect(revMax).to.eql(given.revMax);
              expect(callback).to.be.a('function');

              done();
            };

            es.getEventsByRevision(given.query, given.revMin, given.revMax, given.callback);

          });

        });

        describe('with query and callback', function () {

          it('it should pass them correctly', function (done) {

            var given = {
              query: { aggregateId: 'myAggId', aggregate: 'myAgg', context: 'myCont' },
              callback: function () {}
            };

            es.store.getEventsByRevision = function (query, revMin, revMax, callback) {
              expect(query).to.eql(given.query);
              expect(revMin).to.eql(0);
              expect(revMax).to.eql(-1);
              expect(callback).to.be.a('function');

              done();
            };

            es.getEventsByRevision(given.query, given.callback);

          });

        });

        describe('with query, revMin and callback', function () {

          it('it should pass them correctly', function (done) {

            var given = {
              query: { aggregateId: 'myAggId', aggregate: 'myAgg', context: 'myCont' },
              revMin: 2,
              callback: function () {}
            };

            es.store.getEventsByRevision = function (query, revMin, revMax, callback) {
              expect(query).to.eql(given.query);
              expect(revMin).to.eql(given.revMin);
              expect(revMax).to.eql(-1);
              expect(callback).to.be.a('function');

              done();
            };

            es.getEventsByRevision(given.query, given.revMin, given.callback);

          });

        });

        describe('with query as string, revMin, revMax and callback', function () {

          it('it should pass them correctly', function (done) {

            var given = {
              query: 'myAggId',
              revMin: 2,
              revMax: 4,
              callback: function () {}
            };

            es.store.getEventsByRevision = function (query, revMin, revMax, callback) {
              expect(query).to.be.an('object');
              expect(query.aggregateId).to.eql('myAggId');
              expect(revMin).to.eql(given.revMin);
              expect(revMax).to.eql(given.revMax);
              expect(callback).to.be.a('function');

              done();
            };

            es.getEventsByRevision(given.query, given.revMin, given.revMax, given.callback);

          });

        });

        describe('with wrong query', function () {

          it('it should pass them correctly', function (done) {

            es.getEventsByRevision(123, 3, 100, function (err) {
              expect(err.message).to.match(/aggregateId/);
              done();
            });

          });

        });

      });

      describe('getEventStream', function () {

        var es = eventstore(),
          orgFunc = es.store.getEventsByRevision;

        before(function (done) {
          es.init(done);
        });

        after(function () {
          es.store.getEventsByRevision = orgFunc;
        });

        describe('with nice arguments', function () {

          it('it should pass them correctly', function (done) {

            var given = {
              query: { aggregateId: 'myAggId', aggregate: 'myAgg', context: 'myCont' },
              revMin: 2,
              revMax: 32,
              callback: function () {}
            };

            es.store.getEventsByRevision = function (query, revMin, revMax, callback) {
              expect(query).to.eql(given.query);
              expect(revMin).to.eql(given.revMin);
              expect(revMax).to.eql(given.revMax);
              expect(callback).to.be.a('function');

              done();
            };

            es.getEventStream(given.query, given.revMin, given.revMax, given.callback);

          });

        });

        describe('with query and callback', function () {

          it('it should pass them correctly', function (done) {

            var given = {
              query: { aggregateId: 'myAggId', aggregate: 'myAgg', context: 'myCont' },
              callback: function () {}
            };

            es.store.getEventsByRevision = function (query, revMin, revMax, callback) {
              expect(query).to.eql(given.query);
              expect(revMin).to.eql(0);
              expect(revMax).to.eql(-1);
              expect(callback).to.be.a('function');

              done();
            };

            es.getEventStream(given.query, given.callback);

          });

        });

        describe('with query, revMin and callback', function () {

          it('it should pass them correctly', function (done) {

            var given = {
              query: { aggregateId: 'myAggId', aggregate: 'myAgg', context: 'myCont' },
              revMin: 2,
              callback: function () {}
            };

            es.store.getEventsByRevision = function (query, revMin, revMax, callback) {
              expect(query).to.eql(given.query);
              expect(revMin).to.eql(given.revMin);
              expect(revMax).to.eql(-1);
              expect(callback).to.be.a('function');

              done();
            };

            es.getEventStream(given.query, given.revMin, given.callback);

          });

        });

        describe('with query as string, revMin, revMax and callback', function () {

          it('it should pass them correctly', function (done) {

            var given = {
              query: 'myAggId',
              revMin: 2,
              revMax: 4,
              callback: function () {}
            };

            es.store.getEventsByRevision = function (query, revMin, revMax, callback) {
              expect(query).to.be.an('object');
              expect(query.aggregateId).to.eql('myAggId');
              expect(revMin).to.eql(given.revMin);
              expect(revMax).to.eql(given.revMax);
              expect(callback).to.be.a('function');

              done();
            };

            es.getEventStream(given.query, given.revMin, given.revMax, given.callback);

          });

        });

        describe('with wrong query', function () {

          it('it should pass them correctly', function (done) {

            es.getEventStream(123, 3, 100, function (err) {
              expect(err.message).to.match(/aggregateId/);
              done();
            });

          });

        });

      });

      describe('getFromSnapshot', function () {

        var es = eventstore(),
          orgFunc = es.store.getSnapshot;

        before(function (done) {
          es.init(done);
        });

        after(function () {
          es.store.getSnapshot = orgFunc;
        });

        describe('with nice arguments', function () {

          it('it should pass them correctly', function (done) {

            var given = {
              query: { aggregateId: 'myAggId', aggregate: 'myAgg', context: 'myCont' },
              revMax: 32,
              callback: function () {
              }
            };

            es.store.getSnapshot = function (query, revMax, callback) {
              expect(query).to.eql(given.query);
              expect(revMax).to.eql(given.revMax);
              expect(callback).to.be.a('function');

              done();
            };

            es.getFromSnapshot(given.query, given.revMax, given.callback);

          });

        });

        describe('with query and callback', function () {

          it('it should pass them correctly', function (done) {

            var given = {
              query: { aggregateId: 'myAggId', aggregate: 'myAgg', context: 'myCont' },
              callback: function () {
              }
            };

            es.store.getSnapshot = function (query, revMax, callback) {
              expect(query).to.eql(given.query);
              expect(revMax).to.eql(-1);
              expect(callback).to.be.a('function');

              done();
            };

            es.getFromSnapshot(given.query, given.callback);

          });

          describe('with query as string, revMax and callback', function () {

            it('it should pass them correctly', function (done) {

              var given = {
                query: 'myAggId',
                revMax: 31,
                callback: function () {
                }
              };

              es.store.getSnapshot = function (query, revMax, callback) {
                expect(query).to.be.an('object');
                expect(query.aggregateId).to.eql('myAggId');
                expect(revMax).to.eql(31);
                expect(callback).to.be.a('function');

                done();
              };

              es.getFromSnapshot(given.query, given.revMax, given.callback);

            });

          });

          describe('with wrong query', function () {

            it('it should pass them correctly', function (done) {

              es.getFromSnapshot(123, 100, function (err) {
                expect(err.message).to.match(/aggregateId/);
                done();
              });

            });

          });

        });

      });

      describe('createSnapshot', function () {

        var es = eventstore(),
          orgFunc = es.store.addSnapshot;

        before(function (done) {
          es.init(done);
        });

        after(function () {
          es.store.addSnapshot = orgFunc;
        });

        describe('with nice arguments', function () {

          it('it should pass them correctly', function (done) {

            var obj = {
              aggregateId: 'myAggId',
              aggregate: 'myAgg',
              context: 'myCont',
              data: { snap: 'data' }
            };

            es.store.addSnapshot = function (snap, callback) {
              expect(snap.aggregateId).to.eql(obj.aggregateId);
              expect(snap.aggregate).to.eql(obj.aggregate);
              expect(snap.context).to.eql(obj.context);
              expect(snap.data).to.eql(obj.data);
              expect(callback).to.be.a('function');

              done();
            };

            es.createSnapshot(obj, function () {});

          });

        });

        describe('with streamId', function () {

          it('it should pass them correctly', function (done) {

            var obj = {
              streamId: 'myAggId',
              data: { snap: 'data' }
            };

            es.store.addSnapshot = function (snap, callback) {
              expect(snap.aggregateId).to.eql(obj.streamId);
              expect(snap.data).to.eql(obj.data);
              expect(callback).to.be.a('function');

              done();
            };

            es.createSnapshot(obj, function () {});

          });

        });

        describe('with wrong aggregateId', function () {

          it('it should pass them correctly', function (done) {

            var obj = {
              data: { snap: 'data' }
            };

            es.createSnapshot(obj, function (err) {
              expect(err.message).to.match(/aggregateId/);
              done();
            });

          });

        });

        describe('with wrong data', function () {

          it('it should pass them correctly', function (done) {

            var obj = {
              aggregateId: 'myAggId',
              aggregate: 'myAgg',
              context: 'myCont'
            };

            es.createSnapshot(obj, function (err) {
              expect(err.message).to.match(/data/);
              done();
            });

          });

        });

      });

      describe('cleanSnapshots', function () {

        var es = eventstore({
            maxSnapshotsCount: 5
          }),
          orgFunc = es.store.cleanSnapshots,
          addSnapshot = es.store.addSnapshot;

        before(function (done) {
          es.store.addSnapshot = function (snap, callback) {
            callback();
          };
          es.init(done);
        });

        after(function () {
          es.store.cleanSnapshots = orgFunc;
          es.store.addSnapshot = addSnapshot;
        });

        describe('with streamId', function () {

          it('it should pass them correctly', function (done) {

            var obj = {
              streamId: 'myAggId',
              aggregate: 'myAgg',
              context: 'myCont',
              data: { snap: 'data' }
            };

            es.store.cleanSnapshots = function (query, callback) {
              expect(query.aggregateId).to.eql(obj.streamId);
              expect(query.aggregate).to.eql(obj.aggregate);
              expect(query.context).to.eql(obj.context);
              expect(callback).to.be.a('function');
              callback();
            };

            es.createSnapshot(obj, done);
          });

        });

        describe('with options not activated', function () {

          before(function () {
            es.options.maxSnapshotsCount = 0;
          });

          it('it should not clean snapshots', function (done) {

            var obj = {
              streamId: 'myAggId',
              aggregate: 'myAgg',
              context: 'myCont',
              data: { snap: 'data' }
            };

            es.store.cleanSnapshots = function (query, callback) {
              callback(new Error('clean snapshots should not have been called'));
            };

            es.createSnapshot(obj, done);
          });

        });
      });

      describe('setEventToDispatched', function () {

        var es = eventstore(),
          orgFunc = es.store.setEventToDispatched;

        before(function (done) {
          es.init(done);
        });

        after(function () {
          es.store.setEventToDispatched = orgFunc;
        });

        describe('with an event', function () {

          it('it should pass it correctly', function (done) {

            var evt = {
              commitId: '1234'
            };

            es.store.setEventToDispatched = function (id, callback) {
              expect(id).to.eql(evt.id);
              expect(callback).to.be.a('function');

              done();
            };

            es.setEventToDispatched(evt, function () {
            });

          });

        });

        describe('with a commitId', function () {

          it('it should pass it correctly', function (done) {

            var evt = {
              commitId: '1234'
            };

            es.store.setEventToDispatched = function (id, callback) {
              expect(id).to.eql(evt.commitId);
              expect(callback).to.be.a('function');

              done();
            };

            es.setEventToDispatched(evt.commitId, function () {});

          });

        });

      });

    });

    describe('with options containing a type property with the value of', function () {

      var types = ['inmemory', 'tingodb', 'mongodb', 'redis'/*, 'elasticsearch', 'azuretable', 'dynamodb'*/];
      var streamingApiTypes = ['mongodb'];
      var positionTypes = ['mongodb', 'inmemory'];

      var token = crypto.randomBytes(16).toString('hex');

      types.forEach(function (type) {

        describe('"' + type + '"', function () {

          var es = null;

          var options = {};

          before(function () {
            if (type === "azuretable" || type === "dynamodb") {
              options = {
                  eventsTableName: 'events' + token,
                  undispatchedEventsTableName: 'undispatchedevents' + token,
                  snapshotsTableName: 'snapshots' + token
              }
            }
            if (type === 'redis') {
              options = {
                db: 3
              };
            }
            options.type = type;
          });

          after(function(done){
            if(type === "dynamodb") {
              // AWS has a limit on the number of DynamoDB tables for an account. Let's clean up when we're done
              var Store = require('../lib/databases/' + type);
              var store = new Store(options);
              store.connect(function(err, s) {
                if(err) return done(err);
                s.removeTables(function(err, result) {
                  done(err);
                });
              });
            } else {
              done(null);
            }
          });

          describe('calling init without callback', function () {

            afterEach(function (done) {
              es.store.disconnect(done);
            });

            beforeEach(function () {
              es = eventstore(options);
            });

            it('it should emit connect', function (done) {

              es.init();
              es.once('connect', done);

            });

          });

          describe('calling init with callback', function () {

            afterEach(function (done) {
              es.store.disconnect(done);
            });

            beforeEach(function () {
              es = eventstore(options);
            });

            it('it should callback successfully', function (done) {

              es.init(function(err) {
                expect(err).not.to.be.ok();
                done();
              });

            });

          });

          describe('having initialized (connected)', function () {

            describe('calling disconnect on store', function () {

              beforeEach(function (done) {
                es = eventstore(options);
                es.init(done);
              });

              it('it should callback successfully', function (done) {

                es.store.disconnect(function (err) {
                  expect(err).not.to.be.ok();
                  done();
                });

              });

              it('it should emit disconnect', function (done) {

                es.once('disconnect', done);
                es.store.disconnect();

              });

            });

            describe('using the eventstore', function () {

              before(function (done) {
                es = eventstore(options);
                es.init(function(err) {
                  es.store.clear(done);
                });
              });

              after(function (done) {
                es.store.clear(done);
              });

              describe('calling getNewId', function () {

                it('it should callback with a new Id as string', function (done) {

                  es.getNewId(function (err, id) {
                    expect(err).not.to.be.ok();
                    expect(id).to.be.a('string');
                    done();
                  });

                });

              });

              describe('requesting a new eventstream', function () {

                describe('and committing some new events', function () {

                  it('it should work as expected', function (done) {

                    es.getEventStream({ aggregateId: 'myAggId', aggregate: 'myAgg', context: 'myCont' }, function (err, stream) {
                      expect(err).not.to.be.ok();

                      expect(stream.lastRevision).to.eql(-1);

                      stream.addEvents([{ one: 'event1' }, { two: 'event2' }, { three: 'event3' }]);

                      expect(stream.streamId).to.eql('myAggId');
                      expect(stream.uncommittedEvents.length).to.eql(3);
                      expect(stream.events.length).to.eql(0);
                      expect(stream.lastRevision).to.eql(-1);

                      stream.commit(function(err, str) {
                        expect(err).not.to.be.ok();
                        expect(str).to.eql(stream);

                        expect(str.uncommittedEvents.length).to.eql(0);
                        expect(str.events.length).to.eql(3);
                        expect(str.lastRevision).to.eql(2);

                        expect(str.events[0].commitSequence).to.eql(0);
                        expect(str.events[1].commitSequence).to.eql(1);
                        expect(str.events[2].commitSequence).to.eql(2);

                        expect(str.events[0].restInCommitStream).to.eql(2);
                        expect(str.events[1].restInCommitStream).to.eql(1);
                        expect(str.events[2].restInCommitStream).to.eql(0);

                        expect(str.eventsToDispatch.length).to.eql(3);

                        done();
                      });

                    });

                  });

                });

              });

              describe('requesting an existing eventstream', function () {

                describe('and committing some new events', function () {

                  before(function(done) {
                    es.getEventStream({ aggregateId: 'myAggId2', aggregate: 'myAgg', context: 'myCont' }, function (err, stream) {
                      expect(err).not.to.be.ok();

                      stream.addEvents([{ one: 'event1' }, { two: 'event2' }, { three: 'event3' }]);
                      stream.commit(done);
                    });
                  });

                  it('it should work as expected', function (done) {

                    es.getEventStream({ aggregateId: 'myAggId2', aggregate: 'myAgg', context: 'myCont' }, function (err, stream) {
                      expect(err).not.to.be.ok();

                      expect(stream.lastRevision).to.eql(2);

                      stream.addEvents([{ for: 'event4' }, { five: 'event5' }]);

                      expect(stream.streamId).to.eql('myAggId2');
                      expect(stream.uncommittedEvents.length).to.eql(2);
                      expect(stream.events.length).to.eql(3);
                      expect(stream.lastRevision).to.eql(2);

                      stream.commit(function(err, str) {
                        expect(err).not.to.be.ok();
                        expect(str).to.eql(stream);

                        expect(str.uncommittedEvents.length).to.eql(0);
                        expect(str.events.length).to.eql(5);
                        expect(str.lastRevision).to.eql(4);

                        expect(str.events[3].commitSequence).to.eql(0);
                        expect(str.events[4].commitSequence).to.eql(1);

                        expect(str.events[3].restInCommitStream).to.eql(1);
                        expect(str.events[4].restInCommitStream).to.eql(0);

                        expect(str.eventsToDispatch.length).to.eql(2);

                        done();
                      });

                    });

                  });

                  it('it should be able to retrieve them', function (done) {

                    es.getEvents({ aggregateId: 'myAggId2', aggregate: 'myAgg', context: 'myCont' }, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(5);

                      done();
                    });

                  });

                  it('it should be able to retrieve by context', function (done) {

                    es.getEvents({context: 'myCont' }, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(8);

                      done();
                    });

                  });

                });

              });

              describe('requesting existing events and using next function', function () {

                describe('and committing some new events', function () {

                  it('it should work as expected', function (done) {

                    es.getEvents({ aggregate: 'myAgg', context: 'myCont' }, 0, 3, function (err, evts) {
                      expect(err).not.to.be.ok();

                      expect(evts.length).to.eql(3);

                      expect(evts.next).to.be.a('function');

                      evts.next(function (err, nextEvts) {
                        expect(err).not.to.be.ok();

                        expect(nextEvts.length).to.eql(3);

                        expect(nextEvts.next).to.be.a('function');

                        nextEvts.next(function (err, nextNextEvts) {
                          expect(err).not.to.be.ok();

                          expect(nextNextEvts.length).to.eql(2);

                          expect(nextNextEvts.next).to.be.a('function');

                          done();
                        });
                      });

                    });

                  });

                });

              });

              describe('requesting all existing events, without query argument and using next function', function () {

                describe('and committing some new events', function () {

                  it('it should work as expected', function (done) {

                    es.getEvents(0, 3, function (err, evts) {
                      expect(err).not.to.be.ok();

                      expect(evts.length).to.eql(3);

                      expect(evts.next).to.be.a('function');

                      evts.next(function (err, nextEvts) {
                        expect(err).not.to.be.ok();

                        expect(nextEvts.length).to.eql(3);

                        expect(nextEvts.next).to.be.a('function');

                        nextEvts.next(function (err, nextNextEvts) {
                          expect(err).not.to.be.ok();

                          expect(nextNextEvts.length).to.eql(2);

                          expect(nextNextEvts.next).to.be.a('function');

                          done();
                        });
                      });

                    });

                  });

                });

              });

              describe('requesting existing events since a date and using next function', function () {

                describe('and committing some new events', function () {

                  it('it should work as expected', function (done) {

                    es.getEventsSince(new Date(2000, 1, 1), 0, 3, function (err, evts) {
                      expect(err).not.to.be.ok();

                      expect(evts.length).to.eql(3);

                      expect(evts.next).to.be.a('function');

                      evts.next(function (err, nextEvts) {
                        expect(err).not.to.be.ok();

                        expect(nextEvts.length).to.eql(3);

                        expect(nextEvts.next).to.be.a('function');

                        nextEvts.next(function (err, nextNextEvts) {
                          expect(err).not.to.be.ok();

                          expect(nextNextEvts.length).to.eql(2);

                          expect(nextNextEvts.next).to.be.a('function');

                          done();
                        });
                      });

                    });

                  });

                });

              });

              describe('requesting all undispatched events', function () {

                it('it should return the correct events', function (done) {

                  es.getUndispatchedEvents(function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(8);

                    done();
                  });

                });

              });

              describe('requesting all undispatched events by streamId', function () {

                it('it should return the correct events', function (done) {

                  es.getUndispatchedEvents('myAggId2', function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(5);

                    done();
                  });

                });

              });

              describe('requesting all undispatched events by query', function () {

                describe('aggregateId', function () {

                  it('it should return the correct events', function (done) {

                    es.getUndispatchedEvents({ aggregateId: 'myAggId' }, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(3);

                      done();
                    });

                  });

                });

                describe('aggregate', function () {

                  it('it should return the correct events', function (done) {

                    es.getUndispatchedEvents({ aggregate: 'myAgg' }, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(8);

                      done();
                    });

                  });

                });

                describe('context', function () {

                  it('it should return the correct events', function (done) {

                    es.getUndispatchedEvents({ context: 'myCont' }, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(8);

                      done();
                    });

                  });

                });

              });

              describe('setting an event to dispatched', function () {

                it('it should work correctly', function (done) {

                  es.getUndispatchedEvents(function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(8);

                    es.setEventToDispatched(evts[0], function (err) {
                      expect(err).not.to.be.ok();

                      es.getUndispatchedEvents(function (err, evts) {
                        expect(err).not.to.be.ok();
                        expect(evts.length).to.eql(7);

                        done();
                      });
                    });

                  });

                });

              });

              describe('creating a snapshot', function () {

                it('it should callback without error', function (done) {

                  es.getEventStream({ aggregateId: 'myAggIdOfSnap', aggregate: 'myAgg', context: 'myCont' }, function (err, stream) {
                    expect(err).not.to.be.ok();

                    expect(stream.lastRevision).to.eql(-1);

                    stream.addEvents([{ oneSnap: 'event1' }, { twoSnap: 'event2' }, { threeSnap: 'event3' }]);

                    expect(stream.streamId).to.eql('myAggIdOfSnap');
                    expect(stream.uncommittedEvents.length).to.eql(3);
                    expect(stream.events.length).to.eql(0);
                    expect(stream.lastRevision).to.eql(-1);

                    stream.commit(function(err, str) {
                      expect(err).not.to.be.ok();
                      expect(str).to.eql(stream);

                      expect(str.uncommittedEvents.length).to.eql(0);
                      expect(str.events.length).to.eql(3);
                      expect(str.lastRevision).to.eql(2);

                      expect(str.events[0].commitSequence).to.eql(0);
                      expect(str.events[1].commitSequence).to.eql(1);
                      expect(str.events[2].commitSequence).to.eql(2);

                      expect(str.events[0].restInCommitStream).to.eql(2);
                      expect(str.events[1].restInCommitStream).to.eql(1);
                      expect(str.events[2].restInCommitStream).to.eql(0);

                      expect(str.eventsToDispatch.length).to.eql(3);

                      es.createSnapshot({
                        aggregateId: stream.aggregateId,
                        aggregate: stream.aggregate,
                        context: stream.context,
                        revision: stream.lastRevision,
                        version: 1,
                        data: { my: 'snap' }
                      }, function (err) {
                        expect(err).not.to.be.ok();

                        stream.addEvent({ fourSnap: 'event4' });

                        stream.commit(function(err, str) {
                          expect(err).not.to.be.ok();
                          expect(str).to.eql(stream);

                          expect(str.uncommittedEvents.length).to.eql(0);
                          expect(str.events.length).to.eql(4);
                          expect(str.lastRevision).to.eql(3);

                          expect(str.eventsToDispatch.length).to.eql(1);

                          done();
                        });

                      });

                    });

                  });

                });

                it('it should callback without error with no additional events', function (done) {

                  es.getEventStream({ aggregateId: 'myAggIdOfSnap2', aggregate: 'myAgg', context: 'myCont' }, function (err, stream) {
                    expect(err).not.to.be.ok();

                    expect(stream.lastRevision).to.eql(-1);

                    stream.addEvents([{ oneSnap: 'event1' }, { twoSnap: 'event2' }, { threeSnap: 'event3' }]);

                    expect(stream.streamId).to.eql('myAggIdOfSnap2');
                    expect(stream.uncommittedEvents.length).to.eql(3);
                    expect(stream.events.length).to.eql(0);
                    expect(stream.lastRevision).to.eql(-1);

                    stream.commit(function(err, str) {
                      expect(err).not.to.be.ok();
                      expect(str).to.eql(stream);

                      expect(str.uncommittedEvents.length).to.eql(0);
                      expect(str.events.length).to.eql(3);
                      expect(str.lastRevision).to.eql(2);

                      expect(str.events[0].commitSequence).to.eql(0);
                      expect(str.events[1].commitSequence).to.eql(1);
                      expect(str.events[2].commitSequence).to.eql(2);

                      expect(str.events[0].restInCommitStream).to.eql(2);
                      expect(str.events[1].restInCommitStream).to.eql(1);
                      expect(str.events[2].restInCommitStream).to.eql(0);

                      expect(str.eventsToDispatch.length).to.eql(3);

                      es.createSnapshot({
                        aggregateId: stream.aggregateId,
                        aggregate: stream.aggregate,
                        context: stream.context,
                        revision: stream.lastRevision,
                        version: 1,
                        data: { my: 'snap' }
                      }, function (err) {
                        expect(err).not.to.be.ok();
                        done();
                      });
                    });

                  });

                });

                describe('and call getFromSnapshot', function () {

                  it('it should retrieve it and the missing events', function (done) {

                    es.getFromSnapshot({ aggregateId: 'myAggIdOfSnap' }, -1, function (err, snap, stream) {
                      expect(err).not.to.be.ok();

                      expect(snap.aggregateId).to.eql('myAggIdOfSnap');
                      expect(snap.revision).to.eql(2);
                      expect(snap.version).to.eql(1);
                      expect(snap.data.my).to.eql('snap');

                      expect(stream.lastRevision).to.eql(3);

                      done();
                    });

                  });

                  it('it should set the lastRevision of an empty event stream to the snapshot revision', function(done) {

                    es.getFromSnapshot({ aggregateId: 'myAggIdOfSnap2' }, -1, function (err, snap, stream) {
                      expect(err).not.to.be.ok();

                      expect(stream.lastRevision).to.eql(snap.revision);

                      done();
                    });

                  });

                });

              });

              if (streamingApiTypes.indexOf(type) !== -1) {
                describe('streaming api', function () {
                  describe('streaming existing events', function () {                
                    describe('and committing some new events', function () {
                      it('it should work as expected', function (done) {

                        var evts = [];
                        var stream = es.streamEvents({ aggregate: 'myAgg', context: 'myCont' }, 0, 3);
                        stream.on('data', function (e) {
                          evts.push(e);
                        });
                        stream.on('end', function(){
                          expect(evts.length).to.eql(3);
                          done();
                        });

                      });

                    });

                  });
                  describe('streaming all existing events, without query argument', function () {
                    describe('and committing some new events', function () {
                      it('it should work as expected', function (done) {

                        var evts = [];
                        var stream =  es.streamEvents(0, 3);
                        stream.on('data', function (e) {
                          evts.push(e);
                        });
                        stream.on('end', function(){
                          expect(evts.length).to.eql(3);
                          done();
                        });

                      });
                    });
                  });
      
                  describe('requesting existing events since a date', function () {
                    describe('and committing some new events', function () {
                      it('it should work as expected', function (done) {
                        var evts = [];
                        var stream =  es.streamEventsSince(new Date(2000, 1, 1), 0, 3);
                        stream.on('data', function (e) {
                          evts.push(e);
                        });
                        stream.on('end', function(){
                          expect(evts.length).to.eql(3);
                          done();
                        });
                      });
                    });
                  });
                  describe('requesting existing events by revision', function () {
                    describe('and committing some new events', function () {
                      it('it should work as expected', function (done) {
                        var evts = [];
                        var stream =  es.streamEventsByRevision('myAggId2', 0, 3);
                        stream.on('data', function (e) {
                          evts.push(e);
                        });
                        stream.on('end', function(){
                          expect(evts.length).to.eql(3);
                          done();
                        });
                      });
                    });
                  });

                });                    
              }

              if (positionTypes.indexOf(type) !== -1) {
                describe('setting event position option', function() {
                  beforeEach(function (done) {
                    es = eventstore({
                      type: type,
                      positionsCollectionName: 'positions',
                      trackPosition: true,
                    });
                    es.defineEventMappings({ position: 'head.position' });
                    es.init(function(err) {
                      es.store.clear(done);
                    });
                  });
    
                  afterEach(function (done) {
                    es.store.clear(done);
                  });

                  it('it should save the event with position', function(done) {
                    es.getEventStream('streamIdWithPosition', function (err, stream) {
                      expect(err).not.to.be.ok();
                      stream.addEvent({ one: 'event' });
                      stream.addEvent({ one: 'event-other' });
          
                      stream.commit(function (err, st) {
                        expect(err).not.to.be.ok();
          
                        expect(st.events.length).to.eql(2);
                        expect(st.events[0].position).to.eql(1);
                        expect(st.events[1].position).to.eql(2);
          
                        done();
                      });
                    });
                  });

                  it('it should map position to payload', function(done) {
                    es.getEventStream('streamIdWithPosition', function (err, stream) {
                      expect(err).not.to.be.ok();
                      stream.addEvent({ one: 'event' });
                      stream.addEvent({ one: 'event-other' });
          
                      stream.commit(function (err, st) {
                        expect(err).not.to.be.ok();
          
                        expect(st.events.length).to.eql(2);
                        expect(st.events[0].payload.head.position).to.eql(1);
                        expect(st.events[1].payload.head.position).to.eql(2);
          
                        done();
                      });
                    });
                  });

                });
              }
            });

          });

        });

      });

    });

    describe('and defining the commitStamp option', function () {

      it('it should save the commitStamp correctly', function (done) {

        var es = eventstore();
        es.defineEventMappings({ commitStamp: 'head.date' });
        es.init(function (err) {
          expect(err).not.to.be.ok();

          es.getEventStream('streamIdWithDate', function (err, stream) {
            stream.addEvent({ one: 'event' });

            stream.commit(function (err, st) {
              expect(err).not.to.be.ok();

              expect(st.events.length).to.eql(1);
              expect(st.events[0].payload.head.date).to.eql(st.events[0].commitStamp);

              done();
            });
          });
        });

      });

    });

    describe('and not defining the commitStamp option', function () {

      it('it should not save the commitStamp', function (done) {

        var es = eventstore({});
        es.init(function (err) {
          expect(err).not.to.be.ok();

          es.getEventStream('streamIdWithoutDate', function (err, stream) {
            stream.addEvent({ one: 'event' });

            stream.commit(function (err, st) {
              expect(err).not.to.be.ok();

              expect(st.events.length).to.eql(1);
              expect(st.events[0].payload.date).not.to.be.ok();
              expect(st.events[0].payload.head).not.to.be.ok();

              done();
            });
          });
        });

      });

    });

    describe('and defining the streamRevision option', function () {

      it('it should save the streamRevision correctly', function (done) {

        var es = eventstore();
        es.defineEventMappings({ streamRevision: 'version' });
        es.init(function (err) {
          expect(err).not.to.be.ok();

          es.getEventStream('streamIdWithDate', function (err, stream) {
            stream.addEvent({ one: 'event' });

            stream.commit(function (err, st) {
              expect(err).not.to.be.ok();

              expect(st.events.length).to.eql(1);
              expect(st.events[0].payload.version).to.eql(st.events[0].streamRevision);

              done();
            });
          });
        });

      });

    });

    describe('and defining a publisher function in a synchronous way', function () {

      it('it should initialize an eventDispatcher', function (done) {

        function publish (evt) {}
        var es = eventstore();
        es.useEventPublisher(publish);
        es.init(function (err) {
          expect(err).not.to.be.ok();
          expect(es.publisher).to.be.ok();
          done();
        });

      });

      describe('when committing a new event', function () {

        it('it should publish a new event', function (done) {

          function publish (evt) {
            expect(evt.one).to.eql('event');
            done();
          }

          var es = eventstore();
          es.useEventPublisher(publish);
          es.init(function (err) {
            expect(err).not.to.be.ok();

            es.getEventStream('streamId', function (err, stream) {
              stream.addEvent({ one: 'event' });

              stream.commit(function (err) {
                expect(err).not.to.be.ok();
              });
            });
          });

        });

      });

    });

    describe('and defining a publisher function in an asynchronous way', function () {

      it('it should initialize an eventDispatcher', function (done) {

        function publish (evt, callback) {callback();}
        var es = eventstore();
        es.useEventPublisher(publish);
        es.init(function (err) {
          expect(err).not.to.be.ok();
          expect(es.publisher).to.be.ok();
          done();
        });

      });

      describe('when committing a new event', function () {

        it('it should publish a new event', function (done) {

          function publish (evt, callback) {
            expect(evt.one).to.eql('event');
            callback();
            done();
          }

          var es = eventstore();
          es.useEventPublisher(publish);
          es.init(function (err) {
            expect(err).not.to.be.ok();

            es.getEventStream('streamId', function (err, stream) {
              stream.addEvent({ one: 'event' });

              stream.commit(function (err) {
                expect(err).not.to.be.ok();
              });
            });
          });

        });

      });

    });

    describe('and not defining a publisher function', function () {

      it('it should not initialize an eventDispatcher', function (done) {

        var es = eventstore();
        es.init(function (err) {
          expect(err).not.to.be.ok();
          expect(es.publisher).not.to.be.ok();
          done();
        });

      });

    });

  });

});
```

## File: `test/mocha.opts`
```
-R spec -t 20000
```

## File: `test/snapshotTest.js`
```javascript
var expect = require('expect.js'),
  Snapshot = require('../lib/snapshot');

describe('Snapshot', function () {

  describe('creating an instance', function () {

    describe('without passing an id', function () {

      it('it should throw an error', function () {

        expect(function() {
          new Snapshot();
        }).to.throwError(/id/);

      });

    });

    describe('without passing an object', function () {

      it('it should throw an error', function () {

        expect(function() {
          new Snapshot('myId', {});
        }).to.throwError(/object/);

      });

    });

    describe('without passing an aggregateId in the object', function () {

      it('it should throw an error', function () {

        expect(function() {
          new Snapshot('myId', {});
        }).to.throwError(/object.aggregateId/);

      });

    });

    describe('without passing a data property in the object', function () {

      it('it should throw an error', function () {

        expect(function() {
          new Snapshot('myId', { aggregateId: 'myAggId' });
        }).to.throwError(/object.data/);

      });

    });

    describe('passing all needed values', function () {

      it('it should return a valid object', function () {

        var snap = null;

        expect(function() {
          snap = new Snapshot('myId', { aggregateId: 'myAggId', data: 'snap'});
        }).not.to.throwError();

        expect(snap.id).to.eql('myId');
        expect(snap.aggregateId).to.eql('myAggId');
        expect(snap.streamId).to.eql('myAggId');
        expect(snap.data).to.eql('snap');

      });

    });

    describe('passing all values', function () {

      it('it should return a valid object', function () {
        
        var snap = null;

        expect(function() {
          snap = new Snapshot('myId', { aggregateId: 'myAggId', aggregate: 'myAgg', context: 'myCont',
                                            data: 'snap', version: 3, revision: 24 });
        }).not.to.throwError();

        expect(snap.id).to.eql('myId');
        expect(snap.aggregateId).to.eql('myAggId');
        expect(snap.streamId).to.eql('myAggId');
        expect(snap.aggregate).to.eql('myAgg');
        expect(snap.context).to.eql('myCont');
        expect(snap.data).to.eql('snap');
        expect(snap.version).to.eql(3);
        expect(snap.revision).to.eql(24);

      });

    });

  });

});
```

## File: `test/storeEventEmitterTest.js`
```javascript
var expect = require('expect.js');
var eventstore = require('../');
var StoreEventEmitter = require('../lib/storeEventEmitter');

function beforeEachMethod(eventName) {
  var self = this;

  self.es.on('before-' + eventName, function (result) {
    self.receivedBeforeResult = result;
    self.receivedBefore = true;
  });

  self.es.on('after-' + eventName, function (result) {
    self.receivedAfter = true;
    self.receivedAfterResult = result;
  });
}

function resetCheckValues() {
  this.receivedBefore = false;
  this.receivedAfter = false;
  this.receivedBeforeResult = undefined;
  this.receivedAfterResult = undefined;
}

function expectEventsEmitted() {
  expect(this.receivedBefore).to.eql(true);
  expect(this.receivedAfter).to.eql(true);
  expect(this.receivedBeforeResult).to.be.a(Object);
  expect(this.receivedAfterResult).to.be.a(Object);
  expect(this.receivedBeforeResult.milliseconds).to.be.a('number');
  expect(this.receivedAfterResult.milliseconds).to.be.a('number');
}

function expectEventsNotEmitted() {
  expect(this.receivedBefore).to.eql(false);
  expect(this.receivedAfter).to.eql(false);
  expect(this.receivedBeforeResult).to.eql(undefined);
  expect(this.receivedAfterResult).to.eql(undefined);
}

describe('StoreEventEmitter', function () {
  describe('create instance', function() {
    it('it should throw an error if instantiated without eventstore', function () {
      expect(function () {
        new StoreEventEmitter();
      }).to.throwError();
    });

    it('it should be instance of StoreEventEmitter', function () {
      var storeEventEmitter = new StoreEventEmitter(eventstore());
      expect(storeEventEmitter).to.be.a(StoreEventEmitter);
    });

    it('addEventEmitter should be a function', function () {
      var storeEventEmitter = new StoreEventEmitter(eventstore());
      expect(storeEventEmitter.addEventEmitter).to.be.a('function');
    });
  });

  describe('emit store events is disabled by default', function() {
    var self = this;

    beforeEach(function () {
      self.es = eventstore();
      resetCheckValues.call(self);
    });

    afterEach(function () {
      self.es.removeAllListeners();
    });
  
    it('it should not emit any events', function(done) {
      self.es.store.addEvents([], function () {
        expectEventsNotEmitted.call(self);
        done();
      });
    });
  });

  describe('calling that method', function () {
    var self = this;

    beforeEach(function () {
      self.es = eventstore({ emitStoreEvents: true });
      resetCheckValues.call(self);
    });

    afterEach(function () {
      self.es.removeAllListeners();
    });

    describe('clear', function () {
      beforeEach(beforeEachMethod.bind(self, 'clear'));

      it('it should emit the correct events', function (done) {
        self.es.store.clear(function () {
          expectEventsEmitted.call(self);
          done();
        });
      });
    });

    describe('getNextPositions', function () {
      beforeEach(beforeEachMethod.bind(self, 'get-next-positions'));

      it('it should emit the correct events', function (done) {
        self.es.store.getNextPositions(4, function () {
          expectEventsEmitted.call(self);
          done();
        });
      });
    });

    describe('addEvents', function () {
      beforeEach(beforeEachMethod.bind(self, 'add-events'));

      it('it should emit the correct events with valid parameters', function (done) {
        self.es.store.addEvents([{ one: 'event1' }], function () {
          expectEventsEmitted.call(self);
          done();
        });
      });

      it('it should emit the correct events with empty events array', function (done) {
        self.es.store.addEvents([], function () {
          expectEventsEmitted.call(self);
          done();
        });
      });
    });

    describe('getEvents', function () {
      beforeEach(beforeEachMethod.bind(self, 'get-events'));

      it('it should emit the correct events with all parameters', function (done) {
        self.es.getEvents({ aggregateId: 'myAggId', aggregate: 'myAgg', context: 'myCont' }, 2, 32, function () {
          expectEventsEmitted.call(self);
          done();
        });
      });

      it('it should emit the correct events with only callback parameter', function (done) {
        self.es.getEvents(function () {
          expectEventsEmitted.call(self);
          done();
        });
      });

      it('it should emit the correct events with callback instead of skip parameter', function (done) {
        self.es.getEvents({ aggregateId: 'myAggId', aggregate: 'myAgg', context: 'myCont' }, function () {
          expectEventsEmitted.call(self);
          done();
        });
      });

      it('it should emit the correct events with callback instead of limit parameter', function (done) {
        self.es.getEvents({ aggregateId: 'myAggId', aggregate: 'myAgg', context: 'myCont' }, 2, function () {
          expectEventsEmitted.call(self);
          done();
        });
      });
    });

    describe('getEventsSince', function () {
      beforeEach(beforeEachMethod.bind(self, 'get-events-since'));

      it('it should emit the correct events with all parameters', function (done) {
        self.es.getEventsSince(new Date(2000, 1, 1), 0, 3, function () {
          expectEventsEmitted.call(self);
          done();
        });
      });

      it('it should emit the correct events with callback instead of skip parameter', function (done) {
        self.es.getEventsSince(new Date(2000, 1, 1), function () {
          expectEventsEmitted.call(self);
          done();
        });
      });

      it('it should emit the correct events with callback instead of limit parameter', function (done) {
        self.es.getEventsSince(new Date(2000, 1, 1), 0, function () {
          expectEventsEmitted.call(self);
          done();
        });
      });
    });

    describe('getEventsByRevision', function () {
      beforeEach(beforeEachMethod.bind(self, 'get-events-by-revision'));

      it('it should emit the correct events with all parameters', function (done) {
        self.es.getEventsByRevision('myQuery', 3, 100, function () {
          expectEventsEmitted.call(self);
          done();
        });
      });

      it('it should emit the correct events with callback instead of revMin parameter', function (done) {
        self.es.getEventsByRevision('myQuery', function () {
          expectEventsEmitted.call(self);
          done();
        });
      });

      it('it should emit the correct events with callback instead of revMax parameter', function (done) {
        self.es.getEventsByRevision('myQuery', 3, function () {
          expectEventsEmitted.call(self);
          done();
        });
      });
    });

    describe('getLastEvent', function () {
      beforeEach(beforeEachMethod.bind(self, 'get-last-event'));

      it('it should emit the correct events with all parameters', function (done) {
        self.es.getLastEvent('myQuery', function () {
          expectEventsEmitted.call(self);
          done();
        });
      });
    });

    describe('getUndispatchedEvents', function () {
      beforeEach(beforeEachMethod.bind(self, 'get-undispatched-events'));

      it('it should emit the correct events with all parameters', function (done) {
        self.es.getUndispatchedEvents('myQuery', function () {
          expectEventsEmitted.call(self);
          done();
        });
      });

      it('it should emit the correct events with only callback parameter', function (done) {
        self.es.getUndispatchedEvents(function () {
          expectEventsEmitted.call(self);
          done();
        });
      });
    });

    describe('setEventToDispatched', function () {
      beforeEach(function () {
        beforeEachMethod.call(self, 'set-event-to-dispatched');

        self.es.store.setEventToDispatched = function (_id, callback) {
          return callback();
        };

        var storeEventEmitter = new StoreEventEmitter(self.es);
        storeEventEmitter.addEventEmitter();
      });

      it('it should emit the correct events with all parameters', function (done) {
        self.es.setEventToDispatched('my-id', function () {
          expectEventsEmitted.call(self);
          done();
        });
      });
    });

    describe('addSnapshot', function () {
      beforeEach(beforeEachMethod.bind(self, 'add-snapshot'));

      it('it should emit the correct events with all parameters', function (done) {
        self.es.store.addSnapshot('myAggId', function () {
          expectEventsEmitted.call(self);
          done();
        });
      });
    });

    describe('cleanSnapshots', function () {
      beforeEach(beforeEachMethod.bind(self, 'clean-snapshots'));

      it('it should emit the correct events with all parameters', function (done) {
        self.es.store.cleanSnapshots('myQuery', function () {
          expectEventsEmitted.call(self);
          done();
        });
      });
    });

    describe('getSnapshot', function () {
      beforeEach(beforeEachMethod.bind(self, 'get-snapshot'));

      it('it should emit the correct events', function (done) {
        self.es.store.getSnapshot('myQuery', 100, function () {
          expectEventsEmitted.call(self);
          done();
        });
      });
    });

    describe('getEventStream', function () {
      beforeEach(beforeEachMethod.bind(self, 'get-event-stream'));

      it('it should emit the correct events with all parameters', function (done) {
        self.es.getEventStream('myQuery', 3, 100, function () {
          expectEventsEmitted.call(self);
          done();
        });
      });

      it('it should emit the correct events with callback instead of revMin parameter', function (done) {
        self.es.getEventStream('myQuery', function () {
          expectEventsEmitted.call(self);
          done();
        });
      });

      it('it should emit the correct events with callback instead of revMax parameter', function (done) {
        self.es.getEventStream('myQuery', 3, function () {
          expectEventsEmitted.call(self);
          done();
        });
      });
    });

    describe('getFromSnapshot', function () {
      beforeEach(beforeEachMethod.bind(self, 'get-from-snapshot'));

      it('it should emit the correct events with all parameters', function (done) {
        self.es.getFromSnapshot('myQuery', 100, function () {
          expectEventsEmitted.call(self);
          done();
        });
      });

      it('it should emit the correct events with callback instead of revMax parameter', function (done) {
        self.es.getFromSnapshot('myQuery', function () {
          expectEventsEmitted.call(self);
          done();
        });
      });
    });

    describe('createSnapshot', function () {
      beforeEach(beforeEachMethod.bind(self, 'create-snapshot'));

      it('it should emit the correct events with all parameters', function (done) {
        self.es.createSnapshot({ aggregateId: 'myAggId' }, function () {
          expectEventsEmitted.call(self);
          done();
        });
      });
    });

    describe('commit', function () {
      beforeEach(function () {
        beforeEachMethod.call(self, 'commit');

        self.es.commit = function (_eventstream, callback) {
          return callback();
        };

        var storeEventEmitter = new StoreEventEmitter(self.es);
        storeEventEmitter.addEventEmitter();
      });

      it('it should emit the correct events with all parameters', function (done) {
        self.es.commit({}, function () {
          expectEventsEmitted.call(self);
          done();
        });
      });
    });

    describe('getLastEventAsStream', function () {
      beforeEach(beforeEachMethod.bind(self, 'get-last-event-as-stream'));

      it('it should emit the correct events with all parameters', function (done) {
        self.es.getLastEventAsStream({ aggregateId: 'myAggId' }, function () {
          expectEventsEmitted.call(self);
          done();
        });
      });
    });
  });
});
```

## File: `test/storeTest.js`
```javascript
var expect = require('expect.js'),
  Base = require('../lib/base'),
  async = require('async'),
  _ = require('lodash'),
  crypto = require('crypto');

var types = ['inmemory', 'tingodb', 'mongodb', 'redis'/*, 'elasticsearch', 'azuretable', 'dynamodb'*/];

var token = crypto.randomBytes(16).toString('hex');

var options = {};

types.forEach(function (type) {

  describe('"' + type + '" store implementation', function () {

    var Store = require('../lib/databases/' + type);
    var store;

    after(function(done) {
      if(type === "dynamodb") {
        store.removeTables(done);
      } else {
        done(null);
      }
    });

    describe('creating an instance', function () {

      before(function () {
        options = {};
        if (type === "azuretable" || type === "dynamodb") {
          options = {
              eventsTableName: 'events' + token,
              undispatchedEventsTableName: 'undispatchedevents' + token,
              snapshotsTableName: 'snapshots' + token
          }
        }
        if (type === 'redis') {
          options = {
            db: 3
          };
        }
        options.maxSnapshotsCount = 5;
        store = new Store(options);
      });

      it('it should return correct object', function () {
        expect(store).to.be.a(Base);
        expect(store.connect).to.be.a('function');
        expect(store.disconnect).to.be.a('function');
        expect(store.getNewId).to.be.a('function');
        expect(store.getEvents).to.be.a('function');
        expect(store.getEventsSince).to.be.a('function');
        expect(store.getEventsByRevision).to.be.a('function');
        expect(store.getSnapshot).to.be.a('function');
        expect(store.addSnapshot).to.be.a('function');
        expect(store.addEvents).to.be.a('function');
        expect(store.getUndispatchedEvents).to.be.a('function');
        expect(store.setEventToDispatched).to.be.a('function');
        expect(store.clear).to.be.a('function');

        if (type === 'mongodb' || type === 'tingodb') {
          expect(store.getPendingTransactions).to.be.a('function');
          expect(store.getLastEvent).to.be.a('function');
          expect(store.repairFailedTransaction).to.be.a('function');
        }
      });

      describe('calling connect', function () {

        afterEach(function (done) {
          store.disconnect(done);
        });

        it('it should callback successfully', function (done) {

          store.connect(function (err) {
            expect(err).not.to.be.ok();
            done();
          });

        });

        it('it should emit connect', function (done) {

          store.once('connect', done);
          store.connect();

        });

      });

      describe('having connected', function () {

        describe('calling disconnect', function () {

          beforeEach(function (done) {
            store.connect(done);
          });

          it('it should callback successfully', function (done) {

            store.disconnect(function (err) {
              expect(err).not.to.be.ok();
              done();
            });

          });

          it('it should emit disconnect', function (done) {

            store.once('disconnect', done);
            store.disconnect();

          });

        });

        describe('using the store', function () {

          before(function (done) {
            store.connect(done);
          });

          beforeEach(function (done) {
            store.clear(done);
          });

          after(function (done) {
            store.clear(done);
          });

          describe('calling getNewId', function () {

            it('it should callback with a new Id as string', function (done) {

              store.getNewId(function (err, id) {
                expect(err).not.to.be.ok();
                expect(id).to.be.a('string');
                done();
              });

            });

          });

          describe('calling addEvents', function () {

            describe('with one event in the array', function () {

              it('it should save the event', function(done) {

                var event = {
                  aggregateId: 'id1',
                  id: '111',
                  streamRevision: 0,
                  commitId: '111',
                  commitStamp: new Date(),
                  commitSequence: 0,
                  payload: {
                    event:'bla'
                  },
                  applyMappings: function () {}
                };

                store.addEvents([event], function(err) {
                  expect(err).not.to.be.ok();

                  store.getEvents({}, 0, -1, function(err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts).to.be.an('array');
                    expect(evts).to.have.length(1);
                    expect(evts[0].commitStamp.getTime()).to.eql(event.commitStamp.getTime());
                    expect(evts[0].aggregateId).to.eql(event.aggregateId);
                    expect(evts[0].commitId).to.eql(event.commitId);
                    expect(evts[0].payload.event).to.eql(event.payload.event);

                    done();
                  });
                });

              });

            });

            describe('with an array in the payload', function () {

              it('it should save the event', function(done) {

                var event = {
                  aggregateId: 'id1',
                  id: '111',
                  streamRevision: 0,
                  commitId: '111',
                  commitStamp: new Date(),
                  commitSequence: 0,
                  payload: {
                    event:'bla',
                    array: []
                  },
                  applyMappings: function () {}
                };

                store.addEvents([event], function(err) {
                  expect(err).not.to.be.ok();

                  store.getEvents({}, 0, -1, function(err, evts) {
                    expect(err).not.to.be.ok();

                    expect(evts[0].payload.array).to.be.an('array');

                    done();
                  });
                });

              });

            });

            describe('with multiple events in the array', function () {

              it('it should save the event', function(done) {

                var event1 = {
                  aggregateId: 'id2',
                  streamRevision: 0,
                  id: '112',
                  commitId: '987',
                  commitStamp: new Date(Date.now() + 1),
                  commitSequence: 0,
                  restInCommitStream: 1,
                  payload: {
                    event:'bla'
                  },
                  applyMappings: function () {}
                };

                var event2 = {
                  aggregateId: 'id2',
                  streamRevision: 1,
                  id:'113',
                  commitId: '987',
                  commitStamp: new Date(Date.now() + 1),
                  commitSequence: 1,
                  restInCommitStream: 0,
                  payload: {
                    event:'bla2'
                  },
                  applyMappings: function () {}
                };

                store.addEvents([event1, event2], function(err) {
                  expect(err).not.to.be.ok();

                  store.getEvents({}, 0, -1, function(err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts).to.be.an('array');
                    expect(evts).to.have.length(2);
                    expect(evts[0].commitStamp.getTime()).to.eql(event1.commitStamp.getTime());
                    expect(evts[0].aggregateId).to.eql(event1.aggregateId);
                    expect(evts[0].commitId).to.eql(event1.commitId);
                    expect(evts[0].payload.event).to.eql(event1.payload.event);
                    expect(evts[1].commitStamp.getTime()).to.eql(event2.commitStamp.getTime());
                    expect(evts[1].aggregateId).to.eql(event2.aggregateId);
                    expect(evts[1].commitId).to.eql(event2.commitId);
                    expect(evts[1].payload.event).to.eql(event2.payload.event);
                    expect(evts[1].streamRevision).to.be.a('number');

                    store.getLastEvent({ aggregateId: event2.aggregateId }, function(err, evt) {
                      expect(err).not.to.be.ok();

                      expect(evt.commitStamp.getTime()).to.eql(event2.commitStamp.getTime());
                      expect(evt.aggregateId).to.eql(event2.aggregateId);
                      expect(evt.commitId).to.eql(event2.commitId);
                      expect(evt.payload.event).to.eql(event2.payload.event);
                      done();
                    });
                  });
                });

              });

              if (type === 'mongodb' || type === 'tingodb') {

                describe('failing to save all events', function () {

                  it('it should successfully handle the transaction', function(done) {

                    var event1 = {
                      aggregateId: 'id2_tx',
                      streamRevision: 0,
                      id: '112_tx',
                      commitId: '987_tx',
                      commitStamp: new Date(Date.now() + 1),
                      commitSequence: 0,
                      restInCommitStream: 1,
                      payload: {
                        event:'bla'
                      }
                    };

                    var event2 = {
                      aggregateId: 'id2_tx',
                      streamRevision: 1,
                      id:'113_tx',
                      commitId: '987_tx',
                      commitStamp: new Date(Date.now() + 1),
                      commitSequence: 1,
                      restInCommitStream: 0,
                      payload: {
                        event:'bla2'
                      }
                    };

                    store.addEvents([event1, event2], function(err) {
                      expect(err).not.to.be.ok();

                      store.transactions.insert({
                        _id: event1.commitId,
                        events: [event1, event2],
                        aggregateId: event1.aggregateId,
                        aggregate: event1.aggregate,
                        context: event1.context
                      }, function (err) {
                        expect(err).not.to.be.ok();

                        store.events.remove({ _id: event2.id }, function (err) {
                          expect(err).not.to.be.ok();

                          store.getPendingTransactions(function(err, txs) {
                            expect(err).not.to.be.ok();

                            expect(txs).to.be.an('array');
                            expect(txs).to.have.length(1);

                            store.getLastEvent({ aggregateId: txs[0].aggregateId }, function (err, lastEvt) {
                              expect(err).not.to.be.ok();

                              expect(lastEvt.commitStamp.getTime()).to.eql(event1.commitStamp.getTime());
                              expect(lastEvt.aggregateId).to.eql(event1.aggregateId);
                              expect(lastEvt.commitId).to.eql(event1.commitId);
                              expect(lastEvt.payload.event).to.eql(event1.payload.event);

                              store.getEventsByRevision({ aggregateId: event2.aggregateId }, 0, -1, function(err, evts) {
                                expect(err).not.to.be.ok();
                                expect(evts).to.be.an('array');
                                expect(evts).to.have.length(2);
                                expect(evts[0].commitStamp.getTime()).to.eql(event1.commitStamp.getTime());
                                expect(evts[0].aggregateId).to.eql(event1.aggregateId);
                                expect(evts[0].commitId).to.eql(event1.commitId);
                                expect(evts[0].payload.event).to.eql(event1.payload.event);
                                expect(evts[1].commitStamp.getTime()).to.eql(event2.commitStamp.getTime());
                                expect(evts[1].aggregateId).to.eql(event2.aggregateId);
                                expect(evts[1].commitId).to.eql(event2.commitId);
                                expect(evts[1].payload.event).to.eql(event2.payload.event);

                                done();
                              });
                            });
                          });
                        });
                      });
                    });

                  });

                  describe('having no event saved but only the transaction', function () {

                    it('it should ignore the transaction', function(done) {

                      var event1 = {
                        aggregateId: 'id2_tx5',
                        streamRevision: 3,
                        id: '112_tx5',
                        commitId: '987_tx5',
                        commitStamp: new Date(Date.now() + 1),
                        commitSequence: 0,
                        restInCommitStream: 2,
                        payload: {
                          event:'bla'
                        }
                      };

                      var event2 = {
                        aggregateId: 'id2_tx5',
                        streamRevision: 4,
                        id:'113_tx5',
                        commitId: '987_tx5',
                        commitStamp: new Date(Date.now() + 1),
                        commitSequence: 1,
                        restInCommitStream: 1,
                        payload: {
                          event:'bla2'
                        }
                      };

                      var event3 = {
                        aggregateId: 'id2_tx5',
                        streamRevision: 5,
                        id:'114_tx5',
                        commitId: '987_tx5',
                        commitStamp: new Date(Date.now() + 1),
                        commitSequence: 2,
                        restInCommitStream: 0,
                        payload: {
                          event:'bla3'
                        }
                      };

                      store.addEvents([event1, event2, event3], function(err) {
                        expect(err).not.to.be.ok();

                        store.transactions.insert({
                          _id: event1.commitId,
                          events: [event1, event2, event3],
                          aggregateId: event1.aggregateId,
                          aggregate: event1.aggregate,
                          context: event1.context
                        }, function (err) {
                          expect(err).not.to.be.ok();

                          store.events.remove({ '$or': [ { _id: event1.id }, { _id: event2.id }, { _id: event3.id } ] }, function (err) {
                            expect(err).not.to.be.ok();

                            store.getLastEvent({ aggregateId: event1.aggregateId }, function (err, lastEvt) {
                              expect(err).not.to.be.ok();
                              expect(lastEvt).not.to.be.ok();

                              store.transactions.find({}).toArray(function (err, txs) {
                                expect(err).not.to.be.ok();

                                expect(txs).to.have.length(1);
                                expect(txs[0]._id).to.eql(event1.commitId);

                                store.getEventsByRevision({ aggregateId: event1.aggregateId }, 0, -1, function(err, evts) {
                                  expect(err).not.to.be.ok();
                                  expect(evts).to.be.an('array');
                                  expect(evts).to.have.length(0);

                                  store.transactions.find({}).toArray(function (err, txs) {
                                    expect(err).not.to.be.ok();

                                    expect(txs).to.have.length(1);
                                    expect(txs[0]._id).to.eql(event1.commitId);

                                    store.getPendingTransactions(function(err, txs) {
                                      expect(err).not.to.be.ok();

                                      expect(txs).to.be.an('array');
                                      expect(txs).to.have.length(0);

                                      store.transactions.find({}).toArray(function (err, txs) {
                                        expect(err).not.to.be.ok();

                                        expect(txs).to.have.length(0);

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

                  describe('calling getEventsByRevision with a low maxRev value', function () {

                    it('it should successfully handle the transaction', function(done) {

                      var event1 = {
                        aggregateId: 'id2_tx0',
                        streamRevision: 3,
                        id: '112_tx0',
                        commitId: '987_tx0',
                        commitStamp: new Date(Date.now() + 1),
                        commitSequence: 0,
                        restInCommitStream: 2,
                        payload: {
                          event:'bla'
                        }
                      };

                      var event2 = {
                        aggregateId: 'id2_tx0',
                        streamRevision: 4,
                        id:'113_tx0',
                        commitId: '987_tx0',
                        commitStamp: new Date(Date.now() + 1),
                        commitSequence: 1,
                        restInCommitStream: 1,
                        payload: {
                          event:'bla2'
                        }
                      };

                      var event3 = {
                        aggregateId: 'id2_tx0',
                        streamRevision: 5,
                        id:'114_tx0',
                        commitId: '987_tx0',
                        commitStamp: new Date(Date.now() + 1),
                        commitSequence: 2,
                        restInCommitStream: 0,
                        payload: {
                          event:'bla3'
                        }
                      };

                      store.addEvents([event1, event2, event3], function(err) {
                        expect(err).not.to.be.ok();

                        store.transactions.insert({
                          _id: event1.commitId,
                          events: [event1, event2, event3],
                          aggregateId: event1.aggregateId,
                          aggregate: event1.aggregate,
                          context: event1.context
                        }, function (err) {
                          expect(err).not.to.be.ok();

                          store.events.remove({ '$or': [ { _id: event2.id }, { _id: event3.id } ] }, function (err) {
                            expect(err).not.to.be.ok();

                            store.getPendingTransactions(function(err, txs) {
                              expect(err).not.to.be.ok();

                              expect(txs).to.be.an('array');
                              expect(txs).to.have.length(1);

                              store.getLastEvent({ aggregateId: txs[0].aggregateId }, function (err, lastEvt) {
                                expect(err).not.to.be.ok();

                                expect(lastEvt.commitStamp.getTime()).to.eql(event1.commitStamp.getTime());
                                expect(lastEvt.aggregateId).to.eql(event1.aggregateId);
                                expect(lastEvt.commitId).to.eql(event1.commitId);
                                expect(lastEvt.payload.event).to.eql(event1.payload.event);

                                store.getEventsByRevision({ aggregateId: event2.aggregateId }, 0, 5, function(err, evts) {
                                  expect(err).not.to.be.ok();
                                  expect(evts).to.be.an('array');
                                  expect(evts).to.have.length(2);
                                  expect(evts[0].commitStamp.getTime()).to.eql(event1.commitStamp.getTime());
                                  expect(evts[0].aggregateId).to.eql(event1.aggregateId);
                                  expect(evts[0].commitId).to.eql(event1.commitId);
                                  expect(evts[0].payload.event).to.eql(event1.payload.event);
                                  expect(evts[1].commitStamp.getTime()).to.eql(event2.commitStamp.getTime());
                                  expect(evts[1].aggregateId).to.eql(event2.aggregateId);
                                  expect(evts[1].commitId).to.eql(event2.commitId);
                                  expect(evts[1].payload.event).to.eql(event2.payload.event);

                                  store.getLastEvent({ aggregateId: event2.aggregateId }, function (err, lastEvt) {
                                    expect(err).not.to.be.ok();

                                    expect(lastEvt.commitStamp.getTime()).to.eql(event3.commitStamp.getTime());
                                    expect(lastEvt.aggregateId).to.eql(event3.aggregateId);
                                    expect(lastEvt.commitId).to.eql(event3.commitId);
                                    expect(lastEvt.payload.event).to.eql(event3.payload.event);

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

                  describe('calling getEventsByRevision with a too big maxRev value', function () {

                    it('it should successfully handle the transaction', function(done) {

                      var event1 = {
                        aggregateId: 'id2_tx6',
                        streamRevision: 3,
                        id: '112_tx6',
                        commitId: '987_tx6',
                        commitStamp: new Date(Date.now() + 1),
                        commitSequence: 0,
                        restInCommitStream: 2,
                        payload: {
                          event:'bla'
                        }
                      };

                      var event2 = {
                        aggregateId: 'id2_tx6',
                        streamRevision: 4,
                        id:'113_tx6',
                        commitId: '987_tx6',
                        commitStamp: new Date(Date.now() + 1),
                        commitSequence: 1,
                        restInCommitStream: 1,
                        payload: {
                          event:'bla2'
                        }
                      };

                      var event3 = {
                        aggregateId: 'id2_tx6',
                        streamRevision: 5,
                        id:'114_tx6',
                        commitId: '987_tx6',
                        commitStamp: new Date(Date.now() + 1),
                        commitSequence: 2,
                        restInCommitStream: 0,
                        payload: {
                          event:'bla3'
                        }
                      };

                      store.addEvents([event1, event2, event3], function(err) {
                        expect(err).not.to.be.ok();

                        store.transactions.insert({
                          _id: event1.commitId,
                          events: [event1, event2, event3],
                          aggregateId: event1.aggregateId,
                          aggregate: event1.aggregate,
                          context: event1.context
                        }, function (err) {
                          expect(err).not.to.be.ok();

                          store.events.remove({ '$or': [ { _id: event2.id }, { _id: event3.id } ] }, function (err) {
                            expect(err).not.to.be.ok();

                            store.getPendingTransactions(function(err, txs) {
                              expect(err).not.to.be.ok();

                              expect(txs).to.be.an('array');
                              expect(txs).to.have.length(1);

                              store.getLastEvent({ aggregateId: txs[0].aggregateId }, function (err, lastEvt) {
                                expect(err).not.to.be.ok();

                                expect(lastEvt.commitStamp.getTime()).to.eql(event1.commitStamp.getTime());
                                expect(lastEvt.aggregateId).to.eql(event1.aggregateId);
                                expect(lastEvt.commitId).to.eql(event1.commitId);
                                expect(lastEvt.payload.event).to.eql(event1.payload.event);

                                store.getEventsByRevision({ aggregateId: event2.aggregateId }, 0, 10, function(err, evts) {
                                  expect(err).not.to.be.ok();
                                  expect(evts).to.be.an('array');
                                  expect(evts).to.have.length(3);
                                  expect(evts[0].commitStamp.getTime()).to.eql(event1.commitStamp.getTime());
                                  expect(evts[0].aggregateId).to.eql(event1.aggregateId);
                                  expect(evts[0].commitId).to.eql(event1.commitId);
                                  expect(evts[0].payload.event).to.eql(event1.payload.event);
                                  expect(evts[1].commitStamp.getTime()).to.eql(event2.commitStamp.getTime());
                                  expect(evts[1].aggregateId).to.eql(event2.aggregateId);
                                  expect(evts[1].commitId).to.eql(event2.commitId);
                                  expect(evts[1].payload.event).to.eql(event2.payload.event);
                                  expect(evts[2].commitStamp.getTime()).to.eql(event3.commitStamp.getTime());
                                  expect(evts[2].aggregateId).to.eql(event3.aggregateId);
                                  expect(evts[2].commitId).to.eql(event3.commitId);
                                  expect(evts[2].payload.event).to.eql(event3.payload.event);

                                  store.getLastEvent({ aggregateId: event3.aggregateId }, function (err, lastEvt) {
                                    expect(err).not.to.be.ok();

                                    expect(lastEvt.commitStamp.getTime()).to.eql(event3.commitStamp.getTime());
                                    expect(lastEvt.aggregateId).to.eql(event3.aggregateId);
                                    expect(lastEvt.commitId).to.eql(event3.commitId);
                                    expect(lastEvt.payload.event).to.eql(event3.payload.event);

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

                  describe('and not calling getEventsByRevision', function () {

                    it('the transaction can successfully be handled from outside', function(done) {

                      var event1 = {
                        aggregateId: 'id2_tx',
                        streamRevision: 0,
                        id: '112_tx2',
                        commitId: '987_tx2',
                        commitStamp: new Date(Date.now() + 1),
                        commitSequence: 0,
                        restInCommitStream: 1,
                        payload: {
                          event:'bla'
                        }
                      };

                      var event2 = {
                        aggregateId: 'id2_tx',
                        streamRevision: 1,
                        id:'113_tx2',
                        commitId: '987_tx2',
                        commitStamp: new Date(Date.now() + 1),
                        commitSequence: 1,
                        restInCommitStream: 0,
                        payload: {
                          event:'bla2'
                        }
                      };

                      store.addEvents([event1, event2], function(err) {
                        expect(err).not.to.be.ok();

                        store.transactions.insert({
                          _id: event1.commitId,
                          events: [event1, event2],
                          aggregateId: event1.aggregateId,
                          aggregate: event1.aggregate,
                          context: event1.context
                        }, function (err) {
                          expect(err).not.to.be.ok();

                          store.events.remove({ _id: event2.id }, function (err) {
                            expect(err).not.to.be.ok();

                            store.getPendingTransactions(function(err, txs) {
                              expect(err).not.to.be.ok();

                              expect(txs).to.be.an('array');
                              expect(txs).to.have.length(1);

                              store.getLastEvent({ aggregateId: txs[0].aggregateId }, function (err, lastEvt) {
                                expect(err).not.to.be.ok();

                                expect(lastEvt.commitStamp.getTime()).to.eql(event1.commitStamp.getTime());
                                expect(lastEvt.aggregateId).to.eql(event1.aggregateId);
                                expect(lastEvt.commitId).to.eql(event1.commitId);
                                expect(lastEvt.payload.event).to.eql(event1.payload.event);

                                store.repairFailedTransaction(lastEvt, function (err) {
                                  expect(err).not.to.be.ok();

                                  store.getEvents({}, 0, -1, function(err, evts) {
                                    expect(err).not.to.be.ok();
                                    expect(evts).to.be.an('array');
                                    expect(evts).to.have.length(2);
                                    expect(evts[0].commitStamp.getTime()).to.eql(event1.commitStamp.getTime());
                                    expect(evts[0].aggregateId).to.eql(event1.aggregateId);
                                    expect(evts[0].commitId).to.eql(event1.commitId);
                                    expect(evts[0].payload.event).to.eql(event1.payload.event);
                                    expect(evts[1].commitStamp.getTime()).to.eql(event2.commitStamp.getTime());
                                    expect(evts[1].aggregateId).to.eql(event2.aggregateId);
                                    expect(evts[1].commitId).to.eql(event2.commitId);
                                    expect(evts[1].payload.event).to.eql(event2.payload.event);

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

              }

            });

            describe('without aggregateId', function () {

              it('it should callback with an error', function (done) {

                var event = {
                  //aggregateId: 'id1',
                  streamRevision: 0,
                  commitId: '114',
                  commitStamp: new Date(),
                  commitSequence: 0,
                  payload: {
                    event:'bla'
                  },
                  applyMappings: function () {}
                };

                store.addEvents([event], function(err) {
                  expect(err).to.be.ok();
                  done();
                });

              });

            });

            describe('only with aggregateId', function () {

              it('it should save the event', function (done) {

                var event = {
                  aggregateId: 'idhaha',
                  streamRevision: 0,
                  id: '115',
                  commitId: '115',
                  commitStamp: new Date(),
                  commitSequence: 0,
                  payload: {
                    event:'blaffff'
                  },
                  applyMappings: function () {}
                };

                store.addEvents([event], function(err) {
                  expect(err).not.to.be.ok();

                  store.getEvents({}, 0, -1, function(err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts).to.be.an('array');
                    expect(evts).to.have.length(1);
                    expect(evts[0].commitStamp.getTime()).to.eql(event.commitStamp.getTime());
                    expect(evts[0].aggregateId).to.eql(event.aggregateId);
                    expect(evts[0].commitId).to.eql(event.commitId);
                    expect(evts[0].payload.event).to.eql(event.payload.event);

                    done();
                  });
                });

              });

            });

            describe('with aggregateId and aggregate', function () {

              it('it should save the event correctly', function (done) {

                var event = {
                  aggregateId: 'aggId',
                  aggregate: 'myAgg',
                  streamRevision: 0,
                  id:'116',
                  commitId: '116',
                  commitStamp: new Date(),
                  commitSequence: 0,
                  payload: {
                    event:'blaffff'
                  },
                  applyMappings: function () {}
                };

                store.addEvents([event], function(err) {
                  expect(err).not.to.be.ok();

                  store.getEvents({}, 0, -1, function(err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts).to.be.an('array');
                    expect(evts).to.have.length(1);
                    expect(evts[0].commitStamp.getTime()).to.eql(event.commitStamp.getTime());
                    expect(evts[0].aggregateId).to.eql(event.aggregateId);
                    expect(evts[0].aggregate).to.eql(event.aggregate);
                    expect(evts[0].commitId).to.eql(event.commitId);
                    expect(evts[0].payload.event).to.eql(event.payload.event);

                    done();
                  });
                });

              });

            });

            describe('with aggregateId and aggregate and context', function () {

              it('it should save the event correctly', function (done) {

                var event = {
                  aggregateId: 'aggId',
                  aggregate: 'myAgg',
                  context: 'myContext',
                  streamRevision: 0,
                  id:'117',
                  commitId: '117',
                  commitStamp: new Date(),
                  commitSequence: 0,
                  payload: {
                    event:'blaffff'
                  },
                  applyMappings: function () {}
                };

                store.addEvents([event], function(err) {
                  expect(err).not.to.be.ok();

                  store.getEvents({}, 0, -1, function(err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts).to.be.an('array');
                    expect(evts).to.have.length(1);
                    expect(evts[0].commitStamp.getTime()).to.eql(event.commitStamp.getTime());
                    expect(evts[0].aggregateId).to.eql(event.aggregateId);
                    expect(evts[0].aggregate).to.eql(event.aggregate);
                    expect(evts[0].context).to.eql(event.context);
                    expect(evts[0].commitId).to.eql(event.commitId);
                    expect(evts[0].payload.event).to.eql(event.payload.event);

                    done();
                  });
                });

              });

            });

            describe('with aggregateId and context', function () {

              it('it should save the event correctly', function (done) {

                var event = {
                  aggregateId: 'aggId',
                  context: 'myContext',
                  streamRevision: 0,
                  id:'118',
                  commitStamp: new Date(),
                  commitSequence: 0,
                  commitId: '118',
                  payload: {
                    event:'blaffff'
                  },
                  applyMappings: function () {}
                };

                store.addEvents([event], function(err) {
                  expect(err).not.to.be.ok();

                  store.getEvents({}, 0, -1, function(err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts).to.be.an('array');
                    expect(evts).to.have.length(1);
                    expect(evts[0].commitStamp.getTime()).to.eql(event.commitStamp.getTime());
                    expect(evts[0].aggregateId).to.eql(event.aggregateId);
                    expect(evts[0].context).to.eql(event.context);
                    expect(evts[0].commitId).to.eql(event.commitId);
                    expect(evts[0].payload.event).to.eql(event.payload.event);

                    done();
                  });
                });

              });

            });

          });

          describe('having some events in the eventstore', function () {

            var dateSince = new Date(Date.now() + 50);

            var stream1 = [{
              aggregateId: 'id',
              streamRevision: 0,
              id: '119',
              commitId: '1119',
              commitStamp: new Date(Date.now() + 10),
              commitSequence: 0,
              payload: {
                event:'bla'
              },
              applyMappings: function () {}
            }, {
              aggregateId: 'id',
              streamRevision: 1,
              id: '120',
              commitId: '1119',
              commitStamp: new Date(Date.now() + 10),
              commitSequence: 1,
              payload: {
                event:'bla2'
              },
              applyMappings: function () {}
            }];

            var stream2 = [{
              aggregateId: 'idWithAgg',
              aggregate: 'myAgg',
              streamRevision: 0,
              id: '121',
              commitId: '1121',
              commitStamp: new Date(Date.now() + 30),
              commitSequence: 0,
              payload: {
                event:'bla'
              },
              applyMappings: function () {}
            }, {
              aggregateId: 'idWithAgg',
              aggregate: 'myAgg',
              streamRevision: 1,
              id: '122',
              commitId: '1121',
              commitStamp: new Date(Date.now() + 30),
              commitSequence: 1,
              payload: {
                event: 'bla2'
              },
              applyMappings: function () {}
            }];

            var stream3 = [{
              aggregateId: 'id', // id already existing...
              aggregate: 'myAgg',
              streamRevision: 0,
              id: '123',
              commitId: '1123',
              commitStamp: new Date(Date.now() + 50),
              commitSequence: 0,
              payload: {
                event:'bla2'
              },
              applyMappings: function () {}
            }];

            var stream4 = [{
              aggregateId: 'idWithCont',
              context: 'myCont',
              streamRevision: 0,
              id: '124',
              commitId: '1124',
              commitStamp: new Date(Date.now() + 60),
              commitSequence: 0,
              payload: {
                event:'bla'
              },
              applyMappings: function () {}
            }, {
              aggregateId: 'idWithCont',
              context: 'myCont',
              streamRevision: 1,
              id: '125',
              commitId: '1124',
              commitStamp: new Date(Date.now() + 60),
              commitSequence: 1,
              payload: {
                event: 'bla2'
              },
              applyMappings: function () {}
            }];

            var stream5 = [{
              aggregateId: 'id', // id already existing...
              context: 'myCont',
              streamRevision: 0,
              id: '126',
              commitId: '1126',
              commitStamp: new Date(Date.now() + 80),
              commitSequence: 0,
              payload: {
                event:'bla2'
              },
              applyMappings: function () {}
            }];

            var stream6 = [{
              aggregateId: 'idWithAggrAndCont',
              aggregate: 'myAggrrr',
              context: 'myConttttt',
              streamRevision: 0,
              id: '127',
              commitId: '1127',
              commitStamp: new Date(Date.now() + 90),
              commitSequence: 0,
              payload: {
                event:'bla'
              },
              applyMappings: function () {}
            }, {
              aggregateId: 'idWithAggrAndCont',
              aggregate: 'myAggrrr',
              context: 'myConttttt',
              streamRevision: 1,
              id: '128',
              commitId: '1127',
              commitStamp: new Date(Date.now() + 90),
              commitSequence: 1,
              payload: {
                event: 'bla2'
              },
              applyMappings: function () {}
            }];

            var stream7 = [{
              aggregateId: 'idWithAggrAndCont2',
              aggregate: 'myAggrrr2',
              context: 'myConttttt',
              streamRevision: 0,
              id: '129',
              commitId: '1129',
              commitStamp: new Date(Date.now() + 110),
              commitSequence: 0,
              payload: {
                event:'bla'
              },
              applyMappings: function () {}
            }, {
              aggregateId: 'idWithAggrAndCont2',
              aggregate: 'myAggrrr2',
              context: 'myConttttt',
              streamRevision: 1,
              id: '130',
              commitId: '1129',
              commitStamp: new Date(Date.now() + 110),
              commitSequence: 1,
              payload: {
                event: 'bla2'
              },
              applyMappings: function () {}
            }];

            var stream8 = [{
              aggregateId: 'idWithAggrAndCont2',
              aggregate: 'myAggrrr',
              context: 'myConttttt',
              streamRevision: 0,
              id: '131',
              commitId: '1131',
              commitStamp: new Date(Date.now() + 130),
              commitSequence: 0,
              payload: {
                event:'bla'
              },
              applyMappings: function () {}
            }];

            var stream9 = [{
              aggregateId: 'idWithAggrAndCont',
              aggregate: 'myAggrrr2',
              context: 'myConttttt',
              streamRevision: 0,
              id: '132',
              commitId: '1132',
              commitStamp: new Date(Date.now() + 140),
              commitSequence: 0,
              payload: {
                event: 'bla2'
              },
              applyMappings: function () {}
            }];

            var stream10 = [{
              aggregateId: 'id', // id already existing...
              aggregate: 'wowAgg',
              context: 'wowCont',
              streamRevision: 0,
              id: '133',
              commitId: '1133',
              commitStamp: new Date(Date.now() + 150),
              commitSequence: 0,
              payload: {
                event:'bla2'
              },
              applyMappings: function () {}
            }];

            var allEvents = [].concat(stream1).concat(stream2).concat(stream3)
                              .concat(stream4).concat(stream5).concat(stream6)
                              .concat(stream7).concat(stream8).concat(stream9).concat(stream10);

            beforeEach(function (done) {
              async.series([
                function (callback) {
                  store.addEvents(stream1, callback);
                },
                function (callback) {
                  store.addEvents(stream2, callback);
                },
                function (callback) {
                  store.addEvents(stream3, callback);
                },
                function (callback) {
                  store.addEvents(stream4, callback);
                },
                function (callback) {
                  store.addEvents(stream5, callback);
                },
                function (callback) {
                  store.addEvents(stream6, callback);
                },
                function (callback) {
                  store.addEvents(stream7, callback);
                },
                function (callback) {
                  store.addEvents(stream8, callback);
                },
                function (callback) {
                  store.addEvents(stream9, callback);
                },
                function (callback) {
                  store.addEvents(stream10, callback);
                }
              ], done);
            });

            describe('calling getEventsSince', function () {

              describe('to get all events since a date', function () {

                it('it should return the correct values', function (done) {

                  var expectedEvts = allEvents.slice(4);

                  store.getEventsSince(dateSince, 0, -1, function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(expectedEvts.length);

                    var lastCommitStamp = 0;
                    var lastCommitId = 0;
                    var lastId = 0;
                    _.each(evts, function (evt) {
                      expect(evt.id).to.be.greaterThan(lastId);
                      expect(evt.commitId >= lastCommitId).to.eql(true);
                      expect(evt.commitStamp.getTime() >= lastCommitStamp).to.eql(true);
                      lastId = evt.id;
                      lastCommitId = evt.commitId;
                      lastCommitStamp = evt.commitStamp.getTime();
                    });

                    done();
                  });

                });

                describe('with a skip value', function () {

                  it('it should return the correct values', function (done) {

                    var expectedEvts = allEvents.slice(7);

                    store.getEventsSince(dateSince, 3, -1, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(expectedEvts.length);

                      var lastCommitStamp = 0;
                      var lastCommitId = 0;
                      var lastId = 0;
                      _.each(evts, function (evt) {
                        expect(evt.id).to.be.greaterThan(lastId);
                        expect(evt.commitId >= lastCommitId).to.eql(true);
                        expect(evt.commitStamp.getTime() >= lastCommitStamp).to.eql(true);
                        lastId = evt.id;
                        lastCommitId = evt.commitId;
                        lastCommitStamp = evt.commitStamp.getTime();
                      });

                      done();
                    });

                  });

                });

                describe('with a limit value', function () {

                  it('it should return the correct values', function (done) {

                    var expectedEvts = allEvents.slice(4, 9);

                    store.getEventsSince(dateSince, 0, 5, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(expectedEvts.length);

                      var lastCommitStamp = 0;
                      var lastCommitId = 0;
                      var lastId = 0;
                      _.each(evts, function (evt) {
                        expect(evt.id).to.be.greaterThan(lastId);
                        expect(evt.commitId >= lastCommitId).to.eql(true);
                        expect(evt.commitStamp.getTime() >= lastCommitStamp).to.eql(true);
                        lastId = evt.id;
                        lastCommitId = evt.commitId;
                        lastCommitStamp = evt.commitStamp.getTime();
                      });

                      done();
                    });

                  });

                });

                describe('with a skip and a limit value', function () {

                  it('it should return the correct values', function (done) {

                    var expectedEvts = allEvents.slice(7, 9);

                    store.getEventsSince(dateSince, 4, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(expectedEvts.length);

                      var lastCommitStamp = 0;
                      var lastCommitId = 0;
                      var lastId = 0;
                      _.each(evts, function (evt) {
                        expect(evt.id).to.be.greaterThan(lastId);
                        expect(evt.commitId >= lastCommitId).to.eql(true);
                        expect(evt.commitStamp.getTime() >= lastCommitStamp).to.eql(true);
                        lastId = evt.id;
                        lastCommitId = evt.commitId;
                        lastCommitStamp = evt.commitStamp.getTime();
                      });

                      done();
                    });

                  });

                });

              });

              describe('with an aggregateId being used only in one context and aggregate', function () {

                it('it should return the correct events', function (done) {

                  store.getEvents({ aggregateId: 'idWithAgg' }, 0, -1, function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(2);
                    expect(evts[0].id).to.eql(stream2[0].id);
                    expect(evts[0].aggregateId).to.eql(stream2[0].aggregateId);
                    expect(evts[0].commitStamp.getTime()).to.eql(stream2[0].commitStamp.getTime());
                    expect(evts[0].commitSequence).to.eql(stream2[0].commitSequence);
                    expect(evts[0].streamRevision).to.eql(stream2[0].streamRevision);
                    expect(evts[1].id).to.eql(stream2[1].id);
                    expect(evts[1].aggregateId).to.eql(stream2[1].aggregateId);
                    expect(evts[1].commitStamp.getTime()).to.eql(stream2[1].commitStamp.getTime());
                    expect(evts[1].commitSequence).to.eql(stream2[1].commitSequence);
                    expect(evts[1].streamRevision).to.eql(stream2[1].streamRevision);

                    done();
                  });

                });

                describe('and limit it with skip and limit', function () {

                  it('it should return the correct events', function (done) {

                    store.getEvents({ aggregateId: 'idWithAgg' }, 1, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(1);
                      expect(evts[0].aggregateId).to.eql(stream2[1].aggregateId);
                      expect(evts[0].commitStamp.getTime()).to.eql(stream2[1].commitStamp.getTime());
                      expect(evts[0].streamRevision).to.eql(stream2[1].streamRevision);

                      store.getLastEvent({ aggregateId: 'idWithAgg' }, function(err, evt) {
                        expect(err).not.to.be.ok();

                        expect(evt.aggregateId).to.eql(stream2[1].aggregateId);
                        expect(evt.commitStamp.getTime()).to.eql(stream2[1].commitStamp.getTime());
                        expect(evt.streamRevision).to.eql(stream2[1].streamRevision);
                        done();
                      });
                    });

                  });

                });

              });

              describe('with an aggregateId being used in an other context or aggregate', function () {

                it('it should return the correct events', function (done) {

                  store.getEvents({ aggregateId: 'id' }, 0, -1, function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(5);
                    expect(evts[0].aggregateId).to.eql(stream1[0].aggregateId);
                    expect(evts[0].commitStamp.getTime()).to.eql(stream1[0].commitStamp.getTime());
                    expect(evts[0].streamRevision).to.eql(stream1[0].streamRevision);
                    expect(evts[1].aggregateId).to.eql(stream1[1].aggregateId);
                    expect(evts[1].commitStamp.getTime()).to.eql(stream1[1].commitStamp.getTime());
                    expect(evts[1].streamRevision).to.eql(stream1[1].streamRevision);
                    expect(evts[2].aggregateId).to.eql(stream3[0].aggregateId);
                    expect(evts[2].commitStamp.getTime()).to.eql(stream3[0].commitStamp.getTime());
                    expect(evts[2].streamRevision).to.eql(stream3[0].streamRevision);
                    expect(evts[3].aggregateId).to.eql(stream5[0].aggregateId);
                    expect(evts[3].commitStamp.getTime()).to.eql(stream5[0].commitStamp.getTime());
                    expect(evts[3].streamRevision).to.eql(stream5[0].streamRevision);
                    expect(evts[4].aggregateId).to.eql(stream10[0].aggregateId);
                    expect(evts[4].commitStamp.getTime()).to.eql(stream10[0].commitStamp.getTime());
                    expect(evts[4].streamRevision).to.eql(stream10[0].streamRevision);

                    done();
                  });

                });

                describe('and limit it with revMin and revMax', function () {

                  it('it should return the correct events', function (done) {

                    store.getEvents({ aggregateId: 'id' }, 1, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(2);
                      expect(evts[0].aggregateId).to.eql(stream1[1].aggregateId);
                      expect(evts[0].commitStamp.getTime()).to.eql(stream1[1].commitStamp.getTime());
                      expect(evts[0].streamRevision).to.eql(stream1[1].streamRevision);

                      done();
                    });

                  });

                });

              });

              describe('without an aggregateId but with an aggregate', function () {

                it('it should return the correct events', function (done) {

                  store.getEvents({ aggregate: 'myAggrrr2' }, 0, -1, function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(3);
                    expect(evts[0].aggregateId).to.eql(stream7[0].aggregateId);
                    expect(evts[0].commitStamp.getTime()).to.eql(stream7[0].commitStamp.getTime());
                    expect(evts[0].streamRevision).to.eql(stream7[0].streamRevision);
                    expect(evts[1].aggregateId).to.eql(stream7[1].aggregateId);
                    expect(evts[1].commitStamp.getTime()).to.eql(stream7[1].commitStamp.getTime());
                    expect(evts[1].streamRevision).to.eql(stream7[1].streamRevision);
                    expect(evts[2].aggregateId).to.eql(stream9[0].aggregateId);
                    expect(evts[2].commitStamp.getTime()).to.eql(stream9[0].commitStamp.getTime());
                    expect(evts[2].streamRevision).to.eql(stream9[0].streamRevision);

                    done();
                  });

                });

                describe('and limit it with skip and limit', function () {

                  it('it should return the correct events', function (done) {

                    store.getEvents({ aggregate: 'myAggrrr2' }, 1, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(2);
                      expect(evts[0].aggregateId).to.eql(stream7[1].aggregateId);
                      expect(evts[0].commitStamp.getTime()).to.eql(stream7[1].commitStamp.getTime());
                      expect(evts[0].streamRevision).to.eql(stream7[1].streamRevision);
                      expect(evts[1].aggregateId).to.eql(stream9[0].aggregateId);
                      expect(evts[1].commitStamp.getTime()).to.eql(stream9[0].commitStamp.getTime());
                      expect(evts[1].streamRevision).to.eql(stream9[0].streamRevision);

                      done();
                    });

                  });

                });

              });

              describe('with an aggregateId and with an aggregate', function () {

                it('it should return the correct events', function (done) {

                  store.getEvents({ aggregate: 'myAggrrr2', aggregateId: 'idWithAggrAndCont' }, 0, -1, function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(1);
                    expect(evts[0].aggregateId).to.eql(stream9[0].aggregateId);
                    expect(evts[0].commitStamp.getTime()).to.eql(stream9[0].commitStamp.getTime());
                    expect(evts[0].streamRevision).to.eql(stream9[0].streamRevision);

                    done();
                  });

                });

                describe('and limit it with skip and limit', function () {

                  it('it should return the correct events', function (done) {

                    store.getEvents({ aggregate: 'myAggrrr2', aggregateId: 'idWithAggrAndCont' }, 1, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(0);

                      done();
                    });

                  });

                });

              });

              describe('with an aggregateId and without an aggregate but with a context', function () {

                it('it should return the correct events', function (done) {

                  store.getEvents({ aggregateId: 'idWithAggrAndCont', context: 'myConttttt' }, 0, -1, function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(3);
                    expect(evts[0].aggregateId).to.eql(stream6[0].aggregateId);
                    expect(evts[0].commitStamp.getTime()).to.eql(stream6[0].commitStamp.getTime());
                    expect(evts[0].streamRevision).to.eql(stream6[0].streamRevision);
                    expect(evts[1].aggregateId).to.eql(stream6[1].aggregateId);
                    expect(evts[1].commitStamp.getTime()).to.eql(stream6[1].commitStamp.getTime());
                    expect(evts[1].streamRevision).to.eql(stream6[1].streamRevision);
                    expect(evts[2].aggregateId).to.eql(stream9[0].aggregateId);
                    expect(evts[2].commitStamp.getTime()).to.eql(stream9[0].commitStamp.getTime());
                    expect(evts[2].streamRevision).to.eql(stream9[0].streamRevision);

                    done();
                  });

                });

                describe('and limit it with skip and limit', function () {

                  it('it should return the correct events', function (done) {

                    store.getEvents({ aggregateId: 'idWithAggrAndCont', context: 'myConttttt' }, 1, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(2);
                      expect(evts[0].aggregateId).to.eql(stream6[1].aggregateId);
                      expect(evts[0].commitStamp.getTime()).to.eql(stream6[1].commitStamp.getTime());
                      expect(evts[0].streamRevision).to.eql(stream6[1].streamRevision);
                      expect(evts[1].aggregateId).to.eql(stream9[0].aggregateId);
                      expect(evts[1].commitStamp.getTime()).to.eql(stream9[0].commitStamp.getTime());
                      expect(evts[1].streamRevision).to.eql(stream9[0].streamRevision);

                      done();
                    });

                  });

                });

              });

              describe('with an aggregateId and with an aggregate and with a context', function () {

                it('it should return the correct events', function (done) {

                  store.getEvents({ aggregateId: 'id', aggregate: 'wowAgg', context: 'wowCont' }, 0, -1, function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(1);
                    expect(evts[0].aggregateId).to.eql(stream10[0].aggregateId);
                    expect(evts[0].commitStamp.getTime()).to.eql(stream10[0].commitStamp.getTime());
                    expect(evts[0].streamRevision).to.eql(stream10[0].streamRevision);

                    done();
                  });

                });

                describe('and limit it with skip and limit', function () {

                  it('it should return the correct events', function (done) {

                    store.getEvents({ aggregateId: 'id', aggregate: 'wowAgg', context: 'wowCont' }, 1, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(0);

                      done();
                    });

                  });

                });

              });

              describe('without an aggregateId and without an aggregate but with a context', function () {

                it('it should return the correct events', function (done) {

                  store.getEvents({ context: 'myCont' }, 0, -1, function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(3);
                    expect(evts[0].aggregateId).to.eql(stream4[0].aggregateId);
                    expect(evts[0].commitStamp.getTime()).to.eql(stream4[0].commitStamp.getTime());
                    expect(evts[0].streamRevision).to.eql(stream4[0].streamRevision);
                    expect(evts[1].aggregateId).to.eql(stream4[1].aggregateId);
                    expect(evts[1].commitStamp.getTime()).to.eql(stream4[1].commitStamp.getTime());
                    expect(evts[1].streamRevision).to.eql(stream4[1].streamRevision);
                    expect(evts[2].aggregateId).to.eql(stream5[0].aggregateId);
                    expect(evts[2].commitStamp.getTime()).to.eql(stream5[0].commitStamp.getTime());
                    expect(evts[2].streamRevision).to.eql(stream5[0].streamRevision);

                    done();
                  });

                });

                describe('and limit it with skip and limit', function () {

                  it('it should return the correct events', function (done) {

                    store.getEvents({ context: 'myCont' }, 1, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(2);
                      expect(evts[0].aggregateId).to.eql(stream4[1].aggregateId);
                      expect(evts[0].commitStamp.getTime()).to.eql(stream4[1].commitStamp.getTime());
                      expect(evts[0].streamRevision).to.eql(stream4[1].streamRevision);
                      expect(evts[1].aggregateId).to.eql(stream5[0].aggregateId);
                      expect(evts[1].commitStamp.getTime()).to.eql(stream5[0].commitStamp.getTime());
                      expect(evts[1].streamRevision).to.eql(stream5[0].streamRevision);

                      done();
                    });

                  });

                });

              });

              describe('without an aggregateId but with an aggregate and with a context', function () {

                it('it should return the correct events', function (done) {

                  store.getEvents({ context: 'myConttttt', aggregate: 'myAggrrr' }, 0, -1, function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(3);
                    expect(evts[0].aggregateId).to.eql(stream6[0].aggregateId);
                    expect(evts[0].commitStamp.getTime()).to.eql(stream6[0].commitStamp.getTime());
                    expect(evts[0].streamRevision).to.eql(stream6[0].streamRevision);
                    expect(evts[1].aggregateId).to.eql(stream6[1].aggregateId);
                    expect(evts[1].commitStamp.getTime()).to.eql(stream6[1].commitStamp.getTime());
                    expect(evts[1].streamRevision).to.eql(stream6[1].streamRevision);
                    expect(evts[2].aggregateId).to.eql(stream8[0].aggregateId);
                    expect(evts[2].commitStamp.getTime()).to.eql(stream8[0].commitStamp.getTime());
                    expect(evts[2].streamRevision).to.eql(stream8[0].streamRevision);

                    done();
                  });

                });

                describe('and limit it with skip and limit', function () {

                  it('it should return the correct events', function (done) {

                    store.getEvents({ context: 'myConttttt', aggregate: 'myAggrrr' }, 1, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(2);
                      expect(evts[0].aggregateId).to.eql(stream6[1].aggregateId);
                      expect(evts[0].commitStamp.getTime()).to.eql(stream6[1].commitStamp.getTime());
                      expect(evts[0].streamRevision).to.eql(stream6[1].streamRevision);
                      expect(evts[1].aggregateId).to.eql(stream8[0].aggregateId);
                      expect(evts[1].commitStamp.getTime()).to.eql(stream8[0].commitStamp.getTime());
                      expect(evts[1].streamRevision).to.eql(stream8[0].streamRevision);

                      done();
                    });

                  });

                });

              });

            });

            describe('calling getEvents', function () {

              describe('to get all events', function () {

                it('it should return the correct values', function (done) {

                  store.getEvents({}, 0, -1, function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(allEvents.length);

                    var lastCommitStamp = 0;
                    var lastCommitId = 0;
                    var lastId = 0;
                    _.each(evts, function (evt) {
                      expect(evt.id).to.be.greaterThan(lastId);
                      expect(evt.commitId >= lastCommitId).to.eql(true);
                      expect(evt.commitStamp.getTime() >= lastCommitStamp).to.eql(true);
                      lastId = evt.id;
                      lastCommitId = evt.commitId;
                      lastCommitStamp = evt.commitStamp.getTime();
                    });

                    done();
                  });

                });

                describe('with a skip value', function () {

                  it('it should return the correct values', function (done) {

                    var expectedEvts = allEvents.slice(3);

                    store.getEvents({}, 3, -1, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(expectedEvts.length);

                      var lastCommitStamp = 0;
                      var lastCommitId = 0;
                      var lastId = 0;
                      _.each(evts, function (evt) {
                        expect(evt.id).to.be.greaterThan(lastId);
                        expect(evt.commitId >= lastCommitId).to.eql(true);
                        expect(evt.commitStamp.getTime() >= lastCommitStamp).to.eql(true);
                        lastId = evt.id;
                        lastCommitId = evt.commitId;
                        lastCommitStamp = evt.commitStamp.getTime();
                      });

                      done();
                    });

                  });

                });

                describe('with a limit value', function () {

                  it('it should return the correct values', function (done) {

                    var expectedEvts = allEvents.slice(0, 5);

                    store.getEvents({}, 0, 5, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(expectedEvts.length);

                      var lastCommitStamp = 0;
                      var lastCommitId = 0;
                      var lastId = 0;
                      _.each(evts, function (evt) {
                        expect(evt.id).to.be.greaterThan(lastId);
                        expect(evt.commitId >= lastCommitId).to.eql(true);
                        expect(evt.commitStamp.getTime() >= lastCommitStamp).to.eql(true);
                        lastId = evt.id;
                        lastCommitId = evt.commitId;
                        lastCommitStamp = evt.commitStamp.getTime();
                      });

                      done();
                    });

                  });

                });

                describe('with a skip and a limit value', function () {

                  it('it should return the correct values', function (done) {

                    var expectedEvts = allEvents.slice(3, 5);

                    store.getEvents({}, 3, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(expectedEvts.length);

                      var lastCommitStamp = 0;
                      var lastCommitId = 0;
                      var lastId = 0;
                      _.each(evts, function (evt) {
                        expect(evt.id).to.be.greaterThan(lastId);
                        expect(evt.commitId >= lastCommitId).to.eql(true);
                        expect(evt.commitStamp.getTime() >= lastCommitStamp).to.eql(true);
                        lastId = evt.id;
                        lastCommitId = evt.commitId;
                        lastCommitStamp = evt.commitStamp.getTime();
                      });

                      done();
                    });

                  });

                });

              });

              describe('with an aggregateId being used only in one context and aggregate', function () {

                it('it should return the correct events', function (done) {

                  store.getEvents({ aggregateId: 'idWithAgg' }, 0, -1, function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(2);
                    expect(evts[0].id).to.eql(stream2[0].id);
                    expect(evts[0].aggregateId).to.eql(stream2[0].aggregateId);
                    expect(evts[0].commitStamp.getTime()).to.eql(stream2[0].commitStamp.getTime());
                    expect(evts[0].commitSequence).to.eql(stream2[0].commitSequence);
                    expect(evts[0].streamRevision).to.eql(stream2[0].streamRevision);
                    expect(evts[1].id).to.eql(stream2[1].id);
                    expect(evts[1].aggregateId).to.eql(stream2[1].aggregateId);
                    expect(evts[1].commitStamp.getTime()).to.eql(stream2[1].commitStamp.getTime());
                    expect(evts[1].commitSequence).to.eql(stream2[1].commitSequence);
                    expect(evts[1].streamRevision).to.eql(stream2[1].streamRevision);

                    done();
                  });

                });

                describe('and limit it with skip and limit', function () {

                  it('it should return the correct events', function (done) {

                    store.getEvents({ aggregateId: 'idWithAgg' }, 1, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(1);
                      expect(evts[0].aggregateId).to.eql(stream2[1].aggregateId);
                      expect(evts[0].commitStamp.getTime()).to.eql(stream2[1].commitStamp.getTime());
                      expect(evts[0].streamRevision).to.eql(stream2[1].streamRevision);

                      done();
                    });

                  });

                });

              });

              describe('with an aggregateId being used in an other context or aggregate', function () {

                it('it should return the correct events', function (done) {

                  store.getEvents({ aggregateId: 'id' }, 0, -1, function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(5);
                    expect(evts[0].aggregateId).to.eql(stream1[0].aggregateId);
                    expect(evts[0].commitStamp.getTime()).to.eql(stream1[0].commitStamp.getTime());
                    expect(evts[0].streamRevision).to.eql(stream1[0].streamRevision);
                    expect(evts[1].aggregateId).to.eql(stream1[1].aggregateId);
                    expect(evts[1].commitStamp.getTime()).to.eql(stream1[1].commitStamp.getTime());
                    expect(evts[1].streamRevision).to.eql(stream1[1].streamRevision);
                    expect(evts[2].aggregateId).to.eql(stream3[0].aggregateId);
                    expect(evts[2].commitStamp.getTime()).to.eql(stream3[0].commitStamp.getTime());
                    expect(evts[2].streamRevision).to.eql(stream3[0].streamRevision);
                    expect(evts[3].aggregateId).to.eql(stream5[0].aggregateId);
                    expect(evts[3].commitStamp.getTime()).to.eql(stream5[0].commitStamp.getTime());
                    expect(evts[3].streamRevision).to.eql(stream5[0].streamRevision);
                    expect(evts[4].aggregateId).to.eql(stream10[0].aggregateId);
                    expect(evts[4].commitStamp.getTime()).to.eql(stream10[0].commitStamp.getTime());
                    expect(evts[4].streamRevision).to.eql(stream10[0].streamRevision);

                    done();
                  });

                });

                describe('and limit it with revMin and revMax', function () {

                  it('it should return the correct events', function (done) {

                    store.getEvents({ aggregateId: 'id' }, 1, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(2);
                      expect(evts[0].aggregateId).to.eql(stream1[1].aggregateId);
                      expect(evts[0].commitStamp.getTime()).to.eql(stream1[1].commitStamp.getTime());
                      expect(evts[0].streamRevision).to.eql(stream1[1].streamRevision);

                      done();
                    });

                  });

                });

              });

              describe('without an aggregateId but with an aggregate', function () {

                it('it should return the correct events', function (done) {

                  store.getEvents({ aggregate: 'myAggrrr2' }, 0, -1, function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(3);
                    expect(evts[0].aggregateId).to.eql(stream7[0].aggregateId);
                    expect(evts[0].commitStamp.getTime()).to.eql(stream7[0].commitStamp.getTime());
                    expect(evts[0].streamRevision).to.eql(stream7[0].streamRevision);
                    expect(evts[1].aggregateId).to.eql(stream7[1].aggregateId);
                    expect(evts[1].commitStamp.getTime()).to.eql(stream7[1].commitStamp.getTime());
                    expect(evts[1].streamRevision).to.eql(stream7[1].streamRevision);
                    expect(evts[2].aggregateId).to.eql(stream9[0].aggregateId);
                    expect(evts[2].commitStamp.getTime()).to.eql(stream9[0].commitStamp.getTime());
                    expect(evts[2].streamRevision).to.eql(stream9[0].streamRevision);

                    done();
                  });

                });

                describe('and limit it with skip and limit', function () {

                  it('it should return the correct events', function (done) {

                    store.getEvents({ aggregate: 'myAggrrr2' }, 1, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(2);
                      expect(evts[0].aggregateId).to.eql(stream7[1].aggregateId);
                      expect(evts[0].commitStamp.getTime()).to.eql(stream7[1].commitStamp.getTime());
                      expect(evts[0].streamRevision).to.eql(stream7[1].streamRevision);
                      expect(evts[1].aggregateId).to.eql(stream9[0].aggregateId);
                      expect(evts[1].commitStamp.getTime()).to.eql(stream9[0].commitStamp.getTime());
                      expect(evts[1].streamRevision).to.eql(stream9[0].streamRevision);

                      done();
                    });

                  });

                });

              });

              describe('with an aggregateId and with an aggregate', function () {

                it('it should return the correct events', function (done) {

                  store.getEvents({ aggregate: 'myAggrrr2', aggregateId: 'idWithAggrAndCont' }, 0, -1, function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(1);
                    expect(evts[0].aggregateId).to.eql(stream9[0].aggregateId);
                    expect(evts[0].commitStamp.getTime()).to.eql(stream9[0].commitStamp.getTime());
                    expect(evts[0].streamRevision).to.eql(stream9[0].streamRevision);

                    done();
                  });

                });

                describe('and limit it with skip and limit', function () {

                  it('it should return the correct events', function (done) {

                    store.getEvents({ aggregate: 'myAggrrr2', aggregateId: 'idWithAggrAndCont' }, 1, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(0);

                      done();
                    });

                  });

                });

              });

              describe('with an aggregateId and without an aggregate but with a context', function () {

                it('it should return the correct events', function (done) {

                  store.getEvents({ aggregateId: 'idWithAggrAndCont', context: 'myConttttt' }, 0, -1, function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(3);
                    expect(evts[0].aggregateId).to.eql(stream6[0].aggregateId);
                    expect(evts[0].commitStamp.getTime()).to.eql(stream6[0].commitStamp.getTime());
                    expect(evts[0].streamRevision).to.eql(stream6[0].streamRevision);
                    expect(evts[1].aggregateId).to.eql(stream6[1].aggregateId);
                    expect(evts[1].commitStamp.getTime()).to.eql(stream6[1].commitStamp.getTime());
                    expect(evts[1].streamRevision).to.eql(stream6[1].streamRevision);
                    expect(evts[2].aggregateId).to.eql(stream9[0].aggregateId);
                    expect(evts[2].commitStamp.getTime()).to.eql(stream9[0].commitStamp.getTime());
                    expect(evts[2].streamRevision).to.eql(stream9[0].streamRevision);

                    done();
                  });

                });

                describe('and limit it with skip and limit', function () {

                  it('it should return the correct events', function (done) {

                    store.getEvents({ aggregateId: 'idWithAggrAndCont', context: 'myConttttt' }, 1, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(2);
                      expect(evts[0].aggregateId).to.eql(stream6[1].aggregateId);
                      expect(evts[0].commitStamp.getTime()).to.eql(stream6[1].commitStamp.getTime());
                      expect(evts[0].streamRevision).to.eql(stream6[1].streamRevision);
                      expect(evts[1].aggregateId).to.eql(stream9[0].aggregateId);
                      expect(evts[1].commitStamp.getTime()).to.eql(stream9[0].commitStamp.getTime());
                      expect(evts[1].streamRevision).to.eql(stream9[0].streamRevision);

                      done();
                    });

                  });

                });

              });

              describe('with an aggregateId and with an aggregate and with a context', function () {

                it('it should return the correct events', function (done) {

                  store.getEvents({ aggregateId: 'id', aggregate: 'wowAgg', context: 'wowCont' }, 0, -1, function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(1);
                    expect(evts[0].aggregateId).to.eql(stream10[0].aggregateId);
                    expect(evts[0].commitStamp.getTime()).to.eql(stream10[0].commitStamp.getTime());
                    expect(evts[0].streamRevision).to.eql(stream10[0].streamRevision);

                    done();
                  });

                });

                describe('and limit it with skip and limit', function () {

                  it('it should return the correct events', function (done) {

                    store.getEvents({ aggregateId: 'id', aggregate: 'wowAgg', context: 'wowCont' }, 1, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(0);

                      done();
                    });

                  });

                });

              });

              describe('without an aggregateId and without an aggregate but with a context', function () {

                it('it should return the correct events', function (done) {

                  store.getEvents({ context: 'myCont' }, 0, -1, function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(3);
                    expect(evts[0].aggregateId).to.eql(stream4[0].aggregateId);
                    expect(evts[0].commitStamp.getTime()).to.eql(stream4[0].commitStamp.getTime());
                    expect(evts[0].streamRevision).to.eql(stream4[0].streamRevision);
                    expect(evts[1].aggregateId).to.eql(stream4[1].aggregateId);
                    expect(evts[1].commitStamp.getTime()).to.eql(stream4[1].commitStamp.getTime());
                    expect(evts[1].streamRevision).to.eql(stream4[1].streamRevision);
                    expect(evts[2].aggregateId).to.eql(stream5[0].aggregateId);
                    expect(evts[2].commitStamp.getTime()).to.eql(stream5[0].commitStamp.getTime());
                    expect(evts[2].streamRevision).to.eql(stream5[0].streamRevision);

                    done();
                  });

                });

                describe('and limit it with skip and limit', function () {

                  it('it should return the correct events', function (done) {

                    store.getEvents({ context: 'myCont' }, 1, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(2);
                      expect(evts[0].aggregateId).to.eql(stream4[1].aggregateId);
                      expect(evts[0].commitStamp.getTime()).to.eql(stream4[1].commitStamp.getTime());
                      expect(evts[0].streamRevision).to.eql(stream4[1].streamRevision);
                      expect(evts[1].aggregateId).to.eql(stream5[0].aggregateId);
                      expect(evts[1].commitStamp.getTime()).to.eql(stream5[0].commitStamp.getTime());
                      expect(evts[1].streamRevision).to.eql(stream5[0].streamRevision);

                      done();
                    });

                  });

                });

              });

              describe('without an aggregateId but with an aggregate and with a context', function () {

                it('it should return the correct events', function (done) {

                  store.getEvents({ context: 'myConttttt', aggregate: 'myAggrrr' }, 0, -1, function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(3);
                    expect(evts[0].aggregateId).to.eql(stream6[0].aggregateId);
                    expect(evts[0].commitStamp.getTime()).to.eql(stream6[0].commitStamp.getTime());
                    expect(evts[0].streamRevision).to.eql(stream6[0].streamRevision);
                    expect(evts[1].aggregateId).to.eql(stream6[1].aggregateId);
                    expect(evts[1].commitStamp.getTime()).to.eql(stream6[1].commitStamp.getTime());
                    expect(evts[1].streamRevision).to.eql(stream6[1].streamRevision);
                    expect(evts[2].aggregateId).to.eql(stream8[0].aggregateId);
                    expect(evts[2].commitStamp.getTime()).to.eql(stream8[0].commitStamp.getTime());
                    expect(evts[2].streamRevision).to.eql(stream8[0].streamRevision);

                    done();
                  });

                });

                describe('and limit it with skip and limit', function () {

                  it('it should return the correct events', function (done) {

                    store.getEvents({ context: 'myConttttt', aggregate: 'myAggrrr' }, 1, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(2);
                      expect(evts[0].aggregateId).to.eql(stream6[1].aggregateId);
                      expect(evts[0].commitStamp.getTime()).to.eql(stream6[1].commitStamp.getTime());
                      expect(evts[0].streamRevision).to.eql(stream6[1].streamRevision);
                      expect(evts[1].aggregateId).to.eql(stream8[0].aggregateId);
                      expect(evts[1].commitStamp.getTime()).to.eql(stream8[0].commitStamp.getTime());
                      expect(evts[1].streamRevision).to.eql(stream8[0].streamRevision);

                      done();
                    });

                  });

                });

              });

            });

            describe('calling getEventsByRevision', function () {

              describe('with an aggregateId being used only in one context and aggregate', function () {

                it('it should return the correct events', function (done) {

                  store.getEventsByRevision({ aggregateId: 'idWithAgg' }, 0, -1, function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(2);
                    expect(evts[0].aggregateId).to.eql(stream2[0].aggregateId);
                    expect(evts[0].commitStamp.getTime()).to.eql(stream2[0].commitStamp.getTime());
                    expect(evts[0].streamRevision).to.eql(stream2[0].streamRevision);
                    expect(evts[1].aggregateId).to.eql(stream2[1].aggregateId);
                    expect(evts[1].commitStamp.getTime()).to.eql(stream2[1].commitStamp.getTime());
                    expect(evts[1].streamRevision).to.eql(stream2[1].streamRevision);

                    done();
                  });

                });

                describe('and limit it with revMin and revMax', function () {

                  it('it should return the correct events', function (done) {

                    store.getEventsByRevision({ aggregateId: 'idWithAgg' }, 1, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(1);
                      expect(evts[0].aggregateId).to.eql(stream2[1].aggregateId);
                      expect(evts[0].commitStamp.getTime()).to.eql(stream2[1].commitStamp.getTime());
                      expect(evts[0].streamRevision).to.eql(stream2[1].streamRevision);

                      done();
                    });

                  });

                });

              });

              describe('with an aggregateId being used in an other context or aggregate', function () {

                it('it should return the correct events', function (done) {

                  store.getEventsByRevision({ aggregateId: 'id' }, 0, -1, function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(5);
                    expect(evts[0].aggregateId).to.eql(stream1[0].aggregateId);
                    expect(evts[0].commitStamp.getTime()).to.eql(stream1[0].commitStamp.getTime());
                    expect(evts[0].streamRevision).to.eql(stream1[0].streamRevision);
                    expect(evts[1].aggregateId).to.eql(stream1[1].aggregateId);
                    expect(evts[1].commitStamp.getTime()).to.eql(stream1[1].commitStamp.getTime());
                    expect(evts[1].streamRevision).to.eql(stream1[1].streamRevision);
                    expect(evts[2].aggregateId).to.eql(stream3[0].aggregateId);
                    expect(evts[2].commitStamp.getTime()).to.eql(stream3[0].commitStamp.getTime());
                    expect(evts[2].streamRevision).to.eql(stream3[0].streamRevision);
                    expect(evts[3].aggregateId).to.eql(stream5[0].aggregateId);
                    expect(evts[3].commitStamp.getTime()).to.eql(stream5[0].commitStamp.getTime());
                    expect(evts[3].streamRevision).to.eql(stream5[0].streamRevision);
                    expect(evts[4].aggregateId).to.eql(stream10[0].aggregateId);
                    expect(evts[4].commitStamp.getTime()).to.eql(stream10[0].commitStamp.getTime());
                    expect(evts[4].streamRevision).to.eql(stream10[0].streamRevision);

                    done();
                  });

                });

                describe('and limit it with revMin and revMax', function () {

                  it('it should return the correct events', function (done) {

                    store.getEventsByRevision({ aggregateId: 'id' }, 1, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(1);
                      expect(evts[0].aggregateId).to.eql(stream1[1].aggregateId);
                      expect(evts[0].commitStamp.getTime()).to.eql(stream1[1].commitStamp.getTime());
                      expect(evts[0].streamRevision).to.eql(stream1[1].streamRevision);

                      done();
                    });

                  });

                });

              });

              describe('with an aggregateId and with an aggregate', function () {

                it('it should return the correct events', function (done) {

                  store.getEventsByRevision({ aggregate: 'myAggrrr2', aggregateId: 'idWithAggrAndCont' }, 0, -1, function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(1);
                    expect(evts[0].aggregateId).to.eql(stream9[0].aggregateId);
                    expect(evts[0].commitStamp.getTime()).to.eql(stream9[0].commitStamp.getTime());
                    expect(evts[0].streamRevision).to.eql(stream9[0].streamRevision);

                    done();
                  });

                });

                describe('and limit it with skip and limit', function () {

                  it('it should return the correct events', function (done) {

                    store.getEventsByRevision({ aggregate: 'myAggrrr2', aggregateId: 'idWithAggrAndCont' }, 1, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(0);

                      done();
                    });

                  });

                });

                describe('and an other combination of limit and skip', function () {

                  it('it should return the correct events', function (done) {

                    store.getEventsByRevision({ aggregate: 'myAggrrr2', aggregateId: 'idWithAggrAndCont' }, 0, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(1);

                      done();
                    });

                  });

                });

              });

              describe('with an aggregateId and with an aggregate and with a context', function () {

                it('it should return the correct events', function (done) {

                  store.getEventsByRevision({ aggregateId: 'id', aggregate: 'wowAgg', context: 'wowCont' }, 0, -1, function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(1);
                    expect(evts[0].aggregateId).to.eql(stream10[0].aggregateId);
                    expect(evts[0].commitStamp.getTime()).to.eql(stream10[0].commitStamp.getTime());
                    expect(evts[0].streamRevision).to.eql(stream10[0].streamRevision);

                    done();
                  });

                });

                describe('and limit it with skip and limit', function () {

                  it('it should return the correct events', function (done) {

                    store.getEventsByRevision({ aggregateId: 'id', aggregate: 'wowAgg', context: 'wowCont' }, 1, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(0);

                      done();
                    });

                  });

                });

                describe('and an other combination of limit and skip', function () {

                  it('it should return the correct events', function (done) {

                    store.getEventsByRevision({ aggregateId: 'id', aggregate: 'wowAgg', context: 'wowCont' }, 0, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(1);

                      done();
                    });

                  });

                });

              });

              describe('with an aggregateId and without an aggregate but with a context', function () {

                it('it should return the correct events', function (done) {

                  store.getEventsByRevision({ aggregateId: 'idWithAggrAndCont', context: 'myConttttt' }, 0, -1, function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(3);
                    expect(evts[0].aggregateId).to.eql(stream6[0].aggregateId);
                    expect(evts[0].commitStamp.getTime()).to.eql(stream6[0].commitStamp.getTime());
                    expect(evts[0].streamRevision).to.eql(stream6[0].streamRevision);
                    expect(evts[1].aggregateId).to.eql(stream6[1].aggregateId);
                    expect(evts[1].commitStamp.getTime()).to.eql(stream6[1].commitStamp.getTime());
                    expect(evts[1].streamRevision).to.eql(stream6[1].streamRevision);
                    expect(evts[2].aggregateId).to.eql(stream9[0].aggregateId);
                    expect(evts[2].commitStamp.getTime()).to.eql(stream9[0].commitStamp.getTime());
                    expect(evts[2].streamRevision).to.eql(stream9[0].streamRevision);

                    done();
                  });

                });

                describe('and limit it with skip and limit', function () {

                  it('it should return the correct events', function (done) {

                    store.getEventsByRevision({ aggregateId: 'idWithAggrAndCont', context: 'myConttttt' }, 1, 2, function (err, evts) {
                      expect(err).not.to.be.ok();
                      expect(evts.length).to.eql(1);
                      expect(evts[0].aggregateId).to.eql(stream6[1].aggregateId);
                      expect(evts[0].commitStamp.getTime()).to.eql(stream6[1].commitStamp.getTime());
                      expect(evts[0].streamRevision).to.eql(stream6[1].streamRevision);

                      done();
                    });

                  });

                });

              });

            });

          });

          describe('adding some events', function () {

            var stream = [{
              aggregateId: 'id',
              streamRevision: 0,
              id: '119',
              commitId: '11119',
              commitStamp: new Date(Date.now() + 10),
              commitSequence: 0,
              payload: {
                event:'bla'
              },
              applyMappings: function () {}
            }, {
              aggregateId: 'id',
              streamRevision: 1,
              id: '120',
              commitId: '11119',
              commitStamp: new Date(Date.now() + 10),
              commitSequence: 1,
              payload: {
                event:'bla2'
              },
              applyMappings: function () {}
            }];

            beforeEach(function (done) {
              store.addEvents(stream, done);
            });

            describe('and requesting all undispatched events', function () {

              it('it should return the correct events', function (done) {

                store.getUndispatchedEvents(null, function (err, evts) {
                  expect(err).not.to.be.ok();
                  expect(evts.length).to.eql(2);
                  expect(evts[0].id).to.eql(stream[0].id);
                  expect(evts[0].commitId).to.eql(stream[0].commitId);
                  expect(evts[0].commitStamp.getTime()).to.eql(stream[0].commitStamp.getTime());
                  expect(evts[1].id).to.eql(stream[1].id);
                  expect(evts[1].commitId).to.eql(stream[1].commitId);
                  expect(evts[1].commitStamp.getTime()).to.eql(stream[1].commitStamp.getTime());

                  done();
                });

              });

            });

            describe('calling setEventToDispatched', function () {

              beforeEach(function (done) {
                store.getUndispatchedEvents(null, function (err, evts) {
                  expect(evts.length).to.eql(2);
                  done();
                });
              });

              it('it should work correctly', function (done) {

                store.setEventToDispatched('119', function (err) {
                  expect(err).not.to.be.ok();

                  store.getUndispatchedEvents(null, function (err, evts) {
                    expect(err).not.to.be.ok();
                    expect(evts.length).to.eql(1);
                    expect(evts[0].commitId).to.eql(stream[1].commitId);
                    expect(evts[0].commitStamp.getTime()).to.eql(stream[1].commitStamp.getTime());

                    done();
                  });
                });

              });

            });

          });

          describe('calling addSnapshot', function () {

            var snap = {
              id: '12345',
              aggregateId: '920193847',
              aggregate: 'myCoolAggregate',
              context: 'myEvenCoolerContext',
              commitStamp: new Date(Date.now() + 400),
              revision: 3,
              version: 1,
              data: {
                mySnappi: 'data'
              }
            };

            it('it should save the snapshot', function (done) {

              store.addSnapshot(snap, function (err) {
                expect(err).not.to.be.ok();

                store.getSnapshot({ aggregateId: snap.aggregateId }, -1 , function (err, shot) {
                  expect(err).not.to.be.ok();
                  expect(shot.id).to.eql(snap.id);
                  expect(shot.aggregateId).to.eql(snap.aggregateId);
                  expect(shot.aggregate).to.eql(snap.aggregate);
                  expect(shot.context).to.eql(snap.context);
                  expect(shot.commitStamp.getTime()).to.eql(snap.commitStamp.getTime());
                  expect(shot.revision).to.eql(snap.revision);
                  expect(shot.version).to.eql(snap.version);
                  expect(shot.data.mySnappi).to.eql(snap.data.mySnappi);

                  done();
                });
              });

            });

            describe('having some snapshots in the eventstore calling getSnapshot', function () {

              var snap1 = {
                id: '12345',
                aggregateId: '920193847',
                commitStamp: new Date(Date.now() + 405),
                revision: 3,
                version: 1,
                data: {
                  mySnappi: 'data'
                }
              };

              var snap2 = {
                id: '123456',
                aggregateId: '920193847',
                commitStamp: new Date(Date.now() + 410),
                revision: 8,
                version: 1,
                data: {
                  mySnappi: 'data2'
                }
              };

              var snap3 = {
                id: '1234567',
                aggregateId: '142351',
                aggregate: 'myCoolAggregate',
                context: 'conntttt',
                commitStamp: new Date(Date.now() + 420),
                revision: 5,
                version: 1,
                data: {
                  mySnappi: 'data2'
                }
              };

              var snap4 = {
                id: '12345678',
                aggregateId: '920193847',
                aggregate: 'myCoolAggregate',
                commitStamp: new Date(Date.now() + 430),
                revision: 9,
                version: 1,
                data: {
                  mySnappi: 'data6'
                }
              };

              var snap5 = {
                id: '123456789',
                aggregateId: '938179341',
                aggregate: 'myCoolAggregate',
                context: 'myCoolContext',
                commitStamp: new Date(Date.now() + 440),
                revision: 2,
                version: 1,
                data: {
                  mySnappi: 'dataXY'
                }
              };

              var snap6 = {
                id: '12345678910',
                aggregateId: '920193847',
                aggregate: 'myCoolAggregate2',
                context: 'myCoolContext',
                commitStamp: new Date(Date.now() + 450),
                revision: 12,
                version: 1,
                data: {
                  mySnappi: 'dataaaaa'
                }
              };

              var snap7 = {
                id: '123456789104',
                aggregateId: '920193847313131313',
                aggregate: 'myCoolAggregate2',
                context: 'myCoolContext',
                commitStamp: new Date(Date.now() + 555),
                revision: 16,
                version: 2,
                data: {
                  mySnappi: 'dataaaaa2'
                }
              };

              var snap8 = {
                id: '123456789102',
                aggregateId: '920193847313131313',
                aggregate: 'myCoolAggregate2',
                context: 'myCoolContext',
                commitStamp: new Date(Date.now() + 575),
                revision: 16,
                version: 3,
                data: {
                  mySnappi: 'dataaaaa3'
                }
              };

              beforeEach(function (done) {
                async.series([
                  function (callback) {
                    store.addSnapshot(snap1, callback);
                  },
                  function (callback) {
                    store.addSnapshot(snap2, callback);
                  },
                  function (callback) {
                    store.addSnapshot(snap3, callback);
                  },
                  function (callback) {
                    store.addSnapshot(snap4, callback);
                  },
                  function (callback) {
                    store.addSnapshot(snap5, callback);
                  },
                  function (callback) {
                    store.addSnapshot(snap6, callback);
                  },
                  function (callback) {
                    store.addSnapshot(snap7, callback);
                  },
                  function (callback) {
                    store.addSnapshot(snap8, callback);
                  }
                ], done);
              });

              describe('with an aggregateId being used only in one context and aggregate', function () {

                it('it should return the correct snapshot', function (done) {

                  store.getSnapshot({ aggregateId: '142351' }, -1, function (err, shot) {
                    expect(err).not.to.be.ok();
                    expect(shot.id).to.eql(snap3.id);
                    expect(shot.aggregateId).to.eql(snap3.aggregateId);
                    expect(shot.aggregate).to.eql(snap3.aggregate);
                    expect(shot.context).to.eql(snap3.context);
                    expect(shot.commitStamp.getTime()).to.eql(snap3.commitStamp.getTime());
                    expect(shot.revision).to.eql(snap3.revision);
                    expect(shot.version).to.eql(snap3.version);
                    expect(shot.data.mySnappi).to.eql(snap3.data.mySnappi);

                    done();
                  });

                });

                describe('and limit it with revMax', function () {

                  it('it should return the correct snapshot', function (done) {

                    store.getSnapshot({ aggregateId: '142351' }, 1, function (err, shot) {
                      expect(err).not.to.be.ok();
                      expect(shot).not.to.be.ok();

                      done();
                    });

                  });

                });

                describe('and an other revMax', function () {

                  it('it should return the correct snapshot', function (done) {

                    store.getSnapshot({ aggregateId: '142351' }, 5, function (err, shot) {
                      expect(err).not.to.be.ok();
                      expect(shot.id).to.eql(snap3.id);
                      expect(shot.aggregateId).to.eql(snap3.aggregateId);
                      expect(shot.aggregate).to.eql(snap3.aggregate);
                      expect(shot.context).to.eql(snap3.context);
                      expect(shot.commitStamp.getTime()).to.eql(snap3.commitStamp.getTime());
                      expect(shot.revision).to.eql(snap3.revision);
                      expect(shot.version).to.eql(snap3.version);
                      expect(shot.data.mySnappi).to.eql(snap3.data.mySnappi);

                      done();
                    });

                  });

                });

              });

              describe('with an aggregateId being used in an other context or aggregate', function () {

                it('it should return the correct snapshot', function (done) {

                  store.getSnapshot({ aggregateId: '920193847' }, -1, function (err, shot) {
                    expect(err).not.to.be.ok();
                    expect(shot.id).to.eql(snap6.id);
                    expect(shot.aggregateId).to.eql(snap6.aggregateId);
                    expect(shot.aggregate).to.eql(snap6.aggregate);
                    expect(shot.context).to.eql(snap6.context);
                    expect(shot.commitStamp.getTime()).to.eql(snap6.commitStamp.getTime());
                    expect(shot.revision).to.eql(snap6.revision);
                    expect(shot.version).to.eql(snap6.version);
                    expect(shot.data.mySnappi).to.eql(snap6.data.mySnappi);

                    done();
                  });

                });

                describe('and limit it with revMax', function () {

                  it('it should return the correct snapshot', function (done) {

                    store.getSnapshot({ aggregateId: '920193847' }, 1, function (err, shot) {
                      expect(err).not.to.be.ok();
                      expect(shot).not.to.be.ok();

                      done();
                    });

                  });

                });

                describe('and an other revMax', function () {

                  it('it should return the correct snapshot', function (done) {

                    store.getSnapshot({ aggregateId: '920193847' }, 5, function (err, shot) {
                      expect(err).not.to.be.ok();
                      expect(shot.id).to.eql(snap1.id);
                      expect(shot.aggregateId).to.eql(snap1.aggregateId);
                      expect(shot.aggregate).to.eql(snap1.aggregate);
                      expect(shot.context).to.eql(snap1.context);
                      expect(shot.commitStamp.getTime()).to.eql(snap1.commitStamp.getTime());
                      expect(shot.revision).to.eql(snap1.revision);
                      expect(shot.version).to.eql(snap1.version);
                      expect(shot.data.mySnappi).to.eql(snap1.data.mySnappi);

                      done();
                    });

                  });

                });

              });

              describe('with an aggregateId and with an aggregate', function () {

                it('it should return the correct snapshot', function (done) {

                  store.getSnapshot({ aggregateId: '920193847', aggregate: 'myCoolAggregate' }, -1, function (err, shot) {
                    expect(err).not.to.be.ok();
                    expect(shot.id).to.eql(snap4.id);
                    expect(shot.aggregateId).to.eql(snap4.aggregateId);
                    expect(shot.aggregate).to.eql(snap4.aggregate);
                    expect(shot.context).to.eql(snap4.context);
                    expect(shot.commitStamp.getTime()).to.eql(snap4.commitStamp.getTime());
                    expect(shot.revision).to.eql(snap4.revision);
                    expect(shot.version).to.eql(snap4.version);
                    expect(shot.data.mySnappi).to.eql(snap4.data.mySnappi);

                    done();
                  });

                });

                describe('and limit it with revMax', function () {

                  it('it should return the correct snapshot', function (done) {

                    store.getSnapshot({ aggregateId: '920193847', aggregate: 'myCoolAggregate' }, 1, function (err, shot) {
                      expect(err).not.to.be.ok();
                      expect(shot).not.to.be.ok();

                      done();
                    });

                  });

                });

                describe('and an other revMax', function () {

                  it('it should return the correct snapshot', function (done) {

                    store.getSnapshot({ aggregateId: '920193847', aggregate: 'myCoolAggregate' }, 9, function (err, shot) {
                      expect(err).not.to.be.ok();
                      expect(shot.id).to.eql(snap4.id);
                      expect(shot.aggregateId).to.eql(snap4.aggregateId);
                      expect(shot.aggregate).to.eql(snap4.aggregate);
                      expect(shot.context).to.eql(snap4.context);
                      expect(shot.commitStamp.getTime()).to.eql(snap4.commitStamp.getTime());
                      expect(shot.revision).to.eql(snap4.revision);
                      expect(shot.version).to.eql(snap4.version);
                      expect(shot.data.mySnappi).to.eql(snap4.data.mySnappi);

                      done();
                    });

                  });

                });

              });

              describe('with an aggregateId and with an aggregate and with a context', function () {

                it('it should return the correct snapshot', function (done) {

                  store.getSnapshot({ aggregateId: '938179341', aggregate: 'myCoolAggregate', context: 'myCoolContext' }, -1, function (err, shot) {
                    expect(err).not.to.be.ok();
                    expect(shot.id).to.eql(snap5.id);
                    expect(shot.aggregateId).to.eql(snap5.aggregateId);
                    expect(shot.aggregate).to.eql(snap5.aggregate);
                    expect(shot.context).to.eql(snap5.context);
                    expect(shot.commitStamp.getTime()).to.eql(snap5.commitStamp.getTime());
                    expect(shot.revision).to.eql(snap5.revision);
                    expect(shot.version).to.eql(snap5.version);
                    expect(shot.data.mySnappi).to.eql(snap5.data.mySnappi);

                    done();
                  });

                });

                describe('and limit it with revMax', function () {

                  it('it should return the correct snapshot', function (done) {

                    store.getSnapshot({ aggregateId: '938179341', aggregate: 'myCoolAggregate', context: 'myCoolContext' }, 1, function (err, shot) {
                      expect(err).not.to.be.ok();
                      expect(shot).not.to.be.ok();

                      done();
                    });

                  });

                });

                describe('and an other revMax', function () {

                  it('it should return the correct snapshot', function (done) {

                    store.getSnapshot({ aggregateId: '938179341', aggregate: 'myCoolAggregate', context: 'myCoolContext' }, 2, function (err, shot) {
                      expect(err).not.to.be.ok();
                      expect(shot.id).to.eql(snap5.id);
                      expect(shot.aggregateId).to.eql(snap5.aggregateId);
                      expect(shot.aggregate).to.eql(snap5.aggregate);
                      expect(shot.context).to.eql(snap5.context);
                      expect(shot.commitStamp.getTime()).to.eql(snap5.commitStamp.getTime());
                      expect(shot.revision).to.eql(snap5.revision);
                      expect(shot.version).to.eql(snap5.version);
                      expect(shot.data.mySnappi).to.eql(snap5.data.mySnappi);

                      done();
                    });

                  });

                });

              });

              describe('with an aggregateId and without an aggregate but with a context', function () {

                it('it should return the correct snapshot', function (done) {

                  store.getSnapshot({ aggregateId: '142351', context: 'conntttt' }, -1, function (err, shot) {
                    expect(err).not.to.be.ok();
                    expect(shot.id).to.eql(snap3.id);
                    expect(shot.aggregateId).to.eql(snap3.aggregateId);
                    expect(shot.aggregate).to.eql(snap3.aggregate);
                    expect(shot.context).to.eql(snap3.context);
                    expect(shot.commitStamp.getTime()).to.eql(snap3.commitStamp.getTime());
                    expect(shot.revision).to.eql(snap3.revision);
                    expect(shot.version).to.eql(snap3.version);
                    expect(shot.data.mySnappi).to.eql(snap3.data.mySnappi);

                    done();
                  });

                });

                describe('and limit it with revMax', function () {

                  it('it should return the correct snapshot', function (done) {

                    store.getSnapshot({ aggregateId: '142351', context: 'conntttt' }, 1, function (err, shot) {
                      expect(err).not.to.be.ok();
                      expect(shot).not.to.be.ok();

                      done();
                    });

                  });

                });

                describe('and an other revMax', function () {

                  it('it should return the correct snapshot', function (done) {

                    store.getSnapshot({ aggregateId: '142351', context: 'conntttt' }, 5, function (err, shot) {
                      expect(err).not.to.be.ok();
                      expect(shot.id).to.eql(snap3.id);
                      expect(shot.aggregateId).to.eql(snap3.aggregateId);
                      expect(shot.aggregate).to.eql(snap3.aggregate);
                      expect(shot.context).to.eql(snap3.context);
                      expect(shot.commitStamp.getTime()).to.eql(snap3.commitStamp.getTime());
                      expect(shot.revision).to.eql(snap3.revision);
                      expect(shot.version).to.eql(snap3.version);
                      expect(shot.data.mySnappi).to.eql(snap3.data.mySnappi);

                      done();
                    });

                  });

                });

              });

              describe('with a revision that already exists but with a newer version', function () {

                it('it should return the correct snapshot', function (done) {

                  store.getSnapshot({ aggregateId: '920193847313131313', aggregate: 'myCoolAggregate2', context: 'myCoolContext' }, -1, function (err, shot) {
                    expect(err).not.to.be.ok();
                    expect(shot.id).to.eql(snap8.id);
                    expect(shot.aggregateId).to.eql(snap8.aggregateId);
                    expect(shot.aggregate).to.eql(snap8.aggregate);
                    expect(shot.context).to.eql(snap8.context);
                    expect(shot.commitStamp.getTime()).to.eql(snap8.commitStamp.getTime());
                    expect(shot.revision).to.eql(snap8.revision);
                    expect(shot.version).to.eql(snap8.version);
                    expect(shot.data.mySnappi).to.eql(snap8.data.mySnappi);

                    done();
                  });

                });

              });

            });

          });

          describe('cleaning snapshots', function () {

            describe('having some snapshots in the eventstore calling cleanSnapshot', function () {

              var snap1 = {
                id: 'rev3',
                aggregateId: '920193847',
                aggregate: 'myCoolAggregate',
                context: 'myCoolContext',
                commitStamp: new Date(Date.now() + 405),
                revision: 3,
                version: 1,
                data: {
                  mySnappi: 'data'
                }
              };

              var snap2 = {
                id: 'rev4',
                aggregateId: '920193847',
                aggregate: 'myCoolAggregate',
                context: 'myCoolContext',
                commitStamp: new Date(Date.now() + 410),
                revision: 4,
                version: 1,
                data: {
                  mySnappi: 'data2'
                }
              };

              var snap3 = {
                id: 'rev5',
                aggregateId: '920193847',
                aggregate: 'myCoolAggregate',
                context: 'myCoolContext',
                commitStamp: new Date(Date.now() + 420),
                revision: 5,
                version: 1,
                data: {
                  mySnappi: 'data3'
                }
              };

              var snap4 = {
                id: 'rev9',
                aggregateId: '920193847',
                aggregate: 'myCoolAggregate',
                context: 'myCoolContext',
                commitStamp: new Date(Date.now() + 430),
                revision: 9,
                version: 1,
                data: {
                  mySnappi: 'data4'
                }
              };

              var snap5 = {
                id: 'rev10',
                aggregateId: '920193847',
                aggregate: 'myCoolAggregate',
                context: 'myCoolContext',
                commitStamp: new Date(Date.now() + 440),
                revision: 10,
                version: 1,
                data: {
                  mySnappi: 'dataXY'
                }
              };

              var snap6 = {
                id: 'rev12',
                aggregateId: '920193847',
                aggregate: 'myCoolAggregate',
                context: 'myCoolContext',
                commitStamp: new Date(Date.now() + 450),
                revision: 12,
                version: 1,
                data: {
                  mySnappi: 'dataaaaa'
                }
              };

              var snap7 = {
                id: 'rev16',
                aggregateId: '920193847',
                aggregate: 'myCoolAggregate',
                context: 'myCoolContext',
                commitStamp: new Date(Date.now() + 555),
                revision: 16,
                version: 1,
                data: {
                  mySnappi: 'dataaaaa2'
                }
              };

              var snap8 = {
                id: 'rev17',
                aggregateId: '920193847',
                aggregate: 'myCoolAggregate',
                context: 'myCoolContext',
                commitStamp: new Date(Date.now() + 575),
                revision: 17,
                version: 1,
                data: {
                  mySnappi: 'dataaaaa3'
                }
              };

              describe('with an aggregateId being used only in one context and aggregate', function () {

                describe('having fewer snapshots than the threshold', function() {

                  beforeEach(function (done) {
                    async.series([
                      function (callback) {
                        store.addSnapshot(snap1, callback);
                      },
                      function (callback) {
                        store.addSnapshot(snap2, callback);
                      },
                      function (callback) {
                        store.addSnapshot(snap3, callback);
                      },
                      function (callback) {
                        store.addSnapshot(snap4, callback);
                      }
                    ], done);
                  });

                  it('can be called without error', function(done) {

                    store.cleanSnapshots({
                      aggregateId: '920193847',
                      aggregate: 'myCoolAggregate',
                      context: 'myCoolContext'
                    }, function (err, cleanedCount) {
                      expect(err).not.to.be.ok();
                      expect(cleanedCount).to.equal(0);
                      done();
                    });

                  })
                })

                describe('having more snapshots than the threshold', function() {

                  beforeEach(function (done) {
                    async.series([
                      function (callback) {
                        store.addSnapshot(snap1, callback);
                      },
                      function (callback) {
                        store.addSnapshot(snap2, callback);
                      },
                      function (callback) {
                        store.addSnapshot(snap3, callback);
                      },
                      function (callback) {
                        store.addSnapshot(snap4, callback);
                      },
                      function (callback) {
                        store.addSnapshot(snap5, callback);
                      },
                      function (callback) {
                        store.addSnapshot(snap6, callback);
                      },
                      function (callback) {
                        store.addSnapshot(snap7, callback);
                      },
                      function (callback) {
                        store.addSnapshot(snap8, callback);
                      }
                    ], done);
                  });

                  it('it should clean oldest snapshots', function (done) {

                    store.cleanSnapshots({
                      aggregateId: '920193847',
                      aggregate: 'myCoolAggregate',
                      context: 'myCoolContext'
                    }, function (err, cleanedCount) {
                      expect(err).not.to.be.ok();
                      expect(cleanedCount).to.equal(3);
                      done();
                    });

                  });

                });

              });

            })

          });
        });
      });
    });

  });

});
```


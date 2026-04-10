# Knowledge Dump for akka-ddd

## File: .travis.yml
```
 language: scala

 scala:
   - "2.12.6"

 jdk:
   - oraclejdk8

 cache:
  directories:
    - $HOME/.ivy2/cache
    - $HOME/.sbt/boot

 before_cache:
    - find $HOME/.sbt -name "*.lock" | xargs rm
    - find $HOME/.ivy2 -name "ivydata-*.properties" | xargs rm

 branches:
  except:
  - docs

 script:
  - sbt test
  - sbt "it:test"

 sudo: required

 services:
   - docker

 install:
  - sudo apt-get update -qq
  - sudo apt-get install -y -qq httpie

 before_script:
  - docker run --name ecommerce-event-store -d -p 2113:2113 -p 1113:1113 newicom/eventstore
```

## File: license.md
```
The MIT License (MIT)

Copyright (c) 2014 Paweł Kaczor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

## File: README.md
```
akka-ddd [![Build Status](https://travis-ci.org/pawelkaczor/akka-ddd.svg?branch=master)](https://travis-ci.org/pawelkaczor/akka-ddd) [![Scala CI](https://github.com/pawelkaczor/akka-ddd/actions/workflows/scala.yml/badge.svg)](https://github.com/pawelkaczor/akka-ddd/actions/workflows/scala.yml) [![Version](https://img.shields.io/maven-central/v/pl.newicom.dddd/akka-ddd-core_2.12.svg?label=version)](http://search.maven.org/#search%7Cga%7C1%7Cg%3Apl.newicom.dddd)
========

[![Join the chat at https://gitter.im/pawelkaczor/akka-ddd](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/pawelkaczor/akka-ddd?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Akka-DDD is a framework for building distributed services following DDD/CQRS/ES architecture on top of the Akka platform. Thanks to the pluggable architecture of the Akka-Persistence, Akka-DDD is not tied to any particular event journal provider.

The services are built as actor systems. Different services can be distributed in the same cluster (Akka cluster) or can be deployed to independent clusters.

Akka-DDD offers concise APIs for implementing business logic of the following actor types:

- **Aggregate Root**
- **Process Manager**
- **Receptor**

All of these are **event-sourced** actors that support **reliable** (effectively-once delivery) communication. Process Managers and Receptors are operating within non-blocking **back-pressured** event processing pipeline.

Akka-DDD provides an extensible implementation of the View Update Service that is responsible for running running **Projections** on the read-side of the system. Implementation of SQL View Update Service is available out of the box.

Akka-DDD has been tested with the [EventStore](https://eventstore.org/) journal implementation. A [demo project](https://github.com/pawelkaczor/ddd-leaven-akka-v2) of an e-commerce system implemented using Akka-DDD is available on GitHub.

### Documentation

Project [homepage](http://newicom.pl/akka-ddd/).

[Documentation](http://newicom.pl/akka-ddd/docs/getting-started.html).

Articles in [Reactive DDD with Akka](http://pkaczor.blogspot.com/search/label/Reactive-DDD) series.

Demo [project](https://github.com/pawelkaczor/ddd-leaven-akka-v2).

```

## File: _GIT_INGEST.md
```
# OmniClaw Repo Plow: CIV_FETCHED_akka-ddd_183846



================================================
FILE: LICENSE.md
================================================
The MIT License (MIT)

Copyright (c) 2014 Paweł Kaczor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


================================================
FILE: README.md
================================================
akka-ddd [![Build Status](https://travis-ci.org/pawelkaczor/akka-ddd.svg?branch=master)](https://travis-ci.org/pawelkaczor/akka-ddd) [![Scala CI](https://github.com/pawelkaczor/akka-ddd/actions/workflows/scala.yml/badge.svg)](https://github.com/pawelkaczor/akka-ddd/actions/workflows/scala.yml) [![Version](https://img.shields.io/maven-central/v/pl.newicom.dddd/akka-ddd-core_2.12.svg?label=version)](http://search.maven.org/#search%7Cga%7C1%7Cg%3Apl.newicom.dddd)
========

[![Join the chat at https://gitter.im/pawelkaczor/akka-ddd](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/pawelkaczor/akka-ddd?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Akka-DDD is a framework for building distributed services following DDD/CQRS/ES architecture on top of the Akka platform. Thanks to the pluggable architecture of the Akka-Persistence, Akka-DDD is not tied to any particular event journal provider.

The services are built as actor systems. Different services can be distributed in the same cluster (Akka cluster) or can be deployed to independent clusters.

Akka-DDD offers concise APIs for implementing business logic of the following actor types:

- **Aggregate Root**
- **Process Manager**
- **Receptor**

All of these are **event-sourced** actors that support **reliable** (effectively-once delivery) communication. Process Managers and Receptors are operating within non-blocking **back-pressured** event processing pipeline.

Akka-DDD provides an extensible implementation of the View Update Service that is responsible for running running **Projections** on the read-side of the system. Implementation of SQL View Update Service is available out of the box.

Akka-DDD has been tested with the [EventStore](https://eventstore.org/) journal implementation. A [demo project](https://github.com/pawelkaczor/ddd-leaven-akka-v2) of an e-commerce system implemented using Akka-DDD is available on GitHub.

### Documentation

Project [homepage](http://newicom.pl/akka-ddd/).

[Documentation](http://newicom.pl/akka-ddd/docs/getting-started.html).

Articles in [Reactive DDD with Akka](http://pkaczor.blogspot.com/search/label/Reactive-DDD) series.

Demo [project](https://github.com/pawelkaczor/ddd-leaven-akka-v2).


================================================
FILE: akka-ddd-scheduling\src\main\resources\clock-metadata.json
================================================
{
  "$maxCount": 1
}


================================================
FILE: akka-ddd-scheduling\src\main\resources\clock.js
================================================
/*
 Emit 1 tick per minute (assuming --stats-period-sec is not changed (default 30) or set to value lower than 60)
 */
fromStream('$stats-0.0.0.0:2113').
    when({
        '$init' : function(s,e) {
            return { "timeMillis": new Date().getTime() };
        },
        '$statsCollected' : function(s,e) {
            var time = new Date();
            var timeMillis = time.getTime();
            if (s.timeMillis < timeMillis) {
                s.timeMillis = timeMillis;
                emit('clock', 'tick', { "time": time, "timeMillis": timeMillis});
            }
        }
    });

================================================
FILE: akka-ddd-scheduling\src\main\resources\current-deadlines.js
================================================
fromStreams(['clock', 'deadlines']).
when({
    '$init' : function(s,e) {
        return { "deadlines": []}
    },
    'pl.newicom.dddd.scheduling.EventScheduled' : function(s,e) {
        s.deadlines[s.deadlines.length] = e;
    },
    'tick' : function(s,e) {
        for(var i = s.deadlines.length -1; i >= 0; i--) {
            var eventScheduledEnvelope = s.deadlines[i];

            var eventScheduledMetadata = JSON.parse(eventScheduledEnvelope.metadataRaw);
            var eventScheduled = JSON.parse(eventScheduledEnvelope.bodyRaw);

            var deadlineMillis = eventScheduled.payload.metadata.deadlineMillis;
            var currentTimeMillis = JSON.parse(e.bodyRaw).timeMillis;
            var businessUnit = eventScheduled.payload.metadata.businessUnit;
            var target = eventScheduled.payload.metadata.target;

            var deadlineEventPayload = eventScheduled.payload.event;
            var deadlineEventClass = eventScheduled.payload.eventClass;

            var deadlineEvent = eventScheduled;
            deadlineEvent.payload = deadlineEventPayload;
            deadlineEvent.payload.jsonClass = deadlineEventClass;

            var deadlineEventMetadata = eventScheduledMetadata;
            deadlineEventMetadata.content.target = target;

            if (currentTimeMillis >= deadlineMillis) {
                s.deadlines.splice(i, 1);
                emit('currentDeadlines-' + businessUnit, deadlineEventClass, deadlineEvent, deadlineEventMetadata);
            }
        }
    }
});

================================================
FILE: eventstore-akka-persistence\src\main\resources\tags.js
================================================
fromAll()
    .when({
        $any: function(s,e){
            if (!e.linkMetadataRaw && e.metadataRaw && e.metadataRaw.includes("tags")) {
                var md = JSON.parse(e.metadataRaw);
                if (md.content && md.content.tags) {
                    var tags = md.content.tags;
                    for (var i = 0; i < tags.length; i++) {
                        linkTo(tags[i], e);
                    }
                }
            }
        }
    })
```

## File: .github\workflows\scala.yml
```
name: Scala CI

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up JDK 11
      uses: actions/setup-java@v2
      with:
        java-version: '11'
        distribution: 'adopt'
    - name: Run tests
      run: sbt test

```

## File: akka-ddd-scheduling\src\main\resources\clock-metadata.json
```
{
  "$maxCount": 1
}

```

## File: akka-ddd-scheduling\src\main\resources\clock.js
```
/*
 Emit 1 tick per minute (assuming --stats-period-sec is not changed (default 30) or set to value lower than 60)
 */
fromStream('$stats-0.0.0.0:2113').
    when({
        '$init' : function(s,e) {
            return { "timeMillis": new Date().getTime() };
        },
        '$statsCollected' : function(s,e) {
            var time = new Date();
            var timeMillis = time.getTime();
            if (s.timeMillis < timeMillis) {
                s.timeMillis = timeMillis;
                emit('clock', 'tick', { "time": time, "timeMillis": timeMillis});
            }
        }
    });
```

## File: akka-ddd-scheduling\src\main\resources\current-deadlines.js
```
fromStreams(['clock', 'deadlines']).
when({
    '$init' : function(s,e) {
        return { "deadlines": []}
    },
    'pl.newicom.dddd.scheduling.EventScheduled' : function(s,e) {
        s.deadlines[s.deadlines.length] = e;
    },
    'tick' : function(s,e) {
        for(var i = s.deadlines.length -1; i >= 0; i--) {
            var eventScheduledEnvelope = s.deadlines[i];

            var eventScheduledMetadata = JSON.parse(eventScheduledEnvelope.metadataRaw);
            var eventScheduled = JSON.parse(eventScheduledEnvelope.bodyRaw);

            var deadlineMillis = eventScheduled.payload.metadata.deadlineMillis;
            var currentTimeMillis = JSON.parse(e.bodyRaw).timeMillis;
            var businessUnit = eventScheduled.payload.metadata.businessUnit;
            var target = eventScheduled.payload.metadata.target;

            var deadlineEventPayload = eventScheduled.payload.event;
            var deadlineEventClass = eventScheduled.payload.eventClass;

            var deadlineEvent = eventScheduled;
            deadlineEvent.payload = deadlineEventPayload;
            deadlineEvent.payload.jsonClass = deadlineEventClass;

            var deadlineEventMetadata = eventScheduledMetadata;
            deadlineEventMetadata.content.target = target;

            if (currentTimeMillis >= deadlineMillis) {
                s.deadlines.splice(i, 1);
                emit('currentDeadlines-' + businessUnit, deadlineEventClass, deadlineEvent, deadlineEventMetadata);
            }
        }
    }
});
```

## File: eventstore-akka-persistence\src\main\resources\tags.js
```
fromAll()
    .when({
        $any: function(s,e){
            if (!e.linkMetadataRaw && e.metadataRaw && e.metadataRaw.includes("tags")) {
                var md = JSON.parse(e.metadataRaw);
                if (md.content && md.content.tags) {
                    var tags = md.content.tags;
                    for (var i = 0; i < tags.length; i++) {
                        linkTo(tags[i], e);
                    }
                }
            }
        }
    })
```


---
id: pprof
type: knowledge
owner: OA_Triage
---
# pprof
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "@datadog/pprof",
  "version": "6.0.0-pre",
  "description": "pprof support for Node.js",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/DataDog/pprof-nodejs.git"
  },
  "main": "out/src/index.js",
  "types": "out/src/index.d.ts",
  "scripts": {
    "build:asan": "node-gyp configure build --jobs=max --address_sanitizer",
    "build:tsan": "node-gyp configure build --jobs=max --thread_sanitizer",
    "build": "node-gyp configure build --jobs=max",
    "codecov": "nyc report --reporter=json && codecov -f coverage/*.json",
    "compile": "tsc -p .",
    "fix": "gts fix",
    "format": "clang-format --style file -i --glob='bindings/**/*.{h,hh,cpp,cc}'",
    "install": "exit 0",
    "lint": "jsgl --local . && gts check && clang-format --style file -n -Werror --glob='bindings/**/*.{h,hh,cpp,cc}'",
    "prepare": "npm run compile && npm run rebuild",
    "pretest:js-asan": "npm run compile && npm run build:asan",
    "pretest:js-tsan": "npm run compile && npm run build:tsan",
    "pretest:js-valgrind": "npm run pretest",
    "pretest": "npm run compile",
    "rebuild": "node-gyp rebuild --jobs=max",
    "test:cpp": "node scripts/cctest.js",
    "test:js-asan": "LSAN_OPTIONS='suppressions=./suppressions/lsan_suppr.txt' LD_PRELOAD=`gcc -print-file-name=libasan.so` mocha out/test/test-*.js",
    "test:js-tsan": "LD_PRELOAD=`gcc -print-file-name=libtsan.so` mocha out/test/test-*.js",
    "test:js-valgrind": "valgrind --leak-check=full mocha out/test/test-*.js",
    "test:js": "nyc mocha -r source-map-support/register out/test/test-*.js",
    "test": "npm run test:js"
  },
  "author": {
    "name": "Google Inc."
  },
  "license": "Apache-2.0",
  "dependencies": {
    "node-gyp-build": "<4.0",
    "pprof-format": "^2.2.1",
    "source-map": "^0.7.4"
  },
  "devDependencies": {
    "@types/mocha": "^10.0.1",
    "@types/node": "25.5.0",
    "@types/semver": "^7.5.8",
    "@types/sinon": "^21.0.0",
    "@types/tmp": "^0.2.3",
    "clang-format": "^1.8.0",
    "codecov": "^3.8.3",
    "deep-copy": "^1.4.2",
    "eslint-plugin-n": "^17.24.0",
    "gts": "^7.0.0",
    "js-green-licenses": "^4.0.0",
    "mocha": "^11.7.5",
    "nan": "^2.26.2",
    "nyc": "^18.0.0",
    "semver": "^7.7.4",
    "sinon": "^21.0.3",
    "source-map-support": "^0.5.21",
    "tmp": "0.2.5",
    "typescript": "^5.9.3"
  },
  "files": [
    "out/src",
    "out/third_party/cloud-debug-nodejs",
    "proto",
    "package-lock.json",
    "package.json",
    "README.md",
    "scripts/preinstall.js",
    "scripts/require-package-json.js",
    "scripts/should_rebuild.js",
    "prebuilds"
  ],
  "nyc": {
    "exclude": [
      "proto",
      "out/test",
      "out/system-test"
    ]
  },
  "engines": {
    "node": ">=16"
  },
  "//": "Temporary fix to make nan@2.22.2 work with Node 24",
  "postinstall": "sed -i '' 's/^.* Holder() const.*//' ./node_modules/nan/nan_callbacks_12_inl.h"
}

```

### File: README.md
```md
# pprof support for Node.js

[![NPM Version][npm-image]][npm-url]
[![Build Status][build-image]][build-url]
[![Known Vulnerabilities][snyk-image]][snyk-url]

[pprof][pprof-url] support for Node.js.

## Prerequisites
1. Your application will need to be using Node.js 18 or greater.

2. The `pprof` module has a native component that is used to collect profiles
with v8's CPU and Heap profilers. You may need to install additional
dependencies to build this module.
    * `pprof` has prebuilt binaries available for Linux arm64/x64,
    Alpine Linux x64, macOS arm64/x64, and Windows x64 for Node 18/20/22/24/25.
    No additional dependencies are required.
    * For other environments: on environments that `pprof` does not have
    prebuilt binaries for, the module
    [`node-gyp`](https://www.npmjs.com/package/node-gyp) will be used to
    build binaries. See `node-gyp`'s
    [documentation](https://github.com/nodejs/node-gyp#installation)
    for information on dependencies required to build binaries with `node-gyp`.

3. The [`pprof`][pprof-url] CLI can be used to view profiles collected with
this module. Instructions for installing the `pprof` CLI can be found
[here][pprof-install-url].

## Basic Set-up

Install [`pprof`][npm-url] with `npm` or add to your `package.json`.
  ```sh
  # Install through npm while saving to the local 'package.json'
  npm install --save @datadog/pprof
  ```

## Using the Profiler

### Collect a Wall Time Profile

#### In code:
1. Update code to collect and save a profile:
    ```javascript
    const profile = await pprof.time.profile({
      durationMillis: 10000,    // time in milliseconds for which to
                                // collect profile.
    });
    const buf = await pprof.encode(profile);
    fs.writeFile('wall.pb.gz', buf, (err) => {
      if (err) throw err;
    });
    ```

2. View the profile with command line [`pprof`][pprof-url]:
    ```sh
    pprof -http=: wall.pb.gz
    ```

#### Requiring from the command line

1. Start program from the command line:
    ```sh
    node --require @datadog/pprof app.js
    ```

2. A wall time profile for the job will be saved in
`pprof-profile-${process.pid}.pb.gz`. View the profile with command line
[`pprof`][pprof-url]:
    ```sh
    pprof -http=: pprof-profile-${process.pid}.pb.gz
    ```

### Collect a Heap Profile
1. Enable heap profiling at the start of the application:
    ```javascript
    // The average number of bytes between samples.
    const intervalBytes = 512 * 1024;

    // The maximum stack depth for samples collected.
    const stackDepth = 64;

    heap.start(intervalBytes, stackDepth);
    ```
2. Collect heap profiles:

    * Collecting and saving a profile in profile.proto format:
        ```javascript
        const profile = await pprof.heap.profile();
        const buf = await pprof.encode(profile);
        fs.writeFile('heap.pb.gz', buf, (err) => {
          if (err) throw err;
        })
        ```

    * View the profile with command line [`pprof`][pprof-url].
        ```sh
        pprof -http=: heap.pb.gz
        ```

    * Collecting a heap profile with V8 allocation profile format:
        ```javascript
          const profile = pprof.heap.v8Profile(pprof.heap.convertProfile);
        ```
        `v8Profile` accepts a callback and returns its result. Allocation nodes
        are only valid during the callback, so copy/transform what you need
        before returning. `heap.convertProfile` performs that conversion during
        the callback, and `heap.profile()` uses it under the hood.

[build-image]: https://github.com/Datadog/pprof-nodejs/actions/workflows/build.yml/badge.svg?branch=main
[build-url]: https://github.com/Datadog/pprof-nodejs/actions/workflows/build.yml
[npm-image]: https://badge.fury.io/js/@datadog%2Fpprof.svg
[npm-url]: https://npmjs.org/package/@datadog/pprof
[pprof-url]: https://github.com/google/pprof
[pprof-install-url]: https://github.com/google/pprof#building-pprof
[snyk-image]: https://snyk.io/test/github/Datadog/pprof-nodejs/badge.svg
[snyk-url]: https://snyk.io/test/github/Datadog/pprof-nodejs

```

### File: .prettierrc.js
```js
// Copyright 2020 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      https://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

module.exports = {
  endOfLine: 'auto',
  ...require('gts/.prettierrc.json'),
};

```

### File: codecov.yaml
```yaml
ignore:
    proto

```

### File: CONTRIBUTING.md
```md
# How to become a contributor and submit your own code

**Table of contents**

* [Contributor License Agreements](#contributor-license-agreements)
* [Contributing a patch](#contributing-a-patch)
* [Running the tests](#running-the-tests)
* [Releasing the library](#releasing-the-library)

## Contributor License Agreements

We'd love to accept your sample apps and patches! Before we can take them, we
have to jump a couple of legal hurdles.

Please fill out either the individual or corporate Contributor License Agreement
(CLA).

  * If you are an individual writing original source code and you're sure you
    own the intellectual property, then you'll need to sign an [individual CLA](https://developers.google.com/open-source/cla/individual).
  * If you work for a company that wants to allow you to contribute your work,
    then you'll need to sign a [corporate CLA](https://developers.google.com/open-source/cla/corporate).

Follow either of the two links above to access the appropriate CLA and
instructions for how to sign and return it. Once we receive it, we'll be able to
accept your pull requests.

## Contributing A Patch

1.  Submit an issue describing your proposed change to the repo in question.
1.  The repo owner will respond to your issue promptly.
1.  If your proposed change is accepted, and you haven't already done so, sign a
    Contributor License Agreement (see details above).
1.  Fork the desired repo, develop and test your code changes.
1.  Ensure that your code adheres to the existing style in the code to which
    you are contributing.
1.  Ensure that your code has an appropriate set of tests which all pass.
1.  Submit a pull request.

## Running the tests

1.  [Prepare your environment for Node.js setup][setup].

1.  Install dependencies:
    ```sh
    npm install
    ```

1.  Run the tests:
    ```sh
    npm test
    ```

1.  Lint (and maybe fix) any changes:
    ```sh
    npm run fix
    ```

[setup]: https://cloud.google.com/nodejs/docs/setup

# Running the system test
The system test starts a simple benchmark, uses this module to collect a time
and a heap profile, and verifies that the profiles contain functions from 
within the benchmark. 

To run the system test, [golang](https://golang.org/) must be installed.

The following command can be used to run the system test with all supported
versions of Node.JS:
```sh
sh system-test/system_test.sh
```

To run the system test with the v8 canary build, use:
```sh
RUN_ONLY_V8_CANARY_TEST=true sh system-test/system_test.sh
```
```

### File: eslint.config.js
```js
'use strict';
const gts = require('./node_modules/gts');

module.exports = [
  {
    ignores: [
      '**/node_modules',
      '**/coverage',
      'build/**',
      'proto/**',
      'out/**',
      'benchmark/**',
      'scripts/**',
      'system-test/**',
      'test.ts',
    ],
  },
  ...gts,
];

```

### File: renovate.json
```json
{
  "extends": [
    "config:base",
    ":preserveSemverRanges",
    ":pinDigestsDisabled"
  ],
  "packageRules": [
    {
      "extends": "packages:linters",
      "groupName": "linters"
    }
  ]
}

```

### File: tsconfig.json
```json
{
  "extends": "./node_modules/gts/tsconfig-google.json",
  "compilerOptions": {
    "rootDir": "ts",
    "outDir": "out",
    "target": "es2020",
    "esModuleInterop": true,
  },
  "include": [
    "ts/**/*.ts"
  ],
  "exclude": [
    "node_modules"
  ]
}

```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
**What does this PR do?**:
<!-- A brief description of the change being made with this pull request. -->

**Motivation**:
<!-- What inspired you to submit this pull request? -->

**Additional Notes**:
<!-- Anything else we should know when reviewing? -->

**How to test the change?**:
<!--
Describe here how the change can be validated.
You are strongly encouraged to provide automated tests for this PR (unit or integration).
If this change cannot be feasibly tested, please explain why,
unless the change does not modify code (e.g. only modifies docs, comments).
-->



```

### File: doc\sample_context_in_cped.md
```md
# Storing Sample Context in V8 Continuation-Preserved Embedder Data

## What is the Sample Context?
Datadog's Node.js profiler has the ability to store a custom object that it will
then associate with collected CPU samples. We refer to this object as the
"sample context." A higher-level embedding (typically, dd-trace-js) will then
update the sample context to keep it current with changes in the execution. A
typical piece of data sample context stores is the tracing span ID, so whenever
it changes, the sample context needs to be updated.

## How is the Sample Context stored and updated?
Before Node 22.7, the sample context would be stored in a
`std::shared_ptr<v8::Global<v8::Value>>` field on the C++ `WallProfiler`
instance. Due to it being a single piece of instance state, it had to be updated
every time the active span changed, possibly on every invocation of
`AsyncLocalStorage.enterWith` and `.run`, but even more importantly on every
async context change, and for that we needed to register a "before" callback
with `async_hooks.createHook`. This meant that we needed to both update the
sample context on every async context change, but more importantly it also meant
we needed to use `async_hooks.createHook` which is getting deprecated in Node.
Current documentation for it is not exactly a shining endorsement:
> Please migrate away from this API, if you can. We do not recommend using the
> createHook, AsyncHook, and executionAsyncResource APIs as they have usability
> issues, safety risks, and performance implications.

Fortunately, first the V8 engine and then Node.js gave us building blocks for a
better solution.

## V8 Continuation-Preserved Embedder Data and Node.js Async Context Frame
In the V8 engine starting from version 12 (the one shipping with Node 22)
`v8::Isolate` exposes an API to set and get embedder-specific data on it so that
it is preserved across executions that are logical continuations of each other
(essentially: across promise chains; this includes await expressions.) Even
though the APIs are exposed on the isolate, the data is stored on a
per-continuation basis and the engine takes care to return the right one when
`Isolate::GetContinuationPreservedEmbedderData()` method is invoked. We will
refer to continuation-preserved embedder data as "CPED" from now on.

Starting with Node.js 22.7, CPED is used to implement data storage behind
Node.js `AsyncLocalStorage` API. This dovetails nicely with our needs as all the
span-related data we set on the sample context is normally managed in an async
local storage (ALS) by the tracer. An application can create any number of
ALSes, and each ALS manages a single value per async context. This value is
somewhat confusingly called the "store" of the async local storage, making it
important to not confuse the terms "storage" (an identity with multiple values,
one per async context) and "store", which is a value of a storage within a
particular async context.

The new implementation for storing ALS stores introduces an internal Node.js
class named `AsyncContextFrame` (ACF) which is a subclass of JavaScript Map
class that uses ALSes as keys and their stores as the map values, essentially
providing a mapping from an ALS to its store in the current async context. (This
implementation is very similar to how e.g. Java implements `ThreadLocal`, which
is a close analogue to ALS in Node.js.) ACF instances are then stored in CPED.

## Storing the Sample Context in CPED
Node.js – as the embedder of V8 – commandeers the CPED to store instances of
ACF in it. This means that our profiler can't directly store our sample context
in the CPED, because then we'd overwrite the ACF reference already in there and
break Node.js. Fortunately, since ACF is "just" an ordinary JavaScript Map,
we can store our sample context in it as a key-value pair! When a new ACF is
created (normally, through `AsyncLocalStorage.enterWith`), all key-value pairs
are copied into the new map, so our sample context is nicely propagated.
Our logic for storing the sample context thus becomes:
* get the CPED from the V8 isolate
* if it is not a Map, do nothing (we can't set the sample context)
* otherwise set the sample context as a value in the map with our key.

It's worth noting that our key is just an ordinary empty JavaScript object
created internally by the profiler. We could've also passed it an externally
created `AsyncLocalStorage` instance, thus preserving the invariant that all
keys in an ACF are ALS instances, but this doesn't seem necessary.

We use a mutex implemented as an atomic boolean to guard our writes to the map.
The JavaScript code for AsyncContextFrame/AsyncLocalStorage treats the maps as
immutable. Whenever a new AsyncLocalStorage is added to the map, or even its
store value changes, the AsyncContextFrame map is copied into a new instance,
the change effected there, and the CPED reference in the isolate updated to the
new map. This means that for uncoordinated changes in JavaScript, we thankfully
require no guard. We only need to ensure we're guarding our own writes to the
map, which are the only in-place mutation of it. (Even we could've performed a
copy, but it feels excessive.)

Internally, we hold on to the sample context value with a shared pointer to a
V8 `Global`:
```
using ContextPtr = std::shared_ptr<v8::Global<v8::Value>>;
```

The values we store in ACF need to be JavaScript values. We use Node.js
`WrapObject` class for this purpose – it allows defining C++ classes that have
a JavaScript "mirror" object, carry a pointer to their C++ object in an internal
field, and when the JS object is garbage collected, the C++ object is destroyed.
Our `WrapObject` subclass in named `PersistentContextPtr` (PCP) because it has
only one field – the above introduced `ContextPtr`, and it is "persistent"
because its lifecycle is bound to that of its representative JavaScript object.

So the more detailed algorithm for setting a sample context is:
* get the CPED from the V8 isolate
* if it is not a Map, do nothing (we can't set the sample context)
* if sample context is undefined, delete the key (if it exists) from the map
* if sample context is a different value, create a new `PersistentContextPtr`
  wrapped in a JS object, and set the JS object as the value with the key in the
  map.

The chain of data now looks something like this:
```
v8::Isolate (from Isolate::GetCurrent())
 +-> current continuation (internally managed by V8)
   +-> node::AsyncContextFrame (in continuation's CPED field)
    +-> Object (the PersistentContextPtr wrapper, associated with our key)
     +-> dd::PersistentContextPtr (pointed in Object's internal field)
      +-> ContextPtr (in `context` field)
       +-> v8::Global (in shared_ptr)
        +-> v8::Value (the actual sample context object)
```
The last 3-4 steps were the same in the previous code version as well, except
there we used a field directly in the `WallProfiler`:
```
dd::WallProfiler
 +-> ContextPtr (in `curContext_` field)
  +-> v8::Global (in shared_ptr)
   +-> v8::Value (the actual sample context object)
```
The difference between the two diagrams shows how we moved the ContextPtr from
being a single instance state of `WallProfiler` to being an element in ACF maps.

## Looking up values in a signal handler
The signal handler unfortunately can't directly call any V8 APIs, so in order to
traverse the chain of data above, it relies on some pointer arithmetic and
structure definition. Every `Global` and `Local` have one field, and `Address*`.
Thus, to dereference the actual memory location of a JS object represented by a
global reference `ref`, we use `**<reinterpret_cast>(Address**)(&ref)`. These
addresses are _tagged_, meaning their LSB is set to 1, and need to be masked to
obtain the actual memory address. We can safely get the current Isolate pointer,
but then we need to interpret as an address the memory location at an internal
offset where it keeps the current CPED. If it's a JS Map, then we need to
retrieve from it a pointer to its `OrderedHashMap`, and then know its memory
layout to find the right hash bucket and traverse the linked list until we find
a key-value pair where the key address is our key object's current address (this
can be moved around by the GC, so that's why our Global is an `Address*`, for
a sufficient number of indirections to keep up with the moves.) The algorithm
for executing an equivalent of a `Map.get()` with knowledge of the V8 object
memory layouts is encapsulated in `map-get.cc`. We define C++ structs that
describe V8 internal `JSMap`, `FixedArray`, `OrderedHashMap` and
`SmallOrderedHashMap` structures, treat the memory pointed to by those pointers
as if they were these data structures (because they are), and read from them. If
in the future V8 changes these structures, we wil also need to adapt.
Unfortunately V8 doesn't export definitions of these data structures in a
publicly accessible header.

## Odds and ends
And that's mostly it! There are few more small odds and ends to make it work
safely. As we mentioned above, we're preventing the signal handler from reading
if we're just writing the value using an atomic boolean. We also register GC
prologue and epilogue callbacks with the V8 isolate so we can know when GCs are
ongoing and the signal handler will also refrain from touching memory while a GC
runs. We'll however grab the current sample context from the CPED
and store it in a profiler instance field in the GC prologue and use it for any
samples taken during GC.

Speaking of GC, we can now have an unbounded number of PersistentContextPtr
objects – one for each live ACF. Each PCP is allocated on the C++ heap, and
needs to be deleted eventually. The profiler tracks every PCP it creates in an
internal set of live PCPs and deletes them all when it itself gets disposed.
This is combined with `WrapObject` having GC finalization callback for every
PCP. When V8 collects a PCP wrapper its finalization callback will delete the
PCP.

## Changes in dd-trace-js
For completeness, we'll describe the changes in dd-trace-js here as well. The
main change is that with Node 24, we no longer require async hooks. The
instrumentation point for `AsyncLocalStorage.enterWith` is the only one
remaining (`AsyncLocalStorage.run` is implemented in terms of `enterWith`.)
We can further optimize and _not_ set the sample context object if we see it's
the same as the current one (because `enterWith` was run without setting a new
span as the current span.)

There are some small performance optimizations that no longer apply with the new
approach, though. For one, with the old approach we did some data conversions
(span IDs to string, a tag array to endpoint string) in a sample context when a
sample was captured. With the new approach, we do these conversions for all
sample contexts during profile serialization. Doing them after each sample
capture amortized their cost possibly minimally reducing the latency induced at
serialization time. With the old approach we also called `SetContext` only once
per sampling – we'd install a sample context to be used for the next sample, and
then kept updating a `ref` field in it with a reference to the actual data.
Since we no longer have a single sample context (but rather one per
continuation) we can not do this anymore, and we need to call `SetContext`
either every time `enterWith` runs, or only when we notice that the relevant
span data changed.
The cost of this (basically, going into a native call from JavaScript) are still
well offset by not having to use async hooks and do work on every async context
change. We could arguably even simplify the code by removing those small
optimizations.

```

### File: scripts\cctest.js
```js
'use strict'

const { execSync } = require('child_process')
const { existsSync } = require('fs')
const { join } = require('path')

const name = process.argv[2] || 'test_dd_pprof'

const cmd = [
  'node-gyp',
  'configure',
  'build',
  '--build_tests'
].join(' ')

execSync(cmd, { stdio: [0, 1, 2] })

function findBuild (mode) {
  const path = join(__dirname, '..', 'build', mode, name) + '.node'
  if (!existsSync(path)) {
    // eslint-disable-next-line no-console
    console.warn(`No ${mode} binary found for ${name} at: ${path}`)
    return
  }
  return path
}

const path = findBuild('Release') || findBuild('Debug')
if (!path) {
  // eslint-disable-next-line no-console
  console.error(`No ${name} build found`)
  process.exitCode = 1
} else {
  execSync(`node ${path}`, { stdio: [0, 1, 2] })
}

```

### File: tools\publish.sh
```sh
#!/bin/bash

# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

. $(dirname $0)/retry.sh

set -eo pipefail

# Install desired version of Node.js
retry curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash >/dev/null
export NVM_DIR="$HOME/.nvm" >/dev/null
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" >/dev/null

retry nvm install 10 &>/dev/null

cd $(dirname $0)/..

NPM_TOKEN=$(cat $KOKORO_KEYSTORE_DIR/72935_pprof-npm-token)
echo "//wombat-dressing-room.appspot.com/:_authToken=${NPM_TOKEN}" > ~/.npmrc

retry npm install --quiet
npm publish --access=public \
    --registry=https://wombat-dressing-room.appspot.com

```

### File: tools\retry.sh
```sh
#!/bin/bash

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
retry() {
  for attempt in {1..3}; do
    [ $attempt == 1 ] || sleep 10  # Backing off after a failed attempt.
    "${@}" && return 0
  done
  return 1
}

```

### File: .github\chainguard\self.github.release.push-tags.sts.yaml
```yaml
issuer: https://token.actions.githubusercontent.com

subject: repo:DataDog/pprof-nodejs:environment:npm

claim_pattern:
  event_name: push
  job_workflow_ref: DataDog/pprof-nodejs/\.github/workflows/release\.yml@refs/heads/v[0-9]+\.x
  ref: refs/heads/v[0-9]+\.x
  repository: DataDog/pprof-nodejs

permissions:
  contents: write

```

### File: ts\src\heap-profiler-bindings.ts
```ts
/**
 * Copyright 2018 Google Inc. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import * as path from 'path';

import {AllocationProfileNode} from './v8-types';

const findBinding = require('node-gyp-build');
const profiler = findBinding(path.join(__dirname, '..', '..'));

// Wrappers around native heap profiler functions.

export function startSamplingHeapProfiler(
  heapIntervalBytes: number,
  heapStackDepth: number,
) {
  profiler.heapProfiler.startSamplingHeapProfiler(
    heapIntervalBytes,
    heapStackDepth,
  );
}

export function stopSamplingHeapProfiler() {
  profiler.heapProfiler.stopSamplingHeapProfiler();
}

export function mapAllocationProfile<T>(
  callback: (root: AllocationProfileNode) => T,
): T {
  return profiler.heapProfiler.mapAllocationProfile(callback);
}

export type NearHeapLimitCallback = (profile: AllocationProfileNode) => void;

export function monitorOutOfMemory(
  heapLimitExtensionSize: number,
  maxHeapLimitExtensionCount: number,
  dumpHeapProfileOnSdterr: boolean,
  exportCommand: Array<string> | undefined,
  callback: NearHeapLimitCallback | undefined,
  callbackMode: number,
  isMainThread: boolean,
) {
  profiler.heapProfiler.monitorOutOfMemory(
    heapLimitExtensionSize,
    maxHeapLimitExtensionCount,
    dumpHeapProfileOnSdterr,
    exportCommand,
    callback,
    callbackMode,
    isMainThread,
  );
}

```

### File: ts\src\heap-profiler.ts
```ts
/**
 * Copyright 2017 Google Inc. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import {Profile} from 'pprof-format';

import {
  mapAllocationProfile,
  startSamplingHeapProfiler,
  stopSamplingHeapProfiler,
  monitorOutOfMemory as monitorOutOfMemoryImported,
} from './heap-profiler-bindings';
import {serializeHeapProfile} from './profile-serializer';
import {SourceMapper} from './sourcemapper/sourcemapper';
import {
  AllocationProfileNode,
  GenerateAllocationLabelsFunction,
} from './v8-types';
import {isMainThread} from 'worker_threads';

let enabled = false;
let heapIntervalBytes = 0;
let heapStackDepth = 0;
/**
 * Collects a heap profile when heapProfiler is enabled. Otherwise throws
 * an error.
 * Map the heap profiler to a converted profile using callback function.
 *
 * WARNING: Nodes in the tree are only valid during the callback. Do not store
 * references to them. The memory is freed when the callback returns.
 *
 * @param callback - function to convert the heap profiler to a converted profile
 * @returns <T> converted profile
 */
export function v8Profile<T>(callback: (root: AllocationProfileNode) => T): T {
  if (!enabled) {
    throw new Error('Heap profiler is not enabled.');
  }
  return mapAllocationProfile(callback);
}

export function convertProfile(
  rootNode: AllocationProfileNode,
  ignoreSamplePath?: string,
  sourceMapper?: SourceMapper,
  generateLabels?: GenerateAllocationLabelsFunction,
): Profile {
  const startTimeNanos = Date.now() * 1000 * 1000;
  // Add node for external memory usage.
  // Current type definitions do not have external.
  // TODO: remove any once type definition is updated to include external.
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const {external}: {external: number} = process.memoryUsage() as any;
  let root: AllocationProfileNode;
  if (external > 0) {
    const externalNode: AllocationProfileNode = {
      name: '(external)',
      scriptName: '',
      children: [],
      allocations: [{sizeBytes: external, count: 1}],
    };
    root = {...rootNode, children: [...rootNode.children, externalNode]};
  } else {
    root = rootNode;
  }
  return serializeHeapProfile(
    root,
    startTimeNanos,
    heapIntervalBytes,
    ignoreSamplePath,
    sourceMapper,
    generateLabels,
  );
}

/**
 * Collects a profile and returns it serialized in pprof format using lazy V2 API.
 * Throws if heap profiler is not enabled.
 *
 * @param ignoreSamplePath
 * @param sourceMapper
 * @param generateLabels
 */
export function profile(
  ignoreSamplePath?: string,
  sourceMapper?: SourceMapper,
  generateLabels?: GenerateAllocationLabelsFunction,
): Profile {
  return v8Profile(root => {
    return convertProfile(root, ignoreSamplePath, sourceMapper, generateLabels);
  });
}

/**
 * Starts heap profiling. If heap profiling has already been started with
 * the same parameters, this is a noop. If heap profiler has already been
 * started with different parameters, this throws an error.
 *
 * @param intervalBytes - average number of bytes between samples.
 * @param stackDepth - maximum stack depth for samples collected.
 */
export function start(intervalBytes: number, stackDepth: number) {
  if (enabled) {
    throw new Error(
      `Heap profiler is already started  with intervalBytes ${heapIntervalBytes} and stackDepth ${stackDepth}`,
    );
  }
  heapIntervalBytes = intervalBytes;
  heapStackDepth = stackDepth;
  startSamplingHeapProfiler(heapIntervalBytes, heapStackDepth);
  enabled = true;
}

// Stops heap profiling. If heap profiling has not been started, does nothing.
export function stop() {
  if (enabled) {
    enabled = false;
    stopSamplingHeapProfiler();
  }
}

export type NearHeapLimitCallback = (profile: Profile) => void;

export const CallbackMode = {
  Async: 1,
  Interrupt: 2,
  Both: 3,
};

/**
 * Add monitoring for v8 heap, heap profiler must already be started.
 * When an out of heap memory event occurs:
 *  - an extension of heap memory of |heapLimitExtensionSize| bytes is
 *    requested to v8. This extension can occur |maxHeapLimitExtensionCount|
 *    number of times. If the extension amount is not enough to satisfy
 *    memory allocation that triggers GC and OOM, process will abort.
 *  - heap profile is dumped as folded stacks on stderr if
 *    |dumpHeapProfileOnSdterr| is true
 *  - heap profile is dumped in temporary file and a new process is spawned
 *    with |exportCommand| arguments and profile path appended at the end.
 *  - |callback| is called. Callback can be invoked only if
 *    heapLimitExtensionSize is enough for the process to continue. Invocation
 *    will be done by a RequestInterrupt if |callbackMode| is Interrupt or Both,
 *    this might be unsafe since Isolate should not be reentered
 *    from RequestInterrupt, but this allows to interrupt synchronous code.
 *    Otherwise the callback is scheduled to be called asynchronously.
 * @param heapLimitExtensionSize - amount of bytes heap should be expanded
 *  with upon OOM
 * @param maxHeapLimitExtensionCount - maximum number of times heap size
 *  extension can occur
 * @param dumpHeapProfileOnSdterr - dump heap profile on stderr upon OOM
 * @param exportCommand - command to execute upon OOM, filepath of a
 *  temporary file containing heap profile will be appended
 * @param callback - callback to call when OOM occurs
 * @param callbackMode
 */
export function monitorOutOfMemory(
  heapLimitExtensionSize: number,
  maxHeapLimitExtensionCount: number,
  dumpHeapProfileOnSdterr: boolean,
  exportCommand?: Array<string>,
  callback?: NearHeapLimitCallback,
  callbackMode?: number,
) {
  if (!enabled) {
    throw new Error(
      'Heap profiler must already be started to call monitorOutOfMemory',
    );
  }
  let newCallback;
  if (typeof callback !== 'undefined') {
    newCallback = (profile: AllocationProfileNode) => {
      callback(convertProfile(profile));
    };
  }
  monitorOutOfMemoryImported(
    heapLimitExtensionSize,
    maxHeapLimitExtensionCount,
    dumpHeapProfileOnSdterr,
    exportCommand || [],
    newCallback,
    typeof callbackMode !== 'undefined' ? callbackMode : CallbackMode.Async,
    isMainThread,
  );
}

```

### File: ts\src\index.ts
```ts
/**
 * Copyright 2019 Google Inc. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
import {writeFileSync} from 'fs';

import * as heapProfiler from './heap-profiler';
import {encodeSync} from './profile-encoder';
import * as timeProfiler from './time-profiler';
export {
  AllocationProfileNode,
  TimeProfileNode,
  ProfileNode,
  LabelSet,
} from './v8-types';

export {encode, encodeSync} from './profile-encoder';
export {SourceMapper} from './sourcemapper/sourcemapper';
export {setLogger} from './logger';
export {getNativeThreadId} from './time-profiler';

export const time = {
  profile: timeProfiler.profile,
  start: timeProfiler.start,
  stop: timeProfiler.stop,
  getContext: timeProfiler.getContext,
  setContext: timeProfiler.setContext,
  runWithContext: timeProfiler.runWithContext,
  isStarted: timeProfiler.isStarted,
  v8ProfilerStuckEventLoopDetected:
    timeProfiler.v8ProfilerStuckEventLoopDetected,
  getState: timeProfiler.getState,
  getMetrics: timeProfiler.getMetrics,
  constants: timeProfiler.constants,
};

export const heap = {
  start: heapProfiler.start,
  stop: heapProfiler.stop,
  profile: heapProfiler.profile,
  convertProfile: heapProfiler.convertProfile,
  v8Profile: heapProfiler.v8Profile,
  monitorOutOfMemory: heapProfiler.monitorOutOfMemory,
  CallbackMode: heapProfiler.CallbackMode,
};

// If loaded with --require, start profiling.
if (module.parent && module.parent.id === 'internal/preload') {
  time.start({});
  process.on('exit', () => {
    // The process is going to terminate imminently. All work here needs to
    // be synchronous.
    const profile = time.stop();
    const buffer = encodeSync(profile);
    writeFileSync(`pprof-profile-${process.pid}.pb.gz`, buffer);
  });
}

```

### File: ts\src\logger.ts
```ts
export interface Logger {
  error(...args: Array<{}>): void;
  trace(...args: Array<{}>): void;
  debug(...args: Array<{}>): void;
  info(...args: Array<{}>): void;
  warn(...args: Array<{}>): void;
  fatal(...args: Array<{}>): void;
}

export class NullLogger implements Logger {
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  info(...args: Array<{}>): void {
    return;
  }
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  error(...args: Array<{}>): void {
    return;
  }
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  trace(...args: Array<{}>): void {
    return;
  }
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  warn(...args: Array<{}>): void {
    return;
  }
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  fatal(...args: Array<{}>): void {
    return;
  }
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  debug(...args: Array<{}>): void {
    return;
  }
}

export let logger = new NullLogger();

export function setLogger(newLogger: Logger) {
  logger = newLogger;
}

```

### File: ts\src\profile-encoder.ts
```ts
/**
 * Copyright 2019 Google Inc. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import {promisify} from 'util';
import {gzip, gzipSync} from 'zlib';

import {Profile} from 'pprof-format';

const gzipPromise = promisify(gzip);

export function encode(profile: Profile): Promise<Buffer> {
  return profile.encodeAsync().then(gzipPromise);
}

export function encodeSync(profile: Profile): Buffer {
  return gzipSync(profile.encode());
}

```

### File: ts\src\profile-serializer.ts
```ts
/**
 * Copyright 2017 Google Inc. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import {
  Function,
  Label,
  LabelInput,
  Line,
  Location,
  Profile,
  Sample,
  ValueType,
  StringTable,
  ProfileInput,
} from 'pprof-format';
import {
  GeneratedLocation,
  SourceLocation,
  SourceMapper,
} from './sourcemapper/sourcemapper';
import {
  AllocationProfileNode,
  GenerateAllocationLabelsFunction,
  GenerateTimeLabelsFunction,
  ProfileNode,
  TimeProfile,
  TimeProfileNode,
} from './v8-types';

export const NON_JS_THREADS_FUNCTION_NAME = 'Non JS threads activity';
export const GARBAGE_COLLECTION_FUNCTION_NAME = 'Garbage Collection';

/**
 * A stack of function IDs.
 */
type Stack = number[];

/**
 * A function which converts entry into one or more samples, then
 * appends those sample(s) to samples.
 */
type AppendEntryToSamples<T extends ProfileNode> = (
  entry: Entry<T>,
  samples: Sample[],
) => void;

/**
 * Profile node and stack trace to that node.
 */
interface Entry<T extends ProfileNode> {
  node: T;
  stack: Stack;
}

function isGeneratedLocation(
  location: SourceLocation,
): location is GeneratedLocation {
  return (
    location.column !== undefined &&
    location.line !== undefined &&
    location.line > 0
  );
}

/**
 * Takes v8 profile and populates sample, location, and function fields of
 * profile.proto.
 *
 * @param profile - profile.proto with empty sample, location, and function
 * fields.
 * @param root - root of v8 profile tree describing samples to be appended
 * to profile.
 * @param appendToSamples - function which converts entry to sample(s)  and
 * appends these to end of an array of samples.
 * @param stringTable - string table for the existing profile.
 */
function serialize<T extends ProfileNode>(
  profile: ProfileInput,
  root: T,
  appendToSamples: AppendEntryToSamples<T>,
  stringTable: StringTable,
  ignoreSamplesPath?: string,
  sourceMapper?: SourceMapper,
) {
  const samples: Sample[] = [];
  const locations: Location[] = [];
  const functions: Function[] = [];
  const functionIdMap = new Map<string, number>();
  const locationIdMap = new Map<string, number>();

  let hasMissingMapFiles = false;

  const entries: Array<Entry<T>> = (root.children as T[]).map((n: T) => ({
    node: n,
    stack: [],
  }));
  while (entries.length > 0) {
    const entry = entries.pop()!;
    const node = entry.node;

    // mjs files have a `file://` prefix in the scriptName -> remove it
    const scriptName = node.scriptName.startsWith('file://')
      ? node.scriptName.slice(7)
      : node.scriptName;

    if (ignoreSamplesPath && scriptName.indexOf(ignoreSamplesPath) > -1) {
      continue;
    }
    const stack = entry.stack;
    const location = getLocation(node, scriptName, sourceMapper);
    stack.unshift(location.id as number);
    appendToSamples(entry, samples);
    for (const child of node.children as T[]) {
      entries.push({node: child, stack: stack.slice()});
    }
  }

  profile.sample = samples;
  profile.location = locations;
  profile.function = functions;
  profile.stringTable = stringTable;

  if (hasMissingMapFiles) {
    profile.comment = [stringTable.dedup('dd:has-missing-map-files')];
  }

  function getLocation(
    node: ProfileNode,
    scriptName: string,
    sourceMapper?: SourceMapper,
  ): Location {
    let profLoc: SourceLocation = {
      file: scriptName || '',
      line: node.lineNumber,
      column: node.columnNumber,
      name: node.name,
    };

    if (profLoc.line) {
      if (sourceMapper && isGeneratedLocation(profLoc)) {
        profLoc = sourceMapper.mappingInfo(profLoc);
        if (profLoc.missingMapFile) {
          hasMissingMapFiles = true;
        }
      }
    }
    const keyStr = `${node.scriptId}:${profLoc.line}:${profLoc.column}:${profLoc.name}`;
    let id = locationIdMap.get(keyStr);
    if (id !== undefined) {
      // id is index+1, since 0 is not valid id.
      return locations[id - 1];
    }
    id = locations.length + 1;
    locationIdMap.set(keyStr, id);
    const line = getLine(profLoc, node.scriptId);
    const location = new Location({id, line: [line]});
    locations.push(location);
    return location;
  }

  function getLine(loc: SourceLocation, scriptId?: number): Line {
    return new Line({
      functionId: getFunction(loc, scriptId).id,
      line: loc.line,
    });
  }

  function getFunction(loc: SourceLocation, scriptId?: number): Function {
    let name = loc.name;
    const keyStr = name
      ? `${scriptId}:${name}`
      : `${scriptId}:${loc.line}:${loc.column}`;
    let id = functionIdMap.get(keyStr);
    if (id !== undefined) {
      // id is index+1, since 0 is not valid id.
      return functions[id - 1];
    }
    id = functions.length + 1;
    functionIdMap.set(keyStr, id);
    if (!name) {
      if (loc.line) {
        if (loc.column) {
          name = `(anonymous:L#${loc.line}:C#${loc.column})`;
        } else {
          name = `(anonymous:L#${loc.line})`;
        }
      } else {
        name = '(anonymous)';
      }
    }
    const nameId = stringTable.dedup(name);
    const f = new Function({
      id,
      name: nameId,
      systemName: nameId,
      filename: stringTable.dedup(loc.file || ''),
    });
    functions.push(f);
    return f;
  }
}

/**
 * @return value type for sample counts (type:sample, units:count), and
 * adds strings used in this value type to the table.
 */
function createSampleCountValueType(table: StringTable): ValueType {
  return new ValueType({
    type: table.dedup('sample'),
    unit: table.dedup('count'),
  });
}

/**
 * @return value type for time samples (type:wall, units:nanoseconds), and
 * adds strings used in this value type to the table.
 */
function createTimeValueType(table: StringTable): ValueType {
  return new ValueType({
    type: table.dedup('wall'),
    unit: table.dedup('nanoseconds'),
  });
}

/**
 * @return value type for cpu samples (type:cpu, units:nanoseconds), and
 * adds strings used in this value type to the table.
 */
function createCpuValueType(table: StringTable): ValueType {
  return new ValueType({
    type: table.dedup('cpu'),
    unit: table.dedup('nanoseconds'),
  });
}

/**
 * @return value type for object counts (type:objects, units:count), and
 * adds strings used in this value type to the table.
 */
function createObjectCountValueType(table: StringTable): ValueType {
  return new ValueType({
    type: table.dedup('objects'),
    unit: table.dedup('count'),
  });
}

/**
 * @return value type for memory allocations (type:space, units:bytes), and
 * adds strings used in this value type to the table.
 */
function createAllocationValueType(table: StringTable): ValueType {
  return new ValueType({
    type: table.dedup('space'),
    unit: table.dedup('bytes'),
  });
}

export function computeTotalHitCount(root: TimeProfileNode): number {
  return (
    root.hitCount +
    (root.children as TimeProfileNode[]).reduce(
      (sum, node) => sum + computeTotalHitCount(node),
      0,
    )
  );
}

/** Perform some modifications on time profile:
 *  - Add non-JS thread activity node if available
 *  - remove `(program)` nodes
 *  - remove `(idle)` nodes with no context
 *  - set `(idle)` nodes' wall time to zero when they have a context
 *  - Convert `(garbage collector)` node to `Garbage Collection`
 *  - Put `non-JS thread activity` node and `Garbage Collection` under a top level `Node.js` node
 * This function does not change the input profile.
 */
function updateTimeProfile(prof: TimeProfile): TimeProfile {
  const newTopLevelChildren: TimeProfileNode[] = [];

  let runtimeNode: TimeProfileNode | undefined;

  function getRuntimeNode(): TimeProfileNode {
    if (!runtimeNode) {
      runtimeNode = {
        name: 'Node.js',
        scriptName: '',
        scriptId: 0,
        lineNumber: 0,
        columnNumber: 0,
        children: [],
        hitCount: 0,
      };
      newTopLevelChildren.push(runtimeNode);
    }
    return runtimeNode;
  }

  for (const child of prof.topDownRoot.children as TimeProfileNode[]) {
    if (child.name === '(program)') {
      continue;
    }
    if (child.name === '(idle)' && child.contexts?.length === 0) {
      continue;
    }
    if (child.name === '(garbage collector)') {
      // Create a new node to avoid modifying the input one
      const newChild: TimeProfileNode = {
        ...child,
        name: GARBAGE_COLLECTION_FUNCTION_NAME,
      };
      getRuntimeNode().children.push(newChild);
    } else {
      newTopLevelChildren.push(child);
    }
  }

  if (prof.hasCpuTime && prof.nonJSThreadsCpuTime) {
    const node: TimeProfileNode = {
      name: NON_JS_THREADS_FUNCTION_NAME,
      scriptName: '',
      scriptId: 0,
      lineNumber: 0,
      columnNumber: 0,
      children: [],
      hitCount: 0, // 0 because this should not be accounted for wall time
      contexts: [
        {
          context: {},
          timestamp: BigInt(0),
          cpuTime: prof.nonJSThreadsCpuTime,
          asyncId: -1,
        },
      ],
    };
    getRuntimeNode().children.push(node);
  }
  return {
    ...prof,
    topDownRoot: {...prof.topDownRoot, children: newTopLevelChildren},
  };
}

/**
 * Converts v8 time profile into into a profile proto.
 * (https://github.com/google/pprof/blob/master/proto/profile.proto)
 *
 * @param prof - profile to be converted.
 * @param intervalMicros - average time (microseconds) between samples.
 */
export function serializeTimeProfile(
  prof: TimeProfile,
  intervalMicros: number,
  sourceMapper?: SourceMapper,
  recomputeSamplingInterval = false,
  generateLabels?: GenerateTimeLabelsFunction,
  lowCardinalityLabels: string[] = [],
): Profile {
  // If requested, recompute sampling interval from profile duration and total number of hits,
  // since profile duration should be #hits x interval.
  // Recomputing an average interval is more accurate, since in practice intervals between
  // samples are larger than the requested sampling interval (eg. 12.5ms vs 10ms requested).
  // For very short durations, computation becomes meaningless (eg. if there is only one hit),
  // therefore keep intervalMicros as a lower bound and 2 * intervalMicros as upper bound.
  if (recomputeSamplingInterval) {
    const totalHitCount =
      prof.totalHitCount ?? computeTotalHitCount(prof.topDownRoot);
    if (totalHitCount > 0) {
      intervalMicros = Math.min(
        Math.max(
          Math.floor((prof.endTime - prof.startTime) / totalHitCount),
          intervalMicros,
        ),
        2 * intervalMicros,
      );
    }
  }
  const intervalNanos = intervalMicros * 1000;
  const stringTable = new StringTable();
  const labelCaches: Map<number | bigint, Label>[] = [];
  for (const l of lowCardinalityLabels) {
    labelCaches[stringTable.dedup(l)] = new Map<number | bigint, Label>();
  }
  const dedupLabels = (labels: Label[]) => {
    for (let i = 0; i < labels.length; i++) {
      const label = labels[i];
      const cache = labelCaches[Number(label.key)];
      if (cache !== undefined) {
        const key = label.str ?? label.num;
        const exlabel = cache.get(key);
        if (exlabel === undefined) {
          cache.set(key, label);
        } else if (
          label.str === exlabel.str &&
          label.num === exlabel.num &&
          label.numUnit === exlabel.numUnit
        ) {
          labels[i] = exlabel;
        }
      }
    }
    return labels;
  };

  const appendTimeEntryToSamples: AppendEntryToSamples<TimeProfileNode> = (
    entry: Entry<TimeProfileNode>,
    samples: Sample[],
  ) => {
    let unlabelledHits = entry.node.hitCount;
    let unlabelledCpuTime = 0;
    const isIdle = entry.node.name === '(idle)';
    for (const context of entry.node.contexts || []) {
      const labels = generateLabels
        ? generateLabels({node: entry.node, context})
        : (context.context ?? {});
      const labelsArr = buildLabels(labels, stringTable);
      if (labelsArr.length > 0) {
        // Only assign wall time if there are hits, some special nodes such as `(Non-JS threads)`
        // have zero hit count (since they do not count as wall time) and should not be assigned any
        // wall time. Also, `(idle)` nodes should be assigned zero wall time.
        const values =
          unlabelledHits > 0 ? [1, isIdle ? 0 : intervalNanos] : [0, 0];
        if (prof.hasCpuTime) {
          values.push(context.cpuTime ?? 0);
        }
        const sample = new Sample({
          locationId: entry.stack,
          value: values,
          label: dedupLabels(labelsArr),
        });
        samples.push(sample);
        unlabelledHits--;
      } else if (prof.hasCpuTime) {
        unlabelledCpuTime += context.cpuTime ?? 0;
      }
    }
    if ((!isIdle && unlabelledHits > 0) || unlabelledCpuTime > 0) {
      const labels = generateLabels ? generateLabels({node: entry.node}) : {};
      const values =
        unlabelledHits > 0
          ? [unlabelledHits, isIdle ? 0 : unlabelledHits * intervalNanos]
          : [0, 0];
      if (prof.hasCpuTime) {
        values.push(unlabelledCpuTime);
      }
      const sample = new Sample({
        locationId: entry.stack,
        value: values,
        label: buildLabels(labels, stringTable),
      });
      samples.push(sample);
    }
  };

  const sampleValueType = createSampleCountValueType(stringTable);
  const timeValueType = createTimeValueType(stringTable);

  const sampleTypes = [sampleValueType, timeValueType];
  if (prof.hasCpuTime) {
    const cpuValueType = createCpuValueType(stringTable);
    sampleTypes.push(cpuValueType);
  }

  const profile = {
    sampleType: sampleTypes,
    timeNanos: Date.now() * 1000 * 1000,
    durationNanos: (prof.endTime - prof.startTime) * 1000,
    periodType: timeValueType,
    period: intervalNanos,
  };

  const updatedProf = updateTimeProfile(prof);

  serialize(
    profile,
    updatedProf.topDownRoot,
    appendTimeEntryToSamples,
    stringTable,
    undefined,
    sourceMapper,
  );

  return new Profile(profile);
}

function buildLabels(labelSet: object, stringTable: StringTable): Label[] {
  const labels: Label[] = [];

  for (const [key, value] of Object.entries(labelSet)) {
    const labelInput: LabelInput = {
      key: stringTable.dedup(key),
    };
    switch (typeof value) {
      case 'string':
        labelInput.str = stringTable.dedup(value);
        break;
      case 'number':
      case 'bigint':
        labelInput.num = value;
   
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

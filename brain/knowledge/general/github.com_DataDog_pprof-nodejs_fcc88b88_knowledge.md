---
id: github.com-datadog-pprof-nodejs-fcc88b88-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:43.244958
---

# KNOWLEDGE EXTRACT: github.com_DataDog_pprof-nodejs_fcc88b88
> **Extracted on:** 2026-04-01 13:20:41
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007522371/github.com_DataDog_pprof-nodejs_fcc88b88

---

## File: `.clang-format`
```
---
Language:        Cpp
# BasedOnStyle:  Google
AccessModifierOffset: -1
AlignAfterOpenBracket: Align
AlignConsecutiveAssignments: false
AlignConsecutiveDeclarations: false
AlignEscapedNewlines: Right
AlignOperands:   true
AlignTrailingComments: true
AllowAllParametersOfDeclarationOnNextLine: true
AllowShortBlocksOnASingleLine: false
AllowShortCaseLabelsOnASingleLine: false
AllowShortFunctionsOnASingleLine: Inline
AllowShortIfStatementsOnASingleLine: true
AllowShortLoopsOnASingleLine: true
AlwaysBreakAfterDefinitionReturnType: None
AlwaysBreakAfterReturnType: None
AlwaysBreakBeforeMultilineStrings: false
AlwaysBreakTemplateDeclarations: true
BinPackArguments: false
BinPackParameters: false
BraceWrapping:
  AfterClass:      false
  AfterControlStatement: false
  AfterEnum:       false
  AfterFunction:   false
  AfterNamespace:  false
  AfterObjCDeclaration: false
  AfterStruct:     false
  AfterUnion:      false
  AfterExternBlock: false
  BeforeCatch:     false
  BeforeElse:      false
  IndentBraces:    false
  SplitEmptyFunction: true
  SplitEmptyRecord: true
  SplitEmptyNamespace: true
BreakBeforeBinaryOperators: None
BreakBeforeBraces: Attach
BreakBeforeInheritanceComma: false
BreakBeforeTernaryOperators: true
BreakConstructorInitializersBeforeComma: false
BreakConstructorInitializers: BeforeColon
BreakAfterJavaFieldAnnotations: false
BreakStringLiterals: true
ColumnLimit:      80
CommentPragmas:  '^ IWYU pragma:'
CompactNamespaces: false
ConstructorInitializerAllOnOneLineOrOnePerLine: true
ConstructorInitializerIndentWidth: 4
ContinuationIndentWidth: 4
Cpp11BracedListStyle: true
DerivePointerAlignment: false
DisableFormat:   false
ExperimentalAutoDetectBinPacking: false
FixNamespaceComments: true
ForEachMacros:
  - foreach
  - Q_FOREACH
  - BOOST_FOREACH
IncludeBlocks:   Preserve
IncludeCategories:
  - Regex:           '^<ext/.*\.h>'
    Priority:        2
  - Regex:           '^<.*\.h>'
    Priority:        1
  - Regex:           '^<.*'
    Priority:        2
  - Regex:           '.*'
    Priority:        3
IncludeIsMainRegex: '([-_](test|unittest))?$'
IndentCaseLabels: true
IndentPPDirectives: None
IndentWidth:     2
IndentWrappedFunctionNames: false
JavaScriptQuotes: Leave
JavaScriptWrapImports: true
KeepEmptyLinesAtTheStartOfBlocks: false
MacroBlockBegin: ''
MacroBlockEnd:   ''
MaxEmptyLinesToKeep: 1
NamespaceIndentation: None
ObjCBlockIndentWidth: 2
ObjCSpaceAfterProperty: false
ObjCSpaceBeforeProtocolList: false
PenaltyBreakAssignment: 2
PenaltyBreakBeforeFirstCallParameter: 1
PenaltyBreakComment: 300
PenaltyBreakFirstLessLess: 120
PenaltyBreakString: 1000
PenaltyExcessCharacter: 1000000
PenaltyReturnTypeOnItsOwnLine: 200
PointerAlignment: Left
ReflowComments:  true
SortIncludes:    true
SortUsingDeclarations: true
SpaceAfterCStyleCast: false
SpaceAfterTemplateKeyword: true
SpaceBeforeAssignmentOperators: true
SpaceBeforeParens: ControlStatements
SpaceInEmptyParentheses: false
SpacesBeforeTrailingComments: 2
SpacesInAngles:  false
SpacesInContainerLiterals: true
SpacesInCStyleCastParentheses: false
SpacesInParentheses: false
SpacesInSquareBrackets: false
Standard:        Auto
TabWidth:        8
UseTab:          Never
```

## File: `.editorconfig`
```
; http://editorconfig.org

root = true

[*]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.md]
indent_size = 4
```

## File: `.gitignore`
```
.nyc_output
.coverage
.vscode
/*.build
/build
out
node_modules
system-test/busybench/package-lock.json
system-test/busybench-js/package-lock.json
prebuilds
tsconfig.tsbuildinfo
```

## File: `.gitlab-ci.yml`
```yaml
stages:
  - benchmarks

include: ".gitlab/benchmarks.yml"
```

## File: `.nycrc`
```
{
  "report-dir": "./.coverage",
  "reporter": "lcov",
  "exclude": [
    "src/*{/*,/**/*}.js",
    "src/*/v*/*.js",
    "test/**/*.js",
    "build/test"
  ],
  "watermarks": {
    "branches": [
      95,
      100
    ],
    "functions": [
      95,
      100
    ],
    "lines": [
      95,
      100
    ],
    "statements": [
      95,
      100
    ]
  }
}
```

## File: `.prettierrc.js`
```javascript
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

## File: `CONTRIBUTING.md`
```markdown
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

[setup]: https://cloud.google.com/nodejs/brain/knowledge/docs_legacy/setup

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

## File: `LICENSE`
```

                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## File: `README.md`
```markdown
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

## File: `appveyor.yml`
```yaml
environment:
  matrix:
    - nodejs_version: "6"
    - nodejs_version: "8"
    - nodejs_version: "10"
    - nodejs_version: "11"

install:
  - ps: Install-Product node $env:nodejs_version
  - npm install

test_script:
  - node --version
  - npm --version
  - npm test

build: off
```

## File: `binding.gyp`
```
{
    "variables": {
        "address_sanitizer%": 0, # enable address + undefined behaviour sanitizer
        "thread_sanitizer%": 0, # enable thread sanitizer,
        "build_tests%": 0
    },
    "conditions": [
        [
            "build_tests != 'true'",
            {
                "targets": [
                    {
                        "target_name": "dd_pprof",
                        "sources": [
                            "bindings/profilers/heap.cc",
                            "bindings/profilers/wall.cc",
                            "bindings/per-isolate-data.cc",
                            "bindings/thread-cpu-clock.cc",
                            "bindings/translate-heap-profile.cc",
                            "bindings/translate-time-profile.cc",
                            "bindings/binding.cc",
                            "bindings/map-get.cc",
                            "bindings/allocation-profile-node.cc"
                        ],
                        "include_dirs": [
                            "bindings",
                            "<!(node -e \"require('nan')\")"
                        ]
                    }
                ]
            }
        ],
        [
            "build_tests == 'true'",
            {
                "targets": [
                    {
                        "target_name": "test_dd_pprof",
                        "sources": [
                            "bindings/profilers/heap.cc",
                            "bindings/profilers/wall.cc",
                            "bindings/per-isolate-data.cc",
                            "bindings/thread-cpu-clock.cc",
                            "bindings/translate-heap-profile.cc",
                            "bindings/translate-time-profile.cc",
                            "bindings/test/binding.cc",
                            "bindings/allocation-profile-node.cc"
                        ],
                        "include_dirs": [
                            "bindings",
                            "<!(node -e \"require('nan')\")"
                        ]
                    }
                ]
            }
        ]
    ],
    "target_defaults": {
        "conditions": [
            [
                'OS == "win"',
                {
                    "defines": [
                        "NOMINMAX"
                    ],
                    'msvs_settings': {
                        'VCCLCompilerTool': {
                            'AdditionalOptions': [
                                '/Zc:__cplusplus',
                                '-std:c++20',
                            ],
                        },
                    },
                },
            ],
            ["OS == 'linux'",
                {
                "cflags+":
                    ["-Wno-deprecated-declarations"],
                "cflags_cc!": ["-std=gnu++14", "-std=gnu++1y", "-std=gnu++20" ],
                "cflags_cc": ["-std=gnu++2a"],
                }
            ],
            ["OS == 'mac'",
                {
                'xcode_settings': {
                    'MACOSX_DEPLOYMENT_TARGET': '11',
                    'CLANG_CXX_LANGUAGE_STANDARD': 'c++20',
                    'OTHER_CFLAGS+': [
                        "-Wno-deprecated-declarations",
                        "-Wno-cast-function-type-mismatch", # clang17 now warns about casts between incompatible function types and v8 has some of those
                        "-Wno-unknown-warning-option", # "-Wcast-function-type-mismatch" is not a valid warning option for clang < 17
                        ],
                    },
                }
            ],
            ["address_sanitizer == 'true' and OS == 'mac'", {
                'xcode_settings': {
                    'OTHER_CFLAGS+': [
                        '-fno-omit-frame-pointer',
                        '-fsanitize=address,undefined',
                        '-O0',
                        '-g',
                    ],
                    'OTHER_CFLAGS!': [
                        '-fomit-frame-pointer',
                        '-O3',
                    ],
                },
                'target_conditions': [
                    ['_type!="static_library"', {
                        'xcode_settings': {'OTHER_LDFLAGS+': ['-fsanitize=address,undefined']},
                    }],
                ],
            }],
            ["address_sanitizer == 'true' and OS != 'mac'", {
                "cflags+": [
                "-fno-omit-frame-pointer",
                "-fsanitize=address,undefined",
                "-O0",
                "-g",
                ],
                "cflags!": [ "-fomit-frame-pointer", "-O3" ],
                "ldflags+": [ "-fsanitize=address,undefined" ],
            }],
            ["thread_sanitizer == 'true' and OS == 'mac'", {
                'xcode_settings': {
                    'OTHER_CFLAGS+': [
                        '-fno-omit-frame-pointer',
                        '-fsanitize=thread',
                    ],
                    'OTHER_CFLAGS!': [
                        '-fomit-frame-pointer',
                    ],
                },
                'target_conditions': [
                    ['_type!="static_library"', {
                        'xcode_settings': {'OTHER_LDFLAGS+': ['-fsanitize=thread']},
                    }],
                ],
            }],
            ["thread_sanitizer == 'true' and OS != 'mac'", {
                "cflags+": [
                "-fno-omit-frame-pointer",
                "-fsanitize=thread",
                ],
                "cflags!": [ "-fomit-frame-pointer" ],
                "ldflags+": [ "-fsanitize=thread" ],
            }]
        ],
    }
}
```

## File: `codecov.yaml`
```yaml
ignore:
    proto
```

## File: `eslint.config.js`
```javascript
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

## File: `package.json`
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

## File: `renovate.json`
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

## File: `tsconfig.json`
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

## File: `benchmark/sirun/run-all-variants.js`
```javascript
'use strict'

const childProcess = require('child_process')
const path = require('path')
const readline = require('readline')

process.env.DD_TRACE_TELEMETRY_ENABLED = 'false'

function exec (...args) {
  return new Promise((resolve, reject) => {
    const proc = childProcess.spawn(...args)
    streamAddVersion(proc.stdout)
    proc.on('error', reject)
    proc.on('exit', (code) => {
      if (code === 0) {
        resolve()
      } else {
        reject(new Error('Process exited with non-zero code.'))
      }
    })
  })
}

const metaJson = require(path.join(process.cwd(), 'meta.json'))

const env = Object.assign({}, process.env, { DD_TRACE_STARTUP_LOGS: 'false' })

function streamAddVersion (input) {
  input.rl = readline.createInterface({ input })
  input.rl.on('line', function (line) {
    try {
      const json = JSON.parse(line.toString())
      json.nodeVersion = process.versions.node
      // eslint-disable-next-line no-console
      console.log(JSON.stringify(json))
    } catch (e) {
      // eslint-disable-next-line no-console
      console.log(line)
    }
  })
}

function getStdio () {
  return ['inherit', 'pipe', 'inherit']
}

(async () => {
  try {
    if (metaJson.variants) {
      const variants = metaJson.variants
      for (const variant in variants) {
        const variantEnv = Object.assign({}, env, { SIRUN_VARIANT: variant })
        await exec('sirun', ['meta.json'], { env: variantEnv, stdio: getStdio() })
      }
    } else {
      await exec('sirun', ['meta.json'], { env, stdio: getStdio() })
    }
  } catch (e) {
    setImmediate(() => {
      throw e // Older Node versions don't fail on uncaught promise rejections.
    })
  }
})()
```

## File: `benchmark/sirun/runall.sh`
```bash
#!/usr/bin/env bash

set -euo pipefail

if [ -n "${MAJOR_NODE_VERSION:-}" ]; then
    if test -f ~/.nvm/nvm.sh; then
        source ~/.nvm/nvm.sh
    else
        source "${NVM_DIR:-usr/local/nvm}/nvm.sh"
    fi

    nvm use "${MAJOR_NODE_VERSION}"

    pushd ../../
    npm install
    popd
fi

VERSION=$(node -v)
echo "using Node.js ${VERSION}"

for d in *; do
    if [ -d "${d}" ]; then
        pushd "$d"
        time node ../run-all-variants.js >> ../results.ndjson
        popd
    fi
done

if [ "${DEBUG_RESULTS:-false}" == "true" ]; then
  echo "Benchmark Results:"
  cat ./results.ndjson
fi

echo "all tests for ${VERSION} have now completed."
```

## File: `benchmark/sirun/wall-profiler/index.js`
```javascript
'use strict'

const profiler = require('../../../out/src/time-profiler')
const { createServer, request } = require('http')

const concurrency = Number(process.env.CONCURRENCY || '10')
const requestFrequency = Number(process.env.REQUEST_FREQUENCY || '15')
const sampleFrequency = Number(process.env.SAMPLE_FREQUENCY || '999')

const server = createServer((req, res) => {
  setImmediate(() => {
    res.end('hello')
  })
})

function get (options) {
  return new Promise((resolve, reject) => {
    const req = request(options, (res) => {
      const chunks = []
      res.on('error', reject)
      res.on('data', chunks.push.bind(chunks))
      res.on('end', () => {
        resolve(Buffer.concat(chunks))
      })
    })
    req.on('error', reject)
    req.end()
  })
}

function delay (ms) {
  return new Promise(resolve => setTimeout(resolve, ms))
}

async function storm (requestFrequency, task) {
  const gap = (1 / requestFrequency) * 1e9
  while (server.listening) {
    const start = process.hrtime.bigint()
    try {
      await task()
    } catch (e) {
      // Ignore ECONNRESET if server is shutting down
      if (e.code !== 'ECONNRESET' || server.listening) {
        throw e
      }
    }
    const end = process.hrtime.bigint()
    const remainder = gap - Number(end - start)
    await delay(Math.max(0, remainder / 1e6))
  }
}

server.listen(8080, '0.0.0.0', async () => {
  if (!concurrency) return
  const { address, port } = server.address()
  const getter = get.bind(null, {
    hostname: address,
    path: '/',
    port
  })
  const task = storm.bind(null, requestFrequency, getter)
  const tasks = Array.from({ length: concurrency }, task)
  await Promise.all(tasks)
})

if (sampleFrequency !== 0) {
  profiler.start({ intervalMicros: 1e6 / sampleFrequency })
}

setTimeout(() => {
  if (profiler.isStarted()) {
    profiler.stop()
  }
  server.close()
}, 1000)
```

## File: `benchmark/sirun/wall-profiler/meta.json`
```json
{
  "name": "profiler",
  "run": "node index.js",
  "cachegrind": true,
  "iterations": 10,
  "variants": {
    "idle-no-wall-profiler": {
      "env": {
        "CONCURRENCY": "0",
        "REQUEST_FREQUENCY": "0",
        "SAMPLE_FREQUENCY": "0"
      }
    },
    "idle-with-wall-profiler": {
      "env": {
        "CONCURRENCY": "0",
        "REQUEST_FREQUENCY": "0",
        "SAMPLE_FREQUENCY": "999"
      }
    },
    "light-load-no-wall-profiler": {
      "env": {
        "CONCURRENCY": "5",
        "REQUEST_FREQUENCY": "5",
        "SAMPLE_FREQUENCY": "0"
      }
    },
    "light-load-with-wall-profiler": {
      "env": {
        "CONCURRENCY": "5",
        "REQUEST_FREQUENCY": "5",
        "SAMPLE_FREQUENCY": "999"
      }
    },
    "heavy-load-no-wall-profiler": {
      "env": {
        "CONCURRENCY": "15",
        "REQUEST_FREQUENCY": "50",
        "SAMPLE_FREQUENCY": "0"
      }
    },
    "heavy-load-with-wall-profiler": {
      "env": {
        "CONCURRENCY": "15",
        "REQUEST_FREQUENCY": "50",
        "SAMPLE_FREQUENCY": "999"
      }
    }
  }
}
```

## File: `bindings/allocation-profile-node.cc`
```
/*
 * Copyright 2026 Datadog, Inc
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "allocation-profile-node.hh"
#include "per-isolate-data.hh"

using namespace v8;

namespace dd {

template <typename F>
void AllocationProfileNodeView::mapAllocationProfileNode(
    const Nan::PropertyCallbackInfo<Value>& info, F&& mapper) {
  auto* node = static_cast<AllocationProfile::Node*>(
      Nan::GetInternalFieldPointer(info.Holder(), 0));
  info.GetReturnValue().Set(mapper(node));
}

NAN_MODULE_INIT(AllocationProfileNodeView::Init) {
  Local<FunctionTemplate> tpl = Nan::New<FunctionTemplate>();
  tpl->SetClassName(Nan::New("AllocationProfileNode").ToLocalChecked());
  tpl->InstanceTemplate()->SetInternalFieldCount(1);

  auto inst = tpl->InstanceTemplate();
  Nan::SetAccessor(inst, Nan::New("name").ToLocalChecked(), GetName);
  Nan::SetAccessor(
      inst, Nan::New("scriptName").ToLocalChecked(), GetScriptName);
  Nan::SetAccessor(inst, Nan::New("scriptId").ToLocalChecked(), GetScriptId);
  Nan::SetAccessor(
      inst, Nan::New("lineNumber").ToLocalChecked(), GetLineNumber);
  Nan::SetAccessor(
      inst, Nan::New("columnNumber").ToLocalChecked(), GetColumnNumber);
  Nan::SetAccessor(
      inst, Nan::New("allocations").ToLocalChecked(), GetAllocations);
  Nan::SetAccessor(inst, Nan::New("children").ToLocalChecked(), GetChildren);

  PerIsolateData::For(Isolate::GetCurrent())
      ->AllocationNodeConstructor()
      .Reset(Nan::GetFunction(tpl).ToLocalChecked());
}

Local<Object> AllocationProfileNodeView::New(AllocationProfile::Node* node) {
  auto* isolate = Isolate::GetCurrent();

  Local<Function> constructor =
      Nan::New(PerIsolateData::For(isolate)->AllocationNodeConstructor());

  Local<Object> obj = Nan::NewInstance(constructor).ToLocalChecked();

  Nan::SetInternalFieldPointer(obj, 0, node);

  return obj;
}

NAN_GETTER(AllocationProfileNodeView::GetName) {
  mapAllocationProfileNode(
      info, [](AllocationProfile::Node* node) { return node->name; });
}

NAN_GETTER(AllocationProfileNodeView::GetScriptName) {
  mapAllocationProfileNode(
      info, [](AllocationProfile::Node* node) { return node->script_name; });
}

NAN_GETTER(AllocationProfileNodeView::GetScriptId) {
  mapAllocationProfileNode(
      info, [](AllocationProfile::Node* node) { return node->script_id; });
}

NAN_GETTER(AllocationProfileNodeView::GetLineNumber) {
  mapAllocationProfileNode(
      info, [](AllocationProfile::Node* node) { return node->line_number; });
}

NAN_GETTER(AllocationProfileNodeView::GetColumnNumber) {
  mapAllocationProfileNode(
      info, [](AllocationProfile::Node* node) { return node->column_number; });
}

NAN_GETTER(AllocationProfileNodeView::GetAllocations) {
  mapAllocationProfileNode(info, [](AllocationProfile::Node* node) {
    auto* isolate = Isolate::GetCurrent();
    auto context = isolate->GetCurrentContext();

    const auto& allocations = node->allocations;
    Local<Array> arr = Array::New(isolate, allocations.size());
    auto sizeBytes = String::NewFromUtf8Literal(isolate, "sizeBytes");
    auto count = String::NewFromUtf8Literal(isolate, "count");

    for (size_t i = 0; i < allocations.size(); i++) {
      const auto& alloc = allocations[i];
      Local<Object> alloc_obj = Object::New(isolate);
      Nan::Set(alloc_obj,
               sizeBytes,
               Number::New(isolate, static_cast<double>(alloc.size)));
      Nan::Set(alloc_obj,
               count,
               Number::New(isolate, static_cast<double>(alloc.count)));
      arr->Set(context, i, alloc_obj).Check();
    }
    return arr;
  });
}

NAN_GETTER(AllocationProfileNodeView::GetChildren) {
  mapAllocationProfileNode(info, [](AllocationProfile::Node* node) {
    auto* isolate = Isolate::GetCurrent();
    auto context = isolate->GetCurrentContext();

    const auto& children = node->children;
    Local<Array> arr = Array::New(isolate, children.size());
    for (size_t i = 0; i < children.size(); i++) {
      arr->Set(context, i, AllocationProfileNodeView::New(children[i])).Check();
    }
    return arr;
  });
}

}  // namespace dd
```

## File: `bindings/allocation-profile-node.hh`
```
/*
 * Copyright 2026 Datadog, Inc
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#pragma once

#include <nan.h>
#include <v8-profiler.h>

namespace dd {

class AllocationProfileNodeView {
 public:
  static NAN_MODULE_INIT(Init);

  static v8::Local<v8::Object> New(v8::AllocationProfile::Node* node);

 private:
  template <typename F>
  static void mapAllocationProfileNode(
      const Nan::PropertyCallbackInfo<v8::Value>& info, F&& mapper);

  static NAN_GETTER(GetName);
  static NAN_GETTER(GetScriptName);
  static NAN_GETTER(GetScriptId);
  static NAN_GETTER(GetLineNumber);
  static NAN_GETTER(GetColumnNumber);
  static NAN_GETTER(GetAllocations);
  static NAN_GETTER(GetChildren);
};

}  // namespace dd
```

## File: `bindings/binding.cc`
```
/*
 * Copyright 2023 Datadog, Inc
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include <nan.h>
#include <node.h>
#include <v8.h>

#include "allocation-profile-node.hh"
#include "profilers/heap.hh"
#include "profilers/wall.hh"
#include "translate-time-profile.hh"

#ifdef __linux__
#include <sys/syscall.h>
#include <unistd.h>
#endif

static NAN_METHOD(GetNativeThreadId) {
#ifdef __APPLE__
  uint64_t native_id;
  (void)pthread_threadid_np(NULL, &native_id);
#elif defined(__linux__)
  pid_t native_id = syscall(SYS_gettid);
#elif defined(_MSC_VER)
  DWORD native_id = GetCurrentThreadId();
#endif
  info.GetReturnValue().Set(v8::Integer::New(info.GetIsolate(), native_id));
}

#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wcast-function-type"
#endif
NODE_MODULE_INIT(/* exports, module, context */) {
#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC diagnostic pop
#endif

  dd::AllocationProfileNodeView::Init(exports);
  dd::TimeProfileNodeView::Init(exports);
  dd::HeapProfiler::Init(exports);
  dd::WallProfiler::Init(exports);
  Nan::SetMethod(exports, "getNativeThreadId", GetNativeThreadId);
}
```

## File: `bindings/contexts.hh`
```
/*
 * Copyright 2023 Datadog, Inc
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#pragma once

#include <v8-profiler.h>
#include <unordered_map>

namespace dd {

struct NodeInfo {
  v8::Local<v8::Array> contexts;
  uint32_t hitcount;
};

using ContextsByNode = std::unordered_map<const v8::CpuProfileNode*, NodeInfo>;
}  // namespace dd
```

## File: `bindings/defer.hh`
```
/*
 * Copyright 2023 Datadog, Inc
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#pragma once

#include <utility>

namespace details {

struct DeferDummy {};

template <typename F>
class DeferHolder {
 public:
  DeferHolder(DeferHolder&&) = default;
  DeferHolder(const DeferHolder&) = delete;
  DeferHolder& operator=(DeferHolder&&) = delete;
  DeferHolder& operator=(const DeferHolder&) = delete;

  template <typename T>
  explicit DeferHolder(T&& f) : _func(std::forward<T>(f)) {}

  ~DeferHolder() { reset(); }

  void reset() {
    if (_active) {
      _func();
      _active = false;
    }
  }

  void release() { _active = false; }

 private:
  F _func;
  bool _active = true;
};

template <class F>
DeferHolder<F> operator*(DeferDummy, F&& f) {
  return DeferHolder<F>{std::forward<F>(f)};
}

}  // namespace details

template <class F>
details::DeferHolder<F> make_defer(F&& f) {
  return details::DeferHolder<F>{std::forward<F>(f)};
}

#define DEFER_(LINE) zz_defer##LINE
#define DEFER(LINE) DEFER_(LINE)
#define defer                                                                  \
  [[maybe_unused]] const auto& DEFER(__COUNTER__) = details::DeferDummy{}* [&]()
```

## File: `bindings/map-get.cc`
```
/**
 * Copyright 2025 Datadog. All Rights Reserved.
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

#include "map-get.hh"

// Find a value in JavaScript map by directly reading the underlying V8 hash
// map.
//
// V8 uses TWO internal hash map representations:
//   1. SmallOrderedHashMap: For small maps (capacity 4-254)
//      - Metadata stored as uint8_t bytes
//      - Entry size: 2 (key, value)
//      - Chain table separate from entries
//
//   2. OrderedHashMap: For larger maps (capacity >254)
//      - Metadata stored as Smis in FixedArray
//      - Entry size: 3 (key, value, chain)
//      - Chain stored inline with entries
//
// This code handles both types by detecting the table format at runtime.
// Practical testing shows that at least the AsyncContextFrame maps use the
// large map format even for small cardinality maps, but just in case we handle
// both.

#include <cstdint>

namespace dd {

using Address = uintptr_t;

#ifndef _WIN32
// ============================================================================
// Constants from V8 internals
// ============================================================================

// Heap object tagging
constexpr int kHeapObjectTag = 1;

// OrderedHashMap/SmallOrderedHashMap shared constants
constexpr int kNotFound = -1;
constexpr int kLoadFactor = 2;

// ============================================================================
// Helper Functions (needed by struct methods)
// ============================================================================

inline Address UntagPointer(Address tagged) {
  return tagged - kHeapObjectTag;
}

// IsSmi and SmiToInt implementations are valid only on 64-bit platforms, the
// only ones we support.
static_assert(sizeof(void*) == 8, "Only 64-bit platforms supported");

inline bool IsSmi(Address value) {
  // More rigorous than (value & 1) but valid on 64-bit platforms only.
  return (value & 0xFFFFFFFF) == 0;
}

inline int SmiToInt(Address smi) {
  return static_cast<int>(static_cast<intptr_t>(smi) >> 32);
}

// ============================================================================
// V8 Hashtable Structure Definitions
// ============================================================================

// HeapObject layout - base for all V8 heap objects
// From v8/src/objects/heap-object.h
struct HeapObjectLayout {
  Address classMap_;  // Tagged pointer to the class map
};

// JavaScript Map object
struct JSMapLayout {
  HeapObjectLayout header_;     // Map is a HeapObject
  Address properties_or_hash_;  // not used by us
  Address elements_;            // not used by us
  // Tagged pointer to a [Small]OrderedHashMapLayout
  Address table_;
};

// V8 FixedArray: length_ is a Smi, followed by that many element slots
struct FixedArrayLayout {
  HeapObjectLayout header_;  // FixedArray is a HeapObject
  Address length_;
  Address elements_[0];
};

// NOTE: both OrderedHashMap and SmallOrderedHashMap have compatible method
// definitions so FindEntryByHash and FindValueByHash can be defined as
// templated function working on both.

// OrderedHashMap layout (for large maps, capacity >254)
// From v8/src/objects/ordered-hash-table.h
struct OrderedHashMapLayout {
  FixedArrayLayout fixedArray_;  // OrderedHashMap is a FixedArray
  // The first 3 address slots in the FixedArray that is a Hashtable are the
  // number of elements, deleted elements, and buckets. Each one is a Smi.
  Address number_of_elements_;
  Address number_of_deleted_elements_;
  Address number_of_buckets_;
  // First number_of_buckets_ entries in head_and_data_table_ is the head table:
  // each entry is an index of the first entry (head of the linked list of
  // entries) in the data table for that bucket. This is followed by the data
  // table. Each data table entry uses three (kEntrySize == 3) tagged pointer
  // slots:
  //   [0]: key (Tagged Object)
  //   [1]: value (Tagged Object)
  //   [2]: chain (Smi - next entry index or -1)
  // All indices (both to the head of the list and to the next entry are
  // expressed in number of entries from the start of the data table, so to
  // convert it into a head_and_data_table_ you need to add number_of_buckets_
  // (length of the head table) and then 3 * index.
  Address head_and_data_table_[0];  // Variable: [head_table][data_table]

  // Constants for entry structure
  static constexpr int kEntrySize = 3;
  static constexpr int kKeyOffset = 0;
  static constexpr int kValueOffset = 1;
  static constexpr int kChainOffset = 2;
  static constexpr int kNotFoundValue = kNotFound;

  // Get number of buckets (converts Smi to int)
  int NumberOfBuckets() const { return SmiToInt(number_of_buckets_); }

  int GetEntryCount() const {
    return SmiToInt(number_of_elements_) +
           SmiToInt(number_of_deleted_elements_);
  }

  // Get first entry index for a bucket
  int GetFirstEntry(int bucket) const {
    Address entry_smi = head_and_data_table_[bucket];
    return IsSmi(entry_smi) ? SmiToInt(entry_smi) : kNotFound;
  }

  // Convert entry index to head_and_data_table_ index for the entry's key
  int EntryToIndex(int entry) const {
    return NumberOfBuckets() + (entry * kEntrySize);
  }

  // Get key at entry index
  Address GetKey(int entry) const {
    int index = EntryToIndex(entry);
    return head_and_data_table_[index + kKeyOffset];
  }

  // Get value at entry index
  Address GetValue(int entry) const {
    int index = EntryToIndex(entry);
    return head_and_data_table_[index + kValueOffset];
  }

  // Get next entry in chain
  int GetNextChainEntry(int entry) const {
    int index = EntryToIndex(entry);
    Address chain_smi = head_and_data_table_[index + kChainOffset];
    return IsSmi(chain_smi) ? SmiToInt(chain_smi) : kNotFound;
  }
};

// SmallOrderedHashMap layout (for small maps, capacity 4-254)
// Memory layout (stores metadata as uint8_t, not Smis):
//   [0]: map pointer (HeapObject)
//   [kHeaderSize + 0]: number_of_elements (uint8)
//   [kHeaderSize + 1]: number_of_deleted_elements (uint8)
//   [kHeaderSize + 2]: number_of_buckets (uint8)
//   [kHeaderSize + 3...]: padding (5 bytes on 64-bit, 1 byte on 32-bit)
//   [DataTableStartOffset...]: data table (key-value pairs as Tagged)
//   [...]: hash table (uint8 bucket indices)
//   [...]: chain table (uint8 next entry indices)
//
// Each entry is 2 Tagged elements (kEntrySize = 2):
//   [0]: key (Tagged Object)
//   [1]: value (Tagged Object)
//
// From v8/src/objects/ordered-hash-table.h
struct SmallOrderedHashMapLayout {
  HeapObjectLayout header_;
  uint8_t number_of_elements_;
  uint8_t number_of_deleted_elements_;
  uint8_t number_of_buckets_;
  uint8_t padding_[5];  // 5 bytes on 64-bit
  // Variable length:
  // - Address data_table_[capacity * kEntrySize]  // Keys and values
  // - uint8_t hash_table_[number_of_buckets_]     // Bucket -> first entry
  // - uint8_t chain_table_[capacity]              // Entry -> next entry
  Address data_table_[0];

  // Constants for entry structure
  static constexpr int kEntrySize = 2;
  static constexpr int kKeyOffset = 0;
  static constexpr int kValueOffset = 1;
  static constexpr int kNotFoundValue = 255;

  // Get capacity from number of buckets
  int Capacity() const { return number_of_buckets_ * kLoadFactor; }

  int NumberOfBuckets() const { return number_of_buckets_; }

  int GetEntryCount() const {
    return number_of_elements_ + number_of_deleted_elements_;
  }

  const uint8_t* GetHashTable() const {
    return reinterpret_cast<const uint8_t*>(data_table_ +
                                            Capacity() * kEntrySize);
  }

  const uint8_t* GetChainTable() const {
    return GetHashTable() + number_of_buckets_;
  }

  // Get key at entry index
  Address GetKey(int entry) const {
    return data_table_[entry * kEntrySize + kKeyOffset];
  }

  // Get value at entry index
  Address GetValue(int entry) const {
    return data_table_[entry * kEntrySize + kValueOffset];
  }

  // Get first entry in bucket
  uint8_t GetFirstEntry(int bucket) const {
    const uint8_t* hash_table = GetHashTable();
    return hash_table[bucket];
  }

  // Get next entry in chain
  uint8_t GetNextChainEntry(int entry) const {
    const uint8_t* chain_table = GetChainTable();
    return chain_table[entry];
  }
};

// ============================================================================
// Templated Hash Table Lookup
// ============================================================================

// Find an entry by a key and its hash in any hash table layout
// Template parameter LayoutT should be either OrderedHashMapLayout or
// SmallOrderedHashMapLayout
template <typename LayoutT>
int FindEntryByHash(const LayoutT* layout, int hash, Address key_to_find) {
  const int entry_count = layout->GetEntryCount();
  const int bucket = hash & (layout->NumberOfBuckets() - 1);
  int entry = layout->GetFirstEntry(bucket);

  // Paranoid: by never traversing more than the total number of entries in the
  // map we guarantee this terminates in bound time even if for some unforeseen
  // reason the chain is cyclical. Also, every entry value must be between
  // [0, GetEntryCount).
  for (int max_entries_left = entry_count;
       entry != LayoutT::kNotFoundValue && entry >= 0 && entry < entry_count &&
       max_entries_left > 0;
       max_entries_left--) {
    Address key_at_entry = layout->GetKey(entry);
    if (key_at_entry == key_to_find) {
      return entry;
    }
    entry = layout->GetNextChainEntry(entry);
  }

  return kNotFound;
}

// Find an entry by a key and its hash in any hash table layout, and return its
// value or the zero address if it is not found.
// Template parameter LayoutT should be either OrderedHashMapLayout or
// SmallOrderedHashMapLayout
template <typename LayoutT>
Address FindValueByHash(const LayoutT* layout, int hash, Address key_to_find) {
  auto entry = FindEntryByHash(layout, hash, key_to_find);
  return entry == kNotFound ? 0 : layout->GetValue(entry);
}

static bool IsSmallOrderedHashMap(Address table_untagged) {
  const SmallOrderedHashMapLayout* potential_small =
      reinterpret_cast<const SmallOrderedHashMapLayout*>(table_untagged);

  // Read the header as one 64-bit value for validation
  uint64_t smallHeader =
      *reinterpret_cast<const uint64_t*>(&potential_small->number_of_elements_);

  static_assert(__BYTE_ORDER__ == __ORDER_LITTLE_ENDIAN__,
                "Little-endian required");
  // Small map will have some bits in bytes 0-2 be nonzero, and all bits in
  // bytes 3-7 zero. That effectively limits the value range of smallHeader to
  // [0x1-0xFFFFFF].
  if (smallHeader == 0 || smallHeader >= 0x1000000) return false;

  auto num_elements = potential_small->number_of_elements_;
  auto num_deleted = potential_small->number_of_deleted_elements_;
  auto num_buckets = potential_small->number_of_buckets_;

  // num_buckets must be between 2 and 127
  if (num_buckets < 2 || num_buckets > 127) return false;

  // num_buckets must be a power of 2
  if ((num_buckets & (num_buckets - 1)) != 0) return false;

  auto capacity = num_buckets * kLoadFactor;
  // Sum of elements and deleted elements can't exceed capacity
  return num_elements + num_deleted <= capacity;
}

static bool IsOrderedHashMap(Address table_untagged) {
  const OrderedHashMapLayout* layout =
      reinterpret_cast<const OrderedHashMapLayout*>(table_untagged);

  // Let's validate its invariants!

  // Its length must be a Smi.
  if (!IsSmi(layout->fixedArray_.length_)) return false;
  auto length = SmiToInt(layout->fixedArray_.length_);

  // Must have at least 3 elements for number_of_* fields.
  if (length < 3) return false;

  // All of them must be Smis
  if (!IsSmi(layout->number_of_buckets_) ||
      !IsSmi(layout->number_of_deleted_elements_) ||
      !IsSmi(layout->number_of_elements_))
    return false;
  auto num_buckets = SmiToInt(layout->number_of_buckets_);
  auto num_deleted = SmiToInt(layout->number_of_deleted_elements_);
  auto num_elements = SmiToInt(layout->number_of_elements_);

  // num_buckets must be a power of 2
  if (num_buckets <= 0 || (num_buckets & (num_buckets - 1)) != 0) return false;
  auto capacity = num_buckets * kLoadFactor;

  // number of elements and number of deleted elements can't be negative, and
  // they can't add up to more than the capacity.
  if (num_elements < 0 || num_deleted < 0 ||
      num_elements + num_deleted > capacity)
    return false;

  // The length of the array must be enough to store the whole map.
  return length >=
         3 + num_buckets + OrderedHashMapLayout::kEntrySize * capacity;
}

// ============================================================================
// Main entry point
// ============================================================================

// Lookup value in a Map given the hash and key pointer. If the key is not found
// in the map (or the lookup can not be performed) returns a zero Address (which
// is essentially a zero Smi value.)
Address GetValueFromMap(Address map_addr, int hash, Address key) {
  const JSMapLayout* map_untagged =
      reinterpret_cast<const JSMapLayout*>(UntagPointer(map_addr));
  Address table_untagged = UntagPointer(map_untagged->table_);

  if (IsSmallOrderedHashMap(table_untagged)) {
    const SmallOrderedHashMapLayout* layout =
        reinterpret_cast<const SmallOrderedHashMapLayout*>(table_untagged);
    return FindValueByHash(layout, hash, key);
  } else if (IsOrderedHashMap(table_untagged)) {
    const OrderedHashMapLayout* layout =
        reinterpret_cast<const OrderedHashMapLayout*>(table_untagged);
    return FindValueByHash(layout, hash, key);
  }
  return 0;  // We couldn't determine the kind of the map, just return zero.
}

#else  // _WIN32

Address GetValueFromMap(Address map_addr, int hash, Address key) {
  return 0;
}

#endif  // _WIN32
}  // namespace dd
```

## File: `bindings/map-get.hh`
```
/**
 * Copyright 2025 Datadog. All Rights Reserved.
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

#pragma once

#include <cstdint>

using Address = uintptr_t;

namespace dd {
Address GetValueFromMap(Address map_addr, int hash, Address key);
}  // namespace dd
```

## File: `bindings/per-isolate-data.cc`
```
/*
 * Copyright 2023 Datadog, Inc
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include <mutex>
#include <unordered_map>
#include <utility>

#include "per-isolate-data.hh"

namespace dd {

static std::unordered_map<v8::Isolate*, PerIsolateData> per_isolate_data_;
static std::mutex mutex;

PerIsolateData* PerIsolateData::For(v8::Isolate* isolate) {
  const std::lock_guard<std::mutex> lock(mutex);
  auto maybe = per_isolate_data_.find(isolate);
  if (maybe != per_isolate_data_.end()) {
    return &maybe->second;
  }

  per_isolate_data_.emplace(std::make_pair(isolate, PerIsolateData()));

  auto pair = per_isolate_data_.find(isolate);
  auto perIsolateData = &pair->second;

  node::AddEnvironmentCleanupHook(
      isolate,
      [](void* data) {
        const std::lock_guard<std::mutex> lock(mutex);
        per_isolate_data_.erase(static_cast<v8::Isolate*>(data));
      },
      isolate);

  return perIsolateData;
}

Nan::Global<v8::Function>& PerIsolateData::WallProfilerConstructor() {
  return wall_profiler_constructor;
}

Nan::Global<v8::Function>& PerIsolateData::AllocationNodeConstructor() {
  return allocation_node_constructor;
}

Nan::Global<v8::Function>& PerIsolateData::TimeProfileNodeConstructor() {
  return time_profile_node_constructor;
}

std::shared_ptr<HeapProfilerState>& PerIsolateData::GetHeapProfilerState() {
  return heap_profiler_state;
}

}  // namespace dd
```

## File: `bindings/per-isolate-data.hh`
```
/*
 * Copyright 2023 Datadog, Inc
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#pragma once

#include <nan.h>
#include <node.h>
#include <v8.h>
#include <memory>

namespace dd {

struct HeapProfilerState;

class PerIsolateData {
 private:
  Nan::Global<v8::Function> wall_profiler_constructor;
  Nan::Global<v8::Function> allocation_node_constructor;
  Nan::Global<v8::Function> time_profile_node_constructor;
  std::shared_ptr<HeapProfilerState> heap_profiler_state;

  PerIsolateData() {}

 public:
  static PerIsolateData* For(v8::Isolate* isolate);

  Nan::Global<v8::Function>& WallProfilerConstructor();
  Nan::Global<v8::Function>& AllocationNodeConstructor();
  Nan::Global<v8::Function>& TimeProfileNodeConstructor();
  std::shared_ptr<HeapProfilerState>& GetHeapProfilerState();
};

}  // namespace dd
```

## File: `bindings/profile-translator.hh`
```
/*
 * Copyright 2024 Datadog, Inc
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include <v8.h>

namespace dd {
class ProfileTranslator {
  v8::Isolate* isolate = v8::Isolate::GetCurrent();
  v8::Local<v8::Context> context = isolate->GetCurrentContext();
  v8::Local<v8::Array> emptyArray = v8::Array::New(isolate, 0);

 protected:
  v8::Local<v8::Object> NewObject() { return v8::Object::New(isolate); }

  v8::Local<v8::Integer> NewInteger(int x) {
    return v8::Integer::New(isolate, x);
  }

  v8::Local<v8::Boolean> NewBoolean(bool x) {
    return v8::Boolean::New(isolate, x);
  }

  template <typename T>
  v8::Local<v8::Number> NewNumber(T x) {
    return v8::Number::New(isolate, x);
  }

  v8::Local<v8::Array> NewArray(int length) {
    return length == 0 ? emptyArray : v8::Array::New(isolate, length);
  }

  v8::Local<v8::String> NewString(const char* str) {
    return v8::String::NewFromUtf8(isolate, str).ToLocalChecked();
  }

  v8::MaybeLocal<v8::Value> Get(v8::Local<v8::Array> arr, uint32_t index) {
    return arr->Get(context, index);
  }

  v8::Maybe<bool> Set(v8::Local<v8::Array> arr,
                      uint32_t index,
                      v8::Local<v8::Value> value) {
    return arr->Set(context, index, value);
  }

  v8::Maybe<bool> Set(v8::Local<v8::Object> obj,
                      v8::Local<v8::Value> key,
                      v8::Local<v8::Value> value) {
    return obj->Set(context, key, value);
  }

  ProfileTranslator() = default;
};
};  // namespace dd
```

## File: `bindings/thread-cpu-clock.cc`
```
/*
 * Copyright 2023 Datadog, Inc
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "thread-cpu-clock.hh"

#ifdef __linux__
#include <errno.h>
#include <pthread.h>
#include <string.h>
#elif __APPLE__
#define _DARWIN_C_SOURCE
#include <mach/mach_error.h>
#include <mach/mach_init.h>
#include <mach/thread_act.h>
#elif _WIN32
#include <Windows.h>
#endif

namespace dd {

namespace {
constexpr std::chrono::nanoseconds timespec_to_duration(timespec ts) {
  return std::chrono::seconds{ts.tv_sec} + std::chrono::nanoseconds{ts.tv_nsec};
}

#ifdef _WIN32
constexpr std::chrono::nanoseconds filetime_to_nanos(FILETIME t) {
  return std::chrono::nanoseconds{
      ((static_cast<uint64_t>(t.dwHighDateTime) << 32) |
       static_cast<uint64_t>(t.dwLowDateTime)) *
      100};
}
#endif
}  // namespace

CurrentThreadCpuClock::time_point CurrentThreadCpuClock::now() noexcept {
#ifndef _WIN32
  timespec ts;
  clock_gettime(CLOCK_THREAD_CPUTIME_ID, &ts);
  return time_point{timespec_to_duration(ts)};
#else
  FILETIME creationTime, exitTime, kernelTime, userTime;
  if (!GetThreadTimes(GetCurrentThread(),
                      &creationTime,
                      &exitTime,
                      &kernelTime,
                      &userTime)) {
    return {};
  }
  return time_point{filetime_to_nanos(kernelTime) +
                    filetime_to_nanos(userTime)};
#endif
}

ProcessCpuClock::time_point ProcessCpuClock::now() noexcept {
#ifndef _WIN32
  timespec ts;
  clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &ts);
  return time_point{timespec_to_duration(ts)};
#else
  FILETIME creationTime, exitTime, kernelTime, userTime;
  if (!GetProcessTimes(GetCurrentProcess(),
                       &creationTime,
                       &exitTime,
                       &kernelTime,
                       &userTime)) {
    return {};
  }
  return time_point{filetime_to_nanos(kernelTime) +
                    filetime_to_nanos(userTime)};
#endif
}

ThreadCpuClock::ThreadCpuClock() {
#ifdef __linux__
  pthread_getcpuclockid(pthread_self(), &clockid_);
#elif __APPLE__
  thread_ = mach_thread_self();
#elif _WIN32
  thread_ = GetCurrentThread();
#endif
}

ThreadCpuClock::time_point ThreadCpuClock::now() const noexcept {
#ifdef __linux__
  timespec ts;
  if (clock_gettime(clockid_, &ts)) {
    return {};
  }
  return time_point{timespec_to_duration(ts)};
#elif __APPLE__
  mach_msg_type_number_t count = THREAD_BASIC_INFO_COUNT;
  thread_basic_info_data_t info;
  kern_return_t kr =
      thread_info(thread_, THREAD_BASIC_INFO, (thread_info_t)&info, &count);

  if (kr != KERN_SUCCESS) {
    return {};
  }

  return time_point{
      std::chrono::seconds{info.user_time.seconds + info.system_time.seconds} +
      std::chrono::microseconds{info.user_time.microseconds +
                                info.system_time.microseconds}};
#elif _WIN32
  FILETIME creationTime, exitTime, kernelTime, userTime;
  if (!GetThreadTimes(
          thread_, &creationTime, &exitTime, &kernelTime, &userTime)) {
    return {};
  }
  return time_point{filetime_to_nanos(kernelTime) +
                    filetime_to_nanos(userTime)};
#endif

  return {};
}

}  // namespace dd
```

## File: `bindings/thread-cpu-clock.hh`
```
/*
 * Copyright 2023 Datadog, Inc
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#pragma once

#include <chrono>
#include <cstdint>
#include <ctime>

#ifdef __linux__
#include <pthread.h>
#elif __APPLE__
#include <mach/mach.h>
#elif _WIN32
#include <Windows.h>
#endif

namespace dd {

struct CurrentThreadCpuClock {
  using duration = std::chrono::nanoseconds;
  using rep = duration::rep;
  using period = duration::period;
  using time_point = std::chrono::time_point<CurrentThreadCpuClock, duration>;

  static constexpr bool is_steady = true;

  static time_point now() noexcept;
};

struct ProcessCpuClock {
  using duration = std::chrono::nanoseconds;
  using rep = duration::rep;
  using period = duration::period;
  using time_point = std::chrono::time_point<ProcessCpuClock, duration>;

  static constexpr bool is_steady = true;

  static time_point now() noexcept;
};

class ThreadCpuClock {
 public:
  using duration = std::chrono::nanoseconds;
  using rep = duration::rep;
  using period = duration::period;
  using time_point = std::chrono::time_point<ThreadCpuClock, duration>;

  static constexpr bool is_steady = true;

  ThreadCpuClock();
  time_point now() const noexcept;

 private:
#ifdef __linux__
  clockid_t clockid_;
#elif __APPLE__
  mach_port_t thread_;
#elif _WIN32
  HANDLE thread_;
#endif
};

class ThreadCpuStopWatch {
 public:
  ThreadCpuStopWatch() { last_ = clock_.now(); }

  ThreadCpuClock::duration GetAndReset() {
    auto now = clock_.now();
    auto d = now - last_;
    last_ = now;
    return d;
  }

 private:
  ThreadCpuClock clock_;
  ThreadCpuClock::time_point last_;
};

}  // namespace dd
```

## File: `bindings/translate-heap-profile.cc`
```
/*
 * Copyright 2024 Datadog, Inc
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "translate-heap-profile.hh"
#include <nan.h>
#include "profile-translator.hh"

namespace dd {

namespace {
class HeapProfileTranslator : ProfileTranslator {
#define NODE_FIELDS                                                            \
  X(name)                                                                      \
  X(scriptName)                                                                \
  X(scriptId)                                                                  \
  X(lineNumber)                                                                \
  X(columnNumber)                                                              \
  X(children)                                                                  \
  X(allocations)

#define ALLOCATION_FIELDS                                                      \
  X(sizeBytes)                                                                 \
  X(count)

#define X(name) v8::Local<v8::String> str_##name = NewString(#name);
  NODE_FIELDS
  ALLOCATION_FIELDS
#undef X

 public:
  v8::Local<v8::Value> TranslateAllocationProfile(Node* node) {
    v8::Local<v8::Array> children = NewArray(node->children.size());
    for (size_t i = 0; i < node->children.size(); i++) {
      Set(children, i, TranslateAllocationProfile(node->children[i].get()));
    }

    v8::Local<v8::Array> allocations = NewArray(node->allocations.size());
    for (size_t i = 0; i < node->allocations.size(); i++) {
      auto alloc = node->allocations[i];
      Set(allocations,
          i,
          CreateAllocation(NewNumber(alloc.count), NewNumber(alloc.size)));
    }

    return CreateNode(NewString(node->name.c_str()),
                      NewString(node->script_name.c_str()),
                      NewInteger(node->script_id),
                      NewInteger(node->line_number),
                      NewInteger(node->column_number),
                      children,
                      allocations);
  }

 private:
  v8::Local<v8::Object> CreateNode(v8::Local<v8::String> name,
                                   v8::Local<v8::String> scriptName,
                                   v8::Local<v8::Integer> scriptId,
                                   v8::Local<v8::Integer> lineNumber,
                                   v8::Local<v8::Integer> columnNumber,
                                   v8::Local<v8::Array> children,
                                   v8::Local<v8::Array> allocations) {
    v8::Local<v8::Object> js_node = NewObject();
#define X(name) Set(js_node, str_##name, name);
    NODE_FIELDS
#undef X
#undef NODE_FIELDS
    return js_node;
  }

  v8::Local<v8::Object> CreateAllocation(v8::Local<v8::Number> count,
                                         v8::Local<v8::Number> sizeBytes) {
    v8::Local<v8::Object> js_alloc = NewObject();
#define X(name) Set(js_alloc, str_##name, name);
    ALLOCATION_FIELDS
#undef X
#undef ALLOCATION_FIELDS
    return js_alloc;
  }

 public:
  explicit HeapProfileTranslator() {}
};
}  // namespace

std::shared_ptr<Node> TranslateAllocationProfileToCpp(
    v8::AllocationProfile::Node* node) {
  auto new_node = std::make_shared<Node>();
  new_node->line_number = node->line_number;
  new_node->column_number = node->column_number;
  new_node->script_id = node->script_id;
  Nan::Utf8String name(node->name);
  new_node->name.assign(*name, name.length());
  Nan::Utf8String script_name(node->script_name);
  new_node->script_name.assign(*script_name, script_name.length());

  new_node->children.reserve(node->children.size());
  for (auto& child : node->children) {
    new_node->children.push_back(TranslateAllocationProfileToCpp(child));
  }

  new_node->allocations.reserve(node->allocations.size());
  for (auto& allocation : node->allocations) {
    new_node->allocations.push_back(allocation);
  }
  return new_node;
}

v8::Local<v8::Value> TranslateAllocationProfile(Node* node) {
  return HeapProfileTranslator().TranslateAllocationProfile(node);
}

}  // namespace dd
```

## File: `bindings/translate-heap-profile.hh`
```
/*
 * Copyright 2024 Datadog, Inc
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#pragma once

#include <v8-profiler.h>
#include <v8.h>
#include <memory>
#include <string>
#include <vector>

namespace dd {

struct Node {
  using Allocation = v8::AllocationProfile::Allocation;
  std::string name;
  std::string script_name;
  int line_number;
  int column_number;
  int script_id;
  std::vector<std::shared_ptr<Node>> children;
  std::vector<Allocation> allocations;
};

std::shared_ptr<Node> TranslateAllocationProfileToCpp(
    v8::AllocationProfile::Node* node);

v8::Local<v8::Value> TranslateAllocationProfile(Node* node);
}  // namespace dd
```

## File: `bindings/translate-time-profile.cc`
```
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

#include "translate-time-profile.hh"
#include <v8-version.h>
#include "per-isolate-data.hh"
#include "profile-translator.hh"

namespace dd {

namespace {

TimeProfileNodeInfo* AllocNode(TimeProfileViewState* state,
                               const v8::CpuProfileNode* node,
                               const v8::CpuProfileNode* metadata_node,
                               int line_number,
                               int column_number,
                               int hit_count,
                               bool is_line_root = false) {
  auto info = std::make_unique<TimeProfileNodeInfo>();
  info->node = node;
  info->metadata_node = metadata_node;
  info->line_number = line_number;
  info->column_number = column_number;
  info->hit_count = hit_count;
  info->is_line_root = is_line_root;
  info->state = state;
  auto* raw = info.get();
  state->owned_nodes.push_back(std::move(info));
  return raw;
}

// Line-info mode: for a given V8 node, append its line ticks (leaves with
// hit_count > 0) and child calls (intermediate nodes with hit_count 0).
void AppendLineChildren(TimeProfileViewState* state,
                        const v8::CpuProfileNode* node,
                        std::vector<TimeProfileNodeInfo*>& out) {
  unsigned int hitLineCount = node->GetHitLineCount();
  unsigned int hitCount = node->GetHitCount();

  if (hitLineCount > 0) {
    std::vector<v8::CpuProfileNode::LineTick> entries(hitLineCount);
    node->GetLineTicks(&entries[0], hitLineCount);
    for (const auto& entry : entries) {
      int column = 0;
#if V8_MAJOR_VERSION >= 14
      column = entry.column;
#endif
      out.push_back(
          AllocNode(state, node, node, entry.line, column, entry.hit_count));
    }
  } else if (hitCount > 0) {
    out.push_back(AllocNode(state,
                            node,
                            node,
                            node->GetLineNumber(),
                            node->GetColumnNumber(),
                            hitCount));
  }

  int32_t count = node->GetChildrenCount();
  for (int32_t i = 0; i < count; i++) {
    auto* child = node->GetChild(i);
    out.push_back(AllocNode(state,
                            child,
                            node,
                            child->GetLineNumber(),
                            child->GetColumnNumber(),
                            0));
  }
}

int ResolveHitCount(const v8::CpuProfileNode* node, ContextsByNode* cbn) {
  if (!cbn) return node->GetHitCount();
  auto it = cbn->find(node);
  return it != cbn->end() ? it->second.hitcount : 0;
}

int ComputeTotalHitCount(const v8::CpuProfileNode* node, ContextsByNode* cbn) {
  int total = ResolveHitCount(node, cbn);
  int32_t count = node->GetChildrenCount();
  for (int32_t i = 0; i < count; i++) {
    total += ComputeTotalHitCount(node->GetChild(i), cbn);
  }
  return total;
}

// WrapNode: create a JS wrapper for a profile node.
// Normal mode stores CpuProfileNode* directly.
// line-info mode stores owned info.
v8::Local<v8::Object> WrapNode(const v8::CpuProfileNode* node,
                               TimeProfileViewState* state) {
  auto* isolate = v8::Isolate::GetCurrent();
  auto ctor =
      Nan::New(PerIsolateData::For(isolate)->TimeProfileNodeConstructor());
  auto obj = Nan::NewInstance(ctor).ToLocalChecked();
  Nan::SetInternalFieldPointer(obj, 0, const_cast<v8::CpuProfileNode*>(node));
  Nan::SetInternalFieldPointer(obj, 1, state);
  return obj;
}

v8::Local<v8::Object> WrapNode(TimeProfileNodeInfo* info) {
  auto* isolate = v8::Isolate::GetCurrent();
  auto ctor =
      Nan::New(PerIsolateData::For(isolate)->TimeProfileNodeConstructor());
  auto obj = Nan::NewInstance(ctor).ToLocalChecked();
  Nan::SetInternalFieldPointer(obj, 0, info);
  Nan::SetInternalFieldPointer(obj, 1, info->state);
  return obj;
}

// Extracts the two internal fields from a JS wrapper object.
// field 0 represents the node data (depends on mode, see below).
// field 1 TimeProfileViewState* (shared state, always present).
//
// Line-info: field 0 is a TimeProfileNodeInfo* holding synthetic
// line/column/hitCount values. Normal: field 0 is a CpuProfileNode* pointing
// directly to V8.
struct NodeFields {
  void* ptr;
  TimeProfileViewState* state;

  bool is_line_info() const { return state->include_line_info; }

  TimeProfileNodeInfo* as_info() const {
    return static_cast<TimeProfileNodeInfo*>(ptr);
  }

  const v8::CpuProfileNode* as_node() const {
    return static_cast<const v8::CpuProfileNode*>(ptr);
  }
};

NodeFields GetFields(const Nan::PropertyCallbackInfo<v8::Value>& info) {
  return {Nan::GetInternalFieldPointer(info.Holder(), 0),
          static_cast<TimeProfileViewState*>(
              Nan::GetInternalFieldPointer(info.Holder(), 1))};
}

NAN_GETTER(GetName) {
  auto fields = GetFields(info);
  if (fields.is_line_info()) {
    info.GetReturnValue().Set(
        fields.as_info()->metadata_node->GetFunctionName());
  } else {
    info.GetReturnValue().Set(fields.as_node()->GetFunctionName());
  }
}

NAN_GETTER(GetScriptName) {
  auto fields = GetFields(info);
  if (fields.is_line_info()) {
    info.GetReturnValue().Set(
        fields.as_info()->metadata_node->GetScriptResourceName());
  } else {
    info.GetReturnValue().Set(fields.as_node()->GetScriptResourceName());
  }
}

NAN_GETTER(GetScriptId) {
  auto fields = GetFields(info);
  if (fields.is_line_info()) {
    info.GetReturnValue().Set(
        Nan::New<v8::Integer>(fields.as_info()->metadata_node->GetScriptId()));
  } else {
    info.GetReturnValue().Set(
        Nan::New<v8::Integer>(fields.as_node()->GetScriptId()));
  }
}

NAN_GETTER(GetLineNumber) {
  auto fields = GetFields(info);
  if (fields.is_line_info()) {
    info.GetReturnValue().Set(
        Nan::New<v8::Integer>(fields.as_info()->line_number));
  } else {
    info.GetReturnValue().Set(
        Nan::New<v8::Integer>(fields.as_node()->GetLineNumber()));
  }
}

NAN_GETTER(GetColumnNumber) {
  auto fields = GetFields(info);
  if (fields.is_line_info()) {
    info.GetReturnValue().Set(
        Nan::New<v8::Integer>(fields.as_info()->column_number));
  } else {
    info.GetReturnValue().Set(
        Nan::New<v8::Integer>(fields.as_node()->GetColumnNumber()));
  }
}

NAN_GETTER(GetHitCount) {
  auto fields = GetFields(info);
  if (fields.is_line_info()) {
    info.GetReturnValue().Set(
        Nan::New<v8::Integer>(fields.as_info()->hit_count));
  } else {
    info.GetReturnValue().Set(Nan::New<v8::Integer>(
        ResolveHitCount(fields.as_node(), fields.state->contexts_by_node)));
  }
}

NAN_GETTER(GetContexts) {
  auto fields = GetFields(info);
  auto* isolate = v8::Isolate::GetCurrent();
  // Line-info nodes and nodes without context tracking return empty contexts.
  if (fields.is_line_info() || !fields.state->contexts_by_node) {
    info.GetReturnValue().Set(v8::Array::New(isolate, 0));
    return;
  }
  auto it = fields.state->contexts_by_node->find(fields.as_node());
  if (it != fields.state->contexts_by_node->end()) {
    info.GetReturnValue().Set(it->second.contexts);
  } else {
    info.GetReturnValue().Set(v8::Array::New(isolate, 0));
  }
}

NAN_GETTER(GetChildren) {
  auto fields = GetFields(info);
  auto* isolate = info.GetIsolate();
  auto ctx = isolate->GetCurrentContext();

  if (fields.is_line_info()) {
    std::vector<TimeProfileNodeInfo*> children;

    // Root in line-info mode is flattened from each direct child to preserve
    // eager v1 top-level shape.
    if (fields.as_info()->is_line_root) {
      int32_t count = fields.as_info()->node->GetChildrenCount();
      for (int32_t i = 0; i < count; i++) {
        AppendLineChildren(
            fields.state, fields.as_info()->node->GetChild(i), children);
      }
      auto arr = v8::Array::New(isolate, children.size());
      for (size_t i = 0; i < children.size(); i++) {
        arr->Set(ctx, i, WrapNode(children[i])).Check();
      }
      info.GetReturnValue().Set(arr);
      return;
    }

    // In line-info mode, leaf nodes (hitCount > 0) have no children.
    if (fields.as_info()->hit_count > 0) {
      info.GetReturnValue().Set(v8::Array::New(isolate, 0));
      return;
    }

    AppendLineChildren(fields.state, fields.as_info()->node, children);
    auto arr = v8::Array::New(isolate, children.size());
    for (size_t i = 0; i < children.size(); i++) {
      arr->Set(ctx, i, WrapNode(children[i])).Check();
    }
    info.GetReturnValue().Set(arr);
  } else {
    int32_t count = fields.as_node()->GetChildrenCount();
    auto arr = v8::Array::New(isolate, count);
    for (int32_t i = 0; i < count; i++) {
      arr->Set(ctx, i, WrapNode(fields.as_node()->GetChild(i), fields.state))
          .Check();
    }
    info.GetReturnValue().Set(arr);
  }
}

class TimeProfileTranslator : ProfileTranslator {
 private:
  ContextsByNode* contextsByNode;
  v8::Local<v8::Array> emptyArray = NewArray(0);
  v8::Local<v8::Integer> zero = NewInteger(0);

#define FIELDS                                                                 \
  X(name)                                                                      \
  X(scriptName)                                                                \
  X(scriptId)                                                                  \
  X(lineNumber)                                                                \
  X(columnNumber)                                                              \
  X(hitCount)                                                                  \
  X(children)                                                                  \
  X(contexts)

#define X(name) v8::Local<v8::String> str_##name = NewString(#name);
  FIELDS
#undef X

  v8::Local<v8::Array> getContextsForNode(const v8::CpuProfileNode* node,
                                          uint32_t& hitcount) {
    hitcount = node->GetHitCount();
    if (!contextsByNode) {
      // custom contexts are not enabled, keep the node hitcount and return
      // empty array
      return emptyArray;
    }

    auto it = contextsByNode->find(node);
    auto contexts = emptyArray;
    if (it != contextsByNode->end()) {
      hitcount = it->second.hitcount;
      contexts = it->second.contexts;
    } else {
      // no context found for node, discard it since every sample taken from
      // signal handler should have a matching context if it does not, it means
      // sample was captured by a deopt event
      hitcount = 0;
    }
    return contexts;
  }

  v8::Local<v8::Object> CreateTimeNode(v8::Local<v8::String> name,
                                       v8::Local<v8::String> scriptName,
                                       v8::Local<v8::Integer> scriptId,
                                       v8::Local<v8::Integer> lineNumber,
                                       v8::Local<v8::Integer> columnNumber,
                                       v8::Local<v8::Integer> hitCount,
                                       v8::Local<v8::Array> children,
                                       v8::Local<v8::Array> contexts) {
    v8::Local<v8::Object> js_node = NewObject();
#define X(name) Set(js_node, str_##name, name);
    FIELDS
#undef X
#undef FIELDS
    return js_node;
  }

  v8::Local<v8::Array> GetLineNumberTimeProfileChildren(
      const v8::CpuProfileNode* node) {
    unsigned int index = 0;
    v8::Local<v8::Array> children;
    int32_t count = node->GetChildrenCount();

    unsigned int hitLineCount = node->GetHitLineCount();
    unsigned int hitCount = node->GetHitCount();
    auto scriptId = NewInteger(node->GetScriptId());
    if (hitLineCount > 0) {
      std::vector<v8::CpuProfileNode::LineTick> entries(hitLineCount);
      node->GetLineTicks(&entries[0], hitLineCount);
      children = NewArray(count + hitLineCount);
      for (const v8::CpuProfileNode::LineTick entry : entries) {
        Set(children,
            index++,
            CreateTimeNode(node->GetFunctionName(),
                           node->GetScriptResourceName(),
                           scriptId,
                           NewInteger(entry.line),
// V8 14+ (Node.js 25+) added column field to LineTick struct
#if V8_MAJOR_VERSION >= 14
                           NewInteger(entry.column),
#else
                           zero,
#endif
                           NewInteger(entry.hit_count),
                           emptyArray,
                           emptyArray));
      }
    } else if (hitCount > 0) {
      // Handle nodes for pseudo-functions like "process" and "garbage
      // collection" which do not have hit line counts.
      children = NewArray(count + 1);
      Set(children,
          index++,
          CreateTimeNode(node->GetFunctionName(),
                         node->GetScriptResourceName(),
                         scriptId,
                         NewInteger(node->GetLineNumber()),
                         NewInteger(node->GetColumnNumber()),
                         NewInteger(hitCount),
                         emptyArray,
                         emptyArray));
    } else {
      children = NewArray(count);
    }

    for (int32_t i = 0; i < count; i++) {
      Set(children,
          index++,
          TranslateLineNumbersTimeProfileNode(node, node->GetChild(i)));
    };

    return children;
  }

  v8::Local<v8::Object> TranslateLineNumbersTimeProfileNode(
      const v8::CpuProfileNode* parent, const v8::CpuProfileNode* node) {
    return CreateTimeNode(parent->GetFunctionName(),
                          parent->GetScriptResourceName(),
                          NewInteger(parent->GetScriptId()),
                          NewInteger(node->GetLineNumber()),
                          NewInteger(node->GetColumnNumber()),
                          zero,
                          GetLineNumberTimeProfileChildren(node),
                          emptyArray);
  }

  // In profiles with line level accurate line numbers, a node's line number
  // and column number refer to the line/column from which the function was
  // called.
  v8::Local<v8::Value> TranslateLineNumbersTimeProfileRoot(
      const v8::CpuProfileNode* node) {
    int32_t count = node->GetChildrenCount();
    std::vector<v8::Local<v8::Array>> childrenArrs(count);
    int32_t childCount = 0;
    for (int32_t i = 0; i < count; i++) {
      v8::Local<v8::Array> c =
          GetLineNumberTimeProfileChildren(node->GetChild(i));
      childCount = childCount + c->Length();
      childrenArrs[i] = c;
    }

    v8::Local<v8::Array> children = NewArray(childCount);
    int32_t idx = 0;
    for (int32_t i = 0; i < count; i++) {
      v8::Local<v8::Array> arr = childrenArrs[i];
      for (uint32_t j = 0; j < arr->Length(); j++) {
        Set(children, idx, Get(arr, j).ToLocalChecked());
        idx++;
      }
    }

    return CreateTimeNode(node->GetFunctionName(),
                          node->GetScriptResourceName(),
                          NewInteger(node->GetScriptId()),
                          NewInteger(node->GetLineNumber()),
                          NewInteger(node->GetColumnNumber()),
                          zero,
                          children,
                          emptyArray);
  }

  v8::Local<v8::Value> TranslateTimeProfileNode(
      const v8::CpuProfileNode* node) {
    int32_t count = node->GetChildrenCount();
    v8::Local<v8::Array> children = NewArray(count);
    for (int32_t i = 0; i < count; i++) {
      Set(children, i, TranslateTimeProfileNode(node->GetChild(i)));
    }

    uint32_t hitcount = 0;
    auto contexts = getContextsForNode(node, hitcount);

    return CreateTimeNode(node->GetFunctionName(),
                          node->GetScriptResourceName(),
                          NewInteger(node->GetScriptId()),
                          NewInteger(node->GetLineNumber()),
                          NewInteger(node->GetColumnNumber()),
                          NewInteger(hitcount),
                          children,
                          contexts);
  }

 public:
  explicit TimeProfileTranslator(ContextsByNode* nls = nullptr)
      : contextsByNode(nls) {}

  v8::Local<v8::Value> TranslateTimeProfile(const v8::CpuProfile* profile,
                                            bool includeLineInfo,
                                            bool hasCpuTime,
                                            int64_t nonJSThreadsCpuTime) {
    v8::Local<v8::Object> js_profile = NewObject();

    if (includeLineInfo) {
      Set(js_profile,
          NewString("topDownRoot"),
          TranslateLineNumbersTimeProfileRoot(profile->GetTopDownRoot()));
    } else {
      Set(js_profile,
          NewString("topDownRoot"),
          TranslateTimeProfileNode(profile->GetTopDownRoot()));
    }
    Set(js_profile, NewString("startTime"), NewNumber(profile->GetStartTime()));
    Set(js_profile, NewString("endTime"), NewNumber(profile->GetEndTime()));
    Set(js_profile, NewString("hasCpuTime"), NewBoolean(hasCpuTime));

    Set(js_profile,
        NewString("nonJSThreadsCpuTime"),
        NewNumber(nonJSThreadsCpuTime));
    return js_profile;
  }
};
}  // namespace

NAN_MODULE_INIT(TimeProfileNodeView::Init) {
  v8::Local<v8::FunctionTemplate> tpl = Nan::New<v8::FunctionTemplate>();
  tpl->SetClassName(Nan::New("TimeProfileNode").ToLocalChecked());
  tpl->InstanceTemplate()->SetInternalFieldCount(2);

  auto inst = tpl->InstanceTemplate();
  Nan::SetAccessor(inst, Nan::New("name").ToLocalChecked(), GetName);
  Nan::SetAccessor(
      inst, Nan::New("scriptName").ToLocalChecked(), GetScriptName);
  Nan::SetAccessor(inst, Nan::New("scriptId").ToLocalChecked(), GetScriptId);
  Nan::SetAccessor(
      inst, Nan::New("lineNumber").ToLocalChecked(), GetLineNumber);
  Nan::SetAccessor(
      inst, Nan::New("columnNumber").ToLocalChecked(), GetColumnNumber);
  Nan::SetAccessor(inst, Nan::New("hitCount").ToLocalChecked(), GetHitCount);
  Nan::SetAccessor(inst, Nan::New("children").ToLocalChecked(), GetChildren);
  Nan::SetAccessor(inst, Nan::New("contexts").ToLocalChecked(), GetContexts);

  PerIsolateData::For(v8::Isolate::GetCurrent())
      ->TimeProfileNodeConstructor()
      .Reset(Nan::GetFunction(tpl).ToLocalChecked());
}

// Builds a lazy JS profile view.
// For non-line-info, wrappers store raw CpuProfileNode pointers.
// For line-info, owned TimeProfileNodeInfo structs are used for synthetic
// nodes.
v8::Local<v8::Value> BuildTimeProfileView(const v8::CpuProfile* profile,
                                          bool has_cpu_time,
                                          int64_t non_js_threads_cpu_time,
                                          TimeProfileViewState& state) {
  auto* isolate = v8::Isolate::GetCurrent();
  v8::Local<v8::Object> js_profile = v8::Object::New(isolate);

  auto* root_node = profile->GetTopDownRoot();

  if (state.include_line_info) {
    auto* root_info = AllocNode(&state,
                                root_node,
                                root_node,
                                root_node->GetLineNumber(),
                                root_node->GetColumnNumber(),
                                0,
                                true);
    auto root = WrapNode(root_info);

    Nan::Set(js_profile, Nan::New("topDownRoot").ToLocalChecked(), root);
  } else {
    Nan::Set(js_profile,
             Nan::New("topDownRoot").ToLocalChecked(),
             WrapNode(root_node, &state));
  }
  Nan::Set(js_profile,
           Nan::New("startTime").ToLocalChecked(),
           Nan::New<v8::Number>(profile->GetStartTime()));
  Nan::Set(js_profile,
           Nan::New("endTime").ToLocalChecked(),
           Nan::New<v8::Number>(profile->GetEndTime()));
  Nan::Set(js_profile,
           Nan::New("hasCpuTime").ToLocalChecked(),
           Nan::New(has_cpu_time));
  Nan::Set(js_profile,
           Nan::New("nonJSThreadsCpuTime").ToLocalChecked(),
           Nan::New<v8::Number>(non_js_threads_cpu_time));
  Nan::Set(js_profile,
           Nan::New("totalHitCount").ToLocalChecked(),
           Nan::New<v8::Integer>(
               ComputeTotalHitCount(root_node, state.contexts_by_node)));
  return js_profile;
}

v8::Local<v8::Value> TranslateTimeProfile(const v8::CpuProfile* profile,
                                          bool includeLineInfo,
                                          ContextsByNode* contextsByNode,
                                          bool hasCpuTime,
                                          int64_t nonJSThreadsCpuTime) {
  return TimeProfileTranslator(contextsByNode)
      .TranslateTimeProfile(
          profile, includeLineInfo, hasCpuTime, nonJSThreadsCpuTime);
}

}  // namespace dd
```

## File: `bindings/translate-time-profile.hh`
```
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

#pragma once

#include <nan.h>
#include <v8-profiler.h>
#include <cstdint>
#include <memory>
#include <vector>
#include "contexts.hh"

namespace dd {

struct TimeProfileNodeInfo;

// Shared state for the lazy profile view.
// In line-info mode, owned_nodes keeps synthetic TimeProfileNodeInfo objects
// alive for as long as JS wrappers may reference them.
// In normal mode, owned_nodes stays empty - wrappers point directly to V8
// nodes.
struct TimeProfileViewState {
  bool include_line_info;
  ContextsByNode* contexts_by_node;
  std::vector<std::unique_ptr<TimeProfileNodeInfo>> owned_nodes;
};

// Line-info mode only: stored in internal field 0 of JS wrappers.
// Needed because line-info nodes have line/column/hitCount values
// and a metadata_node that differs from the traversal node.
struct TimeProfileNodeInfo {
  const v8::CpuProfileNode* node;
  const v8::CpuProfileNode* metadata_node;
  int line_number;
  int column_number;
  int hit_count;
  bool is_line_root;
  TimeProfileViewState* state;
};

class TimeProfileNodeView {
 public:
  static NAN_MODULE_INIT(Init);
};

v8::Local<v8::Value> BuildTimeProfileView(const v8::CpuProfile* profile,
                                          bool has_cpu_time,
                                          int64_t non_js_threads_cpu_time,
                                          TimeProfileViewState& state);

v8::Local<v8::Value> TranslateTimeProfile(
    const v8::CpuProfile* profile,
    bool includeLineInfo,
    ContextsByNode* contextsByNode = nullptr,
    bool hasCpuTime = false,
    int64_t nonJSThreadsCpuTime = 0);

}  // namespace dd
```

## File: `bindings/wrap.hh`
```
/*
 * Copyright 2023 Datadog, Inc
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#pragma once

#include <v8.h>  // cppcheck-suppress missingIncludeSystem

namespace dd {

class LabelWrap {
 protected:
  v8::Global<v8::Value> handle_;

 public:
  LabelWrap(v8::Local<v8::Value> object)
      : handle_(v8::Isolate::GetCurrent(), object) {}

  v8::Local<v8::Value> handle() {
    return handle_.Get(v8::Isolate::GetCurrent());
  }
};

};  // namespace dd
```

## File: `bindings/profilers/heap.cc`
```
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

#include "heap.hh"

#include "defer.hh"
#include "per-isolate-data.hh"
#include "translate-heap-profile.hh"

#include <chrono>
#include <memory>
#include <mutex>
#include <unordered_set>
#include <vector>

#include <node.h>
#include <v8-profiler.h>
#include "allocation-profile-node.hh"

namespace dd {

// Track which isolates have cleanup hooks registered for heap profiler
static std::unordered_set<v8::Isolate*> g_heap_profiler_isolates;
static std::mutex g_heap_profiler_mutex;

// Cleanup hook to stop heap profiler before isolate is destroyed
static void HeapProfilerCleanupHook(void* data) {
  auto isolate = static_cast<v8::Isolate*>(data);
  {
    const std::lock_guard<std::mutex> lock(g_heap_profiler_mutex);
    g_heap_profiler_isolates.erase(isolate);
  }
  // Stop the sampling heap profiler to prevent crash during V8 teardown
  auto heap_profiler = isolate->GetHeapProfiler();
  if (heap_profiler) {
    heap_profiler->StopSamplingHeapProfiler();
  }
}

static size_t NearHeapLimit(void* data,
                            size_t current_heap_limit,
                            size_t initial_heap_limit);
static void InterruptCallback(v8::Isolate* isolate, void* data);
static void AsyncCallback(uv_async_t* handle);

enum CallbackMode {
  kNoCallback = 0,
  kAsyncCallback = 1,
  kInterruptCallback = 2,
};

struct HeapProfilerState {
  explicit HeapProfilerState(v8::Isolate* isolate) : isolate(isolate) {}

  ~HeapProfilerState() {
    auto profiler = isolate->GetHeapProfiler();
    if (profiler) {
      profiler->StopSamplingHeapProfiler();
    }

    UninstallNearHeapLimitCallback();
    if (async) {
      // defer deletion of async when uv_close callback is invoked
      uv_close(reinterpret_cast<uv_handle_t*>(async), [](uv_handle_t* handle) {
        delete reinterpret_cast<uv_async_t*>(handle);
      });
      async = nullptr;
    }
  }

  void UninstallNearHeapLimitCallback() {
    if (isolate && callbackInstalled) {
      isolate->RemoveNearHeapLimitCallback(&NearHeapLimit, 0);
      callbackInstalled = false;
    }
  }

  void InstallNearHeapLimitCallback() {
    if (isolate) {
      isolate->AddNearHeapLimitCallback(&NearHeapLimit, nullptr);
      callbackInstalled = true;
    }
  }

  void RegisterAsyncCallback() {
    if (async) {
      return;
    }
    // async is dynamically allocated so that its lifetime can be different
    // from the one of HeapProfilerState since uv_close is asynchronous
    async = new uv_async_t();
    uv_async_init(Nan::GetCurrentEventLoop(), async, AsyncCallback);
    uv_unref(reinterpret_cast<uv_handle_t*>(async));
  }

  void OnNewProfile() {
    profile.reset();
    if (!callbackInstalled) {
      // Reinstall NearHeapLimit callback if it was removed before
      InstallNearHeapLimitCallback();
    }
  }

  v8::Isolate* isolate = nullptr;
  uint32_t heap_extension_size = 0;
  uint32_t max_heap_extension_count = 0;
  uint32_t current_heap_extension_count = 0;
  uv_async_t* async = nullptr;
  std::shared_ptr<Node> profile;
  std::vector<std::string> export_command;
  bool dumpProfileOnStderr = false;
  Nan::Callback callback;
  uint32_t callbackMode = 0;
  bool isMainThread = true;
  bool callbackInstalled = false;
  bool insideCallback = false;
};

static void dumpAllocationProfile(FILE* file,
                                  Node* node,
                                  std::string& cur_stack) {
  auto initial_len = cur_stack.size();
  char buf[256];

  snprintf(buf,
           sizeof(buf),
           "%s%s:%s:%d",
           cur_stack.empty() ? "" : ";",
           node->script_name.empty() ? "_" : node->script_name.c_str(),
           node->name.empty() ? "(anonymous)" : node->name.c_str(),
           node->line_number);
  cur_stack += buf;
  for (auto& allocation : node->allocations) {
    fprintf(file,
            "%s %u %zu\n",
            cur_stack.c_str(),
            allocation.count,
            allocation.count * allocation.size);
  }
  for (auto& child : node->children) {
    dumpAllocationProfile(file, child.get(), cur_stack);
  }
  cur_stack.resize(initial_len);
}

static void dumpAllocationProfile(FILE* file, Node* node) {
  std::string stack;
  dumpAllocationProfile(file, node, stack);
}

static void dumpAllocationProfileAsJSON(FILE* file, Node* node) {
  fprintf(
      file,
      R"({"name":"%s","scriptName":"%s","scriptId":%d,"lineNumber":%d,"columnNumber":%d,"children":[)",
      node->name.c_str(),
      node->script_name.c_str(),
      node->script_id,
      node->line_number,
      node->column_number);

  bool first = true;
  for (auto& child : node->children) {
    if (!first) {
      fputs(",", file);
    } else {
      first = false;
    }
    dumpAllocationProfileAsJSON(file, child.get());
  }
  fprintf(file, R"(],"allocations":[)");
  first = true;
  for (auto& allocation : node->allocations) {
    fprintf(file,
            R"(%s{"sizeBytes":%zu,"count":%d})",
            first ? "" : ",",
            allocation.size,
            allocation.count);
    first = false;
  }
  fputs("]}", file);
}

static void OnExit(uv_process_t* req, int64_t, int) {
  if (req->data) {
    uv_timer_stop(reinterpret_cast<uv_timer_t*>(req->data));
  }
  uv_close((uv_handle_t*)req, nullptr);
}

static void CloseLoop(uv_loop_t& loop) {
  uv_run(&loop, UV_RUN_DEFAULT);
  uv_walk(
      &loop,
      [](uv_handle_t* handle, void* arg) {
        if (!uv_is_closing(handle)) {
          uv_close(handle, nullptr);
        }
      },
      nullptr);
  int r;
  do {
    r = uv_run(&loop, UV_RUN_ONCE);
  } while (r != 0);

  if (uv_loop_close(&loop)) {
    fprintf(stderr, "Failed to close event loop\n");
  }
}

static int CreateTempFile(uv_loop_t& loop, std::string& filepath) {
  char buf[PATH_MAX];
  size_t sz = sizeof(buf);
  int r;
  if ((r = uv_os_tmpdir(buf, &sz)) != 0) {
    fprintf(stderr, "Failed to retrieve temp directory: %s\n", uv_strerror(r));
    return -1;
  }

#if defined(__linux__) || defined(__APPLE__)
  filepath = std::string{buf, sz} + "/heap_profile_XXXXXX";
  int fd = mkstemp(&filepath[0]);
  if (fd < 0) {
    fprintf(stderr,
            "Failed to create temp file %s : %s\n",
            filepath.c_str(),
            strerror(errno));
    return -1;
  }
  return fd;
#else
  // Use custom implementation of mkstemp() for Windows
  // uv_fs_mkstemp() is not used because it fails unexpectedly on Windows
  // (fail fast exception is raised when trying to write to the returned file
  // descriptor)
  const int max_tries = 3;
  for (int i = 0; i < max_tries; ++i) {
    filepath = std::string{buf, sz} + "/heap_profile_" +
               std::to_string(
                   std::chrono::system_clock::now().time_since_epoch().count());
    uv_fs_t fs_req{};
    int fd = uv_fs_open(&loop,
                        &fs_req,
                        filepath.c_str(),
                        UV_FS_O_CREAT | UV_FS_O_EXCL | UV_FS_O_WRONLY,
                        0600,
                        nullptr);
    uv_fs_req_cleanup(&fs_req);
    if (fd >= 0) {
      return r;
    }
    if (fd != UV_EEXIST) {
      fprintf(stderr, "Failed to create temp file: %s\n", uv_strerror(fd));
      return -1;
    }
  }
  return -1;
#endif
}

static void ExportProfile(HeapProfilerState& state) {
  const int64_t timeoutMs = 15000;
  uv_loop_t loop;
  int r;

  if ((r = uv_loop_init(&loop)) != 0) {
    fprintf(stderr, "Failed to init new event loop: %s\n", uv_strerror(r));
    return;
  }

  defer {
    CloseLoop(loop);
  };

  std::string filepath;
  int fd;
  if ((fd = CreateTempFile(loop, filepath)) < 0) {
    return;
  }
  FILE* file = fdopen(fd, "w");
  dumpAllocationProfileAsJSON(file, state.profile.get());
  fclose(file);
  std::vector<char*> args;
  for (auto& arg : state.export_command) {
    args.push_back(const_cast<char*>(arg.data()));
  }
  args.push_back(&filepath[0]);
  args.push_back(nullptr);
  uv_process_options_t options = {};
  options.flags = UV_PROCESS_DETACHED;
  options.file = args[0];
  options.args = args.data();
  options.exit_cb = &OnExit;
  uv_stdio_container_t child_stdio[3];
  child_stdio[0].flags = UV_IGNORE;
  child_stdio[1].flags = UV_INHERIT_FD;
  child_stdio[1].data.fd = 2;
  child_stdio[2].flags = UV_INHERIT_FD;
  child_stdio[2].data.fd = 2;
  options.stdio = child_stdio;
  options.stdio_count = 3;
  uv_process_t child_req;
  uv_timer_t timer;
  timer.data = &child_req;
  child_req.data = &timer;

  fprintf(stderr, "Spawning export process:");
  for (auto arg : args) {
    fprintf(stderr, " %s", arg ? arg : "\n");
  }
  if ((r = uv_spawn(&loop, &child_req, &options))) {
    fprintf(stderr, "Failed to spawn export process: %s\n", uv_strerror(r));
    return;
  }
  if ((r = uv_timer_init(&loop, &timer)) != 0) {
    fprintf(stderr, "Failed to init timer: %s\n", uv_strerror(r));
    return;
  }
  if ((r = uv_timer_start(
           &timer,
           [](uv_timer_t* handle) {
             uv_process_kill(reinterpret_cast<uv_process_t*>(handle->data),
                             SIGKILL);
           },
           timeoutMs,
           0))) {
    fprintf(stderr, "Failed to start timer: %s\n", uv_strerror(r));
    return;
  }
  uv_run(&loop, UV_RUN_DEFAULT);

  // Delete temp file
  uv_fs_t fs_req{};
  uv_fs_unlink(&loop, &fs_req, filepath.c_str(), nullptr);
  uv_fs_req_cleanup(&fs_req);
}

size_t NearHeapLimit(void* data,
                     size_t current_heap_limit,
                     size_t initial_heap_limit) {
  auto isolate = v8::Isolate::GetCurrent();
  auto state = PerIsolateData::For(isolate)->GetHeapProfilerState();

  if (state->insideCallback) {
    // Reentrant call detected, try to increase heap limit a bit so that
    // previous callback can proceed
    const uint32_t default_heap_extension_size = 10 * 1024 * 1024;
    auto extension_size = state->heap_extension_size
                              ? state->heap_extension_size
                              : default_heap_extension_size;
    return current_heap_limit + extension_size;
  }
  state->insideCallback = true;
  defer {
    state->insideCallback = false;
  };

  ++state->current_heap_extension_count;
  fprintf(stderr,
          "NearHeapLimit(count=%d): current_heap_limit=%zu, "
          "initial_heap_limit=%zu\n",
          state->current_heap_extension_count,
          current_heap_limit,
          initial_heap_limit);

  auto n = isolate->NumberOfTrackedHeapObjectTypes();
  v8::HeapObjectStatistics stats;

  for (size_t i = 0; i < n; ++i) {
    if (isolate->GetHeapObjectStatisticsAtLastGC(&stats, i) &&
        stats.object_count() > 0) {
      fprintf(stderr,
              "HeapObjectStats: type=%s, subtype=%s, size=%zu, count=%zu\n",
              stats.object_type(),
              stats.object_sub_type(),
              stats.object_size(),
              stats.object_count());
    }
  }
  std::unique_ptr<v8::AllocationProfile> profile{
      isolate->GetHeapProfiler()->GetAllocationProfile()};
  state->profile = TranslateAllocationProfileToCpp(profile->GetRootNode());
  if (state->dumpProfileOnStderr) {
    dumpAllocationProfile(stderr, state->profile.get());
  }

  if (!state->export_command.empty()) {
    ExportProfile(*state);
  }

  if (!state->callback.IsEmpty()) {
    if (state->callbackMode & kInterruptCallback) {
      isolate->RequestInterrupt(InterruptCallback, nullptr);
    }
    if (state->callbackMode & kAsyncCallback) {
      uv_async_send(state->async);
    }
  } else {
    state->profile.reset();
  }

  if (!state->isMainThread) {
    // In worker thread, OOM is not fatal to the whole process and will only
    // terminate the worker.
    // This is done by a callback registered by node, that's why we remove our
    // callback and then call LowMemoryNotification() here to trigger another
    // garbage collection, which will eventually call the callback registered by
    // node.
    state->UninstallNearHeapLimitCallback();
    isolate->LowMemoryNotification();
    // use the same value as node plus 1
    constexpr size_t kExtraHeapAllowance = 16 * 1024 * 1024;
    return current_heap_limit + kExtraHeapAllowance + 1;
  }

  size_t new_heap_limit =
      current_heap_limit +
      ((state->current_heap_extension_count <= state->max_heap_extension_count)
           ? state->heap_extension_size
           : 0);
  if (state->current_heap_extension_count >= state->max_heap_extension_count) {
    // On Node 14, NearLimitCallback is sometimes called many times, without the
    // process aborting, even when returned limit is not increased. Disable
    // callback until next call to GetAllocationProfile()
    state->UninstallNearHeapLimitCallback();
  }
  return new_heap_limit;
}

NAN_METHOD(HeapProfiler::StartSamplingHeapProfiler) {
  auto isolate = info.GetIsolate();

  // Register cleanup hook if not already registered for this isolate
  {
    const std::lock_guard<std::mutex> lock(g_heap_profiler_mutex);
    if (g_heap_profiler_isolates.find(isolate) ==
        g_heap_profiler_isolates.end()) {
      node::AddEnvironmentCleanupHook(
          isolate, HeapProfilerCleanupHook, isolate);
      g_heap_profiler_isolates.insert(isolate);
    }
  }

  if (info.Length() == 2) {
    if (!info[0]->IsUint32()) {
      return Nan::ThrowTypeError("First argument type must be uint32.");
    }
    if (!info[1]->IsNumber()) {
      return Nan::ThrowTypeError("First argument type must be Integer.");
    }

    uint64_t sample_interval = info[0].As<v8::Integer>()->Value();
    int stack_depth = info[1].As<v8::Integer>()->Value();

    isolate->GetHeapProfiler()->StartSamplingHeapProfiler(sample_interval,
                                                          stack_depth);
  } else {
    isolate->GetHeapProfiler()->StartSamplingHeapProfiler();
  }
}

// Signature:
// stopSamplingHeapProfiler()
NAN_METHOD(HeapProfiler::StopSamplingHeapProfiler) {
  auto isolate = info.GetIsolate();
  isolate->GetHeapProfiler()->StopSamplingHeapProfiler();
  PerIsolateData::For(isolate)->GetHeapProfilerState().reset();

  // Remove cleanup hook since profiler is explicitly stopped
  {
    const std::lock_guard<std::mutex> lock(g_heap_profiler_mutex);
    if (g_heap_profiler_isolates.erase(isolate) == 1) {
      node::RemoveEnvironmentCleanupHook(
          isolate, HeapProfilerCleanupHook, isolate);
    }
  }
}

// mapAllocationProfile(callback): callback result
NAN_METHOD(HeapProfiler::MapAllocationProfile) {
  if (info.Length() < 1 || !info[0]->IsFunction()) {
    return Nan::ThrowTypeError("mapAllocationProfile requires a callback");
  }
  auto isolate = info.GetIsolate();
  auto callback = info[0].As<v8::Function>();

  std::unique_ptr<v8::AllocationProfile> profile(
      isolate->GetHeapProfiler()->GetAllocationProfile());

  if (!profile) {
    return Nan::ThrowError("Heap profiler is not enabled.");
  }

  auto state = PerIsolateData::For(isolate)->GetHeapProfilerState();
  if (state) {
    state->OnNewProfile();
  }

  auto root = AllocationProfileNodeView::New(profile->GetRootNode());
  v8::Local<v8::Value> argv[] = {root};
  auto result =
      Nan::Call(callback, isolate->GetCurrentContext()->Global(), 1, argv);
  if (!result.IsEmpty()) {
    info.GetReturnValue().Set(result.ToLocalChecked());
  }
}

NAN_METHOD(HeapProfiler::MonitorOutOfMemory) {
  if (info.Length() != 7) {
    return Nan::ThrowTypeError("MonitorOOMCondition must have 7 arguments.");
  }
  if (!info[0]->IsUint32()) {
    return Nan::ThrowTypeError("Heap limit extension size must be a uint32.");
  }
  if (!info[1]->IsUint32()) {
    return Nan::ThrowTypeError(
        "Max heap limit extension count must be a uint32.");
  }
  if (!info[2]->IsBoolean()) {
    return Nan::ThrowTypeError("DumpHeapProfileOnStdErr must be a boolean.");
  }
  if (!info[3]->IsArray()) {
    return Nan::ThrowTypeError("Export command must be a string array.");
  }
  if (!info[4]->IsNullOrUndefined() && !info[4]->IsFunction()) {
    return Nan::ThrowTypeError("Callback name must be a function.");
  }
  if (!info[5]->IsUint32()) {
    return Nan::ThrowTypeError("CallbackMode must be a uint32.");
  }
  if (!info[6]->IsBoolean()) {
    return Nan::ThrowTypeError("IsMainThread must be a boolean.");
  }

  auto isolate = v8::Isolate::GetCurrent();

  auto& state = PerIsolateData::For(isolate)->GetHeapProfilerState();
  state = std::make_shared<HeapProfilerState>(isolate);

  state->heap_extension_size = info[0].As<v8::Integer>()->Value();
  state->max_heap_extension_count = info[1].As<v8::Integer>()->Value();
  state->dumpProfileOnStderr = info[2].As<v8::Boolean>()->Value();
  state->callbackMode = info[5].As<v8::Integer>()->Value();
  state->isMainThread = info[6].As<v8::Boolean>()->Value();
  state->InstallNearHeapLimitCallback();
  if (!info[4]->IsNullOrUndefined() && state->callbackMode != kNoCallback) {
    state->callback.Reset(Nan::To<v8::Function>(info[4]).ToLocalChecked());
  }

  auto commands = info[3].As<v8::Array>();
  for (uint32_t i = 0; i < commands->Length(); ++i) {
    auto value = Nan::Get(commands, i).ToLocalChecked();
    if (value->IsString()) {
      Nan::Utf8String arg{value};
      state->export_command.emplace_back(*arg, arg.length());
    }
  }

  if (!state->callback.IsEmpty() && (state->callbackMode & kAsyncCallback)) {
    state->RegisterAsyncCallback();
  }
}

NAN_MODULE_INIT(HeapProfiler::Init) {
  v8::Local<v8::Object> heapProfiler = Nan::New<v8::Object>();
  Nan::SetMethod(
      heapProfiler, "startSamplingHeapProfiler", StartSamplingHeapProfiler);
  Nan::SetMethod(
      heapProfiler, "stopSamplingHeapProfiler", StopSamplingHeapProfiler);
  Nan::SetMethod(heapProfiler, "mapAllocationProfile", MapAllocationProfile);
  Nan::SetMethod(heapProfiler, "monitorOutOfMemory", MonitorOutOfMemory);
  Nan::Set(target,
           Nan::New<v8::String>("heapProfiler").ToLocalChecked(),
           heapProfiler);
}

void InterruptCallback(v8::Isolate* isolate, void* data) {
  v8::HandleScope scope(isolate);
  auto state = PerIsolateData::For(isolate)->GetHeapProfilerState();
  if (!state->profile) {
    return;
  }
  v8::Local<v8::Value> argv[1] = {
      dd::TranslateAllocationProfile(state->profile.get())};
  Nan::AsyncResource resource("NearHeapLimit");
  state->callback.Call(1, argv, &resource);
  // Release the retained native profile once the callback has been invoked.
  state->profile.reset();
}

void AsyncCallback(uv_async_t* handle) {
  InterruptCallback(v8::Isolate::GetCurrent(), nullptr);
}

}  // namespace dd
```

## File: `bindings/profilers/heap.hh`
```
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

#pragma once

#include <nan.h>

namespace dd {

class HeapProfiler {
 public:
  // Signature:
  // startSamplingHeapProfiler()
  static NAN_METHOD(StartSamplingHeapProfiler);

  // Signature:
  // stopSamplingHeapProfiler()
  static NAN_METHOD(StopSamplingHeapProfiler);

  // Signature:
  // mapAllocationProfile(callback): callback result
  static NAN_METHOD(MapAllocationProfile);

  static NAN_METHOD(MonitorOutOfMemory);

  static NAN_MODULE_INIT(Init);
};

}  // namespace dd
```

## File: `bindings/profilers/wall.cc`
```
/*
 * Copyright 2023 Datadog, Inc
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include <nan.h>
#include <node.h>
#include <v8-internal.h>
#include <v8-profiler.h>
#include <cinttypes>
#include <cstdint>
#include <limits>
#include <memory>
#include <mutex>
#include <type_traits>
#include <vector>

#include "map-get.hh"
#include "per-isolate-data.hh"
#include "translate-time-profile.hh"
#include "wall.hh"

#ifndef _WIN32
#define DD_WALL_USE_SIGPROF true

// Declare v8::base::TimeTicks::Now. It is exported from the node executable so
// our addon will be able to dynamically link to the symbol when loaded.
namespace v8 {
namespace base {
struct TimeTicks {
  static int64_t Now();
};
}  // namespace base
#if NODE_MAJOR_VERSION >= 22

// Available from 22.7.0
#define DD_WALL_USE_CPED true

namespace internal {
#if NODE_MAJOR_VERSION < 25
struct HandleScopeData {
  v8::internal::Address* next;
  v8::internal::Address* limit;
};
#endif  // NODE_MAJOR_VERSION < 25
#if NODE_MAJOR_VERSION >= 24
constexpr int kHandleBlockSize = v8::internal::KB - 2;
#endif  // NODE_MAJOR_VERSION >= 24
}  // namespace internal
#else  // NODE_MAJOR_VERSION >= 22
#define DD_WALL_USE_CPED false
#endif  //
}  // namespace v8

static int64_t Now() {
  return v8::base::TimeTicks::Now();
};

#else
#define DD_WALL_USE_SIGPROF false
#define DD_WALL_USE_CPED false

static int64_t Now() {
  return 0;
};

#endif

using namespace v8;

namespace dd {

class SignalGuard {
  std::atomic<bool>& guard_;

  inline void store(bool value) {
    std::atomic_signal_fence(std::memory_order_release);
    guard_.store(value, std::memory_order_relaxed);
  }

 public:
  inline SignalGuard(std::atomic<bool>& guard) : guard_(guard) { store(true); }

  inline ~SignalGuard() { store(false); }
};

void SetContextPtr(ContextPtr& contextPtr,
                   Isolate* isolate,
                   Local<Value> value) {
  if (!value->IsNullOrUndefined()) {
    contextPtr = std::make_shared<Global<Value>>(isolate, value);
  } else {
    contextPtr.reset();
  }
}

class PersistentContextPtr : public node::ObjectWrap {
  ContextPtr context;
  std::unordered_set<PersistentContextPtr*>* live;

 public:
  PersistentContextPtr(std::unordered_set<PersistentContextPtr*>* live,
                       Local<Object> wrap)
      : live(live) {
    Wrap(wrap);
  }

  void Detach() { live = nullptr; }

  ~PersistentContextPtr() {
    if (live) {
      live->erase(this);
    }
  }

  void Set(Isolate* isolate, const Local<Value>& value) {
    SetContextPtr(context, isolate, value);
  }

  ContextPtr Get() const { return context; }

  static PersistentContextPtr* Unwrap(Local<Object> wrap) {
    return node::ObjectWrap::Unwrap<PersistentContextPtr>(wrap);
  }
};

// Maximum number of rounds in the GetV8ToEpochOffset
static constexpr int MAX_EPOCH_OFFSET_ATTEMPTS = 20;

int getTotalHitCount(const v8::CpuProfileNode* node, bool* noHitLeaf) {
  int count = node->GetHitCount();
  auto child_count = node->GetChildrenCount();

  for (int i = 0; i < child_count; ++i) {
    count += getTotalHitCount(node->GetChild(i), noHitLeaf);
  }
  if (child_count == 0 && count == 0) {
    *noHitLeaf = true;
  }
  return count;
}

/** Returns 0 if no bug detected, 1 if possible bug (it could be a false
 * positive), 2 if bug detected for certain. */
int detectV8Bug(const v8::CpuProfile* profile) {
  /* When the profiler operates correctly, there'll be at least one node with
   * a non-zero hit count and the number of samples will be strictly greater
   * than the number of hits because they'll contain at least the starting
   * sample and potentially some deoptimization samples. If these conditions
   * don't hold, it implies that v8::SamplingEventsProcessor::ProcessOneSample
   * loop is stuck for ticks_buffer_ or vm_ticks_buffer_. */

  bool noHitLeaf = false;
  auto totalHitCount = getTotalHitCount(profile->GetTopDownRoot(), &noHitLeaf);
  if (totalHitCount == 0) {
    return 2;
  }

  if (profile->GetSamplesCount() == totalHitCount && !noHitLeaf) {
    /*  Checking number of samples against number of hits potentially leads to
     * false positive because some ticks samples can be discarded if their
     * timestamp is older than profile start time because of queueing.
     * Additionally check for leaf nodes with zero hit count, if there is one,
     * this implies that one non-tick sample was processed.
     */
    return 1;
  }
  return 0;
}

class ProtectedProfilerMap {
 public:
  WallProfiler* GetProfiler(const Isolate* isolate) const {
    // Prevent updates to profiler map by atomically setting g_profilers to null
    auto prof_map = profilers_.exchange(nullptr, std::memory_order_acq_rel);
    if (!prof_map) {
      return nullptr;
    }
    auto prof_it = prof_map->find(isolate);
    WallProfiler* profiler = nullptr;
    if (prof_it != prof_map->end()) {
      profiler = prof_it->second;
    }
    // Allow updates
    profilers_.store(prof_map, std::memory_order_release);
    return profiler;
  }

  WallProfiler* RemoveProfilerForIsolate(const v8::Isolate* isolate) {
    return UpdateProfilers([isolate](auto map) {
      auto it = map->find(isolate);
      if (it != map->end()) {
        auto profiler = it->second;
        map->erase(it);
        return profiler;
      }
      return static_cast<WallProfiler*>(nullptr);
    });
  }

  bool RemoveProfiler(const v8::Isolate* isolate, WallProfiler* profiler) {
    return UpdateProfilers([isolate, profiler, this](auto map) {
      terminatedWorkersCpu_ += profiler->GetAndResetThreadCpu();

      if (isolate != nullptr) {
        auto it = map->find(isolate);
        if (it != map->end() && it->second == profiler) {
          map->erase(it);
          return true;
        }
      } else {
        auto it = std::find_if(map->begin(), map->end(), [profiler](auto& x) {
          return x.second == profiler;
        });
        if (it != map->end()) {
          map->erase(it);
          return true;
        }
      }
      return false;
    });
  }

  bool AddProfiler(const v8::Isolate* isolate, WallProfiler* profiler) {
    return UpdateProfilers([isolate, profiler](auto map) {
      return map->emplace(isolate, profiler).second;
    });
  }

  ThreadCpuClock::duration GatherTotalWorkerCpuAndReset() {
    std::lock_guard<std::mutex> lock(update_mutex_);

    // Retrieve CPU of workers that have terminated during the last period
    ThreadCpuClock::duration totalWorkerCpu = terminatedWorkersCpu_;

    // Reset terminated workers cpu to 0
    terminatedWorkersCpu_ = ThreadCpuClock::duration::zero();

    if (!init_) {
      return totalWorkerCpu;
    }

    auto currProfilers = profilers_.load(std::memory_order_acquire);
    // Wait until sighandler is done using the map
    while (!currProfilers) {
      currProfilers = profilers_.load(std::memory_order_relaxed);
    }

    // Gather CPU of workers that are still running
    for (auto& profiler : *currProfilers) {
      totalWorkerCpu += profiler.second->GetAndResetThreadCpu();
    }

    return totalWorkerCpu;
  }

 private:
  using ProfilerMap = std::unordered_map<const Isolate*, WallProfiler*>;

  template <typename F>
  std::invoke_result_t<F, ProfilerMap*> UpdateProfilers(F updateFn) {
    // use mutex to prevent two isolates of updating profilers concurrently
    std::lock_guard<std::mutex> lock(update_mutex_);

    if (!init_) {
      profilers_.store(new ProfilerMap(), std::memory_order_release);
      init_ = true;
    }

    auto currProfilers = profilers_.load(std::memory_order_acquire);
    // Wait until sighandler is done using the map
    while (!currProfilers) {
      currProfilers = profilers_.load(std::memory_order_relaxed);
    }
    auto newProfilers = new ProfilerMap(*currProfilers);
    auto res = updateFn(newProfilers);
    // Wait until sighandler is done using the map before installing a new map.
    // The value in profilers is either nullptr or currProfilers.
    for (;;) {
      ProfilerMap* currProfilers2 = currProfilers;
      if (profilers_.compare_exchange_weak(
              currProfilers2, newProfilers, std::memory_order_acq_rel)) {
        break;
      }
    }
    delete currProfilers;
    return res;
  }

  mutable std::atomic<ProfilerMap*> profilers_;
  std::mutex update_mutex_;
  bool init_ = false;
  std::chrono::nanoseconds terminatedWorkersCpu_{};
};

using ProfilerMap = std::unordered_map<Isolate*, WallProfiler*>;

static ProtectedProfilerMap g_profilers;

namespace {

#if DD_WALL_USE_SIGPROF
class SignalHandler {
 public:
  static void IncreaseUseCount() {
    std::lock_guard<std::mutex> lock(mutex_);
    ++use_count_;
    // Always reinstall the signal handler
    Install();
  }

  static void DecreaseUseCount() {
    std::lock_guard<std::mutex> lock(mutex_);
    if (--use_count_ == 0) {
      Restore();
    }
  }

  static bool Installed() {
    std::lock_guard<std::mutex> lock(mutex_);
    return installed_;
  }

 private:
  static void Install() {
    struct sigaction sa;
    sa.sa_sigaction = &HandleProfilerSignal;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = SA_RESTART | SA_SIGINFO | SA_ONSTACK;
    if (installed_) {
      sigaction(SIGPROF, &sa, nullptr);
    } else {
      installed_ = (sigaction(SIGPROF, &sa, &old_handler_) == 0);
      old_handler_func_.store(old_handler_.sa_sigaction,
                              std::memory_order_relaxed);
    }
  }

  static void Restore() {
    if (installed_) {
      sigaction(SIGPROF, &old_handler_, nullptr);
      installed_ = false;
      old_handler_func_.store(nullptr, std::memory_order_relaxed);
    }
  }

  static void HandleProfilerSignal(int signal, siginfo_t* info, void* context);

  // Protects the process wide state below.
  static std::mutex mutex_;
  static int use_count_;
  static bool installed_;
  static struct sigaction old_handler_;
  using HandlerFunc = void (*)(int, siginfo_t*, void*);
  static std::atomic<HandlerFunc> old_handler_func_;
};

std::mutex SignalHandler::mutex_;
int SignalHandler::use_count_ = 0;
struct sigaction SignalHandler::old_handler_;
bool SignalHandler::installed_ = false;
std::atomic<SignalHandler::HandlerFunc> SignalHandler::old_handler_func_;

void SignalHandler::HandleProfilerSignal(int sig,
                                         siginfo_t* info,
                                         void* context) {
  auto old_handler = old_handler_func_.load(std::memory_order_relaxed);

  if (!old_handler) {
    return;
  }
  auto isolate = Isolate::GetCurrent();
  if (!isolate) {
    return;
  }
  WallProfiler* prof = g_profilers.GetProfiler(isolate);

  if (!prof) {
    // no profiler found for current isolate, just pass the signal to old
    // handler
    old_handler(sig, info, context);
    return;
  }

  auto mode = prof->collectionMode();
  if (mode == WallProfiler::CollectionMode::kNoCollect) {
    return;
  } else if (mode == WallProfiler::CollectionMode::kPassThrough) {
    old_handler(sig, info, context);
    return;
  }

  int64_t cpu_time = 0;
  if (prof->collectCpuTime()) {
    cpu_time = CurrentThreadCpuClock::now().time_since_epoch().count();
  }
  auto time_from = Now();
  old_handler(sig, info, context);
  auto time_to = Now();
  prof->PushContext(time_from, time_to, cpu_time, isolate);
}
#else
class SignalHandler {
 public:
  static void IncreaseUseCount() {}
  static void DecreaseUseCount() {}
};
#endif
}  // namespace

static_assert((-1L >> 1) == -1L, "Right shift is not arithmetic");

static int64_t midpoint(int64_t x, int64_t y) {
  // TODO: remove when we're on C++20 as it has a built-in midpoint
  return ((x ^ y) >> 1) + (x & y);
}

static int64_t GetV8ToEpochOffset() {
  using namespace std::chrono;
  // Make a best effort to capture the difference between UNIX epoch and the V8
  // profiling timer as precisely as possible. Will make at most 20 attempts to
  // capture the epoch time within the same V8 microsecond and use the one with
  // the smallest error. We repeat this every time we gather a profile (so,
  // every minute) instead of once statically, as the difference doesn't
  // necessarily remain constant depending on the characteristics of the clocks
  // being used.
  int64_t V8toEpochOffset = 0;
  int64_t smallestDiff = std::numeric_limits<int64_t>::max();
  for (int i = 0; i < MAX_EPOCH_OFFSET_ATTEMPTS; ++i) {
    auto v8Now = Now();
    auto epochNow =
        duration_cast<microseconds>(system_clock::now().time_since_epoch())
            .count();
    auto v8Now2 = Now();
    auto diff = v8Now2 - v8Now;
    if (diff < smallestDiff) {
      V8toEpochOffset = epochNow - midpoint(v8Now, v8Now2);
      if (diff == 0) {
        break;
      }
      smallestDiff = diff;
    }
  }
  return V8toEpochOffset;
}

void WallProfiler::CleanupHook(void* data) {
  auto isolate = static_cast<Isolate*>(data);
  auto prof = g_profilers.RemoveProfilerForIsolate(isolate);
  if (prof) {
    prof->Cleanup(isolate);
    delete prof;
  }
}

// This is only called when isolate is terminated without `beforeExit`
// notification.
void WallProfiler::Cleanup(Isolate* isolate) {
  if (started_) {
    cpuProfiler_->Stop(profileId_);
    if (interceptSignal()) {
      SignalHandler::DecreaseUseCount();
    }
    Dispose(isolate, false);
  }
}

ContextsByNode WallProfiler::GetContextsByNode(CpuProfile* profile,
                                               ContextBuffer& contexts,
                                               int64_t startCpuTime) {
  ContextsByNode contextsByNode;

  auto sampleCount = profile->GetSamplesCount();
  if (contexts.empty() || sampleCount == 0) {
    return contextsByNode;
  }

  auto isolate = Isolate::GetCurrent();
  auto v8Context = isolate->GetCurrentContext();
  auto contextIt = contexts.begin();

  // deltaIdx is the offset of the sample to process compared to current
  // iteration index
  int deltaIdx = 0;

  auto contextKey = String::NewFromUtf8Literal(isolate, "context");
  auto timestampKey = String::NewFromUtf8Literal(isolate, "timestamp");
  auto cpuTimeKey = String::NewFromUtf8Literal(isolate, "cpuTime");
  auto asyncIdKey = String::NewFromUtf8Literal(isolate, "asyncId");
  auto V8toEpochOffset = GetV8ToEpochOffset();
  auto lastCpuTime = startCpuTime;

  // skip first sample because it's the one taken on profiler start, outside of
  // signal handler
  for (int i = 1; i < sampleCount; i++) {
    // Handle out-of-order samples, hypothesis is that at most 2 consecutive
    // samples can be out-of-order
    if (deltaIdx == 1) {
      // previous iteration was processing next sample, so this one should
      // process previous sample
      deltaIdx = -1;
    } else if (deltaIdx == -1) {
      // previous iteration was processing previous sample, returns to normal
      // index
      deltaIdx = 0;
    } else if (i < sampleCount - 1 && profile->GetSampleTimestamp(i + 1) <
                                          profile->GetSampleTimestamp(i)) {
      // detected  out-of-order sample, process next sample
      deltaIdx = 1;
    }

    auto sampleIdx = i + deltaIdx;
    auto sample = profile->GetSample(sampleIdx);

    auto sampleTimestamp = profile->GetSampleTimestamp(sampleIdx);

    // This loop will drop all contexts that are too old to be associated with
    // the current sample; association is done by matching each sample with
    // context whose [time_from,time_to] interval encompasses sample timestamp.
    while (contextIt != contexts.end()) {
      auto& sampleContext = *contextIt;
      if (sampleContext.time_to < sampleTimestamp) {
        // Current sample context is too old, discard it and fetch the next one.
        ++contextIt;
      } else if (sampleContext.time_from > sampleTimestamp) {
        // Current sample context is too recent, we'll try to match it to the
        // next sample.
        break;
      } else {
        // This sample context is the closest to this sample.
        auto it = contextsByNode.find(sample);
        Local<Array> array;
        if (it == contextsByNode.end()) {
          array = Array::New(isolate);
          contextsByNode[sample] = {array, 1};
        } else {
          array = it->second.contexts;
          ++it->second.hitcount;
        }
        // Conforms to TimeProfileNodeContext defined in v8-types.ts
        Local<Object> timedContext = Object::New(isolate);
        timedContext
            ->Set(v8Context,
                  timestampKey,
                  BigInt::New(isolate, sampleTimestamp + V8toEpochOffset))
            .Check();
        auto* function_name = sample->GetFunctionNameStr();
        // If current sample is program, reports its cpu time to the next sample
        if (strcmp(function_name, "(program)") != 0) {
          if (collectCpuTime_) {
            timedContext
                ->Set(
                    v8Context,
                    cpuTimeKey,
                    Number::New(isolate, sampleContext.cpu_time - lastCpuTime))
                .Check();
            lastCpuTime = sampleContext.cpu_time;
          }
          // If current sample is neither program nor idle, associate a sampling
          // context and async ID
          if (strcmp(function_name, "(idle)") != 0) {
            if (sampleContext.context) {
              timedContext
                  ->Set(v8Context,
                        contextKey,
                        sampleContext.context.get()->Get(isolate))
                  .Check();
            }
            if (collectAsyncId_) {
              timedContext
                  ->Set(v8Context,
                        asyncIdKey,
                        Number::New(isolate, sampleContext.async_id))
                  .Check();
            }
          }
        }
        array->Set(v8Context, array->Length(), timedContext).Check();

        // Sample context was consumed, fetch the next one
        ++contextIt;
        break;  // don't match more than one context to one sample
      }
    }
  }

  return contextsByNode;
}

void GCPrologueCallback(Isolate* isolate,
                        GCType type,
                        GCCallbackFlags flags,
                        void* data) {
  static_cast<WallProfiler*>(data)->OnGCStart(isolate);
}

void GCEpilogueCallback(Isolate* isolate,
                        GCType type,
                        GCCallbackFlags flags,
                        void* data) {
  static_cast<WallProfiler*>(data)->OnGCEnd();
}

WallProfiler::WallProfiler(std::chrono::microseconds samplingPeriod,
                           std::chrono::microseconds duration,
                           bool includeLines,
                           bool withContexts,
                           bool workaroundV8Bug,
                           bool collectCpuTime,
                           bool collectAsyncId,
                           bool isMainThread,
                           Local<Value> cpedKey)
    : samplingPeriod_(samplingPeriod),
      includeLines_(includeLines),
      withContexts_(withContexts),
      isMainThread_(isMainThread) {
  // Try to workaround V8 bug where profiler event processor loop becomes stuck.
  // When starting a new profile, wait for one signal before and one signal
  // after to reduce the likelihood that race condition occurs and one code
  // event just after triggers the issue.
  workaroundV8Bug_ = workaroundV8Bug && DD_WALL_USE_SIGPROF && detectV8Bug_;
  collectCpuTime_ = collectCpuTime && withContexts;
  collectAsyncId_ = collectAsyncId && withContexts;
#if DD_WALL_USE_CPED
  bool useCPED = withContexts && cpedKey->IsObject();
#else
  constexpr bool useCPED = false;
#endif

  if (withContexts_) {
    contexts_.reserve(duration * 2 / samplingPeriod);
  }

  collectionMode_.store(CollectionMode::kNoCollect, std::memory_order_relaxed);
  gcCount.store(0, std::memory_order_relaxed);

  // TODO: bind to this isolate? Would fix the Dispose(nullptr) issue.
  auto isolate = v8::Isolate::GetCurrent();
  v8::Local<v8::ArrayBuffer> buffer =
      v8::ArrayBuffer::New(isolate, sizeof(uint32_t) * kFieldCount);

  v8::Local<v8::Uint32Array> jsArray =
      v8::Uint32Array::New(buffer, 0, kFieldCount);
  fields_ = static_cast<uint32_t*>(buffer->GetBackingStore()->Data());
  jsArray_ = v8::Global<v8::Uint32Array>(isolate, jsArray);
  std::fill(fields_, fields_ + kFieldCount, 0);

  if (useCPED) {
    // Used to create Map value objects that will have one internal field to
    // store the sample context pointer.
    auto wrapObjectTemplate = ObjectTemplate::New(isolate);
    wrapObjectTemplate->SetInternalFieldCount(1);
    wrapObjectTemplate_.Reset(isolate, wrapObjectTemplate);
    auto cpedKeyObj = cpedKey.As<Object>();
    cpedKey_.Reset(isolate, cpedKeyObj);
    cpedKeyHash_ = cpedKeyObj->GetIdentityHash();
  }
}

WallProfiler::~WallProfiler() {
  // Delete all live contexts
  for (auto ptr : liveContextPtrs_) {
    ptr->Detach();  // so it doesn't invalidate our iterator
    delete ptr;
  }
  liveContextPtrs_.clear();
}

void WallProfiler::Dispose(Isolate* isolate, bool removeFromMap) {
  if (cpuProfiler_ != nullptr) {
    cpuProfiler_->Dispose();
    cpuProfiler_ = nullptr;

    if (removeFromMap) {
      g_profilers.RemoveProfiler(isolate, this);
    }

    if (collectAsyncId_ || useCPED()) {
      isolate->RemoveGCPrologueCallback(&GCPrologueCallback, this);
      isolate->RemoveGCEpilogueCallback(&GCEpilogueCallback, this);
    }

    node::RemoveEnvironmentCleanupHook(
        isolate, &WallProfiler::CleanupHook, isolate);
  }
}

#define DD_WALL_PROFILER_GET_BOOLEAN_CONFIG(name)                              \
  auto name##Value = getArg(#name);                                            \
  if (name##Value.IsEmpty() || !name##Value.ToLocalChecked()->IsBoolean()) {   \
    return Nan::ThrowTypeError(#name " must be a boolean.");                   \
  }                                                                            \
  bool name = name##Value.ToLocalChecked().As<v8::Boolean>()->Value();

NAN_METHOD(WallProfiler::New) {
  if (info.Length() != 1 || !info[0]->IsObject()) {
    return Nan::ThrowTypeError("WallProfiler must have one object argument.");
  }

  if (info.IsConstructCall()) {
    auto arg = info[0].As<v8::Object>();
    auto isolate = info.GetIsolate();
    auto context = isolate->GetCurrentContext();
    auto getArg = [&](const char* name) {
      return arg->Get(context,
                      String::NewFromUtf8(isolate, name).ToLocalChecked());
    };

    auto intervalMicrosValue = getArg("intervalMicros");
    if (intervalMicrosValue.IsEmpty() ||
        !intervalMicrosValue.ToLocalChecked()->IsNumber()) {
      return Nan::ThrowTypeError("intervalMicros must be a number.");
    }

    std::chrono::microseconds interval{
        intervalMicrosValue.ToLocalChecked().As<v8::Integer>()->Value()};

    if (interval <= std::chrono::microseconds::zero()) {
      return Nan::ThrowTypeError("Sample rate must be positive.");
    }

    auto durationMillisValue = getArg("durationMillis");
    if (durationMillisValue.IsEmpty() ||
        !durationMillisValue.ToLocalChecked()->IsNumber()) {
      return Nan::ThrowTypeError("durationMillis must be a number.");
    }

    std::chrono::milliseconds duration{
        durationMillisValue.ToLocalChecked().As<v8::Integer>()->Value()};

    if (duration <= std::chrono::microseconds::zero()) {
      return Nan::ThrowTypeError("Duration must be positive.");
    }
    if (duration < interval) {
      return Nan::ThrowTypeError("Duration must not be less than sample rate.");
    }

    DD_WALL_PROFILER_GET_BOOLEAN_CONFIG(lineNumbers);
    DD_WALL_PROFILER_GET_BOOLEAN_CONFIG(withContexts);
    DD_WALL_PROFILER_GET_BOOLEAN_CONFIG(workaroundV8Bug);
    DD_WALL_PROFILER_GET_BOOLEAN_CONFIG(collectCpuTime);
    DD_WALL_PROFILER_GET_BOOLEAN_CONFIG(collectAsyncId);
    DD_WALL_PROFILER_GET_BOOLEAN_CONFIG(isMainThread);
    DD_WALL_PROFILER_GET_BOOLEAN_CONFIG(useCPED);

    auto cpedKey = getArg("CPEDKey").ToLocalChecked();
    if (cpedKey->IsObject() && !useCPED) {
      return Nan::ThrowTypeError("useCPED is false but CPEDKey is specified");
    }
    if (useCPED && cpedKey->IsUndefined()) {
      cpedKey = Object::New(isolate);
    }
#if !DD_WALL_USE_CPED
    if (useCPED) {
      return Nan::ThrowTypeError(
#ifndef _WIN32
          "useCPED is not supported on this Node.js version."
#else
          "useCPED is not supported on Windows."
#endif
      );
    }
#endif

    if (withContexts && !DD_WALL_USE_SIGPROF) {
      return Nan::ThrowTypeError("Contexts are not supported.");
    }

    if (collectCpuTime && !withContexts) {
      return Nan::ThrowTypeError("Cpu time collection requires contexts.");
    }

    if (collectAsyncId && !withContexts) {
      return Nan::ThrowTypeError("Async ID collection requires contexts.");
    }

    if (lineNumbers && withContexts) {
      // Currently custom contexts are not compatible with caller line
      // information, because it's not possible to associate context with line
      // ticks:
      // context is associated to sample which itself is associated with
      // a CpuProfileNode, but if node has several line ticks, then we cannot
      // determine context <-> line ticks association. Note that line number is
      // present in v8 internal sample struct and would allow mapping sample to
      // line tick, and thus context to line tick, but this information is not
      // available in v8 public API.
      // Moreover in caller line number mode, line number of a CpuProfileNode
      // is not the line of the current function, but the line number where this
      // function is called, therefore we don't have access either to the line
      // of the function (otherwise we could ignore line ticks and replace them
      // with single hit count for the function).
      return Nan::ThrowTypeError(
          "Include line option is not compatible with contexts.");
    }

    WallProfiler* obj = new WallProfiler(interval,
                                         duration,
                                         lineNumbers,
                                         withContexts,
                                         workaroundV8Bug,
                                         collectCpuTime,
                                         collectAsyncId,
                                         isMainThread,
                                         cpedKey);
    obj->Wrap(info.This());
    info.GetReturnValue().Set(info.This());
  } else {
    v8::Local<v8::Value> arg = info[0];
    v8::Local<v8::Function> cons = Nan::New(
        PerIsolateData::For(info.GetIsolate())->WallProfilerConstructor());
    info.GetReturnValue().Set(Nan::NewInstance(cons, 1, &arg).ToLocalChecked());
  }
}

#undef DD_WALL_PROFILER_GET_BOOLEAN_CONFIG

NAN_METHOD(WallProfiler::Start) {
  WallProfiler* wallProfiler =
      Nan::ObjectWrap::Unwrap<WallProfiler>(info.This());

  if (info.Length() != 0) {
    return Nan::ThrowTypeError("Start must not have any arguments.");
  }

  auto res = wallProfiler->StartImpl();
  if (!res.success) {
    return Nan::ThrowTypeError(res.msg.c_str());
  }
}

Result WallProfiler::StartImpl() {
  if (started_) {
    return Result{"Start called on already started profiler, stop it first."};
  }

  profileIdx_ = 0;

  if (!CreateV8CpuProfiler()) {
    return Result{"Cannot start profiler: another profiler is already active."};
  }

  // Register GC callbacks for async ID and CPED context tracking before
  // starting profiling
  auto isolate = Isolate::GetCurrent();
  if (collectAsyncId_ || useCPED()) {
    isolate->AddGCPrologueCallback(&GCPrologueCallback, this);
    isolate->AddGCEpilogueCallback(&GCEpilogueCallback, this);
  }

  profileId_ = StartInternal();

  auto collectionMode = withContexts_
                            ? CollectionMode::kCollectContexts
                            : (workaroundV8Bug_ ? CollectionMode::kPassThrough
                                                : CollectionMode::kNoCollect);
  collectionMode_.store(collectionMode, std::memory_order_relaxed);
  started_ = true;
  node::AddEnvironmentCleanupHook(isolate, &WallProfiler::CleanupHook, isolate);
  return {};
}

v8::ProfilerId WallProfiler::StartInternal() {
  // Reuse the same names for the profiles because strings used for profile
  // names are not released until v8::CpuProfiler object is destroyed.
  // https://github.com/nodejs/node/blob/b53c51995380b1f8d642297d848cab6010d2909c/deps/v8/src/profiler/profile-generator.h#L516
  char buf[128];
  snprintf(buf, sizeof(buf), "pprof-%" PRId64, (profileIdx_++) % 2);
  v8::Local<v8::String> title = Nan::New<String>(buf).ToLocalChecked();
  auto result = cpuProfiler_->Start(
      title,
      includeLines_ ? CpuProfilingMode::kCallerLineNumbers
                    : CpuProfilingMode::kLeafNodeLineNumbers,
      // Always record samples in order to be able to check if non tick samples
      // (ie. starting or deopt samples) have been processed, and therefore if
      // SamplingEventsProcessor::ProcessOneSample is stuck on vm_ticks_buffer_.
      withContexts_ || detectV8Bug_);

  // reinstall sighandler on each new upload period
  if (withContexts_ || workaroundV8Bug_) {
    SignalHandler::IncreaseUseCount();
    fields_[kSampleCount] = 0;
  }

  if (collectCpuTime_) {
    startThreadCpuTime_ =
        CurrentThreadCpuClock::now().time_since_epoch().count();
    startProcessCpuTime_ = ProcessCpuClock::now();
  }

  // Force collection of two other non-tick samples (ie. that will not add to
  // hit count).
  // This is to be able to detect when v8 profiler event processor loop is
  // stuck on ticks_from_vm_buffer_.
  // A non-tick sample is already taken upon profiling start, and should be
  // enough to determine if a non-tick sample has been processed at the end by
  // comparing number of samples with total hit count.
  // The first tick sample might be discarded though if its timestamp is older
  // than profile start time due to queueing and in that case it is still added
  // to hit count but not to the sample array, leading to incorrectly detect
  // that ticks_from_vm_buffer_ is stuck.
  // This is not needed when workaroundV8Bug_ is enabled because in that case,
  // we wait for one signal before starting a new profile which should leave
  // time to process in-flight tick samples.
  if (detectV8Bug_ && !workaroundV8Bug_) {
    cpuProfiler_->CollectSample(v8::Isolate::GetCurrent());
    cpuProfiler_->CollectSample(v8::Isolate::GetCurrent());
  }

  return result.id;
}

// stopAndCollect(restart, callback): callback result
NAN_METHOD(WallProfiler::StopAndCollect) {
  if (info.Length() != 2) {
    return Nan::ThrowTypeError("stopAndCollect must have two arguments.");
  }
  if (!info[0]->IsBoolean()) {
    return Nan::ThrowTypeError("Restart must be a boolean.");
  }
  if (!info[1]->IsFunction()) {
    return Nan::ThrowTypeError("stopAndCollect requires a callback.");
  }

  bool restart = info[0].As<Boolean>()->Value();
  auto callback = info[1].As<Function>();

  WallProfiler* wallProfiler =
      Nan::ObjectWrap::Unwrap<WallProfiler>(info.This());

  v8::Local<v8::Value> result;
  auto err = wallProfiler->StopAndCollectImpl(restart, callback, result);
  if (!err.success) {
    return Nan::ThrowTypeError(err.msg.c_str());
  }
  if (!result.IsEmpty()) {
    info.GetReturnValue().Set(result);
  }
}

bool WallProfiler::waitForSignal(uint64_t targetCallCount) {
  auto currentCallCount = noCollectCallCount_.load(std::memory_order_relaxed);
  std::atomic_signal_fence(std::memory_order_acquire);
  if (targetCallCount != 0) {
    // check if target call count already reached
    if (currentCallCount >= targetCallCount) {
      return true;
    }
  } else {
    // no target call count in input, wait for the next signal
    targetCallCount = currentCallCount + 1;
  }
#if DD_WALL_USE_SIGPROF
  const int maxRetries = 2;
  // wait for a maximum of 2 sample periods
  // if a signal occurs it will interrupt sleep (we use nanosleep and not
  // uv_sleep because we want this behaviour)
  timespec ts = {
      0, std::chrono::nanoseconds(samplingPeriod_ * maxRetries).count()};
  nanosleep(&ts, nullptr);
#endif
  auto res = noCollectCallCount_.load(std::memory_order_relaxed);
  std::atomic_signal_fence(std::memory_order_acquire);
  return res >= targetCallCount;
}

template <typename ProfileBuilder>
Result WallProfiler::StopCore(bool restart, ProfileBuilder&& buildProfile) {
  if (!started_) {
    return Result{"Stop called on not started profiler."};
  }

  uint64_t callCount = 0;
  auto oldProfileId = profileId_;
  if (restart && workaroundV8Bug_) {
    std::atomic_signal_fence(std::memory_order_release);
    collectionMode_.store(CollectionMode::kNoCollect,
                          std::memory_order_relaxed);
    waitForSignal();
  } else if (withContexts_) {
    std::atomic_signal_fence(std::memory_order_release);
    collectionMode_.store(CollectionMode::kNoCollect,
                          std::memory_order_relaxed);

    // make sure timestamp changes to avoid having samples from previous profile
    auto now = Now();
    while (Now() == now) {
    }
  }

  auto startThreadCpuTime = startThreadCpuTime_;
  auto startProcessCpuTime = startProcessCpuTime_;

  if (restart) {
    profileId_ = StartInternal();
    // record call count to wait for next signal at the end of function
    callCount = noCollectCallCount_.load(std::memory_order_relaxed);
    std::atomic_signal_fence(std::memory_order_acquire);
  }

  if (interceptSignal()) {
    SignalHandler::DecreaseUseCount();
  }

  auto v8_profile = cpuProfiler_->Stop(oldProfileId);

  ContextBuffer contexts;
  if (withContexts_) {
    contexts.reserve(contexts_.capacity());
    std::swap(contexts, contexts_);
  }

  if (detectV8Bug_) {
    v8ProfilerStuckEventLoopDetected_ = detectV8Bug(v8_profile);
  }

  if (restart && withContexts_ && !workaroundV8Bug_) {
    // make sure timestamp changes to avoid mixing sample taken upon start and a
    // sample from signal handler
    // If v8 bug workaround is enabled, reactivation of sample collection is
    // delayed until function end.
    auto now = Now();
    while (Now() == now) {
    }
    std::atomic_signal_fence(std::memory_order_release);
    collectionMode_.store(CollectionMode::kCollectContexts,
                          std::memory_order_relaxed);
  }

  ContextsByNode contextsByNode;
  ContextsByNode* contextsByNodePtr = nullptr;
  int64_t nonJSThreadsCpuTime = 0;
  bool hasCpuTime = false;

  if (withContexts_) {
    if (isMainThread_ && collectCpuTime_) {
      // account for non-JS threads CPU only in main thread
      // CPU time of non-JS threads is the difference between process CPU time
      // and sum of all worker JS thread during the profiling period of main
      // worker thread.
      auto totalWorkerCpu = g_profilers.GatherTotalWorkerCpuAndReset();
      auto processCpu = ProcessCpuClock::now() - startProcessCpuTime;
      nonJSThreadsCpuTime =
          std::max(processCpu - totalWorkerCpu, ProcessCpuClock::duration{})
              .count();
    }
    contextsByNode =
        GetContextsByNode(v8_profile, contexts, startThreadCpuTime);
    contextsByNodePtr = &contextsByNode;
    hasCpuTime = collectCpuTime_;
  }

  buildProfile(v8_profile, hasCpuTime, nonJSThreadsCpuTime, contextsByNodePtr);

  v8_profile->Delete();

  if (!restart) {
    Dispose(v8::Isolate::GetCurrent(), true);
  } else if (workaroundV8Bug_) {
    waitForSignal(callCount + 1);
    std::atomic_signal_fence(std::memory_order_release);
    collectionMode_.store(withContexts_ ? CollectionMode::kCollectContexts
                                        : CollectionMode::kPassThrough,
                          std::memory_order_relaxed);
  }

  started_ = restart;
  return {};
}

Result WallProfiler::StopAndCollectImpl(bool restart,
                                        v8::Local<v8::Function> callback,
                                        v8::Local<v8::Value>& result) {
  return StopCore(
      restart,
      [&](const v8::CpuProfile* v8_profile,
          bool hasCpuTime,
          int64_t nonJSThreadsCpuTime,
          ContextsByNode* contextsByNodePtr) {
        auto* isolate = Isolate::GetCurrent();
        TimeProfileViewState state{includeLines_, contextsByNodePtr, {}};
        auto profile_view = BuildTimeProfileView(
            v8_profile, hasCpuTime, nonJSThreadsCpuTime, state);
        v8::Local<v8::Value> argv[] = {profile_view};
        auto cb_result = Nan::Call(
            callback, isolate->GetCurrentContext()->Global(), 1, argv);
        if (!cb_result.IsEmpty()) {
          result = cb_result.ToLocalChecked();
        }
      });
}

NAN_MODULE_INIT(WallProfiler::Init) {
  Local<FunctionTemplate> tpl = Nan::New<FunctionTemplate>(New);
  Local<String> className = Nan::New("TimeProfiler").ToLocalChecked();
  tpl->SetClassName(className);
  tpl->InstanceTemplate()->SetInternalFieldCount(1);

  Nan::SetAccessor(tpl->InstanceTemplate(),
                   Nan::New("context").ToLocalChecked(),
                   GetContext,
                   SetContext);

  Nan::SetPrototypeMethod(tpl, "start", Start);
  Nan::SetPrototypeMethod(tpl, "stopAndCollect", StopAndCollect);
  Nan::SetPrototypeMethod(tpl, "dispose", Dispose);
  Nan::SetPrototypeMethod(tpl,
                          "v8ProfilerStuckEventLoopDetected",
                          V8ProfilerStuckEventLoopDetected);
  Nan::SetPrototypeMethod(tpl, "createContextHolder", CreateContextHolder);

  Nan::SetAccessor(tpl->InstanceTemplate(),
                   Nan::New("state").ToLocalChecked(),
                   SharedArrayGetter);

  Nan::SetAccessor(tpl->InstanceTemplate(),
                   Nan::New("metrics").ToLocalChecked(),
                   GetMetrics);

  PerIsolateData::For(Isolate::GetCurrent())
      ->WallProfilerConstructor()
      .Reset(Nan::GetFunction(tpl).ToLocalChecked());
  Nan::Set(target, className, Nan::GetFunction(tpl).ToLocalChecked());

  auto isolate = v8::Isolate::GetCurrent();
  v8::PropertyAttribute ReadOnlyDontDelete =
      static_cast<v8::PropertyAttribute>(ReadOnly | DontDelete);

  v8::Local<Object> constants = v8::Object::New(isolate);
  Nan::DefineOwnProperty(constants,
                         Nan::New("kSampleCount").ToLocalChecked(),
                         Nan::New<Integer>(kSampleCount),
                         ReadOnlyDontDelete)
      .FromJust();
  Nan::DefineOwnProperty(target,
                         Nan::New("constants").ToLocalChecked(),
                         constants,
                         ReadOnlyDontDelete)
      .FromJust();
}

v8::CpuProfiler* WallProfiler::CreateV8CpuProfiler() {
  if (cpuProfiler_ == nullptr) {
    v8::Isolate* isolate = v8::Isolate::GetCurrent();

    bool inserted = g_profilers.AddProfiler(isolate, this);

    if (!inserted) {
      // refuse to create a new profiler if one is already active
      return nullptr;
    }
    cpuProfiler_ = v8::CpuProfiler::New(isolate);
    cpuProfiler_->SetSamplingInterval(
        std::chrono::microseconds(samplingPeriod_).count());
  }
  return cpuProfiler_;
}

Local<Value> WallProfiler::GetContext(Isolate* isolate) {
  auto context = GetContextPtr(isolate);
  if (context) {
    return context->Get(isolate);
  }
  return Undefined(isolate);
}

void WallProfiler::SetCurrentContextPtr(Isolate* isolate, Local<Value> value) {
  SignalGuard m(setInProgress_);
  SetContextPtr(curContext_, isolate, value);
}

void WallProfiler::SetContext(Isolate* isolate, Local<Value> value) {
#if DD_WALL_USE_CPED
  if (!useCPED()) {
    SetCurrentContextPtr(isolate, value);
    return;
  }

  auto cped = isolate->GetContinuationPreservedEmbedderData();
  // No Node AsyncContextFrame in this continuation yet
  if (!cped->IsMap()) return;

  auto v8Ctx = isolate->GetCurrentContext();
  // This should always be called from a V8 context, but check just in case.
  if (v8Ctx.IsEmpty()) return;

  auto cpedMap = cped.As<Map>();
  auto localKey = cpedKey_.Get(isolate);

  // Always replace the PersistentContextPtr in the map even if it is present,
  // we want the PersistentContextPtr in a parent map to not be mutated.
  if (value->IsUndefined()) {
    // The absence of a sample context will be interpreted as undefined in
    // GetContextPtr so if value is undefined, just delete the key.
    SignalGuard m(setInProgress_);
    cpedMap->Delete(v8Ctx, localKey).Check();
  } else {
    auto contextHolder = CreateContextHolder(isolate, v8Ctx, value);
    SignalGuard m(setInProgress_);
    cpedMap->Set(v8Ctx, localKey, contextHolder).ToLocalChecked();
  }
#else
  SetCurrentContextPtr(isolate, value);
#endif
}

Local<Object> WallProfiler::CreateContextHolder(Isolate* isolate,
                                                Local<Context> v8Ctx,
                                                Local<Value> value) {
  auto wrap =
      wrapObjectTemplate_.Get(isolate)->NewInstance(v8Ctx).ToLocalChecked();
  // for easy access from JS when cpedKey is an ALS, it can do
  // als.getStore()?.[0];
  wrap->Set(v8Ctx, 0, value).Check();
  auto contextPtr = new PersistentContextPtr(&liveContextPtrs_, wrap);
  liveContextPtrs_.insert(contextPtr);
  contextPtr->Set(isolate, value);
  return wrap;
}

ContextPtr WallProfiler::GetContextPtrSignalSafe(Isolate* isolate) {
  auto isSetInProgress = setInProgress_.load(std::memory_order_relaxed);
  std::atomic_signal_fence(std::memory_order_acquire);
  if (isSetInProgress) {
    // New sample context is being set. Safe behavior is to not try attempt
    // Object::Get on it and just return empty right now.
    return ContextPtr();
  }

  if (useCPED()) {
    auto curGcCount = gcCount.load(std::memory_order_relaxed);
    std::atomic_signal_fence(std::memory_order_acquire);
    if (curGcCount > 0) {
      return gcContext_;
    }
  }

  return GetContextPtr(isolate);
}

ContextPtr WallProfiler::GetContextPtr(Isolate* isolate) {
#if DD_WALL_USE_CPED
  if (!useCPED()) {
    return curContext_;
  }

  if (!isolate->IsInUse()) {
    return ContextPtr();
  }

  auto cpedAddrPtr = reinterpret_cast<internal::Address*>(
      reinterpret_cast<uint64_t>(isolate) +
      internal::Internals::kContinuationPreservedEmbedderDataOffset);
  auto cpedAddr = *cpedAddrPtr;
  if (internal::Internals::HasHeapObjectTag(cpedAddr)) {
    auto cpedValuePtr = reinterpret_cast<Value*>(cpedAddrPtr);
    if (cpedValuePtr->IsMap()) {
      Address keyAddr = **(reinterpret_cast<Address**>(&cpedKey_));

      Address wrapAddr = GetValueFromMap(cpedAddr, cpedKeyHash_, keyAddr);
      if (internal::Internals::HasHeapObjectTag(wrapAddr)) {
        auto wrapValue = reinterpret_cast<Value*>(&wrapAddr);
        if (wrapValue->IsObject()) {
          auto wrapObj = reinterpret_cast<Object*>(wrapValue);
          if (wrapObj->InternalFieldCount() > 0) {
            return static_cast<PersistentContextPtr*>(
                       wrapObj->GetAlignedPointerFromInternalField(0))
                ->Get();
          }
        }
      }
    }
  }
  return ContextPtr();
#else
  return curContext_;
#endif
}

Local<Object> WallProfiler::GetMetrics(Isolate* isolate) {
  auto usedAsyncContextCount = liveContextPtrs_.size();
  auto context = isolate->GetCurrentContext();
  auto metrics = Object::New(isolate);
  metrics
      ->Set(context,
            String::NewFromUtf8Literal(isolate, "usedAsyncContextCount"),
            Number::New(isolate, usedAsyncContextCount))
      .ToChecked();
  metrics
      ->Set(context,
            String::NewFromUtf8Literal(isolate, "totalAsyncContextCount"),
            Number::New(isolate, usedAsyncContextCount))
      .ToChecked();
  return metrics;
}

NAN_GETTER(WallProfiler::GetContext) {
  auto profiler = Nan::ObjectWrap::Unwrap<WallProfiler>(info.This());
  info.GetReturnValue().Set(profiler->GetContext(info.GetIsolate()));
}

NAN_SETTER(WallProfiler::SetContext) {
  auto profiler = Nan::ObjectWrap::Unwrap<WallProfiler>(info.This());
  profiler->SetContext(info.GetIsolate(), value);
}

NAN_METHOD(WallProfiler::CreateContextHolder) {
  auto profiler = Nan::ObjectWrap::Unwrap<WallProfiler>(info.This());
  if (!profiler->useCPED()) {
    return Nan::ThrowTypeError(
        "CreateContextHolder can only be used with CPED");
  }
  auto isolate = info.GetIsolate();
  auto contextHolder = profiler->CreateContextHolder(
      isolate, isolate->GetCurrentContext(), info[0]);
  info.GetReturnValue().Set(contextHolder);
}

NAN_GETTER(WallProfiler::SharedArrayGetter) {
  auto profiler = Nan::ObjectWrap::Unwrap<WallProfiler>(info.This());
  info.GetReturnValue().Set(profiler->jsArray_.Get(v8::Isolate::GetCurrent()));
}

NAN_GETTER(WallProfiler::GetMetrics) {
  auto profiler = Nan::ObjectWrap::Unwrap<WallProfiler>(info.This());
  info.GetReturnValue().Set(profiler->GetMetrics(info.GetIsolate()));
}

NAN_METHOD(WallProfiler::V8ProfilerStuckEventLoopDetected) {
  auto profiler = Nan::ObjectWrap::Unwrap<WallProfiler>(info.This());
  info.GetReturnValue().Set(profiler->v8ProfilerStuckEventLoopDetected());
}

NAN_METHOD(WallProfiler::Dispose) {
  auto profiler = Nan::ObjectWrap::Unwrap<WallProfiler>(info.This());
  // Profiler must already be stopped when this is called.
  if (profiler->started_) {
    return Nan::ThrowTypeError("Profiler is still running, stop it first.");
  }
  delete profiler;
}

#if NODE_MAJOR_VERSION >= 24 && DD_WALL_USE_SIGPROF
// Returns the number of free Address slots for Locals that can be returned by
// the isolate without triggering memory allocation.
int GetFreeLocalSlotCount(Isolate* isolate) {
  v8::internal::HandleScopeData* data =
      reinterpret_cast<v8::internal::HandleScopeData*>(
          reinterpret_cast<uint64_t>(isolate) +
          v8::internal::Internals::kIsolateHandleScopeDataOffset);
  auto diff = data->limit - data->next;
  // sanity check: diff can be at most kHandleBlockSize. If it is larger,
  // something is suspicious. See
  // https://github.com/v8/v8/blob/6fcfeccda2d8bcb7397f89bf5bbacd0c2eb2fb7f/src/handles/handles.cc#L195
  return diff > v8::internal::kHandleBlockSize ? 0 : diff;
}
#endif

double GetAsyncIdNoGC(v8::Isolate* isolate) {
  if (!isolate->IsInUse()) {
    // Must not try to create a handle scope if isolate is not in use.
    return -1;
  }
#if NODE_MAJOR_VERSION >= 24 && DD_WALL_USE_SIGPROF
  if (GetFreeLocalSlotCount(isolate) < 1) {
    // Must not try to create a handle scope if we can't create one local handle
    // (return value of GetEnteredOrMicrotaskContext) without allocation.
    return -1;
  }
  HandleScope scope(isolate);
  auto context = isolate->GetEnteredOrMicrotaskContext();
  return context.IsEmpty() ? -1 : node::AsyncHooksGetExecutionAsyncId(context);
#else
  return node::AsyncHooksGetExecutionAsyncId(isolate);
#endif
}

double WallProfiler::GetAsyncId(v8::Isolate* isolate) {
  if (!collectAsyncId_) {
    return -1;
  }
  auto curGcCount = gcCount.load(std::memory_order_relaxed);
  std::atomic_signal_fence(std::memory_order_acquire);
  if (curGcCount > 0) {
    return gcAsyncId;
  }
  return GetAsyncIdNoGC(isolate);
}

void WallProfiler::OnGCStart(v8::Isolate* isolate) {
  auto curCount = gcCount.load(std::memory_order_relaxed);
  std::atomic_signal_fence(std::memory_order_acquire);
  if (curCount == 0) {
    if (collectAsyncId_) {
      gcAsyncId = GetAsyncIdNoGC(isolate);
    }
    if (useCPED()) {
      gcContext_ = GetContextPtrSignalSafe(isolate);
    }
  }
  std::atomic_signal_fence(std::memory_order_release);
  gcCount.store(curCount + 1, std::memory_order_relaxed);
}

void WallProfiler::OnGCEnd() {
  auto oldCount = gcCount.fetch_sub(1, std::memory_order_relaxed);
  if (oldCount != 1 || !useCPED()) {
    return;
  }
  // Not strictly necessary, as we'll reset it to something else on next GC,
  // but why retain it longer than needed?
  gcContext_.reset();
}

void WallProfiler::PushContext(int64_t time_from,
                               int64_t time_to,
                               int64_t cpu_time,
                               Isolate* isolate) {
  // Be careful this is called in a signal handler context therefore all
  // operations must be async signal safe (in particular no allocations).
  // Our ring buffer avoids allocations.
  if (contexts_.size() < contexts_.capacity()) {
    contexts_.push_back({GetContextPtrSignalSafe(isolate),
                         time_from,
                         time_to,
                         cpu_time,
                         GetAsyncId(isolate)});
    std::atomic_fetch_add_explicit(
        reinterpret_cast<std::atomic<uint32_t>*>(&fields_[kSampleCount]),
        1U,
        std::memory_order_relaxed);
  }
}

}  // namespace dd
```

## File: `bindings/profilers/wall.hh`
```
/*
 * Copyright 2023 Datadog, Inc
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#pragma once

#include "contexts.hh"
#include "thread-cpu-clock.hh"

#include <nan.h>
#include <v8-profiler.h>
#include <atomic>
#include <memory>
#include <unordered_map>
#include <utility>

namespace dd {

struct Result {
  Result() = default;
  explicit Result(const char* msg) : success{false}, msg{msg} {};

  bool success = true;
  std::string msg;
};

using ContextPtr = std::shared_ptr<v8::Global<v8::Value>>;

class PersistentContextPtr;

class WallProfiler : public Nan::ObjectWrap {
 public:
  enum class CollectionMode { kNoCollect, kPassThrough, kCollectContexts };
  enum Fields { kSampleCount, kFieldCount };

 private:
  std::chrono::microseconds samplingPeriod_{0};
  v8::CpuProfiler* cpuProfiler_ = nullptr;

  // If we aren't using the CPED, we use a single context ptr stored here.
  ContextPtr curContext_;
  // Otherwise we'll use an object as a key to store the context in
  // AsyncContextFrame maps.
  v8::Global<v8::Object> cpedKey_;
  int cpedKeyHash_ = 0;
  v8::Global<v8::ObjectTemplate> wrapObjectTemplate_;

  // We track live context pointers in a set to avoid memory leaks. They will
  // be deleted when the profiler is disposed.
  std::unordered_set<PersistentContextPtr*> liveContextPtrs_;

  std::atomic<int> gcCount = 0;
  std::atomic<bool> setInProgress_ = false;
  double gcAsyncId;
  ContextPtr gcContext_;

  std::atomic<CollectionMode> collectionMode_;
  std::atomic<uint64_t> noCollectCallCount_;
  v8::ProfilerId profileId_;
  uint64_t profileIdx_ = 0;
  bool includeLines_ = false;
  bool withContexts_ = false;
  bool started_ = false;
  bool workaroundV8Bug_;
  static inline constexpr bool detectV8Bug_ = true;
  bool collectCpuTime_;
  bool collectAsyncId_;
  bool isMainThread_;
  int v8ProfilerStuckEventLoopDetected_ = 0;
  ProcessCpuClock::time_point startProcessCpuTime_{};
  int64_t startThreadCpuTime_ = 0;
  /* threadCpuStopWatch_ is used to measure CPU consumed by JS thread owning the
   * WallProfiler object during profiling period of main worker thread. */
  ThreadCpuStopWatch threadCpuStopWatch_;
  uint32_t* fields_;
  v8::Global<v8::Uint32Array> jsArray_;

  struct SampleContext {
    ContextPtr context;
    int64_t time_from;
    int64_t time_to;
    int64_t cpu_time;
    double async_id;
  };

  using ContextBuffer = std::vector<SampleContext>;
  ContextBuffer contexts_;

  ~WallProfiler();
  void Dispose(v8::Isolate* isolate, bool removeFromMap);

  // A new CPU profiler object will be created each time profiling is started
  // to work around https://bugs.chromium.org/p/v8/issues/detail?id=11051.
  v8::CpuProfiler* CreateV8CpuProfiler();

  ContextsByNode GetContextsByNode(v8::CpuProfile* profile,
                                   ContextBuffer& contexts,
                                   int64_t startCpuTime);

  bool waitForSignal(uint64_t targetCallCount = 0);
  static void CleanupHook(void* data);
  void Cleanup(v8::Isolate* isolate);

  ContextPtr GetContextPtr(v8::Isolate* isolate);
  ContextPtr GetContextPtrSignalSafe(v8::Isolate* isolate);

  void SetCurrentContextPtr(v8::Isolate* isolate, v8::Local<v8::Value> context);

  inline bool useCPED() { return !cpedKey_.IsEmpty(); }

 public:
  /**
   * @param samplingPeriodMicros sampling interval, in microseconds
   * @param durationMicros the duration of sampling, in microseconds. This
   * parameter is informative; it is up to the caller to call the Stop method
   * every period. The parameter is used to preallocate data structures that
   * should not be reallocated in async signal safe code.
   * @param cpedKey if an object, then the profiler should use the
   * AsyncLocalFrame stored in the V8 ContinuationPreservedEmbedderData to store
   * the current sampling context.
   */
  explicit WallProfiler(std::chrono::microseconds samplingPeriod,
                        std::chrono::microseconds duration,
                        bool includeLines,
                        bool withContexts,
                        bool workaroundV8bug,
                        bool collectCpuTime,
                        bool collectAsyncId,
                        bool isMainThread,
                        v8::Local<v8::Value> cpedKey);

  v8::Local<v8::Value> GetContext(v8::Isolate*);
  void SetContext(v8::Isolate*, v8::Local<v8::Value>);
  v8::Local<v8::Object> CreateContextHolder(v8::Isolate*,
                                            v8::Local<v8::Context>,
                                            v8::Local<v8::Value>);

  void PushContext(int64_t time_from,
                   int64_t time_to,
                   int64_t cpu_time,
                   v8::Isolate* isolate);
  v8::Local<v8::Object> GetMetrics(v8::Isolate*);

  Result StartImpl();
  v8::ProfilerId StartInternal();
  template <typename ProfileBuilder>
  Result StopCore(bool restart, ProfileBuilder&& buildProfile);
  Result StopAndCollectImpl(bool restart,
                            v8::Local<v8::Function> callback,
                            v8::Local<v8::Value>& result);

  CollectionMode collectionMode() {
    auto res = collectionMode_.load(std::memory_order_relaxed);
    if (res == CollectionMode::kNoCollect) {
      noCollectCallCount_.fetch_add(1, std::memory_order_relaxed);
    }
    std::atomic_signal_fence(std::memory_order_acquire);
    return res;
  }

  bool collectCpuTime() const { return collectCpuTime_; }

  bool interceptSignal() const { return withContexts_ || workaroundV8Bug_; }

  int v8ProfilerStuckEventLoopDetected() const {
    return v8ProfilerStuckEventLoopDetected_;
  }

  ThreadCpuClock::duration GetAndResetThreadCpu() {
    return threadCpuStopWatch_.GetAndReset();
  }

  double GetAsyncId(v8::Isolate* isolate);
  void OnGCStart(v8::Isolate* isolate);
  void OnGCEnd();

  static NAN_METHOD(New);
  static NAN_METHOD(Start);
  static NAN_METHOD(StopAndCollect);
  static NAN_METHOD(V8ProfilerStuckEventLoopDetected);
  static NAN_METHOD(Dispose);
  static NAN_MODULE_INIT(Init);
  static NAN_GETTER(GetContext);
  static NAN_SETTER(SetContext);
  static NAN_METHOD(CreateContextHolder);
  static NAN_GETTER(SharedArrayGetter);
  static NAN_GETTER(GetMetrics);
};

}  // namespace dd
```

## File: `bindings/test/binding.cc`
```
/*
 * Copyright 2023 Datadog, Inc
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include <cstdlib>
#include <sstream>
#include <unordered_map>

#include "nan.h"
#include "node.h"
#include "tap.h"
#include "v8.h"

#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wcast-function-type"
#endif
NODE_MODULE_INIT(/* exports, module, context */) {
#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC diagnostic pop
#endif

  Tap t;
  const char* env_var = std::getenv("TEST");
  std::string name(env_var == nullptr ? "" : env_var);

  std::unordered_map<std::string, std::function<void(Tap&)>> tests = {};

  if (name.empty()) {
    t.plan(tests.size());
    for (auto test : tests) {
      t.test(test.first, test.second);
    }
  } else {
    t.plan(1);
    if (tests.count(name)) {
      t.test(name, tests[name]);
    } else {
      std::ostringstream s;
      s << "Unknown test: " << name;
      t.fail(s.str());
    }
  }

  // End test and set `process.exitCode`
  int exitCode = t.end();
  auto processKey = Nan::New<v8::String>("process").ToLocalChecked();
  auto process = Nan::Get(context->Global(), processKey).ToLocalChecked();
  Nan::Set(process.As<v8::Object>(),
           Nan::New<v8::String>("exitCode").ToLocalChecked(),
           Nan::New<v8::Number>(exitCode));
}
```

## File: `bindings/test/tap.h`
```c
/*
 * Copyright 2023 Datadog, Inc
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef _INCLUDE_TAP_H_
#define _INCLUDE_TAP_H_

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * @brief This is the TAP document every function will interact with
 */
typedef struct tap_s {
  FILE* out;               /**< FILE where TAP document will be written */
  int plan_count;          /**< Number of expected checks */
  int count;               /**< Number of checks made so far */
  int failures;            /**< Number of failures so far */
  int skip_count;          /**< Number of future checks to skip */
  int skipped;             /**< Number of checks skipped so far */
  int indent;              /**< Indentation level for sub-tests */
  const char* skip_reason; /**< Reason to report for future skipped checks */
  void* data;              /**< Free pointer slot to pass data into sub-tests */
} tap_t;

/**
 * @brief Sub-test function signature
 *
 * @param t TAP document
 */
typedef void (*tap_test_fn)(tap_t* t);

/**
 * @private
 * @brief Print indentation level for sub-tests
 * @note Internal use only!
 *
 * @param t TAP document
 */
static inline void _tap_print_indent(tap_t* t) {
  for (int i = 0; i < t->indent; i++) {
    fprintf(t->out, " ");
  }
}

/**
 * @private
 * @brief This is separated to prevent sub-tests from re-printing TAP version.
 * @note Internal use only!
 *
 * @param t TAP document
 */
static inline tap_t _tap_init(FILE* out, int indent) {
  return {
      out,  // out
      0,    // plan_count
      0,    // count
      0,    // failures
      0,    // skip_count
      0,    // skipped
      indent,
      NULL,  // skip_reason
      NULL   // data
  };
}

/**
 * @brief Creates a TAP document writing to the given FILE.
 *
 * ```c
 * tap_t t = tap(stdout);
 * // or...
 * tap_t t = tap(fopen("out.tap", "w"));
 * ```
 *
 * ```tap
 * TAP version 13
 * ```
 *
 * @param out FILE to which the TAP document will be written
 * @return tap_t
 */
static inline tap_t tap(FILE* out) {
  fprintf(out, "TAP version 13\n");
  return _tap_init(out, 0);
}

/**
 * @brief Enable given pragma key
 *
 * ```c
 * tap_on(&t, "strict");
 * ```
 *
 * ```tap
 * pragma +strict
 * ```
 *
 * @param t TAP document
 * @param pragma Key to enable
 */
static inline void tap_on(tap_t* t, const char* pragma) {
  _tap_print_indent(t);
  fprintf(t->out, "pragma +%s\n", pragma);
}

/**
 * @brief Disable given pragma key
 *
 * ```c
 * tap_off(&t, "strict");
 * ```
 *
 * ```tap
 * pragma -strict
 * ```
 *
 * @param t TAP document
 * @param pragma Key to disable
 */
static inline void tap_off(tap_t* t, const char* pragma) {
  _tap_print_indent(t);
  fprintf(t->out, "pragma -%s\n", pragma);
}

/**
 * @brief Bail out of the test
 *
 * ```c
 * tap_bail_out(&t, "Oh no!");
 * ```
 *
 * ```tap
 * Bail out! Oh No!
 * ```
 *
 * @param t TAP document
 * @param reason Reason to record to TAP document for bailing out
 */
static inline void tap_bail_out(tap_t* t, const char* reason) {
  fprintf(t->out, "Bail out! %s\n", reason);
  exit(1);
}

/**
 * @brief Inform the TAP document to expect a set number of test completions
 * when ended.
 *
 * Setting the plan multiple times is invalid. If not specified it will
 * be set automatically from the total test count when the test is ended.
 *
 * ```c
 * tap_plan(&t, 123);
 * ```
 *
 * ```tap
 * 1..123
 * ```
 *
 * @param t TAP document
 * @param n number of expected checks
 */
static inline void tap_plan(tap_t* t, int n) {
  if (t->plan_count != 0) {
    tap_bail_out(t, "setting the plan multiple times is invalid");
    return;
  }
  t->plan_count = n;
  _tap_print_indent(t);
  fprintf(t->out, "1..%d\n", n);
}

/**
 * @brief Add a comment line to the tap document. Useful for separating groups
 * of tests too small to warrant splitting out to a fully separate test block.
 *
 * ```c
 * tap_comment(&t, "my section");
 * ```
 *
 * ```tap
 * # my section
 * ```
 *
 * @param t TAP document
 * @param comment Comment to write to the TAP document
 */
static inline void tap_comment(tap_t* t, const char* comment) {
  _tap_print_indent(t);
  fprintf(t->out, "# %s\n", comment);
}

/**
 * @brief Skips the next n tests.
 *
 * ```c
 * tap_skip_n(&t, 1, "unimplemented");
 * tap_pass(&t, "not done yet");
 * // or...
 * tap_skip_n(&t, 2);
 * tap_pass(&t, "just skipping");
 * tap_pass(&t, "also skipping");
 * ```
 *
 * ```tap
 * ok 1 - not done yet # SKIP unimplemented
 * ok 2 - just skipping # SKIP
 * ok 3 - also skipping # SKIP
 * ```
 *
 * @param t TAP document
 * @param n Number of checks to skip
 * @param reason Optional reason for skipping
 */
static inline void tap_skip_n(tap_t* t, int n, const char* reason) {
  if (t->skip_count > 0) {
    tap_bail_out(t, "only one skip task may be active");
    return;
  }
  t->skip_count = n;
  t->skip_reason = reason;
}

/**
 * @brief Skips the next test.
 *
 * ```c
 * tap_skip(&t, "unimplemented");
 * tap_pass(&t, "not done yet");
 * // or...
 * tap_skip(&t);
 * tap_pass(&t, "just skipping");
 * ```
 *
 * ```tap
 * ok 1 - not done yet # SKIP unimplemented
 * ok 2 - just skipping # SKIP
 * ```
 *
 * @param t TAP document
 * @param reason Optional reason for skipping
 */
static inline void tap_skip(tap_t* t, const char* reason, ...) {
  tap_skip_n(t, 1, reason);
}

/**
 * @internal
 * Hack to make reason optional
 */
#define tap_skip(t, ...) tap_skip(t, ##__VA_ARGS__, NULL)

/**
 * @brief Check if a given value is truthy.
 *
 * All other check types are sugar around this one.
 *
 * ```c
 * tap_ok(&t, true, "it's true");
 * // or...
 * tap_ok(&t, false);
 * ```
 *
 * ```tap
 * ok 1 - it's true
 * not ok 2
 * ```
 *
 * @param t TAP document
 * @param pass Mark if the checked value is truthy
 * @param description Optional description of what was checked
 */
static inline void tap_ok(tap_t* t, bool pass, const char* description, ...) {
  const char* skip_reason = t->skip_reason;
  int skip_count = t->skip_count;

  if (t->skip_count) {
    t->skip_count--;
    t->skipped++;
    if (!t->skip_count) {
      t->skip_reason = NULL;
    }
  } else {
    t->count++;
    if (!pass) {
      t->failures++;
    }
  }
  // Status information
  _tap_print_indent(t);
  if (!pass) fprintf(t->out, "not ");
  fprintf(t->out, "ok %d", t->count);
  // Optional message
  if (description != NULL && strlen(description)) {
    fprintf(t->out, " - %s", description);
  }
  // Directive
  if (skip_reason != NULL && strlen(skip_reason)) {
    fprintf(t->out, " # SKIP %s", skip_reason);
  } else if (skip_count > 0) {
    fprintf(t->out, " # SKIP");
  }
  fprintf(t->out, "\n");
}

/**
 * @internal
 * Hack to make descriptions optional
 */
#define tap_ok(t, value, ...) tap_ok(t, value, ##__VA_ARGS__, "")

/**
 * @brief Check if the value is falsy.
 *
 * ```c
 * tap_not_ok(&t, true, "it is falsy");
 * // or...
 * tap_not_ok(&t, false);
 * ```
 *
 * ```tap
 * not ok 1 - it is falsy
 * ok 2
 * ```
 *
 * @param t TAP document
 * @param value Value to check if it is falsy
 * @param description Optional description of what was checked
 */
#define tap_not_ok(t, value, ...) tap_ok(t, !((bool)value), __VA_ARGS__)

/**
 * @brief Mark a passed check.
 *
 * ```c
 * tap_pass(&t, "it passed");
 * // or...
 * tap_pass(&t);
 * ```
 *
 * ```tap
 * ok 1 - it passed
 * ok 2
 * ```
 *
 * @param t TAP document
 * @param description Optional description of what was checked
 */
#define tap_pass(t, ...) tap_ok(t, true, __VA_ARGS__)

/**
 * @brief Mark a failed check.
 *
 * ```c
 * tap_fail(&t, "it failed");
 * // or...
 * tap_fail(&t);
 * ```
 *
 * ```tap
 * not ok 1 - it failed
 * not ok 2
 * ```
 *
 * @param t TAP document
 * @param description Optional description of what was checked
 */
#define tap_fail(t, ...) tap_ok(t, false, __VA_ARGS__)

/**
 * @brief Check if values are equal.
 *
 * ```c
 * tap_equal(&t, a, b, "values are equal");
 * // or...
 * tap_equal(&t, a, b);
 * ```
 *
 * ```tap
 * ok 1 - values are equal
 * ok 2
 * ```
 *
 * @param t TAP document
 * @param a First value to compare
 * @param b Second balue to compare
 * @param description Optional description of what was checked
 */
#define tap_equal(t, a, b, ...) tap_ok(t, a == b, __VA_ARGS__)

/**
 * @brief Check if values are not equal.
 *
 * ```c
 * tap_not_equal(&t, a, b, "values are not equal");
 * // or...
 * tap_not_equal(&t, a, b);
 * ```
 *
 * ```tap
 * ok 1 - values are equal
 * ok 2
 * ```
 *
 * @param t TAP document
 * @param a First value to compare
 * @param b Second balue to compare
 * @param description Optional description of what was checked
 */
#define tap_not_equal(t, a, b, ...) tap_ok(t, a != b, __VA_ARGS__)

/**
 * @brief End the test document. Will record the plan range if not already set.
 *
 * ```c
 * tap_t t = tap(stdout);
 * tap_pass(&t, "yay!");
 * tap_end(&t);
 * ```
 *
 * ```tap
 * TAP version 13
 * ok 1 - yay!
 * 1..1
 * ```
 *
 * @param t TAP document
 * @return int Return 1 if unskipped failures or count does not match plan
 */
static inline int tap_end(tap_t* t) {
  if (t->plan_count == 0) {
    tap_plan(t, t->count + t->skipped);
  }
  if (t->failures > 0) return 1;
  if ((t->count + t->skipped) != t->plan_count) return 1;
  return 0;
}

/**
 * @brief Add a named sub-test
 *
 * ```c
 * void sub_test(tap_t* t) {
 *   tap_pass(t, "it passed");
 * }
 *
 * tap_test(&t, "sub-test", sub_test);
 * ```
 *
 * ```tap
 * # Subtest: sub-test
 *     ok 1 - it passed
 *     1..1
 * ok 1 - sub-test
 * ```
 *
 * @param t TAP document
 * @param name Test name
 * @param fn Test function
 * @param ptr Optional pointer to attach to tap_t given to test function
 */
static inline void tap_test(
    tap_t* t, const char* name, tap_test_fn fn, void* ptr, ...) {
  _tap_print_indent(t);
  fprintf(t->out, "# Subtest: %s\n", name);
  tap_t t2 = _tap_init(t->out, t->indent + 4);
  t2.data = ptr;
  fn(&t2);
  tap_ok(t, tap_end(&t2) == 0, name);
}

/**
 * @internal
 * Hack to make ptr optional
 */
#define tap_test(t, name, fn, ...) tap_test(t, name, fn, ##__VA_ARGS__, NULL)

#if __cplusplus >= 201103L || (defined(_MSC_VER) && _MSC_VER >= 1900)

#include <functional>
#include <string>

/**
 * @brief This is a TAP document
 */
class Tap : private tap_t {
 public:
  /**
   * @brief Construct a new TAP document
   *
   * @param out FILE stream to write TAP document to. Defaults to stdout.
   */
  Tap(FILE* out = stdout) : tap_t(tap(out)) {}

  /**
   * @brief Enable given pragma key
   *
   * ```cpp
   * t.on(&t, "strict");
   * ```
   *
   * ```tap
   * pragma +strict
   * ```
   *
   * @param pragma Key to enable
   */
  void on(const std::string& pragma) { tap_on(this, pragma.c_str()); }

  /**
   * @brief Disable given pragma key
   *
   * ```cpp
   * t.off(&t, "strict");
   * ```
   *
   * ```tap
   * pragma -strict
   * ```
   *
   * @param pragma Key to disable
   */
  void off(const std::string& pragma) { tap_off(this, pragma.c_str()); }

  /**
   * @brief Bail out of the test
   *
   * ```cpp
   * t.bail_out("Oh no!");
   * ```
   *
   * ```tap
   * Bail out! Oh No!
   * ```
   *
   * @param reason Reason to record to TAP document for bailing out
   */
  void bail_out(const std::string& reason = "") {
    tap_bail_out(this, reason.c_str());
  }

  /**
   * @brief Expect a set number of test completions when ended.
   *
   * ```cpp
   * t.plan(123);
   * ```
   *
   * ```tap
   * 1..123
   * ```
   *
   * @param n number of expected checks
   */
  void plan(int n) { tap_plan(this, n); }

  /**
   * @brief Add a comment line to the tap document. Useful for separating
   * groups of tests too small to warrant splitting out to a fully separate
   * test block.
   *
   * ```cpp
   * t.comment("my section");
   * ```
   *
   * ```tap
   * # my section
   * ```
   *
   * @param comment Comment to write to the TAP document
   */
  void comment(const std::string& comment) {
    tap_comment(this, comment.c_str());
  }

  /**
   * @brief Skips the next n tests.
   *
   * ```cpp
   * t.skip(1, "unimplemented");
   * t.pass("not done yet");
   * // or...
   * t.skip(2);
   * t.pass("just skipping");
   * t.pass("also skipping");
   * ```
   *
   * ```tap
   * ok 1 - not done yet # SKIP unimplemented
   * ok 2 - just skipping # SKIP
   * ok 3 - also skipping # SKIP
   * ```
   *
   * @param n Number of checks to skip
   * @param reason Optional reason for skipping
   */
  void skip(int n, const std::string& reason = "") {
    tap_skip_n(this, n, reason.c_str());
  }

  /**
   * @brief Skips the next test.
   *
   * ```cpp
   * t.skip("unimplemented");
   * t.pass("not done yet");
   * // or...
   * t.skip();
   * t.pass("just skipping");
   * ```
   *
   * ```tap
   * ok 1 - not done yet # SKIP unimplemented
   * ok 2 - just skipping # SKIP
   * ```
   *
   * @param reason Optional reason for skipping
   */
  void skip(const std::string& reason = "") { skip(1, reason); }

  /**
   * @brief Check if a given value is truthy.
   *
   * All other check types are sugar around this one.
   *
   * ```cpp
   * t.ok(true, "it's true");
   * // or...
   * t.ok(false);
   * ```
   *
   * ```tap
   * ok 1 - it's true
   * not ok 2
   * ```
   *
   * @param pass Mark if the checked value is truthy
   * @param description Optional description of what was checked
   */
  template <typename T>
  void ok(T pass, const std::string& description = "") {
    tap_ok(this, pass, description.c_str());
  }

  /**
   * @brief Check if the value is falsy.
   *
   * ```cpp
   * t.not_ok(true, "it is falsy");
   * // or...
   * t.not_ok(false);
   * ```
   *
   * ```tap
   * not ok 1 - it is falsy
   * ok 2
   * ```
   *
   * @param value Value to check if it is falsy
   * @param description Optional description of what was checked
   */
  template <typename T>
  void not_ok(T value, const std::string& description = "") {
    ok(!value, description);
  }

  /**
   * @brief Mark a passed check.
   *
   * ```cpp
   * t.pass("it passed");
   * // or...
   * t.pass();
   * ```
   *
   * ```tap
   * ok 1 - it passed
   * ok 2
   * ```
   *
   * @param description Optional description of what was checked
   */
  void pass(const std::string& description = "") { ok(true, description); }

  /**
   * @brief Mark a failed check.
   *
   * ```cpp
   * t.fail("it failed");
   * // or...
   * t.fail();
   * ```
   *
   * ```tap
   * not ok 1 - it failed
   * not ok 2
   * ```
   *
   * @param description Optional description of what was checked
   */
  void fail(const std::string& description = "") { ok(false, description); }

  /**
   * @brief Check if values are equal.
   *
   * ```cpp
   * t.equal(a, b, "values are equal");
   * // or...
   * t.equal(a, b);
   * ```
   *
   * ```tap
   * ok 1 - values are equal
   * ok 2
   * ```
   *
   * @param a First value to compare
   * @param b Second balue to compare
   * @param description Optional description of what was checked
   */
  template <typename A, typename B>
  void equal(A a, B b, const std::string& description = "") {
    ok(a == b, description);
  }

  /**
   * @brief Check if values are not equal.
   *
   * ```cpp
   * t.not_equal(a, b, "values are not equal");
   * // or...
   * t.not_equal(a, b);
   * ```
   *
   * ```tap
   * ok 1 - values are equal
   * ok 2
   * ```
   *
   * @param a First value to compare
   * @param b Second balue to compare
   * @param description Optional description of what was checked
   */
  template <typename A, typename B>
  void not_equal(A a, B b, const std::string& description = "") {
    ok(a != b, description);
  }

  /**
   * @brief End the test document. Will record the plan range if not already
   * set.
   *
   * ```cpp
   * Tap t;
   * t.pass("yay!");
   * t.end();
   * ```
   *
   * ```tap
   * TAP version 13
   * ok 1 - yay!
   * 1..1
   * ```
   *
   * @return int Return 1 if unskipped failures or count does not match plan
   */
  int end() { return tap_end(this); }

  /**
   * @brief Add a named sub-test
   *
   * ```cpp
   * t.test("sub-test", [](Tap& t) {
   *   tap_pass(t, "it passed");
   * });
   * ```
   *
   * ```tap
   * # Subtest: sub-test
   *     ok 1 - it passed
   *     1..1
   * ok 1 - sub-test
   * ```
   *
   * @param name Test name
   * @param fn Test function
   */
  void test(const std::string& name, std::function<void(Tap&)> fn) {
    struct callback {
      std::function<void(Tap&)> fn;
    };
    callback wrap = {fn};
    tap_test(
        this,
        name.c_str(),
        [](tap_t* t) {
          callback* wrap = static_cast<callback*>(t->data);
          wrap->fn(*static_cast<Tap*>(t));
        },
        &wrap);
  }
};

#endif  // __cplusplus >= 201103L

#endif  // _INCLUDE_TAP_H_
```

## File: `doc/sample_context_in_cped.md`
```markdown
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

## File: `scripts/cctest.js`
```javascript
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

## File: `suppressions/lsan_suppr.txt`
```
leak:CRYPTO_zalloc
```

## File: `system-test/Dockerfile.linux`
```
FROM golang:1.16-stretch as builder
RUN apt-get update && apt-get install -y \
    git \
 && rm -rf /var/lib/apt/lists/*
WORKDIR /root/
RUN go get github.com/google/pprof

FROM debian:stretch

ARG NODE_VERSION
ARG NVM_NODEJS_ORG_MIRROR
ARG ADDITIONAL_PACKAGES
ARG VERIFY_TIME_LINE_NUMBERS

RUN apt-get update && apt-get install -y curl $ADDITIONAL_PACKAGES \
    && rm -rf /var/lib/apt/lists/*

ENV NVM_DIR /bin/.nvm
RUN mkdir -p $NVM_DIR


# Install nvm with node and npm
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash \
    && . $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION

ENV BASH_ENV /root/.bashrc

WORKDIR /root/
COPY --from=builder /go/bin/pprof /bin
```

## File: `system-test/Dockerfile.node10-alpine`
```
FROM golang:1.16-alpine as builder
RUN apk add --no-cache git
WORKDIR /root/
RUN go get github.com/google/pprof


FROM node:10-alpine

ARG ADDITIONAL_PACKAGES

RUN apk add --no-cache bash $ADDITIONAL_PACKAGES
WORKDIR /root/
COPY --from=builder /go/bin/pprof /bin
RUN chmod a+x /bin/pprof
```

## File: `system-test/Dockerfile.node12-alpine`
```
FROM golang:1.16-alpine as builder
RUN apk add --no-cache git
WORKDIR /root/
RUN go get github.com/google/pprof


FROM node:12-alpine

ARG ADDITIONAL_PACKAGES

RUN apk add --no-cache bash $ADDITIONAL_PACKAGES
WORKDIR /root/
COPY --from=builder /go/bin/pprof /bin
RUN chmod a+x /bin/pprof
```

## File: `system-test/Dockerfile.node14-alpine`
```
FROM golang:1.16-alpine as builder
RUN apk add --no-cache git
WORKDIR /root/
RUN go get github.com/google/pprof


FROM node:14-alpine

ARG ADDITIONAL_PACKAGES

RUN apk add --no-cache bash $ADDITIONAL_PACKAGES
WORKDIR /root/
COPY --from=builder /go/bin/pprof /bin
RUN chmod a+x /bin/pprof
```

## File: `system-test/Dockerfile.node15-alpine`
```
FROM golang:1.16-alpine as builder
RUN apk add --no-cache git
WORKDIR /root/
RUN go get github.com/google/pprof


FROM node:15-alpine

ARG ADDITIONAL_PACKAGES

RUN apk add --no-cache bash $ADDITIONAL_PACKAGES
WORKDIR /root/
COPY --from=builder /go/bin/pprof /bin
RUN chmod a+x /bin/pprof
```

## File: `system-test/Dockerfile.node16-alpine`
```
FROM golang:1.16-alpine as builder
RUN apk add --no-cache git
WORKDIR /root/
RUN go get github.com/google/pprof


FROM node:16-alpine

ARG ADDITIONAL_PACKAGES

RUN apk add --no-cache bash $ADDITIONAL_PACKAGES
WORKDIR /root/
COPY --from=builder /go/bin/pprof /bin
RUN chmod a+x /bin/pprof
```

## File: `system-test/system_test.sh`
```bash
#!/bin/bash

# Trap all errors.
trap "echo '** AT LEAST ONE OF TESTS FAILED **'" ERR

# Fail on any error, show commands run.
set -eox pipefail

. $(dirname $0)/../tools/retry.sh

cd $(dirname $0)

if [[ -z "$BINARY_HOST" ]]; then
  ADDITIONAL_PACKAGES="python3 g++ make"
fi

if [[ "$RUN_ONLY_V8_CANARY_TEST" == "true" ]]; then
  NVM_NODEJS_ORG_MIRROR="https://nodejs.org/download/v8-canary"
  NODE_VERSIONS=(node)
else
  NODE_VERSIONS=(10 12 14 15 16)
fi

for i in ${NODE_VERSIONS[@]}; do
  # Test Linux support for the given node version.
  retry docker build -f Dockerfile.linux --build-arg NODE_VERSION=$i \
      --build-arg ADDITIONAL_PACKAGES="$ADDITIONAL_PACKAGES" \
      --build-arg  NVM_NODEJS_ORG_MIRROR="$NVM_NODEJS_ORG_MIRROR" \
      -t node$i-linux .

  docker run  -v $PWD/..:/src -e BINARY_HOST="$BINARY_HOST" node$i-linux \
      /src/system-test/test.sh

  # Test support for accurate line numbers with node versions supporting this
  # feature.
  if [ "$i" != "10" ]; then
    docker run  -v $PWD/..:/src -e BINARY_HOST="$BINARY_HOST" \
        -e VERIFY_TIME_LINE_NUMBERS="true" node$i-linux \
        /src/system-test/test.sh
  fi

  # Skip running on alpine if NVM_NODEJS_ORG_MIRROR is specified.
  if [[ ! -z "$NVM_NODEJS_ORG_MIRROR" ]]; then
    continue
  fi

  # Test Alpine support for the given node version.
  retry docker build -f Dockerfile.node$i-alpine \
      --build-arg ADDITIONAL_PACKAGES="$ADDITIONAL_PACKAGES" -t node$i-alpine .

  docker run -v $PWD/..:/src -e BINARY_HOST="$BINARY_HOST" node$i-alpine \
      /src/system-test/test.sh
done

echo '** ALL TESTS PASSED **'
```

## File: `system-test/test.sh`
```bash
#!/bin/bash

trap "cd $(dirname $0)/.. && npm run clean" EXIT
trap "echo '** TEST FAILED **'" ERR

. $(dirname $0)/../tools/retry.sh

function timeout_after() {
  # timeout on Node 11 alpine image requires -t to specify time.
  if [[ -f /bin/busybox ]] &&  [[ $(node -v) =~ ^v11.* ]]; then
    timeout -t "${@}"
  else
    timeout "${@}"
  fi
}

npm_install() {
  timeout_after 60 npm install --quiet "${@}"
}

set -eox pipefail
cd $(dirname $0)/..

NODEDIR=$(dirname $(dirname $(which node)))

# TODO: Remove when a new version of nan (current version 2.12.1) is released.
# For v8-canary tests, we need to use the version of NAN on github, which
# contains unreleased fixes that allow the native component to be compiled
# with Node's V8 canary build.
[ -z $NVM_NODEJS_ORG_MIRROR ] \
    || retry npm_install https://github.com/nodejs/nan.git

retry npm_install --nodedir="$NODEDIR" \
    ${BINARY_HOST:+--pprof_binary_host_mirror=$BINARY_HOST} >/dev/null

npm run compile
npm pack --quiet
VERSION=$(node -e "console.log(require('./package.json').version);")
PROFILER="$PWD/pprof-$VERSION.tgz"

if [[ "$VERIFY_TIME_LINE_NUMBERS" == "true" ]]; then
  BENCHDIR="$PWD/system-test/busybench-js"
  BENCHPATH="src/busybench.js"
else
  BENCHDIR="$PWD/system-test/busybench"
  BENCHPATH="build/src/busybench.js"
fi

TESTDIR=$(mktemp -d)
cp -r "$BENCHDIR" "$TESTDIR/busybench"
cd "$TESTDIR/busybench"

retry npm_install typescript gts @types/node >/dev/null
retry npm_install --nodedir="$NODEDIR" \
    $([ -z "$BINARY_HOST" ] && echo "--build-from-source=pprof" \
        || echo "--pprof_binary_host_mirror=$BINARY_HOST")\
    "$PROFILER">/dev/null

if [[ "$VERIFY_TIME_LINE_NUMBERS" != "true" ]]; then
  npm run compile
fi

node -v
node --trace-warnings "$BENCHPATH" 10 $VERIFY_TIME_LINE_NUMBERS

if [[ "$VERIFY_TIME_LINE_NUMBERS" == "true" ]]; then
  pprof -lines -top -nodecount=2 time.pb.gz
  pprof -lines -top -nodecount=2 time.pb.gz | \
      grep "busyLoop.*src/busybench.js:3[3-5]"
  pprof -filefunctions -top -nodecount=2 heap.pb.gz
  pprof -filefunctions -top -nodecount=2 heap.pb.gz | \
      grep "busyLoop.*src/busybench.js"
else
  pprof -filefunctions -top -nodecount=2 time.pb.gz
  pprof -filefunctions -top -nodecount=2 time.pb.gz | \
      grep "busyLoop.*src/busybench.ts"
  pprof -filefunctions -top -nodecount=2 heap.pb.gz
  pprof -filefunctions -top -nodecount=2 heap.pb.gz | \
      grep "busyLoop.*src/busybench.ts"
fi


echo '** TEST PASSED **'
```

## File: `system-test/busybench/package.json`
```json
{
  "name": "busybench",
  "version": "1.0.0",
  "description": "",
  "main": "build/src/busybench.js",
  "types": "build/src/busybench.d.ts",
  "files": [
    "build/src"
  ],
  "license": "Apache-2.0",
  "keywords": [],
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "check": "gts check",
    "clean": "gts clean",
    "compile": "tsc -p .",
    "fix": "gts fix",
    "prepare": "npm run compile",
    "pretest": "npm run compile",
    "posttest": "npm run check"
  },
  "devDependencies": {},
  "dependencies": {},
  "engines": {
    "node": ">=12"
  }
}
```

## File: `system-test/busybench/tsconfig.json`
```json
{
  "extends": "./node_modules/gts/tsconfig-google.json",
  "compilerOptions": {
    "rootDir": ".",
    "outDir": "build",
    "lib": [ "es2015" ],
    "target": "es2015"
  },
  "include": [
    "src/*.ts",
    "src/**/*.ts",
    "test/*.ts",
    "test/**/*.ts"
  ]
}
```

## File: `system-test/busybench/src/busybench.ts`
```typescript
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

import {writeFile as writeFilePromise} from 'fs/promises';
// eslint-disable-next-line node/no-extraneous-import
import {encode, heap, SourceMapper, time} from 'pprof';

const startTime: number = Date.now();
const testArr: number[][] = [];

/**
 * Fills several arrays, then calls itself with setTimeout.
 * It continues to do this until durationSeconds after the startTime.
 */
function busyLoop(durationSeconds: number) {
  for (let i = 0; i < testArr.length; i++) {
    for (let j = 0; j < testArr[i].length; j++) {
      testArr[i][j] = Math.sqrt(j * testArr[i][j]);
    }
  }
  if (Date.now() - startTime < 1000 * durationSeconds) {
    setTimeout(() => busyLoop(durationSeconds), 5);
  }
}

function benchmark(durationSeconds: number) {
  // Allocate 16 MiB in 64 KiB chunks.
  for (let i = 0; i < 16 * 16; i++) {
    testArr[i] = new Array<number>(64 * 1024);
  }
  busyLoop(durationSeconds);
}

async function collectAndSaveTimeProfile(
  durationSeconds: number,
  sourceMapper: SourceMapper
): Promise<void> {
  const profile = await time.profile({
    durationMillis: 1000 * durationSeconds,
    sourceMapper,
  });
  const buf = await encode(profile);
  await writeFilePromise('time.pb.gz', buf);
}

async function collectAndSaveHeapProfile(
  sourceMapper: SourceMapper
): Promise<void> {
  const profile = await heap.profile(undefined, sourceMapper);
  const buf = await encode(profile);
  await writeFilePromise('heap.pb.gz', buf);
}

async function collectAndSaveProfiles(): Promise<void> {
  const sourceMapper = await SourceMapper.create([process.cwd()]);
  collectAndSaveTimeProfile(durationSeconds, sourceMapper);
  collectAndSaveHeapProfile(sourceMapper);
}

const durationSeconds = Number(process.argv.length > 2 ? process.argv[2] : 30);
heap.start(512 * 1024, 64);
benchmark(durationSeconds);

collectAndSaveProfiles();
```

## File: `system-test/busybench-js/package.json`
```json
{
  "name": "busybench",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "dependencies": {},
  "devDependencies": {},
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "engines": {
    "node": ">=12"
  }
}
```

## File: `system-test/busybench-js/src/busybench.js`
```javascript
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

const fs = require('fs');
// eslint-disable-next-line node/no-missing-require
const pprof = require('pprof');

const writeFilePromise = fs.promises.writeFile;

const startTime = Date.now();
const testArr = [];

/**
 * Fills several arrays, then calls itself with setTimeout.
 * It continues to do this until durationSeconds after the startTime.
 */
function busyLoop(durationSeconds) {
  for (let i = 0; i < testArr.length; i++) {
    for (let j = 0; j < testArr[i].length; j++) {
      testArr[i][j] = Math.sqrt(j * testArr[i][j]);
    }
  }
  if (Date.now() - startTime < 1000 * durationSeconds) {
    setTimeout(() => busyLoop(durationSeconds), 5);
  }
}

function benchmark(durationSeconds) {
  // Allocate 16 MiB in 64 KiB chunks.
  for (let i = 0; i < 16 * 16; i++) {
    testArr[i] = new Array(64 * 1024);
  }
  busyLoop(durationSeconds);
}

async function collectAndSaveTimeProfile(
  durationSeconds,
  sourceMapper,
  lineNumbers
) {
  const profile = await pprof.time.profile({
    durationMillis: 1000 * durationSeconds,
    lineNumbers: lineNumbers,
    sourceMapper: sourceMapper,
  });
  const buf = await pprof.encode(profile);
  await writeFilePromise('time.pb.gz', buf);
}

async function collectAndSaveHeapProfile(sourceMapper) {
  const profile = pprof.heap.profile(undefined, sourceMapper);
  const buf = await pprof.encode(profile);
  await writeFilePromise('heap.pb.gz', buf);
}

async function collectAndSaveProfiles(collectLineNumberTimeProfile) {
  const sourceMapper = await pprof.SourceMapper.create([process.cwd()]);
  collectAndSaveHeapProfile(sourceMapper);
  collectAndSaveTimeProfile(
    durationSeconds / 2,
    sourceMapper,
    collectLineNumberTimeProfile
  );
}

const durationSeconds = Number(process.argv.length > 2 ? process.argv[2] : 30);
const collectLineNumberTimeProfile = Boolean(
  process.argv.length > 3 ? process.argv[3] : false
);

pprof.heap.start(512 * 1024, 64);
benchmark(durationSeconds);

collectAndSaveProfiles(collectLineNumberTimeProfile);
```

## File: `tools/publish.sh`
```bash
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

## File: `tools/retry.sh`
```bash
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

## File: `tools/kokoro/release/common.cfg`
```
# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

before_action {
  fetch_keystore {
    keystore_resource {
      keystore_config_id: 72935
      keyname: "cloud-profiler-e2e-service-account-key"
    }
  }
}

env_vars {
  key: "BUILD_TYPE"
  value: "release"
}
```

## File: `tools/kokoro/release/linux.cfg`
```
# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Kokoro config for job in release workflow which builds non-alpine Linux
# binaries.

# Location of the build script in this repository.
build_file: "pprof-nodejs/tools/build/linux_build_and_test.sh"
```

## File: `tools/kokoro/release/publish.cfg`
```
# Copyright 2019 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Kokoro config for job in release workflow which publishes module to npm.

# Get npm token from Keystore
before_action {
  fetch_keystore {
    keystore_resource {
      keystore_config_id: 72935
      keyname: "pprof-npm-token"
    }
  }
}

build_file: "pprof-nodejs/tools/publish.sh"
```

## File: `tools/kokoro/system-test/continuous/linux-prebuild.cfg`
```
# Format: //devtools/kokoro/config/proto/build.proto

before_action {
  fetch_keystore {
    keystore_resource {
      keystore_config_id: 72935
      keyname: "cloud-profiler-e2e-service-account-key"
    }
  }
}

build_file: "pprof-nodejs/tools/build/linux_build_and_test.sh"
```

## File: `tools/kokoro/system-test/continuous/linux-v8-canary.cfg`
```
# Format: //devtools/kokoro/config/proto/build.proto

build_file: "pprof-nodejs/system-test/system_test.sh"

env_vars {
  key: "RUN_ONLY_V8_CANARY_TEST"
  value: "true"
}
```

## File: `tools/kokoro/system-test/continuous/linux.cfg`
```
# Format: //devtools/kokoro/config/proto/build.proto

build_file: "pprof-nodejs/system-test/system_test.sh"
```

## File: `tools/kokoro/system-test/presubmit/linux-prebuild.cfg`
```
# Format: //devtools/kokoro/config/proto/build.proto

before_action {
  fetch_keystore {
    keystore_resource {
      keystore_config_id: 72935
      keyname: "cloud-profiler-e2e-service-account-key"
    }
  }
}

build_file: "pprof-nodejs/tools/build/linux_build_and_test.sh"
```

## File: `tools/kokoro/system-test/presubmit/linux.cfg`
```
# Format: //devtools/kokoro/config/proto/build.proto

build_file: "pprof-nodejs/system-test/system_test.sh"
```

## File: `ts/src/heap-profiler-bindings.ts`
```typescript
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

## File: `ts/src/heap-profiler.ts`
```typescript
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

## File: `ts/src/index.ts`
```typescript
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

## File: `ts/src/logger.ts`
```typescript
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

## File: `ts/src/profile-encoder.ts`
```typescript
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

## File: `ts/src/profile-serializer.ts`
```typescript
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
        break;
      default:
        continue;
    }
    labels.push(new Label(labelInput));
  }

  return labels;
}

/**
 * Converts v8 heap profile into into a profile proto.
 * (https://github.com/google/pprof/blob/master/proto/profile.proto)
 *
 * @param prof - profile to be converted.
 * @param startTimeNanos - start time of profile, in nanoseconds (POSIX time).
 * @param durationsNanos - duration of the profile (wall clock time) in
 * nanoseconds.
 * @param intervalBytes - bytes allocated between samples.
 */
export function serializeHeapProfile(
  prof: AllocationProfileNode,
  startTimeNanos: number,
  intervalBytes: number,
  ignoreSamplesPath?: string,
  sourceMapper?: SourceMapper,
  generateLabels?: GenerateAllocationLabelsFunction,
): Profile {
  const appendHeapEntryToSamples: AppendEntryToSamples<
    AllocationProfileNode
  > = (entry: Entry<AllocationProfileNode>, samples: Sample[]) => {
    if (entry.node.allocations.length > 0) {
      const labels = generateLabels
        ? buildLabels(generateLabels({node: entry.node}), stringTable)
        : [];
      for (const alloc of entry.node.allocations) {
        const sample = new Sample({
          locationId: entry.stack,
          value: [alloc.count, alloc.sizeBytes * alloc.count],
          label: labels,
          // TODO: add tag for allocation size
        });
        samples.push(sample);
      }
    }
  };

  const stringTable = new StringTable();
  const sampleValueType = createObjectCountValueType(stringTable);
  const allocationValueType = createAllocationValueType(stringTable);

  const profile = {
    sampleType: [sampleValueType, allocationValueType],
    timeNanos: startTimeNanos,
    periodType: allocationValueType,
    period: intervalBytes,
  };

  serialize(
    profile,
    prof,
    appendHeapEntryToSamples,
    stringTable,
    ignoreSamplesPath,
    sourceMapper,
  );

  return new Profile(profile);
}
```

## File: `ts/src/time-profiler-bindings.ts`
```typescript
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
import {join} from 'path';

const findBinding = require('node-gyp-build');
const profiler = findBinding(join(__dirname, '..', '..'));

export const TimeProfiler = profiler.TimeProfiler;
export const constants = profiler.constants;
export const getNativeThreadId = profiler.getNativeThreadId;
```

## File: `ts/src/time-profiler.ts`
```typescript
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

import {setTimeout} from 'timers/promises';

import {
  serializeTimeProfile,
  GARBAGE_COLLECTION_FUNCTION_NAME,
  NON_JS_THREADS_FUNCTION_NAME,
} from './profile-serializer';
import {SourceMapper} from './sourcemapper/sourcemapper';
import {
  TimeProfiler,
  getNativeThreadId,
  constants as profilerConstants,
} from './time-profiler-bindings';
import {
  GenerateTimeLabelsFunction,
  TimeProfile,
  TimeProfilerMetrics,
} from './v8-types';
import {isMainThread} from 'worker_threads';
import {AsyncLocalStorage} from 'async_hooks';
const {kSampleCount} = profilerConstants;

const DEFAULT_INTERVAL_MICROS: Microseconds = 1000;
const DEFAULT_DURATION_MILLIS: Milliseconds = 60000;

type Microseconds = number;
type Milliseconds = number;

type NativeTimeProfiler = InstanceType<typeof TimeProfiler> & {
  stopAndCollect: <T>(
    restart: boolean,
    callback: (profile: TimeProfile) => T,
  ) => T;
};

let gProfiler: NativeTimeProfiler | undefined;
let gStore: AsyncLocalStorage<unknown> | undefined;
let gSourceMapper: SourceMapper | undefined;
let gIntervalMicros: Microseconds;
let gV8ProfilerStuckEventLoopDetected = 0;

function handleStopRestart() {
  if (!gProfiler) {
    return;
  }
  gV8ProfilerStuckEventLoopDetected =
    gProfiler.v8ProfilerStuckEventLoopDetected();
  // Workaround for v8 bug, where profiler event processor thread is stuck in
  // a loop eating 100% CPU, leading to empty profiles.
  // Fully stop and restart the profiler to reset the profile to a valid state.
  if (gV8ProfilerStuckEventLoopDetected > 0) {
    gProfiler.stopAndCollect(false, () => undefined);
    gProfiler.start();
  }
}

function handleStopNoRestart() {
  gV8ProfilerStuckEventLoopDetected = 0;
  gProfiler?.dispose();
  gProfiler = undefined;
  gSourceMapper = undefined;
  if (gStore !== undefined) {
    gStore.disable();
    gStore = undefined;
  }
}

/** Make sure to stop profiler before node shuts down, otherwise profiling
 * signal might cause a crash if it occurs during shutdown */
process.once('exit', () => {
  if (isStarted()) stop();
});

export interface TimeProfilerOptions {
  /** time in milliseconds for which to collect profile. */
  durationMillis?: Milliseconds;
  /** average time in microseconds between samples */
  intervalMicros?: Microseconds;
  sourceMapper?: SourceMapper;

  /**
   * This configuration option is experimental.
   * When set to true, functions will be aggregated at the line level, rather
   * than at the function level.
   * This defaults to false.
   */
  lineNumbers?: boolean;
  withContexts?: boolean;
  workaroundV8Bug?: boolean;
  collectCpuTime?: boolean;
  collectAsyncId?: boolean;
  useCPED?: boolean;
}

const DEFAULT_OPTIONS: TimeProfilerOptions = {
  durationMillis: DEFAULT_DURATION_MILLIS,
  intervalMicros: DEFAULT_INTERVAL_MICROS,
  lineNumbers: false,
  withContexts: false,
  workaroundV8Bug: true,
  collectCpuTime: false,
  collectAsyncId: false,
  useCPED: false,
};

export async function profile(options: TimeProfilerOptions = {}) {
  options = {...DEFAULT_OPTIONS, ...options};
  start(options);
  await setTimeout(options.durationMillis!);
  return stop();
}

// Temporarily retained for backwards compatibility with older tracer
export function start(options: TimeProfilerOptions = {}) {
  options = {...DEFAULT_OPTIONS, ...options};
  if (gProfiler) {
    throw new Error('Wall profiler is already started');
  }

  const store = options.useCPED === true ? new AsyncLocalStorage() : undefined;
  gProfiler = new TimeProfiler({...options, CPEDKey: store, isMainThread});
  gSourceMapper = options.sourceMapper;
  gIntervalMicros = options.intervalMicros!;
  gV8ProfilerStuckEventLoopDetected = 0;

  gProfiler.start();
  gStore = store;

  // If contexts are enabled without using CPED, set an initial empty context
  if (options.withContexts && !options.useCPED) {
    setContext({});
  }
}

/**
 * Serializes the profile inside a native callback while the V8 profile is
 * still alive. This reduces memory overhead.
 */
export function stop(
  restart = false,
  generateLabels?: GenerateTimeLabelsFunction,
  lowCardinalityLabels?: string[],
) {
  if (!gProfiler) {
    throw new Error('Wall profiler is not started');
  }

  const serializedProfile = gProfiler.stopAndCollect(
    restart,
    (profile: TimeProfile) =>
      serializeTimeProfile(
        profile,
        gIntervalMicros,
        gSourceMapper,
        true,
        generateLabels,
        lowCardinalityLabels,
      ),
  );
  if (restart) {
    handleStopRestart();
  } else {
    handleStopNoRestart();
  }
  return serializedProfile;
}

export function getState() {
  if (!gProfiler) {
    throw new Error('Wall profiler is not started');
  }
  return gProfiler.state;
}

export function setContext(context?: object) {
  if (!gProfiler) {
    throw new Error('Wall profiler is not started');
  }
  gProfiler.context = context;
}

export function runWithContext<R, TArgs extends unknown[]>(
  context: object,
  f: (...args: TArgs) => R,
  ...args: TArgs
): R {
  if (!gProfiler) {
    throw new Error('Wall profiler is not started');
  } else if (!gStore) {
    throw new Error('Can only use runWithContext with AsyncContextFrame');
  }
  return gStore.run(gProfiler.createContextHolder(context), f, ...args);
}

export function getContext() {
  if (!gProfiler) {
    throw new Error('Wall profiler is not started');
  }
  return gProfiler.context;
}

export function getMetrics(): TimeProfilerMetrics {
  if (!gProfiler) {
    throw new Error('Wall profiler is not started');
  }
  return gProfiler.metrics as TimeProfilerMetrics;
}

export function isStarted() {
  return !!gProfiler;
}

// Return 0 if no issue detected, 1 if possible issue, 2 if issue detected for certain
export function v8ProfilerStuckEventLoopDetected() {
  return gV8ProfilerStuckEventLoopDetected;
}

export const constants = {
  kSampleCount,
  GARBAGE_COLLECTION_FUNCTION_NAME,
  NON_JS_THREADS_FUNCTION_NAME,
};
export {getNativeThreadId};
```

## File: `ts/src/v8-types.ts`
```typescript
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

// Type Definitions based on implementation in bindings/

export interface TimeProfile {
  /** Time in nanoseconds at which profile was stopped. */
  endTime: number;
  topDownRoot: TimeProfileNode;
  /** Time in nanoseconds at which profile was started. */
  startTime: number;
  hasCpuTime?: boolean;
  /** CPU time of non-JS threads, only reported for the main worker thread */
  nonJSThreadsCpuTime?: number;
  /** Computed in C++ to avoid a full JS tree traversal. */
  totalHitCount?: number;
}

export interface ProfileNode {
  // name is the function name.
  name?: string;
  scriptName: string;
  scriptId?: number;
  lineNumber?: number;
  columnNumber?: number;
  children: ProfileNode[];
}

export interface TimeProfileNodeContext {
  context?: object;
  timestamp: bigint; // end of sample taking; in microseconds since epoch
  cpuTime?: number; // cpu time in nanoseconds
  asyncId?: number; // async_hooks.executionAsyncId() at the time of sample taking
}

export interface TimeProfileNode extends ProfileNode {
  hitCount: number;
  contexts?: TimeProfileNodeContext[];
}

export interface AllocationProfileNode extends ProfileNode {
  allocations: Allocation[];
  children: AllocationProfileNode[];
}

export interface Allocation {
  sizeBytes: number;
  count: number;
}
export interface LabelSet {
  [key: string]: string | number;
}

export interface GenerateAllocationLabelsFunction {
  ({node}: {node: AllocationProfileNode}): LabelSet;
}

export interface GenerateTimeLabelsArgs {
  node: TimeProfileNode;
  context?: TimeProfileNodeContext;
}

export interface GenerateTimeLabelsFunction {
  (args: GenerateTimeLabelsArgs): LabelSet;
}

export interface TimeProfilerMetrics {
  usedAsyncContextCount: number;
  totalAsyncContextCount: number;
}
```

## File: `ts/src/sourcemapper/sourcemapper.ts`
```typescript
/**
 * Copyright 2016 Google Inc. All Rights Reserved.
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

// Originally copied from cloud-debug-nodejs's sourcemapper.ts from
// https://github.com/googleapis/cloud-debug-nodejs/blob/7bdc2f1f62a3b45b7b53ea79f9444c8ed50e138b/src/agent/io/sourcemapper.ts
// Modified to map from generated code to source code, rather than from source
// code to generated code.

import * as fs from 'fs';
import * as path from 'path';
import * as sourceMap from 'source-map';
import {logger} from '../logger';

const readFile = fs.promises.readFile;

const CONCURRENCY = 10;

function createLimiter(concurrency: number) {
  let active = 0;
  const queue: Array<() => void> = [];
  return function limit<T>(fn: () => Promise<T>): Promise<T> {
    return new Promise<T>((resolve, reject) => {
      const run = () => {
        active++;
        fn()
          .then(resolve, reject)
          .finally(() => {
            active--;
            if (queue.length > 0) queue.shift()!();
          });
      };
      if (active < concurrency) run();
      else queue.push(run);
    });
  };
}
const MAP_EXT = '.map';

// Per TC39 ECMA-426 §11.1.2.1 JavaScriptExtractSourceMapURL (without parsing):
// https://tc39.es/ecma426/#sec-linking-inline
//
// Split on these line terminators (ECMA-262 LineTerminatorSequence):
const LINE_SPLIT_RE = /\r\n|\n|\r|\u2028|\u2029/;
// Bytes to read from the end of a JS file when scanning for the annotation.
// The annotation must be on the last non-empty line, which is always short
// for external URLs. If no line terminator appears in the tail we fall back
// to a full file read (handles very large inline data: maps).
export const ANNOTATION_TAIL_BYTES = 4 * 1024;
// Quote code points that invalidate the annotation (U+0022, U+0027, U+0060):
const QUOTE_CHARS_RE = /["'`]/;
// MatchSourceMapURL pattern applied to the comment text that follows "//":
const MATCH_SOURCE_MAP_URL_RE = /^[@#]\s*sourceMappingURL=(\S*?)\s*$/;

/**
 * Extracts a sourceMappingURL from JS source per ECMA-426 §11.1.2.1
 * (without-parsing variant).
 *
 * Scans lines from the end, skipping empty/whitespace-only lines.
 * Returns null as soon as the first non-empty line is found that does not
 * carry a valid annotation — the URL must be on the last non-empty line.
 */
export function extractSourceMappingURL(content: string): string | undefined {
  const lines = content.split(LINE_SPLIT_RE);
  for (let i = lines.length - 1; i >= 0; i--) {
    const line = lines[i];
    if (line.trim() === '') continue; // skip empty / whitespace-only lines

    // This is the last non-empty line; it must carry the annotation or we stop.
    const commentStart = line.indexOf('//');
    if (commentStart === -1) return undefined;

    const comment = line.slice(commentStart + 2);
    if (QUOTE_CHARS_RE.test(comment)) return undefined;

    const match = MATCH_SOURCE_MAP_URL_RE.exec(comment);
    return match ? match[1] || undefined : undefined;
  }
  return undefined;
}

/**
 * Reads the sourceMappingURL from a JS file efficiently by only reading a
 * small tail of the file.
 *
 * The annotation must be on the last non-empty line (ECMA-426), so as long as
 * the tail contains at least one line terminator the last line is fully
 * captured. If no line terminator appears in the tail the entire tail is part
 * of one very long inline data: line; we fall back to a full file read in
 * that case.
 */
export async function readSourceMappingURL(
  filePath: string,
): Promise<string | undefined> {
  const fd = await fs.promises.open(filePath, 'r');
  try {
    const {size} = await fd.stat();
    if (size === 0) return undefined;

    const tailSize = Math.min(ANNOTATION_TAIL_BYTES, size);
    const buf = Buffer.allocUnsafe(tailSize);
    await fd.read(buf, 0, tailSize, size - tailSize);
    const tail = buf.toString('utf8');

    // The last non-empty line is fully captured in the tail if and only if a
    // line terminator that precedes it also falls within the tail — i.e. the
    // last non-empty segment is not the very first element of the split result.
    //
    // Counter-example: a large inline map followed by trailing empty lines.
    // The tail might be "<end of base64>\n\n", which contains line terminators
    // but whose last non-empty content ("<end of base64>") is the first
    // segment — it extends before the window. Checking LINE_TERM_RE alone
    // would incorrectly accept this tail.
    const lines = tail.split(LINE_SPLIT_RE);
    let lastNonEmptyIdx = lines.length - 1;
    while (lastNonEmptyIdx > 0 && lines[lastNonEmptyIdx].trim() === '') {
      lastNonEmptyIdx--;
    }
    if (tailSize === size || lastNonEmptyIdx > 0) {
      return extractSourceMappingURL(tail);
    }

    const fullContent = await readFile(filePath, 'utf8');
    return extractSourceMappingURL(fullContent);
  } finally {
    await fd.close();
  }
}

function error(msg: string) {
  logger.debug(`Error: ${msg}`);
  return new Error(msg);
}

export interface MapInfoCompiled {
  mapFileDir: string;
  mapConsumer: sourceMap.RawSourceMap;
}

export interface GeneratedLocation {
  file: string;
  name?: string;
  line: number;
  column: number;
}

export interface SourceLocation {
  file?: string;
  name?: string;
  line?: number;
  column?: number;
  /** True when the file declares a sourceMappingURL but the map could not be found. */
  missingMapFile?: boolean;
}

/**
 * @param {!Map} infoMap The map that maps input source files to
 *  SourceMapConsumer objects that are used to calculate mapping information
 * @param {string} mapPath The path to the source map file to process.  The
 *  path should be relative to the process's current working directory
 * @private
 */
async function processSourceMap(
  infoMap: Map<string, MapInfoCompiled>,
  mapPath: string,
  debug: boolean,
): Promise<void> {
  // this handles the case when the path is undefined, null, or
  // the empty string
  if (!mapPath || !mapPath.endsWith(MAP_EXT)) {
    throw error(`The path "${mapPath}" does not specify a source map file`);
  }
  mapPath = path.normalize(mapPath);

  let contents;
  try {
    contents = await readFile(mapPath, 'utf8');
  } catch (e) {
    throw error('Could not read source map file ' + mapPath + ': ' + e);
  }

  /* If the source map file defines a "file" attribute, use it as
   * the output file where the path is relative to the directory
   * containing the map file.  Otherwise, use the name of the output
   * file (with the .map extension removed) as the output file.

   * With nextjs/webpack, when there are subdirectories in `pages` directory,
   * the generated source maps do not reference correctly the generated files
   * in their `file` property.
   * For example if the generated file / source maps have paths:
   * <root>/pages/sub/foo.js(.map)
   * foo.js.map will have ../pages/sub/foo.js as `file` property instead of
   * ../../pages/sub/foo.js
   * To workaround this, check first if file referenced in `file` property
   * exists and if it does not, check if generated file exists alongside the
   * source map file.
   */
  const dir = path.dirname(mapPath);

  // Parse JSON once: extract the `file` property for early-exit checks and
  // reuse the parsed object when constructing SourceMapConsumer (avoids a
  // second parse inside the library).
  let parsedMap: sourceMap.RawSourceMap | undefined;
  let rawFile: string | undefined;
  try {
    parsedMap = JSON.parse(contents) as sourceMap.RawSourceMap;
    rawFile = parsedMap.file;
  } catch {
    // Will fail again below when creating SourceMapConsumer; let that throw.
  }

  const generatedPathCandidates: string[] = [];
  if (rawFile) {
    generatedPathCandidates.push(path.resolve(dir, rawFile));
  }
  const samePath = path.resolve(dir, path.basename(mapPath, MAP_EXT));
  if (
    generatedPathCandidates.length === 0 ||
    generatedPathCandidates[0] !== samePath
  ) {
    generatedPathCandidates.push(samePath);
  }

  // Find the first candidate that exists and hasn't been loaded already.
  let targetPath: string | undefined;
  for (const candidate of generatedPathCandidates) {
    if (infoMap.has(candidate)) {
      // Already loaded via sourceMappingURL annotation; skip this map file.
      if (debug) {
        logger.debug(
          `Skipping ${mapPath}: ${candidate} already loaded via sourceMappingURL`,
        );
      }
      return;
    }
    try {
      await fs.promises.access(candidate, fs.constants.F_OK);
      targetPath = candidate;
      break;
    } catch {
      if (debug) {
        logger.debug(`Generated path ${candidate} does not exist`);
      }
    }
  }

  if (!targetPath) {
    if (debug) {
      logger.debug(`Unable to find generated file for ${mapPath}`);
    }
    return;
  }

  let consumer: sourceMap.RawSourceMap;
  try {
    // TODO: Determine how to reconsile the type conflict where `consumer`
    //       is constructed as a SourceMapConsumer but is used as a
    //       RawSourceMap.
    consumer = (await new sourceMap.SourceMapConsumer(
      (parsedMap ?? contents) as {} as sourceMap.RawSourceMap,
    )) as {} as sourceMap.RawSourceMap;
  } catch (e) {
    throw error(
      'An error occurred while reading the ' +
        'sourceMap file ' +
        mapPath +
        ': ' +
        e,
    );
  }

  infoMap.set(targetPath, {mapFileDir: dir, mapConsumer: consumer});
  if (debug) {
    logger.debug(`Loaded source map for ${targetPath} => ${mapPath}`);
  }
}

export class SourceMapper {
  infoMap: Map<string, MapInfoCompiled>;
  /** JS files that declared a sourceMappingURL but no map was ultimately found. */
  private declaredMissingMap = new Set<string>();
  debug: boolean;

  static async create(
    searchDirs: string[],
    debug = false,
  ): Promise<SourceMapper> {
    const mapper = new SourceMapper(debug);
    for (const dir of searchDirs) {
      await mapper.loadDirectory(dir);
    }
    return mapper;
  }

  constructor(debug = false) {
    this.infoMap = new Map();
    this.debug = debug;
  }

  /**
   * Scans `searchDir` recursively for JS files and source map files, loading
   * source maps for all JS files found.
   *
   * Priority for each JS file:
   *  1. A map pointed to by a `sourceMappingURL` annotation in the JS file
   *     (inline `data:` URL or external file path, only if the file exists).
   *  2. A `.map` file found in the directory scan that claims to belong to
   *     that JS file (via its `file` property or naming convention).
   *
   * Safe to call multiple times; already-loaded files are skipped.
   */
  async loadDirectory(searchDir: string): Promise<void> {
    // Resolve to absolute so all paths in infoMap are consistent regardless of
    // whether the caller passed a relative or absolute directory.
    searchDir = path.resolve(searchDir);

    if (this.debug) {
      logger.debug(`Loading source maps from directory: ${searchDir}`);
    }

    const jsFiles: string[] = [];
    const mapFiles: string[] = [];

    for await (const entry of walk(
      searchDir,
      filename =>
        /\.[cm]?js$/.test(filename) || /\.[cm]?js\.map$/.test(filename),
      (root, dirname) =>
        root !== '/proc' && dirname !== '.git' && dirname !== 'node_modules',
    )) {
      if (entry.endsWith(MAP_EXT)) {
        mapFiles.push(entry);
      } else {
        jsFiles.push(entry);
      }
    }

    if (this.debug) {
      logger.debug(
        `Found ${jsFiles.length} JS files and ${mapFiles.length} map files in ${searchDir}`,
      );
    }

    const limit = createLimiter(CONCURRENCY);

    // JS files that declared a sourceMappingURL but Phase 1 couldn't load the map.
    const annotatedNotLoaded = new Set<string>();

    // Phase 1: Check sourceMappingURL annotations in JS files (higher priority).
    await Promise.all(
      jsFiles.map(jsPath =>
        limit(async () => {
          if (this.infoMap.has(jsPath)) return;

          let url: string | undefined;
          try {
            url = await readSourceMappingURL(jsPath);
          } catch {
            return;
          }
          if (!url) return;

          if (url.startsWith('data:')) {
            // Inline source map data URL. Handles both:
            //   data:application/json;base64,<b64>
            //   data:application/json;charset=utf-8;base64,<b64>
            //   data:application/json,<urlencoded>  (and other non-base64 forms)
            const commaIdx = url.indexOf(',');
            if (commaIdx !== -1) {
              const meta = url.slice(0, commaIdx);
              const data = url.slice(commaIdx + 1);
              const mapContent = meta.endsWith(';base64')
                ? Buffer.from(data, 'base64').toString()
                : decodeURIComponent(data);
              await this.loadMapContent(
                jsPath,
                mapContent,
                path.dirname(jsPath),
              );
            }
            // If the data URL is malformed (no comma), skip silently — not a
            // missing map file, just an unreadable inline annotation.
          } else {
            const mapPath = path.resolve(path.dirname(jsPath), url);
            try {
              const mapContent = await readFile(mapPath, 'utf8');
              await this.loadMapContent(
                jsPath,
                mapContent,
                path.dirname(mapPath),
              );
            } catch {
              // Map file doesn't exist or is unreadable; fall through to Phase 2.
              annotatedNotLoaded.add(jsPath);
            }
          }
        }),
      ),
    );

    // Phase 2: Process .map files for any JS files not yet resolved.
    await Promise.all(
      mapFiles.map(mapPath =>
        limit(() => processSourceMap(this.infoMap, mapPath, this.debug)),
      ),
    );

    // Any file whose annotation pointed to a missing map and that still has no
    // entry after Phase 2 is tracked as "declared but missing".
    for (const jsPath of annotatedNotLoaded) {
      if (!this.infoMap.has(jsPath)) {
        this.declaredMissingMap.add(jsPath);
      }
    }
  }

  private async loadMapContent(
    jsPath: string,
    mapContent: string,
    mapDir: string,
  ): Promise<void> {
    try {
      const parsedMap = JSON.parse(mapContent) as sourceMap.RawSourceMap;
      const consumer = (await new sourceMap.SourceMapConsumer(
        parsedMap,
      )) as {} as sourceMap.RawSourceMap;
      this.infoMap.set(jsPath, {mapFileDir: mapDir, mapConsumer: consumer});
      if (this.debug) {
        logger.debug(`Loaded source map for ${jsPath} via sourceMappingURL`);
      }
    } catch (e) {
      logger.debug(`Failed to parse source map for ${jsPath}: ${e}`);
    }
  }

  /**
   * Used to get the information about the transpiled file from a given input
   * source file provided there isn't any ambiguity with associating the input
   * path to exactly one output transpiled file.
   *
   * @param inputPath The (possibly relative) path to the original source file.
   * @return The `MapInfoCompiled` object that describes the transpiled file
   *  associated with the specified input path.  `null` is returned if either
   *  zero files are associated with the input path or if more than one file
   *  could possibly be associated with the given input path.
   */
  private getMappingInfo(inputPath: string): MapInfoCompiled | null {
    const normalizedPath = path.normalize(inputPath);
    if (this.infoMap.has(normalizedPath)) {
      return this.infoMap.get(normalizedPath) as MapInfoCompiled;
    }
    return null;
  }

  /**
   * Used to determine if the source file specified by the given path has
   * a .map file and an output file associated with it.
   *
   * If there is no such mapping, it could be because the input file is not
   * the input to a transpilation process or it is the input to a transpilation
   * process but its corresponding .map file was not given to the constructor
   * of this mapper.
   *
   * @param {string} inputPath The path to an input file that could
   *  possibly be the input to a transpilation process.  The path should be
   *  relative to the process's current working directory.
   */
  hasMappingInfo(inputPath: string): boolean {
    return this.getMappingInfo(inputPath) !== null;
  }

  /**
   * @param {string} inputPath The path to an input file that could possibly
   *  be the input to a transpilation process.  The path should be relative to
   *  the process's current working directory
   * @param {number} The line number in the input file where the line number is
   *   zero-based.
   * @param {number} (Optional) The column number in the line of the file
   *   specified where the column number is zero-based.
   * @return {Object} The object returned has a "file" attribute for the
   *   path of the output file associated with the given input file (where the
   *   path is relative to the process's current working directory),
   *   a "line" attribute of the line number in the output file associated with
   *   the given line number for the input file, and an optional "column" number
   *   of the column number of the output file associated with the given file
   *   and line information.
   *
   *   If the given input file does not have mapping information associated
   *   with it then the input location is returned.
   */
  mappingInfo(location: GeneratedLocation): SourceLocation {
    const inputPath = path.normalize(location.file);
    const entry = this.getMappingInfo(inputPath);
    if (entry === null) {
      if (this.debug) {
        logger.debug(
          `Source map lookup failed: no map found for ${location.file} (normalized: ${inputPath})`,
        );
      }
      if (this.declaredMissingMap.has(inputPath)) {
        return {...location, missingMapFile: true};
      }
      return location;
    }

    const generatedPos = {
      line: location.line,
      column: location.column > 0 ? location.column - 1 : 0, // SourceMapConsumer expects column to be 0-based
    };

    // TODO: Determine how to remove the explicit cast here.
    const consumer: sourceMap.SourceMapConsumer =
      entry.mapConsumer as {} as sourceMap.SourceMapConsumer;

    // When column is 0, we don't have real column info (e.g., from V8's LineTick
    // which only provides line numbers). Use LEAST_UPPER_BOUND to find the first
    // mapping on this line instead of failing because there's nothing at column 0.
    const bias =
      generatedPos.column === 0
        ? sourceMap.SourceMapConsumer.LEAST_UPPER_BOUND
        : sourceMap.SourceMapConsumer.GREATEST_LOWER_BOUND;

    const pos = consumer.originalPositionFor({...generatedPos, bias});
    if (pos.source === null) {
      if (this.debug) {
        logger.debug(
          `Source map lookup failed for ${location.name}(${location.file}:${location.line}:${location.column})`,
        );
      }
      return location;
    }

    const loc = {
      file: path.resolve(entry.mapFileDir, pos.source),
      line: pos.line || undefined,
      name: pos.name || location.name,
      column: pos.column === null ? undefined : pos.column + 1, // convert column back to 1-based
    };

    if (this.debug) {
      logger.debug(
        `Source map lookup succeeded for ${location.name}(${location.file}:${location.line}:${location.column}) => ${loc.name}(${loc.file}:${loc.line}:${loc.column})`,
      );
    }
    return loc;
  }
}

function isErrnoException(e: unknown): e is NodeJS.ErrnoException {
  return e instanceof Error && 'code' in e;
}

function isNonFatalError(error: unknown) {
  const nonFatalErrors = ['ENOENT', 'EPERM', 'EACCES', 'ELOOP'];

  return (
    isErrnoException(error) && error.code && nonFatalErrors.includes(error.code)
  );
}

async function* walk(
  dir: string,
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  fileFilter = (filename: string) => true,
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  directoryFilter = (root: string, dirname: string) => true,
): AsyncIterable<string> {
  async function* walkRecursive(dir: string): AsyncIterable<string> {
    try {
      for await (const d of await fs.promises.opendir(dir)) {
        const entry = path.join(dir, d.name);
        if (d.isDirectory() && directoryFilter(dir, d.name)) {
          yield* walkRecursive(entry);
        } else if (d.isFile() && fileFilter(d.name)) {
          // check that the file is readable
          await fs.promises.access(entry, fs.constants.R_OK);
          yield entry;
        }
      }
    } catch (error) {
      if (!isNonFatalError(error)) {
        throw error;
      } else {
        logger.debug(() => `Non fatal error: ${error}`);
      }
    }
  }

  yield* walkRecursive(dir);
}
```

## File: `ts/test/check_profile.ts`
```typescript
import fs from 'fs';

if (fs.existsSync(process.argv[1])) {
  fs.writeFileSync('oom_check.log', 'ok');
} else {
  fs.writeFileSync('oom_check.log', 'ko');
}
```

## File: `ts/test/oom.ts`
```typescript
'use strict';

import {Worker, isMainThread, threadId} from 'worker_threads';
import {heap} from '../src/index';
import path from 'path';

const nworkers = Number(process.argv[2] || 0);
const workerMaxOldGenerationSizeMb = process.argv[3];
const maxCount = Number(process.argv[4] || 12);
const sleepMs = Number(process.argv[5] || 50);
const sizeQuantum = Number(process.argv[6] || 5 * 1024 * 1024);

console.log(`${isMainThread ? 'Main thread' : `Worker ${threadId}`}: \
nworkers=${nworkers} workerMaxOldGenerationSizeMb=${workerMaxOldGenerationSizeMb} \
maxCount=${maxCount} sleepMs=${sleepMs} sizeQuantum=${sizeQuantum}`);

heap.start(1024 * 1024, 64);
heap.monitorOutOfMemory(0, 0, false, [
  process.execPath,
  path.join(__dirname, 'check_profile.js'),
]);

if (isMainThread) {
  for (let i = 0; i < nworkers; i++) {
    const worker = new Worker(__filename, {
      argv: [0, ...process.argv.slice(3)],
      ...(workerMaxOldGenerationSizeMb
        ? {resourceLimits: {maxOldGenerationSizeMb: 50}}
        : {}),
    });
    const threadId = worker.threadId;
    worker
      .on('error', err => {
        console.log(`Worker ${threadId} error: ${err}`);
      })
      .on('exit', code => {
        console.log(`Worker ${threadId} exit: ${code}`);
      });
  }
}

const leak: number[][] = [];
let count = 0;

function foo(size: number) {
  count += 1;
  const n = size / 8;
  const x: number[] = [];
  x.length = n;
  for (let i = 0; i < n; i++) {
    x[i] = Math.random();
  }
  leak.push(x);

  if (count < maxCount) {
    setTimeout(() => foo(size), sleepMs);
  }
}

setTimeout(() => foo(sizeQuantum), sleepMs);
```

## File: `ts/test/profiles-for-tests.ts`
```typescript
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

import * as fs from 'fs';
import * as path from 'path';
import * as tmp from 'tmp';
import {SourceMapGenerator} from 'source-map';

import {Function, Location, Profile, Sample, ValueType} from 'pprof-format';

import {TimeProfile} from '../src/v8-types';
import {StringTable} from 'pprof-format';

import assert from 'assert';

function buildStringTable(values: string[]): StringTable {
  const table = new StringTable();
  for (const value of values) {
    table.dedup(value);
  }
  return table;
}

const timeLeaf1 = {
  name: 'function1',
  scriptName: 'script1',
  scriptId: 1,
  lineNumber: 10,
  columnNumber: 5,
  hitCount: 1,
  children: [],
};

const timeLeaf2 = {
  name: 'function1',
  scriptName: 'script2',
  scriptId: 2,
  lineNumber: 15,
  columnNumber: 3,
  hitCount: 2,
  children: [],
};

const timeLeaf3 = {
  name: 'function1',
  scriptName: 'script1',
  scriptId: 1,
  lineNumber: 5,
  columnNumber: 3,
  hitCount: 1,
  children: [],
};

const timeNode1 = {
  name: 'function1',
  scriptName: 'script1',
  scriptId: 1,
  lineNumber: 5,
  columnNumber: 3,
  hitCount: 3,
  children: [timeLeaf1, timeLeaf2],
};

const timeNode2 = {
  name: 'function2',
  scriptName: 'script2',
  scriptId: 2,
  lineNumber: 1,
  columnNumber: 5,
  hitCount: 0,
  children: [timeLeaf3],
};

const timeRoot = Object.freeze({
  name: '(root)',
  scriptName: 'root',
  scriptId: 0,
  lineNumber: 0,
  columnNumber: 0,
  hitCount: 0,
  children: [timeNode1, timeNode2],
});

export const v8TimeProfile: TimeProfile = Object.freeze({
  startTime: 0,
  endTime: 7 * 1000,
  topDownRoot: timeRoot,
});

const timeLines = [
  {functionId: 1, line: 1},
  {functionId: 2, line: 5},
  {functionId: 3, line: 15},
  {functionId: 2, line: 10},
];

const timeFunctions = [
  new Function({
    id: 1,
    name: 5,
    systemName: 5,
    filename: 6,
  }),
  new Function({
    id: 2,
    name: 7,
    systemName: 7,
    filename: 8,
  }),
  new Function({
    id: 3,
    name: 7,
    systemName: 7,
    filename: 6,
  }),
];

const timeLocations = [
  new Location({
    line: [timeLines[0]],
    id: 1,
  }),
  new Location({
    line: [timeLines[1]],
    id: 2,
  }),
  new Location({
    line: [timeLines[2]],
    id: 3,
  }),
  new Location({
    line: [timeLines[3]],
    id: 4,
  }),
];

export const timeProfile = new Profile({
  sampleType: [
    new ValueType({type: 1, unit: 2}),
    new ValueType({type: 3, unit: 4}),
  ],
  sample: [
    new Sample({
      locationId: [2, 1],
      value: [1, 1000000],
      label: [],
    }),
    new Sample({
      locationId: [2],
      value: [3, 3000000],
      label: [],
    }),
    new Sample({
      locationId: [3, 2],
      value: [2, 2000000],
      label: [],
    }),
    new Sample({
      locationId: [4, 2],
      value: [1, 1000000],
      label: [],
    }),
  ],
  location: timeLocations,
  function: timeFunctions,
  stringTable: buildStringTable([
    'sample',
    'count',
    'wall',
    'nanoseconds',
    'function2',
    'script2',
    'function1',
    'script1',
  ]),
  timeNanos: 0,
  durationNanos: 7 * 1000 * 1000,
  periodType: new ValueType({type: 3, unit: 4}),
  period: 1000000,
});

// timeProfile is encoded then decoded to convert numbers to longs, in
// decodedTimeProfile
const encodedTimeProfile = timeProfile.encode();
export const decodedTimeProfile = Object.freeze(
  Profile.decode(encodedTimeProfile),
);

const heapLeaf1 = {
  name: 'function2',
  scriptName: 'script1',
  scriptId: 1,
  lineNumber: 8,
  columnNumber: 5,
  allocations: [{count: 5, sizeBytes: 1024}],
  children: [],
};

const heapLeaf2 = {
  name: 'function3',
  scriptName: 'script1',
  scriptId: 1,
  lineNumber: 10,
  columnNumber: 5,
  allocations: [
    {count: 8, sizeBytes: 10},
    {count: 15, sizeBytes: 72},
  ],
  children: [],
};

const heapNode2 = {
  name: 'function1',
  scriptName: 'script1',
  scriptId: 1,
  lineNumber: 5,
  columnNumber: 5,
  allocations: [],
  children: [heapLeaf1, heapLeaf2],
};

const heapNode1 = {
  name: 'main',
  scriptName: 'main',
  scriptId: 0,
  lineNumber: 1,
  columnNumber: 5,
  allocations: [
    {count: 1, sizeBytes: 5},
    {count: 3, sizeBytes: 7},
  ],
  children: [heapNode2],
};

export const v8HeapProfile = Object.freeze({
  name: '(root)',
  scriptName: '(root)',
  scriptId: 10000,
  lineNumber: 0,
  columnNumber: 5,
  allocations: [],
  children: [heapNode1],
});

const heapLines = [
  {functionId: 1, line: 1},
  {functionId: 2, line: 5},
  {functionId: 3, line: 10},
  {functionId: 4, line: 8},
];

const heapFunctions = [
  new Function({
    id: 1,
    name: 5,
    systemName: 5,
    filename: 5,
  }),
  new Function({
    id: 2,
    name: 6,
    systemName: 6,
    filename: 7,
  }),
  new Function({
    id: 3,
    name: 8,
    systemName: 8,
    filename: 7,
  }),
  new Function({
    id: 4,
    name: 9,
    systemName: 9,
    filename: 7,
  }),
];

const heapLocations = [
  new Location({line: [heapLines[0]], id: 1}),
  new Location({line: [heapLines[1]], id: 2}),
  new Location({line: [heapLines[2]], id: 3}),
  new Location({line: [heapLines[3]], id: 4}),
];

export const heapProfile = new Profile({
  sampleType: [
    new ValueType({type: 1, unit: 2}),
    new ValueType({type: 3, unit: 4}),
  ],
  sample: [
    new Sample({
      locationId: [1],
      value: [1, 5],
      label: [],
    }),
    new Sample({
      locationId: [1],
      value: [3, 21],
      label: [],
    }),
    new Sample({
      locationId: [3, 2, 1],
      value: [8, 80],
      label: [],
    }),
    new Sample({
      locationId: [3, 2, 1],
      value: [15, 15 * 72],
      label: [],
    }),
    new Sample({
      locationId: [4, 2, 1],
      value: [5, 5 * 1024],
      label: [],
    }),
  ],
  location: heapLocations,
  function: heapFunctions,
  stringTable: buildStringTable([
    'objects',
    'count',
    'space',
    'bytes',
    'main',
    'function1',
    'script1',
    'function3',
    'function2',
  ]),
  timeNanos: 0,
  periodType: new ValueType({type: 3, unit: 4}),
  period: 524288,
});

// heapProfile is encoded then decoded to convert numbers to longs, in
// decodedHeapProfile
const encodedHeapProfile = heapProfile.encode();
export const decodedHeapProfile = Object.freeze(
  Profile.decode(encodedHeapProfile),
);

const heapLinesWithExternal = [
  {functionId: 1},
  {functionId: 2, line: 1},
  {functionId: 3, line: 5},
  {functionId: 4, line: 10},
  {functionId: 5, line: 8},
];

const heapFunctionsWithExternal = [
  new Function({
    id: 1,
    name: 5,
    systemName: 5,
    filename: 0,
  }),
  new Function({
    id: 2,
    name: 6,
    systemName: 6,
    filename: 6,
  }),
  new Function({
    id: 3,
    name: 7,
    systemName: 7,
    filename: 8,
  }),
  new Function({
    id: 4,
    name: 9,
    systemName: 9,
    filename: 8,
  }),
  new Function({
    id: 5,
    name: 10,
    systemName: 10,
    filename: 8,
  }),
];

const heapLocationsWithExternal = [
  new Location({line: [heapLinesWithExternal[0]], id: 1}),
  new Location({line: [heapLinesWithExternal[1]], id: 2}),
  new Location({line: [heapLinesWithExternal[2]], id: 3}),
  new Location({line: [heapLinesWithExternal[3]], id: 4}),
  new Location({line: [heapLinesWithExternal[4]], id: 5}),
];

export const heapProfileWithExternal = new Profile({
  sampleType: [
    new ValueType({type: 1, unit: 2}),
    new ValueType({type: 3, unit: 4}),
  ],
  sample: [
    new Sample({
      locationId: [1],
      value: [1, 1024],
      label: [],
    }),
    new Sample({
      locationId: [2],
      value: [1, 5],
      label: [],
    }),
    new Sample({
      locationId: [2],
      value: [3, 21],
      label: [],
    }),
    new Sample({
      locationId: [4, 3, 2],
      value: [8, 80],
      label: [],
    }),
    new Sample({
      locationId: [4, 3, 2],
      value: [15, 15 * 72],
      label: [],
    }),
    new Sample({
      locationId: [5, 3, 2],
      value: [5, 5 * 1024],
      label: [],
    }),
  ],
  location: heapLocationsWithExternal,
  function: heapFunctionsWithExternal,
  stringTable: buildStringTable([
    'objects',
    'count',
    'space',
    'bytes',
    '(external)',
    'main',
    'function1',
    'script1',
    'function3',
    'function2',
  ]),
  timeNanos: 0,
  periodType: new ValueType({type: 3, unit: 4}),
  period: 524288,
});

// heapProfile is encoded then decoded to convert numbers to longs, in
// decodedHeapProfile
const encodedHeapProfileWithExternal = heapProfile.encode();
export const decodedHeapProfileWithExternal = Object.freeze(
  Profile.decode(encodedHeapProfileWithExternal),
);

const anonymousHeapNode = {
  scriptName: 'main',
  scriptId: 0,
  lineNumber: 1,
  columnNumber: 5,
  allocations: [{count: 1, sizeBytes: 5}],
  children: [],
};

export const v8AnonymousFunctionHeapProfile = Object.freeze({
  name: '(root)',
  scriptName: '(root)',
  scriptId: 10000,
  lineNumber: 0,
  columnNumber: 5,
  allocations: [],
  children: [anonymousHeapNode],
});

const anonymousFunctionHeapLines = [{functionId: 1, line: 1}];

const anonymousFunctionHeapFunctions = [
  new Function({
    id: 1,
    name: 5,
    systemName: 5,
    filename: 6,
  }),
];

const anonymousFunctionHeapLocations = [
  new Location({
    line: [anonymousFunctionHeapLines[0]],
    id: 1,
  }),
];

export const anonymousFunctionHeapProfile = new Profile({
  sampleType: [
    new ValueType({type: 1, unit: 2}),
    new ValueType({type: 3, unit: 4}),
  ],
  sample: [
    new Sample({
      locationId: [1],
      value: [1, 5],
      label: [],
    }),
  ],
  location: anonymousFunctionHeapLocations,
  function: anonymousFunctionHeapFunctions,
  stringTable: buildStringTable([
    'objects',
    'count',
    'space',
    'bytes',
    '(anonymous:L#1:C#5)',
    'main',
  ]),
  timeNanos: 0,
  periodType: new ValueType({type: 3, unit: 4}),
  period: 524288,
});

const anonymousFunctionTimeNode = {
  scriptName: 'main',
  scriptId: 2,
  lineNumber: 1,
  columnNumber: 5,
  hitCount: 1,
  children: [],
};

const anonymousFunctionTimeRoot = {
  name: '(root)',
  scriptName: 'root',
  scriptId: 0,
  lineNumber: 0,
  columnNumber: 0,
  hitCount: 0,
  children: [anonymousFunctionTimeNode],
};

export const v8AnonymousFunctionTimeProfile: TimeProfile = Object.freeze({
  startTime: 0,
  endTime: 10 * 1000 * 1000,
  topDownRoot: anonymousFunctionTimeRoot,
});

const anonymousFunctionTimeLines = [{functionId: 1, line: 1}];

const anonymousFunctionTimeFunctions = [
  new Function({
    id: 1,
    name: 5,
    systemName: 5,
    filename: 6,
  }),
];

const anonymousFunctionTimeLocations = [
  new Location({
    line: [anonymousFunctionTimeLines[0]],
    id: 1,
  }),
];

export const anonymousFunctionTimeProfile = new Profile({
  sampleType: [
    new ValueType({type: 1, unit: 2}),
    new ValueType({type: 3, unit: 4}),
  ],
  sample: [
    new Sample({
      locationId: [1],
      value: [1, 1000000],
      label: [],
    }),
  ],
  location: anonymousFunctionTimeLocations,
  function: anonymousFunctionTimeFunctions,
  stringTable: buildStringTable([
    'sample',
    'count',
    'wall',
    'nanoseconds',
    '(anonymous:L#1:C#5)',
    'main',
  ]),
  timeNanos: 0,
  durationNanos: 10 * 1000 * 1000 * 1000,
  periodType: new ValueType({type: 3, unit: 4}),
  period: 1000000,
});

const heapWithPathLeaf1 = {
  name: 'foo2',
  scriptName: 'foo.ts',
  scriptId: 0,
  lineNumber: 3,
  columnNumber: 3,
  allocations: [{count: 1, sizeBytes: 2}],
  children: [],
};

const heapWithPathLeaf2 = {
  name: 'bar',
  scriptName: '@google-cloud/profiler/profiler.ts',
  scriptId: 1,
  lineNumber: 10,
  columnNumber: 5,
  allocations: [{count: 2, sizeBytes: 2}],
  children: [],
};

const heapWithPathLeaf3 = {
  name: 'bar',
  scriptName: 'bar.ts',
  scriptId: 2,
  lineNumber: 3,
  columnNumber: 3,
  allocations: [{count: 3, sizeBytes: 2}],
  children: [],
};

const heapWithPathNode2 = {
  name: 'baz',
  scriptName: 'foo.ts',
  scriptId: 0,
  lineNumber: 1,
  columnNumber: 5,
  allocations: [],
  children: [heapWithPathLeaf1, heapWithPathLeaf2],
};

const heapWithPathNode1 = {
  name: 'foo1',
  scriptName: 'node_modules/@google-cloud/profiler/profiler.ts',
  scriptId: 3,
  lineNumber: 2,
  columnNumber: 5,
  allocations: [],
  children: [heapWithPathLeaf3],
};

export const v8HeapWithPathProfile = Object.freeze({
  name: '(root)',
  scriptName: '(root)',
  scriptId: 10000,
  lineNumber: 0,
  columnNumber: 5,
  allocations: [],
  children: [heapWithPathNode1, heapWithPathNode2],
});

const heapIncludePathFunctions = [
  new Function({
    id: 1,
    name: 5,
    systemName: 5,
    filename: 6,
  }),
  new Function({
    id: 2,
    name: 7,
    systemName: 7,
    filename: 8,
  }),
  new Function({
    id: 3,
    name: 9,
    systemName: 9,
    filename: 6,
  }),
  new Function({
    id: 4,
    name: 10,
    systemName: 10,
    filename: 11,
  }),
  new Function({
    id: 5,
    name: 7,
    systemName: 7,
    filename: 12,
  }),
];

const heapIncludePathLocations = [
  new Location({
    line: [{functionId: 1, line: 1}],
    id: 1,
  }),
  new Location({
    line: [{functionId: 2, line: 10}],
    id: 2,
  }),
  new Location({
    line: [{functionId: 3, line: 3}],
    id: 3,
  }),
  new Location({
    line: [{functionId: 4, line: 2}],
    id: 4,
  }),
  new Location({
    line: [{functionId: 5, line: 3}],
    id: 5,
  }),
];

export const heapProfileIncludePath = new Profile({
  sampleType: [
    new ValueType({type: 1, unit: 2}),
    new ValueType({type: 3, unit: 4}),
  ],
  sample: [
    new Sample({
      locationId: [2, 1],
      value: [2, 4],
      label: [],
    }),
    new Sample({
      locationId: [3, 1],
      value: [1, 2],
      label: [],
    }),
    new Sample({
      locationId: [5, 4],
      value: [3, 6],
      label: [],
    }),
  ],
  location: heapIncludePathLocations,
  function: heapIncludePathFunctions,
  stringTable: buildStringTable([
    'objects',
    'count',
    'space',
    'bytes',
    'baz',
    'foo.ts',
    'bar',
    '@google-cloud/profiler/profiler.ts',
    'foo2',
    'foo1',
    'node_modules/@google-cloud/profiler/profiler.ts',
    'bar.ts',
  ]),
  timeNanos: 0,
  periodType: new ValueType({type: 3, unit: 4}),
  period: 524288,
});

export const heapProfileIncludePathWithLabels = new Profile({
  sampleType: [
    new ValueType({type: 1, unit: 2}),
    new ValueType({type: 3, unit: 4}),
  ],
  sample: [
    new Sample({
      locationId: [2, 1],
      value: [2, 4],
      label: [
        {
          key: 5,
          num: 0,
          numUnit: 0,
          str: 7,
        },
      ],
    }),
    new Sample({
      locationId: [3, 1],
      value: [1, 2],
      label: [
        {
          key: 5,
          num: 0,
          numUnit: 0,
          str: 7,
        },
      ],
    }),
    new Sample({
      locationId: [5, 4],
      value: [3, 6],
      label: [
        {
          key: 5,
          num: 0,
          numUnit: 0,
          str: 7,
        },
      ],
    }),
  ],
  location: heapIncludePathLocations,
  function: heapIncludePathFunctions,
  stringTable: buildStringTable([
    'objects',
    'count',
    'space',
    'bytes',
    'baz',
    'foo.ts',
    'bar',
    '@google-cloud/profiler/profiler.ts',
    'foo2',
    'foo1',
    'node_modules/@google-cloud/profiler/profiler.ts',
    'bar.ts',
  ]),
  timeNanos: 0,
  periodType: new ValueType({type: 3, unit: 4}),
  period: 524288,
});

// heapProfile is encoded then decoded to convert numbers to longs, in
// decodedHeapProfile
const encodedHeapProfileIncludePath = heapProfileIncludePath.encode();
export const decodedHeapProfileIncludePath = Object.freeze(
  Profile.decode(encodedHeapProfileIncludePath),
);

const heapExcludePathFunctions = [
  new Function({
    id: 1,
    name: 5,
    systemName: 5,
    filename: 6,
  }),
  new Function({
    id: 2,
    name: 7,
    systemName: 7,
    filename: 6,
  }),
];

const heapExcludePathLocations = [
  new Location({
    line: [{functionId: 1, line: 1}],
    id: 1,
  }),
  new Location({
    line: [{functionId: 2, line: 3}],
    id: 2,
  }),
];

export const heapProfileExcludePath = new Profile({
  sampleType: [
    new ValueType({type: 1, unit: 2}),
    new ValueType({type: 3, unit: 4}),
  ],
  sample: [
    new Sample({
      locationId: [2, 1],
      value: [1, 2],
      label: [],
    }),
  ],
  location: heapExcludePathLocations,
  function: heapExcludePathFunctions,
  stringTable: buildStringTable([
    'objects',
    'count',
    'space',
    'bytes',
    'baz',
    'foo.ts',
    'foo2',
  ]),
  timeNanos: 0,
  periodType: new ValueType({type: 3, unit: 4}),
  period: 524288,
});

// heapProfile is encoded then decoded to convert numbers to longs, in
// decodedHeapProfile
const encodedHeapProfileExcludePath = heapProfileExcludePath.encode();
export const decodedHeapProfileExcludePath = Object.freeze(
  Profile.decode(encodedHeapProfileExcludePath),
);

export const mapDirPath = ((name: string) => {
  if (process.platform === 'win32') {
    // map-source turns drive letters to lowercase, so we should do it too so the
    // string comparisons of paths in assertions succeed.
    return name.substring(0, 1).toLowerCase().concat(name.substring(1));
  }
  return name;
})(tmp.dirSync().name);

export const mapFoo = new SourceMapGenerator({file: 'foo.js'});
mapFoo.addMapping({
  source: path.join(mapDirPath, 'foo.ts'),
  name: 'foo1',
  generated: {line: 1, column: 3},
  original: {line: 10, column: 0},
});
mapFoo.addMapping({
  source: path.join(mapDirPath, 'foo.ts'),
  name: 'foo2',
  generated: {line: 5, column: 5},
  original: {line: 20, column: 0},
});

export const mapBaz = new SourceMapGenerator({file: 'baz.js'});
mapBaz.addMapping({
  source: path.join(mapDirPath, 'baz.ts'),
  name: 'baz',
  generated: {line: 3, column: 0},
  original: {line: 5, column: 0},
});

fs.writeFileSync(path.join(mapDirPath, 'foo.js.map'), mapFoo.toString());
fs.writeFileSync(path.join(mapDirPath, 'foo.js'), '');
fs.writeFileSync(path.join(mapDirPath, 'baz.js.map'), mapBaz.toString());
fs.writeFileSync(path.join(mapDirPath, 'baz.js'), '');

const heapGeneratedLeaf1 = {
  name: 'foo2',
  scriptName: path.join(mapDirPath, 'foo.js'),
  scriptId: 1,
  lineNumber: 5,
  columnNumber: 6,
  allocations: [{count: 3, sizeBytes: 2}],
  children: [],
};

const heapGeneratedLeaf2 = {
  name: 'baz',
  scriptName: path.join(mapDirPath, 'baz.js'),
  scriptId: 3,
  lineNumber: 3,
  columnNumber: 1,
  allocations: [{count: 5, sizeBytes: 5}],
  children: [],
};

const heapGeneratedNode2 = {
  name: 'bar',
  scriptName: path.join(mapDirPath, 'bar.js'),
  scriptId: 2,
  lineNumber: 10,
  columnNumber: 1,
  allocations: [],
  children: [heapGeneratedLeaf2],
};

const heapGeneratedNode1 = {
  name: 'foo1',
  scriptName: path.join(mapDirPath, 'foo.js'),
  scriptId: 1,
  lineNumber: 1,
  columnNumber: 4,
  allocations: [],
  children: [heapGeneratedNode2, heapGeneratedLeaf1],
};

export const v8HeapGeneratedProfile = Object.freeze({
  name: '(root)',
  scriptName: '(root)',
  scriptId: 10000,
  lineNumber: 0,
  columnNumber: 0,
  allocations: [],
  children: [heapGeneratedNode1],
});

const heapSourceFunctions = [
  new Function({
    id: 1,
    name: 5,
    systemName: 5,
    filename: 6,
  }),
  new Function({
    id: 2,
    name: 7,
    systemName: 7,
    filename: 6,
  }),
  new Function({
    id: 3,
    name: 8,
    systemName: 8,
    filename: 9,
  }),
  new Function({
    id: 4,
    name: 10,
    systemName: 10,
    filename: 11,
  }),
];

const heapSourceLocations = [
  new Location({
    line: [{functionId: 1, line: 10}],
    id: 1,
  }),
  new Location({
    line: [{functionId: 2, line: 20}],
    id: 2,
  }),
  new Location({
    line: [{functionId: 3, line: 10}],
    id: 3,
  }),
  new Location({
    line: [{functionId: 4, line: 5}],
    id: 4,
  }),
];

export const heapSourceProfile = new Profile({
  sampleType: [
    new ValueType({type: 1, unit: 2}),
    new ValueType({type: 3, unit: 4}),
  ],
  sample: [
    new Sample({
      locationId: [2, 1],
      value: [3, 6],
      label: [],
    }),
    new Sample({
      locationId: [4, 3, 1],
      value: [5, 25],
      label: [],
    }),
  ],
  location: heapSourceLocations,
  function: heapSourceFunctions,
  stringTable: buildStringTable([
    'objects',
    'count',
    'space',
    'bytes',
    'foo1',
    path.join(mapDirPath, 'foo.ts'),
    'foo2',
    'bar',
    path.join(mapDirPath, 'bar.js'),
    'baz',
    path.join(mapDirPath, 'baz.ts'),
  ]),
  timeNanos: 0,
  periodType: new ValueType({type: 3, unit: 4}),
  period: 524288,
});

const timeGeneratedLeaf1 = {
  name: 'foo',
  scriptName: path.join(mapDirPath, 'foo.js'),
  scriptId: 1,
  lineNumber: 5,
  columnNumber: 6,
  hitCount: 5,
  children: [],
};

const timeGeneratedLeaf2 = {
  name: 'baz',
  scriptName: path.join(mapDirPath, 'baz.js'),
  scriptId: 3,
  lineNumber: 3,
  columnNumber: 1,
  hitCount: 10,
  children: [],
};

const timeGeneratedNode2 = {
  name: 'bar',
  scriptName: path.join(mapDirPath, 'bar.js'),
  scriptId: 2,
  lineNumber: 10,
  columnNumber: 1,
  children: [timeGeneratedLeaf2],
};

const timeGeneratedNode1 = {
  name: 'foo1',
  scriptName: path.join(mapDirPath, 'foo.js'),
  scriptId: 1,
  lineNumber: 1,
  columnNumber: 4,
  hitCount: 0,
  children: [timeGeneratedNode2, timeGeneratedLeaf1],
};

export const timeGeneratedProfileRoot = Object.freeze({
  name: '(root)',
  scriptName: '(root)',
  scriptId: 10000,
  lineNumber: 0,
  columnNumber: 0,
  hitCount: 0,
  children: [timeGeneratedNode1],
});

export const v8TimeGeneratedProfile: TimeProfile = Object.freeze({
  startTime: 0,
  endTime: 10 * 1000 * 1000,
  topDownRoot: timeGeneratedProfileRoot,
});

const timeSourceFunctions = [
  new Function({
    id: 1,
    name: 5,
    systemName: 5,
    filename: 6,
  }),
  new Function({
    id: 2,
    name: 7,
    systemName: 7,
    filename: 6,
  }),
  new Function({
    id: 3,
    name: 8,
    systemName: 8,
    filename: 9,
  }),
  new Function({
    id: 4,
    name: 10,
    systemName: 10,
    filename: 11,
  }),
];

const timeSourceLocations = [
  new Location({
    line: [{functionId: 1, line: 10}],
    id: 1,
  }),
  new Location({
    line: [{functionId: 2, line: 20}],
    id: 2,
  }),
  new Location({
    line: [{functionId: 3, line: 10}],
    id: 3,
  }),
  new Location({
    line: [{functionId: 4, line: 5}],
    id: 4,
  }),
];

export const timeSourceProfile = new Profile({
  sampleType: [
    new ValueType({type: 1, unit: 2}),
    new ValueType({type: 3, unit: 4}),
  ],
  sample: [
    new Sample({
      locationId: [2, 1],
      value: [5, 5000000],
      label: [],
    }),
    new Sample({
      locationId: [4, 3, 1],
      value: [10, 10000000],
      label: [],
    }),
  ],
  location: timeSourceLocations,
  function: timeSourceFunctions,
  stringTable: buildStringTable([
    'sample',
    'count',
    'wall',
    'nanoseconds',
    'foo1',
    path.join(mapDirPath, 'foo.ts'),
    'foo2',
    'bar',
    path.join(mapDirPath, 'bar.js'),
    'baz',
    path.join(mapDirPath, 'baz.ts'),
  ]),
  timeNanos: 0,
  durationNanos: 10 * 1000 * 1000 * 1000,
  periodType: new ValueType({type: 3, unit: 4}),
  period: 1000000,
});

export const labelEncodingProfile = {
  startTime: 0,
  endTime: 10 * 1000 * 1000,
  topDownRoot: {
    name: '(root)',
    scriptName: '(root)',
    scriptId: 10000,
    lineNumber: 0,
    columnNumber: 0,
    hitCount: 0,
    children: [
      {
        name: 'foo1',
        scriptName: 'foo',
        scriptId: 1,
        lineNumber: 1,
        columnNumber: 4,
        hitCount: 1,
        children: [],
        contexts: [
          {
            context: {
              someStr: 'foo',
              someNum: 42,
              someBigint: 18446744073709551557n,
              ignored: {},
            },
          },
        ],
      },
    ],
  },
};

const {hasOwnProperty} = Object.prototype;

export function getAndVerifyPresence(
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  list: any[],
  id: number,
  zeroIndex = false,
) {
  assert.strictEqual(typeof id, 'number', 'has id');
  const index = id - (zeroIndex ? 0 : 1);
  assert.ok(list.length > index, 'exists in list');
  return list[index];
}

export function getAndVerifyString(
  stringTable: StringTable,
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  source: any,
  field: string,
) {
  assert.ok(hasOwnProperty.call(source, field), 'has id field');
  const str = getAndVerifyPresence(
    stringTable.strings,
    source[field] as number,
    true,
  );
  assert.strictEqual(typeof str, 'string', 'is a string');
  return str;
}
```

## File: `ts/test/test-get-value-from-map-profiler.ts`
```typescript
/**
 * Copyright 2025 Datadog, Inc
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * Tests for GetValueFromMap through the TimeProfiler API.
 *
 * These tests verify that GetValueFromMap works correctly in its actual usage context:
 * - The profiler creates a key object (AsyncLocalStorage or internal key)
 * - Contexts are stored in the CPED map using that key
 * - GetValueFromMap retrieves contexts using the same key during signal handling
 *
 * This is the real-world usage pattern, and these tests confirm the structure
 * layout and key address extraction work correctly on Node 24.x / V8 13.6.
 */

import assert from 'assert';
import {join} from 'path';
import {AsyncLocalStorage} from 'async_hooks';
import {satisfies} from 'semver';

const findBinding = require('node-gyp-build');
const profiler = findBinding(join(__dirname, '..', '..'));

const useCPED =
  (satisfies(process.versions.node, '>=24.0.0') &&
    !process.execArgv.includes('--no-async-context-frame')) ||
  (satisfies(process.versions.node, '>=22.7.0') &&
    process.execArgv.includes('--experimental-async-context-frame'));

const supportedPlatform =
  process.platform === 'darwin' || process.platform === 'linux';

if (useCPED && supportedPlatform) {
  describe('GetValueFromMap (through TimeProfiler)', () => {
    describe('basic context storage and retrieval', () => {
      it('should store and retrieve a simple object context', () => {
        const als = new AsyncLocalStorage();
        const profiler = createProfiler(als);

        als.enterWith([]);

        const context = {label: 'test-context'};
        profiler.context = context;

        const retrieved = profiler.context;
        assert.strictEqual(
          retrieved,
          context,
          'Should retrieve the same object',
        );

        profiler.dispose();
      });

      it('should store and retrieve context with multiple properties', () => {
        const als = new AsyncLocalStorage();
        const profiler = createProfiler(als);

        als.enterWith([]);

        const context = {
          spanId: '1234567890',
          traceId: 'abcdef123456',
          operation: 'test-operation',
          resource: '/api/endpoint',
          tags: {environment: 'test', version: '1.0'},
        };

        profiler.context = context;
        const retrieved = profiler.context;

        assert.deepStrictEqual(retrieved, context);
        assert.strictEqual(retrieved.spanId, context.spanId);
        assert.strictEqual(retrieved.traceId, context.traceId);
        assert.deepStrictEqual(retrieved.tags, context.tags);

        profiler.dispose();
      });

      it('should handle context updates', () => {
        const als = new AsyncLocalStorage();
        const profiler = createProfiler(als);

        als.enterWith([]);

        const context1 = {label: 'first'};
        profiler.context = context1;
        assert.strictEqual(profiler.context, context1);

        const context2 = {label: 'second'};
        profiler.context = context2;
        assert.strictEqual(profiler.context, context2);

        const context3 = {label: 'third', extra: 'data'};
        profiler.context = context3;
        assert.strictEqual(profiler.context, context3);

        profiler.dispose();
      });

      it('should return undefined for undefined context', () => {
        const als = new AsyncLocalStorage();
        const profiler = createProfiler(als);

        als.enterWith([]);

        profiler.context = undefined;
        const retrieved = profiler.context;

        assert.strictEqual(retrieved, undefined);

        profiler.dispose();
      });

      it('should work with createContextHolder pattern', () => {
        // This tests the pattern used by runWithContext where
        // createContextHolder creates a wrap object that's stored in CPED map

        const als = new AsyncLocalStorage();
        const profiler = createProfiler(als);

        const context = {label: 'wrapped-context', id: 999};

        // Using als.run mimics what runWithContext does internally
        als.run(profiler.createContextHolder(context), () => {
          const retrieved = profiler.context;

          // The wrap object stores context at index 0
          assert.ok(retrieved !== null && typeof retrieved === 'object');
          assert.deepStrictEqual(retrieved, context);
        });

        profiler.dispose();
      });
    });

    describe('multiple context frames', () => {
      it('should isolate contexts in different async frames', () => {
        const als = new AsyncLocalStorage();
        const profiler = createProfiler(als);

        const context1 = {frame: 'frame1'};
        const context2 = {frame: 'frame2'};

        // Frame 1
        als.run([], () => {
          profiler.context = context1;
          assert.deepStrictEqual(profiler.context, context1);
        });

        // Frame 2
        als.run([], () => {
          assert.strictEqual(profiler.context, undefined);
          profiler.context = context2;
          assert.deepStrictEqual(profiler.context, context2);
        });

        // Outside frames
        assert.strictEqual(profiler.context, undefined);

        profiler.dispose();
      });

      it('should handle nested async frames', () => {
        const als = new AsyncLocalStorage();
        const profiler = createProfiler(als);

        const outerContext = {level: 'outer'};
        const innerContext = {level: 'inner'};

        als.run([], () => {
          profiler.context = outerContext;
          assert.deepStrictEqual(profiler.context, outerContext);

          als.run([], () => {
            profiler.context = innerContext;
            assert.deepStrictEqual(profiler.context, innerContext);
          });

          // Back to outer context frame
          assert.deepStrictEqual(profiler.context, outerContext);
        });

        profiler.dispose();
      });
    });
  });
}

function createProfiler(als: AsyncLocalStorage<unknown>) {
  return new profiler.TimeProfiler({
    intervalMicros: 10000,
    durationMillis: 500,
    withContexts: true,
    useCPED: true,
    CPEDKey: als,
    lineNumbers: false,
    workaroundV8Bug: false,
    collectCpuTime: false,
    collectAsyncId: true,
    isMainThread: true,
  });
}
```

## File: `ts/test/test-heap-profiler.ts`
```typescript
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

import * as sinon from 'sinon';

import * as heapProfiler from '../src/heap-profiler';
import * as v8HeapProfiler from '../src/heap-profiler-bindings';
import {AllocationProfileNode, LabelSet} from '../src/v8-types';
import {fork} from 'child_process';
import path from 'path';
import fs from 'fs';

import {
  heapProfileExcludePath,
  heapProfileIncludePath,
  heapProfileWithExternal,
  v8HeapProfile,
  v8HeapWithPathProfile,
  heapProfileIncludePathWithLabels,
} from './profiles-for-tests';

const copy = require('deep-copy');
const assert = require('assert');

function mapToGetterNode(node: AllocationProfileNode): AllocationProfileNode {
  const children = (node.children || []).map(mapToGetterNode);
  const allocations = node.allocations || [];
  const result = {};

  Object.defineProperties(result, {
    name: {get: () => node.name},
    scriptName: {get: () => node.scriptName},
    scriptId: {get: () => node.scriptId},
    lineNumber: {get: () => node.lineNumber},
    columnNumber: {get: () => node.columnNumber},
    allocations: {get: () => allocations},
    children: {get: () => children},
  });
  return result as AllocationProfileNode;
}

describe('HeapProfiler', () => {
  let startStub: sinon.SinonStub<[number, number], void>;
  let stopStub: sinon.SinonStub<[], void>;
  let profileStub: sinon.SinonStub<
    [(root: AllocationProfileNode) => unknown],
    unknown
  >;
  let dateStub: sinon.SinonStub<[], number>;
  let memoryUsageStub: sinon.SinonStub<[], NodeJS.MemoryUsage>;
  beforeEach(() => {
    startStub = sinon.stub(v8HeapProfiler, 'startSamplingHeapProfiler');
    stopStub = sinon.stub(v8HeapProfiler, 'stopSamplingHeapProfiler');
    dateStub = sinon.stub(Date, 'now').returns(0);
  });

  afterEach(() => {
    heapProfiler.stop();
    startStub.restore();
    stopStub.restore();
    profileStub.restore();
    dateStub.restore();
    memoryUsageStub.restore();
  });
  describe('profile', () => {
    it('should return a profile equal to the expected profile when external memory is allocated', async () => {
      profileStub = sinon
        .stub(v8HeapProfiler, 'mapAllocationProfile')
        .callsFake(callback => callback(mapToGetterNode(copy(v8HeapProfile))));
      memoryUsageStub = sinon.stub(process, 'memoryUsage').returns({
        external: 1024,
        rss: 2048,
        heapTotal: 4096,
        heapUsed: 2048,
        arrayBuffers: 512,
      });
      const intervalBytes = 1024 * 512;
      const stackDepth = 32;
      heapProfiler.start(intervalBytes, stackDepth);
      const profile = heapProfiler.profile();
      assert.deepEqual(heapProfileWithExternal, profile);
    });

    it('should return a profile equal to the expected profile when including all samples', async () => {
      profileStub = sinon
        .stub(v8HeapProfiler, 'mapAllocationProfile')
        .callsFake(callback =>
          callback(mapToGetterNode(copy(v8HeapWithPathProfile))),
        );
      memoryUsageStub = sinon.stub(process, 'memoryUsage').returns({
        external: 0,
        rss: 2048,
        heapTotal: 4096,
        heapUsed: 2048,
        arrayBuffers: 512,
      });
      const intervalBytes = 1024 * 512;
      const stackDepth = 32;
      heapProfiler.start(intervalBytes, stackDepth);
      const profile = heapProfiler.profile();
      assert.deepEqual(heapProfileIncludePath, profile);
    });

    it('should return a profile equal to the expected profile when excluding profiler samples', async () => {
      profileStub = sinon
        .stub(v8HeapProfiler, 'mapAllocationProfile')
        .callsFake(callback =>
          callback(mapToGetterNode(copy(v8HeapWithPathProfile))),
        );
      memoryUsageStub = sinon.stub(process, 'memoryUsage').returns({
        external: 0,
        rss: 2048,
        heapTotal: 4096,
        heapUsed: 2048,
        arrayBuffers: 512,
      });
      const intervalBytes = 1024 * 512;
      const stackDepth = 32;
      heapProfiler.start(intervalBytes, stackDepth);
      const profile = heapProfiler.profile('@google-cloud/profiler');
      assert.deepEqual(heapProfileExcludePath, profile);
    });

    it('should return a profile equal to the expected profile when adding labels', async () => {
      profileStub = sinon
        .stub(v8HeapProfiler, 'mapAllocationProfile')
        .callsFake(callback =>
          callback(mapToGetterNode(copy(v8HeapWithPathProfile))),
        );
      memoryUsageStub = sinon.stub(process, 'memoryUsage').returns({
        external: 0,
        rss: 2048,
        heapTotal: 4096,
        heapUsed: 2048,
        arrayBuffers: 512,
      });
      const intervalBytes = 1024 * 512;
      const stackDepth = 32;
      heapProfiler.start(intervalBytes, stackDepth);
      const labels: LabelSet = {baz: 'bar'};
      const profile = heapProfiler.profile(undefined, undefined, () => {
        return labels;
      });
      assert.deepEqual(heapProfileIncludePathWithLabels, profile);
    });

    it('should throw error when not started', () => {
      assert.throws(
        () => {
          heapProfiler.profile();
        },
        (err: Error) => {
          return err.message === 'Heap profiler is not enabled.';
        },
      );
    });

    it('should throw error when started then stopped', () => {
      const intervalBytes = 1024 * 512;
      const stackDepth = 32;
      heapProfiler.start(intervalBytes, stackDepth);
      heapProfiler.stop();
      assert.throws(
        () => {
          heapProfiler.profile();
        },
        (err: Error) => {
          return err.message === 'Heap profiler is not enabled.';
        },
      );
    });
  });

  describe('start', () => {
    it('should call startSamplingHeapProfiler', () => {
      const intervalBytes1 = 1024 * 512;
      const stackDepth1 = 32;
      heapProfiler.start(intervalBytes1, stackDepth1);
      assert.ok(
        startStub.calledWith(intervalBytes1, stackDepth1),
        'expected startSamplingHeapProfiler to be called',
      );
    });
    it('should throw error when enabled and started with different parameters', () => {
      const intervalBytes1 = 1024 * 512;
      const stackDepth1 = 32;
      heapProfiler.start(intervalBytes1, stackDepth1);
      assert.ok(
        startStub.calledWith(intervalBytes1, stackDepth1),
        'expected startSamplingHeapProfiler to be called',
      );
      startStub.resetHistory();
      const intervalBytes2 = 1024 * 128;
      const stackDepth2 = 64;
      try {
        heapProfiler.start(intervalBytes2, stackDepth2);
      } catch (e) {
        assert.strictEqual(
          (e as Error).message,
          'Heap profiler is already started  with intervalBytes 524288 and' +
            ' stackDepth 64',
        );
      }
      assert.ok(
        !startStub.called,
        'expected startSamplingHeapProfiler not to be called second time',
      );
    });
  });

  describe('stop', () => {
    it('should not call stopSamplingHeapProfiler if profiler not started', () => {
      heapProfiler.stop();
      assert.ok(!stopStub.called, 'stop() should have been no-op.');
    });
    it('should call stopSamplingHeapProfiler if profiler started', () => {
      heapProfiler.start(1024 * 512, 32);
      heapProfiler.stop();
      assert.ok(
        stopStub.called,
        'expected stopSamplingHeapProfiler to be called',
      );
    });
  });
});

describe('OOMMonitoring', () => {
  it('should call external process upon OOM', async function () {
    // this test is very slow on some configs (asan/valgrind)
    this.timeout(20000);
    const proc = fork(path.join(__dirname, 'oom.js'), {
      execArgv: ['--max-old-space-size=50'],
    });
    const checkFilePath = 'oom_check.log';
    if (fs.existsSync(checkFilePath)) {
      fs.unlinkSync(checkFilePath);
    }
    // wait for proc to exit
    await new Promise<void>((resolve, reject) => {
      proc.on('exit', code => {
        if (code === 0) {
          reject();
        } else {
          resolve();
        }
      });
    });
    assert.equal(fs.readFileSync(checkFilePath), 'ok');
    fs.unlinkSync(checkFilePath);
  });
});
```

## File: `ts/test/test-profile-encoder.ts`
```typescript
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
import {gunzip as gunzipCallback, gunzipSync} from 'zlib';

import {Profile} from 'pprof-format';
import {encode, encodeSync} from '../src/profile-encoder';

import {decodedTimeProfile, timeProfile} from './profiles-for-tests';

const assert = require('assert');
const gunzip = promisify(gunzipCallback);

describe('profile-encoded', () => {
  describe('encode', () => {
    it('should encode profile such that the encoded profile can be decoded', async () => {
      const encoded = await encode(timeProfile);
      const unzipped = await gunzip(encoded);
      const decoded = Profile.decode(unzipped);
      assert.deepEqual(decoded, decodedTimeProfile);
    });
  });
  describe('encodeSync', () => {
    it('should encode profile such that the encoded profile can be decoded', () => {
      const encoded = encodeSync(timeProfile);
      const unzipped = gunzipSync(encoded);
      const decoded = Profile.decode(unzipped);
      assert.deepEqual(decoded, decodedTimeProfile);
    });
  });
});
```

## File: `ts/test/test-profile-serializer.ts`
```typescript
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
import * as sinon from 'sinon';
import * as tmp from 'tmp';

import {
  NON_JS_THREADS_FUNCTION_NAME,
  serializeHeapProfile,
  serializeTimeProfile,
} from '../src/profile-serializer';
import {SourceMapper} from '../src/sourcemapper/sourcemapper';
import {Label, Profile} from 'pprof-format';
import {TimeProfile, TimeProfileNode} from '../src/v8-types';
import {
  anonymousFunctionHeapProfile,
  getAndVerifyPresence,
  getAndVerifyString,
  heapProfile,
  heapSourceProfile,
  labelEncodingProfile,
  mapDirPath,
  timeProfile,
  timeSourceProfile,
  v8AnonymousFunctionHeapProfile,
  v8HeapGeneratedProfile,
  v8HeapProfile,
  v8TimeGeneratedProfile,
  v8TimeProfile,
} from './profiles-for-tests';

const assert = require('assert');

function getNonJSThreadsSample(profile: Profile): number[] | null {
  for (const sample of profile.sample!) {
    const locationId = sample.locationId[0];
    const location = getAndVerifyPresence(
      profile.location!,
      locationId as number,
    );
    const functionId = location.line![0].functionId;
    const fn = getAndVerifyPresence(profile.function!, functionId as number);
    const fn_name = profile.stringTable.strings[fn.name as number];
    if (fn_name === NON_JS_THREADS_FUNCTION_NAME) {
      return sample.value as number[];
    }
  }

  return null;
}

describe('profile-serializer', () => {
  let dateStub: sinon.SinonStub<[], number>;

  before(() => {
    dateStub = sinon.stub(Date, 'now').returns(0);
  });
  after(() => {
    dateStub.restore();
  });

  describe('serializeTimeProfile', () => {
    it('should produce expected profile', () => {
      const timeProfileOut = serializeTimeProfile(v8TimeProfile, 1000);
      assert.deepEqual(timeProfileOut, timeProfile);
    });

    it('should omit non-jS threads CPU time when profile has no CPU time', () => {
      const timeProfile: TimeProfile = {
        startTime: 0,
        endTime: 10 * 1000 * 1000,
        hasCpuTime: false,
        nonJSThreadsCpuTime: 1000,
        topDownRoot: {
          name: '(root)',
          scriptName: 'root',
          scriptId: 0,
          lineNumber: 0,
          columnNumber: 0,
          hitCount: 0,
          children: [],
        },
      };
      const timeProfileOut = serializeTimeProfile(timeProfile, 1000);
      assert.equal(getNonJSThreadsSample(timeProfileOut), null);
      const timeProfileOutWithLabels = serializeTimeProfile(
        timeProfile,
        1000,
        undefined,
        false,
        () => {
          return {foo: 'bar'};
        },
      );
      assert.equal(getNonJSThreadsSample(timeProfileOutWithLabels), null);
    });

    it('should omit non-jS threads CPU time when it is zero', () => {
      const timeProfile: TimeProfile = {
        startTime: 0,
        endTime: 10 * 1000 * 1000,
        hasCpuTime: true,
        nonJSThreadsCpuTime: 0,
        topDownRoot: {
          name: '(root)',
          scriptName: 'root',
          scriptId: 0,
          lineNumber: 0,
          columnNumber: 0,
          hitCount: 0,
          children: [],
        },
      };
      const timeProfileOut = serializeTimeProfile(timeProfile, 1000);
      assert.equal(getNonJSThreadsSample(timeProfileOut), null);
      const timeProfileOutWithLabels = serializeTimeProfile(
        timeProfile,
        1000,
        undefined,
        false,
        () => {
          return {foo: 'bar'};
        },
      );
      assert.equal(getNonJSThreadsSample(timeProfileOutWithLabels), null);
    });

    it('should produce Non-JS thread sample with zero wall time', () => {
      const timeProfile: TimeProfile = {
        startTime: 0,
        endTime: 10 * 1000 * 1000,
        hasCpuTime: true,
        nonJSThreadsCpuTime: 1000,
        topDownRoot: {
          name: '(root)',
          scriptName: 'root',
          scriptId: 0,
          lineNumber: 0,
          columnNumber: 0,
          hitCount: 0,
          children: [],
        },
      };
      const timeProfileOut = serializeTimeProfile(timeProfile, 1000);
      const values = getNonJSThreadsSample(timeProfileOut);
      assert.notEqual(values, null);
      assert.equal(values![0], 0);
      assert.equal(values![1], 0);
      assert.equal(values![2], 1000);
      const timeProfileOutWithLabels = serializeTimeProfile(
        timeProfile,
        1000,
        undefined,
        false,
        () => {
          return {foo: 'bar'};
        },
      );
      const valuesWithLabels = getNonJSThreadsSample(timeProfileOutWithLabels);
      assert.notEqual(valuesWithLabels, null);
      assert.equal(valuesWithLabels![0], 0);
      assert.equal(valuesWithLabels![1], 0);
      assert.equal(valuesWithLabels![2], 1000);
    });
  });

  describe('label builder', () => {
    it('should accept strings, numbers, and bigints', () => {
      const profileOut = serializeTimeProfile(labelEncodingProfile, 1000);
      const st = profileOut.stringTable;
      assert.deepEqual(profileOut.sample[0].label, [
        new Label({key: st.dedup('someStr'), str: st.dedup('foo')}),
        new Label({key: st.dedup('someNum'), num: 42}),
        new Label({key: st.dedup('someBigint'), num: 18446744073709551557n}),
      ]);
    });
  });

  describe('serializeHeapProfile', () => {
    it('should produce expected profile', () => {
      const heapProfileOut = serializeHeapProfile(v8HeapProfile, 0, 512 * 1024);
      assert.deepEqual(heapProfileOut, heapProfile);
    });
    it('should produce expected profile when there is anonymous function', () => {
      const heapProfileOut = serializeHeapProfile(
        v8AnonymousFunctionHeapProfile,
        0,
        512 * 1024,
      );
      assert.deepEqual(heapProfileOut, anonymousFunctionHeapProfile);
    });
  });

  describe('source map specified', () => {
    let sourceMapper: SourceMapper;
    before(async () => {
      sourceMapper = await SourceMapper.create([mapDirPath]);
    });

    describe('serializeHeapProfile', () => {
      it('should produce expected profile', () => {
        const heapProfileOut = serializeHeapProfile(
          v8HeapGeneratedProfile,
          0,
          512 * 1024,
          undefined,
          sourceMapper,
        );
        assert.deepEqual(heapProfileOut, heapSourceProfile);
      });
    });

    describe('serializeTimeProfile', () => {
      it('should produce expected profile', () => {
        const timeProfileOut = serializeTimeProfile(
          v8TimeGeneratedProfile,
          1000,
          sourceMapper,
        );
        assert.deepEqual(timeProfileOut, timeSourceProfile);
      });
    });

    after(() => {
      tmp.setGracefulCleanup();
    });
  });

  describe('missing source map file reporting', () => {
    let sourceMapper: SourceMapper;
    let missingJsPath: string;

    before(async () => {
      const fs = await import('fs');
      const path = await import('path');
      const testDir = tmp.dirSync().name;
      missingJsPath = path.join(testDir, 'missing-map.js');
      // JS file that declares a sourceMappingURL but the map file doesn't exist.
      fs.writeFileSync(
        missingJsPath,
        '//# sourceMappingURL=nonexistent.js.map\n',
      );
      sourceMapper = await SourceMapper.create([testDir]);
    });

    function makeSingleNodeTimeProfile(scriptName: string) {
      return {
        startTime: 0,
        endTime: 1000000,
        topDownRoot: {
          name: '(root)',
          scriptName: 'root',
          scriptId: 0,
          lineNumber: 0,
          columnNumber: 0,
          hitCount: 0,
          children: [
            {
              name: 'foo',
              scriptName,
              scriptId: 1,
              lineNumber: 1,
              columnNumber: 1,
              hitCount: 1,
              children: [],
            },
          ],
        },
      };
    }

    function assertHasMissingMapToken(profile: Profile) {
      const st = profile.stringTable;
      const tokenId = st.dedup('dd:has-missing-map-files');
      const comments = profile.comment as number[];
      assert.ok(
        Array.isArray(comments) && comments.includes(tokenId),
        'expected dd:has-missing-map-files token in profile comments',
      );
    }

    it('serializeTimeProfile emits missing-map token when a map is declared but absent', () => {
      const profile = serializeTimeProfile(
        makeSingleNodeTimeProfile(missingJsPath),
        1000,
        sourceMapper,
      );
      assertHasMissingMapToken(profile);
    });

    it('serializeHeapProfile emits missing-map token when a map is declared but absent', () => {
      // serialize() iterates root.children, so the node with allocations must
      // be a child of the root passed to serializeHeapProfile.
      const heapNode = {
        name: '(root)',
        scriptName: '',
        scriptId: 0,
        lineNumber: 0,
        columnNumber: 0,
        allocations: [],
        children: [
          {
            name: 'foo',
            scriptName: missingJsPath,
            scriptId: 1,
            lineNumber: 1,
            columnNumber: 1,
            allocations: [{sizeBytes: 100, count: 1}],
            children: [],
          },
        ],
      };
      const profile = serializeHeapProfile(
        heapNode,
        0,
        512 * 1024,
        undefined,
        sourceMapper,
      );
      assertHasMissingMapToken(profile);
    });

    it('does not emit missing-map token when no source mapper is used', () => {
      const profile = serializeTimeProfile(
        makeSingleNodeTimeProfile(missingJsPath),
        1000,
      );
      assert.ok(
        !profile.comment || profile.comment.length === 0,
        'expected no comments when no source mapper is provided',
      );
    });

    it('does not emit missing-map token when all maps are found', () => {
      const {
        mapDirPath,
        v8TimeGeneratedProfile,
      } = require('./profiles-for-tests');
      return SourceMapper.create([mapDirPath]).then(sm => {
        const profile = serializeTimeProfile(v8TimeGeneratedProfile, 1000, sm);
        assert.ok(
          !profile.comment || profile.comment.length === 0,
          'expected no comments when all maps are resolved',
        );
      });
    });

    after(() => {
      tmp.setGracefulCleanup();
    });
  });

  describe('source map with column 0 (LineTick simulation)', () => {
    // This tests the LEAST_UPPER_BOUND fallback for when V8's LineTick
    // doesn't provide column information (column=0)
    let sourceMapper: SourceMapper;
    let testMapDir: string;

    // Line in source.ts that the first call maps to (column 10)
    const FIRST_CALL_SOURCE_LINE = 100;
    // Line in source.ts that the second call maps to (column 25)
    const SECOND_CALL_SOURCE_LINE = 200;

    before(async () => {
      // Create a source map simulating: return fib(n-1) + fib(n-2)
      // Same function called twice on the same line at different columns
      testMapDir = tmp.dirSync().name;
      const {SourceMapGenerator} = await import('source-map');
      const fs = await import('fs');
      const path = await import('path');

      const mapGen = new SourceMapGenerator({file: 'generated.js'});

      // First fib() call at column 10 -> maps to source line 100
      mapGen.addMapping({
        source: path.join(testMapDir, 'source.ts'),
        name: 'fib',
        generated: {line: 5, column: 10},
        original: {line: FIRST_CALL_SOURCE_LINE, column: 0},
      });

      // Second fib() call at column 25 -> maps to source line 200
      mapGen.addMapping({
        source: path.join(testMapDir, 'source.ts'),
        name: 'fib',
        generated: {line: 5, column: 25},
        original: {line: SECOND_CALL_SOURCE_LINE, column: 0},
      });

      fs.writeFileSync(
        path.join(testMapDir, 'generated.js.map'),
        mapGen.toString(),
      );
      fs.writeFileSync(path.join(testMapDir, 'generated.js'), '');

      sourceMapper = await SourceMapper.create([testMapDir]);
    });

    it('should map column 0 to first mapping on line (LEAST_UPPER_BOUND fallback)', () => {
      const path = require('path');
      // Simulate LineTick entry with column=0 (no column info from V8 < 14)
      // This is the fallback behavior when LineTick.column is not available
      const childNode: TimeProfileNode = {
        name: 'fib',
        scriptName: path.join(testMapDir, 'generated.js'),
        scriptId: 1,
        lineNumber: 5,
        columnNumber: 0, // LineTick has no column in V8 < 14
        hitCount: 1,
        children: [],
      };
      const v8Profile: TimeProfile = {
        startTime: 0,
        endTime: 1000000,
        topDownRoot: {
          name: '(root)',
          scriptName: 'root',
          scriptId: 0,
          lineNumber: 0,
          columnNumber: 0,
          hitCount: 0,
          children: [childNode],
        },
      };

      const profile = serializeTimeProfile(v8Profile, 1000, sourceMapper);

      assert.strictEqual(profile.location!.length, 1);
      const loc = profile.location![0];
      const line = loc.line![0];
      const func = getAndVerifyPresence(
        profile.function!,
        line.functionId as number,
      );
      const filename = getAndVerifyString(
        profile.stringTable,
        func,
        'filename',
      );

      // Should be mapped to source.ts
      assert.ok(
        filename.includes('source.ts'),
        `Expected source.ts but got ${filename}`,
      );
      // With column 0 and LEAST_UPPER_BOUND, should map to FIRST mapping (line 100)
      assert.strictEqual(
        line.line,
        FIRST_CALL_SOURCE_LINE,
        'Column 0 should use LEAST_UPPER_BOUND to find first mapping on line',
      );
    });

    it('should map to second call when column points to it (V8 14+ with LineTick.column)', () => {
      const path = require('path');
      // Simulate V8 14+ behavior where LineTick has actual column data
      // Column 26 is after the second mapping at column 25
      const childNode: TimeProfileNode = {
        name: 'fib',
        scriptName: path.join(testMapDir, 'generated.js'),
        scriptId: 1,
        lineNumber: 5,
        columnNumber: 26, // V8 14+ provides actual column from LineTick
        hitCount: 1,
        children: [],
      };
      const v8Profile: TimeProfile = {
        startTime: 0,
        endTime: 1000000,
        topDownRoot: {
          name: '(root)',
          scriptName: 'root',
          scriptId: 0,
          lineNumber: 0,
          columnNumber: 0,
          hitCount: 0,
          children: [childNode],
        },
      };

      const profile = serializeTimeProfile(v8Profile, 1000, sourceMapper);

      assert.strictEqual(profile.location!.length, 1);
      const loc = profile.location![0];
      const line = loc.line![0];

      // Column 26 with GREATEST_LOWER_BOUND should map to second call (line 200)
      assert.strictEqual(
        line.line,
        SECOND_CALL_SOURCE_LINE,
        'Column 26 should use GREATEST_LOWER_BOUND to find mapping at column 25',
      );
    });

    it('should map to first call when column points to it (V8 14+ with LineTick.column)', () => {
      const path = require('path');
      // Simulate V8 14+ behavior where LineTick has actual column data
      // Column 11 is after the first mapping at column 10 but before second at 25
      const childNode: TimeProfileNode = {
        name: 'fib',
        scriptName: path.join(testMapDir, 'generated.js'),
        scriptId: 1,
        lineNumber: 5,
        columnNumber: 11, // V8 14+ provides actual column from LineTick
        hitCount: 1,
        children: [],
      };
      const v8Profile: TimeProfile = {
        startTime: 0,
        endTime: 1000000,
        topDownRoot: {
          name: '(root)',
          scriptName: 'root',
          scriptId: 0,
          lineNumber: 0,
          columnNumber: 0,
          hitCount: 0,
          children: [childNode],
        },
      };

      const profile = serializeTimeProfile(v8Profile, 1000, sourceMapper);

      assert.strictEqual(profile.location!.length, 1);
      const loc = profile.location![0];
      const line = loc.line![0];

      // Column 11 with GREATEST_LOWER_BOUND should map to first call (line 100)
      assert.strictEqual(
        line.line,
        FIRST_CALL_SOURCE_LINE,
        'Column 11 should use GREATEST_LOWER_BOUND to find mapping at column 10',
      );
    });
  });
});
```

## File: `ts/test/test-sourcemapper.ts`
```typescript
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
import * as assert from 'assert';
import * as fs from 'fs';
import * as path from 'path';
import * as tmp from 'tmp';

import {
  ANNOTATION_TAIL_BYTES,
  SourceMapper,
  extractSourceMappingURL,
  readSourceMappingURL,
} from '../src/sourcemapper/sourcemapper';

describe('extractSourceMappingURL', () => {
  it('returns URL from a standard annotation', () => {
    assert.strictEqual(
      extractSourceMappingURL('//# sourceMappingURL=foo.js.map\n'),
      'foo.js.map',
    );
  });

  it('accepts legacy //@ prefix', () => {
    assert.strictEqual(
      extractSourceMappingURL('//@ sourceMappingURL=foo.js.map\n'),
      'foo.js.map',
    );
  });

  it('skips trailing empty and whitespace-only lines', () => {
    assert.strictEqual(
      extractSourceMappingURL('//# sourceMappingURL=foo.js.map\n\n   \n'),
      'foo.js.map',
    );
  });

  it('allows leading whitespace before //', () => {
    assert.strictEqual(
      extractSourceMappingURL('   //# sourceMappingURL=foo.js.map\n'),
      'foo.js.map',
    );
  });

  it('returns undefined when last non-empty line has no // comment', () => {
    assert.strictEqual(extractSourceMappingURL('const x = 1;\n'), undefined);
  });

  it('returns undefined when // comment does not match annotation pattern', () => {
    assert.strictEqual(
      extractSourceMappingURL('// some other comment\n'),
      undefined,
    );
  });

  it('returns undefined (early exit) when last non-empty line is not an annotation, even if earlier lines are', () => {
    // The annotation must be on the last non-empty line; earlier ones are ignored.
    assert.strictEqual(
      extractSourceMappingURL(
        '//# sourceMappingURL=foo.js.map\nconst x = 1;\n',
      ),
      undefined,
    );
  });

  it('returns undefined when comment contains a double-quote', () => {
    assert.strictEqual(
      extractSourceMappingURL('//# sourceMappingURL="foo.js.map"\n'),
      undefined,
    );
  });

  it('returns undefined when comment contains a single-quote', () => {
    assert.strictEqual(
      extractSourceMappingURL("//# sourceMappingURL='foo.js.map'\n"),
      undefined,
    );
  });

  it('returns undefined when comment contains a backtick', () => {
    assert.strictEqual(
      extractSourceMappingURL('//# sourceMappingURL=`foo.js.map`\n'),
      undefined,
    );
  });

  it('returns undefined for empty content', () => {
    assert.strictEqual(extractSourceMappingURL(''), undefined);
  });

  it('returns undefined for whitespace-only content', () => {
    assert.strictEqual(extractSourceMappingURL('   \n\n   \n'), undefined);
  });

  it('handles all line terminator variants', () => {
    assert.strictEqual(
      extractSourceMappingURL('x\r//# sourceMappingURL=a.map'),
      'a.map',
    );
    assert.strictEqual(
      extractSourceMappingURL('x\r\n//# sourceMappingURL=b.map'),
      'b.map',
    );
    assert.strictEqual(
      extractSourceMappingURL('x\u2028//# sourceMappingURL=c.map'),
      'c.map',
    );
    assert.strictEqual(
      extractSourceMappingURL('x\u2029//# sourceMappingURL=d.map'),
      'd.map',
    );
  });

  it('returns a data: URL for inline source maps', () => {
    const map = Buffer.from('{"mappings":""}').toString('base64');
    const url = `data:application/json;base64,${map}`;
    assert.strictEqual(
      extractSourceMappingURL(`//# sourceMappingURL=${url}\n`),
      url,
    );
  });
});

describe('readSourceMappingURL', () => {
  let tmpDir: string;

  before(() => {
    tmp.setGracefulCleanup();
    tmpDir = tmp.dirSync().name;
  });

  function write(name: string, content: string): string {
    const p = path.join(tmpDir, name);
    fs.writeFileSync(p, content, 'utf8');
    return p;
  }

  // Build a fake base64 payload larger than ANNOTATION_TAIL_BYTES to force
  // the "last non-empty line extends before the tail window" scenario.
  const LARGE_BASE64 = 'A'.repeat(ANNOTATION_TAIL_BYTES + 128);
  const LARGE_ANNOTATION = `//# sourceMappingURL=data:application/json;base64,${LARGE_BASE64}`;

  it('reads external URL from a small file (fits entirely in tail)', async () => {
    const p = write('ext-small.js', '//# sourceMappingURL=ext-small.js.map\n');
    assert.strictEqual(await readSourceMappingURL(p), 'ext-small.js.map');
  });

  it('reads inline data: URL from a small file (fits entirely in tail)', async () => {
    const map = Buffer.from('{"mappings":""}').toString('base64');
    const url = `data:application/json;base64,${map}`;
    const p = write('inline-small.js', `//# sourceMappingURL=${url}\n`);
    assert.strictEqual(await readSourceMappingURL(p), url);
  });

  it('returns undefined for a small file with no annotation', async () => {
    const p = write('no-annotation.js', 'const x = 1;\n');
    assert.strictEqual(await readSourceMappingURL(p), undefined);
  });

  it('reads external URL from a large file (last line short, captured in tail)', async () => {
    // Pad the file so the total size exceeds ANNOTATION_TAIL_BYTES, but keep
    // the annotation line itself short so it fits within the tail.
    const padding = '//' + ' '.repeat(ANNOTATION_TAIL_BYTES) + '\n';
    const p = write(
      'ext-large.js',
      padding + '//# sourceMappingURL=ext-large.js.map\n',
    );
    assert.strictEqual(await readSourceMappingURL(p), 'ext-large.js.map');
  });

  it('reads large inline data: URL — no trailing newline (full-file fallback)', async () => {
    // The annotation line is longer than ANNOTATION_TAIL_BYTES with no
    // trailing newline, so the tail contains no line terminator → fallback.
    const p = write('inline-large-no-nl.js', LARGE_ANNOTATION);
    assert.strictEqual(
      await readSourceMappingURL(p),
      `data:application/json;base64,${LARGE_BASE64}`,
    );
  });

  it('reads large inline data: URL — single trailing newline (full-file fallback)', async () => {
    // tail = "<end of base64>\n" → lastNonEmptyIdx === 0 → fallback.
    const p = write('inline-large-one-nl.js', LARGE_ANNOTATION + '\n');
    assert.strictEqual(
      await readSourceMappingURL(p),
      `data:application/json;base64,${LARGE_BASE64}`,
    );
  });

  it('reads large inline data: URL — multiple trailing empty lines (full-file fallback)', async () => {
    // The bug case: tail = "<end of base64>\n\n" has line terminators but
    // lastNonEmptyIdx === 0, so we must not use the tail alone.
    const p = write('inline-large-multi-nl.js', LARGE_ANNOTATION + '\n\n\n');
    assert.strictEqual(
      await readSourceMappingURL(p),
      `data:application/json;base64,${LARGE_BASE64}`,
    );
  });

  it('returns undefined for a large file with no annotation', async () => {
    const padding = 'x'.repeat(ANNOTATION_TAIL_BYTES + 1) + '\n';
    const p = write('large-no-annotation.js', padding + 'const x = 1;\n');
    assert.strictEqual(await readSourceMappingURL(p), undefined);
  });

  it('returns undefined for an empty file', async () => {
    const p = write('empty.js', '');
    assert.strictEqual(await readSourceMappingURL(p), undefined);
  });
});

describe('SourceMapper.loadDirectory', () => {
  let tmpDir: string;

  before(() => {
    tmp.setGracefulCleanup();
    tmpDir = tmp.dirSync().name;
  });

  function write(name: string, content: string): string {
    const p = path.join(tmpDir, name);
    fs.writeFileSync(p, content, 'utf8');
    return p;
  }

  // A minimal valid source map for test.js -> test.ts
  const MAP_CONTENT = JSON.stringify({
    version: 3,
    file: 'test.js',
    sources: ['test.ts'],
    names: [],
    mappings: 'AAAA',
  });

  it('falls back to .map file when sourceMappingURL points to a non-existent file', async () => {
    // The annotation references a file that doesn't exist; Phase 2 should
    // find and load the conventional test.js.map instead.
    write('test.js', '//# sourceMappingURL=nonexistent.js.map\n');
    write('test.js.map', MAP_CONTENT);

    const sm = new SourceMapper();
    await sm.loadDirectory(tmpDir);

    assert.ok(
      sm.hasMappingInfo(path.join(tmpDir, 'test.js')),
      'expected mapping to be loaded via .map file fallback',
    );
  });

  it('loads no mapping when sourceMappingURL points to a non-existent file and there is no .map fallback', async () => {
    write('orphan.js', '//# sourceMappingURL=nonexistent.js.map\n');
    // No orphan.js.map written — nothing to fall back to.

    const sm = new SourceMapper();
    await sm.loadDirectory(tmpDir);

    assert.ok(
      !sm.hasMappingInfo(path.join(tmpDir, 'orphan.js')),
      'expected no mapping to be loaded',
    );
  });

  it('sets missingMapFile=true when sourceMappingURL declares a missing map', async () => {
    write('declared-missing.js', '//# sourceMappingURL=nonexistent.js.map\n');
    // No declared-missing.js.map written — nothing to fall back to.

    const sm = new SourceMapper();
    await sm.loadDirectory(tmpDir);

    const jsPath = path.join(tmpDir, 'declared-missing.js');
    const loc = sm.mappingInfo({file: jsPath, line: 1, column: 0, name: 'foo'});
    assert.strictEqual(
      loc.missingMapFile,
      true,
      'expected missingMapFile to be true for a file with a declared but missing map',
    );
  });

  it('does not set missingMapFile when file has no sourceMappingURL', async () => {
    write('plain.js', 'console.log("hello");\n');

    const sm = new SourceMapper();
    await sm.loadDirectory(tmpDir);

    const jsPath = path.join(tmpDir, 'plain.js');
    const loc = sm.mappingInfo({file: jsPath, line: 1, column: 0, name: 'foo'});
    assert.ok(
      !loc.missingMapFile,
      'expected missingMapFile to be falsy for a file with no sourceMappingURL',
    );
  });

  it('does not set missingMapFile for an inline data: URL with charset parameter', async () => {
    // data:application/json;charset=utf-8;base64,... is a valid inline form but
    // does not match the old exact INLINE_PREFIX. It must not be treated as a
    // file path and must not produce a false missingMapFile signal.
    const mapJson = JSON.stringify({
      version: 3,
      file: 'charset.js',
      sources: ['charset.ts'],
      names: [],
      mappings: 'AAAA',
    });
    const b64 = Buffer.from(mapJson).toString('base64');
    const url = `data:application/json;charset=utf-8;base64,${b64}`;
    write('charset.js', `//# sourceMappingURL=${url}\n`);

    const sm = new SourceMapper();
    await sm.loadDirectory(tmpDir);

    const jsPath = path.join(tmpDir, 'charset.js');
    assert.ok(
      sm.hasMappingInfo(jsPath),
      'expected mapping to be loaded from charset data: URL',
    );
    assert.ok(
      !sm.mappingInfo({file: jsPath, line: 1, column: 0, name: 'f'})
        .missingMapFile,
      'expected missingMapFile to be falsy for an inline charset data: URL',
    );
  });

  it('does not set missingMapFile when map was found via .map fallback', async () => {
    // JS with annotation pointing to nonexistent path, but a .map file exists
    // alongside it (Phase 2 fallback).
    const {SourceMapGenerator} = await import('source-map');
    const gen = new SourceMapGenerator({file: 'fallback.js'});
    gen.addMapping({
      source: path.join(tmpDir, 'source.ts'),
      generated: {line: 1, column: 0},
      original: {line: 10, column: 0},
    });
    write('fallback.js', '//# sourceMappingURL=nowhere.js.map\n');
    write('fallback.js.map', gen.toString());

    const sm = new SourceMapper();
    await sm.loadDirectory(tmpDir);

    const jsPath = path.join(tmpDir, 'fallback.js');
    const loc = sm.mappingInfo({file: jsPath, line: 1, column: 0, name: 'foo'});
    assert.ok(
      !loc.missingMapFile,
      'expected missingMapFile to be falsy when map was found via Phase 2 fallback',
    );
  });
});
```

## File: `ts/test/test-time-profiler.ts`
```typescript
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

import * as sinon from 'sinon';
import {time, getNativeThreadId} from '../src';
import {stop} from '../src/time-profiler';
import * as v8TimeProfiler from '../src/time-profiler-bindings';
import {timeProfile, v8TimeProfile} from './profiles-for-tests';
import {hrtime} from 'process';
import {Label, Profile} from 'pprof-format';
import {AssertionError} from 'assert';
import {GenerateTimeLabelsArgs, LabelSet} from '../src/v8-types';
import {satisfies} from 'semver';
import {setTimeout as setTimeoutPromise} from 'timers/promises';

import assert from 'assert';

const useCPED =
  (satisfies(process.versions.node, '>=24.0.0') &&
    !process.execArgv.includes('--no-async-context-frame')) ||
  (satisfies(process.versions.node, '>=22.7.0') &&
    process.execArgv.includes('--experimental-async-context-frame'));

const collectAsyncId = satisfies(process.versions.node, '>=24.0.0');

const unsupportedPlatform =
  process.platform !== 'darwin' && process.platform !== 'linux';
const shouldSkipCPEDTests = !useCPED || unsupportedPlatform;

const PROFILE_OPTIONS = {
  durationMillis: 500,
  intervalMicros: 1000,
};

describe('Time Profiler', () => {
  describe('profile', () => {
    it('should exclude program and idle time', async () => {
      const profile = await time.profile(PROFILE_OPTIONS);
      assert.ok(profile.stringTable);
      assert.equal(profile.stringTable.strings!.indexOf('(program)'), -1);
    });

    it('should update state', function shouldUpdateState() {
      if (unsupportedPlatform) {
        this.skip();
      }
      const startTime = BigInt(Date.now()) * 1000n;
      time.start({
        intervalMicros: 20 * 1_000,
        durationMillis: PROFILE_OPTIONS.durationMillis,
        withContexts: true,
        lineNumbers: false,
        useCPED,
      });
      const initialContext: {[key: string]: string} = {};
      time.setContext(initialContext);
      const kSampleCount = time.constants.kSampleCount;
      const state = time.getState();
      assert.equal(state[kSampleCount], 0, 'Initial state should be 0');
      const deadline = Date.now() + 1000;
      while (state[kSampleCount] === 0) {
        if (Date.now() > deadline) {
          assert.fail('State did not change');
        }
      }
      assert(state[kSampleCount] >= 1, 'Unexpected number of samples');

      let checked = false;
      initialContext['aaa'] = 'bbb';

      let endTime = 0n;
      time.stop(false, ({node, context}: GenerateTimeLabelsArgs) => {
        if (node.name === time.constants.NON_JS_THREADS_FUNCTION_NAME) {
          return {};
        }
        assert.ok(context !== null, 'Context should not be null');
        if (!endTime) {
          endTime = BigInt(Date.now()) * 1000n;
        }

        assert.deepEqual(
          context!.context,
          initialContext,
          'Unexpected context',
        );

        assert.ok(context!.timestamp >= startTime);
        assert.ok(context!.timestamp <= endTime);
        checked = true;
        return {...context!.context};
      });
      assert(checked, 'No context found');
    });

    it('should have labels', function shouldHaveLabels() {
      if (unsupportedPlatform) {
        this.skip();
      }
      this.timeout(3000);

      const intervalNanos = PROFILE_OPTIONS.intervalMicros * 1_000;
      time.start({
        intervalMicros: PROFILE_OPTIONS.intervalMicros,
        durationMillis: PROFILE_OPTIONS.durationMillis,
        withContexts: true,
        collectAsyncId: collectAsyncId,
        lineNumbers: false,
        useCPED,
      });
      // By repeating the test few times, we also exercise the profiler
      // start-stop overlap behavior.
      const repeats = 3;
      const rootSpanId = '1234';
      const endPointLabel = 'trace endpoint';
      const rootSpanIdLabel = 'local root span id';
      const asyncIdLabel = 'async id';
      const endPoint = 'foo';
      let enableEndPoint = false;
      const label0 = {label: 'value0'};
      const label1 = {label: 'value1', [rootSpanIdLabel]: rootSpanId};

      for (let i = 0; i < repeats; ++i) {
        loop();
        enableEndPoint = i % 2 === 0;
        validateProfile(
          time.stop(
            i < repeats - 1,
            enableEndPoint || collectAsyncId ? generateLabels : undefined,
          ),
        );
      }

      function generateLabels({context}: GenerateTimeLabelsArgs) {
        if (!context) {
          return {};
        }
        const labels: LabelSet = {};
        if (typeof context.asyncId !== 'undefined') {
          assert(collectAsyncId);
          labels[asyncIdLabel] = context.asyncId;
        }
        for (const [key, value] of Object.entries(context.context ?? {})) {
          if (typeof value === 'string') {
            labels[key] = value;
            if (
              enableEndPoint &&
              key === rootSpanIdLabel &&
              value === rootSpanId
            ) {
              labels[endPointLabel] = endPoint;
            }
          }
        }
        return labels;
      }

      // Each of fn0, fn1, fn2 loops busily for one or two profiling intervals.
      // fn0 resets the label; fn1 and fn2 don't. Label for fn1
      // is reset in the loop. This ensures the following invariants that we
      // test for:
      // label0 can be observed in loop or fn0
      // label1 can be observed in loop or fn1
      // fn0 might be observed with no label
      // fn1 must always be observed with label1
      // fn2 must never be observed with a label
      function fn0() {
        const start = hrtime.bigint();
        while (hrtime.bigint() - start < intervalNanos);
        time.setContext(undefined);
        // With node 22, many deopt events are generated by `setContext` call above.
        // On MacOS, `v8::TimeTicks::Now` has a resolution of ~42us because
        // `mach_absolute_time` ticks (a tick is ~42ns) conversion to microseconds
        // is done in such a way that drops the 3 least significant digits
        // (https://github.com/nodejs/node/blob/v22.x/deps/v8/src/base/platform/time.cc#L745-L746).
        // This two facts lead to samples having identical timestamps, and
        // incorrectly matched contexts.
        // Workaround here just ensures that after deopt event caused by `setContext`,
        // no sample in `fn1` is immediately taken.
        const start2 = hrtime.bigint();
        while (hrtime.bigint() - start2 < intervalNanos);
      }

      function fn1() {
        const start = hrtime.bigint();
        while (hrtime.bigint() - start < intervalNanos);
      }

      function fn2() {
        const start = hrtime.bigint();
        while (hrtime.bigint() - start < intervalNanos);
      }

      function loop() {
        const durationNanos = PROFILE_OPTIONS.durationMillis * 1_000_000;
        const start = hrtime.bigint();
        while (hrtime.bigint() - start < durationNanos) {
          time.setContext(label0);
          fn0();
          time.setContext(label1);
          fn1();
          time.setContext(undefined);
          fn2();
        }
      }

      function validateProfile(profile: Profile) {
        // Get string table indices for strings we're interested in
        const stringTable = profile.stringTable;
        const [
          loopIdx,
          fn0Idx,
          fn1Idx,
          fn2Idx,
          hrtimeBigIntIdx,
          asyncIdLabelIdx,
        ] = ['loop', 'fn0', 'fn1', 'fn2', 'hrtimeBigInt', asyncIdLabel].map(x =>
          stringTable.dedup(x),
        );

        function getString(n: number | bigint): string {
          if (typeof n === 'number') {
            return stringTable.strings[n];
          }
          throw new AssertionError({message: 'Expected a number'});
        }

        function labelIs(l: Label, key: string, str: string) {
          return getString(l.key) === key && getString(l.str) === str;
        }

        function idx(n: number | bigint): number {
          if (typeof n === 'number') {
            // We want a 0-based array index, but IDs start from 1.
            return n - 1;
          }
          throw new AssertionError({message: 'Expected a number'});
        }

        function labelStr(label: Label) {
          return label
            ? `${getString(label.key)}=${getString(label.str)}`
            : 'undefined';
        }

        function getLabels(labels: Label[]) {
          const labelObj: {[key: string]: string} = {};
          labels.forEach(label => {
            labelObj[getString(label.key)] = getString(label.str);
          });
          return labelObj;
        }

        let fn0ObservedWithLabel0 = false;
        let fn1ObservedWithLabel1 = false;
        let fn2ObservedWithoutLabels = false;
        let observedAsyncId = false;
        profile.sample.forEach(sample => {
          let fnName;
          for (const locationId of sample.locationId) {
            const locIdx = idx(locationId);
            const loc = profile.location[locIdx];
            const fnIdx = idx(loc.line[0].functionId);
            const fn = profile.function[fnIdx];
            fnName = fn.name;
            if (fnName !== hrtimeBigIntIdx) {
              break;
            }
          }
          const labels = sample.label;
          if (collectAsyncId) {
            const idx = labels.findIndex(
              label => label.key === asyncIdLabelIdx,
            );
            if (idx !== -1) {
              // Remove async ID label so it doesn't confuse the assertions on
              // labels further below.
              labels.splice(idx, 1);
              observedAsyncId = true;
            }
          }
          switch (fnName) {
            case loopIdx:
              if (enableEndPoint) {
                assert(
                  labels.length < 4,
                  'loop can have at most two labels and one endpoint',
                );
                labels.forEach(label => {
                  assert(
                    labelIs(label, 'label', 'value0') ||
                      labelIs(label, 'label', 'value1') ||
                      labelIs(label, endPointLabel, endPoint) ||
                      labelIs(label, rootSpanIdLabel, rootSpanId),
                    'loop can be observed with value0 or value1 or root span id or endpoint',
                  );
                });
              } else {
                assert(labels.length < 3, 'loop can have at most one label');
                labels.forEach(label => {
                  assert(
                    labelIs(label, 'label', 'value0') ||
                      labelIs(label, 'label', 'value1') ||
                      labelIs(label, rootSpanIdLabel, rootSpanId),
                    'loop can be observed with value0 or value1 or root span id',
                  );
                });
              }

              break;
            case fn0Idx:
              assert(
                labels.length < 2,
                `fn0 can have at most one label, instead got: ${labels.map(
                  labelStr,
                )}`,
              );
              labels.forEach(label => {
                if (labelIs(label, 'label', 'value0')) {
                  fn0ObservedWithLabel0 = true;
                } else {
                  throw new AssertionError({
                    message:
                      'Only value0 can be observed with fn0. Observed instead ' +
                      labelStr(label),
                  });
                }
              });
              break;
            case fn1Idx:
              if (enableEndPoint) {
                assert(
                  labels.length === 3,
                  'fn1 must be observed with a label, a root span id and an endpoint',
                );
                const labelMap = getLabels(labels);
                assert.deepEqual(labelMap, {
                  ...label1,
                  [endPointLabel]: endPoint,
                });
              } else {
                assert(
                  labels.length === 2,
                  'fn1 must be observed with a label',
                );
                labels.forEach(label => {
                  assert(
                    labelIs(label, 'label', 'value1') ||
                      labelIs(label, rootSpanIdLabel, rootSpanId),
                    'Only value1 can be observed with fn1',
                  );
                });
              }
              fn1ObservedWithLabel1 = true;
              break;
            case fn2Idx:
              assert(
                labels.length === 0,
                'fn2 must be observed with no labels. Observed instead with ' +
                  labelStr(labels[0]),
              );
              fn2ObservedWithoutLabels = true;
              break;
            default:
            // Make no assumptions about other functions; we can just as well
            // capture internals of time-profiler.ts, GC, etc.
          }
        });
        assert(fn0ObservedWithLabel0, 'fn0 was not observed with value0');
        assert(fn1ObservedWithLabel1, 'fn1 was not observed with value1');
        assert(
          fn2ObservedWithoutLabels,
          'fn2 was not observed without a label',
        );
        assert(!collectAsyncId || observedAsyncId, 'Async ID was not observed');
      }
    });
  });

  it('should have async IDs when enabled', async function shouldCollectAsyncIDs() {
    if (!(collectAsyncId && ['darwin', 'linux'].includes(process.platform))) {
      this.skip();
    }
    this.timeout(3000);

    time.start({
      intervalMicros: PROFILE_OPTIONS.intervalMicros,
      durationMillis: PROFILE_OPTIONS.durationMillis,
      withContexts: true,
      lineNumbers: false,
      collectAsyncId: true,
    });
    let setDone: () => void;
    const done = new Promise<void>(resolve => {
      setDone = resolve;
    });

    const testStart = hrtime.bigint();
    const testDurationNanos = PROFILE_OPTIONS.durationMillis * 1_000_000;
    setTimeout(loop, 0);

    function loop() {
      const loopDurationNanos = PROFILE_OPTIONS.intervalMicros * 1_000;
      const loopStart = hrtime.bigint();
      while (hrtime.bigint() - loopStart < loopDurationNanos);
      if (hrtime.bigint() - testStart < testDurationNanos) {
        setTimeout(loop, 0);
      } else {
        setDone();
      }
    }

    await done;

    let asyncIdObserved = false;
    time.stop(false, ({context}: GenerateTimeLabelsArgs) => {
      if (!asyncIdObserved && typeof context?.asyncId === 'number') {
        asyncIdObserved = context?.asyncId !== -1;
      }
      return {};
    });
    assert(asyncIdObserved, 'Async ID was not observed');
  });

  describe('profile (w/ stubs)', () => {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const sinonStubs: Array<sinon.SinonStub<any, any>> = [];
    const timeProfilerStub = {
      start: sinon.stub(),
      stopAndCollect: sinon
        .stub()
        .callsFake(
          (_restart: boolean, cb: (p: typeof v8TimeProfile) => unknown) =>
            cb(v8TimeProfile),
        ),
      dispose: sinon.stub(),
      v8ProfilerStuckEventLoopDetected: sinon.stub().returns(0),
    };

    before(() => {
      sinonStubs.push(
        sinon.stub(v8TimeProfiler, 'TimeProfiler').returns(timeProfilerStub),
      );
      sinonStubs.push(sinon.stub(Date, 'now').returns(0));
    });

    after(() => {
      sinonStubs.forEach(stub => {
        stub.restore();
      });
    });

    it('should profile during duration and finish profiling after duration', async () => {
      let isProfiling = true;
      void time.profile(PROFILE_OPTIONS).then(() => {
        isProfiling = false;
      });
      await setTimeoutPromise(2 * PROFILE_OPTIONS.durationMillis);
      assert.strictEqual(false, isProfiling, 'profiler is still running');
    });

    it('should return a profile equal to the expected profile', async () => {
      const profile = await time.profile(PROFILE_OPTIONS);
      assert.deepEqual(timeProfile, profile);
    });

    it('should be able to restart when stopping', async () => {
      time.start({intervalMicros: PROFILE_OPTIONS.intervalMicros});
      timeProfilerStub.start.resetHistory();
      timeProfilerStub.stopAndCollect.resetHistory();

      assert.deepEqual(timeProfile, time.stop(true));
      assert.equal(
        time.v8ProfilerStuckEventLoopDetected(),
        0,
        'v8 bug detected',
      );

      sinon.assert.notCalled(timeProfilerStub.start);
      sinon.assert.calledOnce(timeProfilerStub.stopAndCollect);

      timeProfilerStub.start.resetHistory();
      timeProfilerStub.stopAndCollect.resetHistory();

      assert.deepEqual(timeProfile, time.stop());

      sinon.assert.notCalled(timeProfilerStub.start);
      sinon.assert.calledOnce(timeProfilerStub.stopAndCollect);
    });
  });

  describe('stop`', () => {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const sinonStubs: Array<sinon.SinonStub<any, any>> = [];
    const timeProfilerStub = {
      start: sinon.stub(),
      // stopAndCollect invokes the callback synchronously with the raw profile,
      // mirroring what the native binding does.
      stopAndCollect: sinon
        .stub()
        .callsFake(
          (_restart: boolean, cb: (p: typeof v8TimeProfile) => unknown) =>
            cb(v8TimeProfile),
        ),
      dispose: sinon.stub(),
      v8ProfilerStuckEventLoopDetected: sinon.stub().returns(0),
    };

    before(() => {
      sinonStubs.push(
        sinon.stub(v8TimeProfiler, 'TimeProfiler').returns(timeProfilerStub),
      );
      sinonStubs.push(sinon.stub(Date, 'now').returns(0));
    });

    after(() => {
      sinonStubs.forEach(stub => stub.restore());
    });

    it('should profile during duration and finish profiling after duration', async () => {
      let isProfiling = true;
      void time.profile(PROFILE_OPTIONS).then(() => {
        isProfiling = false;
      });
      await setTimeoutPromise(2 * PROFILE_OPTIONS.durationMillis);
      assert.strictEqual(false, isProfiling, 'profiler is still running');
    });

    it('should return a profile equal to the expected profile', async () => {
      const profile = await time.profile(PROFILE_OPTIONS);
      assert.deepEqual(timeProfile, profile);
    });

    it('should be able to restart when stopping', async () => {
      time.start({intervalMicros: PROFILE_OPTIONS.intervalMicros});
      timeProfilerStub.start.resetHistory();
      timeProfilerStub.stopAndCollect.resetHistory();

      assert.deepEqual(timeProfile, stop(true));
      assert.equal(
        time.v8ProfilerStuckEventLoopDetected(),
        0,
        'v8 bug detected',
      );
      sinon.assert.notCalled(timeProfilerStub.start);
      sinon.assert.calledOnce(timeProfilerStub.stopAndCollect);

      timeProfilerStub.start.resetHistory();
      timeProfilerStub.stopAndCollect.resetHistory();

      assert.deepEqual(timeProfile, stop());
      sinon.assert.notCalled(timeProfilerStub.start);
      sinon.assert.calledOnce(timeProfilerStub.stopAndCollect);
    });
  });

  describe('v8BugWorkaround (w/ stubs)', () => {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const sinonStubs: Array<sinon.SinonStub<any, any>> = [];
    const timeProfilerStub = {
      start: sinon.stub(),
      stopAndCollect: sinon
        .stub()
        .callsFake(
          (_restart: boolean, cb: (p: typeof v8TimeProfile) => unknown) =>
            cb(v8TimeProfile),
        ),
      dispose: sinon.stub(),
      v8ProfilerStuckEventLoopDetected: sinon.stub().returns(2),
    };

    before(() => {
      sinonStubs.push(
        sinon.stub(v8TimeProfiler, 'TimeProfiler').returns(timeProfilerStub),
      );
      sinonStubs.push(sinon.stub(Date, 'now').returns(0));
    });

    after(() => {
      sinonStubs.forEach(stub => {
        stub.restore();
      });
    });

    it('should reset profiler when empty profile is returned and restart is requested', () => {
      time.start(PROFILE_OPTIONS);
      time.stop(true);
      sinon.assert.calledTwice(timeProfilerStub.start);
      sinon.assert.calledTwice(timeProfilerStub.stopAndCollect);

      assert.equal(
        time.v8ProfilerStuckEventLoopDetected(),
        2,
        'v8 bug not detected',
      );
      timeProfilerStub.start.resetHistory();
      timeProfilerStub.stopAndCollect.resetHistory();

      time.stop(false);
      sinon.assert.notCalled(timeProfilerStub.start);
      sinon.assert.calledOnce(timeProfilerStub.stopAndCollect);
    });
  });

  describe('lowCardinalityLabels', () => {
    it('should handle lowCardinalityLabels parameter in stop', async function testLowCardinalityLabels() {
      if (unsupportedPlatform) {
        this.skip();
      }
      this.timeout(3000);

      // Set up some contexts with labels that we'll mark as low cardinality
      const lowCardLabel = 'service_name';
      const highCardLabel = 'trace_id';
      const lowCardValues = ['web-service', 'api-service']; // Low cardinality values
      const context1 = {
        [lowCardLabel]: lowCardValues[0],
        [highCardLabel]: '12345',
      };
      const context2 = {
        [lowCardLabel]: lowCardValues[1],
        [highCardLabel]: '67890',
      };
      const context3 = {
        [lowCardLabel]: lowCardValues[0],
        [highCardLabel]: '54321',
      }; // Reuse low card value

      time.start({
        intervalMicros: PROFILE_OPTIONS.intervalMicros,
        durationMillis: PROFILE_OPTIONS.durationMillis,
        withContexts: true,
        lineNumbers: false,
        useCPED,
      });

      // Run busy loop with context switching for profile duration
      const profileStart = Date.now();
      let iterationCount = 0;

      while (Date.now() - profileStart < PROFILE_OPTIONS.durationMillis) {
        const start = hrtime.bigint();
        const durationNanos = PROFILE_OPTIONS.intervalMicros * 1000;
        while (hrtime.bigint() - start < durationNanos) {
          // Busy loop
        }

        // Cycle through different contexts
        const contexts = [context1, context2, context3];
        time.setContext(contexts[iterationCount % contexts.length]);
        iterationCount++;

        // Allow other tasks to run
        await new Promise(resolve => setImmediate(resolve));
      }

      let labelsCollected = false;
      const lowCardinalityArray = [lowCardLabel];

      const generateLabelsFunc = ({context}: GenerateTimeLabelsArgs) => {
        if (!context) {
          return {};
        }
        labelsCollected = true;
        // Generate labels from context
        const labels: LabelSet = {};
        for (const [key, value] of Object.entries(context.context ?? {})) {
          if (typeof value === 'string') {
            labels[key] = value;
          }
        }
        return labels;
      };

      const profile = time.stop(false, generateLabelsFunc, lowCardinalityArray);

      // Verify that labels were collected and the profile is valid
      assert(labelsCollected, 'Labels should have been collected');
      assert.ok(profile, 'Profile should be generated');
      assert.ok(profile.stringTable, 'Profile should have string table');
      assert(profile.sample.length > 0, 'Profile should have samples');

      // Check that samples have the expected labels and collect low cardinality labels
      let foundLowCardLabel = false;
      let foundHighCardLabel = false;
      const lowCardinalityLabels: Label[] = [];

      for (const sample of profile.sample) {
        if (sample.label && sample.label.length > 0) {
          for (const label of sample.label) {
            const keyStr = profile.stringTable.strings[Number(label.key)];
            const valueStr = profile.stringTable.strings[Number(label.str)];

            if (keyStr === lowCardLabel && lowCardValues.includes(valueStr)) {
              foundLowCardLabel = true;
              lowCardinalityLabels.push(label);
            }
            if (keyStr === highCardLabel) {
              foundHighCardLabel = true;
            }
          }
        }
      }

      assert(foundLowCardLabel, 'Should find low cardinality label in samples');
      assert(
        foundHighCardLabel,
        'Should find high cardinality label in samples',
      );

      // Verify that the lowCardinalityLabels parameter is working correctly.

      // Group labels by value and count them
      const labelsByValue = new Map<string, Label[]>();
      lowCardinalityLabels.forEach(label => {
        const valueStr = profile.stringTable.strings[Number(label.str)];
        if (!labelsByValue.has(valueStr)) {
          labelsByValue.set(valueStr, []);
        }
        labelsByValue.get(valueStr)!.push(label);
      });

      // We should have exactly 2 distinct values (web-service and api-service)
      assert(
        labelsByValue.size === 2,
        `Expected exactly 2 distinct low cardinality label values, found ${
          labelsByValue.size
        }. Values: ${Array.from(labelsByValue.keys()).join(', ')}`,
      );

      // Verify we found both expected values
      assert(
        labelsByValue.has('web-service'),
        'Should find web-service labels',
      );
      assert(
        labelsByValue.has('api-service'),
        'Should find api-service labels',
      );

      // Verify that the lowCardinalityLabels parameter was properly used
      // This tests that labels are being processed with the low cardinality configuration
      labelsByValue.forEach((labels, value) => {
        assert(
          labels.length > 0,
          `Should have at least one label with value '${value}'`,
        );

        // Check that all labels have the same key (service_name)
        labels.forEach(label => {
          const keyStr = profile.stringTable.strings[Number(label.key)];
          assert(
            keyStr === lowCardLabel,
            `Expected label key to be '${lowCardLabel}', got '${keyStr}'`,
          );
        });
      });

      // Test that the Set of all low cardinality labels contains exactly 2 unique values
      // This verifies that the lowCardinalityLabels parameter is properly handled
      const allUniqueValues = new Set(
        lowCardinalityLabels.map(
          label => profile.stringTable.strings[Number(label.str)],
        ),
      );
      assert(
        allUniqueValues.size === 2,
        `Expected exactly 2 unique low cardinality label values across all samples, found ${allUniqueValues.size}`,
      );
      assert(
        allUniqueValues.has('web-service') &&
          allUniqueValues.has('api-service'),
        'Should find both web-service and api-service values in the low cardinality labels',
      );

      // Verify that low cardinality labels with the same value are the same object
      // This tests the deduplication behavior as requested by the user
      labelsByValue.forEach((labels, value) => {
        const uniqueObjects = new Set(labels);
        assert(
          uniqueObjects.size === 1,
          `All labels with value '${value}' should be the same object, found ${uniqueObjects.size} different objects. ` +
            'The lowCardinalityLabels parameter should enable deduplication of Label objects with identical key/value pairs.',
        );
      });
    });
  });

  describe('getNativeThreadId', () => {
    it('should return a number', () => {
      const threadId = getNativeThreadId();
      assert.ok(typeof threadId === 'number');
      assert.ok(threadId > 0);
    });
  });

  describe('runWithContext', () => {
    it('should throw when profiler is not started', () => {
      assert.throws(() => {
        time.runWithContext({label: 'test'}, () => {});
      }, /Wall profiler is not started/);
    });

    it('should throw when useCPED is not enabled', function testNoCPED() {
      if (unsupportedPlatform) {
        this.skip();
      }

      time.start({
        intervalMicros: PROFILE_OPTIONS.intervalMicros,
        durationMillis: PROFILE_OPTIONS.durationMillis,
        withContexts: true,
        useCPED: false,
      });

      try {
        assert.throws(() => {
          time.runWithContext({label: 'test'}, () => {});
        }, /Can only use runWithContext with AsyncContextFrame/);
      } finally {
        time.stop();
      }
    });

    it('should run function with context when useCPED is enabled', function testRunWithContext() {
      if (shouldSkipCPEDTests) {
        this.skip();
      }

      time.start({
        intervalMicros: PROFILE_OPTIONS.intervalMicros,
        durationMillis: PROFILE_OPTIONS.durationMillis,
        withContexts: true,
        useCPED: true,
      });

      try {
        const testContext = {label: 'test-value', id: '123'};
        let contextInsideFunction;

        time.runWithContext(testContext, () => {
          contextInsideFunction = time.getContext();
        });

        assert.deepEqual(
          contextInsideFunction,
          testContext,
          'Context should be accessible within function',
        );
      } finally {
        time.stop();
      }
    });

    it('should pass arguments to function correctly', function testArguments() {
      if (shouldSkipCPEDTests) {
        this.skip();
      }

      time.start({
        intervalMicros: PROFILE_OPTIONS.intervalMicros,
        durationMillis: PROFILE_OPTIONS.durationMillis,
        withContexts: true,
        useCPED: true,
      });

      try {
        const testContext = {label: 'test'};
        const result = time.runWithContext(
          testContext,
          (a: number, b: string, c: boolean) => {
            return {a, b, c};
          },
          42,
          'hello',
          true,
        );

        assert.deepEqual(
          result,
          {a: 42, b: 'hello', c: true},
          'Arguments should be passed correctly',
        );
      } finally {
        time.stop();
      }
    });

    it('should return function result', function testReturnValue() {
      if (shouldSkipCPEDTests) {
        this.skip();
      }

      time.start({
        intervalMicros: PROFILE_OPTIONS.intervalMicros,
        durationMillis: PROFILE_OPTIONS.durationMillis,
        withContexts: true,
        useCPED: true,
      });

      try {
        const testContext = {label: 'test'};
        const result = time.runWithContext(testContext, () => {
          return 'test-result';
        });

        assert.strictEqual(
          result,
          'test-result',
          'Function result should be returned',
        );
      } finally {
        time.stop();
      }
    });

    it('should handle nested runWithContext calls', function testNestedCalls() {
      if (shouldSkipCPEDTests) {
        this.skip();
      }

      time.start({
        intervalMicros: PROFILE_OPTIONS.intervalMicros,
        durationMillis: PROFILE_OPTIONS.durationMillis,
        withContexts: true,
        useCPED: true,
      });

      try {
        const outerContext = {label: 'outer'};
        const innerContext = {label: 'inner'};
        const results: string[] = [];

        time.runWithContext(outerContext, () => {
          const ctx1 = time.getContext();
          results.push((ctx1 as Record<string, string>).label);

          time.runWithContext(innerContext, () => {
            const ctx2 = time.getContext();
            results.push((ctx2 as Record<string, string>).label);
          });

          const ctx3 = time.getContext();
          results.push((ctx3 as Record<string, string>).label);
        });

        assert.deepEqual(
          results,
          ['outer', 'inner', 'outer'],
          'Nested contexts should be properly isolated and restored',
        );
      } finally {
        time.stop();
      }
    });

    it('should isolate context from outside runWithContext', function testContextIsolation() {
      if (shouldSkipCPEDTests) {
        this.skip();
      }

      time.start({
        intervalMicros: PROFILE_OPTIONS.intervalMicros,
        durationMillis: PROFILE_OPTIONS.durationMillis,
        withContexts: true,
        useCPED: true,
      });

      try {
        const runWithContextContext = {label: 'inside'};
        let contextInside;

        time.runWithContext(runWithContextContext, () => {
          contextInside = time.getContext();
        });

        // Context outside runWithContext should be undefined since we're using CPED
        const contextOutside = time.getContext();

        assert.deepEqual(
          contextInside,
          runWithContextContext,
          'Context inside should match',
        );
        assert.strictEqual(
          contextOutside,
          undefined,
          'Context outside should be undefined with CPED',
        );
      } finally {
        time.stop();
      }
    });

    it('should work with async functions', async function testAsyncFunction() {
      if (shouldSkipCPEDTests) {
        this.skip();
      }

      time.start({
        intervalMicros: PROFILE_OPTIONS.intervalMicros,
        durationMillis: PROFILE_OPTIONS.durationMillis,
        withContexts: true,
        useCPED: true,
      });

      try {
        const testContext = {label: 'async-test'};

        const result = await time.runWithContext(testContext, async () => {
          const ctx1 = time.getContext();
          await setTimeoutPromise(10);
          const ctx2 = time.getContext();
          return {ctx1, ctx2};
        });

        assert.deepEqual(
          result.ctx1,
          testContext,
          'Context should be available before await',
        );
        assert.deepEqual(
          result.ctx2,
          testContext,
          'Context should be preserved after await',
        );
      } finally {
        time.stop();
      }
    });
  });
});
```

## File: `ts/test/test-worker-threads.ts`
```typescript
import {execFile} from 'child_process';
import {promisify} from 'util';
import {Worker} from 'worker_threads';

const exec = promisify(execFile);

describe('Worker Threads', () => {
  // eslint-ignore-next-line prefer-array-callback
  it('should work', function () {
    this.timeout(20000);
    const nbWorkers = 2;
    return exec('node', ['./out/test/worker.js', String(nbWorkers)]);
  });

  it('should not crash when worker is terminated', async function () {
    this.timeout(30000);
    const nruns = 5;
    const concurrentWorkers = 20;
    for (let i = 0; i < nruns; i++) {
      const workers = [];
      for (let j = 0; j < concurrentWorkers; j++) {
        const worker = new Worker('./out/test/worker2.js');
        worker.postMessage('hello');

        worker.on('message', () => {
          void worker.terminate();
        });

        workers.push(
          new Promise<void>((resolve, reject) => {
            worker.on('exit', exitCode => {
              if (exitCode === 1) {
                resolve();
              } else {
                reject(new Error('Worker exited with code 0'));
              }
            });
          }),
        );
      }
      await Promise.all(workers);
    }
  });
});
```

## File: `ts/test/worker.ts`
```typescript
import {Worker, isMainThread, workerData, parentPort} from 'worker_threads';
import {pbkdf2} from 'crypto';
import {time} from '../src/index';
import {Profile, ValueType} from 'pprof-format';
import {getAndVerifyPresence, getAndVerifyString} from './profiles-for-tests';
import {satisfies} from 'semver';

import assert from 'assert';

const DURATION_MILLIS = 1000;
const intervalMicros = 10000;
const withContexts =
  process.platform === 'darwin' || process.platform === 'linux';
const useCPED =
  withContexts &&
  ((satisfies(process.versions.node, '>=24.0.0') &&
    !process.execArgv.includes('--no-async-context-frame')) ||
    (satisfies(process.versions.node, '>=22.7.0') &&
      process.execArgv.includes('--experimental-async-context-frame')));
const collectAsyncId =
  withContexts && satisfies(process.versions.node, '>=24.0.0');

function createWorker(durationMs: number): Promise<Profile[]> {
  return new Promise((resolve, reject) => {
    const profiles: Profile[] = [];
    new Worker(__filename, {workerData: {durationMs}})
      .on('exit', exitCode => {
        if (exitCode !== 0) reject();
        setTimeout(
          () => {
            // Run a second worker after the first one exited to test for proper
            // cleanup after first worker. This used to segfault.
            new Worker(__filename, {workerData: {durationMs}})
              .on('exit', exitCode => {
                if (exitCode !== 0) reject();
                resolve(profiles);
              })
              .on('error', reject)
              .on('message', profile => {
                profiles.push(profile);
              });
          },
          Math.floor(Math.random() * durationMs),
        );
      })
      .on('error', reject)
      .on('message', profile => {
        profiles.push(profile);
      });
  });
}

async function executeWorkers(nbWorkers: number, durationMs: number) {
  const workers = [];
  for (let i = 0; i < nbWorkers; i++) {
    workers.push(createWorker(durationMs));
  }
  return Promise.all(workers).then(profiles => profiles.flat());
}

function getCpuUsage() {
  const cpu = process.cpuUsage();
  return cpu.user + cpu.system;
}

async function main(durationMs: number) {
  time.start({
    durationMillis: durationMs * 3,
    intervalMicros,
    withContexts,
    collectCpuTime: withContexts,
    useCPED: useCPED,
    collectAsyncId: collectAsyncId,
  });
  if (withContexts) {
    time.setContext({});
  }

  const cpu0 = getCpuUsage();
  const nbWorkers = Number(process.argv[2] ?? 2);

  // start workers
  const workers = executeWorkers(nbWorkers, durationMs);

  const deadline = Date.now() + durationMs;
  // wait for all work to finish
  await Promise.all([bar(deadline), foo(deadline)]);
  const workerProfiles = await workers;

  // restart and check profile
  const profile1 = time.stop(true);
  const cpu1 = getCpuUsage();

  workerProfiles.forEach(checkProfile);
  checkProfile(profile1);
  if (withContexts) {
    checkCpuTime(profile1, cpu1 - cpu0, workerProfiles);
  }
  const newDeadline = Date.now() + durationMs;
  await Promise.all([bar(newDeadline), foo(newDeadline)]);

  const profile2 = time.stop();
  const cpu2 = getCpuUsage();
  checkProfile(profile2);
  if (withContexts) {
    checkCpuTime(profile2, cpu2 - cpu1);
  }
}

async function worker(durationMs: number) {
  time.start({
    durationMillis: durationMs,
    intervalMicros,
    withContexts,
    collectCpuTime: withContexts,
    useCPED: useCPED,
    collectAsyncId: collectAsyncId,
  });
  if (withContexts) {
    time.setContext({});
  }

  const deadline = Date.now() + durationMs;
  await Promise.all([bar(deadline), foo(deadline)]);

  const profile = time.stop();
  parentPort?.postMessage(profile);
}

if (isMainThread) {
  void main(DURATION_MILLIS);
} else {
  void worker(workerData.durationMs);
}

function valueName(profile: Profile, vt: ValueType) {
  const type = getAndVerifyString(profile.stringTable!, vt, 'type');
  const unit = getAndVerifyString(profile.stringTable!, vt, 'unit');
  return `${type}/${unit}`;
}

function sampleName(profile: Profile, sampleType: ValueType[]) {
  return sampleType.map(valueName.bind(null, profile));
}

function getCpuTime(profile: Profile) {
  let jsCpuTime = 0;
  let nonJsCpuTime = 0;
  if (!withContexts) return {jsCpuTime, nonJsCpuTime};
  for (const sample of profile.sample!) {
    const locationId = sample.locationId[0];
    const location = getAndVerifyPresence(
      profile.location!,
      locationId as number,
    );
    const functionId = location.line![0].functionId;
    const fn = getAndVerifyPresence(profile.function!, functionId as number);
    const fn_name = profile.stringTable.strings[fn.name as number];
    if (fn_name === time.constants.NON_JS_THREADS_FUNCTION_NAME) {
      nonJsCpuTime += sample.value![2] as number;
      assert.strictEqual(sample.value![0], 0);
      assert.strictEqual(sample.value![1], 0);
    } else {
      jsCpuTime += sample.value![2] as number;
    }
  }

  return {jsCpuTime, nonJsCpuTime};
}

function checkCpuTime(
  profile: Profile,
  processCpuTimeMicros: number,
  workerProfiles: Profile[] = [],
  maxRelativeError = 0.1,
) {
  let workersJsCpuTime = 0;
  let workersNonJsCpuTime = 0;

  for (const workerProfile of workerProfiles) {
    const {jsCpuTime, nonJsCpuTime} = getCpuTime(workerProfile);
    workersJsCpuTime += jsCpuTime;
    workersNonJsCpuTime += nonJsCpuTime;
  }

  const {jsCpuTime: mainJsCpuTime, nonJsCpuTime: mainNonJsCpuTime} =
    getCpuTime(profile);

  // workers should not report non-JS CPU time
  assert.strictEqual(
    workersNonJsCpuTime,
    0,
    'worker non-JS CPU time should be null',
  );

  const totalCpuTimeMicros =
    (mainJsCpuTime + mainNonJsCpuTime + workersJsCpuTime) / 1000;
  const err =
    Math.abs(totalCpuTimeMicros - processCpuTimeMicros) / processCpuTimeMicros;
  const msg = `process cpu time: ${
    processCpuTimeMicros / 1000
  }ms\ntotal profile cpu time: ${
    totalCpuTimeMicros / 1000
  }ms\nmain JS cpu time: ${mainJsCpuTime / 1000000}ms\nworker JS cpu time: ${
    workersJsCpuTime / 1000000
  }\nnon-JS cpu time: ${mainNonJsCpuTime / 1000000}ms\nerror: ${err}`;
  assert.ok(
    err <= maxRelativeError,
    `total profile CPU time should be close to process cpu time:\n${msg}`,
  );
}

function checkProfile(profile: Profile) {
  assert.deepStrictEqual(sampleName(profile, profile.sampleType!), [
    'sample/count',
    'wall/nanoseconds',
    ...(withContexts ? ['cpu/nanoseconds'] : []),
  ]);
  assert.strictEqual(typeof profile.timeNanos, 'number');
  assert.strictEqual(typeof profile.durationNanos, 'number');
  assert.strictEqual(typeof profile.period, 'number');
  assert.strictEqual(
    valueName(profile, profile.periodType!),
    'wall/nanoseconds',
  );

  assert.ok(profile.sample.length > 0, 'No samples');

  for (const sample of profile.sample!) {
    assert.deepStrictEqual(sample.label, []);

    for (const value of sample.value!) {
      assert.strictEqual(typeof value, 'number');
    }

    for (const locationId of sample.locationId!) {
      const location = getAndVerifyPresence(
        profile.location!,
        locationId as number,
      );

      for (const {functionId, line} of location.line!) {
        const fn = getAndVerifyPresence(
          profile.function!,
          functionId as number,
        );

        getAndVerifyString(profile.stringTable!, fn, 'name');
        getAndVerifyString(profile.stringTable!, fn, 'systemName');
        getAndVerifyString(profile.stringTable!, fn, 'filename');
        assert.strictEqual(typeof line, 'number');
      }
    }
  }
}

async function bar(deadline: number) {
  let done = false;
  setTimeout(() => {
    done = true;
  }, deadline - Date.now());
  while (!done) {
    await new Promise<void>(resolve => {
      pbkdf2('secret', 'salt', 100000, 64, 'sha512', () => {
        resolve();
      });
    });
  }
}

function fooWork() {
  let sum = 0;
  for (let i = 0; i < 1e7; i++) {
    sum += sum;
  }
  return sum;
}

async function foo(deadline: number) {
  let done = false;
  setTimeout(() => {
    done = true;
  }, deadline - Date.now());

  while (!done) {
    await new Promise<void>(resolve => {
      fooWork();
      setImmediate(() => resolve());
    });
  }
}
```

## File: `ts/test/worker2.ts`
```typescript
import {parentPort} from 'node:worker_threads';
import {time} from '../src/index';
import {satisfies} from 'semver';

const delay = (ms: number) => new Promise(res => setTimeout(res, ms));

const DURATION_MILLIS = 1000;
const INTERVAL_MICROS = 10000;
const withContexts =
  process.platform === 'darwin' || process.platform === 'linux';

const useCPED =
  withContexts &&
  ((satisfies(process.versions.node, '>=24.0.0') &&
    !process.execArgv.includes('--no-async-context-frame')) ||
    (satisfies(process.versions.node, '>=22.7.0') &&
      process.execArgv.includes('--experimental-async-context-frame')));

const collectAsyncId =
  withContexts && satisfies(process.versions.node, '>=24.0.0');

time.start({
  durationMillis: DURATION_MILLIS,
  intervalMicros: INTERVAL_MICROS,
  withContexts: withContexts,
  collectCpuTime: withContexts,
  collectAsyncId: collectAsyncId,
  useCPED: useCPED,
});

parentPort?.on('message', () => {
  void delay(50).then(() => {
    parentPort?.postMessage('hello');
  });
});
```


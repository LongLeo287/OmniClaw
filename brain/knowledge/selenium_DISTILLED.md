---
id: selenium
type: knowledge
owner: OA_Triage
---
# selenium
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "selenium",
  "packageManager": "pnpm@9.15.4",
  "workspaces": [
    "javascript/grid-ui",
    "javascript/selenium-webdriver"
  ],
  "repository": {
    "type": "git",
    "url": "https://github.com/SeleniumHQ/selenium.git"
  },
  "pnpm": {
    "onlyBuiltDependencies": [],
    "packageExtensions": {
      "google-closure-deps": {
        "dependencies": {
          "minimatch": "*"
        }
      },
      "minimatch": {
        "dependencies": {
          "brace-expansion": "*"
        }
      },
      "brace-expansion": {
        "dependencies": {
          "balanced-match": "*"
        }
      }
    }
  }
}

```

### File: README.md
```md
<h1 align="center">
  <br/>
  <a href="https://selenium.dev"><img src="common/images/selenium_logo_mark_green.svg" alt="Selenium" width="100"></a>
  <br/>
  Selenium
  <br/>
</h1>

<h3 align="center">Automates browsers. That's it!</h3>

<p align="center">
  <a href="#contributing">Contributing</a> •
  <a href="#installing">Installing</a> •
  <a href="#building">Building</a> •
  <a href="#developing">Developing</a> •
  <a href="#testing">Testing</a> •
  <a href="#documenting">Documenting</a> •
  <a href="#releasing">Releasing</a>
</p>

<br>

Selenium is an umbrella project encapsulating a variety of tools and
libraries enabling web browser automation. Selenium specifically
provides an infrastructure for the [W3C WebDriver specification](https://w3c.github.io/webdriver/)
— a platform and language-neutral coding interface compatible with all
major web browsers.

The project is made possible by volunteer contributors who've
generously donated thousands of hours in code development and upkeep.

This README is for developers interested in contributing to the project.
For people looking to get started using Selenium, please check out
our [User Manual](https://selenium.dev/documentation/) for detailed examples and descriptions, and if you
get stuck, there are several ways to [Get Help](https://www.selenium.dev/support/).

[![CI](https://github.com/SeleniumHQ/selenium/actions/workflows/ci.yml/badge.svg)](https://github.com/SeleniumHQ/selenium/actions/workflows/ci.yml)
[![CI - RBE](https://github.com/SeleniumHQ/selenium/actions/workflows/ci-rbe.yml/badge.svg)](https://github.com/SeleniumHQ/selenium/actions/workflows/ci-rbe.yml)
[![Releases downloads](https://img.shields.io/github/downloads/SeleniumHQ/selenium/total.svg)](https://github.com/SeleniumHQ/selenium/releases)

## Contributing

Please read [CONTRIBUTING.md](https://github.com/SeleniumHQ/selenium/blob/trunk/CONTRIBUTING.md)
before submitting your pull requests.

## Installing

These are the requirements to create your own local dev environment to contribute to Selenium.

### All Platforms

* [Bazelisk](https://github.com/bazelbuild/bazelisk), a Bazel wrapper that automatically downloads
  the version of Bazel specified in `.bazelversion` file and transparently passes through all
  command-line arguments to the real Bazel binary.
* Java JDK version 17 or greater (e.g., [Java 17 Temurin](https://adoptium.net/temurin/releases/?version=17))
  * Set `JAVA_HOME` environment variable to location of Java executable (the JDK not the JRE)
  * To test this, try running the command `javac`. This command won't exist if you only have the JRE
  installed. If you're met with a list of command-line options, you're referencing the JDK properly.

### MacOS

  * Xcode including the command-line tools. Install the latest version using: `xcode-select --install`
  * Rosetta for Apple Silicon Macs. Add `build --host_platform=//:rosetta` to the `.bazelrc.local` file. We are working
  to make sure this isn't required in the long run.

### Windows

Several years ago [Jim Evans](https://www.linkedin.com/in/jimevansmusic/) published a great article on
[Setting Up a Windows Development Environment for the Selenium .NET Language Bindings](https://jimevansmusic.blogspot.com/2020/04/setting-up-windows-development.html);
This article is out of date, but it includes more detailed descriptions and screenshots that some people might find useful.

<details>
<summary>Click to see Current Windows Setup Requirements</summary>

#### Option 1: Automatic Installation from Scratch

This script will ensure a complete ready to execute developer environment.
(nothing is installed or set that is already present unless otherwise prompted)

1. Open Powershell as an Administrator
2. Execute: `Set-ExecutionPolicy Bypass -Scope Process -Force` to allow running the script in the process
3. Navigate to the directory you want to clone Selenium in, or the parent directory of an already cloned Selenium repo
4. Download and execute this script in the powershell terminal: [scripts/dev-environment-setup.ps1]`

#### Option 2: Manual Installation

1. Allow running scripts in Selenium in general:
    ```
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
    ```
2. Enable Developer Mode:
    ```
    reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\AppModelUnlock" /t REG_DWORD /f /v "AllowDevelopmentWithoutDevLicense" /d "1"
    ```
3. Install [MSYS2](https://www.msys2.org/), which is an alternative shell environment that provides Unix-like commands
    * Add bin directory to `PATH` environment variable (e.g., `"C:\tools\msys64\usr\bin"`)
    * Add `bash.exe` location as the `BAZEL_SH` environment variable (e.g., `"C:\tools\msys64\usr\bin\bash.exe"`)
4. Install the latest version of [Visual Studio Community](https://visualstudio.microsoft.com/vs/community/)
    * Use the visual studio installer to modify and add the "Desktop development with C++" Workload
    * Add Visual C++ build tools installation directory location to `BAZEL_VC` environment variable (e.g. `"C:\Program Files\Microsoft Visual Studio\2022\Community\VC"`)
    * Add Visual C++ Build tools version to `BAZEL_VC_FULL_VERSION` environment variable (this can be discovered from the directory name in `"$BAZEL_VC\Tools\MSVC\<BAZEL_VC_FULL_VERSION>"`)
5. Add support for long file names (bazel has a lot of nested directories that can exceed default limits in Windows)
    * Enable Long Paths support with these 2 registry commands:
    ```shell
    reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Command Processor" /t REG_DWORD /f /v "DisableUNCCheck" /d "1"
    reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem" /t REG_DWORD /f /v "LongPathsEnabled" /d "1"
    ```
    * Allow Bazel to create short name versions of long file paths: `fsutil 8dot3name set 0`
    * Set bazel output to `C:/tmp` instead of nested inside project directory:
        * Create a file `selenium/.bazelrc.windows.local`
        * Add "startup --output_user_root=C:/tmp" to the file

</details>

### Alternative Dev Environments

If you want to contribute to the project, but do not want to set up your own local dev environment,
there are two alternatives available.

#### Using GitPod

Rather than creating your own local dev environment, GitPod provides a ready to use environment for you.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/SeleniumHQ/selenium)

#### Using Dev Container

As an alternative you can build a [Dev Container](https://containers.dev/) - basically a docker container -
suitable for building and testing Selenium using the devcontainer.json in the
[.devcontainer](.devcontainer/devcontainer.json) directory. Supporting IDEs like VS Code or IntelliJ IDEA
should point you to how such a container can be created.

#### Using Docker Image

You can also build a Docker image suitable
for building and testing Selenium using the Dockerfile in the
[dev image](scripts/dev-image/Dockerfile) directory.

## Building

Selenium is built using a common build tool called [Bazel](https://bazel.build/), to
allow us to easily manage dependency downloads, generate required binaries, build and release packages, and execute tests;
all in a fast, efficient manner. For a more detailed discussion, read Simon Stewart's article on [Building Selenium](https://www.selenium.dev/blog/2023/building-selenium/)

Often we wrap Bazel commands with our custom [Rake](http://rake.rubyforge.org/) wrapper. These are run with the `./go` command.

The common Bazel commands are:
* `bazel build` — evaluates dependencies, compiles source files and generates output files for the specified target.
It's used to create executable binaries, libraries, or other artifacts.
* `bazel run` — builds the target and then executes it.
It's typically used for targets that produce executable binaries.
* `bazel test` — builds and runs the target in a context with additional testing functionality
* `bazel query` — identifies available targets for the provided path.

Each module that can be built is defined in a `BUILD.bazel` file. To execute the module you refer to it starting with a
`//`, then include the relative path to the file that defines it, then `:`, then the name of the target.
For example, the target to build the Grid is named `executable-grid` and it is
defined in the `'selenium/java/src/org/openqa/selenium/grid/BAZEL.build'` file.
So to build the grid you would run: `bazel build //java/src/org/openqa/selenium/grid:executable-grid`.

The Bazel documentation has a [handy guide](https://bazel.build/run/build#specifying-build-targets)
for various shortcuts and all the ways to build multiple targets, which Selenium makes frequent use of.

To build everything for a given language:

```shell
bazel build //<language>/...
```

To build just the grid there is an alias name to use (the log will show where the output jar is located):

```shell
bazel build grid
```

To make things more simple, building each of the bindings is available with this `./go` command:

```shell
./go <language>:build
```

## Developing

### Java

#### IntelliJ

Most of the team uses Intellij for their day-to-day editing. If you're
working in IntelliJ, then we highly recommend installing the [Bazel IJ
plugin](https://plugins.jetbrains.com/plugin/8609-bazel) which is documented on
[its own site](https://plugins.jetbrains.com/plugin/8609-bazel).

To use Selenium with the IntelliJ Bazel plugin, import the repository as a Bazel project, and select the project
view file from the [scripts](scripts) directory. `ij.bazelproject` for Mac/Linux and `ij-win.bazelproject` for Windows.

#### Linting

We also use Google Java Format for linting, so using the Google Java Formatter Plugin is useful;
there are a few steps to get it working, so read their [configuration documentation](https://github.com/google/google-java-format/blob/master/README.md#intellij-jre-config).
There is also an auto-formatting script that can be run: `./scripts/format.sh`

#### Local Installation

While Selenium is not built with Maven, you can build and install the Selenium pieces
for Maven to use locally by deploying to your local maven repository (`~/.m2/repository`), using:

```shell
./go java:install
```

#### Updating Dependencies

Dependencies are defined in the file [MODULE.bazel](https://github.com/SeleniumHQ/selenium/blob/trunk/MODULE.bazel).

To update a dependency, modify the version in the `MODULE.bazel` file and run:

```shell
RULES_JVM_EXTERNAL_REPIN=1 bazel run @maven//:pin
```

To automatically update and pin new dependencies, run:

```shell
./go java:update
```

### Python

#### Linting and Formatting

We follow the [PEP8 Style Guide for Python Code](https://peps.python.org/pep-0008) (except we use a 120 character line length).
This is checked and enforced with [ruff](https://docs.astral.sh/ruff/), a linting/formatting tool.
There is also an auto-formatting script that can be run: `./scripts/format.sh`

#### Local Installation

To run Python code locally without building/installing the package, you must first install the dependencies:

```shell
pip install -r py/requirements.txt
```

Then, build the generated files and copy them into your local source tree:

```shell
./go py:local_dev
```

After that, you can import the selenium package directly from source from the `py` directory.

Instead of running from source, you can build and install the selenium package (wheel) locally:

```shell
./go py:install
```

This will attempt to install into the global Python `site-packages` directory,
which might not be writable. To avoid this, you should create and activate a
[virtual environment](https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-virtual-environments)
before installing.


### Ruby

Instead of using `irb`, you can create an interactive REPL with all gems loaded using: `bazel run //rb:console`

If you want to debug code, you can do it via [`debug`](https://github.com/ruby/debug) gem:

1. Add `binding.break` to the code where you want the debugger to start.
2. Run tests with  `ruby_debug` configuration: `bazel test --config ruby_debug <test>`.
3. When debugger starts, run the following in a separate terminal to connect to debugger:

```shell
bazel-selenium/external/bundle/bin/rdbg -A
```

If you want to use [RubyMine](https://www.jetbrains.com/ruby/) for development,
you can configure it use Bazel artifacts:

1. Open `rb/` as a main project directory.
2. From the `selenium` (parent) directory, run `./go rb:local_dev` to create up-to-date artifacts.
3. In <kbd>Settings / Languages & Frameworks / Ruby SDK and Gems</kbd> add new <kbd>Interpreter</kbd> pointing to `../bazel-selenium/external/rules_ruby++ruby+ruby/dist/bin/ruby`.
4. You should now be able to run and debug any spec. It uses Chrome by default, but you can alter it using environment variables specified in [Ruby Testing](#ruby-2) section below.

### Rust

To keep `Cargo.Bazel.lock` synchronized with `Cargo.lock`, run:

```shell
CARGO_BAZEL_REPIN=true bazel run @crates//:all
```

## Testing

There are a number of bazel configurations specific for testing.

### Common Options Examples

Here are examples of arguments we make use of in testing the Selenium code:
* `--pin_browsers=false` - use Selenium Manager to locate browsers/drivers
* `--headless` - run browsers in headless mode (supported be Chrome, Edge and Firefox)
* `--flaky_test_attempts 3` - re-run failed tests up to 3 times
* `--local_test_jobs 1` - control parallelism of tests
* `--cache_test_results=no`, `-t-` - disable caching of test results and re-runs all of them
* `--test_output all` - print all output from the tests, not just errors
* `--test_output streamed` - run all tests one by one and print its output immediately
* `--test_env FOO=bar` - pass extra environment variable to test process
* `--run_under="xvfb-run -a"` - prefix to insert before the execution

### Filtering

Selenium tests can be filtered by size:
* small — typically unit tests where no browser is opened
* large — typically tests that actually drive a browser
* medium — tests that are more involved than simple unit tests, but not fully driving a browser

These can be filtered using the `test_size_filters` argument like this:

```shell
bazel test //<language>/... --test_size_filters=small
```

Tests can also be filtered by tag like:

```shell
bazel test //<language>/... --test_tag_filters=this,-not-this
```

If there are multiple `--test_tag_filters`, only the last one is considered,
so be careful if also using an inherited config

### Java

<details>
<summary>Click to see Java Test Commands</summary>

To run unit tests:

```shell
bazel test //java/... --test_size_filters=small
```
To run integration tests:

```shell
bazel test //java/... --test_size_filters=medium
```
To run browser tests:

```shell
bazel test //java/... --test_size_filters=large --test_tag_filters=<browser>
```

To run a specif
... [TRUNCATED]
```

### File: javascript\readme.txt
```txt
To regenerate deps.js:
$./go calcdeps

To run the tests locally, start the webserver:
```bash
bazel run //java/test/org/openqa/selenium/environment:appserver
```

You can access it in your browser at http://localhost:2310/javascript.

```

### File: rust\README.md
```md
# Selenium Manager

Selenium Manager is a command-line tool implemented in Rust that provides automated driver and browser management for Selenium. For details about its features, visit the [Selenium Manager documentation page](https://www.selenium.dev/documentation/selenium_manager/).

## Rust installation
Selenium Manager has been implemented as a CLI (Command-Line Interface) tool using [Rust](https://www.rust-lang.org/). Therefore, to run it from the source code, you need to [install Rust and Cargo](https://doc.rust-lang.org/cargo/getting-started/installation.html). On Linux and macOS systems, this is done as follows:

```
curl https://sh.rustup.rs -sSf | sh
```

Alternatively, you can build it using [Bazel](https://bazel.build) by executing `bazel build //rust:selenium-manager` from the top-level directory of the Selenium repo (the same one where the `WORKSPACE` file is).

## Usage
Selenium Manager can be executed using Cargo as follows:

```
$ cargo run -- --help
```

For instance, the command required to manage chromedriver is the following:

```
$ cargo run -- --browser chrome
```

Alternatively, you can replace `cargo run` with `bazel run //rust:selenium-manager`, for example `bazel run //rust:selenium-manager -- --browser chrome --debug`

### Windows ARM

There are issues when building on Windows ARM64. To workaround, use `cargo` with `--config Cargo.aarch64-pc-windows-msvc.toml` flag.
```

### File: common\devtools\README.md
```md
# Chrome Debugging Protocol

We keep multiple versions of the protocol in the tree in order to allow us to generate bindings as
needed.

They are typically downloaded from the [devtools source][]

Fortunately both Chrome and Edge are based off Chromium releases and those are OSS. In order to get
the versions of the protocol spoken by particular releases of Chrome:

* Find out the latest version of [Stable Channel Update for Desktop][] (e.g., `96.0.4664.45`).
* Create a `vXX` directory under `//common/devtools/chromium` (e.g. `v96` for `96.0.4664.45`)
* Copy the `BUILD.bazel` file from the `vXX-1` directory.
* Navigate to the [Chromium source][] and open the tag matching the release number.
* Find `//third_party/blink/public/devtools_protocol/browser_protocol.pdl` and download the file
  to `//common/devtools/chromium/vXX`.
  * (Quick link:
    `https://raw.githubusercontent.com/chromium/chromium/<LATEST_VERSION_NUMBER>/third_party/blink/public/devtools_protocol/browser_protocol.pdl`)
* Now figure out the version of v8 used by the version of Chromium. In Chromium's source, navigate
  to `//:DEPS` and search for `v8_revision`
  * (Quick
    link: `https://github.com/chromium/chromium/blob/<LATEST_VERSION_NUMBER>/DEPS#:~:text=the%20commit%20queue%20can%20handle%20cls%20rolling%20v8`)
* Head over to the [v8 source](https://github.com/v8/v8) and switch to the indicated revision
  * (e.g., `451d38b60be0a0f692b11815289cf8cbc9b1dc98`)
* Find `//include/js_protocol.pdl` and download the file to `//common/devtools/chromium/vXX`.
  (Quick link: `https://github.com/v8/v8/raw/<V8_REVISION_NUMBER>/include/js_protocol.pdl`)

You may also find the same information at the [OmahaProxy CSV Viewer][]

We have a modified form of the scripts used by Chromium to generate the protocol files. The
originals were in:

https://github.com/chromium/chromium/blob/master/third_party/inspector_protocol/convert_protocol_to_json.py

[devtools source]: https://github.com/ChromeDevTools/devtools-protocol/tree/master/json

[Stable Channel Update for Desktop]: https://chromereleases.googleblog.com/search/label/Stable%20updates

[Chromium source]: https://github.com/chromium/chromium/

[OmahaProxy CSV Viewer]: https://omahaproxy.appspot.com

```

### File: javascript\atoms\package.json
```json
{
  "name": "selenium-atoms",
  "version": "1.0.0",
  "private": true,
  "description": "Build tools for Selenium Browser Automation Atoms",
  "license": "Apache-2.0",
  "repository": {
    "type": "git",
    "url": "https://github.com/SeleniumHQ/selenium.git"
  },
  "devDependencies": {
    "google-closure-deps": "^20230802.0.0"
  }
}

```

### File: javascript\atoms\README.md
```md
# Javascript Atoms

These "atoms" provide reusable building blocks for browser automation
(which is why we call them "atoms"!) They're currently built with the
Google Closure Compiler, but at some point, we'd love to migrate them
to TypeScript since Closure isn't as widely known.

## Testing the Atoms

### Iteratively

While working on the atoms, it can be helpful to be able to iterate on
the code in your IDE of choice, and then run the tests in a
browser. You can do this by starting a debug server:

```shell
bazel run javascript/atoms:closure-test_debug_server
```

And then navigating to: <http://localhost:2310/filez/_main/javascript/atoms/>

You'll be able to browse around the filesystem until you find the test
you want to work on.

These files are symlinked by bazel to the ones in the source code, so
edits you make there will be reflected in the code in the browser,
however, new files and removed files may cause you to need to restart
the `bazel run` command.

### Using Bazel

You can run all the tests for a browser using:

```shell
bazel test //javascript/atoms:closure-test{,-chrome,-edge,-safari}
```

You can also filter to a specific test using the name of the file
stripped of it's `.html` suffix. For example:

```shell
bazel test --test_filter=shown_test --//common:headless=false javascript/atoms:closure-test-chrome
```

```

### File: AGENTS.md
```md
<!--
Guidance for AI agents working in the Selenium monorepo.
Language-specific details live in respective subdirectories.
-->
See @.local/AGENTS.md for additional guidance

Selenium is a Bazel-built monorepo implementing the W3C WebDriver (and related) protocols,
shipping multiple language bindings plus Grid and Selenium Manager.
The repository README is aimed at contributors; end-user docs live elsewhere.

## Invariants (don't violate unless explicitly asked)
- Maintain API/ABI compatibility - users upgrade by changing only version number
- Avoid repo-wide refactors/formatting; prefer small, reversible diffs

## Toolchain
- The project uses Bazelisk with a hermetic Bazel toolset. Do not run tests or execute Selenium code assuming a language-specific local development environment is configured.
- Rakefile tasks are executed with a bundled jruby wrapped with `go`/`go.bat` and frequently used by CI jobs
- Prefer targeted Bazel commands; use `bazel query ...` to locate labels before build/test

## Execution model
- Use `bazel query` to explore build graph before reading files
- Attempt to execute Bazel commands directly. If prevented due to network/toolchain restrictions within the sandbox, fall back to suggesting copy/paste commands for the user on a separate line.
## Repo layout
Bindings (see `AGENTS.md` in each directory for language-specific details):
- Java: `java/`
- Python: `py/`
- Ruby: `rb/`
- JavaScript: `javascript/selenium-webdriver/`
- .NET: `dotnet/`

Shared/high-risk areas:
- `rust/` (Selenium Manager, see `rust/AGENTS.md`)
- `common/` (build/test wiring; affects multiple areas)
- `common/src/` (test HTML fixtures)
- `javascript/atoms/` (shared JS atoms; high blast radius)
- `scripts/`, `rake_tasks/`, `.github/`, `Rakefile` (tooling/build)
- `third_party/` treat as read-only
- `bazel-*/` treat as generated output

### Agent workspace
The `.local/` directory (gitignored) is available for generated artifacts or temporary files:
- Use `--output_base=.local/bazel-out` if bazel output directory restricted

## Cross-binding consistency checks
When changing user-visible behavior, compare with at least one other binding:
- Example: `rg <term> java/ py/ rb/ dotnet/ javascript/selenium-webdriver/`

If behavior is shared/low-level (protocol, serialization, "remote"/transport), suggest follow-up parity work or to file an issue

## Testing
When implementing solutions prefer writing a test for it first 
Prefer small (unit) tests over browser tests for speed/reliability
Avoid mocks—they can misrepresent API contracts

Useful flags:
- `--test_size_filters=small` (unit tests only)
- `--test_output=all` (display console output)
- `--cache_test_results=no` (force re-run)
See language-specific AGENTS.md for applicable testing usage

## Logging
Add logging where users may need insight into what's happening
See language-specific AGENTS.md for applicable logging usage

## Deprecation policy
This project does not follow semantic versioning (semver); before removing public functionality, mark it as deprecated with a message pointing to the alternative.
See language-specific AGENTS.md for applicable deprecation usage

## General Guidelines
- Comments should explain *why*, not *what* - prefer well-named methods over comments
- PRs should focus on one thing; we squash PRs to default `trunk` branch
- Prefer copying files to deleting and recreating to maintain git history
- Avoid running `bazel clean --expunge`
- Run or suggest running `./scripts/format.sh` or `./go all:lint` before pushing to prevent CI failures

## High risk changes (request verification before modifying unless explicitly instructed)
- Everything referenced above as high risk
- WebDriver/BiDi semantics, capability parsing, wire-level behavior
- Dependency updates / `MODULE.bazel` / repin flows
- Grid routing/distributor/queue logic

## After making code changes
- Call out any high risk areas touched
- Note cross-binding impact and any follow-up issues needed

```

### File: CLAUDE.local.md
```md
@.local/AGENTS.md

```

### File: CLAUDE.md
```md
@AGENTS.md

```

### File: CONTRIBUTING.md
```md
# Contributing to Selenium

The Selenium project welcomes contributions from everyone. There are a
number of ways you can help:

## Bug Reports

When opening new issues or commenting on existing issues please make
sure discussions are related to concrete technical issues with the
Selenium software.

It's imperative that issue reports outline the steps to reproduce
the defect. If the issue can't be reproduced it will be closed.
Please provide [concise reproducible test cases](http://sscce.org/)
and describe what results you are seeing and what results you expect.

Issues shouldn't be used for support. To raise a bug, please go to the
[Issue tracker](https://github.com/SeleniumHQ/selenium/issues).
Discussion of high level project ideas or non-technical topics should
move to the Selenium [Slack channel](https://inviter.co/seleniumhq).

We also need help with triaging
[issues that needs investigation](https://github.com/SeleniumHQ/selenium/labels/I-needs%20investigation).
This means asking the right questions, procuring the right information
to properly debug and verify the issue, and bisecting a commit range if
the issue is a regression.

## Feature Requests

If you find that Selenium is missing something, feel free to open an issue
with details describing what feature(s) you'd like added or changed.

If you'd like a hand at trying to implement the feature yourself, please refer to the [Code Contributions](#code-contributions) section of the document.

## Documentation

Selenium is a big software project and documentation is key to
understanding how things work and learning effective ways to exploit
its potential.

The [seleniumhq.github.io](https://github.com/SeleniumHQ/seleniumhq.github.io/)
repository contains both Selenium’s site and documentation. This is an ongoing effort (not targeted
at any specific release) to provide updated information on how to use Selenium effectively, how to
get involved and how to contribute to Selenium.

The official documentation of Selenium is at https://selenium.dev/documentation/. More details on
how to get involved and contribute, please check the site's and
documentation [contributing guidelines](https://www.selenium.dev/documentation/about/contributing/).

## Code Contributions

The Selenium project welcomes new contributors. Individuals making
significant and valuable contributions over time are made _Committers_
and given commit-access to the project.

If you're looking for easy bugs, have a look at
[issues labelled: `good first issue`](https://github.com/SeleniumHQ/selenium/issues?q=is%3Aopen%20is%3Aissue%20label%3A%22good%20first%20issue%22)
on Github.

This document will guide you through the contribution process.

### Step 1: Fork & Clone

Fork the project [on Github](https://github.com/seleniumhq/selenium)
and clone the repository locally. Use `--depth 1` for a quick clone.
The repository is over 2GB and cloning the whole history takes a while.

```shell
% git clone git@github.com:username/selenium.git --depth 1
% cd selenium
% git remote add upstream git://github.com/seleniumhq/selenium.git
```

#### Dependencies

We bundle dependencies in the _third-party/_ directory that are not
part of the proper project. Any changes to files in this directory or
its subdirectories should be sent upstream to the respective projects.
Please don't send your patch to us as we cannot accept it.

We do accept help in upgrading our existing dependencies or removing
superfluous dependencies. If you need to add a new dependency it's
often a good idea to reach out to the committers on the
[IRC channel or the mailing list](https://github.com/SeleniumHQ/selenium/blob/trunk/CONTRIBUTING.md#communication)
to check that your approach aligns with the project's
ideas. Nothing is more frustrating than seeing your hard work go to
waste because your vision doesn't align with the project's.

#### Dependencies Managed by Bazel

##### Java

Edit `MODULE.bazel`, and either update or add the dependency you want
using the regular maven coordinates to the `maven.install` with the
name `maven`. Once done, run `REPIN=1 bazel run @maven//:pin` to
update the lock file, create a PR and check the change in.

##### JS

We use `pnpm` for JS development in the project, and we also use [pnpm
workspaces](https://pnpm.io/workspaces). Take a look at the top-level
`pnpm-workspace.yaml` file to find them all, but the main thing to
know is that each of the workspaces has its own `package.json`. You
can add dependencies to specific workspaces either by using `pnpm`
installed on your local machine, or by executing:

```shell
# Example of adding a dep to the JS webdriver bindings 
cd javascript/selenium-webdriver
bazel run javascript:pnpm -- install my-amazing-dep --dir $PWD
```

This will install the dependency using the same version of `pnpm` we
build the project with for a single JS project.

To update all dependencies in the tree to the latest version:

`bazel run javascript:pnpm -- -r up --dir $PWD`

This will also update the lock file, so once a change is made, create
a PR and commit all the changed files.

#### License Headers

Every file in the Selenium project must carry the following license
header boilerplate:

```text
Licensed to the Software Freedom Conservancy (SFC) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The SFC licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
```

There's no need to include a copyright statement in the file's header.
The copyright attributions can be reviewed in the
[NOTICE](https://github.com/SeleniumHQ/selenium/blob/trunk/NOTICE)
file found in the top-level directory.

### Step 2: Branch

Create a feature branch and start hacking:

```shell
% git checkout -b my-feature-branch
```

We practice HEAD-based development, which means all changes are applied
directly on top of trunk.

### Step 3: Commit

First make sure git knows your name and email address:

```shell
% git config --global user.name 'Santa Claus'
% git config --global user.email 'santa@example.com'
```

**Writing good commit messages is important.** A commit message
should describe what changed, why, and reference issues fixed (if
any). Follow these guidelines when writing one:

1. The first line should be around 50 characters or less and contain a
    short description of the change.
2. Keep the second line blank.
3. Wrap all other lines at 72 columns.
4. Include `Fixes #N`, where _N_ is the issue number the commit
    fixes, if any.

A good commit message can look like this:

```text
explain commit normatively in one line

Body of commit message is a few lines of text, explaining things
in more detail, possibly giving some background about the issue
being fixed, etc.

The body of the commit message can be several paragraphs, and
please do proper word-wrap and keep columns shorter than about
72 characters or so. That way `git log` will show things
nicely even when it is indented.

Fixes #141
```

The first line must be meaningful as it's what people see when they
run `git shortlog` or `git log --oneline`.

### Step 4: Rebase

Use `git rebase` (not `git merge`) to sync your work from time to time.

```shell
% git fetch upstream
% git rebase upstream/trunk
```

### Step 5: Test

Bug fixes and features **should have tests**. Look at other tests to
see how they should be structured. Verify that new and existing tests are
passing locally before pushing code.

#### Running tests locally

Build your code for the latest changes and run tests locally.

##### Python
<details>
  <summary>
    Click to see How to run Python Tests.
  </summary>

  It's not mandatory to run tests sequentially but running Unit tests
  before browser testing is recommended.

  Unit Tests
  ```shell
  % bazel test //py:unit
  ```

  Remote Tests
  ```shell
  % bazel test --jobs 1 //py:test-remote
  ```

  Browser Tests
  ```shell
  % bazel test //py:test-<browsername> #eg test-chrome, test-firefox
  ```
</details>

##### Javascript
<details>
  <summary>
    Click to see How to run JavaScript Tests.
  </summary>

  Node Tests
  ```shell
  % bazel test //javascript/selenium-webdriver:all
  ```

  Firefox Atom Tests
  ```shell
  % bazel test --test_tag_filters=firefox //javascript/atoms/... //javascript/webdriver/...
  ```

  Grid UI Unit Tests
  ```shell
  % cd javascript/grid-ui && npm install && npm test
  ```
</details>

##### Java
<details>
  <summary>
    Click to see How to run Java Tests.
  </summary>

  Small Tests
  ```shell
  % bazel test --cache_test_results=no --test_size_filters=small grid java/test/...
  ```

  Large Tests
  ```shell
  % bazel test --cache_test_results=no java/test/org/openqa/selenium/grid/router:large-tests
  ```

  Browser Tests
  ```shell
  bazel test --test_size_filters=small,medium --cache_test_results=no --test_tag_filters=-browser-test //java/...
  ```
</details>

##### Ruby

Please see https://github.com/SeleniumHQ/selenium#ruby for details about running
tests.

### Step 6: Push

```shell
% git push origin my-feature-branch
```

Go to https://github.com/yourusername/selenium.git and press the _Pull
Request_ and fill out the form.

Pull requests are usually reviewed within a few days. If there are
comments to address, apply your changes in new commits (preferably
[fixups](http://git-scm.com/docs/git-commit)) and push to the same
branch.

### Step 7: Integration

When code review is complete, a committer will take your PR and
integrate it on Selenium's trunk branch. Because we like to keep a
linear history on the trunk branch, we will normally squash and rebase
your branch history.

## Stages of an Issue or PR

From your create your issue or pull request, through code review and
towards integration, it will be assigned different Github labels. The
labels serve for the committers to more easily keep track of work
that's pending or awaiting action.

Component labels are yellow and carry the **C** prefix. They highlight
the subsystem or component your PR makes changes in.

The driver labels (**D**) indicate if the changes are related to a
WebDriver implementation or the Selenium atoms.

The review labels (**R**) are:

* **awaiting answer**: awaits an answer from you
* **awaiting merge**: waits for a committer to integrate the PR
* **awaiting reviewer**: pending code review
* **blocked on external**: a change in an upstream repo is required
* **needs code changes**: waiting for you to fix a review issue
* **needs rebase**: the branch isn't in sync with trunk and needs to
    be rebased

Issues are labelled to make them easier to categorise and find by:

* which **component** they relate to (java, cpp, dotnet, py, rb, nodejs)
* which **driver** is affected
* their presumed **difficulty** (easy, less easy, hard)
* what **type** of issue they are (defect, race condition, cleanup)

## Communication

Selenium contributors frequent the `#selenium` channel on
[`libera.chat`](https://web.libera.chat/). You can also join
the [`selenium-developers@` mailing list](https://groups.google.com/forum/#!forum/selenium-developers).
Check https://selenium.dev/support/ for a complete list of options to communicate.

## Using the EngFlow RBE

To access the EngFlow RBE, a developer needs to be granted access to our project
container repository. Once that has been done, then any bazel command can be run
remotely by using `--config=rbe`. For example: `bazel build --config=rbe
grid` or `bazel test --config=rbe java/test/...`

When you run a remote build, one of the first lines of output from Bazel will 
include a link to the EngFlow UI so you can track the progress of the build and
gather information about the efficiency of the build.

```

### File: generate_web_code.sh
```sh
#!/usr/bin/env bash

# copy website to build
cp -R common/src/web build

# switch to gh-pages and copy the files
git checkout gh-pages || exit
# make sure that our local version is up to date.
git pull || exit

rm -rf web
mv build/web web

git add -A web

read -p "Do you want to commit the changes? (Y/n):" changes </dev/tty

if [ -z $changes ]; then
  changes=Y
fi

case "$changes" in
Y | y) echo "" ;;
N | n) exit ;;
*) exit ;;
esac

echo "Committing changes"
git commit -am "updating test website code"

echo "pushing to origin gh-pages"
git push origin gh-pages

echo "switching back to trunk branch"
git checkout trunk

```

### File: multitool.lock.json
```json
{
  "$schema": "https://raw.githubusercontent.com/theoremlp/rules_multitool/main/lockfile.schema.json",
  "shellcheck": {
    "binaries": [
      {
        "kind": "archive",
        "url": "https://github.com/koalaman/shellcheck/releases/download/v0.11.0/shellcheck-v0.11.0.linux.aarch64.tar.xz",
        "file": "shellcheck-v0.11.0/shellcheck",
        "sha256": "12b331c1d2db6b9eb13cfca64306b1b157a86eb69db83023e261eaa7e7c14588",
        "os": "linux",
        "cpu": "arm64"
      },
      {
        "kind": "archive",
        "url": "https://github.com/koalaman/shellcheck/releases/download/v0.11.0/shellcheck-v0.11.0.linux.x86_64.tar.xz",
        "file": "shellcheck-v0.11.0/shellcheck",
        "sha256": "8c3be12b05d5c177a04c29e3c78ce89ac86f1595681cab149b65b97c4e227198",
        "os": "linux",
        "cpu": "x86_64"
      },
      {
        "kind": "archive",
        "url": "https://github.com/koalaman/shellcheck/releases/download/v0.11.0/shellcheck-v0.11.0.darwin.aarch64.tar.xz",
        "file": "shellcheck-v0.11.0/shellcheck",
        "sha256": "56affdd8de5527894dca6dc3d7e0a99a873b0f004d7aabc30ae407d3f48b0a79",
        "os": "macos",
        "cpu": "arm64"
      },
      {
        "kind": "archive",
        "url": "https://github.com/koalaman/shellcheck/releases/download/v0.11.0/shellcheck-v0.11.0.darwin.x86_64.tar.xz",
        "file": "shellcheck-v0.11.0/shellcheck",
        "sha256": "3c89db4edcab7cf1c27bff178882e0f6f27f7afdf54e859fa041fca10febe4c6",
        "os": "macos",
        "cpu": "x86_64"
      },
      {
        "kind": "archive",
        "url": "https://github.com/koalaman/shellcheck/releases/download/v0.11.0/shellcheck-v0.11.0.zip",
        "file": "shellcheck.exe",
        "sha256": "8a4e35ab0b331c85d73567b12f2a444df187f483e5079ceffa6bda1faa2e740e",
        "os": "windows",
        "cpu": "x86_64"
      }
    ]
  },
  "actionlint": {
    "binaries": [
      {
        "kind": "archive",
        "url": "https://github.com/rhysd/actionlint/releases/download/v1.7.11/actionlint_1.7.11_linux_arm64.tar.gz",
        "file": "actionlint",
        "sha256": "21bc0dfb57a913fe175298c2a9e906ee630f747cb66d0a934d0d4b69f4ee1235",
        "os": "linux",
        "cpu": "arm64"
      },
      {
        "kind": "archive",
        "url": "https://github.com/rhysd/actionlint/releases/download/v1.7.11/actionlint_1.7.11_linux_amd64.tar.gz",
        "file": "actionlint",
        "sha256": "900919a84f2229bac68ca9cd4103ea297abc35e9689ebb842c6e34a3d1b01b0a",
        "os": "linux",
        "cpu": "x86_64"
      },
      {
        "kind": "archive",
        "url": "https://github.com/rhysd/actionlint/releases/download/v1.7.11/actionlint_1.7.11_darwin_arm64.tar.gz",
        "file": "actionlint",
        "sha256": "a21ba7366d8329e7223faee0ed69eb13da27fe8acabb356bb7eb0b7f1e1cb6d8",
        "os": "macos",
        "cpu": "arm64"
      },
      {
        "kind": "archive",
        "url": "https://github.com/rhysd/actionlint/releases/download/v1.7.11/actionlint_1.7.11_darwin_amd64.tar.gz",
        "file": "actionlint",
        "sha256": "17ffc17fed8f0258ef6ad4aed932d3272464c7ef7d64e1cb0d65aa97c9752107",
        "os": "macos",
        "cpu": "x86_64"
      },
      {
        "kind": "archive",
        "url": "https://github.com/rhysd/actionlint/releases/download/v1.7.11/actionlint_1.7.11_windows_amd64.zip",
        "file": "actionlint.exe",
        "sha256": "5414b7124a91f4b5abee62e5c9d84802237734f8d15b9b7032732a32c3ebffa3",
        "os": "windows",
        "cpu": "x86_64"
      }
    ]
  },
  "ruff": {
    "binaries": [
      {
        "kind": "archive",
        "url": "https://github.com/astral-sh/ruff/releases/download/0.15.8/ruff-aarch64-unknown-linux-musl.tar.gz",
        "file": "ruff-aarch64-unknown-linux-musl/ruff",
        "sha256": "15e6a6c21696bbe59c56d0f1c437452b960bcdfe81ecc3bc19fa89e6a7d70eb6",
        "os": "linux",
        "cpu": "arm64"
      },
      {
        "kind": "archive",
        "url": "https://github.com/astral-sh/ruff/releases/download/0.15.8/ruff-x86_64-unknown-linux-musl.tar.gz",
        "file": "ruff-x86_64-unknown-linux-musl/ruff",
        "sha256": "d541beae99d550ed4abb3a1d026b907886c7cdf44a533b24624871e3d8c81330",
        "os": "linux",
        "cpu": "x86_64"
      },
      {
        "kind": "archive",
        "url": "https://github.com/astral-sh/ruff/releases/download/0.15.8/ruff-aarch64-apple-darwin.tar.gz",
        "file": "ruff-aarch64-apple-darwin/ruff",
        "sha256": "94fc061f928c8f2b04c4b3a98aad2b1b04f38b4c808839bc5b33a2f0a63a47a3",
        "os": "macos",
        "cpu": "arm64"
      },
      {
        "kind": "archive",
        "url": "https://github.com/astral-sh/ruff/releases/download/0.15.8/ruff-x86_64-apple-darwin.tar.gz",
        "file": "ruff-x86_64-apple-darwin/ruff",
        "sha256": "153d1801068df606290e832058ce2e5601584ac302788a055d0390adf6c772ce",
        "os": "macos",
        "cpu": "x86_64"
      },
      {
        "kind": "archive",
        "url": "https://github.com/astral-sh/ruff/releases/download/0.15.8/ruff-x86_64-pc-windows-msvc.zip",
        "file": "ruff-x86_64-pc-windows-msvc/ruff.exe",
        "sha256": "1e6ebd021dc9cefa8b9f15b5d6500c275ec49a0f2da968824845c34f30060c78",
        "os": "windows",
        "cpu": "x86_64"
      }
    ]
  }
}

```

### File: pnpm-workspace.yaml
```yaml
packages:
  - 'javascript/atoms'
  - 'javascript/grid-ui'
  - 'javascript/private'
  - 'javascript/selenium-webdriver'

```

### File: renovate.json
```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": ["config:recommended"],
  "packageRules": [
    {
      "matchManagers": [ "bazel", "bazel-module", "bazelisk" ],
      "matchPackageNames": [ "!rules_java", "!rules_jvm_external", "!contrib_rules_jvm", "!rules_dotnet", "!aspect_rules_js", "!aspect_rules_ts", "!rules_nodejs", "!rules_python", "!rules_ruby", "!rules_cc" ],
      "matchDatasources": [ "!maven" ],
      "commitMessagePrefix": "[dotnet][java][js][py][rb][rust]",
      "labels": [ "dependencies", "c-build" ]
    },
    {
      "matchManagers": [ "nuget" ],
      "commitMessagePrefix": "[dotnet]",
      "labels": [ "dependencies", "c-dotnet" ]
    },
    {
      "matchPackageNames": [ "rules_dotnet" ],
      "commitMessagePrefix": "[dotnet]",
      "labels": [ "dependencies", "c-dotnet" ]
    },
    {
      "matchManagers": [ "bazel", "bazel-module" ],
      "matchDatasources": ["maven"],
      "versioning": "maven",
      "commitMessagePrefix": "[java]",
      "labels": [ "dependencies", "c-java" ]
    },
    {
      "matchManagers": [ "bazel-module" ],
      "matchPackageNames": [ "rules_java", "rules_jvm_external", "contrib_rules_jvm" ],
      "commitMessagePrefix": "[java]",
      "labels": [ "dependencies", "c-java" ]
    },
    {
      "matchManagers": [ "maven" ],
      "commitMessagePrefix": "[java]",
      "labels": [ "dependencies", "c-java" ]
    },
    {
      "matchManagers": [ "npm" ],
      "rangeStrategy": "bump",
      "commitMessagePrefix": "[js]",
      "labels": [ "dependencies", "c-nodejs" ]
    },
    {
      "matchPackageNames": [ "aspect_rules_js", "aspect_rules_ts", "rules_nodejs" ],
      "commitMessagePrefix": "[js]",
      "labels": [ "dependencies", "c-nodejs" ]
    },
    {
      "matchManagers": [ "pip_requirements", "pip_setup" ],
      "commitMessagePrefix": "[py]",
      "labels": [ "dependencies", "c-py" ]
    },
    {
      "matchPackageNames": [ "rules_python" ],
      "commitMessagePrefix": "[py]",
      "labels": [ "dependencies", "c-py" ]
    },
    {
      "matchManagers": [ "bundler", "ruby-version" ],
      "commitMessagePrefix": "[rb]",
      "labels": [ "dependencies", "c-rb" ]
    },
    {
      "matchPackageNames": [ "rules_ruby" ],
      "commitMessagePrefix": "[rb]",
      "labels": [ "dependencies", "c-rb" ]
    },
    {
      "matchManagers": [ "cargo" ],
      "rangeStrategy": "bump",
      "commitMessagePrefix": "[rust]",
      "labels": [ "dependencies", "c-rust" ]
    },
    {
      "matchPackageNames": [ "rules_cc" ],
      "commitMessagePrefix": "[rust]",
      "labels": [ "dependencies", "c-rust" ]
    }
  ],
  "prConcurrentLimit": 10
}

```

### File: .devcontainer\devcontainer.json
```json
// https://containers.dev/implementors/json_reference/

{
  "name": "selenium-devcontainer",
  "build": {
    "dockerfile": "../scripts/dev-image/Dockerfile"
  },
  "runArgs": ["--name", "selenium_devcontainer"]
}

```

### File: .github\copilot-instructions.md
```md
Always read AGENTS.md before answering

```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
<!-- Thanks for Contributing to Selenium! -->
<!-- Please read our contribution guidelines: https://github.com/SeleniumHQ/selenium/blob/trunk/CONTRIBUTING.md -->

### 🔗 Related Issues
<!-- Example: Fixes #1234 or Closes #5678 -->
<!-- If the reason for this PR is not obvious, consider creating an issue for it first -->

### 💥 What does this PR do?
<!-- Describe what this change includes and how it works -->

### 🔧 Implementation Notes
<!--- Why did you implement it this way? -->
<!--- What alternatives to this approach did you consider? -->

### 💡 Additional Considerations
<!--- Are there any decisions that need to be made before accepting this PR? -->
<!--- Is there any follow-on work that needs to be done? (e.g., docs, tests, etc.) -->

### 🔄 Types of changes
<!-- ✂️ Please delete anything that doesn't apply -->
- Cleanup (formatting, renaming)
- Bug fix (backwards compatible)
- New feature (non-breaking change which adds functionality *and tests!*)
- Breaking change (fix or feature that would cause existing functionality to change)

```

### File: .github\renovate.json
```json
{
  "labels": [
    "B-dependencies"
  ],
  "docker": {
    "enabled": false
  },
  "packageRules": [
    {
      "matchDatasources": [
        "docker"
      ],
      "enabled": false
    },
    {
      "matchPackagePatterns": [
        "^docker:",
        "^gcr.io/",
        "^registry.k8s.io/",
        "^quay.io/",
        "^ghcr.io/"
      ],
      "enabled": false
    }
  ]
}

```

### File: java\AGENTS.md
```md
<!-- Guidance for AI agents working in Selenium Java Bindings and Grid. -->

## Code location
- Java Bindings: `java/src/`, `java/test/`
- Grid Server: `java/src/org/openqa/selenium/grid/`

## Common commands
- Build: `bazel build //java/...`
- Build Grid: `bazel build grid`

## Testing
See `java/TESTING.md`

## Code conventions

### Logging
```java
import java.util.logging.Logger;
private static final Logger LOG = Logger.getLogger(MyClass.class.getName());

LOG.warning("actionable: something needs attention");
LOG.info("useful: server started on port 4444");
LOG.fine("diagnostic: request details for debugging");
```

### Deprecation
```java
@Deprecated(forRemoval = true)
public void legacyMethod() { }
```

### Documentation
Use Javadoc for public APIs:
```java
/**
 * Brief description.
 *
 * @param name description
 * @return description
 * @throws ExceptionType when condition
 */
```

```

### File: java\empty_test_template.txt
```txt

```

### File: java\java_stub_template.txt
```txt
#!/usr/bin/env bash
# Copyright 2014 The Bazel Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This script was generated from java_stub_template.txt.  Please
# don't edit it directly.
#
# If present, these flags should either be at the beginning of the command
# line, or they should be wrapped in a --wrapper_script_flag=FLAG argument.
#
# --debug               Launch the JVM in remote debugging mode listening
# --debug=<port>        to the specified port or the port set in the
#                       DEFAULT_JVM_DEBUG_PORT environment variable (e.g.
#                       'export DEFAULT_JVM_DEBUG_PORT=8000') or else the
#                       default port of 5005.  The JVM starts suspended
#                       unless the DEFAULT_JVM_DEBUG_SUSPEND environment
#                       variable is set to 'n'.
# --main_advice=<class> Run an alternate main class with the usual main
#                       program and arguments appended as arguments.
# --main_advice_classpath=<classpath>
#                       Prepend additional class path entries.
# --jvm_flag=<flag>     Pass <flag> to the "java" command itself.
#                       <flag> may contain spaces. Can be used multiple times.
# --jvm_flags=<flags>   Pass space-separated flags to the "java" command
#                       itself. Can be used multiple times.
# --singlejar           Start the program from the packed-up deployment
#                       jar rather than from the classpath.
# --print_javabin       Print the location of java executable binary and exit.
# --classpath_limit=<length>
#                       Specify the maximum classpath length. If the classpath
#                       is shorter, this script passes it to Java as a command
#                       line flag, otherwise it creates a classpath jar.
#
# The remainder of the command line is passed to the program.

set -o posix

# Make it easy to insert 'set -x' or similar commands when debugging problems with this script.
eval "$JAVA_STUB_DEBUG"

# Prevent problems where the caller has exported CLASSPATH, causing our
# computed value to be copied into the environment and double-counted
# against the argv limit.
unset CLASSPATH

JVM_FLAGS_CMDLINE=()

# Processes an argument for the wrapper. Returns 0 if the given argument
# was recognized as an argument for this wrapper, and 1 if it was not.
function process_wrapper_argument() {
  case "$1" in
    --debug) JVM_DEBUG_PORT="${DEFAULT_JVM_DEBUG_PORT:-5005}" ;;
    --debug=*) JVM_DEBUG_PORT="${1#--debug=}" ;;
    --main_advice=*) MAIN_ADVICE="${1#--main_advice=}" ;;
    --main_advice_classpath=*) MAIN_ADVICE_CLASSPATH="${1#--main_advice_classpath=}" ;;
    --jvm_flag=*) JVM_FLAGS_CMDLINE+=( "${1#--jvm_flag=}" ) ;;
    --jvm_flags=*) JVM_FLAGS_CMDLINE+=( ${1#--jvm_flags=} ) ;;
    --singlejar) SINGLEJAR=1 ;;
    --print_javabin) PRINT_JAVABIN=1 ;;
    --classpath_limit=*)
        CLASSPATH_LIMIT="${1#--classpath_limit=}"
        echo "$CLASSPATH_LIMIT" | grep -q '^[0-9]\+$' || \
          die "ERROR: $self failed, --classpath_limit is not a number"
        ;;
    *)
      return 1 ;;
  esac
  return 0
}

die() {
  printf "%s: $1\n" "$0" "${@:2}" >&2
  exit 1
}

# Windows
function is_windows() {
  [[ "${OSTYPE}" =~ msys* ]] || [[ "${OSTYPE}" =~ cygwin* ]]
}

# macOS
function is_macos() {
  [[ "${OSTYPE}" =~ darwin* ]]
}

# Parse arguments sequentially until the first unrecognized arg is encountered.
# Scan the remaining args for --wrapper_script_flag=X options and process them.
ARGS=()
for ARG in "$@"; do
  if [[ "$ARG" == --wrapper_script_flag=* ]]; then
    process_wrapper_argument "${ARG#--wrapper_script_flag=}" \
      || die "invalid wrapper argument '%s'" "$ARG"
  elif [[ "${#ARGS}" -gt 0 ]] || ! process_wrapper_argument "$ARG"; then
    ARGS+=( "$ARG" )
  fi
done

# Find our runfiles tree.  We need this to construct the classpath
# (unless --singlejar was passed).
#
# Call this program X.  X was generated by a java_binary or java_test rule.
# X may be invoked in many ways:
#   1a) directly by a user, with $0 in the output tree
#   1b) via 'bazel run' (similar to case 1a)
#   2) directly by a user, with $0 in X's runfiles tree
#   3) by another program Y which has a data dependency on X, with $0 in Y's runfiles tree
#   4) via 'bazel test'
#   5) by a genrule cmd, with $0 in the output tree
#   6) case 3 in the context of a genrule
#
# For case 1, $0 will be a regular file, and the runfiles tree will be
# at $0.runfiles.
# For case 2, $0 will be a symlink to the file seen in case 1.
# For case 3, we use Y's runfiles tree, which will be a superset of X's.
# For case 4, $JAVA_RUNFILES and $TEST_SRCDIR should already be set.
# Case 5 is handled like case 1.
# Case 6 is handled like case 3.

# If we are running on Windows, convert the windows style path
# to unix style for detecting runfiles path.
if is_windows; then
  self=$(cygpath --unix "$0")
else
  self="$0"
fi

if [[ "$self" != /* ]]; then
  self="$PWD/$self"
fi

if [[ "$SINGLEJAR" != 1 || "%needs_runfiles%" == 1 ]]; then
  if [[ -z "$JAVA_RUNFILES" ]]; then
    while true; do
      if [[ -e "$self.runfiles" ]]; then
        JAVA_RUNFILES="$self.runfiles"
        break
      fi
      if [[ $self == *.runfiles/* ]]; then
        JAVA_RUNFILES="${self%.runfiles/*}.runfiles"
        break
      fi
      if [[ ! -L "$self" ]]; then
        break
      fi
      readlink="$(readlink "$self")"
      if [[ "$readlink" = /* ]]; then
        self="$readlink"
      else
        # resolve relative symlink
        self="${self%/*}/$readlink"
      fi
    done
    if [[ -n "$JAVA_RUNFILES" ]]; then
      export TEST_SRCDIR=${TEST_SRCDIR:-$JAVA_RUNFILES}
    elif [[ -f "${self}_deploy.jar" && "%needs_runfiles%" == 0 ]]; then
      SINGLEJAR=1;
    else
      die 'Cannot locate runfiles directory. (Set $JAVA_RUNFILES to inhibit searching.)'
    fi
  fi
fi

# If we are running on Windows, we need a windows style runfiles path for constructing CLASSPATH
if is_windows; then
  JAVA_RUNFILES=$(cygpath --windows "$JAVA_RUNFILES")
fi

export JAVA_RUNFILES
export RUNFILES_MANIFEST_FILE="${JAVA_RUNFILES}/MANIFEST"
export RUNFILES_MANIFEST_ONLY=%runfiles_manifest_only%

if [ -z "$RUNFILES_MANIFEST_ONLY" ]; then
  function rlocation() {
    if [[ "$1" = /* ]]; then
      echo $1
    else
      echo "$(dirname $RUNFILES_MANIFEST_FILE)/$1"
    fi
  }
else
  if ! is_macos; then
    # Read file into my_array
    oifs=$IFS
    IFS=$'\n'
    my_array=( $(sed -e 's/\r//g' "$RUNFILES_MANIFEST_FILE") )
    IFS=$oifs

    # Process each runfile line into a [key,value] entry in runfiles_array
    # declare -A is not supported on macOS because an old version of bash is used.
    declare -A runfiles_array
    for line in "${my_array[@]}"
    do
      line_split=($line)
      runfiles_array[${line_split[0]}]=${line_split[@]:1}
    done
  fi

  function rlocation() {
    if [[ "$1" = /* ]]; then
      echo $1
    else
      if is_macos; then
        # Print the rest of line after the first space
        # First, set the first column to empty and print rest of the line
        # Second, use a trick of awk to remove leading and trailing spaces.
        echo $(grep "^$1 " $RUNFILES_MANIFEST_FILE | awk '{ $1=""; print }' | awk '{ $1=$1; print }')
      else
        echo ${runfiles_array[$1]}
      fi
    fi
  }
fi

if is_macos || [[ ${OSTYPE} == "freebsd" ]]; then
  function md5func() { md5 -q $@ ; }
else
  function md5func() { md5sum $@ | awk '{print $1}' ; }
fi

# Set JAVABIN to the path to the JVM launcher.
%javabin%

if [[ "$PRINT_JAVABIN" == 1 || "%java_start_class%" == "--print_javabin" ]]; then
  echo -n "$JAVABIN"
  exit 0
fi

if [[ "$SINGLEJAR" == 1 ]]; then
  CLASSPATH="${self}_deploy.jar"
  # Check for the deploy jar now.  If it doesn't exist, we can print a
  # more helpful error message than the JVM.
  [[ -r "$CLASSPATH" ]] \
    || die "Option --singlejar was passed, but %s does not exist.\n  (You may need to build it explicitly.)" "$CLASSPATH"
else
  # Create the shortest classpath we can, by making it relative if possible.
  RUNPATH="${JAVA_RUNFILES}/%workspace_prefix%"
  RUNPATH="${RUNPATH#$PWD/}"
  CLASSPATH=%classpath%
fi

# Export the locations which will be used to find the location of the classes from the classpath file.
export SELF_LOCATION="$self"
export CLASSLOADER_PREFIX_PATH="${RUNPATH}"

# If using Jacoco in offline instrumentation mode, the CLASSPATH contains instrumented files.
# We need to make the metadata jar with uninstrumented classes available for generating
# the lcov-compatible coverage report, and we don't want it on the classpath.
%set_jacoco_metadata%
%set_jacoco_main_class%
%set_jacoco_java_runfiles_root%

if [[ -n "$JVM_DEBUG_PORT" ]]; then
  JVM_DEBUG_SUSPEND=${DEFAULT_JVM_DEBUG_SUSPEND:-"y"}
  JVM_DEBUG_FLAGS="-agentlib:jdwp=transport=dt_socket,server=y,suspend=${JVM_DEBUG_SUSPEND},address=${JVM_DEBUG_PORT}"

  if [[ "$PERSISTENT_TEST_RUNNER" == "true" ]]; then
    JVM_DEBUG_FLAGS+=",quiet=y"
  fi
fi

if [[ -n "$MAIN_ADVICE_CLASSPATH" ]]; then
  CLASSPATH="${MAIN_ADVICE_CLASSPATH}:${CLASSPATH}"
fi

# Check if TEST_TMPDIR is available to use for scratch.
if [[ -n "$TEST_TMPDIR" && -d "$TEST_TMPDIR" ]]; then
  JVM_FLAGS+=" -Djava.io.tmpdir=$TEST_TMPDIR"
fi

ARGS=(
  ${JVM_DEBUG_FLAGS}
  ${JVM_FLAGS}
  %jvm_flags%
  "${JVM_FLAGS_CMDLINE[@]}"
  ${MAIN_ADVICE}
  %java_start_class%
  "${ARGS[@]}")


function create_and_run_classpath_jar() {
  # Build class path as one single string separated by spaces
  MANIFEST_CLASSPATH=""
  if is_windows; then
    IFS=';'
    URI_PREFIX="file:/"  # e.g. "file:/C:/temp/foo.jar"
  else
    IFS=':'
    URI_PREFIX="file:$(pwd)/"  # e.g. "file:/usr/local/foo.jar"
  fi
  for x in $CLASSPATH; do
    # Add file:/ prefix and escaped space characters, it should be a URI.
    x="${URI_PREFIX}${x// /%20}"
    MANIFEST_CLASSPATH="$MANIFEST_CLASSPATH $x"
  done
  unset IFS

  # Create manifest file
  MANIFEST_FILE="$(mktemp -t XXXXXXXX.jar_manifest)"

  (
    echo "Manifest-Version: 1.0"
    CLASSPATH_LINE="Class-Path:$MANIFEST_CLASSPATH"
    # No line in the MANIFEST.MF file may be longer than 72 bytes.
    # A space prefix indicates the line is still the content of the last attribute.
    for ((i = 0; i < "${#CLASSPATH_LINE}"; i += 71)); do
      PREFIX=" "
      if ((i == 0)); then
        PREFIX=""
      fi
      echo "$PREFIX${CLASSPATH_LINE:$i:71}"
    done
    echo "Created-By: Bazel"
  ) >$MANIFEST_FILE

  # Create classpath JAR file
  MANIFEST_JAR_FILE="$(mktemp -t XXXXXXXX-classpath.jar)"
  if is_windows; then
    MANIFEST_JAR_FILE="$(cygpath --windows "$MANIFEST_JAR_FILE")"
    MANIFEST_FILE="$(cygpath --windows "$MANIFEST_FILE")"
  fi
  JARBIN="${JARBIN:-$(rlocation "$1")}"
  $JARBIN cvfm "$MANIFEST_JAR_FILE" "$MANIFEST_FILE" >/dev/null || \
    die "ERROR: $self failed because $JARBIN failed"

  # Execute JAVA command
  $JAVABIN -classpath "$MANIFEST_JAR_FILE" "${ARGS[@]}"
  exit_code=$?
  rm -f "$MANIFEST_FILE"
  rm -f "$MANIFEST_JAR_FILE"
  exit $exit_code
}

# If the user didn't specify a --classpath_limit, use the default value.
if [ -z "$CLASSPATH_LIMIT" ]; then
  # Windows per-arg limit MAX_ARG_STRLEN == 8k
  # Linux per-arg limit MAX_ARG_STRLEN == 128k
  is_windows && CLASSPATH_LIMIT=7000 || CLASSPATH_LIMIT=120000
fi

if is_windows && (("${#CLASSPATH}" > ${CLASSPATH_LIMIT} )); then
  create_and_run_classpath_jar "local_jdk/bin/jar.exe"
elif (("${#CLASSPATH}" > ${CLASSPATH_LIMIT})); then
  create_and_run_classpath_jar "local_jdk/bin/jar"
else
  exec $JAVABIN -classpath $CLASSPATH "${ARGS[@]}"
fi

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

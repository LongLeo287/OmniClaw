---
id: node-gyp
type: knowledge
owner: OA_Triage
---
# node-gyp
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "@electron/node-gyp",
  "description": "Node.js native addon build tool",
  "license": "MIT",
  "keywords": [
    "native",
    "addon",
    "module",
    "c",
    "c++",
    "bindings",
    "gyp"
  ],
  "version": "10.2.0-electron.2",
  "installVersion": 11,
  "author": "Nathan Rajlich <nathan@tootallnate.net> (http://tootallnate.net)",
  "repository": {
    "type": "git",
    "url": "git://github.com/nodejs/node-gyp.git"
  },
  "preferGlobal": true,
  "bin": "./bin/node-gyp.js",
  "main": "./lib/node-gyp.js",
  "dependencies": {
    "env-paths": "^2.2.0",
    "exponential-backoff": "^3.1.1",
    "glob": "^8.1.0",
    "graceful-fs": "^4.2.6",
    "make-fetch-happen": "^10.2.1",
    "nopt": "^6.0.0",
    "proc-log": "^2.0.1",
    "semver": "^7.3.5",
    "tar": "^6.2.1",
    "which": "^2.0.2"
  },
  "engines": {
    "node": ">=12.13.0"
  },
  "devDependencies": {
    "bindings": "^1.5.0",
    "cross-env": "^7.0.3",
    "mocha": "^10.2.0",
    "nan": "^2.14.2",
    "require-inject": "^1.4.4",
    "standard": "^17.0.0"
  },
  "scripts": {
    "lint": "standard --write \"*/*.js\" \"test/**/*.js\" \".github/**/*.js\"",
    "test": "cross-env NODE_GYP_NULL_LOGGER=true mocha --timeout 15000 test/test-download.js test/test-*"
  }
}

```

### File: README.md
```md
# `node-gyp` - Node.js native addon build tool

This is a fork of the original and excellent `node-gyp` with only one feature added: Support for Node v12. The Electron maintainers took this step to ensure that our community can easily build their Electron apps on macOS Sequoia. Here is what happened:

- Python 3.12 has removed `distutils`, which `node-gyp` below v10 depended on.
- macOS Sequoia updated their default version of Python to 3.12.
- When installing a native Node addon, a lot of code bases suddenly showed `ModuleNotFoundError: No module named 'distutils'` error messages that are cryptic for anyone who doesn't have a full understanding of the dependency chain involved

This left the Electron maintainers with the following choices:

1. **Tell the community to manually install either Python 3.11 or `setuptools`**. While this fixes the issue, it requires manual user intervention and requires our users to first search for the error message.
2. **Upgrade to `node-gyp` v10**. That would have required a bump in minimum Node.js version for `@electron/rebuild` and in turn all other packages that depend on it, resulting in major version bumps across the entire ecosystem. This too doesn't fix the issue for our users without them performing manual major version upgrades.
3. **Fork node-gyp v10, make it compatible with Node.js v12, and only patch our tools**: We chose this option to get a fix out to our users as quickly and painless as possible.

Electron has a major version bump in required Node.js version on its roadmap. Once that is the case, we will sunset this fork and go back to the original `node-gyp`.

# Original Readme

[![Build Status](https://github.com/nodejs/node-gyp/workflows/Tests/badge.svg?branch=main)](https://github.com/nodejs/node-gyp/actions?query=workflow%3ATests+branch%3Amain)
![npm](https://img.shields.io/npm/dm/node-gyp)

`node-gyp` is a cross-platform command-line tool written in Node.js for
compiling native addon modules for Node.js. It contains a vendored copy of the
[gyp-next](https://github.com/nodejs/gyp-next) project that was previously used
by the Chromium team and extended to support the development of Node.js native
addons.

Note that `node-gyp` is _not_ used to build Node.js itself.

All current and LTS target versions of Node.js are supported. Depending on what version of Node.js is actually installed on your system
`node-gyp` downloads the necessary development files or headers for the target version. List of stable Node.js versions can be found on [Node.js website](https://nodejs.org/en/about/previous-releases).

## Features

 * The same build commands work on any of the supported platforms
 * Supports the targeting of different versions of Node.js

## Installation

> [!Important]
> Python >= v3.12 requires `node-gyp` >= v10

You can install `node-gyp` using `npm`:

``` bash
npm install -g node-gyp
```

Depending on your operating system, you will need to install:

### On Unix

   * [A supported version of Python](https://devguide.python.org/versions/)
   * `make`
   * A proper C/C++ compiler toolchain, like [GCC](https://gcc.gnu.org)

### On macOS

   * [A supported version of Python](https://devguide.python.org/versions/)
   * `Xcode Command Line Tools` which will install `clang`, `clang++`, and `make`.
     * Install the `Xcode Command Line Tools` standalone by running `xcode-select --install`. -- OR --
     * Alternatively, if you already have the [full Xcode installed](https://developer.apple.com/xcode/download/), you can install the Command Line Tools under the menu `Xcode -> Open Developer Tool -> More Developer Tools...`.


### On Windows

Install tools with [Chocolatey](https://chocolatey.org):
``` bash
choco install python visualstudio2022-workload-vctools -y
```

Or install and configure Python and Visual Studio tools manually:

  * Install the current [version of Python](https://devguide.python.org/versions/) from the
  [Microsoft Store](https://apps.microsoft.com/store/search?publisher=Python+Software+Foundation).

   * Install Visual C++ Build Environment: For Visual Studio 2019 or later, use the `Desktop development with C++` workload from [Visual Studio Community](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community).  For a version older than Visual Studio 2019, install [Visual Studio Build Tools](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools) with the `Visual C++ build tools` option.

   If the above steps didn't work for you, please visit [Microsoft's Node.js Guidelines for Windows](https://github.com/Microsoft/nodejs-guidelines/blob/master/windows-environment.md#compiling-native-addon-modules) for additional tips.

   To target native ARM64 Node.js on Windows on ARM, add the components "Visual C++ compilers and libraries for ARM64" and "Visual C++ ATL for ARM64".

   To use the native ARM64 C++ compiler on Windows on ARM, ensure that you have Visual Studio 2022 [17.4 or later](https://devblogs.microsoft.com/visualstudio/arm64-visual-studio-is-officially-here/) installed.

It's advised to install following Powershell module: [VSSetup](https://github.com/microsoft/vssetup.powershell) using `Install-Module VSSetup -Scope CurrentUser`.
This will make Visual Studio detection logic to use more flexible and accessible method, avoiding Powershell's `ConstrainedLanguage` mode.

### Configuring Python Dependency

`node-gyp` requires that you have installed a [supported version of Python](https://devguide.python.org/versions/).
If you have multiple versions of Python installed, you can identify which version
`node-gyp` should use in one of the following ways:

1. by setting the `--python` command-line option, e.g.:

``` bash
node-gyp <command> --python /path/to/executable/python
```

2. If `node-gyp` is called by way of `npm`, *and* you have multiple versions of
Python installed, then you can set the `npm_config_python` environment variable
to the appropriate path:
``` bash
export npm_config_python=/path/to/executable/python
```
&nbsp;&nbsp;&nbsp;&nbsp;Or on Windows:
```console
py --list-paths  # To see the installed Python versions
set npm_config_python=C:\path\to\python.exe  # CMD
$Env:npm_config_python="C:\path\to\python.exe"  # PowerShell
```

3. If the `PYTHON` environment variable is set to the path of a Python executable,
then that version will be used if it is a supported version.

4. If the `NODE_GYP_FORCE_PYTHON` environment variable is set to the path of a
Python executable, it will be used instead of any of the other configured or
built-in Python search paths. If it's not a compatible version, no further
searching will be done.

### Build for Third Party Node.js Runtimes

When building modules for third-party Node.js runtimes like Electron, which have
different build configurations from the official Node.js distribution, you
should use `--dist-url` or `--nodedir` flags to specify the headers of the
runtime to build for.

Also when `--dist-url` or `--nodedir` flags are passed, node-gyp will use the
`config.gypi` shipped in the headers distribution to generate build
configurations, which is different from the default mode that would use the
`process.config` object of the running Node.js instance.

Some old versions of Electron shipped malformed `config.gypi` in their headers
distributions, and you might need to pass `--force-process-config` to node-gyp
to work around configuration errors.

## How to Use

To compile your native addon first go to its root directory:

``` bash
cd my_node_addon
```

The next step is to generate the appropriate project build files for the current
platform. Use `configure` for that:

``` bash
node-gyp configure
```

Auto-detection fails for Visual C++ Build Tools 2015, so `--msvs_version=2015`
needs to be added (not needed when run by npm as configured above):
``` bash
node-gyp configure --msvs_version=2015
```

__Note__: The `configure` step looks for a `binding.gyp` file in the current
directory to process. See below for instructions on creating a `binding.gyp` file.

Now you will have either a `Makefile` (on Unix platforms) or a `vcxproj` file
(on Windows) in the `build/` directory. Next, invoke the `build` command:

``` bash
node-gyp build
```

Now you have your compiled `.node` bindings file! The compiled bindings end up
in `build/Debug/` or `build/Release/`, depending on the build mode. At this point,
you can require the `.node` file with Node.js and run your tests!

__Note:__ To create a _Debug_ build of the bindings file, pass the `--debug` (or
`-d`) switch when running either the `configure`, `build` or `rebuild` commands.

## The `binding.gyp` file

A `binding.gyp` file describes the configuration to build your module, in a
JSON-like format. This file gets placed in the root of your package, alongside
`package.json`.

A barebones `gyp` file appropriate for building a Node.js addon could look like:

```python
{
  "targets": [
    {
      "target_name": "binding",
      "sources": [ "src/binding.cc" ]
    }
  ]
}
```

## Further reading

The **[docs](./docs/)** directory contains additional documentation on specific node-gyp topics that may be useful if you are experiencing problems installing or building addons using node-gyp.

Some additional resources for Node.js native addons and writing `gyp` configuration files:

 * ["Going Native" a nodeschool.io tutorial](http://nodeschool.io/#goingnative)
 * ["Hello World" node addon example](https://github.com/nodejs/node/tree/main/test/addons/hello-world)
 * [gyp user documentation](https://gyp.gsrc.io/docs/UserDocumentation.md)
 * [gyp input format reference](https://gyp.gsrc.io/docs/InputFormatReference.md)
 * [*"binding.gyp" files out in the wild* wiki page](./docs/binding.gyp-files-in-the-wild.md)

## Commands

`node-gyp` responds to the following commands:

| **Command**   | **Description**
|:--------------|:---------------------------------------------------------------
| `help`        | Shows the help dialog
| `build`       | Invokes `make`/`msbuild.exe` and builds the native addon
| `clean`       | Removes the `build` directory if it exists
| `configure`   | Generates project build files for the current platform
| `rebuild`     | Runs `clean`, `configure` and `build` all in a row
| `install`     | Installs Node.js header files for the given version
| `list`        | Lists the currently installed Node.js header versions
| `remove`      | Removes the Node.js header files for the given version


## Command Options

`node-gyp` accepts the following command options:

| **Command**                       | **Description**
|:----------------------------------|:------------------------------------------
| `-j n`, `--jobs n`                | Run `make` in parallel. The value `max` will use all available CPU cores
| `--target=v6.2.1`                 | Node.js version to build for (default is `process.version`)
| `--silly`, `--loglevel=silly`     | Log all progress to console
| `--verbose`, `--loglevel=verbose` | Log most progress to console
| `--silent`, `--loglevel=silent`   | Don't log anything to console
| `debug`, `--debug`                | Make Debug build (default is `Release`)
| `--release`, `--no-debug`         | Make Release build
| `-C $dir`, `--directory=$dir`     | Run command in different directory
| `--make=$make`                    | Override `make` command (e.g. `gmake`)
| `--thin=yes`                      | Enable thin static libraries
| `--arch=$arch`                    | Set target architecture (e.g. ia32)
| `--tarball=$path`                 | Get headers from a local tarball
| `--devdir=$path`                  | SDK download directory (default is OS cache directory)
| `--ensure`                        | Don't reinstall headers if already present
| `--dist-url=$url`                 | Download header tarball from custom URL
| `--proxy=$url`                    | Set HTTP(S) proxy for downloading header tarball
| `--noproxy=$urls`                 | Set urls to ignore proxies when downloading header tarball
| `--cafile=$cafile`                | Override default CA chain (to download tarball)
| `--nodedir=$path`                 | Set the path to the node source code
| `--python=$path`                  | Set path to the Python binary
| `--msvs_version=$version`         | Set Visual Studio version (Windows only)
| `--solution=$solution`            | Set Visual Studio Solution version (Windows only)
| `--force-process-config`          | Force using runtime's `process.config` object to generate `config.gypi` file

## Configuration

### Environment variables

Use the form `npm_config_OPTION_NAME` for any of the command options listed
above (dashes in option names should be replaced by underscores).

For example, to set `devdir` equal to `/tmp/.gyp`, you would:

Run this on Unix:

```bash
export npm_config_devdir=/tmp/.gyp
```

Or this on Windows:

```console
set npm_config_devdir=c:\temp\.gyp
```

### `npm` configuration for npm versions before v9

Use the form `OPTION_NAME` for any of the command options listed above.

For example, to set `devdir` equal to `/tmp/.gyp`, you would run:

```bash
npm config set [--global] devdir /tmp/.gyp
```

**Note:** Configuration set via `npm` will only be used when `node-gyp`
is run via `npm`, not when `node-gyp` is run directly.

## License

`node-gyp` is available under the MIT license. See the [LICENSE
file](LICENSE) for details.

```

### File: docs\README.md
```md
## Versions of `node-gyp` that are earlier than v10.x.x

Please look thru your error log for the string `gyp info using node-gyp@` and if that version number is less than the [current release of node-gyp](https://github.com/nodejs/node-gyp/releases) then __please upgrade__ using [these instructions](https://github.com/nodejs/node-gyp/blob/main/docs/Updating-npm-bundled-node-gyp.md) and then try your command again.

## `node-sass` is deprecated

Please be aware that the package [`node-sass` is deprecated](https://github.com/sass/node-sass#node-sass) so you should actively seek alternatives.  You can try:
```
npm uninstall node-sass
npm install sass --save
# or ...
npm install --global node-sass@latest
```
`node-sass` projects _may_ work by downgrading to Node.js v14 but [that release is end-of-life](https://github.com/nodejs/release#release-schedule).

In any case, please avoid opening new `node-sass` issues on this repo because we [cannot help much](https://github.com/nodejs/node-gyp/issues?q=is%3Aissue+label%3A%22Node+Sass+--%3E+Dart+Sass%22+).

## `node-pre-gyp` is no longer maintained

* mapbox/node-pre-gyp#657

Support in the `abi_crosswalk.json` file ends at Node.js v17 but [that release is end-of-life](https://github.com/nodejs/release#release-schedule).

In any case, please avoid opening new `node-pre-gyp` issues on this repo because we [cannot help much](https://github.com/nodejs/node-gyp/issues?q=is%3Aissue+label%3A%22node-pre-gyp+is+unmaintained%22).

Unsupported __WORKAROUND__ for versions of Node.js > v17
```
npm ci  # mapbox/node-pre-gyp
npm run update-crosswalk
# npm audit  # Currently fails on a `Severity: critical` issue
```

```

### File: gyp\README.md
```md
GYP can Generate Your Projects.
===================================

Documents are available at [`./docs`](./docs).

__gyp-next__ is [released](https://github.com/nodejs/gyp-next/releases) to the [__Python Packaging Index__](https://pypi.org/project/gyp-next) (PyPI) and can be installed with the command:
* `python3 -m pip install gyp-next`

When used as a command line utility, __gyp-next__ can also be installed with [pipx](https://pypa.github.io/pipx):
* `pipx install gyp-next`
```
Installing to a new venv 'gyp-next'
  installed package gyp-next 0.13.0, installed using Python 3.10.6
  These apps are now globally available
    - gyp
done! ✨ 🌟 ✨
```

Or to run __gyp-next__ directly without installing it:
* `pipx run gyp-next --help`
```
NOTE: running app 'gyp' from 'gyp-next'
usage: usage: gyp [options ...] [build_file ...]

options:
  -h, --help            show this help message and exit
  --build CONFIGS       configuration for build after project generation
  --check               check format of gyp files
  [ ... ]
```

```

### File: gyp\docs\README.md
```md
# Generate Your Projects (gyp-next)

GYP is a Meta-Build system: a build system that generates other build systems.

* [User documentation](./UserDocumentation.md)
* [Input Format Reference](./InputFormatReference.md)
* [Language specification](./LanguageSpecification.md)
* [Hacking](./Hacking.md)
* [Testing](./Testing.md)
* [GYP vs. CMake](./GypVsCMake.md)

GYP is intended to support large projects that need to be built on multiple
platforms (e.g., Mac, Windows, Linux), and where it is important that
the project can be built using the IDEs that are popular on each platform
as if the project is a "native" one.

It can be used to generate XCode projects, Visual Studio projects, Ninja
build files, and Makefiles. In each case GYP's goal is to replicate as
closely as possible the way one would set up a native build of the project
using the IDE.

GYP can also be used to generate "hybrid" projects that provide the IDE
scaffolding for a nice user experience but call out to Ninja to do the actual
building (which is usually much faster than the native build systems of the
IDEs).

For more information on GYP, click on the links above.

```

### File: .release-please-manifest.json
```json
{
    ".": "10.2.0"
}

```

### File: CHANGELOG.md
```md
# Changelog

## [10.2.0](https://github.com/nodejs/node-gyp/compare/v10.1.0...v10.2.0) (2024-07-09)


### Features

* allow VCINSTALLDIR to specify a portable instance ([#3036](https://github.com/nodejs/node-gyp/issues/3036)) ([d38af2e](https://github.com/nodejs/node-gyp/commit/d38af2e0c2a81b12cd221b1f8517fb89e609d62c))
* **gyp:** update gyp to v0.18.1 ([#3039](https://github.com/nodejs/node-gyp/issues/3039)) ([ea99fea](https://github.com/nodejs/node-gyp/commit/ea99fea83485dc5be04db01df9b2fdbe05319b8e))
* support `rebuild` and `build` for cross-compiling Node-API module to wasm on Windows ([#2974](https://github.com/nodejs/node-gyp/issues/2974)) ([6318d2b](https://github.com/nodejs/node-gyp/commit/6318d2b210224415ff5932c2863e6cc14d4583dc))


### Core

* add an arch check to VS 2019 ([#3025](https://github.com/nodejs/node-gyp/issues/3025)) ([323957b](https://github.com/nodejs/node-gyp/commit/323957b74e9586fb3fbfb2acad5040379c778de6))
* **deps:** bump seanmiddleditch/gha-setup-ninja from 4 to 5 ([#3041](https://github.com/nodejs/node-gyp/issues/3041)) ([10f6730](https://github.com/nodejs/node-gyp/commit/10f6730be660e7a38be8a12111937e37fcf74834))
* proc-log@4.0.0 ([#3022](https://github.com/nodejs/node-gyp/issues/3022)) ([141aa6b](https://github.com/nodejs/node-gyp/commit/141aa6bf029e6f984be8ea98aaf985e5df894082))
* tar@6.2.1 ([#3021](https://github.com/nodejs/node-gyp/issues/3021)) ([b22d5ee](https://github.com/nodejs/node-gyp/commit/b22d5eef861892c968052ffc1c71b551f738163b))


### Doc

* `node-pre-gyp` is no longer maintained ([#3015](https://github.com/nodejs/node-gyp/issues/3015)) ([93186f1](https://github.com/nodejs/node-gyp/commit/93186f10c966b4148fc500e48f8cbffacccdfa3c))
* add the way to configuring Python dependency for Windows PowerShell ([#2996](https://github.com/nodejs/node-gyp/issues/2996)) ([9fd7936](https://github.com/nodejs/node-gyp/commit/9fd7936f0d7232a8a79e6a7b6cbfb814d9042b13))
* Installation -- Python >= v3.12 requires `node-gyp` >= v10 ([#3010](https://github.com/nodejs/node-gyp/issues/3010)) ([a6b48fc](https://github.com/nodejs/node-gyp/commit/a6b48fca9993e54d757cd110f6b41f8200d99ca4))


### Miscellaneous

* fix ruff command ([#3044](https://github.com/nodejs/node-gyp/issues/3044)) ([b3916d5](https://github.com/nodejs/node-gyp/commit/b3916d5b25704a53e89be16b500036a14bdc5060))

## [10.1.0](https://github.com/nodejs/node-gyp/compare/v10.0.1...v10.1.0) (2024-03-13)


### Features

* improve visual studio detection ([#2957](https://github.com/nodejs/node-gyp/issues/2957)) ([109e3d4](https://github.com/nodejs/node-gyp/commit/109e3d4245504a7b75c99f578e1203c0ef4b518e))


### Core

* add support for locally installed headers ([#2964](https://github.com/nodejs/node-gyp/issues/2964)) ([3298731](https://github.com/nodejs/node-gyp/commit/329873141f0d3e3787d3c006801431da04e4ed0c))
* **deps:** bump actions/setup-python from 4 to 5 ([#2960](https://github.com/nodejs/node-gyp/issues/2960)) ([3f0df7e](https://github.com/nodejs/node-gyp/commit/3f0df7e9334e49e8c7f6fdbbb9e1e6c5a8cca53b))
* **deps:** bump google-github-actions/release-please-action ([#2961](https://github.com/nodejs/node-gyp/issues/2961)) ([b1f1808](https://github.com/nodejs/node-gyp/commit/b1f1808bfff0d51e6d3eb696ab6a5b89b7b9630c))
* print Python executable path using UTF-8 ([#2995](https://github.com/nodejs/node-gyp/issues/2995)) ([c472912](https://github.com/nodejs/node-gyp/commit/c4729129daa9bb5204246b857826fb391ac961e1))
* update supported vs versions ([#2959](https://github.com/nodejs/node-gyp/issues/2959)) ([391cc5b](https://github.com/nodejs/node-gyp/commit/391cc5b9b25cffe0cb2edcba3583414a771b4a15))


### Doc

* npm is currently v10 ([#2970](https://github.com/nodejs/node-gyp/issues/2970)) ([7705a22](https://github.com/nodejs/node-gyp/commit/7705a22f31a62076e9f8429780a459f4ad71ea4c))
* remove outdated Node versions from readme ([#2955](https://github.com/nodejs/node-gyp/issues/2955)) ([ae8478e](https://github.com/nodejs/node-gyp/commit/ae8478ec32d9b2fa71b591ac22cdf867ef2e9a7d))
* remove outdated update engines.node reference in 10.0.0 changelog ([b42e796](https://github.com/nodejs/node-gyp/commit/b42e7966177f006f3d1aab1d27885d8372c8ed01))


### Miscellaneous

* only run release please on push ([cff9ac2](https://github.com/nodejs/node-gyp/commit/cff9ac2c3083769a383e00bc60b91562f03116e3))
* upgrade release please action from v2 to v4 ([#2982](https://github.com/nodejs/node-gyp/issues/2982)) ([0035d8e](https://github.com/nodejs/node-gyp/commit/0035d8e9dc98b94f0bc8cd9023a6fa635003703e))

### [10.0.1](https://www.github.com/nodejs/node-gyp/compare/v10.0.0...v10.0.1) (2023-11-02)


### Bug Fixes

* use local `util` for `findAccessibleSync()` ([b39e681](https://www.github.com/nodejs/node-gyp/commit/b39e6819aa9e2c45107d6e60a4913ca036ebfbfd))


### Miscellaneous

* add parallel test logging ([7de1f5f](https://www.github.com/nodejs/node-gyp/commit/7de1f5f32d550d26d48fe4f76aed5866744edcba))
* lint fixes ([4e0ed99](https://www.github.com/nodejs/node-gyp/commit/4e0ed992566f43abc6e988af091ad07fde04acbf))
* use platform specific timeouts in tests ([a68586a](https://www.github.com/nodejs/node-gyp/commit/a68586a67d0af238300662cc062422b42820044d))

## [10.0.0](https://www.github.com/nodejs/node-gyp/compare/v9.4.0...v10.0.0) (2023-10-28)


### ⚠ BREAKING CHANGES

* use .npmignore file to limit which files are published (#2921)
* the `Gyp` class exported is now created using ECMAScript classes and therefore might have small differences to classes that were previously created with `util.inherits`.
* All internal functions have been coverted to return promises and no longer accept callbacks. This is not a breaking change for users but may be breaking to consumers of `node-gyp` if you are requiring internal functions directly.
* `node-gyp` now supports node `^16.14.0 || >=18.0.0`

### Features

* convert all internal functions to async/await ([355622f](https://www.github.com/nodejs/node-gyp/commit/355622f4aac3bd3056b9e03aac5fa2f42a4b3576))
* convert internal classes from util.inherits to classes ([d52997e](https://www.github.com/nodejs/node-gyp/commit/d52997e975b9da6e0cea3d9b99873e9ddc768679))
* drop node 14 support ([#2929](https://www.github.com/nodejs/node-gyp/issues/2929)) ([1b3bd34](https://www.github.com/nodejs/node-gyp/commit/1b3bd341b40f384988d03207ce8187e93ba609bc))
* drop rimraf dependency ([4a50fe3](https://www.github.com/nodejs/node-gyp/commit/4a50fe31574217c4b2a798fc72b19947a64ceea1))
* **gyp:** update gyp to v0.16.1 ([#2923](https://www.github.com/nodejs/node-gyp/issues/2923)) ([707927c](https://www.github.com/nodejs/node-gyp/commit/707927cd579205ef2b4b17e61c1cce24c056b452))
* replace npmlog with proc-log ([4a50fe3](https://www.github.com/nodejs/node-gyp/commit/4a50fe31574217c4b2a798fc72b19947a64ceea1))
* update engines.node to ^14.17.0 || ^16.13.0 || >=18.0.0 ([4a50fe3](https://www.github.com/nodejs/node-gyp/commit/4a50fe31574217c4b2a798fc72b19947a64ceea1))
* use .npmignore file to limit which files are published ([#2921](https://www.github.com/nodejs/node-gyp/issues/2921)) ([864a979](https://www.github.com/nodejs/node-gyp/commit/864a979930cf0ef5ad64bc887b901fa8955d058f))


### Bug Fixes

* create Python symlink only during builds, and clean it up after ([#2721](https://www.github.com/nodejs/node-gyp/issues/2721)) ([0f1f667](https://www.github.com/nodejs/node-gyp/commit/0f1f667b737d21905e283df100a2cb639993562a))
* promisify build command ([4a50fe3](https://www.github.com/nodejs/node-gyp/commit/4a50fe31574217c4b2a798fc72b19947a64ceea1))
* use fs/promises in favor of fs.promises ([4a50fe3](https://www.github.com/nodejs/node-gyp/commit/4a50fe31574217c4b2a798fc72b19947a64ceea1))


### Tests

* increase mocha timeout ([#2887](https://www.github.com/nodejs/node-gyp/issues/2887)) ([445c28f](https://www.github.com/nodejs/node-gyp/commit/445c28fabc5fbdf9c3bb3341fb70660a3530f6ad))
* update expired certs ([#2908](https://www.github.com/nodejs/node-gyp/issues/2908)) ([5746691](https://www.github.com/nodejs/node-gyp/commit/5746691a36f7b37019d4b8d4e9616aec43d20410))


### Doc

* Add note about Python symlinks (PR 2362) to CHANGELOG.md for 9.1.0 ([#2783](https://www.github.com/nodejs/node-gyp/issues/2783)) ([b3d41ae](https://www.github.com/nodejs/node-gyp/commit/b3d41aeb737ddd54cc292f363abc561dcc0a614e))
* README.md Do not hardcode the supported versions of Python ([#2880](https://www.github.com/nodejs/node-gyp/issues/2880)) ([bb93b94](https://www.github.com/nodejs/node-gyp/commit/bb93b946a9c74934b59164deb52128cf913c97d5))
* update applicable GitHub links from master to main ([#2843](https://www.github.com/nodejs/node-gyp/issues/2843)) ([d644ce4](https://www.github.com/nodejs/node-gyp/commit/d644ce48311edf090d0e920ad449e5766c757933))
* Update windows installation instructions in README.md ([#2882](https://www.github.com/nodejs/node-gyp/issues/2882)) ([c9caa2e](https://www.github.com/nodejs/node-gyp/commit/c9caa2ecf3c7deae68444ce8fabb32d2dca651cd))


### Core

* find python checks order changed on windows ([#2872](https://www.github.com/nodejs/node-gyp/issues/2872)) ([b030555](https://www.github.com/nodejs/node-gyp/commit/b030555cdb754d9c23906e7e707115cd077bbf76))
* glob@10.3.10 ([#2926](https://www.github.com/nodejs/node-gyp/issues/2926)) ([4bef1ec](https://www.github.com/nodejs/node-gyp/commit/4bef1ecc7554097d92beb397fbe1a546c5227545))
* glob@8.0.3 ([4a50fe3](https://www.github.com/nodejs/node-gyp/commit/4a50fe31574217c4b2a798fc72b19947a64ceea1))
* make-fetch-happen@13.0.0 ([#2927](https://www.github.com/nodejs/node-gyp/issues/2927)) ([059bb6f](https://www.github.com/nodejs/node-gyp/commit/059bb6fd41bb50955a9efbd97887773d60d53221))
* nopt@^7.0.0 ([4a50fe3](https://www.github.com/nodejs/node-gyp/commit/4a50fe31574217c4b2a798fc72b19947a64ceea1))
* standard@17.0.0 and fix linting errors ([4a50fe3](https://www.github.com/nodejs/node-gyp/commit/4a50fe31574217c4b2a798fc72b19947a64ceea1))
* which@3.0.0 ([4a50fe3](https://www.github.com/nodejs/node-gyp/commit/4a50fe31574217c4b2a798fc72b19947a64ceea1))
* which@4.0.0 ([#2928](https://www.github.com/nodejs/node-gyp/issues/2928)) ([e388255](https://www.github.com/nodejs/node-gyp/commit/e38825531403aabeae7abe58e76867f31b832f36))


### Miscellaneous

* add check engines script to CI ([#2922](https://www.github.com/nodejs/node-gyp/issues/2922)) ([21a7249](https://www.github.com/nodejs/node-gyp/commit/21a7249b40d8f95e7721e450fd18764adb1648a7))
* empty commit to add changelog entries from [#2770](https://www.github.com/nodejs/node-gyp/issues/2770) ([4a50fe3](https://www.github.com/nodejs/node-gyp/commit/4a50fe31574217c4b2a798fc72b19947a64ceea1))
* GitHub Workflows security hardening ([#2740](https://www.github.com/nodejs/node-gyp/issues/2740)) ([26683e9](https://www.github.com/nodejs/node-gyp/commit/26683e993df038fb94d89f2276f3535e4522d79a))
* misc testing fixes ([#2930](https://www.github.com/nodejs/node-gyp/issues/2930)) ([4e493d4](https://www.github.com/nodejs/node-gyp/commit/4e493d4fb262d12ac52c84979071ccc79e666a1a))
* run tests after release please PR ([3032e10](https://www.github.com/nodejs/node-gyp/commit/3032e1061cc2b7b49f83c397d385bafddc6b0214))

## [9.4.0](https://www.github.com/nodejs/node-gyp/compare/v9.3.1...v9.4.0) (2023-06-12)


### Features

* add support for native windows arm64 build tools ([bb76021](https://www.github.com/nodejs/node-gyp/commit/bb76021d35964d2bb125bc6214286f35ae4e6cad))
* Upgrade Python linting from flake8 to ruff ([#2815](https://www.github.com/nodejs/node-gyp/issues/2815)) ([fc0ddc6](https://www.github.com/nodejs/node-gyp/commit/fc0ddc6523c62b10e5ca1257500b3ceac01450a7))


### Bug Fixes

* extract tarball to temp directory on Windows ([#2846](https://www.github.com/nodejs/node-gyp/issues/2846)) ([aaa117c](https://www.github.com/nodejs/node-gyp/commit/aaa117c514430aa2c1e568b95df1b6ed1c1fd3b6))
* log statement is for devDir not nodedir ([#2840](https://www.github.com/nodejs/node-gyp/issues/2840)) ([55048f8](https://www.github.com/nodejs/node-gyp/commit/55048f8be5707c295fb0876306aded75638a8b63))


### Miscellaneous

* get update-gyp.py to work with Python >= v3.5 ([#2826](https://www.github.com/nodejs/node-gyp/issues/2826)) ([337e8e6](https://www.github.com/nodejs/node-gyp/commit/337e8e68209bd2481cbb11dacce61234dc5c9419))


### Doc

* docs/README.md add advise about deprecated node-sass ([#2828](https://www.github.com/nodejs/node-gyp/issues/2828)) ([6f3c2d3](https://www.github.com/nodejs/node-gyp/commit/6f3c2d3c6c0de0dbf8c7245f34c2e0b3eea53812))
* Update README.md ([#2822](https://www.github.com/nodejs/node-gyp/issues/2822)) ([c7927e2](https://www.github.com/nodejs/node-gyp/commit/c7927e228dfde059c93e08c26b54dd8026144583))


### Tests

* remove deprecated Node.js and Python ([#2868](https://www.github.com/nodejs/node-gyp/issues/2868)) ([a0b3d1c](https://www.github.com/nodejs/node-gyp/commit/a0b3d1c3afed71a74501476fcbc6ee3fface4d13))

### [9.3.1](https://www.github.com/nodejs/node-gyp/compare/v9.3.0...v9.3.1) (2022-12-16)


### Bug Fixes

* increase node 12 support to ^12.13 ([#2771](https://www.github.com/nodejs/node-gyp/issues/2771)) ([888efb9](https://www.github.com/nodejs/node-gyp/commit/888efb9055857afee6a6b54550722cf9ae3ee323))


### Miscellaneous

* update python test matrix ([#2774](https://www.github.com/nodejs/node-gyp/issues/2774)) ([38f01fa](https://www.github.com/nodejs/node-gyp/commit/38f01fa57d10fdb3db7697121d957bc2e0e96508))

## [9.3.0](https://www.github.com/nodejs/node-gyp/compare/v9.2.0...v9.3.0) (2022-10-10)


### Features

* **gyp:** update gyp to v0.14.0 ([#2749](https://www.github.com/nodejs/node-gyp/issues/2749)) ([713b8dc](https://www.github.com/nodejs/node-gyp/commit/713b8dcdbf44532ca9453a127da266386cc737f8))
* remove support for VS2015 in Node.js >=19 ([#2746](https://www.github.com/nodejs/node-gyp/issues/2746)) ([131d1a4](https://www.github.com/nodejs/node-gyp/commit/131d1a463baf034a04154bcda753a8295f112a34))
* support IBM Open XL C/C++ on z/OS ([#2743](https://www.github.com/nodejs/node-gyp/issues/2743)) ([7d0c83d](https://www.github.com/nodejs/node-gyp/commit/7d0c83d2a95aca743dff972826d0da26203acfc4))

## [9.2.0](https://www.github.com/nodejs/node-gyp/compare/v9.1.0...v9.2.0) (2022-10-02)


### Features

* Add proper support for IBM i ([a26494f](https://www.github.com/nodejs/node-gyp/commit/a26494fbb8883d9ef784503979e115dec3e2791e))
* **gyp:** update gyp to v0.13.0 ([3e2a532](https://www.github.com/nodejs/node-gyp/commit/3e2a5324f1c24f3a04bca04cf54fe23d5c4d5e50))


### Bug Fixes

* node.js debugger adds stderr (but exit code is 0) -> shouldn't throw ([#2719](https://www.github.com/nodejs/node-gyp/issues/2719)) ([c379a74](https://www.github.com/nodejs/node-gyp/commit/c379a744c65c7ab07c2c3193d9c7e8f25ae1b05e))


### Core

* enable support for zoslib on z/OS ([#2600](https://www.github.com/nodejs/node-gyp/issues/2600)) ([83c0a12](https://www.github.com/nodejs/node-gyp/commit/83c0a12bf23b4cbf3125d41f9e2d4201db76c9ae))


### Miscellaneous

* update dependency - nopt@
... [TRUNCATED]
```

### File: CODE_OF_CONDUCT.md
```md
# Code of Conduct

* [Node.js Code of Conduct](https://github.com/nodejs/admin/blob/master/CODE_OF_CONDUCT.md)
* [Node.js Moderation Policy](https://github.com/nodejs/admin/blob/master/Moderation-Policy.md)

```

### File: CONTRIBUTING.md
```md
# Contributing to node-gyp

## Code of Conduct

Please read the
[Code of Conduct](https://github.com/nodejs/admin/blob/main/CODE_OF_CONDUCT.md)
which explains the minimum behavior expectations for node-gyp contributors.

<a id="developers-certificate-of-origin"></a>
## Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

* (a) The contribution was created in whole or in part by me and I
  have the right to submit it under the open source license
  indicated in the file; or

* (b) The contribution is based upon previous work that, to the best
  of my knowledge, is covered under an appropriate open source
  license and I have the right under that license to submit that
  work with modifications, whether created in whole or in part
  by me, under the same open source license (unless I am
  permitted to submit under a different license), as indicated
  in the file; or

* (c) The contribution was provided directly to me by some other
  person who certified (a), (b) or (c) and I have not modified
  it.

* (d) I understand and agree that this project and the contribution
  are public and that a record of the contribution (including all
  personal information I submit with it, including my sign-off) is
  maintained indefinitely and may be redistributed consistent with
  this project or the open source license(s) involved.

```

### File: macOS_Catalina_acid_test.sh
```sh
#!/bin/bash

pkgs=(
  "com.apple.pkg.DeveloperToolsCLILeo" # standalone
  "com.apple.pkg.DeveloperToolsCLI"    # from XCode
  "com.apple.pkg.CLTools_Executables"  # Mavericks
)

for pkg in "${pkgs[@]}"; do
  output=$(/usr/sbin/pkgutil --pkg-info "$pkg" 2>/dev/null)
  if [ "$output" ]; then
    version=$(echo "$output" | grep 'version' | cut -d' ' -f2)
    break
  fi
done

if [ "$version" ]; then
  echo "Command Line Tools version: $version"
else
  echo >&2 'Command Line Tools not found'
fi

```

### File: release-please-config.json
```json
{
    "packages": {
        ".": {
            "include-component-in-tag": false,
            "release-type": "node",
            "changelog-sections": [
                { "type": "feat", "section": "Features", "hidden": false },
                { "type": "fix", "section": "Bug Fixes", "hidden": false },
                { "type": "bin", "section": "Core", "hidden": false },
                { "type": "gyp", "section": "Core", "hidden": false },
                { "type": "lib", "section": "Core", "hidden": false },
                { "type": "src", "section": "Core", "hidden": false },
                { "type": "test", "section": "Tests", "hidden": false },
                { "type": "build", "section": "Core", "hidden": false },
                { "type": "clean", "section": "Core", "hidden": false },
                { "type": "configure", "section": "Core", "hidden": false },
                { "type": "install", "section": "Core", "hidden": false },
                { "type": "list", "section": "Core", "hidden": false },
                { "type": "rebuild", "section": "Core", "hidden": false },
                { "type": "remove", "section": "Core", "hidden": false },
                { "type": "deps", "section": "Core", "hidden": false },
                { "type": "python", "section": "Core", "hidden": false },
                { "type": "lin", "section": "Core", "hidden": false },
                { "type": "linux", "section": "Core", "hidden": false },
                { "type": "mac", "section": "Core", "hidden": false },
                { "type": "macos", "section": "Core", "hidden": false },
                { "type": "win", "section": "Core", "hidden": false },
                { "type": "windows", "section": "Core", "hidden": false },
                { "type": "zos", "section": "Core", "hidden": false },
                { "type": "doc", "section": "Doc", "hidden": false },
                { "type": "docs", "section": "Doc", "hidden": false },
                { "type": "readme", "section": "Doc", "hidden": false },
                { "type": "chore", "section": "Miscellaneous", "hidden": false },
                { "type": "refactor", "section": "Miscellaneous", "hidden": false },
                { "type": "ci", "section": "Miscellaneous", "hidden": false },
                { "type": "meta", "section": "Miscellaneous", "hidden": false }
            ]
        }
    }
}

```

### File: SECURITY.md
```md
If you believe you have found a security issue in the software in this
repository, please consult https://github.com/nodejs/node/blob/HEAD/SECURITY.md.
```

### File: update-gyp.py
```py
#!/usr/bin/env python3

import argparse
import os
import shutil
import subprocess
import tarfile
import tempfile
import urllib.request

BASE_URL = "https://github.com/nodejs/gyp-next/archive/"
CHECKOUT_PATH = os.path.dirname(os.path.realpath(__file__))
CHECKOUT_GYP_PATH = os.path.join(CHECKOUT_PATH, "gyp")

parser = argparse.ArgumentParser()
parser.add_argument("tag", help="gyp tag to update to")
args = parser.parse_args()

tar_url = BASE_URL + args.tag + ".tar.gz"

changed_files = subprocess.check_output(["git", "diff", "--name-only"]).strip()
if changed_files:
    raise Exception("Can't update gyp while you have uncommitted changes in node-gyp")

with tempfile.TemporaryDirectory() as tmp_dir:
    tar_file = os.path.join(tmp_dir, "gyp.tar.gz")
    unzip_target = os.path.join(tmp_dir, "gyp")
    with open(tar_file, "wb") as f:
        print("Downloading gyp-next@" + args.tag + " into temporary directory...")
        print("From: " + tar_url)
        with urllib.request.urlopen(tar_url) as in_file:
            f.write(in_file.read())

        print("Unzipping...")
        with tarfile.open(tar_file, "r:gz") as tar_ref:
            def is_within_directory(directory, target):

                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)

                prefix = os.path.commonprefix([abs_directory, abs_target])

                return prefix == abs_directory

            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):

                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")

                tar.extractall(path, members, numeric_owner=numeric_owner)

            safe_extract(tar_ref, unzip_target)

        print("Moving to current checkout (" + CHECKOUT_PATH + ")...")
        if os.path.exists(CHECKOUT_GYP_PATH):
            shutil.rmtree(CHECKOUT_GYP_PATH)
        shutil.move(
            os.path.join(unzip_target, os.listdir(unzip_target)[0]), CHECKOUT_GYP_PATH
        )

subprocess.check_output(["git", "add", "gyp"], cwd=CHECKOUT_PATH)
subprocess.check_output(["git", "commit", "-m", "feat(gyp): update gyp to " + args.tag])

```

### File: .github\ISSUE_TEMPLATE.md
```md
<!--
Thank you for reporting an issue!

Remember, this issue tracker is for reporting issues ONLY with node-gyp.

If you have an issue installing a specific module, please file an issue on
that module's issue tracker (`npm issues modulename`). Open issue here only if
you are sure this is an issue with node-gyp, not with the module you are
trying to build.

Fill out the form below. We probably won't investigate an issue that does not
provide the basic information we require.

-->

Please look thru your error log for the string `gyp info using node-gyp@` and if the version number is less than the [current release of node-gyp](https://github.com/nodejs/node-gyp/releases) then __please upgrade__ using the instructions at https://github.com/nodejs/node-gyp/blob/main/docs/Updating-npm-bundled-node-gyp.md and try your command again.

Requests for help with [`node-sass` are very common](https://github.com/nodejs/node-gyp/issues?q=label%3A%22Node+Sass+--%3E+Dart+Sass%22). Please be aware that this package is deprecated, you should seek alternatives and avoid opening new issues about it here.

* **Node Version**: <!-- `node -v` and `npm -v` -->
* **Platform**: <!-- `uname -a` (UNIX), or `systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"` (Windows) -->
* **Compiler**: <!-- `cc -v` (UNIX) or `msbuild /version & cl` (Windows) -->
* **Module**: <!-- what you tried to build/install -->

<details><summary>Verbose output (from npm or node-gyp):</summary>

```
Paste your log here, between the backticks. It can be:
  - npm --verbose output,
  - or contents of npm-debug.log,
  - or output of node-gyp rebuild --verbose.
Include the command you were trying to run.

This should look like this:

>npm --verbose
npm info it worked if it ends with ok
npm verb cli [
npm verb cli   'C:\\...\\node\\13.9.0\\x64\\node.exe',
npm verb cli   'C:\\...\\node\\13.9.0\\x64\\node_modules\\npm\\bin\\npm-cli.js',
npm verb cli   '--verbose'
npm verb cli ]
npm info using npm@6.13.7
npm info using node@v13.9.0

Usage: npm <command>
(...)
```

</details>

<!-- Any further details -->

```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
<!--
Thank you for your pull request. Please review the below requirements.

Contributor guide: https://github.com/nodejs/node/blob/main/CONTRIBUTING.md
-->

##### Checklist
<!-- Remove items that do not apply. For completed items, change [ ] to [x]. -->

- [ ] `npm install && npm run lint && npm test` passes
- [ ] tests are included <!-- Bug fixes and new features should include tests -->
- [ ] documentation is changed or added
- [ ] commit message follows [commit guidelines](https://github.com/googleapis/release-please#how-should-i-write-my-commits)

##### Description of change
<!-- Provide a description of the change -->


```

### File: bin\node-gyp.js
```js
#!/usr/bin/env node

'use strict'

process.title = 'node-gyp'

const envPaths = require('env-paths')
const gyp = require('../')
const log = require('../lib/log')
const os = require('os')

/**
 * Process and execute the selected commands.
 */

const prog = gyp()
let completed = false
prog.parseArgv(process.argv)
prog.devDir = prog.opts.devdir

const homeDir = os.homedir()
if (prog.devDir) {
  prog.devDir = prog.devDir.replace(/^~/, homeDir)
} else if (homeDir) {
  prog.devDir = envPaths('node-gyp', { suffix: '' }).cache
} else {
  throw new Error(
    "node-gyp requires that the user's home directory is specified " +
    'in either of the environmental variables HOME or USERPROFILE. ' +
    'Overide with: --devdir /path/to/.node-gyp')
}

if (prog.todo.length === 0) {
  if (~process.argv.indexOf('-v') || ~process.argv.indexOf('--version')) {
    log.stdout('v%s', prog.version)
  } else {
    log.stdout('%s', prog.usage())
  }
  process.exit(0)
}

log.info('it worked if it ends with', 'ok')
log.verbose('cli', process.argv)
log.info('using', 'node-gyp@%s', prog.version)
log.info('using', 'node@%s | %s | %s', process.versions.node, process.platform, process.arch)

/**
 * Change dir if -C/--directory was passed.
 */

const dir = prog.opts.directory
if (dir) {
  const fs = require('fs')
  try {
    const stat = fs.statSync(dir)
    if (stat.isDirectory()) {
      log.info('chdir', dir)
      process.chdir(dir)
    } else {
      log.warn('chdir', dir + ' is not a directory')
    }
  } catch (e) {
    if (e.code === 'ENOENT') {
      log.warn('chdir', dir + ' is not a directory')
    } else {
      log.warn('chdir', 'error during chdir() "%s"', e.message)
    }
  }
}

async function run () {
  const command = prog.todo.shift()
  if (!command) {
    // done!
    completed = true
    log.info('ok')
    return
  }

  try {
    const args = await prog.commands[command.name](command.args) || []

    if (command.name === 'list') {
      if (args.length) {
        args.forEach((version) => log.stdout(version))
      } else {
        log.stdout('No node development files installed. Use `node-gyp install` to install a version.')
      }
    } else if (args.length >= 1) {
      log.stdout(...args.slice(1))
    }

    // now run the next command in the queue
    return run()
  } catch (err) {
    log.error(command.name + ' error')
    log.error('stack', err.stack)
    errorMessage()
    log.error('not ok')
    return process.exit(1)
  }
}

process.on('exit', function (code) {
  if (!completed && !code) {
    log.error('Completion callback never invoked!')
    issueMessage()
    process.exit(6)
  }
})

process.on('uncaughtException', function (err) {
  log.error('UNCAUGHT EXCEPTION')
  log.error('stack', err.stack)
  issueMessage()
  process.exit(7)
})

function errorMessage () {
  // copied from npm's lib/utils/error-handler.js
  const os = require('os')
  log.error('System', os.type() + ' ' + os.release())
  log.error('command', process.argv
    .map(JSON.stringify).join(' '))
  log.error('cwd', process.cwd())
  log.error('node -v', process.version)
  log.error('node-gyp -v', 'v' + prog.package.version)
}

function issueMessage () {
  errorMessage()
  log.error('', ['Node-gyp failed to build your package.',
    'Try to update npm and/or node-gyp and if it does not help file an issue with the package author.'
  ].join('\n'))
}

// start running the given commands!
run()

```

### File: docs\binding.gyp-files-in-the-wild.md
```md
This page contains links to some examples of existing `binding.gyp` files that other node modules are using. Take a look at them for inspiration.

To add to this page, just add the link to the project's `binding.gyp` file below:

 * [ons](https://github.com/XadillaX/aliyun-ons/blob/master/binding.gyp)
 * [thmclrx](https://github.com/XadillaX/thmclrx/blob/master/binding.gyp)
 * [libxmljs](https://github.com/polotek/libxmljs/blob/master/binding.gyp)
 * [node-buffertools](https://github.com/bnoordhuis/node-buffertools/blob/master/binding.gyp)
 * [node-canvas](https://github.com/LearnBoost/node-canvas/blob/master/binding.gyp)
 * [node-ffi](https://github.com/rbranson/node-ffi/blob/master/binding.gyp) + [libffi](https://github.com/rbranson/node-ffi/blob/master/deps/libffi/libffi.gyp)
 * [node-time](https://github.com/TooTallNate/node-time/blob/master/binding.gyp)
 * [node-sass](https://github.com/sass/node-sass/blob/master/binding.gyp) + [libsass](https://github.com/sass/node-sass/blob/master/src/libsass.gyp)
 * [node-serialport](https://github.com/voodootikigod/node-serialport/blob/master/binding.gyp)
 * [node-weak](https://github.com/TooTallNate/node-weak/blob/master/binding.gyp)
 * [pty.js](https://github.com/chjj/pty.js/blob/master/binding.gyp)
 * [ref](https://github.com/TooTallNate/ref/blob/master/binding.gyp)
 * [appjs](https://github.com/milani/appjs/blob/master/binding.gyp)
 * [nwm](https://github.com/mixu/nwm/blob/master/binding.gyp)
 * [bcrypt](https://github.com/ncb000gt/node.bcrypt.js/blob/master/binding.gyp)
 * [nk-mysql](https://github.com/mmod/nodamysql/blob/master/binding.gyp)
 * [nk-xrm-installer](https://github.com/mmod/nk-xrm-installer/blob/master/binding.gyp) + [includable.gypi](https://github.com/mmod/nk-xrm-installer/blob/master/includable.gypi) + [unpack.py](https://github.com/mmod/nk-xrm-installer/blob/master/unpack.py) + [disburse.py](https://github.com/mmod/nk-xrm-installer/blob/master/disburse.py)   
   <sub>.py files above provide complete reference for examples of fetching source via http, extracting, and moving files.</sub>
 * [node-memwatch](https://github.com/lloyd/node-memwatch/blob/master/binding.gyp)
 * [node-ip2location](https://github.com/bolgovr/node-ip2location/blob/master/binding.gyp)
 * [node-midi](https://github.com/justinlatimer/node-midi/blob/master/binding.gyp)
 * [node-sqlite3](https://github.com/developmentseed/node-sqlite3/blob/master/binding.gyp) + [libsqlite3](https://github.com/developmentseed/node-sqlite3/blob/master/deps/sqlite3.gyp)
 * [node-zipfile](https://github.com/mapbox/node-zipfile/blob/master/binding.gyp)
 * [node-mapnik](https://github.com/mapnik/node-mapnik/blob/master/binding.gyp)
 * [node-inotify](https://github.com/c4milo/node-inotify/blob/master/binding.gyp)
 * [v8-profiler](https://github.com/c4milo/v8-profiler/blob/master/binding.gyp)
 * [airtunes](https://github.com/radioline/node_airtunes/blob/master/binding.gyp)
 * [node-fann](https://github.com/c4milo/node-fann/blob/master/binding.gyp)
 * [node-talib](https://github.com/oransel/node-talib/blob/master/binding.gyp)
 * [node-leveldown](https://github.com/rvagg/node-leveldown/blob/master/binding.gyp) + [leveldb.gyp](https://github.com/rvagg/node-leveldown/blob/master/deps/leveldb/leveldb.gyp) + [snappy.gyp](https://github.com/rvagg/node-leveldown/blob/master/deps/snappy/snappy.gyp)
 * [node-expat](https://github.com/astro/node-expat/blob/master/binding.gyp) + [libexpat](https://github.com/astro/node-expat/blob/master/deps/libexpat/libexpat.gyp)
 * [node-openvg-canvas](https://github.com/luismreis/node-openvg-canvas/blob/master/binding.gyp) + [node-openvg](https://github.com/luismreis/node-openvg/blob/master/binding.gyp)
 * [node-cryptopp](https://github.com/BatikhSouri/node-cryptopp/blob/master/binding.gyp)
 * [topcube](https://github.com/creationix/topcube/blob/master/binding.gyp)
 * [node-osmium](https://github.com/osmcode/node-osmium/blob/master/binding.gyp)
 * [node-osrm](https://github.com/DennisOSRM/node-osrm)
 * [node-oracle](https://github.com/joeferner/node-oracle/blob/master/binding.gyp)
 * [node-oracledb](https://github.com/oracle/node-oracledb/blob/main/binding.gyp)
 * [node-process-list](https://github.com/ReklatsMasters/node-process-list/blob/master/binding.gyp)
 * [node-nanomsg](https://github.com/nickdesaulniers/node-nanomsg/blob/master/binding.gyp)
 * [Ghostscript4JS](https://github.com/NickNaso/ghostscript4js/blob/master/binding.gyp)
 * [nodecv](https://github.com/xudafeng/nodecv/blob/master/binding.gyp)
 * [magick-cli](https://github.com/NickNaso/magick-cli/blob/master/binding.gyp)
 * [sharp](https://github.com/lovell/sharp/blob/master/binding.gyp)
 * [krb5](https://github.com/adaltas/node-krb5/blob/master/binding.gyp)
 * [node-heapdump](https://github.com/bnoordhuis/node-heapdump/blob/master/binding.gyp)

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

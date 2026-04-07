---
id: workerd
type: knowledge
owner: OA_Triage
---
# workerd
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "@cloudflare/workerd-root",
  "private": true,
  "scripts": {},
  "dependencies": {
    "prettier": "^3.8.1",
    "typescript": "6.0.2"
  },
  "devDependencies": {
    "@eslint/js": "^10.0.1",
    "@types/node": "^25.5.0",
    "capnp-es": "0.0.14",
    "chrome-remote-interface": "^0.34.0",
    "esbuild": "^0.27.4",
    "eslint": "^10.1.0",
    "expect-type": "^1.3.0",
    "typescript-eslint": "^8.57.2"
  },
  "pnpm": {
    "onlyBuiltDependencies": [
      "esbuild"
    ],
    "packageExtensions": {
      "@opennextjs/cloudflare": {
        "dependencies": {
          "esbuild": "^0.27.4"
        }
      }
    }
  },
  "packageManager": "pnpm@10.32.1"
}

```

### File: README.md
```md
# 👷 `workerd`, Cloudflare's JavaScript/Wasm Runtime

![Banner](/docs/assets/banner.png)

`workerd` (pronounced: "worker-dee") is a JavaScript / Wasm server runtime based on the same code that powers [Cloudflare Workers](https://workers.dev).

You might use it:

* **As an application server**, to self-host applications designed for Cloudflare Workers.
* **As a development tool**, to develop and test such code locally.
* **As a programmable HTTP proxy** (forward or reverse), to efficiently intercept, modify, and
  route network requests.

## Introduction

### Design Principles

* **Server-first:** Designed for servers, not CLIs nor GUIs.

* **Standard-based:** Built-in APIs are based on web platform standards, such as `fetch()`.

* **Nanoservices:** Split your application into components that are decoupled and independently-deployable like microservices, but with performance of a local function call. When one nanoservice calls another, the callee runs in the same thread and process.

* **Homogeneous deployment:** Instead of deploying different microservices to different machines in your cluster, deploy all your nanoservices to every machine in the cluster, making load balancing much easier.

* **Capability bindings:** `workerd` configuration uses capabilities instead of global namespaces to connect nanoservices to each other and external resources. The result is code that is more composable -- and immune to SSRF attacks.

* **Always backwards compatible:** Updating `workerd` to a newer version will never break your JavaScript code. `workerd`'s version number is simply a date, corresponding to the maximum ["compatibility date"](https://developers.cloudflare.com/workers/platform/compatibility-dates/) supported by that version. You can always configure your worker to a past date, and `workerd` will emulate the API as it existed on that date.

[Read the blog post to learn more about these principles.](https://blog.cloudflare.com/workerd-open-source-workers-runtime/)

### WARNING: `workerd` is not a hardened sandbox

`workerd` tries to isolate each Worker so that it can only access the resources it is configured to access. However, `workerd` on its own does not contain suitable defense-in-depth against the possibility of implementation bugs. When using `workerd` to run possibly-malicious code, you must run it inside an appropriate secure sandbox, such as a virtual machine. The Cloudflare Workers hosting service in particular [uses many additional layers of defense-in-depth](https://blog.cloudflare.com/mitigating-spectre-and-other-security-threats-the-cloudflare-workers-security-model/).

With that said, if you discover a bug that allows malicious code to break out of `workerd`, please submit it to [Cloudflare's bug bounty program](https://hackerone.com/cloudflare?type=team) for a reward.

## Getting Started

### Supported Platforms

In theory, `workerd` should work on any POSIX system that is supported by V8 and Windows.

In practice, `workerd` is tested on:

* Linux and macOS (x86-64 and arm64 architectures)
* Windows (x86-64 architecture)

On other platforms, you may have to do tinkering to make things work.

### Building `workerd`

To build `workerd`, you need:

* Bazel
  * If you use [Bazelisk](https://github.com/bazelbuild/bazelisk) (recommended), it will automatically download and use the right version of Bazel for building workerd.
* On Linux:
  * We use the clang/LLVM toolchain to build workerd and support version 19 and higher. Earlier versions of clang may still work, but are not officially supported.
  * Clang 19+ (e.g. package `clang-19` on Debian Trixie). If clang is installed as `clang-<version>` please create a symlink to it in your PATH named `clang`, or use `--repo_env=CC=clang-<version>` on `bazel` command lines to specify the compiler name.

  * libc++ 19+ (e.g. packages `libc++-19-dev` and `libc++abi-19-dev`)
  * LLD 19+ (e.g. package `lld-19`).
  * `python3`, `python3-distutils`, and `tcl8.6`
* On macOS:
  * Xcode 16.3 installation (available on macOS 15 and higher). Building with just the Xcode Command Line Tools is not being tested, but should work too.
  * Homebrew installed `tcl-tk` package (provides Tcl 8.6)
* On Windows:
  * Install [App Installer](https://learn.microsoft.com/en-us/windows/package-manager/winget/#install-winget)
    from the Microsoft Store for the `winget` package manager and then run
    [install-deps.bat](tools/windows/install-deps.bat) from an administrator prompt to install
    bazelisk, LLVM, and other dependencies required to build workerd on Windows.
  * Add `startup --output_user_root=C:/tmp` to the `.bazelrc` file in your user directory.
  * When developing at the command-line, run [bazel-env.bat](tools/windows/bazel-env.bat) in your shell first
    to select tools and Windows SDK versions before running bazel.

You may then build `workerd` at the command-line with:

```sh
bazel build //src/workerd/server:workerd
```

You can pass `--config=release` to compile in release mode:

```sh
bazel build //src/workerd/server:workerd --config=release
```

You can also build from within Visual Studio Code using the instructions in [docs/vscode.md](docs/vscode.md).

The compiled binary will be located at `bazel-bin/src/workerd/server/workerd`.

If you run a Bazel build before you've installed some dependencies (like clang or libc++), and then you install the dependencies, you must resync locally cached toolchains, or clean Bazel's cache, otherwise you might get strange errors:

```sh
bazel fetch --configure --force
```

If that fails, you can try:

```sh
bazel clean --expunge
```

The cache will now be cleaned and you can try building again.

If you have a fairly recent clang packages installed you can build a more performant release
version of workerd:

```sh
bazel build --config=thin-lto //src/workerd/server:workerd
```

### Configuring `workerd`

`workerd` is configured using a config file written in Cap'n Proto text format.

A simple "Hello World!" config file might look like:

```capnp
using Workerd = import "/workerd/workerd.capnp";

const config :Workerd.Config = (
  services = [
    (name = "main", worker = .mainWorker),
  ],

  sockets = [
    # Serve HTTP on port 8080.
    ( name = "http",
      address = "*:8080",
      http = (),
      service = "main"
    ),
  ]
);

const mainWorker :Workerd.Worker = (
  serviceWorkerScript = embed "hello.js",
  compatibilityDate = "2023-02-28",
  # Learn more about compatibility dates at:
  # https://developers.cloudflare.com/workers/platform/compatibility-dates/
);
```

Where `hello.js` contains:

```javascript
addEventListener("fetch", event => {
  event.respondWith(new Response("Hello World"));
});
```

[Complete reference documentation is provided by the comments in workerd.capnp.](src/workerd/server/workerd.capnp)

[There is also a library of sample config files.](samples)

### Running `workerd`

To serve your config, do:

`workerd serve my-config.capnp`

For more details about command-line usage, use `workerd --help`.

Prebuilt binaries are distributed via `npm`. Run `npx workerd ...` to use these. If you're running a prebuilt binary, you'll need to make sure your system has the right dependencies installed:

* On Linux:
  * glibc 2.35 or higher (already included on e.g. Ubuntu 22.04, Debian Bookworm)
* On macOS:
  * macOS 13.5 or higher
  * The Xcode command line tools, which can be installed with `xcode-select --install`
* x86_64 CPU with at least SSE4.2 and CLMUL ISA extensions, or arm64 CPU with CRC extension (enabled by default under armv8.1-a). These extensions are supported by all recent x86 and arm64 CPUs.

### Local Worker development with `wrangler`

You can use [Wrangler](https://developers.cloudflare.com/workers/wrangler/) (v3.0 or greater) to develop Cloudflare Workers locally, using `workerd`. First, run the following command to configure Miniflare to use this build of `workerd`.

```
export MINIFLARE_WORKERD_PATH="<WORKERD_REPO_DIR>/bazel-bin/src/workerd/server/workerd"
```

Then, run:

`wrangler dev`

### Serving in production

`workerd` is designed to be unopinionated about how it runs.

One good way to manage `workerd` in production is using `systemd`. Particularly useful is `systemd`'s ability to open privileged sockets on `workerd`'s behalf while running the service itself under an unprivileged user account. To help with this, `workerd` supports inheriting sockets from the parent process using the `--socket-fd` flag.

Here's an example system service file, assuming your config defines two sockets named `http` and `https`:

```sh
# /etc/systemd/system/workerd.service
[Unit]
Description=workerd runtime
After=local-fs.target remote-fs.target network-online.target
Requires=local-fs.target remote-fs.target workerd.socket
Wants=network-online.target

[Service]
Type=exec
ExecStart=/usr/bin/workerd serve /etc/workerd/config.capnp --socket-fd http=3 --socket-fd https=4
Sockets=workerd.socket

# If workerd crashes, restart it.
Restart=always

# Run under an unprivileged user account.
User=nobody
Group=nogroup

# Hardening measure: Do not allow workerd to run suid-root programs.
NoNewPrivileges=true

[Install]
WantedBy=multi-user.target
```

And corresponding sockets file:

```sh
# /etc/systemd/system/workerd.socket
[Unit]
Description=sockets for workerd
PartOf=workerd.service

[Socket]
ListenStream=0.0.0.0:80
ListenStream=0.0.0.0:443

[Install]
WantedBy=sockets.target
```

Once these files are in place you can enable the service -- see the systemd documentation or ask your favorite LLM for details.

```

### File: types\README.md
```md
# Workers Types Generator

This directory contains scripts for automatically generating TypeScript types
from [JSG RTTI](../src/workerd/jsg/rtti.h).

## Generating Types

```shell
# Generates types to `../bazel-bin/types/api.d.ts`
$ bazel build //types:types
```

## Developing Generator Scripts

When developing generator scripts with an IDE, you'll need to install
dependencies yourself for integrated type checking and completions to work.

```shell
# Generates JSG RTTI Cap’n Proto JavaScript/TypeScript files
$ bazel build //src/workerd/jsg:rtti_capnp_js
# Install dependencies (note pnpm is required by https://github.com/aspect-build/rules_js)
$ pnpm install
# Generates types to `../bazel-bin/types/api.d.ts`
$ bazel build //types:types
# Run tests
$ bazel test //types:all
```

## Structure

- `src/generator`: generating TypeScript AST nodes from JSG RTTI
- `src/transforms`: post-processing TypeScript AST transforms
- `src/index.ts`: main entrypoint
- `src/{print,program}.ts`: helpers for printing nodes and creating programs
- `defines`: additional TypeScript-only definitions that don't correspond to
  `workerd` runtime APIs, appended to the end of outputs

## Updates types

```shell
just generate-types
```

```

### File: samples\extensions\README.md
```md
# Extensions

This directory contains comprehensive samples of using workerd extensions.

This example defines a fictional burrito shop extension in
[burrito-shop.capnp](burrito-shop.capnp)
and demonstrates following features:

- using modules to provide new user-level api: [burrito-shop.js](burrito-shop.js) and
  [worker.js](worker.js)
- using internal modules to hide implementation details from the user: [kitchen.js](kitchen.js)

The sample will be extended as more functionality is implemented.

## Running

```
$ bazel run //src/workerd/server:workerd -- serve $(pwd)/samples/extensions/config.capnp
$ curl localhost:8080 -X POST -d 'veggie'
9
```

## Demonstrated Methods

### Importable Module

This method demonstrates a publicly importable module, with the initialization being handled by the worker in  [worker.js](worker.js)

#### Accessibility

The module `burrito-shop:burrito-shop`, which is defined in the config [burrito-shop.capnp](burrito-shop.capnp), is an importable module.

You can import it as demonstrated in [burrito-shop.js](burrito-shop.js)

```javascript
import { BurritoShop } from "burrito-shop:burrito-shop";
```

#### Definition

This import definition is demonstrated in [burrito-shop.capnp](burrito-shop.capnp).

```capnp
...
( name = "burrito-shop:burrito-shop", esModule = embed "burrito-shop.js" )
...
```

### Environment Variable (with internal initialization from environment variables)

#### Accessibility

The module `burrito-shop:binding` is defined in the config [burrito-shop.capnp](burrito-shop.capnp) and is provided as an environment variable in standard `workerd` fashion. As we're using an esmodule it's provided as an argument to the workers entrypoint.

You can access it as shown below in [worker.js](worker.js)

```javascript
return new Response(env.shop.makeBurrito(burritoType).price());
```

The initialization for this module is demonstrated in [binding.js](binding.js), the default behavior of worker uses the exported function for initialization, and is called by `workerd`.

#### Definition

- The environment name of `shop` is provided in [config.capnp](config.capnp) with the field `name` located in the binding definition used by the worker.

```capnp
bindings = [
( 
    ...
    name = "shop"
    ...
)]
```

- **Note** An environment bindings module must be marked as internal, this is demonstrated in [burrito-shop.capnp](burrito-shop.capnp)

#### Using a exported function that isn't default as the entrypoint

A default exported entrypoint is not required for binding as long as you define a different entrypoint with `entrypoint = "methodname"`, for example you can define a non-default function as the entrypoint with `entrypoint = "makeMagicBurritoBinding"` in [config.capnp](config.capnp).  An example is provided below on how you could change the entrypoint.

In [binding.js](binding.js)

```javascript
export function makeMagicBurritoBinding(env) {
    return new BurritoShop(env.recipes);
}
```

In [config.capnp](config.capnp)

```capnp
(
  name = "shop",
  wrapped = (
    ...
    entrypoint = "makeMagicBurritoBinding" # The new entrypoint name
    ...
)
```

```

### File: src\cloudflare\README.md
```md
# Cloudflare specific modules

## tests

This codebase includes many unit tests. To run them, do:

```
bazel test  --test_output=all //src/cloudflare/...
```

Running just a specific module tests:

```
bazel test  --test_output=all //src/cloudflare/internal/test/aig/...
```

Running just eslint:

```
bazel test  --test_output=all //src/cloudflare:cloudflare@eslint
```

## Code formating

You need to format your code before opening a pull request, otherwise the CI will fail:

```
prettier src/cloudflare -w
prettier types/defines -w
```

```

### File: src\node\README.md
```md
# Node.js Compatibility

1. Node.js compatibility is best-effort. We intend to implement a subset of the Node.js API as closely as possible but we do not intend on being generally 100% compatible with Node.js as a whole.

1. For Web Platform Standard APIs, the standard spec is the source of truth. If Node.js implements those APIs differently, we will implement those differences in nodejs_compat mode ONLY if it can be done so in a backwards-compatible way or ONLY with an explicitly opt-in compatibility flag.

1. For Node.js APIs, Node.js is the source of truth. We will attempt, to the best of our ability within the constraints of our runtime, to implement the API as close to Node.js' defined behavior as possible. However, exceptions will be made when those cannot be implemented without breaking backwards compatibility. When Workers Runtime constraints, or this framework, make it impossible to implement a Node.js API in a manner that exactly matches Node.js, a best-effort attempt will be made to get as close as possible and any differences will be documented.

1. When a Node.js API overlaps (even partially) in functionality with a Workers runtime or Web Platform Standard API, there is no requirement that the Node.js API implementation conform to, or even be consistent with, the standard or runtime API as long as it does not conflict with those or force backwards compatibility issues. The existence of a Web Platform or Workers specific API will not rule out implementing the Node.js API even if functionally equivalent.

1. Just as we do with Web Platform APIs, we may choose not to implement some Node.js APIs simply because we decide they are not a good fit or experience for the Workers runtime environment (or, in some cases because doing so is simply not possible because of runtime constraints).

1. When implementing a Node.js API adds significant runtime, or development time, overhead, partial implementations can be merged and evolved incrementally, taking care to avoid breaking changes and using compatibility flags where appropriate. The emphasis will be on making smaller incremental improvements over time.

1. Enabling the nodejs_compat flag does not mean "all APIs work the way they do in Node.js" ... it just means that the Node.js APIs are available. When there is conflict between a Node.js API and a Web Platform API, or Workers-specific API, that is already implemented in the runtime, the Web Platform API / Workers API will take precedence. We may still implement the Node.js alternative behavior behind an explicitly opt-in compat flag.

1. For the global scope, Node.js APIs and behaviors are second to web platform APIs and other existing runtime globals. We will implement the Node.js specific globals only if they do not break backwards compatibility. We may implement such changes behind an explicitly opt-in compat flag.

1. We will seek to prioritize implementation of Node.js APIs that are needed by npm modules and other ecosystem dependencies that our customers want and are trying to use. When those modules require Node.js core APIs, we will implement those in accordance with this framework. In some cases that may mean it will not be possible to support the module as written. Like the Node.js APIs themselves, support will be best-effort. When we cannot fully implement support for these modules directly in the runtime, we will attempt to work with the maintainers of those modules to implement a workers-compatible alternative or work to develop alternative workarounds.

1. Polyfills of Node.js APIs (that is, external implementations that are not bundled directly into the workers runtime) may be leveraged by tooling as a last-resort alternative to patch over parts of the Node.js API we choose not to implement in the runtime. When used, these must be generally available for any Workers user, not only those using wrangler. The built-in implementation of Node.js APIs should always take precedence in general but individual workers should be able to BYOI ("bring your own implementation") within the reasonable constraints of the runtime. Cloudflare tooling should avoid polyfilling an API that already exists within the runtime, and the existence of a polyfill implementation will not rule out implementing the API directly in the runtime. At the same time, the existence of a polyfill implementation does not guarantee that the API will be implemented in the runtime and the existence of the runtime API does not guarantee that a polyfill will not be implemented. It is also not guaranteed that the runtime implementation of the API will match exactly the implementation of the polyfill. When new APIs are added to the runtime, the polyfill should be removed if it is no longer needed but the runtime will not itself take steps to remove the polyfill from the tooling.

1. Experimental APIs only recently added to Node.js should not be implemented immediately in the workers runtime. Such APIs may be unstable for some time and could cause long term backwards compatibility issues or other unfortunate complexities in the workers runtime due to our "No Breaking Changes Without Compatibility Flags" policy. It is better to allow these APIs to sit and mature a bit in the Node.js runtime to ensure they are stable before being implemented in the workers runtime. Exceptions can be made to address immediate priority use cases.

1. When a decision is made to explicit *not* implement a particular Node.js API, that decision should be documented. Attempts to use such APIs should result in a runtime error rather than silent failure or silently ignoring.

```

### File: src\workerd\README.md
```md
The subdirectories are organized as follows:

* **util:** Contains random unrelated utilities that don't depend on each other or the rest of the system.
* **jsg:** Contains magic template library for auto-generating FFI glue between C++ and V8 JavaScript.
* **io:** Generally contains code that handles the I/O layer which allows APIs to talk to the rest of the world. Also includes basic Worker lifecycle and event delivery.
* **api:** Contains implementations of publicly documented application-visible JavaScript APIs.
* **server:** Contains the high-level server implementation.
* **tools:** Contains additional meta-programs, notably a script for exporting API types. 
```

### File: .prettierrc.json
```json
{
  "printWidth": 80,
  "tabWidth": 2,
  "singleQuote": true,
  "trailingComma": "es5"
}

```

### File: AGENTS.md
```md
# AGENTS.md

This file provides guidance to Claude Code (claude.ai/code) or Opencode (opencode.ai) when working with code in this repository.

Subdirectory `AGENTS.md` files provide component-specific context (key classes, where-to-look tables, local conventions and anti-patterns).

## Instructions for AI Code Assistants

- Suggest updates to AGENTS.md when you find new high-level information
- You should always determine if the current repository was checked out standalone or as a submodule
  of the larger workers project.
- If checked out as a submodule, be aware that there is additional documentation and context in the
  root of that repository that is not present here. Look for the `../../README.md`, `../../AGENTS.md`,
  and other markdown files in the root of the parent repository.

## Project Overview

**workerd** is Cloudflare's JavaScript/WebAssembly server runtime that powers Cloudflare Workers. It's an open-source implementation of the same technology used in production at Cloudflare, designed for self-hosting applications, local development, and programmable HTTP proxy functionality.

## Build System & Commands

### Primary Build System: Bazel

- Main build command: `bazel build //src/workerd/server:workerd`
- Binary output: `bazel-bin/src/workerd/server/workerd`

### Just Commands (recommended for development)

- `just build` or `just b` - Build the project
- `just test` or `just t` - Run all tests
- `just format` or `just f` - Format code (uses clang-format + Python formatter)
- `just clippy <package>` - Run Rust clippy linter (e.g., `just clippy jsg-macros`)
- `just clang-tidy <target>` - Run clang-tidy on C++ code (e.g., `just clang-tidy //src/rust/jsg:ffi`)
- `just stream-test <target>` - Stream test output for debugging
- `just node-test <name>` - Run specific Node.js compatibility tests (e.g., `just node-test zlib`)
- `just wpt-test <name>` - Run Web Platform Tests (e.g., `just wpt-test urlpattern`)
- `just generate-types` - Generate TypeScript definitions
- `just compile-commands` - Generate compile_commands.json for clangd support
- `just build-asan` - Build with AddressSanitizer
- `just test-asan` - Run tests with AddressSanitizer
- `just new-test <target>` - Scaffold a new test (e.g., `just new-test //src/workerd/api/tests:my-test`)
- `just new-wpt-test <name>` - Scaffold a new WPT test
- `just lint` or `just eslint` - Run ESLint on TypeScript sources
- `just coverage <path>` - Generate code coverage report (Linux only, defaults to `//...`)
- `just watch <args>` - Watch `src/` and `build/` dirs, re-run a just command on changes

## Testing

### Test Types

- **`.wd-test` tests**: Cap'n Proto config files that define a `Workerd.Config` with embedded JS/TS modules. Bazel macro: `wd_test()`. See format details below.
- **C++ tests**: KJ-based unit tests (`.c++` files). Bazel macro: `kj_test()`.
- **Node.js compatibility tests**: `just node-test <test_name>`
- **Web Platform Tests**: `just wpt-test <test_name>`
- **Benchmarks**: `just bench <path>` (e.g., `just bench mimetype`)

### Running a Single Test

Both `just test` and `just build` accept specific Bazel targets (they default to `//...`):

```
just test //src/workerd/api/tests:encoding-test@
just test //src/workerd/io:io-gate-test@
just stream-test //src/workerd/api/tests:encoding-test@    # streams output for debugging
```

Or use Bazel directly:

```
bazel test //src/workerd/api/tests:encoding-test@
```

### Test Variants

Every test automatically generates multiple variants via the build macros:

- **`name@`** — default variant (oldest compat date, 2000-01-01)
- **`name@all-compat-flags`** — newest compat date (2999-12-31), tests with all flags enabled
- **`name@all-autogates`** — all autogates enabled + oldest compat date

The `@` suffix is required in target names. For example: `//src/workerd/io:io-gate-test@`, not `//src/workerd/io:io-gate-test`.

To find the right target name for a file, check the `BUILD.bazel` file in the same directory for `wd_test()` or `kj_test()` rules. You can also use Bazel query:

```
bazel query //src/workerd/api/tests:all    # list all targets in a package
```

### `.wd-test` File Format

`.wd-test` files are Cap'n Proto configs that define test workers:

```capnp
using Workerd = import "/workerd/workerd.capnp";

const unitTests :Workerd.Config = (
  services = [(
    name = "my-test",
    worker = (
      modules = [(name = "worker", esModule = embed "my-test.js")],
      compatibilityDate = "2024-01-01",
      compatibilityFlags = ["nodejs_compat"],
    ),
  )],
);
```

Key elements: `modules` (embed JS/TS files), `compatibilityFlags`, `bindings` (service bindings, JSON, KV, etc.), `durableObjectNamespaces`.

## Architecture

### Dependencies

- **Cap'n Proto source code** available in `external/capnp-cpp` - contains KJ C++ base library and
  capnproto RPC library. Consult it for all questions about `kj/` and `capnproto/` includes and
  `kj::` and `capnp::` namespaces.

The other core runtime dependencies include:

| Dependency                          | Description                                                         |
| ----------------------------------- | ------------------------------------------------------------------- |
| V8                                  | JavaScript engine                                                   |
| Cap'n Proto (capnp-cpp)             | Serialization/RPC framework and KJ base library                     |
| BoringSSL                           | TLS/crypto (Google's OpenSSL fork, patched for ncrypto/libdecrepit) |
| SQLite3                             | Embedded database                                                   |
| ICU (com_googlesource_chromium_icu) | Internationalization (Chromium fork)                                |
| zlib                                | Compression (Chromium fork, patched)                                |
| zstd                                | Zstandard compression                                               |
| brotli                              | Brotli compression                                                  |
| tcmalloc                            | Memory allocator                                                    |
| ada-url                             | URL parser                                                          |
| simdutf                             | Unicode transcoding (SIMD-accelerated)                              |
| nbytes                              | Node.js byte utilities                                              |
| ncrypto                             | Node.js crypto utilities                                            |
| perfetto                            | Tracing/profiling framework (patched)                               |
| fast_float                          | Fast float parsing                                                  |
| fp16                                | Half-precision float support                                        |
| highway                             | SIMD abstraction library                                            |
| dragonbox                           | Float-to-string conversion                                          |

These dependencies are vendored via Bazel into the `external/` directory. See `MODULE.bazel` and the `build/deps/` directory for how they are integrated into the build system. (The project uses bzlmod; the legacy `WORKSPACE` file may still exist but is no longer the primary mechanism.)

For several of these dependencies (notably V8, boringssl, sqlite, perfetto, and zlib), we maintain sets of patches that are applied on top of the upstream code. These patches are stored in the `patches/` directory and are applied during the build process. When updating these dependencies, it's important to review and update the corresponding patches as needed. The patches may introduce workerd-specific customizations and new APIs.

Be aware that workerd uses tcmalloc for memory allocation in the typical case. When analyzing memory usage or debugging memory issues, be aware that tcmalloc's behavior may differ from the standard allocator. Any memory usage analysis that you perform should take this into account.

### Core Directory Structure (`src/workerd/`)

- **`api/`** - Runtime APIs (HTTP, crypto, streams, WebSocket, etc.)
  - Contains C++ implementations of the core APIs exposed to JavaScript, as well as the Node.js compatibility layer
  - C++ portions of the Node.js compatibility layer are in `api/node/`, while the JavaScript and TypeScript implementations live in `src/node/`
  - Tests in `api/tests/` and `api/node/tests/`
  - TypeScript definitions are derived from C++ (which can have some annotations). This generation is handled by code in `types/` directory.

- **`io/`** - I/O subsystem, actor storage, threading, worker lifecycle
  - Actor storage and caching (`actor-cache.c++`, `actor-sqlite.c++`)
  - Request tracking and limits (`request-tracker.c++`, `limit-enforcer.h`)
- **`jsg/`** - JavaScript Glue layer for V8 integration
  - Core JavaScript engine bindings and type wrappers
  - Promise handling, memory management, module system
- **`server/`** - Main server implementation and configuration
  - Main binary entry point and Cap'n Proto config handling
- **`util/`** - Utility libraries (SQLite, UUID, threading, etc.)

### Multi-Language Support

- **`src/cloudflare/`** - Cloudflare-specific APIs (TypeScript)
- **`src/node/`** - Node.js compatibility layer (TypeScript)
- **`src/pyodide/`** - Python runtime support via Pyodide
- **`src/rust/`** - Rust integration components; see `src/rust/AGENTS.md` for the full macro reference and GC tracing guide

### Configuration System

- Uses **Cap'n Proto** for configuration files (`.capnp` format)
- Main schema: `src/workerd/server/workerd.capnp`
- Sample configurations in `samples/` directory
- Configuration uses capability-based security model

### Where to Look

| Task                   | Location                                                      | Notes                                                          |
| ---------------------- | ------------------------------------------------------------- | -------------------------------------------------------------- |
| Add/modify JS API      | `src/workerd/api/`                                            | C++ with JSG macros; see `jsg/jsg.h` for binding system        |
| Add Node.js compat     | `src/workerd/api/node/` (C++) + `src/node/` (TS)              | Dual-layer; register in `api/node/node.h` NODEJS_MODULES macro |
| Add Cloudflare API     | `src/cloudflare/`                                             | TypeScript; mock in `internal/test/<product>/`                 |
| Modify compat flags    | `src/workerd/io/compatibility-date.capnp`                     | ~1400 lines; annotations define flag names + enable dates      |
| Add autogate           | `src/workerd/util/autogate.h` + `.c++`                        | Enum + string map; both must stay in sync                      |
| Config schema          | `src/workerd/server/workerd.capnp`                            | Cap'n Proto; capability-based security                         |
| Worker lifecycle       | `src/workerd/io/worker.{h,c++}`                               | Isolate, Script, Worker, Actor classes                         |
| Request lifecycle      | `src/workerd/io/io-context.{h,c++}`                           | IoContext: the per-request god object                          |
| Durable Object storage | `src/workerd/io/actor-cache.{h,c++}` + `actor-sqlite.{h,c++}` | LRU cache over RPC / SQLite-backed                             |
| Streams implementation | `src/workerd/api/streams/`                                    | Has 842-line README; dual internal/standard impl               |
| Bazel build rules      | `build/`                                                      | Custom `wd_*` macros; `wd_test.bzl` generates 3 test variants  |
| TypeScript types       | `types/`                                                      | Extracted from C++ RTTI + hand-written `defines/*.d.ts`        |
| V8 patches             | `patches/v8/`                                                 | 33 patches; see `docs/v8-updates.md`                           |

## Coding Conventions

This project generally follows the [KJ Style Guide](https://github.com/capnproto/capnproto/blob/v2/kjdoc/style-guide.md) and [KJ Tour](https://github.com/capnproto/capnproto/blob/v2/kjdoc/tour.md), with one exception: comment style follows the more common idiomatic C++ patterns (e.g., `//` line comments) rather than KJ's comment conventions.

- **C++ standard**: C++23 (`-std=c++23`)
- **C++ file extensions**: `.c++` / `.h` (not `.cpp`); test suffix `-test` (hyphenated)
- **Formatting**: `just format` runs clang-format + prettier + ruff + buildifier + rustfmt
- **Pre-commit hook**: Blocks `KJ_DBG` in staged code; runs format check
- **Commit discipline**: Split PRs into small commits; each must compile + pass tests; no fixup commits
- **TypeScript**: Strict mode, `exactOptionalPropertyTypes`, private `#` syntax enforced, explicit return types

### Use KJ types, not STL

This project uses the KJ library instead of the C++ standard library for most types:

| Instead of              | Use                                                 |
| ----------------------- | --------------------------------------------------- |
| `std::string`           | `kj::String` (owned) / `kj::StringPtr` (view)       |
| `std::vector`           | `kj::Array<T>` (fixed) / `kj::Vector<T>` (growable) |
| `std::unique_ptr`       | `kj::Own<T>`                                        |
| `std::shared_ptr`       | `kj::Rc<T>` / `kj::Arc<T>` (thread-safe)            |
| `std::optional`         | `kj::Maybe<T>`                                      |
| `std::function`         | `kj::Function<T>`                                   |
| `std::variant`          | `kj::OneOf<T...>`                                   |
| `std::span` / array ref | `kj::ArrayPtr<T>`                                   |
| `std::exception`        | `kj::Exception`                                     |
| `std::promise`/`future` | `kj::Promise<T>` / `kj::ForkedPromise<T>`           |

### Error Handling

- `KJ_IF_SOME` for unwrapping `kj::Maybe` (1400+ uses across the codebase)
- `JSG_REQUIRE` / `JSG_FAIL_REQUIRE` for JS-facing errors with DOM exception types
- `KJ_ASSERT` / `KJ_REQUIRE` / `KJ_FAIL_ASSERT` for C++ assertions and preconditions

### JSG (JavaScript Glue)

C++ classes are exposed to JavaScript via JSG macros in `src/workerd/jsg/`. See the comprehensive guide at `src/workerd/jsg/README.md` for details. When adding or modifying JavaScript APIs, find a similar existing API and follow its pattern.

- `JSG_RESOURCE_TYPE` for reference types, `JSG_STRUCT` for value types
- `js.alloc<T>()` for resource allocation

### Feature Management

- **Compatibility flags** (`src/workerd/io/com
... [TRUNCATED]
```

### File: build-releases.sh
```sh
#! /bin/bash
set -euo pipefail

if [[ $(uname -m) == 'x86_64' ]]; then
  echo "This _must_ be run on an Apple Silicon machine, since the macOS ARM build cannot be dockerised due to macOS license restrictions"
  exit 1
fi

rm -f workerd-darwin-arm64 workerd-darwin-arm64.gz
rm -f workerd-linux-arm64 workerd-linux-arm64.gz

# Get the tag associated with the latest release, to ensure parity between binaries
TAG_NAME=$(curl -sL https://api.github.com/repos/cloudflare/workerd/releases/latest | jq -r ".tag_name")

git checkout $TAG_NAME

# Build macOS binary
pnpm exec bazel build --disk_cache=./.bazel-cache --config=release_macos //src/workerd/server:workerd

cp bazel-bin/src/workerd/server/workerd ./workerd-darwin-arm64

docker buildx build --platform linux/arm64 -f Dockerfile.release -t workerd:$TAG_NAME --target=artifact --output type=local,dest=$(pwd) .

chmod +x workerd*

mv workerd-darwin-arm64 workerd
gzip -9N workerd
mv workerd.gz workerd-darwin-arm64.gz

mv workerd-linux-arm64 workerd
gzip -9N workerd
mv workerd.gz workerd-linux-arm64.gz

```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
[workerd@cloudflare.com](mailto:workerd@cloudflare.com).
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.

```

### File: compile_flags.txt
```txt
-std=c++23
-stdlib=libc++
-xc++
-nostdinc
-Ibazel-bin/external/+new_local_repository+com_cloudflare_lol_html/_virtual_includes/lolhtml
-Ibazel-bin/external/perfetto+/
-Iexternal/ada-url+/
-Iexternal/abseil-cpp+/
-Iexternal/+http+simdutf/
-Iexternal/+http+nbytes/include/
-Iexternal/codspeed_google_benchmark_compat+/include/
-Iexternal/perfetto+/include/
-Iexternal/perfetto+/include/perfetto/base/build_configs/bazel/
-Iexternal/boringssl+/include
-Iexternal/+http+ncrypto/include
-isystembazel-bin/external/sqlite3+
-Isrc
-isystem/usr/lib/llvm-22/include/c++/v1
-isystem/usr/lib/llvm-22/lib/clang/22/include
-isystem/usr/lib/llvm-21/include/c++/v1
-isystem/usr/lib/llvm-21/lib/clang/21/include
-isystem/usr/lib/llvm-20/include/c++/v1
-isystem/usr/lib/llvm-20/lib/clang/20/include
-isystem/usr/lib/llvm-19/include/c++/v1
-isystem/usr/lib/llvm-19/lib/clang/19/include
-isystem/usr/include/x86_64-linux-gnu
-isystem/usr/include/aarch64-linux-gnu
-isystem/usr/include
-isystem/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/c++/v1
-isystem/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/clang/17/include
-isystem/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include
-isystem/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/System/Library/Frameworks/Kernel.framework/Versions/Current/Headers
-isystembazel-bin/_virtual_includes/icudata-embed
-isystembazel-bin/external/+http+capnp-cpp/src
-isystembazel-bin/external/+http+capnp-cpp/src/capnp/_virtual_includes/capnp
-isystembazel-bin/external/+http+capnp-cpp/src/capnp/_virtual_includes/capnp-rpc
-isystembazel-bin/external/+http+capnp-cpp/src/capnp/compat/_virtual_includes/http-over-capnp
-isystembazel-bin/external/+http+capnp-cpp/src/capnp/compat/_virtual_includes/json
-isystembazel-bin/external/+http+capnp-cpp/src/kj/_virtual_includes/kj
-isystembazel-bin/external/+http+capnp-cpp/src/kj/_virtual_includes/kj-async
-isystembazel-bin/external/+http+capnp-cpp/src/kj/compat/_virtual_includes/kj-brotli
-isystembazel-bin/external/+http+capnp-cpp/src/kj/compat/_virtual_includes/kj-gzip
-isystembazel-bin/external/+http+capnp-cpp/src/kj/compat/_virtual_includes/kj-http
-isystembazel-bin/external/+http+capnp-cpp/src/kj/compat/_virtual_includes/kj-tls
-isystembazel-bin/external/+http+workerd-cxx/_virtual_includes/core/
-isystembazel-bin/external/+http+workerd-cxx/kj-rs/_virtual_includes/kj-rs-lib/
-isystemexternal/+http_archive+v8/include
-isystemexternal/+http_archive+v8/include/cppgc
-isystemexternal/+_repo_rules2+v8/include
-isystemexternal/+_repo_rules2+v8/include/cppgc
-isystembazel-bin/src
-isystemexternal/brotli+/c/include
-isystembazel-bin/external/+git_repository+com_googlesource_chromium_icu/_virtual_includes/icu/third_party/icu/source/common
-isystemexternal/zlib+
-isystembazel-bin/src/rust/cxx-integration/_virtual_includes/lib.rs@cxx
-isystembazel-bin/src/rust/cxx-integration-test/_virtual_includes/lib.rs@cxx
-isystembazel-bin/src/rust/dns/_virtual_includes/lib.rs@cxx
-isystembazel-bin/src/rust/kj/_virtual_includes/ffi
-isystembazel-bin/src/rust/kj/_virtual_includes/http.rs@cxx
-isystembazel-bin/src/rust/kj/_virtual_includes/io.rs@cxx
-isystembazel-bin/src/rust/kj/tests/_virtual_includes/lib.rs@cxx
-isystembazel-bin/src/rust/python-parser/_virtual_includes/lib.rs@cxx
-isystembazel-bin/src/rust/net/_virtual_includes/lib.rs@cxx
-isystembazel-bin/src/rust/transpiler/_virtual_includes/lib.rs@cxx
-isystembazel-bin/src/rust/api/_virtual_includes/lib.rs@cxx
-isystembazel-bin/src/rust/jsg/_virtual_includes/ffi
-isystembazel-bin/src/rust/jsg/_virtual_includes/lib.rs@cxx
-isystembazel-bin/src/rust/jsg/_virtual_includes/v8.rs@cxx
-isystembazel-bin/src/rust/jsg-test/_virtual_includes/ffi-hdrs
-isystembazel-bin/src/rust/encoding/_virtual_includes/lib.rs@cxx
-isystembazel-bin/src/rust/jsg-test/_virtual_includes/lib.rs@cxx
-isystembazel-bin/src/rust/gen-compile-cache/_virtual_includes/cxx-bridge
-isystembazel-bin/src/rust/gen-compile-cache/_virtual_includes/gen-compile-cache@cxx
-D_FORTIFY_SOURCE=1
-D_LIBCPP_REMOVE_TRANSITIVE_INCLUDES
-D_LIBCPP_NO_ABI_TAG
-D_LIBCPP_HAS_NO_INCOMPLETE_PSTL
-DCAPNP_VERSION=11000
-DDEBUG
-DGOOGLE3
-DHAVE_DLOPEN=0
-DKJ_HAS_LIBDL
-DKJ_HAS_OPENSSL
-DKJ_HAS_ZLIB
-DKJ_SAVE_ACQUIRED_LOCK_INFO=0
-DKJ_TRACK_LOCK_BLOCKING=0
-DSQLITE_ENABLE_FTS5
-DSQLITE_ENABLE_NORMALIZE
-DSQLITE_MAX_ALLOCATION_SIZE=16777216
-DSQLITE_PRINTF_PRECISION_LIMIT=100000
-DUCONFIG_ONLY_HTML_CONVERSION=1
-DUNISTR_FROM_CHAR_EXPLICIT=
-DUNISTR_FROM_STRING_EXPLICIT=
-DUSE_CHROMIUM_ICU=1
-DU_CHARSET_IS_UTF8=1
-DU_COMMON_IMPLEMENTATION
-DU_ENABLE_DYLOAD=0
-DU_ENABLE_RESOURCE_TRACING=0
-DU_ENABLE_TRACING=1
-DU_I18N_IMPLEMENTATION
-DU_ICUDATAENTRY_IN_COMMON
-DU_USING_ICU_NAMESPACE=0
-DV8_31BIT_SMIS_ON_64BIT_ARCH
-DV8_ADVANCED_BIGINT_ALGORITHMS
-DV8_COMPRESS_POINTERS
-DV8_COMPRESS_POINTERS_IN_SHARED_CAGE
-DV8_CONCURRENT_MARKING
-DV8_DEPRECATION_WARNINGS
-DV8_ENABLE_CHECKS
-DV8_ENABLE_CONTINUATION_PRESERVED_EMBEDDER_DATA
-DV8_ENABLE_LAZY_SOURCE_POSITIONS
-DV8_ENABLE_MAGLEV
-DV8_ENABLE_SPARKPLUG
-DV8_ENABLE_TURBOFAN
-DV8_ENABLE_WEBASSEMBLY
-DV8_HAVE_TARGET_OS
-DV8_IMMINENT_DEPRECATION_WARNINGS
-DV8_SHORT_BUILTIN_CALLS
-DV8_TARGET_ARCH_X64
-DV8_TARGET_OS_LINUX
-DV8_TYPED_ARRAY_MAX_SIZE_IN_HEAP=64
-DWORKERD_USE_PERFETTO
-DPERFETTO_ENABLE_LEGACY_TRACE_EVENTS=1
-DWORKERD_ICU_DATA_EMBED
-Wall
-Werror=dangling
-Werror=implicit-fallthrough
-Werror=return-stack-address
-Werror=return-type
-Werror=switch
-Werror=uninitialized
-Werror=unreachable-code
-Werror=unused-function
-Werror=unused-lambda-capture
-Werror=unused-variable
-Wextra
-Wno-builtin-macro-redefined
-Wno-free-nonheap-object
-Wno-missing-field-initializers
-Wno-sign-compare
-Wno-unused-parameter
-Wself-assign
-Wthread-safety
-Wunused-but-set-parameter
-Wunused-function
-Wunused-lambda-capture
-Wunused-variable
-no-canonical-prefixes
-fbracket-depth=512

```

### File: CONTRIBUTING.md
```md
# Contributing to `workerd`

Before contributing code to `workerd`, please read these guidelines carefully.

## Questions? Use "discussions".

If you just want to ask a question or have an open-ended conversation, use the "discussions" tab rather than filing an issue. This way, the issues list stays restricted to action items

## Before you code: Discuss your change

This repository is the canonical source code for the core of Cloudflare Workers. The Workers team actively does their development in this repository. Any changes landed in the main branch will automatically become available on the Cloudflare Workers Platform typically within a week or two.

Cloudflare Workers has a [strong commitment to backwards-compatibility](https://blog.cloudflare.com/backwards-compatibility-in-cloudflare-workers/). Once a feature is in use on Cloudflare's platform, it generally cannot be taken away. The Workers team will be required to maintain the feature forever. (Note that we do not use semver and cannot just bump a major version number to introduce breaking changes -- [the blog post](https://blog.cloudflare.com/backwards-compatibility-in-cloudflare-workers/) explains why!)

As a result, we are cautious about what we add. Typically, inside Cloudflare, a new feature will be discussed by product managers and described in design docs long before any code is written.

What does that mean for external contributors? The most important thing is:

**For non-trivial changes, always post an issue or discussion before you write code.**

If you have a very specific proposal for which you're seeking approval, file an issue with the label "feature proposal". If your ideas are more open-ended, they may make sense as a discussion instead. Either way, we can then discuss whether we would accept the feature and, if so, give you some hints on how to implement it. We may ask you to write a design doc and do other preparatory work before we make a decision -- just as we would for any internal engineer making such a proposal.

Please note that we set an extremely high bar for new APIs that are not defined by standards. If you are proposing adding a new non-standard API, it is very likely we will decline. Conversely, if you are proposing adding support for an API that is defined by standards, it is an easier decision for us to accept it.

(For trivial changes, it is OK to go directly to filing a PR, with the understanding that the PR issue itself will serve as the place to discuss the change idea.)

## Hacking on the code

This codebase includes many unit tests. To run them, do:

```
bazel test //src/...
```

You may find it convenient to have Bazel automatically re-run every time you change a file. You can accomplish this using [watchexec](https://github.com/watchexec/watchexec) like so:

```
watchexec --restart --watch src bazel test //src/...
```

`workerd` is based on KJ, the C++ toolkit library underlying Cap'n Proto. Before writing code, we highly recommend you check out the [KJ style guide](https://github.com/capnproto/capnproto/blob/master/style-guide.md) and the [tour of KJ](https://github.com/capnproto/capnproto/blob/master/kjdoc/tour.md) to understand how to use KJ.

### Using Visual Studio Code for development

See [this guide](docs/vscode.md) for instructions on how to set up Visual Studio Code for development.

TODO: Add more on tooling best practices, etc.

## Pull requests and code review

The Cloudflare Workers project has a culture of careful code review. If we find your code hard to review, it's likely that it will take much longer to land, or may be declined entirely for this reason alone. We apply the same standards within our own team.

To make sure your pull request is as easy to review as possible:

* **Follow the style guide.** Please see the [KJ style guide](https://github.com/capnproto/capnproto/blob/master/style-guide.md) and the [tour of KJ](https://github.com/capnproto/capnproto/blob/master/kjdoc/tour.md) to understand how we write code.

* **Split PRs into small commits wherever possible**, especially when it helps the reviewers separate concerns. The code should compile and all tests should pass at every commit. For example, if you are adding a feature that requires refactoring some code, do the refactoring in a separate commit (or series of commits) from introducing the new feature. Each commit message should describe the particular bit of refactoring in the commit and why it was needed. It's especially important to use separate commits when moving and modifying code. If you need to move a large block of code from one place to another, try your best to do it in an individual commit that is purely a block cut/paste without making any modifications to the code. Then, actually modify the code in the next commit.

* **Don't push fixup commits.** When your reviewer asks for changes, they will want you to rewrite your branch history so that the commit history is clean. We don't want have "fixup commits" in our history, but we also don't want to squash-merge a clean commit series and lose the information it provides. You may want to familiarize yourself with `git commit --fixup` -- it makes it relatively easy to rewrite history.

* **Push fixups and rebases separately.** When a reviewer asks for changes, they will wan to review what you change separately from what was already written. It is very important, therefore, that any time you force-push an update to your PR, the push _either_ contains new changes of yours, _or_ rebases onto the latest version of the `main` branch, but _never_ both as the same time. If you do both at once, when your reviewer clicks the "view changes" button, they won't be able to tell which changes are yours vs. new changes to the main branch. In this case they may ask you to revert and try again.

* **Use three-way conflict markers.** Unfortunately, it is very hard for code reviewers to review conflict resolutions in general, and this can be a source of bugs. You can reduce the probability of bugs by making sure you've enabled three-way conflict markers in git, by running `git config --global merge.conflictstyle diff3`. This makes conflicts much easier to understand, by showing not just "yours" and "theirs", but also the original code from which both were derived.

* **Do not submit code you haven't tested.** If you are not able to build your code and run it locally to verify that it does what you expect, please do not submit code changes. Even the best programmers usually write code that doesn't work on the first try. If at all possible, include unit tests for any new functionality you add.

* **Write lots of comments.** Everyone knows that they should write comments, but a lot of programmers still don't do it. Do not expect your reviewers to learn what your code does by reading the implementation. By the time they get to implementation details, they should be simply confirming that they match what was promised. Every declaration in a header file should have a comment if its purpose isn't immediately obvious from the declaration name. (Do not write comments that simply state what is already obvious from the name.) In implementation code, you should have a comment every few lines saying what the next few lines are doing and describing any non-obvious concerns that the code needs to address.

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

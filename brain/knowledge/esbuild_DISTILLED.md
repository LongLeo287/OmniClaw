---
id: esbuild
type: knowledge
owner: OA_Triage
---
# esbuild
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./images/wordmark-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="./images/wordmark-light.svg">
    <img alt="esbuild: An extremely fast JavaScript bundler" src="./images/wordmark-light.svg">
  </picture>
  <br>
  <a href="https://esbuild.github.io/">Website</a> |
  <a href="https://esbuild.github.io/getting-started/">Getting started</a> |
  <a href="https://esbuild.github.io/api/">Documentation</a> |
  <a href="https://esbuild.github.io/plugins/">Plugins</a> |
  <a href="https://esbuild.github.io/faq/">FAQ</a>
</p>

## Why?

Our current build tools for the web are 10-100x slower than they could be:

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./images/benchmark-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="./images/benchmark-light.svg">
    <img alt="Bar chart with benchmark results" src="./images/benchmark-light.svg">
  </picture>
</p>

The main goal of the esbuild bundler project is to bring about a new era of build tool performance, and create an easy-to-use modern bundler along the way.

Major features:

- Extreme speed without needing a cache
- [JavaScript](https://esbuild.github.io/content-types/#javascript), [CSS](https://esbuild.github.io/content-types/#css), [TypeScript](https://esbuild.github.io/content-types/#typescript), and [JSX](https://esbuild.github.io/content-types/#jsx) built-in
- A straightforward [API](https://esbuild.github.io/api/) for CLI, JS, and Go
- Bundles ESM and CommonJS modules
- Bundles CSS including [CSS modules](https://github.com/css-modules/css-modules)
- Tree shaking, [minification](https://esbuild.github.io/api/#minify), and [source maps](https://esbuild.github.io/api/#sourcemap)
- [Local server](https://esbuild.github.io/api/#serve), [watch mode](https://esbuild.github.io/api/#watch), and [plugins](https://esbuild.github.io/plugins/)

Check out the [getting started](https://esbuild.github.io/getting-started/) instructions if you want to give esbuild a try.

```

### File: lib\package.json
```json
{
  "private": true,
  "dependencies": {
    "@types/node": "25.5.0",
    "typescript": "6.0.2"
  }
}

```

### File: lib\README.md
```md
This directory contains the TypeScript code that becomes the JavaScript API code in the `esbuild` and `esbuild-wasm` packages. It's automatically built during the build process for those packages (i.e. the top-level `make platform-neutral` and `make platform-wasm` commands).

```

### File: scripts\package.json
```json
{
  "dependencies": {
    "@types/node": "14.14.6",
    "@unicode/unicode-15.1.0": "1.5.2",
    "@unicode/unicode-3.0.0": "1.0.6",
    "fuse.js": "3.2.0",
    "js-yaml": "3.14.0",
    "react": "17.0.1",
    "source-map": "0.7.4",
    "typescript": "4.7.4"
  }
}

```

### File: CHANGELOG-2024.md
```md
# Changelog: 2024

This changelog documents all esbuild versions published in the year 2024 (versions 0.19.12 through 0.24.2).

## 0.24.2

* Fix regression with `--define` and `import.meta` ([#4010](https://github.com/evanw/esbuild/issues/4010), [#4012](https://github.com/evanw/esbuild/issues/4012), [#4013](https://github.com/evanw/esbuild/pull/4013))

    The previous change in version 0.24.1 to use a more expression-like parser for `define` values to allow quoted property names introduced a regression that removed the ability to use `--define:import.meta=...`. Even though `import` is normally a keyword that can't be used as an identifier, ES modules special-case the `import.meta` expression to behave like an identifier anyway. This change fixes the regression.

    This fix was contributed by [@sapphi-red](https://github.com/sapphi-red).

## 0.24.1

* Allow `es2024` as a target in `tsconfig.json` ([#4004](https://github.com/evanw/esbuild/issues/4004))

    TypeScript recently [added `es2024`](https://devblogs.microsoft.com/typescript/announcing-typescript-5-7/#support-for---target-es2024-and---lib-es2024) as a compilation target, so esbuild now supports this in the `target` field of `tsconfig.json` files, such as in the following configuration file:

    ```json
    {
      "compilerOptions": {
        "target": "ES2024"
      }
    }
    ```

    As a reminder, the only thing that esbuild uses this field for is determining whether or not to use legacy TypeScript behavior for class fields. You can read more in [the documentation](https://esbuild.github.io/content-types/#tsconfig-json).

    This fix was contributed by [@billyjanitsch](https://github.com/billyjanitsch).

* Allow automatic semicolon insertion after `get`/`set`

    This change fixes a grammar bug in the parser that incorrectly treated the following code as a syntax error:

    ```ts
    class Foo {
      get
      *x() {}
      set
      *y() {}
    }
    ```

    The above code will be considered valid starting with this release. This change to esbuild follows a [similar change to TypeScript](https://github.com/microsoft/TypeScript/pull/60225) which will allow this syntax starting with TypeScript 5.7.

* Allow quoted property names in `--define` and `--pure` ([#4008](https://github.com/evanw/esbuild/issues/4008))

    The `define` and `pure` API options now accept identifier expressions containing quoted property names. Previously all identifiers in the identifier expression had to be bare identifiers. This change now makes `--define` and `--pure` consistent with `--global-name`, which already supported quoted property names. For example, the following is now possible:

    ```js
    // The following code now transforms to "return true;\n"
    console.log(esbuild.transformSync(
      `return process.env['SOME-TEST-VAR']`,
      { define: { 'process.env["SOME-TEST-VAR"]': 'true' } },
    ))
    ```

    Note that if you're passing values like this on the command line using esbuild's `--define` flag, then you'll need to know how to escape quote characters for your shell. You may find esbuild's JavaScript API more ergonomic and portable than writing shell code.

* Minify empty `try`/`catch`/`finally` blocks ([#4003](https://github.com/evanw/esbuild/issues/4003))

    With this release, esbuild will now attempt to minify empty `try` blocks:

    ```js
    // Original code
    try {} catch { foo() } finally { bar() }

    // Old output (with --minify)
    try{}catch{foo()}finally{bar()}

    // New output (with --minify)
    bar();
    ```

    This can sometimes expose additional minification opportunities.

* Include `entryPoint` metadata for the `copy` loader ([#3985](https://github.com/evanw/esbuild/issues/3985))

    Almost all entry points already include a `entryPoint` field in the `outputs` map in esbuild's build metadata. However, this wasn't the case for the `copy` loader as that loader is a special-case that doesn't behave like other loaders. This release adds the `entryPoint` field in this case.

* Source mappings may now contain `null` entries ([#3310](https://github.com/evanw/esbuild/issues/3310), [#3878](https://github.com/evanw/esbuild/issues/3878))

    With this change, sources that result in an empty source map may now emit a `null` source mapping (i.e. one with a generated position but without a source index or original position). This change improves source map accuracy by fixing a problem where minified code from a source without any source mappings could potentially still be associated with a mapping from another source file earlier in the generated output on the same minified line. It manifests as nonsensical files in source mapped stack traces. Now the `null` mapping "resets" the source map so that any lookups into the minified code without any mappings resolves to `null` (which appears as the output file in stack traces) instead of the incorrect source file.

    This change shouldn't affect anything in most situations. I'm only mentioning it in the release notes in case it introduces a bug with source mapping. It's part of a work-in-progress future feature that will let you omit certain unimportant files from the generated source map to reduce source map size.

* Avoid using the parent directory name for determinism ([#3998](https://github.com/evanw/esbuild/issues/3998))

    To make generated code more readable, esbuild includes the name of the source file when generating certain variable names within the file. Specifically bundling a CommonJS file generates a variable to store the lazily-evaluated module initializer. However, if a file is named `index.js` (or with a different extension), esbuild will use the name of the parent directory instead for a better name (since many packages have files all named `index.js` but have unique directory names).

    This is problematic when the bundle entry point is named `index.js` and the parent directory name is non-deterministic (e.g. a temporary directory created by a build script). To avoid non-determinism in esbuild's output, esbuild will now use `index` instead of the parent directory in this case. Specifically this will happen if the parent directory is equal to esbuild's `outbase` API option, which defaults to the [lowest common ancestor](https://en.wikipedia.org/wiki/Lowest_common_ancestor) of all user-specified entry point paths.

* Experimental support for esbuild on NetBSD ([#3974](https://github.com/evanw/esbuild/pull/3974))

    With this release, esbuild now has a published binary executable for [NetBSD](https://www.netbsd.org/) in the [`@esbuild/netbsd-arm64`](https://www.npmjs.com/package/@esbuild/netbsd-arm64) npm package, and esbuild's installer has been modified to attempt to use it when on NetBSD. Hopefully this makes installing esbuild via npm work on NetBSD. This change was contributed by [@bsiegert](https://github.com/bsiegert).

    ⚠️ Note: NetBSD is not one of [Node's supported platforms](https://nodejs.org/api/process.html#process_process_platform), so installing esbuild may or may not work on NetBSD depending on how Node has been patched. This is not a problem with esbuild. ⚠️

## 0.24.0

**_This release deliberately contains backwards-incompatible changes._** To avoid automatically picking up releases like this, you should either be pinning the exact version of `esbuild` in your `package.json` file (recommended) or be using a version range syntax that only accepts patch upgrades such as `^0.23.0` or `~0.23.0`. See npm's documentation about [semver](https://docs.npmjs.com/cli/v6/using-npm/semver/) for more information.

* Drop support for older platforms ([#3902](https://github.com/evanw/esbuild/pull/3902))

    This release drops support for the following operating system:

    * macOS 10.15 Catalina

    This is because the Go programming language dropped support for this operating system version in Go 1.23, and this release updates esbuild from Go 1.22 to Go 1.23. Go 1.23 now requires macOS 11 Big Sur or later.

    Note that this only affects the binary esbuild executables that are published to the esbuild npm package. It's still possible to compile esbuild's source code for these older operating systems. If you need to, you can compile esbuild for yourself using an older version of the Go compiler (before Go version 1.23). That might look something like this:

    ```
    git clone https://github.com/evanw/esbuild.git
    cd esbuild
    go build ./cmd/esbuild
    ./esbuild --version
    ```

* Fix class field decorators in TypeScript if `useDefineForClassFields` is `false` ([#3913](https://github.com/evanw/esbuild/issues/3913))

    Setting the `useDefineForClassFields` flag to `false` in `tsconfig.json` means class fields use the legacy TypeScript behavior instead of the standard JavaScript behavior. Specifically they use assign semantics instead of define semantics (e.g. setters are triggered) and fields without an initializer are not initialized at all. However, when this legacy behavior is combined with standard JavaScript decorators, TypeScript switches to always initializing all fields, even those without initializers. Previously esbuild incorrectly continued to omit field initializers for this edge case. These field initializers in this case should now be emitted starting with this release.

* Avoid incorrect cycle warning with `tsconfig.json` multiple inheritance ([#3898](https://github.com/evanw/esbuild/issues/3898))

    TypeScript 5.0 introduced multiple inheritance for `tsconfig.json` files where `extends` can be an array of file paths. Previously esbuild would incorrectly treat files encountered more than once when processing separate subtrees of the multiple inheritance hierarchy as an inheritance cycle. With this release, `tsconfig.json` files containing this edge case should work correctly without generating a warning.

* Handle Yarn Plug'n'Play stack overflow with `tsconfig.json` ([#3915](https://github.com/evanw/esbuild/issues/3915))

    Previously a `tsconfig.json` file that `extends` another file in a package with an `exports` map could cause a stack overflow when Yarn's Plug'n'Play resolution was active. This edge case should work now starting with this release.

* Work around more issues with Deno 1.31+ ([#3917](https://github.com/evanw/esbuild/pull/3917))

    This version of Deno broke the `stdin` and `stdout` properties on command objects for inherited streams, which matters when you run esbuild's Deno module as the entry point (i.e. when `import.meta.main` is `true`). Previously esbuild would crash in Deno 1.31+ if you ran esbuild like that. This should be fixed starting with this release.

    This fix was contributed by [@Joshix-1](https://github.com/Joshix-1).

## 0.23.1

* Allow using the `node:` import prefix with `es*` targets ([#3821](https://github.com/evanw/esbuild/issues/3821))

    The [`node:` prefix on imports](https://nodejs.org/api/esm.html#node-imports) is an alternate way to import built-in node modules. For example, `import fs from "fs"` can also be written `import fs from "node:fs"`. This only works with certain newer versions of node, so esbuild removes it when you target older versions of node such as with `--target=node14` so that your code still works. With the way esbuild's platform-specific feature compatibility table works, this was added by saying that only newer versions of node support this feature. However, that means that a target such as `--target=node18,es2022` removes the `node:` prefix because none of the `es*` targets are known to support this feature. This release adds the support for the `node:` flag to esbuild's internal compatibility table for `es*` to allow you to use compound targets like this:

    ```js
    // Original code
    import fs from 'node:fs'
    fs.open

    // Old output (with --bundle --format=esm --platform=node --target=node18,es2022)
    import fs from "fs";
    fs.open;

    // New output (with --bundle --format=esm --platform=node --target=node18,es2022)
    import fs from "node:fs";
    fs.open;
    ```

* Fix a panic when using the CLI with invalid build flags if `--analyze` is present ([#3834](https://github.com/evanw/esbuild/issues/3834))

    Previously esbuild's CLI could crash if it was invoked with flags that aren't valid for a "build" API call and the `--analyze` flag is present. This was caused by esbuild's internals attempting to add a Go plugin (which is how `--analyze` is implemented) to a null build object. The panic has been fixed in this release.

* Fix incorrect location of certain error messages ([#3845](https://github.com/evanw/esbuild/issues/3845))

    This release fixes a regression that caused certain errors relating to variable declarations to be reported at an incorrect location. The regression was introduced in version 0.18.7 of esbuild.

* Print comments before case clauses in switch statements ([#3838](https://github.com/evanw/esbuild/issues/3838))

    With this release, esbuild will attempt to print comments that come before case clauses in switch statements. This is similar to what esbuild already does for comments inside of certain types of expressions. Note that these types of comments are not printed if minification is enabled (specifically whitespace minification).

* Fix a memory leak with `pluginData` ([#3825](https://github.com/evanw/esbuild/issues/3825))

    With this release, the build context's internal `pluginData` cache will now be cleared when starting a new build. This should fix a leak of memory from plugins that return `pluginData` objects from `onResolve` and/or `onLoad` callbacks.

## 0.23.0

**_This release deliberately contains backwards-incompatible changes._** To avoid automatically picking up releases like this, you should either be pinning the exact version of `esbuild` in your `package.json` file (recommended) or be using a version range syntax that only accepts patch upgrades such as `^0.22.0` or `~0.22.0`. See npm's documentation about [semver](https://docs.npmjs.com/cli/v6/using-npm/semver/) for more information.

* Revert the recent change to avoid bundling dependencies for node ([#3819](https://github.com/evanw/esbuild/issues/3819))

    This release reverts the recent change in version 0.22.0 that made `--packages=external` the default behavior with `--platform=node`.  The default is now back to `--packages=bundle`.

    I've just been made aware that Amazon doesn't pin their dependencies in their "AWS CDK" product, which means that whenever esbuild publishes a new release, many people (potentially everyone?) using their SDK around the world instantly starts using it without Amazon checking that it works first. This change in version 0.22.0 happened to break their SDK. I'm amazed that things haven't broken before this point. This revert attempts to avoid these problems for Amazon's customers. Hopefully Amazon will pin their dependencies in the future.

    In addition, this is probably a sign that e
... [TRUNCATED]
```

### File: CHANGELOG-2025.md
```md
# Changelog: 2025

This changelog documents all esbuild versions published in the year 2025 (versions 0.25.0 through 0.27.2).

## 0.27.2

* Allow import path specifiers starting with `#/` ([#4361](https://github.com/evanw/esbuild/pull/4361))

    Previously the specification for `package.json` disallowed import path specifiers starting with `#/`, but this restriction [has recently been relaxed](https://github.com/nodejs/node/pull/60864) and support for it is being added across the JavaScript ecosystem. One use case is using it for a wildcard pattern such as mapping `#/*` to `./src/*` (previously you had to use another character such as `#_*` instead, which was more confusing). There is some more context in [nodejs/node#49182](https://github.com/nodejs/node/issues/49182).

    This change was contributed by [@hybrist](https://github.com/hybrist).

* Automatically add the `-webkit-mask` prefix ([#4357](https://github.com/evanw/esbuild/issues/4357), [#4358](https://github.com/evanw/esbuild/issues/4358))

    This release automatically adds the `-webkit-` vendor prefix for the [`mask`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask) CSS shorthand property:

    ```css
    /* Original code */
    main {
      mask: url(x.png) center/5rem no-repeat
    }

    /* Old output (with --target=chrome110) */
    main {
      mask: url(x.png) center/5rem no-repeat;
    }

    /* New output (with --target=chrome110) */
    main {
      -webkit-mask: url(x.png) center/5rem no-repeat;
      mask: url(x.png) center/5rem no-repeat;
    }
    ```

    This change was contributed by [@BPJEnnova](https://github.com/BPJEnnova).

* Additional minification of `switch` statements ([#4176](https://github.com/evanw/esbuild/issues/4176), [#4359](https://github.com/evanw/esbuild/issues/4359))

    This release contains additional minification patterns for reducing `switch` statements. Here is an example:

    ```js
    // Original code
    switch (x) {
      case 0:
        foo()
        break
      case 1:
      default:
        bar()
    }

    // Old output (with --minify)
    switch(x){case 0:foo();break;case 1:default:bar()}

    // New output (with --minify)
    x===0?foo():bar();
    ```

* Forbid `using` declarations inside `switch` clauses ([#4323](https://github.com/evanw/esbuild/issues/4323))

    This is a rare change to remove something that was previously possible. The [Explicit Resource Management](https://github.com/tc39/proposal-explicit-resource-management) proposal introduced `using` declarations. These were previously allowed inside `case` and `default` clauses in `switch` statements. This had well-defined semantics and was already widely implemented (by V8, SpiderMonkey, TypeScript, esbuild, and others). However, it was considered to be too confusing because of how scope works in switch statements, so it has been removed from the specification. This edge case will now be a syntax error. See [tc39/proposal-explicit-resource-management#215](https://github.com/tc39/proposal-explicit-resource-management/issues/215) and [rbuckton/ecma262#14](https://github.com/rbuckton/ecma262/pull/14) for details.

    Here is an example of code that is no longer allowed:

    ```js
    switch (mode) {
      case 'read':
        using readLock = db.read()
        return readAll(readLock)

      case 'write':
        using writeLock = db.write()
        return writeAll(writeLock)
    }
    ```

    That code will now have to be modified to look like this instead (note the additional `{` and `}` block statements around each case body):

    ```js
    switch (mode) {
      case 'read': {
        using readLock = db.read()
        return readAll(readLock)
      }
      case 'write': {
        using writeLock = db.write()
        return writeAll(writeLock)
      }
    }
    ```

    This is not being released in one of esbuild's breaking change releases since this feature hasn't been finalized yet, and esbuild always tracks the current state of the specification (so esbuild's previous behavior was arguably incorrect).

## 0.27.1

* Fix bundler bug with `var` nested inside `if` ([#4348](https://github.com/evanw/esbuild/issues/4348))

    This release fixes a bug with the bundler that happens when importing an ES module using `require` (which causes it to be wrapped) and there's a top-level `var` inside an `if` statement without being wrapped in a `{ ... }` block (and a few other conditions). The bundling transform needed to hoist these `var` declarations outside of the lazy ES module wrapper for correctness. See the issue for details.

* Fix minifier bug with `for` inside `try` inside label ([#4351](https://github.com/evanw/esbuild/issues/4351))

    This fixes an old regression from [version v0.21.4](https://github.com/evanw/esbuild/releases/v0.21.4). Some code was introduced to move the label inside the `try` statement to address a problem with transforming labeled `for await` loops to avoid the `await` (the transformation involves converting the `for await` loop into a `for` loop and wrapping it in a `try` statement). However, it introduces problems for cross-compiled JVM code that uses all three of these features heavily. This release restricts this transform to only apply to `for` loops that esbuild itself generates internally as part of the `for await` transform. Here is an example of some affected code:

    ```js
    // Original code
    d: {
      e: {
        try {
          while (1) { break d }
        } catch { break e; }
      }
    }

    // Old output (with --minify)
    a:try{e:for(;;)break a}catch{break e}

    // New output (with --minify)
    a:e:try{for(;;)break a}catch{break e}
    ```

* Inline IIFEs containing a single expression ([#4354](https://github.com/evanw/esbuild/issues/4354))

    Previously inlining of IIFEs (immediately-invoked function expressions) only worked if the body contained a single `return` statement. Now it should also work if the body contains a single expression statement instead:

    ```js
    // Original code
    const foo = () => {
      const cb = () => {
        console.log(x())
      }
      return cb()
    }

    // Old output (with --minify)
    const foo=()=>(()=>{console.log(x())})();

    // New output (with --minify)
    const foo=()=>{console.log(x())};
    ```

* The minifier now strips empty `finally` clauses ([#4353](https://github.com/evanw/esbuild/issues/4353))

    This improvement means that `finally` clauses containing dead code can potentially cause the associated `try` statement to be removed from the output entirely in minified builds:

    ```js
    // Original code
    function foo(callback) {
      if (DEBUG) stack.push(callback.name);
      try {
        callback();
      } finally {
        if (DEBUG) stack.pop();
      }
    }

    // Old output (with --minify --define:DEBUG=false)
    function foo(a){try{a()}finally{}}

    // New output (with --minify --define:DEBUG=false)
    function foo(a){a()}
    ```

* Allow tree-shaking of the `Symbol` constructor

    With this release, calling `Symbol` is now considered to be side-effect free when the argument is known to be a primitive value. This means esbuild can now tree-shake module-level symbol variables:

    ```js
    // Original code
    const a = Symbol('foo')
    const b = Symbol(bar)

    // Old output (with --tree-shaking=true)
    const a = Symbol("foo");
    const b = Symbol(bar);

    // New output (with --tree-shaking=true)
    const b = Symbol(bar);
    ```

## 0.27.0

**This release deliberately contains backwards-incompatible changes.** To avoid automatically picking up releases like this, you should either be pinning the exact version of `esbuild` in your `package.json` file (recommended) or be using a version range syntax that only accepts patch upgrades such as `^0.26.0` or `~0.26.0`. See npm's documentation about [semver](https://docs.npmjs.com/cli/v6/using-npm/semver/) for more information.

* Use `Uint8Array.fromBase64` if available ([#4286](https://github.com/evanw/esbuild/issues/4286))

    With this release, esbuild's `binary` loader will now use the new [`Uint8Array.fromBase64`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64) function unless it's unavailable in the configured target environment. If it's unavailable, esbuild's previous code for this will be used as a fallback. Note that this means you may now need to specify `target` when using this feature with Node (for example `--target=node22`) unless you're using Node v25+.

* Update the Go compiler from v1.23.12 to v1.25.4 ([#4208](https://github.com/evanw/esbuild/issues/4208), [#4311](https://github.com/evanw/esbuild/pull/4311))

    This raises the operating system requirements for running esbuild:

    * Linux: now requires a kernel version of 3.2 or later
    * macOS: now requires macOS 12 (Monterey) or later

## 0.26.0

* Enable trusted publishing ([#4281](https://github.com/evanw/esbuild/issues/4281))

    GitHub and npm are recommending that maintainers for packages such as esbuild switch to [trusted publishing](https://docs.npmjs.com/trusted-publishers). With this release, a VM on GitHub will now build and publish all of esbuild's packages to npm instead of me. In theory.

    Unfortunately there isn't really a way to test that this works other than to do it live. So this release is that live test. Hopefully this release is uneventful and is exactly the same as the previous one (well, except for the green provenance attestation checkmark on npm that happens with trusted publishing).

## 0.25.12

* Fix a minification regression with CSS media queries ([#4315](https://github.com/evanw/esbuild/issues/4315))

    The previous release introduced support for parsing media queries which unintentionally introduced a regression with the removal of duplicate media rules during minification. Specifically the grammar for `@media <media-type> and <media-condition-without-or> { ... }` was missing an equality check for the `<media-condition-without-or>` part, so rules with different suffix clauses in this position would incorrectly compare equal and be deduplicated. This release fixes the regression.

* Update the list of known JavaScript globals ([#4310](https://github.com/evanw/esbuild/issues/4310))

    This release updates esbuild's internal list of known JavaScript globals. These are globals that are known to not have side-effects when the property is accessed. For example, accessing the global `Array` property is considered to be side-effect free but accessing the global `scrollY` property can trigger a layout, which is a side-effect. This is used by esbuild's tree-shaking to safely remove unused code that is known to be side-effect free. This update adds the following global properties:

    From [ES2017](https://tc39.es/ecma262/2017/):
    - `Atomics`
    - `SharedArrayBuffer`

    From [ES2020](https://tc39.es/ecma262/2020/):
    - `BigInt64Array`
    - `BigUint64Array`

    From [ES2021](https://tc39.es/ecma262/2021/):
    - `FinalizationRegistry`
    - `WeakRef`

    From [ES2025](https://tc39.es/ecma262/2025/):
    - `Float16Array`
    - `Iterator`

    Note that this does not indicate that constructing any of these objects is side-effect free, just that accessing the identifier is side-effect free. For example, this now allows esbuild to tree-shake classes that extend from `Iterator`:

    ```js
    // This can now be tree-shaken by esbuild:
    class ExampleIterator extends Iterator {}
    ```

* Add support for the new `@view-transition` CSS rule ([#4313](https://github.com/evanw/esbuild/pull/4313))

    With this release, esbuild now has improved support for pretty-printing and minifying the new `@view-transition` rule (which esbuild was previously unaware of):

    ```css
    /* Original code */
    @view-transition {
      navigation: auto;
      types: check;
    }

    /* Old output */
    @view-transition { navigation: auto; types: check; }

    /* New output */
    @view-transition {
      navigation: auto;
      types: check;
    }
    ```

    The new view transition feature provides a mechanism for creating animated transitions between documents in a multi-page app. You can read more about view transition rules [here](https://developer.mozilla.org/en-US/docs/Web/CSS/@view-transition).

    This change was contributed by [@yisibl](https://github.com/yisibl).

* Trim CSS rules that will never match

    The CSS minifier will now remove rules whose selectors contain `:is()` and `:where()` as those selectors will never match. These selectors can currently be automatically generated by esbuild when you give esbuild nonsensical input such as the following:

    ```css
    /* Original code */
    div:before {
      color: green;
      &.foo {
        color: red;
      }
    }

    /* Old output (with --supported:nesting=false --minify) */
    div:before{color:green}:is().foo{color:red}

    /* New output (with --supported:nesting=false --minify) */
    div:before{color:green}
    ```

    This input is nonsensical because CSS nesting is (unfortunately) not supported inside of pseudo-elements such as `:before`. Currently esbuild generates a rule containing `:is()` in this case when you tell esbuild to transform nested CSS into non-nested CSS. I think it's reasonable to do that as it sort of helps explain what's going on (or at least indicates that something is wrong in the output). It shouldn't be present in minified code, however, so this release now strips it out.

## 0.25.11

* Add support for `with { type: 'bytes' }` imports ([#4292](https://github.com/evanw/esbuild/issues/4292))

    The [import bytes](https://github.com/tc39/proposal-import-bytes) proposal has reached stage 2.7 in the TC39 process, which means that although it isn't quite recommended for implementation, it's generally approved and ready for validation. Furthermore it has already been implemented by [Deno](https://docs.deno.com/examples/importing_bytes/) and [Webpack](https://github.com/webpack/webpack/pull/19928). So with this release, esbuild will also add support for this. It behaves exactly the same as esbuild's existing [`binary` loader](https://esbuild.github.io/content-types/#binary). Here's an example:

    ```js
    import data from './image.png' with { type: 'bytes' }
    const view = new DataView(data.buffer, 0, 24)
    const width = view.getInt32(16)
    const height = view.getInt32(20)
    console.log('size:', width + '\xD7' + height)
    ```

* Lower CSS media query range syntax ([#3748](https://github.com/evanw/esbuild/issues/3748), [#4293](https://github.com/evanw/esbuild/issues/4293))

    With this release, esbuild will now transform CSS media query range syntax into equivalent syntax using `min-`/`max-` prefixes for older browsers. For example, the following CSS:

    ```css
    @media (640px <= width <= 960px) {
      main {
        display: flex;
      }
 
... [TRUNCATED]
```

### File: CHANGELOG.md
```md
# Changelog

## 0.28.0

* Add support for `with { type: 'text' }` imports ([#4435](https://github.com/evanw/esbuild/issues/4435))

    The [import text](https://github.com/tc39/proposal-import-text) proposal has reached stage 3 in the TC39 process, which means that it's recommended for implementation. It has also already been implemented by [Deno](https://docs.deno.com/examples/importing_text/) and [Bun](https://bun.com/docs/guides/runtime/import-html). So with this release, esbuild also adds support for it. This behaves exactly the same as esbuild's existing [`text` loader](https://esbuild.github.io/content-types/#text). Here's an example:

    ```js
    import string from './example.txt' with { type: 'text' }
    console.log(string)
    ```

* Add integrity checks to fallback download path ([#4343](https://github.com/evanw/esbuild/issues/4343))

    Installing esbuild via npm is somewhat complicated with several different edge cases (see [esbuild's documentation](https://esbuild.github.io/getting-started/#additional-npm-flags) for details). If the regular installation of esbuild's platform-specific package fails, esbuild's install script attempts to download the platform-specific package itself (first with the `npm` command, and then with a HTTP request to `registry.npmjs.org` as a last resort).

    This last resort path previously didn't have any integrity checks. With this release, esbuild will now verify that the hash of the downloaded binary matches the expected hash for the current release. This means the hashes for all of esbuild's platform-specific binary packages will now be embedded in the top-level `esbuild` package. Hopefully this should work without any problems. But just in case, this change is being done as a breaking change release.

* Update the Go compiler from 1.25.7 to 1.26.1

    This upgrade should not affect anything. However, there have been some significant internal changes to the Go compiler, so esbuild could potentially behave differently in certain edge cases:

    - It now uses the [new garbage collector](https://go.dev/doc/go1.26#new-garbage-collector) that comes with Go 1.26.
    - The Go compiler is now more aggressive with allocating memory on the stack.
    - The executable format that the Go linker uses has undergone several changes.
    - The WebAssembly build now unconditionally makes use of the sign extension and non-trapping floating-point to integer conversion instructions.

    You can read the [Go 1.26 release notes](https://go.dev/doc/go1.26) for more information.

## 0.27.7

* Fix lowering of define semantics for TypeScript parameter properties ([#4421](https://github.com/evanw/esbuild/issues/4421))

    The previous release incorrectly generated class fields for TypeScript parameter properties even when the configured target environment does not support class fields. With this release, the generated class fields will now be correctly lowered in this case:

    ```ts
    // Original code
    class Foo {
      constructor(public x = 1) {}
      y = 2
    }

    // Old output (with --loader=ts --target=es2021)
    class Foo {
      constructor(x = 1) {
        this.x = x;
        __publicField(this, "y", 2);
      }
      x;
    }

    // New output (with --loader=ts --target=es2021)
    class Foo {
      constructor(x = 1) {
        __publicField(this, "x", x);
        __publicField(this, "y", 2);
      }
    }
    ```

## 0.27.5

* Fix for an async generator edge case ([#4401](https://github.com/evanw/esbuild/issues/4401), [#4417](https://github.com/evanw/esbuild/pull/4417))

    Support for transforming async generators into the equivalent state machine was added in version 0.19.0. However, the generated state machine didn't work correctly when polling async generators concurrently, such as in the following code:

    ```js
    async function* inner() { yield 1; yield 2 }
    async function* outer() { yield* inner() }
    let gen = outer()
    for await (let x of [gen.next(), gen.next()]) console.log(x)
    ```

    Previously esbuild's output of the above code behaved incorrectly when async generators were transformed (such as with `--supported:async-generator=false`). The transformation should be fixed starting with this release.

    This fix was contributed by [@2767mr](https://github.com/2767mr).

* Fix a regression when `metafile` is enabled ([#4420](https://github.com/evanw/esbuild/issues/4420), [#4418](https://github.com/evanw/esbuild/pull/4418))

    This release fixes a regression introduced by the previous release. When `metafile: true` was enabled in esbuild's JavaScript API, builds with build errors were incorrectly throwing an error about an empty JSON string instead of an object containing the build errors.

* Use define semantics for TypeScript parameter properties ([#4421](https://github.com/evanw/esbuild/issues/4421))

    Parameter properties are a TypeScript-specific code generation feature that converts constructor parameters into class fields when they are prefixed by certain keywords. When `"useDefineForClassFields": true` is present in `tsconfig.json`, the TypeScript compiler automatically generates class field declarations for parameter properties. Previously esbuild didn't do this, but esbuild will now do this starting with this release:

    ```ts
    // Original code
    class Foo {
      constructor(public x: number) {}
    }

    // Old output (with --loader=ts)
    class Foo {
      constructor(x) {
        this.x = x;
      }
    }

    // New output (with --loader=ts)
    class Foo {
      constructor(x) {
        this.x = x;
      }
      x;
    }
    ```

* Allow `es2025` as a target in `tsconfig.json` ([#4432](https://github.com/evanw/esbuild/issues/4432))

    TypeScript recently [added `es2025`](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/#es2025-option-for-target-and-lib) as a compilation target, so esbuild now supports this in the `target` field of `tsconfig.json` files, such as in the following configuration file:

    ```json
    {
      "compilerOptions": {
        "target": "ES2025"
      }
    }
    ```

    As a reminder, the only thing that esbuild uses this field for is determining whether or not to use legacy TypeScript behavior for class fields. You can read more in [the documentation](https://esbuild.github.io/content-types/#tsconfig-json).

## 0.27.4

* Fix a regression with CSS media queries ([#4395](https://github.com/evanw/esbuild/issues/4395), [#4405](https://github.com/evanw/esbuild/issues/4405), [#4406](https://github.com/evanw/esbuild/issues/4406))

    Version 0.25.11 of esbuild introduced support for parsing media queries. This unintentionally introduced a regression with printing media queries that use the `<media-type> and <media-condition-without-or>` grammar. Specifically, esbuild was failing to wrap an `or` clause with parentheses when inside `<media-condition-without-or>`. This release fixes the regression.

    Here is an example:

    ```css
    /* Original code */
    @media only screen and ((min-width: 10px) or (min-height: 10px)) {
      a { color: red }
    }

    /* Old output (incorrect) */
    @media only screen and (min-width: 10px) or (min-height: 10px) {
      a {
        color: red;
      }
    }

    /* New output (correct) */
    @media only screen and ((min-width: 10px) or (min-height: 10px)) {
      a {
        color: red;
      }
    }
    ```

* Fix an edge case with the `inject` feature ([#4407](https://github.com/evanw/esbuild/issues/4407))

    This release fixes an edge case where esbuild's `inject` feature could not be used with arbitrary module namespace names exported using an `export {} from` statement with bundling disabled and a target environment where arbitrary module namespace names is unsupported.

    With the fix, the following `inject` file:

    ```js
    import jquery from 'jquery';
    export { jquery as 'window.jQuery' };
    ```

    Can now always be rewritten as this without esbuild sometimes incorrectly generating an error:

    ```js
    export { default as 'window.jQuery' } from 'jquery';
    ```

* Attempt to improve API handling of huge metafiles ([#4329](https://github.com/evanw/esbuild/issues/4329), [#4415](https://github.com/evanw/esbuild/issues/4415))

    This release contains a few changes that attempt to improve the behavior of esbuild's JavaScript API with huge metafiles (esbuild's name for the build metadata, formatted as a JSON object). The JavaScript API is designed to return the metafile JSON as a JavaScript object in memory, which makes it easy to access from within a JavaScript-based plugin. Multiple people have encountered issues where this API breaks down with a pathologically-large metafile.

    The primary issue is that V8 has an implementation-specific maximum string length, so using the `JSON.parse` API with large enough strings is impossible. This release will now attempt to use a fallback JavaScript-based JSON parser that operates directly on the UTF8-encoded JSON bytes instead of using `JSON.parse` when the JSON metafile is too big to fit in a JavaScript string. The new fallback path has not yet been heavily-tested. The metafile will also now be generated with whitespace removed if the bundle is significantly large, which will reduce the size of the metafile JSON slightly.

    However, hitting this case is potentially a sign that something else is wrong. Ideally you wouldn't be building something so enormous that the build metadata can't even fit inside a JavaScript string. You may want to consider optimizing your project, or breaking up your project into multiple parts that are built independently. Another option could potentially be to use esbuild's command-line API instead of its JavaScript API, which is more efficient (although of course then you can't use JavaScript plugins, so it may not be an option).

## 0.27.3

* Preserve URL fragments in data URLs ([#4370](https://github.com/evanw/esbuild/issues/4370))

    Consider the following HTML, CSS, and SVG:

    * `index.html`:

        ```html
        <!DOCTYPE html>
        <html>
          <head><link rel="stylesheet" href="icons.css"></head>
          <body><div class="triangle"></div></body>
        </html>
        ```

    * `icons.css`:

        ```css
        .triangle {
          width: 10px;
          height: 10px;
          background: currentColor;
          clip-path: url(./triangle.svg#x);
        }
        ```

    * `triangle.svg`:

        ```xml
        <svg xmlns="http://www.w3.org/2000/svg">
          <defs>
            <clipPath id="x">
              <path d="M0 0H10V10Z"/>
            </clipPath>
          </defs>
        </svg>
        ```

    The CSS uses a URL fragment (the `#x`) to reference the `clipPath` element in the SVG file. Previously esbuild's CSS bundler didn't preserve the URL fragment when bundling the SVG using the `dataurl` loader, which broke the bundled CSS. With this release, esbuild will now preserve the URL fragment in the bundled CSS:

    ```css
    /* icons.css */
    .triangle {
      width: 10px;
      height: 10px;
      background: currentColor;
      clip-path: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg"><defs><clipPath id="x"><path d="M0 0H10V10Z"/></clipPath></defs></svg>#x');
    }
    ```

* Parse and print CSS `@scope` rules ([#4322](https://github.com/evanw/esbuild/issues/4322))

    This release includes dedicated support for parsing `@scope` rules in CSS. These rules include optional "start" and "end" selector lists. One important consequence of this is that the local/global status of names in selector lists is now respected, which improves the correctness of esbuild's support for [CSS modules](https://esbuild.github.io/content-types/#local-css). Minification of selectors inside `@scope` rules has also improved slightly.

    Here's an example:

    ```css
    /* Original code */
    @scope (:global(.foo)) to (:local(.bar)) {
      .bar {
        color: red;
      }
    }

    /* Old output (with --loader=local-css --minify) */
    @scope (:global(.foo)) to (:local(.bar)){.o{color:red}}

    /* New output (with --loader=local-css --minify) */
    @scope(.foo)to (.o){.o{color:red}}
    ```

* Fix a minification bug with lowering of `for await` ([#4378](https://github.com/evanw/esbuild/pull/4378), [#4385](https://github.com/evanw/esbuild/pull/4385))

    This release fixes a bug where the minifier would incorrectly strip the variable in the automatically-generated `catch` clause of lowered `for await` loops. The code that generated the loop previously failed to mark the internal variable references as used.

* Update the Go compiler from v1.25.5 to v1.25.7 ([#4383](https://github.com/evanw/esbuild/issues/4383), [#4388](https://github.com/evanw/esbuild/pull/4388))

    This PR was contributed by [@MikeWillCook](https://github.com/MikeWillCook).

## 2025

All esbuild versions published in the year 2025 (versions 0.25.0 through 0.27.2) can be found in [CHANGELOG-2025.md](./CHANGELOG-2025.md).

## 2024

All esbuild versions published in the year 2024 (versions 0.19.12 through 0.24.2) can be found in [CHANGELOG-2024.md](./CHANGELOG-2024.md).

## 2023

All esbuild versions published in the year 2023 (versions 0.16.13 through 0.19.11) can be found in [CHANGELOG-2023.md](./CHANGELOG-2023.md).

## 2022

All esbuild versions published in the year 2022 (versions 0.14.11 through 0.16.12) can be found in [CHANGELOG-2022.md](./CHANGELOG-2022.md).

## 2021

All esbuild versions published in the year 2021 (versions 0.8.29 through 0.14.10) can be found in [CHANGELOG-2021.md](./CHANGELOG-2021.md).

## 2020

All esbuild versions published in the year 2020 (versions 0.3.0 through 0.8.28) can be found in [CHANGELOG-2020.md](./CHANGELOG-2020.md).

```

### File: dl.sh
```sh
#!/bin/sh
set -eu
dir=$(mktemp -d)
platform=$(uname -ms)
tgz="$dir/esbuild-$ESBUILD_VERSION.tgz"

# Download the binary executable for the current platform
case $platform in
  'Darwin arm64') curl -fo "$tgz" "https://registry.npmjs.org/@esbuild/darwin-arm64/-/darwin-arm64-$ESBUILD_VERSION.tgz";;
  'Darwin x86_64') curl -fo "$tgz" "https://registry.npmjs.org/@esbuild/darwin-x64/-/darwin-x64-$ESBUILD_VERSION.tgz";;
  'Linux arm64' | 'Linux aarch64') curl -fo "$tgz" "https://registry.npmjs.org/@esbuild/linux-arm64/-/linux-arm64-$ESBUILD_VERSION.tgz";;
  'Linux x86_64') curl -fo "$tgz" "https://registry.npmjs.org/@esbuild/linux-x64/-/linux-x64-$ESBUILD_VERSION.tgz";;
  'NetBSD amd64') curl -fo "$tgz" "https://registry.npmjs.org/@esbuild/netbsd-x64/-/netbsd-x64-$ESBUILD_VERSION.tgz";;
  'OpenBSD arm64') curl -fo "$tgz" "https://registry.npmjs.org/@esbuild/openbsd-arm64/-/openbsd-arm64-$ESBUILD_VERSION.tgz";;
  'OpenBSD amd64') curl -fo "$tgz" "https://registry.npmjs.org/@esbuild/openbsd-x64/-/openbsd-x64-$ESBUILD_VERSION.tgz";;
  *) echo "error: Unsupported platform: $platform"; exit 1
esac

# Extract the binary executable to the current directory
tar -xzf "$tgz" -C "$dir" package/bin/esbuild
mv "$dir/package/bin/esbuild" .
rm "$tgz"

```

### File: LICENSE.md
```md
MIT License

Copyright (c) 2020 Evan Wallace

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

### File: RUNBOOK.md
```md
# Runbook

This documents some maintenance tasks for esbuild so I don't forget how they
work. There are a lot of moving parts now that esbuild uses trusted publishing.

## Publishing a release

Publishing a release is now done by using GitHub Actions as a
[trusted publisher](https://docs.npmjs.com/trusted-publishers).
To publish a new release:

1. Update the version in [`version.txt`](./version.txt). Only include the number. Do not include a leading `v`.
2. Copy that version verbatim (without the leading `v`) to a `##` header in [`CHANGELOG.md`](./CHANGELOG.md). This usually replaces the `## Unreleased` header used for unreleased changes.
3. Run `make platform-all` to update the version number in all `package.json` files. The publishing workflow will fail without this step.
4. Commit and push using a message such as `publish 0.X.Y to npm`. This should trigger the publishing workflow described below.

Pushing a change to [`version.txt`](./version.txt) causes the following:

- The [`publish.yml`](./.github/workflows/publish.yml) workflow in this repo
  will be triggered, which will:

    1. Build and publish all npm packages to npm using trusted publishing
    2. Create a tag for the release that looks like `v0.X.Y`
    3. Publish a [GitHub Release](https://github.com/evanw/esbuild/releases) containing the release notes in [`CHANGELOG.md`](./CHANGELOG.md)

- The [`release.yml`](https://github.com/esbuild/deno-esbuild/blob/main/.github/workflows/release.yml)
  workflow in the https://github.com/esbuild/deno-esbuild repo runs
  occasionally. On the next run, it will notice the version change and:

    1. Clone this repo
    2. Run `make platform-deno`
    3. Commit and push the new contents of the `deno` folder to the `deno-esbuild` repo
    4. Create a tag for the release that looks like `v0.X.Y`
    5. Post an event to the https://api.deno.land/webhook/gh/esbuild webhook
    6. Deno will then add a new version to https://deno.land/x/esbuild

    You can also manually trigger this workflow if you want it to happen immediately.

- The [`release.yml`](https://github.com/esbuild/esbuild.github.io/blob/main/.github/workflows/release.yml)
  workflow in the https://github.com/esbuild/esbuild.github.io repo runs
  occasionally. On the next run, it will notice the version change and:

    1. Create a new `dl/v0.X.Y` script for the new version number
    2. Update the `dl/latest` script with the new version number
    3. Commit and push these new scripts to the `gh-pages` branch of the `esbuild.github.io` repo
    4. GitHub Pages will then deploy these updates to https://esbuild.github.io/

    You can also manually trigger this workflow if you want it to happen immediately.

## Adding a new package

Each platform (operating system + architecture) needs a separate optional npm
package due to how esbuild's installer works. New packages should be created
under the `@esbuild/` scope so it's obvious that they are official.

Create a directory for the new package inside the [`npm/@esbuild`](./npm/@esbuild/)
directory. Then modify the rest of the repo to reference the new package. The
specifics for what to modify depends on the platform, but a good place to
start is to search for the name of a similar existing package and see where
it's used.

In addition, you'll need to prepare that package for the next release. To do
that:

1. Create an empty package with the expected name and a version of 0.0.1
2. Publish it with `npm publish --access public` (note that scoped packages are private by default)
3. Log in to the npm website and go to the package settings
4. Ensure that the only maintainer is the [esbuild](https://www.npmjs.com/~esbuild) user
5. Add the GitHub repo as the trusted publisher:
    - **Organization or user:** `evanw`
    - **Repository:** `esbuild`
    - **Workflow filename:** `publish.yml`
6. Ensure publishing access is set to **Require two-factor authentication and disallow tokens (recommended)**

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

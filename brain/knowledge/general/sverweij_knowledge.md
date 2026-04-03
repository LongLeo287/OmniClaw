---
id: sverweij-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:19.408976
---

# KNOWLEDGE EXTRACT: sverweij
> **Extracted on:** 2026-03-30 17:54:12
> **Source:** sverweij

---

## File: `dependency-cruiser.md`
```markdown
# 📦 sverweij/dependency-cruiser [🔖 PENDING/APPROVE]
🔗 https://github.com/sverweij/dependency-cruiser
🌐 https://npmjs.com/dependency-cruiser

## Meta
- **Stars:** ⭐ 6496 | **Forks:** 🍴 278
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Validate and visualize dependencies. Your rules. JavaScript, TypeScript, CoffeeScript. ES6, CommonJS, AMD.

## README (trích đầu)
```
# Dependency cruiser ![Dependency cruiser](https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/doc/assets/ZKH-Dependency-recolored-160.png)

_Validate and visualise dependencies. With your rules._ JavaScript. TypeScript. CoffeeScript. ES6, CommonJS, AMD.

## What's this do?

![Snazzy dot output to whet your appetite](https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/doc/assets/sample-dot-output.png)

This runs through the dependencies in any JavaScript, TypeScript, LiveScript or CoffeeScript project and ...

- ... **validates** them against (your own) [rules](./doc/rules-reference.md)
- ... **reports** violated rules
  - in text (for your builds)
  - in graphics (for your eyeballs)

As a side effect it can generate dependency graphs in various output formats including [**cool visualizations**](./doc/real-world-samples.md)
you can stick on the wall to impress your grandma.

## How do I use it?

### Install it ...

```shell
npm install --save-dev dependency-cruiser
# or
yarn add -D dependency-cruiser
pnpm add -D dependency-cruiser
```

### ... and generate a config

```shell
npx depcruise --init
```

This will look around in your environment a bit, ask you some questions and create
a `.dependency-cruiser.js` configuration file attuned to your project[^1][^2].

[^1]:
    We're using `npx` in the example scripts for convenience. When you use the
    commands in a script in `package.json` it's not necessary to prefix them with
    `npx`.

[^2]:
    If you don't want to use `npx`, but instead `pnpx` (from the `pnpm`
    package manager) or `yarn` - please refer to that tool's documentation.
    Particularly `pnpx` has semantics that differ from `npx` quite significantly
    and that you want to be aware of before using it. In the mean time: `npx`
    _should_ work even when you installed the dependency with a package manager
    different from `npm`.

### Show stuff to your grandma

To create a graph of the dependencies in your src folder, you'd run dependency
cruiser with output type `dot` and run _GraphViz dot_[^3] on the result. In
a one liner:

```shell
npx depcruise src --include-only "^src" --output-type dot | dot -T svg > dependency-graph.svg
```

> <details>
> <summary>dependency-cruiser v12 and older: add --config option</summary>
>
> While not necessary from dependency-cruiser v13 and later, in v12 and older
> you'll have to pass the --config option to make it find the .dependency-cruiser.js
> configuration file:
>
> ```shell
> npx depcruise src --include-only "^src" --config --output-type dot | dot -T svg > dependency-graph.svg
> ```

</details>

- You can read more about what you can do with `--include-only` and other command line
  options in the [command line interface](./doc/cli.md) documentation.
- _[Real world samples](./doc/real-world-samples.md)_
  contains dependency cruises of some of the most used projects on npm.
- If your grandma is more into formats like `mermaid`, `json`, `csv`, `html` or plain 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


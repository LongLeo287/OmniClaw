---
id: github.com-k-kolomeitsev-data-structure-protocol-6
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:17.139740
---

# KNOWLEDGE EXTRACT: github.com_k-kolomeitsev_data-structure-protocol_6013fe65
> **Extracted on:** 2026-04-01 13:04:20
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007522238/github.com_k-kolomeitsev_data-structure-protocol_6013fe65

---

## File: `ARCHITECTURE.md`
```markdown
## DSP (Data Structure Protocol) — architecture

---

### Agent Prompt (paste into system/user prompt)

> **This project uses DSP (Data Structure Protocol).**
> The `.dsp/` directory is the project entity graph: modules, functions, dependencies, public API. This is your long-term memory of the code structure.
>
> **Working rules:**
>
> 1. **Before changing code** — find the affected entities via `dsp-cli search`, `find-by-source`, or `read-toc`. Read their `description` and `imports` to understand the context.
> 2. **When creating a file/module** — immediately call `dsp-cli create-object`. For each exported function — `create-function` (with `--owner`). Register exports via `create-shared`.
> 3. **When adding an import** — call `dsp-cli add-import` with a short `why`. For external dependencies — first `create-object --kind external` if the entity does not exist yet.
> 4. **When removing an import / export / file** — call `remove-import`, `remove-shared`, `remove-entity` respectively. Cascading cleanup is performed automatically.
> 5. **When renaming/moving a file** — call `move-entity`. The UID does not change.
> 6. **Don’t touch DSP** if only internal implementation changed, without changing purpose and dependencies.
> 7. **Bootstrap** — if `.dsp/` is empty, traverse the project from the root entrypoint downwards (DFS over imports), documenting every file.
>
> **Key commands:**
> ```
> dsp-cli init
> dsp-cli create-object <source> <purpose> [--kind external] [--toc ROOT_UID]
> dsp-cli create-function <source> <purpose> [--owner UID] [--toc ROOT_UID]
> dsp-cli create-shared <exporter_uid> <shared_uid> [<shared_uid> ...]
> dsp-cli add-import <importer_uid> <imported_uid> <why> [--exporter UID]
> dsp-cli remove-import <importer_uid> <imported_uid> [--exporter UID]
> dsp-cli remove-shared <exporter_uid> <shared_uid>
> dsp-cli remove-entity <uid>
> dsp-cli move-entity <uid> <new_source>
> dsp-cli update-description <uid> [--source S] [--purpose P] [--kind K]
> dsp-cli get-entity <uid>
> dsp-cli get-children <uid> [--depth N]
> dsp-cli get-parents <uid> [--depth N]
> dsp-cli search <query>
> dsp-cli find-by-source <path>
> dsp-cli read-toc [--toc ROOT_UID]
> dsp-cli get-stats
> ```

---

### 1) Goal and scope

**The goal of DSP** is to store _minimal, but sufficient_ context about a repository/artifact system as a graph “entities → dependencies/public API”, so that an LLM can:

- quickly find the required fragments by UID,
- understand _why_ entities exist and _how_ they are connected,
- avoid having to load the entire source tree into the context window.

**DSP is long-term memory and an index of the project for an LLM.** At any time, an agent can run project-wide search (grep), find the required entities by descriptions/keywords, and from a found UID expand the whole relationship graph: incoming dependencies, outgoing imports, and recipients via `exports`. This replaces the need to “remember” the project structure or load it in full — the whole project map is always available through `.dsp`.

**DSP is not documentation for humans and not an AST dump.** DSP records:

- the _meaning_ of entities (purpose),
- _boundaries_ (what it imports / what it shares outward),
- _reasons for relationships_ (why something is imported), in a volume sufficient for code generation and refactoring.

**DSP works with any data and codebases** (Node.js, Python, Go, frontend, backend, infrastructure, etc.).

### 2) Model principles

- **Code = graph.** Graph nodes are _objects_ and _functions_. Edges are `imports`, `shared/exports`.
- **Identity by UID, not by file.** A file path is an attribute, not an identifier. Renames/moves must not change the UID.
- **“Shared” creates an entity.** If part of an object becomes available externally (export/public), it must have its own UID (and its own directory in `.dsp`).
- **Import tracks both “from where” and “what”.** For one actual import in code, two links may be recorded:
  - to the **Object module/provider** (where we import from),
  - to the **specific shared entity** (what exactly we use).
- **Import completeness (coverage).** **Any file/artifact that is imported/connected somewhere must be represented in `.dsp` as an Object with UID and `source:`.** This includes not only code, but also assets/resources: images (`.png/.svg/.webp`), styles (`.css/.scss`), data (`.json`), wasm, sql, templates, etc.
- **`why` is always written next to the imported entity.** The feedback is stored in `exports` of the imported entity (see §4.3 and `addImport`).
- **Start from roots.** Each root is a separate entrypoint with its own TOC file. By default, roots are auto-detected via the LLM; if needed, they are specified manually. Imports are traversed depth-first from each root.
- **External dependencies are recorded only.** If an entity imports an external library/tool (npm packages, stdlib, SDK, etc.), DSP records the _fact of the import_ and a brief purpose, but **does not dive inside** the dependency (in Node.js do not go into `node_modules`; in Python — into `site-packages`; in Go — into `vendor`/module cache; etc.). At the same time, external dependencies still have an **`exports index`** — you can see who imports them and why, so the relationship graph remains complete.

### 3) Terms

- **Entity**: a graph node. Two base kinds: `Object` and `Function`.
- **Object**: _any “thing” with a UID that is not a function_ (module/ES module, class, namespace, config, resource file, external dependency, etc.). Variables are considered part of a global or local Object; when shared/exported they become separate entities with their own UID.
- **Function**: a function/method/handler/pipeline that performs work.
- **imports**: a list of UIDs of any entities outside the local scope that the current entity **uses** (imports of modules, libraries, objects, functions; dependencies via constructor/DI in classes). For an Object, this also includes its own methods/functions — so the object “sees” its composition.
- **shared**: a list of UIDs of entities available outside the local scope (exported functions, objects, variables; public fields/methods of classes).
- **exports index**: a reverse index “who imports this entity and why”. Maintained for any imported entity (Object, Function, external).


### 4) Storage: the `.dsp` directory

#### 4.1. Directory structure

At the repository root, a `.dsp/` directory is created. For each entity, a directory is created:

- `.dsp/<uid>/`

UID format (to avoid collisions and indicate type by prefix):

- `obj-<8 hex>` — for objects (example: `obj-a1b2c3d4`)
- `func-<8 hex>` — for functions (example: `func-7f3a9c12`)

Generation: first 8 characters of `uuid4().hex`. 4 billion possible UIDs is enough for any project.

For entities **inside a file** (to avoid binding to line numbers), the UID is anchored to code via a **comment marker** right before the declaration:

```js
// @dsp func-a1b2c3d4
export function calculateTotal(items) { ... }
```

```python
# @dsp obj-e5f6g7h8
class UserService:
```

The `@dsp <uid>` marker lets you quickly find an entity in code via grep, is independent of lines/formatting, and does not require renaming symbols.

> Important: the UID must be _stable_ for “the same” entity across moves/renames (path/file may change, UID must not).

#### 4.2. Entity files

Each entity directory contains:

- `description` — purpose + link to the source code (path/symbol).
- `imports` — list of imports/references to entities (one entry per line).
- `shared` — list of UIDs of entities available outside the local scope (exports, public fields/methods).
- `exports/` — _(created as needed)_ reverse index: who imports this entity and/or its shared parts, and why. Works for any kind (Object, Function, external).

##### 4.2.1. `description` format

The `description` file is a **short, human- and LLM-readable** block. Minimal recommended template:

```text
source: <repo-relative-path>[#<symbol>]
kind: object|function|external
purpose: <1-3 sentences: what it is and why>
```

After that (optional), freeform text/markdown sections may follow (no rigid schema), e.g. `notes:` / `contracts:`.

**Rule for the root file (root entrypoint):** its `description` must include a **brief project overview** (what the system is, its main pipeline/workflow, and what is public API/boundaries) — as short as possible so it becomes the first “project context” for the LLM.

##### 4.2.2. `imports` format

Minimal format (one line — one dependency):

```text
<imported_uid>
```

Allowed extension (if you need to encode “via which exporter” or other metadata):

```text
<imported_uid> via=<exporter_obj_uid>
```

##### 4.2.3. `shared` format

One line — one shared entity UID:

```text
<shared_uid>
```

#### 4.3. Export index (reverse index)

The `exports/` directory is created for **any** imported entity (Object, Function, external) and shows who uses it and why.

**For an entity without shared** (Function, external, or an Object imported as a whole):

- `.dsp/<uid>/exports/<importer_uid>` — a file with text “why it is imported” (1–3 sentences).

**For an Object with shared entities**, add the following:

- `.dsp/<uid>/exports/<shared_uid>/description` — what is exported (briefly).
- `.dsp/<uid>/exports/<shared_uid>/<importer_uid>` — “why this shared is imported” (1–3 sentences).

This gives the LLM answers to three questions:

- **who imports the entity and why** (via `exports/<importer_uid>`),
- **what can be imported from the object** (via `shared`),
- **why a specific shared is imported** (via `exports/<shared_uid>/<importer_uid>`).

> If the same shared UID is re-exported from multiple objects (barrel exports), export indices are kept _separately in each exporter_.

#### 4.4. Table of contents (TOC) files — mandatory

For each root entrypoint, **its own TOC file** is created under `.dsp/`. One root — one TOC.

**Naming:** `.dsp/TOC` for a single root, `.dsp/TOC-<rootUid>` if there are multiple roots.

**Format:**

```text
<uid_root>
<uid_2>
<uid_3>
...
<uid_N>
```

**Rules:**

- **TOC[0] is always the root** of this entrypoint. This is how the LLM gets a starting point.
- Next — all entities reachable from that root, in documentation order (traversal order during bootstrap).
- Each UID appears in a given TOC **exactly once**.
- The same entity **may** be in multiple TOCs (if reachable from multiple roots).
- When documenting new entities — append them to the end of the corresponding TOC.

**Purpose:**

- A complete overview of all entities reachable from a given root.
- Lets the LLM start navigation from the right entrypoint and dive into its structure.
- In multi-root projects (monorepo, multiple applications), each TOC is an independent map of its subtree.

### 5) Operations (tooling-level API)

Below are the operations used by the `.dsp` generator.

#### 5.0. `init`

Initialize the `.dsp/` directory at the project root. Required first step before any operations. Idempotent — repeated calls are safe.

CLI: `dsp-cli init`

#### 5.1. `createObject(sourceRef, purpose, kind?) -> objUid`

Parameters:

- `sourceRef` — path to source (+ symbol if applicable),
- `purpose` — purpose,
- `kind` — `object` (default) or `external` (for external dependencies).

Actions:

- generate/resolve `objUid` (stably),
- create `.dsp/<objUid>/`,
- write `.dsp/<objUid>/description` (source, kind, purpose),
- create `.dsp/<objUid>/imports` if missing (empty),
- if needed — `.dsp/<objUid>/shared` (empty),
- **append `objUid` to `.dsp/TOC`**.

#### 5.2. `createFunction(sourceRef, purpose, ownerUid?) -> funcUid`

Actions:

- generate/resolve `funcUid` (stably),
- create `.dsp/<funcUid>/`,
- write `.dsp/<funcUid>/description`,
- create `.dsp/<funcUid>/imports` (empty),
- if `ownerUid` is provided:
  - append `funcUid` to the owner object’s `imports` (so the object “sees” its methods),
  - create a reverse record `.dsp/<funcUid>/exports/<ownerUid>` (so `getParents` can find the owner without a full scan),
- **append `funcUid` to `.dsp/TOC`**.

> Function ownership is determined through the owner’s `imports`. Reverse lookup — through `getParents(funcUid)`. A standalone function (without an owner) is simply added to a module’s `shared` if it is exported.

#### 5.3. `createShared(exporterUid, sharedUids[])`

Actions:

- append `sharedUids` to `.dsp/<exporterUid>/shared`,
- ensure `.dsp/<exporterUid>/exports/` exists,
- for each `sharedUid`, ensure `.dsp/<exporterUid>/exports/<sharedUid>/description` exists — if the file is created for the first time, `description` is auto-filled from the `purpose` of the shared entity (if it already exists in `.dsp`).

#### 5.4. `addImport(importerUid, importedUid, exporterUid?, why)`

Actions:

- append `importedUid` (and optionally `via=exporterUid`) to `.dsp/<importerUid>/imports`,
- write the reverse feedback “why we import” **into `exports` of the imported entity**:
  - if importing a **shared entity** and `exporterUid` is known:
    - create/update `.dsp/<exporterUid>/exports/<importedUid>/<importerUid>` with text `why`,
  - otherwise (importing the **Object as a whole** — local module, external package/submodule, side-effect import, etc.):
    - ensure `.dsp/<importedUid>/exports/` exists,
    - create/update `.dsp/<importedUid>/exports/<importerUid>` with text `why`.

**When one `addImport` call is enough vs when you need two:**

You need two calls when importing **both the whole module (or as a namespace) and a specific symbol from it**. One call is enough when only one of those happens.

```js
// Example 1: namespace import + named import from the same module
import * as utils from './utils';     // → addImport(thisUid, utilsObjUid, why="formatting utilities")
import { calc } from './utils';       // → addImport(thisUid, calcUid, utilsObjUid, why="total calculation")
// Total: 2 addImport calls

// Example 2: named import only
import { UserService } from './services';
// → addImport(thisUid, userServiceUid, servicesObjUid, why="user management")
// Total: 1 call (to the shared entity, exporter provided via exporterUid)

// Example 3: side-effect import (no specific symbol)
import './polyfills';
// → addImport(thisUid, polyfillsObjUid, why="browser polyfills")
// Total: 1 call (to the whole Object)

// Example 4: default import
import express from 'express';
// → addImport(thisUid, expressObjUid, why="HTTP framework")
// Total: 1 call (to the whole Object, external)
```

---

#### Update operations

#### 5.5. `updateDescription(uid, fields)`

Update the description of an existing entity. Typical scenarios: the purpose of a module changed, the file path changed (rename/move), or the description was refined after refactoring.

Actions:

- read `.dsp/<uid>/description`,
- update specified fields (`source:`, `purpose:`, `kind:`, freeform sections),
- write back `.dsp/<uid>/description`.

#### 5.6. `updateImportWhy(importerUid, importedUid, exporterUid?, newWhy)`

Update the reason for an import (the `why` text). Typical scenario: a module still imports a dependency, but uses it for a different purpose.

Actions:

- locate the feedback file in `exports`:
  - if `exporterUid` is provided: `.dsp/<exporterUid>/exports/<importedUid>/<importerUid>`,
  - otherwise: `.dsp/<importedUid>/exports/<importerUid>`,
- overwrite the file contents with `newWhy`.

#### 5.7. `moveEntity(uid, newSourceRef)`

The entity moved (file rename/move). UID stays the same; only the source reference changes.

Actions:

- update `source:` in `.dsp/<uid>/description` to `newSourceRef`.

> This is a special case of `updateDescription`, separated for clarity: the UID **does not change** on moves.

---

#### Delete operations

#### 5.8. `removeImport(importerUid, importedUid, exporterUid?)`

Remove an import relationship. Typical scenario: an `import` was removed from code.

Actions:

- remove `importedUid` from `.dsp/<importerUid>/imports`,
- delete the feedback file from `exports`:
  - if `exporterUid` is provided: delete `.dsp/<exporterUid>/exports/<importedUid>/<importerUid>`,
  - otherwise: delete `.dsp/<importedUid>/exports/<importerUid>`.

#### 5.9. `removeShared(exporterUid, sharedUid)`

The entity is no longer exported. Typical scenario: `export` was removed from code.

Actions:

- remove `sharedUid` from `.dsp/<exporterUid>/shared`,
- delete the directory `.dsp/<exporterUid>/exports/<sharedUid>/` with all recipient files,
- for each recipient (former files under `exports/<sharedUid>/`) — remove `sharedUid` from their `imports`.

#### 5.10. `removeEntity(uid)`

Remove an entity from DSP completely. Typical scenario: a file/module was deleted from the project.

Actions:

1. **Full imports scan**: for each entity in `.dsp` — remove from `imports` all lines where `uid` appears as `imported` or as a `via=` target. This covers direct imports, shared-imports via `uid`, owner links — everything in one pass.
2. **Clean outgoing links**: read `.dsp/<uid>/imports` — for each imported entity, delete the feedback file from its `exports/`.
3. **Clean shared references in exporters**: for each entity — if `uid` appears in someone’s `shared`, remove `uid` from `.dsp/<exporterUid>/shared` and delete `.dsp/<exporterUid>/exports/<uid>/`.
4. Remove `uid` from **all** TOC files.
5. Delete the `.dsp/<uid>/` directory entirely.

---

#### Read operations (single entity)

#### 5.11. `getEntity(uid) -> EntityInfo`

Get a full snapshot of an entity. Basic operation — an entry point for any analysis of a specific module.

Returns:

- `description` (source, kind, purpose, notes),
- `imports[]` — list of dependency UIDs,
- `shared[]` — list of exported entity UIDs (for Objects),
- `exportedTo[]` — list of recipients from `exports/` (who imports it and why).

Implementation: read files from `.dsp/<uid>/`.

#### 5.12. `getShared(uid) -> SharedInfo[]`

Get the public API of an entity — what it makes available externally and who uses it. Typical scenario: an agent needs to understand what can be imported from a module/class/function.

Returns for each shared UID:

- description (from `.dsp/<uid>/exports/<sharedUid>/description`),
- list of recipients with reasons (files under `.dsp/<uid>/exports/<sharedUid>/`).

#### 5.13. `getRecipients(uid) -> RecipientInfo[]`

Get everyone who imports this entity, and why. Typical scenario: impact analysis — who will be affected by changes in this module.

Returns: a list of pairs `(recipientUid, why)`.

Implementation — a three-level search (each level complements the previous, with UID deduplication):

1. **Direct recipients**: files under `.dsp/<uid>/exports/` (direct imports via `addImport` without `exporter`).
2. **Via shared exporters**: if `uid` is present in someone’s `shared`, read files under `.dsp/<exporterUid>/exports/<uid>/` (imports via `addImport` with `exporter`).
3. **Imports fallback**: scan all entities — if `uid` is found in someone’s `imports` (e.g., owner relationship) but wasn’t discovered at previous levels.

---

#### Graph traversal operations

#### 5.14. `getChildren(uid, depth?) -> Tree`

Get the dependency tree **downwards** — what this entity imports (and what its dependencies import, etc.). Typical scenarios: understand what a module consists of, which libraries it pulls in.

Parameters:

- `uid` — starting point,
- `depth` — traversal depth (default `1` — direct imports only; `Infinity` — full tree).

Returns: a tree of nodes `{ uid, description.purpose, children[] }`.

Implementation: recursive reading of `imports` with a `visited` set to guard against cycles.

#### 5.15. `getParents(uid, depth?) -> Tree`

Get the dependency tree **upwards** — who imports this entity (and who imports those, etc.). Typical scenarios: understand blast radius, find all entry points that use this code.

Parameters:

- `uid` — starting point,
- `depth` — traversal depth (default `1` — direct recipients only; `Infinity` — up to the root(s)).

Returns: a tree of nodes `{ uid, description.purpose, why, parents[] }`.

Implementation: recursive reading of `exports/` with a `visited` set.

#### 5.16. `getPath(fromUid, toUid) -> uid[] | null`

Find the shortest path between two entities in the graph (in any direction along `imports` edges). Typical scenario: understand how two modules are connected to each other.

Returns: an ordered list of UIDs from `fromUid` to `toUid`, or `null` if no path exists.

Implementation: BFS over the `imports` graph (bidirectional — via `imports` and `exports`).

---

#### Search and discovery operations

#### 5.17. `search(query) -> SearchResult[]`

Full-text search across `.dsp`. Typical scenarios: find a module by a keyword (“authentication”, “routing”, “cache”), find entities related to a specific file.

Searches for matches in:

- `description` (purpose, source, notes),
- file names under `exports/` (recipient UIDs).

Returns: a list `{ uid, matchContext }` — the UID and the fragment where the match was found.

Implementation: `grep -r "query" .dsp/` over `description` files.

#### 5.18. `findBySource(sourcePath) -> uid[]`

Find entities by a source file path. Typical scenario: an agent sees a file in code and wants its DSP representation.

Returns a **list** of UIDs, because one file may contain multiple entities (the module Object + shared functions/classes inside). Matching: exact by `source:` or by the `sourcePath#` prefix (for entities inside a file).

Implementation: search for `source:` across all `.dsp/*/description`.

#### 5.19. `readTOC() -> uid[]`

Read the project table of contents. Entry point for getting familiar with the project: TOC[0] is the root, then all other entities in documentation order.

Implementation: read `.dsp/TOC`.

---

#### Diagnostics operations

#### 5.20. `detectCycles() -> uid[][]`

Detect cyclic dependencies in the `imports` graph. Typical scenario: project audit, finding architectural issues.

Returns: a list of cycles; each cycle is an array of UIDs forming a closed path.

#### 5.21. `getOrphans() -> uid[]`

Find “orphan” entities — those that nobody uses except the root. Typical scenario: find dead code and unused modules.

An entity is **not** considered an orphan if at least one of the following holds:

- it is a root (the first UID in any TOC),
- it appears in `imports` of any other entity (as `imported` or as a `via=` target),
- its `exports/` is non-empty (there is at least one recipient).

Implementation: collect the set of all UIDs appearing in imports (including `via=` targets), then for the remaining ones check `exports/`.

#### 5.22. `getStats() -> ProjectStats`

Overall statistics for the DSP graph. Typical scenario: quick orientation in the scale of the project.

Returns:

- total number of entities (Object / Function / External),
- number of edges (imports),
- number of shared entities,
- number of cycles (if any),
- number of orphans.

### 6) Bootstrap (initial mapping)

#### Algorithm (depth-first traversal)

Bootstrap is a simple DFS traversal of dependencies starting from a root file. **For each root entrypoint**, bootstrap is executed separately with its own TOC file.

**Step 1. Identify root entrypoint(s):**

- by default — auto-detect via the LLM (package.json `main`, framework entrypoint, etc.),
- or specify manually,
- if there are multiple roots — run bootstrap for each, creating a separate TOC (`TOC-<rootUid>`).

**Step 2. Fully document the root file:**

- `createObject` for the module (UID is written to TOC **first**),
- extract functions → `createFunction` for each (with ownerUid pointing to this Object),
- extract `shared` (exports/public API) → `createShared`,
- extract all `imports` → `addImport`,
- external dependencies from imports → `createObject(..., kind: external)` (append to TOC, but do not descend).

**Step 3. Take the first import from the current file that is NOT an external dependency** (not a library, not node_modules, not stdlib):

- document it fully (same as Step 2),
- append its UID to TOC.

**Step 4. Recursive descent:**

- from the just-documented file, take the first non-library import,
- if it exists — document it and repeat Step 4,
- if **none exist** — **go up one level** and take the next unprocessed non-library import.

**Step 5.** Repeat until all reachable non-library files are documented.

**Visually:**

```
root (document)
 ├─ import_A (non-library → document)
 │   ├─ import_A1 (non-library → document)
 │   │   └─ ... (descend deeper)
 │   ├─ import_A2 (external → record kind: external, DO NOT descend)
 │   └─ import_A3 (non-library → document)
 │       └─ ... no non-library imports → backtrack
 ├─ import_B (non-library → document)
 │   └─ ...
 └─ import_C (external → record kind: external, DO NOT descend)
```

**Key rules:**

- Traversal uses a `visited` set by UID/sourceRef — **no infinite recursion**.
- External dependencies are recorded as Objects with `kind: external`, but their internal structure **is not analyzed**.
- After traversal completes, `.dsp/TOC` contains a complete ordered list of all project entities.

### 7) UID: stability and “versioning”

#### 7.1. Invariants

- UID must not depend on the file path.
- UID must survive:
  - rename/move,
  - code rearrangement,
  - formatting,
  - small implementation changes.

#### 7.2. UID change policy

A new UID is created only if an entity **changes its purpose** (semantic identity), for example:

- a module/class/function started solving a _different_ problem,
- the entity was “reborn” (the old one was replaced with different logic while keeping the name).

In all other cases, update descriptions/links and keep the UID.

#### 7.3. UID for entities inside a file (comment marker)

Separate identity between “file as an Object” and “entities inside a file”:

- **File as an Object**: `uid = obj-<uuid>`, `source: <filePath>`.
- **Entities inside a file** (shared functions, shared objects, exported classes): their own `uid = obj-<uuid>` or `func-<uuid>`, anchored to code via a **comment marker** `@dsp <uid>` before the declaration.

Example (TypeScript):

```ts
// @dsp func-7f3a9c12
export function calculateTotal(items: Item[]): number { ... }

// @dsp obj-b4e82d01
export class OrderService { ... }
```

Example (Python):

```python
# @dsp func-3c19ab8e
def process_payment(order):
    ...
```

**Why a comment, not a line-number binding:**

- you can **instantly find the UID in code** via `grep "@dsp func-7f3a9c12"`,
- it does not depend on line numbers, formatting, code rearrangement,
- it does not require renaming symbols — names stay clean,
- it works for any language (every language has comments).

`sourceRef` in `description` is stored as `source: <filePath>#<uid>`.

> The source of truth is `.dsp`: after a file rename/move it is enough to update `source:` in `description` without changing the UID.

### 8) Special cases

#### 8.1. Cyclic dependencies

- the tool must be able to detect cycles in the `imports` graph,
- traversal must be resilient to cycles,
- cycles are diagnostic information (not fatal), but must be recorded.

#### 8.2. Re-export (barrel exports)

- one shared UID may be available from multiple exporters,
- the `exports index` is maintained **per exporter**, because the LLM must understand “where it is usually imported from”.

#### 8.3. Code generation by an agent

When an agent (LLM) writes new code, it **simultaneously calls DSP operations** to register the created entities:

- created a new module → `createObject`,
- created a function → `createFunction`,
- added an export → `createShared`,
- added an import → `addImport`.

DSP is updated **during code generation**, not after the fact.

#### 8.4. Dynamic imports

- Dynamic dependencies (e.g., `import()` in JS, `importlib` in Python) are recorded as normal `imports` when discovered.
- If a dynamic import cannot be determined statically — it is added to DSP upon first execution/discovery.

#### 8.5. External dependencies (libraries, SDKs, stdlib)

DSP works with any data and codebases. At the same time, **DSP does not dive into external dependencies** — it only records the fact of import:

- An external import is represented as an `Object` with `kind: external` in `description`.
- `description` records: package/module/version and purpose (why it is imported).
- **The internal structure of the library is not analyzed.** For example: in Node.js — do not go into `node_modules`; in Python — do not go into `site-packages`; in Go — do not go into `vendor`/module cache; etc.
- The `exports index` **is maintained** — you can see who imports this library and why. This allows you to immediately get the list of all recipients when updating/replacing a dependency.

This keeps the graph closed (all links point to existing UIDs) and fully navigable, without inflating `.dsp` with descriptions of third-party internals.

### 9) LLM integration: contract and navigation

Two logical components work with DSP:

- **DSP Builder** — a tool (script/agent) that builds and updates `.dsp`. It calls operations from §5 and maintains graph integrity.
- **LLM Orchestrator** — an agent (LLM) that uses `.dsp` as project memory. It reads TOC, searches entities, expands the relationship graph, and builds context for code generation.

**DSP Builder** is responsible for:

- building `.dsp` (bootstrap and ongoing updates),
- graph integrity,
- minimal, precise descriptions of entities and dependency reasons.

**LLM Orchestrator** is responsible for:

- selecting relevant UIDs for a task,
- building “context bundles”:
  - `description` of the target entities,
  - their `imports` (+ transitive dependencies if needed),
  - `shared` and the `exports index` to understand API and usage patterns,
- passing strictly limited sections into the model — without overloading the context.

#### 9.1) Navigation and search in `.dsp`

An agent can find required modules and entities in several ways:

**Via TOC:**

- Read `.dsp/TOC` → get the full UID list → read `description` of the required entities.

**Via grep/search over files, including the `.dsp` directory:**

- Search `description` files — find entities by keywords, purpose, source path.
- Search `imports` — find dependencies of a specific entity.
- Search `exports/` — find all recipients (who uses a given entity and why).

### 10) Granularity and minimal-context policy

- **Completeness at the file level, not at the code-within-file level.** “Import completeness” (§2) means every **file/module** that is imported in the project must have an Object in `.dsp`. This is about files and modules — not about every variable inside a file. Within one file, a separate UID is assigned only to an entity that is **shared outward** (`shared`) or **used from multiple places**. Local variables, internal helpers, private fields — remain part of the parent Object, without their own UID. If granularity keeps growing, something is wrong.

- **Update recipients via `exports`.** To update a library/module/symbol, it is enough to open `exports` of the imported entity and get the list of importers (recipients) by UID, then update them precisely.

- **Change tracking.** `git diff` shows what changed — a new file was created, a function or an object changed. Changed files are fed to the LLM to update DSP. Changes inside functions often do not require DSP updates, because the description captures *purpose*, not implementation details — unless imports were added/removed.

```

## File: `GETTING_STARTED.md`
```markdown
# Getting Started with DSP

**DSP (Data Structure Protocol)** is graph-based long-term structural memory for AI coding agents. The graph lives under **`.dsp/`** in your repository. The CLI is **`skills/data-structure-protocol/scripts/dsp-cli.py`** (run it from the repo root, or pass a full path to `python`).

This guide takes about **3–5 minutes**. You will install the skill, initialize `.dsp/`, learn how to bootstrap or grow the graph, and use the commands you will rely on every day.

---

## 0. The fastest way: dsp-boilerplate

If you're starting a **new project**, skip manual setup entirely. [**dsp-boilerplate**](https://github.com/k-kolomeitsev/dsp-boilerplate) is a production-ready fullstack starter (NestJS 11 + React 19 + Vite 7 + Docker Compose) with everything pre-configured:

- `.dsp/` graph fully initialized with two roots (backend + frontend)
- `@dsp` UID markers in all source files
- DSP skill installed for Cursor, Claude Code, and Codex
- Cursor rules, Claude Code hooks, AGENTS.md
- Git hooks for DSP consistency
- GitHub Actions CI

```bash
git clone https://github.com/k-kolomeitsev/dsp-boilerplate.git my-project
cd my-project
docker-compose up -d
```

The agent has full structural memory from the first session. You can start building immediately.

If you want to add DSP to an **existing project** or set it up manually, continue below.

---

## 1. Install the DSP Skill

**macOS / Linux (default install):**

```bash
curl -fsSL https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.sh | bash
```

**Windows (PowerShell):**

```powershell
irm https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.ps1 | iex
```

**Specific agent (example: Cursor):**

```bash
curl -fsSL https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.sh | bash -s -- cursor
```

**Codex skill-installer:**

```bash
$skill-installer install https://github.com/k-kolomeitsev/data-structure-protocol/tree/main/skills/data-structure-protocol
```

---

## 2. Initialize DSP

From your **project root** (where you want `.dsp/`):

```bash
python dsp-cli.py --root . init
```

If the CLI is not on `PATH`, use the path to the script, for example:

```bash
python skills/data-structure-protocol/scripts/dsp-cli.py --root . init
```

**What this does:** creates a **`.dsp/`** directory and an **empty graph** ready for entities and import edges. You commit `.dsp/` with your code so the structure is versioned and shareable.

---

## 3. Bootstrap an Existing Project (Brownfield)

For a codebase that already exists, treat bootstrapping as a **depth-first walk** over the import graph:

1. **Identify root entrypoints** — e.g. `src/main.ts`, `src/app.module.ts`, or your framework’s real roots.
2. **Create a root entity** for each entry file:

   ```bash
   python dsp-cli.py --root . create-object "src/main.ts" "Application entrypoint"
   ```

3. **Walk imports depth-first**: for each file you reach, **create an object** (or function) entity so every important node exists in the graph.
4. **Record each import** with a short reason:

   ```bash
   python dsp-cli.py --root . add-import obj-<from-uid> obj-<to-uid> "HTTP routing and request handling"
   ```

5. **Mark public APIs** where one module exports symbols others rely on:

   ```bash
   python dsp-cli.py --root . create-shared obj-<owner-uid> obj-<shared-uid>
   ```

6. **External dependencies** (npm packages, stdlib, generated vendor code): model them as **`kind: external`** and **do not** try to map their full internals:

   ```bash
   python dsp-cli.py --root . create-object "node_modules/some-pkg/index.js" "HTTP client library" --kind external
   ```

**Trade-off (honest):** bootstrapping a large repo is **upfront work**. The payoff is **lower token usage** (agents find structure without re-reading everything), **faster discovery** of relevant files, and **safer refactors** because dependency direction and public surface are explicit.

**Greenfield projects:** you do not need a big-bang bootstrap. **Register entities as you create files and imports**; the graph stays cheap to maintain.

---

## 4. Navigate the Graph

| Goal | Example |
|------|---------|
| Find by keyword in descriptions / metadata | `python dsp-cli.py --root . search "authentication"` |
| Find entity for a file | `python dsp-cli.py --root . find-by-source "src/auth/index.ts"` |
| Inspect one entity | `python dsp-cli.py --root . get-entity obj-a1b2c3d4` |
| Downward dependency tree (what this imports) | `python dsp-cli.py --root . get-children obj-a1b2c3d4 --depth 2` |
| Table of contents from a root | `python dsp-cli.py --root . read-toc --toc obj-<root-uid>` |

Use **`find-by-source`** after you know a path; use **`search`** when you only have a concept or feature name.

---

## 5. Update DSP as You Code

Keep the graph aligned with the repo as you change code:

| Change | DSP action |
|--------|------------|
| **New file** | `create-object` (or `create-function`) and **`add-import`** for each new edge |
| **New public function / exported API** | `create-function`, then **`create-shared`** from the owning module, and add an **`@dsp`** marker in source if your workflow uses it |
| **New import** | `add-import <importer-uid> <imported-uid> "why this dependency exists"` |
| **Delete code** | `remove-entity` / `remove-import` / `remove-shared` as appropriate |
| **Move or rename a file** | `move-entity <uid> "new/path.ts"` |
| **Internal-only edits** (private helpers, same file) | **No DSP update required** |

Example — new import after you already have UIDs from `find-by-source`:

```bash
python dsp-cli.py --root . add-import obj-aaaabbbb obj-ccccdddd "Shared validation schemas for login"
```

---

## 6. Impact Analysis Before Refactoring

Before you change a **public** contract or a widely used module:

- **Who depends on this, transitively?** (walk **up** the import graph)

  ```bash
  python dsp-cli.py --root . get-parents obj-targetuid --depth inf
  ```

- **Who imports this directly?**

  ```bash
  python dsp-cli.py --root . get-recipients obj-targetuid
  ```

Review **all consumers** surfaced by these commands before renaming exports, changing signatures, or deleting shared entities.

---

## 7. Set Up Git Hooks (Optional)

Optional automation around `.dsp/`:

- **Pre-commit:** compares **new / deleted files** in the index against the graph so obvious drift is caught early.
- **Pre-push:** runs **full graph checks** (e.g. orphans, cycles) before the change leaves your machine.
- **Agent-assisted review:** deeper LLM-powered analysis can sit alongside these checks in your workflow (see hook README in-repo).

**Install (Unix-like):**

```bash
./hooks/install-hooks.sh
```

On Windows, use **`hooks/install-hooks.ps1`** if you use the PowerShell installer path, or run the shell script from Git Bash / WSL.

---

## 8. What’s Next

- **[ARCHITECTURE.md](ARCHITECTURE.md)** — full protocol and storage model
- **[docs/workflows/brownfield.md](docs/workflows/brownfield.md)** — detailed brownfield workflow
- **[docs/workflows/greenfield.md](docs/workflows/greenfield.md)** — detailed greenfield workflow
- **[docs/comparisons/](docs/comparisons/)** — DSP vs GSD, DSP vs Superpowers, and related notes
- **[integrations/](integrations/)** — Claude Code, Cursor, Codex integration packs

---

---

## Tip: study the boilerplate

Even if you're adding DSP to an existing project, [**dsp-boilerplate**](https://github.com/k-kolomeitsev/dsp-boilerplate) is a great reference to see how a properly bootstrapped DSP graph looks in practice — entity structure, `@dsp` markers in code, import edges with `why`, multi-root TOCs, and integration configs for all agents.

---

*You now have DSP initialized, a mental model for brownfield vs greenfield, and the commands to navigate, update, and analyze impact. Run `python dsp-cli.py --root . get-stats` anytime to see how your graph is growing.*
```

## File: `LICENSE`
```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

1.  Definitions.

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

2.  Grant of Copyright License. Subject to the terms and conditions of
    this License, each Contributor hereby grants to You a perpetual,
    worldwide, non-exclusive, no-charge, royalty-free, irrevocable
    copyright license to reproduce, prepare Derivative Works of,
    publicly display, publicly perform, sublicense, and distribute the
    Work and such Derivative Works in Source or Object form.

3.  Grant of Patent License. Subject to the terms and conditions of
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

4.  Redistribution. You may reproduce and distribute copies of the
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

5.  Submission of Contributions. Unless You explicitly state otherwise,
    any Contribution intentionally submitted for inclusion in the Work
    by You to the Licensor shall be under the terms and conditions of
    this License, without any additional terms or conditions.
    Notwithstanding the above, nothing herein shall supersede or modify
    the terms of any separate license agreement you may have executed
    with Licensor regarding such Contributions.

6.  Trademarks. This License does not grant permission to use the trade
    names, trademarks, service marks, or product names of the Licensor,
    except as required for reasonable and customary use in describing the
    origin of the Work and reproducing the content of the NOTICE file.

7.  Disclaimer of Warranty. Unless required by applicable law or
    agreed to in writing, Licensor provides the Work (and each
    Contributor provides its Contributions) on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
    implied, including, without limitation, any warranties or conditions
    of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
    PARTICULAR PURPOSE. You are solely responsible for determining the
    appropriateness of using or redistributing the Work and assume any
    risks associated with Your exercise of permissions under this License.

8.  Limitation of Liability. In no event and under no legal theory,
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

9.  Accepting Warranty or Additional Liability. While redistributing
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

Copyright 2026 KONSTANTIN KOLOMEITSEV

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
[![GitHub stars](https://img.shields.io/github/stars/k-kolomeitsev/data-structure-protocol?style=social)](https://github.com/k-kolomeitsev/data-structure-protocol)
[![License](https://img.shields.io/github/license/k-kolomeitsev/data-structure-protocol)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude_Code-supported-green)]()
[![Cursor](https://img.shields.io/badge/Cursor-supported-green)]()
[![Codex](https://img.shields.io/badge/Codex-supported-green)]()

# Data Structure Protocol (DSP)

**The missing memory layer for AI-assisted development**

---

## The problem

Your agent re-reads the same codebase every session. **DSP fixes that.**

Every time you start a new task, your AI coding agent spends the first 5–15 minutes "getting oriented" — scanning files, tracing imports, figuring out what depends on what. On large projects this becomes a constant tax on tokens and attention. Context is rebuilt from scratch, every single time.

DSP is a graph-based long-term structural memory stored in `.dsp/`. It gives agents a persistent, versionable map of your codebase — entities, dependencies, public APIs, and the *reasons* behind every connection — so they can pick up exactly where they left off.

> **DSP is not another workflow framework.** It's the persistent structural memory layer that's missing from every AI coding workflow.

---

## Install

**macOS / Linux:**

```bash
curl -fsSL https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.sh | bash
```

**Windows:**

```powershell
irm https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.ps1 | iex
```

**Codex:**

```
$skill-installer install https://github.com/k-kolomeitsev/data-structure-protocol/tree/main/skills/data-structure-protocol
```

---

## What you get

- **Agent stops re-learning your project every session** — structural context persists across tasks, sessions, and even team members
- **Dependency discovery in seconds, not minutes** — graph traversal replaces full-repo scanning
- **Impact analysis before refactors** — know what breaks before you touch it
- **Safer changes on brownfield codebases** — hidden couplings become visible edges in the graph
- **Works with Claude Code, Cursor, Codex — no lock-in** — DSP is an agent skill, not a platform
- **Git-native and versionable** — `.dsp/` is plain text, diffs cleanly, reviews like code

> **Honest trade-off:** bootstrapping DSP on a large project takes real effort (time, tokens, discipline). It pays back over the project lifetime through lower per-task token usage, faster discovery, and more predictable agent behavior.

---

## How it works

```
┌──────────────────────┐
│      Codebase        │
│  (files + assets)    │
└──────────┬───────────┘
           │  create/update graph as you work
           ▼
┌──────────────────────┐
│   DSP Builder / CLI  │
│   (dsp-cli.py)       │
└──────────┬───────────┘
           │  writes
           ▼
┌──────────────────────┐
│        .dsp/         │
│ entity graph + whys  │
└──────────┬───────────┘
           │  reads/searches/traverses
           ▼
┌──────────────────────┐
│   LLM Orchestrator   │
│ (your agent + skill) │
└──────────────────────┘
```

As you work, DSP builds a lightweight graph of your codebase: modules, functions, dependencies, and public APIs. Each connection carries a `why` — the reason it exists. Your agent reads this graph instead of re-scanning the repo, navigates structure through graph traversal, and keeps the graph updated as code evolves.

The graph lives in `.dsp/` — plain text files that commit, diff, and merge like any other source artifact.

---

## Quick start

### Option A: Start from the boilerplate (fastest)

[**dsp-boilerplate**](https://github.com/k-kolomeitsev/dsp-boilerplate) is a production-ready fullstack starter — **NestJS 11 + React 19 + Vite 7** in Docker Compose, with a **fully initialized DSP graph**, pre-configured skills for all agents, Cursor rules, git hooks, and CI.

```bash
git clone https://github.com/k-kolomeitsev/dsp-boilerplate.git my-project
cd my-project
docker-compose up -d
```

Everything is wired: `.dsp/` graph with two roots (backend + frontend), `@dsp` markers in all source files, DSP skills for Cursor, Claude Code, and Codex. You can start coding and the agent already knows the entire project structure.

### Option B: Add DSP to any project

#### 1. Initialize

```bash
python dsp-cli.py --root . init
```

#### 2. Create entities

```bash
python dsp-cli.py --root . create-object "src/app.ts" "Main application entrypoint"
# → obj-a1b2c3d4

python dsp-cli.py --root . create-function "src/app.ts#start" "Starts the HTTP server" --owner obj-a1b2c3d4
# → func-7f3a9c12

python dsp-cli.py --root . add-import obj-a1b2c3d4 obj-deadbeef "HTTP routing"
```

#### 3. Navigate

```bash
python dsp-cli.py --root . search "authentication"
python dsp-cli.py --root . find-by-source "src/auth/index.ts"
python dsp-cli.py --root . get-children obj-a1b2c3d4 --depth 2
```

#### 4. Impact analysis

```bash
python dsp-cli.py --root . get-parents obj-a1b2c3d4 --depth inf
python dsp-cli.py --root . get-recipients obj-a1b2c3d4
```

> Before any refactor, run `get-parents` or `get-recipients` to see everything that depends on the entity you're about to change.

---

## Supported agents

DSP installs as a skill for your agent. Pick your agent and scope.

Don't have a coding agent yet? Install one first:

| Agent | Install |
|---|---|
| **Claude Code** | `npm i -g @anthropic-ai/claude-code` — [docs](https://docs.anthropic.com/en/docs/claude-code/setup) |
| **Cursor** | [cursor.com/downloads](https://www.cursor.com/downloads) — [docs](https://docs.cursor.com) |
| **Codex CLI** | `npm i -g @openai/codex` — [docs](https://developers.openai.com/codex/cli) \| [github](https://github.com/openai/codex) |

### macOS / Linux

| Agent | Project Install | Global Install |
|---|---|---|
| **Cursor** | `curl -fsSL https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.sh \| bash -s -- cursor` | `curl -fsSL https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.sh \| bash -s -- --global cursor` |
| **Claude Code** | `curl -fsSL https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.sh \| bash -s -- claude` | `curl -fsSL https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.sh \| bash -s -- --global claude` |
| **Codex** | `curl -fsSL https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.sh \| bash -s -- codex` | `curl -fsSL https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.sh \| bash -s -- --global codex` |

### Windows

```powershell
# Project-level (current directory)
irm https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.ps1 | iex

# With specific agent
powershell -ExecutionPolicy Bypass -File install.ps1 -Agent cursor
powershell -ExecutionPolicy Bypass -File install.ps1 -Agent claude
powershell -ExecutionPolicy Bypass -File install.ps1 -Agent codex

# Global (user-level)
powershell -ExecutionPolicy Bypass -File install.ps1 -Agent cursor -Global
```

### Codex (alternative)

```
$skill-installer install https://github.com/k-kolomeitsev/data-structure-protocol/tree/main/skills/data-structure-protocol
```

> **Project install** puts the skill in your repo (`.cursor/skills/`, `.claude/skills/`, `.codex/skills/`).
> **Global install** puts it in your home directory so it's available across all projects.

---

## DSP vs alternatives

Modern agents already know how to plan, write tests, verify, and ship. They don't need process wrappers. What they lack is **memory**.

| | **DSP** | **GSD** | **Superpowers** |
|---|---|---|---|
| **Core idea** | Persistent structural memory | Process/confidence wrapper | Engineering discipline (TDD) |
| **What it solves** | Agent has no memory of project between sessions | Agent doesn't follow structured workflow | Agent might skip tests/planning |
| **Is the problem real?** | Yes — no model has built-in project memory | Diminishing — modern models plan and verify natively | Diminishing — modern models know TDD when prompted |
| **Persistent memory** | Full graph across sessions | None | None |
| **Impact analysis** | Built-in (graph traversal) | No | No |
| **Brownfield** | First-class | One-time scan | No explicit support |
| **Overhead** | Low | Medium | Medium |

> Modern agents are smarter than most mid-level engineers. They plan, they test, they verify. They just can't remember your project. DSP is the fix. [Detailed comparison with GSD](./docs/comparisons/dsp-vs-gsd.md) | [Detailed comparison with Superpowers](./docs/comparisons/dsp-vs-superpowers.md)

---

## Core concepts

| Concept | What it is |
|---|---|
| **Entity** | A node in the graph. Either an **Object** (module/file/class/config/external dep) or a **Function** (function/method/handler) |
| **UID** | Stable identifier (`obj-<8hex>`, `func-<8hex>`). File paths are attributes, not identity — entities survive renames and moves |
| **imports** | Outgoing edges — what this entity uses, with a `why` for each connection |
| **shared** | Public API of an object — what it exposes to consumers |
| **exports/** | Reverse index — who imports this entity and why (incoming edges) |
| **TOC** | Per-entrypoint table of contents listing all reachable entities from a root |

UID markers anchor identity in source code:

```ts
// @dsp func-7f3a9c12
export function calculateTotal(items: Item[]): number { /* ... */ }
```

```python
# @dsp func-3c19ab8e
def process_payment(order):
    ...
```

---

## Storage format

`.dsp/` is plain text in a deterministic directory layout:

```
.dsp/
├── TOC                        # Table of contents (single root)
├── TOC-<rootUid>              # One TOC per root (multi-root projects)
├── obj-a1b2c3d4/              # Object entity
│   ├── description            # source, kind, purpose
│   ├── imports                # imported UIDs (one per line)
│   ├── shared                 # exported/shared UIDs (one per line)
│   └── exports/               # reverse index
│       ├── <importer_uid>     # why the whole object is imported
│       └── <shared_uid>/      # per shared entity
│           ├── description    # what is exported
│           └── <importer_uid> # why this shared is imported
└── func-7f3a9c12/             # Function entity
    ├── description
    ├── imports
    └── exports/
        └── <owner_uid>        # ownership link
```

Full specification: [`ARCHITECTURE.md`](./ARCHITECTURE.md)

---

## Git hooks & CI

DSP ships with hooks that keep the graph in sync with your code:

| Hook | What it does | LLM required |
|---|---|---|
| **pre-commit** | Checks staged files against DSP graph — flags new files without entities, deleted files still referenced, orphans | No |
| **pre-push** | Full graph integrity — orphan detection, cycle detection, stats summary | No |
| **Agent-assisted review** | Deep semantic analysis of changes against DSP entities, dependency impact | Yes |

Install hooks:

```bash
./hooks/install-hooks.sh          # macOS/Linux
.\hooks\install-hooks.ps1         # Windows
```

See [`hooks/`](./hooks/) for configuration, standalone scripts, and GitHub Actions integration.

---

## Integration packs

Ready-made configurations for each supported agent:

| Agent | Skill location |
|---|---|
| **Cursor** | `.cursor/skills/data-structure-protocol/` |
| **Claude Code** | `.claude/skills/data-structure-protocol/` |
| **Codex** | `.codex/skills/data-structure-protocol/` |

Each integration includes the skill instructions (`SKILL.md`), CLI (`dsp-cli.py`), and reference docs. See [`integrations/`](./integrations/) for agent-specific setup guides.

---

## Documentation

| Document | Description |
|---|---|
| [**dsp-boilerplate**](https://github.com/k-kolomeitsev/dsp-boilerplate) | Fullstack boilerplate (NestJS + React + Docker Compose) with DSP pre-initialized — the fastest way to start |
| [**GETTING_STARTED.md**](../corp/docs/usage_guides/getting_started.md) | Step-by-step guide from install to first impact analysis |
| [**ARCHITECTURE.md**](./ARCHITECTURE.md) | Full protocol specification — entity model, storage format, operations |
| [**docs/comparisons/**](./docs/comparisons/) | Detailed comparisons with GSD, Superpowers, and other tools |
| [**docs/workflows/**](./docs/workflows/) | Workflow guides — bootstrap, brownfield adoption, team usage |
| [**integrations/**](./integrations/) | Agent-specific integration guides and configurations |

---

## Contributing

Contributions are welcome. Areas where help is most valuable:

- **Architecture spec** — improving [`ARCHITECTURE.md`](./ARCHITECTURE.md)
- **CLI** — keeping `dsp-cli.py` aligned with the spec
- **Skill instructions** — refining [`SKILL.md`](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) for agent clarity
- **New integrations** — adding support for more agents and editors
- **Documentation** — examples, workflow guides, comparisons

Please keep changes minimal, explicit, and consistent with the "minimal sufficient context" philosophy.

---

## License

Apache License 2.0 — see [`LICENSE`](./LICENSE).
```

## File: `article.md`
```markdown
## DSP (Data Structure Protocol): how to give LLM agents "long-term memory" of a large repository

There’s a pattern everyone who works with agents recognizes: **the first 5–15 minutes are spent not on the task, but on “getting oriented.”** Where is the entry point? Where do the dependencies come from? Why this library and not another one? Who considers this a public API? In a small project it’s annoying. In a large one, it becomes a constant tax on tokens and attention.

DSP (Data Structure Protocol) “externalizes the project map” — into a simple, versioned, language-agnostic graph that lives alongside the code and is available to the agent as persistent memory.

The goal is phrased in the architecture like this:

```
1) Goal and scope

The goal of DSP is to store minimal, but sufficient context about a repository / artifact system as a graph “entities → dependencies / public API”, so that an LLM can:

- quickly locate the necessary fragments by UID,
- understand why entities exist and how they are connected,
- avoid having to load the entire source tree into the context window.

DSP is long-term memory and an index of the project for an LLM. At any time, the agent can run a project-wide search (grep), find the required entities by descriptions/keywords, and from the found UID expand the entire relationship graph: incoming dependencies, outgoing imports, and consumers via `exports`. This replaces the need to “remember” the project structure or load it in full — the entire project map is always available through `.dsp`.
```

---

## What DSP is, in essence

### **DSP = an entity graph + the reasons behind connections**

DSP is stored in the **`.dsp/`** directory. Each “entity” gets a stable **UID** and a small set of files:

- **`description`**: _where it is_ (`source`), _what it is_ (`kind`), _why it exists_ (`purpose`).
- **`imports`**: what this entity uses (UID references).
- **`shared`**: what it exposes as a public API (exports).
- **`exports/`**: a reverse index — **who imports this entity and why** (the `why` text next to each consumer).

In large systems, one detail matters especially: DSP captures not only “what depends on what,” but also **why**. This drastically reduces guesswork in refactoring, migrations, and legacy removal.

### **There are only two base entity types**

- **Object**: module/file/class/config/resource/external dependency — “everything that isn’t a function.”
- **Function**: function/method/handler/pipeline.

Another bonus: **DSP is language-agnostic**. It works the same across TS/JS, Python, Go, infrastructure YAML, SQL, assets, and so on. The architecture also explicitly defines “import completeness”: **if something is imported, it must exist in `.dsp`**, including styles, images, JSON, wasm, and other artifacts. This matters more than it seems: agents more often lose not code, but _resource dependencies_.

---

## Why UID is the central idea

DSP is built on identity by UID, not by path. A path is an attribute. A UID is an entity’s “identity.”

- Renamed a file → run `move-entity`, the UID stays the same.
- Moved code around / reformatted → the UID stays the same.
- **A UID changes only when the purpose (semantic identity) changes**: the module truly became “about something else.”

To attach a UID to entities inside a file (exported functions/classes), DSP uses a simple marker comment `@dsp <uid>` right in the source code. It’s a pragmatic choice: it doesn’t depend on line numbers, works in any language, and is easy to find with grep.

---

## How an agent “walks” DSP instead of endlessly reading code

A typical agent workflow in a DSP-based project looks like this:

- **Find an entity**: `search` by keywords, or `find-by-source` by file path.
- **Understand the boundaries**: read `description`, `shared`, `imports`.
- **Pull context in batches**: instead of “give me the whole repo,” the agent fetches only the nodes it needs plus 1–2 levels of dependencies.
- **Estimate impact**: who consumes the entity and why (`get-parents` / `get-recipients`), whether there are cycles, whether there are “orphans.”

Example commands (PowerShell style; the CLI is shipped inside the skill):

```powershell
python .\.claude\skills\data-structure-protocol\scripts\dsp-cli.py --root . search "authorization"

python .\.claude\skills\data-structure-protocol\scripts\dsp-cli.py --root . get-entity obj-a1b2c3d4
python .\.claude\skills\data-structure-protocol\scripts\dsp-cli.py --root . get-children obj-a1b2c3d4 --depth 2

python .\.claude\skills\data-structure-protocol\scripts\dsp-cli.py --root . get-recipients obj-a1b2c3d4
python .\.claude\skills\data-structure-protocol\scripts\dsp-cli.py --root . get-path obj-a1b2c3d4 func-7f3a9c12
```

---

## What the `data-structure-protocol` skill adds (and why it’s more important than it seems)

DSP architecture is a set of rules. But without discipline an agent can easily violate them: poke the code at random, drag half the repo into the context, forget to update the index, and break graph integrity.

The skill covers exactly the operational part:

- **It embeds an Agent Prompt**: “before changing anything — find the entities; when creating — register; when importing — add `why`; when deleting — perform cascade cleanup.”
- **It provides reference materials** in `references/`: the storage format, the bootstrap algorithm (DFS from entry points), the semantics of operations.
- **It ships a production-ready CLI** `scripts/dsp-cli.py` that implements the operations from `ARCHITECTURE.md` and supports navigation/diagnostics (cycles/orphans/stats).

**DSP becomes not a “document,” but a living contract** that the agent executes while working — and keeps `.dsp` consistent without manual intervention.

---

## Cost of adoption: bootstrapping a large project will be expensive

Yes. **The initial bootstrap on a large repository is expensive** — in time, attention, and tokens.

Why:

- You need to identify the root entry points (and there are many in a monorepo).
- You need to traverse dependencies depth-first (DFS) and record all reachable modules/files/resources.
- For each node, you need to write a _minimal, but precise_ `purpose`.
- You need to fill in the reasons (`why`) for import edges in a disciplined way — otherwise half of DSP’s value disappears.
- Sometimes you need to add `@dsp` markers in source files for exported entities (so the UID becomes an “anchor” in code).

On large systems, this can realistically be its own mini-project.

---

## Why it pays off (and usually pays off faster than it seems)

The value of DSP is not “a pretty structure.” It’s in the economics of agent work:

- **Fewer tokens spent on orientation**: instead of repeatedly “warming up” context, the agent reads short `description/imports/shared/exports` and pulls exactly the files that need to be changed.
- **Context doesn’t dissolve between tasks**: `.dsp` is external memory that doesn’t depend on the current context window or the model’s “mood.”
- **Fast semantic lookup**: `search` finds entities by keywords, and `exports/` answers the question “why is this even here.”
- **Refactoring becomes safer**: impact analysis gets cheaper — you quickly get all consumers of an entity and update them precisely.
- **External dependencies become transparent**: external packages are captured as `kind: external`, without bloating the graph, but they remain navigable via the exports index.

And here’s an important point from the architecture — **granularity control**, so DSP doesn’t turn into a junk drawer:

```
10) Granularity and minimal-context policy

- Completeness at the file level, not at the code-within-file level. “Import completeness” (section 2) means that every file/module that is imported in the project must have an Object in `.dsp`. This is about files and modules — not about every variable inside a file. Within a single file, a separate UID is assigned only to an entity that is shared externally (`shared`) or used from multiple places. Local variables, internal helpers, private fields — remain part of the parent Object, without their own UID. If granularity keeps growing, something is being done wrong.

- Update consumers via `exports`. To update a library/module/symbol, it’s enough to open `exports` of the imported entity and get the list of importers (consumers) by UID, then update them precisely.

- Change tracking. `git diff` shows what changed — a new file was created, a function or object changed. The changed files are passed to the LLM to update DSP. Changes inside functions often don’t require updating DSP, because descriptions capture purpose, not implementation details — unless imports were added/removed.
```

This is what makes DSP viable over time: **the index stays compact**, and updates stay rare and meaningful.

---

## When DSP really shines

- **Large monoliths and monorepos**, where the context “never fits.”
- **Long-lived products**, where agents will work for months and years, not just one sprint.
- **Teams that frequently do refactors/migrations/dependency replacements**.
- **Projects with a complex resource layer** (assets/configs/generation) that is hard for agents to keep in their heads.

---

## Conclusion

DSP is an attempt to do for LLM agents what people have long done informally: keep a mental map of a system. Only instead of a head — **a graph on disk**; instead of “that’s how I remember it” — **minimal descriptions, connections, and reasons**; instead of “read the whole project” — **targeted navigation from entry points**.

Yes, **bootstrapping a large project will be expensive**. But if you truly plan to use agents systematically, this cost typically comes back through:

- fewer tokens spent on orientation,
- less context loss between tasks,
- faster discovery of the needed modules/dependencies,
- more predictable task execution (especially refactoring work).
```

## File: `install.ps1`
```powershell
#Requires -Version 5.1
[CmdletBinding()]
param(
    [ValidateSet('cursor', 'claude', 'codex', 'all')]
    [string[]]$Agent = @('all'),

    [switch]$Global,

    [string]$Branch = 'main'
)

$ErrorActionPreference = 'Stop'
$DSP_REPO = 'k-kolomeitsev/data-structure-protocol'
$DSP_SKILL_PATH = 'skills/data-structure-protocol'

function Get-TargetPath {
    param([string]$AgentName)

    if ($Global) {
        switch ($AgentName) {
            'cursor' { return Join-Path $HOME '.cursor/skills/data-structure-protocol' }
            'claude' { return Join-Path $HOME '.claude/skills/data-structure-protocol' }
            'codex'  { return Join-Path $HOME '.codex/skills/data-structure-protocol' }
        }
    } else {
        switch ($AgentName) {
            'cursor' { return '.cursor/skills/data-structure-protocol' }
            'claude' { return '.claude/skills/data-structure-protocol' }
            'codex'  { return '.codex/skills/data-structure-protocol' }
        }
    }
}

function Install-ForAgent {
    param([string]$AgentName)

    $target = Get-TargetPath $AgentName
    Write-Host "=> Installing DSP skill for $AgentName => $target"

    New-Item -ItemType Directory -Force -Path $target | Out-Null

    $tmp = Join-Path ([System.IO.Path]::GetTempPath()) "dsp-install-$([guid]::NewGuid().ToString('N').Substring(0,8))"
    $zipPath = "$tmp.zip"

    try {
        Invoke-WebRequest -Uri "https://github.com/$DSP_REPO/archive/$Branch.zip" `
            -OutFile $zipPath -UseBasicParsing

        Expand-Archive -Path $zipPath -DestinationPath $tmp -Force

        $extractedRoot = Get-ChildItem -Path $tmp -Directory | Select-Object -First 1
        $sourcePath = Join-Path $extractedRoot.FullName $DSP_SKILL_PATH

        if (-not (Test-Path $sourcePath)) {
            throw "Skill folder not found at $sourcePath"
        }

        Copy-Item -Path "$sourcePath\*" -Destination $target -Recurse -Force
        Write-Host "[OK] DSP skill installed for $AgentName" -ForegroundColor Green
    }
    finally {
        if (Test-Path $zipPath) { Remove-Item $zipPath -Force }
        if (Test-Path $tmp) { Remove-Item $tmp -Recurse -Force }
    }
}

Write-Host ""
Write-Host "DSP Skill Installer" -ForegroundColor Cyan
Write-Host "===================" -ForegroundColor Cyan
Write-Host ""

$resolvedAgents = if ($Agent -contains 'all') { @('cursor', 'claude', 'codex') } else { $Agent }

foreach ($a in $resolvedAgents) {
    Install-ForAgent $a
}

Write-Host ""
Write-Host "Done! Restart your agent/IDE to pick up the new skill." -ForegroundColor Green
Write-Host ""
```

## File: `install.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

DSP_REPO="k-kolomeitsev/data-structure-protocol"
DSP_BRANCH="main"
DSP_SKILL_PATH="skills/data-structure-protocol"

usage() {
  cat <<EOF
DSP Skill Installer

Usage: $0 [OPTIONS] [AGENT...]

Agents: cursor, claude, codex, all (default: all)

Options:
  --global    Install to user-level directory (~/.cursor/skills/ etc.)
  --branch B  Use specific branch (default: main)
  --help      Show this help

Examples:
  curl -fsSL https://raw.githubusercontent.com/$DSP_REPO/main/install.sh | bash
  curl -fsSL https://raw.githubusercontent.com/$DSP_REPO/main/install.sh | bash -s -- cursor
  curl -fsSL https://raw.githubusercontent.com/$DSP_REPO/main/install.sh | bash -s -- --global all
EOF
  exit 0
}

GLOBAL=false
AGENTS=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --global) GLOBAL=true; shift ;;
    --branch) DSP_BRANCH="$2"; shift 2 ;;
    --help) usage ;;
    *) AGENTS+=("$1"); shift ;;
  esac
done

[[ ${#AGENTS[@]} -eq 0 ]] && AGENTS=("all")

get_targets() {
  local agent="$1"
  local base
  if [[ "$GLOBAL" == "true" ]]; then
    case "$agent" in
      cursor) base="$HOME/.cursor/skills" ;;
      claude) base="$HOME/.claude/skills" ;;
      codex)  base="$HOME/.codex/skills" ;;
    esac
  else
    case "$agent" in
      cursor) base=".cursor/skills" ;;
      claude) base=".claude/skills" ;;
      codex)  base=".codex/skills" ;;
    esac
  fi
  echo "$base/data-structure-protocol"
}

install_for_agent() {
  local agent="$1"
  local target
  target="$(get_targets "$agent")"

  echo "→ Installing DSP skill for $agent → $target"
  mkdir -p "$target"

  local tmp
  tmp="$(mktemp -d)"
  trap "rm -rf '$tmp'" EXIT

  curl -fsSL "https://github.com/$DSP_REPO/archive/$DSP_BRANCH.tar.gz" \
    | tar -xz -C "$tmp" --strip-components=1

  cp -r "$tmp/$DSP_SKILL_PATH/"* "$target/"
  echo "✓ DSP skill installed for $agent"
}

resolve_agents() {
  for a in "${AGENTS[@]}"; do
    case "$a" in
      all) echo "cursor claude codex" ;;
      cursor|claude|codex) echo "$a" ;;
      *) echo "Unknown agent: $a" >&2; exit 1 ;;
    esac
  done
}

echo ""
echo "DSP Skill Installer"
echo "==================="
echo ""

for agent in $(resolve_agents); do
  install_for_agent "$agent"
done

echo ""
echo "Done! Restart your agent/IDE to pick up the new skill."
echo ""
```

## File: `docs/comparisons/dsp-vs-gsd.md`
```markdown
# DSP vs GSD (Get Shit Done)

## The real question

Modern AI coding agents — Claude Sonnet 4, GPT-4.1, Gemini 2.5 Pro — are already better at planning, structuring work, verifying output, and writing tests than most mid-level engineers. They don't need a wrapper to tell them how to plan. They don't need lifecycle phases imposed from outside. They already know.

The one thing they **cannot** do is remember your project between sessions.

Every new chat, every new task, every context window reset — the agent starts from zero. It re-reads files, re-discovers dependencies, re-learns what depends on what. On large codebases this "orientation tax" burns tokens, burns time, and produces worse results because the agent is working from incomplete information.

**DSP fixes the actual problem.** GSD wraps a problem that modern models have largely solved on their own.

## What each actually does

**DSP** gives agents persistent structural memory. A graph of entities, dependencies, public APIs, and the *reasons* behind every connection — stored in `.dsp/`, versioned with git, readable in seconds. The agent opens a new session and immediately knows the project.

**GSD** gives agents a workflow wrapper. Structured phases (plan → execute → verify → ship), fresh-context management, wave execution. It tells the agent *how* to work — planning docs, verification steps, atomic commits.

The difference: DSP solves a problem agents genuinely have (no memory). GSD solves a problem that was real 12 months ago but that modern models handle natively.

## Feature comparison

| Feature | DSP | GSD |
|---|---|---|
| **Core idea** | Persistent structural memory | Process/confidence wrapper |
| **What it solves** | Agent has no memory of project between sessions | Agent doesn't follow structured workflow |
| **Is the problem still real?** | Yes — no model has built-in project memory | Partially — modern models plan, verify, and ship without external phases |
| **Memory / Persistence** | Full graph persists across sessions, tools, branches | No persistent project memory |
| **Brownfield support** | First-class — DFS bootstrap maps existing codebases | `map-codebase` command — one-time scan, not persistent |
| **Impact analysis** | Built-in — `get-parents`, `get-recipients`, `get-children` | Not available |
| **Overhead** | Low — memory layer, no ceremony | Medium — lifecycle phases, planning docs, verification steps |
| **Install** | `curl \| bash` or `irm \| iex` | `npx get-shit-done-cc@latest` |
| **Codebase mapping** | Full entity graph with `why` for every edge | One-time scan |
| **Session continuity** | Agent reads `.dsp/` — instant structural context | Fresh-context model — each wave starts clean |
| **Dependency discovery** | `search`, `find-by-source`, `get-children` — seconds | Requires re-scanning or agent exploration |
| **Reason tracking** | Every import has a `why`; every export tracks who uses it and why | Not tracked |
| **Git hooks / CI** | Pre-commit, pre-push, GitHub Actions | Git hooks for workflow enforcement |
| **Tool support** | Claude Code, Cursor, Codex | Claude Code, OpenCode, Gemini CLI, Codex, Copilot |

## Why agents don't need lifecycle wrappers

GSD's value proposition is: your agent needs structured phases, otherwise it produces chaotic output.

This was a reasonable claim in early 2025. It is increasingly untrue in 2026:

- **Planning** — ask any modern agent to plan before coding and it will. It doesn't need `/gsd:plan-phase` to know that planning is useful.
- **Verification** — agents already run tests, check types, lint code, and review their own output. They don't need `/gsd:verify-work` as an external trigger.
- **Atomic commits** — any agent instructed to commit atomically will do so. This is prompt-level, not framework-level.
- **Fresh contexts** — useful concept, but the agent can manage context windows without a wrapper orchestrating "waves."

What agents **cannot** do without external help:
- Remember what `src/services/payment.service.ts` imports and why
- Know that 7 modules depend on the auth middleware before you change it
- Recall that the frontend config fetcher was refactored last week and moved to a new path
- Navigate a 200-file codebase without loading everything into context

That's what DSP does. No other tool in the category addresses this.

## Example: "Add authentication to an existing Express.js project"

### With DSP + agent

```bash
# Agent starts a session — reads DSP for instant context
dsp-cli search "express app"
# obj-a1b2c3d4  [purpose] Express application entry point and middleware setup

dsp-cli get-children obj-a1b2c3d4 --depth 2
# Full dependency tree: routes → controllers → services → database

dsp-cli get-recipients obj-a1b2c3d4
# Every module that depends on the app setup

# Agent has full structural context in seconds.
# Plans, implements, tests, ships — using its own intelligence.
# Registers new entities as it goes:
dsp-cli create-object "src/middleware/auth.ts" "JWT authentication middleware"
dsp-cli add-import obj-a1b2c3d4 obj-NEW_AUTH "applies JWT auth to protected routes"

# Next session: agent reads DSP, sees auth already integrated, continues from where it left off.
```

### With GSD + agent

```bash
# /gsd:plan-phase
# Agent scans codebase from scratch (expensive — reads dozens of files)
# GSD generates planning docs (agent could have planned without this)

# /gsd:execute-phase
# Wave 1: Create auth middleware (fresh context — re-reads relevant files)
# Wave 2: Create auth service (another fresh context — re-reads again)
# Wave 3: Integrate with routes (another fresh context — re-reads yet again)

# /gsd:verify-work
# Agent verifies (it would have done this anyway if asked)

# Next session: agent has no memory. Starts from zero again.
# No persistent knowledge that auth exists, what depends on it, or why.
```

The difference: with DSP, the agent spends tokens on **work**. Without it, the agent spends tokens on **re-orientation** — every single session.

## What about using both?

You can use DSP alongside GSD. DSP provides memory; GSD provides workflow ceremony. If your team finds value in GSD's structured phases, DSP makes every phase faster and more accurate because the agent starts with structural context instead of re-scanning.

But the honest take: if the agent already has DSP's structural memory, much of GSD's value disappears. The agent doesn't need a wrapper to plan well when it already knows the full dependency graph. It doesn't need fresh-context waves when it can read `.dsp/` and instantly understand the project.

## Summary

| | DSP | GSD |
|---|---|---|
| **Solves** | Lack of persistent project memory | Lack of structured workflow |
| **Is the problem real in 2026?** | Yes — no model has built-in project memory | Diminishing — modern models are disciplined by default |
| **What you need** | DSP + any modern agent | GSD + hope the agent can't plan on its own |
| **Overhead** | Low | Medium |
| **Persistence** | Full graph across sessions | None |

**The bottom line:** modern agents are smart enough to plan, verify, and ship. They are not smart enough to remember your project. DSP is the fix. Everything else is optional ceremony.

## Try it

- **DSP protocol + skill**: [data-structure-protocol](https://github.com/k-kolomeitsev/data-structure-protocol)
- **Fullstack boilerplate with DSP pre-initialized**: [dsp-boilerplate](https://github.com/k-kolomeitsev/dsp-boilerplate) — NestJS + React + Docker Compose, ready to clone and build on
```

## File: `docs/comparisons/dsp-vs-superpowers.md`
```markdown
# DSP vs Superpowers

## The real question

Superpowers sells engineering discipline — TDD enforcement, structured planning, code review, subagent orchestration. It wraps the agent in a methodology: think first, plan first, test first, review everything.

The question is: does a modern agent need this?

Claude Sonnet 4, GPT-4.1, Gemini 2.5 Pro — these models already know TDD. They know RED-GREEN-REFACTOR. They plan before coding when asked. They review their own output. They decompose tasks. They write tests. They don't need a skill file to tell them that tests should exist before implementation — they learned this from millions of engineering discussions in their training data.

What they **cannot** do is remember your project. Every new session is a blank slate. The agent re-reads your codebase, re-discovers dependencies, re-learns the architecture. On a 200-file project this "orientation phase" is expensive and lossy — the agent builds an incomplete mental model and makes decisions based on partial information.

**DSP solves the problem agents actually have.** Superpowers solves a problem that modern models handle natively.

## What each actually does

**DSP** gives agents persistent structural memory. A graph of entities, dependencies, public APIs, and the *reasons* behind every connection. The agent reads `.dsp/` and knows the project — instantly, accurately, across sessions.

**Superpowers** gives agents engineering methodology. Composable skills that trigger automatically: brainstorming, planning, TDD, code review, subagent-driven development. It tells the agent *how* to approach tasks.

The difference: DSP provides knowledge the agent doesn't have. Superpowers provides discipline the agent already has.

## Feature comparison

| Feature | DSP | Superpowers |
|---|---|---|
| **Core idea** | Persistent structural memory | Engineering discipline enforcement |
| **What it solves** | Agent has no memory of project between sessions | Agent might skip tests/planning/review |
| **Is the problem still real?** | Yes — no model has built-in project memory | Diminishing — modern models follow TDD and plan when prompted |
| **Architecture** | Graph database in `.dsp/` (plain text) | Composable skills/subagents |
| **Memory / Persistence** | Full graph persists across sessions, tools, branches | No persistent project memory |
| **Brownfield support** | First-class — DFS bootstrap for existing codebases | No explicit brownfield workflow |
| **Impact analysis** | Built-in — graph traversal shows what breaks | Not available |
| **TDD** | Not in scope — agent handles this natively | Core selling point — enforces RED-GREEN-REFACTOR |
| **Overhead** | Low — memory layer, no ceremony | Medium — mandates full TDD cycle even for trivial changes |
| **Install** | `curl \| bash` or `irm \| iex` | Plugin marketplace or manual setup |
| **Codebase mapping** | Full entity graph with `why` for every edge | Agent must scan files manually |
| **Session continuity** | Agent reads `.dsp/` — instant context | No built-in session memory |
| **Dependency discovery** | `search`, `find-by-source`, `get-children` — seconds | Agent must explore on its own |
| **Tool support** | Claude Code, Cursor, Codex | Primarily Claude Code and Cursor |

## Why agents don't need discipline enforcement

Superpowers' core value proposition: left to themselves, agents skip tests, don't plan, write sloppy code. You need a framework to force discipline.

This was partly true with earlier models. With current models:

- **TDD** — tell any modern agent "follow TDD, write failing tests first" and it will. It doesn't need a skill file to enforce this — it needs a single line in the system prompt or project rules.
- **Planning** — agents plan naturally when the task is complex. When it's simple, forcing a planning phase is overhead.
- **Code review** — agents can review their own work, run linters, run tests, check types. An external review skill adds a round trip for something the agent already does.
- **Brainstorming** — a modern agent exploring architecture options doesn't need a dedicated skill triggering. It thinks about tradeoffs as part of its reasoning.

What agents **genuinely cannot** do:
- Remember that `PaymentService` imports `StripeClient` and `DatabaseService`, and that `OrderService` and `WebhookHandler` depend on it
- Know that changing `src/lib/common/config-fragment.ts` affects 12 other modules
- Recall the purpose and contract of a module they worked with 3 days ago
- Navigate a multi-root project (backend + frontend) without reading hundreds of files

That's what DSP provides. No amount of "discipline enforcement" solves the memory problem.

## Example: "Add rate limiting to API endpoints"

### With DSP + agent

```bash
# Agent reads DSP — instant structural context
dsp-cli search "middleware"
# obj-55667788  [purpose] API middleware stack — cors, logging, error handling

dsp-cli get-children obj-55667788 --depth 1
# Middleware stack → [cors-config, request-logger, error-handler]

dsp-cli get-recipients obj-55667788
# obj-11223344: API router applies middleware stack to all routes

# Agent already knows: where middleware lives, what's already there,
# who depends on it, how to extend it.
# Plans, writes tests, implements, registers — all with full context.

dsp-cli create-object "src/middleware/rate-limiter.ts" "Rate limiting — sliding window per IP with Redis"
dsp-cli add-import obj-55667788 obj-NEW_RATE_LIMITER "rate limiting before route handlers"

# Next session: agent knows rate limiter exists, where it sits, who uses it.
```

### With Superpowers + agent

```bash
# Brainstorm skill fires — agent scans codebase from scratch
# (reads files to figure out what middleware exists, what routes look like)

# Plan skill fires — creates implementation plan
# (based on the incomplete picture from file scanning)

# Implementation skill: TDD cycle
# Write failing test (agent knows how to do this without the skill)
# Implement rate limiter
# Green test, refactor

# Review skill checks code quality
# (agent could have done this by running tests + linting)

# Next session: agent has no memory. Re-scans everything.
# Doesn't know rate limiter exists or who depends on it.
```

### The difference

With DSP, the agent starts with full structural knowledge and spends tokens on **work**. Without it, every skill in Superpowers starts with a "re-discover the project" phase that burns tokens and produces incomplete context.

The irony: Superpowers' skills would work **dramatically better** if they had DSP's structural context. The brainstorming skill would brainstorm with full knowledge of existing architecture. The planning skill would plan with accurate impact analysis. The review skill would check DSP consistency alongside code quality.

## Can you use both?

Yes. If you find value in Superpowers' TDD enforcement or subagent orchestration, DSP makes every skill more effective by providing instant structural context. The brainstorming skill stops guessing about architecture. The planning skill gets accurate dependency graphs. Subagents receive targeted context from `.dsp/` instead of scanning the full repo.

But the honest question remains: if your agent has DSP's structural memory and you give it a clear instruction like "follow TDD, plan before coding, review your work" — do you still need a framework enforcing this?

For most teams using modern models, the answer is no. The agent is already disciplined. It just needs memory.

## Summary

| | DSP | Superpowers |
|---|---|---|
| **Solves** | Lack of persistent project memory | Lack of engineering discipline |
| **Is the problem real in 2026?** | Yes — no model has built-in project memory | Diminishing — modern models are disciplined when prompted |
| **What you need** | DSP + any modern agent | Superpowers + hope the agent can't write tests on its own |
| **Overhead** | Low | Medium |
| **Persistence** | Full graph across sessions | None |

**The bottom line:** modern agents already know TDD, planning, and code review. They don't know your project structure. DSP is the fix.

## Try it

- **DSP protocol + skill**: [data-structure-protocol](https://github.com/k-kolomeitsev/data-structure-protocol)
- **Fullstack boilerplate with DSP pre-initialized**: [dsp-boilerplate](https://github.com/k-kolomeitsev/dsp-boilerplate) — NestJS + React + Docker Compose, ready to clone and build on
```

## File: `docs/workflows/brownfield.md`
```markdown
# Brownfield Workflow: Adding DSP to an Existing Project

A step-by-step guide for bootstrapping DSP on an existing codebase — the use case where DSP provides the most value.

## Prerequisites

- Python 3.10+
- An existing project with source code
- An AI coding agent (Claude Code, Cursor, or Codex)

## 1. Install the DSP skill

Choose your agent and run the one-liner:

**macOS / Linux:**
```bash
curl -fsSL https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.sh | bash -s -- cursor
```

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.ps1 | iex
```

**Codex (via skill-installer):**
```
$skill-installer install https://github.com/k-kolomeitsev/data-structure-protocol/tree/main/skills/data-structure-protocol
```

This installs the skill (SKILL.md + dsp-cli.py + references) into the appropriate directory for your agent.

## 2. Initialize DSP

```bash
dsp-cli init
# initialized .dsp/
```

This creates the `.dsp/` directory in your project root. Add it to version control — DSP is designed to be git-tracked.

## 3. Identify root entrypoints

Before bootstrapping, identify the root entrypoints of your project. Common patterns:

| Project type | Typical roots |
|---|---|
| Backend API | `src/main.ts`, `src/app.module.ts`, `cmd/server/main.go` |
| Frontend SPA | `src/main.tsx`, `src/App.tsx`, `pages/_app.tsx` |
| Fullstack monorepo | One root per package: `backend/src/main.ts`, `frontend/src/main.tsx` |
| CLI tool | `src/cli.ts`, `cmd/root.go`, `__main__.py` |
| Library | `src/index.ts`, `lib/mod.rs`, `__init__.py` |

For multi-root projects, each root gets its own TOC file using the `--toc` flag.

## 4. Bootstrap via DFS traversal

This is the most important step. The agent traverses the project from root entrypoints downward, registering every entity and its relationships.

### Step 4.1: Register the root

```bash
dsp-cli create-object "src/app.module.ts" \
  "Application root module — bootstraps NestJS app, registers all feature modules and global middleware"
# obj-82e23068
```

### Step 4.2: Open the root file, identify its imports

The agent reads `src/app.module.ts` and identifies all imports. For each import, it registers the target entity and the relationship.

```bash
# Register an imported module
dsp-cli create-object "src/users/users.module.ts" \
  "Users feature module — user CRUD, authentication, profile management"
# obj-a1b2c3d4

# Register the import with a reason
dsp-cli add-import obj-82e23068 obj-a1b2c3d4 \
  "app module imports users module to enable user management endpoints"

# Register another imported module
dsp-cli create-object "src/products/products.module.ts" \
  "Products feature module — product catalog, search, and inventory"
# obj-e5f6a7b8

dsp-cli add-import obj-82e23068 obj-e5f6a7b8 \
  "app module imports products module to enable catalog endpoints"
```

### Step 4.3: Register external dependencies

External libraries are registered as `--kind external`. You don't go inside them, but you track who uses them and why.

```bash
dsp-cli create-object "@nestjs/core" \
  "NestJS core framework — dependency injection, module system, lifecycle hooks" \
  --kind external
# obj-ext-01

dsp-cli add-import obj-82e23068 obj-ext-01 \
  "app module uses NestJS core for module bootstrapping and DI container"
```

### Step 4.4: Traverse depth-first

For each registered module, the agent opens its source, identifies its imports, and repeats the process. This is a DFS (depth-first search) traversal:

```
app.module.ts (root)
├── users/users.module.ts
│   ├── users/users.controller.ts
│   ├── users/users.service.ts
│   │   ├── users/users.repository.ts
│   │   │   └── database/database.service.ts (shared)
│   │   └── auth/auth.service.ts
│   └── users/dto/create-user.dto.ts
├── products/products.module.ts
│   ├── products/products.controller.ts
│   ├── products/products.service.ts
│   └── ...
└── database/database.module.ts (shared across features)
```

At each node:
1. **Register the entity** (`create-object` or `create-function`)
2. **Register its imports** (`add-import` with `why`)
3. **Register its exports** (`create-shared` for public API)
4. **Recurse into imports** (DFS)

### Step 4.5: Register shared/exported entities

When a module exports functions or entities used by other modules, register them:

```bash
# The users service has public methods used by other modules
dsp-cli create-function "src/users/users.service.ts#findById" \
  "Finds a user by ID — returns full user entity or throws NotFoundException" \
  --owner obj-a1b2c3d4
# func-c9d0e1f2

dsp-cli create-function "src/users/users.service.ts#validateCredentials" \
  "Validates email/password pair — returns user entity or null" \
  --owner obj-a1b2c3d4
# func-d3e4f5a6

# Register these as shared exports of the users module
dsp-cli create-shared obj-a1b2c3d4 func-c9d0e1f2 func-d3e4f5a6
```

### Step 4.6: Wire shared imports with exporters

When module A imports a specific function from module B, the import tracks both the function and the exporter:

```bash
# Auth service imports validateCredentials from users service
dsp-cli add-import obj-AUTH_SVC func-d3e4f5a6 \
  "auth service uses validateCredentials to verify login attempts" \
  --exporter obj-a1b2c3d4
```

### Bootstrap tips

- **Don't try to map everything in one session.** Start with the critical path (root → main modules → core services) and expand incrementally.
- **Focus on modules/files first, functions second.** Register all `create-object` entities for the key files, wire their imports, then add `create-function` for important public APIs.
- **External dependencies can be batched.** Register commonly used externals (framework, ORM, HTTP client) once and reference them across modules.
- **The agent should do this, not you.** Give the agent the DSP skill instructions and ask it to "bootstrap DSP for this project starting from `src/main.ts`".

## 5. Daily workflow: navigate → code → update DSP

Once bootstrapped, the daily cycle is:

### Before making changes — navigate

```bash
# Find the entity you need to modify
dsp-cli search "payment"
# obj-p1a2y3m4  [purpose] Payment processing service

dsp-cli find-by-source "src/services/payment.service.ts"
# obj-p1a2y3m4

# Understand its context
dsp-cli get-entity obj-p1a2y3m4
# Shows: source, purpose, imports, shared exports, who depends on it

# See its dependency tree
dsp-cli get-children obj-p1a2y3m4 --depth 2
# Payment service → [Stripe SDK, DB service, Config service]
```

### While coding — work normally

Write code as usual. DSP doesn't interfere with your coding flow.

### After changes — update DSP

```bash
# New file created? Register it.
dsp-cli create-object "src/services/refund.service.ts" \
  "Refund processing — handles partial and full refunds via Stripe"
# obj-r1e2f3u4

# New import added? Track it.
dsp-cli add-import obj-r1e2f3u4 obj-p1a2y3m4 \
  "refund service uses payment service to look up original charges"

# New public function? Register and share.
dsp-cli create-function "src/services/refund.service.ts#processRefund" \
  "Processes a refund request — validates amount, calls Stripe, updates order" \
  --owner obj-r1e2f3u4
# func-n5e6w7f8
dsp-cli create-shared obj-r1e2f3u4 func-n5e6w7f8

# File moved/renamed? Update the source.
dsp-cli move-entity obj-p1a2y3m4 "src/payments/payment.service.ts"

# Import removed? Clean up.
dsp-cli remove-import obj-r1e2f3u4 obj-OLD_DEP

# File deleted? Remove the entity.
dsp-cli remove-entity obj-DELETED_UID
```

## 6. Impact analysis before refactoring

This is where DSP truly shines on brownfield projects.

### "What breaks if I change this?"

```bash
# Get everything that depends on the payment service
dsp-cli get-parents obj-p1a2y3m4 --depth inf
# obj-p1a2y3m4: Payment processing service
# ├── obj-c8d9e0f1: Webhook handler processes payment events
# ├── obj-b3c4d5e6: Order service triggers charges on checkout
# │   ├── obj-f7a8b9c0: Checkout controller
# │   └── obj-d1e2f3a4: Admin order management
# └── obj-r1e2f3u4: Refund service processes refunds

# Get direct consumers
dsp-cli get-recipients obj-p1a2y3m4
# obj-c8d9e0f1: webhook handler processes payment events
# obj-b3c4d5e6: order service triggers charges on checkout
# obj-r1e2f3u4: refund service uses payment service to look up original charges
```

### "What does this module actually depend on?"

```bash
dsp-cli get-children obj-b3c4d5e6 --depth 3
# Order service
# ├── obj-p1a2y3m4: Payment service
# │   ├── obj-ext-stripe: Stripe SDK
# │   └── obj-db-svc: Database service
# ├── obj-inv-svc: Inventory service
# │   └── obj-db-svc: Database service
# └── obj-email-svc: Email notification service
```

### "Are there circular dependencies?"

```bash
dsp-cli detect-cycles
# no cycles detected

# Or:
# cycle 1: obj-a1b2 -> obj-c3d4 -> obj-e5f6 -> obj-a1b2
```

### "What's the connection between these two modules?"

```bash
dsp-cli get-path obj-CHECKOUT_CTRL obj-DB_SERVICE
# obj-CHECKOUT_CTRL -> obj-ORDER_SVC -> obj-PAYMENT_SVC -> obj-DB_SERVICE
```

## 7. Setting up hooks

### Git hooks (pre-commit)

Install DSP consistency checks as pre-commit hooks:

**macOS / Linux:**
```bash
./hooks/install-hooks.sh
```

**Windows:**
```powershell
.\hooks\install-hooks.ps1
```

This installs a pre-commit hook that checks:
- New files are registered in DSP
- Deleted files are removed from DSP
- No orphaned entities
- No broken references

Configure the behavior:

```bash
# Warning mode (default) — warns but doesn't block commits
export DSP_PRECOMMIT_MODE=warn

# Block mode — blocks commits with DSP errors
export DSP_PRECOMMIT_MODE=block
```

### CI (GitHub Actions)

Add `.github/workflows/dsp-consistency.yml` to run DSP checks on every PR. See the [CI workflow template](../../.github/workflows/dsp-consistency.yml).

### Agent hooks (Claude Code / Cursor)

See the integration packs in `integrations/claude/` and `integrations/cursor/` for agent-specific hooks that check DSP consistency during coding sessions.

## 8. Common patterns and tips

### Pattern: Incremental bootstrap

Don't try to map the entire project at once. Start with:

1. **Core modules** — the main entrypoints and critical services
2. **Active development area** — whatever you're working on right now
3. **Shared infrastructure** — database, config, logging, auth
4. **Expand as needed** — when you touch a new area, bootstrap it then

### Pattern: External dependency grouping

Group related external deps under a single entity rather than creating one per import:

```bash
# Good: one entity for the framework
dsp-cli create-object "@nestjs/core + @nestjs/common" \
  "NestJS framework — DI, module system, decorators, HTTP abstractions" \
  --kind external

# Rather than separate entities for @nestjs/core, @nestjs/common, @nestjs/platform-express
```

### Pattern: Regular health checks

Periodically check the graph health:

```bash
dsp-cli get-stats
# Quick overview: entity count, imports, shared, cycles, orphans

dsp-cli get-orphans
# Find disconnected entities that might need cleanup

dsp-cli detect-cycles
# Find circular dependencies to investigate
```

### Tip: Let the agent do the work

The agent already knows the DSP skill instructions. Instead of running CLI commands manually, ask the agent:

- *"Bootstrap DSP for this project starting from `src/main.ts`"*
- *"Update DSP after the changes I just made"*
- *"Run DSP health check and fix any issues"*
- *"Check impact before I refactor the payment module"*

### Tip: Commit `.dsp/` changes with your code

DSP changes should be part of the same commit as the code changes they describe. This keeps the graph and the code in sync at every point in git history.

### Tip: Don't update DSP for internal-only changes

If you change implementation details inside a module without affecting its purpose, imports, or public API, there's no need to update DSP. The protocol tracks *structure and contracts*, not implementation details.

### Tip: Study the boilerplate as a reference

[**dsp-boilerplate**](https://github.com/k-kolomeitsev/dsp-boilerplate) is a fully bootstrapped real-world example — NestJS + React with a complete DSP graph, `@dsp` markers in every source file, multi-root TOCs, import edges with `why`, and integration configs for all agents. It's the best reference for how a finished bootstrap should look.
```

## File: `docs/workflows/greenfield.md`
```markdown
# Greenfield Workflow: Starting a New Project with DSP

A guide for building a new project with DSP from day one — growing the structural graph incrementally alongside your code.

## The fastest path: dsp-boilerplate

If you want to skip all manual setup, use [**dsp-boilerplate**](https://github.com/k-kolomeitsev/dsp-boilerplate) — a production-ready fullstack starter (NestJS 11 + React 19 + Vite 7 + Docker Compose) with DSP fully pre-initialized:

```bash
git clone https://github.com/k-kolomeitsev/dsp-boilerplate.git my-project
cd my-project
docker-compose up -d
```

It comes with a complete `.dsp/` graph (two roots: backend + frontend), `@dsp` markers in all source files, DSP skills for all agents, Cursor rules, Claude Code hooks, git hooks, and CI. Your agent has structural memory from the first session.

If you prefer to start from scratch or use a different stack, follow the manual steps below.

## Prerequisites

- Python 3.10+
- An AI coding agent (Claude Code, Cursor, or Codex)

## 1. Install the DSP skill

Choose your agent and run the one-liner:

**macOS / Linux:**
```bash
curl -fsSL https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.sh | bash -s -- cursor
```

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.ps1 | iex
```

**Codex (via skill-installer):**
```
$skill-installer install https://github.com/k-kolomeitsev/data-structure-protocol/tree/main/skills/data-structure-protocol
```

## 2. Initialize DSP

Right after creating your project scaffold:

```bash
# Create project
mkdir my-project && cd my-project
git init

# Initialize DSP
dsp-cli init
# initialized .dsp/
```

## 3. Create the first module and register

As you write your first file, immediately register it in DSP.

### Example: NestJS backend

```bash
# Create and register the app module (root)
dsp-cli create-object "src/app.module.ts" \
  "Application root module — bootstraps NestJS app, registers feature modules and global config"
# obj-82e23068

# Create and register the first feature module
dsp-cli create-object "src/health/health.module.ts" \
  "Health check module — exposes /health endpoint for load balancer probes"
# obj-a1b2c3d4

# Wire the dependency
dsp-cli add-import obj-82e23068 obj-a1b2c3d4 \
  "app module registers health module for uptime monitoring"

# Register external framework dependency
dsp-cli create-object "@nestjs/core" \
  "NestJS framework — dependency injection, module system, lifecycle management" \
  --kind external
# obj-ext-nest

dsp-cli add-import obj-82e23068 obj-ext-nest \
  "app module uses NestJS core for module bootstrapping and DI container"
```

### Example: Next.js frontend

```bash
# Register the app layout (root)
dsp-cli create-object "src/app/layout.tsx" \
  "Root layout — defines HTML structure, global providers, and shared UI shell"
# obj-layout01

# Register the home page
dsp-cli create-object "src/app/page.tsx" \
  "Home page — landing page with hero section and feature highlights"
# obj-home-pg

dsp-cli add-import obj-layout01 obj-home-pg \
  "layout renders home page as default route"
```

### Example: Python CLI

```bash
# Register the CLI entry point (root)
dsp-cli create-object "src/cli.py" \
  "CLI entry point — argument parsing, command dispatch, global error handling"
# obj-cli-main

# Register the first command module
dsp-cli create-object "src/commands/init.py" \
  "Init command — scaffolds project directory structure and config files"
# obj-cmd-init

dsp-cli add-import obj-cli-main obj-cmd-init \
  "CLI dispatches 'init' subcommand to this handler"
```

## 4. Growing the graph incrementally

The key principle: **register entities as you create them, not after**. This keeps the graph accurate and avoids catch-up work.

### When you create a new file

```bash
# 1. Write the file
# 2. Register it immediately
dsp-cli create-object "src/users/users.service.ts" \
  "Users service — CRUD operations, validation, password hashing"
# obj-usr-svc

# 3. Wire its imports
dsp-cli add-import obj-usr-svc obj-DB_SERVICE \
  "users service uses database for persistence"
dsp-cli add-import obj-usr-svc obj-ext-bcrypt \
  "uses bcrypt for password hashing"
```

### When you create a public function

```bash
# Register the function under its owner
dsp-cli create-function "src/users/users.service.ts#createUser" \
  "Creates a new user — validates input, hashes password, persists to database" \
  --owner obj-usr-svc
# func-create-usr

# Share it (make it part of the module's public API)
dsp-cli create-shared obj-usr-svc func-create-usr
```

### When another module imports it

```bash
# Auth controller imports createUser from users service
dsp-cli add-import obj-auth-ctrl func-create-usr \
  "registration endpoint delegates user creation to users service" \
  --exporter obj-usr-svc
```

### The growth pattern

As your project grows, the graph grows with it naturally:

```
Week 1:  3 entities, 4 imports     (app root, health, one feature)
Week 2:  12 entities, 25 imports   (auth, users, basic CRUD)
Week 3:  28 entities, 67 imports   (payments, notifications, admin)
Week 4:  45 entities, 110 imports  (full MVP)
```

Each entity takes seconds to register. The cumulative investment is small; the cumulative value (instant context for every future session) is large.

## 5. Setting up hooks from day one

On greenfield projects, set up hooks early — it's easier to maintain consistency from the start than to fix it later.

### Git hooks

```bash
# macOS / Linux
./hooks/install-hooks.sh

# Windows
.\hooks\install-hooks.ps1
```

Start with warning mode:

```bash
export DSP_PRECOMMIT_MODE=warn
```

This warns you (or the agent) when a commit includes new files not registered in DSP. Switch to `block` mode once the team is comfortable with the workflow.

### CI (GitHub Actions)

Add the DSP consistency workflow to your repo from day one. Copy `.github/workflows/dsp-consistency.yml` from the DSP repository. This provides:

- Graph stats in PR summaries
- Orphan detection
- Cycle detection
- Coverage check for changed files

### Agent hooks

If using Claude Code, set up the session hooks from the integration pack:

- **Session start** — prints DSP stats summary
- **Pre-write check** — warns if a file being edited isn't in DSP
- **Session end** — reminds about unregistered changes

## 6. Best practices for new projects

### Register modules before functions

Start with `create-object` for each file/module. Add `create-function` for public APIs once the module is stable. Internal helper functions don't need DSP entries.

### Write meaningful `purpose` fields

The `purpose` field is the most valuable part of a DSP entity. Write it as if explaining to a new team member:

```bash
# Weak
dsp-cli create-object "src/auth.ts" "Authentication"

# Strong
dsp-cli create-object "src/auth/auth.service.ts" \
  "Authentication service — JWT token generation/validation, session management, OAuth2 provider integration"
```

### Write meaningful `why` on imports

The `why` field on imports explains *the reason for the dependency*, not just its existence:

```bash
# Weak
dsp-cli add-import obj-A obj-B "imports B"

# Strong
dsp-cli add-import obj-ORDER_SVC obj-PAYMENT_SVC \
  "order service delegates payment processing to payment service during checkout flow"
```

### Use `--toc` for multi-root projects

If your project has multiple entry points (e.g., monorepo), use the `--toc` flag to group entities by root:

```bash
# Backend root
dsp-cli create-object "backend/src/main.ts" "Backend entry point" --toc obj-backend-root
# obj-backend-root

# Frontend root
dsp-cli create-object "frontend/src/main.tsx" "Frontend entry point" --toc obj-frontend-root
# obj-frontend-root

# Read a specific TOC
dsp-cli read-toc --toc obj-backend-root
```

### Don't over-register

Not everything needs a DSP entry. Skip:

- Internal helper functions that aren't exported
- Type definition files (unless they define shared contracts)
- Test files (unless they define test utilities used across modules)
- Configuration files (unless they're shared across features)
- Static assets (unless they're imported by code)

DSP tracks *structure and contracts*. Internal implementation details don't belong in the graph.

### Commit `.dsp/` with your code

Every commit that changes code structure should include the corresponding `.dsp/` changes. This keeps the graph in sync with the codebase at every point in git history.

```bash
git add src/users/users.service.ts .dsp/
git commit -m "feat: add users service with CRUD operations"
```

### Run health checks periodically

```bash
# Quick graph overview
dsp-cli get-stats
# entities: 28, objects: 22, functions: 6, imports: 67, cycles: 0, orphans: 0

# Find disconnected entities
dsp-cli get-orphans
# no orphans

# Check for circular dependencies
dsp-cli detect-cycles
# no cycles detected
```

Make this part of your regular development rhythm — weekly or before each release.
```

## File: `hooks/README.md`
```markdown
# DSP Git Hooks

Git hooks and standalone scripts for **Data Structure Protocol** consistency checking.

## Overview

DSP hooks provide two complementary modes:

| Mode | Speed | LLM Required | Use Case |
|------|-------|-------------|----------|
| **Deterministic** | Fast (< 1s) | No | Pre-commit / pre-push — checks file presence in DSP graph, orphans, cycles |
| **Agent-assisted** | Slower (10-30s) | Yes | Deep review — semantic analysis of changes against DSP entities, dependency impact |

Deterministic checks run automatically on every commit/push. Agent-assisted review is invoked manually for important commits.

## Installation

### Bash (Linux / macOS / Git Bash on Windows)

```bash
./hooks/install-hooks.sh
```

### PowerShell (Windows)

```powershell
.\hooks\install-hooks.ps1
```

Both installers copy `pre-commit` and `pre-push` into your `.git/hooks/` directory.

## Configuration

All configuration is done via environment variables:

| Variable | Values | Default | Description |
|----------|--------|---------|-------------|
| `DSP_PRECOMMIT_MODE` | `warn` \| `block` | `warn` | `warn` — print issues but allow commit; `block` — reject commit if DSP errors exist |
| `DSP_CLI` | path | *(auto-detected)* | Explicit path to `dsp-cli.py`. Auto-detection searches `.cursor/`, `.claude/`, `.codex/`, and `skills/` directories |
| `DSP_SKIP_PATTERNS` | glob list | `*.md,*.txt,*.json,*.yml,*.yaml,*.lock,*.log` | Comma-separated glob patterns for files to skip during checks |

### Examples

```bash
# Block commits with DSP errors
export DSP_PRECOMMIT_MODE=block

# Use a custom CLI path
export DSP_CLI="python /path/to/dsp-cli.py"

# Skip additional patterns
export DSP_SKIP_PATTERNS="*.md,*.txt,*.json,*.yml,*.yaml,*.lock,*.log,*.css"
```

## Hooks

### pre-commit

Runs on every `git commit`. Performs deterministic checks:

- **New/modified files not in DSP** — trackable source files (`.ts`, `.tsx`, `.js`, `.jsx`, `.py`, `.go`, `.rs`, `.java`, `.rb`, `.vue`, `.svelte`) that are staged but have no corresponding DSP entity
- **Deleted files still in DSP** — files removed from the repo but still referenced by DSP entities
- **Orphaned entities** — DSP entities with no valid connections to the graph

In `warn` mode (default), issues are printed but the commit proceeds. In `block` mode, the commit is rejected if any errors are found.

### pre-push

Runs on every `git push`. Performs a full graph integrity check:

- **Orphan detection** — entities not connected to any parent
- **Cycle detection** — circular dependency chains in the DSP graph
- **Graph statistics** — summary of entities, relations, and coverage

Pre-push always runs in warning mode and never blocks the push.

## Standalone Scripts

### dsp-check-staged

Deterministic checker that can be run independently (same logic as pre-commit):

```bash
./hooks/dsp-check-staged.sh          # Bash
.\hooks\dsp-check-staged.ps1         # PowerShell
```

### dsp-agent-review

Agent-assisted deep review. Collects git diff, DSP state for affected files, graph stats, and orphans into a review document:

```bash
./hooks/dsp-agent-review.sh          # Bash
.\hooks\dsp-agent-review.ps1         # PowerShell
```

The review document can be sent to an LLM agent (Claude Code, Cursor, Codex) for semantic analysis. The agent checks:

- Whether DSP entities accurately reflect the code changes
- Whether dependencies and relations need updating
- Whether new entities should be created for new abstractions
- Impact analysis on dependent entities

## File Overview

```
hooks/
├── README.md                 # This file
├── pre-commit                # Git pre-commit hook (bash)
├── pre-push                  # Git pre-push hook (bash)
├── install-hooks.sh          # Installer (bash)
├── install-hooks.ps1         # Installer (PowerShell)
├── dsp-agent-review.sh       # Agent-assisted review (bash)
├── dsp-agent-review.ps1      # Agent-assisted review (PowerShell)
├── dsp-check-staged.sh       # Standalone staged check (bash)
└── dsp-check-staged.ps1      # Standalone staged check (PowerShell)
```
```

## File: `hooks/dsp-agent-review.ps1`
```powershell
#Requires -Version 5.1
[CmdletBinding()]
param(
    [string]$DspCli = "python .cursor\skills\data-structure-protocol\scripts\dsp-cli.py",
    [string]$DspRoot = "."
)

$ErrorActionPreference = 'Stop'

if (-not (Test-Path "$DspRoot\.dsp")) {
    Write-Host "No .dsp\ directory found. Skipping agent review."
    exit 0
}

$diff = git diff --staged 2>$null
if (-not $diff) { $diff = git diff HEAD~1 }
if (-not $diff) {
    Write-Host "No changes to review."
    exit 0
}

$stagedFiles = (git diff --cached --name-only --diff-filter=ACMRD 2>$null)
if (-not $stagedFiles) {
    $stagedFiles = (git diff HEAD~1 --name-only --diff-filter=ACMRD)
}

$dspContext = ""
foreach ($file in $stagedFiles -split "`n") {
    $file = $file.Trim()
    if (-not $file) { continue }

    $entity = & cmd /c "$DspCli --root $DspRoot find-by-source `"$file`"" 2>$null
    if ($entity) {
        $uid = [regex]::Match($entity, '(obj|func)-[a-f0-9]{8}').Value
        if ($uid) {
            $entityInfo = & cmd /c "$DspCli --root $DspRoot get-entity $uid" 2>$null
            $dspContext += "=== DSP entity for $file ($uid) ===`n$entityInfo`n`n"
        }
    } else {
        $dspContext += "=== $file - NOT in DSP ===`n`n"
    }
}

$stats = & cmd /c "$DspCli --root $DspRoot get-stats" 2>$null
$orphans = & cmd /c "$DspCli --root $DspRoot get-orphans" 2>$null

$reviewFile = Join-Path $env:TEMP "dsp-review-$([guid]::NewGuid().ToString('N').Substring(0,8)).md"

@"
# DSP Consistency Review Request

## Git Diff

``````diff
$($diff -join "`n")
``````

## DSP State for Affected Files

$dspContext

## Project Stats

$stats

## Current Orphans

$orphans

## Review Instructions

Check all items from the DSP consistency review checklist.
For each issue found, provide the exact dsp-cli command to fix it.
"@ | Set-Content -Path $reviewFile -Encoding UTF8

Write-Host ""
Write-Host "Review context saved to: $reviewFile" -ForegroundColor Cyan
Write-Host ""
Write-Host "Send this to your agent for review:"
Write-Host "  Get-Content $reviewFile | Set-Clipboard"
Write-Host ""
Write-Host "Or pipe to agent CLI directly."
```

## File: `hooks/dsp-agent-review.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

DSP_CLI="${DSP_CLI:-python .cursor/skills/data-structure-protocol/scripts/dsp-cli.py}"
DSP_ROOT="${DSP_ROOT:-.}"

if [[ ! -d "$DSP_ROOT/.dsp" ]]; then
  echo "No .dsp/ directory found. Skipping agent review."
  exit 0
fi

DIFF=$(git diff --staged 2>/dev/null || git diff HEAD~1)
if [[ -z "$DIFF" ]]; then
  echo "No changes to review."
  exit 0
fi

STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACMRD 2>/dev/null || git diff HEAD~1 --name-only --diff-filter=ACMRD)

DSP_CONTEXT=""
for file in $STAGED_FILES; do
  entity=$($DSP_CLI --root "$DSP_ROOT" find-by-source "$file" 2>/dev/null || true)
  if [[ -n "$entity" ]]; then
    uid=$(echo "$entity" | grep -oP '(obj|func)-[a-f0-9]{8}' | head -1)
    if [[ -n "$uid" ]]; then
      entity_info=$($DSP_CLI --root "$DSP_ROOT" get-entity "$uid" 2>/dev/null || true)
      DSP_CONTEXT+="=== DSP entity for $file ($uid) ===\n$entity_info\n\n"
    fi
  else
    DSP_CONTEXT+="=== $file — NOT in DSP ===\n\n"
  fi
done

STATS=$($DSP_CLI --root "$DSP_ROOT" get-stats 2>/dev/null || echo "stats unavailable")
ORPHANS=$($DSP_CLI --root "$DSP_ROOT" get-orphans 2>/dev/null || echo "none")

REVIEW_FILE=$(mktemp /tmp/dsp-review-XXXXXX.md)
cat > "$REVIEW_FILE" <<REVIEW_EOF
# DSP Consistency Review Request

## Git Diff

\`\`\`diff
$DIFF
\`\`\`

## DSP State for Affected Files

$DSP_CONTEXT

## Project Stats

$STATS

## Current Orphans

$ORPHANS

## Review Instructions

Check all items from the DSP consistency review checklist.
For each issue found, provide the exact dsp-cli command to fix it.
REVIEW_EOF

echo "Review context saved to: $REVIEW_FILE"
echo ""
echo "Send this to your agent for review:"
echo "  cat $REVIEW_FILE | pbcopy   # macOS"
echo "  cat $REVIEW_FILE | xclip    # Linux"
echo ""
echo "Or use directly with Claude Code:"
echo "  claude \"Review DSP consistency: \$(cat $REVIEW_FILE)\""
```

## File: `hooks/dsp-check-staged.ps1`
```powershell
#Requires -Version 5.1
[CmdletBinding()]
param(
    [string]$DspRoot = (git rev-parse --show-toplevel)
)

$ErrorActionPreference = 'Stop'

$dspCli = $null
$candidates = @(
    "$DspRoot\.cursor\skills\data-structure-protocol\scripts\dsp-cli.py",
    "$DspRoot\.claude\skills\data-structure-protocol\scripts\dsp-cli.py",
    "$DspRoot\.codex\skills\data-structure-protocol\scripts\dsp-cli.py",
    "$DspRoot\skills\data-structure-protocol\scripts\dsp-cli.py"
)

foreach ($c in $candidates) {
    if (Test-Path $c) {
        $dspCli = "python $c"
        break
    }
}

if (-not $dspCli) {
    Write-Host "[DSP] CLI not found." -ForegroundColor Red
    exit 1
}

if (-not (Test-Path "$DspRoot\.dsp")) {
    Write-Host "[DSP] No .dsp\ directory found." -ForegroundColor Red
    exit 1
}

$trackableExtensions = @('.ts', '.tsx', '.js', '.jsx', '.py', '.go', '.rs', '.java', '.rb', '.vue', '.svelte')
$issues = 0

Write-Host "[DSP] Checking staged files against DSP graph..."
Write-Host ""

$newFiles = (git diff --cached --name-only --diff-filter=ACMR) -split "`n" | Where-Object { $_.Trim() }
foreach ($file in $newFiles) {
    $ext = [System.IO.Path]::GetExtension($file)
    if ($ext -notin $trackableExtensions) { continue }

    $result = & cmd /c "$dspCli --root $DspRoot find-by-source `"$file`"" 2>$null
    if (-not $result) {
        Write-Host "[WARN] NEW/MODIFIED file not in DSP: $file" -ForegroundColor Yellow
        $issues++
    } else {
        Write-Host "[OK] $file" -ForegroundColor Green
    }
}

$deletedFiles = (git diff --cached --name-only --diff-filter=D) -split "`n" | Where-Object { $_.Trim() }
foreach ($file in $deletedFiles) {
    $result = & cmd /c "$dspCli --root $DspRoot find-by-source `"$file`"" 2>$null
    if ($result) {
        Write-Host "[ERR] DELETED file still in DSP: $file" -ForegroundColor Red
        $issues++
    }
}

$orphans = & cmd /c "$dspCli --root $DspRoot get-orphans" 2>$null
if ($orphans -and $orphans -notmatch "No orphans|0 orphan") {
    Write-Host ""
    Write-Host "[WARN] Orphaned DSP entities detected" -ForegroundColor Yellow
    $issues++
}

Write-Host ""
if ($issues -gt 0) {
    Write-Host "[DSP] Found $issues issue(s). Consider updating DSP before committing." -ForegroundColor Yellow
    exit 1
} else {
    Write-Host "[DSP] All staged files are consistent with DSP graph." -ForegroundColor Green
}
```

## File: `hooks/dsp-check-staged.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

DSP_ROOT="${DSP_ROOT:-$(git rev-parse --show-toplevel)}"

for candidate in \
  "$DSP_ROOT/.cursor/skills/data-structure-protocol/scripts/dsp-cli.py" \
  "$DSP_ROOT/.claude/skills/data-structure-protocol/scripts/dsp-cli.py" \
  "$DSP_ROOT/.codex/skills/data-structure-protocol/scripts/dsp-cli.py" \
  "$DSP_ROOT/skills/data-structure-protocol/scripts/dsp-cli.py"; do
  if [[ -f "$candidate" ]]; then
    DSP_CLI="python $candidate"
    break
  fi
done

DSP_CLI="${DSP_CLI:-}"
if [[ -z "$DSP_CLI" ]]; then
  echo "[DSP] CLI not found."
  exit 1
fi

if [[ ! -d "$DSP_ROOT/.dsp" ]]; then
  echo "[DSP] No .dsp/ directory found."
  exit 1
fi

SKIP_PATTERNS="${DSP_SKIP_PATTERNS:-*.md,*.txt,*.json,*.yml,*.yaml,*.lock,*.log}"
ISSUES=0

echo "[DSP] Checking staged files against DSP graph..."
echo ""

should_track() {
  local file="$1"
  for pattern in ${SKIP_PATTERNS//,/ }; do
    case "$file" in $pattern) return 1 ;; esac
  done
  [[ "$file" == *.ts || "$file" == *.tsx || "$file" == *.js || "$file" == *.jsx || \
     "$file" == *.py || "$file" == *.go || "$file" == *.rs || "$file" == *.java || \
     "$file" == *.rb || "$file" == *.vue || "$file" == *.svelte ]]
}

while IFS= read -r file; do
  [[ -z "$file" ]] && continue
  if should_track "$file"; then
    result=$($DSP_CLI --root "$DSP_ROOT" find-by-source "$file" 2>/dev/null || true)
    if [[ -z "$result" ]]; then
      echo "⚠ NEW/MODIFIED file not in DSP: $file"
      ((ISSUES++)) || true
    else
      echo "✓ $file"
    fi
  fi
done < <(git diff --cached --name-only --diff-filter=ACMR)

while IFS= read -r file; do
  [[ -z "$file" ]] && continue
  result=$($DSP_CLI --root "$DSP_ROOT" find-by-source "$file" 2>/dev/null || true)
  if [[ -n "$result" ]]; then
    echo "✗ DELETED file still in DSP: $file"
    ((ISSUES++)) || true
  fi
done < <(git diff --cached --name-only --diff-filter=D)

orphans=$($DSP_CLI --root "$DSP_ROOT" get-orphans 2>/dev/null || true)
if [[ -n "$orphans" && "$orphans" != *"No orphans"* && "$orphans" != *"0 orphan"* ]]; then
  echo ""
  echo "⚠ Orphaned DSP entities detected"
  ((ISSUES++)) || true
fi

echo ""
if [[ $ISSUES -gt 0 ]]; then
  echo "[DSP] Found $ISSUES issue(s). Consider updating DSP before committing."
  exit 1
else
  echo "[DSP] All staged files are consistent with DSP graph."
fi
```

## File: `hooks/install-hooks.ps1`
```powershell
#Requires -Version 5.1

$hooksDir = Join-Path (git rev-parse --git-dir) "hooks"
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "Installing DSP git hooks..."

Copy-Item (Join-Path $scriptDir "pre-commit") (Join-Path $hooksDir "pre-commit") -Force
Copy-Item (Join-Path $scriptDir "pre-push") (Join-Path $hooksDir "pre-push") -Force

Write-Host "[OK] DSP git hooks installed" -ForegroundColor Green
Write-Host ""
Write-Host "Configuration (environment variables):"
Write-Host "  DSP_PRECOMMIT_MODE=warn|block  (default: warn)"
Write-Host "  DSP_CLI=<path-to-dsp-cli.py>   (auto-detected)"
Write-Host "  DSP_SKIP_PATTERNS=<glob,...>    (files to skip)"
```

## File: `hooks/install-hooks.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

HOOKS_DIR="$(git rev-parse --git-dir)/hooks"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Installing DSP git hooks..."

cp "$SCRIPT_DIR/pre-commit" "$HOOKS_DIR/pre-commit"
chmod +x "$HOOKS_DIR/pre-commit"

cp "$SCRIPT_DIR/pre-push" "$HOOKS_DIR/pre-push"
chmod +x "$HOOKS_DIR/pre-push"

echo "✓ DSP git hooks installed"
echo ""
echo "Configuration (environment variables):"
echo "  DSP_PRECOMMIT_MODE=warn|block  (default: warn)"
echo "  DSP_CLI=<path-to-dsp-cli.py>   (auto-detected)"
echo "  DSP_SKIP_PATTERNS=<glob,...>    (files to skip, e.g. '*.md,*.txt')"
```

## File: `hooks/pre-commit`
```
#!/usr/bin/env bash
# DSP pre-commit hook — deterministic consistency check
set -euo pipefail

DSP_MODE="${DSP_PRECOMMIT_MODE:-warn}"
DSP_ROOT="$(git rev-parse --show-toplevel)"

for candidate in \
  "$DSP_ROOT/.cursor/skills/data-structure-protocol/scripts/dsp-cli.py" \
  "$DSP_ROOT/.claude/skills/data-structure-protocol/scripts/dsp-cli.py" \
  "$DSP_ROOT/.codex/skills/data-structure-protocol/scripts/dsp-cli.py" \
  "$DSP_ROOT/skills/data-structure-protocol/scripts/dsp-cli.py"; do
  if [[ -f "$candidate" ]]; then
    DSP_CLI="python $candidate"
    break
  fi
done

DSP_CLI="${DSP_CLI:-}"
if [[ -z "$DSP_CLI" ]]; then
  echo "[DSP] CLI not found. Skipping DSP check."
  exit 0
fi

if [[ ! -d "$DSP_ROOT/.dsp" ]]; then
  exit 0
fi

SKIP_PATTERNS="${DSP_SKIP_PATTERNS:-*.md,*.txt,*.json,*.yml,*.yaml,*.lock,*.log}"

WARNINGS=()
ERRORS=()

should_track() {
  local file="$1"
  for pattern in ${SKIP_PATTERNS//,/ }; do
    case "$file" in $pattern) return 1 ;; esac
  done
  [[ "$file" == *.ts || "$file" == *.tsx || "$file" == *.js || "$file" == *.jsx || \
     "$file" == *.py || "$file" == *.go || "$file" == *.rs || "$file" == *.java || \
     "$file" == *.rb || "$file" == *.vue || "$file" == *.svelte ]]
}

while IFS= read -r file; do
  [[ -z "$file" ]] && continue
  if should_track "$file"; then
    result=$($DSP_CLI --root "$DSP_ROOT" find-by-source "$file" 2>/dev/null || true)
    if [[ -z "$result" ]]; then
      WARNINGS+=("  NEW/MODIFIED file not in DSP: $file")
    fi
  fi
done < <(git diff --cached --name-only --diff-filter=ACMR)

while IFS= read -r file; do
  [[ -z "$file" ]] && continue
  result=$($DSP_CLI --root "$DSP_ROOT" find-by-source "$file" 2>/dev/null || true)
  if [[ -n "$result" ]]; then
    ERRORS+=("  DELETED file still in DSP: $file")
  fi
done < <(git diff --cached --name-only --diff-filter=D)

orphans=$($DSP_CLI --root "$DSP_ROOT" get-orphans 2>/dev/null || true)
if [[ -n "$orphans" && "$orphans" != *"No orphans"* && "$orphans" != *"0 orphan"* ]]; then
  WARNINGS+=("  Orphaned DSP entities detected. Run: dsp-cli get-orphans")
fi

if [[ ${#ERRORS[@]} -gt 0 || ${#WARNINGS[@]} -gt 0 ]]; then
  echo ""
  echo "[DSP] Consistency check results:"
  echo ""

  if [[ ${#ERRORS[@]} -gt 0 ]]; then
    echo "ERRORS (DSP graph is inconsistent):"
    printf '%s\n' "${ERRORS[@]}"
    echo ""
  fi

  if [[ ${#WARNINGS[@]} -gt 0 ]]; then
    echo "WARNINGS (DSP may need updating):"
    printf '%s\n' "${WARNINGS[@]}"
    echo ""
  fi

  if [[ "$DSP_MODE" == "block" && ${#ERRORS[@]} -gt 0 ]]; then
    echo "Commit blocked. Fix DSP errors first, or set DSP_PRECOMMIT_MODE=warn to allow."
    exit 1
  fi

  echo "Tip: Run './hooks/dsp-agent-review.sh' for deep agent-assisted review."
  echo ""
fi

exit 0
```

## File: `hooks/pre-push`
```
#!/usr/bin/env bash
# DSP pre-push hook — full graph integrity check
set -euo pipefail

DSP_ROOT="$(git rev-parse --show-toplevel)"

for candidate in \
  "$DSP_ROOT/.cursor/skills/data-structure-protocol/scripts/dsp-cli.py" \
  "$DSP_ROOT/.claude/skills/data-structure-protocol/scripts/dsp-cli.py" \
  "$DSP_ROOT/.codex/skills/data-structure-protocol/scripts/dsp-cli.py" \
  "$DSP_ROOT/skills/data-structure-protocol/scripts/dsp-cli.py"; do
  if [[ -f "$candidate" ]]; then
    DSP_CLI="python $candidate"
    break
  fi
done

DSP_CLI="${DSP_CLI:-}"
if [[ -z "$DSP_CLI" || ! -d "$DSP_ROOT/.dsp" ]]; then
  exit 0
fi

echo "[DSP] Running full graph integrity check before push..."

orphans=$($DSP_CLI --root "$DSP_ROOT" get-orphans 2>/dev/null || true)
if [[ -n "$orphans" && "$orphans" != *"No orphans"* && "$orphans" != *"0 orphan"* ]]; then
  echo "[DSP] WARNING: Orphaned entities found:"
  echo "$orphans"
fi

cycles=$($DSP_CLI --root "$DSP_ROOT" detect-cycles 2>/dev/null || true)
if [[ -n "$cycles" && "$cycles" != *"No cycles"* && "$cycles" != *"0 cycle"* ]]; then
  echo "[DSP] WARNING: Circular dependencies detected:"
  echo "$cycles"
fi

stats=$($DSP_CLI --root "$DSP_ROOT" get-stats 2>/dev/null || true)
echo "[DSP] Graph stats:"
echo "$stats"
echo ""

exit 0
```

## File: `integrations/claude/AGENTS.md`
```markdown
# Data Structure Protocol (DSP) — Agent Guidance

This project uses **DSP** — a graph-based structural memory stored in `.dsp/`. It tracks entities (objects, functions), their dependencies (imports), and public interfaces (shared/exports).

DSP lets you understand the codebase structure without reading every file.

## Core Rules

1. **Before modifying code** — look up affected entities via `search`, `find-by-source`, or `read-toc`
2. **When creating files** — register with `create-object` or `create-function`, then `add-import` for dependencies and `create-shared` for public APIs
3. **When deleting/moving** — use `remove-entity` or `move-entity`, clean up with `remove-import` / `remove-shared`
4. **Skip DSP updates** for internal-only changes: formatting, comments, private function body edits, dependency bumps

## Command Reference

| Command | Purpose | Example |
|---|---|---|
| `init` | Initialize `.dsp/` in project root | `dsp-cli init` |
| `read-toc` | List all root entities (table of contents) | `dsp-cli read-toc` |
| `search <query>` | Full-text search across entity descriptions | `dsp-cli search "auth"` |
| `find-by-source <path>` | Find entity by source file path | `dsp-cli find-by-source src/auth/login.ts` |
| `get-entity <uid>` | Get full entity details | `dsp-cli get-entity obj-a1b2c3d4` |
| `get-children <uid>` | List child entities | `dsp-cli get-children obj-a1b2c3d4` |
| `get-parents <uid>` | Find who imports this entity | `dsp-cli get-parents func-e5f6g7h8` |
| `get-recipients <uid>` | Find who consumes shared exports | `dsp-cli get-recipients obj-a1b2c3d4` |
| `get-stats` | Project-wide DSP statistics | `dsp-cli get-stats` |
| `get-orphans` | Find entities with broken references | `dsp-cli get-orphans` |
| `detect-cycles` | Find circular dependencies | `dsp-cli detect-cycles` |
| `create-object` | Register a module/class/component | `dsp-cli create-object --source src/auth/login.ts --purpose "Login page"` |
| `create-function` | Register a function entity | `dsp-cli create-function --source src/utils/hash.ts --purpose "Password hashing" --owner obj-a1b2c3d4` |
| `create-shared` | Declare a public API export | `dsp-cli create-shared <uid> <name>` |
| `add-import` | Record a dependency between entities | `dsp-cli add-import <uid> <target-uid> --why "uses auth service"` |
| `move-entity` | Update source path after file move | `dsp-cli move-entity <uid> --source new/path.ts` |
| `remove-entity` | Delete an entity from the graph | `dsp-cli remove-entity <uid>` |
| `remove-import` | Remove a dependency link | `dsp-cli remove-import <uid> <target-uid>` |
| `remove-shared` | Remove a public API export | `dsp-cli remove-shared <uid> <name>` |
| `update-description` | Update entity purpose/kind | `dsp-cli update-description <uid> --purpose "Updated purpose"` |
| `update-import-why` | Update the reason for a dependency | `dsp-cli update-import-why <uid> <target-uid> --why "new reason"` |

## Typical Workflow

```
1. read-toc                          → understand project structure
2. search "feature-area"             → find relevant entities
3. get-entity <uid>                  → read details + imports + shared
4. get-parents <uid>                 → impact analysis before changes
5. ... make code changes ...
6. create-object / create-function   → register new entities
7. add-import --why "..."            → record new dependencies
8. create-shared                     → expose public APIs
9. get-orphans                       → verify graph consistency
```

## What NOT to Update in DSP

- Formatting or whitespace changes
- Comment-only edits
- Private function body refactors (no signature change)
- Dependency version bumps in package.json/requirements.txt
- Config file tweaks (.env, .gitignore, CI config)
- Test file internals (unless test architecture changes)
```

## File: `integrations/claude/README.md`
```markdown
# Claude Code Integration Pack for DSP

Integration pack that connects [Data Structure Protocol](https://github.com/k-kolomeitsev/data-structure-protocol) with Claude Code via hooks and agent guidance.

## What's Included

| File | Purpose |
|---|---|
| `.claude/settings.json` | Hook configuration for SessionStart, PreToolUse, PostToolUse, SessionEnd |
| `hooks/dsp-session-start.sh` | Loads DSP summary at session start |
| `hooks/dsp-pre-write-check.sh` | Warns if a file being written isn't tracked in DSP |
| `hooks/dsp-track-write.sh` | Records written files for later sync |
| `hooks/dsp-session-end-check.sh` | Reminds to sync DSP before session ends |
| `AGENTS.md` | Standalone agent guidance (works without hooks) |
| `examples/` | Brownfield and greenfield workflow walkthroughs |

## Installation

### Full install (recommended)

Copy the `.claude/` directory and hooks to your project root:

```bash
# From the DSP repository
cp -r integrations/claude/.claude /path/to/your-project/
cp -r integrations/claude/hooks /path/to/your-project/.claude/

# Make hooks executable
chmod +x /path/to/your-project/.claude/hooks/dsp-*.sh
```

### Selective install

Pick only the hooks you need:

```bash
# Just session start/end (minimal awareness)
cp integrations/claude/hooks/dsp-session-start.sh /path/to/your-project/.claude/hooks/
cp integrations/claude/hooks/dsp-session-end-check.sh /path/to/your-project/.claude/hooks/
chmod +x /path/to/your-project/.claude/hooks/dsp-*.sh
```

Then add the corresponding entries to your `.claude/settings.json` — see the included `settings.json` for the full configuration.

### AGENTS.md only (zero config)

If you don't want hooks, copy `AGENTS.md` to your project root. Claude Code reads it automatically:

```bash
cp integrations/claude/AGENTS.md /path/to/your-project/AGENTS.md
```

## How Hooks Work

Claude Code hooks fire at specific lifecycle events. All DSP hooks are **non-blocking** (exit 0) and produce only stdout/stderr guidance for the agent.

```
Session Start ──→ dsp-session-start.sh ──→ prints DSP stats summary
       │
       ▼
  Agent works...
       │
  PreToolUse(Write/Edit) ──→ dsp-pre-write-check.sh ──→ warns if file untracked
       │
  PostToolUse(Write/Edit) ──→ dsp-track-write.sh ──→ records file to .dsp-touched
       │
       ▼
Session End ──→ dsp-session-end-check.sh ──→ reminds to sync, cleans up
```

## Requirements

- DSP skill installed (`.dsp/` directory initialized in your project)
- `python3` available in PATH
- `dsp-cli.py` discoverable (auto-detected from common locations)

## Hook Design Principles

- **Fast**: No network calls, no LLM invocations, pure filesystem operations
- **Deterministic**: Same input always produces the same output
- **Non-blocking**: Always exit 0 — hooks advise, never block
- **Auto-detect CLI**: Hooks search common paths for `dsp-cli.py` automatically
```

## File: `integrations/claude/examples/brownfield-workflow.md`
```markdown
# Brownfield Workflow — Adding a Feature with DSP (Claude Code)

A realistic walkthrough of using DSP when working on an existing codebase with Claude Code.

## Scenario

You have an e-commerce project with DSP already bootstrapped. The user asks Claude to add a "wishlist" feature.

## Step 1: Understand the Existing Structure

The user prompts Claude:

> Add a wishlist feature. Users should be able to save products and view their wishlist.

Claude starts by reading DSP:

```bash
dsp-cli read-toc
```

Output:

```
obj-1a2b3c4d  src/products/       Product catalog module
obj-5e6f7a8b  src/auth/           Authentication module
obj-9c0d1e2f  src/cart/           Shopping cart module
obj-3a4b5c6d  src/database/       Database layer
```

## Step 2: Find Related Entities

Claude searches for existing product and user-related entities:

```bash
dsp-cli search "product"
dsp-cli search "user"
```

Then inspects the product module for its public API:

```bash
dsp-cli get-entity obj-1a2b3c4d
dsp-cli get-children obj-1a2b3c4d
```

Output reveals `obj-1a2b3c4d` has a shared export `ProductService` and child functions like `getProductById`.

## Step 3: Check Impact Before Changes

Claude checks who depends on the product module:

```bash
dsp-cli get-parents obj-1a2b3c4d
dsp-cli get-recipients obj-1a2b3c4d
```

This shows `cart` module already imports from `products` — Claude can follow the same pattern.

## Step 4: Implement the Feature

Claude creates the wishlist module files:

- `src/wishlist/wishlist.service.ts`
- `src/wishlist/wishlist.controller.ts`
- `src/wishlist/wishlist.repository.ts`

## Step 5: Register New Entities in DSP

```bash
# Register the wishlist module
dsp-cli create-object \
  --source src/wishlist/ \
  --purpose "Wishlist module — save and manage favorite products per user"

# Output: obj-aa11bb22

# Register the service function
dsp-cli create-function \
  --source src/wishlist/wishlist.service.ts \
  --purpose "Wishlist business logic — add, remove, list saved products" \
  --owner obj-aa11bb22

# Output: func-cc33dd44
```

## Step 6: Record Dependencies

```bash
# Wishlist depends on ProductService
dsp-cli add-import obj-aa11bb22 obj-1a2b3c4d \
  --why "uses ProductService to validate product existence"

# Wishlist depends on Database layer
dsp-cli add-import obj-aa11bb22 obj-3a4b5c6d \
  --why "persists wishlist items"

# Wishlist depends on Auth module
dsp-cli add-import obj-aa11bb22 obj-5e6f7a8b \
  --why "authenticates user before wishlist operations"
```

## Step 7: Declare Public API

```bash
# Wishlist exposes WishlistService for use by other modules
dsp-cli create-shared obj-aa11bb22 WishlistService
```

## Step 8: Verify Consistency

```bash
dsp-cli get-orphans
dsp-cli get-stats
```

No orphans — the graph is consistent.

## Result

The DSP graph now reflects the new feature. Next time an agent works on this codebase, it will instantly know:

- The wishlist module exists and what it does
- It depends on products, auth, and database
- It exposes `WishlistService` as a public API
- Who else might be affected if wishlist changes
```

## File: `integrations/claude/examples/greenfield-workflow.md`
```markdown
# Greenfield Workflow — Starting a New Project with DSP (Claude Code)

A walkthrough of building a new project from scratch with DSP and Claude Code.

## Scenario

You're starting a new REST API for a task management app. You want DSP from day one so the agent always has structural awareness.

## Step 1: Initialize DSP

```bash
dsp-cli init
```

This creates the `.dsp/` directory in your project root.

## Step 2: Plan the Architecture

The user prompts Claude:

> Build a task management API with users, projects, and tasks. Use Express + TypeScript.

Claude plans the module structure first, then registers each module in DSP as it creates files.

## Step 3: Create and Register the Database Layer

Claude creates `src/database/connection.ts` and immediately registers it:

```bash
dsp-cli create-object \
  --source src/database/ \
  --purpose "Database connection and query layer (PostgreSQL)"

# Output: obj-db000001
```

## Step 4: Create Core Modules

For each module, Claude writes code and registers the DSP entity:

```bash
# Users module
dsp-cli create-object \
  --source src/users/ \
  --purpose "User management — registration, authentication, profiles"
# Output: obj-us000002

# Projects module
dsp-cli create-object \
  --source src/projects/ \
  --purpose "Project management — CRUD operations for projects"
# Output: obj-pj000003

# Tasks module
dsp-cli create-object \
  --source src/tasks/ \
  --purpose "Task management — create, assign, update, complete tasks"
# Output: obj-tk000004
```

## Step 5: Register Functions Within Modules

```bash
dsp-cli create-function \
  --source src/users/users.service.ts \
  --purpose "User business logic — signup, login, profile updates" \
  --owner obj-us000002
# Output: func-us000005

dsp-cli create-function \
  --source src/tasks/tasks.service.ts \
  --purpose "Task business logic — CRUD, assignment, status transitions" \
  --owner obj-tk000004
# Output: func-tk000006
```

## Step 6: Declare Dependencies

```bash
# Users → Database
dsp-cli add-import obj-us000002 obj-db000001 \
  --why "persists user records"

# Projects → Database + Users
dsp-cli add-import obj-pj000003 obj-db000001 \
  --why "persists project records"
dsp-cli add-import obj-pj000003 obj-us000002 \
  --why "validates project owner exists"

# Tasks → Database + Projects + Users
dsp-cli add-import obj-tk000004 obj-db000001 \
  --why "persists task records"
dsp-cli add-import obj-tk000004 obj-pj000003 \
  --why "tasks belong to projects"
dsp-cli add-import obj-tk000004 obj-us000002 \
  --why "tasks are assigned to users"
```

## Step 7: Declare Public APIs

```bash
dsp-cli create-shared obj-us000002 UserService
dsp-cli create-shared obj-pj000003 ProjectService
dsp-cli create-shared obj-tk000004 TaskService
dsp-cli create-shared obj-db000001 DatabasePool
```

## Step 8: Verify the Graph

```bash
dsp-cli get-stats
```

```
entities: 6
objects: 4
functions: 2
imports: 6
shared: 4
orphans: 0
cycles: 0
```

```bash
dsp-cli read-toc
```

```
obj-db000001  src/database/    Database connection and query layer (PostgreSQL)
obj-us000002  src/users/       User management — registration, authentication, profiles
obj-pj000003  src/projects/    Project management — CRUD operations for projects
obj-tk000004  src/tasks/       Task management — create, assign, update, complete tasks
```

## Result

From the very first commit, the project has a complete structural memory. Any agent that opens this project will immediately understand:

- What modules exist and their purpose
- How they depend on each other and why
- What public APIs are available
- The project is clean — no orphans, no cycles

As the project grows, DSP grows with it. The agent never has to re-discover the architecture from scratch.
```

## File: `integrations/claude/hooks/dsp-pre-write-check.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

find_dsp_cli() {
  local candidates=(
    ".cursor/skills/data-structure-protocol/scripts/dsp-cli.py"
    ".claude/skills/data-structure-protocol/scripts/dsp-cli.py"
    ".codex/skills/data-structure-protocol/scripts/dsp-cli.py"
    "skills/data-structure-protocol/scripts/dsp-cli.py"
  )
  for c in "${candidates[@]}"; do
    if [[ -f "$c" ]]; then
      echo "$c"
      return 0
    fi
  done
  return 1
}

if [[ ! -d ".dsp" ]]; then
  exit 0
fi

DSP_CLI="${DSP_CLI:-}"
if [[ -z "$DSP_CLI" ]]; then
  DSP_CLI=$(find_dsp_cli) || exit 0
fi

PYTHON="${PYTHON:-python3}"
command -v "$PYTHON" &>/dev/null || PYTHON="python"
command -v "$PYTHON" &>/dev/null || exit 0

input=$(cat)
file_path=$(echo "$input" | "$PYTHON" -c "import sys,json; print(json.load(sys.stdin).get('file_path',''))" 2>/dev/null) || exit 0

if [[ -z "$file_path" ]]; then
  exit 0
fi

result=$("$PYTHON" "$DSP_CLI" --root . find-by-source "$file_path" 2>/dev/null) || exit 0

if [[ -z "$result" ]]; then
  echo "[DSP] Warning: '$file_path' is not tracked in DSP."
  echo "[DSP] Consider registering it with create-object or create-function after writing."
fi

exit 0
```

## File: `integrations/claude/hooks/dsp-session-end-check.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

TOUCHED_FILE=".dsp-touched"

if [[ ! -d ".dsp" ]]; then
  rm -f "$TOUCHED_FILE"
  exit 0
fi

if [[ ! -f "$TOUCHED_FILE" ]]; then
  exit 0
fi

count=$(wc -l < "$TOUCHED_FILE" | tr -d ' ')

if [[ "$count" -gt 0 ]]; then
  echo "[DSP] $count file(s) were modified during this session:"
  head -20 "$TOUCHED_FILE" | sed 's/^/  /'
  if [[ "$count" -gt 20 ]]; then
    echo "  ... and $((count - 20)) more"
  fi
  echo ""
  echo "[DSP] Reminder: run 'dsp-cli get-orphans' to check for unregistered entities."
  echo "[DSP] Run 'dsp-cli find-by-source <file>' on modified files to verify DSP is up to date."
fi

rm -f "$TOUCHED_FILE"

exit 0
```

## File: `integrations/claude/hooks/dsp-session-start.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

find_dsp_cli() {
  local candidates=(
    ".cursor/skills/data-structure-protocol/scripts/dsp-cli.py"
    ".claude/skills/data-structure-protocol/scripts/dsp-cli.py"
    ".codex/skills/data-structure-protocol/scripts/dsp-cli.py"
    "skills/data-structure-protocol/scripts/dsp-cli.py"
  )
  for c in "${candidates[@]}"; do
    if [[ -f "$c" ]]; then
      echo "$c"
      return 0
    fi
  done
  return 1
}

if [[ ! -d ".dsp" ]]; then
  exit 0
fi

DSP_CLI="${DSP_CLI:-}"
if [[ -z "$DSP_CLI" ]]; then
  DSP_CLI=$(find_dsp_cli) || exit 0
fi

PYTHON="${PYTHON:-python3}"
command -v "$PYTHON" &>/dev/null || PYTHON="python"
command -v "$PYTHON" &>/dev/null || exit 0

stats=$("$PYTHON" "$DSP_CLI" --root . get-stats 2>/dev/null) || exit 0

echo "[DSP] Structural memory loaded."
echo "$stats"

exit 0
```

## File: `integrations/claude/hooks/dsp-track-write.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

if [[ ! -d ".dsp" ]]; then
  exit 0
fi

PYTHON="${PYTHON:-python3}"
command -v "$PYTHON" &>/dev/null || PYTHON="python"
command -v "$PYTHON" &>/dev/null || exit 0

input=$(cat)
file_path=$(echo "$input" | "$PYTHON" -c "import sys,json; print(json.load(sys.stdin).get('file_path',''))" 2>/dev/null) || exit 0

if [[ -z "$file_path" ]]; then
  exit 0
fi

TOUCHED_FILE=".dsp-touched"

if [[ -f "$TOUCHED_FILE" ]]; then
  if grep -qxF "$file_path" "$TOUCHED_FILE" 2>/dev/null; then
    exit 0
  fi
fi

echo "$file_path" >> "$TOUCHED_FILE"

exit 0
```

## File: `integrations/codex/AGENTS.md`
```markdown
# Data Structure Protocol (DSP) — Agent Guidance

This project uses **DSP** — a graph-based structural memory stored in `.dsp/`. It tracks entities (objects, functions), their dependencies (imports), and public interfaces (shared/exports).

DSP lets you understand the codebase structure without reading every file.

## Core Rules

1. **Before modifying code** — look up affected entities via `search`, `find-by-source`, or `read-toc`
2. **When creating files** — register with `create-object` or `create-function`, then `add-import` for dependencies and `create-shared` for public APIs
3. **When deleting/moving** — use `remove-entity` or `move-entity`, clean up with `remove-import` / `remove-shared`
4. **Skip DSP updates** for internal-only changes: formatting, comments, private function body edits, dependency bumps

## Command Reference

| Command | Purpose | Example |
|---|---|---|
| `init` | Initialize `.dsp/` in project root | `dsp-cli init` |
| `read-toc` | List all root entities (table of contents) | `dsp-cli read-toc` |
| `search <query>` | Full-text search across entity descriptions | `dsp-cli search "auth"` |
| `find-by-source <path>` | Find entity by source file path | `dsp-cli find-by-source src/auth/login.ts` |
| `get-entity <uid>` | Get full entity details | `dsp-cli get-entity obj-a1b2c3d4` |
| `get-children <uid>` | List child entities | `dsp-cli get-children obj-a1b2c3d4` |
| `get-parents <uid>` | Find who imports this entity | `dsp-cli get-parents func-e5f6g7h8` |
| `get-recipients <uid>` | Find who consumes shared exports | `dsp-cli get-recipients obj-a1b2c3d4` |
| `get-stats` | Project-wide DSP statistics | `dsp-cli get-stats` |
| `get-orphans` | Find entities with broken references | `dsp-cli get-orphans` |
| `detect-cycles` | Find circular dependencies | `dsp-cli detect-cycles` |
| `create-object` | Register a module/class/component | `dsp-cli create-object --source src/auth/login.ts --purpose "Login page"` |
| `create-function` | Register a function entity | `dsp-cli create-function --source src/utils/hash.ts --purpose "Password hashing" --owner obj-a1b2c3d4` |
| `create-shared` | Declare a public API export | `dsp-cli create-shared <uid> <name>` |
| `add-import` | Record a dependency between entities | `dsp-cli add-import <uid> <target-uid> --why "uses auth service"` |
| `move-entity` | Update source path after file move | `dsp-cli move-entity <uid> --source new/path.ts` |
| `remove-entity` | Delete an entity from the graph | `dsp-cli remove-entity <uid>` |
| `remove-import` | Remove a dependency link | `dsp-cli remove-import <uid> <target-uid>` |
| `remove-shared` | Remove a public API export | `dsp-cli remove-shared <uid> <name>` |
| `update-description` | Update entity purpose/kind | `dsp-cli update-description <uid> --purpose "Updated purpose"` |
| `update-import-why` | Update the reason for a dependency | `dsp-cli update-import-why <uid> <target-uid> --why "new reason"` |

## Typical Workflow

```
1. read-toc                          → understand project structure
2. search "feature-area"             → find relevant entities
3. get-entity <uid>                  → read details + imports + shared
4. get-parents <uid>                 → impact analysis before changes
5. ... make code changes ...
6. create-object / create-function   → register new entities
7. add-import --why "..."            → record new dependencies
8. create-shared                     → expose public APIs
9. get-orphans                       → verify graph consistency
```

## What NOT to Update in DSP

- Formatting or whitespace changes
- Comment-only edits
- Private function body refactors (no signature change)
- Dependency version bumps in package.json/requirements.txt
- Config file tweaks (.env, .gitignore, CI config)
- Test file internals (unless test architecture changes)
```

## File: `integrations/codex/README.md`
```markdown
# Codex Integration Pack for DSP

Integration pack that connects [Data Structure Protocol](https://github.com/k-kolomeitsev/data-structure-protocol) with OpenAI Codex.

## How Codex Discovers DSP

Codex automatically discovers skills from `.codex/skills/`. When the DSP skill is installed, Codex reads the `SKILL.md` file and gains access to `dsp-cli.py` for structural memory operations.

## Installation

### Via install script (recommended)

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.sh | bash -s -- codex

# Windows (PowerShell)
irm https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.ps1 | iex
```

### Via Codex skill-installer

If you have the Codex skill-installer available:

```
$skill-installer install https://github.com/k-kolomeitsev/data-structure-protocol/tree/main/skills/data-structure-protocol
```

### Manual installation

```bash
# Clone the repository
git clone https://github.com/k-kolomeitsev/data-structure-protocol.git /tmp/dsp

# Copy the skill
mkdir -p .codex/skills/data-structure-protocol
cp -r /tmp/dsp/skills/data-structure-protocol/* .codex/skills/data-structure-protocol/

# Clean up
rm -rf /tmp/dsp
```

## What's Included

| File | Purpose |
|---|---|
| `AGENTS.md` | Standalone agent guidance — works with any agent, including Codex |
| `examples/brownfield-workflow.md` | Step-by-step workflow for existing projects |
| `examples/greenfield-workflow.md` | Step-by-step workflow for new projects |

## Additional Setup

### AGENTS.md (optional fallback)

Copy `AGENTS.md` to your project root for guidance that works even without the DSP skill installed:

```bash
cp integrations/codex/AGENTS.md /path/to/your-project/AGENTS.md
```

### Initialize DSP

After installing the skill, initialize DSP in your project:

```bash
dsp-cli init
```

## Requirements

- Codex with skill support (`.codex/skills/` discovery)
- `python3` available in PATH
- DSP initialized (`.dsp/` directory) in your project
```

## File: `integrations/codex/examples/brownfield-workflow.md`
```markdown
# Brownfield Workflow — Adding a Feature with DSP (Codex)

A realistic walkthrough of using DSP when working on an existing codebase with OpenAI Codex.

## Scenario

You have an e-commerce project with DSP already bootstrapped. You ask Codex to add a "wishlist" feature.

## Prerequisites

- DSP skill installed in `.codex/skills/data-structure-protocol/`
- DSP initialized (`.dsp/` exists with registered entities)

## Step 1: Understand the Existing Structure

You prompt Codex:

> Add a wishlist feature. Users should be able to save products and view their wishlist.

Codex uses the DSP skill to understand the project first:

```bash
dsp-cli read-toc
```

Output:

```
obj-1a2b3c4d  src/products/       Product catalog module
obj-5e6f7a8b  src/auth/           Authentication module
obj-9c0d1e2f  src/cart/           Shopping cart module
obj-3a4b5c6d  src/database/       Database layer
```

## Step 2: Find Related Entities

Codex searches for product and user-related entities:

```bash
dsp-cli search "product"
dsp-cli search "user"
```

Then inspects the product module for its public API:

```bash
dsp-cli get-entity obj-1a2b3c4d
dsp-cli get-children obj-1a2b3c4d
```

This reveals `obj-1a2b3c4d` has a shared export `ProductService` and child functions like `getProductById`.

## Step 3: Check Impact Before Changes

Codex checks who depends on the product module:

```bash
dsp-cli get-parents obj-1a2b3c4d
dsp-cli get-recipients obj-1a2b3c4d
```

The cart module already imports from products — Codex follows the same pattern for the wishlist.

## Step 4: Implement the Feature

Codex creates the wishlist module files:

- `src/wishlist/wishlist.service.ts`
- `src/wishlist/wishlist.controller.ts`
- `src/wishlist/wishlist.repository.ts`

## Step 5: Register New Entities in DSP

```bash
dsp-cli create-object \
  --source src/wishlist/ \
  --purpose "Wishlist module — save and manage favorite products per user"
# Output: obj-aa11bb22

dsp-cli create-function \
  --source src/wishlist/wishlist.service.ts \
  --purpose "Wishlist business logic — add, remove, list saved products" \
  --owner obj-aa11bb22
# Output: func-cc33dd44
```

## Step 6: Record Dependencies

```bash
dsp-cli add-import obj-aa11bb22 obj-1a2b3c4d \
  --why "uses ProductService to validate product existence"

dsp-cli add-import obj-aa11bb22 obj-3a4b5c6d \
  --why "persists wishlist items"

dsp-cli add-import obj-aa11bb22 obj-5e6f7a8b \
  --why "authenticates user before wishlist operations"
```

## Step 7: Declare Public API

```bash
dsp-cli create-shared obj-aa11bb22 WishlistService
```

## Step 8: Verify Consistency

```bash
dsp-cli get-orphans
dsp-cli get-stats
```

No orphans — the graph is consistent.

## Result

Codex used DSP to understand the existing architecture before writing code, then kept the graph up to date with the new feature. On the next task, Codex will instantly know the wishlist exists, what it does, and how it connects to other modules.
```

## File: `integrations/codex/examples/greenfield-workflow.md`
```markdown
# Greenfield Workflow — Starting a New Project with DSP (Codex)

A walkthrough of building a new project from scratch with DSP and OpenAI Codex.

## Scenario

You're starting a new REST API for a task management app. You want DSP from day one so Codex always has structural awareness.

## Prerequisites

- DSP skill installed in `.codex/skills/data-structure-protocol/`

## Step 1: Initialize DSP

```bash
dsp-cli init
```

This creates the `.dsp/` directory in your project root.

## Step 2: Plan the Architecture

You prompt Codex:

> Build a task management API with users, projects, and tasks. Use Express + TypeScript.

Codex uses the DSP skill to plan the module structure and register entities as it creates files.

## Step 3: Create and Register the Database Layer

Codex creates `src/database/connection.ts` and registers it:

```bash
dsp-cli create-object \
  --source src/database/ \
  --purpose "Database connection and query layer (PostgreSQL)"
# Output: obj-db000001
```

## Step 4: Create Core Modules

For each module, Codex writes code and registers the DSP entity:

```bash
dsp-cli create-object \
  --source src/users/ \
  --purpose "User management — registration, authentication, profiles"
# Output: obj-us000002

dsp-cli create-object \
  --source src/projects/ \
  --purpose "Project management — CRUD operations for projects"
# Output: obj-pj000003

dsp-cli create-object \
  --source src/tasks/ \
  --purpose "Task management — create, assign, update, complete tasks"
# Output: obj-tk000004
```

## Step 5: Register Functions Within Modules

```bash
dsp-cli create-function \
  --source src/users/users.service.ts \
  --purpose "User business logic — signup, login, profile updates" \
  --owner obj-us000002
# Output: func-us000005

dsp-cli create-function \
  --source src/tasks/tasks.service.ts \
  --purpose "Task business logic — CRUD, assignment, status transitions" \
  --owner obj-tk000004
# Output: func-tk000006
```

## Step 6: Declare Dependencies

```bash
dsp-cli add-import obj-us000002 obj-db000001 \
  --why "persists user records"

dsp-cli add-import obj-pj000003 obj-db000001 \
  --why "persists project records"
dsp-cli add-import obj-pj000003 obj-us000002 \
  --why "validates project owner exists"

dsp-cli add-import obj-tk000004 obj-db000001 \
  --why "persists task records"
dsp-cli add-import obj-tk000004 obj-pj000003 \
  --why "tasks belong to projects"
dsp-cli add-import obj-tk000004 obj-us000002 \
  --why "tasks are assigned to users"
```

## Step 7: Declare Public APIs

```bash
dsp-cli create-shared obj-us000002 UserService
dsp-cli create-shared obj-pj000003 ProjectService
dsp-cli create-shared obj-tk000004 TaskService
dsp-cli create-shared obj-db000001 DatabasePool
```

## Step 8: Verify the Graph

```bash
dsp-cli get-stats
```

```
entities: 6
objects: 4
functions: 2
imports: 6
shared: 4
orphans: 0
cycles: 0
```

```bash
dsp-cli read-toc
```

```
obj-db000001  src/database/    Database connection and query layer (PostgreSQL)
obj-us000002  src/users/       User management — registration, authentication, profiles
obj-pj000003  src/projects/    Project management — CRUD operations for projects
obj-tk000004  src/tasks/       Task management — create, assign, update, complete tasks
```

## Result

From the first commit, the project has a complete structural memory. Codex will never need to re-read the entire codebase to understand the architecture. As the project grows, DSP grows with it — each new module and dependency is tracked in the graph.
```

## File: `integrations/cursor/AGENTS.md`
```markdown
# Data Structure Protocol (DSP) — Agent Guidance

This project uses **DSP** — a graph-based structural memory stored in `.dsp/`. It tracks entities (objects, functions), their dependencies (imports), and public interfaces (shared/exports).

DSP lets you understand the codebase structure without reading every file.

## Core Rules

1. **Before modifying code** — look up affected entities via `search`, `find-by-source`, or `read-toc`
2. **When creating files** — register with `create-object` or `create-function`, then `add-import` for dependencies and `create-shared` for public APIs
3. **When deleting/moving** — use `remove-entity` or `move-entity`, clean up with `remove-import` / `remove-shared`
4. **Skip DSP updates** for internal-only changes: formatting, comments, private function body edits, dependency bumps

## Command Reference

| Command | Purpose | Example |
|---|---|---|
| `init` | Initialize `.dsp/` in project root | `dsp-cli init` |
| `read-toc` | List all root entities (table of contents) | `dsp-cli read-toc` |
| `search <query>` | Full-text search across entity descriptions | `dsp-cli search "auth"` |
| `find-by-source <path>` | Find entity by source file path | `dsp-cli find-by-source src/auth/login.ts` |
| `get-entity <uid>` | Get full entity details | `dsp-cli get-entity obj-a1b2c3d4` |
| `get-children <uid>` | List child entities | `dsp-cli get-children obj-a1b2c3d4` |
| `get-parents <uid>` | Find who imports this entity | `dsp-cli get-parents func-e5f6g7h8` |
| `get-recipients <uid>` | Find who consumes shared exports | `dsp-cli get-recipients obj-a1b2c3d4` |
| `get-stats` | Project-wide DSP statistics | `dsp-cli get-stats` |
| `get-orphans` | Find entities with broken references | `dsp-cli get-orphans` |
| `detect-cycles` | Find circular dependencies | `dsp-cli detect-cycles` |
| `create-object` | Register a module/class/component | `dsp-cli create-object --source src/auth/login.ts --purpose "Login page"` |
| `create-function` | Register a function entity | `dsp-cli create-function --source src/utils/hash.ts --purpose "Password hashing" --owner obj-a1b2c3d4` |
| `create-shared` | Declare a public API export | `dsp-cli create-shared <uid> <name>` |
| `add-import` | Record a dependency between entities | `dsp-cli add-import <uid> <target-uid> --why "uses auth service"` |
| `move-entity` | Update source path after file move | `dsp-cli move-entity <uid> --source new/path.ts` |
| `remove-entity` | Delete an entity from the graph | `dsp-cli remove-entity <uid>` |
| `remove-import` | Remove a dependency link | `dsp-cli remove-import <uid> <target-uid>` |
| `remove-shared` | Remove a public API export | `dsp-cli remove-shared <uid> <name>` |
| `update-description` | Update entity purpose/kind | `dsp-cli update-description <uid> --purpose "Updated purpose"` |
| `update-import-why` | Update the reason for a dependency | `dsp-cli update-import-why <uid> <target-uid> --why "new reason"` |

## Typical Workflow

```
1. read-toc                          → understand project structure
2. search "feature-area"             → find relevant entities
3. get-entity <uid>                  → read details + imports + shared
4. get-parents <uid>                 → impact analysis before changes
5. ... make code changes ...
6. create-object / create-function   → register new entities
7. add-import --why "..."            → record new dependencies
8. create-shared                     → expose public APIs
9. get-orphans                       → verify graph consistency
```

## What NOT to Update in DSP

- Formatting or whitespace changes
- Comment-only edits
- Private function body refactors (no signature change)
- Dependency version bumps in package.json/requirements.txt
- Config file tweaks (.env, .gitignore, CI config)
- Test file internals (unless test architecture changes)
```

## File: `integrations/cursor/README.md`
```markdown
# Cursor Integration Pack for DSP

Integration pack that connects [Data Structure Protocol](https://github.com/k-kolomeitsev/data-structure-protocol) with Cursor via rules (.mdc files) and optional hooks.

## What's Included

| File | Type | Purpose |
|---|---|---|
| `.cursor/rules/dsp-core.mdc` | Always active | Core DSP awareness — read before modify, update after changes |
| `.cursor/rules/dsp-brownfield.mdc` | Manual trigger | Brownfield workflow guide for existing projects |
| `.cursor/rules/dsp-new-file.mdc` | Auto on new files | Register new source files in DSP |
| `.cursor/rules/dsp-refactor-safety.mdc` | Manual trigger | Impact analysis before refactoring |
| `.cursor/rules/dsp-public-api-changes.mdc` | Manual trigger | Update shared/exports on public API changes |
| `.cursor/rules/dsp-when-not-to-update.mdc` | Always active | Skip DSP for internal-only changes |
| `AGENTS.md` | Standalone guidance | Works without rules for any agent |
| `examples/` | Walkthroughs | Brownfield and greenfield workflow examples |

## Installation

### Full install (recommended)

Copy the `.cursor/rules/` directory to your project:

```bash
# From the DSP repository
cp -r integrations/cursor/.cursor/rules/ /path/to/your-project/.cursor/rules/
```

Or on Windows (PowerShell):

```powershell
Copy-Item -Recurse integrations\cursor\.cursor\rules\ \path\to\your-project\.cursor\rules\
```

If you already have `.cursor/rules/`, the DSP rule files won't conflict — they use the `dsp-` prefix.

### Selective install

Copy only the rules you need. At minimum, install these two:

- `dsp-core.mdc` — core awareness (always active)
- `dsp-when-not-to-update.mdc` — prevents unnecessary DSP updates

### AGENTS.md only (zero config)

Copy `AGENTS.md` to your project root for lightweight agent guidance:

```bash
cp integrations/cursor/AGENTS.md /path/to/your-project/AGENTS.md
```

## Hooks via Third-Party Hooks

Cursor supports Claude Code hooks through the **Third-party hooks** feature. This means the Claude integration hooks work in Cursor too.

### Enabling Third-Party Hooks

1. Open Cursor Settings
2. Go to **Features**
3. Enable **Third-party hooks**
4. Copy `.claude/settings.json` from the Claude integration pack to your project

```bash
cp -r integrations/claude/.claude /path/to/your-project/
cp -r integrations/claude/hooks /path/to/your-project/.claude/
chmod +x /path/to/your-project/.claude/hooks/dsp-*.sh
```

This gives you the same hook-based DSP awareness as Claude Code — session start summary, write tracking, and session end reminders.

## How Rules Work

Cursor rules provide contextual guidance to the AI agent:

- **Always active** rules are injected into every conversation
- **Auto-trigger** rules activate when matching files are created or edited
- **Manual trigger** rules are available for the agent to reference when relevant

The DSP rules teach the agent to consult `.dsp/` before making changes and to keep the graph up to date after changes.

## Requirements

- DSP skill installed (`.dsp/` directory initialized in your project)
- `python3` available in PATH (or `python` on Windows)
- `dsp-cli.py` discoverable from a standard skill location
```

## File: `integrations/cursor/examples/brownfield-workflow.md`
```markdown
# Brownfield Workflow — Adding a Feature with DSP (Cursor)

A realistic walkthrough of using DSP when working on an existing codebase with Cursor.

## Scenario

You have an e-commerce project with DSP already bootstrapped. You ask the Cursor agent to add a "wishlist" feature.

## Prerequisites

- DSP skill installed in `.cursor/skills/data-structure-protocol/`
- DSP initialized (`.dsp/` exists with registered entities)
- DSP Cursor rules installed in `.cursor/rules/` (optional but recommended)

## Step 1: Understand the Existing Structure

You prompt the agent:

> Add a wishlist feature. Users should be able to save products and view their wishlist.

With `dsp-core.mdc` active, the agent automatically consults DSP first:

```bash
dsp-cli read-toc
```

Output:

```
obj-1a2b3c4d  src/products/       Product catalog module
obj-5e6f7a8b  src/auth/           Authentication module
obj-9c0d1e2f  src/cart/           Shopping cart module
obj-3a4b5c6d  src/database/       Database layer
```

## Step 2: Find Related Entities

The agent searches for product and user-related entities:

```bash
dsp-cli search "product"
dsp-cli search "user"
```

Then inspects the product module for its public API:

```bash
dsp-cli get-entity obj-1a2b3c4d
dsp-cli get-children obj-1a2b3c4d
```

This reveals `obj-1a2b3c4d` has a shared export `ProductService` and child functions like `getProductById`.

## Step 3: Check Impact Before Changes

The agent checks who depends on the product module:

```bash
dsp-cli get-parents obj-1a2b3c4d
dsp-cli get-recipients obj-1a2b3c4d
```

The cart module already imports from products — the agent follows the same pattern for the wishlist.

## Step 4: Implement the Feature

The agent creates the wishlist module files:

- `src/wishlist/wishlist.service.ts`
- `src/wishlist/wishlist.controller.ts`
- `src/wishlist/wishlist.repository.ts`

With `dsp-new-file.mdc` active, the agent is prompted to register each new file.

## Step 5: Register New Entities in DSP

```bash
dsp-cli create-object \
  --source src/wishlist/ \
  --purpose "Wishlist module — save and manage favorite products per user"
# Output: obj-aa11bb22

dsp-cli create-function \
  --source src/wishlist/wishlist.service.ts \
  --purpose "Wishlist business logic — add, remove, list saved products" \
  --owner obj-aa11bb22
# Output: func-cc33dd44
```

## Step 6: Record Dependencies

```bash
dsp-cli add-import obj-aa11bb22 obj-1a2b3c4d \
  --why "uses ProductService to validate product existence"

dsp-cli add-import obj-aa11bb22 obj-3a4b5c6d \
  --why "persists wishlist items"

dsp-cli add-import obj-aa11bb22 obj-5e6f7a8b \
  --why "authenticates user before wishlist operations"
```

## Step 7: Declare Public API

```bash
dsp-cli create-shared obj-aa11bb22 WishlistService
```

## Step 8: Verify Consistency

```bash
dsp-cli get-orphans
dsp-cli get-stats
```

No orphans — the graph is consistent.

## Result

Thanks to DSP Cursor rules, the agent followed the read-before-modify → implement → register → verify cycle automatically. The wishlist feature is fully tracked in the structural graph for future sessions.
```

## File: `integrations/cursor/examples/greenfield-workflow.md`
```markdown
# Greenfield Workflow — Starting a New Project with DSP (Cursor)

A walkthrough of building a new project from scratch with DSP and Cursor.

## Scenario

You're starting a new REST API for a task management app. You want DSP from day one so the agent always has structural awareness.

## Prerequisites

- DSP skill installed in `.cursor/skills/data-structure-protocol/`
- DSP Cursor rules installed in `.cursor/rules/` (optional but recommended)

## Step 1: Initialize DSP

```bash
dsp-cli init
```

This creates the `.dsp/` directory in your project root.

## Step 2: Plan the Architecture

You prompt the agent:

> Build a task management API with users, projects, and tasks. Use Express + TypeScript.

With `dsp-core.mdc` active, the agent plans the module structure and registers entities as it creates files.

## Step 3: Create and Register the Database Layer

The agent creates `src/database/connection.ts` and registers it:

```bash
dsp-cli create-object \
  --source src/database/ \
  --purpose "Database connection and query layer (PostgreSQL)"
# Output: obj-db000001
```

## Step 4: Create Core Modules

With `dsp-new-file.mdc` triggering on each new source file, the agent registers modules as it goes:

```bash
dsp-cli create-object \
  --source src/users/ \
  --purpose "User management — registration, authentication, profiles"
# Output: obj-us000002

dsp-cli create-object \
  --source src/projects/ \
  --purpose "Project management — CRUD operations for projects"
# Output: obj-pj000003

dsp-cli create-object \
  --source src/tasks/ \
  --purpose "Task management — create, assign, update, complete tasks"
# Output: obj-tk000004
```

## Step 5: Register Functions Within Modules

```bash
dsp-cli create-function \
  --source src/users/users.service.ts \
  --purpose "User business logic — signup, login, profile updates" \
  --owner obj-us000002
# Output: func-us000005

dsp-cli create-function \
  --source src/tasks/tasks.service.ts \
  --purpose "Task business logic — CRUD, assignment, status transitions" \
  --owner obj-tk000004
# Output: func-tk000006
```

## Step 6: Declare Dependencies

```bash
dsp-cli add-import obj-us000002 obj-db000001 \
  --why "persists user records"

dsp-cli add-import obj-pj000003 obj-db000001 \
  --why "persists project records"
dsp-cli add-import obj-pj000003 obj-us000002 \
  --why "validates project owner exists"

dsp-cli add-import obj-tk000004 obj-db000001 \
  --why "persists task records"
dsp-cli add-import obj-tk000004 obj-pj000003 \
  --why "tasks belong to projects"
dsp-cli add-import obj-tk000004 obj-us000002 \
  --why "tasks are assigned to users"
```

## Step 7: Declare Public APIs

```bash
dsp-cli create-shared obj-us000002 UserService
dsp-cli create-shared obj-pj000003 ProjectService
dsp-cli create-shared obj-tk000004 TaskService
dsp-cli create-shared obj-db000001 DatabasePool
```

## Step 8: Verify the Graph

```bash
dsp-cli get-stats
```

```
entities: 6
objects: 4
functions: 2
imports: 6
shared: 4
orphans: 0
cycles: 0
```

```bash
dsp-cli read-toc
```

```
obj-db000001  src/database/    Database connection and query layer (PostgreSQL)
obj-us000002  src/users/       User management — registration, authentication, profiles
obj-pj000003  src/projects/    Project management — CRUD operations for projects
obj-tk000004  src/tasks/       Task management — create, assign, update, complete tasks
```

## Result

From the first commit, the project has a complete structural memory. Cursor's DSP rules ensure the agent consults the graph before changes and registers entities as it creates them. New sessions start with full architectural awareness — no re-discovery needed.
```

## File: `skills/data-structure-protocol/LICENSE`
```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

1.  Definitions.

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

2.  Grant of Copyright License. Subject to the terms and conditions of
    this License, each Contributor hereby grants to You a perpetual,
    worldwide, non-exclusive, no-charge, royalty-free, irrevocable
    copyright license to reproduce, prepare Derivative Works of,
    publicly display, publicly perform, sublicense, and distribute the
    Work and such Derivative Works in Source or Object form.

3.  Grant of Patent License. Subject to the terms and conditions of
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

4.  Redistribution. You may reproduce and distribute copies of the
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

5.  Submission of Contributions. Unless You explicitly state otherwise,
    any Contribution intentionally submitted for inclusion in the Work
    by You to the Licensor shall be under the terms and conditions of
    this License, without any additional terms or conditions.
    Notwithstanding the above, nothing herein shall supersede or modify
    the terms of any separate license agreement you may have executed
    with Licensor regarding such Contributions.

6.  Trademarks. This License does not grant permission to use the trade
    names, trademarks, service marks, or product names of the Licensor,
    except as required for reasonable and customary use in describing the
    origin of the Work and reproducing the content of the NOTICE file.

7.  Disclaimer of Warranty. Unless required by applicable law or
    agreed to in writing, Licensor provides the Work (and each
    Contributor provides its Contributions) on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
    implied, including, without limitation, any warranties or conditions
    of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
    PARTICULAR PURPOSE. You are solely responsible for determining the
    appropriateness of using or redistributing the Work and assume any
    risks associated with Your exercise of permissions under this License.

8.  Limitation of Liability. In no event and under no legal theory,
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

9.  Accepting Warranty or Additional Liability. While redistributing
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

Copyright 2026 KONSTANTIN KOLOMEITSEV

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

## File: `skills/data-structure-protocol/SKILL.md`
```markdown
---
name: data-structure-protocol
description: >-
  Build and navigate DSP (Data Structure Protocol) — graph-based long-term structural memory of codebases for LLM agents.
  Stores entities (modules, functions), their dependencies (imports), public API (shared/exports), and reasons for every connection.
  Use when: (1) project has a .dsp/ directory, (2) user asks to set up DSP or bootstrap project structure,
  (3) creating/modifying/deleting code files in a DSP-tracked project, (4) navigating project structure, understanding dependencies,
  or finding modules, (5) user mentions DSP, dsp-cli, .dsp, or structure mapping.
---

# Data Structure Protocol (DSP)

DSP builds a dependency graph of project entities in a `.dsp/` directory. Each entity (module, function, external dependency) gets a UID, description, import list, and export index. The graph answers: what exists, why it exists, what depends on what, and who uses what.

**DSP is NOT documentation for humans or AST dump.** It captures _meaning_ (purpose), _boundaries_ (imports/exports), and _reasons for connections_ (why).

## Agent Prompt

Embed this context when working on a DSP-tracked project:

> **This project uses DSP (Data Structure Protocol).**
> The `.dsp/` directory is the entity graph of this project: modules, functions, dependencies, public API. It is your long-term memory of the code structure.
>
> **Core rules:**
>
> 1. **Before changing code** — find affected entities via `dsp-cli search`, `find-by-source`, or `read-toc`. Read their `description` and `imports` to understand context.
> 2. **When creating a file/module** — call `dsp-cli create-object`. For each exported function — `create-function` (with `--owner`). Register exports via `create-shared`.
> 3. **When adding an import** — call `dsp-cli add-import` with a brief `why`. For external dependencies — first `create-object --kind external` if the entity doesn't exist yet.
> 4. **When removing import / export / file** — call `remove-import`, `remove-shared`, `remove-entity` respectively. Cascade cleanup is automatic.
> 5. **When renaming/moving a file** — call `move-entity`. UID does not change.
> 6. **Don't touch DSP** if only internal implementation changed without affecting purpose or dependencies.
> 7. **Bootstrap** — if `.dsp/` is empty, traverse the project from root entrypoint via DFS on imports, documenting every file.
>
> **Key commands:**
> ```
> dsp-cli init
> dsp-cli create-object <source> <purpose> [--kind external] [--toc ROOT_UID]
> dsp-cli create-function <source> <purpose> [--owner UID] [--toc ROOT_UID]
> dsp-cli create-shared <exporter_uid> <shared_uid> [<shared_uid> ...]
> dsp-cli add-import <importer_uid> <imported_uid> <why> [--exporter UID]
> dsp-cli remove-import <importer_uid> <imported_uid> [--exporter UID]
> dsp-cli remove-shared <exporter_uid> <shared_uid>
> dsp-cli remove-entity <uid>
> dsp-cli move-entity <uid> <new_source>
> dsp-cli update-description <uid> [--source S] [--purpose P] [--kind K]
> dsp-cli get-entity <uid>
> dsp-cli get-children <uid> [--depth N]
> dsp-cli get-parents <uid> [--depth N]
> dsp-cli search <query>
> dsp-cli find-by-source <path>
> dsp-cli read-toc [--toc ROOT_UID]
> dsp-cli get-stats
> ```

## Using the CLI

The script is at `scripts/dsp-cli.py` relative to this skill directory.

```
python <skill-path>/scripts/dsp-cli.py [--root <project-root>] <command> [args]
```

`--root` defaults to current working directory. All paths in arguments are repo-relative.

## Core Concepts

- **Code = graph.** Nodes are Objects and Functions. Edges are `imports` and `shared/exports`.
- **Identity by UID, not file path.** Path is an attribute; renames/moves don't change UID.
- **"Shared" creates an entity.** If something becomes public (exported), it gets its own UID.
- **Import tracks both "from where" and "what".** One code import may create two DSP links: to the module and to the specific shared entity.
- **Full import coverage.** Every imported file/asset must be an Object in `.dsp` — code, images, styles, configs, everything.
- **`why` lives next to the imported entity** in its `exports/` directory (reverse index).
- **Start from roots.** Each root entrypoint has its own TOC file.
- **External deps — record only.** `kind: external`, no deep dive into `node_modules`/`site-packages`/etc. But `exports index` works — shows who imports it.

## UID Format

- Objects: `obj-<8 hex>` (e.g., `obj-a1b2c3d4`)
- Functions: `func-<8 hex>` (e.g., `func-7f3a9c12`)

UID marker in source code — comment `@dsp <uid>` before declaration:

```js
// @dsp func-7f3a9c12
export function calculateTotal(items) { ... }
```

```python
# @dsp obj-e5f6g7h8
class UserService:
```

## Workflows

### Setting Up DSP

1. Run `dsp-cli init` to create `.dsp/` directory.
2. Identify root entrypoint(s) — `package.json` main, framework entry, etc.
3. Run bootstrap (DFS from root). See [bootstrap.md](../../../core/security/QUARANTINE/vetted/repos/codymaster/commands/bootstrap.md).

### Creating Entities (when writing new code)

1. Create module: `dsp-cli create-object <path> <purpose>`
2. Create functions: `dsp-cli create-function <path>#<symbol> <purpose> --owner <module-uid>`
3. Register exports: `dsp-cli create-shared <module-uid> <func-uid> [<func-uid> ...]`
4. Register imports: `dsp-cli add-import <this-uid> <imported-uid> <why> [--exporter <module-uid>]`
5. External deps: `dsp-cli create-object <package-name> <purpose> --kind external`

### Navigating the Graph (when reading/understanding code)

- **Find entity by file**: `dsp-cli find-by-source <path>`
- **Search by keyword**: `dsp-cli search <query>`
- **Read TOC**: `dsp-cli read-toc` → get all UIDs, then `get-entity` for details
- **Dependency tree down**: `dsp-cli get-children <uid> --depth N`
- **Dependency tree up**: `dsp-cli get-parents <uid> --depth N`
- **Impact analysis**: `dsp-cli get-recipients <uid>` — who depends on this entity
- **Path between entities**: `dsp-cli get-path <from> <to>`

### Updating (when modifying code)

- Purpose changed: `dsp-cli update-description <uid> --purpose <new>`
- File moved: `dsp-cli move-entity <uid> <new-path>`
- Import reason changed: `dsp-cli update-import-why <importer> <imported> <new-why>`

### Deleting (when removing code)

- Import removed: `dsp-cli remove-import <importer> <imported> [--exporter UID]`
- Export removed: `dsp-cli remove-shared <exporter> <shared>`
- File/module deleted: `dsp-cli remove-entity <uid>` (cascading cleanup)

### Diagnostics

- `dsp-cli detect-cycles` — circular dependencies
- `dsp-cli get-orphans` — unused entities
- `dsp-cli get-stats` — project graph overview

## When to Update DSP

| Code Change | DSP Action |
|---|---|
| New file/module | `create-object` + `create-function` + `create-shared` + `add-import` |
| New import added | `add-import` (+ `create-object --kind external` if new external dep) |
| Import removed | `remove-import` |
| Export added | `create-shared` (+ `create-function` if new function) |
| Export removed | `remove-shared` |
| File renamed/moved | `move-entity` |
| File deleted | `remove-entity` |
| Purpose changed | `update-description` |
| Internal-only change | **No DSP update needed** |

## References

- **[Storage format](references/storage-format.md)** — `.dsp/` directory structure, file formats, TOC
- **[Bootstrap procedure](../../../core/security/QUARANTINE/vetted/repos/codymaster/commands/bootstrap.md)** — initial project markup (DFS algorithm)
- **[Operations reference](../corp/daily_briefs/operations.md)** — detailed semantics of all operations with import examples
```

## File: `skills/data-structure-protocol/references/bootstrap.md`
```markdown
# DSP Bootstrap Procedure

## Table of Contents

- [Overview](#overview)
- [Algorithm](#algorithm)
- [Step-by-Step](#step-by-step)
- [Visual Example](#visual-example)
- [Key Rules](#key-rules)

## Overview

Bootstrap is a DFS (depth-first search) traversal of dependencies from root entrypoint(s). Each reachable file gets documented as an entity in `.dsp/`. For each root — a separate TOC file.

## Algorithm

### Step 1: Identify Root Entrypoint(s)

- Auto-detect via LLM: `package.json` main, framework entry, `main.py`, `cmd/main.go`, etc.
- Or specify manually.
- Multiple roots → separate bootstrap per root, each with its own `TOC-<rootUid>`.

### Step 2: Document the Root File Completely

```
createObject(rootPath, rootPurpose)          → rootUid (first in TOC)
createFunction(path#symbol, purpose, rootUid) → funcUid (for each function)
createShared(rootUid, [funcUid, ...])         (for exports)
addImport(rootUid, importedUid, why)          (for each VERIFIED import)
createObject(pkgName, purpose, kind=external) (for external deps, add to TOC but don't descend)
```

**Root's description must include a brief project overview.**

#### Import Verification (REQUIRED for every import)

Before calling `addImport`, you MUST verify that the imported symbol is **actually used** in the file body (outside the `import` statement itself):

1. For each imported symbol (`import { Foo, Bar } from '...'`), search for `Foo` and `Bar` in the rest of the file (excluding the import line).
2. **If a symbol is NOT found in the file body** → it is a dead import. Do NOT register it in DSP. Remove it from the source code.
3. **If a symbol IS found** → write the `why` based on the **actual usage site in this specific file**, not by restating the imported entity's description/purpose.

The `why` must answer: **"what would break in THIS file if this import were removed?"**

```
BAD why:  "Quick action suggestion buttons"       ← copied from entity description
GOOD why: "Rendered below chat input as quick-reply options when AI responds"
                                                   ← describes actual usage in this file

BAD why:  "Animation library for React"            ← generic package description
GOOD why: "motion.div wraps stat cards for fade-in entry on scroll"
                                                   ← describes what specifically is animated
```

This step prevents phantom dependencies in the graph — imports that exist in code but serve no purpose.

### Step 3: Take First Non-External Import

From the current file's imports, pick the first one that is NOT an external dependency (not a library, not `node_modules`, not stdlib). Document it fully (same as Step 2). Add its UID to TOC.

### Step 4: Recursive Descent

From the just-documented file, take its first non-external import:
- If exists → document it, repeat Step 4 (go deeper).
- If none → **backtrack** to the previous level, take the next unprocessed non-external import.

### Step 5: Repeat Until Complete

Continue until all reachable non-external files are documented.

## Visual Example

```
root (document)
 ├─ import_A (local → document)
 │   ├─ import_A1 (local → document)
 │   │   └─ ... (descend deeper)
 │   ├─ import_A2 (external → record kind:external, DON'T descend)
 │   └─ import_A3 (local → document)
 │       └─ ... no local imports → backtrack
 ├─ import_B (local → document)
 │   └─ ...
 └─ import_C (external → record kind:external, DON'T descend)
```

## Key Rules

- Maintain a `visited` set by UID/sourceRef — no infinite recursion.
- External dependencies: `createObject(..., kind=external)` + add to TOC, but **never analyze their internals** (no `node_modules`, no `site-packages`, no `vendor`).
- After traversal, the TOC file contains a complete ordered list of all project entities.
- One file may contain multiple entities (Object + shared Functions) — all get separate UIDs.
- Place `@dsp <uid>` comment markers in source code before each entity declaration.
- **Never register an import without verifying the symbol is used in the file body.** See [Import Verification](#import-verification-required-for-every-import) in Step 2.
```

## File: `skills/data-structure-protocol/references/operations.md`
```markdown
# DSP Operations Reference

## Table of Contents

- [Create Operations](#create-operations)
- [Update Operations](#update-operations)
- [Delete Operations](#delete-operations)
- [Read Operations](#read-operations)
- [Graph Traversal](#graph-traversal)
- [Search and Discovery](#search-and-discovery)
- [Diagnostics](#diagnostics)
- [Import Patterns](#import-patterns)

## Create Operations

### createObject (§5.1)

```
dsp-cli create-object <source> <purpose> [--kind external] [--toc ROOT_UID]
```

Creates an Object entity (module, class, config, external dep).

Actions:
1. Generate `obj-<8hex>` UID
2. Create `.dsp/<uid>/` with `description`, empty `imports`, empty `shared`
3. Append UID to TOC

### createFunction (§5.2)

```
dsp-cli create-function <source> <purpose> [--owner UID] [--toc ROOT_UID]
```

Creates a Function entity.

Actions:
1. Generate `func-<8hex>` UID
2. Create `.dsp/<uid>/` with `description`, empty `imports`
3. If `--owner` specified:
   - Add funcUid to owner's `imports` (object "sees" its methods)
   - Create `.dsp/<funcUid>/exports/<ownerUid>` with "owner: method/member"
4. Append UID to TOC

### createShared (§5.3)

```
dsp-cli create-shared <exporter_uid> <shared_uid> [<shared_uid> ...]
```

Register entities as exported/public from an object.

Actions:
1. Append each shared_uid to `.dsp/<exporter>/shared`
2. Create `.dsp/<exporter>/exports/<shared_uid>/description` (auto-filled from entity's purpose)

### addImport (§5.4)

```
dsp-cli add-import <importer_uid> <imported_uid> <why> [--exporter UID]
```

Record an import relationship.

**Pre-condition — Verify before calling:**

Before registering ANY import, you MUST confirm the imported symbol is **actually used** in the importer's file body (outside the `import` statement):

1. Search for the imported symbol in the file body (excluding the import line itself).
2. **If NOT found** → dead import. Do NOT call `addImport`. Remove the import from source code instead.
3. **If found** → proceed, but write `why` based on the **actual usage site**, not by restating the imported entity's purpose/description.

The `why` parameter answers: **"what would break in THIS file if this import were removed?"** It must describe the concrete role the import plays in the importing file.

```
BAD:  "Animation library"                          ← restates entity description
GOOD: "motion.div wraps each stat card for staggered fade-in on viewport entry"

BAD:  "Quick action suggestion buttons"            ← restates entity description
GOOD: "Rendered as horizontal pill row below chat messages for one-tap AI queries"

BAD:  "React namespace for component typing"       ← generic, says nothing specific
GOOD: "useState manages sidebar collapsed state, useEffect syncs with localStorage"
```

Actions:
1. Append `imported_uid [via=exporter]` to importer's `imports`
2. Write reverse link:
   - With `--exporter`: `.dsp/<exporter>/exports/<imported_uid>/<importer_uid>` = why
   - Without: `.dsp/<imported_uid>/exports/<importer_uid>` = why

## Update Operations

### updateDescription (§5.5)

```
dsp-cli update-description <uid> [--source S] [--purpose P] [--kind K]
```

Update specific fields in entity's description. Unspecified fields remain unchanged.

### updateImportWhy (§5.6)

```
dsp-cli update-import-why <importer> <imported> <new_why> [--exporter UID]
```

Update the reason text for an existing import.

### moveEntity (§5.7)

```
dsp-cli move-entity <uid> <new_source>
```

Update source path after file rename/move. UID stays the same.

## Delete Operations

### removeImport (§5.8)

```
dsp-cli remove-import <importer> <imported> [--exporter UID]
```

Remove an import relationship. Deletes the line from `imports` and the reverse link from `exports/`.

### removeShared (§5.9)

```
dsp-cli remove-shared <exporter> <shared_uid>
```

Unregister a shared entity. Cascading:
1. Remove from `shared` file
2. Delete `exports/<shared_uid>/` directory with all recipients
3. Remove `shared_uid` from each recipient's `imports`

### removeEntity (§5.10)

```
dsp-cli remove-entity <uid>
```

Full entity removal with cascading cleanup:
1. Scan all entities' `imports` — remove lines referencing this uid (as imported or via=)
2. Clean outgoing links — remove reverse entries in other entities' `exports/`
3. Clean shared references — remove from any exporter's `shared` + delete `exports/<uid>/`
4. Remove uid from all TOC files
5. Delete `.dsp/<uid>/` directory

## Read Operations

### getEntity (§5.11)

```
dsp-cli get-entity <uid>
```

Full snapshot: description, imports, shared, exported_to.

### getShared (§5.12)

```
dsp-cli get-shared <uid>
```

Public API of entity — what it exports and who uses each export.

### getRecipients (§5.13)

```
dsp-cli get-recipients <uid>
```

All importers of this entity (three-level search: direct, via shared exporters, fallback by imports scan).

## Graph Traversal

### getChildren (§5.14)

```
dsp-cli get-children <uid> [--depth N]
```

Dependency tree downward (what this entity imports). Default depth=1, use `inf` for full tree.

### getParents (§5.15)

```
dsp-cli get-parents <uid> [--depth N]
```

Dependency tree upward (who imports this entity). Default depth=1, use `inf` for full tree.

### getPath (§5.16)

```
dsp-cli get-path <from_uid> <to_uid>
```

Shortest path between entities (BFS, bidirectional on imports/exports edges).

## Search and Discovery

### search (§5.17)

```
dsp-cli search <query>
```

Full-text search across `.dsp/` descriptions and export file names. Case-insensitive.

### findBySource (§5.18)

```
dsp-cli find-by-source <source_path>
```

Find entities by source file path. Returns multiple UIDs (one file may contain Object + shared Functions).

### readTOC (§5.19)

```
dsp-cli read-toc [--toc ROOT_UID]
```

Read table of contents. TOC[0] = root. Entry point for project overview.

## Diagnostics

### detectCycles (§5.20)

```
dsp-cli detect-cycles
```

Find circular dependencies in the import graph.

### getOrphans (§5.21)

```
dsp-cli get-orphans
```

Find entities not imported by anyone (except roots). Candidates for dead code.

### getStats (§5.22)

```
dsp-cli get-stats
```

Overview: entity counts (objects/functions/externals), imports, shared, cycles, orphans.

## Import Patterns

When to use one `addImport` vs two:

```js
// 1 call: named import only
import { UserService } from './services';
// → addImport(thisUid, userServiceUid, servicesObjUid, why="user management")

// 1 call: side-effect / default import
import './polyfills';
// → addImport(thisUid, polyfillsObjUid, why="browser polyfills")

import express from 'express';
// → addImport(thisUid, expressObjUid, why="HTTP framework")

// 2 calls: namespace + named from same module
import * as utils from './utils';
// → addImport(thisUid, utilsObjUid, why="formatting utilities")
import { calc } from './utils';
// → addImport(thisUid, calcUid, utilsObjUid, why="total calculation")
```

**Rule:** two calls when importing BOTH the module as a whole AND a specific symbol from it. One call otherwise.

### Dead Import Detection

An `import` statement in source code is NOT proof of a dependency. Code may contain unused imports (leftover from refactoring, copy-paste, or auto-imports).

**Before every `addImport` call:**
1. Find the imported symbol name (e.g., `Foo` from `import { Foo } from '...'`).
2. Search for `Foo` in the file body **excluding the import line**.
3. If zero matches → **dead import**. Do not register. Remove from source code.

This applies equally during bootstrap and during incremental updates. A phantom edge in the dependency graph is worse than a missing edge — it creates false coupling and misleads impact analysis.
```

## File: `skills/data-structure-protocol/references/storage-format.md`
```markdown
# DSP Storage Format

## Table of Contents

- [Directory Structure](#directory-structure)
- [Entity Directory](#entity-directory)
- [description File](#description-file)
- [imports File](#imports-file)
- [shared File](#shared-file)
- [exports/ Directory](#exports-directory)
- [TOC Files](#toc-files)

## Directory Structure

```
.dsp/
├── TOC                     # Table of contents (single root)
├── TOC-<rootUid>           # TOC per root (multi-root projects)
├── obj-a1b2c3d4/           # Object entity
│   ├── description         # source, kind, purpose
│   ├── imports             # list of imported UIDs
│   ├── shared              # list of exported UIDs
│   └── exports/            # reverse index (who imports this)
│       ├── <importer_uid>  # file: why this entity is imported
│       └── <shared_uid>/   # subdirectory per shared entity
│           ├── description # what is exported
│           └── <importer_uid>  # file: why this shared is imported
└── func-7f3a9c12/          # Function entity
    ├── description
    ├── imports
    └── exports/
        └── <owner_uid>     # file: "owner: method/member of this object"
```

## Entity Directory

Each entity gets `.dsp/<uid>/` where UID format is:

- `obj-<8 hex>` — objects (modules, classes, configs, externals)
- `func-<8 hex>` — functions (methods, handlers, pipelines)

Generated from first 8 chars of `uuid4().hex`.

## description File

```
source: <repo-relative-path>[#<symbol>]
kind: object|function|external
purpose: <1-3 sentences: what and why>
```

Optional extra sections (freeform): `notes:`, `contracts:`, etc.

**Root entrypoint rule:** root's `description` must include a brief project description (what the system is, main workflow, public API boundaries).

## imports File

One line per dependency:

```
<imported_uid>
```

Extended format (when imported via an exporter):

```
<imported_uid> via=<exporter_obj_uid>
```

Owner references (functions owned by objects) also appear here.

## shared File

One line per exported UID:

```
<shared_uid>
```

## exports/ Directory

Reverse index showing who imports this entity and why.

**Entity without shared** (Function, external, or Object imported wholesale):

```
exports/
└── <importer_uid>    # file content: "why imported" (1-3 sentences)
```

**Object with shared entities:**

```
exports/
├── <importer_uid>           # direct import of the whole object
└── <shared_uid>/            # subdirectory per shared entity
    ├── description          # what is exported (auto-filled from purpose)
    └── <importer_uid>       # why this specific shared is imported
```

This answers three questions:
1. **Who imports this entity** → `exports/<importer_uid>`
2. **What can be imported from it** → `shared` file
3. **Why a specific shared is imported** → `exports/<shared_uid>/<importer_uid>`

If the same shared-UID is re-exported from multiple objects (barrel exports), each exporter maintains its own exports index.

## TOC Files

**Naming:**
- `.dsp/TOC` — single root project
- `.dsp/TOC-<rootUid>` — multi-root project (one per root)

**Format:**

```
<uid_root>
<uid_2>
<uid_3>
...
```

**Rules:**
- TOC[0] is always the root entrypoint for this TOC
- Contains all entities reachable from this root, in documentation order
- Each UID appears exactly once per TOC
- Same entity may appear in multiple TOCs (if reachable from multiple roots)
- New entities are appended at the end
```

## File: `skills/data-structure-protocol/scripts/dsp-cli.py`
```python
#!/usr/bin/env python3
"""dsp-cli — Data Structure Protocol CLI.

Production-ready CLI for building and navigating DSP project graphs.
Used by LLM agents to maintain long-term structural memory of codebases.

Operations mirror ARCHITECTURE.md §5 exactly.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
import uuid
from collections import deque
from pathlib import Path

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Constants
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") not in ("utf8", "utf16"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
if sys.stderr.encoding and sys.stderr.encoding.lower().replace("-", "") not in ("utf8", "utf16"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]

DSP_DIR = ".dsp"
DESC_FILE = "description"
IMPORTS_FILE = "imports"
SHARED_FILE = "shared"
EXPORTS_DIR = "exports"
TOC_BASE = "TOC"

_MAX_DEPTH = 10**6


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Low-level helpers
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def _gen_uid(kind: str) -> str:
    prefix = "func" if kind == "function" else "obj"
    return f"{prefix}-{uuid.uuid4().hex[:8]}"


def _parse_import_line(line: str) -> tuple[str, str | None]:
    parts = line.split()
    if not parts:
        return "", None
    uid = parts[0]
    via: str | None = None
    for p in parts[1:]:
        if p.startswith("via="):
            via = p[4:]
    return uid, via


def _format_import_line(uid: str, via: str | None) -> str:
    return f"{uid} via={via}" if via else uid


def _read_lines(path: Path) -> list[str]:
    if not path.exists():
        return []
    return [ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()]


def _write_lines(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def _append_line_unique(path: Path, line: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    existing = _read_lines(path)
    if line not in existing:
        existing.append(line)
        _write_lines(path, existing)


def _remove_line_value(path: Path, target: str) -> bool:
    lines = _read_lines(path)
    new = [ln for ln in lines if ln != target]
    changed = len(new) != len(lines)
    _write_lines(path, new)
    return changed


def _read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8").strip()


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def _safe_unlink(path: Path) -> None:
    if path.exists() and path.is_file():
        path.unlink()


def _safe_rmtree(path: Path) -> None:
    if path.exists() and path.is_dir():
        shutil.rmtree(path)


def _fail(msg: str) -> None:
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(1)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Description parsing / serialization
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

_DESC_KEY_RE = re.compile(r"^([a-z_]+):\s?(.*)", re.DOTALL)
_DESC_ORDERED = ("source", "kind", "purpose")


def _parse_desc(text: str) -> dict[str, str]:
    result: dict[str, str] = {}
    cur_key: str | None = None
    cur_lines: list[str] = []
    for raw in text.splitlines():
        m = _DESC_KEY_RE.match(raw)
        if m:
            if cur_key is not None:
                result[cur_key] = "\n".join(cur_lines).strip()
            cur_key = m.group(1)
            cur_lines = [m.group(2)]
        elif cur_key is not None:
            cur_lines.append(raw)
    if cur_key is not None:
        result[cur_key] = "\n".join(cur_lines).strip()
    return result


def _serialize_desc(fields: dict[str, str]) -> str:
    lines: list[str] = []
    for k in _DESC_ORDERED:
        if k in fields:
            lines.append(f"{k}: {fields[k]}")
    for k, v in fields.items():
        if k not in _DESC_ORDERED:
            lines.append(f"{k}: {v}")
    return "\n".join(lines)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Store — filesystem abstraction over .dsp/
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class Store:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.base = self.root / DSP_DIR

    # ── guards ──

    def ensure_init(self) -> None:
        if not self.base.is_dir():
            _fail(f"directory {self.base} not found — run 'init' first")

    def entity_exists(self, uid: str) -> bool:
        return (self.base / uid).is_dir()

    def require_entity(self, uid: str) -> None:
        if not self.entity_exists(uid):
            _fail(f"entity {uid} does not exist")

    # ── uid enumeration ──

    def all_uids(self) -> list[str]:
        if not self.base.is_dir():
            return []
        return sorted(
            d.name
            for d in self.base.iterdir()
            if d.is_dir() and (d.name.startswith("obj-") or d.name.startswith("func-"))
        )

    # ── TOC ──

    def toc_path(self, root_uid: str | None = None) -> Path:
        if root_uid:
            return self.base / f"{TOC_BASE}-{root_uid}"
        return self.base / TOC_BASE

    def all_toc_paths(self) -> list[Path]:
        if not self.base.is_dir():
            return []
        return sorted(p for p in self.base.iterdir() if p.is_file() and p.name.startswith(TOC_BASE))

    # ── description ──

    def desc_path(self, uid: str) -> Path:
        return self.base / uid / DESC_FILE

    def read_desc(self, uid: str) -> dict[str, str]:
        return _parse_desc(_read_text(self.desc_path(uid)))

    def write_desc(self, uid: str, fields: dict[str, str]) -> None:
        _write_text(self.desc_path(uid), _serialize_desc(fields))

    # ── imports ──

    def imports_path(self, uid: str) -> Path:
        return self.base / uid / IMPORTS_FILE

    def read_imports(self, uid: str) -> list[tuple[str, str | None]]:
        return [_parse_import_line(ln) for ln in _read_lines(self.imports_path(uid)) if ln]

    def read_import_uids(self, uid: str) -> list[str]:
        return [i[0] for i in self.read_imports(uid) if i[0]]

    # ── shared ──

    def shared_path(self, uid: str) -> Path:
        return self.base / uid / SHARED_FILE

    def read_shared(self, uid: str) -> list[str]:
        return _read_lines(self.shared_path(uid))

    # ── exports ──

    def exports_dir(self, uid: str) -> Path:
        return self.base / uid / EXPORTS_DIR

    def read_direct_recipients(self, uid: str) -> list[tuple[str, str]]:
        d = self.exports_dir(uid)
        if not d.is_dir():
            return []
        return [(e.name, _read_text(e)) for e in sorted(d.iterdir()) if e.is_file()]

    def read_shared_recipients(self, uid: str) -> dict[str, list[tuple[str, str]]]:
        d = self.exports_dir(uid)
        if not d.is_dir():
            return {}
        result: dict[str, list[tuple[str, str]]] = {}
        for entry in sorted(d.iterdir()):
            if entry.is_dir():
                recs: list[tuple[str, str]] = []
                for f in sorted(entry.iterdir()):
                    if f.is_file() and f.name != DESC_FILE:
                        recs.append((f.name, _read_text(f)))
                result[entry.name] = recs
        return result

    def read_shared_export_desc(self, uid: str, shared_uid: str) -> str:
        return _read_text(self.exports_dir(uid) / shared_uid / DESC_FILE)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Engine — all DSP operations (ARCHITECTURE.md §5)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class Engine:
    def __init__(self, store: Store):
        self.s = store

    # ── init ──

    def init(self) -> None:
        self.s.base.mkdir(parents=True, exist_ok=True)
        print(f"initialized {self.s.base}")

    # ── §5.1 createObject ──

    def create_object(
        self, source: str, purpose: str, kind: str = "object", toc: str | None = None
    ) -> str:
        self.s.ensure_init()
        uid = _gen_uid("object")
        (self.s.base / uid).mkdir(parents=True)
        self.s.write_desc(uid, {"source": source, "kind": kind, "purpose": purpose})
        _write_lines(self.s.imports_path(uid), [])
        _write_lines(self.s.shared_path(uid), [])
        _append_line_unique(self.s.toc_path(toc), uid)
        return uid

    # ── §5.2 createFunction ──

    def create_function(
        self, source: str, purpose: str, owner: str | None = None, toc: str | None = None
    ) -> str:
        self.s.ensure_init()
        uid = _gen_uid("function")
        (self.s.base / uid).mkdir(parents=True)
        self.s.write_desc(uid, {"source": source, "kind": "function", "purpose": purpose})
        _write_lines(self.s.imports_path(uid), [])
        if owner:
            self.s.require_entity(owner)
            _append_line_unique(self.s.imports_path(owner), uid)
            exp = self.s.exports_dir(uid)
            exp.mkdir(parents=True, exist_ok=True)
            _write_text(exp / owner, "owner: method/member of this object")
        _append_line_unique(self.s.toc_path(toc), uid)
        return uid

    # ── §5.3 createShared ──

    def create_shared(self, exporter: str, shared_uids: list[str]) -> None:
        self.s.ensure_init()
        self.s.require_entity(exporter)
        exp_dir = self.s.exports_dir(exporter)
        exp_dir.mkdir(parents=True, exist_ok=True)
        for sid in shared_uids:
            _append_line_unique(self.s.shared_path(exporter), sid)
            shared_sub = exp_dir / sid
            shared_sub.mkdir(parents=True, exist_ok=True)
            desc_path = shared_sub / DESC_FILE
            if not desc_path.exists():
                purpose = ""
                if self.s.entity_exists(sid):
                    purpose = self.s.read_desc(sid).get("purpose", "")
                _write_text(desc_path, purpose if purpose else sid)

    # ── §5.4 addImport ──

    def add_import(
        self, importer: str, imported: str, why: str, exporter: str | None = None
    ) -> None:
        self.s.ensure_init()
        self.s.require_entity(importer)
        line = _format_import_line(imported, exporter)
        _append_line_unique(self.s.imports_path(importer), line)
        if exporter:
            self.s.require_entity(exporter)
            rev_dir = self.s.exports_dir(exporter) / imported
            rev_dir.mkdir(parents=True, exist_ok=True)
            _write_text(rev_dir / importer, why)
        else:
            self.s.require_entity(imported)
            exp = self.s.exports_dir(imported)
            exp.mkdir(parents=True, exist_ok=True)
            _write_text(exp / importer, why)

    # ── §5.5 updateDescription ──

    def update_description(self, uid: str, fields: dict[str, str]) -> None:
        self.s.ensure_init()
        self.s.require_entity(uid)
        current = self.s.read_desc(uid)
        current.update(fields)
        self.s.write_desc(uid, current)

    # ── §5.6 updateImportWhy ──

    def update_import_why(
        self, importer: str, imported: str, new_why: str, exporter: str | None = None
    ) -> None:
        self.s.ensure_init()
        if exporter:
            path = self.s.exports_dir(exporter) / imported / importer
        else:
            path = self.s.exports_dir(imported) / importer
        if not path.exists():
            _fail(f"reverse entry not found: {imported} ← {importer}" + (f" via {exporter}" if exporter else ""))
        _write_text(path, new_why)

    # ── §5.7 moveEntity ──

    def move_entity(self, uid: str, new_source: str) -> None:
        self.s.ensure_init()
        self.s.require_entity(uid)
        desc = self.s.read_desc(uid)
        desc["source"] = new_source
        self.s.write_desc(uid, desc)

    # ── §5.8 removeImport ──

    def remove_import(self, importer: str, imported: str, exporter: str | None = None) -> None:
        self.s.ensure_init()
        self.s.require_entity(importer)
        imports = self.s.read_imports(importer)
        new_lines: list[str] = []
        removed = False
        for imp_uid, imp_via in imports:
            if imp_uid == imported and not removed:
                if exporter is None or imp_via == exporter:
                    removed = True
                    continue
            new_lines.append(_format_import_line(imp_uid, imp_via))
        _write_lines(self.s.imports_path(importer), new_lines)
        if exporter:
            _safe_unlink(self.s.exports_dir(exporter) / imported / importer)
        else:
            _safe_unlink(self.s.exports_dir(imported) / importer)

    # ── §5.9 removeShared ──

    def remove_shared(self, exporter: str, shared_uid: str) -> None:
        self.s.ensure_init()
        self.s.require_entity(exporter)
        _remove_line_value(self.s.shared_path(exporter), shared_uid)
        shared_dir = self.s.exports_dir(exporter) / shared_uid
        if shared_dir.is_dir():
            for entry in list(shared_dir.iterdir()):
                if entry.is_file() and entry.name != DESC_FILE:
                    recipient_uid = entry.name
                    if self.s.entity_exists(recipient_uid):
                        imports = self.s.read_imports(recipient_uid)
                        new_lines = [
                            _format_import_line(u, v)
                            for u, v in imports
                            if not (u == shared_uid and v == exporter)
                        ]
                        _write_lines(self.s.imports_path(recipient_uid), new_lines)
            _safe_rmtree(shared_dir)

    # ── §5.10 removeEntity ──

    def remove_entity(self, uid: str) -> None:
        self.s.ensure_init()
        self.s.require_entity(uid)

        all_uids = self.s.all_uids()

        for other in all_uids:
            if other == uid:
                continue
            imports = self.s.read_imports(other)
            had = any(u == uid or v == uid for u, v in imports)
            if had:
                new_lines = [
                    _format_import_line(u, v)
                    for u, v in imports
                    if u != uid and v != uid
                ]
                _write_lines(self.s.imports_path(other), new_lines)

        for imp_uid, imp_via in self.s.read_imports(uid):
            if imp_via:
                _safe_unlink(self.s.exports_dir(imp_via) / imp_uid / uid)
            else:
                _safe_unlink(self.s.exports_dir(imp_uid) / uid)

        for other in all_uids:
            if other == uid:
                continue
            shared = self.s.read_shared(other)
            if uid in shared:
                _remove_line_value(self.s.shared_path(other), uid)
                _safe_rmtree(self.s.exports_dir(other) / uid)

        for toc in self.s.all_toc_paths():
            _remove_line_value(toc, uid)

        _safe_rmtree(self.s.base / uid)

    # ── §5.11 getEntity ──

    def get_entity(self, uid: str) -> dict:
        self.s.ensure_init()
        self.s.require_entity(uid)
        desc = self.s.read_desc(uid)
        imports = self.s.read_imports(uid)
        shared = self.s.read_shared(uid)
        recipients = self._all_importers(uid)
        return {
            "uid": uid,
            "description": desc,
            "imports": imports,
            "shared": shared,
            "exported_to": recipients,
        }

    # ── §5.12 getShared ──

    def get_shared(self, uid: str) -> list[dict]:
        self.s.ensure_init()
        self.s.require_entity(uid)
        shared_uids = self.s.read_shared(uid)
        result: list[dict] = []
        for sid in shared_uids:
            desc = self.s.read_shared_export_desc(uid, sid)
            recs: list[tuple[str, str]] = []
            sub = self.s.exports_dir(uid) / sid
            if sub.is_dir():
                for f in sorted(sub.iterdir()):
                    if f.is_file() and f.name != DESC_FILE:
                        recs.append((f.name, _read_text(f)))
            result.append({"shared_uid": sid, "description": desc, "recipients": recs})
        return result

    # ── §5.13 getRecipients ──

    def get_recipients(self, uid: str) -> list[tuple[str, str]]:
        self.s.ensure_init()
        self.s.require_entity(uid)
        return self._all_importers(uid)

    def _all_importers(self, uid: str) -> list[tuple[str, str]]:
        seen: set[str] = set()
        result: list[tuple[str, str]] = []

        for rec_uid, why in self.s.read_direct_recipients(uid):
            if rec_uid not in seen:
                result.append((rec_uid, why))
                seen.add(rec_uid)

        for other in self.s.all_uids():
            if uid in self.s.read_shared(other):
                sub = self.s.exports_dir(other) / uid
                if sub.is_dir():
                    for f in sorted(sub.iterdir()):
                        if f.is_file() and f.name != DESC_FILE and f.name not in seen:
                            result.append((f.name, _read_text(f)))
                            seen.add(f.name)

        for other in self.s.all_uids():
            if other in seen:
                continue
            for imp_uid, _ in self.s.read_imports(other):
                if imp_uid == uid:
                    result.append((other, ""))
                    seen.add(other)
                    break

        return result

    # ── §5.14 getChildren ──

    def get_children(self, uid: str, depth: int = 1) -> dict:
        self.s.ensure_init()
        self.s.require_entity(uid)
        visited: set[str] = set()

        def walk(u: str, d: int) -> dict:
            desc = self.s.read_desc(u) if self.s.entity_exists(u) else {}
            node: dict = {
                "uid": u,
                "kind": desc.get("kind", ""),
                "purpose": desc.get("purpose", ""),
                "children": [],
            }
            if u in visited:
                node["cycle"] = True
                return node
            visited.add(u)
            if d > 0:
                for imp_uid, _ in self.s.read_imports(u):
                    node["children"].append(walk(imp_uid, d - 1))
            return node

        return walk(uid, depth)

    # ── §5.15 getParents ──

    def get_parents(self, uid: str, depth: int = 1) -> dict:
        self.s.ensure_init()
        self.s.require_entity(uid)
        visited: set[str] = set()

        def walk(u: str, d: int) -> dict:
            desc = self.s.read_desc(u) if self.s.entity_exists(u) else {}
            node: dict = {
                "uid": u,
                "kind": desc.get("kind", ""),
                "purpose": desc.get("purpose", ""),
                "parents": [],
            }
            if u in visited:
                node["cycle"] = True
                return node
            visited.add(u)
            if d > 0:
                for rec_uid, why in self._all_importers(u):
                    child = walk(rec_uid, d - 1)
                    child["why"] = why
                    node["parents"].append(child)
            return node

        return walk(uid, depth)

    # ── §5.16 getPath ──

    def get_path(self, from_uid: str, to_uid: str) -> list[str] | None:
        self.s.ensure_init()
        self.s.require_entity(from_uid)
        self.s.require_entity(to_uid)
        if from_uid == to_uid:
            return [from_uid]

        visited: set[str] = {from_uid}
        queue: deque[tuple[str, list[str]]] = deque([(from_uid, [from_uid])])

        while queue:
            current, path = queue.popleft()
            neighbors: set[str] = set()
            for imp_uid, _ in self.s.read_imports(current):
                neighbors.add(imp_uid)
            for rec_uid, _ in self._all_importers(current):
                neighbors.add(rec_uid)
            for nb in sorted(neighbors):
                if nb == to_uid:
                    return path + [nb]
                if nb not in visited and self.s.entity_exists(nb):
                    visited.add(nb)
                    queue.append((nb, path + [nb]))
        return None

    # ── §5.17 search ──

    def search(self, query: str) -> list[dict]:
        self.s.ensure_init()
        q = query.lower()
        results: list[dict] = []
        for uid in self.s.all_uids():
            desc = self.s.read_desc(uid)
            for field, value in desc.items():
                if q in value.lower():
                    results.append({"uid": uid, "field": field, "match": value})
                    break
            else:
                exp = self.s.exports_dir(uid)
                if exp.is_dir():
                    for entry in exp.iterdir():
                        if q in entry.name.lower():
                            results.append({"uid": uid, "field": "exports", "match": entry.name})
                            break
        return results

    # ── §5.18 findBySource ──

    def find_by_source(self, source_path: str) -> list[str]:
        self.s.ensure_init()
        found: list[str] = []
        normalized = source_path.replace("\\", "/")
        for uid in self.s.all_uids():
            desc = self.s.read_desc(uid)
            src = desc.get("source", "").replace("\\", "/")
            if src == normalized or src.startswith(normalized + "#"):
                found.append(uid)
        return found

    # ── §5.19 readTOC ──

    def read_toc(self, root_uid: str | None = None) -> list[str]:
        self.s.ensure_init()
        toc = self.s.toc_path(root_uid)
        if not toc.exists():
            _fail(f"TOC file not found: {toc.name}")
        return _read_lines(toc)

    # ── §5.20 detectCycles ──

    def detect_cycles(self) -> list[list[str]]:
        self.s.ensure_init()
        WHITE, GRAY, BLACK = 0, 1, 2
        color: dict[str, int] = {}
        path_stack: list[str] = []
        cycles: list[list[str]] = []
        all_uids = self.s.all_uids()
        for u in all_uids:
            color[u] = WHITE

        def dfs(u: str) -> None:
            color[u] = GRAY
            path_stack.append(u)
            for imp_uid in self.s.read_import_uids(u):
                c = color.get(imp_uid, -1)
                if c == GRAY:
                    idx = path_stack.index(imp_uid)
                    cycles.append(path_stack[idx:] + [imp_uid])
                elif c == WHITE:
                    dfs(imp_uid)
            path_stack.pop()
            color[u] = BLACK

        for u in all_uids:
            if color[u] == WHITE:
                dfs(u)
        return cycles

    # ── §5.21 getOrphans ──

    def get_orphans(self) -> list[str]:
        self.s.ensure_init()
        roots: set[str] = set()
        for toc in self.s.all_toc_paths():
            lines = _read_lines(toc)
            if lines:
                roots.add(lines[0])

        imported_uids: set[str] = set()
        for uid in self.s.all_uids():
            for imp_uid, imp_via in self.s.read_imports(uid):
                if imp_uid:
                    imported_uids.add(imp_uid)
                if imp_via:
                    imported_uids.add(imp_via)

        orphans: list[str] = []
        for uid in self.s.all_uids():
            if uid in roots:
                continue
            if uid in imported_uids:
                continue
            exp = self.s.exports_dir(uid)
            if exp.is_dir() and any(True for _ in exp.iterdir()):
                continue
            orphans.append(uid)
        return orphans

    # ── §5.22 getStats ──

    def get_stats(self) -> dict:
        self.s.ensure_init()
        uids = self.s.all_uids()
        objects = functions = externals = total_imports = total_shared = 0
        for uid in uids:
            desc = self.s.read_desc(uid)
            kind = desc.get("kind", "object")
            if kind == "external":
                externals += 1
            elif kind == "function":
                functions += 1
            else:
                objects += 1
            total_imports += len(self.s.read_import_uids(uid))
            total_shared += len(self.s.read_shared(uid))
        cycles = self.detect_cycles()
        orphans = self.get_orphans()
        return {
            "entities": len(uids),
            "objects": objects,
            "functions": functions,
            "externals": externals,
            "imports": total_imports,
            "shared": total_shared,
            "cycles": len(cycles),
            "orphans": len(orphans),
        }


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Output formatting
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def _kind_tag(kind: str) -> str:
    if kind and kind not in ("object",):
        return f" [{kind}]"
    return ""


def _print_tree(node: dict, key: str = "children") -> None:
    kt = _kind_tag(node.get("kind", ""))
    why_s = f"  (why: {node['why']})" if node.get("why") else ""
    print(f"{node['uid']}{kt}: {node.get('purpose', '')}{why_s}")
    children = node.get(key, [])
    for i, child in enumerate(children):
        _print_subtree(child, "", i == len(children) - 1, key)


def _print_subtree(node: dict, prefix: str, is_last: bool, key: str) -> None:
    conn = "\u2514\u2500\u2500 " if is_last else "\u251c\u2500\u2500 "
    kt = _kind_tag(node.get("kind", ""))
    cycle_mark = " \u21bb" if node.get("cycle") else ""
    why_s = f"  (why: {node['why']})" if node.get("why") else ""
    print(f"{prefix}{conn}{node['uid']}{kt}{cycle_mark}: {node.get('purpose', '')}{why_s}")
    if node.get("cycle"):
        return
    children = node.get(key, [])
    for i, child in enumerate(children):
        ext = "    " if is_last else "\u2502   "
        _print_subtree(child, prefix + ext, i == len(children) - 1, key)


def _print_entity(info: dict) -> None:
    desc = info["description"]
    print(f"uid: {info['uid']}")
    print(f"source: {desc.get('source', '')}")
    print(f"kind: {desc.get('kind', '')}")
    print(f"purpose: {desc.get('purpose', '')}")
    for k, v in desc.items():
        if k not in ("source", "kind", "purpose"):
            print(f"{k}: {v}")

    imp = info["imports"]
    if imp:
        print("\nimports:")
        for uid, via in imp:
            line = f"  {uid}"
            if via:
                line += f" via={via}"
            print(line)

    shared = info["shared"]
    if shared:
        print("\nshared:")
        for s in shared:
            print(f"  {s}")

    exp = info["exported_to"]
    if exp:
        print("\nexported to:")
        for rec_uid, why in exp:
            print(f"  {rec_uid}: {why}" if why else f"  {rec_uid}")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CLI definition
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def _depth_type(value: str) -> int:
    if value.lower() in ("inf", "infinity", "all"):
        return _MAX_DEPTH
    n = int(value)
    if n < 0:
        raise argparse.ArgumentTypeError("depth must be >= 0")
    return n


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="dsp-cli", description="Data Structure Protocol CLI")
    p.add_argument("--root", default=".", help="project root directory (default: cwd)")
    sub = p.add_subparsers(dest="command")
    sub.required = True

    # ── init ──
    sub.add_parser("init", help="initialize .dsp directory")

    # ── create-object ──
    sp = sub.add_parser("create-object", help="§5.1 create an Object entity")
    sp.add_argument("source", help="repo-relative source path")
    sp.add_argument("purpose", help="1-3 sentences: what and why")
    sp.add_argument("--kind", default="object", choices=["object", "external"], help="entity kind")
    sp.add_argument("--toc", default=None, metavar="ROOT_UID", help="TOC root uid (multi-root)")

    # ── create-function ──
    sp = sub.add_parser("create-function", help="§5.2 create a Function entity")
    sp.add_argument("source", help="repo-relative source path (with #symbol if needed)")
    sp.add_argument("purpose", help="1-3 sentences: what and why")
    sp.add_argument("--owner", default=None, metavar="UID", help="owner Object uid")
    sp.add_argument("--toc", default=None, metavar="ROOT_UID", help="TOC root uid (multi-root)")

    # ── create-shared ──
    sp = sub.add_parser("create-shared", help="§5.3 register shared/exported entities")
    sp.add_argument("exporter", help="exporter Object uid")
    sp.add_argument("shared", nargs="+", help="uid(s) of shared entities")

    # ── add-import ──
    sp = sub.add_parser("add-import", help="§5.4 add an import relationship")
    sp.add_argument("importer", help="importer entity uid")
    sp.add_argument("imported", help="imported entity uid")
    sp.add_argument("why", help="1-3 sentences: why this is imported")
    sp.add_argument("--exporter", default=None, metavar="UID", help="exporter Object uid (for shared imports)")

    # ── update-description ──
    sp = sub.add_parser("update-description", help="§5.5 update entity description fields")
    sp.add_argument("uid", help="entity uid")
    sp.add_argument("--source", default=None, dest="new_source")
    sp.add_argument("--purpose", default=None, dest="new_purpose")
    sp.add_argument("--kind", default=None, dest="new_kind")

    # ── update-import-why ──
    sp = sub.add_parser("update-import-why", help="§5.6 update import reason text")
    sp.add_argument("importer", help="importer entity uid")
    sp.add_argument("imported", help="imported entity uid")
    sp.add_argument("why", help="new reason text")
    sp.add_argument("--exporter", default=None, metavar="UID")

    # ── move-entity ──
    sp = sub.add_parser("move-entity", help="§5.7 update source path after rename/move")
    sp.add_argument("uid", help="entity uid")
    sp.add_argument("new_source", help="new repo-relative source path")

    # ── remove-import ──
    sp = sub.add_parser("remove-import", help="§5.8 remove an import relationship")
    sp.add_argument("importer", help="importer entity uid")
    sp.add_argument("imported", help="imported entity uid")
    sp.add_argument("--exporter", default=None, metavar="UID")

    # ── remove-shared ──
    sp = sub.add_parser("remove-shared", help="§5.9 unregister a shared entity")
    sp.add_argument("exporter", help="exporter Object uid")
    sp.add_argument("shared", help="shared entity uid")

    # ── remove-entity ──
    sp = sub.add_parser("remove-entity", help="§5.10 remove entity and all references")
    sp.add_argument("uid", help="entity uid to remove")

    # ── get-entity ──
    sp = sub.add_parser("get-entity", help="§5.11 get full entity snapshot")
    sp.add_argument("uid", help="entity uid")

    # ── get-shared ──
    sp = sub.add_parser("get-shared", help="§5.12 get public API of entity")
    sp.add_argument("uid", help="entity uid")

    # ── get-recipients ──
    sp = sub.add_parser("get-recipients", help="§5.13 get all importers of entity")
    sp.add_argument("uid", help="entity uid")

    # ── get-children ──
    sp = sub.add_parser("get-children", help="§5.14 import tree downward")
    sp.add_argument("uid", help="entity uid")
    sp.add_argument("--depth", type=_depth_type, default=1, help="traversal depth (default 1, 'inf' for full)")

    # ── get-parents ──
    sp = sub.add_parser("get-parents", help="§5.15 import tree upward")
    sp.add_argument("uid", help="entity uid")
    sp.add_argument("--depth", type=_depth_type, default=1, help="traversal depth (default 1, 'inf' for full)")

    # ── get-path ──
    sp = sub.add_parser("get-path", help="§5.16 shortest path between entities")
    sp.add_argument("from_uid", help="start entity uid")
    sp.add_argument("to_uid", help="end entity uid")

    # ── search ──
    sp = sub.add_parser("search", help="§5.17 full-text search across .dsp")
    sp.add_argument("query", help="search query (case-insensitive substring)")

    # ── find-by-source ──
    sp = sub.add_parser("find-by-source", help="§5.18 find entity by source file path")
    sp.add_argument("source_path", help="repo-relative source path")

    # ── read-toc ──
    sp = sub.add_parser("read-toc", help="§5.19 read table of contents")
    sp.add_argument("--toc", default=None, metavar="ROOT_UID", help="TOC root uid (multi-root)")

    # ── detect-cycles ──
    sub.add_parser("detect-cycles", help="§5.20 find circular dependencies")

    # ── get-orphans ──
    sub.add_parser("get-orphans", help="§5.21 find unused entities")

    # ── get-stats ──
    sub.add_parser("get-stats", help="§5.22 project graph statistics")

    return p


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Dispatch
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()
    root = Path(args.root).resolve()
    store = Store(root)
    engine = Engine(store)
    cmd = args.command

    if cmd == "init":
        engine.init()

    elif cmd == "create-object":
        uid = engine.create_object(args.source, args.purpose, args.kind, args.toc)
        print(uid)

    elif cmd == "create-function":
        uid = engine.create_function(args.source, args.purpose, args.owner, args.toc)
        print(uid)

    elif cmd == "create-shared":
        engine.create_shared(args.exporter, args.shared)
        print("ok")

    elif cmd == "add-import":
        engine.add_import(args.importer, args.imported, args.why, args.exporter)
        print("ok")

    elif cmd == "update-description":
        fields: dict[str, str] = {}
        if args.new_source is not None:
            fields["source"] = args.new_source
        if args.new_purpose is not None:
            fields["purpose"] = args.new_purpose
        if args.new_kind is not None:
            fields["kind"] = args.new_kind
        if not fields:
            _fail("provide at least one field to update (--source, --purpose, --kind)")
        engine.update_description(args.uid, fields)
        print("ok")

    elif cmd == "update-import-why":
        engine.update_import_why(args.importer, args.imported, args.why, args.exporter)
        print("ok")

    elif cmd == "move-entity":
        engine.move_entity(args.uid, args.new_source)
        print("ok")

    elif cmd == "remove-import":
        engine.remove_import(args.importer, args.imported, args.exporter)
        print("ok")

    elif cmd == "remove-shared":
        engine.remove_shared(args.exporter, args.shared)
        print("ok")

    elif cmd == "remove-entity":
        engine.remove_entity(args.uid)
        print("ok")

    elif cmd == "get-entity":
        info = engine.get_entity(args.uid)
        _print_entity(info)

    elif cmd == "get-shared":
        items = engine.get_shared(args.uid)
        if not items:
            print("no shared entities")
        for item in items:
            print(f"\n{item['shared_uid']}:")
            print(f"  description: {item['description']}")
            if item["recipients"]:
                print("  imported by:")
                for rec_uid, why in item["recipients"]:
                    print(f"    {rec_uid}: {why}" if why else f"    {rec_uid}")

    elif cmd == "get-recipients":
        recs = engine.get_recipients(args.uid)
        if not recs:
            print("no recipients")
        for rec_uid, why in recs:
            print(f"{rec_uid}: {why}" if why else rec_uid)

    elif cmd == "get-children":
        tree = engine.get_children(args.uid, args.depth)
        _print_tree(tree, key="children")

    elif cmd == "get-parents":
        tree = engine.get_parents(args.uid, args.depth)
        _print_tree(tree, key="parents")

    elif cmd == "get-path":
        path = engine.get_path(args.from_uid, args.to_uid)
        if path is None:
            print("no path found")
            sys.exit(1)
        print(" -> ".join(path))

    elif cmd == "search":
        results = engine.search(args.query)
        if not results:
            print("no matches")
        for r in results:
            print(f"{r['uid']}  [{r['field']}] {r['match']}")

    elif cmd == "find-by-source":
        found = engine.find_by_source(args.source_path)
        if not found:
            print("not found")
            sys.exit(1)
        for uid in found:
            print(uid)

    elif cmd == "read-toc":
        uids = engine.read_toc(args.toc)
        for i, uid in enumerate(uids):
            tag = " [root]" if i == 0 else ""
            print(f"{uid}{tag}")

    elif cmd == "detect-cycles":
        cycles = engine.detect_cycles()
        if not cycles:
            print("no cycles detected")
        for i, cycle in enumerate(cycles, 1):
            print(f"cycle {i}: {' -> '.join(cycle)}")

    elif cmd == "get-orphans":
        orphans = engine.get_orphans()
        if not orphans:
            print("no orphans")
        for uid in orphans:
            print(uid)

    elif cmd == "get-stats":
        stats = engine.get_stats()
        print(f"entities:  {stats['entities']}")
        print(f"  objects:   {stats['objects']}")
        print(f"  functions: {stats['functions']}")
        print(f"  external:  {stats['externals']}")
        print(f"imports:   {stats['imports']}")
        print(f"shared:    {stats['shared']}")
        print(f"cycles:    {stats['cycles']}")
        print(f"orphans:   {stats['orphans']}")


if __name__ == "__main__":
    main()
```

